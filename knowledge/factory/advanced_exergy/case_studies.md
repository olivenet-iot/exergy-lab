---
title: "Ileri Exergy Analizi Vaka Calismalari (Advanced Exergy Analysis Case Studies)"
category: factory
equipment_type: factory
keywords: [ileri exergy, vaka calismasi, kombine cevrim, sogutma sistemi, tekstil fabrikasi, 4-yollu dekompozisyon, kacinilabilir, kacinlamaz, endojen, ekzojen, IPN, avoidable, unavoidable, endogenous, exogenous, case study, combined cycle, refrigeration, textile]
related_files: [factory/advanced_exergy/overview.md, factory/advanced_exergy/four_way_splitting.md, factory/advanced_exergy/methodology.md, factory/advanced_exergy/avoidable_unavoidable.md, factory/advanced_exergy/endogenous_exogenous.md, factory/cross_equipment.md, factory/prioritization.md, factory/exergoeconomic/overview.md]
use_when: ["Ileri exergy analizinin gercek sistem uygulamalari incelenirken", "4-yollu dekompozisyon sonuclarinin yorumlanmasi gerektiginde", "Geleneksel ve ileri analiz karsilastirmasi yapilirken", "Yatirim onceliklendirmesi icin referans vaka aranidiginda", "ExergyLab kullanicilarina fabrika olceginde ornek sunulurken"]
priority: medium
last_updated: 2025-05-15
---
# Ileri Exergy Analizi Vaka Calismalari (Advanced Exergy Analysis Case Studies)

> Son guncelleme: 2025-05-15

## Genel Bakis

Bu dosya, ileri exergy analizinin (advanced exergy analysis) farkli endustriyel sistemlere uygulanmasini uc detayli vaka calismasi uzerinden sunmaktadir. Her vaka calismasi, geleneksel exergy analizinin yetersiz kaldigi noktalari ve 4-yollu dekompozisyonun (four-way splitting) yatirim kararlarini nasil degistirdigini somut verilerle gostermektedir.

Vaka calismalari su amaclara hizmet eder:
- Teorik kavramlarin gercek sistemlerdeki karsiligini gostermek
- Geleneksel ve ileri analiz sonuclarinin farkini kanitlamak
- ExergyLab kullanicilarinin kendi fabrikalarinda benzer analizleri yorumlamasina rehberlik etmek

## Vaka 1: Kombine Cevrim Santrali (Combined Cycle Power Plant)

**Kaynak:** Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012)

### 1.1 Sistem Tanimi

```
Sistem: Kombine cevrim guc santrali (Combined Cycle Power Plant, CCPP)
Konfigrasyon: Gaz turbini + HRSG (Heat Recovery Steam Generator) + Buhar turbini
Toplam elektrik gucu: ~400 MW

Gaz turbini alt sistemi:
  - Hava kompresoru (AC): Basinc orani 17:1
  - Yanma odasi (CC): Dogalgaz yakitli, TIT = 1,260 degC
  - Gaz turbini (GT): Izentropik verim ~%89

Buhar alt sistemi:
  - HRSG: Uc basincli (HP/IP/LP), yeniden isitmali (reheat)
  - Buhar turbini HP: Giris 120 bar / 560 degC
  - Buhar turbini IP: Giris 28 bar / 560 degC (reheat sonrasi)
  - Buhar turbini LP: Giris 4 bar / doymus buhar yakininda
  - Kondenser: Su sogutmali, 0.05 bar
  - Besleme suyu pompalari (FWP)

Bilesen sayisi: 12 ana bilesen (detayli analiz)
```

### 1.2 Geleneksel Exergy Analizi Sonuclari

```
Geleneksel analiz (I_total bazli):

Bilesen                | Ex_F [MW] | Ex_P [MW] | I_total [MW] | epsilon [%] | I/I_toplam [%]
-----------------------+-----------+-----------+--------------+-------------+----------------
Yanma odasi (CC)       |  620.0    |  452.0    |   168.0      |    72.9     |    62.0
HRSG                   |  245.0    |  213.0    |    32.0      |    86.9     |    11.8
Gaz turbini (GT)       |  180.0    |  155.0    |    25.0      |    86.1     |     9.2
Kondenser              |   24.0    |    9.0    |    15.0      |    37.5     |     5.5
Buhar turbini LP       |   35.0    |   23.0    |    12.0      |    65.7     |     4.4
Buhar turbini HP       |   52.0    |   44.0    |     8.0      |    84.6     |     3.0
Hava kompresoru (AC)   |   42.0    |   36.5    |     5.5      |    86.9     |     2.0
Buhar turbini IP       |   18.0    |   15.2    |     2.8      |    84.4     |     1.0
Besleme suyu pompalari |    2.5    |    2.0    |     0.5      |    80.0     |     0.2
Diger (vanalar, vb.)   |    —      |    —      |     2.2      |    —        |     0.8
-----------------------+-----------+-----------+--------------+-------------+----------------
TOPLAM                 |           |           |   271.0      |             |   100.0

Net guc cikisi: ~400 MW
Toplam exergetik verimlilik: ~%54
```

**Geleneksel analiz yorumu:**
Yanma odasi 168 MW ile toplam exergy yikiminin %62'sine sahiptir. Geleneksel yaklasim, tum dikkat ve yatirimin yanma odasina yonlendirilmesini onerir. HRSG ve gaz turbini ikinci ve ucuncu siradadir.

### 1.3 Ileri Exergy Analizi — Kacinilabilir / Kacinlamaz Ayirimi

```
Kacinlamaz kosullar (unavoidable conditions):
  - Hava kompresoru: eta_is = 0.93
  - Yanma odasi: Hava fazlasi %5, adyabatik, minimum sicaklik farki
  - Gaz turbini: eta_is = 0.96
  - HRSG: Delta_T_min = 3 degC, Delta_P/P = 0.01
  - Buhar turbinleri: eta_is = 0.93-0.95
  - Kondenser: Delta_T_min = 2 degC
  - Pompalar: eta = 0.92
```

### 1.4 Ileri Exergy Analizi — 4-Yollu Dekompozisyon Sonuclari

Asagidaki tablo, 6 ana bilesen icin tam 4-yollu dekompozisyon sonuclarini sunmaktadir:

| Bilesen | I_total [MW] | I_EN_AV [MW] | I_EN_UN [MW] | I_EX_AV [MW] | I_EX_UN [MW] | theta |
|---|---|---|---|---|---|---|
| Yanma odasi (CC) | 168.0 | 12.0 | 130.0 | 10.0 | 16.0 | 0.13 |
| Gaz turbini (GT) | 25.0 | 9.0 | 8.0 | 5.0 | 3.0 | 0.56 |
| HRSG | 32.0 | 8.0 | 15.0 | 6.0 | 3.0 | 0.44 |
| Buhar turbini HP | 8.0 | 3.0 | 3.0 | 1.2 | 0.8 | 0.53 |
| Buhar turbini LP | 12.0 | 5.0 | 4.0 | 1.8 | 1.2 | 0.57 |
| Kondenser | 15.0 | 4.0 | 7.0 | 2.5 | 1.5 | 0.43 |

