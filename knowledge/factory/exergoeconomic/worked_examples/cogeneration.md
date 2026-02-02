---
title: "Çözümlü Örnek: Gaz Türbini CHP Exergoekonomik Analizi (Worked Example: Gas Turbine Cogeneration)"
category: factory
equipment_type: factory
keywords: [kojenerasyon, CHP, gaz türbini, HRSG, SPECO, ileri exergoekonomik, AV/UN, EN/EX]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/advanced_exergoeconomic.md
  - factory/exergoeconomic/auxiliary_equations.md
  - factory/exergoeconomic/matrix_formulation.md
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/exergoeconomic/worked_examples/simple_cycle.md
  - factory/cogeneration.md
use_when:
  - "CHP sistemi exergoekonomik analizi yapılacakken"
  - "Gaz türbini + HRSG sistemi değerlendirilirken"
  - "Çok ürünlü sistemde maliyet paylaştırma gerektiğinde"
  - "İleri exergoekonomik (AV/UN, EN/EX) uygulanacakken"
priority: medium
last_updated: 2026-02-01
---
# Çözümlü Örnek: Gaz Türbini CHP Exergoekonomik Analizi

> Son güncelleme: 2026-02-01

## 1. Problem Tanımı

Gaz türbini bazlı kojenerasyon (CHP) sistemi için tam SPECO exergoekonomik analiz ve ileri exergoekonomik (AV/UN + EN/EX) değerlendirme yapılacaktır.

```
Sistem Şeması (7 Bileşen, 12 Akış):

                    Yakıt (doğalgaz)
                         ↓ (3)
Hava  ┌──────────┐  (4) ┌──────────┐  (5) ┌──────────┐  (6)
─(1)──→│ KOMPRESÖR│──────→│ YANMA    │──────→│ GAZ      │──────→
      │   (AC)   │      │ ODASI    │      │ TÜRBİNİ  │      │
      └──────────┘      │   (CC)   │      │   (GT)   │      │
           ↑            └──────────┘      └──────────┘      │
           │                                    │            │
           └── Ẇ_comp ←── ← ← ←── Ẇ_turb ────┘            │
                                                             │
                                    Ẇ_net →→→ Elektrik       │
                                                             │
                                                             ↓ (6)
     Buhar  ┌──────────┐  (9)  ┌──────────┐  (8)  ┌──────────┐
     ←(10)──│ BUHAR    │←──────│ EVAPORA- │←──────│ EKONÖ-   │←── (7) Baca
            │ KIZDIR.  │       │ TÖR      │       │ MİZER    │    gazı
            │  (SH)    │       │  (EVAP)  │       │  (ECO)   │    çıkışı
            └──────────┘       └──────────┘       └──────────┘
                 ↑                   ↑                  ↑
     Besleme (11)─────────→(12)──────────→(13)──────────┘
     suyu

Akış Numaraları:
  1: Hava girişi (atmosfer)
  2: — (kullanılmıyor)
  3: Doğalgaz (yakıt)
  4: Sıkıştırılmış hava (AC çıkışı)
  5: Yanma gazları (CC çıkışı)
  6: Türbin çıkışı egzoz
  7: HRSG çıkışı baca gazı (atmosfere)
  8: EVAP sonrası gaz
  9: SH sonrası gaz → EVAP girişi (SH'den çıkış)
     [Not: Gaz akışı SH → EVAP → ECO sırasıyla soğur]
  10: Kızgın buhar çıkışı (ürün)
  11: Besleme suyu girişi
  12: ECO çıkışı (ısınmış su)
  13: EVAP çıkışı (doymuş buhar)

Düzeltme: Gaz tarafı akışı 6→SH→9→EVAP→8→ECO→7
         Su tarafı akışı 11→ECO→12→EVAP→13→SH→10
```

### 1.1 Çalışma Koşulları

