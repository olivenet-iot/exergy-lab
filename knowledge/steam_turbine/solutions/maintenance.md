---
title: "Buhar Türbini Bakım Planlaması — Steam Turbine Maintenance Planning"
category: solutions
equipment_type: steam_turbine
keywords: [bakım planlaması, maintenance planning, vibrasyon izleme, vibration monitoring, predictive maintenance, preventive maintenance, RCM, major overhaul, kanat muayenesi, blade inspection, yağ analizi, oil analysis, sızdırmazlık, sealing system, labyrinth seal, ISO 10816, ISO 20816, NDT]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/audit.md, steam_turbine/solutions/efficiency_improvement.md, steam_turbine/solutions/load_matching.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/condensing.md, steam_turbine/equipment/extraction.md]
use_when: ["Bakım stratejisi belirlenirken", "Major overhaul planlaması yapılırken", "Vibrasyon seviyeleri değerlendirilirken", "Türbin performans bozunması analiz edilirken", "Exergy verim düşüşünün bakım kaynaklı olduğu şüphelenildiğinde"]
priority: medium
last_updated: 2026-02-02
---
# Buhar Türbini Bakım Planlaması — Steam Turbine Maintenance Planning

> Son guncelleme: 2026-02-02

## Ozet

**Problem:** Buhar turbinlerinde ihmal edilen veya planlanmamis bakim, izentropik verimde %3-8 kayba neden olur. Bu durum artan exergy yikimi, dusuk elektrik uretimi ve yuksek yakit tuketimi olarak yansir. Endustriyel tesislerde bakim ihmali her yil yuz binlerce EUR ek maliyet olusturabilir.

**Cozum:** Yapilandirilmis bir bakim programi (structured maintenance program) ile performans bozunmasi minimize edilir. Ongorucyu bakim (predictive maintenance) teknikleri — vibrasyon analizi, yag analizi, termografi ve performans izleme — erken uyari saglar. Planli major overhaul'lar turkbin omrunu uzatir ve verimi restore eder.

**Tipik Tasarruf:** %2-5 izentropik verim iyilestirmesi (bakim sonrasi)
**Tipik ROI:** 0.5-2 yil (predictive maintenance sistemi icin), major overhaul ROI 1-4 yil

## 1. Bakim Stratejileri — Maintenance Strategies

### 1.1 Strateji Turleri

Endustriyel buhar turbinleri icin dort temel bakim stratejisi vardir:

**Duzeltici Bakim (Corrective/Reactive Maintenance):**
Ekipman arizalanincaya kadar mudahale yapilmaz. Planlanmamis durus sureleri uzun ve maliyetlidir. Buhar turbinlerinde reaktif bakim ciddi ikincil hasar riskine yol acar (ornegin yatak arizasi kanat hasarina neden olabilir).

**Onleyici Bakim (Preventive Maintenance):**
Zaman veya isletme saati bazli planli bakim aktiviteleri uygulanir. Uretici onerilerine (OEM recommendations) dayali olarak belirli araliklarda yag degisimi, filtre degisimi, sizma kontrolleri yapilir. Maliyet etkin ancak asiri bakim (over-maintenance) riski tasir.

**Ongorucyu Bakim (Predictive Maintenance — PdM):**
Ekipman durumu surekli veya periyodik olarak izlenir. Vibrasyon analizi, yag analizi, termografi (infrared thermography) ve performans izleme (performance monitoring) gibi teknikler kullanilir. Ariza belirtileri erken tespit edilerek planli mudahale yapilir.

**Guvenilirlik Merkezli Bakim (RCM — Reliability Centered Maintenance):**
Ekipmanin kritiklik analizi yapilarak her bilesene en uygun bakim stratejisi atanir. Ariza modlari ve etkileri analizi (FMEA — Failure Mode and Effects Analysis) temelinde karar verilir. En kapsamli ve sistematik yaklasimdir.

### 1.2 Strateji Karsilastirma Tablosu

