---
title: "Buyuk Bilesik Egri - GCC (Grand Composite Curve)"
category: factory
equipment_type: factory
keywords: [grand composite curve, GCC, buyuk bilesik egri, utility yerlestirme, isi cebi, heat pocket, CHP, isi pompasi, exergy GCC, pinch analizi, enerji hedefleme]
related_files: [factory/pinch/INDEX.md, factory/pinch/problem_table.md, factory/pinch/composite_curves.md, factory/pinch/utility_systems.md, factory/pinch/fundamentals.md, factory/heat_integration.md, factory/cross_equipment.md]
use_when: ["GCC olusturma ve yorumlama gerektiginde", "Utility seviyelerini optimize ederken", "CHP veya isi pompasi boyutlandirirken", "Isi cebi analizi yapilirken", "Exergy tabanli utility secimi yapilirken"]
priority: high
last_updated: 2026-02-01
---

# Buyuk Bilesik Egri - GCC (Grand Composite Curve)

> Son guncelleme: 2026-02-01

## Genel Bakis

Buyuk Bilesik Egri (Grand Composite Curve - GCC), pinch analizinin en guclu araclarindan biridir. Problem Tablosu Algoritmasi'nin (PTA) duzeltilmis kaskad sonuclarindan elde edilen GCC, kaydirilmis sicaklik (shifted temperature, T*) ile net isi akisi (net heat flow, R) arasindaki iliskiyi grafik olarak gosterir. Bilesik egrilerin (composite curves) aksine, GCC dogrudan utility seviye secimi, CHP boyutlandirmasi, isi pompasi yerlestirme ve isi cebi (heat pocket) analizi icin kullanilir.

GCC'nin temel avantaji, prosesin utility ile etkilesimini tek bir egri uzerinde gostermesidir. Bilesik egrilerde iki ayri egri (sicak ve soguk) varken, GCC bunlari tek bir profile indirger ve muhendise "prosesin hangi sicaklik seviyesinde ne kadar dis enerjiye ihtiyaci var?" sorusunu dogrudan yanitlar.

Bu dosya, 5-akisli referans problem uzerinden GCC'nin olusturulmasini, yorumlanmasini ve ileri uygulamalarini kapsamli sekilde aciklar.

### Referans Problem (Tum Dosyalarda Ortak)

```
Akis Verileri:
  H1: 270->80 C,  CP=15 kW/ C,  Q=2,850 kW
  H2: 180->40 C,  CP=25 kW/ C,  Q=3,500 kW
  H3: 150->60 C,  CP=10 kW/ C,  Q=900 kW
  C1: 30->250 C,  CP=18 kW/ C,  Q=3,960 kW
  C2: 60->200 C,  CP=12 kW/ C,  Q=1,680 kW

Delta_Tmin = 10 C
Pinch: 175 C (shifted) / 180 C (hot) / 170 C (cold)
QH,min = 1,800 kW
QC,min = 2,240 kW
```

---

## 1. GCC Tanimi ve Olusturma (GCC Definition and Construction)

### 1.1 GCC Nedir?

GCC, duzeltilmis kaskadin grafik gosterimidir. Dikey eksen kaydirilmis sicakligi (T*), yatay eksen ise net isi akisini (R, kW) temsil eder. GCC'nin iki kritik ozelligi vardir:

1. **Pinch noktasinda R = 0:** Egri yatay eksene dokunur
2. **Uc noktalar:** Ust ucta QH,min, alt ucta QC,min okunur

```
GCC Tanimi:
  Dikey eksen: T* (kaydirilmis sicaklik, C)
  Yatay eksen: R  (net isi akisi, kW)

  T* = T_gercek - Delta_Tmin/2  (sicak akislar icin)
  T* = T_gercek + Delta_Tmin/2  (soguk akislar icin)

  R degeri Problem Tablosu Algoritmasi'nin duzeltilmis kaskadi'ndan alinir.
  Pinch noktasinda R = 0 olacak sekilde duzeltme yapilir.
```

### 1.2 GCC Olusturma Adimlari (Step-by-Step Construction)

GCC'yi olusturmak icin Problem Tablosu Algoritmasi'nin (PTA) sonuclari kullanilir. Asagida adim adim surec gosterilmistir:

**Adim 1: Kaydirilmis Sicakliklari Hesapla**

```
Delta_Tmin = 10 C  =>  Delta_Tmin/2 = 5 C

Sicak akislar (T* = T - 5):
  H1: 265 -> 75 C
  H2: 175 -> 35 C
  H3: 145 -> 55 C

Soguk akislar (T* = T + 5):
  C1: 35 -> 255 C
  C2: 65 -> 205 C
```

**Adim 2: Sicaklik Araliklarini Belirle**

```
Tum kaydirilmis sicakliklari siralama (buyukten kucuge):
  255, 205, 175, 145, 75, 65, 55, 35

Sicaklik araliklari:
  Aralik 1: 255 - 205 = 50 C
  Aralik 2: 205 - 175 = 30 C
  Aralik 3: 175 - 145 = 30 C
  Aralik 4: 145 - 75  = 70 C
  Aralik 5: 75  - 65  = 10 C
  Aralik 6: 65  - 55  = 10 C
  Aralik 7: 55  - 35  = 20 C
```

**Adim 3: Her Aralikta Net Isi Dengesini Hesapla**

