---
title: "Maliyet Tahmini ve Ekonomik Analiz (Cost Estimation and Economic Analysis)"
category: factory
equipment_type: factory
keywords: [maliyet tahmini, TAC, NPV, IRR, eşanjör maliyet, Bath formülü, ekonomik analiz]
related_files: [factory/pinch/targeting.md, factory/pinch/delta_t_min.md, factory/pinch/hen_design.md, factory/pinch/hen_retrofit.md]
use_when: ["Pinch projesi maliyet analizi yapılırken", "TAC hesaplanırken", "Yatırım değerlendirmesi yapılırken"]
priority: medium
last_updated: 2026-02-01
---

> **Not:** Bu dosyadaki maliyet formülleri orijinal akademik kaynaklarda USD bazlıdır. Türkiye endüstriyel uygulamaları için güncel EUR/USD döviz kuru ile çevirin (2024 referans: 1 USD ≈ 0,92 EUR).

# Maliyet Tahmini ve Ekonomik Analiz (Cost Estimation and Economic Analysis)

Pinch analizinde enerji tasarruf hedefleri belirlendikten sonra en kritik adim, bu hedeflere ulasmanin
ekonomik maliyetini tahmin etmektir. Toplam Yillik Maliyet (TAC — Total Annual Cost) minimizasyonu,
optimal Delta T_min degeri secimi ve yatirim kararlarinin temelini olusturur.

Bu dosya, referans problem uzerinden tam bir maliyet tahmini ve ekonomik analiz sureci sunar.

## Referans Problem

| Akim | T_giris (°C) | T_cikis (°C) | CP (kW/°C) | Q (kW)  |
|------|---------------|---------------|-------------|---------|
| H1   | 270           | 80            | 15          | 2850    |
| H2   | 180           | 40            | 25          | 3500    |
| H3   | 150           | 60            | 10          | 900     |
| C1   | 30            | 250           | 18          | 3960    |
| C2   | 60            | 200           | 12          | 1680    |

- Delta T_min = 10°C
- QH,min = 1800 kW (minimum sicak utility ihtiyaci)
- QC,min = 2240 kW (minimum soguk utility ihtiyaci)

---

## 1. Esanjor Maliyet Modelleri (Heat Exchanger Cost Models)

Isi esanjorlerinin kurulu maliyeti (installed cost) genellikle us fonksiyonu (power law) ile ifade edilir:

```
C_esanjor = a + b × A^c
```

Burada:
- C_esanjor : Kurulu maliyet (USD veya EUR)
- A : Isi transfer alani (m²)
- a : Sabit maliyet bileseni (kurulum, borulama, temel isler)
- b : Alan bagimliligi katsayisi
- c : Olcekleme ussu (scaling exponent), tipik olarak 0.6–1.0 araliginda

### 1.1 Tip ve Malzemeye Gore Katsayilar

| Esanjor Tipi                | Malzeme           | a (USD) | b (USD/m^c) | c    | Gecerli Aralik (m²) |
|-----------------------------|-------------------|---------|-------------|------|----------------------|
| Boru-kabuk (Shell-and-Tube) | Karbon celigi      | 8000    | 750         | 0.81 | 10–1000              |
| Boru-kabuk (Shell-and-Tube) | Paslanmaz celik    | 12000   | 1050        | 0.81 | 10–1000              |
| Plakali (Plate)             | Paslanmaz celik    | 3000    | 600         | 0.85 | 1–500                |
| Plakali (Plate)             | Titanyum           | 5000    | 1100        | 0.85 | 1–500                |
| Hava sogutmali (Air-Cooled) | Karbon celigi      | 15000   | 400         | 0.90 | 50–5000              |
| Hava sogutmali (Air-Cooled) | Paslanmaz celik    | 20000   | 550         | 0.90 | 50–5000              |
| Cift borulu (Double-Pipe)   | Karbon celigi      | 2000    | 500         | 0.75 | 1–50                 |
| Spiral (Spiral)             | Paslanmaz celik    | 10000   | 800         | 0.83 | 5–300                |

### 1.2 Maliyet Guncelleme (Cost Update)

Farkli yillardaki maliyet verilerini guncellemek icin CEPCI (Chemical Engineering Plant Cost Index) kullanilir:

```
C_guncel = C_referans × (CEPCI_guncel / CEPCI_referans)
```

Ornek CEPCI degerleri:
- 2007: 525.4
- 2013: 567.3
- 2020: 596.2
- 2024: 680.0 (tahmini)

### 1.3 Kurulum Carpani (Installation Factor)

Eger maliyet modeli sadece ekipman maliyeti veriyorsa, kurulu maliyete donusum:

```
C_kurulu = f_kurulum × C_ekipman
```

Tipik f_kurulum degerleri:
- Boru-kabuk esanjor: 3.0–3.5
- Plakali esanjor: 1.5–2.0
- Hava sogutmali: 2.0–2.5

---

## 2. Alan Hesabi (Area Calculation)

### 2.1 Temel Denklem

Bir esanjordeki isi transfer alani:

```
Q = U × A × Delta_T_LM × F_t
```

Cozum:

```
A = Q / (U × Delta_T_LM × F_t)
```

Burada:
- Q : Isi yukü (kW)
- U : Toplam isi transfer katsayisi (kW/m²·°C)
- Delta_T_LM : Logaritmik ortalama sicaklik farki — LMTD (°C)
- F_t : LMTD duzeltme faktoru (correction factor), genellikle 0.8–1.0

### 2.2 LMTD Hesabi

Karsi-akim (counter-current) esanjor icin:

```
Delta_T_LM = (Delta_T_1 - Delta_T_2) / ln(Delta_T_1 / Delta_T_2)
```

Burada:
- Delta_T_1 = T_h,giris - T_c,cikis
- Delta_T_2 = T_h,cikis - T_c,giris

Eger Delta_T_1 = Delta_T_2 ise:

```
Delta_T_LM = Delta_T_1 = Delta_T_2
```

### 2.3 F_t Duzeltme Faktoru

Cok gecisli (multi-pass) boru-kabuk esanjorler icin F_t < 1.0 olur. Hesap icin R ve P parametreleri:

```
R = (T_h,giris - T_h,cikis) / (T_c,cikis - T_c,giris)
P = (T_c,cikis - T_c,giris) / (T_h,giris - T_c,giris)
```

Kural: F_t < 0.75 ise tasarim uygun degildir, esanjor konfigurasyonu degistirilmelidir.

### 2.4 Film Katsayilari Tablosu (Film Coefficients)

| Akiskan / Durum                         | h (kW/m²·°C) |
|-----------------------------------------|---------------|
| Su (forced convection)                  | 1.0–3.0       |
| Organik sivi (forced convection)        | 0.3–1.0       |
| Gaz (1 atm, forced convection)          | 0.02–0.10     |
| Gaz (yuksek basinc, forced convection)  | 0.10–0.50     |
| Yogusan buhar (condensing steam)        | 5.0–15.0      |
| Kaynar su (boiling water)               | 2.0–10.0      |
| Termal yag (thermal oil)                | 0.3–0.8       |
| Hava (dogal konveksiyon)                | 0.005–0.025   |

### 2.5 Toplam Isi Transfer Katsayisi (Overall Heat Transfer Coefficient)

```
1/U = 1/h_h + R_f,h + d_w/k_w + R_f,c + 1/h_c
```

Burada:
- h_h, h_c : Sicak ve soguk taraf film katsayilari
- R_f,h, R_f,c : Kirlenme direnci (fouling resistance), tipik 0.0001–0.0005 m²·°C/kW
- d_w : Boru duvar kalinligi (m)
- k_w : Duvar termal iletkenlik (kW/m·°C)

Tipik U degerleri (hizli tahmin icin):

| Eslesme                        | U (kW/m²·°C) |
|--------------------------------|---------------|
| Su — Su                       | 0.8–1.5       |
| Su — Organik sivi             | 0.3–0.8       |
| Organik sivi — Organik sivi   | 0.1–0.4       |
| Gaz — Gaz                     | 0.01–0.05     |
| Gaz — Sivi                    | 0.02–0.10     |
| Yogusan buhar — Su            | 1.5–4.0       |
| Yogusan buhar — Organik sivi  | 0.5–1.5       |

---

