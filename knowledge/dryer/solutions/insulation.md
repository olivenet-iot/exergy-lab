---
title: "Yalıtım İyileştirmesi (Dryer Insulation Improvement)"
category: dryer
equipment_type: dryer
keywords: [yalıtım, insulation, radyasyon kaybı, iletim kaybı, yüzey sıcaklığı]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/audit.md, dryer/equipment/tunnel_dryer.md, dryer/equipment/rotary_dryer.md]
use_when: ["Radyasyon/iletim kayıpları yüksek olduğunda", "Kurutucu yüzey sıcaklığı ortam + 60°C üzerinde olduğunda"]
priority: medium
last_updated: 2026-02-01
---
# Yalıtım İyileştirmesi (Dryer Insulation Improvement)

> Son güncelleme: 2026-02-01

## Genel Bakis

Endustriyel kurutucularda govde, kanal, kapi ve vana gibi sicak yuzeylerden radyasyon ve iletim (conduction) yoluyla onemli miktarda isi kaybi olusur. Yetersiz veya hasarli yalitim, toplam enerji tuketiminin %5-15'ine varan kayiplara neden olabilir. Yalitim iyilestirmesi, dusuk yatirim maliyeti ve kisa geri odeme suresiyle en etkili enerji verimliligi onlemlerinden biridir.

**Problem:** Kurutucu yuzey sicakligi ortam sicakliginin 60°C uzerinde oldugunda konveksiyon ve radyasyon kayiplari hizla artar. Ozellikle donel (rotary) ve tunel kurutucularda genis govde yuzey alanlari nedeniyle kayiplar buyuk boyutlara ulasir.

**Cozum:** Uygun yalitim malzemesi ile kurutucu govdesinin, sicak hava kanallarinin, kapilar ve baglanti noktalarinin izole edilmesi; vana ve flanslarda sokulebilir yalitim ceketleri kullanilmasi.

**Tipik Tasarruf:** Toplam kurutucu enerjisinin %3-8'i
**Tipik Geri Odeme Suresi (SPP):** 0.5-2.0 yil

## Tetikleyici (Trigger Conditions)

Asagidaki kosullardan biri veya birden fazlasi tespit edildiginde yalitim iyilestirmesi degerlendirmeye alinmalidir:

| Kriter | Esik Deger | Aciklama |
|--------|------------|----------|
| Yuzey sicakligi | T_surface > T_ambient + 60°C | IR termografi ile tespit; acil mudahale gerektirir |
| Radyasyon/iletim kayiplari | > %8 toplam enerji girdisi | Enerji denetiminde hesaplanan toplam yuzey kaybi orani |
| Gorunur yalitim hasari | Gorunur hasar mevcut | Yirtik, ezik, dusmis veya islak yalitim |
| Yalitim yasi | > 15 yil | Performans dususu ve mekanik bozulma beklenir |
| Isi kaybi yogunlugu | > 500 W/m² | Yuksek oncelikli sicak noktalar (hot spots) |

### Uygulama Sinir Kosullari

Yalitim iyilestirmesi uygulanmamalidir:
- Dusuk sicaklikli kurutucularda (<50°C calisma sicakligi) — tasarruf potansiyeli dusuk
- Kasitli isi yayma gereken yuzeyler (radyatif kurutma zonlari)
- Yalitim zaten optimum kalinlikta ve iyi durumda ise

## Isi Kaybi Hesaplama (Heat Loss Calculation)

Yalitimisiz sicak yuzeylerden toplam isi kaybi, konveksiyon ve radyasyon bilesenlerinin toplamidir:

### Toplam Isi Kaybi Formulu

```
Q_loss = Q_convection + Q_radiation

Q_convection = h x A x (T_surface - T_ambient)

Q_radiation = epsilon x sigma x A x (T_s^4 - T_a^4)

Burada:
  Q_loss      = Toplam isi kaybi [W]
  h           = Konvektif isi transfer katsayisi [W/(m^2.K)]
                Dogal konveksiyon (natural convection): h = 5-10 W/(m^2.K)
                Hafif hava akimi olan ortam: h = 10-15 W/(m^2.K)
                Dis ortam (ruzgarli): h = 15-30 W/(m^2.K)
  A           = Yuzey alani [m^2]
  T_surface   = Yuzey sicakligi [K]
  T_ambient   = Ortam sicakligi [K]
  epsilon     = Yayinim katsayisi (emissivity) [-]
  sigma       = Stefan-Boltzmann sabiti = 5.67 x 10^-8 W/(m^2.K^4)
```

