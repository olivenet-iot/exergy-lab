---
title: "Besleme Suyu Aritma --- Feedwater Treatment"
category: solutions
equipment_type: boiler
keywords: [besleme suyu, arıtma, kazan, kireç]
related_files: [boiler/solutions/blowdown_recovery.md, boiler/benchmarks.md, boiler/audit.md]
use_when: ["Besleme suyu arıtma önerisi değerlendirilirken", "Kazan su kalitesi iyileştirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Besleme Suyu Aritma --- Feedwater Treatment

> Son guncelleme: 2026-01-31

## Ozet

**Problem:** Dusuk kaliteli besleme suyu kazanlarda kirec (scale) olusumu, korozyon, artan blowdown ihtiyaci ve boru arizalarina neden olur. 1 mm kirec tabakasi bile ~%2 verim kaybina yol acar. Cozunmus oksijen boru korozyonuna, yuksek TDS ise kopurme/tasima (carryover) ve asiri blowdown'a sebep olur.

**Cozum:** Kapsamli besleme suyu aritma programi (yumusatma, deaerasyon, kimyasal dozlama, pH kontrolu) ile su kalitesini kazan gereksinimlerine uygun hale getirmek.

**Tipik Tasarruf:** %2-5 (dolayli -- azalan blowdown, azalan bakim, artan isi transferi verimi)
**Tipik ROI:** 1-2 yil

## Calisma Prensibi

Kazan besleme suyundaki safsiziliklar dort temel mekanizma ile verim kaybi ve ekipman hasarina yol acar:

### 1. Sertlik (Hardness) -- Kirec Olusumu
- Kalsiyum (Ca++) ve magnezyum (Mg++) iyonlari yuksek sicaklikta cozunurluklerini kaybeder
- CaCO3 ve CaSO4 olarak isi transfer yuzeylerinde cokelir (scale/kirec)
- Kirec tabakasi isi gecis direnci olusturur (kirec iletkenlik ~1-3 W/mK vs celik ~50 W/mK)
- Baca gazi sicakligi artar, verim duser
- Asiri kirec birikimi boru tikanikligina ve lokal asiri isinmaya neden olabilir

### 2. Kirec Kalinligi vs Enerji Kaybi
- 1 mm kirec tabakasi yaklasik %2 verim kaybina esittir
- Bu kayip baca gazi sicakliginda ~15-20 C artisa karsilik gelir
- Kirec kalinligi arttikca kayip ustel olarak buyur (asagida tablo)

### 3. Cozunmus Oksijen -- Korozyon
- Suda cozunmus O2 celik yuzeylerle reaksiyona girer (pitting corrosion)
- Oksijen korozyonu en yaygin kazan boru ariza nedenidir
- Ozellikle besleme suyu sicakligi 60-100 C arasindayken korozyon hizi maksimumdur
- Hedef: <7 ppb O2 (deaerator cikisinda)

### 4. Toplam Cozunmus Katilar (TDS)
- Yuksek TDS kopurme (foaming) ve buhar ile su tasinmasina (carryover) neden olur
- Carryover buhar kalitesini dusurur, buhar hatti ve turbinlere zarar verir
- TDS kontrolu icin blowdown yapilir; yuksek TDS = yuksek blowdown = enerji kaybi
- Blowdown her %1 artista yaklasik %0.2 verim kaybi demektir

### 5. pH Kontrolu
- Kazan suyu pH'i 10.5-11.5 arasinda tutulmalidir
- Dusuk pH (<9): Asit korozyonu hizlanir
- Yuksek pH (>12): Kostik kirilganlik (caustic embrittlement), SCC riski
- Besleme suyu pH'i 8.5-9.5 arasinda olmalidir
- pH kontrolu genellikle fosfat programi veya koordineli fosfat/NaOH dozlamasiyla saglanir

## Su Kalitesi Parametreleri

### Besleme Suyu ve Kazan Suyu Limitleri (Orta Basinc: 10-25 bar)

| Parametre | Birim | Besleme Suyu Limiti | Kazan Suyu Limiti |
|-----------|-------|--------------------|--------------------|
| Toplam Sertlik (TH) | ppm CaCO3 | < 2 | < 1 |
| Toplam Cozunmus Katilar (TDS) | ppm | < 300 | < 2,500 (10 bar), < 1,500 (25 bar) |
| pH | -- | 8.5-9.5 | 10.5-11.5 |
| Cozunmus Oksijen (O2) | ppb | < 7 (deaerator cikisi) | -- |
| Demir (Fe) | ppm | < 0.05 | < 1 |
| Bakir (Cu) | ppm | < 0.01 | -- |
| Silika (SiO2) | ppm | < 5 | < 150 (10 bar), < 20 (25 bar) |
| Alkalinite (M) | ppm CaCO3 | -- | < 700 |
| Iletkenlik | uS/cm | < 450 | < 3,500 |
| Yag / Gres | ppm | < 1 | 0 |

**Not:** Basinc arttikca su kalitesi limitleri sertlesir. Yuksek basincli kazanlar (>40 bar) demineralize su gerektirir.

## Aritma Yontemleri

### 1. Yumusatma (Softening) -- Iyon Degisimi

- Resin yatak uzerinden Ca++ ve Mg++ iyonlari Na+ ile degistirilir
- Cikis sertligi: < 1 ppm (tipik < 0.5 ppm)
- Rejenere edici: NaCl (tuz) cozeltisi
- TDS'yi degistirmez, sadece sertligi giderir
- En yaygin ve ekonomik on-aritma yontemi
- Kapasite: Tipik olarak 50-100 m3/rejenasyon (resin hacmine bagli)

### 2. Ters Ozmoz (Reverse Osmosis -- RO)

- Yari gecirgen membran ile iyonlarin %95-99'u giderilir
- TDS, sertlik, silika dahil hemen tum safsiziliklar azaltilir
- Geri kazanim orani: %50-75 (kayip su: reject/konsantre)
- Yuksek basincli kazanlar ve yuksek TDS sehir sularinda tercih edilir
- On-aritma (yumusatma + antiscalant) genellikle gereklidir
- RO sonrasi genellikle deaeration + pH ayar gerekir

### 3. Deaerasyon (Hava/Oksijen Giderimi)

#### Termal Deaerator
- Henry Yasasi: Cozunmus gaz konsantrasyonu sicaklikla azalir
- Su kaynama noktasina yaklastikca O2 cozunurlugu sifira yaklasir
- Deaerator suyu 105 C'ye (0.2 bar gauge buhar) isitarak O2'yi giderir
- Cikis O2: < 7 ppb (termal deaerator garantisi)
- Ayni zamanda besleme suyunu on-isitir (verim artisi)

#### Deaerator Tipleri

| Tip | Calisma Prensibi | Kapasite | O2 Cikisi | Avantaj |
|-----|-----------------|----------|-----------|---------|
| Spray (Puskurtme) | Suyu ince damlaciklar halinde buharla temas ettirir | Kucuk-orta | < 7 ppb | Kompakt, ucuz |
| Tray (Tepsi) | Su tepsi serileri uzerinden buharla karsi akimli temas | Orta-buyuk | < 7 ppb | Yuksek kapasite, daha stabil |
| Vakum Deaerator | Vakum altinda dusuk sicaklikta gaz giderimi | Kucuk | < 20 ppb | Buhar gerektirmez |

#### Deaerator Ek Faydalari
- Besleme suyunu ~105 C'ye on-isitir (kazan verimini arttirir)
- Buhar kondensati donusu icin toplama deposu gorevi gorur
- Termal sok riskini azaltir (kazan beslemesi sabit sicaklikta)

### 4. Kimyasal Aritma

| Kimyasal | Amac | Dozlama Noktasi | Tipik Doz |
|----------|------|-----------------|-----------|
| Sodyum sulfit (Na2SO3) | Oksijen tutucu (scavenger) | Deaerator sonrasi / besleme tanki | 8 ppm / 1 ppm O2 |
| Hidrazin (N2H4) | Oksijen tutucu (yuksek basinc) | Besleme suyu hatti | 1:1 mol O2 |
| DEHA (dietil hidroksilamin) | Oksijen tutucu (ucar) | Besleme suyu hatti | 1-3 ppm |
| Trisodyum fosfat (Na3PO4) | Sertlik kontrolu (kazan icinde) | Kazan suyu | 20-50 ppm PO4 |
| Polimer dispersant | Camur dagitici | Kazan suyu | 10-30 ppm |
| NaOH / Kostik | pH kontrolu | Kazan suyu | pH'a gore |
| Amonyak / Morfollin | Kondensat hatti pH kontrolu | Buhar hatti / kondensat | pH 8.5-9.0 |
| Antiscalant | RO membran koruma | RO oncesi | Uretici tavsiyesi |

## Kirec/Kabuk Etkisi -- Verim Kaybi Tablosu

| Kirec Kalinligi (mm) | Yaklasik Verim Kaybi (%) | Yakit Israfi (%) | Baca Gazi Sicaklik Artisi (C) |
|----------------------|--------------------------|------------------|-------------------------------|
| 0.5 | ~1 | ~1 | ~8-10 |
| 1.0 | ~2 | ~2 | ~15-20 |
| 1.5 | ~3 | ~3 | ~22-28 |
| 2.0 | ~4 | ~4 | ~30-35 |
| 3.0 | ~7 | ~7 | ~50-55 |
| 5.0 | ~12 | ~12 | ~80-90 |
| 6.0+ | >15 | >15 | >100 (tehlikeli) |

**Not:** 3 mm uzerinde kirec birikimi lokal asiri isinma ve boru deformasyonuna (bagging) neden olabilir. Bu durum acil kimyasal temizlik (acid cleaning) gerektirir.

## Blowdown Orani ile Iliski

### Blowdown Neden Gereklidir
- Buhar uretimi saf su alir, safsiziliklar kazan suyunda konsantre olur
- TDS limiti asilmamasi icin duzgun araliklarla blowdown yapilmalidir
- Her blowdown ile sicak su (ve enerji) kaybi olusur

### Blowdown Orani Formulu
```
Blowdown% = (TDS_besleme / (TDS_kazan_max - TDS_besleme)) x 100

veya

Cycles_of_concentration (N) = TDS_kazan / TDS_besleme
Blowdown% = 1 / N x 100 = Besleme_debisi / N
```

### Ornek
- Besleme suyu TDS: 200 ppm (yumusatilmis sehir suyu)
- Kazan max TDS: 2,500 ppm
- N = 2,500 / 200 = 12.5 cevrim
- Blowdown = 1/12.5 = %8

RO ile aritilmis su kullanirsak:
- Besleme suyu TDS: 20 ppm
- N = 2,500 / 20 = 125 cevrim
- Blowdown = 1/125 = %0.8

**Sonuc:** Iyi aritma ile blowdown %8'den %0.8'e dusurulabilir. Bu dogrudan enerji tasarrufu saglar.

### Blowdown Enerji Kaybi
```
Q_blowdown = m_blowdown x Cp x (T_kazan - T_makyaj)
            = Buhar_uretimi x (Blowdown%/100) x 4.18 x (T_kazan - T_makyaj)  [kJ/saat]
```

## Uygulanabilirlik Kriterleri

### Su Aritma Ne Zaman Onceliklidir
- Mevcut sertlik > 5 ppm (acil yumusatma gerekli)
- Blowdown orani > %5 (TDS cok yuksek, aritma iyilestirilebilir)
- Kirec birikimi gorsel olarak tespit ediliyorsa
- Boru arizalari tekrarlaniyorsa (korozyon suplesi)
- Kondensat donusu < %50 (makyaj suyu orani yuksek)
- Buhar kalitesinde dusus (carryover belirtileri)

### Su Aritma Gereksiz/Dusuk Oncelikli Oldugu Durumlar
- Zaten demineralize su kullaniliyor ve blowdown < %2
- Kondensatin %80+'si donuyorsa ve su kalitesi iyi
- Cok kucuk kazanlar (< 200 kW) -- maliyet/fayda dengesizligi

## Yatirim Maliyeti

| Ekipman | Kapasite | Maliyet Araligi (EUR) | Kullanim Omru |
|---------|----------|----------------------|---------------|
| Otomatik yumusatici (duplex) | 5-20 m3/saat | 5,000-15,000 | 10-15 yil (resin: 3-5 yil) |
| RO sistemi | 1-5 m3/saat | 15,000-50,000 | 15-20 yil (membran: 3-5 yil) |
| RO sistemi | 5-20 m3/saat | 40,000-120,000 | 15-20 yil (membran: 3-5 yil) |
| Termal deaerator (spray tip) | 5-20 ton/saat | 25,000-60,000 | 20-30 yil |
| Termal deaerator (tray tip) | 20-100 ton/saat | 50,000-150,000 | 20-30 yil |
| Kimyasal dozlama sistemi | -- | 3,000-10,000 | 10-15 yil |
| Blowdown isi geri kazanimi | 1-10 ton/saat | 5,000-20,000 | 15-20 yil |
| Su analiz cihazlari (online) | -- | 5,000-15,000 | 7-10 yil |

### Isletme Maliyetleri (Yillik)

| Kalem | Tipik Yillik Maliyet (EUR) |
|-------|---------------------------|
| Yumusatici tuz (NaCl) | 500-2,000 |
| RO membran degisimi (yillik ortama) | 2,000-8,000 |
| Kimyasal dozlama (oksijen tutucu, fosfat, vb.) | 3,000-15,000 |
| Su analiz ve laboratuvar | 1,000-3,000 |
| Bakim ve iscilik | 2,000-5,000 |

## ROI Hesabi

### Formul
```
Yillik_tasarruf = Yakit_tasarrufu + Blowdown_azaltma_tasarrufu + Bakim_maliyet_azalma

Yakit_tasarrufu = Yakit_tuketimi x Verim_artisi% / 100 x Yakit_fiyati
Blowdown_tasarrufu = Buhar_uretimi x (Blowdown_eski% - Blowdown_yeni%) / 100 x Buhar_maliyeti
Bakim_azalma = Yillik_bakim_maliyeti x Azalma_orani

Geri_odeme_yil = (Yatirim + Kurulum) / (Yillik_tasarruf - Yillik_isletme_maliyeti)
```

### Ornek Hesap
Tesis: 10 ton/saat buhar kazani, dogalgaz, 6,000 saat/yil

**Mevcut durum:**
- Besleme suyu sertligi: 50 ppm (aritma yok)
- Kirec birikimi: ~2 mm/yil
- Verim kaybi: ~%4
- Blowdown: %12 (yuksek TDS)
- Yillik yakit tuketimi: 600,000 m3 dogalgaz (EUR 0.40/m3 = EUR 240,000/yil)

**Aritma sonrasi:**
- Sertlik: < 1 ppm (yumusatici)
- Kirec: ihmal edilebilir
- Verim kaybi: ~%0
- Blowdown: %4 (kontrol altinda TDS)

**Tasarruf hesabi:**
- Yakit tasarrufu: EUR 240,000 x %4 / 100 = EUR 9,600/yil
- Blowdown tasarrufu: (%12 - %4) = %8 azalma, ~EUR 5,000/yil
- Bakim tasarrufu (kimyasal temizlik, boru degisimi): ~EUR 3,000/yil
- **Toplam tasarruf: EUR 17,600/yil**

**Yatirim:**
- Duplex yumusatici: EUR 12,000
- Kimyasal dozlama: EUR 6,000
- Blowdown isi geri kazanim: EUR 8,000
- Online izleme: EUR 7,000
- Kurulum: EUR 7,000
- **Toplam yatirim: EUR 40,000**

**Yillik isletme maliyeti: EUR 6,000** (tuz + kimyasal + bakim)

**Geri odeme: EUR 40,000 / (EUR 17,600 - EUR 6,000) = 3.4 yil**

**Not:** Deaerator da eklenirse (ek EUR 40,000 yatirim) korozyon kayiplarinin azalmasi ile toplam ROI 2-3 yila dusebilir; bu hesap tesise ozel degerlendirilmelidir.

## Uygulama Adimlari

1. **Su analizi:** Mevcut besleme suyu, kazan suyu ve kondensat numunelerini kapsamli analiz ettirin
2. **Durum tespiti:** Kazanin ic yuzeylerini, boruları ve kirec durumunu inceleyin
3. **Hedef belirleme:** Kazan basinci ve tipine gore su kalitesi hedeflerini tanimlayin
4. **Sistem tasarimi:** Yumusatici, RO, deaerator ve kimyasal dozlama kombinasyonunu belirleyin
5. **Ekipman temini:** Yetkili tedarikci ile kapasite boyutlandirmasi ve teknik sartname hazirlama
6. **Kurulum:** Mekanik ve elektrik baglantilari, boru hatti modifikasyonlari
7. **Kimyasal temizlik:** Kurulum oncesi mevcut kireci asit yikama (acid cleaning) ile giderin
8. **Devreye alma:** Su kalitesi parametrelerini olcum ve dozlama ayarlari
9. **Egitim:** Operatorlere su analizi, kimyasal dozlama ve izleme egitimi verin
10. **Izleme programi:** Gunluk/haftalik analiz rutinlerini ve online izleme sistemini baslatın
11. **Dogrulama:** 3 ay sonra verim testleri ile tasarrufu dogrulayin

## Riskler ve Dikkat Edilecekler

| Risk | Aciklama | Onlem |
|------|----------|-------|
| Asiri kimyasal dozlama | Gereksiz maliyet; alkalinite asimi kostik kirilganliga neden olabilir | Online izleme, duzenli analiz, otomatik dozlama |
| Yetersiz aritma | Kirec ve korozyon devam eder | Minimum haftalik analiz, alarm limitleri |
| Kimyasal maliyetleri | Isletme butcesini asabilir | Dozlama optimizasyonu, kondensat donusu artirma |
| Deaerator ariza | O2 artisi, ani korozyon hizlanmasi | Yedek kimyasal O2 tutucu, alarm sistemi |
| Resin/membran bitimleri | Sertlik kacagi, TDS artisi | Sertlik alarmı, otomatik yedek gecis (duplex) |
| Blowdown otomasyonu ariza | TDS kontrolsuz yukselebilir | Manuel blowdown proseduru yedek |
| Silika birikimi | Ozellikle yuksek basincli kazanlarda | RO veya demineralizasyon, silika izleme |
| Kondensat kontaminasyonu | Proses kaynakli kirlilik kazan suyuna karismasi | Kondensat kalite izleme, otomatik divert |

## Ilgili Dosyalar
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Buhar kazani (firetube): `equipment/boiler_steam_firetube.md`
- Buhar kazani (watertube): `equipment/boiler_steam_watertube.md`
- Kazan yakitlari: `equipment/boiler_fuels.md`
- Exergy formulleri: `formulas/boiler_exergy.md`
- Yoğuşmali kazan: `equipment/boiler_condensing.md`

## Referanslar
- ASME, "Consensus on Operating Practices for the Control of Feedwater and Boiler Water Chemistry in Modern Industrial Boilers"
- ABMA (American Boiler Manufacturers Association), "Boiler Water Quality Requirements and Associated Steam Quality for Industrial Boilers"
- DOE/AMO, "Improve Your Boiler's Combustion Efficiency" -- Tip Sheet #4 (Feedwater section)
- Spirax Sarco, "The Steam and Condensate Loop" -- Chapter 3: The Boiler House (Water Treatment)
- Cleaver-Brooks, "Boiler Water Treatment" Technical Reference
- BG01 -- BS 2486: "Treatment of Water for Steam Boilers and Water Heaters"
- VdTUV, Merkblatt Wasserchemie (Alman kazan suyu kalite standartlari)
- ASME PTC 4, "Fired Steam Generators" -- Performance Test Code
