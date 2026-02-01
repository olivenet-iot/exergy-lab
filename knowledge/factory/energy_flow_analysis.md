# Enerji Akis Analizi ve Sankey Diyagramlari (Energy Flow Analysis and Sankey Diagrams)

> Son güncelleme: 2026-01-31

## Genel Bakis

Enerji akis analizi, bir endustriyel tesisin tum enerji giris, donusum, dagilim ve cikis noktalarini sistematik olarak haritalandiran temel bir enerji denetim aracidir. Bu analiz, Sankey diyagramlari araciligiyla gorsellestirildiginde, enerji kayiplarinin buyuklugunu ve konumunu sezgisel olarak ortaya koyar. Termodinamigin birinci yasasina (enerji korunumu) dayanan bu yaklasim, fabrika seviyesinde enerji dengesinin kurulmasinin ilk adimidir.

Bu dosya; enerji dengesi metodolojisi, Sankey diyagrami insasi, olcum tabanli ve hesaplama tabanli denge yaklasimlarini, fabrika seviyesinde enerji dagilim analizini, tipik endustriyel enerji akis paternlerini ve denge kapanma kriterlerini kapsar.

## 1. Enerji Dengesi Metodolojisi (Energy Balance Methodology)

### 1.1 Temel Prensip

Termodinamigin birinci yasasi geregi, bir kontrol hacmine giren toplam enerji, cikan toplam enerjiye esittir (kararli hal):

```
E_giris = E_cikis + E_kayip + dE_depo/dt

Kararli hal icin (dE_depo/dt = 0):
E_giris = E_faydali + E_atik

Burada:
- E_giris    = Tum enerji giris kalemleri [kW veya kWh/yil]
- E_faydali  = Faydali urun ve prosese aktarilan enerji [kW]
- E_atik     = Tum enerji kayiplari (baca gazi, yuzey, sogutma vb.) [kW]
```

### 1.2 Enerji Dengesi Adim Adim Sureci

```
Adim 1: Sistem sinirlarini tanimla (bkz. system_boundaries.md)
Adim 2: Tum enerji giris noktalarini belirle
Adim 3: Tum enerji cikis ve kayip noktalarini belirle
Adim 4: Her nokta icin debi, sicaklik, basinc olcumleri yap
Adim 5: Enerji degerlerini hesapla (kW veya kWh/yil)
Adim 6: Giris-cikis dengesini kontrol et (kapanma kriteri: +-5%)
Adim 7: Sankey diyagramini ciz
Adim 8: Kayip dagilimini analiz et ve iyilestirme firsatlarini belirle
```

### 1.3 Denge Kapanma Kriterleri (Balance Closure Criteria)

```
Kapanma hatasi = |E_giris - E_cikis| / E_giris x 100 [%]

Kabul edilebilir kapanma hatalari:

| Seviye       | Kapanma Hatasi | Degerlendirme                        |
|--------------|---------------|--------------------------------------|
| Mukemmel     | < +-2%        | Yuksek dogruluklu olcum sistemi      |
| Iyi          | +-2% — +-5%  | Standart endustriyel denetim         |
| Ortalama     | +-5% — +-10% | Kabul edilebilir, ek olcum onerisi   |
| Dusuk        | +-10% — +-15%| Onemli olcum eksiklikleri mevcut     |
| Kritik       | > +-15%       | Denge guvenilir degil, tekrar olcum  |

Not: +-5% standart kabul siniridir. Bu sinir asilirsa,
olcum noktalari ve hesaplamalar gozden gecirilmelidir.
```

## 2. Enerji Giris Kalemleri (Energy Input Items)

### 2.1 Birincil Enerji Kaynaklari

| Enerji Kalemi | Hesaplama | Tipik Birim | Donusum |
|---|---|---|---|
| Dogalgaz | V x LHV | Nm3/h | LHV = 34.5 MJ/Nm3 = 9.58 kWh/Nm3 |
| Elektrik (sebeke) | W_elektrik | kW | 1 kWh = 3.6 MJ |
| Fuel oil | m_dot x LHV | kg/h | LHV = 40.4 MJ/kg |
| LPG | m_dot x LHV | kg/h | LHV = 46.0 MJ/kg |
| Komur (linyit) | m_dot x LHV | kg/h | LHV = 10-20 MJ/kg (ture bagli) |
| Biyokutle | m_dot x LHV | kg/h | LHV = 12-18 MJ/kg (neme bagli) |
| Gunes enerjisi | A x G x eta | kW | G = isinim [kW/m2] |

