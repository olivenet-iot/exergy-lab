# Hava On Isitici --- Air Preheater

> Son guncelleme: 2026-01-31

## Ozet

**Problem:** Kazan baca gazlari yuksek sicaklikta (tipik 200-350 degC) atmosfere atilir. Bu kayip, toplam yakit enerjisinin %5-15'ini olusturur. Ayrica yanma havasi ortam sicakliginda (15-30 degC) kazana beslenir; dusuk hava sicakligi alev sicakligini ve yanma verimini sinirlar.

**Cozum:** Hava on isitici (air preheater) ile baca gazi atik isisini kullanarak yanma havasini 100-300 degC arasina on isitmak. On isitilmis hava, alev sicakligini artirarak yanma verimini yukselttir ve baca gazi cikis sicakligini dusurir.

**Tipik Tasarruf:** %2-5 yakit tasarrufu (kazan verimi artisi)

**Tipik ROI:** 2-4 yil

## Calisma Prensibi

Hava on isitici, kazanin baca gazi cikisinda yer alir ve baca gazinin termal enerjisini yanma havasina aktarir. Boylece:

1. **Baca gazi cikis sicakligi duser** --> daha az isi kaybi
2. **Yanma havasi sicakligi artar** --> daha yuksek alev sicakligi
3. **Yanma verimi artar** --> yakit molekullerinin daha hizli ve tam yanmasi
4. **Daha dusuk hava fazlasi ile calisma imkani** --> daha az baca gazi kaybi

### On Isitilmis Havanin Yanma Uzerine Etkisi

On isitilmis yanma havasi, alev sicakligini dogrudan arttirir. Daha yuksek alev sicakligi:
- Yanma reaksiyon hizini arttirir (Arrhenius kinetigi)
- Yakit atomizasyonunu ve buharlasmesini iyilestirir (ozellikle agir yakitlarda)
- Daha dusuk hava fazlasi katsayisiyla (lambda) calismayi mumkun kilar
- Dusuk kaliteli yakitlarin (yuksek nemli komur, biyokutle) yanmasini kolaylastirir

### Verim Artisi Formulu

```
Delta_eta = (T_hava_on - T_hava_soguk) / (T_baca_giris - T_hava_soguk) x eta_APH x K_yakit

Burada:
  Delta_eta       : Kazan verim artisi (oran olarak, ornegin 0.03 = %3)
  T_hava_on       : On isitilmis hava sicakligi (degC)
  T_hava_soguk    : Ortam havasi sicakligi (degC)
  T_baca_giris    : Baca gazi hava on isitici giris sicakligi (degC)
  eta_APH         : Hava on isitici etkinligi (tipik 0.60-0.80)
  K_yakit         : Yakit duzeltme faktoru (dogalgaz: 0.85, fuel oil: 0.90, komur: 0.95)
```

### Pratik Kural: Her 20 degC Hava On Isitmasi

```
Her 20 degC yanma havasi on isitmasi --> yaklasik %1 kazan verimi artisi

Ornek:
  Ortam havasi: 20 degC --> On isitilmis hava: 200 degC
  Sicaklik artisi: 180 degC
  Tahmini verim artisi: 180 / 20 x 1% = ~%9 (teorik maksimum)
  Pratikte: %4-6 (isi esanjoru kayiplari ve hava kacaklari nedeniyle)
```

## Hava On Isitici Tipleri

### 1. Rekuperatif Tip (Recuperative Type)

Baca gazi ve yanma havasi sabit metal yuzeyler uzerinden birbirine isi aktarir. Akiskanlar fiziksel olarak birbirinden ayrilmistir.

**Alt Tipler:**
- **Borulu (Tubular):** Celik borular icinden baca gazi, disindan hava gecer (veya tersi). En yaygin rekuperatif tip.
- **Plakali (Plate Type):** Duz veya oluklu plakalar ile isi transferi. Kompakt tasarim.

**Avantajlar:** Hava kacagi yok (%0), basit yapi, kolay bakim
**Dezavantajlar:** Buyuk boyut, agir, yuksek maliyet (buyuk kapasitelerde)

### 2. Rejeneratif Tip (Regenerative Type)

