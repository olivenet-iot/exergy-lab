---
title: "Sicaklik Optimizasyonu (Drying Temperature Optimization)"
category: dryer
equipment_type: dryer
keywords: [sicaklik optimizasyonu, temperature optimization, kurutma profili, cok bolgeli kurutma]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/psychrometrics.md, dryer/equipment/belt_dryer.md, dryer/equipment/tunnel_dryer.md, dryer/solutions/exhaust_heat_recovery.md]
use_when: ["Kurutma sicakligi optimizasyonu degerlendirilirken", "Asiri kurutma veya dusuk verim tespit edildiginde"]
priority: medium
last_updated: 2026-02-01
---
# Sicaklik Optimizasyonu (Drying Temperature Optimization)

> Son guncelleme: 2026-02-01

## Genel Bakis

Endustriyel kurutucularda besleme havasi sicakligi, kurutma hizi, urun kalitesi ve enerji tuketimi arasindaki dengeyi belirleyen en kritik parametredir. Bircogu tesiste kurutucular, guvenlik marji veya eski aliskanliklar nedeniyle gereginden yuksek sicaklikta calistirilir. Bu durum asiri exergy yikimina (exergy destruction) yol acar: yuksek sicaklikli enerji kaynagi, termodinamik kalitesinin buyuk kismini dusuk sicaklikli buharlasmaya aktarirken kaybeder.

**Temel Prensip:** Kurutma sicakligindaki her gereksiz 10 degreeC artis, egzoz kayiplarini yaklasik %3-5 arttirir ve exergy verimini dusurur. Ancak sicaklik dususu, kurutma hizini da azaltacagindan *optimum nokta* her urun ve proses icin ayri ayri belirlenmelidir.

**Tipik Tasarruf:** %5-20 enerji tasarrufu (tek bolge optimizasyonunda %5-10, cok bolgeli retrofit ile %10-20)
**Tipik Yatirim:** Kontrol sistemi iyilestirmeleri icin EUR 10,000-30,000
**Geri Odeme Suresi (SPP):** 0.5-2.0 yil

---

## Optimum Sicaklik (Optimum Drying Temperature)

### Sicaklik-Verim Dengesi

Kurutma sicakligi arttirildiginda iki karsi yonlu etki olusur:

1. **Kurutma hizi artar** -- sicaklik gradyani buyudukce isi ve kutle transferi hizlanir, throughput yukselir.
2. **Exergy yikimi artar** -- yuksek sicaklikli havanin exergy'sinin buyuk kismi dusuk sicaklikli buharlasmada yikilir.

Exergy perspektifinden optimum sicaklik, toplam exergy yikimini minimize eden noktadir:

```
Ex_input = m_air x Cp x [(T_in - T_0) - T_0 x ln(T_in / T_0)]

Exergy verimi:
eta_ex = Ex_evaporation / Ex_input

Burada:
- T_in  = besleme havasi sicakligi [K]
- T_0   = referans (ortam) sicakligi [K] (tipik 298.15 K)
- Ex_evaporation = buharlasmma icin kullanilan faydali exergy [kW]
```

Besleme sicakligi dusuruldugunde Ex_input azalir, ancak ayni nem yukunde kurutma suresi uzar ve toplam hava debisi artabilir. Optimum nokta, urun kalitesi, kapasite gereksinimi ve enerji maliyetini birlikte degerlendiren bir muhendislik kararidir.

### Urune Gore Optimum Sicaklik Araliklari

| Urun | Maks. T [degreeC] | Optimum T [degreeC] | Kritik Parametre |
|------|-------------------|---------------------|-----------------|
| Tahil (Grain) | 60-100 | 50-70 | Cimlenme yetenegi, protein |
| Meyve/sebze | 50-70 | 40-60 | Vitamin kaybi, renk (browning) |
| Kereste (Timber) | 60-80 | 50-65 | Catlama, deformasyon |
| Bitkisel urunler (Herbs) | 40-60 | 35-45 | Ucucu yag kaybi |
| Seramik (Ceramics) | 200-400 | Asamaya gore | Catlama, duzgun kuruma |
| Kagit (Paper) | 100-150 | 80-120 | Sarilma, boyutsal kararlilik |
| Tekstil (Textile) | 80-130 | 70-110 | Elyaf hasari, renk |
| Sut tozu (Milk powder) | 150-200 (giris) | 170-190 (giris) | Protein denaturasyonu |
| Camur/atik (Sludge) | 100-250 | 80-150 | Koku, emisyon |