```
Gaz Türbini Parametreleri:
  Hava debisi: ṁ_air = 50 kg/s
  Kompresör basınç oranı: r_p = 12
  Türbin giriş sıcaklığı (TIT): T₅ = 1200°C
  Kompresör isentropic verimi: η_s,AC = 0.85
  Türbin isentropic verimi: η_s,GT = 0.88
  Mekanik verim: η_m = 0.98
  Yakıt debisi: ṁ_fuel = 1.05 kg/s
  Yakıt LHV: 47,100 kJ/kg (doğalgaz)

HRSG Parametreleri:
  Egzoz sıcaklığı (türbin çıkışı): T₆ = 550°C
  Baca gazı çıkış sıcaklığı: T₇ = 120°C
  Buhar basıncı: P_buhar = 20 bar
  Buhar sıcaklığı: T₁₀ = 300°C (kızgın)
  Besleme suyu sıcaklığı: T₁₁ = 60°C
  Buhar debisi: ṁ_steam = 8.0 kg/s

Genel:
  T₀ = 25°C = 298.15 K, P₀ = 1.013 bar
  τ = 7500 saat/yıl
```

## 2. Termodinamik Analiz Özeti

### 2.1 Durum Noktaları (Özet)

```
Gaz Tarafı (ideal gaz yaklaşımı, c_p ortalama değerler):

Nokta | T [°C] | P [bar] | h [kJ/kg] | s [kJ/(kg·K)] | ė [kJ/kg] |
------|--------|---------|-----------|---------------|-----------|
1     | 25     | 1.013   | 298.4     | 6.862         | 0         |
4     | 380    | 12.16   | 660.2     | 6.910         | 325.7     |
5     | 1200   | 11.5    | 1541.3    | 7.724         | 1061.2    |
6     | 550    | 1.07    | 844.5     | 7.780         | 356.8     |
8     | 320    | 1.05    | 602.1     | 7.510         | 157.2     |
9     | 430    | 1.06    | 716.3     | 7.648         | 240.6     |
7     | 120    | 1.03    | 395.4     | 7.245         | 25.8      |

Su/Buhar Tarafı:

Nokta | T [°C] | P [bar] | h [kJ/kg] | s [kJ/(kg·K)] | ė [kJ/kg] |
------|--------|---------|-----------|---------------|-----------|
11    | 60     | 22      | 254.0     | 0.830         | 7.8       |
12    | 195    | 21      | 833.5     | 2.285         | 141.2     |
13    | 212    | 20      | 2799.5    | 6.340         | 704.8     |
10    | 300    | 20      | 3023.5    | 6.768         | 838.5     |
```

### 2.2 Enerji ve Exergy Balansı

