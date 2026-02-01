---
title: "Exergy Akis Analizi ve Grassmann Diyagramlari (Exergy Flow Analysis and Grassmann Diagrams)"
category: factory
equipment_type: factory
keywords: [exergy akış, Grassmann, yıkım]
related_files: [factory/energy_flow_analysis.md, factory/exergy_fundamentals.md, factory/system_boundaries.md]
use_when: ["Exergy akış analizi yapılırken", "Exergy yıkım noktaları belirlenirken"]
priority: medium
last_updated: 2026-01-31
---
# Exergy Akis Analizi ve Grassmann Diyagramlari (Exergy Flow Analysis and Grassmann Diagrams)

> Son güncelleme: 2026-01-31

## Genel Bakis

Exergy akis analizi, enerji akis analizinin otesine gecerek enerji kalitesini ve gercek termodinamik kayiplari ortaya koyan ileri duzey bir denetim aracidir. Sankey diyagraminin exergy versiyonu olan Grassmann diyagramlari, tersinmezlik (irreversibility) kaynakli exergy yikimini gorsel olarak haritalandirir. Bu analiz, enerji analizinde gorunmeyen ancak gercek iyilestirme potansiyelini gosteren kayiplari aciga cikarir: yanma tersinmezligi, isi transferi tersinmezligi, karisim kayiplari ve kisma kayiplari.

Bu dosya; exergy akis haritalama metodolojisi, Grassmann diyagram insasi, fabrika alt sistemlerinde tersinmezlik haritalamasi, enerji ile exergy akislarinin karsilastirilmasi, exergy yikim selalesi (waterfall) analizi ve iyilestirme potansiyeli belirleme yontemlerini kapsar.

## 1. Exergy Akis Haritalama Metodolojisi (Exergy Flow Mapping Methodology)

### 1.1 Temel Prensip

Exergy dengesi, enerji dengesinden farkli olarak korunum saglamaz. Termodinamigin ikinci yasasi geregi exergy her gercek proseste yikilir:

```
Ex_giris = Ex_urun + Ex_atik + Ex_yikim

Burada:
- Ex_giris  = Toplam exergy girisi [kW]
- Ex_urun   = Faydali urun exergisi [kW]
- Ex_atik   = Atik akislarin exergisi (geri kazanilabilir) [kW]
- Ex_yikim  = Tersinmezlik kaynakli exergy yikimi [kW]
             = T0 x S_gen (Gouy-Stodola teoremi)

Not: Ex_yikim her zaman > 0'dir (tersinir proses haricinde).
Bu, exergy analizinin enerji analizinden temel farkidir.
```

### 1.2 Exergy Akis Haritalama Adimlari

```
Adim 1: Enerji dengesini kur (bkz. energy_flow_analysis.md)
Adim 2: Referans cevre kosullarini (olu durum) tanimla
         T0 = 25 C = 298.15 K, P0 = 101.325 kPa
Adim 3: Her enerji akisi icin exergy degerini hesapla
Adim 4: Alt sistem bazinda exergy dengelerini kur
Adim 5: Her alt sistemdeki exergy yikimini hesapla
Adim 6: Grassmann diyagramini ciz
Adim 7: Exergy yikim selalesi (waterfall) analizi yap
Adim 8: Kacinilabilir vs. kacinilmaz exergy yikimini ayir
Adim 9: Iyilestirme potansiyelini belirle ve onceliklendir
```

### 1.3 Exergy Hesaplama Formulleri (Akis Turleri Icin)

```
1. Yakit exergisi:
   Ex_yakit = m_dot_yakit x phi x LHV [kW]

   Burada:
   - phi = kimyasal exergy/LHV orani
   - Dogalgaz: phi = 1.04
   - Fuel oil: phi = 1.06
   - Komur: phi = 1.06-1.10
   - Biyokutle: phi = 1.10-1.25

2. Elektrik exergisi:
   Ex_elektrik = W_elektrik [kW]
   (Elektrik saf exerjidir, donusum orani = 1.00)

3. Isil akis exergisi (sabit sicaklik kaynagi):
   Ex_Q = Q x (1 - T0/T_kaynak) [kW]

   Burada:
   - Q = isi akisi [kW]
   - T_kaynak = kaynak sicakligi [K]
   - T0 = referans sicaklik [K]

4. Madde akisi fiziksel exergisi:
   ex_fiz = (h - h0) - T0 x (s - s0) [kJ/kg]
   Ex_fiz = m_dot x ex_fiz [kW]

5. Basingli gaz exergisi (ideal gaz):
   ex_basinc = R x T0 x ln(P/P0) [kJ/kg]

   Burada:
   - R = gaz sabiti (hava: 0.287 kJ/kgK)
   - P = gaz basinci [kPa]
   - P0 = referans basinc (101.325 kPa)

6. Sogutma exergisi (T < T0):
   Ex_sogutma = Q_sogutma x |1 - T0/T_sogutma| [kW]

   Not: Sogutma exergisi dusuktur cunku T0'a yakin sicakliklarda
   Carnot carpani cok kucuktur.
```

