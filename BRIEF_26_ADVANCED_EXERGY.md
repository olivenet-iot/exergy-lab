# BRIEF_26: Advanced Exergy — Endojen/Eksojen (EN/EX) Dekompozisyon Motoru

> **Tarih:** 2026-02-05
> **Öncelik:** Yüksek
> **Tahmini Süre:** 4-6 saat
> **Karmaşıklık:** Yüksek
> **Bağımlılıklar:** Mevcut AV/UN ayrışımı (core.py), exergoekonomik (exergoeconomic.py), fabrika modülü (factory.py)
> **Etkilenen Dosyalar:** Yeni + mevcut toplam ~12 dosya

---

## 1. Bağlam ve Motivasyon

### 1.1 Tsatsaronis'in 4-Kadran Dekompozisyonu

ExergyLab şu an exergy yıkımını **AV/UN** (kaçınılabilir/kaçınılamaz) olarak ayırıyor. Bu tek boyutlu bir ayrışım — "ne kadarı iyileştirilebilir?" sorusuna cevap verir. Ancak Tsatsaronis'in tam metodolojisi **iki boyutlu** bir matris gerektirir:

```
                    Endojen (EN)              Eksojen (EX)
                 ┌─────────────────────┬─────────────────────┐
  Kaçınılabilir  │     AV-EN           │     AV-EX           │
  (AV)           │ BU ekipmanı         │ DİĞER ekipmanları   │
                 │ iyileştir ✅        │ iyileştir 🔄        │
                 │ (En yüksek öncelik) │                     │
                 ├─────────────────────┼─────────────────────┤
  Kaçınılamaz    │     UN-EN           │     UN-EX           │
  (UN)           │ Bu ekipmanın        │ Sistem yapısının     │
                 │ doğal sınırı 🔒    │ dayattığı sınır 🔒  │
                 └─────────────────────┴─────────────────────┘
```

**Neden önemli?**
- AV/UN tek başına "85 kW kaçınılabilir" der → ama bu 85 kW'ı azaltmak için hangi ekipmana müdahale etmeliyiz?
- EN/EX bunu cevaplar: "60 kW'ı BU kompresörün kendisinden, 25 kW'ı BU kompresörü besleyen kazanın verimsizliğinden kaynaklanıyor"
- 4-kadran, enerji yöneticisine net aksiyon planı verir

### 1.2 ExergyLab'ın Mimari Kısıtı

**Kritik tasarım kararı:** ExergyLab termodinamik çevrim simülasyonu yapmıyor. Her ekipman bağımsız olarak, kullanıcının verdiği parametrelerle analiz ediliyor. Bu, klasik EN/EX yönteminin (tüm diğer ekipmanları ideal yapıp sistemi yeniden simüle etme) doğrudan uygulanamayacağı anlamına gelir.

**Çözüm: Mühendislik yaklaşımı (Engineering Approximation)**

Tsatsaronis & Park (2002) ve Kelly et al. (2009) referanslarından uyarlanmış, fabrika ekipman listesi üzerinde çalışan bir yaklaşım:

1. **Ekipman etkileşim matrisi** — Hangi ekipmanlar birbirini etkiler?
2. **Etkileşim katsayıları** — Ne kadar etkiler?
3. **İzolasyon faktörü** — Her ekipmanın "yalnız çalışsaydı" ne kadar yıkım yaratacağı

Bu yaklaşım tam proses simülasyonu kadar hassas değildir, ancak mühendislik pratiğinde güvenilir sonuçlar verir ve ExergyLab'ın "her ekipman bağımsız" mimarisine uyar.

### 1.3 Knowledge Base

`knowledge/factory/advanced_exergy/` dizininde ~18 dosya mevcut. Uygulama koşulu: **3+ ekipman, I_total > 100 kW**.

---

## 2. Teori — EN/EX Dekompozisyon

### 2.1 Temel Tanımlar

```
I_k       = Ekipman k'nın toplam exergy yıkımı (kW)
I_k^EN    = Endojen yıkım: k'nın kendi iç tersinmezliklerinden kaynaklanan kısım
I_k^EX    = Eksojen yıkım: diğer ekipmanların verimsizliğinden kaynaklanan kısım

Temel ilişki: I_k = I_k^EN + I_k^EX
```

### 2.2 Endojen Yıkım Hesabı

Tam yöntem (proses simülasyonu ile):
```
I_k^EN = I_k(tüm diğer ekipmanlar ideal, k gerçek)
```

ExergyLab yaklaşımı (izolasyon faktörü ile):
```
I_k^EN = I_k × φ_k

φ_k = izolasyon faktörü (0 < φ_k ≤ 1)
    = ekipmanın yıkımının ne kadarının kendi iç verimsizliğinden kaynaklandığını gösteren oran

φ_k hesabı:
  1. Baz değer: ekipman tipine özel varsayılan φ₀ (literatürden)
  2. Etkileşim düzeltmesi: bağlı ekipmanların verimlilik sapmasına göre düzelt

φ_k = φ₀_k × (1 - Σⱼ αₖⱼ × δⱼ)

Burada:
  φ₀_k   = ekipman tipi k'nın taban izolasyon faktörü
  αₖⱼ    = ekipman j'nin ekipman k üzerindeki etkileşim katsayısı
  δⱼ     = ekipman j'nin referans verimden sapması: (η_ref_j - η_actual_j) / η_ref_j
```

### 2.3 İzolasyon Faktörleri (Literatür Referansları)

| Ekipman Tipi | φ₀ (taban) | Açıklama | Referans |
|-------------|-----------|----------|----------|
| Kompresör | 0.75 | Çoğunlukla kendi verimsizliği (izentropik kayıplar) | Tsatsaronis 2002 |
| Kazan | 0.80 | Yanma tersinmezliği büyük oranda endojen | Cziesla et al. 2006 |
| Chiller | 0.65 | Kondenser/evaporatör koşulları dış etkilere duyarlı | Morosuk & Tsatsaronis 2009 |
| Pompa | 0.85 | Hidrolik kayıplar büyük oranda endojen | Kelly et al. 2009 |
| Isı Eşanjörü | 0.55 | ΔT sıcaklık farkı her iki tarafa da bağlı — güçlü eksojen | Petrakopoulou et al. 2012 |
| Buhar Türbini | 0.70 | İzentropik verim endojen, ama giriş koşulları kazana bağlı | Tsatsaronis & Morosuk 2010 |
| Kurutma Fırını | 0.60 | Kurutma havası koşulları dış ısıtmaya bağlı | Erbay & Hepbasli 2014 |

### 2.4 Etkileşim Katsayıları Matrisi

Hangi ekipman hangisini ne kadar etkiler:

```python
# INTERACTION_COEFFICIENTS[affected][affecting] = α
# "affected" ekipmanının yıkımı, "affecting" ekipmanının verimsizliğinden ne kadar etkilenir

INTERACTION_COEFFICIENTS = {
    "compressor": {
        "heat_exchanger": 0.10,  # Aftercooler koşulları
        "chiller": 0.05,        # Soğutma sistemi
    },
    "boiler": {
        "pump": 0.05,           # Besleme suyu pompası
        "heat_exchanger": 0.08, # Economizer/preheater
    },
    "chiller": {
        "heat_exchanger": 0.12, # Kondenser/evaporatör HX
        "pump": 0.08,           # Soğutma suyu pompası
        "compressor": 0.05,     # Soğutucu kompresör
    },
    "pump": {
        "heat_exchanger": 0.05, # Boru hattı basınç düşümü
    },
    "heat_exchanger": {
        "boiler": 0.15,         # Sıcak akışkan koşulları
        "compressor": 0.10,     # Sıcak gaz koşulları
        "chiller": 0.10,        # Soğuk akışkan koşulları
        "steam_turbine": 0.10,  # Çıkış buharı koşulları
        "dryer": 0.08,          # Egzoz koşulları
    },
    "steam_turbine": {
        "boiler": 0.20,         # Giriş buharı koşulları (GÜÇLÜ bağımlılık)
        "pump": 0.05,           # Kondens pompası
    },
    "dryer": {
        "boiler": 0.15,         # Isıtma kaynağı
        "heat_exchanger": 0.10, # Hava ön ısıtma
        "steam_turbine": 0.08,  # Proses buharı kaynağı
    },
}
```

