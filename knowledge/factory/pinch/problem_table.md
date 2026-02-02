---
title: "Problem Tablosu Algoritması (Problem Table Algorithm — PTA)"
category: factory
equipment_type: factory
keywords: [problem tablosu, PTA, sıcaklık kaydırma, ısı kaskadı, pinch noktası, minimum enerji hedefleri, Linnhoff, bileşik eğri, ısı entegrasyonu, kaskad diyagramı, düzeltilmiş kaskad]
related_files: [factory/pinch/INDEX.md, factory/pinch/composite_curves.md, factory/pinch/fundamentals.md, factory/pinch/grand_composite.md, factory/pinch/targeting.md, factory/pinch/hen_design.md, factory/pinch/delta_t_min.md]
use_when: ["PTA ile minimum enerji hedeflerini hesaplarken", "Pinch noktasını cebirsel yöntemle belirlerken", "Isı kaskadı oluştururken", "Bileşik eğrilerin sayısal doğrulaması yapılırken", "Grand Composite Curve için ara sonuçlar gerektiğinde"]
priority: high
last_updated: 2026-02-01
---

# Problem Tablosu Algoritması (Problem Table Algorithm — PTA)

> Son güncelleme: 2026-02-01

## Genel Bakış

Problem Tablosu Algoritması (PTA), Linnhoff ve Flower (1978) tarafından geliştirilen ve bir prosesin minimum sıcak utility ihtiyacını (QH,min), minimum soğuk utility ihtiyacını (QC,min) ve pinch noktası sıcaklığını cebirsel olarak belirleyen temel pinch analizi aracıdır. Bileşik eğrilerin (composite curves) grafik yöntemiyle elde edilen sonuçları sayısal hassasiyetle doğrulayan ve bilgisayar implementasyonuna uygun olan bu algoritma, endüstriyel ölçekte ısı entegrasyonu projelerinin vazgeçilmez hesaplama adımıdır.

Grafik yöntemler (bileşik eğri çizimi) görsel olarak güçlü olmakla birlikte, akış sayısı arttığında hassasiyet kaybına uğrar ve elle çizimde okuma hataları oluşur. PTA bu sorunu ortadan kaldırarak, herhangi bir akış sayısı için kesin sonuçlar verir. Ayrıca algoritmanın yapılandırılmış doğası, yazılım implementasyonunu ve otomasyonu kolaylaştırır.

### PTA'nın Bileşik Eğrilerle İlişkisi

Bileşik eğriler, sıcak ve soğuk akışların birleştirilmiş sıcaklık-entalpi profillerini grafik olarak gösterir. PTA ise aynı bilgiyi cebirsel olarak işler:

```
Bileşik Eğriler (Grafik)       ←→     PTA (Cebirsel)
───────────────────────────            ──────────────────
Eğriler arası minimum mesafe    =  ΔTmin (tasarım parametresi)
Eğrilerin üst üste binme alanı  =  İç ısı geri kazanımı (heat recovery)
Sol taraftaki boşluk             =  QH,min (sıcak utility ihtiyacı)
Sağ taraftaki boşluk             =  QC,min (soğuk utility ihtiyacı)
Eğrilerin en yakın noktası       =  Pinch noktası
```

PTA, bileşik eğrilerin veremediği ek bilgiyi de sağlar: her sıcaklık aralığındaki net ısı fazlası veya açığı. Bu bilgi, Grand Composite Curve (GCC) oluşturmanın ve utility yerleştirmenin temelini oluşturur.

## 1. Problem Tablosu Algoritması Genel Bakış (PTA Overview)

### 1.1 PTA'nın Gerekliliği (Why PTA is Needed)

Grafik yöntemlerin sınırlamaları PTA'yı zorunlu kılar:

1. **Hassasiyet sorunu:** Bileşik eğrilerin elle çiziminde okuma hatası kaçınılmazdır. 5-6 akışlık bir problemde bile QH,min ve QC,min değerlerinde %5-10 hata oluşabilir.

2. **Ölçekleme sorunu:** 20+ akışlı endüstriyel problemlerde bileşik eğrilerin elle çizimi pratik değildir. PTA, akış sayısından bağımsız olarak sistematik çözüm sunar.

3. **Otomasyon ihtiyacı:** Bilgisayar tabanlı çözümlerde cebirsel algoritma gereklidir. PTA, doğrudan kodlanabilir bir yapıya sahiptir.

4. **GCC oluşturma:** Grand Composite Curve, ancak PTA'nın ara sonuçlarından (düzeltilmiş kaskad değerleri) elde edilebilir.

5. **Çoklu senaryo analizi:** ΔTmin değişiminin etkisini hızla değerlendirmek için PTA tekrarlanabilir yapısıyla idealdir. Süperhedefleme (supertargeting) çalışmaları PTA'ya dayanır.

6. **Eğitim değeri:** PTA, ısı kaskadı kavramını somutlaştırarak pinch analizinin termodinamik temellerini anlamayı kolaylaştırır.

### 1.2 Algoritma Adımları (Algorithm Steps)

PTA altı temel adımdan oluşur:

```
Adım 1: Sıcaklık Kaydırma (Temperature Shifting)
         Sıcak akışlar ΔTmin/2 aşağı, soğuk akışlar ΔTmin/2 yukarı kaydırılır

Adım 2: Sıcaklık Aralıklarının Belirlenmesi (Temperature Interval Definition)
         Kaydırılmış sıcaklıklar büyükten küçüğe sıralanarak aralıklar oluşturulur

Adım 3: Aktif Akışların Belirlenmesi (Active Stream Identification)
         Her aralıkta hangi akışların mevcut olduğu tespit edilir

Adım 4: Net Isı Dengesi Hesabı (Net Heat Balance)
         Her aralıkta ΔH = (ΣCP_hot - ΣCP_cold) × ΔT hesaplanır

Adım 5: Başlangıç Isı Kaskadı (Initial Heat Cascade)
         R₀ = 0 başlangıcıyla kaskad oluşturulur, negatif değerler tespit edilir

Adım 6: Düzeltilmiş Kaskad (Corrected Cascade)
         En negatif değer kadar sıcak utility eklenerek QH,min, QC,min ve
         pinch noktası belirlenir
```

### 1.3 Referans Problem (Reference Problem)

Bu dosya boyunca kullanılan 5-akışlı referans problem:

| Akış | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Q [kW] |
|------|-----|---------------|--------------|-------------|---------|
| H1 | Sıcak | 270 | 80 | 15 | 2,850 |
| H2 | Sıcak | 180 | 40 | 25 | 3,500 |
| H3 | Sıcak | 150 | 60 | 10 | 900 |
| C1 | Soğuk | 30 | 250 | 18 | 3,960 |
| C2 | Soğuk | 60 | 200 | 12 | 1,680 |

```
ΔTmin = 10°C

Toplam ısı yükleri:
  ΣQ_hot = 2,850 + 3,500 + 900 = 7,250 kW
  ΣQ_cold = 3,960 + 1,680 = 5,640 kW
  Net fark = ΣQ_hot - ΣQ_cold = 1,610 kW

PTA sonuçları:
  QH,min  = 450 kW
  QC,min  = 2,060 kW
  Pinch   = 175°C (shifted) / 180°C (hot) / 170°C (cold)

Doğrulama: QC,min - QH,min = 2,060 - 450 = 1,610 kW = ΣQ_hot - ΣQ_cold ✓
```

> **Not:** INDEX.md'deki genel referans değerler (QH,min = 1,800 kW, QC,min = 2,240 kW) farklı bir CP konfigürasyonuna aittir. Bu dosyada yukarıdaki akış verileri ile tam tutarlı hesaplama sunulmaktadır. Pinch noktası sıcaklığı (175°C shifted / 180°C hot / 170°C cold) her iki durumda da aynıdır.

## 2. Sıcaklık Kaydırma (Temperature Shifting)

### 2.1 Kaydırma Kuralı (Shifting Rule)

Sıcaklık kaydırma, farklı türdeki akışların (sıcak ve soğuk) aynı sıcaklık ölçeğinde karşılaştırılabilmesini sağlayan temel PTA adımıdır. Simetrik kaydırma kuralı:

```
Sıcak akışlar:  T_shifted = T_actual - ΔTmin/2
Soğuk akışlar:  T_shifted = T_actual + ΔTmin/2
```

ΔTmin = 10°C olduğunda kaydırma miktarı her yön için 5°C'dir.

### 2.2 Kaydırmanın Fiziksel Anlamı (Physical Meaning of Shifting)

Kaydırma, ısı transferi fizibilitesini garanti eden bir matematik dönüşümdür. Kaydırılmış sıcaklık ölçeğinde aynı seviyedeki bir sıcak ve soğuk akış arasında tam olarak ΔTmin sıcaklık farkı vardır:

```
Eğer T_hot_shifted = T_cold_shifted ise:
  T_hot_actual   = T_shifted + ΔTmin/2
  T_cold_actual  = T_shifted - ΔTmin/2
  ΔT_actual      = T_hot_actual - T_cold_actual = ΔTmin

Sonuç olarak kaydırılmış ölçekte:
  T_hot_shifted > T_cold_shifted  → ΔT > ΔTmin → kesinlikle fizibl ✓
  T_hot_shifted = T_cold_shifted  → ΔT = ΔTmin → sınırda fizibl ✓
  T_hot_shifted < T_cold_shifted  → ΔT < ΔTmin → fizibl DEĞİL ✗
```

Bu sayede kaydırılmış sıcaklık ölçeğinde, aynı aralıktaki sıcak akıştan soğuk akışa ısı transferi termodinamik olarak her zaman mümkündür. Kaskad hesabı bu özelliğe dayanır.

### 2.3 Sayısal Hesaplama (Numerical Calculation)

Her akış için kaydırılmış sıcaklık değerleri (ΔTmin/2 = 5°C):

**Sıcak akışlar (T_shifted = T_actual - 5°C):**

| Akış | T_kaynak [°C] | T_hedef [°C] | T_kaynak_shifted [°C] | T_hedef_shifted [°C] | CP [kW/°C] |
|------|---------------|--------------|----------------------|---------------------|-------------|
| H1 | 270 | 80 | **265** | **75** | 15 |
| H2 | 180 | 40 | **175** | **35** | 25 |
| H3 | 150 | 60 | **145** | **55** | 10 |

```
H1: 270 - 5 = 265°C → 80 - 5 = 75°C   (ΔT_shifted = 190°C)
H2: 180 - 5 = 175°C → 40 - 5 = 35°C   (ΔT_shifted = 140°C)
H3: 150 - 5 = 145°C → 60 - 5 = 55°C   (ΔT_shifted = 90°C)
```

**Soğuk akışlar (T_shifted = T_actual + 5°C):**

| Akış | T_kaynak [°C] | T_hedef [°C] | T_kaynak_shifted [°C] | T_hedef_shifted [°C] | CP [kW/°C] |
|------|---------------|--------------|----------------------|---------------------|-------------|
| C1 | 30 | 250 | **35** | **255** | 18 |
| C2 | 60 | 200 | **65** | **205** | 12 |

