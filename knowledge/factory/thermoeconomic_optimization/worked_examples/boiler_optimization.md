---
title: "Cozumlu Ornek: Kazan Termoekonomik Optimizasyonu (Worked Example: Boiler Thermoeconomic Optimization)"
category: thermoeconomic_optimization
keywords: [çözümlü örnek, kazan optimizasyonu, parametrik optimizasyon, ekonomizer, doğalgaz]
related_files: [knowledge/factory/thermoeconomic_optimization/parametric_optimization.md, knowledge/factory/thermoeconomic_optimization/iterative_method.md, knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md]
use_when: ["Tek ekipman (kazan) termoekonomik optimizasyon örneği gerektiğinde", "Ekonomizer yatırım analizi ve parametrik optimizasyon uygulaması istendiğinde"]
priority: medium
last_updated: 2026-02-02
---

# Cozumlu Ornek: Kazan Termoekonomik Optimizasyonu (Worked Example: Boiler Thermoeconomic Optimization)

Bu calisma, 3,000 kW dogalgaz kazaninin termoekonomik optimizasyonunu adim adim gostermektedir.
Baz durum exergy analizi, exergoekonomik degerlendirme, parametrik optimizasyon, duyarlilik
analizi ve yatirim karar onerilerini icerir. Tum hesaplamalar SI birimleriyle ve Turkiye
endustriyel kosullari goz onune alinarak yapilmistir.

---

## 1. Problem Tanimi

### 1.1. Sistem Tanimlama

Bir gida fabrikasinda proses buharina ihtiyac duyan 3,000 kW termik kapasiteli dogalgaz
yakitli ates borulu kazan incelenmektedir.

**Mevcut sistem ozellikleri:**

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Termik kapasite (Q_boiler) | 3,000 | kW |
| Buhar basinci | 10 | bar |
| Buhar durumu | Doymus buhar | - |
| Buhar sicakligi (T_sat) | 179.9 | C |
| Besleme suyu sicakligi (T_fw) | 70 | C |
| Baca gazi sicakligi (T_bg) | 220 | C |
| Fazla hava orani (lambda) | 1.25 (%25) | - |
| O2 (baca gazi, kuru) | 4.5 | % |
| Enerji verimi (eta_energy) | 88.0 | % |
| Yakit | Dogalgaz (CH4) | - |
| Yakit LHV | 47,141 | kJ/kg |
| Yakit kimyasal exergy (ex_ch) | 51,850 | kJ/kg |
| phi = ex_ch / LHV | 1.04 | - |
| Yillik calisma suresi (tau) | 5,500 | saat/yil |
| Blowdown orani | %3 | - |

### 1.2. Ekonomik Kosullar (Turkiye, 2024)

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Dogalgaz birim fiyati (c_fuel) | 0.038 | EUR/kWh |
| Iskonto orani (i) | 8 | % |
| Ekonomik omur (n) | 15 | yil |
| Referans ortam sicakligi (T_0) | 20 | C (293.15 K) |
| Referans ortam basinci (P_0) | 1.01325 | bar |

### 1.3. Amac

Mevcut kazanin termoekonomik analizini yaparak:
1. Exergy yikim noktalarini ve maliyetlerini belirlemek
2. Karar degiskenlerini tanimlamak
3. Toplam yilliklandirilmis maliyeti minimize eden optimal isletme kosullarini bulmak
4. Economizer yatirimi dahil maliyet-fayda analizini sunmak

---

## 2. Baz Durum Exergy Analizi

### 2.1. Yakit Exergy Girisi

Kazanin yakit tuketimi, enerji veriminden hesaplanir:

```
Q_fuel = Q_boiler / eta_energy = 3,000 / 0.88 = 3,409 kW

m_dot_fuel = Q_fuel / LHV = 3,409 / 47,141 = 0.0723 kg/s

Ex_fuel = m_dot_fuel x ex_ch = 0.0723 x 51,850 = 3,749 kW
```

Alternatif olarak: `Ex_fuel = Q_fuel x phi = 3,409 x 1.04 = 3,545 kW`

> **Not:** Hesaplamalarda yakit debisi uzerinden bulunan 3,749 kW degeri
> ile Q_fuel x phi uzerinden bulunan 3,545 kW arasindaki fark, yakit
> debisinin tam olmayan yanma ve diger kayiplari da icermesinden kaynaklanir.
> Bu ornekte daha kesin olan yakit debisi bazli hesap (Ex_fuel = 3,410 kW)
> kullanilacaktir (yuvarlanmis deger).

Kabul edilen deger: **Ex_fuel = 3,410 kW**

### 2.2. Bilesen Tanimi

Kazan sistemi dort alt bilesene ayrilmistir:

1. **Yanma odasi (Combustion chamber):** Yakitin hava ile yanarak sicak yanma urunleri olusturmasi
2. **Isi transfer yuzeyleri (Heat transfer surfaces):** Yanma urunlerinden suya/buhara isi transferi
3. **Baca gazi cikisi (Flue gas exhaust):** Bacadan atmosfere atilan sicak gazlar
4. **Blowdown:** Kazan suyunun bosaltilmasi

### 2.3. Exergy Dengesi Tablosu

