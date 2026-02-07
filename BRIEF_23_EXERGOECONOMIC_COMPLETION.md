# BRIEF_23: Exergoekonomik Analiz Tamamlama

> **Tarih:** 2026-02-05
> **Oncelik:** Yuksek
> **Tahmini Sure:** 2-3 saat
> **Etkilenen Dosyalar:** engine/exergoeconomic.py, engine/heat_exchanger.py, engine/steam_turbine.py, engine/dryer.py, tests/test_exergoeconomic.py

---

## 1. Problem

ExergyLab'in exergoekonomik analizi (SPECO metodolojisi) 7 ekipmandan sadece 4'unde gercek maliyet korelasyonlarina sahip. Kalan 3 ekipman (heat_exchanger, steam_turbine, dryer) varsayilan degerlere dusuyor. Bu durum:

- Exergoekonomik sonuclarin guvenilirligini dusuruyor
- f-faktor ve r-faktor yorumlarini yaniltici yapiyor
- Fabrika seviyesi maliyet dagitimini bozuyor

### Mevcut Durum

| Ekipman | a | b | Formul | Durum |
|---------|---|---|--------|-------|
| Kompresor | 3,500 | 0.70 | PEC = 3500 × W^0.70 | ✅ Tamamlandi |
| Kazan | 2,000 | 0.75 | PEC = 2000 × W^0.75 | ✅ Tamamlandi |
| Chiller | 1,200 | 0.80 | PEC = 1200 × W^0.80 | ✅ Tamamlandi |
| Pompa | 1,000 | 0.65 | PEC = 1000 × W^0.65 | ✅ Tamamlandi |
| Isi Esanjoru | ? | ? | Varsayilan kullaniliyor | ❌ Eksik |
| Buhar Turbini | ? | ? | Varsayilan kullaniliyor | ❌ Eksik |
| Kurutma Firini | ? | ? | Varsayilan kullaniliyor | ❌ Eksik |

---

## 2. Hedef

3 eksik ekipman tipi icin literatur tabanli maliyet korelasyonlari ekleyerek exergoekonomik analizi tamamlamak.

---

## 3. Maliyet Korelasyonlari -- Literatur Referanslari

Asagidaki korelasyonlar Bejan, Tsatsaronis & Moran (1996) "Thermal Design & Optimization" ve Turton et al. (2018) "Analysis, Synthesis and Design of Chemical Processes" kaynaklarindan derlenip ExergyLab formatina uyarlanmistir.

### 3.1 Isi Esanjoru (Heat Exchanger)

**Temel boyutlandirma parametresi:** Isi transfer alani (A, m²) veya isi kapasitesi (Q, kW)

Mevcut sistemde `estimate_equipment_cost(capacity_kW, equipment_type)` guc bazli calistigindan, isi esanjorlerinde `Q_dot` (isi yukü, kW) kullanilacak.

```python
COST_CORRELATIONS = {
    # ... mevcut 4 ekipman ...
    "heat_exchanger": {
        "a": 1_500,
        "b": 0.75,
        # PEC = 1500 × Q^0.75  (USD, 2020 bazli)
        # Kaynak: Turton et al. (2018), shell-and-tube referans
        # Gecerli aralik: 10 kW - 10,000 kW
        # Not: plate HX icin a=1200, air-cooled icin a=2000 uygulanabilir
        "subtypes": {
            "shell_tube":   {"a": 1_500, "b": 0.75},
            "plate":        {"a": 1_200, "b": 0.72},
            "air_cooled":   {"a": 2_000, "b": 0.78},
            "double_pipe":  {"a": 1_000, "b": 0.68},
            "spiral":       {"a": 1_800, "b": 0.76},
            "economizer":   {"a": 1_400, "b": 0.73},
            "recuperator":  {"a": 1_600, "b": 0.74},
        }
    },
}
```

### 3.2 Buhar Turbini (Steam Turbine)

**Temel boyutlandirma parametresi:** Cikis gucu (W_out, kW)

```python
COST_CORRELATIONS = {
    # ...
    "steam_turbine": {
        "a": 4_500,
        "b": 0.70,
        # PEC = 4500 × W^0.70  (USD, 2020 bazli)
        # Kaynak: Bejan, Tsatsaronis & Moran (1996), Tsatsaronis (2003)
        # Gecerli aralik: 100 kW - 50,000 kW
        "subtypes": {
            "back_pressure":  {"a": 4_000, "b": 0.70},
            "condensing":     {"a": 5_000, "b": 0.72},
            "extraction":     {"a": 5_500, "b": 0.73},
            "orc":            {"a": 6_000, "b": 0.75},  # ORC daha pahali
            "micro_turbine":  {"a": 3_000, "b": 0.65},
        }
    },
}
```

