---
title: "Yardimci Denklemler (Auxiliary Equations — F-Rule & P-Rule)"
category: factory
equipment_type: factory
keywords: [yardimci denklem, F-kurali, P-kurali, sinir kosulu, dissipative, kojenerasyon, CHP, denklem sayisi, SPECO]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/fuel_product_definitions.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/exergoeconomic/matrix_formulation.md
use_when:
  - "Yardimci denklemler yazilirken"
  - "F-kurali veya P-kurali uygulanirken"
  - "Sinir kosullari belirlenmek istendiginde"
  - "Dissipative bilesen maliyet atamasi yapilirken"
  - "Denklem sayisi dogrulamasi yapilirken"
  - "Kojenerasyon (CHP) sistemi analiz edilirken"
priority: medium
last_updated: 2026-02-01
---
# Yardimci Denklemler (Auxiliary Equations -- F-Rule & P-Rule)

> Son guncelleme: 2026-02-01

## 1. Giris ve Motivasyon

Exergoekonomik analizde her bilesen icin bir maliyet denge denklemi (cost balance equation) yazilir. Ancak bir bilesenin birden fazla cikisi (veya birden fazla exergy farki) varsa, maliyet denge denklemi tek basina tum bilinmeyenleri cozmeye yetmez. Bu durumda **yardimci denklemler** (auxiliary equations) devreye girer.

SPECO metodunda yardimci denklemler iki sistematik kurala dayanir:

```
1. F-kurali (Fuel Rule): Yakit tarafindaki exergy farklari icin
2. P-kurali (Product Rule): Urun tarafindaki exergy farklari icin

Bu iki kural, denklem sistemini eksiksiz ve tutarli hale getirir.

Ek olarak:
3. Sinir kosullari (Boundary Conditions): Dis kaynak maliyetleri
4. Dissipative bilesen kurallari: Kondenser, valf gibi ozel durumlar
```

### 1.1 Neden Yardimci Denklemler Gereklidir?

Bir termal sistemde n adet akis (stream) varsa, n adet bilinmeyen birim exergy maliyeti (c_1, c_2, ..., c_n) belirlenmelidir. Maliyet denge denklemleri yalnizca bilesen sayisi (k) kadar denklem verir. Geriye kalan (n - k) bilinmeyen icin yardimci denklemler ve sinir kosullari gerekir.

```
Genel Formul:

n_bilinmeyen = n_akis + n_is_akisi
n_maliyet_dengesi = n_bilesen
n_eksik = n_bilinmeyen - n_maliyet_dengesi

Bu eksik denklemler su kaynaklardan tamamlanir:
  n_eksik = n_yardimci + n_sinir

Burada:
- n_yardimci = F-kurali ve P-kurali ile elde edilen denklem sayisi
- n_sinir = Bilinen dis kaynak maliyetleri (c_yakit, c_elektrik, c_cevre = 0)
```

## 2. F-Kurali (Fuel Rule) -- Detayli Aciklama

### 2.1 Temel Tanim

F-kurali, bir bilesenin Yakit (Fuel) exergy'sinin birden fazla exergy farkından olusması durumunda uygulanir. Kural su sekilde ifade edilir:

```
F-Kurali:
Bir bilesenin yakiti, bir akisin giris ve cikis exergy'si arasindaki
farktan olusuyorsa, bu akisin giristeki ve cikistaki birim exergy
maliyetleri esittir.

Matematiksel ifade:
  Yakit = E_i,giris - E_i,cikis  ise  =>  c_i,giris = c_i,cikis

Fiziksel anlam:
  Akiskanin bilesenden gecerken kaybettigi exergy'nin birim maliyeti,
  akiskanin bilesene girmeden onceki birim maliyetiyle aynidir.
  Bilesen yalnizca "miktar" tuketir, "kalite basina fiyati" degistirmez.
```

### 2.2 F-Kurali -- Fiziksel Gerekce

F-kuralinin temelinde su muhendislik mantigi yatar: Bir akiskan bir bilesene girdikten sonra exergy'sinin bir kismi tuketilir (yakit olarak). Bu tuketilen exergy'nin birim maliyeti, akiskanin taşıdıgı genel birim maliyet ile aynidir. Baska bir deyisle, bilesen exergy tuketirken "secici" degildir; exergy'nin turkce ifadesiyle "is yapabilme kapasitesini" homojen bicimde kullanir.

```
Ornek -- Su/buhar akisi turbin icerisinde genislerken:
  Giris:  T_1 = 500 degC, P_1 = 60 bar  =>  E_1 = 15,200 kW,  c_1 = ?
  Cikis:  T_2 = 200 degC, P_2 = 3 bar   =>  E_2 = 8,100 kW,   c_2 = ?

  Yakit:  E_F = E_1 - E_2 = 7,100 kW
  F-kurali: c_1 = c_2

  Anlam: Buhar genislerken birim exergy maliyeti degismez,
         yalnizca tasinan exergy miktari azalir.
```

### 2.3 F-Kurali Ornekleri -- Ekipman Tipine Gore

#### 2.3.1 Turbin (Turbine)

```
Turbin Akis Semasi:
                    ┌───────────┐
  Akis 1 (buhar) ──→│  TURBiN   │──→ Akis 2 (dusuk basinc buhar)
                    │           │──→ W_T (is cikisi)
                    └───────────┘

Yakit:  E_F = E_1 - E_2  (tek exergy farki)
Urun:   E_P = W_T

Maliyet dengesi:
  c_W · W_T + c_2 · E_2 = c_1 · E_1 + Z_T

Bilinmeyenler: c_1, c_2, c_W  (3 adet)
Denklem: 1 maliyet dengesi
Yardimci: 1 F-kurali gerekli

F-kurali: c_1 = c_2
  → Buhar turbinden gecerken birim maliyeti korur
  → Turbinin islevi exergy'yi ise donusturmektir, akiskani "pahalilaştirmak" degil
```

#### 2.3.2 Isi Degistirici (Heat Exchanger)

```
Isi Degistirici Akis Semasi:
                         ┌──────────────────┐
  Akis 1 (sicak giris) ──→│  ISI DEGiSTiRiCi  │──→ Akis 2 (sicak cikis)
  Akis 3 (soguk giris) ──→│                    │──→ Akis 4 (soguk cikis)
                         └──────────────────┘

Yakit:  E_F = E_1 - E_2  (sicak taraf exergy azalisi)
Urun:   E_P = E_4 - E_3  (soguk taraf exergy artisi)

Maliyet dengesi:
  c_2 · E_2 + c_4 · E_4 = c_1 · E_1 + c_3 · E_3 + Z_HX

Bilinmeyenler: c_1, c_2, c_3, c_4 (4 adet, ancak c_1 ve c_3 genellikle bilinen)
Yardimci: 1 F-kurali

F-kurali: c_1 = c_2
  → Sicak akiskan isi degistiricide sogurken birim maliyeti korur
  → Exergy kaybinin maliyeti, akiskanin tasidigi birim maliyetle orantilidir
```

#### 2.3.3 Kazan (Boiler) -- Baca Gazi Durumu

