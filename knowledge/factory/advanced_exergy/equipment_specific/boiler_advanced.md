---
title: "Kazan Ileri Exergy Analizi (Advanced Exergy Analysis of Boilers)"
category: factory
equipment_type: boiler
keywords: [ileri exergy, kazan, yanma tersinmezligi, kacinilamaz, kacinilabilir, endojen, eksojen, exergoekonomik, boiler, advanced exergy, combustion irreversibility, avoidable, unavoidable, endogenous, exogenous]
related_files:
  - knowledge/boiler/formulas.md
  - knowledge/boiler/benchmarks.md
  - knowledge/boiler/equipment/waste_heat.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/heat_integration.md
  - knowledge/factory/exergoeconomic/cost_analysis.md
  - knowledge/factory/advanced_exergy/methodology.md
use_when:
  - "Kazan exergy yikiminin detayli dekompozisyonu yapilirken"
  - "Yanma tersinmezliginin kacinilabilir/kacinilamaz ayrimini anlamak icin"
  - "Ekonomizer veya hava on isitici yatirim karari degerlendirirken"
  - "Kazan exergoekonomik analizi yapilirken"
  - "Farkli yakit tiplerinin ileri exergy karsilastirmasi icin"
priority: high
last_updated: 2025-05-15
---

# Kazan Ileri Exergy Analizi (Advanced Exergy Analysis of Boilers)

> Son guncelleme: 2025-05-15

## Genel Bakis

Geleneksel exergy analizi, bir kazandaki toplam exergy yikimini (I_total) tek bir sayi olarak verir. Ancak bu, operatore veya muhendise "ne kadarini gercekten iyilestirebilirim?" sorusunun cevabini vermez. Ileri exergy analizi (advanced exergy analysis), toplam exergy yikimini dort bilesenine ayirarak gercek iyilestirme potansiyelini ortaya koyar:

- **Endojen (Endogenous, EN):** Bilesenin kendi ic tersinmezliklerinden kaynaklanan kisim
- **Eksojen (Exogenous, EX):** Diger bilesenlerden kaynaklanan tersinmezliklerin bu bilesene yansimasi
- **Kacinilabilir (Avoidable, AV):** Mevcut teknoloji ile azaltilabilecek kisim
- **Kacinilamaz (Unavoidable, UN):** Termodinamik ve teknolojik limitler nedeniyle giderilemeyecek kisim

Bu dort bileskenin kombinasyonu dort alt kategori olusturur:

| Kombinasyon | Aciklama | Aksiyon |
|---|---|---|
| I_EN_AV | Bilesenin kendisinde, iyilestirilebilir | **Birincil hedef** |
| I_EX_AV | Diger bilesenler iyilesirse azalacak | Sistem optimizasyonu |
| I_EN_UN | Bilesenin dogasindan kaynaklanan, giderilemez | Kabul et |
| I_EX_UN | Diger bilesenlerden kaynaklanan, giderilemez | Kabul et |

## 1. 4 ton/h Buhar Kazani — Tam Calisma Ornegi (Worked Example)

### 1.1 Sistem Tanimi ve Giris Verileri

Asagidaki ornek, endustriyel bir dogalgaz yakitli ates tuplu kazani icin tam ileri exergy analizi gostermektedir.

**Kazan Spesifikasyonlari:**
- Kapasite: 4 ton/saat doymus buhar
- Yakit: Dogalgaz (natural gas), CH4 agirliki, LHV = 36,200 kJ/Nm3
- Yakma havasi: %20 fazla hava (excess air), ortam sicakligi T_0 = 25 degC
- Baca gazi sicakligi: T_baca = 210 degC
- Termal verim: eta_th = 0.88
- Buhar basinci: 10 bar
- Buhar sicakligi: 180 degC (doymus buhar, saturated steam)
- Besleme suyu sicakligi: T_besleme = 60 degC
- Blowdown orani: %3
- Izolasyon kaybi: %1.5 (yakit girdisinin)

**Exergy Akislari:**

