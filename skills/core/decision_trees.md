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

## Kurutma Fırını Analizi Karar Ağacı

```
BAŞLA: Kurutma fırını analizi
│
├── Exergy verimi < 10% (konvektif) veya < 15% (ısı pompalı)?
│   ├── EVET → Düşük verim
│   │   ├── SMER < 0.5 kg/kWh (konvektif)?
│   │   │   └── EVET → OKU: dryer/benchmarks.md (tip bazlı karşılaştır)
│   │   │       ├── Mekanik ön su alma yapılıyor mu?
│   │   │       │   └── HAYIR → OKU: solutions/mechanical_dewatering.md
│   │   │       └── Kurutucu tipi uygun mu?
│   │   │           └── HAYIR → Tip değişikliği değerlendir
│   │   │
│   │   ├── Egzoz sıcaklığı > 80°C?
│   │   │   └── EVET → OKU: solutions/exhaust_heat_recovery.md
│   │   │
│   │   ├── Egzoz bağıl nemi < %60?
│   │   │   └── EVET → OKU: solutions/air_recirculation.md
│   │   │
│   │   ├── Kurutma sıcaklığı < 80°C ve konvektif?
│   │   │   └── EVET → OKU: solutions/heat_pump_retrofit.md
│   │   │
│   │   └── Yüzey sıcaklığı > ortam + 60°C?
│   │       └── EVET → OKU: solutions/insulation.md
│   │
│   └── HAYIR → Kabul edilebilir verim
│       ├── Sıcaklık optimizasyonu potansiyeli?
│       │   └── OKU: solutions/temperature_optimization.md
│       └── Bakım ve izleme öner
│
├── Enerji verimi < 50%?
│   └── EVET → OKU: dryer/audit.md (detaylı denetim öner)
│
└── SONUÇ: Öneri listesi oluştur, ROI'ye göre sırala
```

## Buhar Türbini Analizi Karar Ağacı

```
BAŞLA: Buhar türbini analizi
│
├── Türbin tipi belirleme
│   ├── Back-pressure → OKU: equipment/back_pressure.md
│   ├── Condensing → OKU: equipment/condensing.md
│   ├── Extraction → OKU: equipment/extraction.md
│   └── ORC → OKU: equipment/orc.md
│
├── İzentropik verim < benchmark?
│   ├── Küçük (<1 MW): benchmark η_is > 60%
│   ├── Orta (1-10 MW): benchmark η_is > 75%
│   └── Büyük (>10 MW): benchmark η_is > 85%
│
├── η_is düşükse:
│   ├── Çalışma süresi > 40,000 saat ve η bozunma > %3?
│   │   └── EVET → OKU: solutions/maintenance.md (Overhaul öner)
│   ├── Sızdırmazlık kaçağı tespit edildi mi?
│   │   └── EVET → OKU: solutions/efficiency_improvement.md (Seal bakımı)
│   ├── Kanat fouling/erosion?
│   │   └── EVET → OKU: solutions/efficiency_improvement.md (Temizlik/kaplama)
│   └── Kısmi yükte mi çalışıyor (<%60)?
│       └── EVET → OKU: solutions/load_matching.md
│
├── CHP analizi (back-pressure veya extraction ise):
│   ├── PES < %10?
│   │   └── EVET → OKU: systems/steam_turbine_chp.md (Optimizasyon)
│   ├── HPR uygun mu (termal/elektrik dengesinde)?
│   │   └── HAYIR → OKU: solutions/load_matching.md
│   └── Kondensat dönüş oranı < %60?
│       └── EVET → OKU: solutions/condensate_optimization.md
│
├── PRV ikamesi fırsatı var mı?
│   ├── PRV debisi > 3 ton/h VE ΔP > 10 bar?
│   │   └── EVET → OKU: equipment/micro_turbine.md (Yüksek öncelik)
│   └── HAYIR → Mevcut türbin optimizasyonuna odaklan
│
├── Atık ısı değerlendirmesi
│   ├── Düşük T kaynağı (80-350°C) var mı?
│   │   └── EVET → OKU: equipment/orc.md (ORC fizibilite)
│   └── Yüksek T kaynağı (>350°C) var mı?
│       └── EVET → OKU: systems/hrsg.md (HRSG değerlendirme)
│
└── SONUÇ: Öneri listesi oluştur, ROI'ye göre sırala
    → Fizibilite gerekiyorsa: OKU: economics/feasibility.md
```

