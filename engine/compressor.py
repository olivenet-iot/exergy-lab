"""
ExergyLab - Compressor Exergy Analysis

Kompresör exergy hesaplamaları.
Vidalı, pistonlu, scroll ve santrifüj kompresör tipleri için.
"""

from dataclasses import dataclass
from typing import Optional
import math

import copy

from .core import (
    DeadState, ExergyResult, compute_avoidable_split,
    R_AIR, CP_AIR, celsius_to_kelvin, bar_to_kpa,
    m3_min_to_m3_s, air_density, heat_exergy
)
from .exergoeconomic import _apply_exergoeconomic


# Best-achievable isentropic efficiency per compressor type (Tsatsaronis & Morosuk 2008)
UNAVOIDABLE_REF_COMPRESSOR = {
    'screw': {'eta_is_best': 0.90},
    'piston': {'eta_is_best': 0.88},
    'scroll': {'eta_is_best': 0.85},
    'centrifugal': {'eta_is_best': 0.92},
}


# ---------------------------------------------------------------------------
# Input dataclasses
# ---------------------------------------------------------------------------

@dataclass
class CompressorInput:
    """Kompresör analizi için giriş verileri (vidalı / genel)"""

    # Zorunlu
    power_kW: float              # Elektrik gücü [kW]
    flow_rate_m3_min: float      # Hava debisi [m³/min]
    outlet_pressure_bar: float   # Çıkış basıncı [bar]

    # Opsiyonel - ölçülen
    inlet_temp_C: Optional[float] = None    # Giriş sıcaklığı [°C]
    outlet_temp_C: Optional[float] = None   # Çıkış sıcaklığı [°C]
    ambient_temp_C: Optional[float] = None  # Ortam sıcaklığı [°C]

    # Operasyonel
    operating_hours: float = 4000           # Yıllık çalışma [saat]
    load_factor: float = 0.75               # Yük faktörü [0-1]

    # Ekonomik
    electricity_price_eur_kwh: float = 0.10  # Elektrik fiyatı [€/kWh]
    equipment_cost_eur: Optional[float] = None  # Ekipman maliyeti PEC [€]

    # Ekipman bilgisi
    compressor_type: str = "screw"          # screw, piston, scroll, centrifugal
    brand: Optional[str] = None
    model: Optional[str] = None
    age_years: Optional[int] = None

    def __post_init__(self):
        """Varsayılan değerleri ayarla"""
        if self.ambient_temp_C is None:
            self.ambient_temp_C = 25.0
        if self.inlet_temp_C is None:
            self.inlet_temp_C = self.ambient_temp_C
        if self.outlet_temp_C is None:
            defaults = {
                'screw': 85,
                'piston': 140,
                'scroll': 90,
                'centrifugal': 120
            }
            self.outlet_temp_C = defaults.get(self.compressor_type, 85)


@dataclass
class PistonCompressorInput(CompressorInput):
    """Pistonlu kompresör giriş verileri"""
    stages: int = 1                  # Kademe sayısı (1-4)
    cooling_type: str = "air"        # Soğutma tipi: "air" veya "water"

    def __post_init__(self):
        self.compressor_type = "piston"
        super().__post_init__()


@dataclass
class ScrollCompressorInput(CompressorInput):
    """Scroll kompresör giriş verileri"""
    oil_free: bool = False           # Yağsız mı?

    def __post_init__(self):
        self.compressor_type = "scroll"
        super().__post_init__()


