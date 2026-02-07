---
title: "Proses Bilgi Tabanı İndeks (Process Knowledge Base Index)"
category: factory
equipment_type: factory
keywords: [proses, process, gap analysis, boşluk analizi, BAT, ESI, sürdürülebilirlik, bilgi tabanı, navigasyon]
related_files: [factory/INDEX.md, factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/factory_benchmarks.md]
use_when: ["Proses seviyesi bilgi tabanı navigasyonu gerektiğinde", "Proses boşluk analizi başlatılacakken"]
priority: high
last_updated: 2026-02-08
---

# Proses Bilgi Tabanı İndeks (Process Knowledge Base Index)

## Genel Bakış

Proses seviyesi exergy boşluk analizi (Process Gap Analysis) için bilgi tabanı. 8 endüstriyel proses tipi, 3 temel kavram dosyası ve bu indeks dosyasından oluşur. Her proses dosyası termodinamik minimum, BAT referansı, ESI değerlendirmesi ve AI yorumlama kuralları içerir.

---

## Dosya Listesi

### Temel Kavram Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `gap_analysis_methodology.md` | 3 katmanlı boşluk modeli, formüller, çözümlü örnek | Yüksek | Her proses analizinde temel referans |
| `bat_overview.md` | BAT kavramı, EU BREF sistemi, exergy dönüşümü | Yüksek | BAT değerleri yorumlanırken |
| `sustainability_index.md` | ESI tanımı, A-F derecelendirme, sektörel tipik değerler | Yüksek | ESI sonuçları yorumlanırken |

### Proses Dosyaları
| Dosya | Proses | Tipik ESI | İlgili Ekipman |
|-------|--------|-----------|----------------|
| `heating.md` | Isıtma (kazan/brülör) | 0.10 – 0.35 | Kazan (boiler) |
| `steam_generation.md` | Buhar üretimi | 0.20 – 0.35 | Kazan (boiler) |
| `compressed_air.md` | Basınçlı hava | 0.05 – 0.15 | Kompresör (compressor) |
| `cooling.md` | Soğutma | 0.10 – 0.45 | Chiller |
| `cold_storage.md` | Soğuk depolama | 0.08 – 0.55 | Chiller, soğutma sistemi |
| `drying.md` | Kurutma | 0.03 – 0.25 | Kurutucu (dryer) |
| `chp.md` | CHP/Kojenerasyon | 0.25 – 0.55 | Buhar türbini, gaz türbini |
| `general_manufacturing.md` | Çimento, cam, kağıt, şeker | 0.08 – 0.28 | Çoklu ekipman |

---

## Navigasyon Senaryoları

### Senaryo 1: Tek Proses Boşluk Analizi
1. `gap_analysis_methodology.md` oku (formüller)
2. `sustainability_index.md` oku (ESI derecelendirme)
3. İlgili proses dosyasını oku (ör. `heating.md`)
4. Varsa ilgili ekipman benchmark dosyasını oku (ör. `boiler/benchmarks.md`)

### Senaryo 2: BAT Referans Sorgulama
1. `bat_overview.md` oku (BREF sistemi)
2. İlgili proses dosyasının §4 BAT Referansı bölümünü oku
3. BAT güvenilirlik seviyesini kontrol et

### Senaryo 3: Çoklu Proses Karşılaştırması
1. `gap_analysis_methodology.md` oku
2. `sustainability_index.md` oku (ağırlıklı ESI hesabı, §6.3)
3. Her proses dosyasını oku
4. `factory/factory_benchmarks.md` ile sektörel karşılaştırma yap

### Senaryo 4: Fabrika Entegrasyonu
1. Proses bazlı analiz yap (yukarıdaki senaryolar)
2. `factory/cross_equipment.md` oku (ekipmanlar arası fırsatlar)
3. `factory/heat_integration.md` oku (ısı entegrasyonu)
4. `factory/pinch/INDEX.md` oku (pinch analizi gerekiyorsa)

### Senaryo 5: AI Yorumlama
1. Proses dosyasının §7 Yorumlama Rehberi bölümünü oku
2. `sustainability_index.md`'den ESI derecelendirmesini al
3. Sektörel bağlamı dikkate al
4. İyileştirme stratejilerini sırala

---

## Bağımlılık Grafiği

```
gap_analysis_methodology.md
  ├── sustainability_index.md (ESI tanımı)
  ├── bat_overview.md (BAT kavramı)
  │
  ├── heating.md
  │     └── → boiler/benchmarks.md
  ├── steam_generation.md
  │     ├── → boiler/benchmarks.md
  │     └── → chp.md
  ├── compressed_air.md
  │     └── → compressor/benchmarks.md
  ├── cooling.md
  │     ├── → chiller/benchmarks.md
  │     └── → cold_storage.md
  ├── cold_storage.md
  │     └── → chiller/benchmarks.md
  ├── drying.md
  │     └── → dryer/benchmarks.md
  ├── chp.md
  │     └── → steam_turbine/systems/
  └── general_manufacturing.md
        ├── → factory/sector_cement.md
        ├── → factory/sector_paper.md
        └── → factory/sector_food.md
```

---

## ESI Hızlı Referans Tablosu

| Proses | ESI < (Kötü) | ESI ≈ (Orta) | ESI > (İyi) |
|--------|-------------|-------------|-------------|
| Isıtma (düşük T) | 0.08 | 0.10-0.12 | 0.15 |
| Isıtma (yüksek T) | 0.25 | 0.30-0.35 | 0.40 |
| Buhar üretimi | 0.25 | 0.28-0.32 | 0.35 |
| Basınçlı hava | 0.05 | 0.07-0.10 | 0.12 |
| Soğutma (7 °C) | 0.20 | 0.25-0.35 | 0.40 |
| Soğuk depo (−20 °C) | 0.15 | 0.20-0.30 | 0.35 |
| Kurutma | 0.04 | 0.06-0.10 | 0.15 |
| CHP | 0.30 | 0.35-0.45 | 0.50 |
| Çimento | 0.10 | 0.15-0.20 | 0.25 |
| Cam | 0.08 | 0.12-0.18 | 0.20 |
| Kağıt | 0.12 | 0.18-0.22 | 0.25 |

---

## İlgili Dosyalar

- `factory/INDEX.md` — Fabrika bilgi tabanı ana indeks
- `factory/factory_benchmarks.md` — Fabrika seviyesi benchmark
- `factory/cross_equipment.md` — Ekipmanlar arası entegrasyon
- `skills/factory/process_analyst.md` — Proses analisti skill dosyası

## Referanslar

1. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
2. European Commission, JRC. BREF Document Series — www.eippcb.jrc.ec.europa.eu/reference
