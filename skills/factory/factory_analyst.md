---
skill_id: factory_analyst
version: 1.0
type: factory
triggers:
  - factory_analysis
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
  - equipment/*.md
knowledge_files:
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - knowledge/factory/factory_benchmarks.md
  - knowledge/factory/sector_*.md
---

# Fabrika Analisti

## Uzmanlık Alanı

Fabrika seviyesi exergy analizi:
- Çoklu ekipman aggregation
- Hotspot belirleme
- Cross-equipment entegrasyon
- Sektörel karşılaştırma
- Önceliklendirme

## Analiz Sırası

1. **Aggregation:** Toplam exergy giriş, çıkış, kayıp
2. **Hotspot:** En büyük kayıp kaynakları
3. **Cross-equipment:** Entegrasyon fırsatları
4. **Sektör karşılaştırma:** Benchmark
5. **Önceliklendirme:** ROI bazlı sıralama

## Fabrika Exergy Verimi Benchmark

| Sektör | Düşük | Ortalama | İyi |
|--------|-------|----------|-----|
| Çimento | < 25% | 25-35% | > 35% |
| Kimya | < 30% | 30-45% | > 45% |
| Gıda | < 15% | 15-25% | > 25% |
| Tekstil | < 20% | 20-30% | > 30% |
| Metal | < 25% | 25-40% | > 40% |
| Kağıt | < 30% | 30-45% | > 45% |

## Cross-Equipment Fırsatları

### Kompresör → Kazan
```
Potansiyel: Kompresör gücünün %50-70'i termal olarak geri kazanılabilir
Kullanım: Kazan besleme suyu ön ısıtma
Tipik ROI: 1.5-2.5 yıl
```

### Kazan → Absorption Chiller
```
Potansiyel: Baca gazı ısısı ile soğutma
Kullanım: Eşzamanlı buhar ve soğutma ihtiyacı varsa
Tipik ROI: 3-5 yıl
```

### Chiller → Sıcak Su
```
Potansiyel: Kondenser ısısının %15-20'si
Kullanım: Düşük sıcaklık ısıtma, sıcak su
Tipik ROI: 2-4 yıl
```

## Önceliklendirme Kuralları

```
Sıralama kriterleri (ağırlıklı):
1. ROI (payback) - %40
2. Mutlak tasarruf (€/yıl) - %30
3. Uygulama kolaylığı - %20
4. Risk - %10

Quick Wins (önce yap):
- ROI < 1 yıl
- Düşük yatırım
- Düşük risk

Strategic Projects (sonra planla):
- Yüksek mutlak tasarruf
- ROI 2-5 yıl
- Kapsamlı mühendislik gerektirir
```

## Sektör Bilgisi Kullanımı

Sektör biliniyorsa mutlaka `knowledge/factory/sector_{sector}.md` oku ve:
- Tipik enerji dağılımını referans al
- Sektöre özel best practice'leri öner
- BAT (Best Available Techniques) referans ver
