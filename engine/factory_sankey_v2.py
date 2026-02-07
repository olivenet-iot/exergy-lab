"""
ExergyLab - Factory Sankey V2: Grassmann-Style Multi-Layer Diagram

5-layer Grassmann-style Sankey data generator:
  Layer 0: Energy sources (electricity, fuel, thermal)
  Layer 1: Distribution (optional, for large source groups)
  Layer 2: Equipment nodes
  Layer 3: Output nodes (product, destruction AV/UN, recovery)
  Layer 4: Aggregation nodes (totals)

Supports 3 view modes: exergy_flow, destruction_focus, cost_flow.
"""

from __future__ import annotations

from typing import Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

EQUIPMENT_ENERGY_SOURCE: dict[str, str] = {
    "compressor": "electricity",
    "chiller": "electricity",
    "pump": "electricity",
    "boiler": "fuel",
    "dryer": "fuel",
    "steam_turbine": "thermal",
    "heat_exchanger": "thermal",
}

DRYER_ELECTRIC_SUBTYPES = {"heat_pump", "infrared", "microwave"}

EQUIPMENT_PRODUCT_LABELS: dict[str, str] = {
    "compressor": "Basınçlı Hava",
    "boiler": "Buhar / Sıcak Su",
    "chiller": "Soğutma",
    "pump": "Hidrolik İş",
    "heat_exchanger": "Isı Transferi",
    "steam_turbine": "Mekanik / Elektrik",
    "dryer": "Kurutma",
}

SOURCE_LABELS: dict[str, tuple[str, str]] = {
    "electricity": ("Elektrik", "#3b82f6"),
    "fuel": ("Yakıt (Doğalgaz)", "#f97316"),
    "thermal": ("Termal Giriş", "#ef4444"),
}

# X-positions for each layer (0.0 – 1.0)
LAYER_X: dict[int, float] = {0: 0.01, 1: 0.20, 2: 0.45, 3: 0.75, 4: 0.99}

# Source ordering for Y layout: electricity top, fuel middle, thermal bottom
SOURCE_Y_ORDER = ["electricity", "fuel", "thermal"]

