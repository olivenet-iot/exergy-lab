# Dalgıç Pompa — Submersible Pump

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Kinetik (santrifüj), çok kademeli, motor-pompa entegre
- Alt tipler: Kuyu pompası (deep well), drenaj (dewatering), atıksu (sewage/wastewater)
- Kapasite aralığı: 1 - 1,000+ m³/h
- Head / derinlik aralığı: 10 - 500+ m
- Motor ve pompa birlikte sıvı içine daldırılır
- Yaygın markalar: Grundfos (SP, SE, SEG), KSB (UPA, Amarex), Wilo (TWU, Rexa), Xylem/Goulds (GS, Flygt), Lowara (GS), Caprari (E6, E8)

## Çalışma Prensibi
Dalgıç pompalarda motor ve pompa tek bir ünite olarak sıvı içine yerleştirilir. Motor altta, pompa üstte konumlanır. Çok kademeli santrifüj impellerlar sıvıyı yukarı doğru iter. Motor, suya dayanıklı (hermetically sealed) olarak tasarlanmıştır ve elektrik enerjisi yüzeyden kablo ile iletilir.

### Temel Bileşenler
- **Dalgıç motor (Submersible Motor):** Su dolu veya yağ dolu, genellikle sincap kafesli (squirrel cage) asenkron motor
- **Çok kademeli pompa (Multi-stage Pump):** 2-50+ kademe, her kademe 5-15 m head üretir
- **Emme ızgarası (Suction Strainer):** Katı parçacıkların pompaya girmesini önler
- **Güç kablosu (Power Cable):** Yüzeyden motora elektrik iletimi; uzunluk derinliğe bağlı
- **Çekvalf (Check Valve):** Pompanın durması durumunda su geri akışını önler
- **Motor koruma cihazı (Motor Protection Unit):** Aşırı akım, kuru çalışma, faz kaybı koruması

### Motor Soğutma Mekanizması
- Dalgıç motorlar pompalanan sıvı tarafından soğutulur
- Motor üzerinden geçen minimum su hızı gereklidir (tipik >0.15 m/s)
- Kuyu pompalarında motor çapı kuyu çapından küçük olmalı — aradaki boşluktan su geçerek soğutma sağlanır
- Soğutma yetersizse motor sıcaklığı artar → izolasyon ömrü kısalır, arıza riski yükselir

## Alt Tipler

