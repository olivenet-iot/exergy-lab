---
title: "Hedefleme Teknikleri (Targeting Techniques)"
category: factory
equipment_type: factory
keywords: [enerji hedefleme, alan hedefleme, maliyet hedefleme, Bath formülü, eşanjör sayısı]
related_files: [factory/pinch/fundamentals.md, factory/pinch/composite_curves.md, factory/pinch/delta_t_min.md, factory/pinch/cost_estimation.md]
use_when: ["Enerji hedefleri belirlenirken", "Alan hedefleme yapılırken", "Minimum eşanjör sayısı hesaplanırken"]
priority: high
last_updated: 2026-02-01
---

# Hedefleme Teknikleri (Targeting Techniques)

Pinch analizinin en güçlü yönlerinden biri, ısı eşanjör ağı (Heat Exchanger Network — HEN) tasarlanmadan **önce** hedef değerlerin belirlenebilmesidir. Bu hedefler; minimum enerji tüketimi, minimum ısı transfer alanı, minimum eşanjör sayısı ve minimum toplam yıllık maliyet olarak sıralanır. Hedefleme (targeting), tasarım öncesi karar verme sürecini güçlendirir ve yatırım kararlarını destekler.

## Referans Problem

Bu dokümanda aşağıdaki referans problem kullanılmaktadır:

```
Akışlar (Streams):
─────────────────────────────────────────────────────
Akış   Tip     T_in(°C)  T_out(°C)  CP(kW/°C)  Q(kW)
─────────────────────────────────────────────────────
H1     Sıcak   270       80         15          2850
H2     Sıcak   180       40         25          3500
H3     Sıcak   150       60         10          900
C1     Soğuk   30        250        18          3960
C2     Soğuk   60        200        12          1680
─────────────────────────────────────────────────────

Toplam sıcak yük: 2850 + 3500 + 900 = 7250 kW
Toplam soğuk yük: 3960 + 1680 = 5640 kW

Parametreler:
  ΔTmin = 10°C
  Pinch (shifted): 175°C
  Pinch (hot side): 180°C
  Pinch (cold side): 170°C
  QH,min = 1800 kW  (minimum sıcak utility)
  QC,min = 2240 kW  (minimum soğuk utility)
```

---

## 1. Enerji Hedefleme (Energy Targeting)

### 1.1 Problem Tablosu Algoritması (Problem Table Algorithm — PTA)

Enerji hedeflerinin belirlenmesi için Linnhoff & Flower (1978) tarafından geliştirilen Problem Tablosu Algoritması kullanılır. Bu yöntem, Bileşik Eğriler (Composite Curves) üzerinden grafiksel olarak da elde edilebilir, ancak PTA sayısal hassasiyet sağlar.

**Adımlar:**
1. Tüm akış sıcaklıklarını kaydırılmış sıcaklık ölçeğine (shifted temperature scale) çevir
   - Sıcak akışlar: T_shifted = T_actual - ΔTmin/2
   - Soğuk akışlar: T_shifted = T_actual + ΔTmin/2
2. Sıcaklık aralıklarını (temperature intervals) belirle
3. Her aralıktaki net ısı fazlasını/açığını hesapla
4. Isı kaskadını (heat cascade) oluştur
5. Negatif olmayan kaskad elde edilene kadar sıcak utility ekle

**Referans problem için PTA sonuçları:**

```
Kaydırılmış Sıcaklık Aralıkları:
──────────────────────────────────────────────────────────────────
Aralık   T_shifted(°C)   CP_hot   CP_cold   ΔCP      Q_net(kW)
──────────────────────────────────────────────────────────────────
1        265 → 255       15       0         15       150
2        255 → 175       15       18        -3       -240
3        175 → 145       15+25    18+12     0        0
4        145 → 65        15+25    18+12     0        0
         (Not: Bu aralıklarda detaylı CP dengeleri değişir)
──────────────────────────────────────────────────────────────────

Kaskad Sonucu:
  QH,min = 1800 kW
  QC,min = 2240 kW
  Pinch noktası: 175°C (shifted)
```

