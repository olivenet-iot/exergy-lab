---
title: "Çözümlü Örnek: Endüstriyel Tesis Exergoekonomik Analizi (Worked Example: Industrial Plant with ExergyLab Equipment)"
category: factory
equipment_type: factory
keywords: [endüstriyel tesis, ExergyLab, kazan, kompresör, chiller, pompa, eşanjör, SPECO, matris, önceliklendirme]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/matrix_formulation.md
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/exergoeconomic/optimization.md
  - factory/exergoeconomic/sensitivity_analysis.md
  - factory/cross_equipment.md
  - factory/prioritization.md
  - factory/exergoeconomic/worked_examples/simple_cycle.md
  - factory/exergoeconomic/worked_examples/cogeneration.md
use_when:
  - "ExergyLab ekipman tiplerini içeren tesis analizi yapılacakken"
  - "Çapraz ekipman exergoekonomik değerlendirme gerektiğinde"
  - "Gerçek endüstriyel tesis senaryosu örneği istendiğinde"
  - "Geleneksel ve exergoekonomik yöntem karşılaştırması yapılacakken"
priority: high
last_updated: 2026-02-01
---
# Çözümlü Örnek: Endüstriyel Tesis Exergoekonomik Analizi

> Son güncelleme: 2026-02-01

## 1. Problem Tanımı

Bir gıda işleme tesisi için ExergyLab ekipman tipleri (kazan, kompresör, chiller, pompa, eşanjör) kullanılarak tam exergoekonomik analiz yapılacaktır. Bu örnek, ExergyLab platformunun analiz ettiği gerçekçi bir endüstriyel senaryoyu temsil eder.

```
Tesis Şeması:

                     Doğalgaz
                        ↓
                  ┌──────────┐  Buhar (10 bar)
                  │          │─────────────────────→ Proses
                  │  KAZAN   │                      hattı
                  │  (B)     │
                  │          │  Baca gazı
                  └──────────┘─────┐
                       ↑           │
            Besleme    │     ┌──────────┐
            suyu ──────┘     │ EŞANJÖR  │ (baca gazı → besleme suyu)
                             │  (HX)   │
                             └──────────┘
                                  │
                                  ↓ Baca gazı (soğutulmuş)
                              Atmosfer

    ┌──────────┐  Basınçlı hava
    │KOMPRESÖR │──────────────────→ Üretim hattı
    │  (C)     │
    │          │─── Atık ısı (80°C) ──→ [Potansiyel geri kazanım]
    └──────────┘
         ↑
     Elektrik

    ┌──────────┐  Soğuk su (7°C)
    │ CHILLER  │──────────────────→ Proses soğutma
    │  (CH)    │
    │          │
    └──────────┘
         ↑
     Elektrik

    ┌──────────┐  Basınçlı su
    │  POMPA   │──────────────────→ Su dağıtım
    │  (P)     │                     sistemi
    │          │
    └──────────┘
         ↑
     Elektrik

Bileşenler: Kazan (B), Eşanjör (HX), Kompresör (C), Chiller (CH), Pompa (P)
Toplamda 5 bileşen
```

### 1.1 Tesis Parametreleri

