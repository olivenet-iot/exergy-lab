# ExergyLab Knowledge Base Index

AI navigasyon haritası. Bu dosya, ExergyLab bilgi tabanının yapısı ve kullanım kuralları hakkında rehberlik sağlar.

## Dizin Yapısı

```
knowledge/
├── INDEX.md                    ← Bu dosya (navigasyon haritası)
├── compressor/                 ← Kompresör bilgi tabanı (18 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — Sektör karşılaştırma verileri [Öncelik: Yüksek]
│   ├── audit.md               — Enerji denetimi metodolojisi [Öncelik: Orta]
│   ├── equipment/             — Ekipman tipleri (7 dosya)
│   │   ├── systems_overview.md — Genel sistem bilgisi
│   │   ├── screw.md           — Vidalı kompresör detayları
│   │   ├── screw_oilfree.md   — Yağsız vidalı kompresör
│   │   ├── piston.md          — Pistonlu kompresör
│   │   ├── scroll.md          — Scroll kompresör
│   │   ├── centrifugal.md     — Santrifüj kompresör
│   │   └── roots.md           — Roots blower
│   └── solutions/             — İyileştirme çözümleri (8 dosya)
│       ├── heat_recovery.md   — Atık ısı geri kazanımı [Öncelik: Yüksek]
│       ├── vsd.md             — Değişken hız sürücü [Öncelik: Yüksek]
│       ├── pressure_optimization.md — Basınç optimizasyonu
│       ├── air_leaks.md       — Kaçak tespiti/giderimi [Öncelik: Yüksek]
│       ├── maintenance.md     — Bakım optimizasyonu
│       ├── inlet_optimization.md — Giriş optimizasyonu
│       ├── dryer_optimization.md — Kurutucu optimizasyonu
│       └── system_design.md   — Sistem tasarımı
│
├── boiler/                    ← Kazan bilgi tabanı (22 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Kazan exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — Kazan sektör karşılaştırma verileri [Öncelik: Yüksek]
│   ├── audit.md               — Kazan denetimi metodolojisi [Öncelik: Orta]
│   ├── equipment/             — Kazan tipleri (9 dosya)
│   │   ├── systems_overview.md — Genel kazan bilgisi
│   │   ├── steam_firetube.md  — Ateş borulu buhar kazanı
│   │   ├── steam_watertube.md — Su borulu buhar kazanı
│   │   ├── hotwater.md        — Sıcak su kazanı
│   │   ├── condensing.md      — Yoğuşmalı kazan
│   │   ├── waste_heat.md      — Atık ısı kazanı / HRSG
│   │   ├── electric.md        — Elektrikli kazan
│   │   ├── biomass.md         — Biyokütle kazanı
│   │   └── fuels.md           — Yakıt tipleri ve özellikleri
│   └── solutions/             — İyileştirme çözümleri (10 dosya)
│       ├── economizer.md      — Ekonomizer [Öncelik: Yüksek]
│       ├── air_preheater.md   — Hava ön ısıtıcı
│       ├── oxygen_control.md  — Oksijen kontrolü [Öncelik: Yüksek]
│       ├── blowdown_recovery.md — Blöf geri kazanımı
│       ├── condensate_return.md — Kondensat geri dönüşü
│       ├── steam_trap.md      — Buhar kapanı
│       ├── insulation.md      — Yalıtım
│       ├── load_optimization.md — Yük optimizasyonu
│       ├── combustion_tuning.md — Yanma ayarı
│       └── feedwater_treatment.md — Besleme suyu arıtma
│
├── chiller/                   ← Chiller bilgi tabanı (24 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Chiller exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — Chiller sektör karşılaştırma verileri [Öncelik: Yüksek]
│   ├── audit.md               — Chiller denetimi metodolojisi [Öncelik: Orta]
│   ├── equipment/             — Chiller tipleri (11 dosya)
│   │   ├── systems_overview.md — Genel soğutma sistemi bilgisi
│   │   ├── vapor_compression.md — Buhar sıkıştırmalı chiller
│   │   ├── screw.md           — Vidalı chiller
│   │   ├── centrifugal.md     — Santrifüj chiller
│   │   ├── scroll.md          — Scroll chiller
│   │   ├── reciprocating.md   — Pistonlu chiller
│   │   ├── absorption.md      — Absorpsiyonlu chiller
│   │   ├── air_cooled.md      — Hava soğutmalı chiller
│   │   ├── water_cooled.md    — Su soğutmalı chiller
│   │   ├── cooling_tower.md   — Soğutma kulesi
│   │   └── refrigerants.md    — Soğutucu akışkanlar
│   └── solutions/             — İyileştirme çözümleri (10 dosya)
│       ├── vsd.md             — Değişken hız sürücü [Öncelik: Yüksek]
│       ├── condenser_optimization.md — Kondenser optimizasyonu [Öncelik: Yüksek]
│       ├── chilled_water_reset.md — Soğuk su sıcaklık ayarı
│       ├── free_cooling.md    — Serbest soğutma
│       ├── sequencing.md      — Chiller sıralama
│       ├── maintenance.md     — Bakım
│       ├── load_reduction.md  — Yük azaltma
│       ├── delta_t.md         — Delta-T optimizasyonu
│       ├── thermal_storage.md — Termal depolama
│       └── heat_recovery.md   — Isı geri kazanımı
│
├── pump/                      ← Pompa bilgi tabanı (22 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Pompa exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — Pompa sektör karşılaştırma verileri [Öncelik: Yüksek]
│   ├── audit.md               — Pompa denetimi metodolojisi [Öncelik: Orta]
│   ├── equipment/             — Pompa tipleri (9 dosya)
│   │   ├── systems_overview.md — Genel pompa sistemi bilgisi
│   │   ├── centrifugal.md     — Santrifüj pompa
│   │   ├── positive_displacement.md — Pozitif deplasmanlı pompa
│   │   ├── submersible.md     — Dalgıç pompa
│   │   ├── vertical_turbine.md — Dikey türbin pompa
│   │   ├── booster.md         — Hidrofor
│   │   ├── vacuum.md          — Vakum pompası
│   │   ├── axial_mixed.md     — Eksenel/karışık akış pompası
│   │   └── motors_drives.md   — Motor ve sürücüler
│   └── solutions/             — İyileştirme çözümleri (10 dosya)
│       ├── vsd.md             — Değişken hız sürücü [Öncelik: Yüksek]
│       ├── impeller_trimming.md — Çark tornalama [Öncelik: Yüksek]
│       ├── right_sizing.md    — Doğru boyutlandırma
│       ├── parallel_operation.md — Paralel çalışma
│       ├── system_optimization.md — Sistem optimizasyonu
│       ├── motor_upgrade.md   — Motor yükseltme
│       ├── maintenance.md     — Bakım
│       ├── throttle_elimination.md — Kısma eliminasyonu [Öncelik: Yüksek]
│       ├── cavitation_prevention.md — Kavitasyon önleme
│       └── control_optimization.md — Kontrol optimizasyonu
│
└── factory/                   ← Fabrika seviyesi bilgi tabanı (33 dosya)
    ├── INDEX.md               — Alt navigasyon haritası
    ├── cross_equipment.md     — Ekipmanlar arası entegrasyon fırsatları [Öncelik: Yüksek]
    ├── prioritization.md      — Yatırım önceliklendirme rehberi [Öncelik: Yüksek]
    ├── factory_benchmarks.md  — Fabrika seviyesi benchmark verileri [Öncelik: Yüksek]
    ├── cogeneration.md        — Kojenerasyon bilgileri
    ├── energy_management.md   — Enerji yönetim sistemi
    ├── heat_integration.md    — Isı entegrasyonu [Öncelik: Yüksek]
    ├── waste_heat_recovery.md — Atık ısı geri kazanımı [Öncelik: Yüksek]
    ├── pinch_analysis.md      — Pinch analizi
    ├── process_integration.md — Proses entegrasyonu
    ├── economic_analysis.md   — Ekonomik analiz
    ├── exergy_fundamentals.md — Exergy temelleri
    ├── exergy_flow_analysis.md — Exergy akış analizi
    ├── energy_flow_analysis.md — Enerji akış analizi
    ├── methodology.md         — Analiz metodolojisi
    ├── system_boundaries.md   — Sistem sınırları
    ├── kpi_definitions.md     — KPI tanımları
    ├── performance_indicators.md — Performans göstergeleri
    ├── data_collection.md     — Veri toplama
    ├── measurement_verification.md — Ölçüm ve doğrulama
    ├── mass_balance.md        — Kütle dengesi
    ├── utility_analysis.md    — Yardımcı tesis analizi
    ├── life_cycle_cost.md     — Yaşam döngüsü maliyeti
    ├── energy_pricing.md      — Enerji fiyatlandırma
    ├── implementation.md      — Uygulama rehberi
    ├── reporting.md           — Raporlama
    ├── case_studies.md        — Vaka çalışmaları
    ├── sector_automotive.md   — Otomotiv sektörü [Sektöre Özel]
    ├── sector_cement.md       — Çimento sektörü [Sektöre Özel]
    ├── sector_chemical.md     — Kimya sektörü [Sektöre Özel]
    ├── sector_food.md         — Gıda sektörü [Sektöre Özel]
    ├── sector_metal.md        — Metal sektörü [Sektöre Özel]
    ├── sector_paper.md        — Kağıt sektörü [Sektöre Özel]
    └── sector_textile.md      — Tekstil sektörü [Sektöre Özel]
```