### 1.2 Enerji-ΔTmin İlişkisi (Energy-ΔTmin Relationship)

ΔTmin değeri değiştikçe enerji hedefleri de değişir. Daha düşük ΔTmin, daha az enerji tüketimi ama daha fazla ısı transfer alanı gerektirir.

```
ΔTmin ve Enerji Hedefleri (Referans Problem):
─────────────────────────────────────────────
ΔTmin(°C)   QH,min(kW)   QC,min(kW)   Enerji Geri Kazanım(kW)
─────────────────────────────────────────────
5           1650         2090         5600
10          1800         2240         5450
15          1960         2400         5290
20          2130         2570         5120
25          2310         2750         4940
30          2500         2940         4750
─────────────────────────────────────────────
```

### 1.3 Duyarlılık Analizi (Sensitivity Analysis)

Enerji hedeflerinin akış verilerine duyarlılığı değerlendirilmelidir:

- **CP değişimi:** ±10% CP değişimi, enerji hedeflerinde ±5-15% değişime neden olabilir
- **Sıcaklık değişimi:** Pinch noktasına yakın sıcaklıklardaki değişimler kritiktir
- **Yeni akış eklenmesi:** Pinch noktasının kaymasına yol açabilir

> **Pratik kural:** Enerji hedefleri ±5-10% doğrulukla gerçek tasarım değerlerini yansıtır (Kemp, 2007).

---

## 2. Alan Hedefleme — Bath Formülü (Area Targeting — Bath Formula)

### 2.1 Temel Kavram

Minimum ısı transfer alanı, eşanjör ağı tasarlanmadan önce hesaplanabilir. Bath Formülü (Townsend & Linnhoff, 1984; Ahmad & Linnhoff, 1988) bu hesaplamayı Bileşik Eğriler üzerindeki enthalpy aralıklarına (enthalpy intervals) bölerek yapar.

### 2.2 Formül

```
                  N_intervals
A_min = Σ         [ 1/ΔT_LM,k × ( Σ q_i/h_i  +  Σ q_j/h_j ) ]
                k=1                  i∈hot          j∈cold

Burada:
  A_min     : Minimum toplam ısı transfer alanı (m²)
  N_intervals: Enthalpy aralık sayısı
  ΔT_LM,k  : k. aralıktaki logaritmik ortalama sıcaklık farkı (°C)
  q_i       : k. aralıkta i. sıcak akışın ısı yükü (kW)
  h_i       : i. sıcak akışın film ısı transfer katsayısı (kW/m²·°C)
  q_j       : k. aralıkta j. soğuk akışın ısı yükü (kW)
  h_j       : j. soğuk akışın film ısı transfer katsayısı (kW/m²·°C)
```

### 2.3 Terimlerin Açıklaması

**ΔT_LM,k — Logaritmik Ortalama Sıcaklık Farkı (Log-Mean Temperature Difference):**

```
ΔT_LM = (ΔT_1 - ΔT_2) / ln(ΔT_1/ΔT_2)

Burada ΔT_1 ve ΔT_2, k. aralığın iki ucundaki sıcak ve soğuk
bileşik eğriler arasındaki sıcaklık farklarıdır.

Özel durum: ΔT_1 = ΔT_2 ise → ΔT_LM = ΔT_1
```

**q_i/h_i — Akışın Alan Katkısı:**

Her akışın bir aralıktaki alan katkısı, o aralıktaki ısı yükünün film ısı transfer katsayısına bölünmesiyle elde edilir. Bu yaklaşım "dikey ısı transferi" (vertical heat transfer) varsayımına dayanır.

### 2.4 Film Isı Transfer Katsayıları Tablosu (Film Heat Transfer Coefficients)

