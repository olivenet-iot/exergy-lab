"""Request schemas for ExergyLab API."""

from typing import Literal, Optional
from pydantic import BaseModel, Field


class ScrewCompressorParams(BaseModel):
    power_kW: float = Field(..., gt=0, le=1000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(..., gt=0, le=200, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(..., gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Giriş sıcaklığı [°C]")
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300, description="Çıkış sıcaklığı [°C]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sıcaklığı [°C]")
    operating_hours: float = Field(4000, ge=0, le=8760, description="Yıllık çalışma saati")
    load_factor: float = Field(0.75, ge=0, le=1, description="Yük faktörü")
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1, description="Elektrik fiyatı [€/kWh]")


class PistonCompressorParams(BaseModel):
    power_kW: float = Field(..., gt=0, le=1000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(..., gt=0, le=200, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(..., gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300)
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    load_factor: float = Field(0.75, ge=0, le=1)
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1)
    stages: int = Field(1, ge=1, le=4, description="Kademe sayısı")
    cooling_type: Literal["air", "water"] = Field("air", description="Soğutma tipi")


class ScrollCompressorParams(BaseModel):
    power_kW: float = Field(..., gt=0, le=1000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(..., gt=0, le=200, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(..., gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300)
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    load_factor: float = Field(0.75, ge=0, le=1)
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1)
    oil_free: bool = Field(False, description="Yağsız kompresör mü?")


class CentrifugalCompressorParams(BaseModel):
    power_kW: float = Field(..., gt=0, le=5000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(..., gt=0, le=500, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(..., gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300)
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    load_factor: float = Field(0.75, ge=0, le=1)
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1)
    stages: int = Field(1, ge=1, le=5, description="Kademe sayısı")
    igv_position: float = Field(100.0, ge=0, le=100, description="IGV pozisyonu [%]")


class AnalysisRequest(BaseModel):
    equipment_type: Optional[str] = Field(None, description="Ekipman tipi")
    subtype: Optional[str] = Field(None, description="Ekipman alt tipi")
    compressor_type: Optional[Literal["screw", "piston", "scroll", "centrifugal"]] = Field(
        None, description="Kompresör tipi (geriye uyumluluk)"
    )
    parameters: dict = Field(..., description="Ekipman parametreleri")
