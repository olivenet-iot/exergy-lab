---
title: "Kazan Exergy Hesaplamalari"
category: reference
equipment_type: boiler
keywords: [exergy, kazan, termodinamik, hesaplama]
related_files: [boiler/benchmarks.md, boiler/audit.md, boiler/equipment/systems_overview.md]
use_when: ["Kazan exergy hesaplaması yapılırken", "Kazan verimliliği formülleri gerektiğinde"]
priority: high
last_updated: 2026-01-31
---
# Kazan Exergy Hesaplamalari

> Son guncelleme: 2026-01-31

## Temel Ilkeler

Kazan, yakitin kimyasal exergy'sini buhar veya sicak su termik exergy'sine donusturur.
Yanma tersinmezligi en buyuk exergy yikim kaynagidir (~%25-30 yakit exergy'si).
Bu termodinamik bir zorunluluktur -- elimine edilemez, yalnizca minimize edilebilir.

**Enerji verimi ile exergy verimi farki:**
Kazanlarda enerji (birinci yasa) verimi %85-95 arasindadir, ancak exergy (ikinci yasa)
verimi yalnizca %25-50 arasindadir. Bu buyuk fark, yanma isleminin yuksek sicaklikli
kimyasal enerjiyi nispeten dusuk sicaklikli buhar/sicak suya cevirirken onemli
kalite kaybi yaratmasindan kaynaklanir.

## 1. Yakit Exergy'si (Fuel Exergy)

### 1.1 Kimyasal Exergy

Yakitin kimyasal exergy'si, yakitin cevresiyle tam termodinamik denge haline
gelene kadar uretebilecegi maksimum isi:
```
Ex_fuel = m_dot_fuel x ex_ch

Burada:
- m_dot_fuel = yakit kutle debisi [kg/s]
- ex_ch = yakitin spesifik kimyasal exergy'si [kJ/kg]
```

Tipik yakit kimyasal exergy degerleri:

| Yakit Tipi | ex_ch [kJ/kg] | LHV [kJ/kg] | phi = ex_ch/LHV |
|------------|---------------|-------------|------------------|
| Dogal gaz | 51,850 | 47,141 | 1.04 |
| LPG (propan) | 49,000 | 46,350 | 1.06 |
| Fuel oil (No.6) | 45,500 | 40,600 | 1.12 |
| Motorin (dizel) | 47,400 | 42,700 | 1.11 |
| Tas komuru | 27,500 | 25,000 | 1.10 |
| Linyit | 12,800 | 11,500 | 1.11 |
| Biyokutle (odun) | 19,200 | 17,000 | 1.13 |
| Hidrojen | 117,600 | 120,000 | 0.98 |

### 1.2 Exergy/Enerji Orani (phi)

Yakitin kimyasal exergy'si ile alt isil degeri (LHV) arasindaki oran:
```
phi = ex_ch / LHV

Burada:
- phi = exergy/enerji orani (boyutsuz)
- ex_ch = spesifik kimyasal exergy [kJ/kg]
- LHV = alt isil deger [kJ/kg]
```

**Onemli:** Hidrokarbonlar icin phi > 1.0'dir (exergy, LHV'den buyuktur).
Bu, yakitin isi uretme potansiyelinin otesinde is uretme kapasitesine
sahip oldugunu gosterir.

### 1.3 Szargut Korelasyonu

Kati yakitlar icin kimyasal exergy tahmini (Szargut & Styrylska, 1964):
```
phi_solid = 1.0437 + 0.1882 x (H/C) + 0.0610 x (O/C) + 0.0404 x (N/C)

Burada:
- H/C = yakit elementel analizinde hidrojen/karbon kutle orani
- O/C = oksijen/karbon kutle orani
- N/C = azot/karbon kutle orani
```

Gaz yakitlar icin (Szargut):
```
phi_gas = 1.04 (dogal gaz icin pratik deger)
```

## 2. Buhar Exergy'si (Steam Exergy)

### 2.1 Fiziksel Exergy

Buharin fiziksel exergy'si, olum durumuna (dead state) gore:
```
Ex_steam = m_dot x [(h - h_0) - T_0 x (s - s_0)]

Burada:
- m_dot = buhar kutle debisi [kg/s]
- h = buhar entalpisi [kJ/kg]
- h_0 = olum durumu entalpisi (25 C, 1 atm sivi su) = 104.9 kJ/kg
- s = buhar entropisi [kJ/kg.K]
- s_0 = olum durumu entropisi = 0.3672 kJ/kg.K
- T_0 = olum durumu sicakligi = 298.15 K
```

**Not:** Olum durumu (dead state) olarak 25 C, 101.325 kPa basinctaki sivi su
alinir. Bu, buharin hem termal hem de mekanik exergy bilesenlerini icerir.