```
Akışkan Tipi                    h (kW/m²·°C)   Tipik Aralık
──────────────────────────────────────────────────────────────
Su (kaynama)                    5.0 - 10.0      Yüksek
Su (yoğuşma)                   5.0 - 10.0      Yüksek
Su (sıvı, türbülanslı)         1.5 - 4.0       Orta-Yüksek
Su (sıvı, laminer)             0.3 - 0.8       Düşük
Buhar (steam, yoğuşma)         6.0 - 12.0      Yüksek
Hafif organik sıvılar          0.5 - 1.5       Orta
Ağır organik sıvılar           0.1 - 0.5       Düşük
Gazlar (düşük basınç)          0.02 - 0.10     Çok düşük
Gazlar (yüksek basınç)         0.10 - 0.50     Düşük-Orta
Termal yağlar (thermal oils)   0.3 - 0.8       Düşük-Orta
Viskoz sıvılar                 0.05 - 0.3      Çok düşük
──────────────────────────────────────────────────────────────
Kaynak: Sinnott & Towler, 2020; Smith, 2016
```

### 2.5 Sayısal Örnek (Referans Problem)

Referans problem için h değerleri şu şekilde varsayılmıştır:

```
Akış   h (kW/m²·°C)
─────────────────────
H1     0.5   (organik sıvı)
H2     1.5   (hafif sıvı)
H3     0.8   (orta viskoziteli sıvı)
C1     1.0   (proses sıvısı)
C2     1.2   (hafif proses sıvısı)
HU     3.0   (buhar, hot utility)
CU     2.0   (soğutma suyu, cold utility)
─────────────────────
```

**Basitleştirilmiş hesaplama (iki aralık varsayımıyla):**

```
Pinch üstü (above pinch):
  Sıcak akışlar: H1 (270→180°C), H2 (180°C, sadece pinch'te)
  Soğuk akışlar: C1 (170→250°C), C2 (170→200°C), HU

  Örnek aralık (250-200°C shifted bölge):
    ΔT_1 = 20°C, ΔT_2 = 15°C (yaklaşık)
    ΔT_LM = (20-15)/ln(20/15) = 5/0.2877 = 17.4°C

    q_H1 = 15 × 50 = 750 kW (H1 bu aralıkta)
    q_C1 = 18 × 50 = 900 kW (C1 bu aralıkta)

    A_k = 1/17.4 × (750/0.5 + 900/1.0)
        = 0.0575 × (1500 + 900)
        = 0.0575 × 2400
        = 138 m²

Pinch altı (below pinch):
  Benzer hesaplama uygulanır.

Toplam tahmini minimum alan:
  A_min ≈ 780 - 950 m² (tüm aralıklar toplanarak)
```

> **Not:** Gerçek Bath Formülü hesaplaması, Bileşik Eğrilerdeki her kırılma noktasına göre çok sayıda aralık oluşturur. Yukarıdaki örnek basitleştirilmiştir. Tam hesaplama için bilgisayar destekli araçlar (HINT, SPRINT, Aspen Energy Analyzer) kullanılmalıdır.

### 2.6 Spagetti Tasarım vs Dikey Hizalama (Spaghetti Design vs Vertical Alignment)

```
Dikey Hizalama (Vertical Heat Transfer):
  ─────────────────────────────────
  Sıcak Bileşik    →  ████████████
                       ↕ ↕ ↕ ↕ ↕ ↕   (dikey ok: minimum alan)
  Soğuk Bileşik    →  ████████████
  ─────────────────────────────────
  - Bileşik eğriler arasında düşey ısı transferi
  - Minimum toplam alan verir
  - Çok sayıda eşanjör gerektirebilir (spaghetti design)

Çapraz Eşleştirme (Criss-Cross Heat Transfer):
  ─────────────────────────────────
  Sıcak Bileşik    →  ████████████
                       ╲ ╱ ╲ ╱ ╲ ╱   (çapraz ok: daha fazla alan)
  Soğuk Bileşik    →  ████████████
  ─────────────────────────────────
  - Sıcaklık sürüş kuvvetini (driving force) düşürür
  - Daha fazla alan gerektirir
  - Daha az eşanjör sayısı mümkün
```

