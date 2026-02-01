# ExergyLab Knowledge Base Index

AI navigasyon haritasi. Bu dosya, ExergyLab bilgi tabaninin yapisi ve kullanim kurallari hakkinda rehberlik saglar.

## Dizin Yapisi

```
knowledge/
├── INDEX.md                    ← Bu dosya (navigasyon haritasi)
├── compressor/                 ← Kompresor bilgi tabani
│   ├── formulas.md             — Exergy hesaplama formulleri
│   ├── benchmarks.md           — Sektor karsilastirma verileri
│   ├── audit.md                — Denetim rehberi
│   ├── equipment/              — Ekipman tipleri
│   │   ├── systems_overview.md
│   │   ├── screw.md
│   │   ├── screw_oilfree.md
│   │   ├── piston.md
│   │   ├── scroll.md
│   │   ├── centrifugal.md
│   │   └── roots.md
│   └── solutions/              — Iyilestirme cozumleri
│       ├── heat_recovery.md
│       ├── vsd.md
│       ├── pressure_optimization.md
│       ├── air_leaks.md
│       ├── maintenance.md
│       ├── inlet_optimization.md
│       ├── dryer_optimization.md
│       └── system_design.md
├── boiler/                     ← Kazan bilgi tabani
│   ├── formulas.md
│   ├── benchmarks.md
│   ├── equipment/
│   │   ├── steam_firetube.md
│   │   ├── steam_watertube.md
│   │   ├── hotwater.md
│   │   ├── condensing.md
│   │   ├── waste_heat.md
│   │   ├── electric.md
│   │   └── biomass.md
│   └── solutions/
│       ├── economizer.md
│       ├── air_preheater.md
│       ├── oxygen_control.md
│       ├── blowdown_recovery.md
│       ├── condensate_return.md
│       ├── steam_trap.md
│       ├── insulation.md
│       ├── load_optimization.md
│       ├── combustion_tuning.md
│       └── feedwater_treatment.md
├── chiller/                    ← Chiller bilgi tabani
│   ├── formulas.md
│   ├── benchmarks.md
│   ├── equipment/
│   │   ├── vapor_compression.md
│   │   ├── screw.md
│   │   ├── centrifugal.md
│   │   ├── scroll.md
│   │   ├── reciprocating.md
│   │   ├── absorption.md
│   │   ├── air_cooled.md
│   │   └── water_cooled.md
│   └── solutions/
│       ├── vsd.md
│       ├── condenser_optimization.md
│       ├── chilled_water_reset.md
│       ├── free_cooling.md
│       ├── sequencing.md
│       ├── maintenance.md
│       ├── load_reduction.md
│       ├── delta_t.md
│       ├── thermal_storage.md
│       └── heat_recovery.md
├── pump/                       ← Pompa bilgi tabani
│   ├── formulas.md
│   ├── benchmarks.md
│   ├── equipment/
│   │   ├── centrifugal.md
│   │   ├── positive_displacement.md
│   │   ├── submersible.md
│   │   ├── vertical_turbine.md
│   │   ├── booster.md
│   │   └── vacuum.md
│   └── solutions/
│       ├── vsd.md
│       ├── impeller_trimming.md
│       ├── right_sizing.md
│       ├── parallel_operation.md
│       ├── system_optimization.md
│       ├── motor_upgrade.md
│       ├── maintenance.md
│       ├── throttle_elimination.md
│       ├── cavitation_prevention.md
│       └── control_optimization.md
└── factory/                    ← Fabrika seviyesi bilgi tabani
    ├── cross_equipment.md      — Ekipmanlar arasi entegrasyon firsatlari
    ├── prioritization.md       — Yatirim onceliklendirme rehberi
    ├── factory_benchmarks.md   — Fabrika seviyesi benchmark verileri
    ├── cogeneration.md         — Kojenerasyon bilgileri
    └── energy_management.md    — Enerji yonetim sistemi
```

## Navigasyon Kurallari

### Tekil Ekipman Yorumlama
Tek bir ekipman analiz edildiginde:
1. `knowledge/{equipment_type}/formulas.md` — Hesaplama referansi
2. `knowledge/{equipment_type}/benchmarks.md` — Sektor karsilastirma
3. `knowledge/{equipment_type}/equipment/{subtype}.md` — Ekipman detaylari
4. `knowledge/{equipment_type}/solutions/*.md` — Ilgili cozumler

### Fabrika Seviyesi Yorumlama
Birden fazla ekipman birlikte analiz edildiginde:
1. `knowledge/factory/cross_equipment.md` — Capraz entegrasyon firsatlari
2. `knowledge/factory/prioritization.md` — Onceliklendirme matrisi
3. `knowledge/factory/factory_benchmarks.md` — Fabrika sektor benchmark
4. Her ekipman icin ilgili `knowledge/{type}/benchmarks.md`
5. Entegrasyon icin ilgili `knowledge/{type}/solutions/*.md`

### Oncelik Sirasi
- **Guvenlik uyarilari** her zaman en ustte
- **Yuksek exergy yikimi** olan ekipmanlar once degerlendirilir
- **Capraz ekipman firsatlari** tekil onerilerin uzerinde onceliklendirilir
- **ROI < 2 yil** olan yatirimlar "high" oncelik alir
