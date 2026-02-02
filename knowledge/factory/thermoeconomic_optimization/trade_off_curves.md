---
title: "Ödünleşim Eğrileri (Trade-off Curves)"
category: thermoeconomic_optimization
keywords: [ödünleşim eğrileri, maliyet-verimlilik dengesi, Pareto, optimal nokta, karbon fiyatı etkisi]
related_files: [knowledge/factory/thermoeconomic_optimization/multi_objective.md, knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md, knowledge/factory/thermoeconomic_optimization/practical_guide.md]
use_when: ["Verimlilik-maliyet ödünleşimi analiz edilirken", "Karbon fiyatlamasının optimal noktaya etkisi sorulduğunda"]
priority: medium
last_updated: 2026-02-02
---

# Ödünleşim Eğrileri (Trade-off Curves)

## 1. Temel Kavram

### 1.1. Verimlilik-Maliyet Ödünleşimi

Termoekonomik optimizasyonun temel çıktısı, **verimlilik ile maliyet arasındaki ödünleşim
eğrisidir** (trade-off curve):

```
C_total
(€/yıl)    │
           │╲
           │  ╲  Yatırım maliyeti baskın bölge
           │    ╲
           │      ╲___
           │          ╲___
           │              ╲___
           │     Optimal      ╲___  Yakıt maliyeti baskın bölge
           │     nokta ●          ╲___
           │                          ╲___
           │                              ╲
           └──────────────────────────────────→ η_ex (%)
              Düşük verim                Yüksek verim
              Düşük yatırım             Yüksek yatırım
              Yüksek yakıt maliyeti     Düşük yakıt maliyeti
```

### 1.2. Eğri Şekilleri

| Eğri Tipi | Özellik | Yorum |
|-----------|---------|-------|
| **Konveks** (U-şekilli) | Açık minimum noktası var | En yaygın, tek optimal |
| **Düz tabanlı** | Geniş minimum bölgesi | Farklı çözümler benzer maliyet |
| **Asimetrik** | Minimum sol veya sağda | Yakıt veya yatırım çok baskın |
| **S-eğrisi** | Basamaklı iyileşme | Teknoloji sıçramaları (CHP ekleme) |

---

## 2. Ekipman Bazlı Ödünleşim Verileri

### 2.1. Kazan (3,000 kW, Doğalgaz)

| η_ex [%] | C_fuel [k€/yıl] | C_invest [k€/yıl] | C_total [k€/yıl] | Ana Değişiklik |
|---------|-----------------|------------------|-----------------|----------------|
| 25.0 | 750 | 12.0 | 762.0 | Baz durum, iyileştirmesiz |
| 27.0 | 710 | 14.0 | 724.0 | Fazla hava optimizasyonu |
| 29.0 | 672 | 16.5 | 688.5 | + Economizer (30 m²) |
| 31.0 | 645 | 19.0 | 664.0 | + Economizer (60 m²) + T_fw artışı |
| **31.8** | **635** | **20.5** | **655.5** | **Optimal nokta** |
| 33.0 | 620 | 24.0 | 644.0 | + Air preheater |
| 34.0 | 608 | 30.0 | 638.0 | + Yoğuşmalı (condensing) |
| 35.0 | 598 | 42.0 | 640.0 | + İleri geri kazanım |
| 36.0 | 590 | 58.0 | 648.0 | Aşırı yatırım bölgesi |

> **Gözlem:** η_ex %31.8'den sonra yatırım artışı, yakıt tasarrufunu geçmeye başlar.
> Yoğuşmalı kazan (η_ex ~%34) maliyet-etkin olabilir ama ek yatırım yüksektir.

### 2.2. Kompresör (75 kW, Vidalı)

| η_ex [%] | C_elec [k€/yıl] | C_invest [k€/yıl] | C_total [k€/yıl] | Ana Değişiklik |
|---------|-----------------|------------------|-----------------|----------------|
| 32.0 | 52.0 | 5.5 | 57.5 | Baz durum |
| 35.0 | 48.5 | 6.0 | 54.5 | Basınç optimizasyonu |
| 38.0 | 45.0 | 6.8 | 51.8 | + VSD |
| 40.0 | 42.5 | 7.5 | 50.0 | + Isı geri kazanım |
| **42.0** | **40.0** | **8.5** | **48.5** | **Optimal nokta** |
| 44.0 | 38.0 | 10.5 | 48.5 | + IE4 motor, gelişmiş kontrol |
| 46.0 | 36.0 | 14.0 | 50.0 | Yüksek verimli yeni makine |
| 48.0 | 34.5 | 20.0 | 54.5 | Premium makine + tam paket |

### 2.3. Chiller (300 kW, Santrifüj)

