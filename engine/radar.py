"""
Radar Benchmark Chart — 6-axis score derivation for equipment analysis.

Generates normalized 0-100 scores from engine to_api_dict() output,
computing an overall grade (A-F) for each equipment analysis.
"""

from typing import Any, Dict, List, Optional

# 6-axis definitions: key, Turkish label, English label
RADAR_AXES: List[Dict[str, str]] = [
    {"key": "exergy_efficiency", "label": "Exergy Verimi", "label_en": "Exergy Efficiency"},
    {"key": "improvement_status", "label": "İyileştirme Durumu", "label_en": "Improvement Status"},
    {"key": "sector_ranking", "label": "Sektör Sıralaması", "label_en": "Sector Ranking"},
    {"key": "heat_recovery", "label": "Isı Geri Kazanım", "label_en": "Heat Recovery"},
    {"key": "destruction_ratio", "label": "Yıkım Oranı", "label_en": "Destruction Ratio"},
    {"key": "cost_efficiency", "label": "Maliyet Verimliliği", "label_en": "Cost Efficiency"},
]

# Grade thresholds and labels
_GRADES = [
    (85, "A", "Mükemmel", "Excellent"),
    (70, "B", "İyi", "Good"),
    (50, "C", "Ortalama", "Average"),
    (30, "D", "Düşük", "Below Average"),
    (0,  "F", "Kritik", "Critical"),
]

# Benchmark string -> score mapping
_BENCHMARK_SCORE_MAP = {
    "excellent": 90,
    "good": 75,
    "average": 55,
    "below_average": 35,
    "poor": 15,
}


def _clamp(value: float, lo: float = 0.0, hi: float = 100.0) -> float:
    """Clamp a numeric value between lo and hi."""
    return max(lo, min(hi, value))


def _benchmark_to_score(comparison: Optional[str]) -> float:
    """Map a benchmark_comparison string to a 0-100 score."""
    if not comparison:
        return 50.0
    return _BENCHMARK_SCORE_MAP.get(comparison.lower().strip(), 50.0)


def _compute_heat_recovery_score(api_dict: Dict[str, Any]) -> float:
    """Compute heat recovery score using equipment-specific cascade."""
    destroyed = api_dict.get("exergy_destroyed_kW") or 0

    # 1. Compressor: heat_recovery_potential_kW / destroyed
    hrp = api_dict.get("heat_recovery_potential_kW")
    if hrp is not None and destroyed > 0:
        return _clamp(hrp / destroyed * 100)

    # 2. Dryer / Steam turbine: exhaust_exergy_kW / destroyed
    exhaust = api_dict.get("exhaust_exergy_kW")
    if exhaust is not None and destroyed > 0:
        return _clamp(exhaust / destroyed * 100)

    # 3. Boiler: flue_gas_loss_kW / destroyed
    flue = api_dict.get("flue_gas_loss_kW")
    if flue is not None and destroyed > 0:
        return _clamp(flue / destroyed * 100)

    # 4. Chiller: condenser_loss_kW / destroyed
    condenser = api_dict.get("condenser_loss_kW")
    if condenser is not None and destroyed > 0:
        return _clamp(condenser / destroyed * 100)

    # 5. Heat exchanger: effectiveness (HX IS the recovery device)
    eff = api_dict.get("effectiveness")
    if eff is not None:
        return _clamp(eff * 100)

    # 6. Default (pump — minimal thermal recovery)
    return 30.0


def generate_radar_data(api_dict: Dict[str, Any], operating_hours: int = 6000) -> Dict[str, Any]:
    """Generate 6-axis radar benchmark data from an engine api_dict.

    Args:
        api_dict: Output of ``result.to_api_dict(subtype)``.
        operating_hours: Annual operating hours (default 6000).

    Returns:
        Dictionary with keys: axes, scores, overall_score, grade, grade_letter, grade_en.
    """
    # --- Axis 1: Exergy Efficiency ---
    exergy_eff = _clamp(api_dict.get("exergy_efficiency_pct") or 0)

    # --- Axis 2: Improvement Status (lower avoidable = better) ---
    avoidable = api_dict.get("avoidable_ratio_pct")
    if avoidable is not None:
        improvement = _clamp(100 - avoidable)
    else:
        improvement = 50.0

    # --- Axis 3: Sector Ranking ---
    percentile = api_dict.get("benchmark_percentile")
    if percentile is not None:
        sector = _clamp(float(percentile))
    else:
        sector = _benchmark_to_score(api_dict.get("benchmark_comparison"))

    # --- Axis 4: Heat Recovery ---
    heat_rec = _compute_heat_recovery_score(api_dict)

    # --- Axis 5: Destruction Ratio (lower destruction = better) ---
    ex_input = api_dict.get("exergy_input_kW") or 0
    ex_destroyed = api_dict.get("exergy_destroyed_kW") or 0
    if ex_input > 0:
        destruction = _clamp(100 - (ex_destroyed / ex_input) * 100)
    else:
        destruction = 0.0

    # --- Axis 6: Cost Efficiency ---
    annual_loss = api_dict.get("annual_loss_kWh") or 0
    if ex_input > 0 and operating_hours > 0:
        loss_ratio = annual_loss / (ex_input * operating_hours)
        cost_eff = _clamp((1 - loss_ratio) * 100)
    else:
        cost_eff = 0.0

    scores = {
        "exergy_efficiency": round(exergy_eff, 1),
        "improvement_status": round(improvement, 1),
        "sector_ranking": round(sector, 1),
        "heat_recovery": round(heat_rec, 1),
        "destruction_ratio": round(destruction, 1),
        "cost_efficiency": round(cost_eff, 1),
    }

    overall = round(sum(scores.values()) / len(scores), 1)

    # Grade
    grade_letter = "F"
    grade = "Kritik"
    grade_en = "Critical"
    for threshold, letter, tr_label, en_label in _GRADES:
        if overall >= threshold:
            grade_letter = letter
            grade = tr_label
            grade_en = en_label
            break

    return {
        "axes": [dict(a) for a in RADAR_AXES],
        "scores": scores,
        "overall_score": overall,
        "grade": grade,
        "grade_letter": grade_letter,
        "grade_en": grade_en,
    }
