---
title: "Kurutma Firini Enerji Denetimi (Industrial Dryer Energy Audit)"
category: dryer
equipment_type: dryer
keywords: [enerji denetimi, kurutma firini, dryer audit, exergy analizi, SMER, SEC, ISO 13579, saha olcumu, benchmark, ATEX, termal kamera, psikrometri, enerji dengesi, exergy dengesi]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/equipment/tunnel_dryer.md, dryer/equipment/spray_dryer.md, dryer/equipment/belt_dryer.md, dryer/equipment/rotary_dryer.md, dryer/equipment/fluidized_bed.md, dryer/equipment/heat_pump_dryer.md, dryer/equipment/drum_dryer.md, dryer/equipment/infrared_dryer.md, dryer/solutions/exhaust_heat_recovery.md, dryer/solutions/air_recirculation.md, dryer/solutions/heat_pump_retrofit.md, dryer/solutions/mechanical_dewatering.md, dryer/solutions/insulation.md, dryer/solutions/temperature_optimization.md, dryer/solutions/solar_preheating.md]
use_when: ["Kurutma firini enerji denetimi planlanirken", "Saha olcum metodolojisi belirlenirken", "Denetim raporu hazirlama asamasinda", "Exergy ve enerji dengesi kurulurken", "KPI hesaplamalari yapilirken"]
priority: medium
last_updated: 2026-02-01
---
# Kurutma Firini Enerji Denetimi (Industrial Dryer Energy Audit)

> Son guncelleme: 2026-02-01

## Genel Bakis (Overview)

Bu belge, endustriyel kurutma firinlarinin enerji ve exergy verimliligini sistematik olarak degerlendirmek icin kapsamli bir denetim proseduru tanimlar. Metodoloji ISO 13579 (Industrial furnaces and associated processing equipment -- Energy balance and efficiency calculation method), ISO 50002:2014 (Energy Audits), EU BREF referans belgelerine ve endustri en iyi uygulamalarina dayanir.

Kurutma prosesleri, endustriyel tesislerde toplam enerji tuketiminin %20-60'ini olusturabilir. Kurutma dogasi geregi exergy-destructive bir prosestir: yuksek kaliteli enerji (dogalgaz, buhar) dusuk kaliteli is icin (suyun buharlasmasi ~100 C) kullanilir. Bu nedenle exergy verimi tipik olarak %5-30 arasindadir, enerji verimi ise %35-65 arasindadir. Bu buyuk fark, denetimin enerji dengesinin otesine gecerek exergy dengesi ile tamamlanmasi gerektigini gosterir.

Denetim sureci bes asamadan olusur: on hazirlik, saha calismalari, veri analizi (enerji ve exergy dengeleri), raporlama ve dogrulama.

---

## 1. Denetim Oncesi Hazirlik (Pre-Audit Preparation)

### 1.1 Veri Toplama Kontrol Listesi (Data Collection Checklist)

Saha ziyareti oncesinde asagidaki bilgiler toplanmalidir:

| Kategori | Toplanacak Veriler | Kaynak |
|----------|--------------------|--------|
| Ekipman envanteri | Kurutucu tipi, uretici, model, yasi, nominal kapasite | Nameplate, bakim kayitlari |
| Nominal degerler | Kapasite (kg/saat), giris hava sicakligi (C), enerji tuketimi (kW) | Teknik dokumanlar |
| Uretim verileri | Urun debisi (kg/saat), giris/cikis nem (%), calisma saati (saat/yil) | Uretim raporlari |
| Enerji faturalari | En az 12 aylik dogalgaz, elektrik, buhar tuketimleri | Muhasebe/enerji yonetimi |
| Bakim kayitlari | Son bakim tarihi, sik ariza turleri, yedek parca tuketimi | CMMS / bakim birimi |
| Proses akis semasi (PFD) | Kurutma hattinin seması, ekipman yerlesimi | Muhendislik arsivi |
| Urun spesifikasyonlari | Giris/cikis nem hedefleri, urun cesitleri, kalite gereksinimleri | Kalite/uretim birimi |
| Mevsimsel degisimler | Uretim hacmi ve ortam kosullarindaki yillik degisim | Uretim planlama |

### 1.2 Gerekli Olcum Cihazlari (Required Instruments)

Denetim icin gerekli enstrumantasyon:

| Cihaz | Ornek Model | Amaci | Yaklasik Maliyet (EUR) |
|-------|-------------|-------|------------------------|
| **Termal kamera (IR thermal camera)** | FLIR E96, Testo 890 | Izolasyon hasari, sicak kacak noktasi, yuzey sicakligi haritalama | 5,000-20,000 |
| **Higrometre / sicaklik-nem olcer** | Vaisala HMT330, Testo 635 | Hava sicakligi ve bagil nemi (giris, cikis, ortam) | 800-3,000 |
| **Anemometre (kanatli/sicak telli)** | Testo 405i, TSI 9565 | Hava hizi ve debi olcumu (kanal, egzoz) | 100-1,500 |
| **Pitot tupu + diferansiyel manometre** | Testo 512, Dwyer 166T | Kanal hava akis hizi ve debisi | 200-600 |
| **IR termometre (nokta olcum)** | Fluke 62 MAX+ | Yuzey sicakligi hizli olcumu | 50-150 |
| **Termokupl veri kaydedici** | Yokogawa GP10, Fluke 1586A | Coklu nokta sicaklik kaydı (uzun sureli) | 2,000-8,000 |
| **Guc analizoru** | Fluke 435-II, Hioki PW3198 | Fan, motor, isitici elektrik guc profilleme | 4,000-8,000 |
| **Gaz analizoru (yanma)** | Testo 340, Bacharach PCA3 | Egzoz gazi bilesimi: O2, CO2, CO, NOx, baca sicakligi | 3,000-8,000 |
| **Urun nem olcer** | Sartorius MA37, Ohaus MB45 | Giris/cikis urun nem icerigi (etuv yontemi) | 1,500-5,000 |
| **NIR nem sensoru (hat ustu)** | NDC MM710e | Surekli hat ustu nem olcumu | 5,000-15,000 |
| **Gaz debimetre** | Elster BK-G, Itron | Dogalgaz tuketim olcumu | 500-2,000 |
| **Veri kaydedici (datalogger)** | Onset HOBO, Yokogawa | Uzun sureli sicaklik, nem, basinc kaydi | 500-2,000 |
| **Dijital diferansiyel manometre** | Testo 510i | Kurutucu boyunca basinc dususu | 150-300 |
| **Kamera (belgeleme)** | Akilli telefon / dijital kamera | Durum ve bulgu fotografi, nameplate kaydi | -- |

### 1.3 Guvenlik Hususlari (Safety Considerations)

#### ATEX Bolgeleri (Yanabilir Tozlar -- Combustible Dusts)

Kurutma proseslerinde yanabilir toz riski ciddi bir guvenlik unsurudur. ATEX Direktifi 2014/34/EU kapsaminda:

| Parametre | Dikkate Alinacak Husus |
|-----------|------------------------|
| **Toz patlama riski** | Un, sut tozu, tahil tozu, ahsap tozu, kimyasal tozlar icin ATEX Zone 20/21/22 degerlendirmesi |
| **Ex-proof ekipman gerekliligi** | ATEX zonlarinda yalnizca uygun kategorideki olcum cihazlari kullanilabilir |
| **Minimum patlama konsantrasyonu (MEC)** | Toz turune gore MEC degerini bilin, havalandirma yeterliligi kontrolu |
| **Patlama basinc tahliyesi** | Kurutucu uzerinde patlama panelleri ve tahliye kanallarinin kontrolu |
| **Inertleme sistemi (varsa)** | N2 veya CO2 inertleme sisteminin calisma durumu |

#### Genel Guvenlik Kontrol Listesi

- [ ] Calisma izni (work permit) alinmali -- sicak calisma, yuksekte calisma
- [ ] Kisisel koruyucu ekipman (KKE): isi eldiveni, koruyucu gozluk, kulaklık, toz maskesi
- [ ] Sicak yuzey uyari isaretleri kontrol edilmeli (>60 C yuzeyler yanma riski)
- [ ] Elektrik panolarina erisim icin yetkili personel esliginde calisma
- [ ] Donen ekipman (fan, konveyor) civarinda guvenlik mesafesi
- [ ] Kapalı mekan girisi (confined space) proseduru -- buyuk kurutma odalari icin
- [ ] Acil durdurma butonlarinin konumu ve calisma durumu
- [ ] Yangin sondurme ekipmaninin erisilebilirligi

#### Operator Gorusme Sorulari (Pre-Audit Interview)

1. Kac kurutucu kurulu? Tipleri ve yaslari nedir?
2. Tipik kurutma sicakligi ve suresi ne kadar?
3. Giris ve cikis nem degerleri olculuyor mu? Hangi yontemle?
4. Son donemde urun kalitesi sorunlari (asiri kurutma, dusuk kurutma) yasandi mi?
5. Egzoz havasi geri kazanimi veya geri devir (recirculation) yapiliyor mu?
6. Izolasyon durumu nasil? Son ne zaman kontrol edildi?
7. Fan ve motorlarin yasi? Degisken hiz suruculeri (VSD) mevcut mu?
8. Kurutma oncesi mekanik su alma (pres, santrifuj) yapiliyor mu?
9. Bilinen isil kayip veya sicak nokta (hotspot) sorunlari var mi?
10. Gelecekte uretim artisi veya urun degisikligi planlaniyor mu?

---

## 2. Olcum Noktalari (Measurement Points)

### 2.1 Giris Havasi Olcumleri (Inlet Air)

