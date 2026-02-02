---
title: "Pinch Analizi Bilgi Tabanı İndeks (Pinch Analysis Knowledge Base Index)"
category: factory
equipment_type: factory
keywords: [pinch analizi, ısı entegrasyonu, HEN, bilgi tabanı, navigasyon]
related_files: [factory/pinch_analysis.md, factory/heat_integration.md, factory/cross_equipment.md]
use_when: ["Pinch analizi bilgi tabanına erişim gerektiğinde", "Hangi pinch dosyasının yükleneceğine karar verirken"]
priority: high
last_updated: 2026-02-01
---

# Pinch Analizi Bilgi Tabanı İndeks (Pinch Analysis Knowledge Base Index)

> Son güncelleme: 2026-02-01

## Genel Bakış

Bu dizin, Linnhoff pinch analizi metodolojisinin kapsamlı bilgi tabanını içerir. Temel kavramlardan ileri uygulamalara, vaka çalışmalarından yazılım araçlarına kadar 18 dosyadan oluşur. Dosyalar tutarlı bir 5-akışlı referans problemi üzerinden örneklendirilmiştir ve birbirine çapraz referanslarla bağlıdır.

## Referans Problem (Tüm Dosyalarda Kullanılır)

```
Akış Verileri:
  H1: 270→80°C,  CP=15 kW/°C,  Q=2,850 kW
  H2: 180→40°C,  CP=25 kW/°C,  Q=3,500 kW
  H3: 150→60°C,  CP=10 kW/°C,  Q=900 kW
  C1: 30→250°C,  CP=18 kW/°C,  Q=3,960 kW
  C2: 60→200°C,  CP=12 kW/°C,  Q=1,680 kW

ΔTmin = 10°C
Pinch: 175°C (shifted) / 180°C (hot) / 170°C (cold)
QH,min = 1,800 kW
QC,min = 2,240 kW
```

## Dosya Haritası

### Çekirdek Dosyalar (Core — Faz 1)
| # | Dosya | Konu | Öncelik |
|---|-------|------|---------|
| 1 | `INDEX.md` | Bu dosya — navigasyon haritası, yükleme kuralları | HIGH |
| 2 | `fundamentals.md` | Linnhoff metodolojisi, MER hedefleri, 3 altın kural, exergy bağlantısı | HIGH |
| 3 | `composite_curves.md` | Hot/Cold composite curve oluşturma, sıcaklık aralığı yöntemi | HIGH |
| 4 | `problem_table.md` | PTA algoritması, sıcaklık kaydırma, kaskad, düzeltilmiş kaskad | HIGH |
| 5 | `grand_composite.md` | GCC oluşturma, ısı cebi, utility yerleştirme, CHP potansiyeli | HIGH |

### Tasarım ve Hedefleme Dosyaları (Design — Faz 2)
| # | Dosya | Konu | Öncelik |
|---|-------|------|---------|
| 6 | `hen_design.md` | Grid diyagramı, CP kuralları, akış bölme, tick-off, döngü kırma | HIGH |
| 7 | `targeting.md` | Enerji/alan/maliyet/eşanjör sayısı hedefleri, Bath formülü | HIGH |
| 8 | `delta_t_min.md` | ΔTmin seçimi, süperhedefleme, TAC optimizasyonu, sektörel değerler | HIGH |

### Pratik ve İleri Dosyalar (Practical — Faz 3)
| # | Dosya | Konu | Öncelik |
|---|-------|------|---------|
| 9 | `stream_data.md` | Akış verisi çıkarma, yumuşak/katı akışlar, faz değişimi, ExergyLab | MEDIUM |
| 10 | `hen_retrofit.md` | Cross-pinch tespiti, network pinch, aşamalı retrofit | MEDIUM |
| 11 | `utility_systems.md` | Çoklu utility seviyeleri, GCC ile yerleştirme, CHP, ısı pompası | MEDIUM |
| 12 | `cost_estimation.md` | Eşanjör maliyet modelleri, Bath formülü, TAC, NPV, IRR | MEDIUM |
| 13 | `batch_integration.md` | Zaman dilimi/ortalama modeli, TES, üretim programı optimizasyonu | MEDIUM |
| 14 | `total_site.md` | Total Site Analysis, site profilleri, buhar seviye optimizasyonu | MEDIUM |
| 15 | `practical_guide.md` | Proje yönetimi, veri toplama, uygulama, devreye alma, kontrol listesi | MEDIUM |
| 16 | `common_mistakes.md` | Veri/metodoloji/tasarım/uygulama hataları, tespit yöntemleri | MEDIUM |

