"""Tests for engine/radar.py — 6-axis benchmark radar chart scoring."""

import pytest

from engine.radar import _clamp, _benchmark_to_score, _compute_heat_recovery_score, generate_radar_data


class TestClamp:
    def test_within_range(self):
        assert _clamp(50.0) == 50.0

    def test_below_min(self):
        assert _clamp(-10.0) == 0.0

    def test_above_max(self):
        assert _clamp(150.0) == 100.0

    def test_at_boundaries(self):
        assert _clamp(0.0) == 0.0
        assert _clamp(100.0) == 100.0


class TestBenchmarkToScore:
    def test_excellent(self):
        assert _benchmark_to_score("excellent") == 90

    def test_good(self):
        assert _benchmark_to_score("good") == 75

    def test_average(self):
        assert _benchmark_to_score("average") == 55

    def test_below_average(self):
        assert _benchmark_to_score("below_average") == 35

    def test_poor(self):
        assert _benchmark_to_score("poor") == 15

    def test_none(self):
        assert _benchmark_to_score(None) == 50.0

    def test_empty(self):
        assert _benchmark_to_score("") == 50.0

    def test_unknown(self):
        assert _benchmark_to_score("unknown_rating") == 50.0


class TestGenerateRadarData:
    def _make_api_dict(self, **overrides):
        base = {
            "exergy_input_kW": 100.0,
            "exergy_output_kW": 60.0,
            "exergy_destroyed_kW": 40.0,
            "exergy_efficiency_pct": 60.0,
            "avoidable_ratio_pct": 55.0,
            "benchmark_percentile": 65,
            "benchmark_comparison": "average",
            "heat_recovery_potential_kW": 20.0,
            "annual_loss_kWh": 240000.0,
        }
        base.update(overrides)
        return base

    def test_basic_structure(self):
        result = generate_radar_data(self._make_api_dict())
        assert "axes" in result
        assert "scores" in result
        assert "overall_score" in result
        assert "grade" in result
        assert "grade_letter" in result
        assert "grade_en" in result
        assert len(result["axes"]) == 6

    def test_scores_in_range(self):
        result = generate_radar_data(self._make_api_dict())
        for key, val in result["scores"].items():
            assert 0 <= val <= 100, f"{key}={val} out of range"

    def test_high_efficiency_grade(self):
        api = self._make_api_dict(
            exergy_efficiency_pct=95.0,
            avoidable_ratio_pct=5.0,
            benchmark_percentile=95,
            heat_recovery_potential_kW=38.0,
            exergy_destroyed_kW=5.0,
            exergy_input_kW=100.0,
            annual_loss_kWh=5000.0,
        )
        result = generate_radar_data(api)
        assert result["grade_letter"] in ("A", "B")

    def test_low_efficiency_grade(self):
        api = self._make_api_dict(
            exergy_efficiency_pct=10.0,
            avoidable_ratio_pct=90.0,
            benchmark_percentile=5,
            heat_recovery_potential_kW=1.0,
            exergy_destroyed_kW=90.0,
            exergy_input_kW=100.0,
            annual_loss_kWh=540000.0,
        )
        result = generate_radar_data(api)
        assert result["grade_letter"] in ("D", "F")

    def test_empty_input(self):
        result = generate_radar_data({})
        assert result["overall_score"] >= 0
        assert result["grade_letter"] in ("A", "B", "C", "D", "F")

    def test_operating_hours_effect(self):
        api = self._make_api_dict()
        r1 = generate_radar_data(api, operating_hours=6000)
        r2 = generate_radar_data(api, operating_hours=8760)
        # Different operating hours => different cost_efficiency score
        assert r1["scores"]["cost_efficiency"] != r2["scores"]["cost_efficiency"]

    def test_percentile_priority_over_comparison(self):
        api = self._make_api_dict(benchmark_percentile=80, benchmark_comparison="poor")
        result = generate_radar_data(api)
        # Percentile (80) should take priority over comparison string ("poor" => 15)
        assert result["scores"]["sector_ranking"] == 80.0

    def test_effectiveness_fallback_for_hx(self):
        """Heat exchanger uses effectiveness when no other thermal recovery field."""
        api = self._make_api_dict(effectiveness=0.75)
        # Remove compressor-specific field
        del api["heat_recovery_potential_kW"]
        result = generate_radar_data(api)
        assert result["scores"]["heat_recovery"] == 75.0


class TestAllEnginesProduceRadar:
    """Integration tests: each engine type produces valid radar data."""

    def test_compressor(self):
        from engine.compressor import CompressorInput, analyze_compressor
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        api_dict = result.to_api_dict("screw")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100
        assert radar["grade_letter"] in ("A", "B", "C", "D", "F")

    def test_boiler(self):
        from engine.boiler import BoilerInput, analyze_boiler
        inp = BoilerInput(fuel_flow_kg_h=100, steam_flow_kg_h=2000, steam_pressure_bar=10)
        result = analyze_boiler(inp)
        api_dict = result.to_api_dict("steam_firetube")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100

    def test_chiller(self):
        from engine.chiller import ChillerInput, analyze_chiller
        inp = ChillerInput(cooling_capacity_kW=350, compressor_power_kW=70)
        result = analyze_chiller(inp)
        api_dict = result.to_api_dict("screw")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100

    def test_pump(self):
        from engine.pump import PumpInput, analyze_pump
        inp = PumpInput(motor_power_kW=15, flow_rate_m3_h=50, total_head_m=40)
        result = analyze_pump(inp)
        api_dict = result.to_api_dict("centrifugal")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100

    def test_heat_exchanger(self):
        from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
        inp = HeatExchangerInput(
            hot_inlet_temp_C=90, hot_outlet_temp_C=70, hot_mass_flow_kg_s=2.0,
            cold_inlet_temp_C=20, cold_outlet_temp_C=50, cold_mass_flow_kg_s=1.5,
        )
        result = analyze_heat_exchanger(inp)
        api_dict = result.to_api_dict("shell_tube")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100

    def test_steam_turbine(self):
        from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
        inp = SteamTurbineInput(
            inlet_temp_C=400, inlet_pressure_bar=40,
            mass_flow_kg_s=5, outlet_pressure_bar=2.0,
        )
        result = analyze_steam_turbine(inp)
        api_dict = result.to_api_dict("backpressure")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100

    def test_dryer(self):
        from engine.dryer import DryerInput, analyze_dryer
        inp = DryerInput(
            product_mass_flow_kg_h=1000, moisture_in_pct=60,
            moisture_out_pct=10, supply_temp_C=200,
        )
        result = analyze_dryer(inp)
        api_dict = result.to_api_dict("rotary")
        radar = generate_radar_data(api_dict)
        assert 0 < radar["overall_score"] <= 100
