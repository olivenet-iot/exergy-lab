"""Tests for Avoidable/Unavoidable (AV/UN) exergy destruction split.

Covers all 7 equipment engines and the factory-level aggregation.
Based on Tsatsaronis & Morosuk (2008) methodology.
"""

import pytest

from engine.core import compute_avoidable_split, ExergyResult
from engine.compressor import (
    CompressorInput, analyze_compressor,
    PistonCompressorInput, analyze_piston_compressor,
    ScrollCompressorInput, analyze_scroll_compressor,
    CentrifugalCompressorInput, analyze_centrifugal_compressor,
)
from engine.boiler import BoilerInput, analyze_boiler
from engine.chiller import ChillerInput, analyze_chiller
from engine.pump import PumpInput, analyze_pump
from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
from engine.dryer import DryerInput, analyze_dryer
from engine.factory import EquipmentItem, analyze_factory


# ---------------------------------------------------------------------------
# Helper: compute_avoidable_split
# ---------------------------------------------------------------------------

class TestComputeAvoidableSplit:
    def test_basic_split(self):
        av, un, ratio = compute_avoidable_split(100.0, 60.0)
        assert av == pytest.approx(40.0)
        assert un == pytest.approx(60.0)
        assert ratio == pytest.approx(40.0)

    def test_zero_actual(self):
        av, un, ratio = compute_avoidable_split(0.0, 50.0)
        assert av == 0.0
        assert un == 0.0
        assert ratio == 0.0

    def test_negative_actual(self):
        av, un, ratio = compute_avoidable_split(-5.0, 3.0)
        assert av == 0.0
        assert un == 0.0
        assert ratio == 0.0

    def test_unavoidable_exceeds_actual(self):
        av, un, ratio = compute_avoidable_split(10.0, 15.0)
        assert un == pytest.approx(10.0)
        assert av == pytest.approx(0.0)
        assert ratio == pytest.approx(0.0)

    def test_all_avoidable(self):
        av, un, ratio = compute_avoidable_split(10.0, 0.0)
        assert av == pytest.approx(10.0)
        assert un == pytest.approx(0.0)
        assert ratio == pytest.approx(100.0)


# ---------------------------------------------------------------------------
# ExergyResult defaults
# ---------------------------------------------------------------------------

class TestExergyResultDefaults:
    def test_default_av_un_fields(self):
        r = ExergyResult(
            exergy_in_kW=100,
            exergy_out_kW=60,
            exergy_destroyed_kW=40,
            exergy_efficiency_pct=60,
            annual_loss_kWh=240000,
            annual_loss_EUR=24000,
        )
        assert r.exergy_destroyed_avoidable_kW == 0.0
        assert r.exergy_destroyed_unavoidable_kW == 0.0
        assert r.avoidable_ratio_pct == 0.0

    def test_to_dict_includes_av_un(self):
        r = ExergyResult(
            exergy_in_kW=100,
            exergy_out_kW=60,
            exergy_destroyed_kW=40,
            exergy_efficiency_pct=60,
            annual_loss_kWh=240000,
            annual_loss_EUR=24000,
            exergy_destroyed_avoidable_kW=15.0,
            exergy_destroyed_unavoidable_kW=25.0,
            avoidable_ratio_pct=37.5,
        )
        d = r.to_dict()
        assert d["exergy_destroyed_avoidable_kW"] == 15.0
        assert d["exergy_destroyed_unavoidable_kW"] == 25.0
        assert d["avoidable_ratio_pct"] == 37.5


# ---------------------------------------------------------------------------
# Generic AV/UN invariants (parametrized over all engines)
# ---------------------------------------------------------------------------

def _make_compressor():
    inp = CompressorInput(power_kW=37, flow_rate_m3_min=6.2, outlet_pressure_bar=7.5)
    return analyze_compressor(inp)