| Kriter | Duzeltici | Onleyici | Ongorucyu (PdM) | RCM |
|--------|-----------|----------|------------------|-----|
| Bakim maliyeti | Dusuk (baslangicta) | Orta | Orta-Yuksek | Yuksek (baslangicta) |
| Planlanmamis durus | Cok yuksek | Dusuk | Cok dusuk | Minimum |
| Toplam maliyet (TCO) | Yuksek | Orta | Dusuk | En dusuk |
| Ikincil hasar riski | Yuksek | Dusuk | Cok dusuk | Minimum |
| Verim koruma | Zayif | Iyi | Cok iyi | En iyi |
| Uygulama zorlugu | Kolay | Kolay | Orta | Zor |
| Yatirim (CAPEX) | Yok | Dusuk | 15,000-80,000 EUR | 50,000-150,000 EUR |
| Tavsiye edilen turbin boyutu | < 500 kW (kritik olmayan) | Tum boyutlar | > 1 MW | > 5 MW |

> **Onemli:** Endustriyel buhar turbinleri icin minimum onleyici bakim, tercihen ongorucyu bakim uygulanmalidir. Tamamen reaktif bakim asla onerilen bir strateji degildir.

## 2. Major Overhaul Planlamasi

### 2.1 Muayene ve Overhaul Araliklari

Buhar turbini muayene araliklari isletme saatine, buhar kalitesine ve turbin tasarimina bagli olarak degisir:

```
Tipik muayene/overhaul araliklari:

Gunluk kontroller:
  - Vibrasyon seviyeleri (online monitoring varsa otomatik)
  - Yatak sicakliklari
  - Yag basinci ve sicakligi
  - Buhar parametreleri (giris/cikis P, T)
  - Sizinti kontrolleri (gorunur sizinti)

Minor muayene (Minor Inspection):
  - Aralik: 20,000-25,000 isletme saati (~2.5-3 yil)
  - Kapsam: Yatak muayenesi, sizma kontrolleri,
    valf kontrolleri, borescope ile kanat kontrolu
  - Tipik sure: 5-10 gun

Major overhaul:
  - Aralik: 40,000-60,000 isletme saati (~5-7 yil)
  - Kapsam: Tam acma, kanat muayene/degisim,
    yatak degisimi, sizma halka degisimi,
    alignment kontrolu, govde muayenesi
  - Tipik sure: 3-6 hafta
```

### 2.2 Major Overhaul Is Kapsami

Tipik bir major overhaul su aktiviteleri icerir:

| Aktivite | Aciklama | Tipik Sure |
|----------|----------|------------|
| Turbin acma ve muayene | Govde acma, rotor cikarma, gorunsel muayene | 3-5 gun |
| Kanat muayenesi (blade inspection) | NDT yontemleri ile kanat butunluk kontrolu | 3-5 gun |
| Kanat onarim/degisim | Erozyonlu/hasarli kanatlarin onarimi veya degisimi | 5-10 gun |
| Yatak degisimi (bearing replacement) | Journal ve thrust yatak degisimi veya yenileme | 2-3 gun |
| Sizma halka degisimi (seal replacement) | Labirent ve karbon halka degisimi | 2-4 gun |
| Alignment kontrolu ve duzeltme | Rotor-stator alignment, coupling alignment | 2-3 gun |
| Govde birlesim yuzeyi kontrolu | Flansh yuzey muayenesi, conta degisimi | 1-2 gun |
| Valf bakim | Governer valfi, trip valfi, kontrol valfleri | 2-4 gun |
| Montaj ve test | Kapama, yaglama, sicak alignment, devreye alma | 3-5 gun |
| **Toplam** | | **21-41 gun** |

### 2.3 Maliyet Tahminleri

Major overhaul maliyetleri turbin boyutu ve durumuna bagli olarak onemli olcude degisir:

| Turbin Boyutu | Minor Muayene (EUR) | Major Overhaul (EUR) | Acil Ariza Onarimi (EUR) |
|---------------|---------------------|----------------------|--------------------------|
| < 1 MW | 8,000-20,000 | 30,000-80,000 | 50,000-200,000 |
| 1-5 MW | 15,000-40,000 | 80,000-250,000 | 150,000-500,000 |
| 5-20 MW | 30,000-80,000 | 200,000-600,000 | 400,000-1,500,000 |
| 20-50 MW | 60,000-150,000 | 500,000-1,500,000 | 1,000,000-4,000,000 |
| > 50 MW | 100,000-300,000 | 1,000,000-4,000,000 | 2,000,000-10,000,000 |