```
KAZAN (B) — Ateş Borulu Buhar Kazanı:
  Yakıt: Doğalgaz (LHV = 47,100 kJ/kg)
  Yakıt debisi: ṁ_fuel = 0.30 kg/s
  Buhar üretimi: ṁ_steam = 3.5 kg/s
  Buhar basıncı: P_steam = 10 bar
  Buhar sıcaklığı: T_steam = 185°C (doymuş)
  Besleme suyu giriş sıcaklığı: T_fw = 80°C (eşanjörden ısıtılmış)
  Baca gazı çıkış sıcaklığı: T_fg = 220°C
  Termal verim: η_th = 0.88

EŞANJÖR (HX) — Ekonomizer (Baca Gazı → Besleme Suyu):
  Sıcak taraf (baca gazı): T_h,in = 220°C, T_h,out = 130°C
  Soğuk taraf (besleme suyu): T_c,in = 25°C, T_c,out = 80°C
  Baca gazı debisi: ṁ_fg = 3.8 kg/s (c_p ≈ 1.05 kJ/(kg·K))
  Su debisi: ṁ_fw = 3.5 kg/s (c_p ≈ 4.18 kJ/(kg·K))
  Q̇_HX = 3.8 × 1.05 × (220-130) = 359.1 kW

KOMPRESÖR (C) — Vidalı Hava Kompresörü:
  Elektrik gücü: Ẇ_C = 110 kW
  Hava debisi: V̇ = 18 m³/min
  Giriş: T_in = 25°C, P_in = 1.013 bar
  Çıkış: T_out = 85°C, P_out = 8 bar
  İsentropic verim: η_s = 0.72
  Atık ısı: Q̇_atık = 85 kW (T_atık = 80°C)

CHILLER (CH) — Su Soğutmalı Vidalı Chiller:
  Soğutma kapasitesi: Q̇_cool = 350 kW
  Kompresör gücü: Ẇ_CH = 95 kW
  Soğuk su: T_chw,in = 12°C, T_chw,out = 7°C
  Kondenser: T_cw,in = 30°C, T_cw,out = 35°C
  COP = Q̇_cool / Ẇ_CH = 350 / 95 = 3.68

POMPA (P) — Santrifüj Su Pompası:
  Motor gücü: Ẇ_P = 15 kW
  Debi: V̇ = 50 m³/h
  Basma yüksekliği: H = 35 m
  Pompa verimi: η_P = 0.75
  Hidrolik güç: Ẇ_hyd = ρ×g×V̇×H = 1000×9.81×(50/3600)×35 = 4.77 kW
  [Not: Yardımcı pompa, ana proses hattını besler]

Genel:
  T₀ = 25°C = 298.15 K, P₀ = 1.013 bar
  τ = 7000 saat/yıl
  Sektör: Gıda işleme
  Elektrik fiyatı (şebeke): c_el = 0.10 €/kWh
  Doğalgaz fiyatı: c_fuel = 0.0378 €/kWh (10.5 €/GJ)
```

## 2. Termodinamik Analiz

### 2.1 Exergy Akışları

