# BRIEF_27: Entropy Generation Minimization (EGM) Motor Modülü

> **Tarih:** 2026-02-06
> **Öncelik:** Yüksek
> **Tahmini Süre:** 3-5 saat
> **Karmaşıklık:** Orta
> **Bağımlılıklar:** Mevcut exergy motorları (core.py, 7 ekipman modülü), fabrika (factory.py)
> **Etkilenen Dosyalar:** Yeni + mevcut toplam ~12 dosya

---

## 1. Bağlam ve Motivasyon

### 1.1 EGM Nedir?

Entropy Generation Minimization (Entropi Üretimi Minimizasyonu), Adrian Bejan'ın öncülüğünü yaptığı termodinamik optimizasyon yaklaşımıdır. Exergy analizi "ne kadar kayıp var?" sorusuna cevap verirken, EGM "entropi üretimi nereden geliyor ve nasıl minimize edilir?" sorusuna odaklanır.

**ExergyLab'a katacağı değer:**
- **Bejan sayısı (N_s):** Ekipmanın entropi üretiminin boyutsuz ölçüsü — farklı tip/ölçek ekipmanları karşılaştırmayı sağlar
- **Gouy-Stodola teoremi:** Exergy yıkımını entropi üretimine bağlar → I_dot = T₀ × S_gen
- **Entropi üretimi dekompozisyonu:** Isı transferi + sürtünme/basınç düşüşü + karışma katkılarını ayırır
- **Augmentation entropy generation number (N_s,a):** İyileştirme sonrası entropi artışını/azalışını ölçer

### 1.2 ExergyLab'ın Mevcut Durumu ile İlişki

ExergyLab şu an exergy yıkımını (I_dot) hesaplıyor ama entropi üretimini (S_gen) açık olarak hesaplamıyor. Oysa ikisi doğrudan bağlantılı:

```
Gouy-Stodola: I_dot = T₀ × S_gen
Dolayısıyla:  S_gen = I_dot / T₀
```

Bu ilişki sayesinde, mevcut exergy sonuçlarından EGM metriklerini **türetebiliriz** — ek fiziksel hesaplama gerekmeden. Bu, mimari olarak çok uygun: mevcut 7 motor modülüne dokunmadan, fabrika seviyesi bir analiz katmanı ekliyoruz.

### 1.3 Knowledge Base

`knowledge/factory/entropy_generation/` dizininde ~19 dosya mevcut. Uygulama koşulu: **N_s > 0.5**.

---

## 2. Teori — EGM Metrikleri

### 2.1 Temel Formüller

#### Gouy-Stodola Teoremi
```
I_dot = T₀ × S_gen                    (kW)
S_gen = I_dot / T₀                    (kW/K)

Burada:
  I_dot = exergy yıkım oranı (kW) — mevcut hesaplanıyor
  T₀    = ölü durum sıcaklığı (K) — DeadState'ten (298.15 K)
  S_gen = entropi üretim oranı (kW/K)
```

#### Bejan Sayısı (N_s)
```
N_s = S_gen / S_gen,min = (T₀ × S_gen) / E_x,in = I_dot / E_x,in

Alternatif formülasyon:
N_s = 1 - η_ex                        (exergy verimi ile doğrudan ilişkili)

Burada:
  E_x,in  = giren exergy (kW)
  η_ex    = exergy verimi (%)

Yorum:
  N_s = 0   → tersinir (ideal)
  N_s = 1   → tamamen tersinmez (tüm exergy yıkılmış)
  N_s > 0.5 → ciddi tersinmezlik → EGM analizi anlamlı
```

**Dikkat:** Bejan sayısı (N_s) ile ısı transferinde kullanılan Bejan sayısı (Be = ΔS_HT / (ΔS_HT + ΔS_FF)) farklıdır. Biz burada termodinamik Bejan sayısını (N_s) kullanıyoruz. Isı transferi Bejan sayısı (Be) sadece ısı eşanjörleri için anlamlıdır ve ayrıca hesaplanır.

#### Entropi Üretimi Dekompozisyonu
```
S_gen = S_gen,ΔT + S_gen,ΔP + S_gen,mix

Burada:
  S_gen,ΔT  = ısı transferindeki sonlu sıcaklık farkından kaynaklanan entropi (kW/K)
  S_gen,ΔP  = sürtünme/basınç düşüşünden kaynaklanan entropi (kW/K)
  S_gen,mix = karışma/kimyasal reaksiyonlardan kaynaklanan entropi (kW/K)
```

Tam dekompozisyon her ekipman tipine göre farklı ağırlıklara sahiptir:

| Ekipman | S_gen,ΔT | S_gen,ΔP | S_gen,mix | Baskın Kaynak |
|---------|----------|----------|-----------|---------------|
| Kompresör | %20-30 | %60-75 | ~%5 | Basınç (izentropik kayıp) |
| Kazan | %15-25 | ~%5 | %65-80 | Karışma (yanma tersinmezliği) |
| Chiller | %50-65 | %20-30 | %10-20 | Isı transferi (ΔT) |
| Pompa | %5-15 | %80-90 | ~%5 | Basınç (hidrolik kayıp) |
| Isı Eşanjörü | %75-90 | %10-20 | ~%5 | Isı transferi (ΔT) |
| Buhar Türbini | %25-35 | %55-70 | ~%5 | Basınç (izentropik kayıp) |
| Kurutma Fırını | %35-50 | %10-20 | %30-45 | Isı transferi + karışma |

### 2.2 Ekipman Tipine Özel Dekompozisyon Katsayıları

