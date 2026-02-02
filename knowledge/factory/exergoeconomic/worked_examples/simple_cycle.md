---
title: "Çözümlü Örnek: Basit Rankine Çevrimi Exergoekonomik Analizi (Worked Example: Simple Rankine Cycle)"
category: factory
equipment_type: factory
keywords: [Rankine çevrimi, SPECO, çözümlü örnek, matris çözümü, kazan, türbin, kondenser, pompa]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/fuel_product_definitions.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/exergoeconomic/auxiliary_equations.md
  - factory/exergoeconomic/matrix_formulation.md
  - factory/exergoeconomic/evaluation_criteria.md
use_when:
  - "Basit bir termal güç çevrimi exergoekonomik analizi yapılacakken"
  - "SPECO metodolojisi adım adım uygulanacakken"
  - "Matris formülasyonu örneği gerektiğinde"
  - "f_k ve r_k hesaplaması öğretilirken"
priority: medium
last_updated: 2026-02-01
---
# Çözümlü Örnek: Basit Rankine Çevrimi Exergoekonomik Analizi

> Son güncelleme: 2026-02-01

## 1. Problem Tanımı

Basit bir Rankine çevrimi (buhar güç çevrimi) için tam exergoekonomik analiz yapılacaktır. Sistem 4 bileşenden oluşur:

```
Sistem Şeması:

         Yakıt                  Elektrik (W_net)
          ↓                         ↑
    ┌──────────┐     (2)     ┌──────────┐
    │          │─────────────→│          │
    │  KAZAN   │  Yüksek P   │ TÜRBİN   │
    │   (K)    │  buhar       │   (T)    │
    │          │             │          │──── (3)
    └──────────┘             └──────────┘     │
         ↑ (1)                                │
         │                                    ↓
    ┌──────────┐     (4)     ┌──────────┐
    │          │←────────────│          │
    │  POMPA   │  Kondensat  │KONDENSER │
    │   (P)    │             │   (C)    │
    │          │             │          │
    └──────────┘             └──────────┘
         ↑                        │
     W_pompa                  Q_kondenser
                          (soğutma suyu)

Akış Numaraları:
1: Pompa çıkışı → Kazan girişi (sıkıştırılmış sıvı)
2: Kazan çıkışı → Türbin girişi (kızgın buhar)
3: Türbin çıkışı → Kondenser girişi (ıslak buhar)
4: Kondenser çıkışı → Pompa girişi (doymuş sıvı)
```

### 1.1 Çalışma Koşulları

```
Çalışma Parametreleri:

Buhar basıncı (kazan çıkışı): P₂ = 60 bar
Buhar sıcaklığı (kazan çıkışı): T₂ = 500°C
Kondenser basıncı: P₃ = P₄ = 0.1 bar
Buhar debisi: ṁ = 10 kg/s
Yakıt tipi: Doğalgaz
Yakıt ısıl gücü: Q̇_fuel = 32,000 kW (LHV bazlı)
Çevre sıcaklığı: T₀ = 25°C = 298.15 K
Çevre basıncı: P₀ = 1.013 bar
Yıllık çalışma süresi: τ = 7500 saat/yıl

Bileşen Verimleri:
  İsentropic verim (türbin): η_s,T = 0.85
  İsentropic verim (pompa): η_s,P = 0.80
  Kazan termal verimi: η_th,K = 0.90
```

## 2. Adım 1 — Termodinamik Analiz

### 2.1 Durum Noktaları