## 2. Grassmann Diyagrami Insasi (Grassmann Diagram Construction)

### 2.1 Grassmann vs. Sankey Karsilastirmasi

| Parametre | Sankey (Enerji) | Grassmann (Exergy) |
|---|---|---|
| Dayandigi yasa | 1. yasa (enerji korunumu) | 2. yasa (exergy yikimi) |
| Toplam | Giris = cikis (korunum) | Giris > cikis (yikim) |
| Atik isi gorunumu | Buyuk (%20-40) | Kucuk (%3-10) |
| Yanma kaybi | Gorunmez (%0) | En buyuk kayip (%15-30) |
| Isi transferi kaybi | Gorunmez | Onemli (%5-15) |
| Dusuk sicaklik isi | Degerli gorunur | Degersiz gorunur |
| Elektrik | Diger enerji ile ayni agirlik | Yuksek kalite (saf exergy) |
| Pratik fayda | Miktar dengesi | Kalite + iyilestirme hedefi |

### 2.2 Grassmann Diyagrami Olusturma Kurallari

```
1. Ok genisligi exergy buyuklugu ile orantili olmalidir
2. Toplam cikis < toplam giris (exergy korunmaz)
3. Exergy yikimi ok genisliginin azalmasi ile gosterilir
4. Yikim noktalari acikca isaretlenmeli (I_k = T0 x S_gen)
5. Atik exergy (geri kazanilabilir) ayri gosterilmeli
6. Renk kodlamasi:
   - Yakit exergisi:     ████ Koyu kirmizi
   - Elektrik exergisi:  ████ Koyu mavi
   - Urun exergisi:      ████ Yesil
   - Exergy yikimi:      ████ Siyah/koyu gri
   - Atik exergy:        ████ Acik gri
```

### 2.3 Tipik Fabrika Grassmann Diyagrami (ASCII)

```
YAKIT EXERGY (%68) ═══════════════════════════════════════════╗
                                                               ║
ELEKTRIK EXERGY (%30) ═══════════════════════════════════╗     ║
                                                          ║     ║
HAMMADDE EXERGY (%2) ═══════════════════════════════╗    ║     ║
                                                     ║    ║     ║
                    ╔════════════════════════════════╩════╩═════╣
                    ║    TOPLAM EXERGY GIRISI (%100)            ║
                    ╠══════════════════════════════════════════╝
                    ║
                    ║──── Yanma tersinmezligi (%18-25) ─────→ ██ YIKIM
                    ║
                    ║──── Isi transfer tersinmezligi (%10-18) → ██ YIKIM
                    ║
                    ║──── Baca gazi exergisi (%5-12) ────────→ ░░ ATIK
                    ║
                    ║──── Kompressor tersinmezligi (%3-8) ──→ ██ YIKIM
                    ║
                    ║──── Sogutma tersinmezligi (%2-5) ─────→ ██ YIKIM
                    ║
                    ║──── Motor/pompa tersinmezligi (%2-5) ─→ ██ YIKIM
                    ║
                    ║──── Karisim/kisma kayiplari (%1-3) ───→ ██ YIKIM
                    ║
                    ║──── Sogutma/dagilim atik (%2-5) ──────→ ░░ ATIK
                    ║
                    ╠═════════════════════════════════╗
                    ║  URUN EXERGY (%20-40)           ║
                    ║  (buhar + hava + sogutma + urun) ║
                    ╚═════════════════════════════════╝

TOPLAM YIKIM: %40-65 (tersinmezlik, geri kazanilamaz)
TOPLAM ATIK EXERGY: %7-17 (kismi geri kazanim mumkun)
URUN EXERGY: %20-40 (faydali cikis)
```

## 3. Alt Sistem Exergy Analizi (Subsystem Exergy Analysis)

### 3.1 Kazan/Buhar Sistemi Exergy Analizi

