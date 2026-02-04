"""Tests for exergoeconomic analysis module."""

import pytest
import math

from engine.exergoeconomic import (
    compute_crf, compute_z_dot, estimate_equipment_cost,
    analyze_exergoeconomic, _apply_exergoeconomic,
    ExergoeconomicInput, ExergoeconomicResult,
)
from engine.compressor import CompressorInput, analyze_compressor
from engine.boiler import BoilerInput, analyze_boiler
from engine.chiller import ChillerInput, analyze_chiller
from engine.pump import PumpInput, analyze_pump


# ---------------------------------------------------------------------------
# TestComputeCRF
# ---------------------------------------------------------------------------

class TestComputeCRF:
    def test_standard_values(self):
        """CRF for 10% interest, 20 years ~ 0.1175."""
        crf = compute_crf(0.10, 20)
        assert 0.10 < crf < 0.13
        # Known value: 0.10 * 1.10^20 / (1.10^20 - 1) = 0.11746
        assert abs(crf - 0.11746) < 0.001

    def test_zero_interest(self):
        """Zero interest rate -> 1/n."""
        crf = compute_crf(0.0, 20)
        assert abs(crf - 0.05) < 0.001

    def test_short_life(self):
        """Short equipment life -> higher CRF."""
        crf_short = compute_crf(0.10, 5)
        crf_long = compute_crf(0.10, 20)
        assert crf_short > crf_long

    def test_single_year(self):
        """1 year life -> CRF = 1+i."""
        crf = compute_crf(0.10, 1)
        assert abs(crf - 1.10) < 0.001


# ---------------------------------------------------------------------------
# TestComputeZDot
# ---------------------------------------------------------------------------

class TestComputeZDot:
    def test_basic_calculation(self):
        """Z_dot should be positive for nonzero investment."""
        crf = compute_crf(0.10, 20)
        z_dot = compute_z_dot(100000, crf, 0.02, 6000)
        assert z_dot > 0
        # Z_dot = 100000 * (0.11746 + 0.02) / 6000 ~ 2.29 EUR/h
        assert 2.0 < z_dot < 2.5

    def test_zero_hours(self):
        """Zero operating hours -> Z_dot = 0."""
        crf = compute_crf(0.10, 20)
        z_dot = compute_z_dot(100000, crf, 0.02, 0)
        assert z_dot == 0.0

    def test_higher_investment_higher_z_dot(self):
        """Higher investment -> higher Z_dot."""
        crf = compute_crf(0.10, 20)
        z1 = compute_z_dot(50000, crf, 0.02, 6000)
        z2 = compute_z_dot(100000, crf, 0.02, 6000)
        assert z2 > z1
        assert abs(z2 - 2 * z1) < 0.01


# ---------------------------------------------------------------------------
# TestEstimateEquipmentCost
# ---------------------------------------------------------------------------

class TestEstimateEquipmentCost:
    def test_compressor_cost(self):
        """Compressor PEC should be reasonable."""
        cost = estimate_equipment_cost('compressor', 37.0)
        assert cost > 1000
        assert cost < 500000

    def test_larger_capacity_higher_cost(self):
        """Larger capacity -> higher PEC."""
        c1 = estimate_equipment_cost('pump', 10.0)
        c2 = estimate_equipment_cost('pump', 100.0)
        assert c2 > c1

    def test_unknown_type_uses_default(self):
        """Unknown equipment type falls back to default."""
        cost = estimate_equipment_cost('unknown_type', 50.0)
        assert cost > 0


# ---------------------------------------------------------------------------
# TestAnalyzeExergoeconomic
# ---------------------------------------------------------------------------