> **Not:** Acil ariza onarimi maliyeti, planli major overhaul'un 2-4 katina cikar. Bu durum planli bakimin ekonomik gerekcelendirmesinin temelini olusturur.

## 3. Vibrasyon Izleme — Vibration Monitoring

### 3.1 Standartlar

Buhar turbini vibrasyon degerlendirmesi icin iki temel standart kullanilir:

- **ISO 10816:** Titresimin yapisal olcumu (bearing housing vibration) — eski standart
- **ISO 20816:** ISO 10816'nin guncellenmis versiyonu. Part 2 buyuk turkbinler, Part 4 gaz turkbinleri kapsar

Olcum buyuklukleri:
```
Vibrasyon parametreleri:
  - Deplasman (displacement): mikron (um), peak-to-peak
    Dusuk frekanslarda hassas (<10 Hz)
  - Hiz (velocity): mm/s, RMS
    Genel makine durumu icin en yaygin
  - Ivme (acceleration): g veya m/s^2, peak
    Yuksek frekans (yatak hatasi tespiti)
```

### 3.2 Vibrasyon Siddet Bolgerleri

ISO 10816-3 / ISO 20816-2 standartlarina gore vibrasyon siddet bolgerleri:

| Bolge | Tanim | Velocity RMS [mm/s] (Grup 1: > 300 kW, esnek mesnet) | Aksiyon |
|-------|-------|-------------------------------------------------------|---------|
| A | Yeni/iyi durum | 0 - 2.3 | Normal isletme |
| B | Sinirsiz isletme icin kabul edilebilir | 2.3 - 4.5 | Normal isletme, izleme |
| C | Sinirli sure isletme | 4.5 - 7.1 | Uyari, bakim planla |
| D | Hasar riski | > 7.1 | Alarm, derhal mudahale |

> **Onemli:** Vibrasyon trend analizi, mutlak degerlerin kendisinden daha onemlidir. Ani bir artis (ornegin %25 artis 24 saat icinde) ciddi bir ariza belirtisi olabilir.

### 3.3 Tipik Ariza Imzalari

| Ariza Turu | Baskin Frekans | Faz Iliskisi | Yonu | Ozellikler |
|------------|----------------|--------------|------|------------|
| Dengesizlik (Imbalance) | 1X (donus frekansi) | Sabit, 90deg yatak arasinda | Radyal | En yaygin hata; tek duzlem veya cift duzlem |
| Eksantriklik (Misalignment) | 1X, 2X, 3X | Kararsiz | Aksiyal + Radyal | Aksiyal bilesen belirgin |
| Yatak hasari (Bearing defect) | Yatak gecis frekanslari (BPFO, BPFI) | Rastgele | Radyal | Yuksek frekans zarfi analizi gerekir |
| Kanat hasari (Blade issue) | Kanat gecis frekansi (BPF = N x RPM) | -- | Radyal | Yan bantlar gorulebilir |
| Yag calkantisi (Oil whirl) | 0.42-0.48X | -- | Radyal | Alt senkron; journal yatak sorunlarinda |
| Rotor catlagi (Shaft crack) | 1X, 2X | 1X fazda kayma | Radyal + Aksiyal | Cok tehlikeli, hizla buyur |

### 3.4 Alarm Seviyeleri Tablosu

Endustriyel buhar turbini icin onerilen alarm seviyeleri:

| Parametre | Uyari (Warning) | Alarm | Trip |
|-----------|-----------------|-------|------|
| Govde vibrasyonu (velocity RMS) | 4.5 mm/s | 7.1 mm/s | 11.0 mm/s |
| Mil vibrasyonu (shaft displacement p-p) | 80 um | 125 um | 200 um |
| Aksiyal deplasman | 0.5 mm | 0.8 mm | 1.2 mm |
| Yatak sicakligi (journal) | 90 degC | 100 degC | 110 degC |
| Yatak sicakligi (thrust) | 100 degC | 110 degC | 120 degC |

