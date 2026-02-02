# ExergyLab - Endüstriyel Exergy Analiz Platformu

## Proje Özeti

ExergyLab, 7 endüstriyel ekipman tipinin (kompresör, kazan, chiller, pompa, ısı eşanjörü, buhar türbini, kurutma fırını) ve fabrikaların exergy analizini yapan, 6 ileri analiz yöntemi ve AI destekli yorumlar sunan bir enerji verimliliği platformudur.

**Temel Fark:** Enerji verimi yerine **exergy verimi** odaklı analiz — termodinamiğin 2. yasasına dayalı gerçek verimlilik ölçümü.

**İstatistikler:** 305+ knowledge dosyası, 17 skill dosyası, 7 ekipman tipi, 6 ileri analiz yöntemi

## Teknoloji Stack

- **Backend:** Python 3.10+, FastAPI, Pydantic
- **Frontend:** React 18, Vite, TailwindCSS, Recharts
- **AI:** Claude API (yorumlama için)
- **Termodinamik:** CoolProp (buhar/su özellikleri)

## Dizin Yapısı

```
exergy-lab/
├── api/                    # FastAPI backend
│   ├── routes/            # API endpoints
│   │   ├── analysis.py    # Ekipman analizi
│   │   ├── factory.py     # Fabrika analizi
│   │   └── interpret.py   # AI yorumlama
│   ├── schemas/           # Pydantic modelleri
│   └── services/          # Business logic
│       ├── claude_code_service.py  # AI entegrasyonu
│       └── equipment_registry.py   # Ekipman tip kayıt defteri
│
├── engine/                 # Exergy hesaplama motorları
│   ├── compressor.py      # Kompresör analizi
│   ├── boiler.py          # Kazan analizi
│   ├── chiller.py         # Chiller analizi
│   ├── pump.py            # Pompa analizi
│   ├── heat_exchanger.py  # Isı eşanjörü analizi
│   ├── steam_turbine.py   # Buhar türbini analizi
│   ├── dryer.py           # Kurutma fırını analizi
│   ├── factory.py         # Fabrika aggregation
│   └── sankey.py          # Sankey diyagramı verisi
│
├── knowledge/              # AI Knowledge Base (305+ dosya)
│   ├── INDEX.md           # Navigasyon haritası
│   ├── compressor/        # 18 dosya
│   ├── boiler/            # 22 dosya
│   ├── chiller/           # 24 dosya
│   ├── pump/              # 22 dosya
│   ├── heat_exchanger/    # 21 dosya — U-değer, etkililik, fouling, NTU
│   ├── steam_turbine/     # 21 dosya — izentropik verim, CHP, PRV ikamesi
│   ├── dryer/             # 26 dosya — SMER, SEC, psikrometri, tip seçimi
│   └── factory/           # 150+ dosya
│       ├── pinch/         # Pinch analizi (18 dosya)
│       ├── advanced_exergy/ # İleri exergy analizi (18 dosya)
│       ├── exergoeconomic/ # Exergoekonomik analiz (21 dosya)
│       ├── thermoeconomic_optimization/ # Termoekonomik opt. (16 dosya)
│       ├── entropy_generation/ # Entropi üretim min. (19 dosya)
│       └── energy_management/ # Enerji yönetimi
│
├── skills/                 # AI Skill dosyaları (17 dosya)
│   ├── core/              # Temel beceriler (3 dosya)
│   │   ├── exergy_fundamentals.md  # Exergy kavramları + EGM + exergoekonomik + pinch
│   │   ├── response_format.md      # JSON şemaları (tek ekipman, fabrika, ileri analiz)
│   │   └── decision_trees.md       # 7 ekipman + fabrika + ileri analiz karar ağaçları
│   ├── equipment/         # Ekipman uzmanları (7 dosya)
│   │   ├── compressor_expert.md
│   │   ├── boiler_expert.md
│   │   ├── chiller_expert.md
│   │   ├── pump_expert.md
│   │   ├── heat_exchanger_expert.md
│   │   ├── steam_turbine_expert.md
│   │   └── dryer_expert.md
│   ├── factory/           # Fabrika analizi (3 dosya)
│   │   ├── factory_analyst.md      # Hotspot, cross-equipment, ileri analiz önerileri
│   │   ├── integration_expert.md   # HEN optimizasyonu, pinch tabanlı eşleştirme
│   │   └── economic_advisor.md     # Exergoekonomik değerlendirme
│   └── output/            # Çıktı formatı (1 dosya)
│       └── turkish_style.md
│
├── frontend/               # React frontend
│   └── src/
│       ├── pages/         # Sayfa componentleri
│       ├── components/    # UI componentleri
│       └── services/      # API client
│
├── tests/                  # Pytest testleri
└── CLAUDE.md              # Bu dosya
```

## Ekipman Tipleri

| # | Tip | Türkçe | Engine | Tipik Exergy Verimi |
|---|-----|--------|--------|---------------------|
| 1 | compressor | Kompresör | Ready | %35-55 |
| 2 | boiler | Kazan | Ready | %25-40 |
| 3 | chiller | Chiller | Ready | %20-35 |
| 4 | pump | Pompa | Ready | %40-65 |
| 5 | heat_exchanger | Isı Eşanjörü | Planned | %30-60 |
| 6 | steam_turbine | Buhar Türbini | Planned | %50-85 |
| 7 | dryer | Kurutma Fırını | Planned | %5-25 |

