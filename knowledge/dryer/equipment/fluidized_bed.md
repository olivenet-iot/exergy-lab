---
title: "Akışkan Yataklı Kurutucu (Fluidized Bed Dryer)"
category: dryer
equipment_type: dryer
keywords:
  - akışkan yatak
  - fluidized bed
  - FBD
  - partikül kurutma
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/temperature_optimization.md
  - dryer/sectors/food_drying.md
use_when:
  - "Akışkan yataklı kurutucu analiz edilirken"
priority: medium
last_updated: 2026-02-01
---

# Akışkan Yataklı Kurutucu (Fluidized Bed Dryer)

## Genel Bakış

Akışkan yataklı kurutucu (fluidized bed dryer — FBD), granül veya partikül halindeki malzemenin alttan üflenen sıcak hava ile askıya alınarak (fluidize edilerek) kurutulduğu endüstriyel bir kurutma sistemidir. Hava hızı, parçacıkların ağırlığını dengeleyecek seviyeye çıkarılır ve parçacıklar sıvı benzeri bir davranış gösterir (fluidization). Bu sayede mükemmel ısı ve kütle transferi sağlanır; her bir parçacık homojen olarak sıcak hava ile temas eder.

FBD, ilaç (pharmaceuticals), kimya (chemicals), gıda granülleri (food granules) ve mineral işleme sektörlerinde yaygın olarak kullanılır. Kompakt yapısı, yüksek ısı transfer katsayısı ve homojen kurutma kabiliyeti ile öne çıkar. Bununla birlikte, parçacık boyutu sınırlaması, aşınma (attrition) ve yüksek basınç düşümü nedeniyle artan fan gücü tüketimi, tasarım ve işletmede dikkat gerektiren konulardır.

### Temel Operasyonel Parametreler

| Parametre | Değer Aralığı | Birim |
|-----------|---------------|-------|
| Giriş hava sıcaklığı (T_air_in) | 40 - 200 | °C |
| Parçacık boyutu aralığı | 50 µm - 10 mm | - |
| Kapasite | 100 - 20.000 | kg/h |
| Yatak derinliği (bed depth) | 0,1 - 0,6 | m |
| Akışkanlaşma hızı (fluidization velocity) | 0,3 - 5 | m/s |
| Yatak basınç düşümü (bed pressure drop) | 2.000 - 12.000 | Pa |
| Exergy verimi (tipik) | 8 - 18 | % |
| SMER (tipik) | 0,5 - 1,5 | kg/kWh |
| Enerji verimi (birinci yasa) | 50 - 65 | % |

---

## Çalışma Prensibi

Akışkan yataklı kurutucunun çalışma prensibi aşağıdaki temel adımlara dayanır:

1. **Hava hazırlama (air preparation):** Ortam havası filtrelenir ve ısıtıcıdan (buhar serpantini, doğalgaz brülörü veya elektrik rezistansı) geçirilerek istenen sıcaklığa getirilir.
2. **Dağılım plakası (distributor plate):** Isıtılan hava, delikli veya gözenekli bir plaka üzerinden eşit şekilde dağıtılarak yatak tabanına yönlendirilir. Plaka, hava dağılımının homojenliğini sağlayan kritik bir bileşendir.
3. **Akışkanlaşma (fluidization):** Hava hızı minimum akışkanlaşma hızını (U_mf) aştığında parçacıklar askıya alınır ve yatak genişler. Parçacıklar, sıvı gibi hareket etmeye başlar.
4. **Isı ve kütle transferi (heat and mass transfer):** Sıcak hava, her bir parçacığı çevreleyerek yüzeyden nemi buharlaştırır. Parçacık-hava temas alanı çok büyük olduğundan, konvektif ısı transfer katsayısı yüksektir (tipik: 100 - 400 W/m².K).
5. **Nem uzaklaşması (moisture removal):** Buharlaşan nem, egzoz havası ile birlikte sistemden çıkar. Egzoz havası genellikle siklon veya torba filtreden geçirilerek ince parçacıklar tutulur.
6. **Ürün çıkışı:** Kurutulan malzeme sürekli (continuous) sistemlerde taşma savağından (overflow weir) boşaltılır; kesikli (batch) sistemlerde ise yerinde kalır ve süre sonunda boşaltılır.

