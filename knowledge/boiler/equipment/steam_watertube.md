---
title: "Su Borulu Buhar Kazani -- Water-tube Steam Boiler"
category: equipment
equipment_type: boiler
subtype: "Su Borulu Buhar"
keywords: [su borulu, buhar kazanı, watertube]
related_files: [boiler/benchmarks.md, boiler/formulas.md, boiler/solutions/combustion_tuning.md]
use_when: ["Su borulu buhar kazanı analizi yapılırken", "Watertube kazan seçimi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Su Borulu Buhar Kazani -- Water-tube Steam Boiler

> Son guncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Su borulu (water-tube) -- su borularin icinden gecer, sicak gazlar dis yuzeyden akar
- Kapasite araligi: 10 - 500+ ton/saat (buyuk endustriyel tesisler ve enerji santralleri)
- Basinca araligi: 10 - 180+ bar (superkritik uygulamalar mumkun, >221 bar)
- Verimlilik: %85-93 (ekonomizer ve hava on isitici ile)
- Exergy verimi: %30-45 (buhar sicakligi ve basincina bagli)
- Yakitlar: Dogalgaz, fuel oil, komur, biyokutle, atik yakitlar
- Konfigurasyonlar: D-tipi, O-tipi, A-tipi, ayriyeten tek ve cift tamburlu (drum) tasarimlar
- Yaygin markalar: Babcock & Wilcox, Aalborg, Mitsubishi Heavy Industries, Bosch Industriekessel, Viessmann, Thermax, Andritz

## Calisma Prensibi

Su borulu kazanlarda su, kazan borularinin icinden gecer; yanma gazlari ise
borularin dis yuzeyinde akar. Bu tasarim, ates borulu kazanlara kiyasla daha
yuksek basinc ve kapasite uygulamarina olanak tanir.

### Dogal Dolasim (Natural Circulation)
Suyun yogunluk farki (sicak su/buhar karisimi daha hafif, sogumus su daha agir)
sayesinde su, kazan borulerinda akis saglar. Tipik olarak 170 bar altindaki
uygulamalarda kullanilir. Ek pompa gerektirmez.

### Zorlanmis Dolasim (Forced Circulation)
Yuksek basincli uygulamalarda (>170 bar) dogal dolasim yeterli olmadiginda,
sirkulasyon pompasi ile suyun borularda dolasimi saglanir. Superkritik
kazanlarda zorunludur.

### Tambur Tasarimi
- **Tek tamburlu (single drum)**: Kompakt tasarim, orta kapasite uygulamalari
- **Cift tamburlu (double drum)**: Ust tambur (steam drum) buhar ayirma, alt tambur (mud drum) tortu toplama. Daha kararlil su seviyesi kontrolu

### Isi Transfer Bolgeleri
1. **Radyant bolge (furnace)**: Alev radrasyonu ile isi transferi -- en yuksek isi akisi
2. **Konveksiyon bolumu**: Sicak gaz akisi ile isi transferi
3. **Superheater (kizdirici)**: Doymus buhari kizdirilmis buhara donusturur
4. **Reheater (yeniden kizdirici)**: Turbin cikis buharini tekrar kizdirir (enerji santralleri)
5. **Ekonomizer**: Baca gazlari ile besleme suyunu on isitr
6. **Hava on isiticisi (air preheater)**: Baca gazlari ile yanma havasini on isitr

## Enerji Dagilimi (Tipik)

Dogalgaz yakitli, ekonomizerli bir su borulu kazan icin tipik enerji dagilimi:

| Enerji Kalemi | Oran (%) | Aciklama |
|---------------|----------|----------|
| Faydali buhar (useful steam output) | 85-93 | Buhar entalpisi olarak cikis |
| Baca gazi kaybi (flue gas loss) | 4-8 | Egzoz sicakligina bagli |
| Radyasyon ve konveksiyon kaybi | 0.5-2.0 | Kazan yuzey alani ve izolasyona bagli |
| Blowdown kaybi | 0.5-2.0 | Su kalitesi ve blowdown oranina bagli |
| Yakilmamis yakit kaybi | 0.1-0.5 | Yanma verimliligine bagli |
| Diger kayiplar | 0.5-1.5 | Buhar kacirlari, sut kacirlari vb. |

## Exergy Analizi

Buhar kazanlarinda enerji verimi yuksek olmasina ragmen, exergy verimi dusuktur.
Bunun temel nedeni yanma islemindeki buyuk sicaklik farkindan kaynaklanan
tersinmezliklerdir (irreversibility).

```
Exergy verimi (psi_ex) = E_buhar / E_yakit

E_buhar = m_s * [(h_s - h_0) - T_0 * (s_s - s_0)]
E_yakit = m_f * (LHV * phi)

Burada:
  m_s   = buhar debisi (kg/s)
  h_s   = buhar entalpisi (kJ/kg)
  h_0   = referans durum entalpisi, 25 degC, 1 atm (kJ/kg)
  T_0   = referans sicaklik (K), tipik 298.15 K
  s_s   = buhar entropisi (kJ/kg.K)
  s_0   = referans durum entropisi (kJ/kg.K)
  m_f   = yakit debisi (kg/s)
  LHV   = alt isil deger (kJ/kg)
  phi   = yakit exergy/enerji orani (dogalgaz ~1.04, komur ~1.06, fuel oil ~1.06)
```

### Exergy Yikim Dagilimi (Tipik)

| Kaynak | Exergy Yikim Payi (%) | Aciklama |
|--------|----------------------|----------|
| Yanma islemi (combustion) | 25-35 | En buyuk tersinmezlik kaynagi |
| Isi transferi (temperature diff.) | 10-18 | Alev-boru arasi sicaklik farki |
| Baca gazi kaybi | 5-10 | Egzozla atilan exergy |
| Blowdown | 1-3 | Atilan sicak suyun exergysi |
| Radyasyon kayiplari | 0.5-2 | Dusuk sicaklikli kayip, dusuk exergy |
| Toplam exergy yikimi | 45-65 | Exergy verimi = %35-55 |

## Olculmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|--------------|---------------|
| Yakit tuketimi | m3/saat veya kg/saat | Yakita bagli | Gaz sayaci, debimetre veya tartim |
| Yakit alt isil degeri (LHV) | kJ/kg veya kJ/m3 | Yakita bagli | Laboratuvar analizi veya fatura |
| Buhar debisi | ton/saat | 10-500+ | Orifis plakasi, vortex veya ultrasonik flowmeter |
| Buhar basinci | bar | 10-180+ | Manometre veya basinc transmiteri |
| Buhar sicakligi | degC | 180-565+ | Termokupl (K veya N tipi) |
| Besleme suyu sicakligi | degC | 80-250 | Termokupl veya Pt100 |
| Baca gazi sicakligi | degC | 120-250 | Termokupl veya baca gazi analizoru |
| Baca gazi O2 | % | 1.5-5.0 | Baca gazi analizoru (zirkonyum veya elektrokimyasal) |

### Opsiyonel (daha detayli analiz icin)
| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|--------------|---------------|
| Baca gazi CO | ppm | <100 | Baca gazi analizoru |
| Baca gazi CO2 | % | 8-14 | Baca gazi analizoru |
| Blowdown debisi/orani | % | 1-5 | Blowdown sayaci veya TDS olcumu |
| Besleme suyu TDS | ppm | <10 | Iletkenlik olcumu |
| Kazan suyu TDS | ppm | 200-3500 | Iletkenlik olcumu |
| Ortam sicakligi | degC | 10-40 | Termometre |
| Ortam nemi | % RH | 30-80 | Higrometre |
| Kondensat donus orani | % | 50-90 | Kondensat sayaci |
| Kondensat donus sicakligi | degC | 60-95 | Termometre veya Pt100 |
| Yakma havasi sicakligi | degC | 20-250 | Termometre (hava on isitici sonrasi) |

### Nameplate Bilgileri
- Marka ve model
- Nominal buhar kapasitesi (ton/saat)
- Tasarim basinci (bar) ve izin verilen calisma basinci (MAWP)
- Tasarim sicakligi (degC)
- Isitma yuzey alani (m2)
- Yakit tipi ve nominal yakit tuketimi
- Uretim yili ve seri numarasi
- ASME veya EN 12952 sertifika bilgileri
- Kasnak numarasi ve muayene tarihi

## Varsayilan Degerler (Olcum Yoksa)

| Parametre | Varsayilan | Not |
|-----------|------------|-----|
| Baca gazi sicakligi | 180 degC | Ekonomizerli kazan |
| Baca gazi O2 | 3.0% | Iyi ayarlanmis brulor (dogalgaz) |
| Blowdown orani | 3% | Ortalama su kalitesi |
| Radyasyon kaybi | 1.0% | ABMA esigri, >50 ton/saat icin |
| Kondensat donus orani | 70% | Endustriyel ortalama |
| Kondensat donus sicakligi | 80 degC | Tipik kondensat tanki sicakligi |
| Besleme suyu sicakligi | 105 degC | Degazor cikisi |
| Ortam sicakligi | 25 degC | Referans sicaklik |
| Yakit exergy orani (phi) | 1.04 | Dogalgaz icin |
| Yanma havasi fazlaligi | %15 | Dogalgaz, iyi ayarlanmis |

## Performans Tablosu

### Kapasite ve Basinca Gore Tipik Verimlilik

| Kapasite (ton/saat) | Basinca (bar) | Buhar Sicakligi (degC) | Enerji Verimi (%) | Exergy Verimi (%) |
|---------------------|---------------|----------------------|--------------------|--------------------|
| 10-30 | 10-20 | Doymus (180-215) | 85-88 | 30-34 |
| 30-80 | 20-45 | 250-350 | 87-90 | 33-38 |
| 80-200 | 45-90 | 350-480 | 89-92 | 36-42 |
| 200-500 | 90-140 | 480-540 | 90-93 | 40-45 |
| 500+ | 140-180+ | 540-565+ | 91-94 | 42-48 |

### Kazan Konfigurasyonlarina Gore Karsilastirma

| Ozellik | D-Tipi | O-Tipi | A-Tipi |
|---------|--------|--------|--------|
| Kapasite araligi | 5-200+ ton/saat | 5-100 ton/saat | 10-300+ ton/saat |
| Basinca araligi | 10-100+ bar | 10-70 bar | 10-140+ bar |
| Kompaktlik | Iyi | En iyi | Orta |
| Bakim erisimi | Tek tarafli erisim | Sinirli | Cift tarafli erisim |
| Uygulama | Genel endustriyel | Paket kazan, gemi | Enerji santrali |
| Maliyet (goreceli) | Orta | Dusuk-Orta | Yuksek |

## Yakita Gore Performans Farklari

| Yakit Tipi | Tipik Verim (%) | Baca Gazi Sicakligi (degC) | O2 Hedefi (%) | Ozel Husus |
|------------|-----------------|---------------------------|---------------|------------|
| Dogalgaz | 90-93 | 120-180 | 2.0-3.0 | Yogusma riski dusuk, temiz yanma |
| Fuel oil (No.6) | 87-91 | 160-220 | 2.5-4.0 | S icerigi, korozyon riski |
| Komur (taskim.) | 85-89 | 140-200 | 3.5-5.0 | Kul, asinma, emisyon kontrolu |
| Biyokutle | 82-88 | 160-220 | 4.0-6.0 | Nem icerigi, kul erime sicakligi |

## Avantajlar ve Dezavantajlar

### Avantajlar
- **Yuksek kapasite**: 500+ ton/saat buhar uretimi mumkun
- **Yuksek basinca**: 180+ bar basincta calisabilir, superkritik uygulamalar
- **Hizli buhar uretimi**: Dusuk su hacmi sayesinde hizli yuklenme (load response)
- **Guvenlik**: Boru patlamasinda ates borulu kazana gore daha dusuk risk (dusuk su hacmi)
- **Esneklik**: Superheater, reheater, ekonomizer entegrasyonu kolay
- **Uzun omur**: Duzgun bakim ile 30-40+ yil calisma omru
- **Yuksek verim**: Ekonomizer ve hava on isiticisi ile %93+ enerji verimi

### Dezavantajlar
- **Yuksek yatirim maliyeti**: Ates borulu kazana gore 2-5 kat daha pahali (500.000 - 15.000.000+ EUR)
- **Karmasik isletme**: Daha fazla otomasyon ve nitelikli personel gerektirir
- **Su kalitesi gereksinimleri**: Cok yuksek su safligil gerekli (TDS < 5 ppm, SiO2 < 0.02 ppm)
- **Bakim maliyeti**: Yillik bakim maliyeti yuksek, ozel ekipman gerektirir
- **Alan gereksinimi**: Buyuk kurulum alani, yardimci ekipman (degazor, kimyasal dozajlama vb.)
- **Devreye alma suresi**: Ilk devreye alma ve kimyasal temizlik sureci uzun (1-4 hafta)

## Maliyet Analizi (Gosterge Niteligi)

| Kapasite (ton/saat) | Yatirim Maliyeti (EUR) | Yillik Bakim Maliyeti (EUR) | Ekonomik Omur (yil) |
|---------------------|----------------------|---------------------------|---------------------|
| 10-30 | 500.000 - 1.500.000 | 30.000 - 80.000 | 25-35 |
| 30-80 | 1.500.000 - 4.000.000 | 80.000 - 200.000 | 25-35 |
| 80-200 | 4.000.000 - 8.000.000 | 200.000 - 400.000 | 30-40 |
| 200-500 | 8.000.000 - 15.000.000+ | 400.000 - 800.000 | 30-40 |

## Dikkat Edilecekler

1. **Su kalitesi kritiktir**: Yuksek basincli su borulu kazanlarda su safligil son derece onemlidir. Yetersiz su aritmasi boru icicinde tortu olusumuna, asiri isimmaya ve boru patlamasina yol acar. TDS, sertlik, SiO2, O2 ve pH surekli izlenmeli.

2. **Baca gazi kayiplari**: Baca gazi sicakliginda her 20 degC dusus yaklasik %1 verim artisi saglar. Ekonomizer ve hava on isiticisi bu kaybi onemli olcude azaltir. Ancak asit cig noktasinin (acid dew point) altina dusulmemelidir -- dogalgaz icin ~55 degC, kurkurtlu yakitlar icin ~130-160 degC.

3. **Hava fazlaligi ayari**: Fazla hava yanma kayiplarini arttirir, yetersiz hava ise eksik yanma (CO olusumu) ve guvenlik riski yaratir. Dogalgazda %10-15, fuel oil'de %15-20 hava fazlaligi hedeflenmeli. O2 trim kontrolu ile surekli optimizasyon oneriliir.

4. **Blowdown yonetimi**: Blowdown oraninin geregindan yuksek olmasi enerji kaybina, dusuk olmasi ise su kalitesi sorunlarina neden olur. Otomatik TDS kontrollu blowdown sistemi ile optimizasyon saglanmali. Blowdown isi geri kazanimi (flash tank + heat exchanger) degerlendirilmeli.

5. **Buhar kacaklari**: 1 mm capindaki bir buhar kacagi 40 bar basincta yilda yaklasik 3.000 - 5.000 EUR kayba neden olabilir. Ultrasonik kacak tespiti ile duzenli kontrol yapilmali.

6. **Yuklenme (load follow)**: Su borulu kazanlarin dusuk su hacmi hizli yuklenmeye izin verir ancak ani yuk degisimlerinde su seviyesi dalgalanmalari (shrink/swell) dikkatle yonetilmeli. Otomatik su seviyesi kontrol sistemi (3-eleman kontrolu: debi, seviye, buhar debisi) oneriliir.

7. **Superheater korumasi**: Buhar debisi dusuk iken superheater borulari asiri isimmaya maruz kalir. Minimum buhar debisi limitlerine uyulmali, desuperheater (attemperator) kontrolu duzgun calismaali.

8. **Periyodik muayene**: EN 12952 ve ASME Section I standartlarina uygun periyodik ic ve dis muayene zorunludur. Turkiye'de isg mevzuati geregi yillik muayene ve 4 yilda bir hidrostatik test yapilmaalidir. Tum muayeneler akredite muayene kurulusu tarafindan gerceklestirilmeli.

## Enerji Tasarruf Potansiyeli

| Onlem | Tipik Tasarruf | Yatirim (EUR) | Geri Odeme |
|-------|----------------|---------------|------------|
| Ekonomizer (baca gazi -> besleme suyu) | %3-5 | 50.000 - 300.000 | 1-3 yil |
| Hava on isiticisi (baca gazi -> yanma havasi) | %1-3 | 40.000 - 200.000 | 1-3 yil |
| O2 trim kontrolu | %1-2 | 15.000 - 50.000 | 0.5-1.5 yil |
| Blowdown isi geri kazanimi | %0.5-1.5 | 10.000 - 40.000 | 0.5-2 yil |
| Kondensat geri kazanimi iyilestirme | %2-5 | 20.000 - 100.000 | 1-2 yil |
| Izolasyon iyilestirme | %0.5-1.5 | 10.000 - 50.000 | 0.5-1 yil |
| Buhar kacak onarimi | %1-3 | 5.000 - 20.000 | <0.5 yil |
| Yakma sistemi modernizasyonu | %2-4 | 100.000 - 500.000 | 2-4 yil |

## İlgili Dosyalar
- Ates borulu buhar kazani: `equipment/boiler_steam_firetube.md`
- Yakit verileri ve isil degerler: `fuels/fuel_properties.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer rehberi: `solutions/boiler_economizer.md`
- Kondensat geri kazanimi: `solutions/steam_condensate_recovery.md`
- Buhar sistemi optimizasyonu: `solutions/steam_system_optimization.md`
- Exergy hesaplama formulleri: `formulas/boiler_exergy.md`
- Buhar dagitim sistemi: `equipment/steam_distribution.md`
- Su aritmasi: `equipment/boiler_water_treatment.md`

## Referanslar
- ASME Boiler and Pressure Vessel Code, Section I -- Power Boilers
- EN 12952 -- Water-tube Boilers and Auxiliary Installations
- Babcock & Wilcox, "Steam: Its Generation and Use", 42nd Edition
- DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry", 2nd Edition
- Turkish Ministry of Labour (CSGB), Is Ekipmanlari Yonetmeligi (Periyodik Muayene)
- Bejan, A., Tsatsaronis, G., Moran, M., "Thermal Design and Optimization", Wiley
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis", Krieger Publishing
