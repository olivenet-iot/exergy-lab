---
skill_id: exergy_fundamentals
version: 1.0
type: core
---

# Exergy Temelleri

## Temel Kavramlar

### Exergy Nedir?
Exergy, bir sistemin çevresiyle dengeye gelene kadar yapabileceği maksimum iştir. Enerji korunur ama exergy yok olur (2. Yasa).

### Exergy vs Enerji
- **Enerji verimi:** Çıkış/Giriş enerji oranı
- **Exergy verimi:** Çıkış/Giriş exergy oranı (termodinamik kalite)

### Neden Exergy?
Kazan %88 enerji verimi gösterebilir ama %35 exergy verimi. Exergy gerçek iyileştirme potansiyelini gösterir.

## Exergy Hesaplama Temelleri

### Fiziksel Exergy
```
ex_physical = (h - h₀) - T₀(s - s₀)
```
- h: Entalpi
- s: Entropi
- ₀: Referans çevre koşulları (T₀=25°C, P₀=1 atm)

### Kimyasal Exergy
Yakıtlar için:
```
Ex_fuel = m_fuel × LHV × φ
```
- φ: Kimyasal exergy faktörü (~1.04-1.08 hidrokarbonlar için)

### Exergy Yıkımı (İrreversibl)
```
I = Ex_in - Ex_out - Ex_useful
```

## Benchmark Değerlendirme Kuralları

| Exergy Verimi | Değerlendirme |
|---------------|---------------|
| > 50% | Mükemmel |
| 40-50% | İyi |
| 30-40% | Ortalama |
| 20-30% | Düşük |
| < 20% | Kritik |

Bu değerler ekipman tipine göre ayarlanmalı (bkz. equipment skills).
