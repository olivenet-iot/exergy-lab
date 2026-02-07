"""
BAT (Best Available Technology) Referans Veritabanı.

Her proses tipi ve alt kategorisi için:
- Spesifik exergy tüketimi (kWh/birim)
- Exergy verimi (%)
- Teknoloji açıklaması
- Kaynak referansı

Kaynaklar: EU BREF dokümanları, DOE Best Practices, akademik literatür.
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
    "heating": {
        "water_low": {
            "label": "Düşük Sıcaklık Su Isıtma (<80°C)",
            "specific_exergy_kwh_per_unit": 0.015,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 45,
            "technology": "Yoğuşmalı kazan + ısı geri kazanımı + ısı pompası",
            "source": "EU BREF Energy Efficiency (2009)",
        },
        "water_high": {
            "label": "Yüksek Sıcaklık Su Isıtma (>80°C)",
            "specific_exergy_kwh_per_unit": 0.035,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 38,
            "technology": "Modüler yoğuşmalı kazan + ekonomizör",
            "source": "EU BREF Energy Efficiency (2009)",
        },
        "general": {
            "label": "Genel Isıtma",
            "specific_exergy_kwh_per_unit": 0.025,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 40,
            "technology": "Yoğuşmalı kazan + egzoz ısı geri kazanımı",
            "source": "DOE Industrial Heating Best Practices (2016)",
        },
    },
    "cooling": {
        "comfort": {
            "label": "Konfor Soğutma",
            "specific_exergy_kwh_per_unit": 0.08,
            "unit": "kWh/kWh soğutma",
            "exergy_efficiency_pct": 42,
            "technology": "Yüksek COP inverter chiller + serbest soğutma",
            "source": "EU BREF Energy Efficiency (2009)",
        },
        "process": {
            "label": "Proses Soğutma",
            "specific_exergy_kwh_per_unit": 0.12,
            "unit": "kWh/kWh soğutma",
            "exergy_efficiency_pct": 35,
            "technology": "Santrifüj chiller + değişken hız sürücü",
            "source": "ASHRAE Handbook, HVAC Systems and Equipment (2020)",
        },
        "general": {
            "label": "Genel Soğutma",
            "specific_exergy_kwh_per_unit": 0.10,
            "unit": "kWh/kWh soğutma",
            "exergy_efficiency_pct": 38,
            "technology": "Yüksek verimli chiller + optimum kule",
            "source": "DOE Best Practices for Cooling Systems (2017)",
        },
    },
    "steam_generation": {
        "industrial_low": {
            "label": "Düşük Basınç Buhar (<10 bar)",
            "specific_exergy_kwh_per_unit": 0.20,
            "unit": "kWh/kg buhar",
            "exergy_efficiency_pct": 42,
            "technology": "Yoğuşmalı kazan + ekonomizör + blowdown ısı geri kazanımı",
            "source": "EU BREF Large Combustion Plants (2017)",
        },
        "industrial_high": {
            "label": "Yüksek Basınç Buhar (>10 bar)",
            "specific_exergy_kwh_per_unit": 0.28,
            "unit": "kWh/kg buhar",
            "exergy_efficiency_pct": 48,
            "technology": "Su boru kazanı + süper ısıtıcı + çok kademeli ekonomizör",
            "source": "EU BREF Large Combustion Plants (2017)",
        },
        "general": {
            "label": "Genel Buhar Üretimi",
            "specific_exergy_kwh_per_unit": 0.24,
            "unit": "kWh/kg buhar",
            "exergy_efficiency_pct": 45,
            "technology": "Verimli buhar kazanı + ısı geri kazanım sistemi",
            "source": "DOE Steam Best Practices (2012)",
        },
    },
    "compressed_air": {
        "general": {
            "label": "Basınçlı Hava Sistemi",
            "specific_exergy_kwh_per_unit": 0.005,
            "unit": "kWh/m³",
            "exergy_efficiency_pct": 30,
            "technology": "VSD vidalı kompresör + ısı geri kazanımı + sızıntı kontrolü",
            "source": "DOE Compressed Air Challenge Best Practices (2016)",
        },
    },
    "chp": {
        "gas_turbine": {
            "label": "Gaz Türbini CHP",
            "specific_exergy_kwh_per_unit": 0.82,
            "unit": "kWh/kWh yakıt",
            "exergy_efficiency_pct": 52,
            "technology": "Ileri gaz türbini + HRSG + buhar türbini (kombine çevrim)",
            "source": "EU BREF Large Combustion Plants (2017)",
        },
        "gas_engine": {
            "label": "Gaz Motoru CHP",
            "specific_exergy_kwh_per_unit": 0.78,
            "unit": "kWh/kWh yakıt",
            "exergy_efficiency_pct": 48,
            "technology": "Yüksek verimli gaz motoru + egzoz ısı geri kazanımı",
            "source": "EPA CHP Partnership, Catalog of Technologies (2017)",
        },
        "general": {
            "label": "Genel CHP",
            "specific_exergy_kwh_per_unit": 0.80,
            "unit": "kWh/kWh yakıt",
            "exergy_efficiency_pct": 50,
            "technology": "Modern CHP sistemi + tam ısı geri kazanımı",
            "source": "IEA CHP/DHC Working Paper (2018)",
        },
    },
    "cold_storage": {
        "general": {
            "label": "Soğuk Depolama",
            "specific_exergy_kwh_per_unit": 0.12,
            "unit": "kWh/kWh soğutma",
            "exergy_efficiency_pct": 32,
            "technology": "Yüksek COP soğutma grubu + iyi yalıtım + VSD",
            "source": "EU BREF Food, Drink and Milk Industries (2019)",
        },
    },
    "general_manufacturing": {
        "cement": {
            "label": "Çimento Üretimi",
            "specific_exergy_kwh_per_unit": 0.85,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 28,
            "technology": "6 kademeli ön ısıtıcılı döner fırın + atık ısı geri kazanımı",
            "source": "EU BREF Cement, Lime and Magnesium Oxide (2013)",
        },
        "glass": {
            "label": "Cam Üretimi",
            "specific_exergy_kwh_per_unit": 1.20,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 22,
            "technology": "Oxy-fuel fırın + rejeneratif ısıtıcı",
            "source": "EU BREF Glass Manufacturing (2013)",
        },
        "paper": {
            "label": "Kağıt Üretimi",
            "specific_exergy_kwh_per_unit": 0.55,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 30,
            "technology": "Shoe press + yankee kurutucu + kapalı hood",
            "source": "EU BREF Pulp and Paper (2015)",
        },
        "sugar": {
            "label": "Şeker Üretimi",
            "specific_exergy_kwh_per_unit": 0.45,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 32,
            "technology": "Çok kademeli buharlaştırma + MVR + ısı entegrasyonu",
            "source": "EU BREF Food, Drink and Milk Industries (2019)",
        },
        "concrete": {
            "label": "Beton Üretimi",
            "specific_exergy_kwh_per_unit": 0.15,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 35,
            "technology": "Optimize beton karışım tasarımı + verimli karıştırma",
            "source": "Concrete Sustainability Report, CSI (2018)",
        },
        "general": {
            "label": "Genel Üretim",
            "specific_exergy_kwh_per_unit": 0.50,
            "unit": "kWh/kg",
            "exergy_efficiency_pct": 28,
            "technology": "Endüstriyel enerji verimliliği en iyi uygulamalar",
            "source": "IEA Energy Efficiency Indicators (2020)",
        },
    },
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
    if not type_refs:
        raise ValueError(f"Desteklenmeyen proses tipi: {process_type}")
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
