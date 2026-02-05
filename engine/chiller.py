"""
ExergyLab - Chiller Exergy Analysis

Chiller exergy hesaplamalari.
Vidali, santrifuj, scroll, pistonlu ve absorpsiyonlu chiller tipleri icin.
Carnot bazli hesaplamalar - CoolProp gerektirmez.
"""

from dataclasses import dataclass
from typing import Optional
import math

import copy

from .core import DeadState, ExergyResult, compute_avoidable_split, celsius_to_kelvin
from .exergoeconomic import _apply_exergoeconomic


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

KW_PER_TON = 3.517  # 1 ton of refrigeration = 3.517 kW

# Best-achievable COP per chiller type (Tsatsaronis & Morosuk 2008)
UNAVOIDABLE_REF_CHILLER = {
    'screw': {'best_cop': 7.0},
    'centrifugal': {'best_cop': 8.0},
    'scroll': {'best_cop': 5.5},
    'reciprocating': {'best_cop': 6.0},
    'air_cooled': {'best_cop': 4.5},
    'water_cooled': {'best_cop': 7.5},
    'absorption': {'best_cop_thermal': 0.80},
}


# ---------------------------------------------------------------------------
# Input dataclass
# ---------------------------------------------------------------------------

@dataclass
class ChillerInput:
    """Chiller analizi icin giris verileri"""

    # Zorunlu
    cooling_capacity_kW: float       # Sogutma kapasitesi [kW]
    compressor_power_kW: float       # Kompressor elektrik gucu [kW] (vapor compression)

    # Opsiyonel - sicakliklar
    chw_supply_temp_C: float = 7.0    # Soguk su cikis sicakligi [C]
    chw_return_temp_C: float = 12.0   # Soguk su donus sicakligi [C]
    cw_supply_temp_C: float = 30.0    # Kondenser suyu giris sicakligi [C]
    cw_return_temp_C: float = 35.0    # Kondenser suyu cikis sicakligi [C]

    # Ekipman bilgisi
    chiller_type: str = "centrifugal"  # screw, centrifugal, scroll, reciprocating, absorption, air_cooled, water_cooled
    condenser_type: str = "water"       # water, air
    ambient_temp_C: Optional[float] = None

    # Absorpsiyon chiller icin
    generator_heat_kW: Optional[float] = None    # Jenerator isisi [kW]
    generator_temp_C: Optional[float] = None      # Jenerator sicakligi [C]

    # Operasyonel
    operating_hours: float = 4000
    electricity_price_eur_kwh: float = 0.12
    equipment_cost_eur: Optional[float] = None  # Ekipman maliyeti PEC [€]

    def __post_init__(self):
        if self.ambient_temp_C is None:
            self.ambient_temp_C = 25.0
        if self.chiller_type == "absorption":
            if self.generator_heat_kW is None:
                # Estimate: COP_abs ~ 0.7 for single-effect
                self.generator_heat_kW = self.cooling_capacity_kW / 0.7
            if self.generator_temp_C is None:
                self.generator_temp_C = 90.0


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class ChillerResult(ExergyResult):
    """Chiller analizi sonuclari"""

    cop: Optional[float] = None
    cop_carnot: Optional[float] = None
    kw_per_ton: Optional[float] = None
    condenser_loss_kW: Optional[float] = None
    internal_loss_kW: Optional[float] = None
    benchmark_comparison: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            'cop': round(self.cop, 2) if self.cop else None,
            'cop_carnot': round(self.cop_carnot, 2) if self.cop_carnot else None,
            'kw_per_ton': round(self.kw_per_ton, 3) if self.kw_per_ton else None,
            'condenser_loss_kW': round(self.condenser_loss_kW, 2) if self.condenser_loss_kW else None,
            'internal_loss_kW': round(self.internal_loss_kW, 2) if self.internal_loss_kW else None,
            'benchmark_comparison': self.benchmark_comparison,
        })
        return base

    def to_api_dict(self, chiller_type: str = "centrifugal") -> dict:
        """API yanit formatina donusturur."""
        return {
            "exergy_input_kW": round(self.exergy_in_kW, 2),
            "exergy_output_kW": round(self.exergy_out_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "cop": round(self.cop, 2) if self.cop else None,
            "cop_carnot": round(self.cop_carnot, 2) if self.cop_carnot else None,
            "kw_per_ton": round(self.kw_per_ton, 3) if self.kw_per_ton else None,
            "condenser_loss_kW": round(self.condenser_loss_kW, 2) if self.condenser_loss_kW else None,
            "internal_loss_kW": round(self.internal_loss_kW, 2) if self.internal_loss_kW else None,
            "annual_loss_kWh": round(self.annual_loss_kWh, 0) if self.annual_loss_kWh else None,
            "annual_loss_EUR": round(self.annual_loss_EUR, 0) if self.annual_loss_EUR else None,
            "benchmark_comparison": self.benchmark_comparison,
            "benchmark_percentile": _calculate_percentile(self.exergy_efficiency_pct, chiller_type),
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
# Analysis function
# ---------------------------------------------------------------------------

def analyze_chiller(input_data: ChillerInput, dead_state: DeadState = None, _calc_avoidable: bool = True) -> ChillerResult:
    """
    Chiller exergy analizi yapar.

    Vapor compression:
        COP = Q_cool / W_comp
        COP_carnot = T_evap / (T_cond - T_evap)
        Ex_cool = Q_cool * (T_0 - T_cool) / T_0
        eta_ex = Ex_cool / W_comp * 100

    Absorption:
        COP = Q_cool / Q_gen
        Ex_heat = Q_gen * (1 - T_0 / T_gen)
        eta_ex = Ex_cool / Ex_heat * 100
    """
    if dead_state is None:
        dead_state = DeadState.from_celsius(input_data.ambient_temp_C)

    T0 = dead_state.T0  # K

    # Evaporator temperature (average of CHW supply/return)
    T_cool_C = (input_data.chw_supply_temp_C + input_data.chw_return_temp_C) / 2.0
    T_cool_K = celsius_to_kelvin(T_cool_C)

    # Condenser temperature (average of CW supply/return)
    T_cond_C = (input_data.cw_supply_temp_C + input_data.cw_return_temp_C) / 2.0
    T_cond_K = celsius_to_kelvin(T_cond_C)

    # Estimate evaporator/condenser refrigerant temps (with approach)
    T_evap_K = T_cool_K - 3.0   # ~3K approach
    T_cond_ref_K = T_cond_K + 3.0  # ~3K approach

    is_absorption = (input_data.chiller_type == "absorption")

    Q_cool = input_data.cooling_capacity_kW

    if is_absorption:
        # Absorption chiller
        Q_gen = input_data.generator_heat_kW
        T_gen_K = celsius_to_kelvin(input_data.generator_temp_C)
        W_comp = input_data.compressor_power_kW  # Solution pump power (usually small)

        cop = Q_cool / Q_gen if Q_gen > 0 else 0.0

        # Exergy of generator heat
        Ex_heat = Q_gen * (1.0 - T0 / T_gen_K) if T_gen_K > T0 else 0.0
        Ex_in = Ex_heat + W_comp

        # Carnot COP for absorption
        if T_gen_K > T_cond_ref_K and T_cond_ref_K > T_evap_K:
            cop_carnot = (T_evap_K / (T_cond_ref_K - T_evap_K)) * ((T_gen_K - T_cond_ref_K) / T_gen_K)
        else:
            cop_carnot = cop * 2.0  # fallback estimate
    else:
        # Vapor compression chiller
        W_comp = input_data.compressor_power_kW
        cop = Q_cool / W_comp if W_comp > 0 else 0.0

        # Carnot COP
        if T_cond_ref_K > T_evap_K:
            cop_carnot = T_evap_K / (T_cond_ref_K - T_evap_K)
        else:
            cop_carnot = cop * 2.0

        Ex_in = W_comp

    # Cooling exergy: Ex_cool = Q_cool * (T_0 - T_cool) / T_0
    # For cooling below ambient, the exergy is positive when T_cool < T_0
    if T_cool_K < T0:
        Ex_cool = Q_cool * (T0 - T_cool_K) / T0
    else:
        Ex_cool = 0.0

    Ex_out = Ex_cool
    Ex_destroyed = max(0.0, Ex_in - Ex_out)
    eta_ex = (Ex_out / Ex_in) * 100 if Ex_in > 0 else 0.0

    # kW/ton
    kw_per_ton = KW_PER_TON / cop if cop > 0 else None

    # Condenser loss (heat rejected to environment)
    Q_cond = Q_cool + W_comp if not is_absorption else Q_cool + Q_gen
    # Exergy of condenser heat (typically low-grade, most is anergy)
    condenser_exergy_loss = Q_cond * abs(T_cond_K - T0) / T_cond_K if T_cond_K > 0 else 0.0

    # Internal irreversibility
    internal_loss = max(0.0, Ex_destroyed - condenser_exergy_loss)

    # Annual losses
    annual_loss_kWh = Ex_destroyed * input_data.operating_hours
    annual_loss_EUR = annual_loss_kWh * input_data.electricity_price_eur_kwh

    benchmark = _get_benchmark_comparison(eta_ex, input_data.chiller_type)

    result = ChillerResult(
        exergy_in_kW=Ex_in,
        exergy_out_kW=Ex_out,
        exergy_destroyed_kW=Ex_destroyed,
        exergy_efficiency_pct=eta_ex,
        annual_loss_kWh=annual_loss_kWh,
        annual_loss_EUR=annual_loss_EUR,
        cop=cop,
        cop_carnot=cop_carnot,
        kw_per_ton=kw_per_ton,
        condenser_loss_kW=condenser_exergy_loss,
        internal_loss_kW=internal_loss,
        benchmark_comparison=benchmark,
    )

    # AV/UN split
    if _calc_avoidable and Ex_destroyed > 0:
        ref = UNAVOIDABLE_REF_CHILLER.get(input_data.chiller_type, {})
        un_input = copy.deepcopy(input_data)
        if is_absorption and 'best_cop_thermal' in ref:
            best_cop = ref['best_cop_thermal']
            if cop < best_cop:
                un_input.generator_heat_kW = Q_cool / best_cop
        elif 'best_cop' in ref:
            best_cop = ref['best_cop']
            if cop < best_cop:
                un_input.compressor_power_kW = Q_cool / best_cop
        un_result = analyze_chiller(un_input, dead_state=dead_state, _calc_avoidable=False)
        av, un, ratio = compute_avoidable_split(Ex_destroyed, un_result.exergy_destroyed_kW)
        result.exergy_destroyed_avoidable_kW = av
        result.exergy_destroyed_unavoidable_kW = un
        result.avoidable_ratio_pct = ratio

    # Exergoeconomic analysis
    _apply_exergoeconomic(
        result, equipment_type='chiller',
        c_fuel_eur_kWh=input_data.electricity_price_eur_kwh,
        capacity_param_kW=input_data.cooling_capacity_kW,
        equipment_cost_eur=input_data.equipment_cost_eur,
        annual_operating_hours=input_data.operating_hours,
        subtype=input_data.chiller_type,
    )

    return result


# ---------------------------------------------------------------------------
# Sankey data
# ---------------------------------------------------------------------------

def generate_chiller_sankey_data(result: ChillerResult, chiller_type: str = "centrifugal") -> dict:
    """
    Chiller Sankey diyagrami icin node ve link verisi olusturur.

    Nodes: Elektrik -> Chiller -> Sogutma Exergy / Kondenser Atik / Ic Kayiplar
    """
    Ex_in = result.exergy_in_kW
    Ex_out = result.exergy_out_kW
    condenser_loss = result.condenser_loss_kW or 0.0
    internal_loss = result.internal_loss_kW or 0.0

    # Normalize
    total_out = Ex_out + condenser_loss + internal_loss
    if total_out > 0 and abs(total_out - Ex_in) > 0.01:
        scale = Ex_in / total_out
        Ex_out_norm = Ex_out * scale
        condenser_norm = condenser_loss * scale
        internal_norm = internal_loss * scale
    else:
        Ex_out_norm = Ex_out
        condenser_norm = condenser_loss
        internal_norm = internal_loss

    is_absorption = (chiller_type == "absorption")
    input_name = "Jenerator Isisi" if is_absorption else "Elektrik Enerjisi"
    input_name_en = "Generator Heat" if is_absorption else "Electrical Energy"

    nodes = [
        {"id": 0, "name": input_name, "name_en": input_name_en},
        {"id": 1, "name": "Chiller", "name_en": "Chiller"},
        {"id": 2, "name": "Sogutma Exergy", "name_en": "Cooling Exergy"},
        {"id": 3, "name": "Kondenser Atik", "name_en": "Condenser Rejection"},
        {"id": 4, "name": "Ic Kayiplar", "name_en": "Internal Losses"},
    ]

    links = [
        {"source": 0, "target": 1, "value": round(Ex_in, 2), "label": input_name},
        {"source": 1, "target": 2, "value": round(Ex_out_norm, 2), "label": "Sogutma Exergy"},
        {"source": 1, "target": 3, "value": round(condenser_norm, 2), "label": "Kondenser Kaybi"},
        {"source": 1, "target": 4, "value": round(internal_norm, 2), "label": "Ic Tersinmezlik"},
    ]

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": round(Ex_in, 2),
            "useful_output_kW": round(Ex_out_norm, 2),
            "recoverable_heat_kW": 0.0,
            "irreversibility_kW": round(condenser_norm + internal_norm, 2),
            "efficiency_pct": round(result.exergy_efficiency_pct, 1),
            "exergy_destroyed_avoidable_kW": round(getattr(result, 'exergy_destroyed_avoidable_kW', 0.0) or 0.0, 2),
            "exergy_destroyed_unavoidable_kW": round(getattr(result, 'exergy_destroyed_unavoidable_kW', 0.0) or 0.0, 2),
            "avoidable_ratio_pct": round(getattr(result, 'avoidable_ratio_pct', 0.0) or 0.0, 1),
        },
    }