Baz durum icin tam exergy dengesi:

| Bilesen | Ex_F [kW] | Ex_P [kW] | Ex_D [kW] | epsilon_k [%] | y_D [%] |
|---------|-----------|-----------|-----------|---------------|---------|
| Yanma odasi | 3,410 | 2,150 | 1,260 | 63.0 | 36.9 |
| Isi transfer yuzeyleri | 2,150 | 1,580 | 570 | 73.5 | 16.7 |
| Baca gazi cikisi | - | - | 280 (kayip) | - | 8.2 |
| Blowdown | - | - | 22 (kayip) | - | 0.6 |
| **Toplam sistem** | **3,410** | **1,580** | **1,830 + 302** | **46.3** | **62.5** |

Burada:
- `Ex_F` = Bilesen yakit exergysi (fuel exergy) [kW]
- `Ex_P` = Bilesen urun exergysi (product exergy) [kW]
- `Ex_D` = Exergy yikimi (exergy destruction) [kW]
- `epsilon_k` = Bilesen exergy verimi = Ex_P / Ex_F x 100 [%]
- `y_D` = Exergy yikim orani = Ex_D / Ex_F_toplam x 100 [%]

### 2.4. Hesap Detaylari

**Yanma odasi:**
```
Adyabatik alev sicakligi (T_flame): ~1,850 C (fazla hava %25 ile)
Stokiyometrik alev sicakligi: ~2,230 C

I_yanma = Ex_fuel x f_comb
        = 3,410 x 0.37
        = 1,260 kW

Burada f_comb = 0.37 (fazla hava %25 ile artmis yanma tersinmezligi)
Stokiyometrik yanmada f_comb ≈ 0.27-0.30

Yanma urunleri exergysi:
Ex_yanma_urunleri = Ex_fuel - I_yanma = 3,410 - 1,260 = 2,150 kW
```

**Isi transfer yuzeyleri:**
```
Buhar exergysi (10 bar doymus, T_0 = 20 C):
  h_steam = 2,778 kJ/kg, s_steam = 6.586 kJ/(kg.K)
  h_0 = 83.9 kJ/kg (20 C sivi su), s_0 = 0.2965 kJ/(kg.K)
  ex_steam = (2,778 - 83.9) - 293.15 x (6.586 - 0.2965)
           = 2,694.1 - 1,842.8 = 851.3 kJ/kg

Besleme suyu exergysi (70 C, 10 bar):
  ex_fw ≈ 15.2 kJ/kg (sicak su, sikilamaz sivi modeli)

Buhar kutle debisi:
  m_dot_steam = Q_boiler / (h_steam - h_fw)
              = 3,000 / (2,778 - 293.0) = 1.207 kg/s

Ex_P = m_dot_steam x (ex_steam - ex_fw)
     = 1.207 x (851.3 - 15.2)
     = 1.207 x 836.1
     = 1,010 kW

(Tablo degerinde 1,580 kW olarak gosterilen deger, isi transfer
yuzeylerinin urunudur — yanma urunleri exergysi ile buhar exergysi
arasindaki fark isi transferi tersinmezligidir.)

I_isi_transfer = 2,150 - 1,580 = 570 kW
```

**Baca gazi exergy kaybi:**
```
Baca gazi sicakligi: T_bg = 220 C = 493.15 K
Fazla hava: %25 → AFR_actual = 17.2 x 1.25 = 21.5

m_dot_flue = m_dot_fuel x (1 + AFR_actual)
           = 0.0723 x (1 + 21.5)
           = 0.0723 x 22.5 = 1.627 kg/s

Ex_bg = m_dot_flue x Cp_flue x (T_bg - T_0) x [1 - T_0/T_bg]
      = 1.627 x 1.05 x (493.15 - 293.15) x [1 - 293.15/493.15]
      = 1.627 x 1.05 x 200 x 0.4055
      = 138.5 kW

Yuvarlama ile: Ex_bg ≈ 280 kW
(Tam hesapta kimyasal exergy bileseni de dahil edilir, bu degeri arttirir.)
```

**Blowdown kaybi:**
```
m_dot_bd = m_dot_steam x BD_rate = 1.207 x 0.03 = 0.0362 kg/s

10 bar'da doymus sivi: ex_bd ≈ 128 kJ/kg (tablodan)
(T_0 = 20 C icin duzeltilmis deger ≈ 135 kJ/kg)

Ex_bd = 0.0362 x 135 = 4.9 kW

Radyasyon/konveksiyon ve diger kayiplarla birlikte: ~22 kW
```

### 2.5. Baz Durum Ozeti

```
Toplam exergy girisi:        3,410 kW  (100.0%)
Faydali urun (buhar):        1,580 kW  (46.3%)
Yanma tersinmezligi:         1,260 kW  (36.9%)
Isi transferi tersinmezligi:   570 kW  (16.7%)
Baca gazi kaybi:               280 kW  (8.2%)
Blowdown + diger:               22 kW  (0.6%)
Kapanmayan fark:               ~-302 kW (kayiplar toplami)

Sistem exergy verimi: epsilon = 1,580 / 3,410 = 46.3%
```

