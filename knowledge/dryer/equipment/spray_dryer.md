---
title: "Sprey Kurutucu (Spray Dryer)"
category: dryer
equipment_type: dryer
keywords:
  - sprey kurutucu
  - spray dryer
  - atomizasyon
  - sıvı kurutma
  - toz üretimi
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/air_recirculation.md
  - dryer/sectors/food_drying.md
use_when:
  - "Sprey kurutucu analiz edilirken"
  - "Sıvı ürün kurutma değerlendirilirken"
priority: medium
last_updated: 2026-02-01
---

# Sprey Kurutucu (Spray Dryer)

## Genel Bakis

Sprey kurutucu (spray dryer), sivi veya bulamac (slurry) formundaki beslemeyi sicak hava ortamina
atomize ederek son derece hizli buharlasmaya dayanan konvektif bir kurutma sistemidir. Atomizasyon
yoluyla olusturulan cok kucuk damlaciklardan (10-200 um) nem, saniyeler icinde uzaklastirilir ve
kuru toz urun elde edilir. Gida, ilac, kimya ve seramik sektorlerinde yaygin olarak kullanilandir.

Sprey kurutucunun en belirgin termik ozelligi, cok yuksek giris havasi sicakligi (150-300 degC) ile
nispeten dusuk cikis havasi sicakliginin (70-100 degC) bir arada bulunmasidir. Bu buyuk sicaklik
farki, kurutma islevi icin gerekli olmakla birlikte, kacinilmaz olarak yuksek exergy yikimine yol
acar. Sonuc olarak sprey kurutucular, tum endustriyel kurutucu tipleri arasinda en dusuk exergy
verimine (%4-10) sahip ekipmanlardir.

| Parametre | Deger |
|-----------|-------|
| Tip | Konvektif (convective) — sicak hava ile atomize sivi besleme temasi |
| Kapasite | 50 - 50.000 kg su buharlastirma/h |
| Giris havasi sicakligi | 150 - 300 degC |
| Cikis havasi sicakligi | 70 - 100 degC |
| Urun nem icerigi | %2-5 (tipik cikis) |
| Kalma suresi | 5-30 saniye |
| Exergy verimi | %4-10 (yapisal olarak dusuk) |
| SMER | 0.3 - 0.7 kg/kWh (tipik) |
| SEC | 3.500 - 8.000 kJ/kg su buharlastirma |
| Hava hacimleri | 5.000 - 500.000 m3/h (cok buyuk) |

## Calisma Prensibi

Sprey kurutma islemi, sivi beslemenin atomizasyon ile cok kucuk damlaciklarara ayrilmasi ve bu
damlaciklararin buyuk hacimli sicak hava akimi ile temas ettirilmesine dayanir. Yuksek yuzey
alani/hacim orani sayesinde kucuk damlaciklardaki nem son derece hizli buhaslasir.

### Proses Adimlari

1. **Besleme hazirlama:** Sivi besleme filtrelenir ve genellikle on konsantrasyon (evaporator) ile
   kati madde orani %30-60 arasina cikarilir. Daha yuksek konsantrasyon, buharlastirilacak su
   miktarini azaltir ve enerji tuketimini dogrudan dusurur.
2. **Hava isitma:** Ortam havasi, buhar isitici (steam heater), dogalgaz yakici (direct/indirect
   gas burner) veya elektrikli isitici ile 150-300 degC'ye isitilir. Giris sicakligi, urun
   hassasiyetine gore belirlenir.
3. **Atomizasyon:** Besleme, atomizor araciligiyla kurutma odasina puskurtulur. Damlacik boyutu
   tipik olarak 10-200 um araligindadir.
4. **Kurutma:** Damlaciklar sicak hava ile temas eder ve nem saniyeler icinde buhaslasir. Kurutma
   odasi cok buyuk boyutludur (cap: 3-15 m, yukseklik: 5-25 m).