```
Kazan exergy dengesi:
Ex_yakit + Ex_hava + Ex_besleme_su = Ex_buhar + Ex_baca + Ex_yuzey + I_kazan

Exergy verimi:
eta_ex_kazan = (Ex_buhar - Ex_besleme) / Ex_yakit

Tersinmezlik bilesenleri:
I_yanma = T0 x S_gen_yanma ≈ 0.25-0.30 x Ex_yakit
I_isi_transfer = T0 x S_gen_isi ≈ 0.15-0.25 x Ex_yakit
I_karisim = T0 x S_gen_mix ≈ 0.01-0.03 x Ex_yakit

Tipik kazan exergy performansi:
| Parametre          | Dusuk  | Ortalama | Iyi    | Mukemmel |
|--------------------|--------|----------|--------|----------|
| eta_ex [%]         | <25    | 25-35    | 35-42  | >42      |
| I_yanma/Ex_yakit   | >0.30  | 0.27-0.30| 0.25-0.27| <0.25  |
| T_baca [C]         | >250   | 180-250  | 130-180| <130     |
| Hava fazlaligi [%] | >30    | 15-30    | 10-15  | <10      |

Detayli hesaplamalar icin bkz. ../boiler/formulas.md
```

### 3.2 Kompressor/Basingli Hava Sistemi Exergy Analizi

```
Kompressor exergy dengesi:
W_kompressor = Ex_hava_cikis - Ex_hava_giris + Q_sogutma x (1 - T0/T_atik) + I_komp

Exergy verimi:
eta_ex_komp = Ex_hava / W_kompressor
            = m_dot x R x T0 x ln(P2/P1) / W_kompressor

Tersinmezlik bilesenleri:
I_sikistirma = W_komp - (Ex_hava_cikis - Ex_hava_giris) - Ex_Q_atik
I_kacak = m_dot_kacak x ex_hava (basincli)
I_basinc_dusus = m_dot x R x T0 x ln(P_komp/P_kullanim) (boru kaybi)

Tipik kompressor exergy performansi:
| Parametre          | Kritik | Dusuk  | Ortalama | Iyi    | Mukemmel |
|--------------------|--------|--------|----------|--------|----------|
| eta_ex [%]         | <8     | 8-12   | 12-18    | 18-25  | >25      |
| Kacak orani [%]    | >35    | 25-35  | 15-25    | 5-15   | <5       |
| SPC [kW/(m3/min)]  | >8.0   | 7.0-8.0| 5.5-7.0  | 4.5-5.5| <4.5    |

Detayli hesaplamalar icin bkz. ../compressor/formulas.md
```

### 3.3 Chiller/Sogutma Sistemi Exergy Analizi

```
Chiller exergy dengesi:
W_kompressor = Ex_sogutma + Ex_kondenser_atik + I_chiller

Sogutma exergisi:
Ex_sogutma = Q_sogutma x |1 - T0/T_sogutma|

Ornek:
- Q_sogutma = 500 kW, T_sogutma = 280 K (7 C), T0 = 298 K
- Ex_sogutma = 500 x |1 - 298/280| = 500 x 0.064 = 32.1 kW

Exergy verimi:
eta_ex_chiller = Ex_sogutma / W_kompressor

Tersinmezlik bilesenleri:
I_sikistirma_chiller ≈ 0.25-0.40 x W_komp
I_kisma (genlestirme vanasi) ≈ 0.15-0.25 x W_komp
I_evaporator ≈ 0.05-0.15 x W_komp
I_kondenser ≈ 0.05-0.10 x W_komp

Tipik chiller exergy performansi:
| Parametre          | Kritik | Dusuk  | Ortalama | Iyi    | Mukemmel |
|--------------------|--------|--------|----------|--------|----------|
| eta_ex [%]         | <12    | 12-18  | 18-28    | 28-38  | >38      |
| COP                | <3.0   | 3.0-4.0| 4.0-5.5  | 5.5-6.5| >6.5    |
| kW/TR              | >1.2   | 0.9-1.2| 0.65-0.9 | 0.5-0.65| <0.5   |

Detayli hesaplamalar icin bkz. ../chiller/formulas.md
```

### 3.4 Pompa Sistemi Exergy Analizi

```
Pompa exergy dengesi:
W_pompa_elektrik = Ex_su_cikis - Ex_su_giris + I_pompa_toplam

Exergy verimi:
eta_ex_pompa = (Ex_su_cikis - Ex_su_giris) / W_elektrik
             = m_dot x v x (P2 - P1) / W_elektrik
             = eta_pompa x eta_motor

Tersinmezlik bilesenleri:
I_motor = W_elektrik x (1 - eta_motor)
I_pompa = W_saft x (1 - eta_pompa)
I_boru = m_dot x v x DP_boru (surtunme kaybi)
I_vana = m_dot x v x DP_vana (kisma kaybi)

Tipik pompa sistemi exergy performansi:
| Parametre          | Kritik | Dusuk  | Ortalama | Iyi    | Mukemmel |
|--------------------|--------|--------|----------|--------|----------|
| eta_ex_sistem [%]  | <25    | 25-35  | 35-50    | 50-65  | >65      |
| eta_pompa [%]      | <50    | 50-65  | 65-78    | 78-88  | >88      |
| eta_motor [%]      | <85    | 85-90  | 90-93    | 93-96  | >96      |

Detayli hesaplamalar icin bkz. ../pump/formulas.md
```