### Yuzey Yayinim Katsayilari (Emissivity Values)

| Yuzey Tipi | Yayinim Katsayisi (epsilon) |
|------------|----------------------------|
| Parlak metal (polished metal) | 0.10-0.30 |
| Oksitlenmis metal (oxidized metal) | 0.60-0.80 |
| Boyali yuzey / pasli celik (painted/rusted) | 0.85-0.95 |
| Aluminyum kaplama (aluminum cladding) | 0.05-0.15 |

### Silindirik Yuzey Alani Hesabi

Donel kurutucular ve boru hatlari icin:
```
A = pi x D x L

Burada:
  D = Dis cap [m]
  L = Uzunluk [m]
```

## Yalitim Malzemeleri (Insulation Materials)

| Malzeme | Maks. Sicaklik [°C] | Isil Iletkenlik lambda [W/(m.K)] | Maliyet [EUR/m^2] | Avantaj | Dezavantaj |
|---------|---------------------|----------------------------------|-------------------|---------|------------|
| Mineral yun (Mineral wool) | 700 | 0.035-0.045 | 20-50 | Ekonomik, kolay uygulama, yaygin | Nem hassasiyeti, ezilme riski |
| Seramik elyaf (Ceramic fiber) | 1200 | 0.040-0.060 | 30-70 | Hafif, cok yuksek sicaklik | Saglik riski (elyaf solunumu) |
| Kalsiyum silikat (Calcium silicate) | 1000 | 0.050-0.070 | 40-80 | Mekanik dayanim, nem direnci | Agir, kirilgan |
| Aerojel yalitim (Aerogel insulation) | 650 | 0.015-0.025 | 100-250 | Ultra ince, en dusuk iletkenlik | Cok pahali |

### Malzeme Secim Rehberi

- **80-200°C calisma sicakligi:** Mineral yun en uygun ve ekonomik secimdir
- **200-700°C calisma sicakligi:** Mineral yun veya kalsiyum silikat
- **700-1200°C calisma sicakligi:** Seramik elyaf zorunlu
- **Alan kisitli bolgeler:** Aerojel yalitim (ince kalinlikta yuksek performans)
- **Mekanik darbe riski olan bolgeler:** Kalsiyum silikat + aluminyum kaplama

## Optimum Kalinlik (Economic Thickness Analysis)

Optimum yalitim kalinligi, yalitim maliyeti ile enerji tasarrufu arasindaki dengeyi arar. Kalinlik arttikca isi kaybi azalir ancak yalitim maliyeti artar. **Ekonomik kalinlik**, toplam maliyetin minimum oldugu noktadir.

```
Toplam_maliyet(t) = Yalitim_yatirimi(t) + SUM [Isi_kaybi(t) x Enerji_fiyati x Calisma_saati] / (1+r)^n

Burada:
  t = Yalitim kalinligi [mm]
  r = Iskonto orani [%]
  n = Degerlendirme suresi [yil]
```

### Pratik Ekonomik Kalinlik Degerleri (Mineral Yun)

| Calisma Sicakligi [°C] | Mineral Yun [mm] | Kalsiyum Silikat [mm] | Seramik Elyaf [mm] |
|------------------------|-------------------|----------------------|---------------------|
| 80-120 | 50-80 | 40-60 | -- |
| 120-200 | 80-100 | 60-80 | 50-80 |
| 200-300 | 100-150 | 80-120 | 80-100 |
| 300-500 | 150-200 | 120-150 | 100-120 |

**Not:** Degerler EUR 0.06/kWh dogalgaz fiyati, 5,000 saat/yil calisma ve 10 yil degerlendirme suresi icin hesaplanmistir.

## Hesaplama Ornegi (Calculation Example)

**Senaryo:** Donel kurutucu (rotary dryer), 3 m cap, 10 m uzunluk, yuzey sicakligi 120°C, ortam sicakligi 20°C, oksitlenmis celik govde (epsilon = 0.80), dogal konveksiyon (h = 8 W/(m^2.K))

### Adim 1: Yuzey Alani Hesabi