## 4. Kanat Muayenesi — Blade Inspection

### 4.1 Muayene Yontemleri

**Gorunsel Muayene (Visual Inspection):**
Ilk asama olarak uygulanir. Borescope ile turbin acilmadan yapilabilir. Erozyon, korozyon, catlak, yabanci cisim hasari (FOD — Foreign Object Damage) ve birikim (fouling) tespit edilir.

**Tahribatsiz Muayene Yontemleri (NDT — Non-Destructive Testing):**

| NDT Yontemi | Uygulama Alani | Tespit Limiti | Avantaj | Dezavantaj |
|-------------|----------------|---------------|---------|------------|
| Manyetik parcacik (Magnetic Particle — MT) | Yuzey ve yuzey alti catlaklari | > 0.5 mm | Hizli, ucuz, gercek zamanli | Sadece ferromanyetik malzeme |
| Ultrasonik (Ultrasonic — UT) | Ic ve yuzey catlaklari | > 1 mm | Derinlik olcumu mumkun | Egitimli personel gerekli |
| Boya nufuz (Dye Penetrant — PT) | Yuzey catlaklari | > 0.5 mm | Basit, ucuz | Sadece acik yuzey catlaklari |
| Girdap akimi (Eddy Current — ET) | Yuzey ve yuzey alti | > 0.3 mm | Temassiz, hizli | Iletken malzemeler icin |

### 4.2 Yaygin Kanat Hasarlari

```
Kanat hasar turleri ve etkileri:

1. Erozyon (Erosion):
   - Kaynak: Islak buhar damlaciklari (wet steam droplets)
   - Bolge: Kanat giri kenarinda (leading edge), ozellikle son kademelerde
   - Etki: %0.5-2.0 verim kaybi
   - Cozum: Stellite kaplama, erosion shield

2. Korozyon (Corrosion):
   - Kaynak: Buhar icindeki kimyasal safsizliklar (Cl, Na, S bilesikleri)
   - Bolge: Wilson cizgisi bolgesi (buhar kuruluk x = 0.95-0.97)
   - Etki: %0.5-1.5 verim kaybi + yorulma catlagi riski
   - Cozum: Buhar kimyasi kontrolu, korozyona dayanikli malzeme

3. Yabanci Cisim Hasari (FOD — Foreign Object Damage):
   - Kaynak: Kaynak curapu, conta parcasi, boru parcasi
   - Bolge: Ilk kademe kanatlari
   - Etki: Degisken — ani verim kaybi
   - Cozum: Buhar hatti temizligi, filtre/strainer

4. Srunme (Creep):
   - Kaynak: Yuksek sicaklik + yuksek gerilme, uzun sure
   - Bolge: HP kademesi kanatlari (> 450 degC)
   - Etki: Kanat uzamasi, tip clearance degisimi
   - Cozum: Malzeme secimi, sicaklik kontrolu

5. Yorulma Catlagi (Fatigue Cracking):
   - Kaynak: Tekrarli mekanik/termal gerilme
   - Bolge: Kanat koku (blade root), filet bolgesi
   - Etki: Katastrofik ariza riski
   - Cozum: NDT ile erken tespit, tasarim iyilestirme
```

### 4.3 Onarim vs Degisim Karar Kriterleri

| Kriter | Onarim Uygun | Degisim Gerekli |
|--------|-------------|-----------------|
| Erozyon derinligi | < 1.5 mm | > 1.5 mm veya %10 kesit kaybi |
| Catlak boyutu | < 3 mm, yuzeysel | > 3 mm veya kok bolgesinde |
| Srunme uzamasi | < %0.5 | > %0.5 |
| Korozyon | Yuzeysel pitting | Derin pitting veya stres korozyon catlagi |
| FOD | Kucuk capak/cizik | Yaprak parcalanmasi veya belirgin deformasyon |
| Kalan omur | > 50,000 saat | < 20,000 saat |

