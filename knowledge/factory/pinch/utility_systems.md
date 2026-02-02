---
title: "Utility Sistemleri ve Optimizasyonu (Utility Systems and Optimization)"
category: factory
equipment_type: factory
keywords: [utility sistemi, çoklu utility, GCC yerleştirme, CHP, ısı pompası, buhar sistemi]
related_files: [factory/pinch/grand_composite.md, factory/pinch/fundamentals.md, factory/pinch/total_site.md, factory/pinch/targeting.md]
use_when: ["Utility sistemi optimize edilirken", "CHP boyutlandırılırken", "Isı pompası değerlendirilirken"]
priority: medium
last_updated: 2026-02-01
---

# Utility Sistemleri ve Optimizasyonu (Utility Systems and Optimization)

> Son güncelleme: 2026-02-01

## Genel Bakis

Utility sistemleri, endüstriyel proseslerin ısıtma ve sogutma ihtiyaçlarını karşılayan dış enerji kaynaklarıdır. Pinch analizinde, Grand Composite Curve (GCC) kullanılarak utility seviyeleri sistematik olarak yerleştirilir, maliyetler minimize edilir ve CHP (Combined Heat and Power) ile ısı pompası (Heat Pump) gibi ileri teknolojilerin entegrasyon potansiyeli belirlenir. Bu dosya, referans problemimizdeki QH,min = 1.800 kW ısıtma ve QC,min = 2.240 kW sogutma ihtiyacının farklı utility seviyeleri arasında nasıl dağıtılacağını ve optimize edileceğini detaylı olarak ele alır.

### Referans Problem Hatırlatma

```
Akis Verileri:
  H1: 270->80°C,  CP=15 kW/°C,  Q=2.850 kW
  H2: 180->40°C,  CP=25 kW/°C,  Q=3.500 kW
  H3: 150->60°C,  CP=10 kW/°C,  Q=900 kW
  C1: 30->250°C,  CP=18 kW/°C,  Q=3.960 kW
  C2: 60->200°C,  CP=12 kW/°C,  Q=1.680 kW

DTmin = 10°C
Pinch: 175°C (shifted) / 180°C (hot) / 170°C (cold)
QH,min = 1.800 kW
QC,min = 2.240 kW
```

---

## 1. Utility Seviyeleri (Utility Levels)

Endüstriyel tesislerde utility'ler sıcaklık seviyelerine ve maliyetlerine göre sınıflandırılır. Uygun seviyenin seçimi enerji maliyetini dogrudan etkiler.

### 1.1 Isıtma Utility'leri (Hot Utilities)

| Utility Türü | Kısaltma | Sıcaklık [°C] | Basınç [bar(g)] | Maliyet [EUR/kWh] | Exergy Faktörü |
|---|---|---|---|---|---|
| Ateşli ısıtıcı (Fired Heater) | FH | 500-1.800 | - | 0,035-0,045 | 0,70-0,85 |
| Yüksek basınç buharı (HP Steam) | HPS | 250-300 | 40-50 | 0,030-0,040 | 0,45-0,55 |
| Orta basınç buharı (MP Steam) | MPS | 175-200 | 8-12 | 0,025-0,032 | 0,35-0,42 |
| Düşük basınç buharı (LP Steam) | LPS | 120-150 | 2-5 | 0,018-0,025 | 0,22-0,30 |
| Sıcak su (Hot Water) | HW | 80-120 | - | 0,012-0,018 | 0,10-0,18 |

```
Maliyet sıralaması (pahalıdan ucuza):
  FH > HPS > MPS > LPS > HW

Exergy kalitesi sıralaması (yüksekten düşüğe):
  FH > HPS > MPS > LPS > HW
```

### 1.2 Sogutma Utility'leri (Cold Utilities)

| Utility Türü | Kısaltma | Sıcaklık [°C] | Maliyet [EUR/kWh] | Exergy Faktörü |
|---|---|---|---|---|
| Sogutma suyu (Cooling Water) | CW | 20-30 | 0,003-0,005 | 0,02-0,05 |
| Hava sogutma (Air Cooling) | AC | 30-40 | 0,004-0,007 | 0,01-0,03 |
| Sogutulmuş su (Chilled Water) | ChW | 5-12 | 0,015-0,025 | 0,08-0,12 |
| Soğutucu akışkan (Refrigeration) | REF | -40 ile +5 | 0,030-0,060 | 0,15-0,35 |
| Kriyojenik (Cryogenic) | CRY | -200 ile -40 | 0,060-0,150 | 0,35-0,70 |

```
Maliyet sıralaması (ucuzdan pahalıya):
  CW < AC < ChW < REF < CRY

Genel kural: Mumkun olan en ucuz utility seviyesini kullan.
             Daha ucuz utility = Daha düşük exergy kaybı
```

### 1.3 Sıcaklık-Maliyet İlişkisi