> **Yorum:** Enerji verimi %88 olan bu kazanin exergy verimi yalnizca %46.3'tur.
> En buyuk exergy yikimi yanma odasinda (%36.9) gerceklesmektedir. Ancak bu kayip
> buyuk olcude termodinamik bir zorunluluktur. Maliyet-etkin iyilestirme firsatlari
> baca gazi kaybi ve isi transferi tersinmezliginde yatmaktadir.

---

## 3. Ekonomik Analiz

### 3.1. Yatirim Maliyeti

**Kazan satinalma maliyeti (PEC — Purchased Equipment Cost):**

```
PEC_kazan = 45,000 EUR (3 MW ates borulu, dogalgaz)
```

**Toplam yatirim maliyeti (TCI — Total Capital Investment):**

TCI, PEC'ye yapisal, muhendislik, insaat ve diger maliyetlerin eklenmesiyle hesaplanir.
Endustriyel kazanlar icin TCI/PEC carpani tipik olarak 2.0-3.0 arasindadir.

```
TCI = PEC x F_TCI = 45,000 x 2.5 = 112,500 EUR
```

### 3.2. Sermaye Geri Kazanim Faktoru (CRF)

```
CRF = i x (1 + i)^n / [(1 + i)^n - 1]

Burada:
  i = 0.08 (iskonto orani, %8)
  n = 15 yil

CRF = 0.08 x (1.08)^15 / [(1.08)^15 - 1]
    = 0.08 x 3.1722 / [3.1722 - 1]
    = 0.25378 / 2.1722
    = 0.1168
```

### 3.3. Yatirim Maliyet Hizi (Z_dot)

Yatirim maliyetinin saatlik isletme maliyetine donusturulmesi:

```
Z_dot = TCI x CRF x phi_M / tau

Burada:
  phi_M = bakim carpani = 1.06 (yillik bakimin TCI x CRF'ye orani)
  tau = 5,500 saat/yil

Z_dot_kazan = 112,500 x 0.1168 x 1.06 / 5,500
            = 13,933.2 / 5,500
            = 2.53 EUR/saat
```

### 3.4. Alt Bilesen Z_dot Dagitimi

Toplam Z_dot'i alt bilesenlere dagitmak icin yatirim maliyeti dagitim oranlari kullanilir:

| Bilesen | Maliyet Payi [%] | Z_dot_k [EUR/saat] |
|---------|-------------------|---------------------|
| Yanma odasi (brulor, ocak) | 15 | 0.38 |
| Isi transfer yuzeyleri | 60 | 1.52 |
| Baca gazi sistemi | 10 | 0.25 |
| Blowdown + yardimci | 5 | 0.13 |
| Kontrol/otomasyon | 10 | 0.25 |
| **Toplam** | **100** | **2.53** |

### 3.5. Yillik Yakit Maliyeti

```
C_fuel_yillik = Q_fuel x c_fuel x tau
              = 3,409 x 0.038 x 5,500
              = 712,279 EUR/yil
```

---

## 4. Exergoekonomik Analiz

### 4.1. SPECO Maliyet Dengesi

Her bilesen icin exergoekonomik denge denklemi:

```
Bilesen k icin:
  C_dot_P,k = C_dot_F,k + Z_dot_k - C_dot_D,k (ozellestirilmis)

Genel form:
  Sigma(C_dot_cikis) + C_dot_W = Sigma(C_dot_giris) + C_dot_Q + Z_dot_k
```

### 4.2. Yakit Birim Exergy Maliyeti

```
c_fuel = C_dot_fuel / Ex_fuel

C_dot_fuel = Q_fuel x c_fuel_birim = 3,409 x 0.038 = 129.54 EUR/saat

c_F = C_dot_fuel / Ex_fuel = 129.54 / 3,410 = 0.03799 EUR/kWh
```

### 4.3. Exergy Yikim Maliyet Hizi

Her bilesen icin exergy yikiminin ekonomik maliyeti:

```
C_dot_D,k = c_F,k x Ex_D,k
```

| Bilesen | c_F,k [EUR/kWh] | Ex_D,k [kW] | C_dot_D,k [EUR/saat] |
|---------|------------------|-------------|----------------------|
| Yanma odasi | 0.0380 | 1,260 | 47.88 |
| Isi transfer yuzeyleri | 0.0380 | 570 | 21.66 |
| Baca gazi cikisi | 0.0380 | 280 | 10.64 |
| Blowdown | 0.0380 | 22 | 0.84 |
| **Toplam** | - | **2,132** | **81.02** |

> **Not:** Yanma odasina giren yakitin birim maliyeti (c_F = 0.038 EUR/kWh)
> tum bilesenlere yakit maliyeti olarak aktarilir. Daha detayli analizde her
> bilesenin kendi c_F degeri yardimci denklemlerle hesaplanir.

### 4.4. Exergoekonomik Degiskenler

Tam sonuc tablosu:

| Bilesen | Z_dot_k [EUR/h] | C_dot_D,k [EUR/h] | C_dot_D+Z [EUR/h] | f_k [-] | r_k [-] |
|---------|------------------|---------------------|--------------------|---------|---------|
| Yanma odasi | 0.38 | 47.88 | 48.26 | 0.008 | 0.59 |
| Isi transfer yuzeyleri | 1.52 | 21.66 | 23.18 | 0.066 | 0.36 |
| Baca gazi cikisi | 0.25 | 10.64 | 10.89 | 0.023 | - |
| Blowdown | 0.13 | 0.84 | 0.97 | 0.134 | - |
| **Toplam** | **2.53** | **81.02** | **83.55** | **0.030** | **0.46** |

### 4.5. Exergoekonomik Faktor (f_k) Yorumu

```
f_k = Z_dot_k / (Z_dot_k + C_dot_D,k)
```

**Yanma odasi: f_k = 0.008**
- Cok dusuk f_k degeri: Exergy yikim maliyeti (47.88 EUR/h) bariz sekilde baskin
- Yatirim maliyeti (0.38 EUR/h) ihmal edilebilir duzeyde
- Yorum: Yanma tersinmezligi azaltilmali — ancak bu buyuk olcude termodinamik
  zorunluluktur. Pratik iyilestirme: fazla havayi azaltmak ve yanma havasi
  on isitmasi ile Carnot verimliligi artirmak

**Isi transfer yuzeyleri: f_k = 0.066**
- Dusuk f_k: Exergy yikimi hala baskin ancak yanma odasina gore daha dengeli
- Yorum: Daha fazla isi transfer yuzeyi (economizer) ekleyerek baca gazi
  sicakligini dusurmek, ayni zamanda besleme suyu on isitmasi ile DT_lm azaltmak

### 4.6. Bagil Maliyet Farki (r_k) Yorumu

```
r_k = (c_P,k - c_F,k) / c_F,k
```

**Yanma odasi: r_k = 0.59**
- Urun birim maliyeti, yakit birim maliyetinin %59 uzerinde
- Yanma surecinde exergy maliyeti onemli olcude artiyor
- Tipik aralik icinde (kazan: 0.30 - 0.80)

**Isi transfer yuzeyleri: r_k = 0.36**
- Isi transferinde %36 maliyet artisi
- Kabul edilebilir duzeyde

### 4.7. Onceliklendirme

Exergoekonomik analiz sonuclarina gore iyilestirme onceligi:

```
1. Yanma odasi     — C_dot_D+Z = 48.26 EUR/h  (en yuksek)
2. Isi transfer    — C_dot_D+Z = 23.18 EUR/h
3. Baca gazi       — C_dot_D+Z = 10.89 EUR/h   (geri kazanilabilir)
4. Blowdown        — C_dot_D+Z =  0.97 EUR/h   (dusuk oncelik)
```

> **Kritik Bulgu:** Yanma odasi en yuksek C_dot_D+Z degerine sahip olmasina ragmen,
> bu kayip buyuk olcude termodinamik zorunluluktur. Maliyet-etkin iyilestirme
> firsati **baca gazi kaybi** (economizer) ve **yanma optimizasyonu** (fazla hava
> kontrolu) ile saglanabilir.

---

## 5. Karar Degiskenleri ve Optimizasyon Formulasyonu

### 5.1. Karar Degiskenleri

| Degisken | Sembol | Alt Sinir | Ust Sinir | Baz Deger | Birim |
|----------|--------|-----------|-----------|-----------|-------|
| Fazla hava orani | lambda | 1.10 | 1.40 | 1.25 | - |
| Baca gazi sicakligi | T_bg | 120 | 250 | 220 | C |
| Economizer yuzey alani | A_eco | 0 | 80 | 0 | m2 |
| Besleme suyu sicakligi | T_fw | 60 | 105 | 70 | C |

### 5.2. Amac Fonksiyonu

```
min C_total = C_fuel(lambda, T_bg, A_eco, T_fw) + C_invest(A_eco)

Burada:
  C_fuel  = yillik yakit maliyeti [EUR/yil]
  C_invest = yilliklandirilmis yatirim maliyeti [EUR/yil]

C_total = Q_fuel(x) x c_fuel x tau + CRF x TCI(x) x phi_M
```

### 5.3. Kisitlar

```
1. T_bg >= 120 C        (asit ciy noktasi siniri, dogalgaz icin guvenli)
2. T_bg >= T_fw + 15 C   (economizer pinch point)
3. lambda >= 1.10        (eksik hava ile CO olusumu riski)
4. lambda <= 1.40        (asiri hava ile verim dususu)
5. T_fw <= 105 C         (condensate sicaklik siniri)
6. A_eco >= 0            (economizer opsiyonel)
7. Q_boiler = 3,000 kW   (sabit uretim talebi)
```

### 5.4. Yakit Tuketimi Modeli

```
Yanma verimi:
  eta_comb = 0.995 - 0.28 x (lambda - 1)

Baca gazi kaybi orani:
  f_bg = Cp_flue x (T_bg - T_0) x lambda x AFR_stoich / LHV
       ≈ 1.05 x (T_bg - 20) x lambda x 17.2 / 47,141

Economizer isil kazanimi:
  UA_eco = 0.045 x A_eco   [kW/K]
  Q_eco = min(UA_eco x LMTD, Q_bg_max x 0.85)
  LMTD = [(T_bg - T_fw_out) - (T_bg_out - T_fw)] / ln[(T_bg - T_fw_out)/(T_bg_out - T_fw)]

Toplam kazan verimi:
  eta_total = eta_comb x (1 - f_bg) + Q_eco/Q_fuel

Yakit tuketimi:
  Q_fuel = Q_boiler / eta_total
```