**Spagetti tasarımın dezavantajı:** Minimum alan hedefine ulaşmak için çok sayıda akış bölünmesi (stream splitting) ve eşanjör gerekir. Pratikte %110-120 alan ile daha basit ağlar tercih edilir.

---

## 3. Eşanjör Sayısı Hedefleme (Number of Units Targeting)

### 3.1 Euler Teoremi (Euler's Theorem)

Minimum eşanjör sayısı, ağ topolojisinin graf teorisi ile analiz edilmesine dayanır:

```
U_min = N_streams + N_utilities - N_subnetworks

Burada:
  U_min          : Minimum eşanjör (unit) sayısı
  N_streams      : Proses akışı sayısı
  N_utilities    : Utility akışı sayısı
  N_subnetworks  : Bağımsız alt ağ sayısı (genellikle 1)
```

### 3.2 Bütünleşik Ağ (Overall Network — Merged)

Pinch bölünmesi yapılmadığında, tüm sistem tek bir alt ağ olarak ele alınır:

```
Referans Problem (bütünleşik):
  N_streams   = 5  (H1, H2, H3, C1, C2)
  N_utilities = 2  (Hot Utility, Cold Utility)
  N_subnetworks = 1

  U_min,merged = 5 + 2 - 1 = 6 eşanjör
```

### 3.3 Pinch-Bölünmüş Ağ (Pinch-Subdivided Network)

Pinch noktasında ağ ikiye bölündüğünde, her alt ağ için ayrı hesaplama yapılır ve sonuçlar toplanır:

```
Pinch Üstü (Above Pinch):
  Aktif sıcak akışlar: H1 (270→180°C)
  Aktif soğuk akışlar: C1 (170→250°C), C2 (170→200°C)
  Utility: Hot Utility (HU)
  N_subnetworks = 1

  U_above = N_hot + N_cold + N_utility - N_sub
          = 1 + 2 + 1 - 1
          = 3 eşanjör

Pinch Altı (Below Pinch):
  Aktif sıcak akışlar: H1 (180→80°C), H2 (180→40°C), H3 (150→60°C)
  Aktif soğuk akışlar: C1 (30→170°C), C2 (60→170°C)
  Utility: Cold Utility (CU)
  N_subnetworks = 1

  U_below = N_hot + N_cold + N_utility - N_sub
          = 3 + 2 + 1 - 1
          = 5 eşanjör

Toplam:
  U_min,pinch = U_above + U_below = 3 + 5 = 8 eşanjör
```

### 3.4 Karşılaştırma

```
────────────────────────────────────────────────────────────
Yöntem              U_min   Enerji Hedefi   Açıklama
────────────────────────────────────────────────────────────
Bütünleşik (merged)   6    Karşılanmaz     Daha az eşanjör ama
                                           pinch ihlali olabilir
Pinch-bölünmüş         8    QH,min=1800 kW  Enerji hedefini
                            QC,min=2240 kW  garanti eder
────────────────────────────────────────────────────────────
Fark: 8 - 6 = 2 ek eşanjör (enerji optimizasyonu maliyeti)
```

> **Tasarım kararı:** Ek 2 eşanjör, enerji tasarrufu ile ödenebiliyorsa pinch-bölünmüş ağ tercih edilir. Bu karar, maliyet hedefleme ile doğrulanır.

---

## 4. Maliyet Hedefleme (Cost Targeting)

### 4.1 Yatırım Maliyeti (Capital Cost — CC)

Isı eşanjörü kurulu maliyeti genellikle alan bazlı bir üs fonksiyonu (power-law) ile modellenir:

```
CC = a + b × A^c

Burada:
  CC  : Eşanjör kurulu maliyeti ($/birim veya TL/birim)
  A   : Isı transfer alanı (m²)
  a   : Sabit maliyet bileşeni (kurulum, boru bağlantıları vb.)
  b   : Alan bazlı maliyet katsayısı
  c   : Alan üssü (genellikle 0.6 - 1.0 arasında)

Tipik değerler (karbon çelik, shell-and-tube):
  a = 16,000 $
  b = 3,200 $/m^(0.7)
  c = 0.7
```

**Toplam yatırım maliyeti:**

```
CC_total = U × (a + b × (A_total/U)^c)

Burada U, eşanjör sayısıdır. Toplam alan eşanjörlere
eşit şekilde bölündüğü varsayılır (basitleştirme).
```

### 4.2 Enerji Maliyeti (Energy Cost — EC)

```
EC = QH,min × c_H + QC,min × c_C

Burada:
  c_H : Sıcak utility birim maliyeti ($/kW·yıl)
  c_C : Soğuk utility birim maliyeti ($/kW·yıl)

Tipik değerler:
  Buhar (steam, 10 bar):   c_H = 120 $/kW·yıl
  Soğutma suyu:            c_C = 10 $/kW·yıl
```

**Referans problem için:**

```
EC = 1800 × 120 + 2240 × 10
   = 216,000 + 22,400
   = 238,400 $/yıl
```

### 4.3 Toplam Yıllık Maliyet (Total Annual Cost — TAC)

```
TAC = CC_annualized + EC

CC_annualized = CC_total × AF

AF (Annuity Factor) = i × (1+i)^n / ((1+i)^n - 1)

Burada:
  i : Yıllık faiz oranı (discount rate)
  n : Ekonomik ömür (yıl)

Örnek: i = 10%, n = 5 yıl
  AF = 0.10 × (1.10)^5 / ((1.10)^5 - 1)
     = 0.10 × 1.6105 / 0.6105
     = 0.2638
```

### 4.4 Referans Problem — Maliyet Hesabı

```
Varsayımlar:
  a = 16,000 $, b = 3,200, c = 0.7
  U = 8 (pinch-bölünmüş)
  A_total = 900 m² (Bath formülü tahmini)
  AF = 0.2638

Yatırım maliyeti:
  CC_total = 8 × (16,000 + 3,200 × (900/8)^0.7)
           = 8 × (16,000 + 3,200 × (112.5)^0.7)
           = 8 × (16,000 + 3,200 × 36.3)
           = 8 × (16,000 + 116,160)
           = 8 × 132,160
           = 1,057,280 $

Yıllık yatırım maliyeti:
  CC_annualized = 1,057,280 × 0.2638 = 278,910 $/yıl

Enerji maliyeti:
  EC = 238,400 $/yıl

Toplam Yıllık Maliyet:
  TAC = 278,910 + 238,400 = 517,310 $/yıl
```

---

## 5. Süperhedefleme (Supertargeting)

### 5.1 Temel Kavram

Süperhedefleme, ΔTmin'i bağımsız değişken olarak kullanarak TAC'ı minimize eden optimum ΔTmin değerini belirler (Ahmad & Linnhoff, 1990). Bu yöntem, tasarım öncesi aşamada en iyi enerji-alan dengesini bulur.

```
  TAC ($)
  │
  │     ╲  CC (yatırım)
  │      ╲
  │       ╲        ╱ EC (enerji)
  │        ╲      ╱
  │         ╲    ╱
  │          ╲  ╱
  │           ╳ ← Optimum ΔTmin
  │          ╱ ╲
  │         ╱   ╲
  │   TAC  ╱     ╲
  │       ╱       ╲
  │──────╱─────────╲────────
  └──────────────────────── ΔTmin (°C)
        ΔTmin,opt
```

### 5.2 TAC vs ΔTmin Tablosu (Referans Problem)