### 2.5 Referans Verimlilikler

Her ekipman tipi için "iyi çalışan" referans verim (δⱼ hesabında kullanılır):

```python
REFERENCE_EFFICIENCIES = {
    "compressor": {
        "screw": 0.80,
        "screw_oilfree": 0.75,
        "piston": 0.78,
        "scroll": 0.76,
        "centrifugal": 0.85,
        "roots": 0.65,
        "_default": 0.80,
    },
    "boiler": {
        "steam_firetube": 0.82,
        "steam_watertube": 0.85,
        "condensing": 0.95,
        "waste_heat": 0.70,
        "electric": 0.35,
        "biomass": 0.75,
        "_default": 0.82,
    },
    "chiller": {
        "screw": 0.40,
        "centrifugal": 0.45,
        "absorption": 0.25,
        "air_cooled": 0.35,
        "water_cooled": 0.42,
        "_default": 0.40,
    },
    "pump": {
        "centrifugal": 0.80,
        "positive_displacement": 0.75,
        "submersible": 0.70,
        "_default": 0.78,
    },
    "heat_exchanger": {
        "shell_tube": 0.75,
        "plate": 0.85,
        "air_cooled": 0.60,
        "double_pipe": 0.70,
        "economizer": 0.72,
        "_default": 0.75,
    },
    "steam_turbine": {
        "back_pressure": 0.78,
        "condensing": 0.82,
        "extraction": 0.76,
        "orc": 0.70,
        "micro_turbine": 0.65,
        "_default": 0.78,
    },
    "dryer": {
        "convective": 0.45,
        "rotary": 0.50,
        "fluidized_bed": 0.55,
        "spray": 0.40,
        "heat_pump": 0.65,
        "_default": 0.45,
    },
}
```

### 2.6 4-Kadran Dekompozisyon

AV/UN (mevcut) + EN/EX (yeni) birleşimi:

```
I_k^AV-EN = I_k^AV × φ_k
I_k^AV-EX = I_k^AV × (1 - φ_k)
I_k^UN-EN = I_k^UN × φ_k
I_k^UN-EX = I_k^UN × (1 - φ_k)

Doğrulama: I_k^AV-EN + I_k^AV-EX + I_k^UN-EN + I_k^UN-EX = I_k
```

### 2.7 Fabrika Seviyesi Metrikler

```
Toplam endojen yıkım:   I_total^EN = Σ_k I_k^EN
Toplam eksojen yıkım:   I_total^EX = Σ_k I_k^EX
Endojen oran:            ratio_EN = I_total^EN / I_total × 100

Etkileşim yoğunluğu:    interaction_density = I_total^EX / I_total
  → Yüksek: sistem entegrasyonu güçlü, ekipmanlar birbirini çok etkiliyor
  → Düşük: ekipmanlar bağımsız çalışıyor

Öncelik sıralaması (AV-EN büyükten küçüğe):
  → Bu sıralama, hangi ekipmana ÖNCE müdahale edilmesi gerektiğini gösterir
```

---

## 3. Engine Modülü: `engine/advanced_exergy.py`

### 3.1 Dosya Yapısı

Tahmini boyut: **~450-550 satır**

```python
"""
ExergyLab İleri Exergy Analizi — EN/EX Dekompozisyon Motoru

Tsatsaronis'in 4-kadran dekompozisyonu:
  - Endojen (EN): Ekipmanın kendi iç tersinmezlikleri
  - Eksojen (EX): Diğer ekipmanların etkisinden kaynaklanan tersinmezlikler
  - AV/UN ile birleşik: AV-EN, AV-EX, UN-EN, UN-EX

Mimari:
  ExergyLab proses simülasyonu yapmadığı için, izolasyon faktörü (φ) ve
  etkileşim katsayıları (α) kullanılarak mühendislik yaklaşımı uygulanır.
  
Referanslar:
  - Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable
    exergy destructions and investment costs..."
  - Kelly, S., Tsatsaronis, G., & Morosuk, T. (2009). "Advanced exergetic
    analysis: Approaches for splitting..."
  - Petrakopoulou, F. et al. (2012). "Conventional and advanced exergetic
    analyses applied to a combined cycle power plant"
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
import logging

logger = logging.getLogger(__name__)
```

### 3.2 Veri Yapıları

```python
@dataclass
class AdvancedExergyEquipmentResult:
    """Tek ekipman için ileri exergy analizi sonucu."""
    equipment_id: str
    equipment_name: str
    equipment_type: str
    subtype: str
    
    # Toplam yıkım (mevcut analiz sonuçlarından)
    exergy_destroyed_kW: float
    exergy_efficiency_pct: float
    
    # AV/UN (mevcut)
    I_avoidable_kW: float
    I_unavoidable_kW: float
    
    # EN/EX (YENİ)
    I_endogenous_kW: float          # Endojen yıkım
    I_exogenous_kW: float           # Eksojen yıkım
    isolation_factor: float          # φ_k (0-1)
    
    # 4-Kadran (YENİ)
    I_AV_EN_kW: float               # Kaçınılabilir + Endojen → BU ekipmanı iyileştir
    I_AV_EX_kW: float               # Kaçınılabilir + Eksojen → DİĞER ekipmanları iyileştir
    I_UN_EN_kW: float               # Kaçınılamaz + Endojen → Doğal sınır
    I_UN_EX_kW: float               # Kaçınılamaz + Eksojen → Sistem sınırı
    
    # Etkileşim detayları
    exogenous_sources: List[Dict]    # Hangi ekipmanlardan ne kadar eksojen yıkım geliyor
    # [{"source_id": "...", "source_name": "...", "source_type": "...", 
    #   "contribution_kW": float, "contribution_pct": float}]
    
    # Öncelik metrikleri
    improvement_priority: str        # "high", "medium", "low"
    priority_reason: str             # Kısa açıklama
    
    def to_dict(self) -> dict:
        """JSON serializasyonu."""
        return {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "subtype": self.subtype,
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "I_avoidable_kW": round(self.I_avoidable_kW, 2),
            "I_unavoidable_kW": round(self.I_unavoidable_kW, 2),
            "I_endogenous_kW": round(self.I_endogenous_kW, 2),
            "I_exogenous_kW": round(self.I_exogenous_kW, 2),
            "isolation_factor": round(self.isolation_factor, 3),
            "I_AV_EN_kW": round(self.I_AV_EN_kW, 2),
            "I_AV_EX_kW": round(self.I_AV_EX_kW, 2),
            "I_UN_EN_kW": round(self.I_UN_EN_kW, 2),
            "I_UN_EX_kW": round(self.I_UN_EX_kW, 2),
            "exogenous_sources": self.exogenous_sources,
            "improvement_priority": self.improvement_priority,
            "priority_reason": self.priority_reason,
        }


@dataclass
class AdvancedExergyResult:
    """Fabrika seviyesi ileri exergy analizi sonucu."""
    # Genel bilgi
    num_equipment: int
    total_exergy_destroyed_kW: float
    
    # EN/EX toplam
    total_endogenous_kW: float
    total_exogenous_kW: float
    endogenous_ratio_pct: float      # I_EN / I_total × 100
    
    # 4-Kadran toplam
    total_AV_EN_kW: float
    total_AV_EX_kW: float
    total_UN_EN_kW: float
    total_UN_EX_kW: float
    
    # Etkileşim metrikleri
    interaction_density: float        # I_EX / I_total (0-1)
    most_influential_equipment: str   # En çok eksojen yıkım yaratan ekipman
    most_affected_equipment: str      # En çok eksojen yıkıma maruz kalan ekipman
    
    # Ekipman bazlı sonuçlar
    equipment_results: List[AdvancedExergyEquipmentResult]
    
    # Öncelik sıralaması (AV-EN bazlı)
    priority_ranking: List[Dict]     # [{id, name, type, I_AV_EN_kW, priority}]
    
    # Etkileşim ağı (Sankey veya graph görselleştirme için)
    interaction_network: List[Dict]  # [{source, target, value_kW}]
    
    # Görselleştirme verileri
    quadrant_chart_data: Dict        # 4-kadran stacked bar chart verisi
    
    # Uyarılar
    warnings: List[str]
    
    is_valid: bool = True
    error_message: str = ""
    
    def to_dict(self) -> dict:
        """JSON serializasyonu."""
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "num_equipment": self.num_equipment,
            "total_exergy_destroyed_kW": round(self.total_exergy_destroyed_kW, 2),
            "total_endogenous_kW": round(self.total_endogenous_kW, 2),
            "total_exogenous_kW": round(self.total_exogenous_kW, 2),
            "endogenous_ratio_pct": round(self.endogenous_ratio_pct, 1),
            "total_AV_EN_kW": round(self.total_AV_EN_kW, 2),
            "total_AV_EX_kW": round(self.total_AV_EX_kW, 2),
            "total_UN_EN_kW": round(self.total_UN_EN_kW, 2),
            "total_UN_EX_kW": round(self.total_UN_EX_kW, 2),
            "interaction_density": round(self.interaction_density, 3),
            "most_influential_equipment": self.most_influential_equipment,
            "most_affected_equipment": self.most_affected_equipment,
            "equipment_results": [r.to_dict() for r in self.equipment_results],
            "priority_ranking": self.priority_ranking,
            "interaction_network": self.interaction_network,
            "quadrant_chart_data": self.quadrant_chart_data,
            "warnings": self.warnings,
        }
```

