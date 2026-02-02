---
title: "Yogusmali Buhar Turbini — Condensing Steam Turbine"
category: equipment
equipment_type: steam_turbine
subtype: "Yogusmali (Condensing)"
keywords: [yogusmali turbin, condensing, kondenser, vakum, Baumann kurali, exhaust loss, yas buhar, exergy]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/extraction.md, steam_turbine/solutions/efficiency_improvement.md, boiler/formulas.md, factory/cogeneration.md]
use_when: ["Yogusmali turbin analizi yapilirken", "Kondenser performansi degerlendirilirken", "Maksimum elektrik uretimi hesaplanirken", "Baumann kurali uygulanirken"]
priority: high
last_updated: 2026-01-31
---
# Yogusmali Buhar Turbini — Condensing Steam Turbine

> Son guncelleme: 2026-01-31

## Genel Bilgiler

Yogusmali (condensing) buhar turbinleri, buharin vakum kosullarinda kondense
olana kadar genisletilerek maksimum is elde edilmesini saglayan turbin tipidir.
Cikis buhari kondenserde sivilastirilir ve isi sogutma suyuna veya havaya atilir.
Bu tip turbinler, termodinamik olarak mevcut entalpi farkinin en buyuk kismini
ise cevirir; ancak kondenserde atilan isi, onemli bir exergy kaybi olusturur.

- **Tip:** Yogusmali (condensing) turbin
- **Kapasite araligi:** 1 - 1,500 MW (endustriyel: tipik 5-100 MW, santral: 100-1,500 MW)
- **Giris kosullari:** 40 - 300 bar, 400 - 600 C (kizgin veya kizgin+reheat)
- **Cikis basinci:** 0.03 - 0.10 bar (vakum kosullari)
- **Elektrik verimi:** %30 - 42 (yalniz elektrik bazinda, Rankine cevrimi)
- **Izentropik verim:** %75 - 93 (boyut ve kademe sayisina bagli)
- **Tipik cikis nemi:** %8 - 12 (son kademelerde yas buhar)
- **Yaygin markalar:** Siemens, GE, MHI, Toshiba, Dongfang, Shanghai Electric

## Calisma Prensibi

### Rankine Cevrimi

Yogusmali turbin tam Rankine cevrimini tamamlar:

```
1. KAZAN: Sivi su --> Kizgin buhar (sabit basincta isobark isitma)
   - Ekonomizer: su on isitma
   - Evaporator: buhar olusumu
   - Superheater: kizginlik

2. TURBIN: Kizgin buhar --> Yas buhar (adyabatik genisleme)
   - Yuksek basinc (HP) kademesi
   - [Reheat (varsa)]
   - Orta basinc (IP) kademesi
   - Dusuk basinc (LP) kademesi

3. KONDENSER: Yas buhar --> Sivi su (sabit basincta isobark sogutma)
   - Buhar yogusur, latent isi sogutma suyuna atilir

4. POMPA: Sivi su --> Yuksek basincli sivi su (adyabatik sikistirma)
   - Besleme suyu pompasi ile kazana geri besleme
```

### Kondenser Tipleri

| Kondenser Tipi | Sogutma Ortami | Tipik Vakum [mbar] | Avantaj | Dezavantaj |
|----------------|---------------|--------------------:|---------|------------|
| Su sogutmali (water-cooled) | Nehir/deniz suyu | 30 - 50 | En iyi vakum, yuksek verim | Su kaynagi gerektirir |
| Sogutma kulesi (cooling tower) | Sirkule eden su | 40 - 70 | Su sarfiyati azalir | Orta verim, kule maliyeti |
| Hava sogutmali (air-cooled) | Hava | 80 - 150 | Su gerektirmez | En kotu vakum, dusuk verim |
| Hibrit (hybrid) | Hava + su | 50 - 100 | Esneklik | Karmasik, yuksek maliyet |

### Vakum Seviyesinin Guce Etkisi

```
Kondenser basinci ve turbin gucu iliskisi:

P_kond [mbar] | Cikis Entalpisi [kJ/kg] | Guc Etkisi (referans: 50 mbar)
30            | ~2,230                    | +2.0% - +3.0%
40            | ~2,260                    | +1.0% - +1.5%
50            | ~2,290                    | 0% (referans)
70            | ~2,330                    | -1.5% - -2.5%
100           | ~2,390                    | -3.5% - -5.0%
150           | ~2,460                    | -6.0% - -8.0%

Kural: Her 10 mbar vakum iyilestirmesi yaklasik %1-1.5 guc artisi saglar.
```

