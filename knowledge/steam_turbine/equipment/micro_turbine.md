---
title: "Mikro Turbin — Micro Turbine (<1 MW)"
category: equipment
equipment_type: steam_turbine
subtype: "Mikro Türbin (Micro Turbine)"
keywords: [mikro turbin, micro turbine, PRV ikamesi, PRV replacement, kucuk CHP, modüler CHP, tek kademe, radyal turbin, exergy, basinc dusurme]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/orc.md, steam_turbine/economics/feasibility.md, steam_turbine/systems/steam_turbine_chp.md, factory/waste_heat_recovery.md, factory/cogeneration.md]
use_when: ["PRV ikamesi degerlendirilirken", "Kucuk olcekli guc uretimi analiz edilirken", "Mikro CHP fizibilite calismalarinda", "50 kW - 1 MW araliginda turbin seciminde"]
priority: medium
last_updated: 2026-02-02
---
# Mikro Turbin — Micro Turbine (<1 MW)

> Son guncelleme: 2026-02-02

## Genel Bilgiler

Mikro turbinler (micro turbines), 50 kW ile 1 MW arasinda elektrik gucu ureten kucuk
olcekli buhar turbinleridir. Endustriyel tesislerde basinc dusurme vanalari (PRV —
Pressure Reducing Valve) yerine kullanilarak, mevcut buhar sistemlerindeki basinc
dusurmesinden elektrik enerjisi geri kazanimi saglarlar. Bu yaklasim, ek yakit tuketimi
gerektirmeden mevcut buhar altyapisini enerji uretim kaynagina donusturur.

- **Tip:** Mikro buhar turbini (micro steam turbine)
- **Kapasite araligi:** 50 kW - 1 MW elektrik
- **Giris kosullari:** 6 - 40 bar, 160 - 400 C (doymus veya kizgin buhar)
- **Cikis basinci:** 0.5 - 10 bar (proses gereksinimlerine bagli)
- **Izentropik verim:** %55 - 72 (boyut ve kademe sayisina bagli)
- **Exergy verimi (is bazli):** %50 - 68
- **Mekanik verim:** %95 - 98
- **Jenerator verimi:** %93 - 97
- **Kademe sayisi:** 1 - 5 (tipik: 1-2 kademe)
- **Yaygin markalar:** Siemens (SST-040/060), Triveni (TG series), Dresser-Rand, Green Turbine, Turboden (Steam), Eneftech, Alphabet Energy
- **Standartlar:** API 611 (genel amacli), API 612 (ozel amacli), IEC 60045-1

## PRV Ikamesi (PRV Replacement)

### PRV'nin Exergy Problemi

Endustriyel buhar sistemlerinde PRV, yuksek basincli buhari proses basincina
dusururken izentalpik (h_giris = h_cikis) genisleme gerceklestirir. Bu islemde
basinc duserken entropi artar ve exergy yok edilir. Oysa ayni basinc dusumunu
bir turbin uzerinden gerceklestirmek mumkundur; turbin, basinc farkini mekanik
ise (ve dolayisiyla elektrige) donusturur.

> **Kilit Kavram:** PRV izentalpik genisler (h sabit, s artar, exergy yok olur).
> Turbin ise izentropige yakin genisler (h duser, s yaklasik sabit, exergy
> ise donusur). Ayni islevi goren iki cihaz arasindaki fark, saf exergy
> kazanci veya kaybidir.

### PRV vs Mikro Turbin Kurulum Semasi

```
MEVCUT DURUM — PRV ile basinc dusurme:

  Kazan Cikisi        PRV          Proses Hatti
  (Yuksek Basinc)    (Kayip!)     (Dusuk Basinc)
  =================[PRV]===================>
  P1 = 10 bar                    P2 = 2 bar
  h1 = 2,778 kJ/kg              h2 = 2,778 kJ/kg  (izentalpik!)
  s1 = 6.586 kJ/(kg.K)          s2 = 7.059 kJ/(kg.K) (entropi ARTAR)
  T1 = 180 C (doymus)           T2 = 152 C (kizgin)

  Exergy kaybi = m_dot x T0 x (s2 - s1)
               = m_dot x 298.15 x (7.059 - 6.586)
               = m_dot x 141 kJ/kg  --> SAF KAYIP!


IYILESTIRILMIS DURUM — Mikro turbin ile guc uretimi:

  Kazan Cikisi     Mikro Turbin      Proses Hatti
  (Yuksek Basinc)  [Jenerator]      (Dusuk Basinc)
  =================[TURBIN]~~~~~=======>
  P1 = 10 bar       |  W_elek       P2 = 2 bar
  h1 = 2,778 kJ/kg  |               h2 = 2,543 kJ/kg
  s1 = 6.586        |               s2 = 6.894 kJ/(kg.K)
                     v
                  Elektrik
                  Sebekesi

  Turbin guc uretimi = m_dot x (h1 - h2) x eta_mek x eta_jen
  Exergy kaybi (turbin) << Exergy kaybi (PRV)

  PRV BYPASS (emniyet icin mevcut kalir):
  =================[PRV]===================>
        (Normal: kapali, turbin arizasinda: acik)
```