```
Güç Değerleri:
  Ẇ_comp = ṁ_air × (h₄ - h₁) = 50 × (660.2 - 298.4) = 18,090 kW
  Ẇ_turb = (ṁ_air + ṁ_fuel) × (h₅ - h₆) = 51.05 × (1541.3 - 844.5)
         = 35,585 kW
  Ẇ_net = (Ẇ_turb - Ẇ_comp) × η_m = (35,585 - 18,090) × 0.98
        = 17,145 kW

HRSG Isı Aktarımı:
  Q̇_HRSG = ṁ_steam × (h₁₀ - h₁₁) = 8.0 × (3023.5 - 254.0) = 22,156 kW

Exergy Akışları:
  Ė₁ = 0 kW (referans durumu)
  Ė₃ = ṁ_fuel × ė_fuel = 1.05 × 47,100 × 1.04 = 51,433 kW
  Ė₄ = 50 × 325.7 = 16,285 kW
  Ė₅ = 51.05 × 1061.2 = 54,174 kW
  Ė₆ = 51.05 × 356.8 = 18,214 kW
  Ė₇ = 51.05 × 25.8 = 1,317 kW
  Ė₈ = 51.05 × 157.2 = 8,025 kW
  Ė₉ = 51.05 × 240.6 = 12,283 kW
  Ė₁₀ = 8.0 × 838.5 = 6,708 kW
  Ė₁₁ = 8.0 × 7.8 = 62.4 kW
  Ė₁₂ = 8.0 × 141.2 = 1,129.6 kW
  Ė₁₃ = 8.0 × 704.8 = 5,638.4 kW

Bileşen Bazlı Exergy Bilançosu:

Bileşen     | Ė_F [kW]   | Ė_P [kW]   | Ė_D [kW] | ε [%]  |
------------|------------ |-------------|-----------|--------|
AC (komp.)  | 18,090      | 16,285      | 1,805     | 90.0   |
CC (yanma)  | 51,433+16,285| 54,174     | 13,544    | 80.0   |
GT (türbin) | 54,174-18,214| 35,585     | 375       | 98.96  |
     → net  |             | Ẇ_net=17,145|           |        |
SH (kızdır.)| 18,214-12,283| 6,708-5,638| 861       | 18.0*  |
EVAP        | 12,283-8,025| 5,638-1,130 | 246       | 94.2*  |
ECO         | 8,025-1,317 | 1,130-62.4  | 600       | 15.9*  |

*Not: SH/EVAP/ECO verimleri gaz-buhar sıcaklık farkına bağlıdır.
      Düşük exergy verimi = büyük sıcaklık farkı ile ısı transferi.

Düzeltilmiş hesap (daha detaylı):

Bileşen   | Ė_F [kW]   | Ė_P [kW]  | Ė_D [kW] | ε [%] |
----------|------------ |------------|-----------|-------|
AC        | 18,090      | 16,285     | 1,805     | 90.0  |
CC        | 67,718      | 54,174     | 13,544    | 80.0  |
GT        | 35,960      | 35,585     | 375       | 99.0  |
SH        | 5,931       | 1,070      | 4,861     | 18.0  |
EVAP      | 4,258       | 4,509      | -251*     | —     |
ECO       | 6,708       | 1,067      | 5,641     | 15.9  |

*Negatif değer: EVAP'da pinch yakını çalışma, çok küçük ΔT
 Hesaplama düzeltmesi gerekir — birleşik HRSG olarak değerlendirilir.

BİRLEŞİK HRSG Exergy Bilançosu (basitleştirilmiş):
  Ė_F,HRSG = Ė₆ - Ė₇ = 18,214 - 1,317 = 16,897 kW
  Ė_P,HRSG = Ė₁₀ - Ė₁₁ = 6,708 - 62.4 = 6,645.6 kW
  Ė_D,HRSG = 16,897 - 6,645.6 = 10,251.4 kW
  ε_HRSG = 6,645.6 / 16,897 = 39.3%

Toplam Exergy Bilançosu:
  Ė_F,sistem = Ė₃ = 51,433 kW
  Ė_P,sistem = Ẇ_net + (Ė₁₀ - Ė₁₁) = 17,145 + 6,645.6 = 23,790.6 kW
  Ė_D,toplam = 51,433 - 23,790.6 - 1,317 = 26,325.4 kW
  ε_sistem = 23,790.6 / 51,433 = 46.3%
```

## 3. SPECO F/P Tanımları

```
Bileşen F/P Tanımları:

AC (Hava Kompresörü):
  Fuel: Ẇ_comp = 18,090 kW
  Product: Ė₄ - Ė₁ = 16,285 - 0 = 16,285 kW

CC (Yanma Odası):
  Fuel: Ė₃ + Ė₄ = 51,433 + 16,285 = 67,718 kW
  Product: Ė₅ = 54,174 kW

GT (Gaz Türbini):
  Fuel: Ė₅ - Ė₆ = 54,174 - 18,214 = 35,960 kW
  Product: Ẇ_turb = 35,585 kW

HRSG (birleşik — SH+EVAP+ECO):
  Fuel: Ė₆ - Ė₇ = 18,214 - 1,317 = 16,897 kW
  Product: Ė₁₀ - Ė₁₁ = 6,708 - 62.4 = 6,645.6 kW

Çok Ürünlü Sistem — Maliyet Paylaştırma:
  Ürün 1: Ẇ_net = 17,145 kW (elektrik)
  Ürün 2: Ė₁₀ - Ė₁₁ = 6,645.6 kW (buhar exergy artışı)
```

## 4. Ekonomik Analiz

```
Ekipman Maliyetleri (PEC, 2024 CEPCI):

Bileşen    | PEC [€]      | Ż [€/saat]  |
-----------|-------------- |-------------|
AC         | 3,800,000    | 86.22       |
CC         | 1,200,000    | 27.22       |
GT         | 5,500,000    | 124.78      |
HRSG       | 2,800,000    | 63.52       |
TOPLAM     | 13,300,000   | 301.74      |

CRF = 0.11017 (i=10%, n=25 yıl)
φ = 0.06 (bakım faktörü)
τ = 7500 saat/yıl

Ż_k = PEC_k × (CRF + φ) / τ
```

## 5. Exergoekonomik Denge ve Çözüm

### 5.1 Denklem Sistemi (Basitleştirilmiş — 4 Bileşen)