### 2.2 Ikincil Enerji Kaynaklari

```
Ikincil kaynaklar (donusturulmus enerji):
- Buhar: Q_buhar = m_dot x (h_buhar - h_besleme) [kW]
- Sicak su: Q_su = m_dot x Cp x (T_cikis - T_giris) [kW]
- Basingli hava: W_hava = V_dot x P_fark / eta [kW]
- Sogutma: Q_sogutma = m_dot x Cp x (T_giris - T_cikis) [kW]
```

### 2.3 Birincil Enerji Donusumu

```
Birincil enerji esdeeri (Primary Energy Equivalent):

E_birincil = E_yakit / eta_kazan + E_elektrik / eta_santral

Burada:
- eta_kazan = Kazan verimi (tipik %85-92)
- eta_santral = Elektrik uretim ve iletim verimi (tipik %35-40)

Turkiye icin birincil enerji carpani:
- Elektrik: 2.36 (EPDK deger, 2025)
- Dogalgaz: 1.00
- Komur: 1.00
```

## 3. Enerji Kayip Kategorileri (Energy Loss Categories)

### 3.1 Kayip Siniflandirmasi

| Kayip Kategorisi | Aciklama | Tipik Pay | Olcum Yontemi |
|---|---|---|---|
| Baca gazi kaybi | Sicak gaz atimi | %5-20 | Baca gazi analizoru |
| Yuzey kaybi | Radyasyon + konveksiyon | %1-5 | IR termometre/kamera |
| Sogutma suyu kaybi | Atik isi | %10-30 | Debi + sicaklik |
| Buhar kapaklari | Kapaklardan kacak | %3-10 | Ultrasonik detektor |
| Basingli hava kacaklari | Hava kacaklari | %15-30 | Ultrasonik kacak dedektoru |
| Elektrik kayiplari | Motor, trafo, kablo | %3-8 | Guc analizoru |
| Proses atik isisi | Urun sogumasi, atik | %5-25 | Sicaklik olcumu |
| Buhar kondensat kaybi | Kondensat atimi | %5-15 | Kondensat debi olcumu |

### 3.2 Kayip Hesaplama Formulleri

```
1. Baca gazi kaybi:
   Q_baca = m_dot_bg x Cp_bg x (T_baca - T_ortam)

   Burada:
   - m_dot_bg = baca gazi kutle debisi [kg/s]
   - Cp_bg = baca gazi ozgul isisi (~1.05 kJ/kgK)
   - T_baca = baca gazi sicakligi [C]
   - T_ortam = ortam sicakligi [C]

2. Yuzey kaybi (silindirik yuzey):
   Q_yuzey = h_toplam x A x (T_yuzey - T_ortam)

   Burada:
   - h_toplam = toplam isi transfer katsayisi [W/m2K]
   - A = yuzey alani [m2]
   - h_toplam = h_konveksiyon + h_radyasyon (tipik 10-20 W/m2K izolasyonsuz)

3. Sogutma suyu kaybi:
   Q_sogutma = m_dot_su x Cp_su x (T_cikis - T_giris)

   Burada:
   - Cp_su = 4.186 kJ/kgK
```

## 4. Olcum Tabanli ve Hesaplama Tabanli Denge (Measurement vs. Calculation Based)

### 4.1 Olcum Tabanli Denge (Top-Down)

```
Yaklasim: Tum ana giris ve cikis noktalarinda dogrudan olcum
Avantajlar:
- Gercek operas yon kosullarini yansitir
- Sektorel karsilastirmaya uygun
- ISO 50001 uyumlu

Dezavantajlar:
- Kapsamli olcum ekipmani gerektirir
- Gecici olcumler temsil edici olmayabilir
- Yuksek maliyet
```

### 4.2 Hesaplama Tabanli Denge (Bottom-Up)

```
Yaklasim: Ekipman katalog degerleri, tasarim parametreleri ve ampirik formullere dayali
Avantajlar:
- Daha az olcum gerektirir
- On analiz icin uygun
- Dusuk maliyet

Dezavantajlar:
- Gercek performanstan sapma olabilir
- Ekipman yaslanmasi dikkate alinmayabilir
- Dogrulama gerektirir
```

### 4.3 Hibrit Yaklasim (Onerilen)