# ---------------------------------------------------------------------------
# Recommendations
# ---------------------------------------------------------------------------

def get_chiller_recommendations(result: ChillerResult, input_data: ChillerInput) -> list:
    """Chiller analiz sonuclarina gore iyilestirme onerileri."""
    recommendations = []

    # COP improvement
    if result.cop and result.cop < 4.0 and input_data.chiller_type != "absorption":
        savings = input_data.compressor_power_kW * 0.15 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'cop_improvement',
            'title': 'COP Iyilestirme',
            'description': f'COP = {result.cop:.2f}. Kondenser/evaporator temizligi ve sarj kontrolu onerilir.',
            'investment_eur': 2000,
            'savings_eur_year': savings,
            'payback_years': 2000 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # Chilled water reset
    if input_data.chw_supply_temp_C < 7:
        savings = input_data.compressor_power_kW * 0.03 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'chw_reset',
            'title': 'Soguk Su Sicakligi Yukseltme',
            'description': f'CHW = {input_data.chw_supply_temp_C}C. Her 1C artis ~%3 enerji tasarrufu saglar.',
            'investment_eur': 500,
            'savings_eur_year': savings,
            'payback_years': 500 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # Condenser water optimization
    if input_data.condenser_type == "water" and input_data.cw_supply_temp_C > 30:
        savings = input_data.compressor_power_kW * 0.05 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'condenser_optimization',
            'title': 'Kondenser Suyu Optimizasyonu',
            'description': 'Kondenser suyu sicakligini dusurme (kule optimizasyonu).',
            'investment_eur': 3000,
            'savings_eur_year': savings,
            'payback_years': 3000 / savings if savings > 0 else float('inf'),
            'priority': 'medium',
        })

    # Maintenance
    if result.benchmark_comparison in ('poor', 'below_average'):
        savings = input_data.compressor_power_kW * 0.10 * input_data.operating_hours * input_data.electricity_price_eur_kwh
        recommendations.append({
            'type': 'maintenance',
            'title': 'Bakim ve Kontrol',
            'description': 'Exergy verimi dusuk. Sogutkan sarji, evaporator/kondenser temizligi onerilir.',
            'investment_eur': 1000,
            'savings_eur_year': savings,
            'payback_years': 1000 / savings if savings > 0 else float('inf'),
            'priority': 'high',
        })

    # Free cooling
    if input_data.ambient_temp_C and input_data.ambient_temp_C < 15:
        recommendations.append({
            'type': 'free_cooling',
            'title': 'Serbest Sogutma (Free Cooling)',
            'description': 'Dusuk dis sicaklikta kompresorsuz sogutma imkani degerlendirilmeli.',
            'investment_eur': 15000,
            'savings_eur_year': input_data.compressor_power_kW * 0.30 * input_data.operating_hours * input_data.electricity_price_eur_kwh,
            'payback_years': 3.0,
            'priority': 'medium',
        })

    return recommendations