---

## Cok Bolgeli Kurutma (Multi-Zone Drying)

### Prensip

Tek sicaklik setpoint'i ile calisan kurutucularda havanin exergy'si ozellikle azalan hizli donemde (falling rate period) buyuk olcude israf edilir. Cok bolgeli kurutma, kurutma kinetigine uyumlu sicaklik profili olusturarak bu israfi azaltir:

- **Bolge 1 (Giris):** Yuksek sicaklik -- sabit hizli donem (constant rate period) boyunca hizli nem uzaklastirma. Urun yuzeyinde serbest su mevcut oldugundan yuksek sicaklik etkilidir.
- **Bolge 2 (Orta):** Orta sicaklik -- gecis donemi. Yuzey kurumaya baslar, ic difuzyon sinirlamasi devreye girer.
- **Bolge 3 (Cikis):** Dusuk sicaklik -- azalan hizli donem. Nem difuzyonla icten gelir; yuksek sicaklik kurutma hizini orantili artirmaz, yalnizca urunu asiri isitir.

### Enerji ve Kalite Kazanimi

| Parametre | Tek Bolge | Cok Bolge (3 Zone) | Kazanim |
|-----------|-----------|---------------------|---------|
| Enerji tuketimi | Referans | %10-20 daha dusuk | Onemli |
| Urun kalitesi | Standart | Daha iyi (renk, besin, yapisal butunluk) | Katma deger |
| Kurutma homojenliği | Degisken | Daha homojen | Az fire |
| Egzoz sicakligi | Yuksek | Daha dusuk | Azalan kayip |

Cok bolgeli kurutmanin sagladigi %10-20 enerji tasarrufu, su mekanizmalardan kaynaklanir:

1. Her bolgede hava debisi ve sicakligi gereksinimine gore ayarlanir -- gereksiz hava isitmasi azalir.
2. Cikis bolgesindeki dusuk sicaklik, egzoz kaybini dogrudan dusurir.
3. Urunun asiri isitilmamasi, yuzey kabuk baglamasini (case hardening) onler ve kurutma verimini arttirir.

---

## Asiri Kurutma Problemi (Over-Drying)

### Tanimlama

Asiri kurutma, urunun hedef nem icerigi altina kurutulmasidir. Endustriyel tesislerde en yaygin enerji israfi kaynaklarindan biridir, ancak cogu zaman fark edilmez.

**Temel Kural:** Hedef nemin her %1 altina inilmesi, kurutma enerjisini %3-10 arttirir. Bu oran azalan hizli donemde ussel (exponential) artan enerji gereksiniminden kaynaklanir.

### Nedenleri

- Nem olcum sisteminin olmamasi veya kalibrasyonsuz olmasi
- Operatorlerin guvenlik marji birakma aliskanligi
- Kurutma suresi veya sicaklik sabit tutulurken besleme nemi degisken olmasi
- Parti bazli (batch) kurutmada hedef neme ulasma aninin bilinememesi

### Etki Analizi

```
Ornek: Tahil kurutucu
Hedef nem: %14 (yasbaz)
Gerceklesen nem: %11 (yasbaz)
Asiri kurutma: 3 puan

Fazladan uzaklastirilan su (1000 kg/h yasbaz besleme):
m_dry = 1000 x (1 - 0.14) = 860 kg/h kuru kati
m_hedef = 860 / (1 - 0.14) = 1000 kg/h (hedefte)
m_gercek = 860 / (1 - 0.11) = 966.3 kg/h (asiri kurutulmus)
m_ekstra_su = 1000 - 966.3 = 33.7 kg/h fazla uzaklastirilan su

Ek enerji: 33.7 x 2,334 / 3600 = 21.8 kW (%5-8 ek enerji)
Yillik ek maliyet (4,000 h, EUR 0.05/kWh, kazan ver. %90):
= 21.8 / 0.90 x 4,000 x 0.05 = EUR 4,844/yil
```

Ayrica asiri kurutma urun agirligini azaltir -- kilogram bazinda satilan urunlerde dogrudan gelir kaybi olusturur.