## 5. Yag Sistemi Bakimi — Lube Oil System Maintenance

### 5.1 Yag Analiz Parametreleri

Turbin yagi duzgun olarak analiz edilerek yatak ve disliler korunur:

| Parametre | Yeni Yag Degeri | Uyari Limiti | Kritik Limit | Olcum Yontemi |
|-----------|-----------------|--------------|--------------|---------------|
| Viskozite (40 degC) | ISO VG 32/46 | +/- %10 degisim | +/- %20 degisim | ASTM D445 |
| Asit sayi (TAN — Total Acid Number) | < 0.1 mg KOH/g | 0.3 mg KOH/g | 0.5 mg KOH/g | ASTM D664 |
| Su icerik | < 50 ppm | 200 ppm | 500 ppm | ASTM D6304 (Karl Fischer) |
| Parcacik sayimi | ISO 15/12/9 | ISO 17/14/11 | ISO 19/16/13 | ISO 4406 |
| Demur (Fe) icerik | < 5 ppm | 20 ppm | 50 ppm | ICP spektrometri |
| Bakir (Cu) icerik | < 2 ppm | 10 ppm | 20 ppm | ICP spektrometri |
| Oksidasyon | < 5 Abs/cm | 15 Abs/cm | 25 Abs/cm | ASTM E2412 (FTIR) |

### 5.2 Yag Degisim Araliklari

```
Turbin yagi degisim stratejisi:

Zaman bazli (konservatif):
  - Mineral yag: 3-5 yil veya 25,000 isletme saati
  - Sentetik yag: 5-8 yil veya 40,000 isletme saati

Durum bazli (onerilen):
  - TAN > 0.5 mg KOH/g → Degistir
  - Su > 500 ppm → Dehidrasyon veya degistir
  - Parcacik > ISO 19/16/13 → Filtrele veya degistir
  - Viskozite degisimi > %20 → Degistir
  - Oksidasyon > 25 Abs/cm → Degistir
```

### 5.3 Yikama Proseduru (Flushing)

Major overhaul sonrasinda veya kontaminasyon tespit edildiginde yag sistemi yikamasi yapilir:

1. Eski yagi bosalt
2. Yikama yagi ile 50-60 degC'de minimum 24 saat sirkule et
3. Parcacik seviyesini olc — hedef: ISO 15/12/9 veya daha iyi
4. Hedefe ulasilamazsa filtre degistir ve yikamaya devam et
5. Yikama yagini tamamen bosalt
6. Yeni turbin yagi ile doldur ve 4 saat sirkule et
7. Tekrar parcacik olcumu yap — kabul kriterini dogrula

### 5.4 Filtre Degisimi

| Filtre Tipi | Degisim Kriteri | Tipik Aralik |
|-------------|-----------------|--------------|
| Ana yag filtresi | Diferansiyel basinc > 1.5 bar | 3-6 ay |
| By-pass filtre (kidney loop) | Diferansiyel basinc > 1.0 bar | 6-12 ay |
| Hava filtresi (breather) | Gorsel kontrol / 6 ay | 6 ay |
| Yag buhari filtresi (mist eliminator) | Diferansiyel basinc olcumu | 12 ay |

## 6. Sizdimazlik Sistemi — Sealing System

### 6.1 Sizdimazlik Turleri

Buhar turbinlerinde uc temel sizdimazlik tipi kullanilir:

```
Sizdimazlik turleri ve ozellikleri:

1. Labirent Sizdimazlik (Labyrinth Seal):
   - En yaygin tip
   - Temassiz — asindirma yok (normal kosullarda)
   - Bosluklarda (clearance) gaz akisini kisitlar
   - Tipik bosluk: 0.3-0.5 mm (yeni)
   - Asiri bosluk: > 0.8-1.0 mm → kapasite kaybi

2. Karbon Halka Sizdimazlik (Carbon Ring Seal):
   - Dusuk basinc bolgelerinde kullanilir
   - Temas yapar — asindirmali
   - Iyi sizdimazlik saglar ancak omru sinirlidir
   - Tipik omur: 15,000-30,000 saat

3. Firca Sizdimazlik (Brush Seal):
   - Modern tasarim, labirente gore %50-80 daha iyi sizdimazlik
   - Ince metal tellerden olusur
   - Yeni tasarimlarda ve retro-fit'lerde yayginlasiyor
   - Tipik bosluk: ~ 0.1 mm etkin bosluk
```

