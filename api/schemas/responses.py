"""Response schemas for ExergyLab API."""

from typing import List, Optional
from pydantic import BaseModel


class MetricsResponse(BaseModel):
    exergy_input_kW: float
    exergy_output_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_pct: float
    mass_flow_kg_s: Optional[float] = None
    specific_power_kW_m3min: Optional[float] = None


class HeatRecoveryResponse(BaseModel):
    heat_recovery_potential_kW: Optional[float] = None
    heat_recovery_savings_eur_year: Optional[float] = None
    annual_loss_kWh: Optional[float] = None
    annual_loss_EUR: Optional[float] = None


class BenchmarkDetailResponse(BaseModel):
    benchmark_comparison: Optional[str] = None
    benchmark_percentile: Optional[int] = None
    comparison_text: Optional[str] = None


class SankeyNodeResponse(BaseModel):
    id: int
    name: str
    name_en: str


class SankeyLinkResponse(BaseModel):
    source: int
    target: int
    value: float
    label: str


class SankeySummaryResponse(BaseModel):
    total_input_kW: float
    useful_output_kW: float
    recoverable_heat_kW: float
    irreversibility_kW: float
    efficiency_pct: float


class SankeyResponse(BaseModel):
    nodes: List[SankeyNodeResponse]
    links: List[SankeyLinkResponse]
    summary: SankeySummaryResponse


class AnalysisResponse(BaseModel):
    compressor_type: str
    metrics: MetricsResponse
    heat_recovery: HeatRecoveryResponse
    benchmark: BenchmarkDetailResponse
    sankey: SankeyResponse


class RecommendationResponse(BaseModel):
    type: str
    title: str
    description: str
    investment_eur: float
    savings_eur_year: float
    payback_years: float
    priority: str


class SolutionsResponse(BaseModel):
    compressor_type: str
    recommendations: List[RecommendationResponse]


# --- Compressor types endpoint ---

class CompressorFieldResponse(BaseModel):
    name: str
    label: str
    type: str
    required: bool
    default: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    unit: Optional[str] = None
    options: Optional[List[str]] = None


class CompressorTypeResponse(BaseModel):
    type: str
    name: str
    description: str
    fields: List[CompressorFieldResponse]


class CompressorTypesListResponse(BaseModel):
    compressor_types: List[CompressorTypeResponse]


# --- Benchmarks endpoint ---

class EfficiencyRangeResponse(BaseModel):
    poor: str
    average: str
    good: str
    excellent: str


class SPCRangeResponse(BaseModel):
    low: str
    typical: str
    high: str


class BenchmarkResponse(BaseModel):
    compressor_type: str
    efficiency_ranges: EfficiencyRangeResponse
    spc_ranges: SPCRangeResponse
    sector_averages: dict