### PRV Ikamesi Ekonomik Hesaplama

```
Tipik PRV ikamesi ekonomik degerlendirmesi:

Veriler:
  m_dot = 5 ton/h = 1.389 kg/s
  P_giris = 10 bar (doymus buhar)
  P_cikis = 2 bar
  eta_is = 0.65 (tek kademe mikro turbin)
  eta_mek = 0.97, eta_jen = 0.95
  Calisma suresi = 7,500 saat/yil
  c_elektrik = 0.12 EUR/kWh

Termodinamik hesap:
  h_giris = 2,778 kJ/kg (10 bar doymus buhar)
  s_giris = 6.586 kJ/(kg.K)
  h_cikis,is = 2,530 kJ/kg (2 bar, izentropik)
  h_cikis = 2,778 - 0.65 x (2,778 - 2,530) = 2,617 kJ/kg

Turbin gucu:
  W_turbin = 1.389 x (2,778 - 2,617) = 224 kW
  W_elek = 224 x 0.97 x 0.95 = 206 kW

Yillik uretim:
  E_yillik = 206 x 7,500 = 1,545,000 kWh/yil

Yillik tasarruf:
  Tasarruf = 1,545,000 x 0.12 = 185,400 EUR/yil

Yatirim (mikro turbin + jenerator + montaj):
  Yatirim = 206 kW x 2,000 EUR/kW = 412,000 EUR

Basit geri odeme:
  PBP = 412,000 / 185,400 = 2.2 yil

  --> Cok karli bir yatirim!
```

## Moduler Mikro-CHP (Modular Micro-CHP)

### Mikro-CHP Kavrami

Mikro turbinler, kucuk olcekli kojenerasyon (CHP — Combined Heat and Power)
sistemlerinin temel bilesenlerinden biridir. Moduler yapilar sayesinde mevcut
kazan altyapisina entegre edilebilir ve hem elektrik hem de proses buhari
saglarlar.

### Tipik Mikro-CHP Konfigurasyonlari

| Konfigürasyon | Kapasite [kWe] | HPR | Uygulama |
|---------------|:--------------:|:---:|----------|
| Tek kazan + mikro turbin | 50 - 300 | 8 - 15 | Kucuk fabrika, hastane |
| Coklu kazan + mikro turbin | 200 - 800 | 5 - 10 | Orta olcekli tesis |
| Biyokutle kazan + mikro turbin | 100 - 500 | 6 - 12 | Tarim, orman urunleri |
| Bolge isitma + mikro turbin | 200 - 1,000 | 4 - 8 | Sehir bolgesi isitma |

### Bolge Isitma Entegrasyonu (District Heating)

```
Bolge isitma sistemlerinde mikro turbin kullanimi:

  Merkez Kazan (10-20 bar)
       |
  [Mikro Turbin] --> Elektrik (200-500 kW)
       |
  Cikis: 2-4 bar buhar
       |
  [Isi Degistirici] --> Sicak su (80-90 C)
       |
  Bolge Isitma Sebekesi
       |
  Bina Isinmalari

Avantajlar:
- Mevcut kazan altyapisi kullanilir
- Ek yakit tuketimi yok (mevcut isi icinden guc uretimi)
- Dusuk yatirim maliyeti
- Modüler yapilanma (taleple birlikte buyume)
```

## Turbin Tipleri (Turbine Types)

### Tek Kademe vs Cok Kademe (Single-Stage vs Multi-Stage)

