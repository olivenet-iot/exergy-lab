"""Tests for What-If scenario comparison."""

import pytest
from fastapi.testclient import TestClient

from api.main import app
from engine.compare import compute_comparison

client = TestClient(app)


# ---------------------------------------------------------------------------
# Unit tests for compute_comparison
# ---------------------------------------------------------------------------

class TestComputeComparison:
    def test_basic_improvement(self):
        """Improved scenario should show positive savings."""
        baseline = {
            "exergy_efficiency_pct": 40.0,
            "exergy_input_kW": 100.0,
            "exergy_output_kW": 40.0,
            "exergy_destroyed_kW": 60.0,
            "exergy_destroyed_avoidable_kW": 30.0,
            "exergy_destroyed_unavoidable_kW": 30.0,
            "avoidable_ratio_pct": 50.0,
            "annual_loss_kWh": 360000.0,
            "annual_loss_EUR": 36000.0,
        }
        scenario = {
            "exergy_efficiency_pct": 50.0,
            "exergy_input_kW": 90.0,
            "exergy_output_kW": 45.0,
            "exergy_destroyed_kW": 45.0,
            "exergy_destroyed_avoidable_kW": 20.0,
            "exergy_destroyed_unavoidable_kW": 25.0,
            "avoidable_ratio_pct": 44.4,
            "annual_loss_kWh": 270000.0,
            "annual_loss_EUR": 27000.0,
        }
        result = compute_comparison(baseline, scenario, energy_price_eur_kwh=0.10, operating_hours=6000)

        assert result["savings"]["exergy_saved_kW"] == 15.0
        assert result["savings"]["annual_savings_kWh"] == 90000.0
        assert result["savings"]["annual_savings_EUR"] == 9000.0
        assert result["savings"]["efficiency_improvement_pct"] == 10.0
        assert len(result["improved_metrics"]) > 0

    def test_degradation(self):
        """Worse scenario should clamp exergy_saved to 0."""
        baseline = {
            "exergy_efficiency_pct": 50.0,
            "exergy_destroyed_kW": 40.0,
        }
        scenario = {
            "exergy_efficiency_pct": 35.0,
            "exergy_destroyed_kW": 55.0,
        }
        result = compute_comparison(baseline, scenario)

        assert result["savings"]["exergy_saved_kW"] == 0
        assert result["savings"]["annual_savings_kWh"] == 0
        assert result["savings"]["efficiency_improvement_pct"] == -15.0
        assert "exergy_destroyed_kW" in result["degraded_metrics"]

    def test_no_change(self):
        """Identical baseline and scenario should produce zero deltas."""
        data = {
            "exergy_efficiency_pct": 45.0,
            "exergy_destroyed_kW": 50.0,
            "exergy_input_kW": 100.0,
            "exergy_output_kW": 50.0,
        }
        result = compute_comparison(data, data)

        for v in result["delta"].values():
            assert abs(v) < 1e-10
        assert result["savings"]["exergy_saved_kW"] == 0
        assert len(result["improved_metrics"]) == 0
        assert len(result["degraded_metrics"]) == 0

    def test_empty_dicts(self):
        """Empty dicts should not crash."""
        result = compute_comparison({}, {})

        assert result["delta"] == {}
        assert result["delta_pct"] == {}
        assert result["savings"]["exergy_saved_kW"] == 0
        assert isinstance(result["summary_tr"], str)

    def test_delta_pct_calculation(self):
        """Delta percent should be computed correctly."""
        baseline = {"exergy_destroyed_kW": 100.0}
        scenario = {"exergy_destroyed_kW": 80.0}
        result = compute_comparison(baseline, scenario)

        assert result["delta"]["exergy_destroyed_kW"] == -20.0
        assert result["delta_pct"]["exergy_destroyed_kW"] == -20.0

    def test_summary_tr(self):
        """Summary should contain Turkish text."""
        baseline = {"exergy_efficiency_pct": 40.0, "exergy_destroyed_kW": 60.0}
        scenario = {"exergy_efficiency_pct": 50.0, "exergy_destroyed_kW": 45.0}
        result = compute_comparison(baseline, scenario)

        assert "verim" in result["summary_tr"].lower()

    def test_custom_energy_price(self):
        """Doubling price should double EUR savings."""
        baseline = {"exergy_destroyed_kW": 100.0}
        scenario = {"exergy_destroyed_kW": 80.0}

        result_1x = compute_comparison(baseline, scenario, energy_price_eur_kwh=0.10, operating_hours=6000)
        result_2x = compute_comparison(baseline, scenario, energy_price_eur_kwh=0.20, operating_hours=6000)

        assert abs(result_2x["savings"]["annual_savings_EUR"] - 2 * result_1x["savings"]["annual_savings_EUR"]) < 0.01