```
En iyi uygulama: Olcum + hesaplama birlesimi
1. Ana giris noktalari: Dogrudan olcum (sayac, debi olcer)
2. Buyuk kayip noktalari: Dogrudan olcum (baca gazi, sogutma)
3. Kucuk kayiplar: Hesaplama (yuzey kaybi, radyasyon)
4. Dogrulama: Kapanma hatasi kontrolu

Onerilen olcum suresi:
- Kararli hal prosesler: Minimum 1 saat surekli olcum
- Degisken yuklu prosesler: Minimum 24 saat (tercihen 1 hafta)
- Mevsimsel degisim: 4 mevsim temsili olcum
```

## 5. Olcum Gereksinimleri (Measurement Requirements)

### 5.1 Temel Olcum Ekipmanlari

| Olcum Noktasi | Ekipman | Dogruluk | Frekans |
|---|---|---|---|
| Elektrik tuketimi | Guc analizoru (3 fazli) | +-1% | 1 s (anlik), 15 dk (ort.) |
| Dogalgaz debisi | Turbine/ultrasonik sayac | +-1.5% | Saat bazli |
| Buhar debisi | Orifis + DP transmitter | +-2% | Surekli |
| Su debisi | Elektromanyetik debi olcer | +-0.5% | Surekli |
| Sicaklik | Termokupl / Pt100 | +-0.5 C | Surekli |
| Basinc | Basinc transmitteri | +-0.25% | Surekli |
| Baca gazi | Gaz analizoru (O2, CO, CO2) | +-0.1% O2 | Spot / surekli |

### 5.2 Minimum Olcum Konfigurasyonu

```
Fabrika seviyesi enerji dengesi icin minimum olcum seti:

1. Elektrik: Ana trafo girisi + buyuk tuketiciler (>50 kW)
2. Dogalgaz: Ana sayac + kazan girisleri
3. Buhar: Kazan cikisi + ana dallarda debi
4. Sogutma suyu: Sogutma kulesi debi + sicaklik farki
5. Baca gazi: Her bacada sicaklik + O2 analizi
6. Ortam: Sicaklik + nem (referans)
7. Uretim: Uretim miktari (ton/saat veya adet/saat)
```

## 6. Sankey Diyagrami Insasi (Sankey Diagram Construction)

### 6.1 Sankey Diyagrami Prensipleri

Sankey diyagrami, enerji akislarini genislikleri oransal olan oklarla gosteren bir gorsellestime aracidir:

```
Temel kurallar:
1. Ok genisligi enerji buyuklugu ile orantilidir
2. Toplam giris genisligi = Toplam cikis genisligi (enerji korunumu)
3. Akis yonu soldan saga (giris → donusum → cikis)
4. Kayiplar genellikle asagi veya yukari yonlu gosterilir
5. Renk kodlamasi: Yakit (kirmizi), elektrik (mavi), kayip (gri)
```

### 6.2 Sankey Diyagrami Olceklendirme

```
Olcek belirleme:
- Toplam enerji girisini %100 olarak referans al
- Her akis icin yuzdeli genislik ata
- Minimum gosterilebilir akis: toplam girisin %1'i
- %1'den kucuk akislar "diger" kategorisinde toplanir

Renk kodlamasi:
- Yakit enerjisi:     ████ Koyu kirmizi
- Elektrik enerjisi:  ████ Mavi
- Buhar enerjisi:     ████ Turuncu
- Sicak su:           ████ Acik kirmizi
- Sogutma:            ████ Acik mavi
- Kayiplar:           ████ Gri
- Faydali urun:       ████ Yesil
```

### 6.3 Tipik Fabrika Sankey Diyagrami (ASCII Gosterim)

```
           DOGALGAZ (%65)                    ELEKTRIK (%35)
           ================                  ===============
                  |                                |
                  v                                v
    ┌─────────────────────────┐     ┌──────────────────────────┐
    │      KAZAN DAIRESI      │     │    ELEKTRIK DAGILIM      │
    │     (Yakit → Buhar)     │     │   (Motor, Aydinlatma)    │
    └─────────┬───────────────┘     └──────────┬───────────────┘
              |                                 |
     Baca gazi (%8)──→ KAYIP          Motor kayiplari (%5)──→ KAYIP
     Yuzey kaybi (%2)──→ KAYIP       Trafo kayiplari (%1)──→ KAYIP
              |                                 |
              v                                 v
    ┌─────────────────────────────────────────────────────┐
    │              PROSES VE DAGILIM                       │
    │                                                     │
    │  Buhar dagilim kaybi (%3) ──────────────→ KAYIP     │
    │  Kondensat kaybi (%4) ───────────────────→ KAYIP    │
    │  Basingli hava kacak (%5) ───────────────→ KAYIP    │
    │  Sogutma sistemi kaybi (%3) ─────────────→ KAYIP    │
    └───────────────────────┬─────────────────────────────┘
                            |
                            v
              ┌──────────────────────────┐
              │   FAYDALI ENERJI (%69)   │
              │                          │
              │  Proses isitma:   %35    │
              │  Mekanik is:      %18    │
              │  Sogutma:         %8     │
              │  Aydinlatma:      %4     │
              │  Diger faydali:   %4     │
              └──────────────────────────┘

Toplam kayiplar: %31
Faydali enerji: %69
Kapanma: %100 (denge saglanmistir)
```

