"""
Proses bazlı minimum exergy hesaplamaları.

Her proses tipi için termodinamik alt limit (reversible process) exergy gereksinimini hesaplar.
Bu değerler gerçek hayatta ulaşılamaz — gap analysis için referans alt limit olarak kullanılır.

Kaynaklar:
- Dincer & Rosen, "Exergy: Energy, Environment and Sustainable Development"
- Bejan, "Advanced Engineering Thermodynamics"
- Szargut, "Exergy Method: Technical and Ecological Applications"
- Kotas, "The Exergy Method of Thermal Plant Analysis"
"""

import math
from dataclasses import dataclass


@dataclass
class ProcessDefinition:
    """Proses kimlik kartı — simülasyon değil, tanım."""
    process_type: str                    # drying, heating, cooling, steam_generation,
                                         # compressed_air, chp, cold_storage, general_manufacturing
    process_label: str                   # Kullanıcının verdiği açıklama
    parameters: dict                     # Proses tipine özel parametreler
    subcategory: str = "general"         # BAT alt kategorisi
    operating_hours: float = 6000        # Yıllık çalışma saati
    energy_price_eur_kwh: float = 0.08   # Enerji fiyatı €/kWh


SUPPORTED_PROCESS_TYPES = {
    "drying": {
        "label": "Kurutma",
        "label_en": "Drying",
        "icon": "flame",
        "description": "Malzemeden nem uzaklaştırma prosesi",
        "required_params": ["mass_flow_kg_h", "moisture_in_pct", "moisture_out_pct"],
        "optional_params": {
            "material_name": {"default": "Malzeme", "type": "str", "label": "Malzeme Adı"},
            "material_inlet_temp_C": {"default": 20, "type": "float", "label": "Giriş Sıcaklığı (°C)"},
            "material_outlet_temp_C": {"default": 50, "type": "float", "label": "Çıkış Sıcaklığı (°C)"},
        },
        "param_definitions": {
            "mass_flow_kg_h": {"type": "float", "label": "Malzeme Debisi", "unit": "kg/h", "min": 1},
            "moisture_in_pct": {"type": "float", "label": "Giriş Nem Oranı", "unit": "%", "min": 0.1, "max": 99},
            "moisture_out_pct": {"type": "float", "label": "Çıkış Nem Oranı", "unit": "%", "min": 0.1, "max": 99},
        },
        "subcategories": ["food_grain", "food_spray", "wood_lumber", "general"],
    },
    "heating": {
        "label": "Isıtma",
        "label_en": "Heating",
        "icon": "thermometer",
        "description": "Akışkan/malzeme ısıtma prosesi",
        "required_params": ["mass_flow_kg_h", "temp_in_C", "temp_out_C"],
        "optional_params": {
            "fluid_name": {"default": "Su", "type": "str", "label": "Akışkan Adı"},
            "specific_heat_kJ_kgK": {"default": 4.18, "type": "float", "label": "Özgül Isı (kJ/kg·K)"},
        },
        "param_definitions": {
            "mass_flow_kg_h": {"type": "float", "label": "Akışkan Debisi", "unit": "kg/h", "min": 1},
            "temp_in_C": {"type": "float", "label": "Giriş Sıcaklığı", "unit": "°C"},
            "temp_out_C": {"type": "float", "label": "Çıkış Sıcaklığı", "unit": "°C"},
        },
        "subcategories": ["water_low", "water_high", "general"],
    },
    "cooling": {
        "label": "Soğutma",
        "label_en": "Cooling",
        "icon": "snowflake",
        "description": "Proses veya konfor soğutma",
        "required_params": ["cooling_load_kW", "cold_temp_C"],
        "optional_params": {
            "ambient_temp_C": {"default": 25, "type": "float", "label": "Ortam Sıcaklığı (°C)"},
        },
        "param_definitions": {
            "cooling_load_kW": {"type": "float", "label": "Soğutma Yükü", "unit": "kW", "min": 0.1},
            "cold_temp_C": {"type": "float", "label": "Soğuk Taraf Sıcaklığı", "unit": "°C"},
        },
        "subcategories": ["comfort", "process", "general"],
    },
    "steam_generation": {
        "label": "Buhar Üretimi",
        "label_en": "Steam Generation",
        "icon": "cloud",
        "description": "Endüstriyel buhar üretim prosesi",
        "required_params": ["steam_flow_kg_h", "steam_pressure_bar"],
        "optional_params": {
            "steam_temp_C": {"default": None, "type": "float", "label": "Buhar Sıcaklığı (°C, boş=doymuş)"},
            "feedwater_temp_C": {"default": 20, "type": "float", "label": "Besleme Suyu Sıcaklığı (°C)"},
        },
        "param_definitions": {
            "steam_flow_kg_h": {"type": "float", "label": "Buhar Debisi", "unit": "kg/h", "min": 1},
            "steam_pressure_bar": {"type": "float", "label": "Buhar Basıncı", "unit": "bar", "min": 1, "max": 200},
        },
        "subcategories": ["industrial_low", "industrial_high", "general"],
    },
    "compressed_air": {
        "label": "Basınçlı Hava",
        "label_en": "Compressed Air",
        "icon": "wind",
        "description": "Basınçlı hava üretim sistemi",
        "required_params": ["air_flow_m3_min", "discharge_pressure_bar"],
        "optional_params": {
            "inlet_temp_C": {"default": 20, "type": "float", "label": "Giriş Sıcaklığı (°C)"},
        },
        "param_definitions": {
            "air_flow_m3_min": {"type": "float", "label": "Hava Debisi (FAD)", "unit": "m³/min", "min": 0.1},
            "discharge_pressure_bar": {"type": "float", "label": "Çıkış Basıncı", "unit": "bar", "min": 2, "max": 40},
        },
        "subcategories": ["general"],
    },
    "chp": {
        "label": "CHP / Kojenerasyon",
        "label_en": "Combined Heat & Power",
        "icon": "zap",
        "description": "Kombine ısı-güç üretimi",
        "required_params": ["fuel_input_kW", "electrical_output_kW", "thermal_output_kW"],
        "optional_params": {
            "thermal_temp_C": {"default": 90, "type": "float", "label": "Isı Çıktı Sıcaklığı (°C)"},
        },
        "param_definitions": {
            "fuel_input_kW": {"type": "float", "label": "Yakıt Girişi (LHV)", "unit": "kW", "min": 1},
            "electrical_output_kW": {"type": "float", "label": "Elektrik Çıktısı", "unit": "kW", "min": 0},
            "thermal_output_kW": {"type": "float", "label": "Isı Çıktısı", "unit": "kW", "min": 0},
        },
        "subcategories": ["gas_turbine", "gas_engine", "general"],
    },
    "cold_storage": {
        "label": "Soğuk Depolama",
        "label_en": "Cold Storage",
        "icon": "box",
        "description": "Soğuk zincir / depolama",
        "required_params": ["heat_load_kW", "target_temp_C"],
        "optional_params": {
            "ambient_temp_C": {"default": 25, "type": "float", "label": "Ortam Sıcaklığı (°C)"},
            "storage_volume_m3": {"default": 100, "type": "float", "label": "Depo Hacmi (m³)"},
        },
        "param_definitions": {
            "heat_load_kW": {"type": "float", "label": "Toplam Isı Yükü", "unit": "kW", "min": 0.1},
            "target_temp_C": {"type": "float", "label": "Hedef Sıcaklık", "unit": "°C"},
        },
        "subcategories": ["general"],
    },
    "general_manufacturing": {
        "label": "Genel Üretim",
        "label_en": "General Manufacturing",
        "icon": "factory",
        "description": "Endüstriyel üretim prosesi",
        "required_params": ["production_rate_ton_h"],
        "optional_params": {
            "product_name": {"default": "Ürün", "type": "str", "label": "Ürün Adı"},
        },
        "param_definitions": {
            "production_rate_ton_h": {"type": "float", "label": "Üretim Hızı", "unit": "ton/h", "min": 0.01},
        },
        "subcategories": ["cement", "glass", "paper", "sugar", "concrete", "general"],
    },
}