| η_ex [%] | C_elec [k€/yıl] | C_invest [k€/yıl] | C_total [k€/yıl] | COP |
|---------|-----------------|------------------|-----------------|-----|
| 18.0 | 42.0 | 8.0 | 50.0 | 4.5 |
| 22.0 | 36.0 | 9.5 | 45.5 | 5.0 |
| 25.0 | 32.5 | 11.0 | 43.5 | 5.5 |
| **27.0** | **30.0** | **12.5** | **42.5** | **5.8 (Optimal)** |
| 29.0 | 28.0 | 14.5 | 42.5 | 6.0 |
| 31.0 | 26.5 | 18.0 | 44.5 | 6.3 |
| 33.0 | 25.0 | 24.0 | 49.0 | 6.5 |

### 2.4. Isı Değiştirici (Economizer)

| A [m²] | η_HX [%] | C_fuel_save [k€/yıl] | C_invest [k€/yıl] | Net Tasarruf [k€/yıl] |
|--------|---------|---------------------|------------------|---------------------|
| 10 | 55 | 35.0 | 2.8 | 32.2 |
| 20 | 65 | 48.0 | 4.5 | 43.5 |
| 40 | 75 | 58.0 | 7.2 | 50.8 |
| **60** | **80** | **63.0** | **9.8** | **53.2 (Optimal)** |
| 80 | 83 | 65.5 | 12.5 | 53.0 |
| 120 | 86 | 68.0 | 17.5 | 50.5 |
| 200 | 89 | 70.0 | 27.0 | 43.0 |

---

## 3. Fabrika Seviyesi Ödünleşim

### 3.1. Toplam Exergy Verimi vs Yıllıklaştırılmış Maliyet

Tekstil fabrikası (kazan 2,000 kW + kompresör 75 kW + chiller 300 kW + pompa 50 kW):

| η_ex,fab [%] | C_total [k€/yıl] | Konfigürasyon | Yatırım [k€] |
|-------------|-----------------|---------------|-------------|
| 22.0 | 520 | Mevcut durum (baz) | 0 (ek) |
| 24.5 | 490 | Quick wins (basınç opt., VSD) | 25 |
| 27.0 | 465 | + Economizer, kompresör ısı GK | 55 |
| 29.5 | 445 | + Chiller optimizasyonu, tam VSD | 85 |
| **31.5** | **432** | **Optimal parametrik** | **110** |
| 33.0 | 430 | + İleri ısı entegrasyonu | 160 |
| 35.0 | 435 | + CHP (küçük ICE) | 350 |
| 38.0 | 428 | CHP + absorpsiyonlu chiller | 500 |
| 40.0 | 440 | Tam trijenerasyon | 650 |

> **Gözlem:** Yapısal değişiklik (CHP ekleme) %35 civarında S-eğrisi kırılmasına neden olur.
> Parametrik optimizasyon η_ex = %31.5'te optimum, ama CHP ile %38'e çıkılabilir.

### 3.2. Yatırım Getirisi Perspektifi

| Adım | Ek Yatırım [k€] | Yıllık Tasarruf [k€] | SPP [yıl] | ROI [%] |
|------|-----------------|---------------------|-----------|---------|
| Quick wins | 25 | 30 | 0.8 | 120 |
| Economizer + ısı GK | 30 | 25 | 1.2 | 83 |
| Chiller + VSD | 30 | 20 | 1.5 | 67 |
| İleri entegrasyon | 50 | 15 | 3.3 | 30 |
| CHP (ICE) | 240 | 12 | 20 | 5 |

> **Dikkat:** İlk adımlar çok yüksek ROI sağlar (low-hanging fruit). CHP gibi büyük
> yapısal kararlar, yalnızca enerji fiyatları yüksekse veya karbon maliyeti varsa ekonomik olur.

---

## 4. Karbon Fiyatlaması Etkisi

### 4.1. Optimal Nokta Kayması

Karbon fiyatı arttıkça, optimal verimlilik noktası sağa (yüksek verime) kayar:

| c_CO₂ [€/tCO₂] | η_ex,opt [%] | C_total,opt [k€/yıl] | Optimal Konfigürasyon |
|----------------|-------------|---------------------|---------------------|
| 0 | 31.5 | 432 | Parametrik optimal (kazan+economizer) |
| 50 | 33.0 | 480 | + İleri ısı entegrasyonu |
| 80 | 35.0 | 512 | CHP değerlendirmesi başlar |
| 100 | 37.0 | 530 | CHP ekonomik hale gelir |
| 150 | 39.0 | 560 | CHP + absorpsiyonlu chiller |

### 4.2. Grafik Yorumlama