### Minimum Akışkanlaşma Hızı (U_mf)

Ergun denklemi ile hesaplanır:

```
U_mf = (d_p² x (rho_p - rho_g) x g) / (150 x mu) x (epsilon_mf³ / (1 - epsilon_mf))

Burada:
- d_p: Parçacık çapı (m)
- rho_p: Parçacık yoğunluğu (kg/m³)
- rho_g: Gaz yoğunluğu (kg/m³)
- mu: Gaz dinamik viskozitesi (Pa.s)
- epsilon_mf: Minimum akışkanlaşma porozitesi (~0,4-0,5)
- g: Yerçekimi ivmesi = 9,81 m/s²
```

**Optimum çalışma noktası:** Kabarcıklı akışkanlaşma (bubbling regime) rejiminde, genellikle 2 - 4 x U_mf hız aralığıdır. Bu rejimde iyi karışım ve yüksek ısı transferi sağlanırken parçacık aşınması sınırlı kalır.

---

## Tipler

### 1. Tam Karışımlı Akışkan Yatak (Well-Mixed / Back-Mixed FBD)

En yaygın tiptir. Parçacıklar yatak içinde sürekli ve rastgele hareket eder, ürün nemi homojendir ancak geniş bir kalış süresi dağılımı (residence time distribution — RTD) oluşur. Bu durum, bazı parçacıkların çok kısa sürede çıkmasına (yetersiz kurutma) veya çok uzun süre kalmasına (aşırı kurutma) neden olabilir.

- **Avantaj:** Basit tasarım, homojen yatak sıcaklığı, kolay işletme
- **Dezavantaj:** Geniş RTD, çıkış nem dağılımı geniş olabilir
- **Uygulama:** Kimyasal kurutma, mineral kurutma, genel amaçlı

### 2. Tıkaç Akışlı Akışkan Yatak (Plug-Flow FBD)

Uzun ve dar bir yatak geometrisi ile parçacıkların bir uçtan girip diğer uçtan çıkması sağlanır. Kalış süresi dağılımı çok daha dar olduğundan çıkış nemi kontrollüdür.

- **Avantaj:** Dar RTD, homojen çıkış nemi, çok kademeli kurutma mümkün
- **Dezavantaj:** Daha karmaşık tasarım, yatak boyunca sıcaklık/nem gradyanı
- **Uygulama:** İlaç sektörü, hassas gıda granülleri, kalite-kritik ürünler

### 3. Titreşimli Akışkan Yatak (Vibrating Fluidized Bed — VFB)

Yatak tabanına mekanik titreşim uygulanır. Bu, akışkanlaşma için gereken hava hızını %30-60 oranında düşürür ve ince/yapışkan parçacıkların akışkanlaşmasını kolaylaştırır.

- **Avantaj:** Düşük hava hızı, düşük fan gücü, yapışkan malzemeler için uygun
- **Dezavantaj:** Titreşim mekanizması bakımı, mekanik karmaşıklık
- **Uygulama:** Şeker kristalleri, tuz, toz deterjan, yapışkan gıda granülleri

### 4. Darbeli Akışkan Yatak (Pulsed Fluidized Bed)

Hava akışı periyodik olarak açılıp kapatılır veya debisi dalgalı (pulsating) olarak değiştirilir. Bu, enerji tüketimini azaltır ve belirli malzemelerde daha iyi karışım sağlar.

- **Avantaj:** %15-30 daha düşük enerji tüketimi, iyi karışım
- **Dezavantaj:** Karmaşık kontrol sistemi, valf bakımı
- **Uygulama:** Araştırma aşamasında, bazı endüstriyel pilot uygulamalar