```
Dogrulama ornekleri:
  Yanma odasi: 12.0 + 130.0 + 10.0 + 16.0 = 168.0 MW  checkmark
  Gaz turbini: 9.0 + 8.0 + 5.0 + 3.0 = 25.0 MW  checkmark
  HRSG: 8.0 + 15.0 + 6.0 + 3.0 = 32.0 MW  checkmark
  Buhar turbini HP: 3.0 + 3.0 + 1.2 + 0.8 = 8.0 MW  checkmark
  Buhar turbini LP: 5.0 + 4.0 + 1.8 + 1.2 = 12.0 MW  checkmark
  Kondenser: 4.0 + 7.0 + 2.5 + 1.5 = 15.0 MW  checkmark

Kacinilabilirlik oranlari (theta):
  theta_CC = (12.0 + 10.0) / 168.0 = 0.13  --> Cok dusuk!
  theta_GT = (9.0 + 5.0) / 25.0 = 0.56     --> Yuksek
  theta_HRSG = (8.0 + 6.0) / 32.0 = 0.44   --> Orta
  theta_ST_HP = (3.0 + 1.2) / 8.0 = 0.53   --> Yuksek
  theta_ST_LP = (5.0 + 1.8) / 12.0 = 0.57  --> Yuksek
  theta_kond = (4.0 + 2.5) / 15.0 = 0.43   --> Orta
```

### 1.5 Geleneksel vs. Ileri Siralama Karsilastirmasi

```
GELENEKSEL SIRALAMA (I_total bazli):
  1. Yanma odasi (CC):   168.0 MW (%62.0) --> "En buyuk kayip, oncelikli iyilestir!"
  2. HRSG:                32.0 MW (%11.8)
  3. Gaz turbini (GT):    25.0 MW  (%9.2)
  4. Kondenser:            15.0 MW  (%5.5)
  5. Buhar turbini LP:     12.0 MW  (%4.4)
  6. Buhar turbini HP:      8.0 MW  (%3.0)

ILERI SIRALAMA (I_EN_AV bazli — bilesen iyilestirme onceligi):
  1. Yanma odasi (CC):   12.0 MW  --> Hala buyuk, ama 168 MW'dan cok farkli!
  2. Gaz turbini (GT):    9.0 MW  --> Sirada YUKSELDI (gelenekselde 3. idi)
  3. HRSG:                 8.0 MW  --> Sabit
  4. Buhar turbini LP:     5.0 MW  --> Sirada YUKSELDI
  5. Kondenser:             4.0 MW
  6. Buhar turbini HP:      3.0 MW

ILERI SIRALAMA (theta bazli — iyilestirme verimliligi):
  1. Buhar turbini LP: theta = 0.57  --> En verimli yatirim hedefi!
  2. Gaz turbini (GT): theta = 0.56
  3. Buhar turbini HP: theta = 0.53
  4. HRSG:             theta = 0.44
  5. Kondenser:        theta = 0.43
  6. Yanma odasi (CC): theta = 0.13  --> EN DUSUK — gelenekselde 1. siraydaydi!

ILERI SIRALAMA (IP_real = I_EN_AV + I_EX_AV bazli — toplam potansiyel):
  1. Yanma odasi (CC): IP_real = 22.0 MW
  2. HRSG:             IP_real = 14.0 MW
  3. Gaz turbini (GT): IP_real = 14.0 MW
  4. Buhar turbini LP: IP_real = 6.8 MW
  5. Kondenser:        IP_real = 6.5 MW
  6. Buhar turbini HP: IP_real = 4.2 MW
```

### 1.6 Kritik Bulgular ve Dersler

```
Ders 1 — Yanma odasi yanilticidir:
  Yanma odasinin toplam exergy yikimi 168 MW ile cok buyuktur, ancak
  theta = 0.13 ile kacinilabilir payi sadece %13'tur. Yikimin %77'si
  (130 MW) endojen-kacinlamaz — metan yanma reaksiyonunun termodinamik
  dogasi geregi var olan tersinmezliktir. Hicbir muhendislik onlemi
  bu kaybi ortadan kaldiramaz.

Ders 2 — Yatirim onceligi yanma odasindan ekspandere kayar:
  Geleneksel analiz: "Yanma odasina yatirim yap" (168 MW)
  Ileri analiz: "Gaz turbinine yatirim yap" (theta = 0.56, I_EN_AV = 9 MW)
  Gaz turbininin izentropik veriminin %89'dan %92'ye cikarilmasi,
  yanma odasinda yapilabilecek herhangi bir iyilestirmeden daha
  maliyet-etkin sonuc verir.

Ders 3 — Buhar turbinleri gizli firsatlardir:
  LP buhar turbini geleneksel analizde 5. sirada (%4.4) gorunur —
  cok kucuk. Ancak theta = 0.57 ile kacinilabilirlik orani en yuksektir.
  Turbine blade (kanatcik) yenileme veya seal (conta) iyilestirme
  maliyeti dusuk, geri donus yuksektir.

Ders 4 — Sistem etkilesimleri (eksojen bilesenler):
  HRSG'nin I_EX_AV = 6.0 MW degeri onemlidir. Bu, gaz turbini ve
  kompresordeki iyilestirmelerin HRSG'deki kaybi da azaltacagi anlamina
  gelir. Bireysel bilesen iyilestirmelerinin dolayli faydalari vardir.

Ders 5 — Ekonomik onceliklendirme:
  Elektrik fiyati c_elek = 0.08 EUR/kWh ile yillik potansiyel (7,500 h):
  GT iyilestirmesi:   9.0 MW x 0.08 x 7,500 = 5,400,000 EUR/yil
  CC iyilestirmesi:  12.0 MW x 0.08 x 7,500 = 7,200,000 EUR/yil
  HRSG iyilestirmesi:  8.0 MW x 0.08 x 7,500 = 4,800,000 EUR/yil

  Ancak GT iyilestirme maliyeti CC'den cok daha dusuktur:
  GT blade yenileme: ~2,000,000 EUR --> SPP = 0.37 yil
  CC yakin tasarimi: ~15,000,000 EUR --> SPP = 2.08 yil
  HRSG finli boru:   ~3,500,000 EUR --> SPP = 0.73 yil
```

## Vaka 2: Endustriyel Sogutma Sistemi (Industrial Refrigeration System)

**Kaynak:** Morosuk, T. & Tsatsaronis, G. (2011)

### 2.1 Sistem Tanimi

```
Sistem: 2 kademeli buhar sikistirmali sogutma cevrimi
         (Two-stage vapor compression refrigeration system)
Sogutma kapasitesi: 500 kW
Sogutkan: R-134a (1,1,1,2-Tetrafloroetan)
Evaporator sicakligi: -10 degC
Kondenser sicakligi: +40 degC

Bilesenler:
  1. LP kompresor (LP-C): Dusuk basinc kademe kompresoru
     eta_is = 0.72, basinc orani = 3.2:1
  2. HP kompresor (HP-C): Yuksek basinc kademe kompresoru
     eta_is = 0.78, basinc orani = 2.8:1
  3. Kondenser (COND): Hava sogutmali
     Delta_T_yaklasim = 8 degC
  4. Evaporator (EVAP): Basincsiz glikon dongusu ile sogutma
     Delta_T_yaklasim = 5 degC
  5. HP genlesme vanasi (HP-EV): Yuksek basinc genlesme
  6. LP genlesme vanasi (LP-EV): Dusuk basinc genlesme

Ara basinc: ~4.5 bar (geometrik ortalama)
Flash tank ile fazlar ayrilir
COP_gercek = 2.35
COP_ideal (Carnot) = T_evap / (T_kond - T_evap) = 263 / 50 = 5.26
Exergetik verimlilik: epsilon = COP / COP_Carnot = 2.35 / 5.26 = 0.447 = %44.7
```

