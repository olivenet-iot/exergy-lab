---
skill_id: boiler_expert
version: 1.0
type: equipment
equipment_type: boiler
triggers:
  - single_equipment_analysis
  - equipment_type == "boiler"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/boiler/benchmarks.md
  - knowledge/boiler/formulas.md
  - knowledge/boiler/audit.md
  - knowledge/boiler/equipment/*.md
  - knowledge/boiler/solutions/*.md
---

# Kazan Uzmanı

## Uzmanlık Alanı

Buhar ve sıcak su kazanları exergy analizi:
- Ateş borulu, su borulu kazanlar
- Yanma optimizasyonu
- Ekonomizer, hava ön ısıtıcı
- Blowdown, kondensat geri dönüş

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Enerji verimi | Q_buhar / Q_yakıt | > 88% |
| Exergy verimi | Ex_buhar / Ex_yakıt | > 38% |
| Baca gazı sıcaklığı | Ölçüm | < 180°C |
| Fazla hava | O2 veya CO2 ölçümü | 10-15% |
| Blowdown oranı | | < 3% |

## Özel Kurallar

### Exergy Verimi Değerlendirmesi
```
Buhar kazanı için:
- > 40%: İyi
- 35-40%: Ortalama
- 30-35%: Düşük
- < 30%: Kritik (acil müdahale)

Not: Exergy verimi her zaman enerji veriminden düşüktür!
Tipik: Enerji %88 iken Exergy %35
```

### Ekonomizer Önerisi
```
Ekonomizer öner eğer:
- Baca gazı sıcaklığı > 180°C VE
- Kazan kapasitesi > 1 ton/h buhar
- ROI genellikle < 1.5 yıl
```

### Yanma Optimizasyonu
```
O2 seviyesi kontrolü:
- < 2%: Eksik yanma riski
- 2-4%: Optimum
- > 5%: Fazla hava kaybı

Her %1 fazla hava ≈ %0.5 verim kaybı
```

## Exergy Kayıp Dağılımı (Tipik)

| Kayıp Kaynağı | Oran |
|---------------|------|
| Yanma irreversibility | 25-30% |
| Baca gazı kaybı | 8-15% |
| Isı transferi irreversibility | 5-10% |
| Blowdown | 1-3% |
| Radyasyon | 1-2% |

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Ekonomizer | %3-6 yakıt | €20-40K | 0.8-1.5 yıl |
| O2 trim | %1-3 yakıt | €5-15K | 0.5-1 yıl |
| Blowdown heat recovery | %1-2 yakıt | €5-10K | 1-2 yıl |
| Kondensat geri dönüş | %1/her %10 artış | Değişken | 0.5-1 yıl |
| İzolasyon | %1-2 | €3-8K | 0.5-1 yıl |
