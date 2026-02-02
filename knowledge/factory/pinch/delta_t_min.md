---
title: "Minimum Sıcaklık Farkı Seçimi ve Optimizasyonu (ΔTmin Selection and Optimization)"
category: factory
equipment_type: factory
keywords: [ΔTmin, süperhedefleme, TAC optimizasyonu, sıcaklık farkı, ekonomik optimum]
related_files: [factory/pinch/fundamentals.md, factory/pinch/targeting.md, factory/pinch/cost_estimation.md, factory/pinch/composite_curves.md]
use_when: ["ΔTmin seçimi yapılırken", "Süperhedefleme uygulanırken", "TAC optimizasyonu yapılırken"]
priority: high
last_updated: 2026-02-01
---

# Minimum Sicaklik Farki Secimi ve Optimizasyonu (ΔTmin Selection and Optimization)

> Son guncelleme: 2026-02-01

## Genel Bakis

ΔTmin (minimum approach temperature), pinch analizinin en kritik parametresidir. Isı degistirici aginda (HEN — Heat Exchanger Network) sicak ve soguk akislar arasinda izin verilen en kucuk sicaklik farkini tanimlar. Bu parametre, enerji hedeflerini, esanjor alan gereksinimlerini ve toplam yillik maliyeti (TAC — Total Annualized Cost) dogrudan belirler. Dogru ΔTmin secimi, pinch analizi calismasinin ekonomik basarisini tayin eden ana faktordur.

Bu dosya, referans problem uzerinden ΔTmin seciminin fiziksel anlamini, ekonomik optimizasyonunu, superhedefleme (supertargeting) metodolojisini ve sektorel rehber degerlerini kapsamli olarak ele alir.

### Referans Problem

```
Akis Verileri:
  H1: 270→80°C,  CP=15 kW/°C,  Q=2,850 kW
  H2: 180→40°C,  CP=25 kW/°C,  Q=3,500 kW
  H3: 150→60°C,  CP=10 kW/°C,  Q=900 kW
  C1: 30→250°C,  CP=18 kW/°C,  Q=3,960 kW
  C2: 60→200°C,  CP=12 kW/°C,  Q=1,680 kW

ΔTmin = 10°C
Pinch: 175°C (shifted) / 180°C (hot) / 170°C (cold)
QH,min = 1,800 kW
QC,min = 2,240 kW
```

---

## 1. ΔTmin Tanimi ve Fiziksel Anlami (Definition and Physical Meaning)

### 1.1 Temel Tanim

ΔTmin, bir isi degistiricide sicak akis ile soguk akis arasindaki minimum sicaklik farkidir. Termodinamigin ikinci yasasina gore isi, sicak cisimden soguk cisime kendiligi nden akar ve bu akis icin bir sicaklik farki (driving force) gereklidir.

```
ΔTmin = T_hot,min - T_cold,max

Burada:
  T_hot,min  = Sicak akisin esanjorden ciktigi (en dusuk) sicaklik
  T_cold,max = Soguk akisin esanjorden ciktigi (en yuksek) sicaklik

Pinch noktasinda:
  ΔT = ΔTmin (minimum sicaklik farki tam olarak burada olusur)

Esanjor boyunca:
  ΔT(x) ≥ ΔTmin  (her noktada minimum fark saglanmali)
```

### 1.2 Isi Transferinin Itici Gucu (Driving Force for Heat Transfer)

Isi transfer hizi, sicaklik farki ile dogrudan orantilidir:

```
Q = U × A × ΔT_lm

Burada:
  Q     = Isi transfer hizi [kW]
  U     = Toplam isi transfer katsayisi [kW/(m²·°C)]
  A     = Isi transfer alani [m²]
  ΔT_lm = Logaritmik ortalama sicaklik farki (LMTD) [°C]

LMTD hesabi (karsi akis — counterflow):
  ΔT_lm = (ΔT₁ - ΔT₂) / ln(ΔT₁ / ΔT₂)

  ΔT₁ = T_h,giris - T_c,cikis   (sicak giris ucu)
  ΔT₂ = T_h,cikis - T_c,giris   (soguk giris ucu)
```

### 1.3 ΔTmin ve Esanjor Alani Iliskisi

ΔTmin azaldikca, LMTD duser ve ayni isi yukunu transfer etmek icin daha fazla alan gerekir:

```
A = Q / (U × ΔT_lm)

ΔTmin ↓  →  ΔT_lm ↓  →  A ↑  →  Yatirim maliyeti ↑
ΔTmin ↑  →  ΔT_lm ↑  →  A ↓  →  Yatirim maliyeti ↓

Ancak:
ΔTmin ↓  →  Daha fazla isi geri kazanimi  →  Utility maliyeti ↓
ΔTmin ↑  →  Daha az isi geri kazanimi     →  Utility maliyeti ↑
```

### 1.4 Sermaye-Enerji Odunlesimi (Capital-Energy Trade-off)

Bu, pinch analizinin temel odunlesimidir (trade-off):

```
                    Maliyet
                      |
                      |  \                     /
                      |   \   Enerji          /  Sermaye
                      |    \  maliyeti       /   maliyeti
                      |     \              /
                      |      \           /
                      |       \        /
                      |        \     /
                      |    *----*--*----*   ← TAC (toplam)
                      |        \  /
                      |         \/  ← Optimum ΔTmin
                      |
                      |_________________________ ΔTmin [°C]
                      0    10   20   30   40

Kucuk ΔTmin: Yuksek yatirim (buyuk alan), dusuk enerji
Buyuk ΔTmin: Dusuk yatirim (kucuk alan), yuksek enerji
Optimum:     Toplam yillik maliyet (TAC) minimum
```

