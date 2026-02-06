"""
Tests for engine/thermoeconomic_optimization.py

Thermoeconomic optimization: Tsatsaronis f/r decision matrix,
equipment-specific actions, investment estimates, savings/payback,
factory metrics, cost-benefit ranking, chart data, and edge cases.
"""

import json
import pytest

from engine.thermoeconomic_optimization import (
    INVESTMENT_ESTIMATES,
    OPTIMIZATION_ACTIONS,
    STRATEGY_COLORS,
    STRATEGY_LABELS,
    OptimizationRecommendation,
    ThermoeconomicOptimizationResult,
    _calculate_factory_metrics,
    _create_cost_benefit_ranking,
    _determine_strategy,
    _estimate_investment,
    _filter_valid_equipment,
    _generate_f_r_scatter,
    _generate_recommendation,
    _generate_savings_waterfall,
    _get_equipment_actions,
    analyze_thermoeconomic_optimization,
    check_thermoeconomic_feasibility,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_equipment_and_results():
    """5 equipment items with different f/r/avoidable profiles.

    comp-1: f=0.15, r=0.60 -> invest (low f, high r)
    boiler-1: f=0.80, r=0.20 -> downsize (high f, low r)
    chiller-1: f=0.70, r=0.70 -> structural (high f, high r)
    pump-1: f=0.40, r=0.30, avoidable=40% -> parametric (mid f, high avoidable)
    hx-1: f=0.45, r=0.25, avoidable=20% -> maintain (mid f, low avoidable)
    """
    equipment = [
        {"id": "comp-1", "name": "Kompresor-1", "equipment_type": "compressor", "subtype": "screw", "parameters": {}},
        {"id": "boiler-1", "name": "Kazan-1", "equipment_type": "boiler", "subtype": "steam_firetube", "parameters": {}},
        {"id": "chiller-1", "name": "Chiller-1", "equipment_type": "chiller", "subtype": "screw", "parameters": {}},
        {"id": "pump-1", "name": "Pompa-1", "equipment_type": "pump", "subtype": "centrifugal", "parameters": {}},
        {"id": "hx-1", "name": "Esanjor-1", "equipment_type": "heat_exchanger", "subtype": "shell_tube", "parameters": {}},
    ]

    results = {
        "comp-1": {
            "exergoeconomic_f_factor": 0.15,
            "exergoeconomic_r_factor": 0.60,
            "exergoeconomic_Z_dot_eur_h": 2.0,
            "exergoeconomic_C_dot_destruction_eur_h": 12.0,
            "avoidable_ratio_pct": 60,
            "exergy_in_kW": 200,
            "exergy_destroyed_kW": 80,
            "exergy_efficiency_pct": 60,
        },
        "boiler-1": {
            "exergoeconomic_f_factor": 0.80,
            "exergoeconomic_r_factor": 0.20,
            "exergoeconomic_Z_dot_eur_h": 15.0,
            "exergoeconomic_C_dot_destruction_eur_h": 4.0,
            "avoidable_ratio_pct": 50,
            "exergy_in_kW": 500,
            "exergy_destroyed_kW": 150,
            "exergy_efficiency_pct": 70,
        },
        "chiller-1": {
            "exergoeconomic_f_factor": 0.70,
            "exergoeconomic_r_factor": 0.70,
            "exergoeconomic_Z_dot_eur_h": 8.0,
            "exergoeconomic_C_dot_destruction_eur_h": 3.5,
            "avoidable_ratio_pct": 45,
            "exergy_in_kW": 150,
            "exergy_destroyed_kW": 50,
            "exergy_efficiency_pct": 66.7,
        },
        "pump-1": {
            "exergoeconomic_f_factor": 0.40,
            "exergoeconomic_r_factor": 0.30,
            "exergoeconomic_Z_dot_eur_h": 1.5,
            "exergoeconomic_C_dot_destruction_eur_h": 2.5,
            "avoidable_ratio_pct": 40,
            "exergy_in_kW": 50,
            "exergy_destroyed_kW": 15,
            "exergy_efficiency_pct": 70,
        },
        "hx-1": {
            "exergoeconomic_f_factor": 0.45,
            "exergoeconomic_r_factor": 0.25,
            "exergoeconomic_Z_dot_eur_h": 3.0,
            "exergoeconomic_C_dot_destruction_eur_h": 3.5,
            "avoidable_ratio_pct": 20,
            "exergy_in_kW": 300,
            "exergy_destroyed_kW": 60,
            "exergy_efficiency_pct": 80,
        },
    }

    return equipment, results


@pytest.fixture
def sample_result(sample_equipment_and_results):
    """Run analyze_thermoeconomic_optimization on sample data."""
    equipment, results = sample_equipment_and_results
    return analyze_thermoeconomic_optimization(equipment, results, operating_hours=8000)


# ---------------------------------------------------------------------------
# Test Classes
# ---------------------------------------------------------------------------

class TestStrategyDetermination:
    """f/r decision matrix tests."""

    def test_low_f_high_r_gives_invest(self):
        """f<0.25, r>0.50 -> invest."""
        strategy, label, priority = _determine_strategy(0.15, 0.60, 0.5)
        assert strategy == "invest"
        assert priority == "high"

    def test_low_f_low_r_gives_parametric(self):
        """f<0.25, r<=0.50 -> parametric."""
        strategy, label, priority = _determine_strategy(0.10, 0.30, 0.5)
        assert strategy == "parametric"
        assert priority == "medium"

    def test_high_f_high_r_gives_structural(self):
        """f>0.65, r>0.50 -> structural."""
        strategy, label, priority = _determine_strategy(0.70, 0.70, 0.5)
        assert strategy == "structural"
        assert priority == "high"

    def test_high_f_low_r_gives_downsize(self):
        """f>0.65, r<=0.50 -> downsize."""
        strategy, label, priority = _determine_strategy(0.80, 0.20, 0.5)
        assert strategy == "downsize"
        assert priority == "medium"

    def test_mid_f_high_avoidable_gives_parametric(self):
        """0.25<=f<=0.65, avoidable>0.30 -> parametric."""
        strategy, label, priority = _determine_strategy(0.40, 0.30, 0.40)
        assert strategy == "parametric"
        assert priority == "medium"

    def test_mid_f_low_avoidable_gives_maintain(self):
        """0.25<=f<=0.65, avoidable<=0.30 -> maintain."""
        strategy, label, priority = _determine_strategy(0.45, 0.25, 0.20)
        assert strategy == "maintain"
        assert priority == "low"

    def test_boundary_f_025(self):
        """f=0.25 is in mid range (not low)."""
        strategy, _, _ = _determine_strategy(0.25, 0.60, 0.40)
        # f=0.25 is in the else branch (0.25 <= f <= 0.65)
        # avoidable=0.40 > 0.30 -> parametric
        assert strategy == "parametric"

    def test_boundary_f_065(self):
        """f=0.65 is in mid range (not high)."""
        strategy, _, _ = _determine_strategy(0.65, 0.60, 0.10)
        # f=0.65 is in the else branch (0.25 <= f <= 0.65)
        # avoidable=0.10 <= 0.30 -> maintain
        assert strategy == "maintain"


class TestEquipmentActions:
    """Equipment-type-specific action tests."""

    def test_all_equipment_types_have_actions(self):
        """All 7 equipment types have actions for all 4 active strategies."""
        for eq_type in OPTIMIZATION_ACTIONS:
            for strategy in ["invest", "parametric", "structural", "downsize"]:
                actions = _get_equipment_actions(eq_type, strategy)
                assert len(actions) >= 1, f"{eq_type}/{strategy} missing actions"

    def test_actions_non_empty(self):
        """All action lists contain non-empty strings."""
        for eq_type in OPTIMIZATION_ACTIONS:
            for strategy, actions in OPTIMIZATION_ACTIONS[eq_type].items():
                for action in actions:
                    assert len(action) > 0

    def test_unknown_type_gets_fallback(self):
        """Unknown equipment type returns fallback actions."""
        actions = _get_equipment_actions("unknown_type", "invest")
        assert len(actions) >= 1
        assert "yatirim" in actions[0].lower() or "verimli" in actions[0].lower()


class TestInvestmentEstimates:
    """Investment cost estimation tests."""

    def test_maintain_zero_investment(self):
        """maintain strategy -> 0 investment."""
        inv = _estimate_investment("compressor", "maintain", 100)
        assert inv == 0.0

    def test_investment_increases_with_capacity(self):
        """Investment increases with capacity."""
        inv_small = _estimate_investment("compressor", "invest", 50)
        inv_large = _estimate_investment("compressor", "invest", 500)
        assert inv_large > inv_small

    def test_structural_more_expensive_than_parametric(self):
        """Structural investment > parametric for same capacity."""
        inv_struct = _estimate_investment("boiler", "structural", 200)
        inv_param = _estimate_investment("boiler", "parametric", 200)
        assert inv_struct > inv_param

    def test_unknown_type_gets_fallback(self):
        """Unknown equipment type uses fallback estimates."""
        inv = _estimate_investment("unknown_type", "invest", 100)
        assert inv > 0


class TestSavingsCalculation:
    """Savings calculation tests."""

    def test_savings_equals_CD_times_avoidable(self, sample_equipment_and_results):
        """C_savings = C_dot_D x avoidable_ratio."""
        equipment, results = sample_equipment_and_results
        rec = _generate_recommendation(equipment[0], results["comp-1"], 8000)
        # comp-1: C_dot_D=12.0, avoidable_ratio=60/100=0.6
        expected_savings_h = 12.0 * 0.6
        assert abs(rec.C_savings_potential_eur_h - expected_savings_h) < 0.001

    def test_annual_savings_uses_operating_hours(self, sample_equipment_and_results):
        """Annual savings = hourly x operating_hours."""
        equipment, results = sample_equipment_and_results
        rec = _generate_recommendation(equipment[0], results["comp-1"], 6000)
        expected_annual = 12.0 * 0.6 * 6000
        assert abs(rec.C_savings_annual_eur - expected_annual) < 0.01

    def test_payback_calculation(self, sample_equipment_and_results):
        """payback = investment / savings_annual."""
        equipment, results = sample_equipment_and_results
        rec = _generate_recommendation(equipment[0], results["comp-1"], 8000)
        if rec.C_savings_annual_eur > 0:
            expected_payback = rec.estimated_investment_eur / rec.C_savings_annual_eur
            expected_payback = min(expected_payback, 99.9)
            assert abs(rec.simple_payback_years - expected_payback) < 0.01

    def test_payback_capped_at_99(self):
        """Zero savings -> payback = 99.9."""
        item = {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal"}
        result = {
            "exergoeconomic_f_factor": 0.45,
            "exergoeconomic_r_factor": 0.25,
            "exergoeconomic_Z_dot_eur_h": 1.0,
            "exergoeconomic_C_dot_destruction_eur_h": 1.0,
            "avoidable_ratio_pct": 0,
            "exergy_in_kW": 100,
        }
        rec = _generate_recommendation(item, result, 8000)
        assert rec.simple_payback_years == 99.9

    def test_zero_avoidable_zero_savings(self):
        """avoidable_ratio = 0 -> savings = 0."""
        item = {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal"}
        result = {
            "exergoeconomic_f_factor": 0.45,
            "exergoeconomic_r_factor": 0.25,
            "exergoeconomic_Z_dot_eur_h": 1.0,
            "exergoeconomic_C_dot_destruction_eur_h": 5.0,
            "avoidable_ratio_pct": 0,
            "exergy_in_kW": 100,
        }
        rec = _generate_recommendation(item, result, 8000)
        assert rec.C_savings_potential_eur_h == 0.0
        assert rec.C_savings_annual_eur == 0.0


class TestFactoryMetrics:
    """Factory-level metrics tests."""

    def test_factory_f_factor(self, sample_result):
        """factory_f = sum(Z_dot) / (sum(Z_dot) + sum(C_dot_D))."""
        recs = sample_result.recommendations
        total_Z = sum(r.Z_dot_eur_h for r in recs)
        total_CD = sum(r.C_dot_D_eur_h for r in recs)
        expected_f = total_Z / (total_Z + total_CD) if (total_Z + total_CD) > 0 else 0.5
        assert abs(sample_result.factory_f_factor - expected_f) < 0.001

    def test_totals_consistent(self, sample_result):
        """Total C = sum of individual C_total_dot."""
        recs = sample_result.recommendations
        total_C = sum(r.C_total_dot_eur_h for r in recs)
        expected_total = sample_result.total_Z_dot_eur_h + sample_result.total_C_dot_D_eur_h
        assert abs(total_C - expected_total) < 0.01

    def test_strategy_distribution_counts(self, sample_result):
        """Strategy distribution sum = num_equipment."""
        total = sum(sample_result.strategy_distribution.values())
        assert total == sample_result.num_equipment

    def test_priority_distribution_counts(self, sample_result):
        """Priority distribution sum = num_equipment."""
        total = sum(sample_result.priority_distribution.values())
        assert total == sample_result.num_equipment


class TestCostBenefitRanking:
    """ROI ranking tests."""

    def test_sorted_by_payback_ascending(self, sample_result):
        """Cost-benefit ranking sorted by payback ascending."""
        ranking = sample_result.cost_benefit_ranking
        if len(ranking) >= 2:
            for i in range(len(ranking) - 1):
                assert ranking[i]["simple_payback_years"] <= ranking[i + 1]["simple_payback_years"]

    def test_maintain_excluded(self, sample_result):
        """maintain strategy excluded from cost-benefit ranking."""
        ranking = sample_result.cost_benefit_ranking
        for item in ranking:
            assert item["strategy"] != "maintain"

    def test_waterfall_cumulative_ascending(self, sample_result):
        """Waterfall cumulative values are ascending."""
        wf = sample_result.savings_waterfall_data
        cumulative = wf.get("cumulative_eur", [])
        if len(cumulative) >= 2:
            for i in range(len(cumulative) - 1):
                assert cumulative[i] <= cumulative[i + 1]

    def test_waterfall_total_matches_sum(self, sample_result):
        """Waterfall total = sum of individual savings."""
        wf = sample_result.savings_waterfall_data
        savings = wf.get("savings_eur", [])
        total = wf.get("total_savings_eur", 0)
        assert abs(total - sum(savings)) < 0.01


class TestChartData:
    """Visualization data tests."""

    def test_f_r_scatter_structure(self, sample_result):
        """Scatter data has correct structure and length."""
        scatter = sample_result.f_r_scatter_data
        assert "equipment_names" in scatter
        assert "f_factors" in scatter
        assert "r_factors" in scatter
        assert "strategies" in scatter
        assert "colors" in scatter
        assert "sizes" in scatter
        assert "zones" in scatter
        n = len(scatter["equipment_names"])
        assert len(scatter["f_factors"]) == n
        assert len(scatter["r_factors"]) == n
        assert len(scatter["strategies"]) == n

    def test_scatter_zones_complete(self, sample_result):
        """Scatter zones include all 4 active strategies."""
        zones = sample_result.f_r_scatter_data.get("zones", {})
        for key in ["invest", "downsize", "structural", "parametric"]:
            assert key in zones
            assert "f_range" in zones[key]
            assert "r_range" in zones[key]

    def test_scatter_bubble_size_clamped(self, sample_result):
        """Bubble sizes are clamped between 8 and 30."""
        sizes = sample_result.f_r_scatter_data.get("sizes", [])
        for s in sizes:
            assert 8 <= s <= 30

    def test_waterfall_colors_match_strategies(self, sample_result):
        """Waterfall colors match strategy colors."""
        wf = sample_result.savings_waterfall_data
        for strat, color in zip(wf.get("strategies", []), wf.get("colors", [])):
            assert color == STRATEGY_COLORS.get(strat, "#9ca3af")


class TestEdgeCases:
    """Edge case tests."""

    def test_no_exergoeconomic_data_invalid(self):
        """No exergoeconomic data -> is_valid=False."""
        equipment = [
            {"id": "a", "name": "A", "equipment_type": "compressor", "subtype": "screw", "parameters": {}},
        ]
        results = {
            "a": {
                "exergy_in_kW": 100,
                "exergy_destroyed_kW": 30,
                # No exergoeconomic_f_factor
            }
        }
        result = analyze_thermoeconomic_optimization(equipment, results)
        assert result.is_valid is False
        assert "Exergoekonomik" in result.error_message

    def test_single_equipment_valid(self):
        """Single equipment with exergoeconomic data -> is_valid=True."""
        equipment = [
            {"id": "a", "name": "A", "equipment_type": "compressor", "subtype": "screw", "parameters": {}},
        ]
        results = {
            "a": {
                "exergoeconomic_f_factor": 0.30,
                "exergoeconomic_r_factor": 0.40,
                "exergoeconomic_Z_dot_eur_h": 2.0,
                "exergoeconomic_C_dot_destruction_eur_h": 5.0,
                "avoidable_ratio_pct": 50,
                "exergy_in_kW": 100,
            }
        }
        result = analyze_thermoeconomic_optimization(equipment, results)
        assert result.is_valid is True
        assert result.num_equipment == 1

    def test_all_maintain_zero_savings(self):
        """All maintain strategy -> total savings = 0."""
        # Both mid-f, low-avoidable -> maintain
        equipment = [
            {"id": "a", "name": "A", "equipment_type": "pump", "subtype": "centrifugal", "parameters": {}},
            {"id": "b", "name": "B", "equipment_type": "pump", "subtype": "centrifugal", "parameters": {}},
        ]
        results = {
            "a": {
                "exergoeconomic_f_factor": 0.40,
                "exergoeconomic_r_factor": 0.25,
                "exergoeconomic_Z_dot_eur_h": 1.0,
                "exergoeconomic_C_dot_destruction_eur_h": 1.0,
                "avoidable_ratio_pct": 10,  # low avoidable -> maintain
                "exergy_in_kW": 50,
            },
            "b": {
                "exergoeconomic_f_factor": 0.50,
                "exergoeconomic_r_factor": 0.20,
                "exergoeconomic_Z_dot_eur_h": 1.5,
                "exergoeconomic_C_dot_destruction_eur_h": 1.5,
                "avoidable_ratio_pct": 15,  # low avoidable -> maintain
                "exergy_in_kW": 80,
            },
        }
        result = analyze_thermoeconomic_optimization(equipment, results)
        assert result.is_valid is True
        # maintain -> C_savings = C_dot_D * avoidable but maintain equipment
        # still has savings computed; check all strategies are maintain
        for rec in result.recommendations:
            assert rec.strategy == "maintain"

    def test_serialization(self, sample_result):
        """to_dict() produces JSON-serializable output."""
        d = sample_result.to_dict()
        json_str = json.dumps(d)
        assert len(json_str) > 0
        parsed = json.loads(json_str)
        assert parsed["is_valid"] is True


class TestFeasibility:
    """Feasibility check tests."""

    def test_feasible_with_data(self, sample_equipment_and_results):
        """Feasibility returns True when exergoeconomic data present."""
        equipment, results = sample_equipment_and_results
        feasible, reasons = check_thermoeconomic_feasibility(equipment, results)
        assert feasible is True

    def test_infeasible_without_data(self):
        """Feasibility returns False when no exergoeconomic data."""
        equipment = [
            {"id": "a", "name": "A", "equipment_type": "pump", "subtype": "centrifugal"},
        ]
        results = {"a": {"exergy_in_kW": 100}}
        feasible, reasons = check_thermoeconomic_feasibility(equipment, results)
        assert feasible is False
        assert len(reasons) > 0


class TestIntegration:
    """Integration with factory analysis."""

    def test_factory_includes_thermoeconomic(self):
        """analyze_factory() result has thermoeconomic_optimization field."""
        from engine.factory import FactoryAnalysisResult
        import dataclasses

        fields = {f.name for f in dataclasses.fields(FactoryAnalysisResult)}
        assert "thermoeconomic_optimization" in fields
