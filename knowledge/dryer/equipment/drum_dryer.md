---
title: "Silindir Kurutucu (Drum/Cylinder Dryer)"
category: dryer
equipment_type: dryer
keywords: [silindir kurutucu, drum dryer, tambur kurutucu, iletimli kurutma, kağıt kurutma]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/solutions/insulation.md, dryer/sectors/paper_drying.md]
use_when: ["Silindir kurutucu analiz edilirken", "Kağıt/film kurutma değerlendirilirken"]
priority: medium
last_updated: 2026-02-01
---
# Silindir Kurutucu (Drum/Cylinder Dryer)

> Son guncelleme: 2026-02-01

## Genel Bakis

Silindir kurutucu (drum dryer / cylinder dryer), urunun buharla isitilmis doner bir silindir
yuzeyine temas ettirilerek kurutuldugu iletimli (conductive) kurutma sistemidir. Isitma
buhari silindirin ic boslugunda yogusarak latent isisini silindir cidarina aktarir; cidar
dis yuzeyinde temas halindeki urun filminden nem buharlasirilir. Konvektif kurutuculara
kiyasla daha yuksek exergy verimi sunar, cunku isi transferi sicak hava yerine dogrudan
metal yuzey uzerinden gerceklesir ve egzoz havasi kayiplari minimumda kalir.

En buyuk endustriyel uygulama **kagit endustrisi**dir: modern bir kagit makinesinin
kurutma bolumunde 40-60 adet buharla isitilmis silindir art arda dizilir. Bunun disinda
gida pastalari (bebek mamasi, patates pul), kimyasal pullar, maya ve nisasta gibi urunlerde
tek veya cift silindirli uniteler kullanilir.

- **Tip:** Iletimli/konduktif (conductive) -- buharla isitilmis silindir yuzeyinden dogrudan isi transferi
- **Kapasite araligi:** 100-5,000 kg/h (tek unite), kagit makinelerinde 20,000+ kg su buharlastirma/h
- **Isitma buhari basinci:** 2-10 bar (uygulama ve silindire bagli)
- **Silindir yuzey sicakligi:** 100-180 C
- **Exergy verimi:** %10-25 (tipik endustriyel aralik, kagit kurutma bolumu dahil)
- **SMER:** 1.0-2.0 kg/kWh (tipik), 2.5 kg/kWh (en iyi uygulama -- optimize edilmis kagit kurutma)
- **Yaygin markalar:** Andritz, Valmet, Voith, Kadant, Mitchell Dryers, GMF Gouda, Buflovak
- **Tipik uygulamalar:** Kagit kurutma (multi-cylinder), gida pastalari, kimyasal pullar, maya

## Calisma Prensibi

Silindir kurutucuda isi transfer mekanizmasi soyledir:

1. **Buhar yogusmasi (condensation):** Doymus buhar silindir ic yuzeyinde yogusarak latent isisini birakir
2. **Cidar iletiimi (wall conduction):** Isi, silindir metal cidari boyunca dis yuzeyine iletilir
3. **Temas isi transferi (contact heat transfer):** Silindir dis yuzeyindeki urun filmine konduksiyon yoluyla isi aktarilir
4. **Buharlasma (evaporation):** Urun filmindeki nem buharlasirilarak ortama veya hood sistemine atilir

Toplam isi transfer direnci, seri bagli dort direncten olusur:

```
R_toplam = R_kondensat + R_cidar + R_temas + R_film

Burada:
  R_kondensat = Silindir icindeki kondensat film direnci (en buyuk degisken)
  R_cidar     = Silindir metal cidari direnci (tipik 20-40 mm celik veya dokme demir)
  R_temas     = Urun-silindir temas direnci (urun cinsine ve basinca bagli)
  R_film      = Urun film kalinligi direnci

Toplam isi transfer katsayisi:
  U = 1 / R_toplam   (tipik 0.5-2.0 kW/m2.C)
  Q = U x A x LMTD   (kW)
```

**Kondensat film etkisi kritiktir:** Silindir icinde biriken kondensat tabakasi isi transfer
direncinin %30-50'sini olusturabilir. 1 mm kondensat birikimi yaklasik %5 performans kaybi
demektir. Etkin kondensat tahliyesi (sifon sistemi) en onemli isletme parametresidir.

### Ic ve Dis Isitma Karsilastirmasi

