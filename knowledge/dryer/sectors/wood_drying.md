---
title: "Kereste Kurutma Firinlari (Wood/Lumber Drying Kilns)"
category: dryer
equipment_type: dryer
keywords:
  - kereste kurutma
  - wood drying
  - lumber kiln
  - ahsap kurutma
  - agac kurutma firini
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/equipment/tunnel_dryer.md
  - dryer/equipment/heat_pump_dryer.md
  - dryer/solutions/heat_pump_retrofit.md
  - dryer/solutions/solar_preheating.md
  - dryer/solutions/exhaust_heat_recovery.md
use_when:
  - "Kereste kurutma analiz edilirken"
  - "Ahsap kurutma firini degerlendirilirken"
priority: medium
last_updated: 2026-02-01
---

# Kereste Kurutma Firinlari (Wood/Lumber Drying Kilns)

## Genel Bakis

Kereste kurutma (wood drying / seasoning), taze kesilmis odunun (green wood) nem icerigini hedef seviyeye dusurme islemidir. Kurutma, ahsabin boyutsal stabilite (dimensional stability) kazanmasi, curume ve mantar olusumunun onlenmesi, agirligin azaltilmasi ve isleme kolayliginin arttirilmasi icin zorunludur.

Dogal kurutma (air drying) hala kullanilmakla birlikte, endstriyel uretimde kontrolllu firin kurutma (kiln drying) baskin yontemdir. Firin kurutma, sicaklik, bagil nem ve hava akis hizinin hassas kontrolu sayesinde daha kisa surede, daha dusuk kusur oraniyla ve tekrarlanabilir sonuclar saglar.

Kereste sektoru, dusuk sicaklik gereksinimleri (40-90 C) nedeniyle isi pompali (heat pump) kurutma teknolojisinin en verimli uygulanabilecegi alanlardan biridir. Bu durum, exergy analizi acisindan buyuk optimizasyon potansiyeli tasir.

### Sektorel Enerji Profili

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Tipik enerji tuketimi | 800 - 2.000 | kWh/m3 kereste |
| Ozgul enerji tuketimi (SEC, geleneksel) | 2.500 - 5.000 | kJ/kg su buharlastirma |
| Ozgul enerji tuketimi (SEC, isi pompali) | 800 - 1.500 | kJ/kg su buharlastirma |
| SMER (geleneksel firin) | 0.5 - 1.0 | kg/kWh |
| SMER (isi pompali firin) | 1.5 - 4.0 | kg/kWh |
| Exergy verimi (geleneksel) | 4 - 8 | % |
| Exergy verimi (isi pompali) | 15 - 30 | % |

## Kurutma Yontemleri

### 1. Geleneksel Isitmali Firin (Conventional Kiln)

Buhar serpantini veya sicak su devreleri ile isitilan hava, kereste yiginlari uzerinden gecirilerek kurutma saglanir. En yaygin endstriyel yontemdir.

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Kurutma sicakligi | 40 - 90 | C |
| Bagil nem kontrolu | 40 - 90 | % |
| Hava hizi (istif arasi) | 1.5 - 3.0 | m/s |
| Kurutma suresi (25 mm yumusak odun) | 3 - 10 | gun |
| Kurutma suresi (50 mm sert odun) | 14 - 60 | gun |
| Firin kapasitesi | 20 - 200 | m3 kereste |
| SMER | 0.5 - 1.0 | kg/kWh |
| Enerji tuketimi | 800 - 1.500 | kWh/m3 |

Isi kaynagi olarak buhar serpantini (steam coils), sicak su serpantini, dogrudan yakma (direct fired) veya odun artiklari (biyokutle) kullanilabilir. Haftalarca suren donguler tipiktir.

### 2. Nem Alma Firini / Isi Pompali Firin (Dehumidification / Heat Pump Kiln)

Kapali devre calisan, nemli havanin evaporatorde sogutularak neminin yogustirilmasi ve kondenserde tekrar isitilarak geri gonderilmesi prensibine dayanan en enerji verimli kurutma yontemidir.

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Kurutma sicakligi | 30 - 60 | C |
| COP (Coefficient of Performance) | 2.5 - 4.0 | - |
| SMER | 1.5 - 4.0 | kg/kWh |
| Kurutma suresi (25 mm yumusak odun) | 5 - 14 | gun |
| Enerji tuketimi | 250 - 600 | kWh/m3 |
| Tipik kapasite | 10 - 100 | m3 kereste |