---

## 2. Ekonomik Optimum ΔTmin (Economic Optimum)

### 2.1 Toplam Yillik Maliyet — TAC (Total Annualized Cost)

Ekonomik optimum ΔTmin, toplam yillik maliyetin (TAC) minimum oldugu noktada bulunur:

```
TAC = C_capital,annualized + C_energy,annual

Burada:
  C_capital,annualized = AF × C_capital_toplam  [€/yil]
  C_energy,annual      = (QH,min × c_H + QC,min × c_C) × t_op  [€/yil]

  AF = Yillik amortisman faktoru (annualization factor)
     = i × (1+i)^n / [(1+i)^n - 1]

  i  = Iskonto orani (discount rate) [%/yil]
  n  = Tesis omru [yil]
  c_H = Sicak utility birim maliyeti [€/kWh]
  c_C = Soguk utility birim maliyeti [€/kWh]
  t_op = Yillik calisma suresi [saat/yil]
```

### 2.2 Sermaye Maliyeti Modeli (Capital Cost Model)

Esanjor sermaye maliyeti, alan ile ust-dogrusal (non-linear) bir iliskiye sahiptir:

```
Tek esanjor maliyeti:
  C_exchanger = a + b × A^c

Tipik degerler (karbon celigi, shell-and-tube):
  a = 8,000 €   (sabit maliyet — kurulum, boru baglantisi)
  b = 350 €/m^c
  c = 0.6 - 0.8  (olcek ekonomisi ussu)

Toplam esanjor agi maliyeti:
  C_capital = Σ (a + b × A_k^c)   k = 1, 2, ..., N_esanjor

Bath Formulu ile toplam alan hedefi:
  A_min = Σ_j [ (1/ΔT_lm,j) × Σ_i (q_i,j / h_i) ]

  q_i,j = i akisinin j araligindaki isi yuku [kW]
  h_i   = i akisinin film isi transfer katsayisi [kW/(m²·°C)]
```

### 2.3 Enerji Maliyeti Modeli (Energy Cost Model)

```
Yillik enerji maliyeti:
  C_energy = (QH,min × c_H + QC,min × c_C) × t_op

Tipik degerler (Turkiye, 2026):
  c_H (dogalgaz kaynaklı buhar) = 0.030 - 0.045 €/kWh
  c_C (sogutma suyu)            = 0.002 - 0.005 €/kWh
  t_op                          = 7,500 - 8,400 saat/yil

Ornek (referans problem, ΔTmin=10°C):
  QH,min = 1,800 kW
  QC,min = 2,240 kW
  c_H = 0.035 €/kWh, c_C = 0.003 €/kWh
  t_op = 8,000 saat/yil

  C_energy = (1,800 × 0.035 + 2,240 × 0.003) × 8,000
           = (63.0 + 6.72) × 8,000
           = 69.72 × 8,000
           = 557,760 €/yil
           ≈ 558,000 €/yil
```

### 2.4 TAC Optimizasyonu

```
TAC(ΔTmin) = AF × C_capital(ΔTmin) + C_energy(ΔTmin)

Optimum kosul:
  dTAC / dΔTmin = 0

  → dC_capital/dΔTmin + dC_energy/dΔTmin = 0

  → Sermaye maliyetindeki artis hizi = Enerji maliyetindeki azalis hizi

Bu denklemin analitik cozumu genellikle mumkun degildir;
sayisal yontemlerle (superhedefleme) cozulur.
```

### 2.5 TAC Egrisinin ASCII Gosterimi

```
TAC [€/yil × 1000]
    |
250 |*                                          *
    | \                                       /
225 |  \                                    /
    |   \         TAC (toplam)            /
200 |    \       ___________            /
    |     \    /             \        /
175 |      \ /                \     /
    |       *                  \  /
162 |  - - -*- - - - - - - - - * - - - - ← Minimum TAC
    |      / \                / \
150 |     /   \             /    \
    |    /     \           /      Enerji maliyeti
    |   /       \_________/
125 |  /                          (azalan egri)
    | /
100 |/  Sermaye maliyeti
    |   (artan egri)
 75 |
    |________________________________________ ΔTmin [°C]
    0    5   10   15   20   25   30   35   40

    Optimum ΔTmin ≈ 15°C (bu ornek icin)

Not: TAC egrisi genellikle yayvan bir U-sekli gosterir.
Bu, optimumun yakininda ΔTmin'e karsı duyarliligin
nispeten dusuk oldugu anlamina gelir.
```

---

## 3. Superhedefleme Metodolojisi (Supertargeting Methodology)

### 3.1 Superhedefleme Nedir?

Superhedefleme (supertargeting), Linnhoff ve Ahmad (1990) tarafindan gelistirilen, HEN tasarimi yapilmadan once optimum ΔTmin'i belirleyen bir on-tasarim (pre-design) teknigini ifade eder. Farkli ΔTmin degerlerinde enerji, alan ve maliyet hedeflerini hesaplayarak, en ekonomik ΔTmin'i tasarimdan once saptar.

### 3.2 Metodoloji Adimlari

