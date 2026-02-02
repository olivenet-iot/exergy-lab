---
title: "Mekanik Ön Su Alma (Mechanical Pre-Dewatering)"
category: dryer
equipment_type: dryer
keywords: [mekanik su alma, mechanical dewatering, presleme, santrifüj, filtrasyon, ön kurutma]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/solutions/exhaust_heat_recovery.md, dryer/sectors/paper_drying.md, dryer/sectors/food_drying.md]
use_when:
  - "Mekanik ön su alma yapılmıyor olduğunda"
  - "Kurutma enerji tüketimi çok yüksek olduğunda"
  - "Ürün nem içeriği >50% olduğunda"
priority: high
last_updated: 2026-02-01
---
# Mekanik Ön Su Alma (Mechanical Pre-Dewatering)

> Son güncelleme: 2026-02-01

## Genel Bakış

Endüstriyel kurutma proseslerinde en büyük enerji tüketim kalemi, suyun sıvı fazdan buhar fazına geçirilmesidir (thermal evaporation). Termal buharlaştırma, suyun gizli ısısı (latent heat) nedeniyle 2,500-4,000 kJ/kg su aralığında enerji gerektirir. Buna karşılık, aynı suyun mekanik yollarla (presleme, santrifüj, filtrasyon) uzaklaştırılması yalnızca 10-50 kJ/kg su enerji tüketir. Bu fark 50 ila 200 kata ulaşabilir.

**Temel prensip:** Suyun mekanik olarak uzaklaştırılması, termal buharlaştırma enerjisinin 1/5 ila 1/10'u kadar enerji tüketir. Bu nedenle ürünün tolere edebildiği her kilogram su, termal kurutucu öncesinde mekanik yollarla alınmalıdır.

**Pratik kural (Rule of Thumb):** Besleme neminde her %1'lik mekanik azalma, kurutucunun toplam enerji tüketimini %3-5 oranında düşürür. Bu kural, mekanik ön su almanın kurutma sistemlerindeki en yüksek getirili yatırımlardan biri olduğunu açıkça göstermektedir.

**Tipik Tasarruf:** %20-60 termal kurutucu enerji tüketiminde azalma (besleme nemine bağlı)
**Tipik ROI:** 0.5-2.0 yıl
**Öncelik:** Yüksek -- en iyi hızlı kazanımlardan (quick win) biri

## Tetikleyici (Trigger Conditions)

Bu çözüm aşağıdaki koşullardan biri veya birkaçı tespit edildiğinde uygulanmalıdır:

1. **Mekanik ön su alma yapılmıyor:** Ürün doğrudan yüksek nemle termal kurutucuya besleniyor. Termal kurutucu öncesinde herhangi bir pres, santrifüj veya filtre bulunmuyor.
2. **Besleme nem içeriği yüksek:** Kurutucuya giren ürünün yaş bazda nem içeriği >%50. Bu durumda suyun büyük kısmı serbest su (free water) olup mekanik olarak uzaklaştırılabilir.
3. **Kurutma enerji tüketimi aşırı yüksek:** SMER (Specific Moisture Extraction Rate) değeri beklenenin altında veya enerji maliyeti üretim maliyetinin önemli bir kısmını oluşturuyor.
4. **Kurutucu kapasite darboğazı:** Mevcut kurutucu talebi karşılayamıyor; mekanik ön su alma ile kurutucu yükü azaltılarak kapasite artışı sağlanabilir.
5. **Exergy verimi çok düşük:** Kurutucunun exergy verimi <%5 ve giren exergy'nin büyük kısmı buharlaştırma tersinmezliğinde yok ediliyor.

## Enerji Karşılaştırma (Energy Comparison)

### Mekanik vs Termal Su Uzaklaştırma