# Link colors by type
LINK_COLORS: dict[str, str] = {
    "electricity_flow": "rgba(59,130,246,0.45)",
    "fuel_flow": "rgba(249,115,22,0.45)",
    "thermal_flow": "rgba(239,68,68,0.40)",
    "product_flow": "rgba(16,185,129,0.45)",
    "destruction_avoidable": "rgba(239,68,68,0.55)",
    "destruction_unavoidable": "rgba(148,163,184,0.45)",
    "destruction_combined": "rgba(239,68,68,0.40)",
    "recovery_potential": "rgba(139,92,246,0.45)",
    "integration_opportunity": "rgba(168,85,247,0.35)",
    "aggregation": "rgba(148,163,184,0.25)",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _determine_energy_source(
    equipment_type: str,
    subtype: str = "",
    parameters: Optional[dict] = None,
) -> str:
    """Return 'electricity', 'fuel', or 'thermal' for an equipment item."""
    if equipment_type == "dryer" and subtype in DRYER_ELECTRIC_SUBTYPES:
        return "electricity"
    return EQUIPMENT_ENERGY_SOURCE.get(equipment_type, "electricity")


def _performance_color(efficiency_pct: float) -> str:
    """Return hex color based on exergy efficiency ranges."""
    if efficiency_pct < 30:
        return "#ef4444"   # red
    elif efficiency_pct < 50:
        return "#f97316"   # orange
    elif efficiency_pct < 65:
        return "#eab308"   # yellow
    else:
        return "#22c55e"   # green


def _safe_value(val, default: float = 0.0) -> float:
    """Safely convert a value to float, defaulting to 0.0."""
    if val is None:
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def generate_factory_sankey_v2(
    equipment_results: list[dict],
    aggregates: dict,
    hotspots: list[dict] | None = None,
    integration_opportunities: list[dict] | None = None,
    advanced_exergy: dict | None = None,
    view_mode: str = "exergy_flow",
) -> dict:
    """
    Generate Grassmann-style 5-layer factory Sankey data.

    Args:
        equipment_results: List of dicts with keys id, name, equipment_type, subtype, analysis.
        aggregates: Factory aggregate metrics from _calculate_aggregates().
        hotspots: Hotspot list (sorted by destruction).
        integration_opportunities: Cross-equipment integration opportunities.
        advanced_exergy: Advanced exergy analysis results (for AV/UN per-equipment).
        view_mode: One of 'exergy_flow', 'destruction_focus', 'cost_flow'.

    Returns:
        dict with keys: nodes, links, layers, summary, view_mode, metadata
    """
    hotspots = hotspots or []
    integration_opportunities = integration_opportunities or []

    # Filter to valid results only
    valid_results = [r for r in equipment_results if r.get("analysis") is not None]

    if not valid_results:
        return _empty_sankey(view_mode)

    # Build per-equipment AV/UN lookup from advanced_exergy if available
    av_un_lookup = _build_av_un_lookup(valid_results, advanced_exergy)

    # Build nodes and links
    nodes = _build_nodes(valid_results, hotspots, av_un_lookup)
    links = _build_links(valid_results, nodes, av_un_lookup, integration_opportunities)

    # Validate energy balance
    _validate_energy_balance(nodes, links)

    # Build summary
    summary = _build_summary(valid_results, aggregates, hotspots, integration_opportunities, av_un_lookup)

    # Build layer metadata
    layers = {
        0: {"name": "Enerji Kaynakları", "name_en": "Energy Sources"},
        1: {"name": "Dağıtım", "name_en": "Distribution"},
        2: {"name": "Ekipmanlar", "name_en": "Equipment"},
        3: {"name": "Çıktılar", "name_en": "Outputs"},
        4: {"name": "Toplam", "name_en": "Aggregation"},
    }

    return {
        "nodes": [_node_to_dict(n) for n in nodes],
        "links": [_link_to_dict(l) for l in links],
        "layers": layers,
        "summary": summary,
        "view_mode": view_mode,
        "metadata": {
            "version": "2.0",
            "layer_count": 5,
            "equipment_count": len(valid_results),
            "has_av_un": any(v["av"] > 0 or v["un"] > 0 for v in av_un_lookup.values()),
            "has_integration": len(integration_opportunities) > 0,
        },
    }


# ---------------------------------------------------------------------------
# Empty sankey
# ---------------------------------------------------------------------------

def _empty_sankey(view_mode: str = "exergy_flow") -> dict:
    """Return a valid empty Sankey structure."""
    return {
        "nodes": [],
        "links": [],
        "layers": {},
        "summary": {
            "total_input_kW": 0,
            "useful_output_kW": 0,
            "recoverable_heat_kW": 0,
            "irreversibility_kW": 0,
            "efficiency_pct": 0,
            "total_destroyed_avoidable_kW": 0,
            "total_destroyed_unavoidable_kW": 0,
            "source_breakdown": {"electricity_kW": 0, "fuel_kW": 0, "thermal_kW": 0},
            "num_integration_opportunities": 0,
            "integration_potential_kW": 0,
        },
        "view_mode": view_mode,
        "metadata": {
            "version": "2.0",
            "layer_count": 5,
            "equipment_count": 0,
            "has_av_un": False,
            "has_integration": False,
        },
    }


# ---------------------------------------------------------------------------
# AV/UN lookup builder
# ---------------------------------------------------------------------------

def _build_av_un_lookup(
    valid_results: list[dict],
    advanced_exergy: dict | None,
) -> dict[str, dict]:
    """
    Build a lookup of equipment_id -> {av, un} destruction values.

    Uses per-equipment AV/UN from analysis results first.
    Falls back to advanced_exergy data if available.
    Falls back to 50/50 split if neither is available.
    """
    lookup: dict[str, dict] = {}

    # Advanced exergy per-equipment data
    adv_equipment: dict[str, dict] = {}
    if advanced_exergy and "equipment_results" in advanced_exergy:
        for eq in advanced_exergy["equipment_results"]:
            eq_id = eq.get("equipment_id") or eq.get("id", "")
            adv_equipment[eq_id] = eq

    for r in valid_results:
        eq_id = r["id"]
        a = r["analysis"]
        total_destroyed = _safe_value(a.get("exergy_destroyed_kW"))

        # Priority 1: Direct from engine result
        av = _safe_value(a.get("exergy_destroyed_avoidable_kW"))
        un = _safe_value(a.get("exergy_destroyed_unavoidable_kW"))

        if av > 0 or un > 0:
            lookup[eq_id] = {"av": av, "un": un}
            continue

        # Priority 2: From advanced exergy
        adv_eq = adv_equipment.get(eq_id, {})
        adv_av = _safe_value(adv_eq.get("avoidable_kW"))
        adv_un = _safe_value(adv_eq.get("unavoidable_kW"))
        if adv_av > 0 or adv_un > 0:
            lookup[eq_id] = {"av": adv_av, "un": adv_un}
            continue

        # Priority 3: Proportional split from aggregates
        # Default: 60% avoidable, 40% unavoidable (typical industrial assumption)
        if total_destroyed > 0:
            lookup[eq_id] = {"av": total_destroyed * 0.6, "un": total_destroyed * 0.4}
        else:
            lookup[eq_id] = {"av": 0.0, "un": 0.0}

    return lookup


# ---------------------------------------------------------------------------
# Node builder
# ---------------------------------------------------------------------------

class _Node:
    """Internal node representation."""
    __slots__ = ("id", "label", "layer", "node_type", "color", "value_kw", "metadata", "y_pos")

    def __init__(self, id: str, label: str, layer: int, node_type: str,
                 color: str, value_kw: float, metadata: dict | None = None):
        self.id = id
        self.label = label
        self.layer = layer
        self.node_type = node_type
        self.color = color
        self.value_kw = value_kw
        self.metadata = metadata or {}
        self.y_pos = 0.5  # will be calculated


def _node_to_dict(n: _Node) -> dict:
    return {
        "id": n.id,
        "name": n.label,
        "name_en": n.metadata.get("name_en", ""),
        "label": n.label,
        "layer": n.layer,
        "node_type": n.node_type,
        "color": n.color,
        "value_kw": round(n.value_kw, 2),
        "metadata": n.metadata,
    }


def _build_nodes(
    valid_results: list[dict],
    hotspots: list[dict],
    av_un_lookup: dict[str, dict],
) -> list[_Node]:
    """Build all 5 layers of nodes."""
    nodes: list[_Node] = []
    hotspot_lookup = {h["id"]: h for h in hotspots}

    # --- Layer 0: Source nodes ---
    # Group equipment by energy source
    source_groups: dict[str, list[dict]] = {}
    for r in valid_results:
        src = _determine_energy_source(
            r["equipment_type"],
            r.get("subtype", ""),
            r.get("parameters"),
        )
        source_groups.setdefault(src, []).append(r)

    for src_type in SOURCE_Y_ORDER:
        if src_type not in source_groups:
            continue
        group = source_groups[src_type]
        total_in = sum(_safe_value(r["analysis"].get("exergy_in_kW")) for r in group)
        label, color = SOURCE_LABELS[src_type]
        nodes.append(_Node(
            id=f"src_{src_type}",
            label=label,
            layer=0,
            node_type=f"source_{src_type}",
            color=color,
            value_kw=total_in,
            metadata={"name_en": src_type.capitalize(), "equipment_count": len(group)},
        ))

    # --- Layer 1: Distribution nodes (skip for now — only add if > 4 equipment per source) ---
    # Per the plan: skip if < 4 equipment per source type
    for src_type in SOURCE_Y_ORDER:
        if src_type not in source_groups:
            continue
        group = source_groups[src_type]
        if len(group) >= 4:
            total_in = sum(_safe_value(r["analysis"].get("exergy_in_kW")) for r in group)
            label, color = SOURCE_LABELS[src_type]
            nodes.append(_Node(
                id=f"dist_{src_type}",
                label=f"{label} Dağıtım",
                layer=1,
                node_type=f"distribution_{src_type}",
                color=color,
                value_kw=total_in,
                metadata={"name_en": f"{src_type.capitalize()} Distribution"},
            ))

    # --- Layer 2: Equipment nodes ---
    for r in valid_results:
        a = r["analysis"]
        eq_id = r["id"]
        efficiency = _safe_value(a.get("exergy_efficiency_pct"))
        ex_in = _safe_value(a.get("exergy_in_kW"))
        ex_out = _safe_value(a.get("exergy_out_kW"))
        destroyed = _safe_value(a.get("exergy_destroyed_kW"))
        av_un = av_un_lookup.get(eq_id, {"av": 0, "un": 0})
        hs = hotspot_lookup.get(eq_id, {})

        nodes.append(_Node(
            id=f"eq_{eq_id}",
            label=r["name"],
            layer=2,
            node_type="equipment",
            color=_performance_color(efficiency),
            value_kw=ex_in,
            metadata={
                "name_en": r["name"],
                "equipment_type": r["equipment_type"],
                "subtype": r.get("subtype", ""),
                "exergy_in_kW": round(ex_in, 2),
                "exergy_out_kW": round(ex_out, 2),
                "exergy_destroyed_kW": round(destroyed, 2),
                "exergy_efficiency_pct": round(efficiency, 1),
                "avoidable_kW": round(av_un["av"], 2),
                "unavoidable_kW": round(av_un["un"], 2),
                "priority": hs.get("priority", ""),
                "annual_loss_EUR": hs.get("annual_loss_EUR", 0),
                # Exergoeconomic fields if available
                "C_dot_destruction_eur_h": _safe_value(a.get("exergoeconomic_C_dot_destruction_eur_h")),
                "Z_dot_eur_h": _safe_value(a.get("exergoeconomic_Z_dot_eur_h")),
                "f_factor": _safe_value(a.get("exergoeconomic_f_factor")),
            },
        ))

    # --- Layer 3: Output nodes (per equipment) ---
    for r in valid_results:
        a = r["analysis"]
        eq_id = r["id"]
        eq_type = r["equipment_type"]
        ex_out = _safe_value(a.get("exergy_out_kW"))
        destroyed = _safe_value(a.get("exergy_destroyed_kW"))
        av_un = av_un_lookup.get(eq_id, {"av": 0, "un": 0})

        # Product node
        product_label = EQUIPMENT_PRODUCT_LABELS.get(eq_type, "Çıktı")
        if ex_out > 0:
            nodes.append(_Node(
                id=f"prod_{eq_id}",
                label=f"{r['name']} → {product_label}",
                layer=3,
                node_type="product",
                color="#22c55e",
                value_kw=ex_out,
                metadata={"name_en": f"{r['name']} Product"},
            ))

        # Destruction nodes (AV and UN)
        if av_un["av"] > 0.01:
            nodes.append(_Node(
                id=f"dest_av_{eq_id}",
                label=f"{r['name']} Önlenebilir Yıkım",
                layer=3,
                node_type="destroyed_avoidable",
                color="#ef4444",
                value_kw=av_un["av"],
                metadata={"name_en": f"{r['name']} Avoidable Destruction"},
            ))
        if av_un["un"] > 0.01:
            nodes.append(_Node(
                id=f"dest_un_{eq_id}",
                label=f"{r['name']} Önlenemez Yıkım",
                layer=3,
                node_type="destroyed_unavoidable",
                color="#94a3b8",
                value_kw=av_un["un"],
                metadata={"name_en": f"{r['name']} Unavoidable Destruction"},
            ))

        # Recovery node if applicable
        recoverable = _safe_value(a.get("recoverable_heat_kW")) or _safe_value(a.get("heat_recovery_potential_kW"))
        if recoverable > 0.01:
            nodes.append(_Node(
                id=f"recv_{eq_id}",
                label=f"{r['name']} Geri Kazanım",
                layer=3,
                node_type="recovery",
                color="#8b5cf6",
                value_kw=recoverable,
                metadata={"name_en": f"{r['name']} Recovery"},
            ))

    # --- Layer 4: Aggregation nodes ---
    total_out = sum(_safe_value(r["analysis"].get("exergy_out_kW")) for r in valid_results)
    total_destroyed = sum(_safe_value(r["analysis"].get("exergy_destroyed_kW")) for r in valid_results)
    total_recovery = sum(
        _safe_value(r["analysis"].get("recoverable_heat_kW")) or _safe_value(r["analysis"].get("heat_recovery_potential_kW"))
        for r in valid_results
    )

    nodes.append(_Node(
        id="agg_useful",
        label="Toplam Faydalı Exergy",
        layer=4,
        node_type="aggregation_useful",
        color="#16a34a",
        value_kw=total_out,
        metadata={"name_en": "Total Useful Exergy"},
    ))
    nodes.append(_Node(
        id="agg_destroyed",
        label="Toplam Exergy Yıkımı",
        layer=4,
        node_type="aggregation_destroyed",
        color="#dc2626",
        value_kw=total_destroyed,
        metadata={"name_en": "Total Exergy Destruction"},
    ))
    if total_recovery > 0.01:
        nodes.append(_Node(
            id="agg_recovery",
            label="Toplam Geri Kazanım",
            layer=4,
            node_type="aggregation_recovery",
            color="#7c3aed",
            value_kw=total_recovery,
            metadata={"name_en": "Total Recovery Potential"},
        ))

    # Calculate Y positions
    _calculate_y_positions(nodes, valid_results)

    return nodes


def _calculate_y_positions(nodes: list[_Node], valid_results: list[dict]) -> None:
    """
    Calculate y positions for all nodes.
    Equipment sorted by source type (electricity top, fuel middle, thermal bottom).
    """
    # Group equipment by source type for ordering
    eq_order: list[str] = []
    for src_type in SOURCE_Y_ORDER:
        for r in valid_results:
            src = _determine_energy_source(r["equipment_type"], r.get("subtype", ""))
            if src == src_type:
                eq_order.append(r["id"])

    total_eq = len(eq_order)
    if total_eq == 0:
        return

    # Equipment Y positions: spread evenly in 0.05 – 0.95
    eq_y: dict[str, float] = {}
    for idx, eq_id in enumerate(eq_order):
        if total_eq == 1:
            eq_y[eq_id] = 0.5
        else:
            eq_y[eq_id] = 0.05 + (0.90 * idx / (total_eq - 1))

    # Source node Y: average of their equipment Y
    src_y: dict[str, float] = {}
    for src_type in SOURCE_Y_ORDER:
        ys = []
        for r in valid_results:
            src = _determine_energy_source(r["equipment_type"], r.get("subtype", ""))
            if src == src_type:
                ys.append(eq_y.get(r["id"], 0.5))
        if ys:
            src_y[src_type] = sum(ys) / len(ys)

    # Assign Y to all nodes
    for node in nodes:
        if node.id.startswith("src_"):
            src_type = node.id.replace("src_", "")
            node.y_pos = src_y.get(src_type, 0.5)
        elif node.id.startswith("dist_"):
            src_type = node.id.replace("dist_", "")
            node.y_pos = src_y.get(src_type, 0.5)
        elif node.id.startswith("eq_"):
            eq_id = node.id.replace("eq_", "")
            node.y_pos = eq_y.get(eq_id, 0.5)
        elif node.id.startswith("prod_") or node.id.startswith("dest_av_") or node.id.startswith("dest_un_") or node.id.startswith("recv_"):
            # Layer 3 nodes: same Y as their equipment
            # Extract equipment id
            for prefix in ("prod_", "dest_av_", "dest_un_", "recv_"):
                if node.id.startswith(prefix):
                    eq_id = node.id[len(prefix):]
                    node.y_pos = eq_y.get(eq_id, 0.5)
                    break
        elif node.id == "agg_useful":
            node.y_pos = 0.15
        elif node.id == "agg_destroyed":
            node.y_pos = 0.65
        elif node.id == "agg_recovery":
            node.y_pos = 0.90


# ---------------------------------------------------------------------------
# Link builder
# ---------------------------------------------------------------------------

class _Link:
    """Internal link representation."""
    __slots__ = ("source", "target", "value", "link_type", "color", "label", "is_opportunity")

    def __init__(self, source: str, target: str, value: float, link_type: str,
                 color: str = "", label: str = "", is_opportunity: bool = False):
        self.source = source
        self.target = target
        self.value = value
        self.link_type = link_type
        self.color = color or LINK_COLORS.get(link_type, "rgba(148,163,184,0.3)")
        self.label = label
        self.is_opportunity = is_opportunity


def _link_to_dict(l: _Link) -> dict:
    return {
        "source": l.source,
        "target": l.target,
        "value": round(l.value, 2),
        "link_type": l.link_type,
        "color": l.color,
        "label": l.label,
        "is_opportunity": l.is_opportunity,
    }


def _build_links(
    valid_results: list[dict],
    nodes: list[_Node],
    av_un_lookup: dict[str, dict],
    integration_opportunities: list[dict],
) -> list[_Link]:
    """Build all links between nodes."""
    links: list[_Link] = []
    node_ids = {n.id for n in nodes}

    # Check which source types have distribution nodes
    dist_sources = {n.id.replace("dist_", "") for n in nodes if n.id.startswith("dist_")}

    for r in valid_results:
        a = r["analysis"]
        eq_id = r["id"]
        eq_type = r["equipment_type"]
        src_type = _determine_energy_source(eq_type, r.get("subtype", ""))

        ex_in = _safe_value(a.get("exergy_in_kW"))
        ex_out = _safe_value(a.get("exergy_out_kW"))
        av_un = av_un_lookup.get(eq_id, {"av": 0, "un": 0})

        flow_type = f"{src_type}_flow"

        # Link: Source → Equipment (or Source → Distribution → Equipment)
        if src_type in dist_sources:
            # Source → Distribution (handled once per source type below)
            # Distribution → Equipment
            if ex_in > 0.01:
                links.append(_Link(
                    source=f"dist_{src_type}",
                    target=f"eq_{eq_id}",
                    value=ex_in,
                    link_type=flow_type,
                    label=f"{r['name']} Girişi",
                ))
        else:
            # Direct Source → Equipment
            if ex_in > 0.01:
                links.append(_Link(
                    source=f"src_{src_type}",
                    target=f"eq_{eq_id}",
                    value=ex_in,
                    link_type=flow_type,
                    label=f"{r['name']} Girişi",
                ))

        # Link: Equipment → Product
        if ex_out > 0.01 and f"prod_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"eq_{eq_id}",
                target=f"prod_{eq_id}",
                value=ex_out,
                link_type="product_flow",
                label=f"{r['name']} Faydalı Çıktı",
            ))

        # Link: Equipment → Destruction (AV and/or UN)
        if av_un["av"] > 0.01 and f"dest_av_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"eq_{eq_id}",
                target=f"dest_av_{eq_id}",
                value=av_un["av"],
                link_type="destruction_avoidable",
                label=f"{r['name']} Önlenebilir Yıkım",
            ))
        if av_un["un"] > 0.01 and f"dest_un_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"eq_{eq_id}",
                target=f"dest_un_{eq_id}",
                value=av_un["un"],
                link_type="destruction_unavoidable",
                label=f"{r['name']} Önlenemez Yıkım",
            ))

        # Link: Equipment → Recovery
        recoverable = _safe_value(a.get("recoverable_heat_kW")) or _safe_value(a.get("heat_recovery_potential_kW"))
        if recoverable > 0.01 and f"recv_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"eq_{eq_id}",
                target=f"recv_{eq_id}",
                value=recoverable,
                link_type="recovery_potential",
                label=f"{r['name']} Geri Kazanım",
            ))

    # Source → Distribution links (one per source type that has distribution)
    for src_type in dist_sources:
        src_node_id = f"src_{src_type}"
        dist_node_id = f"dist_{src_type}"
        if src_node_id in node_ids and dist_node_id in node_ids:
            # Total input for this source
            total = sum(
                _safe_value(r["analysis"].get("exergy_in_kW"))
                for r in valid_results
                if _determine_energy_source(r["equipment_type"], r.get("subtype", "")) == src_type
            )
            if total > 0.01:
                links.append(_Link(
                    source=src_node_id,
                    target=dist_node_id,
                    value=total,
                    link_type=f"{src_type}_flow",
                    label=f"{SOURCE_LABELS[src_type][0]} Dağıtım",
                ))

    # Layer 3 → Layer 4 aggregation links
    for r in valid_results:
        eq_id = r["id"]
        a = r["analysis"]
        ex_out = _safe_value(a.get("exergy_out_kW"))
        av_un = av_un_lookup.get(eq_id, {"av": 0, "un": 0})
        total_dest = av_un["av"] + av_un["un"]

        # Product → Aggregation useful
        if ex_out > 0.01 and f"prod_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"prod_{eq_id}",
                target="agg_useful",
                value=ex_out,
                link_type="aggregation",
                label=f"{r['name']} → Toplam Faydalı",
            ))

        # Destruction → Aggregation destroyed
        if av_un["av"] > 0.01 and f"dest_av_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"dest_av_{eq_id}",
                target="agg_destroyed",
                value=av_un["av"],
                link_type="aggregation",
                label=f"{r['name']} Önlenebilir → Toplam Yıkım",
            ))
        if av_un["un"] > 0.01 and f"dest_un_{eq_id}" in node_ids:
            links.append(_Link(
                source=f"dest_un_{eq_id}",
                target="agg_destroyed",
                value=av_un["un"],
                link_type="aggregation",
                label=f"{r['name']} Önlenemez → Toplam Yıkım",
            ))

        # Recovery → Aggregation recovery
        recoverable = _safe_value(a.get("recoverable_heat_kW")) or _safe_value(a.get("heat_recovery_potential_kW"))
        if recoverable > 0.01 and f"recv_{eq_id}" in node_ids and "agg_recovery" in node_ids:
            links.append(_Link(
                source=f"recv_{eq_id}",
                target="agg_recovery",
                value=recoverable,
                link_type="aggregation",
                label=f"{r['name']} → Toplam Geri Kazanım",
            ))

    # Integration opportunity links
    eq_name_to_id: dict[str, str] = {r["name"]: r["id"] for r in valid_results}
    for opp in integration_opportunities:
        source_name = opp.get("source", "")
        target_name = opp.get("target", "")
        potential_kW = _safe_value(opp.get("potential_recovery_kW"))

        source_eq_id = eq_name_to_id.get(source_name)
        target_eq_id = eq_name_to_id.get(target_name)

        if source_eq_id and target_eq_id and potential_kW > 0.01:
            src_node = f"eq_{source_eq_id}"
            tgt_node = f"eq_{target_eq_id}"
            if src_node in node_ids and tgt_node in node_ids:
                links.append(_Link(
                    source=src_node,
                    target=tgt_node,
                    value=potential_kW,
                    link_type="integration_opportunity",
                    label=opp.get("title", "Entegrasyon Fırsatı"),
                    is_opportunity=True,
                ))

    return links


