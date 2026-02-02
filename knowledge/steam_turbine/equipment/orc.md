---
title: "Organik Rankine Cevrimi — Organic Rankine Cycle (ORC)"
category: equipment
equipment_type: steam_turbine
subtype: "ORC (Organic Rankine Cycle)"
keywords: [ORC, organic Rankine, R245fa, siloksan, n-pentan, R1233zd, dusuk sicaklik, atik isi, GWP, expander, exergy]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/equipment/micro_turbine.md, steam_turbine/economics/feasibility.md, boiler/equipment/waste_heat.md, factory/waste_heat_recovery.md, chiller/benchmarks.md]
use_when: ["Dusuk sicaklik atik isi degerlendirmesinde", "ORC fizibilite analizinde", "Buhar turbinine alternatif aranirken", "80-350 C kaynak sicakliginda guc uretimi"]
priority: medium
last_updated: 2026-01-31
---
# Organik Rankine Cevrimi — Organic Rankine Cycle (ORC)

> Son guncelleme: 2026-01-31

## Genel Bilgiler

Organik Rankine Cevrimi (ORC), su yerine dusuk kaynama noktali organik akiskanlar
kullanan bir Rankine cevrimi varyasyonudur. Dusuk ve orta sicaklikli isi kaynaklarindan
(80-350 C) elektrik uretimi icin kullanilir. Geleneksel buhar turbini bu sicaklik
araliginda verimsiz kalir cunku su, yuksek sicaklikli buhar uretimi icin optimize
edilmis bir akiskandir; ORC akiskanlari ise dusuk sicaklikta daha yuksek termodinamik
performans sunar.