```
Kazan Akis Semasi:
                    ┌──────────┐
  Akis 5 (yakit) ──→│  KAZAN   │──→ Akis 1 (buhar cikisi)
  Akis 4 (su) ──→  │          │──→ Akis 6 (baca gazi)
  Akis 7 (hava) ──→│          │
                    └──────────┘

Yakit:  E_F = E_5 + E_7  (yakit + hava kimyasal exergy)
Urun:   E_P = E_1 - E_4  (buhar exergy artisi)
Kayip:  E_L = E_6  (baca gazi exergy kaybi)

Maliyet dengesi:
  c_1 · E_1 + c_6 · E_6 = c_5 · E_5 + c_4 · E_4 + c_7 · E_7 + Z_B

Baca gazi yakit tarafinda ise F-kurali:
  c_6 = c_5  (baca gazinin birim maliyeti yakit ile ayni)

Alternatif -- baca gazi atik kabul edilirse:
  c_6 = 0  (sinir kosulu, atik akisa maliyet yüklenmez)

Hangisini secmeli?
  → Baca gazi enerjisi geri kazaniliyorsa (ekonomizer): F-kurali (c_6 = c_5)
  → Baca gazi dogrudan atmosfere atiliyorsa: c_6 = 0
```

#### 2.3.4 Kompresor (Compressor) -- F-Kurali Gerekmez

```
Kompresor Akis Semasi:
                     ┌────────────┐
  W_C (is girisi) ──→│  KOMPRESOR │──→ Akis 2 (yuksek basinc gaz)
  Akis 1 (dusuk P) ──→│           │
                     └────────────┘

Yakit:  E_F = W_C  (tek akis, fark degil)
Urun:   E_P = E_2 - E_1

Maliyet dengesi:
  c_2 · E_2 = c_1 · E_1 + c_W · W_C + Z_C

Yardimci denklem gereksiz:
  → c_1 = 0 (cevreden cekilen hava) → sinir kosulu
  → c_W biliniyor (sebekeden gelen elektrik) → sinir kosulu
  → Tek bilinmeyen c_2, tek denklem yeterli

Not: Kompresor icin F-kurali UYGULANMAZ cunku yakit tek bir akistir (W_C),
     exergy farki degildir.
```

#### 2.3.5 Pompa (Pump) -- F-Kurali Gerekmez

```
Pompa Akis Semasi:
                  ┌────────┐
  W_P (is) ──→   │  POMPA │──→ Akis 2 (yuksek basinc sivi)
  Akis 1 (su) ──→│        │
                  └────────┘

Yakit:  E_F = W_P  (tek is akisi)
Urun:   E_P = E_2 - E_1

Yardimci denklem gereksiz:
  → Yakit tek akis (W_P), F-kurali uygulanmaz
  → c_1 onceki bilesenden gelir (bilinen)
  → c_W bilinen (elektrik fiyati)
  → Tek bilinmeyen: c_2
```

### 2.4 F-Kurali -- Coklu Yakit Akislari

Bir bilesenin yakiti birden fazla exergy farkından olusuyorsa, **her bir fark icin** ayri bir F-kurali denklemi yazilir.

```
Ornek: Cift akisli isi degistirici (iki sicak akis, bir soguk akis)

  Sicak Akis A:  E_A,giris - E_A,cikis  → Yakit 1
  Sicak Akis B:  E_B,giris - E_B,cikis  → Yakit 2
  Soguk Akis:    E_soguk,cikis - E_soguk,giris → Urun

F-kurali denklemi sayisi: 2
  (1) c_A,giris = c_A,cikis
  (2) c_B,giris = c_B,cikis

Ek olarak F-kurali genisletilmis yorumu:
  Tum yakit farkli exergy farklarina ait birim maliyetler birbirine esit:
  (c_A,giris · E_A,giris - c_A,cikis · E_A,cikis) / (E_A,giris - E_A,cikis)
  = (c_B,giris · E_B,giris - c_B,cikis · E_B,cikis) / (E_B,giris - E_B,cikis)
```

### 2.5 F-Kurali Ozet Tablosu

| Bilesen | Yakit Tanimi | F-Kurali Uygulanir mi? | Denklem |
|---------|-------------|------------------------|---------|
| Turbin | E_giris - E_cikis | Evet | c_giris = c_cikis |
| Isi degistirici | E_sicak,in - E_sicak,out | Evet | c_sicak,in = c_sicak,out |
| Kazan (baca gazi) | E_yakit + E_hava | Evet (baca icin) | c_baca = c_yakit |
| Kompresor | W_C | Hayir (tek akis) | -- |
| Pompa | W_P | Hayir (tek akis) | -- |
| Chiller | W_ch | Hayir (tek akis) | -- |
| CHP Turbin | E_giris - E_cikis_1 - E_cikis_2 | Evet | c_giris = c_cikis_1 = c_cikis_2 |
| Kisma valfi | E_giris - E_cikis | Evet | c_giris = c_cikis |

## 3. P-Kurali (Product Rule) -- Detayli Aciklama

### 3.1 Temel Tanim

P-kurali, bir bilesenin Urun (Product) exergy'sinin birden fazla exergy akisindan veya farkindan olusması durumunda uygulanir.

```
P-Kurali:
Bir bilesenin urunu birden fazla exergy akisi veya farkından olusuyorsa,
her bir urun akisinin / farkinin birim exergy maliyeti birbirine esittir.

Matematiksel ifade:
  Urun = {P_1, P_2, ...}  ise  =>  c_P1 = c_P2 = ...

Fiziksel anlam:
  Bilesen ayni surecte birden fazla urun uretiyorsa,
  bu urunlerin birim exergy maliyeti esit kabul edilir.
  Bu varsayim, bilesenin uretim surecinde "adil maliyet dagilimi" saglar.
```

### 3.2 P-Kurali -- Fiziksel Gerekce

P-kuralinin mantigi sudur: Bir bilesen tek bir termodinamik surecle birden fazla urun uretiyorsa, bu urunlerin birim exergy maliyetini farklilaştirmak icin fiziksel bir gerekce yoktur. Bilesen her iki urunu de "ayni maliyetle" uretir.

```
Ornek -- Kojenerasyon turbini:
  Urun 1: Elektrik (W_T)
  Urun 2: Proses buhari (E_ara_cekim - E_referans)

  P-kurali: c_W = (C_ara - C_ref) / (E_ara - E_ref)
  yani elektrigin birim exergy maliyeti = proses buhari birim exergy maliyeti

  Anlam: Turbin her iki urunu de ayni exergy donusum surecinde uretir,
         dolayisiyla birim maliyetleri esit olmalidir.
```

### 3.3 P-Kurali Ornekleri -- Ekipman Tipine Gore

#### 3.3.1 Ayirici (Splitter / Tee)

```
Ayirici Akis Semasi:
                    ┌──────────┐
  Akis 1 (giris) ──→│  AYIRICI │──→ Akis 2 (cikis A)
                    │          │──→ Akis 3 (cikis B)
                    └──────────┘

Urun:  E_P = E_2 + E_3  (iki ayri cikis akisi)
Yakit: E_F = E_1  (tek giris)

Maliyet dengesi:
  c_2 · E_2 + c_3 · E_3 = c_1 · E_1 + Z_ayirici

Bilinmeyenler: c_2, c_3  (c_1 bilinen)
Denklem: 1 maliyet dengesi
Yardimci: 1 P-kurali

P-kurali: c_2 = c_3
  → Her iki cikis akisi da ayni birim exergy maliyetine sahip
  → Ayirma islemi maliyeti yeniden dagitmaz, sadece akisi boler

Not: Ayiricide birden fazla cikis varsa, (n_cikis - 1) adet P-kurali yazilir
  3 cikisli ayirici: c_2 = c_3 = c_4  → 2 P-kurali denklemi
```

#### 3.3.2 Kojenerasyon Turbini (CHP Turbine)