### 6.2 Asinma Gostergeleri

| Gosterge | Normal | Uyari | Kritik |
|----------|--------|-------|--------|
| Labirent bosluk artisi | < %20 | %20-50 | > %50 |
| Gland buhar tuketimi artisi | < %10 | %10-30 | > %30 |
| Sizma buharina isi kaybi | < %0.5 toplam giris | %0.5-1.5 | > %1.5 |
| Karbon halka kalinti kalinligi | > %50 | %30-50 | < %30 |

### 6.3 Sizdimazlik Bozulmasinin Exergy Etkisi

Sizdimazlik bozulmasi dogrudan exergy kaybina neden olur:

```
Exergy kaybi hesabi — sizdimazlik sizintisi:

Sizinti debisi (leakage mass flow):
  m_leak = C_d * A_gap * sqrt(2 * rho * dP)

  Burada:
    C_d  : Bosaltim katsayisi (~0.6-0.8)
    A_gap: Bosluk alani [m^2]
    rho  : Buhar yogunlugu [kg/m^3]
    dP   : Basinc farki [Pa]

Sizintinin exergy kaybi:
  Ex_leak = m_leak * (h_leak - h_0 - T_0 * (s_leak - s_0))

  Burada:
    h_leak, s_leak: Sizinti buharinin entalpi ve entropisi
    h_0, s_0, T_0 : Referans (dead state) degerleri

Tipik etki:
  Bosluk %100 artarsa → sizinti debisi ~%40-60 artar
  5 MW turbin icin: 20-80 kW exergy kaybi artisi
```

## 7. Bakim Takvimi Ornegi — Sample Annual Maintenance Calendar

Asagida 5 MW endustriyel karsi-basinc (back-pressure) buhar turbini icin yillik bakim takvimi ornegi verilmistir:

| Aktivite | Periyot | O | S | M | N | M | H | T | A | E | E | K | A |
|----------|---------|---|---|---|---|---|---|---|---|---|---|---|---|
| Gunluk isletme kontrolleri | Gunluk | X | X | X | X | X | X | X | X | X | X | X | X |
| Vibrasyon olcumu (offline) | Aylik | X | X | X | X | X | X | X | X | X | X | X | X |
| Yag numune analizi | 3 aylik | X | | | X | | | X | | | X | | |
| Governer/kontrol valf testi | 6 aylik | | | X | | | | | | X | | | |
| Emniyet valf testi (trip test) | 6 aylik | X | | | | | | X | | | | | |
| Filtre degisimi (ana yag) | 6 aylik | | X | | | | | | X | | | | |
| Elektrik ve enstrumantasyon kontrol | 6 aylik | | | | X | | | | | | X | | |
| Gland steam sistem kontrolu | 6 aylik | | | X | | | | | | X | | | |
| Buhar kalitesi analizi | 3 aylik | X | | | X | | | X | | | X | | |
| Yillik genel muayene | Yillik | | | | | | | | | | | | X |
| Borescope kanat kontrolu | Yillik | | | | | | | | | | | | X |
| Termal performans testi (ASME PTC 6) | Yillik | | | | | | X | | | | | | |
| Alignment kontrolu | Yillik | | | | | | | | | | | | X |

> **Not:** Tablo aylari Ocak-Aralik sirasina gore gosterir (O, S, M, N, M, H, T, A, E, E, K, A). Yillik muayene ve overhaul tercihen plansiz talep dusuk oldugu doneme (tipik olarak yaz) planlanir, ancak burada genel takvim gosterilmistir.

### Gunluk Kontrol Listesi

