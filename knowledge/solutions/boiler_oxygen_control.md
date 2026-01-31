# O₂ Trim / Fazla Hava Kontrolu -- Oxygen Trim Control

> Son guncelleme: 2026-01-31

## Ozet

**Problem:** Kazanlarda fazla hava (excess air) orani gereginden yuksek tutuldugunda, baca gazi kayiplari artar ve kazan verimi duser. Sabit hava/yakit oranli brulor sistemlerinde, yuk degisimlerinde optimum hava orani korunamaz.

**Cozum:** O₂ trim kontrolu ile baca gazindaki oksijen konsantrasyonunu surekli olcup, hava damperi veya brulor fan hizini otomatik ayarlayarak optimum hava/yakit oranini her yuk kosulunda saglamak.

**Tipik Tasarruf:** %1-3 yakit tasarrufu (fazla havanin azaltilmasiyla baca gazi kayiplarinin dusurulmesi)
**Tipik ROI:** <1 yil

## Calisma Prensibi

### O₂ Analizor Turleri

| Analizor Tipi | Calisma Prensibi | Olcum Araligi | Tepki Suresi | Tipik Maliyet |
|---------------|------------------|---------------|--------------|---------------|
| Zirkonyum oksit prob (ZrO₂) | Katı elektrolit oksijen hucresinde Nernst potansiyeli olcumu | 0-25% O₂ | 5-10 s | EUR 2,000-5,000 |
| Paramanyetik | Oksijenin paramanyetik ozelliginden yararlanarak olcum | 0-25% O₂ | 15-30 s | EUR 3,000-8,000 |
| Elektrokimyasal hucre | Galvanik hucre ile oksijen indirgemesi | 0-25% O₂ | 10-20 s | EUR 500-2,000 |
| Tunable diode laser (TDL) | Lazer absorpsiyon spektroskopisi | 0-25% O₂ | 1-3 s | EUR 8,000-20,000 |

**Endustriyel kazanlarda en yaygin:** Zirkonyum oksit (zirconia) prob -- yuksek sicakliga dayanikli, dogrudan baca icine monte edilebilir, bakim gereksinimi dusuk.

### Geri Besleme Dongusu (Feedback Loop)

O₂ trim kontrol sistemi asagidaki adimlarla calisir:

1. **Olcum:** Baca gazindaki O₂ konsantrasyonu zirkonyum prob ile surekli olculur
2. **Karsilastirma:** Olculen O₂ degeri, yakit turune ve yuke gore belirlenen setpoint ile karsilastirilir
3. **Kontrol:** PID kontrolor, sapma (error) sinyaline gore hava damperi veya fan hizi komutunu hesaplar
4. **Aktuator:** Hava damperi pozisyonu veya VSD fan hizi ayarlanir
5. **Dogrulama:** Yeni O₂ degeri olculur, dongu tekrarlanir

### Modulating vs On-Off Brulorler

| Brulor Tipi | O₂ Trim Uygunlugu | Aciklama |
|-------------|-------------------|----------|
| Tam modulasyonlu (Modulating) | Cok uygun | Surekli kapasite kontrolu, O₂ trim tum yuk araliginda calisir |
| Yuksek-dusuk alev (High-Low) | Uygun | Iki kademede O₂ setpoint tanimlanir |
| On-Off | Sinirli | Sadece yanma esnasinda trim uygulanabilir, sik acma-kapama nedeniyle etkinlik dusuk |
| Tam modulasyonlu + VSD fan | En uygun | Hem hava damperi hem fan hizi kontrolu ile genis turndown |

## Fazla Hava Etkisi

Fazla hava, baca gazi debisini ve sicakligini artirir; bu da baca gazi kayiplarini dogrudan yukselterek kazan verimini dusurur.

### O₂ Artisi ve Verim Kaybi Iliskisi

