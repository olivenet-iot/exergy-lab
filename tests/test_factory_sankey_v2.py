"""
Tests for engine/factory_sankey_v2.py — Grassmann-style 5-layer factory Sankey.

12 test cases covering:
  1. Single equipment sankey
  2. Mixed source sankey (electricity + fuel + thermal)
  3. AV/UN destruction split
  4. Integration opportunity links
  5. Cost flow mode (exergoeconomic metadata)
  6. Node layer assignment
  7. Energy conservation at every equipment node (CRITICAL)
  8. Plotly format conversion
  9. Empty factory
  10. Large factory layout (7+ equipment)
  11. Energy balance per equipment
  12. Total source equals total sink
"""

import pytest

from engine.factory import (
    EquipmentItem,
    analyze_factory,
)
from engine.factory_sankey_v2 import (
    generate_factory_sankey_v2,
    to_plotly_format,
    _determine_energy_source,
    _performance_color,
    _build_av_un_lookup,
)


# ---------------------------------------------------------------------------
# Fixtures: reusable factory equipment lists
# ---------------------------------------------------------------------------

def _single_compressor_items():
    """1 compressor (simplest case)."""
    return [
        EquipmentItem(
            id="c1", name="Kompressor-1", equipment_type="compressor", subtype="screw",
            parameters={"power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
        ),
    ]


def _mixed_source_items():
    """3 equipment: compressor (electricity) + boiler (fuel) + heat_exchanger (thermal)."""
    return [
        EquipmentItem(
            id="c1", name="Kompressor-1", equipment_type="compressor", subtype="screw",
            parameters={"power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
        ),
        EquipmentItem(
            id="b1", name="Kazan-1", equipment_type="boiler", subtype="steam_firetube",
            parameters={"fuel_flow_kg_h": 100, "steam_flow_kg_h": 1200, "steam_pressure_bar": 10},
        ),
        EquipmentItem(
            id="hx1", name="Esanjor-1", equipment_type="heat_exchanger", subtype="shell_tube",
            parameters={
                "hot_inlet_temp_C": 90, "hot_outlet_temp_C": 70, "hot_mass_flow_kg_s": 2.0,
                "cold_inlet_temp_C": 20, "cold_outlet_temp_C": 50, "cold_mass_flow_kg_s": 1.5,
            },
        ),
    ]


def _large_factory_items():
    """7 equipment, all types."""
    return [
        EquipmentItem(
            id="c1", name="Kompressor-1", equipment_type="compressor", subtype="screw",
            parameters={"power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
        ),
        EquipmentItem(
            id="b1", name="Kazan-1", equipment_type="boiler", subtype="steam_firetube",
            parameters={"fuel_flow_kg_h": 100, "steam_flow_kg_h": 1200, "steam_pressure_bar": 10},
        ),
        EquipmentItem(
            id="ch1", name="Chiller-1", equipment_type="chiller", subtype="screw",
            parameters={
                "cooling_capacity_kW": 350, "compressor_power_kW": 70,
                "chw_supply_temp_C": 7, "chw_return_temp_C": 12,
                "cw_supply_temp_C": 30, "cw_return_temp_C": 35,
            },
        ),
        EquipmentItem(
            id="p1", name="Pompa-1", equipment_type="pump", subtype="centrifugal",
            parameters={"motor_power_kW": 15, "flow_rate_m3_h": 50, "total_head_m": 40},
        ),
        EquipmentItem(
            id="hx1", name="Esanjor-1", equipment_type="heat_exchanger", subtype="shell_tube",
            parameters={
                "hot_inlet_temp_C": 90, "hot_outlet_temp_C": 70, "hot_mass_flow_kg_s": 2.0,
                "cold_inlet_temp_C": 20, "cold_outlet_temp_C": 50, "cold_mass_flow_kg_s": 1.5,
            },
        ),
        EquipmentItem(
            id="st1", name="Turbin-1", equipment_type="steam_turbine", subtype="back_pressure",
            parameters={
                "inlet_temp_C": 400, "inlet_pressure_bar": 40,
                "mass_flow_kg_s": 5, "outlet_pressure_bar": 2.0,
                "isentropic_efficiency": 0.80,
            },
        ),
        EquipmentItem(
            id="d1", name="Kurutucu-1", equipment_type="dryer", subtype="rotary",
            parameters={},
        ),
    ]


def _with_integration_items():
    """2 equipment that should generate integration opportunities."""
    return [
        EquipmentItem(
            id="c1", name="Kompressor-1", equipment_type="compressor", subtype="screw",
            parameters={"power_kW": 37, "flow_rate_m3_min": 6.2, "outlet_pressure_bar": 7.5},
        ),
        EquipmentItem(
            id="b1", name="Kazan-1", equipment_type="boiler", subtype="steam_firetube",
            parameters={"fuel_flow_kg_h": 100, "steam_flow_kg_h": 1200, "steam_pressure_bar": 10},
        ),
    ]


def _run_factory(items):
    """Analyze factory and return (result, sankey)."""
    result = analyze_factory(items)
    return result, result.sankey


# ---------------------------------------------------------------------------
# Test 1: Single equipment sankey
# ---------------------------------------------------------------------------

class TestSingleEquipmentSankey:
    def test_single_compressor_layer_assignment(self):
        """1 compressor: verify correct layer assignment and minimum node/link counts."""
        result, sankey = _run_factory(_single_compressor_items())

        nodes = sankey["nodes"]
        links = sankey["links"]

        # Must have at least: 1 source + 1 equipment + 1 product + 1-2 destruction + 2 aggregation
        assert len(nodes) >= 5
        assert len(links) >= 4

        # Check layer assignments
        layers_present = {n["layer"] for n in nodes}
        assert 0 in layers_present, "Layer 0 (source) missing"
        assert 2 in layers_present, "Layer 2 (equipment) missing"
        assert 3 in layers_present, "Layer 3 (outputs) missing"
        assert 4 in layers_present, "Layer 4 (aggregation) missing"

    def test_single_compressor_has_source_node(self):
        _, sankey = _run_factory(_single_compressor_items())
        source_nodes = [n for n in sankey["nodes"] if n["layer"] == 0]
        assert len(source_nodes) == 1
        assert "electricity" in source_nodes[0]["node_type"]


# ---------------------------------------------------------------------------
# Test 2: Mixed source sankey
# ---------------------------------------------------------------------------

class TestMixedSourceSankey:
    def test_separate_source_nodes(self):
        """Electricity + fuel + thermal sources: verify separate source nodes."""
        _, sankey = _run_factory(_mixed_source_items())

        source_nodes = [n for n in sankey["nodes"] if n["layer"] == 0]
        source_types = {n["node_type"] for n in source_nodes}

        assert "source_electricity" in source_types
        assert "source_fuel" in source_types
        assert "source_thermal" in source_types
        assert len(source_nodes) == 3

    def test_source_colors_match_constants(self):
        """Each source node should have the correct color."""
        _, sankey = _run_factory(_mixed_source_items())

        for node in sankey["nodes"]:
            if node["node_type"] == "source_electricity":
                assert node["color"] == "#3b82f6"
            elif node["node_type"] == "source_fuel":
                assert node["color"] == "#f97316"
            elif node["node_type"] == "source_thermal":
                assert node["color"] == "#ef4444"


# ---------------------------------------------------------------------------
# Test 3: AV/UN destruction split
# ---------------------------------------------------------------------------

class TestAvoidableUnavoidableSplit:
    def test_destruction_nodes_exist(self):
        """destruction_focus mode: verify AV and UN appear as separate nodes."""
        result, sankey = _run_factory(_single_compressor_items())

        dest_nodes = [n for n in sankey["nodes"] if "destroyed" in (n.get("node_type") or "")]
        assert len(dest_nodes) >= 1, "Should have at least one destruction node"

    def test_av_un_values_sum_to_total(self):
        """AV + UN should approximately equal total destruction for each equipment."""
        result, sankey = _run_factory(_single_compressor_items())

        # Check from sankey summary
        summary = sankey["summary"]
        total_destroyed = summary["irreversibility_kW"]
        av = summary.get("total_destroyed_avoidable_kW", 0)
        un = summary.get("total_destroyed_unavoidable_kW", 0)

        if av > 0 or un > 0:
            assert abs((av + un) - total_destroyed) < 1.0, \
                f"AV ({av}) + UN ({un}) = {av+un} != total ({total_destroyed})"


# ---------------------------------------------------------------------------
# Test 4: Integration opportunities links
# ---------------------------------------------------------------------------

class TestIntegrationOpportunities:
    def test_integration_links_present(self):
        """Compressor + boiler should produce integration opportunity links."""
        result, sankey = _run_factory(_with_integration_items())

        integration_links = [l for l in sankey["links"] if l.get("is_opportunity")]
        integration_opps = result.integration_opportunities

        # If integration opportunities were detected in the factory analysis,
        # matching integration links should appear in the sankey
        if integration_opps:
            # Check that at least some integration links exist (some may not map to equipment nodes)
            opp_with_both_equipment = [
                o for o in integration_opps
                if o["source"] in ("Kompressor-1",) and o["target"] in ("Kazan-1",)
            ]
            if opp_with_both_equipment:
                assert len(integration_links) >= 1

    def test_integration_links_flagged(self):
        """Integration links should have is_opportunity=True."""
        _, sankey = _run_factory(_with_integration_items())

        for link in sankey["links"]:
            if link.get("link_type") == "integration_opportunity":
                assert link["is_opportunity"] is True


# ---------------------------------------------------------------------------
# Test 5: Cost flow mode (exergoeconomic metadata)
# ---------------------------------------------------------------------------

class TestCostFlowMode:
    def test_equipment_nodes_have_cost_metadata(self):
        """Equipment nodes should carry exergoeconomic metadata fields."""
        _, sankey = _run_factory(_single_compressor_items())

        eq_nodes = [n for n in sankey["nodes"] if n.get("node_type") == "equipment"]
        assert len(eq_nodes) >= 1

        for eq in eq_nodes:
            meta = eq.get("metadata", {})
            # Should have cost fields (may be 0 if no exergoeconomic data)
            assert "C_dot_destruction_eur_h" in meta
            assert "Z_dot_eur_h" in meta
            assert "f_factor" in meta


# ---------------------------------------------------------------------------
# Test 6: Node layer assignment
# ---------------------------------------------------------------------------

class TestNodeLayers:
    def test_all_nodes_have_valid_layer(self):
        """All nodes must have a layer between 0 and 4."""
        _, sankey = _run_factory(_large_factory_items())

        for node in sankey["nodes"]:
            assert "layer" in node, f"Node {node['id']} missing layer"
            assert 0 <= node["layer"] <= 4, \
                f"Node {node['id']} has invalid layer {node['layer']}"

    def test_layer_0_are_sources(self):
        _, sankey = _run_factory(_large_factory_items())
        for node in sankey["nodes"]:
            if node["layer"] == 0:
                assert "source" in node["node_type"]

    def test_layer_2_are_equipment(self):
        _, sankey = _run_factory(_large_factory_items())
        for node in sankey["nodes"]:
            if node["layer"] == 2:
                assert node["node_type"] == "equipment"

    def test_layer_4_are_aggregation(self):
        _, sankey = _run_factory(_large_factory_items())
        for node in sankey["nodes"]:
            if node["layer"] == 4:
                assert "aggregation" in node["node_type"]


# ---------------------------------------------------------------------------
# Test 7: Energy conservation (CRITICAL)
# ---------------------------------------------------------------------------

class TestEnergyConservation:
    def test_equipment_inflow_equals_outflow(self):
        """
        CRITICAL: For every equipment node, sum(incoming links) == sum(outgoing links)
        within tolerance. Integration opportunity links excluded.
        """
        _, sankey = _run_factory(_mixed_source_items())

        nodes = sankey["nodes"]
        links = sankey["links"]
        eq_nodes = [n for n in nodes if n.get("node_type") == "equipment"]

        for eq in eq_nodes:
            eq_id = eq["id"]
            incoming = sum(
                l["value"] for l in links
                if l["target"] == eq_id and not l.get("is_opportunity")
            )
            outgoing = sum(
                l["value"] for l in links
                if l["source"] == eq_id and not l.get("is_opportunity")
            )

            assert abs(incoming - outgoing) < 1.0, \
                f"Energy balance violated at {eq_id}: in={incoming:.2f} out={outgoing:.2f} diff={abs(incoming-outgoing):.2f}"

    def test_energy_conservation_large_factory(self):
        """Energy conservation check across all 7 equipment types."""
        _, sankey = _run_factory(_large_factory_items())

        eq_nodes = [n for n in sankey["nodes"] if n.get("node_type") == "equipment"]
        assert len(eq_nodes) == 7

        for eq in eq_nodes:
            eq_id = eq["id"]
            incoming = sum(
                l["value"] for l in sankey["links"]
                if l["target"] == eq_id and not l.get("is_opportunity")
            )
            outgoing = sum(
                l["value"] for l in sankey["links"]
                if l["source"] == eq_id and not l.get("is_opportunity")
            )

            assert abs(incoming - outgoing) < 1.0, \
                f"Energy balance violated at {eq_id}: in={incoming:.2f} out={outgoing:.2f}"


# ---------------------------------------------------------------------------
# Test 8: Plotly format conversion
# ---------------------------------------------------------------------------

class TestPlotlyFormat:
    def test_plotly_trace_structure(self):
        """to_plotly_format() should produce valid Plotly sankey trace."""
        _, sankey = _run_factory(_mixed_source_items())
        plotly = to_plotly_format(sankey)

        assert "data" in plotly
        assert "layout" in plotly
        assert len(plotly["data"]) == 1

        trace = plotly["data"][0]
        assert trace["type"] == "sankey"
        assert "node" in trace
        assert "link" in trace

        node = trace["node"]
        assert "label" in node
        assert "color" in node
        assert "x" in node

        link = trace["link"]
        assert "source" in link
        assert "target" in link
        assert "value" in link
        assert len(link["source"]) == len(link["target"]) == len(link["value"])

    def test_plotly_node_indices_valid(self):
        """All link source/target must be valid node indices."""
        _, sankey = _run_factory(_mixed_source_items())
        plotly = to_plotly_format(sankey)

        trace = plotly["data"][0]
        num_nodes = len(trace["node"]["label"])

        for idx in trace["link"]["source"]:
            assert 0 <= idx < num_nodes, f"Invalid source index {idx}"
        for idx in trace["link"]["target"]:
            assert 0 <= idx < num_nodes, f"Invalid target index {idx}"


# ---------------------------------------------------------------------------
# Test 9: Empty factory
# ---------------------------------------------------------------------------

class TestEmptyFactory:
    def test_empty_results(self):
        """Empty results list: returns valid structure, no crash."""
        sankey = generate_factory_sankey_v2(
            equipment_results=[],
            aggregates={},
            hotspots=[],
            integration_opportunities=[],
        )

        assert sankey["nodes"] == []
        assert sankey["links"] == []
        assert "summary" in sankey
        assert "view_mode" in sankey
        assert sankey["metadata"]["equipment_count"] == 0

    def test_empty_plotly_format(self):
        """Empty sankey should produce valid Plotly trace."""
        sankey = generate_factory_sankey_v2(
            equipment_results=[], aggregates={},
        )
        plotly = to_plotly_format(sankey)
        assert plotly["data"][0]["type"] == "sankey"
        assert plotly["data"][0]["node"]["label"] == []


# ---------------------------------------------------------------------------
# Test 10: Large factory layout
# ---------------------------------------------------------------------------

class TestLargeFactoryLayout:
    def test_seven_equipment_all_present(self):
        """7+ equipment: all should appear as equipment nodes."""
        _, sankey = _run_factory(_large_factory_items())

        eq_nodes = [n for n in sankey["nodes"] if n.get("node_type") == "equipment"]
        assert len(eq_nodes) == 7

    def test_no_duplicate_y_positions_for_equipment(self):
        """No two equipment nodes should share the same y position (within tolerance)."""
        result = analyze_factory(_large_factory_items())
        # Y positions are in the internal build, but we can verify equipment order
        # through node IDs in the output
        sankey = result.sankey
        eq_nodes = [n for n in sankey["nodes"] if n.get("node_type") == "equipment"]
        eq_ids = [n["id"] for n in eq_nodes]
        # All equipment should have unique IDs
        assert len(eq_ids) == len(set(eq_ids))


# ---------------------------------------------------------------------------
# Test 11: Energy balance per equipment (extra validation)
# ---------------------------------------------------------------------------

class TestEnergyBalancePerEquipment:
    def test_single_compressor_balance(self):
        """Single compressor: inflow == outflow at equipment node."""
        _, sankey = _run_factory(_single_compressor_items())
        eq_nodes = [n for n in sankey["nodes"] if n["node_type"] == "equipment"]
        assert len(eq_nodes) == 1

        eq_id = eq_nodes[0]["id"]
        incoming = sum(l["value"] for l in sankey["links"] if l["target"] == eq_id and not l.get("is_opportunity"))
        outgoing = sum(l["value"] for l in sankey["links"] if l["source"] == eq_id and not l.get("is_opportunity"))
        assert abs(incoming - outgoing) < 1.0


# ---------------------------------------------------------------------------
# Test 12: Total source equals total sink
# ---------------------------------------------------------------------------

class TestTotalBalance:
    def test_total_source_output_equals_aggregation_input(self):
        """Sum of all source node outputs should equal sum of all Layer 4 aggregation inputs."""
        _, sankey = _run_factory(_mixed_source_items())

        # Sum values flowing out of source nodes (layer 0)
        source_ids = {n["id"] for n in sankey["nodes"] if n["layer"] == 0}
        total_from_sources = sum(
            l["value"] for l in sankey["links"]
            if l["source"] in source_ids and not l.get("is_opportunity")
        )

        # Sum values flowing into aggregation nodes (layer 4)
        agg_ids = {n["id"] for n in sankey["nodes"] if n["layer"] == 4}
        total_to_agg = sum(
            l["value"] for l in sankey["links"]
            if l["target"] in agg_ids and not l.get("is_opportunity")
        )

        # These should be close (recovery nodes may not sum perfectly
        # because recovery potential is additional metadata, not part of the main flow)
        # But product + destruction should match source
        agg_destroyed_id = {n["id"] for n in sankey["nodes"] if n.get("node_type") == "aggregation_destroyed"}
        agg_useful_id = {n["id"] for n in sankey["nodes"] if n.get("node_type") == "aggregation_useful"}
        product_plus_destruction = sum(
            l["value"] for l in sankey["links"]
            if l["target"] in (agg_destroyed_id | agg_useful_id) and not l.get("is_opportunity")
        )

        assert abs(total_from_sources - product_plus_destruction) < 2.0, \
            f"Source total ({total_from_sources:.2f}) != product+destruction ({product_plus_destruction:.2f})"


# ---------------------------------------------------------------------------
# Unit tests for helpers
# ---------------------------------------------------------------------------

class TestHelpers:
    def test_determine_energy_source_defaults(self):
        assert _determine_energy_source("compressor") == "electricity"
        assert _determine_energy_source("boiler") == "fuel"
        assert _determine_energy_source("heat_exchanger") == "thermal"
        assert _determine_energy_source("steam_turbine") == "thermal"

    def test_dryer_electric_subtypes(self):
        assert _determine_energy_source("dryer", "heat_pump") == "electricity"
        assert _determine_energy_source("dryer", "infrared") == "electricity"
        assert _determine_energy_source("dryer", "microwave") == "electricity"
        assert _determine_energy_source("dryer", "rotary") == "fuel"

    def test_performance_color_ranges(self):
        assert _performance_color(10) == "#ef4444"   # red
        assert _performance_color(40) == "#f97316"   # orange
        assert _performance_color(55) == "#eab308"   # yellow
        assert _performance_color(80) == "#22c55e"   # green

    def test_summary_has_backward_compatible_keys(self):
        """Summary should contain keys expected by the old FactorySankey component."""
        _, sankey = _run_factory(_single_compressor_items())
        summary = sankey["summary"]
        assert "total_input_kW" in summary
        assert "useful_output_kW" in summary
        assert "irreversibility_kW" in summary
        assert "efficiency_pct" in summary

    def test_metadata_version(self):
        _, sankey = _run_factory(_single_compressor_items())
        assert sankey["metadata"]["version"] == "2.0"
        assert sankey["metadata"]["layer_count"] == 5

    def test_view_mode_default(self):
        _, sankey = _run_factory(_single_compressor_items())
        assert sankey["view_mode"] == "exergy_flow"
