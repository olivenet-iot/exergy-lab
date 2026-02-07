# BRIEF 1: Gap Analysis Engine + DB + API + Tests

> **Tarih:** 2026-02-07
> **Öncelik:** Kritik — Tüm frontend çalışmaları buna bağımlı
> **Bağımlılık:** Brief 0 ile paralel çalıştırılabilir (farklı klasörler)
> **Dokunduğu Klasörler:** engine/, api/, tests/
> **Tahmini:** ~1200 satır yeni kod + testler
> **Kural:** Frontend'e DOKUNMA, knowledge/ klasörüne DOKUNMA

---

## 1. Amaç

ExergyLab'e proses tanımı ve exergetic gap analysis motoru eklemek. Bu brief backend tarafını kapsar:
- 8 proses tipi için minimum exergy hesaplama
- BAT referans veritabanı
- Gap analysis motoru
- DB migration (yeni alanlar)
- API endpointleri
- Factory pipeline entegrasyonu (Adım 11)
- Kapsamlı testler

---

## 2. Yeni Dosyalar

### 2.1 `engine/process_exergy.py` (~300 satır)

Bu dosya her proses tipi için termodinamik minimum exergy gereksinimini hesaplar.

**ÖNEMLİ:** Bunlar simülasyon DEĞİL — termodinamik alt limitler. %10-20 hata payı kabul edilebilir. Önemli olan büyüklük sırası.

```python
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
from dataclasses import dataclass, field
from typing import Optional

# engine/core.py'deki DeadState'i import et
# from engine.core import DeadState  — mevcut dead state yapısını kullan


@dataclass
class ProcessDefinition:
    """Proses kimlik kartı — simülasyon değil, tanım."""
    process_type: str                    # drying, heating, cooling, steam_generation, 
                                         # compressed_air, chp, cold_storage, general_manufacturing
    process_label: str                   # Kullanıcının verdiği açıklama (ör: "Mısır kurutma hattı")
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
    """Bir proses tipi için mevcut alt kategorileri döndürür.
    bat_references.py'deki BAT_REFERENCES'tan çeker."""
    # bat_references.py import edilecek
    pass


def calculate_minimum_exergy(process_def: ProcessDefinition, T0_K: float = 298.15) -> dict:
    """
    Proses tipine göre termodinamik minimum exergy gereksinimini hesaplar.
    
    Args:
        process_def: Proses tanımı
        T0_K: Dead state sıcaklığı (K), varsayılan 298.15 K (25°C)
    
    Returns:
        {
            "minimum_exergy_kW": float,
            "calculation_method": str,
            "assumptions": list[str],
            "breakdown": dict,
            "specific_unit": str,           # "kWh/kg su", "kWh/kg buhar", vb.
            "specific_minimum": float,      # Birim başına minimum exergy
            "production_rate_unit": float,  # Birim/saat (normalizasyon için)
        }
    
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
```

#### Minimum Exergy Hesaplama Fonksiyonları

