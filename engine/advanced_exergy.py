"""
ExergyLab - Advanced Exergy Analysis (EN/EX Decomposition)

Tsatsaronis 4-quadrant methodology:
- Endogenous (EN): destruction caused by equipment's own inefficiency
- Exogenous (EX): destruction caused by other equipment interactions
- Combined with AV/UN split: AV-EN, AV-EX, UN-EN, UN-EX quadrants

Reference: Tsatsaronis & Park, "On avoidable and unavoidable exergy
destructions and investment costs in thermal systems", Energy Conversion
and Management, 2002.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Base isolation factors per equipment type (φ₀)
# Higher = more endogenous (less affected by other equipment)
BASE_ISOLATION_FACTORS = {
    "compressor": 0.75,
    "boiler": 0.80,
    "chiller": 0.65,
    "pump": 0.85,
    "heat_exchanger": 0.55,
    "steam_turbine": 0.70,
    "dryer": 0.60,
}

# Interaction coefficients (α): how much equipment type A affects type B
# Key: (affected_type, source_type) → coefficient
# Only non-zero entries are stored (sparse)
INTERACTION_COEFFICIENTS = {
    # compressor affected by:
    ("compressor", "boiler"): 0.05,
    ("compressor", "heat_exchanger"): 0.08,
    # boiler affected by:
    ("boiler", "heat_exchanger"): 0.10,
    ("boiler", "steam_turbine"): 0.08,
    ("boiler", "dryer"): 0.06,
    # chiller affected by:
    ("chiller", "compressor"): 0.10,
    ("chiller", "boiler"): 0.08,
    ("chiller", "heat_exchanger"): 0.12,
    # pump affected by:
    ("pump", "boiler"): 0.05,
    ("pump", "heat_exchanger"): 0.06,
    # heat_exchanger affected by:
    ("heat_exchanger", "boiler"): 0.15,
    ("heat_exchanger", "compressor"): 0.08,
    ("heat_exchanger", "steam_turbine"): 0.10,
    ("heat_exchanger", "dryer"): 0.07,
    # steam_turbine affected by:
    ("steam_turbine", "boiler"): 0.20,
    ("steam_turbine", "heat_exchanger"): 0.10,
    ("steam_turbine", "pump"): 0.05,
    # dryer affected by:
    ("dryer", "boiler"): 0.12,
    ("dryer", "heat_exchanger"): 0.10,
    ("dryer", "steam_turbine"): 0.08,
}

# Reference exergy efficiencies (best-practice) per equipment type/subtype
# Used to calculate efficiency deviations (δ)
REFERENCE_EFFICIENCIES = {
    "compressor": {
        "_default": 0.80,
        "screw": 0.80,
        "piston": 0.78,
        "centrifugal": 0.85,
        "scroll": 0.76,
    },
    "boiler": {
        "_default": 0.82,
        "steam_firetube": 0.82,
        "steam_watertube": 0.85,
        "hotwater": 0.78,
        "condensing": 0.95,
        "waste_heat": 0.70,
        "electric": 0.90,
        "biomass": 0.72,
    },
    "chiller": {
        "_default": 0.40,
        "screw": 0.40,
        "centrifugal": 0.45,
        "scroll": 0.38,
        "reciprocating": 0.35,
        "air_cooled": 0.35,
        "water_cooled": 0.42,
        "absorption": 0.25,
    },
    "pump": {
        "_default": 0.80,
        "centrifugal": 0.80,
        "positive_displacement": 0.75,
        "submersible": 0.70,
        "vertical_turbine": 0.78,
        "booster": 0.72,
        "vacuum": 0.65,
    },
    "heat_exchanger": {
        "_default": 0.75,
        "shell_tube": 0.75,
        "plate": 0.85,
        "air_cooled": 0.60,
        "double_pipe": 0.70,
        "spiral": 0.78,
        "economizer": 0.72,
        "recuperator": 0.74,
        "finned_tube": 0.68,
    },
    "steam_turbine": {
        "_default": 0.78,
        "back_pressure": 0.78,
        "backpressure": 0.78,
        "condensing": 0.82,
        "extraction": 0.76,
        "orc": 0.70,
        "micro_turbine": 0.65,
    },
    "dryer": {
        "_default": 0.45,
        "convective": 0.45,
        "rotary": 0.50,
        "fluidized_bed": 0.55,
        "spray": 0.42,
        "belt": 0.48,
        "heat_pump": 0.60,
        "infrared": 0.40,
        "drum": 0.46,
        "conveyor": 0.47,
        "tray": 0.44,
        "microwave": 0.38,
    },
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class AdvancedExergyEquipmentResult:
    """Per-equipment EN/EX decomposition result."""
    equipment_id: str
    equipment_name: str
    equipment_type: str
    subtype: str

    # Total exergy destruction
    I_total_kW: float

    # EN/EX decomposition
    I_EN_kW: float
    I_EX_kW: float
    isolation_factor: float  # φ

    # 4-quadrant decomposition
    I_AV_EN_kW: float
    I_AV_EX_kW: float
    I_UN_EN_kW: float
    I_UN_EX_kW: float

    # AV/UN totals
    I_AV_kW: float
    I_UN_kW: float

    # Exogenous sources
    exogenous_sources: List[dict] = field(default_factory=list)

    # Priority
    priority: str = "low"
    priority_reason: str = ""

    # Warnings
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "subtype": self.subtype,
            "I_total_kW": round(self.I_total_kW, 2),
            "I_EN_kW": round(self.I_EN_kW, 2),
            "I_EX_kW": round(self.I_EX_kW, 2),
            "isolation_factor": round(self.isolation_factor, 4),
            "I_AV_EN_kW": round(self.I_AV_EN_kW, 2),
            "I_AV_EX_kW": round(self.I_AV_EX_kW, 2),
            "I_UN_EN_kW": round(self.I_UN_EN_kW, 2),
            "I_UN_EX_kW": round(self.I_UN_EX_kW, 2),
            "I_AV_kW": round(self.I_AV_kW, 2),
            "I_UN_kW": round(self.I_UN_kW, 2),
            "exogenous_sources": self.exogenous_sources,
            "priority": self.priority,
            "priority_reason": self.priority_reason,
            "warnings": self.warnings,
        }


@dataclass
class AdvancedExergyResult:
    """Factory-level advanced exergy analysis result."""
    is_valid: bool
    equipment_results: List[AdvancedExergyEquipmentResult] = field(default_factory=list)

    # Factory-level metrics
    total_I_EN_kW: float = 0.0
    total_I_EX_kW: float = 0.0
    total_I_AV_EN_kW: float = 0.0
    total_I_AV_EX_kW: float = 0.0
    total_I_UN_EN_kW: float = 0.0
    total_I_UN_EX_kW: float = 0.0
    total_I_kW: float = 0.0

    endogenous_ratio: float = 0.0
    interaction_density: float = 0.0

    # Rankings and network
    priority_ranking: List[dict] = field(default_factory=list)
    interaction_network: List[dict] = field(default_factory=list)
    quadrant_chart_data: dict = field(default_factory=dict)

    # Most influential/affected equipment
    most_influential: str = ""
    most_affected: str = ""

    # Warnings
    warnings: List[str] = field(default_factory=list)
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "equipment_results": [r.to_dict() for r in self.equipment_results],
            "total_I_EN_kW": round(self.total_I_EN_kW, 2),
            "total_I_EX_kW": round(self.total_I_EX_kW, 2),
            "total_I_AV_EN_kW": round(self.total_I_AV_EN_kW, 2),
            "total_I_AV_EX_kW": round(self.total_I_AV_EX_kW, 2),
            "total_I_UN_EN_kW": round(self.total_I_UN_EN_kW, 2),
            "total_I_UN_EX_kW": round(self.total_I_UN_EX_kW, 2),
            "total_I_kW": round(self.total_I_kW, 2),
            "endogenous_ratio": round(self.endogenous_ratio, 4),
            "interaction_density": round(self.interaction_density, 4),
            "priority_ranking": self.priority_ranking,
            "interaction_network": self.interaction_network,
            "quadrant_chart_data": self.quadrant_chart_data,
            "most_influential": self.most_influential,
            "most_affected": self.most_affected,
            "warnings": self.warnings,
            "error": self.error,
        }


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _filter_valid_equipment(
    equipment_list: list,
    analysis_results: dict,
) -> list:
    """Keep only equipment with positive exergy destruction."""
    valid = []
    for item in equipment_list:
        eq_id = item["id"] if isinstance(item, dict) else item.id
        result = analysis_results.get(eq_id)
        if result and result.get("exergy_destroyed_kW", 0) > 0:
            valid.append(item)
    return valid


def _get_factory_equipment_types(equipment_list: list) -> dict:
    """Group equipment IDs by equipment type.

    Returns:
        dict: {equipment_type: [id1, id2, ...]}
    """
    types = {}
    for item in equipment_list:
        eq_id = item["id"] if isinstance(item, dict) else item.id
        eq_type = item["equipment_type"] if isinstance(item, dict) else item.equipment_type
        types.setdefault(eq_type, []).append(eq_id)
    return types


def _get_item_field(item, field_name: str):
    """Get a field from an item (dict or object)."""
    if isinstance(item, dict):
        return item.get(field_name, "")
    return getattr(item, field_name, "")


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def _calculate_efficiency_deviations(
    equipment_list: list,
    analysis_results: dict,
) -> dict:
    """Calculate efficiency deviations from reference values.

    δ = (η_ref - η_actual) / η_ref
    Positive δ means underperforming (below reference).
    Clamped to [-0.5, 1.0].

    Returns:
        dict: {equipment_id: deviation_value}
    """
    deviations = {}
    for item in equipment_list:
        eq_id = _get_item_field(item, "id")
        eq_type = _get_item_field(item, "equipment_type")
        subtype = _get_item_field(item, "subtype")

        result = analysis_results.get(eq_id, {})
        actual_eff = result.get("exergy_efficiency_pct", 0) / 100.0

        # Look up reference efficiency
        type_refs = REFERENCE_EFFICIENCIES.get(eq_type, {})
        ref_eff = type_refs.get(subtype, type_refs.get("_default", 0.50))

        if ref_eff > 0:
            delta = (ref_eff - actual_eff) / ref_eff
        else:
            delta = 0.0

        # Clamp to [-0.5, 1.0]
        delta = max(-0.5, min(1.0, delta))
        deviations[eq_id] = delta

    return deviations


def _calculate_isolation_factors(
    equipment_list: list,
    analysis_results: dict,
    factory_types: dict,
    deviations: dict,
) -> dict:
    """Calculate isolation factors for each equipment.

    φ = φ₀ × (1 - Σ α_ij × δ_j)
    Only positive δ (underperforming) neighbors reduce isolation.
    Self is excluded from the sum.
    Clamped to [0.20, 0.95].

    Returns:
        dict: {equipment_id: isolation_factor}
    """
    isolation_factors = {}

    for item in equipment_list:
        eq_id = _get_item_field(item, "id")
        eq_type = _get_item_field(item, "equipment_type")

        phi_0 = BASE_ISOLATION_FACTORS.get(eq_type, 0.70)

        # Sum interaction effects from other equipment
        interaction_sum = 0.0
        for other_item in equipment_list:
            other_id = _get_item_field(other_item, "id")
            if other_id == eq_id:
                continue  # Skip self

            other_type = _get_item_field(other_item, "equipment_type")
            other_delta = deviations.get(other_id, 0.0)

            # Only positive δ (underperforming) contributes
            if other_delta <= 0:
                continue

            alpha = INTERACTION_COEFFICIENTS.get((eq_type, other_type), 0.0)
            interaction_sum += alpha * other_delta

        phi = phi_0 * (1 - interaction_sum)

        # Clamp to [0.20, 0.95]
        phi = max(0.20, min(0.95, phi))
        isolation_factors[eq_id] = phi

    return isolation_factors


def _analyze_single_equipment(
    item: dict,
    result: dict,
    isolation_factor: float,
    all_equipment: list,
    deviations: dict,
) -> AdvancedExergyEquipmentResult:
    """Perform EN/EX and 4-quadrant decomposition for a single equipment.

    EN/EX split:
        I_EN = I_total × φ
        I_EX = I_total - I_EN

    4-quadrant via φ on AV/UN:
        I_AV_EN = I_AV × φ
        I_AV_EX = I_AV - I_AV_EN
        I_UN_EN = I_UN × φ
        I_UN_EX = I_UN - I_UN_EN
    """
    eq_id = _get_item_field(item, "id")
    eq_name = _get_item_field(item, "name")
    eq_type = _get_item_field(item, "equipment_type")
    subtype = _get_item_field(item, "subtype")

    I_total = result.get("exergy_destroyed_kW", 0)

    # EN/EX decomposition
    I_EN = I_total * isolation_factor
    I_EX = I_total - I_EN

    # AV/UN split (may not be present)
    I_AV = result.get("exergy_destroyed_avoidable_kW", 0) or 0
    I_UN = result.get("exergy_destroyed_unavoidable_kW", 0) or 0

    warnings = []

    # If AV/UN not available, default: all is unavoidable
    if I_AV == 0 and I_UN == 0 and I_total > 0:
        I_UN = I_total
        warnings.append(f"{eq_name}: AV/UN split not available, assuming all unavoidable")

    # 4-quadrant decomposition
    I_AV_EN = I_AV * isolation_factor
    I_AV_EX = I_AV - I_AV_EN
    I_UN_EN = I_UN * isolation_factor
    I_UN_EX = I_UN - I_UN_EN

    # Ensure non-negative
    I_AV_EN = max(0, I_AV_EN)
    I_AV_EX = max(0, I_AV_EX)
    I_UN_EN = max(0, I_UN_EN)
    I_UN_EX = max(0, I_UN_EX)

    # Identify exogenous sources
    exogenous_sources = _identify_exogenous_sources(
        item, I_EX, all_equipment, deviations
    )

    # Determine priority
    priority, reason = _determine_priority(
        I_AV_EN, I_AV_EX, I_total, isolation_factor
    )

    return AdvancedExergyEquipmentResult(
        equipment_id=eq_id,
        equipment_name=eq_name,
        equipment_type=eq_type,
        subtype=subtype,
        I_total_kW=I_total,
        I_EN_kW=I_EN,
        I_EX_kW=I_EX,
        isolation_factor=isolation_factor,
        I_AV_EN_kW=I_AV_EN,
        I_AV_EX_kW=I_AV_EX,
        I_UN_EN_kW=I_UN_EN,
        I_UN_EX_kW=I_UN_EX,
        I_AV_kW=I_AV,
        I_UN_kW=I_UN,
        exogenous_sources=exogenous_sources,
        priority=priority,
        priority_reason=reason,
        warnings=warnings,
    )


def _identify_exogenous_sources(
    item,
    I_EX_total: float,
    all_equipment: list,
    deviations: dict,
) -> List[dict]:
    """Identify which equipment contributes to exogenous destruction.

    Uses interaction coefficients and deviations to weight contributions.
    Normalized to sum to I_EX_total kW.

    Returns:
        list of {source_id, source_name, source_type, value_kW, share_pct}
        sorted descending by value_kW
    """
    eq_id = _get_item_field(item, "id")
    eq_type = _get_item_field(item, "equipment_type")

    if I_EX_total <= 0:
        return []

    raw_contributions = []
    total_weight = 0.0

    for other in all_equipment:
        other_id = _get_item_field(other, "id")
        if other_id == eq_id:
            continue  # Skip self

        other_type = _get_item_field(other, "equipment_type")
        other_delta = deviations.get(other_id, 0.0)

        if other_delta <= 0:
            continue  # Only underperforming equipment contributes

        alpha = INTERACTION_COEFFICIENTS.get((eq_type, other_type), 0.0)
        weight = alpha * other_delta

        if weight > 0:
            raw_contributions.append({
                "source_id": other_id,
                "source_name": _get_item_field(other, "name"),
                "source_type": other_type,
                "weight": weight,
            })
            total_weight += weight

    if total_weight == 0:
        return []

    # Normalize to kW
    sources = []
    for contrib in raw_contributions:
        value_kW = I_EX_total * (contrib["weight"] / total_weight)
        if value_kW >= 0.01:  # Skip negligible
            sources.append({
                "source_id": contrib["source_id"],
                "source_name": contrib["source_name"],
                "source_type": contrib["source_type"],
                "value_kW": round(value_kW, 2),
                "share_pct": round(value_kW / I_EX_total * 100, 1),
            })

    # Sort descending
    sources.sort(key=lambda x: x["value_kW"], reverse=True)
    return sources


def _determine_priority(
    I_AV_EN: float,
    I_AV_EX: float,
    I_total: float,
    isolation_factor: float,
) -> Tuple[str, str]:
    """Determine improvement priority based on AV-EN ratio.

    Thresholds:
    - high: AV-EN/I_total > 0.30
    - medium: AV-EN/I_total > 0.15
    - low: otherwise

    Returns:
        (priority_level, reason_text)
    """
    if I_total <= 0:
        return "low", "No exergy destruction"

    av_en_ratio = I_AV_EN / I_total

    if av_en_ratio > 0.30:
        return "high", f"AV-EN ratio {av_en_ratio:.1%} - high improvement potential through own optimization"
    elif av_en_ratio > 0.15:
        return "medium", f"AV-EN ratio {av_en_ratio:.1%} - moderate improvement potential"
    else:
        if isolation_factor < 0.40:
            return "medium", f"Low AV-EN but high interaction (phi={isolation_factor:.2f}) - system-level optimization needed"
        return "low", f"AV-EN ratio {av_en_ratio:.1%} - limited direct improvement potential"


# ---------------------------------------------------------------------------
# Factory-level aggregation functions
# ---------------------------------------------------------------------------

def _calculate_factory_metrics(
    equipment_results: List[AdvancedExergyEquipmentResult],
) -> dict:
    """Calculate factory-level EN/EX totals and ratios.

    Returns:
        dict with total_EN, total_EX, total_AV_EN, etc.
    """
    total_EN = sum(r.I_EN_kW for r in equipment_results)
    total_EX = sum(r.I_EX_kW for r in equipment_results)
    total_AV_EN = sum(r.I_AV_EN_kW for r in equipment_results)
    total_AV_EX = sum(r.I_AV_EX_kW for r in equipment_results)
    total_UN_EN = sum(r.I_UN_EN_kW for r in equipment_results)
    total_UN_EX = sum(r.I_UN_EX_kW for r in equipment_results)
    total_I = sum(r.I_total_kW for r in equipment_results)

    endogenous_ratio = total_EN / total_I if total_I > 0 else 0.0

    # Interaction density: fraction of equipment with significant EX
    n = len(equipment_results)
    if n > 0:
        significant_ex_count = sum(
            1 for r in equipment_results
            if r.I_EX_kW > 0.05 * r.I_total_kW  # >5% exogenous
        )
        interaction_density = significant_ex_count / n
    else:
        interaction_density = 0.0

    # Most influential: equipment that appears most as exogenous source
    influence_count = {}
    for r in equipment_results:
        for src in r.exogenous_sources:
            sid = src["source_id"]
            influence_count[sid] = influence_count.get(sid, 0) + src["value_kW"]

    most_influential = ""
    if influence_count:
        most_influential_id = max(influence_count, key=influence_count.get)
        for r in equipment_results:
            if r.equipment_id == most_influential_id:
                most_influential = r.equipment_name
                break

    # Most affected: equipment with highest EX ratio
    most_affected = ""
    max_ex_ratio = 0.0
    for r in equipment_results:
        if r.I_total_kW > 0:
            ex_ratio = r.I_EX_kW / r.I_total_kW
            if ex_ratio > max_ex_ratio:
                max_ex_ratio = ex_ratio
                most_affected = r.equipment_name

    return {
        "total_EN": total_EN,
        "total_EX": total_EX,
        "total_AV_EN": total_AV_EN,
        "total_AV_EX": total_AV_EX,
        "total_UN_EN": total_UN_EN,
        "total_UN_EX": total_UN_EX,
        "total_I": total_I,
        "endogenous_ratio": endogenous_ratio,
        "interaction_density": interaction_density,
        "most_influential": most_influential,
        "most_affected": most_affected,
    }


def _create_priority_ranking(
    equipment_results: List[AdvancedExergyEquipmentResult],
) -> List[dict]:
    """Create priority ranking sorted by AV-EN descending.

    Returns:
        list of dicts with ranking info
    """
    ranked = sorted(equipment_results, key=lambda r: r.I_AV_EN_kW, reverse=True)
    return [
        {
            "rank": i + 1,
            "equipment_id": r.equipment_id,
            "equipment_name": r.equipment_name,
            "equipment_type": r.equipment_type,
            "I_AV_EN_kW": round(r.I_AV_EN_kW, 2),
            "I_total_kW": round(r.I_total_kW, 2),
            "isolation_factor": round(r.isolation_factor, 4),
            "priority": r.priority,
            "priority_reason": r.priority_reason,
        }
        for i, r in enumerate(ranked)
    ]


def _build_interaction_network(
    equipment_results: List[AdvancedExergyEquipmentResult],
    equipment_list: list,
    deviations: dict,
) -> List[dict]:
    """Build interaction network edges for visualization.

    Returns:
        list of {source, target, value_kW} dicts, min 1 kW, sorted desc
    """
    edges = []
    seen = set()

    for r in equipment_results:
        for src in r.exogenous_sources:
            key = (src["source_id"], r.equipment_id)
            if key in seen:
                continue
            seen.add(key)

            if src["value_kW"] >= 1.0:
                edges.append({
                    "source": src["source_name"],
                    "source_id": src["source_id"],
                    "target": r.equipment_name,
                    "target_id": r.equipment_id,
                    "value_kW": src["value_kW"],
                })

    edges.sort(key=lambda x: x["value_kW"], reverse=True)
    return edges


def _generate_quadrant_chart_data(
    equipment_results: List[AdvancedExergyEquipmentResult],
) -> dict:
    """Generate stacked bar chart data for 4-quadrant visualization.

    Returns:
        dict with labels and 4 data arrays, sorted by AV-EN descending
    """
    sorted_results = sorted(
        equipment_results, key=lambda r: r.I_AV_EN_kW, reverse=True
    )

    return {
        "labels": [r.equipment_name for r in sorted_results],
        "AV_EN": [round(r.I_AV_EN_kW, 2) for r in sorted_results],
        "AV_EX": [round(r.I_AV_EX_kW, 2) for r in sorted_results],
        "UN_EN": [round(r.I_UN_EN_kW, 2) for r in sorted_results],
        "UN_EX": [round(r.I_UN_EX_kW, 2) for r in sorted_results],
    }


def _collect_warnings(
    equipment_results: List[AdvancedExergyEquipmentResult],
    factory_types: dict,
) -> List[str]:
    """Collect factory-level warnings.

    Checks:
    - Single equipment type (limited interaction analysis)
    - Low total destruction
    - High exogenous ratio (system-level issues)
    """
    warnings = []

    # Collect equipment-level warnings
    for r in equipment_results:
        warnings.extend(r.warnings)

    # Single type warning
    if len(factory_types) == 1:
        warnings.append(
            "All equipment is the same type - interaction analysis is limited"
        )

    # Low destruction warning
    total_I = sum(r.I_total_kW for r in equipment_results)
    if total_I < 20 and total_I > 0:
        warnings.append(
            f"Total exergy destruction is low ({total_I:.1f} kW) - "
            "advanced analysis may have limited value"
        )

    # High exogenous warning
    if total_I > 0:
        total_EX = sum(r.I_EX_kW for r in equipment_results)
        ex_ratio = total_EX / total_I
        if ex_ratio > 0.50:
            warnings.append(
                f"High exogenous ratio ({ex_ratio:.0%}) - "
                "strong equipment interactions suggest system-level optimization"
            )

    return warnings


# ---------------------------------------------------------------------------
# Main analysis function
# ---------------------------------------------------------------------------

def analyze_advanced_exergy(
    equipment_list: list,
    analysis_results: dict,
) -> AdvancedExergyResult:
    """Perform advanced exergy analysis (EN/EX decomposition) for a factory.

    Args:
        equipment_list: list of equipment items (dicts or EquipmentItem objects)
            Each must have: id, name, equipment_type, subtype
        analysis_results: dict mapping equipment_id -> analysis result dict
            Each result must have: exergy_destroyed_kW, exergy_efficiency_pct

    Returns:
        AdvancedExergyResult with per-equipment and factory-level results
    """
    # 1. Filter valid equipment
    valid_equipment = _filter_valid_equipment(equipment_list, analysis_results)

    if len(valid_equipment) < 2:
        return AdvancedExergyResult(
            is_valid=False,
            error="Need at least 2 equipment with positive exergy destruction",
        )

    # 2. Get factory equipment types
    factory_types = _get_factory_equipment_types(valid_equipment)

    # 3. Calculate efficiency deviations
    deviations = _calculate_efficiency_deviations(valid_equipment, analysis_results)

    # 4. Calculate isolation factors
    isolation_factors = _calculate_isolation_factors(
        valid_equipment, analysis_results, factory_types, deviations
    )

    # 5. Analyze each equipment
    equipment_results = []
    for item in valid_equipment:
        eq_id = _get_item_field(item, "id")
        result = analysis_results[eq_id]
        phi = isolation_factors[eq_id]

        eq_result = _analyze_single_equipment(
            item, result, phi, valid_equipment, deviations
        )
        equipment_results.append(eq_result)

    # 6. Calculate factory metrics
    metrics = _calculate_factory_metrics(equipment_results)

    # 7. Create priority ranking
    priority_ranking = _create_priority_ranking(equipment_results)

    # 8. Build interaction network
    interaction_network = _build_interaction_network(
        equipment_results, valid_equipment, deviations
    )

    # 9. Generate quadrant chart data
    quadrant_chart_data = _generate_quadrant_chart_data(equipment_results)

    # 10. Collect warnings
    warnings = _collect_warnings(equipment_results, factory_types)

    return AdvancedExergyResult(
        is_valid=True,
        equipment_results=equipment_results,
        total_I_EN_kW=metrics["total_EN"],
        total_I_EX_kW=metrics["total_EX"],
        total_I_AV_EN_kW=metrics["total_AV_EN"],
        total_I_AV_EX_kW=metrics["total_AV_EX"],
        total_I_UN_EN_kW=metrics["total_UN_EN"],
        total_I_UN_EX_kW=metrics["total_UN_EX"],
        total_I_kW=metrics["total_I"],
        endogenous_ratio=metrics["endogenous_ratio"],
        interaction_density=metrics["interaction_density"],
        priority_ranking=priority_ranking,
        interaction_network=interaction_network,
        quadrant_chart_data=quadrant_chart_data,
        most_influential=metrics["most_influential"],
        most_affected=metrics["most_affected"],
        warnings=warnings,
    )


def check_advanced_exergy_feasibility(
    equipment_list: list,
    analysis_results: dict,
) -> Tuple[bool, str]:
    """Check if advanced exergy analysis is feasible.

    Requirements:
    - At least 2 equipment with positive exergy destruction
    - Total destruction > 10 kW

    Returns:
        (feasible: bool, reason: str)
    """
    valid = _filter_valid_equipment(equipment_list, analysis_results)

    if len(valid) < 2:
        return False, f"Need at least 2 equipment with destruction, found {len(valid)}"

    total_I = sum(
        analysis_results.get(
            _get_item_field(item, "id"), {}
        ).get("exergy_destroyed_kW", 0)
        for item in valid
    )

    if total_I < 10:
        return False, f"Total destruction {total_I:.1f} kW is below 10 kW threshold"

    return True, f"Feasible: {len(valid)} equipment, {total_I:.1f} kW total destruction"