| Ozellik | Tek Kademe | Cok Kademe (2-5) |
|---------|:----------:|:----------------:|
| Kapasite | 50 - 300 kW | 200 kW - 1 MW |
| Izentropik verim | %55 - 65 | %62 - 72 |
| Basinc orani (P1/P2) | 2 - 5 | 3 - 20 |
| Maliyet [EUR/kW] | 1,500 - 2,500 | 2,000 - 3,000 |
| Karmasiklik | Dusuk | Orta |
| Bakim gereksinimi | Az | Orta |
| Tipik uygulama | PRV ikamesi | Kucuk CHP |

### Aksiyal vs Radyal (Axial vs Radial)

| Ozellik | Aksiyal Turbin | Radyal Turbin (IFR) |
|---------|:--------------:|:-------------------:|
| Kapasite araligi | 200 kW - 1 MW+ | 50 - 500 kW |
| Izentropik verim | %60 - 72 | %55 - 68 |
| Basinc orani | 2 - 10 | 2 - 6 |
| Boyut | Orta | Kompakt |
| Rotor yapisi | Kanatli disk | Radyal impeller |
| Maliyet | Orta-yuksek | Dusuk-orta |
| Avantaj | Yuksek verim | Kompakt, ucuz |
| Dezavantaj | Karmasik kanat | Dusuk verim (buyuklerde) |

> **Not:** 200 kW altinda radyal (IFR — Inward Flow Radial) turbinler maliyet ve
> kompaktlik acisindan avantajlidir. 200 kW uzerinde aksiyal turbinler daha yuksek
> verim saglar.

### Impuls vs Reaksiyon (Impulse vs Reaction)

```
Kucuk olcekli turbinlerde akis tipleri:

IMPULS TURBIN (Curtis veya de Laval):
- Basinc dususu tamamen nozulda (stator) gerceklesir
- Rotor kanatlarinda sadece hiz yonu degisir
- Avantaj: Basit yapilanma, tek kademe ile yuksek basinc orani
- Tipik kullanim: <300 kW PRV ikamesi
- Verim: %55-65 (tek kademe Curtis)

REAKSIYON TURBIN:
- Basinc dususu hem stator hem rotorda gerceklesir
- Genellikle %50 reaksiyon derecesi (parsons tipi)
- Avantaj: Daha yuksek verim (cok kademede)
- Tipik kullanim: 300 kW - 1 MW
- Verim: %62-72 (cok kademe)

Kural: Kucuk kapasitede impuls, buyuk kapasitede reaksiyon tercih edilir.
```

## Exergy Analizi (Exergy Analysis)

### Exergy Yikim Kaynaklari

Mikro turbinlerde exergy yikimi, buyuk turbinlere kiyasla oransal olarak
daha yuksektir cunku kucuk boyutlarda aerodinamik kayiplar ve sizinti kayiplari
toplam debiye oranla daha buyuktur.

| Exergy Yikim Kaynagi | Mikro Turbin [%] | Buyuk Turbin [%] | Aciklama |
|----------------------|:----------------:|:----------------:|----------|
| Kanat profil kayiplari (blade profile) | 5 - 10 | 2 - 4 | Dusuk Reynolds sayisi etkisi |
| Kanat ucu sizintisi (tip leakage) | 3 - 8 | 1 - 3 | Oransal olarak buyuk bosluk |
| Ikincil akis kayiplari (secondary flow) | 2 - 5 | 1 - 2 | Kucuk kanat yuksekligi |
| Nozul kayiplari | 2 - 4 | 1 - 2 | Kucuk nozul boyutu |
| Mekanik kayiplar (bearings, seals) | 2 - 5 | 0.5 - 1 | Sabit kayip / kucuk guc |
| Nem kayiplari (varsa) | 0 - 2 | 0 - 1 | Doymus buhar girisinde |
| **Toplam exergy yikim orani** | **15 - 30** | **5 - 12** | |

### Izentropik Verim vs Exergy Verimi

```
Mikro turbin icin izentropik verim ve exergy verimi iliskisi:

Izentropik verim:
eta_is = (h_giris - h_cikis) / (h_giris - h_cikis,is)

Turbin exergy verimi (is bazli):
eta_ex = W_turbin / (Ex_giris - Ex_cikis)
       = m_dot x (h_giris - h_cikis) / [m_dot x ((h_giris - h_cikis) - T0 x (s_giris - s_cikis))]

Iliskisi:
- Kucuk turbinlerde eta_ex genellikle eta_is'den %3-8 daha dusuktur
- Bunun nedeni: Mekanik kayiplar, sizinti kayiplari (exergy dengesi icinde)
- Buyuk turbinlerde bu fark %1-3'e duser

Tipik degerler:
| Kapasite [kW] | eta_is [%] | eta_ex (is bazli) [%] | Fark [%] |
|:-------------:|:----------:|:---------------------:|:--------:|
| 50            | 55         | 48                    | 7        |
| 100           | 60         | 54                    | 6        |
| 200           | 63         | 58                    | 5        |
| 500           | 68         | 63                    | 5        |
| 1,000         | 72         | 68                    | 4        |
```