## 7. Sektorel Enerji Dagilim Paternleri (Sector-Specific Energy Flow Patterns)

### 7.1 Tipik Enerji Dagilimi Sektorlere Gore

| Sektor | Termal [%] | Elektrik [%] | Ana Termal Kullanim | Ana Elektrik Kullanim |
|---|---|---|---|---|
| Cimento | 75-85 | 15-25 | Klinker pisirme | Degirmen, fan |
| Tekstil | 60-75 | 25-40 | Boyama, kurutma, buhar | Motor, klima |
| Gida ve icecek | 55-70 | 30-45 | Pasturizasyon, kurutma | Sogutma, pompa |
| Kimya | 50-70 | 30-50 | Reaktor, damitma | Kompressor, pompa |
| Metal isleme | 40-65 | 35-60 | Firin, isil islem | EAF, motor |
| Otomotiv | 45-55 | 45-55 | Boyahane, kurutma | Robot, basingli hava |
| Kagit | 65-80 | 20-35 | Kurutma, buhar | Degirmen, pompa |

### 7.2 Enerji Tuketim Dagilimi Alt Sistemlere Gore

| Alt Sistem | Tipik Pay [%] | Enerji Turu | Iyilestirme Potansiyeli |
|---|---|---|---|
| Buhar/Isitma | 30-50 | Termal | %10-25 (ekonomizer, izolasyon) |
| Motorlar/Tahrik | 20-35 | Elektrik | %15-30 (VSD, verimli motor) |
| Basingli hava | 10-20 | Elektrik | %20-40 (kacak, VSD, basinc) |
| Sogutma/HVAC | 5-15 | Elektrik | %15-30 (chiller optimizasyon) |
| Aydinlatma | 3-8 | Elektrik | %30-60 (LED) |
| Pompalama | 5-15 | Elektrik | %15-30 (VSD, boyutlandirma) |
| Ofis/Yardimci | 2-5 | Elektrik | %10-20 |

## 8. Hesaplama Ornegi: Fabrika Enerji Dengesi (Worked Example)

### 8.1 Senaryo

Orta olcekli gida isleme fabrikasi:
- Dogalgaz tuketimi: 600 Nm3/h (LHV = 34.5 MJ/Nm3)
- Elektrik tuketimi: 1,200 kW
- Calisma: 6,000 saat/yil
- Uretim: 25,000 ton/yil

### 8.2 Enerji Giris Hesabi

```
1. Dogalgaz enerji girisi:
   Q_gaz = 600 x 34.5 / 3.6 = 5,750 kW
   Yillik: 5,750 x 6,000 = 34,500,000 kWh/yil

2. Elektrik enerji girisi:
   W_elekt = 1,200 kW
   Yillik: 1,200 x 6,000 = 7,200,000 kWh/yil

3. Toplam enerji girisi:
   E_toplam = 5,750 + 1,200 = 6,950 kW
   Yillik: 41,700,000 kWh/yil

4. Enerji kaynak dagilimi:
   Dogalgaz: 5,750 / 6,950 = %82.7
   Elektrik: 1,200 / 6,950 = %17.3
```

### 8.3 Enerji Cikis ve Kayip Hesabi