```
Referans durumu: T₀ = 298.15 K, P₀ = 1.013 bar

KAZAN (B):
  Yakıt exergy: Ė_fuel = ṁ_fuel × LHV × φ = 0.30 × 47,100 × 1.04
              = 14,695.2 kW
  Besleme suyu exergy (80°C, 12 bar):
    h_fw = 336.0 kJ/kg, s_fw = 1.075 kJ/(kg·K)
    ė_fw = (336.0 - 104.9) - 298.15 × (1.075 - 0.367) = 231.1 - 211.1 = 20.0 kJ/kg
    Ė_fw = 3.5 × 20.0 = 70.0 kW

  Buhar exergy (185°C, 10 bar, doymuş):
    h_steam = 2778.1 kJ/kg, s_steam = 6.586 kJ/(kg·K)
    ė_steam = (2778.1 - 104.9) - 298.15 × (6.586 - 0.367)
            = 2673.2 - 1854.3 = 818.9 kJ/kg
    Ė_steam = 3.5 × 818.9 = 2,866.2 kW

  Baca gazı exergy (220°C):
    ė_fg,220 = c_p × [(T-T₀) - T₀ × ln(T/T₀)]
             = 1.05 × [(493.15-298.15) - 298.15 × ln(493.15/298.15)]
             = 1.05 × [195 - 298.15 × 0.503] = 1.05 × [195 - 150.0]
             = 47.25 kJ/kg
    Ė_fg,220 = 3.8 × 47.25 = 179.6 kW

  Exergy bilançosu:
    Ė_F,B = Ė_fuel = 14,695.2 kW
    Ė_P,B = Ė_steam - Ė_fw = 2,866.2 - 70.0 = 2,796.2 kW
    Ė_fg (çıkış) = 179.6 kW (eşanjöre giden)
    Ė_D,B = 14,695.2 - 2,796.2 - 179.6 = 11,719.4 kW
    ε_B = 2,796.2 / 14,695.2 = 19.0%

    [Not: Burada Ė_fg kazan çıkışında kayıp değil, eşanjöre aktarılır.
     Ė_D,B hesabında baca gazının kazandan çıkışı dikkate alınır.]

EŞANJÖR (HX):
  Baca gazı giriş exergy: Ė_h,in = 179.6 kW (220°C)
  Baca gazı çıkış exergy (130°C):
    ė_fg,130 = 1.05 × [(403.15-298.15) - 298.15 × ln(403.15/298.15)]
             = 1.05 × [105 - 298.15 × 0.301] = 1.05 × [105 - 89.7]
             = 16.07 kJ/kg
    Ė_h,out = 3.8 × 16.07 = 61.1 kW

  Su giriş exergy (25°C): Ė_c,in ≈ 0 kW (referans durumunda)
  Su çıkış exergy (80°C, ~12 bar): Ė_c,out = 70.0 kW (yukarıda hesaplandı)

  Exergy bilançosu:
    Ė_F,HX = Ė_h,in - Ė_h,out = 179.6 - 61.1 = 118.5 kW
    Ė_P,HX = Ė_c,out - Ė_c,in = 70.0 - 0 = 70.0 kW
    Ė_D,HX = 118.5 - 70.0 = 48.5 kW
    ε_HX = 70.0 / 118.5 = 59.1%

KOMPRESÖR (C):
  Hava giriş exergy: Ė_air,in = 0 kW (atmosfer)
  Hava çıkış exergy (85°C, 8 bar):
    ė_air,out = c_p × [(T-T₀) - T₀ × ln(T/T₀)] + R × T₀ × ln(P/P₀)
              = 1.005 × [(358.15-298.15) - 298.15 × ln(358.15/298.15)]
                + 0.287 × 298.15 × ln(8/1.013)
              = 1.005 × [60 - 298.15 × 0.183] + 0.287 × 298.15 × 2.068
              = 1.005 × [60 - 54.6] + 176.9
              = 5.43 + 176.9 = 182.3 kJ/kg

    ṁ_air = ρ × V̇ = 1.225 × (18/60) = 0.3675 kg/s
    Ė_air,out = 0.3675 × 182.3 = 67.0 kW

  Atık ısı exergy (80°C):
    Ė_atık = Q̇_atık × (1 - T₀/T_atık) = 85 × (1 - 298.15/353.15)
           = 85 × 0.1557 = 13.2 kW

  Exergy bilançosu:
    Ė_F,C = Ẇ_C = 110 kW
    Ė_P,C = Ė_air,out - Ė_air,in = 67.0 - 0 = 67.0 kW
    Ė_D,C = 110 - 67.0 - 13.2 = 29.8 kW  [atık ısı exergy kayıp olarak]
    ε_C = 67.0 / 110 = 60.9%

    [Alternatif: Atık ısı geri kazanılırsa Ė_P,C = 67.0 + 13.2 = 80.2 kW]

CHILLER (CH):
  Ẇ_CH = 95 kW (elektrik girişi)
  Soğutma exergy'si:
    Ė_cool = Q̇_cool × |T₀/T_cool - 1|
           = 350 × |298.15/280.15 - 1| = 350 × 0.0642 = 22.5 kW
    [T_cool = (7+12)/2 = 9.5°C = 282.65 K, ortalama]
    [Düzeltme: T_cool = 280.15 K (7°C çıkış bazında)]

  Exergy bilançosu:
    Ė_F,CH = Ẇ_CH = 95 kW
    Ė_P,CH = Ė_cool = 22.5 kW
    Ė_D,CH = 95 - 22.5 = 72.5 kW
    ε_CH = 22.5 / 95 = 23.7%

POMPA (P):
  Exergy bilançosu:
    Ė_F,P = Ẇ_P = 15 kW
    Ė_P,P = Ẇ_hyd / η_motor ≈ ṁ × Δ(P×v) ≈ 4.77 kW (hidrolik güç)
    [Basitleştirme: Ė_P = akışkanın basınç exergy artışı]
    Ė_D,P = 15 - 4.77 = 10.23 kW
    ε_P = 4.77 / 15 = 31.8%

    [Not: Düşük verim — pompa aşırı boyutlu veya kısmalı çalışıyor olabilir]
```

### 2.2 Exergy Bilançosu Özet Tablosu

```
Tesis Exergy Bilançosu:

Bileşen    | Ė_F [kW]    | Ė_P [kW]   | Ė_D [kW]   | ε [%]  | Pay [%] |
-----------|-------------|-------------|-------------|--------|---------|
Kazan (B)  | 14,695.2    | 2,796.2     | 11,719.4    | 19.0   | 98.6    |
Eşanjör(HX)| 118.5       | 70.0        | 48.5        | 59.1   | 0.4     |
Kompresör  | 110.0       | 67.0        | 29.8        | 60.9   | 0.3     |
Chiller    | 95.0        | 22.5        | 72.5        | 23.7   | 0.6     |
Pompa (P)  | 15.0        | 4.77        | 10.23       | 31.8   | 0.1     |
TOPLAM     | —           | —           | 11,880.4    | —      | 100%    |

Geleneksel enerji analizi yorumu:
→ Kazan termal verimi %88 — "iyi"
→ Kompresör çalışıyor — "normal"

Exergy analizi gerçeği:
→ Kazan exergy verimi %19 — çok düşük (yanma irreversibilitesi)
→ Chiller exergy verimi %24 — düşük (Carnot sınırı etkisi)
→ Pompa exergy verimi %32 — düşük (muhtemelen aşırı boyutlu)
```

