# BRIEF_24: Pinch Analizi Motor Modülü

> **Tarih:** 2026-02-05
> **Öncelik:** Yüksek
> **Tahmini Süre:** 6-8 saat
> **Karmaşıklık:** Yüksek
> **Bağımlılıklar:** BRIEF_22 (exergoekonomik — tamamlandı), mevcut fabrika modülü
> **Etkilenen Dosyalar:** Yeni + mevcut toplam ~15 dosya

---

## 1. Bağlam ve Motivasyon

### 1.1 Neden Pinch Analizi?

ExergyLab şu an tekil ekipman exergy analizinde çok güçlü (7 tip, 46 alt tip, SPECO). Fabrika modülü ekipmanları bir araya getirip hotspot tespiti ve basit entegrasyon fırsatları sunuyor. Ancak **ısı entegrasyonu** konusunda somut, rakamsal hedefler veremiyor.

Pinch analizi bu boşluğu doldurur:
- "Bu fabrikada minimum ne kadar dış ısıtma/soğutma gerekir?" sorusuna **termodinamik olarak kanıtlanmış** cevap verir
- Mevcut ısı geri kazanım fırsatlarını kW ve EUR cinsinden somutlaştırır
- Ekipmanlar arası ısı eşleştirmelerini (HEN — Heat Exchanger Network) sistematik olarak önerir

### 1.2 Knowledge Base Durumu

`knowledge/factory/pinch/` dizininde ~18 dosya zaten mevcut. Uygulama koşulu: **3+ sıcak/soğuk akış, toplam ısı > 500 kW**. AI yorumlama altyapısı hazır — eksik olan hesaplama motoru ve görselleştirme.

### 1.3 Hedef Çıktı

Fabrika analizi çalıştırıldığında, yeterli termal akış varsa otomatik olarak pinch analizi de yapılacak. Sonuçlar:
- Composite Curves (sıcak ve soğuk birleşik eğriler)
- Grand Composite Curve (GCC)
- Pinch noktası (T_pinch, ΔT_min)
- Enerji hedefleri (QH_min, QC_min)
- Mevcut vs. hedef karşılaştırması
- HEN eşleştirme önerileri
- Tasarruf potansiyeli (kW, EUR/yıl)

---

## 2. Pinch Analizi Teorisi — Uygulama Referansı

### 2.1 Temel Kavramlar

**Pinch noktası**, bir prosesin ısı geri kazanım potansiyelinin termodinamik sınırını tanımlar. Linnhoff & Hindmarsh (1983) metodolojisi:

```
Temel Kural: Pinch noktasının üstünde sadece dış ısıtma,
             altında sadece dış soğutma yapılmalı.

Pinch İhlalleri:
  1. Pinch üstünden soğutma → QC_excess
  2. Pinch altından ısıtma  → QH_excess
  3. Pinch üzerinden ısı transferi → her iki tarafta fazla yük
```

### 2.2 Hesaplama Adımları

```
Adım 1: Akış Çıkarma (Stream Extraction)
  - Her ekipmandan sıcak ve soğuk akışları çıkar
  - Her akış: T_supply, T_target, Q_dot (kW), CP (kW/K)

Adım 2: Shifted Temperature (Kaydırılmış Sıcaklık)
  - Sıcak akışlar: T_shifted = T_actual - ΔT_min/2
  - Soğuk akışlar: T_shifted = T_actual + ΔT_min/2

Adım 3: Sıcaklık Aralıkları (Temperature Intervals)
  - Tüm shifted sıcaklıkları sırala
  - Ardışık aralıklar oluştur

Adım 4: Enerji Dengesi (Her aralık için)
  - ΔH_interval = (ΣCP_hot - ΣCP_cold) × ΔT_interval
  - Pozitif: ısı fazlası (soğutma gerekir)
  - Negatif: ısı açığı (ısıtma gerekir)

Adım 5: Kaskad (Cascade / Problem Table)
  - Yukarıdan aşağı ısı kaskadı
  - Negatif minimum → pinch noktası
  - QH_min = |minimum negatif değer|
  - QC_min = son kaskad değeri + QH_min

Adım 6: Grand Composite Curve
  - Düzeltilmiş kaskad: her aralıkta net ısı akışı
  - T_shifted vs. net ısı → GCC çizimi
  - GCC'nin x-eksenine dokunduğu nokta = pinch
```

### 2.3 ΔT_min Seçimi

| Endüstri / Uygulama | Tipik ΔT_min (°C) |
|----------------------|---------------------|
| Petrokimya | 10-20 |
| Kimya | 10-15 |
| Gıda | 5-10 |
| Tekstil | 10-15 |
| Kağıt/Selüloz | 10-20 |
| Enerji santrali | 5-10 |
| Genel endüstri | 10 (varsayılan) |

---

## 3. Akış Çıkarma (Stream Extraction) — Kritik Tasarım

### 3.1 Genel Yaklaşım

Her ekipman analizi zaten sıcaklık, basınç ve ısı akışı değerlerini hesaplıyor. Pinch modülü bu sonuçlardan termal akışları çıkaracak.

**Veri yapısı:**

```python
@dataclass
class ThermalStream:
    """Pinch analizi için termal akış."""
    stream_id: str              # "boiler_1_flue_gas"
    stream_type: str            # "hot" veya "cold"
    equipment_name: str         # "Kazan-1"
    equipment_type: str         # "boiler"
    description: str            # "Baca gazı (soğutma)"
    T_supply_C: float           # Kaynak sıcaklığı (°C)
    T_target_C: float           # Hedef sıcaklığı (°C)
    Q_dot_kW: float             # Isı yükü (kW)
    CP_kW_per_K: float          # Isı kapasitesi akış hızı (kW/K)
    # CP = Q / |T_supply - T_target|
    
    # Opsiyonel metadata
    fluid: str = "unknown"      # "air", "water", "steam", "flue_gas", vb.
    phase_change: bool = False  # Faz değişimi var mı (buharlaşma/yoğuşma)
    latent_heat_kW: float = 0.0 # Faz değişimi varsa gizli ısı bileşeni
```

### 3.2 Ekipman Bazlı Akış Çıkarma Kuralları

Her ekipman tipi için hangi akışlar çıkarılacak:

#### Kazan (Boiler)
```
HOT akış: Baca gazı soğutma
  - T_supply = T_flue_gas (baca gazı sıcaklığı)
  - T_target = T_stack (baca çıkış sıcaklığı, ~150°C veya input'taki değer)
  - Q = recoverable_heat_kW (zaten hesaplanıyor)
  - Not: waste_heat boiler hariç (zaten atık ısıyı kullanıyor)

COLD akış: Besleme suyu ısıtma
  - T_supply = T_feedwater (besleme suyu sıcaklığı)
  - T_target = T_steam (buhar sıcaklığı)
  - Q = useful_heat_kW
  - Not: Faz değişimi içerir (buharlaşma) — linearizasyon gerekebilir
```

#### Kompresör (Compressor)
```
HOT akış: Sıkıştırılmış hava/gaz soğutma (aftercooler)
  - T_supply = T_outlet (kompresör çıkış sıcaklığı)
  - T_target = T_ambient + 10°C (aftercooler çıkışı, ~40-45°C)
  - Q = recoverable_heat_kW
  - Not: Önemli ısı geri kazanım kaynağı! 60-90°C arası kullanılabilir ısı
```

#### Chiller
```
HOT akış: Kondenser atık ısısı
  - T_supply = T_condenser (~35-45°C)
  - T_target = T_ambient (~25-30°C)
  - Q = Q_condenser_kW (Q_evap + W_comp)
  - Not: Düşük sıcaklıklı ısı — genellikle entegrasyon değeri düşük

COLD akış: Soğutma yükü
  - T_supply = T_chilled_return (~12°C)
  - T_target = T_chilled_supply (~7°C)
  - Q = Q_evap_kW
```

#### Pompa (Pump)
```
Genellikle termal açıdan önemsiz (sıcaklık farkı < 1°C).
Sadece çok büyük pompalarda (>500 kW) ısınma kayda değer.
→ Varsayılan: Pinch'ten hariç tut. Opsiyonel flag ile dahil et.
```

#### Isı Eşanjörü (Heat Exchanger)
```
HOT akış: Sıcak taraf
  - T_supply = T_hot_in
  - T_target = T_hot_out
  - Q = Q_dot (transfer edilen ısı)

COLD akış: Soğuk taraf
  - T_supply = T_cold_in
  - T_target = T_cold_out
  - Q = Q_dot

Not: HX zaten bir entegrasyon elemanı. Pinch analizinde:
  - Eğer HX proses-proses ise: her iki akışı da dahil et (mevcut entegrasyonu gösterir)
  - Eğer HX utility kullanıyorsa: sadece proses tarafını dahil et
  → Basitleştirme: İlk versiyonda her iki tarafı da dahil et, 
    kullanıcı "utility" flag'i ile hariç tutabilsin
```

#### Buhar Türbini (Steam Turbine)
```
HOT akış: Çıkış buharı / egzoz
  - back_pressure: T_supply = T_exhaust, T_target = proses kullanım sıcaklığı
  - condensing: T_supply = T_exhaust, T_target = T_condenser (~40°C)
  - extraction: Ara çekiş akışı ek HOT akış olarak

  - Q = m_dot × (h_exhaust - h_target) veya doğrudan exhaust_heat_kW

COLD akış (CHP modunda):
  - Eğer proses ısısı kullanılıyorsa: proses ısıtma yükü
```

#### Kurutma Fırını (Dryer)
```
HOT akış: Egzoz havası
  - T_supply = T_exhaust (egzoz sıcaklığı, ~80-150°C)
  - T_target = T_ambient + 10°C
  - Q = recoverable_heat_kW
  - Not: Nemli hava — duyulur + gizli ısı ayrımı önemli ama ilk versiyonda 
    toplam olarak ele alınabilir

COLD akış: Malzeme ısıtma + buharlaştırma
  - T_supply = T_material_in
  - T_target = T_drying (kurutma sıcaklığı)
  - Q = Q_input_kW (toplam kurutma yükü)
```

### 3.3 Akış Çıkarma Fonksiyonu