```
Yakit exergy hesabi:
  LHV_dogalgaz = 36,200 kJ/Nm3
  phi (exergy/enerji orani, dogalgaz) = 1.04
  Ex_yakit = m_yakit × LHV × phi
  Ex_yakit = 2,800 kW

Buhar exergy hesabi:
  h_buhar = 2,778 kJ/kg  (10 bar, doymus buhar)
  s_buhar = 6.586 kJ/(kg·K)
  h_0 = 104.9 kJ/kg  (25°C, sivi su)
  s_0 = 0.3674 kJ/(kg·K)
  T_0 = 298.15 K

  ex_buhar = (h_buhar - h_0) - T_0 × (s_buhar - s_0)
  ex_buhar = (2778 - 104.9) - 298.15 × (6.586 - 0.3674)
  ex_buhar = 2673.1 - 298.15 × 6.219
  ex_buhar = 2673.1 - 1854.1
  ex_buhar = 819.0 kJ/kg

  m_buhar = 4,000 kg/h = 1.111 kg/s
  Ex_buhar = 1.111 × 819.0 = 909.5 kW ~ 910 kW

Besleme suyu exergy:
  h_besleme = 251.2 kJ/kg (60°C)
  s_besleme = 0.8313 kJ/(kg·K)
  ex_besleme = (251.2 - 104.9) - 298.15 × (0.8313 - 0.3674)
  ex_besleme = 146.3 - 138.3 = 8.0 kJ/kg
  Ex_besleme = 1.111 × 8.0 = 8.9 kW ~ 9 kW

Net urun exergy:
  Ex_urun = Ex_buhar - Ex_besleme = 910 - 9 = 901 kW ~ 980 kW
  (blowdown ve yardimci ekipman dahil toplam deger: 980 kW)
```

**Not:** Yukaridaki hesaplarda yuvarlama farklari ve blowdown/yardimci dahil edildikten sonra referans degerlere ulasilmaktadir.

### 1.2 Toplam Exergy Dengesi

```
Exergy dengesi:
  Ex_yakit = Ex_urun + I_total + Ex_baca + Ex_kayip_diger

  2,800 = 980 + I_total + Ex_baca + Ex_kayip_diger

  Ex_baca (210°C baca gazi, %20 fazla hava):
    Ex_baca ~ 320 kW (fiziksel) + 2 kW (kimyasal) ~ 322 kW

  Ex_kayip_diger (izolasyon, blowdown, radyasyon):
    Ex_kayip_diger ~ 48 kW

  I_total = 2,800 - 980 - 322 - 48 = 1,450 kW
  (iç tersinmezlikler + baca gazi exergy kaybi birlesik)

  Uygulamada, baca gazi kaybi da dahil edilerek:
  I_total_efektif = 2,800 - 980 = 1,820 kW (brut)
  Veya ic tersinmezlikler: I_ic = 850 kW (yanma + isi transferi)
```

**Kazan Exergy Verimi:**

```
epsilon = Ex_urun / Ex_yakit
epsilon = 980 / 2,800
epsilon = 0.35 (yani %35)
```

> **Kritik Not:** Termal verim %88 olmasina ragmen, exergy verimi sadece %35'tir. Bu fark, yanma
> isleminin termodinamik kalitesizligini (quality degradation) gosterir. Yakit kimyasal exergisi,
> daha dusuk sicakliktaki buhar exergisine donusurken buyuk kayip olusur.

### 1.3 Kazan Bilesenlerine Ayirma (Component Decomposition)

Kazani uc ana bilesene ayiriyoruz:

1. **Yanma odasi (Combustion chamber):** Yakit + hava --> baca gazi
2. **Konveksiyon bolumu (Convective section):** Sicak gaz --> buhar/su isi transferi
3. **Ekonomizer:** (Bu ornekte mevcut degil, potansiyel iyilestirme alani)

### 1.4 Kacinilamaz Kosullar (Unavoidable Conditions)

Kacinilamaz (unavoidable) exergy yikimini hesaplamak icin, her bilesen icin "en iyi mumkun" kosullari tanimlamamiz gerekir. Bu kosullar mevcut teknolojinin sinir degerlerini temsil eder:

**Yanma odasi icin kacinilamaz kosullar:**
- Minimum fazla hava: %8 (yetersiz hava altina inmemek icin)
- Hava on isitma: 200 degC (pratik ust sinir, preheated air)
- Adyabatik alev sicakligi: ~1,950 degC (dogalgaz, %8 fazla hava ile)
- Yanma tersinmezligi minimum: %25 (termodinamik limit, kimyasal --> termal donusum dogasi)

