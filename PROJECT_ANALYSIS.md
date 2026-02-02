# ExergyLab — Proje Analiz Raporu

> Otomatik uretim tarihi: 2026-02-02
> Analiz yontemi: Statik kod analizi + test yurutme + dizin taramasi

---

## 1. Proje Ozeti

**ExergyLab**, endustriyel tesislerdeki 7 ekipman tipinin ve fabrika genelinin exergy analizini yapan, 6 ileri analiz yontemi icin bilgi tabani sunan ve Claude AI destekli yorumlar ureten bir enerji verimliligi platformudur.

**Temel Odak:** Enerji verimi yerine **exergy verimi** — termodinamigin 2. yasasina dayali gercek verimlilik olcumu. Dusuk sicakliktaki isi, dusuk exergy'dir; bu platform bu farki olcer ve raporlar.

**Mevcut Durum:** 4/7 ekipman tipi icin hesaplama motoru hazir, 7/7 ekipman tipi icin AI bilgi tabani ve skill dosyalari mevcut, fabrika seviyesi aggregation ve cross-equipment entegrasyon tespiti calisiyor. 243 test %100 basarili.

### Teknoloji Yigini

| Katman | Teknoloji | Versiyon |
|--------|-----------|----------|
| Backend | Python, FastAPI, Pydantic | 3.10+, >=0.109, >=2.0 |
| Frontend | React, Vite, TailwindCSS | 19.2, Vite 6.x |
| AI | Claude Code CLI | - |
| Termodinamik | CoolProp | >=6.4.0 |
| Grafik | Plotly, Recharts (react-plotly.js) | >=5.0, 2.6 |
| Test | Pytest, httpx | >=7.0, >=0.26 |

---

## 2. Proje Istatistikleri

| Metrik | Deger |
|--------|-------|
| Toplam Python satiri | 6,976 |
| Toplam JSX satiri | 2,676 |
| Toplam JS satiri (hooks + services) | 282 |
| Toplam Knowledge Base satiri | ~141,233 |
| Toplam Skill satiri | 3,146 |
| Knowledge dosya sayisi | 305 |
| Skill dosya sayisi | 17 |
| Engine modulleri | 10 (.py dosyasi, `__init__` dahil) |
| API dosyalari | 11 (.py) |
| Frontend component/sayfa | 31 JSX dosyasi |
| Test dosyalari | 6 (conftest + 4 test modulu + `__init__`) |
| Test metodu sayisi | 243 |
| Test basari orani | %100 (243/243 passed, 1.73s) |
| Git commit sayisi | 21 |
| Git branch | master (tekil) |
| TODO/FIXME sayisi | 0 |

---

## 3. Dizin Yapisi

```
exergy-lab/                          # Proje koku
├── CLAUDE.md                        # Proje talimatlari (Claude Code icin)
├── requirements.txt                 # Python bagimliliklari (14 paket)
│
├── api/                             # FastAPI backend (2,177 satir)
│   ├── __init__.py
│   ├── main.py                      # 49 sat. — App factory, router mount
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── analysis.py              # 500 sat. — /analyze, /types, /config
│   │   ├── benchmarks.py            # 93 sat.  — /benchmarks/{type}/{subtype}
│   │   ├── factory.py               # 214 sat. — /factory CRUD + /analyze
│   │   ├── interpret.py             # 62 sat.  — /interpret (AI)
│   │   └── solutions.py             # 85 sat.  — /solutions/{type}
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── factory.py               # 62 sat.  — FactoryProject, EquipmentItem
│   │   ├── requests.py              # 132 sat. — Pydantic request modelleri
│   │   └── responses.py             # 150 sat. — Pydantic response modelleri
│   └── services/
│       ├── __init__.py
│       ├── claude_code_service.py   # 654 sat. — AI entegrasyonu (singleton)
│       └── equipment_registry.py    # 173 sat. — 7 ekipman tip kaydi
│
├── engine/                          # Hesaplama motoru (3,023 satir)
│   ├── __init__.py                  # 26 sat.  — Public API export
│   ├── core.py                      # 119 sat. — DeadState, ExergyResult, yardimci
│   ├── utils.py                     # 113 sat. — Birim cevrim, validasyon, I/O
│   ├── compressor.py                # 529 sat. — 4 alt tip, 5 class, 17 fonk.
│   ├── boiler.py                    # 627 sat. — 7 alt tip, 2 class, 13 fonk.
│   ├── chiller.py                   # 466 sat. — Vapor comp. + absorption, 10 fonk.
│   ├── pump.py                      # 439 sat. — VSD analizi dahil, 10 fonk.
│   ├── factory.py                   # 592 sat. — Aggregation, hotspot, entegrasyon
│   └── sankey.py                    # 112 sat. — Sankey dispatcher (4 tip)
│
├── knowledge/                       # AI Bilgi Tabani (305 dosya, ~141K satir)
│   ├── INDEX.md                     # Master navigasyon haritasi
│   ├── compressor/                  # 19 dosya — 3,803 satir
│   ├── boiler/                      # 23 dosya — 7,760 satir
│   ├── chiller/                     # 25 dosya — 7,981 satir
│   ├── pump/                        # 23 dosya — 5,750 satir
│   ├── heat_exchanger/              # 21 dosya — 7,737 satir
│   ├── steam_turbine/               # 23 dosya — 10,071 satir
│   ├── dryer/                       # 26 dosya — 12,005 satir
│   └── factory/                     # 144 dosya — ~85,740 satir
│       ├── pinch/                   # 18 dosya
│       ├── advanced_exergy/         # 18 dosya
│       ├── exergoeconomic/          # 18 dosya
│       ├── thermoeconomic_opt./     # 16 dosya
│       ├── entropy_generation/      # 19 dosya
│       ├── energy_management/       # 21 dosya
│       └── (genel dosyalar)         # 34 dosya
│
├── skills/                          # AI Skill Dosyalari (17 dosya, 3,146 satir)
│   ├── README.md                    # 97 sat.
│   ├── SKILL_exergy_calculator.md   # 135 sat. (legacy)
│   ├── SKILL_exergy_interpreter.md  # 227 sat. (legacy)
│   ├── core/                        # 3 dosya — 738 satir
│   ├── equipment/                   # 7 dosya — 1,247 satir
│   ├── factory/                     # 3 dosya — 641 satir
│   └── output/                      # 1 dosya — 61 satir
│
├── frontend/                        # React frontend
│   ├── package.json                 # 7 runtime dependency
│   └── src/
│       ├── App.jsx                  # 34 sat. — Router tanimlamasi
│       ├── main.jsx                 # 10 sat. — Entry point
│       ├── pages/                   # 5 sayfa — 900 satir
│       │   ├── Dashboard.jsx        # 103 sat.
│       │   ├── EquipmentAnalysis.jsx# 139 sat.
│       │   ├── FactoryDashboard.jsx # 261 sat.
│       │   ├── FactoryList.jsx      # 126 sat.
│       │   └── FactoryWizard.jsx    # 271 sat.
│       ├── components/              # 24 component — 1,732 satir
│       │   ├── common/              # 4 (Button, Card, Loading, Tooltip)
│       │   ├── equipment/           # 1 (SubtypeSelector)
│       │   ├── factory/             # 6 (AddEquipmentModal, EquipmentInventory, ...)
│       │   ├── forms/               # 3 (CompressorTypeSelector, FormField, ParameterForm)
│       │   ├── layout/              # 4 (Footer, Header, Layout, Sidebar)
│       │   └── results/             # 6 (AIInterpretation, BenchmarkChart, ...)
│       ├── hooks/                   # 2 hook — 100 satir
│       │   ├── useAnalysis.js       # 75 sat.
│       │   └── useCompressorTypes.js# 25 sat.
│       └── services/                # 2 API client — 182 satir
│           ├── api.js               # 146 sat.
│           └── factoryApi.js        # 36 sat.
│
└── tests/                           # Pytest testleri (1,776 satir)
    ├── conftest.py                  # 7 sat. — TestClient fixture
    ├── test_api.py                  # 596 sat. — API entegrasyon testleri
    ├── test_engine.py               # 550 sat. — Engine birim testleri
    ├── test_equipment_registry.py   # 170 sat. — Registry testleri
    └── test_skills.py               # 453 sat. — Skill/knowledge testleri
```