```python
def _min_exergy_drying(params: dict, T0_K: float) -> dict:
    """
    Kurutma prosesi minimum exergy.
    
    Termodinamik minimum = suyun kimyasal exergisi farkı (bağlı su → serbest buhar)
    
    Basitleştirilmiş formül (Dincer & Rosen):
    Ex_min ≈ m_water_removed × ex_water_evaporation(T0)
    
    Burada ex_water_evaporation(25°C) ≈ 50 kJ/kg su
    Bu değer suyun kimyasal exergisinden gelir:
    ex_chem_water = R*T0*ln(1/phi_0) + [h_fg - T0*s_fg] ≈ 50 kJ/kg
    (phi_0 = ortam bağıl nemi, tipik %60 için)
    
    Referans: Dincer & Rosen, "Exergy Analysis of Drying Processes and Systems"
              Sustainable Cities and Society, 2011, 1(2), 91-96
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
    # Bu çok düşük bir değer — gerçek kurutma bunun 50-200 katı
    EX_EVAP_KJ_PER_KG = 50.0
    
    evap_exergy_kW = water_removed_kg_h * EX_EVAP_KJ_PER_KG / 3600
    
    # Eğer malzeme ısıtma da gerekiyorsa
    T_in_K = (params.get("material_inlet_temp_C", 20)) + 273.15
    T_out_K = (params.get("material_outlet_temp_C", 20)) + 273.15  # varsayılan: giriş ile aynı
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
            f"Buharlaştırma exergisi: {EX_EVAP_KJ_PER_KG} kJ/kg su @{T0_K-273.15:.0f}°C",
            "Ortam bağıl nemi %60 varsayılmış",
            "Malzeme-su bağlanma enerjisi ihmal edilmiş (bound moisture ignored)",
        ],
        "breakdown": {
            "evaporation_exergy_kW": round(evap_exergy_kW, 4),
            "heating_exergy_kW": round(heating_exergy_kW, 4),
        },
        "specific_unit": "kWh/kg su",
        "specific_minimum": round(EX_EVAP_KJ_PER_KG / 3600, 6),  # kWh/kg
        "production_rate_unit": round(water_removed_kg_h, 2),
    }


def _min_exergy_heating(params: dict, T0_K: float) -> dict:
    """
    Isıtma prosesi minimum exergy = Carnot work.
    
    Ex_min = Q × (1 - T0/T_lm)
    T_lm = (T_out - T_in) / ln(T_out/T_in)
    Q = m × cp × (T_out - T_in)
    
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
    
    Bu, ideal Carnot soğutma makinasının minimum iş gereksinimi.
    COP_carnot = T_cold / (T0 - T_cold)
    W_min = Q_cool / COP_carnot = Q_cool × (T0/T_cold - 1)
    
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
            f"Ortam sıcaklığı: {T0-273.15:.1f}°C",
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
    
    Ex_min = m_steam × (ex_steam - ex_feedwater)
    ex = (h - h0) - T0 × (s - s0)
    
    CoolProp varsa kullan, yoksa yaklaşık formül (steam table approximation).
    
    Referans: Szargut, "Exergy Method: Technical and Ecological Applications"
    """
    steam_flow = params["steam_flow_kg_h"]
    P_bar = params["steam_pressure_bar"]
    T_steam_C = params.get("steam_temp_C")  # None = doymuş buhar
    T_fw_C = params.get("feedwater_temp_C", 20)
    
    T0_C = T0_K - 273.15
    
    try:
        import CoolProp.CoolProp as CP
        
        P_Pa = P_bar * 1e5
        
        # Buhar durumu
        if T_steam_C is None:
            # Doymuş buhar
            h_steam = CP.PropsSI('H', 'P', P_Pa, 'Q', 1, 'Water') / 1000  # kJ/kg
            s_steam = CP.PropsSI('S', 'P', P_Pa, 'Q', 1, 'Water') / 1000  # kJ/kg·K
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
        # Doymuş buhar exergisi yaklaşık değerleri (kJ/kg)
        # Basınca göre lineer interpolasyon (kaba ama büyüklük sırası doğru)
        steam_exergy_approx = {
            1: 450, 2: 550, 3: 610, 5: 700, 7: 750,
            10: 810, 15: 870, 20: 920, 30: 980, 40: 1030, 50: 1070,
        }
        # En yakın basınca interpolasyon
        pressures = sorted(steam_exergy_approx.keys())
        if P_bar <= pressures[0]:
            ex_steam_approx = steam_exergy_approx[pressures[0]]
        elif P_bar >= pressures[-1]:
            ex_steam_approx = steam_exergy_approx[pressures[-1]]
        else:
            for i in range(len(pressures) - 1):
                if pressures[i] <= P_bar <= pressures[i+1]:
                    frac = (P_bar - pressures[i]) / (pressures[i+1] - pressures[i])
                    ex_steam_approx = (steam_exergy_approx[pressures[i]] * (1-frac) + 
                                      steam_exergy_approx[pressures[i+1]] * frac)
                    break
        
        # Besleme suyu exergisi (20°C'de ≈ 0 kJ/kg, sıcak besleme suyunda biraz daha fazla)
        ex_fw_approx = max(0, (T_fw_C - T0_C) * 4.18 * (1 - T0_K / (T_fw_C + 273.15 + T0_K) * 2))
        
        h_steam = s_steam = h_fw = s_fw = h0 = s0 = 0  # Kullanılmıyor fallback'te
        
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
    ex_steam = (h_steam - h0) - T0_K * (s_steam - s0)  # kJ/kg
    ex_fw = (h_fw - h0) - T0_K * (s_fw - s0)  # kJ/kg
    
    min_exergy_per_kg = ex_steam - ex_fw  # kJ/kg buhar
    min_exergy_kW = steam_flow * min_exergy_per_kg / 3600
    
    return {
        "minimum_exergy_kW": round(min_exergy_kW, 2),
        "calculation_method": method,
        "assumptions": [
            f"Buhar: {P_bar} bar, {'doymuş' if T_steam_C is None else f'{T_steam_C}°C'}",
            f"Besleme suyu: {T_fw_C}°C, atmosferik basınç",
            f"Dead state: {T0_K-273.15:.1f}°C, 1 atm",
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
    R_specific_air = 287 J/kg·K
    rho_air@20°C,1atm ≈ 1.2 kg/m³
    
    Bu termodinamik alt limit — gerçek kompresörler bunun 5-10 katı tüketir.
    
    Referans: DOE Compressed Air Challenge; Bejan Chapter 4
    """
    Q_m3_min = params["air_flow_m3_min"]  # FAD (Free Air Delivery)
    P2_bar = params["discharge_pressure_bar"]
    T_inlet_C = params.get("inlet_temp_C", 20)
    P1_bar = 1.01325  # Atmosfer
    
    # m³/min → kg/s
    T_inlet_K = T_inlet_C + 273.15
    rho_air = 101325 / (287 * T_inlet_K)  # kg/m³ (ideal gaz)
    m_dot_kg_s = Q_m3_min * rho_air / 60
    
    R_air = 287  # J/kg·K
    
    # İzothermal sıkıştırma (termodinamik minimum)
    W_min_kW = m_dot_kg_s * R_air * T0_K * math.log(P2_bar / P1_bar) / 1000
    
    # Spesifik: kWh/m³ FAD
    specific_kWh_m3 = W_min_kW / (Q_m3_min * 60) if Q_m3_min > 0 else 0  # kWh/m³
    
    return {
        "minimum_exergy_kW": round(W_min_kW, 4),
        "air_mass_flow_kg_s": round(m_dot_kg_s, 4),
        "calculation_method": "Isothermal compression work (Bejan, DOE)",
        "assumptions": [
            f"İzothermal sıkıştırma @{T0_K-273.15:.0f}°C",
            f"Basınç oranı: {P2_bar/P1_bar:.2f}",
            f"Hava yoğunluğu: {rho_air:.3f} kg/m³ @{T_inlet_C}°C",
            "İdeal gaz varsayımı",
        ],
        "breakdown": {
            "pressure_ratio": round(P2_bar / P1_bar, 2),
            "isothermal_work_kW": round(W_min_kW, 4),
        },
        "specific_unit": "kWh/m³",
        "specific_minimum": round(specific_kWh_m3, 6),
        "production_rate_unit": round(Q_m3_min * 60, 2),  # m³/h
    }


def _min_exergy_chp(params: dict, T0_K: float) -> dict:
    """
    CHP minimum exergy = toplam faydalı exergy çıktısı.
    
    Ex_min = Ex_electrical + Ex_thermal
    Ex_electrical = W_elec (elektrik = saf exergy)
    Ex_thermal = Q_thermal × (1 - T0/T_heat)
    
    Yakıt exergisi > Ex_min olmalı (fark = yıkım + kayıp)
    
    Referans: Tsatsaronis, "Thermoeconomic Analysis and Optimization"
    """
    fuel_kW = params["fuel_input_kW"]
    W_elec = params["electrical_output_kW"]
    Q_thermal = params["thermal_output_kW"]
    T_heat_C = params.get("thermal_temp_C", 90)
    T_heat_K = T_heat_C + 273.15
    
    ex_electrical = W_elec  # Elektrik = saf exergy
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
    Genel üretim prosesi — sektör bazlı spesifik exergy referansı.
    
    Burada termodinamik minimum yerine sektör BAT değerinin %30-50'si kullanılır.
    (Gerçek minimum hesaplamak için proses-spesifik bilgi gerekir)
    
    NOT: Bu en kaba tahmindir. Diğer 7 proses tipi kullanılabiliyorsa tercih edilmeli.
    """
    # bat_references.py'den BAT değeri alınacak
    from engine.bat_references import get_bat_reference
    
    production_rate = params["production_rate_ton_h"]
    subcategory = params.get("sector_subcategory", "general")
    
    bat_ref = get_bat_reference("general_manufacturing", subcategory)
    bat_specific = bat_ref["specific_exergy_kwh_per_unit"]
    
    # Minimum ≈ BAT'ın %30'u (kaba tahmin — termodinamik limit bilinmiyor)
    MINIMUM_FRACTION = 0.30
    min_specific = bat_specific * MINIMUM_FRACTION
    min_exergy_kW = production_rate * 1000 * min_specific  # ton/h → kg/h, kWh/kg → kW
    
    return {
        "minimum_exergy_kW": round(min_exergy_kW, 2),
        "calculation_method": f"Sektör BAT referansının %{MINIMUM_FRACTION*100:.0f}'i (tahmin)",
        "assumptions": [
            f"Sektör: {bat_ref.get('label', subcategory)}",
            f"BAT spesifik exergy: {bat_specific} kWh/kg",
            f"Minimum tahmin oranı: %{MINIMUM_FRACTION*100:.0f}",
            "⚠️ Bu kaba bir tahmindir — proses-spesifik hesaplama yapılamamıştır",
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
```