### 5. Kızgın Buhar Akışkan Yatak (Superheated Steam FBD)

Kurutma ortamı olarak hava yerine kızgın buhar (superheated steam) kullanılır. Buhar yoğunluğu yüksek olduğundan akışkanlaşma daha kolaydır ve egzoz buharı enerji geri kazanımı için kullanılabilir.

- **Avantaj:** Yüksek enerji verimi (egzoz buharı geri kazanılabilir), inert ortam (patlama riski yok)
- **Dezavantaj:** Yüksek yatırım maliyeti, sızdırmazlık kritik, başlangıç/durdurma zor
- **Uygulama:** Şeker pancarı küspesi, kömür kurutma, odun peletleri

---

## Parametreler

### Giriş Parametreleri

| Parametre | Sembol | Birim | Tipik Aralık | Açıklama |
|-----------|--------|-------|--------------|----------|
| Giriş hava sıcaklığı | T_air_in | °C | 40 - 200 | Isıtılmış havanın kurutucu girişindeki sıcaklığı |
| Ortam sıcaklığı | T_0 | °C | 15 - 35 | Referans (ölü durum) sıcaklığı |
| Ortam bağıl nemi | RH_0 | % | 30 - 80 | Ortam havası bağıl nemi |
| Malzeme giriş nemi | M_in | % (yaş baz) | 5 - 40 | Besleme malzemesinin nem içeriği |
| Malzeme besleme debisi | m_feed | kg/h | 100 - 20.000 | Yaş malzeme besleme hızı |
| Hava kütlesel debisi | m_air | kg/h | 1.000 - 100.000 | Kurutma havası debisi |
| Fan giriş gücü | P_fan | kW | 10 - 200 | Fan elektrik tüketimi |
| Parçacık çapı | d_p | mm | 0,05 - 10 | Ortalama parçacık çapı |
| Parçacık yoğunluğu | rho_p | kg/m³ | 800 - 3.000 | Parçacık malzeme yoğunluğu |

### Çıkış ve Hesaplanan Parametreler

| Parametre | Sembol | Birim | Tipik Aralık | Açıklama |
|-----------|--------|-------|--------------|----------|
| Egzoz sıcaklığı | T_exhaust | °C | 40 - 80 | Egzoz havası sıcaklığı |
| Egzoz bağıl nemi | RH_out | % | 50 - 90 | Egzoz havasının bağıl nemi |
| Malzeme çıkış nemi | M_out | % (yaş baz) | 0,5 - 5 | Kurutulmuş ürün nemi |
| Yatak sıcaklığı | T_bed | °C | 35 - 70 | Akışkan yatak iç sıcaklığı (adyabatik doyma sıcaklığına yakın) |
| Buharlaşan su miktarı | m_evap | kg/h | Hesaplanan | m_feed x (M_in - M_out) / (1 - M_out) |
| SMER | SMER | kg/kWh | 0,5 - 1,5 | m_evap / (Q_thermal + P_fan) |
| Termal verimlilik | eta_th | % | 50 - 65 | Q_evaporation / Q_input x 100 |
| Exergy verimi | eta_ex | % | 8 - 18 | Ex_evaporation / (Ex_thermal + Ex_fan) x 100 |
| Akışkanlaşma sayısı | U/U_mf | - | 2 - 4 | Çalışma hızı / minimum akışkanlaşma hızı |

---

## Exergy Analizi

### Exergy Girdisi

FBD'de exergy girdisi iki ana bileşenden oluşur:

**Termal exergy (ısıtıcı):**
```
Ex_thermal = Q_heater x (1 - T_0 / T_supply)  [kW]
```

**Elektrik exergy (fan + yardımcı):**
```
Ex_electric = P_fan + P_aux  [kW]
```
Elektrik saf exergy'dir (%100 exergy içeriği).

**Toplam exergy girdisi:**
```
Ex_input = Ex_thermal + Ex_electric  [kW]
```

### Faydalı Exergy Çıkışı