```
KAZAN DAIRESI:
- Buhar uretimi: 8 ton/h, 10 bar doymus
  Q_buhar = (8,000/3,600) x (2,778 - 419) = 5,242 kW
  Kazan verimi: Q_buhar / Q_gaz = 5,242 / 5,750 = %91.2

- Baca gazi kaybi (T_baca = 180 C, T_ortam = 25 C):
  Q_baca = 5,750 x 0.058 = 334 kW (%4.8 toplam)

- Yuzey kaybi:
  Q_yuzey = 5,750 x 0.015 = 86 kW (%1.2 toplam)

- Blowdown kaybi:
  Q_blowdown = 5,750 x 0.015 = 88 kW (%1.3 toplam)

BUHAR DAGILIM:
- Boru kayiplari (izolasyon, kapan):
  Q_dagilim = 5,242 x 0.08 = 419 kW (%6.0 toplam)

- Faydali buhar proses isisi:
  Q_proses_buhar = 5,242 - 419 = 4,823 kW

ELEKTRIK TUKETIM DAGILIMI:
- Motorlar/mekanik is: 1,200 x 0.45 = 540 kW
  Motor kayiplari (ortalama %88 verim): 540 x 0.12/0.88 = 74 kW
  Faydali mekanik is: 540 - 74 = 466 kW

- Basingli hava sistemi: 1,200 x 0.18 = 216 kW
  Kompressor kaybi: 216 x 0.85 = 184 kW (isi)
  Faydali hava enerjisi: 216 - 184 = 32 kW
  Kacak kaybi: 32 x 0.25 = 8 kW

- Sogutma sistemi: 1,200 x 0.12 = 144 kW
  COP = 4.0 → Q_sogutma = 144 x 4 = 576 kW
  Kondenser atik isisi: 576 + 144 = 720 kW (cevre)
  Faydali sogutma: 576 kW

- Pompa sistemi: 1,200 x 0.10 = 120 kW
  Pompa/motor kaybi: 120 x 0.35 = 42 kW
  Faydali hidrolik is: 78 kW

- Aydinlatma: 1,200 x 0.05 = 60 kW
  Faydali isik: 60 x 0.30 = 18 kW
  Isi kaybi: 42 kW

- Diger (ofis, kontrol): 1,200 x 0.10 = 120 kW
```

### 8.4 Enerji Dengesi Ozet Tablosu

| Kalem | Enerji [kW] | Pay [%] | Kategori |
|---|---|---|---|
| **GIRISLER** | | | |
| Dogalgaz | 5,750 | 82.7 | Giris |
| Elektrik | 1,200 | 17.3 | Giris |
| **TOPLAM GIRIS** | **6,950** | **100.0** | |
| **FAYDALI CIKISLAR** | | | |
| Proses isitma (buhar) | 4,823 | 69.4 | Faydali |
| Mekanik is (motorlar) | 466 | 6.7 | Faydali |
| Sogutma | 576 | 8.3 | Faydali |
| Hidrolik is (pompalar) | 78 | 1.1 | Faydali |
| Aydinlatma (faydali) | 18 | 0.3 | Faydali |
| **TOPLAM FAYDALI** | **5,961** | **85.8** | |
| **KAYIPLAR** | | | |
| Baca gazi | 334 | 4.8 | Kayip |
| Kazan yuzey kaybi | 86 | 1.2 | Kayip |
| Blowdown | 88 | 1.3 | Kayip |
| Buhar dagilim kaybi | 419 | 6.0 | Kayip |
| Motor/pompa kayiplari | 116 | 1.7 | Kayip |
| Kompressor atik isisi | 184 | 2.6 | Kayip |
| Hava kacagi | 8 | 0.1 | Kayip |
| Kondenser atik isisi | -720 | — | Cevre |
| Aydinlatma isi | 42 | 0.6 | Kayip |
| Diger | 120 | 1.7 | Kayip |
| **TOPLAM KAYIP** | **677** | **9.7** | |

```
Denge kontrolu:
Faydali + Kayip = 5,961 + 677 = 6,638 kW
Not: Sogutma sistemi kondenser isisi cevreden alinan isi icerdiginden
ayrima dikkat edilmelidir. Fabrika siniri icinde:
6,950 kW giris ≈ 6,950 kW cikis (kapanma: <%1) ✓
```

### 8.5 SEC Hesabi

```
SEC = 41,700,000 / 25,000 = 1,668 kWh/ton urun

Karsilastirma (gida sektoru):
- Iyi uygulama: ~1,200 kWh/ton
- Sektor ortalamasi: ~1,600 kWh/ton
- Bu fabrika: 1,668 kWh/ton → Sektör ortalamasi civari

Iyilestirme potansiyeli: ~%15-25 (hedef: 1,250 kWh/ton)
```

## 9. Enerji Dagilim Analizi (Energy Distribution Analysis)

### 9.1 Pareto Analizi (80/20 Kurali)