### 3.3 Sabit Veriler

```python
# --- Taban İzolasyon Faktörleri ---
BASE_ISOLATION_FACTORS: Dict[str, float] = {
    "compressor": 0.75,
    "boiler": 0.80,
    "chiller": 0.65,
    "pump": 0.85,
    "heat_exchanger": 0.55,
    "steam_turbine": 0.70,
    "dryer": 0.60,
}

# --- Etkileşim Katsayıları Matrisi ---
# INTERACTION_COEFFICIENTS[affected_type][affecting_type] = α
INTERACTION_COEFFICIENTS: Dict[str, Dict[str, float]] = {
    "compressor": {
        "heat_exchanger": 0.10,
        "chiller": 0.05,
    },
    "boiler": {
        "pump": 0.05,
        "heat_exchanger": 0.08,
    },
    "chiller": {
        "heat_exchanger": 0.12,
        "pump": 0.08,
        "compressor": 0.05,
    },
    "pump": {
        "heat_exchanger": 0.05,
    },
    "heat_exchanger": {
        "boiler": 0.15,
        "compressor": 0.10,
        "chiller": 0.10,
        "steam_turbine": 0.10,
        "dryer": 0.08,
    },
    "steam_turbine": {
        "boiler": 0.20,
        "pump": 0.05,
    },
    "dryer": {
        "boiler": 0.15,
        "heat_exchanger": 0.10,
        "steam_turbine": 0.08,
    },
}

# --- Referans Verimlilikleri (exergy bazlı) ---
# Her alt tip için "iyi çalışan" referans exergy verimi
REFERENCE_EFFICIENCIES: Dict[str, Dict[str, float]] = {
    "compressor": {
        "screw": 0.80, "screw_oilfree": 0.75, "piston": 0.78,
        "scroll": 0.76, "centrifugal": 0.85, "roots": 0.65,
        "_default": 0.80,
    },
    "boiler": {
        "steam_firetube": 0.82, "steam_watertube": 0.85,
        "hotwater": 0.80, "condensing": 0.95, "waste_heat": 0.70,
        "electric": 0.35, "biomass": 0.75,
        "_default": 0.82,
    },
    "chiller": {
        "screw": 0.40, "centrifugal": 0.45, "scroll": 0.38,
        "reciprocating": 0.35, "absorption": 0.25,
        "air_cooled": 0.35, "water_cooled": 0.42,
        "_default": 0.40,
    },
    "pump": {
        "centrifugal": 0.80, "positive_displacement": 0.75,
        "submersible": 0.70, "vertical_turbine": 0.78,
        "booster": 0.72, "vacuum": 0.65,
        "_default": 0.78,
    },
    "heat_exchanger": {
        "shell_tube": 0.75, "plate": 0.85, "air_cooled": 0.60,
        "double_pipe": 0.70, "spiral": 0.78,
        "economizer": 0.72, "recuperator": 0.74,
        "_default": 0.75,
    },
    "steam_turbine": {
        "back_pressure": 0.78, "condensing": 0.82,
        "extraction": 0.76, "orc": 0.70, "micro_turbine": 0.65,
        "_default": 0.78,
    },
    "dryer": {
        "convective": 0.45, "rotary": 0.50, "fluidized_bed": 0.55,
        "spray": 0.40, "belt": 0.48, "heat_pump": 0.65,
        "infrared": 0.42, "drum": 0.44,
        "_default": 0.45,
    },
}
```

### 3.4 Ana Fonksiyonlar

#### 3.4.1 `analyze_advanced_exergy()` — Ana Giriş Noktası

```python
def analyze_advanced_exergy(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
) -> AdvancedExergyResult:
    """
    Fabrika ekipmanları için ileri exergy analizi (EN/EX dekompozisyon).
    
    Args:
        equipment_list: Fabrika ekipman listesi (EquipmentItem formatında)
            Her item: {id, name, equipment_type, subtype, parameters}
        analysis_results: Her ekipmanın analiz sonuçları
            Key: equipment_id, Value: analiz sonucu dict
    
    Returns:
        AdvancedExergyResult: 4-kadran dekompozisyon sonuçları
    """
    # 1. Yeterlilik kontrolü
    valid_equipment = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid_equipment) < 2:
        return AdvancedExergyResult(
            is_valid=False,
            error_message="En az 2 ekipman gerekli (EN/EX etkileşim analizi için)",
            # ... varsayılan boş değerler
        )
    
    # 2. Fabrikadaki ekipman tiplerini tespit et
    factory_types = _get_factory_equipment_types(valid_equipment)
    
    # 3. Her ekipman için verimlilik sapmasını hesapla
    deviations = _calculate_efficiency_deviations(valid_equipment, analysis_results)
    
    # 4. Her ekipman için izolasyon faktörünü hesapla
    isolation_factors = _calculate_isolation_factors(
        valid_equipment, analysis_results, factory_types, deviations
    )
    
    # 5. Her ekipman için EN/EX ve 4-kadran hesapla
    equipment_results = []
    for item in valid_equipment:
        result = analysis_results[item["id"]]
        eq_result = _analyze_single_equipment(
            item, result, isolation_factors[item["id"]],
            valid_equipment, deviations
        )
        equipment_results.append(eq_result)
    
    # 6. Fabrika seviyesi metrikleri hesapla
    factory_metrics = _calculate_factory_metrics(equipment_results)
    
    # 7. Öncelik sıralaması (AV-EN büyükten küçüğe)
    priority_ranking = _create_priority_ranking(equipment_results)
    
    # 8. Etkileşim ağı (görselleştirme için)
    interaction_network = _build_interaction_network(
        equipment_results, valid_equipment, deviations
    )
    
    # 9. 4-Kadran chart verisi
    quadrant_data = _generate_quadrant_chart_data(equipment_results)
    
    # 10. Sonuç derleme
    return AdvancedExergyResult(
        num_equipment=len(equipment_results),
        equipment_results=equipment_results,
        priority_ranking=priority_ranking,
        interaction_network=interaction_network,
        quadrant_chart_data=quadrant_data,
        warnings=_collect_warnings(equipment_results, factory_types),
        **factory_metrics,
    )
```

#### 3.4.2 `_calculate_efficiency_deviations()` — Verimlilik Sapması