Avantajlari: %50-70 enerji tasarrufu, dusuk kusur orani, cevre emisyonu yok (kapali devre), yuksek kurutma kalitesi.

### 3. Vakum Firini (Vacuum Kiln)

Dusuk basinc altinda (50-300 mbar) suyun kaynama noktasini dusurerek, 40-70 C gibi dusuk sicakliklarda hizli kurutma saglar.

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Calisma basinci | 50 - 300 | mbar |
| Kurutma sicakligi | 40 - 70 | C |
| Kurutma suresi (25 mm) | 1 - 5 | gun |
| SMER | 0.8 - 1.5 | kg/kWh |
| Enerji tuketimi | 500 - 1.200 | kWh/m3 |
| Tipik kapasite | 5 - 30 | m3 kereste |

Degerli sert odun turleri (ceviz, mese, gul agaci) icin idealdir. Renk degisimi minimumdur. Yuksek yatirim maliyeti ve kucuk kapasite dezavantajlaridir.

### 4. Gunes Enerjili Firin (Solar Kiln)

Sera benzeri yapi icinde gunes enerjisiyle isitilan hava ile kurutma. Kirsal bolgeler, kucuk atolyeler ve dusuk maliyetli uygulamalar icin uygundur.

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Kurutma sicakligi | 30 - 60 | C (gun icinde degisken) |
| Kurutma suresi | 14 - 90 | gun (mevsim ve iklime bagli) |
| Enerji tuketimi (fan + kontrol) | 50 - 150 | kWh/m3 |
| Tipik kapasite | 5 - 50 | m3 kereste |

Cok dusuk SEC (temel olarak fan enerjisi), ancak yavas ve mevsime bagimlidir. Hibrit sistemler (gunes + isi pompasi) ile hem maliyet hem sure optimize edilebilir.

### 5. Yuksek Sicaklik Firini (High-Temperature Kiln)

100 C uzerinde (tipik 100-130 C) calisan hizli kurutma yontemidir.

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Kurutma sicakligi | 100 - 130 | C |
| Kurutma suresi (25 mm yumusak odun) | 1 - 3 | gun |
| SMER | 0.4 - 0.8 | kg/kWh |

Avantajlari cok kisa kurutma suresidir. Dezavantajlari ise yuksek enerji tuketimi, renk koyulasmasi, recine akmasi, ic catlak (honeycomb) ve kabuk sertlesmesi (case hardening) riskidir. Genellikle yapisal kereste ve ambalaj odunu icin kullanilir, mobilya kerestesi icin uygun degildir.

## Kurutma Sureci

Tipik bir kereste kurutma dongusu asagidaki asamalardan olusur:

1. **Yas kereste (green wood):** Nem icerigi %60-100+ (kuru bazda). Agac turune gore degisir — kavak %80-120, mese %60-100, cam %80-150.

2. **Kosullama (conditioning / warming up):** Kereste firina yerlestirilir ve dusuk sicaklik, yuksek nem ortaminda birkacsaat bekletilir. Amac: iç ve dis sicakligin esitlenmesi.

3. **Kurutma (drying):** Sicaklik ve bagil nem, kurutma cizelgesine (drying schedule) gore kademeli olarak ayarlanir. Lif doygunlugu noktasinin (fiber saturation point, FSP ~ %28-30) altina indikten sonra kurutma hizi yavaslar.

4. **Esitleme (equalization):** Kurutma sonunda istif icindeki kerestelerin nem icerikleri arasindaki farki minimuma indirmek icin bagil nem yukseltilir. Tipik hedef: ortalama nem +/- %1-2.

5. **Kosullama (stress relief / conditioning):** Yuzey gerilmelerini gidermek icin yuksek bagil nem ortaminda (>85% RH) 4-12 saat bekleme. Kabuk sertlesmesini (case hardening) onler.

6. **Sogutma (cooling):** Kereste yavasca sogutulur ve firindan cikarilir.

**Hedef nem icerikleri:**

