"""Factory analysis schemas for ExergyLab API."""

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class EquipmentTypeEnum(str, Enum):
    compressor = "compressor"
    boiler = "boiler"
    chiller = "chiller"
    pump = "pump"
    heat_exchanger = "heat_exchanger"
    steam_turbine = "steam_turbine"
    dryer = "dryer"


class EquipmentItemRequest(BaseModel):
    type: EquipmentTypeEnum = Field(..., description="Ekipman tipi")
    subtype: str = Field(..., description="Ekipman alt tipi (screw, steam_firetube, etc.)")
    name: str = Field(..., description="Ekipman adi")
    parameters: dict = Field(..., description="Ekipman parametreleri")


class CreateFactoryProjectRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Proje adi")
    sector: Optional[str] = Field(None, description="Sektor (textile, food, chemical, metal, cement, paper, automotive)")
    description: Optional[str] = Field(None, description="Proje aciklamasi")


class AddEquipmentRequest(BaseModel):
    type: EquipmentTypeEnum = Field(..., description="Ekipman tipi")
    subtype: str = Field(..., description="Ekipman alt tipi")
    name: str = Field(..., description="Ekipman adi")
    parameters: dict = Field(..., description="Ekipman parametreleri")


class EquipmentItemResponse(BaseModel):
    id: str
    type: str
    subtype: str
    name: str
    parameters: dict
    analysis_result: Optional[dict] = None


class FactoryProjectResponse(BaseModel):
    id: str
    name: str
    sector: Optional[str] = None
    description: Optional[str] = None
    equipment: List[EquipmentItemResponse] = []
    created_at: str
    equipment_count: int = 0


class PinchAnalysisRequest(BaseModel):
    delta_T_min_C: float = Field(default=10.0, ge=1.0, le=50.0, description="Minimum sicaklik yaklasmasi [°C]")
    fuel_price_eur_kwh: float = Field(default=0.08, ge=0.01, le=1.0, description="Yakit fiyati [EUR/kWh]")
    operating_hours: int = Field(default=8000, ge=1000, le=8760, description="Yillik calisma saati")
    include_pumps: bool = Field(default=False, description="Pompa akislarini dahil et")


class FactoryAnalysisResponse(BaseModel):
    success: bool
    project_id: str
    equipment_results: List[dict]
    aggregates: dict
    hotspots: List[dict]
    integration_opportunities: List[dict]
    sankey: dict
    pinch_analysis: Optional[dict] = None
    advanced_exergy: Optional[dict] = None
    entropy_generation: Optional[dict] = None
    thermoeconomic_optimization: Optional[dict] = None
    energy_management: Optional[dict] = None