```python
def extract_thermal_streams(
    equipment_list: List[EquipmentItem],
    analysis_results: Dict[str, ExergyResult],
    include_pumps: bool = False,
    include_utility_hx: bool = True,
) -> List[ThermalStream]:
    """
    Fabrika ekipmanlarından pinch analizi için termal akışları çıkarır.
    
    Her ekipman tipine özel çıkarma kuralları uygulanır.
    Minimum Q_dot eşiği: 5 kW (gürültüyü filtrele).
    
    Returns:
        hot_streams: List[ThermalStream] — sıcak akışlar
        cold_streams: List[ThermalStream] — soğuk akışlar
    """
```

### 3.4 Eksik Veri Yönetimi

Bazı ekipman analizlerinde akış çıkarmak için gerekli tüm sıcaklıklar doğrudan mevcut olmayabilir. Strateji:

| Durum | Çözüm |
|-------|-------|
| T_stack bilinmiyor (kazan) | Varsayılan 150°C kullan |
| T_aftercooler bilinmiyor (kompresör) | T_ambient + 15°C kullan |
| T_condenser bilinmiyor (chiller) | T_ambient + 10°C kullan |
| Q_recoverable = 0 | Bu akışı dahil etme |
| T_supply ≈ T_target (ΔT < 2°C) | Bu akışı dahil etme |

---

## 4. Engine Modülü: `engine/pinch.py`

### 4.1 Dosya Yapısı

Tahmini boyut: **~600-700 satır**

```python
"""
ExergyLab Pinch Analizi Motor Modülü

Linnhoff & Hindmarsh (1983) metodolojisi ile ısı entegrasyonu analizi.
Fabrika ekipmanlarından termal akışlar çıkarılır ve minimum enerji
hedefleri, pinch noktası, composite curve'ler ve HEN önerileri üretilir.

Referanslar:
  - Linnhoff, B. & Hindmarsh, E. (1983). "The pinch design method..."
  - Kemp, I.C. (2007). "Pinch Analysis and Process Integration"
  - Smith, R. (2005). "Chemical Process Design and Integration"
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
```

### 4.2 Veri Yapıları

```python
class StreamType(str, Enum):
    HOT = "hot"
    COLD = "cold"


@dataclass
class ThermalStream:
    """Pinch analizi için termal akış."""
    stream_id: str
    stream_type: StreamType
    equipment_name: str
    equipment_type: str
    description: str
    T_supply_C: float
    T_target_C: float
    Q_dot_kW: float
    CP_kW_per_K: float  # = Q / |ΔT|
    fluid: str = "unknown"
    phase_change: bool = False
    is_utility: bool = False  # True ise pinch'ten hariç tutulabilir


@dataclass
class TemperatureInterval:
    """Sıcaklık aralığı (Problem Table için)."""
    T_upper_C: float           # Aralık üst sıcaklığı (shifted)
    T_lower_C: float           # Aralık alt sıcaklığı (shifted)
    delta_T_C: float           # Sıcaklık farkı
    sum_CP_hot: float          # Bu aralıktaki toplam sıcak CP (kW/K)
    sum_CP_cold: float         # Bu aralıktaki toplam soğuk CP (kW/K)
    delta_H_kW: float          # Net ısı fazlası: (ΣCP_hot - ΣCP_cold) × ΔT
    cascade_kW: float = 0.0    # Kaskad değeri (Adım 5'te hesaplanır)


@dataclass
class PinchResult:
    """Pinch analizi sonuçları."""
    # Analiz parametreleri
    delta_T_min_C: float             # Kullanılan ΔT_min
    num_hot_streams: int             # Sıcak akış sayısı
    num_cold_streams: int            # Soğuk akış sayısı
    total_hot_duty_kW: float         # Toplam sıcak yük
    total_cold_duty_kW: float        # Toplam soğuk yük
    
    # Pinch noktası
    pinch_temperature_C: float       # Pinch sıcaklığı (gerçek, shifted değil)
    pinch_temperature_hot_C: float   # Sıcak taraf pinch: T_pinch + ΔT_min/2
    pinch_temperature_cold_C: float  # Soğuk taraf pinch: T_pinch - ΔT_min/2
    
    # Enerji hedefleri
    QH_min_kW: float                 # Minimum dış ısıtma ihtiyacı (hot utility)
    QC_min_kW: float                 # Minimum dış soğutma ihtiyacı (cold utility)
    max_heat_recovery_kW: float      # Maksimum ısı geri kazanım potansiyeli
    
    # Mevcut durum karşılaştırması
    QH_current_kW: float             # Mevcut dış ısıtma (kazan + diğer utility)
    QC_current_kW: float             # Mevcut dış soğutma (chiller + soğutma kuleleri)
    QH_excess_kW: float              # Fazla ısıtma: QH_current - QH_min
    QC_excess_kW: float              # Fazla soğutma: QC_current - QC_min
    cross_pinch_kW: float            # Pinch üzerinden transfer edilen ısı
    
    # Tasarruf
    savings_potential_kW: float      # QH_excess + QC_excess
    savings_potential_pct: float     # Tasarruf / mevcut toplam (%)
    annual_savings_kWh: float        # Yıllık tasarruf (kWh)
    annual_savings_EUR: float        # Yıllık tasarruf (EUR)
    
    # Görselleştirme verileri
    composite_curves: Dict           # Plotly composite curve verisi
    grand_composite_curve: Dict      # Plotly GCC verisi
    problem_table: List[Dict]        # Sıcaklık aralıkları tablosu
    
    # Akış bilgileri
    streams: List[Dict]              # Tüm akışlar (to_dict formatında)
    
    # HEN önerileri
    hen_matches: List[Dict]          # Önerilen ısı eşanjörü eşleştirmeleri
    
    # Uyarılar
    warnings: List[str]              # Analiz uyarıları
    
    # Yardımcı
    is_valid: bool = True            # Analiz geçerli mi
    error_message: str = ""          # Hata durumunda açıklama
    
    def to_dict(self) -> dict:
        """JSON serializasyonu."""
        ...
```

### 4.3 Ana Fonksiyonlar

#### 4.3.1 `analyze_pinch()` — Ana Giriş Noktası

```python
def analyze_pinch(
    equipment_list: List[EquipmentItem],
    analysis_results: Dict[str, dict],
    delta_T_min_C: float = 10.0,
    fuel_price_eur_kwh: float = 0.08,
    operating_hours: int = 8000,
    include_pumps: bool = False,
) -> PinchResult:
    """
    Fabrika ekipmanları için Linnhoff pinch analizi.
    
    Args:
        equipment_list: Fabrika ekipman listesi
        analysis_results: Her ekipmanın analiz sonuçları (dict formatında)
        delta_T_min_C: Minimum sıcaklık farkı (°C), varsayılan 10
        fuel_price_eur_kwh: Yakıt fiyatı (EUR/kWh), tasarruf hesabı için
        operating_hours: Yıllık çalışma saati
        include_pumps: Pompaları dahil et (genellikle False)
    
    Returns:
        PinchResult: Kapsamlı pinch analizi sonuçları
    
    Raises:
        ValueError: Yetersiz akış (< 1 sıcak + 1 soğuk) durumunda
    """
    # 1. Akış çıkarma
    streams = extract_thermal_streams(equipment_list, analysis_results, include_pumps)
    
    hot_streams = [s for s in streams if s.stream_type == StreamType.HOT]
    cold_streams = [s for s in streams if s.stream_type == StreamType.COLD]
    
    # 2. Yeterlilik kontrolü
    if len(hot_streams) < 1 or len(cold_streams) < 1:
        return PinchResult(is_valid=False, error_message="Yetersiz akış sayısı")
    
    # 3. Shifted sıcaklıklar
    shifted_temps = compute_shifted_temperatures(hot_streams, cold_streams, delta_T_min_C)
    
    # 4. Sıcaklık aralıkları
    intervals = create_temperature_intervals(hot_streams, cold_streams, shifted_temps)
    
    # 5. Problem tablosu ve kaskad
    intervals, QH_min, QC_min, pinch_idx = solve_cascade(intervals)
    
    # 6. Pinch noktası
    pinch_temp = compute_pinch_temperature(intervals, pinch_idx, delta_T_min_C)
    
    # 7. Composite curves
    cc_data = generate_composite_curves(hot_streams, cold_streams, delta_T_min_C)
    
    # 8. Grand Composite Curve
    gcc_data = generate_grand_composite_curve(intervals, QH_min)
    
    # 9. Mevcut durum karşılaştırması
    current = estimate_current_utility_usage(equipment_list, analysis_results)
    
    # 10. HEN eşleştirme önerileri
    hen = suggest_hen_matches(hot_streams, cold_streams, pinch_temp, delta_T_min_C)
    
    # 11. Sonuç derleme
    return PinchResult(...)
```

#### 4.3.2 `extract_thermal_streams()` — Akış Çıkarma

```python
def extract_thermal_streams(
    equipment_list: List[EquipmentItem],
    analysis_results: Dict[str, dict],
    include_pumps: bool = False,
) -> List[ThermalStream]:
    """Ekipman sonuçlarından termal akışlar çıkarır."""
    
    streams = []
    extractors = {
        "boiler": _extract_boiler_streams,
        "compressor": _extract_compressor_streams,
        "chiller": _extract_chiller_streams,
        "pump": _extract_pump_streams,
        "heat_exchanger": _extract_heat_exchanger_streams,
        "steam_turbine": _extract_steam_turbine_streams,
        "dryer": _extract_dryer_streams,
    }
    
    for item in equipment_list:
        if item.equipment_type == "pump" and not include_pumps:
            continue
        
        result = analysis_results.get(item.id)
        if not result:
            continue
        
        extractor = extractors.get(item.equipment_type)
        if extractor:
            extracted = extractor(item, result)
            streams.extend(extracted)
    
    # Minimum Q filtresi
    streams = [s for s in streams if s.Q_dot_kW >= 5.0]
    
    # Geçerlilik kontrolü: T_supply != T_target
    streams = [s for s in streams if abs(s.T_supply_C - s.T_target_C) >= 2.0]
    
    return streams
```

#### 4.3.3 Ekipman Bazlı Çıkarma Fonksiyonları

