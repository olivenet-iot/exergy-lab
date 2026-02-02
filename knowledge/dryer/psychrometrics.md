---
title: "Nemli Hava Termodinamiği ve Psikrometri (Psychrometrics and Moist Air Thermodynamics)"
category: dryer
equipment_type: dryer
keywords: [psikrometri, nemli hava, kurutma, mutlak nem, bağıl nem, entalpi, doyma basıncı, Mollier diyagramı, exergy, yaş termometre, çiğ noktası, Antoine denklemi, ASHRAE, hava geri deviri, recirculation, adyabatik kurutma, kimyasal exergy, termal exergy]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/solutions/air_recirculation.md, dryer/solutions/exhaust_heat_recovery.md]
use_when: ["Kurutma havası hesaplamaları yapılırken", "Nemli hava exergy analizi gerektiğinde", "Psikrometrik süreç analizi yapılırken", "Kurutma prosesi optimize edilirken", "Hava geri devir oranı belirlenirken", "Doyma basıncı ve çiğ noktası hesaplanırken"]
priority: high
last_updated: 2026-02-01
---
# Nemli Hava Termodinamiği ve Psikrometri (Psychrometrics and Moist Air Thermodynamics)

> Son güncelleme: 2026-02-01

## Giriş

Endüstriyel kurutma proseslerinde hava, hem enerji taşıyıcı hem de nem taşıyıcı olarak görev yapar.
Psikrometri (psychrometrics), nemli havanın termodinamik özelliklerini inceleyen bilim dalıdır ve
kurutma sistemlerinin doğru tasarımı, analizi ve optimizasyonu için temel oluşturur.

Exergy analizi açısından nemli havanın önemi büyüktür: kurutma havası hem termal exergy (sıcaklık farkı)
hem de kimyasal exergy (nem konsantrasyonu farkı) taşır. Bu iki bileşenin doğru hesaplanması,
kurutma sisteminin gerçek termodinamik performansını ortaya koyar.

---

## 1. Nemli Hava Özellikleri (Moist Air Properties)

### 1.1 Mutlak Nem (Humidity Ratio, w)

Mutlak nem (humidity ratio), kuru hava başına düşen su buharı kütlesidir:

```
w = m_v / m_a = 0.622 × Pw / (P - Pw)   [kg_su / kg_kuru_hava]

Burada:
- m_v   = su buharı kütlesi [kg]
- m_a   = kuru hava kütlesi [kg]
- Pw    = su buharı kısmi basıncı [Pa]
- P     = toplam basınç [Pa] (standart atmosfer: 101325 Pa)
- 0.622 = M_w / M_a = 18.015 / 28.964 (mol kütlesi oranı)
```

Tipik endüstriyel değerler:

| Ortam Koşulu | Sıcaklık (°C) | Bağıl Nem (%) | w (g/kg) |
|-------------|---------------|---------------|----------|
| Kış (soğuk, kuru) | 5 | 60 | 3.2 |
| İlkbahar/sonbahar | 15 | 65 | 6.9 |
| Yaz (sıcak, nemli) | 30 | 70 | 18.8 |
| Tropikal | 35 | 80 | 28.7 |
| Kurutma havası (tipik) | 80 | 5-10 | 5-10* |
| Kurutma havası (yüksek T) | 150 | 2-5 | 15-25* |

*Kurutma havası değerleri giriş nemi ve ısıtma derecesine bağlıdır.

### 1.2 Bağıl Nem (Relative Humidity, phi)

Bağıl nem, havanın mevcut su buharı basıncının aynı sıcaklıktaki doyma basıncına oranıdır:

```
phi = Pw / Pws(T)   [0-1 arası veya %0-%100]

Burada:
- Pw  = gerçek su buharı kısmi basıncı [Pa]
- Pws = T sıcaklığındaki doyma basıncı [Pa]
```

Mutlak nem ile bağıl nem arasındaki ilişki:

```
phi = (w × P) / ((0.622 + w) × Pws)

veya tersine:

w = 0.622 × phi × Pws / (P - phi × Pws)
```

**Kurutma açısından önemi:** Bağıl nem, kurutma hızını doğrudan etkiler. Düşük phi değerine sahip
hava daha fazla nem alabilir. Kurutma havasının phi değeri genellikle %5-15 aralığında tutulur.

### 1.3 Nemli Havanın Özgül Hacmi (Specific Volume)

```
v = (R_a × T_abs) / (P - Pw) × (1 + 1.608 × w)   [m^3/kg_kuru_hava]

Burada:
- R_a   = 287.05 J/(kg·K)  — kuru hava gaz sabiti
- T_abs = T + 273.15 [K]
- P     = toplam basınç [Pa]
- Pw    = su buharı kısmi basıncı [Pa]

Yaklaşık formül (düşük nem için):
v ~ (R_a × T_abs / P) × (1 + 1.608 × w)
```

Endüstriyel kurutma koşullarında özgül hacim değerleri:

| Sıcaklık (°C) | w (g/kg) | v (m^3/kg) | Not |
|---------------|----------|------------|-----|
| 20 | 8.7 | 0.842 | Ortam havası (yaz) |
| 80 | 8.7 | 1.012 | Isıtılmış kurutma havası |
| 150 | 8.7 | 1.219 | Yüksek sıcaklık kurutma |
| 40 | 30.0 | 0.920 | Egzoz havası (nemli) |
| 60 | 50.0 | 1.010 | Egzoz havası (çok nemli) |

### 1.4 Nemli Hava Entalpisi (Enthalpy of Moist Air)

Kuru hava başına entalpi:

```
h = Cp_a × T + w × (h_fg + Cp_v × T)   [kJ/kg_kuru_hava]

Burada:
- Cp_a = 1.005 kJ/(kg·K)  — kuru hava özgül ısısı
- Cp_v = 1.88 kJ/(kg·K)   — su buharı özgül ısısı (ortalama)
- h_fg = 2501 kJ/kg        — 0°C'de buharlaşma gizli ısısı
- T    = sıcaklık [°C]
- w    = mutlak nem [kg/kg]
```

Sayısal değerlendirme:

