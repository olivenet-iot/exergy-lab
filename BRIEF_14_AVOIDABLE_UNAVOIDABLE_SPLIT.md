# Brief 14: Avoidable / Unavoidable Exergy Yıkımı Ayrıştırması (7/7 Ekipman)

> **Claude Code için:** Bu brief'i oku ve uygula. Mevcut engine pattern'larını önce incele, uyumsuzluk görürsen mevcut kodu referans al.

---

## 🎯 Hedef

Tüm 7 engine'e **Avoidable (Kaçınılabilir) / Unavoidable (Kaçınılamaz) exergy yıkımı ayrıştırması** ekle. Bu, ExergyLab'ın en değerli özelliği: "Kompresörünüzde 50 kW exergy yıkılıyor" yerine **"35 kW'ı iyileştirilebilir, 15 kW'ı fiziksel limit"** diyebilmek.

**Referans:** Tsatsaronis & Morosuk (2008), "Advanced Exergetic Analysis" metodolojisi.

**Kapsam:**
- Ekipman bazlı AV/UN split (bu brief)
- Endogenous/Exogenous split = fabrika seviyesi, bu brief'te YOK (gelecek brief)

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. **ÖNCE mevcut engine kodunu oku** — her engine'in Input/Result dataclass'ını ve analyze fonksiyonunu incele
3. Mevcut pattern ile uyumsuzluk varsa **mevcut kodu referans al** (brief'i değil)
4. Her engine'in alt tipleri için uygun referans parametreleri kullan
5. Edge case'leri handle et (actual < unavoidable → avoidable = 0)
6. **Mevcut çalışan 307 testi ASLA bozma** — her değişiklikten sonra `pytest tests/ -v` çalıştır
7. Yeni testler ekle (her engine için AV/UN testleri)
8. Knowledge base'deki `knowledge/factory/advanced_exergy/` dosyalarını referans olarak oku

---

## 📋 Adım 0: ÖNCE Mevcut Kodu Anla (KRİTİK)

```bash
# 1. Core.py — ExergyResult base class
cat engine/core.py

# 2. Tüm engine'lerin Input dataclass'ları ve analyze fonksiyonları
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/compressor.py
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/boiler.py
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/chiller.py
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/pump.py
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/heat_exchanger.py
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/steam_turbine.py
grep -n "class.*Input\|class.*Result\|def analyze_\|def to_api_dict" engine/dryer.py

# 3. ExergyResult'ın to_api_dict() metodu
grep -A 20 "class ExergyResult" engine/core.py

# 4. Her engine'in Sankey fonksiyonu — destruction node'u nasıl oluşturulur?
grep -n "Exergy Yıkımı\|exergy_destroyed\|destruction\|yıkım" engine/*.py

# 5. Knowledge base — advanced exergy referans dosyaları
ls knowledge/factory/advanced_exergy/
cat knowledge/factory/advanced_exergy/overview.md | head -50
cat knowledge/factory/advanced_exergy/avoidable_unavoidable.md | head -80 2>/dev/null || echo "Not found"

# 6. Compressor subtypes — önemli çünkü 4 ayrı analyze fonksiyonu var
grep -n "def analyze_" engine/compressor.py

# 7. Mevcut test pattern'ı
head -30 tests/test_engine.py
head -30 tests/test_heat_exchanger.py
```

**Bu çıktıları incele. Devam etmeden önce her engine'in Input field adlarını ve analyze fonksiyon imzalarını anla.**

---

## 🧪 Termodinamik Metodoloji

### Temel Kavram

```
Toplam Exergy Yıkımı = Kaçınılabilir (AV) + Kaçınılamaz (UN)

  Ėx_D = Ėx_D,AV + Ėx_D,UN

Kaçınılamaz (UN):
  "En iyi mevcut teknoloji" ile bile ortadan kaldırılamayan yıkım.
  → Fiziksel limitler, termodinamik alt sınırlar.

Kaçınılabilir (AV):
  Mevcut teknoloji ile iyileştirilebilir kısım.
  → Yatırım ve operasyonel iyileştirmelerle düşürülebilir.
  → AV = Ėx_D,actual - Ėx_D,UN
```

### Hesaplama Yöntemi

Her engine için:
1. **Aynı proses koşullarını** koru (aynı basınçlar, sıcaklıklar, debiler, ısı yükleri)
2. **Ekipman parametrelerini** "en iyi ulaşılabilir" değerlere çek (η_is,best, η_mech,best, vb.)
3. **Aynı analyze fonksiyonunu** bu "en iyi" input ile çalıştır → `result_unavoidable`
4. **Unavoidable** = `result_unavoidable.exergy_destroyed_kW`
5. **Avoidable** = `max(0, actual.exergy_destroyed_kW - unavoidable)`

Bu yaklaşım zarif çünkü:
- Mevcut hesaplama mantığını yeniden kullanır (DRY)
- Yeni formül yazmak gerekmez
- Fiziksel tutarlılık garanti edilir

### Edge Case'ler

- `actual < unavoidable` → `avoidable = 0` (kullanıcı zaten en iyiden iyi değerler girmiş)
- `unavoidable < 0` → `unavoidable = 0` (numerik hata guard)
- `actual = 0` → `avoidable = 0, unavoidable = 0`

---

## 📦 Adım 1: `engine/core.py` — ExergyResult Base Class Güncelleme

Mevcut `ExergyResult` dataclass'ına 3 yeni field ekle:

```python
# ExergyResult dataclass'ına EKLE (mevcut field'ların altına):

# Avoidable/Unavoidable split
exergy_destroyed_avoidable_kW: float = 0.0
exergy_destroyed_unavoidable_kW: float = 0.0
avoidable_ratio_pct: float = 0.0     # AV / (AV + UN) × 100
```

Ve `to_api_dict()` metoduna ekle:

```python
# to_api_dict() içine EKLE:
'exergy_destroyed_avoidable_kW': round(self.exergy_destroyed_avoidable_kW, 2),
'exergy_destroyed_unavoidable_kW': round(self.exergy_destroyed_unavoidable_kW, 2),
'avoidable_ratio_pct': round(self.avoidable_ratio_pct, 1),
```

**Bu değişiklik TÜM engine'lerin API çıktısına AV/UN field'larını otomatik ekler.**

---

## 📦 Adım 2: Referans Parametreleri — "En İyi Mevcut Teknoloji"

Her engine tipi ve alt tipi için "unavoidable" referans parametrelerini tanımla. Bu değerler, akademik literatür ve endüstri best-practice'e dayanır.

### 2.1 Compressor Referans Parametreleri

Compressor'da 4 alt tip, her birinin ayrı `Input` class'ı ve `analyze` fonksiyonu var.

```python
# engine/compressor.py'ye EKLE (dosya başına, sabit olarak)

UNAVOIDABLE_REF_COMPRESSOR = {
    # Subtype: {field: best_achievable_value}
    # Sadece verim/kayıp parametreleri — proses koşulları (basınç, debi) DEĞİŞMEZ
    'screw': {
        'isentropic_efficiency': 0.90,
        'mechanical_efficiency': 0.98,
    },
    'piston': {
        'isentropic_efficiency': 0.88,
        'mechanical_efficiency': 0.97,
    },
    'scroll': {
        'isentropic_efficiency': 0.85,
        'mechanical_efficiency': 0.97,
    },
    'centrifugal': {
        'isentropic_efficiency': 0.92,
        'mechanical_efficiency': 0.99,
    },
}
```

**DİKKAT:** Compressor Input dataclass'larında field adları farklı olabilir. Mevcut kodu oku:
- `CompressorInput` → muhtemelen `isentropic_efficiency` veya benzeri
- `PistonCompressorInput` → kademe sayısı, soğutma tipi var ama verim parametresi de var
- `ScrollCompressorInput` → yağsız seçeneği
- `CentrifugalCompressorInput` → surge/choke, guide vane

Her Input class'ın verim parametresinin **gerçek field adını** kod okuyarak bul ve referans dict'ini ona göre oluştur.

### 2.2 Boiler Referans Parametreleri

```python
UNAVOIDABLE_REF_BOILER = {
    # Alt tip bazlı en iyi ulaşılabilir parametreler
    # Yanma irreversibilitesi kaçınılamazdır — sadece kayıp parametreleri iyileştirilir
    'steam_firetube': {
        'excess_air_pct': 5.0,          # En iyi: %5 fazla hava (doğalgaz)
        'flue_gas_temp_C': 120.0,       # Ekonomizer ile en düşük baca sıcaklığı
        'radiation_loss_pct': 0.5,      # En iyi yalıtım
        'blowdown_rate_pct': 1.0,       # TDS kontrolü ile minimum
    },
    'steam_watertube': {
        'excess_air_pct': 5.0,
        'flue_gas_temp_C': 120.0,
        'radiation_loss_pct': 0.3,
        'blowdown_rate_pct': 1.0,
    },
    'hotwater': {
        'excess_air_pct': 5.0,
        'flue_gas_temp_C': 100.0,
        'radiation_loss_pct': 0.5,
    },
    'condensing': {
        'excess_air_pct': 3.0,
        'flue_gas_temp_C': 55.0,        # Yoğuşma noktası altı
        'radiation_loss_pct': 0.3,
    },
    'waste_heat': {
        'flue_gas_temp_C': 100.0,       # WHR için minimum stack temp
        'radiation_loss_pct': 0.3,
    },
    'electric': {
        # Elektrik kazanında kayıp minimal — zaten ~%99 verimli
        # Unavoidable ≈ actual (çok az avoidable)
    },
    'biomass': {
        'excess_air_pct': 15.0,         # Biomass için daha yüksek
        'flue_gas_temp_C': 150.0,       # Korozyon limiti
        'radiation_loss_pct': 0.5,
    },
}
```

**ÖNEMLI:** Boiler'daki yanma irreversibilitesi (yakıtın yüksek sıcaklıkta yanıp düşük sıcaklıkta buhara aktarılması) BÜYÜK oranda kaçınılamazdır. Bu yüzden boiler'da avoidable oranı tipik olarak düşüktür (%10-25). Bu termodinamik olarak doğrudur.

**DİKKAT:** Boiler Input class'ındaki gerçek field adlarını kontrol et. Yukarıdaki isimler tahmini — `cat engine/boiler.py` ile doğrula.

### 2.3 Chiller Referans Parametreleri

```python
UNAVOIDABLE_REF_CHILLER = {
    # Vapor compression subtypes
    'screw': {
        'compressor_isentropic_efficiency': 0.88,
        'condenser_approach_C': 3.0,     # ΔT_cond,min
        'evaporator_approach_C': 3.0,    # ΔT_evap,min
    },
    'centrifugal': {
        'compressor_isentropic_efficiency': 0.90,
        'condenser_approach_C': 2.0,
        'evaporator_approach_C': 2.0,
    },
    'scroll': {
        'compressor_isentropic_efficiency': 0.82,
        'condenser_approach_C': 4.0,
        'evaporator_approach_C': 4.0,
    },
    'reciprocating': {
        'compressor_isentropic_efficiency': 0.85,
        'condenser_approach_C': 3.0,
        'evaporator_approach_C': 3.0,
    },
    # Absorption
    'absorption_single': {
        'cop_thermal': 0.80,            # Tek kademeli best COP
    },
    'absorption_double': {
        'cop_thermal': 1.40,            # Çift kademeli best COP
    },
}
```

**DİKKAT:** Chiller engine'inin mevcut Input yapısını oku. Approach temperature veya COP field'ları farklı isimde olabilir. Ayrıca absorption vs vapor compression için ayrı code path'ler olabilir.

### 2.4 Pump Referans Parametreleri

```python
UNAVOIDABLE_REF_PUMP = {
    # Pompa tipi bazlı en iyi verimler
    'centrifugal_large': {              # >30 kW
        'pump_efficiency': 0.90,
        'motor_efficiency': 0.96,       # IE4
    },
    'centrifugal_small': {              # <30 kW
        'pump_efficiency': 0.85,
        'motor_efficiency': 0.93,       # IE4 (küçük motor)
    },
    'positive_displacement': {
        'pump_efficiency': 0.85,
        'motor_efficiency': 0.95,
    },
    'submersible': {
        'pump_efficiency': 0.80,
        'motor_efficiency': 0.90,
    },
}
```

**DİKKAT:** Pump engine'de alt tip ayrımının nasıl yapıldığını oku. `pump_type` field'ı mı var, yoksa genel bir `pump_efficiency` field'ı mı? Referans dict'ini buna göre ayarla.

Pump'ta ayrıca kontrol yöntemi (throttle vs VSD) etkisi var. Unavoidable hesabında VSD referans alınmalı (en verimli kontrol).

### 2.5 Heat Exchanger Referans Parametreleri

```python
UNAVOIDABLE_REF_HEAT_EXCHANGER = {
    # HX'te exergy yıkımının iki kaynağı:
    #   1. Sıcaklık farkı (ΔT) — proses koşullarına bağlı, büyük oranda kaçınılamaz
    #   2. Basınç düşüşü (ΔP) — tasarıma bağlı, büyük oranda kaçınılabilir
    # Unavoidable: minimum ΔP ile hesapla
    'shell_tube': {
        'hot_pressure_drop_kPa': 8.0,   # Best design S&T
        'cold_pressure_drop_kPa': 8.0,
    },
    'plate': {
        'hot_pressure_drop_kPa': 5.0,   # Best design plate
        'cold_pressure_drop_kPa': 5.0,
    },
    'finned_tube': {
        'hot_pressure_drop_kPa': 3.0,   # Air-side low ΔP
        'cold_pressure_drop_kPa': 10.0,
    },
    'economizer': {
        'hot_pressure_drop_kPa': 2.0,   # Baca gazı tarafı düşük ΔP
        'cold_pressure_drop_kPa': 10.0,
    },
    'air_cooled': {
        'hot_pressure_drop_kPa': 5.0,
        'cold_pressure_drop_kPa': 0.5,  # Fan tarafı
    },
    'double_pipe': {
        'hot_pressure_drop_kPa': 5.0,
        'cold_pressure_drop_kPa': 5.0,
    },
    'spiral': {
        'hot_pressure_drop_kPa': 8.0,
        'cold_pressure_drop_kPa': 8.0,
    },
}
```

**NOT:** HX'te sıcaklık farkı kaynaklı exergy yıkımı büyük oranda kaçınılamazdır (belirli bir ısı yükünü transfer etmek için sıcaklık farkı gerekir). Basınç düşüşü kaynaklı yıkım daha çok kaçınılabilirdir. Bejan sayısı zaten bu ayrımı yapıyor — unavoidable hesabında bu bilgiyi kullan.

### 2.6 Steam Turbine Referans Parametreleri

```python
UNAVOIDABLE_REF_STEAM_TURBINE = {
    'backpressure': {
        'isentropic_efficiency': 0.90,
        'mechanical_efficiency': 0.99,
        'generator_efficiency': 0.98,
    },
    'condensing': {
        'isentropic_efficiency': 0.92,  # Büyük yoğuşmalı türbinler
        'mechanical_efficiency': 0.99,
        'generator_efficiency': 0.98,
    },
    'extraction': {
        'isentropic_efficiency': 0.88,  # Ara çekiş daha kompleks
        'mechanical_efficiency': 0.99,
        'generator_efficiency': 0.98,
    },
    'condensing_extraction': {
        'isentropic_efficiency': 0.87,
        'mechanical_efficiency': 0.99,
        'generator_efficiency': 0.98,
    },
    'chp_backpressure': {
        'isentropic_efficiency': 0.90,
        'mechanical_efficiency': 0.99,
        'generator_efficiency': 0.98,
        'heat_recovery_fraction': 0.85, # Best HRS
    },
}
```

### 2.7 Dryer Referans Parametreleri

```python
UNAVOIDABLE_REF_DRYER = {
    # Her kurutucu tipinin en iyi termal verimi
    # + en iyi egzoz sıcaklığı (çiğ noktası + 10°C ≈ 55-65°C)
    'conveyor': {
        'fuel_efficiency': 0.95,         # Best combustion
        'air_outlet_temp_C': 60.0,       # Egzoz ısı geri kazanımlı
    },
    'rotary': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 55.0,
    },
    'spray': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 70.0,       # Spray dryer limiti daha yüksek
    },
    'fluidized_bed': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 55.0,
    },
    'tray': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 60.0,
    },
    'drum': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 55.0,
    },
    'infrared': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 50.0,
    },
    'microwave': {
        'fuel_efficiency': 0.95,
        'air_outlet_temp_C': 50.0,
    },
}
```

---

## 📦 Adım 3: Engine Güncelleme Pattern'ı — Tam Örnek

Aşağıda **bir engine** için tam implementasyonu gösteriyorum. Diğer 6 engine aynı pattern'ı takip edecek.

### Pattern: `_calc_avoidable_split()` fonksiyonu

Her engine dosyasına bir helper fonksiyon ekle:

```python
import copy

def _calc_avoidable_split(input_data, actual_result, analyze_func, ref_params: dict):
    """
    Avoidable/Unavoidable exergy yıkımı ayrıştırması.

    Tsatsaronis & Morosuk (2008) metodolojisi:
    - Aynı proses koşulları + en iyi mevcut teknoloji parametreleri → unavoidable
    - Avoidable = actual - unavoidable

    Args:
        input_data: Orijinal Input dataclass
        actual_result: Gerçek analiz sonucu
        analyze_func: Engine'in analyze fonksiyonu (callable)
        ref_params: Unavoidable referans parametreleri {field: value}

    Returns:
        (avoidable_kW, unavoidable_kW, avoidable_ratio_pct)
    """
    if actual_result.exergy_destroyed_kW <= 0:
        return 0.0, 0.0, 0.0

    # Unavoidable input: aynı proses koşulları + en iyi teknoloji
    un_input = copy.deepcopy(input_data)
    for field, value in ref_params.items():
        if hasattr(un_input, field):
            setattr(un_input, field, value)

    # Unavoidable analiz
    try:
        un_result = analyze_func(un_input)
        unavoidable = max(un_result.exergy_destroyed_kW, 0.0)
    except Exception:
        # Hata durumunda conservative tahmin: %50 unavoidable
        unavoidable = actual_result.exergy_destroyed_kW * 0.50

    # Avoidable = actual - unavoidable (minimum 0)
    avoidable = max(actual_result.exergy_destroyed_kW - unavoidable, 0.0)

    # Eğer unavoidable > actual (kullanıcı zaten çok iyi), normalize et
    if unavoidable > actual_result.exergy_destroyed_kW:
        unavoidable = actual_result.exergy_destroyed_kW
        avoidable = 0.0

    total = avoidable + unavoidable
    ratio = (avoidable / total * 100) if total > 0 else 0.0

    return avoidable, unavoidable, ratio
```

### Örnek: compressor.py güncelleme

```python
# 1. UNAVOIDABLE_REF_COMPRESSOR dict'ini dosya başına ekle (Adım 2.1)

# 2. Her analyze fonksiyonunun SONUNA AV/UN hesabı ekle:

def analyze_compressor(input_data: CompressorInput, dead_state: DeadState = None) -> CompressorResult:
    """Mevcut analyze fonksiyonu — DEĞİŞTİRME, sadece SONUNA EKLE"""

    # ... mevcut hesaplamalar aynen kalır ...
    # ... result oluşturulur ...

    # === YENİ: Avoidable/Unavoidable Split ===
    subtype = getattr(input_data, 'compressor_type', 'screw')  # field adını kontrol et!
    ref = UNAVOIDABLE_REF_COMPRESSOR.get(subtype, UNAVOIDABLE_REF_COMPRESSOR['screw'])

    av, un, ratio = _calc_avoidable_split(
        input_data, result, analyze_compressor, ref
    )
    result.exergy_destroyed_avoidable_kW = av
    result.exergy_destroyed_unavoidable_kW = un
    result.avoidable_ratio_pct = ratio

    return result
```

**DİKKAT — Recursion Guard:**

`_calc_avoidable_split` tekrar `analyze_compressor()` çağırıyor → bu da tekrar `_calc_avoidable_split` çağırır → SONSUZ DÖNGÜ!

Bunu engelleme yöntemleri:

**Yöntem A (Önerilen): Flag parametresi**
```python
def analyze_compressor(input_data, dead_state=None, _calc_avoidable=True):
    # ... mevcut hesaplamalar ...

    # AV/UN split — sadece ilk çağrıda
    if _calc_avoidable:
        ref = UNAVOIDABLE_REF_COMPRESSOR.get(subtype, ...)
        # Recursive çağrıda _calc_avoidable=False
        un_input = copy.deepcopy(input_data)
        for field, value in ref.items():
            if hasattr(un_input, field):
                setattr(un_input, field, value)
        try:
            un_result = analyze_compressor(un_input, dead_state, _calc_avoidable=False)
            unavoidable = max(un_result.exergy_destroyed_kW, 0.0)
        except Exception:
            unavoidable = result.exergy_destroyed_kW * 0.50

        avoidable = max(result.exergy_destroyed_kW - unavoidable, 0.0)
        if unavoidable > result.exergy_destroyed_kW:
            unavoidable = result.exergy_destroyed_kW
            avoidable = 0.0
        total = avoidable + unavoidable
        result.exergy_destroyed_avoidable_kW = avoidable
        result.exergy_destroyed_unavoidable_kW = unavoidable
        result.avoidable_ratio_pct = (avoidable / total * 100) if total > 0 else 0.0

    return result
```

**Yöntem B: Ayrı helper fonksiyon (analyze fonksiyonuna dokunmadan)**
```python
def _analyze_compressor_core(input_data, dead_state=None):
    """Core hesaplama — AV/UN olmadan"""
    # ... mevcut hesaplamaların tamamı buraya taşınır ...
    return result

def analyze_compressor(input_data, dead_state=None):
    """Public API — AV/UN split dahil"""
    result = _analyze_compressor_core(input_data, dead_state)

    ref = UNAVOIDABLE_REF_COMPRESSOR.get(...)
    un_input = copy.deepcopy(input_data)
    for field, value in ref.items():
        if hasattr(un_input, field):
            setattr(un_input, field, value)

    un_result = _analyze_compressor_core(un_input, dead_state)
    # ... AV/UN hesapla ve result'a ata ...
    return result
```

**Yöntem A daha basit** (mevcut fonksiyona flag ekle). **Yöntem B daha temiz** (SRP). Hangisi mevcut koda daha uygunsa onu kullan.

**Her iki yöntemde de `import copy` eklemeyi UNUTMA!**

---

## 📦 Adım 4: 7 Engine Güncelleme Listesi

Her engine için aynı pattern'ı uygula. Aşağıdaki tabloda her engine'in özel dikkat noktaları:

### 4.1 `engine/compressor.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | screw (default), piston, scroll, centrifugal |
| Analyze fonksiyonları | `analyze_compressor()`, `analyze_piston_compressor()`, `analyze_scroll_compressor()`, `analyze_centrifugal_compressor()` |
| Referans parametreleri | `isentropic_efficiency`, `mechanical_efficiency` |
| Dikkat | **4 ayrı analyze fonksiyonu var** — hepsine AV/UN ekle |
| Beklenen AV oranı | %30-60 (verime bağlı) |

### 4.2 `engine/boiler.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | steam_firetube, steam_watertube, hotwater, condensing, waste_heat, electric, biomass |
| Analyze fonksiyonları | `analyze_boiler()` (muhtemelen tek fonksiyon) |
| Referans parametreleri | `excess_air_pct`, `flue_gas_temp_C`, `radiation_loss_pct`, `blowdown_rate_pct` |
| Dikkat | Yanma irreversibilitesi BÜYÜK ve kaçınılamaz |
| Beklenen AV oranı | %10-25 (düşük — yanma dominanttır) |

### 4.3 `engine/chiller.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | screw, centrifugal, scroll, reciprocating, absorption |
| Analyze fonksiyonları | Muhtemelen tek `analyze_chiller()` ama vapor compression vs absorption ayrımı var |
| Referans parametreleri | Compressor efficiency, approach temperatures, COP |
| Dikkat | Absorption ve vapor compression ayrı code path olabilir |
| Beklenen AV oranı | %20-40 |

### 4.4 `engine/pump.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | centrifugal, positive_displacement, submersible |
| Analyze fonksiyonları | `analyze_pump()` |
| Referans parametreleri | `pump_efficiency`, `motor_efficiency` |
| Dikkat | Kontrol yöntemi (throttle vs VSD) büyük fark yaratır. VSD referans al. |
| Beklenen AV oranı | %40-70 (özellikle throttle kontrolde) |

### 4.5 `engine/heat_exchanger.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | shell_tube, plate, finned_tube, economizer, air_cooled, double_pipe, spiral |
| Analyze fonksiyonları | `analyze_heat_exchanger()` |
| Referans parametreleri | `hot_pressure_drop_kPa`, `cold_pressure_drop_kPa` |
| Dikkat | ΔT kaynaklı yıkım büyük oranda unavoidable. ΔP kaynaklı avoidable. Bejan sayısı bu ayrımı zaten yapıyor. |
| Beklenen AV oranı | %5-30 (Be'ye bağlı: düşük Be = daha çok ΔP kaynağı = daha çok AV) |

**Alternatif yaklaşım (daha hassas):** Bejan sayısı kullanarak ayrıştırma:
```python
# Bejan'dan yararlanarak:
# S_gen_ΔT → büyük oranda unavoidable (%85'i UN, %15'i AV daha iyi tasarımla)
# S_gen_ΔP → büyük oranda avoidable (%30'u UN, %70'i AV daha iyi tasarımla)
un_from_dT = result.entropy_gen_heat_transfer_kW_K * T0 * 0.85
un_from_dP = result.entropy_gen_pressure_drop_kW_K * T0 * 0.30
unavoidable = un_from_dT + un_from_dP
```
Bu yaklaşım, basınç düşüşü referans parametresi yerine direkt Bejan dekompozisyonundan unavoidable hesaplar. **İki yaklaşımı değerlendir, hangisi daha tutarlı sonuç veriyorsa onu kullan.**

### 4.6 `engine/steam_turbine.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | backpressure, condensing, extraction, condensing_extraction, chp_backpressure |
| Analyze fonksiyonları | `analyze_steam_turbine()` |
| Referans parametreleri | `isentropic_efficiency`, `mechanical_efficiency`, `generator_efficiency` |
| Dikkat | CHP modda `heat_recovery_fraction` de referans parametresi |
| Beklenen AV oranı | %30-60 |

### 4.7 `engine/dryer.py`

| Özellik | Detay |
|---------|-------|
| Alt tipler | conveyor, rotary, spray, fluidized_bed, tray, drum, infrared, microwave |
| Analyze fonksiyonları | `analyze_dryer()` |
| Referans parametreleri | `fuel_efficiency`, `air_outlet_temp_C` |
| Dikkat | Buharlaşma exergy'si büyük oranda unavoidable (suyu buharlaştırmak zorunlu). Egzoz kaybı avoidable (ısı geri kazanım ile). |
| Beklenen AV oranı | %30-50 |

---

## 📦 Adım 5: Sankey Diyagramı Güncelleme

Mevcut Sankey'de "Exergy Yıkımı" tek bir node. Bunu ikiye böl:

### 5.1 Renk Kodları

```
Kaçınılabilir Yıkım (AV): #e74c3c (kırmızı) — "Buna odaklanın!"
Kaçınılamaz Yıkım (UN):   #95a5a6 (gri)    — "Fiziksel limit"
```

### 5.2 Her engine'in `generate_xxx_sankey_data()` fonksiyonu

Mevcut kod (tahmini):
```python
# MEVCUT:
nodes.append({'id': n, 'name': 'Exergy Yıkımı', 'name_en': 'Exergy Destruction', 'color': '#e74c3c'})
links.append({'source': src, 'target': n, 'value': result.exergy_destroyed_kW})
```

Yeni kod:
```python
# YENİ: İki node — AV ve UN
if result.exergy_destroyed_avoidable_kW > 0:
    nodes.append({
        'id': n, 'name': 'Kaçınılabilir Yıkım',
        'name_en': 'Avoidable Destruction', 'color': '#e74c3c'
    })
    links.append({'source': src, 'target': n, 'value': result.exergy_destroyed_avoidable_kW})
    n += 1

if result.exergy_destroyed_unavoidable_kW > 0:
    nodes.append({
        'id': n, 'name': 'Kaçınılamaz Yıkım',
        'name_en': 'Unavoidable Destruction', 'color': '#95a5a6'
    })
    links.append({'source': src, 'target': n, 'value': result.exergy_destroyed_unavoidable_kW})
    n += 1
```

**FALLBACK:** Eğer AV/UN hesaplanmamışsa (eski test verisi, edge case), eski "Exergy Yıkımı" tek node'unu göster:
```python
if result.exergy_destroyed_avoidable_kW > 0 or result.exergy_destroyed_unavoidable_kW > 0:
    # İkiye böl (yukarıdaki kod)
else:
    # Eski tek node (mevcut kod aynen kalsın)
```

**DİKKAT:** Node id numaralandırmasını dikkatli yönet. Bir node yerine iki node geldiğinde sonraki id'ler kayar. Her engine'in Sankey fonksiyonundaki id mantığını incele.

### 5.3 `engine/sankey.py` Dispatcher

Dispatcher'a dokunmaya gerek yok — her engine kendi Sankey fonksiyonunda değişiklik yapıyor.

### 5.4 Factory Sankey

`engine/factory.py`'deki `_generate_factory_sankey()` fonksiyonunda fabrika toplam Sankey'i var. Burada da toplam AV/UN gösterilebilir:

```python
total_av = sum(eq.get('exergy_destroyed_avoidable_kW', 0) for eq in equipment_results)
total_un = sum(eq.get('exergy_destroyed_unavoidable_kW', 0) for eq in equipment_results)
```

Factory Sankey'de de destruction node'u AV/UN olarak ikiye böl.

---

## 📦 Adım 6: Frontend — ResultsPanel Güncelleme

### 6.1 API Response Mapping (`frontend/src/services/api.js`)

`analyzeEquipment()` fonksiyonunda yeni field'ları map'le:

```javascript
// api.js — analyzeEquipment return mapping'ine EKLE:
exergy_destroyed_avoidable_kW: data.metrics.exergy_destroyed_avoidable_kW,
exergy_destroyed_unavoidable_kW: data.metrics.exergy_destroyed_unavoidable_kW,
avoidable_ratio_pct: data.metrics.avoidable_ratio_pct,
```

### 6.2 ResultsPanel Güncelleme

Mevcut 4 ana metrik kartının altına **"Yıkım Ayrıştırması"** bölümü ekle.

**Görsel:** Stacked bar — kırmızı (AV) + gri (UN)

```jsx
{/* AV/UN Split Section */}
{metrics.exergy_destroyed_avoidable_kW != null && (
  <div className="mt-6 p-4 bg-white rounded-lg border border-gray-200">
    <h3 className="text-sm font-semibold text-gray-700 mb-3">
      Yıkım Ayrıştırması (Tsatsaronis Metodu)
    </h3>

    {/* Stacked Bar */}
    <div className="flex h-8 rounded-lg overflow-hidden mb-3">
      {metrics.avoidable_ratio_pct > 0 && (
        <div
          className="bg-red-500 flex items-center justify-center text-white text-xs font-medium"
          style={{ width: `${metrics.avoidable_ratio_pct}%` }}
        >
          {metrics.avoidable_ratio_pct > 15 && `${metrics.avoidable_ratio_pct.toFixed(0)}%`}
        </div>
      )}
      {(100 - metrics.avoidable_ratio_pct) > 0 && (
        <div
          className="bg-gray-400 flex items-center justify-center text-white text-xs font-medium"
          style={{ width: `${100 - metrics.avoidable_ratio_pct}%` }}
        >
          {(100 - metrics.avoidable_ratio_pct) > 15 && `${(100 - metrics.avoidable_ratio_pct).toFixed(0)}%`}
        </div>
      )}
    </div>

    {/* Metin */}
    <div className="grid grid-cols-2 gap-4 text-sm">
      <div>
        <span className="inline-block w-3 h-3 bg-red-500 rounded mr-2"></span>
        <span className="font-medium text-red-700">Kaçınılabilir:</span>
        <span className="ml-1">{metrics.exergy_destroyed_avoidable_kW.toFixed(1)} kW</span>
      </div>
      <div>
        <span className="inline-block w-3 h-3 bg-gray-400 rounded mr-2"></span>
        <span className="font-medium text-gray-600">Kaçınılamaz:</span>
        <span className="ml-1">{metrics.exergy_destroyed_unavoidable_kW.toFixed(1)} kW</span>
      </div>
    </div>

    {/* Açıklama */}
    <p className="mt-2 text-xs text-gray-500">
      Kaçınılabilir yıkım, mevcut teknoloji ile iyileştirilebilir kısımdır.
      Yatırım ve operasyonel değişikliklerle düşürülebilir.
    </p>
  </div>
)}
```

**NOT:** Bu JSX kodu referans — mevcut ResultsPanel'in styling pattern'ına uyarla.

---

## 📦 Adım 7: AI Prompt Template Güncelleme

`api/services/claude_code_service.py`'de AI yorumlama prompt'una AV/UN verisi ekle.

### 7.1 `_build_prompt()` fonksiyonuna ek veri

```python
# Analiz verisi formatlarken AV/UN bilgisini ekle:
if analysis_data.get('exergy_destroyed_avoidable_kW'):
    prompt_parts.append(f"""
Yıkım Ayrıştırması:
- Kaçınılabilir (AV): {analysis_data['exergy_destroyed_avoidable_kW']:.1f} kW
- Kaçınılamaz (UN): {analysis_data['exergy_destroyed_unavoidable_kW']:.1f} kW
- Kaçınılabilir Oran: %{analysis_data['avoidable_ratio_pct']:.1f}
""")
```

### 7.2 Skill güncelleme (Opsiyonel ama önerilen)

`skills/core/decision_trees.md` veya `skills/core/exergy_fundamentals.md` dosyasına AV/UN karar ağacı ekle:

```
Avoidable Ratio > %50: "Önemli iyileştirme potansiyeli var"
  → Önerileri avoidable kısma odakla
  → ROI hesabını avoidable_kW × operating_hours × energy_price üzerinden yap

Avoidable Ratio %20-%50: "Orta düzey iyileştirme potansiyeli"
  → Maliyet-etkin çözümler öner
  → Unavoidable kısmı "fiziksel limit" olarak açıkla

Avoidable Ratio < %20: "Ekipman zaten iyi seviyede"
  → Sistem seviyesi (cross-equipment) optimizasyon öner
  → Endogenous/Exogenous analiz öner (factory mode)
```

---

## 📋 Adım 8: Test Stratejisi

### 8.1 Yeni Testler (her engine için)

Her engine'in test dosyasına AV/UN testleri ekle. Pattern:

```python
class TestAvoidableUnavoidable:
    """Avoidable/Unavoidable exergy yıkımı testleri"""

    def test_av_un_sum_equals_total(self):
        """AV + UN = toplam exergy yıkımı"""
        inp = XxxInput()  # default input
        result = analyze_xxx(inp)
        total = result.exergy_destroyed_avoidable_kW + result.exergy_destroyed_unavoidable_kW
        assert abs(total - result.exergy_destroyed_kW) < 0.1

    def test_avoidable_non_negative(self):
        """Avoidable >= 0"""
        inp = XxxInput()
        result = analyze_xxx(inp)
        assert result.exergy_destroyed_avoidable_kW >= 0

    def test_unavoidable_non_negative(self):
        """Unavoidable >= 0"""
        inp = XxxInput()
        result = analyze_xxx(inp)
        assert result.exergy_destroyed_unavoidable_kW >= 0

    def test_avoidable_ratio_range(self):
        """Avoidable ratio 0-100 aralığında"""
        inp = XxxInput()
        result = analyze_xxx(inp)
        assert 0 <= result.avoidable_ratio_pct <= 100

    def test_poor_efficiency_has_high_avoidable(self):
        """Düşük verimli ekipman → yüksek avoidable"""
        # Kasten düşük verimli input oluştur
        inp = XxxInput(isentropic_efficiency=0.50)  # field adını uyarla
        result = analyze_xxx(inp)
        assert result.avoidable_ratio_pct > 30  # Düşük verim = çok avoidable

    def test_good_efficiency_has_low_avoidable(self):
        """Yüksek verimli ekipman → düşük avoidable"""
        # Kasten yüksek verimli input oluştur
        inp = XxxInput(isentropic_efficiency=0.90)  # field adını uyarla
        result = analyze_xxx(inp)
        assert result.avoidable_ratio_pct < 60  # Yüksek verim = az avoidable

    def test_av_un_in_api_dict(self):
        """to_api_dict() AV/UN field'larını içeriyor"""
        inp = XxxInput()
        result = analyze_xxx(inp)
        d = result.to_api_dict()
        assert 'exergy_destroyed_avoidable_kW' in d
        assert 'exergy_destroyed_unavoidable_kW' in d
        assert 'avoidable_ratio_pct' in d

    def test_av_un_in_sankey(self):
        """Sankey verisinde AV/UN node'ları var"""
        inp = XxxInput()
        result = analyze_xxx(inp)
        sankey = generate_xxx_sankey_data(result)
        node_names = [n['name'] for n in sankey['nodes']]
        assert 'Kaçınılabilir Yıkım' in node_names or 'Kaçınılamaz Yıkım' in node_names
```

### 8.2 Her Engine İçin Uyarla

Her engine'in test'ine yukarıdaki pattern'ı uyarla. Input field adları ve beklenen AV oranları ekipmana göre değişir:

| Engine | Düşük verim input | Yüksek verim input | AV oranı beklentisi |
|--------|-------------------|---------------------|---------------------|
| compressor | η_is=0.50 | η_is=0.88 | Düşük: >30%, Yüksek: <60% |
| boiler | flue_gas=250°C, excess_air=20% | flue_gas=130°C, excess_air=5% | Düşük: >10%, Yüksek: <20% |
| chiller | COP düşük | COP yüksek | Düşük: >20%, Yüksek: <40% |
| pump | η_pump=0.50, throttle | η_pump=0.85, VSD | Düşük: >40%, Yüksek: <50% |
| heat_exchanger | ΔP yüksek | ΔP düşük | Düşük: >10%, Yüksek: <20% |
| steam_turbine | η_is=0.60 | η_is=0.88 | Düşük: >30%, Yüksek: <40% |
| dryer | egzoz_temp=120°C | egzoz_temp=60°C | Düşük: >30%, Yüksek: <40% |

### 8.3 Regression

```bash
# TÜM testler geçmeli
pytest tests/ -v
# Beklenti: 307 + ~50 yeni = ~357+ test, %100 pass
```

---

## 📋 Adım 9: Entegrasyon Doğrulama

```bash
# 1. Core.py base class kontrolü
python3 -c "
from engine.core import ExergyResult
r = ExergyResult()
assert hasattr(r, 'exergy_destroyed_avoidable_kW')
assert hasattr(r, 'exergy_destroyed_unavoidable_kW')
assert hasattr(r, 'avoidable_ratio_pct')
print('✅ ExergyResult base class updated')
"

# 2. Her engine'de AV/UN hesaplanıyor
python3 -c "
from engine.compressor import CompressorInput, analyze_compressor
r = analyze_compressor(CompressorInput())
assert r.exergy_destroyed_avoidable_kW >= 0
assert r.exergy_destroyed_unavoidable_kW >= 0
total = r.exergy_destroyed_avoidable_kW + r.exergy_destroyed_unavoidable_kW
assert abs(total - r.exergy_destroyed_kW) < 0.1, f'{total} != {r.exergy_destroyed_kW}'
print(f'✅ Compressor: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%), UN={r.exergy_destroyed_unavoidable_kW:.1f} kW')
"

python3 -c "
from engine.boiler import analyze_boiler
from engine.boiler import BoilerInput  # veya gerçek class adı
r = analyze_boiler(BoilerInput())  # veya gerçek constructor
assert r.exergy_destroyed_avoidable_kW >= 0
print(f'✅ Boiler: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%)')
"

python3 -c "
from engine.chiller import analyze_chiller, ChillerInput
r = analyze_chiller(ChillerInput())
assert r.exergy_destroyed_avoidable_kW >= 0
print(f'✅ Chiller: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%)')
"

python3 -c "
from engine.pump import analyze_pump, PumpInput
r = analyze_pump(PumpInput())
assert r.exergy_destroyed_avoidable_kW >= 0
print(f'✅ Pump: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%)')
"

python3 -c "
from engine.heat_exchanger import analyze_heat_exchanger, HeatExchangerInput
r = analyze_heat_exchanger(HeatExchangerInput())
assert r.exergy_destroyed_avoidable_kW >= 0
print(f'✅ Heat Exchanger: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%)')
"

python3 -c "
from engine.steam_turbine import analyze_steam_turbine, SteamTurbineInput
r = analyze_steam_turbine(SteamTurbineInput())
assert r.exergy_destroyed_avoidable_kW >= 0
print(f'✅ Steam Turbine: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%)')
"

python3 -c "
from engine.dryer import analyze_dryer, DryerInput
r = analyze_dryer(DryerInput())
assert r.exergy_destroyed_avoidable_kW >= 0
print(f'✅ Dryer: AV={r.exergy_destroyed_avoidable_kW:.1f} kW ({r.avoidable_ratio_pct:.0f}%)')
"

# 3. to_api_dict kontrolü
python3 -c "
from engine.compressor import CompressorInput, analyze_compressor
r = analyze_compressor(CompressorInput())
d = r.to_api_dict()
assert 'exergy_destroyed_avoidable_kW' in d
assert 'exergy_destroyed_unavoidable_kW' in d
assert 'avoidable_ratio_pct' in d
print(f'✅ to_api_dict includes AV/UN fields')
"

# 4. Sankey kontrolü
python3 -c "
from engine.compressor import CompressorInput, analyze_compressor
from engine.sankey import generate_sankey_data
r = analyze_compressor(CompressorInput())
s = generate_sankey_data(r)
node_names = [n.get('name', '') for n in s['nodes']]
has_av = 'Kaçınılabilir Yıkım' in node_names
has_un = 'Kaçınılamaz Yıkım' in node_names
print(f'Sankey nodes: {node_names}')
assert has_av or has_un, 'AV/UN nodes missing from Sankey'
print(f'✅ Sankey AV/UN nodes present')
"

# 5. API endpoint testi
python3 -c "
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
resp = client.post('/api/analyze', json={
    'equipment_type': 'compressor',
    'subtype': 'screw',
    'params': {}
})
data = resp.json()
metrics = data.get('metrics', data.get('result', {}))
assert 'exergy_destroyed_avoidable_kW' in str(data), f'AV not in API response: {list(metrics.keys())[:10]}'
print(f'✅ API returns AV/UN data')
"
```

---

## ⚠️ Dikkat Edilecekler

1. **RECURSION GUARD KRİTİK.** Analyze fonksiyonu içinde tekrar kendini çağırınca sonsuz döngü olur. `_calc_avoidable=False` flag veya `_core()` ayrıştırması ZORUNLU.

2. **`import copy` eklemeyi UNUTMA.** Her engine'e `import copy` gerekecek.

3. **`__post_init__` yan etkileri.** Bazı Input class'larında `__post_init__` türetilmiş değerler hesaplar (dryer: water_removed, heat_input). deepcopy + field değişikliği post_init'i tetiklemez — eğer gerekiyorsa yeniden hesaplatmak için yeni bir instance oluşturabilirsin.

4. **Boiler'da CoolProp.** Boiler engine CoolProp kullanıyor. Unavoidable hesabında farklı sıcaklıklarla CoolProp çağrılabilir — hata kontrolü yap.

5. **Compressor'da 4 fonksiyon.** `analyze_compressor()`, `analyze_piston_compressor()`, `analyze_scroll_compressor()`, `analyze_centrifugal_compressor()` — hepsine ayrı AV/UN ekle. Her birinin referans parametreleri farklı.

6. **Sankey node ID yönetimi.** İki node yerine artık üç (veya daha fazla) node olabilir. ID numaralandırma dikkatli yapılmalı.

7. **Chiller absorption/vapor compression.** İkisi farklı code path'te analiz ediliyor. Her ikisine de AV/UN ekle.

8. **Mevcut testleri bozma.** 307 test + yeni testler → ~357+ test, hepsi geçmeli.

---

## ✅ Tamamlanma Kriterleri

- [ ] `engine/core.py` — ExergyResult'a 3 yeni field eklendi
- [ ] `engine/core.py` — `to_api_dict()` AV/UN field'larını içeriyor
- [ ] `engine/compressor.py` — 4 analyze fonksiyonunun hepsinde AV/UN hesaplanıyor
- [ ] `engine/boiler.py` — AV/UN hesaplanıyor
- [ ] `engine/chiller.py` — AV/UN hesaplanıyor (absorption + vapor comp.)
- [ ] `engine/pump.py` — AV/UN hesaplanıyor
- [ ] `engine/heat_exchanger.py` — AV/UN hesaplanıyor
- [ ] `engine/steam_turbine.py` — AV/UN hesaplanıyor
- [ ] `engine/dryer.py` — AV/UN hesaplanıyor
- [ ] 7 engine'in Sankey fonksiyonlarında destruction node → AV + UN ikiye bölündü
- [ ] Factory Sankey'de toplam AV/UN gösteriliyor
- [ ] `frontend/src/services/api.js` — AV/UN mapping eklendi
- [ ] `frontend/src/components/results/ResultsPanel.jsx` — AV/UN stacked bar eklendi
- [ ] `api/services/claude_code_service.py` — AI prompt'a AV/UN verisi eklendi
- [ ] Yeni testler yazıldı (her engine için ~7 test × 7 engine ≈ 49 test)
- [ ] Mevcut 307 test hâlâ geçiyor (regression yok)
- [ ] Tüm entegrasyon doğrulama scriptleri başarılı
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| AV/UN desteği | 0/7 ekipman | 7/7 ekipman |
| Sankey'de AV/UN | Yok | Tüm ekipmanlar + fabrika |
| Frontend'de AV/UN | Yok | Stacked bar + metrik kartları |
| AI'da AV/UN bilgisi | Yok | Prompt'a dahil |
| Test sayısı | 307 | ~357+ |
| Test başarı oranı | %100 | %100 |