```python
def _extract_boiler_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Kazan akışları: baca gazı (HOT) + besleme suyu (COLD)."""
    streams = []
    params = item.parameters
    
    # HOT: Baca gazı soğutma
    T_flue = result.get("T_flue_gas_C") or params.get("flue_gas_temp_c", 200)
    T_stack = params.get("stack_temp_c", 150)
    Q_recoverable = result.get("recoverable_heat_kW", 0)
    
    if Q_recoverable > 5 and T_flue > T_stack + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_flue_gas",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="boiler",
            description="Baca gazı atık ısısı",
            T_supply_C=T_flue,
            T_target_C=T_stack,
            Q_dot_kW=Q_recoverable,
            CP_kW_per_K=Q_recoverable / max(T_flue - T_stack, 1),
            fluid="flue_gas",
        ))
    
    # COLD: Besleme suyu ısıtma (opsiyonel — yararlı çıktı)
    T_feedwater = params.get("feedwater_temp_c", 20)
    T_steam = params.get("steam_temp_c") or params.get("outlet_temp_c", 180)
    Q_useful = result.get("useful_heat_kW") or result.get("exergy_out_kW", 0)
    
    if Q_useful > 5 and T_steam > T_feedwater + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_feedwater",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="boiler",
            description="Besleme suyu ısıtma",
            T_supply_C=T_feedwater,
            T_target_C=T_steam,
            Q_dot_kW=Q_useful,
            CP_kW_per_K=Q_useful / max(T_steam - T_feedwater, 1),
            fluid="water",
            phase_change=True,
        ))
    
    return streams


def _extract_compressor_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Kompresör akışları: sıkıştırma ısısı (HOT)."""
    streams = []
    params = item.parameters
    
    T_outlet = result.get("T_outlet_C") or params.get("outlet_temp_c", 80)
    T_aftercooler = params.get("aftercooler_temp_c") or (params.get("inlet_temp_c", 25) + 15)
    Q_heat = result.get("recoverable_heat_kW", 0)
    
    # Eğer recoverable_heat yoksa, exergy destroyed'dan tahmin et
    if Q_heat <= 0:
        Q_heat = result.get("exergy_destroyed_kW", 0) * 0.7  # ~70% ısı olarak geri kazanılabilir
    
    if Q_heat > 5 and T_outlet > T_aftercooler + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_compression_heat",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="compressor",
            description="Sıkıştırma atık ısısı",
            T_supply_C=T_outlet,
            T_target_C=T_aftercooler,
            Q_dot_kW=Q_heat,
            CP_kW_per_K=Q_heat / max(T_outlet - T_aftercooler, 1),
            fluid="compressed_air",
        ))
    
    return streams


def _extract_chiller_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Chiller akışları: kondenser (HOT) + evaporatör (COLD)."""
    streams = []
    params = item.parameters
    
    # HOT: Kondenser atık ısısı
    T_cond = params.get("condenser_temp_c", 40)
    T_ambient = params.get("ambient_temp_c", 25)
    Q_evap = result.get("cooling_capacity_kW") or params.get("cooling_capacity_kw", 0)
    W_comp = result.get("power_input_kW") or params.get("power_input_kw", 0)
    Q_cond = Q_evap + W_comp  # Enerji dengesi
    
    if Q_cond > 5 and T_cond > T_ambient + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_condenser",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="chiller",
            description="Kondenser atık ısısı",
            T_supply_C=T_cond,
            T_target_C=T_ambient,
            Q_dot_kW=Q_cond,
            CP_kW_per_K=Q_cond / max(T_cond - T_ambient, 1),
            fluid="refrigerant",
        ))
    
    # COLD: Soğutma yükü
    T_return = params.get("chilled_water_return_c", 12)
    T_supply = params.get("chilled_water_supply_c", 7)
    
    if Q_evap > 5 and T_return > T_supply + 1:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_evaporator",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="chiller",
            description="Soğutma yükü",
            T_supply_C=T_return,  # Soğuk akışta supply = warm side
            T_target_C=T_supply,  # Target = cold side
            Q_dot_kW=Q_evap,
            CP_kW_per_K=Q_evap / max(T_return - T_supply, 1),
            fluid="chilled_water",
        ))
    
    return streams


def _extract_pump_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Pompa akışları: genellikle termal olarak önemsiz. Sadece büyük pompalarda."""
    # Pompa ısınması: ΔT = W_loss / (m_dot × Cp)
    # Genellikle < 1°C — pinch'te önemsiz
    return []


def _extract_heat_exchanger_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Isı eşanjörü akışları: sıcak taraf (HOT) + soğuk taraf (COLD)."""
    streams = []
    params = item.parameters
    
    # HOT: Sıcak taraf
    T_hot_in = params.get("hot_inlet_temp_c", 90)
    T_hot_out = params.get("hot_outlet_temp_c", 60)
    Q = result.get("heat_duty_kW") or params.get("heat_duty_kw", 0)
    
    if Q > 5 and T_hot_in > T_hot_out + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_hot_side",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="heat_exchanger",
            description="Sıcak taraf",
            T_supply_C=T_hot_in,
            T_target_C=T_hot_out,
            Q_dot_kW=Q,
            CP_kW_per_K=Q / max(T_hot_in - T_hot_out, 1),
            fluid="process_fluid",
        ))
    
    # COLD: Soğuk taraf
    T_cold_in = params.get("cold_inlet_temp_c", 20)
    T_cold_out = params.get("cold_outlet_temp_c", 50)
    
    if Q > 5 and T_cold_out > T_cold_in + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_cold_side",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="heat_exchanger",
            description="Soğuk taraf",
            T_supply_C=T_cold_in,
            T_target_C=T_cold_out,
            Q_dot_kW=Q,
            CP_kW_per_K=Q / max(T_cold_out - T_cold_in, 1),
            fluid="process_fluid",
        ))
    
    return streams


def _extract_steam_turbine_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Buhar türbini akışları: egzoz buharı (HOT)."""
    streams = []
    params = item.parameters
    
    T_inlet = params.get("inlet_temp_c", 400)
    T_exhaust = result.get("T_exhaust_C") or params.get("outlet_temp_c", 150)
    T_target = params.get("process_return_temp_c", 80)  # back_pressure: proses dönüş
    
    turbine_type = params.get("turbine_type", "back_pressure")
    
    # Egzoz ısısı
    Q_exhaust = result.get("exhaust_heat_kW") or result.get("recoverable_heat_kW", 0)
    
    if Q_exhaust <= 0:
        # Tahmin: türbin gücünün ~60-80%'i egzoz ısısı olarak
        W_shaft = result.get("power_output_kW", 0)
        Q_exhaust = W_shaft * 1.2  # Basit tahmin: Q_in ≈ W + Q_exhaust
    
    if turbine_type == "condensing":
        T_target = params.get("condenser_temp_c", 40)
    
    if Q_exhaust > 5 and T_exhaust > T_target + 2:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_exhaust",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="steam_turbine",
            description="Egzoz buharı/ısısı",
            T_supply_C=T_exhaust,
            T_target_C=T_target,
            Q_dot_kW=Q_exhaust,
            CP_kW_per_K=Q_exhaust / max(T_exhaust - T_target, 1),
            fluid="steam",
            phase_change=True if turbine_type == "condensing" else False,
        ))
    
    return streams


def _extract_dryer_streams(item: EquipmentItem, result: dict) -> List[ThermalStream]:
    """Kurutma fırını akışları: egzoz havası (HOT) + malzeme ısıtma (COLD)."""
    streams = []
    params = item.parameters
    
    # HOT: Egzoz havası
    T_exhaust = params.get("exhaust_temp_c") or params.get("outlet_air_temp_c", 80)
    T_ambient = params.get("ambient_temp_c", 25)
    Q_recoverable = result.get("recoverable_heat_kW", 0)
    
    if Q_recoverable <= 0:
        Q_input = result.get("heat_input_kW") or params.get("heat_input_kw", 0)
        Q_recoverable = Q_input * 0.25  # ~25% egzoz kaybı tahmini
    
    if Q_recoverable > 5 and T_exhaust > T_ambient + 5:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_exhaust_air",
            stream_type=StreamType.HOT,
            equipment_name=item.name,
            equipment_type="dryer",
            description="Egzoz havası atık ısısı",
            T_supply_C=T_exhaust,
            T_target_C=T_ambient + 5,  # Dew point'in biraz üstü
            Q_dot_kW=Q_recoverable,
            CP_kW_per_K=Q_recoverable / max(T_exhaust - (T_ambient + 5), 1),
            fluid="humid_air",
        ))
    
    # COLD: Kurutma yükü
    T_material_in = params.get("material_inlet_temp_c", 20)
    T_drying = params.get("drying_temp_c") or params.get("inlet_air_temp_c", 120)
    Q_input = result.get("heat_input_kW") or params.get("heat_input_kw", 0)
    
    if Q_input > 5 and T_drying > T_material_in + 5:
        streams.append(ThermalStream(
            stream_id=f"{item.id}_drying_load",
            stream_type=StreamType.COLD,
            equipment_name=item.name,
            equipment_type="dryer",
            description="Kurutma ısı yükü",
            T_supply_C=T_material_in,
            T_target_C=T_drying,
            Q_dot_kW=Q_input,
            CP_kW_per_K=Q_input / max(T_drying - T_material_in, 1),
            fluid="material",
        ))
    
    return streams
```

#### 4.3.4 `compute_shifted_temperatures()` — Sıcaklık Kaydırma

```python
def compute_shifted_temperatures(
    hot_streams: List[ThermalStream],
    cold_streams: List[ThermalStream],
    delta_T_min: float,
) -> List[float]:
    """
    Shifted sıcaklıkları hesapla ve sırala.
    
    Sıcak akışlar: T_shifted = T - ΔT_min/2
    Soğuk akışlar: T_shifted = T + ΔT_min/2
    
    Returns:
        Benzersiz ve sıralı shifted sıcaklıklar listesi (azalan sıra)
    """
    shift = delta_T_min / 2.0
    temps = set()
    
    for s in hot_streams:
        temps.add(s.T_supply_C - shift)
        temps.add(s.T_target_C - shift)
    
    for s in cold_streams:
        temps.add(s.T_supply_C + shift)
        temps.add(s.T_target_C + shift)
    
    return sorted(temps, reverse=True)  # En sıcaktan en soğuğa
```

#### 4.3.5 `create_temperature_intervals()` — Aralık Oluşturma