## Yas Buhar ve Baumann Kurali

### Yas Buhar Olusumu

Yogusmali turbinlerde buhar, genisleme sirasinda doyma egrisi altina inerek
yas buhar bolgesine girer. Bu, ozellikle son (LP) kademelerinde olur.

```
Yas buhar kalitesi:
x = (h - h_f) / h_fg

Burada:
- x = buhar kalitesi (dryness fraction) [0-1]
- h = gercek entalpi [kJ/kg]
- h_f = doymus sivi entalpisi [kJ/kg]
- h_fg = buharlasmma entalpisi [kJ/kg]

Tipik cikis kalitesi: x = 0.88 - 0.92
(Yani %8-12 nem icerigi)
```

### Baumann Kurali (Baumann Rule)

Yas buhar, turbin verimini dusurir. Baumann kurali bu kaybi tahmin eder:

```
eta_is_yas = eta_is_kuru x [1 - alpha x (1 - x_ort)]

Burada:
- eta_is_kuru = kuru buhar izentropik verimi
- alpha = Baumann faktoru (tipik 0.8 - 1.2, genellikle 1.0 alinir)
- x_ort = ortalama buhar kalitesi = (x_giris + x_cikis) / 2

Pratik kural: Her %1 nem artisi --> yaklasik %1 izentropik verim kaybi

Ornek:
Kuru buhar verimi: eta_is_kuru = %88
Cikis kalitesi: x_cikis = 0.88 (12% nem)
Giris kalitesi: x_giris = 1.0 (kuru)
x_ort = (1.0 + 0.88) / 2 = 0.94

eta_is_yas = 0.88 x [1 - 1.0 x (1 - 0.94)]
           = 0.88 x [1 - 0.06]
           = 0.88 x 0.94
           = 0.827 = %82.7

Verim kaybi = %88 - %82.7 = %5.3
```

### Nem Etkilerini Azaltma Yontemleri

| Yontem | Etki | Uygulama |
|--------|------|----------|
| Reheat (tekrar kizdinma) | Cikis nemini %3-5 azaltir | Buyuk santrallerde (>100 MW) |
| Moisture separator | Kademe arasi nem ayrimi | LP kademe girisinde |
| Yuksek giris sicakligi | Doyma egrisine gec ulasilir | Superkritik tasarim |
| Stellite kanat kaplama | Erozyon direnci arttirir | Son kademe kanatlari |
| Son kademe kanat tasarimi | Nem parcaciklarini yonlendirir | Ozel profil tasarimi |

## Exhaust Loss (Cikis Kinetik Enerji Kaybi)

### Tanimi ve Hesaplanmasi

```
Son kademe cikisinda buhar belirli bir hizda kondensere girer.
Bu kinetik enerji ise donusturulemez ve kaybolur.

Exhaust loss:
DH_exhaust = V_cikis^2 / (2 x 1000)   [kJ/kg]

V_cikis = m_dot x v_cikis / A_annulus   [m/s]

Burada:
- V_cikis = son kademe cikis hizi [m/s]
- m_dot = buhar kutle debisi [kg/s]
- v_cikis = spesifik hacim @ cikis kosullari [m3/kg]
- A_annulus = son kademe halka alani [m2]

Tipik degerler:
| Son Kademe Kanat Yuksekligi | V_cikis [m/s] | DH_exhaust [kJ/kg] |
|:---------------------------:|:-------------:|:-------------------:|
| Kisa (<0.5 m)              | 200 - 300     | 20 - 45             |
| Orta (0.5-0.9 m)           | 150 - 220     | 11 - 24             |
| Uzun (0.9-1.2 m)           | 100 - 170     | 5 - 14              |
| Cok uzun (>1.2 m)          | 80 - 140      | 3 - 10              |
```

### Exhaust Loss ve Yukleme Iliskisi

```
Kismi yukte exhaust loss degisimi:

Yuk [%]  | Hacimsel Akis [%] | V_cikis [%] | DH_exhaust [%]
100      | 100               | 100         | 100 (referans)
80       | 80                | 80          | 64
60       | 60                | 60          | 36
40       | 40                | 40          | 16
20       | 20                | 20          | 4

Not: Kismi yukte exhaust loss azalir (V^2 iliskisi).
Ancak kismi yukte kademe verimleri de duser; net etki
genellikle kismi yuk performansinin dusuk olmasidir.
```

## Vakum Optimizasyonu

### Kondenser Performans Parametreleri

