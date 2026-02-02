---
title: "Toplam Tesis Analizi (Total Site Analysis)"
category: factory
equipment_type: factory
keywords: [total site, site profili, buhar seviye, çoklu proses, site entegrasyon]
related_files: [factory/pinch/fundamentals.md, factory/pinch/utility_systems.md, factory/pinch/grand_composite.md, factory/pinch/batch_integration.md]
use_when: ["Çoklu proses entegrasyonu yapılırken", "Site seviyesi buhar optimizasyonu yapılırken", "Total site hedefleri belirlenirken"]
priority: medium
last_updated: 2026-02-01
---

# Toplam Tesis Analizi (Total Site Analysis)

> Son güncelleme: 2026-02-01

## Genel Bakis

Toplam Tesis Analizi (Total Site Analysis — TSA), Dhole ve Linnhoff tarafindan 1993 yilinda gelistirilen, bir sanayi tesisindeki birden fazla proses biriminin ortak utility sistemi uzerinden entegrasyonunu sistematik olarak ele alan bir metodolojidir. Geleneksel pinch analizi tek bir proses biriminin icindeki isi degisim firsatlarini belirlerken, TSA tesisin tamamindaki proses birimlerini bir arada degerlendirerek site seviyesinde minimum enerji tuketimi, optimum buhar seviye sayisi ve sicakliklari ile kojenerasyon (CHP) potansiyelini hedefler.

Tipik bir endustriyel tesiste (rafineri, petrokimya kompleksi, gida kampusu) birden fazla proses birimi vardir ve her birinin kendi isi ihtiyaci bulunur. Bu proses birimleri, merkezi bir buhar sistemi uzerinden isi alis-verisi yapar. TSA, bu yapiyi analiz ederek:

- Her proses biriminin disari verdigi isiyi (source) ve disaridan aldigi isiyi (sink) tanimlar
- Site seviyesinde toplam isi kaynagi ve isi talebi profillerini olusturur
- Optimum buhar basinc seviyelerini ve CHP hedeflerini belirler
- Site genelinde CO2 emisyon hedeflerini hesaplar

Endustriyel uygulamalarda TSA, tipik olarak **%10-30** ek enerji tasarrufu saglar (bireysel proses pinch analizinin otesinde).

## 1. Total Site Kavrami (Total Site Concept)

### 1.1 Dhole & Linnhoff 1993 Yaklasimi

Dhole ve Linnhoff, 1993 yilinda yayimladiklari calisma ile endustriyel tesislerin butunsel enerji analizine sistematik bir cerceve sunmuslardir. Temel fikir, her proses biriminin Grand Composite Curve (GCC) egirisinden yola cikarak, site seviyesinde toplam kaynak ve talep profillerinin olusturulmasidir.

```
Klasik Pinch Analizi vs Total Site Analizi:

Klasik Pinch:
  - Tek proses birimi analiz edilir
  - Proses ici isi degisimi maksimize edilir
  - Utility ihtiyaci minimize edilir
  - Kapsam: tek birim

Total Site Analizi:
  - Tum proses birimleri birlikte analiz edilir
  - Prosesler arasi (utility uzerinden) isi degisimi hedeflenir
  - Site seviyesinde utility ve CHP optimize edilir
  - Kapsam: tum tesis
```

### 1.2 Temel Terminoloji

| Terim | Aciklama |
|---|---|
| Process Unit (Proses Birimi) | Bagimsiz olarak analiz edilebilen uretim birimi |
| Utility System (Utility Sistemi) | Buhar, sicak su, sogutma suyu saglayan merkezi sistem |
| Steam Main (Buhar Ana Hatti) | Belirli basinc seviyesindeki buhar dagitim hatti |
| Site Source Profile | Proses birimlerinin utility sistemine verdigi toplam isi |
| Site Sink Profile | Proses birimlerinin utility sisteminden aldigi toplam isi |
| Site Pinch (Site Darbogazlari) | Site seviyesinde isi transferinin kisitlandigi noktalar |
| Site Composite Curves | Site kaynak ve talep profillerinin birlestirilmisi |

### 1.3 Metodolojinin Adim Adim Ozeti

