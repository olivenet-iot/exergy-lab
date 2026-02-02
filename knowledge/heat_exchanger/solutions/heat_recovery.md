---
title: "Isi Geri Kazanim Uygulamalari (Heat Recovery Applications)"
category: solution
equipment_type: heat_exchanger
keywords: [isi geri kazanim, waste heat, atik isi, heat recovery, pinch, HEN, run-around coil, heat pipe]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, factory/waste_heat_recovery.md, factory/heat_integration.md, factory/pinch_analysis.md]
use_when: ["Atik isi kaynagi tespit edildiginde", "Isi geri kazanim firsati degerlendirilirken", "Fabrika geneli isi entegrasyonu planlanirken"]
priority: high
last_updated: 2026-02-01
---
# Isi Geri Kazanim Uygulamalari (Heat Recovery Applications)

> Son guncelleme: 2026-02-01

## Ozet

**Problem:** Endustriyel tesislerde onemli miktarda isi, baca gazi, sogutma suyu, proses atik akimlari ve kondensat yoluyla cevrye atilmaktadir. Bu atik isi kaynakari genellikle 40-400 C arasinda sicaklik seviyelerinde bulunur ve toplam enerji tuketiminin %20-50'sini olusturabilir. Atik isinin kullanlmamasi, hem enerji maliyetlerini arttirir hem de onemli bir exergy kaybi yaratir.

**Cozum:** Atik isi kaynaklarinin sistematik olarak tanimlanmasi, siniflandirilmasi ve uygun isi esanjoru teknolojileri ile geri kazanilmasi. Pinch analizi ile fabrika genelinde optimal isi geri kazanim agi (Heat Exchanger Network — HEN) tasarimi.

**Tipik Tasarruf:** %10-40 (toplam yakiti tuketiminde azalma)
**Tipik ROI:** 1-5 yil

## Atik Isi Kaynagi Tanimlama ve Siniflandirma

### Sicaklik Seviyesine Gore Siniflandirma

| Sicaklik Seviyesi | Aralik (C) | Tipik Kaynaklar | Kalite (Exergy) |
|-------------------|------------|-----------------|-----------------|
| Yuksek sicaklik | >400 | Firin baca gazlari, cam/metal eritme, dogrudan yanma | Yuksek exergy |
| Orta-yuksek sicaklik | 200-400 | Kazan baca gazlari, kurutma egzoz, CHP egzoz | Orta-yuksek exergy |
| Orta sicaklik | 100-200 | Buhar kondensat, proses egzoz, distilasyon | Orta exergy |
| Dusuk-orta sicaklik | 60-100 | Kompressor sogutma, motor sogutma, proses sogutma | Dusuk-orta exergy |
| Dusuk sicaklik | <60 | Sogutma kulesi, chiller kondenser, atik su | Dusuk exergy |

### Endustriyel Atik Isi Kaynaklari Envanteri

| Kaynak | Tipik Sicaklik (C) | Tipik Kapasite (kW) | Sureklilik | Temizlik |
|--------|---------------------|---------------------|------------|----------|
| Kazan baca gazi | 150-300 | 50-5,000 | Surekli | Orta |
| CHP egzoz gazi | 350-550 | 100-10,000 | Surekli | Orta |
| Kurutma egzozu | 80-200 | 50-2,000 | Kesikli | Dusuk (toz) |
| Firin baca gazi | 300-800 | 100-50,000 | Surekli | Dusuk (kul) |
| Buhar kondensat | 80-150 | 20-1,000 | Surekli | Yuksek |
| Kompressor sogutma | 60-90 | 10-500 | Surekli | Yuksek |
| Chiller kondenser | 30-45 | 50-5,000 | Mevsimsel | Yuksek |
| Proses sogutma suyu | 40-80 | 50-5,000 | Surekli | Orta |
| Atik su | 30-60 | 20-500 | Surekli | Dusuk |
| Havalandirma egzozu | 20-40 | 50-2,000 | Surekli | Orta |