```
Aralik [C]   | Aktif Sicak     | Aktif Soguk    | CP_H   | CP_C   | Net CP        | Delta_T | Delta_H [kW]
-------------|-----------------|----------------|--------|--------|---------------|---------|-------------
255 - 205    | (yok)           | C1             | 0      | 18     | 0 - 18 = -18  | 50      | -900
205 - 175    | (yok)           | C1 + C2        | 0      | 30     | 0 - 30 = -30  | 30      | -900
175 - 145    | H1 + H2         | C1 + C2        | 40     | 30     | 40 - 30 = +10 | 30      | +300
145 - 75     | H1 + H2 + H3    | C1 + C2        | 50     | 30     | 50 - 30 = +20 | 70      | +1,400
75 - 65      | H2 + H3         | C1 + C2        | 35     | 30     | 35 - 30 = +5  | 10      | +50
65 - 55      | H2 + H3         | C2             | 35     | 12     | 35 - 12 = +23 | 10      | +230
55 - 35      | H2              | C2             | 25     | 12     | 25 - 12 = +13 | 20      | +260

Not: H1 aktif araligi 265-75 C, H2: 175-35 C, H3: 145-55 C
     C1 aktif araligi 35-255 C, C2: 65-205 C
```

**Adim 4: Duzeltilmemis Kaskad (Uncorrected Cascade)**

```
Baslangic: R_0 = 0 (henuz duzeltme yok)

T* = 255 C:  R = 0
T* = 205 C:  R = 0 + (-900)   = -900 kW
T* = 175 C:  R = -900 + (-900) = -1,800 kW   <-- En negatif deger
T* = 145 C:  R = -1,800 + 300  = -1,500 kW
T* = 75  C:  R = -1,500 + 1,400 = -100 kW
T* = 65  C:  R = -100 + 50      = -50 kW
T* = 55  C:  R = -50 + 230      = +180 kW
T* = 35  C:  R = 180 + 260      = +440 kW
```

**Adim 5: Duzeltilmis Kaskad (Corrected Cascade)**

```
Duzeltme: R_0 = |en negatif deger| = |-1,800| = 1,800 kW
Bu deger QH,min'dir (minimum sicak utility).

T* = 255 C:  R = 0 + 1,800 = 1,800 kW   <-- QH,min
T* = 205 C:  R = -900 + 1,800 = 900 kW
T* = 175 C:  R = -1,800 + 1,800 = 0 kW   <-- PINCH NOKTASI
T* = 145 C:  R = -1,500 + 1,800 = 300 kW
T* = 75  C:  R = -100 + 1,800 = 1,700 kW
T* = 65  C:  R = -50 + 1,800 = 1,750 kW
T* = 55  C:  R = 180 + 1,800 = 1,980 kW
T* = 35  C:  R = 440 + 1,800 = 2,240 kW   <-- QC,min
```

### 1.3 GCC Veri Tablosu (Grand Composite Curve Data Table)

```
+--------+-----------------+------------------------------+
| T* [C] | R (net isi) [kW]| Aciklama                     |
+--------+-----------------+------------------------------+
|  255   |    1,800        | QH,min - Sicak utility baslangici |
|  205   |      900        | Ara nokta                    |
|  175   |        0        | PINCH NOKTASI                |
|  145   |      300        | Isi cebi baslangici          |
|   75   |    1,700        | Isi cebi bitisi              |
|   65   |    1,750        | Ara nokta                    |
|   55   |    1,980        | Ara nokta                    |
|   35   |    2,240        | QC,min - Soguk utility sonu  |
+--------+-----------------+------------------------------+

Dogrulama:
  QH,min = 1,800 kW  (ust nokta)
  QC,min = 2,240 kW  (alt nokta)
  Pinch  = 175 C     (R = 0 noktasi)
```

### 1.4 GCC ASCII Diyagrami

```
T* [C]
  |
260|  *                                     QH,min = 1,800 kW
  |   \
240|    \
  |     \
220|      \
  |       \
200|        *                               R = 900 kW
  |         \
180|          \
  |           \
175|- - - - - -*  <- PINCH (R = 0)
  |           /
160|          /
  |         /
140|        *                               R = 300 kW (isi cebi)
  |       /
120|      /
  |     /
100|    /
  |   /
 80|  /
  | /
 75|*                                       R = 1,700 kW
  ||
 65|*                                       R = 1,750 kW
  ||
 55|*                                       R = 1,980 kW
  | \
 40|  \
  |   *                                     QC,min = 2,240 kW
 35|- - - - - - - - - - - - - - - - - - -
  |_______________________________________
  0    400   800  1200  1600  2000  2400
                  R [kW] -->

Egri Ozellikleri:
  - Pinch noktasinda (T*=175 C) egri yatay eksene dokunur
  - Ust uc (T*=255 C): QH,min = 1,800 kW okunur
  - Alt uc (T*=35 C): QC,min = 2,240 kW okunur
  - T*=145 C'de egri ice doner -> isi cebi (heat pocket)
```

---

## 2. GCC Yorumlama (GCC Interpretation)

### 2.1 Pinch Ustu Bolge (Above Pinch Region)

Pinch ustundeki bolge (T* > 175 C) bir **isi yutagi** (heat sink) gibi davranir. Bu bolgede prosesin net isi acigi vardir ve dis isi kaynagina (sicak utility) ihtiyac duyulur.

```
Pinch Ustu Analizi:
  T* araligi: 175 - 255 C
  Net isi ihtiyaci: QH,min = 1,800 kW

  Fiziksel anlam:
  - Bu bolgede soguk akislarin isi talebi, sicak akislarin isi arzindan fazladir
  - Fark, sicak utility (buhar, atesli isitici vb.) ile karsilanmalidir
  - GCC egrisinin bu bolgedeki genisligi, utility ihtiyacinin yogunlugunu gosterir

  T* = 255 C'de: R = 1,800 kW (tum sicak utility burada temsil edilir)
  T* = 205 C'de: R = 900 kW (orta bolgede azalan ihtiyac)
  T* = 175 C'de: R = 0 kW (pinch - isi dengede)
```