| Bileşen | Formül Terimi | T=80°C, w=0.01 | T=150°C, w=0.01 |
|---------|--------------|-----------------|------------------|
| Kuru hava sensible | Cp_a × T | 80.4 kJ/kg | 150.75 kJ/kg |
| Su buharı latent | w × h_fg | 25.01 kJ/kg | 25.01 kJ/kg |
| Su buharı sensible | w × Cp_v × T | 1.50 kJ/kg | 2.82 kJ/kg |
| **Toplam entalpi** | **h** | **106.9 kJ/kg** | **178.6 kJ/kg** |

### 1.5 Yaş Termometre Sıcaklığı (Wet-Bulb Temperature)

Yaş termometre sıcaklığı (T_wb), adyabatik doyma sıcaklığına çok yakındır ve
kurutma potansiyelini belirlemede kritik öneme sahiptir:

```
Tanım: h(T_db, w) ~ h(T_wb, w_s(T_wb))

Açık yazılırsa:
Cp_a × T_db + w × (h_fg + Cp_v × T_db) ~ Cp_a × T_wb + w_s(T_wb) × (h_fg + Cp_v × T_wb)

Burada:
- T_db      = kuru termometre sıcaklığı (dry-bulb temperature) [°C]
- T_wb      = yaş termometre sıcaklığı (wet-bulb temperature) [°C]
- w_s(T_wb) = T_wb'deki doyma nemi [kg/kg]
```

**Kurutma için önemi:** Adyabatik kurutmada hava, yaş termometre sıcaklığına kadar soğuyabilir.
T_db ile T_wb arasındaki fark (wet-bulb depression) kurutma potansiyelini gösterir.
Büyük fark = yüksek kurutma kapasitesi.

### 1.6 Çiğ Noktası Sıcaklığı (Dew Point Temperature)

Çiğ noktası, havanın sabit basınçta soğutulduğunda yoğuşmanın başladığı sıcaklıktır:

```
T_dp, şu koşulu sağlayan sıcaklıktır:
Pws(T_dp) = Pw = phi × Pws(T_db)

Magnus formülü ile yaklaşık çözüm:
T_dp = 237.3 × ln(Pw / 610.78) / (17.27 - ln(Pw / 610.78))   [°C]
```

Kurutma proseslerinde çiğ noktası referans tablosu:

| T_db (°C) | phi (%) | w (g/kg) | T_wb (°C) | T_dp (°C) |
|-----------|---------|----------|-----------|-----------|
| 20 | 50 | 7.3 | 13.7 | 9.3 |
| 30 | 60 | 16.1 | 23.0 | 21.4 |
| 60 | 10 | 13.0 | 28.5 | 17.2 |
| 80 | 5 | 15.2 | 32.8 | 20.5 |
| 100 | 3 | 19.2 | 36.5 | 24.8 |
| 150 | 1 | 12.8 | 34.0 | 17.5 |

---

## 2. Doyma Basıncı Hesaplamaları (Saturation Pressure Calculations)

### 2.1 Antoine Denklemi (Antoine Equation)

Endüstriyel kurutma sıcaklık aralığında en yaygın kullanılan doyma basıncı denklemi:

```
log10(Pws [mmHg]) = A - B / (C + T [°C])

Su için Antoine sabitleri:

Aralık 1 (1-100°C):
  A = 8.07131,  B = 1730.63,  C = 233.426

Aralık 2 (99-374°C):
  A = 8.14019,  B = 1810.94,  C = 244.485

Pa'ya dönüştürme:  Pws [Pa] = Pws [mmHg] × 133.322
```

**Uygulama notu:** Endüstriyel kurutucularda tipik hava sıcaklığı aralığı 60-250°C olduğundan,
her iki aralığın da kullanılması gerekebilir. 100°C civarında iki aralık sonuçları birbirine
yakın olmalıdır; bu geçiş noktasında doğrulama yapılması önerilir.

### 2.2 ASHRAE Formülleri (ASHRAE Saturation Pressure)

ASHRAE Fundamentals Handbook'ta önerilen yüksek doğruluklu formül:

```
0°C ila 200°C arası:
ln(Pws) = C8/T + C9 + C10×T + C11×T^2 + C12×T^3 + C13×ln(T)

Burada T [K], Pws [Pa]

Katsayılar:
C8  = -5.800 220 6 × 10^3
C9  =  1.391 499 3
C10 = -4.864 023 9 × 10^-2
C11 =  4.176 476 8 × 10^-5
C12 = -1.445 209 3 × 10^-8
C13 =  6.545 967 3
```

**ASHRAE ile Magnus karşılaştırması:**

| Sıcaklık (°C) | Magnus Pws (Pa) | ASHRAE Pws (Pa) | Fark (%) |
|---------------|-----------------|-----------------|----------|
| 20 | 2339 | 2338 | <0.1 |
| 60 | 19946 | 19933 | <0.1 |
| 100 | 101325 | 101325 | 0.0 |
| 150 | 476101 | 476165 | <0.1 |
| 200 | 1555740 | 1554920 | <0.1 |

Her iki formül de endüstriyel kurutma hesapları için yeterli doğruluktadır.

### 2.3 Magnus Formülü (Basitleştirilmiş)

Yaygın kullanılan yaklaşık formül (0-100°C arası):

```
Pws = 610.78 × exp(17.27 × T / (T + 237.3))   [Pa]

Burada T = sıcaklık [°C]
```

### 2.4 Doyma Basıncı ve Maksimum Nem Taşıma Kapasitesi Tablosu