```
C1: 30 + 5 = 35°C → 250 + 5 = 255°C   (ΔT_shifted = 220°C)
C2: 60 + 5 = 65°C → 200 + 5 = 205°C   (ΔT_shifted = 140°C)
```

### 2.4 Kaydırma Doğrulaması (Shifting Verification)

Kaydırma sonrası akış ısı yükleri değişmemelidir:

```
H1: CP × ΔT_shifted = 15 × (265 - 75)  = 15 × 190 = 2,850 kW ✓
H2: CP × ΔT_shifted = 25 × (175 - 35)  = 25 × 140 = 3,500 kW ✓
H3: CP × ΔT_shifted = 10 × (145 - 55)  = 10 × 90  = 900 kW   ✓
C1: CP × ΔT_shifted = 18 × (255 - 35)  = 18 × 220 = 3,960 kW ✓
C2: CP × ΔT_shifted = 12 × (205 - 65)  = 12 × 140 = 1,680 kW ✓
```

Fizibilite kontrol örneği:

```
H2 ve C2 pinch bölgesinde:
  H2 shifted @ 175°C → H2 actual = 175 + 5 = 180°C
  C2 shifted @ 175°C → C2 actual = 175 - 5 = 170°C
  ΔT_actual = 180 - 170 = 10°C = ΔTmin ✓ (sınırda fizibl)
```

## 3. Sıcaklık Aralıklarının Belirlenmesi (Temperature Interval Definition)

### 3.1 Kaydırılmış Sıcaklıkların Sıralanması (Sorting Shifted Temperatures)

Tüm kaydırılmış sıcaklık değerleri (kaynak ve hedef) tek bir kümede toplanır ve büyükten küçüğe sıralanır. Tekrarlayan değerler yalnızca bir kez yazılır:

```
H1: 265, 75
H2: 175, 35
H3: 145, 55
C1: 35, 255
C2: 65, 205

Tekil değerler kümesi: {265, 255, 205, 175, 145, 75, 65, 55, 35}

Azalan sırada: 265 → 255 → 205 → 175 → 145 → 75 → 65 → 55 → 35
```

Not: 35°C hem H2'nin kaydırılmış hedef sıcaklığı hem de C1'in kaydırılmış kaynak sıcaklığıdır. Tekrarlayan değerler bir kez yazılır; aralık sınırları etkilenmez.

### 3.2 Sıcaklık Aralıkları (Temperature Intervals)

Ardışık kaydırılmış sıcaklıklar arasında N-1 adet aralık tanımlanır (N = tekil sıcaklık sayısı):

| Aralık k | T_üst [°C] | T_alt [°C] | ΔT_k [°C] |
|----------|-----------|-----------|-----------|
| 1 | 265 | 255 | 10 |
| 2 | 255 | 205 | 50 |
| 3 | 205 | 175 | 30 |
| 4 | 175 | 145 | 30 |
| 5 | 145 | 75 | 70 |
| 6 | 75 | 65 | 10 |
| 7 | 65 | 55 | 10 |
| 8 | 55 | 35 | 20 |

Toplam 9 tekil sıcaklık, 8 sıcaklık aralığı oluşturmuştur.

### 3.3 Aktif Akışların Belirlenmesi (Identifying Active Streams)

Bir akış, kaydırılmış sıcaklık aralığını tamamen kapsıyorsa o aralıkta aktiftir. Sınır koşulları:

```
Sıcak akış aktiflik kuralı:
  T_kaynak_shifted >= T_üst  VE  T_hedef_shifted <= T_alt

Soğuk akış aktiflik kuralı:
  T_hedef_shifted >= T_üst  VE  T_kaynak_shifted <= T_alt

ÖNEMLİ: Sınır değerleri dahildir (>=, <=). Bir akışın kaydırılmış
sıcaklığı aralık sınırına tam olarak eşitse, o akış o aralıkta aktiftir.
```

Her aralık için aktiflik tablosu:

| Aralık | T_üst–T_alt | H1 (265–75) | H2 (175–35) | H3 (145–55) | C1 (35–255) | C2 (65–205) |
|--------|-------------|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| 1 | 265–255 | Aktif | — | — | — | — |
| 2 | 255–205 | Aktif | — | — | Aktif | — |
| 3 | 205–175 | Aktif | — | — | Aktif | Aktif |
| 4 | 175–145 | Aktif | Aktif | — | Aktif | Aktif |
| 5 | 145–75 | Aktif | Aktif | Aktif | Aktif | Aktif |
| 6 | 75–65 | — | Aktif | Aktif | Aktif | Aktif |
| 7 | 65–55 | — | Aktif | Aktif | Aktif | — |
| 8 | 55–35 | — | Aktif | — | Aktif | — |

Aktiflik sınır kontrolü detayları:

```
Aralık 1 (265-255):
  C1: T_hedef_shifted = 255 >= T_üst = 265? → 255 >= 265? HAYIR → Aktif DEĞİL
  (C1 bu aralığın üst sınırına ulaşmaz)

Aralık 2 (255-205):
  C1: 255 >= 255? EVET ve 35 <= 205? EVET → Aktif
  C2: T_hedef_shifted = 205 >= T_üst = 255? → 205 >= 255? HAYIR → Aktif DEĞİL

Aralık 3 (205-175):
  C2: 205 >= 205? EVET ve 65 <= 175? EVET → Aktif (sınır dahil)

Aralık 4 (175-145):
  H2: T_kaynak_shifted = 175 >= T_üst = 175? EVET → Aktif (sınır dahil)
  H3: T_kaynak_shifted = 145 >= T_üst = 175? HAYIR → Aktif DEĞİL

Aralık 7 (65-55):
  C2: T_kaynak_shifted = 65 <= T_alt = 55? HAYIR → Aktif DEĞİL
  (C2 bu aralığın alt sınırının altında başlamaz)
```