| Baca Gazi O₂ (%) | Tahmini Fazla Hava (%) | Verim Kaybi (yaklasik) | Degerlendirme |
|-------------------|------------------------|------------------------|---------------|
| 2.0 | ~10 | Referans | Optimum (dogalgaz) |
| 3.0 | ~15 | +%0.5 | Kabul edilebilir |
| 4.0 | ~21 | +%1.0 | Yuksek |
| 5.0 | ~28 | +%1.5 | Cok yuksek (gaz icin) |
| 6.0 | ~36 | +%2.0 | Asiri |
| 7.0 | ~44 | +%2.5 | Kabul edilemez |
| 8.0 | ~54 | +%3.0 | Tehlikeli derecede asiri |
| 9.0 | ~64 | +%3.5-4.0 | Acil mudahale gerekir |

**Genel kural:** Her %1 fazla O₂ artisi, yaklasik %0.5-1.0 verim kaybina neden olur (baca gazi sicakligina bagli).

## O₂ / Fazla Hava Donusum Formulu

Baca gazindaki O₂ konsantrasyonundan fazla hava oranini hesaplamak icin:

```
EA = (O₂_olculen / (20.9 - O₂_olculen)) x 100

Burada:
  EA           : Fazla hava orani (Excess Air) [%]
  O₂_olculen   : Baca gazinda olculen O₂ konsantrasyonu [% hacimsel, kuru bazda]
  20.9         : Atmosferdeki O₂ konsantrasyonu [%]
```

### Ornek Hesap

```
O₂_olculen = 4.0%

EA = (4.0 / (20.9 - 4.0)) x 100
EA = (4.0 / 16.9) x 100
EA = %23.7 fazla hava
```

### Hava Fazlasi Katsayisi (lambda)

```
lambda = 1 + EA / 100 = 20.9 / (20.9 - O₂_olculen)

Burada:
  lambda       : Hava fazlasi katsayisi (excess air ratio) [boyutsuz]
  EA           : Fazla hava orani [%]
  O₂_olculen   : Baca gazinda olculen O₂ [% hacimsel, kuru baz]
```

## Optimum O₂ Seviyeleri (Yakit Turune Gore)

| Yakit Turu | Optimum O₂ (%) | Fazla Hava (%) | lambda | Aciklama |
|------------|----------------|----------------|--------|----------|
| Dogalgaz (Natural Gas) | 2.0-3.0 | 10-17 | 1.05-1.15 | Temiz yanma, dusuk fazla hava yeterli |
| LPG | 2.0-3.0 | 10-17 | 1.05-1.15 | Dogalgaza benzer ozellikler |
| Fuel Oil No. 2 (Gasoil) | 3.0-4.0 | 17-23 | 1.15-1.20 | Atomizasyon kalitesine bagli |
| Fuel Oil No. 6 (Agir yakit) | 3.5-4.5 | 20-28 | 1.18-1.25 | Yuksek viskozite, dusuk atomizasyon kalitesi |
| Komur (pulverize) | 3.5-5.0 | 20-31 | 1.15-1.25 | Katı yakit, homojen olmayan dagilim |
| Komur (izgarali) | 4.0-6.0 | 23-40 | 1.20-1.40 | Izgara tipi ve komur boyutuna bagli |
| Biyokutle (pelet) | 4.0-6.0 | 23-40 | 1.25-1.40 | Yuksek nem ve degisken bilesin |
| Biyokutle (yonga/atik) | 5.0-7.0 | 31-50 | 1.30-1.50 | Heterojen yakit, genis hava marji gerekir |

**Onemli not:** Optimum O₂ degerleri brulor tipine, kazan yasu, yuk oranina ve bakim durumuna gore degisir. Yukaridaki degerler iyi bakim yapilmis modern brulorler icindir.

## Uygulanabilirlik Kriterleri

### O₂ Trim Ne Zaman Uygulanmali