| Sıcaklık (°C) | Pws (Pa) | Pws (kPa) | w_s (g/kg)* | Maksimum Nem Kapasitesi Yorumu |
|---------------|----------|-----------|-------------|-------------------------------|
| 0 | 611 | 0.611 | 3.8 | Çok düşük kurutma kapasitesi |
| 10 | 1228 | 1.228 | 7.6 | Düşük kurutma kapasitesi |
| 20 | 2339 | 2.339 | 14.7 | Sınırlı kapasite |
| 30 | 4243 | 4.243 | 27.2 | Düşük sıcaklık kurutma |
| 40 | 7384 | 7.384 | 48.9 | Isı pompası kurutucu aralığı |
| 50 | 12349 | 12.349 | 86.0 | Orta sıcaklık kurutma |
| 60 | 19946 | 19.946 | 152.4 | Konvektif kurutucu alt aralığı |
| 70 | 31188 | 31.188 | 276.2 | Konvektif kurutucu orta aralığı |
| 80 | 47414 | 47.414 | 546.6 | Konvektif kurutucu üst aralığı |
| 90 | 70182 | 70.182 | 1399 | Yüksek sıcaklık kurutma |
| 100 | 101325 | 101.325 | --- (doymuş) | Pws = P_atm, hava tam doyma |
| 120 | 198674 | 198.674 | --- | Pws > P_atm |
| 150 | 476101 | 476.101 | --- | Süper ısıtılmış buhar alanı |

*w_s = 0.622 × Pws / (101325 - Pws), standart atmosfer basıncında.

**Kritik not:** 100°C üzerinde Pws > P_atm olduğundan, standart basınçta hava tamamen
doyma noktasının üstünde çalışır. Bu nedenle yüksek sıcaklık kurutucularda bağıl nem
çok düşüktür ve havanın nem taşıma kapasitesi fiilen çok yüksektir.

### 2.5 Yükseklik (Altitude) ve Basınç Etkisi

Deniz seviyesinden yüksekte kurulu tesislerde atmosfer basıncı düşer. Bu durum nemli hava
hesaplamalarını doğrudan etkiler:

```
Barometrik basınç formülü (standart atmosfer):
P = 101325 × (1 - 2.2558 × 10^-5 × z)^5.2559   [Pa]

Burada z = deniz seviyesinden yükseklik [m]
```

Yüksekliğe göre doyma nem oranı değişimi:

| Yükseklik (m) | P_atm (kPa) | w_s @ 80°C (g/kg) | w_s artış (%) |
|---------------|-------------|-------------------|---------------|
| 0 (deniz seviyesi) | 101.325 | 546.6 | referans |
| 500 | 95.46 | 610.4 | +11.7 |
| 1000 | 89.87 | 685.9 | +25.5 |
| 1500 | 84.56 | 776.6 | +42.1 |
| 2000 | 79.50 | 888.6 | +62.6 |

**Pratik sonuç:** Yüksek rakımlı tesislerde hava daha fazla nem taşıyabilir. Bu nedenle
aynı sıcaklıkta daha az hava debisi ile aynı kurutma yükü karşılanabilir; ancak fan
basınç gereksinimi ve motor performansı da etkilenir.

---

## 3. Mollier Diyagramı (Mollier h-w Diagram)

### 3.1 Diyagram Yapısı

Mollier diyagramı (h-w veya h-x diyagramı), nemli havanın tüm özelliklerini tek bir grafikte
gösterir. Avrupa'da yaygın kullanılır (ABD'de psikrometrik chart tercih edilir).

```
  h (kJ/kg)
  ^
  |           /  phi = 100% (doyma eğrisi)
  |          / /
  |         / / /  phi = 80%
  |        / / / /
  |       / / / / /  phi = 50%
  |      / / / / / /
  |     / / / / / / /  phi = 20%
  |    / / / / / / / /
  |   / / / / / / / / /  phi = 5%
  |  / / / / / / / / / /
  | / / / / / / / / / / /
  |/ / / / / / / / / / / /
  +===============================> w (g/kg kuru hava)
  0    5   10   15   20   25   30

Eksenler:
- Yatay eksen : Mutlak nem w (g/kg veya kg/kg)
- Dikey eksen : Entalpi h (kJ/kg kuru hava)
- Eğri çizgiler: Sabit bağıl nem phi eğrileri
- Yatay çizgiler: Sabit entalpi (adyabatik doyma çizgileri yaklaşık yatay seyreder)
- Eğik düz çizgiler: Sabit sıcaklık (izotermler, hafif eğimli)
```

### 3.2 Diyagramın Okunması ve Kurutma Analizi İçin Kullanımı

Mollier diyagramından okunabilecek bilgiler:

1. **Bir noktanın tüm özellikleri:** T, w, phi, h, T_wb, T_dp değerleri iki bağımsız
   parametre (genellikle T ve phi, veya T ve w) bilindiğinde diğerleri okunur.

2. **Proses çizgileri:** Isıtma, kurutma, karıştırma gibi prosesler diyagram üzerinde
   karakteristik çizgiler oluşturur.

3. **Enerji dengesi:** Entalpi ekseninden ısı giriş/çıkış miktarları doğrudan okunur.

4. **Kurutma kapasitesi:** Giriş ve çıkış noktaları arasındaki w farkı, havanın
   taşıyabileceği nem miktarını gösterir.

### 3.3 Kurutma Prosesi Çizgileri

```
  h (kJ/kg)
  ^
  |
  |  B <<<<<<<<<< A (Isıtma: yatay hareket, w sabit, T artar)
  |  |  \
  |  |    \  C (Adyabatik kurutma: h ~ sabit, w artar, T azalır)
  |  |      \
  |  |        \  D (Gerçek kurutma: B ile C arası)
  |  |          \
  |  |            E  (Doyma eğrisi üzerinde, phi = 100%)
  |  |
  +===================================> w (g/kg)

Proses açıklamaları:
A -> B : Isıtma (w sabit, T artar, phi azalır)
B -> C : Adyabatik kurutma (h ~ sabit, w artar, T azalır)
B -> D : Gerçek kurutma (ısı kaybı ile, h biraz azalır)
B -> E : Teorik maksimum kurutma (doyma noktasına kadar)

Noktalar:
A = Ortam havası      (T_amb, phi_amb, düşük h)
B = Kurutucu girişi   (T_supply, düşük phi, yüksek h)
C = Adyabatik egzoz   (T ~ T_wb, yüksek phi, h ~ h_B)
D = Gerçek egzoz      (T > T_wb, phi < 100%, h < h_B)
E = İdeal egzoz       (T = T_wb, phi = 100%)
```

### 3.4 Adyabatik Doyma Çizgisi (Adiabatic Saturation Line)

