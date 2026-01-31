# Hava Soğutmalı Chiller — Air-Cooled Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı soğutma çevrimi — hava soğutmalı kondenser
- Kapasite aralığı: 5 - 1,500 kW (1.4 - 430 ton)
- Kondenser tipi: Fin-tube (kanatlı boru) veya microchannel (mikro kanallı)
- COP aralığı: 2.5 - 3.5 (35°C ortam sıcaklığında, tam yük)
- COP karşılaştırması: Su soğutmalı sisteme göre %10-20 daha düşük
- Ekserji verimi: %12 - 28
- Fan enerji tüketimi: Toplam güç tüketiminin %5-15'i
- Soğutucu akışkan: R-134a, R-410A, R-32, R-513A, R-1234ze(E)
- Kompresör tipi: Scroll (küçük), vidalı (orta), santrifüj (büyük)
- Yaygın markalar: Carrier, Trane, Daikin, Mitsubishi, York, Hitachi, Climaveneta, Aermec, Clivet
- Avantaj: Soğutma kulesi gerektirmez, düşük su tüketimi, basit kurulum
- Uygulama: Ofis, AVM, otel, hastane, küçük-orta endüstriyel tesisler

## Çalışma Prensibi

Hava soğutmalı chiller, buhar sıkıştırmalı soğutma çevriminin kondenser tarafında hava ile ısı atımı yapar. Sistem, kapalı bir soğutma çevriminde çalışır:

1. **Evaporatör:** Soğutucu akışkan düşük basınçta buharlaşarak soğuk su devresinden ısı alır
2. **Kompresör:** Düşük basınçlı buhar sıkıştırılarak yüksek basınç ve sıcaklığa çıkarılır
3. **Kondenser (hava soğutmalı):** Yüksek basınçlı sıcak buhar, fan yardımıyla çekilen ortam havası ile soğutularak yoğuşur
4. **Genleşme vanası:** Sıvı soğutucu akışkan basıncı düşürülerek evaporatöre geri döner

### Kondenser Tasarımı

#### Fin-Tube (Kanatlı Boru)
- Bakır veya alüminyum borular üzerine alüminyum kanatlar preslenmiş yapı
- Kanat aralığı: 1.8 - 2.5 mm (standart), 3.0 - 4.0 mm (kirli ortam, epoksi kaplı)
- Isı transfer yüzeyi artırma oranı: 10-20x (düz boruya göre)
- Yaygın kullanım: Küçük ve orta kapasite chillerler
- Dezavantaj: Korozyon riski (deniz kenarı, kimyasal ortam), kanat kirlenmesi

#### Microchannel (Mikro Kanallı)
- Yassı alüminyum tüpler içinde çok sayıda küçük kanal (<1 mm)
- Soğutucu akışkan şarjı %30-40 daha az
- Daha kompakt ve hafif yapı
- Isı transfer katsayısı daha yüksek
- Dezavantaj: Korozyon hassasiyeti, onarım zorluğu, kirlenmeye duyarlı

### Ortam Sıcaklığının Performansa Etkisi

Hava soğutmalı chillerde kondensasyon sıcaklığı doğrudan ortam hava sıcaklığına bağlıdır. Ortam sıcaklığı arttıkça kondensasyon basıncı yükselir, kompresör daha fazla iş yapar ve COP düşer.

```
T_kondensasyon ≈ T_ortam + ΔT_yaklaşım

Burada:
  T_kondensasyon : Kondensasyon sıcaklığı (°C)
  T_ortam        : Ortam hava sıcaklığı (°C)
  ΔT_yaklaşım   : Kondenser yaklaşım sıcaklığı, tipik 8-15°C
```

| Ortam Sıcaklığı (°C) | Kondensasyon Sıcaklığı (°C) | COP (tipik) | Kapasite (% tasarım) |
|------------------------|-----------------------------|-------------|----------------------|
| 25 | 35 - 40 | 3.5 - 4.2 | 115 - 125 |
| 30 | 40 - 45 | 3.0 - 3.7 | 105 - 115 |
| 35 | 45 - 50 | 2.5 - 3.2 | 95 - 105 |
| 40 | 50 - 55 | 2.2 - 2.8 | 80 - 95 |
| 43 | 53 - 58 | 1.9 - 2.5 | 70 - 85 |
| 46 | 56 - 61 | 1.7 - 2.2 | 60 - 75 |

Ortam sıcaklığındaki her 1°C artış, COP'u yaklaşık %1.5-2.5 düşürür ve soğutma kapasitesini %1-2 azaltır.

