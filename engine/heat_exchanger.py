"""
ExergyLab - Heat Exchanger Exergy Analysis

Isı eşanjörü exergy hesaplamaları.
Shell & tube, plakalı, finned tube, ekonomizer tipleri için.
"""

from dataclasses import dataclass
from typing import Optional
import math

import copy

from .core import (
    DeadState, ExergyResult, compute_avoidable_split,
    celsius_to_kelvin,
    heat_exergy, CP_AIR, R_AIR
)
from .exergoeconomic import _apply_exergoeconomic


# Akışkan özgül ısıları (kJ/kg·K)
FLUID_CP = {
    'water': 4.18,
    'steam': 2.01,
    'air': 1.005,
    'flue_gas': 1.10,
    'thermal_oil': 2.10,
    'glycol_30': 3.70,
    'glycol_50': 3.30,
}

# Akışkan R değerleri (kJ/kg·K) — basınç düşüşü entropi hesabı için
FLUID_R = {
    'air': 0.287,
    'flue_gas': 0.287,
    'steam': 0.4615,
    'water': 0.0,
    'thermal_oil': 0.0,
    'glycol_30': 0.0,
    'glycol_50': 0.0,
}

# Best-achievable pressure drops per HX type (Tsatsaronis & Morosuk 2008)
UNAVOIDABLE_REF_HEAT_EXCHANGER = {
    'shell_tube':  {'hot_pressure_drop_kPa': 8.0, 'cold_pressure_drop_kPa': 8.0},
    'plate':       {'hot_pressure_drop_kPa': 5.0, 'cold_pressure_drop_kPa': 5.0},
    'finned_tube': {'hot_pressure_drop_kPa': 3.0, 'cold_pressure_drop_kPa': 10.0},
    'economizer':  {'hot_pressure_drop_kPa': 2.0, 'cold_pressure_drop_kPa': 10.0},
    'air_cooled':  {'hot_pressure_drop_kPa': 5.0, 'cold_pressure_drop_kPa': 0.5},
    'double_pipe': {'hot_pressure_drop_kPa': 5.0, 'cold_pressure_drop_kPa': 5.0},
    'spiral':      {'hot_pressure_drop_kPa': 8.0, 'cold_pressure_drop_kPa': 8.0},
    'recuperator': {'hot_pressure_drop_kPa': 5.0, 'cold_pressure_drop_kPa': 5.0},
}


# ---------------------------------------------------------------------------
# Input dataclass
# ---------------------------------------------------------------------------