```
Adim 1: Her proses birimi icin bagimsiz pinch analizi yap
         → GCC egrisini olustur

Adim 2: Her GCC'den utility ile iliskili isi cebi (heat pocket) bilgisini cikar
         → Prosesin utility'ye verdigi isi (source)
         → Prosesin utility'den aldigi isi (sink)

Adim 3: Tum birimlerin source'larini birlestir → Site Source Profile
         Tum birimlerin sink'lerini birlestir → Site Sink Profile

Adim 4: Site Source ve Sink profillerini ayni grafige ciz
         → Site Composite Curves

Adim 5: Site seviyesi hedefleri hesapla
         → Minimum sicak utility (QH,site)
         → Minimum soguk utility (QC,site)
         → Maksimum CHP potansiyeli

Adim 6: Buhar seviye sayisini ve sicakliklarini optimize et

Adim 7: Emisyon hedeflerini hesapla
```

## 2. Site Profilleri (Site Profiles)

### 2.1 Site Source Profile (Site Kaynak Profili)

Site Source Profile, tum proses birimlerinin utility sistemine (buhar sistemine) verebilecegi toplam isiyi sicakliga gore gosteren egrisidir. Her proses biriminin GCC egrisindeki "utility'ye isi veren" kismindan turetilir.

```
Olusturma Algoritması:

Adim 1: Her proses biriminin GCC'sini ciz
Adim 2: GCC'nin pinch noktasinin altindaki (sogutma gerektiren) bolgeyi
         sifir cizgisine gore ayristir
Adim 3: Isi ceplerini cikar (cepler proses ici degisimdir, utility'yi icermez)
Adim 4: Kalan source egrisini alin
Adim 5: Tum birimlerin source egrilerini enthalpy ekseninde toplayarak birlestirin
```

### 2.2 Site Sink Profile (Site Talep Profili)

Site Sink Profile, tum proses birimlerinin utility sisteminden almasi gereken toplam isiyi sicakliga gore gosteren egrisidir. GCC egrisinin pinch uzerindeki (isitma gerektiren) kismindan turetilir.

```
Site Sink Profile olusturma adimları:

Adim 1: Her proses biriminin GCC'sini ciz
Adim 2: GCC'nin pinch noktasinin ustundeki (isitma gerektiren) bolgeyi sec
Adim 3: Isi ceplerini cikar
Adim 4: Kalan sink egrisini alin
Adim 5: Tum birimlerin sink egrilerini enthalpy ekseninde toplayarak birlestirin
```

### 2.3 Referans Ornek: Uc Proses Birimli Tesis

Asagidaki referans ornek, TSA metodolojisini gostermek icin kullanilacaktir:

| Proses | Aciklama | QH,min [kW] | QC,min [kW] | Pinch [°C] |
|---|---|---|---|---|
| P1 — Distilasyon | Ham petrol damitma | 4,200 | 3,800 | 180 |
| P2 — Reaksiyon | Kimyasal reaktor | 2,600 | 1,900 | 120 |
| P3 — Kurutma | Urun kurutma | 1,800 | 2,200 | 85 |

```
Site Toplam Utility Ihtiyaci (entegrasyon OLMADAN):
  QH,toplam = 4,200 + 2,600 + 1,800 = 8,600 kW
  QC,toplam = 3,800 + 1,900 + 2,200 = 7,900 kW
```

### 2.4 ASCII Site Profil Diyagrami

```
   T [°C]
    |
300 |                          Sink Profile
    |                         /
250 |                        /
    |                       /          Source Profile
200 |           ___________/          /
    |          /                     /
150 |         /                     /
    |        /              _______/
100 |       /              /
    |      /              /
 50 |     /              /
    |    /              /
  0 |___/___________/__/____________________> Q [kW]
    0   1000  2000  3000  4000  5000  6000

  Sink Profile: Proseslerin utility'den istedigi isi (isitma talebi)
  Source Profile: Proseslerin utility'ye verdigi isi (sogutma kaynak)
```

## 3. Site Bilesik Egrileri (Site Composite Curves)

### 3.1 Site Composite Curve Olusturma

Site Composite Curves, Site Source Profile ile Site Sink Profile'in ayni grafik uzerinde cizilmesiyle elde edilir. Bu egriler, site seviyesindeki isi transferi potansiyelini ve minimum utility ihtiyacini gosterir.

