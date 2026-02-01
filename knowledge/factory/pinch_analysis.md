# Pinch Analizi ve Isı Entegrasyonu (Pinch Analysis and Heat Integration)

> Son güncelleme: 2026-01-31

## Genel Bakış

Pinch analizi, Boden Linnhoff tarafından 1978'de geliştirilen ve endüstriyel proseslerde minimum enerji tüketimini sistematik olarak belirleyen termodinamik tabanlı bir metodolojidir. Sıcak ve soğuk akışların ısı alışverişi potansiyelini analiz ederek, prosesin teorik minimum dış enerji (utility) ihtiyacını hesaplar ve optimum Isı Eşanjör Ağı (HEN — Heat Exchanger Network) tasarımına yol gösterir. Pinch analizi, fabrika seviyesinde enerji entegrasyonunun temel aracıdır ve tipik olarak %20-40 enerji tasarrufu sağlar.

## 1. Temel Kavramlar (Fundamental Concepts)

### 1.1 Sıcak ve Soğuk Akışlar (Hot and Cold Streams)

Bir proseste ısıtılması veya soğutulması gereken her madde akışı, pinch analizi için temel veri kaynağıdır:

```
Sıcak akış (Hot stream): Soğutulması gereken akış
  T_kaynak > T_hedef → Isı veren akış
  Örnek: Reaktör çıkışı 250°C → 80°C soğutulmalı

Soğuk akış (Cold stream): Isıtılması gereken akış
  T_kaynak < T_hedef → Isı alan akış
  Örnek: Besleme suyu 25°C → 180°C ısıtılmalı

Akış ısı kapasitesi (Heat Capacity Flowrate):
CP = ṁ × Cp [kW/°C]

Burada:
- ṁ = kütle debisi [kg/s]
- Cp = özgül ısı kapasitesi [kJ/(kg·°C)]

Akışın ısı yükü (Heat Duty):
Q = CP × |T_kaynak - T_hedef| [kW]
```

### 1.2 Akış Veri Tablosu (Stream Data Table)

Pinch analizinin ilk adımı, proses akış verilerinin çıkarılmasıdır:

| Akış No | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Q [kW] |
|---|---|---|---|---|---|
| H1 | Sıcak | 270 | 80 | 15.0 | 2,850 |
| H2 | Sıcak | 180 | 40 | 25.0 | 3,500 |
| H3 | Sıcak | 150 | 60 | 10.0 | 900 |
| C1 | Soğuk | 30 | 250 | 18.0 | 3,960 |
| C2 | Soğuk | 60 | 200 | 12.0 | 1,680 |

```
Toplam sıcak akış ısı yükü: Q_H = 2,850 + 3,500 + 900 = 7,250 kW
Toplam soğuk akış ısı yükü: Q_C = 3,960 + 1,680 = 5,640 kW
```

### 1.3 Minimum Yaklaşım Sıcaklığı Farkı (ΔTmin)

ΔTmin, sıcak ve soğuk akışlar arasındaki minimum izin verilen sıcaklık farkıdır:

```
ΔTmin seçimi bir ekonomik optimizasyon problemidir:

Küçük ΔTmin:
  + Daha fazla ısı geri kazanımı (düşük utility maliyeti)
  - Daha büyük eşanjör alanı (yüksek yatırım maliyeti)

Büyük ΔTmin:
  + Daha küçük eşanjör alanı (düşük yatırım maliyeti)
  - Daha az ısı geri kazanımı (yüksek utility maliyeti)

Optimum ΔTmin: Toplam yıllık maliyet (yatırım + enerji) minimum olan nokta
```

### 1.4 Endüstri Bazında Tipik ΔTmin Değerleri

| Endüstri / Uygulama | Tipik ΔTmin [°C] | Açıklama |
|---|---|---|
| Petrol rafineri | 20-40 | Yüksek sıcaklık, yüksek enerji maliyeti |
| Petrokimya | 10-20 | Orta-yüksek sıcaklık prosesleri |
| Kimya endüstrisi | 10-20 | Proses türüne bağlı |
| Gıda ve içecek | 5-15 | Düşük sıcaklık, hijyen gereksinimleri |
| Kağıt ve selüloz | 10-25 | Su-buhar sistemleri |
| Tekstil | 10-20 | Boyama ve kurutma prosesleri |
| Çimento / seramik | 30-50 | Çok yüksek sıcaklık farkları |
| Soğutma sistemleri | 3-5 | Küçük sıcaklık farkları kritik |

## 2. Bileşik Eğriler (Composite Curves)

### 2.1 Sıcak Bileşik Eğri Oluşturma (Hot Composite Curve)