| Kriter | Minimum | Ideal |
|--------|---------|-------|
| Kazan kapasitesi | 500 kW_th | >2,000 kW_th |
| Yillik calisma suresi | 3,000 saat/yil | >5,000 saat/yil |
| Yuk degiskenlik orani | >%20 yuk dalgalanmasi | >%40 yuk dalgalanmasi |
| Mevcut O₂ seviyesi | >%4 (dogalgaz) | >%5 (dogalgaz) |
| Brulor tipi | Minimum high-low | Tam modulasyonlu |
| Yakit maliyeti | EUR 30,000/yil ustu | EUR 100,000/yil ustu |

### Uygulanmamasi Gereken Durumlar
- On-off brulorlu kucuk kazanlar (<200 kW_th)
- Yil boyunca sabit tam yukte calisan kazanlar (mevcut ayar yeterliyse)
- Cok eski kazanlar (sizinti ve mekanik problemler oncelikle giderilmeli)
- Cok dusuk calisma suresi (<1,500 saat/yil)

## Yatirim Maliyeti

| Sistem Bileseni | Maliyet Araligi | Aciklama |
|-----------------|-----------------|----------|
| Zirkonyum O₂ prob (tek) | EUR 1,500-3,500 | In-situ tip, 700 degC'ye kadar |
| Paramanyetik analizor | EUR 3,000-8,000 | Numune alma sistemi dahil |
| PID kontrolor / modulu | EUR 500-2,000 | DCS/PLC entegrasyonu icin |
| Hava damperi aktuatoru | EUR 800-3,000 | Modulasyonlu tip |
| VSD fan surucusu | EUR 2,000-8,000 | Fan gucune bagli |
| Montaj ve devreye alma | EUR 1,000-3,000 | Mekanik + elektrik iscilik |
| **Toplam: Basit O₂ trim** | **EUR 2,000-6,000** | Prob + kontrolor + aktuator |
| **Toplam: Gelismis sistem** | **EUR 8,000-15,000** | Prob + analizor + VSD fan + kontrol |

**Not:** Fiyatlar 2025-2026 Turkiye piyasasi icin tahmini degerlerdir. Buyuk kapasiteli sistemlerde birden fazla olcum noktasi gerekebilir.

## ROI Hesabi

### Formul

```
Yakit_tasarrufu_orani = (O₂_once - O₂_sonra) x 0.75 / 100

Yillik_yakit_tuketimi_EUR = m_yakit x LHV x Yakit_birim_fiyati

Yillik_tasarruf_EUR = Yillik_yakit_tuketimi_EUR x Yakit_tasarrufu_orani

Geri_odeme_yil = Yatirim / Yillik_tasarruf_EUR

Burada:
  O₂_once        : Mevcut baca gazi O₂ seviyesi [%]
  O₂_sonra       : O₂ trim sonrasi hedef O₂ seviyesi [%]
  0.75           : Ortalama verim kazanci katsayisi (her %1 O₂ icin ~%0.75 verim)
  m_yakit        : Yillik yakit tuketimi [kg veya m³]
  LHV            : Alt isil deger [kJ/kg veya kJ/m³]
  Yakit_birim_fiyati : Yakit birim fiyati [EUR/kWh veya EUR/m³]
```

### Ornek Hesap

**Senaryo:** 4,000 kW_th dogalgaz kazani, 5,000 saat/yil, O₂ seviyesi %5.5'ten %2.5'e dusurme

```
Yakit_tasarrufu_orani = (5.5 - 2.5) x 0.75 / 100 = %2.25

Kazan verimi (mevcut) = %88 (tahmini)
Yillik yakit tuketimi = 4,000 / 0.88 x 5,000 = 22,727,273 kWh_th
Dogalgaz fiyati = EUR 0.045/kWh (Turkiye endustriyel, 2025)
Yillik yakit maliyeti = 22,727,273 x 0.045 = EUR 1,022,727

Yillik tasarruf = EUR 1,022,727 x 0.0225 = EUR 23,011/yil

Yatirim = EUR 5,000 (basit O₂ trim sistemi)
Geri odeme = 5,000 / 23,011 = 0.22 yil (yaklasik 2.6 ay)
```

