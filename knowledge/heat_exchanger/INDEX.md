---
title: "Isı Eşanjörü Bilgi Tabanı İndeks (Heat Exchanger Knowledge Base Index)"
category: reference
equipment_type: heat_exchanger
keywords: [ısı eşanjörü, heat exchanger, indeks, navigasyon]
related_files: [knowledge/INDEX.md, knowledge/heat_exchanger/formulas.md, knowledge/heat_exchanger/benchmarks.md]
use_when: ["Isı eşanjörü bilgi tabanı navigasyonu gerektiğinde"]
priority: high
last_updated: 2026-02-02
---
# Isı Eşanjörü Bilgi Tabanı İndeks

## Genel Bakış

Isı eşanjörleri (heat exchangers) exergy analizi için kapsamlı bilgi tabanı.
Bu bilgi tabanı, endüstriyel ısı eşanjörlerinin termodinamik performans
değerlendirmesi, exergy yıkım analizi ve optimizasyon önerileri için
gerekli tüm referans verilerini içerir.

Isı eşanjörleri, iki veya daha fazla akışkan arasında ısı transferi sağlayan
cihazlardır. Exergy analizi açısından, ısı eşanjörlerinde iki temel
tersinmezlik kaynağı vardır:
1. **Sonlu sıcaklık farkıyla ısı transferi** — en büyük exergy yıkım kaynağı
2. **Basınç düşüşü** — pompajla ilişkili ek exergy kaybı

## Dosya Listesi

### Temel Dosyalar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `formulas.md` | Isı eşanjörü exergy hesaplama formülleri | Yüksek | Her eşanjör analizinde |
| `benchmarks.md` | Sektör karşılaştırma verileri, U-değer aralıkları | Yüksek | Değerlendirme ve sınıflandırma |
| `audit.md` | Isı eşanjörü enerji denetimi metodolojisi | Orta | Denetim planlama |
| `standards.md` | TEMA, ASME, API standartları | Orta | Tasarım ve değerlendirme |
| `case_studies.md` | Uygulama örnekleri ve vaka çalışmaları | Düşük | Referans ve karşılaştırma |

### Ekipman Dosyaları (`equipment/`)
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `systems_overview.md` | Isı eşanjörü sistemlerine genel bakış | Genel bilgi |
| `shell_and_tube.md` | Gövde-boru (shell & tube) eşanjörler | subtype=shell_and_tube analizi |
| `plate.md` | Plakalı eşanjörler (plate heat exchangers) | subtype=plate analizi |
| `air_cooled.md` | Hava soğutmalı eşanjörler (air-cooled HX) | subtype=air_cooled analizi |
| `double_pipe.md` | Çift borulu eşanjörler (double pipe) | subtype=double_pipe analizi |
| `spiral.md` | Spiral eşanjörler | subtype=spiral analizi |
| `economizer.md` | Ekonomizerler (boiler economizers) | subtype=economizer analizi |
| `air_preheater.md` | Hava ön ısıtıcıları (air preheaters) | subtype=air_preheater analizi |
| `recuperator.md` | Reküperatörler/rejeneratörler | subtype=recuperator analizi |

### Çözüm Dosyaları (`solutions/`)
| Dosya | Açıklama | Öncelik | Tetikleyici |
|-------|----------|---------|-------------|
| `fouling_management.md` | Kirlenme (fouling) yönetimi | Yüksek | U-değer düşüşü > %20 |
| `approach_temp.md` | Yaklaşım sıcaklığı optimizasyonu | Yüksek | ΔT_approach > 15°C |
| `pressure_drop.md` | Basınç düşüşü azaltma | Orta | ΔP > tasarım değerinin %130'u |
| `heat_recovery.md` | Isı geri kazanım uygulamaları | Yüksek | Atık ısı > 50 kW |
| `retrofit.md` | Mevcut eşanjör iyileştirme | Orta | Performans düşüşü |
| `material_selection.md` | Malzeme seçimi rehberi | Düşük | Korozyon/erozyon sorunları |

## Eşanjör Tipi Seçim Rehberi

Akışkan kombinasyonu ve proses koşullarına göre uygun eşanjör tipi seçimi:

| Akışkan Kombinasyonu | Önerilen Tip | Alternatif | Referans Dosya |
|----------------------|-------------|-----------|----------------|
| Sıvı – Sıvı (temiz) | Plakalı | Gövde-boru | `equipment/plate.md` |
| Sıvı – Sıvı (kirli/viskoz) | Gövde-boru | Spiral | `equipment/shell_and_tube.md` |
| Gaz – Sıvı (baca gazı → su) | Ekonomizer (finli boru) | Gövde-boru | `equipment/economizer.md` |
| Gaz – Gaz (baca gazı → hava) | Reküperatör / Hava ön ısıtıcı | Isı tekeri | `equipment/recuperator.md` |
| Buhar – Sıvı (yoğuşma) | Gövde-boru | Plakalı | `equipment/shell_and_tube.md` |
| Yüksek basınç (>25 bar) | Gövde-boru / Çift borulu | — | `equipment/double_pipe.md` |
| Küçük kapasite (<50 kW) | Çift borulu | Plakalı | `equipment/double_pipe.md` |
| Yüksek sıcaklık (>400°C) | Reküperatör | Gövde-boru (alaşım) | `equipment/recuperator.md` |
| Alan kısıtı (kompakt gerek) | Plakalı | Spiral | `equipment/plate.md` |
| Kolay temizlik gerekli | Plakalı | Gövde-boru (U-tube) | `equipment/plate.md` |

## Navigasyon Kuralları