```
A = pi x D x L = 3.14159 x 3 x 10 = 94.25 m^2
```

### Adim 2: Yalitim Oncesi Isi Kaybi (Before Insulation)

```
Sicakliklar (Kelvin):
T_surface = 120 + 273 = 393 K
T_ambient = 20 + 273 = 293 K

Q_convection = h x A x (T_surface - T_ambient)
             = 8 x 94.25 x (120 - 20)
             = 8 x 94.25 x 100
             = 75,400 W = 75.4 kW

Q_radiation = epsilon x sigma x A x (T_s^4 - T_a^4)
            = 0.80 x 5.67x10^-8 x 94.25 x (393^4 - 293^4)
            = 0.80 x 5.67x10^-8 x 94.25 x (2.386x10^10 - 7.370x10^9)
            = 0.80 x 5.67x10^-8 x 94.25 x 1.649x10^10
            = 70,550 W = 70.6 kW

Q_loss_toplam = 75.4 + 70.6 = 146.0 kW
```

### Adim 3: Yalitim Sonrasi Isi Kaybi (After 100 mm Mineral Wool)

100 mm mineral yun yalitim uygulandiginda yuzey sicakligi ortam uzerinde yaklasik 30°C'ye duser:

```
T_surface_new = 50°C = 323 K

Q_convection_new = 8 x 94.25 x (50 - 20)
                 = 8 x 94.25 x 30
                 = 22,620 W = 22.6 kW

Q_radiation_new = 0.80 x 5.67x10^-8 x 94.25 x (323^4 - 293^4)
                = 0.80 x 5.67x10^-8 x 94.25 x (1.088x10^10 - 7.370x10^9)
                = 0.80 x 5.67x10^-8 x 94.25 x 3.510x10^9
                = 12,650 W = 12.7 kW

Q_loss_new = 22.6 + 12.7 = 35.3 kW
```

### Adim 4: Tasarruf Hesabi

```
Tasarruf = Q_loss_oncesi - Q_loss_sonrasi
         = 146.0 - 35.3 = 110.7 kW (%75.8 azalma)

Yillik enerji tasarrufu (5,000 saat/yil):
E_tasarruf = 110.7 x 5,000 = 553,500 kWh/yil

Dogalgaz karsiligi (kazan verimi %90):
Gaz_tasarrufu = 553,500 / 0.90 = 615,000 kWh/yil

Parasal tasarruf (dogalgaz EUR 0.06/kWh):
Yillik_tasarruf = 615,000 x 0.06 = EUR 36,900/yil
```

## Pratik Cozumler (Practical Solutions)

### Sokulebilir Yalitim Ceketleri (Removable Insulation Jackets)

Vanalar, flanslar ve duzenli bakim gereken noktalar icin ideal cozumdur:

| Bilesen | Ceket Maliyeti [EUR/adet] | Tasarruf [EUR/yil/adet] | Geri Odeme |
|---------|--------------------------|------------------------|------------|
| DN50 vana | 80-150 | 60-120 | 0.7-2.5 yil |
| DN100 vana | 150-300 | 120-250 | 0.6-2.0 yil |
| DN150 flans | 100-200 | 80-180 | 0.6-2.0 yil |
| Filtre govdesi | 300-800 | 200-600 | 0.5-2.0 yil |

**Ozellikler:**
- Ic katman: Yuksek sicaklik silikon kumas + mineral yun dolgu
- Dis katman: Su gecirmez kumas
- Baglama: Paslanmaz celik tokali kayislar veya Velcro bantlar
- Sokme/takma suresi: 1-5 dakika
- Omur: 5-10 yil (tekrar tekrar kullanilabilir)

### Spreyle Uygulanan Yalitim (Spray-On Insulation)

Karmasik geometrili yuzeyler, dirsekler, reduksiyonlar ve standart yalitim uygulanamayan bolgeler icin:

- **Seramik boya yalitim (Ceramic paint coating):** 0.5-2 mm kalinlikta uygulanir. Dusuk isi iletkenligine sahip seramik mikro kurecikler icerir. Tam yalitim yerine ek koruma olarak degerlendirilmelidir
- **Poliuretan kopuk (PU foam spray):** Dusuk sicaklik (<100°C) uygulamalari icin. Mukemmel yapiskanligi sayesinde karmasik sekillere uygulanabilir
- **Yuksek sicaklik seramik kaplama:** 300°C'ye kadar uygulamalar icin ozel formule edilmis sprey yalitim