```python
def _calculate_efficiency_deviations(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
) -> Dict[str, float]:
    """
    Her ekipmanın referans verimden sapmasını hesapla.
    
    δ_j = (η_ref - η_actual) / η_ref
    
    δ > 0: referansın altında (verimsiz)
    δ = 0: referans seviyesinde
    δ < 0: referansın üstünde (çok iyi)
    
    Returns:
        {equipment_id: deviation_ratio}
    """
    deviations = {}
    
    for item in equipment_list:
        eq_type = item["equipment_type"]
        subtype = item.get("subtype", "_default")
        result = analysis_results.get(item["id"], {})
        
        # Gerçek verim
        eta_actual = result.get("exergy_efficiency_pct", 50) / 100.0
        
        # Referans verim
        ref_dict = REFERENCE_EFFICIENCIES.get(eq_type, {})
        eta_ref = ref_dict.get(subtype, ref_dict.get("_default", 0.70))
        
        # Sapma
        if eta_ref > 0:
            delta = (eta_ref - eta_actual) / eta_ref
        else:
            delta = 0.0
        
        # Clamp: -0.5 ile 1.0 arası (referansın üstünde olabilir ama sınırlı)
        delta = max(-0.5, min(1.0, delta))
        
        deviations[item["id"]] = delta
    
    return deviations
```

#### 3.4.3 `_calculate_isolation_factors()` — İzolasyon Faktörü

```python
def _calculate_isolation_factors(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
    factory_types: Dict[str, List[str]],
    deviations: Dict[str, float],
) -> Dict[str, float]:
    """
    Her ekipman için izolasyon faktörü (φ_k) hesapla.
    
    φ_k = φ₀_k × (1 - Σⱼ αₖⱼ × δⱼ)
    
    - φ₀_k: taban izolasyon faktörü (ekipman tipine özel)
    - αₖⱼ: j'nin k üzerindeki etkileşim katsayısı
    - δⱼ: j'nin referanstan sapması
    
    Sadece fabrikada MEVCUT olan ekipman tipleri etkileşime girer.
    
    Returns:
        {equipment_id: isolation_factor}
    """
    isolation_factors = {}
    
    for item in equipment_list:
        eq_type = item["equipment_type"]
        eq_id = item["id"]
        
        # Taban faktör
        phi_base = BASE_ISOLATION_FACTORS.get(eq_type, 0.70)
        
        # Etkileşim düzeltmesi
        interactions = INTERACTION_COEFFICIENTS.get(eq_type, {})
        total_interaction = 0.0
        
        for other_item in equipment_list:
            if other_item["id"] == eq_id:
                continue  # Kendisi hariç
            
            other_type = other_item["equipment_type"]
            alpha = interactions.get(other_type, 0.0)
            
            if alpha > 0:
                delta = deviations.get(other_item["id"], 0.0)
                # Sadece pozitif sapma (verimsiz ekipman) eksojen etkiyi artırır
                if delta > 0:
                    total_interaction += alpha * delta
        
        # Düzeltilmiş izolasyon faktörü
        phi = phi_base * (1.0 - total_interaction)
        
        # Clamp: 0.20 ile 0.95 arası (fiziksel anlamlılık)
        phi = max(0.20, min(0.95, phi))
        
        isolation_factors[eq_id] = phi
    
    return isolation_factors
```

#### 3.4.4 `_analyze_single_equipment()` — Tek Ekipman EN/EX

```python
def _analyze_single_equipment(
    item: dict,
    result: dict,
    isolation_factor: float,
    all_equipment: List[dict],
    deviations: Dict[str, float],
) -> AdvancedExergyEquipmentResult:
    """
    Tek ekipman için EN/EX ve 4-kadran hesapla.
    """
    eq_id = item["id"]
    eq_type = item["equipment_type"]
    I_total = result.get("exergy_destroyed_kW", 0)
    I_AV = result.get("exergy_destroyed_avoidable_kW", 0)
    I_UN = result.get("exergy_destroyed_unavoidable_kW", 0)
    
    # AV/UN tutarsızlık düzeltmesi
    if abs((I_AV + I_UN) - I_total) > 0.1:
        I_UN = I_total - I_AV
    
    # EN/EX hesabı
    I_EN = I_total * isolation_factor
    I_EX = I_total - I_EN
    
    # 4-Kadran
    I_AV_EN = I_AV * isolation_factor
    I_AV_EX = I_AV * (1.0 - isolation_factor)
    I_UN_EN = I_UN * isolation_factor
    I_UN_EX = I_UN * (1.0 - isolation_factor)
    
    # Eksojen kaynakları (hangi ekipmanlardan geliyor)
    exogenous_sources = _identify_exogenous_sources(
        item, I_EX, all_equipment, deviations
    )
    
    # Öncelik belirleme
    priority, reason = _determine_priority(
        I_AV_EN, I_AV_EX, I_total, isolation_factor
    )
    
    return AdvancedExergyEquipmentResult(
        equipment_id=eq_id,
        equipment_name=item.get("name", f"{eq_type}_{eq_id[:4]}"),
        equipment_type=eq_type,
        subtype=item.get("subtype", ""),
        exergy_destroyed_kW=I_total,
        exergy_efficiency_pct=result.get("exergy_efficiency_pct", 0),
        I_avoidable_kW=I_AV,
        I_unavoidable_kW=I_UN,
        I_endogenous_kW=I_EN,
        I_exogenous_kW=I_EX,
        isolation_factor=isolation_factor,
        I_AV_EN_kW=I_AV_EN,
        I_AV_EX_kW=I_AV_EX,
        I_UN_EN_kW=I_UN_EN,
        I_UN_EX_kW=I_UN_EX,
        exogenous_sources=exogenous_sources,
        improvement_priority=priority,
        priority_reason=reason,
    )
```

#### 3.4.5 `_identify_exogenous_sources()` — Eksojen Kaynaklar

```python
def _identify_exogenous_sources(
    item: dict,
    I_EX_total: float,
    all_equipment: List[dict],
    deviations: Dict[str, float],
) -> List[Dict]:
    """
    Eksojen yıkımın hangi ekipmanlardan kaynaklandığını belirle.
    
    Her kaynak ekipmanın katkısı, etkileşim katsayısı ve sapmasıyla orantılı.
    """
    eq_type = item["equipment_type"]
    eq_id = item["id"]
    interactions = INTERACTION_COEFFICIENTS.get(eq_type, {})
    
    sources = []
    total_weighted = 0.0
    
    # Ağırlıkları hesapla
    for other in all_equipment:
        if other["id"] == eq_id:
            continue
        
        other_type = other["equipment_type"]
        alpha = interactions.get(other_type, 0.0)
        delta = max(deviations.get(other["id"], 0.0), 0.0)  # Sadece pozitif
        
        weight = alpha * delta
        if weight > 0.001:
            sources.append({
                "source_id": other["id"],
                "source_name": other.get("name", other_type),
                "source_type": other_type,
                "weight": weight,
            })
            total_weighted += weight
    
    # Katkıları normalize et ve kW cinsinden hesapla
    for source in sources:
        if total_weighted > 0:
            ratio = source["weight"] / total_weighted
        else:
            ratio = 0
        source["contribution_kW"] = round(I_EX_total * ratio, 2)
        source["contribution_pct"] = round(ratio * 100, 1)
        del source["weight"]
    
    # Büyükten küçüğe sırala
    sources.sort(key=lambda s: s["contribution_kW"], reverse=True)
    
    return sources
```

#### 3.4.6 `_determine_priority()` — Öncelik Belirleme

```python
def _determine_priority(
    I_AV_EN: float,
    I_AV_EX: float,
    I_total: float,
    isolation_factor: float,
) -> Tuple[str, str]:
    """
    Ekipman iyileştirme önceliğini belirle.
    
    Karar ağacı:
    1. I_AV_EN / I_total > 0.30 → YÜKSEK: "Bu ekipmana doğrudan müdahale edin"
    2. I_AV_EX / I_total > 0.30 → YÜKSEK: "Bağlı ekipmanları iyileştirin"
    3. I_AV_EN / I_total > 0.15 → ORTA: "İyileştirme potansiyeli var"
    4. Aksi halde → DÜŞÜK: "Ekipman kabul edilebilir seviyede"
    """
    if I_total <= 0:
        return "low", "Exergy yıkımı ihmal edilebilir"
    
    ratio_AV_EN = I_AV_EN / I_total
    ratio_AV_EX = I_AV_EX / I_total
    
    if ratio_AV_EN > 0.30:
        return "high", f"Kaçınılabilir-endojen yıkım yüksek (%{ratio_AV_EN*100:.0f}) — bu ekipmanı doğrudan iyileştirin"
    elif ratio_AV_EX > 0.30:
        return "high", f"Kaçınılabilir-eksojen yıkım yüksek (%{ratio_AV_EX*100:.0f}) — bağlı ekipmanları iyileştirin"
    elif ratio_AV_EN > 0.15:
        return "medium", f"Orta düzey endojen iyileştirme potansiyeli (%{ratio_AV_EN*100:.0f})"
    elif ratio_AV_EX > 0.15:
        return "medium", f"Orta düzey eksojen etki (%{ratio_AV_EX*100:.0f}) — sistem entegrasyonunu gözden geçirin"
    else:
        return "low", "Ekipman kabul edilebilir seviyede çalışıyor"
```