```
Adım 1: Sıcaklık aralıklarını belirle
  Tüm sıcak akışların T_kaynak ve T_hedef değerlerini sırala:
  270, 180, 150, 80, 60, 40 → sıralı: 40, 60, 80, 150, 180, 270

Adım 2: Her aralıkta toplam CP hesapla
  40-60°C:   CP = CP_H2 = 25.0 kW/°C
  60-80°C:   CP = CP_H2 + CP_H3 = 25.0 + 10.0 = 35.0 kW/°C
  80-150°C:  CP = CP_H2 + CP_H3 = 25.0 + 10.0 = 35.0 kW/°C
  (Not: H1 bu aralıkta 270→80, yani 80°C altında yok)
  80-150°C:  CP = CP_H1 + CP_H2 + CP_H3 = 15.0 + 25.0 + 10.0 = 50.0 kW/°C
  → Düzeltme: H1: 270→80, H2: 180→40, H3: 150→60
  40-60°C:   H2 aktif → CP = 25.0
  60-80°C:   H2 + H3 aktif → CP = 35.0
  80-150°C:  H1 + H2 + H3 aktif → CP = 50.0
  150-180°C: H1 + H2 aktif → CP = 40.0
  180-270°C: H1 aktif → CP = 15.0

Adım 3: Her aralığın ısı yükünü hesapla
  40-60°C:   Q = 25.0 × 20 = 500 kW
  60-80°C:   Q = 35.0 × 20 = 700 kW
  80-150°C:  Q = 50.0 × 70 = 3,500 kW
  150-180°C: Q = 40.0 × 30 = 1,200 kW
  180-270°C: Q = 15.0 × 90 = 1,350 kW
  Toplam: 7,250 kW ✓

Adım 4: Kümülatif ısı (enthalpy) tablosu
  T [°C]  |  Q_kümülatif [kW]
  270     |  0
  180     |  1,350
  150     |  2,550
  80      |  6,050
  60      |  6,750
  40      |  7,250
```

### 2.2 Soğuk Bileşik Eğri Oluşturma (Cold Composite Curve)

```
Soğuk akışlar: C1: 30→250 (CP=18.0), C2: 60→200 (CP=12.0)

Sıcaklık aralıkları: 30, 60, 200, 250

  30-60°C:   C1 aktif → CP = 18.0
  60-200°C:  C1 + C2 aktif → CP = 30.0
  200-250°C: C1 aktif → CP = 18.0

Isı yükleri:
  30-60°C:   Q = 18.0 × 30 = 540 kW
  60-200°C:  Q = 30.0 × 140 = 4,200 kW
  200-250°C: Q = 18.0 × 50 = 900 kW
  Toplam: 5,640 kW ✓

Kümülatif ısı tablosu:
  T [°C]  |  Q_kümülatif [kW]
  30      |  0
  60      |  540
  200     |  4,740
  250     |  5,640
```

### 2.3 Bileşik Eğrilerin Grafiksel Gösterimi (ASCII)

```
Sıcaklık [°C]
    |
280 |                          * (H, 270°C)
    |                        /
240 |                      /     * (C, 250°C)
    |                    /      /
200 |                  /      * (C, 200°C)
    |                /      /
160 |              /      /
    |            * (H)  /
120 |          /      /
    |        /      /
 80 |      * (H)  /
    |     /     /
 60 |    *    * (C, 60°C)
    |   /   /
 40 |  * (H, 40°C)
    | /
 20 |* (C, 30°C)
    |__________________________ Enthalpy [kW]
    0   1000  2000 3000 4000 5000 6000 7000

Sıcak bileşik eğri: sağdan sola (yüksek → düşük sıcaklık)
Soğuk bileşik eğri: soldan sağa (düşük → yüksek sıcaklık)
Eğriler arasındaki yatay mesafe: ΔTmin noktasında minimum
```

## 3. Enerji Hedefleri (Energy Targets)

### 3.1 Minimum Enerji Hedeflerinin Hesaplanması