### Cozum: Nem Kontrol Sistemi

- **NIR (Near-Infrared) sensorler:** Urun nemini anlik olcer, non-contact, hassasiyet +/- 0.1-0.3%.
- **Mikrodalga (Microwave) sensorler:** Bulk nem olcumu, kalinlik etkisine daha dayanikli, hassasiyet +/- 0.2-0.5%.
- **PID veya model tabanli kontrol:** Olculen neme gore sicakligi, hava debisini veya kurutma suresini otomatik ayarlar.

---

## Kurutma Egrisi Analizi (Drying Curve Analysis)

### Sabit Hizli Donem (Constant Rate Period)

Bu donemde urun yuzeyinde serbest su vardir. Kurutma hizi, hava kosullarina (sicaklik, nem, hiz) baglidir ve urun ozelliklerinden bagimsizdir.

```
Kurutma hizi (sabit donem):
dM/dt = h_c x A x (T_air - T_wb) / h_fg  [kg/s]

Burada:
- h_c   = konvektif isi transfer katsayisi [W/(m2.K)]
- A     = kurutma yuzey alani [m2]
- T_air = hava sicakligi [degreeC]
- T_wb  = yas termometre sicakligi [degreeC]
- h_fg  = buharlasmma gizli isisi [kJ/kg]
```

Bu donemde yuksek sicaklik, kurutma hizini dogrudan arttirir. Urun sicakligi yaklasik T_wb'de kalir ve asiri isinamaz.

### Kritik Nem Icerigi (Critical Moisture Content)

Sabit hizli donemden azalan hizli doneme gecis noktasidir. Urune gore degisir:

| Urun | Kritik Nem [kg su/kg kuru] | Kritik Nem [% yasbaz] |
|------|----------------------------|-----------------------|
| Tahil | 0.25-0.35 | 20-26% |
| Meyve/sebze | 2.0-4.0 | 67-80% |
| Kagit hamuru | 1.5-2.5 | 60-71% |
| Seramik | 0.10-0.20 | 9-17% |
| Kereste | 0.30-0.60 | 23-38% |

### Azalan Hizli Donem (Falling Rate Period)

Yuzey kuruyunca nem difuzyonla icten tasina ve kurutma hizi duser. Bu donemde:

- Kurutma hizi artik urun ic yapisina (goz enekliligi, difuzyon katsayisi) baglidir
- Sicaklik artirmak sinirli fayda saglar -- difuzyon darbogazdir
- Yuksek sicaklik urunu asiri isitir, kalite bozulmasi (renk, yapisal catlak, besin kaybi) riski artar
- **Sonuc:** Bu donemde sicakligi dusurmek enerji tasarrufu saglarken urun kalitesini de korur

---

## Sicaklik-Nem Profili Optimizasyonu (Temperature-Humidity Profile Optimization)

### Optimum Giris Sicakliginin Belirlenmesi

Verilen throughput ve hedef nem icin optimum giris sicakligi, asagidaki adimlarla belirlenir:

1. **Kurutma kinetigi testi:** Laboratuvarda veya pilot olcekte farkli sicakliklarda (5 degreeC adimlarla) kurutma egrisi cikarilir.
2. **Minimum kurutma suresi:** Hedef neme ulasmak icin gereken minimum sure her sicaklik icin belirlenir.
3. **Enerji tuketimi hesabi:** Her sicaklik-sure kombinasyonu icin toplam enerji tuketimi (isitma + fan) hesaplanir.
4. **Kalite degerlendirmesi:** Urunun gorsel, yapisal ve kimyasal kalite parametreleri her sicaklikta kontrol edilir.
5. **Optimum secim:** Enerji tuketimi, kapasite ve kalite kriterlerini birlikte karsilayan sicaklik secilir.

### Egzoz Kosullarinin Optimizasyonu

Egzoz havasinin bagi nem orani (relative humidity) kurutma veriminin anahtar gostergesidir:

| Egzoz Bagil Nem | Durum | Aksiyon |
|-----------------|-------|---------|
| < %30 | Cok dusuk verim | Hava debisini azalt veya sicakligi dusur |
| %30-50 | Ortalama | Iyilestirme potansiyeli var |
| %50-70 | Iyi | Standart optimize operasyon |
| %70-90 | Cok iyi | Hava kapasitesi etkin kullaniliyor |
| > %90 | Yogusma riski | Cig noktasi kontrolu gerekli |