```python
# Entropi üretimi dekompozisyon katsayıları
# Her ekipman tipinin S_gen'inin hangi mekanizmalardan kaynaklandığı
# Katsayılar: (f_ΔT, f_ΔP, f_mix) — toplamı 1.0

ENTROPY_DECOMPOSITION_FRACTIONS = {
    "compressor": {
        "screw": (0.25, 0.70, 0.05),
        "screw_oilfree": (0.20, 0.75, 0.05),
        "piston": (0.30, 0.65, 0.05),
        "scroll": (0.25, 0.70, 0.05),
        "centrifugal": (0.20, 0.75, 0.05),
        "roots": (0.30, 0.60, 0.10),
        "_default": (0.25, 0.70, 0.05),
    },
    "boiler": {
        "steam_firetube": (0.20, 0.05, 0.75),
        "steam_watertube": (0.18, 0.05, 0.77),
        "hotwater": (0.25, 0.05, 0.70),
        "condensing": (0.15, 0.05, 0.80),
        "waste_heat": (0.45, 0.05, 0.50),
        "electric": (0.90, 0.05, 0.05),     # Elektrik → ısı, yanma yok
        "biomass": (0.20, 0.05, 0.75),
        "_default": (0.20, 0.05, 0.75),
    },
    "chiller": {
        "screw": (0.55, 0.30, 0.15),
        "centrifugal": (0.50, 0.35, 0.15),
        "scroll": (0.55, 0.30, 0.15),
        "reciprocating": (0.50, 0.30, 0.20),
        "absorption": (0.65, 0.10, 0.25),
        "air_cooled": (0.60, 0.25, 0.15),
        "water_cooled": (0.55, 0.30, 0.15),
        "_default": (0.55, 0.30, 0.15),
    },
    "pump": {
        "centrifugal": (0.10, 0.85, 0.05),
        "positive_displacement": (0.10, 0.85, 0.05),
        "submersible": (0.10, 0.85, 0.05),
        "vertical_turbine": (0.10, 0.85, 0.05),
        "booster": (0.10, 0.85, 0.05),
        "vacuum": (0.15, 0.80, 0.05),
        "_default": (0.10, 0.85, 0.05),
    },
    "heat_exchanger": {
        "shell_tube": (0.80, 0.15, 0.05),
        "plate": (0.85, 0.12, 0.03),
        "air_cooled": (0.75, 0.20, 0.05),
        "double_pipe": (0.80, 0.15, 0.05),
        "spiral": (0.82, 0.13, 0.05),
        "economizer": (0.78, 0.17, 0.05),
        "recuperator": (0.80, 0.15, 0.05),
        "_default": (0.80, 0.15, 0.05),
    },
    "steam_turbine": {
        "back_pressure": (0.30, 0.65, 0.05),
        "condensing": (0.25, 0.70, 0.05),
        "extraction": (0.30, 0.60, 0.10),
        "orc": (0.35, 0.55, 0.10),
        "micro_turbine": (0.30, 0.60, 0.10),
        "_default": (0.30, 0.65, 0.05),
    },
    "dryer": {
        "convective": (0.40, 0.15, 0.45),
        "rotary": (0.40, 0.20, 0.40),
        "fluidized_bed": (0.35, 0.25, 0.40),
        "spray": (0.45, 0.10, 0.45),
        "belt": (0.40, 0.15, 0.45),
        "heat_pump": (0.50, 0.15, 0.35),
        "infrared": (0.55, 0.10, 0.35),
        "drum": (0.40, 0.20, 0.40),
        "_default": (0.40, 0.15, 0.45),
    },
}
```

### 2.3 Isı Transferi Bejan Sayısı (Sadece Isı Eşanjörleri)

```
Be = S_gen,ΔT / (S_gen,ΔT + S_gen,ΔP)

Yorum:
  Be → 1: Isı transferi tersinmezliği baskın (ΔT çok büyük)
  Be → 0: Akış sürtünmesi baskın (ΔP çok büyük)
  Be ≈ 0.5: Dengeli tasarım (genellikle optimum yakınında)

Bu sadece heat_exchanger tipi için hesaplanır.
```

### 2.4 Augmentation Entropy Generation Number (N_s,a)

```
N_s,a = S_gen,improved / S_gen,current

Yorum:
  N_s,a < 1: İyileştirme entropi üretimini azaltmış ✅
  N_s,a = 1: Değişiklik yok
  N_s,a > 1: İyileştirme entropi üretimini artırmış ❌

ExergyLab yaklaşımı:
  S_gen,current = I_dot / T₀
  S_gen,improved = I_dot_unavoidable / T₀  (kaçınılamaz yıkım = en iyi ulaşılabilir durum)
  
  N_s,a = I_dot_unavoidable / I_dot = 1 - avoidable_ratio
```

### 2.5 Entropi Üretimi Yoğunluğu (Volumetric/Specific)

```
s_gen_specific = S_gen / Q_dot          (kW/K per kW termal)
  → Birim ısı transferi başına entropi üretimi

s_gen_per_exergy = S_gen / E_x,in      (kW/K per kW exergy)
  → Birim exergy girişi başına entropi üretimi (= N_s / T₀)
```

### 2.6 Fabrika Seviyesi Metrikler

```
S_gen_total = Σ_k S_gen,k                     (kW/K)
N_s_factory = S_gen_total × T₀ / E_x,in_total  (boyutsuz)

Entropi üretimi dağılımı:
  S_gen,ΔT_total = Σ_k S_gen,ΔT_k
  S_gen,ΔP_total = Σ_k S_gen,ΔP_k
  S_gen,mix_total = Σ_k S_gen,mix_k

Baskın mekanizma:
  dominant = argmax(S_gen,ΔT_total, S_gen,ΔP_total, S_gen,mix_total)

Entropi hotspot sıralaması (N_s bazlı):
  → N_s büyükten küçüğe → en fazla "tersinmez" ekipman önce
```

---

## 3. Engine Modülü: `engine/entropy_generation.py`

### 3.1 Dosya Yapısı

Tahmini boyut: **~400-500 satır**

```python
"""
ExergyLab Entropi Üretimi Minimizasyonu (EGM) Motor Modülü

Bejan'ın EGM metodolojisi:
  - Gouy-Stodola: I_dot = T₀ × S_gen
  - Bejan sayısı (N_s): boyutsuz tersinmezlik ölçüsü
  - Entropi dekompozisyonu: ΔT + ΔP + karışma katkıları
  - Augmentation number (N_s,a): iyileştirme potansiyeli

Referanslar:
  - Bejan, A. (1996). "Entropy Generation Minimization"
  - Bejan, A. (2013). "Convection Heat Transfer", 4th ed.
  - Hesselgreaves, J.E. (2001). "Compact Heat Exchangers"
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
import logging

logger = logging.getLogger(__name__)
```

### 3.2 Veri Yapıları

