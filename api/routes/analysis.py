"""Analysis routes for ExergyLab API."""

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from engine.compressor import (
    CompressorInput, PistonCompressorInput,
    ScrollCompressorInput, CentrifugalCompressorInput,
    analyze_compressor, analyze_piston_compressor,
    analyze_scroll_compressor, analyze_centrifugal_compressor,
)
from engine.boiler import BoilerInput, analyze_boiler
from engine.chiller import ChillerInput, analyze_chiller
from engine.pump import PumpInput, analyze_pump
from engine.heat_exchanger import HeatExchangerInput, analyze_heat_exchanger
from engine.steam_turbine import SteamTurbineInput, analyze_steam_turbine
from engine.dryer import DryerInput, analyze_dryer
from engine.sankey import generate_sankey_data
from engine.radar import generate_radar_data
from engine.compare import compute_comparison
from api.schemas.requests import (
    AnalysisRequest, CompareRequest, ScrewCompressorParams,
    PistonCompressorParams, ScrollCompressorParams,
    CentrifugalCompressorParams,
    BoilerParams, VaporCompressionChillerParams,
    AbsorptionChillerParams, PumpParams,
    HeatExchangerParams, SteamTurbineParams, DryerParams,
)
from api.schemas.responses import (
    AnalysisResponse, MetricsResponse, HeatRecoveryResponse,
    BenchmarkDetailResponse, SankeyResponse,
    RadarDataResponse, RadarScoreResponse, RadarAxisResponse,
    CompressorTypesListResponse, CompressorTypeResponse, CompressorFieldResponse,
    EquipmentTypeConfigResponse, EquipmentSubtypeConfig,
    CompareResponse, ComparisonData, ComparisonSavings,
)
from api.services.equipment_registry import (
    get_equipment_types,
    get_equipment_subtypes,
    is_valid_equipment,
    is_engine_ready,
)

router = APIRouter()


def _build_radar_response(api_dict: dict, operating_hours: int = 6000) -> RadarDataResponse:
    """Build RadarDataResponse from engine api_dict."""
    raw = generate_radar_data(api_dict, operating_hours)
    return RadarDataResponse(
        axes=[RadarAxisResponse(**a) for a in raw["axes"]],
        scores=RadarScoreResponse(**raw["scores"]),
        overall_score=raw["overall_score"],
        grade=raw["grade"],
        grade_letter=raw["grade_letter"],
        grade_en=raw["grade_en"],
    )


# Param validators per compressor subtype
_COMPRESSOR_VALIDATORS = {
    "screw": ScrewCompressorParams,
    "piston": PistonCompressorParams,
    "scroll": ScrollCompressorParams,
    "centrifugal": CentrifugalCompressorParams,
}

# Engine dispatch for compressor subtypes
_COMPRESSOR_ANALYZERS = {
    "screw": (CompressorInput, analyze_compressor),
    "piston": (PistonCompressorInput, analyze_piston_compressor),
    "scroll": (ScrollCompressorInput, analyze_scroll_compressor),
    "centrifugal": (CentrifugalCompressorInput, analyze_centrifugal_compressor),
}

# Boiler: all subtypes share same validator and analyzer
_BOILER_SUBTYPES = {
    "steam_firetube", "steam_watertube", "hotwater", "condensing",
    "waste_heat", "electric", "biomass",
}

# Chiller: vapor compression vs absorption
_VC_CHILLER_SUBTYPES = {"screw", "centrifugal", "scroll", "reciprocating", "air_cooled", "water_cooled"}
_ABS_CHILLER_SUBTYPES = {"absorption"}

# Pump: all subtypes share same validator and analyzer
_PUMP_SUBTYPES = {
    "centrifugal", "positive_displacement", "submersible",
    "vertical_turbine", "booster", "vacuum",
}

# Heat exchanger subtypes
_HE_SUBTYPES = {
    "shell_tube", "plate", "air_cooled", "double_pipe",
    "spiral", "economizer", "recuperator", "finned_tube",
}

# Steam turbine subtypes
_ST_SUBTYPES = {
    "back_pressure", "condensing", "extraction", "orc", "micro_turbine",
    "backpressure",
}

# Dryer subtypes
_DRYER_SUBTYPES = {
    "convective", "rotary", "fluidized_bed", "spray",
    "belt", "heat_pump", "infrared", "drum",
    "conveyor", "tray", "microwave",
}


@router.get("/equipment-types")
async def list_equipment_types():
    """Tum desteklenen ekipman tiplerini listele."""
    return {"equipment_types": get_equipment_types()}


@router.get("/equipment-types/{equipment_type}/subtypes")
async def list_subtypes(equipment_type: str):
    """Belirli ekipman tipinin alt tiplerini listele."""
    if not is_valid_equipment(equipment_type):
        raise HTTPException(status_code=404, detail=f"Unknown equipment type: {equipment_type}")
    return {"subtypes": get_equipment_subtypes(equipment_type)}