```
CHP Turbin Akis Semasi:
                        ┌────────────────┐
  Akis 1 (YB buhar) ──→│  CHP TURBiN    │──→ W_T (elektrik)
                        │                │──→ Akis 2 (ara cekim - proses buharina)
                        │                │──→ Akis 3 (DB buhar - kondensere)
                        └────────────────┘

Yakit:  E_F = E_1 - E_2 - E_3
Urun:   E_P = W_T (elektrik) + (E_2 - E_ref) (proses buhari)

Burada E_ref, proses buharinin referans durumdaki (kondensat donusu) exergy'sidir.

Maliyet dengesi:
  c_W · W_T + c_2 · E_2 + c_3 · E_3 = c_1 · E_1 + Z_CHP

Bilinmeyenler: c_W, c_2, c_3  (c_1 bilinen)
Denklemler: 1 maliyet dengesi
Yardimci denklem gereksinimleri: 2 adet (F-kurali + P-kurali)

F-kurali: c_1 = c_3
  → Yakit tarafinda buhar genislerken birim maliyet korunur

P-kurali: c_W = (C_2 - C_ref) / (E_2 - E_ref)
  → Elektrik ve proses buhari urunlerinin birim exergy maliyeti esit
  → Basitlestirilmis: c_W = c_2 (eger E_ref ≈ 0)
```

#### 3.3.3 Coklu Urunlu Kazan (Multi-Product Boiler)

```
Iki farkli basinc seviyesinde buhar ureten kazan:

                    ┌──────────┐
  Akis 5 (yakit) ──→│  KAZAN   │──→ Akis 1 (YB buhar - 40 bar)
  Akis 4 (su)    ──→│          │──→ Akis 2 (AB buhar - 10 bar)
                    └──────────┘

Urun 1: E_1 - E_4a  (YB buhar exergy artisi)
Urun 2: E_2 - E_4b  (AB buhar exergy artisi)

(E_4a, E_4b: Her buhar hattina giren suyun exergy'si)

P-kurali:
  (C_1 - C_4a) / (E_1 - E_4a) = (C_2 - C_4b) / (E_2 - E_4b)

Anlam: Her iki buhar seviyesi de ayni yakma isleminden uretildigi icin,
       birim exergy urun maliyetleri esittir.
```

### 3.4 P-Kurali Ozet Tablosu

| Bilesen | Urun Tanimi | P-Kurali Uygulanir mi? | Denklem |
|---------|------------|------------------------|---------|
| Ayirici (2 cikis) | E_cikis1, E_cikis2 | Evet | c_cikis1 = c_cikis2 |
| CHP Turbin | W_T + (E_ara - E_ref) | Evet | c_W = c_ara_cekimde birim maliyet |
| Coklu urunlu kazan | (E_buhar1 - E_su1), (E_buhar2 - E_su2) | Evet | Birim urun maliyetleri esit |
| Turbin (tek is cikisi) | W_T (tek urun) | Hayir | -- |
| Kompresor | E_cikis - E_giris (tek fark) | Hayir | -- |
| Pompa | E_cikis - E_giris (tek fark) | Hayir | -- |
| Isi degistirici | E_soguk,out - E_soguk,in (tek fark) | Hayir | -- |

## 4. Sinir Kosullari (Boundary Conditions)

### 4.1 Dis Kaynak Maliyetleri

Sinir kosullari, sistemin disarisindaki kaynaklardan bilinen maliyet bilgileridir. Bu kosullar, denklem sistemini cozulebilir hale getirmek icin zorunludur.

```
Sinir Kosullari Genel Kurallari:

1. Yakit maliyeti (c_fuel):
   c_yakit = Yakit birim fiyati / Yakit exergy degeri

   Ornek -- Dogalgaz:
     Fiyat: 0.035 EUR/kWh (LHV bazli)
     Exergy/LHV orani: ~1.04
     c_dogalgaz = 0.035 / (1.04 × 3600) = 0.00935 EUR/kJ
     veya c_dogalgaz = 0.035 / 1.04 = 0.0337 EUR/kWh_exergy

   Ornek -- Fuel oil:
     Fiyat: 0.042 EUR/kWh (LHV bazli)
     Exergy/LHV orani: ~1.06
     c_fueloil = 0.042 / (1.06 × 3600) = 0.0110 EUR/kJ

2. Elektrik maliyeti (c_electricity):
   c_elektrik = Elektrik birim fiyati / 3600  [EUR/kJ]
   (Elektrigin exergy degeri = enerji degeri, yani exergy/enerji = 1.0)

   Ornek -- Turkiye sanayi tarife:
     Fiyat: 0.095 EUR/kWh
     c_elektrik = 0.095 / 3600 = 0.0000264 EUR/kJ
     veya c_elektrik = 0.095 EUR/kWh (kWh bazinda dogrudan)

3. Ortam akislari (c = 0):
   Cevre sicakliginda sisteme giren akislarin birim exergy maliyeti sifirdir.

   c_hava = 0          (atmosferden cekilen hava)
   c_sogutma_suyu = 0  (nehir/deniz suyu, giris)
   c_ortam = 0         (referans cevre kosullarindaki herhangi bir akis)

   Gerekce: Bu akislarin elde edilmesi icin bir exergy harcamasi
            yapilmamistir (veya ihmal edilebilir duzeydedir).
```

### 4.2 Yakit Exergy Degerlerinin Hesaplanmasi

```
Yakit Turleri ve Exergy/LHV Oranlari:

| Yakit Turu          | LHV [kJ/kg] | Exergy [kJ/kg] | Exergy/LHV | Tipik c [EUR/kJ] |
|---------------------|-------------|-----------------|------------|-------------------|
| Dogalgaz (CH4)      | 50,000      | 52,000          | 1.04       | 0.008-0.012       |
| Fuel oil (No. 6)    | 39,500      | 41,870          | 1.06       | 0.009-0.013       |
| Dizel               | 42,500      | 44,400          | 1.045      | 0.012-0.018       |
| Komur (bituminous)  | 29,000      | 30,600          | 1.055      | 0.004-0.007       |
| Biyomass (odun)     | 18,000      | 19,200          | 1.067      | 0.003-0.006       |
| Hidrojen             | 120,000     | 117,600         | 0.98       | 0.020-0.040       |

Formul:
  c_yakit [EUR/kJ] = Fiyat_yakit [EUR/kg] / Exergy_yakit [kJ/kg]

  veya

  c_yakit [EUR/kWh_ex] = Fiyat_yakit [EUR/kWh_LHV] × (LHV/Exergy)
```

### 4.3 Sinir Kosulu Tipleri Ozeti

```
Sinir Kosulu Siniflari:

Tip 1 -- Dis kaynak bilinen:
  c_yakit = bilinen (piyasa fiyati / exergy)
  c_elektrik = bilinen (tarife / exergy)
  → n_dis_kaynak adet denklem saglar

Tip 2 -- Cevre akislari:
  c_hava = 0
  c_sogutma_suyu_giris = 0
  c_ortam_su = 0
  → n_cevre adet denklem saglar

Tip 3 -- Atik akislar (opsiyonel):
  c_atik = 0  (atik maliyetsiz kabul edilir)
  veya c_atik > 0 (atik bertaraf maliyeti dahil)
  → Bu secim analizin varsayimlarina baglidir

Tip 4 -- Ozel tanimlar:
  Bilesik bilesen (merged component) giris/cikis tanimlari
  → Sistem sinirlarinin yeniden tanimlanmasindan kaynaklanir
```

## 5. Dissipative Bilesen Ele Alimi (Dissipative Component Handling)

### 5.1 Dissipative Bilesen Nedir?

Dissipative bilesenler, termodinamik olarak zorunlu olan ancak dogrudan bir **urun** tanimlanamayan bilesenlerdir. Bu bilesenler exergy'yi yokeder ancak buna karsilik bir urun uretmez.

