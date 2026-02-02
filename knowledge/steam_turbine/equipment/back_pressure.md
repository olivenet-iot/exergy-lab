---
title: "Karsi Basincli Buhar Turbini — Back-Pressure Steam Turbine"
category: equipment
equipment_type: steam_turbine
subtype: "Karsi Basincli (Back-Pressure)"
keywords: [karsi basincli turbin, back-pressure, CHP, kojenerasyon, proses buhari, HPR, exergy]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/equipment/extraction.md, steam_turbine/economics/feasibility.md, boiler/formulas.md, factory/cogeneration.md]
use_when: ["Karsi basincli turbin analizi yapilirken", "CHP exergy verimi hesaplanirken", "Proses buhari entegrasyonu degerlendirilirken", "HPR hesaplamasi gerektiginde"]
priority: high
last_updated: 2026-01-31
---
# Karsi Basincli Buhar Turbini — Back-Pressure Steam Turbine

> Son guncelleme: 2026-01-31

## Genel Bilgiler

Karsi basincli (back-pressure) buhar turbinleri, yuksek basincli buhari belirli bir cikis basincinda
proses buhari olarak teslim ederken elektrik veya mekanik guc ureten turbin tipidir.
Tum cikis buhari proseste kullanildigi icin kondenser gerektirmez; bu da karsi basincli
turbinleri CHP (combined heat and power / kojenerasyon) sistemlerinin temel bileseni yapar.

- **Tip:** Karsi basincli (back-pressure / non-condensing) turbin
- **Kapasite araligi:** 0.5 - 100 MW elektrik (endustriyel: tipik 1-30 MW)
- **Giris kosullari:** 10 - 100 bar, 250 - 540 C (kizgin buhar)
- **Cikis basinci:** 2 - 15 bar (proses ihtiyacina gore)
- **Elektrik verimi:** %15 - 25 (yalniz elektrik bazinda)
- **Toplam enerji verimi:** %80 - 92 (elektrik + isi)
- **Toplam exergy verimi:** %25 - 38 (elektrik + proses buhari exergisi)
- **HPR (Heat-to-Power Ratio):** 3 - 10 (tipik 4-8)
- **Izentropik verim:** %65 - 85 (boyut ve kademe sayisina bagli)
- **Yaygin markalar:** Siemens, MAN, Dresser-Rand, Shin Nippon, Triveni, TGM

## Calisma Prensibi

Karsi basincli turbin, Rankine cevriminin bir parcasi olarak calisir ancak klasik yogusmali
cevrimden farkli olarak cikis buhari vakuma degil proses basincina genisler.

### Temel Is Dongusu

```
1. Kazan yuksek basincli kizgin buhar uretir (ornegin 40 bar, 400 C)
2. Buhar turbin girisine beslenir
3. Turbin icinde buhar genisler, rotor doner, jenerator elektrik uretir
4. Cikis buhari (ornegin 4 bar, doymus veya hafif kizgin) prosese gider
5. Proses buhari kullanilir (isitma, kurutma, reaksiyon vb.)
6. Kondensat kazan besleme suyuna geri doner
```

### Enerji ve Exergy Akisi

```
YAKIT EXERGY GIRISI (100%)
|
|--> KAZAN --> Yanma tersinmezligi (%25-30)
|              Isi transfer tersinmezligi (%15-25)
|              Baca gazi, radyasyon kaybi (%5-10)
|
|--> TURBIN GIRIS EXERGY (%35-48 yakit exergy'si)
|     |
|     |--> ELEKTRIK (saf exergy): %5-10 yakit exergy'si
|     |--> Turbin ici tersinmezlik: %2-5 yakit exergy'si
|     |
|     |--> PROSES BUHARI EXERGY: %20-35 yakit exergy'si
|           (Proses tarafindan kullanilir veya kaybolur)
```

**Onemli:** Karsi basincli turbin, giris ve cikis exergisi arasindaki farktan
is uretir. Cikis buharinin hala yuksek exergy icerigi vardir ve bu exergy
proseste degerlendirilebilir.

## Proses Buhari Entegrasyonu

### Tipik Proses Buhar Basinclari

