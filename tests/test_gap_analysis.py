"""Tests for engine/gap_analysis.py — top-down exergetic gap analysis."""

import pytest

from engine.process_exergy import ProcessDefinition
from engine.gap_analysis import (
    GapAnalysisResult,
    analyze_gap,
    _calculate_gap_distribution,
    _calculate_sustainability_index,
    _build_waterfall_data,
    _build_comparison_bar_data,
    _build_gap_pie_data,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def drying_process():
    return ProcessDefinition(
        process_type="drying",
        process_label="Tahıl kurutma hattı",
        parameters={"mass_flow_kg_h": 1000, "moisture_in_pct": 20, "moisture_out_pct": 5},
        subcategory="food_grain",
        operating_hours=6000,
        energy_price_eur_kwh=0.08,
    )


@pytest.fixture
def mock_equipment_results():
    return [
        {
            "id": "eq1", "name": "Kompresör 1", "equipment_type": "compressor",
            "subtype": "screw",
            "analysis": {"exergy_in_kW": 100, "exergy_destroyed_kW": 40, "exergy_efficiency_pct": 60},
        },
        {
            "id": "eq2", "name": "Kazan 1", "equipment_type": "boiler",
            "subtype": "steam_firetube",
            "analysis": {"exergy_in_kW": 200, "exergy_destroyed_kW": 120, "exergy_efficiency_pct": 40},
        },
        {
            "id": "eq3", "name": "Pompa 1", "equipment_type": "pump",
            "subtype": "centrifugal",
            "analysis": {"exergy_in_kW": 50, "exergy_destroyed_kW": 15, "exergy_efficiency_pct": 70},
        },
    ]


@pytest.fixture
def mock_aggregates():
    return {
        "total_exergy_input_kW": 350,
        "total_exergy_output_kW": 175,
        "total_exergy_destroyed_kW": 175,
        "factory_exergy_efficiency_pct": 50.0,
        "equipment_count": 3,
    }


@pytest.fixture
def mock_hotspots():
    return [
        {"id": "eq2", "name": "Kazan 1", "exergy_destroyed_kW": 120, "priority": "high"},
        {"id": "eq1", "name": "Kompresör 1", "exergy_destroyed_kW": 40, "priority": "medium"},
        {"id": "eq3", "name": "Pompa 1", "exergy_destroyed_kW": 15, "priority": "low"},
    ]


# ---------------------------------------------------------------------------
# GapAnalysisResult
# ---------------------------------------------------------------------------

class TestGapAnalysisResult:

    def test_to_dict(self):
        result = GapAnalysisResult(
            process_type="heating", process_label="Test", subcategory="general",
            minimum_exergy_kW=10, bat_exergy_kW=50, actual_exergy_kW=100,
            total_gap_kW=90, bat_gap_kW=50, technology_gap_kW=40,
            total_gap_pct=90.0, bat_gap_pct=50.0, technology_gap_pct=40.0,
            specific_actual=0.1, specific_bat=0.05, specific_minimum=0.01,
            specific_unit="kWh/kg",
            actual_to_minimum_ratio=10.0, actual_to_bat_ratio=2.0,
        )
        d = result.to_dict()
        assert isinstance(d, dict)
        assert d["process_type"] == "heating"
        assert d["minimum_exergy_kW"] == 10
        assert d["total_gap_kW"] == 90


# ---------------------------------------------------------------------------
# analyze_gap (integration)
# ---------------------------------------------------------------------------

class TestAnalyzeGap:

    def test_gap_hierarchy(self, drying_process, mock_equipment_results,
                           mock_aggregates, mock_hotspots):
        """minimum < BAT < actual always holds."""
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        assert result.minimum_exergy_kW < result.bat_exergy_kW
        assert result.bat_exergy_kW < result.actual_exergy_kW

    def test_gap_percentages(self, drying_process, mock_equipment_results,
                             mock_aggregates, mock_hotspots):
        """bat_gap_pct + technology_gap_pct ≈ total_gap_pct."""
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        assert abs(
            result.bat_gap_pct + result.technology_gap_pct - result.total_gap_pct
        ) < 0.5  # rounding tolerance

    def test_process_info_populated(self, drying_process, mock_equipment_results,
                                     mock_aggregates, mock_hotspots):
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        assert result.process_type == "drying"
        assert result.process_label == "Tahıl kurutma hattı"
        assert result.subcategory == "food_grain"

    def test_economic_impact(self, drying_process, mock_equipment_results,
                             mock_aggregates, mock_hotspots):
        """annual_cost = gap × price × hours."""
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
            energy_price_eur_kwh=0.10,
            operating_hours=8000,
        )
        expected_total = result.total_gap_kW * 0.10 * 8000
        assert abs(result.annual_total_gap_cost_eur - round(expected_total, 0)) < 10

    def test_esi_in_range(self, drying_process, mock_equipment_results,
                          mock_aggregates, mock_hotspots):
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        assert 0 <= result.exergetic_sustainability_index <= 1
        assert result.grade in ("A", "B", "C", "D", "E", "F")

    def test_bat_info_populated(self, drying_process, mock_equipment_results,
                                 mock_aggregates, mock_hotspots):
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        assert result.bat_technology
        assert result.bat_source
        assert result.bat_efficiency_pct > 0

    def test_visualization_data_present(self, drying_process, mock_equipment_results,
                                         mock_aggregates, mock_hotspots):
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        assert "labels" in result.waterfall_data
        assert "values" in result.waterfall_data
        assert "categories" in result.comparison_bar_data
        assert "labels" in result.gap_pie_data

    def test_to_dict_serializable(self, drying_process, mock_equipment_results,
                                   mock_aggregates, mock_hotspots):
        """to_dict produces JSON-serializable output."""
        import json
        result = analyze_gap(
            drying_process, mock_equipment_results,
            mock_aggregates, mock_hotspots,
        )
        d = result.to_dict()
        json_str = json.dumps(d)
        assert len(json_str) > 100

    def test_zero_actual_fallback(self, drying_process, mock_equipment_results):
        """When aggregates has 0 input, fall back to equipment sum."""
        agg = {"total_exergy_input_kW": 0}
        result = analyze_gap(
            drying_process, mock_equipment_results, agg, [],
        )
        # Falls back to equipment sum: 100 + 200 + 50 = 350
        assert result.actual_exergy_kW > 0