| Kullanim Alani | Hedef Nem (% kuru baz) |
|----------------|------------------------|
| Mobilya (furniture) | 8 - 10 |
| Dograma (joinery) | 10 - 12 |
| Parke (flooring) | 8 - 10 |
| Dis cephe (exterior) | 12 - 15 |
| Yapi kerestesi (structural / construction) | 18 - 20 |
| Ambalaj (packaging) | 18 - 22 |

## Kurutma Cizelgesi (Drying Schedule)

Kurutma cizelgesi, agac turu, kereste kalinligi ve hedef nem icerigine gore belirlenen sicaklik ve bagil nem adimlarinin programidir. Dogru cizelge, kurutma kalitesini belirleyen en kritik faktordur.

### Cizelge Parametreleri

- **Kuru termometre sicakligi (dry-bulb temperature):** Firin icindeki hava sicakligi
- **Yas termometre sicakligi (wet-bulb temperature):** Nemli hava sicakligi — bagil nem kontrolu icin kullanilir
- **Kuru-yas termometre farki (wet-bulb depression):** Kurutma hizini belirler — fark arttikca kurutma hizi artar
- **Hava hizi:** Istif arasindan gecen hava hizi (1.5-3.0 m/s tipik)

### Tipik Cizelge Yaklasimi

Kurutma basinda dusuk sicaklik ve dusuk yas termometre farki uygulanir (yavas kurutma). Nem icerigi dustukce sicaklik artirilir ve yas termometre farki genisletilir (agresif kurutma). FSP altina indikten sonra sicaklik daha da artirilabilir.

### Kurutma Kusurlari ve Onleme

Yanlis cizelge uygulanmasi durumunda olusabilecek kusurlar:

| Kusur | Ingilizce | Nedeni | Onlem |
|-------|-----------|--------|-------|
| Yuzey catlagi | Surface check | Yuzey hizli kurur, ic nemli kalir | Baslangicta yuksek nem |
| Uc catlagi | End split | Uclerden hizli nem kaybi | Uc kaplama (end sealing) |
| Ic catlak | Honeycomb | Ic gerilme asiri artar | Yavas cizelge, kosullama |
| Canak carpilmasi | Cup | Tangential-radial burzulme farki | Dogru istifleme, agirlik |
| Yay carpilmasi | Bow | Uzunlamasina nem gradyani | Uniform hava akisi |
| Burma | Twist | Lif acisi (spiral grain) | Yavas kurutma, agirlik |
| Kabuk sertlesmesi | Case hardening | Dis hizli, ic yavas kuruma | Son kosullama adimi |

## Benchmarklar

### Kurutma Teknolojisi Bazli Karsilastirma

| Parametre | Geleneksel Firin | Isi Pompali Firin | Vakum Firin | Gunes Firini |
|-----------|-----------------|-------------------|-------------|--------------|
| SEC (kJ/kg su) | 2.500 - 5.000 | 800 - 1.500 | 1.500 - 3.000 | Cok dusuk (fan) |
| SMER (kg/kWh) | 0.5 - 1.0 | 1.5 - 4.0 | 0.8 - 1.5 | Degisken |
| Exergy verimi (%) | 4 - 8 | 15 - 30 | 8 - 15 | Degisken |
| Kusur orani (%) | 3 - 8 | 1 - 3 | 1 - 4 | 2 - 6 |
| Enerji maliyeti (EUR/m3) | 40 - 80 | 15 - 35 | 30 - 70 | 5 - 15 |

### Performans Seviyeleri

| Parametre | Dusuk | Tipik | Iyi | En Iyi Uygulama |
|-----------|-------|-------|-----|-----------------|
| Enerji tuketimi (kWh/m3) | > 1.500 | 800 - 1.500 | 400 - 800 | < 400 (HP) |
| SMER (kg/kWh) | < 0.6 | 0.6 - 1.0 | 1.0 - 2.0 | > 2.0 (HP) |
| Exergy verimi (%) | < 5 | 5 - 8 | 8 - 20 | > 20 (HP) |
| Kusur orani (%) | > 8 | 3 - 8 | 1 - 3 | < 1 |
| Kurutma suresi (25 mm cam) | > 10 gun | 5 - 10 gun | 3 - 5 gun | < 3 gun (vakum) |

## Iyilestirme Firsatlari

### 1. Isi Pompasi Retrofiti (Heat Pump Retrofit)

