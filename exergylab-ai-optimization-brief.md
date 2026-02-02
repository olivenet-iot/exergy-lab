# ExergyLab AI Optimizasyon Brief - Kapsamlı Rehber

> **Claude Code için:** Bu brief, ExergyLab projesinde AI performansını optimize etmek için kapsamlı bir rehberdir. Brief'teki görevleri tamamla VE kendi insiyatifinle projeyi geliştirmek adına ek iyileştirmeler yap.

---

## 🎯 OTONOM İYİLEŞTİRME YETKİSİ

**Bu brief'i uygularken şu yetkilere sahipsin:**

1. **Brief'teki görevleri tamamla** — Aşağıda belirtilen tüm iyileştirmeleri uygula
2. **Kendi iyileştirmelerini ekle** — Projeyi incelerken fark ettiğin eksiklikleri, optimizasyon fırsatlarını, bug'ları veya geliştirme alanlarını kendi insiyatifinle düzelt
3. **Dokümantasyon ekle** — Eksik gördüğün dokümantasyonu tamamla
4. **Kod kalitesi** — Refactoring, error handling, type hints eksikse ekle
5. **Test coverage** — Eksik testler varsa ekle
6. **Knowledge base** — Eksik veya yetersiz bilgi varsa güncelle/ekle

**Kısıtlar:**
- Mevcut çalışan işlevselliği bozma
- API contract'larını değiştirme (breaking changes)
- Her değişikliği commit mesajında açıkla

**Beklenti:** Brief'in sonunda, sadece belirtilen görevleri değil, aynı zamanda projenin genel kalitesini artıran ek iyileştirmeleri de tamamlamış ol.

---

## 📋 BÖLÜM 1: CLAUDE.md Oluşturma

**Dosya:** `/CLAUDE.md` (proje kökünde)

Claude Code projeyi açtığında **ilk bu dosyayı okur**. Projenin DNA'sı burada.

### İçerik:

```markdown
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
├── knowledge/              # AI Knowledge Base (119 dosya)
│   ├── INDEX.md           # Navigasyon haritası
│   ├── compressor/        # 18 dosya
│   ├── boiler/            # 22 dosya
│   ├── chiller/           # 24 dosya
│   ├── pump/              # 22 dosya
│   └── factory/           # 33 dosya
│
├── skills/                 # AI Skill dosyaları
│   └── SKILL_exergy_interpreter.md
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
```

---

## 📋 BÖLÜM 2: Modüler Skill Yapısı

Mevcut tek büyük SKILL dosyasını **modüler skill'lere** böl.

### 2.1 Yeni Dizin Yapısı

```
skills/
├── README.md                    # Skills sistemi açıklaması
├── core/
│   ├── exergy_fundamentals.md   # Temel exergy kavramları
│   ├── response_format.md       # JSON yanıt şablonları
│   └── decision_trees.md        # Karar ağaçları
│
├── equipment/
│   ├── compressor_expert.md     # Kompresör uzmanı
│   ├── boiler_expert.md         # Kazan uzmanı
│   ├── chiller_expert.md        # Chiller uzmanı
│   └── pump_expert.md           # Pompa uzmanı
│
├── factory/
│   ├── factory_analyst.md       # Fabrika analisti
│   ├── integration_expert.md    # Entegrasyon uzmanı
│   └── economic_advisor.md      # Ekonomik danışman
│
└── output/
    ├── report_writer.md         # Rapor yazma kuralları
    └── turkish_style.md         # Türkçe yazım kuralları
```

### 2.2 Her Skill Dosyasının Yapısı

```markdown
---
skill_id: compressor_expert
version: 1.0
triggers:
  - equipment_type: compressor
  - analysis_type: single_equipment
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
knowledge_files:
  - knowledge/compressor/benchmarks.md
  - knowledge/compressor/formulas.md
  - knowledge/compressor/solutions/*.md
---

# [Skill Adı]

## Amaç
[Bu skill ne yapar]

## Ne Zaman Kullanılır
[Tetiklenme koşulları]

## Bilgi Kaynakları
[Hangi knowledge dosyalarını oku]

## Karar Kuralları
[Spesifik karar mantığı]

## Yanıt Formatı
[JSON schema veya örnek]

## Örnekler
[Input/output örnekleri]
```

### 2.3 Skill Dosyaları İçerikleri

#### skills/README.md

```markdown
# ExergyLab Skills Sistemi

## Genel Bakış

Skills, AI'ın davranışını ve uzmanlık alanlarını tanımlayan modüler dosyalardır.

## Skill Kategorileri

### Core Skills
Tüm analizlerde kullanılan temel beceriler.

### Equipment Skills
Ekipman tipine özel uzmanlık.

### Factory Skills
Fabrika seviyesi analiz becerileri.

### Output Skills
Çıktı formatı ve stil kuralları.

## Skill Seçim Mantığı

```
1. Analiz tipi belirlenir (single_equipment / factory)
2. Ekipman tipi belirlenir
3. İlgili skill dosyaları yüklenir
4. Karar ağacı işletilir
5. Yanıt formatına göre çıktı üretilir
```

## Yeni Skill Ekleme

1. Uygun kategoride .md dosyası oluştur
2. Metadata header ekle
3. Karar kurallarını tanımla
4. Örnekler ekle
5. Test et
```

