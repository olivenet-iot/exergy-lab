---
title: "Tünel Kurutucu (Tunnel Dryer)"
category: dryer
equipment_type: dryer
keywords:
  - tünel kurutucu
  - tunnel dryer
  - konvektif kurutma
  - batch kurutma
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/air_recirculation.md
  - dryer/sectors/ceramic_drying.md
  - dryer/sectors/food_drying.md
use_when:
  - "Tünel kurutucu analiz edilirken"
  - "Karşı akışlı kurutma sistemi değerlendirilirken"
priority: medium
last_updated: 2026-02-01
---

# Tünel Kurutucu (Tunnel Dryer)

## Genel Bakış

Tünel kurutucu (tunnel dryer), endüstriyel ölçekte sürekli veya yarı-sürekli çalışan konvektif bir kurutma sistemidir. Ürün, vagonlar (cars/trolleys), paletler veya taşıma bantları üzerinde uzun bir tünel boyunca hareket ederken, sıcak hava ile temas ederek kurutulur. Tünel kurutucular, yüksek hacimli ve uzun kurutma süresi gerektiren uygulamalar için tercih edilir; özellikle seramik, tuğla, kereste, gıda ve kimyasal ürün endüstrilerinde yaygın olarak kullanılır.

Temel avantajları arasında büyük kapasiteli üretim, düşük işçilik gereksinimi ve farklı akış konfigürasyonlarına uyarlanabilirlik yer alır. Bununla birlikte, uzun tünel yapısı nedeniyle büyük tesis alanı ve yüksek yatırım maliyeti gerektirir. Enerji tüketimi açısından en önemli kayıp kaynağı egzoz havası ile atılan ısıdır; bu kayıp toplam enerjinin %30-40'ına ulaşabilir.

- **Tip:** Sürekli konvektif (continuous convective)
- **Kapasite aralığı:** 100 - 10.000 kg/h
- **Giriş havası sıcaklığı:** 50 - 200 °C (ürüne bağlı)
- **Tünel uzunluğu:** 10 - 100 m (tipik)
- **Kalma süresi (residence time):** 1 - 72 saat (ürüne bağlı)
- **Enerji kaynağı:** Doğal gaz brülörü, buhar serpantini (steam coils), sıcak su, elektrikli ısıtıcı
- **Exergy verimi:** %5 - 12 (tipik endüstriyel değer)
- **SMER (Specific Moisture Extraction Rate):** 0,3 - 0,8 kg/kWh
- **Yatırım maliyeti:** 150.000 - 2.500.000 €

## Çalışma Prensibi

Tünel kurutucu, sıcak hava ile ürün arasındaki konvektif ısı ve kütle transferine dayalı çalışır. Temel proses adımları şunlardır:

1. **Hava ısıtma (air heating):** Ortam havası, doğal gaz brülörü, buhar serpantini veya sıcak su ısı eşanjörü ile belirlenen sıcaklığa ısıtılır.
2. **Hava dağıtımı (air distribution):** Isıtılmış hava, fan sistemi aracılığıyla tünel boyunca yönlendirilir. Konfigürasyona bağlı olarak ürünle aynı yönde (co-current), ters yönde (counter-current) veya karışık akışta (mixed flow) hareket eder.
3. **Kurutma (drying):** Ürün, vagon veya palet üzerinde tünel boyunca ilerlerken sıcak hava ile temas eder. Üründeki nem, konveksiyon ve difüzyon mekanizmaları ile havaya geçer.
4. **Egzoz (exhaust):** Nemli hava, tünel çıkışından veya ara noktalardan egzoz fanları ile dışarı atılır. Bu aşama, sistemin en büyük enerji kaybı noktasıdır.
5. **Ürün çıkışı:** Kurutulmuş ürün, tünel sonunda hedef nem değerine ulaşmış olarak çıkarılır.

### Kurutma Eğrisi (Drying Curve)

