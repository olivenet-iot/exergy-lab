"""
ExergyLab - Compressor Exergy Analysis

Kompresör exergy hesaplamaları.
Vidalı, pistonlu ve diğer kompresör tipleri için.
"""

from dataclasses import dataclass
from typing import Optional
import math

from .core import (
    DeadState, ExergyResult,
    R_AIR, celsius_to_kelvin, bar_to_kpa,
    m3_min_to_m3_s, air_density, heat_exergy
)


@dataclass
class CompressorInput:
    """Kompresör analizi için giriş verileri"""

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
            # Tip bazlı varsayılan çıkış sıcaklığı
            defaults = {
                'screw': 85,
                'piston': 140,
                'scroll': 90,
                'centrifugal': 120
            }
            self.outlet_temp_C = defaults.get(self.compressor_type, 85)


@dataclass
class CompressorResult(ExergyResult):
    """Kompresör analizi sonuçları"""

    # Ek kompresör-spesifik sonuçlar
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


def analyze_compressor(input_data: CompressorInput, dead_state: DeadState = None) -> CompressorResult:
    """
    Kompresör exergy analizi yapar.

    Args:
        input_data: Kompresör giriş verileri
        dead_state: Dead state koşulları (opsiyonel)

    Returns:
        CompressorResult: Analiz sonuçları
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    # Birim dönüşümleri
    T_in_K = celsius_to_kelvin(input_data.inlet_temp_C)
    T_out_K = celsius_to_kelvin(input_data.outlet_temp_C)
    P_out_kPa = bar_to_kpa(input_data.outlet_pressure_bar)
    V_dot_m3_s = m3_min_to_m3_s(input_data.flow_rate_m3_min)

    # Kütle debisi
    rho = air_density(T_in_K, dead_state.P0)
    m_dot = V_dot_m3_s * rho  # kg/s

    # 1. Giren exergy (elektrik)
    Ex_in = input_data.power_kW

    # 2. Çıkan exergy (basınçlı hava)
    # İdeal gaz için: Ex_air = ṁ × R × T₀ × ln(P₂/P₁)
    pressure_ratio = P_out_kPa / dead_state.P0
    Ex_out = m_dot * R_AIR * dead_state.T0 * math.log(pressure_ratio)

    # 3. Exergy yıkımı
    Ex_destroyed = Ex_in - Ex_out

    # 4. Exergy verimi
    eta_ex = (Ex_out / Ex_in) * 100 if Ex_in > 0 else 0

    # 5. Yıllık kayıp
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.electricity_price_eur_kwh

    # 6. Isı geri kazanım potansiyeli
    # Atık ısının exergy değeri
    heat_recovery_potential = heat_exergy(Ex_destroyed, T_out_K, dead_state)

    # Termal tasarruf (doğalgaz alternatifi varsayımıyla)
    gas_price_eur_kwh = 0.06  # Yaklaşık doğalgaz fiyatı
    recoverable_thermal = Ex_destroyed * 0.70 * 0.85  # %70 ısıya, %85 HRU verimi
    heat_recovery_savings = recoverable_thermal * input_data.operating_hours * 0.70 * gas_price_eur_kwh

    # 7. Spesifik güç
    specific_power = input_data.power_kW / input_data.flow_rate_m3_min

    # 8. Benchmark karşılaştırma
    benchmark = _get_benchmark_comparison(eta_ex, input_data.compressor_type)

    return CompressorResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        recoverable_heat_kW=heat_recovery_potential,
        mass_flow_kg_s=m_dot,
        specific_power_kW_m3min=specific_power,
        heat_recovery_potential_kW=recoverable_thermal,
        heat_recovery_savings_eur_year=heat_recovery_savings,
        benchmark_comparison=benchmark
    )


def _get_benchmark_comparison(eta_ex: float, compressor_type: str) -> str:
    """
    Exergy verimine göre benchmark karşılaştırması yapar.
    """
    # Tip bazlı benchmark aralıkları
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


def get_compressor_recommendations(result: CompressorResult, input_data: CompressorInput) -> list:
    """
    Analiz sonuçlarına göre iyileştirme önerileri üretir.

    Returns:
        List of recommendation dictionaries
    """
    recommendations = []

    # 1. Isı geri kazanımı değerlendirmesi
    if input_data.power_kW >= 15 and result.heat_recovery_savings_eur_year > 1000:
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
        recommendations.append({
            'type': 'maintenance',
            'title': 'Bakım ve Kontrol',
            'description': 'Exergy verimi düşük. Filtre, yağ, conta kontrolü önerilir.',
            'investment_eur': 500,
            'savings_eur_year': result.annual_loss_EUR * 0.10,  # %10 iyileşme varsayımı
            'payback_years': 500 / (result.annual_loss_EUR * 0.10) if result.annual_loss_EUR > 0 else float('inf'),
            'priority': 'high'
        })

    # 3. Spesifik güç yüksekse
    if result.specific_power_kW_m3min > 7.0:
        recommendations.append({
            'type': 'pressure_optimization',
            'title': 'Basınç Optimizasyonu',
            'description': 'Spesifik güç yüksek. Sistem basıncını düşürme imkanı araştırılmalı.',
            'investment_eur': 0,
            'savings_eur_year': result.annual_loss_EUR * 0.07,  # Her 1 bar = %7 tasarruf
            'payback_years': 0,
            'priority': 'high'
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
