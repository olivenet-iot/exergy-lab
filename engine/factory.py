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
from .heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
from .steam_turbine import SteamTurbineInput, analyze_steam_turbine
from .dryer import DryerInput, analyze_dryer


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

class EquipmentType(str, Enum):
    COMPRESSOR = "compressor"
    BOILER = "boiler"
    CHILLER = "chiller"
    PUMP = "pump"
    HEAT_EXCHANGER = "heat_exchanger"
    STEAM_TURBINE = "steam_turbine"
    DRYER = "dryer"


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
    pinch_analysis: Optional[dict] = None
    advanced_exergy: Optional[dict] = None
    entropy_generation: Optional[dict] = None
    thermoeconomic_optimization: Optional[dict] = None


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

_HEAT_EXCHANGER_SUBTYPES = {
    "shell_tube", "plate", "air_cooled", "double_pipe",
    "spiral", "economizer", "recuperator", "finned_tube",
}

_STEAM_TURBINE_SUBTYPES = {
    "back_pressure", "condensing", "extraction", "orc", "micro_turbine",
    "backpressure",  # alias
}

_DRYER_SUBTYPES = {
    "convective", "rotary", "fluidized_bed", "spray",
    "belt", "heat_pump", "infrared", "drum",
    "conveyor", "tray", "microwave",
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
    elif eq_type == "heat_exchanger":
        return _analyze_heat_exchanger_item(subtype, params)
    elif eq_type == "steam_turbine":
        return _analyze_steam_turbine_item(subtype, params)
    elif eq_type == "dryer":
        return _analyze_dryer_item(subtype, params)
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


def _analyze_heat_exchanger_item(subtype: str, params: dict) -> dict:
    """Dispatch heat exchanger analysis."""
    engine_kwargs = _filter_params(params, HeatExchangerInput)
    engine_kwargs["hx_type"] = subtype

    input_data = HeatExchangerInput(**engine_kwargs)
    result = analyze_heat_exchanger(input_data)
    return result.to_dict()


def _analyze_steam_turbine_item(subtype: str, params: dict) -> dict:
    """Dispatch steam turbine analysis."""
    engine_kwargs = _filter_params(params, SteamTurbineInput)
    # Map registry subtype names to engine turbine_type
    turbine_type_map = {
        "back_pressure": "backpressure",
        "backpressure": "backpressure",
        "condensing": "condensing",
        "extraction": "extraction",
        "orc": "backpressure",
        "micro_turbine": "backpressure",
    }
    engine_kwargs["turbine_type"] = turbine_type_map.get(subtype, "backpressure")

    input_data = SteamTurbineInput(**engine_kwargs)
    result = analyze_steam_turbine(input_data)
    return result.to_dict()


def _analyze_dryer_item(subtype: str, params: dict) -> dict:
    """Dispatch dryer analysis."""
    engine_kwargs = _filter_params(params, DryerInput)
    # Map registry subtype names to engine dryer_type
    dryer_type_map = {
        "convective": "conveyor",
        "belt": "conveyor",
        "heat_pump": "conveyor",
    }
    engine_kwargs["dryer_type"] = dryer_type_map.get(subtype, subtype)

    input_data = DryerInput(**engine_kwargs)
    result = analyze_dryer(input_data)
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
    integration = _detect_integration_opportunities(valid_results, equipment_list)

    # 5. Generate factory Sankey
    sankey = _generate_factory_sankey(valid_results, aggregates)

    # 6. Pinch analysis (optional, best-effort)
    pinch_analysis = None
    try:
        from .pinch import analyze_pinch, extract_thermal_streams, check_pinch_feasibility

        results_dict = {r["id"]: r["analysis"] for r in valid_results if r.get("analysis")}
        streams = extract_thermal_streams(equipment_list, results_dict)
        feasible, _ = check_pinch_feasibility(streams)
        if feasible:
            pinch_result = analyze_pinch(equipment_list, results_dict)
            if pinch_result.is_valid:
                pinch_analysis = pinch_result.to_dict()
    except Exception:
        pass  # pinch_analysis stays None

    # 7. Advanced Exergy (optional, best-effort)
    advanced_exergy = None
    try:
        from .advanced_exergy import analyze_advanced_exergy, check_advanced_exergy_feasibility

        adv_results_dict = {r["id"]: r["analysis"] for r in valid_results if r.get("analysis")}
        eq_list_dicts = [
            {"id": item.id, "name": item.name, "equipment_type": item.equipment_type,
             "subtype": item.subtype, "parameters": item.parameters}
            for item in equipment_list
        ]
        feasible, _ = check_advanced_exergy_feasibility(eq_list_dicts, adv_results_dict)
        if feasible:
            adv_result = analyze_advanced_exergy(eq_list_dicts, adv_results_dict)
            if adv_result.is_valid:
                advanced_exergy = adv_result.to_dict()
    except Exception:
        pass

    # 8. EGM - Entropy Generation Minimization (optional, best-effort)
    entropy_generation = None
    try:
        from .entropy_generation import analyze_entropy_generation, check_egm_feasibility

        egm_results_dict = {r["id"]: r["analysis"] for r in valid_results if r.get("analysis")}
        egm_eq_list = [
            {"id": item.id, "name": item.name, "equipment_type": item.equipment_type,
             "subtype": item.subtype, "parameters": item.parameters}
            for item in equipment_list
        ]
        egm_feasible, _ = check_egm_feasibility(egm_eq_list, egm_results_dict)
        if egm_feasible:
            egm_result = analyze_entropy_generation(egm_eq_list, egm_results_dict)
            if egm_result.is_valid:
                entropy_generation = egm_result.to_dict()
    except Exception:
        pass

    # 9. Thermoeconomic Optimization (optional, best-effort)
    thermoeconomic_optimization = None
    try:
        from .thermoeconomic_optimization import analyze_thermoeconomic_optimization, check_thermoeconomic_feasibility

        thermo_results_dict = {r["id"]: r["analysis"] for r in valid_results if r.get("analysis")}
        thermo_eq_list = [
            {"id": item.id, "name": item.name, "equipment_type": item.equipment_type,
             "subtype": item.subtype, "parameters": item.parameters}
            for item in equipment_list
        ]
        thermo_feasible, _ = check_thermoeconomic_feasibility(thermo_eq_list, thermo_results_dict)
        if thermo_feasible:
            thermo_result = analyze_thermoeconomic_optimization(thermo_eq_list, thermo_results_dict)
            if thermo_result.is_valid:
                thermoeconomic_optimization = thermo_result.to_dict()
    except Exception:
        pass

    return FactoryAnalysisResult(
        equipment_results=equipment_results,
        aggregates=aggregates,
        hotspots=hotspots,
        integration_opportunities=integration,
        sankey=sankey,
        pinch_analysis=pinch_analysis,
        advanced_exergy=advanced_exergy,
        entropy_generation=entropy_generation,
        thermoeconomic_optimization=thermoeconomic_optimization,
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
    total_avoidable = 0.0
    total_unavoidable = 0.0

    for r in results:
        a = r["analysis"]
        total_in += a.get("exergy_in_kW", 0)
        total_out += a.get("exergy_out_kW", 0)
        total_destroyed += a.get("exergy_destroyed_kW", 0)
        total_annual_loss_kwh += a.get("annual_loss_kWh", 0) or 0
        total_annual_loss_eur += a.get("annual_loss_EUR", 0) or 0
        total_avoidable += a.get("exergy_destroyed_avoidable_kW", 0) or 0
        total_unavoidable += a.get("exergy_destroyed_unavoidable_kW", 0) or 0

    factory_efficiency = (total_out / total_in * 100) if total_in > 0 else 0.0
    avoidable_ratio = (total_avoidable / total_destroyed * 100) if total_destroyed > 0 else 0.0

    return {
        "total_exergy_input_kW": round(total_in, 2),
        "total_exergy_output_kW": round(total_out, 2),
        "total_exergy_destroyed_kW": round(total_destroyed, 2),
        "factory_exergy_efficiency_pct": round(factory_efficiency, 1),
        "total_annual_loss_kWh": round(total_annual_loss_kwh, 0),
        "total_annual_loss_EUR": round(total_annual_loss_eur, 0),
        "equipment_count": len(results),
        "total_exergy_destroyed_avoidable_kW": round(total_avoidable, 2),
        "total_exergy_destroyed_unavoidable_kW": round(total_unavoidable, 2),
        "avoidable_ratio_pct": round(avoidable_ratio, 1),
    }


# ---------------------------------------------------------------------------
# Hotspots
# ---------------------------------------------------------------------------

def _get_priority(efficiency: float, loss_kW: float, total_loss_kW: float) -> str:
    """
    Hotspot oncelik seviyesi belirle.

    Hem mutlak hem oransal kriterleri kullanir:
    - high: verim < %30 VEYA kayip > toplam kaybın %40'i VEYA mutlak kayip > 20 kW
    - medium: verim < %50 VEYA kayip > toplam kaybın %20'si VEYA mutlak kayip > 5 kW
    - low: diger
    """
    loss_ratio = (loss_kW / total_loss_kW) if total_loss_kW > 0 else 0

    if efficiency < 30 or loss_ratio > 0.40 or loss_kW > 20:
        return "high"
    elif efficiency < 50 or loss_ratio > 0.20 or loss_kW > 5:
        return "medium"
    else:
        return "low"


def _identify_hotspots(results: List[dict]) -> List[dict]:
    """Ekipmanlari exergy yikimina gore siralar (azalan)."""
    # Calculate total loss first for relative priority
    total_loss_kW = sum(
        r["analysis"].get("exergy_destroyed_kW", 0) for r in results
    )

    hotspots = []
    for r in results:
        a = r["analysis"]
        destroyed = a.get("exergy_destroyed_kW", 0)
        efficiency = a.get("exergy_efficiency_pct", 0)
        annual_loss = a.get("annual_loss_EUR", 0) or 0

        priority = _get_priority(efficiency, destroyed, total_loss_kW)

        hotspots.append({
            "id": r["id"],
            "name": r["name"],
            "equipment_type": r["equipment_type"],
            "subtype": r["subtype"],
            "exergy_destroyed_kW": round(destroyed, 2),
            "exergy_efficiency_pct": round(efficiency, 1),
            "annual_loss_EUR": round(annual_loss, 0),
            "priority": priority,
        })

    # Sort by exergy destruction descending
    hotspots.sort(key=lambda x: x["exergy_destroyed_kW"], reverse=True)
    return hotspots


# ---------------------------------------------------------------------------
# Integration opportunities
# ---------------------------------------------------------------------------

def _detect_integration_opportunities(
    results: List[dict],
    equipment_list: List[EquipmentItem],
) -> List[dict]:
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

    # Build lookup from equipment id -> original EquipmentItem for parameter access
    eq_lookup = {item.id: item for item in equipment_list}

    # Categorize equipment
    compressors = [r for r in results if r["equipment_type"] == "compressor"]
    boilers = [r for r in results if r["equipment_type"] == "boiler"]
    chillers = [r for r in results if r["equipment_type"] == "chiller"]
    pumps = [r for r in results if r["equipment_type"] == "pump"]
    heat_exchangers = [r for r in results if r["equipment_type"] == "heat_exchanger"]
    steam_turbines = [r for r in results if r["equipment_type"] == "steam_turbine"]
    dryers = [r for r in results if r["equipment_type"] == "dryer"]

    # Helper: get compressor thermal power from first principles
    # ~90% of electrical input becomes heat, ~75% is recoverable via oil cooler / aftercooler
    def _compressor_recoverable_kW(comp_result: dict) -> float:
        ca = comp_result["analysis"]
        power_kW = ca.get("exergy_in_kW", 0)  # equals electrical input for compressors
        if not power_kW:
            # Fallback to original parameters
            item = eq_lookup.get(comp_result["id"])
            if item:
                power_kW = item.parameters.get("power_kW", 0) or 0
        return power_kW * 0.90 * 0.75  # ~67.5% of input is recoverable heat

    def _get_operating_hours(comp_result: dict, default: int = 6000) -> int:
        item = eq_lookup.get(comp_result["id"])
        if item:
            return item.parameters.get("operating_hours", default) or default
        return default

    # Pattern 1: Compressor waste heat -> Boiler feedwater preheating
    if compressors and boilers:
        for comp in compressors:
            recoverable = _compressor_recoverable_kW(comp)
            if recoverable > 0:
                hours = _get_operating_hours(comp)
                usable = recoverable * 0.60  # 60% heat exchanger effectiveness
                savings = usable * hours * 0.05  # ~0.05 EUR/kWh fuel displaced
                investment = 15000
                for boiler in boilers:
                    opportunities.append({
                        "type": "compressor_heat_to_boiler",
                        "title": "Kompresor Atik Isisi → Kazan Besleme Suyu",
                        "source": comp["name"],
                        "target": boiler["name"],
                        "potential_recovery_kW": round(usable, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": investment,
                        "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                        "complexity": "medium",
                        "description": f"{comp['name']} atik isisinin {boiler['name']} besleme suyu on isitmada kullanimi. "
                                       f"Tahmini geri kazanilabilir isi: {usable:.1f} kW.",
                    })
                    break  # One opportunity per compressor

    # Pattern 2: Compressor waste heat -> Space heating
    for comp in compressors:
        recoverable = _compressor_recoverable_kW(comp)
        if recoverable > 3:  # At least 3 kW
            usable = recoverable * 0.50  # 50% useful for space heating
            savings = usable * 2000 * 0.06  # 2000h heating season, gas price
            investment = 8000
            opportunities.append({
                "type": "compressor_heat_to_space",
                "title": "Kompresor Atik Isisi → Mekan Isitma",
                "source": comp["name"],
                "target": "Mekan Isitma Sistemi",
                "potential_recovery_kW": round(usable, 1),
                "estimated_savings_EUR_year": round(savings, 0),
                "estimated_investment_EUR": investment,
                "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                "complexity": "low",
                "description": f"{comp['name']} atik isisinin mekan isitmada kullanimi (kis sezonu).",
            })

    # Pattern 3: Boiler flue gas -> Absorption chiller
    if boilers and chillers:
        for boiler in boilers:
            ba = boiler["analysis"]
            flue_gas_loss = ba.get("flue_gas_loss_kW", 0) or 0
            if flue_gas_loss > 10:
                hours = _get_operating_hours(boiler, 4000)
                cooling_potential = flue_gas_loss * 0.5 * 0.7  # 50% capture, COP 0.7
                electricity_saved = cooling_potential / 4.0  # replaces electric chiller COP=4
                savings = electricity_saved * hours * 0.12
                investment = 50000
                for chiller in chillers:
                    opportunities.append({
                        "type": "flue_gas_to_absorption",
                        "title": "Kazan Baca Gazi → Absorpsiyonlu Chiller",
                        "source": boiler["name"],
                        "target": chiller["name"],
                        "potential_recovery_kW": round(cooling_potential, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": investment,
                        "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                        "complexity": "high",
                        "description": f"{boiler['name']} baca gazi isisi ile {chiller['name']} yerine absorpsiyonlu sogutma.",
                    })
                    break

    # Pattern 4: Chiller condenser heat -> Hot water
    for chiller in chillers:
        ca = chiller["analysis"]
        # Use cooling capacity + compressor power as condenser rejection
        cooling_kW = ca.get("cooling_capacity_kW", 0) or 0
        comp_power = ca.get("compressor_power_kW", 0) or ca.get("exergy_in_kW", 0)
        condenser_heat = cooling_kW + comp_power if cooling_kW else comp_power * 1.2
        if condenser_heat > 10:
            recoverable = condenser_heat * 0.30  # 30% usable for hot water
            hours = _get_operating_hours(chiller, 4000)
            savings = recoverable * hours * 0.05  # fuel displacement
            investment = 12000
            if savings > 500:
                opportunities.append({
                    "type": "condenser_heat_to_hotwater",
                    "title": "Chiller Kondenser Isisi → Sicak Su",
                    "source": chiller["name"],
                    "target": "Sicak Su Sistemi",
                    "potential_recovery_kW": round(recoverable, 1),
                    "estimated_savings_EUR_year": round(savings, 0),
                    "estimated_investment_EUR": investment,
                    "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                    "complexity": "medium",
                    "description": f"{chiller['name']} kondenser atik isisinin sicak su uretiminde kullanimi.",
                })

    # Pattern 5: Pump VSD retrofit
    for pump in pumps:
        pa = pump["analysis"]
        vsd_savings = pa.get("vsd_savings_potential_kW", 0) or 0
        if vsd_savings > 1:
            hours = _get_operating_hours(pump)
            annual_savings = vsd_savings * hours * 0.12
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

    # Pattern 6: Dryer exhaust → HX for air preheating
    if dryers and heat_exchangers:
        for dryer in dryers:
            da = dryer["analysis"]
            exhaust_ex = da.get("exhaust_exergy_kW", 0) or 0
            if exhaust_ex > 5:
                hours = _get_operating_hours(dryer, 5000)
                usable = exhaust_ex * 0.5
                savings = usable * hours * 0.05
                investment = 12000
                for hx in heat_exchangers:
                    opportunities.append({
                        "type": "dryer_exhaust_to_hx",
                        "title": "Kurutucu Egzoz → Isi Esanjoru On Isitma",
                        "source": dryer["name"],
                        "target": hx["name"],
                        "potential_recovery_kW": round(usable, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": investment,
                        "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                        "complexity": "medium",
                        "description": f"{dryer['name']} egzoz isisi ile {hx['name']} giris havasini on isitma.",
                    })
                    break

    # Pattern 7: Steam turbine exhaust → absorption chiller
    if steam_turbines and chillers:
        for st in steam_turbines:
            sa = st["analysis"]
            exhaust_ex = sa.get("exhaust_exergy_kW", 0) or 0
            if exhaust_ex > 50:
                hours = _get_operating_hours(st, 6000)
                cooling_potential = exhaust_ex * 0.4 * 0.7
                electricity_saved = cooling_potential / 4.0
                savings = electricity_saved * hours * 0.12
                investment = 60000
                for chiller in chillers:
                    opportunities.append({
                        "type": "turbine_exhaust_to_absorption",
                        "title": "Buhar Turbini Egzoz → Absorpsiyonlu Chiller",
                        "source": st["name"],
                        "target": chiller["name"],
                        "potential_recovery_kW": round(cooling_potential, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": investment,
                        "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                        "complexity": "high",
                        "description": f"{st['name']} egzoz buhari ile {chiller['name']} yerine absorpsiyonlu sogutma.",
                    })
                    break

    # Pattern 8: Boiler flue gas → HX economizer for feedwater
    if boilers and heat_exchangers:
        for boiler in boilers:
            ba = boiler["analysis"]
            flue_gas_loss = ba.get("flue_gas_loss_kW", 0) or 0
            if flue_gas_loss > 10:
                hours = _get_operating_hours(boiler, 6000)
                usable = flue_gas_loss * 0.45
                savings = usable * hours * 0.05
                investment = 18000
                for hx in heat_exchangers:
                    opportunities.append({
                        "type": "boiler_flue_to_hx_economizer",
                        "title": "Kazan Baca Gazi → Ekonomizer (HX)",
                        "source": boiler["name"],
                        "target": hx["name"],
                        "potential_recovery_kW": round(usable, 1),
                        "estimated_savings_EUR_year": round(savings, 0),
                        "estimated_investment_EUR": investment,
                        "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                        "complexity": "medium",
                        "description": f"{boiler['name']} baca gazi isisi ile {hx['name']} kullanarak besleme suyu on isitma.",
                    })
                    break

    # Pattern 9: Steam turbine CHP → plant heating
    for st in steam_turbines:
        sa = st["analysis"]
        heat_recovered = sa.get("heat_recovered_kW", 0) or 0
        if heat_recovered == 0:
            exhaust_ex = sa.get("exhaust_exergy_kW", 0) or 0
            if exhaust_ex > 100:
                hours = _get_operating_hours(st, 6000)
                usable = exhaust_ex * 0.5
                savings = usable * hours * 0.04
                investment = 40000
                opportunities.append({
                    "type": "turbine_chp_heating",
                    "title": "Buhar Turbini CHP → Tesis Isitma",
                    "source": st["name"],
                    "target": "Tesis Isitma Sistemi",
                    "potential_recovery_kW": round(usable, 1),
                    "estimated_savings_EUR_year": round(savings, 0),
                    "estimated_investment_EUR": investment,
                    "roi_years": round(investment / savings, 1) if savings > 0 else 99,
                    "complexity": "medium",
                    "description": f"{st['name']} egzoz buharindan CHP ile tesis isitma.",
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
        "heat_exchanger": "Isi Esanjoru",
        "steam_turbine": "Buhar Turbini",
        "dryer": "Kurutma Firini",
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

    # Check if AV/UN data is available at factory level
    total_av = aggregates.get("total_exergy_destroyed_avoidable_kW", 0)
    total_un = aggregates.get("total_exergy_destroyed_unavoidable_kW", 0)
    has_av_un = (total_av > 0 or total_un > 0)

    if has_av_un:
        av_node_id = loss_node_id
        un_node_id = loss_node_id + 1
        nodes.append({"id": av_node_id, "name": "Exergy Kaybi (Onlenebilir)", "name_en": "Exergy Loss (Avoidable)", "color": "#e74c3c"})
        nodes.append({"id": un_node_id, "name": "Exergy Kaybi (Onlenemez)", "name_en": "Exergy Loss (Unavoidable)", "color": "#95a5a6"})

        # Redistribute existing loss links into AV and UN
        total_loss_sum = total_av + total_un
        new_links = []
        for link in links:
            if link["target"] == loss_node_id:
                loss_val = link["value"]
                if total_loss_sum > 0:
                    av_share = loss_val * (total_av / total_loss_sum)
                    un_share = loss_val * (total_un / total_loss_sum)
                else:
                    av_share = loss_val
                    un_share = 0
                if av_share > 0.01:
                    new_links.append({
                        "source": link["source"],
                        "target": av_node_id,
                        "value": round(av_share, 2),
                        "label": link["label"].replace("Kayip", "Onlenebilir"),
                    })
                if un_share > 0.01:
                    new_links.append({
                        "source": link["source"],
                        "target": un_node_id,
                        "value": round(un_share, 2),
                        "label": link["label"].replace("Kayip", "Onlenemez"),
                    })
            else:
                new_links.append(link)
        links = new_links
    else:
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
            "exergy_destroyed_avoidable_kW": round(total_av, 2),
            "exergy_destroyed_unavoidable_kW": round(total_un, 2),
            "avoidable_ratio_pct": aggregates.get("avoidable_ratio_pct", 0),
        },
    }