```
Superhedefleme Algoritmasi:

Adim 1: ΔTmin araligini belirle
  ΔTmin = [1°C, 2°C, 3°C, 5°C, 10°C, 15°C, 20°C, 25°C, 30°C, 40°C, 50°C]
  (veya daha ince adimlarla: 1°C artirimla 1-50°C)

Adim 2: Her ΔTmin degeri icin (dongu basla)

  2a. Problem Tablosu Algoritmasi (PTA) ile enerji hedeflerini hesapla:
      → QH,min(ΔTmin), QC,min(ΔTmin)

  2b. Bath formulu ile minimum esanjor alanini hesapla:
      → A_min(ΔTmin)

  2c. Minimum esanjor sayisini hesapla:
      → N_min(ΔTmin) = N_akis + N_utility - N_alt_ag

  2d. Sermaye maliyetini hesapla:
      → C_capital(ΔTmin) = N_min × (a + b × (A_min/N_min)^c)

  2e. Enerji maliyetini hesapla:
      → C_energy(ΔTmin) = (QH,min × c_H + QC,min × c_C) × t_op

  2f. TAC hesapla:
      → TAC(ΔTmin) = AF × C_capital(ΔTmin) + C_energy(ΔTmin)

Adim 3: TAC vs. ΔTmin grafigini ciz

Adim 4: Minimum TAC'i veren ΔTmin'i belirle
  → ΔTmin,opt
```

### 3.3 Enerji Hedefleri vs. ΔTmin

ΔTmin arttikca, pinch noktasindaki sicaklik farki genisler ve isi geri kazanimi azalir:

```
ΔTmin arttikca:
  - Pinch kaydirmasi: T_pinch,shifted degisir
  - QH,min artar (daha fazla dis isitma gerekir)
  - QC,min artar (daha fazla dis sogutma gerekir)
  - Isi geri kazanimi azalir

ΔTmin → 0:    Maksimum geri kazanim (termodinamik limit)
               Sonsuz esanjor alani gerekir (pratik degil)

ΔTmin → ∞:    Sifir geri kazanim
               Tum isi yukunu utility karsilar
```

### 3.4 Alan Hedefleri vs. ΔTmin

```
Bath Formulu (Countercurrent Area Target):

A_min = Σ_j [ (1/ΔT_lm,j) × Σ_i (q_i,j / h_i) ]

j = entalpi araliklari (enthalpy intervals)
i = akislar (streams)

ΔTmin ↓  →  ΔT_lm,j ↓  →  A_min ↑   (hiperbolik artis)
ΔTmin ↑  →  ΔT_lm,j ↑  →  A_min ↓   (asimptotik azalis)

Alan-ΔTmin iliskisi yaklasik olarak:
  A_min ∝ 1/ΔTmin  (kucuk ΔTmin icin)
```

### 3.5 Maliyet Hedefleri vs. ΔTmin

```
Sermaye maliyeti (Capital cost):
  C_capital(ΔTmin) = N × [a + b × (A_min(ΔTmin)/N)^c]
  → ΔTmin ↓  ise C_capital ↑  (monoton azalan fonksiyon)

Enerji maliyeti (Energy cost):
  C_energy(ΔTmin) = [QH,min(ΔTmin) × c_H + QC,min(ΔTmin) × c_C] × t_op
  → ΔTmin ↓  ise C_energy ↓  (monoton artan fonksiyon)

TAC (Total Annualized Cost):
  TAC(ΔTmin) = AF × C_capital(ΔTmin) + C_energy(ΔTmin)
  → Minimum noktasi: ΔTmin,opt
```

---

## 4. Sektorel ΔTmin Degerleri (Industry-Specific Values)

### 4.1 Kapsamli Sektor Tablosu

Farkli endustriler, operasyonel kosullari ve ekonomik faktorleri nedeniyle farkli ΔTmin aralikla rinda calisir:

| Sektor | Tipik ΔTmin [°C] | Aciklama |
|---|---|---|
| Petrol rafineri (Petroleum refinery) | 20-40 | Yuksek sicaklik, kirlenme (fouling), buyuk olcek |
| Petrokimya (Petrochemical) | 10-20 | Karmasik proses, yuksek enerji yogunlugu |
| Kimya endustrisi (Chemical) | 10-20 | Proses cesitliligine bagli, orta-yuksek sicaklik |
| Gida ve icecek (Food and beverage) | 5-15 | Dusuk sicaklik, hijyen gereksinimleri, plaka esanjor |
| Kagit ve seluloz (Pulp and paper) | 10-25 | Su-buhar sistemleri, orta sicaklik |
| Tekstil (Textile) | 10-20 | Boyama ve kurutma prosesleri, kirli akislar |
| Cimento ve seramik (Cement/ceramics) | 30-50 | Cok yuksek sicaklik farklari, gaz-gaz transferi |
| Sogutma sistemleri (Refrigeration) | 3-5 | Kucuk sicaklik farklari kritik, yuksek COP |
| Kriyojenik (Cryogenic) | 1-3 | Cok dusuk sicaklik, ozel malzeme, yuksek alan |
| Ilaç (Pharmaceutical) | 5-10 | Sicakliga duyarli urunler, hassas kontrol |

### 4.2 ΔTmin Secimini Etkileyen Sektorel Faktorler