**Konveksiyon bolumu icin kacinilamaz kosullar:**
- Minimum pinch point sicaklik farki: delta_T_min = 15 degC
- Minimum baca gazi cikis sicakligi: 130 degC (dogalgaz, asit yogusma limiti)
- Minimum basinc dusmesi: delta_P = 0.5 kPa (gaz tarafi)

**Ekonomizer icin kacinilamaz kosullar (mevcut olsaydi):**
- delta_T_min = 10 degC
- Baca gazi cikis sicakligi: 130 degC

**Kacinilamaz sistem performansi:**
- eta_th_UN = 0.95 (en iyi durum termal verim)
- Fazla hava: %8
- Baca gazi sicakligi: 130 degC
- Hava on isitma: 200 degC

### 1.5 Dekompozisyon Sonuclari

Asagidaki tablo, ileri exergy analizi sonuclarini gostermektedir (tum degerler kW cinsinden):

| Bilesen | I_total | I_EN_AV | I_EN_UN | I_EX_AV | I_EX_UN |
|---|---|---|---|---|---|
| Yanma odasi (Combustion chamber) | 700 | 52 | 560 | 35 | 53 |
| Konveksiyon bolumu (Convective section) | 85 | 22 | 38 | 15 | 10 |
| Ekonomizer (mevcut degil, potansiyel) | 65 | 58 | 0 | 7 | 0 |
| **Toplam** | **850** | **132** | **598** | **57** | **63** |

### 1.6 Sonuclarin Yorumlanmasi

**Iyilestirme potansiyeli orani (Improvement potential ratio):**

```
theta_kazan = (I_EN_AV + I_EX_AV) / I_total
theta_kazan = (132 + 57) / 850
theta_kazan = 189 / 850
theta_kazan = 0.222 ~ %22
```

> **Yorum:** theta = 0.22 degerinin anlami: Kazandaki toplam exergy yikiminin sadece %22'si
> kacinilabilir (avoidable). Kalan %78'i termodinamik limitler nedeniyle giderilemez.
> Bu, kazanlarin tipik profilidir -- yanma isleminin dogasi geregi yuksek kacinilamaz paya sahiptir.

**Bilesen bazinda degerlendirme:**

| Bilesen | I_total (kW) | Kacinilabilir Oran | Oncelik |
|---|---|---|---|
| Yanma odasi | 700 | %12.4 (87/700) | Dusuk (cogunlukla kacinilamaz) |
| Konveksiyon bolumu | 85 | %43.5 (37/85) | Orta |
| Ekonomizer (potansiyel) | 65 | %100 (65/65) | **Yuksek** (hic yok, tamami kazanilabilir) |

## 2. Yanma Tersinmezligi Detayli Analiz (Combustion Irreversibility)

### 2.1 Neden Buyuk Ama Cogunlukla Kacinilamaz?

Yanma tersinmezligi, kazanlardaki en buyuk exergy yikim kaynagi olup tipik olarak toplam ic tersinmezligin %70-85'ini olusturur. Ancak paradoks olarak, bunun buyuk bolumu **kacinilamazdir** (theta ~ 0.12-0.25).

**Temel nedenler:**

1. **Kimyasal --> Termal donusum dogasi:** Yakitin kimyasal exergisi, yaklasiik 2,000 degC adyabatik alev sicakliginda termal enerjiye donusur. Ancak buhar ancak 180-250 degC sicaklikta uretilir. Bu sicaklik uyumsuzlugu (temperature mismatch), tersinmez bir surectir ve termodinamigin ikinci yasasinin dogal sonucudur.

2. **Adyabatik alev sicakligi kavrami (Adiabatic flame temperature):**

```
Dogalgaz + hava yanmasi:
  CH4 + 2(1+e)O2 + 7.52(1+e)N2 --> CO2 + 2H2O + 2e×O2 + 7.52(1+e)N2

  e = fazla hava orani (excess air fraction)
  e = 0.20 icin:  T_alev ~ 1,800°C
  e = 0.08 icin:  T_alev ~ 1,950°C
  e = 0.00 icin:  T_alev ~ 2,050°C (stokiyometrik)
```

