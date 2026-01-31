"""Solutions routes for ExergyLab API."""

from typing import Optional
from fastapi import APIRouter, HTTPException, Query

from engine.compressor import (
    CompressorInput, PistonCompressorInput,
    ScrollCompressorInput, CentrifugalCompressorInput,
    analyze_compressor, analyze_piston_compressor,
    analyze_scroll_compressor, analyze_centrifugal_compressor,
    get_compressor_recommendations,
)
from api.schemas.responses import SolutionsResponse, RecommendationResponse

router = APIRouter()

_VALID_TYPES = {"screw", "piston", "scroll", "centrifugal"}

# Default parameters per type for generating recommendations
_DEFAULT_PARAMS = {
    "screw": {"power_kW": 55, "flow_rate_m3_min": 9.0, "outlet_pressure_bar": 7.5},
    "piston": {"power_kW": 22, "flow_rate_m3_min": 3.0, "outlet_pressure_bar": 8.0},
    "scroll": {"power_kW": 11, "flow_rate_m3_min": 1.5, "outlet_pressure_bar": 8.0},
    "centrifugal": {"power_kW": 250, "flow_rate_m3_min": 45.0, "outlet_pressure_bar": 7.5},
}

_INPUT_CLASSES = {
    "screw": CompressorInput,
    "piston": PistonCompressorInput,
    "scroll": ScrollCompressorInput,
    "centrifugal": CentrifugalCompressorInput,
}

_ANALYZERS = {
    "screw": analyze_compressor,
    "piston": analyze_piston_compressor,
    "scroll": analyze_scroll_compressor,
    "centrifugal": analyze_centrifugal_compressor,
}


@router.get("/solutions/{compressor_type}", response_model=SolutionsResponse)
async def get_solutions(
    compressor_type: str,
    efficiency: Optional[float] = Query(None, ge=0, le=100, description="Mevcut exergy verimi [%]"),
    specific_power: Optional[float] = Query(None, ge=0, le=20, description="Spesifik güç [kW/(m³/min)]"),
    operating_hours: Optional[float] = Query(None, ge=0, le=8760, description="Yıllık çalışma saati"),
):
    """Kompresör tipi için filtrelenmiş çözüm önerileri döndürür."""
    if compressor_type not in _VALID_TYPES:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown compressor type: {compressor_type}. Valid types: {sorted(_VALID_TYPES)}",
        )

    defaults = _DEFAULT_PARAMS[compressor_type]
    input_cls = _INPUT_CLASSES[compressor_type]
    analyze_fn = _ANALYZERS[compressor_type]

    kwargs = dict(defaults)
    if operating_hours is not None:
        kwargs["operating_hours"] = operating_hours

    input_data = input_cls(**kwargs)
    result = analyze_fn(input_data)

    # Override efficiency-based benchmark if provided
    if efficiency is not None:
        from engine.compressor import _get_benchmark_comparison
        result.exergy_efficiency_pct = efficiency
        result.benchmark_comparison = _get_benchmark_comparison(efficiency, compressor_type)

    if specific_power is not None:
        result.specific_power_kW_m3min = specific_power

    recommendations = get_compressor_recommendations(result, input_data)

    # Sort by priority
    priority_order = {"high": 0, "medium": 1, "low": 2}
    recommendations.sort(key=lambda r: priority_order.get(r["priority"], 3))

    return SolutionsResponse(
        compressor_type=compressor_type,
        recommendations=[RecommendationResponse(**r) for r in recommendations],
    )
