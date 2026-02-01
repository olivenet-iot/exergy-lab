---
skill_id: integration_expert
version: 1.0
type: factory
triggers:
  - factory_analysis
  - cross_equipment_opportunities
dependencies:
  - factory/factory_analyst.md
knowledge_files:
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/heat_integration.md
  - knowledge/factory/waste_heat_recovery.md
  - knowledge/factory/pinch_analysis.md
---

# Entegrasyon Uzmanı

## Uzmanlık Alanı

Ekipmanlar arası enerji/exergy entegrasyonu:
- Atık ısı geri kazanımı
- Isı değiştirici ağı tasarımı
- Pinch analizi temelleri
- Kojenerasyon fırsatları

## Entegrasyon Matrisi

| Kaynak | Sıcaklık | Potansiyel Kullanım |
|--------|----------|---------------------|
| Kompresör atık ısısı | 70-90°C | Besleme suyu, bina ısıtma |
| Kazan baca gazı | 150-250°C | Ekonomizer, hava ön ısıtma |
| Kazan blowdown | 100-180°C | Flash tank, ön ısıtma |
| Chiller kondenser | 35-45°C | Düşük sıcaklık ısıtma |
| Fırın egzozu | 200-400°C | Buhar üretimi, ORC |

## Eşleştirme Kuralları

```
Isı transferi için:
ΔT_min = 10-20°C (minimum sıcaklık farkı)

Sıcaklık eşleştirmesi:
- Kaynak sıcaklığı > Hedef sıcaklığı + ΔT_min

Örnek:
Kompresör: 85°C
Besleme suyu: 20°C → 60°C
ΔT = 85 - 60 = 25°C > 10°C ✓ Uygun
```

## Yatırım Tahminleri

| Teknoloji | Maliyet | Birim |
|-----------|---------|-------|
| Plakali eşanjör | €100-200 | /kW |
| Ekonomizer | €150-300 | /kW |
| Heat recovery unit | €200-400 | /kW |
| Absorption chiller | €300-500 | /kW soğutma |
| ORC sistemi | €2000-4000 | /kW elektrik |

## Dikkat Edilecekler

1. **Mesafe:** Kaynak-hedef arası mesafe maliyeti artırır
2. **Senkronizasyon:** Kaynak ve hedef aynı anda mı çalışıyor?
3. **Güvenilirlik:** Entegrasyon sistem güvenilirliğini etkiler mi?
4. **Bakım:** Ek bakım ihtiyacı
5. **Legionella riski:** 25-45°C su stagnasyonu önlenmeli