Buharlaşma exergy'si:
```
Ex_evaporation = m_evap x [(h_fg - T_0 x s_fg)]  [kW]

Burada:
- h_fg = buharlaşma gizli ısısı (kJ/kg) — sıcaklığa bağlı
- s_fg = buharlaşma entropisi = h_fg / T_evap (kJ/kg.K)
- T_evap = buharlaşma sıcaklığı (K) — yatak sıcaklığına yakın
- T_0 = ölü durum sıcaklığı = 298,15 K (25°C)
```

### Exergy Verimi

```
eta_ex = Ex_evaporation / Ex_input x 100  [%]
```

### FBD Exergy Verimi Benchmark

| Seviye | Exergy Verimi (%) | Yorum |
|--------|-------------------|-------|
| Düşük | < 8 | Büyük iyileştirme potansiyeli, acil müdahale |
| Ortalama | 8 - 14 | Tipik FBD performansı |
| İyi | 14 - 18 | Optimize edilmiş modern sistem |
| Mükemmel | > 18 | Isı geri kazanımlı, çok kademeli veya ısı pompalı |

### Exergy Analizi Önemli Notlar

- Fan gücü saf exergy (elektrik) olduğu için exergy analizinde orantısız şekilde önemlidir. 1 kW elektrik = 1 kW exergy, ancak 1 kW termal enerji < 1 kW exergy.
- Yatak sıcaklığı genellikle adyabatik doyma sıcaklığına (adiabatic saturation temperature) yakındır ve kurutma veriminin dolaylı göstergesidir.
- Düşük sıcaklıklı uygulamalarda (< 80°C) ısı pompası entegrasyonu exergy verimini 2-3 kat artırabilir.

---

## Kayıp Dağılımı

### Tipik Enerji Dağılımı

| Enerji Bileşeni | Oran (%) | Açıklama |
|-----------------|----------|----------|
| Buharlaşma (evaporation) | ~55 | Ana faydalı enerji kullanımı |
| Egzoz kaybı (exhaust loss) | ~22 | Sıcak ve nemli egzoz havası |
| Fan gücü (fan power) | ~10 | Akışkanlaşma basınç düşümünü karşılamak için |
| Radyasyon/konveksiyon kaybı (shell loss) | ~6 | Gövde yüzeyinden çevreye ısı transferi |
| Malzeme sensible ısıtma | ~4 | Ürünün sıcaklık artışı |
| Diğer kayıplar (sızıntı, toz toplama vb.) | ~3 | Çeşitli küçük kayıplar |

### Tipik Exergy Dağılımı (Grassmann Diyagramı)

```
EXERGY GİRİŞİ (100%)
|
|-- Termal exergy girdisi (~75-85%)
|   |
|   |-- Isıtma tersinmezliği (%18-28) ------------> EXERGY YIKIM
|   |   [Yüksek sıcaklık -> düşük sıcaklık ısı transferi]
|   |
|   |-- Kurutma prosesi tersinmezliği (%22-32) ---> EXERGY YIKIM
|   |   [Nemli malzeme - hava etkileşimi, kütle transferi]
|   |
|   |-- Egzoz havası exergy kaybı (%18-28) -------> KAYIP (GERİ KAZANILABİLİR)
|   |
|   |-- Gövde kayıpları (%2-5) -------------------> KAYIP
|   |
|   |-- Faydalı buharlaşma exergy'si (%8-18) -----> FAYDALI ÇIKIŞ
|
|-- Fan elektrik girdisi (~15-25%)
|   |-- Fan tersinmezliği (%5-10) -----------------> EXERGY YIKIM
```

### Kayıp Azaltma Öncelikleri

1. **Egzoz kaybı** — en büyük geri kazanılabilir kayıp kaynağı
2. **Isıtma tersinmezliği** — daha düşük sıcaklık kaynağı kullanımı ile azaltılabilir
3. **Fan gücü** — VFD ve basınç düşümü optimizasyonu ile azaltılabilir
4. **Gövde kayıpları** — izolasyon iyileştirmesi ile minimize edilebilir