## Çalıştırma

```bash
# Backend
cd exergy-lab
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

## AI Yorumlama Sistemi

### Nasıl Çalışır?

1. Kullanıcı ekipman/fabrika analizi yapar
2. Engine hesaplamaları yapar (exergy, kayıp, benchmark)
3. Sonuçlar `/api/interpret` endpoint'ine gönderilir
4. Claude API, skill ve knowledge dosyalarını kullanarak yorum üretir
5. Yapılandırılmış JSON yanıt döner

### Skill Yükleme Sırası

AI yorumlama sırasında `claude_code_service.py` şu sırayla skill yükler:

1. **Core skills** (her zaman): `exergy_fundamentals.md` → `response_format.md` → `decision_trees.md`
2. **Equipment skill** (tek ekipman): `equipment/{type}_expert.md`
3. **Factory skills** (fabrika): `factory_analyst.md` → `integration_expert.md` → `economic_advisor.md`
4. **Output skill** (her zaman): `output/turkish_style.md`

### Knowledge Base Kullanımı

AI yorumlama yaparken şu dosyaları referans alır:

**Tek Ekipman İçin:**
- `knowledge/{equipment}/benchmarks.md` — Verimlilik karşılaştırma
- `knowledge/{equipment}/formulas.md` — Hesaplama doğrulama
- `knowledge/{equipment}/solutions/*.md` — Öneri kaynakları

**Fabrika İçin:**
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası fırsatlar
- `knowledge/factory/prioritization.md` — Önceliklendirme
- `knowledge/factory/factory_benchmarks.md` — Sektörel benchmark
- `knowledge/factory/sector_{sector}.md` — Sektöre özel
- `knowledge/factory/advanced_exergy/overview.md` — İleri exergy analizi
- `knowledge/factory/pinch/fundamentals.md` — Pinch analizi temelleri
- `knowledge/factory/entropy_generation/overview.md` — EGM genel bakış
- `knowledge/factory/exergoeconomic/evaluation_criteria.md` — Exergoekonomik değerlendirme

## Kod Konvansiyonları

### Python
- Type hints kullan
- Docstring ekle (Google style)
- Error handling ile wrap et
- Birim: SI (kW, kJ, °C, bar)

### JavaScript/React
- Functional components
- Hooks kullan
- TailwindCSS utility classes
- API çağrıları için async/await

### Knowledge Base (Markdown)
- Türkçe başlıklar, teknik terimler İngilizce parantez içinde
- Her dosyada: "## İlgili Dosyalar" ve "## Referanslar" bölümü
- Tablolar, formüller, pratik örnekler

## Test

```bash
# Tüm testler
pytest tests/ -v

# Specific test
pytest tests/test_api.py -v
pytest tests/test_engine.py -v
pytest tests/test_skills.py -v
pytest tests/test_equipment_registry.py -v
```

## Önemli Notlar

1. **Exergy vs Enerji:** Exergy termodinamik kaliteyi ölçer. Düşük sıcaklıktaki ısı düşük exergy'dir.

2. **Cross-Equipment:** Asıl değer ekipmanlar arası entegrasyonda (kompresör atık ısısı → kazan).

3. **Sektörel Benchmark:** Her sektörün farklı exergy profili var (gıda vs çimento).

4. **AI Yorumu:** Engine hesaplar, AI yorumlar. İkisi birbirini tamamlar.

5. **7 Ekipman Tipi:** AI sistemi 7 ekipman tipini destekler, engine hesaplama ilk 4 tip için hazır.

## İleri Analiz Yöntemleri

ExergyLab bilgi tabanı aşağıdaki 6 ileri analiz yöntemini destekler:

1. **Pinch Analizi:** Linnhoff metodolojisi, composite curve, GCC, HEN tasarımı — `knowledge/factory/pinch/`
   - Ne zaman: 3+ sıcak/soğuk akış, toplam ısı > 500 kW

2. **İleri Exergy Analizi:** AV/UN, EN/EX, 4-yollu dekompozisyon — `knowledge/factory/advanced_exergy/`
   - Ne zaman: 3+ ekipman, I_total > 100 kW, ekipmanlar arası güçlü etkileşim

3. **Exergoekonomik Analiz:** SPECO, Ċ_D, f_k/r_k değerlendirmesi — `knowledge/factory/exergoeconomic/`
   - Ne zaman: f_k < 0.25 veya f_k > 0.65 olan bileşenler

4. **Termoekonomik Optimizasyon:** Parametrik, yapısal, çok amaçlı optimizasyon — `knowledge/factory/thermoeconomic_optimization/`
   - Ne zaman: Toplam Ċ_D > 50.000 €/yıl, birden fazla yatırım alternatifi

5. **Entropi Üretim Minimizasyonu (EGM):** Bejan sayısı, Gouy-Stodola, constructal yasa — `knowledge/factory/entropy_generation/`
   - Ne zaman: N_s > 0.5, irreversibility kaynak analizi gerekli

6. **Enerji Yönetim Sistemi:** ISO 50001, enerji denetimi — `knowledge/factory/energy_management/`
   - Ne zaman: Sistematik enerji yönetimi gerekli

## Katkıda Bulunma

1. Feature branch oluştur
2. Testleri geçir
3. PR aç

## Lisans

Proprietary - Olivenet Ltd.