### 2.2 Doymus Buhar Tablosu

Cesitli basinclarda doymus buharin exergy degerleri (T_0 = 25 C, P_0 = 1 atm):

| P [bar] | T_sat [C] | h [kJ/kg] | s [kJ/kg.K] | ex [kJ/kg] |
|---------|-----------|-----------|-------------|------------|
| 1 | 99.6 | 2,675 | 7.359 | 486 |
| 3 | 133.5 | 2,725 | 6.992 | 644 |
| 5 | 151.8 | 2,749 | 6.821 | 730 |
| 7 | 165.0 | 2,763 | 6.709 | 790 |
| 10 | 179.9 | 2,778 | 6.586 | 858 |
| 15 | 198.3 | 2,792 | 6.445 | 936 |
| 20 | 212.4 | 2,799 | 6.340 | 994 |
| 25 | 224.0 | 2,801 | 6.257 | 1,038 |
| 40 | 250.4 | 2,801 | 6.070 | 1,134 |
| 60 | 275.6 | 2,784 | 5.890 | 1,213 |

### 2.3 Kizgin Buhar (Superheated Steam)

Kizgin buhar icin ayni formul gecelidir, ancak kizginlik derecesi
buhar exergy'sini onemli olcude arttirir:
```
Ex_sh = m_dot x [(h_sh - h_0) - T_0 x (s_sh - s_0)]

Burada:
- h_sh = kizgin buhar entalpisi [kJ/kg]
- s_sh = kizgin buhar entropisi [kJ/kg.K]
```

Ornek kizgin buhar exergy degerleri:

| P [bar] | T [C] | h [kJ/kg] | s [kJ/kg.K] | ex [kJ/kg] |
|---------|-------|-----------|-------------|------------|
| 10 | 250 | 2,943 | 7.038 | 911 |
| 10 | 350 | 3,158 | 7.301 | 987 |
| 20 | 300 | 3,024 | 6.768 | 1,049 |
| 20 | 400 | 3,248 | 7.127 | 1,121 |
| 40 | 400 | 3,214 | 6.769 | 1,201 |
| 40 | 500 | 3,446 | 7.090 | 1,282 |
| 60 | 400 | 3,178 | 6.541 | 1,233 |
| 60 | 500 | 3,423 | 6.880 | 1,318 |

## 3. Sicak Su Exergy'si (Hot Water Exergy)

### 3.1 Basitlestirilmis Formul (Sikilamazlik Kabulu)

Sicak su icin, sikilamaz sivi modeliyle:
```
Ex_water = m_dot x Cp x [(T - T_0) - T_0 x ln(T/T_0)]

Burada:
- m_dot = su kutle debisi [kg/s]
- Cp = suyun ortalama isil kapasitesi = 4.18 kJ/kg.K
- T = su sicakligi [K]
- T_0 = olum durumu sicakligi = 298.15 K (25 C)
```

**Onemli:** T degerleri mutlaka Kelvin cinsinden olmalidir!

### 3.2 Sicak Su Exergy Tablosu

Cesitli sicakliklarda sicak suyun spesifik exergy degerleri (T_0 = 25 C):

| T [C] | T [K] | (h-h_0) [kJ/kg] | ex [kJ/kg] | Carnot faktoru |
|-------|-------|-----------------|------------|----------------|
| 40 | 313.15 | 62.7 | 1.4 | 0.048 |
| 50 | 323.15 | 104.5 | 4.7 | 0.077 |
| 60 | 333.15 | 146.3 | 10.4 | 0.104 |
| 70 | 343.15 | 188.1 | 18.5 | 0.130 |
| 80 | 353.15 | 229.9 | 28.8 | 0.155 |
| 90 | 363.15 | 271.7 | 41.3 | 0.179 |
| 100 | 373.15 | 313.5 | 55.9 | 0.201 |
| 120 | 393.15 | 397.1 | 90.2 | 0.242 |
| 150 | 423.15 | 522.4 | 149.9 | 0.295 |
| 180 | 453.15 | 647.7 | 221.7 | 0.342 |

**Not:** Carnot faktoru = 1 - T_0/T degerini gosterir. Dusuk sicaklikli
sicak suyun exergy iceriginin ne kadar dusuk olduguna dikkat ediniz.
Ornegin 60 C'lik sicak suyun enerji icerigi 146.3 kJ/kg, ancak exergy
icerigi yalnizca 10.4 kJ/kg'dir (%7.1).

## 4. Baca Gazi Exergy Kaybi (Flue Gas Exergy Loss)

### 4.1 Genel Formul

