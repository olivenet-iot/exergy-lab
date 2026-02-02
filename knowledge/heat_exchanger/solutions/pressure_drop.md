---
title: "Basinc Dususu Azaltma (Pressure Drop Reduction)"
category: solution
equipment_type: heat_exchanger
keywords: [basinc dususu, pressure drop, pompa enerjisi, baffle, DP, exergy kaybi]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/audit.md]
use_when: ["Basinc dususu tasarim degerini astiginda", "Pompa/fan enerji tuketimi yuksek oldugunda", "Basinc dususu kaynakli exergy kaybi analiz edilirken"]
priority: medium
last_updated: 2026-02-01
---
# Basinc Dususu Azaltma (Pressure Drop Reduction)

> Son guncelleme: 2026-02-01

## Ozet

**Problem:** Isi esanjorlerinde basinc dususu (pressure drop, DP), akiskani sirkule ettiren pompa veya fanlarin enerji tuketimini dogrudan arttirir. Asiri basinc dususu hem isletme maliyetini yukselterek hem de akiskan exergisini azaltarak onemli bir exergy yikim kaynagi olusturur. Kirlenme, hatali tasarim, asiri boru gecis sayisi veya yetersiz baffle araligi gibi nedenlerle basinc dususu tasarim degerinin cok uzerine cikabilir.

**Cozum:** Basinc dususu kaynaklarini analiz ederek baffle dizayni, boru gecis sayisi, paralel esanjor duzenlemesi ve akis optimizasyonu ile DP'yi azaltmak.

**Tipik Tasarruf:** %10-40 (pompa/fan enerji tuketiminde azalma)
**Tipik ROI:** 1-3 yil

## Basinc Dususu Hesaplama Formulleri

### Boru Tarafi Basinc Dususu (Tube Side Pressure Drop)

```
DP_tube = DP_friction + DP_return + DP_nozzle

DP_friction = N_p x [f x (L/d_i) x (rho x v^2 / 2)]  [Pa]
DP_return = N_p x 4 x (rho x v^2 / 2)  [Pa]  (donus kayiplari)
DP_nozzle = 1.5 x (rho x v_n^2 / 2)  [Pa]  (giris + cikis nozul)

Burada:
  N_p   = Boru gecis sayisi [-]
  f     = Darcy sürtünme faktoru [-]
  L     = Boru uzunlugu [m]
  d_i   = Boru ic capi [m]
  rho   = Akiskan yogunlugu [kg/m3]
  v     = Boru ici ortalama akis hizi [m/s]
  v_n   = Nozul hizi [m/s]
```

Tipik boru tarafi basinc dususu araliklari:

| Akiskan | Tipik DP Araligi (kPa) | Maksimum Izin Verilen DP (kPa) |
|---------|------------------------|-------------------------------|
| Su (sogutma suyu) | 30-70 | 100 |
| Su (kazan besleme) | 50-150 | 200 |
| Organik solvent | 30-70 | 100 |
| Yag (dusuk viskozite) | 50-150 | 200 |
| Yag (yuksek viskozite) | 100-300 | 400 |
| Gaz (dusuk basinc) | 1-5 | 10 |
| Gaz (yuksek basinc) | 10-50 | 100 |
| Buhar | 5-30 | 50 |

### Govde Tarafi Basinc Dususu (Shell Side Pressure Drop)

#### Kern Yontemi (Basitlesetirilmis)

```
DP_shell = f_s x D_s x (N_b + 1) x rho x v_s^2 / (2 x d_e)  [Pa]

Burada:
  f_s   = Govde tarafi surtunme faktoru [-]
  D_s   = Govde ic capi [m]
  N_b   = Baffle sayisi [-]
  v_s   = Govde tarafi ortalama akis hizi [m/s]
  d_e   = Esdefer cap (equivalent diameter) [m]
```

#### Bell-Delaware Yontemi (Detayli)

Bell-Delaware yontemi, Kern yonteminin iyilestirilmis versiyonudur ve kacak akimlari dikkate alir:

```
DP_shell = DP_crossflow + DP_window + DP_nozzle

DP_crossflow = N_b x DP_ideal_crossflow x R_b x R_l
DP_window = N_b x DP_ideal_window x R_l
DP_nozzle = 2 x DP_ideal_nozzle

Duzeltme faktorleri:
  R_b = Bypass akimi duzeltme faktoru (0.5-1.0)
  R_l = Kacak akimi duzeltme faktoru (0.4-0.8)
```