| Su Uzaklaştırma Yöntemi | Spesifik Enerji [kJ/kg su] | Spesifik Enerji [kWh/kg su] | Enerji Oranı |
|--------------------------|---------------------------|----------------------------|-------------|
| Termal buharlaştırma (konvektif, 100°C) | 2,500-3,500 | 0.70-1.00 | 1x (referans) |
| Termal buharlaştırma (vakum, 60°C) | 2,800-4,000 | 0.78-1.11 | 1.0-1.1x |
| Santrifüj (centrifuge) | 15-40 | 0.004-0.011 | 0.006-0.016x |
| Filtrasyon (vakum, basınçlı) | 10-30 | 0.003-0.008 | 0.004-0.012x |
| Presleme (screw, belt, roll press) | 5-20 | 0.001-0.006 | 0.002-0.008x |
| Osmotik su alma (osmotic dewatering) | ~0 (minimal) | ~0 | ~0x |

**Exergy perspektifi:** Termal buharlaştırmada yüksek kaliteli yakıt exergy'si (doğal gaz: ~52 MJ/kg kimyasal exergy) düşük kaliteli bir işlem için kullanılır. Mekanik su almada ise düşük miktarda elektrik (saf exergy) kullanılır. Exergy yıkımı açısından mekanik yol çok daha verimlidir.

### Neden Bu Kadar Büyük Fark Var?

Termal buharlaştırma faz değişimi gerektirir: suyun sıvı fazdan buhar fazına geçmesi için gizli ısı (latent heat) sağlanmalıdır. Mekanik su alma ise faz değişimi gerektirmez; su sıvı olarak kalır ve yalnızca fiziksel kuvvetlerle (basınç, merkezkaç, vakum) ürün matrisinden ayrıştırılır. Faz değişiminin olmaması, enerji gereksinimini dramatik şekilde düşürür.

## Teknolojiler (Technologies)

### 1. Filtrasyon (Filtration)

**Vakum filtre (Vacuum Filter):**
- Spesifik enerji: 10-20 kJ/kg su
- Çalışma prensibi: Filtre ortamı altında vakum uygulanarak su çekilir
- Kapasite: 5-200 t/h
- Uygun malzemeler: Mineral konsantre, nişasta, selüloz, kaolin
- Giriş nemi: %70-95, çıkış nemi: %50-75 (yaş bazda)

**Basınçlı filtre (Pressure Filter / Filter Press):**
- Spesifik enerji: 15-30 kJ/kg su
- Çalışma prensibi: Yüksek basınçlı (5-16 bar) filtrasyon ile su süzülür
- Kapasite: 1-50 t/h (genellikle batch)
- Uygun malzemeler: Pigment, kaolin, ilaç ara ürünleri, kimyasal çökelti
- Giriş nemi: %80-98, çıkış nemi: %40-65 (yaş bazda)

### 2. Santrifüj (Centrifugation)

**Dekantör santrifüj (Decanter Centrifuge):**
- Spesifik enerji: 20-40 kJ/kg su
- Çalışma prensibi: Sürekli merkezkaç kuvvetiyle (2,000-4,000 g) katı-sıvı ayrıştırma
- Kapasite: 1-120 t/h
- Uygun malzemeler: Atıksu çamuru, zeytin posası, bira mayası, kimyasal çökelti
- Giriş nemi: %85-99, çıkış nemi: %55-80 (yaş bazda)

**Sepet santrifüj (Basket Centrifuge):**
- Spesifik enerji: 15-35 kJ/kg su
- Çalışma prensibi: Delikli sepette merkezkaç kuvvetiyle su ayrıştırma
- Kapasite: 0.5-30 t/h (batch veya sürekli)
- Uygun malzemeler: Şeker kristali, tuz, plastik granül, tekstil
- Giriş nemi: %60-95, çıkış nemi: %40-70 (yaş bazda)

### 3. Presleme (Pressing)

**Vida presi (Screw Press):**
- Spesifik enerji: 5-15 kJ/kg su
- Çalışma prensibi: Dönen vida ile malzeme sıkıştırılarak su süzülür
- Kapasite: 1-50 t/h
- Uygun malzemeler: Meyve posası, pancar küspesi, ahşap talaşı, kağıt hamuru
- Giriş nemi: %60-90, çıkış nemi: %40-65 (yaş bazda)

**Bant presi (Belt Press):**
- Spesifik enerji: 5-15 kJ/kg su
- Çalışma prensibi: İki bant arasında kademeli sıkıştırma
- Kapasite: 5-100 t/h
- Uygun malzemeler: Atıksu çamuru, kağıt hamuru, endüstriyel çamur
- Giriş nemi: %85-99, çıkış nemi: %60-80 (yaş bazda)