def _make_piston_compressor():
    inp = PistonCompressorInput(power_kW=30, flow_rate_m3_min=5.0, outlet_pressure_bar=7.5)
    return analyze_piston_compressor(inp)

def _make_scroll_compressor():
    inp = ScrollCompressorInput(power_kW=15, flow_rate_m3_min=2.5, outlet_pressure_bar=7.5)
    return analyze_scroll_compressor(inp)

def _make_centrifugal_compressor():
    inp = CentrifugalCompressorInput(power_kW=200, flow_rate_m3_min=40, outlet_pressure_bar=7.5)
    return analyze_centrifugal_compressor(inp)

def _make_boiler():
    inp = BoilerInput(
        fuel_flow_kg_h=100, steam_flow_kg_h=1200, steam_pressure_bar=10,
        flue_gas_temp_C=180, excess_air_pct=15,
    )
    return analyze_boiler(inp)

def _make_chiller():
    inp = ChillerInput(
        cooling_capacity_kW=350, compressor_power_kW=70,
        chw_supply_temp_C=7, chw_return_temp_C=12,
        cw_supply_temp_C=30, cw_return_temp_C=35,
    )
    return analyze_chiller(inp)

def _make_pump():
    inp = PumpInput(
        motor_power_kW=15, flow_rate_m3_h=50, total_head_m=40,
        pump_efficiency_pct=75, motor_efficiency_pct=90,
    )
    return analyze_pump(inp)

def _make_heat_exchanger():
    inp = HeatExchangerInput(
        hot_inlet_temp_C=90, hot_outlet_temp_C=70,
        hot_mass_flow_kg_s=2.0,
        cold_inlet_temp_C=20, cold_outlet_temp_C=50,
        cold_mass_flow_kg_s=1.5,
    )
    return analyze_heat_exchanger(inp)

def _make_steam_turbine():
    inp = SteamTurbineInput(
        inlet_temp_C=400, inlet_pressure_bar=40,
        mass_flow_kg_s=5, outlet_pressure_bar=2.0,
        isentropic_efficiency=0.80,
    )
    return analyze_steam_turbine(inp)

def _make_steam_turbine_low_eta():
    inp = SteamTurbineInput(
        inlet_temp_C=400, inlet_pressure_bar=40,
        mass_flow_kg_s=5, outlet_pressure_bar=2.0,
        isentropic_efficiency=0.65,
    )
    return analyze_steam_turbine(inp)

def _make_dryer():
    inp = DryerInput()
    return analyze_dryer(inp)


ALL_ENGINES = [
    ("compressor", _make_compressor),
    ("piston_compressor", _make_piston_compressor),
    ("scroll_compressor", _make_scroll_compressor),
    ("centrifugal_compressor", _make_centrifugal_compressor),
    ("boiler", _make_boiler),
    ("chiller", _make_chiller),
    ("pump", _make_pump),
    ("heat_exchanger", _make_heat_exchanger),
    ("steam_turbine", _make_steam_turbine),
    ("dryer", _make_dryer),
]


@pytest.mark.parametrize("name,make_fn", ALL_ENGINES, ids=[x[0] for x in ALL_ENGINES])
class TestAVUNInvariants:
    """AV/UN invariants that must hold for every engine."""

    def test_av_un_sum_equals_total(self, name, make_fn):
        """AV + UN must equal total exergy destroyed (within tolerance)."""
        result = make_fn()
        total = result.exergy_destroyed_kW
        av = result.exergy_destroyed_avoidable_kW
        un = result.exergy_destroyed_unavoidable_kW
        assert abs((av + un) - total) < 0.2, (
            f"{name}: AV({av:.2f}) + UN({un:.2f}) = {av+un:.2f} != total({total:.2f})"
        )

    def test_avoidable_non_negative(self, name, make_fn):
        result = make_fn()
        assert result.exergy_destroyed_avoidable_kW >= 0.0

    def test_unavoidable_non_negative(self, name, make_fn):
        result = make_fn()
        assert result.exergy_destroyed_unavoidable_kW >= 0.0

    def test_avoidable_ratio_range(self, name, make_fn):
        result = make_fn()
        assert 0.0 <= result.avoidable_ratio_pct <= 100.0

    def test_av_un_in_api_dict(self, name, make_fn):
        """to_api_dict (or to_dict) must include AV/UN fields."""
        result = make_fn()
        # Try to_api_dict first (compressor, boiler, etc.), fall back to to_dict
        if hasattr(result, 'to_api_dict'):
            try:
                d = result.to_api_dict("test")
            except TypeError:
                d = result.to_dict()
        else:
            d = result.to_dict()
        assert "exergy_destroyed_avoidable_kW" in d
        assert "exergy_destroyed_unavoidable_kW" in d
        assert "avoidable_ratio_pct" in d


