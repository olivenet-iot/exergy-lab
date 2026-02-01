# Su Soğutmalı Chiller — Water-Cooled Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı soğutma çevrimi — su soğutmalı kondenser
- Kapasite aralığı: 30 - 15,000+ kW (8.5 - 4,300+ ton)
- Kondenser tipi: Shell-and-tube (gövde-boru) veya plakalı ısı değiştirici
- COP aralığı: 4.5 - 7.5 (tam yük, standart koşullar)
- COP avantajı: Hava soğutmalı sisteme göre %10-30 daha yüksek
- Ekserji verimi: %20 - 45
- Soğutucu akışkan: R-134a, R-410A, R-1234ze(E), R-513A, R-514A, R-1233zd(E)
- Kompresör tipi: Scroll (küçük), vidalı (orta), santrifüj (büyük)
- Soğutma kulesi entegrasyonu gerektirir
- Yaygın markalar: Carrier, Trane, York (Johnson Controls), Daikin, Mitsubishi, Hitachi, McQuay, Dunham-Bush
- Uygulama: Büyük ticari binalar, hastane, veri merkezi, endüstriyel proses soğutma, bölgesel soğutma

## Çalışma Prensibi

Su soğutmalı chiller, buhar sıkıştırmalı soğutma çevriminin kondenser tarafında su ile ısı atımı yapar. Kondenserde ısınan soğutma suyu (condenser water), soğutma kulesine gönderilir ve evaporatif soğutma ile ısısını atmosfere atar.

### Sistem Bileşenleri
1. **Chiller ünitesi:** Evaporatör, kompresör, kondenser, genleşme cihazı
2. **Soğutma kulesi (Cooling Tower):** Açık çevrimli (evaporatif) veya kapalı çevrimli
3. **Soğutma suyu pompaları (CW pumps):** Chiller kondenser — soğutma kulesi arasında su sirkülasyonu
4. **Soğuk su pompaları (CHW pumps):** Chiller evaporatör — kullanım noktaları (AHU, FCU) arasında
5. **Su işleme sistemi:** Kireç önleyici, korozyon inhibitörü, biyosit dozajı

### Kondenser Tasarımı

#### Shell-and-Tube (Gövde-Boru)
- Soğutma suyu borulardan, soğutucu akışkan gövde tarafından akar
- Büyük kapasite chillerler için standart tasarım
- Bakım: Boru tarafı mekanik temizlenebilir (fırça, kimyasal)
- Fouling faktörü: 0.000044 m²·K/W (ARI standart), kirli su için daha yüksek
- Boru malzemesi: Bakır (standart), CuNi %90/10 (deniz suyu), titanyum (agresif su)

#### Plakalı Isı Değiştirici (PHE)
- Kompakt tasarım, yüksek ısı transfer katsayısı
- Küçük-orta kapasite chillerlerde ve modüler sistemlerde kullanılır
- Daha düşük su hacmi, hızlı yanıt
- Dezavantaj: Fouling'e daha duyarlı, temizlik daha zor

## Yaklaşım Sıcaklığı Kavramları (Approach Temperature)

Su soğutmalı sistemlerde performansı etkileyen üç kritik yaklaşım sıcaklığı vardır:

### 1. Kondenser Yaklaşım Sıcaklığı

```
ΔT_kond = T_kondensasyon - T_CW_çıkış

Burada:
  ΔT_kond        : Kondenser yaklaşım sıcaklığı (°C), tipik 1.5 - 3.0°C
  T_kondensasyon : Soğutucu akışkan kondensasyon sıcaklığı (°C)
  T_CW_çıkış    : Soğutma suyu çıkış sıcaklığı (°C)
```

### 2. Evaporatör Yaklaşım Sıcaklığı

```
ΔT_evap = T_CHW_çıkış - T_evaporasyon

Burada:
  ΔT_evap        : Evaporatör yaklaşım sıcaklığı (°C), tipik 1.5 - 3.0°C
  T_CHW_çıkış   : Soğuk su çıkış sıcaklığı (°C)
  T_evaporasyon  : Soğutucu akışkan evaporasyon sıcaklığı (°C)
```

### 3. Soğutma Kulesi Yaklaşım Sıcaklığı

```
ΔT_kule = T_CW_çıkış_kule - T_wb

Burada:
  ΔT_kule        : Soğutma kulesi yaklaşım sıcaklığı (°C), tipik 3 - 7°C
  T_CW_çıkış_kule: Soğutma kulesi çıkış (soğuk) su sıcaklığı (°C)
  T_wb           : Ortam yaş termometre sıcaklığı (wet bulb) (°C)
```