### 1. Kuyu Pompası (Deep Well Submersible)
- Dar gövde (4", 6", 8", 10", 12" çap)
- Çok kademeli (10-50+ kademe)
- Temiz su uygulamaları: içme suyu, sulama, endüstriyel su temini
- Derinlik: 20-500+ m
- Verimlilik: %60-82 (boyut ve kademe sayısına bağlı)

### 2. Drenaj Pompası (Dewatering)
- Geniş gövde, tek veya az kademeli
- Şantiye su boşaltma, maden drenajı, sel suyu tahliyesi
- Katı geçirgenlik: 10-50+ mm
- Verimlilik: %50-70

### 3. Atıksu Pompası (Sewage / Wastewater)
- Özel impeller: vortex, kanal tipi (channel), kesicili (grinder)
- Çamur ve katı madde içeren sıvılar
- Verimlilik: %40-65 (kirli su impeller geometrisi nedeniyle)
- Önemli: Serbest geçiş çapı (free passage) belirtilir

## Enerji Dağılımı (Tipik — Kuyu Pompası)
- Faydalı hidrolik iş: ~55-75%
- Hidrolik kayıplar (impeller, difüzör, giriş/çıkış): ~10-20%
- Motor kayıpları (bakır, demir, sürtünme): ~10-18%
- Kablo kayıpları (I²R): ~1-5% (derinliğe bağlı)
- Mekanik kayıplar (yatak, eksenel yük): ~2-5%

## Kablo Kayıpları (I²R Kayıp)

Dalgıç pompalarda kablo uzunluğu önemli bir enerji kaybı kaynağıdır:

```
P_cable_loss = I² × R_cable
R_cable = ρ_conductor × L / A
```

| Derinlik (m) | Kablo Uzunluğu (m) | Tipik Kablo Kaybı (%) | Not |
|-------------|--------------------|-----------------------|-----|
| 20-50 | 25-60 | %0.5-1.5 | İhmal edilebilir |
| 50-150 | 60-170 | %1.5-3.0 | Dikkate alınmalı |
| 150-300 | 170-350 | %3.0-5.0 | Kablo kesiti artırılmalı |
| >300 | >350 | %5.0-8.0+ | Kritik — büyük kesit veya yüksek gerilim |

Kablo kaybını azaltma yöntemleri:
- Daha büyük kesitli kablo kullanımı
- Yüksek gerilimli motor seçimi (400V yerine 690V veya 1000V+)
- Kablonun doğru boyutlandırılması (voltage drop <%3 hedef)

## Wire-to-Water Verimlilik

```
η_wire-to-water = η_cable × η_motor × η_pump
η_wire-to-water = (1 - P_cable_loss/P_input) × η_motor × η_pump
```

## Verimlilik Benchmarkları

| Pompa Tipi / Boyut | Düşük | Ortalama | İyi | Best-in-class |
|--------------------|-------|----------|-----|---------------|
| Kuyu 4" (<5 kW) | <%50 | %50-60 | %60-70 | >%70 |
| Kuyu 6" (5-30 kW) | <%60 | %60-70 | %70-78 | >%78 |
| Kuyu 8" (30-100 kW) | <%65 | %65-75 | %75-82 | >%82 |
| Kuyu 10-12" (>100 kW) | <%70 | %70-78 | %78-85 | >%85 |
| Drenaj | <%45 | %45-55 | %55-65 | >%65 |
| Atıksu | <%35 | %35-50 | %50-60 | >%60 |

Not: Değerler wire-to-water verimi (kablo kaybı dahil değil) olarak verilmiştir.

## Kum ve Korozyon Etkileri
- **Kum:** Kuyudaki kum impeller ve difüzör aşınmasına neden olur → verim düşer, ömür kısalır
  - Kum toleransı: Max 50 g/m³ (standart), max 300 g/m³ (aşınmaya dayanıklı malzeme ile)
  - Aşınmaya dayanıklı malzemeler: SiC (silikon karbür) yatak, AISI 904L veya duplex paslanmaz çelik
- **Korozyon:** Agresif su kimyası (yüksek klorür, düşük pH) motor ve pompa gövdesini etkiler
  - Standart: AISI 304 paslanmaz çelik
  - Korozif ortam: AISI 316L, duplex 2205, süper duplex 2507

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (yüzeyde) | kW | 0.5-500 | Güç analizörü (pano çıkışı) |
| Basma basıncı (yüzeyde) | bar | 1-50 | Basınç sensörü |
| Debi | m³/h | 1-1000+ | Flowmeter (yüzeyde) |
| Statik su seviyesi | m | 5-300+ | Su seviye ölçer |
| Dinamik su seviyesi (pompaj sırasında) | m | 10-400+ | Su seviye ölçer |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Motor akımı | A | Etiket değerine göre | Pens ampermetre |
| Motor sıcaklığı | °C | 30-90 | Dahili sıcaklık sensörü (varsa) |
| Kum içeriği | g/m³ | 0-300 | Filtre ağırlık ölçümü |
| Gerilim (motor terminalinde) | V | 380-1000 | Voltmetre |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç |
| İzolasyon direnci | MΩ | >20 | Megger test |

### Nameplate Bilgileri
- Marka ve model (örn. Grundfos SP 77-3)
- Nominal güç (kW)
- Nominal debi (m³/h)
- Nominal head (m)
- Kademe sayısı
- Motor gerilimi (V) ve akımı (A)
- Kuyu çapı (inç)
- Minimum kuyu çapı gereksinimi
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Sıvı yoğunluğu | 1000 kg/m³ | Temiz su varsayımı |
| Kablo kaybı | %3 | 100-200 m derinlik ortalaması |
| Motor verimi | %85 | Dalgıç motor standart (aboveground motordan düşük) |
| Pompa verimi | %70 | Orta boy kuyu pompası ortalaması |
| Wire-to-water verim | %58 | Kablo + motor + pompa çarpımı |
| Yük oranı | %80 | Genellikle sabit yükte çalışır |
| Çalışma saati | 4000 saat/yıl | Sulama uygulaması |
| cosφ (güç faktörü) | 0.82 | Dalgıç motorlarda biraz düşük |
| Statik/dinamik seviye farkı (drawdown) | 10 m | Orta kapasiteli kuyu |

## Exergy Verimi Hesabı

```
Ė_electric_input = P_measured_at_surface  (yüzeyde ölçülen elektrik gücü)
P_cable_loss = I² × R_cable  (kablo kaybı)
P_motor_input = P_measured - P_cable_loss
P_hydraulic = ρ × g × H_total × Q / 3600

η_exergy = P_hydraulic / P_measured_at_surface
```

Burada H_total = statik seviye + dinamik düşüm (drawdown) + sürtünme kayıpları + çıkış basıncı yüksekliği.

Dalgıç pompalarda kablo kaybı ek bir exergy yıkım kaynağıdır — santrifüj pompalarda bulunmayan bu kayıp derin kuyu uygulamalarında anlamlı boyuta ulaşabilir.

## VSD Uygulaması (Dalgıç Pompalarda)
- Kuyu seviyesine göre debi ayarı yapılabilir
- VSD çıkış kablosu harmonik ve EMI içerir → özel kablo (shielded, VFD-rated) gerekli
- VSD-motor mesafesi arttıkça kablo kayıpları artar → VSD mümkünse kuyu başına yakın konumlandırılmalı
- dU/dt filtresi veya sinüs filtresi motor izolasyonunu korur
- Enerji tasarrufu: Değişken su seviyeli uygulamalarda %15-30 tasarruf potansiyeli

## Dikkat Edilecekler

1. **Kuru çalışma koruması:** Motor soğutması akan suya bağlıdır — su seviyesi düşerse motor yanar; seviye sensörü veya akım koruması zorunlu
2. **Kablo boyutlandırma:** Yetersiz kablo kesiti → voltaj düşümü → motor verimsiz çalışır veya hasar görür; <%3 voltage drop hedeflenmelidir
3. **Kum etkisi:** Kumlu kuyularda impeller ve yatak aşınması %10-25 verim kaybına yol açar — periyodik verim testi önerilir
4. **Minimum debi:** Çok düşük debide motor soğuması yetersiz kalır — minimum debi değerinin altında çalıştırılmamalı
5. **Korozyon:** Su kimyası (pH, klorür, H₂S) pompa malzeme seçimini belirler — yanlış malzeme erken arızaya neden olur
6. **Yaşlanma etkisi:** 10+ yıllık pompalarda %15-30 verim kaybı beklenir — enerji maliyeti karşılaştırması ile yenileme değerlendirilmeli
7. **İzolasyon direnci:** Periyodik megger testi ile motor izolasyonu kontrol edilmeli — düşük direnç arıza habercisi

## İlgili Dosyalar
- Santrifüj pompa genel: `equipment/pump_centrifugal.md`
- Dikey türbin pompa: `equipment/pump_vertical_turbine.md`
- VSD uygulaması: `solutions/pump_vsd.md`
- Benchmark verileri: `benchmarks/pump_benchmarks.md`
- Exergy hesaplamaları: `formulas/pump_exergy.md`

## Referanslar
- Grundfos SP Series Engineering Manual & Submersible Pump Handbook
- KSB UPA Submersible Pump Technical Documentation
- Hydraulic Institute Standards (ANSI/HI 2.1-2.2 — Submersible Pump Tests)
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Water Well Journal, "What Actually Is Wire-to-Water Efficiency?"
- Gülich, J.F., "Centrifugal Pumps," Springer — Submersible Pump Chapter
- ISO 9906:2012 — Rotodynamic Pumps — Hydraulic Performance Acceptance Tests