Adyabatik doyma çizgisi, sabit entalpi çizgisine çok yakındır. Bu çizgi kurutma prosesinin
ideal rotasını gösterir:

```
Adyabatik doyma koşulu:
h(T, w) = h(T_as, w_s(T_as)) = sabit

Burada:
- T_as    = adyabatik doyma sıcaklığı [°C]
- w_s(T_as) = T_as'deki doyma nemi [kg/kg]

Yaklaşım:
T_as ~ T_wb (yaş termometre sıcaklığına yaklaşık eşit)

Adyabatik doyma çizgisi boyunca:
- Sıcaklık azalır (sensible ısı, nemi buharlaştırmaya harcanır)
- Nem oranı artar (nemlilik artar)
- Entalpi yaklaşık sabit kalır
- Bağıl nem artarak %100'e yaklaşır
```

**Endüstriyel önemi:** Gerçek kurutucularda proses tam olarak adyabatik doyma çizgisini
takip etmez; ısı kayıpları nedeniyle çizginin biraz altında seyreder.

---

## 4. Kurutma Prosesi Psikrometrik Analizi (Psychrometric Analysis of Drying Process)

### 4.1 Isıtma Aşaması (Air Heating: Constant w, Increasing T)

Hava ısıtıcıda (heater) sabit nem oranında ısıtılır:

```
Proses: Mollier diyagramında yatay çizgi (w = sabit)
- T artar: T_amb -> T_supply
- phi azalır: hava daha kuru hale gelir
- h artar: delta_h = Cp_a × delta_T + w × Cp_v × delta_T ~ (1.005 + 1.88w) × delta_T

Örnek: T_amb = 20°C, phi = 60%, w = 8.8 g/kg
        T_supply = 80°C sonrası:
        phi ~ 1.9%, w = 8.8 g/kg (değişmez)
        h = 1.005 × 80 + 0.0088 × (2501 + 1.88 × 80) = 103.6 kJ/kg
```

### 4.2 Adyabatik Kurutma (Following Wet-Bulb Line)

İdeal kurutma: hava entalpisi yaklaşık sabit kalır; havanın sensible ısısı
ürünün nemini buharlaştırmaya harcanır:

```
Proses: Sabit entalpi çizgisi (h ~ sabit)
- T azalır: T_supply -> T_wb'ye yakın
- w artar: nem üründen havaya geçer
- phi artar: %100'e yaklaşır (ideal durumda)

Enerji dengesi (adyabatik hal):
Cp_a × (T_in - T_out) ~ (w_out - w_in) × h_fg

Burada h_fg ~ 2501 + 1.88 × T_wb [kJ/kg] (T_wb civarında)
```

### 4.3 Egzoz Havası Durum Belirleme (Exhaust Air State Determination)

Gerçek kurutucularda ısı kayıpları nedeniyle proses tam adyabatik değildir:

```
Proses: Adyabatik ve izotermal arasında bir yol izler.
- Hava entalpisi biraz azalır (duvar kayıpları, radyasyon, konveksiyon)
- Egzoz sıcaklığı T_wb'den biraz yüksektir
- Egzoz nemi doyma noktasına ulaşmaz (phi_out < 100%)

Tipik egzoz koşulları:
- Konveyör (bantlı) kurutucu : phi_out = %60-80, T_out = T_wb + 5-15°C
- Akışkan yataklı kurutucu   : phi_out = %50-70
- Püskürtmeli (spray) kurutucu: phi_out = %30-60 (kısa temas süresi)
- Tambur (rotary) kurutucu    : phi_out = %50-75
- Tünel kurutucu              : phi_out = %60-80
```

Egzoz durumu denklemi (gerçek kurutucu):

```
h_out = h_in - Q_loss / m_air

Burada:
- h_out   = egzoz havası entalpisi [kJ/kg]
- h_in    = giriş havası entalpisi [kJ/kg]
- Q_loss  = kurutucu ısı kaybı [kW]
- m_air   = kuru hava kütle debisi [kg/s]

Ardından iteratif olarak:
1) T_out ve w_out tahmini yap
2) h(T_out, w_out) = h_out koşulunu kontrol et
3) phi(T_out, w_out) <= phi_max koşulunu kontrol et (genellikle phi_max = %70-85)
4) Yakınsayana kadar tekrarla
```

### 4.4 Hava Geri Deviri Karışım Hesaplamaları (Air Recirculation Mixing)

Geri devir (recirculation) yapıldığında, taze hava ile egzoz havası karıştırılır:

```
Karışım denklemi (kütle bazlı):
m_mix = m_fresh + m_recirc
w_mix = (m_fresh × w_fresh + m_recirc × w_recirc) / m_mix
h_mix = (m_fresh × h_fresh + m_recirc × h_recirc) / m_mix
T_mix ~ (m_fresh × T_fresh + m_recirc × T_recirc) / m_mix

Geri devir oranı (recirculation ratio):
R = m_recirc / m_mix = m_recirc / (m_fresh + m_recirc)   [0-1 arası]

Burada:
- m_fresh  = taze hava debisi [kg/s]
- m_recirc = geri devredilen hava debisi [kg/s]
- m_mix    = karışım debisi [kg/s]
```

**Mollier diyagramında:** Karışım noktası, taze ve egzoz noktalarını birleştiren doğru
üzerinde, kütle oranına göre belirlenir.

---

## 5. Nemli Hava Exergy'si (Moist Air Exergy)

### 5.1 Termal Exergy Bileşeni (Thermal Exergy Component)

Sıcaklık farkından kaynaklanan exergy:

```
ex_thermal = (Cp_a + w × Cp_v) × [(T - T_0) - T_0 × ln(T / T_0)]   [kJ/kg_kuru_hava]

Burada:
- Cp_a = 1.005 kJ/(kg·K)     — kuru hava özgül ısısı
- Cp_v = 1.88 kJ/(kg·K)      — su buharı özgül ısısı
- T    = hava sıcaklığı [K]
- T_0  = dead state sıcaklığı [K] (referans ortam)

Not: T > T_0 ise pozitif (sıcak hava), T < T_0 ise de pozitif (soğuk hava).
Her iki durumda da termal exergy sıfırdan büyüktür.
```

