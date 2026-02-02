---
title: "Kirlenme Yonetimi (Fouling Management)"
category: solution
equipment_type: heat_exchanger
keywords: [fouling, kirlenme, temizlik, CIP, fouling factor, TEMA, U-deger]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/audit.md]
use_when: ["U-deger dususu tespit edildiginde", "Kirlenme yonetimi planlanirken"]
priority: high
last_updated: 2026-02-01
---
# Kirlenme Yonetimi (Fouling Management)

> Son guncelleme: 2026-02-01

## Ozet

**Problem:** Isi esanjorlerinde kirlenme (fouling), yuzey uzerinde istenmeyen birikintilerin olusmasidir. Kirlenme isi transfer katsayisini (U-deger) dusurerek termal performansi azaltir, basinc dususunu arttirir ve enerji tuketimini yukselterek onemli exergy kayiplarina neden olur. Endustriyel tesislerde kirlenme kaynakli enerji kayiplari toplam isi transfer maliyetinin %2-10'unu olusturabilir.

**Cozum:** Kirlenme turune uygun temizlik yontemleri, CIP (Clean-in-Place) sistemleri, online izleme ve kestirimci bakim stratejileri ile kirlenmenin kontrol altinda tutulmasi.

**Tipik Tasarruf:** %5-20 (isi transfer veriminde iyilesme)
**Tipik ROI:** 0.5-2 yil

## Kirlenme Turleri (Fouling Types)

### 1. Kireclenme / Tortulanma (Scaling / Crystallization Fouling)

Cozunmus minerallerin (ozellikle CaCO3, CaSO4, SiO2) isitilan yuzeylerde cokelmesidir:

- **Olusum mekanizmasi:** Su sicakligi arttiginda CaCO3 cozunurlugu azalir; doyma noktasi asildiginda kristalizasyon baslar
- **Tipik birikinti:** Kalsiyum karbonat (CaCO3), kalsiyum sulfat (CaSO4), silika (SiO2)
- **Kritik sicaklik:** >60 C uzerinde hizlanir
- **Risk faktorleri:** Sert su (>200 ppm CaCO3), yuksek isil akim, dusuk akis hizi
- **Termal direnc:** 0.1-0.5 m2-K/kW (siddetine bagli)

### 2. Biyolojik Kirlenme (Biological Fouling / Biofouling)

Mikro-organizma (bakteri, alg, mantar) ve makro-organizma (midye, yosun) buyumesidir:

- **Olusum mekanizmasi:** Biyofilm tabakasi olusumu, organizma tutunmasi ve cogalma
- **Kritik sicaklik araligi:** 20-50 C (optimum buyume araligi)
- **Risk faktorleri:** Acik devre sogutma suyu, nehir/deniz suyu, organik madde icerigi yuksek sular
- **Tipik tesisler:** Sogutma kuleleri, kondenser devrelerinde yaygin
- **Termal direnc:** 0.05-0.3 m2-K/kW

### 3. Korozyon Urunleri Birikimi (Corrosion Fouling)

Metal yuzey korozyonu sonucu olusan oksit ve hidroksit tabakalarinin birikmesidir:

- **Olusum mekanizmasi:** Elektrokimyasal korozyon -> oksit tabakasi -> yuzeyden ayrilma -> yeni yuzey korozyonu
- **Tipik birikinti:** Demir oksit (Fe2O3), bakir oksit (CuO)
- **Risk faktorleri:** Dusuk pH, yuksek oksijen icerigi, farkli metal temas (galvanik)
- **Termal direnc:** 0.05-0.2 m2-K/kW

### 4. Kimyasal Reaksiyon Kirlenmesi (Chemical Reaction Fouling)

Akiskan icerisindeki kimyasal reaksiyonlar sonucu kati urunlerin olusmasidir:

- **Olusum mekanizmasi:** Polimerizasyon, oksidanma, cokme reaksiyonlari
- **Tipik uygulamalar:** Petrol rafineleri (kokslanma), gida endustrisi (proteinlerin denatürasyonu)
- **Kritik sicaklik:** Reaksiyon turune bagli, genellikle >150 C
- **Termal direnc:** 0.1-1.0 m2-K/kW

### 5. Sedimantasyon (Particulate / Sedimentation Fouling)

Akiskanda asili kati partiküllerin yuzey uzerinde cokmesidir:

- **Olusum mekanizmasi:** Düsük akis hizinda yercekimi ile cokme, turbulansin azaldigi bolgelerde birikim
- **Tipik partikul:** Kum, kil, pas parcaciklari, proses atiklarinin katilari
- **Risk faktorleri:** Düsük akis hizi (<0.5 m/s), filtrasyon eksikligi
- **Termal direnc:** 0.05-0.5 m2-K/kW

### 6. Donma Kirlenmesi (Freezing / Solidification Fouling)

Akiskanin soguk yuzey ile temas edip katilasmasidir:

- **Olusum mekanizmasi:** Akiskanin donma noktasi alti yuzey sicakliginda katilasma
- **Tipik uygulamalar:** Balmumu iceren petrol akiskanlari, yag sogutma, kriyojenik sistemler
- **Risk faktorleri:** Yuzey sicakligi < akiskan donma noktasi
- **Termal direnc:** 0.05-0.3 m2-K/kW

## TEMA Kirlenme Direnci Degerleri (Fouling Resistance — R_f)

TEMA (Tubular Exchanger Manufacturers Association) standartlarina gore onerilen kirlenme direnci degerleri:

| Akiskan | R_f (m2-K/kW) | Aciklama |
|---------|----------------|----------|
| Aritmali kazan besleme suyu | 0.09 | Dusuk TDS, degazorlu |
| Sehir suyu (yumusak) | 0.18 | <100 ppm CaCO3 |
| Sehir suyu (sert) | 0.35 | >200 ppm CaCO3 |
| Nehir suyu | 0.35-0.53 | Filtrelenmis |
| Deniz suyu | 0.09-0.18 | Klorlanmis, <50 C |
| Deniz suyu (sicak) | 0.35 | >50 C |
| Sogutma kulesi suyu (aritilmis) | 0.18 | Kimyasal dozajlamali |
| Sogutma kulesi suyu (aritilmamis) | 0.53 | Biyosit yok |
| Buhar (temiz) | 0.009 | Kondensat |
| Motor yagi | 0.18 | Normal isletme |
| Hidrolik yag | 0.18 | Temiz sistem |
| Hafif hidrokarbonlar | 0.18 | Temiz |
| Agir hidrokarbonlar | 0.35-0.53 | Kokslanma riski |
| Hava (temiz) | 0.18-0.35 | Toz icerigine bagli |
| Baca gazi | 0.53-0.88 | Kurum ve kul |

**Not:** Bu degerler tasarim icin kullanilir. Fiili kirlenme direnci olculerek U-deger dususu izlenmelidir.

## Kirlenme Izleme KPI'lari (Fouling Monitoring KPIs)

### 1. Temizlik Faktoru (Cleanliness Factor — CF)

```
CF = U_actual / U_clean

Burada:
  CF       = Temizlik faktoru [-] (1.0 = temiz, 0.0 = tamamen kirli)
  U_actual = Mevcut toplam isi transfer katsayisi [W/(m2-K)]
  U_clean  = Temiz durumdaki toplam isi transfer katsayisi [W/(m2-K)]
```

| CF Degeri | Durum | Aksiyon |
|-----------|-------|---------|
| 0.90-1.00 | Temiz | Normal isletme |
| 0.80-0.90 | Hafif kirlenme | Izlemeye devam |
| 0.70-0.80 | Orta kirlenme | Temizlik planlama |
| 0.60-0.70 | Ciddi kirlenme | Acil temizlik gerekli |
| <0.60 | Kritik | Derhal temizlik, esanjor durdur |

### 2. Kirlenme Direnci Trendi (Fouling Resistance Trend)

```
R_f = (1/U_actual) - (1/U_clean) [m2-K/W]
```

R_f zaman icinde izlenerek kirlenme hizi (fouling rate) belirlenir:

```
Fouling Rate = dR_f / dt [m2-K/(W-gun)]
```

### 3. U-Deger Dusus Hizi (U-Value Decay Rate)

```
U_decay = (U_clean - U_actual) / (U_clean x t_isletme) x 100 [%/ay]
```

| U-Deger Dusus Hizi | Degerlendirme |
|---------------------|---------------|
| <1%/ay | Normal |
| 1-3%/ay | Dikkat — kirlenme artisi |
| 3-5%/ay | Yuksek — su kimyasini kontrol et |
| >5%/ay | Kritik — acil mudahale |

## CIP (Clean-in-Place) Prosedürleri

### Plakali Isi Esanjorler Icin CIP