5. **Urun toplama:** Kuru toz, kurutma odasi tabanindan ve/veya siklon (cyclone) separatorlerle
   toplanir. Ince tozlar torba filtre (bag filter) ile yakalanir.
6. **Egzoz havasi atimi:** Nemli ve hala sicak olan egzoz havasi (70-100 degC) sisteme atilir.
   Bu, en buyuk enerji ve exergy kaybi noktasidir.

### Hava Akis Konfigurasyonlari

| Konfigrasyon | Aciklama | Uygulama | Exergy Etkisi |
|--------------|----------|----------|---------------|
| Esyonlu (co-current) | Sicak hava ve besleme ayni yonde | Isiya duyarli urunler (sut, ilac) | En yaygin; urun dusuk T'de kalir |
| Ters yonlu (counter-current) | Sicak hava ve besleme zit yonde | Isiya dayanikli urunler (deterjan, seramik) | Daha dusuk egzoz T, daha iyi exergy |
| Karisik akis (mixed flow) | Her iki yonun kombinasyonu | Ozel uygulamalar | Orta performans |

Esyonlu konfigurasyonda urun sicak hava girisine yakin atomize edilir ve cikisa dogru hava ile
birlikte hareket eder. Urun en sicak havaya islak haldeyken maruz kalir, bu nedenle isiya duyarli
malzemeler icin uygundur. Ancak egzoz havasi nispeten sicak cikar, bu da exergy kaybini arttirir.

Ters yonlu konfigurasyonda kuru urun en sicak hava ile temas eder. Cikis havasi daha soguk
olabilir, bu da daha dusuk egzoz kaybi anlamina gelir. Ancak isiya duyarli urunlerde bozulma
riski vardir.

## Atomizer Tipleri

Atomizor secimi, urun kalitesi, kapasite ve enerji verimi uzerinde dogrudan etkilidir.

| Atomizasyon Yontemi | Damlacik Boyutu (um) | Kapasite Araligi | Avantaj | Dezavantaj |
|---------------------|----------------------|------------------|---------|-----------|
| Doner diskli (rotary atomizer) | 30-120 | Yuksek (>5.000 L/h) | Genis kapasite araligi, kararli isletme, degisken vizkoziteye tolerans | Mekanik asinma, yuksek bakim maliyeti, buyuk oda gerektirir |
| Basinc nozulu (pressure nozzle) | 50-200 | Orta (500-10.000 L/h) | Basit yapi, dusuk ilk yatirim, kompakt oda | Tiklanma riski, dar kapasite araligi, asinmaya duyarli |
| Iki akiskanli nozul (two-fluid nozzle) | 10-80 | Dusuk-orta (50-2.000 L/h) | Cok ince toz, iyi kontrol, dusuk basinc | Yuksek basinli hava gerekli (ek enerji), sinirli kapasite |
| Ultrasonik nozul | 10-50 | Dusuk (<500 L/h) | En ince toz, dusuk enerji tuketimi, hassas kontrol | Sinirli kapasite, yuksek yatirim, endustriyel olcege sinirli uygulanabilirlik |

**Doner diskli atomizor** endustriyel olcekte en yaygin kullanilan tiptir. Disk, 10.000-30.000
dev/dak hizda doner ve sivi beslemeyi ince damlaciklarara ayirir. Genis vizkozite araliginda
(1-500 mPa.s) calisabilir. Dezavantaji, buyuk kurutma odasi gerektirmesi ve mekanik bakim
maliyetidir.

**Basinc nozulu** sivi beslemeyi 50-300 bar basincta kucuk bir orifisten gecirir. Daha kompakt
kurutma odasi mumkundur ancak tiklanmaya karsi hassas oldugu icin beslemenin dikkatli
filtrelenmesi gerekir.

**Iki akiskanli nozul** sivi besleme ile birlikte yuksek basincli hava (2-7 bar) kullanir.
Cok ince toz uretimi icin idealdir ancak basinli hava uretimi ek enerji tuketir (tipik olarak
atomizasyon enerjisini 3-5 kat arttirir).

