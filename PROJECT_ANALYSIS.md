# ExergyLab - Kapsamli Proje Analizi

> **Son Guncelleme:** 2026-02-05
> **Versiyon:** 2.0
> **Durum:** Uretim (Production)

---

## Icindekiler

1. [Proje Ozeti](#1-proje-ozeti)
2. [Hizli Baslangic](#2-hizli-baslangic)
3. [Mimari Genel Bakis](#3-mimari-genel-bakis)
4. [Dizin Yapisi](#4-dizin-yapisi-guncel)
5. [Backend Detaylari](#5-backend-detaylari)
6. [Frontend Detaylari](#6-frontend-detaylari)
7. [Knowledge Base](#7-knowledge-base)
8. [AI Sistemi](#8-ai-sistemi)
9. [Test Kapsamsi](#9-test-kapsamsi)
10. [Bagimliliklar](#10-bagimliliklar)
11. [Guvenlik](#11-guvenlik)
12. [Bilinen Sorunlar](#12-bilinen-sorunlar)
13. [Gelistirme Onerileri](#13-gelistirme-onerileri)
14. [Commit Gecmisi](#14-commit-gecmisi)
15. [Metrik Ozeti](#15-metrik-ozeti)

---

## 1. Proje Ozeti

ExergyLab, 7 endustriyel ekipman tipinin ve fabrikalarin exergy analizini yapan, 6 ileri analiz yontemi ve AI destekli yorumlar sunan bir enerji verimliligi platformudur.

**Temel Fark:** Enerji verimi yerine **exergy verimi** odakli analiz -- termodinamigin 2. yasasina dayali gercek verimlilik olcumu.

### Platform Ozellikleri

| Ozellik | Aciklama |
|---------|----------|
| 7 Ekipman Tipi | Kompresor, kazan, chiller, pompa, isi esanjoru, buhar turbini, kurutma firini |
| 46 Alt Tip | Her ekipman icin detayli alt tip destegi |
| 6 Ileri Analiz | Pinch, ileri exergy, exergoekonomik, termoekonomik, EGM, enerji yonetimi |
| AI Yorumlama | Claude API ile Turkce teknik yorumlar |
| What-If Senaryolar | Baseline vs senaryo karsilastirmasi |
| Radar Benchmark | 6 eksenli performans degerlendirme (A-F not) |
| AV/UN Ayrisim | Kacinilinabilir/kacinilmaz exergy yikim analizi |
| Exergoekonomik | SPECO metodolojisi, f-faktor, r-faktor |
| Fabrika Analizi | Coklu ekipman agregasyonu, hotspot tespiti, entegrasyon firsatlari |
| SQLite Kalicilik | Proje ve analiz sonuclarinin veritabaninda saklanmasi |
| JWT Kimlik Dogrulama | Opsiyonel kullanici yetkilendirmesi |

### Teknoloji Stack

| Katman | Teknoloji |
|--------|-----------|
| Backend | Python 3.10+, FastAPI, Pydantic v2, SQLAlchemy 2.0 |
| Frontend | React 19, Vite 7, TailwindCSS 3, Plotly.js |
| AI | Claude API (yorumlama + sohbet) |
| Termodinamik | CoolProp (buhar/su ozellikleri) |
| Veritabani | SQLite + aiosqlite |
| Auth | python-jose (JWT), passlib (bcrypt) |

---

## 2. Hizli Baslangic

### Backend

```bash
cd exergy-lab
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

Backend basladiginda:
- API dokumantasyonu: http://localhost:8000/docs
- Saglik kontrolu: http://localhost:8000/health

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend basladiginda:
- Uygulama: http://localhost:5173
- Vite proxy: `/api/*` -> `http://localhost:8000`

### Testler

```bash
pytest tests/ -v                          # Tum testler
pytest tests/test_api.py -v               # Sadece API testleri
pytest tests/test_engine.py -v            # Sadece motor testleri
pytest tests/test_exergoeconomic.py -v    # Exergoekonomik testler
```

---

## 3. Mimari Genel Bakis

```
+-------------------+         +-------------------+         +------------------+
|                   |  HTTP   |                   |         |                  |
|   React Frontend  | ------> |   FastAPI Backend  | ------> |  Engine Modules  |
|   (Vite + Tailwind)|  /api  |   (REST API)      |         |  (Hesaplamalar)  |
|                   |         |                   |         |                  |
+-------------------+         +--------+----------+         +------------------+
                                       |
                              +--------+----------+
                              |                   |
                    +---------+---------+ +-------+---------+
                    |                   | |                 |
                    |   Claude AI API   | |  SQLite DB      |
                    |   (Yorumlama)     | |  (Kalicilik)    |
                    |                   | |                 |
                    +-------------------+ +-----------------+
```

### Veri Akisi

```
Kullanici Girisi
    |
    v
Ekipman Input Sinifi (CompressorInput, BoilerInput, vb.)
    |
    v
Ekipman Analizoru (analyze_compressor, analyze_boiler, vb.)
    |
    v
ExergyResult (temel exergy metrikleri)
    |
    +---> _apply_exergoeconomic()  [ekonomik alanlar eklenir]
    +---> generate_*_sankey_data() [diagram verisi]
    +---> generate_radar_data()    [6 eksenli benchmark]
    +---> compute_comparison()     [what-if senaryo]
    |
    v
API Response (to_dict() serializasyonu)
```

---

## 4. Dizin Yapisi (Guncel)

```
exergy-lab/
|
|-- api/                              # FastAPI backend (4,236 satir)
|   |-- main.py                       # App, CORS, lifespan, router kaydi (66 satir)
|   |-- __init__.py
|   |-- auth/                         # Kimlik dogrulama modulu
|   |   |-- config.py                 # JWT ayarlari (10 satir)
|   |   |-- dependencies.py           # Auth dependency injection (66 satir)
|   |   |-- schemas.py                # User/Token skemalari (26 satir)
|   |   |-- security.py               # Parola hash, JWT olusturma (40 satir)
|   |-- database/                     # Veritabani katmani
|   |   |-- __init__.py               # DB init/close (23 satir)
|   |   |-- config.py                 # DB ayarlari (8 satir)
|   |   |-- crud.py                   # CRUD operasyonlari (230 satir)
|   |   |-- models.py                 # 7 SQLAlchemy modeli (145 satir)
|   |   |-- session.py                # Oturum yonetimi (38 satir)
|   |-- routes/                       # API endpointleri
|   |   |-- analysis.py               # Ekipman analizi (943 satir)
|   |   |-- auth.py                   # Kimlik dogrulama (60 satir)
|   |   |-- benchmarks.py             # Benchmark verileri (93 satir)
|   |   |-- chat.py                   # AI sohbet (75 satir)
|   |   |-- factory.py                # Fabrika CRUD + analiz (279 satir)
|   |   |-- interpret.py              # AI yorumlama (62 satir)
|   |   |-- solutions.py              # Cozum onerileri (85 satir)
|   |-- schemas/                      # Pydantic modelleri
|   |   |-- requests.py               # Istek skemalari (211 satir)
|   |   |-- responses.py              # Yanit skemalari (225 satir)
|   |   |-- factory.py                # Fabrika skemalari (65 satir)
|   |-- services/                     # Business logic
|       |-- claude_code_service.py     # AI entegrasyonu (1,036 satir)
|       |-- equipment_registry.py      # Ekipman tip kayit defteri (173 satir)
|       |-- knowledge_router.py        # Bilgi yonlendirme (274 satir)
|
|-- engine/                            # Exergy hesaplama motorlari (5,870 satir)
|   |-- __init__.py                    # Modul baslangici (47 satir)
|   |-- core.py                        # DeadState, ExergyResult, temel fonksiyonlar (171 satir)
|   |-- exergoeconomic.py             # SPECO analizi, f/r faktorleri (242 satir)
|   |-- compressor.py                  # Kompresor analizi (656 satir)
|   |-- boiler.py                      # Kazan analizi (678 satir)
|   |-- chiller.py                     # Chiller analizi (522 satir)
|   |-- pump.py                        # Pompa analizi (497 satir)
|   |-- heat_exchanger.py             # Isi esanjoru analizi (513 satir)
|   |-- steam_turbine.py              # Buhar turbini analizi (580 satir)
|   |-- dryer.py                       # Kurutma firini analizi (555 satir)
|   |-- factory.py                     # Fabrika agregasyonu (824 satir)
|   |-- sankey.py                      # Sankey diyagrami verisi (158 satir)
|   |-- radar.py                       # Radar benchmark (159 satir)
|   |-- compare.py                     # What-if karsilastirma (155 satir)
|   |-- utils.py                       # Yardimci fonksiyonlar (113 satir)
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
|       |-- pinch/                     # Pinch analizi
|       |-- advanced_exergy/           # Ileri exergy analizi
|       |-- exergoeconomic/            # Exergoekonomik analiz
|       |-- thermoeconomic_optimization/ # Termoekonomik optimizasyon
|       |-- entropy_generation/        # Entropi uretim minimizasyonu
|       |-- energy_management/         # Enerji yonetimi
|
|-- skills/                            # AI Skill dosyalari (17 dosya)
|   |-- core/                          # Temel beceriler (3 dosya)
|   |   |-- exergy_fundamentals.md     # Exergy kavramlari + EGM + exergoekonomik + pinch
|   |   |-- response_format.md         # JSON semalari
|   |   |-- decision_trees.md          # 7 ekipman + fabrika karar agaclari
|   |-- equipment/                     # Ekipman uzmanlari (7 dosya)
|   |   |-- compressor_expert.md
|   |   |-- boiler_expert.md
|   |   |-- chiller_expert.md
|   |   |-- pump_expert.md
|   |   |-- heat_exchanger_expert.md
|   |   |-- steam_turbine_expert.md
|   |   |-- dryer_expert.md
|   |-- factory/                       # Fabrika analizi (3 dosya)
|   |   |-- factory_analyst.md         # Hotspot, cross-equipment onerileri
|   |   |-- integration_expert.md      # HEN optimizasyonu, pinch eslestirme
|   |   |-- economic_advisor.md        # Exergoekonomik degerlendirme
|   |-- output/                        # Cikti formati (1 dosya)
|       |-- turkish_style.md           # Turkce cikti stili
|
|-- frontend/                          # React frontend (5,199 satir)
|   |-- src/
|       |-- main.jsx                   # React giris noktasi
|       |-- App.jsx                    # Routing yapilandirmasi
|       |-- pages/                     # 6 sayfa componenti
|       |-- components/                # ~50 UI componenti
|       |   |-- layout/               # Layout, Header, Sidebar, Footer
|       |   |-- dashboard/            # DashboardLayout, TabContainer, OverviewTab, FlowTab, AITab, ScenarioTab
|       |   |-- forms/                # ParameterForm, FormField
|       |   |-- equipment/            # SubtypeSelector
|       |   |-- results/              # AIInterpretation, SankeyDiagram, RadarBenchmark
|       |   |-- whatif/               # ScenarioEditor, ComparisonPanel, RadarComparison
|       |   |-- factory/              # FactoryHeader, PriorityList, IntegrationPanel, FactorySankey
|       |   |-- chat/                 # ChatPanel (markdown render, sohbet)
|       |   |-- common/              # Card, Button, Loading, Tooltip
|       |-- services/                  # API istemcileri
|       |   |-- api.js                 # Axios instance + ekipman API'leri
|       |   |-- factoryApi.js          # Fabrika API'leri
|       |-- hooks/                     # Custom React hooks
|       |   |-- useAnalysis.js         # Analiz state yonetimi
|       |   |-- useCompressorTypes.js  # Kompresor tipleri
|       |-- utils/
|           |-- formatters.js          # Sayi/para birimi formatlama
|
|-- tests/                             # Pytest testleri (3,712 satir)
|   |-- conftest.py                    # DB fixture + TestClient
|   |-- test_api.py                    # API endpoint testleri (48 test)
|   |-- test_engine.py                 # Motor testleri (60 test)
|   |-- test_avoidable_unavoidable.py  # AV/UN testleri (29 test)
|   |-- test_compare.py               # What-if testleri (12 test)
|   |-- test_dryer.py                  # Kurutma firini testleri (23 test)
|   |-- test_equipment_registry.py     # Kayit defteri testleri (18 test)
|   |-- test_exergoeconomic.py         # Exergoekonomik testler (22 test)
|   |-- test_heat_exchanger.py         # Isi esanjoru testleri (23 test)
|   |-- test_knowledge_router.py       # Bilgi yonlendirme testleri (24 test)
|   |-- test_radar.py                  # Radar chart testleri (20 test)
|   |-- test_skills.py                 # AI beceri testleri (71 test)
|   |-- test_steam_turbine.py          # Buhar turbini testleri (20 test)
|
|-- requirements.txt                   # Python bagimliliklari (17 paket)
|-- CLAUDE.md                         # Proje talimat dosyasi
|-- PROJECT_ANALYSIS.md               # Bu dosya
|-- exergylab.db                       # SQLite veritabani
```

---

## 5. Backend Detaylari

### 5.1 API Endpointleri

Toplam **21 endpoint** -- 7 route dosyasi uzerinden:

#### Kok Endpointler (api/main.py)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| GET | `/` | API bilgi + docs linki |
| GET | `/health` | Saglik kontrolu `{"status": "ok"}` |

#### Ekipman Analizi (api/routes/analysis.py -- 943 satir)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| GET | `/api/equipment-types` | 7 ekipman tipi listesi |
| GET | `/api/equipment-types/{type}/subtypes` | Alt tip listesi |
| GET | `/api/equipment-types/{type}/config` | Alan tanimlari + varsayilan degerler |
| POST | `/api/analyze` | Tek ekipman exergy analizi |
| POST | `/api/compare` | Baseline vs senaryo karsilastirmasi |
| GET | `/api/compressor-types` | Legacy geriye uyumluluk |

#### Benchmark & Cozumler (api/routes/benchmarks.py, solutions.py)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| GET | `/api/benchmarks/{type}` | Verimlilik karsilastirma verileri |
| GET | `/api/solutions/{type}` | Filtrelenmis cozum onerileri |

#### AI Yorumlama & Sohbet (api/routes/interpret.py, chat.py)

| Metot | Yol | Aciklama |
|-------|-----|----------|
| POST | `/api/interpret` | Tek ekipman AI yorumu |
| POST | `/api/chat` | Bilgi tabani destekli AI sohbet |

#### Kimlik Dogrulama (api/routes/auth.py)

| Metot | Yol | Auth | Aciklama |
|-------|-----|------|----------|
| POST | `/api/auth/register` | Hayir | Kullanici kaydi |
| POST | `/api/auth/login` | Hayir | JWT token alma |
| GET | `/api/auth/me` | Evet | Mevcut kullanici bilgisi |

#### Fabrika Yonetimi (api/routes/factory.py -- 279 satir)

| Metot | Yol | Auth | Aciklama |
|-------|-----|------|----------|
| POST | `/api/factory/projects` | Opsiyonel | Yeni proje olustur |
| GET | `/api/factory/projects` | Opsiyonel | Proje listesi |
| GET | `/api/factory/projects/{id}` | Opsiyonel | Proje detayi |
| POST | `/api/factory/projects/{id}/equipment` | Opsiyonel | Ekipman ekle |
| DELETE | `/api/factory/projects/{id}/equipment/{eid}` | Opsiyonel | Ekipman kaldir |
| POST | `/api/factory/projects/{id}/analyze` | Opsiyonel | Fabrika analizi calistir |
| POST | `/api/factory/projects/{id}/interpret` | Opsiyonel | Fabrika AI yorumu |

### 5.2 Veritabani Semasi

6 SQLAlchemy modeli (`api/database/models.py` -- 145 satir):

#### users

| Sutun | Tip | Aciklama |
|-------|-----|----------|
| id | str (UUID) | Primary key |
| email | str | Benzersiz, indeksli |
| hashed_password | str | bcrypt hash |
| full_name | str? | Kullanici adi |
| is_active | bool | Aktiflik durumu (varsayilan True) |
| created_at | datetime | Kayit tarihi |

#### factory_projects

| Sutun | Tip | Aciklama |
|-------|-----|----------|
| id | str (8-char UUID) | Primary key |
| name | str | Proje adi |
| sector | str? | Sektor (tekstil, gida, kimya, vb.) |
| description | str? | Aciklama |
| owner_id | str? | FK -> users.id |
| created_at | datetime | Olusturma tarihi |
| updated_at | datetime | Son guncelleme |

#### equipment

| Sutun | Tip | Aciklama |
|-------|-----|----------|
| id | str (8-char UUID) | Primary key |
| project_id | str | FK -> factory_projects.id |
| name | str | Ekipman adi |
| equipment_type | str | 7 tip birinden |
| subtype | str? | Alt tip |
| parameters | JSON | Ekipman parametreleri |
| created_at | datetime | Ekleme tarihi |

#### analysis_results

| Sutun | Tip | Aciklama |
|-------|-----|----------|
| id | str (8-char UUID) | Primary key |
| equipment_id | str | FK -> equipment.id (unique, 1-to-1) |
| result_data | JSON | Tam analiz ciktisi |
| analyzed_at | datetime | Analiz tarihi |

#### factory_analyses

| Sutun | Tip | Aciklama |
|-------|-----|----------|
| id | str (8-char UUID) | Primary key |
| project_id | str | FK -> factory_projects.id |
| aggregates | JSON | Toplam metrikler |
| hotspots | JSON | Oncelik sirali ekipmanlar |
| integration_opportunities | JSON | Entegrasyon firsatlari |
| sankey_data | JSON | Fabrika Sankey verisi |
| analyzed_at | datetime | Analiz tarihi |

#### ai_interpretations

| Sutun | Tip | Aciklama |
|-------|-----|----------|
| id | str (8-char UUID) | Primary key |
| project_id | str? | FK -> factory_projects.id |
| equipment_id | str? | FK -> equipment.id |
| interpretation_data | JSON | AI yorum ciktisi |
| created_at | datetime | Olusturma tarihi |

#### Iliskiler

```
User 1---* FactoryProject 1---* Equipment 1---1 AnalysisResult
                           1---* FactoryAnalysis
                           1---* AIInterpretation
```

Tum alt iliskiler `cascade="all, delete-orphan"` ile yapilandirilmistir.

### 5.3 Engine Modulleri

14 Python dosyasi, toplam **5,870 satir**:

#### core.py (171 satir) -- Temel Veri Yapilari

**Siniflar:**
- `DeadState` -- Referans ortam kosullari (T0=298.15K, P0=101.325kPa)
- `ExergyResult` -- Tum ekipman sonuclarinin temel sinifi

**ExergyResult Alanlari:**
- Exergy: `exergy_in_kW`, `exergy_out_kW`, `exergy_destroyed_kW`, `exergy_efficiency_pct`
- Ekonomik: `annual_loss_kWh`, `annual_loss_EUR`, `recoverable_heat_kW`
- AV/UN: `exergy_destroyed_avoidable_kW`, `exergy_destroyed_unavoidable_kW`, `avoidable_ratio_pct`
- Exergoekonomik: `exergoeconomic_Z_dot_eur_h`, `exergoeconomic_C_dot_destruction_eur_h`, `exergoeconomic_f_factor`, `exergoeconomic_r_factor`, `exergoeconomic_c_product_eur_kWh`, `exergoeconomic_total_cost_rate_eur_h`

**Yardimci Fonksiyonlar:**
- `heat_exergy(Q_kW, T_K)` -- Isi exergisi: Ex_Q = Q x (1 - T0/T)
- `carnot_factor(T_hot_K, T_cold_K)` -- Carnot verimi
- `celsius_to_kelvin()`, `bar_to_kpa()`, `air_density()` -- Birim donusumleri
- `compute_avoidable_split()` -- AV/UN ayrisimi (Tsatsaronis & Morosuk 2008)

#### exergoeconomic.py (242 satir) -- SPECO Analizi

**Siniflar:**
- `ExergoeconomicInput` -- PEC, faiz orani, ekipman omru, bakim faktoru
- `ExergoeconomicResult` -- Z_dot, C_dot_D, f-faktor, r-faktor, c_product

**Fonksiyonlar:**
- `compute_crf()` -- Sermaye geri kazanim faktoru
- `compute_z_dot()` -- Yilliklandirilmis yatirim maliyeti orani
- `estimate_equipment_cost()` -- Guc yasasi maliyet korelasyonu (PEC = a x W^b)
- `analyze_exergoeconomic()` -- Tam SPECO analizi
- `_apply_exergoeconomic()` -- ExergyResult'a ekonomik alanlari enjekte eder

**Maliyet Korelasyonlari:**
| Ekipman | a | b | Formul |
|---------|---|---|--------|
| Kompresor | 3,500 | 0.70 | PEC = 3500 x W^0.70 |
| Kazan | 2,000 | 0.75 | PEC = 2000 x W^0.75 |
| Chiller | 1,200 | 0.80 | PEC = 1200 x W^0.80 |
| Pompa | 1,000 | 0.65 | PEC = 1000 x W^0.65 |

#### 7 Ekipman Modulu

Her ekipman modulu asagidaki standart yapiyi izler:

| Modul | Satir | Alt Tip Sayisi | Analiz Fonksiyonu |
|-------|-------|----------------|-------------------|
| compressor.py | 656 | 4 (screw, piston, scroll, centrifugal) | `analyze_compressor()` + 3 ozel |
| boiler.py | 678 | 7 (firetube, watertube, hotwater, condensing, waste_heat, electric, biomass) | `analyze_boiler()` |
| chiller.py | 522 | 7 (screw, centrifugal, scroll, reciprocating, absorption, air_cooled, water_cooled) | `analyze_chiller()` |
| pump.py | 497 | 6 (centrifugal, positive_displacement, submersible, vertical_turbine, booster, vacuum) | `analyze_pump()` |
| heat_exchanger.py | 513 | 7 (shell_tube, plate, air_cooled, double_pipe, spiral, economizer, recuperator) | `analyze_heat_exchanger()` |
| steam_turbine.py | 580 | 5 (back_pressure, condensing, extraction, orc, micro_turbine) | `analyze_steam_turbine()` |
| dryer.py | 555 | 8+ (convective, rotary, fluidized_bed, spray, belt, heat_pump, infrared, drum) | `analyze_dryer()` |

Her moduldeki ortak fonksiyonlar:
- `analyze_{equipment}(input_data, dead_state, _calc_avoidable)` -- Ana analiz
- `generate_{equipment}_sankey_data(result, subtype)` -- Sankey verisi
- `get_{equipment}_recommendations(result, input_data)` -- Cozum onerileri
- `_get_benchmark_comparison(eta_ex, subtype)` -- Benchmark eslestirme
- `_calculate_percentile(eta_ex, subtype)` -- Sektor yuzdelik dilimi

Her modulde `UNAVOIDABLE_REF_{EQUIPMENT}` sozlugu var -- en iyi ulasilabilir referans degerleri (Tsatsaronis metodolojisi).

#### factory.py (824 satir) -- Fabrika Agregasyonu

**Siniflar:**
- `EquipmentType` -- Enum (7 tip)
- `EquipmentItem` -- Tek ekipman kaydi
- `FactoryAnalysisResult` -- Fabrika ciktisi

**Fonksiyonlar:**
- `analyze_factory(equipment_list)` -- Ana fabrika analizi
- `analyze_equipment_item(item)` -- Tek ekipman dispatch
- `_calculate_aggregates(results)` -- Toplam exergy metrikleri
- `_identify_hotspots(results)` -- Oncelikli exergy kayiplari siralamassi
- `_detect_integration_opportunities(equipment_list, results)` -- Capraz ekipman firsatlari
- `_generate_factory_sankey(results, aggregates)` -- Birlesmis Sankey

#### Diger Moduller

| Modul | Satir | Aciklama |
|-------|-------|----------|
| sankey.py | 158 | Sankey diyagrami dispatcher (ekipman tipine gore) |
| radar.py | 159 | 6 eksenli benchmark: Exergy Verimi, Iyilestirme, Sektor, Isi Geri Kazanim, Yikim Orani, Maliyet Verimliligi. Not: A(85+), B(70+), C(50+), D(30+), F(<30) |
| compare.py | 155 | What-if: delta hesaplama, iyilesen/kotulesen metrikler, Turkce ozet |
| utils.py | 113 | Birim donusumu, dogrulama, formatlama, JSON I/O |

### 5.4 Kimlik Dogrulama Sistemi

**Mimari:** JWT tabanli, opsiyonel (geriye uyumlu)

**Bilesenler:**
- `api/auth/config.py` -- SECRET_KEY, ALGORITHM (HS256), TOKEN_EXPIRE (24 saat)
- `api/auth/security.py` -- `create_access_token()`, `get_password_hash()`, `verify_password()`
- `api/auth/dependencies.py` -- `require_auth` (zorunlu), `optional_auth` (opsiyonel)

**Yetki Kontrol Kurallari:**
1. Kullanici yok -> izin ver
2. Proje sahibi yok -> izin ver
3. Kullanici == sahip -> izin ver
4. Kullanici != sahip -> 403 Forbidden

**Akis:**
```
POST /api/auth/register -> bcrypt hash + DB kayit
POST /api/auth/login    -> JWT token uretimi
GET  /api/auth/me       -> Token dogrulama + kullanici bilgisi
```

### 5.5 Ekipman Kayit Defteri

`api/services/equipment_registry.py` (173 satir) -- 7 ekipman tipi ve 46 alt tip:

| Ekipman | Alt Tipler | engine_ready |
|---------|------------|-------------|
| Kompresor | screw, screw_oilfree, piston, scroll, centrifugal, roots | Evet |
| Kazan | steam_firetube, steam_watertube, hotwater, condensing, waste_heat, electric, biomass | Evet |
| Chiller | screw, centrifugal, scroll, reciprocating, absorption, air_cooled, water_cooled | Evet |
| Pompa | centrifugal, positive_displacement, submersible, vertical_turbine, booster, vacuum | Evet |
| Isi Esanjoru | shell_tube, plate, air_cooled, double_pipe, spiral, economizer, recuperator | Evet |
| Buhar Turbini | back_pressure, condensing, extraction, orc, micro_turbine | Evet |
| Kurutma Firini | convective, rotary, fluidized_bed, spray, belt, heat_pump, infrared, drum | Evet |

---

## 6. Frontend Detaylari

### 6.1 Sayfa Yapisi

6 sayfa + routing (`App.jsx`):

```
BrowserRouter
|-- /login           -> Login (tam sayfa, layout yok)
|-- Layout (sidebar + ana icerik)
    |-- /                          -> Dashboard (7 ekipman karti)
    |-- /equipment/:equipmentType  -> EquipmentAnalysis
    |-- /factory                   -> FactoryList
    |-- /factory/new               -> FactoryWizard
    |-- /factory/:projectId        -> FactoryDashboard
    |-- /reports                   -> ReportsPlaceholder (yakinday)
    |-- *                          -> Redirect -> /
```

#### Dashboard.jsx
- 7 ekipman karti gosterir
- Fabrika analizi tanitim karti
- Tek ekipman analiz sayfasina yonlendirir

#### EquipmentAnalysis.jsx
- Iki modlu layout: analiz oncesi (form) / analiz sonrasi (dashboard)
- 4 sekme: Genel Bakis (Radar + AV/UN), Akis (Sankey), AI (Yorum + Sohbet), Senaryo (What-if)
- `useAnalysis()` hook ile state yonetimi
- Asenkron AI yorumlama (ana analizi engellemez)

#### FactoryList.jsx
- Fabrika projelerini listeler
- Sektor rozeti, ekipman sayisi, tarih bilgisi

#### FactoryWizard.jsx
- 2 adimli sihirbaz: proje bilgileri -> ekipman ekleme
- `AddEquipmentModal`: 3 adim (tip -> alt tip -> parametreler)

#### FactoryDashboard.jsx
- Uc gorunum modu:
  1. Bos: ekipman yok -> "Ekipman Ekle" yonlendirmesi
  2. Ekipmanli: analiz yok -> "Analiz Calistir" butonu
  3. Tam Dashboard: metrik bar + oncelik listesi + entegrasyon + Sankey + AI

#### Login.jsx
- Giris/kayit gecisi
- JWT token localStorage'a kayit
- Otomatik `/factory` yonlendirmesi

### 6.2 Component Hiyerarsisi

50 JSX + 5 JS dosyasi, 10 alt dizin:

#### Layout (4 dosya)
- `Layout.jsx` -- Ana sarmalayici (sidebar + icerik)
- `Header.jsx` -- Kullanici bilgisi, cikis butonu
- `Sidebar.jsx` -- 64px genislik, katlanabilir gruplar, NavLink
- `Footer.jsx` -- Alt bilgi

#### Dashboard (8 dosya)
- `DashboardLayout.jsx` -- Analiz oncesi/sonrasi layout degistirici
- `TabContainer.jsx` -- Sekme navigasyonu (hidden class ile state koruma)
- `OverviewTab.jsx` -- RadarBenchmark + AV/UN stacked bar + temel metrikler
- `FlowTab.jsx` -- Sankey diyagrami
- `AITab.jsx` -- AI yorumlama + sohbet paneli
- `ScenarioTab.jsx` -- What-if senaryo editoru + karsilastirma
- `ParameterSidebar.jsx` -- Sol kenar cubugu (parametreler + yeniden analiz)
- `MetricBar.jsx` -- Ust yatay metrik cubugu

#### Forms (3 dosya)
- `ParameterForm.jsx` -- 2 sutunlu alan gridi
- `FormField.jsx` -- Dinamik alan render (input/select/checkbox)
- `CompressorTypeSelector.jsx` -- Kompresor tipi butonlari

#### Results (7 dosya)
- `AIInterpretation.jsx` -- Ozet, detayli analiz, oneriler, aksiyon plani, uyarilar
- `SankeyDiagram.jsx` -- Plotly sankey (node -> link -> value)
- `RadarBenchmark.jsx` -- 6 eksenli Plotly polar/radar grafigi (A-F not rozeti)
- `BenchmarkChart.jsx` -- Benchmark cubuk grafigi
- `MetricsCard.jsx` -- Metrik ozet karti
- `SolutionsList.jsx` -- Oneri listesi
- `ResultsPanel.jsx` -- Sonuc konteyner

#### What-if (3 dosya)
- `ScenarioEditor.jsx` -- Baseline/senaryo parametre editoru
- `ComparisonPanel.jsx` -- Delta karsilastirma tablosu (yesil/kirmizi gosterge)
- `RadarComparison.jsx` -- Iki katmanli radar grafigi

#### Factory (11 dosya)
- `FactoryHeader.jsx` -- Proje adi, sektor rozeti, butonlar
- `FactoryMetricBar.jsx` -- Fabrika seviyesi metrikler
- `EquipmentInventory.jsx` -- Ekipman tablosu (tip, alt tip, durum, silme)
- `AddEquipmentModal.jsx` -- 3 adimli modal sihirbaz
- `PriorityList.jsx` -- Oncelik sirali hotspot listesi (verimlilik cubugu, AV%, not rozeti, kW + EUR)
- `HotspotList.jsx` -- Basitlesmis hotspot gorunumu
- `IntegrationPanel.jsx` -- Capraz ekipman firsatlari (kaynak -> hedef oklari)
- `IntegrationOpportunities.jsx` -- Entegrasyon detaylari
- `FactoryAIPanel.jsx` -- Fabrika AI yorumlama butonu + sonuclari
- `FactoryAIInterpretation.jsx` -- Fabrika seviyesi AI gorunumu
- `FactorySankey.jsx` -- Fabrika seviyesi Sankey

#### Chat (1 dosya)
- `ChatPanel.jsx` -- Tam sohbet arayuzu: markdown render, mavi/beyaz mesaj balonlari, bilgi kaynagi rozetleri, oneri butonlari

#### Common (4 dosya)
- `Card.jsx`, `Button.jsx`, `Loading.jsx`, `Tooltip.jsx`

### 6.3 Servisler

#### api.js -- Ana API Istemcisi
```javascript
const api = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
});
// Otomatik JWT token ekleme (localStorage'dan)
```

**Ekipman API'leri:**
- `getEquipmentConfig(type)` -- Alan tanimlari
- `analyzeEquipment(type, subtype, params)` -- Analiz
- `getEquipmentTypes()` -- Tip listesi

**AI API'leri:**
- `interpretAnalysis(result, type, subtype, params)` -- AI yorumu
- `compareScenarios({...})` -- What-if
- `chatWithAI({type, subtype, question, data, history})` -- Sohbet

**Auth API'leri:**
- `register()`, `login()`, `getMe()`, `logout()`

#### factoryApi.js -- Fabrika API Istemcisi
- `createFactoryProject()`, `getFactoryProjects()`, `getFactoryProject()`
- `addEquipmentToProject()`, `removeEquipmentFromProject()`
- `analyzeFactory()`, `interpretFactory()`

### 6.4 Custom Hooks

#### useAnalysis
```javascript
const { result, solutions, loading, error, analyze, reset, interpretation, aiLoading } = useAnalysis();
```
2 fazli analiz:
1. Faz 1: Ana analiz + cozumler (engelleyici)
2. Faz 2: AI yorumlama (arka planda, engellemez)

#### useCompressorTypes
```javascript
const { types, loading, error } = useCompressorTypes();
```

### 6.5 Vite Yapilandirmasi

```javascript
defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
```

---

## 7. Knowledge Base

305 markdown dosyasi, 8 ana dizin:

| Dizin | Dosya Sayisi | Icerik |
|-------|-------------|--------|
| compressor/ | 19 | Benchmark, formuller, cozumler, alt tip detaylari |
| boiler/ | 23 | Yakit exergy faktorleri, baca gazi analizi, yoğusma |
| chiller/ | 25 | COP, absorption, serbest sogutma, termal depolama |
| pump/ | 23 | Hidrolik guc, VSD, kavitasyon, sistem egrisi |
| heat_exchanger/ | 21 | U-deger, LMTD, NTU, fouling, etkinlik |
| steam_turbine/ | 23 | Izentropik verim, CHP, PRV ikamesi, ORC |
| dryer/ | 26 | SMER, SEC, psikrometri, tip secimi |
| factory/ | 144 | 6 ileri analiz yontemi (asagida detay) |

### Fabrika Knowledge (144 dosya, 6 ileri yontem)

| Alt Dizin | Dosya | Yontem | Uygulama Kosulu |
|-----------|-------|--------|-----------------|
| pinch/ | ~18 | Linnhoff Pinch Analizi | 3+ sicak/soguk akis, toplam isi > 500 kW |
| advanced_exergy/ | ~18 | AV/UN + EN/EX dekompozisyon | 3+ ekipman, I_total > 100 kW |
| exergoeconomic/ | ~21 | SPECO, C_D, f_k/r_k | f_k < 0.25 veya f_k > 0.65 |
| thermoeconomic_optimization/ | ~16 | Parametrik/yapisal optimizasyon | C_D > 50,000 EUR/yil |
| entropy_generation/ | ~19 | Bejan sayisi, Gouy-Stodola | N_s > 0.5 |
| energy_management/ | ~10 | ISO 50001, enerji denetimi | Sistematik yonetim ihtiyaci |

Her knowledge dosyasinda:
- YAML frontmatter (skill_id, versiyon, ekipman)
- Turkce basliklar, teknik terimler Ingilizce parantez icinde
- Tablolar, formuller, pratik ornekler
- "Ilgili Dosyalar" ve "Referanslar" bolumleri

---

## 8. AI Sistemi

### 8.1 Skill Yukleme Sirasi

`claude_code_service.py` (1,036 satir) AI yorumlama sirasinda:

```
1. Core Skills (her zaman):
   |-- exergy_fundamentals.md    # Exergy kavramlari
   |-- response_format.md       # JSON semalari
   |-- decision_trees.md        # Karar agaclari

2. Equipment Skill (tek ekipman):
   |-- equipment/{type}_expert.md

3. Factory Skills (fabrika analizi):
   |-- factory_analyst.md        # Hotspot, capraz ekipman
   |-- integration_expert.md     # HEN, pinch eslestirme
   |-- economic_advisor.md       # Exergoekonomik

4. Output Skill (her zaman):
   |-- output/turkish_style.md   # Turkce cikti stili
```

### 8.2 Knowledge Yonlendirme

`knowledge_router.py` (274 satir) -- soru/analiz turune gore dosya yonlendirme:

**Tek Ekipman:**
- `knowledge/{equipment}/benchmarks.md`
- `knowledge/{equipment}/formulas.md`
- Cozum dosyalari (soru icerigi bazli)

**Fabrika:**
- `knowledge/factory/cross_equipment.md`
- `knowledge/factory/prioritization.md`
- `knowledge/factory/factory_benchmarks.md`
- `knowledge/factory/exergoeconomic/evaluation_criteria.md`
- `knowledge/factory/advanced_exergy/overview.md`
- `knowledge/factory/pinch/fundamentals.md`
- `knowledge/factory/entropy_generation/overview.md`
- `knowledge/factory/sector_{sector}.md` (sektor varsa)

### 8.3 AI Sohbet

`/api/chat` endpoint'i:
- Ekipman tipine gore knowledge routing
- Analiz verisi baglami (opsiyonel)
- Sohbet gecmisi destegi
- Turkce yanit + bilgi kaynaklari + takip onerileri

### 8.4 Fallback Mekanizmasi

AI kullanilamadiginda guvenli varsayilan yanit:
```json
{
  "ai_available": false,
  "summary": "...",
  "detailed_analysis": "...",
  "key_insights": [],
  "recommendations": [],
  "not_recommended": [],
  "action_plan": {"immediate": [], "short_term": [], "medium_term": []},
  "warnings": []
}
```

### 8.5 JSON Cikarma

3 katmanli parser:
1. Dogrudan JSON parse
2. Markdown fence cikarma (```json...```)
3. Regex tabanli ham JSON tespiti

---

## 9. Test Kapsamsi

14 test dosyasi, **327 test fonksiyonu**, toplam **3,712 satir**:

### Test Dosyalari

| Dosya | Test Sayisi | Satir | Kapsam |
|-------|------------|-------|--------|
| test_api.py | 48 | 599 | API endpointleri, fabrika CRUD |
| test_engine.py | 60 | 552 | 4 temel ekipman motoru |
| test_skills.py | 71 | 453 | AI beceri dosyalari, knowledge dogrulama |
| test_avoidable_unavoidable.py | 29 | 376 | AV/UN ayrisimi, invariantler |
| test_exergoeconomic.py | 22 | 325 | SPECO, f-faktor, r-faktor |
| test_compare.py | 12 | 232 | What-if delta hesaplama |
| test_heat_exchanger.py | 23 | 200 | Bejan sayisi, LMTD, fouling |
| test_radar.py | 20 | 200 | 6 eksenli benchmark puanlama |
| test_dryer.py | 23 | 196 | SMER, isi kaynaklari, termal verim |
| test_steam_turbine.py | 20 | 178 | CHP modu, izentropik verim |
| test_equipment_registry.py | 18 | 170 | 7 tip, 46 alt tip dogrulama |
| test_knowledge_router.py | 24 | 159 | Bilgi yonlendirme, sohbet |
| conftest.py | - | 72 | DB fixture, TestClient |

### Test Kategorileri

| Kategori | Test Sayisi | Aciklama |
|----------|------------|----------|
| Temel Exergy Hesaplama | ~130 | Enerji dengesi, verimlilik, benchmark |
| API Entegrasyonu | ~48 | Endpoint yanit dogrulama |
| Ileri Analiz | ~61 | Exergoekonomik, what-if, radar |
| AI Sistemi | ~71 | Beceri dosyalari, knowledge, JSON cikarma |
| AV/UN Invariantlari | ~29 | Avoidable <= Total, sum = Total |

### Test Altyapisi

- **Veritabani:** Her test icin bellekte SQLite (izole)
- **API:** FastAPI TestClient + dependency override
- **Parametrik:** Pytest parametrize (10 motor x 5 invariant = 50 varyant)
- **Konfigurasyon:** `conftest.py` -- otomatik tablo olusturma/silme

---

## 10. Bagimliliklar

### Python (requirements.txt -- 17 paket)

| Kategori | Paketler |
|----------|----------|
| Web API | fastapi >= 0.109.0, uvicorn >= 0.27.0, python-multipart >= 0.0.6 |
| Veri Modelleri | pydantic >= 2.0.0 |
| Termodinamik | CoolProp >= 6.4.0 |
| Veri Isleme | numpy >= 1.21.0, pandas >= 1.3.0 |
| Gorsellestirme | plotly >= 5.0.0, matplotlib >= 3.4.0 |
| Raporlama | reportlab >= 3.6.0, python-docx >= 0.8.11 |
| Veritabani | sqlalchemy >= 2.0.0, aiosqlite >= 0.19.0 |
| Auth | python-jose[cryptography] >= 3.3.0, passlib[bcrypt] >= 1.7.4 |
| Yapilandirma | python-dotenv >= 0.19.0 |
| Test | pytest >= 7.0.0, httpx >= 0.26.0 |

### Frontend (package.json)

**Calisma Zamani (7 paket):**

| Paket | Versiyon | Amac |
|-------|---------|------|
| react | 19.2.0 | UI framework |
| react-dom | 19.2.0 | DOM rendering |
| react-router-dom | 7.13.0 | Client-side routing |
| axios | 1.13.4 | HTTP istemcisi |
| lucide-react | 0.563.0 | Ikon kutuphanesi |
| plotly.js | 3.3.1 | Grafik kutuphanesi (Sankey, Radar) |
| react-plotly.js | 2.6.0 | Plotly React sarmalayicisi |

**Gelistirme (5 paket):**

| Paket | Versiyon | Amac |
|-------|---------|------|
| vite | 7.2.4 | Build araci |
| @vitejs/plugin-react | 5.1.1 | Vite React eklentisi |
| tailwindcss | 3.4.19 | Utility CSS framework |
| postcss | 8.5.6 | CSS donusumu |
| autoprefixer | 10.4.24 | CSS vendor onekleri |

---

## 11. Guvenlik

### Mevcut Onlemler

| Alan | Durum | Detay |
|------|-------|-------|
| Girdi Dogrulama | Aktif | Pydantic v2 ile tum endpoint'lerde |
| Kimlik Dogrulama | Aktif | JWT (HS256), 24 saat gecerlilik |
| Parola Hashleme | Aktif | bcrypt (passlib) |
| CORS | Aktif | localhost:5173, localhost:3000 |
| Sahiplik Kontrolu | Aktif | Fabrika projelerinde owner_id dogrulama |
| SQL Injection | Korunmus | SQLAlchemy ORM (parametrik sorgular) |
| XSS | Korunmus | React DOM escaping |
| Hata Gizleme | Aktif | AI hatalari kullaniciya gosterilmez (fallback) |

### Dikkat Gerektiren Alanlar

| Alan | Risk | Oneri |
|------|------|-------|
| SECRET_KEY | Ortam degiskeni ile yonetilmeli | `.env` dosyasindan yukleniyor |
| CORS | Uretimde kisitlanmali | Sadece localhost'a izin var |
| Rate Limiting | Yok | AI endpointlerine eklenebilir |
| HTTPS | Uygulanmamis | Uretimde zorunlu |
| Girdi Boyutu | Sinirli | Buyuk JSON'lar icin limit eklenebilir |

---

## 12. Bilinen Sorunlar

### Cozulmus Sorunlar

| Sorun | Commit | Cozum |
|-------|--------|-------|
| "Argument list too long" fabrika AI yorumlamasinda | ececa31 | Prompt gecmisi ve knowledge icerigi kirpma |
| 422 hatalari eksik Pydantic varsayilanlari | 823fa48 | Tum zorunlu alanlara varsayilan deger ekleme |
| Sohbet takip basarisizligi | 329bda6 | Prompt gecmisi ve knowledge icerigi kirpma |
| AI prompt sablonlari HX/ST/Dryer icin eksik | 481608c | Sablon ekleme |

### Bilinen Kisitlamalar

| Kisitlama | Detay |
|-----------|-------|
| CoolProp bagimliligi | Buhar/su ozellikleri icin gerekli; fallback yaklasimsiz hesaplama mevcut |
| AI yanit suresi | Claude API suresi uzun olabilir (~10-30sn); frontend'de non-blocking |
| Tekil veritabani | SQLite tek yazici -- eşzamanlı yazma islemi desteklemez |
| Radar benchmark | Sadece kompresor icin sektorel detay; diger ekipmanlarda genel |
| Cost korelasyonlari | 4/7 ekipman icin mevcut; diger 3 icin varsayilan kullanilir |

---

## 13. Gelistirme Onerileri

### Kisa Vadeli (1-2 ay)

| Oneri | Oncelik | Etki |
|-------|---------|------|
| Tum ekipmanlara sektorel radar detayi | Yuksek | Benchmark kalitesi |
| Heat exchanger + steam turbine + dryer maliyet korelasyonlari | Yuksek | Exergoekonomik dogruluk |
| Rate limiting (AI endpointleri) | Orta | Guvenlik |
| Analiz sonuclarini PDF/DOCX export | Orta | Kullanilabilirlik |

### Orta Vadeli (3-6 ay)

| Oneri | Oncelik | Etki |
|-------|---------|------|
| Pinch analizi motor modulu | Yuksek | Fabrika optimizasyonu |
| Ileri exergy motor modulu (AV/UN + EN/EX) | Yuksek | Analiz derinligi |
| PostgreSQL gecisi | Orta | Olceklenebilirlik |
| Frontend state yonetimi (Redux/Zustand) | Orta | Karmasiklik yonetimi |
| WebSocket ile gercek zamanli AI streaming | Orta | Kullanici deneyimi |

### Uzun Vadeli (6-12 ay)

| Oneri | Oncelik | Etki |
|-------|---------|------|
| Coklu kullanici + takim yonetimi | Orta | Kurumsal kullanim |
| Tarihsel veri analizi + trend izleme | Orta | Veri odakli karar |
| Mobil uyumlu responsive tasarim | Dusuk | Erisim genisligi |
| Uluslararasilastirma (i18n) | Dusuk | Pazar genisligi |

---

## 14. Commit Gecmisi

Son 25 commit (en yeniden en eskiye):

| Commit | Aciklama |
|--------|----------|
| ececa31 | "Argument list too long" hatasini fabrika AI yorumlamasinda duzelt |
| 72a905f | 4 ekipman motoruna exergoekonomik analiz ekle (f-faktor, r-faktor, maliyet oranlari) |
| 6a6d5a8 | Fabrika projeleri icin opsiyonel JWT kimlik dogrulama + sahiplik ekle |
| cc5bd2c | Bellek ici fabrika depolamasini SQLite kalicilik katmaniyla degistir |
| 3dfbbfc | Fabrika dashboard'unu uc modlu layout + 5 yeni bilesenle yeniden tasarla |
| 3cecff3 | Ekipman analizi UI'ini iki modlu dashboard layout ile yeniden tasarla |
| 329bda6 | Prompt gecmisi ve knowledge icerigi kirparak sohbet takip hatasini duzelt |
| cffa443 | 305 dosyali knowledge tabani yonlendirmesiyle AI sohbet paneli ekle |
| 1eb234f | 7 ekipman tipi icin What-If senaryo karsilastirma modu ekle |
| f2253a6 | Tum ekipman analiz sonuclarina 6 eksenli benchmark radar grafigi ekle |
| 823fa48 | Tum Pydantic sema alanlarina varsayilan deger ekleyerek 422 hatalarini duzelt |
| f6616fc | 7 motorda kacinilabilir/kacinilmaz exergy yikim ayrisimi ekle |
| 481608c | Isi esanjoru, buhar turbini, kurutma firini AI prompt sablonlarini duzelt |
| 162e11f | Isi esanjoru, buhar turbini, kurutma firinini frontend UI'ina entegre et |
| d092c48 | Isi esanjoru, buhar turbini, kurutma firini exergy motorlarini API ile ekle |
| fd0a740 | Kapsamli proje analiz raporu ekle (844 satirlik Turkce kod taramasi) |
| e77027e | 7 ekipman tipi ve 6 ileri analiz yontemini AI servis katmanina bagla |
| 43848a6 | Isi esanjoru, buhar turbini, kurutma firini knowledge tabanlari + fabrika genislet |
| b562547 | Moduler AI beceri sistemi, knowledge metadata, optimize prompt yukleme ekle |
| 06b176b | Capraz ekipman isi geri kazanim hesaplamasi duzelt + UI cilala |
| 24261eb | Tam yigin uygulamayla fabrika seviyesi exergy analiz sistemi ekle |
| be7b85d | Fabrika seviyesi enerji/exergy analiz knowledge tabani ekle (33 dosya) |
| 793b8cb | Tum ekipman tipleri icin AI yorumlamayi etkinlestir (kazan, chiller, pompa) |
| b7aafcb | Kazan, chiller, pompa exergy analiz motor modulleri ekle |
| 057bc79 | Coklu ekipman platformu icin sidebar navigasyon ve React Router ekle |

---

## 15. Metrik Ozeti

| Metrik | Deger |
|--------|-------|
| **Toplam Kod Satiri** | **19,017** |
| Python satiri | 13,818 |
| JS/JSX satiri | 5,199 |
| Engine modulleri | 15 dosya (5,870 satir) |
| API modulleri | 26 dosya (4,236 satir) |
| Knowledge dosyalari | 305 |
| Skill dosyalari | 17 |
| Test dosyalari | 14 |
| Test fonksiyonlari | 327 |
| Test satiri | 3,712 |
| API endpointleri | 21 |
| Veritabani tablolari | 6 (+ 1 SQLAlchemy Base) |
| React sayfalar | 6 |
| React componentler | 50 JSX + 5 JS |
| Ekipman tipleri | 7 |
| Ekipman alt tipleri | 46 |
| Python bagimliliklari | 17 |
| Frontend bagimliliklari | 12 (7 runtime + 5 dev) |
| Git commit sayisi (gosterilen) | 25 |

---

*Bu dokuman, ExergyLab kod tabaninin 2026-02-05 tarihli kapsamli analizidir.*
*Otomatik olarak olusturulmustur -- guncellik icin kaynak kodu kontrol edin.*