def get_process_types() -> dict:
    """Tüm desteklenen proses tiplerini ve meta bilgilerini döndürür."""
    return SUPPORTED_PROCESS_TYPES


def get_subcategories(process_type: str) -> list[dict]:
    """Bir proses tipi için mevcut alt kategorileri döndürür."""
    from engine.bat_references import get_available_subcategories
    return get_available_subcategories(process_type)


def calculate_minimum_exergy(process_def: ProcessDefinition, T0_K: float = 298.15) -> dict:
    """
    Proses tipine göre termodinamik minimum exergy gereksinimini hesaplar.

    Args:
        process_def: Proses tanımı
        T0_K: Dead state sıcaklığı (K), varsayılan 298.15 K (25°C)

    Returns:
        dict with minimum_exergy_kW, calculation_method, assumptions, breakdown,
        specific_unit, specific_minimum, production_rate_unit

    Raises:
        ValueError: Desteklenmeyen proses tipi veya eksik parametre
    """
    calculators = {
        "drying": _min_exergy_drying,
        "heating": _min_exergy_heating,
        "cooling": _min_exergy_cooling,
        "steam_generation": _min_exergy_steam,
        "compressed_air": _min_exergy_compressed_air,
        "chp": _min_exergy_chp,
        "cold_storage": _min_exergy_cold_storage,
        "general_manufacturing": _min_exergy_general,
    }

    calculator = calculators.get(process_def.process_type)
    if not calculator:
        raise ValueError(f"Desteklenmeyen proses tipi: {process_def.process_type}")

    # Gerekli parametrelerin varlığını kontrol et
    type_info = SUPPORTED_PROCESS_TYPES[process_def.process_type]
    for param in type_info["required_params"]:
        if param not in process_def.parameters:
            raise ValueError(f"Eksik parametre: {param}")

    return calculator(process_def.parameters, T0_K)