```
Yaygin Dissipative Bilesenler:
├── Kondenser (soğutma ve yoguşturma)
├── Kisma valfi (basinc dusurme)
├── Sogutma kulesi (atik isi reddi)
├── Boru hatlari (basinc dusumu, isi kaybi)
└── Karistirici (bazi konfigurasyonlarda)
```

### 5.2 Kondenser -- Maliyet Atama Yontemleri

Kondenser, Rankine cevrimi ve sogutma sistemlerinde en yaygin dissipative bilesendir.

```
Kondenser Akis Semasi (Rankine cevrimi):

                      ┌────────────┐
  Akis 2 (turbin     │            │
  cikisi, DB buhar) ──→│ KONDENSER │──→ Akis 3 (sivi su, pompa girisine)
                      │            │
  Akis 7 (sogutma    │            │──→ Akis 8 (sogutma suyu cikis)
  suyu giris)      ──→│            │
                      └────────────┘

Exergy yikimi: E_D,kond = (E_2 - E_3) - (E_8 - E_7)
  (cok buyuk olabilir, cunku DB buhar → sivi donusumunde buyuk exergy kaybi)
```

#### Yontem A: Bilesik Bilesen (Merge)

```
Kondenseri, servis ettigi bilesen ile birlestir.

Ornek: Kazan + Kondenser birlesmesi
  Bilesik bilesen: "Buhar Ureticisi"
  F: E_yakit
  P: E_buhar,cikis - E_su,giris  (ayni)
  E_D: E_D,kazan + E_D,kondenser (toplam)
  Z: Z_kazan + Z_kondenser (toplam)

Avantaj:
  + Dissipative bilesen problemi ortadan kalkar
  + Denklem sayisi azalir

Dezavantaj:
  - Kondenserin bireysel katkisi gorulemez
  - Bilesen bazli detayli analiz kaybi
```

#### Yontem B: Exergy Yikimini Dagitma

```
Kondenserin E_D'sini, onu "zorunlu kilan" bilesenlere orantili dagit.

Dagitim kriteri: Her bilesenin E_D'si ile orantili

Ornek (3 bilesenli sistem):
  E_D,kazan = 27,000 kW
  E_D,turbin = 300 kW
  E_D,pompa = 200 kW
  E_D,kondenser = 7,760 kW
  Toplam (kondenser haric) = 27,500 kW

  Dagitim:
    Kazan payı:  7,760 × (27,000/27,500) = 7,622 kW
    Turbin payı: 7,760 × (300/27,500) = 84.7 kW
    Pompa payı:  7,760 × (200/27,500) = 56.4 kW

  Duzeltilmis E_D degerleri:
    E_D,kazan_yeni = 27,000 + 7,622 = 34,622 kW
    E_D,turbin_yeni = 300 + 84.7 = 384.7 kW
    E_D,pompa_yeni = 200 + 56.4 = 256.4 kW

Avantaj: Dissipative maliyet servis eden bilesenlere yansiyor
Dezavantaj: Dagitim kriteri tartismaya acik
```

#### Yontem C: Bagimsiz Bilesen (Standalone)

```
Kondenseri bagimsiz bilesen olarak tut, F-kurali uygula.

Maliyet dengesi:
  c_3 · E_3 + c_8 · E_8 = c_2 · E_2 + c_7 · E_7 + Z_kond

Sinir kosullari:
  c_7 = 0  (sogutma suyu giris, cevre akisi)
  c_8 = 0  (sogutma suyu cikis, atik kabul edilir)

Yardimci denklem (F-kurali):
  c_2 = c_1  (turbinden gelen buhar, zaten F-kurali ile belirlenmis)

Sonuc:
  c_3 = (c_2 · E_2 + Z_kond) / E_3
  → c_3 buyuk olabilir cunku E_3 << E_2

Avantaj: Kondenserdin katkisi bireysel olarak izlenebilir
Dezavantaj: c_3 cok yuksek cikar (dusuk exergy'ye yuksek maliyet yuklenir)
```

### 5.3 Kisma Valfi -- Maliyet Atama

```
Kisma Valfi Akis Semasi:
                    ┌──────────┐
  Akis 1 (giris) ──→│  VALF    │──→ Akis 2 (cikis, dusuk basinc)
                    └──────────┘

Ozellik: Izoentalpik surecte (h_1 = h_2), entropi artar → exergy yokedilir

Maliyet dengesi:
  c_2 · E_2 = c_1 · E_1 + Z_valf
  (Z_valf ≈ 0, valf yatirim maliyeti genellikle ihmal edilebilir)

Yardimci denklem (F-kurali):
  c_1 = c_2
  → Akiskanin birim exergy maliyeti valf gecisinde degismez

Sonuc:
  Z_valf ≈ 0 ve c_1 = c_2 ise:
  c_2 · E_2 = c_1 · E_1
  → c_2 = c_1 × (E_1/E_2) > c_1  (cunku E_1 > E_2)

DIKKAT: c_1 = c_2 yardimci denklemi birim maliyet esitligi saglar,
        ancak maliyet akisi C_2 < C_1 olur (exergy azalir, birim maliyet artar).

Alternatif yaklasim (dissipative birlestirme):
  Valfi bitisik bilesenle birlestir → Ayri denklem gereksiz
```

### 5.4 Dissipative Bilesen Karar Tablosu

| Durum | Onerilen Yontem | Gerekce |
|-------|-----------------|---------|
| Basit sistem (< 5 bilesen) | A -- Birlestir | Daha az denklem, hizli cozum |
| Orta karmasik sistem | B -- Dagit | Detayli maliyet izleme |
| Detayli akademik analiz | C -- Bagimsiz | Bilesen bazli tam goruntu |
| Kondenser + kazan bütünleşik | A -- Birlestir | Dogal tasarim siniri |
| Valf (Z ≈ 0) | F-kurali (c_in = c_out) | En basit, tutarli |
| Sogutma kulesi | C -- Bagimsiz | Ayri yatirim maliyeti var |

## 6. Denklem Sayisi Dogrulamasi (Equation Count Verification)

### 6.1 Temel Formul

Exergoekonomik denklem sisteminin dogru kuruldugundan emin olmak icin denklem sayisi dogrulamasi yapilir.

```
Denklem Sayisi Dogrulamasi:

n_bilinmeyen = n_akis + n_is_akisi + n_isi_akisi

n_denklem_toplam = n_bilesen + n_yardimci + n_sinir

Kontrol:
  n_bilinmeyen = n_denklem_toplam  → Sistem cozulebilir (tam belirli)
  n_bilinmeyen > n_denklem_toplam  → Eksik denklem (belirsiz)
  n_bilinmeyen < n_denklem_toplam  → Fazla belirli (tutarsizlik riski)

Genisletilmis formul:
  n_bilinmeyen = n_bilesenler + n_yardimci + n_sinir

  Bu formul su sekilde de yazilabilir:
  n_bilinmeyen = n_components + n_auxiliary + n_boundary
```

### 6.2 Sistematik Sayma Yontemi