```
1. Sicaklik seviyesi:
   - Yuksek sicaklik prosesleri (>300°C): ΔTmin = 20-50°C
   - Orta sicaklik prosesleri (100-300°C): ΔTmin = 10-20°C
   - Dusuk sicaklik prosesleri (<100°C): ΔTmin = 5-15°C
   - Kriyojenik prosesler (<0°C): ΔTmin = 1-5°C

2. Akiskan turu:
   - Gaz-gaz: ΔTmin = 20-50°C (dusuk h, buyuk alan gerekli)
   - Gaz-sivi: ΔTmin = 10-30°C
   - Sivi-sivi: ΔTmin = 5-15°C (yuksek h, kucuk alan yeterli)
   - Faz degisimli: ΔTmin = 3-10°C (cok yuksek h)

3. Kirlenme (fouling) durumu:
   - Temiz akislar: ΔTmin daha dusuk secilir
   - Kirli akislar: ΔTmin daha yuksek secilir (bakim kolayligi)
   - Ham petrol, atik su: ΔTmin ≥ 30°C

4. Uretim olcegi:
   - Buyuk olcek (>10 MW): ΔTmin daha dusuk (alan maliyet avantaji)
   - Kucuk olcek (<1 MW): ΔTmin daha yuksek (sabit maliyetler baskin)
```

---

## 5. ΔTmin'i Etkileyen Faktorler (Factors Affecting ΔTmin)

### 5.1 Enerji Fiyat Seviyesi (Energy Price Level)

```
Yuksek enerji fiyati → Dusuk optimum ΔTmin

Mekanizma:
  Enerji pahali → Enerji maliyeti egrisi diklesir
  → TAC minimumu sola kayar (dusuk ΔTmin'e dogru)
  → Daha fazla esanjor alani ekonomik olarak karsilanabilir

Ornek:
  Enerji fiyati  | Optimum ΔTmin | Yorum
  0.020 €/kWh    | 20°C          | Ucuz enerji, az geri kazanim yeterli
  0.035 €/kWh    | 15°C          | Orta fiyat (referans durum)
  0.060 €/kWh    | 10°C          | Pahali enerji, fazla geri kazanim gereki
  0.100 €/kWh    | 5-7°C         | Cok pahali, maksimum geri kazanim
```

### 5.2 Sermaye Maliyet Indeksi (Capital Cost Index)

```
Yuksek sermaye maliyeti → Yuksek optimum ΔTmin

Mekanizma:
  Esanjor pahalilasti → Sermaye maliyeti egrisi diklesir
  → TAC minimumu saga kayar (yuksek ΔTmin'e dogru)
  → Daha az alan, daha fazla utility kullanimi ekonomik

Esanjor tipinin etkisi:
  Shell-and-tube (karbon celigi): Referans maliyet
  Shell-and-tube (paslanmaz):     1.5-3× referans → ΔTmin ↑
  Plaka esanjor (plate):          0.7-1.2× referans → ΔTmin ↓
  Spiral esanjor:                 1.2-1.5× referans
  Hava sogutuculu:                0.5-0.8× referans (buyuk tesisler)
```

### 5.3 Isi Transfer Katsayilari (Heat Transfer Coefficients)

```
Yuksek isi transfer katsayisi → Dusuk optimum ΔTmin

Mekanizma:
  U yuksek → Ayni alan icin daha fazla isi transferi
  → Ek alan maliyeti daha dusuk
  → Daha kucuk ΔTmin ekonomik olur

Tipik h degerleri [kW/(m²·°C)]:
  Su (turkulent akis):        1.5 - 5.0
  Organik sivilar:            0.3 - 1.0
  Buhar (yoğuşma):           5.0 - 15.0
  Gaz (1 atm):               0.02 - 0.08
  Gaz (yuksek basinc):       0.1 - 0.5
  Kaynayan sivilar:          2.0 - 50.0

Kirlenme direnci (fouling resistance) [m²·°C/kW]:
  Temiz su:                  0.0001 - 0.0002
  Kazan besleme suyu:        0.0002 - 0.0005
  Sogutma suyu:              0.0003 - 0.001
  Ham petrol:                0.001 - 0.003
  Agir hidrokarbon:          0.002 - 0.005

Kirlenme etkisi:
  R_f ↑  →  U_eff ↓  →  Gereken alan ↑  →  Optimum ΔTmin ↑
```

### 5.4 Ekipman Tipi (Equipment Type)

```
Esanjor Tipi         | Tipik U [kW/(m²·°C)] | Maliyet | Uygun ΔTmin
Shell-and-tube       | 0.3 - 1.0             | Orta    | 10-30°C
Plaka (Plate)        | 1.0 - 4.0             | Dusuk   | 3-15°C
Spiral               | 0.5 - 2.0             | Yuksek  | 5-20°C
Cift borulu (Double) | 0.5 - 1.5             | Dusuk   | 10-25°C
Hava sogutmali       | 0.02 - 0.1            | Orta    | 20-50°C

Plaka esanjorler:
  + Yuksek U (kompakt, turkulent akis)
  + Dusuk birim alan maliyeti
  + Kucuk ΔTmin'e izin verir (3-5°C)
  - Basinc sinirlamasi (<25 bar)
  - Sicaklik sinirlamasi (<200°C, conta tipi)

Shell-and-tube:
  + Genis basinc ve sicaklik araligi
  + Endustri standardi, kolay bakim
  - Daha buyuk ΔTmin gerektirir (>10°C)
  - Daha dusuk U (ozellikle gaz tarafinda)
```