# ---------------------------------------------------------------------------
# _calculate_gap_distribution
# ---------------------------------------------------------------------------

class TestGapDistribution:

    def test_sorted_by_destroyed(self, mock_equipment_results):
        dist = _calculate_gap_distribution(mock_equipment_results, [])
        if len(dist) >= 2:
            assert dist[0]["destroyed_kW"] >= dist[1]["destroyed_kW"]

    def test_share_percentages(self, mock_equipment_results):
        dist = _calculate_gap_distribution(mock_equipment_results, [])
        total_share = sum(item["gap_share_pct"] for item in dist)
        # Should be close to 100 (small items may be skipped)
        assert total_share > 90

    def test_priority_assignment(self, mock_equipment_results):
        dist = _calculate_gap_distribution(mock_equipment_results, [])
        for item in dist:
            assert item["priority"] in ("critical", "high", "medium", "low")

    def test_empty_results(self):
        dist = _calculate_gap_distribution([], [])
        assert dist == []

    def test_zero_destruction(self):
        eq = [{"name": "X", "equipment_type": "pump",
               "analysis": {"exergy_destroyed_kW": 0}}]
        dist = _calculate_gap_distribution(eq, [])
        assert dist == []


# ---------------------------------------------------------------------------
# _calculate_sustainability_index
# ---------------------------------------------------------------------------