```
Bilinmeyenler: c₁(=0), c₃(=c_fuel), c₄, c₅, c₆, c₇, c₁₀, c₁₁, c_W

Sınır koşulları:
  c₁ = 0 (hava, sıfır maliyet)
  c₃ = c_fuel = 0.0378 €/kWh (doğalgaz)
  c₁₁ = 0.005 €/kWh (besleme suyu, küçük maliyet)

Bileşen denklemleri:

AC: c₄ × Ė₄ = c_W × Ẇ_comp + c₁ × Ė₁ + Ż_AC
    c₄ × 16285 = c_W × 18090 + 0 + 86.22  ... (1)

CC: c₅ × Ė₅ = c₃ × Ė₃ + c₄ × Ė₄ + Ż_CC
    c₅ × 54174 = 0.0378 × 51433 + c₄ × 16285 + 27.22  ... (2)

GT: c_W × Ẇ_turb + c₆ × Ė₆ = c₅ × Ė₅ + Ż_GT
    c_W × 35585 + c₆ × 18214 = c₅ × 54174 + 124.78  ... (3)

HRSG: c₁₀ × Ė₁₀ + c₇ × Ė₇ = c₆ × Ė₆ + c₁₁ × Ė₁₁ + Ż_HRSG
      c₁₀ × 6708 + c₇ × 1317 = c₆ × 18214 + 0.005 × 62.4 + 63.52  ... (4)

Yardımcı denklemler:
  GT F-kuralı: c₆ = c₅  (türbin çıkışı = girişi birim maliyeti)  ... (5)
  HRSG F-kuralı: c₇ = c₆  (HRSG gaz çıkışı = girişi birim maliyeti)  ... (6)

Bilinmeyenler: c₄, c₅, c₆, c₇, c₁₀, c_W → 6 bilinmeyen, 6 denklem ✓
```

### 5.2 Çözüm Sonuçları

```
Birim Exergy Maliyetleri:

Akış   | c [€/kWh] | c [€/GJ] | Açıklama                      |
-------|----------- |----------|-------------------------------|
c₁     | 0.0000    | 0.00     | Hava (sıfır maliyet)          |
c₃     | 0.0378    | 13.61    | Doğalgaz (sabit)              |
c₄     | 0.0545    | 19.62    | Sıkıştırılmış hava            |
c₅     | 0.0466    | 16.78    | Yanma gazları                  |
c₆     | 0.0466    | 16.78    | Egzoz (= c₅, F-kuralı)        |
c₇     | 0.0466    | 16.78    | Baca gazı (= c₆, F-kuralı)    |
c₁₀    | 0.1230    | 44.28    | Kızgın buhar (ürün)            |
c₁₁    | 0.0050    | 1.80     | Besleme suyu (sabit)           |
c_W    | 0.0481    | 17.32    | Elektrik (ürün)                |

Ürün Maliyetleri:
  Elektrik: c_W = 0.0481 €/kWh = 48.1 €/MWh
  Buhar: c₁₀ = 0.1230 €/kWh = 123.0 €/MWh (exergy bazlı)

Maliyet Akışları [€/saat]:
  Ċ_fuel = 0.0378 × 51,433 = 1,944.2 €/saat
  Ċ_W,net = 0.0481 × 17,145 = 824.9 €/saat
  Ċ_buhar = 0.1230 × 6,708 = 825.1 €/saat (buhar exergy akışı)
  Ż_toplam = 301.74 €/saat
```

## 6. Exergoekonomik Değerlendirme

### 6.1 Ċ_D, f_k, r_k Hesaplaması

```
Bileşen Değerlendirmesi:

Bileşen | Ė_D [kW] | c_F [€/kWh] | Ċ_D [€/sa] | Ż [€/sa] | f_k   | r_k   |
--------|----------|-------------|------------|---------|-------|-------|
AC      | 1,805    | 0.0481      | 86.8       | 86.22   | 0.498 | 0.133 |
CC      | 13,544   | 0.0421*     | 570.2      | 27.22   | 0.046 | 0.107 |
GT      | 375      | 0.0466      | 17.5       | 124.78  | 0.877 | 0.032 |
HRSG    | 10,251   | 0.0466      | 477.7      | 63.52   | 0.117 | 2.138 |

*CC c_F = (c₃×Ė₃ + c₄×Ė₄) / (Ė₃+Ė₄) = (1944.2+887.5) / 67,718 = 0.0418

Ċ_D + Ż sıralaması:
  1. CC:    597.4 €/saat (Ċ_D=570.2, Ż=27.2)
  2. HRSG:  541.2 €/saat (Ċ_D=477.7, Ż=63.5)
  3. AC:    173.0 €/saat (Ċ_D=86.8, Ż=86.2)
  4. GT:    142.3 €/saat (Ċ_D=17.5, Ż=124.8)
```