Baca gazinin fiziksel exergy'si:
```
Ex_flue = m_dot_flue x [(h_flue - h_0) - T_0 x (s_flue - s_0)]

Burada:
- m_dot_flue = baca gazi kutle debisi [kg/s]
- h_flue = baca gazi entalpisi [kJ/kg]
- s_flue = baca gazi entropisi [kJ/kg.K]
- h_0, s_0 = olum durumunda (25 C, 1 atm) degerler
```

### 4.2 Basitlestirilmis Formul (Ideal Gaz Kabulu)

Baca gazi icin ideal gaz ve sabit Cp kabuluyle:
```
Ex_flue = m_dot_flue x Cp_flue x (T_flue - T_0) x [1 - T_0/T_flue]

Burada:
- Cp_flue = baca gazi ortalama isil kapasitesi ≈ 1.05 kJ/kg.K
- T_flue = baca gazi sicakligi [K]
- T_0 = 298.15 K
```

**DIKKAT:** Tum sicaklik degerleri Kelvin cinsinden olmalidir!

### 4.3 Baca Gazi Sicakligina Gore Exergy Kaybi

| T_flue [C] | T_flue [K] | Carnot | Ex/m_dot [kJ/kg] | Kayip sinifi |
|------------|-----------|--------|------------------|-------------|
| 120 | 393.15 | 0.242 | 24.1 | Cok iyi |
| 150 | 423.15 | 0.295 | 38.7 | Iyi |
| 180 | 453.15 | 0.342 | 56.6 | Ortalama |
| 200 | 473.15 | 0.370 | 68.1 | Yuksek |
| 250 | 523.15 | 0.430 | 101.5 | Cok yuksek |
| 300 | 573.15 | 0.480 | 138.4 | Asiri |
| 350 | 623.15 | 0.521 | 177.9 | Asiri |

### 4.4 Baca Gazi Debisi Tahmini

Dogal gaz icin yaklasik baca gazi debisi:
```
m_dot_flue = m_dot_fuel x (1 + AFR)

AFR_stoich = 17.2 kg_hava/kg_yakit (dogal gaz icin)
AFR_actual = AFR_stoich x (1 + fazla_hava/100)

Burada:
- AFR = hava/yakit orani [kg/kg]
- fazla_hava = fazla hava yuzdesi [%]
```

## 5. Yanma Tersinmezligi (Combustion Irreversibility)

### 5.1 Entropi Uretimi Formulu

Yanma isleminin entropi uretimi:
```
I_comb = T_0 x S_gen_comb

S_gen_comb = m_dot_flue x s_products - m_dot_fuel x s_fuel - m_dot_air x s_air

Burada:
- I_comb = yanma tersinmezligi (exergy yikimi) [kW]
- S_gen_comb = yanmada uretilen entropi [kW/K]
- T_0 = olum durumu sicakligi [K]
```

### 5.2 Basitlestirilmis Tahmin

Pratikte yanma tersinmezligi yakit exergy'sinin belirli bir yuzdesidir:
```
I_comb ≈ f_comb x Ex_fuel

Burada:
- f_comb = yanma tersinmezlik faktoru (boyutsuz)
```

Yakita gore tipik yanma tersinmezlik degerleri:

| Yakit Tipi | f_comb | I_comb / Ex_fuel |
|------------|--------|------------------|
| Dogal gaz (CH4) | 0.25 - 0.30 | %25-30 |
| LPG (propan) | 0.26 - 0.31 | %26-31 |
| Fuel oil | 0.28 - 0.32 | %28-32 |
| Motorin | 0.27 - 0.31 | %27-31 |
| Tas komuru | 0.30 - 0.35 | %30-35 |
| Linyit | 0.32 - 0.38 | %32-38 |
| Biyokutle | 0.30 - 0.38 | %30-38 |
| Hidrojen | 0.22 - 0.26 | %22-26 |

**Kritik Not:** Bu kayip termodinamik bir zorunluluktur. Kimyasal reaksiyonun
tersinmez dogasindan kaynaklanir ve hicbir muhendislik onlemiyle sifira
indirilemez. Yalnizca on isitma (rejenerasyon) ile kismen azaltilabilir.

### 5.3 Alev Sicakliginin Etkisi

Yuksek adyabatik alev sicakligi, yanma exergy yikimini azaltir:
```
I_comb ≈ Ex_fuel x [1 - (T_flame - T_0) / T_flame x (T_0/T_0)]

Basitlestirilmis:
I_comb ≈ Ex_fuel x [1 - eta_Carnot_flame]

Burada:
- T_flame = adyabatik alev sicakligi [K]
- Dogal gaz: T_flame ≈ 2,230 K (stokiyometrik)
- Fuel oil: T_flame ≈ 2,150 K
- Komur: T_flame ≈ 2,050 K
```