**Not:** Gercek govde tarafi basinc dususu, Kern yonteminin %50-200'u arasinda olabilir. Hassas hesap icin Bell-Delaware veya HTRI/HTFS yazilimi kullanilmalidir.

### Plakali Esanjor Basinc Dususu

```
DP_plate = f_p x (L_p / d_h) x (rho x v^2 / 2) x N_pass + 1.3 x (rho x v_port^2 / 2)  [Pa]

Burada:
  f_p    = Plaka surtunme faktoru [-] (duz plaka: 0.5-5, oluklu plaka: 1-15)
  L_p    = Plaka etkin uzunlugu [m]
  d_h    = Hidrolik cap [m] (tipik 2-5 mm)
  v      = Kanal ici akis hizi [m/s]
  N_pass = Gecis sayisi [-]
  v_port = Port hizi [m/s]
```

## Basinc Dususunun Exergy Maliyeti

Basinc dususu akiskanin mekanik exergisini azaltir. Bu kayip, pompa veya fan tarafindan telafi edilir:

```
Exergy kaybi (basinc dususu kaynakli):
  Ex_loss_DP = V_dot x DP / eta_pump  [kW]

Burada:
  V_dot     = Hacimsel debi [m3/s]
  DP        = Basinc dususu [Pa]
  eta_pump  = Pompa/fan toplam verimi [-] (tipik 0.60-0.80)
```

### Sayisal Ornek: Basinc Dususunun Exergy Maliyeti

Kosullar: Sogutma suyu devresi, 100 m3/saat = 0.0278 m3/s

| Senaryo | DP (kPa) | Pompa Gucu (kW) | Yillik Enerji (kWh) | Yillik Maliyet (EUR) |
|---------|----------|-----------------|---------------------|----------------------|
| Tasarim | 50 | 2.31 | 18,500 | 2,220 |
| Mevcut (kirli) | 85 | 3.94 | 31,500 | 3,780 |
| Optimize | 35 | 1.62 | 13,000 | 1,560 |

```
Pompa gucu = V_dot x DP / eta_pump
  = 0.0278 x 50,000 / 0.60 = 2,317 W = 2.31 kW

Yillik enerji = 2.31 x 8,000 = 18,500 kWh
Yillik maliyet = 18,500 x 0.12 = €2,220
```

Mevcut (kirli) durum ile optimize durum arasindaki tasarruf: €3,780 - €1,560 = **€2,220/yil**

## Basinc Dususu Optimizasyon Stratejileri

### 1. Baffle Araligi Optimizasyonu (Govde-Boru Esanjor)

Baffle araligi govde tarafi basinc dususunu dogrudan etkiler:

```
DP_shell ~ 1 / (baffle_araligi)^2

Baffle araligi arttikca:
  - DP azalir (kuvvetli etki)
  - Govde tarafi h_s azalir (is transfer katsayisi)
  - Titresim riski artabilir
```

| Baffle Araligi / Govde Capi Orani | DP Etkisi | h_s Etkisi | Oneri |
|------------------------------------|-----------|------------|-------|
| 0.2 (minimum) | Cok yuksek DP | Cok yuksek h_s | Ozel uygulamalar |
| 0.3-0.4 | Yuksek DP | Yuksek h_s | Yuksek h_s gerekli |
| 0.4-0.6 | Orta DP | Orta h_s | Standart tasarim |
| 0.6-0.8 | Dusuk DP | Dusuk h_s | DP sinirli uygulamalar |
| 1.0 (maksimum) | Minimum DP | Minimum h_s | Sadece DP kritik ise |

### 2. Baffle Kesimi Optimizasyonu (Baffle Cut)

```
Baffle kesim orani (%) = Acik alan yuksekligi / Govde capi x 100

Tipik aralik: %20-35
  - %20 kesim: Yuksek DP, yuksek h_s
  - %25 kesim: Standart (en yaygin)
  - %35 kesim: Dusuk DP, dusuk h_s
```

### 3. Helisel Baffle (Helical Baffle) Donusumu

Segmental baffle'larin helisel baffle ile degistirilmesi:

| Ozellik | Segmental Baffle | Helisel Baffle |
|---------|-----------------|----------------|
| Govde tarafi DP | Referans (1.0x) | 0.30-0.60x |
| Govde tarafi h_s | Referans (1.0x) | 0.80-0.95x |
| h_s/DP orani | Referans (1.0x) | 1.5-2.5x |
| Titresim riski | Orta-yuksek | Dusuk |
| Ölü bolge (dead zone) | Var | Yok |
| Maliyet (yeni esanjor) | Referans (1.0x) | 1.2-1.5x |
| Retrofit imkani | — | Sinirli (govde acma gerekli) |

