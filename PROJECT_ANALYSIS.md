# ExergyLab - Kapsamli Proje Analizi

> **Son Guncelleme:** 2026-02-07
> **Versiyon:** 3.1
> **Durum:** Uretim (Production)
> **HEAD:** 32980c8

---

## Icindekiler

1. [Proje Ozeti](#1-proje-ozeti)
2. [Mimari Genel Bakis](#2-mimari-genel-bakis)
3. [Engine Katmani (Detayli)](#3-engine-katmani-detayli)
4. [API Katmani](#4-api-katmani)
5. [Frontend Katmani](#5-frontend-katmani)
6. [Test Altyapisi](#6-test-altyapisi)
7. [Knowledge Base](#7-knowledge-base)
8. [Bagimliliklar](#8-bagimliliklar)
9. [Konfigurasyon](#9-konfigurasyon)
10. [Bilinen Kisitlamalar ve Teknik Borc](#10-bilinen-kisitlamalar-ve-teknik-borc)
11. [Gelistirme Gecmisi](#11-gelistirme-gecmisi)
12. [Sonraki Adimlar (Backlog)](#12-sonraki-adimlar-backlog)

---

## 1. Proje Ozeti

ExergyLab, 7 endustriyel ekipman tipinin ve fabrikalarin exergy analizini yapan, 6 ileri analiz motoru ve AI destekli yorumlar sunan bir enerji verimliligi platformudur. Termodinamigin ikinci yasasina dayali exergy analizi, klasik enerji verimliliginden farkli olarak termodinamik kalitenin gercek olcumunu saglar: dusuk sicakliktaki isi dusuk exergy tasir, yuksek sicakliktaki isi yuksek exergy tasir.

Platform; kompresor, kazan, chiller, pompa, isi esanjoru, buhar turbini ve kurutma firini icin tek ekipman analizinden, coklu ekipman fabrika agregasyonuna, Linnhoff pinch analizinden Tsatsaronis ileri exergy dekompozisyonuna, Bejan entropi uretim minimizasyonundan ISO 50001 enerji yonetim denetimlerine kadar genis bir analiz yelpazesi sunar.

Frontend katmani React 19 + Plotly.js ile Sankey diyagramlari, radar benchmark grafikleri, composite curve ve GCC gorsellestirmeleri saglarken, backend katmani FastAPI + CoolProp + SQLAlchemy ile termodinamik hesaplamalari, veritabani kaliciligini ve Claude API uzerinden Turkce AI yorumlamayi yonetir.

### Platform Ozellikleri

| Ozellik | Aciklama |
|---------|----------|
| 7 Ekipman Tipi | Kompresor, kazan, chiller, pompa, isi esanjoru, buhar turbini, kurutma firini |
| 46 Alt Tip | Her ekipman icin detayli alt tip destegi |
| 6 Ileri Analiz Motoru | Pinch, ileri exergy, exergoekonomik, termoekonomik opt., EGM, enerji yonetimi |
| AI Yorumlama | Claude API ile Turkce teknik yorumlar (305 knowledge dosyasi) |
| What-If Senaryolar | Baseline vs senaryo karsilastirmasi (7 ekipman) |
| Radar Benchmark | 6 eksenli performans degerlendirme (A-F not) |
| AV/UN Ayrisim | Kacinilinabilir/kacinilmaz exergy yikim analizi (Tsatsaronis) |
| Exergoekonomik | SPECO metodolojisi, f-faktor, r-faktor, 7 tip maliyet korelasyonu |
| Fabrika Analizi | Coklu ekipman agregasyonu, hotspot tespiti, entegrasyon firsatlari |
| SQLite Kalicilik | Proje ve analiz sonuclarinin veritabaninda saklanmasi |
| JWT Kimlik Dogrulama | Opsiyonel kullanici yetkilendirmesi |

### Teknoloji Stack

| Katman | Teknoloji |
|--------|-----------|
| Backend | Python 3.10+, FastAPI, Pydantic v2, SQLAlchemy 2.0 |
| Frontend | React 19.2, Vite 7.2, TailwindCSS 3.4, Plotly.js 3.3 |
| AI | Claude API (yorumlama + sohbet) via subprocess CLI |
| Termodinamik | CoolProp (buhar/su ozellikleri) |
| Veritabani | SQLite + aiosqlite |
| Auth | python-jose (JWT HS256), passlib (bcrypt) |
| XSS Koruma | DOMPurify 3.3 (frontend HTML render) |

### Metrik Ozeti

| Metrik | Deger |
|--------|-------|
| **Toplam Kod Satiri** | **30,080** |
| Python satiri | 22,227 |
| JS/JSX satiri | 7,853 |
| Engine modulleri | 20 dosya (10,419 satir) |
| API modulleri | 28 dosya (4,872 satir) |
| Frontend dosyalari | 67 component + 6 sayfa (7,853 satir) |
| Knowledge dosyalari | 305 |
| Skill dosyalari | 17 |
| Test dosyalari | 18 (17 test modulu + conftest + __init__) |
| Test fonksiyonlari | 671 |
| Test satiri | 6,936 |
| API endpointleri | 25 |
| Veritabani tablolari | 6 |
| Ekipman tipleri | 7 (46 alt tip) |

---

## 2. Mimari Genel Bakis

### 2.1 Tech Stack

```
+-------------------+         +-------------------+         +------------------+
|                   |  HTTP   |                   |         |                  |
|   React Frontend  | ------> |   FastAPI Backend  | ------> |  Engine Modules  |
|   (Vite + Tailwind)|  /api  |   (REST API)      |         |  (20 dosya)      |
|                   |         |                   |         |                  |
+-------------------+         +--------+----------+         +------------------+
                                       |
                              +--------+----------+
                              |                   |
                    +---------+---------+ +-------+---------+
                    |                   | |                 |
                    |   Claude AI API   | |  SQLite DB      |
                    |   (subprocess)    | |  (aiosqlite)    |
                    |                   | |                 |
                    +-------------------+ +-----------------+
```

### 2.2 Dizin Yapisi

```
exergy-lab/
|
|-- api/                              # FastAPI backend (4,872 satir, 28 dosya)
|   |-- main.py                       # App, CORS, lifespan, router kaydi (66 satir)
|   |-- auth/                         # Kimlik dogrulama (142 satir, 5 dosya)
|   |   |-- config.py                 # JWT ayarlari (10 satir)
|   |   |-- dependencies.py           # Auth dependency injection (66 satir)
|   |   |-- schemas.py                # User/Token skemalari (26 satir)
|   |   |-- security.py               # Parola hash, JWT olusturma (40 satir)
|   |-- database/                     # Veritabani katmani (444 satir, 5 dosya)
|   |   |-- config.py                 # DB ayarlari (8 satir)
|   |   |-- crud.py                   # CRUD operasyonlari (230 satir)
|   |   |-- models.py                 # 6 SQLAlchemy modeli (145 satir)
|   |   |-- session.py                # Oturum yonetimi (38 satir)
|   |-- routes/                       # API endpointleri (1,926 satir, 8 dosya)
|   |   |-- analysis.py               # Ekipman analizi dispatch (943 satir)
|   |   |-- factory.py                # Fabrika CRUD + 6 ileri analiz (607 satir)
|   |   |-- interpret.py              # AI yorumlama (62 satir)
|   |   |-- chat.py                   # AI sohbet (75 satir)
|   |   |-- benchmarks.py             # Benchmark verileri (93 satir)
|   |   |-- solutions.py              # Cozum onerileri (85 satir)
|   |   |-- auth.py                   # Kimlik dogrulama (60 satir)
|   |-- schemas/                      # Pydantic modelleri (514 satir, 4 dosya)
|   |   |-- requests.py               # Istek skemalari (211 satir)
|   |   |-- responses.py              # Yanit skemalari (225 satir)
|   |   |-- factory.py                # Fabrika skemalari (77 satir)
|   |-- services/                     # Business logic (1,779 satir, 3 dosya)
|       |-- claude_code_service.py     # AI entegrasyonu (1,332 satir)
|       |-- equipment_registry.py      # Ekipman tip kayit defteri (173 satir)
|       |-- knowledge_router.py        # Bilgi yonlendirme (274 satir)
|
|-- engine/                            # Exergy hesaplama motorlari (10,419 satir, 20 dosya)
|   |-- core.py                        # DeadState, ExergyResult (171 satir)
|   |-- exergoeconomic.py             # SPECO analizi (292 satir)
|   |-- compressor.py                  # Kompresor analizi (660 satir)
|   |-- boiler.py                      # Kazan analizi (679 satir)
|   |-- chiller.py                     # Chiller analizi (523 satir)
|   |-- pump.py                        # Pompa analizi (498 satir)
|   |-- heat_exchanger.py             # Isi esanjoru analizi (525 satir)
|   |-- steam_turbine.py              # Buhar turbini analizi (592 satir)
|   |-- dryer.py                       # Kurutma firini analizi (567 satir)
|   |-- factory.py                     # Fabrika agregasyonu (928 satir)
|   |-- pinch.py                       # Pinch analizi (1,071 satir)
|   |-- advanced_exergy.py            # Ileri exergy dekompozisyonu (888 satir)
|   |-- entropy_generation.py         # EGM, Bejan sayisi (617 satir)
|   |-- thermoeconomic_optimization.py # Termoekonomik optimizasyon (788 satir)
|   |-- energy_management.py          # ISO 50001 enerji yonetimi (967 satir)
|   |-- sankey.py                      # Sankey diyagrami verisi (158 satir)
|   |-- radar.py                       # Radar benchmark (159 satir)
|   |-- compare.py                     # What-if karsilastirma (155 satir)
|   |-- utils.py                       # Yardimci fonksiyonlar (113 satir)
|   |-- __init__.py                    # Modul baslangici (68 satir)
|
|-- knowledge/                         # AI Knowledge Base (305 dosya)
|   |-- INDEX.md                       # Navigasyon haritasi
|   |-- compressor/                    # 19 dosya
|   |-- boiler/                        # 23 dosya
|   |-- chiller/                       # 25 dosya
|   |-- pump/                          # 23 dosya
|   |-- heat_exchanger/                # 21 dosya
|   |-- steam_turbine/                 # 23 dosya
|   |-- dryer/                         # 26 dosya
|   |-- factory/                       # 144 dosya
|       |-- pinch/                     # 18 dosya
|       |-- advanced_exergy/           # 18 dosya
|       |-- exergoeconomic/            # 18 dosya
|       |-- thermoeconomic_optimization/ # 16 dosya
|       |-- entropy_generation/        # 19 dosya
|       |-- energy_management/         # 21 dosya
|       |-- (kok dosyalar)             # ~34 dosya
|
|-- skills/                            # AI Skill dosyalari (17 dosya)
|   |-- core/                          # Temel beceriler (3 dosya)
|   |-- equipment/                     # Ekipman uzmanlari (7 dosya)
|   |-- factory/                       # Fabrika analisti (3 dosya)
|   |-- output/                        # Cikti formati (1 dosya)
|   |-- README.md                      # Skill sistemi aciklamasi
|   |-- SKILL_exergy_calculator.md     # Legacy skill
|   |-- SKILL_exergy_interpreter.md    # Legacy skill
|
|-- frontend/                          # React frontend (7,853 satir)
|   |-- src/
|       |-- pages/                     # 6 sayfa (1,453 satir)
|       |-- components/                # 67 component (5,806 satir)
|       |-- services/                  # API istemcileri (293 satir)
|       |-- hooks/                     # Custom hooks (100 satir)
|       |-- utils/                     # Yardimci fonksiyonlar (151 satir, 4 dosya)
|       |-- App.jsx                    # Routing (41 satir)
|       |-- main.jsx                   # Giris noktasi
|
|-- tests/                             # Pytest testleri (6,936 satir, 18 dosya)
|
|-- requirements.txt                   # Python bagimliliklari (17 paket)
|-- CLAUDE.md                         # Proje talimat dosyasi
|-- PROJECT_ANALYSIS.md               # Bu dosya
|-- exergylab.db                       # SQLite veritabani
```

### 2.3 Veri Akisi

```
Kullanici Girisi (Frontend)
    |
    v
React Component --> POST /api/analyze (tek ekipman)
                --> POST /api/factory/projects/{id}/analyze (fabrika)
    |
    v
API Route (analysis.py / factory.py)
    |
    v
Engine Dispatch: analyze_compressor / analyze_boiler / ... (7 ekipman motoru)
    |
    v
ExergyResult (temel exergy metrikleri)
    |
    +---> _apply_exergoeconomic()   [SPECO ekonomik alanlar enjekte]
    +---> generate_*_sankey_data()  [Sankey diyagram verisi]
    +---> generate_radar_data()     [6 eksenli benchmark puanlama]
    +---> compute_comparison()      [What-if delta hesaplama]
    |
    v
analyze_factory() -- Fabrika Agregasyon Pipeline (10 adim)
    |
    +---> 1. Ekipman analizleri (7 motora dispatch)
    +---> 2. Agregat hesaplama (toplam exergy, verimlilik)
    +---> 3. Hotspot tespiti (oncelik sirali exergy yikim)
    +---> 4. Entegrasyon firsatlari (9 capraz ekipman patterni)
    +---> 5. Fabrika Sankey uretimi
    +---> 6. Pinch analizi (Linnhoff, opsiyonel)
    +---> 7. Ileri exergy analizi (EN/EX + AV/UN 4-yollu, opsiyonel)
    +---> 8. Entropi uretim minimizasyonu (EGM, opsiyonel)
    +---> 9. Termoekonomik optimizasyon (f/r karar matrisi, opsiyonel)
    +---> 10. Enerji yonetimi (ISO 50001, opsiyonel)
    |
    v
FactoryAnalysisResult --> JSON API Response --> React Dashboard
    |
    v
POST /api/interpret | /api/factory/projects/{id}/interpret
    |
    v
claude_code_service.py (skills + knowledge yukleme -> Claude subprocess)
    |
    v
AI Turkce Yorum (JSON: ozet, analiz, oneriler, aksiyon plani)
```

---

## 3. Engine Katmani (Detayli)

20 Python dosyasi, toplam **10,419 satir**.

### 3.1 Temel Analiz Motorlari

#### core.py (171 satir) -- Temel Veri Yapilari

**Siniflar:**

`DeadState` -- Referans ortam kosullari:
- `T0: float = 298.15` (K)
- `P0: float = 101.325` (kPa)
- Metotlar: `T0_celsius()`, `from_celsius(T_celsius, P_kPa)`

`ExergyResult` -- Tum ekipman sonuclarinin temel sinifi:
- Exergy: `exergy_in_kW`, `exergy_out_kW`, `exergy_destroyed_kW`, `exergy_efficiency_pct`
- Ekonomik: `annual_loss_kWh`, `annual_loss_EUR`, `recoverable_heat_kW`
- AV/UN: `exergy_destroyed_avoidable_kW`, `exergy_destroyed_unavoidable_kW`, `avoidable_ratio_pct`
- Exergoekonomik: `exergoeconomic_Z_dot_eur_h`, `exergoeconomic_C_dot_destruction_eur_h`, `exergoeconomic_f_factor`, `exergoeconomic_r_factor`, `exergoeconomic_c_product_eur_kWh`, `exergoeconomic_total_cost_rate_eur_h`
- Metot: `to_dict()` -- serializasyon (yuvarlamali)

**Fonksiyonlar:**
- `heat_exergy(Q_kW, T_K, dead_state)` -- Isi exergisi: Ex_Q = Q * (1 - T0/T)
- `carnot_factor(T_hot_K, T_cold_K)` -- Carnot verimi
- `celsius_to_kelvin()`, `kelvin_to_celsius()`, `bar_to_kpa()`, `kpa_to_bar()`, `m3_min_to_m3_s()`
- `air_density(T_K, P_kPa)` -- Ideal gaz yasasi
- `compute_avoidable_split(actual_destroyed, unavoidable_destroyed)` -- AV/UN ayrisimi

**Sabitler:** `R_AIR = 0.287`, `R_UNIVERSAL = 8.314`, `CP_AIR = 1.005`

#### exergoeconomic.py (292 satir) -- SPECO Analizi

**Siniflar:**

`ExergoeconomicInput` -- Ekonomik parametreler:
- `equipment_cost_eur: Optional[float]`
- `installation_factor: float = 1.65`
- `interest_rate: float = 0.10`
- `equipment_life_years: int = 20`
- `maintenance_factor: float = 0.02`
- `annual_operating_hours: float = 6000`

`ExergoeconomicResult`:
- `Z_dot_eur_h`, `C_dot_destruction_eur_h`, `c_fuel_eur_kWh`, `c_product_eur_kWh`
- `f_factor`, `r_factor`, `total_cost_rate_eur_h`

**Sabitler -- COST_CORRELATIONS:**

PEC = a * W^b guc yasasi korelasyonlari (7 ekipman tipi x alt tipler):

| Ekipman | a (varsayilan) | b (varsayilan) | Alt Tip Varyasyonlari |
|---------|----------------|----------------|----------------------|
| Kompresor | 3,500 | 0.70 | screw, piston, scroll, centrifugal |
| Kazan | 2,000 | 0.75 | steam_firetube, condensing, waste_heat, biomass, electric |
| Chiller | 1,200 | 0.80 | screw, centrifugal, absorption |
| Pompa | 1,000 | 0.65 | centrifugal, submersible, vertical_turbine |
| Isi Esanjoru | 800 | 0.72 | shell_tube, plate, air_cooled |
| Buhar Turbini | 5,000 | 0.78 | back_pressure, condensing, orc |
| Kurutma Firini | 2,500 | 0.68 | rotary, fluidized_bed, spray, heat_pump |

**Fonksiyonlar:**
- `compute_crf(interest_rate, life_years)` -- Sermaye geri kazanim faktoru
- `compute_z_dot(total_investment, crf, maintenance_factor, annual_hours)` -- Yilliklandirilmis yatirim orani
- `estimate_equipment_cost(equipment_type, capacity_param_kW, subtype)` -- Guc yasasi maliyet tahmini
- `analyze_exergoeconomic(exergy_destroyed_kW, exergy_efficiency_pct, exergy_in_kW, exergy_out_kW, c_fuel_eur_kWh, equipment_type, capacity_param_kW, ...)` -- Tam SPECO analizi
- `_apply_exergoeconomic(result, equipment_type, c_fuel_eur_kWh, capacity_param_kW, ...)` -- ExergyResult'a ekonomik alanlari enjekte eder

### 3.2 Yardimci Moduller

#### sankey.py (158 satir)

- `generate_sankey_data(result, equipment_subtype)` -- Ekipman tipine gore dispatcher
- `_generate_compressor_sankey_data(result, compressor_type)` -- Nodes/links/summary (AV/UN dahil)
- Her ekipman tipi icin ozel sankey fonksiyonu

#### radar.py (159 satir)

6 eksenli benchmark puanlama sistemi:
- Eksenler: exergy_efficiency, improvement_status, sector_ranking, heat_recovery, destruction_ratio, cost_efficiency
- Not sistemi: A (85+), B (70+), C (50+), D (30+), F (<30)

Fonksiyonlar:
- `generate_radar_data(api_dict, operating_hours=6000)` -- 6 puan (0-100), genel not, harf notu
- `_compute_heat_recovery_score(api_dict)` -- Ekipman tipine ozel kaskad

#### compare.py (155 satir)

- `compute_comparison(baseline_dict, scenario_dict, energy_price_eur_kwh, operating_hours)` -- Delta, delta_pct, savings, improved/degraded metrics, Turkce ozet
- Yukseldikce iyi metrikler: exergy_efficiency_pct, exergy_output_kW, avoidable_ratio_pct
- Dusuldukce iyi metrikler: exergy_destroyed_kW, annual_loss_kWh, annual_loss_EUR

#### utils.py (113 satir)

- `convert_pressure(value, from_unit, to_unit)` -- bar, psi, atm, mbar, kPa
- `convert_temperature(value, from_unit, to_unit)` -- C, F, K
- `validate_positive(value, name)`, `validate_range(value, min_val, max_val, name)`
- `format_currency(value)`, `format_percentage(value)`, `format_power(value_kw)`
- `save_analysis_result(result, filepath)`, `load_analysis_result(filepath)`

### 3.3 Ekipman Motorlari (7 dosya, 4,044 satir)

Her ekipman modulu asagidaki standart yapiyi izler:

1. **Input Dataclass** -- Tum parametreleri tutar (alt tipe ozel varyantlar olabilir)
2. **Result Dataclass** -- ExergyResult'tan turetilir, ekipmana ozel alanlar ekler
3. **analyze_{equipment}(input_data, dead_state=None, _calc_avoidable=True)** -- Ana analiz fonksiyonu
4. **generate_{equipment}_sankey_data()** -- Sankey verisi
5. **get_{equipment}_recommendations()** -- Cozum onerileri
6. **_get_benchmark_comparison()** -- Benchmark eslestirme
7. **UNAVOIDABLE_REF_{EQUIPMENT}** sozlugu -- Tsatsaronis referans degerleri

| Modul | Satir | Alt Tipler | Analiz Fonksiyonu |
|-------|-------|------------|-------------------|
| compressor.py | 660 | 4 (screw, piston, scroll, centrifugal) | `analyze_compressor()` |
| boiler.py | 679 | 7 (steam_firetube, steam_watertube, hotwater, condensing, waste_heat, electric, biomass) | `analyze_boiler()` |
| chiller.py | 523 | 7 (screw, centrifugal, scroll, reciprocating, absorption, air_cooled, water_cooled) | `analyze_chiller()` |
| pump.py | 498 | 6 (centrifugal, positive_displacement, submersible, vertical_turbine, booster, vacuum) | `analyze_pump()` |
| heat_exchanger.py | 525 | 8 (shell_tube, plate, air_cooled, double_pipe, spiral, economizer, recuperator, finned_tube) | `analyze_heat_exchanger()` |
| steam_turbine.py | 592 | 5 (back_pressure, condensing, extraction, orc, micro_turbine) | `analyze_steam_turbine()` |
| dryer.py | 567 | 11 (convective, rotary, fluidized_bed, spray, belt, heat_pump, infrared, drum, conveyor, tray, microwave) | `analyze_dryer()` |

### 3.4 Fabrika Agregasyonu -- factory.py (928 satir)

**Siniflar:**

`EquipmentType` -- Enum: COMPRESSOR, BOILER, CHILLER, PUMP, HEAT_EXCHANGER, STEAM_TURBINE, DRYER

`EquipmentItem`:
- `id: str`, `name: str`, `equipment_type: str`, `subtype: str`
- `parameters: dict`, `analysis_result: Optional[dict]`

`FactoryAnalysisResult` -- Tam fabrika ciktisi:
- `equipment_results: List[dict]` -- Ekipman bazli analiz sonuclari
- `aggregates: dict` -- Toplam exergy metrikleri (exergy_in, exergy_out, destroyed, efficiency)
- `hotspots: List[dict]` -- Exergy yikim sirali ekipman listesi (priority: high/medium/low)
- `integration_opportunities: List[dict]` -- Capraz ekipman geri kazanim firsatlari
- `sankey: dict` -- Fabrika seviyesi Sankey diyagrami verisi
- `pinch_analysis: Optional[dict]` -- Linnhoff pinch analizi sonucu
- `advanced_exergy: Optional[dict]` -- EN/EX + AV/UN 4-yollu dekompozisyon
- `entropy_generation: Optional[dict]` -- EGM, Bejan sayilari
- `thermoeconomic_optimization: Optional[dict]` -- f/r karar matrisi + yatirim onerileri
- `energy_management: Optional[dict]` -- ISO 50001 olgunluk + aksiyon plani

**10 Adimli Fabrika Analiz Pipeline:**

| Adim | Fonksiyon | Aciklama |
|------|-----------|----------|
| 1 | `analyze_equipment_item()` | Her ekipman icin dispatch (7 motora) |
| 2 | `_calculate_aggregates()` | Toplam exergy metrikleri (SUM) |
| 3 | `_identify_hotspots()` | Oncelikli exergy yikim siralaması |
| 4 | `_detect_integration_opportunities()` | 9 capraz ekipman patterni |
| 5 | `_generate_factory_sankey()` | Birlesmis Sankey diyagrami |
| 6 | `analyze_pinch()` | Linnhoff pinch (feasibility check) |
| 7 | `analyze_advanced_exergy()` | EN/EX 4-quadrant (feasibility check) |
| 8 | `analyze_entropy_generation()` | EGM, Bejan (feasibility check) |
| 9 | `analyze_thermoeconomic_optimization()` | f/r matrisi (feasibility check) |
| 10 | `analyze_energy_management()` | ISO 50001 (feasibility check) |

Adimlar 6-10 best-effort: feasibility check basariszisa `None` doner, pipeline durmaz.

**Hotspot Oncelik Mantigi:**
```
if efficiency < 30% OR loss_ratio > 40% OR loss_kW > 20:    "high"
elif efficiency < 50% OR loss_ratio > 20% OR loss_kW > 5:   "medium"
else:                                                        "low"
```

**Entegrasyon Firsatlari (9 Pattern):**
1. Kompresor atik isisi → Kazan beslem suyu on isitma
2. Kompresor atik isisi → Mekan isitma
3. Kazan baca gazi → Absorption chiller
4. Chiller kondanser isisi → Sicak su
5. Pompa VSD retrofiti
6. Kurutma firini egzoz → HX hava on isitma
7. Buhar turbini egzoz → Absorption chiller
8. Kazan baca gazi → HX ekonomizer
9. Buhar turbini CHP → Tesis isitma

### 3.5 Ileri Analiz Motorlari (5 dosya, 4,331 satir)

#### 3.5.1 Pinch Analizi -- pinch.py (1,071 satir)

Linnhoff metodolojisi ile sicak/soguk akis eslestirme ve minimum yarar isisi hesaplama.

**Siniflar:**

`StreamType` -- Enum: HOT, COLD

`ThermalStream`:
- `stream_id`, `stream_type: StreamType`, `equipment_name`, `equipment_type`
- `description`, `T_supply_C`, `T_target_C`, `Q_dot_kW`, `CP_kW_per_K`
- `fluid`, `phase_change: bool`, `is_utility: bool`

`TemperatureInterval`:
- `T_upper_C`, `T_lower_C`, `delta_T_C`
- `sum_CP_hot`, `sum_CP_cold`, `delta_H_kW`, `cascade_kW`

`PinchResult`:
- `is_valid: bool`
- `streams: List[dict]`, `hot_stream_count`, `cold_stream_count`
- `pinch_temperature_C`, `delta_T_min_C = 10.0`
- `QH_min_kW`, `QC_min_kW`, `max_heat_recovery_kW`
- `QH_current_kW`, `QC_current_kW` (mevcut yarar isisi tahmini)
- `QH_excess_kW`, `QC_excess_kW`, `savings_pct`
- `annual_savings_kWh`, `annual_savings_EUR`
- `composite_curves`, `grand_composite_curve`, `intervals`, `hen_matches`
- `fuel_price_eur_kwh = 0.08`, `operating_hours = 8000`

**Sabitler:** `_MIN_Q_KW = 5.0`, `_MIN_DT_C = 2.0`, `_DEFAULT_STACK_T = 150.0`

**Akis Cikarma Fonksiyonlari:**
- `extract_thermal_streams(equipment_list, analysis_results, include_pumps=False)` -- 7 ekipman tipinden sicak/soguk akis cikarimi
- `_extract_boiler_streams()` -- Sicak (baca gazi) + soguk (beslem suyu)
- `_extract_compressor_streams()` -- Sicak (kompresyon isisi)
- `_extract_chiller_streams()` -- Sicak (kondanser) + soguk (evaporator)
- `_extract_heat_exchanger_streams()` -- Sicak + soguk taraflar
- `_extract_steam_turbine_streams()` -- Sicak egzoz
- `_extract_dryer_streams()` -- Sicak (egzoz) + soguk (kurutma yuku)

**Problem Table Algorithm:**
- `compute_shifted_temperatures(streams, delta_T_min_C)` -- Hot: T - dT/2; Cold: T + dT/2
- `create_temperature_intervals(streams, shifted_temps, delta_T_min_C)`
- `solve_cascade(intervals)` -- QH_min, QC_min, pinch noktasi

**Gorsellestirme:**
- `generate_composite_curves(streams, QH_min_kW)` -- Plotly verisi
- `generate_grand_composite_curve(intervals, cascade)` -- GCC verisi

**HEN Tasarimi:**
- `suggest_hen_matches(streams, pinch_T_shifted, delta_T_min_C)` -- Acgozlu (greedy) eslestirme

**Fizibilite:** `check_pinch_feasibility(streams, delta_T_min_C)` -- En az 1 sicak + 1 soguk akis, Q > 50 kW, sicaklik ortusme

**Ana Orkestrator:** `analyze_pinch(equipment_list, analysis_results, delta_T_min_C=10.0, fuel_price_eur_kwh=0.08, operating_hours=8000, include_pumps=False)` → `PinchResult`

#### 3.5.2 Ileri Exergy Analizi -- advanced_exergy.py (888 satir)

Tsatsaronis & Morosuk metodolojisi ile EN/EX (endojen/eksojen) ve AV/UN (kacinilinabilir/kacinilmaz) 4-yollu dekompozisyon.

**Sabitler:**

`BASE_ISOLATION_FACTORS` -- Ekipman bazli izolasyon faktoru (phi_0):

| Ekipman | phi_0 |
|---------|-------|
| compressor | 0.75 |
| boiler | 0.80 |
| chiller | 0.65 |
| pump | 0.85 |
| heat_exchanger | 0.55 |
| steam_turbine | 0.70 |
| dryer | 0.60 |

`INTERACTION_COEFFICIENTS` -- Seyrek matris {(etkilenen_tip, kaynak_tip): alpha}

`REFERENCE_EFFICIENCIES` -- En iyi uygulama referans verimlilikleri (tip/alt tip bazli):
- Kazan condensing: %95, waste_heat: %70
- Chiller absorption: %25, centrifugal: %45
- Kurutma firini heat_pump: %60, microwave: %38

**Siniflar:**

`AdvancedExergyEquipmentResult`:
- `equipment_id`, `equipment_name`, `equipment_type`, `subtype`
- `I_total_kW` -- Toplam exergy yikim
- `I_EN_kW`, `I_EX_kW` -- Endojen/eksojen ayrisim
- `isolation_factor: float` -- phi
- `I_AV_EN_kW`, `I_AV_EX_kW`, `I_UN_EN_kW`, `I_UN_EX_kW` -- 4-quadrant
- `I_AV_kW`, `I_UN_kW` -- Toplam kacinilinabilir/kacinilmaz
- `exogenous_sources: List[dict]` -- Bu ekipmani etkileyen diger ekipmanlar
- `priority: str`, `priority_reason: str`
- `warnings: List[str]`

`AdvancedExergyResult`:
- `is_valid: bool`
- `equipment_results: List[AdvancedExergyEquipmentResult]`
- Fabrika toplamlari: `total_I_EN_kW`, `total_I_EX_kW`, `total_I_AV_EN_kW`, `total_I_AV_EX_kW`, `total_I_UN_EN_kW`, `total_I_UN_EX_kW`, `total_I_kW`
- `endogenous_ratio: float`, `interaction_density: float`
- `priority_ranking: List[dict]`, `interaction_network: List[dict]`, `quadrant_chart_data: dict`
- `most_influential: str`, `most_affected: str`
- `warnings: List[str]`, `error: str`

**Hesaplama Fonksiyonlari:**
- `_calculate_efficiency_deviations(equipment_list, analysis_results)` -- delta = (eta_ref - eta_actual) / eta_ref, [-0.5, 1.0] arasi
- `_calculate_isolation_factors(...)` -- phi = phi_0 * (1 - SUM(alpha_ij * delta_j)), [0.20, 0.95] arasi
- `_analyze_single_equipment(item, result, isolation_factor, all_equipment, deviations)` -- EN/EX ve 4-quadrant

**Fizibilite:** `check_advanced_exergy_feasibility(equipment_list, analysis_results)` -- En az 3 ekipman, I_total > 100 kW

**Ana Orkestrator:** `analyze_advanced_exergy(equipment_list, analysis_results)` → `AdvancedExergyResult`

#### 3.5.3 Entropi Uretim Minimizasyonu (EGM) -- entropy_generation.py (617 satir)

Bejan N_s sayisi, Gouy-Stodola teoremi ve mekanizma bazli entropi uretim dekompozisyonu.

**Sabitler:**

`ENTROPY_DECOMPOSITION_FRACTIONS` -- (f_heat_transfer, f_pressure_drop, f_mixing) ekipman/alt tip bazli:
- Isi esanjoru: (0.80, 0.15, 0.05) -- Isi transferi baskin
- Pompa: (0.10, 0.85, 0.05) -- Basinc dusumu baskin
- Kazan: (0.20, 0.05, 0.75) -- Karisim baskin

`BEJAN_GRADES` -- Not sinifi:
- A: 0.00 - 0.15 (Mukemmel)
- B: 0.15 - 0.30 (Iyi)
- C: 0.30 - 0.50 (Ortalama)
- D: 0.50 - 0.70 (Zayif)
- F: 0.70 - 1.01 (Kritik)

**Siniflar:**

`EntropyEquipmentResult`:
- `equipment_id`, `equipment_name`, `equipment_type`, `subtype`
- `exergy_in_kW`, `exergy_destroyed_kW`, `exergy_efficiency_pct`
- `S_gen_kW_K` -- Gouy-Stodola: I_dot / T0
- `T0_K`
- `N_s: float` -- Bejan sayisi = I_dot / Ex_in
- `N_s_grade: str` -- A-F not
- `S_gen_heat_transfer_kW_K`, `S_gen_pressure_drop_kW_K`, `S_gen_mixing_kW_K`
- `dominant_mechanism: str`
- `Be_heat_transfer: Optional[float]` -- Sadece HX icin
- `N_s_augmentation: float`, `improvement_potential_pct: float`
- `s_gen_per_exergy_input: float`

`EntropyGenerationResult`:
- `is_valid: bool`
- `num_equipment`, `T0_K`
- `S_gen_total_kW_K`, `N_s_factory`
- Dekompozisyon toplamlari: `S_gen_heat_transfer_total_kW_K`, `S_gen_pressure_drop_total_kW_K`, `S_gen_mixing_total_kW_K`
- `dominant_mechanism_factory`
- Yuzdeler: `heat_transfer_pct`, `pressure_drop_pct`, `mixing_pct`
- `total_exergy_destroyed_kW` -- Gouy-Stodola dogrulama
- `equipment_results: List[EntropyEquipmentResult]`
- `irreversibility_ranking: List[Dict]`
- `decomposition_chart_data`, `bejan_number_chart_data`
- `warnings: List[str]`

**Fonksiyonlar:**
- `_analyze_single_equipment(item, result, T0_K)` -- Gouy-Stodola, N_s, dekompozisyon
- `_assign_bejan_grade(N_s)` -- A-F not atama
- `_get_decomposition_fractions(eq_type, subtype)` -- (f_ht, f_dp, f_mix)
- `_get_dominant_mechanism(S_ht, S_dp, S_mix)` -- Baskin mekanizma

**Fizibilite:** `check_egm_feasibility(equipment_list, analysis_results)` -- En az 1 ekipman, I_total > 10 kW

**Ana Orkestrator:** `analyze_entropy_generation(equipment_list, analysis_results, T0_K=298.15)` → `EntropyGenerationResult`

#### 3.5.4 Termoekonomik Optimizasyon -- thermoeconomic_optimization.py (788 satir)

Tsatsaronis f/r karar matrisi ile yatirim stratejisi belirleme, maliyet-fayda analizi.

**Sabitler:**

`STRATEGY_LABELS` -- 5 strateji: "invest", "parametric", "structural", "downsize", "maintain"

`STRATEGY_COLORS` -- Red (invest), Orange (parametric), Purple (structural), Blue (downsize), Green (maintain)

`OPTIMIZATION_ACTIONS` -- Ekipman tipi x strateji: ozel aksiyon listeleri (Turkce)

`INVESTMENT_ESTIMATES` -- Ekipman tipi x strateji: lambda fonksiyonlari ile maliyet tahmini

**Siniflar:**

`OptimizationRecommendation`:
- `equipment_id`, `equipment_name`, `equipment_type`, `subtype`
- `f_factor`, `r_factor` -- SPECO metrikleri
- `Z_dot_eur_h`, `C_dot_D_eur_h`, `C_total_dot_eur_h`
- `avoidable_ratio: float` (0-1)
- `strategy: str` -- invest | parametric | structural | downsize | maintain
- `strategy_label: str`, `priority: str` (high | medium | low)
- `recommended_actions: List[str]`
- `C_savings_potential_eur_h`, `C_savings_annual_eur`
- `estimated_investment_eur`, `simple_payback_years`

`ThermoeconomicOptimizationResult`:
- `is_valid: bool`
- `num_equipment`, `operating_hours`
- `total_Z_dot_eur_h`, `total_C_dot_D_eur_h`, `total_C_total_dot_eur_h`
- `factory_f_factor`
- `total_savings_potential_eur_h`, `total_savings_annual_eur`
- `total_estimated_investment_eur`, `factory_payback_years`
- `strategy_distribution: Dict[str, int]`, `priority_distribution: Dict[str, int]`
- `recommendations: List[OptimizationRecommendation]` -- Yillik tasarruf sirali
- `cost_benefit_ranking: List[Dict]`
- `f_r_scatter_data`, `savings_waterfall_data` -- Gorsellestirme verisi
- `warnings: List[str]`

**Karar Fonksiyonu:**
- `_determine_strategy(f_factor, r_factor, avoidable_ratio)` -- SPECO metriklerine gore strateji:
  - f < 0.25 & r > 0.5 → invest (exergy yikim baskin)
  - f > 0.65 → downsize (yatirim baskin)
  - 0.25 <= f <= 0.65 & avoidable > 0.5 → parametric
  - 0.25 <= f <= 0.65 & avoidable <= 0.5 → maintain
  - Diger → structural

**Fizibilite:** `check_thermoeconomic_feasibility(equipment_list, analysis_results)` -- Toplam C_dot_D > 10 EUR/h

**Ana Orkestrator:** `analyze_thermoeconomic_optimization(equipment_list, analysis_results, operating_hours=8000)` → `ThermoeconomicOptimizationResult`

#### 3.5.5 Enerji Yonetimi -- energy_management.py (967 satir)

ISO 50001 cercevesinde enerji performans gostergeleri (EnPI), olgunluk degerlendirmesi ve aksiyon plani olusturma. Diger 4 ileri analiz motorunun sonuclarini sentezler.

**Sabitler:**

`MATURITY_LEVELS`:
- leading: 90+ puan
- mature: 70+ puan
- developing: 50+ puan
- beginning: 30+ puan
- aware: 0+ puan

`MATURITY_DIMENSIONS` -- 7 ISO 50001 boyutu ile puanlama

`ACTION_CATEGORIES`:
- quick_win: 0-3 ay
- medium_term: 3-12 ay
- strategic: 1-3 yil
- monitoring: surekli

`GAP_RECOMMENDATIONS` -- Boyut bazli kapama aksiyonlari

**Siniflar:**

`EnPIMetrics` -- 7 Enerji Performans Gostergesi:
- `exergy_efficiency_pct` -- Fabrika exergy verimi (eta_ex)
- `specific_exergy_consumption` -- SEC = Ex_in / Ex_out
- `exergy_destruction_ratio_pct` -- EDR = I_total / Ex_in * 100
- `avoidable_loss_ratio_pct` -- ALR = I_avoidable / I_total * 100
- `energy_cost_intensity_eur_kWh` -- ECI = C_dot_D / Ex_in
- `heat_recovery_potential_pct` -- HRP = recoverable / I_total * 100
- `entropy_generation_intensity` -- EGI = N_s_factory

`MaturityDimension`:
- `dimension`, `label`, `iso_clause`, `score` (0-100), `max_score`
- `findings: List[str]`, `gaps: List[str]`

`ActionItem`:
- `id`, `source`, `equipment_id`, `equipment_name`
- `action`, `category`, `estimated_savings_eur`, `estimated_investment_eur`
- `payback_years`, `priority`, `timeline`

`EnergyManagementResult`:
- `is_valid: bool`
- `num_equipment`
- `enpi: Optional[EnPIMetrics]`
- `maturity_score: int` (0-100), `maturity_level: str`, `maturity_level_label: str`
- `maturity_dimensions: List[MaturityDimension]`
- `num_gaps: int`, `critical_gaps: List[str]` (puan < 50)
- `action_plan: List[ActionItem]`
- `action_summary: Dict` -- Kategorilere gore dagılim
- `total_potential_savings_eur`, `total_estimated_investment_eur`
- `enpi_radar_data`, `maturity_radar_data`, `action_timeline_data` -- Gorsellestirme
- `warnings: List[str]`

**Puanlama Fonksiyonlari (7 ISO 50001 boyutu):**
- `_score_energy_review(factory_data)` -- 6.3 Enerji Gozden Gecirmesi
- `_score_performance_indicators(factory_data)` -- 6.5 Performans Gostergeleri
- `_score_improvement_opportunities(factory_data)` -- 6.4 Iyilestirme Firsatlari
- `_score_action_planning(factory_data)` -- 6.6 Aksiyon Planlama
- `_score_monitoring(factory_data)` -- 9.1 Izleme
- `_score_heat_integration(factory_data)` -- 6.4 Isi Entegrasyonu
- `_score_cost_optimization(factory_data)` -- 6.5 Maliyet Optimizasyonu

Her fonksiyon donusu: `(score: int, findings: List[str], gaps: List[str])`

**Fizibilite:** `check_energy_management_feasibility(factory_dict)` -- En az 1 ekipman sonucu (exergy verisi)

**Ana Orkestrator:** `analyze_energy_management(factory_dict)` → `EnergyManagementResult`

---

## 4. API Katmani

28 Python dosyasi, toplam **4,872 satir**. 7 route dosyasi uzerinden **25 endpoint**.

### 4.1 Endpoint Listesi

#### Kok Endpointler (api/main.py -- 66 satir)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| GET | `/` | API bilgi + docs linki |
| GET | `/health` | Saglik kontrolu `{"status": "ok"}` |

#### Ekipman Analizi (api/routes/analysis.py -- 943 satir)

| Metot | Yol | Engine Fonksiyonu | Aciklama |
|-------|-----|-------------------|----------|
| GET | `/api/equipment-types` | `equipment_registry` | 7 ekipman tipi listesi |
| GET | `/api/equipment-types/{type}/subtypes` | `equipment_registry` | Alt tip listesi |
| GET | `/api/equipment-types/{type}/config` | `equipment_registry` | Alan tanimlari + varsayilan degerler |
| POST | `/api/analyze` | `analyze_compressor/boiler/...` | Tek ekipman exergy analizi |
| POST | `/api/compare` | `compute_comparison()` | Baseline vs senaryo karsilastirmasi |
| GET | `/api/compressor-types` | `equipment_registry` | Legacy geriye uyumluluk |

#### Benchmark ve Cozumler (benchmarks.py -- 93, solutions.py -- 85 satir)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| GET | `/api/benchmarks/{type}` | Sektorel verimlilik karsilastirma verileri |
| GET | `/api/solutions/{type}` | Filtrelenmis cozum onerileri |

#### AI Yorumlama ve Sohbet (interpret.py -- 62, chat.py -- 75 satir)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| POST | `/api/interpret` | Tek ekipman AI yorumu (Claude subprocess) |
| POST | `/api/chat` | Bilgi tabani destekli AI sohbet |

#### Kimlik Dogrulama (auth.py -- 60 satir)

| Metot | Yol | Auth | Aciklama |
|-------|-----|------|----------|
| POST | `/api/auth/register` | Hayir | Kullanici kaydi |
| POST | `/api/auth/login` | Hayir | JWT token alma |
| GET | `/api/auth/me` | Evet | Mevcut kullanici bilgisi |

#### Fabrika Yonetimi ve Ileri Analiz (factory.py -- 607 satir)

| Metot | Yol | Auth | Engine Fonksiyonu | Aciklama |
|-------|-----|------|-------------------|----------|
| POST | `/api/factory/projects` | Opsiyonel | -- | Yeni proje olustur |
| GET | `/api/factory/projects` | Opsiyonel | -- | Proje listesi |
| GET | `/api/factory/projects/{id}` | Opsiyonel | -- | Proje detayi |
| POST | `/api/factory/projects/{id}/equipment` | Opsiyonel | -- | Ekipman ekle |
| DELETE | `/api/factory/projects/{id}/equipment/{eid}` | Opsiyonel | -- | Ekipman kaldir |
| POST | `/api/factory/projects/{id}/analyze` | Opsiyonel | `analyze_factory()` | Fabrika analizi (tam pipeline) |
| POST | `/api/factory/projects/{id}/pinch` | Opsiyonel | `analyze_pinch()` | Pinch analizi |
| POST | `/api/factory/projects/{id}/advanced-exergy` | Opsiyonel | `analyze_advanced_exergy()` | Ileri exergy |
| POST | `/api/factory/projects/{id}/entropy-generation` | Opsiyonel | `analyze_entropy_generation()` | EGM |
| POST | `/api/factory/projects/{id}/thermoeconomic-optimization` | Opsiyonel | `analyze_thermoeconomic_optimization()` | Termoekonomik |
| POST | `/api/factory/projects/{id}/energy-management` | Opsiyonel | `analyze_energy_management()` | Enerji yonetimi |
| POST | `/api/factory/projects/{id}/interpret` | Opsiyonel | `interpret_factory_analysis()` | Fabrika AI yorumu |

### 4.2 Schemalar

#### AnalysisResponse (api/schemas/responses.py -- 225 satir)

MetricsResponse alanlari:
- **Exergy:** `exergy_input_kW`, `exergy_output_kW`, `exergy_destroyed_kW`, `exergy_efficiency_pct`
- **Isi Geri Kazanim:** `heat_recovery_potential_kW`, `heat_recovery_savings_eur_year`, `annual_loss_kWh`, `annual_loss_EUR`
- **AV/UN:** `exergy_destroyed_avoidable_kW`, `exergy_destroyed_unavoidable_kW`, `avoidable_ratio_pct`
- **Exergoekonomik:** `exergoeconomic_Z_dot_eur_h`, `exergoeconomic_C_dot_destruction_eur_h`, `exergoeconomic_f_factor`, `exergoeconomic_r_factor`, `exergoeconomic_c_product_eur_kWh`, `exergoeconomic_total_cost_rate_eur_h`
- **Ekipmana Ozel:** Kazan (thermal_efficiency_pct, combustion_loss_kW), Chiller (cop, cop_carnot, kw_per_ton), Pompa (hydraulic_power_kW, wire_to_water_efficiency_pct), HX (heat_duty_kW, lmtd_K, effectiveness, bejan_number), Buhar Turbini (shaft_power_kW, electrical_power_kW, chp_exergy_efficiency_pct), Kurutma Firini (water_removed_kg_h, specific_energy_kJ_kg_water)

#### FactoryAnalysisResponse (api/schemas/factory.py -- 77 satir)

```
success: bool
project_id: str
equipment_results: List[dict]
aggregates: dict
hotspots: List[dict]
integration_opportunities: List[dict]
sankey: dict
pinch_analysis: Optional[dict]
advanced_exergy: Optional[dict]
entropy_generation: Optional[dict]
thermoeconomic_optimization: Optional[dict]
energy_management: Optional[dict]
```

### 4.3 Veritabani Semasi (6 tablo)

| Tablo | Sutunlar | Aciklama |
|-------|----------|----------|
| `users` | id (UUID), email (unique), hashed_password, full_name, is_active, created_at | Kullanici kayitlari |
| `factory_projects` | id (8-char UUID), name, sector, description, owner_id (FK→users), created_at, updated_at | Fabrika projeleri |
| `equipment` | id (8-char UUID), project_id (FK→projects), name, equipment_type, subtype, parameters (JSON), created_at | Ekipman kayitlari |
| `analysis_results` | id (8-char UUID), equipment_id (FK→equipment, unique), result_data (JSON), analyzed_at | Analiz sonuclari (1-to-1) |
| `factory_analyses` | id (8-char UUID), project_id (FK→projects), aggregates (JSON), hotspots (JSON), integration_opportunities (JSON), sankey_data (JSON), analyzed_at | Fabrika analiz sonuclari |
| `ai_interpretations` | id (8-char UUID), project_id (FK→projects), equipment_id (FK→equipment), interpretation_data (JSON), created_at | AI yorum sonuclari |

Iliski: `User 1---* FactoryProject 1---* Equipment 1---1 AnalysisResult`
Tum cascade: `"all, delete-orphan"`

### 4.4 AI Servisi -- claude_code_service.py (1,332 satir)

AI yorumlama ve sohbet entegrasyonu. Claude Code CLI'yi subprocess ile cagirarak calisan moduler prompt sistemi.

**Anahtar Fonksiyonlar:**

| Fonksiyon | Aciklama |
|-----------|----------|
| `_load_skills(analysis_type, equipment_type)` | Moduler skill yukleme (core → equipment → factory → output) |
| `_load_relevant_knowledge(analysis_type, equipment_type, sector)` | Analiz turune gore knowledge dosyasi yonlendirme |
| `_build_prompt(analysis_result, equipment_type, subtype, parameters)` | Skills + knowledge + metrics ile prompt olusturma |
| `interpret_with_claude_code(analysis_result, ...)` | Ana async yorumlama (subprocess.run, timeout=120s) |
| `interpret_factory_analysis(project, sector)` | Fabrika seviyesi yorumlama (hotspot odakli) |
| `_extract_json(text)` | 3 katmanli JSON parser (dogrudan → markdown fence → regex) |

**Skill Yukleme Sirasi:**
1. Core (her zaman): `exergy_fundamentals.md` → `response_format.md` → `decision_trees.md`
2. Equipment (tek ekipman): `equipment/{type}_expert.md`
3. Factory (fabrika): `factory_analyst.md` → `integration_expert.md` → `economic_advisor.md`
4. Output (her zaman): `output/turkish_style.md`

**Knowledge Yonlendirme (knowledge_router.py -- 274 satir):**
- Tek ekipman: benchmarks.md, formulas.md, ilgili cozum dosyalari
- Fabrika: cross_equipment.md, prioritization.md, factory_benchmarks.md, sector_{sector}.md
- Ileri analiz: overview.md dosyalari (pinch, advanced_exergy, entropy_generation, exergoeconomic)

**Timeout:** 120 saniye (subprocess)
**Fallback:** Claude kullanilamadiginda guvenli varsayilan JSON donusu

---

## 5. Frontend Katmani

67 component + 6 sayfa, toplam **7,853 satir** JavaScript/JSX.

### 5.1 Rotalar (App.jsx -- 41 satir)

| Rota | Component | Aciklama |
|------|-----------|----------|
| `/login` | `Login` | Tam sayfa, layout yok |
| `/` | `Dashboard` | 7 ekipman karti + fabrika tanitim |
| `/equipment/:equipmentType` | `EquipmentAnalysis` | Tek ekipman analiz sayfasi |
| `/factory` | `FactoryList` | Proje listesi |
| `/factory/new` | `FactoryWizard` | Proje olusturma sihirbazi |
| `/factory/:projectId` | `FactoryDashboard` | Fabrika analiz dashboard'u |
| `/reports` | `ReportsPlaceholder` | Raporlar (yakin zamanda) |
| `*` | Redirect → `/` | Tanimli olmayan rotalar |

### 5.2 Sayfalar (6 dosya, 1,453 satir)

| Sayfa | Satir | Aciklama |
|-------|-------|----------|
| Dashboard.jsx | 133 | 7 ekipman karti, fabrika tanitim karti, sayfa secimi |
| EquipmentAnalysis.jsx | 247 | Progressive disclosure, HeroScoreBanner, 4 sekme, FloatingChat FAB |
| FactoryList.jsx | 126 | Proje listesi, sektor rozeti, ekipman sayisi |
| FactoryWizard.jsx | 274 | 2 adimli sihirbaz (proje bilgileri → ekipman ekleme) |
| FactoryDashboard.jsx | 539 | Fabrika analiz merkezi, 9-tab sistemi, 15 useState |
| Login.jsx | 134 | Giris/kayit gecisi, JWT token localStorage kaydi |

### 5.3 Component Agaci (67 dosya, 5,806 satir)

```
components/ (67 dosya, 5,806 satir)
|
|-- common/               (5 dosya, 183 satir)
|   |-- AIActionBar.jsx   # AI butonu + yorumlama tetikleyici (95 satir)
|   |-- Button.jsx         # Genel buton (kullanilmiyor)
|   |-- Card.jsx           # Kart wrapper
|   |-- Loading.jsx        # Yukleme gostergesi
|   |-- Tooltip.jsx        # Bilgi ipucu
|
|-- layout/               (4 dosya, 211 satir)
|   |-- Layout.jsx         # Ana sarmalayici (sidebar + icerik)
|   |-- Header.jsx         # Kullanici bilgisi, cikis butonu (70 satir)
|   |-- Sidebar.jsx        # Katlanabilir gruplar, NavLink (114 satir)
|   |-- Footer.jsx         # Alt bilgi
|
|-- forms/                (3 dosya, 181 satir)
|   |-- ParameterForm.jsx  # 2 sutunlu alan gridi (43 satir)
|   |-- FormField.jsx      # Dinamik alan render: input/select/checkbox (99 satir)
|   |-- CompressorTypeSelector.jsx  # Legacy kompresor tipi butonlari
|
|-- equipment/            (1 dosya, 30 satir)
|   |-- SubtypeSelector.jsx  # Genel alt tip secici
|
|-- dashboard/            (9 dosya, 668 satir)
|   |-- DashboardLayout.jsx     # Analiz oncesi/sonrasi layout degistirici (23 satir)
|   |-- TabContainer.jsx        # Sekme navigasyonu (hidden class, state koruma) (40 satir)
|   |-- OverviewTab.jsx         # AIInsightCard + DestructionBreakdown + ExergoeconomicSummary + DetailedMetrics + RadarBenchmark (62 satir)
|   |-- FlowTab.jsx             # Sankey diyagrami (36 satir)
|   |-- AITab.jsx               # Accordion: ozet → bulgular → oneriler → aksiyon plani (198 satir)
|   |-- ScenarioTab.jsx         # What-if senaryo editoru + karsilastirma (75 satir)
|   |-- ParameterSidebar.jsx    # Sol kenar cubugu (80 satir)
|   |-- HeroScoreBanner.jsx     # GaugeChart SVG + grade letter + 3 KPI (93 satir)
|   |-- GaugeChart.jsx          # SVG yarim daire gosterge (61 satir)
|
|-- results/              (11 dosya, 973 satir)
|   |-- ResultsPanel.jsx       # Sonuc konteyner (187 satir)
|   |-- AIInsightCard.jsx      # AI ozet karti, performans rozeti (54 satir)
|   |-- ActionTimeline.jsx     # Zaman cizgili aksiyon plani (59 satir)
|   |-- DestructionBreakdown.jsx  # Exergy yikim dagilimi cubuk grafigi (83 satir)
|   |-- DetailedMetrics.jsx    # Genisletilmis metrik gridi (113 satir)
|   |-- ExergoeconomicSummary.jsx  # f-faktor, r-faktor, Z_dot, C_dot ozeti (77 satir)
|   |-- RecommendationCard.jsx # Oneri karti (oncelik rozeti, maliyet) (91 satir)
|   |-- RadarBenchmark.jsx     # 6 eksenli Plotly polar/radar grafigi (122 satir)
|   |-- SankeyDiagram.jsx      # Plotly sankey (70 satir)
|   |-- BenchmarkChart.jsx     # Benchmark cubuk grafigi (52 satir)
|   |-- SolutionsList.jsx      # Oneri listesi (65 satir)
|
|-- factory/              (11 dosya, 1,210 satir)
|   |-- FactoryHeader.jsx          # Proje adi, sektor rozeti (67 satir)
|   |-- FactoryMetricBar.jsx       # Koyu hero stil metrik cubugu (69 satir)
|   |-- EquipmentInventory.jsx     # Ekipman tablosu (tip, durum, silme) (81 satir)
|   |-- AddEquipmentModal.jsx      # 3 adimli modal (tip → alt tip → param) (252 satir)
|   |-- PriorityList.jsx           # Oncelik sirali hotspot listesi (138 satir)
|   |-- HotspotList.jsx            # Basitlesmis hotspot gorunumu (76 satir)
|   |-- IntegrationPanel.jsx       # Capraz ekipman firsatlari (83 satir)
|   |-- IntegrationOpportunities.jsx  # Entegrasyon detaylari (79 satir)
|   |-- FactoryAIPanel.jsx         # Fabrika AI yorumlama butonu (140 satir)
|   |-- FactoryAIInterpretation.jsx   # Fabrika AI gorunumu (172 satir)
|   |-- FactorySankey.jsx          # Fabrika seviyesi Sankey (53 satir)
|
|-- pinch/                (6 dosya, 399 satir)
|   |-- PinchTab.jsx              # Pinch analiz sonuclari (101 satir)
|   |-- CompositeCurveChart.jsx   # Hot/cold composite curves (Plotly) (53 satir)
|   |-- GrandCompositeCurveChart.jsx  # GCC gorsellestirme (Plotly) (62 satir)
|   |-- StreamTable.jsx           # Sicak/soguk akis tablosu (71 satir)
|   |-- HENMatches.jsx            # Isi esanjor agi eslestirmeleri (58 satir)
|   |-- PinchMetricBar.jsx        # Pinch metrik cubugu (54 satir)
|
|-- advanced-exergy/      (5 dosya, 338 satir)
|   |-- AdvancedExergyTab.jsx      # AV/UN sonuclari + etkilesim agi (85 satir)
|   |-- QuadrantChart.jsx          # AV vs UN scatter (Plotly) (68 satir)
|   |-- InteractionNetwork.jsx     # Ekipman etkilesim grafigi (44 satir)
|   |-- AdvancedExergyMetricBar.jsx  # Ileri exergy metrik cubugu (63 satir)
|   |-- AdvancedExergyPriorityList.jsx  # Oncelik listesi (78 satir)
|
|-- entropy-generation/   (5 dosya, 371 satir)
|   |-- EntropyGenerationTab.jsx   # EGM sonuc gorunumu (85 satir)
|   |-- BejanNumberChart.jsx       # Bejan N_s scatter (Plotly) (60 satir)
|   |-- EntropyDecompositionChart.jsx  # Irreversibility dagilimi (Plotly) (75 satir)
|   |-- EGMMetricBar.jsx           # EGM metrik cubugu (66 satir)
|   |-- IrreversibilityRanking.jsx  # Tersinmezlik siralamasi (85 satir)
|
|-- thermoeconomic/       (1 dosya, 285 satir)
|   |-- ThermoeconomicTab.jsx      # SPECO degerlendirme + Tsatsaronis matrisi
|
|-- energy-management/    (1 dosya, 301 satir)
|   |-- EnergyManagementTab.jsx    # ISO 50001 olgunluk + aksiyon planlari
|
|-- whatif/               (3 dosya, 320 satir)
|   |-- ScenarioEditor.jsx         # Baseline/senaryo parametre editoru (102 satir)
|   |-- ComparisonPanel.jsx        # Delta karsilastirma (yesil/kirmizi) (134 satir)
|   |-- RadarComparison.jsx        # Iki katmanli radar grafigi (84 satir)
|
|-- chat/                 (2 dosya, 336 satir)
    |-- ChatPanel.jsx              # Tam sohbet: markdown render, oneri butonlari (281 satir)
    |-- FloatingChat.jsx           # FAB buton (sag alt, violet, z-50) + ChatPanel acilir panel (55 satir)
```

### 5.4 Servisler, Hooks, Utils

#### services/ (293 satir, 2 dosya)

**api.js (232 satir):**
- Axios instance: `baseURL: '/api'`, otomatik JWT token ekleme
- Ekipman: `getEquipmentConfig()`, `analyzeEquipment()`, `getEquipmentTypes()`
- AI: `interpretAnalysis()`, `compareScenarios()`, `chatWithAI()`
- Auth: `register()`, `login()`, `getMe()`, `logout()`
- Benchmark/Solutions: `getBenchmarks()`, `getSolutions()`

**factoryApi.js (61 satir):**
- `createFactoryProject()`, `getFactoryProjects()`, `getFactoryProject()`
- `addEquipmentToProject()`, `removeEquipmentFromProject()`
- `analyzeFactory()`, `interpretFactory()`

#### hooks/ (100 satir, 2 dosya)

**useAnalysis.js (75 satir):**
- 2 fazli analiz: Faz 1 (ana analiz + cozumler, engelleyici) → Faz 2 (AI yorumlama, arka plan)
- State: result, solutions, loading, error, interpretation, aiLoading

**useCompressorTypes.js (25 satir):**
- Equipment types fetch hook

#### utils/ (151 satir, 4 dosya)

- `formatters.js` (22 satir) -- Sayi/para birimi formatlama
- `priorityStyles.js` (17 satir) -- CSS sinif esleme (high/medium/low → Tailwind renkleri)
- `performanceColors.js` (24 satir) -- getPerformanceColor(), getPerformanceHex(), getGradeInfo()
- `turkishLabels.js` (88 satir) -- EQUIPMENT_TYPE_LABELS, SUBTYPE_LABELS, STRATEGY_LABELS, Turkce ceviri

### 5.5 Dashboard UX Mimarisi

#### 5.5.1 Ekipman Dashboard (EquipmentAnalysis.jsx)

Progressive disclosure pattern:
- **Analiz oncesi:** SubtypeSelector → ParameterForm (tam genislik)
- **Analiz sonrasi:** HeroScoreBanner (GaugeChart SVG + grade letter + 3 KPI) + ParameterSidebar (sol) + 4 sekme (sag) + FloatingChat FAB

HeroScoreBanner: Yari daire SVG gosterge (`GaugeChart.jsx`), harf notu (A-F), performans rengi, 3 KPI karti (exergy giris, exergy yikim, isi geri kazanim).

FloatingChat: Sag alt sabit FAB buton (violet, z-50). Tiklandiginda ChatPanel acilir (slide-up animasyon). Tum sekmelerde erisebilir.

4 sekme yapisi:
1. **Genel Bakis (OverviewTab):** AIInsightCard + DestructionBreakdown + ExergoeconomicSummary + DetailedMetrics + RadarBenchmark
2. **Akis (FlowTab):** SankeyDiagram (Plotly)
3. **AI (AITab):** Accordion yapisi (ozet → bulgular → oneriler → onerilmeyenler → aksiyon plani) + RecommendationCard + ActionTimeline
4. **Senaryo (ScenarioTab):** ScenarioEditor + ComparisonPanel + RadarComparison

TabContainer: `hidden` class ile state koruma (sekme gecisinde veri kaybi yok)

#### 5.5.2 Fabrika Dashboard (FactoryDashboard.jsx)

9-tab sistemi (scroll-to-section mimarisinden gecis):
- **TABS dizisi:** ai, priorities, sankey, pinch, advanced, egm, thermo, energy, inventory
- **Tab cubugu:** lucide ikonlari + durum noktasi (yesil = veri var, nokta yok = henuz calistirilmamis)
- **Her tab conditional render** (hidden class degil, dogrudan render)

FactoryMetricBar: Koyu hero stil (dark gradient + beyaz metin + KPI kartlari)

3 render modu (hala gecerli):
- **Bos:** Ekipman yok → "Ekipman Ekle" yonlendirmesi
- **Ekipmanli:** Analiz yok → "Analiz Calistir" butonu
- **Tam Dashboard:** Tab sistemi ile icerik gosterimi

Tab icerikleri:
1. **AI Yorum** -- FactoryAIPanel + FactoryAIInterpretation
2. **Oncelikler** -- PriorityList (hotspot sirali) + IntegrationPanel
3. **Sankey** -- FactorySankey (fabrika seviyesi)
4. **Pinch** -- PinchTab (Linnhoff analizi)
5. **Ileri Exergy** -- AdvancedExergyTab (EN/EX 4-quadrant)
6. **EGM** -- EntropyGenerationTab (Bejan sayisi)
7. **Termoekonomik** -- ThermoeconomicTab (f/r matrisi)
8. **Enerji Yonetimi** -- EnergyManagementTab (ISO 50001)
9. **Envanter** -- EquipmentInventory + AddEquipmentModal

#### 5.5.3 AI Paneli Detaylari

3 katmanli AI sistemi:
1. **Ekipman AI (AIInsightCard + AITab):** Tek ekipman yorumu -- AIInsightCard (ozet + performans rozeti), AITab accordion (bulgular → oneriler → onerilmeyenler → aksiyon plani), RecommendationCard, ActionTimeline
2. **Fabrika AI (FactoryAIPanel + FactoryAIInterpretation):** Fabrika seviyesi yorum -- hotspot analizi, entegrasyon firsatlari, onceliklendirme
3. **Sohbet (FloatingChat + ChatPanel):** FAB butonu ile erisilen Q&A -- markdown render, mavi/beyaz mesaj balonlari, bilgi kaynagi rozetleri, oneri butonlari, DOMPurify ile XSS koruma

### 5.6 Stil Sistemi

**Tailwind yapilandirmasi (tailwind.config.js):**

Renk paleti:
- primary: `#3b82f6` (blue-500 → blue-700 arasi)
- success: `#10b981` (green)
- warning: `#f59e0b` (amber)
- danger: `#ef4444` (red)

**Dinamik performans renklendirmesi (performanceColors.js):**
- emerald (>=80%), blue (>=60%), amber (>=40%), red (<40%)
- Grade harf sistemi: A (Mukemmel), B (Iyi), C (Orta), D (Zayif), F (Kritik)

**Kart ve tipografi stilleri:**
- Kart: rounded-xl, p-5/p-6, hover:shadow-md transition-shadow
- Tipografi: tabular-nums metriklerde, font-mono sayilarda

Font: sistem varsayilani (sans-serif)

**Plotly temalamasi:** Her grafik icin ozel Plotly layout (arka plan: seffaf, yazi: Tailwind renklerine uyumlu)

---

## 6. Test Altyapisi

18 dosya (17 test modulu + conftest + __init__), **671 test fonksiyonu**, toplam **6,936 satir**.

### 6.1 Test Dosyalari

| Dosya | Test Sayisi | Satir | Kapsam |
|-------|------------|-------|--------|
| test_pinch.py | 36 | 700 | Akis cikarimi, cascade, composite curves, HEN, fizibilite |
| test_energy_management.py | 49 | 689 | EnPI, olgunluk, aksiyon plani, 7 ISO boyutu |
| test_advanced_exergy.py | 36 | 618 | EN/EX ayrisim, 4-quadrant, etkilesim agi |
| test_api.py | 47 | 599 | API endpointleri, fabrika CRUD, analiz dispatch |
| test_engine.py | 45 | 552 | 7 ekipman motoru, exergy dengesi, verimlilik |
| test_entropy_generation.py | 38 | 546 | Gouy-Stodola, Bejan sayisi, dekompozisyon |
| test_exergoeconomic.py | 34 | 505 | SPECO, f-faktor, r-faktor, maliyet korelasyonu |
| test_thermoeconomic_optimization.py | 39 | 491 | Strateji belirleme, yatirim tahmini, geri odeme |
| test_skills.py | 50 | 453 | AI beceri dosyalari, knowledge dogrulama |
| test_avoidable_unavoidable.py | 22 | 376 | AV/UN ayrisimi, invariantler |
| test_compare.py | 12 | 232 | What-if delta hesaplama |
| test_radar.py | 27 | 200 | 6 eksenli benchmark puanlama |
| test_heat_exchanger.py | 21 | 200 | Bejan sayisi, LMTD, fouling, etkinlik |
| test_dryer.py | 24 | 196 | SMER, isi kaynaklari, termal verim |
| test_steam_turbine.py | 19 | 178 | CHP modu, izentropik verim, PRV ikamesi |
| test_equipment_registry.py | 18 | 170 | 7 tip, 46 alt tip dogrulama |
| test_knowledge_router.py | 18 | 159 | Bilgi yonlendirme, sohbet |
| conftest.py | - | 72 | DB fixture + TestClient |
| __init__.py | - | 0 | Paket tanimlama |

### 6.2 Toplamlar

| Metrik | Deger |
|--------|-------|
| Test dosyasi | 17 (+ conftest + __init__) |
| Test fonksiyonu | 671 |
| Toplam satir | 6,936 |
| Veritabani | Her test icin bellekte SQLite (izole) |
| API test | FastAPI TestClient + dependency override |
| Parametrik | pytest.parametrize (ekipman tipleri x invariantler) |

---

## 7. Knowledge Base

### 7.1 Dizin Yapisi (305 dosya)

| Dizin | Dosya Sayisi | Icerik |
|-------|-------------|--------|
| compressor/ | 19 | Benchmark, formuller, cozumler, alt tip detaylari |
| boiler/ | 23 | Yakit exergy faktorleri, baca gazi analizi, yogusma |
| chiller/ | 25 | COP, absorption, serbest sogutma, termal depolama |
| pump/ | 23 | Hidrolik guc, VSD, kavitasyon, sistem egrisi |
| heat_exchanger/ | 21 | U-deger, LMTD, NTU, fouling, etkinlik |
| steam_turbine/ | 23 | Izentropik verim, CHP, PRV ikamesi, ORC |
| dryer/ | 26 | SMER, SEC, psikrometri, tip secimi |
| **factory/** | **144** | 6 ileri analiz yontemi + kok dosyalar |

**Fabrika alt dizinleri:**

| Alt Dizin | Dosya | Yontem | Uygulama Kosulu |
|-----------|-------|--------|-----------------|
| pinch/ | 18 | Linnhoff Pinch Analizi | 1+ sicak/soguk akis, Q > 50 kW |
| advanced_exergy/ | 18 | AV/UN + EN/EX dekompozisyon | 3+ ekipman, I_total > 100 kW |
| exergoeconomic/ | 18 | SPECO, C_D, f_k/r_k | f_k < 0.25 veya f_k > 0.65 |
| thermoeconomic_optimization/ | 16 | Parametrik/yapisal opt. | C_D > 50,000 EUR/yil |
| entropy_generation/ | 19 | Bejan sayisi, Gouy-Stodola | N_s > 0.5 |
| energy_management/ | 21 | ISO 50001, enerji denetimi | Sistematik yonetim ihtiyaci |
| (kok dosyalar) | ~34 | cross_equipment, sector_*, prioritization, benchmarks | -- |

Her knowledge dosyasinda:
- YAML frontmatter (skill_id, versiyon, ekipman)
- Turkce basliklar, teknik terimler Ingilizce parantez icinde
- Tablolar, formuller, pratik ornekler
- "Ilgili Dosyalar" ve "Referanslar" bolumleri

### 7.2 Skill Dosyalari (17 dosya)

```
skills/
|-- core/                          # Temel beceriler (3 dosya)
|   |-- exergy_fundamentals.md     # Exergy kavramlari + EGM + exergoekonomik + pinch
|   |-- response_format.md         # JSON semalari (tek ekipman, fabrika, ileri analiz)
|   |-- decision_trees.md          # 7 ekipman + fabrika + ileri analiz karar agaclari
|
|-- equipment/                     # Ekipman uzmanlari (7 dosya)
|   |-- compressor_expert.md
|   |-- boiler_expert.md
|   |-- chiller_expert.md
|   |-- pump_expert.md
|   |-- heat_exchanger_expert.md
|   |-- steam_turbine_expert.md
|   |-- dryer_expert.md
|
|-- factory/                       # Fabrika analisti (3 dosya)
|   |-- factory_analyst.md         # Hotspot, capraz ekipman onerileri
|   |-- integration_expert.md      # HEN optimizasyonu, pinch eslestirme
|   |-- economic_advisor.md        # Exergoekonomik degerlendirme
|
|-- output/                        # Cikti formati (1 dosya)
|   |-- turkish_style.md           # Turkce cikti stili
|
|-- README.md                      # Skill sistemi aciklamasi
|-- SKILL_exergy_calculator.md     # Legacy skill
|-- SKILL_exergy_interpreter.md    # Legacy skill
```

---

## 8. Bagimliliklar

### 8.1 Python (requirements.txt -- 17 paket)

| Kategori | Paketler | Versiyon |
|----------|----------|---------|
| Web API | fastapi, uvicorn, python-multipart | >= 0.109.0, >= 0.27.0, >= 0.0.6 |
| Veri Modelleri | pydantic | >= 2.0.0 |
| Termodinamik | CoolProp | >= 6.4.0 |
| Veri Isleme | numpy, pandas | >= 1.21.0, >= 1.3.0 |
| Gorsellestirme | plotly, matplotlib | >= 5.0.0, >= 3.4.0 |
| Raporlama | reportlab, python-docx | >= 3.6.0, >= 0.8.11 |
| Veritabani | sqlalchemy, aiosqlite | >= 2.0.0, >= 0.19.0 |
| Auth | python-jose[cryptography], passlib[bcrypt] | >= 3.3.0, >= 1.7.4 |
| Yapilandirma | python-dotenv | >= 0.19.0 |
| Test | pytest, httpx | >= 7.0.0, >= 0.26.0 |

### 8.2 Frontend (package.json)

**Calisma Zamani (8 paket):**

| Paket | Versiyon | Amac |
|-------|---------|------|
| react | ^19.2.0 | UI framework |
| react-dom | ^19.2.0 | DOM rendering |
| react-router-dom | ^7.13.0 | Client-side routing |
| axios | ^1.13.4 | HTTP istemcisi |
| dompurify | ^3.3.1 | XSS koruma (HTML sanitize) |
| lucide-react | ^0.563.0 | Ikon kutuphanesi |
| plotly.js | ^3.3.1 | Grafik kutuphanesi (Sankey, Radar, Scatter) |
| react-plotly.js | ^2.6.0 | Plotly React sarmalayicisi |

**Gelistirme (8 paket):**

| Paket | Versiyon | Amac |
|-------|---------|------|
| vite | ^7.2.4 | Build araci |
| @vitejs/plugin-react | ^5.1.1 | Vite React eklentisi |
| tailwindcss | ^3.4.19 | Utility CSS framework |
| postcss | ^8.5.6 | CSS donusumu |
| autoprefixer | ^10.4.24 | CSS vendor onekleri |
| eslint | ^9.39.1 | Kod kalite kontrolu |
| eslint-plugin-react-hooks | ^7.0.1 | Hooks kurallari |
| eslint-plugin-react-refresh | ^0.4.24 | HMR uyumluluk |

---

## 9. Konfigurasyon

### Ortam Degiskenleri

| Degisken | Varsayilan | Aciklama |
|----------|-----------|----------|
| `JWT_SECRET_KEY` | `exergylab-dev-secret-key-change-in-production` | JWT imzalama anahtari |
| `DATABASE_URL` | `sqlite+aiosqlite:///./exergylab.db` | Veritabani baglanti dizesi |
| `JWT_ALGORITHM` | `HS256` | JWT algoritma |
| `JWT_EXPIRE_MINUTES` | `10080` (7 gun) | Token gecerlilik suresi |

### CORS Yapilandirmasi (api/main.py)

```
Izin Verilen Kaynaklar: http://localhost:5173, http://localhost:3000
Credentials: True
Metotlar: * (tumu)
Basliklar: * (tumu)
```

### Vite Proxy (frontend/vite.config.js)

```
/api/* → http://localhost:8000 (FastAPI backend)
changeOrigin: true
```

### Veritabani

- Tip: SQLite (async, aiosqlite)
- Dosya: `./exergylab.db` (proje kokunde)
- ORM: SQLAlchemy 2.0 (async session)
- Lifespan: Uygulama baslangicinda `init_db()`, kapanista `close_db()`

---

## 10. Bilinen Kisitlamalar ve Teknik Borc

### Teknik Kisitlamalar

| Kisitlama | Detay |
|-----------|-------|
| SQLite tek yazici | Eszamanli yazma islemi desteklemez; uretimde PostgreSQL gecisi gerekebilir |
| CoolProp bagimliligi | Buhar/su ozellikleri icin gerekli; kurulumu zor olabilir; fallback yaklasimsiz hesaplama mevcut |
| AI yanit suresi | Claude subprocess 10-30 saniye; frontend'de non-blocking ama kullanici beklemeli |
| Radar benchmark | Sadece kompresor sektoru icin detayli benchmark; diger 6 ekipmanda genel |
| Plotly bundle boyutu | plotly.js ~3.3 MB minified; lazy loading uygulanmamis |

### Teknik Borc

| Sorun | Dosya | Detay |
|-------|-------|-------|
| MetricBar tekrari | factory/FactoryMetricBar, pinch/PinchMetricBar, advanced-exergy/AdvancedExergyMetricBar, entropy-generation/EGMMetricBar | dashboard/MetricBar → HeroScoreBanner'a donusturuldu; 4 MetricBar varyanti kaldi |
| Button.jsx kullanilmiyor | common/Button.jsx (38 satir) | Hicbir dosyada import edilmiyor |
| FactoryDashboard useState yiginmasi | pages/FactoryDashboard.jsx | 15 useState hook'u (17'den dusuruldu); tab sistemi karmasikligi azaltti ama Zustand hala faydali olabilir |
| Lazy loading yok | frontend/vite.config.js | Tum componentler eagerly yukleniyor; code splitting uygulanmamis |
| Plotly font tutarsizligi | Plotly grafikleri | Plotly kendi font'unu kullaniyor, Tailwind sistem font'u ile uyumsuz |
| Erisebilirlik (a11y) | Genel | ARIA etiketleri, klavye navigasyonu, renk kontrasti kontrolu eksik |
| Toplu ekipman ekleme | FactoryWizard | Her ekipman tek tek ekleniyor; toplu ekleme (batch) destegi yok |

---

## 11. Gelistirme Gecmisi

Son 20 commit (en yeniden en eskiye):

| Commit | Aciklama |
|--------|----------|
| 32980c8 | Factory dashboard redesign: scroll-to-section → gercek tab sistemi, Turkce diacritic, koyu hero metrik cubugu |
| c32fde2 | Equipment analysis UI polish: Turkce diacritic, Sankey/radar fix, FloatingChat gorunurluk, senaryo temizlik |
| e566b8c | Equipment analysis page redesign: progressive disclosure, floating chat, accordion UI |
| 2201c28 | PROJECT_ANALYSIS.md guncelleme: 6 ileri motor, 671 test, UX overhaul yansitmasi |
| a43cab7 | Post-UX/UI polish: yumusak katlanabilir animasyon, fabrika chat backend fix, Turkce diacritic |
| 0193b8b | Frontend UX/UI overhaul: AI panel one cikma, bolum nav, katlanabilir analizler, XSS fix |
| 12ca183 | ISO 50001 enerji yonetimi: EnPI metrikleri, olgunluk puanlama, aksiyon plani motoru |
| 8df0df9 | Termoekonomik optimizasyon: Tsatsaronis f/r karar matrisi motoru |
| 2c35400 | Entropi uretim minimizasyonu (EGM): Bejan N_s analiz motoru |
| 91bffd7 | Ileri exergy analizi: Tsatsaronis EN/EX 4-quadrant dekompozisyon motoru |
| dd1a1c5 | Fabrika AI prompt boyutu fix: ~95K → ~29K karakter on-kirpma |
| 2184b27 | Linnhoff pinch analizi: motor, testler, API, frontend, AI entegrasyonu |
| 0ae5d30 | Exergoekonomik analiz tamamlama: 7 ekipman tipi alt tip destekli maliyet korelasyonu |
| 1a9335a | PROJECT_ANALYSIS.md guncelleme: kapsamli 15-bolum kod analizi (v2) |
| ececa31 | "Argument list too long" hatasi fix: fabrika AI yorumlama |
| 72a905f | 4 ekipman motoruna exergoekonomik analiz ekleme (f-faktor, r-faktor, maliyet oranlari) |
| 6a6d5a8 | Opsiyonel JWT kimlik dogrulama + fabrika proje sahipligi |
| cc5bd2c | SQLite kalicilik katmani: bellek ici depolamayi degistirme |
| 3dfbbfc | Fabrika dashboard overhaul: uc modlu layout + 5 yeni bilesen |
| 3cecff3 | Ekipman analizi UI overhaul: iki modlu dashboard layout |
| 329bda6 | Sohbet takip fix: prompt gecmisi ve knowledge kirpma |
| cffa443 | Knowledge-destekli AI sohbet paneli (305 dosya knowledge yonlendirme) |

---

## 12. Sonraki Adimlar (Backlog)

### Kisa Vadeli (1-2 ay)

| Oneri | Oncelik | Etki |
|-------|---------|------|
| Tum ekipmanlara sektorel radar detayi | Yuksek | Benchmark kalitesi |
| MetricBar bilesenlerini ortaklastirma (dashboard/MetricBar → HeroScoreBanner tamamlandi; 4 varyant kaldi) | Orta | Teknik borc azaltma |
| Button.jsx kaldir veya kullan | Dusuk | Temizlik |
| Rate limiting (AI endpointleri) | Orta | Guvenlik |
| Analiz sonuclarini PDF/DOCX export | Orta | Kullanilabilirlik |

### Orta Vadeli (3-6 ay)

| Oneri | Oncelik | Etki |
|-------|---------|------|
| PostgreSQL gecisi | Orta | Olceklenebilirlik (coklu yazici) |
| Frontend lazy loading + code splitting | Yuksek | Performans (Plotly 3.3 MB) |
| State yonetimi (Zustand) | Orta | FactoryDashboard 17→15 useState, tab sistemi iyilestirdi ama hala faydali |
| Toplu ekipman ekleme (batch) | Orta | Kullanici deneyimi |
| Erisebilirlik (a11y) iyilestirmeleri | Orta | Uyumluluk |

### Uzun Vadeli (6-12 ay)

| Oneri | Oncelik | Etki |
|-------|---------|------|
| WebSocket ile gercek zamanli AI streaming | Orta | Kullanici deneyimi |
| Coklu kullanici + takim yonetimi | Orta | Kurumsal kullanim |
| Tarihsel veri analizi + trend izleme | Orta | Veri odakli karar |
| Uluslararasilastirma (i18n) | Dusuk | Pazar genisligi |
| Mobil uyumlu responsive tasarim | Dusuk | Erisim genisligi |

---

*Bu dokuman, ExergyLab kod tabaninin 2026-02-07 tarihli kapsamli analizidir (v3.1).*
*30,080 satir kod, 671 test, 305 knowledge dosyasi, 6 ileri analiz motoru.*