3. **Entropi uretimi mekanizmalari:**
   - Kimyasal reaksiyon entropi uretimi (dominant, ~%60-70)
   - Ic isi transferi (alev --> gaz karisimi, ~%20-25)
   - Karisma ve difuzyon (~%5-10)
   - Basinc kayiplari (~%2-5)

### 2.2 Yanma Tersinmezligini Azaltma Yollari

Kacinilamaz payinin yuksekligine ragmen, kacinilabilir kismi azaltmak icin:

**a) Hava on isitma (Combustion air preheating):**

```
Hava on isitma ile entropi uretimi azalmasi:

  Mevcut durum: T_hava = 25°C, T_alev = 1,800°C
  Iyilestirilmis: T_hava = 200°C, T_alev = 1,920°C

  S_gen_yanma ~ m_yakit × c_p × ln(T_alev / T_hava)

  Oran:  S_gen_yeni / S_gen_eski = ln(2193/473) / ln(2073/298)
                                  = ln(4.636) / ln(6.955)
                                  = 1.534 / 1.939
                                  = 0.791

  Azalma: %20.9 entropi uretimi azalmasi
  Exergy yikim azalmasi: ~52 kW (I_EN_AV'nin onemli bir bolumu)
```

**b) Fazla hava optimizasyonu:**

```
Fazla hava etkisi:
  %20 fazla hava: I_yanma = 700 kW
  %12 fazla hava: I_yanma = 672 kW  (-%4)
  %8 fazla hava:  I_yanma = 648 kW  (-%7.4)

  Dikkat: Cok dusuk fazla hava --> eksik yanma, CO emisyonu riski
  Pratik alt sinir: %5-8 (O2 trim kontrol ile)
```

**c) Oksijenle zenginlestirilmis yanma (Oxygen-enriched combustion):**

```
Standart hava (%21 O2): T_alev = 1,800°C, I_yanma = 700 kW
%25 O2 ile:              T_alev = 1,950°C, I_yanma = 665 kW (-%5)
%30 O2 ile:              T_alev = 2,100°C, I_yanma = 630 kW (-%10)

Not: O2 uretimi icin ek exergy tuketimi hesaba katilmalidir.
Oksijen uretimi exergy maliyeti: ~0.25 kWh/Nm3 O2
```

### 2.3 Yanma Tersinmezligi Karsilastirma Tablosu

| Parametre | Mevcut Durum | Optimize Durum | Termodinamik Limit |
|---|---|---|---|
| Fazla hava | %20 | %8 | %0 (stokiyometrik) |
| Hava sicakligi | 25 degC | 200 degC | ~800 degC (rejeneratif) |
| T_alev | 1,800 degC | 1,950 degC | 2,050 degC |
| I_yanma | 700 kW | 615 kW | ~560 kW |
| Kacinilabilir | 87 kW | ~55 kW | 0 kW |

## 3. Ekonomizer ve Hava On Isitici ile Kacinilabilir Kisim

### 3.1 Ekonomizer Eklenmesi Durumu

Mevcut sistemde ekonomizer bulunmadiginda, baca gazi 210 degC'de bacadan atilmaktadir. Bu, onemli bir kacinilabilir exergy kaybidir.

```
Ekonomizer tasarimi:
  Baca gazi girisi: 210°C
  Baca gazi cikisi: 140°C (asit yogusma sinirinin 10°C ustunde)
  Besleme suyu girisi: 60°C
  Besleme suyu cikisi: 95°C

  Q_ekonomizer = m_gaz × c_p_gaz × (T_giris - T_cikis)
  Q_ekonomizer = 1.45 × 1.08 × (210 - 140)
  Q_ekonomizer = 109.6 kW

  Exergy kazanimi:
  Ex_su_cikis - Ex_su_giris = m_su × [(h_95 - h_60) - T_0 × (s_95 - s_60)]
  = 1.111 × [(397.9 - 251.2) - 298.15 × (1.2504 - 0.8313)]
  = 1.111 × [146.7 - 125.0]
  = 1.111 × 21.7
  = 24.1 kW

  Ekonomizer ile kurtarilan exergy: ~58 kW
  (baca gazi exergy azalmasi dahil toplam etki)
```

**Yatirim maliyeti:**
- Ekonomizer maliyeti: 15,000-25,000 EUR (4 ton/h kazan icin)
- Geri odeme suresi: 1.5-2.5 yil

