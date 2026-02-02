"""Kurutma fırını engine testleri"""
import pytest
import math
from engine.dryer import (
    DryerInput, DryerResult,
    analyze_dryer, get_dryer_recommendations,
    generate_dryer_sankey_data,
    _get_hfg, DRYER_THERMAL_EFF
)
from engine.core import DeadState


class TestDryerInput:
    """DryerInput testleri"""

    def test_default_values(self):
        inp = DryerInput()
        assert inp.dryer_type == 'conveyor'
        assert inp.moisture_in_pct == 60.0
        assert inp.moisture_out_pct == 10.0
        assert inp.water_removed_kg_h > 0
        assert inp.heat_input_kW > 0

    def test_water_removal_calculation(self):
        inp = DryerInput(
            product_mass_flow_kg_h=1000,
            moisture_in_pct=50,
            moisture_out_pct=10,
        )
        expected_water = 1000 - 500 / 0.9
        assert abs(inp.water_removed_kg_h - expected_water) < 1.0

    def test_zero_moisture_change(self):
        inp = DryerInput(moisture_in_pct=10, moisture_out_pct=10)
        assert inp.water_removed_kg_h == 0 or inp.water_removed_kg_h < 1

    def test_heat_input_auto_calc(self):
        inp = DryerInput(heat_input_kW=None)
        assert inp.heat_input_kW > 0

    def test_custom_heat_input(self):
        inp = DryerInput(heat_input_kW=500.0)
        assert inp.heat_input_kW == 500.0

    def test_hfg_function(self):
        h60 = _get_hfg(60)
        h100 = _get_hfg(100)
        assert h60 > h100
        assert h100 > 2200


class TestAnalyzeDryer:
    """analyze_dryer testleri"""

    def test_basic_analysis(self):
        inp = DryerInput(
            product_mass_flow_kg_h=1000,
            moisture_in_pct=60, moisture_out_pct=10,
            supply_temp_C=200,
        )
        result = analyze_dryer(inp)
        assert result.exergy_in_kW > 0
        assert result.exergy_out_kW >= 0
        assert result.exergy_destroyed_kW >= 0
        assert 0 <= result.exergy_efficiency_pct <= 100
        assert result.water_removed_kg_h > 0

    def test_exergy_balance(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        total = result.exergy_out_kW + result.exhaust_exergy_kW + result.exergy_destroyed_kW
        assert abs(result.exergy_in_kW - total) < 1.0

    def test_electrical_source(self):
        inp = DryerInput(heat_source='electrical', heat_input_kW=100)
        result = analyze_dryer(inp)
        assert result.exergy_in_kW == 100.0

    def test_steam_source(self):
        inp = DryerInput(heat_source='steam', heat_input_kW=100, supply_temp_C=150)
        result = analyze_dryer(inp)
        assert result.exergy_in_kW < 100

    def test_natural_gas_source(self):
        inp = DryerInput(heat_source='natural_gas', heat_input_kW=100)
        result = analyze_dryer(inp)
        assert result.exergy_in_kW > 100

    def test_thermal_efficiency(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        assert 0 < result.thermal_efficiency_pct < 100

    def test_specific_energy(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        assert result.specific_energy_kJ_kg_water > 2000

    def test_different_dryer_types(self):
        for dryer_type in DRYER_THERMAL_EFF.keys():
            inp = DryerInput(dryer_type=dryer_type)
            result = analyze_dryer(inp)
            assert result.exergy_in_kW > 0
            assert result.benchmark_comparison is not None

    def test_exhaust_recovery(self):
        inp = DryerInput(air_outlet_temp_C=120)
        result = analyze_dryer(inp)
        assert result.exhaust_exergy_kW > 0
        assert result.exhaust_recovery_potential_kW > 0

    def test_annual_values(self):
        inp = DryerInput(operating_hours=5000, fuel_price_eur_kwh=0.05)
        result = analyze_dryer(inp)
        assert result.annual_loss_kWh > 0
        assert result.annual_loss_EUR > 0

    def test_to_api_dict(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        d = result.to_api_dict()
        assert 'water_removed_kg_h' in d
        assert 'specific_energy_kJ_kg_water' in d
        assert 'exhaust_exergy_kW' in d
        assert 'benchmark_percentile' in d
        assert 'comparison_text' in d

    def test_to_dict(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        d = result.to_dict()
        assert 'exergy_in_kW' in d
        assert 'water_removed_kg_h' in d


class TestDryerSankey:
    """Sankey testleri"""

    def test_sankey_structure(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        sankey = generate_dryer_sankey_data(result)
        assert 'nodes' in sankey
        assert 'links' in sankey
        assert 'summary' in sankey
        assert len(sankey['links']) >= 2
        # Verify structured node format
        for node in sankey['nodes']:
            assert 'id' in node
            assert 'name' in node
            assert 'name_en' in node

    def test_sankey_energy_balance(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        sankey = generate_dryer_sankey_data(result)
        total = sum(link['value'] for link in sankey['links'])
        assert abs(total - result.exergy_in_kW) < 1.0

    def test_sankey_links_have_labels(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        sankey = generate_dryer_sankey_data(result)
        for link in sankey['links']:
            assert 'label' in link


class TestDryerRecommendations:
    """Öneri testleri"""

    def test_exhaust_recovery_recommendation(self):
        inp = DryerInput(air_outlet_temp_C=120, operating_hours=6000)
        result = analyze_dryer(inp)
        recs = get_dryer_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'exhaust_heat_recovery' in types

    def test_electrical_source_recommendation(self):
        inp = DryerInput(heat_source='electrical', heat_input_kW=100)
        result = analyze_dryer(inp)
        recs = get_dryer_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'heat_source_change' in types

    def test_recommendation_structure(self):
        inp = DryerInput()
        result = analyze_dryer(inp)
        recs = get_dryer_recommendations(result, inp)
        for rec in recs:
            assert 'type' in rec
            assert 'title' in rec
            assert 'description' in rec
            assert 'investment_eur' in rec
            assert 'savings_eur_year' in rec
            assert 'payback_years' in rec
            assert 'priority' in rec