## 3. Bath Formulu Detay (Bath Formula Detail)

### 3.1 Alan Hedefleme (Area Targeting)

Bath formulu (Townsend ve Linnhoff, 1984), minimum alan hedefini esanjor agi tasarimi yapmadan
hesaplamayi mumkun kilar. Formul, Bilesik Egrilerin (Composite Curves) her enthalpy araligindaki
alan gereksinimini toplar.

### 3.2 Formul

```
A_min = Sigma_k [ (1/Delta_T_LM,k) × Sigma_i (q_i,k / h_i) ]
```

Burada:
- k : Enthalpy araligi (interval) indeksi
- Delta_T_LM,k : k. araliktaki LMTD
- q_i,k : i. akimin k. araliktaki isi yukü
- h_i : i. akimin film katsayisi

### 3.3 Varsayimlar

1. Tam karsi-akim (pure counter-current) eslesme varsayilir
2. Her araliktaki sicaklik profili dogrusal kabul edilir
3. Film katsayilari sabit (sicakliga bagimsiz) alinir
4. Kirlenme direnci ihmal edilir veya h degerlerine dahil edilir
5. F_t = 1.0 varsayilir (ideal karsi-akim)

### 3.4 Sayisal Ornek

Referans problem icin basitlestirilmis iki aralikli gosterim:

**Aralik 1:** Sicak Bilesik 270–180°C, Soguk Bilesik 200–250°C
- Delta_T_1 = 270 - 250 = 20°C
- Delta_T_2 = 180 - 200 = (-) → Bu aralikta pinch noktasinin ustunde duzenleme yapilir
- Ortalama Delta_T ~ 15°C (duzeltilmis)
- Toplam Q_aralik1 ~ 1800 kW
- U_eff ~ 0.5 kW/m²·°C
- A_1 = 1800 / (0.5 × 15) = 240 m²

**Aralik 2:** Sicak Bilesik 180–80°C, Soguk Bilesik 30–170°C
- Delta_T_LM ~ 30°C (hesaplanmis)
- Toplam Q_aralik2 ~ 4250 kW
- U_eff ~ 0.5 kW/m²·°C
- A_2 = 4250 / (0.5 × 30) = 283 m²

**Toplam minimum alan:** A_min = 240 + 283 = 523 m²

Not: Gercek Bath formulu tum araliklari kapsar; burada kavramsal gosterim yapilmistir.

---

## 4. Toplam Yillik Maliyet — TAC (Total Annual Cost)

### 4.1 TAC Tanimi

```
TAC = C_yatirim_yillik + C_enerji_yillik
```

Burada:
- C_yatirim_yillik : Yillik sermaye maliyeti (annualized capital cost)
- C_enerji_yillik : Yillik enerji (utility) maliyeti

### 4.2 Yillik Sermaye Maliyeti

```
C_yatirim_yillik = CRF × C_yatirim_toplam
```

Burada CRF (Capital Recovery Factor — Sermaye Geri Kazanim Faktoru):

```
CRF = [i × (1 + i)^n] / [(1 + i)^n - 1]
```

- i : Iskonto orani (discount rate), tipik %8–15
- n : Tesis omru (plant lifetime), tipik 10–25 yil

### 4.3 CRF Degerleri Tablosu

| Iskonto Orani (i) | n = 10 yil | n = 15 yil | n = 20 yil | n = 25 yil |
|--------------------|-----------|-----------|-----------|-----------|
| %5                 | 0.1295    | 0.0963    | 0.0802    | 0.0710    |
| %8                 | 0.1490    | 0.1168    | 0.1019    | 0.0937    |
| %10                | 0.1627    | 0.1315    | 0.1175    | 0.1102    |
| %12                | 0.1770    | 0.1468    | 0.1339    | 0.1275    |
| %15                | 0.1993    | 0.1710    | 0.1598    | 0.1547    |

### 4.4 Yillik Enerji Maliyeti

```
C_enerji_yillik = (QH,min × C_isitma + QC,min × C_sogutma) × t_isletme
```