### 3.3 Kurutma Firini (Dryer)

**Temel boyutlandirma parametresi:** Isi yukü veya buharlatirma kapasitesi (kW)

```python
COST_CORRELATIONS = {
    # ...
    "dryer": {
        "a": 2_500,
        "b": 0.78,
        # PEC = 2500 × Q^0.78  (USD, 2020 bazli)
        # Kaynak: Turton et al. (2018), Peters & Timmerhaus (2003)
        # Gecerli aralik: 50 kW - 5,000 kW
        "subtypes": {
            "convective":     {"a": 2_500, "b": 0.78},
            "rotary":         {"a": 3_000, "b": 0.80},
            "fluidized_bed":  {"a": 3_500, "b": 0.82},
            "spray":          {"a": 4_000, "b": 0.83},
            "belt":           {"a": 2_800, "b": 0.77},
            "heat_pump":      {"a": 4_500, "b": 0.80},  # HP ek maliyeti
            "infrared":       {"a": 2_200, "b": 0.72},
            "drum":           {"a": 2_000, "b": 0.75},
        }
    },
}
```

---

## 4. Uygulama Plani

### Adim 1: `engine/exergoeconomic.py` Guncelleme

1. `COST_CORRELATIONS` sozlugune 3 yeni ekipman tipini ekle (yukaridaki degerlerle)
2. `estimate_equipment_cost()` fonksiyonunu **alt tip destegi** ile genislet:

```python
def estimate_equipment_cost(capacity_kW: float, equipment_type: str, subtype: str = None) -> float:
    """
    Guc yasasi maliyet korelasyonu ile PEC tahmini.
    
    Alt tip verilmisse, alt tipe ozgu korelasyon kullanilir.
    Verilmemisse, ekipman tipinin genel korelasyonu kullanilir.
    """
    if equipment_type not in COST_CORRELATIONS:
        # Fallback: genel korelasyon
        return 1000 * capacity_kW ** 0.70
    
    corr = COST_CORRELATIONS[equipment_type]
    
    # Alt tip korelasyonu varsa kullan
    if subtype and "subtypes" in corr and subtype in corr["subtypes"]:
        sub_corr = corr["subtypes"][subtype]
        a, b = sub_corr["a"], sub_corr["b"]
    else:
        a, b = corr["a"], corr["b"]
    
    return a * capacity_kW ** b
```

3. `_apply_exergoeconomic()` fonksiyonunu guncelleyerek `subtype` parametresi ekle:

```python
def _apply_exergoeconomic(result: ExergyResult, equipment_type: str, 
                          capacity_kW: float, subtype: str = None,
                          c_fuel_eur_kwh: float = 0.08,
                          interest_rate: float = 0.10,
                          lifetime_years: int = 20,
                          maintenance_factor: float = 1.06) -> ExergyResult:
```

### Adim 2: Ekipman Motorlarini Guncelle

Her 3 ekipman motorunda (`heat_exchanger.py`, `steam_turbine.py`, `dryer.py`) `_apply_exergoeconomic()` cagrisina `subtype` parametresini ekle.

**heat_exchanger.py:**
```python
# Mevcut (varsayilan):
_apply_exergoeconomic(result, "heat_exchanger", Q_dot_kW)

# Yeni:
_apply_exergoeconomic(result, "heat_exchanger", Q_dot_kW, subtype=subtype)
```

**steam_turbine.py:**
```python
_apply_exergoeconomic(result, "steam_turbine", W_out_kW, subtype=subtype)
```

**dryer.py:**
```python
_apply_exergoeconomic(result, "dryer", Q_dot_kW, subtype=subtype)
```

**AYRICA:** Mevcut 4 ekipmani da (compressor, boiler, chiller, pump) `subtype` parametresiyle guncelle -- geriye donuk uyumlu olacak sekilde.

### Adim 3: Mevcut 4 Ekipmana Alt Tip Korelasyonlari Ekle

Mevcut 4 ekipman da alt tip korelasyonu desteklemeli (opsiyonel ama tutarlilik icin):