```
Site Composite Curve Yorumlama:

   T [°C]
    |
    |           Site Sink           Site Source
    |          (isitma talebi)     (sogutma kaynak)
300 |              /                    |
    |             /                     |
250 |     -------/                      |
    |    /       QH,site ←              |
200 |   /   (minimum sicak utility)     |
    |  /                          \     |
150 | /            ORTUSME          \   |
    |/         (site uzerinden       \  |
100 |           isi transferi)        \ |
    |                            ------\|
 50 |              QC,site →            \
    |         (minimum soguk utility)    \
  0 |________________________________________> Q [kW]

  QH,site: Site seviyesi minimum sicak utility
  QC,site: Site seviyesi minimum soguk utility
  Ortusme: Utility sistemi uzerinden prosesler arasi isi transferi
```

### 3.2 Site Seviyesi Enerji Hedefleri

Site Composite Curves'ten hesaplanan hedefler:

```
Referans ornek icin (entegrasyon ILE):
  QH,site = 6,400 kW    (entegrasyon olmadan: 8,600 kW)
  QC,site = 5,700 kW    (entegrasyon olmadan: 7,900 kW)

  Site entegrasyon tasarrufu:
  DeltaQH = 8,600 - 6,400 = 2,200 kW  (%25.6 azalma)
  DeltaQC = 7,900 - 5,700 = 2,200 kW  (%27.8 azalma)
```

### 3.3 Site Pinch Kavrami

Site Pinch, site composite curves'un birbirine en yakin oldugu sicaklik noktasidir. Geleneksel pinch'ten farki, site pinch utility sistemi parametreleri (buhar seviyeleri) tarafindan belirlenir.

```
Site Pinch ozellikleri:
  - Genellikle bir buhar seviyesine denk gelir
  - Site pinch'te utility sistemi darbogazdadir
  - Site pinch uzerinde isitma, altinda sogutma yapilmalidir (klasik kural)
  - Birden fazla site pinch olusabilir (her buhar seviyesinde bir tane)
```

## 4. Buhar Seviye Optimizasyonu (Steam Level Optimization)

### 4.1 Buhar Seviyeleri ve Site Entegrasyonu

Endustriyel tesislerde buhar, farkli basinc seviyelerinde uretilir ve dagitilir. Her buhar seviyesi belirli bir sicaklik ve basinc araligi sunar:

| Buhar Seviyesi | Tipik Basinc [bar] | Doyma Sicakligi [°C] | Tipik Kullanim |
|---|---|---|---|
| VHP (Very High Pressure) | 80-120 | 295-324 | Turbin girisi |
| HP (High Pressure) | 30-50 | 234-264 | Yuksek sicaklik prosesler |
| MP (Medium Pressure) | 8-15 | 170-198 | Orta sicaklik prosesler |
| LP (Low Pressure) | 2-5 | 120-152 | Dusuk sicaklik prosesler, isitma |
| LLP (Very Low Pressure) | 1.0-1.5 | 100-111 | Degazor, iz isitma |

### 4.2 Optimum Buhar Seviye Sayisi

Buhar seviye sayisinin belirlenmesi bir ekonomik optimizasyon problemidir:

```
Az buhar seviyesi (ornegin 2):
  + Basit sistem, dusuk yatirim
  + Kolay isletme ve bakim
  - Buyuk sicaklik farklarinda isi transferi → exergy kaybi yuksek
  - CHP potansiyeli sinirli

Cok buhar seviyesi (ornegin 5):
  + Kucuk sicaklik farklarinda isi transferi → exergy kaybi dusuk
  + Yuksek CHP potansiyeli
  - Karmasik sistem, yuksek yatirim
  - Operasyonel zorluklar

Tipik optimum: 3-4 buhar seviyesi (HP, MP, LP ve bazen LLP)
```

### 4.3 Buhar Seviye Sicakliginin Belirlenmesi

Optimum buhar seviyesi sicakliklari, Site Composite Curves uzerinden belirlenir:

```
Optimizasyon Algoritmasi:

Adim 1: Site Source ve Sink profillerini ciz
Adim 2: Mevcut buhar seviyelerini yatay cizgiler olarak ekle
Adim 3: Her buhar seviyesinde transfer edilen isiyi hesapla:
         Q_transfer,i = min(Q_source,i , Q_sink,i)
Adim 4: Toplam site isi geri kazanimini maksimize eden
         buhar seviyesi sicakliklari T*_steam,i icin optimize et:

         max SUM_i [ Q_transfer,i(T_steam,i) ]

         Kisitlar:
         - T_steam,i > T_steam,i+1  (sicaklik sirasi korunmali)
         - DeltaT_min,site >= 20°C  (site seviyesi minimum yaklasim)
         - Buhar basinclari standart degerlere yakin olmali
```

### 4.4 Buhar Ana Hatti Basinc Optimizasyonu

```
Ornek: MP buhar seviyesi optimizasyonu

Mevcut MP buhar: 10 bar (180°C)
Alternatifler:
  8 bar (170°C)  → Daha fazla LP uretimi, ancak daha az MP kullanici
  12 bar (188°C) → Daha fazla MP kullanici, ancak daha az turbin isi

Degerlendirme kriterleri:
  1. Site isi geri kazanimi [kW]
  2. CHP gucu [kW_e]
  3. Toplam yillik maliyet [EUR/yil]
  4. CO2 emisyonu [ton/yil]

Optimum, tum kriterlerin agirlikli toplami ile belirlenir.
```

## 5. CHP Hedefleme (CHP Targeting at Site Level)

### 5.1 Site Seviyesi Kojenerasyon Potansiyeli

Total Site Analysis, site genelinde kojenerasyon (Combined Heat and Power) potansiyelini belirlemek icin guclu bir aractir. GCC egirileri ve site profilleri kullanilarak, her buhar seviyesinde ne kadar isi gerektigini ve bu isinin ne kadarinin buhar turbinleri uzerinden guc uretirken saglanabilecegi hesaplanir.

```
CHP Hedefleme Formulu:

Turbin isi dusumu (isentropic):
  W_turbin = m_buhar × (h_giris - h_cikis) [kW]

Burada:
  m_buhar = buhar kutle debisi [kg/s]
  h_giris = turbin giris entalpisi [kJ/kg]
  h_cikis = turbin cikis entalpisi [kJ/kg]

Site seviyesi toplam CHP gucu:
  W_CHP,site = SUM_j [ m_j × (h_j,in - h_j,out) × eta_is,j ]

Burada j, turbin kademelerini temsil eder:
  j=1: VHP → HP
  j=2: HP → MP
  j=3: MP → LP
  j=4: LP → LLP (veya kondens)
```

### 5.2 Shaft Work Hedefleme (Shaft Work Targeting)

Shaft work hedefleme, buhar turbinlerinden elde edilebilecek maksimum mekanik/elektrik gucunu belirler:

```
                    VHP Buhar (100 bar, 540°C)
                         |
                    +----+----+
                    | Turbin  |
                    | Kademe 1|
                    +----+----+
                         |  W1 = guç
                    HP Buhar (40 bar)
                    /         \
              Proses P1     +----+----+
              (QHP kW)      | Turbin  |
                            | Kademe 2|
                            +----+----+
                                 |  W2 = guç
                            MP Buhar (10 bar)
                            /         \
                      Proses P2     +----+----+
                      (QMP kW)      | Turbin  |
                                    | Kademe 3|
                                    +----+----+
                                         |  W3 = guç
                                    LP Buhar (3 bar)
                                         |
                                    Proses P3
                                    (QLP kW)
```

### 5.3 R-Egrisi (R-Curve: Fuel vs Power)

R-egrisi, bir tesisin yakit tuketimi ile guc uretimi arasindaki iliskiyi gosteren temel bir TSA aracidir. Farkli isletme stratejilerinin karsilastirilmasini saglar.

```
R-Curve (Yakit - Guc Egrisi):

  W [MW_e]
    |
    |                          * Maksimum guc
    |                        /   (full condensing)
    |                      /
    |                    /
    |                  * Optimum CHP noktasi
    |                /
    |              /
    |            /
    |          * Sadece isi
    |        /   (no power)
    |      /
    |____/___________________________________> F [MW_th]
    0    20    40    60    80    100

  R = W / F  (guc/yakit orani)

  R degerleri:
    R = 0     : Sadece isi uretimi (kazan)
    R = 0.05-0.15 : Geri basinc turbini (back-pressure)
    R = 0.25-0.40 : Karsit basinc + kondensasyon turbini
    R = 0.35-0.45 : Gaz turbini + HRSG (kojenerasyon)
    R > 0.50  : Kombine cevrim (CCGT)
```