Donen bir isi depolama kutlesi (rotor), baca gazindan isi alir ve yanma havasina aktarir. En bilinen tipi **Ljungstrom** hava on isiticidir.

**Ljungstrom Hava On Isitici:**
- Donen silindirik rotor, oluklu metal saclardan olusur
- Rotor yavas doner (1-3 d/dk)
- Bir yarisinda baca gazi gecer (isiyi alir), diger yarisinda hava gecer (isiyi birakir)
- Buyuk kapasiteli santral ve endustriyel kazanlarda tercih edilir

**Avantajlar:** Kompakt (birim kapasiteye gore), yuksek isi transfer yuzeyi, ucuz (buyuk kapasitelerde)
**Dezavantajlar:** Hava kacagi (%5-15 arasi), karmasik sIzdIrmazlIk, hareketli parcalar

## Karsilastirma Tablolari

### Rekuperatif vs Rejeneratif Hava On Isitici

| Ozellik | Rekuperatif (Tubular/Plate) | Rejeneratif (Ljungstrom) |
|---------|----------------------------|--------------------------|
| Hava kacagi | %0 (sifir) | %5-15 |
| Isi transfer yuzeyi | 50-200 m2/(MW yakit) | 20-80 m2/(MW yakit) |
| Boyut / agirlik | Buyuk | Kompakt (birim kapasiteye gore) |
| Bakim karmasikligi | Dusuk | Orta-yuksek (sIzdIrmazlIk, rotor) |
| Tipik uygulama | Kucuk-orta kazanlar (<50 MW) | Buyuk kazanlar (>50 MW), santraller |
| Hareketli parca | Yok | Rotor, tahrik sistemi |
| Maliyet (kucuk kapasite) | Dusuk | Yuksek |
| Maliyet (buyuk kapasite) | Yuksek | Orta |
| Maksimum hava on isitma | 250 degC | 350 degC |
| Tipik etkinlik | %60-75 | %70-85 |
| Korozyon direnci | Iyi (malzeme secimi ile) | Orta (donen parcalarda zorluk) |

### Ekonomizer vs Hava On Isitici Karsilastirmasi

| Ozellik | Ekonomizer (Su On Isitma) | Hava On Isitici |
|---------|--------------------------|-----------------|
| Isitilan akiskan | Besleme suyu | Yanma havasi |
| Tipik verim artisi | %3-5 | %2-5 |
| Minimum baca gazi sicakligi | ~105 degC (dogalgaz), ~160 degC (fuel oil) | ~120 degC (dogalgaz), ~170 degC (fuel oil) |
| Korozyon riski | Dusuk (su tarafi) | Orta-yuksek (hava tarafinda asit yogusmasi) |
| Dogalgaz kazanlarinda | Cok tercih edilir | Nadiren gerekli (ekonomizer yeterli) |
| Fuel oil kazanlarinda | Tercih edilir | Ekonomizerle birlikte uygulanabilir |
| Komur kazanlarinda | Tercih edilir | Cok yaygin, ozellikle buyuk kazanlarda |
| Biyokutle kazanlarinda | Tercih edilir | Yaygin (nemli yakitlarda gerekli) |
| Yatirim maliyeti | Orta | Orta-yuksek |
| Fouling riski | Dusuk (su tarafi temiz) | Yuksek (baca gazi tarafinda kul/kurum) |
| Tipik ROI | 1-3 yil | 2-4 yil |

**Genel kural:** Dogalgaz kazanlarinda once ekonomizer uygulanir; hava on isitici genellikle gerekli degildir. Komur ve fuel oil kazanlarinda her ikisi birden uygulanabilir --- once ekonomizer, ardindan hava on isitici.

## Uygulanabilirlik Kriterleri

| Kriter | Minimum | Ideal |
|--------|---------|-------|
| Kazan kapasitesi | 5 MW_th | >20 MW_th |
| Baca gazi sicakligi | >200 degC | >280 degC |
| Yakit tipi | Fuel oil, komur, biyokutle | Yuksek kukurtlu fuel oil, komur |
| Calisma saati | 4000 saat/yil | >6000 saat/yil |
| Mevcut ekonomizer | Var (ek tasarruf icin APH) | Ekonomizer + APH birlikte |
| Hava fazlasi katsayisi (lambda) | >1.15 | >1.25 |