### 5.2 Kimyasal (Konsantrasyon) Exergy Bileşeni (Chemical Exergy Component)

Nem konsantrasyonu farkından kaynaklanan exergy:

```
ex_chemical = R_a × T_0 × [(1 + 1.608w) × ln((1 + 1.608w_0) / (1 + 1.608w))
             + 1.608w × ln(w / w_0)]   [kJ/kg_kuru_hava]

Burada:
- R_a   = 0.287 kJ/(kg·K)     — kuru hava gaz sabiti
- T_0   = dead state sıcaklığı [K]
- w     = havanın mutlak nemi [kg/kg]
- w_0   = dead state mutlak nemi [kg/kg]
- 1.608 = M_a / M_w = 28.964 / 18.015

Fiziksel anlam:
- w < w_0 ise (kuru hava): nem alma potansiyeli var -> kimyasal exergy pozitif
- w > w_0 ise (nemli hava): yoğuşma potansiyeli var -> kimyasal exergy pozitif
- w = w_0 ise: kimyasal denge, ex_chemical = 0
```

### 5.3 Toplam Nemli Hava Exergy Formülü (Total Moist Air Exergy)

Dead state'e (T_0, P_0, w_0) göre toplam spesifik exergy:

```
ex_total = ex_thermal + ex_chemical

ex_total = (Cp_a + w × Cp_v) × [(T - T_0) - T_0 × ln(T / T_0)]
         + R_a × T_0 × [(1 + 1.608w) × ln((1 + 1.608w_0) / (1 + 1.608w))
         + 1.608w × ln(w / w_0)]

Birim: kJ / kg_kuru_hava

Parametreler:
- Cp_a  = 1.005 kJ/(kg·K)
- Cp_v  = 1.88 kJ/(kg·K)
- R_a   = 0.287 kJ/(kg·K)
- T     = hava sıcaklığı [K]
- T_0   = dead state sıcaklığı [K]
- w     = mutlak nem [kg/kg]
- w_0   = dead state mutlak nemi [kg/kg]
```

### 5.4 Exergy Değerleri Tablosu

Dead state: T_0 = 25°C (298.15 K), phi_0 = 60%, w_0 = 0.01197 kg/kg

| Durum | T (°C) | w (g/kg) | ex_thermal (kJ/kg) | ex_chemical (kJ/kg) | ex_total (kJ/kg) |
|-------|--------|----------|---------------------|---------------------|-------------------|
| Ortam (dead state) | 25 | 11.97 | 0.00 | 0.00 | 0.00 |
| Isıtılmış (60°C) | 60 | 11.97 | 2.00 | 0.00 | 2.00 |
| Isıtılmış (80°C) | 80 | 11.97 | 4.91 | 0.00 | 4.91 |
| Isıtılmış (100°C) | 100 | 11.97 | 9.14 | 0.00 | 9.14 |
| Isıtılmış (150°C) | 150 | 11.97 | 22.17 | 0.00 | 22.17 |
| Kurutma girişi | 80 | 8.80 | 4.91 | 0.28 | 5.19 |
| Kurutma girişi | 150 | 8.80 | 22.17 | 0.28 | 22.45 |
| Egzoz (nemli) | 45 | 30.0 | 0.66 | 2.62 | 3.28 |
| Egzoz (nemli) | 55 | 50.0 | 1.48 | 5.75 | 7.23 |
| Egzoz (çok nemli) | 40 | 40.0 | 0.37 | 4.02 | 4.39 |

**Kritik gözlem:** Isıtılmış kurutma havasında termal exergy baskındır. Nemli egzoz havasında ise
kimyasal exergy önemli bir paya sahiptir. Bu nedenle egzoz havasının sadece ısısını değil,
nemini de değerlendirmek exergy geri kazanımı açısından gereklidir.

### 5.5 Sayısal Örnek: Nemli Hava Exergy Hesabı

**Kurutma girişi havası:** T = 150°C = 423.15 K, w = 0.0088 kg/kg
**Dead state:** T_0 = 25°C = 298.15 K, w_0 = 0.01197 kg/kg

```
Termal exergy:
ex_th = (1.005 + 0.0088 × 1.88) × [(423.15 - 298.15) - 298.15 × ln(423.15/298.15)]
      = 1.02154 × [125.0 - 298.15 × 0.3497]
      = 1.02154 × [125.0 - 104.30]
      = 1.02154 × 20.70
      = 21.15 kJ/kg

Kimyasal exergy:
ex_ch = 0.287 × 298.15 × [(1 + 1.608 × 0.0088) × ln((1 + 1.608 × 0.01197)/(1 + 1.608 × 0.0088))
       + 1.608 × 0.0088 × ln(0.0088/0.01197)]
      = 85.57 × [(1.01415) × ln(1.01925/1.01415) + 0.01415 × ln(0.7352)]
      = 85.57 × [(1.01415) × 0.00503 + 0.01415 × (-0.3075)]
      = 85.57 × [0.00510 - 0.00435]
      = 85.57 × 0.00075
      = 0.064 kJ/kg

Toplam: ex_total = 21.15 + 0.064 = 21.21 kJ/kg
```

**Egzoz havası:** T = 45°C = 318.15 K, w = 0.030 kg/kg

```
Termal exergy:
ex_th = (1.005 + 0.030 × 1.88) × [(318.15 - 298.15) - 298.15 × ln(318.15/298.15)]
      = 1.0614 × [20 - 298.15 × 0.06503]
      = 1.0614 × [20 - 19.39]
      = 1.0614 × 0.61
      = 0.65 kJ/kg

Kimyasal exergy:
ex_ch = 0.287 × 298.15 × [(1 + 1.608 × 0.030) × ln((1 + 1.608 × 0.01197)/(1 + 1.608 × 0.030))
       + 1.608 × 0.030 × ln(0.030/0.01197)]
      = 85.57 × [(1.04824) × ln(1.01925/1.04824) + 0.04824 × ln(2.506)]
      = 85.57 × [(1.04824) × (-0.02802) + 0.04824 × 0.9189]
      = 85.57 × [-0.02937 + 0.04433]
      = 85.57 × 0.01496
      = 1.28 kJ/kg

Toplam: ex_total = 0.65 + 1.28 = 1.93 kJ/kg
```

