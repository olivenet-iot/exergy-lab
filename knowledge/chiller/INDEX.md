# Chiller Bilgi Tabanı İndeks

## Genel Bakış
Soğutma sistemleri exergy analizi için kapsamlı bilgi tabanı.

## Dosya Listesi

### Temel Dosyalar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `formulas.md` | Chiller exergy hesaplama formülleri, COP, Carnot | Yüksek | Her chiller analizinde |
| `benchmarks.md` | COP benchmark verileri, verim aralıkları | Yüksek | Değerlendirme ve sınıflandırma |
| `audit.md` | Soğutma sistemi denetim metodolojisi | Orta | Denetim planlama |

### Ekipman Dosyaları (`equipment/`)
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `systems_overview.md` | Soğutma sistemine genel bakış | Genel bilgi |
| `vapor_compression.md` | Buhar sıkıştırmalı çevrim | Temel çevrim bilgisi |
| `screw.md` | Vidalı chiller | subtype=screw analizi |
| `centrifugal.md` | Santrifüj chiller | subtype=centrifugal analizi |
| `scroll.md` | Scroll chiller | subtype=scroll analizi |
| `reciprocating.md` | Pistonlu chiller | subtype=reciprocating analizi |
| `absorption.md` | Absorpsiyonlu chiller | subtype=absorption analizi |
| `air_cooled.md` | Hava soğutmalı chiller | Soğutma tipi değerlendirmesi |
| `water_cooled.md` | Su soğutmalı chiller | Soğutma tipi değerlendirmesi |
| `cooling_tower.md` | Soğutma kulesi bilgileri | Kondenser sistemi |
| `refrigerants.md` | Soğutucu akışkan bilgileri | Akışkan seçimi |

### Çözüm Dosyaları (`solutions/`)
| Dosya | Açıklama | Öncelik | Tetikleyici |
|-------|----------|---------|-------------|
| `vsd.md` | Değişken hız sürücü | Yüksek | Kısmi yük çalışma > %30 |
| `condenser_optimization.md` | Kondenser optimizasyonu | Yüksek | Approach temp > 5°C |
| `chilled_water_reset.md` | Soğuk su sıcaklık sıfırlama | Orta | Sabit setpoint |
| `free_cooling.md` | Serbest soğutma (free cooling) | Orta | Dış ortam < 15°C dönemleri |
| `sequencing.md` | Chiller sıralama optimizasyonu | Orta | Çoklu chiller kurulumu |
| `maintenance.md` | Bakım optimizasyonu | Orta | COP düşüşü |
| `load_reduction.md` | Yük azaltma stratejileri | Düşük | Aşırı soğutma ihtiyacı |
| `delta_t.md` | Delta-T optimizasyonu | Orta | Düşük ΔT sendromu |
| `thermal_storage.md` | Termal depolama | Düşük | Puant tarife, değişken yük |
| `heat_recovery.md` | Kondenser ısı geri kazanımı | Orta | Eşzamanlı ısıtma ihtiyacı |

## Navigasyon Kuralları
1. Her analiz `formulas.md` + `benchmarks.md` ile başlar
2. Alt tip biliniyorsa `equipment/{subtype}.md` oku
3. Soğutma tipi (hava/su) bilgisi `equipment/air_cooled.md` veya `water_cooled.md`
4. Benchmark sonucuna göre ilgili `solutions/*.md` dosyalarına git