### 2.2 Geleneksel Exergy Analizi Sonuclari

```
Bilesen           | Ex_F [kW] | Ex_P [kW] | I_total [kW] | epsilon [%] | I/I_toplam [%]
------------------+-----------+-----------+--------------+-------------+----------------
LP kompresor      |  122.0    |   97.5    |    24.5      |    79.9     |    20.7
HP kompresor      |   90.5    |   76.0    |    14.5      |    84.0     |    12.2
Kondenser         |   82.0    |   55.0    |    27.0      |    67.1     |    22.8
Evaporator        |   48.0    |   35.0    |    13.0      |    72.9     |    11.0
HP genlesme vanasi|   32.0    |   12.5    |    19.5      |    39.1     |    16.5
LP genlesme vanasi|   28.0    |    8.0    |    20.0      |    28.6     |    16.9
------------------+-----------+-----------+--------------+-------------+----------------
TOPLAM            |           |           |   118.5      |             |   100.0

Toplam kompresur gucu: W_komp = 122.0 + 90.5 = 212.5 kW
COP = 500 / 212.5 = 2.35

Geleneksel siralama (I_total):
  1. Kondenser:          27.0 kW (%22.8)
  2. LP genlesme vanasi: 20.0 kW (%16.9)
  3. HP genlesme vanasi: 19.5 kW (%16.5)
  4. LP kompresur:       24.5 kW (%20.7)
  5. HP kompresur:       14.5 kW (%12.2)
  6. Evaporator:         13.0 kW (%11.0)
```

**Geleneksel analiz yorumu:**
Kondenser ve genlesme vanalari en yuksek exergy yikimlarina sahiptir. Geleneksel yaklasim, kondenserin ve genlesme vanalarinin iyilestirilmesine yonelik yatirim onerir.

### 2.3 Kacinlamaz Kosullar

```
Kacinlamaz (unavoidable) kosullar:
  - LP kompresur:       eta_is = 0.92
  - HP kompresur:       eta_is = 0.92
  - Kondenser:          Delta_T_min = 2 degC, Delta_P/P = 0.005
  - Evaporator:         Delta_T_min = 2 degC, Delta_P/P = 0.005
  - HP genlesme vanasi: Izentalpik genlesme (termodinamik sinir)
  - LP genlesme vanasi: Izentalpik genlesme (termodinamik sinir)

Not: Genlesme vanalari icin kacinlamaz kosul = izentalpik genlesme.
Izentropik genlesme (turbo-ekspander) teknolojik olarak mumkun
ancak standart sogutma sistemlerinde kullanilmaz.
Bu analizde genlesme vanasinin kacinlamaz yikimi, izentalpik
genlesmenin termodinamik dogasindan kaynaklanir.
```

### 2.4 Ileri Exergy Analizi — 4-Yollu Dekompozisyon

| Bilesen | I_total [kW] | I_EN_AV [kW] | I_EN_UN [kW] | I_EX_AV [kW] | I_EX_UN [kW] | theta |
|---|---|---|---|---|---|---|
| LP kompresor (LP-C) | 24.5 | 8.2 | 10.5 | 3.8 | 2.0 | 0.49 |
| HP kompresor (HP-C) | 14.5 | 5.1 | 5.8 | 2.4 | 1.2 | 0.52 |
| Kondenser (COND) | 27.0 | 5.5 | 12.0 | 5.2 | 4.3 | 0.40 |
| Evaporator (EVAP) | 13.0 | 3.0 | 5.5 | 2.8 | 1.7 | 0.45 |
| HP genlesme vanasi (HP-EV) | 19.5 | 1.2 | 15.8 | 1.5 | 1.0 | 0.14 |
| LP genlesme vanasi (LP-EV) | 20.0 | 1.0 | 17.0 | 1.2 | 0.8 | 0.11 |

```
Dogrulama:
  LP-C:  8.2 + 10.5 + 3.8 + 2.0 = 24.5 kW  checkmark
  HP-C:  5.1 + 5.8 + 2.4 + 1.2 = 14.5 kW  checkmark
  COND:  5.5 + 12.0 + 5.2 + 4.3 = 27.0 kW  checkmark
  EVAP:  3.0 + 5.5 + 2.8 + 1.7 = 13.0 kW  checkmark
  HP-EV: 1.2 + 15.8 + 1.5 + 1.0 = 19.5 kW  checkmark
  LP-EV: 1.0 + 17.0 + 1.2 + 0.8 = 20.0 kW  checkmark

Kacinilabilirlik oranlari (theta):
  theta_LP-C  = (8.2 + 3.8) / 24.5 = 0.49
  theta_HP-C  = (5.1 + 2.4) / 14.5 = 0.52
  theta_COND  = (5.5 + 5.2) / 27.0 = 0.40
  theta_EVAP  = (3.0 + 2.8) / 13.0 = 0.45
  theta_HP-EV = (1.2 + 1.5) / 19.5 = 0.14
  theta_LP-EV = (1.0 + 1.2) / 20.0 = 0.11
```

### 2.5 Geleneksel vs. Ileri Siralama Karsilastirmasi

```
GELENEKSEL SIRALAMA (I_total):
  1. Kondenser:          27.0 kW --> "Kondenseri iyilestir!"
  2. LP kompresur:       24.5 kW
  3. LP genlesme vanasi: 20.0 kW --> "Genlesme vanasi buyuk kayip!"
  4. HP genlesme vanasi: 19.5 kW
  5. HP kompresur:       14.5 kW
  6. Evaporator:         13.0 kW

ILERI SIRALAMA (I_EN_AV bazli — bilesen iyilestirme onceligi):
  1. LP kompresur:        8.2 kW --> Birinci oncelik!
  2. Kondenser:           5.5 kW
  3. HP kompresur:        5.1 kW
  4. Evaporator:          3.0 kW
  5. HP genlesme vanasi:  1.2 kW --> Gelenekselde 4. idi, simdi 5.!
  6. LP genlesme vanasi:  1.0 kW --> Gelenekselde 3. idi, simdi 6.!

ILERI SIRALAMA (theta bazli):
  1. HP kompresur:  theta = 0.52 --> En verimli yatirim!
  2. LP kompresur:  theta = 0.49
  3. Evaporator:    theta = 0.45
  4. Kondenser:     theta = 0.40
  5. HP genlesme:   theta = 0.14 --> Cok dusuk — yatirim anlamsiz
  6. LP genlesme:   theta = 0.11 --> En dusuk — yatirim anlamsiz
```