### 5.4 CHP Hedefleme Hesaplama Ornegi

```
Referans tesis icin CHP hedefleme:

Site isi talepleri (Site Sink Profile'den):
  QHP  = 2,400 kW  (HP buhar, 40 bar)
  QMP  = 3,200 kW  (MP buhar, 10 bar)
  QLP  = 1,800 kW  (LP buhar, 3 bar)
  Toplam: Q_site = 7,400 kW

VHP buhar uretimi (kazan): 100 bar, 540°C
  h_VHP = 3,540 kJ/kg

Turbin kademe performanslari (eta_is = 0.80):
  VHP → HP:  Dh = 280 kJ/kg  → W_spesifik = 224 kW/(kg/s)
  HP → MP:   Dh = 340 kJ/kg  → W_spesifik = 272 kW/(kg/s)
  MP → LP:   Dh = 260 kJ/kg  → W_spesifik = 208 kW/(kg/s)

Buhar debi hesabi:
  m_HP = Q_HP / Dh_HP = 2,400 / 2,100 = 1.14 kg/s
  m_MP = Q_MP / Dh_MP = 3,200 / 2,015 = 1.59 kg/s
  m_LP = Q_LP / Dh_LP = 1,800 / 1,890 = 0.95 kg/s

Toplam CHP gucu:
  W_CHP = (m_HP+m_MP+m_LP)×224 + (m_MP+m_LP)×272 + m_LP×208
  W_CHP = 3.68×224 + 2.54×272 + 0.95×208
  W_CHP = 824 + 691 + 198
  W_CHP = 1,713 kW_e

Yakit tuketimi (kazan verimi %90):
  F = (Q_site + W_CHP/eta_gen) / eta_kazan
  F = (7,400 + 1,713/0.95) / 0.90
  F = (7,400 + 1,803) / 0.90
  F = 10,226 kW_th

R = W_CHP / F = 1,713 / 10,226 = 0.168
```

## 6. Emisyon Hedefleme (Emissions Targeting)

### 6.1 Site Seviyesi CO2 Hedefleri

TSA, site seviyesinde CO2 emisyon hedeflerini belirlemek icin kullanilabilir. Yaklaşim, minimum yakit tuketimi hedefinden CO2 emisyonunu hesaplamaktir.

```
CO2 Emisyon Hesabi:

Emisyon = F × EF × t [ton CO2/yil]

Burada:
  F   = yakit tuketimi [kW_th]
  EF  = emisyon faktoru [kg CO2/kWh_th]
  t   = yillik calisma suresi [saat/yil]

Tipik emisyon faktorleri:
  Dogal gaz:    0.205 kg CO2/kWh
  Fuel oil:     0.279 kg CO2/kWh
  Komur:        0.341 kg CO2/kWh
  Biyokutle:    0.025 kg CO2/kWh (sadece dolaylı)
  Elektrik (TR):0.480 kg CO2/kWh (sebeke ortlamasi)
```

### 6.2 Yakit Karisimi Optimizasyonu (Fuel Mix Optimization)

```
Optimizasyon Problemi:

  min  SUM_k [ F_k × EF_k ]     (toplam CO2 minimizasyonu)

  Kisitlar:
  SUM_k [ F_k ] >= F_site,min    (minimum yakit ihtiyaci karsilanmali)
  F_k >= 0                        (negatif yakit olamaz)
  F_k <= F_k,max                  (her yakitin kapasitesi sinirli)

Burada k, yakit turlerini temsil eder (dogal gaz, fuel oil, biyokutle vb.)
```

### 6.3 Emisyon Azaltma Stratejileri

| Strateji | CO2 Azaltma Potansiyeli | Maliyet Seviyesi |
|---|---|---|
| Site isi entegrasyonu (TSA) | %10-25 | Dusuk-Orta |
| CHP optimizasyonu | %5-15 | Orta |
| Yakit degisimi (komur → dogal gaz) | %30-45 | Orta-Yuksek |
| Biyokutle katilimi | %15-40 | Orta |
| Elektrikli isitma (yesil elektrik) | %40-80 | Yuksek |
| Karbon yakalama (CCS) | %85-95 | Cok Yuksek |

