---
title: "Ara Cekisli Buhar Turbini — Extraction Steam Turbine"
category: equipment
equipment_type: steam_turbine
subtype: "Ara Cekisli (Extraction)"
keywords: [cekisli turbin, extraction, kontollu cekis, HP-LP kademe, Willans cizgisi, esnek CHP, exergy]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/condensing.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/solutions/load_matching.md, factory/cogeneration.md]
use_when: ["Cekisli turbin analizi yapilirken", "Esnek CHP sistemi degerlendirilirken", "Degisken HPR gerektiginde", "Willans cizgisi ile kisa yol hesap yapilirken"]
priority: medium
last_updated: 2026-01-31
---
# Ara Cekisli Buhar Turbini — Extraction Steam Turbine

> Son guncelleme: 2026-01-31

## Genel Bilgiler

Ara cekisli (extraction) buhar turbinleri, turbin ici belirli bir noktadan (veya
birden fazla noktadan) buhar cekerek hem elektrik uretimi hem de proses buhari
saglanmasina olanak taniyan esnek turbin tipidir. Karsi basincli turbinin sabit
HPR kisitlamasini ortadan kaldirir; operasyonda elektrik ve isi oranini
bagimisiz olarak kontrol etme imkani sunar.

- **Tip:** Ara cekisli (extraction) turbin — kontollu veya kontrolsuz
- **Kapasite araligi:** 1 - 500 MW (endustriyel: tipik 2-50 MW)
- **Giris kosullari:** 20 - 170 bar, 350 - 540 C
- **Cekis basinci:** 2 - 40 bar (tek veya cift cekis)
- **Cikis basinci:** 0.03 - 15 bar (yogusmali veya karsi basincli)
- **Elektrik verimi:** %18 - 38 (cekis oranina ve cikis tipine bagli)
- **HPR (degisken):** 0 (tam yogusma) - 15+ (tam cekis)
- **Izentropik verim:** %72 - 88
- **Yaygin markalar:** Siemens, GE, MHI, Shin Nippon, Triveni, Dresser-Rand

## Calisma Prensibi

### Temel Konfigurasyonlar

```
1. EXTRACTION-CONDENSING (Cekis-Yogusmali):
   Giris buhari --> HP kademe --> CEKIS NOKTASI --> LP kademe --> Kondenser
                                      |
                                      +--> Proses buhari

   En yaygin tip. Cekis miktari degiskenidir.
   Tam yogusmada: HPR = 0 (tum buhar kondensere gider)
   Tam cekiste: Karsi basincli turbin gibi calisir.

2. EXTRACTION-BACK PRESSURE (Cekis-Karsi Basincli):
   Giris buhari --> HP kademe --> CEKIS (orta basinc) --> LP kademe --> LP proses
                                      |
                                      +--> MP proses buhari

   Iki farkli basinc seviyesinde proses buhari saglar.
   Ornegin: 10 bar cekis + 3 bar cikis.

3. DOUBLE EXTRACTION (Cift Cekisli):
   Giris --> HP --> 1. CEKIS --> IP --> 2. CEKIS --> LP --> Kondenser/BP
                       |                    |
                       +--> HP proses       +--> LP proses

   Iki farkli basinc seviyesinde cekis, en yuksek esneklik.
```

### Kontollu vs Kontrolsuz Cekis

| Ozellik | Kontollu Cekis | Kontrolsuz Cekis |
|---------|----------------|------------------|
| Basinc kontrolu | Cekis vanasi basinci sabit tutar | Basinc yuke gore degisir |
| Esneklik | Yuksek — bagimsiz kontrol | Dusuk — yuke bagli |
| Maliyet | Yuksek (kontrol valfi, akttuator) | Dusuk |
| Uygulama | Proses buhari gereken CHP | Feedwater isitma, deaerator |
| Exergy etkisi | Proses isi kalitesi korunur | Basinc/sicaklik degisken |

**Kontollu cekis** endustriyel CHP uygulamalarinin standart secenegidir.
Cekis vanasi (extraction valve), cekis noktasindaki basinci ayarlar.
HP kademesi cikisindaki buhar, cekis vanasi uzerinden prosese yonlenir
veya LP kademesine gecis yaptirilir.

## HP-LP Kademe Ayrimi

### Kademe Karakteristikleri