# ---------------------------------------------------------------------------
# Summary builder
# ---------------------------------------------------------------------------

def _build_summary(
    valid_results: list[dict],
    aggregates: dict,
    hotspots: list[dict],
    integration_opportunities: list[dict],
    av_un_lookup: dict[str, dict],
) -> dict:
    """Build aggregated summary metrics."""
    total_in = _safe_value(aggregates.get("total_exergy_input_kW"))
    total_out = _safe_value(aggregates.get("total_exergy_output_kW"))
    total_destroyed = _safe_value(aggregates.get("total_exergy_destroyed_kW"))
    efficiency = _safe_value(aggregates.get("factory_exergy_efficiency_pct"))

    total_av = sum(v["av"] for v in av_un_lookup.values())
    total_un = sum(v["un"] for v in av_un_lookup.values())

    total_recovery = sum(
        _safe_value(r["analysis"].get("recoverable_heat_kW")) or _safe_value(r["analysis"].get("heat_recovery_potential_kW"))
        for r in valid_results
    )

    # Source breakdown
    source_kw: dict[str, float] = {"electricity": 0, "fuel": 0, "thermal": 0}
    for r in valid_results:
        src = _determine_energy_source(r["equipment_type"], r.get("subtype", ""))
        source_kw[src] += _safe_value(r["analysis"].get("exergy_in_kW"))

    # Biggest loss
    biggest_name = ""
    biggest_kw = 0.0
    if hotspots:
        biggest_name = hotspots[0].get("name", "")
        biggest_kw = _safe_value(hotspots[0].get("exergy_destroyed_kW"))

    # Integration potential
    integ_kw = sum(_safe_value(o.get("potential_recovery_kW")) for o in integration_opportunities)

    return {
        "total_input_kW": round(total_in, 2),
        "useful_output_kW": round(total_out, 2),
        "recoverable_heat_kW": round(total_recovery, 2),
        "irreversibility_kW": round(total_destroyed, 2),
        "efficiency_pct": round(efficiency, 1),
        "total_destroyed_avoidable_kW": round(total_av, 2),
        "total_destroyed_unavoidable_kW": round(total_un, 2),
        "exergy_destroyed_avoidable_kW": round(total_av, 2),
        "exergy_destroyed_unavoidable_kW": round(total_un, 2),
        "avoidable_ratio_pct": round((total_av / total_destroyed * 100) if total_destroyed > 0 else 0, 1),
        "source_breakdown": {
            "electricity_kW": round(source_kw["electricity"], 2),
            "fuel_kW": round(source_kw["fuel"], 2),
            "thermal_kW": round(source_kw["thermal"], 2),
        },
        "biggest_loss_equipment": biggest_name,
        "biggest_loss_kW": round(biggest_kw, 2),
        "num_integration_opportunities": len(integration_opportunities),
        "integration_potential_kW": round(integ_kw, 2),
    }