#### skills/core/exergy_fundamentals.md

```markdown
---
skill_id: exergy_fundamentals
version: 1.0
type: core
---

# Exergy Temelleri

## Temel Kavramlar

### Exergy Nedir?
Exergy, bir sistemin çevresiyle dengeye gelene kadar yapabileceği maksimum iştir. Enerji korunur ama exergy yok olur (2. Yasa).

### Exergy vs Enerji
- **Enerji verimi:** Çıkış/Giriş enerji oranı
- **Exergy verimi:** Çıkış/Giriş exergy oranı (termodinamik kalite)

### Neden Exergy?
Kazan %88 enerji verimi gösterebilir ama %35 exergy verimi. Exergy gerçek iyileştirme potansiyelini gösterir.

## Exergy Hesaplama Temelleri

### Fiziksel Exergy
```
ex_physical = (h - h₀) - T₀(s - s₀)
```
- h: Entalpi
- s: Entropi
- ₀: Referans çevre koşulları (T₀=25°C, P₀=1 atm)

### Kimyasal Exergy
Yakıtlar için:
```
Ex_fuel = m_fuel × LHV × φ
```
- φ: Kimyasal exergy faktörü (~1.04-1.08 hidrokarbonlar için)

### Exergy Yıkımı (İrreversibl)
```
I = Ex_in - Ex_out - Ex_useful
```

## Benchmark Değerlendirme Kuralları

| Exergy Verimi | Değerlendirme |
|---------------|---------------|
| > 50% | Mükemmel |
| 40-50% | İyi |
| 30-40% | Ortalama |
| 20-30% | Düşük |
| < 20% | Kritik |

Bu değerler ekipman tipine göre ayarlanmalı (bkz. equipment skills).
```

#### skills/core/response_format.md

```markdown
---
skill_id: response_format
version: 1.0
type: core
---

# AI Yanıt Formatları

## Tek Ekipman Analizi JSON Schema

```json
{
  "summary": "string - 2-3 cümle özet",
  "detailed_analysis": "string - Detaylı teknik analiz",
  
  "key_findings": [
    {
      "finding": "string - Bulgu",
      "severity": "high|medium|low",
      "evidence": "string - Kanıt/veri"
    }
  ],
  
  "recommendations": [
    {
      "title": "string - Öneri başlığı",
      "priority": "high|medium|low",
      "description": "string - Detaylı açıklama",
      "annual_savings_eur": number,
      "investment_eur": number,
      "payback_years": number
    }
  ],
  
  "not_recommended": [
    {
      "title": "string",
      "reason": "string"
    }
  ],
  
  "action_plan": {
    "immediate": ["string"],
    "short_term": ["string"],
    "medium_term": ["string"]
  },
  
  "warnings": ["string"]
}
```

## Fabrika Analizi JSON Schema

```json
{
  "summary": "string",
  "factory_efficiency_assessment": "string",
  
  "hotspot_analysis": [
    {
      "equipment_id": "string",
      "equipment_name": "string",
      "priority": "high|medium|low",
      "analysis": "string",
      "exergy_destroyed_kW": number
    }
  ],
  
  "integration_opportunities": [
    {
      "title": "string",
      "source": "string",
      "target": "string",
      "description": "string",
      "potential_savings_eur": number,
      "investment_eur": number,
      "roi_years": number
    }
  ],
  
  "prioritized_actions": [
    {
      "rank": number,
      "action": "string",
      "priority": "high|medium|low",
      "annual_savings_eur": number,
      "investment_eur": number,
      "payback_years": number
    }
  ],
  
  "sector_specific_insights": ["string"],
  
  "warnings": ["string"]
}
```

## Yanıt Kuralları

1. **Somut ol:** "İyileştirme yapılabilir" yerine "€5,000/yıl tasarruf sağlanabilir"
2. **Rakam ver:** Her öneri için tasarruf, yatırım, ROI
3. **Önceliklendir:** High > Medium > Low
4. **Uyarı ekle:** Risk ve dikkat edilmesi gerekenler
5. **Türkçe yaz:** Teknik terimler parantez içinde İngilizce olabilir
```

#### skills/core/decision_trees.md