## Isi Geri Kazanim Ekipman Secimi

### Sicaklik Araligina Gore Esanjor Secimi

| Sicaklik Araligi (C) | Onerilen Esanjor Tipi | Tipik U Degeri W/(m2-K) | Maliyet Seviyesi |
|----------------------|----------------------|------------------------|-----------------|
| >500 | Radyasyon rekuperator, seramik rejenerator | 10-30 | Yuksek |
| 300-500 | Metalik rekuperator, konvektif ekonomizer | 20-60 | Orta-yuksek |
| 150-300 | Boru demeti ekonomizer, isi borulari (heat pipe) | 30-100 | Orta |
| 80-150 | Govde-boru, plakali, run-around coil | 200-1,500 | Orta |
| 40-80 | Plakali, yuksek verimli govde-boru | 500-3,000 | Dusuk-orta |
| <40 | Isi pompasi destekli, buyuk yuzey alan | 200-1,000 | Dusuk |

### Isi Geri Kazanim Karar Matrisi

```
Atik isi kaynagi -> Sicaklik seviyesi belirle
  |
  +-- >150 C: Dogrudan isi geri kazanim (ekonomizer, rekuperator)
  |     |-- Temiz gaz -> Metalik esanjor
  |     |-- Kirli gaz -> Isi borusu (heat pipe), cam kapli
  |
  +-- 60-150 C: Dogrudan veya run-around coil
  |     |-- Akimlar yakin -> Dogrudan esanjor
  |     |-- Akimlar uzak -> Run-around coil sistemi
  |
  +-- 30-60 C: Dusuk sicaklik geri kazanim
  |     |-- Isi pompasi ile yukseltme
  |     |-- Onisitma uygulamasi
  |
  +-- <30 C: Genellikle ekonomik degil
        |-- Cok buyuk debi + isi pompasi icin degerlendir
```

## Run-Around Coil Sistemleri

Run-around coil, fiziksel olarak ayri konumdaki isi kaynagi ve isi yutucu arasinda isi transferi saglar:

### Calisma Prensibi

```
Komponentler:
  1. Kaynak tarafinda isi esanjoru (finned coil, plakali vb.)
  2. Yukucu tarafinda isi esanjoru
  3. Ara devre sirkülasyon sivisisi (su, glikol karisimi)
  4. Sirkülasyon pompasi
  5. Genlesme tanki ve kontrol elemanlari

Avantajlar:
  - Akimlar fiziksel olarak ayridir (kontaminasyon riski yok)
  - Uzun mesafe tasima mumkun (50-200 m)
  - Esnek kapasite kontrolu
  - Bagimsiz basinc seviyeleri

Dezavantajlar:
  - Ek sicaklik farki kaybi (2 esanjor, ara devre)
  - Pompa enerji tuketimi
  - %60-80 verimlilik (dogrudan esanjore gore daha dusuk)
```

### Run-Around Coil Tasarim Parametreleri

| Parametre | Tipik Aralik | Aciklama |
|-----------|-------------|----------|
| Ara devre sivi | Su veya %30-50 etilen glikol | Donma riski varsa glikol |
| Sivi sicaklik farki | 5-15 C | Kaynak-yutucu arasinda |
| Mesafe | 10-200 m | Boru izolasyonu gerekli |
| Pompa gucu | %2-5 x Q_recovery | Sirkülasyon enerjisi |
| Toplam verimlilik | %60-80 | Dogrudan HX'e gore daha dusuk |
| Duzeltme | F = 0.7-0.9 | Ek sicaklik dusus icin |

### Ornek: Kurutma Egzoz Isisi ile Taze Hava Onisitma

- Kurutma egzoz: 120 C, 15,000 m3/saat
- Taze hava: 10 C (kis), 5,000 m3/saat
- Mesafe: 80 m