---

## Hesaplama Ornegi (3 Bolgeli vs Tek Bolgeli Bant Kurutucu)

### Senaryo

Tahil kurutma tesisi, konveyor bant kurutucu. Giris nemi %25 yasbaz, hedef nem %14 yasbaz. Uretim kapasitesi 2,000 kg/h yasbaz besleme. Yillik calisma: 4,000 saat. Dogalgaz fiyati: EUR 0.05/kWh, kazan verimi %90.

### Tek Bolgeli Kurutucu (Mevcut Durum)

```
Besleme sicakligi: T_in = 100 degreeC (tum bolge)
Hava debisi: m_air = 8,000 kg/h = 2.222 kg/s
Egzoz sicakligi: T_ex = 60 degreeC
Ortam sicakligi: T_0 = 20 degreeC

Isitici gucu:
Q_tek = m_air x Cp x (T_in - T_0) = 2.222 x 1.005 x (100 - 20) = 178.7 kW

Buharlasmma:
m_dry = 2000 x (1-0.25) = 1500 kg/h kuru kati
m_out = 1500 / (1-0.14) = 1744.2 kg/h
m_w = 2000 - 1744.2 = 255.8 kg/h = 0.071 kg/s

SMER = 255.8 / 178.7 = 1.43 kg/kWh

Yillik enerji tuketimi:
E_tek = 178.7 / 0.90 x 4,000 = 794,222 kWh/yil
Yillik maliyet = 794,222 x 0.05 = EUR 39,711/yil
```

### Uc Bolgeli Kurutucu (Optimize Durum)

```
Bolge 1 (giris -- sabit hizli donem):
  T_1 = 100 degreeC, m_air_1 = 3,500 kg/h = 0.972 kg/s
  Q_1 = 0.972 x 1.005 x (100 - 20) = 78.1 kW

Bolge 2 (orta -- gecis):
  T_2 = 75 degreeC, m_air_2 = 2,500 kg/h = 0.694 kg/s
  Q_2 = 0.694 x 1.005 x (75 - 20) = 38.4 kW

Bolge 3 (cikis -- azalan hizli donem):
  T_3 = 55 degreeC, m_air_3 = 2,000 kg/h = 0.556 kg/s
  Q_3 = 0.556 x 1.005 x (55 - 20) = 19.5 kW

Toplam:
Q_cok = 78.1 + 38.4 + 19.5 = 136.0 kW
m_air_toplam = 8,000 kg/h (ayni toplam hava, dagitim farkli)

SMER = 255.8 / 136.0 = 1.88 kg/kWh

Yillik enerji tuketimi:
E_cok = 136.0 / 0.90 x 4,000 = 604,444 kWh/yil
Yillik maliyet = 604,444 x 0.05 = EUR 30,222/yil
```

### Karsilastirma

| Parametre | Tek Bolge | 3 Bolge | Fark |
|-----------|-----------|---------|------|
| Isitici gucu [kW] | 178.7 | 136.0 | -%23.9 |
| SMER [kg/kWh] | 1.43 | 1.88 | +%31.5 |
| Yillik enerji [kWh/yil] | 794,222 | 604,444 | -189,778 |
| Yillik maliyet [EUR/yil] | 39,711 | 30,222 | -9,489 |
| Egzoz sicakligi (cikis) [degreeC] | 60 | ~40 | -20 |
| Urun kalitesi | Standart | Iyilestirilmis | + |

**Yillik tasarruf: EUR 9,489/yil (%23.9 enerji tasarrufu)**

### Exergy Karsilastirmasi

```
Tek bolge exergy girdisi:
Ex_tek = Q_tek x (1 - T_0/T_in) = 178.7 x (1 - 293.15/373.15) = 178.7 x 0.214 = 38.2 kW

3 bolge toplam exergy girdisi:
Ex_1 = 78.1 x (1 - 293.15/373.15) = 78.1 x 0.214 = 16.7 kW
Ex_2 = 38.4 x (1 - 293.15/348.15) = 38.4 x 0.158 = 6.1 kW
Ex_3 = 19.5 x (1 - 293.15/328.15) = 19.5 x 0.107 = 2.1 kW
Ex_cok = 16.7 + 6.1 + 2.1 = 24.9 kW

Exergy tasarrufu: 38.2 - 24.9 = 13.3 kW (%34.8 exergy tasarrufu)
```