@dataclass
class CentrifugalCompressorInput(CompressorInput):
    """Santrifüj kompresör giriş verileri"""
    stages: int = 1                  # Kademe sayısı (1-5)
    igv_position: float = 100.0      # Inlet guide vane pozisyonu (0-100%)

    def __post_init__(self):
        self.compressor_type = "centrifugal"
        super().__post_init__()


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class CompressorResult(ExergyResult):
    """Kompresör analizi sonuçları"""

    mass_flow_kg_s: Optional[float] = None
    specific_power_kW_m3min: Optional[float] = None
    heat_recovery_potential_kW: Optional[float] = None
    heat_recovery_savings_eur_year: Optional[float] = None
    benchmark_comparison: Optional[str] = None  # "poor", "average", "good", "excellent"

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'mass_flow_kg_s': round(self.mass_flow_kg_s, 4) if self.mass_flow_kg_s else None,
            'specific_power_kW_m3min': round(self.specific_power_kW_m3min, 2) if self.specific_power_kW_m3min else None,
            'heat_recovery_potential_kW': round(self.heat_recovery_potential_kW, 2) if self.heat_recovery_potential_kW else None,
            'heat_recovery_savings_eur_year': round(self.heat_recovery_savings_eur_year, 0) if self.heat_recovery_savings_eur_year else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base

    def to_api_dict(self, compressor_type: str = "screw") -> dict:
        """API yanıt formatına dönüştürür."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "mass_flow_kg_s": round(self.mass_flow_kg_s, 4) if self.mass_flow_kg_s else None,
            "specific_power_kW_m3min": round(self.specific_power_kW_m3min, 2) if self.specific_power_kW_m3min else None,
            "heat_recovery_potential_kW": round(self.heat_recovery_potential_kW, 2) if self.heat_recovery_potential_kW else None,
            "heat_recovery_savings_eur_year": round(self.heat_recovery_savings_eur_year, 0) if self.heat_recovery_savings_eur_year else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, compressor_type),
            "comparison_text": _get_comparison_text(self.benchmark_comparison),
            "exergy_destroyed_avoidable_kW": round(self.exergy_destroyed_avoidable_kW, 2),
            "exergy_destroyed_unavoidable_kW": round(self.exergy_destroyed_unavoidable_kW, 2),
            "avoidable_ratio_pct": round(self.avoidable_ratio_pct, 1),
            "exergoeconomic_Z_dot_eur_h": round(self.exergoeconomic_Z_dot_eur_h, 4),
            "exergoeconomic_C_dot_destruction_eur_h": round(self.exergoeconomic_C_dot_destruction_eur_h, 4),
            "exergoeconomic_f_factor": round(self.exergoeconomic_f_factor, 4),
            "exergoeconomic_r_factor": round(self.exergoeconomic_r_factor, 4),
            "exergoeconomic_c_product_eur_kWh": round(self.exergoeconomic_c_product_eur_kWh, 4),
            "exergoeconomic_total_cost_rate_eur_h": round(self.exergoeconomic_total_cost_rate_eur_h, 4),
        }


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _calculate_exergy_output(m_dot: float, T_out_K: float, P_out_kPa: float,
                             dead_state: DeadState) -> float:
    """
    Basınçlı havanın exergy'sini hesaplar.

    Genel formül (section 1.4):
      Ex_air = m_dot * [Cp*(T2-T0) - T0*Cp*ln(T2/T0) + R*T0*ln(P2/P1)]

    |T_out - T0| <= 10K ise basitleştirilmiş izothermal formül:
      Ex_air = m_dot * R * T0 * ln(P2/P1)
    """
    T0 = dead_state.T0
    P0 = dead_state.P0
    pressure_ratio = P_out_kPa / P0

    if abs(T_out_K - T0) <= 10.0:
        # İzothermal yaklaşım
        return m_dot * R_AIR * T0 * math.log(pressure_ratio)
    else:
        # Genel formül (termal + mekanik exergy)
        thermal = CP_AIR * (T_out_K - T0) - T0 * CP_AIR * math.log(T_out_K / T0)
        mechanical = R_AIR * T0 * math.log(pressure_ratio)
        return m_dot * (thermal + mechanical)


def _build_result(Ex_in: float, Ex_out: float, m_dot: float, T_out_K: float,
                  power_kW: float, flow_rate_m3_min: float,
                  hours: float, price: float,
                  compressor_type: str, dead_state: DeadState) -> CompressorResult:
    """Ortak sonuç hesaplama ve oluşturma."""
    Ex_destroyed = Ex_in - Ex_out
    eta_ex = (Ex_out / Ex_in) * 100 if Ex_in > 0 else 0.0

    annual_loss_kWh = Ex_destroyed * hours
    annual_loss_EUR = annual_loss_kWh * price

    # Isı geri kazanım potansiyeli
    heat_recovery_exergy = heat_exergy(Ex_destroyed, T_out_K, dead_state)

    gas_price_eur_kwh = 0.06
    recoverable_thermal = Ex_destroyed * 0.70 * 0.85  # %70 ısıya, %85 HRU verimi
    heat_recovery_savings = recoverable_thermal * hours * 0.70 * gas_price_eur_kwh

    specific_power = power_kW / flow_rate_m3_min if flow_rate_m3_min > 0 else 0.0

    benchmark = _get_benchmark_comparison(eta_ex, compressor_type)

    return CompressorResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=heat_recovery_exergy,
        mass_flow_kg_s=m_dot,
        specific_power_kW_m3min=specific_power,
        heat_recovery_potential_kW=recoverable_thermal,
        heat_recovery_savings_eur_year=heat_recovery_savings,
        benchmark_comparison=benchmark,
    )


# ---------------------------------------------------------------------------
# Analysis functions
# ---------------------------------------------------------------------------

def _apply_avoidable_split(result: CompressorResult, input_data, dead_state: DeadState, analyze_fn, _calc_avoidable: bool) -> CompressorResult:
    """
    Apply AV/UN split to a compressor result.

    For compressors, best-achievable technology means higher isentropic
    efficiency → lower power consumption for same output.

    Two cases:
    1. Outlet temp > isentropic temp (no aftercooling): improve via eta_is
    2. Outlet temp <= isentropic temp (aftercooled): reduce power input
       while keeping same flow + pressure + outlet temp
    """
    if not _calc_avoidable or result.exergy_destroyed_kW <= 0:
        return result

    ref = UNAVOIDABLE_REF_COMPRESSOR.get(input_data.compressor_type, {'eta_is_best': 0.90})
    eta_is_best = ref['eta_is_best']

    P_ratio = bar_to_kpa(input_data.outlet_pressure_bar) / dead_state.P0
    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    gamma = 1.4
    T_isentropic_K = T_in_K * (P_ratio) ** ((gamma - 1) / gamma)

    un_input = copy.deepcopy(input_data)

    if T_out_K >= T_isentropic_K:
        # Case 1: No aftercooling — outlet temp encodes efficiency
        eta_is_actual = (T_isentropic_K - T_in_K) / (T_out_K - T_in_K)
        if eta_is_actual >= eta_is_best:
            result.exergy_destroyed_unavoidable_kW = result.exergy_destroyed_kW
            return result
        T_out_best_K = T_in_K + (T_isentropic_K - T_in_K) / eta_is_best
        un_input.outlet_temp_C = T_out_best_K - 273.15
    else:
        # Case 2: Aftercooled — compute best-case power from isentropic work
        V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)
        rho = air_density(T_in_K, dead_state.P0)
        m_dot = V_dot_m3_s * rho
        # Isentropic work: W_is = m_dot * cp * (T_isen - T_in)
        W_isentropic = m_dot * CP_AIR * (T_isentropic_K - T_in_K)
        best_power = W_isentropic / eta_is_best
        if best_power >= input_data.power_kW:
            result.exergy_destroyed_unavoidable_kW = result.exergy_destroyed_kW
            return result
        un_input.power_kW = best_power

    un_result = analyze_fn(un_input, dead_state=dead_state, _calc_avoidable=False)

    av, un, ratio = compute_avoidable_split(result.exergy_destroyed_kW, un_result.exergy_destroyed_kW)
    result.exergy_destroyed_avoidable_kW = av
    result.exergy_destroyed_unavoidable_kW = un
    result.avoidable_ratio_pct = ratio
    return result


def analyze_compressor(input_data: CompressorInput, dead_state: DeadState = None, _calc_avoidable: bool = True) -> CompressorResult:
    """
    Kompresör exergy analizi yapar (vidalı / genel).

    Args:
        input_data: Kompresör giriş verileri
        dead_state: Dead state koşulları (opsiyonel)
        _calc_avoidable: AV/UN hesaplaması yapılsın mı (iç kullanım)

    Returns:
        CompressorResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    P_out_kPa = bar_to_kpa(input_data.outlet_pressure_bar)
    V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)

    rho = air_density(T_in_K, dead_state.P0)
    m_dot = V_dot_m3_s * rho

    Ex_in = input_data.power_kW
    Ex_out = _calculate_exergy_output(m_dot, T_out_K, P_out_kPa, dead_state)

    result = _build_result(
        Ex_in=Ex_in, Ex_out=Ex_out, m_dot=m_dot, T_out_K=T_out_K,
        power_kW=input_data.power_kW,
        flow_rate_m3_min=input_data.flow_rate_m3_min,
        hours=input_data.operating_hours,
        price=input_data.electricity_price_eur_kwh,
        compressor_type=input_data.compressor_type,
        dead_state=dead_state,
    )

    result = _apply_avoidable_split(result, input_data, dead_state, analyze_compressor, _calc_avoidable)

    _apply_exergoeconomic(
        result, equipment_type='compressor',
        c_fuel_eur_kWh=input_data.electricity_price_eur_kwh,
        capacity_param_kW=input_data.power_kW,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
    )

    return result