### 2.6 Genlesme Vanasi Retrofit Karsilastirmasi

```
Konvansiyonel sonuc genlesme vanalarini onceliklendirirdi.
Ileri analiz gosteriyor ki genlesme vanalarinin theta degeri
cok dusuktur (0.11-0.14). Peki retrofit seenekleri nelerdir?

Secenek A — Ejektor (Ejector) Retrofit:
  Genlesme vanasi yerine ejektor kullanarak genlesme isinden
  kismen yararlanma.
  - LP genlesme vanasi yerine ejektor: I_AV = 2.2 kW kazanim
  - Ejektor verimi: ~%15-25 (izentropik)
  - Maliyet: ~8,000-12,000 EUR
  - Yillik tasarruf: 2.2 kW x 0.12 EUR/kWh x 6,000 h = 1,584 EUR/yil
  - SPP = 10,000 / 1,584 = 6.3 yil
  - Degerlendirme: Ekonomik degil

Secenek B — Turbo-ekspander Retrofit:
  Genlesme vanasi yerine turbo-ekspander ile is geri kazanimi.
  - LP genlesme vanasi yerine turbo-ekspander: I_AV = 2.2 kW kazanim
  - Turbo-ekspander verimi: ~%50-60 (izentropik)
  - Geri kazanilan is: ~1.5 kW (kompresure mekanik destek)
  - Maliyet: ~25,000-40,000 EUR
  - Yillik tasarruf: (2.2 + 1.5) kW x 0.12 x 6,000 = 2,664 EUR/yil
  - SPP = 32,500 / 2,664 = 12.2 yil
  - Degerlendirme: Ekonomik degil

Secenek C — Kompresur Verim Iyilestirme (Ileri Analizin Onerisi):
  HP kompresur izentropik verimini 0.78 --> 0.85'e cikarmak.
  - I_EN_AV kazanim: ~3.5 kW dogrudan + 1.5 kW dolayli (I_EX azalma)
  - Yontem: Yeni nesil vidalay kompresur veya VSD ekleme
  - Maliyet: ~15,000 EUR
  - Yillik tasarruf: 5.0 kW x 0.12 x 6,000 = 3,600 EUR/yil
  - SPP = 15,000 / 3,600 = 4.2 yil
  - Degerlendirme: Makul (ve ek dolayli faydalar var)

Sonuc: Genlesme vanasi retrofit'i ekonomik degildir.
Ileri analiz, kompresur iyilestirmesinin cok daha degerli
oldugunu ortaya koymustur.
```

### 2.7 Dersler ve Cikarimlar

```
Ders 1 — Genlesme vanalari yanilticidir:
  Geleneksel analizde genlesme vanalari toplam yikimin %33.4'une
  (19.5 + 20.0 = 39.5 kW) sahiptir. Ancak theta degerleri 0.11-0.14
  ile kacinilabilir paylari cok dusuktur. Genlesme isleminin
  termodinamik dogasi geregi (izentalpik genlesme) kayip kacinlamazdir.

Ders 2 — Kompresurler asil firsattir:
  HP kompresur theta = 0.52 ve LP kompresur theta = 0.49 ile
  en yuksek iyilestirme verimliligine sahiptir. Izentropik verim
  artisi hem dogrudan (I_EN_AV) hem de dolayli (I_EX_AV azalma)
  fayda saglar.

Ders 3 — Sistem etklesimi onemlidir:
  Kondenserin I_EX_AV = 5.2 kW degeri, I_EN_AV = 5.5 kW'a
  yakindir. Bu, kompresur ve evaporatordeki iyilestirmelerin
  kondenser kaybini da azaltacagi anlamina gelir. Kondensere
  dogrudan yatirim yerine, kompresur iyilestirmesinin dolayli
  faydasi tercih edilebilir.

Ders 4 — COP iyilestirme potansiyeli:
  Toplam kacinilabilir exergy yikimi:
  I_AV_toplam = 12.0 + 7.5 + 10.7 + 5.8 + 2.7 + 2.2 = 40.9 kW
  Mevcut W_komp = 212.5 kW, COP = 2.35
  Potansiyel W_komp = 212.5 - 40.9 = 171.6 kW
  Potansiyel COP = 500 / 171.6 = 2.91
  COP iyilesmesi: %23.8 (2.35 --> 2.91)
```

## Vaka 3: ExergyLab Ozel — Tekstil Fabrikasi (5 Bilesen)

**Bu vaka calismasi, ExergyLab kullanicilari icin ozel olarak hazirlanmis cozumlu bir ornektir.**

### 3.1 Sistem Tanimi

```
Sistem: Orta olcekli tekstil fabrikasi (boyahane)
Sektor: Tekstil — boyama, yikama, kurutma prosesleri

Bilesenler:
  1. Kazan: Dogalgaz yakitli ates borulu buhar kazani
     - Kapasite: 6 ton/h doymus buhar @ 10 bar (180 degC)
     - Termal verim: eta_termal = 0.86
     - Baca gazi sicakligi: 210 degC
     - Hava fazlasi: %25
     - Calisma suresi: 6,500 saat/yil
     - Ekonomizer: Yok

  2. Kompresor: Vidali hava kompresuru
     - Nominal guc: 55 kW
     - Izentropik verim: eta_is = 0.70
     - Basinc: 7 bar
     - Sogutma: Su sogutmali
     - Ortalama yuk: %80
     - Calisma suresi: 6,000 saat/yil

  3. Chiller: Su sogutmali vidalay chiller
     - Sogutma kapasitesi: 200 kW
     - COP: 3.8 (tasarim), 3.2 (gercek — fouling, yaslanma)
     - Sogutkan: R-134a
     - Chilled water: 7/12 degC
     - Calisma suresi: 5,500 saat/yil

  4. Pompa 1: Sogutma suyu sirkuasyon pompasi
     - Nominal guc: 15 kW
     - Pompa verimi: eta_pompa = 0.62
     - Motor verimi: eta_motor = 0.91
     - Kontrol: Kisma vanasi ile debi kontrolu
     - Ortalama yuk: %65 (kismali)
     - Calisma suresi: 6,500 saat/yil

  5. Pompa 2: Proses suyu pompasi (VSD mevcut)
     - Nominal guc: 7.5 kW
     - Pompa verimi: eta_pompa = 0.75
     - Motor verimi: eta_motor = 0.92
     - Kontrol: VSD (degisken hiz surucu)
     - Ortalama yuk: %70
     - Calisma suresi: 6,000 saat/yil

Enerji maliyetleri:
  - Dogalgaz: 0.045 EUR/kWh (alt isil deger bazinda)
  - Elektrik: 0.12 EUR/kWh
```

### 3.2 Geleneksel Exergy Analizi Sonuclari