```
Enerji tuketicilerin siralamasi (buyukten kucuge):

| Sira | Tuketici          | Enerji [kW] | Pay [%] | Kumulatif [%] |
|------|-------------------|-------------|---------|---------------|
| 1    | Kazan/buhar       | 5,750       | 82.7    | 82.7          |
| 2    | Motorlar          | 540         | 7.8     | 90.5          |
| 3    | Basingli hava     | 216         | 3.1     | 93.6          |
| 4    | Sogutma           | 144         | 2.1     | 95.7          |
| 5    | Pompalar          | 120         | 1.7     | 97.4          |
| 6    | Diger             | 120         | 1.7     | 99.1          |
| 7    | Aydinlatma        | 60          | 0.9     | 100.0         |

Sonuc: Ilk 3 tuketici toplam enerjinin %93.6'sini olusturur.
Iyilestirme calismalari oncelikle bu 3 alana odaklanmalidir.
```

### 9.2 Enerji Maliyet Dagilimi

```
Enerji maliyet hesabi:
- Dogalgaz: 600 Nm3/h x 6,000 h x 0.45 EUR/Nm3 = 1,620,000 EUR/yil
- Elektrik: 1,200 kW x 6,000 h x 0.12 EUR/kWh = 864,000 EUR/yil
- Toplam: 2,484,000 EUR/yil

Maliyet dagilimi:
- Dogalgaz: %65.2
- Elektrik: %34.8

Not: Enerji maliyet dagilimi, enerji miktar dagilimindan farkli olabilir.
Elektrik birim fiyatinin dogalgaz birim fiyatina orani onemlidir.
Bkz. energy_pricing.md
```

## 10. Sankey Diyagrami Raporlama Gereksinimleri

### 10.1 Diyagramda Bulunmasi Gerekenler

```
1. Baslik: Fabrika adi, denetim tarihi, referans donem
2. Birimler: kW veya kWh/yil (tutarli birim kullanimi)
3. Tum enerji giris kalemleri (degerler ile)
4. Tum faydali cikis kalemleri (degerler ile)
5. Tum kayip kalemleri (degerler ile)
6. Yuzde dagilim (%X seklinde)
7. Renk kodlamasi aciklamasi (lejant)
8. Denge kapanma hatasi bilgisi
9. Not: Olcum / hesaplama yontemi belirtilmeli
```

### 10.2 Yaygin Hatalar

```
Sankey diyagrami olusturmada yaygin hatalar:
1. Enerji korunumunun saglanmamasi (giris ≠ cikis)
2. Farkli referans noktalari kullanilmasi (LHV vs. HHV karisimi)
3. Birincil ve son enerji karistirilmasi
4. Sogutma sisteminin cevreden aldigi isiyi dahil etmemek
5. Buhar kondensat geri donusunu goz ardi etmek
6. Mevsimsel degisimleri dikkate almamak
7. Basingli hava sisteminde isi geri kazanimini atlama
```

## İlgili Dosyalar

- [Sistem Sinirlari](system_boundaries.md) — Kontrol hacimleri ve olcum noktalari
- [Exergy Akis Analizi](exergy_flow_analysis.md) — Exergy tabanli akis analizi ve Grassmann diyagramlari
- [Kutle Dengesi](mass_balance.md) — Materyal akis analizi ve su dengesi
- [KPI Tanimlari](kpi_definitions.md) — SEC, EUI ve diger performans gostergeleri
- [Enerji Yonetimi](energy_management.md) — ISO 50001 enerji performans izleme
- [Enerji Fiyatlandirma](energy_pricing.md) — Tarife yapilari ve maliyet analizi
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy analizi temel kavramlar
- [Kazan Formulleri](../boiler/formulas.md) — Kazan enerji ve exergy hesaplamalari
- [Kompressor Formulleri](../compressor/formulas.md) — Basingli hava sistemi hesaplamalari
- [Chiller Formulleri](../chiller/formulas.md) — Sogutma sistemi hesaplamalari

## Referanslar

- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 4th Edition, 2016
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- Thumann, A. & Younger, W., "Handbook of Energy Audits," 9th Edition, Fairmont Press, 2012
- ASHRAE, "Procedures for Commercial Building Energy Audits," 2nd Edition, 2011
- EU BREF, "Energy Efficiency," European Commission, 2009
- Schmidt, M., "The Sankey Diagram in Energy and Material Flow Management," Journal of Industrial Ecology, 2008
- Cullen, J.M. & Allwood, J.M. (2010), "The efficient use of energy: Tracing the global flow of energy from fuel to service," Energy Policy, 38(1), 75-81