### 2.2 Pinch Alti Bolge (Below Pinch Region)

Pinch altindaki bolge (T* < 175 C) bir **isi kaynagi** (heat source) gibi davranir. Bu bolgede prosesin net isi fazlasi vardir ve dis sogutma (soguk utility) gereklidir.

```
Pinch Alti Analizi:
  T* araligi: 35 - 175 C
  Net isi fazlasi: QC,min = 2,240 kW

  Fiziksel anlam:
  - Bu bolgede sicak akislarin isi arzi, soguk akislarin isi talebinden fazladir
  - Fark, soguk utility (sogutma suyu, chiller vb.) ile uzaklastirilmalidir
  - GCC egrisinin bu bolgedeki genisligi, sogutma ihtiyacinin yogunlugunu gosterir

  T* = 175 C'de: R = 0 kW (pinch)
  T* = 145 C'de: R = 300 kW (dusuk isi fazlasi bolgesi)
  T* = 75  C'de: R = 1,700 kW (yuksek isi fazlasi bolgesi)
  T* = 35  C'de: R = 2,240 kW (tum soguk utility burada)
```

### 2.3 Burun / Cep Bolgeleri (Nose / Pocket Regions)

GCC uzerinde bazi bolgeler egri icerisine dogru kivrilan "burun" (nose) veya "cep" (pocket) olusturur. Bu bolgeler onemli bilgi tasir:

```
Burun bolgeleri:
  - GCC'nin yatay eksene yaklasip tekrar uzaklastigi bolgelerdir
  - Bu bolgelerde ic isi degisimi (internal heat exchange) potansiyeli vardir
  - Burun ne kadar buyukse, o kadar fazla ic isi degisimi mumkundur
  - Burun bolgesi utility ihtiyacini etkilemez (zaten ic olarak karsilanir)

Referans problemde:
  T* = 145 C'de R = 300 kW deger, pinch altinda bir burun/cep olusturur.
  Bu, 175 - 145 C arasinda net CP_sicak > CP_soguk oldugunu gosterir.
  Proses bu bolgede kendi icinde isi degisimi yapabilir.
```

---

## 3. Isi Cebi Kavrami (Heat Pocket Concept)

### 3.1 Isi Cebi Nedir?

Isi cebi (heat pocket), GCC'nin kendi icerisine dogru geri dondugu bolgedir. Fiziksel olarak, bu bolgede prosesin ic isi degisimi ile karsilanabilecek bir isi gereksinimi veya fazlasi vardir; dis utility gerekmez.

```
Isi Cebi Tanimi:
  GCC uzerinde R degerinin azaldigi (yatay eksene yaklastigi) ve sonra
  tekrar arttigi bolge bir isi cebi olusturur.

  Referans problemde isi cebi:
    T* = 175 C: R = 0 kW     (pinch)
    T* = 145 C: R = 300 kW   (cep bolgesi)
    T* = 75 C:  R = 1,700 kW

  Burada T*=175-145 C arasinda R, 0'dan 300'e cikar.
  Ardindan T*=145-75 C arasinda R, 300'den 1700'e cikar.
  Bu profil monoton artan oldugundan, bu ornekte klasik bir "geri donen"
  cep yoktur. Ancak farkli veri setlerinde R degerlerinin azalip tekrar
  artmasi tipik isi cebini olusturur.
```

### 3.2 Isi Cebinin Fiziksel Anlami

```
Isi cebi olusan bolgede:
  1. Proses ic isi degisimi ile isi dengesini saglayabilir
  2. Bu bolgedeki isi, utility'den karsilanmak zorunda degildir
  3. Isi cebi ne kadar buyukse, ic isi degisimi potansiyeli o kadar fazladir
  4. Cebin ortadan kaldirilmasi icin ek esanjor gerekir

Isi cebinin utility'ye etkisi:
  - Isi cebi QH,min ve QC,min'i DEGISTIRMEZ
  - Ancak cebin ic isi degisimi ile karsilanmasi durumunda
    utility kullanim profili iyilesir
  - Cep bolgesi kullanilmazsa, zaten duzeltilmis kaskad
    bu isiyi dogru sekilde dagitir
```

### 3.3 Isi Cebinin Sayisal Tespiti

GCC verisinden isi cebi tespiti icin asagidaki algoritma uygulanir:

```
Algoritma: Isi Cebi Tespiti (Heat Pocket Detection)

Girdi: GCC veri tablosu (T*, R) - pinch'ten asagi dogru

Adim 1: Pinch noktasini bul (R = 0)
Adim 2: Pinch'ten asagiya dogru R degerlerini tara
Adim 3: R degeri azaliyor mu kontrol et (R[i+1] < R[i])
  - Evet: Isi cebi baslamistir
  - Hayir: Devam et
Adim 4: R degerinin tekrar artmaya basladigi noktayi bul
Adim 5: Cebin buyuklugu = R[cep_basi] - R[cep_dibi]

Referans problem icin:
  Pinch (T*=175): R = 0
  T*=145: R = 300      (artiyor - cep yok)
  T*=75:  R = 1,700    (artiyor - cep yok)
  T*=65:  R = 1,750    (artiyor - cep yok)
  T*=55:  R = 1,980    (artiyor - cep yok)
  T*=35:  R = 2,240    (artiyor - cep yok)

Sonuc: Referans problemde pinch altinda monoton artan profil var.
       Klasik isi cebi OLUSMAMISTIR.
       (Isi cebi olusabilmesi icin pinch altinda negatif net CP
        olan bir aralik gerekir.)
```

