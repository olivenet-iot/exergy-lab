# ExergyLab Chiller Knowledge Base Araştırma Brief

> **Claude Code için:** Bu dosyayı oku ve chiller modülü için kapsamlı knowledge base oluştur.

---

## 🎯 Görev Özeti

ExergyLab projesine **chiller (soğutma grubu)** modülü ekliyoruz. Kompresör modülü zaten tamamlandı ve referans olarak kullanılacak.

**Görevin:**
1. Önce `/knowledge/` altındaki mevcut kompresör dosyalarını tara — format ve yapıyı anla
2. Aynı format ve derinlikte chiller knowledge base'i oluştur
3. Akademik makaleler, endüstri standartları, teknik kaynakları araştır
4. Tüm klasörlerde (equipment, solutions, benchmarks, formulas, methodology) ilgili dosyaları oluştur

---

## 📚 BÖLÜM 1: Mevcut Yapıyı Anla (ÖNCE BUNU YAP)

### 1.1 Kompresör Dosyalarını Tara

Şu dosyaları oku ve formatı anla:

```
/knowledge/
├── equipment/
│   ├── compressor_screw.md
│   ├── compressor_piston.md
│   └── ...
├── solutions/
│   ├── compressor_vsd.md
│   └── ...
├── benchmarks/
│   └── compressor_benchmarks.md
├── formulas/
│   └── compressor_exergy.md
└── methodology/
    └── compressed_air_audit.md
```

**Her dosyada dikkat et:**
- Başlık yapısı (H1, H2, H3)
- Tablo formatları
- Benchmark aralıkları nasıl verilmiş
- Formüller nasıl yazılmış
- Çözüm önerileri nasıl yapılandırılmış
- ROI, tasarruf hesapları nasıl gösterilmiş

### 1.2 Format Tutarlılığı

Chiller dosyaları **AYNI FORMAT**ta olmalı.

---

## ❄️ BÖLÜM 2: Chiller Araştırma Kapsamı

### 2.1 Chiller Tipleri (Equipment)

Her tip için ayrı dosya oluştur:

#### `/knowledge/equipment/chiller_vapor_compression.md`
**Buhar Sıkıştırmalı Chiller (Vapor Compression) - Genel**
- Soğutma çevrimi temelleri (evaporatör, kompresör, kondenser, genleşme valfi)
- Carnot COP vs gerçek COP
- Soğutucu akışkan türleri (R-134a, R-410A, R-1234ze, R-290, NH3, CO2)
- Ozon ve GWP değerleri
- F-gas regülasyonları
- Kapasite aralıkları
- Exergy verimi konsepti

#### `/knowledge/equipment/chiller_screw.md`
**Vidalı Kompresörlü Chiller (Screw Chiller)**
- Çalışma prensibi
- Tek vida vs çift vida
- Kapasite aralığı (50-1500 kW tipik)
- Kısmi yük performansı (slide valve)
- IPLV/NPLV değerleri
- COP aralıkları (tam yük ve kısmi yük)
- Exergy verimi aralıkları
- Su soğutmalı vs hava soğutmalı
- Avantaj/dezavantajlar
- Tipik uygulamalar
- Başlıca üreticiler (Carrier, Trane, York, Daikin, Mitsubishi)

#### `/knowledge/equipment/chiller_centrifugal.md`
**Santrifüj Kompresörlü Chiller (Centrifugal Chiller)**
- Çalışma prensibi (impeller, volüt)
- Tek kademe vs çok kademe
- Kapasite aralığı (300-10,000+ kW)
- Yüksek verimlilik potansiyeli
- Inlet Guide Vane (IGV) kontrolü
- VSD uygulaması
- Manyetik yatak (oil-free) teknolojisi
- Surge ve surge kontrolü
- COP aralıkları (en yüksek)
- IPLV/NPLV değerleri
- Exergy verimi aralıkları
- Tipik uygulamalar (büyük binalar, data center)

#### `/knowledge/equipment/chiller_scroll.md`
**Scroll Kompresörlü Chiller**
- Çalışma prensibi
- Kapasite aralığı (10-500 kW)
- Modüler sistemler (çoklu scroll)
- Kısmi yük kontrolü (digital scroll, tandem)
- COP aralıkları
- Ses seviyesi avantajı
- Exergy verimi aralıkları
- Tipik uygulamalar