# ---------------------------------------------------------------------------
# Private calculator functions
# ---------------------------------------------------------------------------

def _min_exergy_drying(params: dict, T0_K: float) -> dict:
    """
    Kurutma prosesi minimum exergy.

    Ex_min ≈ m_water_removed × ex_water_evaporation(T0)
    ex_water_evaporation(25°C) ≈ 50 kJ/kg su

    Referans: Dincer & Rosen, "Exergy Analysis of Drying Processes and Systems"
    """
    mass_flow = params["mass_flow_kg_h"]
    moisture_in = params["moisture_in_pct"] / 100
    moisture_out = params["moisture_out_pct"] / 100

    if moisture_in <= moisture_out:
        return {
            "minimum_exergy_kW": 0.0,
            "calculation_method": "No drying needed (moisture_in <= moisture_out)",
            "assumptions": [],
            "breakdown": {},
            "specific_unit": "kWh/kg su",
            "specific_minimum": 0.0,
            "production_rate_unit": 0.0,
        }

    # Kuru bazda su miktarı hesabı
    dry_mass = mass_flow * (1 - moisture_in)
    water_in = dry_mass * moisture_in / (1 - moisture_in)
    water_out = dry_mass * moisture_out / (1 - moisture_out)
    water_removed_kg_h = water_in - water_out

    # Minimum exergy: kimyasal exergy of water removal at T0
    # ~50 kJ/kg removed water @25°C (Dincer & Rosen)
    EX_EVAP_KJ_PER_KG = 50.0

    evap_exergy_kW = water_removed_kg_h * EX_EVAP_KJ_PER_KG / 3600

    # Eğer malzeme ısıtma da gerekiyorsa
    T_in_K = params.get("material_inlet_temp_C", 20) + 273.15
    T_out_K = params.get("material_outlet_temp_C", 20) + 273.15
    heating_exergy_kW = 0.0

    if T_out_K > T_in_K and T_out_K > T0_K:
        cp_material = 2.0  # kJ/kg·K (ıslak malzeme yaklaşık)
        Q_heating_kW = mass_flow * cp_material * (T_out_K - T_in_K) / 3600
        T_lm = (T_out_K - T_in_K) / math.log(T_out_K / T_in_K) if T_out_K != T_in_K else T_in_K
        carnot = max(0, 1 - T0_K / T_lm)
        heating_exergy_kW = Q_heating_kW * carnot

    min_exergy_kW = evap_exergy_kW + heating_exergy_kW

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 4),
        "water_removed_kg_h": round(water_removed_kg_h, 2),
        "calculation_method": "Chemical exergy of water removal (Dincer & Rosen, 2011)",
        "assumptions": [
            f"Buharlaştırma exergisi: {EX_EVAP_KJ_PER_KG} kJ/kg su @{T0_K - 273.15:.0f}°C",
            "Ortam bağıl nemi %60 varsayılmış",
            "Malzeme-su bağlanma enerjisi ihmal edilmiş (bound moisture ignored)",
        ],
        "breakdown": {
            "evaporation_exergy_kW": round(evap_exergy_kW, 4),
            "heating_exergy_kW": round(heating_exergy_kW, 4),
        },
        "specific_unit": "kWh/kg su",
        "specific_minimum": round(EX_EVAP_KJ_PER_KG / 3600, 6),
        "production_rate_unit": round(water_removed_kg_h, 2),
    }