## Isı Eşanjörü Analizi Karar Ağacı

```
BAŞLA: Isı eşanjörü analizi
│
├── Etkililik (effectiveness) < benchmark?
│   ├── Gövde-boru: benchmark ε > 0.60
│   ├── Plakalı: benchmark ε > 0.75
│   └── Çift borulu: benchmark ε > 0.50
│
├── Etkililik düşükse:
│   ├── U-değer tasarımdan <%70?
│   │   └── EVET → Fouling tespit → OKU: solutions/fouling_management.md
│   ├── Yaklaşım sıcaklığı (approach temp) > 2×ΔT_min?
│   │   └── EVET → OKU: solutions/approach_temp_optimization.md
│   ├── Basınç düşümü tasarımdan >%50 fazla?
│   │   └── EVET → OKU: solutions/pressure_drop_optimization.md
│   └── Bejan sayısı analizi
│       ├── Be > 0.5 → Isı transfer iyileştirmesi öncelikli
│       └── Be < 0.5 → Akış direnci azaltma öncelikli
│
├── Exergy verimi < 40%?
│   ├── EVET → Termodinamik kalite düşük
│   │   ├── Büyük ΔT (>30°C) → OKU: solutions/heat_recovery.md (Kademeli ısı değişimi)
│   │   └── Düşük sıcaklık (<60°C) → Exergy kalitesi doğal olarak düşük
│   └── HAYIR → Kabul edilebilir, bakım ve izleme öner
│
└── SONUÇ: Öneri listesi oluştur, ROI'ye göre sırala
```

## İleri Analiz Tetikleme Karar Ağacı