## Enerji Dağılımı (Tipik — 35°C Ortam, Tam Yük)

| Enerji Akışı | Oran (%) | Açıklama |
|---------------|----------|----------|
| Evaporatörde alınan ısı (soğutma etkisi) | 72 - 78 | Faydalı soğutma |
| Kompresör iş girdisi | 22 - 28 | Elektrik enerjisi (sıkıştırma) |
| Kondenser fan gücü | 5 - 15 | Toplam gücün yüzdesi olarak |
| Kondenserde atılan ısı | 100 | Q_evap + W_comp (fan ısısı dahil) |
| Kompresör mekanik/motor kayıpları | 3 - 8 | Sürtünme, motor verimi |

### Fan Enerji Tüketimi

```
P_fan = (V̇_air × ΔP_air) / η_fan

Burada:
  P_fan    : Fan motor gücü (kW)
  V̇_air   : Hava hacimsel debisi (m³/s)
  ΔP_air   : Hava tarafı basınç düşüşü (Pa), tipik 80-200 Pa
  η_fan    : Fan verimi (motor dahil), tipik %40-65

Toplam fan gücü = P_fan × fan sayısı
Tipik: 0.03 - 0.08 kW fan gücü / kW soğutma kapasitesi
```

Fan gücü toplam enerji tüketiminin %5-15'ini oluşturur. EC (electronically commutated) motorlu fanlar, konvansiyonel AC fanlara göre %30-50 enerji tasarrufu sağlar.

## Kısmi Yük Performansı

| Yük Oranı (%) | COP / COP_tam_yük (%) | Fan Gücü (%) | Toplam Güç (%) |
|----------------|------------------------|--------------|----------------|
| 100 | 100 | 100 | 100 |
| 75 | 105 - 115 | 60 - 80 | 65 - 75 |
| 50 | 110 - 130 | 30 - 50 | 40 - 55 |
| 25 | 90 - 120 | 15 - 30 | 25 - 40 |

Kısmi yükte ortam sıcaklığı genellikle tasarım değerinin altındadır. Bu nedenle gerçek kısmi yük performansı, yalnızca yük azalmasından daha iyi olabilir. IPLV/NPLV değerleri bu etkiyi yansıtır.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (toplam chiller) | kW | 2 - 500 | Güç analizörü |
| Soğuk su giriş sıcaklığı (evaporatör) | °C | 10 - 16 | PT100 sensör |
| Soğuk su çıkış sıcaklığı (evaporatör) | °C | 5 - 9 | PT100 sensör |
| Soğuk su debisi | m³/h | Kapasiteye bağlı | Ultrasonik debimetre |
| Ortam hava sıcaklığı | °C | 15 - 48 | Termometre (gölgede, cihaz emme tarafı) |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kondenser hava çıkış sıcaklığı | °C | Ortam + 8-18°C | Termometre (kondenser üstü) |
| Kondenser hava sıcaklık yükselmesi (ΔT) | °C | 8 - 18 | Giriş ve çıkış farkı |
| Kompresör gücü (ayrı) | kW | Kapasiteye bağlı | Güç analizörü (kompresör beslemesi) |
| Fan gücü (toplam) | kW | 0.5 - 50 | Güç analizörü (fan beslemesi) |
| Emme basıncı | bar | 3 - 6 | Manometre |
| Basma basıncı | bar | 12 - 25 | Manometre |
| Kompresör emme gazı sıcaklığı | °C | 0 - 15 (superheat) | Termokupl |
| Rüzgar hızı ve yönü | m/s | 0 - 15 | Anemometre |
| Ses basınç seviyesi | dB(A) | 60 - 90 | Ses ölçer (1m, 1.5m yükseklikte) |
| Çalışma saati | saat/yıl | 2,000 - 6,000 | Sayaç |

### Nameplate Bilgileri
- Marka ve model
- Nominal soğutma kapasitesi (kW veya ton) ve koşulları (ortam sıcaklığı, su sıcaklıkları)
- Nominal elektrik gücü (kW)
- Kompresör tipi ve sayısı
- Fan sayısı ve motor gücü
- Soğutucu akışkan tipi ve şarj miktarı (kg)
- Nominal COP veya EER
- Ses basınç seviyesi (dB(A))
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Soğuk su giriş sıcaklığı | 12°C | Konfor soğutma varsayımı |
| Soğuk su çıkış sıcaklığı | 7°C | Standart chiller çıkışı |
| Ortam sıcaklığı | 35°C | Yaz tasarım koşulu (Türkiye) |
| Kondenser yaklaşım sıcaklığı | 12°C | Hava-soğutucu akışkan farkı |
| COP (tam yük, 35°C ortam) | 2.8 | Orta kapasite, scroll/vidalı kompresör |
| IPLV/NPLV | 4.0 - 5.5 | Mevsimsel ortalama verim |
| Fan gücü oranı | %10 | Toplam gücün yüzdesi |
| Ekserji verimi | %18 | Ortalama çalışma koşulları |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa (1 atm) | Standart ölü durum |
| Çalışma saati | 3,000 saat/yıl | Türkiye, ticari soğutma |
| Yük oranı (ortalama) | %60 | Mevsimsel ortalama |

