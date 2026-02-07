"""Tests for engine/bat_references.py — BAT reference database."""

import pytest

from engine.bat_references import (
    BAT_REFERENCES,
    get_bat_reference,
    get_available_subcategories,
    calculate_bat_exergy,
)
from engine.process_exergy import ProcessDefinition


# ---------------------------------------------------------------------------
# BAT_REFERENCES structure tests
# ---------------------------------------------------------------------------

class TestBATReferencesStructure:
    """Verify BAT_REFERENCES dict completeness and integrity."""

    EXPECTED_TYPES = [
        "drying", "heating", "cooling", "steam_generation",
        "compressed_air", "chp", "cold_storage", "general_manufacturing",
    ]

    def test_all_process_types_present(self):
        """All 8 process types exist in BAT_REFERENCES."""
        for ptype in self.EXPECTED_TYPES:
            assert ptype in BAT_REFERENCES, f"Missing process type: {ptype}"

    def test_all_process_types_have_general(self):
        """Every process type has a 'general' subcategory."""
        for ptype in self.EXPECTED_TYPES:
            assert "general" in BAT_REFERENCES[ptype], (
                f"{ptype} missing 'general' subcategory"
            )

    def test_bat_values_positive(self):
        """All BAT specific_exergy_kwh_per_unit values are positive."""
        for ptype, subcats in BAT_REFERENCES.items():
            for subcat, ref in subcats.items():
                assert ref["specific_exergy_kwh_per_unit"] > 0, (
                    f"{ptype}/{subcat}: specific_exergy must be > 0"
                )

    def test_bat_efficiency_in_range(self):
        """All BAT efficiency values are 0-100%."""
        for ptype, subcats in BAT_REFERENCES.items():
            for subcat, ref in subcats.items():
                pct = ref["exergy_efficiency_pct"]
                assert 0 < pct <= 100, (
                    f"{ptype}/{subcat}: efficiency {pct} out of range"
                )

    def test_required_fields_present(self):
        """Every BAT entry has all required fields."""
        required = {"label", "specific_exergy_kwh_per_unit", "unit",
                    "exergy_efficiency_pct", "technology", "source"}
        for ptype, subcats in BAT_REFERENCES.items():
            for subcat, ref in subcats.items():
                missing = required - set(ref.keys())
                assert not missing, (
                    f"{ptype}/{subcat} missing fields: {missing}"
                )


# ---------------------------------------------------------------------------
# get_bat_reference tests
# ---------------------------------------------------------------------------

class TestGetBATReference:

    def test_known_subcategory(self):
        ref = get_bat_reference("drying", "food_grain")
        assert ref["label"] == "Tahıl Kurutma"
        assert ref["specific_exergy_kwh_per_unit"] > 0

    def test_fallback_to_general(self):
        """Unknown subcategory falls back to 'general'."""
        ref = get_bat_reference("drying", "nonexistent_subcat")
        assert ref["label"] == BAT_REFERENCES["drying"]["general"]["label"]

    def test_general_explicit(self):
        ref = get_bat_reference("heating", "general")
        assert ref["specific_exergy_kwh_per_unit"] > 0

    def test_unknown_process_type_raises(self):
        with pytest.raises(ValueError, match="BAT referansı bulunamadı"):
            get_bat_reference("nonexistent_type")


# ---------------------------------------------------------------------------
# get_available_subcategories tests
# ---------------------------------------------------------------------------

class TestGetAvailableSubcategories:

    def test_returns_list(self):
        result = get_available_subcategories("drying")
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_subcategory_dict_structure(self):
        result = get_available_subcategories("drying")
        for item in result:
            assert "key" in item
            assert "label" in item
            assert "source" in item

    def test_drying_subcategories(self):
        result = get_available_subcategories("drying")
        keys = [item["key"] for item in result]
        assert "food_grain" in keys
        assert "general" in keys

    def test_unknown_type_raises(self):
        with pytest.raises(ValueError):
            get_available_subcategories("nonexistent_type")


# ---------------------------------------------------------------------------
# calculate_bat_exergy tests
# ---------------------------------------------------------------------------

class TestCalculateBATExergy:

    def test_positive_result(self):
        process_def = ProcessDefinition(
            process_type="drying",
            process_label="Test",
            parameters={"mass_flow_kg_h": 1000, "moisture_in_pct": 20, "moisture_out_pct": 5},
        )
        min_result = {
            "production_rate_unit": 150.0,
            "minimum_exergy_kW": 2.0,
        }
        bat = calculate_bat_exergy(process_def, min_result)
        assert bat["bat_exergy_kW"] > 0
        assert "bat_technology" in bat
        assert "bat_source" in bat

    def test_zero_production_rate(self):
        process_def = ProcessDefinition(
            process_type="heating",
            process_label="Test",
            parameters={"mass_flow_kg_h": 100, "temp_in_C": 20, "temp_out_C": 80},
        )
        min_result = {"production_rate_unit": 0.0}
        bat = calculate_bat_exergy(process_def, min_result)
        assert bat["bat_exergy_kW"] == 0.0

    def test_bat_label_populated(self):
        process_def = ProcessDefinition(
            process_type="compressed_air",
            process_label="Test",
            parameters={"air_flow_m3_min": 10, "discharge_pressure_bar": 7},
        )
        min_result = {"production_rate_unit": 600.0}
        bat = calculate_bat_exergy(process_def, min_result)
        assert bat["bat_label"] == "Basınçlı Hava Sistemi"