```
Her bilesen icin geleneksel exergy analizi:

Kazan:
  Yakit exergysi: Ex_F = m_yakit x ex_yakit = 2,420 kW
  Urun exergysi (buhar): Ex_P = m_buhar x (ex_buhar - ex_su)
    = (6,000/3,600) x (748 - 3.2) = 1,241 kW
  I_total,kazan = 2,420 - 1,241 = 1,179 kW
  epsilon_kazan = 1,241 / 2,420 = 0.513 = %51.3

Kompresor:
  W_gercek = 55 x 0.80 = 44 kW (gucun %80'i kullaniliyor)
  W_izentropik = 44 x 0.70 = 30.8 kW
  I_total,komp = 44 - 30.8 = 13.2 kW
  epsilon_komp = 30.8 / 44 = 0.70 = %70.0

Chiller:
  W_komp = Q_sogutma / COP = 200 / 3.2 = 62.5 kW
  Ex_sogutma = Q_sogutma x |1 - T_0/T_evap|
             = 200 x |1 - 298/278| = 200 x 0.072 = 14.4 kW
  I_total,chiller = 62.5 - 14.4 = 48.1 kW
  epsilon_chiller = 14.4 / 62.5 = 0.230 = %23.0

Pompa 1 (kisma vanali):
  W_gercek = 15 x 0.65 = 9.75 kW (kismali calisma)
  W_ideal = 15 x 0.65 x 0.62 x 0.91 x (1 - 0.35) = 3.58 kW
  I_total,pompa1 = 9.75 - 3.58 = 6.17 kW
  epsilon_pompa1 = 3.58 / 9.75 = 0.367 = %36.7

Pompa 2 (VSD):
  W_gercek = 7.5 x (0.70)^3 = 7.5 x 0.343 = 2.57 kW (VSD ile)
  W_ideal = 7.5 x 0.343 x 0.75 x 0.92 = 1.77 kW
  I_total,pompa2 = 2.57 - 1.77 = 0.80 kW
  epsilon_pompa2 = 1.77 / 2.57 = 0.689 = %68.9

GELENEKSEL OZET TABLOSU:

Bilesen     | I_total [kW] | epsilon [%] | I/I_toplam [%]
------------+-------------+-------------+----------------
Kazan       |  1,179.0    |    51.3     |    92.5
Chiller     |     48.1    |    23.0     |     3.8
Kompresor   |     13.2    |    70.0     |     1.0
Pompa 1     |      6.17   |    36.7     |     0.5
Pompa 2     |      0.80   |    68.9     |     0.1
TOPLAM      |  1,247.3    |     —       |   100.0*
* Yuvarlamadan dolayi tam %100 olmayabilir
```

**Geleneksel analiz yorumu:**
Kazan toplam exergy yikiminin %92.5'ine sahiptir. Geleneksel yaklasim, tum dikkatin kazana yonlendirilmesini onerir. Diger bilesenler ihmal edilebilir gorunur.

### 3.3 Kacinlamaz Kosullar Tanimi

```
Her bilesen icin kacinlamaz (BAT - Best Available Technology) kosullar:

Kazan:
  - eta_termal = 0.96 (kondansasyon kazani)
  - Baca gazi T = 55 degC (kondansasyonlu)
  - Hava fazlasi = %5 (O2 trim kontrol)
  - Yanma tersinmezligi: CH4 + 2O2 --> CO2 + 2H2O (kacinlamaz)

Kompresor:
  - eta_is = 0.92 (en iyi mevcut vidali kompresur)
  - Mekanik kayip: %2 (minimum)
  - VSD ile tam yuk eslesme

Chiller:
  - COP = 5.5 (en iyi mevcut vidalay chiller, R-134a, ayni kosullar)
  - Temiz kondenser, optimal sarj
  - Minimum superheat, minimum subcooling

Pompa 1:
  - eta_pompa = 0.88 (en iyi santrifuj pompa)
  - eta_motor = 0.96 (IE4 premium motor)
  - VSD ile kontrol (kisma vanasi yok)

Pompa 2:
  - eta_pompa = 0.88 (en iyi santrifuj pompa)
  - eta_motor = 0.96
  - VSD mevcut (zaten iyi)
```

### 3.4 4-Yollu Dekompozisyon Sonuclari

```
Hibrit ve kacinlamaz cevrim simulasyonlari sonuclari:

KAZAN:
  I_total = 1,179.0 kW
  Hibrit cevrim (kazan gercek, digerler ideal):
    I_EN = 1,085.0 kW   |   I_EX = 94.0 kW
  Kacinlamaz cevrim:
    I_UN = 988.0 kW      |   I_AV = 191.0 kW
  Hibrit + kacinlamaz:
    I_EN_UN = 920.0 kW

  4 bilesen:
    I_EN_AV = 1,085.0 - 920.0 = 165.0 kW
    I_EN_UN = 920.0 kW
    I_EX_UN = 988.0 - 920.0 = 68.0 kW
    I_EX_AV = 94.0 - 68.0 = 26.0 kW
    TOPLAM = 165.0 + 920.0 + 26.0 + 68.0 = 1,179.0 kW  checkmark
    theta_kazan = (165.0 + 26.0) / 1,179.0 = 0.16

KOMPRESOR:
  I_total = 13.2 kW
  Hibrit cevrim:
    I_EN = 11.0 kW   |   I_EX = 2.2 kW
  Kacinlamaz cevrim:
    I_UN = 5.8 kW    |   I_AV = 7.4 kW
  Hibrit + kacinlamaz:
    I_EN_UN = 4.6 kW

  4 bilesen:
    I_EN_AV = 11.0 - 4.6 = 6.4 kW
    I_EN_UN = 4.6 kW
    I_EX_UN = 5.8 - 4.6 = 1.2 kW
    I_EX_AV = 2.2 - 1.2 = 1.0 kW
    TOPLAM = 6.4 + 4.6 + 1.0 + 1.2 = 13.2 kW  checkmark
    theta_komp = (6.4 + 1.0) / 13.2 = 0.56

CHILLER:
  I_total = 48.1 kW
  Hibrit cevrim:
    I_EN = 38.0 kW   |   I_EX = 10.1 kW
  Kacinlamaz cevrim:
    I_UN = 22.5 kW   |   I_AV = 25.6 kW
  Hibrit + kacinlamaz:
    I_EN_UN = 17.0 kW

  4 bilesen:
    I_EN_AV = 38.0 - 17.0 = 21.0 kW
    I_EN_UN = 17.0 kW
    I_EX_UN = 22.5 - 17.0 = 5.5 kW
    I_EX_AV = 10.1 - 5.5 = 4.6 kW
    TOPLAM = 21.0 + 17.0 + 4.6 + 5.5 = 48.1 kW  checkmark
    theta_chiller = (21.0 + 4.6) / 48.1 = 0.53

POMPA 1 (kisma vanali):
  I_total = 6.17 kW
  Hibrit cevrim:
    I_EN = 5.10 kW   |   I_EX = 1.07 kW
  Kacinlamaz cevrim:
    I_UN = 1.62 kW   |   I_AV = 4.55 kW
  Hibrit + kacinlamaz:
    I_EN_UN = 1.25 kW

  4 bilesen:
    I_EN_AV = 5.10 - 1.25 = 3.85 kW
    I_EN_UN = 1.25 kW
    I_EX_UN = 1.62 - 1.25 = 0.37 kW
    I_EX_AV = 1.07 - 0.37 = 0.70 kW
    TOPLAM = 3.85 + 1.25 + 0.70 + 0.37 = 6.17 kW  checkmark
    theta_pompa1 = (3.85 + 0.70) / 6.17 = 0.74

POMPA 2 (VSD):
  I_total = 0.80 kW
  Hibrit cevrim:
    I_EN = 0.68 kW   |   I_EX = 0.12 kW
  Kacinlamaz cevrim:
    I_UN = 0.52 kW   |   I_AV = 0.28 kW
  Hibrit + kacinlamaz:
    I_EN_UN = 0.45 kW

  4 bilesen:
    I_EN_AV = 0.68 - 0.45 = 0.23 kW
    I_EN_UN = 0.45 kW
    I_EX_UN = 0.52 - 0.45 = 0.07 kW
    I_EX_AV = 0.12 - 0.07 = 0.05 kW
    TOPLAM = 0.23 + 0.45 + 0.05 + 0.07 = 0.80 kW  checkmark
    theta_pompa2 = (0.23 + 0.05) / 0.80 = 0.35
```