```
Adim 1: Tum akislari say
  → Her akis (stream) icin bir c bilinmeyeni
  → Her is akisi (W) icin bir c_W bilinmeyeni
  → Her isi akisi (Q, eger varsa) icin bir c_Q bilinmeyeni

Adim 2: Maliyet denge denklemlerini say
  → Her bilesen icin 1 denklem
  → Toplam: n_bilesen

Adim 3: Sinir kosullarini say
  → Bilinen dis kaynak maliyetleri
  → Cevre akislari (c = 0)
  → Atik akislar (c = 0, eger atik ise)

Adim 4: Gerekli yardimci denklem sayisini hesapla
  → n_yardimci = n_bilinmeyen - n_bilesen - n_sinir

Adim 5: F ve P kurallarini uygula
  → Her bilesen icin:
     F tarafinda kac exergy farki var? → (n_F_farki - 1) F-kurali
     P tarafinda kac urun akisi/farki var? → (n_P_farki - 1) P-kurali

Adim 6: Dogrulamayi yap
  → Yazilan F-kurali + P-kurali = n_yardimci ?
  → Evet → Sistem tam belirli, cozume gecilir
  → Hayir → Tanimlamalari gozden gecir
```

### 6.3 Ekipman Bazli Yardimci Denklem Sayisi Rehberi

```
Her bilesen turu icin tipik yardimci denklem sayisi:

| Bilesen Tipi           | n_cikis | n_bilinmeyen* | n_yardimci | Kural Turu    |
|------------------------|---------|---------------|------------|---------------|
| Kompresor              | 1       | 1             | 0          | --            |
| Turbin                 | 2       | 2             | 1          | F-kurali      |
| Kazan (baca atik)      | 1       | 1             | 0          | (c_baca = 0)  |
| Kazan (baca F-kurali)  | 2       | 2             | 1          | F-kurali      |
| Isi degistirici        | 2       | 2**           | 1          | F-kurali      |
| Pompa                  | 1       | 1             | 0          | --            |
| Chiller                | 1-2     | 1-2           | 0-1        | Kondenser     |
| Karistirici            | 1       | 1             | 0          | --            |
| Ayirici (2 cikis)      | 2       | 2             | 1          | P-kurali      |
| Ayirici (3 cikis)      | 3       | 3             | 2          | P-kurali (×2) |
| CHP Turbin (2 cikis+W) | 3       | 3             | 2          | F + P kurali  |
| Valf                   | 1       | 1             | 0***       | F-kurali      |

* Gelen akis maliyetleri bilinen varsayilarak sadece bilesenden cikan bilinmeyenler
** Soguk taraf girisi genellikle bilinen
*** Valf icin F-kurali zaten sinir kosulu gibi uygulanir (c_in = c_out)
```

### 6.4 Dogrulama Ornegi

```
Ornek: 4-Bilesenli Rankine Cevrimi

Akislar: 1 (kazan cikis), 2 (turbin cikis), 3 (kondenser cikis), 4 (pompa cikis)
         5 (yakit), W_T (turbin isi), W_P (pompa isi)
Bilesenler: Kazan, Turbin, Kondenser (bağımsız), Pompa

n_bilinmeyen = 4 (c_1, c_2, c_3, c_4) + 1 (c_W_T) + 1 (c_W_P) + 1 (c_5) = 7
  → Ancak: c_5 = bilinen (yakit fiyati) → sinir kosulu
  → c_W_P = c_W_T (ayni elektrik sebekesi varsayimi) veya bagimsiz

Basitlestirilmis sayim:
  n_bilinmeyen = 5 (c_1, c_2, c_3, c_4, c_W)
  n_bilesen = 4 (kazan, turbin, kondenser, pompa)
  n_sinir = 1 (c_5 = c_yakit)
  n_yardimci_gerekli = 5 - 4 = 1 (sinir haric bilinmeyen - denklem)

  Yardimci denklemler:
    Turbin F-kurali: c_1 = c_2  → 1 denklem

  Kontrol:
    Toplam denklem = 4 (maliyet dengesi) + 1 (F-kurali) + 1 (sinir) = 6
    Bilinmeyen = 5 + 1 (c_5 dahil) = 6  ✓ Dogru!

  Not: Kondenser icin c_sogutma_suyu = 0 (cevre) ek sinir kosulu var
       Bu da toplam sayiyi tutar.
```

## 7. Kojenerasyon Sistemi Ornegi -- Kapsamli Uygulama (CHP with Gas Turbine, HRSG, Process Heat)

### 7.1 Sistem Tanimi

```
Kojenerasyon (CHP) Sistemi:

Bilesenler:
  1. Kompresor (AC) — Hava sikistirma
  2. Yanma odasi (CC) — Yakit yakma
  3. Gaz turbini (GT) — Guc uretimi
  4. HRSG (Heat Recovery Steam Generator) — Atik isi geri kazanimi
  5. Proses isi degistirici (PHX) — Proses isisi temini

Akislar:
  1: Hava girisi (ortam, kompresor giris)
  2: Sikistirilmis hava (kompresor cikis → yanma odasi)
  3: Yanma gazlari (yanma odasi cikis → gaz turbin giris)
  4: Egzoz gazlari (gaz turbin cikis → HRSG giris)
  5: Egzoz cikis (HRSG cikis → baca)
  6: Besleme suyu (HRSG giris, soguk taraf)
  7: Buhar (HRSG cikis → PHX giris)
  8: Kondensat (PHX cikis → geri donus)
  9: Proses akiskani giris (PHX soguk taraf giris)
  10: Proses akiskani cikis (PHX soguk taraf cikis)
  11: Yakit (yanma odasi girisi)

  W_GT: Gaz turbini brut guc cikisi
  W_AC: Kompresor guc tuketimi
  W_net: Net elektrik cikisi (W_GT - W_AC)

Sistem Semasi:
                 Yakit (11)
                    │
                    ▼
  Hava (1) → [AC] → (2) → [CC] → (3) → [GT] → (4) → [HRSG] → (5) Baca
              ↑                          │               │
              │                          ▼               ▼
              W_AC ←────────── W_GT      (7) Buhar
                     │                   │
                     ▼                   ▼
                  W_net              [PHX] → (10) Proses cikis
                                     ↑
                                  (9) Proses giris
                                     ↓
                                  (8) Kondensat
```

### 7.2 Exergy Verileri

| Akis | Aciklama | E [kW] | Durum |
|------|----------|--------|-------|
| 1 | Hava (ortam) | 0 | T₀ = 25 degC, P₀ = 1.013 bar |
| 2 | Sikistirilmis hava | 8,450 | T = 350 degC, P = 12 bar |
| 3 | Yanma gazlari | 52,100 | T = 1,100 degC, P = 11.5 bar |
| 4 | Egzoz (turbin cikis) | 18,200 | T = 520 degC, P = 1.05 bar |
| 5 | Egzoz (HRSG cikis) | 2,300 | T = 130 degC, P = 1.02 bar |
| 6 | Besleme suyu | 120 | T = 60 degC, P = 25 bar |
| 7 | Buhar (HRSG cikis) | 9,800 | T = 400 degC, P = 20 bar |
| 8 | Kondensat (PHX cikis) | 350 | T = 85 degC, P = 2 bar |
| 9 | Proses akiskani giris | 180 | T = 40 degC |
| 10 | Proses akiskani cikis | 3,200 | T = 180 degC |
| 11 | Yakit (dogalgaz) | 55,000 | Kimyasal exergy |
| W_GT | Turbin guc cikisi | 25,600 | -- |
| W_AC | Kompresor tuketimi | 8,200 | -- |
| W_net | Net elektrik | 17,400 | W_GT - W_AC |

### 7.3 F ve P Tanimlari