---

### 2.2 `engine/bat_references.py` (~200 satır)

BAT referans veritabanı. Statik Python dict — ileride DB'ye taşınabilir.

```python
"""
BAT (Best Available Technology) Referans Veritabanı.

Her proses tipi ve alt kategorisi için:
- Spesifik exergy tüketimi (kWh/birim)
- Exergy verimi (%)
- Teknoloji açıklaması
- Kaynak referansı

Kaynaklar: EU BREF dokümanları, DOE Best Practices, akademik literatür.
Bu değerler Brief 0 (Knowledge Base) araştırmasıyla doğrulanmalıdır.
"""

BAT_REFERENCES: dict[str, dict[str, dict]] = {
    "drying": {
        "food_grain": {
            "label": "Tahıl Kurutma",
            "specific_exergy_kwh_per_unit": 0.18,
            "unit": "kWh/kg su",
            "exergy_efficiency_pct": 35,
            "technology": "Isı pompalı kurutucu + atık ısı geri kazanımı",
            "source": "EU BREF Food, Drink and Milk Industries (2019)",
        },
        "food_spray": {
            "label": "Sprey Kurutma",
            "specific_exergy_kwh_per_unit": 0.25,
            "unit": "kWh/kg su",
            "exergy_efficiency_pct": 28,
            "technology": "Çok kademeli sprey + egzoz geri devir",
            "source": "Mujumdar, Handbook of Industrial Drying (2020)",
        },
        "wood_lumber": {
            "label": "Kereste Kurutma",
            "specific_exergy_kwh_per_unit": 0.30,
            "unit": "kWh/kg su",
            "exergy_efficiency_pct": 25,
            "technology": "Vakumlu kurutma + güneş ön kurutma",
            "source": "EU BREF Wood-based Panels (2015)",
        },
        "general": {
            "label": "Genel Kurutma",
            "specific_exergy_kwh_per_unit": 0.22,
            "unit": "kWh/kg su",
            "exergy_efficiency_pct": 30,
            "technology": "Isı pompalı kurutucu + rejeneratif ısı değişimi",
            "source": "Kemp, Pinch Analysis and Process Integration (2007)",
        },
    },
    # ... Tüm proses tipleri aynı yapıda
    # Heating, cooling, steam_generation, compressed_air, chp, cold_storage, general_manufacturing
    # (Önceki brief'teki yapı aynen kullanılacak — burada kısaltıyorum)
}


def get_bat_reference(process_type: str, subcategory: str = "general") -> dict:
    """BAT referansını döndürür. Bulunamazsa 'general' alt kategoriye fallback."""
    type_refs = BAT_REFERENCES.get(process_type, {})
    ref = type_refs.get(subcategory) or type_refs.get("general")
    if not ref:
        raise ValueError(f"BAT referansı bulunamadı: {process_type}/{subcategory}")
    return ref


def get_available_subcategories(process_type: str) -> list[dict]:
    """Bir proses tipi için mevcut alt kategorileri listeler."""
    type_refs = BAT_REFERENCES.get(process_type, {})
    return [
        {"key": key, "label": ref["label"], "source": ref.get("source", "")}
        for key, ref in type_refs.items()
    ]


def calculate_bat_exergy(process_def, min_exergy_result: dict) -> dict:
    """
    BAT referansından proses ölçeğinde BAT exergy tüketimini hesaplar.
    
    BAT exergy = production_rate × BAT_specific_exergy
    """
    bat_ref = get_bat_reference(process_def.process_type, process_def.subcategory)
    production_rate = min_exergy_result.get("production_rate_unit", 0)
    bat_specific = bat_ref["specific_exergy_kwh_per_unit"]
    
    # Birim dönüşümü: production_rate [unit/h] × specific [kWh/unit] = kW
    bat_exergy_kW = production_rate * bat_specific
    
    return {
        "bat_exergy_kW": round(bat_exergy_kW, 2),
        "bat_specific": bat_specific,
        "bat_unit": bat_ref["unit"],
        "bat_efficiency_pct": bat_ref["exergy_efficiency_pct"],
        "bat_technology": bat_ref["technology"],
        "bat_source": bat_ref["source"],
        "bat_label": bat_ref["label"],
    }
```

