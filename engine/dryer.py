"""
ExergyLab - Dryer Exergy Analysis

Kurutma fırını exergy hesaplamaları.
Konveyörlü, döner, spreyli, akışkan yataklı ve raflı kurutucular için.
"""

from dataclasses import dataclass
from typing import Optional
import math

import dataclasses

from .core import (
    DeadState, ExergyResult, compute_avoidable_split,
    celsius_to_kelvin,
    heat_exergy, CP_AIR
)


# Sabitler
H_FG_100C = 2257.0
CP_WATER_VAPOR = 1.87       # kJ/kg·K
CP_WATER = 4.18             # kJ/kg·K


def _get_hfg(T_C: float) -> float:
    """Buharlaşma entalpisi [kJ/kg] — lineer yaklaşım"""
    return max(2501 - 2.36 * T_C, 1800)


# Kurutucu tip verimi referansları (1. yasa termal verim)
# Best-achievable parameters per dryer type (Tsatsaronis & Morosuk 2008)
UNAVOIDABLE_REF_DRYER = {
    'conveyor':      {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 60.0},
    'rotary':        {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 55.0},
    'spray':         {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 70.0},
    'fluidized_bed': {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 55.0},
    'tray':          {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 60.0},
    'drum':          {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 55.0},
    'infrared':      {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 50.0},
    'microwave':     {'fuel_efficiency': 0.95, 'air_outlet_temp_C': 50.0},
}

DRYER_THERMAL_EFF = {
    'conveyor': 0.55,
    'rotary': 0.60,
    'spray': 0.40,
    'fluidized_bed': 0.65,
    'tray': 0.50,
    'drum': 0.55,
    'infrared': 0.45,
    'microwave': 0.50,
}


# ---------------------------------------------------------------------------
# Input dataclass
# ---------------------------------------------------------------------------