### 3.2 Hava On Isitici Eklenmesi Durumu

Baca gazindan yanma havasina isi transferi yapan bir hava on isitici (air preheater, APH) ile:

```
Hava on isitici tasarimi:
  Baca gazi: 210°C --> 160°C
  Yanma havasi: 25°C --> 120°C

  Q_APH = m_hava × c_p_hava × (T_hava_cikis - T_hava_giris)
  Q_APH = 1.28 × 1.005 × (120 - 25)
  Q_APH = 122.2 kW

  Exergy kazanimi (yanma tarafinda):
  - Alev sicakligi artisi: 1,800 --> 1,860°C
  - I_yanma azalmasi: ~35 kW
  - Baca gazi exergy kazanimi: ~20 kW
  Toplam APH exergy kazanimi: ~55 kW
```

### 3.3 Kombine Etki (Ekonomizer + Hava On Isitici)

Her iki sistemi birlikte uygulamak:

```
Kombine senaryo:
  Baca gazi akisi: Kazan cikisi 210°C
    --> Ekonomizer: 210°C --> 165°C (besleme suyu on isitma)
    --> Hava on isitici: 165°C --> 130°C (yanma havasi isitma)
    --> Bacaya: 130°C

  Toplam I_AV azalmasi:
    Ekonomizer: ~58 kW
    Hava on isitici: ~32 kW (ekonomizer sonrasi daha dusuk T)
    Toplam: ~90 kW

  Yeni exergy verimi:
    epsilon_yeni = (980 + 90) / 2,800 = 1,070 / 2,800 = 0.382
    epsilon artisi: %35 --> %38.2 (3.2 puan iyilesme)
```

| Senaryo | epsilon | I_AV (kW) | Yatirim (EUR) | Geri Odeme |
|---|---|---|---|---|
| Mevcut durum | %35.0 | 189 | - | - |
| + Ekonomizer | %37.1 | 131 | 20,000 | 2.0 yil |
| + Hava on isitici | %36.3 | 134 | 18,000 | 1.8 yil |
| + Her ikisi | %38.2 | 99 | 35,000 | 2.2 yil |

## 4. Exergoekonomik Maliyet Hesabi (Exergoeconomic Cost Analysis)

### 4.1 Kacinilabilir Exergy Yikim Maliyeti

Ileri exergy analizinin en guclu uygulamalarindan biri, kacinilabilir exergy yikiminin parasal degerini hesaplamaktir.

```
Kacinilabilir exergy yikim maliyeti:
  C_D,k_AV = c_F × I_AV,k

  Burada:
  c_F = yakit exergetik birim maliyeti (fuel exergetic unit cost)
  I_AV,k = k bilesenindeki kacinilabilir exergy yikim hizi (kW)

Dogalgaz icin:
  Dogalgaz fiyati: 0.032 EUR/kWh (LHV bazli)
  Exergy/enerji orani (phi): 1.04
  c_F = 0.032 / 1.04 = 0.0308 EUR/kWh ~ 0.035 EUR/kWh
  (iletim, dagitim ve vergi dahil efektif deger)
```

### 4.2 Bilesen Bazinda Maliyet

```
Yillik kacinilabilir exergy yikim maliyeti:
  Calisma suresi: tau = 8,000 saat/yil

  Yanma odasi:
    I_AV = I_EN_AV + I_EX_AV = 52 + 35 = 87 kW
    C_D_AV = 0.035 × 87 × 8,000 = 24,360 EUR/yil

  Konveksiyon bolumu:
    I_AV = 22 + 15 = 37 kW
    C_D_AV = 0.035 × 37 × 8,000 = 10,360 EUR/yil

  Ekonomizer (potansiyel):
    I_AV = 58 + 7 = 65 kW
    C_D_AV = 0.035 × 65 × 8,000 = 18,200 EUR/yil

  Toplam kazan:
    I_AV_toplam = 87 + 37 + 65 = 189 kW
    C_D_AV_toplam = 0.035 × 189 × 8,000 = 52,920 EUR/yil
```

> **Onemli:** Bu deger (52,920 EUR/yil), kazandaki iyilestirme icin harcanabilecek maksimum
> yillik yatirim bedelini gosterir. Bunun ustunde yapilacak yatirim ekonomik olarak
> gerekcelendirilemez.

