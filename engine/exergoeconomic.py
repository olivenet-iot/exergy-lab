"""
ExergyLab - Exergoeconomic Analysis Module

SPECO yontemiyle exergoekonomik analiz.
f-faktor, r-faktor, yikim maliyet akisi hesaplamalari.

Referanslar:
  - Bejan, Tsatsaronis & Moran (1996) Thermal Design and Optimization
  - Lazzaretto & Tsatsaronis (2006) SPECO methodology
"""

from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class ExergoeconomicInput:
    """Exergoekonomik analiz icin opsiyonel ekonomik parametreler."""
    equipment_cost_eur: Optional[float] = None  # PEC [EUR] (None = otomatik tahmin)
    installation_factor: float = 1.65            # TCI/PEC orani
    interest_rate: float = 0.10                  # Yillik faiz orani
    equipment_life_years: int = 20               # Ekipman omru [yil]
    maintenance_factor: float = 0.02             # O&M / TCI (phi_OM)
    annual_operating_hours: float = 6000         # tau [h/yil]


@dataclass
class ExergoeconomicResult:
    """Exergoekonomik analiz sonuclari."""
    Z_dot_eur_h: float = 0.0           # Levelized yatirim maliyet akisi [EUR/h]
    C_dot_destruction_eur_h: float = 0.0  # Yikim maliyet akisi [EUR/h]
    c_fuel_eur_kWh: float = 0.0        # Yakit birim maliyeti [EUR/kWh]
    c_product_eur_kWh: float = 0.0     # Urun birim maliyeti [EUR/kWh]
    f_factor: float = 0.0              # Exergoekonomik faktor [-]
    r_factor: float = 0.0             # Goreli maliyet farki [-]
    total_cost_rate_eur_h: float = 0.0 # Z_dot + C_dot_D [EUR/h]


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def compute_crf(interest_rate: float, life_years: int) -> float:
    """
    Capital Recovery Factor (CRF).

    CRF = i * (1+i)^n / ((1+i)^n - 1)

    Args:
        interest_rate: Yillik faiz orani (ornegin 0.10)
        life_years: Ekipman omru [yil]

    Returns:
        CRF degeri [-]
    """
    if interest_rate <= 0:
        return 1.0 / life_years if life_years > 0 else 1.0
    i = interest_rate
    n = life_years
    factor = (1 + i) ** n
    return i * factor / (factor - 1)


def compute_z_dot(total_investment_eur: float, crf: float,
                  maintenance_factor: float,
                  annual_hours: float) -> float:
    """
    Levelized yatirim maliyet akisi Z_dot [EUR/h].

    Z_dot = (Z_total * CRF + Z_total * phi_OM) / tau

    Args:
        total_investment_eur: Toplam yatirim maliyeti TCI [EUR]
        crf: Capital Recovery Factor
        maintenance_factor: O&M / TCI orani (phi_OM)
        annual_hours: Yillik calisma saati (tau)

    Returns:
        Z_dot [EUR/h]
    """
    if annual_hours <= 0:
        return 0.0
    return total_investment_eur * (crf + maintenance_factor) / annual_hours