## Parametreler

### Zorunlu Olcum Parametreleri

| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|-------------|---------------|
| Besleme debisi (feed flow rate) | L/h veya kg/h | 50-50.000 L/h | Kutle debi olcer (Coriolis) |
| Besleme kati madde orani | % | 30-60 | Refraktometre veya kurutma firini |
| Giris havasi sicakligi (inlet air T) | degC | 150-300 | Termokupl (K-tipi) |
| Cikis havasi sicakligi (outlet air T) | degC | 70-100 | Termokupl (K-tipi) |
| Egzoz havasi nem icerigi | g/kg veya %RH | 30-80 g/kg | Nem sensoru (kapasitif) |
| Toplam enerji tuketimi | kW | 100-10.000 | Gaz sayaci + elektrik sayaci |
| Urun nem icerigi (product moisture) | % | 2-5 | Nem tayin cihazi (infrared/halogen) |
| Urun cikis debisi | kg/h | 20-10.000 | Kantar veya konveyor tartim |

### Opsiyonel Parametreler

| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|-------------|---------------|
| Hava debisi (air flow rate) | m3/h | 5.000-500.000 | Pitot tupu veya anemometre |
| Atomizor hizi (rotary) veya basinc (nozzle) | rpm veya bar | 10.000-30.000 rpm / 50-300 bar | Takometre / basinc transmiteri |
| Fan gucu (fan power) | kW | 10-500 | Guc analizoru |
| Ortam sicakligi ve nemi | degC, %RH | 15-40 degC, %30-80 | Hava istasyonu |
| Urun parcacik boyutu | um | 20-200 | Lazer kirinim (laser diffraction) |

### Varsayilan Degerler

Sahada olcum yapilamadigi durumlarda kullanilacak varsayilan degerler:

| Parametre | Varsayilan | Birim | Not |
|-----------|-----------|-------|-----|
| Giris havasi sicakligi | 200 | degC | Gida sektoru ortalamasi |
| Cikis havasi sicakligi | 85 | degC | Orta verimli isletme |
| Besleme kati madde orani | 45 | % | On konsantrasyon sonrasi |
| Urun nem icerigi | 3.5 | % | Tipik toz urun |
| Ortam sicakligi (T0) | 25 | degC | Referans sicakligi |
| Ortam nemi | 50 | %RH | Standart kosullar |
| Radyasyon kaybi | 10 | % | Yalitimsiz tipik sistem |
| Fan verimi | 70 | % | Standart santrifuj fan |
| Atomizor gucu / toplam guc | 5 | % | Tipik oran |
| SMER | 0.5 | kg/kWh | Olcum yoksa ilk tahmin |
| Exergy verimi | 7 | % | Ortalama endustriyel sprey kurutucu |
| Yillik calisma saati | 5.000 | saat/yil | 2 vardiya endustriyel isletme |

## Exergy Analizi

### Neden Bu Kadar Dusuk Exergy Verimi?

Sprey kurutucunun exergy verimi (%4-10), tum endustriyel kurutucu tipleri icinde en dusuk
olanlardan biridir. Bu yapisal bir ozellik olup su nedenlerden kaynaklanir:

1. **Yuksek sicaklik farki (large Delta T):** 150-300 degC giris havasinin exergy icerigi
   yuksektir, ancak kurutma islemi icin kullanilan exergy orani cok dusuktur. Buharlastirma
   buyuk olcude latent isi gerektirir ve bu islem nispeten dusuk sicaklikta gerceklesir.

2. **Cok buyuk hava hacimleri:** Sprey kurutucularda hava/besleme kutle orani 10-30 arasindadir.
   Bu devasa hava akimi, egzoz ile birlikte buyuk miktarda exergy tasinmasina neden olur.