```python
def create_temperature_intervals(
    hot_streams: List[ThermalStream],
    cold_streams: List[ThermalStream],
    shifted_temps: List[float],
) -> List[TemperatureInterval]:
    """
    Shifted sıcaklıklar arasında aralıklar oluştur.
    Her aralık için aktif akışların CP toplamını hesapla.
    """
    intervals = []
    shift = ... # delta_T_min / 2
    
    for i in range(len(shifted_temps) - 1):
        T_upper = shifted_temps[i]
        T_lower = shifted_temps[i + 1]
        delta_T = T_upper - T_lower
        
        if delta_T < 0.001:
            continue
        
        # Bu aralıkta aktif olan akışları bul
        sum_CP_hot = 0.0
        for s in hot_streams:
            T_s_upper = s.T_supply_C - shift
            T_s_lower = s.T_target_C - shift
            if T_s_upper >= T_upper and T_s_lower <= T_lower:
                sum_CP_hot += s.CP_kW_per_K
        
        sum_CP_cold = 0.0
        for s in cold_streams:
            T_s_upper = s.T_target_C + shift
            T_s_lower = s.T_supply_C + shift
            if T_s_upper >= T_upper and T_s_lower <= T_lower:
                sum_CP_cold += s.CP_kW_per_K
        
        delta_H = (sum_CP_hot - sum_CP_cold) * delta_T
        
        intervals.append(TemperatureInterval(
            T_upper_C=T_upper,
            T_lower_C=T_lower,
            delta_T_C=delta_T,
            sum_CP_hot=sum_CP_hot,
            sum_CP_cold=sum_CP_cold,
            delta_H_kW=delta_H,
        ))
    
    return intervals
```

#### 4.3.6 `solve_cascade()` — Kaskad Çözümü

```python
def solve_cascade(
    intervals: List[TemperatureInterval],
) -> Tuple[List[TemperatureInterval], float, float, int]:
    """
    Problem Table Algorithm (Kaskad).
    
    1. İlk geçiş: Kaskad değerlerini hesapla (QH = 0 varsayımıyla)
    2. En negatif kaskad değerini bul → QH_min = |min_negative|
    3. İkinci geçiş: QH_min ekleyerek düzeltilmiş kaskad
    4. Kaskadın 0 olduğu nokta = pinch
    5. Son kaskad değeri = QC_min
    
    Returns:
        intervals: Güncellenmiş aralıklar (cascade_kW dolu)
        QH_min: Minimum dış ısıtma (kW)
        QC_min: Minimum dış soğutma (kW)
        pinch_idx: Pinch noktası aralık indeksi
    """
    # İlk geçiş
    cascade = [0.0]
    for interval in intervals:
        cascade.append(cascade[-1] + interval.delta_H_kW)
    
    # QH_min
    min_cascade = min(cascade)
    QH_min = -min_cascade if min_cascade < 0 else 0.0
    
    # Düzeltilmiş kaskad
    corrected = [c + QH_min for c in cascade]
    
    # Pinch: kaskadın 0 olduğu nokta
    pinch_idx = 0
    min_val = float('inf')
    for i, c in enumerate(corrected):
        if abs(c) < min_val:
            min_val = abs(c)
            pinch_idx = i
    
    # QC_min
    QC_min = corrected[-1]
    
    # Aralıklara kaskad değerlerini yaz
    for i, interval in enumerate(intervals):
        interval.cascade_kW = corrected[i + 1]
    
    return intervals, QH_min, QC_min, pinch_idx
```

#### 4.3.7 `generate_composite_curves()` — Composite Curve Verisi

```python
def generate_composite_curves(
    hot_streams: List[ThermalStream],
    cold_streams: List[ThermalStream],
    delta_T_min: float,
) -> Dict:
    """
    Sıcak ve soğuk composite curve'leri oluştur (Plotly formatında).
    
    Her curve: T vs. H (enthalpy) grafiği
    - X ekseni: Kümülatif enthalpy (kW)
    - Y ekseni: Sıcaklık (°C)
    
    Soğuk eğri, QH_min kadar sağa kaydırılarak pinch noktasında
    ΔT_min mesafede temas eder.
    
    Returns:
        {
            "hot_curve": {"H_kW": [...], "T_C": [...]},
            "cold_curve": {"H_kW": [...], "T_C": [...]},
            "pinch_point": {"H_kW": float, "T_hot_C": float, "T_cold_C": float},
            "QH_min_kW": float,
            "QC_min_kW": float,
        }
    """
    # Sıcak composite: tüm sıcak akışları birleştir
    hot_curve = _build_composite(hot_streams, is_hot=True)
    
    # Soğuk composite: tüm soğuk akışları birleştir
    cold_curve = _build_composite(cold_streams, is_hot=False)
    
    # Soğuk eğriyi QH_min kadar kaydır (pinch noktasında temas için)
    # ...
    
    return {
        "hot_curve": hot_curve,
        "cold_curve": cold_curve,
        "pinch_point": pinch_point,
        "QH_min_kW": QH_min,
        "QC_min_kW": QC_min,
    }


def _build_composite(streams: List[ThermalStream], is_hot: bool) -> Dict:
    """
    Birden fazla akışı tek bir composite curve'de birleştirir.
    
    Algoritma:
    1. Tüm akışların sıcaklık noktalarını topla ve sırala
    2. Her sıcaklık aralığında aktif akışların CP'sini topla
    3. ΔH = ΣCP × ΔT ile kümülatif enthalpy hesapla
    4. (T, H) noktalarını döndür
    """
    # Tüm sıcaklık noktalarını topla
    temp_points = set()
    for s in streams:
        temp_points.add(s.T_supply_C)
        temp_points.add(s.T_target_C)
    
    temp_points = sorted(temp_points, reverse=is_hot)
    
    # Kümülatif enthalpy
    H_cumulative = [0.0]
    T_points = [temp_points[0]]
    
    for i in range(len(temp_points) - 1):
        T_upper = max(temp_points[i], temp_points[i + 1])
        T_lower = min(temp_points[i], temp_points[i + 1])
        delta_T = T_upper - T_lower
        
        # Bu aralıkta aktif akışlar
        sum_CP = 0.0
        for s in streams:
            T_high = max(s.T_supply_C, s.T_target_C)
            T_low = min(s.T_supply_C, s.T_target_C)
            if T_high >= T_upper and T_low <= T_lower:
                sum_CP += s.CP_kW_per_K
        
        delta_H = sum_CP * delta_T
        H_cumulative.append(H_cumulative[-1] + delta_H)
        T_points.append(temp_points[i + 1])
    
    return {"H_kW": H_cumulative, "T_C": T_points}
```

#### 4.3.8 `generate_grand_composite_curve()` — GCC Verisi

```python
def generate_grand_composite_curve(
    intervals: List[TemperatureInterval],
    QH_min: float,
) -> Dict:
    """
    Grand Composite Curve (GCC) verisi.
    
    GCC: Shifted sıcaklık vs. net ısı akışı
    - X ekseni: Net kaskad ısı akışı (kW)
    - Y ekseni: Shifted sıcaklık (°C)
    - Pinch noktası: GCC'nin x=0'a dokunduğu yer
    
    Returns:
        {
            "H_kW": [...],     # Net ısı akışı değerleri
            "T_shifted_C": [...],  # Shifted sıcaklık değerleri
            "pinch_T_C": float,    # Pinch shifted sıcaklığı
        }
    """
    H_values = [QH_min]  # Üstten başla
    T_values = [intervals[0].T_upper_C]
    
    cascade = QH_min
    for interval in intervals:
        cascade -= interval.delta_H_kW  # veya uygun yön
        H_values.append(cascade)
        T_values.append(interval.T_lower_C)
    
    return {
        "H_kW": H_values,
        "T_shifted_C": T_values,
        "pinch_T_C": ...,  # Kaskadın 0'a en yakın olduğu T
    }
```

#### 4.3.9 `suggest_hen_matches()` — HEN Eşleştirme Önerileri