```
HP (High Pressure) Kademe:
- Giris: Turbin giris kosullari (yuksek basinc, kizgin buhar)
- Cikis: Cekis basinci
- Buhar debisi: Sabit (= turbin giris debisi)
- Is uretimi: W_HP = m_giris x (h_giris - h_cekis)

LP (Low Pressure) Kademe:
- Giris: Cekis basincinda buhar (cekis sonrasi kalan kisim)
- Cikis: Kondenser vakumu veya karsi basinc
- Buhar debisi: Degisken (= m_giris - m_cekis)
- Is uretimi: W_LP = (m_giris - m_cekis) x (h_cekis - h_cikis)

Toplam guc:
W_toplam = W_HP + W_LP
W_toplam = m_giris x (h_giris - h_cekis) + (m_giris - m_cekis) x (h_cekis - h_cikis)
```

### Kademe Guc Dagilimi Ornegi

```
Senaryo: 20 MW extraction-condensing turbin
Giris: 60 bar, 480 C
Cekis: 6 bar (kontollu)
Cikis: 0.06 bar (kondenser)
Giris debisi: 30 kg/s

Durum 1: Tam yogusma (cekis = 0)
  W_HP = 30 x (h_giris - h_cekis) = 30 x 420 = 12,600 kW
  W_LP = 30 x (h_cekis - h_cikis) = 30 x 560 = 16,800 kW
  W_toplam = 29,400 kW --> HPR = 0

Durum 2: %50 cekis (m_cekis = 15 kg/s)
  W_HP = 30 x 420 = 12,600 kW
  W_LP = 15 x 560 = 8,400 kW
  W_toplam = 21,000 kW
  Q_proses = 15 x (h_cekis - h_kondensat) = 15 x 2,360 = 35,400 kW
  HPR = 35,400 / 21,000 = 1.69

Durum 3: Tam cekis (m_cekis = 30 kg/s)
  W_HP = 30 x 420 = 12,600 kW
  W_LP = 0 kW
  W_toplam = 12,600 kW
  Q_proses = 30 x 2,360 = 70,800 kW
  HPR = 70,800 / 12,600 = 5.62
```

## Willans Cizgisi (Willans Line)

### Tanimi

Willans cizgisi, turbin buhar tuketiminin ise dogrusal bir yaklasim ile
ifade edilmesidir. Kismi yuk performansini hizli tahmin etmek icin kullanilir.

```
m_dot = a + b x W   [kg/s]

Burada:
- m_dot = turbin toplam buhar debisi [kg/s]
- W = turbin mekanik guc ciktisi [kW]
- a = bos calisma (no-load) buhar tuketimi [kg/s]
- b = artimsal buhar tuketimi [kg/(s.kW)] = 1/spesifik is

Willans parametreleri:
a = 0.08 - 0.12 x m_nominal  (tipik)
b = (m_nominal - a) / W_nominal

Dogrusal yaklasim gecerliligi: %30 - 100 yuk arasinda
%30 altinda dogrusalliktan sapma artar
```

### Cekisli Turbin Willans Cizgisi

Cekisli turbinde Willans cizgisi daha karmasiktir cunku iki
bagimsiz degisken vardir (cekis debisi ve guc):

```
m_giris = a + b_HP x W_HP + b_LP x W_LP

veya alternatif olarak:

W_toplam = f(m_giris, m_cekis)

Basitlestirilmis yaklasim (sabit cekis debisinde):
m_giris = a' + b' x W_toplam   (sabit m_cekis icin)

Bu yaklasim, her cekis debisi icin farkli bir Willans cizgisi verir.
```

### Willans Cizgisi Kullanim Ornegi

```
Verilen: 10 MW turbin, m_nominal = 20 kg/s

Willans parametreleri:
a = 0.10 x 20 = 2.0 kg/s
b = (20 - 2.0) / 10,000 = 0.0018 kg/(s.kW)

%70 yuk (7 MW):
m_dot = 2.0 + 0.0018 x 7,000 = 14.6 kg/s

Spesifik buhar tuketimi:
SSC_100% = 20 / 10,000 = 0.002 kg/(s.kW) = 7.2 kg/kWh
SSC_70% = 14.6 / 7,000 = 0.00209 kg/(s.kW) = 7.5 kg/kWh
(Kismi yukte SSC artar --> verim duser)
```

## Degisken HPR ve Esneklik Avantaji

### Isletme Zarfi (Operating Envelope)