# ---------------------------------------------------------------------------
# Directional tests: poor efficiency → higher AV, good efficiency → lower AV
# ---------------------------------------------------------------------------

class TestPumpAVDirectional:
    """Pump with worse efficiency should have higher AV ratio."""

    def test_poor_vs_good_efficiency(self):
        poor = PumpInput(
            motor_power_kW=15, flow_rate_m3_h=50, total_head_m=40,
            pump_efficiency_pct=50, motor_efficiency_pct=80,
        )
        good = PumpInput(
            motor_power_kW=15, flow_rate_m3_h=50, total_head_m=40,
            pump_efficiency_pct=88, motor_efficiency_pct=95,
        )
        r_poor = analyze_pump(poor)
        r_good = analyze_pump(good)
        # Poor efficiency pump should have higher avoidable ratio
        assert r_poor.avoidable_ratio_pct >= r_good.avoidable_ratio_pct


class TestChillerAVDirectional:
    """Chiller with worse COP should have higher AV ratio."""

    def test_poor_vs_good_cop(self):
        poor = ChillerInput(
            cooling_capacity_kW=350, compressor_power_kW=120,
            chw_supply_temp_C=7, chw_return_temp_C=12,
            cw_supply_temp_C=30, cw_return_temp_C=35,
        )
        good = ChillerInput(
            cooling_capacity_kW=350, compressor_power_kW=50,
            chw_supply_temp_C=7, chw_return_temp_C=12,
            cw_supply_temp_C=30, cw_return_temp_C=35,
        )
        r_poor = analyze_chiller(poor)
        r_good = analyze_chiller(good)
        assert r_poor.avoidable_ratio_pct >= r_good.avoidable_ratio_pct


class TestSteamTurbineAVDirectional:
    """Steam turbine with lower eta_is should have higher AV ratio."""

    def test_low_vs_high_eta(self):
        r_low = _make_steam_turbine_low_eta()  # eta_is = 0.65
        r_high = _make_steam_turbine()          # eta_is = 0.80
        assert r_low.avoidable_ratio_pct >= r_high.avoidable_ratio_pct


# ---------------------------------------------------------------------------
# Factory-level AV/UN aggregation
# ---------------------------------------------------------------------------