### 4.3 Exergoekonomik Faktor (Exergoeconomic Factor)

```
Exergoekonomik faktor:
  f_k = Z_k / (Z_k + C_D,k)

  Burada:
  Z_k = bilesenin yillik yatirim + bakim maliyeti (EUR/yil)
  C_D,k = bilesenin exergy yikim maliyeti (EUR/yil)

  Kazan icin:
    Z_kazan = 12,000 EUR/yil (amortisman + bakim)
    C_D_kazan = 52,920 EUR/yil (kacinilabilir kisim)

    f_kazan = 12,000 / (12,000 + 52,920) = 0.185

  Yorum: f < 0.5 --> Bilesene yatirim yaparak exergy yikimini
  azaltmak ekonomik olarak mantikli. Yani kazan icin ekonomizer,
  hava on isitici gibi yatirimlara oncelik verilmeli.
```

### 4.4 Yakit Tiplerine Gore Maliyet Karsilastirmasi

| Yakit Tipi | c_F (EUR/kWh) | I_AV (kW) | C_D_AV (EUR/yil) |
|---|---|---|---|
| Dogalgaz | 0.035 | 189 | 52,920 |
| Fuel oil No.6 | 0.030 | 210 | 50,400 |
| Biyokutle (pellet) | 0.028 | 245 | 54,880 |
| Komur (linyit) | 0.018 | 280 | 40,320 |

## 5. Farkli Yakit Tiplerinin Ileri Exergy Karsilastirmasi

### 5.1 Dogalgaz (Natural Gas)

```
Dogalgaz kazani:
  phi = 1.04 (exergy/LHV orani)
  Adyabatik alev sicakligi: ~2,050°C (stokiyometrik)
  Tipik exergy verimi: %33-38
  Yanma tersinmezligi orani: %70-80 (I_yanma / I_toplam)
  theta_kacinilabilir: %18-25
  Avantaj: Dusuk emisyon, yuksek modulasyon, kolay kontrol
```

### 5.2 Fuel Oil (No. 6, Agir Yakit)

```
Fuel oil kazani:
  phi = 1.06
  Adyabatik alev sicakligi: ~2,100°C
  Tipik exergy verimi: %30-35
  Yanma tersinmezligi orani: %72-82
  theta_kacinilabilir: %20-28
  Dezavantaj: SOx emisyonu, baca gazi asit yogusma T daha yuksek (~160°C)
    --> Ekonomizer cikis sicakligi daha yuksek tutulmali
    --> Daha az isi geri kazanimi
```

### 5.3 Biyokutle (Biomass — Pellet/Woodchip)

```
Biyokutle kazani:
  phi = 1.15-1.25 (nem icerigine bagli)
  Adyabatik alev sicakligi: ~1,400-1,600°C (dogalgazdan dusuk)
  Tipik exergy verimi: %22-30
  Yanma tersinmezligi orani: %75-85
  theta_kacinilabilir: %15-22
  Ozellik: Daha yuksek nem icerigi --> daha fazla exergy yikimi
           Ancak: karbon-notr yakit, cevre avantaji
```

### 5.4 Karsilastirma Tablosu

| Parametre | Dogalgaz | Fuel Oil | Biyokutle | Komur |
|---|---|---|---|---|
| phi (exergy/LHV) | 1.04 | 1.06 | 1.15-1.25 | 1.09 |
| T_alev (degC) | 2,050 | 2,100 | 1,400-1,600 | 1,900 |
| epsilon tipik (%) | 33-38 | 30-35 | 22-30 | 28-33 |
| theta (%) | 18-25 | 20-28 | 15-22 | 16-24 |
| I_yanma / I_top (%) | 70-80 | 72-82 | 75-85 | 73-83 |
| T_baca_min (degC) | 130 | 160 | 140 | 150 |
| CO2 (kg/kWh) | 0.20 | 0.28 | ~0 (notr) | 0.34 |

## 6. Adim Adim Hesaplama Kilavuzu (Step-by-Step Calculation Walkthrough)

### Adim 1: Gercek Sistem Analizi (Real System Analysis)