**ÖNEMLİ:** BAT_REFERENCES dict'indeki tüm proses tipleri için tam değerleri yaz. Önceki brief'teki değerleri kullan ama web araştırmasıyla doğrula. `bat_references.py` dosyasının içeriği eksiksiz olmalı — tüm proses tipleri ve alt kategorileri dahil.

---

### 2.3 `engine/gap_analysis.py` (~350 satır)

```python
"""
Exergetic Gap Analysis — Top-down proses analizi.

Proses tanımı + ekipman analiz sonuçlarını birleştirerek
3 katmanlı exergetic gap analizi yapar:

1. Termodinamik Minimum (ideal, tersinir proses)
2. BAT (Best Available Technology) referansı
3. Mevcut Tesis (actual) — factory aggregates'ten

Referans: Tsatsaronis & Moung-Ho Park, "On Avoidable and Unavoidable 
Exergy Destructions", Energy, 2002
"""

from dataclasses import dataclass, field


@dataclass
class GapAnalysisResult:
    """Top-down gap analizi sonucu."""
    
    # Proses bilgisi
    process_type: str
    process_label: str
    subcategory: str
    
    # 3 katman (kW)
    minimum_exergy_kW: float
    bat_exergy_kW: float
    actual_exergy_kW: float
    
    # Gap hesaplamaları (kW)
    total_gap_kW: float              # actual - minimum
    bat_gap_kW: float                # actual - BAT (gerçekçi iyileştirme)
    technology_gap_kW: float         # BAT - minimum (teknoloji limiti)
    
    # Yüzdesel
    total_gap_pct: float             # total_gap / actual × 100
    bat_gap_pct: float               # bat_gap / actual × 100
    technology_gap_pct: float        # technology_gap / actual × 100
    
    # Spesifik tüketim
    specific_actual: float           # kWh/birim (mevcut)
    specific_bat: float              # kWh/birim (BAT)
    specific_minimum: float          # kWh/birim (ideal)
    specific_unit: str               # "kWh/kg su", "kWh/m³", vb.
    
    # Ratio
    actual_to_minimum_ratio: float   # actual / minimum (idealin kaç katı)
    actual_to_bat_ratio: float       # actual / BAT (BAT'ın kaç katı)
    
    # Gap dağılımı (ekipman bazlı)
    gap_distribution: list[dict]     # [{name, type, destroyed_kW, gap_share_pct, priority}, ...]
    
    # Ekonomik etki
    annual_total_gap_cost_eur: float
    annual_bat_gap_cost_eur: float
    energy_price_eur_kwh: float
    operating_hours: float
    
    # BAT bilgisi
    bat_technology: str
    bat_source: str
    bat_efficiency_pct: float
    
    # Sürdürülebilirlik skoru
    exergetic_sustainability_index: float  # minimum / actual (0-1)
    grade: str                             # A-F
    grade_description: str                 # "Dünya lideri" / "Kritik" / ...
    
    # Hesaplama detayları
    min_exergy_method: str
    min_exergy_assumptions: list[str]
    
    # Görselleştirme verisi (Plotly formatı)
    waterfall_data: dict
    comparison_bar_data: dict
    gap_pie_data: dict
    
    def to_dict(self) -> dict:
        """JSON serializable dict döndürür (DB'ye kaydetmek için)."""
        # dataclass fields → dict
        import dataclasses
        return dataclasses.asdict(self)


def analyze_gap(
    process_def,               # ProcessDefinition
    equipment_results: list,   # Ekipman analiz sonuçları (list of dicts from factory aggregates)
    aggregates: dict,          # Factory aggregates (mevcut pipeline çıktısı)
    hotspots: list,            # Factory hotspots (mevcut pipeline çıktısı)
    T0_K: float = 298.15,
    energy_price_eur_kwh: float = 0.08,
    operating_hours: float = 6000,
) -> GapAnalysisResult:
    """
    Ana gap analysis fonksiyonu.
    
    Adımlar:
    1. Minimum exergy hesapla (process_exergy.py)
    2. BAT exergy hesapla (bat_references.py)
    3. Mevcut exergy'yi aggregates'ten al
    4. Gap'leri hesapla
    5. Gap dağılımını ekipman bazlı çıkar
    6. ESI skoru hesapla
    7. Ekonomik etki hesapla
    8. Görselleştirme verisi üret
    """
    from engine.process_exergy import calculate_minimum_exergy
    from engine.bat_references import calculate_bat_exergy
    
    # Adım 1: Minimum exergy
    min_result = calculate_minimum_exergy(process_def, T0_K)
    minimum_kW = min_result["minimum_exergy_kW"]
    
    # Adım 2: BAT exergy
    bat_result = calculate_bat_exergy(process_def, min_result)
    bat_kW = bat_result["bat_exergy_kW"]
    
    # Adım 3: Mevcut exergy (factory aggregates'ten)
    # aggregates yapısı: {"total_fuel_exergy_kW": ..., "total_destroyed_kW": ..., ...}
    actual_kW = aggregates.get("total_fuel_exergy_kW", 0) or aggregates.get("total_input_exergy_kW", 0)
    
    # Eğer actual 0 ise veya minimum'dan küçükse — hata durumu
    if actual_kW <= 0:
        actual_kW = sum(
            eq.get("fuel_exergy_kW", 0) or eq.get("exergy_input_kW", 0)
            for eq in equipment_results
        )
    
    # Minimum ve BAT'ın actual'dan büyük olmadığından emin ol
    if bat_kW >= actual_kW:
        bat_kW = actual_kW * 0.7  # Fallback: mevcut'un %70'i
    if minimum_kW >= bat_kW:
        minimum_kW = bat_kW * 0.3  # Fallback: BAT'ın %30'u
    
    # Adım 4: Gap hesaplamaları
    total_gap = actual_kW - minimum_kW
    bat_gap = actual_kW - bat_kW
    tech_gap = bat_kW - minimum_kW
    
    total_gap_pct = (total_gap / actual_kW * 100) if actual_kW > 0 else 0
    bat_gap_pct = (bat_gap / actual_kW * 100) if actual_kW > 0 else 0
    tech_gap_pct = (tech_gap / actual_kW * 100) if actual_kW > 0 else 0
    
    # Spesifik tüketim
    production_rate = min_result.get("production_rate_unit", 1) or 1
    specific_actual = actual_kW / production_rate if production_rate > 0 else 0
    
    # Ratio
    ratio_to_min = actual_kW / minimum_kW if minimum_kW > 0 else float('inf')
    ratio_to_bat = actual_kW / bat_kW if bat_kW > 0 else float('inf')
    
    # Adım 5: Gap dağılımı
    gap_dist = _calculate_gap_distribution(equipment_results, hotspots)
    
    # Adım 6: ESI skoru
    esi, grade, grade_desc = _calculate_sustainability_index(minimum_kW, actual_kW)
    
    # Adım 7: Ekonomik etki
    annual_total = total_gap * energy_price_eur_kwh * operating_hours
    annual_bat = bat_gap * energy_price_eur_kwh * operating_hours
    
    # Adım 8: Görselleştirme verisi
    waterfall = _build_waterfall_data(minimum_kW, bat_kW, actual_kW, tech_gap, gap_dist)
    comparison = _build_comparison_bar_data(minimum_kW, bat_kW, actual_kW)
    pie = _build_gap_pie_data(gap_dist)
    
    return GapAnalysisResult(
        process_type=process_def.process_type,
        process_label=process_def.process_label,
        subcategory=process_def.subcategory,
        minimum_exergy_kW=round(minimum_kW, 2),
        bat_exergy_kW=round(bat_kW, 2),
        actual_exergy_kW=round(actual_kW, 2),
        total_gap_kW=round(total_gap, 2),
        bat_gap_kW=round(bat_gap, 2),
        technology_gap_kW=round(tech_gap, 2),
        total_gap_pct=round(total_gap_pct, 1),
        bat_gap_pct=round(bat_gap_pct, 1),
        technology_gap_pct=round(tech_gap_pct, 1),
        specific_actual=round(specific_actual, 4),
        specific_bat=bat_result["bat_specific"],
        specific_minimum=min_result["specific_minimum"],
        specific_unit=min_result["specific_unit"],
        actual_to_minimum_ratio=round(ratio_to_min, 1),
        actual_to_bat_ratio=round(ratio_to_bat, 1),
        gap_distribution=gap_dist,
        annual_total_gap_cost_eur=round(annual_total, 0),
        annual_bat_gap_cost_eur=round(annual_bat, 0),
        energy_price_eur_kwh=energy_price_eur_kwh,
        operating_hours=operating_hours,
        bat_technology=bat_result["bat_technology"],
        bat_source=bat_result["bat_source"],
        bat_efficiency_pct=bat_result["bat_efficiency_pct"],
        exergetic_sustainability_index=esi,
        grade=grade,
        grade_description=grade_desc,
        min_exergy_method=min_result["calculation_method"],
        min_exergy_assumptions=min_result["assumptions"],
        waterfall_data=waterfall,
        comparison_bar_data=comparison,
        gap_pie_data=pie,
    )


def _calculate_gap_distribution(equipment_results: list, hotspots: list) -> list[dict]:
    """Ekipman bazlı gap dağılımı. Hotspots zaten sıralı."""
    total_destroyed = sum(
        eq.get("exergy_destroyed_kW", 0) or eq.get("destroyed_kW", 0)
        for eq in equipment_results
    )
    
    if total_destroyed <= 0:
        return []
    
    distribution = []
    cumulative = 0
    for eq in sorted(equipment_results, 
                     key=lambda x: x.get("exergy_destroyed_kW", 0) or x.get("destroyed_kW", 0),
                     reverse=True):
        destroyed = eq.get("exergy_destroyed_kW", 0) or eq.get("destroyed_kW", 0)
        share = (destroyed / total_destroyed * 100) if total_destroyed > 0 else 0
        cumulative += share
        
        if share < 0.5:  # %0.5'ten küçük olanları atla
            continue
            
        priority = (
            "critical" if share > 30 else
            "high" if share > 15 else
            "medium" if share > 5 else
            "low"
        )
        
        distribution.append({
            "equipment_name": eq.get("name", "Bilinmeyen"),
            "equipment_type": eq.get("equipment_type", "unknown"),
            "destroyed_kW": round(destroyed, 2),
            "gap_share_pct": round(share, 1),
            "cumulative_pct": round(cumulative, 1),
            "priority": priority,
        })
    
    return distribution


def _calculate_sustainability_index(minimum_kW: float, actual_kW: float) -> tuple[float, str, str]:
    """
    Exergetic Sustainability Index.
    ESI = minimum / actual (0-1)
    """
    if actual_kW <= 0 or minimum_kW <= 0:
        return 0.0, "F", "Hesaplanamadı"
    
    esi = minimum_kW / actual_kW
    esi = min(1.0, max(0.0, esi))
    
    grades = [
        (0.50, "A", "Dünya lideri seviyesi"),
        (0.35, "B", "Çok iyi performans"),
        (0.20, "C", "İyi performans"),
        (0.10, "D", "Ortalama"),
        (0.05, "E", "Zayıf — iyileştirme gerekli"),
        (0.00, "F", "Kritik — büyük dönüşüm gerekli"),
    ]
    
    for threshold, grade, desc in grades:
        if esi >= threshold:
            return round(esi, 4), grade, desc
    
    return round(esi, 4), "F", "Kritik"


def _build_waterfall_data(min_kW, bat_kW, actual_kW, tech_gap, gap_dist) -> dict:
    """Plotly waterfall chart verisi."""
    labels = ["Minimum"]
    values = [min_kW]
    types = ["absolute"]
    
    # Teknoloji limiti
    labels.append("Teknoloji Limiti")
    values.append(tech_gap)
    types.append("relative")
    
    # Top 5 ekipman gap
    for eq in gap_dist[:5]:
        labels.append(eq["equipment_name"])
        values.append(eq["destroyed_kW"])
        types.append("relative")
    
    # Toplam
    labels.append("Mevcut Tesis")
    values.append(actual_kW)
    types.append("total")
    
    return {
        "labels": labels,
        "values": [round(v, 1) for v in values],
        "types": types,
    }


def _build_comparison_bar_data(min_kW, bat_kW, actual_kW) -> dict:
    """3 katman bar chart verisi."""
    return {
        "categories": ["Termodinamik\nMinimum", "BAT\nReferans", "Mevcut\nTesis"],
        "values": [round(min_kW, 1), round(bat_kW, 1), round(actual_kW, 1)],
        "colors": ["#10B981", "#F59E0B", "#EF4444"],
    }


def _build_gap_pie_data(gap_dist) -> dict:
    """Gap dağılımı donut chart verisi."""
    labels = [eq["equipment_name"] for eq in gap_dist[:7]]
    values = [eq["destroyed_kW"] for eq in gap_dist[:7]]
    
    # Geri kalanı "Diğer" olarak topla
    if len(gap_dist) > 7:
        labels.append("Diğer")
        values.append(sum(eq["destroyed_kW"] for eq in gap_dist[7:]))
    
    return {"labels": labels, "values": [round(v, 1) for v in values]}
```