3. **Anlik buharlasma:** Damlaciklarin saniyeler icinde kurumasiyla sicak havanin buyuk bolumu
   urun ile yeterli sureligine temas edemez; hava kurutma odasindan hala yuksek exergy icerigi
   ile cikar.

4. **Yanma geri donusumu yok:** Diger kurutucu tiplerinden farkli olarak, egzoz havasinin geri
   devri nemdeki sinirlamalar nedeniyle cok kisitlidir.

### Exergy Verimi Hesabi

```
psi_spray = Ex_urun / (Ex_hava_giris + W_fan + W_atomizor)

Burada:
  psi_spray     = Exergy verimi (boyutsuz, tipik 0.04-0.10)
  Ex_urun       = Urunun exergysi — nemin uzaklastirilma islevi (kW)
  Ex_hava_giris = Giris havasinin fiziksel exergysi (kW)
  W_fan         = Fan guc tuketimi (kW)
  W_atomizor    = Atomizor guc tuketimi (kW)
```

Giris havasinin exergysi:

```
Ex_hava = m_hava × [Cp × (T - T0 - T0 × ln(T/T0)) + R × T0 × ln(P/P0)]

Burada:
  m_hava = Hava kutle debisi (kg/s) — sprey kurutucularda cok yuksek
  Cp     = Havanin ozgul isisi (~1.005 kJ/kg·K)
  T      = Hava sicakligi (K)
  T0     = Referans (olu durum) sicakligi (K), tipik 298.15 K
  R      = Hava gaz sabiti (0.287 kJ/kg·K)
  P/P0   = Basinc orani (genellikle ~1, ihmal edilebilir)
```

### Exergy Verimi Benchmark

| Seviye | Exergy Verimi (%) | Yorum |
|--------|-------------------|-------|
| Cok dusuk | < 4 | Ciddi sorunlu veya cok eski sistem |
| Dusuk | 4 - 6 | Tipik eski sprey kurutucu, iyilestirme oncelikli |
| Orta | 6 - 8 | Standart endustriyel seviye |
| Iyi | 8 - 10 | Optimize edilmis modern sistem |
| En iyi uygulama | > 10 | Cok asamali sistem + isi geri kazanim + on konsantrasyon |

### Ornek Hesaplama

Tipik bir sut tozu sprey kurutucusu (5.000 kg su buharlastirma/h):

```
Giris: T_giris = 200 degC, T_cikis = 85 degC, m_hava = 150.000 kg/h, T0 = 25 degC
Termal guc: Q_in = 150.000 × 1.005 × (200 - 25) / 3.600 = 7.325 kW
Egzoz kaybi: Q_egz = 150.000 × 1.005 × (85 - 25) / 3.600 = 2.513 kW
Fan gucu: W_fan = 250 kW
Atomizor gucu: W_atom = 75 kW

Ex_giris = 150.000/3.600 × 1.005 × [(473-298) - 298 × ln(473/298)] = 1.185 kW
Ex_cikis = 150.000/3.600 × 1.005 × [(358-298) - 298 × ln(358/298)] = 101 kW
Ex_yikim = 1.185 - 101 + 250 + 75 = 1.409 kW (toplam giris exergy)
Ex_urun ~ 85 kW (nemin uzaklastirilmasi icin minimum is)

psi = 85 / (1.185 + 250 + 75) = 85 / 1.510 = %5.6
```

Bu deger, endustriyel sprey kurutucularin tipik exergy verimi araligindadir.

## Kayip Dagilimi

Sprey kurutucuda exergy kayip dagilimi (tipik endustriyel sistem, dogalgaz isitmali):