Tünel kurutucu boyunca kurutma üç temel aşamada gerçekleşir:
- **Isınma aşaması (warm-up period):** Ürün sıcaklığı yükselir, buharlaşma yavaş başlar
- **Sabit hız dönemi (constant rate period):** Yüzey nemi sabit hızda buharlaşır; ürün sıcaklığı yaş termometre sıcaklığına yakın kalır
- **Azalan hız dönemi (falling rate period):** İç difüzyon kontrollüdür; kurutma hızı düşer, ürün sıcaklığı yükselir

## Tipler (Flow Configurations)

### Karşı Akışlı (Counter-Current)

Hava ve ürün birbirine zıt yönlerde hareket eder. Sıcak hava, kuru ürün tarafından girer; nemli ürün tarafından çıkar.

- **Avantajlar:** En yüksek termal verimlilik; tünel boyunca daha düzgün sıcaklık gradyanı; düşük egzoz sıcaklığı (daha fazla enerji ürüne transfer edilir)
- **Dezavantajlar:** Kuru ürün yüksek sıcaklıkla karşılaşır — ısıya duyarlı ürünlerde hasar riski
- **Tipik uygulama:** Seramik, tuğla, refrakter malzemeler
- **Termal verimlilik:** %55 - 70
- **Exergy verimi:** %8 - 12

### Eş Yönlü Akış (Co-Current)

Hava ve ürün aynı yönde hareket eder. Sıcak hava, ıslak ürün tarafından girer.

- **Avantajlar:** Ürün çıkışında düşük sıcaklık (ısıya duyarlı ürünler için güvenli); başlangıçta yüksek kurutma hızı
- **Dezavantajlar:** Egzoz havası daha sıcak çıkar — daha yüksek enerji kaybı; termal verimlilik counter-current'a göre düşük
- **Tipik uygulama:** Gıda ürünleri, meyve, sebze, makarna
- **Termal verimlilik:** %40 - 55
- **Exergy verimi:** %5 - 9

### Karışık Akış (Mixed Flow)

Tünel, birden fazla bölgeye (zone) ayrılır ve her bölgede farklı akış yönü uygulanır. Tipik olarak ilk bölge co-current, son bölge counter-current şeklinde tasarlanır.

- **Avantajlar:** En esnek konfigürasyon; her bölgede bağımsız sıcaklık ve hava hızı kontrolü; ürün kalitesi ve verimlilik dengesini optimize etme imkanı
- **Dezavantajlar:** Daha karmaşık kontrol sistemi; yüksek yatırım maliyeti; daha fazla fan ve kanal gereksinimi
- **Tipik uygulama:** Çok aşamalı kurutma gerektiren ürünler — kereste, özel seramikler
- **Termal verimlilik:** %50 - 65
- **Exergy verimi:** %7 - 11

## Tipik Çalışma Parametreleri (Typical Operating Conditions)

| Parametre | Minimum | Tipik | Maksimum | Birim |
|-----------|---------|-------|----------|-------|
| Giriş havası sıcaklığı (T_air_in) | 50 | 120 | 200 | °C |
| Egzoz havası sıcaklığı (T_exhaust) | 40 | 70 | 110 | °C |
| Hava hızı (air velocity) | 0,5 | 2,0 | 5,0 | m/s |
| Ürün besleme debisi (feed rate) | 100 | 2.000 | 10.000 | kg/h |
| Ürün giriş nemi (M_in) | 10 | 30 | 60 | % (yaş baz) |
| Ürün çıkış nemi (M_out) | 1 | 5 | 15 | % (yaş baz) |
| Tünel uzunluğu | 10 | 40 | 100 | m |
| Tünel genişliği | 2 | 3 | 6 | m |
| Tünel yüksekliği | 2 | 2,5 | 4 | m |
| Kalma süresi (residence time) | 1 | 12 | 72 | saat |
| Hava debisi (air flow rate) | 5.000 | 25.000 | 80.000 | m3/h |
| Isıtma gücü (thermal input) | 50 | 500 | 5.000 | kW |
| Fan gücü (fan power) | 5 | 40 | 150 | kW |
| Ortam sıcaklığı (T_0) | 15 | 25 | 40 | °C |

## Exergy Analizi (Exergy Analysis)