@dataclass
class DryerInput:
    """Kurutma fırını analizi için giriş verileri"""

    # Ürün parametreleri
    product_mass_flow_kg_h: float = 1000.0
    moisture_in_pct: float = 60.0          # yaş bazda
    moisture_out_pct: float = 10.0         # yaş bazda
    product_inlet_temp_C: float = 25.0
    product_outlet_temp_C: float = 60.0

    # Isıtma parametreleri
    heat_source: str = 'natural_gas'       # natural_gas, steam, electrical, hot_air
    supply_temp_C: float = 200.0
    heat_input_kW: Optional[float] = None
    fuel_efficiency: float = 0.85

    # Hava parametreleri
    air_inlet_temp_C: float = 25.0
    air_outlet_temp_C: float = 80.0
    air_mass_flow_kg_h: Optional[float] = None

    # Ortam
    ambient_temp_C: float = 25.0
    ambient_humidity_pct: float = 50.0

    # Operasyonel
    operating_hours: float = 5000
    electricity_price_eur_kwh: float = 0.10
    fuel_price_eur_kwh: float = 0.05

    # Ekipman
    dryer_type: str = 'conveyor'
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None

    def __post_init__(self):
        """Hesaplanan varsayılanlar"""
        self._calc_water_removal()
        if self.heat_input_kW is None:
            self._calc_heat_input()
        if self.air_mass_flow_kg_h is None:
            self._calc_air_flow()

    def _calc_water_removal(self):
        """Buharlaştırılacak su miktarı [kg/h]"""
        m_dry = self.product_mass_flow_kg_h * (1 - self.moisture_in_pct / 100)
        m_wet_in = self.product_mass_flow_kg_h
        m_wet_out = m_dry / (1 - self.moisture_out_pct / 100)
        self.water_removed_kg_h = max(m_wet_in - m_wet_out, 0)

    def _calc_heat_input(self):
        """Minimum ısı girişi tahmini [kW]"""
        h_fg = _get_hfg(self.product_outlet_temp_C)
        Q_evap = self.water_removed_kg_h * h_fg / 3600
        Q_sensible = (self.product_mass_flow_kg_h * CP_WATER * 0.3 *
                      (self.product_outlet_temp_C - self.product_inlet_temp_C)) / 3600
        thermal_eff = DRYER_THERMAL_EFF.get(self.dryer_type, 0.55)
        self.heat_input_kW = (Q_evap + Q_sensible) / thermal_eff

    def _calc_air_flow(self):
        """Hava debisi tahmini [kg/h]"""
        if self.supply_temp_C > self.air_outlet_temp_C:
            dT = self.supply_temp_C - self.air_outlet_temp_C
            self.air_mass_flow_kg_h = self.heat_input_kW * 3600 / (CP_AIR * dT)
        else:
            self.air_mass_flow_kg_h = 5000


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class DryerResult(ExergyResult):
    """Kurutma fırını analizi sonuçları"""

    water_removed_kg_h: Optional[float] = None
    heat_input_kW: Optional[float] = None
    evaporation_energy_kW: Optional[float] = None
    exhaust_exergy_kW: Optional[float] = None

    thermal_efficiency_pct: Optional[float] = None
    specific_energy_kJ_kg_water: Optional[float] = None
    specific_exergy_kJ_kg_water: Optional[float] = None

    exhaust_recovery_potential_kW: Optional[float] = None
    exhaust_recovery_savings_eur_year: Optional[float] = None

    benchmark_comparison: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'water_removed_kg_h': round(self.water_removed_kg_h, 1) if self.water_removed_kg_h else None,
            'heat_input_kW': round(self.heat_input_kW, 1) if self.heat_input_kW else None,
            'evaporation_energy_kW': round(self.evaporation_energy_kW, 1) if self.evaporation_energy_kW else None,
            'exhaust_exergy_kW': round(self.exhaust_exergy_kW, 1) if self.exhaust_exergy_kW else None,
            'thermal_efficiency_pct': round(self.thermal_efficiency_pct, 1) if self.thermal_efficiency_pct else None,
            'specific_energy_kJ_kg_water': round(self.specific_energy_kJ_kg_water, 0) if self.specific_energy_kJ_kg_water else None,
            'specific_exergy_kJ_kg_water': round(self.specific_exergy_kJ_kg_water, 0) if self.specific_exergy_kJ_kg_water else None,
            'exhaust_recovery_potential_kW': round(self.exhaust_recovery_potential_kW, 1) if self.exhaust_recovery_potential_kW else None,
            'exhaust_recovery_savings_eur_year': round(self.exhaust_recovery_savings_eur_year, 0) if self.exhaust_recovery_savings_eur_year else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base

    def to_api_dict(self, dryer_type: str = "conveyor") -> dict:
        """API yanıt formatına dönüştürür."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "water_removed_kg_h": round(self.water_removed_kg_h, 1) if self.water_removed_kg_h else None,
            "thermal_efficiency_pct": round(self.thermal_efficiency_pct, 1) if self.thermal_efficiency_pct else None,
            "specific_energy_kJ_kg_water": round(self.specific_energy_kJ_kg_water, 0) if self.specific_energy_kJ_kg_water else None,
            "exhaust_exergy_kW": round(self.exhaust_exergy_kW, 1) if self.exhaust_exergy_kW else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, dryer_type),
            "comparison_text": _get_comparison_text(self.benchmark_comparison),
            "exergy_destroyed_avoidable_kW": round(self.exergy_destroyed_avoidable_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(self.exergy_destroyed_unavoidable_kW, 2),
            "avoidable_ratio_pct": round(self.avoidable_ratio_pct, 1),
        }


# ---------------------------------------------------------------------------
# Analysis function
# ---------------------------------------------------------------------------

def analyze_dryer(input_data: DryerInput, dead_state: DeadState = None, _calc_avoidable: bool = True) -> DryerResult:
    """
    Kurutma fırını exergy analizi yapar.

    Args:
        input_data: Kurutucu giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        DryerResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T0 = dead_state.T0

    T_supply = celsius_to_kelvin(input_data.supply_temp_C)
    T_exhaust = celsius_to_kelvin(input_data.air_outlet_temp_C)
    T_product_in = celsius_to_kelvin(input_data.product_inlet_temp_C)
    T_product_out = celsius_to_kelvin(input_data.product_outlet_temp_C)

    # Su buharlaştırma
    m_water_h = input_data.water_removed_kg_h
    m_water_s = m_water_h / 3600
    h_fg = _get_hfg(input_data.product_outlet_temp_C)
    Q_evap = m_water_s * h_fg

    Q_input = input_data.heat_input_kW

    # --- Giren Exergy ---
    if input_data.heat_source == 'electrical':
        Ex_in = Q_input
    elif input_data.heat_source == 'steam':
        Ex_in = Q_input * (1 - T0 / T_supply)
    else:
        exergy_factor = 1.04  # doğalgaz
        Ex_in = Q_input * exergy_factor

    # --- Faydalı Exergy ---
    T_evap = T_product_out
    if T_evap > T0:
        Ex_useful = Q_evap * (1 - T0 / T_evap)
    else:
        Ex_useful = 0

    m_product_s = input_data.product_mass_flow_kg_h / 3600
    cp_product = CP_WATER * 0.3
    Q_product = m_product_s * cp_product * (T_product_out - T_product_in)
    if T_product_out > T0:
        Ex_product_heating = Q_product * (1 - T0 / ((T_product_out + T_product_in) / 2))
        Ex_product_heating = max(Ex_product_heating, 0)
    else:
        Ex_product_heating = 0

    Ex_total_useful = Ex_useful + Ex_product_heating

    # --- Egzoz Exergy ---
    m_air_s = input_data.air_mass_flow_kg_h / 3600 if input_data.air_mass_flow_kg_h else 0
    if T_exhaust > T0 and m_air_s > 0:
        Ex_exhaust = m_air_s * CP_AIR * (
            (T_exhaust - T0) - T0 * math.log(T_exhaust / T0)
        )
        Ex_exhaust += m_water_s * CP_WATER_VAPOR * (
            (T_exhaust - T0) - T0 * math.log(T_exhaust / T0)
        )
        Ex_exhaust = max(Ex_exhaust, 0)
    else:
        Ex_exhaust = 0

    # --- Exergy Yıkımı ---
    Ex_destroyed = Ex_in - Ex_total_useful - Ex_exhaust
    Ex_destroyed = max(Ex_destroyed, 0)

    # --- Verimler ---
    eta_ex = (Ex_total_useful / Ex_in * 100) if Ex_in > 0 else 0

    Q_useful = Q_evap + Q_product
    thermal_eff = (Q_useful / Q_input * 100) if Q_input > 0 else 0

    specific_energy = (Q_input * 3600 / m_water_h) if m_water_h > 0 else 0
    specific_exergy = (Ex_in * 3600 / m_water_h) if m_water_h > 0 else 0

    # --- Egzoz Geri Kazanım ---
    exhaust_recovery = Ex_exhaust * 0.6
    exhaust_recovery_savings = exhaust_recovery * input_data.operating_hours * input_data.fuel_price_eur_kwh

    # --- Yıllık ---
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.fuel_price_eur_kwh

    benchmark = _get_dryer_benchmark(eta_ex, input_data.dryer_type)

    result = DryerResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_total_useful,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=exhaust_recovery,
        water_removed_kg_h=m_water_h,
        heat_input_kW=Q_input,
        evaporation_energy_kW=Q_evap,
        exhaust_exergy_kW=Ex_exhaust,
        thermal_efficiency_pct=thermal_eff,
        specific_energy_kJ_kg_water=specific_energy,
        specific_exergy_kJ_kg_water=specific_exergy,
        exhaust_recovery_potential_kW=exhaust_recovery,
        exhaust_recovery_savings_eur_year=exhaust_recovery_savings,
        benchmark_comparison=benchmark,
    )

    # AV/UN split — construct new instance to trigger __post_init__ recalculation
    if _calc_avoidable and Ex_destroyed > 0:
        ref_params = UNAVOIDABLE_REF_DRYER.get(input_data.dryer_type, {})
        if ref_params:
            fields_dict = {f.name: getattr(input_data, f.name) for f in dataclasses.fields(DryerInput)}
            fields_dict.update(ref_params)
            fields_dict['heat_input_kW'] = None       # Recalculate with new fuel_efficiency
            fields_dict['air_mass_flow_kg_h'] = None  # Recalculate with new air_outlet_temp_C
            un_input = DryerInput(**fields_dict)
            un_result = analyze_dryer(un_input, dead_state=dead_state, _calc_avoidable=False)
            av, un, ratio = compute_avoidable_split(Ex_destroyed, un_result.exergy_destroyed_kW)
            result.exergy_destroyed_avoidable_kW = av
            result.exergy_destroyed_unavoidable_kW = un
            result.avoidable_ratio_pct = ratio

    return result