### 3.4 Isi Cebi Olan Ornek Senaryo

```
Farkli bir problemde isi cebi ornegi:
(Referans probleme C3: 100->160 C, CP=40 kW/C soguk akis eklendigini varsayalim)

T* [C]  | R [kW]  | Yorum
--------|---------|------------------
  175   |     0   | Pinch
  155   |   100   | Artis
  145   |  -200   | Azalis -> ISI CEBI BASLANGICI
  105   |  -500   | Cep dibi
   75   |   700   | Artis -> ISI CEBI BITISI
   35   | 1,500   | QC,min

Isi cebi buyuklugu: 100 - (-500) = 600 kW
Bu 600 kW'lik isi, ic isi degisimi ile karsilanabilir.
Isi cebi, utility ihtiyacini degistirmez ancak HEN tasarimini etkiler.
```

---

## 4. Utility Yerlestirme (Utility Placement)

### 4.1 GCC ile Utility Seviye Secimi

GCC'nin en guclu uygulamalarindan biri, coklu utility seviyelerinin optimum yerlesimini belirlemektir. Tek seviye utility (ornegin yalnizca HP buhar) kullanmak yerine, GCC'nin profiline uygun birden fazla utility seviyesi kullanilarak maliyet optimize edilir.

```
Utility Yerlestirme Prensibi:
  1. GCC uzerinde yatay bir cizgi cekilir (utility sicakligi)
  2. Bu cizgi GCC ile kesistigi noktaya kadar utility kullanilabilir
  3. Kalan isi, bir ust/alt utility seviyesinden karsilanir

Kural: Mumkun olan en dusuk kaliteli (en ucuz) utility tercih edilir.
  - Pinch ustu: Mumkun olan en dusuk sicaklikta sicak utility
  - Pinch alti: Mumkun olan en yuksek sicaklikta soguk utility
```

### 4.2 Referans Problem Icin Utility Yerlestirme

```
PINCH USTU (QH,min = 1,800 kW gerekli):

GCC Profili (pinch ustu):
  T* = 175 C: R = 0
  T* = 205 C: R = 900
  T* = 255 C: R = 1,800

Secenek A: Tek seviye HP buhar (T_buhar = 250 C, T* ~ 245 C)
  HP Buhar: 1,800 kW
  Maliyet: 1,800 x 0.040 = 72.0 EUR/h

Secenek B: HP + LP buhar (T_HP = 250 C, T_LP = 150 C -> T* ~ 145 C)
  Dikkat: LP buhar T* = 145 C'de. GCC'de T*=175'te R=0, yani
  LP buhar pinch ustu bolgede yalnizca T*>175 ise kullanilabilir.
  LP buhar T* = 155 C (gercek 150 C + 5 C kaydirma):
    - Pinch ustu bolgede LP buhar kullanilabilir mi?
    - GCC'de T*=175 C'de R=0 ve T*=205 C'de R=900 kW
    - LP buhar (T*~155 C) pinch sicakligindan dusuk, pinch ustu icin UYGUN DEGIL

  Duzeltilmis secenek: MP Buhar (T*=200 C, gercek ~205 C)
  GCC'de T*=205'te R=900 kW -> MP buhar ile 900 kW karsilanabilir
  HP Buhar: 1,800 - 900 = 900 kW (T*=205-255 arasi)
  MP Buhar: 900 kW (T*=175-205 arasi)

  Maliyet:
    HP Buhar: 900 x 0.040 = 36.0 EUR/h
    MP Buhar: 900 x 0.030 = 27.0 EUR/h
    Toplam: 63.0 EUR/h

  Tasarruf: 72.0 - 63.0 = 9.0 EUR/h = ~54,000 EUR/yil
```

```
PINCH ALTI (QC,min = 2,240 kW gerekli):

GCC Profili (pinch alti):
  T* = 175 C: R = 0
  T* = 145 C: R = 300
  T* = 75 C:  R = 1,700
  T* = 35 C:  R = 2,240

Secenek A: Tek seviye sogutma suyu (T = 25 C)
  Sogutma suyu: 2,240 kW
  Maliyet: 2,240 x 0.003 = 6.72 EUR/h

Secenek B: Sogutma suyu (tek seviye yeterli)
  Bu ornekte pinch alti tamamen sogutma suyu ile karsilanabilir.
  Sogutma suyu sicakligi (25-35 C) GCC'nin alt ucundan (T*=35 C)
  dusuk oldugu icin tum bolgeyi kapsar.

  Sogutma suyu yeterli -> ek soguk utility seviyesine gerek yok.
```

### 4.3 Utility Yerlestirme Ozet Tablosu

```
+-------------------+----------+----------+-------------+--------------+
| Utility           | Seviye   | Miktar   | Birim Fiyat | Yillik       |
|                   | [C]      | [kW]     | [EUR/kWh]   | Maliyet [EUR]|
+-------------------+----------+----------+-------------+--------------+
| HP Buhar          | 250      | 900      | 0.040       | 280,800      |
| MP Buhar          | 205      | 900      | 0.030       | 210,600      |
| Sogutma Suyu      | 25-35    | 2,240    | 0.003       | 52,530       |
+-------------------+----------+----------+-------------+--------------+
| TOPLAM            |          |          |             | 543,930      |
+-------------------+----------+----------+-------------+--------------+

Karsilastirma (tek seviye HP buhar + sogutma suyu):
  HP Buhar: 1,800 kW x 0.040 = 561,600 EUR/yil
  Sogutma suyu: 2,240 kW x 0.003 = 52,530 EUR/yil
  Toplam: 614,130 EUR/yil

Coklu utility tasarrufu: 614,130 - 543,930 = 70,200 EUR/yil
```