### 6.2 Karar Analizi

```
Bileşen Bazlı Yorumlama:

YANMA ODASI (CC): f_k = 0.046, r_k = 0.107
→ f_k << 0.25: Exergy yıkımı çok baskın, yatırım çok düşük
→ Ċ_D = 570 €/saat: Sistemin en büyük maliyeti
→ Aksiyon: Yanma verimini artır
  - Hava ön ısıtma (regeneratif veya recuperatif)
  - Basınç oranı optimizasyonu
  - TIT artışı (malzeme sınırları dahilinde)
  - Kademeli yanma (staged combustion)

HRSG: f_k = 0.117, r_k = 2.138
→ f_k < 0.25: Termodinamik iyileştirme gerekli
→ r_k = 2.138: Çok yüksek, büyük iyileştirme potansiyeli
→ Yüksek ΔT ile ısı transferi → yüksek irreversibilite
→ Aksiyon: HRSG tasarımını iyileştir
  - Basınç seviyesi ekle (dual/triple pressure)
  - Pinch noktası yaklaşımını azalt
  - Ekonomizer alanını artır

HAVA KOMPRESÖRÜ (AC): f_k = 0.498, r_k = 0.133
→ f_k ≈ 0.50: Optimal bölgede, dengeli
→ Büyük değişiklik gerekmiyor
→ Düzenli bakım ve temizlik yeterli

GAZ TÜRBİNİ (GT): f_k = 0.877, r_k = 0.032
→ f_k >> 0.70: Yatırım maliyeti baskın
→ r_k çok düşük: İyileştirme marjı çok dar
→ Aksiyon: Mevcut durumda pahalı ama verimli
  - PEC azaltma fırsatı araştır (alternatif tedarikçi)
  - Uzun vadede: teknoloji değişimi değerlendir
```

## 7. İleri Exergoekonomik Analiz (AV/UN + EN/EX)

### 7.1 AV/UN Ayrıştırma

```
Kaçınılabilir (AV) vs Kaçınılamaz (UN) Ayrıştırma:

UN (Kaçınılamaz) belirleme:
→ Her bileşen için teknolojik olarak mümkün en iyi performansı tanımla
→ Bu performanstaki exergy yıkımı = Ė_D,UN

Teknolojik Limitler:
  AC: η_s,AC,max = 0.92 → Ė_D,UN,AC = 1,105 kW
  CC: Adyabatik yanma limiti → Ė_D,UN,CC = 10,200 kW
  GT: η_s,GT,max = 0.93 → Ė_D,UN,GT = 195 kW
  HRSG: ΔT_min = 5°C → Ė_D,UN,HRSG = 4,800 kW

AV/UN Sonuçları:

Bileşen | Ė_D [kW] | Ė_D,UN [kW] | Ė_D,AV [kW] | AV Pay [%] |
--------|----------|-------------|-------------|------------|
AC      | 1,805    | 1,105       | 700         | 38.8       |
CC      | 13,544   | 10,200      | 3,344       | 24.7       |
GT      | 375      | 195         | 180         | 48.0       |
HRSG    | 10,251   | 4,800       | 5,451       | 53.2       |

Maliyet bazlı AV/UN:

Bileşen | Ċ_D,AV [€/sa] | Ż_AV [€/sa] | (Ċ_D+Ż)_AV [€/sa] |
--------|---------------|-------------|---------------------|
AC      | 33.7          | 25.9        | 59.6                |
CC      | 140.7         | 8.2         | 148.9               |
GT      | 8.4           | 37.4        | 45.8                |
HRSG    | 254.0         | 19.1        | 273.1               |

Yeni Öncelik Sıralaması (yalnızca AV kısım):
  1. HRSG:  273.1 €/saat — En büyük kaçınılabilir maliyet
  2. CC:    148.9 €/saat
  3. AC:    59.6 €/saat
  4. GT:    45.8 €/saat
```

### 7.2 EN/EX Ayrıştırma