Geleneksel firinlar icin en etkili iyilestirmedir. Mevcut firina isi pompasi unitesi eklenerek kapali devre kurutma saglanir.

| Parametre | Geleneksel | Isi Pompali | Iyilesme |
|-----------|------------|-------------|----------|
| SMER (kg/kWh) | 0.5 - 1.0 | 1.5 - 4.0 | 3-4 kat |
| Enerji tuketimi (kWh/m3) | 800 - 1.500 | 250 - 600 | %50-70 azalma |
| Exergy verimi (%) | 4 - 8 | 15 - 30 | 3-4 kat |
| Kusur orani (%) | 3 - 8 | 1 - 3 | %50-70 azalma |
| CO2 emisyonu | Yuksek | Dusuk | %60-80 azalma |

- Yatirim: 60.000 - 200.000 EUR (50 m3 kapasite firina)
- Yillik enerji tasarrufu: 20.000 - 60.000 EUR
- Geri donus suresi: 2 - 4 yil

### 2. Gunes Enerjisi On Isitma (Solar Preheating)

Gunes kolektorleri veya sera tarzinda on isitma bolumu ile firina giren havanin sicakliginin yukseltilmesi.

- Enerji tasarrufu: %20-40
- Yatirim: 15.000 - 50.000 EUR
- Geri donus suresi: 3 - 6 yil
- Hibrit yaklasim (gunes + isi pompasi) en yuksek verimi saglar

### 3. Firin Yalitim Iyilestirmesi (Insulation Improvement)

Eski firinlarda yetersiz yalitim ciddi isi kayiplarina neden olur. Duvar, tavan ve kapi yalitiminin iyilestirilmesi:

- Mevcut: 50-75 mm mineral yun (tipik eski firin)
- Hedef: 100-150 mm mineral yun veya PIR panel
- Enerji tasarrufu: %10-20
- Hava sizinti (air leakage) onarimi ek %5-10 tasarruf saglar
- Yatirim: 10.000 - 30.000 EUR
- Geri donus suresi: 1 - 2 yil

### 4. Kurutma Cizelgesi Optimizasyonu (Schedule Optimization)

Agac turu, kalinlik ve nem icerigine ozel optimize edilmis cizelgeler:

- Kurutma suresinde %10-30 kisalma
- Enerji tasarrufu: %5-15
- Kusur oraninda %20-50 azalma
- Yatirim: 5.000 - 20.000 EUR (kontrol sistemi + sensor)

### 5. Biyokutle Isitma (Biomass Heating)

Kereste fabrikasindaki odun artiklari (talas, kabuk, kirpinti) ile isi uretimi:

- Yakit maliyeti: 0 - 15 EUR/MWh (kendi artigi kullanildiginda)
- Dogal gaz veya LPG ikamesi ile onemli maliyet dususu
- Karbon notruluk avantaji
- Yatirim (biyokutle kazani): 50.000 - 200.000 EUR
- Geri donus suresi: 2 - 5 yil

### 6. Egzoz Isi Geri Kazanimi (Exhaust Heat Recovery)

Geleneksel firinlarda egzoz havasinin isi iceriginin geri kazanilmasi:

- Hava-hava isi degistirici ile giris havasi on isitma
- Tipik resirkulasyon orani: %60-80
- Enerji tasarrufu: %10-20
- Yatirim: 5.000 - 15.000 EUR
- Geri donus suresi: 0.5 - 1.5 yil

## Turkiye Kereste Sektoru

Turkiye, ormancilik urunleri ve mobilya sektoru acisindan onemli bir uretim ulkesidir.

### Sektorel Profil

- **Orman varligi:** ~22.7 milyon hektar orman alani (%29 ormanlik oran)
- **Yillik endstriyel odun uretimi:** ~20-25 milyon m3
- **Mobilya ihracati:** Turkiye, Avrupa'nin en buyuk mobilya ureticileri arasindadir
- **Mobilya uretim merkezleri:** Inegol (Bursa), Ankara (Siteler), Kayseri, Istanbul
- **Kereste kurutma ihtiyaci:** Mobilya sektorunun buyumesiyle paralel artmaktadir

### Turkiye'ye Ozel Firsatlar