def analyze_piston_compressor(input_data: PistonCompressorInput,
                              dead_state: DeadState = None, _calc_avoidable: bool = True) -> CompressorResult:
    """
    Pistonlu kompresör exergy analizi.
    Politropik model: n=1.3 (hava soğutmalı), n=1.1 (su soğutmalı).
    Çok kademeli destek.
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    P_out_kPa = bar_to_kpa(input_data.outlet_pressure_bar)
    V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)

    rho = air_density(T_in_K, dead_state.P0)
    m_dot = V_dot_m3_s * rho

    Ex_in = input_data.power_kW
    Ex_out = _calculate_exergy_output(m_dot, T_out_K, P_out_kPa, dead_state)

    result = _build_result(
        Ex_in=Ex_in, Ex_out=Ex_out, m_dot=m_dot, T_out_K=T_out_K,
        power_kW=input_data.power_kW,
        flow_rate_m3_min=input_data.flow_rate_m3_min,
        hours=input_data.operating_hours,
        price=input_data.electricity_price_eur_kwh,
        compressor_type="piston",
        dead_state=dead_state,
    )

    result = _apply_avoidable_split(result, input_data, dead_state, analyze_piston_compressor, _calc_avoidable)

    _apply_exergoeconomic(
        result, equipment_type='compressor',
        c_fuel_eur_kWh=input_data.electricity_price_eur_kwh,
        capacity_param_kW=input_data.power_kW,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
    )

    return result


def analyze_scroll_compressor(input_data: ScrollCompressorInput,
                              dead_state: DeadState = None, _calc_avoidable: bool = True) -> CompressorResult:
    """
    Scroll kompresör exergy analizi.
    Tek kademeli, yağsız seçeneği.
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    P_out_kPa = bar_to_kpa(input_data.outlet_pressure_bar)
    V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)

    rho = air_density(T_in_K, dead_state.P0)
    m_dot = V_dot_m3_s * rho

    Ex_in = input_data.power_kW
    Ex_out = _calculate_exergy_output(m_dot, T_out_K, P_out_kPa, dead_state)

    result = _build_result(
        Ex_in=Ex_in, Ex_out=Ex_out, m_dot=m_dot, T_out_K=T_out_K,
        power_kW=input_data.power_kW,
        flow_rate_m3_min=input_data.flow_rate_m3_min,
        hours=input_data.operating_hours,
        price=input_data.electricity_price_eur_kwh,
        compressor_type="scroll",
        dead_state=dead_state,
    )

    result = _apply_avoidable_split(result, input_data, dead_state, analyze_scroll_compressor, _calc_avoidable)

    _apply_exergoeconomic(
        result, equipment_type='compressor',
        c_fuel_eur_kWh=input_data.electricity_price_eur_kwh,
        capacity_param_kW=input_data.power_kW,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
    )

    return result