def _dispatch_analysis(equipment_type: str, subtype: str, parameters: dict) -> AnalysisResponse:
    """Dispatch analysis to the appropriate equipment handler.

    Args:
        equipment_type: Equipment category (compressor, boiler, etc.)
        subtype: Equipment subtype (screw, steam_firetube, etc.)
        parameters: Analysis parameters dict.

    Returns:
        AnalysisResponse with full analysis results.
    """
    if equipment_type == "compressor":
        return _analyze_compressor(subtype, parameters)
    elif equipment_type == "boiler":
        return _analyze_boiler(subtype, parameters)
    elif equipment_type == "chiller":
        return _analyze_chiller(subtype, parameters)
    elif equipment_type == "pump":
        return _analyze_pump(subtype, parameters)
    elif equipment_type == "heat_exchanger":
        return _analyze_heat_exchanger(subtype, parameters)
    elif equipment_type == "steam_turbine":
        return _analyze_steam_turbine(subtype, parameters)
    elif equipment_type == "dryer":
        return _analyze_dryer(subtype, parameters)
    else:
        raise HTTPException(status_code=422, detail=f"Unsupported equipment type: {equipment_type}")


def _flatten_analysis_response(resp: AnalysisResponse) -> dict:
    """Merge metrics + heat_recovery into a flat dict for comparison engine."""
    flat = resp.metrics.model_dump()
    flat.update(resp.heat_recovery.model_dump())
    return flat


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest):
    """Ekipman exergy analizi yapar. Hem eski hem yeni format desteklenir."""
    # Normalize: support both old (compressor_type) and new (equipment_type/subtype) formats
    if request.compressor_type and not request.equipment_type:
        equipment_type = "compressor"
        subtype = request.compressor_type
    elif request.equipment_type:
        equipment_type = request.equipment_type
        subtype = request.subtype
        if not is_engine_ready(equipment_type):
            raise HTTPException(
                status_code=501,
                detail="Bu ekipman tipi henuz desteklenmiyor",
            )
    else:
        raise HTTPException(status_code=422, detail="compressor_type or equipment_type is required")

    return _dispatch_analysis(equipment_type, subtype, request.parameters)


@router.post("/compare", response_model=CompareResponse)
async def compare_scenarios(request: CompareRequest):
    """Compare baseline vs scenario analysis for What-If mode."""
    if not is_engine_ready(request.equipment_type):
        raise HTTPException(
            status_code=501,
            detail="Bu ekipman tipi henuz desteklenmiyor",
        )

    subtype = request.subtype
    if not subtype:
        raise HTTPException(status_code=422, detail="subtype is required for comparison")

    # Run both analyses
    baseline_resp = _dispatch_analysis(request.equipment_type, subtype, request.baseline_params)
    scenario_resp = _dispatch_analysis(request.equipment_type, subtype, request.scenario_params)

    # Flatten for comparison engine
    baseline_flat = _flatten_analysis_response(baseline_resp)
    scenario_flat = _flatten_analysis_response(scenario_resp)

    # Determine energy price from params (cascade)
    energy_price = (
        request.baseline_params.get("electricity_price_eur_kwh")
        or request.baseline_params.get("fuel_price_eur_kwh")
        or request.baseline_params.get("fuel_price_eur_kg")
        or 0.10
    )
    operating_hours = request.baseline_params.get("operating_hours", 6000)

    comparison_raw = compute_comparison(
        baseline_flat, scenario_flat,
        energy_price_eur_kwh=float(energy_price),
        operating_hours=float(operating_hours),
    )

    comparison = ComparisonData(
        delta=comparison_raw["delta"],
        delta_pct=comparison_raw["delta_pct"],
        savings=ComparisonSavings(**comparison_raw["savings"]),
        improved_metrics=comparison_raw["improved_metrics"],
        degraded_metrics=comparison_raw["degraded_metrics"],
        summary_tr=comparison_raw["summary_tr"],
    )

    return CompareResponse(
        baseline=baseline_resp,
        scenario=scenario_resp,
        comparison=comparison,
    )