### 4.4 GCC Uzerinde Utility Gosterimi (ASCII)

```
T* [C]
  |
260|  *............. QH,min = 1,800 kW
  |   \          :
240|    \         :  HP Buhar: 900 kW
  |     \        :  (T* > 205 C bolgesi)
220|      \       :
  |       \      :
200|        *.....:  R = 900 kW
  |         \    :
180|          \   :  MP Buhar: 900 kW
  |           \  :  (175 < T* < 205 C)
175|- - - - - -*  <- PINCH (R = 0)
  |           /
160|          /
  |         /
140|        *
  |       /
120|      /
  |     /
100|    /
  |   /
 80|  /
  | /
 75|*
  ||              :
 65|*             :  Sogutma Suyu: 2,240 kW
  ||              :  (T* < 175 C tum bolgesi)
 55|*             :
  | \             :
 40|  \           :
  |   *...........:  QC,min = 2,240 kW
  |_______________________________________
  0    400   800  1200  1600  2000  2400
                  R [kW] -->
```

---

## 5. CHP Potansiyeli (Combined Heat and Power Potential)

### 5.1 GCC ile CHP Boyutlandirmasi

GCC, kombine isi ve guc (Combined Heat and Power - CHP) sistemlerinin boyutlandirilmasinda kritik bir aractir. Townsend ve Linnhoff (1983) tarafindan gelistirilen "Uygun Yerlestirme Prensibi" (Appropriate Placement Principle), CHP'nin pinch'e gore nereye yerlestirileceigini belirler.

```
Uygun Yerlestirme Prensibi (Appropriate Placement):

  CHP sistemi isi uretir ve guc (shaft work) saglar.
  CHP'nin pinch'e gore yerlestirmesi:

  1. Pinch USTU yerlestirme (DOGRU):
     - CHP'nin atik isisi prosesin pinch ustu ihtiyacini karsilar
     - Hem guc uretilir hem de sicak utility azalir
     - Net fayda: Guc + Isi tasarrufu

  2. Pinch ALTI yerlestirme (YANLIS):
     - CHP'nin atik isisi pinch altinda kullanilir
     - Ancak pinch altinda zaten isi fazlasi var
     - Sonuc: Ek soguk utility gerekir -> CHP faydasi azalir

  3. Pinch UZERINDEN yerlestirme (YANLIS):
     - CHP pinch ustunden isi alir, pinch altina verir
     - Bu pinch kuralini ihlal eder
     - Sonuc: 2x ceza (QH,min artar, QC,min artar)
```

### 5.2 CHP Boyutlandirma Hesabi

```
Referans Problem Icin CHP Analizi:

GCC Pinch Ustu Profili:
  T* = 175 C: R = 0
  T* = 205 C: R = 900 kW
  T* = 255 C: R = 1,800 kW

CHP Potansiyeli:
  QH,min = 1,800 kW (tum sicak utility CHP ile karsilanabilir)

Gaz Turbini Ornegi:
  Elektrik verimi: eta_e = 0.30
  Isil verim: eta_th = 0.50
  Toplam verim: eta_total = 0.80

  Gerekli isi: Q_CHP = 1,800 kW
  Yakit girdisi: Q_yakit = Q_CHP / eta_th = 1,800 / 0.50 = 3,600 kW
  Elektrik uretimi: W_e = Q_yakit x eta_e = 3,600 x 0.30 = 1,080 kW_e
  Atik isi (baca + kayip): Q_kayip = Q_yakit x (1 - eta_total) = 720 kW

  Karsilastirma (CHP olmadan):
    Ayri buhar kazani: Q_buhar = 1,800 kW, eta_kazan = 0.90
    Yakit = 1,800 / 0.90 = 2,000 kW
    Ayri elektrik (sebekeden): W_e = 1,080 kW_e
    Sebekeden alinan elektrigin birincil enerji karsiligi:
    Q_primer = 1,080 / 0.40 = 2,700 kW (santral verimi %40)
    Toplam birincil enerji: 2,000 + 2,700 = 4,700 kW

  CHP ile:
    Toplam birincil enerji: 3,600 kW
    Tasarruf: 4,700 - 3,600 = 1,100 kW (%23.4 birincil enerji tasarrufu)
```

### 5.3 Shaft Work Hedefleme (Shaft Work Targeting from GCC)

```
GCC'den shaft work hedefi:
  W_max = QH,min x (1 - T_pinch / T_CHP_kaynak)

  T_pinch = 175 + 273 = 448 K (shifted pinch)
  T_CHP_kaynak = 1200 C (gaz turbini cikis) = 1473 K

  W_max = 1,800 x (1 - 448/1473) = 1,800 x 0.696 = 1,253 kW

  Gercekci hedef (tersinmezlik hesaba katildiginda):
  W_gercekci = W_max x eta_Carnot_faktor = 1,253 x 0.65 = 814 kW

  Not: Bu hedef, GCC profilinin tamami boyunca entegre edildiginde
  elde edilir. Pratik CHP verimi bu hedefin %60-80'ine ulasabilir.
```

---

## 6. Isi Pompasi Yerlestirme (Heat Pump Placement)

### 6.1 Pinch Uzerinden Isi Pompasi Kavrami

Isi pompasi, dusuk sicakliktan yuksek sicakliga isi transfer eden bir cihazidir. Pinch analizinde en etkili isi pompasi yerlestirmesi, pinch noktasi UZERINDEN (across-pinch) yapilan yerlestirmedir.