### 3.5 HVAC Sistemi Exergy Analizi

```
HVAC exergy dengesi:
W_HVAC = Ex_isitma + Ex_sogutma + Ex_fan + I_HVAC

Isitma exergisi (kaloriferde):
Ex_isitma = Q_isitma x (1 - T0/T_ic_ortam)

Not: Bina isitmasinda T_ic = ~293-295 K, T0 = 273-288 K (kis)
Carnot carpani cok dusuktur → exergy verimi cok dusuktur
Dogalgaz ile isitmanin exergy verimi tipik %5-8

Sogutma exergisi:
Ex_sogutma_HVAC = Q_sogutma x |1 - T0/T_ic|

Tipik HVAC exergy performansi:
| Parametre          | Kritik | Dusuk  | Ortalama | Iyi    | Mukemmel |
|--------------------|--------|--------|----------|--------|----------|
| eta_ex_isitma [%]  | <3     | 3-5    | 5-8      | 8-12   | >12      |
| eta_ex_sogutma [%] | <8     | 8-15   | 15-25    | 25-35  | >35      |
| eta_ex_HVAC [%]    | <5     | 5-10   | 10-15    | 15-22  | >22      |
```

## 4. Enerji vs. Exergy Akis Karsilastirmasi (Energy vs. Exergy Comparison)

### 4.1 Tipik Fabrika Icin Karsilastirma

```
ENERJI AKISI (1. Yasa):
═════════════════════════════════════════════
Giris:   Yakit %65 + Elektrik %35 = %100
Cikis:   Faydali %70 + Kayip %30 = %100
Verim:   %70 (iyi gorunuyor!)

EXERGY AKISI (2. Yasa):
═════════════════════════════════════════════
Giris:   Yakit Ex %68 + Elektrik Ex %30 + Diger %2 = %100
Cikis:   Faydali Ex %28 + Yikim %55 + Atik Ex %17 = %100
Verim:   %28 (gercek performans!)
```

### 4.2 Alt Sistem Bazinda Karsilastirma Tablosu

| Alt Sistem | Enerji Verimi [%] | Exergy Verimi [%] | Fark | Aciklama |
|---|---|---|---|---|
| Kazan (buhar) | 85-92 | 25-42 | ~50 puan | Yanma + isi transfer tersinmezligi |
| Kompressor | 75-90 (izentropik) | 10-25 | ~60 puan | Sikistirma tersinmezligi |
| Chiller (COP/Carnot) | 40-65 (2. yasa) | 15-38 | ~30 puan | Kisma + isi transfer |
| Pompa sistemi | 55-85 | 35-65 | ~20 puan | Motor + pompa kayiplari |
| Bina isitma (gaz) | 85-95 | 5-12 | ~80 puan | En buyuk fark — kalite uyumsuzlugu |
| Elektrik motoru | 88-96 | 85-93 | ~3 puan | En kucuk fark — elektrik saf exergy |
| Isik (LED) | 30-50 (lumen/W) | 25-40 | ~10 puan | Isik dusuk exergy icermez |

### 4.3 Onemli Cikarimlar

```
1. Enerji verimi yuksek olsa bile exergy verimi dusuk olabilir
   Ornek: Kazan %90 enerji verimi, %30 exergy verimi
   → Enerjinin %90'i korunuyor ama kalitenin %70'i yok ediliyor

2. Dusuk sicaklik isitma en buyuk exergy savurganligi
   → Yuksek kaliteli yakit (1,500 C alev) ile dusuk kaliteli is (80 C su)
   → Isi pompasi veya atik isi kullanimi cok daha verimli

3. Elektrikli sistemler enerji ve exergy verimi yakin
   → Elektrik saf exergy oldugu icin iki analiz benzer sonuc verir
   → Motorlar, pompalar, fanlar icin enerji analizi yeterli olabilir

4. Sogutma exergisi cok dusuktur
   → 500 kW sogutma yuku ≈ 30-40 kW exergy
   → Chiller COP 5.0 olsa bile exergy verimi %25-35
```

## 5. Exergy Yikim Selalesi Analizi (Exergy Destruction Waterfall Analysis)

### 5.1 Waterfall (Selale) Diyagrami Kavrami