| Parametre | Sembol | Birim | Olcum Noktasi | Cihaz |
|-----------|--------|-------|---------------|-------|
| Sicaklik | T_in | C | Isitici sonrasi, kurutucu girisinde | Termokupl / higrometre |
| Bagil nem | RH_in | % | Ayni nokta | Higrometre |
| Nem orani | w_in | kg_su/kg_kuru_hava | Hesaplama (T_in, RH_in'den) | -- |
| Hava debisi | V_in | m3/saat | Giris kanali (anemometre/pitot) | Anemometre |
| Kutle debisi | m_air_in | kg/saat | Hesaplama (V_in x rho) | -- |

### 2.2 Egzoz Havasi Olcumleri (Exhaust Air)

| Parametre | Sembol | Birim | Olcum Noktasi | Cihaz |
|-----------|--------|-------|---------------|-------|
| Sicaklik | T_out | C | Kurutucu cikis kanali, fan oncesi | Termokupl / higrometre |
| Bagil nem | RH_out | % | Ayni nokta | Higrometre |
| Nem orani | w_out | kg_su/kg_kuru_hava | Hesaplama (T_out, RH_out'dan) | -- |
| Hava debisi | V_out | m3/saat | Egzoz kanali (pitot tupu) | Pitot + manometre |
| Kutle debisi | m_air_out | kg/saat | Hesaplama (V_out x rho) | -- |

> **Not:** Egzoz neminin dusuk olmasi (RH < %40-50) onemli bir geri devir (recirculation) potansiyeline isaret eder. Bkz. `dryer/psychrometrics.md`

### 2.3 Urun Olcumleri (Product)

| Parametre | Sembol | Birim | Yontem | Aciklama |
|-----------|--------|-------|--------|----------|
| Giris nem icerigi | M_in | % (wb veya db) | Etuv (ISO 712), NIR, mikrodalga | Kurutma oncesi urun nemi |
| Cikis nem icerigi | M_out | % (wb veya db) | Ayni yontem | Kurutma sonrasi urun nemi |
| Urun debisi (giris) | m_product_in | kg/saat | Bant kantari, debimetre | Kurutucuya giren urun |
| Urun debisi (cikis) | m_product_out | kg/saat | Bant kantari | Kurutucudan cikan urun |
| Urun sicakligi (giris) | T_product_in | C | Termokupl / IR | Giris urun sicakligi |
| Urun sicakligi (cikis) | T_product_out | C | Termokupl / IR | Cikis urun sicakligi |

### 2.4 Yuzey Sicakliklari (Surface Temperatures)

IR termal kamera ile kurutucu dis yuzey sicakliklari haritalanir:

| Bolge | Beklenen T_surface (C) | Alarm Esigi | Aciklama |
|-------|------------------------|-------------|----------|
| Kurutucu govde (iyi yalitim) | < 40 | > 50 | Ortam + 15 C idealdir |
| Kurutucu govde (hasar) | > 60 | > 80 | Izolasyon onarimi gerekli |
| Kapak / kapi bolgesi | 40-60 | > 70 | Contalar kontrol edilmeli |
| Hava kanallari | < 45 | > 55 | Kanal izolasyonu kontrolu |
| Boru ve vanalar | < 50 | > 60 | Izolasyon eksikligi |
| Brulor bolgesi | 50-80 | > 100 | Yanma kaybi gostergesi |

### 2.5 Yakit / Enerji Tuketimi (Fuel / Energy Consumption)

| Enerji Kaynagi | Olcum | Birim | Cihaz |
|----------------|-------|-------|-------|
| Dogalgaz | Debi | Nm3/saat | Gaz debimetre, sayac |
| LPG | Debi | kg/saat | Kütlesel debimetre |
| Buhar | Debi, basinc, sicaklik | ton/saat, bar, C | Buhar debimetre, manometre |
| Elektrik (fanlar) | Guc | kW | Guc analizoru |
| Elektrik (tasiyicilar) | Guc | kW | Guc analizoru |
| Elektrik (kontrol/yardimci) | Guc | kW | Guc analizoru |

### 2.6 Fan Gucu Olcumleri (Fan Power)

| Parametre | Birim | Olcum Noktasi |
|-----------|-------|---------------|
| Fan motor gucu (aktif) | kW | Motor panosu (guc analizoru) |
| Fan devri | rpm | Takometre |
| Fan basinc artisi | Pa | Diferansiyel manometre (fan giris-cikis) |
| VSD frekansi (varsa) | Hz | VSD paneli |

---

## 3. Enerji Dengesi (Energy Balance)

### 3.1 Kutle Dengesi (Mass Balance)

Enerji dengesinden once kutle dengesi kurulmalidir:

```
Buharlasmis su miktari:
m_water = m_product_in x (M_in - M_out) / (1 - M_out)  [kg/saat]

Kuru urun debisi:
m_dry = m_product_in x (1 - M_in)  [kg/saat]

Dogrulama:
m_product_out = m_product_in - m_water  [kg/saat]

Hava tarafi kutle dengesi:
m_air_dry x (w_out - w_in) = m_water  [kg/saat]
```

> Detayli kutle dengesi hesaplamalari icin bkz. `dryer/formulas.md`

### 3.2 Enerji Girisleri (Energy Inputs)

```
Q_fuel   = m_fuel x LHV                    [kW]  (yakit yakilan kurutucularda)
Q_steam  = m_steam x (h_steam_in - h_cond)  [kW]  (buhar isitmali)
W_fan    = fan elektrik gucu                [kW]
W_conv   = konveyor / tasiyici gucu         [kW]
W_aux    = yardimci ekipman gucu            [kW]

Q_total_input = Q_fuel + Q_steam + W_fan + W_conv + W_aux  [kW]
```

### 3.3 Enerji Cikislari ve Kayiplari (Energy Outputs and Losses)

```
Q_evap    = m_water x h_fg              [kW]  (faydali: suyun buharlasmasi)
Q_exhaust = m_air x cp_air x (T_out - T_amb) + m_water x cp_vapor x (T_out - T_amb)
                                         [kW]  (egzoz kaybi -- en buyuk)
Q_product = m_product x cp_product x (T_product_out - T_product_in)
                                         [kW]  (urun sensible isitma)
Q_wall    = h_combined x A_surface x (T_surface - T_amb)
                                         [kW]  (radyasyon + konveksiyon kaybi)
Q_leakage = hava kacagi kaybi            [kW]  (tahmin veya olcum)
Q_other   = Q_total - (Q_evap + Q_exhaust + Q_product + Q_wall + Q_leakage)
                                         [kW]  (diger / aciklanamayan)
```

### 3.4 Enerji Verimi (Energy Efficiency)

```
eta_energy = Q_evap / Q_total_input x 100  [%]

Tipik degerler:
  Konvektif kurutucu:  %35-55
  Bant kurutucu:       %40-60
  Isi pompali:         %60-85
```

### 3.5 Tipik Enerji Dagilimi (Konvektif Kurutucu)

| Kalem | Pay (%) | Aciklama |
|-------|---------|----------|
| Faydali is (buharlasmistirma) | 35-50 | Hedef: maximize et |
| Egzoz havasi kaybi | 25-40 | En buyuk kayip -- geri kazanilabilir |
| Urun sensible isitma | 5-10 | Urun sicakliga cikartma |
| Duvar / yuzey kayiplari (radyasyon + konveksiyon) | 3-10 | Izolasyon ile azalt |
| Hava kacagi kaybi (leakage) | 2-5 | Contalar, kapilar |
| Diger (aciklanamayan) | 3-8 | Olcum belirsizligi dahil |

---

## 4. Exergy Dengesi (Exergy Balance)

### 4.1 Exergy Girisleri (Exergy Inputs)

```
Yakit exergy'si (dogalgaz):
Ex_fuel = m_fuel x LHV x gamma  [kW]
  gamma ~ 1.04 (dogalgaz icin exergy/enerji orani)

Buhar exergy'si:
Ex_steam = m_steam x [(h_in - h_out) - T0 x (s_in - s_out)]  [kW]

Elektrik exergy'si (fan + yardimci):
Ex_elec = W_fan + W_conv + W_aux  [kW]
  (elektrik = saf exergy, %100 exergy icerigi)

Toplam exergy girdisi:
Ex_total_input = Ex_fuel + Ex_steam + Ex_elec  [kW]
```

### 4.2 Buharlasmma Exergy'si -- Faydali Cikis (Exergy of Evaporation)

```
Ex_evap = m_water x [h_fg - T0 x s_fg]  [kW]

Cesitli sicakliklarda:
  T0 = 298.15 K (25 C)

| T_evap (C) | h_fg (kJ/kg) | s_fg (kJ/kg.K) | ex_evap (kJ/kg) | ex/h_fg (%) |
|------------|-------------|----------------|----------------|-------------|
| 40         | 2,406       | 7.685          | 115            | 4.8         |
| 60         | 2,358       | 7.078          | 247            | 10.5        |
| 80         | 2,309       | 6.537          | 360            | 15.6        |
| 100        | 2,257       | 6.048          | 454            | 20.1        |
```

> **Kritik Gozlem:** 60 C'de buharlasmma exergy'si yalnizca 247 kJ/kg iken gizli isi 2,358 kJ/kg'dir. Buharlasmma enerjisinin yalnizca %10.5'i is uretme kapasitesine sahiptir. Bu, kurutmanin neden inherent olarak exergy-destructive oldugunu gosterir.

### 4.3 Exergy Yikimi (Exergy Destruction Breakdown)

```
1. Yanma tersinmezligi (combustion irreversibility):
   Ex_dest_combustion = Ex_fuel - Q_heater x (1 - T0/T_flame)  [kW]
   Tipik pay: %15-25 toplam exergy girdisinin

2. Isi transfer tersinmezligi (heat transfer irreversibility):
   Ex_dest_HT = Q_heater x [(1 - T0/T_source) - (1 - T0/T_air)]  [kW]
   Tipik pay: %10-20

3. Kurutma prosesi tersinmezligi (drying process irreversibility):
   Ex_dest_drying = kutle transferi ve karisma tersinmezlikleri  [kW]
   Tipik pay: %20-35

4. Egzoz exergy kaybi (exhaust exergy loss):
   Ex_loss_exhaust = m_air x cp x [(T_ex - T0) - T0 x ln(T_ex/T0)]
                   + nem bileseni exergy'si  [kW]
   Tipik pay: %25-40 (EN BUYUK GERI KAZANIM FIRSATI)

5. Govde / yuzey exergy kaybi:
   Ex_loss_wall = Q_wall x (1 - T0/T_surface)  [kW]
   Tipik pay: %3-10

6. Fan ve yardimci ekipman tersinmezligi:
   Ex_dest_fan = W_fan - Ex_kinetic_useful  [kW]
   Tipik pay: %2-5
```

### 4.4 Exergy Verimi (Exergy Efficiency)

```
psi_exergy = Ex_evap / Ex_total_input x 100  [%]

Kurutucu tipine gore tipik exergy verimi:
| Kurutucu Tipi         | psi_exergy (%) |
|-----------------------|----------------|
| Konvektif tunel/bant  | 5-15           |
| Doner kurutucu        | 8-18           |
| Akiskan yatak         | 10-20          |
| Sprey kurutucu        | 5-15           |
| Silindir kurutucu     | 12-25          |
| Isi pompali           | 15-30          |
| Kizgin buhar (SSD)    | 20-40          |
```

> Detayli exergy hesaplamalari icin bkz. `dryer/formulas.md`

---

## 5. Performans Gostergeleri (Key Performance Indicators -- KPIs)

### 5.1 SMER -- Spesifik Nem Uzaklastirma Orani (Specific Moisture Extraction Rate)

Kurutma verimliliginin en pratik gostergesi:

```
SMER = m_water / Q_total_input  [kg_su/kWh]

Burada:
  m_water = buharlasmis su miktari [kg/saat]
  Q_total_input = toplam enerji tuketimi [kW]

Olcum verisinden hesaplama:
  m_water = m_product_in x (M_in - M_out) / (1 - M_out)
  Q_total = (gaz sayaci okumasi x LHV / 3600) + W_elec_toplam

Benchmark siniflandirmasi:
  Cok iyi:   > 1.0 kg/kWh (konvektif); > 2.0 (isi pompali)
  Iyi:       0.7-1.0 kg/kWh
  Ortalama:  0.5-0.7 kg/kWh
  Kotu:      < 0.5 kg/kWh
```

### 5.2 SEC -- Spesifik Enerji Tuketimi (Specific Energy Consumption)

```
SEC = Q_total_input / m_water  [kWh/kg_su]

Bu, SMER'in tersidir: SEC = 1 / SMER

Alternatif bazlar:
  SEC_urun = Q_total / m_product_out  [kWh/kg_urun]
  SEC_kuru = Q_total / m_dry_solid    [kWh/kg_kuru_kati]
```

### 5.3 Enerji Verimi (Energy Efficiency -- First Law)

```
eta_energy = (m_water x h_fg) / Q_total_input x 100  [%]

Olcum verisinden:
  h_fg ~ 2,257 kJ/kg (100 C'de) veya sicakliga gore tablo
  Q_total_input = toplam olculen enerji girisi [kW]
```

### 5.4 Exergy Verimi (Exergy Efficiency -- Second Law)

```
psi_exergy = Ex_evap / Ex_total_input x 100  [%]

Olcum verisinden:
  Ex_evap = m_water x ex_evap_specific (sicakliga gore tablo)
  Ex_total_input = Ex_fuel + Ex_steam + W_elec
```

### 5.5 KPI Ozet Tablosu

| KPI | Formul | Birim | Dusuk | Ortalama | Iyi | Mukemmel | Olcum Sikligi |
|-----|--------|-------|-------|----------|-----|----------|---------------|
| SMER | m_water / Q_total | kg/kWh | < 0.5 | 0.5-0.8 | 0.8-1.2 | > 1.2 | Haftalik |
| SEC | Q_total / m_water | kWh/kg | > 2.0 | 1.3-2.0 | 0.8-1.3 | < 0.8 | Haftalik |
| Enerji verimi | Q_evap / Q_total | % | < 40 | 40-55 | 55-70 | > 70 | Aylik |
| Exergy verimi | Ex_evap / Ex_total | % | < 8 | 8-15 | 15-22 | > 22 | Aylik |
| Egzoz sicakligi | T_exhaust | C | > 130 | 100-130 | 70-100 | < 70 | Surekli |
| Egzoz bagil nem | RH_exhaust | % | < 30 | 30-50 | 50-70 | > 70 | Surekli |
| Duvar kaybi orani | Q_wall / Q_total | % | > 10 | 5-10 | 3-5 | < 3 | Ceyreklik |

---

## 6. Yaygin Bulgular (Common Findings)

### 6.1 Asiri Kurutma (Over-Drying)

**Belirti:** Cikis urun nemi hedefin cok altinda (ornegin hedef %10, gercek %6-7).

**Neden:** Kontrol sisteminin yetersizligi, sabit kurutma parametreleri, nem sensoru sapması.

**Etki:** Her %1 asiri kurutma ~ %3-5 enerji israfi + urun kalite/agirlik kaybi.

**Oneri:** Hat ustu nem sensoru (NIR) ve otomatik sicaklik kontrolu. Bkz. `dryer/solutions/temperature_optimization.md`

### 6.2 Asiri Yuksek Hava Sicakligi (Excessive Air Temperature)

**Belirti:** Kurutma havasi sicakligi, urun gereksiniminden cok yuksek (ornegin urun 80 C'ye dayanir, hava 150 C).

**Neden:** Tek kademeli isitma, sicaklik optimizasyonu yapilmamis, eski brulor kontrol sistemi.

**Etki:** Her 10 C asiri sicaklik ~ %2-5 enerji israfi + exergy yikimi artisi.

**Oneri:** Sicakligi urun kalitesini bozmadan minimize et. Cok kademeli kurutma degerlendir. Bkz. `dryer/solutions/temperature_optimization.md`

### 6.3 Zayif Izolasyon (Poor Insulation)

**Belirti:** IR termografi ile yuzey sicakligi > 60 C olan bolgeler, gorulebilir izolasyon hasari.

**Neden:** Mekanik hasar, yaslanma, nem emilimi, eksik izolasyon.

**Etki:** Yuzey kayiplari toplam enerjinin %3-10'u olabilir.

**Oneri:** Hasar gormus izolasyonun onarimi/yenilenmesi. Tipik geri odeme: 0.5-1.5 yil. Bkz. `dryer/solutions/insulation.md`

### 6.4 Geri Devir Yapilmamasi (No Air Recirculation)

**Belirti:** Egzoz havasi dusuk nemde (RH < %40-50) dogrudan atmosfere atiliyor.

**Neden:** Geri devir sistemi yok veya devre disi, kontaminasyon endisesi.

**Etki:** Isitma enerjisinin %10-25'i geri kazanilabilir.

**Oneri:** Kısmi geri devir sistemi kurulumu. Egzoz nemi izlenerek geri devir orani optimize edilmeli. Bkz. `dryer/solutions/air_recirculation.md`

### 6.5 Hava Kacaklari (Air Leaks)

**Belirti:** Kurutucu kapilarinda, contalarinda, kanal baglanti noktalarinda sicak hava kacagi.

**Neden:** Conta asınması, mekanik deformasyon, bakim yetersizligi.

**Etki:** Kacak hava hem enerji kaybi hem dengesiz kurutma yaratir (%2-8 kayip).

**Oneri:** Contlarin periyodik kontrolu ve degisimi. IR termografi ile kacak tespiti.

### 6.6 Egzoz Isi Geri Kazanimi Yok (No Exhaust Heat Recovery)

**Belirti:** Egzoz havasi > 80 C'de direkt atmosfere veriliyor.

**Neden:** Geri kazanim ekipmani kurulmamis veya arızalı.

**Etki:** En buyuk kayip kalemi -- toplam enerjinin %25-40'i.

**Oneri:** Hava-hava esuanjoru veya kondenser kurulumu. Bkz. `dryer/solutions/exhaust_heat_recovery.md`

### 6.7 Mekanik On Su Alma Yapilmamasi (No Mechanical Pre-Dewatering)

**Belirti:** Yuksek nemli urun (> %60) direkt termik kurutmaya veriyor.

**Neden:** Mekanik su alma ekipmani yok, proses tasarimi buna uygun degil.

**Etki:** 1 kg suyu mekanik olarak almak icin ~7 kJ, termik olarak ~2,600 kJ (~370 kat fark).

**Oneri:** Pres, santrifuj veya filtre ile on su alma degerlendirilmeli. Bkz. `dryer/solutions/mechanical_dewatering.md`

### 6.8 Ozet -- Tipik Bulgular ve Tasarruf Potansiyeli

| Bulgu | Tipik Yakit Tasarrufu | Yatirim Seviyesi | Geri Odeme |
|-------|-----------------------|------------------|------------|
| Egzoz isi geri kazanimi | %10-25 | 15,000-40,000 EUR | 1.0-2.0 yil |
| Hava geri deviri | %5-15 | 5,000-15,000 EUR | 0.5-1.5 yil |
| Izolasyon iyilestirme | %3-8 | 3,000-10,000 EUR | 0.5-1.5 yil |
| Sicaklik optimizasyonu | %5-10 | 0-2,000 EUR | 0-0.5 yil |
| Mekanik on su alma | %10-30 | 10,000-50,000 EUR | 1.0-2.5 yil |
| Fan VSD eklenmesi | %3-8 | 5,000-25,000 EUR | 1.0-3.0 yil |
| Isi pompasi retrofit | %30-50 | 50,000-200,000 EUR | 2.0-4.0 yil |

---

## 7. Denetim Raporu Sablonu (Audit Report Template)

### 7.1 Yonetici Ozeti Formati (Executive Summary -- 1 sayfa)

```
YONETICI OZETI

Tesis:          [Tesis adi ve konumu]
Denetim tarihi: [Baslangic - bitis]
Denetim kapsamı: [Kurutucu sayisi ve tipleri]

MEVCUT DURUM:
  Toplam kurulu kapasite:     _____ kW
  Yillik enerji tuketimi:     _____ kWh/yil
  Yillik enerji maliyeti:     _____ EUR/yil
  Ortalama SMER:              _____ kg/kWh
  Ortalama exergy verimi:     _____ %

TEMEL BULGULAR (en onemli 3-5 madde):
  1. [Bulgu] -- [etki: kWh/yil, EUR/yil]
  2. [Bulgu] -- [etki: kWh/yil, EUR/yil]
  3. [Bulgu] -- [etki: kWh/yil, EUR/yil]

TOPLAM TASARRUF POTANSIYELI:
  Enerji tasarrufu:  _____ kWh/yil (%_____)
  Maliyet tasarrufu: _____ EUR/yil
  CO2 azaltma:       _____ ton CO2/yil
  Toplam yatirim:    _____ EUR
  Kombine geri odeme: _____ yil

ONCELIKLI ONERILER:
  Faz 1 (0-3 ay):   [Hizli kazanimlar -- maliyet, tasarruf]
  Faz 2 (3-12 ay):  [Orta vadeli -- maliyet, tasarruf]
  Faz 3 (1-3 yil):  [Uzun vadeli -- maliyet, tasarruf]
```

### 7.2 Oneri Oncelik Matrisi (Recommendation Priority Matrix)

Oneriler asagidaki kriterlere gore onceliklendirilir:

| Kriter | Agirlik | Puanlama (1-5) |
|--------|---------|----------------|
| Yillik tasarruf (EUR/yil) | %30 | 1: < 5,000 ... 5: > 50,000 |
| Geri odeme suresi | %25 | 1: > 5 yil ... 5: < 1 yil |
| Uygulama kolayligi | %20 | 1: Cok zor ... 5: Cok kolay |
| Risk seviyesi | %15 | 1: Yuksek risk ... 5: Dusuk risk |
| Cevresel etki (CO2) | %10 | 1: Dusuk ... 5: Yuksek |

**Oncelik siniflandirmasi:**

| Toplam Puan | Oncelik | Uygulama Zamani |
|-------------|---------|-----------------|
| 4.0-5.0 | YUKSEK | 0-6 ay |
| 3.0-3.9 | ORTA | 6-18 ay |
| 2.0-2.9 | DUSUK | 18-36 ay |
| < 2.0 | GELECEK | > 36 ay (izle) |

### 7.3 Bulgu Kayit Sablonu

Her bulgu icin:

```
BULGU #X: [Baslik]
Konum:      [Kurutucu No / Hat]
Durum:      [Mevcut olculen deger ve birim]
Benchmark:  [Olmasi gereken deger (kaynak)]
Sapma:      [Fark, % olarak]
Neden:      [Temel neden analizi]
Etki:       [kWh/yil] | [EUR/yil] | [ton CO2/yil]
Oneri:      [Kisa teknik aciklama]
Yatirim:    [EUR tahmini]
Geri odeme: [Yil]
Oncelik:    [YUKSEK / ORTA / DUSUK]
Referans:   [Ilgili cozum dosyasi]
```

### 7.4 Rapor Ekleri

- Ek A: Ham olcum verileri (sicaklik, nem profilleri, enerji loglari)
- Ek B: Ekipman nameplate fotograflari
- Ek C: IR termal goruntu kayitlari
- Ek D: Hesaplama detaylari ve varsayimlar
- Ek E: Psikrometrik diyagramlar
- Ek F: Enerji ve exergy Sankey diyagramlari
- Ek G: Ekipman teknik sartnameleri (onerilenler icin)

### 7.5 Dogrulama ve Takip (Verification and Follow-up)

| Dogrulama Adimi | Zamanlama | Yontem |
|----------------|-----------|--------|
| Kisa donem izleme | Uygulama sonrasi 1-4 hafta | Ayni olcum noktalari, ayni cihazlarla |
| Normallestirilmis karsilastirma | 1-3 ay sonra | Uretim ve ortam kosullarina normallestirilmis |
| Yillik dogrulama | 12 ay sonra | Tam yil verisi ile referans yil karsilastirmasi |

```
Normallestirilmis tasarruf hesabi (IPMVP uyumlu):
SEC_before = kWh / kg_su_before  [kWh/kg_su]
SEC_after  = kWh / kg_su_after   [kWh/kg_su]
Tasarruf%  = (SEC_before - SEC_after) / SEC_before x 100
```

### 7.6 Ornek Tasarruf Hesabi

```
Ornek: Konvektif bant kurutucu, gida sektoru
  Urun debisi:       2,000 kg/saat
  Giris nemi:        60% (wb)
  Cikis nemi:        10% (wb)
  Kurutma sicakligi: 120 C
  Egzoz sicakligi:   110 C
  Egzoz nemi:        45% RH
  Yakit:             Dogalgaz, 0.05 EUR/kWh
  Calisma:           6,000 saat/yil

Buharlasmis su:  2,000 x (0.60 - 0.10) / (1 - 0.10) = 1,111 kg_su/saat
Toplam enerji:   ~1,600 kW (olculen)
SMER:            1,111 / 1,600 = 0.69 kg/kWh (ortalama sinifi)
Yillik enerji:   1,600 x 6,000 = 9,600,000 kWh/yil
Yillik maliyet:  9,600,000 x 0.05 = 480,000 EUR/yil

Oneri 1: Egzoz isi geri kazanimi (%15 tasarruf)
  Tasarruf: 72,000 EUR/yil | Yatirim: ~80,000 EUR | Geri odeme: 1.1 yil

Oneri 2: Hava geri deviri (%10 tasarruf)
  Tasarruf: 48,000 EUR/yil | Yatirim: ~25,000 EUR | Geri odeme: 0.5 yil

Oneri 3: Sicaklik optimizasyonu (120 -> 105 C, %8 tasarruf)
  Tasarruf: 38,400 EUR/yil | Yatirim: ~2,000 EUR  | Geri odeme: 0.05 yil

Toplam kombine tasarruf (kumulatif etki ~%85):
  ~%28-30 | ~135,000 EUR/yil | Toplam yatirim: ~107,000 EUR | Geri odeme: 0.8 yil
```

---

## İlgili Dosyalar (Cross-References)

### Kurutucu Knowledge Base
- Hesaplama formulleri: `dryer/formulas.md`
- Benchmark degerleri: `dryer/benchmarks.md`
- Psikrometri: `dryer/psychrometrics.md`
- Vaka calismalari: `dryer/case_studies.md`

### Ekipman Dosyalari
- `dryer/equipment/tunnel_dryer.md` -- Tunel kurutucu
- `dryer/equipment/belt_dryer.md` -- Bant kurutucu
- `dryer/equipment/rotary_dryer.md` -- Doner kurutucu
- `dryer/equipment/fluidized_bed.md` -- Akiskan yatakli
- `dryer/equipment/spray_dryer.md` -- Sprey kurutucu
- `dryer/equipment/drum_dryer.md` -- Silindir kurutucu
- `dryer/equipment/heat_pump_dryer.md` -- Isi pompali kurutucu
- `dryer/equipment/infrared_dryer.md` -- Infrared kurutucu

### Cozum Dosyalari
- `dryer/solutions/exhaust_heat_recovery.md` -- Egzoz isi geri kazanimi
- `dryer/solutions/air_recirculation.md` -- Hava geri deviri
- `dryer/solutions/heat_pump_retrofit.md` -- Isi pompasi retrofit
- `dryer/solutions/mechanical_dewatering.md` -- Mekanik on su alma
- `dryer/solutions/insulation.md` -- Izolasyon iyilestirme
- `dryer/solutions/temperature_optimization.md` -- Sicaklik optimizasyonu
- `dryer/solutions/solar_preheating.md` -- Solar on isitma

### Diger Ekipman Denetimleri
- Kompresor denetimi: `compressor/audit.md`
- Kazan denetimi: `boiler/audit.md`
- Chiller denetimi: `chiller/audit.md`
- Pompa denetimi: `pump/audit.md`

### Fabrika Seviyesi
- `factory/cross_equipment.md` -- Ekipmanlar arasi entegrasyon firsatlari
- `factory/heat_integration.md` -- Isi entegrasyonu
- `factory/pinch_analysis.md` -- Pinch analizi

---

## Referanslar (References)

1. **ISO 13579:2002** -- Industrial furnaces and associated processing equipment -- Method of measuring energy balance and calculating efficiency
2. **ISO 50002:2014** -- Energy Audits -- Requirements with guidance for use
3. **ISO 50001:2018** -- Energy Management Systems -- Requirements with guidance for use
4. **EU BREF** -- Reference documents on Best Available Techniques: Food, Drink and Milk Industries; Textiles Industry; Pulp and Paper Industry; Ceramic Manufacturing Industry
5. **US DOE** -- "Improving Process Heating System Performance: A Sourcebook for Industry," Advanced Manufacturing Office, 2nd Edition
6. **Carbon Trust** -- "Industrial Energy Efficiency Accelerator: Guide to the Dryer Sector" (CTG062)
7. **ASME PTC 33** -- Spray Dryer Performance Test Code
8. **ATEX Directive 2014/34/EU** -- Equipment and protective systems intended for use in potentially explosive atmospheres
9. **Mujumdar, A.S.** -- "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014
10. **Kemp, I.C.** -- "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4, Wiley, 2012
11. **Dincer, I. & Rosen, M.A.** -- "Exergy Analysis of Drying Processes and Systems," Drying Technology, 2013
12. **Aghbashlo, M. et al.** -- "A review on exergy analysis of drying processes and systems," Renewable and Sustainable Energy Reviews, 22, 1-22, 2013
13. **IPMVP** -- "International Performance Measurement and Verification Protocol," Efficiency Valuation Organization