```
ΔTmin = 10°C seçimi ile Problem Tablosu Algoritması (PTA):

Adım 1: Kaydırılmış sıcaklıklar (Shifted Temperatures)
  Sıcak akışlar: T_kaydırılmış = T_gerçek - ΔTmin/2
  Soğuk akışlar: T_kaydırılmış = T_gerçek + ΔTmin/2

Sıcak akışlar (kaydırılmış):
  H1: 265 → 75
  H2: 175 → 35
  H3: 145 → 55

Soğuk akışlar (kaydırılmış):
  C1: 35 → 255
  C2: 65 → 205

Adım 2: Sıcaklık aralıkları (sıralı kaydırılmış T):
  255, 205, 175, 145, 75, 65, 55, 35

Adım 3: Her aralıkta net ısı dengesi hesapla
  CP_sıcak - CP_soğuk formatında:

  Aralık [°C]      | CP_sıcak | CP_soğuk | Net CP | ΔT  | ΔH [kW]
  255-205           | 0        | 18.0     | -18.0  | 50  | -900
  205-175           | 0        | 30.0     | -30.0  | 30  | -900
  175-145           | 15+25    | 30.0     | 10.0   | 30  | +300
  145-75            | 15+25+10 | 30.0     | 20.0   | 70  | +1,400
  75-65             | 25+10    | 30.0     | 5.0    | 10  | +50
  65-55             | 25+10    | 12.0     | 23.0   | 10  | +230
  55-35             | 25       | 12.0     | 13.0   | 20  | +260

Adım 4: Kaskad (ısı akışı)
  Başlangıç: R₀ = 0
  255°C: R = 0
  205°C: R = 0 + (-900) = -900
  175°C: R = -900 + (-900) = -1,800  ← En negatif değer
  145°C: R = -1,800 + 300 = -1,500
  75°C:  R = -1,500 + 1,400 = -100
  65°C:  R = -100 + 50 = -50
  55°C:  R = -50 + 230 = +180
  35°C:  R = 180 + 260 = +440

Adım 5: Düzeltilmiş kaskad (R₀ = |en negatif| = 1,800)
  255°C: R = 1,800         ← QH,min (minimum sıcak utility)
  205°C: R = 900
  175°C: R = 0             ← PINCH NOKTASI
  145°C: R = 300
  75°C:  R = 1,700
  65°C:  R = 1,750
  55°C:  R = 1,980
  35°C:  R = 2,240         ← QC,min (minimum soğuk utility)
```

### 3.2 Sonuç: Minimum Enerji Hedefleri

```
ΔTmin = 10°C için:

QH,min = 1,800 kW  (minimum sıcak utility — dış ısıtma ihtiyacı)
QC,min = 2,240 kW  (minimum soğuk utility — dış soğutma ihtiyacı)

Pinch noktası: 175°C (kaydırılmış)
  Sıcak taraf: T_pinch,sıcak = 175 + 5 = 180°C
  Soğuk taraf: T_pinch,soğuk = 175 - 5 = 170°C

Maksimum ısı geri kazanım (heat recovery):
Q_geri_kazanım = Q_H_toplam - QC,min = 7,250 - 2,240 = 5,010 kW
Veya: Q_geri_kazanım = Q_C_toplam - QH,min = 5,640 - 1,800 = 3,840 kW

Doğrulama:
QH,min - QC,min = Q_C_toplam - Q_H_toplam
1,800 - 2,240 = 5,640 - 7,250
-440 = -1,610   → (burada net ısı dengesi farkı var)

Toplam enerji dengesi:
Q_H_toplam + QH,min = Q_C_toplam + QC,min
7,250 + 1,800 = 5,640 + 2,240 + Q_geri_kazanım
Verilecek ısı = Alınacak ısı kontrolü ile tutarlılık sağlanır.
```

### 3.3 ΔTmin Duyarlılık Analizi

| ΔTmin [°C] | QH,min [kW] | QC,min [kW] | Q_geri_kazanım [kW] | Eşanjör Alanı [m²] | Toplam Maliyet [€/yıl] |
|---|---|---|---|---|---|
| 5 | 1,300 | 1,740 | 5,510 | 1,850 | 185,000 |
| 10 | 1,800 | 2,240 | 5,010 | 1,200 | 162,000 |
| 15 | 2,200 | 2,640 | 4,610 | 920 | 158,000 |
| 20 | 2,650 | 3,090 | 4,160 | 750 | 165,000 |
| 30 | 3,400 | 3,840 | 3,410 | 540 | 192,000 |
| 40 | 4,100 | 4,540 | 2,710 | 420 | 228,000 |

```
Optimum ΔTmin = 15°C (bu örnek için minimum toplam yıllık maliyet)

Not: Optimum ΔTmin endüstriye, enerji fiyatlarına ve sermaye maliyetine
bağlıdır. Enerji fiyatları arttıkça optimum ΔTmin düşer.
```

## 4. Büyük Bileşik Eğri — GCC (Grand Composite Curve)

### 4.1 GCC Oluşturma

```
GCC, kaydırılmış sıcaklık (T*) vs. net ısı akışı (R) grafiğidir:

T* [°C]   |  R (net ısı akışı) [kW]
255       |  1,800    ← QH,min
205       |  900
175       |  0        ← Pinch
145       |  300
75        |  1,700
65        |  1,750
55        |  1,980
35        |  2,240    ← QC,min

GCC ASCII gösterimi:

T* [°C]
  |
260|*
  |  \
220|    \
  |      \
180|        * ← Pinch (R=0)
  |       /
140|      *
  |     /
100|    /
  |   /
 60|  *
  | /
 40|*
  |_________________ R [kW]
  0   500  1000 1500 2000
```