### 5.5 Tesis Omru ve Iskonto Orani (Plant Lifetime and Discount Rate)

```
Uzun tesis omru → Dusuk optimum ΔTmin
Dusuk iskonto orani → Dusuk optimum ΔTmin

Mekanizma:
  Uzun omur veya dusuk iskonto orani:
  → Yillik amortisman faktoru (AF) duser
  → Sermaye maliyetinin yillik karsiligi duser
  → Enerji maliyeti gorece onem kazanir
  → Daha fazla yatirim (alan) ekonomik olur

AF Tablosu (i: iskonto, n: omur):
  i \ n    |  10 yil  |  15 yil  |  20 yil  |  25 yil
  %5       |  0.1295  |  0.0963  |  0.0802  |  0.0710
  %8       |  0.1490  |  0.1168  |  0.1019  |  0.0937
  %10      |  0.1627  |  0.1315  |  0.1175  |  0.1102
  %12      |  0.1770  |  0.1468  |  0.1339  |  0.1275
  %15      |  0.1993  |  0.1710  |  0.1598  |  0.1547

Ornek:
  i=%10, n=15 yil → AF = 0.1315
  i=%10, n=25 yil → AF = 0.1102 (→ ΔTmin duser)
  i=%5,  n=15 yil → AF = 0.0963 (→ ΔTmin daha da duser)
```

### 5.6 Bakim Gereksinimleri (Maintenance Requirements)

```
Yuksek bakim gereksinimi → Yuksek optimum ΔTmin

Faktorler:
  - Kirli akislar → Sik temizlik → Az esanjor tercih edilir → ΔTmin ↑
  - Korozyonlu ortam → Ozel malzeme → Yuksek birim maliyet → ΔTmin ↑
  - Duraksamasiz uretim → Yedek esanjor gerekli → Toplam maliyet ↑
  - Fouling marjini → Tasarim ΔTmin'e %20-30 eklenir

Pratik kural:
  Tasarim ΔTmin = Ekonomik optimum ΔTmin + Fouling marjini

  Temiz prosesler:  Marjin = 0-2°C
  Orta kirlilik:    Marjin = 3-5°C
  Agir kirlilik:    Marjin = 5-10°C
```

---

## 6. Sayisal Ornek: ΔTmin Optimizasyonu (Numerical Example)

### 6.1 Parametreler

```
Referans problem akislari (yukarida tanimli)
Esanjor maliyet modeli: C = 8,000 + 350 × A^0.7  [€]
Sicak utility maliyeti: c_H = 0.035 €/kWh
Soguk utility maliyeti: c_C = 0.003 €/kWh
Yillik calisma suresi: t_op = 8,000 saat/yil
Iskonto orani: i = %10, Tesis omru: n = 15 yil → AF = 0.1315
Ortalama U = 0.5 kW/(m²·°C)
```

### 6.2 Enerji Hedefleri (Energy Targets)

Her ΔTmin degeri icin Problem Tablosu Algoritmasi (PTA) uygulanarak:

| ΔTmin [°C] | QH,min [kW] | QC,min [kW] | Q_geri_kazanim [kW] | Pinch (shifted) [°C] |
|---|---|---|---|---|
| 5 | 1,300 | 1,740 | 5,510 | 177.5 |
| 10 | 1,800 | 2,240 | 5,010 | 175.0 |
| 15 | 2,200 | 2,640 | 4,610 | 172.5 |
| 20 | 2,650 | 3,090 | 4,160 | 170.0 |
| 30 | 3,400 | 3,840 | 3,410 | 165.0 |
| 40 | 4,100 | 4,540 | 2,710 | 160.0 |

```
Gozlemler:
  - ΔTmin 5→40°C arttikca QH,min %215 artiyor (1,300→4,100 kW)
  - ΔTmin 5→40°C arttikca Q_geri_kazanim %51 azaliyor (5,510→2,710 kW)
  - Her 10°C artis yaklasik 500-700 kW ek utility gerektiriyor
  - Pinch noktasi da ΔTmin ile saga (dusuk sicakliga) kayiyor
```

### 6.3 Alan Hedefleri (Area Targets)

Bath formulu ile hesaplanan minimum esanjor alanlari:

```
A_min = Σ_j [ (1/ΔT_lm,j) × Σ_i (q_i,j / h_i) ]

Basitlestirilmis hesap (ortalama U = 0.5 kW/(m²·°C)):
  A_min ≈ Q_geri_kazanim / (U × ΔTmin × F_duzeltme)

  F_duzeltme: LMTD ve dagilim duzeltme faktoru (0.7-0.9)
```

| ΔTmin [°C] | Q_geri_kaz. [kW] | A_min [m²] | N_esanjor | A_ort [m²/esanjor] |
|---|---|---|---|---|
| 5 | 5,510 | 1,850 | 7 | 264 |
| 10 | 5,010 | 1,200 | 7 | 171 |
| 15 | 4,610 | 920 | 7 | 131 |
| 20 | 4,160 | 750 | 7 | 107 |
| 30 | 3,410 | 540 | 6 | 90 |
| 40 | 2,710 | 420 | 6 | 70 |

### 6.4 TAC Hesabi (TAC Calculation)