| Proses Tipi | Buhar Basinci [bar] | Sicaklik [C] | Kullanim |
|-------------|--------------------:|-------------:|----------|
| Dusuk basincli isitma (LP) | 2 - 4 | 120 - 145 | Kalorifer, on isitma |
| Orta basincli proses (MP) | 4 - 8 | 145 - 170 | Evaporasyon, kurutma |
| Yuksek basincli proses (HP) | 8 - 15 | 170 - 200 | Reaktorler, sterilizasyon |
| Cok yuksek basincli proses | 15 - 40 | 200 - 250 | Kimyasal proses, rafineriler |

### Sektor Bazinda Proses Buhari Gereksinimleri

| Sektor | Tipik Proses Basinci [bar] | Tipik Yuk [ton/h] | HPR Araligi | Uygunluk |
|--------|---------------------------:|-----------:|------------:|----------|
| Seker endustrisi | 2 - 6 | 30 - 150 | 5 - 10 | Cok yuksek |
| Kagit ve seluloz | 3 - 10 | 20 - 200 | 4 - 8 | Cok yuksek |
| Kimya endustrisi | 4 - 40 | 10 - 100 | 3 - 7 | Yuksek |
| Gida ve icecek | 2 - 6 | 5 - 50 | 5 - 10 | Yuksek |
| Tekstil | 3 - 8 | 5 - 30 | 4 - 8 | Orta-Yuksek |
| Petrokimya / Rafineri | 10 - 40 | 50 - 500 | 3 - 6 | Yuksek |

**Seker Endustrisi:** Turkiye'deki seker fabrikalari karsi basincli turbin kullaniminin
en klasik orneklerinden biridir. Kampanya doneminde (90-120 gun) yuksek buhar talebi,
biyokutle (pancar kuspu / bagasse) yakiti ve yuksek HPR ideal bir eslesmedir.

**Kagit Endustrisi:** Kurutma silindirlerinde surekli buhar talebi, karsi basincli
turbinin sabit yuk faktorunde calismasina olanak tanir.

## HPR Analizi (Heat-to-Power Ratio)

### HPR Hesaplamasi

```
HPR = Q_proses / W_elek

Q_proses = m_dot x (h_cikis - h_kondensat)   [kW]
W_elek = m_dot x (h_giris - h_cikis) x eta_mek x eta_jen   [kW]

HPR = (h_cikis - h_kondensat) / [(h_giris - h_cikis) x eta_mek x eta_jen]

Burada:
- h_giris = turbin giris entalpisi [kJ/kg]
- h_cikis = turbin cikis entalpisi [kJ/kg]
- h_kondensat = kondensat donusu entalpisi [kJ/kg]
- eta_mek = mekanik verim [0.97-0.99]
- eta_jen = jenerator verimi [0.95-0.98]
```

### HPR Degerleri ve Giris/Cikis Kosula Bagliligi

| Giris [bar/C] | Cikis [bar] | Izentropik Verim | HPR | Elektrik Verimi [%] |
|:--------------:|:-----------:|:----------------:|:---:|:------------------:|
| 20 bar / 300 C | 4 bar | %75 | 8.2 | 10.9 |
| 40 bar / 400 C | 4 bar | %80 | 6.5 | 13.3 |
| 60 bar / 480 C | 4 bar | %82 | 5.2 | 16.1 |
| 80 bar / 520 C | 4 bar | %85 | 4.3 | 18.9 |
| 40 bar / 400 C | 2 bar | %80 | 4.8 | 17.2 |
| 40 bar / 400 C | 10 bar | %80 | 10.1 | 9.0 |

**Kilit Bilgi:** Giris basinci ve sicakligi arttikca HPR duser (daha fazla elektrik
orani), cikis basinci dusuruldukce HPR duser. Proses gereksinimi cikis basincini
belirler, ancak giris kosullari kazan tasarimina baglidir.

## Kontrol Sistemleri

### Yuk Kontrolu

Karsi basincli turbin, iki farkli kontrol modunda calisabilir:

1. **Buhar debi kontrolu (flow-following):** Turbin, prosesin buhar talebini
   karsilar. Elektrik uretimi buhar debisine baglidir ve dalgalanir.
   - Avantaj: Proses buhari kalitesi korunur
   - Dezavantaj: Elektrik uretimi kontrol edilemez