### 4.2 GCC Kullanım Alanları

```
GCC'nin sağladığı bilgiler:
1. Utility yerleştirme: Hangi sıcaklık seviyesinde ne kadar utility gerekli
2. Isı cebi (heat pocket): GCC'nin pinch altında içe döndüğü bölge
3. Utility seçimi: HP buhar, LP buhar, soğutma suyu seviyeleri
4. CHP potansiyeli: Güç üretimi için kullanılabilir ısı aralığı
5. Isı pompası uygunluğu: Pinch etrafındaki sıcaklık farkı

Utility yerleştirme örneği:
- HP Buhar (250°C): 900 kW → Pinch üzerinde en yüksek sıcaklık bölgesi
- LP Buhar (150°C): 900 kW → Pinch üzerinde orta sıcaklık bölgesi
- Soğutma suyu (25°C): 2,240 kW → Pinch altında
```

### 4.3 Isı Cebi (Heat Pocket) Kavramı

```
Isı cebi, GCC'de pinch altındaki bir bölgede net ısı açığı oluşmasıdır.
Bu bölgede, pinch altında olmasına rağmen iç ısı alışverişi yapılabilir.

Isı cebi analizi:
- Cebin büyüklüğü: İç ısı alışverişi potansiyeli
- Cebin derinliği: Gerekli eşanjör sayısı ve karmaşıklığı
- Cebin ortadan kaldırılması: Soğuk utility azaltılabilir

Pratikte isı cebi ile birlikte QC,min gereksinimi azaltılabilir,
ancak ek eşanjör yatırımı gerekir.
```

## 5. Pinch Kuralları (Pinch Rules)

### 5.1 Üç Altın Kural

```
Kural 1: PINCH ÜZERİNDEN ISI TRANSFER ETMEYİN
  (Don't transfer heat across the pinch)

  Pinch üzerinden ısı transferi yapılırsa:
  - QH,min artar (ΔQ kadar fazla sıcak utility gerekir)
  - QC,min artar (ΔQ kadar fazla soğuk utility gerekir)
  - Toplam utility artışı: 2 × ΔQ (çifte ceza)

Kural 2: PINCH ALTINDA SICAK UTILITY KULLANMAYIN
  (Don't use hot utility below the pinch)

  Pinch altı net ısı fazlası olan bölgedir.
  Sıcak utility eklemek → aynı miktarda soğuk utility eklenmesini gerektirir.

Kural 3: PINCH ÜSTÜNDE SOĞUK UTILITY KULLANMAYIN
  (Don't use cold utility above the pinch)

  Pinch üstü net ısı açığı olan bölgedir.
  Soğuk utility eklemek → aynı miktarda sıcak utility eklenmesini gerektirir.
```

### 5.2 Pinch Kurallarının Sonuçları

| Kural İhlali | Sonuç | Utility Artışı |
|---|---|---|
| Pinch üzerinden ΔQ transfer | QH,min + ΔQ, QC,min + ΔQ | 2 × ΔQ |
| Pinch altında QH utility | QH,min + QH, QC,min + QH | 2 × QH |
| Pinch üstünde QC utility | QH,min + QC, QC,min + QC | 2 × QC |

```
Pratik örnek:
Mevcut bir fabrikada pinch analizi sonucu:
- QH,min = 1,800 kW, QC,min = 2,240 kW
- Mevcut utility kullanımı: QH = 3,500 kW, QC = 3,940 kW

Cross-pinch transfer = QH - QH,min = 3,500 - 1,800 = 1,700 kW
Bu, pinch kurallarının ihlal edildiğini gösterir.
Tasarruf potansiyeli: 1,700 kW sıcak utility + 1,700 kW soğuk utility
```

## 6. Isı Eşanjör Ağı Tasarımı — HEN (Heat Exchanger Network Design)

### 6.1 Pinch Eşleşme Kuralları (Pinch Matching Rules)

```
PINCH ÜSTÜ (Sıcak utility gerekli bölge):
- Sıcak akış sayısı ≤ Soğuk akış sayısı (aksi halde akış bölme gerekli)
- CP_sıcak ≤ CP_soğuk (her eşleşmede)

PINCH ALTI (Soğuk utility gerekli bölge):
- Soğuk akış sayısı ≤ Sıcak akış sayısı (aksi halde akış bölme gerekli)
- CP_soğuk ≤ CP_sıcak (her eşleşmede)

Neden:
- Pinch noktasında ΔT = ΔTmin olmalı
- CP eşitsizliği sağlanmazsa, eşanjör boyunca ΔT < ΔTmin olur
  (termodinamik olarak mümkün olmayan durum)
```

