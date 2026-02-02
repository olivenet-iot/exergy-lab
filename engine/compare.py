"""What-If scenario comparison engine.

Computes deltas, savings, and classification between baseline and scenario analysis results.
"""

from typing import Dict, List, Tuple


# Metrics where an increase is an improvement
_HIGHER_IS_BETTER = {
    "exergy_efficiency_pct",
    "exergy_output_kW",
    "avoidable_ratio_pct",
}

# Metrics where a decrease is an improvement
_LOWER_IS_BETTER = {
    "exergy_input_kW",
    "exergy_destroyed_kW",
    "exergy_destroyed_avoidable_kW",
    "exergy_destroyed_unavoidable_kW",
    "annual_loss_kWh",
    "annual_loss_EUR",
}

# All tracked metrics
_TRACKED_METRICS = _HIGHER_IS_BETTER | _LOWER_IS_BETTER


def compute_comparison(
    baseline_dict: dict,
    scenario_dict: dict,
    energy_price_eur_kwh: float = 0.10,
    operating_hours: float = 6000,
) -> dict:
    """Compare baseline vs scenario analysis results.

    Args:
        baseline_dict: Flat dict of baseline analysis metrics.
        scenario_dict: Flat dict of scenario analysis metrics.
        energy_price_eur_kwh: Energy price for savings calculation.
        operating_hours: Annual operating hours.

    Returns:
        Dict with delta, delta_pct, savings, improved/degraded lists, and Turkish summary.
    """
    delta: Dict[str, float] = {}
    delta_pct: Dict[str, float] = {}
    improved: List[str] = []
    degraded: List[str] = []

    for metric in _TRACKED_METRICS:
        b_val = baseline_dict.get(metric)
        s_val = scenario_dict.get(metric)

        if b_val is None or s_val is None:
            continue

        try:
            b_val = float(b_val)
            s_val = float(s_val)
        except (TypeError, ValueError):
            continue

        d = s_val - b_val
        delta[metric] = round(d, 4)

        if abs(b_val) > 1e-12:
            delta_pct[metric] = round((d / abs(b_val)) * 100, 2)
        else:
            delta_pct[metric] = 0.0

        # Classify
        if abs(d) < 1e-12:
            continue
        if metric in _HIGHER_IS_BETTER:
            if d > 0:
                improved.append(metric)
            else:
                degraded.append(metric)
        elif metric in _LOWER_IS_BETTER:
            if d < 0:
                improved.append(metric)
            else:
                degraded.append(metric)

    # Savings calculation
    b_destroyed = float(baseline_dict.get("exergy_destroyed_kW", 0) or 0)
    s_destroyed = float(scenario_dict.get("exergy_destroyed_kW", 0) or 0)
    exergy_saved_kW = max(b_destroyed - s_destroyed, 0)
    annual_savings_kWh = round(exergy_saved_kW * operating_hours, 2)
    annual_savings_EUR = round(annual_savings_kWh * energy_price_eur_kwh, 2)

    b_eff = float(baseline_dict.get("exergy_efficiency_pct", 0) or 0)
    s_eff = float(scenario_dict.get("exergy_efficiency_pct", 0) or 0)
    efficiency_improvement_pct = round(s_eff - b_eff, 2)

    b_avoidable = float(baseline_dict.get("exergy_destroyed_avoidable_kW", 0) or 0)
    s_avoidable = float(scenario_dict.get("exergy_destroyed_avoidable_kW", 0) or 0)
    avoidable_reduction_kW = round(max(b_avoidable - s_avoidable, 0), 4)

    savings = {
        "exergy_saved_kW": round(exergy_saved_kW, 4),
        "annual_savings_kWh": annual_savings_kWh,
        "annual_savings_EUR": annual_savings_EUR,
        "efficiency_improvement_pct": efficiency_improvement_pct,
        "avoidable_reduction_kW": avoidable_reduction_kW,
    }

    # Turkish summary
    summary_tr = _build_summary_tr(
        efficiency_improvement_pct, exergy_saved_kW,
        annual_savings_kWh, annual_savings_EUR,
        len(improved), len(degraded),
    )

    return {
        "delta": delta,
        "delta_pct": delta_pct,
        "savings": savings,
        "improved_metrics": improved,
        "degraded_metrics": degraded,
        "summary_tr": summary_tr,
    }


def _build_summary_tr(
    eff_improvement: float,
    saved_kW: float,
    saved_kWh: float,
    saved_EUR: float,
    n_improved: int,
    n_degraded: int,
) -> str:
    """Build a Turkish summary string for the comparison."""
    parts = []

    if eff_improvement > 0:
        parts.append(f"Exergy verimi %{eff_improvement:.1f} artti.")
    elif eff_improvement < 0:
        parts.append(f"Exergy verimi %{abs(eff_improvement):.1f} azaldi.")
    else:
        parts.append("Exergy veriminde degisiklik yok.")

    if saved_kW > 0:
        parts.append(
            f"Yillik {saved_kWh:,.0f} kWh ({saved_EUR:,.0f} EUR) tasarruf potansiyeli."
        )

    if n_improved > 0:
        parts.append(f"{n_improved} metrikte iyilesme.")
    if n_degraded > 0:
        parts.append(f"{n_degraded} metrikte gerileme.")

    return " ".join(parts)