@dataclass
class HeatExchangerInput:
    """Isı eşanjörü analizi için giriş verileri"""

    # Sıcak taraf
    hot_fluid: str = 'water'
    hot_inlet_temp_C: float = 90.0
    hot_outlet_temp_C: float = 70.0
    hot_mass_flow_kg_s: float = 2.0
    hot_pressure_drop_kPa: float = 10.0

    # Soğuk taraf
    cold_fluid: str = 'water'
    cold_inlet_temp_C: float = 20.0
    cold_outlet_temp_C: float = 50.0
    cold_mass_flow_kg_s: float = 1.5
    cold_pressure_drop_kPa: float = 15.0

    # Opsiyonel
    heat_duty_kW: Optional[float] = None
    ambient_temp_C: float = 25.0

    # Operasyonel
    operating_hours: float = 6000
    electricity_price_eur_kwh: float = 0.10
    fuel_price_eur_kwh: float = 0.06

    # Ekipman bilgisi
    hx_type: str = 'shell_tube'
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None
    design_heat_duty_kW: Optional[float] = None
    equipment_cost_eur: Optional[float] = None

    def __post_init__(self):
        """Varsayılan değerleri ayarla ve doğrula"""
        if self.heat_duty_kW is None:
            cp_h = FLUID_CP.get(self.hot_fluid, 4.18)
            self.heat_duty_kW = abs(
                self.hot_mass_flow_kg_s * cp_h * (self.hot_inlet_temp_C - self.hot_outlet_temp_C)
            )


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class HeatExchangerResult(ExergyResult):
    """Isı eşanjörü analizi sonuçları"""

    heat_duty_kW: Optional[float] = None
    lmtd_K: Optional[float] = None
    effectiveness: Optional[float] = None
    hot_exergy_decrease_kW: Optional[float] = None
    cold_exergy_increase_kW: Optional[float] = None

    # Bejan analizi
    entropy_gen_total_kW_K: Optional[float] = None
    entropy_gen_heat_transfer_kW_K: Optional[float] = None
    entropy_gen_pressure_drop_kW_K: Optional[float] = None
    bejan_number: Optional[float] = None

    # Benchmark
    benchmark_comparison: Optional[str] = None
    fouling_indicator: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'heat_duty_kW': round(self.heat_duty_kW, 2) if self.heat_duty_kW else None,
            'lmtd_K': round(self.lmtd_K, 2) if self.lmtd_K else None,
            'effectiveness': round(self.effectiveness, 3) if self.effectiveness else None,
            'hot_exergy_decrease_kW': round(self.hot_exergy_decrease_kW, 2) if self.hot_exergy_decrease_kW else None,
            'cold_exergy_increase_kW': round(self.cold_exergy_increase_kW, 2) if self.cold_exergy_increase_kW else None,
            'entropy_gen_total_kW_K': round(self.entropy_gen_total_kW_K, 4) if self.entropy_gen_total_kW_K else None,
            'entropy_gen_heat_transfer_kW_K': round(self.entropy_gen_heat_transfer_kW_K, 4) if self.entropy_gen_heat_transfer_kW_K else None,
            'entropy_gen_pressure_drop_kW_K': round(self.entropy_gen_pressure_drop_kW_K, 4) if self.entropy_gen_pressure_drop_kW_K else None,
            'bejan_number': round(self.bejan_number, 3) if self.bejan_number else None,
            'benchmark_comparison': self.benchmark_comparison,
            'fouling_indicator': self.fouling_indicator,
        })
        return base

    def to_api_dict(self, hx_type: str = "shell_tube") -> dict:
        """API yanıt formatına dönüştürür."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "heat_duty_kW": round(self.heat_duty_kW, 2) if self.heat_duty_kW else None,
            "lmtd_K": round(self.lmtd_K, 2) if self.lmtd_K else None,
            "effectiveness": round(self.effectiveness, 3) if self.effectiveness else None,
            "bejan_number": round(self.bejan_number, 3) if self.bejan_number else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, hx_type),
            "comparison_text": _get_comparison_text(self.benchmark_comparison),
            "exergy_destroyed_avoidable_kW": round(self.exergy_destroyed_avoidable_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(self.exergy_destroyed_unavoidable_kW, 2),
            "avoidable_ratio_pct": round(self.avoidable_ratio_pct, 1),
        }


# ---------------------------------------------------------------------------
# Analysis function
# ---------------------------------------------------------------------------

def analyze_heat_exchanger(input_data: HeatExchangerInput, dead_state: DeadState = None, _calc_avoidable: bool = True) -> HeatExchangerResult:
    """
    Isı eşanjörü exergy analizi yapar.

    Args:
        input_data: HX giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        HeatExchangerResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T0 = dead_state.T0

    # Sıcaklıkları Kelvin'e çevir
    T_h_in = celsius_to_kelvin(input_data.hot_inlet_temp_C)
    T_h_out = celsius_to_kelvin(input_data.hot_outlet_temp_C)
    T_c_in = celsius_to_kelvin(input_data.cold_inlet_temp_C)
    T_c_out = celsius_to_kelvin(input_data.cold_outlet_temp_C)

    # Cp değerleri
    cp_h = FLUID_CP.get(input_data.hot_fluid, 4.18)
    cp_c = FLUID_CP.get(input_data.cold_fluid, 4.18)
    R_h = FLUID_R.get(input_data.hot_fluid, 0.0)
    R_c = FLUID_R.get(input_data.cold_fluid, 0.0)

    m_h = input_data.hot_mass_flow_kg_s
    m_c = input_data.cold_mass_flow_kg_s

    Q = input_data.heat_duty_kW

    # --- LMTD Hesabı (karşı akış varsayımı) ---
    dT1 = T_h_in - T_c_out
    dT2 = T_h_out - T_c_in
    if dT1 > 0 and dT2 > 0 and abs(dT1 - dT2) > 0.01:
        lmtd = (dT1 - dT2) / math.log(dT1 / dT2)
    elif dT1 > 0 and dT2 > 0:
        lmtd = (dT1 + dT2) / 2
    else:
        lmtd = max(abs(dT1), abs(dT2))

    # --- Effectiveness (ε) ---
    C_h = m_h * cp_h
    C_c = m_c * cp_c
    C_min = min(C_h, C_c)
    Q_max = C_min * (T_h_in - T_c_in)
    effectiveness = Q / Q_max if Q_max > 0 else 0

    # --- Exergy Hesapları ---
    delta_ex_hot = m_h * cp_h * (
        (T_h_in - T_h_out) - T0 * math.log(T_h_in / T_h_out)
    )

    delta_ex_cold = m_c * cp_c * (
        (T_c_out - T_c_in) - T0 * math.log(T_c_out / T_c_in)
    )

    Ex_in = delta_ex_hot
    Ex_out = delta_ex_cold

    Ex_destroyed = Ex_in - Ex_out
    if Ex_destroyed < 0:
        Ex_destroyed = 0

    eta_ex = (Ex_out / Ex_in * 100) if Ex_in > 0 else 0

    # --- Entropi Üretimi Ayrıştırma (Bejan) ---
    T_lm_hot = (T_h_in - T_h_out) / math.log(T_h_in / T_h_out) if abs(T_h_in - T_h_out) > 0.1 else T_h_in
    T_lm_cold = (T_c_out - T_c_in) / math.log(T_c_out / T_c_in) if abs(T_c_out - T_c_in) > 0.1 else T_c_in

    S_gen_heat = Q / T_lm_cold - Q / T_lm_hot
    if S_gen_heat < 0:
        S_gen_heat = 0

    S_gen_pressure = 0
    if R_h > 0 and input_data.hot_pressure_drop_kPa > 0:
        P_avg_h = dead_state.P0
        S_gen_pressure += m_h * R_h * input_data.hot_pressure_drop_kPa / P_avg_h
    if R_c > 0 and input_data.cold_pressure_drop_kPa > 0:
        P_avg_c = dead_state.P0
        S_gen_pressure += m_c * R_c * input_data.cold_pressure_drop_kPa / P_avg_c

    S_gen_total = S_gen_heat + S_gen_pressure
    bejan = S_gen_heat / S_gen_total if S_gen_total > 0 else 1.0

    # --- Yıllık Etki ---
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.fuel_price_eur_kwh

    # --- Benchmark ---
    benchmark = _get_hx_benchmark(eta_ex, input_data.hx_type)

    # --- Fouling indicator ---
    fouling = None
    if input_data.design_heat_duty_kW and input_data.design_heat_duty_kW > 0:
        performance_ratio = Q / input_data.design_heat_duty_kW
        if performance_ratio < 0.70:
            fouling = 'severe'
        elif performance_ratio < 0.85:
            fouling = 'moderate'
        elif performance_ratio < 0.95:
            fouling = 'light'
        else:
            fouling = 'clean'

    result = HeatExchangerResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=None,
        heat_duty_kW=Q,
        lmtd_K=lmtd,
        effectiveness=effectiveness,
        hot_exergy_decrease_kW=delta_ex_hot,
        cold_exergy_increase_kW=delta_ex_cold,
        entropy_gen_total_kW_K=S_gen_total,
        entropy_gen_heat_transfer_kW_K=S_gen_heat,
        entropy_gen_pressure_drop_kW_K=S_gen_pressure,
        bejan_number=bejan,
        benchmark_comparison=benchmark,
        fouling_indicator=fouling,
    )

    # AV/UN split
    if _calc_avoidable and Ex_destroyed > 0:
        ref_params = UNAVOIDABLE_REF_HEAT_EXCHANGER.get(input_data.hx_type, {})
        if ref_params:
            un_input = copy.deepcopy(input_data)
            for k, v in ref_params.items():
                if getattr(un_input, k) > v:
                    setattr(un_input, k, v)
            un_result = analyze_heat_exchanger(un_input, dead_state=dead_state, _calc_avoidable=False)
            av, un, ratio = compute_avoidable_split(Ex_destroyed, un_result.exergy_destroyed_kW)
            result.exergy_destroyed_avoidable_kW = av
            result.exergy_destroyed_unavoidable_kW = un
            result.avoidable_ratio_pct = ratio

    # Exergoeconomic analysis
    _apply_exergoeconomic(
        result, equipment_type='heat_exchanger',
        c_fuel_eur_kWh=input_data.fuel_price_eur_kwh,
        capacity_param_kW=Q,
        subtype=input_data.hx_type,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
    )

    return result