```
Bilesen 1 -- Kompresor (AC):
  Yakit:  E_F = W_AC = 8,200 kW
  Urun:   E_P = E_2 - E_1 = 8,450 - 0 = 8,450 kW
  E_D = 8,200 - 8,450 = ...
  Not: E_P > E_F olamaz → E_1'in fiziksel exergy'si dahil edilmeli
  Duzeltme: E_1 ≈ 0 (ortam havasi), E_D = W_AC - (E_2 - E_1) = 8,200 - 8,450
  → Veriler yeniden kontrol edilmeli; pratik ornekte E_2 < W_AC + E_1 olmali
  E_2 = 8,000 kW olarak duzeltilmis:
  E_D = 8,200 - 8,000 = 200 kW

  Yakit tek akis (W_AC) → F-kurali GEREKMEZ
  Urun tek fark (E_2 - E_1) → P-kurali GEREKMEZ

Bilesen 2 -- Yanma Odasi (CC):
  Yakit:  E_F = E_11 + E_2 - E_3... hayir:
  Duzeltme: Yakit kimyasal exergy + hava exergy → yanma gazlari
  F: E_11 (yakit exergy)
  P: E_3 - E_2 (yanma gazlarinin exergy artisi)
  E_D = E_11 - (E_3 - E_2) = 55,000 - (52,100 - 8,000) = 55,000 - 44,100 = 10,900 kW

  Yakit tek akis (E_11) → F-kurali GEREKMEZ
  Urun tek fark (E_3 - E_2) → P-kurali GEREKMEZ

Bilesen 3 -- Gaz Turbini (GT):
  Yakit:  E_F = E_3 - E_4 = 52,100 - 18,200 = 33,900 kW
  Urun:   E_P = W_GT = 25,600 kW
  E_D = 33,900 - 25,600 = 8,300 kW

  Yakit exergy farki (E_3 - E_4) → F-kurali GEREKLI
  Urun tek akis (W_GT) → P-kurali GEREKMEZ

Bilesen 4 -- HRSG:
  Yakit:  E_F = E_4 - E_5 = 18,200 - 2,300 = 15,900 kW
  Urun:   E_P = E_7 - E_6 = 9,800 - 120 = 9,680 kW
  E_D = 15,900 - 9,680 = 6,220 kW

  Yakit exergy farki (E_4 - E_5) → F-kurali GEREKLI
  Urun tek fark (E_7 - E_6) → P-kurali GEREKMEZ

Bilesen 5 -- Proses Isi Degistirici (PHX):
  Yakit:  E_F = E_7 - E_8 = 9,800 - 350 = 9,450 kW
  Urun:   E_P = E_10 - E_9 = 3,200 - 180 = 3,020 kW
  E_D = 9,450 - 3,020 = 6,430 kW

  Yakit exergy farki (E_7 - E_8) → F-kurali GEREKLI
  Urun tek fark (E_10 - E_9) → P-kurali GEREKMEZ
```

### 7.4 Denklem Sayisi Dogrulamasi

```
Adim 1: Bilinmeyenleri say

Akis bilinmeyenleri:
  c_1 = 0 (ortam havasi, sinir kosulu)
  c_2 = ?
  c_3 = ?
  c_4 = ?
  c_5 = ?
  c_6 = ?  (besleme suyu, sinir kosuluna bagli)
  c_7 = ?
  c_8 = ?
  c_9 = ?  (proses akiskani giris, sinir kosuluna bagli)
  c_10 = ?
  c_11 = bilinen (yakit fiyati, sinir kosulu)

Is akisi bilinmeyenleri:
  c_W_GT = ?
  c_W_AC = ?

Varsayim: c_W_GT = c_W_AC = c_W (ayni elektrik sebekesi)
  → 1 bilinmeyen

Toplam bilinmeyen sayisi:
  Akislar: c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10 = 9
  Is: c_W = 1
  Toplam: 10 bilinmeyen

Adim 2: Maliyet denge denklemlerini say
  5 bilesen → 5 denklem

Adim 3: Sinir kosullarini say
  c_1 = 0 (hava, ortam) → 1
  c_11 = c_yakit (bilinen) → 1
  c_6 = 0 (besleme suyu, cevreden) veya c_6 bilinen → 1
  c_9 = 0 (proses akiskani cevreden) veya c_9 bilinen → 1
  Toplam: 4 sinir kosulu

  Not: c_5 (baca gazi) icin karar gerekli:
    → Atik ise: c_5 = 0 → 1 ek sinir kosulu
    → Degeri varsa: Bilinmeyen kalir

  c_5 = 0 (baca atik) varsayimiyla:
  Toplam sinir kosulu: 5

Adim 4: Gerekli yardimci denklem sayisi
  n_yardimci = n_bilinmeyen - n_bilesen - n_sinir
  n_yardimci = 10 - 5 - 5 = 0

  KONTROL: Gaz turbini icin F-kurali yazilmali (c_3 = c_4)
           HRSG icin F-kurali yazilmali (c_4 = c_5)
           PHX icin F-kurali yazilmali (c_7 = c_8)

  Ancak c_5 = 0 sinir kosulunu kullanirsak, c_4 = c_5 = 0 olur ki
  bu tutarsizdir (turbin cikis exergy'si maliyetsiz olamaz).

  DUZELTME: c_5 atik degilse, sinir kosulu olmaktan cikar:
    Sinir kosulu: 4 (c_1=0, c_11=bilinen, c_6=0, c_9=0)
    n_yardimci = 10 - 5 - 4 = 1

  Halbuki 3 adet F-kurali yazilabilir:
    GT:   c_3 = c_4  → 1 denklem
    HRSG: c_4 = c_5  → 1 denklem
    PHX:  c_7 = c_8  → 1 denklem

  Ama 3 F-kurali + 4 sinir + 5 denklem = 12 > 10 bilinmeyen!
  → Fazla belirlenmis sistem

  COZUM: c_5 ya sinir kosulu VEYA F-kurali ile belirlenir, ikisi birden degil.
    → c_5 = 0 kabul edilirse HRSG F-kurali (c_4 = c_5) otomatik olarak
      c_4 = 0 zorlayacagi icin tutarsizdir.
    → Dogru yaklasim: c_5 serbest birakilir, HRSG F-kurali uygulanir.

Duzeltilmis sayim:

  Bilinmeyenler: c_2, c_3, c_4, c_5, c_7, c_8, c_10, c_W = 8
  (c_1=0, c_6=0, c_9=0, c_11=bilinen → 4 sinir; c_6, c_9 sabit)

  Bekleyin -- daha sistematik yapalim:

  Tum bilinmeyenler (c ile gosterilen):
    c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_W = 12

  Sinir kosullari:
    c_1 = 0        → 1
    c_6 = 0        → 1
    c_9 = 0        → 1
    c_11 = bilinen → 1
    Toplam: 4

  Serbest bilinmeyen: 12 - 4 = 8

  Maliyet denge denklemleri: 5

  Gerekli yardimci: 8 - 5 = 3

  Yazilabilecek yardimci denklemler:
    GT F-kurali:   c_3 = c_4    → 1
    HRSG F-kurali: c_4 = c_5    → 1
    PHX F-kurali:  c_7 = c_8    → 1
    Toplam: 3 yardimci denklem  ✓

  DOGRULAMA:
    n_bilinmeyen = 12
    n_bilesen = 5
    n_sinir = 4
    n_yardimci = 3
    Toplam denklem = 5 + 4 + 3 = 12 = n_bilinmeyen  ✓ DOGRU!
```

### 7.5 Ekonomik Veriler

| Bilesen | PEC [EUR] | Z [EUR/saat] |
|---------|-----------|--------------|
| Kompresor (AC) | 3,200,000 | 76.00 |
| Yanma Odasi (CC) | 450,000 | 10.70 |
| Gaz Turbini (GT) | 4,800,000 | 114.00 |
| HRSG | 1,800,000 | 42.75 |
| Proses HX (PHX) | 350,000 | 8.30 |
| **Toplam** | **10,600,000** | **251.75** |

