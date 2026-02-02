---
title: "Ekipman Maliyet Korelasyonları (Equipment Cost Equations — PEC)"
category: factory
equipment_type: factory
keywords: [PEC, ekipman maliyeti, maliyet korelasyonu, Bejan, Turton, CEPCI]
related_files:
  - factory/exergoeconomic/levelized_cost.md
  - factory/exergoeconomic/cost_databases.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/economic_analysis.md
use_when:
  - "Ekipman satın alma maliyeti hesaplanırken"
  - "PEC korelasyonları uygulanırken"
  - "Maliyet düzeltme faktörleri belirlenirken"
priority: high
last_updated: 2026-02-01
---

> **Not:** Bu dosyadaki maliyet formülleri orijinal akademik kaynaklarda USD bazlıdır. Türkiye endüstriyel uygulamaları için güncel EUR/USD döviz kuru ile çevirin (2024 referans: 1 USD ≈ 0,92 EUR).

# Ekipman Maliyet Korelasyonları (Equipment Cost Equations — PEC)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Ekipman satın alma maliyeti (Purchased Equipment Cost — PEC), exergoekonomik analizin ekonomik girdisidir. PEC korelasyonları, ekipman kapasitesi ve tasarım parametrelerinden maliyet tahmini üretir.

```
Genel PEC Formülü:

PEC = PEC_baz · f_M · f_P · f_T · (CEPCI_güncel / CEPCI_referans)

Burada:
- PEC_baz = Baz maliyet (karbon çelik, düşük basınç) [USD veya EUR]
- f_M = Malzeme düzeltme faktörü [-]
- f_P = Basınç düzeltme faktörü [-]
- f_T = Sıcaklık düzeltme faktörü [-]
- CEPCI = Chemical Engineering Plant Cost Index (zaman düzeltmesi)
```

## 2. Ekipman Bazlı PEC Korelasyonları

### 2.1 Kompresör (Compressor)

```
Kaynak: Bejan et al. (1996), Turton et al. (2012)

PEC_kompresör = C₁ · (Ẇ_C)^α

Santrifüj kompresör:
  PEC = 39.5 · ṁ_hava · (P_çıkış/P_giriş) · ln(P_çıkış/P_giriş)
        × 1 / (0.9 - η_is)
  [USD, 1994 bazlı]

Alternatif (Turton 2012):
  log₁₀(PEC_baz) = K₁ + K₂·log₁₀(Ẇ) + K₃·(log₁₀(Ẇ))²

  Santrifüj:  K₁ = 2.2897, K₂ = 1.3604, K₃ = -0.1027  (Ẇ: kW, 75-30000 kW)
  Pistonlu:   K₁ = 2.2897, K₂ = 1.3604, K₃ = -0.1027  (Ẇ: kW, 18-950 kW)

Basınç düzeltme (P > 10 bar):
  log₁₀(f_P) = C₁ + C₂·log₁₀(P) + C₃·(log₁₀(P))²
  C₁ = 0, C₂ = 0, C₃ = 0 (kompresörler için basınç dahil)

Tipik PEC aralığı:
  Küçük (10-50 kW):      15,000 - 60,000 €
  Orta (50-200 kW):      50,000 - 200,000 €
  Büyük (200-1000 kW):   150,000 - 800,000 €

Belirsizlik: ±25-35%
```

### 2.2 Türbin (Turbine)

```
Buhar türbini (Bejan et al. 1996):
  PEC = 6000 · (Ẇ_T)^0.7  [USD, 1994]
  (Ẇ_T: kW, 500-20000 kW)

Gaz türbini (Bejan et al. 1996):
  PEC = 479.34 · ṁ_gaz · (P_çıkış/P_giriş) · ln(P_çıkış/P_giriş)
        × 1 / (0.92 - η_is)
  [USD, 1994]

Turton (2012) — Buhar türbini:
  log₁₀(PEC_baz) = 2.7051 + 1.4398·log₁₀(Ẇ) - 0.1776·(log₁₀(Ẇ))²
  (Ẇ: kW, 100-20000 kW)

Tipik PEC aralığı:
  Küçük buhar türbin (100-500 kW):    80,000 - 350,000 €
  Orta buhar türbin (500-5000 kW):    200,000 - 2,500,000 €
  Gaz türbin (5-50 MW):               2,000,000 - 20,000,000 €

Belirsizlik: ±20-30%
```

### 2.3 Kazan (Boiler)