| Kayip Kalemi | Oran (%) | Aciklama |
|--------------|----------|----------|
| Egzoz havasi kaybi (exhaust air loss) | 40-55 | En buyuk kayip — yuksek debili sicak ve nemli hava atigi |
| Yanma geri donusumsuzlugu (combustion irreversibility) | 15-25 | Dogalgaz yanmasindaki termodinamik geri donusumsuzluk |
| Isi transferi geri donusumsuzlugu (heat transfer) | 10-15 | Yuksek Delta T nedeniyle hava-damlacik isi transferindeki exergy yikimi |
| Radyasyon ve konveksiyon kaybi | 5-10 | Kurutma odasi ve kanal yuzeylerinden cevreye isi kaybi |
| Karisma ve difuzyon kayiplari (mixing losses) | 3-5 | Farkli sicaklik ve nem duzeyindeki hava akimlarinin karismasi |
| Fan ve atomizor kayiplari | 3-5 | Elektriksel ve mekanik kayiplar |

### Egzoz Havasi Kaybi Detayi

Egzoz havasi kaybi, sprey kurutucunun en buyuk exergy verimsizligi kaynagindir. Iki bilesenden
olusur:

```
Q_egzoz = m_hava × Cp_hava × (T_egzoz - T_ortam) + m_su × h_fg

Burada:
  Q_egzoz  = Egzoz havasi ile kaybolan toplam enerji (kW)
  m_hava   = Hava kutle debisi (kg/s) — sprey kurutucularda cok yuksek (10-150 kg/s)
  Cp_hava  = Havanin ozgul isisi (~1.005 kJ/kg·K)
  T_egzoz  = Egzoz havasi sicakligi (degC) — tipik 70-100 degC
  T_ortam  = Ortam sicakligi (degC)
  m_su     = Buharlasen su debisi (kg/s)
  h_fg     = Suyun buharlasma gizli isisi (~2.260 kJ/kg)
```

Her 10 degC'lik egzoz sicakligi dususu yaklasik %3-5 enerji tasarrufu saglar; ancak cikis havasi
sicakligini dusurmek urun nem icerigini arttirir. Bu denge cok dikkatli yonetilmelidir.

### Yanma Geri Donusumsuzlugu

Dogalgaz veya LPG ile dogrudan isitma kullanan sprey kurutucularda yanma islemi onemli bir
exergy yikimi kaynagindir (%15-25). Yakit kimyasal exergysi, yanma urunlerinin termal exergysine
donusurken termodinamigin 2. yasasi geregi kayip olusur. Bu kayip yapisal olup tamamen ortadan
kaldirilamaz; ancak buhar isitma veya dolayli isitma ile yanma kaybi baska bir ekipmana transfer
edilebilir.

## Avantajlar ve Dezavantajlar

### Avantajlar

- **Cok hizli kurutma:** Saniyeler icinde sivi urun toz formuna donusturulur
- **Homojen urun kalitesi:** Kontrol edilebilir parcacik boyutu (20-200 um)
- **Surekli proses:** Kesikli (batch) degil surekli (continuous) calisma
- **Hassas urunlere uygunluk:** Esyonlu akista urun asla giris sicakligina ulasmaz
- **Genis kapasite araligi:** Laboratuvardan (50 L/h) endustriyel olcege (50.000 L/h)
- **Toz urun ozellikleri:** Ani cozunurluk (instant), dusuk yigin yogunlugu elde edilebilir
- **Otomasyon kolayligi:** Cikis havasi sicakligi ile otomatik kontrol mumkun

### Dezavantajlar

- **Cok dusuk exergy verimi (%4-10):** Tum kurutucu tipleri icinde en dusuk
- **Yuksek ozgul enerji tuketimi:** SEC 3.500-8.000 kJ/kg su — bant veya akiskan yatak
  kurutucularin 1.5-3 kati
- **Cok buyuk hava hacimleri:** 5.000-500.000 m3/h — buyuk fan enerji tuketimi
- **Buyuk ekipman boyutu:** Kurutma odasi cap 3-15 m, yukseklik 5-25 m
- **Yuksek yatirim maliyeti:** Buyuk odalar, siklon, filtre, fan sistemleri
- **Sinirli egzoz geri devri:** Nem artisi nedeniyle kapalI cevrim cok kisitli
- **Toz patlama riski:** Organik tozlar (sut, nisasta) patlayici ortam olusturabilir (ATEX)
- **Yapiskanlik sorunu (stickiness):** Bazi urunlerde oda duvari birikimi