| Ozellik | Ic Isitma (Internal Heating) | Dis Isitma (External Heating) |
|---------|------------------------------|-------------------------------|
| Isitma yontemi | Buhar silindirin ic boslugunda yogusur | Silindir dis yuzeyine sicak hava veya kizilotesi |
| Yayginlik | %95+ endustriyel uygulama | Nadir, ozel uygulamalar |
| Isi transfer verimi | Yuksek (dogrudan yogusma) | Orta (konvektif veya radyatif) |
| Basinc sinifi | Silindir basincli kap (2-10 bar) | Atmosferik |
| Uygulama | Kagit, gida, kimya | Hassas film kaplama, laboratuvar |

## Tipler

### Tek Silindir (Single Drum)

Tek buyuk cap silindir (tipik 1.0-2.0 m cap), alt havuzdan daldirma (dip feeding) veya
puskurtme ile besleme. Urun silindir yuzeyinde ince film olusturur, yaklasik 270 derece
dondukten sonra kaziyici (doctor blade) ile siyrilir.

- Kapasite: 100-2,000 kg/h
- Uygulama: Bebek mamasi, patates pul, nisasta, maya

### Cift Silindir (Double Drum)

Iki paralel silindir, arada dar araliktan (nip) besleme yapilir. Her iki silindir de
buharla isitilir; urun her iki yuzeyden ayri ayri kurutularak siyrilir.

- Kapasite: 200-5,000 kg/h (tek silindire gore ~1.5-2x)
- Yatirim: Tek silindire gore yaklasik 1.5x maliyet
- Uygulama: Yuksek kapasiteli gida ve kimya

### Kagit Makinesi Multi-Cylinder Bolumu

Kagit makinesinin kurutma bolumunde 40-60 adet kucuk capli silindir (tipik 1.5 m cap)
ust-alt gruplar halinde dizilir. Kagit bandi sirayla her silindire sarilarak kademeli
olarak kurutulur. Bu, endustriyel olcekte en buyuk silindir kurutma uygulamasidir.

- Silindir sayisi: 40-60 adet (3-6 grup halinde)
- Buhar basinci: Kademeli -- ilk gruplar 2-4 bar, son gruplar 6-10 bar
- Kapasite: 10,000-25,000 kg su buharlastirma/h (buyuk kagit makinesi)
- Uygulama: Gazete kagidi, ambalaj kagidi, karton

### Vakumlu Silindir (Vacuum Drum)

Isiya duyarli urunlerde silindir vakum ortaminda calistirilir. Dusuk basinc nedeniyle
buharlasma sicakligi duser (ornegin 50-70 C), urun kalitesi korunur.

- Yatirim: Atmosferik silindire gore %50-100 fazla
- Uygulama: Enzimler, vitaminli gida konsantreleri

## Parametreler

### Zorunlu Olcum Parametreleri

| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|-------------|---------------|
| Isitma buhari debisi (steam flow rate) | kg/h | 200-3,000 | Vortex veya orifis debi olcer |
| Buhar basinci (steam pressure) | bar | 2-10 | Basinc transmiteri |
| Kondensat sicakligi (condensate temperature) | C | 100-180 | Pt100 sicaklik sensoru |
| Urun besleme debisi (product feed rate) | kg/h | 100-5,000 | Kutle debi olcer |
| Urun giris nem icerigi (inlet moisture) | % | 40-85 | Nem tayin cihazi |
| Urun cikis nem icerigi (outlet moisture) | % | 2-8 | Infrared nem olcer |
| Silindir yuzey sicakligi (drum surface temperature) | C | 100-180 | Kizilotesi termometre (IR gun) |
| Silindir donme hizi (drum speed) | rpm | 2-15 | Takometre |

### Opsiyonel Parametreler

| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|-------------|---------------|
| Kondensat debisi (condensate flow) | kg/h | 200-3,000 | Kondensat olcum tanki |
| Flash buhar miktari | kg/h | 10-150 | Hesaplama (basinc farkina bagli) |
| Hood egzoz sicakligi | C | 50-90 | Termokupl |
| Hood egzoz nemi | g/kg | 100-400 | Nem sensoru |
| Film kalinligi (product film) | mm | 0.1-1.5 | Gap gauge |
| Motor gucu | kW | 5-50 | Guc analizoru |
| Ortam sicakligi ve nemi | C, %RH | 15-40 C | Hava istasyonu |