## 3. Ekonomik Analiz

### 3.1 Ekipman Maliyetleri

```
PEC ve Ż Hesaplaması:

Ekonomik parametreler:
  i = 12% (Türkiye reel WACC)
  n = 20 yıl
  φ = 0.06 (bakım faktörü)
  τ = 7000 saat/yıl

  CRF = 0.12 × (1.12)^20 / [(1.12)^20 - 1]
      = 0.12 × 9.6463 / [9.6463 - 1]
      = 1.1576 / 8.6463
      = 0.13388

  CRF + φ = 0.13388 + 0.06 = 0.19388

Bileşen    | PEC [€]     | Ż = PEC×(CRF+φ)/τ [€/saat] |
-----------|-------------|----------------------------|
Kazan (B)  | 280,000     | 7.76                       |
Eşanjör(HX)| 35,000      | 0.97                       |
Kompresör  | 25,000      | 0.69                       |
Chiller    | 85,000      | 2.36                       |
Pompa (P)  | 8,000       | 0.22                       |
TOPLAM     | 433,000     | 12.00                      |
```

## 4. Exergoekonomik Denge

### 4.1 F/P Tanımları

```
SPECO Fuel/Product Tanımları:

Kazan (B):
  Fuel: Ė_fuel = 14,695.2 kW (doğalgaz)
  Product: Ė_steam - Ė_fw = 2,796.2 kW

Eşanjör (HX):
  Fuel: Ė_fg,in - Ė_fg,out = 118.5 kW (baca gazı exergy azalışı)
  Product: Ė_fw,out - Ė_fw,in = 70.0 kW (besleme suyu exergy artışı)

Kompresör (C):
  Fuel: Ẇ_C = 110 kW (elektrik)
  Product: Ė_air,out - Ė_air,in = 67.0 kW (hava exergy artışı)

Chiller (CH):
  Fuel: Ẇ_CH = 95 kW (elektrik)
  Product: Ė_cool = 22.5 kW (soğutma exergy'si)

Pompa (P):
  Fuel: Ẇ_P = 15 kW (elektrik)
  Product: Ė_P,P = 4.77 kW (basınç exergy artışı)
```

### 4.2 Birim Maliyet Hesaplaması

```
Sınır Koşulları:
  c_fuel = 0.0378 €/kWh (doğalgaz)
  c_el = 0.10 €/kWh (şebeke elektriği)
  c_fw,in = 0.002 €/kWh (şebeke suyu, ihmal edilebilir)

Kazan:
  c_P,B = (c_fuel × Ė_fuel + Ż_B) / Ė_P,B
        = (0.0378 × 14,695.2 + 7.76) / 2,796.2
        = (555.5 + 7.76) / 2,796.2
        = 0.2015 €/kWh

  Not: Kazanın product birim maliyeti = buhar exergy birim maliyeti

Eşanjör:
  c_F,HX = c_fg (baca gazı birim maliyeti)
  Baca gazı maliyeti kazan product maliyetinden türetilir:
  c_fg = c_P,B × (paylaştırma) ≈ Kazan F-kuralı uygulanır

  Basitleştirme: c_fg ≈ c_fuel = 0.0378 €/kWh
  [Baca gazı yakıtın dönüştürülmüş hali, yakıt maliyeti ile değerlendirilir]

  c_P,HX = (c_fg × Ė_F,HX + Ż_HX) / Ė_P,HX
         = (0.0378 × 118.5 + 0.97) / 70.0
         = (4.48 + 0.97) / 70.0
         = 0.0779 €/kWh

Kompresör:
  c_P,C = (c_el × Ẇ_C + Ż_C) / Ė_P,C
        = (0.10 × 110 + 0.69) / 67.0
        = (11.0 + 0.69) / 67.0
        = 0.1744 €/kWh

Chiller:
  c_P,CH = (c_el × Ẇ_CH + Ż_CH) / Ė_P,CH
         = (0.10 × 95 + 2.36) / 22.5
         = (9.5 + 2.36) / 22.5
         = 0.5271 €/kWh

Pompa:
  c_P,P = (c_el × Ẇ_P + Ż_P) / Ė_P,P
        = (0.10 × 15 + 0.22) / 4.77
        = (1.5 + 0.22) / 4.77
        = 0.3606 €/kWh
```