class TestSustainabilityIndex:

    def test_esi_range(self):
        esi, grade, desc = _calculate_sustainability_index(50, 100)
        assert 0 <= esi <= 1
        assert esi == 0.5

    def test_grade_a(self):
        _, grade, _ = _calculate_sustainability_index(60, 100)
        assert grade == "A"

    def test_grade_f(self):
        _, grade, _ = _calculate_sustainability_index(1, 100)
        assert grade == "F"

    def test_zero_actual(self):
        esi, grade, _ = _calculate_sustainability_index(50, 0)
        assert esi == 0.0
        assert grade == "F"

    def test_zero_minimum(self):
        esi, grade, _ = _calculate_sustainability_index(0, 100)
        assert esi == 0.0
        assert grade == "F"

    @pytest.mark.parametrize("min_kW,actual_kW,expected_grade", [
        (55, 100, "A"),
        (40, 100, "B"),
        (25, 100, "C"),
        (12, 100, "D"),
        (7, 100, "E"),
        (2, 100, "F"),
    ])
    def test_grade_thresholds(self, min_kW, actual_kW, expected_grade):
        _, grade, _ = _calculate_sustainability_index(min_kW, actual_kW)
        assert grade == expected_grade


# ---------------------------------------------------------------------------
# Visualization builders
# ---------------------------------------------------------------------------

class TestWaterfallData:

    def test_structure(self):
        gap_dist = [
            {"equipment_name": "Kazan", "destroyed_kW": 50},
            {"equipment_name": "Kompresör", "destroyed_kW": 20},
        ]
        data = _build_waterfall_data(10, 40, 100, 30, gap_dist)
        assert data["labels"][0] == "Minimum"
        assert data["labels"][-1] == "Mevcut Tesis"
        assert data["types"][0] == "absolute"
        assert data["types"][-1] == "total"
        assert len(data["labels"]) == len(data["values"]) == len(data["types"])

    def test_empty_gap_dist(self):
        data = _build_waterfall_data(10, 40, 100, 30, [])
        assert len(data["labels"]) == 3  # Minimum, Teknoloji Limiti, Mevcut Tesis


class TestComparisonBarData:

    def test_three_values(self):
        data = _build_comparison_bar_data(10, 40, 100)
        assert len(data["values"]) == 3
        assert len(data["categories"]) == 3
        assert len(data["colors"]) == 3
        assert data["values"][0] < data["values"][1] < data["values"][2]


class TestGapPieData:

    def test_basic(self):
        gap_dist = [
            {"equipment_name": "A", "destroyed_kW": 50},
            {"equipment_name": "B", "destroyed_kW": 30},
        ]
        data = _build_gap_pie_data(gap_dist)
        assert len(data["labels"]) == 2
        assert data["values"] == [50.0, 30.0]

    def test_overflow_to_other(self):
        """More than 7 items collapses into 'Diğer'."""
        gap_dist = [
            {"equipment_name": f"Eq{i}", "destroyed_kW": 10 - i}
            for i in range(10)
        ]
        data = _build_gap_pie_data(gap_dist)
        assert data["labels"][-1] == "Diğer"
        assert len(data["labels"]) == 8  # 7 + Diğer

    def test_empty(self):
        data = _build_gap_pie_data([])
        assert data["labels"] == []
        assert data["values"] == []


# ---------------------------------------------------------------------------
# Different process types integration
# ---------------------------------------------------------------------------

class TestMultipleProcessTypes:
    """Run gap analysis with different process types to verify no crashes."""

    PROCESS_CONFIGS = [
        ("heating", {"mass_flow_kg_h": 500, "temp_in_C": 20, "temp_out_C": 80}),
        ("cooling", {"cooling_load_kW": 100, "cold_temp_C": -10}),
        ("compressed_air", {"air_flow_m3_min": 10, "discharge_pressure_bar": 7}),
        ("chp", {"fuel_input_kW": 1000, "electrical_output_kW": 350, "thermal_output_kW": 400}),
        ("cold_storage", {"heat_load_kW": 50, "target_temp_C": -20}),
        ("general_manufacturing", {"production_rate_ton_h": 5}),
    ]

    @pytest.mark.parametrize("ptype,params", PROCESS_CONFIGS)
    def test_process_type_runs(self, ptype, params,
                                mock_equipment_results, mock_aggregates, mock_hotspots):
        proc = ProcessDefinition(
            process_type=ptype, process_label=f"Test {ptype}",
            parameters=params, subcategory="general",
        )
        result = analyze_gap(proc, mock_equipment_results, mock_aggregates, mock_hotspots)
        assert result.minimum_exergy_kW < result.actual_exergy_kW
        assert result.grade in ("A", "B", "C", "D", "E", "F")