#### `/knowledge/equipment/chiller_reciprocating.md`
**Pistonlu Kompresörlü Chiller**
- Çalışma prensibi
- Kapasite kontrolü (cylinder unloading)
- Kapasite aralığı (10-500 kW)
- COP karakteristikleri
- Avantaj/dezavantajlar
- Exergy verimi aralıkları
- Mevcut kullanım alanları

#### `/knowledge/equipment/chiller_absorption.md`
**Absorpsiyonlu Chiller**
- Çalışma prensibi (absorber, generator, evaporator, condenser)
- LiBr-Su çifti (pozitif basınç)
- NH3-Su çifti (negatif basınç, düşük sıcaklık)
- Tek etkili vs çift etkili vs üç etkili
- Enerji kaynakları (buhar, sıcak su, doğrudan ateşleme, atık ısı)
- COP aralıkları (0.7-1.4)
- Elektrik tüketimi (çok düşük)
- Exergy verimi konsepti (termal girdi bazlı)
- Kristalizasyon riski
- Kapasite aralıkları
- Tipik uygulamalar (trijenerasyon, atık ısı değerlendirme)

#### `/knowledge/equipment/chiller_air_cooled.md`
**Hava Soğutmalı Chiller**
- Kondenser tasarımı (fin-tube, microchannel)
- Ambient sıcaklık etkisi
- COP karşılaştırması (su soğutmalıya göre %10-20 düşük)
- Fan enerji tüketimi
- Kurulum avantajları (soğutma kulesi yok)
- Exergy verimi karakteristikleri
- Ses ve yerleşim konuları

#### `/knowledge/equipment/chiller_water_cooled.md`
**Su Soğutmalı Chiller**
- Kondenser tasarımı (shell-tube, plate)
- Soğutma kulesi entegrasyonu
- Approaching temperature
- COP avantajı
- Su tüketimi
- Legionella riski ve yönetimi
- Exergy verimi karakteristikleri
- Toplam sistem verimliliği

#### `/knowledge/equipment/cooling_tower.md`
**Soğutma Kulesi (Cooling Tower)**
- Çalışma prensibi (evaporatif soğutma)
- Açık devre vs kapalı devre
- Crossflow vs counterflow
- Wet bulb sıcaklığı ve approach
- Fan tipleri (axial, centrifugal)
- VSD uygulaması
- Su arıtma gereksinimleri
- Enerji tüketimi
- Exergy analizi

#### `/knowledge/equipment/chilled_water_systems.md`
**Soğutma Suyu Sistemleri Genel Bakış**
- Primer-sekonder sistemler
- Değişken primer akış
- Delta-T yönetimi
- Chiller sequencing
- Serbest soğutma (free cooling) entegrasyonu
- Termal depolama
- District cooling
- Sistem seviyesi exergy akışı

### 2.2 Soğutucu Akışkanlar

`/knowledge/equipment/chiller_refrigerants.md` dosyasında:
- HFC'ler (R-134a, R-410A, R-407C)
- HFO'lar (R-1234ze, R-1234yf)
- Doğal soğutucanlar (R-290 propan, R-717 amonyak, R-744 CO2)
- ODP ve GWP değerleri
- F-gas regülasyonları ve phase-out takvimi
- Soğutucu seçim kriterleri
- Termodinamik özellikler

---

## 📊 BÖLÜM 3: Benchmark Verileri

### `/knowledge/benchmarks/chiller_benchmarks.md`

**Araştırılacak benchmark metrikleri:**

#### 3.1 COP (Coefficient of Performance)
```
Buhar sıkıştırmalı (su soğutmalı, tam yük):
  Santrifüj (>500 kW):  6.0-7.5
  Vidalı:               5.0-6.5
  Scroll:               4.5-6.0
  Pistonlu:             4.0-5.5

Hava soğutmalı (tam yük):
  Tüm tipler:           2.8-4.5

Absorpsiyonlu:
  Tek etkili:           0.65-0.75
  Çift etkili:          1.0-1.4
```

