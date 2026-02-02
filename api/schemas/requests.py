"""Request schemas for ExergyLab API."""

from typing import Literal, Optional
from pydantic import BaseModel, Field


class ScrewCompressorParams(BaseModel):
    power_kW: float = Field(37.0, gt=0, le=1000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(6.2, gt=0, le=200, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(7.5, gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Giriş sıcaklığı [°C]")
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300, description="Çıkış sıcaklığı [°C]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sıcaklığı [°C]")
    operating_hours: float = Field(4000, ge=0, le=8760, description="Yıllık çalışma saati")
    load_factor: float = Field(0.75, ge=0, le=1, description="Yük faktörü")
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1, description="Elektrik fiyatı [€/kWh]")


class PistonCompressorParams(BaseModel):
    power_kW: float = Field(37.0, gt=0, le=1000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(6.2, gt=0, le=200, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(7.5, gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300)
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    load_factor: float = Field(0.75, ge=0, le=1)
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1)
    stages: int = Field(1, ge=1, le=4, description="Kademe sayısı")
    cooling_type: Literal["air", "water"] = Field("air", description="Soğutma tipi")


class ScrollCompressorParams(BaseModel):
    power_kW: float = Field(37.0, gt=0, le=1000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(6.2, gt=0, le=200, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(7.5, gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300)
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    load_factor: float = Field(0.75, ge=0, le=1)
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1)
    oil_free: bool = Field(False, description="Yağsız kompresör mü?")


class CentrifugalCompressorParams(BaseModel):
    power_kW: float = Field(37.0, gt=0, le=5000, description="Elektrik gücü [kW]")
    flow_rate_m3_min: float = Field(6.2, gt=0, le=500, description="Hava debisi [m³/min]")
    outlet_pressure_bar: float = Field(7.5, gt=0, le=50, description="Çıkış basıncı [bar]")
    inlet_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    outlet_temp_C: Optional[float] = Field(None, ge=20, le=300)
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    load_factor: float = Field(0.75, ge=0, le=1)
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1)
    stages: int = Field(1, ge=1, le=5, description="Kademe sayısı")
    igv_position: float = Field(100.0, ge=0, le=100, description="IGV pozisyonu [%]")


# --- Boiler params ---

class BoilerParams(BaseModel):
    fuel_flow_kg_h: float = Field(100.0, gt=0, le=50000, description="Yakıt debisi [kg/h]")
    steam_flow_kg_h: float = Field(2000.0, gt=0, le=100000, description="Buhar/su debisi [kg/h]")
    steam_pressure_bar: float = Field(10.0, gt=0, le=100, description="Buhar basıncı [bar]")
    steam_temp_C: Optional[float] = Field(None, ge=50, le=600, description="Buhar sıcaklığı [°C]")
    feedwater_temp_C: float = Field(80.0, ge=5, le=200, description="Besleme suyu sıcaklığı [°C]")
    flue_gas_temp_C: float = Field(180.0, ge=50, le=500, description="Baca gazı sıcaklığı [°C]")
    fuel_type: Literal["natural_gas", "fuel_oil", "coal", "biomass", "lpg", "diesel"] = Field(
        "natural_gas", description="Yakıt tipi"
    )
    fuel_lhv_kj_kg: Optional[float] = Field(None, gt=0, le=60000, description="Yakıt alt ısıl değeri [kJ/kg]")
    excess_air_pct: float = Field(15.0, ge=0, le=100, description="Fazla hava [%]")
    blowdown_rate_pct: float = Field(3.0, ge=0, le=20, description="Blowdown oranı [%]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sıcaklığı [°C]")
    operating_hours: float = Field(6000, ge=0, le=8760, description="Yıllık çalışma saati")
    fuel_price_eur_kg: float = Field(0.50, ge=0, le=10, description="Yakıt fiyatı [€/kg]")


# --- Chiller params (vapor compression) ---

class VaporCompressionChillerParams(BaseModel):
    cooling_capacity_kW: float = Field(350.0, gt=0, le=10000, description="Soğutma kapasitesi [kW]")
    compressor_power_kW: float = Field(70.0, gt=0, le=5000, description="Kompresör gücü [kW]")
    chw_supply_temp_C: float = Field(7.0, ge=-10, le=25, description="Soğuk su çıkış sıcaklığı [°C]")
    chw_return_temp_C: float = Field(12.0, ge=0, le=30, description="Soğuk su dönüş sıcaklığı [°C]")
    cw_supply_temp_C: float = Field(30.0, ge=10, le=50, description="Kondenser suyu giriş sıcaklığı [°C]")
    cw_return_temp_C: float = Field(35.0, ge=15, le=55, description="Kondenser suyu çıkış sıcaklığı [°C]")
    condenser_type: Literal["water", "air"] = Field("water", description="Kondenser tipi")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sıcaklığı [°C]")
    operating_hours: float = Field(4000, ge=0, le=8760, description="Yıllık çalışma saati")
    electricity_price_eur_kwh: float = Field(0.12, ge=0, le=1, description="Elektrik fiyatı [€/kWh]")


class AbsorptionChillerParams(BaseModel):
    cooling_capacity_kW: float = Field(350.0, gt=0, le=10000, description="Soğutma kapasitesi [kW]")
    generator_heat_kW: float = Field(500.0, gt=0, le=20000, description="Jeneratör ısısı [kW]")
    generator_temp_C: float = Field(90.0, ge=60, le=200, description="Jeneratör sıcaklığı [°C]")
    compressor_power_kW: float = Field(0.0, ge=0, le=100, description="Çözelti pompası gücü [kW]")
    chw_supply_temp_C: float = Field(7.0, ge=-10, le=25, description="Soğuk su çıkış sıcaklığı [°C]")
    chw_return_temp_C: float = Field(12.0, ge=0, le=30, description="Soğuk su dönüş sıcaklığı [°C]")
    cw_supply_temp_C: float = Field(30.0, ge=10, le=50, description="Kondenser suyu giriş sıcaklığı [°C]")
    cw_return_temp_C: float = Field(35.0, ge=15, le=55, description="Kondenser suyu çıkış sıcaklığı [°C]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60)
    operating_hours: float = Field(4000, ge=0, le=8760)
    electricity_price_eur_kwh: float = Field(0.12, ge=0, le=1)


# --- Pump params ---

class PumpParams(BaseModel):
    motor_power_kW: float = Field(15.0, gt=0, le=5000, description="Motor gücü [kW]")
    flow_rate_m3_h: float = Field(50.0, gt=0, le=50000, description="Debi [m³/h]")
    total_head_m: float = Field(40.0, gt=0, le=1000, description="Toplam basma yüksekliği [m]")
    fluid_density_kg_m3: float = Field(1000.0, ge=500, le=2000, description="Akışkan yoğunluğu [kg/m³]")
    control_method: Literal["none", "throttle", "vsd", "bypass"] = Field("none", description="Kontrol yöntemi")
    throttle_loss_pct: float = Field(0.0, ge=0, le=50, description="Vana kaybı [%]")
    has_vsd: bool = Field(False, description="VSD var mı?")
    motor_efficiency_pct: Optional[float] = Field(None, ge=50, le=99, description="Motor verimi [%]")
    pump_efficiency_pct: Optional[float] = Field(None, ge=30, le=95, description="Pompa verimi [%]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sıcaklığı [°C]")
    operating_hours: float = Field(6000, ge=0, le=8760, description="Yıllık çalışma saati")
    electricity_price_eur_kwh: float = Field(0.12, ge=0, le=1, description="Elektrik fiyatı [€/kWh]")


# --- Heat Exchanger params ---

class HeatExchangerParams(BaseModel):
    hot_fluid: Literal["water", "steam", "air", "flue_gas", "thermal_oil", "glycol_30", "glycol_50"] = Field(
        "water", description="Sicak taraf akiskan"
    )
    hot_inlet_temp_C: float = Field(90.0, ge=0, le=800, description="Sicak giris sicakligi [C]")
    hot_outlet_temp_C: float = Field(70.0, ge=0, le=800, description="Sicak cikis sicakligi [C]")
    hot_mass_flow_kg_s: float = Field(2.0, gt=0, le=500, description="Sicak taraf kutle debisi [kg/s]")
    hot_pressure_drop_kPa: float = Field(10.0, ge=0, le=500, description="Sicak taraf basinc dususu [kPa]")
    cold_fluid: Literal["water", "steam", "air", "flue_gas", "thermal_oil", "glycol_30", "glycol_50"] = Field(
        "water", description="Soguk taraf akiskan"
    )
    cold_inlet_temp_C: float = Field(20.0, ge=-20, le=500, description="Soguk giris sicakligi [C]")
    cold_outlet_temp_C: float = Field(50.0, ge=-20, le=500, description="Soguk cikis sicakligi [C]")
    cold_mass_flow_kg_s: float = Field(1.5, gt=0, le=500, description="Soguk taraf kutle debisi [kg/s]")
    cold_pressure_drop_kPa: float = Field(15.0, ge=0, le=500, description="Soguk taraf basinc dususu [kPa]")
    heat_duty_kW: Optional[float] = Field(None, gt=0, le=100000, description="Isi gorev gucu [kW]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sicakligi [C]")
    operating_hours: float = Field(6000, ge=0, le=8760, description="Yillik calisma saati")
    fuel_price_eur_kwh: float = Field(0.06, ge=0, le=1, description="Yakit fiyati [EUR/kWh]")
    design_heat_duty_kW: Optional[float] = Field(None, gt=0, le=100000, description="Tasarim isi gucu [kW]")


# --- Steam Turbine params ---

class SteamTurbineParams(BaseModel):
    inlet_temp_C: float = Field(400.0, ge=100, le=650, description="Giris buhar sicakligi [C]")
    inlet_pressure_bar: float = Field(40.0, gt=0, le=200, description="Giris basinci [bar]")
    mass_flow_kg_s: float = Field(5.0, gt=0, le=500, description="Buhar kutle debisi [kg/s]")
    outlet_pressure_bar: float = Field(0.1, gt=0, le=100, description="Cikis basinci [bar]")
    outlet_temp_C: Optional[float] = Field(None, ge=0, le=600, description="Cikis sicakligi [C]")
    isentropic_efficiency: float = Field(0.80, ge=0.3, le=0.98, description="Izentropik verim")
    mechanical_efficiency: float = Field(0.98, ge=0.80, le=1.0, description="Mekanik verim")
    generator_efficiency: float = Field(0.97, ge=0.80, le=1.0, description="Jenerator verimi")
    is_chp: bool = Field(False, description="CHP modu")
    heat_recovery_temp_C: Optional[float] = Field(None, ge=50, le=400, description="Isi geri kazanim sicakligi [C]")
    heat_recovery_fraction: float = Field(0.60, ge=0, le=1.0, description="Isi geri kazanim orani")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sicakligi [C]")
    operating_hours: float = Field(7000, ge=0, le=8760, description="Yillik calisma saati")
    electricity_price_eur_kwh: float = Field(0.10, ge=0, le=1, description="Elektrik fiyati [EUR/kWh]")
    fuel_price_eur_kwh: float = Field(0.04, ge=0, le=1, description="Yakit fiyati [EUR/kWh]")


# --- Dryer params ---

class DryerParams(BaseModel):
    product_mass_flow_kg_h: float = Field(1000.0, gt=0, le=100000, description="Urun debisi [kg/h]")
    moisture_in_pct: float = Field(60.0, ge=1, le=99, description="Giris nem orani [%]")
    moisture_out_pct: float = Field(10.0, ge=0.1, le=90, description="Cikis nem orani [%]")
    product_inlet_temp_C: float = Field(25.0, ge=-10, le=200, description="Urun giris sicakligi [C]")
    product_outlet_temp_C: float = Field(60.0, ge=10, le=300, description="Urun cikis sicakligi [C]")
    heat_source: Literal["natural_gas", "steam", "electrical", "hot_air"] = Field(
        "natural_gas", description="Isi kaynagi"
    )
    supply_temp_C: float = Field(200.0, ge=50, le=800, description="Besleme sicakligi [C]")
    heat_input_kW: Optional[float] = Field(None, gt=0, le=50000, description="Isi girisi [kW]")
    air_outlet_temp_C: float = Field(80.0, ge=20, le=400, description="Hava cikis sicakligi [C]")
    ambient_temp_C: Optional[float] = Field(None, ge=-20, le=60, description="Ortam sicakligi [C]")
    ambient_humidity_pct: float = Field(50.0, ge=5, le=100, description="Ortam nemi [%]")
    operating_hours: float = Field(5000, ge=0, le=8760, description="Yillik calisma saati")
    fuel_price_eur_kwh: float = Field(0.05, ge=0, le=1, description="Yakit fiyati [EUR/kWh]")


class AnalysisRequest(BaseModel):
    equipment_type: Optional[str] = Field(None, description="Ekipman tipi")
    subtype: Optional[str] = Field(None, description="Ekipman alt tipi")
    compressor_type: Optional[Literal["screw", "piston", "scroll", "centrifugal"]] = Field(
        None, description="Kompresör tipi (geriye uyumluluk)"
    )
    parameters: dict = Field(..., description="Ekipman parametreleri")
