---
title: "Kompresör Bilgi Tabanı İndeks (Compressor Knowledge Base Index)"
category: reference
equipment_type: compressor
keywords: [kompresör, basınçlı hava, indeks, navigasyon]
related_files: [knowledge/INDEX.md, knowledge/compressor/formulas.md, knowledge/compressor/benchmarks.md]
use_when: ["Kompresör bilgi tabanı navigasyonu gerektiğinde"]
priority: high
last_updated: 2026-02-02
---
# Kompresör Bilgi Tabanı İndeks

## Genel Bakış
Basınçlı hava sistemleri exergy analizi için kapsamlı bilgi tabanı.

## Dosya Listesi

### Temel Dosyalar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `formulas.md` | Exergy hesaplama formülleri, spesifik güç, izotermal verim | Yüksek | Her kompresör analizinde |
| `benchmarks.md` | Sektör karşılaştırma verileri, verim aralıkları | Yüksek | Değerlendirme ve sınıflandırma |
| `audit.md` | Enerji denetimi metodolojisi, ölçüm rehberi | Orta | Denetim planlama |

### Ekipman Dosyaları (`equipment/`)
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `systems_overview.md` | Basınçlı hava sistemine genel bakış | Genel bilgi |
| `screw.md` | Vidalı kompresör detayları, çalışma prensibi | subtype=screw analizi |
| `screw_oilfree.md` | Yağsız vidalı kompresör özellikleri | subtype=screw_oilfree analizi |
| `piston.md` | Pistonlu kompresör bilgileri | subtype=piston analizi |
| `scroll.md` | Scroll kompresör bilgileri | subtype=scroll analizi |
| `centrifugal.md` | Santrifüj kompresör özellikleri | subtype=centrifugal analizi |
| `roots.md` | Roots blower bilgileri | subtype=roots analizi |

### Çözüm Dosyaları (`solutions/`)
| Dosya | Açıklama | Öncelik | Tetikleyici |
|-------|----------|---------|-------------|
| `heat_recovery.md` | Atık ısı geri kazanımı | Yüksek | Güç > 15 kW, ısıtma ihtiyacı var |
| `vsd.md` | Değişken hız sürücü (VSD) retrofit | Yüksek | Yük faktörü < 70%, değişken yük |
| `pressure_optimization.md` | Basınç optimizasyonu | Yüksek | Basınç > gerekli + 1 bar |
| `air_leaks.md` | Kaçak tespiti ve giderimi | Yüksek | Kaçak oranı > %15 |
| `maintenance.md` | Bakım optimizasyonu | Orta | Düzenli bakım eksikliği |
| `inlet_optimization.md` | Giriş optimizasyonu | Düşük | Yüksek giriş sıcaklığı |
| `dryer_optimization.md` | Kurutucu optimizasyonu | Düşük | Aşırı kurutma |
| `system_design.md` | Sistem tasarımı ve konfigürasyon | Düşük | Yeni sistem veya kapasite artışı |

## Navigasyon Kuralları
1. Her analiz `formulas.md` + `benchmarks.md` ile başlar
2. Alt tip biliniyorsa `equipment/{subtype}.md` oku
3. Benchmark sonucuna göre ilgili `solutions/*.md` dosyalarına git
4. Audit planlanıyorsa `audit.md` ek referans olarak kullan

## Referanslar

1. Compressed Air & Gas Institute (CAGI). *Compressed Air and Gas Handbook*. 7th ed.
2. Saidur, R., Rahim, N.A. & Hasanuzzaman, M. (2010). "A review on compressed-air energy use and energy savings." *Renewable and Sustainable Energy Reviews*, 14(4), 1135-1153.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
