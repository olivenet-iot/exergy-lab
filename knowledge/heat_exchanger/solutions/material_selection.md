---
title: "Malzeme Secimi Rehberi (Material Selection Guide)"
category: solution
equipment_type: heat_exchanger
keywords: [malzeme, korozyon, paslanmaz celik, titanyum, hastelloy, material selection, corrosion]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/audit.md, heat_exchanger/solutions/fouling_management.md]
use_when: ["Korozyon veya erozyon sorunu tespit edildiginde", "Yeni esanjor malzeme secimi yapilirken", "Mevcut esanjor malzeme degisimi degerlendirilirken"]
priority: low
last_updated: 2026-02-01
---
# Malzeme Secimi Rehberi (Material Selection Guide)

> Son guncelleme: 2026-02-01

## Ozet

**Problem:** Yanlis malzeme secimi isi esanjorlerinde korozyon, erozyon, gerilme catlamasi ve erken arizaya neden olur. Korozyon kaynakli boru ariza ve sizma olayli hem uretim kaybi hem de guvenlik riski olusturur. Ayrica korozyon urunleri kirlenme (fouling) kaynagi olarak isi transfer performansini dusurebilir.

**Cozum:** Akiskan ozellikleri, sicaklik, basinc ve korozyon ortamina uygun malzeme secimi. Maliyet-performans optimizasyonu ile uzun vadeli guvenilirlik ve verimlilik saglanmasi.

**Tipik Etki:** Esanjor omrunu 2-5 kat uzatma, korozyon kaynakli kirlenmenin eliminasyonu
**Tipik ROI:** 2-5 yil (uzun omur ve azalmis bakim ile)

## Yaygin Malzemeler ve Ozellikleri

### Karbon Celik (Carbon Steel — CS, SA-516 Gr.70 / SA-179)

- **Kullanim alani:** En yaygin, ekonomik malzeme; temiz su, buhar, hafif hidrokarbonlar
- **Sicaklik siniri:** -29 C ile +425 C
- **Korozyona dayanim:** Sinirli; pH 5-9 arasinda kabul edilebilir; klorur ve asitlere dayanmaz
- **Avantajlar:** Dusuk maliyet, kolay islenebilirlik, yaygin bulunurluk
- **Dezavantajlar:** Korozyona hassas, kirlenme kaynagi olabilir (pas)
- **Goreli maliyet:** 1.0x (referans)

### Paslanmaz Celik 304 (SS 304, UNS S30400)

- **Kullanim alani:** Genel endustriyel, gida, kimya; hafif korozif ortamlar
- **Sicaklik siniri:** -196 C ile +800 C
- **Korozyona dayanim:** Iyi; bircok asit ve alkali ortamda dayanikli; klorur ortaminda cukurcuk korozyonu riski
- **Avantajlar:** Iyi korozyon direnci, hijyenik yuzey, kaynaklanabilir
- **Dezavantajlar:** Klorur SCC (Stress Corrosion Cracking) riski >50 C, cukurcuk korozyonu
- **Goreli maliyet:** 2.0-2.5x

### Paslanmaz Celik 316 / 316L (SS 316L, UNS S31603)

- **Kullanim alani:** Deniz suyu, klorurlu ortamlar, kimya/ilac endustrisi
- **Sicaklik siniri:** -196 C ile +800 C
- **Korozyona dayanim:** 304'e gore ustun (Mo icerigi sayesinde); klorur dayanimi daha iyi
- **Avantajlar:** Iyi cukurcuk direnci, klorur SCC direnci (sinirli), gida uyumlu
- **Dezavantajlar:** Agresif klorur ortaminda yetersiz (>1,000 ppm Cl @ >60 C), maliyet
- **Goreli maliyet:** 2.5-3.0x

### Dupleks Paslanmaz Celik (Duplex SS, UNS S31803 / S32205)

- **Kullanim alani:** Deniz suyu, petrokimya, yuksek klorur ortamlari
- **Sicaklik siniri:** -50 C ile +300 C
- **Korozyona dayanim:** Cok iyi; yuksek klorur direnci, SCC direnci
- **Avantajlar:** Yuksek mukavemet (ince duvar -> daha az malzeme), iyi korozyon direnci
- **Dezavantajlar:** Yuksek maliyet, kaynak ozel dikkat gerektirir
- **Goreli maliyet:** 3.0-4.0x

### Titanyum (Titanium — Grade 1, 2)

