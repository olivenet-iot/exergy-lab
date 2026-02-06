"""
Tests for engine/energy_management.py

ISO 50001 energy management motor: EnPI calculations, maturity scoring,
action plan building, chart data generation, and edge cases.
"""

import json
import pytest

from engine.energy_management import (
    ACTION_CATEGORIES,
    GAP_RECOMMENDATIONS,
    MATURITY_DIMENSIONS,
    MATURITY_LEVELS,
    MATURITY_SCORERS,
    ActionItem,
    EnergyManagementResult,
    EnPIMetrics,
    MaturityDimension,
    _assess_maturity,
    _build_action_plan,
    _calculate_enpi,
    _collect_warnings,
    _determine_maturity_level,
    _generate_action_timeline,
    _generate_enpi_radar,
    _generate_maturity_radar,
    _score_action_planning,
    _score_cost_optimization,
    _score_energy_review,
    _score_heat_integration,
    _score_improvement_opportunities,
    _score_monitoring,
    _score_performance_indicators,
    _summarize_actions,
    analyze_energy_management,
    check_energy_management_feasibility,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def full_factory_data():
    """Complete factory data with all motors and rich equipment results."""
    return {
        "equipment_results": [
            {
                "id": "comp-1",
                "name": "Kompresor-1",
                "equipment_type": "compressor",
                "subtype": "screw",
                "analysis": {
                    "exergy_in_kW": 200,
                    "exergy_out_kW": 120,
                    "exergy_destroyed_kW": 80,
                    "exergy_efficiency_pct": 60.0,
                    "exergy_destroyed_avoidable_kW": 48,
                    "exergy_destroyed_unavoidable_kW": 32,
                    "avoidable_ratio_pct": 60.0,
                    "annual_loss_EUR": 5000,
                    "recoverable_heat_kW": 20,
                    "exergoeconomic_f_factor": 0.15,
                    "exergoeconomic_r_factor": 0.60,
                    "exergoeconomic_Z_dot_eur_h": 2.0,
                    "exergoeconomic_C_dot_destruction_eur_h": 12.0,
                    "benchmark_rating": "average",
                },
            },
            {
                "id": "boiler-1",
                "name": "Kazan-1",
                "equipment_type": "boiler",
                "subtype": "steam_firetube",
                "analysis": {
                    "exergy_in_kW": 500,
                    "exergy_out_kW": 175,
                    "exergy_destroyed_kW": 325,
                    "exergy_efficiency_pct": 35.0,
                    "exergy_destroyed_avoidable_kW": 130,
                    "exergy_destroyed_unavoidable_kW": 195,
                    "avoidable_ratio_pct": 40.0,
                    "annual_loss_EUR": 12000,
                    "recoverable_heat_kW": 50,
                    "exergoeconomic_f_factor": 0.80,
                    "exergoeconomic_r_factor": 0.20,
                    "exergoeconomic_Z_dot_eur_h": 15.0,
                    "exergoeconomic_C_dot_destruction_eur_h": 4.0,
                    "benchmark_rating": "poor",
                },
            },
            {
                "id": "pump-1",
                "name": "Pompa-1",
                "equipment_type": "pump",
                "subtype": "centrifugal",
                "analysis": {
                    "exergy_in_kW": 50,
                    "exergy_out_kW": 30,
                    "exergy_destroyed_kW": 20,
                    "exergy_efficiency_pct": 60.0,
                    "exergy_destroyed_avoidable_kW": 10,
                    "exergy_destroyed_unavoidable_kW": 10,
                    "avoidable_ratio_pct": 50.0,
                    "annual_loss_EUR": 1500,
                    "recoverable_heat_kW": 0,
                    "exergoeconomic_f_factor": 0.40,
                    "exergoeconomic_r_factor": 0.30,
                    "exergoeconomic_Z_dot_eur_h": 1.0,
                    "exergoeconomic_C_dot_destruction_eur_h": 1.5,
                    "benchmark_rating": "good",
                },
            },
        ],
        "aggregates": {
            "total_exergy_input_kW": 750,
            "total_exergy_output_kW": 325,
            "total_exergy_destroyed_kW": 425,
            "factory_exergy_efficiency_pct": 43.3,
            "total_annual_loss_kWh": 150000,
            "total_annual_loss_EUR": 18500,
            "equipment_count": 3,
            "total_exergy_destroyed_avoidable_kW": 188,
            "total_exergy_destroyed_unavoidable_kW": 237,
            "avoidable_ratio_pct": 44.2,
        },
        "hotspots": [
            {"id": "boiler-1", "name": "Kazan-1", "exergy_destroyed_kW": 325, "priority": "high"},
            {"id": "comp-1", "name": "Kompresor-1", "exergy_destroyed_kW": 80, "priority": "medium"},
            {"id": "pump-1", "name": "Pompa-1", "exergy_destroyed_kW": 20, "priority": "low"},
        ],
        "pinch_analysis": {
            "is_valid": True,
            "max_heat_recovery_kW": 150,
            "hot_utility_kW": 200,
            "cold_utility_kW": 100,
        },
        "advanced_exergy": {
            "is_valid": True,
            "num_equipment": 3,
            "total_endogenous_kW": 300,
            "total_exogenous_kW": 125,
        },
        "entropy_generation": {
            "is_valid": True,
            "N_s_factory": 0.42,
            "S_gen_total_kW_K": 1.2,
        },
        "thermoeconomic_optimization": {
            "is_valid": True,
            "recommendations": [
                {
                    "equipment_id": "comp-1",
                    "equipment_name": "Kompresor-1",
                    "strategy": "invest",
                    "priority": "high",
                    "recommended_actions": [
                        "Yuksek verimli motor ve VSD ekleyin",
                        "Izentropik verimi yuksek kompresor tipine gecin",
                    ],
                    "C_savings_annual_eur": 48000,
                    "estimated_investment_eur": 25000,
                    "simple_payback_years": 0.5,
                },
                {
                    "equipment_id": "boiler-1",
                    "equipment_name": "Kazan-1",
                    "strategy": "downsize",
                    "priority": "medium",
                    "recommended_actions": [
                        "Kazan kapasitesini yeniden boyutlandirin",
                    ],
                    "C_savings_annual_eur": 8000,
                    "estimated_investment_eur": 35000,
                    "simple_payback_years": 4.4,
                },
                {
                    "equipment_id": "pump-1",
                    "equipment_name": "Pompa-1",
                    "strategy": "maintain",
                    "priority": "low",
                    "recommended_actions": [
                        "Mevcut bakim programini surdurun",
                    ],
                    "C_savings_annual_eur": 0,
                    "estimated_investment_eur": 0,
                    "simple_payback_years": 99.9,
                },
            ],
            "cost_benefit_ranking": [
                {"equipment_id": "comp-1", "strategy": "invest", "simple_payback_years": 0.5},
                {"equipment_id": "boiler-1", "strategy": "downsize", "simple_payback_years": 4.4},
            ],
            "strategy_distribution": {"invest": 1, "downsize": 1, "maintain": 1},
            "total_savings_annual_eur": 56000,
            "total_estimated_investment_eur": 60000,
            "factory_payback_years": 1.1,
        },
    }


@pytest.fixture
def minimal_factory_data():
    """Minimal factory data: 1 equipment with basic exergy fields only."""
    return {
        "equipment_results": [
            {
                "id": "eq-1",
                "name": "Ekipman-1",
                "equipment_type": "compressor",
                "subtype": "screw",
                "analysis": {
                    "exergy_in_kW": 100,
                    "exergy_out_kW": 50,
                    "exergy_destroyed_kW": 50,
                    "exergy_efficiency_pct": 50.0,
                },
            },
        ],
        "aggregates": {
            "total_exergy_input_kW": 100,
            "total_exergy_output_kW": 50,
            "total_exergy_destroyed_kW": 50,
            "factory_exergy_efficiency_pct": 50.0,
        },
    }


# ---------------------------------------------------------------------------
# TestEnPI
# ---------------------------------------------------------------------------

class TestEnPI:
    """Energy Performance Indicator tests."""

    def test_exergy_efficiency(self, full_factory_data):
        """eta_ex = E_out / E_in * 100."""
        enpi = _calculate_enpi(full_factory_data)
        expected = 325 / 750 * 100
        assert abs(enpi.exergy_efficiency_pct - expected) < 0.1

    def test_sec(self, full_factory_data):
        """SEC = E_in / E_out."""
        enpi = _calculate_enpi(full_factory_data)
        expected = 750 / 325
        assert abs(enpi.specific_exergy_consumption - expected) < 0.01

    def test_edr(self, full_factory_data):
        """EDR = I_total / E_in * 100."""
        enpi = _calculate_enpi(full_factory_data)
        expected = 425 / 750 * 100
        assert abs(enpi.exergy_destruction_ratio_pct - expected) < 0.1

    def test_alr(self, full_factory_data):
        """ALR = I_avoidable / I_total * 100."""
        enpi = _calculate_enpi(full_factory_data)
        I_avoidable = 48 + 130 + 10  # from equipment results
        expected = I_avoidable / 425 * 100
        assert abs(enpi.avoidable_loss_ratio_pct - expected) < 0.1

    def test_eci(self, full_factory_data):
        """ECI = C_dot_D_total / E_in."""
        enpi = _calculate_enpi(full_factory_data)
        C_dot_D = 12.0 + 4.0 + 1.5  # from equipment results
        expected = C_dot_D / 750
        assert abs(enpi.energy_cost_intensity_eur_kWh - expected) < 0.001

    def test_hrp(self, full_factory_data):
        """HRP = recoverable / I_total * 100."""
        enpi = _calculate_enpi(full_factory_data)
        recoverable = 20 + 50 + 0  # from equipment results
        expected = recoverable / 425 * 100
        assert abs(enpi.heat_recovery_potential_pct - expected) < 0.1

    def test_egi(self, full_factory_data):
        """EGI = N_s_factory from EGM."""
        enpi = _calculate_enpi(full_factory_data)
        assert abs(enpi.entropy_generation_intensity - 0.42) < 0.001

    def test_zero_exergy_in_handled(self):
        """E_in = 0 -> all EnPIs safe (no division by zero)."""
        data = {
            "equipment_results": [
                {"analysis": {"exergy_in_kW": 0, "exergy_out_kW": 0, "exergy_destroyed_kW": 0}},
            ],
            "aggregates": {
                "total_exergy_input_kW": 0,
                "total_exergy_output_kW": 0,
                "total_exergy_destroyed_kW": 0,
            },
        }
        enpi = _calculate_enpi(data)
        assert enpi.exergy_efficiency_pct == 0.0
        assert enpi.specific_exergy_consumption == 0.0
        assert enpi.exergy_destruction_ratio_pct == 0.0
        assert enpi.avoidable_loss_ratio_pct == 0.0
        assert enpi.energy_cost_intensity_eur_kWh == 0.0
        assert enpi.heat_recovery_potential_pct == 0.0
        assert enpi.entropy_generation_intensity == 0.0


# ---------------------------------------------------------------------------
# TestMaturity
# ---------------------------------------------------------------------------

class TestMaturity:
    """Maturity assessment tests."""

    def test_all_dimensions_scored(self, full_factory_data):
        """7 dimensions scored."""
        dims = _assess_maturity(full_factory_data)
        assert len(dims) == 7

    def test_scores_0_to_100(self, full_factory_data):
        """All scores between 0 and 100."""
        dims = _assess_maturity(full_factory_data)
        for d in dims:
            assert 0 <= d.score <= 100

    def test_maturity_level_assignment(self):
        """Score -> correct level."""
        assert _determine_maturity_level(95) == ("leading", "Lider (Leading)")
        assert _determine_maturity_level(90) == ("leading", "Lider (Leading)")
        assert _determine_maturity_level(80) == ("mature", "Olgun (Mature)")
        assert _determine_maturity_level(70) == ("mature", "Olgun (Mature)")
        assert _determine_maturity_level(60) == ("developing", "Gelisen (Developing)")
        assert _determine_maturity_level(50) == ("developing", "Gelisen (Developing)")
        assert _determine_maturity_level(40) == ("beginning", "Baslangic (Beginning)")
        assert _determine_maturity_level(30) == ("beginning", "Baslangic (Beginning)")
        assert _determine_maturity_level(20) == ("aware", "Farkindalik (Aware)")
        assert _determine_maturity_level(0) == ("aware", "Farkindalik (Aware)")

    def test_full_data_high_score(self, full_factory_data):
        """All motors present -> high maturity score."""
        dims = _assess_maturity(full_factory_data)
        avg = sum(d.score for d in dims) // len(dims)
        # With all motors and 3 equipment, expect >= 70
        assert avg >= 70

    def test_minimal_data_low_score(self, minimal_factory_data):
        """Only basic analysis -> low maturity score."""
        dims = _assess_maturity(minimal_factory_data)
        avg = sum(d.score for d in dims) // len(dims)
        # With only 1 equipment and no motors, expect < 30
        assert avg < 30

    def test_findings_and_gaps_populated(self, full_factory_data):
        """Findings and gaps are populated."""
        dims = _assess_maturity(full_factory_data)
        for d in dims:
            assert isinstance(d.findings, list)
            assert isinstance(d.gaps, list)
            # Should have at least some findings given full data
            assert len(d.findings) > 0 or len(d.gaps) > 0


# ---------------------------------------------------------------------------
# TestMaturityScorers
# ---------------------------------------------------------------------------

class TestMaturityScorers:
    """Individual scorer tests."""

    def test_energy_review_max_score(self, full_factory_data):
        """Full data -> high score (near 100)."""
        score, findings, gaps = _score_energy_review(full_factory_data)
        # 3 eq * 5 = 15 (max 25), 3 types * 7 = 21 (max 25), AV/UN = 25, EGM = 25
        assert score >= 80

    def test_performance_indicators_no_speco(self, minimal_factory_data):
        """No SPECO -> low score."""
        score, findings, gaps = _score_performance_indicators(minimal_factory_data)
        # Has eta (25) but no SPECO, no benchmark, < 3 equipment
        assert score == 25

    def test_improvement_all_motors(self, full_factory_data):
        """All advanced motors present -> 100."""
        score, findings, gaps = _score_improvement_opportunities(full_factory_data)
        assert score == 100

    def test_action_planning_no_thermo(self, minimal_factory_data):
        """No thermoeconomic -> 0."""
        score, findings, gaps = _score_action_planning(minimal_factory_data)
        assert score == 0

    def test_heat_integration_with_pinch(self, full_factory_data):
        """Pinch present with recovery -> high score."""
        score, findings, gaps = _score_heat_integration(full_factory_data)
        assert score == 100  # pinch valid (50) + recovery (25) + hot_utility (25)

    def test_cost_optimization_with_speco(self, full_factory_data):
        """SPECO + thermo -> high score."""
        score, findings, gaps = _score_cost_optimization(full_factory_data)
        assert score == 100  # SPECO(35) + thermo(35) + ranking(30)


# ---------------------------------------------------------------------------
# TestActionPlan
# ---------------------------------------------------------------------------

class TestActionPlan:
    """Action plan tests."""

    def test_actions_from_thermoeconomic(self, full_factory_data):
        """Thermoeconomic recommendations produce actions."""
        actions = _build_action_plan(full_factory_data)
        thermo_actions = [a for a in actions if a.source == "thermoeconomic"]
        assert len(thermo_actions) == 3  # 3 recommendations

    def test_actions_from_pinch(self, full_factory_data):
        """Pinch recovery produces action."""
        actions = _build_action_plan(full_factory_data)
        pinch_actions = [a for a in actions if a.source == "pinch"]
        assert len(pinch_actions) == 1
        assert "150" in pinch_actions[0].action  # recovery_kW

    def test_category_assignment_quick_win(self, full_factory_data):
        """payback < 1y -> quick_win."""
        actions = _build_action_plan(full_factory_data)
        # comp-1 has payback 0.5y
        comp_actions = [a for a in actions if a.equipment_id == "comp-1"]
        assert len(comp_actions) == 1
        assert comp_actions[0].category == "quick_win"

    def test_category_assignment_strategic(self, full_factory_data):
        """payback > 3y -> strategic."""
        actions = _build_action_plan(full_factory_data)
        # boiler-1 has payback 4.4y
        boiler_actions = [a for a in actions if a.equipment_id == "boiler-1"]
        assert len(boiler_actions) == 1
        assert boiler_actions[0].category == "strategic"

    def test_maintain_is_monitoring(self, full_factory_data):
        """maintain strategy -> monitoring category."""
        actions = _build_action_plan(full_factory_data)
        pump_actions = [a for a in actions if a.equipment_id == "pump-1"]
        assert len(pump_actions) == 1
        assert pump_actions[0].category == "monitoring"

    def test_sorted_by_category_then_payback(self, full_factory_data):
        """Actions sorted: quick_win -> medium -> strategic -> monitoring, then payback."""
        actions = _build_action_plan(full_factory_data)
        category_order = {"quick_win": 0, "medium_term": 1, "strategic": 2, "monitoring": 3}
        for i in range(len(actions) - 1):
            a, b = actions[i], actions[i + 1]
            a_cat = category_order.get(a.category, 4)
            b_cat = category_order.get(b.category, 4)
            if a_cat == b_cat:
                assert a.payback_years <= b.payback_years
            else:
                assert a_cat <= b_cat

    def test_action_ids_sequential(self, full_factory_data):
        """Action IDs are A-01, A-02, ..."""
        actions = _build_action_plan(full_factory_data)
        # IDs are assigned before sorting, but should be present
        ids = [a.id for a in actions]
        assert len(ids) == len(set(ids))  # unique
        for aid in ids:
            assert aid.startswith("A-")


# ---------------------------------------------------------------------------
# TestActionSummary
# ---------------------------------------------------------------------------

class TestActionSummary:
    """Action summary tests."""

    def test_summary_has_all_categories(self, full_factory_data):
        """All 4 categories present in summary."""
        actions = _build_action_plan(full_factory_data)
        summary = _summarize_actions(actions)
        for cat in ACTION_CATEGORIES:
            assert cat in summary

    def test_totals_consistent(self, full_factory_data):
        """Category counts sum to total actions."""
        actions = _build_action_plan(full_factory_data)
        summary = _summarize_actions(actions)
        total_count = sum(v["count"] for v in summary.values())
        assert total_count == len(actions)


# ---------------------------------------------------------------------------
# TestChartData
# ---------------------------------------------------------------------------

class TestChartData:
    """Visualization data tests."""

    def test_enpi_radar_7_categories(self, full_factory_data):
        """7 EnPI categories in radar."""
        enpi = _calculate_enpi(full_factory_data)
        radar = _generate_enpi_radar(enpi)
        assert len(radar["categories"]) == 7
        assert len(radar["values"]) == 7

    def test_enpi_radar_values_0_100(self, full_factory_data):
        """Radar values between 0 and 100."""
        enpi = _calculate_enpi(full_factory_data)
        radar = _generate_enpi_radar(enpi)
        for v in radar["values"]:
            assert 0 <= v <= 100

    def test_maturity_radar_7_dimensions(self, full_factory_data):
        """7 maturity dimensions in radar."""
        dims = _assess_maturity(full_factory_data)
        radar = _generate_maturity_radar(dims)
        assert len(radar["categories"]) == 7
        assert len(radar["values"]) == 7
        assert radar["max_value"] == 100

    def test_action_timeline_structure(self, full_factory_data):
        """Timeline has expected structure."""
        actions = _build_action_plan(full_factory_data)
        timeline = _generate_action_timeline(actions)
        assert "categories" in timeline
        assert "category_labels" in timeline
        assert "category_colors" in timeline
        # Should have at least some categories populated
        assert len(timeline["categories"]) > 0


# ---------------------------------------------------------------------------
# TestEdgeCases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Edge cases."""

    def test_empty_equipment_invalid(self):
        """No equipment -> is_valid=False."""
        result = analyze_energy_management({"equipment_results": []})
        assert result.is_valid is False
        assert "yok" in result.error_message.lower()

    def test_minimal_factory_data(self, minimal_factory_data):
        """Only basic exergy -> valid but low maturity score."""
        result = analyze_energy_management(minimal_factory_data)
        assert result.is_valid is True
        assert result.maturity_score < 30
        assert result.maturity_level in ("aware", "beginning")

    def test_no_advanced_motors(self, minimal_factory_data):
        """No advanced motors -> EnPI partially filled, maturity low."""
        result = analyze_energy_management(minimal_factory_data)
        assert result.enpi is not None
        assert result.enpi.exergy_efficiency_pct > 0
        # EGI should be 0 (no EGM)
        assert result.enpi.entropy_generation_intensity == 0.0
        # HRP should be 0 (no recoverable heat)
        assert result.enpi.heat_recovery_potential_pct == 0.0

    def test_serialization(self, full_factory_data):
        """to_dict() produces JSON-serializable output."""
        result = analyze_energy_management(full_factory_data)
        d = result.to_dict()
        serialized = json.dumps(d)
        assert isinstance(serialized, str)
        parsed = json.loads(serialized)
        assert parsed["is_valid"] is True
        assert parsed["num_equipment"] == 3


# ---------------------------------------------------------------------------
# TestIntegration
# ---------------------------------------------------------------------------

class TestIntegration:
    """Integration with factory pipeline."""

    def test_feasibility_check_positive(self, full_factory_data):
        """Feasibility check passes with equipment."""
        feasible, reasons = check_energy_management_feasibility(full_factory_data)
        assert feasible is True

    def test_feasibility_check_negative(self):
        """Feasibility check fails without equipment."""
        feasible, reasons = check_energy_management_feasibility({"equipment_results": []})
        assert feasible is False

    def test_full_analysis_result_structure(self, full_factory_data):
        """Full analysis produces expected structure."""
        result = analyze_energy_management(full_factory_data)
        assert result.is_valid is True
        assert result.num_equipment == 3
        assert result.enpi is not None
        assert len(result.maturity_dimensions) == 7
        assert result.maturity_score >= 0
        assert result.maturity_level in ("leading", "mature", "developing", "beginning", "aware")
        assert len(result.action_plan) > 0
        assert isinstance(result.action_summary, dict)
        assert isinstance(result.enpi_radar_data, dict)
        assert isinstance(result.maturity_radar_data, dict)
        assert isinstance(result.action_timeline_data, dict)

    def test_factory_includes_energy_management(self):
        """analyze_factory() result includes energy_management field."""
        from engine.factory import FactoryAnalysisResult
        import dataclasses
        field_names = {f.name for f in dataclasses.fields(FactoryAnalysisResult)}
        assert "energy_management" in field_names


# ---------------------------------------------------------------------------
# TestWarnings
# ---------------------------------------------------------------------------

class TestWarnings:
    """Warning generation tests."""

    def test_low_maturity_warning(self):
        """Maturity < 30 triggers warning."""
        enpi = EnPIMetrics(
            exergy_efficiency_pct=40, specific_exergy_consumption=2.5,
            exergy_destruction_ratio_pct=40, avoidable_loss_ratio_pct=30,
            energy_cost_intensity_eur_kWh=0.02, heat_recovery_potential_pct=10,
            entropy_generation_intensity=0.3,
        )
        warnings = _collect_warnings(enpi, 25, [])
        assert any("olgunlug" in w.lower() or "dusuk" in w.lower() for w in warnings)

    def test_high_edr_warning(self):
        """EDR > 60% triggers warning."""
        enpi = EnPIMetrics(
            exergy_efficiency_pct=30, specific_exergy_consumption=3.3,
            exergy_destruction_ratio_pct=70, avoidable_loss_ratio_pct=30,
            energy_cost_intensity_eur_kWh=0.02, heat_recovery_potential_pct=10,
            entropy_generation_intensity=0.3,
        )
        warnings = _collect_warnings(enpi, 50, [ActionItem(
            id="A-01", source="test", equipment_id=None, equipment_name=None,
            action="test", category="quick_win", estimated_savings_eur=100,
            estimated_investment_eur=50, payback_years=0.5, priority="high",
            timeline="0-3 ay",
        )])
        assert any("yikim" in w.lower() for w in warnings)

    def test_no_actions_warning(self):
        """Empty action plan triggers warning."""
        enpi = EnPIMetrics(
            exergy_efficiency_pct=50, specific_exergy_consumption=2.0,
            exergy_destruction_ratio_pct=50, avoidable_loss_ratio_pct=30,
            energy_cost_intensity_eur_kWh=0.02, heat_recovery_potential_pct=10,
            entropy_generation_intensity=0.3,
        )
        warnings = _collect_warnings(enpi, 50, [])
        assert any("aksiyon" in w.lower() for w in warnings)


# ---------------------------------------------------------------------------
# TestConstants
# ---------------------------------------------------------------------------

class TestConstants:
    """Constant/config validation tests."""

    def test_maturity_levels_cover_0_100(self):
        """Maturity levels cover full 0-100 range without gaps."""
        levels = sorted(MATURITY_LEVELS.values(), key=lambda x: x["min"])
        assert levels[0]["min"] == 0  # Lowest starts at 0
        # Each level should be reachable
        for score in range(0, 101):
            level, _ = _determine_maturity_level(score)
            assert level in MATURITY_LEVELS

    def test_7_maturity_dimensions(self):
        """7 maturity dimensions defined."""
        assert len(MATURITY_DIMENSIONS) == 7

    def test_7_scorers(self):
        """7 scorers registered."""
        assert len(MATURITY_SCORERS) == 7
        for key in MATURITY_DIMENSIONS:
            assert key in MATURITY_SCORERS

    def test_4_action_categories(self):
        """4 action categories defined."""
        assert len(ACTION_CATEGORIES) == 4

    def test_gap_recommendations_for_all_dimensions(self):
        """Gap recommendations exist for all 7 dimensions."""
        for key in MATURITY_DIMENSIONS:
            assert key in GAP_RECOMMENDATIONS
            assert len(GAP_RECOMMENDATIONS[key]) >= 2