```python
def suggest_hen_matches(
    hot_streams: List[ThermalStream],
    cold_streams: List[ThermalStream],
    pinch_temp_C: float,
    delta_T_min: float,
) -> List[Dict]:
    """
    Pinch kurallarına uygun ısı eşanjörü eşleştirmeleri öner.
    
    Pinch Design Rules:
    1. Pinch üstü: sadece sıcak → soğuk eşleştirme (dış soğutma yok)
    2. Pinch altı: sadece soğuk → sıcak eşleştirme (dış ısıtma yok)
    3. CP kuralı: Pinch üstünde CP_hot ≤ CP_cold, altında CP_hot ≥ CP_cold
    
    Sezgisel eşleştirme:
    - Önce en büyük Q yüklerine sahip akışları eşleştir
    - Sıcaklık uyumluluğunu kontrol et (ΔT ≥ ΔT_min her noktada)
    - Fazliyetlik oranına göre utility ihtiyacını raporla
    
    Returns:
        [
            {
                "hot_stream": "kompresör_1_compression_heat",
                "cold_stream": "kazan_1_feedwater",
                "hot_equipment": "Kompresör-1",
                "cold_equipment": "Kazan-1",
                "Q_exchange_kW": 85.0,
                "T_hot_in": 90, "T_hot_out": 55,
                "T_cold_in": 20, "T_cold_out": 60,
                "region": "above_pinch",  # veya "below_pinch"
                "description": "Kompresör atık ısısı ile kazan besleme suyu ön ısıtma",
                "annual_savings_EUR": 54400,
                "estimated_hx_area_m2": 12.5,  # Opsiyonel: U × LMTD ile tahmin
                "payback_years": 1.8,
            },
            ...
        ]
    """
    matches = []
    
    # Akışları pinch üstü ve altı olarak ayır
    above_pinch_hot = [s for s in hot_streams if s.T_supply_C > pinch_temp_C]
    above_pinch_cold = [s for s in cold_streams if s.T_target_C > pinch_temp_C]
    below_pinch_hot = [s for s in hot_streams if s.T_target_C < pinch_temp_C]
    below_pinch_cold = [s for s in cold_streams if s.T_supply_C < pinch_temp_C]
    
    # Pinch üstü eşleştirme
    matches.extend(
        _match_streams(above_pinch_hot, above_pinch_cold, delta_T_min, "above_pinch")
    )
    
    # Pinch altı eşleştirme
    matches.extend(
        _match_streams(below_pinch_hot, below_pinch_cold, delta_T_min, "below_pinch")
    )
    
    return matches


def _match_streams(
    hot_list: List[ThermalStream],
    cold_list: List[ThermalStream],
    delta_T_min: float,
    region: str,
) -> List[Dict]:
    """
    Sezgisel (greedy) akış eşleştirme.
    
    Algoritma:
    1. Akışları Q_dot'a göre azalan sırala
    2. Her sıcak akış için en uygun soğuk akışı bul:
       a. Sıcaklık uyumlu mu? (T_hot_supply - T_cold_target ≥ ΔT_min)
       b. Q kapasitesi yeterli mi?
    3. Kalan yük → utility ihtiyacı
    """
    matches = []
    
    hot_remaining = {s.stream_id: s.Q_dot_kW for s in hot_list}
    cold_remaining = {s.stream_id: s.Q_dot_kW for s in cold_list}
    
    hot_sorted = sorted(hot_list, key=lambda s: s.Q_dot_kW, reverse=True)
    cold_sorted = sorted(cold_list, key=lambda s: s.Q_dot_kW, reverse=True)
    
    for hot in hot_sorted:
        if hot_remaining[hot.stream_id] <= 0:
            continue
        
        for cold in cold_sorted:
            if cold_remaining[cold.stream_id] <= 0:
                continue
            
            # Sıcaklık uyumluluğu
            if hot.T_supply_C - cold.T_target_C < delta_T_min:
                continue
            if hot.T_target_C - cold.T_supply_C < -delta_T_min:
                # T_hot_out < T_cold_in ise termodinamik olarak uyumsuz
                pass  # Kısmi eşleştirme yapılabilir
            
            # Eşleştirilebilecek Q
            Q_match = min(hot_remaining[hot.stream_id], cold_remaining[cold.stream_id])
            
            if Q_match >= 5.0:  # Minimum eşleştirme eşiği
                matches.append({
                    "hot_stream_id": hot.stream_id,
                    "cold_stream_id": cold.stream_id,
                    "hot_equipment": hot.equipment_name,
                    "cold_equipment": cold.equipment_name,
                    "hot_description": hot.description,
                    "cold_description": cold.description,
                    "Q_exchange_kW": round(Q_match, 1),
                    "T_hot_in_C": hot.T_supply_C,
                    "T_hot_out_C": hot.T_target_C,
                    "T_cold_in_C": cold.T_supply_C,
                    "T_cold_out_C": cold.T_target_C,
                    "region": region,
                    "description": f"{hot.equipment_name} ({hot.description}) → {cold.equipment_name} ({cold.description})",
                })
                
                hot_remaining[hot.stream_id] -= Q_match
                cold_remaining[cold.stream_id] -= Q_match
    
    return matches
```

#### 4.3.10 `estimate_current_utility_usage()` — Mevcut Durum

```python
def estimate_current_utility_usage(
    equipment_list: List[EquipmentItem],
    analysis_results: Dict[str, dict],
) -> Dict[str, float]:
    """
    Mevcut dış ısıtma/soğutma kullanımını tahmin et.
    
    - Kazanlar → dış ısıtma (QH_current)
    - Chillerler → dış soğutma (QC_current)
    - Diğer → atık ısı (geri kazanılmıyor)
    
    Returns:
        {"QH_current_kW": float, "QC_current_kW": float}
    """
    QH_current = 0.0
    QC_current = 0.0
    
    for item in equipment_list:
        result = analysis_results.get(item.id, {})
        
        if item.equipment_type == "boiler":
            QH_current += result.get("useful_heat_kW", 0) or result.get("exergy_in_kW", 0)
        elif item.equipment_type == "chiller":
            QC_current += result.get("cooling_capacity_kW", 0) or 0
    
    return {"QH_current_kW": QH_current, "QC_current_kW": QC_current}
```

### 4.4 Yardımcı Fonksiyonlar

```python
def compute_pinch_temperature(
    intervals: List[TemperatureInterval],
    pinch_idx: int,
    delta_T_min: float,
) -> Dict[str, float]:
    """Pinch noktası sıcaklıklarını hesapla."""
    if pinch_idx <= 0 or pinch_idx >= len(intervals):
        T_shifted = intervals[0].T_lower_C if intervals else 0
    else:
        T_shifted = intervals[pinch_idx - 1].T_lower_C
    
    return {
        "T_pinch_C": T_shifted,
        "T_pinch_hot_C": T_shifted + delta_T_min / 2.0,
        "T_pinch_cold_C": T_shifted - delta_T_min / 2.0,
    }


def calculate_savings(
    QH_min: float,
    QH_current: float,
    fuel_price_eur_kwh: float,
    operating_hours: int,
) -> Dict[str, float]:
    """Tasarruf potansiyelini hesapla."""
    QH_excess = max(QH_current - QH_min, 0)
    annual_savings_kWh = QH_excess * operating_hours
    annual_savings_EUR = annual_savings_kWh * fuel_price_eur_kwh
    savings_pct = (QH_excess / QH_current * 100) if QH_current > 0 else 0
    
    return {
        "QH_excess_kW": round(QH_excess, 1),
        "annual_savings_kWh": round(annual_savings_kWh, 0),
        "annual_savings_EUR": round(annual_savings_EUR, 0),
        "savings_pct": round(savings_pct, 1),
    }


def check_pinch_feasibility(
    streams: List[ThermalStream],
    total_hot_kW: float,
    total_cold_kW: float,
) -> Tuple[bool, List[str]]:
    """
    Pinch analizinin anlamlı olup olmadığını kontrol et.
    
    Gereksinimler:
    - En az 1 sıcak + 1 soğuk akış
    - Toplam ısı yükü > 50 kW (çok küçükse anlamsız)
    - Sıcaklık örtüşmesi var mı? (yoksa ısı geri kazanım potansiyeli yok)
    """
    warnings = []
    feasible = True
    
    hot_count = sum(1 for s in streams if s.stream_type == StreamType.HOT)
    cold_count = sum(1 for s in streams if s.stream_type == StreamType.COLD)
    
    if hot_count < 1 or cold_count < 1:
        feasible = False
        warnings.append(f"Yetersiz akış: {hot_count} sıcak, {cold_count} soğuk (minimum 1+1)")
    
    if total_hot_kW < 50 and total_cold_kW < 50:
        warnings.append(f"Düşük toplam ısı yükü ({total_hot_kW:.0f} kW) — pinch analizi sınırlı fayda sağlayabilir")
    
    # Sıcaklık örtüşmesi kontrolü
    hot_T_min = min((s.T_target_C for s in streams if s.stream_type == StreamType.HOT), default=0)
    cold_T_max = max((s.T_target_C for s in streams if s.stream_type == StreamType.COLD), default=0)
    
    if hot_T_min >= cold_T_max:
        warnings.append("Sıcak ve soğuk akışlar arasında sıcaklık örtüşmesi yok — ısı geri kazanım potansiyeli düşük")
    
    return feasible, warnings
```

---

## 5. API Entegrasyonu

### 5.1 Factory Analiz Akışına Ekleme

Pinch analizi, fabrika analizi çalıştırıldığında **otomatik olarak** çalışmalı (yeterli akış varsa). Alternatif olarak ayrı bir endpoint de sunulabilir.

**Yaklaşım: İkisi birden.**

#### A) Otomatik: `factory.py` engine'e ekleme

`engine/factory.py` → `analyze_factory()` fonksiyonuna pinch çağrısı ekle:

```python
# engine/factory.py analyze_factory() içinde:

from .pinch import analyze_pinch, check_pinch_feasibility, extract_thermal_streams

def analyze_factory(equipment_list, ...):
    # ... mevcut analiz ...
    
    # Pinch analizi (yeterli akış varsa)
    pinch_result = None
    try:
        streams = extract_thermal_streams(equipment_list, results_dict)
        feasible, warnings = check_pinch_feasibility(streams, ...)
        if feasible:
            pinch_result = analyze_pinch(
                equipment_list, results_dict,
                delta_T_min_C=delta_T_min,
                fuel_price_eur_kwh=fuel_price,
                operating_hours=operating_hours,
            )
    except Exception as e:
        pinch_result = {"is_valid": False, "error_message": str(e)}
    
    return FactoryAnalysisResult(
        ...,
        pinch_analysis=pinch_result,  # Yeni alan
    )
```

#### B) Ayrı endpoint: `api/routes/factory.py`

```python
# api/routes/factory.py

@router.post("/factory/projects/{project_id}/pinch")
async def run_pinch_analysis(
    project_id: str,
    pinch_params: PinchAnalysisRequest = None,
    db: AsyncSession = Depends(get_session),
    user: Optional[dict] = Depends(optional_auth),
):
    """
    Fabrika projesi için pinch analizi çalıştır.
    
    Body (opsiyonel):
        delta_T_min_C: float = 10.0
        fuel_price_eur_kwh: float = 0.08
        operating_hours: int = 8000
        include_pumps: bool = False
    """
    # 1. Projeyi ve ekipmanları getir
    project = await crud.get_factory_project(db, project_id)
    
    # 2. Son analiz sonuçlarını getir
    analysis = await crud.get_latest_factory_analysis(db, project_id)
    
    # 3. Pinch analizi çalıştır
    pinch_result = analyze_pinch(
        project.equipment,
        analysis.results_dict,
        delta_T_min_C=pinch_params.delta_T_min_C if pinch_params else 10.0,
        ...
    )
    
    # 4. Sonucu kaydet (factory_analyses tablosuna veya ayrı tabloya)
    await crud.save_pinch_result(db, project_id, pinch_result.to_dict())
    
    return pinch_result.to_dict()
```

### 5.2 Yeni Schema'lar

`api/schemas/factory.py` dosyasına ekle:

```python
class PinchAnalysisRequest(BaseModel):
    """Pinch analizi istek parametreleri."""
    delta_T_min_C: float = Field(default=10.0, ge=1.0, le=50.0, description="Minimum ΔT (°C)")
    fuel_price_eur_kwh: float = Field(default=0.08, ge=0.01, le=1.0, description="Yakıt fiyatı (EUR/kWh)")
    operating_hours: int = Field(default=8000, ge=1000, le=8760, description="Yıllık çalışma saati")
    include_pumps: bool = Field(default=False, description="Pompaları dahil et")


class PinchAnalysisResponse(BaseModel):
    """Pinch analizi yanıt modeli."""
    is_valid: bool
    error_message: str = ""
    
    # Pinch noktası
    pinch_temperature_C: Optional[float] = None
    pinch_temperature_hot_C: Optional[float] = None
    pinch_temperature_cold_C: Optional[float] = None
    delta_T_min_C: float = 10.0
    
    # Enerji hedefleri
    QH_min_kW: Optional[float] = None
    QC_min_kW: Optional[float] = None
    max_heat_recovery_kW: Optional[float] = None
    
    # Mevcut durum
    QH_current_kW: Optional[float] = None
    QC_current_kW: Optional[float] = None
    savings_potential_kW: Optional[float] = None
    savings_potential_pct: Optional[float] = None
    annual_savings_EUR: Optional[float] = None
    
    # Akışlar
    num_hot_streams: int = 0
    num_cold_streams: int = 0
    streams: List[dict] = []
    
    # Görselleştirme
    composite_curves: Optional[dict] = None
    grand_composite_curve: Optional[dict] = None
    problem_table: List[dict] = []
    
    # HEN
    hen_matches: List[dict] = []
    
    # Uyarılar
    warnings: List[str] = []
```

### 5.3 Veritabanı (Opsiyonel)

Pinch sonuçlarını `factory_analyses` tablosundaki JSON'a eklemek en basit yaklaşım. Ayrı tablo gereksiz karmaşıklık ekler.

```python
# factory_analyses tablosu zaten şu alanlara sahip:
# aggregates, hotspots, integration_opportunities, sankey_data

# Ekleme: pinch_data (JSON)
# VEYA: aggregates JSON'una pinch_analysis anahtarı ekle
```

**Öneri:** Yeni bir `pinch_data` sütunu eklemek yerine, `FactoryAnalysisResult`'a `pinch_analysis` alanı ekle ve `factory_analyses.aggregates` JSON'u içinde sakla. Daha az migration, geriye uyumlu.

---

## 6. Frontend Entegrasyonu

### 6.1 Yeni Componentler

#### `PinchTab.jsx` — Fabrika Dashboard'da yeni sekme

Mevcut FactoryDashboard 3 modlu: Genel Bakış, Sankey, AI. Pinch analizi 4. sekme olarak eklenir.

```
FactoryDashboard Sekmeleri:
  1. Genel Bakış (mevcut)
  2. Akış / Sankey (mevcut)  
  3. Pinch Analizi (YENİ)
  4. AI Yorumlama (mevcut)
```

#### `PinchTab.jsx` İçeriği

```
+----------------------------------------------------------+
| Pinch Analizi                                    [⚙️ ΔTmin] |
+----------------------------------------------------------+
|                                                          |
| +-- Özet Kartlar (MetricBar benzeri) --+                |
| | Pinch T: 85°C | QH_min: 120 kW | QC_min: 45 kW |    |
| | Tasarruf: 35% | 89,600 EUR/yıl | 6 akış         |    |
| +--------------------------------------+                |
|                                                          |
| +-- Composite Curves (Plotly) --------+                 |
| |                                      |                 |
| |  T(°C)                              |                 |
| |  400 ─  ╲                           |                 |
| |  300 ─   ╲  Sıcak                   |                 |
| |  200 ─    ╲╲                         |                 |
| |  150 ─·····╲╲·····Pinch·noktası····· |                 |
| |  100 ─      ╲╲╲  Soğuk              |                 |
| |   50 ─       ╲╲╲                     |                 |
| |    0 ──────────────── H (kW)        |                 |
| |       0   200  400  600  800        |                 |
| +--------------------------------------+                |
|                                                          |
| +-- Grand Composite Curve (Plotly) ---+                 |
| |  T_shifted(°C)                       |                 |
| |  350 ─   ╱                           |                 |
| |  250 ─  ╱                            |                 |
| |  150 ─ ╱  ← QH_min                  |                 |
| |   85 ─╳── Pinch                      |                 |
| |   50 ─ ╲                             |                 |
| |    0 ──────── H (kW)                |                 |
| |       0   50  100  150              |                 |
| +--------------------------------------+                |
|                                                          |
| +-- Akış Tablosu ----------------------+                |
| | # | Ekipman      | Tip  | T_in | T_out | Q(kW) | CP |
| | 1 | Kazan-1      | HOT  | 200  | 150   | 85    | 1.7|
| | 2 | Kompresör-1  | HOT  | 90   | 40    | 45    | 0.9|
| | 3 | HX-1 soğuk   | COLD | 20   | 60    | 120   | 3.0|
| | 4 | Dryer-1 yük  | COLD | 25   | 120   | 200   | 2.1|
| +--------------------------------------+                |
|                                                          |
| +-- HEN Eşleştirme Önerileri ----------+                |
| | 🔥 Kompresör-1 → Kazan-1             |                |
| |    Q: 45 kW | Tasarruf: 28,800 EUR/yıl               |
| |    "Kompresör atık ısısıyla besleme suyu ön ısıtma"   |
| |                                                        |
| | 🔥 Dryer-1 egzoz → HX-1 soğuk taraf  |                |
| |    Q: 35 kW | Tasarruf: 22,400 EUR/yıl               |
| +--------------------------------------+                |
+----------------------------------------------------------+
```

#### `CompositeCurveChart.jsx`

```jsx
// Plotly scatter/line grafiği
// İki eğri: sıcak (kırmızı) + soğuk (mavi)
// Pinch noktası: dikey kesikli çizgi
// QH_min ve QC_min: gölgeli alanlar

import Plot from 'react-plotly.js';

const CompositeCurveChart = ({ compositeData }) => {
  const traces = [
    {
      x: compositeData.hot_curve.H_kW,
      y: compositeData.hot_curve.T_C,
      name: 'Sıcak Composite',
      line: { color: '#ef4444', width: 3 },
      mode: 'lines+markers',
    },
    {
      x: compositeData.cold_curve.H_kW,
      y: compositeData.cold_curve.T_C,
      name: 'Soğuk Composite',
      line: { color: '#3b82f6', width: 3 },
      mode: 'lines+markers',
    },
  ];
  
  const layout = {
    xaxis: { title: 'Enthalpy (kW)' },
    yaxis: { title: 'Sıcaklık (°C)' },
    // Pinch noktası annotation
    annotations: [
      {
        x: compositeData.pinch_point.H_kW,
        y: compositeData.pinch_point.T_hot_C,
        text: `Pinch: ${compositeData.pinch_point.T_hot_C}°C`,
        ...
      }
    ],
    // QH_min ve QC_min shapes (gölgeli alan)
    shapes: [...],
  };
  
  return <Plot data={traces} layout={layout} />;
};
```

#### `GrandCompositeCurveChart.jsx`

```jsx
// Plotly scatter grafiği (dikey: T, yatay: H)
// Tek eğri, pinch noktasında x=0'a dokunur
// QH_min: üst kısımdaki yatay ok
// QC_min: alt kısımdaki yatay ok
```

#### `StreamTable.jsx`

```jsx
// Akış tablosu: sıcak akışlar kırmızı arka plan, soğuk mavi
// Sıralama: Q_dot'a göre azalan
// Her satırda ekipman adı, tip ikonu, sıcaklıklar, Q, CP
```

#### `HENMatches.jsx`

```jsx
// IntegrationPanel benzeri tasarım
// Her eşleştirme bir kart: 
//   sol (sıcak, kırmızı) → ok → sağ (soğuk, mavi)
//   Q değişimi, yıllık tasarruf, açıklama
```

### 6.2 ΔT_min Ayarı

Kullanıcı ΔT_min değerini değiştirebilmeli. Varsayılan sektöre göre:

```jsx
const SECTOR_DEFAULTS = {
  "petrochemical": 15,
  "chemical": 12,
  "food": 8,
  "textile": 12,
  "paper": 15,
  "energy": 8,
  "general": 10,
};
```

Fabrika projesinde sektor bilgisi zaten var → otomatik varsayılan ΔT_min.

### 6.3 API Çağrısı

`frontend/src/services/factoryApi.js` dosyasına ekle:

```javascript
export const runPinchAnalysis = async (projectId, params = {}) => {
  const response = await api.post(`/factory/projects/${projectId}/pinch`, params);
  return response.data;
};
```

---

## 7. Testler

### 7.1 Yeni Test Dosyası: `tests/test_pinch.py`

Tahmini: **~400-500 satır, 30+ test**

```python
"""
ExergyLab Pinch Analizi Testleri

Test kategorileri:
1. Akış çıkarma (stream extraction)
2. Sıcaklık kaydırma (shifted temperatures)
3. Problem tablosu ve kaskad (cascade)
4. Enerji hedefleri (QH_min, QC_min)
5. Composite curves
6. Grand Composite Curve
7. HEN eşleştirme
8. Uç durumlar (edge cases)
9. Fabrika entegrasyonu
"""

import pytest
from engine.pinch import (
    ThermalStream, StreamType, PinchResult,
    analyze_pinch, extract_thermal_streams,
    compute_shifted_temperatures, create_temperature_intervals,
    solve_cascade, generate_composite_curves,
    generate_grand_composite_curve, suggest_hen_matches,
    check_pinch_feasibility,
)
from engine.factory import EquipmentItem, EquipmentType
```

#### Test Kategorileri