- QH,min : Minimum sicak utility (kW)
- QC,min : Minimum soguk utility (kW)
- C_isitma : Isitma birim maliyeti (USD/kWh veya USD/kW·yil)
- C_sogutma : Sogutma birim maliyeti (USD/kWh veya USD/kW·yil)
- t_isletme : Yillik isletme suresi (saat/yil), tipik 8000 saat/yil

### 4.5 TAC ve Delta T_min Iliskisi

Delta T_min arttikca:
- **Enerji maliyeti artar** (daha fazla utility gerekir)
- **Sermaye maliyeti azalir** (daha kucuk alan, daha az esanjor)

Delta T_min azaldikca:
- **Enerji maliyeti azalir** (daha fazla isi geri kazanimi)
- **Sermaye maliyeti artar** (daha buyuk alan, daha fazla esanjor)

**Optimal Delta T_min**, TAC'nin minimum oldugu noktadir.

| Delta T_min (°C) | A_toplam (m²) | C_yatirim_yillik (USD/yil) | C_enerji_yillik (USD/yil) | TAC (USD/yil) |
|-------------------|---------------|---------------------------|--------------------------|---------------|
| 5                 | 1046          | 185,000                   | 280,000                  | 465,000       |
| 10                | 523           | 112,000                   | 323,000                  | 435,000       |
| 15                | 349           | 84,000                    | 370,000                  | 454,000       |
| 20                | 262           | 69,000                    | 420,000                  | 489,000       |
| 25                | 209           | 60,000                    | 475,000                  | 535,000       |
| 30                | 174           | 53,000                    | 534,000                  | 587,000       |

Bu tabloya gore, referans problem icin **optimal Delta T_min ~ 10°C** civarindadir (TAC = 435,000 USD/yil).

---

## 5. Yatirim Degerlendirme Yontemleri (Investment Evaluation Methods)

### 5.1 Basit Geri Odeme Suresi — SPP (Simple Payback Period)

```
SPP = C_yatirim / S_yillik
```

- C_yatirim : Toplam yatirim maliyeti (USD)
- S_yillik : Yillik tasarruf (USD/yil)

**Ornek:**
- Mevcut enerji maliyeti: 800,000 USD/yil
- Pinch sonrasi enerji maliyeti: 323,000 USD/yil
- Yillik tasarruf: S = 800,000 - 323,000 = 477,000 USD/yil
- Esanjor agi yatirim maliyeti: C_yatirim = 950,000 USD
- SPP = 950,000 / 477,000 = **1.99 yil**

Karar kriteri: SPP < 3 yil → Iyi yatirim, SPP < 5 yil → Kabul edilebilir

### 5.2 Net Bugunku Deger — NPV (Net Present Value)

```
NPV = -C_yatirim + Sigma_{t=1}^{n} [S_t / (1 + i)^t]
```

Sabit yillik tasarruf icin:

```
NPV = -C_yatirim + S_yillik × [(1 + i)^n - 1] / [i × (1 + i)^n]
```

**Ornek (n=15 yil, i=%10):**
- NPV = -950,000 + 477,000 × [(1.10)^15 - 1] / [0.10 × (1.10)^15]
- NPV = -950,000 + 477,000 × 7.6061
- NPV = -950,000 + 3,628,110
- NPV = **+2,678,110 USD**

Karar kriteri: NPV > 0 → Yatirim yapilabilir

### 5.3 Ic Verim Orani — IRR (Internal Rate of Return)

IRR, NPV = 0 yapan iskonto oranidir:

```
0 = -C_yatirim + Sigma_{t=1}^{n} [S_t / (1 + IRR)^t]
```

Bu denklem iteratif olarak cozulur.

**Ornek icin yaklasik IRR hesabi:**
- SPP ~ 2 yil, n = 15 yil
- IRR ~ %48 (iteratif cozum veya tablo/yazilim ile)

Karar kriteri: IRR > WACC (agirlikli ortalama sermaye maliyeti) → Yatirim yapilabilir

Tipik sanayi esigi: IRR > %15–20

### 5.4 Karlilik Indeksi — PI (Profitability Index)

```
PI = (NPV + C_yatirim) / C_yatirim = NPV / C_yatirim + 1
```

**Ornek:**
- PI = (2,678,110 + 950,000) / 950,000 = 3,628,110 / 950,000 = **3.82**