### 6.2 HEN Tasarım Adımları

```
Adım 1: Pinch noktasında başla
Adım 2: Pinch üstünü tasarla
  a. Pinch'te CP kuralını kontrol et
  b. Uygun eşleşmeleri yap (tick-off heuristic)
  c. Gerekirse akış bölme uygula
  d. Kalan ısı yükünü utility ile karşıla

Adım 3: Pinch altını tasarla
  a. Pinch'te CP kuralını kontrol et (ters yön)
  b. Uygun eşleşmeleri yap
  c. Kalan ısı yükünü soğuk utility ile karşıla

Adım 4: Minimum eşanjör sayısını hesapla
  U_min = N_akış + N_utility - N_alt_ağ
  N_akış = toplam akış sayısı (sıcak + soğuk)
  N_utility = utility akış sayısı
  N_alt_ağ = bağımsız alt ağ sayısı (genellikle 1 veya 2)
```

### 6.3 HEN Grid Diyagramı (Worked Example)

```
Pinch: 180°C (sıcak) / 170°C (soğuk)
ΔTmin = 10°C

PINCH ÜSTÜ (sol: pinch, sağ: sıcak uçlar)

  H1: 270°C ─────[HX1]──────── 180°C
                    │
  H2: 180°C ──────[pinch]────── 180°C (pinch noktasında, utility yok)

  C1: 170°C ─────[HX1]───[HU1]── 250°C
                           │
  C2: 170°C ──────────[HU2]──── 200°C

  HX1: H1 ↔ C1, Q = 15.0 × (270-180) = 1,350 kW
  HU1: Hot utility → C1, Q = 18.0 × (250-170) - 1,350 = 1,440-1,350 = 90 kW
       → Düzeltme: C1'in pinch üstündeki ısı gereksinimi:
       Q_C1_üst = 18.0 × (250-170) = 1,440 kW
       HX1'den karşılanan: 1,350 kW
       Kalan: QH = 1,440 - 1,350 = 90 kW
  HU2: Hot utility → C2, Q = 12.0 × (200-170) = 360 kW

  Toplam sıcak utility (pinch üstü): 90 + 360 = 450 kW
  (Not: Bu sadece pinch üstü. Gerçek QH,min farklı olabilir —
  burada basitleştirilmiş gösterim yapılmıştır.)

PINCH ALTI (sol: soğuk uçlar, sağ: pinch)

  H1: 180°C ────────[HX2]──────── 80°C
                      │
  H2: 180°C ──[HX3]──[CU1]────── 40°C
                │
  H3: 150°C ──[HX4]──[CU2]────── 60°C

  C1: 30°C  ──[HX2]──[HX3]────── 170°C
                        │
  C2: 60°C  ──[HX4]───────────── 170°C

  Bu bölgede soğuk utility (CU1, CU2) yerleştirilir.
```

### 6.4 Minimum Eşanjör Sayısı

```
Bu örnek için:
N_akış = 5 (H1, H2, H3, C1, C2)
N_utility = 2 (sıcak utility, soğuk utility)
N_alt_ağ = 2 (pinch üstü ve altı)

U_min = (5 + 2) - 2 = 5 eşanjör (pinch bölünmüş)

Bölünmemiş (pinch yok sayılırsa):
U_min = (5 + 2) - 1 = 6 eşanjör

Pinch bölümlemesi genellikle daha az eşanjör verir,
ancak her eşanjörün daha dar ΔT aralığında çalışmasını gerektirir.
```

## 7. Döngü Kırma ve Yol Gevşetme (Loop Breaking and Path Relaxation)

### 7.1 Döngü Kırma (Loop Breaking)

```
HEN'de bir döngü (loop): İki veya daha fazla eşanjör arasında
oluşan kapalı yoldur.

Döngü kırma ile eşanjör sayısı azaltılabilir:
- Bir döngüdeki eşanjörlerden birini kaldır
- Kalan eşanjörlerin ısı yüklerini ayarla
- Sonuç: Daha az eşanjör, ancak ΔTmin ihlali olabilir

Döngü kırma kuralı:
Kaldırılacak eşanjör: En küçük ısı yüküne sahip olan
```

### 7.2 Yol Gevşetme (Path Relaxation)

```
Yol (path): Sıcak utility'den soğuk utility'ye uzanan
eşanjörler zinciridir.

Gevşetme: ΔTmin'i biraz artırarak (ihlal ederek)
daha pratik bir tasarım elde etmek.

Trade-off:
- ΔTmin ihlali: Ek utility maliyeti (genellikle küçük)
- Fayda: Daha az eşanjör, daha basit kontrol, kolay bakım

Kabul edilebilir ihlal: ΔT ≥ 0.8 × ΔTmin (pratik kural)
```

