# Kazan Bilgi Tabanı İndeks

## Genel Bakış
Buhar ve sıcak su kazanları exergy analizi için kapsamlı bilgi tabanı.

## Dosya Listesi

### Temel Dosyalar
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `formulas.md` | Kazan exergy hesaplama formülleri, yanma exergy'si | Yüksek | Her kazan analizinde |
| `benchmarks.md` | Sektör karşılaştırma verileri, verim aralıkları | Yüksek | Değerlendirme ve sınıflandırma |
| `audit.md` | Kazan enerji denetimi metodolojisi | Orta | Denetim planlama |

### Ekipman Dosyaları (`equipment/`)
| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `systems_overview.md` | Kazan sistemlerine genel bakış | Genel bilgi |
| `steam_firetube.md` | Ateş borulu buhar kazanı | subtype=steam_firetube analizi |
| `steam_watertube.md` | Su borulu buhar kazanı | subtype=steam_watertube analizi |
| `hotwater.md` | Sıcak su kazanı | subtype=hotwater analizi |
| `condensing.md` | Yoğuşmalı kazan | subtype=condensing analizi |
| `waste_heat.md` | Atık ısı kazanı / HRSG | subtype=waste_heat analizi |
| `electric.md` | Elektrikli kazan | subtype=electric analizi |
| `biomass.md` | Biyokütle kazanı | subtype=biomass analizi |
| `fuels.md` | Yakıt tipleri ve özellikleri | Yakıt hesaplamaları |

### Çözüm Dosyaları (`solutions/`)
| Dosya | Açıklama | Öncelik | Tetikleyici |
|-------|----------|---------|-------------|
| `economizer.md` | Ekonomizer | Yüksek | Baca gazı > 180°C |
| `air_preheater.md` | Hava ön ısıtıcı | Orta | Baca gazı > 250°C |
| `oxygen_control.md` | Oksijen trim / O2 kontrolü | Yüksek | Fazla hava > %15 |
| `blowdown_recovery.md` | Blöf geri kazanımı | Orta | Blowdown > %3 |
| `condensate_return.md` | Kondensat geri dönüşü | Yüksek | Geri dönüş oranı < %80 |
| `steam_trap.md` | Buhar kapanı bakım/değişim | Orta | Arızalı kapanlar |
| `insulation.md` | Yalıtım iyileştirme | Orta | Radyasyon kayıpları |
| `load_optimization.md` | Yük optimizasyonu | Düşük | Çoklu kazan, düşük yük |
| `combustion_tuning.md` | Yanma ayarı | Yüksek | O2 > %5 veya CO yüksek |
| `feedwater_treatment.md` | Besleme suyu arıtma | Düşük | Su kalitesi sorunları |

## Navigasyon Kuralları
1. Her analiz `formulas.md` + `benchmarks.md` ile başlar
2. Alt tip biliniyorsa `equipment/{subtype}.md` oku
3. Yakıt bilgisi gerekirse `equipment/fuels.md` referans al
4. Benchmark sonucuna göre ilgili `solutions/*.md` dosyalarına git