### Varsayilan Degerler

| Parametre | Varsayilan | Not |
|-----------|-----------|-----|
| Buhar basinci | 6 bar | Orta basinc endustriyel buhar |
| Buhar sicakligi | 159 C | 6 bar doymus buhar |
| Silindir yuzey sicakligi | 150 C | Buhar basincina bagli |
| Kondensat sicakligi | 155 C | Basinc altinda cikis |
| Urun giris nemi | %60 | Tipik bulamac besleme |
| Urun cikis nemi | %5 | Standart kurutulmus urun |
| Radyasyon kaybi | %10 | Standart yalitimli sistem |
| Kondensat geri donus orani | %85 | Acik kondensat sistemi |
| SMER | 1.5 kg/kWh | Olcum yoksa ilk tahmin |
| Exergy verimi | %18 | 6 bar buhar, tipik isletme |
| Yillik calisma saati | 6,000 saat/yil | Surekli uretim |
| Yuk orani (load factor) | %80 | Kagit ve gida sektorleri |
| Toplam isi transfer katsayisi (U) | 1.0 kW/m2.C | Ortalama temiz yuzey |

## Kagit Kurutma Bolumu (Paper Machine Dryer Section)

Kagit endustrisi, silindir kurutucunun en buyuk ve en gelismis uygulama alanidir. Modern
bir kagit makinesinde kurutma bolumu toplam enerji tuketiminin %60-70'ini olusturur.

### Genel Yapi

Kagit makinesi kurutma bolumu tipik olarak sunlardan olusur:

- **Kurutma silindirleri (drying cylinders):** 40-60 adet, tipik 1.5 m cap x 3-10 m uzunluk
- **Kece (felt/fabric):** Kagidi silindirlere bastiran sentetik bant
- **Cep havalari (pocket ventilation):** Silindirler arasi ceplerdeki nemli havanin uzaklastirilmasi
- **Hood (kaput) sistemi:** Kurutma bolumunu cevreleyen kapali alan, nemli hava yonetimi
- **Kondensat tahliye sistemi:** Her silindirden kondensat cikarimi (sifon + seperator)

### Kademeli Buhar Sistemi (Cascade Steam System)

Kagit makinelerinde silindirler gruplara ayrilir ve her gruba farkli basincta buhar verilir.
Yuksek basinc grubundan cikan kondensat, dusuk basinc grubuna flash buhar olarak beslenir:

```
Tipik kademeli buhar dagitimi (4 grup):

Grup 1 (on kurutma):     2-3 bar   -->  Kagit nemi: %55 --> %45
Grup 2 (ara kurutma):    4-5 bar   -->  Kagit nemi: %45 --> %30
Grup 3 (ana kurutma):    6-8 bar   -->  Kagit nemi: %30 --> %15
Grup 4 (son kurutma):    8-10 bar  -->  Kagit nemi: %15 --> %5-8

Flash buhar akisi: Grup 4 kondensat --> Grup 3 --> Grup 2 --> Grup 1
Bu kaskad sistem buhar tuketimini %10-15 azaltir.
```

### Cep Havalari ve Hood Sistemi (Pocket Ventilation & Hood)

Silindirler arasindaki ceplerde nemli hava birikir ve kurutma hizini sinirlar. Cep
havalari (pocket ventilation) bu nemli havayi uzaklastirir ve kurutma kapasitesini arttirir.

- **Acik hood:** Eski tesisler, egzoz havasi dogrudan ortama atilir -- yuksek enerji kaybi
- **Kapali hood:** Modern tesisler, hood icindeki hava kontrol edilir ve isi geri kazanilir
- **Hood egzoz sicakligi:** Tipik 70-90 C, nem icerigi 100-400 g/kg (kuru hava basina)
- **Isi geri kazanim potansiyeli:** Hood egzozundan %50-70 isi geri kazanilabilir

### Kondensat Tahliye (Condensate Evacuation)

Her silindir icindeki kondensat surekli tahliye edilmelidir. Kondensat birikimi isi transferi
ciddi sekilde engeller:

| Kondensat Film Kalinligi | Performans Etkisi | Isletme Durumu |
|---------------------------|-------------------|----------------|
| < 1 mm | Minimum etki | Iyi sifon calismasi |
| 1-3 mm | %5-15 performans dususu | Normal isletme |
| 3-5 mm | %15-25 performans dususu | Sifon bakimi gerekli |
| > 5 mm | %25+ performans dususu, titresim | Acil mudahale |