**Vals presi (Roll Press):**
- Spesifik enerji: 8-20 kJ/kg su
- Çalışma prensibi: İki silindir arasında sıkıştırma
- Kapasite: 5-200 t/h
- Uygun malzemeler: Kağıt, tekstil, pelet hammaddesi
- Giriş nemi: %55-80, çıkış nemi: %35-60 (yaş bazda)

### 4. Osmotik Su Alma (Osmotic Dewatering)

- Spesifik enerji: Minimal (~0 kJ/kg su; yalnızca pompa ve karıştırma enerjisi)
- Çalışma prensibi: Ürün, yüksek konsantrasyonlu bir çözeltiye (tuz, şeker, poliol) batırılır; osmotik basınç farkı ile su çekilir
- Kapasite: 0.1-10 t/h
- Uygun malzemeler: Meyve, sebze, et (gıda sektörüne özgü)
- Giriş nemi: %80-95, çıkış nemi: %50-70 (yaş bazda)
- Sınırlama: Yalnızca gıda sektöründe uygulanabilir; çözelti yönetimi gerektirir

## Sektörel Uygulamalar (Application by Sector)

### Kağıt Sektörü (Paper Drying)

Kağıt üretiminde "pres bölümü" (press section) termal silindir kurutuculardan önce gelir. Modern kağıt makinelerinde çoklu nip pres ve shoe press teknolojisi ile kağıt hamuru nemi %55-60'dan %40-48'e düşürülür. Shoe press ile %38-42 yaş bazda neme ulaşılabilir. Pres bölümündeki her %1'lik ek nem azaltması, silindir kurutma bölümünün buhar tüketimini %3-4 oranında düşürür.

- **Tipik teknoloji:** Shoe press, nip press, extended nip press
- **Referans:** `dryer/sectors/paper_drying.md`

### Gıda Sektörü (Food Drying)

Meyve posası, sebze atıkları ve gıda yan ürünlerinin kurutulmasında vida presi (screw press) en yaygın mekanik ön su alma teknolojisidir. Osmotik su alma ise meyve ve sebze dilimlerinin kurutma öncesi nem azaltılmasında kullanılır. Gıda sektöründe hücre hasarı ve ürün kalitesi kritik kısıtlayıcı faktörlerdir.

- **Tipik teknoloji:** Vida presi, bant presi, osmotik su alma
- **Referans:** `dryer/sectors/food_drying.md`

### Çamur/Atıksu Sektörü (Sludge Drying)

Atıksu arıtma çamuru genellikle %96-99 nemle gelir. Dekantör santrifüj veya bant presi ile %70-80 yaş bazda neme düşürülür, ardından termal kurutucu ile hedef nem (%10-40) elde edilir. Mekanik ön su alma olmadan termal kurutma ekonomik olarak mümkün değildir.

- **Tipik teknoloji:** Dekantör santrifüj, bant presi, filtre presi
- **Katkı:** Polielektrolit flokülant dozajı ile mekanik su alma verimi artırılır

### Tekstil Sektörü (Textile Drying)

Tekstil boyama ve yıkama sonrası kumaş %60-80 yaş bazda nem içerir. Mangle (sıkma silindirleri) ile nem %40-55'e düşürülür. Santrifüj (hydro-extractor) ile iplik bobinlerinde nem %30-45'e indirilebilir. Kumaş hasarı önlemek için mangle basıncı dikkatle ayarlanmalıdır.

- **Tipik teknoloji:** Mangle (padder), santrifüj (hydro-extractor)
- **Referans:** `dryer/sectors/textile_drying.md`

## Hesaplama Örneği (Calculation Example)

### Senaryo: Bant kurutucu öncesi mekanik ön su alma

Bir gıda işleme tesisinde elma posası kurutulmaktadır. Mevcut durumda posa doğrudan bant kurutucuya beslenmektedir.

**Girdiler:**