### Ne Zaman Uygulanmali

- Komur veya fuel oil yakitli buyuk kazanlarda (>10 MW)
- Baca gazi sicakligi ekonomizer sonrasi hala >200 degC olan sistemlerde
- Yuksek nemli biyokutle yakan kazanlarda (kurutma etkisi icin)
- Hava fazlasi katsayisi yuksek olan eski kazanlarda
- Dusuk kaliteli yakit kullanan tesislerde

### Ne Zaman Uygulanmamali

- Kucuk dogalgaz kazanlarinda (<5 MW) --- ekonomizer yeterlidir
- Baca gazi sicakligi zaten <180 degC olan sistemlerde
- Kukurt icerikli yakitlarda baca gazi sicakligi asit cig noktasina yakin ise
- Hava kanallarinin fiziksel yerlestirme alani yoksa

## Tipik Hava On Isitma Sicakliklari

| Yakit Tipi | Ortam Havasi (degC) | On Isitilmis Hava (degC) | Baca Gazi Girisi (degC) | Baca Gazi Cikisi (degC) |
|------------|---------------------|--------------------------|-------------------------|-------------------------|
| Dogalgaz | 20 | 100-150 | 200-250 | 120-160 |
| Fuel Oil No.2 | 20 | 150-200 | 250-300 | 160-200 |
| Fuel Oil No.6 | 20 | 200-280 | 280-350 | 170-220 |
| Bitumlu komur | 20 | 200-300 | 300-400 | 150-200 |
| Linyit | 20 | 250-350 | 350-450 | 160-220 |
| Biyokutle (nemli) | 20 | 150-250 | 250-350 | 140-200 |

## Yatirim Maliyeti

| Kazan Kapasitesi (MW_th) | Rekuperatif APH Maliyeti (EUR) | Rejeneratif APH Maliyeti (EUR) | Kurulum (EUR) | Toplam (EUR) |
|--------------------------|-------------------------------|-------------------------------|---------------|-------------|
| 5-10 | 15,000-35,000 | --- | 5,000-10,000 | 20,000-45,000 |
| 10-25 | 35,000-80,000 | 50,000-90,000 | 10,000-25,000 | 45,000-115,000 |
| 25-50 | 80,000-160,000 | 70,000-140,000 | 25,000-50,000 | 95,000-210,000 |
| 50-100 | 160,000-350,000 | 120,000-250,000 | 50,000-100,000 | 170,000-450,000 |
| >100 | Ozel proje | 200,000-500,000 | 80,000-200,000 | 280,000-700,000 |

**Not:** Rejeneratif tip kucuk kapasitelerde maliyet-etkin degildir; 50 MW uzerinde avantajli hale gelir. "---" rejeneratif tipin o kapasitede tipik olarak uygulanmadigini gosterir.

## ROI Hesabi

### Formul

```
Yakit_tasarrufu_yillik = Q_kazan x (1/eta_eski - 1/eta_yeni) x t_calisma

Burada:
  Q_kazan       : Kazan faydali isi cikisi (kW)
  eta_eski      : Mevcut kazan verimi (oran, ornegin 0.85)
  eta_yeni      : APH sonrasi kazan verimi (oran, ornegin 0.89)
  t_calisma     : Yillik calisma suresi (saat/yil)

Parasal tasarruf (EUR/yil):
Tasarruf = Yakit_tasarrufu_yillik x Yakit_birim_fiyati

Geri odeme suresi (yil):
ROI = Toplam_yatirim / Tasarruf
```

### Ornek ROI Hesabi

**Senaryo:** 30 MW_th komur yakitli kazan, 6000 saat/yil, mevcut verim %84, baca gazi 310 degC

```
APH ile beklenen verim artisi: %4 --> yeni verim = %88

Yakit_tasarrufu = 30,000 kW x (1/0.84 - 1/0.88) x 6000 saat/yil
               = 30,000 x (1.1905 - 1.1364) x 6000
               = 30,000 x 0.0541 x 6000
               = 9,738,000 kWh/yil = 9,738 MWh/yil

Komur maliyeti: ~25 EUR/MWh (linyit)
Tasarruf = 9,738 x 25 = 243,450 EUR/yil

Yatirim: Rekuperatif APH = 100,000 EUR + kurulum 30,000 EUR = 130,000 EUR
Geri odeme = 130,000 / 243,450 = 0.53 yil

Not: Bu optimistik bir senaryo. Pratikte bakim maliyetleri, hava kacagi
kayiplari ve kapasite faktorleri dahil edildiginde geri odeme 1.5-3 yil arasindadir.
```

