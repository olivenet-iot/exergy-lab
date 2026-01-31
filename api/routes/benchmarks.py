"""Benchmark routes for ExergyLab API."""

from fastapi import APIRouter, HTTPException

from api.schemas.responses import (
    BenchmarkResponse, EfficiencyRangeResponse, SPCRangeResponse,
)

router = APIRouter()

_BENCHMARKS = {
    "screw": {
        "efficiency": EfficiencyRangeResponse(
            poor="<30%", average="35-45%", good="45-55%", excellent=">60%",
        ),
        "spc": SPCRangeResponse(
            low="4.8-5.5 kW/(m³/min)",
            typical="5.5-6.5 kW/(m³/min)",
            high="6.5-8.5 kW/(m³/min)",
        ),
        "sectors": {
            "otomotiv": {"typical_efficiency": "40-50%", "typical_spc": "5.5-6.5"},
            "gida": {"typical_efficiency": "35-45%", "typical_spc": "6.0-7.0"},
            "tekstil": {"typical_efficiency": "30-40%", "typical_spc": "6.5-8.0"},
            "metal_isleme": {"typical_efficiency": "35-45%", "typical_spc": "5.5-7.0"},
            "ilac": {"typical_efficiency": "35-45%", "typical_spc": "6.0-7.5"},
            "genel_uretim": {"typical_efficiency": "35-45%", "typical_spc": "6.0-7.5"},
        },
    },
    "piston": {
        "efficiency": EfficiencyRangeResponse(
            poor="<25%", average="30-40%", good="40-50%", excellent=">55%",
        ),
        "spc": SPCRangeResponse(
            low="5.5-6.5 kW/(m³/min)",
            typical="6.0-7.5 kW/(m³/min)",
            high="7.5-10.0 kW/(m³/min)",
        ),
        "sectors": {
            "atolye": {"typical_efficiency": "25-35%", "typical_spc": "7.5-10.0"},
            "kucuk_endustri": {"typical_efficiency": "30-40%", "typical_spc": "6.5-8.5"},
            "orta_endustri": {"typical_efficiency": "35-45%", "typical_spc": "6.0-7.5"},
        },
    },
    "scroll": {
        "efficiency": EfficiencyRangeResponse(
            poor="<30%", average="35-45%", good="45-55%", excellent=">60%",
        ),
        "spc": SPCRangeResponse(
            low="5.0-6.0 kW/(m³/min)",
            typical="6.0-7.0 kW/(m³/min)",
            high="7.0-8.5 kW/(m³/min)",
        ),
        "sectors": {
            "laboratuvar": {"typical_efficiency": "35-45%", "typical_spc": "6.0-7.0"},
            "medikal": {"typical_efficiency": "35-45%", "typical_spc": "6.0-7.5"},
            "kucuk_uretim": {"typical_efficiency": "30-40%", "typical_spc": "6.5-8.0"},
        },
    },
    "centrifugal": {
        "efficiency": EfficiencyRangeResponse(
            poor="<35%", average="40-50%", good="50-60%", excellent=">65%",
        ),
        "spc": SPCRangeResponse(
            low="4.3-5.0 kW/(m³/min)",
            typical="5.0-5.8 kW/(m³/min)",
            high="5.8-6.5 kW/(m³/min)",
        ),
        "sectors": {
            "buyuk_endustri": {"typical_efficiency": "45-55%", "typical_spc": "5.0-6.0"},
            "otomotiv": {"typical_efficiency": "45-55%", "typical_spc": "4.8-5.5"},
            "petrokimya": {"typical_efficiency": "45-55%", "typical_spc": "4.5-5.5"},
        },
    },
}


@router.get("/benchmarks/{compressor_type}", response_model=BenchmarkResponse)
async def get_benchmarks(compressor_type: str):
    """Kompresör tipi için benchmark verilerini döndürür."""
    data = _BENCHMARKS.get(compressor_type)
    if not data:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown compressor type: {compressor_type}. Valid types: {list(_BENCHMARKS.keys())}",
        )

    return BenchmarkResponse(
        compressor_type=compressor_type,
        efficiency_ranges=data["efficiency"],
        spc_ranges=data["spc"],
        sector_averages=data["sectors"],
    )