## 7. Site Entegrasyon Stratejileri (Site Integration Strategies)

### 7.1 Dogrudan vs Dolayli Entegrasyon (Direct vs Indirect Integration)

```
Dogrudan Entegrasyon (Direct Integration):
  - Iki proses birimi arasinda dogrudan isi degistirici kullanilir
  - Utility sistemi bypass edilir
  - Avantaj: Dusuk exergy kaybi, yuksek verimlilik
  - Dezavantaj: Proses birimleri bagimsizligini kaybeder,
    bakimda bir birim durdugunda diger de etkilenir
  - Mesafe sinirlamasi: genellikle < 100 m

  P1 ←—[Isi Degistirici]—→ P2

Dolayli Entegrasyon (Indirect / Utility-Mediated Integration):
  - Prosesler arasi isi transferi utility sistemi uzerinden yapilir
  - Bir proses buhar uretir, diger proses bu buhari kullanir
  - Avantaj: Proses bagimsizligi korunur, esnek isletme
  - Dezavantaj: Ek exergy kaybi (buhar uretim/tuketim farki)
  - Mesafe sinirlamasi yok (buhar borulari ile)

  P1 →[Buhar Uretimi]→ Buhar Hatti →[Buhar Tuketimi]→ P2
```

### 7.2 Utility-Aracili Entegrasyon Turleri

| Entegrasyon Turu | Mekanizma | DeltaT Kaybi | Esneklik |
|---|---|---|---|
| Buhar uretimi → buhar tuketimi | Isitici/sogutucu | 15-30°C | Yuksek |
| Sicak su cevrimi | Ara akiskan | 10-20°C | Orta |
| Termal yag cevrimi | Ara akiskan | 10-25°C | Orta |
| Dogrudan isi degisimi | Isi degistirici | 5-10°C | Dusuk |
| Isı depolama (TES) | Tank/PCM | 5-15°C | Cok Yuksek |

### 7.3 Buhar Ana Hatti Modifikasyonlari (Steam Main Modifications)

TSA sonuclarina gore buhar sisteminde yapilabilecek modifikasyonlar:

```
Modifikasyon 1: Yeni buhar seviyesi ekleme
  Mevcut: HP (40 bar) — LP (3 bar)
  Oneril: HP (40 bar) — MP (10 bar) — LP (3 bar)
  Etki: +350 kW isi geri kazanimi, +120 kW_e CHP

Modifikasyon 2: Buhar seviyesi basincini degistirme
  Mevcut: MP = 10 bar (180°C)
  Oneril: MP = 12 bar (188°C)
  Etki: +180 kW isi geri kazanimi (daha fazla sink karsilanir)

Modifikasyon 3: Vent buharini geri kazanma
  Mevcut: LP fazla buhari atmosfere atiliyor (200 kW kayip)
  Oneril: Absorpsiyon chiller ile sogutma uretimi
  Etki: 200 kW isi geri kazanimi, 50 kW sogutma

Modifikasyon 4: Kondensat geri kazanimi iyilestirme
  Mevcut: %60 kondensat geri donus orani
  Oneril: Flash buhar geri kazanimi + kondensat pompasi
  Etki: +280 kW isi, +15 kW_e pompa tasarrufu
```

### 7.4 Entegrasyon Karar Matrisi

```
Karar Agaci: Hangi entegrasyon yontemi secilmeli?

  Prosesler arasi mesafe < 100 m?
  |— Evet → Isi yukleri surekli ve eslesik mi?
  |         |— Evet → DOGRUDAN ENTEGRASYON
  |         |— Hayir → ISIL DEPOLAMA (TES) + dogrudan
  |
  |— Hayir → Buhar sistemi mevcut mu?
              |— Evet → UTILITY-ARACILI ENTEGRASYON
              |         (buhar uretim/tuketim)
              |
              |— Hayir → Yatirim fizibilitesi uygun mu?
                         |— Evet → YENİ BUHAR HATTI DÖSEME
                         |— Hayir → BAGIMSIZ ISLETME
```

## 8. Endustriyel Ornekler (Industrial Examples)