## Uygulamalar

### Gida Sektoru

| Urun | Giris T (degC) | Cikis T (degC) | Kati Madde (%) | Not |
|------|:--------------:|:--------------:|:--------------:|-----|
| Sut tozu (milk powder) | 180-220 | 80-90 | 45-52 | En yaygin uygulama, SMER 0.4-0.6 |
| Kahve (instant coffee) | 200-250 | 90-100 | 40-55 | Aroma korumasi kritik |
| Bebek mamasi (infant formula) | 160-180 | 75-85 | 45-55 | Dusuk T, vitamin korumasi |
| Peynir alti suyu (whey) | 180-200 | 80-90 | 50-60 | Protein denatasyonu riski |
| Meyve suyu tozu | 140-160 | 70-80 | 30-40 | Yapiskanlik sorunu, maltodekstrin takviyesi |

### Kimya ve Deterjan Sektoru

| Urun | Giris T (degC) | Cikis T (degC) | Not |
|------|:--------------:|:--------------:|-----|
| Deterjan tozu (detergent) | 250-300 | 90-100 | Yuksek T toleransi, ters yonlu akis |
| Seramik granul (ceramic) | 250-300 | 90-110 | Yuksek yogunluk urun, ters yonlu |
| Boya pigmenti (pigment) | 200-250 | 80-95 | Renk homojenlik kritik |
| Katalitor (catalyst) | 200-280 | 85-100 | Gozenek yapisi kontrolu |

### Ilac (Farmasotik) Sektoru

| Urun | Giris T (degC) | Cikis T (degC) | Not |
|------|:--------------:|:--------------:|-----|
| Ilac aktif maddesi (API) | 120-160 | 60-80 | Cok hassas, dusuk T |
| Enzimler (enzymes) | 130-160 | 60-75 | Biyolojik aktivite korumasi |
| Probiyotikler | 120-150 | 55-70 | Canlilik orani kritik |

## Iyilestirme

### Enerji Tasarrufu Onerileri

| Onlem | Enerji Tasarrufu (%) | Tipik Geri Odeme | Aciklama |
|-------|:--------------------:|:----------------:|----------|
| On konsantrasyon (pre-concentration) | 15-30 | 1-2 yil | Evaporator ile besleme konsantrasyonunu %30'dan %50+ seviyesine cikarmak buharlastirilacak su miktarini %40'a kadar azaltir. En etkili tasarruf yontemi |
| Egzoz havasi isi geri kazanimi (exhaust heat recovery) | 10-25 | 1-3 yil | Egzoz havasinin entalpisini giris havasini on isitmak veya beslemeyi on isitmak icin kullanma. Isi degistirici veya isi pompasi ile |
| Cok asamali kurutma (multi-stage drying) | 15-25 | 3-5 yil | Sprey kurutucu + akiskan yatak (fluidized bed) kombinasyonu. Urun sprey kurutucudan %8-12 nemle cikar, son kurutma akiskan yatakta yapilir. Daha dusuk egzoz T mumkun |
| Giris havasi sicakligi optimizasyonu | 3-8 | Yatirim gerektirmez | Urun kalitesi izin verdigi olcude T_giris artirma. Her 10 degC artis ~%2-3 verimlilik iyilesmesi |
| Cikis havasi sicakligi optimizasyonu | 5-15 | Yatirim gerektirmez | T_cikis'i urun nem spesifikasyonuna gore mumkun olan en dusuk seviyeye indirme |
| Egzoz havasi kismi geri devri (partial recirculation) | 5-15 | 2-4 yil | Egzoz havasinin bir kisminin (%10-30) giris havasina karistirilmasi. Nem artisi nedeniyle sinirli, dikkatli kontrol gerektirir |
| Yalitim iyilestirme (insulation) | 3-5 | 0.5-1 yil | Kurutma odasi, kanal ve siklon yalitimi |
| Dogrudan gazla isitma (direct gas firing) | 5-10 | 2-4 yil | Buhar isitma yerine dogrudan yanma; buhar uretim kayiplari onlenir (gida-disi uygulamalar) |