---

## Avantaj ve Dezavantajlar

### Avantajlar

| Avantaj | Açıklama |
|---------|----------|
| Homojen kurutma (uniform drying) | Her parçacık eşit şekilde sıcak hava ile temas eder |
| Yüksek ısı transfer katsayısı | 100-400 W/m².K — konvektif kurutucularda en yüksek seviye |
| Kompakt tasarım | Birim hacim başına yüksek kapasite |
| İyi sıcaklık kontrolü | Yatak sıcaklığı homojen ve kontrol edilebilir |
| Ölçeklendirme kolaylığı | Laboratuvardan endüstriyele kolay scale-up |
| Çok amaçlı | Kurutma, granülasyon, kaplama, soğutma aynı ekipmanla |
| Kesikli ve sürekli | Her iki modda da çalışabilir |
| Kısa kurutma süresi | İyi temas sayesinde hızlı nem uzaklaştırma |

### Dezavantajlar

| Dezavantaj | Açıklama |
|------------|----------|
| Parçacık boyutu sınırlaması | Sadece 50 µm - 10 mm aralığında çalışır |
| Aşınma (attrition) | Parçacıklar arası çarpışma ile kırılma ve toz oluşumu |
| Yüksek basınç düşümü | Yatak basınç düşümü 2-12 kPa, yüksek fan enerjisi |
| Yapışkan malzeme sorunu | Nemli ve yapışkan parçacıklar aglomerasyon yapabilir |
| Toz toplama gereksinimi | Egzoz havasında ince parçacıklar; siklon/torba filtre zorunlu |
| Kanal oluşumu (channeling) | Hava tercihli kanallardan geçebilir, karışım bozulur |
| Geniş kalış süresi dağılımı | Tam karışımlı tiplerde çıkış nemi değişken olabilir |

---

## Uygulamalar

### Sektörel Uygulama Tablosu

| Sektör | Tipik Ürünler | T_air_in (°C) | Parçacık Boyutu | SMER (kg/kWh) | Not |
|--------|---------------|---------------|-----------------|----------------|-----|
| İlaç (pharmaceuticals) | Granüller, tabletler, kaplama | 40 - 80 | 0,1 - 2 mm | 0,5 - 1,0 | GMP koşulları, düşük sıcaklık |
| Kimya (chemicals) | Katalizörler, pigmentler, polimerler | 80 - 200 | 0,05 - 5 mm | 0,8 - 1,5 | Yüksek sıcaklık mümkün |
| Gıda (food) | Kahve, süt tozu, baharat, şeker | 50 - 100 | 0,2 - 5 mm | 0,7 - 1,3 | Kalite koruma, düşük sıcaklık |
| Mineral (minerals) | Kum, silis, alümina, kireç | 100 - 200 | 0,1 - 10 mm | 1,0 - 1,5 | Yüksek sıcaklık, dayanıklı malzeme |
| Tarım (agriculture) | Tohum, tahıl, yem peletleri | 40 - 80 | 1 - 10 mm | 0,8 - 1,3 | Düşük sıcaklık, canlılık koruma |
| Gübre (fertilizer) | Üre, NPK granülleri | 80 - 120 | 1 - 5 mm | 0,9 - 1,4 | Toz minimizasyonu |

### İlaç Sektörü Özel Gereksinimleri

- GMP (Good Manufacturing Practice) uyumlu malzeme ve tasarım
- CIP (Clean-In-Place) sistemi
- HEPA filtrasyon egzoz hattında
- Tam izlenebilirlik (traceability) ve kayıt tutma
- Validasyon gereksinimleri (IQ, OQ, PQ)

---

## İyileştirme

### Enerji İyileştirme Önerileri