### Ornek Exergy Hesaplamasi — 200 kW Mikro Turbin (PRV Ikamesi)

```
Senaryo: 200 kW mikro turbin, 10 bar --> 2 bar PRV ikamesi

Referans kosullari:
  T0 = 25 C = 298.15 K
  h0 = 104.89 kJ/kg
  s0 = 0.3674 kJ/(kg.K)

Giris (10 bar, doymus buhar):
  h_giris = 2,778 kJ/kg
  s_giris = 6.586 kJ/(kg.K)
  ex_giris = (2,778 - 104.89) - 298.15 x (6.586 - 0.3674)
           = 2,673.1 - 1,853.8 = 819.3 kJ/kg

Izentropik cikis (2 bar, s = 6.586):
  h_cikis,is = 2,530 kJ/kg

Gercek cikis (eta_is = 0.63):
  h_cikis = 2,778 - 0.63 x (2,778 - 2,530) = 2,778 - 156.2 = 2,621.8 kJ/kg
  s_cikis = 6.876 kJ/(kg.K) (CoolProp ile)
  ex_cikis = (2,621.8 - 104.89) - 298.15 x (6.876 - 0.3674)
           = 2,516.9 - 1,940.2 = 576.7 kJ/kg

Buhar debisi (200 kW elektrik icin):
  eta_mek = 0.97, eta_jen = 0.95
  W_turbin = W_elek / (eta_mek x eta_jen) = 200 / (0.97 x 0.95) = 217 kW
  m_dot = W_turbin / (h_giris - h_cikis) = 217 / (2,778 - 2,621.8) = 1.39 kg/s = 5.0 ton/h

Exergy dengesi:
  Ex_giris = 1.39 x 819.3 = 1,139 kW
  Ex_cikis = 1.39 x 576.7 = 802 kW
  W_turbin = 217 kW
  Ex_yikim = 1,139 - 802 - 217 = 120 kW

Turbin exergy verimi (is bazli):
  eta_ex = W_turbin / (Ex_giris - Ex_cikis)
         = 217 / (1,139 - 802)
         = 217 / 337 = %64.4

PRV senaryosunda exergy kaybi:
  Ex_kayip_PRV = m_dot x T0 x (s_PRV_cikis - s_giris)
  PRV cikisi: h = 2,778 kJ/kg (izentalpik), P = 2 bar
  s_PRV_cikis = 7.059 kJ/(kg.K)
  Ex_kayip_PRV = 1.39 x 298.15 x (7.059 - 6.586)
               = 1.39 x 298.15 x 0.473
               = 196 kW

Karsilastirma:
  PRV exergy kaybi:    196 kW (tamamen kayip)
  Turbin exergy yikimi: 120 kW (tersinmezlik)
  Turbin elektrik:      200 kW (fayda)
  Net exergy kazanci:   200 - (196 - 120) = 200 kW elektrik + 76 kW daha az kayip

Sonuc: Mikro turbin hem 200 kW elektrik uretir hem de sistemdeki
toplam exergy yikimini azaltir.
```

## Boyutlandirma (Sizing)

### Buhar Debisi Hesaplamasi

```
Mikro turbin boyutlandirma adimlari:

Adim 1: Mevcut PRV debisini belirle
  m_dot = Q_proses / (h_proses - h_kondensat)   [kg/s]

Adim 2: Mevcut entalpi dusumunu hesapla
  Delta_h_is = h_giris - h_cikis,is   [kJ/kg]

Adim 3: Turbin gucunu hesapla
  W_elek = m_dot x Delta_h_is x eta_is x eta_mek x eta_jen   [kW]

Adim 4: Uygun turbin boyutunu sec
  - W_elek < 100 kW: Tek kademe radyal veya impuls
  - 100 < W_elek < 300 kW: Tek kademe aksiyal veya 2 kademe
  - 300 < W_elek < 1,000 kW: 2-5 kademe aksiyal

Adim 5: Ekonomik degerlendirme
  PBP = Yatirim / (W_elek x calisma_saati x c_elektrik)   [yil]
```