```python
# ============================================================
# 1. AKIŞ ÇIKARMA TESTLERİ
# ============================================================

class TestStreamExtraction:
    """Ekipman sonuçlarından termal akış çıkarma."""

    def test_boiler_produces_hot_and_cold_streams(self):
        """Kazan: baca gazı (HOT) + besleme suyu (COLD)."""
        # Boiler item + result mock
        # extract → 1 hot (flue gas) + 1 cold (feedwater)
        pass

    def test_compressor_produces_hot_stream(self):
        """Kompresör: sıkıştırma ısısı (HOT)."""
        pass

    def test_chiller_produces_hot_and_cold_streams(self):
        """Chiller: kondenser (HOT) + evaporatör (COLD)."""
        pass

    def test_pump_excluded_by_default(self):
        """Pompa varsayılan olarak dahil edilmez."""
        pass

    def test_pump_included_when_flag_set(self):
        """include_pumps=True ile pompa dahil edilir."""
        pass

    def test_heat_exchanger_produces_both_streams(self):
        """HX: sıcak taraf (HOT) + soğuk taraf (COLD)."""
        pass

    def test_steam_turbine_produces_hot_stream(self):
        """Buhar türbini: egzoz (HOT)."""
        pass

    def test_dryer_produces_hot_and_cold_streams(self):
        """Dryer: egzoz (HOT) + kurutma yükü (COLD)."""
        pass

    def test_minimum_Q_filter(self):
        """Q < 5 kW olan akışlar filtrelenir."""
        pass

    def test_minimum_deltaT_filter(self):
        """ΔT < 2°C olan akışlar filtrelenir."""
        pass

    def test_missing_result_skipped(self):
        """Analiz sonucu olmayan ekipman atlanır."""
        pass


# ============================================================
# 2. KLASİK PINCH HESAPLAMA TESTLERİ
# ============================================================

class TestClassicPinchCalculation:
    """Bilinen örnek problemlerle pinch hesaplama doğruluğu."""

    @pytest.fixture
    def four_stream_problem(self):
        """
        Klasik 4 akışlı pinch problemi (Linnhoff & Hindmarsh, 1983).
        
        Sıcak akışlar:
        H1: 175°C → 45°C, CP = 2.0 kW/K → Q = 260 kW
        H2: 150°C → 40°C, CP = 4.0 kW/K → Q = 440 kW
        
        Soğuk akışlar:
        C1: 20°C → 155°C, CP = 3.0 kW/K → Q = 405 kW
        C2: 25°C → 112°C, CP = 1.5 kW/K → Q = 130.5 kW
        
        ΔT_min = 10°C
        
        Beklenen:
        QH_min = 7.5 kW (veya hesaplanan değer)
        QC_min = 172.0 kW (veya hesaplanan değer)
        Pinch ≈ 85°C (shifted)
        """
        return [
            ThermalStream("H1", StreamType.HOT, "Eq1", "boiler", "H1",
                          175, 45, 260, 2.0),
            ThermalStream("H2", StreamType.HOT, "Eq2", "hx", "H2",
                          150, 40, 440, 4.0),
            ThermalStream("C1", StreamType.COLD, "Eq3", "hx", "C1",
                          20, 155, 405, 3.0),
            ThermalStream("C2", StreamType.COLD, "Eq4", "dryer", "C2",
                          25, 112, 130.5, 1.5),
        ]

    def test_shifted_temperatures(self, four_stream_problem):
        """Shifted sıcaklıklar doğru hesaplanıyor."""
        hot = [s for s in four_stream_problem if s.stream_type == StreamType.HOT]
        cold = [s for s in four_stream_problem if s.stream_type == StreamType.COLD]
        temps = compute_shifted_temperatures(hot, cold, 10.0)
        # T_shifted sıralı ve benzersiz olmalı
        assert temps == sorted(temps, reverse=True)
        assert len(temps) == len(set(temps))

    def test_energy_balance(self, four_stream_problem):
        """Enerji dengesi: QH_min + ΣQ_hot = QC_min + ΣQ_cold."""
        hot = [s for s in four_stream_problem if s.stream_type == StreamType.HOT]
        cold = [s for s in four_stream_problem if s.stream_type == StreamType.COLD]
        
        total_hot = sum(s.Q_dot_kW for s in hot)  # 700
        total_cold = sum(s.Q_dot_kW for s in cold)  # 535.5
        
        # ... cascade solve ...
        # QH_min + total_hot ≈ QC_min + total_cold (enerji dengesi)
        # assert abs((QH_min + total_hot) - (QC_min + total_cold)) < 0.1

    def test_pinch_temperature(self, four_stream_problem):
        """Pinch sıcaklığı doğru tespit ediliyor."""
        pass

    def test_QH_min_positive(self, four_stream_problem):
        """QH_min ≥ 0."""
        pass

    def test_QC_min_positive(self, four_stream_problem):
        """QC_min ≥ 0."""
        pass

    def test_cascade_non_negative(self, four_stream_problem):
        """Düzeltilmiş kaskadda tüm değerler ≥ 0."""
        pass

    def test_max_heat_recovery(self, four_stream_problem):
        """Max HR = min(ΣQ_hot, ΣQ_cold) - QC_min (veya QH_min)."""
        pass


# ============================================================
# 3. COMPOSITE CURVE TESTLERİ
# ============================================================

class TestCompositeCurves:
    """Composite curve verisi doğruluğu."""

    def test_hot_curve_descending_temperature(self, four_stream_problem):
        """Sıcak composite: sıcaklık azalan."""
        pass

    def test_cold_curve_ascending_temperature(self, four_stream_problem):
        """Soğuk composite: sıcaklık artan."""
        pass

    def test_curves_do_not_cross(self, four_stream_problem):
        """Composite curve'ler kesişmez (ΔT ≥ ΔT_min her noktada)."""
        pass

    def test_curves_touch_at_pinch(self, four_stream_problem):
        """Pinch noktasında eğriler arası mesafe = ΔT_min."""
        pass


# ============================================================
# 4. GCC TESTLERİ
# ============================================================

class TestGrandCompositeCurve:
    """Grand Composite Curve doğruluğu."""

    def test_gcc_touches_zero_at_pinch(self, four_stream_problem):
        """GCC x=0'a pinch noktasında dokunur."""
        pass

    def test_gcc_starts_at_QH_min(self):
        """GCC en üst noktasında QH_min değerinde başlar."""
        pass

    def test_gcc_ends_at_QC_min(self):
        """GCC en alt noktasında QC_min değerinde biter."""
        pass


# ============================================================
# 5. HEN EŞLEŞTİRME TESTLERİ
# ============================================================

class TestHENMatches:
    """HEN eşleştirme önerilerinin doğruluğu."""

    def test_matches_respect_delta_T_min(self):
        """Tüm eşleştirmelerde ΔT ≥ ΔT_min."""
        pass

    def test_no_cross_pinch_matches(self):
        """Pinch üzerinden ısı transferi önerilmez."""
        pass

    def test_total_matched_Q_leq_max_recovery(self):
        """Eşleştirilen toplam Q ≤ max heat recovery."""
        pass


# ============================================================
# 6. UÇ DURUMLAR
# ============================================================

class TestEdgeCases:
    """Uç durumlar ve hata yönetimi."""

    def test_single_hot_single_cold(self):
        """Tek sıcak + tek soğuk akış: basit eşleştirme."""
        pass

    def test_no_hot_streams_returns_invalid(self):
        """Sıcak akış yoksa is_valid=False."""
        pass

    def test_no_cold_streams_returns_invalid(self):
        """Soğuk akış yoksa is_valid=False."""
        pass

    def test_identical_temperatures_no_crash(self):
        """Aynı sıcaklıkta akışlar çökme yapmaz."""
        pass

    def test_very_large_delta_T_min(self):
        """Çok büyük ΔT_min → ısı geri kazanımı yok."""
        pass

    def test_zero_Q_stream_filtered(self):
        """Q=0 akışlar filtrelenir."""
        pass

    def test_phase_change_stream(self):
        """Faz değişimi olan akış doğru işlenir."""
        pass


# ============================================================
# 7. FABRİKA ENTEGRASYON TESTLERİ
# ============================================================

class TestFactoryPinchIntegration:
    """Fabrika analizi ile pinch entegrasyonu."""

    def test_factory_analysis_includes_pinch(self):
        """analyze_factory() sonucunda pinch_analysis alanı var."""
        pass

    def test_insufficient_streams_no_pinch(self):
        """Yetersiz akış: pinch_analysis = None veya is_valid=False."""
        pass

    def test_pinch_savings_consistent_with_factory(self):
        """Pinch tasarruf rakamları fabrika toplamıyla tutarlı."""
        pass
```

### 7.2 Mevcut Testler

`tests/test_engine.py` ve `tests/test_api.py` dosyalarındaki fabrika testlerinin kırılmaması gerekir. Pinch eklenmesi mevcut `FactoryAnalysisResult`'a yeni bir opsiyonel alan ekler — `pinch_analysis: Optional[dict] = None` — geriye uyumlu.

---

## 8. AI Entegrasyonu

### 8.1 Knowledge Router

`api/services/knowledge_router.py` dosyasında pinch analizi zaten destekleniyor olmalı (knowledge/factory/pinch/ mevcut). Sadece pinch sonuçlarının AI yorumlamasına gönderildiğinden emin ol.

### 8.2 Claude Service

`api/services/claude_code_service.py` dosyasında fabrika yorumlama prompt'una pinch sonuçlarını ekle:

```python
# Mevcut fabrika prompt'una ekleme:
if pinch_result and pinch_result.get("is_valid"):
    prompt += f"""
    
    ## Pinch Analizi Sonuçları
    - Pinch sıcaklığı: {pinch_result['pinch_temperature_C']}°C
    - ΔT_min: {pinch_result['delta_T_min_C']}°C
    - QH_min (minimum dış ısıtma): {pinch_result['QH_min_kW']} kW
    - QC_min (minimum dış soğutma): {pinch_result['QC_min_kW']} kW
    - Mevcut QH: {pinch_result['QH_current_kW']} kW → Fazla: {pinch_result['QH_excess_kW']} kW
    - Tasarruf potansiyeli: {pinch_result['savings_potential_pct']}% ({pinch_result['annual_savings_EUR']} EUR/yıl)
    - HEN önerileri: {len(pinch_result['hen_matches'])} eşleştirme
    """
```

---

## 9. Uygulama Planı — Adım Adım

### Faz 1: Engine (Öncelik 1)

| Adım | Dosya | İş |
|------|-------|----|
| 1.1 | `engine/pinch.py` (YENİ) | ThermalStream, PinchResult dataclass'ları |
| 1.2 | `engine/pinch.py` | 7 ekipman için `_extract_*_streams()` fonksiyonları |
| 1.3 | `engine/pinch.py` | `compute_shifted_temperatures()` |
| 1.4 | `engine/pinch.py` | `create_temperature_intervals()` |
| 1.5 | `engine/pinch.py` | `solve_cascade()` |
| 1.6 | `engine/pinch.py` | `generate_composite_curves()` |
| 1.7 | `engine/pinch.py` | `generate_grand_composite_curve()` |
| 1.8 | `engine/pinch.py` | `suggest_hen_matches()` |
| 1.9 | `engine/pinch.py` | `analyze_pinch()` ana fonksiyon |
| 1.10 | `engine/__init__.py` | Pinch modülünü dışa aktar |