1. **On yikama:** Esanjoru proses akiskanindan bosalt, 25-30 C su ile 15 dakika sirkule et
2. **Alkali yikama:** %2-5 NaOH cozeltisi, 70-80 C, 30-60 dakika sirkulasyon
3. **Ara durulama:** Temiz su ile 10 dakika, pH notr olana kadar
4. **Asit yikama:** %1-3 HNO3 veya sitrik asit cozeltisi, 50-60 C, 30-45 dakika
5. **Son durulama:** Temiz su ile 15 dakika, pH notr ve iletkenlik kontrol
6. **Dezenfeksiyon (gida/icecek):** 50-100 ppm perasetik asit, 20 C, 15-20 dakika

| CIP Kimyasali | Konsantrasyon | Sicaklik | Sure | Hedef Kirlenme |
|---------------|---------------|----------|------|----------------|
| NaOH (Kostik soda) | %2-5 | 70-80 C | 30-60 dk | Organik, yag, biyofilm |
| HNO3 (Nitrik asit) | %1-3 | 50-60 C | 30-45 dk | Mineral kirec, oksit |
| Sitrik asit | %2-4 | 60-70 C | 45-60 dk | Hafif kirec (gida uyumlu) |
| HCl (Hidroklorik asit) | %1-2 | 40-50 C | 20-30 dk | Agir kirec (karbon celik) |
| EDTA | %2-5 | 70-80 C | 60-120 dk | Kompleks mineral birikinti |
| Perasetik asit | 50-100 ppm | 20 C | 15-20 dk | Dezenfeksiyon |

**Not:** Paslanmaz celik plakalar icin HCl kullanilmamalidir (cukurcuk korozyonu riski). Titanyum plakalar icin HF iceren kimyasallardan kacinilmalidir.

### Govde-Boru (Shell & Tube) Esanjorler Icin CIP

- **Boru tarafi:** CIP cozeltisi sirkulasyonu standart
- **Govde tarafi:** Akis yolu karmasik, dolgu nozullardan giris gerekli
- **Sirkülasyon debisi:** Normal isletme debisinin en az %150'si (türbülans icin)
- **Kimyasal secimi:** Kirlenme turune ve malzemeye uygun (yukaridaki tabloya gore)

## Mekanik Temizlik Yontemleri

### 1. Hidroblasting (Yüksek Basinc Su Jeti)

- **Basinc araligi:** 300-1,500 bar
- **Uygulama:** Boru ici ve disi yuzeyler, agir kirec ve koks
- **Etkinlik:** %90-99 temizlik
- **Maliyet:** €1,000-5,000/esanjor (boyuta bagli)
- **Avantaj:** Kimyasal gerektirmez, hizli
- **Dezavantaj:** Ekipman durdurma gerekli, uzman personel

### 2. Cubuk ve Matkap Temizligi (Rod/Drill Cleaning)

- **Uygulama:** Boru ici sert birikintiler (kirec, koks)
- **Arac:** Esnek cubuklar, donen firca, matkap uclari
- **Etkinlik:** %85-95 temizlik
- **Maliyet:** €500-3,000/esanjor
- **Not:** Boru ic capina uygun aletler secilmelidir

### 3. Kimyasal Islama (Chemical Soak)

- **Uygulama:** Govde tarafi temizligi, karmasik geometriler
- **Prosedur:** Esanjoru kimyasal cozeltiye daldirma veya dolum
- **Sure:** 4-24 saat (kirlenme siddetine bagli)
- **Kimyasallar:** Asit (kirec icin), alkali (organik icin), solvent (yag icin)
- **Maliyet:** €500-2,000 (kimyasal + iscilik)

### 4. Buhar Temizligi (Steam Lancing)

- **Uygulama:** Boru disi yuzeyler, hava sogutmali esanjorler
- **Parametreler:** 5-10 bar buhar, nozel ile yuzey tarama
- **Etkinlik:** Organik ve hafif birikintiler icin iyi
- **Maliyet:** €200-500/esanjor

### 5. Otomatik Boru Ici Temizlik Sistemleri (ATCS)

- **Tapirogge sistemi:** Her boruya sponj top (sponge ball) gonderme
- **CQM/Eqobrush:** Fircali otomatik temizleme, boru uclarinda fircalar gidip gelir
- **Avantaj:** Online temizlik (duraklatmaya gerek yok), surekli yuksek performans
- **Yatirim:** €15,000-50,000 (esanjor boyutuna bagli)
- **Tasarruf:** CF surekli >0.95, kirlenme kaynakli exergy kaybi minimize