Tünel kurutucularda exergy analizi, enerji analizinin ötesinde termodinamik kalitenin değerlendirilmesini sağlar. Kurutma prosesi düşük sıcaklıklarda gerçekleştiği için Carnot faktörü küçüktür ve enerji verimliliği ile exergy verimliliği arasında büyük fark oluşur.

### Exergy Verimi Tanımı

```
psi_dryer = Ex_evaporation / (Ex_air_in + W_fan)

Burada:
  psi_dryer      = Exergy verimi (boyutsuz, tipik 0,05 - 0,12)
  Ex_evaporation = Buharlaştırma prosesinin exergysi (kW)
  Ex_air_in      = Giriş havasının fiziksel exergysi (kW)
  W_fan          = Fan güç tüketimi (kW)

Ex_air = m_air × Cp × [(T - T0) - T0 × ln(T / T0)]

Burada:
  T0 = Referans (ölü durum) sıcaklığı (K), tipik 298,15 K
  T  = Hava sıcaklığı (K)
```

### Exergy Kayıp Mekanizmaları

Tünel kurutucularda exergy yıkımı (exergy destruction) başlıca şu bileşenlerden oluşur:

1. **Isıtma bölgesinde exergy yıkımı (~40%):** Yüksek sıcaklıktaki enerji kaynağından (yanma gazları veya buhar, 300-1000 °C) düşük sıcaklıktaki havaya (50-200 °C) ısı transferinde büyük sıcaklık farkı (delta T) nedeniyle tersinmezlik oluşur.
2. **Kurutma bölgesinde exergy yıkımı (~25%):** Sıcak hava ile ıslak ürün arasındaki ısı ve kütle transferi tersinmez bir prosestir. Difüzyon kaynaklı entropi üretimi önemlidir.
3. **Egzoz ile exergy kaybı (~25%):** Nemli sıcak havanın sistemi terk etmesi, hem termal hem de kimyasal exergy kaybına neden olur. Düşük egzoz sıcaklığında bile yüksek nem oranı önemli exergy içerir.
4. **Duvar kayıpları ile exergy kaybı (~7%):** Tünel duvarlarından çevreye ısı transferi, düşük sıcaklıkta gerçekleştiği için düşük exergy içeriğine sahiptir, ancak uzun tünel yapısı nedeniyle toplam alan büyüktür.
5. **Diğer kayıplar (~3%):** Hava sızıntısı, fan tersinmezlikleri, kontrol kayıpları.

## Exergy Kayıp Dağılımı (Exergy Loss Distribution)

| Kayıp Bileşeni | Oran (%) | Exergy Yıkımı Tipi | Azaltma Stratejisi |
|-----------------|----------|---------------------|---------------------|
| Isıtma bölgesi (heating section) | ~40 | Dahili yıkım (internal destruction) | Düşük delta T tasarımı, kademeli ısıtma |
| Kurutma bölgesi (drying section) | ~25 | Dahili yıkım (internal destruction) | Optimum hava hızı ve sıcaklık profili |
| Egzoz havası kaybı (exhaust loss) | ~25 | Harici kayıp (external loss) | Isı geri kazanımı, hava resirkülasyonu |
| Duvar kayıpları (wall losses) | ~7 | Harici kayıp (external loss) | Yalıtım iyileştirmesi |
| Diğer (miscellaneous) | ~3 | Karışık | Sızıntı önleme, bakım |

## SMER ve Verimlilik (SMER & Efficiency)

### SMER Benchmark Tablosu

| Performans Seviyesi | SMER (kg/kWh) | Exergy Verimi (%) | Durum |
|---------------------|---------------|-------------------|-------|
| Düşük performans | < 0,3 | < 5 | Acil iyileştirme gerekli |
| Tipik alt sınır | 0,3 - 0,4 | 5 - 7 | Eski veya bakımsız sistem |
| Orta performans | 0,4 - 0,6 | 7 - 9 | Standart endüstriyel işletme |
| İyi performans | 0,6 - 0,8 | 9 - 11 | Optimize edilmiş sistem |
| En iyi uygulama (best practice) | 0,8 - 1,0 | 11 - 12 | Isı geri kazanımlı modern sistem |
| Teorik sınır | ~1,2 | ~15 | İdeal koşullarda |

