"""
ExergyLab - Boiler Exergy Analysis

Kazan exergy hesaplamalari.
Ates borulu, su borulu, sicak su, yogusmali ve diger kazan tipleri icin.
CoolProp ile buhar ozellikleri hesaplanir.
"""

from dataclasses import dataclass
from typing import Optional
import math

import copy

from .core import DeadState, ExergyResult, compute_avoidable_split, celsius_to_kelvin
from .exergoeconomic import _apply_exergoeconomic

try:
    from CoolProp.CoolProp import PropsSI
    HAS_COOLPROP = True
except ImportError:
    HAS_COOLPROP = False


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Fuel exergy factors (phi = Ex_fuel / LHV)
FUEL_EXERGY_FACTORS = {
    'natural_gas': 1.04,
    'fuel_oil': 1.06,
    'coal': 1.09,
    'biomass': 1.13,
    'lpg': 1.05,
    'diesel': 1.07,
}

# Default LHV values [kJ/kg]
FUEL_LHV = {
    'natural_gas': 47100.0,
    'fuel_oil': 41200.0,
    'coal': 25000.0,
    'biomass': 17000.0,
    'lpg': 46100.0,
    'diesel': 43000.0,
}

# Best-achievable parameters per boiler type (Tsatsaronis & Morosuk 2008)
UNAVOIDABLE_REF_BOILER = {
    'steam_firetube':  {'excess_air_pct': 5.0, 'flue_gas_temp_C': 120.0, 'blowdown_rate_pct': 1.0},
    'steam_watertube': {'excess_air_pct': 5.0, 'flue_gas_temp_C': 120.0, 'blowdown_rate_pct': 1.0},
    'hotwater':        {'excess_air_pct': 5.0, 'flue_gas_temp_C': 100.0},
    'condensing':      {'excess_air_pct': 3.0, 'flue_gas_temp_C': 55.0},
    'waste_heat':      {'flue_gas_temp_C': 100.0},
    'electric':        {},
    'biomass':         {'excess_air_pct': 15.0, 'flue_gas_temp_C': 150.0, 'blowdown_rate_pct': 1.0},
}

# Reference state for water (25C, 1 atm, liquid)
H_0_WATER = 104920.0   # J/kg (~104.9 kJ/kg)
S_0_WATER = 367.0       # J/(kg*K) (~0.367 kJ/(kg*K))

# Specific heat of water for hot water calculations
CP_WATER = 4.18  # kJ/(kg*K)


# ---------------------------------------------------------------------------
# Input dataclass
# ---------------------------------------------------------------------------