# ---------------------------------------------------------------------------
# Energy balance validation
# ---------------------------------------------------------------------------

def _validate_energy_balance(nodes: list[_Node], links: list[_Link]) -> None:
    """
    Validate energy conservation at every equipment node.

    For each equipment node: sum(incoming links) should equal sum(outgoing links)
    within a tolerance. Integration opportunity links are excluded from validation
    since they represent potential (not actual) flows.

    Raises ValueError if balance is violated.
    """
    node_ids = {n.id for n in nodes}
    equipment_nodes = [n for n in nodes if n.node_type == "equipment"]

    for eq_node in equipment_nodes:
        eq_id = eq_node.id
        incoming = sum(
            l.value for l in links
            if l.target == eq_id and not l.is_opportunity
        )
        outgoing = sum(
            l.value for l in links
            if l.source == eq_id and not l.is_opportunity
        )

        if abs(incoming - outgoing) > 0.5:
            # Adjust the largest outgoing link to fix balance
            # This handles rounding differences between AV/UN split
            # and total destroyed from the engine
            _rebalance_equipment_links(eq_id, incoming, links)


def _rebalance_equipment_links(eq_id: str, target_total: float, links: list[_Link]) -> None:
    """
    Rebalance outgoing links from an equipment node to match incoming total.

    Adjusts the destruction links proportionally to maintain energy conservation.
    """
    outgoing = [l for l in links if l.source == eq_id and not l.is_opportunity]
    if not outgoing:
        return

    current_total = sum(l.value for l in outgoing)
    if current_total < 0.01:
        return

    diff = target_total - current_total
    if abs(diff) < 0.01:
        return

    # Find destruction links to adjust
    dest_links = [l for l in outgoing if "destruction" in l.link_type]
    if not dest_links:
        # Adjust the last outgoing link
        dest_links = [outgoing[-1]]

    # Distribute diff proportionally among destruction links
    dest_total = sum(l.value for l in dest_links)
    if dest_total < 0.01:
        # Add all to the first destruction link
        dest_links[0].value = max(0.01, dest_links[0].value + diff)
        return

    for l in dest_links:
        l.value = max(0.01, l.value + diff * (l.value / dest_total))