**Avantajlar:** DP %40-70 azalir, h_s sadece %5-20 azalir; net verimlilik artisi.

### 4. Boru Gecis Sayisi Azaltma

```
DP_tube ~ N_p^2 (yaklasik)

2 gecis -> 1 gecis: DP %75 azalir, h_s %20-30 azalir
4 gecis -> 2 gecis: DP %75 azalir, h_s %20-30 azalir
```

| Gecis Sayisi | DP (goreli) | h_s (goreli) | Ne Zaman Uygun |
|--------------|-------------|--------------|----------------|
| 1 | 0.25x | 0.70-0.80x | Dusuk DP gerekli, yeterli uzunluk var |
| 2 | 1.0x (referans) | 1.0x | Standart |
| 4 | 4.0x | 1.15-1.25x | Yuksek h_s gerekli, DP siniri yuksek |
| 6 | 9.0x | 1.25-1.35x | Cok ozel uygulamalar |

### 5. Paralel Esanjor Duzenleme

Tek esanjor yerine iki paralel esanjor kullanarak debiyi bolme:

```
Tek esanjor:  V_dot, DP_1
Paralel (2x): V_dot/2 her biri, DP_paralel = DP_1 / 4

Basinc dususu azalmasi: %75
```

| Konfigurasyon | DP (goreli) | Yatirim (goreli) | Ne Zaman Tercih |
|---------------|-------------|-------------------|-----------------|
| 1 x buyuk | 1.0x | 1.0x | Standart |
| 2 x paralel | 0.25x | 1.4-1.6x | DP kritik, alan var |
| 3 x paralel | 0.11x | 1.8-2.0x | Cok dusuk DP gerekli |

### 6. Fan/Pompa Hiz Kontrolu (VSD)

Basinc dususu azaldiktan sonra pompa/fan hizini dusurerek enerji tasarrufu:

```
Pompa affinite yasalari:
  Q ~ N          (debi hiza orantili)
  H ~ N^2        (basma yuksekligi hizin karesine orantili)
  P ~ N^3        (guc hizin kupune orantili)

%20 debi azaltimi -> %49 guc tasarrufu
%10 debi azaltimi -> %27 guc tasarrufu
```

## Isi Transferi vs Basinc Dususu Odunlesimi

Isi transferi ile basinc dususu arasinda temel bir odunlesim (trade-off) vardir:

```
Performans degerlendirme kriteri:
  PEC = (h / h_ref) / (DP / DP_ref)^(1/3)

  PEC > 1: Iyilestirme (isi transferi basinc dususune gore daha fazla artti)
  PEC < 1: Kotulesme
```

### Performans Karsilastirma Tablosu

| Yontem | h Artisi | DP Artisi | PEC | Degerlendirme |
|--------|----------|-----------|-----|---------------|
| Turklu bant (twisted tape) | %30-80 | %100-300 | 0.8-1.2 | Orta-iyi |
| Tel sargi (wire coil) | %20-50 | %50-200 | 0.9-1.3 | Iyi |
| Ic kanatcik (micro-fin) | %50-100 | %50-150 | 1.1-1.5 | Cok iyi |
| Dimpled yuzey | %20-40 | %30-80 | 1.0-1.3 | Iyi |
| Helisel baffle | h korunur | DP %40-70 azalir | 1.5-2.5 | Mukemmel |
| Paralel duzenleme | h korunur | DP %75 azalir | — | Mukemmel |

## Sayisal Ornek: Pompa Enerji Tasarrufu

### Senaryo: Proses Sogutma Suyu Esanjoru

Mevcut durum:
- 300 m2 govde-boru esanjor, govde tarafi sogutma suyu
- Sogutma suyu debisi: 200 m3/saat
- Govde tarafi DP: 120 kPa (tasarim: 70 kPa — kirlenme + hatali baffle)
- Pompa verimi: 0.65
- Calisma suresi: 8,000 saat/yil
- Elektrik fiyati: €0.12/kWh

```
Mevcut pompa gucu (govde tarafi):
  P_mevcut = (200/3600) x 120,000 / 0.65 = 10,256 W = 10.26 kW
  Yillik enerji = 10.26 x 8,000 = 82,051 kWh
  Yillik maliyet = 82,051 x 0.12 = €9,846

Optimizasyon sonrasi (helisel baffle + temizlik, DP = 45 kPa):
  P_optimize = (200/3600) x 45,000 / 0.65 = 3,846 W = 3.85 kW
  Yillik enerji = 3.85 x 8,000 = 30,769 kWh
  Yillik maliyet = 30,769 x 0.12 = €3,692

Yillik tasarruf: €9,846 - €3,692 = €6,154/yil
```