```
─────────────────────────────────────────────────────────────────
ΔTmin  QH,min  QC,min  A_min   CC_ann    EC       TAC
(°C)   (kW)    (kW)    (m²)    ($/yıl)   ($/yıl)  ($/yıl)
─────────────────────────────────────────────────────────────────
5      1650    2090    1520    412,800   220,900  633,700
8      1740    2180    1080    325,600   231,600  557,200
10     1800    2240    900     278,910   238,400  517,310  ←
12     1870    2310    780     251,300   247,500  498,800
15     1960    2400    650     220,400   257,600  478,000  ←*
18     2060    2500    560     198,700   272,200  470,900  ←**
20     2130    2570    510     186,200   278,100  464,300  ←**
22     2210    2650    470     175,800   287,600  463,400  ←OPT
25     2310    2750    420     163,500   299,600  463,100  ←OPT
28     2420    2860    380     152,800   313,400  466,200
30     2500    2940    360     146,300   322,400  468,700
35     2700    3140    310     131,600   347,400  479,000
40     2910    3350    270     119,100   372,100  491,200
─────────────────────────────────────────────────────────────────
(* Yaklaşık değerler, tam hesap yazılım gerektirir)
Optimum bölge: ΔTmin ≈ 22-25°C → TAC ≈ 463,000 $/yıl
```

### 5.3 Maliyet Parametrelerine Duyarlılık (Sensitivity to Cost Parameters)

Optimum ΔTmin, maliyet parametrelerine güçlü biçimde bağlıdır:

```
────────────────────────────────────────────────────
Senaryo                          ΔTmin,opt (°C)
────────────────────────────────────────────────────
Yüksek enerji maliyeti           Düşük (5-15°C)
  (pahalı buhar, karbon vergisi)

Düşük enerji maliyeti            Yüksek (20-40°C)
  (ucuz doğalgaz, sübvansiyon)

Yüksek yatırım maliyeti          Yüksek (20-35°C)
  (egzotik malzeme, yüksek basınç)

Düşük yatırım maliyeti           Düşük (5-15°C)
  (karbon çelik, standart tasarım)

Kısa geri ödeme süresi           Yüksek (25-40°C)
  (n=2-3 yıl, yüksek AF)

Uzun geri ödeme süresi            Düşük (8-15°C)
  (n=10-15 yıl, düşük AF)
────────────────────────────────────────────────────
```

### 5.4 Süperhedefleme Hassasiyeti

TAC eğrisi genellikle optimum bölgede oldukça düz (flat) bir profil gösterir. Bu durum, geniş bir ΔTmin aralığının benzer maliyetler verdiğini gösterir ve tasarımcıya esneklik sağlar.

```
TAC eğrisi profili:

  ΔTmin = 15-30°C aralığında TAC değişimi: ±3-5%
  ΔTmin = 5-40°C  aralığında TAC değişimi: ±15-25%

Sonuç: ΔTmin seçiminde ±5°C'lik sapma kabul edilebilir.
```

---

## 6. Emisyon Hedefleme (Emissions Targeting)

### 6.1 Enerji Hedeflerinden CO2 Azaltımı

Enerji hedefleme ile belirlenen QH,min, doğrudan CO2 emisyon azaltım potansiyelini gösterir:

```
CO2_azaltım = (QH,mevcut - QH,min) / η_kazan × EF × t_çalışma

Burada:
  QH,mevcut   : Mevcut sıcak utility tüketimi (kW)
  QH,min      : Hedeflenen minimum sıcak utility (kW)
  η_kazan     : Kazan verimi (tipik 0.85-0.92)
  EF          : Emisyon faktörü (kg CO2/kWh yakıt)
  t_çalışma   : Yıllık çalışma süresi (saat)
```

### 6.2 Yakıta Göre Emisyon Faktörleri (Fuel-Specific Emission Factors)