## Ekonomik Analiz (Economic Analysis)

### Toplam Proje Maliyeti

| Kurutucu Boyutu | Yalitim Alani [m^2] | Malzeme [EUR] | Iscilik [EUR] | Toplam Yatirim [EUR] |
|----------------|---------------------|--------------|--------------|---------------------|
| Kucuk (<50 kW) | 10-30 | 1,000-3,000 | 1,000-2,000 | 2,000-5,000 |
| Orta (50-200 kW) | 30-80 | 3,000-8,000 | 2,000-5,000 | 5,000-13,000 |
| Buyuk (>200 kW) | 80-200 | 8,000-20,000 | 5,000-10,000 | 13,000-30,000 |

### Tipik Yatirim Getirisi

| Parametre | Deger |
|-----------|-------|
| Yatirim araligi | EUR 5,000-30,000 |
| Basit geri odeme suresi (SPP) | 0.5-2.0 yil |
| Tipik enerji tasarrufu | %3-8 toplam kurutucu enerjisi |
| Yillik CO2 azaltimi | 30-180 ton CO2/yil (dogalgaz bazli) |
| Yalitim omru | 15-25 yil (duzenli bakimla) |

### Ornekteki Donel Kurutucu icin ROI

```
Yatirim: 94.25 m^2 x EUR 55/m^2 (mineral yun + iscilik) = EUR 5,184
         + kaplama ve yan giderler = EUR 7,000 toplam

Yillik tasarruf: EUR 36,900/yil
Geri odeme = 7,000 / 36,900 = 0.19 yil = 2.3 ay
```

## Termal Goruntuleme (Thermal Imaging)

Infrared (IR) kamera ile termal tarama, yalitim iyilestirme projelerinin temel adimidir:

### Termal Tarama Protokolu

1. **Zamanlama:** Kurutucu en az 2 saat surekli calistiktan sonra (termal denge) olcum yapilmalidir
2. **Ortam kosullari:** Ic mekanda olcum tercihen sabah erken saatlerde; dis yuzey olcumleri bulutlu havada veya gunes almayan taraftan
3. **Ruzgar etkisi:** Dis ortamda ruzgar konveksiyon katsayisini arttirir; olcum ve hesapta dikkate alinmalidir
4. **Kamera ayarlari:** Yuzey yayinim katsayisi (emissivity) dogru ayarlanmalidir; boyali celik icin epsilon = 0.90-0.95
5. **Referans noktasi:** Bilinen sicaklikta bir referans yuzey ile kalibrasyon dogrulanmalidir

### Degerlendirme Kriterleri

| Yuzey Sicakligi (Ortam Uzeri) | Durum | Renk Kodu | Aksiyon |
|-------------------------------|-------|-----------|---------|
| < 30°C | Iyi (Good) | Yesil | Izlemeye devam |
| 30-60°C | Kabul edilebilir (Acceptable) | Sari | Planli iyilestirme |
| > 60°C | Kotu (Poor) | Kirmizi | Acil mudahale gerekli |
| > 100°C | Kritik (Critical) | Mor | Derhal is guvenligi ve yalitim mudahalesi |

### Termal Tarama Raporlama

Her sıcak nokta icin asagidaki bilgiler raporlanmalidir:
- Konum (kurutucu bolge, kanal, vana vb.)
- Olculen yuzey sicakligi [°C]
- Tahmini yuzey alani [m^2]
- Hesaplanan isi kaybi [kW]
- Onerilen yalitim tipi ve kalinligi
- Tahmini tasarruf [EUR/yil]

## Uygulama Adimlari (Implementation Steps)