| Parametre | Değer |
|-----------|-------|
| Yaş ürün debisi (besleme) | 2,000 kg/h |
| Giriş nemi (yaş bazda) | %70 |
| Mekanik su alma sonrası hedef nem | %50 (yaş bazda) |
| Kurutucu çıkış hedef nemi | %10 (yaş bazda) |
| Termal buharlaştırma spesifik enerjisi | 3,000 kJ/kg su |
| Vida presi spesifik enerjisi | 75 kJ/kg su |
| Yıllık çalışma süresi | 6,000 saat |
| Doğal gaz fiyatı | 0.045 EUR/kWh |
| Brülör verimi | %90 |

**Adım 1 -- Kuru madde debisi:**

```
m_dry = 2,000 x (1 - 70/100) = 600 kg kuru madde/saat
```

**Adım 2 -- Mevcut durum (mekanik su alma yok):**

```
X_db_in = 70 / (100 - 70) x 100 = %233.3 (kuru bazda)
X_db_final = 10 / (100 - 10) x 100 = %11.1 (kuru bazda)

Buharlaştırılacak su = 600 x (233.3 - 11.1) / 100 = 1,333.2 kg su/saat
Termal enerji = 1,333.2 x 3,000 / 3,600 = 1,111.0 kW
```

**Adım 3 -- Mekanik su alma sonrası (vida presi ile):**

```
Mekanik su alma sonrası yaş ürün kütlesi:
m_wet_after = 600 / (1 - 0.50) = 1,200 kg/h
Mekanik olarak uzaklaştırılan su = 2,000 - 1,200 = 800 kg su/saat

X_db_after = 50 / (100 - 50) x 100 = %100.0 (kuru bazda)

Buharlaştırılacak su = 600 x (100.0 - 11.1) / 100 = 533.4 kg su/saat
Termal enerji = 533.4 x 3,000 / 3,600 = 444.5 kW
```

**Adım 4 -- Tasarruf:**

```
Termal yük azalması = 1,111.0 - 444.5 = 666.5 kW (%60 azalma)
Buharlaştırılacak su azalması = 1,333.2 - 533.4 = 799.8 kg/h (%60 azalma)

Vida presi enerji tüketimi = 800 x 75 / 3,600 = 16.7 kW
Net enerji tasarrufu = 666.5 - 16.7 = 649.8 kW
```

**Sonuç:** Besleme neminin %70'den %50'ye mekanik olarak düşürülmesi, kurutucunun termal yükünü %60 oranında azaltmaktadır. Vida presi tüketimi (16.7 kW) tasarrufa kıyasla ihmal edilebilir düzeydedir. Exergy açısından, yüksek kaliteli yakıt exergy'si yerine düşük miktarda mekanik exergy kullanılması büyük bir iyileşmedir.

### Farklı Nem Senaryoları

| Başlangıç Nemi | Mekanik Su Alma Sonrası | Hedef Son Nem | Termal Yük Azalması [%] |
|-----------------|-------------------------|---------------|------------------------|
| %80 | %60 | %10 | 52 |
| %80 | %50 | %10 | 68 |
| %70 | %50 | %10 | 60 |
| %70 | %55 | %10 | 44 |
| %60 | %45 | %10 | 42 |
| %60 | %40 | %10 | 52 |
| %90 | %70 | %10 | 50 |
| %90 | %60 | %10 | 66 |

## Ekonomik Analiz (Economic Analysis)

### Yatırım Maliyeti

| Teknoloji | Kapasite | Yatırım Maliyeti | Elektrik Tüketimi | Not |
|-----------|----------|-------------------|-------------------|-----|
| Vida presi (Screw press) | 1-5 t/h | EUR 10,000-40,000 | 5-20 kW | Kompakt, sürekli |
| Vida presi (Screw press) | 5-20 t/h | EUR 40,000-100,000 | 20-55 kW | Büyük endüstriyel |
| Bant presi (Belt press) | 5-20 t/h | EUR 30,000-70,000 | 10-30 kW | Geniş yüzey, sürekli |
| Bant presi (Belt press) | 20-50 t/h | EUR 70,000-120,000 | 25-60 kW | Çok büyük tesis |
| Dekantör santrifüj | 1-10 t/h | EUR 25,000-70,000 | 15-45 kW | Yüksek g-kuvveti |
| Dekantör santrifüj | 10-50 t/h | EUR 70,000-130,000 | 40-110 kW | Büyük endüstriyel |
| Vakum filtre | 5-30 t/h | EUR 40,000-100,000 | 20-50 kW | Mineral işleme |
| Filtre presi | 1-10 t/h (batch) | EUR 20,000-60,000 | 10-30 kW | Yüksek basınç |