```
Exergy yikim selalesi, toplam exergy girisinden baslayarak
her alt sistemdeki yikimi kademeli olarak gosteren bir grafiktir:

Ex_giris ─┐
          │ -I_yanma
          ├─────────────────────────────────────────┐
          │                                          │
          │ -I_isi_transfer                          │
          ├──────────────────────────────┐           │
          │                              │           │
          │ -I_kompressor                │           │
          ├───────────────────────┐      │           │
          │                       │      │           │
          │ -I_chiller            │      │           │
          ├────────────────┐      │      │           │
          │                │      │      │           │
          │ -Ex_atik_baca  │      │      │           │
          ├──────────┐     │      │      │           │
          │          │     │      │      │           │
          │ -Diger   │     │      │      │           │
          ├────┐     │     │      │      │           │
          │    │     │     │      │      │           │
          │    v     v     v      v      v           │
          │  Ex_urun                                 │
          └──────────────────────────────────────────┘

Yukaridan asagiya her kademe bir kayip kaynagini temsil eder.
En buyuk kaynaklar en uste konumlandirilir.
```

### 5.2 Waterfall Analizi Uygulama

```
Fabrika geneli exergy yikim selalesi (ornek):

| Kademe | Aciklama               | Exergy [kW] | Kumulatif Kayip [%] |
|--------|------------------------|-------------|---------------------|
| 0      | Toplam exergy girisi   | 5,800       | 0                   |
| 1      | (-) Yanma tersinmezlik | -1,450      | 25.0                |
| 2      | (-) Isi transfer tersn.| -870        | 40.0                |
| 3      | (-) Baca gazi exergisi | -348        | 46.0                |
| 4      | (-) Kompressor tersn.  | -464        | 54.0                |
| 5      | (-) Chiller tersinmez. | -232        | 58.0                |
| 6      | (-) Pompa tersinmez.   | -116        | 60.0                |
| 7      | (-) Buhar dagilim kaybi| -290        | 65.0                |
| 8      | (-) Hava kacagi        | -87         | 66.5                |
| 9      | (-) Diger kayiplar     | -203        | 70.0                |
| Son    | = Urun exergisi        | 1,740       | —                   |

Exergy verimi: 1,740 / 5,800 = %30.0
```

## 6. Iyilestirme Potansiyeli Belirleme (Improvement Potential Identification)

### 6.1 Van Gool Iyilestirme Potansiyeli

```
IP_k = (1 - eta_ex_toplam) x I_k [kW]

Burada:
- IP_k = k-inci bilesenin iyilestirme potansiyeli [kW]
- eta_ex_toplam = fabrika toplam exergy verimi
- I_k = k-inci bilesenin exergy yikimi [kW]

Ornek (yukaridaki fabrika, eta_ex = 0.30):
IP_yanma = (1 - 0.30) x 1,450 = 1,015 kW
IP_isi_transfer = (1 - 0.30) x 870 = 609 kW
IP_kompressor = (1 - 0.30) x 464 = 325 kW

En yuksek IP degeri, en yuksek iyilestirme onceligi demektir.
```

### 6.2 Kacinilabilir vs. Kacinilmaz Exergy Yikimi

```
I_toplam = I_kacinilmaz + I_kacinilabilir

I_kacinilmaz: Teknolojik ve fiziksel sinirlar nedeniyle azaltilamaz
I_kacinilabilir: Muhendislik mudahalesi ile azaltilabilir

| Kayip Kaynagi          | I_kacinilmaz [%] | I_kacinilabilir [%] | Azaltma Yontemi          |
|------------------------|-------------------|---------------------|--------------------------|
| Yanma tersinmezligi    | %20-25            | %3-8                | Hava on isitma, O2 zen.  |
| Isi transfer tersn.    | %8-12             | %5-10               | Buyuk esanjoer, pinch    |
| Baca gazi kaybi        | %2-3              | %3-10               | Ekonomizer, yogusma      |
| Kompressor kaybi       | %5-8              | %10-20              | VSD, soguk emis, kademe  |
| Chiller kaybi          | %8-12             | %5-15               | Degisken hiz, serbest s. |
| Pompa kaybi            | %3-5              | %5-15               | VSD, boyutlandirma       |
| Kacak/izolasyon        | %0                | %100                | Bakim, onarim, izolasyon |
```

### 6.3 Onceliklendirme Matrisi

```
                    Kolay Uygulama          Zor Uygulama
                ┌─────────────────────┬─────────────────────┐
                │  QUICK WIN          │  STRATEJIK           │
   Yuksek       │  1. Kacak onarimi   │  7. Pinch entegrasyon│
   Tasarruf     │  2. Kapan tamiri    │  8. CHP/kojenerasyon │
                │  3. Izolasyon       │  9. Proses degisimi  │
                ├─────────────────────┼─────────────────────┤
                │  DUSUK MEYVE       │  UZUN VADELI         │
   Dusuk        │  4. Basinc optimiz. │  10. Ekipman yenileme│
   Tasarruf     │  5. Set-point ayari │  11. Bina iyilestirme│
                │  6. Calisma prosedur│  12. Alternatif enerji│
                └─────────────────────┴─────────────────────┘

Uygulama sirasi: Quick Win → Dusuk Meyve → Stratejik → Uzun Vadeli
```