1. **IR termografi taramasi:** Kurutucu calisirken tum yuzeylerin infrared kamera ile taranmasi; sicak noktalarin ve yalitim hasarlarinin belirlenmesi
2. **Yuzey envanteri:** Yalitim gereken tum yuzeylerin (govde, kanal, kapi, vana, flans) alanlarinin ve sicakliklarinin kaydedilmesi
3. **Isi kaybi hesabi:** Mevcut durumda konveksiyon ve radyasyon kayiplarinin hesaplanmasi (yukaridaki formuller ile)
4. **Malzeme secimi:** Calisma sicakligina, mekanik gereksinimlere ve butceye uygun yalitim malzemesinin secimi
5. **Ekonomik kalinlik hesabi:** Optimum yalitim kalinliginin belirlenmesi (yalitim maliyeti vs enerji tasarrufu dengesi)
6. **Kapi contalarinin kontrolu:** Mevcut contalarin durumunun degerlendirilmesi ve gerekirse yenilenmesi
7. **Sokulebilir ceket tasarimi:** Bakim erisimi gereken noktalar icin sokulebilir yalitim ceketlerinin tasarimi
8. **Tedarik ve teklif:** Minimum 3 tedarikciden teklif alinmasi
9. **Uygulama:** Yalitim montaji (genellikle 2-5 gun, planli durusta)
10. **Dogrulama:** Yalitim sonrasi IR termografi ile yuzey sicakliklarinin kontrolu ve tasarrufun dogrulanmasi
11. **Periyodik kontrol programi:** Yilda 1-2 kez IR termografi ile yalitim durumunun izlenmesi

## Riskler (Risks and Considerations)

| Risk | Aciklama | Onlem |
|------|----------|-------|
| Mekanik hasar | Yalitim darbelerle zarar gorebilir | Koruyucu aluminyum veya celik kaplama kullanilmasi |
| Nem girisi | Islanan yalitim performansini kaybeder | Su gecirmez buhar bariyeri ve kaplama uygulanmasi |
| Yuksek sicaklik | Yanlis malzeme secimi yangin riski yaratir | Malzeme sicaklik sinifinin kontrol edilmesi |
| Korozyon (CUI) | Yalitim altinda korozyon (Corrosion Under Insulation) olusabilir | Uygun kaplama, buhar bariyeri ve havalandirma |
| Bakim erisimi | Sabit yalitim bakimi zorlastirir | Bakim noktalarinda sokulebilir ceket kullanilmasi |
| Asiri yalitim | Cok kalin yalitim maliyet-etkin olmayabilir | Ekonomik kalinlik hesabi yapilmasi |
| Kapi contasi | Contalar zamanla sertlesir ve sizdirir | 6 ayda bir conta kontrolu, yillik degisim plani |
| Is guvenligi | Yalitimsiz sicak yuzey yanik riski | OSHA/ISG kurallarina uygun yuzey sicakligi (<60°C) |
| Elyaf solunumu | Seramik elyaf saglik riski tasir | Montaj sirasinda kisisel koruyucu ekipman (KKE) kullanimi |
| Buhar bariyeri | Dusuk sicaklikli kurutucularda yogusma olusabilir | <100°C uygulamalarda buhar bariyeri uygulanmasi |

## İlgili Dosyalar

- Kurutucu exergy formulleri: `dryer/formulas.md`
- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Kurutucu enerji denetimi: `dryer/audit.md`
- Tunel kurutucu ekipmani: `dryer/equipment/tunnel_dryer.md`
- Donel kurutucu ekipmani: `dryer/equipment/rotary_dryer.md`
- Sicaklik optimizasyonu: `dryer/solutions/temperature_optimization.md`
- Egzoz gazi geri kazanimi: `dryer/solutions/exhaust_heat_recovery.md`
- Fabrika atik isi geri kazanimi: `factory/waste_heat_recovery.md`

## Referanslar

- CINI (Committee for Industrial Insulation), "CINI Insulation Manual — Insulation Standards for Industrial Installations"
- US DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry," 3rd Edition
- EU BREF, "Reference Document on Best Available Techniques for Energy Efficiency," European IPPC Bureau
- Carbon Trust, "Insulation — Practical Guide to Saving Energy in Industry," CTG064
- VDI 2055, "Thermal Insulation for Heated and Refrigerated Industrial and Domestic Installations"
- ASTM C680, "Standard Practice for Estimate of Heat Gain or Loss and Surface Temperatures of Insulated Systems"
- BS 5422:2009, "Method for Specifying Thermal Insulating Materials on Pipes, Ductwork and Equipment"
- European Industrial Insulation Foundation (EiiF), "TIPCHECK — Technical Insulation Performance Check"
- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press
- DOE 3EPlus, "Insulation Thickness Computer Program" — ekonomik kalinlik hesap araci
