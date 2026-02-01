# ExergyLab - Endüstriyel Exergy Analiz Platformu

## Proje Özeti

ExergyLab, endüstriyel ekipmanların (kompresör, kazan, chiller, pompa) ve fabrikaların exergy analizini yapan, AI destekli yorumlar sunan bir enerji verimliliği platformudur.

**Temel Fark:** Enerji verimi yerine **exergy verimi** odaklı analiz — termodinamiğin 2. yasasına dayalı gerçek verimlilik ölçümü.

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
│       └── claude_code_service.py  # AI entegrasyonu
│
├── engine/                 # Exergy hesaplama motorları
│   ├── compressor.py      # Kompresör analizi
│   ├── boiler.py          # Kazan analizi
│   ├── chiller.py         # Chiller analizi
│   ├── pump.py            # Pompa analizi
│   ├── factory.py         # Fabrika aggregation
│   └── sankey.py          # Sankey diyagramı verisi
│
├── knowledge/              # AI Knowledge Base (124 dosya)
│   ├── INDEX.md           # Navigasyon haritası
│   ├── compressor/        # 18 dosya
│   ├── boiler/            # 22 dosya
│   ├── chiller/           # 24 dosya
│   ├── pump/              # 22 dosya
│   └── factory/           # 33 dosya
│
├── skills/                 # AI Skill dosyaları
│   ├── core/              # Temel beceriler
│   ├── equipment/         # Ekipman uzmanları
│   ├── factory/           # Fabrika analizi
│   └── output/            # Çıktı formatı
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
4. Claude API, knowledge base'i kullanarak yorum üretir
5. Yapılandırılmış JSON yanıt döner

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

### Skill Dosyaları

`/skills/` dizinindeki dosyalar AI'ın davranışını tanımlar:
- Yanıt formatı (JSON schema)
- Yorumlama kuralları
- Karar ağaçları
- Önceliklendirme mantığı

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
```

## Önemli Notlar

1. **Exergy vs Enerji:** Exergy termodinamik kaliteyi ölçer. Düşük sıcaklıktaki ısı düşük exergy'dir.

2. **Cross-Equipment:** Asıl değer ekipmanlar arası entegrasyonda (kompresör atık ısısı → kazan).

3. **Sektörel Benchmark:** Her sektörün farklı exergy profili var (gıda vs çimento).

4. **AI Yorumu:** Engine hesaplar, AI yorumlar. İkisi birbirini tamamlar.

## Katkıda Bulunma

1. Feature branch oluştur
2. Testleri geçir
3. PR aç

## Lisans

Proprietary - Olivenet Ltd.