@dataclass
class BoilerInput:
    """Kazan analizi icin giris verileri"""

    # Zorunlu
    fuel_flow_kg_h: float           # Yakit debisi [kg/h]
    steam_flow_kg_h: float          # Buhar/su debisi [kg/h]
    steam_pressure_bar: float       # Buhar basinci [bar]

    # Opsiyonel
    steam_temp_C: Optional[float] = None   # Buhar sicakligi [C] (None = doymus)
    feedwater_temp_C: float = 80.0         # Besleme suyu sicakligi [C]
    flue_gas_temp_C: float = 180.0         # Baca gazi sicakligi [C]

    # Yakit
    fuel_type: str = "natural_gas"
    fuel_lhv_kj_kg: Optional[float] = None  # None = fuel_type'dan otomatik

    # Operasyonel
    blowdown_rate_pct: float = 3.0    # Blowdown orani [%]
    excess_air_pct: float = 15.0      # Fazla hava [%]
    ambient_temp_C: Optional[float] = None

    # Ekonomik
    operating_hours: float = 6000
    fuel_price_eur_kg: float = 0.50
    equipment_cost_eur: Optional[float] = None  # Ekipman maliyeti PEC [€]

    # Ekipman
    boiler_type: str = "steam_firetube"

    def __post_init__(self):
        if self.ambient_temp_C is None:
            self.ambient_temp_C = 25.0
        if self.fuel_lhv_kj_kg is None:
            self.fuel_lhv_kj_kg = FUEL_LHV.get(self.fuel_type, 47100.0)


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class BoilerResult(ExergyResult):
    """Kazan analizi sonuclari"""

    thermal_efficiency_pct: Optional[float] = None
    combustion_loss_kW: Optional[float] = None
    flue_gas_loss_kW: Optional[float] = None
    radiation_loss_kW: Optional[float] = None
    blowdown_loss_kW: Optional[float] = None
    benchmark_comparison: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'thermal_efficiency_pct': round(self.thermal_efficiency_pct, 1) if self.thermal_efficiency_pct else None,
            'combustion_loss_kW': round(self.combustion_loss_kW, 2) if self.combustion_loss_kW else None,
            'flue_gas_loss_kW': round(self.flue_gas_loss_kW, 2) if self.flue_gas_loss_kW else None,
            'radiation_loss_kW': round(self.radiation_loss_kW, 2) if self.radiation_loss_kW else None,
            'blowdown_loss_kW': round(self.blowdown_loss_kW, 2) if self.blowdown_loss_kW else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base

    def to_api_dict(self, boiler_type: str = "steam_firetube") -> dict:
        """API yanit formatina donusturur."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "thermal_efficiency_pct": round(self.thermal_efficiency_pct, 1) if self.thermal_efficiency_pct else None,
            "combustion_loss_kW": round(self.combustion_loss_kW, 2) if self.combustion_loss_kW else None,
            "flue_gas_loss_kW": round(self.flue_gas_loss_kW, 2) if self.flue_gas_loss_kW else None,
            "radiation_loss_kW": round(self.radiation_loss_kW, 2) if self.radiation_loss_kW else None,
            "blowdown_loss_kW": round(self.blowdown_loss_kW, 2) if self.blowdown_loss_kW else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, boiler_type),
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
# Steam property helpers
# ---------------------------------------------------------------------------

def _get_steam_properties(pressure_bar: float, temp_C: Optional[float] = None) -> tuple:
    """
    CoolProp ile buhar ozelliklerini hesaplar.

    Returns:
        (h [J/kg], s [J/(kg*K)])
    """
    P_Pa = pressure_bar * 1e5

    if HAS_COOLPROP:
        if temp_C is None:
            # Saturated steam (quality = 1)
            h = PropsSI('H', 'P', P_Pa, 'Q', 1, 'Water')
            s = PropsSI('S', 'P', P_Pa, 'Q', 1, 'Water')
        else:
            T_K = celsius_to_kelvin(temp_C)
            # Check if superheated
            T_sat = PropsSI('T', 'P', P_Pa, 'Q', 1, 'Water')
            if T_K > T_sat:
                h = PropsSI('H', 'P', P_Pa, 'T', T_K, 'Water')
                s = PropsSI('S', 'P', P_Pa, 'T', T_K, 'Water')
            else:
                # At or below saturation - use saturated steam
                h = PropsSI('H', 'P', P_Pa, 'Q', 1, 'Water')
                s = PropsSI('S', 'P', P_Pa, 'Q', 1, 'Water')
    else:
        # Fallback: approximate steam properties without CoolProp
        # Using simplified correlations for industrial steam (1-40 bar)
        h, s = _approximate_steam_properties(pressure_bar, temp_C)

    return h, s


def _approximate_steam_properties(pressure_bar: float, temp_C: Optional[float] = None) -> tuple:
    """
    Approximate steam properties without CoolProp.
    Uses simplified correlations for industrial steam range.
    """
    # Approximate saturation temperature [C]
    T_sat = 100.0 + 28.0 * math.log(pressure_bar) if pressure_bar > 0 else 100.0

    # Approximate saturated steam properties
    # h_g ~ 2675 + 2.0 * P_bar (rough fit for 1-40 bar range)
    h_sat = (2675000.0 + 2000.0 * pressure_bar)  # J/kg
    # s_g ~ 7.36 - 0.58 * ln(P_bar) (rough fit)
    s_sat = (7360.0 - 580.0 * math.log(max(pressure_bar, 0.1)))  # J/(kg*K)

    if temp_C is None or temp_C <= T_sat:
        return h_sat, s_sat

    # Superheated: add Cp_steam * dT
    dT = temp_C - T_sat
    Cp_steam = 2100.0  # J/(kg*K) approximate
    h = h_sat + Cp_steam * dT
    s = s_sat + Cp_steam * math.log((celsius_to_kelvin(temp_C)) / celsius_to_kelvin(T_sat))
    return h, s


def _get_feedwater_properties(temp_C: float, pressure_bar: float) -> tuple:
    """Feedwater (compressed liquid) properties."""
    P_Pa = pressure_bar * 1e5
    T_K = celsius_to_kelvin(temp_C)

    if HAS_COOLPROP:
        try:
            h = PropsSI('H', 'P', P_Pa, 'T', T_K, 'Water')
            s = PropsSI('S', 'P', P_Pa, 'T', T_K, 'Water')
        except Exception:
            # Fallback to simplified
            h = CP_WATER * 1000.0 * temp_C  # J/kg
            s = CP_WATER * 1000.0 * math.log(T_K / 273.15)  # J/(kg*K)
    else:
        h = CP_WATER * 1000.0 * temp_C  # J/kg
        s = CP_WATER * 1000.0 * math.log(T_K / 273.15)  # J/(kg*K)

    return h, s


# ---------------------------------------------------------------------------
# Analysis function
# ---------------------------------------------------------------------------

def analyze_boiler(input_data: BoilerInput, dead_state: DeadState = None, _calc_avoidable: bool = True) -> BoilerResult:
    """
    Kazan exergy analizi yapar.

    Hesaplamalar:
    - Yakit exergy: Ex_fuel = m_fuel * LHV * phi
    - Buhar exergy: ex_steam = (h - h_0) - T_0 * (s - s_0)
    - Kayip dagilimi: yanma, baca gazi, radyasyon, blowdown

    Args:
        input_data: Kazan giris verileri
        dead_state: Dead state kosullari (opsiyonel)

    Returns:
        BoilerResult: Analiz sonuclari
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T0 = dead_state.T0  # K

    # Mass flow rates [kg/s]
    m_fuel = input_data.fuel_flow_kg_h / 3600.0
    m_steam = input_data.steam_flow_kg_h / 3600.0

    # --- Fuel exergy ---
    phi = FUEL_EXERGY_FACTORS.get(input_data.fuel_type, 1.04)
    Q_fuel = m_fuel * input_data.fuel_lhv_kj_kg  # kW (kJ/s)
    Ex_fuel = Q_fuel * phi  # kW

    Ex_in = Ex_fuel

    # --- Steam/water output exergy ---
    is_hotwater = input_data.boiler_type in ('hotwater', 'condensing')

    if is_hotwater:
        # Hot water boiler: incompressible liquid model
        # ex = Cp * [(T - T_0) - T_0 * ln(T/T_0)]
        T_water_C = input_data.steam_temp_C if input_data.steam_temp_C else 90.0
        T_water_K = celsius_to_kelvin(T_water_C)
        T_fw_K = celsius_to_kelvin(input_data.feedwater_temp_C)

        # Output exergy
        ex_out_specific = CP_WATER * ((T_water_K - T0) - T0 * math.log(T_water_K / T0))  # kJ/kg
        ex_fw_specific = CP_WATER * ((T_fw_K - T0) - T0 * math.log(T_fw_K / T0))  # kJ/kg

        Ex_out = m_steam * (ex_out_specific - ex_fw_specific)

        # Thermal efficiency (energy based)
        Q_useful = m_steam * CP_WATER * (T_water_K - T_fw_K)  # kW
        thermal_eff = (Q_useful / Q_fuel) * 100 if Q_fuel > 0 else 0.0
    else:
        # Steam boiler: use CoolProp or approximations
        h_steam, s_steam = _get_steam_properties(input_data.steam_pressure_bar, input_data.steam_temp_C)
        h_fw, s_fw = _get_feedwater_properties(input_data.feedwater_temp_C, input_data.steam_pressure_bar)

        # Specific exergy of steam (relative to dead state)
        ex_steam = (h_steam - H_0_WATER) - T0 * (s_steam - S_0_WATER)  # J/kg
        ex_fw = (h_fw - H_0_WATER) - T0 * (s_fw - S_0_WATER)  # J/kg

        # Net exergy output [kW]
        Ex_out = m_steam * (ex_steam - ex_fw) / 1000.0  # J/kg -> kJ/kg -> kW

        # Thermal efficiency
        Q_useful = m_steam * (h_steam - h_fw) / 1000.0  # kW
        thermal_eff = (Q_useful / Q_fuel) * 100 if Q_fuel > 0 else 0.0

    # Ensure Ex_out is positive and <= Ex_in
    Ex_out = max(0.0, Ex_out)
    if Ex_out > Ex_in:
        Ex_out = Ex_in * 0.45  # Fallback: typical boiler exergy efficiency ~30-45%

    # --- Loss breakdown ---

    # 1. Combustion irreversibility (~25-30% of fuel exergy)
    combustion_loss = Ex_fuel * 0.27  # typical for natural gas

    # 2. Flue gas exergy loss
    T_flue_K = celsius_to_kelvin(input_data.flue_gas_temp_C)
    # Flue gas mass flow ~ m_fuel * (1 + air_fuel_ratio)
    # For natural gas: stoichiometric air ~17.2 kg/kg fuel
    afr_stoich = {'natural_gas': 17.2, 'fuel_oil': 14.0, 'coal': 11.5, 'biomass': 6.5, 'lpg': 15.6, 'diesel': 14.5}
    afr = afr_stoich.get(input_data.fuel_type, 17.2) * (1 + input_data.excess_air_pct / 100.0)
    m_flue = m_fuel * (1 + afr)
    Cp_flue = 1.1  # kJ/(kg*K) average for flue gas

    # Flue gas exergy: Ex_flue = m_flue * Cp * [(T_flue - T0) - T0 * ln(T_flue/T0)]
    if T_flue_K > T0:
        ex_flue_specific = Cp_flue * ((T_flue_K - T0) - T0 * math.log(T_flue_K / T0))
        flue_gas_loss = m_flue * ex_flue_specific
    else:
        flue_gas_loss = 0.0

    # 3. Radiation loss (~1-2% of fuel input)
    radiation_loss = Q_fuel * 0.015

    # 4. Blowdown loss
    blowdown_fraction = input_data.blowdown_rate_pct / 100.0
    m_blowdown = m_steam * blowdown_fraction
    # Blowdown is saturated liquid at steam pressure
    if HAS_COOLPROP:
        try:
            P_Pa = input_data.steam_pressure_bar * 1e5
            h_bd = PropsSI('H', 'P', P_Pa, 'Q', 0, 'Water')
            s_bd = PropsSI('S', 'P', P_Pa, 'Q', 0, 'Water')
            ex_bd = (h_bd - H_0_WATER) - T0 * (s_bd - S_0_WATER)  # J/kg
            blowdown_loss = m_blowdown * ex_bd / 1000.0  # kW
        except Exception:
            blowdown_loss = m_blowdown * 50.0  # ~50 kJ/kg approximate
    else:
        blowdown_loss = m_blowdown * 50.0

    blowdown_loss = max(0.0, blowdown_loss)

    # --- Totals ---
    Ex_destroyed = Ex_in - Ex_out
    eta_ex = (Ex_out / Ex_in) * 100 if Ex_in > 0 else 0.0

    # Scale loss breakdown to match total destruction
    total_losses = combustion_loss + flue_gas_loss + radiation_loss + blowdown_loss
    if total_losses > 0 and abs(total_losses - Ex_destroyed) > 0.1:
        scale = Ex_destroyed / total_losses
        combustion_loss *= scale
        flue_gas_loss *= scale
        radiation_loss *= scale
        blowdown_loss *= scale

    # Annual losses (fuel cost basis)
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    fuel_cost_per_kwh = input_data.fuel_price_eur_kg / (input_data.fuel_lhv_kj_kg / 3600.0) if input_data.fuel_lhv_kj_kg > 0 else 0.05
    annual_loss_EUR = annual_loss_kWh * fuel_cost_per_kwh

    benchmark = _get_benchmark_comparison(eta_ex, input_data.boiler_type)

    result = BoilerResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        thermal_efficiency_pct=thermal_eff,
        combustion_loss_kW=combustion_loss,
        flue_gas_loss_kW=flue_gas_loss,
        radiation_loss_kW=radiation_loss,
        blowdown_loss_kW=blowdown_loss,
        benchmark_comparison=benchmark,
    )

    # AV/UN split
    if _calc_avoidable and Ex_destroyed > 0:
        ref_params = UNAVOIDABLE_REF_BOILER.get(input_data.boiler_type, {})
        if ref_params:
            un_input = copy.deepcopy(input_data)
            for k, v in ref_params.items():
                setattr(un_input, k, v)
            un_result = analyze_boiler(un_input, dead_state=dead_state, _calc_avoidable=False)
            av, un, ratio = compute_avoidable_split(Ex_destroyed, un_result.exergy_destroyed_kW)
            result.exergy_destroyed_avoidable_kW = av
            result.exergy_destroyed_unavoidable_kW = un
            result.avoidable_ratio_pct = ratio

    # Exergoeconomic analysis
    _apply_exergoeconomic(
        result, equipment_type='boiler',
        c_fuel_eur_kWh=fuel_cost_per_kwh,
        capacity_param_kW=Q_fuel,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
    )

    return result