```
Q_kaynak = 15,000/3600 x 1.2 x 1.0 x (120 - 60) = 300 kW (kismi geri kazanim)
Q_recovery = 300 x 0.70 (run-around verim) = 210 kW

Taze hava sicaklik artisi:
  DT_hava = 210 / (5,000/3600 x 1.2 x 1.0) = 126 C -> sinirlandirilir
  T_hava_cikis = 10 + 80 = 90 C (pratik sinir)
  Q_kullanilan = 5,000/3600 x 1.2 x 1.0 x (90 - 10) = 133 kW

Yillik tasarruf (dogalgaz, 5,000 saat isitma sezonu):
  Tasarruf = 133 x 5,000 x 0.045 / 0.88 = €34,034/yil
```

## Isi Borulari (Heat Pipe Heat Exchangers)

### Calisma Prensibi

Isi borulari, kapali bir boru icindeki akiskanin buharlasmasi ve yogusmasi ile isi tasir:

```
Komponentler:
  - Evaporator bolumu: Sicak gaz tarafinda, akiskan buharlasmasi
  - Adyabatik bolum: Buhar tasima (yalitimli)
  - Kondenser bolumu: Soguk gaz tarafinda, buhar yogusmasi

Avantajlar:
  - Hareketli parca yok (pompa gerektirmez)
  - Cok yuksek termal iletkenlik
  - Kaynak/yutucu akimlari tamamen ayri (sizma riski yok)
  - Dusuk bakim gereksinimi
  - Sicaklik seviyesi kontrol edilebilir (calisma basinci ile)

Dezavantajlar:
  - Sinirli kapasite (birim basi)
  - Tek yonlu isi transferi
  - Sicaklik araligi calisan akiskana bagli
```

### Isi Borusu Calisan Akiskan Secimi

| Akiskan | Calisma Sicakligi Araligi (C) | Uygulama |
|---------|-------------------------------|----------|
| Amonyak | -60 ile +60 | Dusuk sicaklik geri kazanim |
| Su | 30-250 | Genel endustriyel |
| Metanol | 10-130 | Orta sicaklik |
| Dowtherm A | 150-350 | Yuksek sicaklik |
| Sodyum | 500-1,100 | Cok yuksek sicaklik |
| Potasyum | 400-1,000 | Yuksek sicaklik |

## Atik Isi Agi Tasarimi (Waste Heat Network)

### Coklu Kaynak — Coklu Yutucu Sistemi

Birden fazla atik isi kaynagi ve tuketici arasinda optimal eslestirme:

```
Atik Isi Kaynaklari:          Isi Yutuculari:
  Kompressor (80 C, 50 kW)       Kazan besleme suyu (20->60 C, 120 kW)
  Baca gazi (200 C, 300 kW)      Proses sicak su (40->70 C, 80 kW)
  Chiller kondenser (40 C, 200 kW) Bina isitma (35->50 C, 150 kW)
  Proses sogutma (65 C, 100 kW)  Kurutma on isitma (30->80 C, 200 kW)

Toplam kaynak: 650 kW
Toplam yutucu: 550 kW
Teorik geri kazanim potansiyeli: 550 kW (sicaklik uyumlulugu kontrolu sonrasi)
```

### Eslestirme Stratejisi

1. **Sicaklik kaskat (temperature cascade):** Yuksek sicaklik kaynaklarini yuksek sicaklik taleplerine, dusuk sicaklik kaynaklarini dusuk sicaklik taleplerine esle
2. **Pinch analizi:** Kompozit egriler ile minimum dis enerji ihtiyacini belirle
3. **Ekonomik optimizasyon:** Esanjor sayisi, boru uzunlugu ve enerji tasarrufunu birlikte optimize et

### Atik Isi Agi Maliyet Tahmin Tablosu