```python
@dataclass
class EntropyEquipmentResult:
    """Tek ekipman için EGM sonucu."""
    equipment_id: str
    equipment_name: str
    equipment_type: str
    subtype: str
    
    # Temel exergy verileri (mevcut analiz sonuçlarından)
    exergy_in_kW: float
    exergy_destroyed_kW: float
    exergy_efficiency_pct: float
    
    # Gouy-Stodola
    S_gen_kW_K: float                    # Entropi üretim oranı (kW/K)
    T0_K: float                          # Ölü durum sıcaklığı (K)
    
    # Bejan sayısı (termodinamik)
    N_s: float                           # I_dot / E_x,in = 1 - η_ex
    N_s_grade: str                       # "A"-"F" kalite notu
    
    # Entropi dekompozisyonu
    S_gen_heat_transfer_kW_K: float      # ΔT kaynaklı
    S_gen_pressure_drop_kW_K: float      # ΔP kaynaklı
    S_gen_mixing_kW_K: float             # Karışma/kimyasal kaynaklı
    dominant_mechanism: str              # "heat_transfer" | "pressure_drop" | "mixing"
    
    # Isı transferi Bejan sayısı (sadece HX'ler için, yoksa None)
    Be_heat_transfer: Optional[float]    # S_gen,ΔT / (S_gen,ΔT + S_gen,ΔP)
    
    # Augmentation number
    N_s_augmentation: float              # S_gen,unavoidable / S_gen = 1 - avoidable_ratio
    improvement_potential_pct: float     # (1 - N_s,a) × 100 = avoidable_ratio × 100
    
    # Spesifik entropi üretimi
    s_gen_per_exergy_input: float        # S_gen / E_x,in (1/K)
    
    def to_dict(self) -> dict:
        d = {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "subtype": self.subtype,
            "exergy_in_kW": round(self.exergy_in_kW, 2),
            "exergy_destroyed_kW": round(self.exergy_destroyed_kW, 2),
            "exergy_efficiency_pct": round(self.exergy_efficiency_pct, 1),
            "S_gen_kW_K": round(self.S_gen_kW_K, 6),
            "T0_K": round(self.T0_K, 2),
            "N_s": round(self.N_s, 4),
            "N_s_grade": self.N_s_grade,
            "S_gen_heat_transfer_kW_K": round(self.S_gen_heat_transfer_kW_K, 6),
            "S_gen_pressure_drop_kW_K": round(self.S_gen_pressure_drop_kW_K, 6),
            "S_gen_mixing_kW_K": round(self.S_gen_mixing_kW_K, 6),
            "dominant_mechanism": self.dominant_mechanism,
            "Be_heat_transfer": round(self.Be_heat_transfer, 4) if self.Be_heat_transfer is not None else None,
            "N_s_augmentation": round(self.N_s_augmentation, 4),
            "improvement_potential_pct": round(self.improvement_potential_pct, 1),
            "s_gen_per_exergy_input": round(self.s_gen_per_exergy_input, 6),
        }
        return d


@dataclass
class EntropyGenerationResult:
    """Fabrika seviyesi EGM sonucu."""
    # Genel
    num_equipment: int
    T0_K: float
    
    # Toplam entropi üretimi
    S_gen_total_kW_K: float
    N_s_factory: float                   # Fabrika seviyesi Bejan sayısı
    
    # Dekompozisyon toplamları
    S_gen_heat_transfer_total_kW_K: float
    S_gen_pressure_drop_total_kW_K: float
    S_gen_mixing_total_kW_K: float
    dominant_mechanism_factory: str       # Fabrika genelinde baskın mekanizma
    
    # Dekompozisyon yüzdeleri
    heat_transfer_pct: float
    pressure_drop_pct: float
    mixing_pct: float
    
    # Gouy-Stodola toplamı
    total_exergy_destroyed_kW: float     # = T₀ × S_gen_total (doğrulama)
    
    # Ekipman sonuçları
    equipment_results: List[EntropyEquipmentResult]
    
    # Sıralama (N_s bazlı — en tersinmez ilk)
    irreversibility_ranking: List[Dict]
    
    # Görselleştirme
    decomposition_chart_data: Dict       # Stacked bar: ΔT + ΔP + mix per equipment
    bejan_number_chart_data: Dict        # Bar chart: N_s per equipment + grade colors
    
    # Uyarılar
    warnings: List[str]
    
    is_valid: bool = True
    error_message: str = ""
    
    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "error_message": self.error_message,
            "num_equipment": self.num_equipment,
            "T0_K": round(self.T0_K, 2),
            "S_gen_total_kW_K": round(self.S_gen_total_kW_K, 6),
            "N_s_factory": round(self.N_s_factory, 4),
            "S_gen_heat_transfer_total_kW_K": round(self.S_gen_heat_transfer_total_kW_K, 6),
            "S_gen_pressure_drop_total_kW_K": round(self.S_gen_pressure_drop_total_kW_K, 6),
            "S_gen_mixing_total_kW_K": round(self.S_gen_mixing_total_kW_K, 6),
            "dominant_mechanism_factory": self.dominant_mechanism_factory,
            "heat_transfer_pct": round(self.heat_transfer_pct, 1),
            "pressure_drop_pct": round(self.pressure_drop_pct, 1),
            "mixing_pct": round(self.mixing_pct, 1),
            "total_exergy_destroyed_kW": round(self.total_exergy_destroyed_kW, 2),
            "equipment_results": [r.to_dict() for r in self.equipment_results],
            "irreversibility_ranking": self.irreversibility_ranking,
            "decomposition_chart_data": self.decomposition_chart_data,
            "bejan_number_chart_data": self.bejan_number_chart_data,
            "warnings": self.warnings,
        }
```

### 3.3 Sabit Veriler

```python
# --- Entropi Dekompozisyon Katsayıları ---
# (f_heat_transfer, f_pressure_drop, f_mixing), toplamları = 1.0
ENTROPY_DECOMPOSITION_FRACTIONS: Dict[str, Dict[str, Tuple[float, float, float]]] = {
    # Bölüm 2.2'deki tam tablo burada
    ...
}

# --- Bejan Sayısı Not Sınırları ---
# N_s düşük → iyi (tersinire yakın)
BEJAN_GRADES = {
    "A": (0.00, 0.15),   # Mükemmel — çok düşük tersinmezlik
    "B": (0.15, 0.30),   # İyi
    "C": (0.30, 0.50),   # Orta
    "D": (0.50, 0.70),   # Zayıf — ciddi tersinmezlik
    "F": (0.70, 1.01),   # Kritik — çok yüksek tersinmezlik
}

# Not: N_s düşük = iyi, bu exergy verimi ile ters orantılı
# N_s = 0.20 → η_ex = 80% → "B" notu
# N_s = 0.60 → η_ex = 40% → "D" notu
```

### 3.4 Ana Fonksiyonlar

#### 3.4.1 `analyze_entropy_generation()` — Ana Giriş Noktası

```python
def analyze_entropy_generation(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
    T0_K: float = 298.15,
) -> EntropyGenerationResult:
    """
    Fabrika ekipmanları için EGM analizi.
    
    Args:
        equipment_list: Fabrika ekipman listesi
        analysis_results: Her ekipmanın analiz sonuçları {id: result_dict}
        T0_K: Ölü durum sıcaklığı (K), varsayılan 298.15 K (25°C)
    
    Returns:
        EntropyGenerationResult
    """
    # 1. Geçerli ekipmanları filtrele
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    if len(valid) < 1:
        return EntropyGenerationResult(
            is_valid=False,
            error_message="En az 1 ekipman gerekli",
            # ... boş değerler
        )
    
    # 2. Her ekipman için EGM hesapla
    equipment_results = []
    for item in valid:
        result = analysis_results[item["id"]]
        eq_result = _analyze_single_equipment(item, result, T0_K)
        equipment_results.append(eq_result)
    
    # 3. Fabrika metrikleri
    factory_metrics = _calculate_factory_metrics(equipment_results, T0_K)
    
    # 4. Tersinmezlik sıralaması (N_s bazlı)
    ranking = _create_irreversibility_ranking(equipment_results)
    
    # 5. Dekompozisyon chart verisi
    decomp_chart = _generate_decomposition_chart(equipment_results)
    
    # 6. Bejan sayısı chart verisi
    bejan_chart = _generate_bejan_chart(equipment_results)
    
    # 7. Uyarılar
    warnings = _collect_warnings(equipment_results, factory_metrics)
    
    return EntropyGenerationResult(
        num_equipment=len(equipment_results),
        T0_K=T0_K,
        equipment_results=equipment_results,
        irreversibility_ranking=ranking,
        decomposition_chart_data=decomp_chart,
        bejan_number_chart_data=bejan_chart,
        warnings=warnings,
        **factory_metrics,
    )
```