Yakit maliyeti: c_11 = 0.0095 EUR/kJ (dogalgaz)

### 7.6 Tam Denklem Sistemi

```
Maliyet Denge Denklemleri (5 adet):

(1) Kompresor:
    c_2 · E_2 = c_1 · E_1 + c_W · W_AC + Z_AC
    c_2 · 8000 = 0 · 0 + c_W · 8200 + 76.00
    c_2 · 8000 = c_W · 8200 + 76.00

(2) Yanma Odasi:
    c_3 · E_3 = c_11 · E_11 + c_2 · E_2 + Z_CC
    c_3 · 52100 = 0.0095 · 55000 + c_2 · 8000 + 10.70
    c_3 · 52100 = 522.50 + c_2 · 8000 + 10.70

(3) Gaz Turbini:
    c_W · W_GT + c_4 · E_4 = c_3 · E_3 + Z_GT
    c_W · 25600 + c_4 · 18200 = c_3 · 52100 + 114.00

(4) HRSG:
    c_5 · E_5 + c_7 · E_7 = c_4 · E_4 + c_6 · E_6 + Z_HRSG
    c_5 · 2300 + c_7 · 9800 = c_4 · 18200 + 0 · 120 + 42.75
    c_5 · 2300 + c_7 · 9800 = c_4 · 18200 + 42.75

(5) Proses HX:
    c_8 · E_8 + c_10 · E_10 = c_7 · E_7 + c_9 · E_9 + Z_PHX
    c_8 · 350 + c_10 · 3200 = c_7 · 9800 + 0 · 180 + 8.30
    c_8 · 350 + c_10 · 3200 = c_7 · 9800 + 8.30

Yardimci Denklemler (3 adet):

(6) GT F-kurali:  c_3 = c_4
(7) HRSG F-kurali: c_4 = c_5
(8) PHX F-kurali:  c_7 = c_8

Sinir Kosullari (4 adet):

(9)  c_1 = 0
(10) c_6 = 0
(11) c_9 = 0
(12) c_11 = 0.0095 EUR/kJ
```

### 7.7 Cozum

```
Sinir kosullarini yerine koyarak basitlestirelim:

(6): c_3 = c_4
(7): c_4 = c_5  → c_3 = c_4 = c_5

(1): c_2 · 8000 = c_W · 8200 + 76.00
(2): c_3 · 52100 = 533.20 + c_2 · 8000
(3): c_W · 25600 + c_3 · 18200 = c_3 · 52100 + 114.00
     → c_W · 25600 = c_3 · (52100 - 18200) + 114.00
     → c_W · 25600 = c_3 · 33900 + 114.00

(4): c_3 · 2300 + c_7 · 9800 = c_3 · 18200 + 42.75
     → c_7 · 9800 = c_3 · (18200 - 2300) + 42.75
     → c_7 · 9800 = c_3 · 15900 + 42.75
     → c_7 = (c_3 · 15900 + 42.75) / 9800

(8): c_7 = c_8

(5): c_8 · 350 + c_10 · 3200 = c_7 · 9800 + 8.30
     → c_7 · 350 + c_10 · 3200 = c_7 · 9800 + 8.30  (c_8 = c_7)
     → c_10 · 3200 = c_7 · (9800 - 350) + 8.30
     → c_10 · 3200 = c_7 · 9450 + 8.30

Denklem (2)'den:
  c_2 = (c_3 · 52100 - 533.20) / 8000

Denklem (1)'den:
  c_W = (c_2 · 8000 - 76.00) / 8200

Denklem (3)'ten:
  c_W = (c_3 · 33900 + 114.00) / 25600

(1) ve (2)'yi birlestirelim:
  c_2 · 8000 = c_W · 8200 + 76.00
  c_3 · 52100 - 533.20 = c_W · 8200 + 76.00
  c_W = (c_3 · 52100 - 609.20) / 8200

(3)'ten:
  c_W = (c_3 · 33900 + 114.00) / 25600

Esitleyelim:
  (c_3 · 52100 - 609.20) / 8200 = (c_3 · 33900 + 114.00) / 25600

  25600 · (c_3 · 52100 - 609.20) = 8200 · (c_3 · 33900 + 114.00)
  c_3 · 1,333,760,000 - 15,595,520 = c_3 · 277,980,000 + 934,800
  c_3 · (1,333,760,000 - 277,980,000) = 15,595,520 + 934,800
  c_3 · 1,055,780,000 = 16,530,320
  c_3 = 16,530,320 / 1,055,780,000
  c_3 = 0.01566 EUR/kJ

Dolayisiyla:
  c_3 = c_4 = c_5 = 0.01566 EUR/kJ
  c_W = (0.01566 · 33900 + 114.00) / 25600 = (530.87 + 114.00) / 25600
  c_W = 644.87 / 25600 = 0.02519 EUR/kJ = 90.7 EUR/MWh
  c_2 = (0.01566 · 52100 - 533.20) / 8000 = (815.9 - 533.20) / 8000
  c_2 = 282.7 / 8000 = 0.03534 EUR/kJ
  c_7 = (0.01566 · 15900 + 42.75) / 9800 = (248.99 + 42.75) / 9800
  c_7 = 291.74 / 9800 = 0.02977 EUR/kJ
  c_8 = 0.02977 EUR/kJ (P-kurali ile)
  c_10 = (0.02977 · 9450 + 8.30) / 3200 = (281.33 + 8.30) / 3200
  c_10 = 289.63 / 3200 = 0.09051 EUR/kJ

Ozet:
  c_3 = c_4 = c_5 = 0.01566 EUR/kJ  (yanma gazlari)
  c_2 = 0.03534 EUR/kJ               (sikistirilmis hava)
  c_W = 0.02519 EUR/kJ = 90.7 EUR/MWh (elektrik)
  c_7 = c_8 = 0.02977 EUR/kJ         (buhar)
  c_10 = 0.09051 EUR/kJ              (proses isisi)
```

### 7.8 Sonuclarin Degerlendirilmesi

```
Bilesen Bazli Degerlendirme:

| Bilesen | c_F [EUR/kJ] | c_P [EUR/kJ] | E_D [kW] | C_D [EUR/h] | Z [EUR/h] | f_k   | r_k  |
|---------|-------------|-------------|----------|------------|----------|-------|------|
| AC      | 0.02519*    | 0.03534     | 200      | 5.04       | 76.00    | 0.938 | 0.40 |
| CC      | 0.0095      | 0.01566     | 10,900   | 103.55     | 10.70    | 0.094 | 0.65 |
| GT      | 0.01566     | 0.02519     | 8,300    | 129.98     | 114.00   | 0.467 | 0.61 |
| HRSG    | 0.01566     | 0.02977     | 6,220    | 97.40      | 42.75    | 0.305 | 0.90 |
| PHX     | 0.02977     | 0.09051     | 6,430    | 191.38     | 8.30     | 0.042 | 2.04 |

* c_F,AC = c_W (elektrik birim maliyeti)

Yorumlama:
┌────────────────────────────────────────────────────────────────────────────┐
│ Yanma Odasi (CC): f_k = 0.094 (cok dusuk)                                │
│ → Exergy yikimi baskın (C_D >> Z)                                        │
│ → Cozum: Yanma verimliligi artirimi, preheating, regenerasyon            │
│ → Yillik C_D ≈ 103.55 × 8000 = 828,400 EUR/yil                         │
├────────────────────────────────────────────────────────────────────────────┤
│ PHX: f_k = 0.042 (en dusuk)                                              │
│ → Exergy yikimi cok baskın, r_k = 2.04 (en yuksek)                      │
│ → Cozum: Daha buyuk isi degistirici, sicaklik farkini azalt              │
│ → Yillik C_D ≈ 191.38 × 8000 = 1,531,040 EUR/yil                       │
├────────────────────────────────────────────────────────────────────────────┤
│ GT: f_k = 0.467 (dengeli)                                                │
│ → Optimize edilmis bolge, ince ayar yapilabilir                          │
│ → r_k = 0.61 makul seviyede                                             │
├────────────────────────────────────────────────────────────────────────────┤
│ AC: f_k = 0.938 (cok yuksek)                                             │
│ → Yatirim maliyeti baskın, daha ucuz kompresor dusunulebilir             │
│ → Ancak E_D dusuk (200 kW), oncelik dusuk                               │
├────────────────────────────────────────────────────────────────────────────┤
│ HRSG: f_k = 0.305 (dengeli)                                              │
│ → r_k = 0.90, orta-yuksek iyilestirme potansiyeli                       │
│ → Daha buyuk isi transfer alani ile verimlilik artisi                    │
└────────────────────────────────────────────────────────────────────────────┘

Oncelik sirasi (C_D + Z bazinda):
  1. PHX:  199.68 EUR/h  (C_D + Z en yuksek — islem isi verimsizligi)
  2. GT:   243.98 EUR/h  (yuksek ancak f_k dengeli — ince ayar)
  3. HRSG: 140.15 EUR/h  (orta — transfer alan optimizasyonu)
  4. CC:   114.25 EUR/h  (dusuk f_k — yanma teknolojisi iyilestirmesi)
  5. AC:   81.04 EUR/h   (yuksek f_k, dusuk oncelik)
```