def _min_exergy_heating(params: dict, T0_K: float) -> dict:
    """
    Isıtma prosesi minimum exergy = Carnot work.

    Ex_min = Q × (1 - T0/T_lm)
    T_lm = (T_out - T_in) / ln(T_out/T_in)

    Referans: Bejan, "Advanced Engineering Thermodynamics", Chapter 3
    """
    mass_flow = params["mass_flow_kg_h"]
    T_in_K = params["temp_in_C"] + 273.15
    T_out_K = params["temp_out_C"] + 273.15
    cp = params.get("specific_heat_kJ_kgK", 4.18)

    if T_out_K <= T_in_K:
        return _empty_result("No heating needed", "kWh/kg")

    Q_kW = mass_flow * cp * (T_out_K - T_in_K) / 3600
    T_lm = (T_out_K - T_in_K) / math.log(T_out_K / T_in_K)
    carnot = max(0, 1 - T0_K / T_lm)
    min_exergy_kW = Q_kW * carnot

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 4),
        "Q_thermal_kW": round(Q_kW, 2),
        "T_lm_K": round(T_lm, 2),
        "carnot_factor": round(carnot, 4),
        "calculation_method": "Carnot work — reversible heat transfer (Bejan)",
        "assumptions": [
            f"Log-mean sıcaklık: {T_lm:.1f} K",
            f"Carnot faktörü: {carnot:.4f}",
            "Basınç düşümü ihmal edildi",
            f"Özgül ısı sabit: {cp} kJ/kg·K",
        ],
        "breakdown": {
            "thermal_load_kW": round(Q_kW, 2),
            "carnot_work_kW": round(min_exergy_kW, 4),
        },
        "specific_unit": "kWh/kg",
        "specific_minimum": round(min_exergy_kW / (mass_flow / 3600) if mass_flow > 0 else 0, 6),
        "production_rate_unit": round(mass_flow, 2),
    }


def _min_exergy_cooling(params: dict, T0_K: float) -> dict:
    """
    Soğutma prosesi minimum exergy = Reverse Carnot work.

    Ex_min = Q_cool × (T0/T_cold - 1)
    COP_carnot = T_cold / (T0 - T_cold)

    Referans: Kotas, "The Exergy Method of Thermal Plant Analysis"
    """
    Q_cool = params["cooling_load_kW"]
    T_cold_K = params["cold_temp_C"] + 273.15
    T0 = params.get("ambient_temp_C", 25) + 273.15 if "ambient_temp_C" in params else T0_K

    if T_cold_K >= T0:
        return _empty_result("No cooling needed (T_cold >= T_ambient)", "kWh/kWh")

    cop_carnot = T_cold_K / (T0 - T_cold_K)
    min_exergy_kW = Q_cool / cop_carnot

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 4),
        "COP_carnot": round(cop_carnot, 2),
        "calculation_method": "Reverse Carnot COP (Kotas)",
        "assumptions": [
            f"Carnot COP: {cop_carnot:.2f}",
            f"Ortam sıcaklığı: {T0 - 273.15:.1f}°C",
            "İdeal tersinir soğutma çevrimi",
        ],
        "breakdown": {
            "cooling_load_kW": Q_cool,
            "carnot_work_kW": round(min_exergy_kW, 4),
        },
        "specific_unit": "kWh/kWh soğutma",
        "specific_minimum": round(1 / cop_carnot, 6),
        "production_rate_unit": round(Q_cool, 2),
    }