### Sektöre Göre Verimlilik Farkları

| Sektör | Tipik SMER (kg/kWh) | Exergy Verimi (%) | Açıklama |
|--------|---------------------|-------------------|----------|
| Seramik / tuğla (ceramics/brick) | 0,3 - 0,6 | 5 - 9 | Yüksek sıcaklık (150-200 °C), uzun süre (24-72 saat) |
| Kereste (timber) | 0,3 - 0,5 | 4 - 8 | Düşük sıcaklık (50-80 °C), çok uzun süre (48-168 saat) |
| Gıda (food products) | 0,4 - 0,7 | 6 - 10 | Orta sıcaklık (60-90 °C), kalite kritik |
| Kimyasal ürünler (chemicals) | 0,5 - 0,8 | 7 - 11 | Değişken, ürüne bağlı |

## Avantajlar ve Dezavantajlar

### Avantajlar

- **Yüksek kapasite:** Büyük hacimli üretim için uygun; 100 - 10.000 kg/h aralığında çalışabilir
- **Sürekli işletme:** Kesintisiz üretim hattına entegre edilebilir; yüksek üretim verimliliği
- **Düzgün kurutma:** Uzun kalma süresi sayesinde homojen nem dağılımı elde edilir
- **Esnek konfigürasyon:** Counter-current, co-current veya mixed flow seçenekleri ile farklı ürün gereksinimlerine uyarlanabilir
- **Otomasyon kolaylığı:** Bölgesel sıcaklık, nem ve hava hızı kontrolü ile tam otomatik işletme mümkün
- **Geniş ürün yelpazesi:** Seramik, tuğla, kereste, gıda, kimyasal ürünler gibi çok çeşitli malzemeler kurutulabilir

### Dezavantajlar

- **Düşük exergy verimi (%5-12):** Büyük sıcaklık farkları ve yüksek egzoz kayıpları nedeniyle termodinamik performans düşüktür
- **Büyük tesis alanı:** Uzun tünel yapısı (10-100 m) geniş alan gerektirir
- **Yüksek yatırım maliyeti:** 150.000 - 2.500.000 € arasında yatırım maliyeti; uzun geri ödeme süresi
- **Uzun kalma süresi:** 1 - 72 saat arasında değişen kurutma süreleri; süreç esnekliği düşük
- **Yüksek egzoz kaybı:** Toplam enerjinin %30-40'ı egzoz ile kaybedilir
- **Düzensiz hava dağılımı riski:** Tünel kesiti boyunca hava hızı ve sıcaklık farklılıkları oluşabilir; ürünler arasında nem farklılıklarına yol açar

## Tipik Uygulamalar (Typical Applications)

### Seramik ve Tuğla (Ceramics & Brick)

- **Giriş sıcaklığı:** 150 - 200 °C
- **Kalma süresi:** 24 - 72 saat
- **Konfigürasyon:** Counter-current (karşı akışlı)
- **Ürün giriş nemi:** %15 - 25 (yaş baz)
- **Ürün çıkış nemi:** %1 - 3 (yaş baz)
- **Kritik faktör:** Çatlama riski — kurutma hızı kontrollü olmalıdır; aşırı hızlı kurutma iç gerilmelere yol açar

### Kereste (Timber / Lumber)

- **Giriş sıcaklığı:** 50 - 80 °C
- **Kalma süresi:** 48 - 168 saat (haftalar sürebilir)
- **Konfigürasyon:** Mixed flow (karışık akış) — bölgesel kontrol ile
- **Ürün giriş nemi:** %40 - 60 (yaş baz)
- **Ürün çıkış nemi:** %8 - 12 (yaş baz)
- **Kritik faktör:** Çarpılma ve çatlama — düşük sıcaklık ve yüksek nem ile yavaş kurutma gerekli

### Gıda Ürünleri (Food Products)