```
Cekisli turbinin isletme zarfi, guc-isi diyagraminda gosterilir:

       Guc (W) [MW]
        |
   Wmax |___________
        |           \
        |            \  Tam yogusma
        |             \  cizgisi
        |              \
        |    ISLETME    \
        |    BOLGES1     \
        |                 \
   Wmin |_________________\___
        |                      Q_isi (MW)
        0                Q_max

Sinir kosullari:
1. Maksimum buhar debisi (m_max) --> ust sinir
2. Minimum buhar debisi (m_min) --> alt sinir
3. Tam yogusma cizgisi (m_cekis = 0) --> sol sinir
4. Tam cekis cizgisi (m_cekis = m_giris) --> sag sinir
5. Minimum LP debisi (LP kademesini sogutmak icin gerekli)
```

### Esneklik Karsilastirmasi

| Turbin Tipi | HPR | Elektrik Esnekligi | Isi Esnekligi | Uygunluk |
|-------------|-----|:------------------:|:-------------:|----------|
| Karsi basincli | Sabit (3-10) | Dusuk | Dusuk | Sabit yuk profili |
| Yogusmali | N/A | Yuksek | Yok | Yalniz elektrik |
| Cekisli-yogusmali | Degisken (0-15) | Yuksek | Yuksek | Degisken yuk profili |
| Cekisli-BP | Degisken (2-15) | Orta | Yuksek | Iki basinc seviyesi |

**Esneklik avantaji:** Cekisli turbin, mevsimsel ve gunluk yuk degisimlerine
uyum saglayabilir. Yaz aylarinda dusuk isi talebi olursa cekis azaltilir ve daha
fazla elektrik uretilir. Kis aylarinda yuksek isi talebi olursa cekis arttirilir.

## Condensing-Extraction Turbin

### Tasarim Ozellikleri

```
Extraction-condensing turbin, endustriyel CHP'nin en esnek cozumudur:

Avantajlar:
- Degisken HPR: 0 (tam yogusma) ile Yuksek (tam cekis) arasinda
- Elektrik ile isi bagimisiz kontrol edilebilir
- Proses durunca elektrik uretimi devam edebilir (tam yogusma)
- Mevsimsel yuk degisimlerine uyum

Dezavantajlar:
- En yuksek yatirim maliyeti (karsi basincli turbinden %50-100 fazla)
- Kondenser ve sogutma sistemi gerektirir
- Daha karmasik kontrol sistemi
- LP kademe boyutlandirmasi kritik (exhaust loss)

Karsi basincli turbinle karsilastirma:
- Karsi basincli: Ucuz, basit, ancak esneksiz
- Cekisli-yogusmali: Pahali, karmasik, ancak esnek
- Secim: Yuk profili degiskenligi belirler
```

## Exergy Analizi

### Cekisli Turbin Exergy Dengesi

```
Exergy girisi:
Ex_giris = m_giris x ex_giris   [kW]

Exergy cikislari:
Ex_is = W_turbin   [kW]  (saf exergy)
Ex_cekis = m_cekis x ex_cekis   [kW]
Ex_yogusma = m_yogusma x ex_cikis   [kW]

Exergy yikimi:
Ex_yikim = Ex_giris - Ex_is - Ex_cekis - Ex_yogusma

Exergy verimi (toplu):
eta_ex = (Ex_is + Ex_cekis) / Ex_giris

Exergy verimi (is bazli):
eta_ex_is = Ex_is / (Ex_giris - Ex_cekis - Ex_yogusma)
```

### Kademe Bazli Exergy Analizi

```
HP Kademe:
  Ex_giris_HP = m_giris x ex_giris
  Ex_cikis_HP = m_giris x ex_cekis_noktasi
  W_HP = m_giris x (h_giris - h_cekis)
  I_HP = Ex_giris_HP - Ex_cikis_HP - W_HP
  eta_ex_HP = W_HP / (Ex_giris_HP - Ex_cikis_HP)

LP Kademe:
  Ex_giris_LP = m_yogusma x ex_cekis_noktasi
  Ex_cikis_LP = m_yogusma x ex_cikis
  W_LP = m_yogusma x (h_cekis - h_cikis)
  I_LP = Ex_giris_LP - Ex_cikis_LP - W_LP
  eta_ex_LP = W_LP / (Ex_giris_LP - Ex_cikis_LP)

Not: Genellikle LP kademe exergy verimi, HP kademeden dusuktur
(yas buhar etkisi ve exhaust loss nedeniyle).
```