#### 3.4.2 `_analyze_single_equipment()` — Tek Ekipman EGM

```python
def _analyze_single_equipment(
    item: dict,
    result: dict,
    T0_K: float,
) -> EntropyEquipmentResult:
    """Tek ekipman için EGM hesapları."""
    eq_type = item["equipment_type"]
    subtype = item.get("subtype", "_default")
    
    # Mevcut exergy verilerini al
    I_dot = result.get("exergy_destroyed_kW", 0)
    E_x_in = result.get("exergy_in_kW", 0)
    eta_ex = result.get("exergy_efficiency_pct", 0) / 100.0
    avoidable_ratio = result.get("avoidable_ratio_pct", 0) / 100.0
    
    # Gouy-Stodola
    S_gen = I_dot / T0_K if T0_K > 0 else 0
    
    # Bejan sayısı (termodinamik)
    N_s = I_dot / E_x_in if E_x_in > 0 else 0
    # Alternatif: N_s = 1 - eta_ex (aynı sonucu verir)
    N_s = max(0, min(1.0, N_s))  # Clamp
    N_s_grade = _assign_bejan_grade(N_s)
    
    # Entropi dekompozisyonu
    fractions = _get_decomposition_fractions(eq_type, subtype)
    S_gen_ht = S_gen * fractions[0]    # Isı transferi
    S_gen_dp = S_gen * fractions[1]    # Basınç düşüşü
    S_gen_mix = S_gen * fractions[2]   # Karışma
    
    # Baskın mekanizma
    dominant = _get_dominant_mechanism(S_gen_ht, S_gen_dp, S_gen_mix)
    
    # Isı transferi Bejan sayısı (sadece HX)
    Be_ht = None
    if eq_type == "heat_exchanger":
        denom = S_gen_ht + S_gen_dp
        Be_ht = S_gen_ht / denom if denom > 0 else None
    
    # Augmentation number
    N_s_a = 1.0 - avoidable_ratio  # = S_gen,unavoidable / S_gen
    improvement_pct = avoidable_ratio * 100
    
    # Spesifik entropi üretimi
    s_gen_per_ex = S_gen / E_x_in if E_x_in > 0 else 0
    
    return EntropyEquipmentResult(
        equipment_id=item["id"],
        equipment_name=item.get("name", f"{eq_type}_{item['id'][:4]}"),
        equipment_type=eq_type,
        subtype=subtype,
        exergy_in_kW=E_x_in,
        exergy_destroyed_kW=I_dot,
        exergy_efficiency_pct=eta_ex * 100,
        S_gen_kW_K=S_gen,
        T0_K=T0_K,
        N_s=N_s,
        N_s_grade=N_s_grade,
        S_gen_heat_transfer_kW_K=S_gen_ht,
        S_gen_pressure_drop_kW_K=S_gen_dp,
        S_gen_mixing_kW_K=S_gen_mix,
        dominant_mechanism=dominant,
        Be_heat_transfer=Be_ht,
        N_s_augmentation=N_s_a,
        improvement_potential_pct=improvement_pct,
        s_gen_per_exergy_input=s_gen_per_ex,
    )
```

#### 3.4.3 Yardımcı Fonksiyonlar