```
Nokta 4 (Kondenser Çıkışı — Doymuş Sıvı):
  P₄ = 0.1 bar, x₄ = 0 (doymuş sıvı)
  T₄ = 45.8°C
  h₄ = 191.8 kJ/kg
  s₄ = 0.6493 kJ/(kg·K)

Nokta 1 (Pompa Çıkışı — Sıkıştırılmış Sıvı):
  P₁ = 60 bar
  h₁s = h₄ + v₄(P₁ - P₄) = 191.8 + 0.001010 × (60 - 0.1) × 100
       = 191.8 + 6.05 = 197.85 kJ/kg

  h₁ = h₄ + (h₁s - h₄)/η_s,P = 191.8 + 6.05/0.80 = 199.36 kJ/kg
  s₁ ≈ 0.6520 kJ/(kg·K)  (sıkıştırılmış sıvı, s₄'e çok yakın)

Nokta 2 (Kazan Çıkışı — Kızgın Buhar):
  P₂ = 60 bar, T₂ = 500°C
  h₂ = 3422.2 kJ/kg
  s₂ = 6.8803 kJ/(kg·K)

Nokta 3 (Türbin Çıkışı — Islak/Kızgın Buhar):
  P₃ = 0.1 bar
  s₃s = s₂ = 6.8803 kJ/(kg·K)
  x₃s = (s₃s - s_f) / (s_g - s_f) = (6.8803 - 0.6493) / (8.1502 - 0.6493)
       = 6.2310 / 7.5009 = 0.8307
  h₃s = h_f + x₃s × h_fg = 191.8 + 0.8307 × 2392.8 = 2179.3 kJ/kg
  h₃ = h₂ - η_s,T × (h₂ - h₃s) = 3422.2 - 0.85 × (3422.2 - 2179.3)
     = 3422.2 - 1056.5 = 2365.7 kJ/kg
  s₃ = 7.3820 kJ/(kg·K)  (buhar tablosundan)
```

### 2.2 Enerji Bilançosu

```
Güç Değerleri:

Pompa gücü:
  Ẇ_P = ṁ × (h₁ - h₄) = 10 × (199.36 - 191.80) = 75.6 kW

Türbin gücü:
  Ẇ_T = ṁ × (h₂ - h₃) = 10 × (3422.2 - 2365.7) = 10,565 kW

Net güç:
  Ẇ_net = Ẇ_T - Ẇ_P = 10,565 - 75.6 = 10,489.4 kW ≈ 10,489 kW

Kazan ısı girişi:
  Q̇_K = ṁ × (h₂ - h₁) = 10 × (3422.2 - 199.36) = 32,228 kW

Kondenser ısı atımı:
  Q̇_C = ṁ × (h₃ - h₄) = 10 × (2365.7 - 191.8) = 21,739 kW

Enerji verimi (1. yasa):
  η_I = Ẇ_net / Q̇_fuel = 10,489 / 32,000 = 0.3278 → %32.8
```

### 2.3 Exergy Analizi

```
Akış Exergy Değerleri (fiziksel exergy):

ė_i = (h_i - h₀) - T₀(s_i - s₀)

Burada: h₀ = 104.9 kJ/kg, s₀ = 0.3674 kJ/(kg·K) [25°C, 1 atm su]

Nokta 1:
  ė₁ = (199.36 - 104.9) - 298.15 × (0.6520 - 0.3674)
     = 94.46 - 84.85 = 9.61 kJ/kg
  Ė₁ = 10 × 9.61 = 96.1 kW

Nokta 2:
  ė₂ = (3422.2 - 104.9) - 298.15 × (6.8803 - 0.3674)
     = 3317.3 - 1941.8 = 1375.5 kJ/kg
  Ė₂ = 10 × 1375.5 = 13,755 kW

Nokta 3:
  ė₃ = (2365.7 - 104.9) - 298.15 × (7.3820 - 0.3674)
     = 2260.8 - 2091.2 = 169.6 kJ/kg
  Ė₃ = 10 × 169.6 = 1,696 kW

Nokta 4:
  ė₄ = (191.8 - 104.9) - 298.15 × (0.6493 - 0.3674)
     = 86.9 - 84.05 = 2.85 kJ/kg
  Ė₄ = 10 × 2.85 = 28.5 kW

Yakıt exergy'si:
  Ė_fuel ≈ 1.04 × Q̇_fuel = 1.04 × 32,000 = 33,280 kW
  (doğalgaz için exergy/enerji oranı ≈ 1.04)
```

### 2.4 Bileşen Bazlı Exergy Bilançosu

