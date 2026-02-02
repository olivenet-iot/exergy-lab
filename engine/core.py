"""
ExergyLab - Core Thermodynamic Functions

Temel exergy hesaplama fonksiyonları.
Dead state ve yardımcı fonksiyonlar.
"""

from dataclasses import dataclass
from typing import Optional
import math

# Sabitler
R_AIR = 0.287  # kJ/kg·K - Kuru hava gaz sabiti
R_UNIVERSAL = 8.314  # J/mol·K
CP_AIR = 1.005  # kJ/kg·K - Havanın sabit basınçta özgül ısısı

@dataclass
class DeadState:
    """Referans çevre koşulları (dead state)"""
    T0: float = 298.15  # K (25°C)
    P0: float = 101.325  # kPa (1 atm)

    def T0_celsius(self) -> float:
        return self.T0 - 273.15

    @classmethod
    def from_celsius(cls, T_celsius: float, P_kPa: float = 101.325):
        return cls(T0=T_celsius + 273.15, P0=P_kPa)


@dataclass
class ExergyResult:
    """Exergy analizi sonuç yapısı"""
    exergy_in_kW: float
    exergy_out_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_pct: float
    annual_loss_kWh: Optional[float] = None
    annual_loss_EUR: Optional[float] = None
    recoverable_heat_kW: Optional[float] = None

    # AV/UN exergy destruction split (Tsatsaronis & Morosuk 2008)
    exergy_destroyed_avoidable_kW: float = 0.0
    exergy_destroyed_unavoidable_kW: float = 0.0
    avoidable_ratio_pct: float = 0.0

    def to_dict(self) -> dict:
        return {
            'exergy_in_kW': round(self.exergy_in_kW, 2),
            'exergy_out_kW': round(self.exergy_out_kW, 2),
            'exergy_destroyed_kW': round(self.exergy_destroyed_kW, 2),
            'exergy_efficiency_pct': round(self.exergy_efficiency_pct, 1),
            'annual_loss_kWh': round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            'annual_loss_EUR': round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            'recoverable_heat_kW': round(self.recoverable_heat_kW, 2) if self.recoverable_heat_kW else None,
            'exergy_destroyed_avoidable_kW': round(self.exergy_destroyed_avoidable_kW, 2),
            'exergy_destroyed_unavoidable_kW': round(self.exergy_destroyed_unavoidable_kW, 2),
            'avoidable_ratio_pct': round(self.avoidable_ratio_pct, 1),
        }


def heat_exergy(Q_kW: float, T_K: float, dead_state: DeadState = None) -> float:
    """
    Isı transferinin exergy'sini hesaplar.

    Ex_Q = Q × (1 - T₀/T)

    Args:
        Q_kW: Isı transfer hızı [kW]
        T_K: Isı transferi sıcaklığı [K]
        dead_state: Dead state koşulları

    Returns:
        Exergy [kW]
    """
    if dead_state is None:
        dead_state = DeadState()

    if T_K <= dead_state.T0:
        # Soğutma durumu - Carnot çarpanı negatif
        return Q_kW * (dead_state.T0 / T_K - 1)
    else:
        # Isıtma durumu
        return Q_kW * (1 - dead_state.T0 / T_K)


def carnot_factor(T_hot_K: float, T_cold_K: float) -> float:
    """
    Carnot faktörü (maksimum teorik verim)

    η_carnot = 1 - T_cold / T_hot
    """
    return 1 - T_cold_K / T_hot_K


def celsius_to_kelvin(T_C: float) -> float:
    """Celsius'u Kelvin'e çevirir"""
    return T_C + 273.15


def kelvin_to_celsius(T_K: float) -> float:
    """Kelvin'i Celsius'a çevirir"""
    return T_K - 273.15


def bar_to_kpa(P_bar: float) -> float:
    """Bar'ı kPa'ya çevirir"""
    return P_bar * 100


def kpa_to_bar(P_kPa: float) -> float:
    """kPa'yı bar'a çevirir"""
    return P_kPa / 100


def m3_min_to_m3_s(V_m3_min: float) -> float:
    """m³/min'i m³/s'ye çevirir"""
    return V_m3_min / 60


def air_density(T_K: float, P_kPa: float) -> float:
    """
    İdeal gaz yasasıyla hava yoğunluğu

    ρ = P / (R × T)
    """
    return P_kPa / (R_AIR * T_K)


def compute_avoidable_split(actual_destroyed: float, unavoidable_destroyed: float) -> tuple:
    """
    Avoidable/Unavoidable exergy destruction split.

    Tsatsaronis & Morosuk (2008):
      AV = actual - UN
      ratio = AV / actual * 100

    Edge cases:
      - actual <= 0: all zeros
      - unavoidable > actual: UN = actual, AV = 0
      - unavoidable < 0: UN = 0, AV = actual

    Args:
        actual_destroyed: Actual exergy destruction [kW]
        unavoidable_destroyed: Unavoidable exergy destruction [kW]

    Returns:
        (avoidable_kW, unavoidable_kW, ratio_pct)
    """
    if actual_destroyed <= 0:
        return (0.0, 0.0, 0.0)

    un = max(0.0, min(unavoidable_destroyed, actual_destroyed))
    av = actual_destroyed - un
    ratio = (av / actual_destroyed) * 100.0 if actual_destroyed > 0 else 0.0

    return (av, un, ratio)