```
Isi Pompasi Prensibi:
  - Pinch altindan (isi fazlasi bolgesi) isi alinir
  - Pinch ustune (isi acigi bolgesi) isi pompalar
  - Her iki taraftaki utility ihtiyaci ayni anda azalir

  Enerji dengesi:
    Q_H_verilen = Q_C_alinan + W_kompressor
    QH,min_yeni = QH,min - Q_H_verilen
    QC,min_yeni = QC,min - Q_C_alinan

  COP (Coefficient of Performance):
    COP = Q_H_verilen / W_kompressor
    COP_Carnot = T_H / (T_H - T_C)   [Kelvin cinsinden]
```

### 6.2 Isi Pompasi Ekonomik Uygulanabilirlik

```
Ekonomik Uygulanabilirlik Kriteri:

Isi pompasi ekonomik olabilmesi icin:
  COP_gercek >= Elektrik fiyati / Isil enerji fiyati

Ornek hesap:
  Elektrik fiyati: 0.12 EUR/kWh
  Dogalgaz fiyati: 0.04 EUR/kWh (buhar uretimi icin)
  Kazan verimi: 0.90
  Buhar maliyeti: 0.04 / 0.90 = 0.044 EUR/kWh_th

  Minimum gerekli COP:
  COP_min = 0.12 / 0.044 = 2.73

  Carnot COP kontrolu (referans problem icin):
    T_H = 180 C = 453 K (pinch sicak tarafi)
    T_C = 170 C = 443 K (pinch soguk tarafi)
    COP_Carnot = 453 / (453 - 443) = 45.3

  Gercekci COP = COP_Carnot x eta = 45.3 x 0.50 = 22.7
  COP_gercek (22.7) >> COP_min (2.73) -> UYGUN

  ANCAK: Pinch etrafindaki sicaklik farki cok kucuk (10 C).
  Pratik isi pompasi tasarimi icin genellikle en az 20-30 C
  sicaklik farki gerekir. GCC uzerinden daha genis bir bolge
  secilmelidir.
```

### 6.3 GCC ile Isi Pompasi Boyutlandirma

```
GCC Uzerinde Isi Pompasi Yerlestirme:

Optimum yerlestirme, GCC'nin "dar" bolgelerine yakindir.
Referans problemde GCC'nin pinch bolgesi cok dardir (R=0 -> R=300 -> R=1700)
Bu durum isi pompasi icin potansiyel olusturur.

Ornek boyutlandirma:
  Isi pompasi sicak cikis: T* = 190 C (pinch ustunde)
  Isi pompasi soguk giris: T* = 145 C (pinch altinda)

  COP_Carnot = (190+273) / ((190+273) - (145+273)) = 463 / 45 = 10.3
  COP_gercek = 10.3 x 0.50 = 5.15

  Isi pompasi ile karsilanan yuk: Q_HP = 300 kW (cep bolgesi)
  Kompressor gucu: W = Q_HP / COP = 300 / 5.15 = 58.3 kW

  Utility etkileri:
    QH,min_yeni = 1,800 - 300 = 1,500 kW (-16.7%)
    QC,min_yeni = 2,240 - (300 - 58.3) = 2,240 - 241.7 = 1,998 kW (-10.8%)

  Ekonomik analiz:
    Sicak utility tasarrufu: 300 x 0.040 = 12.0 EUR/h
    Soguk utility tasarrufu: 241.7 x 0.003 = 0.73 EUR/h
    Kompressor elektrik maliyeti: 58.3 x 0.12 = 7.0 EUR/h
    Net tasarruf: 12.0 + 0.73 - 7.0 = 5.73 EUR/h = ~34,400 EUR/yil
```

---

## 7. Exergy Grand Composite Curve

### 7.1 Termal GCC'den Exergy GCC'ye Donusum

Standart GCC termal enerji (enthalpy) bazindadir. Ancak termodinamigin 2. yasasi acisindan, exergy bazinda analiz daha anlamli sonuclar verir. Exergy GCC, Carnot faktorunu entegre ederek utility secimini exergy kaybi acisindan optimize eder.

```
Exergy GCC Donusum Formulleri:

Carnot Faktoru:
  eta_C = 1 - T_0 / T*

  Burada:
  T_0 = referans cevre sicakligi [K] (genellikle 298 K = 25 C)
  T* = kaydirilmis sicaklik [K]

Exergy akisi:
  Ex = R x eta_C = R x (1 - T_0 / T*)

  Burada:
  R = net isi akisi [kW] (GCC degerlerinden)
  Ex = exergy akisi [kW]
```

### 7.2 Exergy GCC Veri Tablosu

```
T_0 = 25 C = 298 K

+--------+---------+---------+----------+---------+
| T* [C] | T* [K]  | R [kW]  | eta_C    | Ex [kW] |
+--------+---------+---------+----------+---------+
|  255   |  528    |  1,800  | 0.4356   |   784   |
|  205   |  478    |    900  | 0.3766   |   339   |
|  175   |  448    |      0  | 0.3348   |     0   |
|  145   |  418    |    300  | 0.2871   |    86   |
|   75   |  348    |  1,700  | 0.1437   |   244   |
|   65   |  338    |  1,750  | 0.1183   |   207   |
|   55   |  328    |  1,980  | 0.0915   |   181   |
|   35   |  308    |  2,240  | 0.0325   |    73   |
+--------+---------+---------+----------+---------+

Onemli gozlemler:
1. Pinch ustunde exergy yogunlugu yuksek (yuksek sicaklik = yuksek kalite)
2. Pinch altinda exergy yogunlugu dusuk (dusuk sicaklik = dusuk kalite)
3. T*=35 C'de 2,240 kW termal enerji varken yalnizca 73 kW exergy var
   -> Bu isi cok dusuk kaliteli, geri kazanim degeri sinirli
4. T*=255 C'de 1,800 kW'nin 784 kW'si exergy
   -> Bu isi yuksek kaliteli, degerli
```