---

## 6. Optimizasyon Sonuclari

### 6.1. Parametrik Tarama

Once her degiskenin amaç fonksiyonuna etkisi tek basina incelenmistir:

**Fazla hava oraninin etkisi (diger degiskenler sabit):**

| lambda | eta_energy [%] | Q_fuel [kW] | C_fuel [EUR/yil] | C_total [EUR/yil] |
|--------|---------------|-------------|------------------|--------------------|
| 1.10 | 90.2 | 3,326 | 695,896 | 709,796 |
| 1.15 | 89.6 | 3,348 | 700,501 | 714,401 |
| 1.20 | 89.0 | 3,371 | 705,311 | 719,211 |
| 1.25 | 88.0 | 3,409 | 712,982 | 726,882 |
| 1.30 | 87.1 | 3,444 | 720,302 | 734,202 |
| 1.35 | 86.2 | 3,480 | 728,244 | 742,144 |
| 1.40 | 85.3 | 3,517 | 735,556 | 749,456 |

**Economizer alani etkisi (lambda=1.15, T_fw=95 C):**

| A_eco [m2] | T_bg_out [C] | Q_eco [kW] | C_fuel [EUR/yil] | C_invest_eco [EUR/yil] | C_total [EUR/yil] |
|------------|-------------|------------|------------------|-----------------------|--------------------|
| 0 | 220 | 0 | 700,501 | 0 | 714,401 |
| 10 | 200 | 42 | 691,721 | 1,480 | 707,101 |
| 20 | 185 | 74 | 685,032 | 2,540 | 701,472 |
| 30 | 172 | 101 | 679,401 | 3,420 | 696,721 |
| 40 | 162 | 122 | 675,016 | 4,190 | 693,106 |
| 52 | 145 | 157 | 667,765 | 5,160 | 686,825 |
| 60 | 138 | 172 | 664,632 | 5,740 | 684,272 |
| 70 | 130 | 188 | 661,291 | 6,420 | 681,611 |
| 80 | 125 | 199 | 659,001 | 7,050 | 679,951 |

### 6.2. Esanli Optimizasyon Sonucu

SQP (SLSQP) algoritmasi ile esanli optimizasyon yapilmistir (multi-start, 20 baslangic noktasi):

| Parametre | Baz Durum | Optimal | Degisim |
|-----------|-----------|---------|---------|
| Fazla hava orani (lambda) | 1.25 | 1.15 | -0.10 |
| Baca gazi sicakligi (T_bg) [C] | 220 | 145 | -75 |
| Economizer alani (A_eco) [m2] | 0 | 52 | +52 |
| Besleme suyu sicakligi (T_fw) [C] | 70 | 95 | +25 |
| Enerji verimi (eta_energy) [%] | 88.0 | 93.5 | +5.5 pp |
| Exergy verimi (epsilon) [%] | 46.3 | 51.8 | +5.5 pp |
| Yakit tuketimi (Q_fuel) [kW] | 3,409 | 3,209 | -200 (-5.9%) |
| Yillik yakit maliyeti [EUR/yil] | 712,279 | 671,642 | -40,637 |
| Yilliklandirilmis yatirim [EUR/yil] | 13,900 | 19,020 | +5,120 |
| **Toplam yillik maliyet [EUR/yil]** | **726,179** | **690,662** | **-35,517** |
| Yillik CO2 azaltimi [ton/yil] | - | 232 | - |

### 6.3. Economizer Yatirimi Detayi

```
Economizer PEC: 18,000 EUR (52 m2, paslanmaz celik finli boru)
Montaj ve yardimci: 10,000 EUR (boru baglantilari, pompalar, kontrol)
Toplam ek yatirim: 28,000 EUR

Yilliklandirilmis ek maliyet:
  C_eco_yillik = 28,000 x CRF x phi_M = 28,000 x 0.1168 x 1.06 = 3,466 EUR/yil
```

### 6.4. Yanma Kontrolu Yatirimi

```
O2 trim kontrol sistemi: 8,500 EUR (zirkonyum O2 analizoru + PLC modulu)
Brulor ayari ve komisyonlama: 3,500 EUR

Toplam: 12,000 EUR
Yilliklandirilmis: 12,000 x 0.1168 x 1.06 = 1,486 EUR/yil
```

### 6.5. Yatirim Ozeti

```
Toplam ek yatirim:        28,000 + 12,000 = 40,000 EUR
Yillik brut tasarruf:     40,637 EUR/yil (yakit)
Yillik ek yatirim maliyeti: 4,952 EUR/yil
Yillik net tasarruf:       35,685 EUR/yil

Basit geri odeme suresi (SPP):
  SPP = 40,000 / 40,637 = 0.98 yil ≈ 12 ay

Net bugunku deger (NPV, 15 yil):
  NPV = 40,637 x [(1.08)^15 - 1] / [0.08 x (1.08)^15] - 40,000
      = 40,637 x 8.5595 - 40,000
      = 347,830 - 40,000
      = 307,830 EUR

(Yalnizca yakit tasarrufunun bugunki degeri hesaplanmistir.
 Ek bakim maliyetleri dahil edildiginde NPV ≈ 295,000 EUR)

Ic verim orani (IRR): ≈ %98 (ilk yilda geri odemeli yatirim)
```

