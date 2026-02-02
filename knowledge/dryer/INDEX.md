---
title: "Kurutma Fırını Bilgi Tabanı İndeksi (Dryer Knowledge Base Index)"
category: dryer
equipment_type: dryer
keywords: [kurutma fırını, dryer, index, navigasyon]
related_files: [knowledge/INDEX.md]
use_when: ["Kurutma fırını bilgi tabanı gezinirken"]
priority: high
last_updated: 2026-02-01
---
# Kurutma Fırını Bilgi Tabanı (Industrial Dryer Knowledge Base)

AI navigasyon haritası. Bu dosya, kurutma fırını bilgi tabanının yapısı ve kullanım kuralları hakkında rehberlik sağlar.

## Dizin Yapısı

```
knowledge/dryer/
├── INDEX.md                    ← Bu dosya
├── formulas.md                 — Kurutma exergy hesaplama formülleri [Öncelik: Yüksek]
├── benchmarks.md               — Tip/sektör karşılaştırma verileri [Öncelik: Yüksek]
├── psychrometrics.md           — Nemli hava termodinamiği [Öncelik: Yüksek]
├── audit.md                    — Kurutma fırını enerji denetimi [Öncelik: Orta]
├── case_studies.md             — Uygulama vaka çalışmaları [Öncelik: Düşük]
├── equipment/                  — Kurutucu tipleri (8 dosya)
│   ├── tunnel_dryer.md         — Tünel kurutucu
│   ├── belt_dryer.md           — Bant kurutucu
│   ├── rotary_dryer.md         — Döner kurutucu
│   ├── fluidized_bed.md        — Akışkan yataklı kurutucu
│   ├── spray_dryer.md          — Sprey kurutucu
│   ├── drum_dryer.md           — Silindir kurutucu
│   ├── heat_pump_dryer.md      — Isı pompalı kurutucu
│   └── infrared_dryer.md       — Kızılötesi kurutucu
├── solutions/                  — İyileştirme çözümleri (7 dosya)
│   ├── exhaust_heat_recovery.md — Egzoz ısı geri kazanımı [Öncelik: Yüksek]
│   ├── air_recirculation.md     — Hava geri deviri [Öncelik: Yüksek]
│   ├── heat_pump_retrofit.md    — Isı pompası retrofit
│   ├── mechanical_dewatering.md — Mekanik ön su alma [Öncelik: Yüksek]
│   ├── insulation.md            — Yalıtım iyileştirmesi
│   ├── temperature_optimization.md — Sıcaklık optimizasyonu
│   └── solar_preheating.md      — Güneş ön ısıtma
└── sectors/                    — Sektörel uygulama rehberleri (5 dosya)
    ├── food_drying.md           — Gıda kurutma uygulamaları
    ├── paper_drying.md          — Kağıt/selüloz kurutma
    ├── textile_drying.md        — Tekstil kurutma
    ├── ceramic_drying.md        — Seramik kurutma
    └── wood_drying.md           — Kereste kurutma fırınları
```

## Navigasyon Kuralları

### Tekil Kurutma Fırını Yorumlama
Tek bir kurutma fırını analiz edildiğinde:
1. `knowledge/dryer/formulas.md` — Hesaplama referansı [Öncelik: Yüksek]
2. `knowledge/dryer/benchmarks.md` — SMER ve verim karşılaştırma [Öncelik: Yüksek]
3. `knowledge/dryer/psychrometrics.md` — Nemli hava hesaplamaları [Öncelik: Yüksek]
4. `knowledge/dryer/equipment/{subtype}.md` — Kurutucu tipi detayları [Öncelik: Orta]
5. `knowledge/dryer/solutions/*.md` — İlgili çözümler [Öncelik: Orta]
6. `knowledge/dryer/sectors/{sector}.md` — Sektörel bilgi [Öncelik: Düşük]

### Fabrika Seviyesi Entegrasyon
Kurutma fırını fabrika analizinde yer aldığında:
1. `knowledge/factory/cross_equipment.md` — Kazan/kompresör atik isisi ile kurutma entegrasyonu
2. `knowledge/factory/heat_integration.md` — Kurutma egzozu isi kaynagi olarak
3. `knowledge/factory/waste_heat_recovery.md` — WHR teknolojileri
4. `knowledge/factory/pinch_analysis.md` — Pinch analizi ile kurutma entegrasyonu

### Oncelik Sirasi
- **Guvenlik uyarilari** her zaman en ustte (patlama, yangin riski)
- **Yuksek exergy yikimi** olan kurutucular once degerlendirilir
- **Mekanik on su alma** termal kurutmadan once degerlendirilir (en dusuk exergy maliyeti)
- **Egzoz isi geri kazanimi** ve **hava geri deviri** standart oncelikli cozumlerdir
- **ROI < 2 yil** olan yatirimlar "high" oncelik alir