def _min_exergy_steam(params: dict, T0_K: float) -> dict:
    """
    Buhar üretimi minimum exergy = buharın fiziksel exergisi - besleme suyunun exergisi.

    CoolProp varsa kullan, yoksa yaklaşık formül (steam table approximation).

    Referans: Szargut, "Exergy Method: Technical and Ecological Applications"
    """
    steam_flow = params["steam_flow_kg_h"]
    P_bar = params["steam_pressure_bar"]
    T_steam_C = params.get("steam_temp_C")
    T_fw_C = params.get("feedwater_temp_C", 20)

    T0_C = T0_K - 273.15

    try:
        import CoolProp.CoolProp as CP

        P_Pa = P_bar * 1e5

        # Buhar durumu
        if T_steam_C is None:
            h_steam = CP.PropsSI('H', 'P', P_Pa, 'Q', 1, 'Water') / 1000
            s_steam = CP.PropsSI('S', 'P', P_Pa, 'Q', 1, 'Water') / 1000
        else:
            T_steam_K = T_steam_C + 273.15
            h_steam = CP.PropsSI('H', 'P', P_Pa, 'T', T_steam_K, 'Water') / 1000
            s_steam = CP.PropsSI('S', 'P', P_Pa, 'T', T_steam_K, 'Water') / 1000

        # Besleme suyu durumu (sıvı, atmosferik basınç)
        P0_Pa = 101325
        T_fw_K = T_fw_C + 273.15
        h_fw = CP.PropsSI('H', 'P', P0_Pa, 'T', T_fw_K, 'Water') / 1000
        s_fw = CP.PropsSI('S', 'P', P0_Pa, 'T', T_fw_K, 'Water') / 1000

        # Dead state
        h0 = CP.PropsSI('H', 'P', P0_Pa, 'T', T0_K, 'Water') / 1000
        s0 = CP.PropsSI('S', 'P', P0_Pa, 'T', T0_K, 'Water') / 1000

        method = "CoolProp ile fiziksel exergy hesabı (Szargut)"

    except (ImportError, Exception):
        # Fallback: Yaklaşık formül
        steam_exergy_approx = {
            1: 450, 2: 550, 3: 610, 5: 700, 7: 750,
            10: 810, 15: 870, 20: 920, 30: 980, 40: 1030, 50: 1070,
        }
        pressures = sorted(steam_exergy_approx.keys())
        if P_bar <= pressures[0]:
            ex_steam_approx = steam_exergy_approx[pressures[0]]
        elif P_bar >= pressures[-1]:
            ex_steam_approx = steam_exergy_approx[pressures[-1]]
        else:
            ex_steam_approx = steam_exergy_approx[pressures[0]]  # default
            for i in range(len(pressures) - 1):
                if pressures[i] <= P_bar <= pressures[i + 1]:
                    frac = (P_bar - pressures[i]) / (pressures[i + 1] - pressures[i])
                    ex_steam_approx = (
                        steam_exergy_approx[pressures[i]] * (1 - frac)
                        + steam_exergy_approx[pressures[i + 1]] * frac
                    )
                    break

        # Besleme suyu exergisi
        ex_fw_approx = max(0, (T_fw_C - T0_C) * 4.18 * (1 - T0_K / (T_fw_C + 273.15 + T0_K) * 2))

        min_exergy_kW = steam_flow * (ex_steam_approx - ex_fw_approx) / 3600

        return {
            "minimum_exergy_kW": round(min_exergy_kW, 2),
            "calculation_method": "Yaklaşık buhar exergisi tablosu (fallback, CoolProp yok)",
            "assumptions": [
                f"Buhar exergisi ≈ {ex_steam_approx:.0f} kJ/kg @{P_bar} bar (tablo interpolasyonu)",
                "CoolProp mevcut değil, yaklaşık değerler kullanıldı",
            ],
            "breakdown": {
                "steam_exergy_kJ_kg": round(ex_steam_approx, 1),
                "feedwater_exergy_kJ_kg": round(ex_fw_approx, 1),
            },
            "specific_unit": "kWh/kg buhar",
            "specific_minimum": round(ex_steam_approx / 3600, 6),
            "production_rate_unit": round(steam_flow, 2),
        }

    # CoolProp başarılı
    ex_steam = (h_steam - h0) - T0_K * (s_steam - s0)
    ex_fw = (h_fw - h0) - T0_K * (s_fw - s0)

    min_exergy_per_kg = ex_steam - ex_fw
    min_exergy_kW = steam_flow * min_exergy_per_kg / 3600

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 2),
        "calculation_method": method,
        "assumptions": [
            f"Buhar: {P_bar} bar, {'doymuş' if T_steam_C is None else f'{T_steam_C}°C'}",
            f"Besleme suyu: {T_fw_C}°C, atmosferik basınç",
            f"Dead state: {T0_K - 273.15:.1f}°C, 1 atm",
        ],
        "breakdown": {
            "steam_exergy_kJ_kg": round(ex_steam, 2),
            "feedwater_exergy_kJ_kg": round(ex_fw, 2),
            "net_exergy_kJ_kg": round(min_exergy_per_kg, 2),
            "h_steam": round(h_steam, 2),
            "s_steam": round(s_steam, 4),
        },
        "specific_unit": "kWh/kg buhar",
        "specific_minimum": round(min_exergy_per_kg / 3600, 6),
        "production_rate_unit": round(steam_flow, 2),
    }


