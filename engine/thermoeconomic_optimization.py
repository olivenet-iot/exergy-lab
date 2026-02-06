"""
ExergyLab - Thermoeconomic Optimization Motor Modulu

Tsatsaronis'in termoekonomik optimizasyon karar kurallari:
  - f-faktor (Z_dot / C_total_dot) ve r-faktor baziyla strateji belirleme
  - SPECO + AV/UN sonuclarindan optimizasyon onerileri uretme
  - Ekipman bazli aksiyon, yatirim tahmini ve geri odeme hesabi

Referanslar:
  - Tsatsaronis, G. & Park, M.-H. (2002). "On avoidable and unavoidable
    exergy destructions and investment costs in thermal systems"
  - Bejan, A., Tsatsaronis, G. & Moran, M. (1996). "Thermal Design
    and Optimization"
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Strategy labels (Turkish)
STRATEGY_LABELS: Dict[str, str] = {
    "invest": "Verimli ekipmana yatirim",
    "parametric": "Parametrik optimizasyon",
    "structural": "Yapisal degisiklik",
    "downsize": "Boyut kucultme",
    "maintain": "Mevcut durumu surdur",
}

# Strategy colors (for frontend)
STRATEGY_COLORS: Dict[str, str] = {
    "invest": "#ef4444",       # Red — high investment
    "parametric": "#f59e0b",   # Orange — medium effort
    "structural": "#8b5cf6",   # Purple — system change
    "downsize": "#3b82f6",     # Blue — cost reduction
    "maintain": "#22c55e",     # Green — no issue
}

# Equipment-type-specific optimization actions (Turkish)
OPTIMIZATION_ACTIONS: Dict[str, Dict[str, List[str]]] = {
    "compressor": {
        "invest": [
            "Yuksek verimli motor ve VSD (degisken hiz surucusu) ekleyin",
            "Izentropik verimi yuksek kompresor tipine gecin",
            "Cok kademeli kompresyon ile ara sogutma ekleyin",
        ],
        "parametric": [
            "Basinc oranini optimize edin (kacak testi yapin)",
            "Emme havasi sicakligini dusurun (aftercooler bakimi)",
            "Yuk profilini analiz edin — kismi yukte VSD kullanin",
        ],
        "structural": [
            "Kompresyon kademesi ekleyin (2→3 kademe)",
            "Isi geri kazanimli kompresor sistemine gecin",
            "Merkezi sistemi bolgesel unitelere ayirin",
        ],
        "downsize": [
            "Asiri boyutlandirma analizi yapin",
            "Sabit hizli yerine VSD'li daha kucuk unite degerlendirin",
        ],
    },
    "boiler": {
        "invest": [
            "Yogusmali kazan teknolojisine gecin",
            "Economizer / hava on isitici ekleyin",
            "Atik isi geri kazanim sistemi kurun",
        ],
        "parametric": [
            "Fazla hava oranini optimize edin (O2 trim kontrol)",
            "Baca gazi sicakligini dusurun (economizer bakimi)",
            "Blof oranini optimize edin",
        ],
        "structural": [
            "Bolgesel isitma agi kurun (birden fazla kazan)",
            "Kojenerasyon (CHP) sistemi degerlendirin",
            "Yakit tipini degistirin (dogalgaz → biyokutle/atik isi)",
        ],
        "downsize": [
            "Kazan kapasitesini yeniden boyutlandirin",
            "Moduler kazan sistemi degerlendirin",
        ],
    },
    "chiller": {
        "invest": [
            "Yuksek COP'lu chiller'a gecin",
            "Serbest sogutma (free cooling) sistemi ekleyin",
            "Soguk aku (thermal storage) degerlendirin",
        ],
        "parametric": [
            "Evaporator/kondenser yaklasim sicakligini optimize edin",
            "Sogutma kulesi bakimini artirin (kondenser sicakligi)",
            "Set noktasini mevsime gore ayarlayin",
        ],
        "structural": [
            "Absorpsiyon chiller ile atik isi kullanin",
            "Kaskad sogutma sistemi degerlendirin",
            "Bolgesel sogutma agi kurun",
        ],
        "downsize": [
            "Sogutma yukunu yeniden hesaplayin",
            "Degisken debili pompalama sistemi kurun",
        ],
    },
    "pump": {
        "invest": [
            "Yuksek verimli motor ve VSD ekleyin",
            "Pompa tipini optimize edin (spesifik hiz uyumu)",
        ],
        "parametric": [
            "Calisma noktasini BEP'e (en iyi verimlilik noktasi) yaklastirin",
            "Boru hatti kayiplarini azaltin (vana, dirsek)",
            "Impeller capini optimize edin",
        ],
        "structural": [
            "Paralel pompa konfigurasyonu degerlendirin",
            "Booster pompa ekleyerek ana pompa boyutunu kucultun",
        ],
        "downsize": [
            "Asiri boyutlanmis pompayi degistirin",
            "Impeller kirpma (trimming) uygulayin",
        ],
    },
    "heat_exchanger": {
        "invest": [
            "Daha buyuk isi transfer alani ile DeltaT yaklasimini dusurun",
            "Plakali esanjore gecin (daha yuksek U degeri)",
            "Fouling direncini azaltan yuzey kaplamasi uygulayin",
        ],
        "parametric": [
            "Temizlik programini optimize edin (fouling kontrolu)",
            "Akis hizlarini optimize edin (DeltaP vs. DeltaT dengesi)",
            "Bypass ayarini kontrol edin",
        ],
        "structural": [
            "Cok akisli esanjor agi tasarlayin (pinch analizi)",
            "Isi pompali geri kazanim sistemi ekleyin",
            "Kondensasyon ekonomizeri ekleyin",
        ],
        "downsize": [
            "Asiri boyutlanmis esanjoru kucultun",
            "Paralel baglantiyi seri baglantiya cevirin",
        ],
    },
    "steam_turbine": {
        "invest": [
            "Daha yuksek izentropik verimli turbine gecin",
            "Cok kademeli turbin degerlendirin",
            "Kanatcik yukseltme/degistirme yapin",
        ],
        "parametric": [
            "Giris buhari kosullarini optimize edin (kazan ile koordine)",
            "Cikis basincini optimize edin",
            "Sizinti kontrolu yapin (saft contasi)",
        ],
        "structural": [
            "Ekstraksiyon turbine gecin (CHP)",
            "ORC (Organik Rankine Cevrimi) ekleyin",
            "Kondens sistemi iyilestirin (vakum)",
        ],
        "downsize": [
            "Turbin kapasitesini yeniden degerlendirin",
            "Kismi yuk performansini analiz edin",
        ],
    },
    "dryer": {
        "invest": [
            "Isi pompali kurutma sistemine gecin",
            "Egzoz havasi isi geri kazanimi ekleyin",
            "Mekanik on-susuzlastirma ile termal yuku azaltin",
        ],
        "parametric": [
            "Kurutma havasi sicaklik ve debisini optimize edin",
            "Cikis nem kontrol stratejisini iyilestirin",
            "Urun giris nem oranini dusurun (on islem)",
        ],
        "structural": [
            "Cok kademeli kurutma sistemi degerlendirin",
            "Gunes enerjili on isitma ekleyin",
            "Atik isi kaynagindan besleme yapin",
        ],
        "downsize": [
            "Kurutma kapasitesini uretim hizina gore ayarlayin",
            "Kesikli/surekli mod secimini optimize edin",
        ],
    },
}

# Investment cost estimation lambdas (EUR) — capacity in kW
INVESTMENT_ESTIMATES: Dict[str, Dict[str, object]] = {
    "compressor": {
        "invest": lambda cap: 500 * cap**0.7,       # VSD + high efficiency motor
        "parametric": lambda cap: 50 * cap**0.5,     # Control optimization
        "structural": lambda cap: 800 * cap**0.7,    # Stage addition
        "downsize": lambda cap: 300 * cap**0.7,      # New smaller unit
    },
    "boiler": {
        "invest": lambda cap: 400 * cap**0.75,       # Economizer + control
        "parametric": lambda cap: 30 * cap**0.5,     # O2 trim
        "structural": lambda cap: 1200 * cap**0.75,  # CHP system
        "downsize": lambda cap: 250 * cap**0.75,     # Modular boiler
    },
    "chiller": {
        "invest": lambda cap: 350 * cap**0.8,        # High COP chiller
        "parametric": lambda cap: 40 * cap**0.5,     # Optimization
        "structural": lambda cap: 600 * cap**0.8,    # Absorption addition
        "downsize": lambda cap: 200 * cap**0.8,      # Downsizing
    },
    "pump": {
        "invest": lambda cap: 300 * cap**0.65,       # VSD + efficient motor
        "parametric": lambda cap: 20 * cap**0.5,     # Impeller trim
        "structural": lambda cap: 400 * cap**0.65,   # Parallel pump
        "downsize": lambda cap: 150 * cap**0.65,     # Smaller pump
    },
    "heat_exchanger": {
        "invest": lambda cap: 250 * cap**0.7,        # Larger area / plate
        "parametric": lambda cap: 15 * cap**0.5,     # Cleaning program
        "structural": lambda cap: 500 * cap**0.7,    # HEN redesign
        "downsize": lambda cap: 100 * cap**0.7,      # Downsizing
    },
    "steam_turbine": {
        "invest": lambda cap: 600 * cap**0.7,        # Blade upgrade
        "parametric": lambda cap: 40 * cap**0.5,     # Leakage control
        "structural": lambda cap: 1500 * cap**0.7,   # ORC addition
        "downsize": lambda cap: 400 * cap**0.7,      # Resizing
    },
    "dryer": {
        "invest": lambda cap: 450 * cap**0.7,        # Heat recovery
        "parametric": lambda cap: 35 * cap**0.5,     # Control improvement
        "structural": lambda cap: 700 * cap**0.7,    # Multi-stage
        "downsize": lambda cap: 200 * cap**0.7,      # Capacity reduction
    },
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class OptimizationRecommendation:
    """Per-equipment thermoeconomic optimization recommendation."""
    equipment_id: str
    equipment_name: str
    equipment_type: str
    subtype: str

    # SPECO metrics (from existing results)
    f_factor: float                      # Z_dot / (Z_dot + C_dot_D)
    r_factor: float                      # (c_product - c_fuel) / c_fuel
    Z_dot_eur_h: float                   # Investment cost rate
    C_dot_D_eur_h: float                 # Destruction cost rate
    C_total_dot_eur_h: float             # Z_dot + C_dot_D

    # AV/UN
    avoidable_ratio: float               # 0-1

    # Optimization strategy
    strategy: str                        # "invest" | "parametric" | "structural" | "downsize" | "maintain"
    strategy_label: str                  # Human-readable label
    priority: str                        # "high" | "medium" | "low"

    # Actions (equipment-type specific)
    recommended_actions: List[str] = field(default_factory=list)

    # Economic potential
    C_savings_potential_eur_h: float = 0.0     # C_dot_D * avoidable_ratio
    C_savings_annual_eur: float = 0.0          # Annual savings
    estimated_investment_eur: float = 0.0      # Estimated investment cost
    simple_payback_years: float = 99.9         # Simple payback period

    def to_dict(self) -> dict:
        return {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "subtype": self.subtype,
            "f_factor": round(self.f_factor, 3),
            "r_factor": round(self.r_factor, 3),
            "Z_dot_eur_h": round(self.Z_dot_eur_h, 4),
            "C_dot_D_eur_h": round(self.C_dot_D_eur_h, 4),
            "C_total_dot_eur_h": round(self.C_total_dot_eur_h, 4),
            "avoidable_ratio": round(self.avoidable_ratio, 3),
            "strategy": self.strategy,
            "strategy_label": self.strategy_label,
            "priority": self.priority,
            "recommended_actions": self.recommended_actions,
            "C_savings_potential_eur_h": round(self.C_savings_potential_eur_h, 4),
            "C_savings_annual_eur": round(self.C_savings_annual_eur, 2),
            "estimated_investment_eur": round(self.estimated_investment_eur, 2),
            "simple_payback_years": round(self.simple_payback_years, 1),
        }


@dataclass
class ThermoeconomicOptimizationResult:
    """Factory-level thermoeconomic optimization result."""
    is_valid: bool = True
    error_message: str = ""

    num_equipment: int = 0
    operating_hours: int = 8000

    # Total costs
    total_Z_dot_eur_h: float = 0.0
    total_C_dot_D_eur_h: float = 0.0
    total_C_total_dot_eur_h: float = 0.0
    factory_f_factor: float = 0.0

    # Total optimization potential
    total_savings_potential_eur_h: float = 0.0
    total_savings_annual_eur: float = 0.0
    total_estimated_investment_eur: float = 0.0
    factory_payback_years: float = 99.9

    # Strategy distribution
    strategy_distribution: Dict[str, int] = field(default_factory=dict)

    # Priority distribution
    priority_distribution: Dict[str, int] = field(default_factory=dict)

    # Equipment recommendations (sorted by C_savings_annual desc)
    recommendations: List[OptimizationRecommendation] = field(default_factory=list)

    # Cost-benefit ranking
    cost_benefit_ranking: List[Dict] = field(default_factory=list)

    # Visualization data
    f_r_scatter_data: Dict = field(default_factory=dict)
    savings_waterfall_data: Dict = field(default_factory=dict)

    # Warnings
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "num_equipment": self.num_equipment,
            "operating_hours": self.operating_hours,
            "total_Z_dot_eur_h": round(self.total_Z_dot_eur_h, 4),
            "total_C_dot_D_eur_h": round(self.total_C_dot_D_eur_h, 4),
            "total_C_total_dot_eur_h": round(self.total_C_total_dot_eur_h, 4),
            "factory_f_factor": round(self.factory_f_factor, 3),
            "total_savings_potential_eur_h": round(self.total_savings_potential_eur_h, 4),
            "total_savings_annual_eur": round(self.total_savings_annual_eur, 2),
            "total_estimated_investment_eur": round(self.total_estimated_investment_eur, 2),
            "factory_payback_years": round(self.factory_payback_years, 1),
            "strategy_distribution": self.strategy_distribution,
            "priority_distribution": self.priority_distribution,
            "recommendations": [r.to_dict() for r in self.recommendations],
            "cost_benefit_ranking": self.cost_benefit_ranking,
            "f_r_scatter_data": self.f_r_scatter_data,
            "savings_waterfall_data": self.savings_waterfall_data,
            "warnings": self.warnings,
        }


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _get_item_field(item, field_name: str):
    """Get a field from an item (dict or object)."""
    if isinstance(item, dict):
        return item.get(field_name, "")
    return getattr(item, field_name, "")


def _filter_valid_equipment(
    equipment_list: list,
    analysis_results: dict,
) -> list:
    """Keep only equipment with exergoeconomic data (f_factor present and >= 0)."""
    valid = []
    for item in equipment_list:
        eq_id = _get_item_field(item, "id")
        result = analysis_results.get(eq_id)
        if not result:
            continue
        f = result.get("exergoeconomic_f_factor")
        if f is not None and f >= 0:
            valid.append(item)
    return valid


def _determine_strategy(
    f_factor: float, r_factor: float, avoidable_ratio: float,
) -> Tuple[str, str, str]:
    """Determine optimization strategy from f/r decision matrix.

    Args:
        f_factor: Z_dot / (Z_dot + C_dot_D)
        r_factor: (c_product - c_fuel) / c_fuel
        avoidable_ratio: Fraction of avoidable exergy destruction (0-1)

    Returns:
        (strategy, label, priority)
    """
    if f_factor < 0.25:
        if r_factor > 0.50:
            return "invest", STRATEGY_LABELS["invest"], "high"
        else:
            return "parametric", STRATEGY_LABELS["parametric"], "medium"
    elif f_factor > 0.65:
        if r_factor > 0.50:
            return "structural", STRATEGY_LABELS["structural"], "high"
        else:
            return "downsize", STRATEGY_LABELS["downsize"], "medium"
    else:  # 0.25 <= f <= 0.65
        if avoidable_ratio > 0.30:
            return "parametric", STRATEGY_LABELS["parametric"], "medium"
        else:
            return "maintain", STRATEGY_LABELS["maintain"], "low"


def _get_equipment_actions(eq_type: str, strategy: str) -> List[str]:
    """Get equipment-type-specific optimization actions."""
    type_actions = OPTIMIZATION_ACTIONS.get(eq_type, {})
    actions = type_actions.get(strategy, [])
    if not actions:
        # Generic fallback actions
        fallback = {
            "invest": ["Daha verimli ekipmana yatirim yapin"],
            "parametric": ["Calisma parametrelerini optimize edin"],
            "structural": ["Sistem konfigurasyonunu degistirin"],
            "downsize": ["Ekipman boyutunu kucultun"],
            "maintain": ["Mevcut bakim programini surdurun"],
        }
        actions = fallback.get(strategy, ["Degerlendirme yapin"])
    return actions


def _estimate_investment(eq_type: str, strategy: str, capacity_kW: float) -> float:
    """Estimate optimization investment cost (EUR).

    Args:
        eq_type: Equipment type
        strategy: Optimization strategy
        capacity_kW: Equipment capacity in kW

    Returns:
        Estimated investment in EUR
    """
    if strategy == "maintain":
        return 0.0

    type_estimates = INVESTMENT_ESTIMATES.get(eq_type, {})
    estimator = type_estimates.get(strategy)

    cap = max(capacity_kW, 10)  # Min 10 kW floor
    if estimator and capacity_kW > 0:
        return estimator(cap)

    # Generic fallback
    fallback = {
        "invest": 300 * cap**0.7,
        "parametric": 30 * cap**0.5,
        "structural": 600 * cap**0.7,
        "downsize": 150 * cap**0.7,
    }
    return fallback.get(strategy, 0.0)


def _generate_recommendation(
    item, result: dict, operating_hours: int,
) -> OptimizationRecommendation:
    """Generate optimization recommendation for a single equipment.

    Reads SPECO fields from result, determines strategy, calculates
    savings, investment, and payback.
    """
    eq_id = _get_item_field(item, "id")
    eq_name = _get_item_field(item, "name") or _get_item_field(item, "equipment_type")
    eq_type = _get_item_field(item, "equipment_type")
    subtype = _get_item_field(item, "subtype") or "_default"

    # SPECO data
    f = result.get("exergoeconomic_f_factor", 0.5)
    r = result.get("exergoeconomic_r_factor", 0.5)
    Z_dot = result.get("exergoeconomic_Z_dot_eur_h", 0)
    C_dot_D = result.get("exergoeconomic_C_dot_destruction_eur_h", 0)
    avoidable_ratio_pct = result.get("avoidable_ratio_pct", 0)
    if avoidable_ratio_pct is None:
        avoidable_ratio_pct = 0
    avoidable_ratio = avoidable_ratio_pct / 100.0

    C_total_dot = Z_dot + C_dot_D

    # Determine strategy
    strategy, label, priority = _determine_strategy(f, r, avoidable_ratio)

    # Equipment-type-specific actions
    actions = _get_equipment_actions(eq_type, strategy)

    # Savings potential
    C_savings_h = C_dot_D * avoidable_ratio
    C_savings_annual = C_savings_h * operating_hours

    # Investment estimate
    capacity = result.get("exergy_in_kW", 100)
    investment = _estimate_investment(eq_type, strategy, capacity)

    # Payback
    if C_savings_annual > 0:
        payback = investment / C_savings_annual
        payback = min(payback, 99.9)
    else:
        payback = 99.9

    return OptimizationRecommendation(
        equipment_id=eq_id,
        equipment_name=eq_name,
        equipment_type=eq_type,
        subtype=subtype,
        f_factor=f,
        r_factor=r,
        Z_dot_eur_h=Z_dot,
        C_dot_D_eur_h=C_dot_D,
        C_total_dot_eur_h=C_total_dot,
        avoidable_ratio=avoidable_ratio,
        strategy=strategy,
        strategy_label=label,
        priority=priority,
        recommended_actions=actions,
        C_savings_potential_eur_h=C_savings_h,
        C_savings_annual_eur=C_savings_annual,
        estimated_investment_eur=investment,
        simple_payback_years=payback,
    )


def _calculate_factory_metrics(
    recommendations: List[OptimizationRecommendation],
    operating_hours: int,
) -> dict:
    """Calculate factory-level thermoeconomic metrics.

    Returns dict with keys matching ThermoeconomicOptimizationResult fields.
    """
    total_Z = sum(r.Z_dot_eur_h for r in recommendations)
    total_CD = sum(r.C_dot_D_eur_h for r in recommendations)
    total_C = total_Z + total_CD
    total_savings_h = sum(r.C_savings_potential_eur_h for r in recommendations)
    total_savings_yr = sum(r.C_savings_annual_eur for r in recommendations)
    total_invest = sum(r.estimated_investment_eur for r in recommendations)

    factory_f = total_Z / total_C if total_C > 0 else 0.5
    if total_savings_yr > 0:
        factory_payback = total_invest / total_savings_yr
        factory_payback = min(factory_payback, 99.9)
    else:
        factory_payback = 99.9

    # Distributions
    strategy_dist: Dict[str, int] = {}
    priority_dist: Dict[str, int] = {}
    for r in recommendations:
        strategy_dist[r.strategy] = strategy_dist.get(r.strategy, 0) + 1
        priority_dist[r.priority] = priority_dist.get(r.priority, 0) + 1

    return {
        "total_Z_dot_eur_h": total_Z,
        "total_C_dot_D_eur_h": total_CD,
        "total_C_total_dot_eur_h": total_C,
        "factory_f_factor": factory_f,
        "total_savings_potential_eur_h": total_savings_h,
        "total_savings_annual_eur": total_savings_yr,
        "total_estimated_investment_eur": total_invest,
        "factory_payback_years": factory_payback,
        "strategy_distribution": strategy_dist,
        "priority_distribution": priority_dist,
    }


def _create_cost_benefit_ranking(
    recommendations: List[OptimizationRecommendation],
) -> List[dict]:
    """Create ROI-based ranking (shortest payback first, maintain excluded)."""
    actionable = [r for r in recommendations if r.strategy != "maintain"]
    ranked = sorted(actionable, key=lambda r: r.simple_payback_years)
    return [
        {
            "equipment_id": r.equipment_id,
            "equipment_name": r.equipment_name,
            "strategy": r.strategy,
            "strategy_label": r.strategy_label,
            "C_savings_annual_eur": round(r.C_savings_annual_eur, 2),
            "estimated_investment_eur": round(r.estimated_investment_eur, 2),
            "simple_payback_years": round(r.simple_payback_years, 1),
            "priority": r.priority,
        }
        for r in ranked
    ]


def _generate_f_r_scatter(
    recommendations: List[OptimizationRecommendation],
) -> dict:
    """Generate f-factor vs r-factor scatter plot data.

    Bubble size proportional to annual savings potential.
    Includes zone definitions for frontend rendering.
    """
    return {
        "equipment_names": [r.equipment_name for r in recommendations],
        "f_factors": [round(r.f_factor, 3) for r in recommendations],
        "r_factors": [round(r.r_factor, 3) for r in recommendations],
        "strategies": [r.strategy for r in recommendations],
        "colors": [STRATEGY_COLORS.get(r.strategy, "#9ca3af") for r in recommendations],
        "sizes": [max(8, min(30, r.C_savings_annual_eur / 1000)) for r in recommendations],
        # Decision zone definitions (for frontend shapes)
        "zones": {
            "invest": {"f_range": [0, 0.25], "r_range": [0.5, 2.0], "label": "Verim artir"},
            "downsize": {"f_range": [0.65, 1.0], "r_range": [0, 0.5], "label": "Maliyet azalt"},
            "structural": {"f_range": [0.65, 1.0], "r_range": [0.5, 2.0], "label": "Sistem degistir"},
            "parametric": {"f_range": [0.25, 0.65], "r_range": [0, 2.0], "label": "Ince ayar"},
        },
    }


def _generate_savings_waterfall(
    recommendations: List[OptimizationRecommendation],
) -> dict:
    """Generate savings waterfall chart data (largest to smallest).

    Returns bar chart data with cumulative line overlay.
    """
    # Only items with savings > 0
    actionable = [r for r in recommendations if r.C_savings_annual_eur > 0]
    actionable.sort(key=lambda r: r.C_savings_annual_eur, reverse=True)

    names = [r.equipment_name for r in actionable]
    values = [round(r.C_savings_annual_eur, 2) for r in actionable]
    strategies = [r.strategy for r in actionable]
    colors = [STRATEGY_COLORS.get(r.strategy, "#9ca3af") for r in actionable]

    # Cumulative sum
    cumulative = []
    running = 0.0
    for v in values:
        running += v
        cumulative.append(round(running, 2))

    return {
        "equipment_names": names,
        "savings_eur": values,
        "cumulative_eur": cumulative,
        "strategies": strategies,
        "colors": colors,
        "total_savings_eur": round(sum(values), 2),
    }


def _collect_warnings(
    recommendations: List[OptimizationRecommendation],
    factory_metrics: dict,
) -> List[str]:
    """Collect factory-level thermoeconomic optimization warnings."""
    warnings = []

    # High priority equipment with high exergy destruction cost
    high_cd = [r for r in recommendations if r.C_dot_D_eur_h > 10 and r.strategy == "invest"]
    if high_cd:
        names = ", ".join(r.equipment_name for r in high_cd)
        warnings.append(
            f"Yuksek exergy yikim maliyeti (C_dot_D > 10 EUR/h): {names}"
        )

    # All maintain — no optimization potential
    all_maintain = all(r.strategy == "maintain" for r in recommendations)
    if all_maintain and recommendations:
        warnings.append(
            "Tum ekipmanlar 'surdur' stratejisinde — aktif optimizasyon potansiyeli dusuk"
        )

    # Very long factory payback
    factory_payback = factory_metrics.get("factory_payback_years", 0)
    if factory_payback > 10 and factory_payback < 99.9:
        warnings.append(
            f"Fabrika geneli geri odeme suresi uzun ({factory_payback:.1f} yil)"
        )

    # High f_factory (investment cost dominant)
    factory_f = factory_metrics.get("factory_f_factor", 0)
    if factory_f > 0.70:
        warnings.append(
            f"Fabrika f-faktor yuksek ({factory_f:.2f}) — yatirim maliyetleri baskin"
        )

    # Low f_factory (destruction cost dominant)
    if factory_f < 0.20:
        warnings.append(
            f"Fabrika f-faktor dusuk ({factory_f:.2f}) — exergy yikim maliyetleri baskin, verim artisi oncelikli"
        )

    return warnings


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def check_thermoeconomic_feasibility(
    equipment_list: list,
    analysis_results: dict,
) -> Tuple[bool, List[str]]:
    """Check if thermoeconomic optimization is feasible.

    Requirements:
    - At least 1 equipment with exergoeconomic data (f_factor present)

    Returns:
        (feasible, reasons)
    """
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid) < 1:
        return False, ["Exergoekonomik verisi olan ekipman yok"]
    return True, [f"Uygun: {len(valid)} ekipman"]


def analyze_thermoeconomic_optimization(
    equipment_list: list,
    analysis_results: dict,
    operating_hours: int = 8000,
) -> ThermoeconomicOptimizationResult:
    """Perform thermoeconomic optimization for factory equipment.

    Uses SPECO (exergoeconomic) results (f-factor, r-factor, Z_dot, C_dot_D)
    and AV/UN split (avoidable_ratio) to determine optimization strategy for
    each equipment and produce actionable recommendations with cost-benefit ranking.

    Args:
        equipment_list: List of equipment items (dicts or objects with
            id, name, equipment_type, subtype fields)
        analysis_results: Dict mapping equipment_id -> analysis result dict
            (must have exergoeconomic_f_factor, exergoeconomic_r_factor, etc.)
        operating_hours: Annual operating hours (default 8000)

    Returns:
        ThermoeconomicOptimizationResult
    """
    # 1. Filter valid equipment (with exergoeconomic data)
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid) < 1:
        return ThermoeconomicOptimizationResult(
            is_valid=False,
            error_message="Exergoekonomik verisi olan ekipman yok",
        )

    # 2. Generate recommendation for each equipment
    recommendations = []
    for item in valid:
        eq_id = _get_item_field(item, "id")
        result = analysis_results[eq_id]
        rec = _generate_recommendation(item, result, operating_hours)
        recommendations.append(rec)

    # 3. Sort by C_savings_annual descending
    recommendations.sort(key=lambda r: r.C_savings_annual_eur, reverse=True)

    # 4. Factory metrics
    factory_metrics = _calculate_factory_metrics(recommendations, operating_hours)

    # 5. Cost-benefit ranking
    cost_benefit = _create_cost_benefit_ranking(recommendations)

    # 6. f-r scatter plot data
    f_r_data = _generate_f_r_scatter(recommendations)

    # 7. Savings waterfall data
    waterfall_data = _generate_savings_waterfall(recommendations)

    # 8. Warnings
    warnings = _collect_warnings(recommendations, factory_metrics)

    return ThermoeconomicOptimizationResult(
        num_equipment=len(recommendations),
        operating_hours=operating_hours,
        recommendations=recommendations,
        cost_benefit_ranking=cost_benefit,
        f_r_scatter_data=f_r_data,
        savings_waterfall_data=waterfall_data,
        warnings=warnings,
        **factory_metrics,
    )