---

## 3. Veritabanı Değişiklikleri

### 3.1 `api/database/models.py` — FactoryProject modeli

Mevcut modele yeni alanlar ekle (tümü nullable — geriye uyumlu):

```python
# FactoryProject modeline eklenecek alanlar:
process_type = Column(String, nullable=True)           # "drying", "heating", vb.
process_label = Column(String, nullable=True)          # Kullanıcı açıklaması
process_parameters = Column(JSON, nullable=True)       # Proses parametreleri dict
process_subcategory = Column(String, nullable=True)    # BAT alt kategori
operating_hours = Column(Float, nullable=True, default=6000)
energy_price_eur_kwh = Column(Float, nullable=True, default=0.08)
```

### 3.2 `api/database/models.py` — FactoryAnalysis modeli

```python
# FactoryAnalysis modeline eklenecek alan:
gap_analysis = Column(JSON, nullable=True)     # GapAnalysisResult.to_dict()
```

### 3.3 DB Migration

Alembic migration yazılacak. Mevcut veriler etkilenmemeli — tüm yeni alanlar nullable.

---

## 4. API Değişiklikleri

### 4.1 Schema Güncellemeleri (`api/schemas/factory.py`)

```python
class CreateProjectRequest(BaseModel):
    name: str
    sector: str
    description: Optional[str] = None
    # YENİ
    process_type: Optional[str] = None
    process_label: Optional[str] = None
    process_parameters: Optional[dict] = None
    process_subcategory: Optional[str] = None
    operating_hours: Optional[float] = 6000
    energy_price_eur_kwh: Optional[float] = 0.08

class UpdateProcessRequest(BaseModel):
    """Mevcut projeye proses tanımı ekleme/güncelleme."""
    process_type: str
    process_label: str
    process_parameters: dict
    process_subcategory: Optional[str] = "general"
    operating_hours: Optional[float] = 6000
    energy_price_eur_kwh: Optional[float] = 0.08
```