### 4.3 Ürün Birim Maliyet Tablosu

```
Birim Exergy Maliyet Özeti:

Bileşen    | c_F [€/kWh] | c_P [€/kWh] | c_P [€/GJ] | Açıklama         |
-----------|-------------|-------------|------------|------------------|
Kazan      | 0.0378      | 0.2015      | 72.5       | Buhar üretimi    |
Eşanjör    | 0.0378      | 0.0779      | 28.0       | Su ısıtma        |
Kompresör  | 0.1000      | 0.1744      | 62.8       | Basınçlı hava    |
Chiller    | 0.1000      | 0.5271      | 189.8      | Soğutma          |
Pompa      | 0.1000      | 0.3606      | 129.8      | Basınçlı su      |

Yorum:
→ Chiller ürün maliyeti en yüksek (0.527 €/kWh)
  → Carnot limiti nedeniyle düşük exergy verimi → yüksek birim maliyet
→ Kazan ürün maliyeti 0.20 €/kWh
  → Yakıt ucuz ama yanma irreversibilitesi çok yüksek
→ Eşanjör en düşük ürün maliyeti (0.078 €/kWh)
  → "Bedava" baca gazı ısısını kullanıyor
→ Pompa ürün maliyeti yüksek (0.36 €/kWh)
  → Düşük verim nedeniyle (%32)
```

## 5. Exergoekonomik Değerlendirme

### 5.1 Ċ_D, f_k, r_k Hesaplaması

```
Bileşen Bazlı Değerlendirme:

Ċ_D,k = c_F,k × Ė_D,k

Bileşen  | Ė_D [kW] | c_F [€/kWh]| Ċ_D [€/sa]| Ż [€/sa]| Ċ_D+Ż [€/sa]| f_k   | r_k   |
---------|----------|-----------|----------|---------|-------------|-------|-------|
Kazan    |11,719.4  | 0.0378    | 442.99   | 7.76    | 450.75      | 0.017 | 4.331 |
Eşanjör  | 48.5     | 0.0378    | 1.83     | 0.97    | 2.80        | 0.346 | 1.061 |
Kompresör| 29.8     | 0.1000    | 2.98     | 0.69    | 3.67        | 0.188 | 0.744 |
Chiller  | 72.5     | 0.1000    | 7.25     | 2.36    | 9.61        | 0.246 | 4.271 |
Pompa    | 10.23    | 0.1000    | 1.02     | 0.22    | 1.24        | 0.177 | 2.606 |
```

### 5.2 Öncelik Sıralaması ve Karar Analizi