#### 3.2 IPLV/NPLV (Kısmi Yük Verimi)
```
IPLV = 0.01A + 0.42B + 0.45C + 0.12D
A=100%, B=75%, C=50%, D=25% yük

Mükemmel IPLV (su soğutmalı):
  Santrifüj VSD:        >10
  Santrifüj sabit:      6-8
  Vidalı VSD:           7-9
  Vidalı sabit:         5-7
```

#### 3.3 kW/ton
```
1 ton = 3.517 kW soğutma kapasitesi
kW/ton = 1 / COP × 3.517

Mükemmel:  <0.5 kW/ton (COP >7)
İyi:       0.5-0.65 kW/ton (COP 5.4-7)
Ortalama:  0.65-0.85 kW/ton (COP 4.1-5.4)
Düşük:     >0.85 kW/ton (COP <4.1)
```

#### 3.4 Exergy Verimi
```
Chiller exergy verimi:
  Mükemmel:  >45%
  İyi:       35-45%
  Ortalama:  25-35%
  Düşük:     <25%

Not: Soğutma düşük sıcaklıkta yapıldığından
soğutma exergy'si düşüktür (Carnot faktörü)
```

#### 3.5 Kondenser Yaklaşım Sıcaklığı
```
Su soğutmalı kondenser:
  Mükemmel:  <2°C
  İyi:       2-3°C
  Ortalama:  3-5°C
  Düşük:     >5°C

Hava soğutmalı kondenser:
  Mükemmel:  <10°C
  İyi:       10-15°C
  Ortalama:  15-20°C
  Düşük:     >20°C
```

#### 3.6 Evaporatör Yaklaşım Sıcaklığı
```
Mükemmel:  <2°C
İyi:       2-3°C
Ortalama:  3-4°C
Düşük:     >4°C
```

#### 3.7 Lift (Kondenser-Evaporatör Sıcaklık Farkı)
```
Düşük lift = Yüksek COP
Her 1°C lift azalması ≈ %2-3 COP artışı

Tipik değerler:
  Optimum: 20-25°C
  Normal:  25-35°C
  Yüksek:  >35°C
```

---

## 🔬 BÖLÜM 4: Formüller ve Hesaplamalar

### `/knowledge/formulas/chiller_exergy.md`

#### 4.1 Soğutma Yükü
```
Soğutma kapasitesi:
  Q_evap = m_chw × Cp × ΔT_chw

Burada:
  Q_evap = Soğutma kapasitesi (kW)
  m_chw = Soğutma suyu debisi (kg/s)
  Cp = Su özgül ısısı (4.186 kJ/kg·K)
  ΔT_chw = Giriş-çıkış sıcaklık farkı (tipik 5-7°C)
```

#### 4.2 COP Hesabı
```
COP = Q_evap / W_comp

Burada:
  Q_evap = Soğutma kapasitesi (kW)
  W_comp = Kompresör gücü (kW)

Carnot COP (teorik maksimum):
  COP_Carnot = T_evap / (T_cond - T_evap)
  
Not: T mutlak sıcaklık (Kelvin)
Örnek: T_evap=5°C=278K, T_cond=35°C=308K
  COP_Carnot = 278 / (308-278) = 9.27
```

#### 4.3 Soğutma Exergy'si
```
Soğutma exergy'si (evaporatörden çıkan):
  Ex_cool = Q_evap × (T₀/T_evap - 1)

Veya:
  Ex_cool = Q_evap × (1 - T_evap/T₀)

Burada:
  T₀ = Referans sıcaklık (298.15 K = 25°C)
  T_evap = Evaporatör sıcaklığı (K)

Örnek (Q=500kW, T_evap=5°C=278K):
  Ex_cool = 500 × (298.15/278 - 1)
  Ex_cool = 500 × 0.0725
  Ex_cool = 36.3 kW

Not: Soğutma exergy'si ısıtma exergy'sinden 
çok daha düşüktür çünkü T_evap ambient'e yakındır.
```