### 3.5 Ozet Tablosu — 4-Yollu Sonuclar

| Bilesen | I_total [kW] | I_EN_AV [kW] | I_EN_UN [kW] | I_EX_AV [kW] | I_EX_UN [kW] | theta | IP_real [kW] |
|---|---|---|---|---|---|---|---|
| Kazan | 1,179.0 | 165.0 | 920.0 | 26.0 | 68.0 | 0.16 | 191.0 |
| Chiller | 48.1 | 21.0 | 17.0 | 4.6 | 5.5 | 0.53 | 25.6 |
| Kompresor | 13.2 | 6.4 | 4.6 | 1.0 | 1.2 | 0.56 | 7.4 |
| Pompa 1 | 6.17 | 3.85 | 1.25 | 0.70 | 0.37 | 0.74 | 4.55 |
| Pompa 2 | 0.80 | 0.23 | 0.45 | 0.05 | 0.07 | 0.35 | 0.28 |
| **TOPLAM** | **1,247.3** | **196.5** | **943.3** | **32.4** | **75.1** | — | **228.8** |

```
Fabrika toplam kacinilabilirlik orani:
  theta_fabrika = (196.5 + 32.4) / 1,247.3 = 228.8 / 1,247.3 = 0.183

Yorum: Fabrikanin toplam exergy yikiminin yalnizca %18.3'u
kacinilabilir niteliktedir. Geri kalan %81.7'si termodinamik
sinirlar (ozellikle yanma) nedeniyle kacinlamazdir.
```

### 3.6 Geleneksel vs. Ileri Siralama Karsilastirmasi

```
GELENEKSEL SIRALAMA (I_total bazli):
  Sira | Bilesen    | I_total [kW] | I/I_toplam [%]
  -----+------------+-------------+----------------
    1  | Kazan      |  1,179.0    |    94.5      --> "Kazana yatirim yap!"
    2  | Chiller    |     48.1    |     3.9
    3  | Kompresor  |     13.2    |     1.1
    4  | Pompa 1    |      6.17   |     0.5
    5  | Pompa 2    |      0.80   |     0.1

ILERI SIRALAMA (I_EN_AV bazli — dogrudan iyilestirme onceligi):
  Sira | Bilesen    | I_EN_AV [kW] | Aksiyon
  -----+------------+--------------+------------------------------------------
    1  | Kazan      |  165.0       | Ekonomizer + O2 trim + yanma ayari
    2  | Chiller    |   21.0       | Kondenser temizligi + sogutkan optimizasyonu
    3  | Kompresor  |    6.4       | VSD ekleme + basinc optimizasyonu
    4  | Pompa 1    |    3.85      | VSD ile kisma vanasi degistirme
    5  | Pompa 2    |    0.23      | Zaten iyi — dusuk oncelik

ILERI SIRALAMA (theta bazli — yatirim verimliligi):
  Sira | Bilesen    | theta | Degerlendirme
  -----+------------+-------+--------------------------------
    1  | Pompa 1    | 0.74  | Cok yuksek — VSD ile buyuk iyilesme
    2  | Kompresor  | 0.56  | Yuksek — verim artisi efektif
    3  | Chiller    | 0.53  | Yuksek — bakim ve optimizasyon
    4  | Pompa 2    | 0.35  | Orta — zaten VSD var, sinirli
    5  | Kazan      | 0.16  | Dusuk — yanma kacinlamaz
```

### 3.7 IPN Hesabi ve Yatirim Onceliklendirme

```
IPN (Improvement Priority Number) Hesabi:

Yakit exergy birim maliyetleri:
  c_F,kazan    = 0.045 EUR/kWh (dogalgaz)
  c_F,komp     = 0.12 EUR/kWh  (elektrik)
  c_F,chiller  = 0.12 EUR/kWh  (elektrik)
  c_F,pompa1   = 0.12 EUR/kWh  (elektrik)
  c_F,pompa2   = 0.12 EUR/kWh  (elektrik)

Kacinilabilir exergy yikimi yillik maliyetleri:

  Kazan:
    C_AV = I_AV x c_F x t = 191.0 x 0.045 x 6,500 = 55,868 EUR/yil

  Chiller:
    C_AV = I_AV x c_F x t = 25.6 x 0.12 x 5,500 = 16,896 EUR/yil

  Kompresor:
    C_AV = I_AV x c_F x t = 7.4 x 0.12 x 6,000 = 5,328 EUR/yil

  Pompa 1:
    C_AV = I_AV x c_F x t = 4.55 x 0.12 x 6,500 = 3,549 EUR/yil

  Pompa 2:
    C_AV = I_AV x c_F x t = 0.28 x 0.12 x 6,000 = 202 EUR/yil

  TOPLAM C_AV = 81,843 EUR/yil

IPN degerleri:
  IPN_kazan   = 55,868 / 81,843 = 0.682
  IPN_chiller = 16,896 / 81,843 = 0.206
  IPN_komp    =  5,328 / 81,843 = 0.065
  IPN_pompa1  =  3,549 / 81,843 = 0.043
  IPN_pompa2  =    202 / 81,843 = 0.002
  ─────────────────────────────────────
  TOPLAM                         = 1.000  checkmark
```

**IPN Sonuc Tablosu:**

| Bilesen | I_AV [kW] | c_F [EUR/kWh] | t [h/yil] | C_AV [EUR/yil] | IPN | theta | Oncelik |
|---|---|---|---|---|---|---|---|
| Kazan | 191.0 | 0.045 | 6,500 | 55,868 | 0.682 | 0.16 | 1 (IPN) |
| Chiller | 25.6 | 0.12 | 5,500 | 16,896 | 0.206 | 0.53 | 2 |
| Kompresor | 7.4 | 0.12 | 6,000 | 5,328 | 0.065 | 0.56 | 3 |
| Pompa 1 | 4.55 | 0.12 | 6,500 | 3,549 | 0.043 | 0.74 | 4 |
| Pompa 2 | 0.28 | 0.12 | 6,000 | 202 | 0.002 | 0.35 | 5 |

### 3.8 Detayli Yatirim Plani ve Tasarruf Hesabi

