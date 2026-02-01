"""Analysis routes for ExergyLab API."""

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from engine.compressor import (
    CompressorInput, PistonCompressorInput,
    ScrollCompressorInput, CentrifugalCompressorInput,
    analyze_compressor, analyze_piston_compressor,
    analyze_scroll_compressor, analyze_centrifugal_compressor,
)
from engine.sankey import generate_sankey_data
from api.schemas.requests import (
    AnalysisRequest, ScrewCompressorParams,
    PistonCompressorParams, ScrollCompressorParams,
    CentrifugalCompressorParams,
)
from api.schemas.responses import (
    AnalysisResponse, MetricsResponse, HeatRecoveryResponse,
    BenchmarkDetailResponse, SankeyResponse,
    CompressorTypesListResponse, CompressorTypeResponse, CompressorFieldResponse,
)
from api.services.equipment_registry import (
    get_equipment_types,
    get_equipment_subtypes,
    is_valid_equipment,
    is_engine_ready,
)

router = APIRouter()


# Param validators per compressor subtype
_PARAM_VALIDATORS = {
    "screw": ScrewCompressorParams,
    "piston": PistonCompressorParams,
    "scroll": ScrollCompressorParams,
    "centrifugal": CentrifugalCompressorParams,
}

# Engine dispatch for compressor subtypes
_ANALYZERS = {
    "screw": (CompressorInput, analyze_compressor),
    "piston": (PistonCompressorInput, analyze_piston_compressor),
    "scroll": (ScrollCompressorInput, analyze_scroll_compressor),
    "centrifugal": (CentrifugalCompressorInput, analyze_centrifugal_compressor),
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
        # Old format: compressor_type -> equipment_type=compressor, subtype=compressor_type
        equipment_type = "compressor"
        comp_type = request.compressor_type
    elif request.equipment_type:
        # New format
        equipment_type = request.equipment_type
        comp_type = request.subtype
        if not is_engine_ready(equipment_type):
            raise HTTPException(
                status_code=501,
                detail="Bu ekipman tipi henuz desteklenmiyor",
            )
    else:
        raise HTTPException(status_code=422, detail="compressor_type or equipment_type is required")

    # Validate parameters via Pydantic model
    validator_cls = _PARAM_VALIDATORS.get(comp_type)
    if not validator_cls:
        raise HTTPException(status_code=422, detail=f"Unknown compressor type: {comp_type}")

    try:
        validated = validator_cls(**request.parameters)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    # Build engine input dataclass
    input_cls, analyze_fn = _ANALYZERS[comp_type]
    params = validated.model_dump(exclude_none=False)

    # Map to engine input kwargs
    engine_kwargs = {}
    for key, val in params.items():
        if val is not None:
            engine_kwargs[key] = val
        elif key in ("inlet_temp_C", "outlet_temp_C", "ambient_temp_C"):
            # Let the engine dataclass handle defaults
            pass
        else:
            engine_kwargs[key] = val

    input_data = input_cls(**engine_kwargs)
    result = analyze_fn(input_data)

    # Build API response
    api_dict = result.to_api_dict(comp_type)
    sankey_data = generate_sankey_data(result, comp_type)

    return AnalysisResponse(
        compressor_type=comp_type,
        metrics=MetricsResponse(
            exergy_input_kW=api_dict["exergy_input_kW"],
            exergy_output_kW=api_dict["exergy_output_kW"],
            exergy_destroyed_kW=api_dict["exergy_destroyed_kW"],
            exergy_efficiency_pct=api_dict["exergy_efficiency_pct"],
            mass_flow_kg_s=api_dict["mass_flow_kg_s"],
            specific_power_kW_m3min=api_dict["specific_power_kW_m3min"],
        ),
        heat_recovery=HeatRecoveryResponse(
            heat_recovery_potential_kW=api_dict["heat_recovery_potential_kW"],
            heat_recovery_savings_eur_year=api_dict["heat_recovery_savings_eur_year"],
            annual_loss_kWh=api_dict["annual_loss_kWh"],
            annual_loss_EUR=api_dict["annual_loss_EUR"],
        ),
        benchmark=BenchmarkDetailResponse(
            benchmark_comparison=api_dict["benchmark_comparison"],
            benchmark_percentile=api_dict["benchmark_percentile"],
            comparison_text=api_dict["comparison_text"],
        ),
        sankey=SankeyResponse(**sankey_data),
    )


@router.get("/compressor-types", response_model=CompressorTypesListResponse)
async def get_compressor_types():
    """Tüm kompresör tipleri ve form alanlarını döndürür."""
    common_fields = [
        CompressorFieldResponse(
            name="power_kW", label="Elektrik Gücü", type="number",
            required=True, min=0.1, max=5000, unit="kW",
        ),
        CompressorFieldResponse(
            name="flow_rate_m3_min", label="Hava Debisi", type="number",
            required=True, min=0.1, max=500, unit="m³/min",
        ),
        CompressorFieldResponse(
            name="outlet_pressure_bar", label="Çıkış Basıncı", type="number",
            required=True, min=1, max=50, unit="bar",
        ),
        CompressorFieldResponse(
            name="inlet_temp_C", label="Giriş Sıcaklığı", type="number",
            required=False, default=25.0, min=-20, max=60, unit="°C",
        ),
        CompressorFieldResponse(
            name="outlet_temp_C", label="Çıkış Sıcaklığı", type="number",
            required=False, min=20, max=300, unit="°C",
        ),
        CompressorFieldResponse(
            name="ambient_temp_C", label="Ortam Sıcaklığı", type="number",
            required=False, default=25.0, min=-20, max=60, unit="°C",
        ),
        CompressorFieldResponse(
            name="operating_hours", label="Yıllık Çalışma Saati", type="number",
            required=False, default=4000, min=0, max=8760, unit="saat/yıl",
        ),
        CompressorFieldResponse(
            name="load_factor", label="Yük Faktörü", type="number",
            required=False, default=0.75, min=0, max=1,
        ),
        CompressorFieldResponse(
            name="electricity_price_eur_kwh", label="Elektrik Fiyatı", type="number",
            required=False, default=0.10, min=0, max=1, unit="€/kWh",
        ),
    ]

    types = [
        CompressorTypeResponse(
            type="screw",
            name="Vidalı Kompresör",
            description="Endüstriyel vidalı (screw) kompresör analizi",
            fields=common_fields,
        ),
        CompressorTypeResponse(
            type="piston",
            name="Pistonlu Kompresör",
            description="Pistonlu kompresör analizi (tek ve çok kademeli)",
            fields=common_fields + [
                CompressorFieldResponse(
                    name="stages", label="Kademe Sayısı", type="number",
                    required=False, default=1, min=1, max=4,
                ),
                CompressorFieldResponse(
                    name="cooling_type", label="Soğutma Tipi", type="select",
                    required=False, options=["air", "water"],
                ),
            ],
        ),
        CompressorTypeResponse(
            type="scroll",
            name="Scroll Kompresör",
            description="Scroll kompresör analizi",
            fields=common_fields + [
                CompressorFieldResponse(
                    name="oil_free", label="Yağsız", type="boolean",
                    required=False, default=0,
                ),
            ],
        ),
        CompressorTypeResponse(
            type="centrifugal",
            name="Santrifüj Kompresör",
            description="Santrifüj kompresör analizi (tek ve çok kademeli)",
            fields=common_fields + [
                CompressorFieldResponse(
                    name="stages", label="Kademe Sayısı", type="number",
                    required=False, default=1, min=1, max=5,
                ),
                CompressorFieldResponse(
                    name="igv_position", label="IGV Pozisyonu", type="number",
                    required=False, default=100, min=0, max=100, unit="%",
                ),
            ],
        ),
    ]

    return CompressorTypesListResponse(compressor_types=types)
