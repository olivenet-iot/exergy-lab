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