```
Maliyet     |
[EUR/kWh]   |
  0,15  -   |                                                  * CRY
            |
  0,10  -   |
            |
  0,06  -   |                                        * REF
  0,04  -   |                              * FH
  0,03  -   |                     * HPS
  0,025 -   |              * MPS  |
  0,02  -   |       * LPS  |     * ChW
  0,01  -   |  * HW  |     |
  0,005 -   |  | * CW |    |
            |__|__|___|____|________________________________
              0  50  150  250  500         Sıcaklık [°C]

Kural: Ortam sıcaklığından (T0 ~ 25°C) uzaklaştıkça
       utility maliyeti artar.
```

---

## 2. GCC ile Utility Yerleştirme (Utility Placement with GCC)

Grand Composite Curve (GCC), utility yerleştirme için en önemli araçtır. GCC'nin "cepleri" (pockets) proses-proses ısı geri kazanımını, açık kalan bölgeleri ise utility ihtiyacını gösterir.

### 2.1 GCC Oluşturma Hatırlatma

GCC, kaydırılmış sıcaklık (shifted temperature) ile net ısı akısı (net heat flow) arasındaki ilişkiyi gösterir. Pinch noktasında net akıs sıfırdır.

```
Referans Problemin GCC Profili (basitleştirilmiş):

Shifted T [°C]
    |
265 +..........*                          <-- QH,min = 1.800 kW gerekli
    |         /
245 +        /
    |       /
215 +      /
    |     |
195 +     |
    |    /
175 +---*------------- Pinch noktası (net akis = 0)
    |    \
135 +     \
    |      \    *-- Isı cebi (pocket): proses-proses geri kazanım
115 +       \ /
    |        *
 85 +       /
    |      /
 55 +     /
    |    /
 35 +...*                                 <-- QC,min = 2.240 kW gerekli
    |
    +------+------+------+------+------
    0     500   1000   1500   2000   2500
                    Net Isı Akısı [kW]
```

### 2.2 Utility Yerleştirme Prensibi

**Temel Kural:** En ucuz utility'yi mumkun oldugunca çok kullan, pahalı utility'ye yalnızca zorunluyken geç.