**Sifon tipleri:**
- **Stasyoner sifon (stationary siphon):** Sabit pozisyon, yuksek hizda iyi performans
- **Doner sifon (rotary siphon):** Dusuk hizda etkili, yuksek hizda yetersiz
- **Diferansiyel basinc tahliye:** Basinc farkiyla otomatik tahliye

## Exergy Analizi

### Exergy Verimi Hesabi

```
psi_drum = Ex_buharastirma / (Ex_buhar_giris - Ex_kondensat_cikis)

Burada:
  psi_drum          = Exergy verimi (boyutsuz, tipik 0.10-0.25)
  Ex_buharastirma   = Nem uzaklastirma islevi icin gereken minimum exergy (kW)
  Ex_buhar_giris    = Isitma buhari exergysi (kW)
  Ex_kondensat_cikis = Cikis kondensati exergysi (kW)

Ex_buhar = m_buhar x [(h_buhar - h0) - T0 x (s_buhar - s0)]
Ex_kondensat = m_kond x [(h_kond - h0) - T0 x (s_kond - s0)]

Burada:
  h0, s0 = Referans (olu durum) entalpi ve entropi (T0=298.15 K, P0=101.325 kPa)
  m_buhar = Isitma buhari debisi (kg/s)
  m_kond  = Kondensat debisi (kg/s)
```

### Exergy Verimi Benchmark

| Uygulama | Exergy Verimi (%) | Aciklama |
|----------|-------------------|----------|
| Kagit makinesi (eski, acik hood) | 10-14 | Yuksek hood kaybi, kondensat geri kazanim yok |
| Kagit makinesi (modern, kapali hood) | 15-22 | Hood isi geri kazanim, kaskad buhar |
| Tek silindir (gida) | 15-20 | Dusuk kapasite, orta verimlilik |
| Cift silindir (kimya) | 18-25 | Iyi kondensat yonetimi |
| En iyi uygulama (best practice) | 22-25 | Tam optimize edilmis sistem |
| Teorik sinir | ~35 | Kayipsiz ideal konduksiyon kurutma |

Silindir kurutucunun exergy verimi, konvektif kurutuculara (sprey: %15-25, tanel: %8-18)
kiyasla genellikle daha yuksektir cunku:
- Sicak hava yerine yogusma isisi kullanilir (daha dusuk tersinmezlik)
- Egzoz havasi kaybi cok daha azdir
- Dogrudan temas isi transferi daha etkilidir

## Kayip Dagilimi (Exergy Destruction Breakdown)

Tipik bir silindir kurutucu icin exergy kayip dagilimi:

| Kayip Kalemi | Enerji Payi (%) | Exergy Payi (%) | Aciklama |
|--------------|----------------:|----------------:|----------|
| Buharastirma (faydali cikti) | ~55-65 | ~10-25 | Ana islev -- nem uzaklastirma |
| Kondensat kayiplari (condensate losses) | ~12-18 | ~20-30 | Kondensat isi icerigi + flash buhar |
| Radyasyon ve konveksiyon (radiation/convection) | ~8-12 | ~15-25 | Silindir yuzey, boru hatti, uc kayiplari |
| Hood egzoz kaybi (hood exhaust) | ~5-10 | ~10-20 | Nemli sicak hava atigi (kapali hoodda daha az) |
| Urun isitma (product sensible heating) | ~5-8 | ~5-10 | Urunun cikis sicakligina isitilmasi |
| Isi transfer tersinmezligi | -- | ~15-25 | Buhar-cidar-urun arasi sonlu sicaklik farki |
| Diger (kacak, mekanik, baslangic/durus) | ~5-8 | ~5-10 | Hava kacaklari, mekanik surtunme |

**En buyuk exergy kaybi kaynaklari:**
1. Isi transfer tersinmezligi -- buhar yogusma sicakligi ile urun sicakligi arasi fark
2. Kondensat kayiplari -- ozellikle flash buhar geri kazanimi yapilmiyorsa
3. Radyasyon kayiplari -- yalitimsiz silindir uclari ve boru hatlari

## Avantajlar ve Dezavantajlar

### Avantajlar