```
1a. Yakit exergy girisini hesapla:
    Ex_F = m_yakit × LHV × phi

1b. Urun exergy cikisini hesapla:
    Ex_P = m_buhar × [(h_buhar - h_0) - T_0 × (s_buhar - s_0)]
         - m_besleme × [(h_besleme - h_0) - T_0 × (s_besleme - s_0)]

1c. Her bilesen icin exergy yikimini hesapla:
    I_k = Ex_F,k - Ex_P,k (her bilesen k icin)

1d. Toplam exergy yikimini dogrula:
    I_toplam = SUM(I_k) = Ex_F - Ex_P - Ex_kayip
```

### Adim 2: Kacinilamaz Kosullari Tanimla (Define Unavoidable Conditions)

```
2a. Her bilesen icin en iyi teknolojik performansi belirle
    (literatur, uretici verileri, termodinamik limitler)

2b. Kacinilamaz parametreleri ata:
    - Yanma: min fazla hava, max hava on isitma T
    - Isi transferi: min delta_T, min baca T
    - Ekipman: min basinc kaybi, max izolasyon

2c. Kacinilamaz kosullarda her bileseni ayri ayri simule et
```

### Adim 3: Endojen/Eksojen Ayirimi (Endogenous/Exogenous Split)

```
3a. Hibrit cevrim yaklasimi (Hybrid cycle approach):
    - k bileseni gercek kosullarda calistir
    - Diger tum bilesenleri ideal kosullarda calistir
    - Bu durumda I_k = I_EN,k (endojen)

3b. Eksojen kismi hesapla:
    I_EX,k = I_k - I_EN,k

3c. Negatif eksojen deger kontrolu:
    Eger I_EX,k < 0 ise, bilesen diger bilesenlerden fayda
    goruyordur (nadir durum)
```

### Adim 4: Kacinilabilir/Kacinilamaz Ayirimi (Avoidable/Unavoidable Split)

```
4a. Kacinilamaz exergy yikimi:
    I_UN,k: k bileseni kacinilamaz kosullarda,
            diger bilesenler gercek kosullarda calistirildiginda

4b. Kacinilabilir exergy yikimi:
    I_AV,k = I_k - I_UN,k

4c. Dort bilesene ayirma:
    I_EN_UN,k: k gercek, digerler ideal, kacinilamaz kosullar
    I_EN_AV,k = I_EN,k - I_EN_UN,k
    I_EX_UN,k = I_UN,k - I_EN_UN,k
    I_EX_AV,k = I_EX,k - I_EX_UN,k
```

### Adim 5: Sonuclari Yorumla ve Onceliklendir

```
5a. Iyilestirme potansiyeli:
    theta_k = I_AV,k / I_k (her bilesen icin)

5b. Onceliklendirme (kacinilabilir yikim buyuklugune gore):
    Siralama: I_AV,1 > I_AV,2 > ... > I_AV,n

5c. Exergoekonomik degerlendirme:
    C_D_AV,k = c_F × I_AV,k × tau
    f_k = Z_k / (Z_k + C_D,k)
    f_k < 0.5 --> bilesene yatirim yap
    f_k > 0.5 --> mevcut bileseni daha verimli calistir
```

## 7. Pratik Sonuclar ve Operatorler Icin Rehber

### 7.1 Kazan Operatorleri Icin Temel Bulgular

1. **Yanma exergy yikimi yuksek ama musahade etmeyin:** Yanma tersinmezliginin %75-85'i kacinilamazdir. Odak noktaniz baca gazi ve isi transferi kayiplari olmalidir.

2. **Ekonomizer yoksa mutlaka ekleyin:** Ekonomizer en yuksek theta degerine sahip bilesendir. 4 ton/h kazan icin tipik geri odeme suresi 1.5-2.5 yildir.

3. **O2 trim kontrolu kurun:** Fazla havayi %20'den %8-12'ye dusurerek hem yakit tasarrufu hem de exergy verimi artisi saglayabilirsiniz.

4. **Baca gazi sicakligini izleyin:** Her 20 degC dusus, yaklasik %1 verim artisi ve ~15 kW exergy kazanimi saglar.

5. **Izolasyonu kontrol edin:** Kazan disyuzey sicakligi 50 degC'nin altinda olmalidir. Her 10 degC fazla yuzey sicakligi ~5-8 kW exergy kaybi demektir.

### 7.2 Tipik Kazan Ileri Exergy Profili