```
BAŞLA: Fabrika verisi alındığında ileri analiz ihtiyacını değerlendir
│
├── Pinch analizi gerekli mi?
│   ├── 3+ sıcak akış VE 2+ soğuk akış var mı?
│   │   └── EVET → Pinch analizi öner
│   ├── Toplam ısı yükü > 500 kW?
│   │   └── EVET → Pinch analizi öner
│   └── Hem ısıtma hem soğutma utility kullanılıyor mu?
│       └── EVET → Pinch analizi öner
│       → Referans: knowledge/factory/pinch/fundamentals.md
│
├── İleri exergy analizi gerekli mi?
│   ├── 3+ ekipman VE toplam I_total > 100 kW?
│   │   └── EVET → AV/UN ve EN/EX dekompozisyon öner
│   ├── Büyük I_total olan ekipman ama düşük iyileştirme beklentisi?
│   │   └── EVET → θ analizi öner (kaçınılabilirlik oranı)
│   └── Ekipmanlar arası güçlü etkileşim var mı?
│       └── EVET → Ekzojen analiz öner
│       → Referans: knowledge/factory/advanced_exergy/overview.md
│
├── Termoekonomik optimizasyon gerekli mi?
│   ├── Toplam Ċ_D > 50.000 €/yıl?
│   │   └── EVET → Detaylı termoekonomik analiz öner
│   ├── f_k < 0.25 olan bileşen var mı?
│   │   └── EVET → Verim artırma öner
│   └── Birden fazla büyük yatırım alternatifi var mı?
│       └── EVET → Bütünleşik optimizasyon öner
│       → Referans: knowledge/factory/thermoeconomic_optimization/overview.md
│
├── EGM (Entropi üretim minimizasyonu) gerekli mi?
│   ├── N_s > 0.5 olan ekipman var mı?
│   │   └── EVET → EGM analizi öner
│   └── Bejan sayısı bilgisi isteniyorsa?
│       └── EVET → Irreversibility kaynak ayrıştırması öner
│       → Referans: knowledge/factory/entropy_generation/overview.md
│
└── SONUÇ: Uygun ileri analiz yöntemlerini öner, referans dosyalara yönlendir
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
│   ├── Chiller + Isıtma ihtiyacı var mı?
│   │   └── EVET → OKU: factory/heat_integration.md (Kondenser ısısı)
│   ├── Kazan/Kompresör + Kurutma fırını var mı?
│   │   └── EVET → OKU: factory/cross_equipment.md (Kurutma entegrasyonu)
│   └── Fırın/Kiln + Kurutma fırını var mı?
│       └── EVET → OKU: factory/heat_integration.md (Fırın egzozu → kurutma)
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

## Fabrika Termoekonomik Karar Ağacı

```
BAŞLA: Fabrika termoekonomik değerlendirme
│
├── Tek ekipman mı, çoklu ekipman mı?
│   │
│   ├── TEK EKİPMAN
│   │   ├── Yıllık enerji maliyeti < 20.000 €?
│   │   │   └── EVET → Basit ROI analizi yeterli
│   │   │       → OKU: factory/economic_analysis.md
│   │   └── HAYIR → Termoekonomik analiz faydalı
│   │       ├── Mevcut ekipman, parametre ayarı?
│   │       │   └── EVET → Parametrik optimizasyon
│   │       │       → OKU: thermoeconomic_optimization/parametric_optimization.md
│   │       └── Yeni ekipman kararı?
│   │           └── EVET → Basit ROI + duyarlılık yeterli
│   │               → OKU: thermoeconomic_optimization/sensitivity_analysis.md
│   │
│   └── ÇOKLU EKİPMAN
│       │
│       ├── Exergy verisi mevcut mu?
│       │   │
│       │   ├── EVET → Termoekonomik analiz yap
│       │   │   │
│       │   │   ├── Yapısal karar var mı? (CHP, konfigürasyon seçimi)
│       │   │   │   ├── EVET → Yapısal optimizasyon (MINLP)
│       │   │   │   │   → OKU: thermoeconomic_optimization/structural_optimization.md
│       │   │   │   └── HAYIR → Parametrik / İteratif
│       │   │   │       │
│       │   │   │       ├── Hızlı tarama mı? → İteratif yöntem
│       │   │   │       │   → OKU: thermoeconomic_optimization/iterative_method.md
│       │   │   │       └── Detaylı optimizasyon mu? → Parametrik
│       │   │   │           → OKU: thermoeconomic_optimization/parametric_optimization.md
│       │   │   │
│       │   │   ├── Birden fazla amaç var mı? (maliyet + verim + CO₂)
│       │   │   │   ├── EVET → Çok amaçlı optimizasyon (NSGA-II)
│       │   │   │   │   → OKU: thermoeconomic_optimization/multi_objective.md
│       │   │   │   └── HAYIR → Tek amaçlı (min C_total)
│       │   │   │       → OKU: thermoeconomic_optimization/objective_functions.md
│       │   │   │
│       │   │   └── Bütçe kısıtı var mı?
│       │   │       ├── EVET → Portföy optimizasyonu
│       │   │       │   → OKU: thermoeconomic_optimization/practical_guide.md
│       │   │       └── HAYIR → Tam optimizasyon
│       │   │
│       │   └── HAYIR → Önce exergy analizi yap
│       │       → OKU: factory/exergy_fundamentals.md
│       │       → Sonra bu ağaca geri dön
│       │
│       └── SONUÇ: Termoekonomik analiz raporu
│           → OKU: thermoeconomic_optimization/practical_guide.md (Bölüm 8: Raporlama)
```

## Termoekonomik Önceliklendirme Matrisi

Fabrika seviyesinde termoekonomik analizde yöntem seçimi için:

| Toplam Ċ_D [€/yıl] | Ekipman Sayısı ≤ 3 | Ekipman Sayısı 4-8 | Ekipman Sayısı > 8 |
|---------------------|--------------------|--------------------|---------------------|
| < 20.000 | Basit ROI | Basit ROI | İteratif yöntem |
| 20.000 – 50.000 | İteratif yöntem | İteratif + parametrik | Parametrik + duyarlılık |
| 50.000 – 200.000 | Parametrik | Parametrik + çok amaçlı | Çok amaçlı (NSGA-II) |
| > 200.000 | Parametrik + duyarlılık | Çok amaçlı (NSGA-II) | Yapısal + çok amaçlı |

**Ek kurallar:**
- CBAM etkili sektör → bir üst seviye yöntem uygula
- CHP kararı varsa → yapısal optimizasyon ekle
- Bütçe < toplam önerilen yatırımın %50'si → portföy optimizasyonu ekle

**Referanslar:**
- `thermoeconomic_optimization/practical_guide.md` (Bölüm 3: Yöntem seçim matrisi)
- `thermoeconomic_optimization/algorithms.md` (Algoritma seçim rehberi)