```
──────────────────────────────────────────────────
Yakıt Tipi              EF (kg CO2/kWh)
──────────────────────────────────────────────────
Doğalgaz                0.202
LPG                     0.227
Fuel oil (No.6)         0.279
Kömür (bituminous)      0.341
Kömür (lignite)         0.364
Biyokütle (odun peleti) 0.039 (net, yaşam döngüsü)
Elektrik (Türkiye grid) 0.440 (2024 ortalaması)
──────────────────────────────────────────────────
Kaynak: IPCC 2006, TEİAŞ 2024
```

### 6.3 Referans Problem — Emisyon Hedefi

```
Varsayımlar:
  Mevcut QH = 3200 kW (hedefleme yapılmadan önce)
  QH,min = 1800 kW
  Tasarruf = 3200 - 1800 = 1400 kW
  Yakıt: Doğalgaz, η_kazan = 0.90
  Çalışma: 8000 saat/yıl

  CO2_azaltım = 1400 / 0.90 × 0.202 × 8000
              = 1555.6 × 0.202 × 8000
              = 2,513,600 kg/yıl
              ≈ 2,514 ton CO2/yıl
```

---

## 7. Hedefleme Doğruluğu (Targeting Accuracy)

### 7.1 Tasarım Öncesi Doğruluk (Pre-Design Accuracy)

Hedefleme teknikleri, detaylı tasarım yapılmadan "iyi" tahminler sağlar. Ancak doğruluk, hedef türüne göre farklılık gösterir:

```
──────────────────────────────────────────────────────────────
Hedef Türü          Tipik Doğruluk    Açıklama
──────────────────────────────────────────────────────────────
Enerji (QH,min)     ±5-10%           En güvenilir hedef.
                                     PTA matematiksel olarak kesindir.
                                     Sapma, veri kalitesinden kaynaklanır.

Alan (A_min)        ±20-30%          Bath formülü alt sınır verir.
                                     Gerçek ağ bölünmeler nedeniyle
                                     daha fazla alan gerektirir.

Eşanjör sayısı (U)  Alt sınır        Euler hedefi minimum değerdir.
                                     Pratikte akış bölünmeleri
                                     nedeniyle daha fazla olabilir.

Maliyet (TAC)       ±20-40%          Birim maliyet parametrelerine
                                     (a, b, c) hassastır.
                                     Ön fizibilite düzeyinde geçerlidir.
──────────────────────────────────────────────────────────────
```

### 7.2 Doğruluğu Etkileyen Faktörler

1. **Veri kalitesi:** Akış debileri, sıcaklıklar ve CP değerlerindeki belirsizlik
2. **Fouling faktörleri:** Kirlenme dirençleri hesaba katılmadığında alan hedefi düşük kalır
3. **Basınç düşümü kısıtları:** Gerçek tasarımda basınç düşümü alan artışına neden olur
4. **Malzeme seçimi:** Korozyon, sıcaklık ve basınç kısıtları ek maliyet getirir
5. **Pratik kısıtlamalar:** Minimum eşanjör boyutu, standart boyutlar, yerleşim kısıtları

---

## 8. Hedefleme vs Gerçek Tasarım (Targets vs Actual Design)

### 8.1 Hedef ve Gerçek Arasındaki Fark (Gap Analysis)

Hedef değerler her zaman ideal alt sınırları temsil eder. Gerçek tasarımda bu hedeflere tam olarak ulaşmak genellikle mümkün değildir:

```
──────────────────────────────────────────────────────────────────
Parametre           Hedef       Tipik Gerçek     Fark Nedeni
──────────────────────────────────────────────────────────────────
Enerji (QH)         1800 kW     1850-1980 kW     Pinch yakınında
                                (103-110%)        eşleşme zorlukları,
                                                  kontrol gereksinimleri

Enerji geri kazanım 5450 kW     5200-5400 kW     Bazı eşleşmelerin
                                (95-99%)          pratikte uygulanamaz
                                                  olması

Alan (A)            900 m²      990-1080 m²      Akış bölünmelerinin
                                (110-120%)        sınırlı tutulması,
                                                  standart boyutlar

Eşanjör sayısı (U)  8           8-10             Ek bölünmeler
                                (100-125%)        ve bypass hatları

Maliyet (TAC)       463,100 $   500,000-550,000$ Yukarıdaki tüm
                                (108-119%)        faktörlerin toplamı
──────────────────────────────────────────────────────────────────
```