def _analyze_compressor(comp_type: str, parameters: dict) -> AnalysisResponse:
    """Compressor analysis dispatch."""
    validator_cls = _COMPRESSOR_VALIDATORS.get(comp_type)
    if not validator_cls:
        raise HTTPException(status_code=422, detail=f"Unknown compressor type: {comp_type}")

    try:
        validated = validator_cls(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    input_cls, analyze_fn = _COMPRESSOR_ANALYZERS[comp_type]
    params = validated.model_dump(exclude_none=False)

    engine_kwargs = {}
    for key, val in params.items():
        if val is not None:
            engine_kwargs[key] = val
        elif key in ("inlet_temp_C", "outlet_temp_C", "ambient_temp_C"):
            pass
        else:
            engine_kwargs[key] = val

    input_data = input_cls(**engine_kwargs)
    result = analyze_fn(input_data)

    api_dict = result.to_api_dict(comp_type)
    sankey_data = generate_sankey_data(result, comp_type)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 6000) or 6000)

    return AnalysisResponse(
        compressor_type=comp_type,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            mass_flow_kg_s=api_dict.get("mass_flow_kg_s"),
            specific_power_kW_m3min=api_dict.get("specific_power_kW_m3min"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
            exergoeconomic_Z_dot_eur_h=api_dict.get("exergoeconomic_Z_dot_eur_h"),
            exergoeconomic_C_dot_destruction_eur_h=api_dict.get("exergoeconomic_C_dot_destruction_eur_h"),
            exergoeconomic_f_factor=api_dict.get("exergoeconomic_f_factor"),
            exergoeconomic_r_factor=api_dict.get("exergoeconomic_r_factor"),
            exergoeconomic_c_product_eur_kWh=api_dict.get("exergoeconomic_c_product_eur_kWh"),
            exergoeconomic_total_cost_rate_eur_h=api_dict.get("exergoeconomic_total_cost_rate_eur_h"),
        ),
        heat_recovery=HeatRecoveryResponse(
            heat_recovery_potential_kW=api_dict.get("heat_recovery_potential_kW"),
            heat_recovery_savings_eur_year=api_dict.get("heat_recovery_savings_eur_year"),
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


def _analyze_boiler(subtype: str, parameters: dict) -> AnalysisResponse:
    """Boiler analysis dispatch."""
    if subtype not in _BOILER_SUBTYPES:
        raise HTTPException(status_code=422, detail=f"Unknown boiler type: {subtype}")

    try:
        validated = BoilerParams(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    params = validated.model_dump(exclude_none=False)
    engine_kwargs = {k: v for k, v in params.items() if v is not None}
    engine_kwargs["boiler_type"] = subtype

    input_data = BoilerInput(**engine_kwargs)
    result = analyze_boiler(input_data)

    api_dict = result.to_api_dict(subtype)
    sankey_data = generate_sankey_data(result, subtype)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 6000) or 6000)

    return AnalysisResponse(
        compressor_type=subtype,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            thermal_efficiency_pct=api_dict.get("thermal_efficiency_pct"),
            combustion_loss_kW=api_dict.get("combustion_loss_kW"),
            flue_gas_loss_kW=api_dict.get("flue_gas_loss_kW"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
            exergoeconomic_Z_dot_eur_h=api_dict.get("exergoeconomic_Z_dot_eur_h"),
            exergoeconomic_C_dot_destruction_eur_h=api_dict.get("exergoeconomic_C_dot_destruction_eur_h"),
            exergoeconomic_f_factor=api_dict.get("exergoeconomic_f_factor"),
            exergoeconomic_r_factor=api_dict.get("exergoeconomic_r_factor"),
            exergoeconomic_c_product_eur_kWh=api_dict.get("exergoeconomic_c_product_eur_kWh"),
            exergoeconomic_total_cost_rate_eur_h=api_dict.get("exergoeconomic_total_cost_rate_eur_h"),
        ),
        heat_recovery=HeatRecoveryResponse(
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


def _analyze_chiller(subtype: str, parameters: dict) -> AnalysisResponse:
    """Chiller analysis dispatch."""
    is_absorption = subtype in _ABS_CHILLER_SUBTYPES
    is_vc = subtype in _VC_CHILLER_SUBTYPES

    if not is_absorption and not is_vc:
        raise HTTPException(status_code=422, detail=f"Unknown chiller type: {subtype}")

    try:
        if is_absorption:
            validated = AbsorptionChillerParams(**parameters)
        else:
            validated = VaporCompressionChillerParams(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    params = validated.model_dump(exclude_none=False)
    engine_kwargs = {k: v for k, v in params.items() if v is not None}
    engine_kwargs["chiller_type"] = subtype

    input_data = ChillerInput(**engine_kwargs)
    result = analyze_chiller(input_data)

    api_dict = result.to_api_dict(subtype)
    sankey_data = generate_sankey_data(result, subtype)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 4000) or 4000)

    return AnalysisResponse(
        compressor_type=subtype,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            cop=api_dict.get("cop"),
            cop_carnot=api_dict.get("cop_carnot"),
            kw_per_ton=api_dict.get("kw_per_ton"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
            exergoeconomic_Z_dot_eur_h=api_dict.get("exergoeconomic_Z_dot_eur_h"),
            exergoeconomic_C_dot_destruction_eur_h=api_dict.get("exergoeconomic_C_dot_destruction_eur_h"),
            exergoeconomic_f_factor=api_dict.get("exergoeconomic_f_factor"),
            exergoeconomic_r_factor=api_dict.get("exergoeconomic_r_factor"),
            exergoeconomic_c_product_eur_kWh=api_dict.get("exergoeconomic_c_product_eur_kWh"),
            exergoeconomic_total_cost_rate_eur_h=api_dict.get("exergoeconomic_total_cost_rate_eur_h"),
        ),
        heat_recovery=HeatRecoveryResponse(
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


def _analyze_pump(subtype: str, parameters: dict) -> AnalysisResponse:
    """Pump analysis dispatch."""
    if subtype not in _PUMP_SUBTYPES:
        raise HTTPException(status_code=422, detail=f"Unknown pump type: {subtype}")

    try:
        validated = PumpParams(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    params = validated.model_dump(exclude_none=False)
    engine_kwargs = {k: v for k, v in params.items() if v is not None}
    engine_kwargs["pump_type"] = subtype

    input_data = PumpInput(**engine_kwargs)
    result = analyze_pump(input_data)

    api_dict = result.to_api_dict(subtype)
    sankey_data = generate_sankey_data(result, subtype)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 6000) or 6000)

    return AnalysisResponse(
        compressor_type=subtype,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            hydraulic_power_kW=api_dict.get("hydraulic_power_kW"),
            wire_to_water_efficiency_pct=api_dict.get("wire_to_water_efficiency_pct"),
            throttle_loss_kW=api_dict.get("throttle_loss_kW"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
            exergoeconomic_Z_dot_eur_h=api_dict.get("exergoeconomic_Z_dot_eur_h"),
            exergoeconomic_C_dot_destruction_eur_h=api_dict.get("exergoeconomic_C_dot_destruction_eur_h"),
            exergoeconomic_f_factor=api_dict.get("exergoeconomic_f_factor"),
            exergoeconomic_r_factor=api_dict.get("exergoeconomic_r_factor"),
            exergoeconomic_c_product_eur_kWh=api_dict.get("exergoeconomic_c_product_eur_kWh"),
            exergoeconomic_total_cost_rate_eur_h=api_dict.get("exergoeconomic_total_cost_rate_eur_h"),
        ),
        heat_recovery=HeatRecoveryResponse(
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


def _analyze_heat_exchanger(subtype: str, parameters: dict) -> AnalysisResponse:
    """Heat exchanger analysis dispatch."""
    if subtype not in _HE_SUBTYPES:
        raise HTTPException(status_code=422, detail=f"Unknown heat exchanger type: {subtype}")

    try:
        validated = HeatExchangerParams(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    params = validated.model_dump(exclude_none=False)
    engine_kwargs = {k: v for k, v in params.items() if v is not None}
    engine_kwargs["hx_type"] = subtype

    input_data = HeatExchangerInput(**engine_kwargs)
    result = analyze_heat_exchanger(input_data)

    api_dict = result.to_api_dict(subtype)
    sankey_data = generate_sankey_data(result, subtype)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 6000) or 6000)

    return AnalysisResponse(
        compressor_type=subtype,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            heat_duty_kW=api_dict.get("heat_duty_kW"),
            lmtd_K=api_dict.get("lmtd_K"),
            effectiveness=api_dict.get("effectiveness"),
            bejan_number=api_dict.get("bejan_number"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
        ),
        heat_recovery=HeatRecoveryResponse(
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


def _analyze_steam_turbine(subtype: str, parameters: dict) -> AnalysisResponse:
    """Steam turbine analysis dispatch."""
    if subtype not in _ST_SUBTYPES:
        raise HTTPException(status_code=422, detail=f"Unknown steam turbine type: {subtype}")

    try:
        validated = SteamTurbineParams(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    params = validated.model_dump(exclude_none=False)
    engine_kwargs = {k: v for k, v in params.items() if v is not None}
    # Map registry subtype to engine turbine_type
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

    api_dict = result.to_api_dict(engine_kwargs["turbine_type"])
    sankey_data = generate_sankey_data(result, subtype)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 7000) or 7000)

    return AnalysisResponse(
        compressor_type=subtype,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            shaft_power_kW=api_dict.get("shaft_power_kW"),
            electrical_power_kW=api_dict.get("electrical_power_kW"),
            chp_exergy_efficiency_pct=api_dict.get("chp_exergy_efficiency_pct"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
        ),
        heat_recovery=HeatRecoveryResponse(
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


def _analyze_dryer(subtype: str, parameters: dict) -> AnalysisResponse:
    """Dryer analysis dispatch."""
    if subtype not in _DRYER_SUBTYPES:
        raise HTTPException(status_code=422, detail=f"Unknown dryer type: {subtype}")

    try:
        validated = DryerParams(**parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    params = validated.model_dump(exclude_none=False)
    engine_kwargs = {k: v for k, v in params.items() if v is not None}
    # Map registry subtype to engine dryer_type
    dryer_type_map = {
        "convective": "conveyor",
        "belt": "conveyor",
        "heat_pump": "conveyor",
    }
    engine_kwargs["dryer_type"] = dryer_type_map.get(subtype, subtype)

    input_data = DryerInput(**engine_kwargs)
    result = analyze_dryer(input_data)

    api_dict = result.to_api_dict(engine_kwargs["dryer_type"])
    sankey_data = generate_sankey_data(result, subtype)
    radar_response = _build_radar_response(api_dict, getattr(validated, 'operating_hours', 5000) or 5000)

    return AnalysisResponse(
        compressor_type=subtype,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            thermal_efficiency_pct=api_dict.get("thermal_efficiency_pct"),
            water_removed_kg_h=api_dict.get("water_removed_kg_h"),
            specific_energy_kJ_kg_water=api_dict.get("specific_energy_kJ_kg_water"),
            exergy_destroyed_avoidable_kW=api_dict.get("exergy_destroyed_avoidable_kW"),
            exergy_destroyed_unavoidable_kW=api_dict.get("exergy_destroyed_unavoidable_kW"),
            avoidable_ratio_pct=api_dict.get("avoidable_ratio_pct"),
        ),
        heat_recovery=HeatRecoveryResponse(
            annual_loss_kWh=api_dict.get("annual_loss_kWh"),
            annual_loss_EUR=api_dict.get("annual_loss_EUR"),
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict.get("benchmark_comparison"),
            benchmark_percentile=api_dict.get("benchmark_percentile"),
            comparison_text=api_dict.get("comparison_text"),
        ),
        sankey=SankeyResponse(**sankey_data),
        radar_data=radar_response,
    )


# ---------------------------------------------------------------------------
# Equipment config endpoint
# ---------------------------------------------------------------------------

@router.get("/equipment-types/{equipment_type}/config", response_model=EquipmentTypeConfigResponse)
async def get_equipment_config(equipment_type: str):
    """Returns subtypes with field definitions for any equipment type."""
    if not is_valid_equipment(equipment_type):
        raise HTTPException(status_code=404, detail=f"Unknown equipment type: {equipment_type}")

    if equipment_type == "compressor":
        return _get_compressor_config()
    elif equipment_type == "boiler":
        return _get_boiler_config()
    elif equipment_type == "chiller":
        return _get_chiller_config()
    elif equipment_type == "pump":
        return _get_pump_config()
    elif equipment_type == "heat_exchanger":
        return _get_heat_exchanger_config()
    elif equipment_type == "steam_turbine":
        return _get_steam_turbine_config()
    elif equipment_type == "dryer":
        return _get_dryer_config()
    else:
        raise HTTPException(status_code=404, detail=f"No config for: {equipment_type}")


def _get_compressor_config() -> EquipmentTypeConfigResponse:
    """Compressor config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="power_kW", label="Elektrik Gücü", type="number", required=True, default=37, min=0.1, max=5000, unit="kW"),
        CompressorFieldResponse(name="flow_rate_m3_min", label="Hava Debisi", type="number", required=True, default=6.2, min=0.1, max=500, unit="m³/min"),
        CompressorFieldResponse(name="outlet_pressure_bar", label="Çıkış Basıncı", type="number", required=True, default=7.5, min=1, max=50, unit="bar"),
        CompressorFieldResponse(name="inlet_temp_C", label="Giriş Sıcaklığı", type="number", required=False, default=25.0, min=-20, max=60, unit="°C"),
        CompressorFieldResponse(name="outlet_temp_C", label="Çıkış Sıcaklığı", type="number", required=False, min=20, max=300, unit="°C"),
        CompressorFieldResponse(name="ambient_temp_C", label="Ortam Sıcaklığı", type="number", required=False, default=25.0, min=-20, max=60, unit="°C"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=6000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="load_factor", label="Yük Faktörü", type="number", required=False, default=0.75, min=0, max=1, hint="0-1 arası, tipik değer 0.65-0.85"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.12, min=0, max=1, unit="€/kWh"),
        CompressorFieldResponse(name="equipment_cost_eur", label="Ekipman Maliyeti", type="number", required=False, min=0, max=50000000, unit="EUR", hint="Bos birakilirsa otomatik tahmin yapilir"),
    ]

    subtypes = [
        EquipmentSubtypeConfig(id="screw", name="Vidalı Kompresör", description="Endüstriyel vidalı kompresör analizi", fields=common_fields),
        EquipmentSubtypeConfig(id="piston", name="Pistonlu Kompresör", description="Pistonlu kompresör analizi", fields=common_fields + [
            CompressorFieldResponse(name="stages", label="Kademe Sayısı", type="number", required=False, default=1, min=1, max=4),
            CompressorFieldResponse(name="cooling_type", label="Soğutma Tipi", type="select", required=False, options=["air", "water"]),
        ]),
        EquipmentSubtypeConfig(id="scroll", name="Scroll Kompresör", description="Scroll kompresör analizi", fields=common_fields + [
            CompressorFieldResponse(name="oil_free", label="Yağsız", type="boolean", required=False, default=0),
        ]),
        EquipmentSubtypeConfig(id="centrifugal", name="Santrifüj Kompresör", description="Santrifüj kompresör analizi", fields=common_fields + [
            CompressorFieldResponse(name="stages", label="Kademe Sayısı", type="number", required=False, default=1, min=1, max=5),
            CompressorFieldResponse(name="igv_position", label="IGV Pozisyonu", type="number", required=False, default=100, min=0, max=100, unit="%"),
        ]),
    ]

    return EquipmentTypeConfigResponse(equipment_type="compressor", subtypes=subtypes)


def _get_boiler_config() -> EquipmentTypeConfigResponse:
    """Boiler config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="fuel_flow_kg_h", label="Yakıt Debisi", type="number", required=True, default=100, min=1, max=50000, unit="kg/h"),
        CompressorFieldResponse(name="steam_flow_kg_h", label="Buhar Debisi", type="number", required=True, default=2000, min=1, max=100000, unit="kg/h"),
        CompressorFieldResponse(name="steam_pressure_bar", label="Buhar Basıncı", type="number", required=True, default=10, min=1, max=100, unit="bar"),
        CompressorFieldResponse(name="steam_temp_C", label="Buhar Sıcaklığı", type="number", required=False, min=50, max=600, unit="°C"),
        CompressorFieldResponse(name="feedwater_temp_C", label="Besleme Suyu Sıcaklığı", type="number", required=False, default=80, min=5, max=200, unit="°C"),
        CompressorFieldResponse(name="flue_gas_temp_C", label="Baca Gazı Sıcaklığı", type="number", required=False, default=180, min=50, max=500, unit="°C"),
        CompressorFieldResponse(name="fuel_type", label="Yakıt Tipi", type="select", required=False, default="natural_gas", options=[
            {"value": "natural_gas", "label": "Dogalgaz"},
            {"value": "fuel_oil", "label": "Fuel Oil"},
            {"value": "coal", "label": "Komur"},
            {"value": "biomass", "label": "Biyokutle"},
            {"value": "lpg", "label": "LPG"},
            {"value": "diesel", "label": "Dizel"},
        ]),
        CompressorFieldResponse(name="excess_air_pct", label="Fazla Hava", type="number", required=False, default=15, min=0, max=100, unit="%"),
        CompressorFieldResponse(name="blowdown_rate_pct", label="Blowdown Oranı", type="number", required=False, default=3, min=0, max=20, unit="%"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=6000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="fuel_price_eur_kg", label="Yakıt Fiyatı", type="number", required=False, default=0.50, min=0, max=10, unit="€/kg", hint="Dogalgaz icin tipik: 0.35-0.60 €/kg"),
        CompressorFieldResponse(name="equipment_cost_eur", label="Ekipman Maliyeti", type="number", required=False, min=0, max=50000000, unit="EUR", hint="Bos birakilirsa otomatik tahmin yapilir"),
    ]

    subtypes = []
    for st in ["steam_firetube", "steam_watertube", "hotwater", "condensing", "waste_heat", "electric", "biomass"]:
        names = {
            "steam_firetube": "Ateş Borulu Buhar",
            "steam_watertube": "Su Borulu Buhar",
            "hotwater": "Sıcak Su",
            "condensing": "Yoğuşmalı",
            "waste_heat": "Atık Isı / HRSG",
            "electric": "Elektrikli",
            "biomass": "Biyokütle",
        }
        subtypes.append(EquipmentSubtypeConfig(
            id=st, name=names[st], description=f"{names[st]} kazan exergy analizi", fields=common_fields,
        ))

    return EquipmentTypeConfigResponse(equipment_type="boiler", subtypes=subtypes)


def _get_chiller_config() -> EquipmentTypeConfigResponse:
    """Chiller config with field definitions."""
    vc_fields = [
        CompressorFieldResponse(name="cooling_capacity_kW", label="Soğutma Kapasitesi", type="number", required=True, default=350, min=1, max=10000, unit="kW"),
        CompressorFieldResponse(name="compressor_power_kW", label="Kompresör Gücü", type="number", required=True, default=70, min=1, max=5000, unit="kW"),
        CompressorFieldResponse(name="chw_supply_temp_C", label="Soğuk Su Çıkış", type="number", required=False, default=7, min=-10, max=25, unit="°C"),
        CompressorFieldResponse(name="chw_return_temp_C", label="Soğuk Su Dönüş", type="number", required=False, default=12, min=0, max=30, unit="°C"),
        CompressorFieldResponse(name="cw_supply_temp_C", label="Kondenser Suyu Giriş", type="number", required=False, default=30, min=10, max=50, unit="°C"),
        CompressorFieldResponse(name="cw_return_temp_C", label="Kondenser Suyu Çıkış", type="number", required=False, default=35, min=15, max=55, unit="°C"),
        CompressorFieldResponse(name="condenser_type", label="Kondenser Tipi", type="select", required=False, options=[
            {"value": "water", "label": "Su Sogutmali"},
            {"value": "air", "label": "Hava Sogutmali"},
        ]),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=4000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.12, min=0, max=1, unit="€/kWh"),
        CompressorFieldResponse(name="equipment_cost_eur", label="Ekipman Maliyeti", type="number", required=False, min=0, max=50000000, unit="EUR", hint="Bos birakilirsa otomatik tahmin yapilir"),
    ]

    abs_fields = [
        CompressorFieldResponse(name="cooling_capacity_kW", label="Soğutma Kapasitesi", type="number", required=True, min=1, max=10000, unit="kW"),
        CompressorFieldResponse(name="generator_heat_kW", label="Jeneratör Isısı", type="number", required=True, min=1, max=20000, unit="kW"),
        CompressorFieldResponse(name="generator_temp_C", label="Jeneratör Sıcaklığı", type="number", required=False, default=90, min=60, max=200, unit="°C"),
        CompressorFieldResponse(name="compressor_power_kW", label="Çözelti Pompası", type="number", required=False, default=0, min=0, max=100, unit="kW"),
        CompressorFieldResponse(name="chw_supply_temp_C", label="Soğuk Su Çıkış", type="number", required=False, default=7, min=-10, max=25, unit="°C"),
        CompressorFieldResponse(name="chw_return_temp_C", label="Soğuk Su Dönüş", type="number", required=False, default=12, min=0, max=30, unit="°C"),
        CompressorFieldResponse(name="cw_supply_temp_C", label="Kondenser Suyu Giriş", type="number", required=False, default=30, min=10, max=50, unit="°C"),
        CompressorFieldResponse(name="cw_return_temp_C", label="Kondenser Suyu Çıkış", type="number", required=False, default=35, min=15, max=55, unit="°C"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=4000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.12, min=0, max=1, unit="€/kWh"),
        CompressorFieldResponse(name="equipment_cost_eur", label="Ekipman Maliyeti", type="number", required=False, min=0, max=50000000, unit="EUR", hint="Bos birakilirsa otomatik tahmin yapilir"),
    ]

    subtypes = []
    vc_names = {
        "screw": "Vidalı", "centrifugal": "Santrifüj", "scroll": "Scroll",
        "reciprocating": "Pistonlu", "air_cooled": "Hava Soğutmalı", "water_cooled": "Su Soğutmalı",
    }
    for st_id, st_name in vc_names.items():
        subtypes.append(EquipmentSubtypeConfig(
            id=st_id, name=st_name, description=f"{st_name} chiller exergy analizi", fields=vc_fields,
        ))
    subtypes.append(EquipmentSubtypeConfig(
        id="absorption", name="Absorpsiyonlu", description="Absorpsiyonlu chiller exergy analizi", fields=abs_fields,
    ))

    return EquipmentTypeConfigResponse(equipment_type="chiller", subtypes=subtypes)


def _get_pump_config() -> EquipmentTypeConfigResponse:
    """Pump config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="motor_power_kW", label="Motor Gücü", type="number", required=True, default=15, min=0.1, max=5000, unit="kW"),
        CompressorFieldResponse(name="flow_rate_m3_h", label="Debi", type="number", required=True, default=50, min=0.1, max=50000, unit="m³/h"),
        CompressorFieldResponse(name="total_head_m", label="Toplam Basma Yüksekliği", type="number", required=True, default=40, min=1, max=1000, unit="m"),
        CompressorFieldResponse(name="fluid_density_kg_m3", label="Akışkan Yoğunluğu", type="number", required=False, default=1000, min=500, max=2000, unit="kg/m³"),
        CompressorFieldResponse(name="control_method", label="Kontrol Yöntemi", type="select", required=False, options=[
            {"value": "none", "label": "Kontrolsuz"},
            {"value": "throttle", "label": "Vana (Kisma)"},
            {"value": "vsd", "label": "VSD (Degisken Hiz)"},
            {"value": "bypass", "label": "Bypass"},
        ]),
        CompressorFieldResponse(name="throttle_loss_pct", label="Vana Kaybı", type="number", required=False, default=0, min=0, max=50, unit="%"),
        CompressorFieldResponse(name="has_vsd", label="VSD Var mı?", type="boolean", required=False, default=0),
        CompressorFieldResponse(name="motor_efficiency_pct", label="Motor Verimi", type="number", required=False, min=50, max=99, unit="%"),
        CompressorFieldResponse(name="pump_efficiency_pct", label="Pompa Verimi", type="number", required=False, default=75, min=30, max=95, unit="%"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=6000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.12, min=0, max=1, unit="€/kWh"),
        CompressorFieldResponse(name="equipment_cost_eur", label="Ekipman Maliyeti", type="number", required=False, min=0, max=50000000, unit="EUR", hint="Bos birakilirsa otomatik tahmin yapilir"),
    ]

    subtypes = []
    pump_names = {
        "centrifugal": "Santrifüj Pompa",
        "positive_displacement": "Pozitif Deplasman",
        "submersible": "Dalgıç Pompa",
        "vertical_turbine": "Dikey Türbin",
        "booster": "Hidrofor",
        "vacuum": "Vakum Pompası",
    }
    for st_id, st_name in pump_names.items():
        subtypes.append(EquipmentSubtypeConfig(
            id=st_id, name=st_name, description=f"{st_name} exergy analizi", fields=common_fields,
        ))

    return EquipmentTypeConfigResponse(equipment_type="pump", subtypes=subtypes)


def _get_heat_exchanger_config() -> EquipmentTypeConfigResponse:
    """Heat exchanger config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="hot_fluid", label="Sicak Akiskan", type="select", required=False, default="water", options=[
            {"value": "water", "label": "Su"},
            {"value": "steam", "label": "Buhar"},
            {"value": "air", "label": "Hava"},
            {"value": "flue_gas", "label": "Baca Gazi"},
            {"value": "thermal_oil", "label": "Termal Yag"},
        ]),
        CompressorFieldResponse(name="hot_inlet_temp_C", label="Sicak Giris", type="number", required=False, default=90, min=0, max=800, unit="C"),
        CompressorFieldResponse(name="hot_outlet_temp_C", label="Sicak Cikis", type="number", required=False, default=70, min=0, max=800, unit="C"),
        CompressorFieldResponse(name="hot_mass_flow_kg_s", label="Sicak Debi", type="number", required=True, default=2.0, min=0.01, max=500, unit="kg/s"),
        CompressorFieldResponse(name="cold_fluid", label="Soguk Akiskan", type="select", required=False, default="water", options=[
            {"value": "water", "label": "Su"},
            {"value": "air", "label": "Hava"},
            {"value": "glycol_30", "label": "Glikol %30"},
        ]),
        CompressorFieldResponse(name="cold_inlet_temp_C", label="Soguk Giris", type="number", required=False, default=20, min=-20, max=500, unit="C"),
        CompressorFieldResponse(name="cold_outlet_temp_C", label="Soguk Cikis", type="number", required=False, default=50, min=-20, max=500, unit="C"),
        CompressorFieldResponse(name="cold_mass_flow_kg_s", label="Soguk Debi", type="number", required=True, default=1.5, min=0.01, max=500, unit="kg/s"),
        CompressorFieldResponse(name="operating_hours", label="Yillik Calisma Saati", type="number", required=False, default=6000, min=0, max=8760, unit="saat/yil"),
        CompressorFieldResponse(name="fuel_price_eur_kwh", label="Yakit Fiyati", type="number", required=False, default=0.06, min=0, max=1, unit="EUR/kWh"),
    ]

    hx_names = {
        "shell_tube": "Govde-Boru",
        "plate": "Plakali",
        "air_cooled": "Hava Sogutmali",
        "double_pipe": "Cift Borulu",
        "spiral": "Spiral",
        "economizer": "Ekonomizer",
        "recuperator": "Rekuperator",
    }
    subtypes = [
        EquipmentSubtypeConfig(id=st_id, name=st_name, description=f"{st_name} isi esanjoru exergy analizi", fields=common_fields)
        for st_id, st_name in hx_names.items()
    ]

    return EquipmentTypeConfigResponse(equipment_type="heat_exchanger", subtypes=subtypes)


def _get_steam_turbine_config() -> EquipmentTypeConfigResponse:
    """Steam turbine config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="inlet_temp_C", label="Giris Sicakligi", type="number", required=True, default=400, min=100, max=650, unit="C"),
        CompressorFieldResponse(name="inlet_pressure_bar", label="Giris Basinci", type="number", required=True, default=40, min=1, max=200, unit="bar"),
        CompressorFieldResponse(name="mass_flow_kg_s", label="Buhar Debisi", type="number", required=True, default=5, min=0.1, max=500, unit="kg/s"),
        CompressorFieldResponse(name="outlet_pressure_bar", label="Cikis Basinci", type="number", required=True, default=2.0, min=0.01, max=100, unit="bar"),
        CompressorFieldResponse(name="isentropic_efficiency", label="Izentropik Verim", type="number", required=False, default=0.80, min=0.3, max=0.98),
        CompressorFieldResponse(name="is_chp", label="CHP Modu", type="boolean", required=False, default=0),
        CompressorFieldResponse(name="heat_recovery_fraction", label="Isi Geri Kazanim Orani", type="number", required=False, default=0.60, min=0, max=1.0),
        CompressorFieldResponse(name="operating_hours", label="Yillik Calisma Saati", type="number", required=False, default=7000, min=0, max=8760, unit="saat/yil"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyati", type="number", required=False, default=0.10, min=0, max=1, unit="EUR/kWh"),
    ]

    st_names = {
        "back_pressure": "Karsi Basincli",
        "condensing": "Yogusmali",
        "extraction": "Ara Cekisli",
        "orc": "ORC",
        "micro_turbine": "Mikro Turbin",
    }
    subtypes = [
        EquipmentSubtypeConfig(id=st_id, name=st_name, description=f"{st_name} buhar turbini exergy analizi", fields=common_fields)
        for st_id, st_name in st_names.items()
    ]

    return EquipmentTypeConfigResponse(equipment_type="steam_turbine", subtypes=subtypes)


def _get_dryer_config() -> EquipmentTypeConfigResponse:
    """Dryer config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="product_mass_flow_kg_h", label="Urun Debisi", type="number", required=True, default=1000, min=1, max=100000, unit="kg/h"),
        CompressorFieldResponse(name="moisture_in_pct", label="Giris Nem", type="number", required=True, default=60, min=1, max=99, unit="%"),
        CompressorFieldResponse(name="moisture_out_pct", label="Cikis Nem", type="number", required=True, default=10, min=0.1, max=90, unit="%"),
        CompressorFieldResponse(name="supply_temp_C", label="Besleme Sicakligi", type="number", required=False, default=200, min=50, max=800, unit="C"),
        CompressorFieldResponse(name="heat_source", label="Isi Kaynagi", type="select", required=False, default="natural_gas", options=[
            {"value": "natural_gas", "label": "Dogalgaz"},
            {"value": "steam", "label": "Buhar"},
            {"value": "electrical", "label": "Elektrik"},
            {"value": "hot_air", "label": "Sicak Hava"},
        ]),
        CompressorFieldResponse(name="air_outlet_temp_C", label="Hava Cikis Sicakligi", type="number", required=False, default=80, min=20, max=400, unit="C"),
        CompressorFieldResponse(name="operating_hours", label="Yillik Calisma Saati", type="number", required=False, default=5000, min=0, max=8760, unit="saat/yil"),
        CompressorFieldResponse(name="fuel_price_eur_kwh", label="Yakit Fiyati", type="number", required=False, default=0.05, min=0, max=1, unit="EUR/kWh"),
    ]

    dryer_names = {
        "convective": "Konvektif",
        "rotary": "Doner Tamburlu",
        "fluidized_bed": "Akiskan Yatak",
        "spray": "Spreyli",
        "belt": "Bantli",
        "heat_pump": "Isi Pompali",
        "infrared": "Kizilotesi",
        "drum": "Silindir",
    }
    subtypes = [
        EquipmentSubtypeConfig(id=st_id, name=st_name, description=f"{st_name} kurutucu exergy analizi", fields=common_fields)
        for st_id, st_name in dryer_names.items()
    ]

    return EquipmentTypeConfigResponse(equipment_type="dryer", subtypes=subtypes)


# ---------------------------------------------------------------------------
# Legacy compressor-types endpoint (backward compat)
# ---------------------------------------------------------------------------

@router.get("/compressor-types", response_model=CompressorTypesListResponse)
async def get_compressor_types():
    """Tüm kompresör tipleri ve form alanlarını döndürür."""
    config = _get_compressor_config()
    types = [
        CompressorTypeResponse(type=st.id, name=st.name, description=st.description, fields=st.fields)
        for st in config.subtypes
    ]
    return CompressorTypesListResponse(compressor_types=types)