```
Gunluk isletme kontrol listesi:

[ ] Vibrasyon seviyeleri (tum yatak noktalari)
[ ] Yatak sicakliklari (journal + thrust)
[ ] Yag basinci (giris ve cikis)
[ ] Yag sicakligi ve seviyesi
[ ] Buhar giris basinci ve sicakligi
[ ] Buhar cikis basinci ve sicakligi
[ ] Devir (RPM)
[ ] Governer/kontrol sistemi durumu
[ ] Sizdimazlik buhar (gland steam) durumu
[ ] Gorunur sizinti veya ses anomalisi
[ ] Yag sogutucusu sicakliklari
[ ] Drenaj hatlari kontrolu
```

## 8. Exergy Etkisi — Bakimin Exergy Verimine Etkisi

### 8.1 Performans Bozunma Mekanizmalari

Bakim ihmali sonucu olusan exergy verim kayiplari:

| Bozunma Mekanizmasi | Izentropik Verim Kaybi | Exergy Yikimi Artisi | Geri Kazanim Potansiyeli |
|---------------------|------------------------|----------------------|--------------------------|
| Kanat erozyon/fouling | %1-3 | %1-4 | Temizlik/kaplama ile %80-95 |
| Sizdimazlik asinmasi | %0.5-2 | %0.5-2.5 | Degisim ile %95-100 |
| Yatak asinmasi | %0.2-0.5 | %0.2-0.5 | Degisim ile %100 |
| Tip clearance artisi | %0.5-1.5 | %0.5-2 | Overhaul ile %90-95 |
| Valf sizintisi | %0.3-1.0 | %0.3-1.0 | Onarim/degisim ile %90-100 |
| **Toplam (ihmal edilen turbin)** | **%3-8** | **%3-10** | **Kapsamli overhaul ile %80-95** |

### 8.2 Bakimin Exergy Kazanimi Hesabi

```
Bakim sonrasi exergy kazanimi hesabi:

Mevcut durum (bakim oncesi):
  eta_is_mevcut = 0.70 (ornek — benchmark altinda)
  W_gercek_mevcut = m_s * (h_in - h_out_gercek)

Bakim sonrasi (restore edilmis):
  eta_is_bakim = 0.77 (ornek — benchmark yakin)
  W_gercek_bakim = m_s * (h_in - h_out_bakim)
  h_out_bakim = h_in - eta_is_bakim * (h_in - h_out_izentropik)

Exergy kazanimi:
  Delta_Ex = W_gercek_bakim - W_gercek_mevcut [kW]

Ornek hesap (5 MW back-pressure turbin):
  Buhar debisi: m_s = 25 t/h = 6.94 kg/s
  Giris: 40 bar, 400 degC → h_in = 3,214 kJ/kg, s_in = 6.77 kJ/(kg.K)
  Cikis izentropik: 5 bar → h_out_is = 2,752 kJ/kg

  Bakim oncesi (eta_is = 0.70):
    h_out_oncesi = 3,214 - 0.70*(3,214-2,752) = 2,890.6 kJ/kg
    W_oncesi = 6.94 * (3,214 - 2,890.6) = 2,244 kW

  Bakim sonrasi (eta_is = 0.77):
    h_out_sonrasi = 3,214 - 0.77*(3,214-2,752) = 2,858.3 kJ/kg
    W_sonrasi = 6.94 * (3,214 - 2,858.3) = 2,469 kW

  Exergy kazanimi:
    Delta_Ex = 2,469 - 2,244 = 225 kW

  Yillik tasarruf (8,000 saat, 0.10 EUR/kWh):
    225 * 8,000 * 0.10 = 180,000 EUR/yil
```

> **Onemli:** %7'lik bir izentropik verim iyilestirmesi, 5 MW turbinde 225 kW ek guc uretimi ve yillik 180,000 EUR tasarruf saglar. Bu deger, 200,000-600,000 EUR major overhaul maliyetinin 1-3 yil icinde geri donusunu gosterir.

### 8.3 Bozunma Egrisi — Degradation Curve