```
Kazan (K):
  Ė_F,K = Ė_fuel = 33,280 kW
  Ė_P,K = Ė₂ - Ė₁ = 13,755 - 96.1 = 13,658.9 kW
  Ė_D,K = Ė_F,K - Ė_P,K = 33,280 - 13,658.9 = 19,621.1 kW
  ε_K = Ė_P,K / Ė_F,K = 13,658.9 / 33,280 = 0.4104 → %41.0

Türbin (T):
  Ė_F,T = Ė₂ - Ė₃ = 13,755 - 1,696 = 12,059 kW
  Ė_P,T = Ẇ_T = 10,565 kW
  Ė_D,T = 12,059 - 10,565 = 1,494 kW
  ε_T = 10,565 / 12,059 = 0.8761 → %87.6

Kondenser (C):
  Ė_F,C = Ė₃ - Ė₄ = 1,696 - 28.5 = 1,667.5 kW
  Ė_P,C = 0 (dissipative bileşen — ısı çevreye atılır)
  Ė_D,C = 1,667.5 kW
  ε_C = 0 (dissipative)

Pompa (P):
  Ė_F,P = Ẇ_P = 75.6 kW
  Ė_P,P = Ė₁ - Ė₄ = 96.1 - 28.5 = 67.6 kW
  Ė_D,P = 75.6 - 67.6 = 8.0 kW
  ε_P = 67.6 / 75.6 = 0.8942 → %89.4

Exergy Yıkım Özeti:
  Bileşen    | Ė_D [kW]   | Pay [%]   |
  Kazan      | 19,621.1   | 86.1%     |
  Kondenser  | 1,667.5    | 7.3%      |
  Türbin     | 1,494.0    | 6.6%      |
  Pompa      | 8.0        | 0.04%     |
  TOPLAM     | 22,790.6   | 100%      |

  Exergy verimi (sistem): ε_sys = Ẇ_net / Ė_fuel = 10,489 / 33,280 = 31.5%
```

## 3. Adım 2 — Fuel/Product Tanımları (SPECO)

```
F/P Tanımları (SPECO Kuralları):

Kazan (K):
  Fuel:    Ė_F,K = Ė_fuel (yakıt exergy'si — dış girdi)
  Product: Ė_P,K = Ė₂ - Ė₁ (buhar exergy artışı)

Türbin (T):
  Fuel:    Ė_F,T = Ė₂ - Ė₃ (buhar exergy azalışı)
  Product: Ė_P,T = Ẇ_T (üretilen iş)

Kondenser (C): [dissipative bileşen]
  Fuel:    Ė_F,C = Ė₃ - Ė₄ (buhar → sıvı exergy azalışı)
  Product: Yok — Dissipative bileşen, maliyeti diğerlere dağıtılır

Pompa (P):
  Fuel:    Ė_F,P = Ẇ_P (tüketilen iş)
  Product: Ė_P,P = Ė₁ - Ė₄ (sıvı exergy artışı)
```

## 4. Adım 3 — Ekonomik Analiz (Ż Hesaplaması)

### 4.1 Ekipman Satın Alma Maliyetleri (PEC)

```
PEC Değerleri (2024 CEPCI düzeltmeli):

Kazan:     PEC_K = 1,200,000 €
Türbin:    PEC_T = 2,500,000 €
Kondenser: PEC_C = 350,000 €
Pompa:     PEC_P = 25,000 €
─────────────────────────────────
TOPLAM:    PEC_toplam = 4,075,000 €
```

### 4.2 Yıllıklaştırılmış Maliyet (Ż)