2. **Elektrik kontrolu (electricity-following):** Turbin, belirli bir elektrik
   yukunun altinda calisir. Buhar debisi elektrik talebine gore ayarlanir.
   - Avantaj: Elektrik uretimi planlanabilir
   - Dezavantaj: Proses buhari fazlasi/acigi olusabilir

### Bypass ve Emniyet Sistemleri

```
PRV (Pressure Reducing Valve) bypass:
- Turbin devre disi kaldiginda buhar PRV uzerinden prosese gider
- PRV, turbin cikis basincina esit basinca dusurur
- PRV gecisinde exergy kaybi olusur (izentalpik genisleme)

PRV exergy kaybi:
Ex_kayip_PRV = m_dot x T0 x (s_cikis_PRV - s_giris)
(PRV izentalpik oldugu icin h_giris = h_cikis, ancak entropi artar)

Tipik PRV exergy kaybi: Giris exergisinin %5-15'i
```

### Otomatik Kontrol Parametreleri

| Kontrol Parametresi | Tipik Ayar | Tolerans |
|---------------------|-----------|----------|
| Cikis basinci | Proses basinci | +/- 0.2 bar |
| Giris basinci | Kazan basinci | +/- 0.5 bar |
| Giris sicakligi | Kazan kizginlik | +/- 5 C |
| Devir sayisi | 3000 rpm (50 Hz) | +/- 0.5% |
| Titresim seviyesi | < 4.5 mm/s | ISO 10816-3 |

## Boyutlandirma

### Temel Boyutlandirma Adimi

```
Adim 1: Proses buhar debisini belirle
  m_dot = Q_proses / (h_cikis - h_kondensat)   [kg/s]

Adim 2: Turbin guc potansiyelini hesapla
  W_turbin = m_dot x (h_giris - h_cikis) x eta_is   [kW]
  W_elek = W_turbin x eta_mek x eta_jen   [kW]

Adim 3: Kazan kapasitesini dogrula
  Q_kazan = m_dot x (h_giris - h_besleme)   [kW]
  m_dot_yakit = Q_kazan / (LHV x eta_kazan)   [kg/s]

Adim 4: Ekonomik degerlendirme
  Yillik_uretim = W_elek x calisma_saati   [kWh/yil]
  Yillik_tasarruf = Yillik_uretim x c_elektrik   [EUR/yil]
  Geri_odeme = Yatirim / Yillik_tasarruf   [yil]
```

### Boyutlandirma Tablosu

| Turbin Gucu [MW] | Buhar Debisi [ton/h] | Giris Kosulu | Cikis | Tahmini Yatirim [EUR] |
|:-----------------:|:--------------------:|:------------:|:-----:|:---------------------:|
| 0.5 | 8-15 | 20 bar / 300 C | 4 bar | 200,000-400,000 |
| 1.0 | 15-25 | 30 bar / 350 C | 4 bar | 350,000-600,000 |
| 2.0 | 25-40 | 40 bar / 400 C | 4 bar | 550,000-900,000 |
| 5.0 | 50-80 | 40 bar / 400 C | 4 bar | 1,000,000-1,800,000 |
| 10.0 | 90-140 | 60 bar / 480 C | 4 bar | 1,800,000-3,000,000 |
| 20.0 | 160-250 | 80 bar / 520 C | 4 bar | 3,000,000-5,500,000 |

> **Not:** Yatirim maliyetleri turbin, jenerator, kontrol sistemi ve montaj dahil 2025 Avrupa
> piyasa fiyatlaridir. Kazan ve yardimci ekipman ayri fiyatlandirilir.

## Exergy Analizi

### Turbin Exergy Verimi

```
Turbin ici exergy verimi (is bazli):
eta_ex_turbin = W_turbin / (Ex_giris - Ex_cikis)

Burada:
  Ex_giris = m_dot x [(h_giris - h0) - T0 x (s_giris - s0)]
  Ex_cikis = m_dot x [(h_cikis - h0) - T0 x (s_cikis - s0)]

CHP sistemi exergy verimi:
eta_ex_CHP = (W_elek + Ex_proses_buhar) / Ex_yakit

Burada:
  Ex_proses_buhar = m_dot x [(h_cikis - h0) - T0 x (s_cikis - s0)]
  Ex_yakit = m_dot_yakit x ex_ch
```

