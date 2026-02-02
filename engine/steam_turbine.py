"""
ExergyLab - Steam Turbine / CHP Exergy Analysis

Buhar türbini ve kojenerasyon sistemi exergy hesaplamaları.
Condensing, backpressure, extraction ve CHP tipleri için.
"""

from dataclasses import dataclass
from typing import Optional
import math

import dataclasses

from .core import (
    DeadState, ExergyResult, compute_avoidable_split,
    celsius_to_kelvin,
    heat_exergy
)

# Buhar özellikleri (basitleştirilmiş)
CP_STEAM_SUPERHEATED = 2.01     # kJ/kg·K
CP_STEAM_SATURATED = 2.30       # kJ/kg·K
CP_WATER = 4.18                 # kJ/kg·K
R_STEAM = 0.4615                # kJ/kg·K
H_FG_100C = 2257.0              # kJ/kg

# Basınca göre doyma sıcaklıkları [bar → °C]
SATURATION_TEMP = {
    0.05: 32.9,   0.1: 45.8,    0.2: 60.1,   0.5: 81.3,
    1.0: 99.6,    1.5: 111.4,   2.0: 120.2,  3.0: 133.5,
    4.0: 143.6,   5.0: 151.8,   6.0: 158.8,  8.0: 170.4,
    10.0: 179.9,  15.0: 198.3,  20.0: 212.4, 25.0: 224.0,
    30.0: 233.9,  40.0: 250.4,  50.0: 263.9, 60.0: 275.6,
    80.0: 295.0,  100.0: 311.0,
}


# Best-achievable efficiencies per turbine type (Tsatsaronis & Morosuk 2008)
UNAVOIDABLE_REF_STEAM_TURBINE = {
    'backpressure': {'isentropic_efficiency': 0.90, 'mechanical_efficiency': 0.99, 'generator_efficiency': 0.98},
    'condensing':   {'isentropic_efficiency': 0.92, 'mechanical_efficiency': 0.99, 'generator_efficiency': 0.98},
    'extraction':   {'isentropic_efficiency': 0.88, 'mechanical_efficiency': 0.99, 'generator_efficiency': 0.98},
}


def _get_saturation_temp_C(P_bar: float) -> float:
    """Basınca göre doyma sıcaklığı (lineer interpolasyon)"""
    pressures = sorted(SATURATION_TEMP.keys())

    if P_bar <= pressures[0]:
        return SATURATION_TEMP[pressures[0]]
    if P_bar >= pressures[-1]:
        return SATURATION_TEMP[pressures[-1]]

    for i in range(len(pressures) - 1):
        if pressures[i] <= P_bar <= pressures[i + 1]:
            p1, p2 = pressures[i], pressures[i + 1]
            t1, t2 = SATURATION_TEMP[p1], SATURATION_TEMP[p2]
            return t1 + (t2 - t1) * (P_bar - p1) / (p2 - p1)

    return 100.0


# ---------------------------------------------------------------------------
# Input dataclass
# ---------------------------------------------------------------------------