## 6. Radyasyon ve Konveksiyon Kaybi

### 6.1 Yuzey Radyasyon/Konveksiyon Kaybi

Kazan dis yuzeyinden cevrye olan isi kaybi:
```
Q_rad = h_comb x A_surface x (T_surface - T_amb)

Ex_rad = Q_rad x (1 - T_0/T_surface)

Burada:
- h_comb = birlesik isi transfer katsayisi ≈ 10-15 W/m2.K
- A_surface = kazan dis yuzey alani [m2]
- T_surface = yuzey sicakligi [K]
- T_amb = ortam sicakligi [K]
```

### 6.2 Basitlestirilmis Tahmin (ABMA Standardi)

Amerikan Kazan Ureticileri Birligi (ABMA) tahmini:
```
Q_rad / Q_input = C x Q_input^(-0.38)

Burada:
- Q_input = kazan yakit girisi [MW]
- C = kazan tipi sabiti
  - Ates borulu: C = 0.062
  - Su borulu: C = 0.055
```

Tipik radyasyon/konveksiyon kayip degerleri:

| Kazan Kapasitesi [MW] | Kayip [%] |
|-----------------------|-----------|
| 1 | 2.5 - 4.0 |
| 5 | 1.0 - 1.5 |
| 10 | 0.5 - 1.0 |
| 20 | 0.3 - 0.7 |
| 50 | 0.2 - 0.4 |
| 100 | 0.1 - 0.3 |

**Not:** Bu degerler enerji kaybi olarak verilmistir. Exergy kaybi, Carnot
faktoru ile carpilarak bulunur ve genellikle daha dusuktur (T_surface dusuk).

## 7. Blowdown Exergy Kaybi

### 7.1 Blowdown Debisi

Kazan blowdown'u, kazan suyundaki konsantre cozunmus katilari uzaklastirmak
icin periyodik veya surekli olarak kazan suyunun bosaltilmasidir:
```
m_dot_bd = m_dot_fw x BD_rate

Burada:
- m_dot_bd = blowdown kutle debisi [kg/s]
- m_dot_fw = besleme suyu kutle debisi [kg/s]
- BD_rate = blowdown orani (tipik %2-5, kotu su kalitesinde %8-10)
```

### 7.2 Blowdown Exergy Kaybi

Blowdown suyu kazan basincinda doymus sividir:
```
Ex_bd = m_dot_bd x [(h_f - h_0) - T_0 x (s_f - s_0)]

Burada:
- h_f = kazan basincindaki doymus sivi entalpisi [kJ/kg]
- s_f = kazan basincindaki doymus sivi entropisi [kJ/kg.K]
- h_0 = 104.9 kJ/kg (25 C sivi su)
- s_0 = 0.3672 kJ/kg.K
```

Cesitli basinclarda blowdown exergy degerleri (doymus sivi):

| P [bar] | T_sat [C] | h_f [kJ/kg] | ex_bd [kJ/kg] |
|---------|-----------|-------------|---------------|
| 5 | 151.8 | 640 | 87 |
| 10 | 179.9 | 763 | 128 |
| 15 | 198.3 | 845 | 158 |
| 20 | 212.4 | 909 | 183 |
| 25 | 224.0 | 962 | 204 |
| 40 | 250.4 | 1,087 | 253 |

### 7.3 Blowdown Isi Geri Kazanimi

Flash tanki ve isi degistiricisi ile blowdown exergy kaybi azaltilabilir:
```
Ex_bd_recovered = m_dot_bd x [(h_f - h_recovered) - T_0 x (s_f - s_recovered)]

Tasarruf_orani ≈ %60-80 (flash tank + isi degistirici ile)
```

## 8. Toplam Exergy Verimi (Overall Exergy Efficiency)

### 8.1 Direkt Yontem

Exergy veriminin dogrudan hesaplanmasi:
```
eta_ex = Ex_steam / Ex_fuel x 100 [%]

Burada:
- Ex_steam = m_dot_steam x [(h_steam - h_0) - T_0 x (s_steam - s_0)] [kW]
- Ex_fuel = m_dot_fuel x ex_ch [kW]
```

Tipik exergy verim araliklari:

| Kazan Tipi | eta_energy [%] | eta_exergy [%] |
|------------|---------------|----------------|
| Yoğunlasmasiz (standart) | 80 - 88 | 25 - 35 |
| Dusuk NOx | 82 - 90 | 28 - 38 |
| Economizer'li | 88 - 94 | 32 - 42 |
| Yogunlasmali (condensing) | 95 - 107* | 35 - 48 |