---

## 4. Mimari Genel Bakis

### 4.1 Katmanli Mimari

```
┌─────────────────────────────────────────────────────┐
│  Frontend (React 19 + Vite)                         │
│  5 sayfa, 24 component, 2 hook, 2 API servisi       │
│  TailwindCSS + react-plotly.js + lucide-react       │
├─────────────────────────────────────────────────────┤
│  API Gateway (FastAPI)                              │
│  5 route modulu, Pydantic validasyon                │
│  Equipment Registry (7 tip, alt tipler)              │
├──────────────┬──────────────────────────────────────┤
│  Engine      │  AI Service                          │
│  core.py     │  claude_code_service.py              │
│  4 ekipman   │  Skill + Knowledge yukleyici         │
│  factory.py  │  Claude CLI subprocess               │
│  sankey.py   │  3-tier JSON parser                  │
├──────────────┴──────────────────────────────────────┤
│  Knowledge Base (305 dosya) + Skills (17 dosya)      │
│  7 ekipman + factory + 6 ileri analiz yontemi       │
└─────────────────────────────────────────────────────┘
```

### 4.2 Veri Akisi

1. **Kullanici** → Frontend formu doldurur (ekipman parametreleri)
2. **Frontend** → `POST /api/analyze` veya `POST /api/factory/{id}/analyze`
3. **API Routes** → Pydantic ile validasyon, engine dispatcher
4. **Engine** → Termodinamik hesaplama (exergy in/out/destroyed, verim, kayip)
5. **Sankey** → Exergy akis diyagrami verisi uretimi
6. **AI (opsiyonel)** → `POST /api/interpret` → Claude CLI subprocess
7. **Claude CLI** → Skills + Knowledge yuklenir, JSON yanit parse edilir
8. **Frontend** → Sonuclari gorsellestirir (metrik kartlari, Sankey, AI yorumu)

### 4.3 Fabrika Analiz Akisi

1. Frontend'den proje olusturulur (ad, sektor)
2. Ekipmanlar tek tek eklenir (tip, alt tip, parametreler)
3. `POST /api/factory/{id}/analyze` → `engine.factory.analyze_factory()`
4. Her ekipman icin ilgili engine calisir
5. Aggregate metrikler hesaplanir (toplam exergy in/out/destroyed)
6. Hotspot tespiti (verim + kayip orani + mutlak kayip)
7. Cross-equipment entegrasyon firsatlari (5 desen)
8. Fabrika Sankey diyagrami uretilir
9. Opsiyonel AI yorumu: `interpret_factory_analysis()`

---

## 5. Engine Detayli Analiz

### 5.1 core.py (119 satir)

Temel yapitaslari:

| Oge | Tip | Aciklama |
|-----|-----|----------|
| `DeadState` | dataclass | Referans cevre: T₀=298.15 K, P₀=101.325 kPa |
| `ExergyResult` | dataclass | Standart sonuc yapisi (in/out/destroyed/efficiency + yillik) |
| `heat_exergy()` | fonksiyon | Ex_Q = Q × (1 - T₀/T) — isitma ve sogutma durumu |
| `carnot_factor()` | fonksiyon | η_carnot = 1 - T_cold/T_hot |
| Birim ceviriciler | fonksiyonlar | celsius↔kelvin, bar↔kPa, m³/min→m³/s |
| `air_density()` | fonksiyon | Ideal gaz yasasi: ρ = P/(R×T) |

**Sabitler:** R_AIR = 0.287 kJ/kg·K, R_UNIVERSAL = 8.314 J/mol·K, CP_AIR = 1.005 kJ/kg·K

### 5.2 compressor.py (529 satir, 5 class, 17 fonksiyon)

**Desteklenen Alt Tipler:**

| Alt Tip | Input Class | Analiz Fonksiyonu | Ozel Ozellik |
|---------|-------------|-------------------|--------------|
| Vidali (screw) | `CompressorInput` | `analyze_compressor()` | Standart referans |
| Pistonlu | `PistonCompressorInput` | `analyze_piston_compressor()` | Kademe sayisi, sogutma tipi |
| Scroll | `ScrollCompressorInput` | `analyze_scroll_compressor()` | Yagsiz secenegi |
| Santrifuj | `CentrifugalCompressorInput` | `analyze_centrifugal_compressor()` | Surge/choke, guide vane |

**Hesaplama Akisi:**
1. Izentropik is hesabi: W_isen = (k/(k-1)) × P₁V₁ × [(P₂/P₁)^((k-1)/k) - 1]
2. Gercek guc ve spesifik guc
3. Exergy girisi = elektrik gucu
4. Exergy cikisi = basinc exergy'si
5. Exergy yikimi = giris - cikis
6. Isi geri kazanim potansiyeli (~%67.5 recoverable)
7. Benchmark karsilastirma (yuzdelik hesabi)
8. Yillik maliyet (kayip × calissma saati × fiyat)