```python
"compressor": {
    "a": 3_500, "b": 0.70,
    "subtypes": {
        "screw":        {"a": 3_500, "b": 0.70},
        "screw_oilfree":{"a": 4_200, "b": 0.72},
        "piston":       {"a": 2_800, "b": 0.68},
        "scroll":       {"a": 3_000, "b": 0.69},
        "centrifugal":  {"a": 5_000, "b": 0.75},
        "roots":        {"a": 2_500, "b": 0.65},
    }
},
"boiler": {
    "a": 2_000, "b": 0.75,
    "subtypes": {
        "steam_firetube":  {"a": 2_000, "b": 0.75},
        "steam_watertube": {"a": 2_500, "b": 0.78},
        "hotwater":        {"a": 1_500, "b": 0.72},
        "condensing":      {"a": 2_800, "b": 0.76},
        "waste_heat":      {"a": 1_800, "b": 0.70},
        "electric":        {"a": 1_200, "b": 0.65},
        "biomass":         {"a": 3_000, "b": 0.80},
    }
},
"chiller": {
    "a": 1_200, "b": 0.80,
    "subtypes": {
        "screw":          {"a": 1_200, "b": 0.80},
        "centrifugal":    {"a": 1_800, "b": 0.82},
        "scroll":         {"a": 1_000, "b": 0.75},
        "reciprocating":  {"a": 1_100, "b": 0.78},
        "absorption":     {"a": 2_200, "b": 0.85},
        "air_cooled":     {"a": 1_400, "b": 0.79},
        "water_cooled":   {"a": 1_300, "b": 0.80},
    }
},
"pump": {
    "a": 1_000, "b": 0.65,
    "subtypes": {
        "centrifugal":           {"a": 1_000, "b": 0.65},
        "positive_displacement": {"a": 1_500, "b": 0.70},
        "submersible":           {"a": 1_200, "b": 0.68},
        "vertical_turbine":      {"a": 1_400, "b": 0.69},
        "booster":               {"a": 900,  "b": 0.63},
        "vacuum":                {"a": 1_800, "b": 0.72},
    }
},
```

### Adim 4: Kapasite Parametresi Dogru Secimi

Her ekipman tipi icin `estimate_equipment_cost()` fonksiyonuna gonderilen `capacity_kW` degeri dogru olmali:

| Ekipman | capacity_kW olarak ne gonderilmeli |
|---------|-------------------------------------|
| Kompresor | W_in (kompresore verilen guc) |
| Kazan | Q_dot (uretilen isi) |
| Chiller | Q_evap (sogutma kapasitesi) |
| Pompa | W_in (pompaya verilen guc) |
| **Isi Esanjoru** | **Q_dot (transfer edilen isi)** |
| **Buhar Turbini** | **W_out (uretilen guc)** |
| **Kurutma Firini** | **Q_dot (kurutma isi yukü)** |

### Adim 5: Testler

`tests/test_exergoeconomic.py` dosyasina asagidaki testleri ekle:

```python
# 1. Yeni 3 ekipman icin maliyet korelasyonu testi
@pytest.mark.parametrize("equipment_type,capacity,expected_range", [
    ("heat_exchanger", 500, (15_000, 150_000)),
    ("steam_turbine", 1000, (50_000, 500_000)),
    ("dryer", 200, (20_000, 200_000)),
])
def test_new_cost_correlations(equipment_type, capacity, expected_range):
    cost = estimate_equipment_cost(capacity, equipment_type)
    assert expected_range[0] <= cost <= expected_range[1]

# 2. Alt tip korelasyonu testi
def test_subtype_cost_differs_from_default():
    cost_default = estimate_equipment_cost(500, "heat_exchanger")
    cost_plate = estimate_equipment_cost(500, "heat_exchanger", subtype="plate")
    assert cost_default != cost_plate  # Alt tip farkli deger vermeli

# 3. Tum 7 ekipman icin SPECO entegrasyon testi
@pytest.mark.parametrize("equipment_type", [
    "compressor", "boiler", "chiller", "pump",
    "heat_exchanger", "steam_turbine", "dryer"
])
def test_full_speco_pipeline(equipment_type):
    """Tum ekipmanlar icin exergoekonomik alanlar dolu olmali."""
    # Ekipmana uygun test input'u olustur
    # analyze_{equipment}() cagir
    # result.exergoeconomic_f_factor > 0 dogrula
    # result.exergoeconomic_Z_dot_eur_h > 0 dogrula
    pass  # Detay uygulamada

# 4. Alt tip fallback testi
def test_unknown_subtype_falls_back_to_default():
    cost_default = estimate_equipment_cost(500, "compressor")
    cost_unknown = estimate_equipment_cost(500, "compressor", subtype="unknown_type")
    assert cost_default == cost_unknown

# 5. Fabrika seviyesi exergoekonomik tutarlilik
def test_factory_exergoeconomic_aggregation():
    """Fabrika toplam maliyet orani = tekil ekipman maliyet oranlari toplami."""
    pass  # Detay uygulamada
```