```
Terminal Temperature Difference (TTD):
TTD = T_doyma - T_sogutma_cikis   [C]
Tipik: 3 - 8 C (dusuk TTD = iyi kondenser)

Kondenser Temizlik Faktoru (Cleanliness Factor):
CF = U_gercek / U_tasarim x 100   [%]
Tipik: %80 - 95 (yeni: %95, kirli: %70)

Kondenser Basinci:
P_kond = P_doyma(T_sogutma_giris + DT_sogutma + TTD)

Burada:
- T_sogutma_giris = sogutma suyu giris sicakligi [C]
- DT_sogutma = sogutma suyu sicaklik artisi [C] (tipik 5-12 C)
- TTD = terminal temperature difference [C]

Ornek:
T_sogutma_giris = 20 C, DT_sogutma = 8 C, TTD = 5 C
T_kond = 20 + 8 + 5 = 33 C
P_kond = P_doyma(33 C) = 0.050 bar = 50 mbar
```

### Sogutma Suyu Debisi

```
m_dot_sogutma = Q_kond / (Cp_su x DT_sogutma)

Burada:
- Q_kond = kondenser isi yukti [kW]
- Cp_su = suyun isil kapasitesi = 4.18 kJ/(kg.K)
- DT_sogutma = sogutma suyu sicaklik artisi [C]
```

## Son Kademe Kanat Boyutlandirma (Last-Stage Blade Sizing)

### Hacimsel Akis ve Kanat Yuksekligi

```
Cikis hacimsel akis:
V_dot_cikis = m_dot x v_cikis   [m3/s]

Burada v_cikis vakum basincindaki spesifik hacimdir:
- 0.05 bar'da: v = 28.2 m3/kg
- 0.07 bar'da: v = 20.5 m3/kg
- 0.10 bar'da: v = 14.7 m3/kg

Son kademe annulus alani:
A_annulus = V_dot_cikis / V_cikis_izinverilen   [m2]

Tipik izin verilen cikis hizi: V = 150-250 m/s

Kanat yuksekligi (uzunlugu):
L_kanat = A_annulus / (pi x D_orta)   [m]

Burada D_orta = son kademe orta capi [m]
```

### Son Kademe Boyut Siniflandirmasi

| Turbin Gucu [MW] | Son Kademe Kanat [mm] | Annulus Alani [m2] | 50 Hz / 3000 rpm |
|:-----------------:|:---------------------:|:------------------:|:----------------:|
| 5 - 20 | 250 - 500 | 0.3 - 1.5 | Tek akisli |
| 20 - 100 | 500 - 900 | 1.5 - 8.0 | Tek veya cift akisli |
| 100 - 300 | 700 - 1,100 | 5.0 - 20.0 | Cift akisli LP |
| 300 - 1,000 | 900 - 1,350 | 15.0 - 60.0 | 2-4 akisli LP |

## Exergy Analizi — Kondenserde Exergy Kaybi

### Kondenser Exergy Kaybi Hesabi

```
Kondenserde exergy kaybi iki bilesenden olusur:

1. Isi transfer tersinmezligi (temperature difference):
   I_kond = T0 x S_gen_kond
   S_gen_kond = m_dot x (s_kond - s_cikis) + Q_kond / T_sogutma_ort

2. Atilan isinin exergisi:
   Ex_atilan = Q_kond x (1 - T0 / T_kond)

Toplam:
Ex_kayip_kond = I_kond + Ex_atilan

Tipik kondenser exergy kaybi orani:
- Turbin giris exergisinin %5 - 15'i
- Yakit exergisinin %2 - 7'si

Not: Kondenserde atilan isi buyuktur (turbin giris enerjisinin ~%55-65'i),
ancak dusuk sicaklikta oldugu icin exergy icerigi dusuktur.
Bu, enerji analizi ile exergy analizi arasindaki temel farkdir.
```

### Ornek Exergy Hesaplamasi

