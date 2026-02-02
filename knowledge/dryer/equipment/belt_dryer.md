---
title: "Bant Kurutucu (Belt/Conveyor Dryer)"
category: dryer
equipment_type: dryer
keywords:
  - bant kurutucu
  - belt dryer
  - konveyor kurutucu
  - surekli kurutma
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/temperature_optimization.md
  - dryer/sectors/food_drying.md
use_when:
  - "Bant kurutucu analiz edilirken"
priority: medium
last_updated: 2026-02-01
---

# Bant Kurutucu (Belt/Conveyor Dryer)

## Genel Bakis

Bant kurutucu (belt dryer, conveyor dryer), endustriyel kurutma uygulamalarinda yaygin olarak kullanilan surekli (continuous) bir konvektif kurutma sistemidir. Urun, hareketli delikli (perforated) bir bant uzerinde tasinirken sicak hava urunun icinden veya uzerinden gecirilerek nem uzaklastirilir. Buyuk kapasiteli, dusuk-orta sicaklikta ve hassas urunlerin kurutulmasinda tercih edilen bir ekipmandir.

Bant kurutucunun en belirgin avantaji, cok bolgeli (multi-zone) sicaklik kontrol imkanidir. Her bolgede bagimsiz sicaklik, hava debisi ve hava yonu ayarlanarak kurutma profili urunun ozelliklerine gore optimize edilebilir. Bu ozellik, tek-sicaklikli kurutuculara gore hem enerji verimliligi hem de urun kalitesi acisindan onemli bir ustunluk saglar.

Tipik kapasite araligi 200 ila 20.000 kg/h olup, bant genisligi 1-5 m, bant uzunlugu 5-40 m arasinda degisir. Endüstriyel olcekte sebze, bitki, granul, mineral, biyokutle ve aritma camuru kurutmada yaygindır.

---

## Calisma Prensibi (Working Principle)

### Temel Islem Adimlari

1. **Urun besleme (feeding):** Islak urun, titresimli besleyici, vidalı konveyor veya bant yayici ile delikli bant uzerine duzgun bir tabaka halinde serilir. Tabaka kalinligi genellikle 20-150 mm arasindadir.
2. **Hava hazirlama (air preparation):** Her bolge icin hava, isitici serpantin (buhar veya sicak su), dogal gaz brulor ya da atik isi kaynagi ile hedef sicakliga isitilir.
3. **Kurutma (drying):** Sicak hava, urun tabakasi boyunca gecirilerek nemli havanin buharlasmasini saglar. Hava, urunun goczenekli (porous) yapisindan gecerken nem transfer edilir.
4. **Egzoz (exhaust):** Nemlenip sogumis hava, her bolgeden ayri veya toplu olarak egzoz kanalina yonlendirilir.
5. **Urun cikisi (product discharge):** Kurutulmus urun, bant sonundaki dokulme noktasindan toplanir; gerektiginde son bolgede sogutma yapilir.

### Hava Akis Tipleri

**Through-circulation (hava tabakadan gecirme):**
- Sicak hava, delikli banttan ve urun tabakasi boyunca dikey olarak (asagidan yukari veya yukaridan asagi) gecirilerek dogrudan temas saglanir.
- En yaygin ve en verimli konfigurasyondur. Yuksek kutle transferi hizi sebebiyle kurutma suresi kisalir.
- Urun boyutu ve sekli uygun olmalidir (granul, dilim, parca seklinde); toz urunlerde tikanma riski vardir.

**Cross-flow (capraz akis):**
- Hava, bantla paralel veya bant yuzeyine yatay olarak akar.
- Tabaka kalinliginin cok yuksek oldugu veya urunun hava gecirgenliginin dusuk oldugu durumlarda tercih edilir.
- Through-circulation'a gore daha dusuk kutle transferi hizi ve daha uzun kurutma suresi gerektirir.

**Kombine akis (combined):**
- Farkli bolgelerde farkli hava akis yonleri kullanilir (orn. ilk bolgede asagidan yukari through-circulation, son bolgede cross-flow).
- En esnek tasarimdir; her bolgenin gereksinimlerine uyarlanabilir.

---

## Konfigurasyonlar (Configurations)

### Tek Gecisli (Single-Pass)

Urun, tek bir bant uzerinde bastan sona bir kez gecerek kurutulur. Basit tasarim, dusuk bakim gereksinimi. Dusuk-orta nem azaltma icin uygundur (orn. %40 -> %10).