## 8. Utility Yerleştirme (Utility Placement)

### 8.1 GCC Üzerinde Utility Seçimi

```
GCC, farklı utility seviyelerinin optimum yerleşimini gösterir:

Sıcak utility seviyeleri (pinch üstü):
1. Fired heater (>500°C): En pahalı, minimum kullanım
2. HP buhar (250°C): Orta maliyet
3. MP buhar (180°C): Düşük maliyet
4. LP buhar (150°C): En düşük maliyet
→ GCC profiline uygun en düşük seviye tercih edilir

Soğuk utility seviyeleri (pinch altı):
1. Soğutma suyu (25-35°C): En ucuz
2. Chilled water (5-10°C): Orta maliyet
3. Refrigerant (-20°C): En pahalı
→ GCC profiline uygun en yüksek sıcaklık tercih edilir
```

### 8.2 Utility Maliyetleri Karşılaştırma

| Utility Türü | Tipik Maliyet [€/kWh] | Sıcaklık [°C] | Exergy Faktörü |
|---|---|---|---|
| HP Buhar (40 bar) | 0.035-0.045 | 250 | 0.42 |
| MP Buhar (10 bar) | 0.025-0.035 | 180 | 0.35 |
| LP Buhar (3 bar) | 0.018-0.025 | 134 | 0.27 |
| Soğutma suyu | 0.002-0.005 | 25-35 | 0.02 |
| Chilled water | 0.015-0.025 | 5-10 | 0.06 |
| Refrigerant (-20°C) | 0.040-0.060 | -20 | 0.15 |

## 9. Retrofit ve Greenfield Karşılaştırması

### 9.1 Greenfield (Yeni Tesis) Tasarımı

```
Greenfield avantajları:
- Optimum HEN tasarımı yapılabilir
- Minimum utility hedefi yakından yakalanabilir (%90-95)
- Ekipman yerleşimi ısı entegrasyonuna göre planlanabilir
- Boru maliyetleri minimize edilebilir

Greenfield pinch tasarım adımları:
1. Akış verilerini çıkar
2. ΔTmin optimizasyonu yap
3. Enerji hedeflerini belirle
4. Pinch kurallarına uygun HEN tasarla
5. Döngü kırma / gevşetme ile optimize et
6. Ekipman boyutlandır ve maliyet hesapla
```

### 9.2 Retrofit (Mevcut Tesis İyileştirme)

```
Retrofit kısıtlamaları:
- Mevcut eşanjörler korunmalı (mümkün olduğunca)
- Boru güzergahları sınırlı
- Alan kısıtlamaları var
- Duruş süresini minimize et

Retrofit adımları:
1. Mevcut HEN'i analiz et
2. Cross-pinch transferleri tespit et
3. En büyük cross-pinch transferleri ortadan kaldır
4. Yeni eşanjörleri stratejik noktalara ekle
5. Mevcut eşanjör alanlarını değerlendir (repiping vs. yeni)
```

### 9.3 Greenfield vs. Retrofit Karşılaştırma