| Bilesen | Birim Maliyet | Aciklama |
|---------|---------------|----------|
| Plakali esanjor | €80-200/m2 | Paslanmaz celik |
| Govde-boru esanjor | €100-300/m2 | Karbon celik govde, paslanmaz boru |
| Run-around coil | €150-350/kW_recovered | Komple sistem |
| Isi borusu esanjor | €200-500/kW_recovered | Hava-hava uygulamasi |
| Izolasyonlu boru | €50-150/m | DN50-DN150, mineral yun |
| Sirkülasyon pompasi | €1,000-5,000/adet | Debi ve basinca bagli |
| Kontrol vanasi | €500-2,000/adet | Motorlu vana |
| BMS entegrasyonu | €5,000-15,000 | SCADA/PLC programlama |

## Pinch Analizi ile Isi Geri Kazanim Agi Entegrasyonu

### Temel Ilkeler

```
Pinch Kurallari:
  1. Pinch noktasi uzerinde dis isitma YAPILMAMALI
  2. Pinch noktasi altinda dis sogutma YAPILMAMALI
  3. Pinch noktasi uzerinden isi transferi YAPILMAMALI

Bu kurallara uyulmadiginda:
  - Her 1 kW kural ihlali = 2 kW ek dis enerji ihtiyaci
  - "Cross-pinch" isi transferi en yaygin hata
```

### Pinch Tasarim Yontemi (PDM)

```
Adim 1: Sicak ve soguk akimlari belirle
Adim 2: Kompozit egrileri ciz, DT_min sec
Adim 3: Pinch noktasini belirle
Adim 4: Q_H_min (minimum isitma) ve Q_C_min (minimum sogutma) hedeflerini hesapla
Adim 5: Pinch ustu ve alti icin ayri ayri esanjor eslestirmesi yap
Adim 6: Esanjor agini (HEN) olustur
Adim 7: Ekonomik optimizasyon (esanjor sayisi, DT_min hassasiyet analizi)
```

### Ornek: Gida Fabrikasi Isi Entegrasyonu

Mevcut durum:
- Toplam isitma yueku: 2,000 kW (dogalgaz kazan)
- Toplam sogutma yueku: 1,500 kW (sogutma kulesi + chiller)
- Yillik yakit maliyeti: €540,000
- Yillik elektrik maliyeti (sogutma): €180,000

Pinch analizi sonucu (DT_min = 15 C):
- Q_H_min = 800 kW (kazan yerine minimum dis isitma)
- Q_C_min = 300 kW (minimum dis sogutma)
- Q_recovery = 1,200 kW (isi geri kazanim potansiyeli)

```
Yillik yakit tasarrufu:
  = (2,000 - 800) x 8,000 x 0.045 / 0.88 = €490,909 -> Sinirli: gercekci %70 uygulama
  = €490,909 x 0.70 = €343,636/yil

Yillik sogutma tasarrufu:
  = (1,500 - 300) x 8,000 x 0.12 / 5.5 = €209,455 -> Gercekci %70
  = €209,455 x 0.70 = €146,618/yil

Toplam yillik tasarruf: €490,255/yil
```

## Ekonomik Degerlendirme (NPV, IRR, SPP)

### Temel Ekonomik Gostergeler

```
Basit Geri Odeme Suresi (SPP):
  SPP = Yatirim / Yillik_net_tasarruf [yil]

Net Bugunku Deger (NPV):
  NPV = -I_0 + Toplam(CF_t / (1+r)^t)  t=1..n

Burada:
  I_0  = Baslangic yatirimi [EUR]
  CF_t = t yilindaki net nakit akisi [EUR]
  r    = Iskonto orani [-]
  n    = Proje omru [yil]

Ic Verim Orani (IRR):
  NPV = 0 icin r degerini bul
```

### Ornek Ekonomik Degerlendirme

| Parametre | Deger |
|-----------|-------|
| Toplam yatirim | €350,000 |
| Yillik tasarruf (1. yil) | €490,255 |
| Yillik enerji fiyat artisi | %3 |
| Yillik bakim maliyeti | €15,000 |
| Proje omru | 15 yil |
| Iskonto orani | %8 |

```
SPP = 350,000 / (490,255 - 15,000) = 0.74 yil
NPV (15 yil, %8 iskonto) = €3,850,000 (kuvvetli pozitif)
IRR = %134 (cok yuksek)
```