# ---------------------------------------------------------------------------
# Chiller types helper
# ---------------------------------------------------------------------------

def get_chiller_types() -> list:
    """Desteklenen chiller tiplerini dondurur."""
    return [
        {
            "type": "screw",
            "name": "Vidali Chiller",
            "description": "Vidali kompressorlu chiller analizi",
        },
        {
            "type": "centrifugal",
            "name": "Santrifuj Chiller",
            "description": "Santrifuj kompressorlu chiller analizi",
        },
        {
            "type": "scroll",
            "name": "Scroll Chiller",
            "description": "Scroll kompressorlu chiller analizi",
        },
        {
            "type": "reciprocating",
            "name": "Pistonlu Chiller",
            "description": "Pistonlu kompressorlu chiller analizi",
        },
        {
            "type": "absorption",
            "name": "Absorpsiyonlu Chiller",
            "description": "Absorpsiyonlu chiller analizi (tek/cift etkili)",
        },
        {
            "type": "air_cooled",
            "name": "Hava Sogutmali Chiller",
            "description": "Hava sogutmali chiller analizi",
        },
        {
            "type": "water_cooled",
            "name": "Su Sogutmali Chiller",
            "description": "Su sogutmali chiller analizi",
        },
    ]


# ---------------------------------------------------------------------------
# Benchmark helpers
# ---------------------------------------------------------------------------