| Öneri | Tasarruf Potansiyeli | Yatırım Maliyeti | Geri Dönüş |
|-------|---------------------|-------------------|------------|
| Egzoz ısı geri kazanımı (exhaust heat recovery) | %15-25 enerji | 20.000 - 120.000 € | 1 - 2,5 yıl |
| Değişken hızlı fan (VFD) | %15-30 elektrik | 5.000 - 35.000 € | 0,5 - 1,5 yıl |
| Hava resirkülasyonu (partial recirculation) | %10-20 enerji | 10.000 - 50.000 € | 1 - 2 yıl |
| Çok kademeli kurutma (multi-stage drying) | %10-20 enerji | 40.000 - 200.000 € | 2 - 4 yıl |
| İç ısı eşanjörü (internal heat exchanger / immersed tubes) | %8-15 enerji | 15.000 - 80.000 € | 1,5 - 3 yıl |
| Kızgın buhar (superheated steam) dönüşümü | %25-40 enerji | 100.000 - 500.000 € | 3 - 6 yıl |
| Isı pompası entegrasyonu | %30-50 enerji | 60.000 - 350.000 € | 3 - 5 yıl |
| Dağılım plakası optimizasyonu | %3-7 enerji | 5.000 - 25.000 € | 0,5 - 1 yıl |
| Yatak derinliği optimizasyonu | %3-8 enerji | 2.000 - 12.000 € | 0,3 - 0,8 yıl |
| Gelişmiş kontrol sistemi (model-predictive control) | %5-12 enerji | 15.000 - 60.000 € | 1 - 2,5 yıl |
| İzolasyon iyileştirme | %2-5 enerji | 3.000 - 15.000 € | 0,5 - 1 yıl |

### Çok Kademeli Kurutma (Multi-Stage Drying)

Çok kademeli FBD'de her kademe farklı sıcaklık ve nem koşullarında çalışır:

- **1. Kademe:** Yüksek sıcaklık (120-200°C), yüksek hava hızı — sabit kurutma hızı döneminde hızlı nem uzaklaştırma
- **2. Kademe:** Orta sıcaklık (80-120°C) — azalan kurutma hızı dönemine geçiş
- **3. Kademe:** Düşük sıcaklık (40-80°C) — son nem ayarı ve soğutma

Bu yaklaşım, yüksek exergy kalitesindeki enerjiyi yalnızca gerçekten gerekli olan aşamada kullanarak toplam exergy yıkımını %10-20 oranında azaltır.

### İç Isı Eşanjörleri (Immersed Heat Exchangers)

Yatak içine buhar serpantini veya sıcak su boruları yerleştirilerek parçacıklara doğrudan temas yoluyla ısı aktarılır. Bu yöntem:

- Hava debisini ve dolayısıyla fan gücünü %20-40 oranında azaltır
- Egzoz kaybını azaltır (daha az hava = daha az egzoz)
- Exergy verimini %3-6 puan artırabilir
- Özellikle büyük kapasiteli sistemlerde ekonomiktir

### Cross-Equipment Fırsatları

Yakın proseslerden gelen atık ısı, FBD giriş havasının ön ısıtması için kullanılabilir:

- **Kompresör atık ısısı:** Kompresör soğutma suyundan 60-90°C ısı geri kazanımı
- **Kazan baca gazı:** Ekonomizer çıkışı, FBD hava ön ısıtıcısı olarak
- **Soğutma sistemi kondenser ısısı:** Chiller/soğutucu kondenser atık ısısı
- **Fırın/reaktör egzoz ısısı:** Yüksek sıcaklıklı proses egzozu

---

## Yatırım

### Yatırım Maliyeti Tablosu

| Kapasite (kg/h) | Tip | Yatırım Maliyeti (€) | Açıklama |
|------------------|-----|----------------------|----------|
| 100 - 500 | Kesikli (batch) | 50.000 - 150.000 | İlaç, pilot tesis |
| 500 - 2.000 | Sürekli, tek kademe | 120.000 - 350.000 | Kimyasal, gıda |
| 2.000 - 5.000 | Sürekli, çok kademeli | 300.000 - 700.000 | Büyük ölçekli kimyasal/mineral |
| 5.000 - 10.000 | Sürekli, çok kademeli | 600.000 - 1.200.000 | Gübre, büyük mineral tesisleri |
| 10.000 - 20.000 | Sürekli, çok kademeli | 1.000.000 - 2.500.000 | Çok büyük kapasiteli endüstriyel |

