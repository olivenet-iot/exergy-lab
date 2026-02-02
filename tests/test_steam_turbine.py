"""Buhar türbini engine testleri"""
import pytest
import math
from engine.steam_turbine import (
    SteamTurbineInput, SteamTurbineResult,
    analyze_steam_turbine, get_steam_turbine_recommendations,
    generate_steam_turbine_sankey_data,
    _get_saturation_temp_C
)
from engine.core import DeadState


class TestSteamTurbineInput:
    """SteamTurbineInput testleri"""

    def test_default_values(self):
        inp = SteamTurbineInput()
        assert inp.turbine_type == 'backpressure'
        assert inp.inlet_temp_C == 400.0
        assert inp.inlet_pressure_bar == 40.0
        assert inp.outlet_temp_C is not None

    def test_condensing_outlet_temp(self):
        inp = SteamTurbineInput(turbine_type='condensing', outlet_pressure_bar=0.1)
        T_sat = _get_saturation_temp_C(0.1)
        assert abs(inp.outlet_temp_C - T_sat) < 1.0

    def test_backpressure_outlet_temp(self):
        inp = SteamTurbineInput(turbine_type='backpressure', outlet_pressure_bar=5.0)
        T_sat = _get_saturation_temp_C(5.0)
        assert inp.outlet_temp_C >= T_sat


class TestAnalyzeSteamTurbine:
    """analyze_steam_turbine testleri"""

    def test_basic_analysis(self):
        inp = SteamTurbineInput(
            inlet_temp_C=400, inlet_pressure_bar=40,
            mass_flow_kg_s=5.0, outlet_pressure_bar=2.0,
        )
        result = analyze_steam_turbine(inp)
        assert result.exergy_in_kW > 0
        assert result.shaft_power_kW > 0
        assert result.electrical_power_kW > 0
        assert result.exergy_destroyed_kW >= 0
        assert 0 < result.exergy_efficiency_pct <= 100

    def test_exergy_balance(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        balance = abs(result.exergy_in_kW - result.shaft_power_kW - result.exergy_out_kW - result.exergy_destroyed_kW)
        assert balance < 1.0

    def test_electrical_less_than_shaft(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        assert result.electrical_power_kW < result.shaft_power_kW

    def test_chp_mode(self):
        inp = SteamTurbineInput(
            is_chp=True, turbine_type='backpressure',
            outlet_pressure_bar=3.0, heat_recovery_temp_C=130,
        )
        result = analyze_steam_turbine(inp)
        assert result.heat_recovered_kW is not None
        assert result.heat_recovered_kW > 0
        assert result.chp_exergy_efficiency_pct is not None
        # CHP total useful exergy = W_shaft + heat_recovered_exergy
        assert result.total_useful_exergy_kW > result.shaft_power_kW

    def test_condensing_vs_backpressure(self):
        inp_cond = SteamTurbineInput(turbine_type='condensing', outlet_pressure_bar=0.1)
        inp_bp = SteamTurbineInput(turbine_type='backpressure', outlet_pressure_bar=3.0)
        r_cond = analyze_steam_turbine(inp_cond)
        r_bp = analyze_steam_turbine(inp_bp)
        assert r_cond.shaft_power_kW > r_bp.shaft_power_kW

    def test_higher_efficiency_more_work(self):
        inp_low = SteamTurbineInput(isentropic_efficiency=0.60)
        inp_high = SteamTurbineInput(isentropic_efficiency=0.90)
        r_low = analyze_steam_turbine(inp_low)
        r_high = analyze_steam_turbine(inp_high)
        assert r_high.shaft_power_kW >= r_low.shaft_power_kW

    def test_annual_values(self):
        inp = SteamTurbineInput(operating_hours=7000)
        result = analyze_steam_turbine(inp)
        assert result.annual_electricity_MWh > 0
        assert result.annual_electricity_revenue_EUR > 0

    def test_to_api_dict(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        d = result.to_api_dict()
        assert 'shaft_power_kW' in d
        assert 'electrical_power_kW' in d
        assert 'benchmark_comparison' in d
        assert 'benchmark_percentile' in d
        assert 'comparison_text' in d

    def test_to_dict(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        d = result.to_dict()
        assert 'exergy_in_kW' in d
        assert 'shaft_power_kW' in d

    def test_saturation_temp_interpolation(self):
        T_10 = _get_saturation_temp_C(10.0)
        assert abs(T_10 - 179.9) < 0.5
        T_mid = _get_saturation_temp_C(7.0)
        assert 158.8 < T_mid < 170.4


class TestSteamTurbineSankey:
    """Sankey testleri"""

    def test_sankey_structure(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        sankey = generate_steam_turbine_sankey_data(result)
        assert 'nodes' in sankey
        assert 'links' in sankey
        assert 'summary' in sankey
        assert len(sankey['links']) >= 2
        # Verify structured node format
        for node in sankey['nodes']:
            assert 'id' in node
            assert 'name' in node
            assert 'name_en' in node

    def test_sankey_chp_mode(self):
        inp = SteamTurbineInput(
            is_chp=True, turbine_type='backpressure',
            outlet_pressure_bar=3.0, heat_recovery_temp_C=130,
        )
        result = analyze_steam_turbine(inp)
        sankey = generate_steam_turbine_sankey_data(result)
        # CHP modunda daha fazla node
        assert len(sankey['nodes']) >= 4

    def test_sankey_links_have_labels(self):
        inp = SteamTurbineInput()
        result = analyze_steam_turbine(inp)
        sankey = generate_steam_turbine_sankey_data(result)
        for link in sankey['links']:
            assert 'label' in link


class TestSteamTurbineRecommendations:
    """Öneri testleri"""

    def test_chp_recommendation_for_non_chp(self):
        inp = SteamTurbineInput(is_chp=False, outlet_pressure_bar=3.0)
        result = analyze_steam_turbine(inp)
        recs = get_steam_turbine_recommendations(result, inp)
        if result.exhaust_exergy_kW and result.exhaust_exergy_kW > 100:
            types = [r['type'] for r in recs]
            assert 'chp_conversion' in types

    def test_overhaul_recommendation(self):
        inp = SteamTurbineInput(isentropic_efficiency=0.60)
        result = analyze_steam_turbine(inp)
        recs = get_steam_turbine_recommendations(result, inp)
        types = [r['type'] for r in recs]
        assert 'overhaul' in types

    def test_recommendation_structure(self):
        inp = SteamTurbineInput(isentropic_efficiency=0.60)
        result = analyze_steam_turbine(inp)
        recs = get_steam_turbine_recommendations(result, inp)
        for rec in recs:
            assert 'type' in rec
            assert 'title' in rec
            assert 'investment_eur' in rec
            assert 'savings_eur_year' in rec
            assert 'priority' in rec