# ---------------------------------------------------------------------------
# Sankey data
# ---------------------------------------------------------------------------

def generate_dryer_sankey_data(result: DryerResult, dryer_type: str = "conveyor") -> dict:
    """
    Kurutma fırını Sankey diyagramı için node ve link verisi oluşturur.

    Akış: Isı Kaynağı Exergy → [Kurutma İşi, Egzoz Havası Exergy, Exergy Yıkımı]
    """
    Ex_in = result.exergy_in_kW or 0
    Ex_useful = result.exergy_out_kW or 0
    Ex_exhaust = result.exhaust_exergy_kW or 0
    Ex_destroyed = result.exergy_destroyed_kW or 0

    # Normalize
    total_out = Ex_useful + Ex_exhaust + Ex_destroyed
    if total_out > 0 and abs(total_out - Ex_in) > 0.1:
        scale = Ex_in / total_out
        Ex_useful *= scale
        Ex_exhaust *= scale
        Ex_destroyed *= scale

    # AV/UN split for destruction node
    av_kW = getattr(result, 'exergy_destroyed_avoidable_kW', 0.0) or 0.0
    un_kW = getattr(result, 'exergy_destroyed_unavoidable_kW', 0.0) or 0.0
    has_av_un = (av_kW > 0 or un_kW > 0)

    if has_av_un:
        # Scale AV/UN to match normalized Ex_destroyed
        av_un_total = av_kW + un_kW
        if av_un_total > 0:
            av_norm = Ex_destroyed * (av_kW / av_un_total)
            un_norm = Ex_destroyed * (un_kW / av_un_total)
        else:
            av_norm = Ex_destroyed
            un_norm = 0.0

        nodes = [
            {"id": 0, "name": "Isi Kaynagi Exergy", "name_en": "Heat Source Exergy"},
            {"id": 1, "name": "Kurutma Isi", "name_en": "Drying Work"},
            {"id": 2, "name": "Egzoz Havasi Exergy", "name_en": "Exhaust Air Exergy"},
            {"id": 3, "name": "Exergy Yikimi (Onlenebilir)", "name_en": "Exergy Destruction (Avoidable)", "color": "#e74c3c"},
            {"id": 4, "name": "Exergy Yikimi (Onlenemez)", "name_en": "Exergy Destruction (Unavoidable)", "color": "#95a5a6"},
        ]

        links = []
        if Ex_useful > 0:
            links.append({"source": 0, "target": 1, "value": round(Ex_useful, 2), "label": "Kurutma Exergy"})
        if Ex_exhaust > 0:
            links.append({"source": 0, "target": 2, "value": round(Ex_exhaust, 2), "label": "Egzoz Kaybi"})
        if av_norm > 0.01:
            links.append({"source": 0, "target": 3, "value": round(av_norm, 2), "label": "Onlenebilir Kayiplar"})
        if un_norm > 0.01:
            links.append({"source": 0, "target": 4, "value": round(un_norm, 2), "label": "Onlenemez Kayiplar"})
    else:
        nodes = [
            {"id": 0, "name": "Isi Kaynagi Exergy", "name_en": "Heat Source Exergy"},
            {"id": 1, "name": "Kurutma Isi", "name_en": "Drying Work"},
            {"id": 2, "name": "Egzoz Havasi Exergy", "name_en": "Exhaust Air Exergy"},
            {"id": 3, "name": "Exergy Yikimi", "name_en": "Exergy Destruction"},
        ]

        links = []
        if Ex_useful > 0:
            links.append({"source": 0, "target": 1, "value": round(Ex_useful, 2), "label": "Kurutma Exergy"})
        if Ex_exhaust > 0:
            links.append({"source": 0, "target": 2, "value": round(Ex_exhaust, 2), "label": "Egzoz Kaybi"})
        if Ex_destroyed > 0:
            links.append({"source": 0, "target": 3, "value": round(Ex_destroyed, 2), "label": "Tersinmezlik"})

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(result.exergy_out_kW or 0, 2),
            "recoverable_heat_kW": round(result.exhaust_recovery_potential_kW or 0, 2),
            "irreversibility_kW": round(result.exergy_destroyed_kW or 0, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
            "exergy_destroyed_avoidable_kW": round(av_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(un_kW, 2),
            "avoidable_ratio_pct": round(getattr(result, 'avoidable_ratio_pct', 0.0) or 0.0, 1),
        },
    }


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_dryer_recommendations(result: DryerResult, input_data: DryerInput) -> list:
    """Analiz sonuçlarına göre iyileştirme önerileri"""
    recommendations = []

    # 1. Egzoz ısı geri kazanımı
    if result.exhaust_recovery_potential_kW and result.exhaust_recovery_potential_kW > 5:
        recommendations.append({
            'type': 'exhaust_heat_recovery',
            'title': 'Egzoz Havasi Isi Geri Kazanimi',
            'description': f'Egzoz havasinda {result.exhaust_exergy_kW:.1f} kW exergy mevcut. '
                          f'Giris havasini on isitma ile {result.exhaust_recovery_savings_eur_year:.0f} EUR/yil tasarruf.',
            'investment_eur': 15000,
            'savings_eur_year': result.exhaust_recovery_savings_eur_year or 0,
            'payback_years': 15000 / result.exhaust_recovery_savings_eur_year if result.exhaust_recovery_savings_eur_year and result.exhaust_recovery_savings_eur_year > 0 else float('inf'),
            'priority': 'high' if result.exhaust_recovery_savings_eur_year and result.exhaust_recovery_savings_eur_year > 5000 else 'medium',
        })

    # 2. Yüksek spesifik enerji → ön susuzlaştırma
    if result.specific_energy_kJ_kg_water and result.specific_energy_kJ_kg_water > 5000:
        savings = result.annual_loss_EUR * 0.20 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'pre_dewatering',
            'title': 'Mekanik On Susuzlastirma',
            'description': 'Spesifik enerji tuketimi yuksek. Presleme veya santrifuj ile '
                          'giris nem oranini dusurmek onerilir.',
            'investment_eur': 25000,
            'savings_eur_year': savings,
            'payback_years': 25000 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # 3. Düşük termal verim → izolasyon
    if result.thermal_efficiency_pct and result.thermal_efficiency_pct < 45:
        savings = result.annual_loss_EUR * 0.10 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'insulation',
            'title': 'Kurutucu Izolasyonu Iyilestirme',
            'description': f'Termal verim dusuk ({result.thermal_efficiency_pct:.0f}%). '
                          f'Duvar ve boru izolasyonu kontrol edilmeli.',
            'investment_eur': 5000,
            'savings_eur_year': savings,
            'payback_years': 5000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # 4. Hava resirkülasyonu
    if input_data.air_outlet_temp_C > 60 and input_data.ambient_humidity_pct < 60:
        savings = result.annual_loss_EUR * 0.12 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'air_recirculation',
            'title': 'Kismi Hava Resirkülasyonu',
            'description': 'Egzoz havasinin bir kismi geri dondurulerek enerji tasarrufu saglanabilir. '
                          'Urun kalitesine dikkat.',
            'investment_eur': 8000,
            'savings_eur_year': savings,
            'payback_years': 8000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # 5. Elektrik → doğalgaz/atık ısı
    if input_data.heat_source == 'electrical':
        savings = result.annual_loss_EUR * 0.40 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'heat_source_change',
            'title': 'Isi Kaynagi Optimizasyonu',
            'description': 'Elektrikli isitma yerine dogalgaz veya atik isi kaynagi kullanimi '
                          'isletme maliyetini dusurebilir.',
            'investment_eur': 20000,
            'savings_eur_year': savings,
            'payback_years': 20000 / savings if savings > 0 else float('inf'),
            'priority': 'high' if result.heat_input_kW and result.heat_input_kW > 50 else 'medium',
        })

    return recommendations


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_dryer_benchmark(eta_ex: float, dryer_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması"""
    benchmarks = {
        'conveyor':      {'poor': 8,  'average': 15, 'good': 22, 'excellent': 30},
        'rotary':        {'poor': 10, 'average': 18, 'good': 25, 'excellent': 33},
        'spray':         {'poor': 5,  'average': 10, 'good': 18, 'excellent': 25},
        'fluidized_bed': {'poor': 12, 'average': 20, 'good': 28, 'excellent': 35},
        'tray':          {'poor': 6,  'average': 12, 'good': 20, 'excellent': 28},
        'drum':          {'poor': 8,  'average': 15, 'good': 22, 'excellent': 30},
        'infrared':      {'poor': 10, 'average': 18, 'good': 25, 'excellent': 32},
        'microwave':     {'poor': 15, 'average': 22, 'good': 30, 'excellent': 38},
    }
    thresholds = benchmarks.get(dryer_type, benchmarks['conveyor'])

    if eta_ex < thresholds['poor']:
        return 'poor'
    elif eta_ex < thresholds['average']:
        return 'below_average'
    elif eta_ex < thresholds['good']:
        return 'average'
    elif eta_ex < thresholds['excellent']:
        return 'good'
    else:
        return 'excellent'


def _calculate_percentile(eta_ex: float, dryer_type: str) -> int:
    """Exergy verimini 0-100 yuzdelik dilime esler."""
    benchmarks = {
        'conveyor':      {'low': 6,  'mid': 15, 'high': 30},
        'rotary':        {'low': 8,  'mid': 18, 'high': 33},
        'spray':         {'low': 4,  'mid': 10, 'high': 25},
        'fluidized_bed': {'low': 10, 'mid': 20, 'high': 35},
        'tray':          {'low': 5,  'mid': 12, 'high': 28},
        'drum':          {'low': 6,  'mid': 15, 'high': 30},
        'infrared':      {'low': 8,  'mid': 18, 'high': 32},
        'microwave':     {'low': 12, 'mid': 22, 'high': 38},
    }
    thresholds = benchmarks.get(dryer_type, benchmarks['conveyor'])

    if eta_ex <= thresholds['low']:
        return max(0, int(eta_ex / thresholds['low'] * 25))
    elif eta_ex <= thresholds['mid']:
        return 25 + int((eta_ex - thresholds['low']) / (thresholds['mid'] - thresholds['low']) * 25)
    elif eta_ex <= thresholds['high']:
        return 50 + int((eta_ex - thresholds['mid']) / (thresholds['high'] - thresholds['mid']) * 25)
    else:
        return min(100, 75 + int((eta_ex - thresholds['high']) / 15 * 25))


def _get_comparison_text(benchmark: str) -> str:
    """Benchmark sonucuna gore aciklama dondurur."""
    texts = {
        'poor': 'Exergy verimi dusuk. Acil iyilestirme onerilir.',
        'below_average': 'Exergy verimi ortalamanin altinda. Iyilestirme potansiyeli yuksek.',
        'average': 'Exergy verimi ortalama seviyede. Iyilestirme firsatlari mevcut.',
        'good': 'Exergy verimi iyi seviyede. Sinirli iyilestirme potansiyeli.',
        'excellent': 'Exergy verimi mukemmel. En iyi uygulama seviyesinde.',
    }
    return texts.get(benchmark, '')