```
C_total                    c_CO₂ = 0
(k€/yıl)  │               c_CO₂ = 50
           │               c_CO₂ = 100
   700 ─── │  ╲ ╲ ╲
           │    ╲  ╲  ╲
   600 ─── │      ╲   ╲  ╲
           │        ╲    ╲   ╲
   500 ─── │     ●₀   ╲    ●₅₀  ╲
           │              ╲       ╲  ●₁₀₀
   400 ─── │                ╲        ╲
           │                  ╲        ╲
   300 ─── │                    ╲        ╲
           └─────┬────┬────┬────┬────┬────→ η_ex (%)
                 28   30   32   34   36   38

●₀: Optimal c_CO₂ = 0 → η_ex = 31.5%
●₅₀: Optimal c_CO₂ = 50 → η_ex = 33.0%
●₁₀₀: Optimal c_CO₂ = 100 → η_ex = 37.0%
```

> **Çıkarım:** Karbon fiyatı 100 €/tCO₂ olduğunda, optimal exergy verimi %31.5'ten
> %37'ye kayar — bu, CHP gibi büyük yapısal yatırımları ekonomik kılar.

---

## 5. Marjinal Maliyet Analizi

### 5.1. Marjinal Exergy Tasarrufu Maliyeti

```
MC_ex = dC_total / dη_ex    [€/yıl per %]

Düşük η_ex'te: MC_ex negatif (tasarruf > yatırım, free lunch)
Optimal noktada: MC_ex = 0 (marjinal tasarruf = marjinal yatırım)
Yüksek η_ex'te: MC_ex pozitif (yatırım > tasarruf)
```

### 5.2. Marjinal CO₂ Azaltma Maliyeti (MAC)

```
MAC = ΔC_total / ΔCO₂    [€/tCO₂]

Karar kuralı:
  MAC < c_CO₂ → Yatırım yap (karbon fiyatından ucuz)
  MAC > c_CO₂ → Yatırım yapma (karbon vergisi öde)
```

| Önlem | ΔCO₂ [ton/yıl] | ΔC_total [k€/yıl] | MAC [€/tCO₂] |
|-------|----------------|-------------------|---------------|
| Fazla hava optimizasyonu | 120 | -30 (tasarruf) | -250 (negatif = karlı) |
| Economizer | 200 | -25 | -125 |
| VSD (kompresör) | 35 | -8 | -229 |
| İleri ısı GK | 80 | -2 | -25 |
| CHP (ICE) | 350 | +8 | +23 |
| Abs. chiller | 50 | +5 | +100 |

> **Yorum:** MAC negatif olan önlemler, karbon fiyatı olmasa bile ekonomiktir ("no regret"
> önlemler). CHP'nin MAC'ı 23 €/tCO₂ — karbon fiyatı 50 €/t üzerindeyse ekonomik.

---

## 6. Ödünleşim Eğrisi Oluşturma Yöntemi

### 6.1. Epsilon-Constraint ile

```
1. η_ex aralığını belirle: [η_min, η_max]
2. N nokta seç (tipik 20-50)
3. Her nokta için:
   min C_total(x)
   s.t. η_ex(x) ≥ η_target
4. Sonuçları çiz: (η_ex, C_total) noktaları
```

### 6.2. Pareto Cephesinden

```
1. NSGA-II ile çok amaçlı optimizasyon yap
2. Pareto cephesini elde et (100+ nokta)
3. Noktaları η_ex'e göre sırala
4. Ödünleşim eğrisi = Pareto cephesinin 2D projeksiyonu
```

---

## 7. Yorumlama Rehberi

### 7.1. Eğri Bölgeleri

| Bölge | η_ex Aralığı | Yorum | Aksiyon |
|-------|-------------|-------|---------|
| Düşük verim | < η_ex,opt - 5pp | Açık iyileştirme fırsatı | Hemen uygula |
| Optimal yakın | η_ex,opt ± 2pp | Maliyet farkı küçük | Robust çözüm seç |
| Yüksek verim | > η_ex,opt + 5pp | Pahalı bölge | Yalnızca karbon maliyetiyle |
| Aşırı verim | > η_ex,opt + 10pp | Ekonomik olmayan | Kaçın |

### 7.2. Karar Verici İçin Özet

```
1. Mevcut durum noktasını eğri üzerinde işaretle
2. Optimal noktaya olan mesafeyi belirle
3. Mesafe büyükse → Yatırım yapılmalı
4. Mesafe küçükse → Mevcut durum yeterli
5. Karbon fiyatı senaryolarını kontrol et
6. Robust bölgeyi seç (optimal ± %2)
```

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `multi_objective.md` — Pareto analizi
- `sensitivity_analysis.md` — Parametre duyarlılığı
- `practical_guide.md` — Uygulama rehberi
- `objective_functions.md` — Maliyet formülasyonu

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions." *Energy Conversion and Management*, 43, 1259-1270.