## Uygulama Adimlari

1. **Mevcut durum analizi:** Baca gazi O₂, CO, sicaklik olcumleri yapilir; farkli yuk kosullarinda en az 3 nokta olculur
2. **Brulor degerlendirmesi:** Brulor tipi, modulation turndown orani, mevcut hava kontrol mekanizmasi belirlenir
3. **Analizor secimi:** Yakit turune, baca gazi sicakligina ve ortam kosullarina uygun O₂ analizor tipi secilir (cogu uygulama icin zirkonyum prob yeterli)
4. **Montaj noktasi belirlenmesi:** Prob, bruloruden yeterli mesafede (minimum 1-2 metre) ve temsili bir olcum noktasina yerlestirilir
5. **Kontrol entegrasyonu:** O₂ sinyali mevcut DCS/PLC/BMS sistemine baglanir; PID kontrol parametreleri tanimlanir
6. **Setpoint tanimlanmasi:** Her yuk kademesi icin optimum O₂ setpoint degerleri belirlenir (characterization curve)
7. **Devreye alma:** Dusuk yukten yuksek yuke dogru kademeli olarak trim kontrolu devreye alinir; CO seviyesi izlenir
8. **CO guvenlik siniri:** CO konsantrasyonu icin ust sinir alarmi (tipik 200-400 ppm) tanimlanir; ust sinir asildiginda hava damperi otomatik acilir
9. **Kalibrasyon:** Ilk kalibrasyon yapilir; periyodik kalibrasyon takvimi olusturulur (3-6 ayda bir)
10. **Performans dogrulama:** Kurulum sonrasi minimum 1 haftalik veri toplama ile tasarruf dogrulanir

## CO vs O₂ Dengesi

O₂ trim kontrolunde en kritik konu, fazla havayi dusururken CO olusumunu artirmamaktir. Cok dusuk O₂ seviyelerinde eksik yanma baslar ve CO konsantrasyonu hizla yukselir.

### O₂ - CO Iliskisi (Tipik Dogalgaz Kazani)

| Baca Gazi O₂ (%) | Tahmini CO (ppm) | Durum |
|-------------------|-------------------|-------|
| 5.0 | <10 | Asiri fazla hava, dusuk verim |
| 4.0 | <10 | Fazla hava yuksek |
| 3.0 | <20 | Kabul edilebilir |
| 2.5 | 20-50 | Optimum bolge |
| 2.0 | 50-100 | Optimum alt sinir |
| 1.5 | 100-400 | Tehlikeli bolge, eksik yanma basliyor |
| 1.0 | >400 | Kabul edilemez, CO zehirlenmesi riski |

### Guvenli Calisma Penceresi

```
Optimum calisma noktasi:
  O₂_min = CO sinirina gore (CO < 100 ppm)
  O₂_max = Verim hedefine gore (yakit turune uygun ust sinir)

Guvenlik marji:
  O₂_setpoint = O₂_min + 0.5% (guvenlik marji)

Burada:
  O₂_min     : CO sinirinin asildigi minimum O₂ seviyesi [%]
  O₂_max     : Kabul edilebilir maksimum O₂ seviyesi [%]
  O₂_setpoint: Kontrol hedef degeri [%]
```

**Uyari:** CO olcumu olmadan O₂ trim uygulamak tehlikelidir. Ideal sistemde hem O₂ hem CO analizoru birlikte kullanilir (O₂/CO trim).

## Riskler ve Dikkat Edilecekler