```
Ateş borulu kazan (Turton 2012):
  log₁₀(PEC_baz) = K₁ + K₂·log₁₀(Q) + K₃·(log₁₀(Q))²
  K₁ = 0.4091, K₂ = 0.8925, K₃ = 0.000  (Q: kW_th, bakınız not)

Buhar kazanı (Bejan et al. 1996):
  PEC = C_B · (ṁ_buhar)^0.8 · (P_buhar)^0.2 · f_M
  [USD, 1994]

HRSG (Heat Recovery Steam Generator):
  PEC = 6570 · (Q̇/ΔT_lm)^0.8 + 21276·ṁ_buhar + 1184.4·(Ẇ_P_fan)^0.71
  [USD, 2000]

Basınç düzeltme:
  f_P = 0.1089 + 0.08145·ln(P) + 0.0521·(ln(P))²  (P: bar_g)

Malzeme düzeltme:
  Karbon çelik:      f_M = 1.0
  Paslanmaz çelik:   f_M = 1.7-2.5
  Nikel alaşım:      f_M = 3.0-5.0

Tipik PEC aralığı:
  Küçük (0.5-2 t/h buhar):     50,000 - 200,000 €
  Orta (2-10 t/h buhar):       150,000 - 800,000 €
  Büyük (10-50 t/h buhar):     500,000 - 3,000,000 €

Belirsizlik: ±20-35%
```

### 2.4 Isı Değiştirici (Heat Exchanger — HX)

```
Gövde-boru (Shell & Tube) — Turton (2012):
  log₁₀(PEC_baz) = K₁ + K₂·log₁₀(A) + K₃·(log₁₀(A))²
  K₁ = 4.3247, K₂ = -0.3030, K₃ = 0.1634  (A: m², 10-1000 m²)

Plakalı (Plate) — Turton (2012):
  log₁₀(PEC_baz) = K₁ + K₂·log₁₀(A) + K₃·(log₁₀(A))²
  K₁ = 4.6656, K₂ = -0.1557, K₃ = 0.1547  (A: m², 1-500 m²)

Basınç düzeltme (gövde-boru):
  log₁₀(f_P) = 0.03881 - 0.11272·log₁₀(P) + 0.08183·(log₁₀(P))²
  (P: bar_g, tüp tarafı basıncı)

Malzeme düzeltme:
  CS/CS:    f_M = 1.0
  CS/SS:    f_M = 1.7
  SS/SS:    f_M = 2.9
  CS/Ni:    f_M = 3.2
  Ti/Ti:    f_M = 9.6

Tipik PEC aralığı:
  Küçük (1-10 m²):        5,000 - 30,000 €
  Orta (10-100 m²):       20,000 - 150,000 €
  Büyük (100-1000 m²):    100,000 - 800,000 €

Belirsizlik: ±25-40%
```

### 2.5 Pompa (Pump)

```
Santrifüj pompa — Turton (2012):
  log₁₀(PEC_baz) = K₁ + K₂·log₁₀(Ẇ) + K₃·(log₁₀(Ẇ))²
  K₁ = 3.3892, K₂ = 0.0536, K₃ = 0.1538  (Ẇ: kW, 1-300 kW)

Basınç düzeltme:
  log₁₀(f_P) = -0.3935 + 0.3957·log₁₀(P) - 0.00226·(log₁₀(P))²
  (P: bar_g, 10-100 bar)

Motor maliyeti (ayrı):
  log₁₀(PEC_motor) = K₁ + K₂·log₁₀(Ẇ) + K₃·(log₁₀(Ẇ))²
  K₁ = 2.9508, K₂ = 1.0688, K₃ = -0.1315  (Ẇ: kW, 1-150 kW)

Toplam: PEC_pompa = PEC_baz · f_M · f_P + PEC_motor

Tipik PEC aralığı (pompa + motor):
  Küçük (1-10 kW):       3,000 - 15,000 €
  Orta (10-75 kW):       10,000 - 60,000 €
  Büyük (75-300 kW):     40,000 - 200,000 €

Belirsizlik: ±20-30%
```

### 2.6 Chiller (Soğutma Makinesi)

```
Buhar sıkıştırmalı chiller:
  PEC = C_ch · (Q̇_soğutma)^α
  Tipik: C_ch = 540, α = 0.83  (Q̇: kW, 50-5000 kW)
  [EUR, 2020 bazlı]

Absorpsiyon chiller:
  PEC = C_abs · (Q̇_soğutma)^α
  Tipik: C_abs = 1300, α = 0.75  (Q̇: kW, 100-10000 kW)
  [EUR, 2020 bazlı]

Soğutma kulesi (ek):
  PEC_kule = C_CT · (Q̇_atık)^α
  Tipik: C_CT = 190, α = 0.7  (Q̇: kW, 100-10000 kW)

Tipik PEC aralığı (paket chiller):
  Küçük (50-200 kW):       40,000 - 120,000 €
  Orta (200-1000 kW):      80,000 - 450,000 €
  Büyük (1000-5000 kW):    300,000 - 1,500,000 €

Belirsizlik: ±25-40%
```