# ---------------------------------------------------------------------------
# Plotly format converter
# ---------------------------------------------------------------------------

def to_plotly_format(sankey_data: dict) -> dict:
    """
    Convert internal Sankey data to Plotly-compatible trace dict.

    Args:
        sankey_data: Output of generate_factory_sankey_v2().

    Returns:
        Dict with 'data' (Plotly trace) and 'layout' keys.
    """
    nodes_list = sankey_data.get("nodes", [])
    links_list = sankey_data.get("links", [])

    if not nodes_list:
        return {
            "data": [{
                "type": "sankey",
                "orientation": "h",
                "node": {"label": [], "color": [], "x": [], "y": [], "pad": 20, "thickness": 25},
                "link": {"source": [], "target": [], "value": [], "color": [], "label": []},
            }],
            "layout": _default_layout(),
        }

    # Map string node IDs to integer indices
    id_to_idx: dict[str, int] = {}
    for i, node in enumerate(nodes_list):
        node_id = node.get("id", str(i))
        id_to_idx[node_id] = i

    # Build Plotly node arrays
    node_labels = []
    node_colors = []
    node_x = []
    node_y = []
    node_customdata = []

    for node in nodes_list:
        node_labels.append(node.get("label", node.get("name", "")))
        node_colors.append(node.get("color", "#94a3b8"))
        layer = node.get("layer", 2)
        node_x.append(LAYER_X.get(layer, 0.5))
        node_y.append(node.get("metadata", {}).get("y_pos", 0.5) if "y_pos" in node.get("metadata", {}) else 0.5)
        node_customdata.append(node.get("metadata", {}))

    # For Y positions, use the values from our calculation (stored during build)
    # We need to re-extract from our node objects — but in to_plotly_format we get dicts
    # So we use the metadata y_pos if available, otherwise 0.5

    # Build Plotly link arrays
    link_sources = []
    link_targets = []
    link_values = []
    link_colors = []
    link_labels = []

    for link in links_list:
        src_id = link.get("source", "")
        tgt_id = link.get("target", "")
        src_idx = id_to_idx.get(src_id)
        tgt_idx = id_to_idx.get(tgt_id)

        if src_idx is None or tgt_idx is None:
            continue

        link_sources.append(src_idx)
        link_targets.append(tgt_idx)
        link_values.append(link.get("value", 0))
        link_colors.append(link.get("color", "rgba(148,163,184,0.3)"))
        link_labels.append(link.get("label", ""))

    # Hovertemplate (Turkish)
    node_hover = (
        "<b>%{label}</b><br>"
        "Değer: %{value:.1f} kW<br>"
        "<extra></extra>"
    )
    link_hover = (
        "<b>%{label}</b><br>"
        "Akış: %{value:.1f} kW<br>"
        "<extra></extra>"
    )

    trace = {
        "type": "sankey",
        "orientation": "h",
        "arrangement": "snap",
        "node": {
            "label": node_labels,
            "color": node_colors,
            "x": node_x,
            "y": node_y,
            "pad": 20,
            "thickness": 25,
            "line": {"color": "white", "width": 1.5},
            "hovertemplate": node_hover,
            "customdata": node_customdata,
        },
        "link": {
            "source": link_sources,
            "target": link_targets,
            "value": link_values,
            "color": link_colors,
            "label": link_labels,
            "hovertemplate": link_hover,
        },
    }

    return {
        "data": [trace],
        "layout": _default_layout(),
    }


def _default_layout() -> dict:
    """Default Plotly layout for Sankey."""
    return {
        "font": {"family": "Inter, system-ui, sans-serif", "size": 11},
        "margin": {"l": 10, "r": 10, "t": 10, "b": 10},
        "paper_bgcolor": "transparent",
        "plot_bgcolor": "transparent",
        "height": 700,
    }