## Performans Tablosu

### Kapasite ve COP Değerleri (Tam Yük, 35°C Ortam Sıcaklığı)

| Kapasite (kW) | Kompresör Tipi | COP | Ekserji Verimi (%) | Fan Gücü (kW) | Tipik Uygulama | Yaklaşık Fiyat (€) |
|---------------|----------------|-----|---------------------|---------------|----------------|---------------------|
| 5 - 20 | Scroll (tek) | 2.5 - 2.9 | 12 - 16 | 0.3 - 1.5 | Mini chiller, küçük ofis | 2,000 - 6,000 |
| 20 - 80 | Scroll (çoklu) | 2.7 - 3.1 | 14 - 18 | 1.0 - 5.0 | Ofis, mağaza | 5,000 - 20,000 |
| 80 - 250 | Scroll/Vidalı | 2.8 - 3.2 | 16 - 22 | 3.0 - 15.0 | AVM, otel, hastane | 18,000 - 60,000 |
| 250 - 600 | Vidalı | 2.9 - 3.4 | 18 - 25 | 10.0 - 35.0 | Büyük ticari, endüstriyel | 50,000 - 150,000 |
| 600 - 1,500 | Vidalı/Santrifüj | 3.0 - 3.5 | 20 - 28 | 25.0 - 80.0 | Büyük endüstriyel, kampüs | 120,000 - 400,000 |

### Ekserji Verimi Hesabı

```
COP = Q_evap / W_total

W_total = W_comp + W_fan

η_Carnot = T_cold / (T_hot - T_cold)

η_exergy = COP / COP_Carnot × 100

Burada:
  Q_evap     : Evaporatörde alınan ısı — soğutma kapasitesi (kW)
  W_total    : Toplam elektrik gücü — kompresör + fanlar (kW)
  W_comp     : Kompresör elektrik gücü (kW)
  W_fan      : Fan motor gücü (kW)
  T_cold     : Evaporatör soğuk su ortalama sıcaklığı (K)
  T_hot      : Ortam hava sıcaklığı (K) — kondenser dışı referans
  COP_Carnot : Tersinir Carnot COP (—)
  η_exergy   : Ekserji verimi (%)
```

Hava soğutmalı chillerde T_hot olarak ortam hava sıcaklığı alınır. Su soğutmalı sistemlerde bu değer soğutma suyu sıcaklığıdır ve genellikle daha düşüktür — bu fark COP avantajını açıklar.

## Ses ve Yerleşim Konuları

### Ses Seviyeleri (Tipik)

| Kapasite (kW) | Ses Gücü Seviyesi LwA (dB(A)) | 10m Mesafede Ses Basıncı (dB(A)) |
|---------------|-------------------------------|----------------------------------|
| 20 - 80 | 75 - 85 | 45 - 55 |
| 80 - 250 | 82 - 90 | 52 - 60 |
| 250 - 600 | 88 - 95 | 58 - 65 |
| 600 - 1,500 | 92 - 100 | 62 - 70 |

### Yerleşim Kuralları
- Minimum mesafe: Binadan 2-3m, komşu sınırından 5-10m (yerel yönetmeliğe bağlı)
- Hava emme ve basma yönünde engel olmamalı — minimum 1m serbest alan
- Yüksek binalarda çatıya yerleşim: Yapısal yük kontrolü ve titreşim izolasyonu gerekli
- Birden fazla ünitenin yan yana yerleşimi: Sıcak hava resirkülasyonu riski — minimum ünite genişliği kadar ara mesafe
- Ses perdesi (acoustic barrier): Hassas bölgelerde gerekebilir (otel, hastane, konut yakını)

## Free Cooling Entegrasyonu

Ortam sıcaklığı yeterince düşük olduğunda (kış ve geçiş dönemleri) kompresör çalıştırmadan doğrudan hava ile soğutma yapılabilir. Bu kavram "free cooling" veya "economizer mode" olarak adlandırılır.