### 2.7 Kondenser (Condenser)

```
Hava soğutmalı kondenser:
  log₁₀(PEC_baz) = K₁ + K₂·log₁₀(A) + K₃·(log₁₀(A))²
  K₁ = 4.0336, K₂ = 0.2341, K₃ = 0.0497  (A: m², 2-500 m²)

Su soğutmalı kondenser:
  Shell & tube HX korelasyonları uygulanır (Bölüm 2.4)

Tipik PEC aralığı:
  Küçük (10-50 m²):       15,000 - 60,000 €
  Orta (50-200 m²):       40,000 - 200,000 €
  Büyük (200-1000 m²):    150,000 - 600,000 €

Belirsizlik: ±30-40%
```

## 3. Düzeltme Faktörleri

### 3.1 Malzeme Düzeltme Faktörleri (f_M)

| Malzeme | f_M Aralığı | Tipik Uygulama |
|---------|-------------|-----------------|
| Karbon çelik | 1.0 | Standart, düşük sıcaklık |
| Paslanmaz 304 | 1.3-1.7 | Korozif ortam, gıda |
| Paslanmaz 316 | 1.7-2.5 | Kimyasal proses |
| Duplex SS | 2.5-3.5 | Yüksek korozyon |
| Nikel alaşımı | 3.0-5.0 | Yüksek sıcaklık, agressif ortam |
| Titanyum | 7.0-10.0 | Özel uygulamalar |
| Hastelloy | 5.0-8.0 | Aşırı korozyon |

### 3.2 Basınç Düzeltme Faktörleri (f_P)

```
Genel formül (Turton 2012):
log₁₀(f_P) = C₁ + C₂·log₁₀(P_bar_g) + C₃·(log₁₀(P_bar_g))²

Pratik aralıklar:
  0-10 bar_g:    f_P = 1.0-1.2
  10-40 bar_g:   f_P = 1.2-1.8
  40-100 bar_g:  f_P = 1.8-3.5
  100-300 bar_g: f_P = 3.5-8.0
```

### 3.3 Sıcaklık Düzeltme Faktörü (f_T)

```
Genel kural:
  T < 400°C:   f_T = 1.0 (karbon çelik yeterli)
  400-600°C:    f_T = 1.5-2.5 (alaşım çelik gerekli)
  600-800°C:    f_T = 2.5-4.0 (süper alaşım)
  > 800°C:      f_T = 4.0-8.0 (özel malzeme)
```

## 4. Zaman Düzeltmesi (CEPCI)

```
PEC_güncel = PEC_referans × (CEPCI_güncel / CEPCI_referans)

CEPCI Değerleri:
  1994: 368.1 (Bejan korelasyonları referans yılı)
  2000: 394.1
  2001: 394.3 (Turton 2003 referansı)
  2005: 468.2
  2010: 550.8
  2012: 584.6 (Turton 2012 referansı)
  2015: 556.8
  2018: 603.1
  2020: 596.2
  2022: 816.0
  2023: 797.9
  2024: 810 (tahmini)
  2025: 825 (tahmini)
```

> CEPCI değerleri için detaylı tablo: `cost_databases.md`

## 5. Toplam Yatırım Maliyeti (TCI)

```
PEC → TCI dönüşümü:

TCI = PEC × FCI_faktör × TCI_faktör

Tipik faktörler:
  PEC → Teslim (Delivered):     × 1.05-1.10
  Teslim → Kurulum (Installed): × 1.40-1.65
  Kurulum → ISBL:               × 1.15-1.30
  ISBL → TCI:                   × 1.15-1.40

Pratik özet:
  TCI ≈ PEC × 4.0-6.0 (grassroots — yeni tesis)
  TCI ≈ PEC × 2.5-3.5 (retrofit — mevcut tesise ekleme)
  TCI ≈ PEC × 1.5-2.0 (modifikasyon — mevcut ekipman değişikliği)

ExergyLab önerisi (Türkiye, endüstriyel retrofit):
  TCI ≈ PEC × 3.0 (ortalama)
```