| Risk | Aciklama | Onlem |
|------|----------|-------|
| CO olusumu | O₂ cok dusurulurse eksik yanma ve CO uretimi baslar; patlama ve zehirlenme riski | CO analizoru ile ikili kontrol; CO ust sinir alarmi (200 ppm); otomatik hava artisi |
| Sensor kirlenmesi (Fouling) | Baca gazi icindeki partikul, kurum ve kul prob uzerine birikerek olcum hatasina neden olur | Periyodik temizlik (ayda 1); otomatik geri uflemeli (purge) prob kullanimi |
| Kalibrasyon kaymasi (Drift) | Zaman icinde sensor hassasiyeti degisir, yanlis O₂ degeri okunur | 3-6 ayda bir referans gaz ile kalibrasyon; ikili prob ile capraz kontrol |
| Yuk gecislerinde hunting | Hizli yuk degisimlerinde PID kontrolor asiri tepki verir (oscillation) | PID parametrelerini optimize et; derivative (D) terimini dikkatli ayarla; rate limiter kullan |
| Uyumsuz brulor | Eski veya bakim yapilmamis brulorlerde hava/yakit karisimsizligi | Once brulor bakimi ve ayari yap; sizmaz damper kullan |
| Baca cekis degisimi | Ruzgar ve sicaklik degisimleri baca cekisini etkiler; dogal cekisli kazanlarda O₂ dalgalanir | Dengeli cekis (balanced draft) veya zorlamali cekis (forced draft) sistemi tercih et |
| Elektrik arizi | Kontrol sisteminin devre disi kalmasi durumunda brulor guvenli konuma donmeli | Fail-safe tasarim; arizada hava damperi guvenli pozisyona (acik) donmeli |
| Coklu yakit gecisleri | Dual-fuel kazanlarda yakit degisiminde O₂ setpoint guncellenmeli | Yakit turune gore otomatik setpoint degisimi; yakit secim sinyali entegrasyonu |

## Gelismis O₂/CO Trim Stratejileri

### Parallel Positioning (Paralel Konumlandirma)
- Geleneksel yontem: Yakit vanasi ve hava damperi mekanik olarak birbirine baglidir (jackshaft)
- Dezavantaj: Sabit oran, yuk degisimlerine uyum saglanamaz

### O₂ Trim ile Cross-Limiting Kontrol
- Yakit artisinda: Once hava artar, sonra yakit artar (hava onceden — air lead)
- Yakit azalmasinda: Once yakit azalir, sonra hava azalir (yakit onceden — fuel lead)
- Avantaj: Gecis anlarinda zengin karisim (fuel-rich) olusumu engellenir

### O₂/CO Birlesik Trim
- En gelismis yontem: Hem O₂ hem CO surekli olculur
- O₂ kaba kontrol (coarse), CO ince ayar (fine trim) olarak kullanilir
- CO limiti asildigi anda hava otomatik artirilir
- Ek maliyet: EUR 3,000-8,000 (CO analizoru)

## Ilgili Dosyalar
- Kazan yakitlari ve ozellikleri: `equipment/boiler_fuels.md`
- Ates borulu buhar kazanlari: `equipment/boiler_steam_firetube.md`
- Su borulu buhar kazanlari: `equipment/boiler_steam_watertube.md`
- Kazan ekserji hesaplamalari: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Yanma optimizasyonu: `solutions/boiler_combustion_optimization.md`
- Baca gazi isi geri kazanimi: `solutions/boiler_flue_gas_recovery.md`

## Referanslar
- ASME PTC 4 (2013). *Fired Steam Generators -- Performance Test Codes*, ASME.
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- DOE/AMO (2012). *Improve Your Boiler's Combustion Efficiency*, Steam Tip Sheet #4.
- EN 50379 (2012). *Specification for portable electrical apparatus designed to measure combustion flue gas parameters*, CEN.
- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators*, Marcel Dekker.
- ISA-77.44.01 (2007). *Fossil Fuel Power Plant -- Steam Temperature Controls*, ISA.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- NFPA 85 (2019). *Boiler and Combustion Systems Hazards Code*, NFPA.
- Spirax Sarco (2023). *The Steam and Condensate Loop*, Technical Reference Guide.
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