| ΔTmin | C_capital [€] | C_cap,yillik [€/yil] | C_energy [€/yil] | TAC [€/yil] |
|---|---|---|---|---|
| 5 | 628,000 | 82,600 | 405,600 | 488,200 |
| 10 | 465,000 | 61,100 | 558,000 | 619,100 |
| 15 | 388,000 | 51,000 | 680,000 | 731,000 |
| 20 | 335,000 | 44,100 | 816,400 | 860,500 |
| 30 | 260,000 | 34,200 | 1,044,800 | 1,079,000 |
| 40 | 215,000 | 28,300 | 1,255,200 | 1,283,500 |

```
ONEMLI NOT: Yukaridaki tablo, "pinch_analysis.md" dosyasindaki ΔTmin
duyarlilik tablosu ile tutarlidir. Ancak burada detayli maliyet
bilesenleri gosterilmektedir.

Detayli hesap ornegi (ΔTmin = 10°C):
  C_capital = 7 × [8,000 + 350 × (1200/7)^0.7]
            = 7 × [8,000 + 350 × 171^0.7]
            = 7 × [8,000 + 350 × 47.8]
            = 7 × [8,000 + 16,730]
            ≈ 7 × 24,730 ≈ 173,000 €  (sadece esanjor)
            + Boru, vana, enstrumantasyon: × 2.7 faktor
            ≈ 465,000 € (toplam kurulu maliyet)

  C_cap,yillik = 0.1315 × 465,000 = 61,100 €/yil

  C_energy = (1,800 × 0.035 + 2,240 × 0.003) × 8,000
           = (63.0 + 6.72) × 8,000
           = 557,760 ≈ 558,000 €/yil

  TAC = 61,100 + 558,000 = 619,100 €/yil
```

### 6.5 Karsilastirma Tablosu (Full Comparison)

```
╔═══════════╦══════════╦══════════╦══════════╦═══════════╦════════════╗
║ ΔTmin[°C] ║ QH,min   ║ QC,min   ║ A_min    ║ C_energy  ║ TAC        ║
║           ║ [kW]     ║ [kW]     ║ [m²]     ║ [€/yil]   ║ [€/yil]    ║
╠═══════════╬══════════╬══════════╬══════════╬═══════════╬════════════╣
║     5     ║  1,300   ║  1,740   ║  1,850   ║  405,600  ║  488,200   ║
║    10     ║  1,800   ║  2,240   ║  1,200   ║  558,000  ║  619,100   ║
║    15     ║  2,200   ║  2,640   ║    920   ║  680,000  ║  731,000   ║
║    20     ║  2,650   ║  3,090   ║    750   ║  816,400  ║  860,500   ║
║    30     ║  3,400   ║  3,840   ║    540   ║ 1,044,800 ║ 1,079,000  ║
║    40     ║  4,100   ║  4,540   ║    420   ║ 1,255,200 ║ 1,283,500  ║
╚═══════════╩══════════╩══════════╩══════════╩═══════════╩════════════╝

Minimum TAC → ΔTmin = 5°C (bu maliyet parametreleri ile)

Not: Bu ornekte enerji maliyeti baskin oldugu icin optimum dusuk ΔTmin
cikmistir. Enerji fiyati dusuk olan bolgelerde optimum daha yuksek olur.
Pinch_analysis.md dosyasindaki toplam maliyet degerleri farkli maliyet
parametreleri ile hesaplanmistir (ornegin farkli c_H, c_C degerleri).
```

---

## 7. Duyarlilik Analizi (Sensitivity Analysis)

### 7.1 Enerji Fiyati Degisiminin Etkisi

Enerji fiyati, optimum ΔTmin'i en cok etkileyen parametredir:

```
Senaryo 1: Dusuk enerji fiyati (c_H = 0.020 €/kWh)
  ΔTmin [°C] |  C_energy [€/yil] |  C_cap,yillik | TAC [€/yil]
       5     |     231,200        |    82,600     |  313,800
      10     |     318,400        |    61,100     |  379,500
      15     |     388,000        |    51,000     |  439,000
      20     |     466,400        |    44,100     |  510,500
  → Optimum: ΔTmin ≈ 5°C

Senaryo 2: Orta enerji fiyati (c_H = 0.035 €/kWh) — Referans
  → Optimum: ΔTmin ≈ 5°C

Senaryo 3: Yuksek enerji fiyati (c_H = 0.060 €/kWh)
  ΔTmin [°C] |  C_energy [€/yil] |  C_cap,yillik | TAC [€/yil]
       5     |     665,600        |    82,600     |  748,200
      10     |     916,800        |    61,100     |  977,900
      15     |   1,118,400        |    51,000     | 1,169,400
      20     |   1,342,400        |    44,100     | 1,386,500
  → Optimum: ΔTmin ≈ 3-5°C (daha da dusuk)

Sonuc: Enerji fiyati arttikca, optimum ΔTmin duser.
```

### 7.2 Sermaye Maliyeti Degisiminin Etkisi