## 6. Belirsizlik ve Doğrulama

### 6.1 PEC Korelasyonu Belirsizlik Aralıkları

| Kaynak | Belirsizlik | Geçerlilik |
|--------|-------------|------------|
| Bejan 1996 | ±25-40% | 1994 bazlı, genel |
| Turton 2012 | ±20-35% | 2001/2012 bazlı, kimya endüstrisi |
| Üretici teklifi | ±5-10% | Güncel, spesifik |
| Benzer tesis verisi | ±15-25% | Lokasyon bağımlı |

### 6.2 Duyarlılık Analizi Gerekliliği

```
PEC belirsizliği yüksek olduğunda:

1. ±30% PEC variasyonu ile f_k ve r_k'nin değişimini kontrol et
2. Eğer karar değişmiyorsa → Korelasyon yeterli
3. Eğer karar değişiyorsa → Üretici teklifi al

Pratik kural:
  PEC < €50,000 → Korelasyon genellikle yeterli
  PEC > €500,000 → Üretici teklifi önerilir
  Aradaki → Duyarlılık analizi ile karar
```

## 7. Türkiye'ye Özel Düzeltmeler

```
Uluslararası korelasyonlar genellikle USD bazlıdır.
Türkiye uygulaması için:

1. Döviz dönüşümü: PEC_TRY = PEC_USD × Kur_USD/TRY
   veya PEC_EUR = PEC_USD × Kur_USD/EUR

2. Lokasyon faktörü:
   Türkiye / ABD: 0.85-1.10 (ekipman ithal)
   Türkiye / Batı Avrupa: 0.90-1.05

3. Yerli üretim avantajı:
   Kazan, HX, pompa: ×0.60-0.80 (yerli üretim mevcutsa)
   Kompresör, türbin: ×0.90-1.00 (çoğunlukla ithal)
   Chiller: ×0.80-0.95 (bazı yerli üretim)

4. Gümrük ve vergi:
   İthal ekipman: +%18 KDV + %0-5 gümrük
   Teşvikli yatırım: KDV istisnası olabilir
```

## 8. Hızlı Referans — PEC Tahmin Tablosu

| Ekipman | Kapasite | PEC_2024 [€] | Not |
|---------|----------|--------------|-----|
| Kompresör (vidalı) | 100 kW | 45,000-75,000 | VSD dahil |
| Kompresör (santrifüj) | 500 kW | 200,000-400,000 | — |
| Buhar türbin | 1 MW | 400,000-700,000 | Yoğuşmalı |
| Gaz türbin | 5 MW | 3,000,000-5,000,000 | Paket |
| Kazan (ateş borulu) | 5 t/h | 200,000-400,000 | 10 bar |
| Kazan (su borulu) | 20 t/h | 800,000-1,500,000 | 20 bar |
| HX (gövde-boru) | 50 m² | 25,000-50,000 | CS/CS |
| HX (plakalı) | 50 m² | 15,000-35,000 | SS |
| Pompa (santrifüj) | 30 kW | 8,000-20,000 | + motor |
| Chiller (vidalı) | 500 kW | 120,000-250,000 | Su soğutmalı |
| Chiller (santrifüj) | 2000 kW | 350,000-700,000 | Su soğutmalı |
| Kondenser | 100 m² | 40,000-80,000 | Su soğutmalı |
| Soğutma kulesi | 1000 kW | 30,000-60,000 | Açık tip |

> Bu değerler ±30% belirsizlik içerir ve ön fizibilite amaçlıdır.

## İlgili Dosyalar

- `factory/exergoeconomic/levelized_cost.md` — CRF ve Ż hesaplaması
- `factory/exergoeconomic/cost_databases.md` — CEPCI, Marshall & Swift verileri
- `factory/exergoeconomic/sensitivity_analysis.md` — PEC belirsizliği analizi
- `factory/economic_analysis.md` — Genel ekonomik analiz yöntemleri

## Referanslar

1. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Appendix B.
2. Turton, R., Bailie, R.C., Whiting, W.B., Shaeiwitz, J.A. (2012). *Analysis, Synthesis, and Design of Chemical Processes*. 4th Ed. Chapter 22.
3. Couper, J.R., Penney, W.R., Fair, J.R., Walas, S.M. (2012). *Chemical Process Equipment: Selection and Design*. 3rd Ed.
4. Peters, M.S., Timmerhaus, K.D., West, R.E. (2003). *Plant Design and Economics for Chemical Engineers*. 5th Ed.
5. Chemical Engineering Magazine — CEPCI monthly reports.