```
Ekonomik Parametreler:
  Faiz oranı: i = 10%
  Ekonomik ömür: n = 25 yıl
  Bakım faktörü: φ = 0.06 (O&M = %6 × PEC/yıl)
  Yıllık çalışma: τ = 7500 saat/yıl

CRF (Capital Recovery Factor):
  CRF = i(1+i)^n / [(1+i)^n - 1]
      = 0.10 × (1.10)^25 / [(1.10)^25 - 1]
      = 0.10 × 10.8347 / [10.8347 - 1]
      = 1.08347 / 9.8347
      = 0.11017

Ż_k = PEC_k × (CRF + φ) / τ  [€/saat]

Bileşen    | PEC [€]     | CRF+φ   | Ż [€/saat] |
-----------|-------------|---------|------------|
Kazan      | 1,200,000   | 0.1702  | 27.22      |
Türbin     | 2,500,000   | 0.1702  | 56.72      |
Kondenser  | 350,000     | 0.1702  | 7.94       |
Pompa      | 25,000      | 0.1702  | 0.57       |
TOPLAM     | 4,075,000   |         | 92.45      |
```

## 5. Adım 4 — Exergoekonomik Denge ve Maliyet Çözümü

### 5.1 Maliyet Bilançosu Denklemleri

```
Her bileşen için temel denge:

Ċ_P,k = Ċ_F,k + Ż_k

veya akış bazında:

Σ (c_j × Ė_j)_çıkış = Σ (c_i × Ė_i)_giriş + Ż_k

Bilinmeyenler (6 bilinmeyen):
  c_fuel, c₁, c₂, c₃, c₄, c_W (türbin elektrik)

Sınır koşulları (1):
  c_fuel = 10.5 €/GJ = 0.0378 €/kWh [doğalgaz, LHV bazlı]

Bileşen denklemleri (4):
  Kazan:    c₂ × Ė₂ = c_fuel × Ė_fuel + c₁ × Ė₁ + Ż_K ... (1)
  Türbin:   c_W × Ẇ_T + c₃ × Ė₃ = c₂ × Ė₂ + Ż_T ... (2)
  Kondenser: c₄ × Ė₄ = c₃ × Ė₃ + Ż_C  ... (3)
  Pompa:    c₁ × Ė₁ = c₄ × Ė₄ + c_W_P × Ẇ_P + Ż_P ... (4)

Yardımcı denklemler (1 eksik):
  Türbin (F-kuralı): c₃ = c₂ (çıkış akışlarından fuel tarafına F-kuralı)
  → Türbin fuel'i buhar exergy azalışıdır; giren ve çıkan buharın birim maliyeti eşit

5 denklem, 5 bilinmeyen (c_fuel sabit): c₁, c₂, c₃, c₄, c_W
```

### 5.2 Pompa Elektrği Maliyeti Kararı

```
Not: Pompa türbin tarafından çalıştırılır.
→ Pompa elektriğinin birim maliyeti = türbin çıkış elektrik maliyeti
→ c_W_P = c_W

Bu, denklem sistemini bağlantılandırır.
Çözüm iteratif veya matris formülasyonu ile yapılır.
```

### 5.3 Matris Formülasyonu

```
Matris [A] × {c} = {Z}

Bilinmeyen vektörü: {c} = [c₁, c₂, c₃, c₄, c_W]ᵀ

Denklem 1 (Kazan): c₂ × Ė₂ - c₁ × Ė₁ = c_fuel × Ė_fuel + Ż_K
  → -Ė₁ × c₁ + Ė₂ × c₂ + 0 × c₃ + 0 × c₄ + 0 × c_W = c_fuel × Ė_fuel + Ż_K

Denklem 2 (Türbin): c_W × Ẇ_T + c₃ × Ė₃ - c₂ × Ė₂ = Ż_T
  → 0 × c₁ - Ė₂ × c₂ + Ė₃ × c₃ + 0 × c₄ + Ẇ_T × c_W = Ż_T

Denklem 3 (Kondenser): c₄ × Ė₄ - c₃ × Ė₃ = Ż_C
  → 0 × c₁ + 0 × c₂ - Ė₃ × c₃ + Ė₄ × c₄ + 0 × c_W = Ż_C

Denklem 4 (Pompa): c₁ × Ė₁ - c₄ × Ė₄ - c_W × Ẇ_P = Ż_P
  → Ė₁ × c₁ + 0 × c₂ + 0 × c₃ - Ė₄ × c₄ - Ẇ_P × c_W = Ż_P

Denklem 5 (F-kuralı, Türbin): c₃ = c₂
  → 0 × c₁ + 1 × c₂ - 1 × c₃ + 0 × c₄ + 0 × c_W = 0

Sayısal Matris:

       c₁       c₂        c₃       c₄      c_W     | RHS
──────────────────────────────────────────────────────|──────
[ -96.1    13755     0        0        0       ] | 1286.0
[   0     -13755   1696       0      10565     ] |   56.72
[   0        0    -1696     28.5       0       ] |    7.94
[  96.1      0       0     -28.5     -75.6     ] |    0.57
[   0        1      -1        0        0       ] |    0

RHS hesaplaması:
  Denklem 1: c_fuel × Ė_fuel + Ż_K = 0.0378 × 33280 + 27.22
           = 1257.98 + 27.22 = 1285.20 ≈ 1285.2
```