#### 3.4.7 `_calculate_factory_metrics()` — Fabrika Metrikleri

```python
def _calculate_factory_metrics(
    equipment_results: List[AdvancedExergyEquipmentResult],
) -> dict:
    """Fabrika seviyesi EN/EX metrikleri."""
    total_I = sum(r.exergy_destroyed_kW for r in equipment_results)
    total_EN = sum(r.I_endogenous_kW for r in equipment_results)
    total_EX = sum(r.I_exogenous_kW for r in equipment_results)
    total_AV_EN = sum(r.I_AV_EN_kW for r in equipment_results)
    total_AV_EX = sum(r.I_AV_EX_kW for r in equipment_results)
    total_UN_EN = sum(r.I_UN_EN_kW for r in equipment_results)
    total_UN_EX = sum(r.I_UN_EX_kW for r in equipment_results)
    
    # En etkili ve en etkilenen ekipman
    # En etkili: diğer ekipmanların exogenous_sources'ında en çok geçen
    influence_count = {}
    for r in equipment_results:
        for src in r.exogenous_sources:
            sid = src["source_id"]
            influence_count[sid] = influence_count.get(sid, 0) + src["contribution_kW"]
    
    most_influential = max(influence_count, key=influence_count.get) if influence_count else ""
    most_influential_name = ""
    for r in equipment_results:
        if r.equipment_id == most_influential:
            most_influential_name = r.equipment_name
            break
    
    most_affected = max(equipment_results, key=lambda r: r.I_exogenous_kW).equipment_name if equipment_results else ""
    
    return {
        "total_exergy_destroyed_kW": total_I,
        "total_endogenous_kW": total_EN,
        "total_exogenous_kW": total_EX,
        "endogenous_ratio_pct": (total_EN / total_I * 100) if total_I > 0 else 0,
        "total_AV_EN_kW": total_AV_EN,
        "total_AV_EX_kW": total_AV_EX,
        "total_UN_EN_kW": total_UN_EN,
        "total_UN_EX_kW": total_UN_EX,
        "interaction_density": (total_EX / total_I) if total_I > 0 else 0,
        "most_influential_equipment": most_influential_name,
        "most_affected_equipment": most_affected,
    }
```

#### 3.4.8 `_build_interaction_network()` — Etkileşim Ağı

```python
def _build_interaction_network(
    equipment_results: List[AdvancedExergyEquipmentResult],
    equipment_list: List[dict],
    deviations: Dict[str, float],
) -> List[Dict]:
    """
    Ekipmanlar arası etkileşim ağı (Sankey/graph görselleştirme için).
    
    Returns:
        [{"source": "Kazan-1", "target": "Türbin-1", "value_kW": 12.5}, ...]
    """
    network = []
    
    for r in equipment_results:
        for src in r.exogenous_sources:
            if src["contribution_kW"] >= 1.0:  # Minimum 1 kW eşik
                network.append({
                    "source": src["source_name"],
                    "source_type": src["source_type"],
                    "target": r.equipment_name,
                    "target_type": r.equipment_type,
                    "value_kW": src["contribution_kW"],
                })
    
    # Büyükten küçüğe sırala
    network.sort(key=lambda n: n["value_kW"], reverse=True)
    
    return network
```

#### 3.4.9 `_generate_quadrant_chart_data()` — 4-Kadran Chart

```python
def _generate_quadrant_chart_data(
    equipment_results: List[AdvancedExergyEquipmentResult],
) -> Dict:
    """
    4-kadran stacked bar chart verisi (Plotly formatında).
    
    Her ekipman bir bar:
    - AV-EN (yeşil): İyileştirilebilir, bu ekipmandan
    - AV-EX (sarı): İyileştirilebilir, diğer ekipmanlardan
    - UN-EN (gri): Kaçınılamaz, bu ekipmandan
    - UN-EX (açık gri): Kaçınılamaz, diğer ekipmanlardan
    """
    names = [r.equipment_name for r in equipment_results]
    
    return {
        "equipment_names": names,
        "AV_EN_kW": [round(r.I_AV_EN_kW, 2) for r in equipment_results],
        "AV_EX_kW": [round(r.I_AV_EX_kW, 2) for r in equipment_results],
        "UN_EN_kW": [round(r.I_UN_EN_kW, 2) for r in equipment_results],
        "UN_EX_kW": [round(r.I_UN_EX_kW, 2) for r in equipment_results],
    }
```

#### 3.4.10 Yardımcı Fonksiyonlar

```python
def _filter_valid_equipment(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
) -> List[dict]:
    """Analiz sonucu olan ve exergy yıkımı > 0 olan ekipmanları filtrele."""
    valid = []
    for item in equipment_list:
        result = analysis_results.get(item.get("id", ""))
        if result and result.get("exergy_destroyed_kW", 0) > 0:
            valid.append(item)
    return valid


def _get_factory_equipment_types(equipment_list: List[dict]) -> Dict[str, List[str]]:
    """Fabrikadaki ekipman tiplerini ve ID'lerini grupla."""
    types = {}
    for item in equipment_list:
        eq_type = item["equipment_type"]
        if eq_type not in types:
            types[eq_type] = []
        types[eq_type].append(item["id"])
    return types


def _create_priority_ranking(
    equipment_results: List[AdvancedExergyEquipmentResult],
) -> List[Dict]:
    """AV-EN bazlı öncelik sıralaması."""
    ranked = sorted(equipment_results, key=lambda r: r.I_AV_EN_kW, reverse=True)
    return [
        {
            "equipment_id": r.equipment_id,
            "equipment_name": r.equipment_name,
            "equipment_type": r.equipment_type,
            "I_AV_EN_kW": round(r.I_AV_EN_kW, 2),
            "I_AV_EX_kW": round(r.I_AV_EX_kW, 2),
            "isolation_factor": round(r.isolation_factor, 3),
            "improvement_priority": r.improvement_priority,
            "priority_reason": r.priority_reason,
        }
        for r in ranked
    ]


def _collect_warnings(
    equipment_results: List[AdvancedExergyEquipmentResult],
    factory_types: Dict[str, List[str]],
) -> List[str]:
    """Analiz uyarıları topla."""
    warnings = []
    
    if len(factory_types) < 2:
        warnings.append("Tek ekipman tipi — eksojen etkileşim sınırlı")
    
    total_I = sum(r.exergy_destroyed_kW for r in equipment_results)
    if total_I < 50:
        warnings.append(f"Düşük toplam exergy yıkımı ({total_I:.0f} kW) — EN/EX ayrımı sınırlı fayda sağlayabilir")
    
    # Çok yüksek eksojen oran uyarısı
    total_EX_ratio = sum(r.I_exogenous_kW for r in equipment_results) / total_I if total_I > 0 else 0
    if total_EX_ratio > 0.60:
        warnings.append(f"Yüksek eksojen oran (%{total_EX_ratio*100:.0f}) — ekipmanlar arası etkileşim çok güçlü")
    
    return warnings


def check_advanced_exergy_feasibility(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
) -> Tuple[bool, List[str]]:
    """
    İleri exergy analizinin anlamlı olup olmadığını kontrol et.
    
    Gereksinimler:
    - En az 2 ekipman (etkileşim analizi için)
    - Toplam exergy yıkımı > 10 kW
    - En az 1 ekipmanın AV yıkımı > 0
    """
    warnings = []
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    
    if len(valid) < 2:
        return False, ["En az 2 ekipman gerekli"]
    
    total_I = sum(analysis_results[v["id"]].get("exergy_destroyed_kW", 0) for v in valid)
    if total_I < 10:
        return False, [f"Toplam exergy yıkımı çok düşük ({total_I:.0f} kW)"]
    
    has_avoidable = any(
        analysis_results[v["id"]].get("exergy_destroyed_avoidable_kW", 0) > 0
        for v in valid
    )
    if not has_avoidable:
        warnings.append("Hiçbir ekipmanda kaçınılabilir yıkım yok — 4-kadran analizi sınırlı")
    
    return True, warnings
```

