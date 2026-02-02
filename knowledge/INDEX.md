---
title: "ExergyLab Bilgi Tabanı Ana İndeks (Master Knowledge Base Index)"
category: reference
keywords: [exergy, bilgi tabanı, navigasyon, indeks]
related_files: [knowledge/compressor/INDEX.md, knowledge/boiler/INDEX.md, knowledge/chiller/INDEX.md, knowledge/pump/INDEX.md, knowledge/heat_exchanger/INDEX.md, knowledge/steam_turbine/INDEX.md, knowledge/dryer/INDEX.md, knowledge/factory/INDEX.md]
priority: high
last_updated: 2026-02-02
---
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
├── heat_exchanger/              ← Isı Eşanjörü bilgi tabanı (21 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Isı eşanjörü exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — U-değer, etkinlik, exergy verimi aralıkları [Öncelik: Yüksek]
│   ├── audit.md               — Isı eşanjörü enerji denetimi [Öncelik: Orta]
│   ├── standards.md           — TEMA, ASME, API standartları [Öncelik: Orta]
│   ├── case_studies.md        — Uygulama vaka çalışmaları [Öncelik: Düşük]
│   ├── equipment/             — Eşanjör tipleri (9 dosya)
│   │   ├── systems_overview.md — Eşanjör sistemlerine genel bakış
│   │   ├── shell_and_tube.md  — Gövde-boru eşanjör (TEMA)
│   │   ├── plate.md           — Plakalı eşanjör
│   │   ├── air_cooled.md      — Hava soğutmalı eşanjör
│   │   ├── double_pipe.md     — Çift borulu eşanjör
│   │   ├── spiral.md          — Spiral eşanjör
│   │   ├── economizer.md      — Ekonomizer
│   │   ├── air_preheater.md   — Hava ön ısıtıcı
│   │   └── recuperator.md     — Reküperatör
│   └── solutions/             — İyileştirme çözümleri (6 dosya)
│       ├── fouling_management.md  — Kirlenme yönetimi [Öncelik: Yüksek]
│       ├── approach_temp.md       — Yaklaşım sıcaklığı opt. [Öncelik: Yüksek]
│       ├── pressure_drop.md       — Basınç düşüşü azaltma
│       ├── heat_recovery.md       — Isı geri kazanım [Öncelik: Yüksek]
│       ├── retrofit.md            — Eşanjör iyileştirme
│       └── material_selection.md  — Malzeme seçimi
│
├── dryer/                       ← Kurutma fırını bilgi tabanı (26 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Kurutma exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — Tip/sektör karşılaştırma verileri [Öncelik: Yüksek]
│   ├── psychrometrics.md      — Nemli hava termodinamiği [Öncelik: Yüksek]
│   ├── audit.md               — Kurutma fırını enerji denetimi [Öncelik: Orta]
│   ├── case_studies.md        — Uygulama vaka çalışmaları [Öncelik: Orta]
│   ├── equipment/             — Kurutucu tipleri (8 dosya)
│   │   ├── tunnel_dryer.md    — Tünel kurutucu
│   │   ├── belt_dryer.md      — Bant kurutucu
│   │   ├── rotary_dryer.md    — Döner kurutucu
│   │   ├── fluidized_bed.md   — Akışkan yataklı kurutucu
│   │   ├── spray_dryer.md     — Sprey kurutucu
│   │   ├── drum_dryer.md      — Silindir kurutucu
│   │   ├── heat_pump_dryer.md — Isı pompalı kurutucu
│   │   └── infrared_dryer.md  — Kızılötesi kurutucu
│   ├── solutions/             — İyileştirme çözümleri (7 dosya)
│   │   ├── exhaust_heat_recovery.md — Egzoz ısı geri kazanımı [Öncelik: Yüksek]
│   │   ├── air_recirculation.md     — Hava geri deviri [Öncelik: Yüksek]
│   │   ├── heat_pump_retrofit.md    — Isı pompası retrofit
│   │   ├── mechanical_dewatering.md — Mekanik ön su alma [Öncelik: Yüksek]
│   │   ├── insulation.md            — Yalıtım iyileştirmesi
│   │   ├── temperature_optimization.md — Sıcaklık optimizasyonu
│   │   └── solar_preheating.md      — Güneş ön ısıtma
│   └── sectors/               — Sektörel uygulama rehberleri (5 dosya)
│       ├── food_drying.md     — Gıda kurutma uygulamaları
│       ├── paper_drying.md    — Kağıt/selüloz kurutma
│       ├── textile_drying.md  — Tekstil kurutma
│       ├── ceramic_drying.md  — Seramik kurutma
│       └── wood_drying.md     — Kereste kurutma fırınları
│
├── steam_turbine/             ← Buhar türbini / CHP bilgi tabanı (21 dosya)
│   ├── INDEX.md               — Alt navigasyon haritası
│   ├── formulas.md            — Exergy hesaplama formülleri [Öncelik: Yüksek]
│   ├── benchmarks.md          — Sektörel karşılaştırma verileri [Öncelik: Yüksek]
│   ├── audit.md               — Performans denetimi metodolojisi [Öncelik: Orta]
│   ├── case_studies.md        — Türk endüstriyel vaka çalışmaları [Öncelik: Düşük]
│   ├── equipment/             — Türbin tipleri (5 dosya)
│   │   ├── back_pressure.md   — Karşı basınçlı türbin
│   │   ├── condensing.md      — Yoğuşmalı türbin
│   │   ├── extraction.md      — Ara çekişli türbin
│   │   ├── orc.md             — Organic Rankine Cycle
│   │   └── micro_turbine.md   — Mikro türbin / PRV ikamesi
│   ├── systems/               — CHP/CCHP sistem konfigürasyonları (5 dosya)
│   │   ├── steam_turbine_chp.md — Buhar türbini CHP
│   │   ├── gas_turbine_chp.md — Gaz türbini + HRSG CHP
│   │   ├── engine_chp.md      — Motor CHP
│   │   ├── trigeneration.md   — Trijenerasyon (CCHP)
│   │   └── hrsg.md            — HRSG (türbin perspektifi)
│   ├── solutions/             — İyileştirme çözümleri (5 dosya)
│   │   ├── efficiency_improvement.md — Verim iyileştirme
│   │   ├── load_matching.md   — Yük eşleştirme
│   │   ├── condensate_optimization.md — Kondensat optimizasyonu
│   │   ├── maintenance.md     — Bakım planlaması
│   │   └── sizing_guide.md    — Boyutlandırma rehberi
│   └── economics/             — Ekonomik analiz (3 dosya)
│       ├── feasibility.md     — CHP fizibilite analizi
│       ├── feed_in_tariff.md  — Türkiye elektrik piyasası
│       └── financing.md       — Finansman ve teşvikler
│
└── factory/                   ← Fabrika seviyesi bilgi tabanı (33+ dosya)
    ├── INDEX.md               — Alt navigasyon haritası
    ├── advanced_exergy/       ← İleri Exergy Analizi (18 dosya)
    │   ├── INDEX.md           — İleri exergy navigasyon haritası
    │   ├── overview.md        — Genel bakış, tarihçe, 3 dekompozisyon [Öncelik: Yüksek]
    │   ├── avoidable_unavoidable.md — Kaçınılabilir/kaçınılamaz (AV/UN) [Öncelik: Yüksek]
    │   ├── endogenous_exogenous.md  — Endojen/ekzojen (EN/EX) [Öncelik: Yüksek]
    │   ├── four_way_splitting.md    — 4-yollu dekompozisyon [Öncelik: Yüksek]
    │   ├── ideal_conditions.md      — Ekipman bazında ideal koşullar [Öncelik: Yüksek]
    │   ├── methodology.md           — 8-adımlı hesaplama metodolojisi [Öncelik: Yüksek]
    │   ├── interpretation_guide.md  — Sonuç yorumlama rehberi [Öncelik: Yüksek]
    │   ├── improvement_priority.md  — IPN, θ sınıflandırma [Öncelik: Yüksek]
    │   ├── visualization.md         — Görselleştirme yöntemleri [Öncelik: Orta]
    │   ├── limitations.md           — Sınırlılıklar ve uyarılar [Öncelik: Orta]
    │   ├── case_studies.md          — 3 vaka çalışması [Öncelik: Orta]
    │   └── equipment_specific/      — Ekipman bazında ileri analiz (6 dosya)
    │       ├── compressor_advanced.md — Kompresör ileri exergy analizi
    │       ├── boiler_advanced.md     — Kazan ileri exergy analizi
    │       ├── heat_exchanger_advanced.md — Isı değiştirici ileri analizi
    │       ├── turbine_advanced.md    — Türbin ileri exergy analizi
    │       ├── pump_advanced.md       — Pompa ileri exergy analizi
    │       └── chiller_advanced.md    — Chiller ileri exergy analizi
    ├── entropy_generation/    ← Entropi Üretim Minimizasyonu — EGM (19 dosya) [YENİ]
    │   ├── INDEX.md           — EGM navigasyon haritası
    │   ├── overview.md        — EGM genel bakış ve felsefesi [Öncelik: Yüksek]
    │   ├── fundamentals.md    — Termodinamik temeller, Gouy-Stodola [Öncelik: Yüksek]
    │   ├── bejan_number.md    — Bejan sayısı ve entropi üretim sayısı [Öncelik: Yüksek]
    │   ├── heat_transfer_egm.md    — Isı transferinde EGM [Öncelik: Yüksek]
    │   ├── fluid_flow_egm.md       — Akış sistemlerinde EGM [Öncelik: Yüksek]
    │   ├── finite_time_thermo.md   — Sonlu zamanlı termodinamik [Öncelik: Orta]
    │   ├── heat_exchanger_egm.md   — Eşanjör optimizasyonu [Öncelik: Yüksek]
    │   ├── pipe_flow_egm.md        — Boru akışı optimizasyonu [Öncelik: Orta]
    │   ├── power_cycles_egm.md     — Güç çevrimlerinde EGM [Öncelik: Orta]
    │   ├── refrigeration_egm.md    — Soğutma çevrimlerinde EGM [Öncelik: Orta]
    │   ├── heat_storage_egm.md     — Isı depolama optimizasyonu [Öncelik: Orta]
    │   ├── constructal_theory.md   — Constructal yasa [Öncelik: Orta]
    │   ├── industrial_applications.md — Endüstriyel uygulama rehberi [Öncelik: Orta]
    │   ├── egm_vs_exergoeconomic.md   — EGM vs exergoekonomik [Öncelik: Orta]
    │   ├── case_studies.md         — Vaka çalışmaları [Öncelik: Düşük]
    │   └── worked_examples/        — Çözümlü örnekler (3 dosya)
    │       ├── heat_exchanger_opt.md  — Eşanjör EGM örneği
    │       ├── pipe_sizing.md         — Boru çapı optimizasyonu örneği
    │       └── cooling_system.md      — Soğutma sistemi EGM örneği
    ├── exergoeconomic/        ← Exergoekonomik Analiz (21 dosya) [YENİ]
    │   ├── INDEX.md           — Exergoekonomik navigasyon haritası
    │   ├── overview.md        — Genel bakış, tarihçe, uygulama alanları [Öncelik: Yüksek]
    │   ├── speco_method.md    — SPECO metodolojisi (4 adım) [Öncelik: Yüksek]
    │   ├── fuel_product_definitions.md — 10 ekipman tipi F/P tanımları [Öncelik: Yüksek]
    │   ├── cost_equations.md  — PEC korelasyonları, düzeltme faktörleri [Öncelik: Yüksek]
    │   ├── cost_databases.md  — CEPCI değerleri, Türkiye ayarları [Öncelik: Orta]
    │   ├── levelized_cost.md  — CRF formülü, Ż hesabı [Öncelik: Yüksek]
    │   ├── exergoeconomic_balance.md — Ċ_P = Ċ_F + Ż maliyet bilançosu [Öncelik: Yüksek]
    │   ├── auxiliary_equations.md — F-kuralı, P-kuralı [Öncelik: Orta]
    │   ├── matrix_formulation.md — [A]{c}={Z} matris çözümü [Öncelik: Orta]
    │   ├── evaluation_criteria.md — Ċ_D, f_k, r_k tanım/eşik/karar [Öncelik: Yüksek]
    │   ├── advanced_exergoeconomic.md — AV/UN, EN/EX, 4-yollu matris [Öncelik: Orta]
    │   ├── optimization.md    — İteratif ve matematiksel optimizasyon [Öncelik: Orta]
    │   ├── sensitivity_analysis.md — OAT, tornado, Monte Carlo [Öncelik: Orta]
    │   ├── case_studies.md    — 6 akademik vaka çalışması [Öncelik: Düşük]
    │   └── worked_examples/   — Çözümlü örnekler (3 dosya)
    │       ├── simple_cycle.md    — Basit Rankine çevrimi SPECO örneği
    │       ├── cogeneration.md    — Gaz türbini CHP + ileri analiz
    │       └── industrial_plant.md — ExergyLab ekipmanları ile tesis analizi
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

### Buhar Türbini / CHP Yorumlama
Buhar türbini veya CHP analizi yapıldığında:
1. `knowledge/steam_turbine/formulas.md` — Exergy hesaplama referansı [Öncelik: Yüksek]
2. `knowledge/steam_turbine/benchmarks.md` — Verim karşılaştırma [Öncelik: Yüksek]
3. `knowledge/steam_turbine/equipment/{tip}.md` — Türbin tipi detayları [Öncelik: Orta]
4. `knowledge/steam_turbine/systems/{konfigürasyon}.md` — CHP konfigürasyonu [Öncelik: Orta]
5. `knowledge/steam_turbine/solutions/*.md` — İyileştirme çözümleri [Öncelik: Orta]
6. `knowledge/factory/cogeneration.md` — CHP temelleri ve karşılaştırma [Öncelik: Düşük]

### Isı Eşanjörü Yorumlama
Isı eşanjörü analiz edildiğinde:
1. `knowledge/heat_exchanger/formulas.md` — Exergy hesaplama formülleri [Öncelik: Yüksek]
2. `knowledge/heat_exchanger/benchmarks.md` — U-değer, etkinlik, exergy verimi aralıkları [Öncelik: Yüksek]
3. `knowledge/heat_exchanger/equipment/{subtype}.md` — Eşanjör tipi detayları [Öncelik: Orta]
4. `knowledge/heat_exchanger/solutions/*.md` — İyileştirme çözümleri [Öncelik: Orta]
5. `knowledge/heat_exchanger/audit.md` — Denetim metodolojisi [Öncelik: Düşük]
6. `knowledge/heat_exchanger/standards.md` — TEMA, ASME, API standartları [Öncelik: Düşük]

### İleri Exergy Analizi Yorumlama
Kaçınılabilir/kaçınılamaz veya endojen/ekzojen dekompozisyon gerektiğinde:
1. `knowledge/factory/advanced_exergy/overview.md` — İleri exergy genel bakış [Öncelik: Yüksek]
2. `knowledge/factory/advanced_exergy/four_way_splitting.md` — 4-yollu dekompozisyon [Öncelik: Yüksek]
3. `knowledge/factory/advanced_exergy/ideal_conditions.md` — Kaçınılamaz koşullar referansı [Öncelik: Yüksek]
4. `knowledge/factory/advanced_exergy/equipment_specific/{tip}_advanced.md` — Ekipman detayı [Öncelik: Orta]
5. `knowledge/factory/advanced_exergy/interpretation_guide.md` — Sonuç yorumlama [Öncelik: Orta]
6. `knowledge/factory/advanced_exergy/improvement_priority.md` — Önceliklendirme [Öncelik: Düşük]

### EGM / Entropi Üretim Minimizasyonu Yorumlama
Termodinamik optimizasyon veya entropi analizi yapılacakken:
1. `knowledge/factory/entropy_generation/overview.md` — EGM genel bakış [Öncelik: Yüksek]
2. `knowledge/factory/entropy_generation/fundamentals.md` — Gouy-Stodola temelleri [Öncelik: Yüksek]
3. `knowledge/factory/entropy_generation/bejan_number.md` — Bejan sayısı [Öncelik: Yüksek]
4. İlgili ekipman EGM dosyası (heat_exchanger, pipe_flow, power_cycles, refrigeration, heat_storage) [Öncelik: Orta]
5. `knowledge/factory/entropy_generation/worked_examples/*.md` — Çözümlü örnekler [Öncelik: Düşük]

### Exergoekonomik Yorumlama
Exergy yıkım maliyeti, f_k/r_k değerlendirmesi veya maliyet paylaştırma gerektiğinde:
1. `knowledge/factory/exergoeconomic/overview.md` — Genel bakış [Öncelik: Yüksek]
2. `knowledge/factory/exergoeconomic/evaluation_criteria.md` — Ċ_D, f_k, r_k yorumlama [Öncelik: Yüksek]
3. `knowledge/factory/exergoeconomic/speco_method.md` — SPECO metodolojisi [Öncelik: Yüksek]
4. `knowledge/factory/exergoeconomic/fuel_product_definitions.md` — Ekipman F/P tanımları [Öncelik: Orta]
5. `knowledge/factory/exergoeconomic/optimization.md` — Maliyet optimizasyonu [Öncelik: Orta]
6. `knowledge/factory/exergoeconomic/worked_examples/*.md` — Çözümlü örnekler [Öncelik: Düşük]

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

## Referanslar

1. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
2. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
4. Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis and exergoeconomics." *Energy*, 32(4), 249-253.