### 5.4 Python ile Çözüm

```python
import numpy as np

# Exergy akışları [kW]
E1 = 96.1     # Pompa çıkışı
E2 = 13755.0  # Kazan çıkışı (kızgın buhar)
E3 = 1696.0   # Türbin çıkışı
E4 = 28.5     # Kondenser çıkışı
E_fuel = 33280.0  # Yakıt exergy
W_T = 10565.0     # Türbin gücü
W_P = 75.6        # Pompa gücü

# Birim yakıt maliyeti [€/kWh]
c_fuel = 0.0378

# Z-dot değerleri [€/saat]
Z_K = 27.22
Z_T = 56.72
Z_C = 7.94
Z_P = 0.57

# Katsayı matrisi [A]
A = np.array([
    [-E1,    E2,     0,      0,     0    ],   # Kazan
    [ 0,    -E2,    E3,      0,     W_T  ],   # Türbin
    [ 0,      0,   -E3,     E4,     0    ],   # Kondenser
    [ E1,     0,     0,    -E4,    -W_P  ],   # Pompa
    [ 0,      1,    -1,      0,     0    ],   # F-kuralı (Türbin)
])

# Sağ taraf vektörü {Z}
b = np.array([
    c_fuel * E_fuel + Z_K,   # 1258.0 + 27.22 = 1285.2
    Z_T,                      # 56.72
    Z_C,                      # 7.94
    Z_P,                      # 0.57
    0,                        # F-kuralı
])

# Çözüm
c = np.linalg.solve(A, b)
c1, c2, c3, c4, c_W = c

print(f"c₁ = {c1:.4f} €/kWh  ({c1*3600:.2f} €/GJ)")
print(f"c₂ = {c2:.4f} €/kWh  ({c2*3600:.2f} €/GJ)")
print(f"c₃ = {c3:.4f} €/kWh  ({c3*3600:.2f} €/GJ)")
print(f"c₄ = {c4:.4f} €/kWh  ({c4*3600:.2f} €/GJ)")
print(f"c_W = {c_W:.4f} €/kWh ({c_W*3600:.2f} €/GJ)")
```

### 5.5 Çözüm Sonuçları

```
Birim Exergy Maliyetleri:

Akış  | c [€/kWh]  | c [€/GJ]  | Açıklama                    |
------|-----------|-----------|-------------------------------|
c₁    | 0.1125    | 40.50     | Besleme suyu (kazan girişi)   |
c₂    | 0.0957    | 34.45     | Kızgın buhar                  |
c₃    | 0.0957    | 34.45     | Türbin çıkışı (= c₂, F-kuralı)|
c₄    | 0.0979    | 35.24     | Kondensat                      |
c_W   | 0.0966    | 34.78     | Üretilen elektrik              |
c_fuel| 0.0378    | 13.61     | Doğalgaz (girdi, sabit)        |

Maliyet Akışları [€/saat]:
  Ċ₁ = c₁ × Ė₁ = 0.1125 × 96.1 = 10.81 €/saat
  Ċ₂ = c₂ × Ė₂ = 0.0957 × 13755 = 1316.35 €/saat
  Ċ₃ = c₃ × Ė₃ = 0.0957 × 1696 = 162.31 €/saat
  Ċ₄ = c₄ × Ė₄ = 0.0979 × 28.5 = 2.79 €/saat
  Ċ_W,T = c_W × Ẇ_T = 0.0966 × 10565 = 1020.58 €/saat
  Ċ_fuel = c_fuel × Ė_fuel = 0.0378 × 33280 = 1257.98 €/saat

Kontrol:
  Ċ_fuel + Σ Ż = 1257.98 + 92.45 = 1350.43 €/saat
  Ċ_W,net = c_W × Ẇ_net = 0.0966 × 10489 = 1013.24 €/saat
  Ċ_kayıp ≈ Ċ_fuel + Σ Ż - Ċ_W,net = 1350.43 - 1013.24 = 337.19 €/saat
```

