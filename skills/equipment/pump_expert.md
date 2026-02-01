---
skill_id: pump_expert
version: 1.0
type: equipment
equipment_type: pump
triggers:
  - single_equipment_analysis
  - equipment_type == "pump"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
knowledge_files:
  - knowledge/pump/benchmarks.md
  - knowledge/pump/formulas.md
  - knowledge/pump/equipment/*.md
  - knowledge/pump/solutions/*.md
---

# Pompa Uzmanı

## Uzmanlık Alanı

Pompalama sistemleri exergy analizi:
- Santrifüj, pozitif deplasman pompalar
- VSD retrofit
- Throttle eliminasyonu
- Sistem optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Pompa verimi | P_hidrolik / P_mil | > 80% |
| Motor verimi | P_mil / P_elektrik | > 92% |
| Wire-to-water | P_hidrolik / P_elektrik | > 65% |
| Exergy verimi | ≈ Wire-to-water | > 60% |

## Özel Kurallar

### Wire-to-Water Değerlendirmesi
```
- > 70%: Mükemmel
- 60-70%: İyi
- 50-60%: Ortalama
- 40-50%: Düşük
- < 40%: Kritik (muhtemelen throttle veya aşırı boyut)
```

### VSD Tasarruf Potansiyeli
```
Affinity Laws:
- Debi ∝ Hız
- Head ∝ Hız²
- Güç ∝ Hız³

%50 debi için:
- Throttle: Güç ≈ %80-90 (vana kaybı)
- VSD: Güç ≈ %12.5-20 (kübik yasa)

Tasarruf potansiyeli: %30-70 (yük profiline bağlı)
```

### VSD Uygunluk Kriterleri
```
VSD öner eğer:
- Kontrol yöntemi = throttle VEYA bypass VE
- Motor gücü > 5 kW VE
- Değişken debi ihtiyacı var VE
- Statik head oranı < %60 (yoksa tasarruf düşük)
```

### Statik Head Uyarısı
```
Statik head / Toplam head oranı:
- < 30%: VSD çok etkili
- 30-60%: VSD etkili
- > 60%: VSD etkisi sınırlı, dikkatli değerlendir
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| VSD retrofit | %30-50 | €200-400/kW | 1-2 yıl |
| Impeller trim | %10-25 | €500-2000 | 0.5-1 yıl |
| Throttle eliminasyonu | %20-40 | Değişken | 1-2 yıl |
| Motor upgrade (IE3→IE4) | %2-4 | €100-200/kW | 3-5 yıl |
| Boru sistemi optimizasyonu | %5-15 | Değişken | 1-3 yıl |

## Throttle Analizi

```
Throttle kayıp hesabı:
P_kayıp = ρ × g × Q × ΔH_vana / 1000 (kW)

ΔH_vana = Vana basınç düşüşü (m)
```