- **Tip:** Organik Rankine Cevrimi (ORC)
- **Kapasite araligi:** 5 kW - 20 MW (tipik endustriyel: 50 kW - 5 MW)
- **Kaynak sicakligi:** 80 - 350 C
- **Termal verim:** %5 - 25 (kaynak sicakligina bagli)
- **Exergy verimi:** %25 - 60 (dusuk T'de buhar turbinine gore belirgin sekilde yuksek)
- **Calisma akiskanlari:** R245fa, siloksan (MDM/MM), n-pentan, R1233zd(E), toluen
- **Yaygin markalar:** Turboden (Mitsubishi), ORMAT, Enertime, Enogia, Rank, Zuccato
- **Standartlar:** EN 14511, ASHRAE 34 (akiskan siniflandirmasi), EU F-Gas Regulation

## Calisma Prensibi

### ORC Dongusu

```
ORC, klasik Rankine cevrimi ile ayni termodinamik prensibi kullanir:

1. POMPA: Sivi organik akiskan basinclandirilir
   (sivi pompalama isi << buhar turbini isi)

2. EVAPORATOR (Buharlatirici): Akiskan, isi kaynagi ile isitilarak buharlasitirilir
   - On isitma (preheater) + buharlatirma + (varsa) kizdinma (superheater)
   - Isi kaynagi: Atik gaz, sicak su, jeotermal, gunes, biyokutle baca gazi vb.

3. EXPANDER (Genlestirici/Turbin): Buhar genisler, is uretilir
   - Turbo expander (turbin tipi) veya vidali (screw) expander
   - Scroll veya pistonlu expander (kucuk kapasite icin)

4. KONDENSER: Buhar yogustirilur, isi sogutma ortamina atilir
   - Hava sogutmali veya su sogutmali kondenser
   - Rejenerator (varsa): cikis buhariyla giris sivisini on isitma
```

### ORC vs Buhar Rankine Karsilastirmasi

| Ozellik | Buhar Rankine | ORC |
|---------|:------------:|:---:|
| Calisma akiskani | Su (H2O) | Organik akiskan |
| Minimum kaynak sicakligi | ~250 C (pratik) | 80 C |
| Optimal kaynak sicakligi | 400 - 600 C | 100 - 300 C |
| Calisma basinci | 40 - 300 bar | 5 - 35 bar |
| Kizginlik gereksinimi | Zorunlu | Genellikle gereksiz |
| Turbin cikis nemi | Yas buhar (erozyon riski) | Kuru buhar (genellikle) |
| Turbin boyutu | Buyuk (yuksek hacimsel akis) | Kompakt |
| Su aritma | Gerekli (kazan su kalitesi) | Gereksiz |
| Calisma basinci (tipik) | Yuksek (>40 bar) | Dusuk (<30 bar) |
| Bakim | Karmasik (kazan + turbin) | Nispeten basit |

## Calisma Akiskanlari (Working Fluids)

### Akiskan Secim Kriterleri

Ideal ORC akiskani su ozelliklere sahip olmalidir:
- Dusuk kaynama noktasi (isi kaynagindan dusuk)
- Yuksek kritik sicaklik (kaynak sicakligina yakin veya uzerinde)
- Kuru (dry) veya izentropik doyma egrisi (yas buhar riski yok)
- Yuksek buharlasmma entalpisi (latent heat)
- Dusuk viskozite ve iyi isi transfer ozellikleri
- Dusuk GWP (Global Warming Potential) ve ODP (Ozone Depletion Potential) = 0
- Yanmaz, dusuk toksisite, kimyasal kararlilik

### Yaygin ORC Akiskanlari

| Akiskan | T_kaynama [C] | T_kritik [C] | P_kritik [bar] | GWP | ODP | Guvenlik | Kaynak T Araligi [C] |
|---------|:------------:|:------------:|:--------------:|:---:|:---:|:--------:|:---------------------:|
| R245fa (HFC-245fa) | 15.1 | 154.0 | 36.5 | 1,030 | 0 | B1 | 80 - 150 |
| R1233zd(E) (HFO) | 18.3 | 166.5 | 36.2 | 1 | 0 | A1 | 80 - 170 |
| n-Pentan (C5H12) | 36.1 | 196.6 | 33.7 | 5 | 0 | A3 (yanici) | 100 - 200 |
| Siloksan MDM | 152.5 | 290.9 | 14.2 | ~0 | 0 | -- | 200 - 350 |
| Siloksan MM | 100.3 | 245.6 | 19.4 | ~0 | 0 | -- | 150 - 280 |
| Toluen (C7H8) | 110.6 | 318.6 | 41.1 | 3 | 0 | B2 (yanici) | 200 - 350 |
| R134a (HFC-134a) | -26.1 | 101.1 | 40.6 | 1,430 | 0 | A1 | 60 - 100 |
| Siklopentan | 49.3 | 238.5 | 45.2 | 5 | 0 | A3 | 120 - 250 |

### GWP Degerlendirmesi ve Mevzuat

```
EU F-Gas Regulation (517/2014) etkileri:

Yuksek GWP akiskanlar (GWP > 150) icin kisitlamalar artmaktadir:
- R245fa (GWP = 1,030): Kademeli azaltma kapsaminda, 2030 sonrasi kisitli
- R134a (GWP = 1,430): Ayni sekilde kisitlanacak

Dusuk GWP alternatifler (onerilir):
- R1233zd(E) (GWP = 1): R245fa'nin dogrudan ikamesi, benzer performans
- n-Pentan (GWP = 5): Dusuk GWP ama yanici (ATEX bolge gerektirir)
- Siloksanlar (GWP ~0): Yuksek sicaklik ORC icin ideal

Yeni tesis seciminde GWP < 150 olan akiskanlar tercih edilmelidir.
```

## Kaynak Sicakligina Gore Performans

### Termal ve Exergy Verimi Karsilastirmasi

| Kaynak T [C] | Carnot Verimi [%] | ORC Termal Verim [%] | ORC Exergy Verimi [%] | Buhar Rankine (pratik) |
|:------------:|:-----------------:|:--------------------:|:---------------------:|:----------------------:|
| 80 | 16.8 | 4 - 7 | 25 - 40 | Uygulanamaz |
| 100 | 20.1 | 6 - 10 | 30 - 48 | Uygulanamaz |
| 120 | 23.2 | 8 - 13 | 35 - 52 | Uygulanamaz |
| 150 | 28.0 | 10 - 16 | 38 - 55 | Zor (dusuk verim) |
| 200 | 34.9 | 14 - 20 | 40 - 58 | Dusuk verim |
| 250 | 40.2 | 17 - 23 | 42 - 58 | Orta verim |
| 300 | 44.6 | 20 - 25 | 45 - 60 | Kabul edilebilir |
| 350 | 48.2 | 22 - 27 | 45 - 58 | Iyi verim |

**Kilit Kavram:** Dusuk sicakliklarda ORC'nin exergy verimi, buhar turbininden
belirgin sekilde yuksektir. Ornegin 120 C'de ORC exergy verimi %35-52 iken,
buhar turbini pratik olarak uygulanamaz. Bu, ORC'nin temel exergy avantajidir.

### Exergy Verimi Hesaplamasi

```
ORC termal verim:
eta_th_ORC = W_net / Q_giris

ORC exergy verimi:
eta_ex_ORC = W_net / Ex_isi_kaynagi

Isi kaynaginin exergisi:
Ex_isi_kaynagi = Q_kaynak x (1 - T0/T_kaynak)   [kW]

Veya daha dogru olarak (sicaklik degisken ise):
Ex_isi_kaynagi = m_kaynak x [(h_kaynak_giris - h_kaynak_cikis) - T0 x (s_kaynak_giris - s_kaynak_cikis)]

Net guc:
W_net = W_expander - W_pompa   [kW]

Tipik pompa gucu: W_expander'in %3-8'i (buhar Rankine'de %1-3)
```

## ORC Bilesenleri

### Expander (Genlestirici)

| Expander Tipi | Kapasite Araligi | Izentropik Verim [%] | Avantaj | Dezavantaj |
|---------------|:----------------:|:--------------------:|---------|------------|
| Turbo (radyal turbin) | 100 kW - 20 MW | 80 - 90 | Yuksek verim, olceklenebilir | Yuksek maliyet |
| Vidali (screw) | 10 kW - 2 MW | 55 - 75 | Yas buhar toleransi, robust | Orta verim |
| Scroll | 1 kW - 50 kW | 50 - 70 | Ucuz, basit | Kucuk kapasite siniri |
| Pistonlu | 1 kW - 500 kW | 60 - 80 | Iyi verim | Bakim, titresim |

### Esanjor (Isi Degistirici)

```
ORC evanjorleri:
1. Evaporator (buharlatirici):
   - Plakali isi degistirici (PHE) — kucuk ORC icin
   - Govde-boru (shell & tube) — buyuk ORC, yuksek sicaklik
   - Finned tube — gaz kaynaklar icin (baca gazi, egzoz)

2. Kondenser:
   - Hava sogutmali (air-cooled) — su kaynagi yoksa
   - Su sogutmali (water-cooled) — en iyi verim
   - Evaporatif (wet cooling) — orta yol

3. Rejenerator (varsa):
   - Expander cikis ile pompa cikis arasinda isi degisimi
   - %5-15 termal verim artisi saglar
   - Kuru (dry) akiskanlarda etkilidir

Isi degistirici etkinligi (effectiveness):
epsilon = Q_gercek / Q_max
Tipik: %80 - 95
```

### Pompa

```
ORC besleme pompasi:
- Tip: Santrifuj veya pozitif yer degistirme (PD)
- Calisma basinci: 5 - 35 bar
- Pompa gucu: W_net'in %3 - 8'i

Buhar Rankine ile karsilastirma:
- Buhar Rankine pompa gucu: W_net'in %1 - 3'u (cok kademeli)
- ORC pompa gucu oransal olarak yuksektir cunku akiskanin ozgul hacmi kucuk
  ve buharlasmma entalpisi dusuktur
```

## Endustriyel Uygulamalar

### Tipik Isi Kaynaklari

| Kaynak | Sicaklik [C] | Uygun Akiskan | Tipik ORC Gucu | Sektor |
|--------|:-----------:|:-------------:|:--------------:|--------|
| Cimento firini baca gazi | 250 - 400 | Siloksan, toluen | 1 - 10 MW | Cimento |
| Cam firini atik isi | 300 - 500 | Siloksan | 0.5 - 5 MW | Cam |
| Celik dokum atik isi | 200 - 350 | Siloksan, n-pentan | 0.5 - 5 MW | Metal |
| Motor egzozu (CHP) | 350 - 500 | Siloksan | 50 - 500 kW | CHP |
| Motor ceket suyu | 80 - 95 | R245fa, R1233zd | 20 - 200 kW | CHP |
| Jeotermal kaynak | 80 - 180 | R245fa, R1233zd | 0.1 - 10 MW | Enerji |
| Biyokutle kazan baca gazi | 150 - 250 | R245fa, n-pentan | 50 - 500 kW | Tarim, orman |
| Gunes (CSP) | 150 - 350 | Siloksan, toluen | 0.1 - 5 MW | Enerji |
| Kompressor atik isi | 80 - 120 | R245fa, R1233zd | 10 - 100 kW | Imalat |

### Turk Endustriyel Tesislerde Potansiyel

```
Turkiye'deki yuksek potansiyelli sektorler:

1. CIMENTO: 30+ tesis, her birinde 2-10 MW ORC potansiyeli
   - Klinker sogutucusu ve farin degirmeni atik isi
   - Tipik geri odeme: 3-5 yil

2. SERAMIK VE CAM: Atik isi yuksek ama sicaklik degisken
   - 150-400 C araliginda cesitli kaynaklar
   - Tipik geri odeme: 4-6 yil

3. CELIK: Elektrik ark ocagi (EAF) ve hadde isi
   - Kesikli calisma, yuk profili degisken
   - Tipik geri odeme: 4-7 yil

4. JEOTERMAL: Bati Anadolu'da 80-170 C kaynaklar
   - Binary cevrim olarak ORC yaygin
   - MTA verilerine gore 1000+ MW potansiyel

5. BIYOKUTLE: Zeytin pisrina, findik kabugu, orman artikulari
   - Kucuk olcekli ORC (50-500 kW) uygun
   - Koylerde dagilmis uretim potansiyeli
```

## Ekonomik Analiz

### Spesifik Yatirim Maliyeti

| ORC Kapasitesi [kW] | Spesifik Maliyet [EUR/kW] | Toplam Yatirim [EUR] | Not |
|:--------------------:|:-------------------------:|:--------------------:|-----|
| 50 | 4,000 - 6,000 | 200,000 - 300,000 | Mikro ORC |
| 100 | 3,500 - 5,000 | 350,000 - 500,000 | Kucuk ORC |
| 500 | 2,500 - 3,500 | 1,250,000 - 1,750,000 | Orta ORC |
| 1,000 | 2,000 - 3,000 | 2,000,000 - 3,000,000 | Standart |
| 5,000 | 1,500 - 2,500 | 7,500,000 - 12,500,000 | Buyuk ORC |
| 10,000 | 1,200 - 2,000 | 12,000,000 - 20,000,000 | Buyuk endustriyel |

### Geri Odeme Hesaplamasi

```
Yillik elektrik uretimi:
E_yillik = W_net x calisma_saati x kapasite_faktoru   [kWh/yil]

Yillik gelir:
Gelir = E_yillik x c_elektrik   [EUR/yil]

Yatirim geri odeme suresi:
PBP = Yatirim / (Gelir - Isletme_maliyeti)   [yil]

Ornek:
  W_net = 500 kW, calisma = 7,500 saat/yil, CF = 0.85
  E_yillik = 500 x 7,500 x 0.85 = 3,187,500 kWh/yil
  c_elektrik = 0.10 EUR/kWh
  Gelir = 3,187,500 x 0.10 = 318,750 EUR/yil
  Isletme = %2-3 yatirim = ~45,000 EUR/yil
  Yatirim = 1,500,000 EUR
  PBP = 1,500,000 / (318,750 - 45,000) = 5.5 yil

  LCOE = (Yatirim x CRF + Isletme) / E_yillik
  CRF = i x (1+i)^n / [(1+i)^n - 1]  (i=%8, n=20 yil: CRF=0.1019)
  LCOE = (1,500,000 x 0.1019 + 45,000) / 3,187,500 = 0.062 EUR/kWh
```

## Exergy Avantaji — Dusuk Sicaklikta ORC vs Buhar Turbini

### Karsilastirmali Analiz

```
Senaryo: 150 C sicak su kaynagi, 500 kW_th isi icerigi

Exergy icerigi:
Ex_kaynak = 500 x (1 - 298.15 / 423.15) = 500 x 0.296 = 148 kW

1. ORC (R245fa, eta_ex = 45%):
   W_net_ORC = 148 x 0.45 = 66.6 kW
   eta_th_ORC = 66.6 / 500 = %13.3

2. Buhar turbini (pratik olarak zor, eta_ex = 20%):
   W_net_buhar = 148 x 0.20 = 29.6 kW
   eta_th_buhar = 29.6 / 500 = %5.9

3. Fark:
   ORC, buhar turbininden %125 daha fazla guc uretir!

Neden ORC daha iyi?
- ORC akiskani dusuk sicaklikta daha uygun termodinamik ozellikler gosterir
- Kizginlik gerektirmez (buhar turbini kizginlik olmadan yas buhar riski)
- Daha dusuk basinclarda calisir (ekipman basitlesmesi)
- Akiskan secimi ile kaynak sicakligina optimize edilir
```

## Varsayilan Degerler (Olcum Yoksa)

| Parametre | Varsayilan | Aciklama |
|-----------|:---------:|----------|
| Kaynak sicakligi | 150 C | Tipik endustriyel atik isi |
| Sogutma sicakligi | 30 C | Hava sogutmali kondenser |
| Akiskan | R1233zd(E) | Dusuk GWP, guvenli |
| Expander izentropik verim | %80 | Turbo expander |
| Pompa verimi | %70 | Standart |
| Rejenerator etkinligi | %85 | Varsa |
| Kapasite faktoru | %85 | Surekli kaynak |
| Yillik calisma saati | 7,500 saat/yil | Surekli proses |
| Isletme maliyeti | Yatirimin %2-3'u | Yillik bakim |
| Elektrik fiyati | 0.10 EUR/kWh | Turkiye endustriyel tarife |

## İlgili Dosyalar

- [Turbin Formulleri](../formulas.md) -- ORC exergy hesaplamalari
- [Benchmarklar](../benchmarks.md) -- ORC verimlilik karsilastirmasi
- [Mikro Turbin](micro_turbine.md) -- Kucuk olcekli alternatif
- [Fizibilite](../economics/feasibility.md) -- ORC ekonomik degerlendirme
- [Atik Isi Kazani](../../boiler/equipment/waste_heat.md) -- HRSG ile karsilastirma
- [Atik Isi Geri Kazanimi](../../factory/waste_heat_recovery.md) -- Fabrika seviyesinde WHR
- [Chiller Benchmarklari](../../chiller/benchmarks.md) -- Absorpsiyon chiller entegrasyonu
- [Kompressor Formulleri](../../compressor/formulas.md) -- Kompressor atik isi kaynagi

## Referanslar

1. Quoilin, S. et al. (2013). "Techno-economic survey of Organic Rankine Cycle (ORC) systems," *Renewable and Sustainable Energy Reviews*, 22, 168-186.
2. Tchanche, B.F. et al. (2011). "Low-grade heat conversion into power using organic Rankine cycles — A review," *Renewable and Sustainable Energy Reviews*, 15, 3963-3979.
3. Macchi, E. & Astolfi, M. (2017). *Organic Rankine Cycle (ORC) Power Systems*, Woodhead Publishing.
4. Colonna, P. et al. (2015). "Organic Rankine Cycle power systems: From the concept to current technology, applications, and an outlook to the future," *ASME J. Eng. Gas Turbines Power*, 137(10), 100801.
5. Dincer, I. & Rosen, M.A. (2021). *Exergy*, 3rd Edition, Elsevier.
6. Lemmon, E.W. et al. (2023). *REFPROP 10.0*, NIST Standard Reference Database.
7. EU Regulation 517/2014. *F-Gas Regulation* — Fluorinated greenhouse gas control.
8. ASHRAE Standard 34 (2022). *Designation and Safety Classification of Refrigerants*.
9. Tartiere, T. & Astolfi, M. (2017). "A world overview of the organic Rankine cycle market," *Energy Procedia*, 129, 2-9.
10. Imran, M. et al. (2018). "Recent research trends in organic Rankine cycle technology: A bibliometric approach," *Renewable and Sustainable Energy Reviews*, 81, 552-562.