## Online Izleme ve Kestirimci Bakim

### Izlenmesi Gereken Parametreler

| Parametre | Sensor | Olcum Sikligi | Alarm Esigi |
|-----------|--------|---------------|-------------|
| Giris/cikis sicakliklari (4 nokta) | PT100 / PT1000 | Surekli (1 dk) | DT_approach > tasarimin %150'si |
| Debi (her iki taraf) | Ultrasonik / Vortex | Surekli | Debi sapma > %10 |
| Basinc dususu (her iki taraf) | Diferansiyel basinc | Surekli | DP > tasarimin %130'u |
| Hesaplanan U-deger | PLC/SCADA hesaplama | Her 5 dk | U < U_clean x 0.75 |
| Hesaplanan CF | PLC/SCADA hesaplama | Her 5 dk | CF < 0.80 |

### Kestirimci Bakim (Predictive Maintenance) Algoritmalari

```
R_f(t) = R_f_max x (1 - exp(-t/tau))

Burada:
  R_f(t)     = t anindaki kirlenme direnci [m2-K/W]
  R_f_max    = Asimptotik kirlenme direnci [m2-K/W]
  tau        = Zaman sabiti [gun]
  t          = Isletme suresi [gun]
```

Bu modelle gelecek kirlenme seviyesi tahmin edilerek optimal temizlik zamani planlanir.

## Temizlik Zamanlamasi Optimizasyonu

### Maliyet Analizi: Temizlik Maliyeti vs Kirlenme Maliyeti

```
Toplam_maliyet = C_temizlik + C_kirlenme

C_temizlik = (N_temizlik/yil) x (C_kimyasal + C_iscilik + C_duraklatma)
C_kirlenme = integral(0, T) [DeltaU(t) x A x LMTD x C_enerji] dt

Optimal temizlik periyodu minimuma indirir:
  dC_toplam / dT_temizlik = 0
```

| Maliyet Kalemi | Tipik Deger | Aciklama |
|----------------|-------------|----------|
| CIP kimyasal maliyeti | €200-1,000/temizlik | Kimyasal ture ve hacme bagli |
| Iscilik (CIP) | €100-500/temizlik | 2-4 saat teknisyen |
| Mekanik temizlik | €1,000-5,000/temizlik | Hidroblasting, ozel ekipman |
| Uretim kaybi (duraklatma) | €500-10,000/temizlik | Tesise ve ure birimine bagli |
| Kirlenme kaynakli ek enerji | €2,000-20,000/yil | Isi transfer dususu kompanzasyonu |

### Ornek: Temizlik Zamanlama Optimizasyonu

- 100 m2 plakali esanjor, U_clean = 3,500 W/(m2-K)
- Kirlenme hizi: %3/ay U-deger dususu
- LMTD = 10 C, enerji maliyeti = €0.045/kWh
- CIP maliyeti (temizlik + duraklatma) = €1,500/temizlik
- Yillik calisma suresi: 8,000 saat

```
Kirlenme kaynakli ek enerji maliyeti (6 ay sonra):
  U_6ay = 3,500 x (1 - 0.03x6) = 3,500 x 0.82 = 2,870 W/(m2-K)
  Q_kayip = (3,500 - 2,870) x 100 x 10 / 1,000 = 63 kW
  Yillik_kayip_maliyeti = 63 x 8,000 x 0.045 / 2 = €11,340

Yilda 2 temizlik (her 6 ayda):
  C_temizlik = 2 x 1,500 = €3,000
  C_kirlenme = ~€11,340 / 2 = €5,670 (ortalama etki)
  Toplam = €8,670

Yilda 4 temizlik (her 3 ayda):
  C_temizlik = 4 x 1,500 = €6,000
  C_kirlenme = ~€11,340 / 4 = €2,835
  Toplam = €8,835

Yilda 3 temizlik (her 4 ayda):
  C_temizlik = 3 x 1,500 = €4,500
  C_kirlenme = ~€11,340 / 3 = €3,780
  Toplam = €8,280  <-- Optimal
```

**Sonuc:** Bu ornekte optimal temizlik periyodu yaklasik 4 aydir.

## Kirlenmenin Exergy Verimliligi Uzerine Etkisi

Kirlenme, isi esanjorunde ek termal direnc olusturarak sicaklik farkini arttirir ve entropi uretimini (S_gen) yukselterek exergy yikimini arttirir:

```
Kirlenme kaynakli ek exergy yikim:
  Ex_d_fouling = T_0 x S_gen_fouling

  S_gen_fouling = Q^2 x R_f / (A x T_h x T_c)

Burada:
  T_0     = Cevre sicakligi [K]
  Q       = Isi transfer hizi [kW]
  R_f     = Kirlenme direnci [m2-K/W]
  A       = Transfer yuzey alani [m2]
  T_h     = Sicak akiskan ortalama sicakligi [K]
  T_c     = Soguk akiskan ortalama sicakligi [K]
```

### Sayisal Ornek: Kirlenme ve Exergy Kaybi

- Q = 500 kW, A = 50 m2, T_h = 363 K (90 C), T_c = 313 K (40 C), T_0 = 298 K (25 C)
- Temiz: R_f = 0, U_clean = 2,000 W/(m2-K)
- Kirli: R_f = 0.35 m2-K/kW = 0.00035 m2-K/W

```
Temiz durum exergy verimi:
  eta_ex_clean = 1 - T_0 x S_gen_clean / Ex_hot_in = ~%62

Kirli durum (6 ay sonra):
  S_gen_fouling = 500^2 x 0.00035 / (50 x 363 x 313) = 0.0154 kW/K
  Ex_d_fouling = 298 x 0.0154 = 4.59 kW

  eta_ex_fouled = ~%58

Exergy verimi kaybi = %62 - %58 = %4 mutlak dusus
```

## ROI Hesabi: Kirlenme Yonetimi Programi

### Senaryo: Orta Olcekli Kimya Fabrikasi

- 10 adet govde-boru esanjor, ortalama 200 m2/esanjor
- Mevcut durum: Yilda 1 temizlik (reaktif), U-deger ortalama %30 dusuk
- Hedef: Online izleme + optimum zamanlamali temizlik programi

**Yatirim:**
| Kalem | Maliyet |
|-------|---------|
| Online izleme sistemi (10 esanjor) | €35,000 |
| Sensorler ve kablaj | €15,000 |
| SCADA entegrasyonu | €10,000 |
| CIP sistemi iyilestirme | €20,000 |
| Toplam | €80,000 |

**Yillik Tasarruf:**
| Kalem | Deger |
|-------|-------|
| Enerji tasarrufu (U-deger iyilesmesi) | €45,000/yil |
| Azaltilmis mekanik temizlik maliyeti | €8,000/yil |
| Uzayan esanjor omru | €5,000/yil |
| Azaltilmis plansiz duraklatma | €15,000/yil |
| Toplam | €73,000/yil |

**Geri odeme suresi: €80,000 / €73,000 = 1.10 yil**

## İlgili Dosyalar

- Isi esanjoru exergy formulleri: `heat_exchanger/formulas.md`
- Benchmark verileri ve U-deger araliklari: `heat_exchanger/benchmarks.md`
- Isi esanjoru denetim metodolojisi: `heat_exchanger/audit.md`
- Malzeme secimi (korozyon etkilesimi): `heat_exchanger/solutions/material_selection.md`
- Retrofit cozumleri: `heat_exchanger/solutions/retrofit.md`
- Fabrika seviyesi bakim stratejisi: `factory/implementation.md`
- Olcum ve dogrulama: `factory/measurement_verification.md`

## Referanslar

- TEMA, "Standards of the Tubular Exchanger Manufacturers Association," 10th Edition
- Bott, T.R., "Fouling of Heat Exchangers," Elsevier, 1995
- Muller-Steinhagen, H., "Heat Exchanger Fouling: Mitigation and Cleaning Techniques," IChemE, 2000
- EPRI, "Condenser Fouling Monitoring and Cleaning Optimization"
- Garrett-Price, B.A., "Fouling of Heat Exchangers: Characteristics, Costs, Prevention, Control & Removal," Noyes Publications
- Chenoweth, J.M., "Final Report of the HTRI/TEMA Joint Committee to Review the Fouling Section of TEMA Standards"
- Panchal, C.B., "Fouling Mitigation of Industrial Heat-Exchange Equipment," Begell House
- ASME, "Fouling of Heat Transfer Equipment," Conference Proceedings
- Kuppan, T., "Heat Exchanger Design Handbook," 2nd Edition — Chapter 13: Fouling
- ISO 8501, "Preparation of Steel Substrates Before Application of Paints and Related Products"