**Not:** Maliyetler ekipman, montaj, boru tesisatı, elektrik bağlantısı ve devreye alma dahildir. Genel aralık: EUR 10,000-100,000.

### Geri Ödeme Süresi (Simple Payback Period)

Yukarıdaki hesaplama örneğine devam ederek:

```
Vida presi yatırımı (10 t/h sınıfı): EUR 55,000
Yıllık bakım maliyeti: EUR 4,000/yıl
Vida presi elektrik maliyeti: 16.7 kW x 6,000 h x 0.12 EUR/kWh = EUR 12,024/yıl

Yıllık termal enerji tasarrufu:
  649.8 kW x 6,000 h = 3,898,800 kWh/yıl
  Yakıt tasarrufu = 3,898,800 / 0.90 (brülör verimi) = 4,332,000 kWh yakıt
  Maliyet tasarrufu = 4,332,000 x 0.045 = EUR 194,940/yıl

Net yıllık tasarruf = 194,940 - 12,024 - 4,000 = EUR 178,916/yıl
Geri ödeme süresi = 55,000 / 178,916 = 0.31 yıl (yaklaşık 4 ay)
```

**Tipik SPP aralığı:** 0.5-2.0 yıl. Bu, endüstriyel enerji verimliliği yatırımlarında en hızlı geri dönüş sağlayan uygulamalardan biridir.

### Ek Fayda: Kapasite Artışı

Mekanik su alma, kurutucu termal yükünü azaltarak mevcut kurutucunun üretim kapasitesini artırır. Yukarıdaki örnekte kurutucu yükü %60 azaldığı için aynı kurutucu ile %60 daha fazla ürün işlenebilir veya kurutucu boyutu küçültülebilir.

## Sınırlamalar (Limitations)

### Ürün Kalitesi Kısıtları

- **Hücre hasarı (Cell Damage):** Gıda sektöründe mekanik basınç hücre yapısını bozabilir, doku kaybına ve renk/aroma değişimine yol açabilir. Meyve ve sebze dilimlerinde özellikle kritiktir.
- **Partikül boyutu/şekli:** Mekanik presleme ürünün partikül boyutunu veya morfolojisini değiştirebilir. Granüler ürünlerde ezilme riski vardır.
- **Bağlı su (Bound Water):** Mekanik yöntemler yalnızca serbest suyu (free water) uzaklaştırabilir. Bağlı su (hücre içi su, adsorbe su, kapiler su) mekanik olarak alınamaz. Kritik nem içeriği (critical moisture content) altına mekanik yollarla inilemez.

### Malzeme Kısıtları

- **Abrazif malzemeler:** Mineral, kum veya sert parçacık içeren malzemeler ekipman aşınmasını hızlandırır.
- **Yapışkan malzemeler:** Filtre yüzeylerini ve vida kanallarını tıkayabilir.
- **Mevsimsel değişim:** Tarımsal ürünlerde mevsime göre nem içeriği ve reolojik özellikler değişir.

### Proses Kısıtları

- **Ulaşılabilir nem sınırı:** Her malzeme ve teknoloji kombinasyonu için ulaşılabilir minimum nem seviyesi farklıdır. Genellikle yaş bazda %35-55 altına mekanik olarak inilemez.
- **Hijyen gereksinimleri:** Gıda ve ilaç sektöründe CIP (Clean-In-Place) uyumlu tasarım ve paslanmaz çelik (AISI 304/316) malzeme gereklidir.
- **Filtrat yönetimi:** Mekanik su alma ile çıkan sıvı (filtrat) çözünmüş maddeler veya ince parçacıklar içerebilir; arıtma veya geri dönüşüm sistemi gerektirir.

## Uygulama Adımları (Implementation Steps)

