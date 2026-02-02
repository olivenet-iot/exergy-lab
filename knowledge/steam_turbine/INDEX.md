---
title: "Buhar Türbini Bilgi Tabanı İndeks — Steam Turbine Knowledge Base Index"
category: reference
equipment_type: steam_turbine
keywords: [buhar türbini, indeks, navigasyon, CHP]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md]
use_when: ["Buhar türbini bilgi tabanı navigasyonu gerektiğinde"]
priority: high
last_updated: 2026-01-31
---
# Buhar Türbini Bilgi Tabanı İndeks

## Genel Bakış
Buhar türbini ve CHP/kojenerasyon sistemleri için exergy analizi, performans değerlendirmesi ve iyileştirme rehberi. 21 dosya, 4 alt dizin.

## Dizin Yapısı

```
steam_turbine/
├── INDEX.md                        ← Bu dosya (navigasyon haritası)
├── formulas.md                     — Exergy hesaplama formülleri [Öncelik: Yüksek]
├── benchmarks.md                   — Sektörel karşılaştırma verileri [Öncelik: Yüksek]
├── audit.md                        — Performans denetimi metodolojisi [Öncelik: Orta]
├── case_studies.md                 — Türk endüstriyel vaka çalışmaları [Öncelik: Düşük]
├── equipment/                      — Türbin tipleri (5 dosya)
│   ├── back_pressure.md            — Karşı basınçlı türbin [Öncelik: Yüksek]
│   ├── condensing.md               — Yoğuşmalı türbin [Öncelik: Yüksek]
│   ├── extraction.md               — Ara çekişli türbin [Öncelik: Orta]
│   ├── orc.md                      — Organic Rankine Cycle [Öncelik: Orta]
│   └── micro_turbine.md            — Mikro türbin / PRV ikamesi [Öncelik: Orta]
├── systems/                        — CHP/CCHP sistem konfigürasyonları (5 dosya)
│   ├── steam_turbine_chp.md        — Buhar türbini CHP [Öncelik: Yüksek]
│   ├── gas_turbine_chp.md          — Gaz türbini + HRSG CHP [Öncelik: Orta]
│   ├── engine_chp.md               — Motor CHP [Öncelik: Orta]
│   ├── trigeneration.md            — Trijenerasyon (CCHP) [Öncelik: Orta]
│   └── hrsg.md                     — HRSG (türbin perspektifi) [Öncelik: Orta]
├── solutions/                      — İyileştirme çözümleri (5 dosya)
│   ├── efficiency_improvement.md   — Verim iyileştirme [Öncelik: Yüksek]
│   ├── load_matching.md            — Yük eşleştirme [Öncelik: Yüksek]
│   ├── condensate_optimization.md  — Kondensat optimizasyonu [Öncelik: Orta]
│   ├── maintenance.md              — Bakım planlaması [Öncelik: Orta]
│   └── sizing_guide.md             — Boyutlandırma rehberi [Öncelik: Düşük]
└── economics/                      — Ekonomik analiz (3 dosya)
    ├── feasibility.md              — CHP fizibilite analizi [Öncelik: Orta]
    ├── feed_in_tariff.md           — Türkiye elektrik piyasası [Öncelik: Düşük]
    └── financing.md                — Finansman ve teşvikler [Öncelik: Düşük]
```

## Dosya Tabloları

### Çekirdek Dosyalar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `formulas.md` | Exergy, izentropik verim, CHP formülleri | Yüksek | Her analiz |
| `benchmarks.md` | Verim aralıkları, sektörel karşılaştırma | Yüksek | Performans değerlendirme |
| `audit.md` | ASME PTC 6, ölçüm, KPI | Orta | Denetim planı |
| `case_studies.md` | Türk endüstriyel vaka çalışmaları | Düşük | Referans örnekler |

### Ekipman Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `equipment/back_pressure.md` | Karşı basınçlı türbin detayları | Yüksek | BP türbin analizi |
| `equipment/condensing.md` | Yoğuşmalı türbin detayları | Yüksek | Condensing analizi |
| `equipment/extraction.md` | Çekişli türbin detayları | Orta | Extraction analizi |
| `equipment/orc.md` | ORC — düşük sıcaklık türbin | Orta | Atık ısı değerlendirme |
| `equipment/micro_turbine.md` | Mikro türbin, PRV ikamesi | Orta | Küçük ölçek analiz |

### Sistem Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `systems/steam_turbine_chp.md` | BT CHP konfigürasyonları | Yüksek | CHP analiz |
| `systems/gas_turbine_chp.md` | GT + HRSG CHP | Orta | Kombine çevrim |
| `systems/engine_chp.md` | Motor CHP | Orta | Motor CHP |
| `systems/trigeneration.md` | CCHP / Trijenerasyon | Orta | Soğutma entegrasyon |
| `systems/hrsg.md` | HRSG türbin perspektifi | Orta | HRSG tasarım |

### Çözüm Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `solutions/efficiency_improvement.md` | Verim iyileştirme yöntemleri | Yüksek | İyileştirme önerileri |
| `solutions/load_matching.md` | Termal/elektrik yük eşleştirme | Yüksek | Operasyon optimizasyonu |
| `solutions/condensate_optimization.md` | Kondensat ve feedwater | Orta | Sistem iyileştirme |
| `solutions/maintenance.md` | Bakım ve overhaul | Orta | Bakım planı |
| `solutions/sizing_guide.md` | Yeni türbin seçimi | Düşük | Fizibilite |

### Ekonomi Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `economics/feasibility.md` | CHP fizibilite analizi | Orta | Yatırım kararı |
| `economics/feed_in_tariff.md` | Elektrik piyasası, tarife | Düşük | Mevzuat |
| `economics/financing.md` | Finansman modelleri, teşvik | Düşük | Fonlama |

## Navigasyon Kuralları

### Buhar Türbini Analizi
1. `formulas.md` — Hesaplama referansı [Her zaman]
2. `benchmarks.md` — Performans karşılaştırma [Her zaman]
3. `equipment/{tip}.md` — Türbin tipi detayları [Tip biliniyorsa]
4. `solutions/*.md` — İyileştirme önerileri [Verim düşükse]

### CHP Analizi
1. `formulas.md` — CHP formülleri [Her zaman]
2. `benchmarks.md` — CHP benchmark [Her zaman]
3. `systems/{konfigürasyon}.md` — Sistem konfigürasyonu [Tip biliniyorsa]
4. `economics/feasibility.md` — Fizibilite [Yeni yatırım]
5. `../factory/cogeneration.md` — CHP temelleri [Genel bilgi gerekiyorsa]

### Atık Isı Değerlendirmesi
1. `equipment/orc.md` — Düşük sıcaklık kaynaklar
2. `equipment/micro_turbine.md` — PRV ikamesi
3. `systems/hrsg.md` — HRSG seçimi
4. `../factory/waste_heat_recovery.md` — WHR teknolojileri

## Referanslar

1. Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*. 2nd ed., Cotton Fact Inc.
2. Kehlhofer, R. et al. (2009). *Combined-Cycle Gas & Steam Turbine Power Plants*. 3rd ed., PennWell.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
4. ASME PTC 6 (2004). *Steam Turbines Performance Test Code*.
5. Horlock, J.H. (1987). *Cogeneration — Combined Heat and Power*. Krieger.