### Toplam Sıcaklık Zinciri

```
T_kondensasyon = T_wb + ΔT_kule + ΔT_CW_range + ΔT_kond

Burada:
  T_wb          : Yaş termometre sıcaklığı (°C)
  ΔT_kule       : Kule yaklaşımı (°C), tipik 3-7°C
  ΔT_CW_range   : Soğutma suyu sıcaklık farkı (°C), tipik 5-6°C
  ΔT_kond       : Kondenser yaklaşımı (°C), tipik 1.5-3°C

Örnek: T_kond = 25 + 4 + 5.5 + 2 = 36.5°C
(Hava soğutmalıda: T_kond = 35 + 12 = 47°C → fark belirgin)
```

Toplam yaklaşım sıcaklıklarının toplamı ne kadar düşükse, kondensasyon sıcaklığı o kadar düşük ve COP o kadar yüksek olur. Bu, su soğutmalı sistemin temel avantajını açıklar.

## Soğutma Kulesi Entegrasyonu

### Kule Tipleri

| Kule Tipi | Açıklama | Avantaj | Dezavantaj |
|-----------|----------|---------|------------|
| Açık çevrimli (evaporatif) | Su, hava ile doğrudan temas eder | Düşük maliyet, yüksek verim | Su kaybı, fouling, Legionella riski |
| Kapalı çevrimli | Su, kapalı serpantinde, hava ile dolaylı temas | Temiz su devresi | Daha düşük verim, yüksek maliyet |
| Crossflow | Hava yatay, su dikey akar | Düşük fan basıncı | Daha büyük taban alanı |
| Counterflow | Hava ve su karşı yönde akar | Daha kompakt, yüksek verim | Daha yüksek fan basıncı |
| Hibrit (kuru/ıslak) | Kuru ve ıslak soğutma kombinasyonu | Düşük su tüketimi, buhar plümü azaltma | Yüksek maliyet |

### Su Tüketimi

```
ṁ_evap = Q_kule / h_fg ≈ Q_kule / 2,430

Burada:
  ṁ_evap : Buharlaşan su debisi (kg/h)
  Q_kule : Soğutma kulesinden atılan ısı (kJ/h)
  h_fg   : Suyun buharlaşma gizli ısısı (~2,430 kJ/kg, 30°C'de)

Toplam su tüketimi ≈ ṁ_evap × 1.5  (buharlaşma + sürükleme + blowdown)
Tipik: 2.5 - 4.0 L / kWh soğutma (iklime bağlı)
```

### Legionella Riski ve Yönetimi

Soğutma kuleleri, Legionella pneumophila bakterisinin üremesi için uygun ortam sağlar (25-45°C sıcak, nemli, durgun su, biyofilm). Yönetim önlemleri:

- **Su sıcaklığı kontrolü:** Kule havuzu sıcaklığı <20°C veya >60°C (pratik değil, bu nedenle biyosit kullanılır)
- **Biyosit dozajı:** Klor bazlı, brom bazlı veya klordioksit (ClO₂); sürekli veya aralıklı dozaj
- **Biyofilm kontrolü:** Düzenli mekanik temizlik, biyodispersant kullanımı
- **Düzenli test:** Legionella kültür testi (üç ayda bir), genel bakteri sayımı (haftalık)
- **Drift eliminator:** Sürükleme kayıplarını <0.005% düşüren damlacık tutucu; aerosol yayılımını azaltır
- **Yasal gereksinimler:** AB Direktifi 2020/2184, Türkiye — çevre ve sağlık mevzuatı

## Enerji Dağılımı (Tipik — Tam Yük, Standart Koşullar)

| Enerji Akışı | Oran (%) | Açıklama |
|---------------|----------|----------|
| Evaporatörde alınan ısı (soğutma etkisi) | 78 - 85 | Faydalı soğutma |
| Kompresör iş girdisi | 15 - 22 | Elektrik enerjisi (sıkıştırma) |
| Kondenserde atılan ısı | 100 | Q_evap + W_comp |
| Kompresör mekanik/motor kayıpları | 2 - 5 | Sürtünme, motor verimi |

### Toplam Sistem Verimliliği

Su soğutmalı chillerin gerçek verimliliği, yalnızca chiller COP değeri ile değerlendirilemez. Soğutma kulesi fanları, soğutma suyu pompaları ve su işleme enerjisi de dahil edilmelidir:

```
COP_sistem = Q_evap / (W_comp + W_CW_pompa + W_kule_fan + W_CHW_pompa)

Burada:
  Q_evap      : Soğutma kapasitesi (kW)
  W_comp      : Kompresör gücü (kW)
  W_CW_pompa  : Soğutma suyu pompası gücü (kW), tipik Q_evap'ın %3-8'i
  W_kule_fan  : Soğutma kulesi fan gücü (kW), tipik Q_evap'ın %2-5'i
  W_CHW_pompa : Soğuk su pompası gücü (kW), tipik Q_evap'ın %3-8'i

COP_sistem genellikle COP_chiller'ın %70-85'i kadardır.
```

| Bileşen | Güç Tüketimi (% toplam) |
|---------|-------------------------|
| Chiller kompresörü | 55 - 70 |
| Soğuk su pompaları | 10 - 18 |
| Soğutma suyu pompaları | 8 - 15 |
| Soğutma kulesi fanları | 5 - 12 |
| Su işleme, kontrol | 1 - 3 |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (kompresör) | kW | 10 - 3,000 | Güç analizörü |
| Soğuk su giriş sıcaklığı (CHW dönüş) | °C | 10 - 16 | PT100 sensör |
| Soğuk su çıkış sıcaklığı (CHW gidiş) | °C | 5 - 9 | PT100 sensör |
| Soğuk su debisi | m³/h | Kapasiteye bağlı | Ultrasonik / EM debimetre |
| Soğutma suyu giriş sıcaklığı (CW giriş) | °C | 26 - 35 | PT100 sensör |
| Soğutma suyu çıkış sıcaklığı (CW çıkış) | °C | 31 - 40 | PT100 sensör |
| Soğutma suyu debisi | m³/h | Kapasiteye bağlı | Ultrasonik / EM debimetre |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Soğutma kulesi çıkış suyu sıcaklığı | °C | 26 - 32 | PT100 sensör |
| Ortam yaş termometre sıcaklığı | °C | 18 - 30 | Psikrometre / higrometre |
| Ortam kuru termometre sıcaklığı | °C | 25 - 45 | Termometre |
| Kule fan gücü | kW | 2 - 100 | Güç analizörü |
| CW pompa gücü | kW | 2 - 100 | Güç analizörü |
| CHW pompa gücü | kW | 2 - 100 | Güç analizörü |
| Emme basıncı | bar | 2 - 5 | Manometre |
| Basma basıncı | bar | 8 - 15 | Manometre |
| Kompresör emme sıcaklığı | °C | -2 ile +10 (superheat) | Termokupl |
| Su iletkenliği (CW) | µS/cm | 300 - 3,000 | İletkenlik ölçer |
| Su sertliği (CW) | mg/L CaCO₃ | 100 - 500 | Test kiti / laboratuvar |
| Makeup su miktarı | m³/gün | Kapasiteye bağlı | Su sayacı |
| Çalışma saati | saat/yıl | 2,000 - 8,000 | Sayaç |

### Nameplate Bilgileri
- Marka ve model
- Nominal soğutma kapasitesi (kW veya ton) ve koşulları
- Nominal elektrik gücü (kW)
- Kompresör tipi ve sayısı
- Soğutucu akışkan tipi ve şarj miktarı (kg)
- Nominal COP veya kW/ton
- Evaporatör ve kondenser tasarım basınçları (bar)
- Su tarafı tasarım debisi (m³/h)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Soğuk su giriş sıcaklığı (CHW dönüş) | 12°C | Konfor soğutma varsayımı |
| Soğuk su çıkış sıcaklığı (CHW gidiş) | 7°C | Standart chiller çıkışı |
| Soğutma suyu giriş sıcaklığı (CW giriş) | 30°C | Standart ARI koşulu |
| Soğutma suyu çıkış sıcaklığı (CW çıkış) | 35°C | 5°C kondenser range |
| Yaş termometre sıcaklığı | 25°C | Yaz tasarım koşulu (Türkiye) |
| Soğutma kulesi yaklaşımı | 5°C | Tipik yeni kule |
| Kondenser yaklaşımı | 2°C | Temiz kondenser |
| Evaporatör yaklaşımı | 2°C | Temiz evaporatör |
| COP (chiller, tam yük) | 5.5 | Orta-büyük kapasite santrifüj |
| COP (sistem, tam yük) | 4.0 | Chiller + kule + pompalar |
| IPLV/NPLV | 7.0 - 10.0 | Mevsimsel ortalama chiller verimi |
| Ekserji verimi | %30 | Ortalama çalışma koşulları |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa (1 atm) | Standart ölü durum |
| Çalışma saati | 3,000 saat/yıl | Türkiye, ticari soğutma |
| Yük oranı (ortalama) | %60 | Mevsimsel ortalama |
| Su tüketimi | 3.0 L / kWh soğutma | Açık kule, Türkiye iklimi |