def _get_benchmark_comparison(eta_ex: float, chiller_type: str) -> str:
    """Exergy verimine gore benchmark karsilastirmasi."""
    benchmarks = {
        'screw': {'poor': 20, 'average': 30, 'good': 40, 'excellent': 50},
        'centrifugal': {'poor': 25, 'average': 35, 'good': 45, 'excellent': 55},
        'scroll': {'poor': 18, 'average': 28, 'good': 38, 'excellent': 48},
        'reciprocating': {'poor': 18, 'average': 28, 'good': 38, 'excellent': 48},
        'absorption': {'poor': 5, 'average': 10, 'good': 18, 'excellent': 25},
        'air_cooled': {'poor': 15, 'average': 25, 'good': 35, 'excellent': 45},
        'water_cooled': {'poor': 22, 'average': 32, 'good': 42, 'excellent': 52},
    }
    thresholds = benchmarks.get(chiller_type, benchmarks['centrifugal'])

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


def _calculate_percentile(eta_ex: float, chiller_type: str) -> int:
    """Exergy verimini 0-100 yuzdelik dilime esler."""
    benchmarks = {
        'centrifugal': {'low': 20, 'mid': 35, 'high': 55},
        'screw': {'low': 18, 'mid': 30, 'high': 50},
        'scroll': {'low': 15, 'mid': 28, 'high': 48},
        'reciprocating': {'low': 15, 'mid': 28, 'high': 48},
        'absorption': {'low': 5, 'mid': 12, 'high': 25},
        'air_cooled': {'low': 12, 'mid': 25, 'high': 45},
        'water_cooled': {'low': 18, 'mid': 32, 'high': 52},
    }
    thresholds = benchmarks.get(chiller_type, benchmarks['centrifugal'])

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