```markdown
---
skill_id: decision_trees
version: 1.0
type: core
---

# Karar Ağaçları

## Kompresör Analizi Karar Ağacı

```
BAŞLA: Kompresör analizi
│
├── Exergy verimi < 40%?
│   ├── EVET → Kritik düşük verim
│   │   ├── Spesifik güç > 8 kW/(m³/min)?
│   │   │   └── EVET → OKU: solutions/compressor_replacement.md
│   │   ├── Yük faktörü < 50%?
│   │   │   └── EVET → OKU: solutions/capacity_control.md, solutions/vsd.md
│   │   └── Basınç > 8 bar ve kullanım < 7 bar gerekli?
│   │       └── EVET → OKU: solutions/pressure_optimization.md
│   │
│   └── HAYIR → Kabul edilebilir verim
│       ├── Kaçak oranı tahmini?
│       │   └── > %20 → OKU: solutions/leak_detection.md
│       └── VSD var mı?
│           └── HAYIR ve değişken yük → OKU: solutions/vsd.md
│
└── SONUÇ: Öneri listesi oluştur, ROI'ye göre sırala
```

## Kazan Analizi Karar Ağacı

```
BAŞLA: Kazan analizi
│
├── Exergy verimi < 30%?
│   ├── EVET → Düşük verim
│   │   ├── Baca gazı sıcaklığı > 200°C?
│   │   │   └── EVET → OKU: solutions/economizer.md
│   │   ├── Fazla hava > 20%?
│   │   │   └── EVET → OKU: solutions/combustion_optimization.md
│   │   └── Blowdown > 5%?
│   │       └── EVET → OKU: solutions/blowdown_heat_recovery.md
│   │
│   └── HAYIR → Ortalama/iyi verim
│       └── İyileştirme potansiyeli sınırlı, bakım öner
│
├── Enerji verimi < 85%?
│   └── EVET → OKU: solutions/insulation.md, solutions/maintenance.md
│
└── SONUÇ: Öneri listesi oluştur
```

## Chiller Analizi Karar Ağacı

```
BAŞLA: Chiller analizi
│
├── COP < benchmark?
│   ├── Santrifüj: benchmark COP > 5.5
│   ├── Vidalı: benchmark COP > 4.5
│   └── Scroll: benchmark COP > 4.0
│
├── COP düşükse:
│   ├── Kondenser suyu sıcak (>35°C)?
│   │   └── OKU: solutions/condenser_optimization.md
│   ├── Evaporatör ΔT yüksek (>7°C)?
│   │   └── OKU: solutions/evaporator_cleaning.md
│   └── Kısmi yükte mi çalışıyor?
│       └── OKU: solutions/vsd_chiller.md
│
└── SONUÇ: Öneri listesi
```

## Pompa Analizi Karar Ağacı

```
BAŞLA: Pompa analizi
│
├── Wire-to-water verimi < 50%?
│   ├── EVET → Düşük sistem verimi
│   │   ├── Throttle kontrol var mı?
│   │   │   └── EVET → OKU: solutions/vsd.md (Yüksek öncelik)
│   │   ├── Pompa verimi < 70%?
│   │   │   └── EVET → OKU: solutions/pump_replacement.md
│   │   └── Motor verimi < 90%?
│   │       └── OKU: solutions/motor_upgrade.md
│   │
│   └── HAYIR → Kabul edilebilir
│       └── Bakım ve izleme öner
│
├── VSD yok ve değişken debi?
│   └── OKU: solutions/vsd.md
│
└── SONUÇ: Öneri listesi
```

## Fabrika Analizi Karar Ağacı

```
BAŞLA: Fabrika analizi
│
├── Hotspot belirleme
│   └── Kayıp sıralaması yap, en büyük 3'e odaklan
│
├── Cross-equipment fırsatları
│   ├── Kompresör + Kazan var mı?
│   │   └── EVET → OKU: factory/cross_equipment.md (Atık ısı)
│   ├── Kazan + Soğutma ihtiyacı var mı?
│   │   └── EVET → OKU: factory/cogeneration.md (Absorption chiller)
│   └── Chiller + Isıtma ihtiyacı var mı?
│       └── EVET → OKU: factory/heat_integration.md (Kondenser ısısı)
│
├── Sektör bilgisi
│   └── OKU: factory/sector_{sector}.md
│
├── Ekonomik analiz
│   └── OKU: factory/prioritization.md
│   └── Quick wins vs Strategic projects ayır
│
└── SONUÇ: Önceliklendirilmiş aksiyon planı
```

## Önceliklendirme Matrisi

| ROI | Karmaşıklık | Öncelik |
|-----|-------------|---------|
| < 1 yıl | Düşük | Yüksek (Quick Win) |
| < 1 yıl | Yüksek | Yüksek |
| 1-3 yıl | Düşük | Orta |
| 1-3 yıl | Yüksek | Orta |
| > 3 yıl | Düşük | Düşük |
| > 3 yıl | Yüksek | Düşük |
```

#### skills/equipment/compressor_expert.md

```markdown
---
skill_id: compressor_expert
version: 1.0
type: equipment
equipment_type: compressor
triggers:
  - single_equipment_analysis
  - equipment_type == "compressor"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/compressor/benchmarks.md
  - knowledge/compressor/formulas.md
  - knowledge/compressor/audit.md
  - knowledge/compressor/equipment/*.md
  - knowledge/compressor/solutions/*.md
---

# Kompresör Uzmanı

## Uzmanlık Alanı

Basınçlı hava sistemleri exergy analizi:
- Vidalı (screw), pistonlu, santrifüj kompresörler
- VSD, yük kontrolü, kaçak tespiti
- Atık ısı geri kazanımı
- Basınç optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Spesifik güç | kW / (m³/min) | < 6.5 (7 bar) |
| Exergy verimi | Ex_out / Ex_in | > 50% |
| Kaçak oranı | Yük-boşta analizi | < 15% |
| Yük faktörü | Gerçek/Nominal | > 60% |

## Özel Kurallar

### Spesifik Güç Değerlendirmesi
```
7 bar için:
- < 6.0 kW/(m³/min): Mükemmel
- 6.0-6.5: İyi
- 6.5-7.5: Ortalama
- > 7.5: Kötü