```
Ċ_D + Ż Sıralaması (toplam exergoekonomik maliyet):

1. KAZAN:     450.75 €/saat  (%96.3)
2. CHILLER:   9.61 €/saat    (%2.1)
3. KOMPRESÖR: 3.67 €/saat    (%0.8)
4. EŞANJÖR:   2.80 €/saat    (%0.6)
5. POMPA:     1.24 €/saat    (%0.3)
TOPLAM:       468.07 €/saat

══════════════════════════════════════════════════════
BİLEŞEN BAZLI DETAYLI ANALİZ
══════════════════════════════════════════════════════

KAZAN (B): f_k = 0.017, r_k = 4.33 | Ċ_D+Ż = 450.75 €/sa
─────────────────────────────────────────────────────
→ f_k << 0.25: Exergy yıkımı çok baskın (yatırım neredeyse sıfır etkili)
→ r_k = 4.33: Çok yüksek — ürün maliyeti yakıt maliyetinin 5.3 katı
→ Ė_D = 11,719 kW: Toplam yıkımın %98.6'sı
→ Yıllık maliyet: 450.75 × 7000 = 3,155,250 €/yıl

Aksiyon:
  ▸ Mevcut ekonomizer (HX) genişletilebilir → baca T: 130→80°C
  ▸ Hava ön ısıtıcı ekleme → yanma verimi artışı
  ▸ Buhar parametreleri optimizasyonu (P, T inceleme)
  ▸ Kondansat geri dönüşü iyileştirme
  ▸ Uyarı: Yanma irreversibilitesi termodinamik limit — trijenrasyon/CHP
    ile exergy kullanımı çeşitlendirilebilir

  Potansiyel iyileşme: ε_B: %19 → %25 (+6 puan)
  Ė_D azalma: ~2,200 kW → Ċ_D tasarruf: 83.2 €/saat → 582,400 €/yıl
  Yatırım tahmini: ~120,000 € → Geri ödeme: <0.3 yıl

CHILLER (CH): f_k = 0.246, r_k = 4.27 | Ċ_D+Ż = 9.61 €/sa
─────────────────────────────────────────────────────
→ f_k ≈ 0.25: Sınırda — hafif termodinamik baskınlık
→ r_k = 4.27: Çok yüksek (Carnot sınırı etkisi)
→ Ė_D = 72.5 kW: Mutlak değer orta

Aksiyon:
  ▸ Soğuk su set point artırma: 7°C → 10°C
    → Exergy verimi: %24 → %30 → Ė_D ~15 kW azalma
  ▸ Kondenser optimizasyonu (su sıcaklığını düşürme)
  ▸ VSD ekleme (kısmi yükte verim artışı)
  ▸ Serbest soğutma (free cooling) — kış aylarında

  Potansiyel iyileşme: ε_CH: %24 → %32
  Yıllık tasarruf: ~25,200 €/yıl
  Yatırım tahmini: ~15,000 € → Geri ödeme: <0.6 yıl

KOMPRESÖR (C): f_k = 0.188, r_k = 0.74 | Ċ_D+Ż = 3.67 €/sa
─────────────────────────────────────────────────────
→ f_k < 0.25: Termodinamik iyileştirme gerekli
→ r_k = 0.74: Orta-yüksek iyileştirme potansiyeli
→ Ė_D = 29.8 kW: Düşük mutlak değer

Aksiyon:
  ▸ Atık ısı geri kazanımı (80°C → besleme suyu ısıtma veya bina ısıtma)
    → 85 kW termal = ~13 kW exergy geri kazanım
  ▸ Hava kaçak kontrolü (basınçlı hava sistemi)
  ▸ Basınç ayarı (8 bar gerçekten gerekli mi? 7 bar yeterli olabilir)
  ▸ VSD değerlendirmesi

  Potansiyel iyileşme: ε_C: %61 → %70
  Yıllık tasarruf: ~14,000 €/yıl
  Yatırım tahmini: ~8,000 € → Geri ödeme: <0.6 yıl

EŞANJÖR (HX): f_k = 0.346, r_k = 1.06 | Ċ_D+Ż = 2.80 €/sa
─────────────────────────────────────────────────────
→ f_k ≈ 0.35: Orta aralıkta, hafif termodinamik baskınlık
→ r_k = 1.06: Orta — iyileştirme potansiyeli var
→ Ė_D = 48.5 kW: Düşük mutlak değer

Aksiyon:
  ▸ HX alanını artır → ΔT_min azalt → ε_HX ↑
  ▸ Karşı akış tasarımına geçiş (paralel akıştan)
  ▸ Baca gazı çıkışını 130°C → 90°C'ye düşürme
    (asit çiğ noktası dikkat — doğalgazda ~50°C, güvenli)

  Potansiyel iyileşme: ε_HX: %59 → %72
  Yıllık tasarruf: ~7,000 €/yıl
  Yatırım tahmini: ~12,000 € → Geri ödeme: ~1.7 yıl

POMPA (P): f_k = 0.177, r_k = 2.61 | Ċ_D+Ż = 1.24 €/sa
─────────────────────────────────────────────────────
→ f_k < 0.25: Termodinamik iyileştirme gerekli
→ r_k = 2.61: Yüksek — verim çok düşük
→ Ė_D = 10.2 kW: Düşük mutlak değer

Aksiyon:
  ▸ Pompa boyut kontrolü (aşırı boyutlu olabilir)
  ▸ Kısma vanası varsa → VSD ile değiştir
  ▸ Çark tornalama (impeller trimming)

  Potansiyel iyileşme: ε_P: %32 → %55
  Yıllık tasarruf: ~5,600 €/yıl
  Yatırım tahmini: ~4,000 € → Geri ödeme: <0.8 yıl
```

## 6. Çapraz Ekipman Entegrasyon Fırsatları