### 4.2 Yeni Endpointler (`api/routes/factory.py`)

```python
@router.get("/api/process-types")
async def get_process_types():
    """Tüm desteklenen proses tiplerini döndürür."""
    from engine.process_exergy import get_process_types
    return get_process_types()

@router.get("/api/process-types/{process_type}/subcategories")
async def get_subcategories(process_type: str):
    """Bir proses tipi için BAT alt kategorilerini döndürür."""
    from engine.bat_references import get_available_subcategories
    return get_available_subcategories(process_type)

@router.put("/api/factory/projects/{project_id}/process")
async def update_process_definition(project_id: str, req: UpdateProcessRequest, ...):
    """Mevcut projenin proses tanımını günceller."""
    # Projeyi bul, process alanlarını güncelle, kaydet
    pass
```

### 4.3 Factory Analyze Endpoint Güncellemesi

Mevcut `/api/factory/projects/{project_id}/analyze` endpointine:

```python
# Mevcut pipeline çalıştıktan sonra, eğer proses tanımı varsa:
if project.process_type:
    from engine.process_exergy import ProcessDefinition
    from engine.gap_analysis import analyze_gap
    
    process_def = ProcessDefinition(
        process_type=project.process_type,
        process_label=project.process_label or "",
        parameters=project.process_parameters or {},
        subcategory=project.process_subcategory or "general",
        operating_hours=project.operating_hours or 6000,
        energy_price_eur_kwh=project.energy_price_eur_kwh or 0.08,
    )
    
    gap_result = analyze_gap(
        process_def=process_def,
        equipment_results=valid_results,
        aggregates=aggregates,
        hotspots=hotspots,
        energy_price_eur_kwh=process_def.energy_price_eur_kwh,
        operating_hours=process_def.operating_hours,
    )
    
    # factory_analysis kaydına gap_analysis ekle
    factory_analysis.gap_analysis = gap_result.to_dict()
```