### Ornek Hesaplama

```
Senaryo: 15 MW extraction-condensing turbin
Giris: 40 bar / 400 C, m_giris = 25 kg/s
Cekis: 5 bar, m_cekis = 10 kg/s
Cikis: 0.06 bar, m_yogusma = 15 kg/s

Buhar durumlari:
  Giris: h = 3,214 kJ/kg, s = 6.769, ex = 1,200 kJ/kg
  Cekis: h = 2,855 kJ/kg, s = 7.060, ex = 755 kJ/kg
  Cikis: h = 2,220 kJ/kg, s = 7.530, ex = 42 kJ/kg

Guc:
  W_HP = 25 x (3,214 - 2,855) = 8,975 kW
  W_LP = 15 x (2,855 - 2,220) = 9,525 kW
  W_toplam = 18,500 kW

Exergy dengesi:
  Ex_giris = 25 x 1,200 = 30,000 kW
  Ex_cekis = 10 x 755 = 7,550 kW
  Ex_yogusma = 15 x 42 = 630 kW
  W_toplam = 18,500 kW
  Ex_yikim = 30,000 - 7,550 - 630 - 18,500 = 3,320 kW

Verimler:
  eta_ex_toplu = (18,500 + 7,550) / 30,000 = %86.8
  eta_ex_is = 18,500 / (30,000 - 7,550 - 630) = 18,500 / 21,820 = %84.8
  y_D = 3,320 / 30,000 = %11.1
```

## Performans Tablosu

| Parametre | Kucuk (2-10 MW) | Orta (10-50 MW) | Buyuk (50+ MW) |
|-----------|:--------------:|:----------------:|:--------------:|
| Giris basinci [bar] | 20 - 40 | 40 - 100 | 60 - 170 |
| Cekis basinci [bar] | 2 - 10 | 3 - 20 | 4 - 40 |
| Cikis (yogusmali) [mbar] | 50 - 100 | 40 - 70 | 30 - 50 |
| Izentropik verim [%] | 72 - 82 | 78 - 86 | 82 - 88 |
| HPR araligi | 0 - 10 | 0 - 12 | 0 - 15 |

## Varsayilan Degerler (Olcum Yoksa)

| Parametre | Varsayilan | Aciklama |
|-----------|:---------:|----------|
| Giris basinci | 40 bar | Tipik endustriyel CHP |
| Giris sicakligi | 400 C | 40 bar'a uygun kizginlik |
| Cekis basinci | 5 bar | Tipik proses basinci |
| Cikis basinci | 0.06 bar | Sogutma kuleli vakum |
| Cekis orani | %40 | m_cekis / m_giris |
| Izentropik verim (HP) | %80 | Orta olcekli turbin |
| Izentropik verim (LP) | %82 | Kademeli LP |
| Mekanik verim | %98 | Standart |
| Jenerator verimi | %97 | Standart |

## İlgili Dosyalar

- [Turbin Formulleri](../formulas.md) -- Exergy hesaplamalari, Willans cizgisi
- [Benchmarklar](../benchmarks.md) -- Turbin verimlilik karsilastirma verileri
- [Karsi Basincli Turbin](back_pressure.md) -- Sabit HPR alternatifi
- [Yogusmali Turbin](condensing.md) -- Maksimum elektrik alternati
- [Yuk Eslestirme](../solutions/load_matching.md) -- Termal/elektrik yuk optimizasyonu
- [CHP Sistemleri](../systems/steam_turbine_chp.md) -- CHP konfigurasyonlari
- [Kazan Formulleri](../../boiler/formulas.md) -- Kazan verimi hesabi
- [Fabrika Kojenerasyon](../../factory/cogeneration.md) -- CHP temelleri ve karsilastirma
- [Chiller Entegrasyonu](../../chiller/benchmarks.md) -- Absorpsiyon chiller ile CHP

## Referanslar

1. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
2. Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
3. Horlock, J.H. (2002). *Combined Power Plants*, Krieger Publishing.
4. Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Ed., McGraw-Hill.
5. ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
6. Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Ed., Wiley.
7. EU Directive 2012/27/EU. *Energy Efficiency Directive -- High Efficiency Cogeneration*.
8. Moran, M.J. et al. (2018). *Fundamentals of Engineering Thermodynamics*, 9th Ed., Wiley.
9. Spirax Sarco. *The Steam and Condensate Loop*, 2nd Edition.