### 3.4 Kapsama Doğrulaması (Coverage Verification)

Her akışın toplam kapsama alanı, orijinal ısı yükünü vermelidir:

```
H1: Aralık 1-5 → ΔT = 10 + 50 + 30 + 30 + 70 = 190°C
     Q = 15 × 190 = 2,850 kW ✓ (beklenen: 2,850 kW)

H2: Aralık 4-8 → ΔT = 30 + 70 + 10 + 10 + 20 = 140°C
     Q = 25 × 140 = 3,500 kW ✓ (beklenen: 3,500 kW)

H3: Aralık 5-7 → ΔT = 70 + 10 + 10 = 90°C
     Q = 10 × 90 = 900 kW ✓ (beklenen: 900 kW)

C1: Aralık 2-8 → ΔT = 50 + 30 + 30 + 70 + 10 + 10 + 20 = 220°C
     Q = 18 × 220 = 3,960 kW ✓ (beklenen: 3,960 kW)

C2: Aralık 3-6 → ΔT = 30 + 30 + 70 + 10 = 140°C
     Q = 12 × 140 = 1,680 kW ✓ (beklenen: 1,680 kW)
```

Bu doğrulama, aktif akış atamasının doğruluğunu kanıtlar. Herhangi bir akışın kapsama toplamı beklenen ısı yüküne eşit değilse, sınır koşulu hatası vardır.

## 4. Net Isı Dengesi Hesabı (Net Heat Balance Calculation)

### 4.1 Formül (Formula)

Her sıcaklık aralığındaki net ısı dengesi:

```
ΔH_k = (ΣCP_hot,k - ΣCP_cold,k) × ΔT_k    [kW]

Burada:
  ΣCP_hot,k  = k. aralıkta aktif sıcak akışların CP toplamı [kW/°C]
  ΣCP_cold,k = k. aralıkta aktif soğuk akışların CP toplamı [kW/°C]
  ΔT_k       = k. aralığın sıcaklık farkı [°C]

İşaret kuralı (sign convention):
  ΔH_k > 0 → Isı fazlası (heat surplus) — sıcak akışlar baskın
  ΔH_k < 0 → Isı açığı (heat deficit) — soğuk akışlar baskın
  ΔH_k = 0 → Dengeli aralık
```

Isı fazlası olan bir aralıkta, fazla ısı termodinamiğin ikinci yasasına uygun olarak bir alt aralığa aktarılabilir (kaskad prensibi). Isı açığı olan bir aralık ise ya üst aralıktan ısı almalı ya da dış sıcak utility kullanmalıdır.

### 4.2 CP Toplamları ve Net Denge Tablosu (CP Sums and Net Balance Table)

| Aralık | T_üst–T_alt [°C] | ΔT [°C] | Sıcak akışlar | Soğuk akışlar | ΣCP_H [kW/°C] | ΣCP_C [kW/°C] | ΣCP_H - ΣCP_C | ΔH_k [kW] |
|--------|------------------|---------|----------------|---------------|------|------|--------|---------|
| 1 | 265–255 | 10 | H1 | — | 15 | 0 | +15 | **+150** |
| 2 | 255–205 | 50 | H1 | C1 | 15 | 18 | -3 | **-150** |
| 3 | 205–175 | 30 | H1 | C1, C2 | 15 | 30 | -15 | **-450** |
| 4 | 175–145 | 30 | H1, H2 | C1, C2 | 40 | 30 | +10 | **+300** |
| 5 | 145–75 | 70 | H1, H2, H3 | C1, C2 | 50 | 30 | +20 | **+1,400** |
| 6 | 75–65 | 10 | H2, H3 | C1, C2 | 35 | 30 | +5 | **+50** |
| 7 | 65–55 | 10 | H2, H3 | C1 | 35 | 18 | +17 | **+170** |
| 8 | 55–35 | 20 | H2 | C1 | 25 | 18 | +7 | **+140** |

### 4.3 Detaylı Hesaplama (Detailed Calculation)

```
ΔH₁ = (15 - 0)  × 10 = +15 × 10  = +150 kW   (fazla — yalnızca sıcak akış)
ΔH₂ = (15 - 18) × 50 =  -3 × 50  = -150 kW   (açık)
ΔH₃ = (15 - 30) × 30 = -15 × 30  = -450 kW   (açık)
ΔH₄ = (40 - 30) × 30 = +10 × 30  = +300 kW   (fazla)
ΔH₅ = (50 - 30) × 70 = +20 × 70  = +1,400 kW (fazla — en büyük aralık)
ΔH₆ = (35 - 30) × 10 =  +5 × 10  = +50 kW    (fazla)
ΔH₇ = (35 - 18) × 10 = +17 × 10  = +170 kW   (fazla)
ΔH₈ = (25 - 18) × 20 =  +7 × 20  = +140 kW   (fazla)
```

### 4.4 Genel Enerji Dengesi Kontrolü (Overall Energy Balance Check)

```
ΣΔH_k = (+150) + (-150) + (-450) + (+300) + (+1,400) + (+50) + (+170) + (+140)
       = 150 - 150 - 450 + 300 + 1,400 + 50 + 170 + 140
       = +1,610 kW

ΣQ_hot - ΣQ_cold = 7,250 - 5,640 = +1,610 kW

ΣΔH_k = ΣQ_hot - ΣQ_cold = 1,610 kW ✓
```