def _min_exergy_compressed_air(params: dict, T0_K: float) -> dict:
    """
    Basınçlı hava minimum exergy = izothermal sıkıştırma işi.

    W_min = m_air × R_specific × T0 × ln(P2/P1)

    Referans: DOE Compressed Air Challenge; Bejan Chapter 4
    """
    Q_m3_min = params["air_flow_m3_min"]
    P2_bar = params["discharge_pressure_bar"]
    T_inlet_C = params.get("inlet_temp_C", 20)
    P1_bar = 1.01325

    # m³/min → kg/s
    T_inlet_K = T_inlet_C + 273.15
    rho_air = 101325 / (287 * T_inlet_K)
    m_dot_kg_s = Q_m3_min * rho_air / 60

    R_air = 287  # J/kg·K

    # İzothermal sıkıştırma (termodinamik minimum)
    W_min_kW = m_dot_kg_s * R_air * T0_K * math.log(P2_bar / P1_bar) / 1000

    # Spesifik: kWh/m³ FAD
    specific_kWh_m3 = W_min_kW / (Q_m3_min * 60) if Q_m3_min > 0 else 0

    return {
        "minimum_exergy_kW": round(W_min_kW, 4),
        "air_mass_flow_kg_s": round(m_dot_kg_s, 4),
        "calculation_method": "Isothermal compression work (Bejan, DOE)",
        "assumptions": [
            f"İzothermal sıkıştırma @{T0_K - 273.15:.0f}°C",
            f"Basınç oranı: {P2_bar / P1_bar:.2f}",
            f"Hava yoğunluğu: {rho_air:.3f} kg/m³ @{T_inlet_C}°C",
            "İdeal gaz varsayımı",
        ],
        "breakdown": {
            "pressure_ratio": round(P2_bar / P1_bar, 2),
            "isothermal_work_kW": round(W_min_kW, 4),
        },
        "specific_unit": "kWh/m³",
        "specific_minimum": round(specific_kWh_m3, 6),
        "production_rate_unit": round(Q_m3_min * 60, 2),
    }


def _min_exergy_chp(params: dict, T0_K: float) -> dict:
    """
    CHP minimum exergy = toplam faydalı exergy çıktısı.

    Ex_min = Ex_electrical + Ex_thermal

    Referans: Tsatsaronis, "Thermoeconomic Analysis and Optimization"
    """
    fuel_kW = params["fuel_input_kW"]
    W_elec = params["electrical_output_kW"]
    Q_thermal = params["thermal_output_kW"]
    T_heat_C = params.get("thermal_temp_C", 90)
    T_heat_K = T_heat_C + 273.15

    ex_electrical = W_elec
    carnot = max(0, 1 - T0_K / T_heat_K)
    ex_thermal = Q_thermal * carnot

    min_exergy_kW = ex_electrical + ex_thermal

    # Yakıt exergisi (doğalgaz exergy/energy oranı ≈ 1.04)
    FUEL_EXERGY_FACTOR = 1.04
    fuel_exergy_kW = fuel_kW * FUEL_EXERGY_FACTOR

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 2),
        "fuel_exergy_kW": round(fuel_exergy_kW, 2),
        "calculation_method": "Combined exergy output (Tsatsaronis)",
        "assumptions": [
            f"Elektrik = saf exergy: {W_elec} kW",
            f"Isı exergisi: {Q_thermal} kW × {carnot:.4f} = {ex_thermal:.2f} kW",
            f"Yakıt exergy faktörü: {FUEL_EXERGY_FACTOR}",
        ],
        "breakdown": {
            "electrical_exergy_kW": round(ex_electrical, 2),
            "thermal_exergy_kW": round(ex_thermal, 2),
        },
        "specific_unit": "kWh/kWh yakıt",
        "specific_minimum": round(min_exergy_kW / fuel_exergy_kW if fuel_exergy_kW > 0 else 0, 4),
        "production_rate_unit": round(fuel_kW, 2),
    }