# ---------------------------------------------------------------------------
# Sankey data
# ---------------------------------------------------------------------------

def generate_boiler_sankey_data(result: BoilerResult, boiler_type: str = "steam_firetube") -> dict:
    """
    Kazan Sankey diyagrami icin node ve link verisi olusturur.

    Nodes: Yakit Exergy -> Kazan -> Buhar Exergy / Yanma Kaybi / Baca Gazi / Radyasyon / Blowdown
    """
    Ex_in = result.exergy_in_kW
    Ex_out = result.exergy_out_kW
    combustion = result.combustion_loss_kW or 0.0
    flue_gas = result.flue_gas_loss_kW or 0.0
    radiation = result.radiation_loss_kW or 0.0
    blowdown = result.blowdown_loss_kW or 0.0

    is_hotwater = boiler_type in ('hotwater', 'condensing')
    output_name = "Sicak Su Exergy" if is_hotwater else "Buhar Exergy"
    output_name_en = "Hot Water Exergy" if is_hotwater else "Steam Exergy"

    nodes = [
        {"id": 0, "name": "Yakit Exergy", "name_en": "Fuel Exergy"},
        {"id": 1, "name": "Kazan", "name_en": "Boiler"},
        {"id": 2, "name": output_name, "name_en": output_name_en},
        {"id": 3, "name": "Yanma Kaybi", "name_en": "Combustion Loss"},
        {"id": 4, "name": "Baca Gazi", "name_en": "Flue Gas Loss"},
        {"id": 5, "name": "Radyasyon", "name_en": "Radiation Loss"},
        {"id": 6, "name": "Blowdown", "name_en": "Blowdown Loss"},
    ]

    links = [
        {"source": 0, "target": 1, "value": round(Ex_in, 2), "label": "Yakit Girisi"},
        {"source": 1, "target": 2, "value": round(Ex_out, 2), "label": output_name},
        {"source": 1, "target": 3, "value": round(combustion, 2), "label": "Yanma Tersinmezligi"},
        {"source": 1, "target": 4, "value": round(flue_gas, 2), "label": "Baca Gazi Exergy"},
        {"source": 1, "target": 5, "value": round(radiation, 2), "label": "Radyasyon Kaybi"},
        {"source": 1, "target": 6, "value": round(blowdown, 2), "label": "Blowdown Kaybi"},
    ]

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(Ex_out, 2),
            "recoverable_heat_kW": round(flue_gas, 2),
            "irreversibility_kW": round(combustion + radiation + blowdown, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
            "exergy_destroyed_avoidable_kW": round(getattr(result, 'exergy_destroyed_avoidable_kW', 0.0) or 0.0, 2),
            "exergy_destroyed_unavoidable_kW": round(getattr(result, 'exergy_destroyed_unavoidable_kW', 0.0) or 0.0, 2),
            "avoidable_ratio_pct": round(getattr(result, 'avoidable_ratio_pct', 0.0) or 0.0, 1),
        },
    }


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_boiler_recommendations(result: BoilerResult, input_data: BoilerInput) -> list:
    """Kazan analiz sonuclarina gore iyilestirme onerileri."""
    recommendations = []
    fuel_cost_per_kwh = input_data.fuel_price_eur_kg / (input_data.fuel_lhv_kj_kg / 3600.0) if input_data.fuel_lhv_kj_kg > 0 else 0.05

    # Flue gas heat recovery (economizer)
    if result.flue_gas_loss_kW and result.flue_gas_loss_kW > 10 and input_data.flue_gas_temp_C > 150:
        savings = result.flue_gas_loss_kW * 0.50 * input_data.operating_hours * fuel_cost_per_kwh
        recommendations.append({
            'type': 'economizer',
            'title': 'Ekonomizer (Baca Gazi Isi Geri Kazanimi)',
            'description': f'Baca gazi sicakligi {input_data.flue_gas_temp_C}C. Ekonomizer ile kayip %50 azaltilabilir.',
            'investment_eur': 15000,
            'savings_eur_year': savings,
            'payback_years': 15000 / savings if savings > 0 else float('inf'),
            'priority': 'high' if savings > 5000 else 'medium',
        })

    # Excess air optimization
    if input_data.excess_air_pct > 20:
        savings = result.exergy_in_kW * 0.02 * input_data.operating_hours * fuel_cost_per_kwh
        recommendations.append({
            'type': 'combustion_control',
            'title': 'Yanma Kontrol Optimizasyonu',
            'description': f'Fazla hava %{input_data.excess_air_pct}. O2 trim kontrolu ile optimize edilebilir.',
            'investment_eur': 8000,
            'savings_eur_year': savings,
            'payback_years': 8000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # Blowdown heat recovery
    if input_data.blowdown_rate_pct > 2 and result.blowdown_loss_kW and result.blowdown_loss_kW > 5:
        savings = result.blowdown_loss_kW * 0.60 * input_data.operating_hours * fuel_cost_per_kwh
        recommendations.append({
            'type': 'blowdown_recovery',
            'title': 'Blowdown Isi Geri Kazanimi',
            'description': f'Blowdown orani %{input_data.blowdown_rate_pct}. Flas tanki ve isi degistirici ile kazanim.',
            'investment_eur': 5000,
            'savings_eur_year': savings,
            'payback_years': 5000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # Condensing boiler conversion
    if input_data.boiler_type not in ('condensing',) and input_data.flue_gas_temp_C > 120:
        savings = result.exergy_in_kW * 0.05 * input_data.operating_hours * fuel_cost_per_kwh
        recommendations.append({
            'type': 'condensing',
            'title': 'Yogusmali Kazan Degisimi',
            'description': 'Yogusmali kazan ile baca gazi nemi geri kazanilabilir.',
            'investment_eur': 30000,
            'savings_eur_year': savings,
            'payback_years': 30000 / savings if savings > 0 else float('inf'),
            'priority': 'low',
        })

    # Insulation
    if result.radiation_loss_kW and result.radiation_loss_kW > 5:
        savings = result.radiation_loss_kW * 0.50 * input_data.operating_hours * fuel_cost_per_kwh
        recommendations.append({
            'type': 'insulation',
            'title': 'Yalitim Iyilestirme',
            'description': 'Kazan ve boru yalitimi ile radyasyon kayiplari azaltilabilir.',
            'investment_eur': 3000,
            'savings_eur_year': savings,
            'payback_years': 3000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # Feedwater preheating
    if input_data.feedwater_temp_C < 60:
        savings = result.exergy_in_kW * 0.03 * input_data.operating_hours * fuel_cost_per_kwh
        recommendations.append({
            'type': 'feedwater_preheat',
            'title': 'Besleme Suyu On Isitma',
            'description': f'Besleme suyu {input_data.feedwater_temp_C}C. On isitma ile verim arttirilabilir.',
            'investment_eur': 5000,
            'savings_eur_year': savings,
            'payback_years': 5000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    return recommendations


# ---------------------------------------------------------------------------
# Boiler types helper
# ---------------------------------------------------------------------------

def get_boiler_types() -> list:
    """Desteklenen kazan tiplerini dondurur."""
    return [
        {
            "type": "steam_firetube",
            "name": "Ates Borulu Buhar Kazani",
            "description": "Ates borulu buhar kazani exergy analizi",
        },
        {
            "type": "steam_watertube",
            "name": "Su Borulu Buhar Kazani",
            "description": "Su borulu buhar kazani exergy analizi",
        },
        {
            "type": "hotwater",
            "name": "Sicak Su Kazani",
            "description": "Sicak su kazani exergy analizi",
        },
        {
            "type": "condensing",
            "name": "Yogusmali Kazan",
            "description": "Yogusmali kazan exergy analizi",
        },
        {
            "type": "waste_heat",
            "name": "Atik Isi / HRSG",
            "description": "Atik isi kazani / HRSG exergy analizi",
        },
        {
            "type": "electric",
            "name": "Elektrikli Kazan",
            "description": "Elektrikli kazan exergy analizi",
        },
        {
            "type": "biomass",
            "name": "Biyokutle Kazani",
            "description": "Biyokutle kazani exergy analizi",
        },
    ]


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_benchmark_comparison(eta_ex: float, boiler_type: str) -> str:
    """Exergy verimine gore benchmark karsilastirmasi."""
    benchmarks = {
        'steam_firetube': {'poor': 25, 'average': 35, 'good': 42, 'excellent': 48},
        'steam_watertube': {'poor': 28, 'average': 38, 'good': 45, 'excellent': 50},
        'hotwater': {'poor': 8, 'average': 12, 'good': 16, 'excellent': 20},
        'condensing': {'poor': 10, 'average': 15, 'good': 20, 'excellent': 25},
        'waste_heat': {'poor': 20, 'average': 30, 'good': 40, 'excellent': 50},
        'electric': {'poor': 8, 'average': 12, 'good': 16, 'excellent': 20},
        'biomass': {'poor': 20, 'average': 30, 'good': 38, 'excellent': 44},
    }
    thresholds = benchmarks.get(boiler_type, benchmarks['steam_firetube'])

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


def _calculate_percentile(eta_ex: float, boiler_type: str) -> int:
    """Exergy verimini 0-100 yuzdelik dilime esler."""
    benchmarks = {
        'steam_firetube': {'low': 20, 'mid': 35, 'high': 48},
        'steam_watertube': {'low': 22, 'mid': 38, 'high': 50},
        'hotwater': {'low': 6, 'mid': 12, 'high': 20},
        'condensing': {'low': 8, 'mid': 15, 'high': 25},
        'waste_heat': {'low': 18, 'mid': 30, 'high': 50},
        'electric': {'low': 6, 'mid': 12, 'high': 20},
        'biomass': {'low': 18, 'mid': 30, 'high': 44},
    }
    thresholds = benchmarks.get(boiler_type, benchmarks['steam_firetube'])

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