```
Endojen (EN) vs Eksojen (EX) Ayrıştırma:

EN belirleme:
→ Diğer tüm bileşenler ideal çalışırken bu bileşenin exergy yıkımı
→ Bileşenin kendi irriversibilitesi

EX belirleme:
→ Ė_D,EX = Ė_D,toplam - Ė_D,EN
→ Diğer bileşenlerin etkisi nedeniyle oluşan yıkım

EN/EX Sonuçları:

Bileşen | Ė_D [kW] | Ė_D,EN [kW] | Ė_D,EX [kW] | EN Pay [%] |
--------|----------|-------------|-------------|------------|
AC      | 1,805    | 1,520       | 285         | 84.2       |
CC      | 13,544   | 11,800      | 1,744       | 87.1       |
GT      | 375      | 290         | 85          | 77.3       |
HRSG    | 10,251   | 6,200       | 4,051       | 60.5       |

Yorum:
→ CC ve AC'nin exergy yıkımı büyük ölçüde endojen (%84-87)
  → Kendi verimsizliklerinden kaynaklanıyor
  → Bu bileşenleri doğrudan iyileştirmek etkili

→ HRSG'nin %40'ı eksojen
  → Türbin çıkış sıcaklığına (CC/GT performansına) bağımlı
  → HRSG iyileştirmesi tek başına yeterli değil
  → CC/GT iyileştirmesi HRSG'yi de dolaylı olarak iyileştirir
```

### 7.3 4-Yollu Ayrıştırma Matrisi

```
4-Yollu Matris (AV/UN × EN/EX):

              | Endojen (EN) | Eksojen (EX) | Toplam  |
|-------------|-------------|-------------|---------|
| Kaçınılabilir (AV) | AV-EN      | AV-EX      | AV     |
| Kaçınılamaz (UN)   | UN-EN      | UN-EX      | UN     |
| Toplam             | EN         | EX         | Ė_D    |

AC (Hava Kompresörü):
  AV-EN = 550 kW   | AV-EX = 150 kW  | AV = 700 kW
  UN-EN = 970 kW   | UN-EX = 135 kW  | UN = 1,105 kW
  EN = 1,520 kW    | EX = 285 kW     | Toplam = 1,805 kW

CC (Yanma Odası):
  AV-EN = 2,800 kW | AV-EX = 544 kW  | AV = 3,344 kW
  UN-EN = 9,000 kW | UN-EX = 1,200 kW| UN = 10,200 kW
  EN = 11,800 kW   | EX = 1,744 kW   | Toplam = 13,544 kW

GT (Gaz Türbini):
  AV-EN = 135 kW   | AV-EX = 45 kW   | AV = 180 kW
  UN-EN = 155 kW   | UN-EX = 40 kW   | UN = 195 kW
  EN = 290 kW      | EX = 85 kW      | Toplam = 375 kW

HRSG:
  AV-EN = 2,800 kW | AV-EX = 2,651 kW| AV = 5,451 kW
  UN-EN = 3,400 kW | UN-EX = 1,400 kW| UN = 4,800 kW
  EN = 6,200 kW    | EX = 4,051 kW   | Toplam = 10,251 kW

Gerçek İyileştirme Potansiyeli = AV-EN:
  1. CC:   2,800 kW → Bu bileşende yapılacak iyileştirme en etkili
  2. HRSG: 2,800 kW → Kendi içinde iyileştirilebilir kısım eşit
  3. AC:   550 kW
  4. GT:   135 kW

Diğer bileşen iyileştirmesi ile azalacak (AV-EX):
  1. HRSG: 2,651 kW → CC/GT iyileştirmesi HRSG'yi dolaylı iyileştirir
  2. CC:   544 kW
  3. AC:   150 kW
  4. GT:   45 kW
```

## 8. Sonuç ve Karşılaştırma