| Avantaj | Aciklama |
|---------|----------|
| Yuksek isi transfer verimi | Dogrudan temas, sicak hava kaybi yok |
| Daha yuksek exergy verimi | Konvektif sistemlere gore %5-10 daha iyi |
| Kompakt tasarim | Ayni kapasite icin daha kucuk yer gereksimi |
| Kisa kalma suresi | 2-30 saniye -- hassas urunler icin uygun |
| Ince film kontrolu | 0.1-1.5 mm film kalinligi ayarlanabilir |
| Temiz isletme | Kapali sistem, toz emisyonu minimum |
| Kolay olcekleme | Silindir boyutu ve sayisi ile kapasite arttirma |

### Dezavantajlar

| Dezavantaj | Aciklama |
|------------|----------|
| Sinirli urun yelpazesi | Sadece sivi/bulamac besleme -- katiya uygun degil |
| Yuzey kirlilik riski | Urun birikimi isi transferi dusurur |
| Kondensat yonetimi | Sifon bakimi kritik ve karmasik |
| Yuksek yatirim maliyeti | Basincli kap sertifikasi, ozel tasarim |
| Mekanik asinma | Doctor blade ve sifon asinmasi -- periyodik degisim |
| Urun yapiskanligi | Bazi urunler yuzeyden zor ayrilir |

## Uygulamalar

### Kagit Endustrisi (Ana Uygulama)

- **Gazete kagidi:** 40-50 silindir, 2-8 bar buhar, 500-1,500 m/dk makine hizi
- **Ambalaj kagidi (kraft):** 50-60 silindir, 4-10 bar, 200-800 m/dk
- **Karton:** 60+ silindir, 4-10 bar, 100-500 m/dk
- **Tissue (Yankee dryer):** Tek buyuk silindir (4-5 m cap), 6-10 bar, yuksek buhar basinci
- Kagit kurutma toplam enerji tuketiminin %60-70'ini olusturur

### Gida Endustrisi

- Bebek mamasi (instant cereal), patates pul, nisasta, maya, meyve konsantreleri
- Tipik tek veya cift silindir, 3-6 bar buhar

### Kimya Endustrisi

- Kimyasal pullar (flakes), pigmentler, kaolin, polimer filmler
- Tipik tek silindir, 4-8 bar buhar

## Iyilestirme Onlemleri

### Enerji Tasarrufu Potansiyeli

| Onlem | Tasarruf (%) | Tipik Geri Odeme | Yatirim (EUR) | Detay |
|-------|-------------|-----------------|---------------|-------|
| Kondensat flash buhar geri kazanimi | 5-12 | 0.5-1.5 yil | 15,000-80,000 | Flash buhar tank ve isi degistirici |
| Kondensat sifon optimizasyonu | 3-8 | 0.5-1 yil | 5,000-30,000 | Stasyoner sifon veya rotary joint |
| Hood egzoz isi geri kazanimi | 5-15 | 1-3 yil | 50,000-300,000 | Egzoz nemli havasinin isisi ile hava on isitma |
| Cep havalari (pocket ventilation) | 3-8 | 1-2 yil | 30,000-150,000 | Kagit makinesi ozel -- silindirler arasi hava yonetimi |
| Yalitim iyilestirme | 2-5 | 0.5-1 yil | 5,000-25,000 | Silindir uclarindan ve boru hattindan |
| Buhar basinci optimizasyonu | 2-4 | -- | Yatirim gerektirmez | Urun kalitesine gore minimum basinc secimi |
| Kaskad buhar sistemi kurulumu | 8-15 | 2-4 yil | 100,000-500,000 | Cok gruplu kademeli buhar dagilimi |
| Hood kapama / modernizasyon | 10-20 | 2-5 yil | 200,000-1,000,000 | Acik hooddan kapali hooda gecis |
| Kondensat geri donus oranini artirma | 3-8 | 0.5-1 yil | 10,000-50,000 | Kondensat hatti ve pompa iyilestirme |
| Hava kacak kontrolu | 1-3 | 0.5 yil | 2,000-10,000 | Hood sizdirmazlik iyilestirme |

### Onceliklendirme

1. **Dusuk/sifir yatirim:** Buhar basinci optimizasyonu, hava kacak kontrolu
2. **Hizli geri odeme (<1 yil):** Kondensat sifon bakimi, yalitim, kondensat geri donus
3. **Orta vadeli (1-3 yil):** Hood isi geri kazanimi, flash buhar geri kazanimi, cep havalari
4. **Uzun vadeli (3-5 yil):** Hood modernizasyonu, kaskad buhar sistemi