## 7. Tam Fabrika Exergy Akis Analizi Ornegi (Complete Worked Example)

### 7.1 Senaryo

Orta olcekli tekstil fabrikasi (iplik ve dokuma):
- Dogalgaz: 400 Nm3/h (LHV = 34.5 MJ/Nm3)
- Elektrik: 950 kW
- Buhar: 5 ton/h (10 bar, doymus)
- Basingli hava: 12 m3/min (7 bar)
- Sogutma: 250 kW (7 C chilled water)
- Proses sicak su: 80 C, 3 m3/h
- Calisma: 6,500 saat/yil
- T0 = 25 C = 298.15 K, P0 = 101.325 kPa

### 7.2 Exergy Giris Hesabi

```
1. Yakit exergisi:
   Q_yakit = 400/3,600 x 34,500 = 3,833 kW (enerji)
   Ex_yakit = 3,833 x 1.04 = 3,987 kW

2. Elektrik exergisi:
   Ex_elektrik = 950 kW (saf exergy)

3. Besleme suyu exergisi (25 C, ihmal edilir):
   Ex_besleme ≈ 0 kW

4. Toplam exergy girisi:
   Ex_giris = 3,987 + 950 = 4,937 kW

   Exergy dagilimi:
   - Yakit: 3,987 / 4,937 = %80.8
   - Elektrik: 950 / 4,937 = %19.2
```

### 7.3 Alt Sistem Exergy Analizleri

```
A) KAZAN SISTEMI:
   Yakit exergisi girisi: Ex_yakit = 3,987 kW

   Buhar exergisi (10 bar doymus, ex = 858 kJ/kg):
   Ex_buhar = (5,000/3,600) x (858 - 28.8) = 1,152 kW

   Baca gazi exergisi (T_baca = 195 C):
   Ex_baca = m_dot_bg x [(h-h0) - T0(s-s0)] ≈ 218 kW

   Yuzey kaybi exergisi (T_yuzey = 60 C ortalama):
   Ex_yuzey = Q_yuzey x (1 - 298/333) ≈ 86 x 0.105 = 9 kW

   Kazan exergy yikimi:
   I_kazan = 3,987 - 1,152 - 218 - 9 = 2,608 kW

   Kazan exergy verimi:
   eta_ex_kazan = 1,152 / 3,987 = %28.9

   Alt bilesenlere ayirma:
   - Yanma tersinmezligi: I_yanma ≈ 0.27 x 3,987 = 1,076 kW
   - Isi transfer tersinmezligi: I_HT ≈ 2,608 - 1,076 = 1,532 kW

B) KOMPRESSOR SISTEMI:
   Elektrik girisi: W_komp = 180 kW

   Hava exergisi (7 bar, 25 C):
   Ex_hava = (12/60 x 1.225) x 0.287 x 298.15 x ln(8.013/1.013)
   Ex_hava = 0.245 x 0.287 x 298.15 x 2.069 = 43.4 kW

   Atik isi exergisi (T_atik = 85 C):
   Q_atik ≈ 180 x 0.75 = 135 kW
   Ex_atik_isi = 135 x (1 - 298/358) = 135 x 0.168 = 22.6 kW

   Kompressor exergy yikimi:
   I_komp = 180 - 43.4 - 22.6 = 114 kW

   Kacak kaybi (kacak orani %20):
   I_kacak = 43.4 x 0.20 = 8.7 kW

   Kompressor exergy verimi:
   eta_ex_komp = 43.4 / 180 = %24.1

C) CHILLER SISTEMI:
   Elektrik girisi: W_chiller = 75 kW
   Q_sogutma = 250 kW, T_sogutma = 280.15 K

   Sogutma exergisi:
   Ex_sogutma = 250 x |1 - 298.15/280.15| = 250 x 0.064 = 16.1 kW

   Chiller exergy yikimi:
   I_chiller = 75 - 16.1 = 58.9 kW

   Chiller exergy verimi:
   eta_ex_chiller = 16.1 / 75 = %21.4

D) POMPA SISTEMI:
   Elektrik girisi: W_pompa = 85 kW
   Faydali hidrolik is: W_hidrolik = 85 x 0.55 = 46.8 kW

   Pompa sistemi exergy yikimi:
   I_pompa = 85 - 46.8 = 38.2 kW

   Pompa exergy verimi:
   eta_ex_pompa = 46.8 / 85 = %55.0

E) PROSES MOTORLARI:
   Elektrik girisi: W_motor = 480 kW
   Faydali mekanik is: W_mek = 480 x 0.90 = 432 kW

   Motor exergy yikimi:
   I_motor = 480 - 432 = 48 kW

   Motor exergy verimi:
   eta_ex_motor = 432 / 480 = %90.0

F) BUHAR DAGILIM:
   Buhar exergisi (kazandan): Ex_buhar = 1,152 kW
   Dagilim kaybi (izolasyon, kapan, kondensat):
   I_dagilim = 1,152 x 0.12 = 138 kW
   Kullaniciya ulasan: Ex_buhar_net = 1,152 - 138 = 1,014 kW

G) AYDINLATMA VE DIGER:
   Elektrik: W_diger = 130 kW
   Faydali cikis: ~45 kW
   I_diger = 85 kW
```