#### 4.4 Chiller Exergy Verimi
```
Exergy verimi:
  η_ex = Ex_cool / W_comp × 100%

Veya Carnot bazlı:
  η_ex = COP / COP_Carnot × 100%
  η_ex = COP × (T_cond - T_evap) / T_evap × 100%
```

#### 4.5 Kondenser Isı Atımı
```
Enerji dengesi:
  Q_cond = Q_evap + W_comp

Kondenser exergy kaybı:
  Ex_cond = Q_cond × (1 - T₀/T_cond)
```

#### 4.6 Kompresör İrreversibility
```
Kompresör exergy yıkımı:
  I_comp = W_comp - (Ex_out - Ex_in)

İzentropik verimlilik:
  η_is = W_isentropic / W_actual
  
Tipik değerler:
  Santrifüj: 0.75-0.85
  Vidalı: 0.70-0.80
  Scroll: 0.65-0.75
```

#### 4.7 Throttling (Genleşme) Kaybı
```
Genleşme valfi exergy yıkımı:
  I_throttle = m × T₀ × (s_out - s_in)

Bu kayıp termodinamik zorunluluktur.
Azaltma: Ekonomizer, flash tank, ejektör
```

#### 4.8 IPLV Hesabı
```
IPLV = 0.01×COP_100% + 0.42×COP_75% + 0.45×COP_50% + 0.12×COP_25%

Katsayılar yıllık tipik yük dağılımını temsil eder.
```

#### 4.9 Absorpsiyonlu Chiller Exergy
```
Termal COP:
  COP_th = Q_evap / Q_gen

Exergy verimi:
  η_ex = Ex_cool / Ex_heat_input

Ex_heat_input = Q_gen × (1 - T₀/T_gen)
```

---

## 💡 BÖLÜM 5: Çözüm Önerileri (Solutions)

Her çözüm için ayrı dosya:

### `/knowledge/solutions/chiller_vsd.md`
**VSD (Değişken Hız Sürücü) Uygulaması**
- Santrifüj chiller'da VSD
- Vidalı chiller'da VSD
- Kısmi yükte tasarruf potansiyeli
- Surge limitleri (santrifüj)
- Motor uyumluluğu
- Harmonik filtrasyon
- Tasarruf potansiyeli: %15-35
- Yatırım maliyeti
- Tipik ROI: 2-4 yıl

### `/knowledge/solutions/chiller_condenser_optimization.md`
**Kondenser Optimizasyonu**
- Kondenser suyu sıcaklığı düşürme
- Soğutma kulesi optimizasyonu
- Approach temperature iyileştirme
- Kondenser temizliği
- Her 1°C kondenser düşüşü ≈ %2-3 COP artışı
- Tasarruf potansiyeli: %5-15

### `/knowledge/solutions/chiller_chilled_water_reset.md`
**Soğutma Suyu Sıcaklığı Reset**
- Sabit vs değişken setpoint
- Load-based reset
- Outdoor reset
- Her 1°C evaporatör artışı ≈ %2-3 COP artışı
- Tasarruf potansiyeli: %3-10
- Dikkat: Nem kontrolü gereksinimleri

### `/knowledge/solutions/chiller_free_cooling.md`
**Serbest Soğutma (Free Cooling / Economizer)**
- Hava taraflı ekonomizer
- Su taraflı ekonomizer (waterside)
- Kule suyu ile direkt soğutma
- Geçiş sıcaklıkları
- İklim bölgelerine göre potansiyel
- Tasarruf potansiyeli: %10-40 (iklime bağlı)

### `/knowledge/solutions/chiller_sequencing.md`
**Chiller Sıralama Optimizasyonu**
- Optimal yük dağılımı
- Eşit yük vs verim bazlı
- Staging up/down stratejileri
- Minimum yük limitleri
- Tasarruf potansiyeli: %5-15

### `/knowledge/solutions/chiller_maintenance.md`
**Bakım ve Performans İyileştirme**
- Kondenser/evaporatör temizliği
- Soğutucu akışkan şarjı kontrolü
- Yağ yönetimi
- Purge unit (negatif basınçlı sistemler)
- Titreşim analizi
- Verim degradasyonu önleme