## Yatirim Maliyetleri

### Tek/Cift Silindir Kurutucu (Gida/Kimya)

| Silindir Boyutu (cap x uzunluk, m) | Yuzey Alani (m2) | Su Buharlastirma (kg/h) | SMER (kg/kWh) | Tahmini Yatirim (EUR) |
|------------------------------------:|------------------:|------------------------:|---------------:|----------------------:|
| 0.8 x 1.5 | 3.8 | 100-200 | 1.0-1.5 | 50,000-120,000 |
| 1.0 x 2.0 | 6.3 | 200-400 | 1.1-1.6 | 100,000-250,000 |
| 1.2 x 2.5 | 9.4 | 350-650 | 1.2-1.7 | 200,000-450,000 |
| 1.5 x 3.0 | 14.1 | 550-1,000 | 1.3-1.8 | 350,000-700,000 |
| 2.0 x 5.0 | 31.4 | 1,300-2,300 | 1.4-2.0 | 900,000-1,500,000 |

> **Not:** Fiyatlar 2026 yili Avrupa piyasasi, montaj haric. Cift silindir (double drum) icin ~1.5x carpan uygulanir.

### Kagit Makinesi Kurutma Bolumu

| Yatirim Kalemi | Maliyet Araligi (EUR) | Not |
|----------------|----------------------:|-----|
| Tam kurutma bolumu (yeni makine) | 5,000,000-20,000,000 | 40-60 silindir, hood, kondensat sistemi |
| Hood modernizasyonu (acik --> kapali) | 200,000-1,000,000 | Mevcut makineye retrofit |
| Kaskad buhar sistemi kurulumu | 100,000-500,000 | Mevcut silindirler icin buhar yeniden dagitimi |
| Cep havalari sistemi | 30,000-150,000 | Mevcut hooda ekleme |
| Kondensat sistemi yenileme | 50,000-200,000 | Sifon, seperator, pompa degisimi |

### SMER Benchmark Tablosu

| Durum | SMER (kg/kWh) | Aciklama |
|-------|---------------|----------|
| Dusuk performans | < 1.0 | Eski ekipman, yetersiz kondensat tahliye, acik hood |
| Tipik performans | 1.0-1.5 | Standart isletme, periyodik bakim |
| Iyi performans | 1.5-2.0 | Modern ekipman, iyi kondensat yonetimi |
| En iyi uygulama (best practice) | 2.0-2.5 | Optimize edilmis kaskad buhar, kapali hood |
| Teorik sinir | ~3.0 | Kayipsiz ideal konduksiyon kurutma |

## İlgili Dosyalar

- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Exergy hesaplama formuleri: `dryer/formulas.md`
- Yalitim cozumleri: `dryer/solutions/insulation.md`
- Kagit kurutma sektor bilgisi: `dryer/sectors/paper_drying.md`
- Sprey kurutucu: `dryer/equipment/spray_dryer.md`
- Isi pompali kurutucu: `dryer/equipment/heat_pump_dryer.md`
- Egzoz havasi isi geri kazanimi: `dryer/solutions/exhaust_heat_recovery.md`
- Kazan sistemleri (buhar kaynagi): `boiler/equipment/systems_overview.md`
- Fabrika seviyesi analiz: `factory/cross_equipment.md`

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press -- Kurutma teknolojileri temel referansi
2. Karlsson, M. (2000). *Papermaking Part 2: Drying*, TAPPI Press -- Kagit kurutma ozel referansi
3. European Commission (2015). *Reference Document on Best Available Techniques for the Production of Pulp, Paper and Board (BREF)* -- AB en iyi teknikler referansi
4. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press
5. Valmet, *Paper Machine Dryer Section -- Technical Documentation and Energy Optimization Guide*
6. Andritz AG, *Drum Dryer Technical Documentation and Selection Guide*
7. Kadant Inc., *Condensate Removal and Steam System Optimization for Paper Machines*
8. Spirax Sarco, *The Steam and Condensate Loop* -- Kondensat yonetimi referansi
9. DOE/AMO, *Improving Process Heating System Performance -- A Sourcebook for Industry*
10. TAPPI Standards -- Kagit kurutma performans test yontemleri (TIP 0404-36, TIP 0404-52)