class TestAnalyzeExergoeconomic:
    def test_compressor_example(self):
        """Basic compressor exergoeconomic analysis."""
        result = analyze_exergoeconomic(
            exergy_destroyed_kW=15.0,
            exergy_efficiency_pct=45.0,
            exergy_in_kW=37.0,
            exergy_out_kW=16.65,
            c_fuel_eur_kWh=0.10,
            equipment_type='compressor',
            capacity_param_kW=37.0,
        )
        assert result.Z_dot_eur_h > 0
        assert result.C_dot_destruction_eur_h > 0
        assert 0 <= result.f_factor <= 1
        assert result.r_factor >= 0
        assert result.c_product_eur_kWh > result.c_fuel_eur_kWh
        assert result.total_cost_rate_eur_h == pytest.approx(
            result.Z_dot_eur_h + result.C_dot_destruction_eur_h, abs=0.001
        )

    def test_f_factor_bounds(self):
        """f-factor always between 0 and 1."""
        result = analyze_exergoeconomic(
            exergy_destroyed_kW=20.0,
            exergy_efficiency_pct=30.0,
            exergy_in_kW=50.0,
            exergy_out_kW=15.0,
            c_fuel_eur_kWh=0.10,
            equipment_type='boiler',
            capacity_param_kW=200.0,
        )
        assert 0.0 <= result.f_factor <= 1.0

    def test_high_efficiency_low_r(self):
        """High efficiency gives relatively low r_factor."""
        result_good = analyze_exergoeconomic(
            exergy_destroyed_kW=5.0,
            exergy_efficiency_pct=85.0,
            exergy_in_kW=100.0,
            exergy_out_kW=85.0,
            c_fuel_eur_kWh=0.10,
            equipment_type='pump',
            capacity_param_kW=100.0,
        )
        result_bad = analyze_exergoeconomic(
            exergy_destroyed_kW=60.0,
            exergy_efficiency_pct=30.0,
            exergy_in_kW=100.0,
            exergy_out_kW=30.0,
            c_fuel_eur_kWh=0.10,
            equipment_type='pump',
            capacity_param_kW=100.0,
        )
        assert result_good.r_factor < result_bad.r_factor

    def test_zero_destruction(self):
        """Zero exergy destruction gives C_dot_D = 0."""
        result = analyze_exergoeconomic(
            exergy_destroyed_kW=0.0,
            exergy_efficiency_pct=100.0,
            exergy_in_kW=50.0,
            exergy_out_kW=50.0,
            c_fuel_eur_kWh=0.10,
            equipment_type='compressor',
            capacity_param_kW=50.0,
        )
        assert result.C_dot_destruction_eur_h == 0.0
        assert result.f_factor == pytest.approx(1.0, abs=0.001)

    def test_custom_pec(self):
        """Custom equipment cost should change Z_dot."""
        r1 = analyze_exergoeconomic(
            exergy_destroyed_kW=15.0,
            exergy_efficiency_pct=45.0,
            exergy_in_kW=37.0,
            exergy_out_kW=16.65,
            c_fuel_eur_kWh=0.10,
            equipment_type='compressor',
            capacity_param_kW=37.0,
            equipment_cost_eur=None,
        )
        r2 = analyze_exergoeconomic(
            exergy_destroyed_kW=15.0,
            exergy_efficiency_pct=45.0,
            exergy_in_kW=37.0,
            exergy_out_kW=16.65,
            c_fuel_eur_kWh=0.10,
            equipment_type='compressor',
            capacity_param_kW=37.0,
            equipment_cost_eur=200000.0,
        )
        # Custom PEC of 200k should give higher Z_dot than auto-estimated
        assert r2.Z_dot_eur_h > r1.Z_dot_eur_h
        # f-factor should change too
        assert r2.f_factor != r1.f_factor


# ---------------------------------------------------------------------------
# TestExergoeconomicIntegration
# ---------------------------------------------------------------------------

