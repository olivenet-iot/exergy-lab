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

## EGM Bazlı Tasarım Kuralları

### Genleşme Vanası — En Büyük Entropi Kaynağı
Buhar sıkıştırmalı soğutma çevriminde genleşme vanası toplam S_gen'in %30-40'ını oluşturur:
```
S_gen_exp = ṁ_ref × (s_out - s_in)   [kW/K]
```
İzentalpik genleşme (h_in = h_out) tamamen irreversible bir süreçtir. Azaltma yolları:
- Ejektör: Genleşme enerjisinin %15-20'sini geri kazanır → S_gen %15-20 azalır
- Turbo-ekspander: Mil işi olarak geri kazanım → S_gen %30-50 azalır
- Ekonomizer (subcooling): Flash gaz oranını düşürür → etkin S_gen azalır
- Kaskad sistem: Basınç farkını kademelere böler

### Optimum Evaporatör/Kondenser Approach Temperature
```
Approach_opt: min(S_gen_ΔT + S_gen_ΔP) → tipik 3-5°C
```
- Her 1°C kondenser approach azalması → COP %2-3 artar
- Her 1°C evaporatör approach azalması → COP %2-4 artar
- Kondenser optimizasyonu genellikle daha etkilidir (ortam sıcaklığına yakın, büyük ΔT)

### Bejan Sayısı — Chiller Bileşenleri
| Bileşen | Tipik Be | Baskın Kaynak | Aksiyon |
|---------|----------|---------------|---------|
| Kondenser | 0.60-0.80 | Isı transferi | Approach temp düşür, temizle |
| Evaporatör | 0.50-0.70 | Isı transferi | Approach temp düşür |
| Kompresör | 0.25-0.45 | Sürtünme | Verimli kompresör seç |
| Genleşme vanası | N/A | Throttling | Ejektör/subcooling değerlendir |

### Soğutucu Akışkan ve EGM
- R-134a: Dengeli performans, yaygın
- R-1234yf/ze: Düşük GWP, benzer S_gen profili
- R-290 (propan): Yüksek COP → düşük S_gen, ama yanıcılık riski
- R-744 (CO₂): Transkritik çevrimde yüksek throttling S_gen, kompakt ekipman

Detaylı bilgi: `knowledge/factory/entropy_generation/refrigeration_egm.md`

## İleri Exergy Referans Değerleri

### Kaçınılamaz Koşullar (Chiller)
| Parametre | Kaçınılamaz Değer | Kaynak |
|-----------|-------------------|--------|
| COP referansı | COP_Carnot × 0.60-0.70 | Morosuk & Tsatsaronis 2011 |
| Kompresör η_is — Santrifüj | 0.82-0.88 | BAT referansı |
| Kompresör η_is — Vidalı | 0.78-0.84 | BAT referansı |
| Kondenser approach ΔT | 2-3°C | Shell&tube minimum |
| Evaporatör approach ΔT | 2-3°C | Shell&tube minimum |
| Genleşme | İzentalpik (vana) | Termodinamik limit |

### Tipik 4-Yollu Dekompozisyon (Santrifüj Chiller)
| Kategori | Tipik Oran | Açıklama |
|----------|-----------|----------|
| I_EN_AV | %28-38 | Kompresör verimi, approach temp iyileştirme |
| I_EN_UN | %35-45 | Termodinamik limit (Carnot) |
| I_EX_AV | %10-18 | Soğutma kulesi, kondenser suyu etkisi |
| I_EX_UN | %6-12 | Sistem yapısal limiti |

### Göreceli Kaçınılabilirlik (θ)
- Chiller tipik θ: 0.40-0.55 → ORTA-YÜKSEK
- Santrifüj θ ≈ 0.45-0.55, Vidalı θ ≈ 0.40-0.50, Scroll θ ≈ 0.35-0.45
- θ > 0.5 → Kondenser temizliği, VSD retrofit, soğutma kulesi optimizasyonu
- θ < 0.35 → Chiller iyi durumda, sistem entegrasyonuna odaklan

### Alt Bileşen Bazında θ
| Alt Bileşen | Tipik θ | En Etkili Aksiyon |
|-------------|---------|-------------------|
| Kompresör | 0.35-0.45 | VSD, verimli motor |
| Kondenser | 0.40-0.55 | Temizlik, soğutma kulesi opt. |
| Evaporatör | 0.25-0.40 | Approach temp azaltma |
| Genleşme vanası | 0.30-0.40 | Ejektör retrofit (ileri) |

Detaylı bilgi: `knowledge/factory/advanced_exergy/equipment_specific/chiller_advanced.md`

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Kondenser temizliği | %5-15 | Düşük | < 0.3 yıl |
| Soğutma kulesi optimizasyonu | %5-10 | €5-20K | 1-2 yıl |
| Free cooling | %20-40 | €20-50K | 2-4 yıl |
| VSD retrofit | %15-30 | €15-40K | 2-3 yıl |
| Kondenser ısı geri kazanım | €0.05/kWh | €10-25K | 2-4 yıl |