def analyze_centrifugal_compressor(input_data: CentrifugalCompressorInput,
                                   dead_state: DeadState = None, _calc_avoidable: bool = True) -> CompressorResult:
    """
    Santrifüj kompresör exergy analizi.
    Çok kademeli, IGV pozisyon takibi.
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    P_out_kPa = bar_to_kpa(input_data.outlet_pressure_bar)
    V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)

    rho = air_density(T_in_K, dead_state.P0)
    m_dot = V_dot_m3_s * rho

    Ex_in = input_data.power_kW
    Ex_out = _calculate_exergy_output(m_dot, T_out_K, P_out_kPa, dead_state)

    result = _build_result(
        Ex_in=Ex_in, Ex_out=Ex_out, m_dot=m_dot, T_out_K=T_out_K,
        power_kW=input_data.power_kW,
        flow_rate_m3_min=input_data.flow_rate_m3_min,
        hours=input_data.operating_hours,
        price=input_data.electricity_price_eur_kwh,
        compressor_type="centrifugal",
        dead_state=dead_state,
    )

    result = _apply_avoidable_split(result, input_data, dead_state, analyze_centrifugal_compressor, _calc_avoidable)

    _apply_exergoeconomic(
        result, equipment_type='compressor',
        c_fuel_eur_kWh=input_data.electricity_price_eur_kwh,
        capacity_param_kW=input_data.power_kW,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
    )

    return result


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_benchmark_comparison(eta_ex: float, compressor_type: str) -> str:
    """Exergy verimine göre benchmark karşılaştırması yapar."""
    benchmarks = {
        'screw': {'poor': 30, 'average': 45, 'good': 55, 'excellent': 60},
        'piston': {'poor': 25, 'average': 40, 'good': 50, 'excellent': 55},
        'scroll': {'poor': 30, 'average': 45, 'good': 55, 'excellent': 60},
        'centrifugal': {'poor': 35, 'average': 50, 'good': 60, 'excellent': 65},
    }

    thresholds = benchmarks.get(compressor_type, benchmarks['screw'])

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


def _calculate_percentile(eta_ex: float, compressor_type: str) -> int:
    """Exergy verimini 0-100 yüzdelik dilime eşler."""
    benchmarks = {
        'screw': {'low': 25, 'mid': 45, 'high': 65},
        'piston': {'low': 20, 'mid': 40, 'high': 60},
        'scroll': {'low': 25, 'mid': 45, 'high': 65},
        'centrifugal': {'low': 30, 'mid': 50, 'high': 70},
    }
    thresholds = benchmarks.get(compressor_type, benchmarks['screw'])

    if eta_ex <= thresholds['low']:
        return max(0, int(eta_ex / thresholds['low'] * 25))
    elif eta_ex <= thresholds['mid']:
        return 25 + int((eta_ex - thresholds['low']) / (thresholds['mid'] - thresholds['low']) * 25)
    elif eta_ex <= thresholds['high']:
        return 50 + int((eta_ex - thresholds['mid']) / (thresholds['high'] - thresholds['mid']) * 25)
    else:
        return min(100, 75 + int((eta_ex - thresholds['high']) / 15 * 25))


def _get_comparison_text(benchmark: str) -> str:
    """Benchmark sonucuna göre Türkçe açıklama döndürür."""
    texts = {
        'poor': 'Exergy verimi düşük. Acil iyileştirme önerilir.',
        'below_average': 'Exergy verimi ortalamanın altında. İyileştirme potansiyeli yüksek.',
        'average': 'Exergy verimi ortalama seviyede. İyileştirme fırsatları mevcut.',
        'good': 'Exergy verimi iyi seviyede. Sınırlı iyileştirme potansiyeli.',
        'excellent': 'Exergy verimi mükemmel. En iyi uygulama seviyesinde.',
    }
    return texts.get(benchmark, '')


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_compressor_recommendations(result: CompressorResult, input_data: CompressorInput) -> list:
    """
    Analiz sonuçlarına göre iyileştirme önerileri üretir.

    Returns:
        List of recommendation dictionaries
    """
    recommendations = []

    # 1. Isı geri kazanımı değerlendirmesi
    if input_data.power_kW >= 15 and result.heat_recovery_savings_eur_year and result.heat_recovery_savings_eur_year > 1000:
        investment = _estimate_hru_cost(input_data.power_kW)
        payback = investment / result.heat_recovery_savings_eur_year if result.heat_recovery_savings_eur_year > 0 else float('inf')

        recommendations.append({
            'type': 'heat_recovery',
            'title': 'Atık Isı Geri Kazanımı',
            'description': f'Kompresör atık ısısından yılda {result.heat_recovery_savings_eur_year:.0f} € tasarruf potansiyeli',
            'investment_eur': investment,
            'savings_eur_year': result.heat_recovery_savings_eur_year,
            'payback_years': payback,
            'priority': 'high' if payback < 2 else 'medium' if payback < 4 else 'low'
        })

    # 2. Verim düşükse genel öneriler
    if result.benchmark_comparison in ['poor', 'below_average']:
        savings_est = result.annual_loss_EUR * 0.10 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'maintenance',
            'title': 'Bakım ve Kontrol',
            'description': 'Exergy verimi düşük. Filtre, yağ, conta kontrolü önerilir.',
            'investment_eur': 500,
            'savings_eur_year': savings_est,
            'payback_years': 500 / savings_est if savings_est > 0 else float('inf'),
            'priority': 'high'
        })

    # 3. Spesifik güç yüksekse
    if result.specific_power_kW_m3min and result.specific_power_kW_m3min > 7.0:
        savings_est = result.annual_loss_EUR * 0.07 if result.annual_loss_EUR else 0
        recommendations.append({
            'type': 'pressure_optimization',
            'title': 'Basınç Optimizasyonu',
            'description': 'Spesifik güç yüksek. Sistem basıncını düşürme imkanı araştırılmalı.',
            'investment_eur': 0,
            'savings_eur_year': savings_est,
            'payback_years': 0,
            'priority': 'high'
        })

    # 4. VSD önerisi
    if input_data.load_factor < 0.85:
        estimated_savings = input_data.power_kW * (1 - input_data.load_factor) * 0.30 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        vsd_cost = input_data.power_kW * 80  # ~80 €/kW
        payback = vsd_cost / estimated_savings if estimated_savings > 0 else float('inf')
        recommendations.append({
            'type': 'vsd',
            'title': 'Değişken Hız Sürücüsü (VSD)',
            'description': f'Yük faktörü %{input_data.load_factor*100:.0f}. VSD ile yılda {estimated_savings:.0f} € tasarruf potansiyeli.',
            'investment_eur': vsd_cost,
            'savings_eur_year': estimated_savings,
            'payback_years': payback,
            'priority': 'high' if payback < 3 else 'medium' if payback < 5 else 'low'
        })

    # 5. Kaçak kontrolü
    if input_data.operating_hours >= 4000:
        leak_savings = input_data.power_kW * 0.20 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'leak_detection',
            'title': 'Hava Kaçağı Tespiti',
            'description': 'Endüstriyel sistemlerde tipik %15-25 kaçak oranı. Ultrasonik tespit önerilir.',
            'investment_eur': 2000,
            'savings_eur_year': leak_savings,
            'payback_years': 2000 / leak_savings if leak_savings > 0 else float('inf'),
            'priority': 'medium'
        })

    # 6. Giriş filtresi
    recommendations.append({
        'type': 'inlet_filter',
        'title': 'Giriş Filtresi Optimizasyonu',
        'description': 'Temiz filtre ile %1-3 enerji tasarrufu sağlanabilir.',
        'investment_eur': 200,
        'savings_eur_year': input_data.power_kW * 0.02 * input_data.operating_hours * input_data.electricity_price_eur_kwh,
        'payback_years': 0.5,
        'priority': 'low'
    })

    # 7. Kurutucu optimizasyonu
    recommendations.append({
        'type': 'dryer_optimization',
        'title': 'Kurutucu Optimizasyonu',
        'description': 'Enerji verimli kurutucu seçimi veya mevcut kurucunun optimizasyonu.',
        'investment_eur': 3000,
        'savings_eur_year': input_data.power_kW * 0.05 * input_data.operating_hours * input_data.electricity_price_eur_kwh,
        'payback_years': 3000 / (input_data.power_kW * 0.05 * input_data.operating_hours * input_data.electricity_price_eur_kwh) if input_data.power_kW > 0 else float('inf'),
        'priority': 'low'
    })

    # 8. Sistem tasarımı
    recommendations.append({
        'type': 'system_design',
        'title': 'Sistem Tasarımı İyileştirme',
        'description': 'Boru çapları, depolama hacmi ve dağıtım optimizasyonu.',
        'investment_eur': 5000,
        'savings_eur_year': input_data.power_kW * 0.03 * input_data.operating_hours * input_data.electricity_price_eur_kwh,
        'payback_years': 5000 / (input_data.power_kW * 0.03 * input_data.operating_hours * input_data.electricity_price_eur_kwh) if input_data.power_kW > 0 else float('inf'),
        'priority': 'low'
    })

    return recommendations


def _estimate_hru_cost(power_kW: float) -> float:
    """HRU yatırım maliyeti tahmini"""
    if power_kW < 30:
        return 3500
    elif power_kW < 75:
        return 7000
    elif power_kW < 150:
        return 12000
    else:
        return 25000