### `/knowledge/solutions/chiller_load_reduction.md`
**Soğutma Yükü Azaltma**
- Bina kabuğu iyileştirme
- İç kazançları azaltma
- Taze hava optimizasyonu
- Gece öncesi soğutma
- Demand control ventilation

### `/knowledge/solutions/chiller_delta_t.md`
**Delta-T Optimizasyonu**
- Düşük delta-T sendromu
- Nedenleri (üç yollu valf, bypass, oversized coils)
- Etkileri (pompaj enerjisi artışı, chiller kapasitesi düşüşü)
- Çözümler
- Tasarruf potansiyeli: %5-20

### `/knowledge/solutions/chiller_thermal_storage.md`
**Termal Depolama**
- Buz depolama (ice storage)
- Soğuk su depolama (chilled water storage)
- Pik talep yönetimi
- Enerji maliyet optimizasyonu
- Chiller boyut optimizasyonu

### `/knowledge/solutions/chiller_heat_recovery.md`
**Isı Geri Kazanım**
- Kondenser ısısından sıcak su üretimi
- Desuperheater uygulaması
- Eşzamanlı ısıtma-soğutma
- Tasarruf potansiyeli: %10-25 (ısıtma maliyetinden)

---

## 📋 BÖLÜM 6: Audit Metodolojisi

### `/knowledge/methodology/chiller_audit.md`

**Kapsamlı chiller audit prosedürü:**

#### 6.1 Ön Hazırlık
- Chiller nameplate bilgileri
- Soğutucu akışkan tipi ve şarj miktarı
- Tasarım kapasitesi ve koşulları
- Elektrik faturaları
- BMS/otomasyon verileri
- Bakım kayıtları

#### 6.2 Saha Ölçümleri
**Elektrik ölçümleri:**
- Kompresör gücü (kW)
- Kondenser fan/pompa gücü
- Toplam sistem gücü
- Güç faktörü

**Sıcaklık ölçümleri:**
- Soğutma suyu giriş/çıkış (CHW supply/return)
- Kondenser suyu giriş/çıkış
- Evaporatör soğutucu giriş/çıkış
- Kondenser soğutucu giriş/çıkış
- Dış ortam (hava soğutmalı için)

**Basınç ölçümleri:**
- Evaporatör basıncı (veya sıcaklıktan hesap)
- Kondenser basıncı
- Yağ basıncı

**Debi ölçümleri:**
- Soğutma suyu debisi
- Kondenser suyu debisi

#### 6.3 Performans Hesaplama
- Soğutma kapasitesi (kW veya ton)
- COP hesabı
- Approach temperature'lar
- Lift hesabı
- Exergy verimi