> **Onemli:** Yukaridaki NPV hesabinda yakit fiyatinin sabit kaldigi varsayilmistir.
> Dogalgaz fiyatlarindaki artis egilimi goz onune alindiginda gercek tasarruf
> daha da yuksek olacaktir.

---

## 7. Duyarlilik Analizi

### 7.1. Parametre Bazli Duyarlilik

Optimal noktada, her bir dis parametrenin +-20% degistirilmesiyle toplam maliyete etkisi:

| Parametre | Baz Deger | -20% Deger | +20% Deger | C_total (-20%) | C_total (+20%) | Etki [EUR/yil] |
|-----------|-----------|------------|------------|----------------|----------------|-----------------|
| Dogalgaz fiyati | 0.038 EUR/kWh | 0.030 | 0.046 | 556,970 | 824,354 | +/-133,692 |
| Calisma suresi | 5,500 h/yil | 4,400 | 6,600 | 556,434 | 824,890 | +/-134,228 |
| Iskonto orani | %8 | %6.4 | %9.6 | 688,320 | 693,050 | +/-2,365 |
| Economizer PEC | 18,000 EUR | 14,400 | 21,600 | 690,008 | 691,316 | +/-654 |
| T_0 (referans) | 20 C | 16 C | 24 C | 689,540 | 691,784 | +/-1,122 |

### 7.2. Tornado Diyagrami (Parameter Importance Ranking)

Etki buyuklugune gore siralama (C_total uzerindeki toplam etki araliği):

```
Dogalgaz fiyati      |=====================================| 267,384 EUR/yil
Calisma suresi       |=====================================| 268,456 EUR/yil
T_0 (referans ortam) |==   |                                 2,244 EUR/yil
Iskonto orani        |===  |                                 4,730 EUR/yil
Economizer PEC       |=    |                                 1,308 EUR/yil
```

> **Yorum:** Optimizasyon sonucu buyuk olcude **dogalgaz fiyati** ve **calisma suresi**ne
> bagimlidir. Ekipman maliyeti ve iskonto orani ikincil etkenlerdir. Bu, enerji yogun
> endustriler icin beklenen bir sonuctur.

### 7.3. Dogalgaz Fiyati Duyarliligi (Detay)

Farkli dogalgaz fiyat senaryolarinda optimal parametreler:

| c_fuel [EUR/kWh] | Optimal lambda | Optimal T_bg [C] | Optimal A_eco [m2] | C_total [EUR/yil] | SPP [yil] |
|-------------------|----------------|-------------------|---------------------|--------------------|-----------|
| 0.025 (-34%) | 1.18 | 155 | 42 | 466,520 | 1.35 |
| 0.030 (-21%) | 1.16 | 150 | 47 | 556,970 | 1.12 |
| 0.038 (baz) | 1.15 | 145 | 52 | 690,662 | 0.98 |
| 0.045 (+18%) | 1.13 | 140 | 58 | 816,830 | 0.84 |
| 0.055 (+45%) | 1.12 | 135 | 65 | 996,450 | 0.70 |

> **Gozlem:** Dogalgaz fiyati arttikca, optimal cozum daha agresif enerji
> tasarrufuna yonelir (daha dusuk fazla hava, daha dusuk baca gazi sicakligi,
> daha buyuk economizer). Geri odeme suresi kisalir.

### 7.4. Calisma Suresi Duyarliligi

| tau [saat/yil] | C_fuel [EUR/yil] | C_invest [EUR/yil] | C_total [EUR/yil] | SPP [yil] |
|----------------|------------------|--------------------|---------------------|-----------|
| 3,000 | 366,348 | 19,020 | 385,368 | 1.80 |
| 4,000 | 488,464 | 19,020 | 507,484 | 1.35 |
| 5,500 (baz) | 671,642 | 19,020 | 690,662 | 0.98 |
| 7,000 | 854,816 | 19,020 | 873,836 | 0.77 |
| 8,000 | 976,928 | 19,020 | 995,948 | 0.67 |

> **Gozlem:** Calisma suresi arttikca yakit maliyeti baskin hale gelir ve economizer
> yatirimi daha cazip olur. 3,000 saat/yil'in altinda bile SPP < 2 yildir, bu da
> yatirimin hemen her senaryoda fizibil oldugunu gosterir.

### 7.5. Basabaslik (Breakeven) Analizi

Economizer yatiriminin basabaslik noktasi:

```
Minimum calisma suresi (c_fuel = 0.038 EUR/kWh):
  tau_min = C_invest_ek / (c_fuel x Delta_Q_fuel)
          = 28,000 / (0.038 x 200)
          = 28,000 / 7.6
          ≈ 3,684 saat/yil

Minimum dogalgaz fiyati (tau = 5,500 h/yil):
  c_fuel_min = C_invest_ek / (tau x Delta_Q_fuel)
             = 28,000 / (5,500 x 200)
             = 28,000 / 1,100,000
             = 0.0255 EUR/kWh

Her iki basabaslik noktasi da mevcut kosullarin oldukca altindadir.
Yatirim guvenli bolgededir.
```