### Turbin Secim Kriterleri

| Parametre | Minimum | Onerilir | Aciklama |
|-----------|:-------:|:--------:|----------|
| Buhar debisi | 0.5 ton/h | > 2 ton/h | Ekonomik fizibilite icin |
| Basinc orani (P1/P2) | 1.5 | 3 - 10 | Yeterli entalpi dusumu icin |
| Giris basinci | 4 bar | > 8 bar | Makul guc uretimi icin |
| Calisma suresi | 4,000 saat/yil | > 6,000 saat/yil | Geri odeme icin |
| Minimum guc | 30 kW | > 100 kW | Ekonomik olarak anlamli |

### Yatirim Maliyeti

| Kapasite [kW] | Spesifik Maliyet [EUR/kW] | Toplam Maliyet [EUR] | Not |
|:-------------:|:-------------------------:|:--------------------:|-----|
| 50 | 2,500 - 3,500 | 125,000 - 175,000 | Mikro (radyal/impuls) |
| 100 | 2,000 - 3,000 | 200,000 - 300,000 | Kucuk tek kademe |
| 200 | 1,800 - 2,500 | 360,000 - 500,000 | Tek/iki kademe |
| 500 | 1,500 - 2,200 | 750,000 - 1,100,000 | Cok kademe |
| 1,000 | 1,200 - 1,800 | 1,200,000 - 1,800,000 | Sinir: buyuk turbine gecis |

> **Not:** Maliyetler turbin, jenerator, kontrol paneli, bypass PRV ve montaj dahil
> 2025-2026 Avrupa piyasa fiyatlaridir. Elektrik baglantisi ve muhendislik ayri
> fiyatlandirilir. Tipik EPC (mühendislik, tedarik, montaj) carpani: x 1.3-1.5.

### Geri Odeme Suresi Haritasi

```
Mikro turbin geri odeme suresi (yil) — kapasite ve elektrik fiyatina gore:

Elektrik Fiyati -->  0.08 EUR/kWh  0.10 EUR/kWh  0.12 EUR/kWh  0.15 EUR/kWh
Kapasite [kW]
     50               5.5 - 7.0     4.5 - 5.5     3.5 - 4.5     2.8 - 3.5
    100               4.0 - 5.5     3.2 - 4.5     2.7 - 3.5     2.1 - 2.8
    200               3.0 - 4.5     2.5 - 3.5     2.0 - 3.0     1.6 - 2.4
    500               2.5 - 3.5     2.0 - 2.8     1.7 - 2.3     1.3 - 1.8
  1,000               2.0 - 3.0     1.6 - 2.5     1.3 - 2.0     1.0 - 1.6

Varsayimlar: 7,500 saat/yil calisma, eta_is = %63, isletme maliyeti = %2 yatirim
```

## Sektorel Uygulamalar (Industrial Applications)

### Gida Endustrisi (Food Industry)

```
Tipik gida tesisi mikro turbin uygulamasi:

Kazan: 10-15 bar doymus buhar, dogalgaz yakitli
Proses: 2-4 bar buhar (pisiriciler, pastorizatorler, kurutucular)
Buhar debisi: 3-10 ton/h
Turbin kapasitesi: 80-300 kW
Calisma suresi: 5,000-6,500 saat/yil (mevsimsel uretim)
Geri odeme: 2.5-4.5 yil

Ozel durumlar:
- Mevsimsel uretim: Yaz aylarinda dusuk yuk (konserve, meyve suyu)
- Hijyen gereksinimleri: Buhar kalitesi prosesin onunde gelir
- Sogutma entegrasyonu: Turbin cikis buhari absorpsiyon chiller besleyebilir
```

### Kagit Endustrisi (Paper Industry)

```
Tipik kagit tesisi mikro turbin uygulamasi:

Kazan: 15-25 bar kizgin buhar
Proses: 3-6 bar buhar (kurutma silindirleri)
Buhar debisi: 5-20 ton/h
Turbin kapasitesi: 200-800 kW
Calisma suresi: 7,500-8,500 saat/yil (surekli proses)
Geri odeme: 2.0-3.5 yil

Ozel durumlar:
- Yuksek yuk faktoru: Surekli calisma, kisa duruslar
- Sabit buhar talebi: Kurutma silindiri yukü kararli
- Buyuk tesislerde birden fazla mikro turbin paralel kurulum
```