@dataclass
class SteamTurbineInput:
    """Buhar türbini analizi için giriş verileri"""

    # Giriş buharı
    inlet_temp_C: float = 400.0
    inlet_pressure_bar: float = 40.0
    mass_flow_kg_s: float = 5.0

    # Çıkış koşulları
    outlet_pressure_bar: float = 0.1
    outlet_temp_C: Optional[float] = None

    # Türbin özellikleri
    isentropic_efficiency: float = 0.80
    mechanical_efficiency: float = 0.98
    generator_efficiency: float = 0.97

    # CHP parametreleri
    is_chp: bool = False
    heat_recovery_temp_C: Optional[float] = None
    heat_recovery_fraction: float = 0.60

    # Ortam
    ambient_temp_C: float = 25.0

    # Operasyonel
    operating_hours: float = 7000
    electricity_price_eur_kwh: float = 0.10
    fuel_price_eur_kwh: float = 0.04

    # Ekipman
    turbine_type: str = 'backpressure'
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None
    rated_power_MW: Optional[float] = None

    def __post_init__(self):
        """Çıkış sıcaklığını hesapla (verilmemişse)"""
        if self.outlet_temp_C is None:
            T_sat_out = _get_saturation_temp_C(self.outlet_pressure_bar)

            if self.turbine_type == 'condensing':
                self.outlet_temp_C = T_sat_out
            elif self.turbine_type == 'backpressure':
                T_in_K = self.inlet_temp_C + 273.15
                gamma = 1.3
                T_out_isentropic = T_in_K * (self.outlet_pressure_bar / self.inlet_pressure_bar) ** ((gamma - 1) / gamma)
                T_out_actual = T_in_K - self.isentropic_efficiency * (T_in_K - T_out_isentropic)
                self.outlet_temp_C = max(T_out_actual - 273.15, T_sat_out + 5)
            else:
                T_in_K = self.inlet_temp_C + 273.15
                gamma = 1.3
                T_out_isentropic = T_in_K * (self.outlet_pressure_bar / self.inlet_pressure_bar) ** ((gamma - 1) / gamma)
                T_out_actual = T_in_K - self.isentropic_efficiency * (T_in_K - T_out_isentropic)
                self.outlet_temp_C = max(T_out_actual - 273.15, T_sat_out)


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class SteamTurbineResult(ExergyResult):
    """Buhar türbini analizi sonuçları"""

    shaft_power_kW: Optional[float] = None
    electrical_power_kW: Optional[float] = None
    exhaust_exergy_kW: Optional[float] = None
    isentropic_efficiency_actual: Optional[float] = None

    # CHP
    heat_recovered_kW: Optional[float] = None
    heat_recovered_exergy_kW: Optional[float] = None
    total_useful_exergy_kW: Optional[float] = None
    chp_exergy_efficiency_pct: Optional[float] = None

    # Yıllık
    annual_electricity_MWh: Optional[float] = None
    annual_electricity_revenue_EUR: Optional[float] = None

    # Benchmark
    benchmark_comparison: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'shaft_power_kW': round(self.shaft_power_kW, 2) if self.shaft_power_kW else None,
            'electrical_power_kW': round(self.electrical_power_kW, 2) if self.electrical_power_kW else None,
            'exhaust_exergy_kW': round(self.exhaust_exergy_kW, 2) if self.exhaust_exergy_kW else None,
            'isentropic_efficiency_actual': round(self.isentropic_efficiency_actual, 3) if self.isentropic_efficiency_actual else None,
            'heat_recovered_kW': round(self.heat_recovered_kW, 2) if self.heat_recovered_kW else None,
            'heat_recovered_exergy_kW': round(self.heat_recovered_exergy_kW, 2) if self.heat_recovered_exergy_kW else None,
            'total_useful_exergy_kW': round(self.total_useful_exergy_kW, 2) if self.total_useful_exergy_kW else None,
            'chp_exergy_efficiency_pct': round(self.chp_exergy_efficiency_pct, 1) if self.chp_exergy_efficiency_pct else None,
            'annual_electricity_MWh': round(self.annual_electricity_MWh, 1) if self.annual_electricity_MWh else None,
            'annual_electricity_revenue_EUR': round(self.annual_electricity_revenue_EUR, 0) if self.annual_electricity_revenue_EUR else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base

    def to_api_dict(self, turbine_type: str = "backpressure") -> dict:
        """API yanıt formatına dönüştürür."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "shaft_power_kW": round(self.shaft_power_kW, 2) if self.shaft_power_kW else None,
            "electrical_power_kW": round(self.electrical_power_kW, 2) if self.electrical_power_kW else None,
            "exhaust_exergy_kW": round(self.exhaust_exergy_kW, 2) if self.exhaust_exergy_kW else None,
            "chp_exergy_efficiency_pct": round(self.chp_exergy_efficiency_pct, 1) if self.chp_exergy_efficiency_pct else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, turbine_type),
            "comparison_text": _get_comparison_text(self.benchmark_comparison),
            "exergy_destroyed_avoidable_kW": round(self.exergy_destroyed_avoidable_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(self.exergy_destroyed_unavoidable_kW, 2),
            "avoidable_ratio_pct": round(self.avoidable_ratio_pct, 1),
        }


# ---------------------------------------------------------------------------
# Analysis function
# ---------------------------------------------------------------------------

def analyze_steam_turbine(input_data: SteamTurbineInput, dead_state: DeadState = None, _calc_avoidable: bool = True) -> SteamTurbineResult:
    """
    Buhar türbini exergy analizi yapar.

    Args:
        input_data: Türbin giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        SteamTurbineResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T0 = dead_state.T0
    P0_bar = dead_state.P0 / 100  # kPa → bar

    T_in = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out = celsius_to_kelvin(input_data.outlet_temp_C)
    m = input_data.mass_flow_kg_s

    # Uygun cp seçimi
    T_sat_in = celsius_to_kelvin(_get_saturation_temp_C(input_data.inlet_pressure_bar))
    if T_in > T_sat_in + 20:
        cp = CP_STEAM_SUPERHEATED
    else:
        cp = CP_STEAM_SATURATED

    # --- Giren Exergy ---
    ex_in_thermal = cp * ((T_in - T0) - T0 * math.log(T_in / T0))
    ex_in_pressure = R_STEAM * T0 * math.log(input_data.inlet_pressure_bar / P0_bar)
    Ex_in = m * (ex_in_thermal + ex_in_pressure)

    # --- Çıkan Exergy (egzoz) ---
    ex_out_thermal = cp * ((T_out - T0) - T0 * math.log(max(T_out, T0 + 1) / T0))
    ex_out_pressure = R_STEAM * T0 * math.log(max(input_data.outlet_pressure_bar, 0.01) / P0_bar)
    Ex_out_flow = m * (ex_out_thermal + max(ex_out_pressure, 0))

    # --- İş Çıkışı ---
    W_shaft = m * cp * (T_in - T_out)
    W_shaft = max(W_shaft, 0)

    W_electrical = W_shaft * input_data.mechanical_efficiency * input_data.generator_efficiency

    # --- Exergy Yıkımı ---
    Ex_destroyed = Ex_in - W_shaft - Ex_out_flow
    Ex_destroyed = max(Ex_destroyed, 0)

    # --- Exergy Verimi ---
    if Ex_in > Ex_out_flow:
        eta_ex = (W_shaft / (Ex_in - Ex_out_flow)) * 100
    else:
        eta_ex = 0
    eta_ex = min(eta_ex, 100)

    # --- CHP Hesabı ---
    heat_recovered = 0
    heat_recovered_exergy = 0
    total_useful_exergy = W_shaft
    chp_eta_ex = eta_ex

    if input_data.is_chp:
        T_recovery = celsius_to_kelvin(input_data.heat_recovery_temp_C) if input_data.heat_recovery_temp_C else T_out
        Q_exhaust = m * cp * (T_out - T0)
        heat_recovered = Q_exhaust * input_data.heat_recovery_fraction
        heat_recovered = max(heat_recovered, 0)

        if heat_recovered > 0 and T_recovery > T0:
            T_avg_recovery = (T_recovery + T0) / 2
            heat_recovered_exergy = heat_recovered * (1 - T0 / T_avg_recovery)
            heat_recovered_exergy = max(heat_recovered_exergy, 0)

        total_useful_exergy = W_shaft + heat_recovered_exergy
        if Ex_in > 0:
            chp_eta_ex = (total_useful_exergy / Ex_in) * 100
            chp_eta_ex = min(chp_eta_ex, 100)

    # --- Yıllık ---
    annual_elec_MWh = W_electrical * input_data.operating_hours / 1000
    annual_elec_revenue = annual_elec_MWh * 1000 * input_data.electricity_price_eur_kwh
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.fuel_price_eur_kwh

    # --- Benchmark ---
    benchmark = _get_turbine_benchmark(eta_ex, input_data.turbine_type)

    result = SteamTurbineResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out_flow,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=heat_recovered if input_data.is_chp else None,
        shaft_power_kW=W_shaft,
        electrical_power_kW=W_electrical,
        exhaust_exergy_kW=Ex_out_flow,
        isentropic_efficiency_actual=input_data.isentropic_efficiency,
        heat_recovered_kW=heat_recovered if input_data.is_chp else None,
        heat_recovered_exergy_kW=heat_recovered_exergy if input_data.is_chp else None,
        total_useful_exergy_kW=total_useful_exergy,
        chp_exergy_efficiency_pct=chp_eta_ex if input_data.is_chp else None,
        annual_electricity_MWh=annual_elec_MWh,
        annual_electricity_revenue_EUR=annual_elec_revenue,
        benchmark_comparison=benchmark,
    )

    # AV/UN split — construct new instance to trigger __post_init__ recalculation
    if _calc_avoidable and Ex_destroyed > 0:
        ref_params = UNAVOIDABLE_REF_STEAM_TURBINE.get(input_data.turbine_type, {})
        if ref_params:
            fields_dict = {f.name: getattr(input_data, f.name) for f in dataclasses.fields(type(input_data))}
            fields_dict.update(ref_params)
            if input_data.is_chp:
                fields_dict['heat_recovery_fraction'] = max(input_data.heat_recovery_fraction, 0.85)
            fields_dict['outlet_temp_C'] = None  # Force __post_init__ to recalculate
            un_input = type(input_data)(**fields_dict)
            un_result = analyze_steam_turbine(un_input, dead_state=dead_state, _calc_avoidable=False)
            av, un, ratio = compute_avoidable_split(Ex_destroyed, un_result.exergy_destroyed_kW)
            result.exergy_destroyed_avoidable_kW = av
            result.exergy_destroyed_unavoidable_kW = un
            result.avoidable_ratio_pct = ratio

    return result