#### 6.4 Kısmi Yük Analizi
- Yük profili (BMS'den)
- Farklı yüklerde COP
- IPLV tahmini

#### 6.5 Standart Referanslar
- AHRI 550/590 (Water-chilling packages)
- AHRI 560 (Absorption chillers)
- ASHRAE 90.1 (Minimum efficiency)
- Eurovent certification
- ISO 50001

#### 6.6 Audit Checklist
- [ ] Nameplate bilgileri kaydedildi
- [ ] Elektrik ölçümleri yapıldı
- [ ] Sıcaklık ölçümleri yapıldı
- [ ] Debi ölçümleri yapıldı/tahmin edildi
- [ ] COP hesaplandı
- [ ] Approach temperature'lar belirlendi
- [ ] Yük profili incelendi
- [ ] Soğutucu akışkan seviyesi kontrol edildi
- [ ] Kondenser/evaporatör kirlenme değerlendirildi

---

## 🔍 BÖLÜM 7: Araştırma Kaynakları

**Claude Code, şu kaynaklardan derin araştırma yap:**

### 7.1 Akademik Kaynaklar
- Google Scholar: "chiller exergy analysis", "vapor compression exergy"
- ResearchGate: "chiller plant optimization"
- Anahtar makaleler:
  - "Exergy analysis of vapor compression refrigeration"
  - "Chiller plant efficiency optimization"
  - ASHRAE Journal makaleleri

### 7.2 Endüstri Kaynakları
- ASHRAE Handbooks (Fundamentals, HVAC Systems)
- AHRI Standards (550/590, 560)
- Eurovent guidelines
- US DOE "Improving Chilled Water System Performance"

### 7.3 Standartlar
- AHRI 550/590 (Water Chilling Packages)
- AHRI 560 (Absorption Chillers)
- ASHRAE 90.1 (Energy Standard)
- ISO 50001/50002

### 7.4 Üretici Kaynakları
- Carrier (teknik dökümanlar, application guides)
- Trane (Engineers Newsletter, chiller guides)
- York (Johnson Controls)
- Daikin
- Mitsubishi Electric
- LG
- Thermax (absorpsiyonlu)
- Broad (absorpsiyonlu)

---

## 📁 BÖLÜM 8: Oluşturulacak Dosyalar Özeti

```
/knowledge/
├── equipment/
│   ├── chiller_vapor_compression.md    # Genel buhar sıkıştırma
│   ├── chiller_screw.md                # Vidalı chiller
│   ├── chiller_centrifugal.md          # Santrifüj chiller
│   ├── chiller_scroll.md               # Scroll chiller
│   ├── chiller_reciprocating.md        # Pistonlu chiller
│   ├── chiller_absorption.md           # Absorpsiyonlu chiller
│   ├── chiller_air_cooled.md           # Hava soğutmalı
│   ├── chiller_water_cooled.md         # Su soğutmalı
│   ├── chiller_refrigerants.md         # Soğutucu akışkanlar
│   ├── cooling_tower.md                # Soğutma kulesi
│   └── chilled_water_systems.md        # Sistem genel bakış
│
├── solutions/
│   ├── chiller_vsd.md                  # VSD uygulaması
│   ├── chiller_condenser_optimization.md # Kondenser optimizasyonu
│   ├── chiller_chilled_water_reset.md  # CHW sıcaklık reset
│   ├── chiller_free_cooling.md         # Serbest soğutma
│   ├── chiller_sequencing.md           # Chiller sıralama
│   ├── chiller_maintenance.md          # Bakım
│   ├── chiller_load_reduction.md       # Yük azaltma
│   ├── chiller_delta_t.md              # Delta-T optimizasyonu
│   ├── chiller_thermal_storage.md      # Termal depolama
│   └── chiller_heat_recovery.md        # Isı geri kazanım
│
├── benchmarks/
│   └── chiller_benchmarks.md           # Tüm benchmark verileri
│
├── formulas/
│   └── chiller_exergy.md               # Exergy formülleri
│
└── methodology/
    └── chiller_audit.md                # Audit metodolojisi
```

**Toplam: 23 dosya**

---

## ⚠️ Önemli Notlar

1. **Format tutarlılığı:** Kompresör dosyalarındaki format ve yapıyı AYNEN koru
2. **Birim sistemi:** SI birimleri (kW, kJ, °C, bar) + ton (soğutma kapasitesi)
3. **Para birimi:** EUR (€)
4. **Exergy referans durumu:** T₀ = 25°C (298.15 K), P₀ = 1 atm
5. **Benchmark kategorileri:** poor, average, good, excellent
6. **Türkçe başlıklar, teknik terimler İngilizce parantez içinde**

---

## 🚀 Başlangıç Adımları

1. **ÖNCE** `/knowledge/equipment/compressor_screw.md` dosyasını oku — format template
2. **ÖNCE** `/knowledge/solutions/compressor_vsd.md` dosyasını oku — çözüm template  
3. **ÖNCE** `/knowledge/benchmarks/compressor_benchmarks.md` oku — benchmark template
4. **SONRA** web araştırması yap
5. **SONRA** dosyaları oluştur

---

## ✅ Tamamlama Kriterleri

- [ ] Tüm 23 dosya oluşturuldu
- [ ] Her dosya en az 100 satır (kapsamlı içerik)
- [ ] Formüller matematiksel olarak doğru
- [ ] Benchmark değerleri kaynaklı
- [ ] Türkçe başlıklar, tutarlı format
- [ ] Kompresör dosyalarıyla aynı yapı

---

**Bu brief chiller knowledge base için tek kaynak noktasıdır.**