*Yogunlasmali kazanlarda enerji verimi LHV bazinda >%100 olabilir (HHV bazinda <%100)

### 8.2 Indirekt Yontem (Kayip Analizi)

Toplam kayiplardan exergy verimi hesaplama:
```
eta_ex = 100% - I_combustion% - Ex_flue% - Ex_rad% - Ex_bd% - Ex_other%

Burada:
- I_combustion% = yanma tersinmezligi kaybi [%]
- Ex_flue% = baca gazi exergy kaybi [%]
- Ex_rad% = radyasyon/konveksiyon exergy kaybi [%]
- Ex_bd% = blowdown exergy kaybi [%]
- Ex_other% = diger exergy kayiplari (kapatilmamis, tam yanmamis yakit vb.) [%]
```

Tipik exergy kayip dagilimi (dogal gaz, iyi bakimli kazan):

| Kayip Kalemi | Exergy Kaybi [%] |
|-------------|------------------|
| Yanma tersinmezligi | 25 - 30 |
| Baca gazi exergy kaybi | 8 - 15 |
| Radyasyon/konveksiyon | 0.5 - 2.0 |
| Blowdown | 0.5 - 2.0 |
| Diger kayiplar | 1.0 - 3.0 |
| **Toplam kayip** | **35 - 52** |
| **Exergy verimi** | **48 - 65** |

**Not:** Yukaridaki degerler yakit exergy'sinin yuzdeleri olarak verilmistir.
Dusuk sicaklikli buhar uygulamalarinda exergy verimi %25'e kadar dusebilir.

## 9. Enerji Verimi Hesaplamalari

### 9.1 Direkt Yontem (Giris-Cikis)

Enerji veriminin dogrudan hesaplanmasi:
```
eta_th = [m_dot_steam x (h_steam - h_fw)] / [m_dot_fuel x LHV] x 100 [%]

Burada:
- m_dot_steam = buhar kutle debisi [kg/s]
- h_steam = uretilen buharin entalpisi [kJ/kg]
- h_fw = besleme suyu entalpisi [kJ/kg]
- m_dot_fuel = yakit kutle debisi [kg/s]
- LHV = yakitin alt isil degeri [kJ/kg]
```

### 9.2 Indirekt Yontem (Kayip Yontemi, BS 845 / ASME PTC 4)

Toplam kayiplardan enerji verimi hesaplama:
```
eta_th = 100% - L_flue_dry - L_flue_wet - L_rad - L_bd - L_unburnt - L_other

Burada:
- L_flue_dry = kuru baca gazi kaybi [%]
- L_flue_wet = nem kaybi (yakittaki H2 ve nem) [%]
- L_rad = radyasyon/konveksiyon kaybi [%]
- L_bd = blowdown kaybi [%]
- L_unburnt = yanmamis yakit kaybi (CO, is, kurum) [%]
- L_other = diger kayiplar [%]
```

### 9.3 Kuru Baca Gazi Kaybi (Siegert Formulu)

Basitlestirilmis baca gazi kaybi tahmini:
```
L_flue_dry = k_Siegert x (T_flue - T_air) / CO2%

Burada:
- k_Siegert = yakit sabiti
  - Dogal gaz: k = 0.38
  - Fuel oil: k = 0.56
  - Komur: k = 0.68
- T_flue = baca gazi sicakligi [C]
- T_air = yanma havasi sicakligi [C]
- CO2% = baca gazindaki CO2 yuzdesi [%]
```

## 10. Economizer Etkisi

### 10.1 Economizer Isi Kazanimi

Economizer, baca gaziyla besleme suyunu on isitarak verimliligi arttirir:
```
Q_econ = m_dot_flue x Cp_flue x (T_flue_in - T_flue_out)

Burada:
- Q_econ = economizer isi kazanimi [kW]
- T_flue_in = economizer girisi baca gazi sicakligi [C]
- T_flue_out = economizer cikisi baca gazi sicakligi [C]
- Cp_flue ≈ 1.05 kJ/kg.K
```

### 10.2 Yakit Tasarrufu

Her 20 C baca gazi sicaklik dususu yaklasik %1 verim artisi saglar:
```
delta_eta ≈ (T_flue_in - T_flue_out) / 20 x 1.0 [% puan]

Yakit tasarrufu = Q_econ / (LHV x eta_boiler)

Yillik_tasarruf = Yakit_tasarrufu x calisma_saati x yakit_fiyati

Burada:
- Yakit_tasarrufu = tasarruf edilen yakit debisi [kg/s veya m3/s]
- calisma_saati = yillik calisma suresi [saat/yil]
- yakit_fiyati = birim yakit maliyeti [EUR/kg veya EUR/m3]
```