### 7.4 Fabrika Geneli Exergy Dengesi Ozet

| Kalem | Exergy [kW] | Pay [%] | Kategori |
|---|---|---|---|
| **GIRISLER** | | | |
| Yakit exergisi | 3,987 | 80.8 | Giris |
| Elektrik exergisi | 950 | 19.2 | Giris |
| **TOPLAM GIRIS** | **4,937** | **100.0** | |
| **FAYDALI CIKISLAR** | | | |
| Buhar exergisi (prosese) | 1,014 | 20.5 | Urun |
| Mekanik is | 432 | 8.8 | Urun |
| Hidrolik is (pompalar) | 46.8 | 0.9 | Urun |
| Basingli hava exergisi | 34.7 | 0.7 | Urun (kacak cikarilmis) |
| Sogutma exergisi | 16.1 | 0.3 | Urun |
| Diger faydali | 45 | 0.9 | Urun |
| **TOPLAM URUN** | **1,589** | **32.2** | |
| **EXERGY YIKIMI** | | | |
| Yanma tersinmezligi | 1,076 | 21.8 | Yikim |
| Isi transfer tersinmezligi | 1,532 | 31.0 | Yikim |
| Kompressor tersinmezligi | 114 | 2.3 | Yikim |
| Chiller tersinmezligi | 58.9 | 1.2 | Yikim |
| Pompa tersinmezligi | 38.2 | 0.8 | Yikim |
| Motor tersinmezligi | 48 | 1.0 | Yikim |
| Buhar dagilim kaybi | 138 | 2.8 | Yikim |
| Hava kacagi | 8.7 | 0.2 | Yikim |
| Diger tersinmezlik | 85 | 1.7 | Yikim |
| **TOPLAM YIKIM** | **3,099** | **62.8** | |
| **ATIK EXERGY** | | | |
| Baca gazi exergisi | 218 | 4.4 | Atik (geri kazanilabilir) |
| Kompressor atik isi exergisi | 22.6 | 0.5 | Atik (geri kazanilabilir) |
| Yuzey kaybi exergisi | 9 | 0.2 | Atik |
| **TOPLAM ATIK** | **250** | **5.1** | |

### 7.5 Sonuc ve Degerlendirilme

```
Fabrika exergy verimi:
eta_ex = 1,589 / 4,937 = %32.2

Karsilastirma:
- Enerji verimi: ~%82 (kazan + dagilim bazli)
- Exergy verimi: %32.2
- Fark: ~50 yuzde puan → Enerji analizi aldatici derecede iyimser

Enerji vs. Exergy karsilastirmasi:
| Gosterge            | Enerji Analizi | Exergy Analizi |
|---------------------|---------------|----------------|
| Fabrika verimi      | %82           | %32.2          |
| En buyuk kayip      | Baca gazi %5  | Yanma %21.8    |
| 2. buyuk kayip      | Dagilim %6    | Isi transfer %31.0 |
| Sogutma kaybi gorun.| Buyuk (%8)    | Kucuk (%1.2)   |
| Iyilestirme onceligi| Baca gazi geri kaz.| Isi entegrasyonu |

Exergy analizinin farkliligi:
- Yanma tersinmezligi enerji analizinde GORUNMEZ
- Isi transfer tersinmezligi enerji analizinde GORUNMEZ
- Sogutma "kaybi" enerji analizinde BUYUK, exergy'de KUCUK
- Gercek iyilestirme hedefleri tamamen farkli
```

### 7.6 Iyilestirme Onerileri (Exergy Bazli)