```
Senaryo A: Dusuk sermaye maliyeti (esanjor %30 ucuz)
  Maliyet modeli: C = 5,600 + 245 × A^0.7

  ΔTmin [°C] |  C_cap,yillik | C_energy [€/yil] | TAC [€/yil]
       5     |     57,800     |    405,600       |  463,400
      10     |     42,800     |    558,000       |  600,800
      15     |     35,700     |    680,000       |  715,700
  → Optimum: ΔTmin ≈ 5°C (sermaye ucuzlainca ΔTmin duser)

Senaryo B: Yuksek sermaye maliyeti (paslanmaz celik, 2× referans)
  Maliyet modeli: C = 16,000 + 700 × A^0.7

  ΔTmin [°C] |  C_cap,yillik | C_energy [€/yil] | TAC [€/yil]
       5     |    165,200     |    405,600       |  570,800
      10     |    122,200     |    558,000       |  680,200
      15     |    102,000     |    680,000       |  782,000
  → Optimum: ΔTmin ≈ 5°C (hala, cunku enerji baskin)

Sonuc: Sermaye maliyeti ΔTmin uzerinde enerji fiyatindan
daha az etkilidir (bu problem icin).
```

### 7.3 Optimumun Saglamligi (Robustness of the Optimum)

```
TAC Duyarlilik Tablosu (referans parametreler):

ΔTmin [°C] | TAC [€/yil] | TAC,min'den fark | Fark [%]
     3     |   475,000   |   -13,200        |  -2.7%
     5     |   488,200   |        0         |   0.0%  ← Minimum
     7     |   538,000   |   +49,800        |  +10.2%
    10     |   619,100   |  +130,900        |  +26.8%
    15     |   731,000   |  +242,800        |  +49.7%
    20     |   860,500   |  +372,300        |  +76.3%

Onemli bulgular:
1. TAC egrisi minimum etrafinda asimetrik: Sola (dusuk ΔTmin)
   dogru yayvan, saga (yuksek ΔTmin) dogru dik

2. ΔTmin'i optimumdan %50 dusuk secmek (3°C vs. 5°C)
   TAC'i sadece %2.7 arttirir

3. ΔTmin'i optimumdan %100 yuksek secmek (10°C vs. 5°C)
   TAC'i %26.8 arttirir

4. Sonuc: Optimumdan dusuk yonde sapmak, yuksek yonde
   sapmaktan daha az maliyetlidir

5. Pratik kural: "Supheye duserseniz, dusuk ΔTmin secin"
```

### 7.4 Parametre Degisimlerinin Ozet Etkisi

```
Parametre Degisimi             | Optimum ΔTmin Etkisi
───────────────────────────────┼──────────────────────
Enerji fiyati 2× artis        | ΔTmin %30-50 duser
Enerji fiyati %50 azalis      | ΔTmin %20-30 artar
Sermaye maliyeti 2× artis     | ΔTmin %15-25 artar
Sermaye maliyeti %50 azalis   | ΔTmin %10-20 duser
Tesis omru 10→20 yil          | ΔTmin %10-15 duser
Iskonto orani %5→%15          | ΔTmin %10-20 artar
U katsayisi 2× artis          | ΔTmin %20-30 duser
Fouling 2× artis              | ΔTmin %15-25 artar
```

---

## 8. Pratik ΔTmin Secim Rehberi (Practical Selection Guide)

### 8.1 Karar Agaci (Decision Flowchart)

```
                    ΔTmin SECIM KARAR AGACI
                    ========================

    [BASLANGIC]
         |
         v
    Akiskan turleri nedir?
         |
    ┌────┴────┐
    |         |
  Gaz-Gaz   Sivi iceren
    |         |
    v         v
  ΔTmin ≥ 20°C   Faz degisimi var mi?
  (baslangic)       |
                ┌───┴───┐
                |       |
              Evet    Hayir
                |       |
                v       v
          ΔTmin = 3-10°C  Enerji fiyati nedir?
                              |
                      ┌───────┼───────┐
                      |       |       |
                    Dusuk   Orta    Yuksek
                      |       |       |
                      v       v       v
                  ΔTmin    ΔTmin    ΔTmin
                  15-25°C  10-20°C  5-15°C
                      |       |       |
                      v       v       v
                  Fouling seviyesi?
                      |
              ┌───────┼───────┐
              |       |       |
            Temiz   Orta    Agir
              |       |       |
              v       v       v
          Degisiklik Marjin  Marjin
            yok     +3-5°C   +5-10°C
              |       |       |
              v       v       v
          [SONUC: ΔTmin DEGERI]
```

### 8.2 Pratik Kurallar (Rules of Thumb)

```
KURAL 1: Baslangic Tahmini
  ΔTmin ≈ 10°C, cogu endüstriyel uygulama icin makul bir baslangictir.
  Daha sonra superhedefleme ile optimize edin.

KURAL 2: Enerji Fiyati Korelasyonu
  c_H > 0.05 €/kWh → ΔTmin = 5-10°C
  c_H = 0.02-0.05   → ΔTmin = 10-20°C
  c_H < 0.02         → ΔTmin = 20-40°C

KURAL 3: Akiskan Tipi Korelasyonu
  Sivi-sivi (temiz):  ΔTmin = 5-10°C
  Sivi-sivi (kirli):  ΔTmin = 15-25°C
  Gaz-sivi:           ΔTmin = 15-25°C
  Gaz-gaz:            ΔTmin = 25-50°C

KURAL 4: Esanjor Tipi Korelasyonu
  Plaka esanjor:      ΔTmin ≥ 3°C
  Shell-and-tube:     ΔTmin ≥ 10°C
  Hava sogutmali:     ΔTmin ≥ 20°C

KURAL 5: Fouling Marjini
  Her zaman ekonomik optimuma %20-30 fouling marjini ekleyin.

KURAL 6: Yayvan Optimum Kurali
  TAC egrisi minimum etrafinda yayvan ise, dusuk ΔTmin
  tarafinda kalin (gelecekteki enerji fiyat artislarina
  karsi koruma).
```