**Yatirim:**
| Kalem | Maliyet |
|-------|---------|
| Helisel baffle donusumu | €18,000 |
| Esanjor temizligi | €2,000 |
| Pompa VSD ekleme | €5,000 |
| Toplam | €25,000 |

**Geri odeme suresi: €25,000 / €6,154 = 4.06 yil**

**Not:** VSD ile pompa hizi dusuruldugunde enerji tasarrufu daha da artabilir. Ek olarak, azalan DP kirlenme egilimini de azaltarak dolayli tasarruf saglar.

## Bypass ve Paralel Duzenleme Secenekleri

### Bypass Hatti

Esanjor uzerinden kismen bypass yaparak DP'yi azaltma:

```
Toplam debi: V_total = V_HX + V_bypass
DP_sistem = DP_HX x (V_HX / V_total)^2

%20 bypass: DP %36 azalir
%30 bypass: DP %51 azalir
```

**Dikkat:** Bypass, esanjor isi transfer performansini azaltir. Sadece DP cok kritik ve isi transfer kapasitesi yeterli ise uygulanmalidir.

### Paralel Duzenleme ile Kapasite Artisi

Mevcut esanjore paralel ikinci esanjor ekleme:

```
Avantajlar:
  - Her esanjorden gecen debi yarilir -> DP %75 azalir
  - Toplam transfer yuzey alani iki katina cikar
  - Bakim sirasinda bir esanjor calisabilir (redundancy)

Dezavantajlar:
  - Ek esanjor + piping maliyeti
  - Alan gereksinimi
  - Kontrol karmasikligi
```

## Uygulama Adimlari

1. **Mevcut DP olcumu:** Her iki tarafin diferansiyel basinc dususunu olc (temiz ve kirli)
2. **Tasarim DP karsilastirmasi:** Mevcut DP'yi orijinal tasarim degerine kiyasla
3. **Kaynak analizi:** DP artisinin nedeni (kirlenme, baffle, gecis sayisi, debi artisi)
4. **Cozum secimi:** Kisa vadeli (temizlik) ve uzun vadeli (baffle degisimi, paralel ekleme) planlama
5. **h/DP odunlesim analizi:** Isi transfer performansini kontrol et, DP azaltiminin h etkisini hesapla
6. **Pompa/fan guc hesabi:** Yeni DP'ye gore pompa gucu azaltimini hesapla (VSD varsa hiz azaltma)
7. **ROI hesabi:** Yatirim ve enerji tasarrufu karsilastirmasi
8. **Uygulama:** Baffle degisimi, temizlik, paralel ekleme veya VSD kurulumu
9. **Dogrulama:** DP, debi ve sicaklik olcumleri ile performansi dogrula

## İlgili Dosyalar

- Isi esanjoru exergy formulleri: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Kirlenme yonetimi: `heat_exchanger/solutions/fouling_management.md`
- Yaklasim sicakligi optimizasyonu: `heat_exchanger/solutions/approach_temp.md`
- Retrofit cozumleri: `heat_exchanger/solutions/retrofit.md`
- Pompa VSD cozumu: `pump/solutions/vsd.md`
- Pompa sistem optimizasyonu: `pump/solutions/system_optimization.md`
- Fabrika enerji akis analizi: `factory/energy_flow_analysis.md`

## Referanslar

- Kern, D.Q., "Process Heat Transfer," McGraw-Hill, 1950
- Bell, K.J., "Final Report of the Cooperative Research Program on Shell and Tube Heat Exchangers," University of Delaware, Eng. Exp. Station Bulletin No. 5, 1963
- HEDH (Heat Exchanger Design Handbook), Begell House — Sections 2.5 and 3.3
- Taborek, J., "Shell-and-Tube Heat Exchangers: Single Phase Flow," Chapter 3.3, HEDH
- Mukherjee, R., "Effectively Design Shell-and-Tube Heat Exchangers," Chemical Engineering Progress, 1998
- TEMA, "Standards of the Tubular Exchanger Manufacturers Association," 10th Edition
- Shah, R.K. and Sekulic, D.P., "Fundamentals of Heat Exchanger Design," Wiley, 2003
- Bejan, A., "Entropy Generation Through Heat and Fluid Flow," Wiley, 1982
- Thulukkanam, K., "Heat Exchanger Design Handbook," 2nd Edition, CRC Press