```python
def _filter_valid_equipment(equipment_list, analysis_results):
    """exergy_destroyed_kW > 0 ve exergy_in_kW > 0 olan ekipmanlar."""
    valid = []
    for item in equipment_list:
        result = analysis_results.get(item.get("id", ""))
        if result and result.get("exergy_destroyed_kW", 0) > 0 and result.get("exergy_in_kW", 0) > 0:
            valid.append(item)
    return valid


def _assign_bejan_grade(N_s: float) -> str:
    """Bejan sayısına göre kalite notu."""
    for grade, (low, high) in BEJAN_GRADES.items():
        if low <= N_s < high:
            return grade
    return "F"


def _get_decomposition_fractions(eq_type: str, subtype: str) -> Tuple[float, float, float]:
    """Ekipman tipi ve alt tipine göre dekompozisyon katsayıları."""
    type_fractions = ENTROPY_DECOMPOSITION_FRACTIONS.get(eq_type, {})
    fractions = type_fractions.get(subtype, type_fractions.get("_default", (0.33, 0.34, 0.33)))
    return fractions


def _get_dominant_mechanism(S_ht: float, S_dp: float, S_mix: float) -> str:
    """Baskın entropi üretim mekanizması."""
    mechanisms = {
        "heat_transfer": S_ht,
        "pressure_drop": S_dp,
        "mixing": S_mix,
    }
    return max(mechanisms, key=mechanisms.get)


def _calculate_factory_metrics(equipment_results, T0_K):
    """Fabrika seviyesi EGM metrikleri."""
    S_total = sum(r.S_gen_kW_K for r in equipment_results)
    S_ht = sum(r.S_gen_heat_transfer_kW_K for r in equipment_results)
    S_dp = sum(r.S_gen_pressure_drop_kW_K for r in equipment_results)
    S_mix = sum(r.S_gen_mixing_kW_K for r in equipment_results)
    E_x_in_total = sum(r.exergy_in_kW for r in equipment_results)
    I_total = sum(r.exergy_destroyed_kW for r in equipment_results)
    
    N_s_factory = (S_total * T0_K) / E_x_in_total if E_x_in_total > 0 else 0
    
    dominant = _get_dominant_mechanism(S_ht, S_dp, S_mix)
    
    return {
        "S_gen_total_kW_K": S_total,
        "N_s_factory": N_s_factory,
        "S_gen_heat_transfer_total_kW_K": S_ht,
        "S_gen_pressure_drop_total_kW_K": S_dp,
        "S_gen_mixing_total_kW_K": S_mix,
        "dominant_mechanism_factory": dominant,
        "heat_transfer_pct": (S_ht / S_total * 100) if S_total > 0 else 0,
        "pressure_drop_pct": (S_dp / S_total * 100) if S_total > 0 else 0,
        "mixing_pct": (S_mix / S_total * 100) if S_total > 0 else 0,
        "total_exergy_destroyed_kW": I_total,
    }


def _create_irreversibility_ranking(equipment_results):
    """N_s bazlı tersinmezlik sıralaması (büyükten küçüğe)."""
    ranked = sorted(equipment_results, key=lambda r: r.N_s, reverse=True)
    return [
        {
            "equipment_id": r.equipment_id,
            "equipment_name": r.equipment_name,
            "equipment_type": r.equipment_type,
            "N_s": round(r.N_s, 4),
            "N_s_grade": r.N_s_grade,
            "S_gen_kW_K": round(r.S_gen_kW_K, 6),
            "dominant_mechanism": r.dominant_mechanism,
            "improvement_potential_pct": round(r.improvement_potential_pct, 1),
        }
        for r in ranked
    ]


def _generate_decomposition_chart(equipment_results):
    """Entropi dekompozisyon stacked bar chart verisi."""
    # N_s'e göre azalan sıralı
    sorted_results = sorted(equipment_results, key=lambda r: r.N_s, reverse=True)
    return {
        "equipment_names": [r.equipment_name for r in sorted_results],
        "heat_transfer_kW_K": [round(r.S_gen_heat_transfer_kW_K, 6) for r in sorted_results],
        "pressure_drop_kW_K": [round(r.S_gen_pressure_drop_kW_K, 6) for r in sorted_results],
        "mixing_kW_K": [round(r.S_gen_mixing_kW_K, 6) for r in sorted_results],
    }


def _generate_bejan_chart(equipment_results):
    """Bejan sayısı bar chart verisi (not renkleri ile)."""
    sorted_results = sorted(equipment_results, key=lambda r: r.N_s, reverse=True)
    
    GRADE_COLORS = {
        "A": "#22c55e",  # Yeşil
        "B": "#84cc16",  # Açık yeşil
        "C": "#f59e0b",  # Turuncu
        "D": "#ef4444",  # Kırmızı
        "F": "#991b1b",  # Koyu kırmızı
    }
    
    return {
        "equipment_names": [r.equipment_name for r in sorted_results],
        "N_s_values": [round(r.N_s, 4) for r in sorted_results],
        "grades": [r.N_s_grade for r in sorted_results],
        "colors": [GRADE_COLORS.get(r.N_s_grade, "#9ca3af") for r in sorted_results],
    }


def _collect_warnings(equipment_results, factory_metrics):
    """EGM uyarıları."""
    warnings = []
    
    # Yüksek N_s uyarısı
    high_ns = [r for r in equipment_results if r.N_s > 0.70]
    if high_ns:
        names = ", ".join(r.equipment_name for r in high_ns[:3])
        warnings.append(f"Kritik tersinmezlik (N_s > 0.70): {names}")
    
    # Fabrika N_s uyarısı
    if factory_metrics.get("N_s_factory", 0) > 0.50:
        warnings.append(f"Fabrika geneli yüksek tersinmezlik (N_s = {factory_metrics['N_s_factory']:.2f})")
    
    # Düşük entropi üretimi
    if factory_metrics.get("S_gen_total_kW_K", 0) < 0.01:
        warnings.append("Çok düşük toplam entropi üretimi — EGM analizi sınırlı fayda sağlayabilir")
    
    return warnings


def check_egm_feasibility(
    equipment_list: List[dict],
    analysis_results: Dict[str, dict],
) -> Tuple[bool, List[str]]:
    """
    EGM analizinin anlamlı olup olmadığını kontrol et.
    
    Gereksinimler:
    - En az 1 ekipman
    - En az 1 ekipmanda exergy_in_kW > 0 ve exergy_destroyed_kW > 0
    """
    warnings = []
    valid = _filter_valid_equipment(equipment_list, analysis_results)
    
    if len(valid) < 1:
        return False, ["Geçerli ekipman yok"]
    
    return True, warnings
```

---

## 4. API Entegrasyonu

### 4.1 Factory Engine'e Ekleme

`engine/factory.py` → `analyze_factory()` içine, advanced_exergy'den sonra:

```python
# 8. EGM — Entropy Generation Minimization (opsiyonel, best-effort)
entropy_generation = None
try:
    from .entropy_generation import analyze_entropy_generation, check_egm_feasibility
    # equipment dict listesi ve results_dict önceki adımlarda oluşturulmuş
    feasible, _ = check_egm_feasibility(eq_list_dicts, adv_results_dict)
    if feasible:
        egm_result = analyze_entropy_generation(eq_list_dicts, adv_results_dict)
        if egm_result.is_valid:
            entropy_generation = egm_result.to_dict()
except Exception as e:
    logger.warning(f"EGM analysis failed: {e}")
```

`FactoryAnalysisResult`'a ekle:
```python
entropy_generation: Optional[dict] = None
```

### 4.2 Ayrı Endpoint

```python
@router.post("/factory/projects/{project_id}/entropy-generation")
async def run_entropy_generation(project_id, db, current_user):
    """Fabrika projesi için EGM analizi."""
```

### 4.3 AI Prompt Entegrasyonu

```python
def _format_egm_for_prompt(egm_data: dict) -> str:
    """EGM özetini AI prompt'u için formatla. Max ~400 karakter."""
    if not egm_data or not egm_data.get("is_valid"):
        return ""
    
    lines = [
        "\n## Entropi Üretimi Analizi (EGM)",
        f"- Toplam S_gen: {egm_data.get('S_gen_total_kW_K', 0):.4f} kW/K | N_s fabrika: {egm_data.get('N_s_factory', 0):.3f}",
        f"- Dağılım: ΔT %{egm_data.get('heat_transfer_pct', 0):.0f} | ΔP %{egm_data.get('pressure_drop_pct', 0):.0f} | Karışma %{egm_data.get('mixing_pct', 0):.0f}",
        f"- Baskın mekanizma: {egm_data.get('dominant_mechanism_factory', 'N/A')}",
    ]
    
    # En tersinmez 3 ekipman
    ranking = egm_data.get("irreversibility_ranking", [])[:3]
    if ranking:
        lines.append("- En tersinmez: " + ", ".join(
            f"{r['equipment_name']}(N_s={r['N_s']:.2f},{r['N_s_grade']})" for r in ranking
        ))
    
    result = "\n".join(lines)
    return result[:400] if len(result) > 400 else result
```

---

## 5. Frontend Entegrasyonu

### 5.1 Component Yapısı

```
frontend/src/components/entropy-generation/
├── EntropyDecompositionChart.jsx     # Stacked bar: ΔT + ΔP + mix per equipment
├── BejanNumberChart.jsx              # Bar chart: N_s per equipment (not renkleri)
├── EGMMetricBar.jsx                  # Özet kartlar
├── IrreversibilityRanking.jsx        # N_s sıralaması
├── EntropyGenerationTab.jsx          # Ana bileşen
```