# PEC = a * W^b  (basitlestirilmis guc yasasi korelasyonlari, endeks yili 2024)
COST_CORRELATIONS = {
    "compressor": {"a": 3500, "b": 0.70, "subtypes": {
        "screw": {"a": 3500, "b": 0.70}, "screw_oilfree": {"a": 4200, "b": 0.72},
        "piston": {"a": 2800, "b": 0.68}, "scroll": {"a": 3000, "b": 0.69},
        "centrifugal": {"a": 5000, "b": 0.75}, "roots": {"a": 2500, "b": 0.65},
    }},
    "boiler": {"a": 2000, "b": 0.75, "subtypes": {
        "steam_firetube": {"a": 2000, "b": 0.75}, "steam_watertube": {"a": 2500, "b": 0.78},
        "hotwater": {"a": 1500, "b": 0.72}, "condensing": {"a": 2800, "b": 0.76},
        "waste_heat": {"a": 1800, "b": 0.70}, "electric": {"a": 1200, "b": 0.65},
        "biomass": {"a": 3000, "b": 0.80},
    }},
    "chiller": {"a": 1200, "b": 0.80, "subtypes": {
        "screw": {"a": 1200, "b": 0.80}, "centrifugal": {"a": 1800, "b": 0.82},
        "scroll": {"a": 1000, "b": 0.75}, "reciprocating": {"a": 1100, "b": 0.78},
        "absorption": {"a": 2200, "b": 0.85}, "air_cooled": {"a": 1400, "b": 0.79},
        "water_cooled": {"a": 1300, "b": 0.80},
    }},
    "pump": {"a": 1000, "b": 0.65, "subtypes": {
        "centrifugal": {"a": 1000, "b": 0.65}, "positive_displacement": {"a": 1500, "b": 0.70},
        "submersible": {"a": 1200, "b": 0.68}, "vertical_turbine": {"a": 1400, "b": 0.69},
        "booster": {"a": 900, "b": 0.63}, "vacuum": {"a": 1800, "b": 0.72},
    }},
    "heat_exchanger": {"a": 1500, "b": 0.75, "subtypes": {
        "shell_tube": {"a": 1500, "b": 0.75}, "plate": {"a": 1200, "b": 0.72},
        "air_cooled": {"a": 2000, "b": 0.78}, "double_pipe": {"a": 1000, "b": 0.68},
        "spiral": {"a": 1800, "b": 0.76}, "economizer": {"a": 1400, "b": 0.73},
        "recuperator": {"a": 1600, "b": 0.74},
    }},
    "steam_turbine": {"a": 4500, "b": 0.70, "subtypes": {
        "back_pressure": {"a": 4000, "b": 0.70}, "condensing": {"a": 5000, "b": 0.72},
        "extraction": {"a": 5500, "b": 0.73}, "orc": {"a": 6000, "b": 0.75},
        "micro_turbine": {"a": 3000, "b": 0.65},
    }},
    "dryer": {"a": 2500, "b": 0.78, "subtypes": {
        "convective": {"a": 2500, "b": 0.78}, "rotary": {"a": 3000, "b": 0.80},
        "fluidized_bed": {"a": 3500, "b": 0.82}, "spray": {"a": 4000, "b": 0.83},
        "belt": {"a": 2800, "b": 0.77}, "heat_pump": {"a": 4500, "b": 0.80},
        "infrared": {"a": 2200, "b": 0.72}, "drum": {"a": 2000, "b": 0.75},
    }},
}


def estimate_equipment_cost(equipment_type: str, capacity_param_kW: float,
                            subtype: Optional[str] = None) -> float:
    """
    Guc-yasasi korelasyonlariyla ekipman maliyeti (PEC) tahmini.

    Basitlestirilmis korelasyonlar - endeks yili 2024.

    Args:
        equipment_type: Ekipman tipi (compressor, boiler, chiller, pump, heat_exchanger, steam_turbine, dryer)
        capacity_param_kW: Kapasite parametresi [kW]
        subtype: Ekipman alt tipi (opsiyonel, ornegin 'screw', 'plate')

    Returns:
        Tahmini PEC [EUR]
    """
    W = max(capacity_param_kW, 1.0)  # minimum 1 kW

    corr = COST_CORRELATIONS.get(equipment_type)
    if corr is None:
        a, b = 2000.0, 0.70
    elif subtype and subtype in corr.get("subtypes", {}):
        sub = corr["subtypes"][subtype]
        a, b = sub["a"], sub["b"]
    else:
        a, b = corr["a"], corr["b"]

    return a * (W ** b)