---

## 5. Test Gereksinimleri

### 5.1 `tests/test_process_exergy.py`

```python
# Her proses tipi için minimum exergy hesaplama testleri

class TestMinExergyDrying:
    def test_basic_drying(self):
        """1000 kg/h, %20→%5 nem: minimum exergy > 0"""
    
    def test_no_drying_needed(self):
        """moisture_in <= moisture_out: exergy = 0"""
    
    def test_water_removed_calculation(self):
        """Uzaklaştırılan su miktarı doğru hesaplanıyor"""
    
    def test_with_heating(self):
        """Malzeme ısıtma ek exergy ekliyor"""

class TestMinExergyHeating:
    def test_carnot_factor(self):
        """20°C→80°C su ısıtma: Carnot faktörü ve min exergy doğru"""
    
    def test_no_heating(self):
        """T_out <= T_in: exergy = 0"""

class TestMinExergyCooling:
    def test_cop_carnot(self):
        """-20°C soğutma: COP ve min exergy doğru"""
    
    def test_no_cooling(self):
        """T_cold >= T_ambient: exergy = 0"""

class TestMinExergySteam:
    def test_saturated_steam(self):
        """10 bar doymuş buhar: exergy makul aralıkta (500-1000 kJ/kg)"""
    
    def test_coolprop_fallback(self):
        """CoolProp yokken fallback çalışıyor"""

class TestMinExergyCompressedAir:
    def test_isothermal_work(self):
        """7 bar sıkıştırma: W_min = m*R*T0*ln(7) doğru"""
    
    def test_pressure_ratio(self):
        """Basınç arttıkça minimum exergy artar"""

class TestMinExergyCHP:
    def test_combined_output(self):
        """Elektrik + ısı exergisi toplamı doğru"""

class TestProcessTypes:
    def test_all_types_registered(self):
        """8 proses tipi SUPPORTED_PROCESS_TYPES'ta var"""
    
    def test_all_positive_results(self):
        """Tüm proses tipleri pozitif minimum exergy döndürür"""
    
    def test_missing_param_raises(self):
        """Eksik parametre ValueError fırlatır"""
```