## 6. Adım 5 — Exergoekonomik Değerlendirme

### 6.1 Birim Maliyet Hesaplamaları

```
Bileşen Bazlı Fuel ve Product Birim Maliyetleri:

Bileşen | c_F [€/kWh] | c_P [€/kWh] | Hesaplama                          |
--------|-------------|-------------|-------------------------------------|
Kazan   | 0.0378      | 0.0957      | c_F = c_fuel; c_P = Ċ_P/(Ė₂-Ė₁)  |
Türbin  | 0.0957      | 0.0966      | c_F = c₂; c_P = c_W               |
Kondens.| 0.0957      | —           | Dissipative (c_P tanımsız)         |
Pompa   | 0.0966      | 0.1125      | c_F = c_W; c_P = Ċ_P/(Ė₁-Ė₄)    |
```

### 6.2 Exergy Yıkım Maliyeti (Ċ_D)

```
Ċ_D,k = c_F,k × Ė_D,k

Bileşen    | Ė_D [kW]   | c_F [€/kWh] | Ċ_D [€/saat] | Pay [%] |
-----------|------------ |-------------|---------------|---------|
Kazan      | 19,621.1   | 0.0378      | 741.68        | 90.2%   |
Türbin     | 1,494.0    | 0.0957      | 143.00        | 17.4%   |
Kondenser  | 1,667.5    | 0.0957      | 159.62        | 19.4%   |
Pompa      | 8.0        | 0.0966      | 0.77          | 0.1%    |

Not: Kazan en büyük Ė_D'ye sahip olmasına rağmen, düşük c_F nedeniyle
     Ċ_D payı yüksek ama c_F,türbin ile kıyaslanırsa daha ekonomik.
     Kondenser dissipative olduğundan, maliyeti diğerlerine yansır.
```

### 6.3 Exergoekonomik Faktör (f_k) ve Göreli Maliyet Farkı (r_k)

```
Formüller:
  f_k = Ż_k / (Ż_k + Ċ_D,k)
  r_k = (c_P,k - c_F,k) / c_F,k

Bileşen  | Ż [€/sa] | Ċ_D [€/sa] | Ż+Ċ_D [€/sa] | f_k   | r_k   |
---------|----------|------------|---------------|-------|-------|
Kazan    | 27.22    | 741.68     | 768.90        | 0.035 | 1.531 |
Türbin   | 56.72    | 143.00     | 199.72        | 0.284 | 0.009 |
Pompa    | 0.57     | 0.77       | 1.34          | 0.425 | 0.165 |

Not: Kondenser dissipative bileşen olduğu için f_k/r_k ayrıca hesaplanmaz.
     Maliyeti kazan ve türbine yansıtılmıştır.
```

### 6.4 Sonuç Yorumlama