# ---------------------------------------------------------------------------
# Integration tests for /api/compare endpoint
# ---------------------------------------------------------------------------

class TestCompareAPI:
    def test_compare_compressor(self):
        """Compressor comparison should return 200 with correct structure."""
        resp = client.post("/api/compare", json={
            "equipment_type": "compressor",
            "subtype": "screw",
            "baseline_params": {
                "power_kW": 37,
                "flow_rate_m3_min": 6.2,
                "outlet_pressure_bar": 7.5,
            },
            "scenario_params": {
                "power_kW": 37,
                "flow_rate_m3_min": 7.0,
                "outlet_pressure_bar": 7.5,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "baseline" in data
        assert "scenario" in data
        assert "comparison" in data
        assert "savings" in data["comparison"]
        assert "delta" in data["comparison"]
        assert "summary_tr" in data["comparison"]

    def test_compare_boiler(self):
        """Boiler comparison should include boiler-specific metrics."""
        resp = client.post("/api/compare", json={
            "equipment_type": "boiler",
            "subtype": "steam_firetube",
            "baseline_params": {
                "fuel_flow_kg_h": 100,
                "steam_flow_kg_h": 2000,
                "steam_pressure_bar": 10,
            },
            "scenario_params": {
                "fuel_flow_kg_h": 90,
                "steam_flow_kg_h": 2000,
                "steam_pressure_bar": 10,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        # Boiler should have thermal_efficiency_pct in metrics
        assert data["baseline"]["metrics"]["thermal_efficiency_pct"] is not None

    def test_compare_all_equipment_types(self):
        """All 7 equipment types should return 200."""
        configs = [
            ("compressor", "screw", {
                "power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5,
            }),
            ("boiler", "steam_firetube", {
                "fuel_flow_kg_h": 100, "steam_flow_kg_h": 2000, "steam_pressure_bar": 10,
            }),
            ("chiller", "screw", {
                "cooling_capacity_kW": 350, "compressor_power_kW": 70,
            }),
            ("pump", "centrifugal", {
                "motor_power_kW": 15, "flow_rate_m3_h": 50, "total_head_m": 40,
            }),
            ("heat_exchanger", "shell_tube", {
                "hot_mass_flow_kg_s": 2.0, "cold_mass_flow_kg_s": 1.5,
            }),
            ("steam_turbine", "back_pressure", {
                "inlet_temp_C": 400, "inlet_pressure_bar": 40,
                "mass_flow_kg_s": 5, "outlet_pressure_bar": 2.0,
            }),
            ("dryer", "rotary", {
                "product_mass_flow_kg_h": 1000, "moisture_in_pct": 60, "moisture_out_pct": 10,
            }),
        ]

        for eq_type, subtype, params in configs:
            resp = client.post("/api/compare", json={
                "equipment_type": eq_type,
                "subtype": subtype,
                "baseline_params": params,
                "scenario_params": params,
            })
            assert resp.status_code == 200, f"Failed for {eq_type}/{subtype}: {resp.text}"

    def test_compare_returns_radar(self):
        """Both baseline and scenario should include radar_data."""
        resp = client.post("/api/compare", json={
            "equipment_type": "compressor",
            "subtype": "screw",
            "baseline_params": {
                "power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5,
            },
            "scenario_params": {
                "power_kW": 37, "flow_rate_m3_min": 7.0, "outlet_pressure_bar": 7.5,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["baseline"]["radar_data"] is not None
        assert data["scenario"]["radar_data"] is not None
        assert "scores" in data["baseline"]["radar_data"]

    def test_compare_invalid_type(self):
        """Invalid equipment type should return error."""
        resp = client.post("/api/compare", json={
            "equipment_type": "nonexistent",
            "subtype": "foo",
            "baseline_params": {},
            "scenario_params": {},
        })
        assert resp.status_code in (422, 501)