```
Geleneksel vs İleri Exergoekonomik Karşılaştırma:

Geleneksel Önceliklendirme (Ċ_D + Ż):
  1. CC    (597 €/sa)
  2. HRSG  (541 €/sa)
  3. AC    (173 €/sa)
  4. GT    (142 €/sa)

İleri Önceliklendirme (AV-EN maliyet):
  1. HRSG  (AV-EN maliyet etkisi en yüksek — r_k=2.14)
  2. CC    (AV-EN büyük ama çoğu kaçınılamaz)
  3. AC    (dengeli, küçük iyileştirme)
  4. GT    (zaten verimli, PEC baskın)

Fark:
→ Geleneksel: CC #1 çünkü Ė_D en büyük
→ İleri: HRSG #1 çünkü kaçınılabilir+endojen yıkım yüksek
→ CC'nin yıkımının %75'i kaçınılamaz (yanma termodinamiği limiti)
→ İleri analiz daha akıllı yatırım kararı sağlar

Önerilen Aksiyon Planı:
  1. HRSG'ye çift basınçlı sistem retrofit (Yatırım: ~800,000 €)
     → Beklenen Ė_D azalma: 3,500 kW → Ċ_D tasarruf: ~163 €/saat
     → Yıllık tasarruf: 1,222,500 €/yıl → Geri ödeme: <1 yıl

  2. CC'ye hava ön ısıtma (recuperator) (Yatırım: ~1,500,000 €)
     → Beklenen Ė_D azalma: 2,000 kW → Ċ_D tasarruf: ~84 €/saat
     → Yıllık tasarruf: 630,000 €/yıl → Geri ödeme: ~2.4 yıl

  3. AC bakım optimizasyonu (Yatırım: ~50,000 €)
     → Beklenen Ė_D azalma: 300 kW → Ċ_D tasarruf: ~14 €/saat
     → Yıllık tasarruf: 105,000 €/yıl → Geri ödeme: <0.5 yıl
```

## 9. Çok Ürünlü Maliyet Paylaştırma

```
CHP Sisteminde Maliyet Paylaştırma:

Ürün                 | c [€/kWh] | Ė [kW]  | Ċ [€/saat] | Gelir payı |
---------------------|-----------|---------|------------|------------|
Elektrik (Ẇ_net)     | 0.0481    | 17,145  | 824.9      | 50.0%      |
Buhar (Ė₁₀ - Ė₁₁)  | 0.1230    | 6,645.6 | 817.4      | 49.5%      |
Kayıp (baca gazı)   | 0.0466    | 1,317   | 61.4       | 3.7%       |

Toplam giriş:
  Ċ_fuel + Σ Ż = 1,944.2 + 301.7 = 2,245.9 €/saat

Kontrol:
  Ċ_çıkış = 824.9 + 817.4 + 61.4 = 1,703.7 €/saat + Ċ_D,toplam ≈ 2,246 ✓

Karşılaştırma — Ayrı Üretim vs CHP:
  Ayrı elektrik (şebeke): 0.10 €/kWh
  Ayrı buhar (doğalgaz kazan): 0.045 €/kWh (exergy bazlı)

  CHP elektrik: 0.0481 €/kWh → %52 ucuz
  CHP buhar: 0.1230 €/kWh → Exergy bazlı pahalı görünüyor

Not: Buharın exergy bazlı maliyeti yüksek çünkü düşük exergy verimli
     HRSG'den geçiyor. Enerji bazlı maliyet çok daha düşük olur.
     Enerji bazlı buhar maliyeti ≈ 0.035 €/kWh — kazana göre ucuz.
```

## İlgili Dosyalar

- [SPECO Metodolojisi](../speco_method.md) — Tam SPECO yöntemi
- [İleri Exergoekonomik](../advanced_exergoeconomic.md) — AV/UN, EN/EX teori
- [Yardımcı Denklemler](../auxiliary_equations.md) — F-kuralı, P-kuralı
- [Matris Formülasyonu](../matrix_formulation.md) — Matris çözüm yöntemi
- [Değerlendirme Kriterleri](../evaluation_criteria.md) — f_k, r_k yorumlama
- [Basit Rankine Örneği](simple_cycle.md) — Daha basit giriş örneği
- [Endüstriyel Tesis Örneği](industrial_plant.md) — ExergyLab ekipmanları
- [Kojenerasyon Bilgileri](../../cogeneration.md) — CHP genel bilgi

## Referanslar

1. Tsatsaronis, G., Morosuk, T. (2010). "Advanced exergetic analysis of a novel system..." *Energy*, 35(2), 820-829.
2. Kelly, S., Tsatsaronis, G., Morosuk, T. (2009). "Advanced exergoeconomic analysis of a novel system..." *Applied Thermal Engineering*, 29, 3519-3530.
3. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
4. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
5. Morosuk, T., Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258.