## Performans Tablosu

### Kapasite ve COP Değerleri (Tam Yük, ARI Standart Koşullar)

| Kapasite (kW) | Kompresör Tipi | COP | kW/ton | Ekserji Verimi (%) | Tipik Uygulama | Yaklaşık Fiyat (€) |
|---------------|----------------|-----|--------|---------------------|----------------|---------------------|
| 30 - 100 | Scroll | 4.5 - 5.5 | 0.64 - 0.78 | 20 - 28 | Küçük ticari | 8,000 - 25,000 |
| 100 - 350 | Vidalı | 5.0 - 6.0 | 0.59 - 0.70 | 24 - 32 | Orta ticari, otel | 20,000 - 70,000 |
| 350 - 1,000 | Vidalı/Santrifüj | 5.5 - 6.5 | 0.54 - 0.64 | 28 - 38 | Büyük ticari, hastane | 60,000 - 200,000 |
| 1,000 - 3,000 | Santrifüj | 6.0 - 7.0 | 0.50 - 0.59 | 32 - 42 | Büyük endüstriyel, kampüs | 150,000 - 500,000 |
| 3,000 - 8,000 | Santrifüj | 6.5 - 7.3 | 0.48 - 0.54 | 35 - 44 | Bölgesel soğutma | 400,000 - 1,200,000 |
| 8,000 - 15,000+ | Santrifüj (çok kademeli) | 6.8 - 7.5 | 0.47 - 0.52 | 38 - 45 | Büyük bölgesel, veri merkezi | 1,000,000 - 3,000,000+ |

### Ekserji Verimi Hesabı

```
COP = Q_evap / W_comp

η_Carnot = T_cold / (T_hot - T_cold)

η_exergy = COP / COP_Carnot × 100

Burada:
  Q_evap     : Evaporatörde alınan ısı — soğutma kapasitesi (kW)
  W_comp     : Kompresör elektrik gücü (kW)
  T_cold     : Evaporatör soğuk su ortalama sıcaklığı (K)
  T_hot      : Kondenser soğutma suyu ortalama sıcaklığı (K)
  COP_Carnot : Tersinir Carnot COP (—)
  η_exergy   : Ekserji verimi (%)
  T₀         : Referans çevre sıcaklığı = 25°C (298.15 K)
```

Örnek hesaplama (santrifüj chiller, 2,000 kW):

```
T_cold = (12 + 7) / 2 + 273.15 = 282.65 K
T_hot  = (30 + 35) / 2 + 273.15 = 305.65 K
COP_Carnot = 282.65 / (305.65 - 282.65) = 12.29
COP_gerçek = 6.5
η_exergy = 6.5 / 12.29 × 100 = %52.9

Burada:
  Bu değer yalnızca chiller ekserji verimidir.
  Sistem ekserji verimi (kule + pompa dahil) daha düşüktür.
  Sistem COP ≈ 4.5 → η_exergy_sistem = 4.5 / 12.29 × 100 = %36.6
```

### Kısmi Yük Performansı (Santrifüj Chiller + VSD)

| Yük Oranı (%) | COP / COP_tam_yük (%) | Kompresör Gücü (%) | Kule Fan Gücü (%) |
|----------------|------------------------|---------------------|---------------------|
| 100 | 100 | 100 | 100 |
| 75 | 115 - 130 | 55 - 68 | 60 - 80 |
| 50 | 125 - 155 | 28 - 42 | 30 - 50 |
| 25 | 100 - 135 | 12 - 22 | 15 - 30 |

VSD (Variable Speed Drive) donanımlı santrifüj chillerlerin kısmi yük performansı mükemmeldir. IPLV/NPLV değerleri tam yük COP'unun 1.4-1.8 katına çıkabilir.

## Su İşleme ve Bakım

### Soğutma Suyu Kalite Parametreleri