### Alternatif: Hava On Isitma Derecesine Gore Tasarruf

```
Yakit tasarrufu (%) = (T_hava_on - T_ortam) x 0.05

Burada:
  T_hava_on : On isitilmis hava sicakligi (degC)
  T_ortam   : Ortam sicakligi (degC)
  0.05      : Yaklasik katsayi (%/degC), her derece hava on isitma
              icin yaklasik %0.05 yakit tasarrufu

Ornek: 250 degC on isitma, 20 degC ortam
  Tasarruf = (250 - 20) x 0.05 = %11.5 (teorik)
  Pratikte: %4-6 (kayiplar dahil)
```

## Uygulama Adimlari

1. **Mevcut durum analizi:** Baca gazi sicakligi, yakit tipi, baca gazi bilesimi (O2, CO2, SO2) olcumu
2. **Asit cig noktasi hesabi:** Yakittaki kukurt icerigine gore minimum baca gazi sicakliginin belirlenmesi
3. **APH tipi secimi:** Kazan kapasitesi, yakit tipi ve tesis yerlesim duzeni degerlendirilmesi (rekuperatif vs rejeneratif)
4. **Isil tasarim hesaplari:** Isi transfer yuzeyi, hava/baca gazi debileri, basinc kayiplari hesabi
5. **Kanal sistemi tasarimi:** Hava ve baca gazi kanallarinin fiziksel yerlestirmesi ve boyutlandirmasi
6. **Fan kapasitesi kontrolu:** Mevcut ID fan (induced draft) ve FD fan (forced draft) kapasitelerinin yeni basinc kayiplarina yeterliligi
7. **En az 3 tedarikciden teklif alinmasi** (teknik sartname ile birlikte)
8. **Imalat ve kurulum:** Tipik olarak 3-6 ay (buyuk projeler icin 6-12 ay)
9. **Devreye alma ve performans testi:** Baca gazi sicakligi, hava on isitma sicakligi, hava kacagi olcumu
10. **Performans dogrulama:** Kurulumdan 1-3 ay sonra verim testi (ASME PTC 4 veya EN 12952-15 uyarinca)

## Riskler ve Dikkat Edilecekler

| Risk | Aciklama | Onlem |
|------|----------|-------|
| Dusuk sicaklik korozyonu (Low-temperature corrosion) | Baca gazi sicakligi asit cig noktasinin altina duserse H2SO4 yogusmasi ile metal yuzeyler hizla korozyona ugrar | Minimum baca gazi cikis sicakligini asit cig noktasinin 15-25 degC uzerinde tutmak; kukurtlu yakitlarda cam kapli veya emaye kapli yuzeyler kullanmak |
| Hava kacagi (Air leakage) | Rejeneratif tiplerde rotor sIzdIrmazlIklari zamanla asinir, hava kacagi %5'ten %15-20'ye yukselir | Periyodik sIzdIrmazlIk kontrolu (6 ayda bir); sIzdIrmazlIk parcalarini zamaninda degistirmek; radyal ve aksiyel sIzdIrmazlIk basinc farki izlenmesi |
| Fouling (kirlenme) | Baca gazi tarafinda kul, kurum ve yapiskan birikintiler isi transfer yuzeyini kapatir; ozellikle komur ve agir yakitlarda ciddi problem | Kumlama (sootblowing) sistemi; periyodik kimyasal temizlik; on isitici girisine partikul tutucu |
| Erozyon | Kul iceren baca gazlari yuksek hizda metal yuzeyleri asindirabilir | Baca gazi hizini <15 m/s tutmak; asinmaya dayanikli malzeme (Corten celigi); kul yogunlugu yuksek bolgede kalinlastirilmis saclar |
| Fan gucu artisi | APH baca gazi ve hava tarafinda ek basinc kaybi yaratir; mevcut fanlar yetmeyebilir | Tasarim asamasinda fan kapasitesi dogrulamasi; gerekirse fan motor degisimi veya VSD eklenmesi |
| Yangin riski | Rejeneratif tiplerde yanmamis yakit kalintilari birikebilir ve tutusubilir | Sicaklik izleme sistemi; otomatik yangin sondurme (su spreyi); dusuk yuklu calismalarda dikkatli izleme |