---

## 4. API Entegrasyonu

### 4.1 Factory Engine'e Ekleme

`engine/factory.py` → `analyze_factory()` içine, pinch'ten sonra:

```python
# engine/factory.py analyze_factory() içinde:

from .advanced_exergy import analyze_advanced_exergy, check_advanced_exergy_feasibility

# ... mevcut analiz + pinch ...

# 7. Advanced Exergy (EN/EX dekompozisyon)
advanced_exergy = None
try:
    results_dict = {r["id"]: r["analysis"] for r in valid_results if r.get("analysis")}
    eq_list_dicts = [
        {"id": item.id, "name": item.name, "equipment_type": item.equipment_type,
         "subtype": item.subtype, "parameters": item.parameters}
        for item in equipment_list
    ]
    feasible, _ = check_advanced_exergy_feasibility(eq_list_dicts, results_dict)
    if feasible:
        adv_result = analyze_advanced_exergy(eq_list_dicts, results_dict)
        if adv_result.is_valid:
            advanced_exergy = adv_result.to_dict()
except Exception as e:
    logger.warning(f"Advanced exergy analysis failed: {e}")

# FactoryAnalysisResult'a ekle
return FactoryAnalysisResult(
    ...,
    pinch_analysis=pinch_analysis,
    advanced_exergy=advanced_exergy,  # YENİ
)
```

### 4.2 Ayrı Endpoint (Opsiyonel)

```python
# api/routes/factory.py

@router.post("/factory/projects/{project_id}/advanced-exergy")
async def run_advanced_exergy(
    project_id: str,
    db: AsyncSession = Depends(get_session),
    user: Optional[dict] = Depends(optional_auth),
):
    """Fabrika projesi için ileri exergy analizi çalıştır."""
    # Projeyi getir, ekipman ve sonuçları yükle
    # analyze_advanced_exergy() çağır
    # Sonucu döndür
```

### 4.3 Schema

```python
# api/schemas/factory.py

class AdvancedExergyResponse(BaseModel):
    """İleri exergy analizi yanıt modeli."""
    is_valid: bool
    error_message: str = ""
    num_equipment: int = 0
    total_endogenous_kW: Optional[float] = None
    total_exogenous_kW: Optional[float] = None
    endogenous_ratio_pct: Optional[float] = None
    interaction_density: Optional[float] = None
    equipment_results: List[dict] = []
    priority_ranking: List[dict] = []
    quadrant_chart_data: Optional[dict] = None
    warnings: List[str] = []
```

### 4.4 AI Prompt Entegrasyonu

`api/services/claude_code_service.py` → fabrika yorumlama prompt'una:

```python
def _format_advanced_exergy_for_prompt(adv_data: dict) -> str:
    """İleri exergy özetini AI prompt'u için formatla. Max ~400 karakter."""
    if not adv_data or not adv_data.get("is_valid"):
        return ""
    
    lines = [
        "\n## İleri Exergy Analizi (EN/EX Dekompozisyon)",
        f"- Endojen oran: %{adv_data.get('endogenous_ratio_pct', 0):.0f} (endojen: {adv_data.get('total_endogenous_kW', 0):.0f} kW, eksojen: {adv_data.get('total_exogenous_kW', 0):.0f} kW)",
        f"- Etkileşim yoğunluğu: {adv_data.get('interaction_density', 0):.2f}",
        f"- AV-EN: {adv_data.get('total_AV_EN_kW', 0):.0f} kW | AV-EX: {adv_data.get('total_AV_EX_kW', 0):.0f} kW",
        f"- En etkili: {adv_data.get('most_influential_equipment', 'N/A')} | En etkilenen: {adv_data.get('most_affected_equipment', 'N/A')}",
    ]
    
    # Öncelik sıralaması (ilk 3)
    ranking = adv_data.get("priority_ranking", [])[:3]
    if ranking:
        lines.append("- Öncelik: " + ", ".join(
            f"{r['equipment_name']}({r['I_AV_EN_kW']}kW)" for r in ranking
        ))
    
    result = "\n".join(lines)
    return result[:400] if len(result) > 400 else result
```

---

## 5. Frontend Entegrasyonu

### 5.1 Yeni Componentler

#### `AdvancedExergyTab.jsx` — Fabrika Dashboard'da

Mevcut FactoryDashboard'a kart bazlı ekleme (PinchTab gibi):

```
+----------------------------------------------------------+
| İleri Exergy Analizi (EN/EX)                             |
+----------------------------------------------------------+
|                                                          |
| +-- Özet Kartlar --+                                    |
| | Endojen: 65% | Eksojen: 35% | Etkileşim: 0.35 |     |
| | AV-EN: 120kW | AV-EX: 45kW  | Ekipman: 5      |     |
| +------------------+                                    |
|                                                          |
| +-- 4-Kadran Stacked Bar Chart (Plotly) ---+            |
| |                                           |            |
| | Kompresör-1  [████████████████░░░░]       |            |
| | Kazan-1      [██████████░░░░░░░░░░]       |            |
| | HX-1         [████░░░░░░████████░░]       |            |
| | Türbin-1     [██████████████░░░░░░]       |            |
| |                                           |            |
| | ■ AV-EN  ■ AV-EX  ■ UN-EN  ■ UN-EX     |            |
| +-------------------------------------------+            |
|                                                          |
| +-- Öncelik Sıralaması --------+                        |
| | 1. Kompresör-1 | AV-EN: 45kW | ⚡ YÜKSEK            |
| |    "Bu ekipmanı doğrudan iyileştirin"                  |
| | 2. HX-1        | AV-EN: 30kW | ⚡ YÜKSEK            |
| |    "Bağlı ekipmanları iyileştirin"                     |
| | 3. Kazan-1     | AV-EN: 25kW | ⚠ ORTA               |
| +--------------------------------------+                |
|                                                          |
| +-- Etkileşim Ağı (opsiyonel) -+                       |
| | Kazan-1 ──(12kW)──> Türbin-1                         |
| | Kazan-1 ──(8kW)───> Dryer-1                          |
| | HX-1    ──(5kW)───> Chiller-1                        |
| +--------------------------------------+                |
+----------------------------------------------------------+
```

#### Componentler

1. **`QuadrantChart.jsx`** — Plotly stacked horizontal bar: AV-EN (yeşil), AV-EX (sarı/turuncu), UN-EN (gri), UN-EX (açık gri)
2. **`AdvancedExergyMetricBar.jsx`** — Özet metrik kartları
3. **`AdvancedExergyPriorityList.jsx`** — Öncelik sıralaması (PriorityList.jsx benzeri)
4. **`InteractionNetwork.jsx`** — Ekipmanlar arası etkileşim ok diyagramı (opsiyonel — basit liste de olur)
5. **`AdvancedExergyTab.jsx`** — Ana bileşen

### 5.2 FactoryDashboard Entegrasyonu

```
FactoryDashboard kart sırası:
  1. MetricBar (mevcut)
  2. PriorityList + IntegrationPanel (mevcut)
  3. FactorySankey (mevcut)
  4. PinchTab (BRIEF_24)
  5. AdvancedExergyTab (BRIEF_26 — YENİ)
  6. FactoryAIPanel (mevcut)
```

---

## 6. Testler

### 6.1 `tests/test_advanced_exergy.py`

Tahmini: **~400 satır, 28+ test**