### Cok Gecisli (Multi-Pass)

Birden fazla bant ust uste veya ard arda dizilir. Urun, bir banttan digerine aktarilarak kurutma suresi uzatilir. Yuksek nem azaltma gereken durumlarda (orn. %80 -> %5) ve sinirli zemin alaninda tercih edilir. 2-5 gecis tipiktir.

### Cok Bolgeli (Multi-Zone)

Her bolge bagimsiz sicaklik, hava debisi ve hava yonu kontrolune sahiptir. Tipik olarak 2-6 bolge kullanilir:

| Bolge | Amac | Tipik Sicaklik (C) | Hava Debisi | Aciklama |
|-------|------|---------------------|-------------|----------|
| Bolge 1 — On kurutma | Hizli yuzey nemi giderme | 120-150 | Yuksek | Sabit kurutma hizi donemi |
| Bolge 2 — Ana kurutma | Hacimsel nem uzaklastirma | 90-120 | Orta-yuksek | Gecis donemi |
| Bolge 3 — Son kurutma | Hedef nem degerine ulasma | 60-90 | Orta | Azalan hiz donemi, hassas kontrol |
| Bolge 4 — Sogutma | Urun sogutma | 25-40 | Dusuk-orta | Paketleme oncesi stabilizasyon |

Cok bolgeli tasarim, tek bolgeli sisteme gore %8-15 enerji tasarrufu saglayabilir cunku her asamada yalnizca gerekli kalitede (sicaklikta) enerji kullanilir.

---

## Tipik Calisma Parametreleri (Typical Operating Conditions)

| Parametre | Deger | Birim | Not |
|-----------|-------|-------|-----|
| Giris hava sicakligi | 60-150 | C | Urune bagli; hassas urunlerde <80 C |
| Egzoz havasi sicakligi | 40-75 | C | Dusuk = daha verimli |
| Kapasite | 200-20.000 | kg/h | Besleme debisi (islak bazda) |
| Bant genisligi | 1-5 | m | Endüstriyel boyut |
| Bant uzunlugu | 5-40 | m | Tek gecis icin |
| Bant hizi | 0.3-5.0 | m/min | Urun ve nem icerigi ile orantili |
| Urun tabaka kalinligi | 20-150 | mm | Homojen dagilim kritik |
| Bolge sayisi | 2-6 | adet | Cok bolgeli tasarimda |
| Hava debisi (bolge basina) | 2.000-20.000 | m3/h | Through-circulation icin |
| Toplam isitma gucu | 100-5.000 | kW | Kapasiteye bagli |
| Fan elektrik tuketimi | 10-120 | kW | Toplam fan gucu |
| Ozgul enerji tuketimi | 3.000-6.000 | kJ/kg su buharlastirma | Geri kazanimsiz sistem |
| SMER | 0.5-1.2 | kg/kWh | Standart sistem; geri kazanimli 1.5'e kadar |

---

## Exergy Analizi (Exergy Analysis)