### Cok Asamali Kurutma Detayi

Cok asamali kurutma (multi-stage drying), sprey kurutucunun exergy verimini iyilestirmenin en
etkili yapisal yontemidir:

- **1. asama (spray dryer):** Urun %8-12 neme kadar kurutulur (geleneksel %3-5 yerine)
- **2. asama (fluidized bed):** Son kurutma dusuk sicaklikta (60-90 degC) akiskan yatakta yapilir
- **3. asama (opsiyonel):** Titresimli akiskan yatak ile sogutma ve son kurutma

Bu yaklasimin avantajlari:
- Sprey kurutucuda cikis havasi sicakligi dusurulur (SMER iyilesir)
- Akiskan yatak daha dusuk sicaklikta calisir (daha az exergy yikimi)
- Toplam SEC %15-25 azalir
- Urun parcacik boyutu ve yogunlugu daha iyi kontrol edilir

Dezavantaji: Daha yuksek ilk yatirim ve daha karmasik isletme.

### Egzoz Havasi Geri Devri Sinirlamalari

Sprey kurutucularda egzoz havasi geri devri, diger kurutucu tiplerine gore cok daha kisitlidir:

- **Nem siniri:** Giris havasindaki nem artisi, kurutma kapasitesini dogrudan dusurur
- **Maksimum geri devir orani:** Tipik %10-30 (bant kurutucuda %50-70 mumkun)
- **Urun kalite riski:** Yuksek nemli hava ile temas, yapiskan urunlerde oda birikimini arttirir
- **Kontrol zorlugu:** Nem dengesi cok hassas, kapali cevrim kontrol sistemi gerektirir
- **Gida guvenligi:** Gida uygulamalarinda hijyen riski nedeniyle geri devir kisitlanabilir

## Yatirim

### Ekipman Maliyetleri (2026 Avrupa Fiyatlari)

| Kapasite (kg su/h) | Kurutma Odasi + Atomizor (EUR) | Siklon + Filtre (EUR) | Fan Sistemi (EUR) | Isitma Sistemi (EUR) | Toplam Sistem (EUR) |
|--------------------:|-------------------------------:|----------------------:|------------------:|---------------------:|--------------------:|
| 50-100 | 30.000-80.000 | 10.000-30.000 | 5.000-15.000 | 5.000-20.000 | 50.000-150.000 |
| 500-1.000 | 80.000-250.000 | 30.000-80.000 | 20.000-50.000 | 20.000-60.000 | 150.000-500.000 |
| 1.000-3.000 | 250.000-700.000 | 80.000-200.000 | 50.000-120.000 | 50.000-150.000 | 500.000-1.500.000 |
| 3.000-6.000 | 500.000-1.200.000 | 150.000-350.000 | 100.000-250.000 | 100.000-300.000 | 1.000.000-2.500.000 |
| 6.000-30.000 | 1.000.000-2.500.000 | 300.000-700.000 | 200.000-500.000 | 200.000-600.000 | 2.000.000-5.000.000 |

> **Not:** Fiyatlar montaj, insaat, otomasyon ve yardimci ekipman harictir. Montaj dahil toplam
> proje maliyeti, ekipman maliyetinin 1.5-2.5 kati olabilir. Gida sektoru uygulamalarinda paslanmaz
> celik (AISI 316) kullanimi maliyeti %30-50 arttirir.

### Isletme Maliyetleri (Yillik, 5.000 saat/yil)

