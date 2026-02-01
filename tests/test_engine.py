"""Tests for ExergyLab engine."""

import math
import pytest

from engine.compressor import (
    CompressorInput, CompressorResult,
    PistonCompressorInput, ScrollCompressorInput, CentrifugalCompressorInput,
    analyze_compressor, analyze_piston_compressor,
    analyze_scroll_compressor, analyze_centrifugal_compressor,
    get_compressor_recommendations,
)
from engine.boiler import (
    BoilerInput, BoilerResult, analyze_boiler,
    get_boiler_recommendations, generate_boiler_sankey_data,
)
from engine.chiller import (
    ChillerInput, ChillerResult, analyze_chiller,
    get_chiller_recommendations, generate_chiller_sankey_data,
)
from engine.pump import (
    PumpInput, PumpResult, analyze_pump,
    get_pump_recommendations, generate_pump_sankey_data,
)
from engine.sankey import generate_sankey_data


# --- Screw compressor (knowledge base example 7.1) ---

class TestScrewCompressor:
    def test_basic_analysis(self):
        inp = CompressorInput(
            power_kW=32,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
            ambient_temp_C=25.0,
            operating_hours=6000,
            electricity_price_eur_kwh=0.10,
        )
        result = analyze_compressor(inp)

        assert result.exergy_in_kW == 32.0
        # Expected ~21.25 kW output from knowledge base
        assert 20.0 < result.exergy_out_kW < 23.0
        # Expected ~10.75 kW destroyed
        assert 9.0 < result.exergy_destroyed_kW < 12.0
        # Expected ~66.4% efficiency
        assert 60.0 < result.exergy_efficiency_pct < 72.0

    def test_energy_balance(self):
        inp = CompressorInput(
            power_kW=32,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
        )
        result = analyze_compressor(inp)
        # Ex_in = Ex_out + Ex_destroyed
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.01

    def test_benchmark_valid(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        assert result.benchmark_comparison in ('poor', 'below_average', 'average', 'good', 'excellent')

    def test_specific_power(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        assert abs(result.specific_power_kW_m3min - 32 / 6.2) < 0.01

    def test_annual_costs(self):
        inp = CompressorInput(
            power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5,
            operating_hours=6000, electricity_price_eur_kwh=0.10,
        )
        result = analyze_compressor(inp)
        expected_kwh = result.exergy_destroyed_kW * 6000
        assert abs(result.annual_loss_kWh - expected_kwh) < 0.01
        assert abs(result.annual_loss_EUR - expected_kwh * 0.10) < 0.01


# --- Piston compressor ---

class TestPistonCompressor:
    def test_basic_analysis(self):
        inp = PistonCompressorInput(
            power_kW=22,
            flow_rate_m3_min=3.0,
            outlet_pressure_bar=8.0,
            stages=2,
            cooling_type="air",
        )
        result = analyze_piston_compressor(inp)
        assert result.exergy_in_kW == 22.0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW > 0

    def test_energy_balance(self):
        inp = PistonCompressorInput(
            power_kW=22, flow_rate_m3_min=3.0, outlet_pressure_bar=8.0,
        )
        result = analyze_piston_compressor(inp)
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.01

    def test_benchmark_valid(self):
        inp = PistonCompressorInput(
            power_kW=22, flow_rate_m3_min=3.0, outlet_pressure_bar=8.0,
        )
        result = analyze_piston_compressor(inp)
        assert result.benchmark_comparison in ('poor', 'below_average', 'average', 'good', 'excellent')


# --- Scroll compressor ---

class TestScrollCompressor:
    def test_basic_analysis(self):
        inp = ScrollCompressorInput(
            power_kW=11,
            flow_rate_m3_min=1.5,
            outlet_pressure_bar=8.0,
            oil_free=True,
        )
        result = analyze_scroll_compressor(inp)
        assert result.exergy_in_kW == 11.0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW > 0

    def test_energy_balance(self):
        inp = ScrollCompressorInput(
            power_kW=11, flow_rate_m3_min=1.5, outlet_pressure_bar=8.0,
        )
        result = analyze_scroll_compressor(inp)
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.01


# --- Centrifugal compressor ---

class TestCentrifugalCompressor:
    def test_basic_analysis(self):
        inp = CentrifugalCompressorInput(
            power_kW=250,
            flow_rate_m3_min=45.0,
            outlet_pressure_bar=7.5,
            stages=3,
            igv_position=100.0,
        )
        result = analyze_centrifugal_compressor(inp)
        assert result.exergy_in_kW == 250.0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW > 0

    def test_energy_balance(self):
        inp = CentrifugalCompressorInput(
            power_kW=250, flow_rate_m3_min=45.0, outlet_pressure_bar=7.5,
        )
        result = analyze_centrifugal_compressor(inp)
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.01

    def test_benchmark_valid(self):
        inp = CentrifugalCompressorInput(
            power_kW=250, flow_rate_m3_min=45.0, outlet_pressure_bar=7.5,
        )
        result = analyze_centrifugal_compressor(inp)
        assert result.benchmark_comparison in ('poor', 'below_average', 'average', 'good', 'excellent')


# --- Sankey ---

class TestSankey:
    def test_structure(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        sankey = generate_sankey_data(result, "screw")

        assert "nodes" in sankey
        assert "links" in sankey
        assert "summary" in sankey
        assert len(sankey["nodes"]) == 5
        assert len(sankey["links"]) == 4

    def test_energy_balance(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        sankey = generate_sankey_data(result, "screw")

        input_link = sankey["links"][0]["value"]
        output_sum = sum(link["value"] for link in sankey["links"][1:])
        assert abs(input_link - output_sum) < 0.1

    def test_node_names(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        sankey = generate_sankey_data(result, "screw")
        node_names = [n["name"] for n in sankey["nodes"]]
        assert "Elektrik Enerjisi" in node_names
        assert "Kompresör" in node_names
        assert "Basınçlı Hava" in node_names


# --- to_api_dict ---

class TestApiDict:
    def test_output_format(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        api = result.to_api_dict("screw")

        assert "exergy_input_kW" in api
        assert "exergy_output_kW" in api
        assert "exergy_destroyed_kW" in api
        assert "exergy_efficiency_pct" in api
        assert "benchmark_percentile" in api
        assert "comparison_text" in api
        assert isinstance(api["benchmark_percentile"], int)
        assert 0 <= api["benchmark_percentile"] <= 100

    def test_values_match(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        api = result.to_api_dict("screw")

        assert api["exergy_input_kW"] == round(result.exergy_in_kW, 2)
        assert api["exergy_output_kW"] == round(result.exergy_out_kW, 2)


# --- Recommendations ---

class TestRecommendations:
    def test_returns_list(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        recs = get_compressor_recommendations(result, inp)
        assert isinstance(recs, list)
        assert len(recs) > 0

    def test_recommendation_structure(self):
        inp = CompressorInput(power_kW=32, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
        result = analyze_compressor(inp)
        recs = get_compressor_recommendations(result, inp)
        for rec in recs:
            assert "type" in rec
            assert "title" in rec
            assert "description" in rec
            assert "priority" in rec
            assert rec["priority"] in ("high", "medium", "low")


# ===========================================================================
# Boiler tests
# ===========================================================================

class TestBoiler:
    def test_basic_analysis(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
            ambient_temp_C=25.0,
        )
        result = analyze_boiler(inp)

        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW > 0
        # Boiler exergy efficiency typically 30-50%
        assert 15 < result.exergy_efficiency_pct < 60
        # Thermal efficiency typically 80-95%
        assert result.thermal_efficiency_pct is not None
        assert 50 < result.thermal_efficiency_pct < 100

    def test_energy_balance(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
        )
        result = analyze_boiler(inp)
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.1

    def test_loss_breakdown(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
        )
        result = analyze_boiler(inp)
        assert result.combustion_loss_kW is not None and result.combustion_loss_kW > 0
        assert result.flue_gas_loss_kW is not None and result.flue_gas_loss_kW >= 0
        assert result.radiation_loss_kW is not None and result.radiation_loss_kW > 0
        assert result.blowdown_loss_kW is not None and result.blowdown_loss_kW >= 0

    def test_benchmark_valid(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
        )
        result = analyze_boiler(inp)
        assert result.benchmark_comparison in ('poor', 'below_average', 'average', 'good', 'excellent')

    def test_hotwater_boiler(self):
        inp = BoilerInput(
            fuel_flow_kg_h=100,
            steam_flow_kg_h=3000,
            steam_pressure_bar=3,
            steam_temp_C=90,
            boiler_type="hotwater",
        )
        result = analyze_boiler(inp)
        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW > 0
        # Hot water boiler exergy efficiency is lower
        assert result.exergy_efficiency_pct > 0

    def test_sankey_structure(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
        )
        result = analyze_boiler(inp)
        sankey = generate_sankey_data(result, "steam_firetube")
        assert len(sankey["nodes"]) == 7
        assert len(sankey["links"]) == 6

    def test_api_dict(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
        )
        result = analyze_boiler(inp)
        api = result.to_api_dict("steam_firetube")
        assert "exergy_input_kW" in api
        assert "thermal_efficiency_pct" in api
        assert "benchmark_percentile" in api

    def test_recommendations(self):
        inp = BoilerInput(
            fuel_flow_kg_h=370,
            steam_flow_kg_h=5000,
            steam_pressure_bar=10,
        )
        result = analyze_boiler(inp)
        recs = get_boiler_recommendations(result, inp)
        assert isinstance(recs, list)


# ===========================================================================
# Chiller tests
# ===========================================================================

class TestChiller:
    def test_basic_analysis(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
            chw_supply_temp_C=7,
            chw_return_temp_C=12,
            ambient_temp_C=25.0,
        )
        result = analyze_chiller(inp)

        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW > 0
        # COP should be reasonable
        assert result.cop is not None
        assert 3.0 < result.cop < 10.0
        assert result.cop_carnot is not None
        assert result.cop_carnot > result.cop

    def test_energy_balance(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
        )
        result = analyze_chiller(inp)
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.1

    def test_kw_per_ton(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
        )
        result = analyze_chiller(inp)
        assert result.kw_per_ton is not None
        # kW/ton = 3.517 / COP -> for COP ~6, kW/ton ~ 0.58
        assert 0.3 < result.kw_per_ton < 2.0

    def test_benchmark_valid(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
        )
        result = analyze_chiller(inp)
        assert result.benchmark_comparison in ('poor', 'below_average', 'average', 'good', 'excellent')

    def test_absorption_chiller(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=5,  # solution pump
            chiller_type="absorption",
            generator_heat_kW=700,
            generator_temp_C=90,
        )
        result = analyze_chiller(inp)
        assert result.cop is not None
        assert 0.5 < result.cop < 1.5  # single-effect absorption
        assert result.exergy_in_kW > 0

    def test_sankey_structure(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
        )
        result = analyze_chiller(inp)
        sankey = generate_sankey_data(result, "centrifugal")
        assert len(sankey["nodes"]) == 5
        assert len(sankey["links"]) == 4

    def test_api_dict(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
        )
        result = analyze_chiller(inp)
        api = result.to_api_dict("centrifugal")
        assert "cop" in api
        assert "cop_carnot" in api
        assert "kw_per_ton" in api

    def test_recommendations(self):
        inp = ChillerInput(
            cooling_capacity_kW=500,
            compressor_power_kW=83,
        )
        result = analyze_chiller(inp)
        recs = get_chiller_recommendations(result, inp)
        assert isinstance(recs, list)


# ===========================================================================
# Pump tests
# ===========================================================================

class TestPump:
    def test_basic_analysis(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
            ambient_temp_C=25.0,
        )
        result = analyze_pump(inp)

        assert result.exergy_in_kW == 22.0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW > 0
        assert result.hydraulic_power_kW is not None
        assert result.hydraulic_power_kW > 0
        # Wire-to-water efficiency typically 40-80%
        assert result.wire_to_water_efficiency_pct is not None
        assert 10 < result.wire_to_water_efficiency_pct < 90

    def test_energy_balance(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
        )
        result = analyze_pump(inp)
        assert abs(result.exergy_in_kW - result.exergy_out_kW - result.exergy_destroyed_kW) < 0.1

    def test_hydraulic_power(self):
        """P_hyd = rho * g * Q * H / 1000"""
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
            fluid_density_kg_m3=1000,
        )
        result = analyze_pump(inp)
        expected = 1000 * 9.81 * (80 / 3600) * 45 / 1000
        assert abs(result.hydraulic_power_kW - expected) < 0.1

    def test_benchmark_valid(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
        )
        result = analyze_pump(inp)
        assert result.benchmark_comparison in ('poor', 'below_average', 'average', 'good', 'excellent')

    def test_throttle_loss(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
            control_method="throttle",
            throttle_loss_pct=20,
        )
        result = analyze_pump(inp)
        assert result.throttle_loss_kW is not None
        assert result.throttle_loss_kW > 0

    def test_vsd_savings(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
            control_method="throttle",
            has_vsd=False,
        )
        result = analyze_pump(inp)
        assert result.vsd_savings_potential_kW is not None
        assert result.vsd_savings_potential_kW > 0

    def test_sankey_structure(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
        )
        result = analyze_pump(inp)
        sankey = generate_sankey_data(result, "centrifugal")
        assert len(sankey["nodes"]) == 7
        assert len(sankey["links"]) == 6

    def test_api_dict(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
        )
        result = analyze_pump(inp)
        api = result.to_api_dict("centrifugal")
        assert "hydraulic_power_kW" in api
        assert "wire_to_water_efficiency_pct" in api
        assert "benchmark_percentile" in api

    def test_recommendations(self):
        inp = PumpInput(
            motor_power_kW=22,
            flow_rate_m3_h=80,
            total_head_m=45,
        )
        result = analyze_pump(inp)
        recs = get_pump_recommendations(result, inp)
        assert isinstance(recs, list)