- **Giriş sıcaklığı:** 60 - 90 °C
- **Kalma süresi:** 2 - 12 saat
- **Konfigürasyon:** Co-current (eş yönlü) — ısıya duyarlı ürünler için
- **Ürün giriş nemi:** %20 - 50 (yaş baz)
- **Ürün çıkış nemi:** %5 - 10 (yaş baz)
- **Tipik ürünler:** Meyve, sebze, makarna, baharat
- **Kritik faktör:** Gıda güvenliği ve renk/aroma korunması

### Kimyasal Ürünler (Chemical Products)

- **Giriş sıcaklığı:** 100 - 180 °C
- **Kalma süresi:** 2 - 24 saat
- **Konfigürasyon:** Ürüne bağlı
- **Ürün giriş nemi:** %10 - 30 (yaş baz)
- **Ürün çıkış nemi:** %0,5 - 5 (yaş baz)
- **Tipik ürünler:** Pigmentler, katalizörler, reçineler
- **Kritik faktör:** Ürün spesifikasyonuna uygunluk

## Enerji İyileştirme Fırsatları (Energy Improvement Opportunities)

| Önlem | Enerji Tasarrufu (%) | Yatırım Maliyeti (€) | Geri Ödeme Süresi | Açıklama |
|-------|---------------------|----------------------|-------------------|----------|
| Egzoz ısı geri kazanımı (exhaust heat recovery) | 15 - 25 | 30.000 - 200.000 | 1 - 3 yıl | Egzoz havası ile giriş havasını ön ısıtma; ısı eşanjörü veya ısı borusu (heat pipe) kullanımı |
| Hava resirkülasyonu (air recirculation) | 10 - 20 | 15.000 - 80.000 | 1 - 2 yıl | Egzoz havasının bir kısmının sisteme geri döndürülmesi; nem doygunluk noktasına dikkat |
| Bölgesel sıcaklık kontrolü (zoned temperature control) | 8 - 15 | 20.000 - 100.000 | 1,5 - 3 yıl | Her bölgeye bağımsız sıcaklık ve hava hızı kontrolü; kurutma profiline göre optimizasyon |
| Tünel yalıtım iyileştirmesi (insulation upgrade) | 5 - 12 | 10.000 - 60.000 | 1 - 2 yıl | 50-100 mm mineral yün veya cam yünü ile duvar ve tavan yalıtımı |
| Değişken hızlı fan (VFD) | 10 - 25 (elektrik) | 5.000 - 30.000 | 1 - 2 yıl | Fan hızının kurutma yüküne göre ayarlanması; kısmi yükte büyük tasarruf |
| Nem kontrol sistemi (humidity control) | 5 - 10 | 15.000 - 50.000 | 1 - 2 yıl | Egzoz nem ölçümüne dayalı otomatik hava debisi kontrolü |
| Isı pompası entegrasyonu (heat pump integration) | 30 - 50 | 100.000 - 500.000 | 3 - 6 yıl | Düşük sıcaklıklı uygulamalarda (<80 °C) yüksek COP ile enerji geri kazanımı |
| Hava sızıntısı önleme (air leakage prevention) | 3 - 8 | 5.000 - 25.000 | 0,5 - 1,5 yıl | Tünel giriş/çıkış kapılarında hava perdesi veya sızdırmazlık sistemi |
| Güneş enerjisi ön ısıtma (solar preheating) | 5 - 15 | 20.000 - 100.000 | 3 - 5 yıl | Güneşli bölgelerde giriş havasının güneş kollektörleri ile ön ısıtılması |

### Exergy Analizi İpuçları

- Egzoz havasının exergy içeriği, sıcaklık ve nem oranına bağlıdır. Düşük sıcaklıkta bile yüksek nemli egzoz önemli exergy kaybı oluşturur.
- Tünel kurutucularda exergy yıkımı (exergy destruction) en çok ısıtma bölgesinde gerçekleşir; bu, büyük sıcaklık farkından (delta T) kaynaklanır.
- Düşük sıcaklıklı kurutma uygulamalarında (kereste, bazı gıdalar) ısı pompası kullanımı exergy verimini %5-12 aralığından %15-25 aralığına çıkarabilir.
- Bölgesel sıcaklık kontrolü, gereksiz exergy yıkımını azaltır: kurutma eğrisinin sabit hız döneminde yüksek sıcaklık, azalan hız döneminde düşük sıcaklık uygulanmalıdır.
- **Cross-equipment fırsatı:** Başka ekipmanlardan (kompresör atık ısısı, kazan baca gazı, chiller kondenser ısısı) atık ısı, tünel kurutucu giriş havasının ön ısıtılması için kullanılabilir.