### Faz 2: Testler (Öncelik 1)

| Adım | Dosya | İş |
|------|-------|----|
| 2.1 | `tests/test_pinch.py` (YENİ) | Klasik 4 akış problemi fixture |
| 2.2 | `tests/test_pinch.py` | Stream extraction testleri (11 test) |
| 2.3 | `tests/test_pinch.py` | Cascade ve enerji hedefi testleri (7 test) |
| 2.4 | `tests/test_pinch.py` | Composite curve testleri (4 test) |
| 2.5 | `tests/test_pinch.py` | GCC testleri (3 test) |
| 2.6 | `tests/test_pinch.py` | HEN testleri (3 test) |
| 2.7 | `tests/test_pinch.py` | Edge case testleri (7 test) |

### Faz 3: API + Fabrika Entegrasyonu (Öncelik 2)

| Adım | Dosya | İş |
|------|-------|----|
| 3.1 | `engine/factory.py` | `analyze_factory()` → pinch çağrısı ekle |
| 3.2 | `api/schemas/factory.py` | PinchAnalysisRequest/Response ekle |
| 3.3 | `api/routes/factory.py` | `/pinch` endpoint ekle |
| 3.4 | `api/database/models.py` | factory_analyses → pinch_data (opsiyonel) |
| 3.5 | `tests/test_api.py` | Pinch API testi ekle |

### Faz 4: Frontend (Öncelik 2)

| Adım | Dosya | İş |
|------|-------|----|
| 4.1 | `frontend/src/components/pinch/CompositeCurveChart.jsx` (YENİ) | Plotly composite |
| 4.2 | `frontend/src/components/pinch/GrandCompositeCurveChart.jsx` (YENİ) | Plotly GCC |
| 4.3 | `frontend/src/components/pinch/StreamTable.jsx` (YENİ) | Akış tablosu |
| 4.4 | `frontend/src/components/pinch/HENMatches.jsx` (YENİ) | Eşleştirme kartları |
| 4.5 | `frontend/src/components/pinch/PinchMetricBar.jsx` (YENİ) | Pinch metrikleri |
| 4.6 | `frontend/src/components/factory/PinchTab.jsx` (YENİ) | Ana sekme |
| 4.7 | `frontend/src/pages/FactoryDashboard.jsx` | PinchTab sekmesi ekle |
| 4.8 | `frontend/src/services/factoryApi.js` | `runPinchAnalysis()` ekle |

### Faz 5: AI Entegrasyonu (Öncelik 3)

| Adım | Dosya | İş |
|------|-------|----|
| 5.1 | `api/services/claude_code_service.py` | Fabrika prompt'una pinch verisi ekle |
| 5.2 | `api/services/knowledge_router.py` | Pinch knowledge routing doğrula |

---

## 10. Doğrulama Kontrol Listesi

### Engine
- [ ] `engine/pinch.py` dosyası oluşturuldu
- [ ] ThermalStream ve PinchResult dataclass'ları tanımlı
- [ ] 7 ekipman tipi için akış çıkarma fonksiyonları çalışıyor
- [ ] Shifted sıcaklıklar doğru hesaplanıyor
- [ ] Problem tablosu ve kaskad doğru çözülüyor
- [ ] QH_min + ΣQ_hot ≈ QC_min + ΣQ_cold (enerji dengesi)
- [ ] Composite curve verileri Plotly formatında
- [ ] GCC verisi x=0'a pinch'te dokunuyor
- [ ] HEN eşleştirmeleri ΔT_min'e uyuyor
- [ ] Yetersiz akış durumunda is_valid=False dönüyor

### API
- [ ] `/factory/projects/{id}/pinch` endpoint çalışıyor
- [ ] `analyze_factory()` pinch sonuçlarını içeriyor
- [ ] Pinch sonuçları veritabanına kaydediliyor
- [ ] Pydantic şemaları doğru validasyon yapıyor

### Frontend
- [ ] PinchTab FactoryDashboard'da görünüyor
- [ ] Composite curves doğru render ediliyor
- [ ] GCC doğru render ediliyor
- [ ] Akış tablosu sıcak/soğuk renk kodlu
- [ ] HEN eşleştirmeleri okunabilir kartlarda
- [ ] ΔT_min slider/input çalışıyor
- [ ] Pinch verisi yokken (yetersiz akış) uygun mesaj gösteriliyor

### Testler
- [ ] `pytest tests/test_pinch.py -v` — tüm testler geçiyor
- [ ] `pytest tests/ -v` — hiçbir mevcut test kırılmadı
- [ ] Enerji dengesi invariantı tüm test case'lerde sağlanıyor

---

## 11. Claude Code Prompt

```
PROJECT_ANALYSIS.md dosyasını ve BRIEF_24_PINCH_ANALYSIS.md dosyasını oku.

Görev: ExergyLab'a Linnhoff pinch analizi motor modülü ekle.

Bu büyük bir görev, adım adım ilerle:

Faz 1 — Engine modülü:
1. engine/pinch.py dosyasını oluştur.
2. ThermalStream ve StreamType (dataclass + enum) tanımla. Brief Bölüm 4.2'ye bak.
3. 7 ekipman tipi için _extract_*_streams() fonksiyonlarını yaz. Brief Bölüm 3.2 ve 4.3.3'teki kurallara uy. Minimum Q=5 kW ve ΔT=2°C filtreleri uygula.
4. extract_thermal_streams() dispatcher fonksiyonunu yaz. Brief 4.3.2.
5. compute_shifted_temperatures() yaz. Brief 4.3.4.
6. create_temperature_intervals() yaz. Brief 4.3.5.
7. solve_cascade() yaz (Problem Table Algorithm). Brief 4.3.6. Enerji dengesi sağlanmalı: QH_min + ΣQ_hot = QC_min + ΣQ_cold.
8. generate_composite_curves() yaz. Plotly formatında T vs H. Brief 4.3.7.
9. generate_grand_composite_curve() yaz. Brief 4.3.8.
10. suggest_hen_matches() yaz. Greedy eşleştirme, pinch kurallarına uygun. Brief 4.3.9.
11. check_pinch_feasibility() yaz.
12. PinchResult dataclass tanımla (to_dict metodu ile). Brief 4.2.
13. analyze_pinch() ana fonksiyonu yaz — tüm adımları birleştir. Brief 4.3.1.
14. engine/__init__.py dosyasını güncelle.

Faz 2 — Testler:
15. tests/test_pinch.py dosyasını oluştur.
16. Klasik 4 akışlı Linnhoff problemi fixture'ı tanımla (Brief 7.1'deki H1, H2, C1, C2).
17. Stream extraction testleri (minimum 8 test).
18. Cascade ve enerji hedefi testleri (minimum 5 test).
19. Composite curve ve GCC testleri (minimum 4 test).
20. HEN eşleştirme testleri (minimum 3 test).
21. Edge case testleri (minimum 5 test).
22. pytest tests/test_pinch.py -v çalıştır.
23. pytest tests/ -v çalıştır (regresyon kontrolü).

Faz 3 — API + Fabrika entegrasyonu:
24. api/schemas/factory.py → PinchAnalysisRequest ve PinchAnalysisResponse şemaları ekle. Brief 5.2.
25. engine/factory.py → analyze_factory() içinde pinch çağrısı ekle. Brief 5.1-A.
26. api/routes/factory.py → POST /factory/projects/{id}/pinch endpoint ekle. Brief 5.1-B.
27. API testlerini çalıştır.

Faz 4 — Frontend:
28. frontend/src/components/pinch/ dizini oluştur.
29. CompositeCurveChart.jsx — Plotly composite curves (sıcak kırmızı, soğuk mavi). Brief 6.1.
30. GrandCompositeCurveChart.jsx — Plotly GCC. Brief 6.1.
31. StreamTable.jsx — Akış tablosu (renk kodlu). Brief 6.1.
32. HENMatches.jsx — Eşleştirme kartları. Brief 6.1.
33. PinchMetricBar.jsx — Özet metrikler.
34. PinchTab.jsx — Ana sekme (tüm componentleri birleştirir).
35. FactoryDashboard.jsx → PinchTab sekmesi ekle (mevcut sekmelerin yanına).
36. factoryApi.js → runPinchAnalysis() fonksiyonu ekle.

Faz 5 — AI:
37. api/services/claude_code_service.py → Fabrika yorumlama prompt'una pinch verisi ekle. Brief 8.2.

Her fazdan sonra testleri çalıştır ve geçtiğini doğrula.

Önemli kurallar:
- Mevcut factory analiz akışını bozma. pinch_analysis opsiyonel bir alan olmalı.
- Akış çıkarmada eksik veri varsa varsayılan değer kullan, hata fırlatma.
- Enerji dengesi invariantını her durumda sağla.
- Composite curve'lerde sıcak ve soğuk eğriler kesişmemeli.
- HEN eşleştirmelerinde ΔT ≥ ΔT_min her noktada.
```

---

## 12. Bilinen Kısıtlamalar ve Gelecek İyileştirmeler

| Kısıtlama | Açıklama | Gelecek Çözüm |
|-----------|----------|---------------|
| Faz değişimi linearizasyonu | Buharlaşma/yoğuşma sabit CP ile modelleniyor | Parçalı doğrusal (piecewise) yaklaşım |
| Tek ΔT_min | Tüm akışlar için aynı ΔT_min | Akış çifti bazlı ΔT_min (individual contributions) |
| Greedy HEN | Sezgisel eşleştirme — optimal olmayabilir | MILP optimizasyonu (PuLP veya Pyomo ile) |
| Statik akışlar | Yük değişimi / part-load yok | Çok seviyeli pinch (multi-period) |
| CP sabit | Sıcaklığa bağlı CP varyasyonu yok | Parçalı doğrusal CP(T) |
| Maliyet tahmini | HEN yatırım maliyeti basit tahmin | Detaylı HX boyutlandırma (A = Q / U×LMTD) |

---

*BRIEF_24 — ExergyLab Pinch Analizi Motor Modülü*
*Yazar: Claude (ExergyLab geliştirme desteği)*
*Tarih: 2026-02-05*
*Bağımlılık: BRIEF_23 (exergoekonomik — tamamlandı)*