- **Kullanim alani:** Deniz suyu, klorlu ortamlar, organik asitler, brom/klor iceren cozeltiler
- **Sicaklik siniri:** -50 C ile +300 C
- **Korozyona dayanim:** Mukemmel; deniz suyunda neredeyse sifir korozyon, cukurcuk direnci ustun
- **Avantajlar:** Cok uzun omur (>25 yil deniz suyu), hafif, ince duvar
- **Dezavantajlar:** Yuksek maliyet, HF (hidroflorik asit) ve kuru klor'a dayanmaz
- **Goreli maliyet:** 5.0-8.0x

### Bakir-Nikel Alasimlari (Cu-Ni, C70600 / C71500)

- **Kullanim alani:** Deniz suyu sogutma sistemleri, kondenser borulari
- **C70600 (90/10):** %90 Cu, %10 Ni — sicaklik siniri 250 C
- **C71500 (70/30):** %70 Cu, %30 Ni — daha iyi korozyon direnci
- **Korozyona dayanim:** Deniz suyunda iyi; antifouling ozelligi (bakir iyonu, biyofilm engeller)
- **Avantajlar:** Dogal anti-biyokirlenme, iyi isi iletimi, deniz suyu uyumu
- **Dezavantajlar:** Sulfur iceren ortamlarda hassas, amonyak SCC
- **Goreli maliyet:** 3.0-5.0x

### Hastelloy C-276 (UNS N10276)

- **Kullanim alani:** Agresif kimya, kuvvetli asitler (HCl, H2SO4, HNO3), yuksek sicaklik korozyon
- **Sicaklik siniri:** -196 C ile +1,090 C
- **Korozyona dayanim:** Ustun; hemen hemen tum korozif ortamlarda mükemmel
- **Avantajlar:** Universal korozyon direnci, genis sicaklik araligi
- **Dezavantajlar:** Cok yuksek maliyet, islenebilirlik zorlugu
- **Goreli maliyet:** 8.0-12.0x

### Inconel 625 (UNS N06625)

- **Kullanim alani:** Yuksek sicaklik korozif ortamlar, baca gazi, asidik kondensasyon
- **Sicaklik siniri:** -196 C ile +980 C
- **Korozyona dayanim:** Cok iyi; yuksek sicaklik oksidasyonuna ustun direnc
- **Avantajlar:** Yuksek sicaklik mukavemeti, korozyon direnci, yorulma direnci
- **Dezavantajlar:** Cok yuksek maliyet
- **Goreli maliyet:** 7.0-10.0x

## Korozyon Turleri ve Mekanizmalari

### 1. Uniform (Duz) Korozyon

- **Mekanizma:** Tum yuzey boyunca esit hizda metal kaybi
- **Olcum:** Korozyon hizi (mm/yil)
- **Risk faktorleri:** Asidik ortam, yuksek sicaklik, oksijen varligi

| Korozyon Hizi (mm/yil) | Degerlendirme | Aksiyon |
|------------------------|---------------|---------|
| <0.05 | Mukemmel | Normal isletme |
| 0.05-0.13 | Iyi | Izlemeye devam |
| 0.13-0.25 | Kabul edilebilir | Denetim sikligi artir |
| 0.25-1.0 | Zayif | Malzeme degisikligi degerlendir |
| >1.0 | Kabul edilemez | Derhal malzeme degistir |

### 2. Cukurcuk Korozyonu (Pitting Corrosion)

- **Mekanizma:** Pasif film tabakasinin lokal bozulmasi ile derin cukurcuk olusumu
- **Risk faktorleri:** Klorur iyonu, durgun bolgeler, oksijen konsantrasyon farki
- **PREN (Pitting Resistance Equivalent Number):**

```
PREN = %Cr + 3.3 x %Mo + 16 x %N

PREN > 40: Deniz suyu uyumlu
PREN 30-40: Yuksek klorur direnci
PREN 20-30: Orta klorur direnci
PREN < 20: Dusuk klorur direnci
```

| Malzeme | PREN | Deniz Suyu Uyumu |
|---------|------|-----------------|
| SS 304 | 18-20 | Uygun degil |
| SS 316 | 24-28 | Sinirli (<40 C) |
| SS 316L | 24-28 | Sinirli (<40 C) |
| Duplex 2205 | 34-38 | Iyi (<60 C) |
| Super duplex 2507 | 40-45 | Cok iyi |
| Titanyum Gr.2 | — (pasif film) | Mukemmel |
| Hastelloy C-276 | 69+ | Mukemmel |

### 3. Crevice Korozyonu (Arasik Korozyonu)

