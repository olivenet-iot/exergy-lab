---
title: "Pistonlu Kompresörlü Chiller — Reciprocating Compressor Chiller"
category: equipment
equipment_type: chiller
subtype: "Pistonlu Chiller"
keywords: [pistonlu chiller, reciprocating, küçük kapasite]
related_files: [chiller/benchmarks.md, chiller/formulas.md, chiller/solutions/maintenance.md]
use_when: ["Pistonlu chiller analizi yapılırken", "Küçük kapasite soğutma değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Pistonlu Kompresörlü Chiller — Reciprocating Compressor Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı soğutma çevrimi — pistonlu (reciprocating) kompresör
- Kapasite aralığı: 10 - 500 kW (3 - 142 ton)
- Soğutucu akışkan: R-134a, R-407C, R-410A, R-513A (yeni nesil düşük GWP)
- COP aralığı (su soğutmalı kondenser): 4.0 - 5.5
- COP aralığı (hava soğutmalı kondenser): 2.0 - 3.2
- Ekserji verimi: %15 - 35
- Kompresör tipi: Yarı hermetik veya açık tip pistonlu
- Silindir sayısı: 2, 4, 6, 8 veya 12
- Yaygın markalar: Bitzer, Copeland (Emerson), Carrier (eski modeller), Dorin, Frascold, RefComp
- Güncel durum: Yeni tesislerde büyük ölçüde scroll ve vidalı (screw) kompresörler tarafından ikame edilmiştir; mevcut tesislerde hâlâ yaygındır

## Çalışma Prensibi

Pistonlu kompresör, silindir içinde ileri-geri hareket eden bir piston ile soğutucu akışkanı sıkıştırır. Çalışma döngüsü dört aşamadan oluşur:

1. **Emme (Suction):** Piston aşağı hareket eder, emme vanası açılır, düşük basınçlı soğutucu akışkan gaz silindire çekilir
2. **Sıkıştırma (Compression):** Piston yukarı hareket eder, her iki vana kapalıdır, gaz sıkıştırılarak basınç ve sıcaklığı artar
3. **Basma (Discharge):** Basınç yükselince basma vanası açılır, yüksek basınçlı sıcak gaz kondensere gönderilir
4. **Genleşme (Re-expansion):** Ölü hacimde (clearance volume) kalan az miktarda gaz genleşir — bu hacim volumetrik verimi düşürür

### Temel Bileşenler
- **Piston ve silindir:** Sıkıştırma elemanları; aşınma en çok bu bölgede gerçekleşir
- **Emme ve basma vanaları (reed valves):** Otomatik açılan/kapanan çelik lameller; arıza halinde verim ciddi düşer
- **Krank mili (crankshaft):** Dönme hareketini ileri-geri harekete çevirir
- **Yağ pompası:** Yataklar, piston segmanları ve mekanik conta yağlaması için
- **Unloader mekanizması:** Kapasite kontrolü için silindir devre dışı bırakma sistemi

### Kapasite Kontrol Yöntemleri

| Yöntem | Açıklama | Verim Etkisi |
|--------|----------|--------------|
| Silindir devre dışı bırakma (Cylinder Unloading) | Emme vanası açık tutularak silindir pasif yapılır | İyi — kademeli kontrol |
| Hot gas bypass | Basma gazının bir kısmı emme tarafına aktarılır | Kötü — enerji israfı |
| Hız kontrolü (VSD) | Motor devri değiştirilerek kapasite ayarlanır | Çok iyi — sürekli kontrol |
| On/Off çalışma | Kompresör açılıp kapatılır | Orta — sık start/stop ömrü kısaltır |

Silindir devre dışı bırakma en yaygın yöntemdir. 4 silindirli bir kompresör %25, %50, %75, %100 kademelerinde çalışabilir. Bu kesikli (discrete) kapasite kontrolü, kısmi yüklerde iyi performans sağlar.

## Enerji Dağılımı (Tipik — Su Soğutmalı, Tam Yük)

| Enerji Akışı | Oran (%) | Açıklama |
|---------------|----------|----------|
| Evaporatörde alınan ısı (soğutma etkisi) | 75 - 82 | Faydalı soğutma |
| Kompresör iş girdisi | 18 - 25 | Elektrik enerjisi |
| Kondenserde atılan ısı | 100 | Q_evap + W_comp |
| Mekanik kayıplar (sürtünme, yağlama) | 3 - 6 | Piston, segment, yatak sürtünmesi |
| Elektrik motor kayıpları | 3 - 8 | Motor verimi %92-97 |
| Vana basınç düşüşü kayıpları | 2 - 4 | Emme/basma vanaları |
| Ölü hacim kayıpları (re-expansion) | 3 - 8 | Volumetrik verim düşüşü |

## Kısmi Yük Performansı (Silindir Unloading ile)

| Yük Oranı (%) | Aktif Silindir (4 silindirli) | COP / COP_tam_yük (%) | Güç Tüketimi (%) |
|----------------|-------------------------------|------------------------|-------------------|
| 100 | 4/4 | 100 | 100 |
| 75 | 3/4 | 95 - 100 | 72 - 78 |
| 50 | 2/4 | 85 - 95 | 48 - 55 |
| 25 | 1/4 | 65 - 80 | 28 - 38 |

Silindir unloading ile kısmi yük performansı oldukça iyidir. %50 yükte bile COP, tam yük değerinin %85-95'ini koruyabilir. Bu özellik pistonlu kompresörlerin en önemli avantajlarından biridir.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (kompresör) | kW | 3 - 150 | Güç analizörü |
| Soğuk su giriş sıcaklığı (evaporatör) | °C | 10 - 16 | PT100 sensör |
| Soğuk su çıkış sıcaklığı (evaporatör) | °C | 5 - 9 | PT100 sensör |
| Soğuk su debisi | m³/h | Kapasiteye bağlı | Ultrasonik debimetre |
| Kondenser giriş suyu sıcaklığı (su soğutmalı) | °C | 28 - 35 | PT100 sensör |
| Kondenser çıkış suyu sıcaklığı (su soğutmalı) | °C | 33 - 40 | PT100 sensör |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Emme basıncı (suction) | bar | 2 - 5 | Manometre / basınç transdüseri |
| Basma basıncı (discharge) | bar | 10 - 20 | Manometre / basınç transdüseri |
| Emme gazı sıcaklığı (superheat) | °C | 5 - 15 (superheat) | Termokupl |
| Yağ basıncı | bar | 2 - 6 (diferansiyel) | Basınç göstergesi |
| Yağ sıcaklığı | °C | 40 - 70 | Termometre |
| Titreşim seviyesi | mm/s | <7.1 (ISO 10816) | Titreşim sensörü |
| Motor akımı | A | Motor etiketine göre | Pens ampermetre |
| Ortam sıcaklığı (hava soğutmalı ise) | °C | 20 - 45 | Termometre |
| Kondenser su debisi | m³/h | Kapasiteye bağlı | Ultrasonik debimetre |
| Aktif silindir sayısı | — | 1 - 12 | Kontrolörden okuma |
| Çalışma saati | saat/yıl | 2,000 - 6,000 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. Bitzer 4HE-18Y)
- Nominal soğutma kapasitesi (kW veya ton)
- Nominal elektrik gücü (kW)
- Soğutucu akışkan tipi ve şarj miktarı (kg)
- Silindir sayısı ve hacmi (cm³)
- Nominal COP veya EER
- Maksimum çalışma basınçları (bar)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Soğuk su giriş sıcaklığı | 12°C | Konfor soğutma varsayımı |
| Soğuk su çıkış sıcaklığı | 7°C | Standart chiller çıkışı |
| Kondenser su giriş sıcaklığı | 30°C | Su soğutmalı, yaz koşulu |
| Kondenser su çıkış sıcaklığı | 35°C | 5°C kondenser yaklaşımı |
| Ortam sıcaklığı (hava soğutmalı) | 35°C | Yaz tasarım koşulu |
| COP (su soğutmalı) | 4.5 | Orta kapasite, tam yük |
| COP (hava soğutmalı) | 2.8 | Orta kapasite, 35°C ortam |
| Ekserji verimi | %22 | Ortalama çalışma koşulları |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa (1 atm) | Standart ölü durum |
| Çalışma saati | 3,000 saat/yıl | Türkiye, ticari soğutma |
| Yük oranı (ortalama) | %65 | Mevsimsel ortalama |
| Motor verimi | %92 | Yarı hermetik kompresör |