### 5.2 `tests/test_bat_references.py`

```python
def test_all_process_types_have_general():
    """Her proses tipinin 'general' alt kategorisi var"""

def test_bat_values_positive():
    """Tüm BAT değerleri pozitif"""

def test_get_bat_reference_fallback():
    """Bilinmeyen alt kategori için 'general' fallback çalışıyor"""

def test_subcategories_list():
    """Alt kategoriler doğru listeleniyor"""
```

### 5.3 `tests/test_gap_analysis.py`

```python
def test_gap_hierarchy():
    """minimum < BAT < actual her zaman geçerli"""

def test_gap_percentages_sum():
    """total_gap_pct + technology_gap_pct yaklaşık 100"""

def test_gap_distribution():
    """Ekipman gap payları mantıklı ve sıralı"""

def test_sustainability_index():
    """ESI 0-1 arası, grade A-F"""

def test_economic_impact():
    """annual_cost = gap * price * hours"""

def test_no_process_returns_none():
    """Proses tanımı olmadan gap_analysis = None"""

def test_waterfall_data():
    """Waterfall chart verisi doğru yapıda"""

def test_comparison_bar_data():
    """3 değer: min, BAT, actual"""

def test_full_pipeline_integration():
    """Proses tanımlı fabrika: factory analyze → gap_analysis dolmuş"""
```

---

## 6. Çalışma Sırası

1. `engine/process_exergy.py` — ProcessDefinition + SUPPORTED_PROCESS_TYPES + 8 hesaplama fonksiyonu
2. `engine/bat_references.py` — BAT_REFERENCES tam dict + get/calculate fonksiyonları
3. `engine/gap_analysis.py` — GapAnalysisResult + analyze_gap + yardımcı fonksiyonlar
4. `engine/__init__.py` — yeni modülleri export et
5. DB migration — yeni alanlar ekle
6. API schemas + endpointler
7. `engine/factory.py` — Adım 11 ekleme (gap analysis)
8. Testler
9. Tüm mevcut testlerin hala geçtiğini doğrula

## 7. UYARILAR

1. **Frontend'e DOKUNMA** — Bu brief sadece backend
2. **knowledge/ klasörüne DOKUNMA** — Brief 0'ın işi
3. **Mevcut testler kırılmamalı** — Tüm yeni DB alanları nullable
4. **CoolProp fallback zorunlu** — CoolProp yoksa da çalışmalı
5. **actual_kW hesaplaması dikkatli** — aggregates yapısını incele, doğru alanı kullan
6. **ProcessDefinition → engine/factory.py entegrasyonu** — project.process_type varsa ProcessDefinition oluştur

---

*Bu brief ExergyLab'in gap analysis backend'ini oluşturur. Frontend Brief 2 ve 3'te yapılacak.*