- **Mekanizma:** Dar araliklarda (conta, boru-tubesheet birlesimi) oksijen tukenmesi ile lokal korozyon
- **Risk faktorleri:** Dar arasiklar, klorurlu ortam, durgun sivi
- **Onlem:** Crevice-free tasarim, tam nüfuziyet kaynak, kauçuk conta yerine metalik conta

### 4. Gerilme Korozyonu Catlamasi (SCC — Stress Corrosion Cracking)

- **Mekanizma:** Cekme gerilmesi + korozif ortam = ani catlik yayilimi
- **Tipik kombinasyonlar:**

| Malzeme | SCC Tetikleyen Ortam | Kritik Sicaklik |
|---------|---------------------|-----------------|
| SS 304/316 | Klorur cozeltisi | >50 C |
| Karbon celik | NaOH (kostik) | >80 C |
| Cu alasimi | Amonyak | >25 C |
| Titanyum | Metanol + HCl | >50 C |

### 5. Galvanik Korozyon (Galvanic Corrosion)

- **Mekanizma:** Farkli metallerin elektrik iletken ortamda temas etmesi ile anodik metalin hizli korozyonu
- **Onlem:** Ayni veya yakin galvanik seriden malzeme kullanimi, yalitim boslugu, galvanik koruma

```
Galvanik seri (soydan asiye):
  Platin -> Altin -> Titanyum -> SS 316 -> SS 304 -> Nikel ->
  Cu-Ni -> Bronz -> Bakir -> Kalay -> Kursun -> Karbon celik ->
  Aluminyum -> Cinko -> Magnezyum
```

## Akiskan-Malzeme Uyum Tablosu

| Akiskan | CS | SS 304 | SS 316 | Duplex | Ti | Cu-Ni | Hastelloy |
|---------|-----|--------|--------|--------|-----|-------|-----------|
| Temiz su (<60 C) | A | A | A | A | A | A | A |
| Sert su (>200 ppm) | B | A | A | A | A | B | A |
| Deniz suyu | D | C | C | B | A | B | A |
| Buhar (temiz) | A | A | A | A | A | B | A |
| Dogalgaz (kuru) | A | A | A | A | A | — | A |
| Baca gazi (dusuk S) | B | A | A | A | A | — | A |
| Baca gazi (yuksek S) | D | C | C | B | A | — | A |
| HCl (seyreltik <5%) | D | D | C | C | A* | D | A |
| H2SO4 (seyreltik) | D | C | C | B | C | D | A |
| HNO3 (seyreltik) | D | A | A | A | A | D | A |
| NaOH (<30%) | B | A | A | A | A | — | A |
| Amonyak | A | A | A | A | A | D | A |
| Motor yagi | A | A | A | A | A | A | A |
| Gida urunleri | C | A | A | A | A | C | A |

**Kodlar:** A = Mukemmel, B = Iyi, C = Sinirli (dikkatli kullanim), D = Uygun degil
**Ti*:** Titanyum HF icermeyen HCl icin uygundur.

## Malzeme Maliyet Karsilastirma Tablosu

Govde-boru esanjor boru maliyeti (dis cap 19.05 mm, 1.65 mm duvar, 1 metre uzunluk bazinda):

| Malzeme | Goreli Maliyet | EUR/m (yaklasik) | Yogunluk (kg/m3) | Termal Iletkenlik W/(m-K) |
|---------|---------------|-----------------|-------------------|--------------------------|
| Karbon celik (SA-179) | 1.0x | €3-5 | 7,850 | 50 |
| SS 304 (SA-213 TP304) | 2.2x | €7-11 | 7,900 | 16 |
| SS 316L (SA-213 TP316L) | 2.8x | €9-14 | 7,980 | 16 |
| Duplex 2205 | 3.5x | €11-17 | 7,800 | 19 |
| Titanyum Gr.2 (SB-338) | 6.0x | €18-30 | 4,510 | 22 |
| Cu-Ni 90/10 (SB-111) | 4.0x | €12-20 | 8,900 | 45 |
| Cu-Ni 70/30 (SB-111) | 5.0x | €15-25 | 8,950 | 30 |
| Hastelloy C-276 (SB-619) | 10.0x | €30-50 | 8,890 | 10 |
| Inconel 625 (SB-444) | 8.5x | €26-43 | 8,440 | 10 |

**Not:** Fiyatlar 2026 tahminidir ve hammadde fiyat dalgalanmalarina bagli olarak degisebilir. Govde maliyeti ayri hesaplanmalidir.

## Sicaklik Sinirlari

