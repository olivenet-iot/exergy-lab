---
title: "Termoekonomik Optimizasyon İndeks (Thermoeconomic Optimization Index)"
category: thermoeconomic_optimization
keywords: [termoekonomik optimizasyon, dizin haritası, navigasyon, SPECO]
related_files: [knowledge/factory/thermoeconomic_optimization/overview.md, knowledge/factory/thermoeconomic_optimization/practical_guide.md, knowledge/factory/INDEX.md]
use_when: ["Termoekonomik optimizasyon dosyalarına genel bakış gerektiğinde", "Hangi dosyanın okunması gerektiğine karar verilirken"]
priority: high
last_updated: 2026-02-02
---

# Termoekonomik Optimizasyon - Dizin Haritası (Thermoeconomic Optimization Index)

## Genel Bakış

Bu dizin, endüstriyel sistemlerin termoekonomik optimizasyonu için kapsamlı bir bilgi tabanı sunar.
Termodinamiğin 2. yasası (exergy) ile ekonomik analizin birleştirilmesiyle elde edilen
termoekonomik optimizasyon, gerçek maliyet-verimlilik dengesini ortaya koyar.

**Kapsam:** Tek ekipman optimizasyonundan fabrika seviyesi çok amaçlı optimizasyona kadar
tüm seviyelerde termoekonomik analiz ve optimizasyon.

---

## Dosya Listesi

### Temel Kavramlar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `overview.md` | Termoekonomik optimizasyon temelleri, tarihçe, SPECO yöntemi | Yüksek | Kavramsal temel, her zaman oku |
| `objective_functions.md` | Amaç fonksiyonları, maliyet bileşenleri, CBAM | Yüksek | Maliyet formülasyonu |
| `decision_variables.md` | Karar değişkenleri, kısıtlar, sınırlar | Yüksek | Optimizasyon model kurulumu |

### Optimizasyon Yöntemleri
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `iterative_method.md` | Tsatsaronis iteratif yöntemi, f_k/r_k analizi | Yüksek | Mevcut sistemlerin iyileştirmesi |
| `structural_optimization.md` | Üst-yapı, MINLP, konfigürasyon seçimi | Orta | Yeni tesis / büyük retrofit |
| `parametric_optimization.md` | NLP, SQP, gradient tabanlı optimizasyon | Yüksek | Parametre ince ayarı |
| `multi_objective.md` | Pareto, NSGA-II, TOPSIS, çok amaçlı | Yüksek | Maliyet-verimlilik-çevre dengesi |

### Araçlar ve Teknikler
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `algorithms.md` | GA, PSO, SQP, NSGA-II, hibrit yöntemler | Orta | Algoritma seçimi |
| `sensitivity_analysis.md` | Duyarlılık, Monte Carlo, senaryo analizi | Yüksek | Belirsizlik değerlendirmesi |
| `trade_off_curves.md` | Ödünleşim eğrileri, optimal nokta seçimi | Orta | Karar destek |

### Uygulama
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `practical_guide.md` | 10 adımlı uygulama prosedürü, hatalar, tuzaklar | Yüksek | Endüstriyel uygulama |
| `case_studies.md` | Akademik ve endüstriyel vaka çalışmaları | Orta | Referans ve doğrulama |

### Hesaplanmış Örnekler (Worked Examples)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `worked_examples/boiler_optimization.md` | 3.000 kW kazan optimizasyonu | Yüksek | Tek ekipman örneği |
| `worked_examples/chp_optimization.md` | 500 kWe CHP çok amaçlı optimizasyon | Yüksek | Sistem seviyesi örnek |
| `worked_examples/factory_optimization.md` | Tekstil fabrikası portföy optimizasyonu | Yüksek | Fabrika seviyesi örnek |

---

## Navigasyon Kuralları

1. **Her termoekonomik analizde** `overview.md` ve `objective_functions.md` oku
2. **Mevcut sistem iyileştirmesi** için `iterative_method.md` + `practical_guide.md` oku
3. **Yeni tesis veya büyük retrofit** için `structural_optimization.md` + `parametric_optimization.md` oku
4. **Çok amaçlı optimizasyon** gerekiyorsa `multi_objective.md` + `trade_off_curves.md` oku
5. **Duyarlılık değerlendirmesi** için `sensitivity_analysis.md` oku
6. **Hesaplama örneği** gerektiğinde ilgili `worked_examples/` dosyasını oku
7. **Algoritma seçimi** gerektiğinde `algorithms.md` oku

## Bağlam İçi Referanslar (Cross-References)

### Bu Dizinden → Mevcut Dosyalara
- `factory/economic_analysis.md` — NPV, IRR, SPP hesaplama yöntemleri
- `factory/life_cycle_cost.md` — Yaşam döngüsü maliyet analizi
- `factory/energy_pricing.md` — Türkiye enerji fiyatları
- `factory/exergy_fundamentals.md` — Exergy temel kavramlar
- `factory/exergy_flow_analysis.md` — Exergy akış analizi
- `factory/prioritization.md` — Yatırım önceliklendirme
- `factory/cross_equipment.md` — Ekipmanlar arası fırsatlar
- `factory/cogeneration.md` — Kojenerasyon değerlendirmesi
- `factory/heat_integration.md` — Isı entegrasyonu
- `factory/pinch_analysis.md` — Pinch analizi
- `factory/data_collection.md` — Veri toplama
- `factory/methodology.md` — Analiz metodolojisi

### Bu Dizinden → Ekipman Dosyalarına
- `boiler/formulas.md`, `boiler/benchmarks.md` — Kazan referansları
- `compressor/formulas.md`, `compressor/benchmarks.md` — Kompresör referansları
- `chiller/formulas.md`, `chiller/benchmarks.md` — Chiller referansları
- `pump/formulas.md`, `pump/benchmarks.md` — Pompa referansları

### Planlanan (Henüz Oluşturulmamış) Dizinlere
- `exergoeconomic/` — Detaylı exergoekonomik analiz
- `advanced_exergy/` — İleri exergy analizi (kaçınılabilir/kaçınılamaz)

---

## Kullanım Senaryoları

### Senaryo 1: Mevcut Fabrikada Hızlı Tarama
```
overview.md → practical_guide.md (Bölüm: Yaklaşık hesaplama)
→ iterative_method.md → sensitivity_analysis.md
```

### Senaryo 2: Yeni CHP Sistemi Tasarımı
```
overview.md → objective_functions.md → decision_variables.md
→ structural_optimization.md → multi_objective.md
→ worked_examples/chp_optimization.md
```

### Senaryo 3: Kazan Parametrik Optimizasyonu
```
overview.md → objective_functions.md → decision_variables.md
→ parametric_optimization.md → sensitivity_analysis.md
→ worked_examples/boiler_optimization.md
```

### Senaryo 4: Fabrika Portföy Optimizasyonu
```
overview.md → practical_guide.md → multi_objective.md
→ trade_off_curves.md → worked_examples/factory_optimization.md
```

---

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*
- Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems"
- Lazzaretto, A. & Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology"
- El-Sayed, Y.M. (2003). *The Thermoeconomics of Energy Conversions*