## Karar Matrisi: Isi Geri Kazanim Yatirim Onceliklendirme

| Kriter | Agirlik | Yuksek Puan | Dusuk Puan |
|--------|---------|-------------|------------|
| Atik isi miktari (kW) | %25 | >500 kW | <50 kW |
| Sicaklik seviyesi (C) | %20 | >150 C | <40 C |
| Sureklilik (saat/yil) | %20 | >6,000 | <2,000 |
| Isi yutucu yakinligi | %15 | <30 m | >100 m |
| Akiskan temizligi | %10 | Temiz | Cok kirli |
| Uygulama kolayligi | %10 | Basit retrofit | Karmasik modifikasyon |

## Uygulama Adimlari

1. **Atik isi envanteri:** Tum proses akimlarinin sicaklik, debi ve isi kapasitesini belirle
2. **Isi yutucu envanteri:** Tum isitma gereksinimlerini listele (kazan besleme, DHW, proses, bina)
3. **Sicaklik eslestirme:** Kaynak-yutucu eslesme matrisini olustur
4. **Pinch analizi:** Kompozit egriler ve hedef hesaplama (DT_min hassasiyet dahil)
5. **HEN tasarimi:** Esanjor agini pinch kurallarnia gore tasarla
6. **Ekipman secimi:** Her esanjor icin tip, malzeme ve boyut belirle
7. **Piping dizayni:** Boru guzergahi, izolasyon, vana ve enstrümantasyon
8. **Ekonomik analiz:** SPP, NPV, IRR hesapla
9. **Uygulama plani:** Faz bazli uygulama, onceliklendirme
10. **Devreye alma:** Asamali devreye alma, performans olcumu
11. **Izleme ve optimizasyon:** Surekli performans izleme, mevsimsel ayar

## İlgili Dosyalar

- Isi esanjoru exergy formulleri: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Yaklasim sicakligi optimizasyonu: `heat_exchanger/solutions/approach_temp.md`
- Kirlenme yonetimi: `heat_exchanger/solutions/fouling_management.md`
- Retrofit cozumleri: `heat_exchanger/solutions/retrofit.md`
- Kompressor isi geri kazanimi: `compressor/solutions/heat_recovery.md`
- Chiller isi geri kazanimi: `chiller/solutions/heat_recovery.md`
- Kazan ekonomizer: `boiler/solutions/economizer.md`
- Fabrika atik isi geri kazanimi: `factory/waste_heat_recovery.md`
- Fabrika isi entegrasyonu: `factory/heat_integration.md`
- Fabrika pinch analizi: `factory/pinch_analysis.md`
- Fabrika proses entegrasyonu: `factory/process_integration.md`
- Fabrika ekonomik analiz: `factory/economic_analysis.md`

## Referanslar

- Linnhoff, B., et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1982
- Kemp, I.C., "Pinch Analysis and Process Integration," 2nd Edition, Butterworth-Heinemann, 2007
- Smith, R., "Chemical Process Design and Integration," 2nd Edition, Wiley, 2016
- DOE/AMO, "Waste Heat Recovery: Technology and Opportunities in U.S. Industry," 2008
- Johnson, I., et al., "Waste Heat Recovery — Technology Opportunities in the US Industry," BCS Inc. for DOE, 2008
- Reay, D., Kew, P., McGlen, R., "Heat Pipes: Theory, Design and Applications," 6th Edition, Butterworth-Heinemann, 2014
- CIBSE Guide F, "Energy Efficiency in Buildings" — Heat Recovery Systems
- EN 308, "Heat Exchangers — Test Procedures for Establishing the Performance of Air to Air and Flue Gases Heat Recovery Devices"
- IEA, "Industrial Energy-Related Technologies and Systems (IETS) Annex XV: Industrial Excess Heat Recovery"
- Thekdi, A. and Belt, C., "Waste Heat Reduction and Recovery Options for Metals Industry," Energy Engineering, 2011