1. Her analiz `formulas.md` + `benchmarks.md` ile başlar
2. Alt tip biliniyorsa `equipment/{subtype}.md` oku
3. Standart gerekiyorsa `standards.md` referans al
4. Benchmark sonucuna göre ilgili `solutions/*.md` dosyalarına git

## Karar Ağacı

```
Eşanjör analizi başlat
  |
  +-- formulas.md oku (exergy hesaplamaları)
  +-- benchmarks.md oku (performans değerlendirmesi)
  |
  +-- Alt tip biliniyor mu?
  |     |-- Evet --> equipment/{subtype}.md oku
  |     |-- Hayır --> equipment/systems_overview.md oku
  |
  +-- Performans değerlendirmesi:
        |-- U-değer düşüşü > %20 --> solutions/fouling_management.md
        |-- ΔT_approach > 15°C --> solutions/approach_temp.md
        |-- ΔP fazla --> solutions/pressure_drop.md
        |-- Atık ısı > 50 kW --> solutions/heat_recovery.md
        |-- Genel performans düşüşü --> solutions/retrofit.md
        |-- Korozyon/erozyon --> solutions/material_selection.md
```

## Exergy Analizi Özel Notlar

Isı eşanjörlerinde exergy verimi tipik olarak %20-80 arasındadır. Bu geniş
aralık, sıcaklık farkı ve akışkan kombinasyonuna bağlı olarak büyük değişkenlik
gösterir. Düşük sıcaklık farkı ile çalışan eşanjörler yüksek exergy verimi
sağlar, ancak bu durum daha büyük transfer yüzey alanı gerektirir — klasik
termodinamik-ekonomi ödünleşimi (trade-off).

Enerji verimi ile exergy verimi arasındaki fark:
- **Enerji verimi (ε):** Q_cold / Q_hot — genellikle >%95 (kayıpsız izolasyon)
- **Exergy verimi (η_ex):** 1 - T₀·S_gen/(Ex_hot_in - Ex_hot_out) — tipik %30-70

Bu büyük fark, ısı transferi sırasında sıcaklık kalitesinin (exergy) kaybolmasından
kaynaklanır. Yüksek sıcaklıktan düşük sıcaklığa ısı aktarımı sırasında entropik
ısı üretimi kaçınılmaz bir tersinmezliktir.

### Tipik Exergy Verimi Aralıkları (Eşanjör Tipine Göre)

| Eşanjör Tipi | Düşük | Ortalama | İyi | En İyi |
|--------------|-------|----------|-----|--------|
| Gövde-boru | < %25 | %25-40 | %40-55 | > %55 |
| Plakalı | < %30 | %30-45 | %45-60 | > %60 |
| Hava soğutmalı | < %15 | %15-25 | %25-35 | > %35 |
| Ekonomizer | < %20 | %20-35 | %35-50 | > %50 |
| Reküperatör | < %30 | %30-45 | %45-60 | > %60 |

## Fabrika Seviyesi Entegrasyon

Isı eşanjörleri, fabrika seviyesi enerji optimizasyonunda merkezi bir rol oynar.
Eşanjör performansı doğrudan ısı entegrasyonu ve atık ısı geri kazanım
verimliliğini etkiler.

- **Isı entegrasyonu:** Eşanjör ağları (HEN) ile proses akışları arasında
  ısı alışverişi — `../factory/heat_integration.md`
- **Atık ısı geri kazanım:** Ekonomizer, reküperatör ve ısı geri kazanım
  sistemleri — `../factory/waste_heat_recovery.md`
- **Ekipmanlar arası optimizasyon:** Kompresör atık ısısı → eşanjör →
  kazan besleme suyu gibi çapraz entegrasyonlar — `../factory/cross_equipment.md`
- **Pinch analizi:** Minimum yaklaşım sıcaklığı ve eşanjör ağı tasarımı —
  `../factory/pinch_analysis.md`

## İlgili Dosyalar

### Isı Eşanjörü Bilgi Tabanı (Bu Dizin)
- `formulas.md` — Exergy hesaplama formülleri
- `benchmarks.md` — Performans karşılaştırma verileri
- `audit.md` — Denetim metodolojisi
- `standards.md` — TEMA, ASME, API standartları
- `case_studies.md` — Uygulama vaka çalışmaları

### Fabrika Seviyesi
- `../factory/heat_integration.md` — Isı entegrasyonu ve kaynak-kullanım eşleştirme
- `../factory/waste_heat_recovery.md` — Atık ısı geri kazanım teknolojileri
- `../factory/cross_equipment.md` — Ekipmanlar arası optimizasyon fırsatları
- `../factory/pinch_analysis.md` — Pinch analizi

### Diğer Ekipmanlar
- `../boiler/solutions/economizer.md` — Kazan ekonomizer detayları
- `../compressor/solutions/heat_recovery.md` — Kompresör atık ısı geri kazanım

## Referanslar

1. Shah, R.K. & Sekulic, D.P. (2003). *Fundamentals of Heat Exchanger Design*. Wiley.
2. Kakac, S., Liu, H. & Pramuanjaroenkij, A. (2012). *Heat Exchangers: Selection, Rating, and Thermal Design*. 3rd ed., CRC Press.
3. TEMA (2019). *Standards of the Tubular Exchanger Manufacturers Association*. 10th ed.
4. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
5. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press.
6. Incropera, F.P. & DeWitt, D.P. (2011). *Fundamentals of Heat and Mass Transfer*. 7th ed., Wiley.
7. ASME PTC 12.5 (2000). *Single Phase Heat Exchangers Performance Test Code*.
8. Linnhoff, B. et al. (1982). *User Guide on Process Integration for the Efficient Use of Energy*. IChemE.
