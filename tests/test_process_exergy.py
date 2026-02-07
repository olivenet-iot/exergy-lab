"""Tests for engine/process_exergy.py — minimum exergy calculations."""

import math

import pytest

from engine.process_exergy import (
    ProcessDefinition,
    SUPPORTED_PROCESS_TYPES,
    get_process_types,
    get_subcategories,
    calculate_minimum_exergy,
)


# ---------------------------------------------------------------------------
# ProcessDefinition & SUPPORTED_PROCESS_TYPES
# ---------------------------------------------------------------------------

class TestProcessTypes:

    def test_all_8_types_registered(self):
        expected = {
            "drying", "heating", "cooling", "steam_generation",
            "compressed_air", "chp", "cold_storage", "general_manufacturing",
        }
        assert set(SUPPORTED_PROCESS_TYPES.keys()) == expected

    def test_get_process_types_returns_dict(self):
        result = get_process_types()
        assert isinstance(result, dict)
        assert len(result) == 8

    def test_each_type_has_required_fields(self):
        required = {"label", "label_en", "icon", "description",
                    "required_params", "optional_params",
                    "param_definitions", "subcategories"}
        for ptype, info in SUPPORTED_PROCESS_TYPES.items():
            missing = required - set(info.keys())
            assert not missing, f"{ptype} missing: {missing}"

    def test_get_subcategories(self):
        result = get_subcategories("drying")
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_missing_param_raises(self):
        proc = ProcessDefinition(
            process_type="drying",
            process_label="Test",
            parameters={"mass_flow_kg_h": 100},  # missing moisture_in_pct, moisture_out_pct
        )
        with pytest.raises(ValueError, match="Eksik parametre"):
            calculate_minimum_exergy(proc)

    def test_unsupported_type_raises(self):
        proc = ProcessDefinition(
            process_type="nuclear_fusion",
            process_label="Test",
            parameters={},
        )
        with pytest.raises(ValueError, match="Desteklenmeyen proses tipi"):
            calculate_minimum_exergy(proc)

    def test_all_types_produce_positive_result(self):
        """Every process type with valid params produces positive minimum exergy."""
        test_params = {
            "drying": {"mass_flow_kg_h": 1000, "moisture_in_pct": 30, "moisture_out_pct": 5},
            "heating": {"mass_flow_kg_h": 1000, "temp_in_C": 20, "temp_out_C": 80},
            "cooling": {"cooling_load_kW": 100, "cold_temp_C": -10},
            "steam_generation": {"steam_flow_kg_h": 1000, "steam_pressure_bar": 10},
            "compressed_air": {"air_flow_m3_min": 10, "discharge_pressure_bar": 7},
            "chp": {"fuel_input_kW": 1000, "electrical_output_kW": 350, "thermal_output_kW": 400},
            "cold_storage": {"heat_load_kW": 50, "target_temp_C": -20},
            "general_manufacturing": {"production_rate_ton_h": 5},
        }
        for ptype, params in test_params.items():
            proc = ProcessDefinition(process_type=ptype, process_label=f"Test {ptype}", parameters=params)
            result = calculate_minimum_exergy(proc)
            assert result["minimum_exergy_kW"] > 0, f"{ptype}: expected positive minimum exergy"
            assert result["calculation_method"], f"{ptype}: missing calculation_method"

    def test_result_structure(self):
        """Every result has the required keys."""
        required_keys = {
            "minimum_exergy_kW", "calculation_method", "assumptions",
            "breakdown", "specific_unit", "specific_minimum", "production_rate_unit",
        }
        proc = ProcessDefinition(
            process_type="heating",
            process_label="Test",
            parameters={"mass_flow_kg_h": 500, "temp_in_C": 20, "temp_out_C": 60},
        )
        result = calculate_minimum_exergy(proc)
        missing = required_keys - set(result.keys())
        assert not missing, f"Missing keys: {missing}"


# ---------------------------------------------------------------------------
# Drying tests
# ---------------------------------------------------------------------------

