"""Tests for advanced exergy analysis (EN/EX decomposition)."""

import json
import pytest

from engine.advanced_exergy import (
    AdvancedExergyEquipmentResult,
    AdvancedExergyResult,
    BASE_ISOLATION_FACTORS,
    INTERACTION_COEFFICIENTS,
    REFERENCE_EFFICIENCIES,
    analyze_advanced_exergy,
    check_advanced_exergy_feasibility,
    _calculate_efficiency_deviations,
    _calculate_isolation_factors,
    _analyze_single_equipment,
    _identify_exogenous_sources,
    _determine_priority,
    _calculate_factory_metrics,
    _create_priority_ranking,
    _build_interaction_network,
    _generate_quadrant_chart_data,
    _collect_warnings,
    _filter_valid_equipment,
    _get_factory_equipment_types,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def factory_equipment():
    """4-equipment factory: boiler, compressor, heat_exchanger, steam_turbine."""
    equipment_list = [
        {
            "id": "b1",
            "name": "Kazan-1",
            "equipment_type": "boiler",
            "subtype": "steam_firetube",
            "parameters": {},
        },
        {
            "id": "c1",
            "name": "Kompresor-1",
            "equipment_type": "compressor",
            "subtype": "screw",
            "parameters": {},
        },
        {
            "id": "hx1",
            "name": "Esanjor-1",
            "equipment_type": "heat_exchanger",
            "subtype": "shell_tube",
            "parameters": {},
        },
        {
            "id": "st1",
            "name": "Turbin-1",
            "equipment_type": "steam_turbine",
            "subtype": "back_pressure",
            "parameters": {},
        },
    ]

    # Analysis results with varying efficiencies and AV/UN splits
    analysis_results = {
        "b1": {
            "exergy_destroyed_kW": 120.0,
            "exergy_efficiency_pct": 32.0,  # Below ref 82% → large positive δ
            "exergy_in_kW": 176.5,
            "exergy_out_kW": 56.5,
            "exergy_destroyed_avoidable_kW": 50.0,
            "exergy_destroyed_unavoidable_kW": 70.0,
        },
        "c1": {
            "exergy_destroyed_kW": 45.0,
            "exergy_efficiency_pct": 60.0,  # Below ref 80% → positive δ
            "exergy_in_kW": 112.5,
            "exergy_out_kW": 67.5,
            "exergy_destroyed_avoidable_kW": 25.0,
            "exergy_destroyed_unavoidable_kW": 20.0,
        },
        "hx1": {
            "exergy_destroyed_kW": 30.0,
            "exergy_efficiency_pct": 55.0,  # Below ref 75% → positive δ
            "exergy_in_kW": 66.7,
            "exergy_out_kW": 36.7,
            "exergy_destroyed_avoidable_kW": 18.0,
            "exergy_destroyed_unavoidable_kW": 12.0,
        },
        "st1": {
            "exergy_destroyed_kW": 80.0,
            "exergy_efficiency_pct": 65.0,  # Below ref 78% → positive δ
            "exergy_in_kW": 228.6,
            "exergy_out_kW": 148.6,
            "exergy_destroyed_avoidable_kW": 40.0,
            "exergy_destroyed_unavoidable_kW": 40.0,
        },
    }

    return equipment_list, analysis_results


@pytest.fixture
def two_same_type():
    """2 compressors (same type)."""
    equipment_list = [
        {"id": "c1", "name": "Comp-1", "equipment_type": "compressor",
         "subtype": "screw", "parameters": {}},
        {"id": "c2", "name": "Comp-2", "equipment_type": "compressor",
         "subtype": "centrifugal", "parameters": {}},
    ]
    analysis_results = {
        "c1": {
            "exergy_destroyed_kW": 30.0,
            "exergy_efficiency_pct": 50.0,
            "exergy_destroyed_avoidable_kW": 15.0,
            "exergy_destroyed_unavoidable_kW": 15.0,
        },
        "c2": {
            "exergy_destroyed_kW": 25.0,
            "exergy_efficiency_pct": 70.0,
            "exergy_destroyed_avoidable_kW": 10.0,
            "exergy_destroyed_unavoidable_kW": 15.0,
        },
    }
    return equipment_list, analysis_results


# ---------------------------------------------------------------------------
# TestEfficiencyDeviations
# ---------------------------------------------------------------------------

class TestEfficiencyDeviations:
    """Test efficiency deviation calculation."""

    def test_below_reference_positive_delta(self, factory_equipment):
        """Equipment below reference → positive δ."""
        eq_list, results = factory_equipment
        deviations = _calculate_efficiency_deviations(eq_list, results)

        # Boiler: ref=0.82, actual=0.32 → δ = (0.82-0.32)/0.82 ≈ 0.6098
        assert deviations["b1"] > 0
        assert abs(deviations["b1"] - 0.6098) < 0.01

    def test_at_reference_zero_delta(self):
        """Equipment at exact reference → δ = 0."""
        eq = [{"id": "p1", "name": "P", "equipment_type": "pump",
               "subtype": "centrifugal", "parameters": {}}]
        results = {"p1": {"exergy_efficiency_pct": 80.0, "exergy_destroyed_kW": 5}}
        deviations = _calculate_efficiency_deviations(eq, results)
        assert abs(deviations["p1"]) < 0.001

    def test_above_reference_negative_delta(self):
        """Equipment above reference → negative δ (capped at -0.5)."""
        eq = [{"id": "p1", "name": "P", "equipment_type": "pump",
               "subtype": "centrifugal", "parameters": {}}]
        # Ref=0.80, actual=0.90 → δ = (0.80-0.90)/0.80 = -0.125
        results = {"p1": {"exergy_efficiency_pct": 90.0, "exergy_destroyed_kW": 5}}
        deviations = _calculate_efficiency_deviations(eq, results)
        assert deviations["p1"] < 0
        assert deviations["p1"] >= -0.5

    def test_clamp_high(self):
        """Very inefficient equipment → δ clamped to 1.0."""
        eq = [{"id": "x", "name": "X", "equipment_type": "boiler",
               "subtype": "steam_firetube", "parameters": {}}]
        results = {"x": {"exergy_efficiency_pct": 0.0, "exergy_destroyed_kW": 100}}
        deviations = _calculate_efficiency_deviations(eq, results)
        assert deviations["x"] == 1.0

    def test_subtype_specific_reference(self):
        """Subtype-specific reference efficiency used when available."""
        eq_screw = [{"id": "a", "name": "A", "equipment_type": "compressor",
                     "subtype": "screw", "parameters": {}}]
        eq_cent = [{"id": "b", "name": "B", "equipment_type": "compressor",
                    "subtype": "centrifugal", "parameters": {}}]
        results_a = {"a": {"exergy_efficiency_pct": 60.0, "exergy_destroyed_kW": 10}}
        results_b = {"b": {"exergy_efficiency_pct": 60.0, "exergy_destroyed_kW": 10}}

        dev_a = _calculate_efficiency_deviations(eq_screw, results_a)
        dev_b = _calculate_efficiency_deviations(eq_cent, results_b)

        # screw ref=0.80, cent ref=0.85 → different δ for same actual
        assert dev_a["a"] != dev_b["b"]
        assert dev_b["b"] > dev_a["a"]  # centrifugal has higher ref → larger gap


# ---------------------------------------------------------------------------
# TestIsolationFactors
# ---------------------------------------------------------------------------

class TestIsolationFactors:
    """Test isolation factor calculation."""

    def test_base_factor_no_interactions(self):
        """Single equipment → isolation factor equals base."""
        eq = [{"id": "p1", "name": "P", "equipment_type": "pump",
               "subtype": "centrifugal", "parameters": {}}]
        results = {"p1": {"exergy_efficiency_pct": 80.0, "exergy_destroyed_kW": 10}}
        deviations = {"p1": 0.0}
        types = {"pump": ["p1"]}

        factors = _calculate_isolation_factors(eq, results, types, deviations)
        assert abs(factors["p1"] - BASE_ISOLATION_FACTORS["pump"]) < 0.001

    def test_reduction_from_inefficient_neighbors(self, factory_equipment):
        """Inefficient neighbors reduce isolation factor."""
        eq_list, results = factory_equipment
        types = _get_factory_equipment_types(eq_list)
        deviations = _calculate_efficiency_deviations(eq_list, results)

        factors = _calculate_isolation_factors(eq_list, results, types, deviations)

        # Steam turbine has high α from boiler (0.20) and boiler is very inefficient
        # So st1 should have lower φ than its base (0.70)
        assert factors["st1"] < BASE_ISOLATION_FACTORS["steam_turbine"]

    def test_no_reduction_from_efficient_neighbors(self):
        """Efficient neighbors (δ ≤ 0) don't reduce isolation."""
        eq = [
            {"id": "a", "name": "A", "equipment_type": "boiler",
             "subtype": "steam_firetube", "parameters": {}},
            {"id": "b", "name": "B", "equipment_type": "heat_exchanger",
             "subtype": "plate", "parameters": {}},
        ]
        results = {
            "a": {"exergy_efficiency_pct": 90.0, "exergy_destroyed_kW": 10},
            "b": {"exergy_efficiency_pct": 90.0, "exergy_destroyed_kW": 5},
        }
        deviations = {"a": -0.1, "b": -0.06}  # Both above reference
        types = {"boiler": ["a"], "heat_exchanger": ["b"]}

        factors = _calculate_isolation_factors(eq, results, types, deviations)
        # No reduction → stays at base
        assert abs(factors["a"] - BASE_ISOLATION_FACTORS["boiler"]) < 0.001

    def test_clamp_range(self, factory_equipment):
        """Isolation factor clamped to [0.20, 0.95]."""
        eq_list, results = factory_equipment
        types = _get_factory_equipment_types(eq_list)
        deviations = _calculate_efficiency_deviations(eq_list, results)

        factors = _calculate_isolation_factors(eq_list, results, types, deviations)

        for eq_id, phi in factors.items():
            assert 0.20 <= phi <= 0.95, f"φ={phi} for {eq_id} out of range"

    def test_no_effect_zero_alpha(self):
        """Equipment types with α=0 don't interact."""
        eq = [
            {"id": "p1", "name": "Pump", "equipment_type": "pump",
             "subtype": "centrifugal", "parameters": {}},
            {"id": "c1", "name": "Chiller", "equipment_type": "chiller",
             "subtype": "screw", "parameters": {}},
        ]
        results = {
            "p1": {"exergy_efficiency_pct": 50.0, "exergy_destroyed_kW": 10},
            "c1": {"exergy_efficiency_pct": 20.0, "exergy_destroyed_kW": 15},
        }
        deviations = _calculate_efficiency_deviations(eq, results)
        types = {"pump": ["p1"], "chiller": ["c1"]}

        factors = _calculate_isolation_factors(eq, results, types, deviations)

        # No interaction between pump↔chiller (α=0 both ways)
        # pump affected by chiller: α(pump, chiller)=0 → no effect
        assert abs(factors["p1"] - BASE_ISOLATION_FACTORS["pump"]) < 0.001


# ---------------------------------------------------------------------------
# TestENEXDecomposition
# ---------------------------------------------------------------------------

class TestENEXDecomposition:
    """Test EN/EX and 4-quadrant decomposition."""

    def test_en_ex_sum_equals_total(self, factory_equipment):
        """I_EN + I_EX must equal I_total."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            total = r.I_EN_kW + r.I_EX_kW
            assert abs(total - r.I_total_kW) < 0.01, \
                f"{r.equipment_name}: EN({r.I_EN_kW})+EX({r.I_EX_kW})={total} != {r.I_total_kW}"

    def test_four_quadrant_sum_equals_total(self, factory_equipment):
        """AV-EN + AV-EX + UN-EN + UN-EX must equal I_total."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            quad_sum = r.I_AV_EN_kW + r.I_AV_EX_kW + r.I_UN_EN_kW + r.I_UN_EX_kW
            assert abs(quad_sum - r.I_total_kW) < 0.01, \
                f"{r.equipment_name}: quad sum {quad_sum} != {r.I_total_kW}"

    def test_en_less_than_total(self, factory_equipment):
        """I_EN must be ≤ I_total (isolation_factor ≤ 1)."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            assert r.I_EN_kW <= r.I_total_kW + 0.01

    def test_ex_non_negative(self, factory_equipment):
        """I_EX must be ≥ 0."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            assert r.I_EX_kW >= -0.01, f"{r.equipment_name}: I_EX={r.I_EX_kW} < 0"

    def test_all_quadrants_non_negative(self, factory_equipment):
        """All 4 quadrants must be ≥ 0."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            assert r.I_AV_EN_kW >= 0
            assert r.I_AV_EX_kW >= 0
            assert r.I_UN_EN_kW >= 0
            assert r.I_UN_EX_kW >= 0

    def test_high_isolation_mostly_endogenous(self):
        """Equipment with high isolation factor → mostly endogenous."""
        # Pump has base φ=0.85, and if only paired with non-interacting type
        eq = [
            {"id": "p1", "name": "Pump-1", "equipment_type": "pump",
             "subtype": "centrifugal", "parameters": {}},
            {"id": "p2", "name": "Pump-2", "equipment_type": "pump",
             "subtype": "centrifugal", "parameters": {}},
        ]
        results = {
            "p1": {
                "exergy_destroyed_kW": 20.0,
                "exergy_efficiency_pct": 50.0,
                "exergy_destroyed_avoidable_kW": 10.0,
                "exergy_destroyed_unavoidable_kW": 10.0,
            },
            "p2": {
                "exergy_destroyed_kW": 15.0,
                "exergy_efficiency_pct": 55.0,
                "exergy_destroyed_avoidable_kW": 7.0,
                "exergy_destroyed_unavoidable_kW": 8.0,
            },
        }
        result = analyze_advanced_exergy(eq, results)

        for r in result.equipment_results:
            en_ratio = r.I_EN_kW / r.I_total_kW if r.I_total_kW > 0 else 0
            assert en_ratio > 0.70, f"{r.equipment_name}: EN ratio={en_ratio:.2f} too low"


# ---------------------------------------------------------------------------
# TestExogenousSources
# ---------------------------------------------------------------------------

class TestExogenousSources:
    """Test exogenous source identification."""

    def test_sources_sum_approx_ex(self, factory_equipment):
        """Exogenous sources should sum ≈ I_EX (when sources found)."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            if r.exogenous_sources:
                source_sum = sum(s["value_kW"] for s in r.exogenous_sources)
                assert abs(source_sum - r.I_EX_kW) < 0.5, \
                    f"{r.equipment_name}: sources sum {source_sum} != I_EX {r.I_EX_kW}"

    def test_no_self_reference(self, factory_equipment):
        """Equipment should never appear in its own exogenous sources."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            for src in r.exogenous_sources:
                assert src["source_id"] != r.equipment_id, \
                    f"{r.equipment_name} found in own exogenous sources"

    def test_sources_sorted_descending(self, factory_equipment):
        """Sources should be sorted by value_kW descending."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        for r in result.equipment_results:
            if len(r.exogenous_sources) > 1:
                values = [s["value_kW"] for s in r.exogenous_sources]
                assert values == sorted(values, reverse=True)


# ---------------------------------------------------------------------------
# TestPriorityAndMetrics
# ---------------------------------------------------------------------------

class TestPriorityAndMetrics:
    """Test priority ranking and factory metrics."""

    def test_ranking_sorted_by_av_en(self, factory_equipment):
        """Priority ranking must be sorted by AV-EN descending."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        av_en_values = [r["I_AV_EN_kW"] for r in result.priority_ranking]
        assert av_en_values == sorted(av_en_values, reverse=True)

    def test_high_av_en_ratio_high_priority(self):
        """Equipment with AV-EN/I_total > 0.30 → high priority."""
        priority, _ = _determine_priority(
            I_AV_EN=40.0, I_AV_EX=5.0, I_total=100.0, isolation_factor=0.80
        )
        assert priority == "high"

    def test_density_in_range(self, factory_equipment):
        """Interaction density must be in [0, 1]."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)
        assert 0.0 <= result.interaction_density <= 1.0

    def test_factory_en_ex_equals_total(self, factory_equipment):
        """Factory EN + EX must equal total destruction."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        en_plus_ex = result.total_I_EN_kW + result.total_I_EX_kW
        assert abs(en_plus_ex - result.total_I_kW) < 0.1, \
            f"EN({result.total_I_EN_kW})+EX({result.total_I_EX_kW})={en_plus_ex} != {result.total_I_kW}"


# ---------------------------------------------------------------------------
# TestEdgeCases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_single_equipment_invalid(self):
        """1 equipment → is_valid=False."""
        eq = [{"id": "a", "name": "A", "equipment_type": "boiler",
               "subtype": "steam_firetube", "parameters": {}}]
        results = {"a": {"exergy_destroyed_kW": 50.0, "exergy_efficiency_pct": 30.0}}

        result = analyze_advanced_exergy(eq, results)
        assert result.is_valid is False
        assert "at least 2" in result.error.lower()

    def test_zero_destruction_no_crash(self):
        """Equipment with zero destruction filtered out gracefully."""
        eq = [
            {"id": "a", "name": "A", "equipment_type": "boiler",
             "subtype": "steam_firetube", "parameters": {}},
            {"id": "b", "name": "B", "equipment_type": "compressor",
             "subtype": "screw", "parameters": {}},
            {"id": "c", "name": "C", "equipment_type": "pump",
             "subtype": "centrifugal", "parameters": {}},
        ]
        results = {
            "a": {"exergy_destroyed_kW": 50.0, "exergy_efficiency_pct": 30.0,
                   "exergy_destroyed_avoidable_kW": 25.0,
                   "exergy_destroyed_unavoidable_kW": 25.0},
            "b": {"exergy_destroyed_kW": 0.0, "exergy_efficiency_pct": 80.0},
            "c": {"exergy_destroyed_kW": 20.0, "exergy_efficiency_pct": 60.0,
                   "exergy_destroyed_avoidable_kW": 10.0,
                   "exergy_destroyed_unavoidable_kW": 10.0},
        }
        result = analyze_advanced_exergy(eq, results)
        assert result.is_valid is True
        assert len(result.equipment_results) == 2  # b filtered out

    def test_all_same_type_limited_interaction(self, two_same_type):
        """All same type → warning about limited interaction."""
        eq_list, results = two_same_type
        result = analyze_advanced_exergy(eq_list, results)
        assert result.is_valid is True
        assert any("same type" in w.lower() for w in result.warnings)

    def test_missing_av_un_defaults(self):
        """Missing AV/UN → defaults to all unavoidable with warning."""
        eq = [
            {"id": "a", "name": "A", "equipment_type": "boiler",
             "subtype": "steam_firetube", "parameters": {}},
            {"id": "b", "name": "B", "equipment_type": "compressor",
             "subtype": "screw", "parameters": {}},
        ]
        results = {
            "a": {"exergy_destroyed_kW": 50.0, "exergy_efficiency_pct": 30.0},
            "b": {"exergy_destroyed_kW": 30.0, "exergy_efficiency_pct": 50.0},
        }
        result = analyze_advanced_exergy(eq, results)
        assert result.is_valid is True

        # AV-EN and AV-EX should be 0 (all unavoidable)
        for r in result.equipment_results:
            assert r.I_AV_EN_kW == 0
            assert r.I_AV_EX_kW == 0
            assert r.I_UN_kW == r.I_total_kW
            assert any("AV/UN" in w for w in r.warnings)

    def test_to_dict_serializable(self, factory_equipment):
        """to_dict() output must be JSON-serializable."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)

        d = result.to_dict()
        json_str = json.dumps(d)
        assert isinstance(json_str, str)
        assert len(json_str) > 100

        # Check nested equipment results too
        for eq_result in result.equipment_results:
            eq_d = eq_result.to_dict()
            json.dumps(eq_d)


# ---------------------------------------------------------------------------
# TestFeasibility
# ---------------------------------------------------------------------------

class TestFeasibility:
    """Test feasibility check."""

    def test_feasible_factory(self, factory_equipment):
        """Factory with 4 equipment → feasible."""
        eq_list, results = factory_equipment
        feasible, msg = check_advanced_exergy_feasibility(eq_list, results)
        assert feasible is True

    def test_infeasible_single(self):
        """Single equipment → not feasible."""
        eq = [{"id": "a", "name": "A", "equipment_type": "boiler",
               "subtype": "steam_firetube", "parameters": {}}]
        results = {"a": {"exergy_destroyed_kW": 50.0}}
        feasible, msg = check_advanced_exergy_feasibility(eq, results)
        assert feasible is False

    def test_infeasible_low_destruction(self):
        """Total destruction < 10 kW → not feasible."""
        eq = [
            {"id": "a", "name": "A", "equipment_type": "boiler",
             "subtype": "steam_firetube", "parameters": {}},
            {"id": "b", "name": "B", "equipment_type": "compressor",
             "subtype": "screw", "parameters": {}},
        ]
        results = {
            "a": {"exergy_destroyed_kW": 3.0, "exergy_efficiency_pct": 30.0},
            "b": {"exergy_destroyed_kW": 4.0, "exergy_efficiency_pct": 50.0},
        }
        feasible, msg = check_advanced_exergy_feasibility(eq, results)
        assert feasible is False
        assert "10 kW" in msg


# ---------------------------------------------------------------------------
# TestInteractionNetwork
# ---------------------------------------------------------------------------

class TestInteractionNetwork:
    """Test interaction network building."""

    def test_network_has_edges(self, factory_equipment):
        """Factory with interacting equipment → edges present."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)
        # With 4 different types and inefficiencies, should have edges
        assert len(result.interaction_network) > 0

    def test_network_sorted_descending(self, factory_equipment):
        """Network edges sorted by value descending."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)
        if len(result.interaction_network) > 1:
            values = [e["value_kW"] for e in result.interaction_network]
            assert values == sorted(values, reverse=True)


# ---------------------------------------------------------------------------
# TestQuadrantChartData
# ---------------------------------------------------------------------------

class TestQuadrantChartData:
    """Test quadrant chart data generation."""

    def test_chart_has_all_fields(self, factory_equipment):
        """Chart data has labels and 4 data arrays."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)
        chart = result.quadrant_chart_data

        assert "labels" in chart
        assert "AV_EN" in chart
        assert "AV_EX" in chart
        assert "UN_EN" in chart
        assert "UN_EX" in chart

    def test_chart_sorted_by_av_en(self, factory_equipment):
        """Chart labels sorted by AV-EN descending."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)
        chart = result.quadrant_chart_data

        av_en = chart["AV_EN"]
        assert av_en == sorted(av_en, reverse=True)

    def test_chart_lengths_match(self, factory_equipment):
        """All arrays same length as labels."""
        eq_list, results = factory_equipment
        result = analyze_advanced_exergy(eq_list, results)
        chart = result.quadrant_chart_data

        n = len(chart["labels"])
        assert len(chart["AV_EN"]) == n
        assert len(chart["AV_EX"]) == n
        assert len(chart["UN_EN"]) == n
        assert len(chart["UN_EX"]) == n