### 8.1 Petrol Rafinerisi (Petroleum Refinery)

```
Tesis: Orta olcekli rafineri (150,000 bbl/gun)
Proses birimleri:
  - CDU (Crude Distillation Unit): QH=45 MW, QC=38 MW
  - VDU (Vacuum Distillation Unit): QH=22 MW, QC=18 MW
  - HDS (Hydrodesulfurization): QH=12 MW, QC=9 MW
  - CCR (Catalytic Reformer): QH=8 MW, QC=15 MW
  - FCC (Fluid Catalytic Cracker): QH=5 MW, QC=25 MW

Mevcut durum:
  Toplam yakit tuketimi: 120 MW_th
  Toplam CHP gucu: 18 MW_e
  CO2 emisyonu: 210,000 ton/yil

TSA sonuclari:
  Minimum yakit hedefi: 95 MW_th  (%20.8 azalma)
  Optimum CHP gucu: 28 MW_e  (%55.6 artis)
  CO2 hedefi: 166,000 ton/yil  (%21.0 azalma)

Anahtar onlem:
  - CDU/VDU arasinda MP buhar entegrasyonu (+8 MW geri kazanim)
  - FCC atik isisini LP buhar olarak geri kazanma (+6 MW)
  - VHP→HP→MP→LP kademe turbini (+10 MW_e)

Yatirim: 12 MEUR, Geri odeme: 2.1 yil
```

### 8.2 Petrokimya Kompleksi (Petrochemical Complex)

```
Tesis: Entegre petrokimya kompleksi
Proses birimleri:
  - Etilen kraker: QH=85 MW, QC=110 MW
  - Polietilen: QH=15 MW, QC=25 MW
  - PVC: QH=8 MW, QC=12 MW
  - VCM: QH=18 MW, QC=22 MW
  - Aromatik uretim: QH=30 MW, QC=35 MW

Mevcut durum:
  Toplam yakit tuketimi: 220 MW_th
  CHP gucu: 45 MW_e
  Buhar seviyeleri: VHP (100 bar), HP (40 bar), MP (10 bar), LP (3 bar)

TSA sonuclari:
  Minimum yakit hedefi: 175 MW_th  (%20.5 azalma)
  Optimum CHP: 62 MW_e  (%37.8 artis)
  Optimum buhar seviyeleri:
    VHP: 100 bar (degisiklik yok)
    HP: 42 bar (2 bar artis → daha iyi hedefleme)
    MP: 12 bar (2 bar artis → daha fazla MP sink karsilanir)
    LP: 3.5 bar (0.5 bar artis → degazor sicakligi uyumu)
    LLP: 1.5 bar (yeni seviye → iz isitma ve degazor)

Tasarruf: 45 MW_th yakit + 17 MW_e ek guc
Yatirim: 35 MEUR, Geri odeme: 2.8 yil
```

### 8.3 Gida Isleme Kampusu (Food Processing Campus)

```
Tesis: Coklu gida uretim kampusu
Proses birimleri:
  - Sut isleme: QH=3.2 MW, QC=2.8 MW, Pinch=72°C
  - Bira fabrikasi: QH=4.5 MW, QC=3.9 MW, Pinch=65°C
  - Et isleme: QH=2.1 MW, QC=1.8 MW, Pinch=55°C
  - Paketleme: QH=0.8 MW, QC=0.5 MW, Pinch=45°C

Mevcut durum:
  Toplam yakit: 14.5 MW_th (dogal gaz)
  Buhar: Tek seviye LP (5 bar, 152°C)
  CO2: 25,200 ton/yil

TSA sonuclari:
  Minimum yakit hedefi: 11.2 MW_th  (%22.8 azalma)
  Optimum buhar seviyeleri:
    MP: 8 bar (170°C) — yeni seviye
    LP: 3 bar (134°C) — mevcut 5 bar'dan dusuruldu
    Sicak su: 85°C — yeni ara utility

  Onemli bulgular:
  - Bira fabrikasi kaynama/sogutma isisi → sut pastorizasyonu
  - Et isleme sogutma reject isisi → paketleme isitma
  - Sicak su cevrimi ile 3 tesis arasinda entegrasyon

Tasarruf: 3.3 MW_th yakit, 5,700 ton CO2/yil
Yatirim: 2.8 MEUR, Geri odeme: 3.2 yil
```

