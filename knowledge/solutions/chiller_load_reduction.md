# Çözüm: Soğutma Yükü Azaltma — Cooling Load Reduction

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Aşırı soğutma yükü, chiller enerji tüketimini doğrudan artırır. Yetersiz bina yalıtımı, eski tip aydınlatma, kontrolsüz havalandırma ve güneş ısısı kazanımı, gereksiz yere yüksek soğutma talebi oluşturur. Birçok tesiste mevcut soğutma yükünün %20-40'ı uygun önlemlerle azaltılabilir niteliktedir.

**Çözüm:** Bina kabuğu iyileştirme (yalıtım, cam, gölgeleme), iç kazanç azaltma (LED aydınlatma, verimli ekipman), taze hava optimizasyonu ve talep kontrollü havalandırma (DCV), gece ön soğutma (termal kütle kullanımı) ve güneş ısısı kazanımı azaltma yoluyla soğutma talebini düşürmek.

**Tipik Tasarruf:** %10-30 (geniş değişkenlik gösterir)
**Tipik ROI:** 1-5 yıl

## Çalışma Prensibi

Soğutma yükü azaltma stratejileri, chiller'ın karşılaması gereken toplam soğutma talebini kaynağında düşürür. Toplam soğutma yükü aşağıdaki bileşenlerden oluşur:

- **Dış yükler (External loads):** Güneş ışınımı, dış hava sıcaklık farkı, infiltrasyon ve havalandırma kaynaklı ısı kazanımları
- **İç yükler (Internal loads):** Aydınlatma, ekipman (bilgisayar, motor, proses), insanlar ve nemden kaynaklanan ısı kazanımları
- **Proses yükleri:** Endüstriyel proseslerden kaynaklanan soğutma gereksinimleri

Her bileşenin azaltılması, chiller kapasitesi ve enerji tüketimini doğrudan düşürür:

```
Q_soğutma = Q_güneş + Q_iletim + Q_havalandırma + Q_infiltrasyon + Q_aydınlatma + Q_ekipman + Q_insan + Q_proses

Burada:
  Q_soğutma       = Toplam soğutma yükü [kW]
  Q_güneş         = Güneş ısısı kazanımı (camlardan ve opak yüzeylerden) [kW]
  Q_iletim        = Dış duvar ve çatıdan iletim ile ısı kazanımı [kW]
  Q_havalandırma  = Taze hava (ventilasyon) kaynaklı ısı kazanımı [kW]
  Q_infiltrasyon  = Sızma havası kaynaklı ısı kazanımı [kW]
  Q_aydınlatma    = Aydınlatma kaynaklı ısı kazanımı [kW]
  Q_ekipman       = Elektrikli ekipman kaynaklı ısı kazanımı [kW]
  Q_insan         = İnsan kaynaklı ısı kazanımı [kW]
  Q_proses        = Proses kaynaklı ısı yükü [kW]
```

### Soğutma Yükü Dağılımı (Tipik Ofis Binası)

| Yük Bileşeni | Oran (%) | Azaltılabilirlik |
|---------------|----------|-----------------|
| Güneş ısısı kazanımı (cam) | %20-30 | Yüksek (gölgeleme, film, cam değişimi) |
| Dış duvar/çatı iletimi | %10-15 | Orta (dış yalıtım) |
| Taze hava (ventilasyon) | %15-25 | Yüksek (DCV, enerji geri kazanım) |
| Aydınlatma | %15-25 | Çok yüksek (LED dönüşüm) |
| Ekipman (bilgisayar vb.) | %10-20 | Orta (verimli ekipman, yönetim) |
| İnsan | %5-10 | Düşük (çalışan sayısına bağlı) |
| İnfiltrasyon | %5-10 | Orta (sızdırmazlık) |

## Bina Kabuğu İyileştirme

### Dış Duvar Yalıtımı

Mevcut binalarda dış cephe yalıtımı (ETICS — External Thermal Insulation Composite System) ile ısı iletimi azaltılır:

| Duvar Tipi | U-değeri Mevcut (W/m²·K) | U-değeri İyileştirilmiş (W/m²·K) | Yalıtım Kalınlığı | Soğutma Yükü Azalması |
|------------|--------------------------|----------------------------------|--------------------|-----------------------|
| Tuğla (29 cm) yalıtımsız | 1.6-2.0 | 0.3-0.4 | 8-10 cm EPS/XPS | %70-80 (iletim bileşeni) |
| Beton panel yalıtımsız | 2.5-3.5 | 0.3-0.5 | 10-12 cm EPS/XPS | %80-85 (iletim bileşeni) |
| Tuğla + 3 cm eski yalıtım | 0.8-1.0 | 0.3-0.4 | 5-8 cm ek EPS/XPS | %50-60 (iletim bileşeni) |