## Performans Tablosu

### Kapasite ve COP Değerleri (Tam Yük, Standart Koşullar)

| Kapasite (kW) | Silindir | COP (Su Soğutmalı) | COP (Hava Soğutmalı) | Ekserji Verimi (%) | Tipik Uygulama | Yaklaşık Fiyat (€) |
|---------------|----------|---------------------|----------------------|---------------------|----------------|---------------------|
| 10 - 30 | 2 | 3.8 - 4.2 | 2.0 - 2.5 | 15 - 20 | Küçük ticari | 3,000 - 8,000 |
| 30 - 80 | 4 | 4.0 - 4.8 | 2.3 - 2.8 | 18 - 25 | Orta ticari, otel | 7,000 - 18,000 |
| 80 - 200 | 6 | 4.2 - 5.0 | 2.5 - 3.0 | 20 - 30 | Endüstriyel, AVM | 15,000 - 40,000 |
| 200 - 350 | 8 | 4.5 - 5.3 | 2.7 - 3.1 | 22 - 32 | Büyük endüstriyel | 35,000 - 70,000 |
| 350 - 500 | 12 | 4.5 - 5.5 | 2.8 - 3.2 | 25 - 35 | Büyük endüstriyel | 60,000 - 120,000 |

### Ekserji Verimi Hesabı