### 10.3 Ciy Noktasi Sinirlamasi

Baca gazi sicakligi asit ciy noktasindan dusuk olamamalidir:
```
Kuresel ciy noktasi (yaklasik):
- Dogal gaz: T_dew ≈ 55-60 C (su buhari ciy noktasi)
- Fuel oil (dusuk kuresel): T_dew ≈ 120-140 C (SO3 asit ciy noktasi)
- Komur (yuksek kuresel): T_dew ≈ 130-160 C
```

**Uyari:** Kuresel iceren yakitlarda baca gazi sicakligi asit ciy noktasinin
uzerine tutulmali, aksi halde kazan ve economizer korozyona ugrar.

## 11. Fazla Hava Etkisi (Excess Air Effect)

### 11.1 O2'den Fazla Hava Hesabi

Baca gazindaki O2 olcumunden fazla hava yuzdesini hesaplama:
```
Fazla_hava [%] = O2% / (21 - O2%) x 100

Burada:
- O2% = baca gazindaki oksijen yuzdesi (kuru bazda) [%]
- 21 = havadaki O2 yuzdesi [%]
```

Tipik O2 ve fazla hava degerleri:

| O2 [%] | Fazla Hava [%] | Durum |
|--------|---------------|-------|
| 2.0 | 10.5 | Optimal (dogal gaz) |
| 3.0 | 16.7 | Iyi |
| 5.0 | 31.3 | Yuksek |
| 7.0 | 50.0 | Cok yuksek |
| 9.0 | 75.0 | Asiri |

### 11.2 Verim Etkisi

Her %1 fazla O2 artisi yaklasik %1 enerji verimi kaybi yaratir:
```
delta_eta ≈ -1.0 x delta_O2 [% puan]

Burada:
- delta_O2 = O2 yuzdesindeki artis [% puan]
```

Optimal fazla hava degerleri (yakita gore):

| Yakit Tipi | Optimal O2 [%] | Optimal Fazla Hava [%] |
|------------|---------------|----------------------|
| Dogal gaz | 1.5 - 3.0 | 7.5 - 16.7 |
| LPG | 2.0 - 3.0 | 10.5 - 16.7 |
| Fuel oil | 2.5 - 4.0 | 13.5 - 23.5 |
| Komur (toz) | 3.0 - 5.0 | 16.7 - 31.3 |
| Komur (izgarali) | 5.0 - 8.0 | 31.3 - 61.5 |

## 12. Exergy Akis Diyagrami (Grassmann Diagram)

Tipik bir dogal gaz kazaninin exergy akis diyagrami:

```
YAKIT EXERGY GIRISI (100%)
|
|======================================================================|
|                                                                      |
|   YANMA (Adyabatik alev: ~2230 K)                                   |
|   |                                                                  |
|   |--- Yanma Tersinmezligi (%25-30) ---------> EXERGY YIKIMI        |
|   |    [Termodinamik zorunluluk]               (geri kazanilamaz)    |
|   |                                                                  |
|   v                                                                  |
|   YANMA URUNLERI EXERGY'SI (%70-75)                                 |
|   |                                                                  |
|   |=== Isi Transferi (ocak + konveksiyon) ===>  BUHAR EXERGY'SI     |
|   |    |                                        (%35-48)             |
|   |    |--- Isi transferi tersinmezligi (%15-25) --> EXERGY YIKIMI  |
|   |    |    [Sicaklik farki kaynakli]                                |
|   |                                                                  |
|   |--- Baca Gazi Exergy Kaybi (%8-15) --------> KAYIP               |
|   |    [Economizer ile azaltilabilir]           (kismi geri kazanim) |
|   |                                                                  |
|   |--- Radyasyon/Konveksiyon (%0.5-2) --------> KAYIP               |
|   |    [Yalitim ile azaltilabilir]              (dusuk kaliteli)     |
|   |                                                                  |
|   |--- Blowdown (%0.5-2) ---------------------> KAYIP               |
|   |    [Flash tank ile geri kazanilabilir]       (orta kaliteli)     |
|   |                                                                  |
|   |--- Diger (%1-3) ---------------------------> KAYIP               |
|        [CO, yanmamis yakit, vb.]                                     |
|                                                                      |
|======================================================================|

OZET:
  Faydali buhar exergy'si:    %35-48
  Yanma tersinmezligi:        %25-30  (azaltilamaz)
  Isi transferi tersinmezligi:%15-25  (kismi azaltilabilir)
  Baca gazi kaybi:            %8-15   (economizer ile azaltilabilir)
  Diger kayiplar:             %2-7    (cesitli onlemlerle azaltilabilir)
```

## 13. Ornek Hesaplamalar