class TestMinExergyDrying:

    def test_basic_drying(self):
        proc = ProcessDefinition(
            process_type="drying", process_label="Grain",
            parameters={"mass_flow_kg_h": 1000, "moisture_in_pct": 20, "moisture_out_pct": 5},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0
        assert result["specific_unit"] == "kWh/kg su"

    def test_no_drying_needed(self):
        proc = ProcessDefinition(
            process_type="drying", process_label="No dry",
            parameters={"mass_flow_kg_h": 1000, "moisture_in_pct": 5, "moisture_out_pct": 20},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] == 0.0

    def test_water_removed_calculation(self):
        proc = ProcessDefinition(
            process_type="drying", process_label="Water check",
            parameters={"mass_flow_kg_h": 1000, "moisture_in_pct": 50, "moisture_out_pct": 10},
        )
        result = calculate_minimum_exergy(proc)
        # 1000 kg/h at 50% moisture → 500 kg dry, 500 kg water
        # At 10% moisture → 500 / (1-0.1) ≈ 555.56 kg total, water = 55.56 kg
        # Removed ≈ 500 - 55.56 ≈ 444.44 kg/h
        assert "water_removed_kg_h" in result
        assert result["water_removed_kg_h"] > 400

    def test_with_heating(self):
        """Heating adds extra exergy."""
        params_no_heat = {"mass_flow_kg_h": 1000, "moisture_in_pct": 20, "moisture_out_pct": 5}
        params_heat = {
            **params_no_heat,
            "material_inlet_temp_C": 20, "material_outlet_temp_C": 80,
        }
        proc_no = ProcessDefinition(process_type="drying", process_label="No heat", parameters=params_no_heat)
        proc_yes = ProcessDefinition(process_type="drying", process_label="Heat", parameters=params_heat)
        r_no = calculate_minimum_exergy(proc_no)
        r_yes = calculate_minimum_exergy(proc_yes)
        assert r_yes["minimum_exergy_kW"] > r_no["minimum_exergy_kW"]


# ---------------------------------------------------------------------------
# Heating tests
# ---------------------------------------------------------------------------

class TestMinExergyHeating:

    def test_carnot_factor(self):
        proc = ProcessDefinition(
            process_type="heating", process_label="Water heating",
            parameters={"mass_flow_kg_h": 1000, "temp_in_C": 20, "temp_out_C": 80},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0
        assert "carnot_factor" in result
        assert 0 < result["carnot_factor"] < 1

    def test_no_heating(self):
        proc = ProcessDefinition(
            process_type="heating", process_label="No heat",
            parameters={"mass_flow_kg_h": 1000, "temp_in_C": 80, "temp_out_C": 20},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] == 0.0

    def test_higher_temp_more_exergy(self):
        params_low = {"mass_flow_kg_h": 1000, "temp_in_C": 20, "temp_out_C": 60}
        params_high = {"mass_flow_kg_h": 1000, "temp_in_C": 20, "temp_out_C": 120}
        r_low = calculate_minimum_exergy(ProcessDefinition("heating", "Low", params_low))
        r_high = calculate_minimum_exergy(ProcessDefinition("heating", "High", params_high))
        assert r_high["minimum_exergy_kW"] > r_low["minimum_exergy_kW"]


# ---------------------------------------------------------------------------
# Cooling tests
# ---------------------------------------------------------------------------

class TestMinExergyCooling:

    def test_cop_carnot(self):
        proc = ProcessDefinition(
            process_type="cooling", process_label="Cooling",
            parameters={"cooling_load_kW": 100, "cold_temp_C": -20},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0
        assert "COP_carnot" in result
        assert result["COP_carnot"] > 0

    def test_no_cooling_needed(self):
        proc = ProcessDefinition(
            process_type="cooling", process_label="Warm",
            parameters={"cooling_load_kW": 100, "cold_temp_C": 30},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] == 0.0

    def test_lower_temp_more_exergy(self):
        r_warm = calculate_minimum_exergy(ProcessDefinition(
            "cooling", "W", {"cooling_load_kW": 100, "cold_temp_C": 5}))
        r_cold = calculate_minimum_exergy(ProcessDefinition(
            "cooling", "C", {"cooling_load_kW": 100, "cold_temp_C": -30}))
        assert r_cold["minimum_exergy_kW"] > r_warm["minimum_exergy_kW"]


# ---------------------------------------------------------------------------
# Steam tests
# ---------------------------------------------------------------------------

class TestMinExergySteam:

    def test_saturated_steam(self):
        proc = ProcessDefinition(
            process_type="steam_generation", process_label="Steam",
            parameters={"steam_flow_kg_h": 1000, "steam_pressure_bar": 10},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0
        # Reasonable range for 10 bar steam
        specific_kJ_kg = result["minimum_exergy_kW"] * 3600 / 1000
        assert 100 < specific_kJ_kg < 1200

    def test_higher_pressure_more_exergy(self):
        r_low = calculate_minimum_exergy(ProcessDefinition(
            "steam_generation", "Low", {"steam_flow_kg_h": 1000, "steam_pressure_bar": 3}))
        r_high = calculate_minimum_exergy(ProcessDefinition(
            "steam_generation", "High", {"steam_flow_kg_h": 1000, "steam_pressure_bar": 30}))
        assert r_high["minimum_exergy_kW"] > r_low["minimum_exergy_kW"]

    def test_steam_result_has_method(self):
        proc = ProcessDefinition(
            process_type="steam_generation", process_label="Steam",
            parameters={"steam_flow_kg_h": 500, "steam_pressure_bar": 5},
        )
        result = calculate_minimum_exergy(proc)
        assert result["calculation_method"]  # non-empty string


# ---------------------------------------------------------------------------
# Compressed Air tests
# ---------------------------------------------------------------------------

class TestMinExergyCompressedAir:

    def test_isothermal_work(self):
        proc = ProcessDefinition(
            process_type="compressed_air", process_label="Air",
            parameters={"air_flow_m3_min": 10, "discharge_pressure_bar": 7},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0

    def test_pressure_ratio(self):
        """Higher pressure → more exergy."""
        r_low = calculate_minimum_exergy(ProcessDefinition(
            "compressed_air", "Low", {"air_flow_m3_min": 10, "discharge_pressure_bar": 3}))
        r_high = calculate_minimum_exergy(ProcessDefinition(
            "compressed_air", "High", {"air_flow_m3_min": 10, "discharge_pressure_bar": 10}))
        assert r_high["minimum_exergy_kW"] > r_low["minimum_exergy_kW"]

    def test_isothermal_formula_check(self):
        """Verify against manual isothermal calculation."""
        Q_m3_min = 10
        P2_bar = 7
        T0_K = 298.15
        P1_bar = 1.01325

        rho = 101325 / (287 * 293.15)
        m_dot = Q_m3_min * rho / 60
        W_expected = m_dot * 287 * T0_K * math.log(P2_bar / P1_bar) / 1000

        proc = ProcessDefinition(
            "compressed_air", "Check",
            {"air_flow_m3_min": Q_m3_min, "discharge_pressure_bar": P2_bar},
        )
        result = calculate_minimum_exergy(proc)
        assert abs(result["minimum_exergy_kW"] - W_expected) < 0.1


# ---------------------------------------------------------------------------
# CHP tests
# ---------------------------------------------------------------------------

class TestMinExergyCHP:

    def test_combined_output(self):
        proc = ProcessDefinition(
            process_type="chp", process_label="CHP",
            parameters={"fuel_input_kW": 1000, "electrical_output_kW": 350, "thermal_output_kW": 400},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0
        # Electrical exergy = 350 kW (pure work)
        # Thermal exergy = 400 × (1 - 298.15/363.15) < 400
        assert result["minimum_exergy_kW"] >= 350  # at least the electrical part

    def test_fuel_exergy_factor(self):
        proc = ProcessDefinition(
            process_type="chp", process_label="CHP",
            parameters={"fuel_input_kW": 1000, "electrical_output_kW": 0, "thermal_output_kW": 0},
        )
        result = calculate_minimum_exergy(proc)
        assert result["fuel_exergy_kW"] == 1040  # 1000 × 1.04


# ---------------------------------------------------------------------------
# Cold Storage tests
# ---------------------------------------------------------------------------

class TestMinExergyColdStorage:

    def test_cold_storage(self):
        proc = ProcessDefinition(
            process_type="cold_storage", process_label="Cold",
            parameters={"heat_load_kW": 50, "target_temp_C": -20},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0
        assert "COP_carnot" in result

    def test_no_cooling_warm_target(self):
        proc = ProcessDefinition(
            process_type="cold_storage", process_label="Warm",
            parameters={"heat_load_kW": 50, "target_temp_C": 30},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] == 0.0


# ---------------------------------------------------------------------------
# General Manufacturing tests
# ---------------------------------------------------------------------------

class TestMinExergyGeneral:

    def test_general_manufacturing(self):
        proc = ProcessDefinition(
            process_type="general_manufacturing", process_label="Cement",
            parameters={"production_rate_ton_h": 5},
        )
        result = calculate_minimum_exergy(proc)
        assert result["minimum_exergy_kW"] > 0

    def test_different_sectors(self):
        """Different sector_subcategory gives different results."""
        r_cement = calculate_minimum_exergy(ProcessDefinition(
            "general_manufacturing", "Cement",
            {"production_rate_ton_h": 1, "sector_subcategory": "cement"}))
        r_paper = calculate_minimum_exergy(ProcessDefinition(
            "general_manufacturing", "Paper",
            {"production_rate_ton_h": 1, "sector_subcategory": "paper"}))
        # Cement has higher BAT than paper
        assert r_cement["minimum_exergy_kW"] != r_paper["minimum_exergy_kW"]