```
Exergoekonomik Perspektifle Çapraz Ekipman Analizi:

Fırsat 1: Kompresör Atık Isısı → Besleme Suyu Ön Isıtma
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Kaynak: Kompresör atık ısısı (80°C, 85 kW termal)
  Hedef: Kazan besleme suyu (25°C → 80°C ön ısıtma)
  Exergy kazanımı: ~13 kW exergy geri kazanım
  Maliyet kazanımı:
    c_atık,komp = c_el = 0.10 €/kWh (yakıt maliyeti olarak)
    Ama bu ısı "bedava" atık → c_F,yeni_HX ≈ 0
    Doğalgaz tasarrufu: 85 kW termal → ~97 kW yakıt
    = 0.0021 kg/s doğalgaz = 7.5 kg/saat
    = 52,500 kg/yıl × 0.35 €/kg = 18,375 €/yıl
  Yatırım: ~6,000 € (plakalı eşanjör)
  Geri ödeme: <0.4 yıl

Fırsat 2: Chiller Kondenser Isısı → Düşük Sıcaklık Uygulaması
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Kaynak: Chiller kondenser (35°C, ~445 kW termal)
  Hedef: Bina ısıtma veya tesis ön ısıtma (kış aylarında)
  Exergy: Düşük sıcaklık → düşük exergy, sınırlı fayda
  Maliyet kazanımı: ~5,000-8,000 €/yıl (mevsimsel)
  Yatırım: ~10,000 €
  Geri ödeme: 1.3-2.0 yıl

Fırsat 3: Genişletilmiş Baca Gazı Geri Kazanımı
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Mevcut: Baca gazı 220°C → 130°C (HX ile)
  Potansiyel: 130°C → 80°C daha soğutma
  Ek ısı geri kazanımı: ~200 kW termal
  Exergy kazanımı: ~15 kW
  Maliyet kazanımı: ~12,000 €/yıl
  Yatırım: ~18,000 € (ek ekonomizer)
  Geri ödeme: 1.5 yıl

Entegrasyon Öncelik Matrisi:
  Sıra | Fırsat              | Tasarruf [€/yıl] | Yatırım [€] | Geri Ödeme |
  1    | Komp. atık ısı → BW | 18,375           | 6,000       | 0.3 yıl    |
  2    | Ek ekonomizer        | 12,000           | 18,000      | 1.5 yıl    |
  3    | Chiller ısı geri kaz.| 6,500            | 10,000      | 1.5 yıl    |
```

## 7. Geleneksel vs Exergoekonomik Karşılaştırma

```
══════════════════════════════════════════════════════
GELENEKSEL ENERJİ ANALİZİ vs EXERGOEKONOMİK ANALİZ
══════════════════════════════════════════════════════

                  | Geleneksel (1. Yasa)    | Exergoekonomik           |
──────────────────|─────────────────────────|──────────────────────────|
Kazan             | η=88%, "iyi"            | ε=19%, f_k=0.02, "kötü" |
                  | Aksiyon: yok            | Aksiyon: ekonomizer, CHP  |
                  |                         |                          |
Eşanjör           | Etkililik=85%, "iyi"    | ε=59%, f_k=0.35, "orta" |
                  | Aksiyon: yok            | Aksiyon: alan artır       |
                  |                         |                          |
Kompresör         | η_s=72%, "kabul"        | ε=61%, f_k=0.19, "orta" |
                  | Aksiyon: bakım          | Aksiyon: ısı geri kaz.   |
                  |                         |                          |
Chiller           | COP=3.68, "iyi"         | ε=24%, f_k=0.25, "düşük"|
                  | Aksiyon: yok            | Aksiyon: set point, VSD  |
                  |                         |                          |
Pompa             | η_P=75%, "kabul"        | ε=32%, f_k=0.18, "düşük"|
                  | Aksiyon: yok            | Aksiyon: boyut kontrol   |

Geleneksel Sonuç:
→ "Tesis genel olarak iyi çalışıyor, büyük sorun yok"
→ Toplam enerji verimi: ~%85 (enerji bazlı)
→ Önerilen aksiyon: Düzenli bakım devam

Exergoekonomik Sonuç:
→ "Tesis exergy bazında %19-60 verimliliklerle çalışıyor"
→ Toplam exergy maliyeti: 468 €/saat = 3,276,000 €/yıl
→ Kazan tek başına 450 €/saat maliyet yaratıyor
→ 5 somut aksiyon + 3 çapraz entegrasyon fırsatı
→ Toplam tasarruf potansiyeli: ~665,000 €/yıl
→ Toplam yatırım: ~173,000 € → Ortalama geri ödeme: <0.4 yıl

Katma Değer:
→ Exergoekonomik analiz, geleneksel analizin "iyi" dediği
  yerlerde bile tasarruf fırsatı buluyor
→ f_k ve r_k, her bileşen için doğru aksiyon tipini belirliyor
→ Ċ_D sıralaması, kısıtlı bütçeyi doğru yere yönlendiriyor
```

## 8. Öncelikli Aksiyon Planı