## Yatırım Maliyetleri (Investment Costs)

| Kapasite (kg/h) | Tünel Uzunluğu (m) | Isıtma Gücü (kW) | Yatırım Maliyeti (€) | Yıllık Enerji Maliyeti (€/yıl)* |
|----------------:|--------------------:|------------------:|---------------------:|--------------------------------:|
| 100 - 500 | 10 - 20 | 50 - 200 | 150.000 - 400.000 | 20.000 - 80.000 |
| 500 - 2.000 | 20 - 40 | 200 - 1.000 | 400.000 - 800.000 | 80.000 - 300.000 |
| 2.000 - 5.000 | 40 - 70 | 1.000 - 3.000 | 800.000 - 1.500.000 | 300.000 - 800.000 |
| 5.000 - 10.000 | 70 - 100 | 3.000 - 5.000 | 1.500.000 - 2.500.000 | 800.000 - 1.500.000 |

> *Yıllık enerji maliyeti tahmini: doğal gaz fiyatı 0,045 €/kWh, elektrik fiyatı 0,12 €/kWh, yıllık 5.000 saat çalışma, %75 yük faktörü baz alınmıştır. 2026 yılı Avrupa piyasa koşulları.

## İlgili Dosyalar

- `knowledge/dryer/formulas.md` — Kurutma hesaplama formülleri (SMER, exergy, enerji dengesi)
- `knowledge/dryer/benchmarks.md` — Genel kurutucu benchmark değerleri
- `knowledge/dryer/solutions/exhaust_heat_recovery.md` — Egzoz ısı geri kazanım çözümleri
- `knowledge/dryer/solutions/air_recirculation.md` — Hava resirkülasyonu stratejileri
- `knowledge/dryer/sectors/ceramic_drying.md` — Seramik kurutma sektör bilgisi
- `knowledge/dryer/sectors/food_drying.md` — Gıda kurutma sektör bilgisi
- `knowledge/dryer/equipment/belt_dryer.md` — Bant kurutucu (karşılaştırma için)
- `knowledge/dryer/equipment/rotary_dryer.md` — Döner kurutucu (karşılaştırma için)
- `knowledge/dryer/solutions/temperature_optimization.md` — Sıcaklık optimizasyonu
- `knowledge/dryer/psychrometrics.md` — Psikrometrik hesaplamalar
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası entegrasyon fırsatları

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press — Kurutma teknolojileri temel referansı, Chapter 15: Tunnel Dryers.
2. Kemp, I.C. (2012). *Fundamentals of Energy Analysis of Dryers*, in Modern Drying Technology, Vol. 4, Wiley — Kurutucu enerji ve exergy analizi metodolojisi.
3. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press — İleri kurutma teknolojileri ve enerji optimizasyonu.
4. European Commission (2007). *Reference Document on Best Available Techniques in the Ceramic Manufacturing Industry (BREF)* — Seramik sektörü tünel kurutucu en iyi uygulamaları.
5. European Commission (2006). *Reference Document on Best Available Techniques in the Food, Drink and Milk Industries (BREF)* — Gıda sektörü kurutma süreçleri.
6. ASHRAE Handbook — HVAC Applications (2023), Chapter 24: Drying and Dehumidification — Kurutma sistemleri tasarım rehberi.
7. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier — Exergy analizi temel referansı.
8. Szargut, J. (2005). *Exergy Method: Technical and Ecological Applications*, WIT Press — Endüstriyel exergy analizi yöntemleri.
9. Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, McGraw-Hill, Section 12 — Kurutma mühendisliği temel bilgileri.
10. Strumillo, C. & Kudra, T. (1986). *Drying: Principles, Applications, and Design*, Gordon and Breach — Kurutma tasarım prensipleri.