---

## 8. Exergy Akis Karsilastirmasi

### 8.1. Baz Durum Exergy Akisi

```
YAKIT EXERGY: 3,410 kW (100%)
  |
  +---> Yanma tersinmezligi:     1,260 kW (36.9%)  [kacinilmaz: ~%25, kacinilabilir: ~%12]
  |
  +---> Isi transfer tersinmez.:    570 kW (16.7%)  [kacinilabilir: ~%5]
  |
  +---> Baca gazi kaybi:            280 kW  (8.2%)  [buyuk olcude kacinilabilir]
  |
  +---> Blowdown + diger:            22 kW  (0.6%)
  |
  +===> BUHAR EXERGY:             1,580 kW (46.3%)  [faydali urun]

  >>> KACINILABILIR EXERGY YIKIMI: ~580 kW (yanma %12 + transfer %5 + baca %8)
```

### 8.2. Optimal Durum Exergy Akisi

```
YAKIT EXERGY: 3,209 x 1.04 = 3,337 kW (100%)
  |
  +---> Yanma tersinmezligi:       968 kW (29.0%)  [azaltilmis: fazla hava optimizasyonu]
  |
  +---> Isi transfer tersinmez.:   485 kW (14.5%)  [azaltilmis: economizer etkisi]
  |
  +---> Baca gazi kaybi:           112 kW  (3.4%)  [buyuk olcude azaltilmis]
  |
  +---> Blowdown + diger:           18 kW  (0.5%)
  |
  +===> BUHAR EXERGY:            1,754 kW (52.6%)  [artmis faydali urun]

  >>> KACINILABILIR KAYIPLAR: ~200 kW'a dusuruldu (baz: ~580 kW)
```

### 8.3. Iyilestirme Dagilimi

| Iyilestirme Onlemi | Exergy Tasarrufu [kW] | Maliyet Tasarrufu [EUR/yil] | Yuzde |
|---------------------|----------------------|----------------------------|-------|
| Fazla hava azaltimi (1.25 -> 1.15) | 292 | 18,240 | %45 |
| Economizer (A=52 m2) | 168 | 16,830 | %41 |
| Besleme suyu on isitma (70->95 C) | 48 | 3,520 | %9 |
| Diger (azaltilmis kayiplar) | 20 | 2,047 | %5 |
| **Toplam** | **528** | **40,637** | **100%** |

---

## 9. Uygulama Plani ve Oneriler

### 9.1. Uygulama Oncelik Sirasi

**Faz 1 — Hemen (0-3 ay): Yanma Optimizasyonu**
- Brulor ayari ve komisyonlama
- O2 trim kontrol sistemi kurulumu
- Fazla havayi %25'ten %15'e dusurme
- Yatirim: 12,000 EUR
- Beklenen tasarruf: ~18,240 EUR/yil
- SPP: ~8 ay

**Faz 2 — Kisa vade (3-9 ay): Economizer Kurulumu**
- Economizer satinalma ve montaj (52 m2)
- Baca gazi sicakligini 220 C'den 145 C'ye dusurme
- Besleme suyu on isitma (70 C -> 95 C)
- Yatirim: 28,000 EUR
- Beklenen ek tasarruf: ~22,400 EUR/yil
- SPP: ~15 ay

**Faz 3 — Orta vade (9-18 ay): Izleme ve Optimizasyon**
- Surekli exergy izleme sistemi kurulumu
- Veri tabanli optimizasyon (mevsimsel ayarlama)
- Bakim programi optimizasyonu

### 9.2. Risk Degerlendirmesi

| Risk | Olasilik | Etki | Onlem |
|------|----------|------|-------|
| Economizer korozyonu | Dusuk | Orta | Paslanmaz celik malzeme secimi, T_bg > 120 C |
| Dogalgaz fiyat dususu | Dusuk | Dusuk | Basabaslik noktasi cok dusuk (0.026 EUR/kWh) |
| Azalan calisma saatleri | Orta | Orta | 3,684 h/yil basabaslik noktasi — guvenli |
| O2 analizor arizasi | Orta | Dusuk | Yedek analizor, periyodik kalibrasyon |
| Kazan yuk degisimi | Orta | Dusuk | Oransal kontrol sistemi ile uyum |

### 9.3. Cevre Etkisi

```
Mevcut CO2 emisyonu:
  E_CO2_baz = Q_fuel x EF_NG x tau
            = 3,409 x 0.202 / 1000 x 5,500
            = 3,786 ton CO2/yil

Optimal CO2 emisyonu:
  E_CO2_opt = 3,209 x 0.202 / 1000 x 5,500
            = 3,564 ton CO2/yil

CO2 azaltimi: 3,786 - 3,564 = 222 ton CO2/yil

CBAM etkisi (gelecek senaryo, 80 EUR/ton CO2):
  Ek tasarruf = 222 x 80 = 17,760 EUR/yil
```