### Yatırım Maliyetini Etkileyen Faktörler

- **Malzeme seçimi:** Paslanmaz çelik (AISI 316L) ilaç sektöründe zorunlu; karbon çelik mineral için yeterli
- **ATEX sınıflandırması:** Patlayıcı ortam gereksinimleri maliyeti %20-40 artırır
- **CIP sistemi:** Gıda/ilaç uygulamalarında ek %15-25 maliyet
- **Toz toplama sistemi:** Siklon + torba filtre kombinasyonu ek %10-20 maliyet
- **Kontrol seviyesi:** Basit PID'den tam otomasyon/SCADA'ya maliyeti 2-3 kat değiştirir

### İşletme Maliyeti (Yıllık)

| Kalem | Oran (toplam işletme maliyetinin %'si) | Açıklama |
|-------|----------------------------------------|----------|
| Enerji (termal + elektrik) | 55 - 70 | En büyük maliyet kalemi |
| Bakım ve yedek parça | 8 - 15 | Dağılım plakası, filtre, yatak malzemesi |
| İşçilik | 10 - 20 | Operatör, bakım teknisyeni |
| Toz toplama filtre değişimi | 3 - 8 | Torba filtre ömrü: 1-3 yıl |
| Diğer (sigorta, amortisman) | 5 - 15 | Sabit giderler |

---

## İlgili Dosyalar

- `knowledge/dryer/formulas.md` — Kurutma exergy hesaplama formülleri ve denklemleri
- `knowledge/dryer/benchmarks.md` — Kurutucu performans karşılaştırma benchmark değerleri
- `knowledge/dryer/solutions/exhaust_heat_recovery.md` — Egzoz ısı geri kazanım çözümleri
- `knowledge/dryer/solutions/temperature_optimization.md` — Sıcaklık optimizasyonu rehberi
- `knowledge/dryer/sectors/food_drying.md` — Gıda sektörü kurutma benchmarkları
- `knowledge/dryer/psychrometrics.md` — Nemli hava termodinamiği ve psikrometrik hesaplar
- `knowledge/dryer/equipment/belt_dryer.md` — Bant kurutucu detayları (karşılaştırma)
- `knowledge/dryer/equipment/spray_dryer.md` — Sprey kurutucu detayları (karşılaştırma)
- `knowledge/dryer/equipment/heat_pump_dryer.md` — Isı pompalı kurutucu detayları
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası entegrasyon fırsatları

---

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press. — Bölüm 8: Fluidized Bed Dryers.
2. Kemp, I.C. (2012). *Fundamentals of Energy Analysis of Dryers*, in Modern Drying Technology, Vol. 4, Wiley.
3. Kunii, D. & Levenspiel, O. (1991). *Fluidization Engineering*, 2nd Edition, Butterworth-Heinemann. — Akışkanlaşma temel ilkeleri ve tasarım denklemleri.
4. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press. — Kızgın buhar FBD, titreşimli FBD.
5. Geldart, D. (1986). *Gas Fluidization Technology*, John Wiley & Sons. — Parçacık sınıflandırması (Geldart A/B/C/D).
6. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
7. Szargut, J. (2005). *Exergy Method: Technical and Ecological Applications*, WIT Press.
8. Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, Section 17: Gas-Solid Operations and Equipment.
9. Aghbashlo, M. et al. (2013). "A review on exergy analysis of drying processes and systems," *Renewable and Sustainable Energy Reviews*, 22, 1-22.
10. Syahrul, S. et al. (2002). "Exergy analysis of fluidized bed drying of moist particles," *Exergy, an International Journal*, 2(2), 87-98.