| Kalem | Tipik Aralik | Not |
|-------|:------------:|-----|
| Dogalgaz (termal enerji) | 150.000 - 2.000.000 EUR/yil | En buyuk isletme maliyeti kalemi |
| Elektrik (fan + atomizor) | 30.000 - 400.000 EUR/yil | Buyuk hava hacimleri nedeniyle yuksek |
| Bakim ve yedek parca | 15.000 - 100.000 EUR/yil | Atomizor asinma parcalari, nozullar |
| Toz toplama (filtre) | 5.000 - 30.000 EUR/yil | Torba filtre degisimi |

### Iyilestirme Yatirim Geri Donus Analizi

| Iyilestirme | Tipik Yatirim (EUR) | Yillik Tasarruf (EUR) | Geri Donus (yil) |
|-------------|:-------------------:|:---------------------:|:----------------:|
| Egzoz isi geri kazanim (heat recovery) | 50.000-300.000 | 30.000-200.000 | 1-3 |
| On konsantrasyon (evaporator) | 200.000-1.000.000 | 100.000-500.000 | 1-2.5 |
| Cok asamali donusum (multi-stage) | 300.000-1.500.000 | 80.000-400.000 | 2-5 |
| Yalitim (insulation) | 10.000-50.000 | 10.000-40.000 | 0.5-1.5 |
| VSD fan surucusu | 15.000-80.000 | 10.000-60.000 | 1-2 |

## Dikkat Noktalari

1. **Toz patlama riski:** Organik tozlar (sut tozu, nisasta, un) patlayici ortam olusturabilir.
   ATEX siniflandirmasi (Zone 20/21/22) ve inert gaz (N2) kullanimi degerlendirilmelidir.
2. **Yapiskanlik (stickiness):** Bazi urunler (meyve suyu, bal) yapiskan faz gecis sicakligina
   (sticky point) sahiptir — kurutma odasi duvar birikimini onlemek icin sogutma havasi veya
   maltodekstrin takviyesi gerekebilir.
3. **Urun kalite kontrolu:** Cikis havasi sicakligi en onemli kontrol parametresidir. Urun nemi,
   renk, cozunurluk ve yigin yogunlugu dogrudan bu parametreye baglidir.
4. **Fan enerji tuketimi:** Buyuk hava hacimleri nedeniyle fan gucu toplam elektrik tuketiminin
   %60-80'ini olusturabilir. VSD (degisken hizli surucu) mutlaka degerlendirilmelidir.

## İlgili Dosyalar

- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Exergy hesaplama formulleri: `dryer/formulas.md`
- Egzoz havasi isi geri kazanimi: `dryer/solutions/exhaust_heat_recovery.md`
- Hava geri devri cozumleri: `dryer/solutions/air_recirculation.md`
- Gida sektoru kurutma: `dryer/sectors/food_drying.md`
- Akiskan yatakli kurutucu: `dryer/equipment/fluidized_bed.md`
- Bant kurutucu: `dryer/equipment/belt_dryer.md`
- Isi pompali kurutucu: `dryer/equipment/heat_pump_dryer.md`
- Fabrika seviyesi analiz: `factory/cross_equipment.md`

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press — Kurutma teknolojileri temel referansi
2. Masters, K. (1991). *Spray Drying Handbook*, 5th Edition, Longman Scientific & Technical — Sprey kurutma ozel referansi
3. European Commission (2019). *Reference Document on Best Available Techniques in the Food, Drink and Milk Industries (FDM BREF)* — AB en iyi mevcut teknikler
4. Kemp, I.C. (2012). "Fundamentals of Energy Analysis of Dryers", in *Modern Drying Technology*, Vol. 4, Wiley-VCH
5. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press
6. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier
7. Bhandari, B.R. et al. (1997). "Spray drying of concentrated fruit juices", *Drying Technology*, 15(3-4)
8. DOE/AMO, *Improving Process Heating System Performance — A Sourcebook for Industry*
9. GEA Niro, *Spray Drying — Technical Notes and Application Guide*
10. Szargut, J. (2005). *Exergy Method: Technical and Ecological Applications*, WIT Press