### 5.2 Wireframe

```
+----------------------------------------------------------+
| Entropi Üretimi Analizi (EGM)                            |
+----------------------------------------------------------+
|                                                          |
| +-- Özet Kartlar --+                                    |
| | S_gen: 0.0234 | N_s: 0.42  | Baskın: ΔT  |          |
| | ΔT: 52%       | ΔP: 31%    | Mix: 17%    |          |
| +------------------+                                    |
|                                                          |
| +-- Bejan Sayısı Chart ------+                          |
| |                             |                          |
| | Kazan-1     [████████] 0.65 D                         |
| | Dryer-1     [███████░] 0.58 D                         |
| | Chiller-1   [█████░░░] 0.42 C                         |
| | HX-1        [████░░░░] 0.32 C                         |
| | Kompresör-1 [██░░░░░░] 0.18 B                         |
| |                             |                          |
| | Renkler: ■A ■B ■C ■D ■F   |                          |
| +-----------------------------+                          |
|                                                          |
| +-- Entropi Dekompozisyonu ---+                          |
| |                             |                          |
| | Kazan-1     [▓▓▓░░░████████] (ΔT + ΔP + Mix)         |
| | Dryer-1     [▓▓▓▓░░░█████░░]                          |
| | Chiller-1   [▓▓▓▓▓▓░░░░░░░░]                          |
| | HX-1        [▓▓▓▓▓▓▓▓░░░░░░]                          |
| | Kompresör-1 [▓▓░░░░░░░░░░░░]                          |
| |                             |                          |
| | ■ Isı Transferi  ■ Basınç Düşüşü  ■ Karışma          |
| +-----------------------------+                          |
|                                                          |
| +-- Tersinmezlik Sıralaması -+                          |
| | 1. Kazan-1    | N_s=0.65 D | İyileş: %35 | Mix baskın|
| | 2. Dryer-1    | N_s=0.58 D | İyileş: %28 | ΔT+Mix   |
| | 3. Chiller-1  | N_s=0.42 C | İyileş: %22 | ΔT baskın|
| +-----------------------------+                          |
+----------------------------------------------------------+
```

### 5.3 Renk Paleti

| Mekanizma | Renk | Hex |
|-----------|------|-----|
| Isı Transferi (ΔT) | Kırmızı-turuncu | #f97316 |
| Basınç Düşüşü (ΔP) | Mavi | #3b82f6 |
| Karışma/Kimyasal | Mor | #8b5cf6 |

| Not | N_s Aralığı | Renk | Hex |
|-----|-------------|------|-----|
| A | 0.00 - 0.15 | Koyu yeşil | #22c55e |
| B | 0.15 - 0.30 | Açık yeşil | #84cc16 |
| C | 0.30 - 0.50 | Turuncu | #f59e0b |
| D | 0.50 - 0.70 | Kırmızı | #ef4444 |
| F | 0.70 - 1.00 | Koyu kırmızı | #991b1b |

### 5.4 FactoryDashboard Entegrasyonu

```
FactoryDashboard kart sırası:
  1. MetricBar (mevcut)
  2. PriorityList + IntegrationPanel (mevcut)
  3. FactorySankey (mevcut)
  4. PinchTab (BRIEF_24)
  5. AdvancedExergyTab (BRIEF_26)
  6. EntropyGenerationTab (BRIEF_27 — YENİ)
  7. FactoryAIPanel (mevcut)
```

---

## 6. Testler

### 6.1 `tests/test_entropy_generation.py`

Tahmini: **~350 satır, 30+ test**

```python
class TestGouyStodola:
    """Gouy-Stodola teoremi testleri."""
    
    def test_S_gen_equals_I_dot_over_T0(self):
        """S_gen = I_dot / T₀."""
    
    def test_S_gen_zero_when_no_destruction(self):
        """I_dot = 0 → S_gen = 0."""
    
    def test_S_gen_with_custom_T0(self):
        """Farklı T₀ değerinde doğru S_gen."""
    
    def test_gouy_stodola_consistency(self):
        """T₀ × S_gen = I_dot (geri doğrulama)."""


class TestBejanNumber:
    """Bejan sayısı (N_s) testleri."""
    
    def test_N_s_equals_1_minus_eta_ex(self):
        """N_s ≈ 1 - η_ex."""
    
    def test_N_s_clamped_0_to_1(self):
        """0 ≤ N_s ≤ 1."""
    
    def test_N_s_zero_for_ideal(self):
        """η_ex = 100% → N_s = 0."""
    
    def test_N_s_grade_assignment(self):
        """N_s → doğru not (A-F)."""
    
    def test_all_grades_covered(self):
        """Her not aralığı test edildi."""


class TestEntropyDecomposition:
    """Entropi dekompozisyonu testleri."""
    
    def test_fractions_sum_to_one(self):
        """f_ΔT + f_ΔP + f_mix = 1.0 (tüm ekipman tipleri)."""
    
    def test_components_sum_to_S_gen(self):
        """S_gen,ΔT + S_gen,ΔP + S_gen,mix = S_gen."""
    
    def test_compressor_pressure_dominant(self):
        """Kompresörde basınç baskın."""
    
    def test_boiler_mixing_dominant(self):
        """Kazanda karışma (yanma) baskın."""
    
    def test_heat_exchanger_ht_dominant(self):
        """Isı eşanjöründe ısı transferi baskın."""
    
    def test_pump_pressure_dominant(self):
        """Pompada basınç baskın."""
    
    def test_subtype_specific_fractions(self):
        """Alt tipe özel katsayı kullanılıyor."""
    
    def test_default_fractions_when_unknown_subtype(self):
        """Bilinmeyen alt tip → _default kullanılır."""


class TestHeatTransferBejan:
    """Isı transferi Bejan sayısı (Be) testleri — sadece HX."""
    
    def test_Be_only_for_heat_exchanger(self):
        """Be sadece heat_exchanger tipi için hesaplanır."""
    
    def test_Be_between_0_and_1(self):
        """0 ≤ Be ≤ 1."""
    
    def test_Be_none_for_non_hx(self):
        """Kompresör → Be = None."""


class TestAugmentationNumber:
    """Augmentation entropy generation number testleri."""
    
    def test_N_s_a_equals_1_minus_avoidable_ratio(self):
        """N_s,a = 1 - avoidable_ratio."""
    
    def test_improvement_pct_equals_avoidable_ratio(self):
        """İyileştirme potansiyeli = avoidable_ratio × 100."""
    
    def test_N_s_a_1_when_no_avoidable(self):
        """Kaçınılabilir yıkım yok → N_s,a = 1 (iyileştirme yok)."""


class TestFactoryMetrics:
    """Fabrika seviyesi EGM testleri."""
    
    def test_S_gen_total_sum(self):
        """Σ S_gen,k = S_gen_total."""
    
    def test_decomposition_totals_sum(self):
        """S_ht + S_dp + S_mix = S_gen_total."""
    
    def test_percentages_sum_to_100(self):
        """ΔT% + ΔP% + Mix% ≈ 100."""
    
    def test_N_s_factory_between_0_and_1(self):
        """0 ≤ N_s_factory ≤ 1."""


class TestEdgeCases:
    """Uç durumlar."""
    
    def test_single_equipment_valid(self):
        """Tek ekipman → is_valid=True (EN/EX'ten farklı)."""
    
    def test_zero_exergy_in_handled(self):
        """exergy_in = 0 → N_s = 0, hata yok."""
    
    def test_missing_avoidable_ratio(self):
        """avoidable_ratio eksik → N_s,a = 1 varsayılanı."""
    
    def test_serialization(self):
        """to_dict() → JSON sorunsuz."""


class TestIntegration:
    """Entegrasyon testleri."""
    
    def test_factory_analysis_includes_entropy_generation(self):
        """analyze_factory() sonucu entropy_generation alanı var."""
    
    def test_all_decomposition_fractions_valid(self):
        """Tüm ENTROPY_DECOMPOSITION_FRACTIONS toplamı 1.0."""
```