Karar kriteri: PI > 1.0 → Yatirim yapilabilir, PI > 2.0 → Cok iyi yatirim

### 5.5 Yontemlerin Karsilastirilmasi

| Yontem | Avantaj                              | Dezavantaj                            | En Uygun Kullanim            |
|--------|--------------------------------------|---------------------------------------|------------------------------|
| SPP    | Basit, hizli hesaplanir              | Zaman degerini ihmal eder            | On eleme                     |
| NPV    | Paranin zaman degerini icerir        | Iskonto oranina duyarli              | Proje karsilastirma          |
| IRR    | Yuzde ile ifade, kolay anlasilir     | Coklu IRR sorunu, yeniden yatirim    | Performans olcumu            |
| PI     | Birim yatirim basina deger gosterir  | NPV ile ayni varsayimlar             | Bütce kisitli proje secimi   |

---

## 6. Utility Maliyet Hesabi (Utility Cost Calculation)

### 6.1 Buhar Maliyeti (Steam Cost)

Buhar maliyeti basinc/sicaklik seviyesine gore degisir:

| Buhar Seviyesi          | Basinc (bar) | Sicaklik (°C) | Maliyet (USD/ton) | Maliyet (USD/kWh_t) |
|-------------------------|-------------|---------------|-------------------|--------------------|
| Yuksek basinc (HP)      | 40–60       | 250–275       | 35–45             | 0.040–0.050       |
| Orta basinc (MP)        | 10–15       | 180–200       | 25–35             | 0.030–0.040       |
| Dusuk basinc (LP)       | 3–5         | 135–155       | 15–25             | 0.020–0.030       |

### 6.2 Sogutma Maliyeti

| Sogutma Tipi                  | Maliyet (USD/kWh_t) |
|-------------------------------|---------------------|
| Sogutma suyu (Cooling water)  | 0.002–0.005         |
| Hava sogutma (Air cooling)    | 0.003–0.008         |
| Chiller sogutma               | 0.015–0.030         |
| Kriyojenik sogutma             | 0.050–0.100         |

### 6.3 Diger Enerji Kaynaklari

| Kaynak                     | Birim                | Tipik Fiyat          |
|---------------------------|----------------------|----------------------|
| Dogal gaz (Natural gas)   | USD/m³               | 0.30–0.60            |
| Dogal gaz (Natural gas)   | USD/kWh              | 0.03–0.06            |
| Elektrik (Electricity)    | USD/kWh              | 0.08–0.15            |
| Fuel oil                  | USD/litre            | 0.50–0.90            |
| Komur (Coal)              | USD/ton              | 80–150               |

### 6.4 Yillik Isletme Maliyeti Hesabi

Referans problem icin (t_isletme = 8000 saat/yil):

**Isitma maliyeti (HP buhar, 0.045 USD/kWh_t):**
```
C_isitma = QH,min × C_birim × t_isletme
C_isitma = 1800 kW × 0.045 USD/kWh × 8000 saat/yil
C_isitma = 648,000 USD/yil
```

**Sogutma maliyeti (sogutma suyu, 0.004 USD/kWh_t):**
```
C_sogutma = QC,min × C_birim × t_isletme
C_sogutma = 2240 kW × 0.004 USD/kWh × 8000 saat/yil
C_sogutma = 71,680 USD/yil
```

**Toplam yillik enerji maliyeti:**
```
C_enerji_yillik = 648,000 + 71,680 = 719,680 USD/yil
```

---

## 7. Duyarlilik Analizi (Sensitivity Analysis)

Duyarlilik analizi, temel parametrelerdeki degisimin proje ekonomisi uzerindeki etkisini gosterir.

### 7.1 Enerji Fiyati Duyarliligi

| Enerji Fiyat Degisimi | C_enerji (USD/yil) | TAC (USD/yil) | SPP (yil) |
|------------------------|--------------------|---------------|-----------|
| -30%                   | 503,776            | 615,776       | 2.85      |
| -15%                   | 611,728            | 723,728       | 2.38      |
| Baz senaryo            | 719,680            | 831,680       | 1.99      |
| +15%                   | 827,632            | 939,632       | 1.73      |
| +30%                   | 935,584            | 1,047,584     | 1.53      |