### Ornek Exergy Hesaplamasi

```
Senaryo: 5 MW karsi basincli turbin, 40 bar / 400 C giris, 4 bar cikis

Giris buhari:
  h_giris = 3,214 kJ/kg,  s_giris = 6.769 kJ/(kg.K)
  ex_giris = (3,214 - 104.89) - 298.15 x (6.769 - 0.3674) = 1,200 kJ/kg

Cikis buhari (eta_is = 0.80):
  h_cikis,is = 2,753 kJ/kg
  h_cikis = 3,214 - 0.80 x (3,214 - 2,753) = 2,845 kJ/kg
  s_cikis = 7.051 kJ/(kg.K)
  ex_cikis = (2,845 - 104.89) - 298.15 x (7.051 - 0.3674) = 748 kJ/kg

Buhar debisi (5 MW elektrik icin):
  m_dot = 5,000 / [(3,214 - 2,845) x 0.98 x 0.97] = 14.3 kg/s = 51.5 ton/h

Exergy dengesi:
  Ex_giris = 14.3 x 1,200 = 17,160 kW
  Ex_cikis = 14.3 x 748 = 10,696 kW
  W_turbin = 14.3 x (3,214 - 2,845) = 5,277 kW
  Ex_yikim = 17,160 - 10,696 - 5,277 = 1,187 kW

Turbin exergy verimi (is bazli):
  eta_ex = 5,277 / (17,160 - 10,696) = 5,277 / 6,464 = %81.6

Exergy yikim orani:
  y_D = 1,187 / 17,160 = %6.9
```

### Exergy Yikim Kaynaklari