### 13.1 Temel Kazan Exergy Hesabi

**Senaryo:** Dogal gaz yakitli, 10 bar doymus buhar ureten kazan

**Girdiler:**
- Buhar debisi: m_dot_steam = 5,000 kg/saat = 1.389 kg/s
- Buhar durumu: 10 bar doymus buhar
- Besleme suyu sicakligi: 80 C
- Yakit: Dogal gaz (LHV = 47,141 kJ/kg, ex_ch = 51,850 kJ/kg)
- Yakit tuketimi: m_dot_fuel = 370 kg/saat = 0.1028 kg/s
- Baca gazi sicakligi: 180 C
- O2 yuzdesi: %3.0
- Calisma: 8,000 saat/yil
- Dogal gaz fiyati: 0.35 EUR/m3 (0.44 EUR/kg)

**Hesap:**

Adim 1 - Yakit exergy girisi:
```
Ex_fuel = m_dot_fuel x ex_ch
        = 0.1028 x 51,850
        = 5,330 kW
```

Adim 2 - Buhar exergy cikisi (tablodan: 10 bar doymus buhar ex = 858 kJ/kg):
```
Ex_steam = m_dot_steam x ex_steam
         = 1.389 x 858
         = 1,192 kW
```

Besleme suyu exergy'si (80 C sicak su, tablodan ex ≈ 28.8 kJ/kg):
```
Ex_fw = m_dot_steam x ex_fw
      = 1.389 x 28.8
      = 40 kW
```

Net faydali exergy:
```
Ex_net = Ex_steam - Ex_fw = 1,192 - 40 = 1,152 kW
```

Adim 3 - Exergy verimi:
```
eta_ex = Ex_net / Ex_fuel x 100
       = 1,152 / 5,330 x 100
       = 21.6%
```

Adim 4 - Enerji verimi (karsilastirma icin):
```
Q_fuel = m_dot_fuel x LHV = 0.1028 x 47,141 = 4,846 kW

h_steam (10 bar doymus) = 2,778 kJ/kg
h_fw (80 C) = 335 kJ/kg

Q_steam = m_dot_steam x (h_steam - h_fw) = 1.389 x (2,778 - 335) = 3,394 kW

eta_energy = Q_steam / Q_fuel x 100 = 3,394 / 4,846 x 100 = 70.0%
```

**Sonuc:** Enerji verimi %70.0, exergy verimi ise yalnizca %21.6.
Bu, enerji veriminin sistemin termodinamik performansini abarttigini gosterir.

### 13.2 Baca Gazi Exergy Kaybi Hesabi