## 8. Ozel Durumlar ve Ileri Konular

### 8.1 Egzoz/Baca Gazinin Degerlendirilmesi

```
Baca gazi (egzoz) akislari icin uc yaklasim:

Yaklasim 1: Atik akis (c_baca = 0)
  → Baca gazinin ekonomik degeri yok
  → Basit, ancak baca gazi geri kazanimi ihmal edilir

Yaklasim 2: F-kurali (c_baca = c_yakit_kaynagi)
  → Baca gazinin birim maliyeti, kaynagi olan yakitin birim maliyetiyle ayni
  → Geri kazanim potansiyelini yansitiyor

Yaklasim 3: Cevresel maliyet (c_baca < 0)
  → Karbon vergisi/emisyon maliyeti → negatif maliyet (bertaraf gideri)
  → Ileri analiz icin uygun

Secim kriteri:
  → Baca gazi enerjisi kullaniliyorsa: Yaklasim 2
  → Baca gazi dogrudan atiliyorsa: Yaklasim 1
  → Emisyon maliyetlendirmesi yapiliyorsa: Yaklasim 3
```

### 8.2 Birden Fazla Yakit Kaynagi

```
Bir sistem birden fazla yakitla besleniyorsa (ornegin dogalgaz + fuel oil),
her yakitin c degeri bagimsiz olarak belirlenir:

c_dogalgaz = Fiyat_DG / Exergy_DG
c_fueloil = Fiyat_FO / Exergy_FO

Bu degisik c degerleri, ilgili bilesenin maliyet denge denklemine girilir.
F-kurali ayri ayri uygulanir.
```

### 8.3 Recirculation (Geri Donus) Akislari

```
Sistem icinde geri donus akislari (recirculation) varsa:

Iteratif cozum gerekir:
  1. Baslangic tahmini: c_geri_donus = c_ileri_akis (ilk iterasyon)
  2. Denklem sistemi cozulur
  3. Yeni c_geri_donus hesaplanir
  4. Yakinsayana kadar tekrarla (genellikle 3-5 iterasyon yeterli)

Alternatif: Matris formulasyonu ile dogrudan cozum (iterasyon gereksiz)
  → Detay: matrix_formulation.md
```

## 9. Yardimci Denklem Yazimi -- Hizli Referans

### 9.1 Kontrol Listesi

```
Her bilesen icin su adimlari takip et:

□ 1. Bilesenin F (Yakit) tanimini yaz
□ 2. Bilesenin P (Urun) tanimini yaz
□ 3. F taniminda kac exergy farki var?
     → 1 fark: F-kurali GEREKMEZ
     → n fark: (n-1) F-kurali yaz
□ 4. P taniminda kac urun akisi/farki var?
     → 1 urun: P-kurali GEREKMEZ
     → m urun: (m-1) P-kurali yaz
□ 5. Dissipative bilesen mi?
     → Evet: Yontem A, B veya C sec
     → Hayir: Standart devam
□ 6. Dis kaynak akisi var mi?
     → Evet: Sinir kosulu yaz (c bilinen)
     → Hayir: Devam
□ 7. Denklem sayisi dogrulamasi:
     n_toplam_denklem = n_bilesen + n_yardimci + n_sinir = n_bilinmeyen ?
```

### 9.2 Yaygin Hatalar

| Hata | Dogru Yaklasim |
|------|----------------|
| F-kuralini urun tarafina uygulamak | F-kurali yalnizca YAKIT exergy farklari icin |
| P-kuralini yakit tarafina uygulamak | P-kurali yalnizca URUN exergy farklari icin |
| Hem sinir kosulu hem F-kurali ayni akisa vermek | Ayni akis icin yalnizca bir kaynak kullan |
| Dissipative bilesen icin P tanimi zorlamak | Dissipative bilesen icin ozel yontemlerden birini sec |
| Denklem sayisini kontrol etmemek | Her zaman n_bilinmeyen = n_toplam_denklem dogrula |
| Negatif exergy farki gorunce kurali ters uygulamak | F/P tanimini gozden gecir, farklar her zaman pozitif olmali |
| Is akislarini bilinmeyen saymamak | c_W da bir bilinmeyendir, denklem sayisina dahil et |
| Cevre akislarini (c=0) unutmak | Her cevre akisi bir sinir kosulu denklemidir |

## İlgili Dosyalar

- `factory/exergoeconomic/speco_method.md` -- SPECO metodunun 4 temel adimi ve genel cerceve
- `factory/exergoeconomic/fuel_product_definitions.md` -- Tum ekipman tipleri icin detayli F/P tanimlari
- `factory/exergoeconomic/exergoeconomic_balance.md` -- Maliyet denge denklemlerinin formul detaylari
- `factory/exergoeconomic/matrix_formulation.md` -- Matris formulasyonu ve Python ile cozum
- `factory/exergoeconomic/cost_equations.md` -- PEC korelasyonlari ve Z hesaplamalari
- `factory/exergoeconomic/levelized_cost.md` -- CRF ve seviyelendirilmis maliyet hesabi
- `factory/exergoeconomic/overview.md` -- Exergoekonomik analize genel bakis

## Referanslar

1. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs in thermal systems." *Energy*, 31(8-9), 1257-1289.
2. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Bolum 8: Thermoeconomic Analysis and Optimization.
3. Tsatsaronis, G. (2008). "Recent developments in exergy analysis and exergoeconomics." *Int. J. Exergy*, 5(5-6), 489-499.
4. Tsatsaronis, G., Winhold, M. (1985). "Exergoeconomic analysis and evaluation of energy-conversion plants." *Energy*, 10(1), 69-94.
5. Tsatsaronis, G., Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
6. Lazzaretto, A., Tsatsaronis, G. (1999). "On the quest for objective equations in exergy costing." *Proceedings of the ASME Advanced Energy Systems Division*, 39, 197-208.
7. Valero, A., Lozano, M.A., Serra, L., Torres, C. (1994). "Application of the exergetic cost theory to the CGAM problem." *Energy*, 19(3), 365-381.
