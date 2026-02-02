"""Tests for multi-equipment support."""

import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


class TestEquipmentTypes:
    def test_returns_7_types(self):
        resp = client.get("/api/equipment-types")
        assert resp.status_code == 200
        types = resp.json()["equipment_types"]
        assert len(types) == 7
        type_ids = [t["id"] for t in types]
        assert "compressor" in type_ids
        assert "boiler" in type_ids
        assert "chiller" in type_ids
        assert "pump" in type_ids
        assert "heat_exchanger" in type_ids
        assert "steam_turbine" in type_ids
        assert "dryer" in type_ids

    def test_each_type_has_subtypes(self):
        resp = client.get("/api/equipment-types")
        for t in resp.json()["equipment_types"]:
            assert len(t["subtypes"]) > 0
            assert t["name"]
            assert t["name_en"]
            assert t["icon"]

    def test_subtype_counts(self):
        resp = client.get("/api/equipment-types")
        types = {t["id"]: t for t in resp.json()["equipment_types"]}
        assert len(types["compressor"]["subtypes"]) == 6
        assert len(types["boiler"]["subtypes"]) == 7
        assert len(types["chiller"]["subtypes"]) == 7
        assert len(types["pump"]["subtypes"]) == 6
        assert len(types["heat_exchanger"]["subtypes"]) == 7
        assert len(types["steam_turbine"]["subtypes"]) == 5
        assert len(types["dryer"]["subtypes"]) == 8


class TestEquipmentSubtypes:
    def test_compressor_subtypes(self):
        resp = client.get("/api/equipment-types/compressor/subtypes")
        assert resp.status_code == 200
        subtypes = resp.json()["subtypes"]
        assert len(subtypes) == 6
        ids = [s["id"] for s in subtypes]
        assert "screw" in ids
        assert "piston" in ids

    def test_boiler_subtypes(self):
        resp = client.get("/api/equipment-types/boiler/subtypes")
        assert resp.status_code == 200
        assert len(resp.json()["subtypes"]) == 7

    def test_chiller_subtypes(self):
        resp = client.get("/api/equipment-types/chiller/subtypes")
        assert resp.status_code == 200
        assert len(resp.json()["subtypes"]) == 7

    def test_pump_subtypes(self):
        resp = client.get("/api/equipment-types/pump/subtypes")
        assert resp.status_code == 200
        assert len(resp.json()["subtypes"]) == 6

    def test_heat_exchanger_subtypes(self):
        resp = client.get("/api/equipment-types/heat_exchanger/subtypes")
        assert resp.status_code == 200
        subtypes = resp.json()["subtypes"]
        assert len(subtypes) == 7
        ids = [s["id"] for s in subtypes]
        assert "shell_tube" in ids
        assert "plate" in ids

    def test_steam_turbine_subtypes(self):
        resp = client.get("/api/equipment-types/steam_turbine/subtypes")
        assert resp.status_code == 200
        subtypes = resp.json()["subtypes"]
        assert len(subtypes) == 5
        ids = [s["id"] for s in subtypes]
        assert "back_pressure" in ids
        assert "condensing" in ids

    def test_dryer_subtypes(self):
        resp = client.get("/api/equipment-types/dryer/subtypes")
        assert resp.status_code == 200
        subtypes = resp.json()["subtypes"]
        assert len(subtypes) == 8
        ids = [s["id"] for s in subtypes]
        assert "convective" in ids
        assert "rotary" in ids

    def test_invalid_type_returns_404(self):
        resp = client.get("/api/equipment-types/turbine/subtypes")
        assert resp.status_code == 404


class TestAnalyzeEquipment:
    def test_new_format_compressor(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "compressor",
            "subtype": "screw",
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

    def test_boiler_empty_params_uses_defaults(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "boiler",
            "subtype": "steam_firetube",
            "parameters": {},
        })
        # All fields have defaults, empty params succeeds
        assert resp.status_code == 200

    def test_chiller_empty_params_uses_defaults(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "chiller",
            "subtype": "screw",
            "parameters": {},
        })
        assert resp.status_code == 200

    def test_pump_empty_params_uses_defaults(self):
        resp = client.post("/api/analyze", json={
            "equipment_type": "pump",
            "subtype": "centrifugal",
            "parameters": {},
        })
        assert resp.status_code == 200


class TestFactoryProjects:
    def test_create_project(self):
        resp = client.post("/api/factory/projects", json={
            "name": "Test Fabrikasi",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert data["project"]["name"] == "Test Fabrikasi"
        assert data["project"]["id"] is not None

    def test_get_project(self):
        # Create first
        create_resp = client.post("/api/factory/projects", json={
            "name": "Test Fabrikasi 2",
        })
        project_id = create_resp.json()["project"]["id"]

        # Get
        resp = client.get(f"/api/factory/projects/{project_id}")
        assert resp.status_code == 200
        assert resp.json()["project"]["name"] == "Test Fabrikasi 2"

    def test_get_nonexistent_project_returns_404(self):
        resp = client.get("/api/factory/projects/nonexistent")
        assert resp.status_code == 404