def analyze_exergoeconomic(
    exergy_destroyed_kW: float,
    exergy_efficiency_pct: float,
    exergy_in_kW: float,
    exergy_out_kW: float,
    c_fuel_eur_kWh: float,
    equipment_type: str,
    capacity_param_kW: float,
    equipment_cost_eur: Optional[float] = None,
    installation_factor: float = 1.65,
    interest_rate: float = 0.10,
    equipment_life_years: int = 20,
    maintenance_factor: float = 0.02,
    annual_operating_hours: float = 6000,
    subtype: Optional[str] = None,
) -> ExergoeconomicResult:
    """
    Exergoekonomik analiz yapar (SPECO yontemi).

    Hesaplamalar:
      C_dot_D = c_F * E_dot_D
      c_P = c_F / epsilon + Z_dot / E_P   (epsilon = eta_ex / 100)
      f = Z_dot / (Z_dot + C_dot_D)
      r = (c_P - c_F) / c_F

    Args:
        exergy_destroyed_kW: Exergy yikim hizi [kW]
        exergy_efficiency_pct: Exergy verimi [%]
        exergy_in_kW: Exergy girisi [kW]
        exergy_out_kW: Exergy cikisi [kW]
        c_fuel_eur_kWh: Yakit/enerji birim maliyeti [EUR/kWh]
        equipment_type: Ekipman tipi
        capacity_param_kW: Kapasite parametresi [kW]
        equipment_cost_eur: Ekipman maliyeti PEC [EUR] (None = otomatik tahmin)
        installation_factor: TCI/PEC orani
        interest_rate: Yillik faiz orani
        equipment_life_years: Ekipman omru [yil]
        maintenance_factor: O&M / TCI orani
        annual_operating_hours: Yillik calisma saati [h]

    Returns:
        ExergoeconomicResult
    """
    # PEC and TCI
    if equipment_cost_eur is not None and equipment_cost_eur > 0:
        pec = equipment_cost_eur
    else:
        pec = estimate_equipment_cost(equipment_type, capacity_param_kW, subtype=subtype)

    tci = pec * installation_factor

    # CRF and Z_dot
    crf = compute_crf(interest_rate, equipment_life_years)
    z_dot = compute_z_dot(tci, crf, maintenance_factor, annual_operating_hours)

    # Exergy destruction cost rate
    c_fuel = max(c_fuel_eur_kWh, 0.0)
    c_dot_d = c_fuel * exergy_destroyed_kW

    # Product cost rate (SPECO)
    epsilon = exergy_efficiency_pct / 100.0 if exergy_efficiency_pct > 0 else 0.0
    E_P = exergy_out_kW

    if epsilon > 0 and E_P > 0:
        c_product = c_fuel / epsilon + z_dot / E_P
    elif E_P > 0:
        c_product = z_dot / E_P
    else:
        c_product = 0.0

    # f-factor: exergoeconomic factor
    denominator = z_dot + c_dot_d
    f_factor = z_dot / denominator if denominator > 0 else 0.0

    # r-factor: relative cost difference
    r_factor = (c_product - c_fuel) / c_fuel if c_fuel > 0 else 0.0

    # Total cost rate
    total_cost_rate = z_dot + c_dot_d

    return ExergoeconomicResult(
        Z_dot_eur_h=z_dot,
        C_dot_destruction_eur_h=c_dot_d,
        c_fuel_eur_kWh=c_fuel,
        c_product_eur_kWh=c_product,
        f_factor=f_factor,
        r_factor=r_factor,
        total_cost_rate_eur_h=total_cost_rate,
    )


def _apply_exergoeconomic(result, equipment_type: str,
                           c_fuel_eur_kWh: float,
                           capacity_param_kW: float,
                           equipment_cost_eur: Optional[float] = None,
                           annual_operating_hours: float = 6000,
                           subtype: Optional[str] = None) -> None:
    """
    Exergoekonomik sonuclari mevcut ExergyResult nesnesine yazar.

    Flat alanlari dogrudan set eder (avoidable split paterni).

    Args:
        result: ExergyResult (veya alt sinif) nesnesi
        equipment_type: Ekipman tipi
        c_fuel_eur_kWh: Yakit/enerji birim maliyeti [EUR/kWh]
        capacity_param_kW: Kapasite parametresi [kW]
        equipment_cost_eur: Ekipman maliyeti PEC [EUR] (None = otomatik tahmin)
        annual_operating_hours: Yillik calisma saati [h]
        subtype: Ekipman alt tipi (opsiyonel)
    """
    eco = analyze_exergoeconomic(
        exergy_destroyed_kW=result.exergy_destroyed_kW,
        exergy_efficiency_pct=result.exergy_efficiency_pct,
        exergy_in_kW=result.exergy_in_kW,
        exergy_out_kW=result.exergy_out_kW,
        c_fuel_eur_kWh=c_fuel_eur_kWh,
        equipment_type=equipment_type,
        capacity_param_kW=capacity_param_kW,
        equipment_cost_eur=equipment_cost_eur,
        annual_operating_hours=annual_operating_hours,
        subtype=subtype,
    )

    result.exergoeconomic_Z_dot_eur_h = eco.Z_dot_eur_h
    result.exergoeconomic_C_dot_destruction_eur_h = eco.C_dot_destruction_eur_h
    result.exergoeconomic_f_factor = eco.f_factor
    result.exergoeconomic_r_factor = eco.r_factor
    result.exergoeconomic_c_product_eur_kWh = eco.c_product_eur_kWh
    result.exergoeconomic_total_cost_rate_eur_h = eco.total_cost_rate_eur_h