```
Proje 1 — Kazan Ekonomizer Ekleme (I_EN_AV hedefli):
  Hedef: Baca gazi sicakligini 210 degC --> 130 degC'ye dusurmek
  Geri kazanilan isi: Q_eco = 95 kW (asidik cig noktasi limiti)
  Kacinilabilir exergy kazanimi: ~85 kW (I_EN_AV'nin %52'si)
  Yakit tasarrufu: 95 / 0.86 = 110.5 kW yakit
  Yillik tasarruf: 110.5 x 0.045 x 6,500 = 32,321 EUR/yil
  Yatirim: 22,000 EUR (paslanmaz ekonomizer + boru + montaj)
  SPP = 22,000 / 32,321 = 0.68 yil (8.2 ay)

Proje 2 — Kazan O2 Trim Kontrol Sistemi:
  Hedef: Hava fazlasini %25 --> %8'e dusurmek
  Baca gazi kaybi azalmasi: ~35 kW yakit tasarrufu
  Kacinilabilir exergy kazanimi: ~45 kW
  Yillik tasarruf: 35 x 0.045 x 6,500 = 10,238 EUR/yil
  Yatirim: 8,500 EUR (O2 analizoru + kontrol vanasi + PLC)
  SPP = 8,500 / 10,238 = 0.83 yil (10 ay)

Proje 3 — Chiller Kondenser Temizligi + Sogutkan Optimizasyonu:
  Hedef: COP'u 3.2 --> 4.2'ye cikmak (tasarim degerine yaklasma)
  Guc azalmasi: 200/3.2 - 200/4.2 = 62.5 - 47.6 = 14.9 kW
  Kacinilabilir exergy kazanimi: ~12 kW (I_EN_AV'nin %57'si)
  Yillik tasarruf: 14.9 x 0.12 x 5,500 = 9,834 EUR/yil
  Yatirim: 4,500 EUR (kondenser temizligi + sogutkan sarji + bakim)
  SPP = 4,500 / 9,834 = 0.46 yil (5.5 ay)

Proje 4 — Kompresor VSD Ekleme:
  Hedef: Kismi yuk verimliligini artirma
  Mevcut: 55 kW x 0.80 = 44 kW ortalama tuketim
  VSD ile: Tam yuk eslesmeli, kayip azalmasi ~5.5 kW
  Kacinilabilir exergy kazanimi: ~5 kW
  Yillik tasarruf: 5.5 x 0.12 x 6,000 = 3,960 EUR/yil
  Yatirim: 6,500 EUR (55 kW VSD + montaj + komisyonlama)
  SPP = 6,500 / 3,960 = 1.64 yil

Proje 5 — Pompa 1 VSD Retrofit (kisma vanasi kaldirilmasi):
  Hedef: Kisma vanasini kaldirip VSD ile kontrol
  Mevcut: 15 kW x 0.65 = 9.75 kW (kismali)
  VSD ile: 15 x (0.65)^3 = 4.12 kW
  Tasarruf: 9.75 - 4.12 = 5.63 kW
  Kacinilabilir exergy kazanimi: ~3.5 kW (I_EN_AV'nin %91'i)
  Yillik tasarruf: 5.63 x 0.12 x 6,500 = 4,391 EUR/yil
  Yatirim: 3,800 EUR (15 kW VSD + vana bypas + montaj)
  SPP = 3,800 / 4,391 = 0.87 yil (10.4 ay)
```

### 3.9 Toplam Yatirim Portfoyu

```
ExergyLab Yatirim Portfoy Ozeti — Tekstil Fabrikasi (Boyahane)
======================================================================

Sira | Proje                       | Yatirim [EUR] | Tasarruf [EUR/yil] | SPP [yil]
-----+-----------------------------+---------------+--------------------+----------
  1  | Chiller bakim/optimizasyon  |     4,500     |       9,834        |   0.46
  2  | Kazan ekonomizer            |    22,000     |      32,321        |   0.68
  3  | Kazan O2 trim kontrol       |     8,500     |      10,238        |   0.83
  4  | Pompa 1 VSD retrofit        |     3,800     |       4,391        |   0.87
  5  | Kompresor VSD               |     6,500     |       3,960        |   1.64
-----+-----------------------------+---------------+--------------------+----------
     | TOPLAM                      |    45,300     |      60,744        |   0.75
======================================================================

Toplam yatirim: 45,300 EUR
Toplam yillik tasarruf: 60,744 EUR/yil
Bilesik geri odeme: 0.75 yil (9 ay)
NPV (10 yil, %10 iskonto): ~328,000 EUR

Enerji tasarrufu dagilimi:
  Yakit (dogalgaz) tasarrufu: 42,559 EUR/yil (%70)
  Elektrik tasarrufu: 18,185 EUR/yil (%30)

Toplam enerji tasarrufu orani: ~%15
CO2 azaltimi: ~95 ton/yil
  (Dogalgaz: 0.202 kg CO2/kWh, Elektrik: 0.450 kg CO2/kWh)
```

### 3.10 Fazli Uygulama Plani

```
Faz 1 — Hizli Kazanimlar (Quick Wins) — 0-3 ay:
  Proje: Chiller bakim/optimizasyon + Pompa 1 VSD retrofit
  Yatirim: 4,500 + 3,800 = 8,300 EUR
  Yillik tasarruf: 9,834 + 4,391 = 14,225 EUR/yil
  SPP: 0.58 yil (7 ay)
  Durum suresi: 0 gun (bakim hemen yapilabilir)

Faz 2 — Orta Vadeli Yatirimlar — 3-6 ay:
  Proje: Kazan ekonomizer + O2 trim kontrol
  Yatirim: 22,000 + 8,500 = 30,500 EUR
  Yillik tasarruf: 32,321 + 10,238 = 42,559 EUR/yil
  SPP: 0.72 yil (8.6 ay)
  Not: Ekonomizer montaji icin kazan kisa sureli durdurulur (2-3 gun)
  Planlanan bakim arasi ile eslestirilmesi onerilir.

Faz 3 — Uzun Vadeli Yatirimlar — 6-12 ay:
  Proje: Kompresor VSD ekleme
  Yatirim: 6,500 EUR
  Yillik tasarruf: 3,960 EUR/yil
  SPP: 1.64 yil
  Not: Faz 1 ve 2'nin tasarruflari bu yatirimi finanse eder.

Kumulatif nakit akisi:
  Ay 0:   -8,300 EUR (Faz 1 yatirimi)
  Ay 3:   -8,300 + 3,556 = -4,744 EUR (3 aylik Faz 1 tasarrufu)
  Ay 3:   -4,744 - 30,500 = -35,244 EUR (Faz 2 yatirimi)
  Ay 6:   -35,244 + 14,196 = -21,048 EUR (3 aylik Faz 1+2 tasarrufu)
  Ay 6:   -21,048 - 6,500 = -27,548 EUR (Faz 3 yatirimi)
  Ay 9:   -27,548 + 15,186 = -12,362 EUR
  Ay 12:  -12,362 + 15,186 = +2,824 EUR --> POZITIF (11 ayda geri odeme)
  Ay 24:  +2,824 + 60,744 = +63,568 EUR
  Ay 60:  +2,824 + 4 x 60,744 = +245,800 EUR (5 yil sonunda)
```

### 3.11 Dersler ve Cikarimlar — Tekstil Fabrikasi