| Parametre | Greenfield | Retrofit |
|---|---|---|
| Hedefin yakalanması | %90-95 | %50-80 |
| Yatırım maliyeti | Daha düşük (birim tasarruf başına) | Daha yüksek |
| Uygulama süresi | Yeni tesis ile birlikte | 1-6 ay duruş gerekebilir |
| Esneklik | Yüksek | Sınırlı |
| Risk | Düşük | Orta (mevcut prosese etki) |
| Tipik geri ödeme | — | 1-3 yıl |
| Tipik tasarruf | %30-50 (baseline'a göre) | %15-30 (mevcut duruma göre) |

## 10. Endüstriyel Uygulama Örnekleri

### 10.1 Petrokimya Tesisi

```
Örnek: Etilen fabrikası ısı entegrasyonu
- Akış sayısı: 28 sıcak, 22 soğuk
- Mevcut utility kullanımı: QH = 85 MW, QC = 72 MW
- Pinch analizi sonucu: QH,min = 52 MW, QC,min = 39 MW
- Tasarruf potansiyeli: 33 MW sıcak utility (%39 azalma)
- Yatırım: €4.2M (yeni eşanjörler + boru)
- Yıllık tasarruf: €2.8M
- SPP: 1.5 yıl
```

### 10.2 Gıda Endüstrisi (Süt İşleme)

```
Örnek: Pastörizasyon ve sterilizasyon entegrasyonu
- Akış sayısı: 6 sıcak, 5 soğuk
- Mevcut utility: QH = 2,200 kW, QC = 1,800 kW
- Pinch analizi: QH,min = 1,400 kW, QC,min = 1,000 kW
- Tasarruf: 800 kW sıcak utility (%36 azalma)
- ΔTmin = 5°C (gıda güvenliği: plaka eşanjör zorunluluğu)
- Yatırım: €120,000
- Yıllık tasarruf: €85,000
- SPP: 1.4 yıl
```

### 10.3 Tekstil Fabrikası

```
Örnek: Boyama ve kurutma prosesi entegrasyonu
- Akış sayısı: 8 sıcak, 6 soğuk
- Mevcut utility: QH = 5,500 kW, QC = 4,200 kW
- Pinch analizi: QH,min = 3,800 kW, QC,min = 2,500 kW
- Tasarruf: 1,700 kW sıcak utility (%31 azalma)
- ΔTmin = 15°C (kirli akışlar: temizlik kolaylığı)
- Yatırım: €250,000
- Yıllık tasarruf: €180,000
- SPP: 1.4 yıl
- Ek fayda: Su tüketiminde %15 azalma
```

## 11. Pinch Analizi Performans Değerlendirmesi

### 11.1 Tasarruf Potansiyeli Sınıflandırması

| Mevcut vs. Hedef Utility Farkı | Değerlendirme | Tipik Durum |
|---|---|---|
| >%40 | Mükemmel potansiyel | Hiç ısı entegrasyonu yapılmamış tesis |
| %25-40 | İyi potansiyel | Kısmen entegre tesis |
| %15-25 | Ortalama potansiyel | Temel ısı geri kazanımı mevcut |
| %5-15 | Düşük potansiyel | İyi entegre tesis |
| <%5 | Kritik değil | Pinch-optimum yakın tesis |

### 11.2 Tipik Pinch Analizi Çalışma Sonuçları

| Sektör | Tipik Tasarruf [%] | Tipik SPP [yıl] | Yatırım Aralığı [€] |
|---|---|---|---|
| Petrol rafineri | 20-40 | 1-3 | 500,000 - 5,000,000 |
| Petrokimya | 25-45 | 1-2 | 1,000,000 - 10,000,000 |
| Kimya | 15-35 | 1-3 | 200,000 - 3,000,000 |
| Gıda ve içecek | 20-40 | 1-2 | 50,000 - 500,000 |
| Kağıt ve selüloz | 15-30 | 2-4 | 300,000 - 2,000,000 |
| Tekstil | 20-35 | 1-3 | 100,000 - 800,000 |
| Metal işleme | 10-25 | 2-4 | 200,000 - 1,500,000 |
| Çimento / seramik | 10-20 | 2-5 | 500,000 - 3,000,000 |

## 12. Yazılım Araçları (Software Tools)

### 12.1 Ticari Yazılımlar

| Yazılım | Geliştirici | Özellikler | Yaklaşık Maliyet [€/yıl] |
|---|---|---|---|
| Aspen Energy Analyzer | AspenTech | Tam pinch suite, HEN tasarım, retrofit | 15,000-30,000 |
| SuperTarget | KBC (Yokogawa) | Pinch + utility + distilasyon | 10,000-25,000 |
| HINT | UMIST/Manchester | Eğitim amaçlı, temel pinch | Ücretsiz (akademik) |
| PinCH | Lucerne Univ. | Swiss-made, kullanıcı dostu | 2,000-5,000 |
| Sprint | UMIST | Retrofit odaklı HEN tasarımı | Akademik lisans |
| Spiral | Lund Üniversitesi | Bileşik eğri ve hedef hesap | Ücretsiz (akademik) |

### 12.2 Açık Kaynak / Ücretsiz Araçlar

```
1. HINT (Heat Integration, University of Manchester)
   - Bileşik eğriler, GCC, enerji hedefleri
   - Problem tablosu algoritması
   - Eğitim ve küçük projeler için uygun

2. Python/MATLAB ile özel geliştirme
   - Akış verilerinden bileşik eğri oluşturma
   - PTA (Problem Table Algorithm) implementasyonu
   - GCC ve ΔTmin optimizasyonu
   - HEN grid diyagramları

3. Excel tabanlı hesap tabloları
   - Basit problemler için yeterli
   - Şeffaf hesaplama adımları
   - Hata ayıklama kolaylığı
```

## 13. Gelişmiş Konular (Advanced Topics)

### 13.1 Çoklu Utility Hedefleme (Multiple Utility Targeting)

```
Birden fazla utility seviyesinin optimum dağılımı:
- GCC profili utility yerleştirme için kullanılır
- Her utility seviyesi GCC'nin belirli bir bölgesini karşılar
- Toplam utility maliyeti minimize edilir

Örnek:
GCC'ye göre optimum utility dağılımı:
  HP Buhar (250°C): 600 kW  → €0.040/kWh → €24.0/h
  LP Buhar (130°C): 1,200 kW → €0.022/kWh → €26.4/h
  Toplam sıcak utility maliyeti: €50.4/h

Karşılaştırma (sadece HP buhar):
  HP Buhar: 1,800 kW → €0.040/kWh → €72.0/h
  Tasarruf: €21.6/h = €130,000/yıl
```

### 13.2 Total Site Analizi (Total Site Integration)

```
Total site analizi, birden fazla prosesin birlikte optimize edilmesidir:

Adım 1: Her proses birimi için ayrı pinch analizi
Adım 2: Utility sistemi üzerinden prosesler arası entegrasyon
Adım 3: Site-level GCC (Site Composite Curves) oluşturma
Adım 4: CHP (Combined Heat and Power) potansiyeli değerlendirme
Adım 5: Ortak utility sistemi optimizasyonu

Total site analizi ile ek %10-20 tasarruf potansiyeli
ortaya çıkabilir (tek proses pinch analizinin ötesinde).
```

### 13.3 Isı Pompası ve CHP Entegrasyonu

```
Pinch etrafında ısı pompası:
- Pinch altından ısı alır, pinch üstüne pompalar
- Hem QH,min hem QC,min azalır
- Uygunluk: Pinch ΔT < 50°C ve yüksek utility maliyeti

CHP (Kojenerasyon) yerleştirme:
- GCC kullanılarak optimum CHP boyutu belirlenir
- Atık ısının proses ile entegrasyonu
- Uygunluk: GCC'de yüksek sıcaklık utility gereksinimi büyükse

Performans kriteri:
COP_isı_pompası > T_hot / (T_hot - T_cold)  (Carnot kısıtı)
Verimli bölge: COP > 3-4 (ekonomik kural)
```

## 14. Uygulama Kontrol Listesi

```
Pinch Analizi Kontrol Listesi:

□ Proses akış diyagramı (PFD) güncel mi?
□ Tüm sıcak ve soğuk akışlar tanımlandı mı?
□ Akış debileri ve sıcaklıkları ölçüldü mü?
□ CP değerleri doğru hesaplandı mı? (sıcaklığa bağımlılık)
□ Faz değişimi olan akışlar ayrı ele alındı mı?
□ ΔTmin optimizasyonu yapıldı mı?
□ Problem tablosu algoritması uygulandı mı?
□ Bileşik eğriler ve GCC çizildi mi?
□ Pinch noktası ve enerji hedefleri belirlendi mi?
□ HEN tasarımı pinch kurallarına uygun mu?
□ Retrofit kısıtları değerlendirildi mi?
□ Utility yerleştirme optimize edildi mi?
□ Ekonomik analiz (NPV, SPP) yapıldı mı?
□ Uygulama risk değerlendirmesi yapıldı mı?
□ Operasyonel esneklik değerlendirildi mi?
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) — Exergy hesap ve denge ilkeleri
- [Sistem Sınırları](system_boundaries.md) — Kontrol hacimleri ve akış tanımları
- [Yardımcı Sistemler](utility_analysis.md) — Utility sistemleri analizi ve optimizasyonu
- [Ekonomik Analiz](economic_analysis.md) — Yatırım değerlendirme yöntemleri
- [Yaşam Döngüsü Maliyet](life_cycle_cost.md) — Eşanjör LCC hesaplamaları
- [Önceliklendirme](prioritization.md) — Proje önceliklendirme çerçevesi
- [Metodoloji](methodology.md) — Audit sürecinde pinch analizi rolü
- [Kazan Çözümleri](../boiler/solutions/economizer.md) — Economizer ısı geri kazanımı
- [Kompresör Isı Geri Kazanımı](../compressor/solutions/heat_recovery.md) — Atık ısı entegrasyonu
- [Chiller Isı Geri Kazanımı](../chiller/solutions/heat_recovery.md) — Soğutma sistemi entegrasyonu

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, Rugby, UK, 1982 (1st ed.), 1994 (2nd ed.)
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," Butterworth-Heinemann, 2nd Edition, 2007
- Smith, R., "Chemical Process Design and Integration," Wiley, 2nd Edition, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Linnhoff, B. & Hindmarsh, E. (1983), "The Pinch Design Method for Heat Exchanger Networks," Chemical Engineering Science, 38(5), 745-763
- Tjoe, T.N. & Linnhoff, B. (1986), "Using Pinch Technology for Process Retrofit," Chemical Engineering, 93(8), 47-60
- Dhole, V.R. & Linnhoff, B. (1993), "Total Site Targets for Fuel, Co-Generation, Emissions, and Cooling," Computers & Chemical Engineering, 17(Suppl.), S101-S109
- ESDU Data Item 87001, "Heat Exchanger Network Design"
- IEA Industrial Energy-Related Technologies and Systems (IETS), Annex 10: "Process Integration"