Cok bolgeli kurutmada exergy tasarrufu (%34.8), enerji tasarrufundan (%23.9) daha buyuktur. Bunun nedeni, cikis bolgesinde dusuk sicaklikli (dusuk exergy kalitesinde) enerji kullanilmasidir.

---

## Kontrol Stratejisi (Control Strategy)

### Cikis Nem Olcumu

Asiri kurutmayi onlemenin ve optimum sicakligi korumanin temel araci, urun cikis neminin gercek zamanli olcumudur.

| Sensor Teknolojisi | Calisma Prensibi | Hassasiyet | Maliyet [EUR] | Avantaj | Dezavantaj |
|-------------------|-----------------|------------|---------------|---------|------------|
| NIR (Near-Infrared) | Yakin kizilotesi absorpsiyon | +/- 0.1-0.3% | 8,000-20,000 | Hizli, non-contact, yuzey nemi | Yuzey odakli, kalibrasyon gerekli |
| Mikrodalga (Microwave) | Dielektrik olcum | +/- 0.2-0.5% | 5,000-15,000 | Bulk nem, kalinlik etkisi az | Sicaklik kompanzasyonu gerekli |
| Kapasitif | Dielektrik sabiti | +/- 0.5-1.0% | 2,000-6,000 | Ucuz, dayanikli | Dusuk hassasiyet |
| Tartim bazli | Kutle farki | +/- 0.2% | 3,000-10,000 | Dogrudan olcum | Yavas tepki, batch icin uygun |

### Kontrol Yaklasimi

**PID Kontrol (Basit):**
- Olculen cikis nemi ile hedef nem arasindaki sapma (error) ile sicakligi veya hava debisini ayarlar.
- Ucuz ve uygulamasi kolay.
- Sinirlilik: kurutma prosesinin uzun gecikme suresi (dead time) PID performansini dusurur.

**Model Bazli Kontrol (Model Predictive Control -- MPC):**
- Kurutma kinetik modeli kullanarak gelecek cikis nemini tahmin eder.
- Besleme nemi, ortam kosullari ve uretim hizi degisikliklerine proaktif tepki verir.
- Daha yuksek performans ancak daha karmasik kurulum.
- Tipik ek tasarruf: PID'ye gore %3-8 daha az enerji.

**Cascade Kontrol:**
- Dis dongu: urun cikis nemi -- ic dongu: hava sicakligi veya debi.
- Sicaklik bozulmalarini hizla duzelterek nem kontrolunu iyilestirir.

---

## Ekonomik Analiz (Economic Analysis)

### Yatirim Maliyeti

| Uygulama | Aciklama | Maliyet [EUR] | Tasarruf Etkisi |
|----------|----------|---------------|-----------------|
| Setpoint optimizasyonu | PLC/SCADA setpoint degisikligi | 500-2,000 | Aninda, %3-8 |
| Sicaklik sensorleri | Her bolge icin PT100/thermocouple | 1,000-3,000 | Daha iyi izleme |
| NIR/mikrodalga nem sensoru | Urun cikis nem olcumu | 5,000-20,000 | Asiri kurutma onleme |
| VFD (degisken frekansli fan) | Hava debisi modulasyonu | 2,000-8,000 | %5-15 fan tasarrufu |
| Bolgesel damper sistemi | Bolgesel hava akis kontrolu | 3,000-10,000 | Profil optimizasyonu |
| Tam cok bolgeli retrofit | Isitici + fan + kontrol per bolge | 10,000-30,000 | Maksimum tasarruf |

### Geri Odeme Analizi

| Senaryo | Yatirim [EUR] | Yillik Tasarruf [EUR] | SPP [yil] |
|---------|---------------|----------------------|-----------|
| Basit setpoint dusurme | 500-2,000 | 3,000-8,000 | 0.1-0.5 |
| Nem sensoru + kontrol | 8,000-20,000 | 5,000-15,000 | 0.5-2.0 |
| Sensor + VFD ekleme | 8,000-25,000 | 8,000-20,000 | 0.5-1.5 |
| Cok bolgeli retrofit | 15,000-30,000 | 10,000-25,000 | 0.6-2.0 |