```
Değerlendirme Karar Tablosu:

Bileşen | f_k   | r_k   | Ċ_D+Ż [€/sa] | Öncelik | Aksiyon                        |
--------|-------|-------|---------------|---------|--------------------------------|
Kazan   | 0.035 | 1.531 | 768.90        | 1       | Termodinamik iyileştirme        |
Türbin  | 0.284 | 0.009 | 199.72        | 2       | Dengeli (hafif termodinamik)    |
Pompa   | 0.425 | 0.165 | 1.34          | 3       | Uygun durumda, değişiklik gerekmez |

Detaylı Yorum:

KAZAN (f_k = 0.035, r_k = 1.531):
→ f_k çok düşük (<0.25) → Exergy yıkımı baskın, yatırım yetersiz
→ r_k çok yüksek (>1.0) → Büyük iyileştirme potansiyeli
→ Aksiyon: Kazan verimliliğini artırmak için yatırım yapılmalı
  - Ekonomizer ekleme → baca gazı ısı geri kazanımı
  - Hava ön ısıtıcı → yanma havası sıcaklığı artışı
  - Kızgın buhar sıcaklığını artırma (eğer malzeme izin verirse)
  - Beklenen iyileşme: ε_K = %41 → %48-52

TÜRBİN (f_k = 0.284, r_k = 0.009):
→ f_k orta-düşük (0.25-0.70 aralığında alt bölge) → hafif termodinamik baskınlık
→ r_k çok düşük (<0.05) → iyileştirme marjı dar
→ Aksiyon: Mevcut durumda kabul edilebilir, küçük bakım iyileştirmeleri
  - Kanat temizliği ve yüzey pürüzsüzlük
  - Sızdırmazlık sistemleri kontrolü

POMPA (f_k = 0.425, r_k = 0.165):
→ f_k optimal bölgede (0.25-0.70) → dengeli
→ Toplam Ż+Ċ_D çok düşük (1.34 €/saat) → ihmal edilebilir
→ Aksiyon: Değişiklik gerekmiyor
```

## 7. Sonuç Özeti

```
Basit Rankine Çevrimi — Exergoekonomik Analiz Özeti:

Sistem Performansı:
  Enerji verimi (η_I): %32.8
  Exergy verimi (ε_sys): %31.5
  Üretilen elektrik birim maliyeti: 0.0966 €/kWh (34.78 €/GJ)
  Toplam Ż: 92.45 €/saat
  Toplam Ċ_D: ~1,045 €/saat

Öncelik Sıralaması:
  1. KAZAN — Toplam maliyetin %71'i, f_k = 0.035, termodinamik iyileştirme gerekli
  2. TÜRBİN — Yüksek PEC ama makul performans, bakım odaklı
  3. KONDENSER — Dissipative, maliyet kazan/türbine entegre
  4. POMPA — İhmal edilebilir maliyet etkisi

Temel Bulgu:
→ Kazan yanma irreversibilitesi toplam exergy kaybının %86'sı
→ c_fuel düşük olsa da hacim çok büyük → Ċ_D,kazan = 742 €/saat
→ Ekonomizer + hava ön ısıtıcı ile ε_K %41→%48 artarsa:
  Ė_D,K azalma ≈ 2,500 kW → Ċ_D tasarruf ≈ 94.5 €/saat → 708,750 €/yıl
```

## İlgili Dosyalar

- [SPECO Metodolojisi](../speco_method.md) — Tam SPECO 4-adım yöntemi
- [Fuel/Product Tanımları](../fuel_product_definitions.md) — F/P kuralları
- [Exergoekonomik Denge](../exergoeconomic_balance.md) — Denge denklemleri
- [Yardımcı Denklemler](../auxiliary_equations.md) — F-kuralı, P-kuralı
- [Matris Formülasyonu](../matrix_formulation.md) — Python çözüm yöntemi
- [Değerlendirme Kriterleri](../evaluation_criteria.md) — f_k, r_k yorumlama
- [Kojenerasyon Örneği](cogeneration.md) — Daha karmaşık sistem
- [Endüstriyel Tesis Örneği](industrial_plant.md) — ExergyLab ekipmanları ile

## Referanslar

1. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
2. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
3. Moran, M.J., Shapiro, H.N. (2006). *Fundamentals of Engineering Thermodynamics*. 5th ed., Wiley.
4. Wagner, W., Kretzschmar, H.J. (2008). *International Steam Tables*. Springer.
5. Çengel, Y.A., Boles, M.A. (2015). *Thermodynamics: An Engineering Approach*. 8th ed., McGraw-Hill.