### Kimya Endustrisi (Chemical Industry)

```
Tipik kimya tesisi mikro turbin uygulamasi:

Kazan: 15-40 bar kizgin buhar
Proses: 4-15 bar buhar (reaktorler, distilasyon)
Buhar debisi: 3-15 ton/h
Turbin kapasitesi: 150-700 kW
Calisma suresi: 7,000-8,500 saat/yil
Geri odeme: 2.0-4.0 yil

Ozel durumlar:
- Yuksek basinc orani (esnek): Birden fazla basinc kademesi mumkun
- Proses guvenligi: Bypass PRV zorunlu, otomatik gecis kritik
- Korozif ortam: Malzeme secimi onemli (paslanmaz celik gerekliligi)
```

### Sektorel Parametre Ozeti

| Sektor | Giris [bar] | Cikis [bar] | Debi [ton/h] | Guc [kW] | Calisma [h/yil] | PBP [yil] |
|--------|:-----------:|:-----------:|:------------:|:--------:|:----------------:|:---------:|
| Gida | 10 - 15 | 2 - 4 | 3 - 10 | 80 - 300 | 5,000 - 6,500 | 2.5 - 4.5 |
| Kagit | 15 - 25 | 3 - 6 | 5 - 20 | 200 - 800 | 7,500 - 8,500 | 2.0 - 3.5 |
| Kimya | 15 - 40 | 4 - 15 | 3 - 15 | 150 - 700 | 7,000 - 8,500 | 2.0 - 4.0 |
| Tekstil | 10 - 15 | 2 - 4 | 3 - 8 | 80 - 250 | 5,500 - 7,000 | 2.5 - 4.0 |
| Hastane/Otel | 6 - 10 | 1 - 3 | 1 - 5 | 30 - 150 | 4,000 - 6,000 | 3.5 - 5.5 |
| Bolge isitma | 10 - 20 | 2 - 4 | 5 - 15 | 200 - 600 | 4,500 - 6,000 | 2.5 - 4.0 |

## Karsilastirma Tablosu — Mikro Turbin vs ORC vs PRV

| Parametre | Mikro Turbin | ORC | PRV (mevcut) |
|-----------|:------------:|:---:|:------------:|
| Kapasite araligi | 50 kW - 1 MW | 5 kW - 5 MW | -- (guc yok) |
| Kaynak tipi | Buhar (basinc fark) | Herhangi isi kaynagi | Buhar |
| Kaynak sicakligi | 150 - 400 C | 80 - 350 C | 150 - 400 C |
| Elektrik uretimi | Evet | Evet | Hayir |
| Izentropik verim | %55 - 72 | %60 - 85 (expander) | -- |
| Yatirim maliyeti [EUR/kW] | 1,200 - 3,500 | 1,500 - 6,000 | 500 - 2,000 (salt PRV) |
| Geri odeme suresi | 1.5 - 5 yil | 3 - 7 yil | -- |
| Bakim maliyeti | Dusuk-orta | Dusuk | Cok dusuk |
| Karmasiklik | Dusuk | Orta-yuksek | Cok dusuk |
| Su ihtiyaci | Mevcut buhar sistemi | Kapali cevrim (az) | Mevcut buhar sistemi |
| Mevcut sisteme uyum | Cok iyi (drop-in) | Zor (ayri cevrim) | Mevcut |
| Proses buhar kalitesi | Korunur | Etkilenmez | Korunur |
| Exergy kazanimi | Yuksek | Orta-yuksek | Sifir (kayip) |
| Tipik uygulama | PRV ikamesi | Atik isi degerlendirme | Basinc dusurme |

> **Karar Kurali:**
> - Mevcut buhar hatti ve PRV varsa: **Mikro turbin** (en dusuk maliyet, en hizli geri odeme)
> - Dusuk sicaklik atik isi varsa (<200 C): **ORC** (buhar icermeyen kaynak)
> - Yuksek sicaklik atik isi + buhar sistemi yoksa: **ORC**
> - Buhar debisi < 0.5 ton/h veya calisma < 4,000 saat/yil: **PRV** (yatirim fizibil degil)

## Varsayilan Degerler (Olcum Yoksa)