## Navigasyon Kuralları

### Tekil Ekipman Yorumlama
Tek bir ekipman analiz edildiğinde:
1. `knowledge/{equipment_type}/formulas.md` — Hesaplama referansı [Öncelik: Yüksek]
2. `knowledge/{equipment_type}/benchmarks.md` — Sektör karşılaştırma [Öncelik: Yüksek]
3. `knowledge/{equipment_type}/equipment/{subtype}.md` — Ekipman detayları [Öncelik: Orta]
4. `knowledge/{equipment_type}/solutions/*.md` — İlgili çözümler [Öncelik: Orta]

### Fabrika Seviyesi Yorumlama
Birden fazla ekipman birlikte analiz edildiğinde:
1. `knowledge/factory/cross_equipment.md` — Çapraz entegrasyon fırsatları [Öncelik: Yüksek]
2. `knowledge/factory/prioritization.md` — Önceliklendirme matrisi [Öncelik: Yüksek]
3. `knowledge/factory/factory_benchmarks.md` — Fabrika sektör benchmark [Öncelik: Yüksek]
4. `knowledge/factory/sector_{sector}.md` — Sektöre özel bilgi [Öncelik: Yüksek]
5. Her ekipman için ilgili `knowledge/{type}/benchmarks.md` [Öncelik: Orta]
6. Entegrasyon için ilgili `knowledge/{type}/solutions/*.md` [Öncelik: Düşük]

### Öncelik Sırası
- **Güvenlik uyarıları** her zaman en üstte
- **Yüksek exergy yıkımı** olan ekipmanlar önce değerlendirilir
- **Çapraz ekipman fırsatları** tekil önerilerin üzerinde önceliklendirilir
- **ROI < 2 yıl** olan yatırımlar "high" öncelik alır

### Bağımlılık İlişkileri
- `formulas.md` → `benchmarks.md`: Formüller benchmark değerlendirmesinin temelidir
- `benchmarks.md` → `solutions/*.md`: Benchmark sonucu çözüm seçimini yönlendirir
- `audit.md` → `equipment/*.md`: Denetim sürecinde ekipman bilgisi gerekir
- `factory/cross_equipment.md` → Tüm `{type}/solutions/*.md`: Çapraz fırsatlar çözüm bilgisine dayanır