**Sonuç:** Giriş havasında termal exergy (%99.7) baskınken, egzoz havasında kimyasal exergy (%66.3)
baskındır. Bu durum, egzoz havası geri kazanım stratejisinin yalnızca ısıya değil, neme de
odaklanması gerektiğini gösterir.

---

## 6. Doyma Hesapları (Saturation Calculations)

### 6.1 Çeşitli Sıcaklıklarda Maksimum Nem Taşıma Kapasitesi

Havanın belirli bir sıcaklıkta taşıyabileceği maksimum su buharı miktarı, doyma nemi (w_s)
ile ifade edilir:

```
w_s = 0.622 × Pws(T) / (P - Pws(T))   [kg/kg]

Burada:
- Pws(T) = T sıcaklığındaki doyma basıncı [Pa]
- P      = toplam atmosfer basıncı [Pa]

Koşul: Pws(T) < P olmalıdır. Pws(T) >= P olduğunda (T >= 100°C standart basınçta)
       hava teorik olarak sınırsız nem taşıyabilir.
```

Pratik kurutma sıcaklıkları için kapasite tablosu (P = 101.325 kPa):

| T (°C) | Pws (kPa) | w_s (g/kg) | Kurutma Kapasitesi* (g/kg) | Yorum |
|--------|-----------|------------|---------------------------|-------|
| 40 | 7.38 | 48.9 | 37.9 | Isı pompası kurutucu |
| 50 | 12.35 | 86.0 | 75.0 | Düşük T kurutma |
| 60 | 19.95 | 152.4 | 141.4 | Gıda kurutma alt sınırı |
| 70 | 31.19 | 276.2 | 265.2 | Gıda kurutma üst sınırı |
| 80 | 47.41 | 546.6 | 535.6 | Endüstriyel standart |
| 90 | 70.18 | 1399 | 1388 | Yüksek kapasite |

*Kurutma kapasitesi = w_s - w_0, burada w_0 = 11.0 g/kg (tipik ortam nemi).

### 6.2 Basınç (Yükseklik) Etkisi Altında Doyma Hesapları

Farklı atmosfer basınçlarında aynı sıcaklıktaki doyma nemi:

```
w_s(T, P) = 0.622 × Pws(T) / (P - Pws(T))

Pws sıcaklığa bağlıdır ancak basınçtan bağımsızdır.
Toplam basınç P düştükçe (yükseklik arttıkça):
- (P - Pws) azalır
- w_s artar
```

| T = 80°C | P (kPa) | Pws (kPa) | w_s (g/kg) | Fark (%) |
|----------|---------|-----------|------------|----------|
| Deniz seviyesi | 101.33 | 47.41 | 546.6 | ref |
| 500 m | 95.46 | 47.41 | 613.6 | +12.3 |
| 1000 m | 89.87 | 47.41 | 694.0 | +27.0 |
| 1500 m | 84.56 | 47.41 | 793.9 | +45.2 |
| 2000 m | 79.50 | 47.41 | 919.3 | +68.2 |

---

## 7. Hava Geri Deviri Hesabı (Air Recirculation Calculation)

### 7.1 Taze ve Geri Devir Havası Karışımı

```
Karışım özellikleri:
w_mix = (1 - R) × w_fresh + R × w_exhaust   [kg/kg]
T_mix = (1 - R) × T_fresh + R × T_exhaust   [°C] (yaklaşık)
h_mix = (1 - R) × h_fresh + R × h_exhaust   [kJ/kg]

Burada R = geri devir oranı = m_recirc / m_total   [0 < R < 1]
```

### 7.2 Optimum Geri Devir Oranı Belirleme

Geri devir oranının artması:
- (+) Isıtma enerjisi gereksinimini azaltır (taze hava zaten sıcak)
- (-) Giriş havasının nemini artırır (kurutma kapasitesini azaltır)
- (-) Egzoz neminin geri dönmesi, kurutma hızını yavaşlatır

```
Optimum geri devir oranı kısıtları:

1) Kurutma kapasitesi koşulu:
   w_mix < w_max_supply   (giriş neminin belirlenen üst sınırı)

2) Doyma koşulu:
   phi_exhaust(R) < phi_max   (genellikle phi_max = %85-90, yoğuşma önleme)

3) Ekonomik optimum:
   delta_Q_savings(R) / delta_R > 0   (marjinal tasarrufun pozitif kalması)
```

Tipik optimum geri devir oranları:

| Kurutucu Tipi | Tipik R_opt | phi_exh limit | Tasarruf (%) | Not |
|---------------|-------------|--------------|--------------|-----|
| Bantlı (konveyör) | %20-40 | <%80 | %8-18 | Düşük T, iyi kontrol |
| Tünel | %15-30 | <%75 | %6-15 | Ürüne göre değişir |
| Akışkan yatak | %10-25 | <%70 | %5-12 | Yüksek nem kısıtı |
| Püskürtmeli | %0-15 | <%60 | %3-8 | Çok sınırlı (kalite) |
| Döner tambur | %15-35 | <%75 | %7-16 | Dökme malzeme avantajı |

### 7.3 Geri Devir ile Enerji Tasarrufu Hesabı

```
Geri devirsiz (R = 0):
Q_heat_0 = m_air × (h_supply - h_fresh)   [kW]

Geri devirli (R > 0):
Q_heat_R = m_air × (h_supply - h_mix)     [kW]

Tasarruf:
delta_Q = Q_heat_0 - Q_heat_R = m_air × (h_mix - h_fresh) = m_air × R × (h_exhaust - h_fresh)

Tasarruf yüzdesi:
Savings(%) = delta_Q / Q_heat_0 × 100
           = R × (h_exhaust - h_fresh) / (h_supply - h_fresh) × 100
```

### 7.4 Geri Devir Sayısal Örneği