Bant kurutucular konvektif kurutucu sinifindadir ve diger konvektif kurutucularda oldugu gibi dusuk exergy verimine sahiptir. Bunun temel nedeni, yuksek kaliteli enerjinin (>100 C sicak hava) dusuk kaliteli bir isleme (50-100 C'de buhaslasma) kullanilmasidir.

### Exergy Verimi Araligi

| Performans Seviyesi | Exergy Verimi (%) | Aciklama |
|---------------------|-------------------|----------|
| Dusuk | <6 | Tek bolgeli, eski sistem, geri kazanimsiz |
| Orta-alt | 6-8 | Standart cok bolgeli, geri kazanimsiz |
| Orta | 8-11 | Optimize cok bolgeli sistem |
| Iyi | 11-14 | Isi geri kazanimli, resirkulasyonlu |
| Cok iyi | >14 | Isi pompasi entegreli veya tam optimize hibrit |

Tipik endustriyel bant kurutucuda exergy verimi **%6-14** arasindadir (SMER 0.5-1.2 kg/kWh).

### Exergy Bilancosu (Tipik Ornek)

Ornek: 3 bolgeli bant kurutucu, 500 kW isitma gucu, 25 kW fan, giris havasi 120 C, egzoz 60 C

```
Exergy girdisi:
  Isitici exergy   = Q_heater x (1 - T_0/T_supply)
                   = 500 x (1 - 298.15/393.15)
                   = 500 x 0.242 = 121.0 kW
  Fan elektrik     = 25.0 kW (saf exergy)
  TOPLAM GIRIS     = 146.0 kW (100%)

Exergy cikisi:
  Faydali buhaslasma exergy'si   = ~14.6 kW  (~10%)

Exergy kayiplari:
  Egzoz havasi exergy kaybi       = ~43.8 kW  (~30%)
  Isitma tersinmezligi            = ~29.2 kW  (~20%)
  Kurutma prosesi tersinmezligi   = ~40.9 kW  (~28%)
  Govde/radyasyon kaybi           = ~10.2 kW  (~7%)
  Fan tersinmezligi               = ~7.3 kW   (~5%)
  TOPLAM KAYIP                    = ~131.4 kW (~90%)
```

---

## Kayip Dagilimi (Loss Breakdown)

Bant kurutucudaki exergy yikimi ve kayiplari, asagidaki bilesenlerden olusur:

| Kayip Bileseni | Tipik Oran (%) | Geri Kazanilabilir mi? | Azaltma Yontemi |
|----------------|---------------|------------------------|-----------------|
| Egzoz havasi exergy kaybi (exhaust loss) | 25-35 | Evet — en buyuk firsat | Isi geri kazanimi, resirkulasyon |
| Kurutma prosesi tersinmezligi (drying irreversibility) | 20-30 | Kismi — termodinamik sinir | Cok bolgeli sicaklik profili |
| Isitma tersinmezligi (heating irreversibility) | 15-25 | Kismi | Dusuk sicaklik kaynagi, isi pompasi |
| Govde/yuzey kayiplari (shell/radiation loss) | 5-10 | Evet | Izolasyon iyilestirme |
| Fan ve mekanik kayiplar (fan/mechanical loss) | 3-8 | Kismi | VFD, verimli fan |
| Sizinti ve diger (leakage/misc.) | 2-5 | Evet | Sizdirazlik, bakim |

**En buyuk iyilestirme firsati:** Egzoz havasi isi geri kazanimi. Tipik bant kurutucuda egzoz havasi toplam enerji girdisinin %25-35'ini tasir ve bu enerjinin %40-70'i hava-hava isi degistirici veya kondenser ile geri kazanilabilir.

**Ikinci buyuk firsat:** Cok bolgeli sicaklik optimizasyonu. Ilk bolgelerde yuksek sicaklik (hizli kurutma), son bolgelerde dusuk sicaklik (hassas kontrol) stratejisi, tek sicaklikli sisteme gore exergy yikimini %15-25 azaltir.

---

## Avantajlar ve Dezavantajlar

### Avantajlar

- **Cok bolgeli sicaklik kontrolu:** Her bolgede bagimsiz sicaklik/hava debisi ayari ile optimize kurutma profili olusturulabilir
- **Hassas urunlere uygunluk:** Dusuk sicaklik (60-80 C) ile isiya duyarli urunler (sebze, bitki, ilac) guvenle kurutulabilir
- **Surekli islem:** Kesintisiz uretim; yuksek kapasite (20.000 kg/h'e kadar)
- **Urun bozunmasi dusuk:** Urun hareketsiz olarak bant uzerinde durur; mekanik hasar minimumdur
- **Kolay otomasyon:** Bant hizi, sicaklik, hava debisi PLC ile tam otomatik kontrol edilebilir
- **Genis urun yelpazesi:** Dilim, parca, granul, pelet, levha seklindeki urunlere uygulanabilir

### Dezavantajlar

- **Buyuk alan gereksinimi:** Uzun bant (5-40 m) ve destek ekipmani icin genis zemin alani gerekir
- **Dusuk exergy verimi:** Konvektif sinifin genel dezavantaji; %6-14 tipik exergy verimi
- **Bant bakimi:** Delikli bant tikanma, asinma ve kirlenmeye maruz kalir; duzenli temizlik sart
- **Tabaka homojenlik gereksininimi:** Esit olmayan tabaka kalinligi yetersiz/asiri kurutma ve enerji israfina yol acar
- **Yatirim maliyeti:** Cok bolgeli buyuk kapasiteli sistemler yuksek ilk yatirim gerektirir
- **Toz emisyonu:** Hafif ve toz urunlerde hava akisiyla urun kaybi ve emisyon riski

---

## Uygulamalar (Applications)

| Sektor / Urun | Tipik Sicaklik (C) | Giris Nem (%) | Cikis Nem (%) | Not |
|----------------|---------------------|---------------|---------------|-----|
| Sebze (havuc, sogan, patates) | 60-90 | 70-85 | 5-10 | Dusuk sicaklik, renk koruma |
| Bitkiler ve baharatlar (herbs) | 40-70 | 60-80 | 8-12 | Cok dusuk sicaklik, aroma koruma |
| Meyve dilimleri (elma, muz) | 55-75 | 75-88 | 10-15 | Hassas, vitamin koruma |
| Granul ve pelet (plastik, gubre) | 80-130 | 5-30 | 0.1-2 | Orta-yuksek sicaklik |
| Mineral ve kimyasal (pigment) | 100-150 | 20-50 | 0.5-5 | Yuksek sicaklik, agresif ortam |
| Biyokutle (odun yongasi, camur) | 80-120 | 50-70 | 10-20 | Yuksek kapasite, on kurutma |
| Aritma camuru (sludge) | 80-110 | 70-85 | 20-40 | Yapiskanlık, koku problemi |
| Makarna | 60-85 | 25-35 | 11-13 | Uzun sureli, catlamaya hassas |

---

## Iyilestirme Firsatlari (Improvement Opportunities)

### 1. Egzoz Havasi Isi Geri Kazanimi (Exhaust Heat Recovery)

Egzoz havasindaki termal enerji, hava-hava isi degistirici (recuperator), kondensasyon isi geri kazanimi veya isi borusu (heat pipe) ile giris havasinin on isitilmasina aktarilir.

- Tipik tasarruf: %15-25 termal enerji
- Yatirim: 25.000-120.000 EUR
- Geri donus suresi: 1-2.5 yil

### 2. Hava Resirkulasyonu (Air Recirculation)

Egzoz havasinin bir kismini (nem doygunluk sinirinin altinda kalmak kaydiyla) giris havasina geri karıstirmak.

- Tipik tasarruf: %10-20 termal enerji
- Yatirim: 10.000-50.000 EUR
- Geri donus suresi: 0.5-1.5 yil
- Dikkat: Egzoz nem orani izlenmeli; %85 RH ustunde yogusma riski

### 3. Cok Bolgeli Sicaklik Optimizasyonu (Multi-Zone Temperature Optimization)

Mevcut cok bolgeli sistemde her bolgenin sicaklik ve hava debisi setpointlerini urunun kurutma kinetigi ile eslestirmek.

- Tipik tasarruf: %5-12 termal enerji
- Yatirim: 5.000-20.000 EUR (kontrol sistemi guncellemesi)
- Geri donus suresi: 0.5-1 yil

### 4. Degisken Hizli Fan Suruculeri (VFD — Variable Frequency Drives)

Fan motorlarina frekans konvertoru eklenerek hava debisini gercek zamanda talebe gore ayarlamak.

- Tipik tasarruf: %10-20 elektrik (fan gucu kubikal oranla duser)
- Yatirim: 8.000-30.000 EUR
- Geri donus suresi: 1-2 yil

### 5. Isi Pompasi Entegrasyonu (Heat Pump Integration)

Ozellikle 50-80 C sicaklik araliginda calisan bant kurutucularda kondenser isisi ile kurutma havasini isitmak, evaporator ile egzoz havasini sogutup nemini almak.

- Tipik tasarruf: %30-50 primer enerji
- SMER artisi: 1.5-2.5 kat (COP 2.5-4.0)
- Yatirim: 80.000-400.000 EUR
- Geri donus suresi: 3-5 yil
- Exergy verimi %14 uzerine cikar

### 6. Urun Tabaka Kalinligi ve Bant Hizi Kontrolu

Online nem olcum (NIR, mikrodalga) ile tabaka kalinligi ve bant hizini gercek zamanli optimize etmek.

- Tipik tasarruf: %3-8 enerji + urun kalitesi iyilesmesi
- Yatirim: 15.000-50.000 EUR
- Geri donus suresi: 1-2 yil

### 7. Izolasyon Iyilestirmesi

Kurutucu kasa ve kanal yuzeylerinde izolasyon kalinligini artirmak veya hasarli izolasyonu yenilemek.

- Tipik tasarruf: %2-5 termal enerji
- Yatirim: 5.000-25.000 EUR
- Geri donus suresi: 0.5-1.5 yil

### Iyilestirme Ozet Tablosu

| Onlem | Enerji Tasarrufu | Yatirim (EUR) | Geri Donus (yil) | Oncelik |
|-------|------------------|---------------|-------------------|---------|
| Egzoz isi geri kazanimi | %15-25 | 25.000-120.000 | 1-2.5 | Yuksek |
| Hava resirkulasyonu | %10-20 | 10.000-50.000 | 0.5-1.5 | Yuksek |
| Bolge sicaklik optimizasyonu | %5-12 | 5.000-20.000 | 0.5-1 | Orta-yuksek |
| Fan VFD | %10-20 elektrik | 8.000-30.000 | 1-2 | Orta-yuksek |
| Isi pompasi entegrasyonu | %30-50 | 80.000-400.000 | 3-5 | Orta (uzun vadeli) |
| Tabaka/hiz kontrolu | %3-8 | 15.000-50.000 | 1-2 | Orta |
| Izolasyon iyilestirme | %2-5 | 5.000-25.000 | 0.5-1.5 | Dusuk-orta |

---

## Yatirim (Investment Costs)

| Kapasite Sinifi | Kapasite (kg/h) | Bant Boyutu | Bolge Sayisi | Tahmini Yatirim (EUR) |
|-----------------|-----------------|-------------|--------------|----------------------|
| Kucuk olcek | 200-1.000 | 1-2 m x 5-10 m | 2-3 | 80.000-250.000 |
| Orta olcek | 1.000-5.000 | 2-3 m x 10-20 m | 3-4 | 250.000-700.000 |
| Buyuk olcek | 5.000-10.000 | 3-4 m x 20-30 m | 4-5 | 700.000-1.500.000 |
| Cok buyuk olcek | 10.000-20.000 | 4-5 m x 30-40 m | 5-6 | 1.500.000-3.000.000 |

**Ek maliyet kalemleri:**
- Isi geri kazanim unitesi: +%10-20 sistem maliyeti
- Isi pompasi entegrasyonu: +%25-50 sistem maliyeti
- Gelismis otomasyon (SCADA): +%5-10 sistem maliyeti
- Montaj ve devreye alma: +%10-15 ekipman maliyeti

**Isletme maliyeti (tipik):**
- Enerji: toplam isletme maliyetinin %60-75'i
- Bakim: %10-15
- Isgucuc: %10-20
- Sarf malzeme (bant, filtre): %5-10

---

## İlgili Dosyalar

- `dryer/formulas.md` — Kurutma exergy hesaplama formuller ve denklemler
- `dryer/benchmarks.md` — Kurutucu tipleri arasi SMER, enerji ve exergy verimi karsilastirma
- `dryer/solutions/exhaust_heat_recovery.md` — Egzoz havasi isi geri kazanim cozumleri
- `dryer/solutions/temperature_optimization.md` — Cok bolgeli sicaklik optimizasyonu
- `dryer/sectors/food_drying.md` — Gida sektoru kurutma uygulamalari ve benchmarklar
- `dryer/equipment/tunnel_dryer.md` — Tunel kurutucu ile karsilastirma
- `dryer/equipment/fluidized_bed.md` — Akiskan yatak kurutucu alternatifi
- `dryer/equipment/heat_pump_dryer.md` — Isi pompali kurutucu (hibrit potansiyel)
- `dryer/psychrometrics.md` — Nemli hava termodinamigi ve psikrometrik hesaplar
- `factory/cross_equipment.md` — Ekipmanlar arasi entegrasyon firsatlari

---

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press. (Bolum 7: Conveyor Dryers)
2. Kemp, I.C. (2012). "Fundamentals of Energy Analysis of Dryers," in *Modern Drying Technology*, Vol. 4, Wiley-VCH.
3. EU BREF (2009). *Reference Document on Best Available Techniques for Energy Efficiency*, European Commission.
4. EU BREF (2006). *Reference Document on Best Available Techniques in the Food, Drink and Milk Industries*, European Commission.
5. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press.
6. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
7. Bahu, R.E. (1991). "Energy Considerations in Dryer Design," *Drying Technology*, 9(3), pp. 795-808.
8. Aghbashlo, M. et al. (2013). "A review on exergy analysis of drying processes and systems," *Renewable and Sustainable Energy Reviews*, 22, pp. 1-22.
9. Carbon Trust (2011). *Industrial Energy Efficiency Accelerator — Guide to the Drying Sector* (CTG058).
10. Strumiłło, C., Jones, P.L. & Zyłła, R. (2014). "Energy Aspects in Drying," in *Handbook of Industrial Drying*, CRC Press.
