---
title: "Ates Borulu Buhar Kazani — Fire-tube Steam Boiler"
category: equipment
equipment_type: boiler
subtype: "Ateş Borulu Buhar"
keywords: [ateş borulu, buhar kazanı, firetube]
related_files: [boiler/benchmarks.md, boiler/formulas.md, boiler/solutions/economizer.md]
use_when: ["Ateş borulu buhar kazanı analizi yapılırken", "Firetube kazan seçimi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Ates Borulu Buhar Kazani — Fire-tube Steam Boiler

> Son guncelleme: 2026-01-31

## Genel Bilgiler

Ates borulu (fire-tube) buhar kazanlari, yanma gazlarinin celik borularin icinden gecirilerek
borunun disindaki suya isi transferi saglandigi kazan tipidir. Endustriyel tesislerde en yaygin
kullanilan kazan turudur; kompakt yapisi, kolay isletmesi ve nispeten dusuk yatirim maliyeti
nedeniyle ozellikle kucuk ve orta olcekli tesislerde tercih edilir.

- **Tip:** Ates borulu (fire-tube) — yanma gazlari borularin icinden gecer, su govde (shell) icinde borulari sarar
- **Kapasite araligi:** 0.5–30 ton/saat buhar (tipik endustriyel uygulama)
- **Basinc araligi:** 5–25 bar (maksimum ~30 bar)
- **Verimlilik:** %80–88 (tipik), ekonomizer ile %92'ye kadar cikar
- **Exergy verimi:** %28–42 (tipik) — dusuk buhar basinclarinda exergy verimi belirgin sekilde duser
- **Gecis sayisi (pass):** 2 gecisli, 3 gecisli, 4 gecisli (Scotch marine tasarim en yaygindir)
- **Yaygin markalar:** Bosch (Buderus), Viessmann, Cleaver-Brooks, Miura, Hurst, Aalborg, Babcock Wanson
- **Tipik yakit turleri:** Dogalgaz, LPG, motorin (fuel-oil No. 4), biogas

## Calisma Prensibi

Ates borulu kazanlarda yanma islemi brulorde (burner) gerceklesir. Olusan sicak yanma gazlari
(flame tube / furnace tube) icerisinden gecerek birinci gecisi tamamlar. Ardindan yanma gazlari
arka duman kutusundan (rear smoke box) donerek ikinci, ucuncu ve (varsa) dorduncu gecis
borularina yonlendirilir.

### Scotch Marine Tasarim (Shell-Type)

- En yaygin ates borulu kazan tasarimidir
- Silindirik govde (shell) icinde buyuk capli yanma odasi (furnace tube) ve kucuk capli duman borulari bulunur
- Govdenin tamami su ile doludur; borularin dis yuzeylerinden suya isi transferi saglanir
- Tipik boyutlar: 1.5–4.5 m uzunluk, 1.2–3.5 m cap

### Wet-back ve Dry-back Tasarim

| Ozellik | Wet-back | Dry-back |
|---------|----------|----------|
| Arka duman kutusu | Su ile sogutulmus | Refrakter (tugla) kapli |
| Verimlilik | Daha yuksek (~%2 fark) | Standart |
| Bakim | Daha az bakim gerektirir | Refrakter bakimi gerekir |
| Maliyet | Daha yuksek yatirim | Daha dusuk yatirim |
| Omur | 20–30 yil | 15–25 yil |

### Gecis Sayisina Gore Siniflandirma

| Gecis Sayisi | Baca Gazi Sicakligi (°C) | Tipik Verim (%) | Kullanim |
|-------------|--------------------------|-----------------|----------|
| 2 gecisli | 280–350 | 78–82 | Eski tesisler |
| 3 gecisli | 180–250 | 84–88 | Standart endustriyel |
| 4 gecisli | 150–200 | 86–90 | Yuksek verim uygulamalari |

### Brulor Calismasi

- Otomatik modulasyonlu brulorler (modulating burner) kazan yukunu %20–100 arasinda ayarlar
- On/off brulorler yalnizca kucuk kapasitelerde (<2 ton/saat) kullanilir
- Yuksek-dusuk-kapali (high-low-off) brulorler orta kapasitelerde tercih edilir
- Modulasyonlu brulorler yillik bazda %3–5 yakit tasarrufu saglar

## Enerji Dagilimi (Tipik)

Dogalgaz yakitli, 10 ton/saat kapasiteli, 3 gecisli bir kazan icin tipik enerji dagilimi:

| Enerji Kalemi | Oran (%) | Aciklama |
|---------------|----------|----------|
| Faydali buhar ciktisi (useful steam output) | 82–88 | Ana urun — buhar entalpisi |
| Baca gazi kaybi (flue gas loss) | 8–12 | En buyuk kayip kalemi |
| Radyasyon ve konveksiyon kaybi (radiation/convection loss) | 1.0–2.0 | Govde yuzeyinden |
| Blowdown kaybi (blowdown loss) | 1.0–3.0 | Cozunmus katilarin uzaklastirilmasi |
| Yanmamis yakit kaybi (unburnt fuel) | <0.5 | Iyi bakimli kazanlarda ihmal edilebilir |

### Baca Gazi Kaybi Hesabi (Siegert Formulu)

```
q_baca = (T_baca - T_ortam) × (A1 / (CO2%) + B)

Burada:
  q_baca  = Baca gazi kaybi (%)
  T_baca  = Baca gazi sicakligi (°C)
  T_ortam = Ortam sicakligi (°C)
  CO2%    = Baca gazindaki CO2 yuzdesi (%)
  A1      = Yakit sabiti (dogalgaz icin 0.37)
  B       = Yakit sabiti (dogalgaz icin 0.009)
```

### Kazan Verimi (Dolayli Yontem — Indirect Method)

```
eta_kazan = 100 - q_baca - q_radyasyon - q_blowdown - q_yanmamis

Burada:
  eta_kazan    = Kazan verimi (%)
  q_baca       = Baca gazi kaybi (%)
  q_radyasyon  = Radyasyon ve konveksiyon kaybi (%)
  q_blowdown   = Blowdown kaybi (%)
  q_yanmamis   = Yanmamis yakit kaybi (%)
```

### Exergy Verimi Hesabi

```
psi_kazan = (m_buhar × (h_buhar - h_su) - T0 × (s_buhar - s_su)) / (m_yakit × ex_yakit)

Burada:
  psi_kazan = Exergy verimi (boyutsuz, tipik 0.28–0.42)
  m_buhar   = Buhar debisi (kg/s)
  h_buhar   = Buhar entalpisi (kJ/kg)
  h_su      = Besleme suyu entalpisi (kJ/kg)
  s_buhar   = Buhar entropisi (kJ/kg·K)
  s_su      = Besleme suyu entropisi (kJ/kg·K)
  T0        = Referans (olum durum) sicakligi (K), tipik 298.15 K
  m_yakit   = Yakit debisi (kg/s)
  ex_yakit  = Yakitin spesifik exergysi (kJ/kg)
```

## Olculmesi Gereken Parametreler

### Zorunlu

| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|-------------|---------------|
| Yakit tuketimi (fuel consumption) | m³/h (gaz) veya kg/h (sivi) | 30–2000 m³/h | Gaz sayaci (turbine meter) veya debi olcer |
| Buhar debisi (steam flow rate) | ton/h | 0.5–30 | Vortex veya orifis debi olcer |
| Buhar basinci (steam pressure) | bar | 5–25 | Basinc transmiteri |
| Baca gazi sicakligi (flue gas temperature) | °C | 150–300 | Termokupl (K-tipi) baca cikisinda |
| Baca gazi O2 (flue gas O2) | % | 2–6 | Baca gazi analizoru (electrochemical) |
| Besleme suyu sicakligi (feedwater temperature) | °C | 60–105 | Pt100 sicaklik sensoru |

### Opsiyonel

| Parametre | Birim | Tipik Aralik | Nasil Olculur |
|-----------|-------|-------------|---------------|
| Baca gazi CO (flue gas CO) | ppm | 20–200 | Baca gazi analizoru |
| Yuzey sicakliklari (surface temperatures) | °C | 40–80 | Kizilotesi termometre (IR gun) |
| Blowdown orani (blowdown rate) | % | 1–8 | Blowdown debisi / besleme debisi |
| Kondensat sicakligi (condensate return temperature) | °C | 70–95 | Pt100 sensoru kondensat hattinda |
| Kondensat geri donus orani (condensate return ratio) | % | 50–90 | Kondensat tankinda seviye olcum |
| Baca gazi NOx (flue gas NOx) | ppm | 30–150 | Baca gazi analizoru (cevre mevzuati icin) |

### Nameplate Bilgileri

Saha calismasinda mutlaka kaydedilmesi gereken etiket bilgileri:

- **Marka ve model** (manufacturer, model)
- **Seri numarasi** (serial number)
- **Nominal kapasite** (ton/h veya kW) — ornegin: 10 ton/h veya 6500 kW
- **Maksimum calisma basinci** (bar) — ornegin: 13 bar
- **Tasarim basinci** (bar) — genellikle calisma basincinin %10–15 ustunde
- **Uretim yili** (year of manufacture)
- **Isitma yuzeyi** (m²) — isi transfer yuzeyi alani
- **Test basinci** (bar) — hidrostatik test basinci
- **Ilgili standart** — EN 12953, ASME Section I, vb.

## Varsayilan Degerler (Olcum Yoksa)

Sahada olcum yapilamadigi durumlarda asagidaki varsayilan degerler kullanilabilir.
Bu degerler muhafazakar (conservative) secilmistir; gercek performans bunlardan
daha iyi veya kotu olabilir.

| Parametre | Varsayilan | Not |
|-----------|-----------|-----|
| Baca gazi sicakligi | 200 °C | 3 gecisli, dogalgaz, iyi bakimli kazan |
| Fazla O2 (excess O2) | %4 | Modulasyonlu brulor, dogalgaz |
| Besleme suyu sicakligi | 80 °C | Degaze tankli (deaerator) sistem |
| Blowdown orani | %3 | Otomatik blowdown kontrollu |
| Radyasyon kaybi | %1.5 | 5–15 ton/h kapasite araligi |
| Yillik calisma saati | 4000 saat/yil | Tek vardiya, mevsimsel isitma dahil |
| Yuk orani (load factor) | %70 | Ortalama yillik yuk / nominal kapasite |
| Kondensat geri donus orani | %70 | Standart endustriyel tesis |
| Kazan verimi (birinci enerji) | %85 | Olcum yoksa ilk tahmin |
| Exergy verimi | %35 | 10 bar buhar, dogalgaz yakit |

## Performans Tablosu

Dogalgaz yakitli, 10 bar buhar basincli ates borulu kazanlarda kapasiteye gore tipik performans:

| Kapasite (ton/h) | Tipik Verim (%) | Exergy Verimi (%) | Baca Gazi Sic. (°C) | Yakit Tuketimi (m³/h) | Tahmini Yatirim (€) |
|------------------:|----------------:|-------------------:|---------------------:|----------------------:|--------------------:|
| 0.5 | 80–83 | 25–30 | 220–280 | 35–45 | 25,000–40,000 |
| 1.0 | 82–85 | 27–32 | 200–260 | 65–80 | 40,000–65,000 |
| 2.0 | 84–87 | 29–35 | 190–240 | 125–155 | 65,000–100,000 |
| 5.0 | 85–88 | 30–38 | 180–230 | 300–370 | 120,000–200,000 |
| 10.0 | 86–89 | 32–40 | 170–220 | 590–730 | 200,000–350,000 |
| 15.0 | 87–90 | 33–41 | 165–210 | 880–1080 | 300,000–500,000 |
| 20.0 | 87–90 | 34–42 | 160–200 | 1170–1430 | 400,000–650,000 |
| 30.0 | 87–91 | 34–42 | 155–195 | 1750–2130 | 550,000–900,000 |

> **Not:** Ekonomizer eklenmesi durumunda verim %3–5 artar, baca gazi sicakligi 120–150 °C'ye duser.
> Yatirim maliyetleri 2025 yili Avrupa piyasa fiyatlaridir, montaj haric.

## Enerji Tasarrufu Potansiyeli

| Onlem | Tasarruf (%) | Tipik Geri Odeme | Detay |
|-------|-------------|-----------------|-------|
| Ekonomizer (economizer) montaji | 3–5 | 1–2 yil | Baca gazi ile besleme suyunu on isitma |
| Hava on isitici (air preheater) | 1–3 | 2–3 yil | Baca gazi ile yanma havasini on isitma |
| O2 trim kontrolu (O2 trim control) | 1–2 | 0.5–1 yil | Brulor hava/yakit oranini optimize eder |
| Kondensat geri kazanimi (condensate recovery) | 5–10 | 0.5–1.5 yil | Sicak kondensatin kazan besleme suyuna donusu |
| Blowdown isi geri kazanimi (blowdown heat recovery) | 0.5–1.5 | 1–2 yil | Flash buhar ve isi degistiricisi ile |
| Yalitim iyilestirme (insulation improvement) | 0.5–1 | 0.5–1 yil | Govde ve boru hatti yalitimi |
| Brulor degisimi (burner replacement) | 2–4 | 2–3 yil | Eski bruloru modulasyonlu brulor ile degistirme |
| Yuk yonetimi (load management) | 1–3 | — | Birden fazla kazan optimum yuklenme sirasi |

## Avantajlar ve Dezavantajlar

### Avantajlar

- **Kompakt tasarim:** Dusuk tesis alani gerektirir, kurulumu kolaydir
- **Hizli buhar uretimi:** Kucuk yukler icin 15–30 dakikada buhar uretir (soguk baslatmada)
- **Basit isletme:** Operatorun egitimi kolay, otomatik kontrol sistemi standart
- **Dusuk yatirim maliyeti:** Su borulu kazanlara gore %20–40 daha ucuz
- **Genis buhar depolama kapasitesi:** Buyuk su hacmi sayesinde yuk dalgalanmalarina dayanikli
- **Kolay bakim:** Boru temizligi ve muayene erisimi kolaydir
- **Yaygin servis agi:** Turkiye'de yedek parca ve servis kolayligi yuksek

### Dezavantajlar

- **Sinirli basinc:** Maksimum ~25–30 bar (yuksek basinc uygulamalari icin uygun degil)
- **Sinirli kapasite:** Maksimum ~30 ton/saat (buyuk prosesler icin yetersiz)
- **Yavas yuk tepkisi:** Buyuk ve ani yuk degisimlerine karsi su borulu kazanlar kadar hizli degil
- **Yuksek spesifik yakit tuketimi:** Buyuk kapasitelerde su borulu kazanlara gore daha fazla yakit tuketir
- **Patlama riski:** Buyuk su hacmi nedeniyle govde patlama riski su borulu kazanlara gore daha yuksektir
- **Sinirli asiri isitma:** Kizgin buhar (superheated steam) uretimi icin ek ekipman gerektirir

## Dikkat Edilecekler

1. **Baca gazi sicakligi:** 200 °C'nin uzerinde ise ekonomizer montaji degerlendirilmelidir; her 20 °C dusus ~%1 verim artisi saglar.
2. **Fazla hava kontrolu:** Baca gazindaki O2 degeri %3–5 arasinda tutulmalidir. %6'nin uzerindeki O2, gereksiz isi kaybina neden olur (her %1 fazla O2 ≈ %0.5 verim kaybi).
3. **Besleme suyu sicakligi:** 80 °C'nin altindaki besleme suyu sicakliklari hem verim kaybina hem de kazan govdesinde termal soka (thermal shock) neden olabilir. Minimum 60 °C, ideal 85–105 °C.
4. **Blowdown yonetimi:** Otomatik blowdown sistemi yoksa TDS (toplam cozunmus kati) degeri duzenli olculmelidir. Asiri blowdown (%5 uzerinde) ciddi enerji kaybina yol acar.
5. **Yuzey sicakliklari:** Kazan govde yuzey sicakligi 60 °C'nin uzerindeyse yalitim durumu kontrol edilmelidir. Iyi yalitimli bir kazanda yuzey sicakligi ortam sicakliginin 20 °C ustunu gecmemelidir.
6. **Is cizelgesi ve yuk profili:** Dusuk yuk oranlarinda (%30'un altinda) kazanin verim egrisinin disa bukuk (concave) bolgesine dusulur; on/off calismada verim %5–10 duser.
7. **Su kalitesi:** Besleme suyu sertligi 0.5 °dH'nin altinda tutulmalidir. 1 mm kec (scale) birikimi yaklasik %2 verim kaybina neden olur.
8. **Periyodik bakim:** EN 12953'e gore yillik ic muayene, 4 yilda bir hidrostatik test yapilmalidir. Turkiye'de TSE ve Calisma Bakanligi mevzuatina uyulmalidir.

## Tipik Ariza ve Sorun Tablosu

| Sorun | Olasi Neden | Cozum |
|-------|-------------|-------|
| Dusuk verim | Kec birikimi, fazla hava, kirli baca | Kimyasal temizlik, brulor ayari, baca temizligi |
| Yuksek baca gazi sicakligi | Kirli isi transfer yuzey, kec | Mekanik/kimyasal temizlik |
| Surekli blowdown | Yuksek TDS, kotu su aritma | Su aritma sistemi revizyonu |
| Govde korozyonu | Dusuk pH, cozunmus O2 | Degaze (deaerator) kontrolu, kimyasal dozaj |
| Brulor arizasi | Kirli nozul, fotohucre arizasi | Brulor bakimi, yedek parca degisimi |
| Basinc dalgalanmasi | Ani yuk degisimleri, kontrol valf | PID ayari, yuk yonetimi |

## İlgili Dosyalar

- Su borulu kazan: `equipment/boiler_steam_watertube.md`
- Yakit bilgileri: `equipment/boiler_fuels.md`
- Benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer: `solutions/boiler_economizer.md`
- Exergy hesaplamalari: `formulas/boiler_exergy.md`
- Kondensat geri kazanimi: `solutions/condensate_recovery.md`
- Baca gazi analizi: `formulas/flue_gas_analysis.md`

## Referanslar

1. Spirax Sarco, *The Steam and Condensate Loop*, 2nd Edition — Kapsamli buhar sistemleri referansi
2. Cleaver-Brooks, *Boiler Book* — Endustriyel kazan tasarimi ve isletmesi
3. ASME PTC 4, *Fired Steam Generators* — Kazan performans test kodu
4. EN 12953, *Shell Boilers* — Avrupa govde tipi kazan standardi
5. DOE/AMO, *Steam Best Practices* — ABD Enerji Bakanligi buhar en iyi uygulamalari
6. Turkiye Enerji Verimliligi Dernegi (ENVER), *Endustriyel Kazan Sistemleri Rehberi*
7. ASME Section I, *Rules for Construction of Power Boilers*
8. BS 845, *Methods for Assessing Thermal Performance of Boilers*