### 7.2 Iskonto Orani Duyarliligi

n = 15 yil, yatirim = 950,000 USD, S = 477,000 USD/yil

| Iskonto Orani (i) | CRF     | C_yatirim_yillik (USD/yil) | NPV (USD)     |
|--------------------|---------|-----------------------------|---------------|
| %5                 | 0.0963  | 91,485                      | 4,000,420     |
| %8                 | 0.1168  | 110,960                     | 3,129,450     |
| %10                | 0.1315  | 124,925                     | 2,678,110     |
| %12                | 0.1468  | 139,460                     | 2,291,870     |
| %15                | 0.1710  | 162,450                     | 1,814,060     |

### 7.3 Tesis Omru Duyarliligi

i = %10, yatirim = 950,000 USD, S = 477,000 USD/yil

| Tesis Omru (yil) | CRF     | NPV (USD)     | PI    |
|-------------------|---------|---------------|-------|
| 10                | 0.1627  | 1,981,300     | 3.09  |
| 15                | 0.1315  | 2,678,110     | 3.82  |
| 20                | 0.1175  | 3,109,500     | 4.27  |
| 25                | 0.1102  | 3,380,200     | 4.56  |

### 7.4 Esanjor Maliyet Parametreleri Duyarliligi

b katsayisindaki degisimin etkisi (baz: b = 750, a = 8000, c = 0.81):

| b Degeri (USD/m^c) | C_yatirim (USD) | C_yatirim_yillik (USD/yil) | TAC (USD/yil) |
|---------------------|-----------------|----------------------------|---------------|
| 500 (-33%)          | 675,000         | 88,800                     | 808,480       |
| 625 (-17%)          | 812,000         | 106,800                    | 826,480       |
| 750 (baz)           | 950,000         | 124,925                    | 844,605       |
| 875 (+17%)          | 1,088,000       | 143,070                    | 862,750       |
| 1000 (+33%)         | 1,225,000       | 161,090                    | 880,770       |

### 7.5 Duyarlilik Ozeti

Parametrelerin TAC uzerindeki goreli etkisi (yuzde degisim / yuzde degisim):

| Parametre            | Duyarlilik Katsayisi | Yorum                            |
|----------------------|---------------------|----------------------------------|
| Enerji fiyati        | 0.85                | **Yuksek etki** — en kritik      |
| Iskonto orani        | 0.25                | Orta etki                        |
| Esanjor maliyet (b)  | 0.14                | Dusuk etki                       |
| Tesis omru           | 0.12                | Dusuk etki                       |

Sonuc: Enerji fiyatlari, proje ekonomisini en cok etkileyen parametredir. Enerji fiyatlarinin
yukselmesi beklenen ortamlarda Pinch projeleri daha da karli hale gelir.

---

## 8. Retrofit Maliyet Analizi (Retrofit Cost Analysis)

### 8.1 Mevcut Tesiste Degisiklik Maliyetleri

Retrofit projelerde yeni tesis maliyetine ek olarak su kalemler olusur:

| Maliyet Kalemi              | Tipik Deger            | Aciklama                              |
|-----------------------------|------------------------|---------------------------------------|
| Boru degisikligi (Repiping) | 5,000–30,000 USD/esanjor | Mevcut boru hatlarinin yeniden yonlendirilmesi |
| Ek alan (Additional area)   | Mevcut esanjora ek     | Mevcut esanjorun buyutulmesi veya paralel eklenmesi |
| Proses kesintisi (Downtime) | 10,000–100,000 USD/gun | Uretim kaybi                          |
| Muhendislik (Engineering)   | Yatirimin %10–15'i    | Detay muhendislik ve proje yonetimi   |
| Insaat/montaj               | Yatirimin %20–30'u    | Saha islemleri                        |

### 8.2 Artirimsal Maliyet Analizi (Incremental Cost Analysis)

Retrofit'te her ek esanjor veya modifikasyon icin artirimsal maliyet-tasarruf analizi yapilir:

```
Artirimsal SPP_j = Delta_C_yatirim_j / Delta_S_j
```

- Delta_C_yatirim_j : j. modifikasyonun ek maliyeti
- Delta_S_j : j. modifikasyonun ek yillik tasarruf