class TestExergoeconomicIntegration:
    def test_compressor_has_exergoeconomic_fields(self):
        """Compressor result should include exergoeconomic fields."""
        inp = CompressorInput(
            power_kW=37.0,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
            electricity_price_eur_kwh=0.10,
        )
        result = analyze_compressor(inp)
        assert result.exergoeconomic_f_factor > 0
        assert result.exergoeconomic_r_factor > 0
        assert result.exergoeconomic_Z_dot_eur_h > 0
        assert result.exergoeconomic_C_dot_destruction_eur_h > 0
        assert result.exergoeconomic_c_product_eur_kWh > 0
        assert result.exergoeconomic_total_cost_rate_eur_h > 0

    def test_boiler_has_exergoeconomic_fields(self):
        """Boiler result should include exergoeconomic fields."""
        inp = BoilerInput(
            fuel_flow_kg_h=100.0,
            steam_flow_kg_h=2000.0,
            steam_pressure_bar=10.0,
            fuel_price_eur_kg=0.50,
        )
        result = analyze_boiler(inp)
        assert result.exergoeconomic_f_factor > 0
        assert result.exergoeconomic_Z_dot_eur_h > 0
        assert result.exergoeconomic_C_dot_destruction_eur_h > 0

    def test_chiller_has_exergoeconomic_fields(self):
        """Chiller result should include exergoeconomic fields."""
        inp = ChillerInput(
            cooling_capacity_kW=350.0,
            compressor_power_kW=70.0,
            electricity_price_eur_kwh=0.12,
        )
        result = analyze_chiller(inp)
        assert result.exergoeconomic_f_factor > 0
        assert result.exergoeconomic_Z_dot_eur_h > 0

    def test_pump_has_exergoeconomic_fields(self):
        """Pump result should include exergoeconomic fields."""
        inp = PumpInput(
            motor_power_kW=15.0,
            flow_rate_m3_h=50.0,
            total_head_m=40.0,
            electricity_price_eur_kwh=0.12,
        )
        result = analyze_pump(inp)
        assert result.exergoeconomic_f_factor > 0
        assert result.exergoeconomic_Z_dot_eur_h > 0

    def test_compressor_to_api_dict_includes_fields(self):
        """to_api_dict should include exergoeconomic fields."""
        inp = CompressorInput(
            power_kW=37.0,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
        )
        result = analyze_compressor(inp)
        api = result.to_api_dict("screw")
        assert "exergoeconomic_f_factor" in api
        assert "exergoeconomic_r_factor" in api
        assert "exergoeconomic_Z_dot_eur_h" in api
        assert "exergoeconomic_C_dot_destruction_eur_h" in api
        assert "exergoeconomic_c_product_eur_kWh" in api
        assert "exergoeconomic_total_cost_rate_eur_h" in api

    def test_custom_equipment_cost_changes_f_factor(self):
        """Providing equipment_cost_eur should change f_factor."""
        inp1 = CompressorInput(
            power_kW=37.0,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
        )
        inp2 = CompressorInput(
            power_kW=37.0,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
            equipment_cost_eur=200000.0,
        )
        r1 = analyze_compressor(inp1)
        r2 = analyze_compressor(inp2)
        assert r1.exergoeconomic_f_factor != r2.exergoeconomic_f_factor

    def test_existing_core_results_unchanged(self):
        """Exergoeconomic addition should not change core exergy results."""
        inp = CompressorInput(
            power_kW=37.0,
            flow_rate_m3_min=6.2,
            outlet_pressure_bar=7.5,
        )
        result = analyze_compressor(inp)
        # Core fields should still be correct
        assert result.exergy_in_kW == pytest.approx(37.0, abs=0.01)
        assert result.exergy_efficiency_pct > 0
        assert result.exergy_destroyed_kW > 0
        assert result.exergy_destroyed_avoidable_kW >= 0

    def test_boiler_to_api_dict_includes_fields(self):
        """Boiler to_api_dict should include exergoeconomic fields."""
        inp = BoilerInput(
            fuel_flow_kg_h=100.0,
            steam_flow_kg_h=2000.0,
            steam_pressure_bar=10.0,
        )
        result = analyze_boiler(inp)
        api = result.to_api_dict("steam_firetube")
        assert "exergoeconomic_f_factor" in api
        assert api["exergoeconomic_f_factor"] > 0

    def test_pump_custom_cost(self):
        """Pump with custom equipment cost."""
        inp = PumpInput(
            motor_power_kW=15.0,
            flow_rate_m3_h=50.0,
            total_head_m=40.0,
            equipment_cost_eur=50000.0,
        )
        result = analyze_pump(inp)
        assert result.exergoeconomic_Z_dot_eur_h > 0
        assert result.exergoeconomic_f_factor > 0