### Free Cooling Tipleri
- **Entegre free cooling:** Chiller içinde ek bir kuru soğutucu (dry cooler) serpantini; ortam sıcaklığı set değerinin altında olduğunda otomatik geçiş
- **Harici dry cooler:** Ayrı bir kuru soğutucu ünite; chiller bypass edilerek soğuk su doğrudan dry cooler ile soğutulur
- **Karma (hybrid):** Kısmi free cooling + kısmi mekanik soğutma — geçiş dönemlerinde

### Free Cooling Tasarım Parametreleri

```
Q_free = V̇_air × ρ_air × cp_air × (T_su_dönüş - T_ortam - ΔT_yaklaşım)

Burada:
  Q_free         : Free cooling kapasitesi (kW)
  V̇_air          : Hava hacimsel debisi (m³/s)
  ρ_air          : Hava yoğunluğu (~1.2 kg/m³)
  cp_air         : Havanın özgül ısısı (~1.005 kJ/kg·K)
  T_su_dönüş     : Soğuk su dönüş sıcaklığı (°C)
  T_ortam        : Ortam hava sıcaklığı (°C)
  ΔT_yaklaşım   : Dry cooler yaklaşım sıcaklığı, tipik 5-8°C
```

Free cooling, Türkiye'de tipik olarak ortam sıcaklığı <10-15°C olduğunda (kış ayları ve geçiş dönemleri) devreye girer. Veri merkezleri gibi yıl boyunca soğutma gerektiren tesislerde önemli enerji tasarrufu sağlar.

## Dikkat Edilecekler

1. **Ortam sıcaklığı etkisi:** Hava soğutmalı chillerin performansı ortam sıcaklığına çok duyarlıdır — her 1°C artış COP'u %1.5-2.5 düşürür; sıcak iklimlerde bu dezavantaj belirgindir
2. **Sıcak hava resirkülasyonu:** Kondenser çıkış havasının tekrar emme tarafına dönmesi performansı ciddi düşürür — yerleşim ve hava akış yönü dikkatle planlanmalı
3. **Kanat kirlenmesi:** Kondenser kanatlarına biriken toz, yaprak, tüy vb. hava akışını engeller ve ısı transfer performansını düşürür — düzenli temizlik (yılda 2-4 kez) gerekli
4. **Fan arızası:** Bir veya daha fazla fan arızalanırsa kondensasyon basıncı hızla yükselir — yüksek basınç güvenlik cihazı (HP switch) devreye girmeli
5. **Ses ve komşuluk:** Hava soğutmalı chillerler gürültü kaynağıdır (özellikle gece) — yerleşim mesafesi, ses bariyeri ve düşük gürültülü fan seçimi önemli
6. **Kış koşulları:** Düşük ortam sıcaklığında emme basıncı çok düşebilir — head pressure control (kondenser fan hız kontrolü veya damper) gerekli
7. **Korozyon (deniz kenarı):** Tuzlu ortamda alüminyum kanatlar hızla korozyona uğrar — epoksi kaplamalı veya bakır kanatlı kondenser seçilmeli
8. **Free cooling potansiyeli:** Yıl boyunca soğutma gerektiren tesislerde (veri merkezi, proses soğutma) free cooling entegrasyonu değerlendirilmeli — %20-50 enerji tasarrufu mümkün

## İlgili Dosyalar
- Su soğutmalı chiller: `equipment/chiller_water_cooled.md`
- Absorpsiyonlu chiller: `equipment/chiller_absorption.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Pistonlu kompresörlü chiller: `equipment/chiller_reciprocating.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Free cooling çözümleri: `solutions/chiller_free_cooling.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 39: Condensers
- ASHRAE Standard 90.1-2022: Energy Standard for Buildings Except Low-Rise Residential Buildings
- AHRI Standard 550/590: Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages
- Carrier Technical Development Program: Air-Cooled Chiller Application Guide
- Trane Engineers Newsletter: Air-Cooled Chiller System Design
- Daikin Applied Engineering Manual: Air-Cooled Scroll and Screw Chillers
- McQuiston, F.C., Parker, J.D., Spitler, J.D. (2023). *Heating, Ventilating, and Air Conditioning: Analysis and Design*, Wiley, 7th Edition
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley
- Eurovent Certification: Energy Efficiency Classification for Air-Cooled Chillers
- TS EN 14511: Air conditioners, liquid chilling packages and heat pumps — Part 2: Test conditions