---

## 7. Uygulama Planı

### Faz 1: Engine (Öncelik 1)

| Adım | Dosya | İş |
|------|-------|----|
| 1.1 | `engine/entropy_generation.py` (YENİ) | Veri yapıları (EntropyEquipmentResult, EntropyGenerationResult) |
| 1.2 | `engine/entropy_generation.py` | Sabit veriler: ENTROPY_DECOMPOSITION_FRACTIONS (7 tip × tüm alt tipler), BEJAN_GRADES |
| 1.3 | `engine/entropy_generation.py` | `_filter_valid_equipment()`, `_assign_bejan_grade()`, `_get_decomposition_fractions()`, `_get_dominant_mechanism()` |
| 1.4 | `engine/entropy_generation.py` | `_analyze_single_equipment()` — Gouy-Stodola, N_s, dekompozisyon, Be (HX), N_s,a |
| 1.5 | `engine/entropy_generation.py` | `_calculate_factory_metrics()` |
| 1.6 | `engine/entropy_generation.py` | `_create_irreversibility_ranking()` |
| 1.7 | `engine/entropy_generation.py` | `_generate_decomposition_chart()`, `_generate_bejan_chart()` |
| 1.8 | `engine/entropy_generation.py` | `_collect_warnings()`, `check_egm_feasibility()` |
| 1.9 | `engine/entropy_generation.py` | `analyze_entropy_generation()` ana fonksiyon |
| 1.10 | `engine/__init__.py` | EGM export'ları ekle |

### Faz 2: Testler (Öncelik 1)

| Adım | Dosya | İş |
|------|-------|----|
| 2.1 | `tests/test_entropy_generation.py` (YENİ) | Test fixture'ları (çeşitli tip ekipmanlar) |
| 2.2 | `tests/test_entropy_generation.py` | Gouy-Stodola testleri (4 test) |
| 2.3 | `tests/test_entropy_generation.py` | Bejan sayısı testleri (5 test) |
| 2.4 | `tests/test_entropy_generation.py` | Dekompozisyon testleri (8 test) |
| 2.5 | `tests/test_entropy_generation.py` | HT Bejan + augmentation testleri (5 test) |
| 2.6 | `tests/test_entropy_generation.py` | Fabrika metrikleri testleri (4 test) |
| 2.7 | `tests/test_entropy_generation.py` | Edge case + entegrasyon (4 test) |
| 2.8 | Tüm testler | `pytest tests/ -v` regresyon kontrolü |

### Faz 3: API + Fabrika Entegrasyonu (Öncelik 2)

| Adım | Dosya | İş |
|------|-------|----|
| 3.1 | `engine/factory.py` | `FactoryAnalysisResult`'a `entropy_generation` alanı |
| 3.2 | `engine/factory.py` | `analyze_factory()` içinde EGM çağrısı |
| 3.3 | `api/schemas/factory.py` | `entropy_generation` alanı |
| 3.4 | `api/routes/factory.py` | `/entropy-generation` endpoint |
| 3.5 | `api/services/claude_code_service.py` | `_format_egm_for_prompt()` + prompt'a ekleme |

### Faz 4: Frontend (Öncelik 2)

| Adım | Dosya | İş |
|------|-------|----|
| 4.1 | `frontend/src/components/entropy-generation/` | Dizin oluştur |
| 4.2 | `BejanNumberChart.jsx` (YENİ) | Plotly bar chart (not renkleri) |
| 4.3 | `EntropyDecompositionChart.jsx` (YENİ) | Plotly stacked bar (ΔT turuncu, ΔP mavi, mix mor) |
| 4.4 | `EGMMetricBar.jsx` (YENİ) | Özet kartlar |
| 4.5 | `IrreversibilityRanking.jsx` (YENİ) | N_s sıralaması |
| 4.6 | `EntropyGenerationTab.jsx` (YENİ) | Ana bileşen |
| 4.7 | `FactoryDashboard.jsx` | EntropyGenerationTab entegrasyonu |
| 4.8 | `factoryApi.js` | `runEntropyGeneration()` ekle |

---

## 8. Doğrulama Kontrol Listesi

### Invariantlar
- [ ] S_gen = I_dot / T₀ (Gouy-Stodola, tolerans < 1e-8)
- [ ] T₀ × S_gen ≈ I_dot (geri doğrulama)
- [ ] 0 ≤ N_s ≤ 1
- [ ] S_gen,ΔT + S_gen,ΔP + S_gen,mix = S_gen (tolerans < 1e-8)
- [ ] f_ΔT + f_ΔP + f_mix = 1.0 (tüm ekipman tipi/alt tipleri için)
- [ ] 0 ≤ Be ≤ 1 (sadece HX)
- [ ] 0 ≤ N_s,a ≤ 1
- [ ] ΔT% + ΔP% + Mix% ≈ 100 (fabrika seviyesi)

### Testler
- [ ] `pytest tests/test_entropy_generation.py -v` — tüm testler geçiyor
- [ ] `pytest tests/ -v` — regresyon yok

### API
- [ ] `analyze_factory()` sonucu `entropy_generation` içeriyor
- [ ] `/entropy-generation` endpoint çalışıyor
- [ ] AI prompt boyutu < 35K

### Frontend
- [ ] Bejan chart not renkleri doğru
- [ ] Dekompozisyon chart 3 mekanizma gösteriyor
- [ ] entropy_generation = None ise bölüm gizleniyor

---

## 9. Claude Code Prompt