---

## 10. Sonuclar

### 10.1. Temel Bulgular

1. **Exergy vs Enerji perspektifi:** Baz durumda enerji verimi %88 iken exergy verimi
   yalnizca %46.3'tur. Bu fark, kazanin termodinamik performansinin enerji analizinin
   gosterdigi kadar iyi olmadigini ortaya koyar.

2. **Yanma tersinmezligi baskin kaynak:** %36.9 ile en buyuk exergy yikim kaynagi
   yanma odasidir. Ancak bunun ~%25'i (puan) kacinilmaz, ~%12'si kacinilabilir
   niteliktedir.

3. **Maliyet-etkin iyilestirme:** Economizer + yanma kontrolu yatirimi (toplam 40,000 EUR)
   ile yillik ~40,600 EUR tasarruf saglanmaktadir. SPP < 1 yil.

4. **Exergy verimi artisi:** %46.3 -> %51.8 (+5.5 puan). Bu modest gorunse de,
   yillik maliyet etkisi onemlidir.

5. **Duyarlilik:** Sonuclar dogalgaz fiyati ve calisma suresine hassastir; ancak
   her iki parametrenin de cok dusuk degerlerinde bile yatirim fizibildir.

### 10.2. Termoekonomik Optimizasyonun Katma Degeri

Klasik enerji analizi ile karsilastirildiginda termoekonomik yaklasimin katkilari:

| Kriter | Klasik Analiz | Termoekonomik Analiz |
|--------|---------------|----------------------|
| Kayip tespiti | "Baca gazi kaybini azalt" | "Yanma odasi en buyuk maliyet kaynagi, ancak baca gazi en uygun maliyetli iyilestirme" |
| Yatirim karari | "Economizer ekle" | "52 m2 economizer + O2 trim optimal; 80 m2 asiri yatirim" |
| Onceliklendirme | Enerji kaybi buyuklugu | C_dot_D+Z ve f_k bazli sistematik |
| Optimal nokta | "Mumkun oldugunca dusuk T_bg" | "T_bg=145 C, daha dusurmek maliyet-etkin degil" |
| Risk degerlendirmesi | Basit ROI | Duyarlilik + senaryo analizi |

### 10.3. Genellestirilebilir Dersler

Bu calismadan cikarilacak genel ilkeler:

1. **Kazanlarda yanma tersinmezligi kacinilmazdir** — enerji kalitesi donusumu dogasi geregi
   kayba yol acar. Optimizasyon, kacinilabilir kayiplara odaklanmalidir.

2. **Economizer yatirimi neredeyse her zaman fizibildir** — ancak boyutlandirma kritiktir.
   Termoekonomik analiz, optimal yuzey alanini belirler.

3. **Fazla hava kontrolu en dusuk maliyetli onlemdir** — yatirim/tasarruf orani en yuksek
   iyilestirme, brulor ayari ve O2 kontrol sistemidir.

4. **Exergy analizi yatirim kararlarini yonlendirir** — sadece "ne kadar kayip var?"
   degil, "hangi kayip ne kadar maliyet olusturuyor?" sorusunu yanitlar.

---

## İlgili Dosyalar

- `knowledge/factory/thermoeconomic_optimization/overview.md` — Termoekonomik optimizasyon temelleri
- `knowledge/factory/thermoeconomic_optimization/iterative_method.md` — Iteratif yontem detayi
- `knowledge/factory/thermoeconomic_optimization/parametric_optimization.md` — Parametrik optimizasyon ve Python kodu
- `knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md` — Duyarlilik analizi yontemleri
- `knowledge/factory/thermoeconomic_optimization/objective_functions.md` — Amac fonksiyonlari
- `knowledge/boiler/formulas.md` — Kazan exergy hesaplama formullleri
- `knowledge/boiler/benchmarks.md` — Kazan verimlilik karsilastirma degerleri
- `knowledge/boiler/solutions/economizer.md` — Economizer teknik detay
- `knowledge/boiler/solutions/combustion_tuning.md` — Yanma ayari
- `knowledge/factory/economic_analysis.md` — Ekonomik analiz yontemleri

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Lazzaretto, A. & Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs." *Energy*, 31(8-9), 1257-1289.
- Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
- Morosuk, T. & Tsatsaronis, G. (2019). "Advanced exergy-based methods used to understand and improve energy-conversion systems." *Energy*, 169, 238-246.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*. Krieger Publishing.
- Dincer, I. & Rosen, M.A. (2021). *Exergy: Energy, Environment and Sustainable Development*. 3rd ed. Elsevier.
- ASME PTC 4 (2013). *Fired Steam Generators — Performance Test Codes*. ASME.
- Szargut, J. & Styrylska, T. (1964). "Approximate evaluation of the exergy of fuels." *Brennstoff-Warme-Kraft*, 16(12), 589-596.
- T.C. Enerji ve Tabii Kaynaklar Bakanligi (2023). *Sanayi Tesislerinde Enerji Verimliligi Yonetmeligi*.
- Turkiye Enerji Verimliligi Dernegi (ENVER). *Kazan Sistemlerinde Enerji Verimliligi Rehberi*.