```
COP = Q_evap / W_comp

η_Carnot = T_cold / (T_hot - T_cold)

η_exergy = COP / COP_Carnot × 100

Burada:
  Q_evap     : Evaporatörde alınan ısı — soğutma kapasitesi (kW)
  W_comp     : Kompresör elektrik gücü (kW)
  COP        : Soğutma performans katsayısı (—)
  T_cold     : Evaporatör soğuk su ortalama sıcaklığı (K)
  T_hot      : Kondenser sıcak su/hava ortalama sıcaklığı (K)
  COP_Carnot : Tersinir (ideal) Carnot COP değeri (—)
  η_exergy   : Ekserji verimi (%)
  T₀         : Referans çevre sıcaklığı = 25°C (298.15 K)
```

Örnek hesaplama (su soğutmalı, 100 kW):

```
T_cold = (12 + 7) / 2 + 273.15 = 282.65 K
T_hot  = (30 + 35) / 2 + 273.15 = 305.65 K
COP_Carnot = 282.65 / (305.65 - 282.65) = 12.29
COP_gerçek = 4.5
η_exergy = 4.5 / 12.29 × 100 = %36.6

Burada:
  Bu değer üst sınıra yakındır; ortalama tesislerde %20-28 arasıdır.
```

## Avantajlar ve Dezavantajlar

### Avantajlar
- Kısmi yükte iyi performans (silindir unloading sayesinde kademeli kontrol)
- Geniş çalışma aralığı (evaporasyon ve kondensasyon basıncı)
- Düşük yatırım maliyeti (küçük-orta kapasitelerde)
- Farklı soğutucu akışkanlarla uyumluluk
- Basit yapı, kolay anlaşılır mekanizma
- Yüksek basınç oranlarında çalışabilme (düşük evaporasyon sıcaklığı)