| Malzeme | Min. Sicaklik (C) | Max. Sicaklik (C) | Ozel Not |
|---------|-------------------|--------------------|----------|
| Karbon celik | -29 | +425 | >425 C surtunme kaybi |
| SS 304 | -196 | +800 | >425 C sensitizasyon riski |
| SS 304L | -196 | +800 | Dusuk karbon, kaynak sonrasi |
| SS 316 | -196 | +800 | Mo ile geliştirilmis |
| SS 316L | -196 | +800 | Kaynak sonrasi sensitizasyon direnci |
| Duplex 2205 | -50 | +300 | >300 C sigma faz riski |
| Super Duplex 2507 | -50 | +250 | Sigma faz hassasiyeti |
| Titanyum Gr.2 | -50 | +300 | Oksijen ortaminda >300 C yanma |
| Cu-Ni 90/10 | -200 | +250 | Sulfur ortaminda <200 C |
| Cu-Ni 70/30 | -200 | +300 | Daha iyi yuksek sicaklik |
| Hastelloy C-276 | -196 | +1,090 | Genis aralik |
| Inconel 625 | -196 | +980 | Yuksek sicaklik ustun |
| Aluminyum 3003 | -270 | +200 | Kriyojenik uygun |

## Ozel Kaplamalar ve Astarlar

Baz malzeme uzerine kaplama ile korozyon direncini artirma:

| Kaplama / Astar | Kalinlik (um) | Sicaklik Siniri (C) | Uygulama | Goreli Maliyet |
|-----------------|--------------|---------------------|----------|----------------|
| Epoksi kaplama | 200-500 | 80 | Sogutma suyu, asidik su | 0.3x (CS bazinda) |
| Cam astar (glass lining) | 1,500-2,000 | 200 | Kimya, farma | 2.0-3.0x |
| PTFE (Teflon) kaplama | 25-100 | 260 | Agresif kimyasallar | 1.5-2.5x |
| Rubber lining (kaucuk) | 3,000-6,000 | 100 | H2SO4, HCl, deniz suyu | 1.0-2.0x |
| Nikel kaplama | 50-200 | 400 | Alkali, kostik | 1.5-2.5x |
| Krom kaplama | 25-100 | 500 | Erozyon direnci | 1.0-2.0x |
| Termik sprey (HVOF) | 100-500 | 800+ | Erozyon + korozyon | 2.0-4.0x |

### Kaplama vs Bulk Malzeme Karari

```
Kaplama tercih:
  - Korozif ortam sadece bir tarafta
  - Govde korumasi gerekli (boru degisimi mumkun)
  - Maliyet sinirlamasi var

Bulk malzeme (tam alasim) tercih:
  - Her iki taraf korozif
  - Boru degisimi zorlugu
  - Uzun omur beklentisi (>15 yil)
  - Kaplama hasari riski yuksek (erozyon, termal sok)
```

## Isi Transferi ve Exergy Uzerine Etki

Malzeme secimi isi transfer performansini dolayii yoldan etkiler:

```
Boru duvari termal direnci:
  R_wall = t_wall / (k_material x A_m)

Burada:
  t_wall = Duvar kalinligi [m]
  k_material = Termal iletkenlik [W/(m-K)]
  A_m = Ortalama transfer alani [m2]
```

| Malzeme | k W/(m-K) | R_wall (m2-K/kW) 1.65mm duvar | Etki |
|---------|-----------|-------------------------------|------|
| Karbon celik | 50 | 0.033 | Ihmal edilebilir |
| Cu-Ni 90/10 | 45 | 0.037 | Ihmal edilebilir |
| Titanyum | 22 | 0.075 | Dusuk (ince duvar ile telafi) |
| Duplex SS | 19 | 0.087 | Dusuk-orta |
| SS 304/316 | 16 | 0.103 | Orta |
| Hastelloy C-276 | 10 | 0.165 | Orta-yuksek |
| Inconel 625 | 10 | 0.165 | Orta-yuksek |

**Not:** Dusuk termal iletkenlikli malzemelerde ince duvar kullanimi (yuksek mukavemet sayesinde) boru duvari direncini azaltabilir. Titanyum ve dupleks celikler bu avantaji saglar.

### Korozyon Urunlerinin Kirlenme ve Exergy Etkisi

```
Yanlis malzeme -> korozyon -> korozyon urunleri birikimi (fouling)
  -> R_f artisi -> U dususu -> DT_approach artisi -> S_gen artisi -> Ex_d artisi

Dogru malzeme -> korozyon yok -> temiz yuzey
  -> R_f ~ 0 -> U korunur -> DT_approach optimize -> S_gen minimum -> Ex_d minimum
```

