"""Isı eşanjörü engine testleri"""
import pytest
import math
from engine.heat_exchanger import (
    HeatExchangerInput, HeatExchangerResult,
    analyze_heat_exchanger, get_heat_exchanger_recommendations,
    generate_heat_exchanger_sankey_data,
    FLUID_CP
)
from engine.core import DeadState


class TestHeatExchangerInput:
    """HeatExchangerInput testleri"""

    def test_default_values(self):
        inp = HeatExchangerInput()
        assert inp.hot_fluid == 'water'
        assert inp.cold_fluid == 'water'
        assert inp.hx_type == 'shell_tube'
        assert inp.heat_duty_kW is not None

    def test_heat_duty_auto_calculation(self):
        inp = HeatExchangerInput(
            hot_fluid='water',
            hot_inlet_temp_C=90,
            hot_outlet_temp_C=70,
            hot_mass_flow_kg_s=2.0,
        )
        expected = 2.0 * 4.18 * 20
        assert abs(inp.heat_duty_kW - expected) < 0.1

    def test_custom_heat_duty(self):
        inp = HeatExchangerInput(heat_duty_kW=500.0)
        assert inp.heat_duty_kW == 500.0


class TestAnalyzeHeatExchanger:
    """analyze_heat_exchanger testleri"""

    def test_basic_analysis(self):
        inp = HeatExchangerInput(
            hot_inlet_temp_C=90, hot_outlet_temp_C=70,
            hot_mass_flow_kg_s=2.0,
            cold_inlet_temp_C=20, cold_outlet_temp_C=50,
            cold_mass_flow_kg_s=2.5,
        )
        result = analyze_heat_exchanger(inp)
        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW > 0
        assert result.exergy_destroyed_kW >= 0
        assert 0 < result.exergy_efficiency_pct <= 100
        assert result.heat_duty_kW > 0
        assert result.lmtd_K > 0

    def test_exergy_balance(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        balance = abs(result.exergy_destroyed_kW - (result.exergy_in_kW - result.exergy_out_kW))
        assert balance < 0.01

    def test_effectiveness_range(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        assert 0 <= result.effectiveness <= 1.0

    def test_bejan_number_range(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        assert 0 <= result.bejan_number <= 1.0

    def test_entropy_decomposition(self):
        inp = HeatExchangerInput(
            hot_fluid='air', cold_fluid='air',
            hot_pressure_drop_kPa=5.0, cold_pressure_drop_kPa=8.0,
        )
        result = analyze_heat_exchanger(inp)
        assert result.entropy_gen_heat_transfer_kW_K >= 0
        assert result.entropy_gen_pressure_drop_kW_K >= 0
        total = result.entropy_gen_heat_transfer_kW_K + result.entropy_gen_pressure_drop_kW_K
        assert abs(result.entropy_gen_total_kW_K - total) < 0.001

    def test_fouling_indicator(self):
        inp = HeatExchangerInput(heat_duty_kW=100, design_heat_duty_kW=200)
        result = analyze_heat_exchanger(inp)
        assert result.fouling_indicator == 'severe'

    def test_different_fluids(self):
        for fluid in FLUID_CP.keys():
            inp = HeatExchangerInput(hot_fluid=fluid)
            result = analyze_heat_exchanger(inp)
            assert result.exergy_in_kW > 0

    def test_plate_type(self):
        inp = HeatExchangerInput(hx_type='plate')
        result = analyze_heat_exchanger(inp)
        assert result.benchmark_comparison is not None

    def test_to_api_dict(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        d = result.to_api_dict()
        assert 'heat_duty_kW' in d
        assert 'bejan_number' in d
        assert 'lmtd_K' in d
        assert 'benchmark_percentile' in d
        assert 'comparison_text' in d

    def test_to_dict(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        d = result.to_dict()
        assert 'exergy_in_kW' in d
        assert 'heat_duty_kW' in d
        assert 'bejan_number' in d

    def test_annual_values(self):
        inp = HeatExchangerInput(operating_hours=8000, fuel_price_eur_kwh=0.06)
        result = analyze_heat_exchanger(inp)
        assert result.annual_loss_kWh > 0
        assert result.annual_loss_EUR > 0


class TestHeatExchangerSankey:
    """Sankey testleri"""

    def test_sankey_structure(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        assert 'nodes' in sankey
        assert 'links' in sankey
        assert 'summary' in sankey
        assert len(sankey['links']) >= 1
        # Verify structured node format
        for node in sankey['nodes']:
            assert 'id' in node
            assert 'name' in node
            assert 'name_en' in node

    def test_sankey_energy_balance(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        total = sum(link['value'] for link in sankey['links'])
        assert abs(total - result.exergy_in_kW) < 1.0

    def test_sankey_bejan_split(self):
        inp = HeatExchangerInput(
            hot_fluid='air', cold_fluid='air',
            hot_pressure_drop_kPa=10.0, cold_pressure_drop_kPa=10.0,
        )
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        # Basınç düşüşü varsa en az 3 link olmalı
        if result.entropy_gen_pressure_drop_kW_K > 0.01:
            assert len(sankey['links']) >= 3

    def test_sankey_links_have_labels(self):
        inp = HeatExchangerInput()
        result = analyze_heat_exchanger(inp)
        sankey = generate_heat_exchanger_sankey_data(result)
        for link in sankey['links']:
            assert 'label' in link


class TestHeatExchangerRecommendations:
    """Öneri testleri"""

    def test_fouling_recommendation(self):
        inp = HeatExchangerInput(heat_duty_kW=100, design_heat_duty_kW=200)
        result = analyze_heat_exchanger(inp)
        recs = get_heat_exchanger_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'cleaning' in types

    def test_low_effectiveness_recommendation(self):
        inp = HeatExchangerInput(
            hot_inlet_temp_C=200, hot_outlet_temp_C=180,
            cold_inlet_temp_C=20, cold_outlet_temp_C=25,
            hot_mass_flow_kg_s=5.0, cold_mass_flow_kg_s=5.0,
        )
        result = analyze_heat_exchanger(inp)
        recs = get_heat_exchanger_recommendations(result, inp)
        if result.effectiveness < 0.5:
            types = [r['type'] for r in recs]
            assert 'upgrade' in types

    def test_recommendation_structure(self):
        inp = HeatExchangerInput(heat_duty_kW=100, design_heat_duty_kW=200)
        result = analyze_heat_exchanger(inp)
        recs = get_heat_exchanger_recommendations(result, inp)
        for rec in recs:
            assert 'type' in rec
            assert 'title' in rec
            assert 'description' in rec
            assert 'investment_eur' in rec
            assert 'savings_eur_year' in rec
            assert 'payback_years' in rec
            assert 'priority' in rec
