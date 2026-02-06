"""
ExergyLab - Entropy Generation Minimization (EGM) Motor Modulu

Bejan'in EGM metodolojisi:
  - Gouy-Stodola: I_dot = T0 x S_gen
  - Bejan sayisi (N_s): boyutsuz tersinmezlik olcusu
  - Entropi dekompozisyonu: DeltaT + DeltaP + karisma katkilari
  - Augmentation number (N_s,a): iyilestirme potansiyeli

Referanslar:
  - Bejan, A. (1996). "Entropy Generation Minimization"
  - Bejan, A. (2013). "Convection Heat Transfer", 4th ed.
  - Hesselgreaves, J.E. (2001). "Compact Heat Exchangers"
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Entropy decomposition fractions per equipment type/subtype
# (f_heat_transfer, f_pressure_drop, f_mixing), sum = 1.0
ENTROPY_DECOMPOSITION_FRACTIONS: Dict[str, Dict[str, Tuple[float, float, float]]] = {
    "compressor": {
        "screw": (0.25, 0.70, 0.05),
        "screw_oilfree": (0.20, 0.75, 0.05),
        "piston": (0.30, 0.65, 0.05),
        "scroll": (0.25, 0.70, 0.05),
        "centrifugal": (0.20, 0.75, 0.05),
        "roots": (0.30, 0.60, 0.10),
        "_default": (0.25, 0.70, 0.05),
    },
    "boiler": {
        "steam_firetube": (0.20, 0.05, 0.75),
        "steam_watertube": (0.18, 0.05, 0.77),
        "hotwater": (0.25, 0.05, 0.70),
        "condensing": (0.15, 0.05, 0.80),
        "waste_heat": (0.45, 0.05, 0.50),
        "electric": (0.90, 0.05, 0.05),
        "biomass": (0.20, 0.05, 0.75),
        "_default": (0.20, 0.05, 0.75),
    },
    "chiller": {
        "screw": (0.55, 0.30, 0.15),
        "centrifugal": (0.50, 0.35, 0.15),
        "scroll": (0.55, 0.30, 0.15),
        "reciprocating": (0.50, 0.30, 0.20),
        "absorption": (0.65, 0.10, 0.25),
        "air_cooled": (0.60, 0.25, 0.15),
        "water_cooled": (0.55, 0.30, 0.15),
        "_default": (0.55, 0.30, 0.15),
    },
    "pump": {
        "centrifugal": (0.10, 0.85, 0.05),
        "positive_displacement": (0.10, 0.85, 0.05),
        "submersible": (0.10, 0.85, 0.05),
        "vertical_turbine": (0.10, 0.85, 0.05),
        "booster": (0.10, 0.85, 0.05),
        "vacuum": (0.15, 0.80, 0.05),
        "_default": (0.10, 0.85, 0.05),
    },
    "heat_exchanger": {
        "shell_tube": (0.80, 0.15, 0.05),
        "plate": (0.85, 0.12, 0.03),
        "air_cooled": (0.75, 0.20, 0.05),
        "double_pipe": (0.80, 0.15, 0.05),
        "spiral": (0.82, 0.13, 0.05),
        "economizer": (0.78, 0.17, 0.05),
        "recuperator": (0.80, 0.15, 0.05),
        "finned_tube": (0.77, 0.18, 0.05),
        "_default": (0.80, 0.15, 0.05),
    },
    "steam_turbine": {
        "back_pressure": (0.30, 0.65, 0.05),
        "backpressure": (0.30, 0.65, 0.05),
        "condensing": (0.25, 0.70, 0.05),
        "extraction": (0.30, 0.60, 0.10),
        "orc": (0.35, 0.55, 0.10),
        "micro_turbine": (0.30, 0.60, 0.10),
        "_default": (0.30, 0.65, 0.05),
    },
    "dryer": {
        "convective": (0.40, 0.15, 0.45),
        "rotary": (0.40, 0.20, 0.40),
        "fluidized_bed": (0.35, 0.25, 0.40),
        "spray": (0.45, 0.10, 0.45),
        "belt": (0.40, 0.15, 0.45),
        "heat_pump": (0.50, 0.15, 0.35),
        "infrared": (0.55, 0.10, 0.35),
        "drum": (0.40, 0.20, 0.40),
        "_default": (0.40, 0.15, 0.45),
    },
}

# Bejan number grade boundaries
# Lower N_s = better (closer to reversible)
BEJAN_GRADES = {
    "A": (0.00, 0.15),
    "B": (0.15, 0.30),
    "C": (0.30, 0.50),
    "D": (0.50, 0.70),
    "F": (0.70, 1.01),
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class EntropyEquipmentResult:
    """Per-equipment EGM result."""
    equipment_id: str
    equipment_name: str
    equipment_type: str
    subtype: str

    # Base exergy data
    exergy_in_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_pct: float

    # Gouy-Stodola
    S_gen_kW_K: float
    T0_K: float

    # Bejan number (thermodynamic)
    N_s: float
    N_s_grade: str

    # Entropy decomposition
    S_gen_heat_transfer_kW_K: float
    S_gen_pressure_drop_kW_K: float
    S_gen_mixing_kW_K: float
    dominant_mechanism: str

    # Heat transfer Bejan number (HX only)
    Be_heat_transfer: Optional[float]

    # Augmentation number
    N_s_augmentation: float
    improvement_potential_pct: float

    # Specific entropy generation
    s_gen_per_exergy_input: float

    def to_dict(self) -> dict:
        return {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "subtype": self.subtype,
            "exergy_in_kW": round(self.exergy_in_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "S_gen_kW_K": round(self.S_gen_kW_K, 6),
            "T0_K": round(self.T0_K, 2),
            "N_s": round(self.N_s, 4),
            "N_s_grade": self.N_s_grade,
            "S_gen_heat_transfer_kW_K": round(self.S_gen_heat_transfer_kW_K, 6),
            "S_gen_pressure_drop_kW_K": round(self.S_gen_pressure_drop_kW_K, 6),
            "S_gen_mixing_kW_K": round(self.S_gen_mixing_kW_K, 6),
            "dominant_mechanism": self.dominant_mechanism,
            "Be_heat_transfer": round(self.Be_heat_transfer, 4) if self.Be_heat_transfer is not None else None,
            "N_s_augmentation": round(self.N_s_augmentation, 4),
            "improvement_potential_pct": round(self.improvement_potential_pct, 1),
            "s_gen_per_exergy_input": round(self.s_gen_per_exergy_input, 6),
        }


@dataclass
class EntropyGenerationResult:
    """Factory-level EGM result."""
    is_valid: bool = True
    error_message: str = ""

    num_equipment: int = 0
    T0_K: float = 298.15

    # Total entropy generation
    S_gen_total_kW_K: float = 0.0
    N_s_factory: float = 0.0

    # Decomposition totals
    S_gen_heat_transfer_total_kW_K: float = 0.0
    S_gen_pressure_drop_total_kW_K: float = 0.0
    S_gen_mixing_total_kW_K: float = 0.0
    dominant_mechanism_factory: str = ""

    # Decomposition percentages
    heat_transfer_pct: float = 0.0
    pressure_drop_pct: float = 0.0
    mixing_pct: float = 0.0

    # Gouy-Stodola verification
    total_exergy_destroyed_kW: float = 0.0

    # Equipment results
    equipment_results: List[EntropyEquipmentResult] = field(default_factory=list)

    # Ranking
    irreversibility_ranking: List[Dict] = field(default_factory=list)

    # Chart data
    decomposition_chart_data: Dict = field(default_factory=dict)
    bejan_number_chart_data: Dict = field(default_factory=dict)

    # Warnings
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "num_equipment": self.num_equipment,
            "T0_K": round(self.T0_K, 2),
            "S_gen_total_kW_K": round(self.S_gen_total_kW_K, 6),
            "N_s_factory": round(self.N_s_factory, 4),
            "S_gen_heat_transfer_total_kW_K": round(self.S_gen_heat_transfer_total_kW_K, 6),
            "S_gen_pressure_drop_total_kW_K": round(self.S_gen_pressure_drop_total_kW_K, 6),
            "S_gen_mixing_total_kW_K": round(self.S_gen_mixing_total_kW_K, 6),
            "dominant_mechanism_factory": self.dominant_mechanism_factory,
            "heat_transfer_pct": round(self.heat_transfer_pct, 1),
            "pressure_drop_pct": round(self.pressure_drop_pct, 1),
            "mixing_pct": round(self.mixing_pct, 1),
            "total_exergy_destroyed_kW": round(self.total_exergy_destroyed_kW, 2),
            "equipment_results": [r.to_dict() for r in self.equipment_results],
            "irreversibility_ranking": self.irreversibility_ranking,
            "decomposition_chart_data": self.decomposition_chart_data,
            "bejan_number_chart_data": self.bejan_number_chart_data,
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
    """Keep only equipment with positive exergy destruction and positive exergy input."""
    valid = []
    for item in equipment_list:
        eq_id = _get_item_field(item, "id")
        result = analysis_results.get(eq_id)
        if (
            result
            and result.get("exergy_destroyed_kW", 0) > 0
            and result.get("exergy_in_kW", 0) > 0
        ):
            valid.append(item)
    return valid


def _assign_bejan_grade(N_s: float) -> str:
    """Assign a letter grade based on Bejan number N_s."""
    for grade, (low, high) in BEJAN_GRADES.items():
        if low <= N_s < high:
            return grade
    return "F"


def _get_decomposition_fractions(
    eq_type: str, subtype: str
) -> Tuple[float, float, float]:
    """Look up decomposition fractions for equipment type/subtype."""
    type_fracs = ENTROPY_DECOMPOSITION_FRACTIONS.get(eq_type, {})
    fracs = type_fracs.get(subtype, type_fracs.get("_default"))
    if fracs is None:
        return (0.33, 0.34, 0.33)
    return fracs


def _get_dominant_mechanism(
    S_ht: float, S_dp: float, S_mix: float
) -> str:
    """Return the dominant entropy generation mechanism."""
    vals = {"heat_transfer": S_ht, "pressure_drop": S_dp, "mixing": S_mix}
    return max(vals, key=vals.get)


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def _analyze_single_equipment(
    item,
    result: dict,
    T0_K: float,
) -> EntropyEquipmentResult:
    """Perform EGM calculations for a single equipment.

    Gouy-Stodola: S_gen = I_dot / T0
    N_s = I_dot / E_x_in, clamped to [0, 1]
    Decomposition via lookup fractions
    Be (heat transfer) only for heat_exchanger
    N_s_augmentation = 1 - avoidable_ratio
    """
    eq_id = _get_item_field(item, "id")
    eq_name = _get_item_field(item, "name")
    eq_type = _get_item_field(item, "equipment_type")
    subtype = _get_item_field(item, "subtype") or "_default"

    I_dot = result.get("exergy_destroyed_kW", 0)
    E_x_in = result.get("exergy_in_kW", 0)
    eta_ex_pct = result.get("exergy_efficiency_pct", 0)

    # Gouy-Stodola
    S_gen = I_dot / T0_K

    # Bejan number
    N_s = I_dot / E_x_in if E_x_in > 0 else 0.0
    N_s = max(0.0, min(1.0, N_s))
    N_s_grade = _assign_bejan_grade(N_s)

    # Entropy decomposition
    f_ht, f_dp, f_mix = _get_decomposition_fractions(eq_type, subtype)
    S_gen_ht = S_gen * f_ht
    S_gen_dp = S_gen * f_dp
    S_gen_mix = S_gen * f_mix
    dominant = _get_dominant_mechanism(S_gen_ht, S_gen_dp, S_gen_mix)

    # Heat transfer Bejan number (only for heat_exchanger)
    Be_heat_transfer = None
    if eq_type == "heat_exchanger":
        denom = S_gen_ht + S_gen_dp
        Be_heat_transfer = S_gen_ht / denom if denom > 0 else 0.0

    # Augmentation number
    avoidable_ratio = result.get("avoidable_ratio_pct", 0)
    if avoidable_ratio is None:
        avoidable_ratio = 0
    avoidable_ratio = avoidable_ratio / 100.0
    N_s_augmentation = 1.0 - avoidable_ratio
    improvement_potential_pct = avoidable_ratio * 100.0

    # Specific entropy generation
    s_gen_per_exergy = S_gen / E_x_in if E_x_in > 0 else 0.0

    return EntropyEquipmentResult(
        equipment_id=eq_id,
        equipment_name=eq_name,
        equipment_type=eq_type,
        subtype=subtype,
        exergy_in_kW=E_x_in,
        exergy_destroyed_kW=I_dot,
        exergy_efficiency_pct=eta_ex_pct,
        S_gen_kW_K=S_gen,
        T0_K=T0_K,
        N_s=N_s,
        N_s_grade=N_s_grade,
        S_gen_heat_transfer_kW_K=S_gen_ht,
        S_gen_pressure_drop_kW_K=S_gen_dp,
        S_gen_mixing_kW_K=S_gen_mix,
        dominant_mechanism=dominant,
        Be_heat_transfer=Be_heat_transfer,
        N_s_augmentation=N_s_augmentation,
        improvement_potential_pct=improvement_potential_pct,
        s_gen_per_exergy_input=s_gen_per_exergy,
    )


# ---------------------------------------------------------------------------
# Factory-level aggregation
# ---------------------------------------------------------------------------

def _calculate_factory_metrics(
    equipment_results: List[EntropyEquipmentResult],
    T0_K: float,
) -> dict:
    """Calculate factory-level EGM totals and percentages.

    Returns dict with keys matching EntropyGenerationResult fields.
    """
    S_gen_total = sum(r.S_gen_kW_K for r in equipment_results)
    S_gen_ht_total = sum(r.S_gen_heat_transfer_kW_K for r in equipment_results)
    S_gen_dp_total = sum(r.S_gen_pressure_drop_kW_K for r in equipment_results)
    S_gen_mix_total = sum(r.S_gen_mixing_kW_K for r in equipment_results)

    total_E_x_in = sum(r.exergy_in_kW for r in equipment_results)
    N_s_factory = (S_gen_total * T0_K / total_E_x_in) if total_E_x_in > 0 else 0.0
    N_s_factory = max(0.0, min(1.0, N_s_factory))

    total_exergy_destroyed = S_gen_total * T0_K

    # Decomposition percentages
    if S_gen_total > 0:
        ht_pct = S_gen_ht_total / S_gen_total * 100
        dp_pct = S_gen_dp_total / S_gen_total * 100
        mix_pct = S_gen_mix_total / S_gen_total * 100
    else:
        ht_pct = dp_pct = mix_pct = 0.0

    dominant = _get_dominant_mechanism(S_gen_ht_total, S_gen_dp_total, S_gen_mix_total)

    return {
        "S_gen_total_kW_K": S_gen_total,
        "N_s_factory": N_s_factory,
        "S_gen_heat_transfer_total_kW_K": S_gen_ht_total,
        "S_gen_pressure_drop_total_kW_K": S_gen_dp_total,
        "S_gen_mixing_total_kW_K": S_gen_mix_total,
        "dominant_mechanism_factory": dominant,
        "heat_transfer_pct": ht_pct,
        "pressure_drop_pct": dp_pct,
        "mixing_pct": mix_pct,
        "total_exergy_destroyed_kW": total_exergy_destroyed,
    }


def _create_irreversibility_ranking(
    equipment_results: List[EntropyEquipmentResult],
) -> List[dict]:
    """Create ranking sorted by N_s descending (most irreversible first)."""
    ranked = sorted(equipment_results, key=lambda r: r.N_s, reverse=True)
    return [
        {
            "rank": i + 1,
            "equipment_id": r.equipment_id,
            "equipment_name": r.equipment_name,
            "equipment_type": r.equipment_type,
            "N_s": round(r.N_s, 4),
            "N_s_grade": r.N_s_grade,
            "S_gen_kW_K": round(r.S_gen_kW_K, 6),
            "dominant_mechanism": r.dominant_mechanism,
            "improvement_potential_pct": round(r.improvement_potential_pct, 1),
        }
        for i, r in enumerate(ranked)
    ]


def _generate_decomposition_chart(
    equipment_results: List[EntropyEquipmentResult],
) -> dict:
    """Generate stacked bar chart data for entropy decomposition.

    Returns dict with labels and 3 data arrays (heat_transfer, pressure_drop, mixing).
    """
    sorted_results = sorted(
        equipment_results, key=lambda r: r.S_gen_kW_K, reverse=True
    )
    return {
        "labels": [r.equipment_name for r in sorted_results],
        "heat_transfer": [round(r.S_gen_heat_transfer_kW_K, 6) for r in sorted_results],
        "pressure_drop": [round(r.S_gen_pressure_drop_kW_K, 6) for r in sorted_results],
        "mixing": [round(r.S_gen_mixing_kW_K, 6) for r in sorted_results],
    }


# Grade colors for Bejan number chart
_GRADE_COLORS = {
    "A": "#22c55e",
    "B": "#84cc16",
    "C": "#f59e0b",
    "D": "#ef4444",
    "F": "#991b1b",
}


def _generate_bejan_chart(
    equipment_results: List[EntropyEquipmentResult],
) -> dict:
    """Generate bar chart data for Bejan number visualization.

    Returns dict with labels, N_s values, colors, and grades.
    """
    sorted_results = sorted(
        equipment_results, key=lambda r: r.N_s, reverse=True
    )
    return {
        "labels": [r.equipment_name for r in sorted_results],
        "N_s_values": [round(r.N_s, 4) for r in sorted_results],
        "colors": [_GRADE_COLORS.get(r.N_s_grade, "#991b1b") for r in sorted_results],
        "grades": [r.N_s_grade for r in sorted_results],
    }


def _collect_warnings(
    equipment_results: List[EntropyEquipmentResult],
    factory_metrics: dict,
) -> List[str]:
    """Collect factory-level EGM warnings."""
    warnings = []

    # High N_s equipment
    high_ns = [r for r in equipment_results if r.N_s > 0.7]
    if high_ns:
        names = ", ".join(r.equipment_name for r in high_ns)
        warnings.append(
            f"Kritik tersinmezlik (N_s > 0.70): {names}"
        )

    # Low improvement potential (high N_s_augmentation means low improvement)
    low_improve = [
        r for r in equipment_results
        if r.N_s_augmentation > 0.9 and r.N_s > 0.3
    ]
    if low_improve:
        names = ", ".join(r.equipment_name for r in low_improve)
        warnings.append(
            f"Dusuk iyilestirme potansiyeli (N_s,a > 0.9): {names}"
        )

    # Single equipment type
    types = {r.equipment_type for r in equipment_results}
    if len(types) == 1:
        warnings.append(
            "Tek ekipman tipi — dekompozisyon karsilastirmasi sinirli"
        )

    # Very low total S_gen
    S_gen_total = factory_metrics.get("S_gen_total_kW_K", 0)
    if 0 < S_gen_total < 0.01:
        warnings.append(
            f"Toplam entropi uretimi cok dusuk ({S_gen_total:.6f} kW/K)"
        )

    return warnings


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def check_egm_feasibility(
    equipment_list: list,
    analysis_results: dict,
) -> Tuple[bool, List[str]]:
    """Check if EGM analysis is feasible.

    Requirements:
    - At least 1 equipment with positive exergy destruction and input

    Returns:
        (feasible, reasons)
    """
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    reasons = []

    if len(valid) < 1:
        reasons.append(f"En az 1 gecerli ekipman gerekli, bulunan: {len(valid)}")
        return False, reasons

    reasons.append(f"Uygun: {len(valid)} ekipman")
    return True, reasons


def analyze_entropy_generation(
    equipment_list: list,
    analysis_results: dict,
    T0_K: float = 298.15,
) -> EntropyGenerationResult:
    """Perform EGM analysis for factory equipment.

    Args:
        equipment_list: List of equipment items (dicts or objects with
            id, name, equipment_type, subtype fields)
        analysis_results: Dict mapping equipment_id -> analysis result dict
            (must have exergy_destroyed_kW, exergy_in_kW, exergy_efficiency_pct)
        T0_K: Dead state temperature in Kelvin (default 298.15 K = 25 C)

    Returns:
        EntropyGenerationResult
    """
    # 1. Filter valid equipment
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid) < 1:
        return EntropyGenerationResult(
            is_valid=False,
            error_message="En az 1 gecerli ekipman gerekli",
        )

    # 2. Analyze each equipment
    equipment_results = []
    for item in valid:
        eq_id = _get_item_field(item, "id")
        result = analysis_results[eq_id]
        eq_result = _analyze_single_equipment(item, result, T0_K)
        equipment_results.append(eq_result)

    # 3. Factory metrics
    factory_metrics = _calculate_factory_metrics(equipment_results, T0_K)

    # 4. Irreversibility ranking
    ranking = _create_irreversibility_ranking(equipment_results)

    # 5. Decomposition chart data
    decomp_chart = _generate_decomposition_chart(equipment_results)

    # 6. Bejan number chart data
    bejan_chart = _generate_bejan_chart(equipment_results)

    # 7. Warnings
    warnings = _collect_warnings(equipment_results, factory_metrics)

    return EntropyGenerationResult(
        is_valid=True,
        num_equipment=len(equipment_results),
        T0_K=T0_K,
        equipment_results=equipment_results,
        irreversibility_ranking=ranking,
        decomposition_chart_data=decomp_chart,
        bejan_number_chart_data=bejan_chart,
        warnings=warnings,
        **factory_metrics,
    )