### 8.3 Marjinal Geri Odeme Egrisi (Marginal Payback Curve)

Modifikasyonlar artirimsal geri odeme suresine gore siralanir:

| Modifikasyon | Ek Maliyet (USD) | Ek Tasarruf (USD/yil) | Artirimsal SPP (yil) | Kumulatif Tasarruf (kW) |
|-------------|------------------|-----------------------|----------------------|------------------------|
| M1: H1-C1 eslesmesi | 120,000    | 180,000               | 0.67                 | 500                    |
| M2: H2-C2 eslesmesi | 85,000     | 95,000                | 0.89                 | 830                    |
| M3: H3-C1 ek esanjor | 65,000    | 55,000                | 1.18                 | 980                    |
| M4: Boru degisikligi | 45,000    | 32,000                | 1.41                 | 1090                   |
| M5: H2-C1 ek alan    | 95,000    | 48,000                | 1.98                 | 1220                   |
| M6: Utility degisimi  | 150,000   | 55,000                | 2.73                 | 1370                   |

### 8.4 Retrofit Karar Kriteri

- Artirimsal SPP < 2 yil olan tum modifikasyonlar **kesinlikle uygulanmali**
- 2–4 yil arasi olanlar **duruma gore degerlendirilmeli**
- 4 yil ustu olanlar genellikle **ertelenmeli**

Yukari tabloda M1–M5 arasi modifikasyonlar (SPP < 2 yil) uygulanmali, M6 degerlendirilmelidir.

---

## 9. Sayisal Ornek: Tam TAC Hesabi

Referans problem icin Delta T_min = 10°C'de tam TAC hesabi.

### 9.1 Veriler

- QH,min = 1800 kW, QC,min = 2240 kW
- Isitma maliyeti: 0.045 USD/kWh_t (HP buhar)
- Sogutma maliyeti: 0.004 USD/kWh_t (sogutma suyu)
- Isletme suresi: 8000 saat/yil
- Esanjor tipi: Boru-kabuk, karbon celigi (a=8000, b=750, c=0.81)
- Ortalama U = 0.5 kW/m²·°C
- Iskonto orani: i = %10
- Tesis omru: n = 15 yil
- Tahmini esanjor sayisi: N = 6

### 9.2 Adim 1: Enerji Maliyeti

```
C_isitma = 1800 × 0.045 × 8000 = 648,000 USD/yil
C_sogutma = 2240 × 0.004 × 8000 = 71,680 USD/yil
C_enerji = 648,000 + 71,680 = 719,680 USD/yil
```

### 9.3 Adim 2: Toplam Alan Hesabi

Bath formulu ile hesaplanan minimum alan: A_min = 523 m²

Esanjor basina ortalama alan: A_ort = 523 / 6 = 87.2 m²

### 9.4 Adim 3: Esanjor Maliyeti

Her esanjor icin:
```
C_esanjor = 8000 + 750 × (87.2)^0.81
C_esanjor = 8000 + 750 × 46.8
C_esanjor = 8000 + 35,100
C_esanjor = 43,100 USD
```

Not: A^c hesabi: 87.2^0.81 = e^(0.81 × ln(87.2)) = e^(0.81 × 4.468) = e^(3.619) = 37.3
Duzeltilmis: C_esanjor = 8000 + 750 × 37.3 = 8000 + 27,975 = 35,975 USD

Toplam esanjor maliyeti:
```
C_esanjor_toplam = 6 × 35,975 = 215,850 USD
```

### 9.5 Adim 4: Utility Esanjorleri

Sicak utility esanjoru (heater): Q = 1800 kW
```
A_heater = 1800 / (0.5 × 30) = 120 m²  (Delta_T_LM ~ 30°C varsayildi)
C_heater = 8000 + 750 × 120^0.81 = 8000 + 750 × 58.4 = 51,800 USD
```

Soguk utility esanjoru (cooler): Q = 2240 kW
```
A_cooler = 2240 / (0.5 × 25) = 179.2 m²  (Delta_T_LM ~ 25°C varsayildi)
C_cooler = 8000 + 750 × 179.2^0.81 = 8000 + 750 × 82.1 = 69,575 USD
```

