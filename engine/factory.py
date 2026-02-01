"""
ExergyLab - Factory-Level Exergy Analysis

Fabrika seviyesi exergy analizi.
Birden fazla ekipmani toplu analiz eder, hotspot belirler,
capraz ekipman entegrasyon firsatlarini tespit eder ve
fabrika Sankey diyagrami olusturur.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from .core import DeadState
from .compressor import (
    CompressorInput, PistonCompressorInput,
    ScrollCompressorInput, CentrifugalCompressorInput,
    analyze_compressor, analyze_piston_compressor,
    analyze_scroll_compressor, analyze_centrifugal_compressor,
)
from .boiler import BoilerInput, analyze_boiler
from .chiller import ChillerInput, analyze_chiller
from .pump import PumpInput, analyze_pump


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

class EquipmentType(str, Enum):
    COMPRESSOR = "compressor"
    BOILER = "boiler"
    CHILLER = "chiller"
    PUMP = "pump"


@dataclass
class EquipmentItem:
    """Fabrika icindeki tek bir ekipman."""
    id: str
    name: str
    equipment_type: str   # "compressor", "boiler", "chiller", "pump"
    subtype: str          # e.g. "screw", "steam_firetube", "centrifugal"
    parameters: dict
    analysis_result: Optional[dict] = None


@dataclass
class FactoryAnalysisResult:
    """Fabrika analiz sonuclari."""
    equipment_results: List[dict]
    aggregates: dict
    hotspots: List[dict]
    integration_opportunities: List[dict]
    sankey: dict


# ---------------------------------------------------------------------------
# Compressor subtypes and their analyzers
# ---------------------------------------------------------------------------

_COMPRESSOR_ANALYZERS = {
    "screw": (CompressorInput, analyze_compressor),
    "piston": (PistonCompressorInput, analyze_piston_compressor),
    "scroll": (ScrollCompressorInput, analyze_scroll_compressor),
    "centrifugal": (CentrifugalCompressorInput, analyze_centrifugal_compressor),
}

# Valid subtypes per equipment type
_BOILER_SUBTYPES = {
    "steam_firetube", "steam_watertube", "hotwater", "condensing",
    "waste_heat", "electric", "biomass",
}

_VC_CHILLER_SUBTYPES = {"screw", "centrifugal", "scroll", "reciprocating", "air_cooled", "water_cooled"}
_ABS_CHILLER_SUBTYPES = {"absorption"}

_PUMP_SUBTYPES = {
    "centrifugal", "positive_displacement", "submersible",
    "vertical_turbine", "booster", "vacuum",
}


# ---------------------------------------------------------------------------
# Equipment analysis dispatcher
# ---------------------------------------------------------------------------

def analyze_equipment_item(item: EquipmentItem) -> dict:
    """
    Tek bir ekipmani analiz eder.
    Ekipman tipine gore uygun engine fonksiyonuna dispatch yapar.
    Parametre dict'inden uygun Input dataclass'i olusturur.

    Returns:
        dict with keys: exergy_in_kW, exergy_out_kW, exergy_destroyed_kW,
                        exergy_efficiency_pct, annual_loss_kWh, annual_loss_EUR
                        and equipment-specific fields
    """
    eq_type = item.equipment_type
    subtype = item.subtype
    params = dict(item.parameters)  # copy

    if eq_type == "compressor":
        return _analyze_compressor_item(subtype, params)
    elif eq_type == "boiler":
        return _analyze_boiler_item(subtype, params)
    elif eq_type == "chiller":
        return _analyze_chiller_item(subtype, params)
    elif eq_type == "pump":
        return _analyze_pump_item(subtype, params)
    else:
        raise ValueError(f"Unknown equipment type: {eq_type}")


def _analyze_compressor_item(subtype: str, params: dict) -> dict:
    """Dispatch compressor analysis."""
    entry = _COMPRESSOR_ANALYZERS.get(subtype)
    if not entry:
        # Fall back to generic screw
        entry = _COMPRESSOR_ANALYZERS["screw"]

    input_cls, analyze_fn = entry

    # Filter params to only accepted fields
    engine_kwargs = _filter_params(params, input_cls)
    engine_kwargs["compressor_type"] = subtype

    input_data = input_cls(**engine_kwargs)
    result = analyze_fn(input_data)
    return result.to_dict()


def _analyze_boiler_item(subtype: str, params: dict) -> dict:
    """Dispatch boiler analysis."""
    engine_kwargs = _filter_params(params, BoilerInput)
    engine_kwargs["boiler_type"] = subtype

    input_data = BoilerInput(**engine_kwargs)
    result = analyze_boiler(input_data)
    return result.to_dict()


def _analyze_chiller_item(subtype: str, params: dict) -> dict:
    """Dispatch chiller analysis."""
    engine_kwargs = _filter_params(params, ChillerInput)
    engine_kwargs["chiller_type"] = subtype

    input_data = ChillerInput(**engine_kwargs)
    result = analyze_chiller(input_data)
    return result.to_dict()


def _analyze_pump_item(subtype: str, params: dict) -> dict:
    """Dispatch pump analysis."""
    engine_kwargs = _filter_params(params, PumpInput)
    engine_kwargs["pump_type"] = subtype

    input_data = PumpInput(**engine_kwargs)
    result = analyze_pump(input_data)
    return result.to_dict()


def _filter_params(params: dict, dataclass_cls) -> dict:
    """Filter a parameter dict to only include fields accepted by a dataclass."""
    import dataclasses
    valid_fields = {f.name for f in dataclasses.fields(dataclass_cls)}
    return {k: v for k, v in params.items() if k in valid_fields and v is not None}


# ---------------------------------------------------------------------------
# Factory analysis orchestrator
# ---------------------------------------------------------------------------

def analyze_factory(equipment_list: List[EquipmentItem]) -> FactoryAnalysisResult:
    """
    Fabrika seviyesi analiz orkestratoru.

    1. Her ekipmani analiz et
    2. Toplu metrikleri hesapla
    3. Hotspot'lari belirle (exergy yikimi buyukten kucuge)
    4. Capraz ekipman entegrasyon firsatlarini tespit et
    5. Fabrika Sankey diyagrami olustur

    Args:
        equipment_list: EquipmentItem listesi

    Returns:
        FactoryAnalysisResult
    """
    # 1. Analyze each equipment
    equipment_results = []
    for item in equipment_list:
        try:
            result = analyze_equipment_item(item)
            entry = {
                "id": item.id,
                "name": item.name,
                "equipment_type": item.equipment_type,
                "subtype": item.subtype,
                "analysis": result,
            }
            equipment_results.append(entry)
        except Exception as e:
            equipment_results.append({
                "id": item.id,
                "name": item.name,
                "equipment_type": item.equipment_type,
                "subtype": item.subtype,
                "analysis": None,
                "error": str(e),
            })

    # Filter to only successfully analyzed equipment
    valid_results = [r for r in equipment_results if r.get("analysis") is not None]

    # 2. Calculate aggregates
    aggregates = _calculate_aggregates(valid_results)

    # 3. Identify hotspots
    hotspots = _identify_hotspots(valid_results)

    # 4. Detect integration opportunities
    integration = _detect_integration_opportunities(valid_results)

    # 5. Generate factory Sankey
    sankey = _generate_factory_sankey(valid_results, aggregates)

    return FactoryAnalysisResult(
        equipment_results=equipment_results,
        aggregates=aggregates,
        hotspots=hotspots,
        integration_opportunities=integration,
        sankey=sankey,
    )


# ---------------------------------------------------------------------------
# Aggregates
# ---------------------------------------------------------------------------

def _calculate_aggregates(results: List[dict]) -> dict:
    """Toplam exergy metriklerini hesaplar."""
    total_in = 0.0
    total_out = 0.0
    total_destroyed = 0.0
    total_annual_loss_kwh = 0.0
    total_annual_loss_eur = 0.0

    for r in results:
        a = r["analysis"]
        total_in += a.get("exergy_in_kW", 0)
        total_out += a.get("exergy_out_kW", 0)
        total_destroyed += a.get("exergy_destroyed_kW", 0)
        total_annual_loss_kwh += a.get("annual_loss_kWh", 0) or 0
        total_annual_loss_eur += a.get("annual_loss_EUR", 0) or 0

    factory_efficiency = (total_out / total_in * 100) if total_in > 0 else 0.0

    return {
        "total_exergy_input_kW": round(total_in, 2),
        "total_exergy_output_kW": round(total_out, 2),
        "total_exergy_destroyed_kW": round(total_destroyed, 2),
        "factory_exergy_efficiency_pct": round(factory_efficiency, 1),
        "total_annual_loss_kWh": round(total_annual_loss_kwh, 0),
        "total_annual_loss_EUR": round(total_annual_loss_eur, 0),
        "equipment_count": len(results),
    }


# ---------------------------------------------------------------------------
# Hotspots
# ---------------------------------------------------------------------------

def _identify_hotspots(results: List[dict]) -> List[dict]:
    """Ekipmanlari exergy yikimina gore siralar (azalan)."""
    hotspots = []
    for r in results:
        a = r["analysis"]
        destroyed = a.get("exergy_destroyed_kW", 0)
        annual_loss = a.get("annual_loss_EUR", 0) or 0

        # Priority determination
        if destroyed > 20 or annual_loss > 5000:
            priority = "high"
        elif destroyed > 5 or annual_loss > 1000:
            priority = "medium"
        else:
            priority = "low"

        hotspots.append({
            "id": r["id"],
            "name": r["name"],
            "equipment_type": r["equipment_type"],
            "subtype": r["subtype"],
            "exergy_destroyed_kW": round(destroyed, 2),
            "exergy_efficiency_pct": round(a.get("exergy_efficiency_pct", 0), 1),
            "annual_loss_EUR": round(annual_loss, 0),
            "priority": priority,
        })

    # Sort by exergy destruction descending
    hotspots.sort(key=lambda x: x["exergy_destroyed_kW"], reverse=True)
    return hotspots


# ---------------------------------------------------------------------------
# Integration opportunities
# ---------------------------------------------------------------------------

def _detect_integration_opportunities(results: List[dict]) -> List[dict]:
    """
    Capraz ekipman entegrasyon firsatlarini tespit eder.

    5 desen kontrol edilir:
    1. Kompresor atik isisi -> Kazan besleme suyu on isitma
    2. Kompresor atik isisi -> Mekan isitma
    3. Kazan baca gazi -> Absorpsiyonlu chiller
    4. Chiller kondenser isisi -> Sicak su
    5. Pompa VSD retrofit (kisma -> VSD)
    """
    opportunities = []

    # Categorize equipment
    compressors = [r for r in results if r["equipment_type"] == "compressor"]
    boilers = [r for r in results if r["equipment_type"] == "boiler"]
    chillers = [r for r in results if r["equipment_type"] == "chiller"]
    pumps = [r for r in results if r["equipment_type"] == "pump"]

    # Pattern 1: Compressor waste heat -> Boiler feedwater preheating
    if compressors and boilers:
        for comp in compressors:
            ca = comp["analysis"]
            recoverable = ca.get("recoverable_heat_kW", 0) or 0
            if recoverable > 0:
                for boiler in boilers:
                    savings = recoverable * 0.6 * 6000 * 0.05  # 60% recovery, 6000h, ~0.05 EUR/kWh fuel
                    opportunities.append({
                        "type": "compressor_heat_to_boiler",
                        "title": "Kompresor Atik Isisi → Kazan Besleme Suyu",
                        "source": comp["name"],
                        "target": boiler["name"],
                        "potential_recovery_kW": round(recoverable * 0.6, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": 15000,
                        "roi_years": round(15000 / savings, 1) if savings > 0 else 99,
                        "complexity": "medium",
                        "description": f"{comp['name']} atik isisinin {boiler['name']} besleme suyu on isitmada kullanimi. "
                                       f"Tahmini geri kazanilabilir isi: {recoverable * 0.6:.1f} kW.",
                    })
                    break  # One opportunity per compressor

    # Pattern 2: Compressor waste heat -> Space heating
    for comp in compressors:
        ca = comp["analysis"]
        recoverable = ca.get("recoverable_heat_kW", 0) or 0
        if recoverable > 3:  # At least 3 kW
            savings = recoverable * 0.5 * 2000 * 0.06  # 50% useful, 2000h heating season, gas price
            opportunities.append({
                "type": "compressor_heat_to_space",
                "title": "Kompresor Atik Isisi → Mekan Isitma",
                "source": comp["name"],
                "target": "Mekan Isitma Sistemi",
                "potential_recovery_kW": round(recoverable * 0.5, 1),
                "estimated_savings_EUR_year": round(savings, 0),
                "estimated_investment_EUR": 8000,
                "roi_years": round(8000 / savings, 1) if savings > 0 else 99,
                "complexity": "low",
                "description": f"{comp['name']} atik isisinin mekan isitmada kullanimi (kis sezonu).",
            })

    # Pattern 3: Boiler flue gas -> Absorption chiller
    if boilers and chillers:
        for boiler in boilers:
            ba = boiler["analysis"]
            flue_gas_loss = ba.get("flue_gas_loss_kW", 0) or 0
            if flue_gas_loss > 10:
                for chiller in chillers:
                    # Absorption COP ~0.7
                    cooling_potential = flue_gas_loss * 0.5 * 0.7
                    electricity_savings = cooling_potential / 4.0  # Replace electric chiller COP=4
                    savings = electricity_savings * 4000 * 0.12  # 4000h, 0.12 EUR/kWh
                    opportunities.append({
                        "type": "flue_gas_to_absorption",
                        "title": "Kazan Baca Gazi → Absorpsiyonlu Chiller",
                        "source": boiler["name"],
                        "target": chiller["name"],
                        "potential_recovery_kW": round(cooling_potential, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": 50000,
                        "roi_years": round(50000 / savings, 1) if savings > 0 else 99,
                        "complexity": "high",
                        "description": f"{boiler['name']} baca gazi isisi ile {chiller['name']} yerine absorpsiyonlu sogutma.",
                    })
                    break

    # Pattern 4: Chiller condenser heat -> Hot water
    for chiller in chillers:
        ca = chiller["analysis"]
        exergy_in = ca.get("exergy_in_kW", 0)
        # Condenser rejects Q_cool + W_comp as heat
        if exergy_in > 10:
            # Rough estimate: condenser heat ~ 1.2 * input for VC chillers
            condenser_heat = exergy_in * 1.2
            recoverable = condenser_heat * 0.3  # 30% usable for hot water
            savings = recoverable * 4000 * 0.05  # fuel displacement
            if savings > 500:
                opportunities.append({
                    "type": "condenser_heat_to_hotwater",
                    "title": "Chiller Kondenser Isisi → Sicak Su",
                    "source": chiller["name"],
                    "target": "Sicak Su Sistemi",
                    "potential_recovery_kW": round(recoverable, 1),
                    "estimated_savings_EUR_year": round(savings, 0),
                    "estimated_investment_EUR": 12000,
                    "roi_years": round(12000 / savings, 1) if savings > 0 else 99,
                    "complexity": "medium",
                    "description": f"{chiller['name']} kondenser atik isisinin sicak su uretiminde kullanimi.",
                })

    # Pattern 5: Pump VSD retrofit
    for pump in pumps:
        pa = pump["analysis"]
        vsd_savings = pa.get("vsd_savings_potential_kW", 0) or 0
        if vsd_savings > 1:
            annual_savings = vsd_savings * 6000 * 0.12  # 6000h, 0.12 EUR/kWh
            motor_power = pa.get("exergy_in_kW", 10)
            investment = motor_power * 100  # ~100 EUR/kW for VSD
            opportunities.append({
                "type": "pump_vsd_retrofit",
                "title": "Pompa VSD Retrofit",
                "source": pump["name"],
                "target": pump["name"],
                "potential_recovery_kW": round(vsd_savings, 1),
                "estimated_savings_EUR_year": round(annual_savings, 0),
                "estimated_investment_EUR": round(investment, 0),
                "roi_years": round(investment / annual_savings, 1) if annual_savings > 0 else 99,
                "complexity": "low",
                "description": f"{pump['name']} kisma vanasi kontrolunden VSD'ye gecis.",
            })

    return opportunities


# ---------------------------------------------------------------------------
# Factory Sankey
# ---------------------------------------------------------------------------

def _generate_factory_sankey(results: List[dict], aggregates: dict) -> dict:
    """
    Fabrika seviyesi Sankey diyagrami.

    Yapisi:
    - Enerji Girisi (toplam) -> Her ekipman
    - Her ekipman -> Faydali Cikis | Kayip

    Her ekipman icin ayri node, ortak 'Faydali Exergy' ve 'Exergy Kaybi' node'lari.
    """
    if not results:
        return {
            "nodes": [],
            "links": [],
            "summary": {
                "total_input_kW": 0,
                "useful_output_kW": 0,
                "recoverable_heat_kW": 0,
                "irreversibility_kW": 0,
                "efficiency_pct": 0,
            },
        }

    nodes = []
    links = []

    # Node 0: Toplam Enerji Girisi
    nodes.append({"id": 0, "name": "Enerji Girisi", "name_en": "Energy Input"})

    # Equipment nodes start at id=1
    # Useful output node and Loss node will be at the end
    useful_node_id = len(results) + 1
    loss_node_id = len(results) + 2

    # Create equipment nodes
    type_labels = {
        "compressor": "Kompresor",
        "boiler": "Kazan",
        "chiller": "Chiller",
        "pump": "Pompa",
    }

    for i, r in enumerate(results):
        eq_node_id = i + 1
        label = f"{r['name']}"
        label_en = f"{r['name']}"
        nodes.append({"id": eq_node_id, "name": label, "name_en": label_en})

        a = r["analysis"]
        ex_in = a.get("exergy_in_kW", 0)
        ex_out = a.get("exergy_out_kW", 0)
        ex_loss = ex_in - ex_out

        # Link: Input -> Equipment
        if ex_in > 0:
            links.append({
                "source": 0,
                "target": eq_node_id,
                "value": round(ex_in, 2),
                "label": f"{r['name']} Girisi",
            })

        # Link: Equipment -> Useful Output
        if ex_out > 0:
            links.append({
                "source": eq_node_id,
                "target": useful_node_id,
                "value": round(ex_out, 2),
                "label": f"{r['name']} Faydali",
            })

        # Link: Equipment -> Loss
        if ex_loss > 0:
            links.append({
                "source": eq_node_id,
                "target": loss_node_id,
                "value": round(ex_loss, 2),
                "label": f"{r['name']} Kayip",
            })

    # Add output/loss summary nodes
    nodes.append({"id": useful_node_id, "name": "Faydali Exergy", "name_en": "Useful Exergy"})
    nodes.append({"id": loss_node_id, "name": "Exergy Kaybi", "name_en": "Exergy Loss"})

    return {
        "nodes": nodes,
        "links": links,
        "summary": {
            "total_input_kW": aggregates.get("total_exergy_input_kW", 0),
            "useful_output_kW": aggregates.get("total_exergy_output_kW", 0),
            "recoverable_heat_kW": 0,
            "irreversibility_kW": aggregates.get("total_exergy_destroyed_kW", 0),
            "efficiency_pct": aggregates.get("factory_exergy_efficiency_pct", 0),
        },
    }
