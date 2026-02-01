---
skill_id: decision_trees
version: 1.0
type: core
---

# Karar Ağaçları

## Kompresör Analizi Karar Ağacı

```
BAŞLA: Kompresör analizi
│
├── Exergy verimi < 40%?
│   ├── EVET → Kritik düşük verim
│   │   ├── Spesifik güç > 8 kW/(m³/min)?
│   │   │   └── EVET → OKU: solutions/compressor_replacement.md
│   │   ├── Yük faktörü < 50%?
│   │   │   └── EVET → OKU: solutions/capacity_control.md, solutions/vsd.md
│   │   └── Basınç > 8 bar ve kullanım < 7 bar gerekli?
│   │       └── EVET → OKU: solutions/pressure_optimization.md
│   │
│   └── HAYIR → Kabul edilebilir verim
│       ├── Kaçak oranı tahmini?
│       │   └── > %20 → OKU: solutions/leak_detection.md
│       └── VSD var mı?
│           └── HAYIR ve değişken yük → OKU: solutions/vsd.md
│
└── SONUÇ: Öneri listesi oluştur, ROI'ye göre sırala
```

## Kazan Analizi Karar Ağacı

```
BAŞLA: Kazan analizi
│
├── Exergy verimi < 30%?
│   ├── EVET → Düşük verim
│   │   ├── Baca gazı sıcaklığı > 200°C?
│   │   │   └── EVET → OKU: solutions/economizer.md
│   │   ├── Fazla hava > 20%?
│   │   │   └── EVET → OKU: solutions/combustion_optimization.md
│   │   └── Blowdown > 5%?
│   │       └── EVET → OKU: solutions/blowdown_heat_recovery.md
│   │
│   └── HAYIR → Ortalama/iyi verim
│       └── İyileştirme potansiyeli sınırlı, bakım öner
│
├── Enerji verimi < 85%?
│   └── EVET → OKU: solutions/insulation.md, solutions/maintenance.md
│
└── SONUÇ: Öneri listesi oluştur
```

## Chiller Analizi Karar Ağacı

```
BAŞLA: Chiller analizi
│
├── COP < benchmark?
│   ├── Santrifüj: benchmark COP > 5.5
│   ├── Vidalı: benchmark COP > 4.5
│   └── Scroll: benchmark COP > 4.0
│
├── COP düşükse:
│   ├── Kondenser suyu sıcak (>35°C)?
│   │   └── OKU: solutions/condenser_optimization.md
│   ├── Evaporatör ΔT yüksek (>7°C)?
│   │   └── OKU: solutions/evaporator_cleaning.md
│   └── Kısmi yükte mi çalışıyor?
│       └── OKU: solutions/vsd_chiller.md
│
└── SONUÇ: Öneri listesi
```

## Pompa Analizi Karar Ağacı

```
BAŞLA: Pompa analizi
│
├── Wire-to-water verimi < 50%?
│   ├── EVET → Düşük sistem verimi
│   │   ├── Throttle kontrol var mı?
│   │   │   └── EVET → OKU: solutions/vsd.md (Yüksek öncelik)
│   │   ├── Pompa verimi < 70%?
│   │   │   └── EVET → OKU: solutions/pump_replacement.md
│   │   └── Motor verimi < 90%?
│   │       └── EVET → OKU: solutions/motor_upgrade.md
│   │
│   └── HAYIR → Kabul edilebilir
│       └── Bakım ve izleme öner
│
├── VSD yok ve değişken debi?
│   └── OKU: solutions/vsd.md
│
└── SONUÇ: Öneri listesi
```

## Fabrika Analizi Karar Ağacı

```
BAŞLA: Fabrika analizi
│
├── Hotspot belirleme
│   └── Kayıp sıralaması yap, en büyük 3'e odaklan
│
├── Cross-equipment fırsatları
│   ├── Kompresör + Kazan var mı?
│   │   └── EVET → OKU: factory/cross_equipment.md (Atık ısı)
│   ├── Kazan + Soğutma ihtiyacı var mı?
│   │   └── EVET → OKU: factory/cogeneration.md (Absorption chiller)
│   └── Chiller + Isıtma ihtiyacı var mı?
│       └── EVET → OKU: factory/heat_integration.md (Kondenser ısısı)
│
├── Sektör bilgisi
│   └── OKU: factory/sector_{sector}.md
│
├── Ekonomik analiz
│   └── OKU: factory/prioritization.md
│   └── Quick wins vs Strategic projects ayır
│
└── SONUÇ: Önceliklendirilmiş aksiyon planı
```

## Önceliklendirme Matrisi

| ROI | Karmaşıklık | Öncelik |
|-----|-------------|---------|
| < 1 yıl | Düşük | Yüksek (Quick Win) |
| < 1 yıl | Yüksek | Yüksek |
| 1-3 yıl | Düşük | Orta |
| 1-3 yıl | Yüksek | Orta |
| > 3 yıl | Düşük | Düşük |
| > 3 yıl | Yüksek | Düşük |