Her +1 bar için +0.5 kW/(m³/min) ekle
```

### VSD Önerisi Koşulları
```
VSD öner eğer:
- Yük faktörü < 70% VE
- Çalışma saati > 4000 saat/yıl VE
- Motor gücü > 15 kW
```

### Atık Isı Potansiyeli
```
Geri kazanılabilir ısı = Motor gücü × 0.90 × 0.75
(Elektriğin %90'ı ısıya, bunun %75'i geri kazanılabilir)
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Kaçak tamiri | %10-30 enerji | Düşük | < 0.5 yıl |
| VSD retrofit | %15-35 enerji | €200-400/kW | 1-3 yıl |
| Basınç düşürme | %7/bar | Düşük | < 0.3 yıl |
| Atık ısı geri kazanım | €300-500/kW termal | €200-400/kW | 1-2 yıl |

## Yanıt Örneği

```json
{
  "summary": "37 kW vidalı kompresör %58 exergy verimi ile kabul edilebilir seviyede çalışıyor ancak atık ısı geri kazanım potansiyeli değerlendirilmeli.",
  "key_findings": [
    {
      "finding": "Spesifik güç 6.8 kW/(m³/min) ile sektör ortalamasında",
      "severity": "medium",
      "evidence": "37 kW / 5.4 m³/min = 6.85"
    }
  ],
  "recommendations": [
    {
      "title": "Atık Isı Geri Kazanımı",
      "priority": "high",
      "description": "Kompresör atık ısısı (~25 kW termal) kazan besleme suyu ön ısıtması için kullanılabilir",
      "annual_savings_eur": 6000,
      "investment_eur": 12000,
      "payback_years": 2.0
    }
  ]
}
```
```

#### skills/equipment/boiler_expert.md

```markdown
---
skill_id: boiler_expert
version: 1.0
type: equipment
equipment_type: boiler
triggers:
  - single_equipment_analysis
  - equipment_type == "boiler"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/boiler/benchmarks.md
  - knowledge/boiler/formulas.md
  - knowledge/boiler/audit.md
  - knowledge/boiler/equipment/*.md
  - knowledge/boiler/solutions/*.md
---

# Kazan Uzmanı

## Uzmanlık Alanı

Buhar ve sıcak su kazanları exergy analizi:
- Ateş borulu, su borulu kazanlar
- Yanma optimizasyonu
- Ekonomizer, hava ön ısıtıcı
- Blowdown, kondensat geri dönüş

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Enerji verimi | Q_buhar / Q_yakıt | > 88% |
| Exergy verimi | Ex_buhar / Ex_yakıt | > 38% |
| Baca gazı sıcaklığı | Ölçüm | < 180°C |
| Fazla hava | O2 veya CO2 ölçümü | 10-15% |
| Blowdown oranı | | < 3% |

## Özel Kurallar

### Exergy Verimi Değerlendirmesi
```
Buhar kazanı için:
- > 40%: İyi
- 35-40%: Ortalama
- 30-35%: Düşük
- < 30%: Kritik (acil müdahale)

Not: Exergy verimi her zaman enerji veriminden düşüktür!
Tipik: Enerji %88 iken Exergy %35
```

### Ekonomizer Önerisi
```
Ekonomizer öner eğer:
- Baca gazı sıcaklığı > 180°C VE
- Kazan kapasitesi > 1 ton/h buhar
- ROI genellikle < 1.5 yıl
```

### Yanma Optimizasyonu
```
O2 seviyesi kontrolü:
- < 2%: Eksik yanma riski
- 2-4%: Optimum
- > 5%: Fazla hava kaybı

Her %1 fazla hava ≈ %0.5 verim kaybı
```

## Exergy Kayıp Dağılımı (Tipik)

| Kayıp Kaynağı | Oran |
|---------------|------|
| Yanma irreversibility | 25-30% |
| Baca gazı kaybı | 8-15% |
| Isı transferi irreversibility | 5-10% |
| Blowdown | 1-3% |
| Radyasyon | 1-2% |

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Ekonomizer | %3-6 yakıt | €20-40K | 0.8-1.5 yıl |
| O2 trim | %1-3 yakıt | €5-15K | 0.5-1 yıl |
| Blowdown heat recovery | %1-2 yakıt | €5-10K | 1-2 yıl |
| Kondensat geri dönüş | %1/her %10 artış | Değişken | 0.5-1 yıl |
| İzolasyon | %1-2 | €3-8K | 0.5-1 yıl |
```

#### skills/equipment/chiller_expert.md

```markdown
---
skill_id: chiller_expert
version: 1.0
type: equipment
equipment_type: chiller
triggers:
  - single_equipment_analysis
  - equipment_type == "chiller"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
knowledge_files:
  - knowledge/chiller/benchmarks.md
  - knowledge/chiller/formulas.md
  - knowledge/chiller/equipment/*.md
  - knowledge/chiller/solutions/*.md
---

# Chiller Uzmanı

## Uzmanlık Alanı

Soğutma sistemleri exergy analizi:
- Santrifüj, vidalı, scroll chiller
- Absorption chiller
- Free cooling
- Kondenser optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer (Santrifüj) |
|--------|--------|----------------------|
| COP | Q_soğutma / W_kompresör | > 5.5 |
| IPLV | Kısmi yük COP | > 6.5 |
| Exergy verimi | Ex_soğutma / W_kompresör | > 40% |
| kW/ton | | < 0.6 |

## COP Benchmark

| Chiller Tipi | Düşük | Ortalama | İyi | Mükemmel |
|--------------|-------|----------|-----|----------|
| Santrifüj | < 4.5 | 4.5-5.5 | 5.5-6.5 | > 6.5 |
| Vidalı | < 4.0 | 4.0-5.0 | 5.0-5.5 | > 5.5 |
| Scroll | < 3.5 | 3.5-4.5 | 4.5-5.0 | > 5.0 |
| Absorption (tek etkili) | < 0.6 | 0.6-0.7 | 0.7-0.8 | > 0.8 |

## Özel Kurallar

### Exergy Verimi Hesaplama
```
Soğutma exergy'si:
Ex_cooling = Q_cooling × (T₀/T_cold - 1)

Burada T₀ = 298 K (25°C), T_cold = soğutma sıcaklığı (K)

7°C soğutma için: (298/280 - 1) = 0.064
Yani 100 kW soğutma ≈ 6.4 kW exergy
```

### Kondenser Optimizasyonu
```
Kondenser suyu sıcaklığı her 1°C düşüşünde:
- COP %2-3 artar

Kondenser approach temperature:
- < 3°C: Mükemmel
- 3-5°C: İyi
- > 5°C: Temizlik/bakım gerekli
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Kondenser temizliği | %5-15 | Düşük | < 0.3 yıl |
| Soğutma kulesi optimizasyonu | %5-10 | €5-20K | 1-2 yıl |
| Free cooling | %20-40 | €20-50K | 2-4 yıl |
| VSD retrofit | %15-30 | €15-40K | 2-3 yıl |
| Kondenser ısı geri kazanım | €0.05/kWh | €10-25K | 2-4 yıl |
```

#### skills/equipment/pump_expert.md

```markdown
---
skill_id: pump_expert
version: 1.0
type: equipment
equipment_type: pump
triggers:
  - single_equipment_analysis
  - equipment_type == "pump"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
knowledge_files:
  - knowledge/pump/benchmarks.md
  - knowledge/pump/formulas.md
  - knowledge/pump/equipment/*.md
  - knowledge/pump/solutions/*.md
---

# Pompa Uzmanı

## Uzmanlık Alanı

Pompalama sistemleri exergy analizi:
- Santrifüj, pozitif deplasman pompalar
- VSD retrofit
- Throttle eliminasyonu
- Sistem optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Pompa verimi | P_hidrolik / P_mil | > 80% |
| Motor verimi | P_mil / P_elektrik | > 92% |
| Wire-to-water | P_hidrolik / P_elektrik | > 65% |
| Exergy verimi | ≈ Wire-to-water | > 60% |

## Özel Kurallar

### Wire-to-Water Değerlendirmesi
```
- > 70%: Mükemmel
- 60-70%: İyi
- 50-60%: Ortalama
- 40-50%: Düşük
- < 40%: Kritik (muhtemelen throttle veya aşırı boyut)
```

### VSD Tasarruf Potansiyeli
```
Affinity Laws:
- Debi ∝ Hız
- Head ∝ Hız²
- Güç ∝ Hız³

%50 debi için:
- Throttle: Güç ≈ %80-90 (vana kaybı)
- VSD: Güç ≈ %12.5-20 (kübik yasa)

Tasarruf potansiyeli: %30-70 (yük profiline bağlı)
```

### VSD Uygunluk Kriterleri
```
VSD öner eğer:
- Kontrol yöntemi = throttle VEYA bypass VE
- Motor gücü > 5 kW VE
- Değişken debi ihtiyacı var VE
- Statik head oranı < %60 (yoksa tasarruf düşük)
```

### Statik Head Uyarısı
```
Statik head / Toplam head oranı:
- < 30%: VSD çok etkili
- 30-60%: VSD etkili
- > 60%: VSD etkisi sınırlı, dikkatli değerlendir
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| VSD retrofit | %30-50 | €200-400/kW | 1-2 yıl |
| Impeller trim | %10-25 | €500-2000 | 0.5-1 yıl |
| Throttle eliminasyonu | %20-40 | Değişken | 1-2 yıl |
| Motor upgrade (IE3→IE4) | %2-4 | €100-200/kW | 3-5 yıl |
| Boru sistemi optimizasyonu | %5-15 | Değişken | 1-3 yıl |

## Throttle Analizi

```
Throttle kayıp hesabı:
P_kayıp = ρ × g × Q × ΔH_vana / 1000 (kW)

ΔH_vana = Vana basınç düşüşü (m)
```
```

#### skills/factory/factory_analyst.md

```markdown
---
skill_id: factory_analyst
version: 1.0
type: factory
triggers:
  - factory_analysis
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
  - equipment/*.md
knowledge_files:
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - knowledge/factory/factory_benchmarks.md
  - knowledge/factory/sector_*.md
---

# Fabrika Analisti

## Uzmanlık Alanı

Fabrika seviyesi exergy analizi:
- Çoklu ekipman aggregation
- Hotspot belirleme
- Cross-equipment entegrasyon
- Sektörel karşılaştırma
- Önceliklendirme

## Analiz Sırası

1. **Aggregation:** Toplam exergy giriş, çıkış, kayıp
2. **Hotspot:** En büyük kayıp kaynakları
3. **Cross-equipment:** Entegrasyon fırsatları
4. **Sektör karşılaştırma:** Benchmark
5. **Önceliklendirme:** ROI bazlı sıralama

## Fabrika Exergy Verimi Benchmark

| Sektör | Düşük | Ortalama | İyi |
|--------|-------|----------|-----|
| Çimento | < 25% | 25-35% | > 35% |
| Kimya | < 30% | 30-45% | > 45% |
| Gıda | < 15% | 15-25% | > 25% |
| Tekstil | < 20% | 20-30% | > 30% |
| Metal | < 25% | 25-40% | > 40% |
| Kağıt | < 30% | 30-45% | > 45% |

## Cross-Equipment Fırsatları

### Kompresör → Kazan
```
Potansiyel: Kompresör gücünün %50-70'i termal olarak geri kazanılabilir
Kullanım: Kazan besleme suyu ön ısıtma
Tipik ROI: 1.5-2.5 yıl
```

### Kazan → Absorption Chiller
```
Potansiyel: Baca gazı ısısı ile soğutma
Kullanım: Eşzamanlı buhar ve soğutma ihtiyacı varsa
Tipik ROI: 3-5 yıl
```

### Chiller → Sıcak Su
```
Potansiyel: Kondenser ısısının %15-20'si
Kullanım: Düşük sıcaklık ısıtma, sıcak su
Tipik ROI: 2-4 yıl
```

## Önceliklendirme Kuralları

```
Sıralama kriterleri (ağırlıklı):
1. ROI (payback) - %40
2. Mutlak tasarruf (€/yıl) - %30
3. Uygulama kolaylığı - %20
4. Risk - %10

Quick Wins (önce yap):
- ROI < 1 yıl
- Düşük yatırım
- Düşük risk

Strategic Projects (sonra planla):
- Yüksek mutlak tasarruf
- ROI 2-5 yıl
- Kapsamlı mühendislik gerektirir
```

## Sektör Bilgisi Kullanımı

Sektör biliniyorsa mutlaka `knowledge/factory/sector_{sector}.md` oku ve:
- Tipik enerji dağılımını referans al
- Sektöre özel best practice'leri öner
- BAT (Best Available Techniques) referans ver
```

#### skills/factory/integration_expert.md

```markdown
---
skill_id: integration_expert
version: 1.0
type: factory
triggers:
  - factory_analysis
  - cross_equipment_opportunities
dependencies:
  - factory/factory_analyst.md
knowledge_files:
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/heat_integration.md
  - knowledge/factory/waste_heat_recovery.md
  - knowledge/factory/pinch_analysis.md
---

# Entegrasyon Uzmanı

## Uzmanlık Alanı

Ekipmanlar arası enerji/exergy entegrasyonu:
- Atık ısı geri kazanımı
- Isı değiştirici ağı tasarımı
- Pinch analizi temelleri
- Kojenerasyon fırsatları

## Entegrasyon Matrisi

| Kaynak | Sıcaklık | Potansiyel Kullanım |
|--------|----------|---------------------|
| Kompresör atık ısısı | 70-90°C | Besleme suyu, bina ısıtma |
| Kazan baca gazı | 150-250°C | Ekonomizer, hava ön ısıtma |
| Kazan blowdown | 100-180°C | Flash tank, ön ısıtma |
| Chiller kondenser | 35-45°C | Düşük sıcaklık ısıtma |
| Fırın egzozu | 200-400°C | Buhar üretimi, ORC |

## Eşleştirme Kuralları

```
Isı transferi için:
ΔT_min = 10-20°C (minimum sıcaklık farkı)

Sıcaklık eşleştirmesi:
- Kaynak sıcaklığı > Hedef sıcaklığı + ΔT_min

Örnek:
Kompresör: 85°C
Besleme suyu: 20°C → 60°C
ΔT = 85 - 60 = 25°C > 10°C ✓ Uygun
```

## Yatırım Tahminleri

| Teknoloji | Maliyet | Birim |
|-----------|---------|-------|
| Plakali eşanjör | €100-200 | /kW |
| Ekonomizer | €150-300 | /kW |
| Heat recovery unit | €200-400 | /kW |
| Absorption chiller | €300-500 | /kW soğutma |
| ORC sistemi | €2000-4000 | /kW elektrik |

## Dikkat Edilecekler

1. **Mesafe:** Kaynak-hedef arası mesafe maliyeti artırır
2. **Senkronizasyon:** Kaynak ve hedef aynı anda mı çalışıyor?
3. **Güvenilirlik:** Entegrasyon sistem güvenilirliğini etkiler mi?
4. **Bakım:** Ek bakım ihtiyacı
5. **Legionella riski:** 25-45°C su stagnasyonu önlenmeli
```

#### skills/output/turkish_style.md

```markdown
---
skill_id: turkish_style
version: 1.0
type: output
---

# Türkçe Yazım Kuralları

## Genel İlkeler

1. **Başlıklar Türkçe:** "Öncelikli Aksiyonlar", "Sektöre Özel Bulgular"
2. **Teknik terimler:** Parantez içinde İngilizce verilebilir
   - "Ekonomizer (economizer)"
   - "Baca gazı ısı geri kazanımı (flue gas heat recovery)"
3. **Birimler:** SI sistemi
   - kW, kWh, MJ, GJ
   - °C (Celsius)
   - bar, Pa
   - m³/h, kg/h

## Sayı Formatları

- Binlik ayırıcı: nokta (1.000, 10.000)
- Ondalık ayırıcı: virgül (3,14)
- Para: € simgesi önde (€5.000)
- Yüzde: % simgesi sonra (%35)

## Cümle Yapısı

- Kısa ve net cümleler
- Aktif çatı tercih et
- Teknik ama anlaşılır

**İyi:** "Ekonomizer ekleyerek yıllık €25.000 tasarruf sağlanabilir."
**Kötü:** "Ekonomizer eklenmesi durumunda yıllık bazda yaklaşık olarak €25.000 civarında bir tasarruf sağlanması mümkün olabilecektir."

## Öneri Formatı

```
[Öneri Başlığı]
[Öncelik seviyesi]

[Açıklama - 2-3 cümle]

Yıllık Tasarruf: €X
Yatırım: €Y
Geri Ödeme: Z yıl
```

## Uyarı Formatı

```
⚠️ [Uyarı metni]
```

veya

```
Dikkat: [Uyarı metni]
```

## Kaçınılacaklar

- Aşırı teknik jargon
- Çok uzun paragraflar
- Belirsiz ifadeler ("biraz", "yaklaşık", "belki")
- İngilizce başlıklar
```

---

## 📋 BÖLÜM 3: Knowledge Index Geliştirme

### 3.1 INDEX.md Güncelleme

Mevcut `/knowledge/INDEX.md` dosyasını daha kapsamlı hale getir:

- Her dosya için kısa açıklama
- Kullanım senaryoları
- Bağımlılık ilişkileri
- Öncelik seviyeleri

### 3.2 Her Kategori İçin Alt INDEX

```
knowledge/
├── INDEX.md                    # Ana index
├── compressor/
│   ├── INDEX.md               # Kompresör index
│   ├── equipment/
│   ├── solutions/
│   └── ...
├── boiler/
│   ├── INDEX.md               # Kazan index
│   └── ...
└── factory/
    ├── INDEX.md               # Fabrika index
    └── ...
```

### 3.3 Dosya Metadata Standardizasyonu

Her MD dosyasının başına YAML frontmatter ekle:

```yaml
---
title: Vidalı Kompresör
category: equipment
equipment_type: compressor
subtype: screw
keywords:
  - vidalı kompresör
  - screw compressor
  - basınçlı hava
related_files:
  - ../benchmarks.md
  - ../solutions/vsd.md
  - ../solutions/heat_recovery.md
use_when:
  - Vidalı kompresör analizi yorumlanırken
  - VSD önerisi değerlendirilirken
priority: high
last_updated: 2026-01-31
---
```

---

## 📋 BÖLÜM 4: Prompt Optimizasyonu

### 4.1 Claude Code Service Güncelleme

`/api/services/claude_code_service.py` dosyasını optimize et:

```python
class ExergyInterpreter:
    """
    AI yorumlama servisi.
    
    Modüler skill sistemi kullanır.
    """
    
    def __init__(self):
        self.skills_cache = {}
        self.knowledge_cache = {}
    
    def _load_skills(self, analysis_type: str, equipment_type: str = None) -> str:
        """
        İlgili skill dosyalarını yükle.
        
        Sıra:
        1. Core skills (her zaman)
        2. Equipment skill (ekipman analizi ise)
        3. Factory skills (fabrika analizi ise)
        4. Output skills (her zaman)
        """
        skills = []
        
        # Core skills
        skills.append(self._load_skill("core/exergy_fundamentals.md"))
        skills.append(self._load_skill("core/response_format.md"))
        skills.append(self._load_skill("core/decision_trees.md"))
        
        # Equipment skill
        if equipment_type:
            skills.append(self._load_skill(f"equipment/{equipment_type}_expert.md"))
        
        # Factory skills
        if analysis_type == "factory":
            skills.append(self._load_skill("factory/factory_analyst.md"))
            skills.append(self._load_skill("factory/integration_expert.md"))
        
        # Output skills
        skills.append(self._load_skill("output/turkish_style.md"))
        
        return "\n\n---\n\n".join(skills)
    
    def _load_relevant_knowledge(self, analysis_type: str, equipment_type: str = None, sector: str = None) -> str:
        """
        İlgili knowledge dosyalarını yükle.
        
        Karar ağacına göre dosya seç.
        """
        files = []
        
        if equipment_type:
            files.append(f"knowledge/{equipment_type}/benchmarks.md")
            files.append(f"knowledge/{equipment_type}/formulas.md")
        
        if analysis_type == "factory":
            files.append("knowledge/factory/cross_equipment.md")
            files.append("knowledge/factory/prioritization.md")
            files.append("knowledge/factory/factory_benchmarks.md")
            
            if sector:
                files.append(f"knowledge/factory/sector_{sector}.md")
        
        # Dosyaları yükle ve birleştir
        contents = []
        for f in files:
            content = self._load_knowledge_file(f)
            if content:
                contents.append(f"## {f}\n\n{content}")
        
        return "\n\n---\n\n".join(contents)
    
    def interpret(self, analysis_type: str, equipment_type: str, subtype: str, 
                  analysis_result: dict, sector: str = None) -> dict:
        """
        Ana yorumlama fonksiyonu.
        """
        # Skills yükle
        skills_content = self._load_skills(analysis_type, equipment_type)
        
        # Knowledge yükle
        knowledge_content = self._load_relevant_knowledge(analysis_type, equipment_type, sector)
        
        # Prompt oluştur
        prompt = self._build_prompt(
            skills=skills_content,
            knowledge=knowledge_content,
            analysis_type=analysis_type,
            equipment_type=equipment_type,
            subtype=subtype,
            result=analysis_result,
            sector=sector
        )
        
        # Claude API çağır
        response = self._call_claude(prompt)
        
        return response
```

### 4.2 Caching Stratejisi

Sık kullanılan içerikleri cache'le:

```python
import hashlib
from functools import lru_cache

@lru_cache(maxsize=100)
def _load_skill(self, skill_path: str) -> str:
    """Cache'li skill yükleme."""
    full_path = f"skills/{skill_path}"
    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()

@lru_cache(maxsize=200)
def _load_knowledge_file(self, file_path: str) -> str:
    """Cache'li knowledge yükleme."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None
```

---

## 📋 BÖLÜM 5: Test ve Doğrulama

### 5.1 Skill Testleri

Her skill için test senaryosu:

```python
# tests/test_skills.py

def test_compressor_expert_skill_loaded():
    """Kompresör skill dosyası yüklenebilmeli."""
    interpreter = ExergyInterpreter()
    skill = interpreter._load_skill("equipment/compressor_expert.md")
    assert "Kompresör Uzmanı" in skill
    assert "Spesifik güç" in skill

def test_decision_tree_compressor():
    """Kompresör karar ağacı doğru çalışmalı."""
    # Low efficiency → should recommend VSD
    result = {
        "metrics": {
            "exergy_efficiency": 35,
            "specific_power": 7.5,
            "load_factor": 45
        }
    }
    interpretation = interpret_compressor("screw", result)
    assert any("VSD" in rec["title"] for rec in interpretation["recommendations"])
```

### 5.2 Integration Testleri

```python
def test_factory_analysis_cross_equipment():
    """Fabrika analizinde cross-equipment fırsatları tespit edilmeli."""
    # Kompresör + Kazan
    equipment = [
        {"type": "compressor", "power_kW": 37},
        {"type": "boiler", "capacity_ton_h": 2}
    ]
    result = analyze_factory(equipment)
    
    # Atık ısı entegrasyonu önerilmeli
    opportunities = result["integration_opportunities"]
    assert any("Kompresör" in opp["title"] and "Kazan" in opp["title"] 
               for opp in opportunities)
```

---

## 📋 BÖLÜM 6: Otonom İyileştirmeler (İsteğe Bağlı)

Bu bölümdeki iyileştirmeler **kendi insiyatifinle** yapabileceğin ek geliştirmelerdir. Brief'teki temel görevleri tamamladıktan sonra, projeyi incele ve şunları değerlendir:

### Potansiyel İyileştirme Alanları

1. **Error Handling:** Eksik veya yetersiz error handling varsa ekle
2. **Type Hints:** Python dosyalarında eksik type hint varsa ekle
3. **Docstrings:** Eksik dokümantasyon varsa tamamla
4. **Code Refactoring:** Tekrar eden kod varsa DRY prensibine göre düzenle
5. **Test Coverage:** Eksik test senaryoları varsa ekle
6. **Performance:** Yavaş çalışan kod varsa optimize et
7. **Security:** Güvenlik açığı varsa düzelt
8. **UX:** Frontend'de kullanıcı deneyimini iyileştir
9. **Knowledge Base:** Eksik veya yetersiz bilgi varsa güncelle
10. **API Documentation:** OpenAPI/Swagger dokümentasyonu eksikse ekle

### Ne Bulursan Düzelt

Projeyi incelerken fark ettiğin her türlü:
- Bug
- Eksiklik
- Optimizasyon fırsatı
- Kod kalitesi sorunu
- Dokümantasyon eksikliği

...kendi insiyatifinle düzelt.

---

## ✅ Tamamlama Kontrol Listesi

### Zorunlu Görevler:
- [ ] `/CLAUDE.md` oluşturuldu
- [ ] `/skills/README.md` oluşturuldu
- [ ] `/skills/core/` dosyaları oluşturuldu (3 dosya)
- [ ] `/skills/equipment/` dosyaları oluşturuldu (4 dosya)
- [ ] `/skills/factory/` dosyaları oluşturuldu (2 dosya)
- [ ] `/skills/output/` dosyaları oluşturuldu (1 dosya)
- [ ] Knowledge INDEX dosyaları güncellendi
- [ ] Dosya metadata (YAML frontmatter) eklendi
- [ ] `/api/services/claude_code_service.py` optimize edildi
- [ ] Testler geçiyor
- [ ] Frontend build başarılı

### Otonom İyileştirmeler:
- [ ] Bulunan bug'lar düzeltildi
- [ ] Kod kalitesi iyileştirildi
- [ ] Eksik dokümantasyon tamamlandı
- [ ] Performans optimizasyonları yapıldı
- [ ] [Diğer iyileştirmeler - listele]

### Final:
- [ ] Tüm değişiklikler commit edildi
- [ ] Commit mesajları açıklayıcı
- [ ] Push yapıldı

---

**Bu brief'i eksiksiz uygula ve projeyi kendi insiyatifinle geliştir.**