**Isıtma tarafı (GCC'nin pinch üstü):**
1. GCC profilini en ucuz sıcak utility ile karşılamaya çalış
2. Utility sıcaklığı GCC'nin ihtiyaç duyduğu sıcaklığa ulaşamıyorsa, bir üst seviyeye geç
3. Utility'yi GCC'ye yatay bir çizgi olarak (sabit sıcaklıkta faz değişimi) veya eğimli bir çizgi olarak (duyulur ısı) yerleştir

**Sogutma tarafı (GCC'nin pinch altı):**
1. En ucuz sogutma utility'si ile başla (genellikle sogutma suyu)
2. Düşük sıcaklık gerektiren bölgelerde daha pahalı utility'lere geç

### 2.3 Referans Problem Uzerinde Utility Yerleştirme

Referans problemde QH,min = 1.800 kW ısıtma gereklidir. GCC profilini inceleyelim:

```
Pinch üstü GCC analizi:
  - GCC, 175°C (shifted) ile 265°C (shifted) arasında ısıtma gerektirir
  - Gerçek sıcaklıklar: 180°C ile 270°C arası (soğuk akış tarafı)
  - En düşük ihtiyaç noktası: ~185°C shifted (~190°C gerçek)
  - En yüksek ihtiyaç noktası: 265°C shifted (~270°C gerçek)
```

**Senaryo A: Tek utility (yalnızca HPS)**

HPS 250°C'de doymuş buhar sağlar. Shifted sıcaklık: 245°C.

```
GCC üzerinde HPS yerleştirme:
  - HPS (245°C shifted): GCC'nin 175-245°C shifted aralığını karşılar
  - Ancak GCC 245°C'nin üzerinde de ısıtma gerektirir
  - 245-265°C shifted aralığı icin: ~420 kW ilave gerekli
  - Bu bölge icin ateşli ısıtıcı (FH) veya kızgın yağ gerekir

Sonuç:
  QH_HPS = 1.380 kW (HPS ile karşılanan)
  QH_FH  =   420 kW (FH ile karşılanan)
  Toplam = 1.800 kW = QH,min  (doğrulama tamam)
```

**Senaryo B: Çoklu utility (MPS + HPS)**

MPS 190°C'de (shifted: 185°C), HPS 250°C'de doymuş buhar sağlar.

```
GCC üzerinde çoklu utility yerleştirme:

Shifted T [°C]
    |
265 +..........========== FH (gerekirse)
    |         /
245 +========/========== HPS (250°C, shifted 245°C)
    |       /
215 +      /
    |     |
195 +     |
    |    /
185 +====/=============== MPS (190°C, shifted 185°C)
175 +---*------------- Pinch
    |
    === : Utility seviyesi (yatay yerleştirme)

Dağılım:
  QH_MPS = 680 kW  (MPS: 185°C shifted seviyesinde)
  QH_HPS = 700 kW  (HPS: 245°C shifted seviyesinde)
  QH_FH  = 420 kW  (FH: 265°C üzeri)
  Toplam = 1.800 kW = QH,min
```

### 2.4 Sogutma Tarafı Yerleştirme

Referans problemde QC,min = 2.240 kW sogutma gereklidir.

```
Pinch altı GCC analizi:
  - GCC, 175°C (shifted) ile 35°C (shifted) arasında sogutma gerektirir
  - Sogutma suyu (CW): 25°C giriş / 35°C çıkış, shifted ~30°C
  - Tüm sogutma ihtiyacı CW ile karşılanabilir (en düşük GCC noktası ~35°C shifted)

Sonuç:
  QC_CW = 2.240 kW (tamamı sogutma suyu ile)
  Toplam maliyet: 2.240 x 0,004 = 8,96 EUR/h
```

---

## 3. Çoklu Utility Hedefleme (Multiple Utility Targeting)

### 3.1 Maliyet Minimizasyon Prensibi

Çoklu utility hedeflemede amaç, toplam utility maliyetini minimize etmektir:

```
Toplam Maliyet = SUM(Qi x Ci)    [EUR/h]

Burada:
  Qi = i. utility seviyesinin ısı yükü [kW]
  Ci = i. utility seviyesinin birim maliyeti [EUR/kWh]

Kısıtlar:
  SUM(QH,i) = QH,min     (toplam ısıtma hedefi karşılanmalı)
  SUM(QC,j) = QC,min     (toplam sogutma hedefi karşılanmalı)
  Qi >= 0                 (negatif yük olamaz)
  GCC profili ihlal edilmemeli (utility GCC'nin icine girmemeli)
```

### 3.2 GCC-Tabanlı Dağıtım Algoritması

Adım 1: GCC'yi oluştur (shifted sıcaklık vs net ısı akısı)
Adım 2: En ucuz ısıtma utility'sini GCC'ye yerleştir
Adım 3: Karşılanamayan bölge varsa bir üst seviye utility ekle
Adım 4: Tüm ısıtma karşılanıncaya kadar tekrarla
Adım 5: Sogutma tarafı icin aynı işlemi uygula (en ucuzdan başla)

### 3.3 Sayısal Ornek: Maliyet Karşılaştırma

Referans problem icin üç farklı senaryo:

**Senaryo 1: Tek HPS + CW**
```
Isıtma: QH_HPS = 1.800 kW @ 0,035 EUR/kWh
Sogutma: QC_CW = 2.240 kW @ 0,004 EUR/kWh

Toplam maliyet = (1.800 x 0,035) + (2.240 x 0,004)
               = 63,00 + 8,96
               = 71,96 EUR/h
               = 575.680 EUR/yıl (8.000 h/yıl)
```

**Senaryo 2: MPS + HPS + CW (optimum dağılım)**
```
Isıtma: QH_MPS =   680 kW @ 0,028 EUR/kWh
        QH_HPS =   700 kW @ 0,035 EUR/kWh
        QH_FH  =   420 kW @ 0,040 EUR/kWh
Sogutma: QC_CW  = 2.240 kW @ 0,004 EUR/kWh

Toplam maliyet = (680 x 0,028) + (700 x 0,035) + (420 x 0,040) + (2.240 x 0,004)
               = 19,04 + 24,50 + 16,80 + 8,96
               = 69,30 EUR/h
               = 554.400 EUR/yıl
```

**Senaryo 3: LPS + MPS + HPS + CW (maksimum dağılım)**
```
NOT: LPS 140°C (shifted 135°C) — Pinch altında kalır!
     LPS kullanılamaz (Pinch üstü ısıtma 175°C shifted'dan başlar)

Sonuç: Bu senaryoda LPS yerleştirilemez.
       Pinch sıcaklığı LPS'nin ulaşabildiğinden yüksek.
```

**Karşılaştırma tablosu:**

| Senaryo | Utility Dağılımı | Yıllık Maliyet [EUR] | Tasarruf |
|---|---|---|---|
| 1 | Tek HPS | 575.680 | Referans |
| 2 | MPS + HPS + FH | 554.400 | %3,7 |
| 3 | LPS eklenemez | - | - |

### 3.4 Exergy Perspektifi

```
Utility exergy verimi = (Prosesin minimum exergy ihtiyacı) / (Sağlanan utility exergy'si)

Senaryo 1 (Tek HPS):
  Sağlanan exergy = 1.800 x 0,50 = 900 kW (exergy)
  Proses minimum exergy ihtiyacı ~ 620 kW (GCC'den hesaplanan)
  Exergy verimi = 620 / 900 = %68,9

Senaryo 2 (MPS + HPS + FH):
  Sağlanan exergy = (680 x 0,38) + (700 x 0,50) + (420 x 0,75) = 258 + 350 + 315 = 923 kW
  Exergy verimi = 620 / 923 = %67,2

Not: Senaryo 2 maliyet olarak daha ucuz, ancak FH nedeniyle exergy verimi
     biraz düşük. Burada maliyet-exergy dengesi kurulmalıdır.
```

---

## 4. Buhar Sistemi Optimizasyonu (Steam System Optimization)

### 4.1 Buhar Seviyeleri ve Entegrasyon

Endüstriyel tesislerde buhar sistemi genellikle 3-4 basınç seviyesinden oluşur:

```
Buhar Sistemi Şeması:

  Kazan (Boiler)
    |
    v
  ===== HPS (40-50 bar, 250-300°C) =====
    |                                  |
    | Letdown /                        | Proses
    | Türbin                           | Kullanımı
    v                                  v
  ===== MPS (8-12 bar, 175-195°C) =====
    |                                  |
    | Letdown /                        | Proses
    | Türbin                           | Kullanımı
    v                                  v
  ===== LPS (2-5 bar, 120-155°C) ======
    |                                  |
    | Proses                           | Isıtma /
    | Kullanımı                        | Deaerator
    v                                  v
  ===== Kondensat Dönüşü ==============
    |
    v
  Deaerator --> Kazan Besleme Suyu
```

### 4.2 Letdown ve Venting Analizi

**Letdown (Basınç Düşürme):**
Buharın türbin yerine kısılma vanası (throttling valve) ile düşürülmesi exergy kaybına neden olur.

```
Kısılma vanası ile exergy kaybı:
  Ex_kayıp = m_buhar x T0 x (s2 - s1)    [kW]

Burada:
  m_buhar = buhar debisi [kg/s]
  T0      = ortam sıcaklığı [K] = 298 K
  s1      = giriş entropisi [kJ/(kg·K)]
  s2      = çıkış entropisi [kJ/(kg·K)]

Ornek: HPS -> MPS kısılma
  HPS: 40 bar doymuş buhar, s1 = 6,070 kJ/(kg·K)
  MPS: 10 bar, s2 = 6,290 kJ/(kg·K) (kısılma: h1 = h2)
  m_buhar = 2,0 kg/s

  Ex_kayıp = 2,0 x 298 x (6,290 - 6,070) = 131,1 kW

  Bu kayıp, bir geri basınç türbini ile elektrik üretimine
  dönüştürülebilir.
```

**Venting (Buhar Bırakma):**
Fazla buharın atmosfere bırakılması hem enerji hem exergy kaybıdır.

```
Venting kaybı:
  Q_kayıp = m_vent x h_fg    [kW]
  Ex_kayıp = m_vent x ex_buhar [kW]

Ornek: 0,5 kg/s LPS venting
  h_fg (3 bar) = 2.163 kJ/kg
  ex_buhar (3 bar doymuş) = 640 kJ/kg

  Q_kayıp  = 0,5 x 2.163 = 1.081 kW
  Ex_kayıp = 0,5 x 640   = 320 kW

  Yıllık kayıp: 320 x 8.000 x 0,025 = 64.000 EUR/yıl
```

### 4.3 Deaerator Entegrasyonu

Deaerator (hava giderici), kazan besleme suyundan çözünmüş gazları uzaklaştırır. LPS kullanarak çalışır ve pinch analizinde soguk akış olarak modellenir.

```
Deaerator parametreleri:
  Giriş suyu sıcaklığı:   80°C (kondensat + taze su karışımı)
  Çıkış suyu sıcaklığı:   105°C (LPS basıncında kaynama)
  LPS ihtiyacı:           0,3-0,8 kg/s (tesis büyüklüğüne bağlı)

Pinch entegrasyonu:
  Deaerator ihtiyacı, pinch altında kalıyorsa (T_deaerator < T_pinch),
  proses atık ısısı ile karşılanabilir --> LPS tasarrufu
```

---

## 5. CHP Entegrasyonu (Combined Heat and Power Integration)

### 5.1 Uygun Yerleştirme Prensibi (Appropriate Placement Principle)

Townsend ve Linnhoff (1983) tarafından geliştirilen bu prensip, CHP sistemlerinin pinch analizine nasıl entegre edileceğini tanımlar:

```
KURAL: CHP sistemi, pinch noktasının ÜSTÜNDE ısı sağlamalı
       ve pinch noktasının ÜSTÜNDE iş (elektrik) üretmelidir.

Doğru Yerleştirme (Appropriate Placement):

  Yakıt --> [CHP] --> Elektrik (W)
              |
              v
         Isı (Q_CHP) --> Pinch ÜSTÜ prosesler

  Bu durumda:
  - Yakıt enerjisi hem ısıya hem elektriğe dönüşür
  - Prosesin dış ısıtma ihtiyacı azalır
  - Toplam yakıt tüketimi düşer

Yanlış Yerleştirme:

  Yakıt --> [CHP] --> Elektrik (W)
              |
              v
         Isı (Q_CHP) --> Pinch ALTI prosesler

  Bu durumda:
  - CHP'den gelen ısı gereksizdir (pinch altı zaten ısı fazlası)
  - Sogutma yükü artar
  - Ekonomik ve termodinamik kayıp
```

### 5.2 GCC ile CHP Boyutlandırma

GCC profili, CHP sisteminin maksimum entegrasyon potansiyelini gösterir.

```
CHP Boyutlandırma Adımları:

Adım 1: GCC'nin pinch üstü bölümünü çiz
Adım 2: CHP'nin ısı çıkısı sıcaklığını belirle (MPS veya LPS seviyesi)
Adım 3: GCC profili ile utility seviyesi arasındaki alanı hesapla
Adım 4: Bu alan = CHP'den sağlanacak maksimum ısı (Q_CHP,max)
Adım 5: CHP kapasitesini ve elektrik üretimini hesapla

Referans problem üzerinde:

  QH,min = 1.800 kW (toplam ısıtma ihtiyacı)
  GCC'den: 185°C shifted seviyesine kadar = 680 kW (MPS olarak)
           245°C shifted seviyesine kadar = 1.380 kW (MPS + HPS)
           265°C shifted üzeri = 420 kW (FH)
```

### 5.3 Geri Basınç Türbini vs Ara Çekiş Türbini

**Geri Basınç Türbini (Back-Pressure Turbine):**

```
  HPS (40 bar) --> [Türbin] --> MPS (10 bar)
                      |
                      v
                  Elektrik (W)

Özellikler:
  - Basit yapı, düşük maliyet
  - Elektrik/ısı oranı sabit (tipik 0,15-0,25)
  - Elektrik üretimi ısı talebine bağlı
  - Küçük-orta tesisler icin uygun

Hesaplama:
  W_türbin = m_buhar x (h_HPS - h_MPS)   [kW]
  Q_MPS    = m_buhar x (h_MPS - h_kondensat)  [kW]
  eta_iso  = (h_HPS - h_MPS,gerçek) / (h_HPS - h_MPS,ideal)

Ornek:
  m_buhar = 2,5 kg/s
  h_HPS (40 bar, 400°C) = 3.214 kJ/kg
  h_MPS,ideal (10 bar, s=sabit) = 2.820 kJ/kg
  eta_iso = 0,80

  W_türbin = 2,5 x (3.214 - 2.820) x 0,80 = 788 kW (elektrik)
  Q_MPS = 2,5 x (2.820 - 505) = 5.788 kW (proses ısısı, kondensat 120°C)
  CHP verimi = (788 + 5.788) / (2,5 x 3.214) = %81,8
```

**Ara Çekiş Türbini (Extraction Turbine):**

```
  HPS (40 bar) --> [Türbin Kademe 1] --> MPS çekiş (10 bar)
                                    |
                                    --> [Türbin Kademe 2] --> LPS (3 bar)
                                              |
                                              v
                                          Elektrik (W)

Özellikler:
  - Esnek çalışma, farklı buhar seviyeleri
  - Elektrik/ısı oranı ayarlanabilir
  - Karmaşık kontrol
  - Orta-büyük tesisler icin uygun
  - Daha yüksek yatırım maliyeti
```

### 5.4 CHP Entegrasyon Değerlendirmesi

```
CHP ekonomik değerlendirme:

  Yıllık elektrik üretim değeri:
  E_değer = W_türbin x t_çalışma x C_elektrik   [EUR/yıl]

  Yıllık ilave yakıt maliyeti:
  F_maliyet = (Q_CHP,yakıt - Q_sadece_kazan) x C_yakıt  [EUR/yıl]

  Net tasarruf = E_değer - F_maliyet

Referans problem icin CHP değerlendirmesi:
  W_türbin = 788 kW
  t_çalışma = 8.000 h/yıl
  C_elektrik = 0,12 EUR/kWh
  C_yakıt_artış = 1.500 kW ilave yakıt @ 0,035 EUR/kWh

  E_değer = 788 x 8.000 x 0,12 = 756.480 EUR/yıl
  F_maliyet = 1.500 x 8.000 x 0,035 = 420.000 EUR/yıl
  Net tasarruf = 756.480 - 420.000 = 336.480 EUR/yıl

  Yatırım maliyeti ~ 800.000 EUR (geri basınç türbini)
  Geri ödeme süresi = 800.000 / 336.480 = 2,4 yıl
```

---

## 6. Isı Pompası Yerleştirme (Heat Pump Placement)

### 6.1 Pinch Boyunca Yerleştirme Prensibi (Across-Pinch Principle)

Isı pompası, termodinamik olarak anlamlı olması icin pinch noktasının her iki tarafında da çalışmalıdır.

```
Doğru Yerleştirme (Across the Pinch):

  Pinch ALTI          Pinch ÜSTÜ
  (ısı fazlası)       (ısı açığı)
       |                    ^
       | Q_evap             | Q_cond
       v                    |
    [Evaporatör] --> [W] --> [Kondenser]
                  Isı Pompası

  Q_cond = Q_evap + W
  COP_hp = Q_cond / W

  Avantaj:
  - Pinch altındaki fazla ısıyı pinch üstüne aktarır
  - Hem QH,min hem QC,min azalır
  - DQ_H = Q_cond (ısıtma utility tasarrufu)
  - DQ_C = Q_evap (sogutma utility tasarrufu)

Yanlış Yerleştirme (Tamamen pinch üstü veya altı):

  Pinch üstü (her iki uç):
  - Enerji tasarrufu yok, W kadar ilave harcama
  - Isı yalnızca pinch üstünde dolaşır

  Pinch altı (her iki uç):
  - Enerji tasarrufu yok, W kadar ilave sogutma
  - Isı yalnızca pinch altında dolaşır
```

### 6.2 COP Gereksinimleri ve Ekonomik Uygunluk

Isı pompasının ekonomik olarak uygulanabilir olması icin minimum COP değeri hesaplanmalıdır:

```
Ekonomik uygunluk kriteri:

  COP_min = C_elektrik / (C_utility_ısıtma - C_utility_sogutma)

  Burada:
  C_elektrik = elektrik birim maliyeti [EUR/kWh]
  C_utility_ısıtma = tasarruf edilen ısıtma utility maliyeti [EUR/kWh]
  C_utility_sogutma = tasarruf edilen sogutma utility maliyeti [EUR/kWh]

Referans problem icin:
  C_elektrik = 0,12 EUR/kWh
  C_utility_ısıtma (MPS) = 0,028 EUR/kWh
  C_utility_sogutma (CW) = 0,004 EUR/kWh

  COP_min = 0,12 / (0,028 - 0,004) = 0,12 / 0,024 = 5,0

  Gerekli COP >= 5,0 --> oldukça yüksek!
```

### 6.3 GCC-Tabanlı Isı Pompası Boyutlandırma

```
GCC üzerinde ısı pompası yerleştirme:

Shifted T [°C]
    |
265 +..........*
    |         /
245 +        /
    |       /
215 +      /
    |     |
195 +     |
    |    /
175 +---*------------- Pinch
    |    \
135 +     \
    |      *---+
115 +     /    |
    |    *     | Q_evap (pinch altından alınan ısı)
 85 +   /     |
    |  /      |
 55 + /       |
    |/        |
 35 +*--------+

Isı pompası sıcaklık aralığı:
  T_evap: ~130°C shifted (pinch altı, GCC cebi dibinden)
  T_cond: ~185°C shifted (pinch üstü, MPS seviyesi)
  DT_lift = 185 - 130 = 55°C

Carnot COP:
  COP_Carnot = T_cond / (T_cond - T_evap) = (185+273) / 55 = 8,33

Gerçek COP (eta = 0,50):
  COP_gerçek = 0,50 x 8,33 = 4,17

COP_gerçek (4,17) < COP_min (5,0) --> Isı pompası ekonomik değil!
```

### 6.4 Isı Pompası Uygunluk Karar Ağacı

```
Isı pompası uygulanmalı mı?

  [1] GCC'de pinch boyunca geçiş var mı?
       |
    Evet --> [2] DT_lift < 50°C mi?
       |          |
       |       Evet --> [3] COP_gerçek > COP_min mi?
       |          |          |
       |          |       Evet --> [4] Yıllık tasarruf > Yatırım/3 mi?
       |          |          |          |
       |          |          |       Evet --> UYGULA
       |          |          |          |
       |          |          |       Hayır --> Beklemeye al
       |          |          |
       |          |       Hayır --> MVR veya AHP değerlendir
       |          |
       |       Hayır --> Ekonomik değil, CHP değerlendir
       |
    Hayır --> Isı pompası uygulanamaz

Not: MVR = Mekanik Buhar Sıkıştırma (Mechanical Vapor Recompression)
     AHP = Absorpsiyonlu Isı Pompası (Absorption Heat Pump)
```

---

## 7. Sogutma Sistemi Optimizasyonu (Cooling System Optimization)

### 7.1 Sogutma Utility Seçim Matrisi

| Proses Sıcaklığı | Önerilen Utility | Tipik DT | Açıklama |
|---|---|---|---|
| > 100°C | Sogutma suyu (CW) | 10-20°C | En ekonomik, ilk tercih |
| 60-100°C | Sogutma suyu (CW) | 10-20°C | Standart uygulama |
| 40-60°C | CW veya Hava sogutma (AC) | 15-30°C | Maliyet karşılaştırması yap |
| 20-40°C | Sogutulmuş su (ChW) | 5-10°C | Maliyet 3-5x CW |
| 0-20°C | Sogutulmuş su (ChW) | 5-10°C | Sogutma grubu gerekli |
| -20 ile 0°C | Soğutucu akışkan (REF) | 5-10°C | Maliyet 8-15x CW |
| < -20°C | Kaskad soğutma (CAS) | 5-15°C | Yüksek yatırım ve işletme maliyeti |

### 7.2 Referans Problem Sogutma Analizi

```
Pinch altı sogutma ihtiyacı: QC,min = 2.240 kW

GCC'den sogutma profili:
  - Sogutma 175°C shifted ile 35°C shifted arasında gerekli
  - Tüm sıcaklıklar CW erişim aralığında (> 30°C)
  - Tek CW seviyesi yeterli

Sogutma suyu hesabı:
  CW giriş: 25°C, CW çıkış: 35°C (DT_CW = 10°C)
  m_CW = QC,min / (Cp x DT_CW) = 2.240 / (4,18 x 10) = 53,6 kg/s

  Yıllık su maliyeti: 53,6 x 3.600 x 8.000 / 1.000 x 0,001 = 1.544 m3/h
  (Evaporasyon + blowdown ile toplam taze su ihtiyacı)
```

### 7.3 Hava Sogutma Değerlendirmesi

```
Hava sogutma avantajları:
  - Su tüketimi yok
  - Legionella riski yok
  - Düşük bakım maliyeti

Hava sogutma dezavantajları:
  - Büyük alan gereksinimi (CW kuleye göre 5-10x)
  - Ortam sıcaklığına bağımlılık
  - Daha yüksek yaklaşım sıcaklığı (DT_min,hava = 15-25°C)
  - Fan enerji tüketimi

Ekonomik karşılaştırma (2.240 kW sogutma icin):
  Sogutma suyu: ~8,96 EUR/h (pompa + kule + su)
  Hava sogutma: ~11,20 EUR/h (fan enerji + amortisman)

  Bu senaryoda CW daha ekonomik.
```

---

## 8. Utility Maliyet Karşılaştırma (Utility Cost Comparison)

### 8.1 Kapsamlı Maliyet Tablosu

| Utility | Sıcaklık [°C] | Birim Maliyet [EUR/kWh] | Exergy Faktörü [-] | CO2 Emisyonu [kg/kWh_th] | Yenilenebilir Uyum |
|---|---|---|---|---|---|
| **Isıtma Utility'leri** | | | | | |
| Ateşli ısıtıcı (FH) | 500-1.800 | 0,035-0,045 | 0,70-0,85 | 0,20-0,28 | Düşük |
| HP buhar (HPS) | 250-300 | 0,030-0,040 | 0,45-0,55 | 0,18-0,25 | Orta (biyokütle) |
| MP buhar (MPS) | 175-200 | 0,025-0,032 | 0,35-0,42 | 0,15-0,20 | Orta |
| LP buhar (LPS) | 120-150 | 0,018-0,025 | 0,22-0,30 | 0,10-0,15 | Yüksek |
| Sıcak su (HW) | 80-120 | 0,012-0,018 | 0,10-0,18 | 0,07-0,12 | Yüksek (güneş) |
| **Sogutma Utility'leri** | | | | | |
| Sogutma suyu (CW) | 20-30 | 0,003-0,005 | 0,02-0,05 | 0,002-0,004 | Yüksek |
| Hava sogutma (AC) | 30-40 | 0,004-0,007 | 0,01-0,03 | 0,003-0,005 | Yüksek |
| Sogutulmuş su (ChW) | 5-12 | 0,015-0,025 | 0,08-0,12 | 0,010-0,018 | Orta |
| Soğutucu akışkan (REF) | -40 ile +5 | 0,030-0,060 | 0,15-0,35 | 0,025-0,050 | Düşük |
| Kriyojenik (CRY) | -200 ile -40 | 0,060-0,150 | 0,35-0,70 | 0,050-0,120 | Çok düşük |

### 8.2 Referans Problem Icin Toplam Utility Maliyeti Ozeti

```
Optimal Utility Konfigürasyonu:
  Isıtma: MPS (680 kW) + HPS (700 kW) + FH (420 kW)
  Sogutma: CW (2.240 kW)
  CHP: Geri basınç türbini (788 kW_e)

Yıllık Maliyet Dağılımı (8.000 h/yıl):

  Kalem                    Maliyet [EUR/yıl]    Pay [%]
  ─────────────────────────────────────────────────────
  FH (420 kW)                134.400             17,4
  HPS (700 kW)               196.000             25,4
  MPS (680 kW)               152.320             19,7
  CW (2.240 kW)               71.680              9,3
  CHP elektrik geliri        -756.480           (tasarruf)
  CHP ilave yakıt             420.000             54,4
  Bakım + işletme (CHP)       55.000              7,1
  ─────────────────────────────────────────────────────
  TOPLAM (CHP dahil)         272.920             %35,3*
  TOPLAM (CHP hariç)         554.400            %100,0

  * Referansa göre (%100 = CHP'siz toplam)

  CHP ile net tasarruf: 554.400 - 272.920 = 281.480 EUR/yıl (%50,8)
```

### 8.3 Exergy Bazlı Utility Değerlendirme

```
Exergy verimi karşılaştırması:

  Utility         QH [kW]  Exergy [kW]  Exergy Verim [%]  Maliyet/Exergy
  ────────────────────────────────────────────────────────────────────────
  FH (tek)         1.800      1.350           46,0          0,047 EUR/kW_ex
  HPS (tek)        1.800        900           68,9          0,035 EUR/kW_ex
  MPS+HPS+FH       1.800        923           67,2          0,031 EUR/kW_ex
  CHP+MPS+HPS      1.800        923           67,2          0,015 EUR/kW_ex*

  * CHP ile elektrik geliri düşüldükten sonra

Sonuç: CHP entegrasyonu ile exergy başına maliyet %57 düşer.
```

### 8.4 CO2 Emisyon Karşılaştırması

```
Yıllık CO2 emisyonu (8.000 h/yıl):

  Senaryo                  Yakıt [kW]   CO2 [ton/yıl]
  ───────────────────────────────────────────────────
  Tek HPS                   2.250*         3.960
  MPS+HPS+FH                2.250*         4.050**
  CHP entegreli             3.750          3.300***

  * Kazan verimi %80 varsayımı ile
  ** FH'nin daha yüksek emisyon faktörü nedeniyle
  *** CHP elektrik üretimi şebeke emisyonunu azaltır
       (0,45 kg CO2/kWh_e şebeke ortalaması ile)

CHP ile net CO2 azaltma: 3.960 - 3.300 = 660 ton/yıl (%16,7)
```

---

## Utility Optimizasyon Kontrol Listesi

```
[ ] 1. GCC profilini oluştur ve ısı ceplerini belirle
[ ] 2. Mevcut utility seviyelerini ve sıcaklıklarını listele
[ ] 3. Her utility seviyesini GCC'ye yerleştir (en ucuzdan başla)
[ ] 4. Çoklu utility dağılımının maliyet optimumunu hesapla
[ ] 5. Buhar sistemi letdown ve venting kayıplarını analiz et
[ ] 6. CHP entegrasyon potansiyelini değerlendir (uygun yerleştirme)
[ ] 7. Isı pompası fizibilitesini kontrol et (COP > COP_min)
[ ] 8. Sogutma sistemi optimizasyonunu yap (en ucuz utility)
[ ] 9. Exergy bazlı değerlendirme yap (maliyet/exergy oranı)
[ ] 10. CO2 emisyon etkisini hesapla
[ ] 11. Yatırım-geri dönüş analizi yap (NPV, IRR)
[ ] 12. Sonuçları raporla ve uygulama planı oluştur
```

---

## Formül Özet Tablosu

| Parametre | Formül | Birim |
|---|---|---|
| Utility maliyeti | C_toplam = SUM(Qi x Ci) | EUR/h |
| Letdown exergy kaybı | Ex_kayıp = m x T0 x (s2 - s1) | kW |
| CHP elektrik üretimi | W = m x (h1 - h2) x eta_iso | kW |
| CHP verimi | eta_CHP = (W + Q) / Q_yakıt | - |
| Isı pompası COP | COP = Q_cond / W_kompresör | - |
| Carnot COP | COP_C = T_cond / (T_cond - T_evap) | - |
| Minimum COP | COP_min = C_e / (C_h - C_c) | - |
| Sogutma suyu debisi | m_CW = Q / (Cp x DT) | kg/s |
| Exergy faktörü | f_ex = 1 - T0/T_utility | - |
| CO2 emisyon | E_CO2 = Q_yakıt x EF | kg/h |

---

## İlgili Dosyalar

- [Grand Composite Curve](grand_composite.md) -- GCC oluşturma, ısı cebi analizi, utility yerleştirme temeli
- [Pinch Analizi Temelleri](fundamentals.md) -- Linnhoff metodolojisi, pinch kuralları, MER hedefleri
- [Total Site Analizi](total_site.md) -- Çoklu proses entegrasyonu, site profilleri, buhar seviye optimizasyonu
- [Hedefleme](targeting.md) -- Enerji, alan ve maliyet hedefleri, Bath formülü
- [Pinch Analizi Ana Dosyası](../pinch_analysis.md) -- Temel kavramlar ve hesaplamalar
- [Isı Entegrasyonu](../heat_integration.md) -- Kaynak-kullanım eşleştirme
- [Kojenerasyon](../cogeneration.md) -- CHP sistemleri detaylı analiz
- [Atık Isı Geri Kazanımı](../waste_heat_recovery.md) -- Atık ısı değerlendirme yöntemleri
- [Çapraz Ekipman Analizi](../cross_equipment.md) -- Ekipmanlar arası fırsatlar

## Referanslar

- Linnhoff, B. et al., "User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1994
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," 2nd Ed., Butterworth-Heinemann, 2007
- Smith, R., "Chemical Process Design and Integration," 2nd Ed., Wiley, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration: Minimisation of Energy and Water Use, Waste and Emissions," Woodhead Publishing, 2013
- Townsend, D.W. and Linnhoff, B., "Heat and Power Networks in Process Design. Part I: Criteria for Placement of Heat Engines and Heat Pumps in Process Networks," AIChE Journal, 29(5), pp. 742-748, 1983
- Linnhoff, B. and Hindmarsh, E., "The Pinch Design Method for Heat Exchanger Networks," Chemical Engineering Science, 38(5), pp. 745-763, 1983
- Maréchal, F. and Kalitventzeff, B., "Targeting the Integration of Multi-Period Utility Systems for Site Scale Process Integration," Applied Thermal Engineering, 23(14), pp. 1763-1784, 2003
