---
skill_id: chiller_expert
version: 1.0
type: equipment
equipment_type: chiller
triggers:
  - single_equipment_analysis
  - equipment_type == "chiller"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
knowledge_files:
  - knowledge/chiller/benchmarks.md
  - knowledge/chiller/formulas.md
  - knowledge/chiller/equipment/*.md
  - knowledge/chiller/solutions/*.md
---

# Chiller Uzmanı

## Uzmanlık Alanı

Soğutma sistemleri exergy analizi:
- Santrifüj, vidalı, scroll chiller
- Absorption chiller
- Free cooling
- Kondenser optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer (Santrifüj) |
|--------|--------|----------------------|
| COP | Q_soğutma / W_kompresör | > 5.5 |
| IPLV | Kısmi yük COP | > 6.5 |
| Exergy verimi | Ex_soğutma / W_kompresör | > 40% |
| kW/ton | | < 0.6 |

## COP Benchmark

| Chiller Tipi | Düşük | Ortalama | İyi | Mükemmel |
|--------------|-------|----------|-----|----------|
| Santrifüj | < 4.5 | 4.5-5.5 | 5.5-6.5 | > 6.5 |
| Vidalı | < 4.0 | 4.0-5.0 | 5.0-5.5 | > 5.5 |
| Scroll | < 3.5 | 3.5-4.5 | 4.5-5.0 | > 5.0 |
| Absorption (tek etkili) | < 0.6 | 0.6-0.7 | 0.7-0.8 | > 0.8 |

## Özel Kurallar

### Exergy Verimi Hesaplama
```
Soğutma exergy'si:
Ex_cooling = Q_cooling × (T₀/T_cold - 1)

Burada T₀ = 298 K (25°C), T_cold = soğutma sıcaklığı (K)

7°C soğutma için: (298/280 - 1) = 0.064
Yani 100 kW soğutma ≈ 6.4 kW exergy
```

### Kondenser Optimizasyonu
```
Kondenser suyu sıcaklığı her 1°C düşüşünde:
- COP %2-3 artar

Kondenser approach temperature:
- < 3°C: Mükemmel
- 3-5°C: İyi
- > 5°C: Temizlik/bakım gerekli
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Kondenser temizliği | %5-15 | Düşük | < 0.3 yıl |
| Soğutma kulesi optimizasyonu | %5-10 | €5-20K | 1-2 yıl |
| Free cooling | %20-40 | €20-50K | 2-4 yıl |
| VSD retrofit | %15-30 | €15-40K | 2-3 yıl |
| Kondenser ısı geri kazanım | €0.05/kWh | €10-25K | 2-4 yıl |