### Dezavantajlar
- Yüksek titreşim ve gürültü (ileri-geri hareket nedeniyle)
- Bakım yoğun (vana plakaları, segmanlar, yağ, contalar periyodik değişim gerektirir)
- Tam yükte scroll ve vidalı kompresörlere göre düşük verim
- Sınırlı kapasite (>500 kW için vidalı veya santrifüj tercih edilir)
- Daha fazla hareketli parça (arıza olasılığı yüksek)
- Yağ taşınımı (oil carry-over) riski — evaporatör ve kondenser performansını düşürür

## Güncel Durum ve Uygulamalar

Pistonlu kompresörlü chillerler, yeni tesislerde büyük ölçüde scroll (küçük kapasite) ve vidalı (orta-büyük kapasite) kompresörler tarafından ikame edilmiştir. Ancak aşağıdaki durumlarda hâlâ tercih edilir veya mevcut tesislerde yaygın olarak çalışmaktadır:

- **Mevcut tesisler:** 15-30 yaşında pistonlu chillerler hâlâ aktif çalışmaktadır
- **Düşük sıcaklık uygulamaları:** Evaporasyon sıcaklığı -40°C'ye kadar olan endüstriyel soğutma
- **Transkritik CO₂ sistemleri:** CO₂ (R-744) ile yüksek basınç uygulamaları
- **Amonyak (NH₃) küçük sistemler:** Düşük şarj miktarlı endüstriyel soğutma

## Dikkat Edilecekler

1. **Titreşim izolasyonu:** Pistonlu kompresörlerin titreşimi yüksektir — esnek bağlantılar, titreşim damperleri ve uygun temel tasarımı gereklidir
2. **Vana bakımı:** Emme ve basma vanaları (reed valves) en kritik aşınma parçasıdır — kırık veya eğilmiş vana plakaları ciddi verim kaybına neden olur; yıllık kontrol önerilir
3. **Yağ seviyesi ve kalitesi:** Yağ seviyesi düzenli kontrol edilmeli; düşük yağ seviyesi yatak arızasına, kirli yağ vana ve segment aşınmasına yol açar
4. **Superheat ayarı:** Emme gazı superheat değeri 5-15°C aralığında olmalı — düşük superheat sıvı dönüşü (liquid slugging) riskine, yüksek superheat verim kaybına neden olur
5. **Basınç oranı:** Yüksek basınç oranları (>8:1) volumetrik verimi ciddi düşürür — çift kademeli sıkıştırma değerlendirilmeli
6. **Gürültü:** Makine dairesi ses yalıtımı gerektirir; ISO 3744 gürültü ölçümü önerilir
7. **Yağ taşınımı:** Evaporatöre taşınan yağ ısı transfer katsayısını düşürür — yağ ayırıcı (oil separator) çalışması kontrol edilmeli

## İlgili Dosyalar
- Vidalı kompresörlü chiller: `equipment/chiller_screw.md`
- Scroll kompresörlü chiller: `equipment/chiller_scroll.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Su soğutmalı chiller: `equipment/chiller_water_cooled.md`
- Hava soğutmalı chiller: `equipment/chiller_air_cooled.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 38: Compressors
- ASHRAE Handbook — Refrigeration (2022), Chapter 1: Thermodynamics and Refrigeration Cycles
- ASHRAE Standard 90.1-2022: Energy Standard for Buildings Except Low-Rise Residential Buildings
- Bitzer Compressor Selection Software & Technical Documentation
- Copeland (Emerson) Reciprocating Compressor Application Manual
- Stoecker, W.F., Jones, J.W. (1982). *Refrigeration and Air Conditioning*, McGraw-Hill
- Dossat, R.J. (2001). *Principles of Refrigeration*, Prentice Hall, 5th Edition
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley
- ARI Standard 550/590: Water-Chilling and Heat Pump Water-Heating Packages Using the Vapor Compression Cycle