# ---------------------------------------------------------------------------
# Sankey data
# ---------------------------------------------------------------------------

def generate_steam_turbine_sankey_data(result: SteamTurbineResult, turbine_type: str = "backpressure") -> dict:
    """
    Buhar türbini Sankey diyagramı için node ve link verisi oluşturur.

    Normal mod: Buhar Exergy → [Shaft Work, Egzoz Exergy, Yıkım]
    CHP modu:   Buhar Exergy → [Elektrik, Isı Geri Kazanım, Egzoz, Yıkım]
    """
    Ex_in = result.exergy_in_kW or 0
    W_shaft = result.shaft_power_kW or 0
    Ex_exhaust = result.exhaust_exergy_kW or 0
    Ex_destroyed = result.exergy_destroyed_kW or 0

    is_chp = result.heat_recovered_kW is not None and result.heat_recovered_kW > 0

    # Normalize
    total_out = W_shaft + Ex_exhaust + Ex_destroyed
    if total_out > 0 and abs(total_out - Ex_in) > 0.1:
        scale = Ex_in / total_out
        W_shaft *= scale
        Ex_exhaust *= scale
        Ex_destroyed *= scale

    # AV/UN split for destruction node
    av_kW = getattr(result, 'exergy_destroyed_avoidable_kW', 0.0) or 0.0
    un_kW = getattr(result, 'exergy_destroyed_unavoidable_kW', 0.0) or 0.0
    has_av_un = (av_kW > 0 or un_kW > 0)

    # Scale AV/UN to match normalized Ex_destroyed
    if has_av_un:
        av_un_total = av_kW + un_kW
        if av_un_total > 0:
            av_norm = Ex_destroyed * (av_kW / av_un_total)
            un_norm = Ex_destroyed * (un_kW / av_un_total)
        else:
            av_norm = Ex_destroyed
            un_norm = 0.0

    if is_chp:
        W_elec = result.electrical_power_kW or 0
        heat_rec_ex = result.heat_recovered_exergy_kW or 0

        if has_av_un:
            nodes = [
                {"id": 0, "name": "Buhar Exergy", "name_en": "Steam Exergy"},
                {"id": 1, "name": "Elektrik Uretimi", "name_en": "Electricity Generation"},
                {"id": 2, "name": "Isi Geri Kazanim", "name_en": "Heat Recovery"},
                {"id": 3, "name": "Egzoz Exergy", "name_en": "Exhaust Exergy"},
                {"id": 4, "name": "Exergy Yikimi (Onlenebilir)", "name_en": "Exergy Destruction (Avoidable)", "color": "#e74c3c"},
                {"id": 5, "name": "Exergy Yikimi (Onlenemez)", "name_en": "Exergy Destruction (Unavoidable)", "color": "#95a5a6"},
            ]
            links = []
            if W_elec > 0:
                links.append({"source": 0, "target": 1, "value": round(W_elec, 2), "label": "Elektrik Cikisi"})
            if heat_rec_ex > 0:
                links.append({"source": 0, "target": 2, "value": round(heat_rec_ex, 2), "label": "Isi Geri Kazanimi"})
            remaining_exhaust = max(Ex_exhaust - heat_rec_ex, 0)
            if remaining_exhaust > 0:
                links.append({"source": 0, "target": 3, "value": round(remaining_exhaust, 2), "label": "Egzoz Kaybi"})
            if av_norm > 0.01:
                links.append({"source": 0, "target": 4, "value": round(av_norm, 2), "label": "Onlenebilir Kayiplar"})
            if un_norm > 0.01:
                links.append({"source": 0, "target": 5, "value": round(un_norm, 2), "label": "Onlenemez Kayiplar"})
        else:
            nodes = [
                {"id": 0, "name": "Buhar Exergy", "name_en": "Steam Exergy"},
                {"id": 1, "name": "Elektrik Uretimi", "name_en": "Electricity Generation"},
                {"id": 2, "name": "Isi Geri Kazanim", "name_en": "Heat Recovery"},
                {"id": 3, "name": "Egzoz Exergy", "name_en": "Exhaust Exergy"},
                {"id": 4, "name": "Exergy Yikimi", "name_en": "Exergy Destruction"},
            ]
            links = []
            if W_elec > 0:
                links.append({"source": 0, "target": 1, "value": round(W_elec, 2), "label": "Elektrik Cikisi"})
            if heat_rec_ex > 0:
                links.append({"source": 0, "target": 2, "value": round(heat_rec_ex, 2), "label": "Isi Geri Kazanimi"})
            remaining_exhaust = max(Ex_exhaust - heat_rec_ex, 0)
            if remaining_exhaust > 0:
                links.append({"source": 0, "target": 3, "value": round(remaining_exhaust, 2), "label": "Egzoz Kaybi"})
            if Ex_destroyed > 0:
                links.append({"source": 0, "target": 4, "value": round(Ex_destroyed, 2), "label": "Tersinmezlik"})
    else:
        if has_av_un:
            nodes = [
                {"id": 0, "name": "Buhar Exergy", "name_en": "Steam Exergy"},
                {"id": 1, "name": "Shaft Work", "name_en": "Shaft Work"},
                {"id": 2, "name": "Egzoz Exergy", "name_en": "Exhaust Exergy"},
                {"id": 3, "name": "Exergy Yikimi (Onlenebilir)", "name_en": "Exergy Destruction (Avoidable)", "color": "#e74c3c"},
                {"id": 4, "name": "Exergy Yikimi (Onlenemez)", "name_en": "Exergy Destruction (Unavoidable)", "color": "#95a5a6"},
            ]
            links = []
            if W_shaft > 0:
                links.append({"source": 0, "target": 1, "value": round(W_shaft, 2), "label": "Mekanik Is"})
            if Ex_exhaust > 0:
                links.append({"source": 0, "target": 2, "value": round(Ex_exhaust, 2), "label": "Egzoz Kaybi"})
            if av_norm > 0.01:
                links.append({"source": 0, "target": 3, "value": round(av_norm, 2), "label": "Onlenebilir Kayiplar"})
            if un_norm > 0.01:
                links.append({"source": 0, "target": 4, "value": round(un_norm, 2), "label": "Onlenemez Kayiplar"})
        else:
            nodes = [
                {"id": 0, "name": "Buhar Exergy", "name_en": "Steam Exergy"},
                {"id": 1, "name": "Shaft Work", "name_en": "Shaft Work"},
                {"id": 2, "name": "Egzoz Exergy", "name_en": "Exhaust Exergy"},
                {"id": 3, "name": "Exergy Yikimi", "name_en": "Exergy Destruction"},
            ]
            links = []
            if W_shaft > 0:
                links.append({"source": 0, "target": 1, "value": round(W_shaft, 2), "label": "Mekanik Is"})
            if Ex_exhaust > 0:
                links.append({"source": 0, "target": 2, "value": round(Ex_exhaust, 2), "label": "Egzoz Kaybi"})
            if Ex_destroyed > 0:
                links.append({"source": 0, "target": 3, "value": round(Ex_destroyed, 2), "label": "Tersinmezlik"})

    title = 'Buhar Turbini Exergy Akisi' + (' (CHP)' if is_chp else '')

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(W_shaft, 2),
            "recoverable_heat_kW": round(result.heat_recovered_exergy_kW or 0, 2),
            "irreversibility_kW": round(Ex_destroyed, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
            "exergy_destroyed_avoidable_kW": round(av_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(un_kW, 2),
            "avoidable_ratio_pct": round(getattr(result, 'avoidable_ratio_pct', 0.0) or 0.0, 1),
        },
    }


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_steam_turbine_recommendations(result: SteamTurbineResult, input_data: SteamTurbineInput) -> list:
    """Analiz sonuçlarına göre iyileştirme önerileri"""
    recommendations = []

    # 1. CHP değilse ve egzoz exergy yüksekse → CHP öner
    if not input_data.is_chp and result.exhaust_exergy_kW and result.exhaust_exergy_kW > 100:
        potential_heat = result.exhaust_exergy_kW * 0.6
        savings = potential_heat * input_data.operating_hours * input_data.fuel_price_eur_kwh
        recommendations.append({
            'type': 'chp_conversion',
            'title': 'Kojenerasyon (CHP) Donusumu',
            'description': f'Egzoz buharinda {result.exhaust_exergy_kW:.0f} kW exergy mevcut. '
                          f'CHP ile isi geri kazanimi onerilir.',
            'investment_eur': 50000,
            'savings_eur_year': savings,
            'payback_years': 50000 / savings if savings > 0 else float('inf'),
            'priority': 'high' if savings > 20000 else 'medium',
        })

    # 2. Düşük izentropik verim → bakım
    if input_data.isentropic_efficiency < 0.75:
        savings = result.annual_loss_EUR * 0.15 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'overhaul',
            'title': 'Turbin Revizyonu',
            'description': f'Izentropik verim dusuk ({input_data.isentropic_efficiency:.0%}). '
                          f'Kanat erozyonu veya sizdirma olabilir.',
            'investment_eur': 30000,
            'savings_eur_year': savings,
            'payback_years': 30000 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # 3. Düşük superheat → kızgınlık artırma
    T_sat_in = _get_saturation_temp_C(input_data.inlet_pressure_bar)
    superheat = input_data.inlet_temp_C - T_sat_in
    if superheat < 50:
        savings = result.annual_electricity_revenue_EUR * 0.05 if result.annual_electricity_revenue_EUR else 0
        recommendations.append({
            'type': 'superheat_increase',
            'title': 'Buhar Kizginligini Artir',
            'description': f'Kizginlik sadece {superheat:.0f} C. '
                          f'Daha yuksek kizginlik ile turbin verimi artar.',
            'investment_eur': 20000,
            'savings_eur_year': savings,
            'payback_years': 20000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # 4. Backpressure — basınç optimizasyonu
    if input_data.turbine_type == 'backpressure' and input_data.outlet_pressure_bar > 5.0:
        savings = result.annual_electricity_revenue_EUR * 0.08 if result.annual_electricity_revenue_EUR else 0
        recommendations.append({
            'type': 'backpressure_optimization',
            'title': 'Karsi Basinc Optimizasyonu',
            'description': f'Cikis basinci {input_data.outlet_pressure_bar} bar. '
                          f'Proses gereksinimlerine gore dusurme imkani arastirilmali.',
            'investment_eur': 5000,
            'savings_eur_year': savings,
            'payback_years': 5000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    return recommendations


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_turbine_benchmark(eta_ex: float, turbine_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması"""
    benchmarks = {
        'condensing':   {'poor': 50, 'average': 65, 'good': 75, 'excellent': 82},
        'backpressure': {'poor': 40, 'average': 55, 'good': 70, 'excellent': 80},
        'extraction':   {'poor': 45, 'average': 60, 'good': 72, 'excellent': 80},
    }
    thresholds = benchmarks.get(turbine_type, benchmarks['backpressure'])

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


def _calculate_percentile(eta_ex: float, turbine_type: str) -> int:
    """Exergy verimini 0-100 yuzdelik dilime esler."""
    benchmarks = {
        'condensing':   {'low': 45, 'mid': 65, 'high': 82},
        'backpressure': {'low': 35, 'mid': 55, 'high': 80},
        'extraction':   {'low': 40, 'mid': 60, 'high': 80},
    }
    thresholds = benchmarks.get(turbine_type, benchmarks['backpressure'])

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
