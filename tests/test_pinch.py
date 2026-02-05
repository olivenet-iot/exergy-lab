"""
Tests for the Pinch Analysis Engine.

Covers: stream extraction (7 equipment types), cascade solving,
composite curves, GCC, HEN matching, feasibility, and edge cases.
"""

import pytest
from dataclasses import dataclass
from typing import Optional

from engine.pinch import (
    ThermalStream,
    StreamType,
    TemperatureInterval,
    PinchResult,
    analyze_pinch,
    extract_thermal_streams,
    check_pinch_feasibility,
    compute_shifted_temperatures,
    create_temperature_intervals,
    solve_cascade,
    generate_composite_curves,
    generate_grand_composite_curve,
    suggest_hen_matches,
    calculate_savings,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@dataclass
class MockEquipmentItem:
    """Lightweight stand-in for engine.factory.EquipmentItem."""
    id: str
    name: str
    equipment_type: str
    subtype: str
    parameters: dict
    analysis_result: Optional[dict] = None


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def four_stream_problem():
    """
    Classic Linnhoff 4-stream problem (ΔT_min = 10°C).

    H1: 175→45°C, CP=2.0 → Q=260 kW
    H2: 150→40°C, CP=4.0 → Q=440 kW
    C1: 20→155°C, CP=3.0 → Q=405 kW
    C2: 25→112°C, CP=1.5 → Q=130.5 kW
    """
    streams = [
        ThermalStream(
            stream_id="H1", stream_type=StreamType.HOT,
            equipment_name="Hot1", equipment_type="generic",
            description="H1", T_supply_C=175.0, T_target_C=45.0,
            Q_dot_kW=260.0, CP_kW_per_K=2.0,
        ),
        ThermalStream(
            stream_id="H2", stream_type=StreamType.HOT,
            equipment_name="Hot2", equipment_type="generic",
            description="H2", T_supply_C=150.0, T_target_C=40.0,
            Q_dot_kW=440.0, CP_kW_per_K=4.0,
        ),
        ThermalStream(
            stream_id="C1", stream_type=StreamType.COLD,
            equipment_name="Cold1", equipment_type="generic",
            description="C1", T_supply_C=20.0, T_target_C=155.0,
            Q_dot_kW=405.0, CP_kW_per_K=3.0,
        ),
        ThermalStream(
            stream_id="C2", stream_type=StreamType.COLD,
            equipment_name="Cold2", equipment_type="generic",
            description="C2", T_supply_C=25.0, T_target_C=112.0,
            Q_dot_kW=130.5, CP_kW_per_K=1.5,
        ),
    ]
    return streams


@pytest.fixture
def boiler_item():
    return MockEquipmentItem(
        id="b1", name="Kazan-1", equipment_type="boiler", subtype="steam_firetube",
        parameters={
            "flue_gas_temp_C": 200,
            "feedwater_temp_C": 80,
            "steam_temp_C": 180,
            "steam_pressure_bar": 10,
        },
    )


@pytest.fixture
def boiler_result():
    return {
        "exergy_in_kW": 500,
        "exergy_out_kW": 200,
        "recoverable_heat_kW": 60,
        "flue_gas_loss_kW": 80,
        "thermal_efficiency_pct": 85,
    }


@pytest.fixture
def compressor_item():
    return MockEquipmentItem(
        id="c1", name="Kompresor-1", equipment_type="compressor", subtype="screw",
        parameters={
            "power_kW": 75,
            "inlet_temp_C": 25,
            "outlet_temp_C": 85,
        },
    )


@pytest.fixture
def compressor_result():
    return {
        "exergy_in_kW": 75,
        "exergy_out_kW": 30,
        "recoverable_heat_kW": 35,
        "exergy_destroyed_kW": 45,
    }


@pytest.fixture
def chiller_item():
    return MockEquipmentItem(
        id="ch1", name="Chiller-1", equipment_type="chiller", subtype="centrifugal",
        parameters={
            "cooling_capacity_kW": 200,
            "compressor_power_kW": 50,
            "chw_supply_temp_C": 7,
            "chw_return_temp_C": 12,
            "cw_supply_temp_C": 30,
            "cw_return_temp_C": 35,
        },
    )


@pytest.fixture
def chiller_result():
    return {
        "exergy_in_kW": 50,
        "exergy_out_kW": 15,
    }


@pytest.fixture
def heat_exchanger_item():
    return MockEquipmentItem(
        id="hx1", name="HX-1", equipment_type="heat_exchanger", subtype="shell_tube",
        parameters={
            "hot_inlet_temp_C": 120,
            "hot_outlet_temp_C": 80,
            "cold_inlet_temp_C": 30,
            "cold_outlet_temp_C": 70,
            "hot_fluid": "water",
            "cold_fluid": "water",
        },
    )


@pytest.fixture
def heat_exchanger_result():
    return {
        "exergy_in_kW": 50,
        "exergy_out_kW": 35,
        "heat_duty_kW": 100,
    }


@pytest.fixture
def steam_turbine_item():
    return MockEquipmentItem(
        id="st1", name="Turbin-1", equipment_type="steam_turbine", subtype="backpressure",
        parameters={
            "inlet_temp_C": 400,
            "outlet_temp_C": 150,
            "turbine_type": "backpressure",
            "ambient_temp_C": 25,
        },
    )


@pytest.fixture
def steam_turbine_result():
    return {
        "exergy_in_kW": 500,
        "exergy_out_kW": 300,
        "recoverable_heat_kW": 120,
        "exhaust_exergy_kW": 80,
    }


@pytest.fixture
def dryer_item():
    return MockEquipmentItem(
        id="d1", name="Kurutucu-1", equipment_type="dryer", subtype="conveyor",
        parameters={
            "air_outlet_temp_C": 80,
            "ambient_temp_C": 25,
            "product_inlet_temp_C": 25,
            "supply_temp_C": 200,
            "heat_input_kW": 300,
        },
    )


@pytest.fixture
def dryer_result():
    return {
        "exergy_in_kW": 200,
        "exergy_out_kW": 50,
        "recoverable_heat_kW": 40,
        "heat_input_kW": 300,
    }


@pytest.fixture
def pump_item():
    return MockEquipmentItem(
        id="p1", name="Pompa-1", equipment_type="pump", subtype="centrifugal",
        parameters={"motor_power_kW": 15},
    )


@pytest.fixture
def pump_result():
    return {
        "exergy_in_kW": 15,
        "exergy_out_kW": 8,
    }


# ---------------------------------------------------------------------------
# Stream Extraction Tests
# ---------------------------------------------------------------------------

class TestStreamExtraction:
    def test_boiler_produces_hot_and_cold_streams(self, boiler_item, boiler_result):
        results = {boiler_item.id: boiler_result}
        streams = extract_thermal_streams([boiler_item], results)
        hot = [s for s in streams if s.stream_type == StreamType.HOT]
        cold = [s for s in streams if s.stream_type == StreamType.COLD]
        assert len(hot) >= 1, "Boiler should produce at least 1 hot stream (flue gas)"
        assert len(cold) >= 1, "Boiler should produce at least 1 cold stream (feedwater)"

    def test_compressor_produces_hot_stream(self, compressor_item, compressor_result):
        results = {compressor_item.id: compressor_result}
        streams = extract_thermal_streams([compressor_item], results)
        hot = [s for s in streams if s.stream_type == StreamType.HOT]
        assert len(hot) >= 1, "Compressor should produce at least 1 hot stream"

    def test_chiller_produces_hot_and_cold_streams(self, chiller_item, chiller_result):
        results = {chiller_item.id: chiller_result}
        streams = extract_thermal_streams([chiller_item], results)
        hot = [s for s in streams if s.stream_type == StreamType.HOT]
        cold = [s for s in streams if s.stream_type == StreamType.COLD]
        assert len(hot) >= 1, "Chiller should produce hot stream (condenser)"
        assert len(cold) >= 1, "Chiller should produce cold stream (evaporator)"

    def test_pump_excluded_by_default(self, pump_item, pump_result):
        results = {pump_item.id: pump_result}
        streams = extract_thermal_streams([pump_item], results, include_pumps=False)
        assert len(streams) == 0, "Pumps should be excluded by default"

    def test_heat_exchanger_produces_both_streams(self, heat_exchanger_item, heat_exchanger_result):
        results = {heat_exchanger_item.id: heat_exchanger_result}
        streams = extract_thermal_streams([heat_exchanger_item], results)
        hot = [s for s in streams if s.stream_type == StreamType.HOT]
        cold = [s for s in streams if s.stream_type == StreamType.COLD]
        assert len(hot) >= 1, "HX should produce hot stream"
        assert len(cold) >= 1, "HX should produce cold stream"

    def test_steam_turbine_produces_hot_stream(self, steam_turbine_item, steam_turbine_result):
        results = {steam_turbine_item.id: steam_turbine_result}
        streams = extract_thermal_streams([steam_turbine_item], results)
        hot = [s for s in streams if s.stream_type == StreamType.HOT]
        assert len(hot) >= 1, "Steam turbine should produce hot stream (exhaust)"

    def test_dryer_produces_hot_and_cold_streams(self, dryer_item, dryer_result):
        results = {dryer_item.id: dryer_result}
        streams = extract_thermal_streams([dryer_item], results)
        hot = [s for s in streams if s.stream_type == StreamType.HOT]
        cold = [s for s in streams if s.stream_type == StreamType.COLD]
        assert len(hot) >= 1, "Dryer should produce hot stream (exhaust)"
        assert len(cold) >= 1, "Dryer should produce cold stream (drying load)"

    def test_minimum_Q_filter(self):
        """Streams with Q < 5 kW should be filtered out."""
        item = MockEquipmentItem(
            id="c_small", name="SmallComp", equipment_type="compressor", subtype="screw",
            parameters={"outlet_temp_C": 80, "inlet_temp_C": 25},
        )
        result = {"recoverable_heat_kW": 3.0, "exergy_destroyed_kW": 2.0}
        streams = extract_thermal_streams([item], {item.id: result})
        assert len(streams) == 0, "Streams with Q < 5 kW should be excluded"

    def test_minimum_deltaT_filter(self):
        """Streams with |ΔT| < 2°C should be filtered out."""
        item = MockEquipmentItem(
            id="hx_small", name="SmallHX", equipment_type="heat_exchanger", subtype="plate",
            parameters={
                "hot_inlet_temp_C": 50, "hot_outlet_temp_C": 49,
                "cold_inlet_temp_C": 30, "cold_outlet_temp_C": 31,
            },
        )
        result = {"heat_duty_kW": 100}
        streams = extract_thermal_streams([item], {item.id: result})
        assert len(streams) == 0, "Streams with ΔT < 2°C should be excluded"

    def test_missing_result_skipped(self, boiler_item):
        """Equipment with no result should be skipped."""
        streams = extract_thermal_streams([boiler_item], {})
        assert len(streams) == 0


# ---------------------------------------------------------------------------
# Classic Pinch Calculation Tests
# ---------------------------------------------------------------------------

class TestClassicPinchCalculation:
    def test_shifted_temperatures_sorted_unique(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        assert shifted == sorted(shifted, reverse=True), "Shifted temps must be descending"
        assert len(shifted) == len(set(shifted)), "Shifted temps must be unique"

    def test_energy_balance(self, four_stream_problem):
        """QH_min + ΣQ_hot ≈ QC_min + ΣQ_cold (energy balance invariant)."""
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        QH_min, QC_min, _, _ = solve_cascade(intervals)

        total_Q_hot = sum(s.Q_dot_kW for s in four_stream_problem if s.stream_type == StreamType.HOT)
        total_Q_cold = sum(s.Q_dot_kW for s in four_stream_problem if s.stream_type == StreamType.COLD)

        lhs = QH_min + total_Q_hot
        rhs = QC_min + total_Q_cold

        assert abs(lhs - rhs) < 0.5, f"Energy balance violated: {lhs:.2f} != {rhs:.2f}"

    def test_QH_min_non_negative(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        QH_min, _, _, _ = solve_cascade(intervals)
        assert QH_min >= 0, "QH_min must be non-negative"

    def test_QC_min_non_negative(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        _, QC_min, _, _ = solve_cascade(intervals)
        assert QC_min >= 0, "QC_min must be non-negative"

    def test_cascade_all_non_negative(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        _, _, _, cascade = solve_cascade(intervals)
        for i, val in enumerate(cascade):
            assert val >= -0.01, f"Corrected cascade[{i}] = {val:.2f} is negative"


# ---------------------------------------------------------------------------
# Composite Curve Tests
# ---------------------------------------------------------------------------

class TestCompositeCurves:
    def test_hot_curve_descending_temperature(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        QH_min, _, _, _ = solve_cascade(intervals)

        cc = generate_composite_curves(four_stream_problem, QH_min)
        hot_T = cc["hot_curve"]["T_C"]
        # Hot composite should have generally descending temperature with increasing H
        assert hot_T[0] >= hot_T[-1], "Hot curve should start at high T and end at low T"

    def test_cold_curve_ascending_temperature(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        QH_min, _, _, _ = solve_cascade(intervals)

        cc = generate_composite_curves(four_stream_problem, QH_min)
        cold_T = cc["cold_curve"]["T_C"]
        assert cold_T[-1] >= cold_T[0], "Cold curve should end at high T"

    def test_curves_structure(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        QH_min, _, _, _ = solve_cascade(intervals)

        cc = generate_composite_curves(four_stream_problem, QH_min)
        assert "hot_curve" in cc
        assert "cold_curve" in cc
        assert "H_kW" in cc["hot_curve"]
        assert "T_C" in cc["hot_curve"]
        assert "QH_min_kW" in cc


# ---------------------------------------------------------------------------
# Grand Composite Curve Tests
# ---------------------------------------------------------------------------

class TestGrandCompositeCurve:
    def test_gcc_touches_zero_at_pinch(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        _, _, pinch_T, cascade = solve_cascade(intervals)

        gcc = generate_grand_composite_curve(intervals, cascade)
        # At least one H value should be near zero (pinch point)
        min_H = min(abs(h) for h in gcc["H_kW"])
        assert min_H < 1.0, f"GCC should touch zero at pinch, min |H| = {min_H:.2f}"

    def test_gcc_structure(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        _, _, _, cascade = solve_cascade(intervals)

        gcc = generate_grand_composite_curve(intervals, cascade)
        assert "H_kW" in gcc
        assert "T_shifted_C" in gcc
        assert len(gcc["H_kW"]) == len(gcc["T_shifted_C"])
        assert len(gcc["H_kW"]) > 0


# ---------------------------------------------------------------------------
# HEN Matching Tests
# ---------------------------------------------------------------------------

class TestHENMatches:
    def test_matches_respect_delta_T_min(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        _, _, pinch_T, _ = solve_cascade(intervals)

        matches = suggest_hen_matches(four_stream_problem, pinch_T, 10.0)
        for m in matches:
            dt = m["T_hot_supply_C"] - m["T_cold_target_C"]
            assert dt >= 10.0 - 0.1, (
                f"Match {m['hot_stream']}→{m['cold_stream']}: ΔT={dt:.1f} < ΔT_min"
            )

    def test_total_matched_Q_leq_max_recovery(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        QH_min, QC_min, pinch_T, _ = solve_cascade(intervals)

        total_Q_hot = sum(s.Q_dot_kW for s in four_stream_problem if s.stream_type == StreamType.HOT)
        max_recovery = total_Q_hot - QC_min

        matches = suggest_hen_matches(four_stream_problem, pinch_T, 10.0)
        total_matched = sum(m["Q_exchange_kW"] for m in matches)
        assert total_matched <= max_recovery + 1.0, (
            f"Total matched Q ({total_matched:.1f}) exceeds max recovery ({max_recovery:.1f})"
        )

    def test_matches_have_required_fields(self, four_stream_problem):
        shifted = compute_shifted_temperatures(four_stream_problem, 10.0)
        intervals = create_temperature_intervals(four_stream_problem, shifted, 10.0)
        _, _, pinch_T, _ = solve_cascade(intervals)

        matches = suggest_hen_matches(four_stream_problem, pinch_T, 10.0)
        for m in matches:
            assert "hot_stream" in m
            assert "cold_stream" in m
            assert "Q_exchange_kW" in m
            assert "region" in m
            assert "description" in m


# ---------------------------------------------------------------------------
# Edge Case Tests
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_single_hot_single_cold(self):
        """Minimal case: one hot, one cold stream."""
        streams = [
            ThermalStream(
                stream_id="H1", stream_type=StreamType.HOT,
                equipment_name="Hot", equipment_type="generic",
                description="H1", T_supply_C=100.0, T_target_C=40.0,
                Q_dot_kW=120.0, CP_kW_per_K=2.0,
            ),
            ThermalStream(
                stream_id="C1", stream_type=StreamType.COLD,
                equipment_name="Cold", equipment_type="generic",
                description="C1", T_supply_C=20.0, T_target_C=80.0,
                Q_dot_kW=90.0, CP_kW_per_K=1.5,
            ),
        ]
        shifted = compute_shifted_temperatures(streams, 10.0)
        intervals = create_temperature_intervals(streams, shifted, 10.0)
        QH_min, QC_min, _, cascade = solve_cascade(intervals)

        assert QH_min >= 0
        assert QC_min >= 0
        # Energy balance
        total_hot = 120.0
        total_cold = 90.0
        assert abs((QH_min + total_hot) - (QC_min + total_cold)) < 0.5

    def test_no_hot_streams_returns_invalid(self):
        """No hot streams → invalid result."""
        items = [MockEquipmentItem(
            id="ch1", name="Chiller", equipment_type="chiller", subtype="centrifugal",
            parameters={"chw_supply_temp_C": 7, "chw_return_temp_C": 12, "cooling_capacity_kW": 200, "compressor_power_kW": 0},
        )]
        # Only cold stream possible if condenser Q = 0
        # Actually we force no hot by giving 0 condenser
        result = analyze_pinch(items, {items[0].id: {"exergy_in_kW": 0}})
        assert result.is_valid is False

    def test_no_cold_streams_returns_invalid(self):
        """No cold streams → invalid result."""
        items = [MockEquipmentItem(
            id="c1", name="Comp", equipment_type="compressor", subtype="screw",
            parameters={"outlet_temp_C": 80, "inlet_temp_C": 25},
        )]
        result = analyze_pinch(
            items,
            {items[0].id: {"recoverable_heat_kW": 50, "exergy_destroyed_kW": 30}},
        )
        assert result.is_valid is False

    def test_identical_temperatures_no_crash(self):
        """Streams with same supply/target temp should not crash."""
        streams = [
            ThermalStream(
                stream_id="H1", stream_type=StreamType.HOT,
                equipment_name="H", equipment_type="generic",
                description="H1", T_supply_C=80.0, T_target_C=80.0,
                Q_dot_kW=100.0, CP_kW_per_K=0.0,
            ),
        ]
        shifted = compute_shifted_temperatures(streams, 10.0)
        # Should have at most one temp, so no intervals
        intervals = create_temperature_intervals(streams, shifted, 10.0)
        assert len(intervals) == 0

    def test_very_large_delta_T_min(self):
        """Very large ΔT_min should still produce valid (possibly zero recovery) result."""
        streams = [
            ThermalStream(
                stream_id="H1", stream_type=StreamType.HOT,
                equipment_name="Hot", equipment_type="generic",
                description="H1", T_supply_C=100.0, T_target_C=40.0,
                Q_dot_kW=100.0, CP_kW_per_K=100.0 / 60.0,
            ),
            ThermalStream(
                stream_id="C1", stream_type=StreamType.COLD,
                equipment_name="Cold", equipment_type="generic",
                description="C1", T_supply_C=20.0, T_target_C=80.0,
                Q_dot_kW=90.0, CP_kW_per_K=90.0 / 60.0,
            ),
        ]
        shifted = compute_shifted_temperatures(streams, 200.0)
        intervals = create_temperature_intervals(streams, shifted, 200.0)
        QH_min, QC_min, _, _ = solve_cascade(intervals)
        # With very large ΔT_min, recovery approaches zero
        assert QH_min >= 0
        assert QC_min >= 0


# ---------------------------------------------------------------------------
# Feasibility Tests
# ---------------------------------------------------------------------------

class TestFeasibility:
    def test_feasible_with_hot_and_cold(self, four_stream_problem):
        feasible, msg = check_pinch_feasibility(four_stream_problem)
        assert feasible is True
        assert msg == ""

    def test_not_feasible_empty(self):
        feasible, msg = check_pinch_feasibility([])
        assert feasible is False

    def test_not_feasible_only_hot(self):
        streams = [
            ThermalStream(
                stream_id="H1", stream_type=StreamType.HOT,
                equipment_name="Hot", equipment_type="generic",
                description="H1", T_supply_C=100, T_target_C=40,
                Q_dot_kW=100, CP_kW_per_K=100 / 60,
            ),
        ]
        feasible, msg = check_pinch_feasibility(streams)
        assert feasible is False
        assert "Soguk" in msg


# ---------------------------------------------------------------------------
# PinchResult Serialization Tests
# ---------------------------------------------------------------------------

class TestPinchResultSerialization:
    def test_to_dict_has_all_keys(self):
        r = PinchResult()
        d = r.to_dict()
        assert "is_valid" in d
        assert "streams" in d
        assert "QH_min_kW" in d
        assert "QC_min_kW" in d
        assert "composite_curves" in d
        assert "grand_composite_curve" in d
        assert "hen_matches" in d

    def test_to_dict_roundtrip(self, four_stream_problem):
        """Full analyze_pinch → to_dict should produce valid JSON-serializable dict."""
        import json

        # Create mock equipment for analyze_pinch
        items = [
            MockEquipmentItem(id="b1", name="Kazan", equipment_type="boiler", subtype="steam_firetube",
                              parameters={"flue_gas_temp_C": 200, "feedwater_temp_C": 80, "steam_temp_C": 180}),
            MockEquipmentItem(id="c1", name="Kompresor", equipment_type="compressor", subtype="screw",
                              parameters={"outlet_temp_C": 85, "inlet_temp_C": 25}),
            MockEquipmentItem(id="hx1", name="HX", equipment_type="heat_exchanger", subtype="shell_tube",
                              parameters={"hot_inlet_temp_C": 120, "hot_outlet_temp_C": 80,
                                          "cold_inlet_temp_C": 30, "cold_outlet_temp_C": 70}),
        ]
        results = {
            "b1": {"exergy_in_kW": 500, "recoverable_heat_kW": 60, "thermal_efficiency_pct": 85, "flue_gas_loss_kW": 80},
            "c1": {"recoverable_heat_kW": 35, "exergy_destroyed_kW": 45},
            "hx1": {"heat_duty_kW": 100, "exergy_in_kW": 50, "exergy_out_kW": 35},
        }

        pinch = analyze_pinch(items, results)
        d = pinch.to_dict()

        # Should be JSON serializable
        json_str = json.dumps(d)
        assert len(json_str) > 0


# ---------------------------------------------------------------------------
# Savings Calculation Tests
# ---------------------------------------------------------------------------

class TestSavingsCalculation:
    def test_savings_positive_when_excess(self):
        result = calculate_savings(
            QH_min_kW=100, QC_min_kW=50,
            QH_current_kW=200, QC_current_kW=100,
            fuel_price_eur_kwh=0.08, operating_hours=8000,
        )
        assert result["QH_excess_kW"] == 100
        assert result["annual_savings_kWh"] == 800_000
        assert result["annual_savings_EUR"] == 64_000

    def test_savings_zero_when_no_excess(self):
        result = calculate_savings(
            QH_min_kW=200, QC_min_kW=100,
            QH_current_kW=150, QC_current_kW=80,
            fuel_price_eur_kwh=0.08, operating_hours=8000,
        )
        assert result["QH_excess_kW"] == 0
        assert result["annual_savings_EUR"] == 0


# ---------------------------------------------------------------------------
# Full Integration Test
# ---------------------------------------------------------------------------

class TestFullIntegration:
    def test_analyze_pinch_with_mixed_equipment(self):
        """Test full analysis with boiler + compressor + HX."""
        items = [
            MockEquipmentItem(id="b1", name="Kazan-1", equipment_type="boiler", subtype="steam_firetube",
                              parameters={"flue_gas_temp_C": 200, "feedwater_temp_C": 80, "steam_temp_C": 180}),
            MockEquipmentItem(id="c1", name="Kompresor-1", equipment_type="compressor", subtype="screw",
                              parameters={"outlet_temp_C": 85, "inlet_temp_C": 25}),
            MockEquipmentItem(id="hx1", name="HX-1", equipment_type="heat_exchanger", subtype="shell_tube",
                              parameters={"hot_inlet_temp_C": 120, "hot_outlet_temp_C": 80,
                                          "cold_inlet_temp_C": 30, "cold_outlet_temp_C": 70}),
        ]
        results = {
            "b1": {"exergy_in_kW": 500, "recoverable_heat_kW": 60, "thermal_efficiency_pct": 85, "flue_gas_loss_kW": 80},
            "c1": {"recoverable_heat_kW": 35, "exergy_destroyed_kW": 45},
            "hx1": {"heat_duty_kW": 100, "exergy_in_kW": 50, "exergy_out_kW": 35},
        }

        pinch = analyze_pinch(items, results, delta_T_min_C=10)
        assert pinch.is_valid is True
        assert pinch.hot_stream_count >= 2
        assert pinch.cold_stream_count >= 1
        assert pinch.QH_min_kW >= 0
        assert pinch.QC_min_kW >= 0
        assert pinch.composite_curves is not None
        assert pinch.grand_composite_curve is not None