### 7.3 Exergy GCC ASCII Diyagrami

```
T* [C]
  |
260|  *                                     Ex = 784 kW
  |   \
240|    \
  |     \
220|      \
  |       \
200|        *                               Ex = 339 kW
  |         \
180|          \
  |           \
175|- - - - - -*  <- PINCH (Ex = 0)
  |          /
160|         /
  |        /
140|       *                                Ex = 86 kW
  |      /
120|     /
  |    /
100|   /
  |  /
 80| /
  |/
 75*                                        Ex = 244 kW
  |
 65*                                        Ex = 207 kW
  |
 55*                                        Ex = 181 kW
  |\
 40| \
  |  *                                      Ex = 73 kW
  |_______________________________________
  0    100   200   300   400   500   600  700  800
                  Ex [kW] -->

Karsilastirma: Termal GCC vs Exergy GCC
  - Termal GCC'de pinch alti buyuk gozukur (2,240 kW)
  - Exergy GCC'de pinch alti kucuk gozukur (73 kW)
  - Gercek termodinamik deger exergy ile olculur
```

### 7.4 Exergy Bazli Utility Optimizasyonu

```
Exergy GCC ile Utility Karsilastirma:

Sicak utility alternatifleri:
  1. HP Buhar (250 C, 523 K):
     eta_C = 1 - 298/523 = 0.430
     Exergy girisi = 1,800 x 0.430 = 774 kW_ex
     Proses ihtiyaci (exergy) = 784 kW_ex
     Exergy verimi = 784 / 774 = ~100% (iyi eslesme)

  2. Elektrikli isitici (varsayim: saf exergy):
     Exergy girisi = 1,800 kW_ex (elektrik = saf exergy)
     Proses ihtiyaci (exergy) = 784 kW_ex
     Exergy verimi = 784 / 1800 = 43.6% (buyuk kayip!)

  3. Direkt yanma (1200 C, 1473 K):
     eta_C = 1 - 298/1473 = 0.798
     Exergy girisi = 1,800 x 0.798 = 1,436 kW_ex
     Proses ihtiyaci (exergy) = 784 kW_ex
     Exergy verimi = 784 / 1436 = 54.6% (orta)

Sonuc: HP buhar bu proses icin en uygun exergy eslesmesini saglar.
Coklu seviye (MP + HP) kullanildiginda exergy verimi daha da artar.

Coklu seviye exergy analizi:
  HP Buhar (250 C): 900 kW -> Ex_giris = 900 x 0.430 = 387 kW_ex
  MP Buhar (205 C): 900 kW -> Ex_giris = 900 x 0.377 = 339 kW_ex
  Toplam exergy girisi = 726 kW_ex
  Proses exergy ihtiyaci = 784 kW_ex

  Not: Coklu seviye ile exergy girisi azalir cunku her seviye
  prosesin o bolgesindeki exergy ihtiyacina daha yakin kalitede
  isi saglar.
```

---

## 8. Pratik Kullanim Rehberi (Practical Usage Guide)

### 8.1 GCC Ne Zaman Kullanilir?

```
GCC Kullanim Alanlari:

1. Utility seviye secimi ve optimizasyonu
   -> Kac farkli utility seviyesi gerekli?
   -> Her seviyeden ne kadar utility kullanilmali?

2. CHP boyutlandirma
   -> CHP sistemi ne buyuklukte olmali?
   -> CHP'nin pinch'e gore yerlestirmesi nereye?

3. Isi pompasi degerlendirmesi
   -> Isi pompasi ekonomik mi?
   -> Optimum COP nedir?

4. Isi cebi analizi
   -> Proseste ic isi degisimi potansiyeli var mi?
   -> Isi cebi ne kadar buyuk?

5. Exergy bazli analiz
   -> Utility secimleri exergy acisindan uygun mu?
   -> En buyuk exergy kayiplari nerede?
```

### 8.2 GCC vs Bilesik Egriler: Hangi Durumda Hangisi?

```
+--------------------------+-------------------+-------------------+
| Karar Kriteri            | Bilesik Egriler   | GCC               |
+--------------------------+-------------------+-------------------+
| Enerji hedefi belirleme  | UYGUN             | UYGUN             |
| Pinch noktasi tespiti    | UYGUN             | UYGUN             |
| Utility seviye secimi    | SINIRLI           | EN UYGUN          |
| CHP boyutlandirma        | UYGUN DEGIL       | EN UYGUN          |
| Isi pompasi analizi      | SINIRLI           | UYGUN             |
| HEN tasarim bilgisi      | UYGUN             | SINIRLI           |
| Isi cebi tespiti         | UYGUN DEGIL       | EN UYGUN          |
| Egitim / gorsellestirme  | EN UYGUN          | ORTA              |
| Exergy analizi           | SINIRLI           | EN UYGUN          |
| Delta_Tmin duyarlilik    | UYGUN             | UYGUN             |
+--------------------------+-------------------+-------------------+

Onerilen is akisi:
  1. Once bilesik egriler ile genel resmi gor
  2. Enerji hedeflerini PTA ile hesapla
  3. GCC ile utility seviye secimi yap
  4. GCC ile CHP/isi pompasi potansiyelini degerlendir
  5. Exergy GCC ile utility kalitesini dogrula
```