## Asit Cig Noktasi Referans Tablosu

Kukurt icerigine gore baca gazinin asit cig noktasi ve onerilen minimum cikis sicakligi:

| Yakit | Kukurt Icerigi (%) | Asit Cig Noktasi (degC) | Minimum Baca Gazi Cikisi (degC) |
|-------|---------------------|--------------------------|-------------------------------|
| Dogalgaz | ~0 | ~55 (su buhari cig noktasi) | 80 (yoqusmali: <55) |
| Fuel Oil No.2 | 0.1-1.0 | 110-135 | 130-155 |
| Fuel Oil No.6 | 1.0-3.5 | 120-160 | 145-180 |
| Bitumlu komur | 0.5-3.0 | 120-155 | 140-175 |
| Linyit | 0.5-6.0 | 110-170 | 130-195 |

## Ekserji Analizi: Hava On Isitici

Hava on isitici, baca gazinin ekserjisini yanma havasina aktarir ve boylece yanma ekserjisinin bir kismini geri kazanir.

```
Ekserji kazanimi (hava tarafinda):
Ex_hava = m_hava x cp_hava x [(T_on - T_soguk) - T0 x ln(T_on/T_soguk)]

Ekserji kaybi (baca gazi tarafinda):
Ex_baca_kayip = m_baca x cp_baca x [(T_giris - T_cikis) - T0 x ln(T_giris/T_cikis)]

APH ekserji verimi:
eta_ex_APH = Ex_hava / Ex_baca_kayip

Burada:
  m_hava, m_baca : Hava ve baca gazi kutle debileri (kg/s)
  cp_hava        : Havanin ortalama ozgul isisi (~1.01 kJ/kg.K)
  cp_baca        : Baca gazinin ortalama ozgul isisi (~1.05-1.10 kJ/kg.K)
  T_on, T_soguk  : On isitilmis ve soguk hava sicakliklari (K, mutlak)
  T_giris, T_cikis: Baca gazi giris ve cikis sicakliklari (K, mutlak)
  T0             : Referans cevre sicakligi (298.15 K = 25 degC)
  eta_ex_APH     : APH ekserji verimi (tipik 0.25-0.50)
```

**Not:** Hava on isiticide ekserji verimi enerji veriminden onemli olcude dusuktur; cunku dusuk sicaklikli akiskanlar arasindaki isi transferi tersinmezdir.

## Ilgili Dosyalar

- Kazan yakitlari ve ozellikleri: `equipment/boiler_fuels.md`
- Buhar sistemleri genel bakis: `equipment/steam_systems_overview.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Yanma optimizasyonu (brulor ayari): `solutions/boiler_combustion_optimization.md`
- Baca gazi isi geri kazanimi: `solutions/boiler_flue_gas_recovery.md`
- Kazan ekserji hesaplamalari: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`

## Referanslar

- Basu, P., Kefa, C., Jestin, L. (2000). *Boilers and Burners: Design and Theory*, Springer.
- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators*, Marcel Dekker.
- Ljungstrom, F. (1920). "Regenerative Air Preheater" --- Orijinal patent (ABB/Alstom miras teknolojisi).
- ASME PTC 4 (2013). *Fired Steam Generators --- Performance Test Codes*, ASME.
- EN 12952-15 (2003). *Water-tube Boilers --- Acceptance Tests*, CEN.
- Spirax Sarco (2023). *The Steam and Condensate Loop*, Technical Reference Guide.
- U.S. DOE/AMO (2012). "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths. (Reprinted by Krieger, 1995.)
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
- Rosen, M.A., Dincer, I. (1999). "Exergy Analysis of Waste Emissions," *Int. J. Energy Research*.
- EPA AP-42 (1998). *Compilation of Air Pollutant Emission Factors*, Chapter 1: External Combustion Sources.