| Parametre | Varsayilan | Aciklama |
|-----------|:---------:|----------|
| Giris basinci | 10 bar | Tipik endustriyel orta basinc |
| Giris sicakligi | Doymus buhar | Conservatif (kizginlik yoksa) |
| Cikis basinci | 2 bar | Tipik proses basinci |
| Izentropik verim | %63 | Tek kademe, kucuk turbin |
| Mekanik verim | %97 | Standart yatak kaybi |
| Jenerator verimi | %95 | Kucuk jenerator |
| Yillik calisma saati | 7,000 saat/yil | Surekli proses varsayimi |
| Isletme maliyeti | Yatirimin %2'si | Yillik bakim |
| Elektrik fiyati | 0.12 EUR/kWh | Turkiye endustriyel tarife |
| Referans sicakligi (T0) | 25 C | Standart cevre kosulu |

## Dikkat Edilecekler

1. **Buhar kalitesi:** Giris buharinin nemi %12'yi asarsa (x < 0.88) kanat erozyonu riski artar. Doymus buhar girisinde nem ayirici (moisture separator) onerisi degerlendirilmelidir.

2. **Basinc orani siniri:** Tek kademe turbinlerde P1/P2 > 6 icin verim hizla duser. Yuksek basinc oranlari icin cok kademe tercih edilmelidir.

3. **Minimum debi:** 0.5 ton/h altindaki debilerde mikro turbin ekonomik olarak fizibil degildir. Bu durumda mevcut PRV korunmalidir.

4. **Bypass zorunlulugu:** Mikro turbin ariza veya bakim icin devre disi kaldiginda, proses buhari kesintisiz saglanmalidir. Otomatik PRV bypass her zaman mevcut olmalidir.

5. **Elektrik baglantisi:** Jenerator cikisinin sebekeye paralel baglantisi icin senkronizasyon paneli gereklidir. Enerji yonetmeligi kapsaminda dagitim sirketi ile baglanti anlasmasi yapilmalidir.

6. **Titresim ve gurultu:** Mikro turbinler yuksek devir sayisinda calisir (3,000 - 12,000 rpm). Yatak, temel ve gurultu izolasyonu projelendirilmelidir.

## İlgili Dosyalar

- [Turbin Formulleri](../formulas.md) -- Exergy ve izentropik verim hesaplamalari
- [Benchmarklar](../benchmarks.md) -- Turbin verimlilik karsilastirma verileri
- [Karsi Basincli Turbin](back_pressure.md) -- Buyuk olcekli karsi basincli turbin
- [ORC](orc.md) -- Dusuk sicaklik alternatifi
- [Yogusmali Turbin](condensing.md) -- Maksimum elektrik uretimi
- [CHP Sistemleri](../systems/steam_turbine_chp.md) -- CHP konfigurasyonlari
- [Fizibilite](../economics/feasibility.md) -- Ekonomik degerlendirme
- [Atik Isi Geri Kazanimi](../../factory/waste_heat_recovery.md) -- Fabrika seviyesinde WHR
- [Kojenerasyon](../../factory/cogeneration.md) -- CHP temelleri ve karsilastirma
- [Kazan Atik Isi](../../boiler/equipment/waste_heat.md) -- Atik isi kazani bilgisi

## Referanslar

1. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
2. Horlock, J.H. (1966). *Axial Flow Turbines*, Butterworths.
3. Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Edition, Wiley.
4. Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
5. API 612 (2005). *Petroleum, Petrochemical and Natural Gas Industries -- Steam Turbines -- Special-Purpose Applications*, API.
6. API 611 (2008). *General-Purpose Steam Turbines for Petroleum, Chemical and Gas Industry Services*, API.
7. US DOE (2012). *Improving Steam System Performance -- A Sourcebook for Industry*, 2nd Edition, US Department of Energy.
8. Spirax Sarco. *The Steam and Condensate Loop*, 2nd Edition.
9. Varbanov, P.S. et al. (2017). "Efficiency evaluation and retrofit design of steam turbine systems," *Applied Thermal Engineering*, 124, 951-960.
10. Moran, M.J. et al. (2018). *Fundamentals of Engineering Thermodynamics*, 9th Edition, Wiley.
11. Rosen, M.A. & Dincer, I. (2003). "Exergy-cost-energy-mass analysis of thermal systems and processes," *Energy Conversion and Management*, 44(10), 1633-1651.
12. Tsatsaronis, G. & Morosuk, T. (2012). "Advanced exergy-based methods used to understand and improve energy-conversion systems," *Energy*, 45, 407-413.