```
Tipik endüstriyel kazan ileri exergy dagılımı:

  I_EN_AV  : ████████░░░░░░░░░░░░  %15.5 (132 kW)
  I_EN_UN  : ████████████████████████████████████████████████████████████████████████  %70.4 (598 kW)
  I_EX_AV  : ███░░░░░░░░░░░░░░░░░  %6.7  (57 kW)
  I_EX_UN  : ████░░░░░░░░░░░░░░░░  %7.4  (63 kW)

  Kacinilabilir toplam: %22.2 (189 kW)
  Kacinilamaz toplam:   %77.8 (661 kW)
```

### 7.3 Karar Agaci (Decision Tree)

```
Kazan I_total > 500 kW ?
  |
  +--> Evet: theta > 0.25 ?
  |     |
  |     +--> Evet: Ekonomizer var mi?
  |     |     |
  |     |     +--> Hayir: EKONOMIZER EKLE (Oncelik 1)
  |     |     +--> Evet: Hava on isitici var mi?
  |     |           |
  |     |           +--> Hayir: HAVA ON ISITICI EKLE (Oncelik 2)
  |     |           +--> Evet: O2 trim kontrolu var mi?
  |     |                 |
  |     |                 +--> Hayir: O2 TRIM KUR (Oncelik 3)
  |     |                 +--> Evet: Kondense ekonomizer degerlendir
  |     |
  |     +--> Hayir (theta < 0.25):
  |           Kazan yakindan optimize edilmis.
  |           Eksojen kaynaklara bak (diger ekipmanlar).
  |
  +--> Hayir (I_total < 500 kW):
        Kucuk kazan, mutlak tasarruf sinirli.
        Basit onlemler: izolasyon, O2 kontrolu.
```

## 8. Sinirliliklari ve Dikkat Edilecek Noktalar

1. **Referans sicaklik etkisi:** T_0 secimi exergy hesaplarini onemli olcude etkiler. Turkiye icin yillik ortalama 15-18 degC kullanilmasi onerilir.

2. **Kacinilamaz kosul tanimlari subjektiftir:** Farkli arastirmacilar farkli kacinilamaz kosullar tanimlayabilir. Bu nedenle sonuclar %10-15 belirsizlik tasiyabilir.

3. **Dinamik calisma ihmal edilir:** Ileri exergy analizi genellikle kararli hal (steady-state) icin yapilir. Yuk degisimlerinde sonuclar farklilik gosterebilir.

4. **Eksojen hesap zorlugu:** Cok bilesenli sistemlerde eksojen exergy yikiminin dogru hesaplanmasi, her bilesen kombinasyonu icin ayri simulasyon gerektirir.

## İlgili Dosyalar

- `knowledge/boiler/formulas.md` -- Temel kazan exergy hesaplama formulleri
- `knowledge/boiler/benchmarks.md` -- Kazan verimlilik karsilastirma degerleri
- `knowledge/boiler/equipment/waste_heat.md` -- Atik isi kazani (HRSG) analizi
- `knowledge/factory/cross_equipment.md` -- Ekipmanlar arasi optimizasyon firsatlari
- `knowledge/factory/heat_integration.md` -- Isi entegrasyonu yontemleri
- `knowledge/factory/exergoeconomic/cost_analysis.md` -- Exergoekonomik maliyet analizi
- `knowledge/factory/advanced_exergy/methodology.md` -- Ileri exergy analizi genel metodoloji
- `skills/equipment/boiler_expert.md` -- Kazan AI uzman beceri dosyasi

## Referanslar

1. Tsatsaronis, G., & Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. DOI: 10.1016/S0196-8904(02)00012-2

2. Morosuk, T., & Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258. DOI: 10.1016/j.energy.2009.01.006

3. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T., & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. DOI: 10.1016/j.energy.2011.05.028

4. Kelly, S., Tsatsaronis, G., & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. DOI: 10.1016/j.energy.2008.12.007

5. Bejan, A., Tsatsaronis, G., & Moran, M. J. (1996). *Thermal Design and Optimization*. John Wiley & Sons. ISBN: 978-0-471-58467-4

6. Cziesla, F., Tsatsaronis, G., & Gao, Z. (2006). "Avoidable thermodynamic inefficiencies and costs in an externally fired combined cycle power plant." *Energy*, 31(10-11), 1472-1489. DOI: 10.1016/j.energy.2005.08.001