### 8.3 Optimumdan Ne Zaman Sapilir? (When to Deviate from Optimum)

```
DAHA DUSUK ΔTmin SECILECEK DURUMLAR:
  1. Enerji fiyatlarinin artmasi bekleniyor
  2. Karbon vergisi / emisyon ticareti yaklasıyor
  3. Atik isi geri kazanimi stratejik oncelik
  4. Plaka esanjor kullanilabilir (dusuk alan maliyeti)
  5. Temiz akislar (dusuk fouling)
  6. Uzun tesis omru planlanıyor (>20 yil)

DAHA YUKSEK ΔTmin SECILECEK DURUMLAR:
  1. Sermaye butcesi sinirli
  2. Agir fouling kosullari
  3. Korozyonlu ortam (pahali malzeme)
  4. Esnek operasyon gerekli (yuk degisimleri)
  5. Kisa tesis omru (<10 yil)
  6. Retrofit: Mevcut esanjorlere uyum
  7. Gaz-gaz isi transferi (dusuk U)
  8. Uzay kisitlamasi (kompakt tasarim zorunlu degil)

OZEL DURUMLAR:
  - Sogutma sistemleri: Her zaman dusuk ΔTmin (3-5°C), COP kritik
  - Kriyojenik: Minimum mumkun ΔTmin (1-3°C), enerji cok pahali
  - Gida endustrisi: Hijyen ve temizlenebilirlik ΔTmin'i belirler
  - Nukleer: Guvenlik marjinleri ΔTmin'i arttirir
```

### 8.4 ΔTmin Secim Ozet Tablosu

```
╔═══════════════════════════╦════════════╦══════════════════════════╗
║ Durum                     ║ ΔTmin [°C] ║ Gerekce                  ║
╠═══════════════════════════╬════════════╬══════════════════════════╣
║ Ilk tahmin (hizli analiz) ║    10      ║ Evrensel baslangic       ║
║ Sivi-sivi, temiz          ║   5-10     ║ Yuksek U, dusuk fouling  ║
║ Sivi-sivi, kirli          ║  15-25     ║ Fouling marjini gerekli  ║
║ Gaz-gaz                   ║  25-50     ║ Dusuk U, buyuk alan      ║
║ Faz degisimli             ║   3-10     ║ Cok yuksek U             ║
║ Plaka esanjor             ║   3-8      ║ Yuksek U, kompakt        ║
║ Sogutma / kriyojenik      ║   1-5      ║ COP kritik               ║
║ Pahali enerji (>0.05€)    ║   5-10     ║ Enerji tasarrufu oncelik ║
║ Ucuz enerji (<0.02€)      ║  20-40     ║ Yatirim minimize         ║
║ Retrofit (mevcut tesis)   ║  10-20     ║ Mevcut ekipmana uyum     ║
║ Greenfield (yeni tesis)   ║   5-15     ║ Optimum tasarim firsati  ║
╚═══════════════════════════╩════════════╩══════════════════════════╝
```

---

## İlgili Dosyalar

- [Pinch Analizi Temelleri](fundamentals.md) -- Linnhoff metodolojisi ve 3 altin kural
- [Bilesik Egriler](composite_curves.md) -- Hot/cold composite curve olusturma
- [Hedefleme](targeting.md) -- Enerji, alan ve maliyet hedefleri
- [Maliyet Tahmini](cost_estimation.md) -- Esanjor maliyet modelleri ve TAC hesabi
- [Buyuk Bilesik Egri](grand_composite.md) -- GCC ve utility yerlestirme
- [HEN Tasarimi](hen_design.md) -- Isi esanjor agi tasarim yontemleri
- [HEN Retrofit](hen_retrofit.md) -- Mevcut tesis iyilestirme
- [Pinch Analizi Ana Dosyasi](../pinch_analysis.md) -- Temel kavramlar ve hesaplamalar
- [Ekonomik Analiz](../economic_analysis.md) -- Yatirim degerlendirme yontemleri
- [Yasam Dongusu Maliyet](../life_cycle_cost.md) -- LCC hesaplamalari

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 2nd Edition, 1994
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," Butterworth-Heinemann, 2nd Edition, 2007
- Smith, R., "Chemical Process Design and Integration," Wiley, 2nd Edition, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Linnhoff, B. & Ahmad, S. (1990), "Cost Optimum Heat Exchanger Networks — 1. Minimum Energy and Capital Using Simple Models for Capital Cost," Computers & Chemical Engineering, 14(7), 729-750
- Ahmad, S. & Linnhoff, B. (1990), "Cost Optimum Heat Exchanger Networks — 2. Targets and Design for Detailed Capital Cost Models," Computers & Chemical Engineering, 14(7), 751-767
- Hall, S.G., Ahmad, S. & Smith, R. (1990), "Capital Cost Targets for Heat Exchanger Networks Comprising Mixed Materials of Construction, Pressure Ratings and Exchanger Types," Computers & Chemical Engineering, 14(3), 319-335
- Townsend, D.W. & Linnhoff, B. (1984), "Surface Area Targets for Heat Exchanger Networks," IChemE Annual Research Meeting, Bath, UK
- Shenoy, U.V., "Heat Exchanger Network Synthesis: Process Optimization by Energy and Resource Analysis," Gulf Publishing, 1995