```
PROJECT_ANALYSIS.md ve BRIEF_27_ENTROPY_GENERATION.md dosyalarını oku.

Görev: ExergyLab'a Bejan'ın EGM (Entropy Generation Minimization) motor modülünü ekle.

Faz 1 — Engine modülü:
1. engine/entropy_generation.py dosyasını oluştur (~400-500 satır).
2. Veri yapıları: EntropyEquipmentResult ve EntropyGenerationResult (to_dict metodu ile). Brief 3.2.
3. Sabit veriler: ENTROPY_DECOMPOSITION_FRACTIONS (7 ekipman tipi × tüm alt tipler, her tuple toplamı = 1.0), BEJAN_GRADES. Brief 2.2 ve 3.3.
4. _filter_valid_equipment(): exergy_destroyed_kW > 0 ve exergy_in_kW > 0 olanları filtrele.
5. _assign_bejan_grade(): N_s → A(0-0.15), B(0.15-0.30), C(0.30-0.50), D(0.50-0.70), F(0.70+).
6. _get_decomposition_fractions(): eq_type + subtype → (f_ΔT, f_ΔP, f_mix) tuple, _default fallback.
7. _get_dominant_mechanism(): max(S_ht, S_dp, S_mix) → "heat_transfer" | "pressure_drop" | "mixing".
8. _analyze_single_equipment(): Gouy-Stodola (S_gen = I_dot/T₀), N_s (I_dot/E_x_in, clamp 0-1), dekompozisyon (S_gen × fractions), Be (sadece HX: S_ht/(S_ht+S_dp)), N_s,a (1 - avoidable_ratio). Brief 3.4.2.
9. _calculate_factory_metrics(): toplamlar, yüzdeler, N_s_factory, baskın mekanizma. Brief 3.4.3.
10. _create_irreversibility_ranking(): N_s büyükten küçüğe sıralama.
11. _generate_decomposition_chart(): stacked bar verisi (ΔT, ΔP, mix kW/K).
12. _generate_bejan_chart(): bar chart verisi (N_s + not renkleri).
13. _collect_warnings(): yüksek N_s, düşük S_gen uyarıları.
14. check_egm_feasibility(): min 1 geçerli ekipman.
15. analyze_entropy_generation(): ana fonksiyon, T0_K=298.15 parametresi.
16. engine/__init__.py güncelle.

Faz 2 — Testler:
17. tests/test_entropy_generation.py dosyasını oluştur (~350 satır, 30+ test).
18. Test fixture: karışık ekipman tipleri (kazan, kompresör, HX, chiller, pompa).
19. Gouy-Stodola testleri (4 test): S_gen = I_dot/T₀, sıfır yıkım, geri doğrulama.
20. Bejan sayısı testleri (5 test): N_s = 1 - η_ex, clamp, not ataması.
21. Dekompozisyon testleri (8 test): katsayı toplamları = 1.0, bileşen toplamı = S_gen, baskın mekanizma doğrulaması (kompresör→ΔP, kazan→mix, HX→ΔT).
22. HT Bejan + augmentation testleri (5 test): Be sadece HX, Be 0-1, N_s,a hesabı.
23. Fabrika metrikleri (4 test): toplamlar, yüzdeler ≈ 100, N_s_factory 0-1.
24. Edge case + entegrasyon (4 test): tek ekipman valid, sıfır exergy_in, serialization.
25. ENTROPY_DECOMPOSITION_FRACTIONS doğrulama: tüm tuple toplamları = 1.0.
26. pytest tests/test_entropy_generation.py -v çalıştır.
27. pytest tests/ -v çalıştır (regresyon kontrolü).

Faz 3 — API + Fabrika entegrasyonu:
28. engine/factory.py → FactoryAnalysisResult'a entropy_generation: Optional[dict] = None ekle.
29. engine/factory.py → analyze_factory() içinde EGM çağrısı (best-effort). Mevcut eq_list_dicts ve results_dict varsa yeniden oluştur, yoksa oluştur.
30. api/schemas/factory.py → entropy_generation alanı ekle.
31. api/routes/factory.py → analyze response'a entropy_generation ekle + POST /entropy-generation endpoint.
32. api/services/claude_code_service.py → _format_egm_for_prompt() (max 400 karakter) + fabrika prompt'una ekle.

Faz 4 — Frontend:
33. frontend/src/components/entropy-generation/ dizini oluştur.
34. BejanNumberChart.jsx — Plotly bar chart, not renkleri: A=#22c55e, B=#84cc16, C=#f59e0b, D=#ef4444, F=#991b1b.
35. EntropyDecompositionChart.jsx — Plotly stacked bar: ΔT=#f97316, ΔP=#3b82f6, Mix=#8b5cf6.
36. EGMMetricBar.jsx — S_gen, N_s, baskın mekanizma, dağılım yüzdeleri kartları.
37. IrreversibilityRanking.jsx — N_s sıralaması (PriorityList benzeri).
38. EntropyGenerationTab.jsx — Tüm componentleri birleştirir.
39. FactoryDashboard.jsx → EntropyGenerationTab ekle (AdvancedExergyTab'dan sonra).
40. factoryApi.js → runEntropyGeneration() ekle.

Önemli kurallar:
- EGM tek ekipman için bile çalışır (EN/EX'ten farklı — o 2+ gerektirir).
- Gouy-Stodola invariantı: T₀ × S_gen = I_dot.
- Tüm dekompozisyon katsayı tuple'ları toplamı = 1.0 olmalı.
- Be (heat transfer Bejan) sadece heat_exchanger tipi için hesaplanır, diğerlerinde None.
- N_s,a hesabında avoidable_ratio yoksa varsayılan 0 kullan (N_s,a = 1).
- Mevcut ekipman analiz sonuçlarından kullanılacak alanlar: exergy_in_kW, exergy_destroyed_kW, exergy_efficiency_pct, avoidable_ratio_pct.
```

---

## 10. Bilinen Kısıtlamalar

| Kısıtlama | Açıklama | Gelecek Çözüm |
|-----------|----------|---------------|
| Dekompozisyon katsayıları statik | Gerçek operasyon koşullarına değil literatür ortalamalarına dayalı | Operasyon parametrelerinden dinamik hesaplama |
| Bejan sayısı N_s = 1 - η_ex | Exergy veriminden doğrudan türetiliyor, bağımsız hesaplama değil | CoolProp tabanlı entropi hesabı |
| Tek operasyon noktası | Part-load ve değişken yük koşulları yok | Yük profili tabanlı EGM |
| Isı eşanjörü Be yaklaşık | Gerçek ΔT ve ΔP ölçümüne değil katsayılara dayalı | NTU-ε yönteminden hesaplama |

---

*BRIEF_27 — Entropy Generation Minimization (EGM) Motor Modülü*
*Yazar: Claude (ExergyLab geliştirme desteği)*
*Tarih: 2026-02-06*
*Bağımlılık: Mevcut exergy motorları, BRIEF_26 (Advanced Exergy)*
