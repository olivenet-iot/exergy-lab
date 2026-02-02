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
        # With AV/UN split: 6 nodes (destruction split into avoidable + unavoidable)
        # Without AV/UN (fallback): 5 nodes
        assert len(sankey["nodes"]) >= 5
        assert len(sankey["links"]) >= 4

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

# ===========================================================================
# Factory API tests
# ===========================================================================

class TestFactoryAPI:
    def _create_project(self, name="Test Fabrika", sector="textile"):
        resp = client.post("/api/factory/projects", json={
            "name": name,
            "sector": sector,
            "description": "Test aciklamasi",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        return data["project"]["id"]

    def _add_compressor(self, project_id, name="Kompresor-1"):
        resp = client.post(f"/api/factory/projects/{project_id}/equipment", json={
            "type": "compressor",
            "subtype": "screw",
            "name": name,
            "parameters": {
                "power_kW": 32,
                "flow_rate_m3_min": 6.2,
                "outlet_pressure_bar": 7.5,
            },
        })
        assert resp.status_code == 200
        return resp.json()["equipment"]["id"]

    def _add_boiler(self, project_id, name="Kazan-1"):
        resp = client.post(f"/api/factory/projects/{project_id}/equipment", json={
            "type": "boiler",
            "subtype": "steam_firetube",
            "name": name,
            "parameters": {
                "fuel_flow_kg_h": 370,
                "steam_flow_kg_h": 5000,
                "steam_pressure_bar": 10,
            },
        })
        assert resp.status_code == 200
        return resp.json()["equipment"]["id"]

    def test_create_project(self):
        resp = client.post("/api/factory/projects", json={
            "name": "Yeni Fabrika",
            "sector": "food",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert data["project"]["name"] == "Yeni Fabrika"
        assert data["project"]["sector"] == "food"
        assert data["project"]["id"]
        assert data["project"]["equipment_count"] == 0

    def test_list_projects(self):
        pid = self._create_project("Liste Test")
        resp = client.get("/api/factory/projects")
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert isinstance(data["projects"], list)
        assert any(p["id"] == pid for p in data["projects"])

    def test_get_project(self):
        pid = self._create_project("Get Test")
        resp = client.get(f"/api/factory/projects/{pid}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["project"]["id"] == pid
        assert data["project"]["name"] == "Get Test"

    def test_get_project_not_found(self):
        resp = client.get("/api/factory/projects/nonexist")
        assert resp.status_code == 404

    def test_add_equipment(self):
        pid = self._create_project()
        resp = client.post(f"/api/factory/projects/{pid}/equipment", json={
            "type": "compressor",
            "subtype": "screw",
            "name": "Kompresör A",
            "parameters": {
                "power_kW": 32,
                "flow_rate_m3_min": 6.2,
                "outlet_pressure_bar": 7.5,
            },
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert data["equipment"]["name"] == "Kompresör A"
        assert data["equipment"]["id"]

        # Verify project now has 1 equipment
        proj = client.get(f"/api/factory/projects/{pid}").json()
        assert proj["project"]["equipment_count"] == 1

    def test_remove_equipment(self):
        pid = self._create_project()
        eq_id = self._add_compressor(pid)

        resp = client.delete(f"/api/factory/projects/{pid}/equipment/{eq_id}")
        assert resp.status_code == 200
        assert resp.json()["success"] is True

        # Verify equipment removed
        proj = client.get(f"/api/factory/projects/{pid}").json()
        assert proj["project"]["equipment_count"] == 0

    def test_remove_equipment_not_found(self):
        pid = self._create_project()
        resp = client.delete(f"/api/factory/projects/{pid}/equipment/nonexist")
        assert resp.status_code == 404

    def test_analyze_factory(self):
        pid = self._create_project()
        self._add_compressor(pid)
        self._add_boiler(pid)

        resp = client.post(f"/api/factory/projects/{pid}/analyze")
        assert resp.status_code == 200
        data = resp.json()

        assert data["success"] is True
        assert data["project_id"] == pid
        assert len(data["equipment_results"]) == 2
        assert "aggregates" in data
        assert "hotspots" in data
        assert "integration_opportunities" in data
        assert "sankey" in data

        # Check aggregates
        agg = data["aggregates"]
        assert agg["equipment_count"] == 2
        assert agg["total_exergy_input_kW"] > 0
        assert agg["total_exergy_destroyed_kW"] > 0
        assert 0 < agg["factory_exergy_efficiency_pct"] < 100

    def test_analyze_empty_project(self):
        pid = self._create_project()
        resp = client.post(f"/api/factory/projects/{pid}/analyze")
        assert resp.status_code == 400

    def test_hotspots_sorted(self):
        pid = self._create_project()
        self._add_compressor(pid, "Small-Comp")
        self._add_boiler(pid, "Big-Boiler")

        resp = client.post(f"/api/factory/projects/{pid}/analyze")
        data = resp.json()
        hotspots = data["hotspots"]

        assert len(hotspots) == 2
        # Should be sorted by exergy destruction descending
        assert hotspots[0]["exergy_destroyed_kW"] >= hotspots[1]["exergy_destroyed_kW"]

    def test_sankey_data(self):
        pid = self._create_project()
        self._add_compressor(pid)
        self._add_boiler(pid)

        resp = client.post(f"/api/factory/projects/{pid}/analyze")
        sankey = resp.json()["sankey"]

        assert "nodes" in sankey
        assert "links" in sankey
        assert "summary" in sankey

        # Should have: 1 input + 2 equipment + 1 useful + 1-2 loss nodes
        # With AV/UN split: 6 nodes; without: 5 nodes
        assert len(sankey["nodes"]) >= 5
        # Should have links for each equipment (input->eq, eq->useful, eq->loss)
        assert len(sankey["links"]) >= 4

    def test_integration_opportunities(self):
        """Compressor + boiler should detect heat recovery integration."""
        pid = self._create_project()
        self._add_compressor(pid)
        self._add_boiler(pid)

        resp = client.post(f"/api/factory/projects/{pid}/analyze")
        data = resp.json()

        opportunities = data["integration_opportunities"]
        # Should detect at least compressor heat -> boiler or compressor heat -> space
        assert len(opportunities) >= 1

        # Verify opportunity structure
        for opp in opportunities:
            assert "type" in opp
            assert "title" in opp
            assert "source" in opp
            assert "estimated_savings_EUR_year" in opp


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
