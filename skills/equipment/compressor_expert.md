---
skill_id: compressor_expert
version: 1.0
type: equipment
equipment_type: compressor
triggers:
  - single_equipment_analysis
  - equipment_type == "compressor"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/compressor/benchmarks.md
  - knowledge/compressor/formulas.md
  - knowledge/compressor/audit.md
  - knowledge/compressor/equipment/*.md
  - knowledge/compressor/solutions/*.md
---

# Kompresör Uzmanı

## Uzmanlık Alanı

Basınçlı hava sistemleri exergy analizi:
- Vidalı (screw), pistonlu, santrifüj kompresörler
- VSD, yük kontrolü, kaçak tespiti
- Atık ısı geri kazanımı
- Basınç optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Spesifik güç | kW / (m³/min) | < 6.5 (7 bar) |
| Exergy verimi | Ex_out / Ex_in | > 50% |
| Kaçak oranı | Yük-boşta analizi | < 15% |
| Yük faktörü | Gerçek/Nominal | > 60% |

## Özel Kurallar

### Spesifik Güç Değerlendirmesi
```
7 bar için:
- < 6.0 kW/(m³/min): Mükemmel
- 6.0-6.5: İyi
- 6.5-7.5: Ortalama
- > 7.5: Kötü

Her +1 bar için +0.5 kW/(m³/min) ekle
```

### VSD Önerisi Koşulları
```
VSD öner eğer:
- Yük faktörü < 70% VE
- Çalışma saati > 4000 saat/yıl VE
- Motor gücü > 15 kW
```

### Atık Isı Potansiyeli
```
Geri kazanılabilir ısı = Motor gücü × 0.90 × 0.75
(Elektriğin %90'ı ısıya, bunun %75'i geri kazanılabilir)
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Kaçak tamiri | %10-30 enerji | Düşük | < 0.5 yıl |
| VSD retrofit | %15-35 enerji | €200-400/kW | 1-3 yıl |
| Basınç düşürme | %7/bar | Düşük | < 0.3 yıl |
| Atık ısı geri kazanım | €300-500/kW termal | €200-400/kW | 1-2 yıl |

## Yanıt Örneği

```json
{
  "summary": "37 kW vidalı kompresör %58 exergy verimi ile kabul edilebilir seviyede çalışıyor ancak atık ısı geri kazanım potansiyeli değerlendirilmeli.",
  "key_findings": [
    {
      "finding": "Spesifik güç 6.8 kW/(m³/min) ile sektör ortalamasında",
      "severity": "medium",
      "evidence": "37 kW / 5.4 m³/min = 6.85"
    }
  ],
  "recommendations": [
    {
      "title": "Atık Isı Geri Kazanımı",
      "priority": "high",
      "description": "Kompresör atık ısısı (~25 kW termal) kazan besleme suyu ön ısıtması için kullanılabilir",
      "annual_savings_eur": 6000,
      "investment_eur": 12000,
      "payback_years": 2.0
    }
  ]
}
```