```
Ders 1 — Geleneksel analiz kazana saplandirir:
  Geleneksel yaklasim: "Kazan %92.5 kayip — her sey kazanda!"
  Ileri yaklasim: "Kazan theta = 0.16 — kazanin buyuk kismi kacinlamaz"
  Kazan onemlidir (IPN = 0.682), ama ekonomizer + O2 trim yeterlidir.
  Tam kondansasyon kazani degisimi (>150,000 EUR) gerekli degildir.

Ders 2 — Pompa 1 gizli sampiyondur:
  Geleneksel analizde Pompa 1 yalnizca 6.17 kW (%0.5) ile ihmal
  edilir. Ancak theta = 0.74 ile en yuksek kacinilabilirlik oranina
  sahiptir. VSD yatirimi 3,800 EUR ile 0.87 yilda geri doner.
  Bu, ileri analizin en degerli icgorusudur.

Ders 3 — Chiller bakimi dusuk maliyetli yuksek getiri:
  Chiller'in COP'u 3.2'den 4.2'ye cikarilmasi sadece temizlik ve
  bakim ile mumkundur. 4,500 EUR yatirim, 9,834 EUR/yil getiri.
  Bu "dusuk sarkan meyve" geleneksel analizde de gorunur, ancak
  ileri analiz bunun I_EN_AV bolumunu acikca ortaya koyar.

Ders 4 — VSD olan ekipman zaten iyidir:
  Pompa 2 (VSD mevcut) theta = 0.35 ile orta seviyededir ve
  IPN = 0.002 ile en dusuk onceliklidir. VSD'nin kisma vanasini
  ortadan kaldirmasi, kacinilabilir yikimi onemli olcude azaltmistir.
  Bu, VSD yatiriminin degerini dogrudan kanitlar.

Ders 5 — Toplam fabrika theta dusuk gorunur, ama tasarruf gerceldir:
  theta_fabrika = 0.183 dusuk gorunse de, mutlak kacinilabilir
  maliyet 81,843 EUR/yil'dir. Onemli olan oran degil, mutlak degerdir.
  45,300 EUR yatirimla 60,744 EUR/yil gercekci tasarruf elde edilir.

Ders 6 — Ekipmanlar arasi etki (eksojen bilesenler):
  Kazanin I_EX_AV = 26.0 kW: Kompresur ve pompa iyilestirmeleri
  kazanin yikimini da dolayli olarak azaltir (ornegin pompa VSD
  ile sogutma suyu akisinin optimize edilmesi, kondensat donusunun
  iyilesmesi). Bu dolayli faydalari geleneksel analiz gostermez.
```

## Uc Vakanin Karsilastirmali Ozeti

```
Karsilastirma Tablosu:

Kriter                    | Vaka 1 (CCPP)  | Vaka 2 (Sogutma) | Vaka 3 (Tekstil)
--------------------------+----------------+-------------------+------------------
Sistem olcegi             | 400 MW         | 500 kW            | ~1.3 MW exergy
Bilesen sayisi            | 12             | 6                 | 5
Geleneksel 1. oncelik     | Yanma odasi    | Kondenser         | Kazan
Ileri (theta) 1. oncelik  | BT LP          | HP kompresur      | Pompa 1
Ileri (I_EN_AV) 1. oncelik| Yanma odasi    | LP kompresur      | Kazan
En yaniltici bilesen      | Yanma odasi    | Genlesme vanalari | Kazan
En buyuk theta            | 0.57 (BT LP)   | 0.52 (HP-C)       | 0.74 (Pompa 1)
En kucuk theta            | 0.13 (CC)      | 0.11 (LP-EV)      | 0.16 (Kazan)
Toplam kacinilabilir oran | ~%25           | ~%35               | ~%18
Siralama degisimi         | Evet (1-->2)   | Evet (3-->6)       | Evet (4-->1 theta)

Ortak Sonuclar:
1. Yanma/genlesme gibi termodinamik sinirlar her zaman buyuk ama kacinlamaz
2. Donerli makineler (turbin, kompresur, pompa) yuksek theta degerine sahip
3. Geleneksel ve ileri siralama %60+ olasilikla FARKLI sonuc verir
4. Ileri analiz, yatirimi dogru bileşene yonlendirir ve gercekci beklenti olusturur
```

## İlgili Dosyalar

- [Ileri Exergy Analizi Genel Bakis](overview.md) -- Temel kavramlar, tarihce ve ilk sayisal ornekler
- [4-Yollu Dekompozisyon](four_way_splitting.md) -- Hesaplama metodolojisi, IPN, karar akisi
- [Kacinilabilir/Kacinlamaz Ayrim](avoidable_unavoidable.md) -- BAT parametreleri ve kacinilabilirlik analizi
- [Endojen/Eksojen Ayrim](endogenous_exogenous.md) -- Hibrit cevrim metodolojisi
- [Metodoloji](methodology.md) -- Genel ileri exergy analiz metodolojisi
- [Ekipmanlar Arasi Optimizasyon](../cross_equipment.md) -- Eksojen etkilerin pratik karsiligi
- [Onceliklendirme](../prioritization.md) -- Yatirim onceliklendirme cercevesi
- [Fabrika Benchmarklari](../factory_benchmarks.md) -- Sektorel performans karsilastirmalari
- [Exergoekonomik Genel Bakis](../exergoeconomic/overview.md) -- Maliyet-exergy iliskisi
- [Termoekonomik Optimizasyon](../thermoeconomic_optimization/overview.md) -- Maliyet-verim dengesi
- [Kazan Formulleri](../../boiler/formulas.md) -- Kazan exergy hesaplamalari
- [Kompresor Benchmarklari](../../compressor/benchmarks.md) -- Kompresor verim verileri
- [Chiller Formulleri](../../chiller/formulas.md) -- Chiller exergy hesaplamalari
- [Pompa Formulleri](../../pump/formulas.md) -- Pompa exergy hesaplamalari

## Referanslar

1. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. -- Vaka 1'in temel kaynagi; kombine cevrim santralinde 4-yollu analiz.

2. Morosuk, T. & Tsatsaronis, G. (2011). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258. -- Vaka 2'nin temel kaynagi; sogutma sistemlerinde ileri exergy analizi.

3. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. -- Endojen/eksojen ayrim metodolojisinin sistematik formülasyonu.

4. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. John Wiley & Sons. -- Exergoekonomik teori ve termodinamik optimizasyonun temel referansi.

5. Tsatsaronis, G. & Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. -- Kacinilabilir/kacinlamaz kavraminin ilk sistematik tanimlari.

6. Petrakopoulou, F., Tsatsaronis, G. & Morosuk, T. (2013). "Evaluation of a power plant with chemical looping combustion using an advanced exergetic analysis." *Energy*, 60, 202-211. -- Ileri exergy analizinin guc santrallerindeki uygulamalari.

7. Cziesla, F., Tsatsaronis, G. & Gao, Z. (2006). "Avoidable thermodynamic inefficiencies and costs in an externally fired combined cycle power plant." *Energy*, 31(10-11), 1472-1489. -- Kacinilabilir maliyet kavraminin endustriyel uygulamasi.