**Girdiler (Ornek 13.1'den devam):**
- Baca gazi sicakligi: T_flue = 180 C = 453.15 K
- Fazla hava: %16.7 (O2 = %3.0'dan)
- Stokiyometrik hava/yakit orani: 17.2

**Hesap:**
```
AFR_actual = 17.2 x (1 + 16.7/100) = 17.2 x 1.167 = 20.07

m_dot_flue = m_dot_fuel x (1 + AFR_actual)
           = 0.1028 x (1 + 20.07)
           = 0.1028 x 21.07
           = 2.166 kg/s

Ex_flue = m_dot_flue x Cp_flue x (T_flue - T_0) x [1 - T_0/T_flue]
        = 2.166 x 1.05 x (453.15 - 298.15) x [1 - 298.15/453.15]
        = 2.166 x 1.05 x 155.0 x 0.342
        = 120.5 kW

Ex_flue/Ex_fuel = 120.5 / 5,330 x 100 = 2.3%
```

**Not:** Baca gazi exergy kaybi %2.3, ancak enerji kaybi cok daha yuksektir:
```
Q_flue = m_dot_flue x Cp_flue x (T_flue - T_0)
       = 2.166 x 1.05 x 155.0
       = 352.4 kW

Q_flue/Q_fuel = 352.4 / 4,846 x 100 = 7.3%
```
Enerji kaybi %7.3 iken exergy kaybi sadece %2.3. Bu, baca gazinin dusuk
sicakliginin (180 C) dusuk is uretme kapasitesini yansitir.

### 13.3 Sistem Seviyesi Exergy Dengesi

**Ornek 13.1 kazani icin tam exergy dengesi:**

```
EXERGY GIRISI:
  Yakit exergy'si:              5,330 kW   (100.0%)

EXERGY CIKISI:
  Buhar exergy'si (net):        1,152 kW   (21.6%)

EXERGY KAYIPLARI:
  Yanma tersinmezligi:          1,439 kW   (27.0%)
  Isi transferi tersinmezligi:  2,340 kW   (43.9%)
  Baca gazi exergy:               121 kW   (2.3%)
  Radyasyon/konveksiyon:           43 kW   (0.8%)
  Blowdown:                        53 kW   (1.0%)
  Diger (CO, yanmamis vb.):       182 kW   (3.4%)
  -----------------------------------------------
  TOPLAM KAYIP:                 4,178 kW   (78.4%)
  TOPLAM:                       5,330 kW   (100.0%)
```

**Yorum:** Kazan exergy analizinde en buyuk iki kayip kalemi:
1. Yanma tersinmezligi (%27.0) - termodinamik zorunluluk, azaltilamaz
2. Isi transferi tersinmezligi (%43.9) - sicaklik farkindan kaynaklanan
   kayip, kizgin buhar veya yuksek basincli buhar ile azaltilabilir

Baca gazi kaybi, enerji analizinde buyuk gorunse de (%7.3), exergy
analizinde nispeten kucuktur (%2.3) cunku dusuk sicaklikli isi
dusuk exergy icerir.

### 13.4 Economizer Eklenmesinin Etkisi

**Senaryo:** Ornek 13.1 kazanina economizer eklenerek baca gazi
sicakliginin 180 C'den 120 C'ye dusurulmesi

**Hesap:**
```
Q_econ = m_dot_flue x Cp_flue x (T_flue_in - T_flue_out)
       = 2.166 x 1.05 x (180 - 120)
       = 2.166 x 1.05 x 60
       = 136.5 kW

Verim artisi:
delta_eta ≈ (180 - 120) / 20 x 1.0 = 3.0 % puan

Yakit tasarrufu:
m_dot_fuel_saved = Q_econ / (LHV x eta_boiler)
                 = 136.5 / (47,141 x 0.73)
                 = 0.00397 kg/s = 14.3 kg/saat

Yillik tasarruf:
Yakit_tasarrufu = 14.3 x 8,000 = 114,400 kg/yil
Maliyet_tasarrufu = 114,400 x 0.44 = 50,336 EUR/yil
```

## 14. Sinirlamalar

1. **Ideal gaz kabulu:** Baca gazi hesaplamalarinda ideal gaz kabulu
   yapilmistir. Yuksek nem icerikli veya dusuk sicaklikli durumlarda
   gercek gaz davranisi sapmalara yol acabilir.

2. **Sabit Cp kabulu:** Isil kapasite degerleri sabit alinmistir.
   Gercekte Cp, sicaklikla onemli olcude degisir. Yuksek hassasiyet
   gerektiren durumlarda sicakliga bagli Cp korelasyonlari kullanilmalidir.

3. **Kararli hal analizi:** Hesaplamalar kararli hal (steady-state)
   icin yapilmistir. Kazan baslangic/durdurma ve yuk degisimleri
   sirasindaki gecici rejim kayiplari dahil degildir.

4. **Kimyasal exergy basitlestirilmesi:** Yakit kimyasal exergy degerleri
   standart referans degerler uzerinden alinmistir. Gercek yakit
   kompozisyonu farklilik gosterebilir (ozellikle komur ve biyokutle icin).

5. **Isi transferi tersinmezligi:** Ocak icindeki radyasyon ve konveksiyon
   isi transferi tersinmezligi basitlestirilmis modelle hesaplanmistir.
   Detayli CFD analizi daha dogru sonuc verebilir.

## İlgili Dosyalar

- `knowledge/formulas/compressor_exergy.md` - Kompresor exergy hesaplamalari
- `knowledge/equipment/compressed_air_systems.md` - Basinclı hava sistemleri
- `knowledge/benchmarks/compressor_benchmarks.md` - Kompresor kiyaslama degerleri

## Referanslar

- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 4th Edition
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," Elsevier, 3rd Edition
- Cengel, Y.A. & Boles, M.A., "Thermodynamics: An Engineering Approach," McGraw-Hill, 9th Edition
- ASME PTC 4, "Fired Steam Generators - Performance Test Codes"
- Rosen, M.A. (2001), "Energy- and exergy-based comparison of coal-fired and nuclear steam power plants," Exergy Int. J., 1(3), 180-192
- Szargut, J. & Styrylska, T. (1964), "Approximate evaluation of the exergy of fuels," Brennstoff-Warme-Kraft, 16(12), 589-596
- Aljundi, I.H. (2009), "Energy and exergy analysis of a steam power plant in Jordan," Applied Thermal Engineering, 29, 324-328
- Regulagadda, P. et al. (2010), "Exergy analysis of a thermal power plant with measured boiler and turbine losses," Applied Thermal Engineering, 30, 970-976
- BS 845:1987, "Methods for assessing thermal performance of boilers for steam, hot water and high temperature heat transfer fluids"