### Referans Dosyaları (Reference — Faz 4)
| # | Dosya | Konu | Öncelik |
|---|-------|------|---------|
| 17 | `software_tools.md` | Ticari/akademik/açık kaynak araçlar, Python implementasyonu | LOW |
| 18 | `case_studies.md` | 7 sektörel vaka çalışması, karşılaştırma tablosu | LOW |

## Yükleme Kuralları (Loading Rules)

### Kural 1: Temel Pinch Sorusu
Kullanıcı pinch analizi hakkında genel bir soru sorduğunda:
```
Yükle: fundamentals.md
Opsiyonel: composite_curves.md, problem_table.md
```

### Kural 2: Enerji Hedefleme
Minimum enerji hedefleri, ΔTmin veya bileşik eğriler sorulduğunda:
```
Yükle: composite_curves.md + problem_table.md + targeting.md
Opsiyonel: delta_t_min.md, grand_composite.md
```

### Kural 3: HEN Tasarımı
Isı eşanjör ağı tasarımı veya grid diyagramı sorulduğunda:
```
Yükle: hen_design.md + fundamentals.md
Opsiyonel: hen_retrofit.md, targeting.md
```

### Kural 4: Retrofit Analizi
Mevcut tesis iyileştirmesi veya cross-pinch analizi sorulduğunda:
```
Yükle: hen_retrofit.md + practical_guide.md
Opsiyonel: cost_estimation.md, common_mistakes.md
```

### Kural 5: Utility Optimizasyonu
Utility sistemi, CHP veya ısı pompası sorulduğunda:
```
Yükle: utility_systems.md + grand_composite.md
Opsiyonel: total_site.md
```

### Kural 6: Ekonomik Analiz
Maliyet, yatırım veya TAC optimizasyonu sorulduğunda:
```
Yükle: cost_estimation.md + delta_t_min.md
Opsiyonel: targeting.md
```

### Kural 7: Vaka Çalışması / Referans
Endüstriyel örnek veya yazılım araçları sorulduğunda:
```
Yükle: case_studies.md ve/veya software_tools.md
Opsiyonel: practical_guide.md
```

### Kural 8: Kesikli Proses veya Çok-Tesisli Analiz
Batch proses veya total site sorulduğunda:
```
Yükle: batch_integration.md ve/veya total_site.md
Opsiyonel: utility_systems.md
```

## Dosyalar Arası Bağımlılık Grafiği

```
fundamentals.md ──────┬──→ composite_curves.md ──→ problem_table.md
                      │                                    │
                      │                                    ↓
                      ├──→ hen_design.md            grand_composite.md
                      │         │                          │
                      │         ↓                          ↓
                      │   hen_retrofit.md          utility_systems.md
                      │                                    │
                      ├──→ targeting.md ←──────────────────┘
                      │         │
                      │         ↓
                      ├──→ delta_t_min.md ──→ cost_estimation.md
                      │
                      ├──→ stream_data.md
                      │
                      ├──→ batch_integration.md ──→ total_site.md
                      │
                      ├──→ practical_guide.md
                      │
                      ├──→ common_mistakes.md
                      │
                      ├──→ software_tools.md
                      │
                      └──→ case_studies.md
```

## İlgili Dosyalar

- [Pinch Analizi Ana Dosyası](../pinch_analysis.md) — Temel kavramlar ve hesaplamalar
- [Isı Entegrasyonu](../heat_integration.md) — Kaynak-kullanım eşleştirme
- [Çapraz Ekipman](../cross_equipment.md) — Ekipmanlar arası fırsatlar
- [Fabrika Bilgi Tabanı İndeks](../INDEX.md) — Üst seviye navigasyon

## Referanslar

- Linnhoff, B. et al., "User Guide on Process Integration," IChemE, 1994
- Kemp, I.C., "Pinch Analysis and Process Integration," 2nd Ed., 2007
- Smith, R., "Chemical Process Design and Integration," 2nd Ed., 2016
- Klemeš, J.J., "Handbook of Process Integration," 2013