```
Izentropik verim vs isletme saati (tipik):

eta_is
  |
80|____
  |    \___
77|        \____
  |             \______
74|                    \_____
  |                          \____
71|                               \_____
  |                                     \
68|                                      \
  |___|___|___|___|___|___|___|___|___|___\___
  0   5k  10k 15k 20k 25k 30k 35k 40k 45k 50k
                    Isletme Saati

  ---- Bakim yapilan turbin (tepe:~79%, tabani:~75%)
  ____ Bakimsiz turbin (tepe:~80%, tabani:~68%)

Notlar:
  - Bakimli turbinde her 20,000-25,000 saatte minor muayene
    ile verim kismen restore edilir
  - Bakimsiz turbinde bozunma giderek hizlanir
  - Major overhaul (40,000-60,000 saat) verimi ~%95-98
    oraninda restore eder
```

## İlgili Dosyalar

- **Formul ve hesaplamalar:** [steam_turbine/formulas.md](../formulas.md) — Izentropik verim, exergy yikimi, heat rate formulleri
- **Benchmark degerleri:** [steam_turbine/benchmarks.md](../benchmarks.md) — Turbin tiplerine gore verim beklentileri
- **Denetim rehberi:** [steam_turbine/audit.md](../audit.md) — Saha denetimi ve olcum proseduru
- **Verim iyilestirme:** [steam_turbine/solutions/efficiency_improvement.md](efficiency_improvement.md) — Fouling temizligi, seal degisimi, kaplama
- **Yuk esleme:** [steam_turbine/solutions/load_matching.md](load_matching.md) — Kismi yuk optimizasyonu
- **Kondensat optimizasyonu:** [steam_turbine/solutions/condensate_optimization.md](condensate_optimization.md) — Kondensat geri donus ve feedwater heating
- **Karsi-basinc turkbini:** [steam_turbine/equipment/back_pressure.md](../equipment/back_pressure.md) — Back-pressure turbin tasarimi ve isletmesi
- **Kondensasyon turkbini:** [steam_turbine/equipment/condensing.md](../equipment/condensing.md) — Condensing turbin ozellikleri
- **Carpraz ekipman firsatlari:** [factory/cross_equipment.md](../../factory/cross_equipment.md) — Turbin atik isisi entegrasyonu

## Referanslar

### Akademik Kaynaklar

1. **Kotas, T.J.** (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Buhar turbini exergy analizi metodolojisi ve referans degerler.
2. **Horlock, J.H.** (2003). *Advanced Gas Turbine Cycles*. Pergamon. — CHP sistemlerinde turbin performans analizi ve bakim etkisi.
3. **Bejan, A.** (2006). *Advanced Engineering Thermodynamics*. 3rd ed. Wiley. — Entropi uretimi minimizasyonu ve exergy yikimi teorisi.
4. **Cengel, Y.A. & Boles, M.A.** (2019). *Thermodynamics: An Engineering Approach*. 9th ed. McGraw-Hill. — Buhar turkbini termodinamik temelleri ve Rankine cevrimi.

### Standartlar ve Endüstriyel Rehberler

5. **API 612** — *Petroleum, Petrochemical and Natural Gas Industries — Steam Turbines — Special Purpose*. — Ozel amacli buhar turkbinlerinin tasarim, malzeme ve muayene gereksinimleri.
6. **ASME PTC 6** — *Performance Test Code on Steam Turbines*. — Buhar turkbini performans testi proseduru ve kabul kriterleri.
7. **ISO 10816-3 / ISO 20816-2** — *Mechanical Vibration — Evaluation of Machine Vibration*. — Turbin vibrasyon degerlendirme standartlari ve siddet siniflari.
8. **ISO 4406** — *Hydraulic Fluid Power — Fluids — Method for Coding the Level of Contamination by Solid Particles*. — Yag temizlik siniflandirmasi.
9. **VGB PowerTech** (2018). *Guideline for the Assessment of the Remaining Useful Life of Steam Turbine Components*. — Kanat omur degerlendirmesi rehberi.
10. **EPRI** (2015). *Steam Turbine Maintenance Guide*. Electric Power Research Institute. — Kapsamli turbin bakim planlama rehberi.