## Bagimlilik Iliskileri

```
psychrometrics.md ──→ formulas.md       : Psikrometri kurutma hesaplarini besler
formulas.md ────────→ benchmarks.md     : Formuller benchmark degerlendirmesinin temelidir
benchmarks.md ──────→ solutions/*.md    : Benchmark sonucu cozum secimini yonlendirir
audit.md ───────────→ equipment/*.md    : Denetim surecinde ekipman bilgisi gerekir
equipment/*.md ─────→ sectors/*.md      : Ekipman tipi sektorel uygulamaya baglidir
solutions/*.md ─────→ case_studies.md   : Cozum onerileri vaka calismalari ile dogrulanir
```

- `psychrometrics.md` diger tum dosyalar icin temel referanstir; nemli hava ozellikleri olmadan kurutma exergy hesabi yapilamaz
- `formulas.md` ve `benchmarks.md` birlikte yuklenmeli — verim siniflandirmasi icin her ikisi de gerekir
- `sectors/*.md` dosyalari bagimsiz okunabilir ancak `equipment/*.md` ile birlikte daha etkilidir

## Kurutma Exergy Analizi Ozeti

### Temel Metrikler
| Metrik | Aciklama | Birim |
|--------|----------|-------|
| SMER | Specific Moisture Extraction Rate | kg su / kWh |
| SEC | Specific Energy Consumption | kJ / kg su |
| Exergy verimi | Faydali exergy / Toplam exergy girisi | % |
| Nem alma kapasitesi | Birim zamanda uzaklastirilan su | kg/h |

### Kurutucu Tipine Gore Exergy Verim Araliklari
| Kurutucu Tipi | Exergy Verimi (%) | Tipik SMER (kg/kWh) | Tipik SEC (kJ/kg su) |
|---------------|-------------------|----------------------|----------------------|
| Tünel kurutucu | 5–15 | 0.3–0.8 | 4,500–12,000 |
| Bant kurutucu | 10–20 | 0.5–1.0 | 3,600–7,200 |
| Döner kurutucu | 8–18 | 0.4–0.9 | 4,000–9,000 |
| Akışkan yataklı | 10–25 | 0.5–1.2 | 3,000–7,200 |
| Sprey kurutucu | 5–12 | 0.2–0.6 | 6,000–18,000 |
| Silindir kurutucu | 15–30 | 0.8–1.5 | 2,400–4,500 |
| Isı pompalı kurutucu | 25–50 | 1.5–4.0 | 900–2,400 |
| Kızılötesi kurutucu | 10–20 | 0.3–0.8 | 4,500–12,000 |

### Hizli Referans
- Dusuk exergy verimi (< %10): Acil iyilestirme gerekir — `solutions/` dizinine basvur
- Orta exergy verimi (%10–25): Standart performans — optimizasyon firsatlari ara
- Yuksek exergy verimi (> %25): Iyi performans — isi pompali veya gelismis sistem

## Ilgili Ust Dizin Dosyalari

### Ana Navigasyon
- `knowledge/INDEX.md` — ExergyLab bilgi tabani ana navigasyon haritasi

### Fabrika Seviyesi Entegrasyon
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arasi entegrasyon firsatlari
- `knowledge/factory/heat_integration.md` — Isi entegrasyonu ve kurutma egzoz isisi
- `knowledge/factory/waste_heat_recovery.md` — Atik isi geri kazanim teknolojileri
- `knowledge/factory/pinch_analysis.md` — Pinch analizi ile kurutma entegrasyonu
- `knowledge/factory/cogeneration.md` — CHP atik isisi ile kurutma beslemesi

### Karar Agaci ve Beceri Dosyalari
- `skills/core/decision_trees.md` — Kurutma firini analiz karar agaci
- `skills/equipment/dryer_expert.md` — Kurutma firini AI uzman becerisi

## Dosya Sayisi Ozeti

| Kategori | Dosya Sayisi |
|----------|-------------|
| Temel referans (formulas, benchmarks, psychrometrics, audit) | 4 |
| Vaka calismalari | 1 |
| Ekipman tipleri (equipment/) | 8 |
| Cozum onerileri (solutions/) | 7 |
| Sektorel rehberler (sectors/) | 5 |
| Navigasyon (INDEX.md) | 1 |
| **Toplam** | **26** |

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*. 4th ed., CRC Press.
2. Kemp, I.C. (2012). "Fundamentals of Energy Analysis of Dryers." In: *Modern Drying Technology*, Vol. 4, Wiley.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
4. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*. 2nd ed., CRC Press.
