"""Tests for ExergyLab API."""

import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


class TestHealth:
    def test_root(self):
        resp = client.get("/")
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == "ExergyLab API"
        assert "version" in data

    def test_health(self):
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


class TestAnalyze:
    def test_screw_compressor(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "screw",
            "parameters": {
                "power_kW": 32,
                "flow_rate_m3_min": 6.2,
                "outlet_pressure_bar": 7.5,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "screw"
        assert "metrics" in data
        assert "heat_recovery" in data
        assert "benchmark" in data
        assert "sankey" in data
        assert data["metrics"]["exergy_input_kW"] == 32.0
        assert data["metrics"]["exergy_output_kW"] > 0

    def test_piston_compressor(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "piston",
            "parameters": {
                "power_kW": 22,
                "flow_rate_m3_min": 3.0,
                "outlet_pressure_bar": 8.0,
                "stages": 2,
                "cooling_type": "air",
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "piston"
        assert data["metrics"]["exergy_input_kW"] == 22.0

    def test_scroll_compressor(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "scroll",
            "parameters": {
                "power_kW": 11,
                "flow_rate_m3_min": 1.5,
                "outlet_pressure_bar": 8.0,
                "oil_free": True,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "scroll"

    def test_centrifugal_compressor(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "centrifugal",
            "parameters": {
                "power_kW": 250,
                "flow_rate_m3_min": 45.0,
                "outlet_pressure_bar": 7.5,
                "stages": 3,
                "igv_position": 100.0,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "centrifugal"

    def test_invalid_type(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "turbo",
            "parameters": {"power_kW": 32, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
        })
        assert resp.status_code == 422

    def test_missing_required_fields(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "screw",
            "parameters": {"power_kW": 32},
        })
        assert resp.status_code == 422

    def test_sankey_in_response(self):
        resp = client.post("/api/analyze", json={
            "compressor_type": "screw",
            "parameters": {
                "power_kW": 32,
                "flow_rate_m3_min": 6.2,
                "outlet_pressure_bar": 7.5,
            },
        })
        assert resp.status_code == 200
        sankey = resp.json()["sankey"]
        assert len(sankey["nodes"]) == 5
        assert len(sankey["links"]) == 4

    def test_screw_efficiency_range(self):
        """The knowledge base example expects ~66.4% for 32kW/6.2m³/min/7.5bar."""
        resp = client.post("/api/analyze", json={
            "compressor_type": "screw",
            "parameters": {
                "power_kW": 32,
                "flow_rate_m3_min": 6.2,
                "outlet_pressure_bar": 7.5,
                "ambient_temp_C": 25.0,
            },
        })
        assert resp.status_code == 200
        eff = resp.json()["metrics"]["exergy_efficiency_pct"]
        assert 60.0 < eff < 72.0


class TestCompressorTypes:
    def test_returns_4_types(self):
        resp = client.get("/api/compressor-types")
        assert resp.status_code == 200
        types = resp.json()["compressor_types"]
        assert len(types) == 4
        type_names = [t["type"] for t in types]
        assert "screw" in type_names
        assert "piston" in type_names
        assert "scroll" in type_names
        assert "centrifugal" in type_names

    def test_type_has_fields(self):
        resp = client.get("/api/compressor-types")
        for t in resp.json()["compressor_types"]:
            assert len(t["fields"]) >= 9  # At least the common fields
            assert t["name"]
            assert t["description"]


class TestBenchmarks:
    def test_screw_benchmarks(self):
        resp = client.get("/api/benchmarks/screw")
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "screw"
        assert "efficiency_ranges" in data
        assert "spc_ranges" in data
        assert "sector_averages" in data

    def test_piston_benchmarks(self):
        resp = client.get("/api/benchmarks/piston")
        assert resp.status_code == 200

    def test_scroll_benchmarks(self):
        resp = client.get("/api/benchmarks/scroll")
        assert resp.status_code == 200

    def test_centrifugal_benchmarks(self):
        resp = client.get("/api/benchmarks/centrifugal")
        assert resp.status_code == 200

    def test_invalid_type(self):
        resp = client.get("/api/benchmarks/turbo")
        assert resp.status_code == 404


class TestSolutions:
    def test_screw_solutions(self):
        resp = client.get("/api/solutions/screw")
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "screw"
        assert len(data["recommendations"]) > 0

    def test_solutions_with_params(self):
        resp = client.get("/api/solutions/screw?efficiency=30&operating_hours=6000")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["recommendations"]) > 0

    def test_invalid_type(self):
        resp = client.get("/api/solutions/turbo")
        assert resp.status_code == 404

    def test_recommendation_structure(self):
        resp = client.get("/api/solutions/screw")
        for rec in resp.json()["recommendations"]:
            assert "type" in rec
            assert "title" in rec
            assert "priority" in rec
            assert rec["priority"] in ("high", "medium", "low")


# ===========================================================================
# Boiler API tests
# ===========================================================================

class TestBoilerAnalyze:
    def test_steam_firetube(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "boiler",
            "subtype": "steam_firetube",
            "parameters": {
                "fuel_flow_kg_h": 370,
                "steam_flow_kg_h": 5000,
                "steam_pressure_bar": 10,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "steam_firetube"
        assert data["metrics"]["exergy_input_kW"] > 0
        assert data["metrics"]["exergy_output_kW"] > 0
        assert data["metrics"]["thermal_efficiency_pct"] is not None
        assert "sankey" in data
        assert len(data["sankey"]["nodes"]) == 7

    def test_hotwater_boiler(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "boiler",
            "subtype": "hotwater",
            "parameters": {
                "fuel_flow_kg_h": 100,
                "steam_flow_kg_h": 3000,
                "steam_pressure_bar": 3,
                "steam_temp_C": 90,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "hotwater"

    def test_invalid_boiler_type(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "boiler",
            "subtype": "nuclear",
            "parameters": {
                "fuel_flow_kg_h": 370,
                "steam_flow_kg_h": 5000,
                "steam_pressure_bar": 10,
            },
        })
        assert resp.status_code == 422


# ===========================================================================
# Chiller API tests
# ===========================================================================

class TestChillerAnalyze:
    def test_centrifugal_chiller(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "chiller",
            "subtype": "centrifugal",
            "parameters": {
                "cooling_capacity_kW": 500,
                "compressor_power_kW": 83,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "centrifugal"
        assert data["metrics"]["exergy_input_kW"] > 0
        assert data["metrics"]["cop"] is not None
        assert data["metrics"]["cop"] > 0
        assert "sankey" in data

    def test_absorption_chiller(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "chiller",
            "subtype": "absorption",
            "parameters": {
                "cooling_capacity_kW": 500,
                "generator_heat_kW": 700,
                "generator_temp_C": 90,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "absorption"
        assert data["metrics"]["cop"] is not None

    def test_invalid_chiller_type(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "chiller",
            "subtype": "magnetic",
            "parameters": {
                "cooling_capacity_kW": 500,
                "compressor_power_kW": 83,
            },
        })
        assert resp.status_code == 422


# ===========================================================================
# Pump API tests
# ===========================================================================

class TestPumpAnalyze:
    def test_centrifugal_pump(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "pump",
            "subtype": "centrifugal",
            "parameters": {
                "motor_power_kW": 22,
                "flow_rate_m3_h": 80,
                "total_head_m": 45,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["compressor_type"] == "centrifugal"
        assert data["metrics"]["exergy_input_kW"] == 22.0
        assert data["metrics"]["hydraulic_power_kW"] is not None
        assert data["metrics"]["hydraulic_power_kW"] > 0
        assert "sankey" in data
        assert len(data["sankey"]["nodes"]) == 7

    def test_pump_with_throttle(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "pump",
            "subtype": "centrifugal",
            "parameters": {
                "motor_power_kW": 22,
                "flow_rate_m3_h": 80,
                "total_head_m": 45,
                "control_method": "throttle",
                "throttle_loss_pct": 20,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["metrics"]["throttle_loss_kW"] is not None

    def test_invalid_pump_type(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "pump",
            "subtype": "turbo",
            "parameters": {
                "motor_power_kW": 22,
                "flow_rate_m3_h": 80,
                "total_head_m": 45,
            },
        })
        assert resp.status_code == 422


# ===========================================================================
# Equipment config endpoint
# ===========================================================================

class TestEquipmentConfig:
    def test_compressor_config(self):
        resp = client.get("/api/equipment-types/compressor/config")
        assert resp.status_code == 200
        data = resp.json()
        assert data["equipment_type"] == "compressor"
        assert len(data["subtypes"]) == 4

    def test_boiler_config(self):
        resp = client.get("/api/equipment-types/boiler/config")
        assert resp.status_code == 200
        data = resp.json()
        assert data["equipment_type"] == "boiler"
        assert len(data["subtypes"]) == 7
        for st in data["subtypes"]:
            assert len(st["fields"]) > 0

    def test_chiller_config(self):
        resp = client.get("/api/equipment-types/chiller/config")
        assert resp.status_code == 200
        data = resp.json()
        assert data["equipment_type"] == "chiller"
        assert len(data["subtypes"]) == 7  # 6 VC + 1 absorption

    def test_pump_config(self):
        resp = client.get("/api/equipment-types/pump/config")
        assert resp.status_code == 200
        data = resp.json()
        assert data["equipment_type"] == "pump"
        assert len(data["subtypes"]) == 6

    def test_invalid_equipment_config(self):
        resp = client.get("/api/equipment-types/reactor/config")
        assert resp.status_code == 404