### Cam ve Pencere İyileştirme

Pencereler, soğutma yükünün en büyük tek kaynağıdır (güneş ısısı kazanımı + iletim):

| Cam Tipi | U-değeri (W/m²·K) | SHGC (Solar Heat Gain Coeff.) | Açıklama |
|----------|-------------------|-------------------------------|----------|
| Tek cam | 5.7 | 0.86 | En kötü performans |
| Çift cam (standart) | 2.7-3.0 | 0.70-0.76 | Yaygın mevcut durum |
| Çift cam (Low-E) | 1.4-1.8 | 0.25-0.40 | İyi güneş kontrolü |
| Üçlü cam (Low-E, argon) | 0.7-1.0 | 0.20-0.35 | Yüksek performans |
| Çift cam + güneş filmi | 2.5-2.8 | 0.20-0.35 | Mevcut cama retrofit |

### Güneş Gölgeleme Sistemleri

- **Dış gölgeleme (sabit):** Yatay veya dikey kanatlar, pergola; güneş ısısını %60-80 azaltır
- **Dış gölgeleme (hareketli):** Otomatik panjur, tente; güneş ısısını %70-90 azaltır
- **Güneş kontrol filmi:** Mevcut camlara uygulanır; SHGC değerini %40-60 düşürür
- **Elektrokromik cam:** Şeffaflığı otomatik ayarlanır; SHGC 0.09-0.46 arasında değişir (ileri teknoloji)

## İç Kazanç Azaltma

### LED Aydınlatma Dönüşümü

Aydınlatma hem elektrik hem soğutma yükünü etkiler; her 1 kW aydınlatma tasarrufu, yaklaşık 0.3-0.4 kW ek soğutma tasarrufu sağlar:

| Aydınlatma Tipi | Güç Yoğunluğu (W/m²) | LED Sonrası (W/m²) | Tasarruf |
|-----------------|-----------------------|---------------------|---------|
| Floresan T8 (eski) | 15-20 | 5-8 | %55-70 |
| Floresan T5 | 10-14 | 5-8 | %35-50 |
| Halojen spot | 20-30 | 4-8 | %70-80 |
| Metal halide (endüstriyel) | 12-18 | 4-8 | %55-70 |

```
Aydınlatma_tasarrufu_kW = Alan × (Güç_eski - Güç_yeni) / 1000
Soğutma_tasarrufu_kW = Aydınlatma_tasarrufu_kW × (1/COP + 1) × (1/COP) × COP
Soğutma_tasarrufu_kW ≈ Aydınlatma_tasarrufu_kW / COP_chiller

Burada:
  Alan           = Aydınlatılan alan [m²]
  Güç_eski       = Mevcut aydınlatma güç yoğunluğu [W/m²]
  Güç_yeni       = LED aydınlatma güç yoğunluğu [W/m²]
  COP_chiller    = Chiller performans katsayısı [-]
```

### Ekipman Verimliliği

- **Bilgisayar yönetimi:** Uyku modu politikası, ince istemci (thin client) kullanımı; bilgisayar başına 50-150 W tasarruf
- **Sunucu odası optimizasyonu:** Sıcak/soğuk koridor ayrımı, free cooling, virtualizasyon
- **Verimli elektrik motorları:** IE3/IE4 motorlar, VSD uygulamaları

## Taze Hava Optimizasyonu ve Talep Kontrollü Havalandırma (DCV)

### Taze Hava Soğutma Yükü

```
Q_ventilasyon = ṁ_hava × (h_dış - h_iç)

Burada:
  Q_ventilasyon  = Taze hava kaynaklı soğutma yükü [kW]
  ṁ_hava         = Taze hava kütle debisi [kg/s]
  h_dış          = Dış hava entalpisi [kJ/kg]
  h_iç           = İç hava entalpisi [kJ/kg]
```

### Talep Kontrollü Havalandırma (DCV)

CO₂ sensörleri ile iç mekan hava kalitesini izleyerek taze hava miktarını gerçek ihtiyaca göre ayarlar:

| Parametre | Sabit Havalandırma | DCV ile | Tasarruf |
|-----------|-------------------|---------|----------|
| Taze hava oranı (kişi başı) | 10-15 L/s (sabit) | 5-15 L/s (değişken) | %20-50 |
| CO₂ seviyesi | 400-600 ppm (aşırı havalandırma) | 600-1000 ppm (kontrollü) | — |
| Taze hava soğutma yükü | %100 (referans) | %50-80 | %20-50 |
| Yıllık enerji tasarrufu | — | — | %10-25 (toplam HVAC) |

### Enerji Geri Kazanım Sistemi (Heat Recovery Ventilation)

Egzoz havasından ısıyı taze havaya aktararak soğutma (ve ısıtma) yükünü azaltır:

| Tip | Verimlilik (Sensible) | Verimlilik (Total) | Maliyet |
|-----|----------------------|--------------------|---------|
| Plakalı (cross-flow) | %50-70 | — | Düşük |
| Döner (enthalpy wheel) | %70-85 | %60-80 | Orta |
| Isı borusu (heat pipe) | %45-65 | — | Orta |
| Run-around coil | %40-55 | — | Yüksek (uzun mesafe) |

## Gece Ön Soğutma (Night Pre-Cooling)

Gece saatlerinde düşük dış hava sıcaklığından yararlanarak bina termal kütlesini (beton döşemeler, duvarlar) soğutma:

- **Prensip:** Gece 02:00-06:00 arası free cooling ile bina iç sıcaklığını 20-22°C'ye düşürme; termal kütle gündüz ısı kazanımlarını absorbe eder
- **Uygun bina tipleri:** Ağır yapı (beton), iyi yalıtımlı, düşük infiltrasyonlu
- **Potansiyel:** Pik soğutma yükünü %10-30 azaltır
- **Sınırlama:** Gece-gündüz sıcaklık farkı en az 8-10°C olmalı
- **Kontrol:** Dış hava sıcaklığı sensörü, zaman programı, iç sıcaklık alt limiti (18°C)

## Güneş Isısı Kazanımı Azaltma

### Güneş Filmi Uygulaması

Mevcut camlara güneş kontrol filmi uygulanması en düşük maliyetli retrofit çözümüdür:

| Film Tipi | Görünür Geçirgenlik | SHGC Azalması | Ömür | Maliyet (€/m²) |
|-----------|--------------------|--------------|----- |-----------------|
| Reflektif (gümüş) | %15-25 | %50-65 | 10-15 yıl | 25-40 |
| Seçici (spectrally selective) | %50-70 | %30-50 | 10-15 yıl | 35-60 |
| Seramik (nano-ceramic) | %60-80 | %30-45 | 15-20 yıl | 50-80 |
| Düşük yayımlı (Low-E retrofit) | %60-75 | %25-40 | 10-15 yıl | 40-70 |

### Dış Gölgeleme Sistemleri

| Sistem | Güneş Isısı Azaltma | Maliyet (€/m² cam alanı) | Avantaj/Dezavantaj |
|--------|---------------------|--------------------------|--------------------|
| Sabit yatay kanat | %40-60 | 50-120 | Bakımsız, güney cephe için ideal |
| Hareketli panjur (manuel) | %60-80 | 80-180 | Esnek, kullanıcı müdahalesi gerekir |
| Otomatik panjur/jaluzi | %70-90 | 150-350 | Otomatik kontrol, yüksek verim |
| Dış stor perde | %60-80 | 60-150 | Ekonomik, rüzgar dayanımı sınırlı |

## Proses Soğutma Yükü Optimizasyonu

Endüstriyel tesislerde proses kaynaklı soğutma yükü büyük pay tutar:

- **İzolasyon:** Soğutma gerektiren proses hatlarının ve ekipmanların yalıtılması
- **Proses sıcaklık optimizasyonu:** Gereksiz yere düşük sıcaklık gereksinimine müdahale
- **Atık ısı yönetimi:** Sıcak proses ekipmanlarından yayılan ısının lokal egzoz ile uzaklaştırılması
- **Üretim planlaması:** Isı üreten proseslerin yoğun soğutma saatleri dışına kaydırılması

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı

- Bina soğutma yükü tasarım kapasitesine yakın veya aşıyorsa
- Chiller enerji maliyeti yıllık €50,000'nin üzerindeyse
- Bina kabuğu eski ve yalıtımsızsa (1990 öncesi yapılar)
- Aydınlatma sistemi floresan T8 veya daha eski teknoloji ise
- Taze hava oranı sabit ve yüksekse (DCV yoksa)
- Güneş ışınımına maruz cam alanı geniş ve gölgelemesizse
- Chiller kapasite artışı planlanıyorsa (yük azaltma ile kaçınılabilir)

### Ne Zaman Uygulanmamalı

- Bina zaten yüksek performanslı cepheye sahipse (U<0.4, Low-E cam)
- Soğutma yükünün büyük bölümü prosesten geliyorsa ve değiştirilemiyorsa
- Bina kısa vadede yıkılacak veya köklü renovasyona girecekse

## Yatırım Maliyeti

| Uygulama | Maliyet (€) | Tasarruf Potansiyeli | ROI |
|----------|-------------|---------------------|-----|
| LED aydınlatma dönüşümü (ofis 5,000 m²) | 5,000-50,000 | %15-25 (aydınlatma + soğutma) | 1-3 yıl |
| Güneş kontrol filmi (1,000 m² cam) | 25,000-80,000 | %5-15 (güneş yükü azalması) | 2-5 yıl |
| Dış gölgeleme sistemi (sabit) | 10,000-100,000 | %10-20 (güneş yükü azalması) | 3-7 yıl |
| DCV sistemi (10 AHU) | 10,000-50,000 | %10-25 (taze hava yükü azalması) | 2-4 yıl |
| Enerji geri kazanım (enthalpy wheel) | 15,000-60,000 | %15-30 (taze hava yükü azalması) | 2-5 yıl |
| Dış cephe yalıtımı (2,000 m²) | 50,000-150,000 | %5-15 (iletim yükü azalması) | 5-10 yıl |
| Cam değişimi (Low-E çift cam, 500 m²) | 75,000-200,000 | %15-25 (güneş + iletim) | 7-12 yıl |

## ROI Hesabı

### Formül

```
Soğutma_yükü_azalması_kW = Q_mevcut × Azalma_oranı / 100
Elektrik_tasarrufu_kW = Soğutma_yükü_azalması_kW / COP_chiller
Yıllık_tasarruf_kWh = Elektrik_tasarrufu_kW × Eşdeğer_tam_yük_saat
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Toplam_yatırım / Yıllık_tasarruf_EUR
```

Burada:
- `Q_mevcut`: Mevcut toplam soğutma yükü [kW]
- `Azalma_oranı`: Uygulama ile sağlanan soğutma yükü azalma oranı [%]
- `COP_chiller`: Chiller ortalama COP değeri [-]
- `Eşdeğer_tam_yük_saat`: Yıllık soğutma eşdeğer tam yük saat [saat/yıl]
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap — LED Aydınlatma + DCV Kombinasyonu

- 10,000 m² ofis binası, mevcut toplam soğutma yükü: 800 kW
- Chiller COP: 5.5
- Yıllık eşdeğer tam yük saat: 2,500 saat
- Elektrik fiyatı: €0.12/kWh

**LED aydınlatma dönüşümü:**

```
Aydınlatma_tasarrufu = 10,000 × (16 - 7) / 1000 = 90 kW (elektrik)
Soğutma_yükü_azalması = 90 × 0.9 = 81 kW (iç kazanç azalması, %90 kullanım faktörü)
Chiller_tasarrufu = 81 / 5.5 = 14.7 kW
Toplam_elektrik_tasarrufu = 90 + 14.7 = 104.7 kW
Yıllık_tasarruf = 104.7 × 2,500 × 0.12 = €31,410/yıl
LED_yatırım = €40,000
Geri_ödeme = 40,000 / 31,410 = 1.27 yıl
```

**DCV sistemi:**

```
Taze_hava_yük_azalması = 800 × 0.20 × 0.35 = 56 kW (taze hava payı %20, %35 azaltma)
Chiller_tasarrufu = 56 / 5.5 = 10.2 kW
Yıllık_tasarruf = 10.2 × 2,500 × 0.12 = €3,060/yıl
DCV_yatırım = €25,000
Geri_ödeme = 25,000 / 3,060 = 8.2 yıl (daha uzun ROI, ancak hava kalitesi faydası ek değer)
```

**Not:** DCV sisteminin hava kalitesi iyileştirme ve ısıtma sezonu tasarrufu gibi ek faydaları ROI hesabına dahil değildir; bu faydalarla gerçek geri ödeme süresi 3-4 yıla düşebilir.