```
| Sira | Oneri                        | Exergy Tasarrufu [kW] | SPP [yil] |
|------|------------------------------|----------------------|-----------|
| 1    | Hava kacagi onarimi          | 8.7                  | 0.2       |
| 2    | Buhar kapani bakimi          | 50                   | 0.5       |
| 3    | Izolasyon iyilestirme        | 40                   | 1.2       |
| 4    | Economizer (baca gazi geri k.)| 100                  | 2.5       |
| 5    | Kompressor VSD + isi geri kaz.| 65                   | 2.0       |
| 6    | Chiller free cooling         | 25                   | 1.8       |
| 7    | Pompa VSD                    | 15                   | 2.8       |
| 8    | Pinch analizi isi entegrasyon| 200                  | 3.5       |
| 9    | Hava on isitma (yanma)       | 80                   | 4.0       |
| 10   | Kojenerasyon (CHP)           | 350                  | 5.0       |

Toplam iyilestirme potansiyeli: ~934 kW exergy
Potansiyel yeni exergy verimi: (1,589 + 934) / 4,937 = %51.1
```

## 8. Grassmann Diyagrami Raporlama (Reporting)

### 8.1 Raporlama Gereksinimleri

```
Grassmann diyagrami raporunda bulunmasi gerekenler:
1. Referans cevre kosullari (T0, P0)
2. Olcum tarih ve suresi
3. Tum akislarin exergy degerleri (kW ve %)
4. Alt sistem bazinda exergy verimleri
5. Exergy yikim dagilimi (tablo + grafik)
6. Enerji vs. exergy karsilastirmasi
7. Iyilestirme potansiyeli ozeti
8. Kacinilabilir vs. kacinilmaz ayirimi
9. Ekonomik degerlendirilme (bkz. economic_analysis.md)
```

### 8.2 Yaygin Hatalar

```
Exergy akis analizinde yaygin hatalar:
1. Referans sicakligin yanlis secilmesi (mevsimsel etki)
2. Kimyasal exerginin ihmal edilmesi (ozellikle yakitlarda)
3. Yanma tersinmezliginin hesaplanmamasi
4. Sogutma exergisinin enerji ile karistirilmasi
5. Elektrigin 1:1 exergy olmasi ilkesinin goz ardi edilmesi
6. Buhar exergisinin sicak su exergisi ile karistirilmasi
7. Negatif exergy transferi (sogutma altinda) yanlis isaretlenmesi
```

## İlgili Dosyalar

- [Enerji Akis Analizi](energy_flow_analysis.md) — Enerji dengesi ve Sankey diyagramlari
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy temel kavramlar ve fabrika dengesi
- [Kutle Dengesi](mass_balance.md) — Materyal akis analizi
- [Sistem Sinirlari](system_boundaries.md) — Kontrol hacimleri ve olcum noktalari
- [KPI Tanimlari](kpi_definitions.md) — Exergy verimlilik gostergeleri
- [Ekonomik Analiz](economic_analysis.md) — Yatirim degerlendirme yontemleri
- [Enerji Fiyatlandirma](energy_pricing.md) — Enerji maliyetleri
- [Kazan Formulleri](../boiler/formulas.md) — Kazan exergy hesaplamalari
- [Kazan Benchmarklari](../boiler/benchmarks.md) — Kazan exergy performans karsilastirmasi
- [Kompressor Formulleri](../compressor/formulas.md) — Kompressor exergy hesaplamalari
- [Kompressor Benchmarklari](../compressor/benchmarks.md) — Kompressor performans degerleri
- [Chiller Formulleri](../chiller/formulas.md) — Sogutma sistemi exergy hesaplamalari
- [Chiller Benchmarklari](../chiller/benchmarks.md) — Chiller performans degerleri
- [Pompa Formulleri](../pump/formulas.md) — Pompa sistemi exergy hesaplamalari

## Referanslar

- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 4th Edition, 2016
- Szargut, J., Morris, D.R., Steward, F.R., "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes," Hemisphere Publishing, 1988
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," Elsevier, 3rd Edition, 2021
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing, 1995
- Tsatsaronis, G. (2007), "Definitions and nomenclature in exergy analysis and exergoeconomics," Energy, 32(4), 249-253
- Rosen, M.A. & Dincer, I. (2003), "Exergy-cost-energy-mass analysis of thermal systems and processes," Energy Conversion and Management, 44(10), 1633-1651
- Sciubba, E. & Wall, G. (2007), "A brief commented history of exergy from the beginnings to 2004," Int. J. of Thermodynamics, 10(1), 1-26
- Grassmann, P. (1950), "Zur allgemeinen Definition des Wirkungsgrades," Chemie Ingenieur Technik, 22(4), 77-80
- Cornelissen, R.L. (1997), "Thermodynamics and Sustainable Development," PhD Thesis, University of Twente
- Rosen, M.A. (2002), "Assessing energy technologies and environmental impacts with the principles of thermodynamics," Applied Energy, 72(1), 427-441