| Parametre | Önerilen Aralık | Sorun (Aşılırsa) |
|-----------|-----------------|-------------------|
| pH | 7.0 - 9.0 | <7: Korozyon, >9: Kireçlenme |
| İletkenlik | <3,000 µS/cm | Kireç ve korozyon riski |
| Toplam sertlik | 100 - 500 mg/L CaCO₃ | >500: Kireçlenme, <100: Korozyon |
| Klorür | <250 mg/L | Paslanmaz çelik korozyonu |
| Silika | <150 mg/L | Çözülmesi zor kireç birikimi |
| Toplam bakteri | <10,000 CFU/mL | Biyofilm, Legionella riski |
| Legionella | <1,000 CFU/L | Sağlık riski |

### Kondenser Fouling Etkisi

| Fouling Durumu | Fouling Faktörü (m²·K/W) | COP Etkisi | Kapasite Etkisi |
|----------------|---------------------------|------------|-----------------|
| Temiz (yeni) | 0.000018 | Referans | Referans |
| ARI Standart | 0.000044 | -%2-3 | -%1-2 |
| Hafif kirli | 0.000088 | -%5-8 | -%3-5 |
| Kirli | 0.000176 | -%10-15 | -%8-12 |
| Çok kirli | 0.000350 | -%15-25 | -%12-20 |

Düzenli kondenser temizliği (yılda 1-2 kez) ve etkili su işleme, COP kaybını %2-3 ile sınırlar.

## Dikkat Edilecekler

1. **Soğutma kulesi bakımı:** Kulenin verimliliği doğrudan chiller performansını etkiler — dolgu malzemesi kirlenmesi, fan arızası, su dağıtım sorunları COP'u ciddi düşürür
2. **Kondenser fouling:** Su tarafı kirlenmesi kondenser yaklaşım sıcaklığını artırır, COP düşer — düzenli fırçalama, kimyasal temizlik ve otomatik tüp temizleme sistemleri (ATCS) değerlendirilmeli
3. **Su işleme:** Yetersiz su işleme kireçlenme, korozyon ve biyolojik büyümeye neden olur — blowdown oranı, inhibitör dozajı ve biyosit düzenli kontrol edilmeli
4. **Legionella riski:** Soğutma kuleleri Legionella üreme ortamıdır — düzenli mikrobiyolojik test, biyosit dozajı ve drift eliminator bakımı zorunlu
5. **Toplam sistem verimi:** Chiller COP tek başına yanıltıcı olabilir — pompalar ve kule fan gücü dahil edilmeli; COP_sistem değeri esas alınmalı
6. **Yaklaşım sıcaklıkları:** Kondenser ve evaporatör yaklaşım sıcaklıkları zamanla artar (fouling) — yıllık trend takibi performans bozulmasını erken tespit ettirir
7. **Su tüketimi:** Açık kule sistemleri önemli miktarda su tüketir (~3 L/kWh soğutma) — su kıtlığı olan bölgelerde maliyet ve çevresel etki değerlendirilmeli
8. **Kış işletimi:** Soğutma kulesi donma riski — kule havuzu ısıtıcısı, by-pass hattı veya glikol çözeltisi değerlendirilmeli
9. **Enerji geri kazanımı:** Kondenserde atılan ısı (soğutma kapasitesinin ~1.2x'i) düşük sıcaklıklı ısıtma, sıcak su ön ısıtma veya regenerasyon için kullanılabilir

## İlgili Dosyalar
- Hava soğutmalı chiller: `equipment/chiller_air_cooled.md`
- Absorpsiyonlu chiller: `equipment/chiller_absorption.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Pistonlu kompresörlü chiller: `equipment/chiller_reciprocating.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Soğutma kulesi optimizasyonu: `solutions/cooling_tower_optimization.md`
- Kondenser temizlik çözümleri: `solutions/chiller_condenser_cleaning.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 38: Compressors; Chapter 39: Condensers
- ASHRAE Handbook — HVAC Applications (2023), Chapter 49: Water Treatment
- ASHRAE Standard 90.1-2022: Energy Standard for Buildings Except Low-Rise Residential Buildings
- AHRI Standard 550/590: Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages
- Carrier System Design Manual: Chilled Water Plant Design
- Trane Engineers Newsletter: Chiller Plant Design & Optimization
- York (Johnson Controls) Chiller Application Guide
- CTI STD-201: Certification Standard for Water-Cooling Tower Thermal Performance
- EUROVENT Energy Efficiency Classification for Water-Cooled Chillers
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley
- McQuiston, F.C., Parker, J.D., Spitler, J.D. (2023). *Heating, Ventilating, and Air Conditioning: Analysis and Design*, Wiley, 7th Edition
- Legionella Directive 2020/2184/EU — Drinking Water Quality Requirements
- TS EN 14511: Air conditioners, liquid chilling packages and heat pumps