### 8.3 Karar Akis Diyagrami

```
                      [Akis verileri mevcut mu?]
                                |
                    Evet        |         Hayir
                    |           |           |
              [PTA uygula]      |    [Veri topla]
                    |           |
              [GCC olustur]     |
                    |
         [Pinch noktasi R=0 mi?]
           |                    |
         Evet                 Hayir
           |                    |
    [Utility analizi]     [PTA'yi kontrol et]
           |
    +------+------+
    |             |
[Tek seviye    [Coklu seviye
 yeterli mi?]  gerekli mi?]
    |             |
  Evet          Evet
    |             |
[Maliyet      [GCC'den utility
 hesapla]      seviyelerini
               belirle]
    |             |
    +------+------+
           |
    [CHP potansiyeli var mi?]
           |
     Evet  |  Hayir
       |   |    |
  [CHP     | [Isi pompasi
   boyutla]|  degerlendirmesi]
       |   |    |
       +---+----+
           |
    [Exergy GCC ile
     dogrula]
           |
    [Optimum cozum]
```

### 8.4 Tipik Hatalar ve Kacinilmasi Gerekenler

```
Hata 1: GCC'yi bilesik egrilerle karistirmak
  YANLIS: GCC'nin yatay ekseni entalpi farki (bilesik egriler gibi)
  DOGRU:  GCC'nin yatay ekseni net isi akisi (duzeltilmis kaskad)

Hata 2: Utility'yi pinch kuralina aykiri yerlestirmek
  YANLIS: LP buhar'i pinch altinda kullanmak
  DOGRU:  Sicak utility yalnizca pinch ustu, soguk utility yalnizca pinch alti

Hata 3: CHP'yi pinch uzerinden yerlestirmek
  YANLIS: CHP atik isisini pinch altinda kullanmak
  DOGRU:  CHP atik isisini yalnizca pinch ustunde kullanmak

Hata 4: Isi cebini utility ihtiyaci olarak saymak
  YANLIS: Isi cebi buyuklugunu QH,min veya QC,min'e eklemek
  DOGRU:  Isi cebi ic isi degisimi ile karsilanir, utility'yi etkilemez

Hata 5: Exergy'yi goz ardi etmek
  YANLIS: Tum isi ayni kalitede kabul etmek
  DOGRU:  Exergy GCC ile utility kalitesini degerlendirmek

Hata 6: Sicaklik kaydirmasini unutmak
  YANLIS: GCC'de gercek sicakliklari kullanmak
  DOGRU:  GCC her zaman kaydirilmis sicakliklari (T*) kullanir
```

### 8.5 GCC Okumanin Hizli Kontrol Listesi

```
GCC Okuma Kontrol Listesi:

[ ] Ust uc noktayi oku: T* ve R -> QH,min
[ ] Alt uc noktayi oku: T* ve R -> QC,min
[ ] Pinch noktasini bul: R = 0 olan T*
[ ] Pinch ustu profili incele: Genis mi (cok utility gerekli) dar mi?
[ ] Pinch alti profili incele: Isi cebi var mi?
[ ] Burun/cep bolgelerini isle: Ic isi degisimi potansiyeli
[ ] Utility seviyelerini yerlesatir: En dusuk maliyetli kombinasyon
[ ] CHP potansiyelini degerlendir: Pinch ustu genis bolge var mi?
[ ] Isi pompasi potansiyelini degerlendir: Pinch etrafinda dar bolge var mi?
[ ] Exergy GCC ile karsilastir: Utility kalitesi uygun mu?
```

---

## İlgili Dosyalar

- [Pinch Analizi Indeks](INDEX.md) -- Navigasyon haritasi ve yukleme kurallari
- [Temel Kavramlar](fundamentals.md) -- Linnhoff metodolojisi ve altin kurallar
- [Bilesik Egriler](composite_curves.md) -- Hot/Cold composite curve olusturma
- [Problem Tablosu](problem_table.md) -- PTA algoritmasi ve kaskad hesaplari
- [Utility Sistemleri](utility_systems.md) -- Coklu utility seviyeleri ve CHP detaylari
- [HEN Tasarimi](hen_design.md) -- Grid diyagrami ve esanjor agi tasarimi
- [Hedefleme](targeting.md) -- Enerji, alan ve maliyet hedefleri
- [Pinch Analizi Ana Dosyasi](../pinch_analysis.md) -- Temel kavramlar ve hesaplamalar
- [Isi Entegrasyonu](../heat_integration.md) -- Kaynak-kullanim eslestirme
- [Capraz Ekipman](../cross_equipment.md) -- Ekipmanlar arasi firsatlar
- [Exergy Temelleri](../exergy_fundamentals.md) -- Exergy hesap ve denge ilkeleri
- [Utility Analizi](../utility_analysis.md) -- Utility sistemleri detay analizi

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, Rugby, UK, 1994 (2nd ed.)
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," Butterworth-Heinemann, 2nd Edition, 2007
- Smith, R., "Chemical Process Design and Integration," Wiley, 2nd Edition, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Townsend, D.W. & Linnhoff, B., "Heat and Power Networks in Process Design," AIChE Journal, 29(5), 742-771, 1983
- Linnhoff, B. & Dhole, V.R., "Shaftwork Targets for Low-Temperature Process Design," Chemical Engineering Science, 47(8), 2081-2091, 1992
- Feng, X. & Zhu, X.X., "Combining Pinch and Exergy Analysis for Process Modifications," Applied Thermal Engineering, 17(3), 249-261, 1997
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing, 1995