| Kaynak | Exergy Yikimi [%] | Azaltma Imkani |
|--------|-------------------:|----------------|
| Kanat profil kayiplari (blade profile) | 2 - 4 | Kanat tasarimi, yuzey kalitesi |
| Ikincil akis kayiplari (secondary flow) | 1 - 2 | Akis yonlendiriciler |
| Kanat ucu sizintisi (tip leakage) | 1 - 3 | Sizdirmazlik iyilestirme |
| Nem kayiplari (moisture losses) | 0 - 1 | Genellikle ihmal edilebilir (BP'de) |
| Mekanik kayiplar (bearings) | 0.5 - 1 | Yatak bakimi |

## Giris/Cikis Kosullari ve Varsayilan Degerler

Sahada olcum yapilamadigi durumlarda kullanilacak varsayilan degerler:

| Parametre | Varsayilan Deger | Aciklama |
|-----------|:----------------:|----------|
| Giris basinci | 40 bar | Tipik endustriyel CHP |
| Giris sicakligi | 400 C | 40 bar'a uygun kizginlik |
| Cikis basinci | 4 bar | Tipik proses basinci |
| Izentropik verim | %78 | Orta olcekli (2-10 MW) turbin |
| Mekanik verim | %98 | Standart yatak kaybi |
| Jenerator verimi | %97 | Standart jenerator |
| Kazan verimi | %88 | Dogalgaz, ekonomizerli |
| Kondensat donusu sicakligi | 80 C | Standart kondensat sistemi |
| Kondensat geri donus orani | %75 | Endustriyel ortalama |
| Yillik calisma saati | 7,500 saat/yil | Surekli proses tesisi |

## Sektorel Uygulamalar

### Seker Endustrisi

Turkiye'deki seker fabrikalari tipik konfigurasyonu:
- Kazan: 40-60 bar, biyokutle / dogalgaz yakitli
- Turbin: 5-15 MW karsi basincli
- Cikis: 2-4 bar proses buhari
- Kullanim: Evaporatorler, kristalizasyon, kurutma
- Kampanya donemi: 90-120 gun, %95+ yuk faktoru
- HPR: 6-10

### Kagit ve Seluloz Endustrisi

- Kazan: 40-80 bar, siyah likir (black liquor) + dogalgaz
- Turbin: 10-50 MW karsi basincli veya cekisli
- Cikis: 3-6 bar proses buhari
- Kullanim: Kurutma silindirleri, pismis hamur isitma
- Surekli calisma: 8,000+ saat/yil
- HPR: 4-7

### Kimya Endustrisi

- Kazan: 40-100 bar, dogalgaz / fuel oil
- Turbin: 5-30 MW karsi basincli
- Cikis: 5-40 bar (proses kosuluna bagli)
- Kullanim: Reaksyon isitmasi, distilasyon
- HPR: 3-6

## Avantajlar ve Dezavantajlar

### Avantajlar

- **Yuksek toplam verim:** %80-92 toplam enerji verimi (elektrik + isi)
- **Basit yapi:** Kondenser gerektirmez, sogutma suyu sistemi yok
- **Dusuk yatirim maliyeti:** Yogusmali turbine gore %30-50 daha ucuz
- **Surekli proses buhari:** Prosese sabit basincli buhar saglar
- **Ekstra yakit tuketimi yok:** Mevcut kazan buharini kullaniyor, ek yakit yok
- **Dusuk bakim maliyeti:** Yas buhar bolgesine girilmez, kanat erozyonu az

### Dezavantajlar

- **Dusuk elektrik verimi:** %15-25, yogusmali turbinin yarisinin altinda
- **Buhar-bagli uretim:** Elektrik uretimi proses buhar talebine baglidir
- **Esneklik kisitlamasi:** HPR sabittir, proses degistikce elektrik degisir
- **Kapanma riski:** Proses durursa turbin de durur (bypass PRV devreye girer)
- **Fazla buhar sorunu:** Yaz aylarinda isitma yukunde dusus olursa fazla elektrik uretilmesi icin buhar kondenserden atilmasi gerekir (verimsiz)

## Dikkat Edilecekler

1. **Giris kosullarinin optimize edilmesi:** Giris basinci ve sicakligi yukseldikce elektrik uretimi artar, ancak kazan maliyeti de artar. Optimal nokta ekonomik analizle belirlenir.
2. **Cikis basinci secimi:** Cikis basinci, prosesin minimum ihtiyacina gore belirlenmeli, gereksiz yuksek cikis basinci elektrik uretimini azaltir.
3. **PRV exergy kaybi:** Mevcut tesislerde buhar PRV'den geciriliyorsa, PRV yerine turbin yerlestirilmesi en yuksek oncelikli exergy iyilestirme firsatidir.
4. **Yuk profili eslesmesi:** Tesisin buhar yuk profili ile elektrik yuk profili uyumlu olmalidir. Uyumsuzluk durumunda cekisli turbin daha uygun olabilir.
5. **Kondensat geri donusu:** Yuksek kondensat geri donus orani (%80+) toplam sistem verimini onemli olcude arttirir.

## İlgili Dosyalar

- [Turbin Formulleri](../formulas.md) -- Exergy ve izentropik verim hesaplamalari
- [Benchmarklar](../benchmarks.md) -- Turbin verimlilik karsilastirma verileri
- [Cekisli Turbin](extraction.md) -- Ara cekisli turbin (daha esnek alternatif)
- [Yogusmali Turbin](condensing.md) -- Maksimum elektrik ureten turbin tipi
- [Mikro Turbin](micro_turbine.md) -- Kucuk olcekli PRV ikamesi
- [CHP Sistemleri](../systems/steam_turbine_chp.md) -- CHP konfigurasyonlari
- [Kazan Formulleri](../../boiler/formulas.md) -- Kazan verimi ve yakit exergy hesabi
- [Fabrika Kojenerasyon](../../factory/cogeneration.md) -- CHP temelleri

## Referanslar

1. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
2. Horlock, J.H. (2002). *Combined Power Plants*, Krieger Publishing.
3. Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Ed., McGraw-Hill.
4. Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Ed., Wiley.
5. ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
6. EU Directive 2012/27/EU. *Energy Efficiency Directive -- High Efficiency Cogeneration*.
7. Rosen, M.A. & Dincer, I. (2003). "Exergy-cost-energy-mass analysis of thermal systems and processes," *Energy Conversion and Management*, 44(10), 1633-1651.
8. Regulagadda, P. et al. (2010). "Exergy analysis of a thermal power plant with measured boiler and turbine losses," *Applied Thermal Engineering*, 30, 970-976.
9. Spirax Sarco. *The Steam and Condensate Loop*, 2nd Edition.
10. Turkiye Enerji Verimliligi Dernegi (ENVER). *Kojenerasyon Sistemleri Rehberi*.