## Uygulama Adımları

1. **Soğutma yükü analizi:** Mevcut soğutma yükünü bileşenlerine ayır (güneş, iletim, havalandırma, aydınlatma, ekipman). Bina enerji simülasyonu (EnergyPlus, DesignBuilder) veya hesap tablosu yöntemi kullan
2. **En büyük yük bileşenlerini belirle:** Pareto analizi ile en etkili müdahale alanlarını seç
3. **Fizibilite çalışması:** Her müdahale için teknik uygunluk, yatırım maliyeti ve tasarruf potansiyelini hesapla
4. **Önceliklendirme:** En düşük ROI'ye sahip uygulamalardan başla (genellikle LED → DCV → güneş filmi → gölgeleme → yalıtım)
5. **LED aydınlatma dönüşümü:** Aydınlatma envanteri çıkar, LED eşdeğerlerini seç, pilot uygulama yap
6. **DCV sistemi kurulumu:** CO₂ sensörleri yerleştir, AHU fan ve damper kontrolünü entegre et
7. **Güneş kontrol önlemleri:** Cam yüzeylerini analiz et, uygun film veya gölgeleme sistemi seç ve uygula
8. **Enerji geri kazanım:** Mevcut AHU'lara heat recovery entegrasyonu değerlendir
9. **Performans doğrulama:** Uygulama sonrası soğutma yükünü ölç ve karşılaştır, M&V protokolü uygula
10. **Sürekli izleme:** BMS üzerinden soğutma yükü trendini takip et, mevsimsel optimizasyon yap

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Konfor şikayetleri | Aşırı tasarruf odaklı yaklaşım iç mekan konforunu bozabilir | Sıcaklık ve nem setpoint'lerini koruma, kullanıcı geri bildirimi |
| Havalandırma yetersizliği | DCV ile taze hava aşırı kısılması iç hava kalitesini düşürür | CO₂ üst limiti 1000 ppm, minimum taze hava oranı ASHRAE 62.1'e uyum |
| Gün ışığı kaybı | Güneş filmi ve gölgeleme aydınlık seviyesini düşürür | Görünür geçirgenliği yeterli film seçimi (%50+), aydınlatma kontrolü ile entegrasyon |
| Nem kontrolü | DCV ile taze hava azaltıldığında nemden arındırma kapasitesi değişir | Nem sensörü ile kontrol, by-pass damper, minimum taze hava modu |
| Yanlış boyutlandırma | Yük azaltma sonrası chiller aşırı kapasiteli kalır, düşük yükte çalışır | Chiller staging ve VSD optimizasyonu ile düşük yükte verim artırma |
| Uygulama sıralaması | Yanlış önceliklendirme yatırım etkinliğini düşürür | En düşük ROI'den başla, paket uygulamalar değerlendir |
| Bina fiziği hataları | Yanlış yalıtım uygulaması nem yoğuşmasına neden olabilir | Buhar bariyeri analizi, detay çözümü, uzman danışmanlık |

## İlgili Dosyalar

- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller bakım: `solutions/chiller_maintenance.md`
- Delta-T optimizasyonu: `solutions/chiller_delta_t.md`
- Termal depolama: `solutions/chiller_thermal_storage.md`
- Isı geri kazanım: `solutions/chiller_heat_recovery.md`

## Referanslar

- ASHRAE Handbook — Fundamentals, Chapter 18: "Nonresidential Cooling and Heating Load Calculations"
- ASHRAE Standard 90.1, "Energy Standard for Buildings Except Low-Rise Residential Buildings"
- ASHRAE Standard 62.1, "Ventilation for Acceptable Indoor Air Quality"
- CIBSE Guide A, "Environmental Design" — Cooling Load Calculations
- DOE/EERE, "Advanced Energy Retrofit Guides — Office Buildings and K-12 Schools"
- EN 15232, "Energy Performance of Buildings — Impact of Building Automation, Controls and Building Management"
- Türkiye Bina Enerji Performansı Yönetmeliği (BEP-TR)
- IEA, "Energy Efficiency in Buildings — Heating and Cooling Equipment"
- Lawrence Berkeley National Laboratory, "Cool Roofs and Cool Pavements Toolkit"
- Türkiye Enerji Verimliliği Derneği (ENVER), "Binalarda Enerji Verimliliği Rehberi"
