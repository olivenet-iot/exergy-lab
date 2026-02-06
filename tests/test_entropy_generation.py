"""
Tests for engine/entropy_generation.py — EGM (Entropy Generation Minimization)

Covers:
- Gouy-Stodola theorem
- Bejan number and grading
- Entropy decomposition
- Heat transfer Bejan number (HX only)
- Augmentation number
- Factory metrics
- Edge cases
- Integration
"""

import math
import pytest

from engine.entropy_generation import (
    BEJAN_GRADES,
    ENTROPY_DECOMPOSITION_FRACTIONS,
    EntropyEquipmentResult,
    EntropyGenerationResult,
    _assign_bejan_grade,
    _analyze_single_equipment,
    _calculate_factory_metrics,
    _collect_warnings,
    _create_irreversibility_ranking,
    _filter_valid_equipment,
    _generate_bejan_chart,
    _generate_decomposition_chart,
    _get_decomposition_fractions,
    _get_dominant_mechanism,
    analyze_entropy_generation,
    check_egm_feasibility,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def five_equipment():
    """5 equipment with varying efficiency and AV/UN data."""
    equipment_list = [
        {"id": "b1", "name": "Kazan-1", "equipment_type": "boiler", "subtype": "steam_firetube", "parameters": {}},
        {"id": "c1", "name": "Kompresor-1", "equipment_type": "compressor", "subtype": "screw", "parameters": {}},
        {"id": "hx1", "name": "Esanjor-1", "equipment_type": "heat_exchanger", "subtype": "shell_tube", "parameters": {}},
        {"id": "ch1", "name": "Chiller-1", "equipment_type": "chiller", "subtype": "screw", "parameters": {}},
        {"id": "p1", "name": "Pompa-1", "equipment_type": "pump", "subtype": "centrifugal", "parameters": {}},
    ]
    analysis_results = {
        "b1": {
            "exergy_in_kW": 500.0,
            "exergy_out_kW": 175.0,
            "exergy_destroyed_kW": 325.0,
            "exergy_efficiency_pct": 35.0,
            "avoidable_ratio_pct": 40.0,
        },
        "c1": {
            "exergy_in_kW": 100.0,
            "exergy_out_kW": 55.0,
            "exergy_destroyed_kW": 45.0,
            "exergy_efficiency_pct": 55.0,
            "avoidable_ratio_pct": 50.0,
        },
        "hx1": {
            "exergy_in_kW": 200.0,
            "exergy_out_kW": 120.0,
            "exergy_destroyed_kW": 80.0,
            "exergy_efficiency_pct": 60.0,
            "avoidable_ratio_pct": 30.0,
        },
        "ch1": {
            "exergy_in_kW": 150.0,
            "exergy_out_kW": 45.0,
            "exergy_destroyed_kW": 105.0,
            "exergy_efficiency_pct": 30.0,
            "avoidable_ratio_pct": 35.0,
        },
        "p1": {
            "exergy_in_kW": 50.0,
            "exergy_out_kW": 30.0,
            "exergy_destroyed_kW": 20.0,
            "exergy_efficiency_pct": 60.0,
            "avoidable_ratio_pct": 45.0,
        },
    }
    return equipment_list, analysis_results


@pytest.fixture
def single_boiler():
    """Single boiler equipment."""
    equipment_list = [
        {"id": "b1", "name": "Kazan-1", "equipment_type": "boiler", "subtype": "steam_firetube", "parameters": {}},
    ]
    analysis_results = {
        "b1": {
            "exergy_in_kW": 500.0,
            "exergy_out_kW": 175.0,
            "exergy_destroyed_kW": 325.0,
            "exergy_efficiency_pct": 35.0,
            "avoidable_ratio_pct": 40.0,
        },
    }
    return equipment_list, analysis_results


# ---------------------------------------------------------------------------
# TestGouyStodola
# ---------------------------------------------------------------------------

class TestGouyStodola:
    """Test Gouy-Stodola theorem: S_gen = I_dot / T0."""

    def test_basic_sgen_calculation(self):
        """S_gen = I_dot / T0 for known values."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {"exergy_destroyed_kW": 100.0, "exergy_in_kW": 300.0, "exergy_efficiency_pct": 66.7}
        T0 = 298.15

        eq = _analyze_single_equipment(item, result, T0)
        expected_S_gen = 100.0 / 298.15
        assert abs(eq.S_gen_kW_K - expected_S_gen) < 1e-8

    def test_zero_destruction(self):
        """S_gen = 0 when I_dot = 0 — but filtered out by _filter_valid."""
        item = {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal"}
        result = {"exergy_destroyed_kW": 0.0, "exergy_in_kW": 50.0, "exergy_efficiency_pct": 100.0}
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.S_gen_kW_K == 0.0

    def test_custom_T0(self):
        """S_gen changes with different T0."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {"exergy_destroyed_kW": 100.0, "exergy_in_kW": 300.0, "exergy_efficiency_pct": 66.7}
        T0_300 = 300.0
        T0_288 = 288.15

        eq300 = _analyze_single_equipment(item, result, T0_300)
        eq288 = _analyze_single_equipment(item, result, T0_288)
        assert abs(eq300.S_gen_kW_K - 100.0 / 300.0) < 1e-8
        assert abs(eq288.S_gen_kW_K - 100.0 / 288.15) < 1e-8

    def test_back_verification(self):
        """T0 * S_gen should equal I_dot (Gouy-Stodola verification)."""
        item = {"id": "c1", "name": "Comp", "equipment_type": "compressor", "subtype": "screw"}
        result = {"exergy_destroyed_kW": 45.0, "exergy_in_kW": 100.0, "exergy_efficiency_pct": 55.0}
        T0 = 298.15

        eq = _analyze_single_equipment(item, result, T0)
        back_I = eq.T0_K * eq.S_gen_kW_K
        assert abs(back_I - 45.0) < 1e-8


# ---------------------------------------------------------------------------
# TestBejanNumber
# ---------------------------------------------------------------------------

class TestBejanNumber:
    """Test N_s = I_dot / E_x_in, clamped [0, 1], grading."""

    def test_ns_approximately_one_minus_eta(self):
        """N_s should approximately equal 1 - eta_ex."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {
            "exergy_destroyed_kW": 325.0,
            "exergy_in_kW": 500.0,
            "exergy_efficiency_pct": 35.0,
        }
        eq = _analyze_single_equipment(item, result, 298.15)
        assert abs(eq.N_s - 0.65) < 0.01

    def test_ns_clamped_to_one(self):
        """N_s should be clamped to [0, 1] even if I_dot > E_x_in."""
        item = {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal"}
        result = {
            "exergy_destroyed_kW": 150.0,
            "exergy_in_kW": 100.0,
            "exergy_efficiency_pct": 0.0,
        }
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.N_s == 1.0

    def test_ns_clamped_to_zero(self):
        """N_s should not be negative."""
        item = {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal"}
        result = {
            "exergy_destroyed_kW": 0.0,
            "exergy_in_kW": 100.0,
            "exergy_efficiency_pct": 100.0,
        }
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.N_s == 0.0

    def test_grade_assignment(self):
        """Each N_s value should get correct grade."""
        assert _assign_bejan_grade(0.10) == "A"
        assert _assign_bejan_grade(0.20) == "B"
        assert _assign_bejan_grade(0.40) == "C"
        assert _assign_bejan_grade(0.60) == "D"
        assert _assign_bejan_grade(0.80) == "F"

    def test_all_grades_covered(self):
        """Test boundary values for all grades."""
        assert _assign_bejan_grade(0.00) == "A"
        assert _assign_bejan_grade(0.14) == "A"
        assert _assign_bejan_grade(0.15) == "B"
        assert _assign_bejan_grade(0.29) == "B"
        assert _assign_bejan_grade(0.30) == "C"
        assert _assign_bejan_grade(0.49) == "C"
        assert _assign_bejan_grade(0.50) == "D"
        assert _assign_bejan_grade(0.69) == "D"
        assert _assign_bejan_grade(0.70) == "F"
        assert _assign_bejan_grade(1.00) == "F"


# ---------------------------------------------------------------------------
# TestEntropyDecomposition
# ---------------------------------------------------------------------------

class TestEntropyDecomposition:
    """Test entropy decomposition via fraction lookup."""

    def test_fraction_sum_equals_one(self):
        """All fraction tuples must sum to 1.0."""
        for eq_type, subtypes in ENTROPY_DECOMPOSITION_FRACTIONS.items():
            for subtype, fracs in subtypes.items():
                total = sum(fracs)
                assert abs(total - 1.0) < 1e-10, (
                    f"{eq_type}/{subtype}: sum={total}"
                )

    def test_component_sum_equals_sgen(self):
        """S_gen_ht + S_gen_dp + S_gen_mix = S_gen."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {"exergy_destroyed_kW": 100.0, "exergy_in_kW": 300.0, "exergy_efficiency_pct": 66.7}
        eq = _analyze_single_equipment(item, result, 298.15)
        component_sum = eq.S_gen_heat_transfer_kW_K + eq.S_gen_pressure_drop_kW_K + eq.S_gen_mixing_kW_K
        assert abs(component_sum - eq.S_gen_kW_K) < 1e-8

    def test_compressor_dominant_pressure_drop(self):
        """Compressor should have pressure_drop as dominant mechanism."""
        item = {"id": "c1", "name": "Comp", "equipment_type": "compressor", "subtype": "screw"}
        result = {"exergy_destroyed_kW": 45.0, "exergy_in_kW": 100.0, "exergy_efficiency_pct": 55.0}
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.dominant_mechanism == "pressure_drop"

    def test_boiler_dominant_mixing(self):
        """Boiler should have mixing as dominant mechanism."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {"exergy_destroyed_kW": 100.0, "exergy_in_kW": 300.0, "exergy_efficiency_pct": 66.7}
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.dominant_mechanism == "mixing"

    def test_hx_dominant_heat_transfer(self):
        """Heat exchanger should have heat_transfer as dominant."""
        item = {"id": "hx1", "name": "HX", "equipment_type": "heat_exchanger", "subtype": "shell_tube"}
        result = {"exergy_destroyed_kW": 80.0, "exergy_in_kW": 200.0, "exergy_efficiency_pct": 60.0}
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.dominant_mechanism == "heat_transfer"

    def test_pump_dominant_pressure_drop(self):
        """Pump should have pressure_drop as dominant."""
        item = {"id": "p1", "name": "Pompa", "equipment_type": "pump", "subtype": "centrifugal"}
        result = {"exergy_destroyed_kW": 20.0, "exergy_in_kW": 50.0, "exergy_efficiency_pct": 60.0}
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.dominant_mechanism == "pressure_drop"

    def test_subtype_lookup(self):
        """Specific subtype fractions should differ from default."""
        fracs = _get_decomposition_fractions("boiler", "electric")
        assert fracs == (0.90, 0.05, 0.05)

    def test_default_fallback(self):
        """Unknown subtype should fall back to _default, then to uniform."""
        fracs = _get_decomposition_fractions("boiler", "unknown_subtype")
        assert fracs == (0.20, 0.05, 0.75)  # _default

        fracs2 = _get_decomposition_fractions("unknown_type", "unknown_subtype")
        assert fracs2 == (0.33, 0.34, 0.33)  # absolute fallback


# ---------------------------------------------------------------------------
# TestHeatTransferBejan
# ---------------------------------------------------------------------------

class TestHeatTransferBejan:
    """Test Be = S_gen,ΔT / (S_gen,ΔT + S_gen,ΔP) for heat exchangers."""

    def test_be_only_for_hx(self):
        """Be should only be calculated for heat_exchanger type."""
        hx_item = {"id": "hx1", "name": "HX", "equipment_type": "heat_exchanger", "subtype": "shell_tube"}
        hx_result = {"exergy_destroyed_kW": 80.0, "exergy_in_kW": 200.0, "exergy_efficiency_pct": 60.0}
        eq_hx = _analyze_single_equipment(hx_item, hx_result, 298.15)
        assert eq_hx.Be_heat_transfer is not None

    def test_be_range(self):
        """Be should be between 0 and 1."""
        hx_item = {"id": "hx1", "name": "HX", "equipment_type": "heat_exchanger", "subtype": "shell_tube"}
        hx_result = {"exergy_destroyed_kW": 80.0, "exergy_in_kW": 200.0, "exergy_efficiency_pct": 60.0}
        eq = _analyze_single_equipment(hx_item, hx_result, 298.15)
        assert 0 <= eq.Be_heat_transfer <= 1

    def test_non_hx_be_is_none(self):
        """Non-HX equipment should have Be = None."""
        item = {"id": "c1", "name": "Comp", "equipment_type": "compressor", "subtype": "screw"}
        result = {"exergy_destroyed_kW": 45.0, "exergy_in_kW": 100.0, "exergy_efficiency_pct": 55.0}
        eq = _analyze_single_equipment(item, result, 298.15)
        assert eq.Be_heat_transfer is None


# ---------------------------------------------------------------------------
# TestAugmentationNumber
# ---------------------------------------------------------------------------

class TestAugmentationNumber:
    """Test N_s,a = 1 - avoidable_ratio."""

    def test_augmentation_basic(self):
        """N_s,a = 1 - avoidable_ratio."""
        item = {"id": "c1", "name": "Comp", "equipment_type": "compressor", "subtype": "screw"}
        result = {
            "exergy_destroyed_kW": 45.0,
            "exergy_in_kW": 100.0,
            "exergy_efficiency_pct": 55.0,
            "avoidable_ratio_pct": 50.0,
        }
        eq = _analyze_single_equipment(item, result, 298.15)
        assert abs(eq.N_s_augmentation - 0.5) < 1e-8
        assert abs(eq.improvement_potential_pct - 50.0) < 1e-8

    def test_improvement_pct(self):
        """improvement_potential_pct = avoidable_ratio * 100."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {
            "exergy_destroyed_kW": 325.0,
            "exergy_in_kW": 500.0,
            "exergy_efficiency_pct": 35.0,
            "avoidable_ratio_pct": 40.0,
        }
        eq = _analyze_single_equipment(item, result, 298.15)
        assert abs(eq.improvement_potential_pct - 40.0) < 1e-8

    def test_missing_avoidable_defaults_to_one(self):
        """Missing avoidable_ratio → N_s,a = 1.0 (no improvement info)."""
        item = {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube"}
        result = {
            "exergy_destroyed_kW": 100.0,
            "exergy_in_kW": 300.0,
            "exergy_efficiency_pct": 66.7,
            # No avoidable_ratio_pct
        }
        eq = _analyze_single_equipment(item, result, 298.15)
        assert abs(eq.N_s_augmentation - 1.0) < 1e-8


# ---------------------------------------------------------------------------
# TestFactoryMetrics
# ---------------------------------------------------------------------------

class TestFactoryMetrics:
    """Test factory-level aggregation."""

    def test_sgen_total(self, five_equipment):
        """Total S_gen should equal sum of individual S_gen values."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)
        assert egm.is_valid
        individual_sum = sum(r.S_gen_kW_K for r in egm.equipment_results)
        assert abs(egm.S_gen_total_kW_K - individual_sum) < 1e-8

    def test_decomposition_total(self, five_equipment):
        """Decomposition totals should sum to S_gen total."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)
        decomp_sum = (
            egm.S_gen_heat_transfer_total_kW_K
            + egm.S_gen_pressure_drop_total_kW_K
            + egm.S_gen_mixing_total_kW_K
        )
        assert abs(decomp_sum - egm.S_gen_total_kW_K) < 1e-8

    def test_percentages_sum_to_100(self, five_equipment):
        """Decomposition percentages should sum to ~100%."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)
        pct_sum = egm.heat_transfer_pct + egm.pressure_drop_pct + egm.mixing_pct
        assert abs(pct_sum - 100.0) < 0.1

    def test_ns_factory_range(self, five_equipment):
        """Factory N_s should be in [0, 1]."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)
        assert 0 <= egm.N_s_factory <= 1


# ---------------------------------------------------------------------------
# TestEdgeCases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    """Test edge cases."""

    def test_single_equipment_valid(self, single_boiler):
        """EGM should work with a single equipment."""
        eq_list, results = single_boiler
        egm = analyze_entropy_generation(eq_list, results)
        assert egm.is_valid
        assert egm.num_equipment == 1

    def test_zero_exergy_in_filtered(self):
        """Equipment with zero exergy_in should be filtered out."""
        eq_list = [
            {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal", "parameters": {}},
        ]
        results = {
            "x": {"exergy_destroyed_kW": 10.0, "exergy_in_kW": 0.0, "exergy_efficiency_pct": 0.0},
        }
        egm = analyze_entropy_generation(eq_list, results)
        assert not egm.is_valid

    def test_missing_avoidable_ratio(self):
        """Equipment without avoidable_ratio should still work."""
        eq_list = [
            {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube", "parameters": {}},
        ]
        results = {
            "b1": {
                "exergy_destroyed_kW": 100.0,
                "exergy_in_kW": 300.0,
                "exergy_efficiency_pct": 66.7,
                # No avoidable data
            },
        }
        egm = analyze_entropy_generation(eq_list, results)
        assert egm.is_valid
        assert egm.equipment_results[0].N_s_augmentation == 1.0

    def test_serialization(self, five_equipment):
        """to_dict() should produce valid dict."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)
        d = egm.to_dict()
        assert isinstance(d, dict)
        assert d["is_valid"] is True
        assert len(d["equipment_results"]) == 5
        assert isinstance(d["irreversibility_ranking"], list)
        assert isinstance(d["decomposition_chart_data"], dict)
        assert isinstance(d["bejan_number_chart_data"], dict)

        # Check equipment result serialization
        eq_d = d["equipment_results"][0]
        assert "S_gen_kW_K" in eq_d
        assert "N_s" in eq_d
        assert "N_s_grade" in eq_d


# ---------------------------------------------------------------------------
# TestIntegration
# ---------------------------------------------------------------------------

class TestIntegration:
    """Integration tests."""

    def test_all_decomposition_fractions_sum_to_one(self):
        """All entries in ENTROPY_DECOMPOSITION_FRACTIONS should sum to 1.0."""
        for eq_type, subtypes in ENTROPY_DECOMPOSITION_FRACTIONS.items():
            for subtype, fracs in subtypes.items():
                total = sum(fracs)
                assert abs(total - 1.0) < 1e-10, (
                    f"ENTROPY_DECOMPOSITION_FRACTIONS[{eq_type}][{subtype}] sum={total}"
                )

    def test_analyze_factory_integration(self, five_equipment):
        """Test EGM through analyze_factory (imports test)."""
        eq_list, results = five_equipment
        feasible, reasons = check_egm_feasibility(eq_list, results)
        assert feasible
        egm = analyze_entropy_generation(eq_list, results)
        assert egm.is_valid

        # Verify Gouy-Stodola at factory level
        assert abs(egm.total_exergy_destroyed_kW - egm.S_gen_total_kW_K * egm.T0_K) < 1e-6

    def test_ranking_order(self, five_equipment):
        """Ranking should be sorted by N_s descending."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)
        ranking = egm.irreversibility_ranking
        for i in range(len(ranking) - 1):
            assert ranking[i]["N_s"] >= ranking[i + 1]["N_s"]

    def test_chart_data_consistency(self, five_equipment):
        """Chart data should have same length as equipment results."""
        eq_list, results = five_equipment
        egm = analyze_entropy_generation(eq_list, results)

        decomp = egm.decomposition_chart_data
        assert len(decomp["labels"]) == egm.num_equipment
        assert len(decomp["heat_transfer"]) == egm.num_equipment
        assert len(decomp["pressure_drop"]) == egm.num_equipment
        assert len(decomp["mixing"]) == egm.num_equipment

        bejan = egm.bejan_number_chart_data
        assert len(bejan["labels"]) == egm.num_equipment
        assert len(bejan["N_s_values"]) == egm.num_equipment
        assert len(bejan["colors"]) == egm.num_equipment
        assert len(bejan["grades"]) == egm.num_equipment

    def test_feasibility_check(self):
        """Feasibility check with no valid equipment should return False."""
        eq_list = [
            {"id": "x", "name": "X", "equipment_type": "pump", "subtype": "centrifugal", "parameters": {}},
        ]
        results = {
            "x": {"exergy_destroyed_kW": 0.0, "exergy_in_kW": 0.0, "exergy_efficiency_pct": 0.0},
        }
        feasible, reasons = check_egm_feasibility(eq_list, results)
        assert not feasible

    def test_custom_t0(self, five_equipment):
        """Custom T0 should produce different S_gen values."""
        eq_list, results = five_equipment
        egm_default = analyze_entropy_generation(eq_list, results, T0_K=298.15)
        egm_custom = analyze_entropy_generation(eq_list, results, T0_K=288.15)
        # Lower T0 → higher S_gen for same I_dot
        assert egm_custom.S_gen_total_kW_K > egm_default.S_gen_total_kW_K

    def test_none_avoidable_ratio(self):
        """avoidable_ratio_pct = None should be treated as 0."""
        eq_list = [
            {"id": "b1", "name": "Kazan", "equipment_type": "boiler", "subtype": "steam_firetube", "parameters": {}},
        ]
        results = {
            "b1": {
                "exergy_destroyed_kW": 100.0,
                "exergy_in_kW": 300.0,
                "exergy_efficiency_pct": 66.7,
                "avoidable_ratio_pct": None,
            },
        }
        egm = analyze_entropy_generation(eq_list, results)
        assert egm.is_valid
        assert egm.equipment_results[0].N_s_augmentation == 1.0