**Benchmark Sistemi:** Alt tip bazli spesifik guc (kW/m³/min) karsilastirmasi. Good/average/poor/critical derecelendirme.

### 5.3 boiler.py (627 satir, 2 class, 13 fonksiyon)

**Desteklenen Alt Tipler:** steam_firetube, steam_watertube, hotwater, condensing, waste_heat, electric, biomass

**Hesaplama Akisi:**
1. Yakit exergy'si (yakit tipi bazli exergy/enerji oranlari)
2. Buhar/su exergy cikisi (CoolProp ile buhar ozellikleri veya ampirik formul)
3. Kayip ayristirma: baca gazi, radyasyon, blowdown, yanmamis yakit
4. Exergy yikimi = yakit exergy - cikis exergy - kayiplar
5. Sankey verisi uretimi (baca, radyasyon, blowdown, faydali)

**Ozel:** CoolProp entegrasyonu buhar/su ozelliklerini hassas hesaplar. Yakit tipleri icin exergy/enerji katsayilari tanimli (dogalgaz: 1.04, komur: 1.06, fuel_oil: 1.06, LPG: 1.06, biomass: 1.11, hydrogen: 0.985).

### 5.4 chiller.py (466 satir, 2 class, 10 fonksiyon)

**Desteklenen Alt Tipler:** Vapor compression (screw, centrifugal, scroll, reciprocating, air/water cooled) + Absorption

**Hesaplama Akisi:**
1. Sogutma exergy'si: Ex_cool = Q_cool × (T₀/T_cold - 1)
2. Elektrik/isi girdisi exergy'si
3. COP vs exergetic COP ayristirmasi
4. Absorption chiller: isi kaynagiyla calistirma, COP_th bazli
5. Kondenser kaybi, elektrik-exergy kaybi hesabi

**Ozel:** Absorption ve vapor compression icin ayri analiz yollari. Condenser heat = cooling + compressor power.

### 5.5 pump.py (439 satir, 2 class, 10 fonksiyon)

**Hesaplama Akisi:**
1. Hidrolik guc: P_hyd = ρ × g × Q × H
2. Motor → saft → pompa verim zinciri
3. Kisma kaybi analizi (throttle kontrolu icin)
4. VSD tasarruf potansiyeli (affinite yasalari)
5. Kavitasyon riski kontrolu (NPSH)

**Ozel:** Kontrol yontemi bazli analiz (throttle vs VSD vs on-off). `vsd_savings_potential_kW` ciktisi factory entegrasyon deseni icin kullanilir.

### 5.6 factory.py (592 satir, 14 fonksiyon)

**Ana Fonksiyon:** `analyze_factory(equipment_list)` → `FactoryAnalysisResult`

**Alt Moduller:**

| Modul | Fonksiyon | Satir Aralik | Aciklama |
|-------|-----------|-------------|----------|
| Dispatcher | `analyze_factory()` | 1-234 | Her ekipmani ilgili engine'e yonlendirir |
| Aggregates | `_calculate_aggregates()` | 237-267 | Toplam exergy in/out/destroyed |
| Hotspots | `_identify_hotspots()` | 270-322 | Priority: high/medium/low |
| Integration | `_detect_integration_opportunities()` | 325-491 | 5 cross-equipment deseni |
| Sankey | `_generate_factory_sankey()` | 494-592 | Fabrika seviyesi akis diyagrami |

**Hotspot Onceliklendirme Mantigi:**
- **high:** verim < %30 VEYA kayip > toplamın %40'ı VEYA mutlak kayip > 20 kW
- **medium:** verim < %50 VEYA kayip > toplamın %20'si VEYA mutlak kayip > 5 kW
- **low:** diger

**5 Cross-Equipment Entegrasyon Deseni:**

| # | Desen | Kaynak → Hedef | Karmasiklik |
|---|-------|----------------|-------------|
| 1 | Kompresor → Kazan besleme suyu | Atik isi (%67.5 recoverable × %60 HX) | medium |
| 2 | Kompresor → Mekan isitma | Atik isi (%50 kullanilabilir, 2000h sezon) | low |
| 3 | Kazan baca gazi → Absorpsiyonlu chiller | Baca gazi (%50 capture × COP 0.7) | high |
| 4 | Chiller kondenser → Sicak su | Kondenser (%30 kullanilabilir) | medium |
| 5 | Pompa VSD retrofit | Kisma → VSD gecisi | low |

### 5.7 sankey.py (112 satir, 2 fonksiyon)

Dispatcher yapisi: `generate_sankey_data(result)` → result tipine gore (isinstance) uygun fonksiyona yonlendirir.