Toplam utility esanjor maliyeti:
```
C_utility = 51,800 + 69,575 = 121,375 USD
```

### 9.6 Adim 5: Toplam Yatirim

```
C_yatirim = C_esanjor_toplam + C_utility = 215,850 + 121,375 = 337,225 USD
```

Kurulum ve muhendislik carpani (%40 ek):
```
C_yatirim_kurulu = 337,225 × 1.40 = 472,115 USD
```

### 9.7 Adim 6: Yillik Sermaye Maliyeti

```
CRF = [0.10 × (1.10)^15] / [(1.10)^15 - 1]
CRF = [0.10 × 4.177] / [4.177 - 1]
CRF = 0.4177 / 3.177
CRF = 0.1315

C_yatirim_yillik = 0.1315 × 472,115 = 62,083 USD/yil
```

### 9.8 Adim 7: TAC

```
TAC = C_yatirim_yillik + C_enerji_yillik
TAC = 62,083 + 719,680
TAC = 781,763 USD/yil
```

### 9.9 Sonuc Ozeti

| Kalem                        | Deger              |
|------------------------------|--------------------|
| Toplam alan (proses esanjor) | 523 m²             |
| Esanjor sayisi               | 6 + 2 (utility)    |
| Toplam yatirim (kurulu)      | 472,115 USD        |
| Yillik sermaye maliyeti      | 62,083 USD/yil     |
| Yillik enerji maliyeti       | 719,680 USD/yil    |
| **TAC**                      | **781,763 USD/yil** |
| SPP (mevcut 1,200,000 USD/yil referans) | 0.98 yil |
| NPV (15 yil, %10)            | 3,177,550 USD      |
| IRR                           | ~%98               |
| PI                            | 7.73               |

---

## Maliyet Egrileri (Cost Curves) Kavrami

TAC'nin Delta T_min ile degisim egrisi, iki zit egilimli egrinin toplamidir:

1. **Enerji maliyet egrisi:** Delta T_min arttikca monoton artar (daha fazla utility gerekir)
2. **Sermaye maliyet egrisi:** Delta T_min arttikca monoton azalir (daha kucuk alan gerekir)
3. **TAC egrisi:** Bu ikisinin toplami, bir minimum noktaya sahiptir

Bu minimum, **optimal Delta T_min** degerini verir. Sanayi uygulamalarinda optimal
Delta T_min genellikle 5–30°C araligindadir; proses kosullarına, enerji fiyatlarina ve
esanjor tiplerine bagli olarak degisir.

---

## İlgili Dosyalar

- `knowledge/factory/pinch/targeting.md` — Enerji ve alan hedefleme yontemleri
- `knowledge/factory/pinch/delta_t_min.md` — Delta T_min secimi ve optimizasyonu
- `knowledge/factory/pinch/hen_design.md` — Isi esanjor agi tasarimi
- `knowledge/factory/pinch/hen_retrofit.md` — Mevcut tesiste retrofit tasarimi
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arasi isi geri kazanimi
- `knowledge/factory/prioritization.md` — Yatirim onceliklendirme

## Referanslar

1. Linnhoff, B. (1994). "Use Pinch Analysis to Knock Down Capital Costs and Emissions." *Chemical Engineering Progress*, 90(8), 32-57.
2. Kemp, I.C. (2007). *Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy.* 2nd ed. Butterworth-Heinemann.
3. Smith, R. (2016). *Chemical Process Design and Integration.* 2nd ed. Wiley.
4. Klemes, J.J. (2013). *Handbook of Process Integration (PI): Minimisation of Energy and Water Use, Waste and Emissions.* Woodhead Publishing.
5. Townsend, D.W., Linnhoff, B. (1984). "Surface Area Targets for Heat Exchanger Networks." *IChemE Annual Research Meeting.*
6. Sinnott, R.K. (2005). *Chemical Engineering Design.* 4th ed. Butterworth-Heinemann. (Maliyet tahmin yontemleri)
7. Turton, R. et al. (2012). *Analysis, Synthesis and Design of Chemical Processes.* 4th ed. Prentice Hall. (CEPCI ve maliyet korelasyonlari)