Bu eşitlik, doğru bir PTA'da **her zaman** sağlanmalıdır. Sağlanmıyorsa aktif akış atamasında hata vardır. Eşitlik hem algoritmik doğruluğun hem de akış verisi tutarlılığının kanıtıdır.

## 5. Isı Kaskadı (Heat Cascade)

### 5.1 Kaskad Prensibi (Cascade Principle)

Isı kaskadı, termodinamiğin ikinci yasasına dayanır: ısı yalnızca yüksek sıcaklıktan düşük sıcaklığa akar. Kaydırılmış sıcaklık ölçeğinde her aralıktaki ısı fazlası veya açığı, yukarıdan aşağıya doğru kaskad edilir:

```
Kaskad denklemi:
  R_k = R_(k-1) + ΔH_k

Burada:
  R_k   = k. aralığın ALT sınırından geçen artık ısı akışı (residual heat flow) [kW]
  R_0   = En üst aralığın üst sınırına giren ısı akışı [kW]
  ΔH_k  = k. aralığın net ısı dengesi [kW]

Fiziksel anlam:
  R_k > 0 → k. seviyeden aşağı doğru net ısı akışı var (fizibl)
  R_k = 0 → k. seviyede ısı akışı yok (potansiyel pinch)
  R_k < 0 → k. seviyede ısının yukarı akması gerekir (fizibl DEĞİL)
```

### 5.2 Başlangıç Kaskadı (Initial Cascade, R₀ = 0)

İlk adımda dış utility yokmuş gibi R₀ = 0 alınır:

```
T_shifted [°C]    Kaskad              Artık Isı R [kW]
                                      ─────────────────
    265          R₀ =                        0
                   │  ΔH₁ = +150
                   ↓
    255          R₁ = 0 + 150       =     +150
                   │  ΔH₂ = -150
                   ↓
    205          R₂ = 150 + (-150)  =        0
                   │  ΔH₃ = -450
                   ↓
    175          R₃ = 0 + (-450)    =     -450  ← EN NEGATİF
                   │  ΔH₄ = +300
                   ↓
    145          R₄ = -450 + 300    =     -150
                   │  ΔH₅ = +1,400
                   ↓
     75          R₅ = -150 + 1,400  =   +1,250
                   │  ΔH₆ = +50
                   ↓
     65          R₆ = 1,250 + 50    =   +1,300
                   │  ΔH₇ = +170
                   ↓
     55          R₇ = 1,300 + 170   =   +1,470
                   │  ΔH₈ = +140
                   ↓
     35          R₈ = 1,470 + 140   =   +1,610
```

### 5.3 Kaskad Sonuç Tablosu (Cascade Summary Table)

| Seviye | T_shifted [°C] | ΔH_k [kW] | R_k [kW] | Fizibilite |
|--------|---------------|-----------|---------|------------|
| 0 | 265 | — | 0 | Fizibl |
| 1 | 255 | +150 | +150 | Fizibl |
| 2 | 205 | -150 | 0 | Fizibl (sınırda) |
| 3 | 175 | -450 | **-450** | **Fizibl DEĞİL** |
| 4 | 145 | +300 | -150 | **Fizibl DEĞİL** |
| 5 | 75 | +1,400 | +1,250 | Fizibl |
| 6 | 65 | +50 | +1,300 | Fizibl |
| 7 | 55 | +170 | +1,470 | Fizibl |
| 8 | 35 | +140 | +1,610 | Fizibl |

### 5.4 Fizibilite Analizi (Feasibility Analysis)

Negatif R değerleri, o seviyede ısının termodinamik olarak imkansız bir yönde (düşükten yükseğe) akması gerektiğini gösterir:

```
Negatif değerler:
  R₃ = -450 kW (T = 175°C shifted)  ← en negatif
  R₄ = -150 kW (T = 145°C shifted)

Yorum:
  175°C shifted seviyesinin üzerindeki aralıklarda toplam ısı açığı
  (150 - 150 - 450 = -450 kW) o seviyenin altına aktarılacak ısıdan
  fazladır. Dışarıdan sıcak utility sağlanması zorunludur.

  En negatif değerin büyüklüğü, gerekli minimum sıcak utility miktarını verir.
```

## 6. Düzeltilmiş Kaskad (Corrected/Feasible Cascade)

### 6.1 Düzeltme Prensibi (Correction Principle)

Tüm negatif R değerlerini ortadan kaldırmak için, kaskadın en üst seviyesine (R₀) yeterli miktarda sıcak utility eklenir:

```
QH,min = |min(R_k)| = |R₃| = |-450| = 450 kW

Düzeltilmiş kaskad:
  R'_k = R_k + QH,min    (tüm değerlere QH,min eklenir)
```

Bu işlem, en negatif değeri sıfıra çekerken diğer tüm değerleri sıfır veya pozitif yapar.

### 6.2 Düzeltilmiş Kaskad Hesabı (Corrected Cascade Calculation)

```
QH,min = 450 kW

T_shifted [°C]    Düzeltilmiş R' [kW]    Açıklama
                   ────────────────────    ──────────
    265          R'₀ = 0 + 450    = 450   (QH,min girişi)
                   │  ΔH₁ = +150
                   ↓
    255          R'₁ = 150 + 450  = 600
                   │  ΔH₂ = -150
                   ↓
    205          R'₂ = 0 + 450    = 450
                   │  ΔH₃ = -450
                   ↓
    175          R'₃ = -450 + 450 = 0     ← PINCH NOKTASI (R' = 0)
                   │  ΔH₄ = +300
                   ↓
    145          R'₄ = -150 + 450 = 300
                   │  ΔH₅ = +1,400
                   ↓
     75          R'₅ = 1,250 + 450 = 1,700
                   │  ΔH₆ = +50
                   ↓
     65          R'₆ = 1,300 + 450 = 1,750
                   │  ΔH₇ = +170
                   ↓
     55          R'₇ = 1,470 + 450 = 1,920
                   │  ΔH₈ = +140
                   ↓
     35          R'₈ = 1,610 + 450 = 2,060   (QC,min çıkışı)
```