### 8.2 Gerçek Tasarımda Tipik Başarı Oranları

- **Enerji hedefinin %90-95'i** genellikle ulaşılabilir bir tasarımla elde edilir
- **Alan hedefinin %110-120'si** gerçekçi bir tahmindir
- **Eşanjör sayısı** hedefin %100-125'i arasında kalır
- **TAC**, hedefin %105-120'si olarak gerçekleşir

### 8.3 Hedef-Tasarım Boşluğunu Azaltma Stratejileri

```
Strateji                         Beklenen İyileşme
──────────────────────────────────────────────────────
Akış bölünmesi (stream split)    Enerji hedefine daha yakın
Çoklu utility seviyesi           Alan optimizasyonu
Seri-paralel düzenleme           Eşanjör sayısı azaltma
Esnek ΔTmin (farklı eşanjörler)  Maliyet optimizasyonu
Retrofit yaklaşımı               Mevcut ağ üzerinde iyileştirme
──────────────────────────────────────────────────────
```

---

## Özet Tablosu — Tüm Hedefler (Referans Problem)

```
═══════════════════════════════════════════════════════════════
Hedef Türü              Değer           Birim
═══════════════════════════════════════════════════════════════
QH,min                  1,800           kW
QC,min                  2,240           kW
Enerji geri kazanım     5,450           kW
A_min (Bath)            ~900            m²
U_min (pinch-bölünmüş)  8              adet
U_min (bütünleşik)       6              adet
CC_annualized           ~278,910        $/yıl
EC                      238,400         $/yıl
TAC                     ~517,310        $/yıl
Optimum ΔTmin           22-25           °C
TAC (optimum)           ~463,100        $/yıl
CO2 azaltım potansiyeli ~2,514          ton/yıl
═══════════════════════════════════════════════════════════════
```

---

## İlgili Dosyalar

- `factory/pinch/fundamentals.md` — Pinch analizinin temel kavramları
- `factory/pinch/composite_curves.md` — Bileşik eğriler ve Grand Composite Curve
- `factory/pinch/delta_t_min.md` — ΔTmin seçimi ve etkileri
- `factory/pinch/cost_estimation.md` — Detaylı maliyet tahmin yöntemleri

## Referanslar

1. **Linnhoff, B. & Flower, J.R.** (1978). "Synthesis of heat exchanger networks." *AIChE Journal*, 24(4), 633-642.
2. **Linnhoff, B. & Ahmad, S.** (1990). "Cost optimum heat exchanger networks — 1. Minimum energy and capital using simple models for capital cost." *Computers & Chemical Engineering*, 14(7), 729-750.
3. **Linnhoff, B.** (1994). "Use pinch analysis to knock down capital costs and emissions." *Chemical Engineering Progress*, 90(8), 32-57.
4. **Kemp, I.C.** (2007). *Pinch Analysis and Process Integration*, 2nd ed. Butterworth-Heinemann.
5. **Smith, R.** (2016). *Chemical Process Design and Integration*, 2nd ed. Wiley.
6. **Klemes, J.J.** (Ed.) (2013). *Handbook of Process Integration*. Woodhead Publishing.
7. **Ahmad, S. & Linnhoff, B.** (1988). "Overall cost targets for heat exchanger networks." *IChemE Annual Research Meeting*, Bath, UK.
8. **Townsend, D.W. & Linnhoff, B.** (1984). "Surface area targets for heat exchanger networks." *IChemE Annual Research Meeting*.
9. **Sinnott, R.K. & Towler, G.** (2020). *Chemical Engineering Design*, 6th ed. Butterworth-Heinemann.