# ---------------------------------------------------------------------------
# Sankey data
# ---------------------------------------------------------------------------

def generate_heat_exchanger_sankey_data(result: HeatExchangerResult, hx_type: str = "shell_tube") -> dict:
    """
    Isı eşanjörü Sankey diyagramı için node ve link verisi oluşturur.

    Akış: Sıcak Taraf Exergy → [Soğuk Taraf Kazanımı, ΔT Yıkımı, ΔP Yıkımı]
    """
    Ex_in = result.exergy_in_kW or 0
    Ex_out = result.exergy_out_kW or 0
    Ex_destroyed = result.exergy_destroyed_kW or 0

    # Entropi ayrıştırmasına göre yıkımı böl
    S_heat = result.entropy_gen_heat_transfer_kW_K or 0
    S_pressure = result.entropy_gen_pressure_drop_kW_K or 0
    S_total = S_heat + S_pressure

    if S_total > 0 and Ex_destroyed > 0:
        destruction_heat_transfer = Ex_destroyed * (S_heat / S_total)
        destruction_pressure_drop = Ex_destroyed * (S_pressure / S_total)
    else:
        destruction_heat_transfer = Ex_destroyed
        destruction_pressure_drop = 0

    # Normalize — toplam çıkış = toplam giriş
    total_out = Ex_out + destruction_heat_transfer + destruction_pressure_drop
    if total_out > 0 and abs(total_out - Ex_in) > 0.1:
        scale = Ex_in / total_out
        Ex_out *= scale
        destruction_heat_transfer *= scale
        destruction_pressure_drop *= scale

    has_pressure_loss = destruction_pressure_drop > 0.01

    nodes = [
        {"id": 0, "name": "Sicak Taraf Exergy", "name_en": "Hot Side Exergy"},
        {"id": 1, "name": "Soguk Taraf Kazanimi", "name_en": "Cold Side Gain"},
        {"id": 2, "name": "Isi Transferi Kayip", "name_en": "Heat Transfer Loss"},
    ]

    if has_pressure_loss:
        nodes.append({"id": 3, "name": "Basinc Dususu Kayip", "name_en": "Pressure Drop Loss"})

    links = []
    if Ex_out > 0:
        links.append({"source": 0, "target": 1, "value": round(Ex_out, 2), "label": "Soguk Taraf Exergy"})
    if destruction_heat_transfer > 0.01:
        links.append({"source": 0, "target": 2, "value": round(destruction_heat_transfer, 2), "label": "Isi Transferi Tersinmezligi"})
    if has_pressure_loss:
        links.append({"source": 0, "target": 3, "value": round(destruction_pressure_drop, 2), "label": "Basinc Dususu Kaybi"})

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(result.exergy_out_kW or 0, 2),
            "recoverable_heat_kW": 0,
            "irreversibility_kW": round(Ex_destroyed, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
            "exergy_destroyed_avoidable_kW": round(getattr(result, 'exergy_destroyed_avoidable_kW', 0.0) or 0.0, 2),
            "exergy_destroyed_unavoidable_kW": round(getattr(result, 'exergy_destroyed_unavoidable_kW', 0.0) or 0.0, 2),
            "avoidable_ratio_pct": round(getattr(result, 'avoidable_ratio_pct', 0.0) or 0.0, 1),
        },
    }


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_heat_exchanger_recommendations(result: HeatExchangerResult, input_data: HeatExchangerInput) -> list:
    """Analiz sonuçlarına göre iyileştirme önerileri"""
    recommendations = []

    # 1. Fouling — temizlik önerisi
    if result.fouling_indicator in ['severe', 'moderate']:
        savings_pct = 0.15 if result.fouling_indicator == 'severe' else 0.08
        savings = result.annual_loss_EUR * savings_pct if result.annual_loss_EUR else 0
        investment = 2000 if result.fouling_indicator == 'severe' else 1000
        recommendations.append({
            'type': 'cleaning',
            'title': 'Esanjor Temizligi / Fouling Giderme',
            'description': f'Performans dususu tespit edildi ({result.fouling_indicator}). '
                          f'Kimyasal veya mekanik temizlik onerilir.',
            'investment_eur': investment,
            'savings_eur_year': savings,
            'payback_years': investment / savings if savings > 0 else float('inf'),
            'priority': 'high' if result.fouling_indicator == 'severe' else 'medium',
        })

    # 2. Yüksek ΔT — ek ısı geri kazanım
    if input_data.hot_outlet_temp_C > input_data.cold_inlet_temp_C + 30:
        potential_kW = input_data.hot_mass_flow_kg_s * FLUID_CP.get(input_data.hot_fluid, 4.18) * (
            input_data.hot_outlet_temp_C - input_data.cold_inlet_temp_C - 10
        ) * 0.5
        potential_eur = potential_kW * input_data.operating_hours * input_data.fuel_price_eur_kwh
        recommendations.append({
            'type': 'additional_recovery',
            'title': 'Ek Isi Geri Kazanimi',
            'description': f'Sicak cikis hala yuksek ({input_data.hot_outlet_temp_C} C). '
                          f'Ikinci kademe esanjor veya ekonomizer eklenebilir.',
            'investment_eur': 8000,
            'savings_eur_year': potential_eur,
            'payback_years': 8000 / potential_eur if potential_eur > 0 else float('inf'),
            'priority': 'medium',
        })

    # 3. Bejan > 0.9 — ΔT baskın, alan artırma öner
    if result.bejan_number and result.bejan_number > 0.9:
        savings = result.annual_loss_EUR * 0.20 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'area_increase',
            'title': 'Isi Transfer Alanini Artir',
            'description': 'Entropi uretiminin buyuk kismi sicaklik farkindan. '
                          'Daha buyuk alan ile dT dusrulebilir.',
            'investment_eur': 15000,
            'savings_eur_year': savings,
            'payback_years': 15000 / savings if savings > 0 else float('inf'),
            'priority': 'low',
        })

    # 4. Düşük effectiveness
    if result.effectiveness and result.effectiveness < 0.5:
        savings = result.annual_loss_EUR * 0.30 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'upgrade',
            'title': 'Esanjor Tip Degisikligi',
            'description': f'Etkinlik dusuk (e={result.effectiveness:.2f}). '
                          f'Plakali esanjore gecis dusunulebilir.',
            'investment_eur': 12000,
            'savings_eur_year': savings,
            'payback_years': 12000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    return recommendations


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_hx_benchmark(eta_ex: float, hx_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması"""
    benchmarks = {
        'shell_tube':  {'poor': 25, 'average': 40, 'good': 55, 'excellent': 65},
        'plate':       {'poor': 30, 'average': 50, 'good': 65, 'excellent': 75},
        'finned_tube': {'poor': 20, 'average': 35, 'good': 50, 'excellent': 60},
        'economizer':  {'poor': 25, 'average': 40, 'good': 55, 'excellent': 65},
        'air_cooled':  {'poor': 15, 'average': 30, 'good': 45, 'excellent': 55},
    }
    thresholds = benchmarks.get(hx_type, benchmarks['shell_tube'])

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


def _calculate_percentile(eta_ex: float, hx_type: str) -> int:
    """Exergy verimini 0-100 yuzdelik dilime esler."""
    benchmarks = {
        'shell_tube':  {'low': 20, 'mid': 40, 'high': 65},
        'plate':       {'low': 25, 'mid': 50, 'high': 75},
        'finned_tube': {'low': 18, 'mid': 35, 'high': 60},
        'economizer':  {'low': 20, 'mid': 40, 'high': 65},
        'air_cooled':  {'low': 12, 'mid': 30, 'high': 55},
    }
    thresholds = benchmarks.get(hx_type, benchmarks['shell_tube'])

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