### 6.3 Düzeltilmiş Kaskad Tablosu (Corrected Cascade Table)

| Seviye | T_shifted [°C] | R'_k [kW] | Durum |
|--------|---------------|----------|-------|
| 0 | 265 | 450 | QH,min = 450 kW (sıcak utility girişi) |
| 1 | 255 | 600 | |
| 2 | 205 | 450 | |
| 3 | **175** | **0** | **PINCH NOKTASI** |
| 4 | 145 | 300 | |
| 5 | 75 | 1,700 | |
| 6 | 65 | 1,750 | |
| 7 | 55 | 1,920 | |
| 8 | 35 | 2,060 | QC,min = 2,060 kW (soğuk utility çıkışı) |

### 6.4 PTA Sonuçlarının Okunması (Reading PTA Results)

Düzeltilmiş kaskaddan üç temel sonuç okunur:

```
1. QH,min = R'₀ = 450 kW
   → Minimum sıcak utility ihtiyacı
   → Kaskadın en üstüne eklenen değer

2. QC,min = R'₈ = 2,060 kW
   → Minimum soğuk utility ihtiyacı
   → Kaskadın en altından çıkan değer

3. Pinch noktası: R'_k = 0 olan seviye
   → T_pinch_shifted = 175°C
   → T_pinch_hot = 175 + 5 = 180°C (sıcak taraf)
   → T_pinch_cold = 175 - 5 = 170°C (soğuk taraf)
```

### 6.5 Pinch Noktasının Önemi (Significance of the Pinch Point)

Pinch noktası, prosesi termodinamik olarak iki bağımsız bölgeye ayırır:

```
PINCH ÜSTÜ (T > 175°C shifted):
  ─────────────────────────────
  Yalnızca sıcak utility kullanılır
  Isı: utility → proses yönünde akar
  "Isı alıcısı" (heat sink) bölgesi
  Tasarım kuralı: CP_hot >= CP_cold (her eşleşmede)

PINCH ALTI (T < 175°C shifted):
  ─────────────────────────────
  Yalnızca soğuk utility kullanılır
  Isı: proses → utility yönünde akar
  "Isı kaynağı" (heat source) bölgesi
  Tasarım kuralı: CP_hot <= CP_cold (her eşleşmede)

PINCH KURALLARI (altın kurallar):
  1. Pinch noktasının üzerinden alta ısı transfer etme (cross-pinch ihlali)
  2. Pinch noktasının üzerinde soğuk utility kullanma
  3. Pinch noktasının altında sıcak utility kullanma
```

Bu kurallardan herhangi birinin ihlali, QH,min ve QC,min değerlerinin artmasına neden olur.

## 7. Doğrulama (Verification)

### 7.1 Genel Enerji Dengesi Kontrolü (Overall Energy Balance Check)

PTA sonuçlarının birincil doğrulama yöntemi:

```
Genel enerji dengesi:
  ΣQ_hot + QH,min = ΣQ_cold + QC,min

Kontrol:
  7,250 + 450 = 5,640 + 2,060
  7,700 = 7,700 ✓✓✓

Alternatif form:
  QC,min - QH,min = ΣQ_hot - ΣQ_cold
  2,060 - 450 = 7,250 - 5,640
  1,610 = 1,610 ✓✓✓
```

### 7.2 Kaskad İç Tutarlılık (Cascade Internal Consistency)

Her aralıkta kaskad denklemi doğrulanır:

```
R'₁ = R'₀ + ΔH₁ = 450 + 150   = 600   ✓
R'₂ = R'₁ + ΔH₂ = 600 + (-150) = 450   ✓
R'₃ = R'₂ + ΔH₃ = 450 + (-450) = 0     ✓ (pinch)
R'₄ = R'₃ + ΔH₄ = 0 + 300      = 300   ✓
R'₅ = R'₄ + ΔH₅ = 300 + 1,400  = 1,700 ✓
R'₆ = R'₅ + ΔH₆ = 1,700 + 50   = 1,750 ✓
R'₇ = R'₆ + ΔH₇ = 1,750 + 170  = 1,920 ✓
R'₈ = R'₇ + ΔH₈ = 1,920 + 140  = 2,060 ✓

Tüm R'_k >= 0 ✓ (negatif değer yok → fizibl kaskad)
```

### 7.3 Bileşik Eğrilerle Çapraz Doğrulama (Cross-Verification with Composite Curves)

PTA sonuçları, bileşik eğrilerden okunan değerlerle karşılaştırılmalıdır:

```
Kontrol noktaları:
1. QH,min (bileşik eğrilerin sol üst boşluğu)  = PTA QH,min = 450 kW ✓
2. QC,min (bileşik eğrilerin sağ alt boşluğu)   = PTA QC,min = 2,060 kW ✓
3. Pinch noktası (eğrilerin en yakın noktası)    = 180°C hot / 170°C cold ✓

4. İç ısı geri kazanımı (internal heat recovery):
   Q_recovery = ΣQ_hot - QC,min = 7,250 - 2,060 = 5,190 kW
   veya      = ΣQ_cold - QH,min = 5,640 - 450   = 5,190 kW ✓

5. Geri kazanım oranı:
   η_recovery = Q_recovery / ΣQ_cold = 5,190 / 5,640 = %92.0
   → Soğuk akış ihtiyacının %92'si iç geri kazanımla karşılanabilir
```