def _min_exergy_cold_storage(params: dict, T0_K: float) -> dict:
    """
    Soğuk depolama minimum exergy = cooling prosesiyle aynı mantık.
    Ex_min = Q_load × (T0/T_cold - 1)
    """
    Q_load = params["heat_load_kW"]
    T_cold_C = params["target_temp_C"]
    T_cold_K = T_cold_C + 273.15
    T0 = params.get("ambient_temp_C", 25) + 273.15 if "ambient_temp_C" in params else T0_K

    if T_cold_K >= T0:
        return _empty_result("No cooling needed", "kWh/kWh")

    cop_carnot = T_cold_K / (T0 - T_cold_K)
    min_exergy_kW = Q_load / cop_carnot

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 4),
        "COP_carnot": round(cop_carnot, 2),
        "calculation_method": "Reverse Carnot COP for cold storage",
        "assumptions": [
            f"Hedef sıcaklık: {T_cold_C}°C",
            f"Carnot COP: {cop_carnot:.2f}",
        ],
        "breakdown": {
            "heat_load_kW": Q_load,
            "carnot_work_kW": round(min_exergy_kW, 4),
        },
        "specific_unit": "kWh/kWh soğutma",
        "specific_minimum": round(1 / cop_carnot, 6),
        "production_rate_unit": round(Q_load, 2),
    }


def _min_exergy_general(params: dict, T0_K: float) -> dict:
    """
    Genel üretim prosesi — sektör BAT değerinin %30'u.
    Termodinamik minimum hesaplamak için proses-spesifik bilgi gerekir.
    """
    from engine.bat_references import get_bat_reference

    production_rate = params["production_rate_ton_h"]
    subcategory = params.get("sector_subcategory", "general")

    bat_ref = get_bat_reference("general_manufacturing", subcategory)
    bat_specific = bat_ref["specific_exergy_kwh_per_unit"]

    # Minimum ≈ BAT'ın %30'u (kaba tahmin)
    MINIMUM_FRACTION = 0.30
    min_specific = bat_specific * MINIMUM_FRACTION
    min_exergy_kW = production_rate * 1000 * min_specific  # ton/h → kg/h, kWh/kg → kW

    return {
        "minimum_exergy_kW": round(min_exergy_kW, 2),
        "calculation_method": f"Sektör BAT referansının %{MINIMUM_FRACTION * 100:.0f}'i (tahmin)",
        "assumptions": [
            f"Sektör: {bat_ref.get('label', subcategory)}",
            f"BAT spesifik exergy: {bat_specific} kWh/kg",
            f"Minimum tahmin oranı: %{MINIMUM_FRACTION * 100:.0f}",
            "Bu kaba bir tahmindir — proses-spesifik hesaplama yapılamamıştır",
        ],
        "breakdown": {
            "bat_specific_kWh_kg": bat_specific,
            "minimum_specific_kWh_kg": round(min_specific, 6),
        },
        "specific_unit": "kWh/kg",
        "specific_minimum": round(min_specific, 6),
        "production_rate_unit": round(production_rate * 1000, 2),
    }


def _empty_result(reason: str, unit: str) -> dict:
    """Boş sonuç döndürür (hesaplama gerekmeyen durumlar için)."""
    return {
        "minimum_exergy_kW": 0.0,
        "calculation_method": reason,
        "assumptions": [],
        "breakdown": {},
        "specific_unit": unit,
        "specific_minimum": 0.0,
        "production_rate_unit": 0.0,
    }