1. **Malzeme karakterizasyonu:** Ürünün nem içeriğini (yaş ve kuru bazda), partikül boyutunu, sıkıştırılabilirliğini (compressibility), filtrasyon direncini (specific resistance to filtration) ve reolojik özelliklerini belirle.
2. **Laboratuvar testi:** Farklı mekanik su alma yöntemlerini (vida presi, santrifüj, filtre presi) laboratuvar ölçeğinde test et. Her teknoloji ile ulaşılabilir minimum nem içeriğini ve ürün kalitesine etkisini belirle.
3. **Teknoloji seçimi:** Test sonuçlarına, kapasite ihtiyacına, sürekli/kesikli çalışma gereksinimine, mevcut tesis alanına ve hijyen standartlarına göre en uygun teknolojiyi seç.
4. **Ekipman boyutlandırma:** Üretim kapasitesine, pik yük koşullarına ve gelecekteki genişleme planlarına göre ekipmanı boyutlandır. En az %20 güvenlik payı bırak.
5. **Proses entegrasyonu:** Mekanik su alma ekipmanını mevcut üretim hattına entegre et. Konveyör, besleme hunisi, pompa ve boru bağlantılarını tasarla. Kurutucu besleme sistemiyle uyumu sağla.
6. **Sıvı yönetimi:** Filtrat veya santrifüj sıvısının toplanması, arıtılması veya geri dönüşümü için sistem kur. Atıksu deşarj mevzuatına uyumu sağla.
7. **Elektrik ve kontrol:** Motor, VFD (Variable Frequency Drive), PLC, sensörler (basınç, debi, nem) ve HMI kurulumu için elektrik projesini hazırla.
8. **Montaj ve devreye alma:** Temeli hazırla, ekipmanı yerleştir, mekanik ve elektrik bağlantılarını tamamla. Farklı ürün nemleri ve debilerle test ederek optimum çalışma parametrelerini belirle.
9. **Performans doğrulama:** En az 1 ay boyunca giriş nemi, çıkış nemi, enerji tüketimi ve kurutucu performansını ölç. Beklenen tasarrufları M&V (Measurement and Verification) ile doğrula.
10. **Bakım programı:** Aşınma parçaları (filtre bezi, vida segmentleri, santrifüj başlığı), yağlama noktaları ve temizlik periyotları için bakım planı oluştur. Yıllık bakım bütçesini yatırım maliyetinin %5-8'i olarak planla.

## İlgili Dosyalar

- Kurutucu exergy formülleri: `dryer/formulas.md`
- Kurutucu performans karşılaştırma: `dryer/benchmarks.md`
- Egzoz ısı geri kazanımı: `dryer/solutions/exhaust_heat_recovery.md`
- Kağıt sektörü kurutma: `dryer/sectors/paper_drying.md`
- Gıda sektörü kurutma: `dryer/sectors/food_drying.md`
- Hava geri deviri: `dryer/solutions/air_recirculation.md`
- Isı pompası retrofit: `dryer/solutions/heat_pump_retrofit.md`
- Fabrika çapraz ekipman fırsatları: `factory/cross_equipment.md`

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014 -- Mechanical Dewatering Chapter
- Kemp, I.C., "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4: Energy Savings, Wiley-VCH, 2012
- European Commission, "Reference Document on Best Available Techniques in the Food, Drink and Milk Industries (FDM BREF)," JRC, 2019
- European Commission, "Reference Document on Best Available Techniques for the Pulp and Paper Industry (PP BREF)," JRC, 2015
- US DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry," 3rd Edition
- Wakeman, R.J. & Tarleton, E.S., "Solid/Liquid Separation: Principles of Industrial Filtration," Elsevier, 2005
- Leung, W.W-F., "Industrial Centrifugation Technology," McGraw-Hill, 1998
- Perry's Chemical Engineers' Handbook, 9th Edition -- Section 18: Liquid-Solid Operations and Equipment
- Kudra, T. & Mujumdar, A.S., "Advanced Drying Technologies," 2nd Edition, CRC Press, 2009
- Svarovsky, L., "Solid-Liquid Separation," 4th Edition, Butterworth-Heinemann, 2000