1. **Gunes enerjisi potansiyeli:** Turkiye'nin yuksek gunes isinimi (ozellikle Guney ve Ic Anadolu), gunes enerjili ve hibrit kurutma sistemlerini ekonomik kilar
2. **Biyokutle erisimi:** Mobilya uretim bolgelerinde odun artigi (talas, toz, kirpinti) bol miktarda mevcuttur
3. **Isi pompasi firsati:** Elektrik fiyatlarinin dogal gaz fiyatlarina gore avantajli oldugu durumlerde isi pompali kurutma ekonomik getiri saglar
4. **Kalite artisi:** Mobilya ihracatinda rekabet gucu icin kurutma kalitesinin yukseltilmesi (dusuk nem farki, dusuk kusur) stratejik oneme sahiptir

### Exergy Analizi Ipuclari (Kereste Sektoru Ozel)

1. **Dusuk sicaklik avantaji:** Kereste kurutma 40-90 C gerektirdigi icin, isi pompali sistemler mukemmel exergy uyumu saglar. COP degeri 3-4 olan bir isi pompasi, exergy verimini 3-4 kat arttirir.

2. **Uzun sure etkisi:** Gunlerce suren kurutma donguleri nedeniyle firinin termal kutlesi (thermal mass) ve yalitim kalitesi buyuk onem tasir. Batch degisimlerinde termal kayiplar onemli exergy kaybina neden olur.

3. **Biyokutle exergy uyumsuzlugu:** Odun artiklariyla calisan kazanda, biyokutlenin kimyasal exergy'si (~18 MJ/kg kuru odun) yuksek sicaklikli yanma gazlarina (>1.000 C) donusur, ancak kurutma icin yalnizca 40-90 C gerekir — bu devasa exergy yikimi (exergy destruction) olusturur. Isi pompasi bu sorunu ortadan kaldirir.

4. **Cross-equipment firsati:** Kereste fabrikasinda kompressor atik isisi (40-60 C), firinin on isitma veya kosullama adimi icin idealdir. Kazan egzoz gazlarinin (150-250 C) ekonomizer ile geri kazanimi, kazan besleme suyu on isitmada kullanilabilir.

5. **Vakum kurutma exergy'si:** Vakum kurutmada elektrik enerjisi (yuksek exergy kalitesi) kullanilir. Dusuk sicaklikta buharlastrma saglansa da vakum pompasi enerji tuketimi yuksektir, bu nedenle toplam exergy tuketimi geleneksel firina yakin olabilir. Temel avantaji sure kisalmasidir.

## İlgili Dosyalar

- `knowledge/dryer/formulas.md` — Kurutma hesaplama formulleri (SEC, SMER, exergy verimi)
- `knowledge/dryer/benchmarks.md` — Genel kurutucu benchmark degerleri
- `knowledge/dryer/equipment/tunnel_dryer.md` — Tunel kurutucu detaylari
- `knowledge/dryer/equipment/heat_pump_dryer.md` — Isi pompali kurutucu detaylari
- `knowledge/dryer/solutions/heat_pump_retrofit.md` — Isi pompasi retrofit rehberi
- `knowledge/dryer/solutions/solar_preheating.md` — Gunes enerjisi on isitma cozumu
- `knowledge/dryer/solutions/exhaust_heat_recovery.md` — Egzoz isi geri kazanim cozumu

## Referanslar

1. Simpson, W.T. (1991). *Dry Kiln Operator's Manual*, USDA Forest Service, Agriculture Handbook AH-188.
2. Simpson, W.T. (1998). *Drying and Control of Moisture Content and Dimensional Changes*, USDA Forest Products Laboratory, FPL-GTR-113.
3. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press.
4. Ananias, R.A. et al. (2012). "Energy consumption in industrial drying of radiata pine," *Drying Technology*, 30(7), 774-783.
5. EU BREF (2010). *Best Available Techniques Reference Document for the Wood-Based Panels Production*, European Commission.
6. Langrish, T.A.G. & Walker, J.C.F. (2006). "Drying of Timber," in *Primary Wood Processing*, 2nd Edition, Springer.
7. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
8. Kemp, I.C. (2012). "Fundamentals of Energy Analysis of Dryers," in *Modern Drying Technology*, Vol. 4, Wiley.
9. EN 14298:2004 — Sawn timber: Assessment of drying quality.