**Genel SPP araligi:** 0.5-2.0 yil. Kontrol tabanli iyilestirmeler (sensor + PID/MPC) genellikle en hizli geri odeyen kurutucu yatirimlari arasindadir.

### Ek Ekonomik Faydalar (Dolayli)

- **Asiri kurutma onleme ile urun agirligi artisi:** Kilogram bazinda satilan urunlerde %1-3 gelir artisi.
- **Kalite iyilesmesi:** Daha az fire, daha az iade, marka degeri.
- **Kapasite artisi:** Optimize kurutma ile ayni surette daha fazla uretim.
- **CO2 emisyon azalmasi:** Enerji tasarrufuna paralel emisyon dususu, karbon maliyeti azalmasi.

---

## Uygulama Adimlari (Implementation Steps)

1. **Mevcut durum analizi:** Mevcut besleme ve egzoz sicakliklarini, hava debisini ve urun cikis nemini kaydedin (minimum 1 hafta surekli veri).
2. **Urun gereksinimleri:** Urunun maksimum izin verilen sicakligini, hedef nem icerigini ve kalite kriterlerini belirleyin.
3. **Kurutma kinetigi testi:** Farkli sicakliklarda (5 degreeC adimlarla) kurutma egrisi cikarin; sabit ve azalan hizli donemleri taniyin.
4. **Deneysel optimizasyon:** Uretim sirasinda sicakligi kademeli olarak dusurun; her adimda kurutma suresini, urun kalitesini ve nem icerigini kontrol edin.
5. **Asiri kurutma tespiti:** Cikis nemini istatistiksel olarak analiz edin -- hedef nemin altinda kalma oranini belirleyin.
6. **Nem sensoru kurulumu:** NIR veya mikrodalga sensor ile urun cikis nemini gercek zamanli olcun.
7. **Kontrol sistemi guncelleme:** PID veya model bazli kontrol ile sicakligi/debiyi otomatik ayarlayin.
8. **Cok bolgeli degerlendirme:** Kurutucu tipi uygunsa (tunel, konveyor bant) bolgesel sicaklik kontrolu fizibilitesi yapin.
9. **Performans dogrulama:** Optimizasyon sonrasi 2-4 hafta boyunca enerji tuketimi, SMER ve urun kalitesini izleyin.
10. **Operator egitimi:** Operatorlere yeni parametrelerin mantigini ve urun kalite kontrol prosedurunu anlatin.
11. **Periyodik gozden gecirme:** Mevsimsel ve urun degisikliklerine gore parametreleri yilda 2-4 kez gozden gecirin.

---

## İlgili Dosyalar

- Kurutucu exergy formulleri: `dryer/formulas.md`
- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Psikrometrik hesaplamalar: `dryer/psychrometrics.md`
- Bant kurutucu detaylari: `dryer/equipment/belt_dryer.md`
- Tunel kurutucu detaylari: `dryer/equipment/tunnel_dryer.md`
- Egzoz isi geri kazanimi: `dryer/solutions/exhaust_heat_recovery.md`
- Fabrika capraz ekipman optimizasyonu: `factory/cross_equipment.md`

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014
- Kemp, I.C., "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4, Wiley-VCH, 2012
- EU BREF, "Reference Document on Best Available Techniques for Energy Efficiency," European Commission, 2009
- EU BREF, "Reference Document on BAT in the Food, Drink and Milk Industries," European Commission
- Strumillo, C., Jones, P.L. & Zylla, R., "Energy Aspects in Drying," in Handbook of Industrial Drying
- DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry," 3rd Edition
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," 3rd Edition, Elsevier
- ASHRAE Handbook -- HVAC Applications, Chapter on Drying and Dehumidification
- Keey, R.B., "Drying of Loose and Particulate Materials," Hemisphere Publishing
- Borde, I. & Levy, A., "New Approaches in Drying Technology for Heat-Sensitive Products"
- Perry, R.H. & Green, D.W., "Perry's Chemical Engineers' Handbook," 9th Edition -- Drying Section