```python
class TestEfficiencyDeviations:
    """Verimlilik sapması hesaplama testleri."""
    
    def test_below_reference_gives_positive_deviation(self):
        """Referansın altındaki verimlilik → δ > 0."""
    
    def test_at_reference_gives_zero_deviation(self):
        """Referans seviyesinde verimlilik → δ = 0."""
    
    def test_above_reference_gives_negative_deviation(self):
        """Referansın üstündeki verimlilik → δ < 0."""
    
    def test_deviation_clamped(self):
        """δ -0.5 ile 1.0 arasında sınırlanmış."""
    
    def test_subtype_specific_reference(self):
        """Alt tipe özel referans verim kullanılıyor."""


class TestIsolationFactors:
    """İzolasyon faktörü hesaplama testleri."""
    
    def test_single_equipment_type_uses_base_factor(self):
        """Tek tip ekipman → taban φ₀ kullanılır."""
    
    def test_interacting_equipment_reduces_factor(self):
        """Etkileşen verimsiz ekipman → φ azalır."""
    
    def test_efficient_interacting_equipment_no_reduction(self):
        """İyi çalışan etkileşen ekipman → φ azalmaz."""
    
    def test_factor_clamped_between_bounds(self):
        """φ 0.20 ile 0.95 arasında."""
    
    def test_no_interaction_coefficient_no_effect(self):
        """Etkileşim katsayısı 0 → etki yok."""


class TestENEXDecomposition:
    """EN/EX ayrışım testleri."""
    
    def test_EN_plus_EX_equals_total(self):
        """I_EN + I_EX = I_total (invariant)."""
    
    def test_four_quadrant_sum_equals_total(self):
        """AV-EN + AV-EX + UN-EN + UN-EX = I_total (invariant)."""
    
    def test_EN_leq_total(self):
        """I_EN ≤ I_total."""
    
    def test_EX_non_negative(self):
        """I_EX ≥ 0."""
    
    def test_all_quadrants_non_negative(self):
        """Tüm 4 kadran ≥ 0."""
    
    def test_high_isolation_factor_means_mostly_endogenous(self):
        """φ = 0.90 → I_EN ≈ 0.90 × I_total."""


class TestExogenousSources:
    """Eksojen kaynak tespiti testleri."""
    
    def test_sources_sum_leq_total_exogenous(self):
        """Kaynakların toplamı ≤ I_EX."""
    
    def test_no_self_reference_in_sources(self):
        """Ekipmanın kendisi kaynak listesinde yok."""
    
    def test_sources_sorted_by_contribution(self):
        """Kaynaklar katkıya göre azalan sıralı."""


class TestPriorityRanking:
    """Öncelik sıralaması testleri."""
    
    def test_ranking_sorted_by_AV_EN(self):
        """Sıralama AV-EN'e göre azalan."""
    
    def test_high_AV_EN_ratio_gives_high_priority(self):
        """AV-EN / I_total > 0.30 → yüksek öncelik."""
    
    def test_low_destruction_gives_low_priority(self):
        """Düşük yıkım → düşük öncelik."""


class TestFactoryMetrics:
    """Fabrika seviyesi metrik testleri."""
    
    def test_total_EN_plus_EX_equals_total_destruction(self):
        """Toplam EN + EX = toplam yıkım."""
    
    def test_interaction_density_between_0_and_1(self):
        """Etkileşim yoğunluğu 0-1 arasında."""


class TestEdgeCases:
    """Uç durumlar."""
    
    def test_single_equipment_returns_invalid(self):
        """Tek ekipman → is_valid=False."""
    
    def test_zero_destruction_handled(self):
        """Sıfır yıkım → hata yok."""
    
    def test_all_same_type_limited_interaction(self):
        """Aynı tipte tüm ekipmanlar → sınırlı etkileşim."""
    
    def test_missing_AV_UN_fields_handled(self):
        """AV/UN alanları eksikse varsayılan kullan."""


class TestIntegration:
    """Entegrasyon testleri."""
    
    def test_full_factory_analysis_includes_advanced_exergy(self):
        """analyze_factory() sonucunda advanced_exergy alanı var."""
    
    def test_serialization_roundtrip(self):
        """to_dict() → JSON → tekrar okuma sorunsuz."""
```

---

## 7. Uygulama Planı

### Faz 1: Engine (Öncelik 1)

| Adım | Dosya | İş |
|------|-------|----|
| 1.1 | `engine/advanced_exergy.py` (YENİ) | Veri yapıları + sabit veriler (izolasyon faktörleri, etkileşim katsayıları, referans verimler) |
| 1.2 | `engine/advanced_exergy.py` | `_calculate_efficiency_deviations()` |
| 1.3 | `engine/advanced_exergy.py` | `_calculate_isolation_factors()` |
| 1.4 | `engine/advanced_exergy.py` | `_analyze_single_equipment()` + 4-kadran hesabı |
| 1.5 | `engine/advanced_exergy.py` | `_identify_exogenous_sources()` |
| 1.6 | `engine/advanced_exergy.py` | `_determine_priority()` |
| 1.7 | `engine/advanced_exergy.py` | `_calculate_factory_metrics()` |
| 1.8 | `engine/advanced_exergy.py` | `_build_interaction_network()` |
| 1.9 | `engine/advanced_exergy.py` | `_generate_quadrant_chart_data()` |
| 1.10 | `engine/advanced_exergy.py` | `analyze_advanced_exergy()` ana fonksiyon |
| 1.11 | `engine/advanced_exergy.py` | `check_advanced_exergy_feasibility()` |
| 1.12 | `engine/__init__.py` | Advanced exergy export'ları ekle |

### Faz 2: Testler (Öncelik 1)

| Adım | Dosya | İş |
|------|-------|----|
| 2.1 | `tests/test_advanced_exergy.py` (YENİ) | Test fixture'ları (3-5 ekipman fabrika senaryosu) |
| 2.2 | `tests/test_advanced_exergy.py` | Verimlilik sapması testleri (5 test) |
| 2.3 | `tests/test_advanced_exergy.py` | İzolasyon faktörü testleri (5 test) |
| 2.4 | `tests/test_advanced_exergy.py` | EN/EX ve 4-kadran testleri (6 test) |
| 2.5 | `tests/test_advanced_exergy.py` | Eksojen kaynak testleri (3 test) |
| 2.6 | `tests/test_advanced_exergy.py` | Öncelik ve fabrika metrikleri (4 test) |
| 2.7 | `tests/test_advanced_exergy.py` | Edge case ve entegrasyon (5 test) |
| 2.8 | Tüm testler | `pytest tests/ -v` regresyon kontrolü |

### Faz 3: API + Fabrika Entegrasyonu (Öncelik 2)

| Adım | Dosya | İş |
|------|-------|----|
| 3.1 | `engine/factory.py` | `FactoryAnalysisResult`'a `advanced_exergy` alanı ekle |
| 3.2 | `engine/factory.py` | `analyze_factory()` içinde advanced exergy çağrısı |
| 3.3 | `api/schemas/factory.py` | `AdvancedExergyResponse` schema |
| 3.4 | `api/routes/factory.py` | `/advanced-exergy` endpoint |
| 3.5 | `api/services/claude_code_service.py` | `_format_advanced_exergy_for_prompt()` + prompt'a ekleme |

### Faz 4: Frontend (Öncelik 2)

| Adım | Dosya | İş |
|------|-------|----|
| 4.1 | `frontend/src/components/advanced-exergy/QuadrantChart.jsx` (YENİ) | Plotly stacked bar |
| 4.2 | `frontend/src/components/advanced-exergy/AdvancedExergyMetricBar.jsx` (YENİ) | Özet kartlar |
| 4.3 | `frontend/src/components/advanced-exergy/AdvancedExergyPriorityList.jsx` (YENİ) | Öncelik listesi |
| 4.4 | `frontend/src/components/advanced-exergy/InteractionNetwork.jsx` (YENİ) | Etkileşim listesi |
| 4.5 | `frontend/src/components/advanced-exergy/AdvancedExergyTab.jsx` (YENİ) | Ana bileşen |
| 4.6 | `frontend/src/pages/FactoryDashboard.jsx` | AdvancedExergyTab entegrasyonu |
| 4.7 | `frontend/src/services/factoryApi.js` | `runAdvancedExergy()` ekle |

---