- `CompressorResult` → `_generate_compressor_sankey_data()` (bu dosyada)
- `BoilerResult` → `generate_boiler_sankey_data()` (boiler.py'de)
- `ChillerResult` → `generate_chiller_sankey_data()` (chiller.py'de)
- `PumpResult` → `generate_pump_sankey_data()` (pump.py'de)

Kompressor Sankey'de enerji dengelemesi normalizasyonu yapilir: giris = cikis + recoverable + irreversibility.

### 5.8 utils.py (113 satir, 10 fonksiyon)

Yardimci araclar:
- Birim cevrim (`convert_pressure`, `convert_temperature`) — coklu birim destegi (kPa, bar, psi, atm, mbar)
- Validasyon (`validate_positive`, `validate_range`)
- Formatlama (`format_currency`, `format_percentage`, `format_power`)
- I/O (`save_analysis_result`, `load_analysis_result`) — JSON kaydedici/yukleyici

### 5.9 Pattern Tutarlilik Matrisi

| Ozellik | compressor | boiler | chiller | pump |
|---------|-----------|--------|---------|------|
| Input dataclass | ✅ | ✅ | ✅ | ✅ |
| Result dataclass | ✅ | ✅ | ✅ | ✅ |
| analyze_*() | ✅ | ✅ | ✅ | ✅ |
| get_*_recommendations() | ✅ | ✅ | ✅ | ✅ |
| to_api_dict() | ✅ | ✅ | ✅ | ✅ |
| Sankey verisi | ✅ | ✅ | ✅ | ✅ |
| Benchmark sistemi | ✅ | ✅ | ✅ | ✅ |
| Type hints | ✅ | ✅ | ✅ | ✅ |
| Docstrings | ✅ | ✅ | ✅ | ✅ |
| Yillik maliyet | ✅ | ✅ | ✅ | ✅ |

**Tutarlilik Notu:** 4 mevcut engine ayni dataclass → analyze → to_api_dict → sankey → recommendations kalibini takip eder. Bu kalibin heat_exchanger, steam_turbine ve dryer icin de tekrarlanmasi beklenir.

---

## 6. Knowledge Base Detayli Envanter

### 6.1 Genel Istatistikler

| Metrik | Deger |
|--------|-------|
| Toplam dosya | 305 |
| Toplam satir | ~141,233 |
| Ekipman bazli dosya | 160 (7 tip) |
| Fabrika bazli dosya | 144 |
| Master INDEX | 1 |
| Ortalama dosya uzunlugu | ~463 satir |

### 6.2 Ekipman Bazli Knowledge

| Ekipman | Dosya | Satir | Alt Dizinler |
|---------|-------|-------|-------------|
| compressor | 19 | 3,803 | equipment/ (7), solutions/ (8), INDEX, audit, benchmarks, formulas |
| boiler | 23 | 7,760 | equipment/ (9), solutions/ (10), INDEX, audit, benchmarks, formulas |
| chiller | 25 | 7,981 | equipment/ (11), solutions/ (10), INDEX, audit, benchmarks, formulas |
| pump | 23 | 5,750 | equipment/ (9), solutions/ (10), INDEX, audit, benchmarks, formulas |
| heat_exchanger | 21 | 7,737 | equipment/ (9), solutions/ (6), INDEX, audit, benchmarks, formulas, case_studies, standards |
| steam_turbine | 23 | 10,071 | equipment/ (5), solutions/ (5), systems/ (5), economics/ (3), INDEX, audit, benchmarks, formulas, case_studies |
| dryer | 26 | 12,005 | equipment/ (8), solutions/ (7), sectors/ (5), INDEX, audit, benchmarks, formulas, psychrometrics, case_studies |

**Her ekipman dizini standart olarak icerir:**
- `INDEX.md` — Navigasyon haritasi
- `benchmarks.md` — Verimlilik karsilastirma verileri
- `formulas.md` — Hesaplama formulleri
- `audit.md` — Denetim rehberi
- `equipment/` — Alt tip teknik detaylari
- `solutions/` — Iyilestirme onerileri

**Ek dizinler (bazi ekipmanlarda):**
- `sectors/` (dryer) — Sektor bazli kurutma (gida, tekstil, kagit, seramik, ahsap)
- `systems/` (steam_turbine) — CHP, HRSG, trigeneration
- `economics/` (steam_turbine) — Fizibilite, FiT, finansman
- `standards.md` (heat_exchanger) — TEMA, ASME standartlari

### 6.3 Fabrika Bazli Knowledge (144 dosya, ~85,740 satir)

#### 6.3.1 Ileri Analiz Yontemleri

| Yontem | Dizin | Dosya | Icerik |
|--------|-------|-------|--------|
| Pinch Analizi | `pinch/` | 18 | Composite curve, GCC, HEN tasarimi, delta-T min, targeting, retrofit, batch, total site |
| Ileri Exergy | `advanced_exergy/` | 18 | AV/UN, EN/EX, 4-way splitting, ideal conditions, equipment-specific (6 tip), limitations |
| Exergoekonomik | `exergoeconomic/` | 18 | SPECO, maliyet denklemleri, fuel-product, matris formulasyon, worked examples (3) |
| Termoekonomik Opt. | `thermoeconomic_optimization/` | 16 | Parametrik, yapisal, cok amacli, karar degiskenleri, trade-off, worked examples (3) |
| EGM | `entropy_generation/` | 19 | Bejan sayisi, constructal, sonlu zaman, akis/isi transfer/pipe EGM, worked examples (3) |
| Enerji Yonetimi | `energy_management/` | 21 | ISO 50001, EN 16247, IPMVP, EnPI, CUSUM, M&V, Turkiye mevzuati/tesvik |

#### 6.3.2 Genel Fabrika Dosyalari (34 dosya)

Sektor dosyalari: `sector_food.md`, `sector_cement.md`, `sector_chemical.md`, `sector_textile.md`, `sector_paper.md`, `sector_metal.md`, `sector_automotive.md` (7 sektor)

Diger: `cross_equipment.md`, `prioritization.md`, `factory_benchmarks.md`, `methodology.md`, `data_collection.md`, `system_boundaries.md`, `exergy_fundamentals.md`, `exergy_flow_analysis.md`, `energy_flow_analysis.md`, `mass_balance.md`, `heat_integration.md`, `process_integration.md`, `cogeneration.md`, `waste_heat_recovery.md`, `economic_analysis.md`, `energy_pricing.md`, `life_cycle_cost.md`, `kpi_definitions.md`, `performance_indicators.md`, `measurement_verification.md`, `implementation.md`, `reporting.md`, `case_studies.md`, `utility_analysis.md`, `energy_management.md` (kok dosya), `pinch_analysis.md` (kok dosya)

### 6.4 Frontmatter Kontrolu

Test sonuclarina gore:
- 7/7 ekipman `benchmarks.md` dosyasinda frontmatter ✅
- 7/7 ekipman `formulas.md` dosyasinda frontmatter ✅
- 7/7 ekipman `INDEX.md` dosyasi mevcut ✅
- `factory/cross_equipment.md` frontmatter ✅
- `factory/INDEX.md` mevcut ✅

---

## 7. Skills Sistemi

### 7.1 Dosya Listesi

| Dosya | Satir | Kategori | Aciklama |
|-------|-------|----------|----------|
| `core/exergy_fundamentals.md` | 198 | Core | Exergy kavramlari, EGM, exergoekonomik, pinch |
| `core/response_format.md` | 170 | Core | JSON semalari (tek ekipman, fabrika, ileri) |
| `core/decision_trees.md` | 370 | Core | 7 ekipman + fabrika + ileri analiz karar agaclari |
| `equipment/compressor_expert.md` | 162 | Equipment | Kompresor uzmani |
| `equipment/boiler_expert.md` | 166 | Equipment | Kazan uzmani |
| `equipment/chiller_expert.md` | 152 | Equipment | Chiller uzmani |
| `equipment/pump_expert.md` | 169 | Equipment | Pompa uzmani |
| `equipment/heat_exchanger_expert.md` | 265 | Equipment | Isi esanjoru uzmani |
| `equipment/steam_turbine_expert.md` | 187 | Equipment | Buhar turbini uzmani |
| `equipment/dryer_expert.md` | 146 | Equipment | Kurutma firini uzmani |
| `factory/factory_analyst.md` | 310 | Factory | Hotspot, cross-equipment, ileri analiz |
| `factory/integration_expert.md` | 179 | Factory | HEN optimizasyonu, pinch eslestime |
| `factory/economic_advisor.md` | 152 | Factory | Exergoekonomik degerlendirme |
| `output/turkish_style.md` | 61 | Output | Turkce yazi stili kurallari |
| `SKILL_exergy_interpreter.md` | 227 | Legacy | Geriye uyumlu tek dosya skill |
| `SKILL_exergy_calculator.md` | 135 | Legacy | Hesaplama skill'i |
| `README.md` | 97 | Meta | Skill sistemi dokumanasyonu |

### 7.2 Skill Yukleme Sirasi

`claude_code_service.py` icerisinde `_load_skills()` metodu:

**Tek Ekipman Analizi:**
1. `core/exergy_fundamentals.md` (her zaman)
2. `core/response_format.md` (her zaman)
3. `core/decision_trees.md` (her zaman)
4. `equipment/{type}_expert.md` (ekipman tipine gore)
5. `output/turkish_style.md` (her zaman)

**Fabrika Analizi:**
1. Core skills (3 dosya — her zaman)
2. `factory/factory_analyst.md`
3. `factory/integration_expert.md`
4. `factory/economic_advisor.md`
5. `output/turkish_style.md` (her zaman)

**Fallback:** Moduler skill'ler bos ise legacy `SKILL_exergy_interpreter.md` kullanilir.

---

## 8. AI Servis Katmani

### 8.1 claude_code_service.py Mimarisi (654 satir)

| Sinif/Fonksiyon | Satir | Aciklama |
|-----------------|-------|----------|
| `EQUIPMENT_LABELS` | 12-21 | 7 ekipman Turkce etiketleri |
| `EQUIPMENT_PARAMS_TEMPLATE` | 23-81 | 7 ekipman parametre sablonu |
| `EQUIPMENT_CATEGORIES` | 83-91 | Ekipman bazli cozum kategorileri |
| `_SafeDict` | 94-98 | Eksik key'ler icin 'N/A' donduren dict |
| `_read_file_cached()` | 101-111 | LRU cache ile dosya okuma (maxsize=100) |
| `ClaudeCodeClient` | 114-462 | Singleton AI client |
| `ClaudeCodeClient._load_skills()` | 151-198 | Moduler skill yukleyici |
| `ClaudeCodeClient._load_relevant_knowledge()` | 209-247 | Context-aware knowledge yukleyici |
| `ClaudeCodeClient._build_prompt()` | 249-362 | Tek ekipman icin prompt builder |
| `ClaudeCodeClient._extract_json()` | 364-389 | 3-tier JSON parser |
| `ClaudeCodeClient.interpret()` | 405-462 | Claude CLI subprocess cagirici |
| `interpret_with_claude_code()` | 465-476 | Module-level wrapper (geriye uyumluluk) |
| `_format_factory_analysis()` | 479-500 | Fabrika verisi formatlayici |
| `interpret_factory_analysis()` | 516-654 | Fabrika AI yorumlayici |

### 8.2 AI Yorum Akisi

```
Kullanici Istegi
    ↓
API Route (interpret.py)
    ↓
ClaudeCodeClient.get_instance() ← Singleton
    ↓
_load_skills(type) ← Core + Equipment/Factory + Output
    ↓
_load_relevant_knowledge(type) ← Benchmarks + Formulas (+ Factory files)
    ↓
_build_prompt() ← Skills + Knowledge + Analysis Data → Tek string
    ↓
asyncio.create_subprocess_exec("claude", "-p", prompt)
    ↓ 120s timeout
_extract_json(stdout) ← 3-tier parser
    ↓
Tier 1: json.loads(raw)        → Basarili? Dondur.
Tier 2: regex ```json...```    → Basarili? Dondur.
Tier 3: regex {.*}             → Basarili? Dondur.
    ↓ (hepsi basarisiz)
_fallback_response() ← ai_available: false
```

### 8.3 Knowledge Yukleme Stratejisi

**Tek Ekipman:**
- `knowledge/{type}/benchmarks.md`
- `knowledge/{type}/formulas.md`

**Fabrika:**
- `knowledge/factory/cross_equipment.md`
- `knowledge/factory/prioritization.md`
- `knowledge/factory/factory_benchmarks.md`
- `knowledge/factory/exergoeconomic/evaluation_criteria.md`
- `knowledge/factory/advanced_exergy/overview.md`
- `knowledge/factory/pinch/fundamentals.md`
- `knowledge/factory/entropy_generation/overview.md`
- `knowledge/factory/sector_{sector}.md` (sektor belirtilmisse)

---

## 9. Test Kapsami

### 9.1 Ozet Istatistikler

| Metrik | Deger |
|--------|-------|
| Toplam test | 243 |
| Basarili | 243 (%100) |
| Basarisiz | 0 |
| Calisma suresi | 1.73s |
| Test dosyasi | 4 (+ conftest + __init__) |
| Test satiri | 1,776 |

### 9.2 Test Dosyalari Detayi

#### test_api.py (596 satir)

| Test Sinifi | Test Sayisi | Kapsam |
|-------------|-------------|--------|
| TestHealth | 2 | Root endpoint, health check |
| TestAnalyze | 7 | 4 kompresor alt tipi, invalid tip, missing fields, sankey |
| TestCompressorTypes | 2 | /types endpoint, alan yapisi |
| TestBenchmarks | 5 | 4 tip benchmark + invalid |
| TestSolutions | 4 | Solutions endpoint, parametre destegi, yapi |
| TestBoilerAnalyze | 3 | Firetube, hotwater, invalid |
| TestChillerAnalyze | 3 | Centrifugal, absorption, invalid |
| TestPumpAnalyze | 3 | Centrifugal, throttle, invalid |
| TestFactoryAPI | 12 | CRUD, analyze, hotspot, sankey, integration |
| TestEquipmentConfig | 5 | 4 tip config + invalid |

#### test_engine.py (550 satir)

| Test Sinifi | Test Sayisi | Kapsam |
|-------------|-------------|--------|
| TestScrewCompressor | 5 | Analiz, enerji dengesi, benchmark, spesifik guc, yillik maliyet |
| TestPistonCompressor | 3 | Analiz, enerji dengesi, benchmark |
| TestScrollCompressor | 2 | Analiz, enerji dengesi |
| TestCentrifugalCompressor | 3 | Analiz, enerji dengesi, benchmark |
| TestSankey | 3 | Yapi, enerji dengesi, node isimleri |
| TestApiDict | 2 | Cikti formati, deger eslesmesi |
| TestRecommendations | 2 | Liste yapisi, oneri yapisi |
| TestBoiler | 5 | Analiz, enerji dengesi, kayip breakdown, benchmark, hotwater |
| TestChiller | 5 | Centrifugal, absorption, enerji dengesi, COP |
| TestPump | 5 | Analiz, enerji dengesi, VSD, throttle, benchmark |
| TestFactory | 8 | Aggregation, hotspot, integration, sankey, edge cases |

#### test_skills.py (453 satir)

| Test Sinifi | Test Sayisi | Kapsam |
|-------------|-------------|--------|
| TestSkillFileStructure | 17 | 14 moduler skill dosyasi + 3 dizin |
| TestSkillContentValidation | 45 | Min satir, version, heading, 7 ekipman icerik, karar agaci, JSON sema |
| TestSkillLoading | 10 | Tek skill, 7 ekipman, factory, bilinmeyen, cache |
| TestKnowledgeLoading | 7 | Tek ekipman, factory, sektor, HX, ST, dryer, missing |
| TestKnowledgeFrontmatter | 22 | 7×benchmarks, 7×formulas, 7×INDEX, factory INDEX, cross_equipment |
| TestPromptBuilding | 3 | Skills dahil, data dahil, SafeDict |
| TestFallbackResponses | 2 | Ekipman fallback, factory fallback |
| TestJsonExtraction | 5 | Direct, markdown fence, embedded, invalid, empty |

#### test_equipment_registry.py (170 satir)

| Test Sinifi | Test Sayisi | Kapsam |
|-------------|-------------|--------|
| TestEquipmentTypes | 12 | 7 tip mevcut, alt tipler, engine_ready bayraklari |
| TestRegistryFunctions | 9 | get_types, get_subtypes, is_valid, is_ready, knowledge_path |

### 9.3 Test Bosluklari

| Alan | Durum | Aciklama |
|------|-------|----------|
| heat_exchanger engine | ❌ Yok | Engine mevcut degil, test yok |
| steam_turbine engine | ❌ Yok | Engine mevcut degil, test yok |
| dryer engine | ❌ Yok | Engine mevcut degil, test yok |
| AI interpret (e2e) | ❌ Yok | Claude CLI mock testi yok |
| Frontend | ❌ Yok | React test dosyasi yok |
| Hata durumlari (engine) | ⚠️ Kismi | Negatif deger, sinir kosullari sinirli |
| Performance/load | ❌ Yok | Yuk testi yok |
| Factory multi-type | ⚠️ Kismi | Yalniz comp+boiler+chiller+pump test ediliyor |

---

## 10. CLAUDE.md Analizi

**Dosya:** `/CLAUDE.md` — Proje talimatlari ve navigasyon rehberi.

**Icerik Yeterliligi:**

| Bolum | Mevcut | Dogruluk |
|-------|--------|----------|
| Proje Ozeti | ✅ | Dogru — 7 ekipman, 6 yontem, 305+ KB dosyasi |
| Teknoloji Stack | ✅ | Dogru |
| Dizin Yapisi | ✅ | Buyuk olcude dogru, bazi detaylar eksik |
| Ekipman Tipleri tablosu | ✅ | Dogru — engine_ready durumu dogru |
| Calistirma talimatlari | ✅ | Dogru |
| AI Yorumlama Sistemi | ✅ | Skill yukleme sirasi dogru |
| Knowledge kullanimi | ✅ | Dogru |
| Kod konvansiyonlari | ✅ | Dogru |
| Test talimatlari | ✅ | Dogru (4 test dosyasi listelenmis) |
| Ileri Analiz Yontemleri | ✅ | 6 yontem dogru tanimlanmis |

**Dogruluk Notu:** CLAUDE.md'deki bilgiler mevcut kod tabanini dogru yansitmaktadir. `heat_exchanger`, `steam_turbine`, `dryer` icin engine durumu "Planned" olarak isaretlenmis ki bu dogrudur — bu dosyalar engine/ dizininde mevcut degildir. Istatistikler (305+ KB dosyasi, 17 skill) dogrudur.

---

## 11. Kod Kalitesi Degerlendirmesi

### 11.1 Type Hints

| Dosya | Fonksiyon | Return Type | Parametre Type |
|-------|-----------|-------------|----------------|
| compressor.py | 17 | 8 (%47) | 33 annotation |
| boiler.py | 13 | 12 (%92) | 28 annotation |
| chiller.py | 10 | 9 (%90) | 24 annotation |
| pump.py | 10 | 9 (%90) | 25 annotation |
| factory.py | 14 | 13 (%93) | List[dict] tipli |
| core.py | 11 | 10 (%91) | float/DeadState tipli |

**Genel:** Return type hint kullanimi boiler/chiller/pump/factory/core icin yuksek (%90+), compressor icin nispeten dusuk (%47 — erken yazilan modul).

### 11.2 Docstrings

| Dosya | Triple Quote Ciftleri | Yeterlilik |
|-------|----------------------|------------|
| compressor.py | 26 | Iyi — Google style |
| boiler.py | 19 | Iyi |
| chiller.py | 14 | Yeterli |
| pump.py | 14 | Yeterli |
| factory.py | 21 | Iyi — detayli aciklamalar |
| core.py | 15 | Iyi — formul aciklamalari |

### 11.3 Hata Yonetimi

| Katman | Yaklasim |
|--------|----------|
| Engine | `raise ValueError` ile input validasyon |
| API | FastAPI `HTTPException` ile 400/404 yanit |
| AI Service | try/except ile fallback response (ai_available: false) |
| Factory | Ekipman bazli try/except, basarisiz ekipman error field ile donuyor |
| Frontend | Axios interceptor, loading/error state yonetimi |

### 11.4 TODO/FIXME Durumu

**Sifir (0)** TODO, FIXME, HACK veya XXX yorumu bulundu. Kod tabani temiz, acik is birakılmamis.

### 11.5 Guvenlik Degerlendirmesi

| Alan | Durum | Not |
|------|-------|-----|
| Input validasyon | ✅ | Pydantic Field ile min/max/gt/lt |
| SQL Injection | N/A | Veritabani yok (in-memory) |
| XSS | ⚠️ | Frontend'de dogrudan HTML render yok, ancak AI yaniti render edilirken dikkat |
| Subprocess | ⚠️ | `claude -p prompt` — prompt kullanici verisinden olusuyor (dolaylı) |
| Rate Limiting | ❌ | API'de rate limit yok |
| Authentication | ❌ | Auth sistemi yok |
| CORS | ⚠️ | Kontrol edilmedi, muhtemelen tum originlere acik (gelistirme modu) |

---

## 12. Mevcut Durum Ozet Tablosu

### 12.1 Ekipman Engine Durumu

| Ekipman | Engine | Knowledge | Skill | API Route | Test | Sankey | Alt Tip Sayisi |
|---------|--------|-----------|-------|-----------|------|--------|----------------|
| Kompresor | ✅ 529 sat. | ✅ 19 dosya | ✅ 162 sat. | ✅ | ✅ 43 test | ✅ | 6 |
| Kazan | ✅ 627 sat. | ✅ 23 dosya | ✅ 166 sat. | ✅ | ✅ 8 test | ✅ | 7 |
| Chiller | ✅ 466 sat. | ✅ 25 dosya | ✅ 152 sat. | ✅ | ✅ 8 test | ✅ | 7 |
| Pompa | ✅ 439 sat. | ✅ 23 dosya | ✅ 169 sat. | ✅ | ✅ 8 test | ✅ | 6 |
| Isi Esanjoru | ❌ | ✅ 21 dosya | ✅ 265 sat. | ⚠️ Yalniz AI | ✅ KB testi | ❌ | 7 |
| Buhar Turbini | ❌ | ✅ 23 dosya | ✅ 187 sat. | ⚠️ Yalniz AI | ✅ KB testi | ❌ | 5 |
| Kurutma Firini | ❌ | ✅ 26 dosya | ✅ 146 sat. | ⚠️ Yalniz AI | ✅ KB testi | ❌ | 8 |

**Yalniz AI:** Bu ekipmanlar icin engine hesaplama yoktur, ancak AI yorumlama icin skill ve knowledge dosyalari mevcuttur. `equipment_registry.py`'de `engine_ready: False` olarak isaretlidir.

### 12.2 Ileri Analiz Yontemleri Durumu

| Yontem | Knowledge | Skill Referansi | Engine | UI |
|--------|-----------|-----------------|--------|----|
| Pinch Analizi | ✅ 18 dosya | ✅ factory_analyst + integration_expert | ❌ | ❌ |
| Ileri Exergy (AV/UN, EN/EX) | ✅ 18 dosya | ✅ factory_analyst | ❌ | ❌ |
| Exergoekonomik | ✅ 18 dosya | ✅ economic_advisor | ❌ | ❌ |
| Termoekonomik Opt. | ✅ 16 dosya | ✅ decision_trees referansi | ❌ | ❌ |
| EGM | ✅ 19 dosya | ✅ exergy_fundamentals referansi | ❌ | ❌ |
| Enerji Yonetimi | ✅ 21 dosya | ⚠️ Dolayli | ❌ | ❌ |

**Not:** 6 ileri analiz yonteminin hicbirinde engine hesaplama veya UI komponenti bulunmamaktadir. Yalnizca knowledge (bilgi tabani) ve skill referanslari mevcuttur. AI yorumlama sirasinda bu yontemler uygun oldugunda onerilir.

### 12.3 Fabrika Analizi Durumu

| Ozellik | Durum | Aciklama |
|---------|-------|----------|
| Proje CRUD | ✅ | Olusturma, listeleme, detay, silme |
| Ekipman ekleme/cikarma | ✅ | Proje bazli ekipman yonetimi |
| Toplu analiz | ✅ | Tum ekipmanlarin tek seferde analizi |
| Aggregation | ✅ | Toplam exergy in/out/destroyed |
| Hotspot tespiti | ✅ | 3 seviyeli onceliklendirme |
| Cross-equipment | ✅ | 5 entegrasyon deseni |
| Fabrika Sankey | ✅ | Ekipman bazli akis diyagrami |
| AI yorumlama | ✅ | Sektor destekli fabrika yorumu |
| Ileri analiz onerileri | ⚠️ | AI prompt'unda kosullu oneri (engine yok) |

---

## 13. Bagimliliklar

### 13.1 Python Backend (requirements.txt)

| Paket | Minimum Versiyon | Kullanim | Aktif Kullanim |
|-------|-----------------|----------|----------------|
| CoolProp | >=6.4.0 | Buhar/su ozellikleri | ✅ boiler.py |
| numpy | >=1.21.0 | Sayisal hesaplama | ⚠️ Dogrudan import gorulmedi |
| pandas | >=1.3.0 | Veri isleme | ⚠️ Dogrudan import gorulmedi |
| plotly | >=5.0.0 | Grafik | ⚠️ Backend'de kullanilmiyor |
| matplotlib | >=3.4.0 | Grafik | ⚠️ Backend'de kullanilmiyor |
| fastapi | >=0.109.0 | Web framework | ✅ |
| uvicorn | >=0.27.0 | ASGI server | ✅ |
| python-multipart | >=0.0.6 | Form data | ✅ FastAPI icin |
| reportlab | >=3.6.0 | PDF rapor | ⚠️ Kod'da import gorulmedi |
| python-docx | >=0.8.11 | Word rapor | ⚠️ Kod'da import gorulmedi |
| python-dotenv | >=0.19.0 | Ortam degiskenleri | ⚠️ Dogrudan kullanim gorulmedi |
| pydantic | >=2.0.0 | Veri validasyon | ✅ |
| pytest | >=7.0.0 | Test | ✅ |
| httpx | >=0.26.0 | Async HTTP / test client | ✅ |

**Not:** numpy, pandas, plotly, matplotlib, reportlab, python-docx bagimliliklari requirements.txt'de tanimli ancak mevcut kod tabaninda aktif import'lari tespit edilemedi. Bu paketler gelecek ozellikler (rapor uretimi, ileri analiz) icin hazirlanmis olabilir.

### 13.2 Frontend (package.json dependencies)

| Paket | Versiyon | Kullanim |
|-------|----------|----------|
| react | ^19.2.0 | UI framework |
| react-dom | ^19.2.0 | DOM renderer |
| react-router-dom | ^7.13.0 | Client-side routing |
| axios | ^1.13.4 | HTTP client |
| plotly.js | ^3.3.1 | Grafik kutuphanesi |
| react-plotly.js | ^2.6.0 | Plotly React wrapper |
| lucide-react | ^0.563.0 | Ikon kutuphanesi |

---

## 14. Acik Sorular ve Notlar

### 14.1 Engine Boslukları

1. **heat_exchanger.py, steam_turbine.py, dryer.py mevcut degil.** `equipment_registry.py`'de `engine_ready: False` olarak isaretli. Knowledge ve skill dosyalari hazir, engine implement edildiginde AI sistemi otomatik calisacak.

2. **Engine pattern tutarliligi onemli.** Mevcut 4 engine ayni kalibi takip ediyor: `{Type}Input` → `{Type}Result` → `analyze_{type}()` → `to_api_dict()` → `generate_{type}_sankey_data()` → `get_{type}_recommendations()`. Yeni engine'ler bu kalibi takip etmeli.

3. **factory.py sadece 4 engine'i destekliyor.** `_ANALYZERS` dict'i yalnizca compressor, boiler, chiller, pump icerir. Yeni engine eklendiginde burasi da guncellenmeli.

### 14.2 AI Servis Notlari

4. **Claude CLI subprocess yaklaşımı.** AI yorumlama `asyncio.create_subprocess_exec("claude", "-p", prompt)` ile calisiyor. Bu, Claude Code CLI'nin PATH'te bulunmasini gerektirir. Production ortaminda API tabanli entegrasyon daha uygun olabilir.

5. **120s timeout.** AI yorumlama icin 120 saniyelik timeout tanimli. Buyuk fabrika analizlerinde bu yeterli olmayabilir.

6. **LRU cache maxsize=100.** Skill ve knowledge dosyalari icin 100 dosyalik cache. 305+ knowledge dosyasi dusunuldugunde, yogun kullanimda cache miss orani artabilir.

### 14.3 Test Boslukları

7. **AI entegrasyon testi yok.** Claude CLI mock'u ile end-to-end AI yorum testi mevcut degil. `_extract_json()` ve `_fallback_response()` test edilmis, ancak tam prompt → CLI → parse akisi test edilmemis.

8. **Frontend testi yok.** React componentleri icin birim veya entegrasyon testi bulunmuyor.

9. **Compressor modulu eski.** `compressor.py` ilk yazilan modul olarak return type hint orani (%47) diger modullerin (%90+) gerisinde.

### 14.4 Kullanilmayan Bagimliliklar

10. **6 paket aktif kullanilmiyor olabilir.** numpy, pandas, plotly, matplotlib, reportlab, python-docx aktif import'lari tespit edilemedi. Bu paketler ya kalinti ya da gelecek icin hazirlik.

### 14.5 Guvenlik

11. **Auth ve rate limiting yok.** API herhangi bir kimlik dogrulama veya hiz sinirlamasi icermiyor. Production ortami icin eklenmelidir.

12. **In-memory veri deposu.** Fabrika projeleri muhtemelen memory'de tutuluyor (veritabani baglantisi yok). Sunucu yeniden basladiginda veri kaybolur.

### 14.6 Mimari Guclu Yonleri

13. **Moduler skill/knowledge sistemi.** AI bilgi tabani ve skill dosyalari tamamen ayri markdown dosyalari olarak yonetiliyor. Kod degisikligi gerektirmeden yeni bilgi eklenebilir.

14. **Equipment registry pattern.** Yeni ekipman tipi eklemek icin `equipment_registry.py`'ye bir entry, `engine/` altina modul ve `knowledge/` altina dosyalar eklemek yeterli. Iyi olceklenen bir tasarim.

15. **3-tier JSON parser.** AI yanitlari icin 3 katmanli parser (direct → markdown fence → regex) saglamlik sagliyor.

16. **Test kapsami.** Mevcut 4 engine ve API icin %100 test basarisi. Skill ve knowledge dosyalari da test ediliyor (frontmatter, icerik, yukleme).

---

## Ek: Git Commit Gecmisi

| # | Hash | Mesaj |
|---|------|-------|
| 21 | e77027e | Wire 7 equipment types and 6 advanced analysis methods into AI service layer |
| 20 | 43848a6 | Add heat exchanger, steam turbine, dryer knowledge bases and expand factory-level analysis |
| 19 | b562547 | Add modular AI skill system, knowledge metadata, and optimized prompt loading |
| 18 | 06b176b | Fix cross-equipment heat recovery calculation and UI polish |
| 17 | 24261eb | Add factory-level exergy analysis system with full-stack implementation |
| 16 | be7b85d | Add factory-level energy/exergy analysis knowledge base (33 files) |
| 15 | 793b8cb | Enable AI interpretation for all equipment types (boiler, chiller, pump) |
| 14 | b7aafcb | Add boiler, chiller, and pump exergy analysis engine modules |
| 13 | 057bc79 | Add sidebar navigation and React Router for multi-equipment platform |
| 12 | 7f623ed | Add multi-equipment backend support with equipment registry and factory routes |
| 11 | 98670a1 | Reorganize knowledge base from category-based to equipment-type hierarchy |
| 10 | 4efbbef | Add equipment knowledge base for boilers, chillers, and pumps |
| 9 | 5f4973f | Fix Claude Code CLI by removing --output-format json and inlining SKILL file |
| 8 | e203573 | Add AI-powered interpretation of exergy analysis results |
| 7 | 5e65c56 | Fix Sankey labels, savings display, and number formatting |
| 6 | b9ead50 | Fix results not displaying by correcting double .data unwrap and field name mismatches |
| 5 | abdd6cc | Fix compressor types not displaying by mapping API response fields |
| 4 | 331bbf9 | Add null/undefined safety guards across frontend components and hooks |
| 3 | 72f400a | Add full-stack: React frontend + FastAPI backend + tests |
| 2 | aac5da1 | Expand compressor knowledge base with 14 new files and 4 updates |
| 1 | 212af12 | Initial project setup: ExergyLab compressor exergy analysis engine |

**Gozlem:** Proje kompressor-only olarak baslamis, adimlı olarak 4 engine → fabrika analizi → AI entegrasyonu → moduler skill/knowledge → 7 ekipman destegi + 6 ileri analiz yontemi seklinde buyumus. Net bir iteratif gelistirme izlenmektedir.

---

*Bu rapor ExergyLab kod tabaninin 2026-02-02 tarihli statik analizine dayanmaktadir. Calisma zamani davranislari (performans, AI yanit kalitesi) bu analizin kapsaminda degildir.*
