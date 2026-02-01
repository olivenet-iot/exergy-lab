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
from engine.sankey import generate_sankey_data
from api.schemas.requests import (
    AnalysisRequest, ScrewCompressorParams,
    PistonCompressorParams, ScrollCompressorParams,
    CentrifugalCompressorParams,
    BoilerParams, VaporCompressionChillerParams,
    AbsorptionChillerParams, PumpParams,
)
from api.schemas.responses import (
    AnalysisResponse, MetricsResponse, HeatRecoveryResponse,
    BenchmarkDetailResponse, SankeyResponse,
    CompressorTypesListResponse, CompressorTypeResponse, CompressorFieldResponse,
    EquipmentTypeConfigResponse, EquipmentSubtypeConfig,
)
from api.services.equipment_registry import (
    get_equipment_types,
    get_equipment_subtypes,
    is_valid_equipment,
    is_engine_ready,
)

router = APIRouter()


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

    # Dispatch based on equipment type
    if equipment_type == "compressor":
        return _analyze_compressor(subtype, request.parameters)
    elif equipment_type == "boiler":
        return _analyze_boiler(subtype, request.parameters)
    elif equipment_type == "chiller":
        return _analyze_chiller(subtype, request.parameters)
    elif equipment_type == "pump":
        return _analyze_pump(subtype, request.parameters)
    else:
        raise HTTPException(status_code=422, detail=f"Unsupported equipment type: {equipment_type}")


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

    return AnalysisResponse(
        compressor_type=comp_type,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            mass_flow_kg_s=api_dict.get("mass_flow_kg_s"),
            specific_power_kW_m3min=api_dict.get("specific_power_kW_m3min"),
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
    else:
        raise HTTPException(status_code=404, detail=f"No config for: {equipment_type}")


def _get_compressor_config() -> EquipmentTypeConfigResponse:
    """Compressor config with field definitions."""
    common_fields = [
        CompressorFieldResponse(name="power_kW", label="Elektrik Gücü", type="number", required=True, min=0.1, max=5000, unit="kW"),
        CompressorFieldResponse(name="flow_rate_m3_min", label="Hava Debisi", type="number", required=True, min=0.1, max=500, unit="m³/min"),
        CompressorFieldResponse(name="outlet_pressure_bar", label="Çıkış Basıncı", type="number", required=True, min=1, max=50, unit="bar"),
        CompressorFieldResponse(name="inlet_temp_C", label="Giriş Sıcaklığı", type="number", required=False, default=25.0, min=-20, max=60, unit="°C"),
        CompressorFieldResponse(name="outlet_temp_C", label="Çıkış Sıcaklığı", type="number", required=False, min=20, max=300, unit="°C"),
        CompressorFieldResponse(name="ambient_temp_C", label="Ortam Sıcaklığı", type="number", required=False, default=25.0, min=-20, max=60, unit="°C"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=4000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="load_factor", label="Yük Faktörü", type="number", required=False, default=0.75, min=0, max=1),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.10, min=0, max=1, unit="€/kWh"),
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
        CompressorFieldResponse(name="fuel_flow_kg_h", label="Yakıt Debisi", type="number", required=True, min=1, max=50000, unit="kg/h"),
        CompressorFieldResponse(name="steam_flow_kg_h", label="Buhar Debisi", type="number", required=True, min=1, max=100000, unit="kg/h"),
        CompressorFieldResponse(name="steam_pressure_bar", label="Buhar Basıncı", type="number", required=True, min=1, max=100, unit="bar"),
        CompressorFieldResponse(name="steam_temp_C", label="Buhar Sıcaklığı", type="number", required=False, min=50, max=600, unit="°C"),
        CompressorFieldResponse(name="feedwater_temp_C", label="Besleme Suyu Sıcaklığı", type="number", required=False, default=80, min=5, max=200, unit="°C"),
        CompressorFieldResponse(name="flue_gas_temp_C", label="Baca Gazı Sıcaklığı", type="number", required=False, default=180, min=50, max=500, unit="°C"),
        CompressorFieldResponse(name="fuel_type", label="Yakıt Tipi", type="select", required=False, options=["natural_gas", "fuel_oil", "coal", "biomass", "lpg", "diesel"]),
        CompressorFieldResponse(name="excess_air_pct", label="Fazla Hava", type="number", required=False, default=15, min=0, max=100, unit="%"),
        CompressorFieldResponse(name="blowdown_rate_pct", label="Blowdown Oranı", type="number", required=False, default=3, min=0, max=20, unit="%"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=6000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="fuel_price_eur_kg", label="Yakıt Fiyatı", type="number", required=False, default=0.50, min=0, max=10, unit="€/kg"),
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
        CompressorFieldResponse(name="cooling_capacity_kW", label="Soğutma Kapasitesi", type="number", required=True, min=1, max=10000, unit="kW"),
        CompressorFieldResponse(name="compressor_power_kW", label="Kompresör Gücü", type="number", required=True, min=1, max=5000, unit="kW"),
        CompressorFieldResponse(name="chw_supply_temp_C", label="Soğuk Su Çıkış", type="number", required=False, default=7, min=-10, max=25, unit="°C"),
        CompressorFieldResponse(name="chw_return_temp_C", label="Soğuk Su Dönüş", type="number", required=False, default=12, min=0, max=30, unit="°C"),
        CompressorFieldResponse(name="cw_supply_temp_C", label="Kondenser Suyu Giriş", type="number", required=False, default=30, min=10, max=50, unit="°C"),
        CompressorFieldResponse(name="cw_return_temp_C", label="Kondenser Suyu Çıkış", type="number", required=False, default=35, min=15, max=55, unit="°C"),
        CompressorFieldResponse(name="condenser_type", label="Kondenser Tipi", type="select", required=False, options=["water", "air"]),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=4000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.12, min=0, max=1, unit="€/kWh"),
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
        CompressorFieldResponse(name="motor_power_kW", label="Motor Gücü", type="number", required=True, min=0.1, max=5000, unit="kW"),
        CompressorFieldResponse(name="flow_rate_m3_h", label="Debi", type="number", required=True, min=0.1, max=50000, unit="m³/h"),
        CompressorFieldResponse(name="total_head_m", label="Toplam Basma Yüksekliği", type="number", required=True, min=1, max=1000, unit="m"),
        CompressorFieldResponse(name="fluid_density_kg_m3", label="Akışkan Yoğunluğu", type="number", required=False, default=1000, min=500, max=2000, unit="kg/m³"),
        CompressorFieldResponse(name="control_method", label="Kontrol Yöntemi", type="select", required=False, options=["none", "throttle", "vsd", "bypass"]),
        CompressorFieldResponse(name="throttle_loss_pct", label="Vana Kaybı", type="number", required=False, default=0, min=0, max=50, unit="%"),
        CompressorFieldResponse(name="has_vsd", label="VSD Var mı?", type="boolean", required=False, default=0),
        CompressorFieldResponse(name="motor_efficiency_pct", label="Motor Verimi", type="number", required=False, min=50, max=99, unit="%"),
        CompressorFieldResponse(name="pump_efficiency_pct", label="Pompa Verimi", type="number", required=False, min=30, max=95, unit="%"),
        CompressorFieldResponse(name="operating_hours", label="Yıllık Çalışma Saati", type="number", required=False, default=6000, min=0, max=8760, unit="saat/yıl"),
        CompressorFieldResponse(name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number", required=False, default=0.12, min=0, max=1, unit="€/kWh"),
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