## 8. Doğrulama Kontrol Listesi

### Invariantlar
- [ ] I_k^EN + I_k^EX = I_k (her ekipman için, tolerans < 0.01 kW)
- [ ] AV-EN + AV-EX + UN-EN + UN-EX = I_k (her ekipman için)
- [ ] Toplam EN + toplam EX = toplam I (fabrika seviyesi)
- [ ] 0.20 ≤ φ_k ≤ 0.95 (tüm izolasyon faktörleri)
- [ ] Tüm 4 kadran ≥ 0
- [ ] Eksojen kaynaklar listesinde ekipmanın kendisi yok

### Testler
- [ ] `pytest tests/test_advanced_exergy.py -v` — tüm testler geçiyor
- [ ] `pytest tests/ -v` — regresyon yok

### API
- [ ] `analyze_factory()` sonucu `advanced_exergy` içeriyor (2+ ekipman varsa)
- [ ] `/advanced-exergy` endpoint çalışıyor
- [ ] AI prompt boyutu hâlâ < 35K

### Frontend
- [ ] 4-kadran chart doğru render ediliyor
- [ ] Öncelik sıralaması AV-EN'e göre
- [ ] advanced_exergy = None ise bölüm gizleniyor

---

## 9. Claude Code Prompt

```
PROJECT_ANALYSIS.md ve BRIEF_26_ADVANCED_EXERGY.md dosyalarını oku.

Görev: ExergyLab'a Tsatsaronis EN/EX (endojen/eksojen) dekompozisyon motoru ekle.

Faz 1 — Engine modülü:
1. engine/advanced_exergy.py dosyasını oluştur.
2. Veri yapılarını tanımla: AdvancedExergyEquipmentResult ve AdvancedExergyResult (to_dict metodu ile). Brief 3.2.
3. Sabit verileri tanımla: BASE_ISOLATION_FACTORS, INTERACTION_COEFFICIENTS, REFERENCE_EFFICIENCIES. Brief 3.3. Tüm 7 ekipman tipi ve tüm alt tipler için referans verim değerleri olmalı.
4. _filter_valid_equipment() ve _get_factory_equipment_types() yardımcılarını yaz.
5. _calculate_efficiency_deviations() yaz: δ = (η_ref - η_actual) / η_ref, clamp -0.5 ile 1.0. Brief 3.4.2.
6. _calculate_isolation_factors() yaz: φ = φ₀ × (1 - Σ α×δ), clamp 0.20 ile 0.95. Brief 3.4.3. Sadece fabrikada mevcut ekipman tipleri etkileşime girer. Sadece pozitif δ (verimsiz ekipman) eksojen etkiyi artırır.
7. _analyze_single_equipment() yaz: I_EN = I_total × φ, I_EX = I_total - I_EN, 4-kadran. Brief 3.4.4.
8. _identify_exogenous_sources() yaz: α×δ ağırlıklı, normalize, kW cinsinden. Brief 3.4.5.
9. _determine_priority() yaz: AV-EN/I_total oranına göre high/medium/low. Brief 3.4.6.
10. _calculate_factory_metrics() yaz: toplam EN/EX, etkileşim yoğunluğu, en etkili/etkilenen. Brief 3.4.7.
11. _build_interaction_network() yaz: {source, target, value_kW}. Brief 3.4.8.
12. _generate_quadrant_chart_data() yaz: stacked bar chart verisi. Brief 3.4.9.
13. analyze_advanced_exergy() ana fonksiyon: tüm adımları birleştir. Brief 3.4.1.
14. check_advanced_exergy_feasibility() yaz. Brief 3.4.10.
15. engine/__init__.py güncelle.

Faz 2 — Testler:
16. tests/test_advanced_exergy.py dosyasını oluştur.
17. 3-5 ekipman içeren test fixture'ı tanımla (karışık tipler: kazan, kompresör, HX, türbin).
18. Verimlilik sapması testleri (5 test).
19. İzolasyon faktörü testleri (5 test).
20. EN/EX ve 4-kadran invariant testleri (6 test). Kritik: I_EN + I_EX = I_total, AV-EN + AV-EX + UN-EN + UN-EX = I_total.
21. Eksojen kaynak testleri (3 test).
22. Öncelik ve fabrika metrikleri (4 test).
23. Edge case testleri (5 test): tek ekipman, sıfır yıkım, eksik AV/UN.
24. pytest tests/test_advanced_exergy.py -v çalıştır.
25. pytest tests/ -v çalıştır (regresyon kontrolü).

Faz 3 — API + Fabrika entegrasyonu:
26. engine/factory.py → FactoryAnalysisResult'a advanced_exergy: Optional[dict] = None ekle.
27. engine/factory.py → analyze_factory() içinde advanced exergy çağrısı (best-effort, hata durumunda None). equipment_list'i dict formatına dönüştürmeyi unutma.
28. api/schemas/factory.py → AdvancedExergyResponse ekle.
29. api/routes/factory.py → POST /factory/projects/{id}/advanced-exergy endpoint ekle.
30. api/services/claude_code_service.py → _format_advanced_exergy_for_prompt() fonksiyonu yaz (max 400 karakter). Fabrika prompt'una ekle.

Faz 4 — Frontend:
31. frontend/src/components/advanced-exergy/ dizini oluştur.
32. QuadrantChart.jsx — Plotly horizontal stacked bar (AV-EN yeşil #22c55e, AV-EX turuncu #f59e0b, UN-EN gri #9ca3af, UN-EX açık gri #d1d5db).
33. AdvancedExergyMetricBar.jsx — Endojen %, Eksojen %, AV-EN kW, etkileşim yoğunluğu kartları.
34. AdvancedExergyPriorityList.jsx — AV-EN sıralı öncelik listesi (PriorityList.jsx benzeri tasarım).
35. InteractionNetwork.jsx — Etkileşim ağı basit liste/kart görünümü.
36. AdvancedExergyTab.jsx — Tüm componentleri birleştirir.
37. FactoryDashboard.jsx → AdvancedExergyTab ekle (PinchTab'dan sonra).
38. factoryApi.js → runAdvancedExergy() ekle.

Her fazdan sonra testleri çalıştır.

Önemli kurallar:
- Mevcut factory analiz akışını bozma. advanced_exergy opsiyonel.
- İnvariantlar: I_EN + I_EX = I_total, 4-kadran toplamı = I_total.
- İzolasyon faktörü 0.20-0.95 arasında clamp edilmeli.
- Eksojen kaynaklarda ekipmanın kendisi olmamalı.
- equipment_list dict formatı: {id, name, equipment_type, subtype, parameters}.
- analysis_results dict formatı: key=equipment_id, value=analiz sonucu dict.
- Analiz sonuçlarında kullanılacak alanlar: exergy_destroyed_kW, exergy_efficiency_pct, exergy_destroyed_avoidable_kW, exergy_destroyed_unavoidable_kW.
```

---

## 10. Bilinen Kısıtlamalar ve Gelecek İyileştirmeler

| Kısıtlama | Açıklama | Gelecek Çözüm |
|-----------|----------|---------------|
| Simülasyon yok | EN/EX izolasyon faktörüyle tahmin ediliyor, gerçek proses simülasyonu değil | Termodinamik çevrim simülatörü (CoolProp tabanlı) |
| Sabit etkileşim katsayıları | α değerleri statik, gerçek bağlantılara dayalı değil | Kullanıcı tanımlı topoloji (hangi ekipman hangisine bağlı) |
| Tek yönlü etkileşim | A→B ve B→A ayrı ele alınmıyor | Çift yönlü etkileşim matrisi |
| Zaman bağımsız | Part-load koşulları yok | Yük profili tabanlı analiz |
| Etkileşim katsayıları genel | Sektöre özel olmayabilir | Sektör bazlı α kalibrasyonu |

---

*BRIEF_26 — Advanced Exergy (EN/EX Dekompozisyon) Motor Modülü*
*Yazar: Claude (ExergyLab geliştirme desteği)*
*Tarih: 2026-02-05*
*Bağımlılık: Mevcut AV/UN (core.py), BRIEF_24 (Pinch), BRIEF_25 (Prompt fix)*