### Adim 6: AI Skill Dosyalarini Guncelle

`skills/core/exergy_fundamentals.md` dosyasinda exergoekonomik bolumu guncelleyerek:
- 7/7 ekipmanda maliyet korelasyonu oldugunu belirt
- Alt tip korelasyonlarindan bahset
- f-faktor ve r-faktor yorumlama rehberini guncelle

`skills/factory/economic_advisor.md` dosyasinda:
- Fabrika seviyesi maliyet dagitimi orneklerini guncelle

---

## 5. Dogrulama Kontrol Listesi

- [ ] `COST_CORRELATIONS` sozlugunde 7 ekipman tipi var
- [ ] Her ekipman tipinde `subtypes` sozlugu var
- [ ] `estimate_equipment_cost()` subtype parametresini kabul ediyor
- [ ] `_apply_exergoeconomic()` subtype parametresini iletiyor
- [ ] 7 ekipman motorunun hepsinde `subtype` parametresi geciriliyor
- [ ] Mevcut 4 ekipmanin davranisi degismedi (geriye uyumluluk)
- [ ] Yeni 3 ekipman artik varsayilana dusmuyor
- [ ] `pytest tests/test_exergoeconomic.py -v` gecti
- [ ] `pytest tests/ -v` tum testler gecti
- [ ] Fabrika analizinde maliyet dagitimi mantikli gorunuyor
- [ ] Frontend'de exergoekonomik sonuclar 7 ekipmanda goruluyor

---

## 6. Notlar

### CEPCI Enflasyon Ayarlamasi (Opsiyonel, Gelecek Brief)

Mevcut korelasyonlar 2020 USD bazli. Ileriki asamada CEPCI (Chemical Engineering Plant Cost Index) ile yil bazli enflasyon ayarlamasi eklenebilir:

```
PEC_adjusted = PEC_base × (CEPCI_current / CEPCI_base)
```

Bu brief kapsaminda sabit 2020 USD yeterli.

### Kapasite Sinirlari

Her korelasyonun gecerli oldugu kapasite araligi var. Aralik disinda uyari mesaji verilebilir:

```python
CAPACITY_RANGES = {
    "heat_exchanger": (10, 10_000),    # kW
    "steam_turbine":  (100, 50_000),   # kW
    "dryer":          (50, 5_000),     # kW
}
```

Bu da opsiyonel -- uyari mesaji eklemek kullanici deneyimini iyilestirir ama zorunlu degil.

---

## 7. Claude Code Prompt

```
PROJECT_ANALYSIS.md dosyasini ve BRIEF_23_EXERGOECONOMIC_COMPLETION.md dosyasini oku.

Gorev: ExergyLab'in exergoekonomik analizini tamamla.

1. engine/exergoeconomic.py dosyasini ac ve mevcut COST_CORRELATIONS sozlugunu bul.
2. Brief'teki 3 yeni ekipman (heat_exchanger, steam_turbine, dryer) korelasyonlarini ekle.
3. Mevcut 4 ekipmana da alt tip (subtypes) korelasyonlarini ekle.
4. estimate_equipment_cost() fonksiyonuna subtype parametresi ekle (Brief Adim 1'deki gibi).
5. _apply_exergoeconomic() fonksiyonuna subtype parametresi ekle ve ileri aktar.
6. engine/heat_exchanger.py, engine/steam_turbine.py, engine/dryer.py dosyalarinda _apply_exergoeconomic() cagrilarini subtype ile guncelle.
7. engine/compressor.py, engine/boiler.py, engine/chiller.py, engine/pump.py dosyalarinda da _apply_exergoeconomic() cagrilarini subtype ile guncelle (geriye uyumlu).
8. tests/test_exergoeconomic.py dosyasina Brief Adim 5'teki testleri ekle.
9. pytest tests/test_exergoeconomic.py -v calistir ve tum testlerin gectigini dogrula.
10. pytest tests/ -v calistir ve hicbir mevcut testin kirilmadigini dogrula.

Onemli: Mevcut 4 ekipmanin davranisini bozma. subtype=None oldugunda mevcut genel korelasyonlar kullanilmaya devam etmeli.
```

---

*BRIEF_23 -- ExergyLab Exergoekonomik Analiz Tamamlama*
*Yazar: Claude (ExergyLab gelistirme destegi)*
*Tarih: 2026-02-05*