```
Veriler:
- Taze hava: T_fresh = 20°C, phi = 60%, w_fresh = 8.73 g/kg, h_fresh = 42.3 kJ/kg
- Egzoz havası: T_exh = 45°C, phi = 70%, w_exh = 43.4 g/kg, h_exh = 156.5 kJ/kg
- Kurutucu giriş: T_supply = 80°C
- Hava debisi: m_air = 5.0 kg/s
- Geri devir oranı: R = 0.25 (%25)

Adım 1 — Karışım:
w_mix = 0.75 × 8.73 + 0.25 × 43.4 = 6.55 + 10.85 = 17.40 g/kg
T_mix = 0.75 × 20 + 0.25 × 45 = 15 + 11.25 = 26.25°C
h_mix = 0.75 × 42.3 + 0.25 × 156.5 = 31.7 + 39.1 = 70.8 kJ/kg

Adım 2 — Isıtma yükü karşılaştırma:
Q_heat_0 = 5.0 × (103.5 - 42.3) = 306.0 kW   (geri devirsiz)
Q_heat_R = 5.0 × (103.5 - 70.8) = 163.5 kW   (geri devirli)

Not: h_supply w_mix ile yeniden hesaplanmalıdır:
h_supply_R = 1.005 × 80 + 0.01740 × (2501 + 1.88 × 80) = 80.4 + 46.2 = 126.6 kJ/kg
Q_heat_R   = 5.0 × (126.6 - 70.8) = 279.0 kW

Adım 3 — Tasarruf:
delta_Q = 306.0 - 279.0 = 27.0 kW
Savings = 27.0 / 306.0 × 100 = %8.8

Adım 4 — Dikkat: Geri devir kurutma kapasitesini azaltır
w_out_0 = w_exhaust (R=0) varsayımı = 43.4 g/kg (geri devirsiz)
delta_w_0 = 43.4 - 8.73 = 34.67 g/kg (geri devirsiz nem alma)
delta_w_R = 43.4 - 17.40 = 26.0 g/kg (geri devirli nem alma, %25 azalma)

Sonuç: %25 geri devir, %8.8 ısıtma tasarrufu sağlar ancak kurutma kapasitesini %25
azaltır. Bu nedenle ya kurutma süresi uzatılır ya da debi artırılır.
```

---

## 8. Hesap Örnekleri (Worked Examples)

### 8.1 Örnek 1: 150°C Kurutma Havası Özelliklerinin Hesabı

**Problem:** Bir endüstriyel kurutucuya 150°C, 1 atm basınçta hava verilmektedir.
Ortam havası 25°C, %50 bağıl nemdedir. Kurutma havasının tüm psikrometrik özelliklerini hesaplayın.

**Adım 1: Ortam Havası (25°C, phi = %50)**

```
Pws(25) = 610.78 × exp(17.27 × 25 / (25 + 237.3)) = 3169 Pa
Pw = 0.50 × 3169 = 1585 Pa
w_amb = 0.622 × 1585 / (101325 - 1585) = 0.009886 kg/kg = 9.89 g/kg
h_amb = 1.005 × 25 + 0.009886 × (2501 + 1.88 × 25) = 25.13 + 24.90 = 50.03 kJ/kg
v_amb = (287.05 × 298.15) / (101325 - 1585) × (1 + 1.608 × 0.009886) = 0.872 m^3/kg
```

**Adım 2: Isıtılmış Hava (150°C, w = 9.89 g/kg, aynı)**

```
Isıtmada nem değişmez: w_supply = w_amb = 9.89 g/kg

Pws(150) = 476101 Pa
phi_supply = (0.009886 × 101325) / ((0.622 + 0.009886) × 476101)
           = 1001.7 / 300852
           = 0.00333 = %0.33

h_supply = 1.005 × 150 + 0.009886 × (2501 + 1.88 × 150)
         = 150.75 + 0.009886 × 2782.0
         = 150.75 + 27.50
         = 178.25 kJ/kg

v_supply = (287.05 × 423.15) / (101325 - 1585) × (1 + 1.608 × 0.009886) = 1.239 m^3/kg
```

**Adım 3: Yaş Termometre ve Çiğ Noktası**

```
Çiğ noktası (ortam koşullarına göre):
T_dp = 237.3 × ln(1585 / 610.78) / (17.27 - ln(1585 / 610.78))
     = 237.3 × 0.9540 / (17.27 - 0.9540)
     = 226.4 / 16.316
     = 13.87°C

Isıtılmış havada Pw değişmediğinden T_dp aynı kalır: T_dp = 13.87°C
(Isıtma, çiğ noktasını değiştirmez.)

Yaş termometre sıcaklığı (iteratif hesap):
T_wb ~ 35°C (150°C kuru sıcaklık, w = 9.89 g/kg için yaklaşık değer)
```

**Sonuç Tablosu:**

| Parametre | Ortam (25°C) | Isıtılmış (150°C) | Birim |
|----------|-------------|-------------------|-------|
| Kuru termometre T_db | 25 | 150 | °C |
| Bağıl nem phi | 50 | 0.33 | % |
| Mutlak nem w | 9.89 | 9.89 | g/kg |
| Entalpi h | 50.03 | 178.25 | kJ/kg |
| Özgül hacim v | 0.872 | 1.239 | m^3/kg |
| Çiğ noktası T_dp | 13.87 | 13.87 | °C |
| Yaş termometre T_wb | ~16.7 | ~35 | °C |

### 8.2 Örnek 2: Kurutma Sonrası Egzoz Durumu Belirleme

**Problem:** Örnek 1'deki kurutucu saatte 300 kg su buharlaştırmaktadır. Hava debisi
8.0 kg_kuru_hava/s'dir. Kurutucunun %5 ısı kaybı olduğunu kabul ederek egzoz koşullarını belirleyin.

**Adım 1: Nem artışı hesabı**

```
m_water = 300 kg/h = 0.0833 kg/s
delta_w = m_water / m_air = 0.0833 / 8.0 = 0.01042 kg/kg = 10.42 g/kg

w_exhaust = w_supply + delta_w = 9.89 + 10.42 = 20.31 g/kg
```

**Adım 2: Enerji dengesi**