Sayisal etki ornegi:
- Karbon celik boru, korozif ortam: R_f = 0.35 m2-K/kW (korozyon kirlenmesi)
- SS 316L boru, ayni ortam: R_f = 0.05 m2-K/kW (minimum kirlenme)
- Titanyum boru, ayni ortam: R_f = 0.02 m2-K/kW (hemen hemen sifir)

U-deger farki: %15-30 → Exergy verimi farki: %3-8 mutlak

## Malzeme Secim Karar Agaci

```
Akiskan ve kosullari belirle
  |
  +-- Klorur icerigi?
  |     |-- <200 ppm -> Karbon celik veya SS 304
  |     |-- 200-1,000 ppm -> SS 316L veya Duplex
  |     |-- >1,000 ppm -> Titanyum, Super Duplex, veya Hastelloy
  |
  +-- Sicaklik?
  |     |-- <100 C -> Genis malzeme secenegi
  |     |-- 100-300 C -> Duplex sinirli, SS/Ti/Ni alasimi
  |     |-- >300 C -> Ni alasimlari, ozel celikler
  |
  +-- pH?
  |     |-- <4 (asidik) -> SS 316L, Hastelloy, Ti (asite bagli)
  |     |-- 4-9 (notr) -> Karbon celik yeterli olabilir
  |     |-- >9 (alkali) -> Karbon celik (dikkatli), SS, Ni alasimi
  |
  +-- Butce?
        |-- Sinirli -> CS + kaplama, SS 304/316L
        |-- Orta -> Duplex, Ti
        |-- Yuksek -> Hastelloy, Inconel, Ti
```

## Uygulama Adimlari

1. **Korozyon ortam analizi:** Akiskan bilesimi, pH, sicaklik, basinc, klorur/sulfur icerigi belirle
2. **Korozyon testi:** Gerekirse kupon testi ile aday malzemelerin korozyon hizini olc
3. **NACE/ASTM standart kontrolu:** Uygun malzeme standartlarini belirle (NACE MR0175, ASME BPVC)
4. **Maliyet-omur analizi:** LCC (Life Cycle Cost) hesabi ile malzeme seceneklerini karsilastir
5. **Tedarik ve inspeksiyon:** Malzeme sertifikalari (MTR), PMI (Positive Material Identification) testi
6. **Kaynak proseduru:** WPS/PQR hazirlama, kaynak malzemesi uyumu kontrol
7. **Devreye alma:** Pasivizasyon (paslanmaz celik icin), ilk doldurma proseduru
8. **Izleme:** Korozyon kupon programi, UT duvar kalinligi olcumu, online korozyon izleme

## İlgili Dosyalar

- Isi esanjoru exergy formulleri: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Kirlenme yonetimi: `heat_exchanger/solutions/fouling_management.md`
- Retrofit cozumleri: `heat_exchanger/solutions/retrofit.md`
- Govde-boru esanjor: `heat_exchanger/equipment/shell_and_tube.md`
- Plakali esanjor: `heat_exchanger/equipment/plate.md`
- Hava sogutmali esanjor: `heat_exchanger/equipment/air_cooled.md`
- Kazan besleme suyu aritma: `boiler/solutions/feedwater_treatment.md`

## Referanslar

- NACE International, "Corrosion Engineer's Reference Book," 4th Edition
- NACE MR0175 / ISO 15156, "Petroleum, Petrochemical and Natural Gas Industries — Materials for Use in H2S-Containing Environments"
- ASME Boiler and Pressure Vessel Code, Section VIII, Division 1 — Materials
- ASM Handbook, Volume 13A: "Corrosion: Fundamentals, Testing, and Protection"
- Schweitzer, P.A., "Corrosion Resistance Tables," 5th Edition, CRC Press
- Craig, B.D. and Anderson, D.B., "Handbook of Corrosion Data," ASM International
- TEMA, "Standards of the Tubular Exchanger Manufacturers Association," 10th Edition — Materials Section
- API 660, "Shell-and-Tube Heat Exchangers" — Materials Requirements
- Fontana, M.G., "Corrosion Engineering," 3rd Edition, McGraw-Hill
- Dillon, C.P., "Corrosion Resistance of Stainless Steels," Marcel Dekker
- IMI Titanium, "Titanium in Heat Exchangers — Application Guide"
- Haynes International, "Hastelloy C-276 Alloy — Corrosion Data Sheet"