```
ExergyLab Platformu Formatında Önceliklendirilmiş Aksiyonlar:

═══════════════════════════════════════════════
ACIL (0-3 ay) — Düşük yatırım, yüksek getiri
═══════════════════════════════════════════════

1. Kompresör atık ısı geri kazanımı
   Yatırım: 6,000 € | Tasarruf: 18,375 €/yıl | GÖ: 0.3 yıl
   f_k etkisi: Kompresör ε: 61%→73%

2. Pompa boyut kontrolü ve VSD
   Yatırım: 4,000 € | Tasarruf: 5,600 €/yıl | GÖ: 0.7 yıl
   f_k etkisi: Pompa ε: 32%→55%

3. Chiller set point optimizasyonu (7→10°C)
   Yatırım: 0 € | Tasarruf: ~8,400 €/yıl | GÖ: 0
   f_k etkisi: Chiller ε: 24%→30%

═══════════════════════════════════════════════
KISA VADE (3-6 ay) — Orta yatırım
═══════════════════════════════════════════════

4. Chiller VSD retrofit
   Yatırım: 15,000 € | Tasarruf: 16,800 €/yıl | GÖ: 0.9 yıl

5. Ek baca gazı ekonomizeri
   Yatırım: 18,000 € | Tasarruf: 12,000 €/yıl | GÖ: 1.5 yıl

6. Eşanjör alan genişletme
   Yatırım: 12,000 € | Tasarruf: 7,000 €/yıl | GÖ: 1.7 yıl

═══════════════════════════════════════════════
ORTA VADE (6-18 ay) — Stratejik yatırım
═══════════════════════════════════════════════

7. Kazan modernizasyonu (ekonomizer + hava ön ısıtıcı)
   Yatırım: 120,000 € | Tasarruf: 582,400 €/yıl | GÖ: 0.2 yıl
   Not: En yüksek mutlak tasarruf ama daha büyük proje

8. CHP fizibilite çalışması
   Yatırım: 15,000 € (fizibilite) | Potansiyel: Yüksek
   → Kazan yanma irreversibilitesinin bir kısmını elektriğe dönüştürme

═══════════════════════════════════════════════
TOPLAM
═══════════════════════════════════════════════
  Toplam yatırım: ~190,000 €
  Toplam yıllık tasarruf: ~650,575 €/yıl
  Ortalama geri ödeme: <0.4 yıl
  Exergy verimi artışı: Tesis geneli ε ≈ +8-12 puan
```

## 9. ExergyLab Platform Entegrasyonu Notu

```
Bu analiz ExergyLab platformu aracılığıyla yapılabilir:

1. Her ekipman ayrı ayrı analiz edilir (mevcut özellik)
2. Fabrika analizi ile toplu değerlendirme yapılır (mevcut özellik)
3. AI yorumlama f_k/r_k değerlerini hesaplar ve raporlar (gelecek özellik)
4. Çapraz ekipman entegrasyon fırsatları otomatik tespit edilir (mevcut özellik)

Exergoekonomik modül eklendiğinde:
→ PEC girişi → CRF hesabı → Ż otomatik
→ Matris formülasyonu → c_P otomatik
→ f_k, r_k hesabı ve yorumlama → AI destekli aksiyon planı
→ Duyarlılık analizi → Karar güvenilirliği
```

## İlgili Dosyalar

- [SPECO Metodolojisi](../speco_method.md) — Tam SPECO yöntemi
- [Matris Formülasyonu](../matrix_formulation.md) — Python matris çözümü
- [Değerlendirme Kriterleri](../evaluation_criteria.md) — f_k, r_k, Ċ_D yorumlama
- [Optimizasyon](../optimization.md) — f_k/r_k tabanlı iyileştirme
- [Duyarlılık Analizi](../sensitivity_analysis.md) — Parametre belirsizliği
- [Çapraz Ekipman](../../cross_equipment.md) — Entegrasyon fırsatları
- [Önceliklendirme](../../prioritization.md) — Yatırım sıralaması
- [Basit Rankine Örneği](simple_cycle.md) — Temel SPECO uygulaması
- [CHP Örneği](cogeneration.md) — İleri exergoekonomik analiz

## Referanslar

1. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
2. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
3. Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
4. Turton, R., et al. (2012). *Analysis, Synthesis, and Design of Chemical Processes*. 4th ed., Prentice Hall.
5. ExergyLab Knowledge Base — `knowledge/factory/cross_equipment.md`, `knowledge/factory/prioritization.md`