```
Q_heater = m_air × (h_supply - h_amb) = 8.0 × (178.25 - 50.03) = 1025.8 kW
Q_loss = 0.05 × Q_heater = 51.3 kW

h_exhaust = h_supply - Q_loss / m_air = 178.25 - 51.3/8.0 = 178.25 - 6.41 = 171.84 kJ/kg
```

**Adım 3: Egzoz sıcaklığı (iteratif)**

```
h_exhaust = Cp_a × T_exh + w_exh × (h_fg + Cp_v × T_exh)
171.84 = 1.005 × T_exh + 0.02031 × (2501 + 1.88 × T_exh)

171.84 = 1.005 × T_exh + 50.80 + 0.03818 × T_exh
121.04 = 1.04318 × T_exh
T_exh = 116.0°C

Pws(116) ~ 175000 Pa
phi_exh = (0.02031 × 101325) / ((0.622 + 0.02031) × 175000)
        = 2058 / 112404
        = %1.83

Bu çok düşük bir bağıl nem! Kurutucunun havanın kapasitesini yeterince kullanmadığını gösterir.
Daha fazla malzeme yüklenmeli veya hava debisi azaltılmalıdır.
```

### 8.3 Örnek 3: Geri Devir Fayda Hesabı

**Problem:** Örnek 2'deki kurutucuya %30 oranında hava geri deviri uygulandığında
enerji tasarrufunu hesaplayın.

```
Ortam: T_fresh = 25°C, w_fresh = 9.89 g/kg, h_fresh = 50.03 kJ/kg
Egzoz: T_exh = 116°C, w_exh = 20.31 g/kg, h_exh = 171.84 kJ/kg
Geri devir oranı: R = 0.30

Adım 1 — Karışım:
w_mix = 0.70 × 9.89 + 0.30 × 20.31 = 6.92 + 6.09 = 13.01 g/kg
h_mix = 0.70 × 50.03 + 0.30 × 171.84 = 35.02 + 51.55 = 86.57 kJ/kg
T_mix ~ 0.70 × 25 + 0.30 × 116 = 17.5 + 34.8 = 52.3°C

Adım 2 — Yeni ısıtma yükü:
h_supply_new = 1.005 × 150 + 0.01301 × (2501 + 1.88 × 150)
             = 150.75 + 0.01301 × 2783 = 150.75 + 36.20 = 186.95 kJ/kg

Q_heat_new = 8.0 × (186.95 - 86.57) = 803.0 kW
Q_heat_old = 8.0 × (178.25 - 50.03) = 1025.8 kW

Adım 3 — Tasarruf:
delta_Q = 1025.8 - 803.0 = 222.8 kW
Savings = 222.8 / 1025.8 × 100 = %21.7

Adım 4 — Yıllık tasarruf (6000 h/yıl, dogalgaz = EUR 0.05/kWh):
Yillik_tasarruf = 222.8 × 6000 × 0.05 = EUR 66,840 / yıl
```

**Sonuç:** %30 geri devir oranı ile %21.7 ısıtma enerjisi tasarrufu sağlanır.
Ancak giriş nemi artacağından (9.89 -> 13.01 g/kg) kurutma kapasitesinin yeterli olup
olmadığı kontrol edilmelidir.

---

## 9. Kurutma Havası Optimizasyon Stratejileri Özeti

| Strateji | Psikrometrik Etki | Tasarruf (%) | Yatırım Süresi |
|---------|-------------------|--------------|-----------------|
| Egzoz havası geri deviri | w_in artar, T_in artar | %10-25 | 1-2 yıl |
| Isı geri kazanım eşanjörü | T_fresh artar, w sabit | %10-20 | 1-3 yıl |
| Isı pompası entegrasyonu | Egzoz neminden ısı alır | %30-50 | 2-5 yıl |
| Sıcaklık optimizasyonu | T_supply ayarı, phi_exh hedefi | %5-15 | <1 yıl |
| Hava debisi optimizasyonu | Daha yüksek phi_exh | %5-15 | <1 yıl |
| Çok kademeli kurutma | Her kademe farklı T | %10-25 | 2-4 yıl |

---

## İlgili Dosyalar

- `dryer/formulas.md` — Kurutucu exergy hesaplama formülleri ve motor denklemleri
- `dryer/benchmarks.md` — Kurutucu tiplerine göre verimlilik benchmark verileri
- `dryer/solutions/air_recirculation.md` — Hava geri deviri detaylı analiz ve optimizasyon
- `dryer/solutions/exhaust_heat_recovery.md` — Egzoz havası ısı geri kazanım yöntemleri
- `dryer/equipment/tunnel_dryer.md` — Tünel kurutucu detaylı analiz
- `dryer/equipment/spray_dryer.md` — Püskürtmeli kurutucu detaylı analiz
- `dryer/equipment/heat_pump_dryer.md` — Isı pompası kurutucu exergy analizi
- `factory/cross_equipment.md` — Ekipmanlar arası enerji entegrasyonu (kurutucu atık ısısı)
- `boiler/formulas.md` — Buhar kaynağı hesaplamaları (buhar ile kurutma sistemleri)

## Referanslar

- ASHRAE, "ASHRAE Handbook - Fundamentals," Chapter 1: Psychrometrics, 2021
- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014
- Kemp, I.C., "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4, Wiley-VCH, 2012
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," 3rd Edition, Elsevier, 2021
- Dincer, I. & Sahin, A.Z., "A New Model for Thermodynamic Analysis of a Drying Process," Int. J. Heat Mass Transfer, 2004
- Cengel, Y.A. & Boles, M.A., "Thermodynamics: An Engineering Approach," Chapter 14: Gas-Vapor Mixtures, McGraw-Hill
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Butterworths, 1985
- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 2016
- Strumiłło, C., Jones, P.L. & Żyłła, R., "Energy Aspects in Drying," Handbook of Industrial Drying, Ch. 54
- Aghbashlo, M. et al. (2013), "A review on exergy analysis of drying processes and systems," Renewable and Sustainable Energy Reviews, 22, 1-22
- ISO 13579, "Industrial Furnaces and Associated Processing Equipment - Method of Measuring Energy Balance and Calculating Efficiency"