### 8.4 Endustriyel Orneklerin Karsilastirmasi

| Parametre | Rafineri | Petrokimya | Gida Kampusu |
|---|---|---|---|
| Proses sayisi | 5 | 5 | 4 |
| Toplam QH [MW] | 92 | 156 | 10.6 |
| Yakit tasarrufu [%] | 20.8 | 20.5 | 22.8 |
| CHP artisi [%] | 55.6 | 37.8 | — |
| CO2 azaltma [%] | 21.0 | ~20 | 22.6 |
| Geri odeme [yil] | 2.1 | 2.8 | 3.2 |
| Anahtar entegrasyon | MP buhar | Buhar seviye opt. | Sicak su cevrimi |

## 9. TSA Uygulama Kontrol Listesi

```
[ ] 1. Her proses birimi icin akis verilerini topla
[ ] 2. Her proses birimi icin bagimsiz pinch analizi yap
[ ] 3. Her birimin GCC egrisini olustur
[ ] 4. GCC'lerden source ve sink profillerini cikar
[ ] 5. Site Source ve Sink profillerini olustur
[ ] 6. Site Composite Curves'u ciz
[ ] 7. Site seviyesi enerji hedeflerini hesapla
[ ] 8. Mevcut buhar seviyelerini analiz et
[ ] 9. Optimum buhar seviye sayisini ve sicakliklarini belirle
[ ] 10. CHP hedeflerini hesapla (shaft work, R-curve)
[ ] 11. CO2 emisyon hedeflerini hesapla
[ ] 12. Entegrasyon stratejisini sec (dogrudan/dolayli)
[ ] 13. Yatirim maliyetini ve geri odeme suresini hesapla
[ ] 14. Uygulama yol haritasini hazirla
```

## İlgili Dosyalar

- [Pinch Analizi Temelleri](fundamentals.md) -- Linnhoff metodolojisi, MER hedefleri, 3 altin kural
- [Grand Composite Curve](grand_composite.md) -- GCC olusturma, isi cebi, utility yerlestirme
- [Utility Sistemleri](utility_systems.md) -- Coklu utility seviyeleri, CHP, isi pompasi
- [Batch Entegrasyon](batch_integration.md) -- Kesikli proseslerde isi entegrasyonu
- [Pinch Analizi Ana Dosyasi](../pinch_analysis.md) -- Temel pinch kavramlari
- [Fabrika Isi Entegrasyonu](../heat_integration.md) -- Kaynak-kullanim eslestirme
- [Capraz Ekipman Optimizasyonu](../cross_equipment.md) -- Ekipmanlar arasi firsatlar
- [Kojenerasyon](../cogeneration.md) -- CHP sistemleri detayli analiz

## Referanslar

- Dhole, V.R. & Linnhoff, B., "Total Site Targets for Fuel, Co-generation, Emissions, and Cooling," Computers & Chemical Engineering, Vol. 17, Suppl. 1, pp. S101-S109, 1993
- Linnhoff, B. et al., "User Guide on Process Integration for the Efficient Use of Energy," IChemE, Rugby, UK, 1994
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," 2nd Edition, Butterworth-Heinemann, 2007
- Klemes, J.J. (Ed.), "Handbook of Process Integration (PI): Minimisation of Energy and Water Use, Waste and Emissions," Woodhead Publishing, 2013
- Klemes, J.J., Dhole, V.R., Raissi, K., Perry, S.J. & Puigjaner, L., "Targeting and Design Methodology for Reduction of Fuel, Power and CO2 on Total Sites," Applied Thermal Engineering, Vol. 17, No. 8-10, pp. 993-1003, 1997
- Raissi, K., "Total Site Integration," PhD Thesis, UMIST, Manchester, 1994
- Perry, S., Klemes, J. & Bulatov, I., "Integrating Waste and Renewable Energy to Reduce the Carbon Footprint of Locally Integrated Energy Sectors," Energy, Vol. 33, No. 10, pp. 1489-1497, 2008
- Varbanov, P.S., Doyle, S. & Smith, R., "Modelling and Optimization of Utility Systems," Chemical Engineering Research and Design, Vol. 82, No. A5, pp. 561-578, 2004
