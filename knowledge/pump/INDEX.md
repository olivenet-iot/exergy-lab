---
title: "Pompa Bilgi Tabanı İndeks (Pump Knowledge Base Index)"
category: reference
equipment_type: pump
keywords: [pompa, pompalama, indeks, navigasyon]
related_files: [knowledge/INDEX.md, knowledge/pump/formulas.md, knowledge/pump/benchmarks.md]
use_when: ["Pompa bilgi tabanı navigasyonu gerektiğinde"]
priority: high
last_updated: 2026-02-02
---
# Pompa Bilgi Tabanı İndeks

## Genel Bakış
Pompalama sistemleri exergy analizi için kapsamlı bilgi tabanı.

## Dosya Listesi

### Temel Dosyalar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `formulas.md` | Pompa exergy hesaplama formülleri, wire-to-water | Yüksek | Her pompa analizinde |
| `benchmarks.md` | Pompa verim benchmark verileri | Yüksek | Değerlendirme ve sınıflandırma |
| `audit.md` | Pompalama sistemi denetim metodolojisi | Orta | Denetim planlama |

### Ekipman Dosyaları (`equipment/`)
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `systems_overview.md` | Pompa sistemine genel bakış | Genel bilgi |
| `centrifugal.md` | Santrifüj pompa detayları | subtype=centrifugal analizi |
| `positive_displacement.md` | Pozitif deplasmanlı pompa | subtype=positive_displacement analizi |
| `submersible.md` | Dalgıç pompa | subtype=submersible analizi |
| `vertical_turbine.md` | Dikey türbin pompa | subtype=vertical_turbine analizi |
| `booster.md` | Hidrofor | subtype=booster analizi |
| `vacuum.md` | Vakum pompası | subtype=vacuum analizi |
| `axial_mixed.md` | Eksenel/karışık akış pompası | subtype=axial analizi |
| `motors_drives.md` | Motor ve sürücü bilgileri | Motor verimi değerlendirmesi |

### Çözüm Dosyaları (`solutions/`)
| Dosya | Açıklama | Öncelik | Tetikleyici |
|-------|----------|---------|-------------|
| `vsd.md` | Değişken hız sürücü | Yüksek | Throttle kontrol, değişken debi |
| `impeller_trimming.md` | Çark tornalama | Yüksek | Fazla kapasite, sabit debi |
| `right_sizing.md` | Doğru boyutlandırma | Orta | Pompa aşırı boyutlu |
| `parallel_operation.md` | Paralel çalışma optimizasyonu | Orta | Çoklu pompa sistemi |
| `system_optimization.md` | Sistem optimizasyonu | Orta | Boru kayıpları yüksek |
| `motor_upgrade.md` | Motor yükseltme (IE3→IE4) | Düşük | Eski motor, düşük verim |
| `maintenance.md` | Bakım optimizasyonu | Orta | Verim düşüşü |
| `throttle_elimination.md` | Kısma vanası eliminasyonu | Yüksek | Throttle kontrol var |
| `cavitation_prevention.md` | Kavitasyon önleme | Yüksek | NPSH sorunu |
| `control_optimization.md` | Kontrol sistemi optimizasyonu | Orta | Manuel kontrol |

## Navigasyon Kuralları
1. Her analiz `formulas.md` + `benchmarks.md` ile başlar
2. Alt tip biliniyorsa `equipment/{subtype}.md` oku
3. Motor bilgisi için `equipment/motors_drives.md` referans al
4. Benchmark sonucuna göre ilgili `solutions/*.md` dosyalarına git
5. Throttle kontrol varsa `solutions/throttle_elimination.md` öncelikli

## Referanslar

1. Europump & Hydraulic Institute (2004). *Variable Speed Pumping: A Guide to Successful Applications*. Elsevier.
2. Karassik, I.J. et al. (2008). *Pump Handbook*. 4th ed., McGraw-Hill.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
4. ISO 9906 (2012). *Rotodynamic pumps — Hydraulic performance acceptance tests*.