class TestFactoryAVUN:
    def test_factory_aggregates_av_un(self):
        items = [
            EquipmentItem(
                id="c1", name="Comp-1", equipment_type="compressor", subtype="screw",
                parameters={"power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
            ),
            EquipmentItem(
                id="p1", name="Pump-1", equipment_type="pump", subtype="centrifugal",
                parameters={"motor_power_kW": 15, "flow_rate_m3_h": 50, "total_head_m": 40},
            ),
        ]
        result = analyze_factory(items)
        agg = result.aggregates

        assert "total_exergy_destroyed_avoidable_kW" in agg
        assert "total_exergy_destroyed_unavoidable_kW" in agg
        assert "avoidable_ratio_pct" in agg
        assert agg["total_exergy_destroyed_avoidable_kW"] >= 0
        assert agg["total_exergy_destroyed_unavoidable_kW"] >= 0

        # Sum should roughly match total destroyed
        total = agg["total_exergy_destroyed_kW"]
        av = agg["total_exergy_destroyed_avoidable_kW"]
        un = agg["total_exergy_destroyed_unavoidable_kW"]
        assert abs((av + un) - total) < 0.5

    def test_factory_sankey_has_av_un(self):
        items = [
            EquipmentItem(
                id="c1", name="Comp-1", equipment_type="compressor", subtype="screw",
                parameters={"power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
            ),
        ]
        result = analyze_factory(items)
        sankey = result.sankey
        summary = sankey["summary"]
        assert "exergy_destroyed_avoidable_kW" in summary
        assert "exergy_destroyed_unavoidable_kW" in summary


# ---------------------------------------------------------------------------
# Sankey AV/UN node split tests
# ---------------------------------------------------------------------------

class TestSankeyAVUNSplit:
    def test_compressor_sankey_split_nodes(self):
        """Compressor with AV/UN should have split destruction nodes."""
        from engine.sankey import generate_sankey_data
        result = _make_compressor()
        sankey = generate_sankey_data(result, "screw")
        # If AV or UN > 0, should have 6 nodes (split)
        if result.exergy_destroyed_avoidable_kW > 0 or result.exergy_destroyed_unavoidable_kW > 0:
            assert len(sankey["nodes"]) == 6
            node_names = [n["name"] for n in sankey["nodes"]]
            assert any("Onlenebilir" in name or "Önlenebilir" in name for name in node_names)
            assert any("Onlenemez" in name or "Önlenemez" in name for name in node_names)

    def test_steam_turbine_sankey_split_nodes(self):
        """Steam turbine with AV/UN should have split destruction nodes."""
        from engine.steam_turbine import generate_steam_turbine_sankey_data
        result = _make_steam_turbine()
        sankey = generate_steam_turbine_sankey_data(result)
        if result.exergy_destroyed_avoidable_kW > 0 or result.exergy_destroyed_unavoidable_kW > 0:
            node_names = [n["name"] for n in sankey["nodes"]]
            assert any("Onlenebilir" in name for name in node_names)

    def test_boiler_sankey_summary_has_av_un(self):
        """Boiler sankey summary should include AV/UN fields."""
        from engine.boiler import generate_boiler_sankey_data
        result = _make_boiler()
        sankey = generate_boiler_sankey_data(result, "steam_firetube")
        assert "exergy_destroyed_avoidable_kW" in sankey["summary"]
        assert "exergy_destroyed_unavoidable_kW" in sankey["summary"]

    def test_pump_sankey_summary_has_av_un(self):
        """Pump sankey summary should include AV/UN fields."""
        from engine.pump import generate_pump_sankey_data
        result = _make_pump()
        sankey = generate_pump_sankey_data(result, "centrifugal")
        assert "exergy_destroyed_avoidable_kW" in sankey["summary"]

    def test_fallback_single_node_when_both_zero(self):
        """When AV and UN are both 0, compressor sankey should use single node."""
        from engine.compressor import CompressorResult
        from engine.sankey import generate_sankey_data
        result = CompressorResult(
            exergy_in_kW=100, exergy_out_kW=60, exergy_destroyed_kW=40,
            exergy_efficiency_pct=60, annual_loss_kWh=240000, annual_loss_EUR=24000,
            recoverable_heat_kW=10,
            exergy_destroyed_avoidable_kW=0.0,
            exergy_destroyed_unavoidable_kW=0.0,
            avoidable_ratio_pct=0.0,
        )
        sankey = generate_sankey_data(result, "screw")
        assert len(sankey["nodes"]) == 5  # Original layout
        node_names = [n["name"] for n in sankey["nodes"]]
        assert any("Yıkımı" in name and "Onlenebilir" not in name for name in node_names)