### 7.4 Pinch Noktası Sıcaklık Doğrulaması (Pinch Temperature Verification)

```
Pinch (shifted)    = 175°C

Sıcak taraf pinch  = 175 + ΔTmin/2 = 175 + 5 = 180°C
Soğuk taraf pinch  = 175 - ΔTmin/2 = 175 - 5 = 170°C
ΔT_pinch           = 180 - 170 = 10°C = ΔTmin ✓

Pinch'te aktif akışlar:
  Sıcak: H2 (180°C gerçek sıcaklık → pinch'te)
  Soğuk: C2 (170°C gerçek sıcaklık → pinch'te)
  ΔT = 180 - 170 = 10°C = ΔTmin ✓
```

## 8. Alternatif PTA Formülasyonları (Alternative PTA Formulations)

### 8.1 Linnhoff Orijinal Formülasyonu (Linnhoff's Original Approach, 1978)

Linnhoff ve Flower'ın orijinal formülasyonunda yalnızca tek taraflı kaydırma yapılır:

```
Yaklaşım A — Yalnızca sıcak akışlar kaydırılır:
  T_hot_shifted  = T_hot - ΔTmin
  T_cold_shifted = T_cold (değişmez)

Yaklaşım B — Yalnızca soğuk akışlar kaydırılır:
  T_hot_shifted  = T_hot (değişmez)
  T_cold_shifted = T_cold + ΔTmin
```

Her iki yaklaşım da aynı QH,min, QC,min ve pinch sonuçlarını verir. Ancak aralık sıcaklıkları farklıdır. Simetrik kaydırma (ΔTmin/2) bu iki yaklaşımın ortalamasıdır.

### 8.2 Simetrik Kaydırma (ΔTmin/2 — Bu Belgede Kullanılan)

```
T_hot_shifted  = T_hot - ΔTmin/2
T_cold_shifted = T_cold + ΔTmin/2
```

Bu yaklaşım Linnhoff (1994) User Guide'da standardize edilmiştir ve tercih edilir çünkü:

- Grand Composite Curve (GCC) doğrudan düzeltilmiş kaskad verilerinden oluşturulabilir
- Pinch noktası tek bir kaydırılmış sıcaklık olarak ifade edilir
- Utility yerleştirme sezgisel ve doğrudandır
- Sıcak ve soğuk taraf arasında simetri sağlar

### 8.3 Üç Yaklaşımın Karşılaştırması (Comparison of Three Approaches)

Referans problem için:

| Özellik | Tek taraflı (hot) | Tek taraflı (cold) | Simetrik (ΔTmin/2) |
|---------|-------------------|--------------------|--------------------|
| H1 shifted | 260–70 | 270–80 | 265–75 |
| C1 shifted | 30–250 | 40–260 | 35–255 |
| Aralık sayısı | 8 | 8 | 8 |
| QH,min | 450 kW | 450 kW | 450 kW |
| QC,min | 2,060 kW | 2,060 kW | 2,060 kW |
| Pinch (hot/cold) | 180/170°C | 180/170°C | 180/170°C |

Sonuçlar **tamamen aynıdır**; yalnızca ara hesap sıcaklıkları farklıdır.

### 8.4 Akış-Spesifik ΔTmin (Stream-Specific Contributions)

Farklı akışlar farklı ısı transfer katsayılarına (h) sahip olduğunda, ΔTmin her akış çifti için farklı olabilir:

```
Bireysel ΔT katkısı:
  ΔT_contribution,i = 1 / (h_i)    (yaklaşık, film katsayısı bazlı)

Kaydırma:
  Sıcak akış i: T_shifted = T - ΔT_contribution,i
  Soğuk akış j: T_shifted = T + ΔT_contribution,j

Avantaj: Daha doğru minimum alan hedefleri (Bath formülü ile)
Dezavantaj: Her akış çifti için farklı ΔTmin → hesaplama karmaşıklığı artar
```

Bu ileri düzey formülasyon, endüstriyel uygulamalarda eşanjör maliyetlerinin daha doğru tahminini sağlar ve süperhedefleme (supertargeting) çalışmalarında kullanılır.

## 9. Çoklu Pinch Noktaları (Multiple Pinch Points)

### 9.1 Oluşum Koşulları (When and Why They Occur)

Düzeltilmiş kaskadda birden fazla seviyede R' = 0 olabilir. Bu durum şu koşullarda ortaya çıkar:

1. **Geniş sıcaklık aralıkları:** Akışların sıcaklık aralıkları çok farklıysa ve arada akış olmayan bölgeler varsa
2. **Dengeli CP değerleri:** Belirli ardışık aralıklarda ΣCP_hot = ΣCP_cold ise R' değeri değişmeden kalır
3. **Çok sayıda akış:** Akış sayısı arttıkça çoklu pinch olasılığı artar
4. **Utility akışları:** Utility akışlarının probleme dahil edilmesi yeni pinch noktaları oluşturabilir
5. **Faz değişim akışları:** Sabit sıcaklıkta buharlaşan/yoğuşan akışlar sıklıkla pinch oluşturur

### 9.2 Referans Problemde Analiz (Analysis in Reference Problem)

Referans problemimizde tek pinch (175°C shifted) vardır. Diğer R' değerleri sıfır değildir:

```
Düzeltilmiş kaskad:
  R'₀ = 450    (≠ 0)
  R'₁ = 600    (≠ 0)
  R'₂ = 450    (≠ 0)
  R'₃ = 0      (= 0 → PINCH)
  R'₄ = 300    (≠ 0)
  R'₅ = 1,700  (≠ 0)
  R'₆ = 1,750  (≠ 0)
  R'₇ = 1,920  (≠ 0)
  R'₈ = 2,060  (≠ 0)

NOT: R'₂ = 450 kW ≠ 0, bu nedenle 205°C'de ikinci pinch YOKTUR.
```

### 9.3 Varsayımsal Çoklu Pinch Örneği

Eğer akış verileri farklı olsaydı ve Aralık 2'de ΔH₂ = -600 kW olsaydı:

```
Başlangıç kaskadında:
  R₂ = 150 + (-600) = -450
  R₃ = -450 + (-450) = -900

  QH,min = 900 kW
  R'₂ = -450 + 900 = 450 → hala ≠ 0

Çoklu pinch için R'₂ = 0 olmalı, yani R₂ = -QH,min olmalıdır.
Bu ancak özel CP kombinasyonlarında gerçekleşir.
```

### 9.4 Çoklu Pinch Durumunda HEN Tasarımı (Design with Multiple Pinch Points)

```
Her pinch noktası, Isı Eşanjör Ağı tasarımını bağımsız alt-problemlere böler:

n pinch noktası → (n+1) alt-problem

Örnek: İki pinch noktası (T₁ ve T₂, T₁ > T₂)
  Alt-problem 1: T > T₁ (pinch 1 üstü — sıcak utility bölgesi)
  Alt-problem 2: T₂ < T < T₁ (iki pinch arası — utility yok)
  Alt-problem 3: T < T₂ (pinch 2 altı — soğuk utility bölgesi)

Her alt-problemde:
  - Pinch üstünde: Yalnızca sıcak utility kullanılır
  - Pinch altında: Yalnızca soğuk utility kullanılır
  - Her pinch noktasında: ΔTmin kısıtı sağlanmalıdır
  - CP kuralları her alt-problem için ayrı ayrı uygulanır
```

### 9.5 Utility Pinch (Utility Pinch Points)

Grand Composite Curve üzerinde utility yerleştirildiğinde, utility akışlarının giriş/çıkış sıcaklıkları yeni pinch noktaları oluşturabilir:

```
Proses pinch: 175°C (shifted)

Utility yerleştirme sonrası olası ek pinch noktaları:
  - Yüksek basınç buhar (HP steam, ~250°C) → GCC teğet noktasında
  - Orta basınç buhar (MP steam, ~180°C) → GCC cebi varsa
  - Soğutma suyu (CW, ~25°C) → genellikle pinch oluşturmaz

Utility pinch = GCC eğrisinin utility profiline teğet olduğu nokta

Utility pinch noktaları, çoklu utility seviyelerinin optimum dağılımını belirler
ve Total Site Analysis'in temelini oluşturur.
```

### 9.6 Threshold Problemler (Threshold Problems)

Bazı durumlarda kaskadda hiç negatif değer oluşmaz (QH,min = 0) veya yalnızca bir utility türü gerekir:

```
Threshold problemi türleri:
  Tip 1: QH,min = 0, QC,min > 0 → Yalnızca soğuk utility gerekir
  Tip 2: QH,min > 0, QC,min = 0 → Yalnızca sıcak utility gerekir

Bu durumda proses pinch yerine "threshold" sıcaklığı vardır.
Tasarım, tek taraflı utility problemi olarak çözülür.

ΔTmin değiştirildiğinde threshold problemi normal (iki utility) probleme
dönüşebilir veya tersi olabilir.
```

## İlgili Dosyalar

- [INDEX.md](INDEX.md) — Pinch analizi bilgi tabanı navigasyon haritası ve yükleme kuralları
- [fundamentals.md](fundamentals.md) — Pinch analizi temel kavramları, MER hedefleri, 3 altın kural
- [composite_curves.md](composite_curves.md) — Bileşik eğri oluşturma, grafik yöntem (PTA ile çapraz doğrulama)
- [grand_composite.md](grand_composite.md) — GCC oluşturma (PTA düzeltilmiş kaskad verilerinden), utility yerleştirme
- [targeting.md](targeting.md) — Enerji, alan ve maliyet hedefleme (PTA sonuçlarını kullanır)
- [hen_design.md](hen_design.md) — Isı Eşanjör Ağı tasarımı (pinch noktası ve CP kuralları)
- [delta_t_min.md](delta_t_min.md) — ΔTmin seçimi ve süperhedefleme (PTA tekrarlı çalıştırma)
- [common_mistakes.md](common_mistakes.md) — PTA'da sık yapılan hatalar (sınır koşulları, aktif akış ataması)

## Referanslar

- Linnhoff, B. and Flower, J.R., "Synthesis of Heat Exchanger Networks: I. Systematic Generation of Energy Optimal Networks," AIChE Journal, 24(4), pp. 633-642, 1978
- Linnhoff, B. et al., "User Guide on Process Integration for the Efficient Use of Energy," IChemE, Rugby, UK, 1994 (Revised Edition)
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," 2nd Edition, Butterworth-Heinemann, 2007
- Smith, R., "Chemical Process Design and Integration," 2nd Edition, Wiley, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration: Minimisation of Energy and Water Use, Waste and Emissions," Woodhead Publishing, 2013
- Hohmann, E.C., "Optimum Networks for Heat Exchange," PhD Thesis, University of Southern California, 1971