```
Senaryo: 50 MW yogusmali turbin, 60 bar / 480 C giris, 0.05 bar cikis

Giris buhari:
  h_giris = 3,375 kJ/kg, s_giris = 6.850 kJ/(kg.K)
  ex_giris = (3,375 - 104.89) - 298.15 x (6.850 - 0.3674) = 1,337 kJ/kg

Cikis buhari (eta_is = 0.87):
  h_cikis,is = 2,115 kJ/kg
  h_cikis = 3,375 - 0.87 x (3,375 - 2,115) = 2,279 kJ/kg
  x_cikis = (2,279 - 137.8) / 2,423.7 = 0.884
  s_cikis = 0.476 + 0.884 x 7.919 = 7.478 kJ/(kg.K)
  ex_cikis = (2,279 - 104.89) - 298.15 x (7.478 - 0.3674) = 54 kJ/kg

Buhar debisi:
  m_dot = 50,000 / [(3,375 - 2,279) x 0.98 x 0.97] = 48.0 kg/s

Exergy dengesi:
  Ex_giris = 48.0 x 1,337 = 64,176 kW
  Ex_cikis = 48.0 x 54 = 2,592 kW
  W_turbin = 48.0 x 1,096 = 52,608 kW
  W_elek = 52,608 x 0.98 x 0.97 = 50,009 kW (kontrol)

  Ex_yikim_turbin = 64,176 - 2,592 - 52,608 = 8,976 kW

Turbin exergy verimi:
  eta_ex = 52,608 / (64,176 - 2,592) = 52,608 / 61,584 = %85.4

Kondenser exergy kaybi:
  Q_kond = 48.0 x (2,279 - 137.8) = 102,778 kW
  T_kond = 32.9 C = 306.05 K
  Ex_atilan = 102,778 x (1 - 298.15 / 306.05) = 2,652 kW
  Kondenser exergy kayip orani = 2,652 / 64,176 = %4.1
```

## Performans Tablosu

| Parametre | Kucuk (5-20 MW) | Orta (20-100 MW) | Buyuk (100+ MW) |
|-----------|:---------------:|:----------------:|:---------------:|
| Giris basinci [bar] | 40 - 60 | 60 - 170 | 170 - 300 |
| Giris sicakligi [C] | 400 - 480 | 480 - 540 | 540 - 600 |
| Cikis basinci [mbar] | 50 - 100 | 40 - 70 | 30 - 50 |
| Izentropik verim [%] | 75 - 85 | 82 - 90 | 88 - 93 |
| Elektrik verimi [%] | 30 - 35 | 35 - 39 | 39 - 42 |
| Exhaust loss [kJ/kg] | 15 - 30 | 8 - 18 | 4 - 12 |
| Reheat | Hayir | Bazen | Evet |

## Varsayilan Degerler (Olcum Yoksa)

| Parametre | Varsayilan | Aciklama |
|-----------|:---------:|----------|
| Giris basinci | 60 bar | Endustriyel yogusmali turbin |
| Giris sicakligi | 480 C | 60 bar'a uygun kizginlik |
| Cikis basinci | 0.06 bar | Sogutma kuleli tipik vakum |
| Izentropik verim | %85 | Orta olcekli turbin |
| Mekanik verim | %98 | Standart |
| Jenerator verimi | %97 | Standart |
| Sogutma suyu giris T | 22 C | Turkiye ortalama |
| Kondenser TTD | 5 C | Iyi bakimli kondenser |
| Yillik calisma saati | 7,500 saat/yil | Baz yuk santrali |

## İlgili Dosyalar

- [Turbin Formulleri](../formulas.md) -- Exergy hesaplamalari, Baumann kurali detayi
- [Benchmarklar](../benchmarks.md) -- Turbin verimlilik karsilastirma verileri
- [Karsi Basincli Turbin](back_pressure.md) -- CHP odakli turbin tipi
- [Cekisli Turbin](extraction.md) -- Esnek elektrik/isi dagitimi
- [Verim Iyilestirme](../solutions/efficiency_improvement.md) -- Performans iyilestirme onerileri
- [Bakim](../solutions/maintenance.md) -- Kanat bakimi, kondenser temizligi
- [Kazan Formulleri](../../boiler/formulas.md) -- Kazan verimi ve yakit exergy hesabi
- [Fabrika Kojenerasyon](../../factory/cogeneration.md) -- CHP ile karsilastirma

## Referanslar

1. Baumann, K. (1921). "Some recent developments in large steam turbine practice," *J. Institution of Electrical Engineers*, 59(302), 565-623.
2. Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
4. Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Ed., McGraw-Hill.
5. Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Ed., Wiley.
6. ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
7. Horlock, J.H. (1966). *Axial Flow Turbines*, Butterworths.
8. Leyzerovich, A.S. (2005). *Wet-Steam Turbines for Nuclear Power Plants*, PennWell.
9. Moran, M.J. et al. (2018). *Fundamentals of Engineering Thermodynamics*, 9th Ed., Wiley.
10. Regulagadda, P. et al. (2010). "Exergy analysis of a thermal power plant with measured boiler and turbine losses," *Applied Thermal Engineering*, 30, 970-976.
