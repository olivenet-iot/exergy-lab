# ExergyLab Pompa (Pump) Knowledge Base Araştırma Brief

> **Claude Code için:** Bu dosyayı oku ve pompa modülü için kapsamlı knowledge base oluştur.

---

## 🎯 Görev Özeti

ExergyLab projesine **pompa (pump)** modülü ekliyoruz. Kompresör modülü zaten tamamlandı ve referans olarak kullanılacak.

**Görevin:**
1. Önce `/knowledge/` altındaki mevcut kompresör dosyalarını tara — format ve yapıyı anla
2. Aynı format ve derinlikte pompa knowledge base'i oluştur
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

Pompa dosyaları **AYNI FORMAT**ta olmalı:
- Aynı başlık hiyerarşisi
- Aynı tablo yapısı
- Aynı birim sistemi (kW, %, €, yıl)
- Aynı benchmark kategorileri (poor, average, good, excellent)
- Aynı öneri yapısı (tasarruf potansiyeli, yatırım, ROI)

---

## 💧 BÖLÜM 2: Pompa Araştırma Kapsamı

### 2.1 Pompa Tipleri (Equipment)

Her tip için ayrı dosya oluştur:

#### `/knowledge/equipment/pump_centrifugal.md`
**Santrifüj Pompa (Centrifugal Pump)**
- Çalışma prensibi (impeller, volüt, difüzör)
- Tek kademeli vs çok kademeli
- Kapasite aralığı (1-10,000+ m³/h)
- Basınç aralıkları (head: 10-500+ m)
- Verimlilik karakteristikleri (%60-90)
- Pompa eğrileri (H-Q, P-Q, η-Q)
- Spesifik hız (Ns) ve tip seçimi
- NPSH (Net Positive Suction Head) kavramı
- Kavitasyon ve önleme
- Exergy verimi aralıkları
- Tipik uygulamalar
- Başlıca üreticiler (Grundfos, KSB, Sulzer, Flowserve)

#### `/knowledge/equipment/pump_positive_displacement.md`
**Pozitif Deplasmanlı Pompalar (PD Pumps)**
- Pistonlu pompalar
- Diyafram pompalar
- Vida (screw) pompalar
- Dişli (gear) pompalar
- Lob pompalar
- Peristaltik pompalar
- Karakteristikler (sabit debi, değişken basınç)
- Verimlilik özellikleri
- Viskoz sıvılar için uygunluk
- Exergy analizi farklılıkları

#### `/knowledge/equipment/pump_submersible.md`
**Dalgıç Pompa (Submersible Pump)**
- Kuyu pompası (deep well)
- Drenaj/atıksu pompası
- Motor-pompa entegrasyonu
- Soğutma mekanizması
- Verimlilik karakteristikleri
- Kablo kayıpları (uzun kablo etkisi)
- Exergy verimi hesabı

#### `/knowledge/equipment/pump_vertical_turbine.md`
**Dikey Türbin Pompa (Vertical Turbine)**
- Çok kademeli dikey tasarım
- Kuyu ve sump uygulamaları
- Uzun şaft kayıpları
- Verimlilik karakteristikleri

#### `/knowledge/equipment/pump_axial_mixed.md`
**Eksenel ve Karışık Akışlı Pompalar**
- Eksenel (axial) pompalar - yüksek debi, düşük head
- Karışık akışlı (mixed flow) pompalar
- Propeller pompalar
- Sulama, drenaj uygulamaları
- Verimlilik karakteristikleri

#### `/knowledge/equipment/pump_vacuum.md`
**Vakum Pompaları**
- Sıvı halkalı (liquid ring)
- Kuru vidalı (dry screw)
- Roots blower
- Difüzyon pompaları
- Vakum seviyesi vs verimlilik
- Exergy analizi özellikleri

#### `/knowledge/equipment/pump_booster.md`
**Hidrofor / Basınç Artırıcı Sistemler**
- Tek pompa vs paralel pompa
- VSD kontrol
- Basınç tankı boyutlandırma
- On-off vs modulating kontrol
- Sistem verimi

#### `/knowledge/equipment/pumping_systems_overview.md`
**Pompalama Sistemleri Genel Bakış**
- Sistem eğrisi (system curve) kavramı
- Statik head vs dinamik head
- Seri ve paralel pompa operasyonu
- Throttling vs VSD kontrol karşılaştırması
- Bypass hatları
- Minimum akış koruma
- Sistem seviyesi exergy akışı

### 2.2 Motor ve Sürücü Entegrasyonu

`/knowledge/equipment/pump_motors_drives.md` dosyasında:
- Elektrik motorları (IE1, IE2, IE3, IE4 sınıfları)
- Motor verimlilik standartları (IEC 60034-30)
- Kısmi yük verimi
- VSD (Variable Speed Drive) temelleri
- Affinity laws (benzerlik yasaları)
- Motor-pompa eşleştirme
- Güç faktörü

---

## 📊 BÖLÜM 3: Benchmark Verileri

### `/knowledge/benchmarks/pump_benchmarks.md`

**Araştırılacak benchmark metrikleri:**

#### 3.1 Pompa Verimi (Pump Efficiency)
```
BEP (Best Efficiency Point) bazında:
  Mükemmel:  >85%
  İyi:       75-85%
  Ortalama:  65-75%
  Düşük:     <65%

Not: Verimlilik pompa boyutu ve tipine göre değişir
Küçük pompalar (<10 kW): BEP %60-75
Orta pompalar (10-100 kW): BEP %75-88
Büyük pompalar (>100 kW): BEP %85-93
```

#### 3.2 Motor Verimi
```
IE4 (Super Premium): >95%
IE3 (Premium): 92-95%
IE2 (High): 88-92%
IE1 (Standard): 85-88%

Kısmi yük etkisi:
  100% yük: Nominal verim
  75% yük: -1-2%
  50% yük: -3-5%
  25% yük: -8-15%
```

#### 3.3 Sistem Verimi (Wire-to-Water)
```
Mükemmel:  >70% (VSD, optimum sizing)
İyi:       55-70%
Ortalama:  40-55%
Düşük:     <40% (oversized, throttled)
```

#### 3.4 Spesifik Enerji Tüketimi
```
Temiz su pompası:
  kWh/m³ @ belirli head

Örnek (50m head):
  Mükemmel:  <0.18 kWh/m³
  İyi:       0.18-0.22 kWh/m³
  Ortalama:  0.22-0.28 kWh/m³
  Düşük:     >0.28 kWh/m³
```

#### 3.5 BEP'ten Sapma Etkisi
| BEP'e göre debi | Verim düşüşü | Ömür etkisi |
|-----------------|--------------|-------------|
| 80-120% | 0-2% | Normal |
| 60-80% | 5-10% | Azalır |
| <60% | >15% | Ciddi hasar riski |

#### 3.6 Throttling vs VSD Karşılaştırma
```
%50 debi gerektiğinde:
  Throttling: Pompa gücü ≈ %80 (verimsiz)
  VSD: Pompa gücü ≈ %15-20 (affinity laws)
  
Tasarruf: %60-75 (yüke bağlı)
```

#### 3.7 Exergy Verimi
```
Pompa sistemi exergy verimi:
  Mükemmel:  >65%
  İyi:       50-65%
  Ortalama:  35-50%
  Düşük:     <35%

Kayıp dağılımı (tipik %50 verimli sistem):
  - Hidrolik kayıp: %15-25
  - Motor kayıp: %5-10
  - VSD kayıp (varsa): %3-5
  - Mekanik kayıp: %2-5
  - Throttling kayıp: %10-30 (varsa)
```

---

## 🔬 BÖLÜM 4: Formüller ve Hesaplamalar

### `/knowledge/formulas/pump_exergy.md`

#### 4.1 Hidrolik Güç
```
Hidrolik güç (ideal pompa gücü):
  P_hyd = ρ × g × Q × H / 1000

Burada:
  P_hyd = Hidrolik güç (kW)
  ρ = Sıvı yoğunluğu (kg/m³)
  g = Yerçekimi ivmesi (9.81 m/s²)
  Q = Debi (m³/s)
  H = Toplam head (m)

Alternatif formül:
  P_hyd = Q × ΔP / 1000
  
Burada:
  Q = Debi (m³/s)
  ΔP = Basınç farkı (kPa)
```

#### 4.2 Şaft Gücü ve Pompa Verimi
```
Şaft gücü:
  P_shaft = P_hyd / η_pump

Pompa verimi:
  η_pump = P_hyd / P_shaft × 100%

Tipik değerler:
  Küçük (<5 kW): %50-70
  Orta (5-50 kW): %70-85
  Büyük (>50 kW): %80-90
```

#### 4.3 Elektrik Gücü ve Sistem Verimi
```
Elektrik gücü (şebekeden çekilen):
  P_elec = P_shaft / (η_motor × η_VSD)

Wire-to-water verimi:
  η_system = P_hyd / P_elec × 100%
  η_system = η_pump × η_motor × η_VSD × η_mechanical
```

#### 4.4 Affinity Laws (Benzerlik Yasaları)
```
Hız değişimi etkisi:
  Q₂/Q₁ = n₂/n₁
  H₂/H₁ = (n₂/n₁)²
  P₂/P₁ = (n₂/n₁)³

Burada:
  Q = Debi
  H = Head
  P = Güç
  n = Devir (rpm)

ÖNEMLİ: %50 hız = %12.5 güç (teorik)
Gerçekte: %15-20 (verim düşüşü nedeniyle)
```

#### 4.5 Exergy Analizi
```
Pompa giren exergy:
  Ex_in = P_elec (elektrik exergy'si ≈ %100 enerji)

Pompa çıkan exergy (faydalı):
  Ex_out = ρ × Q × g × H (potansiyel enerji artışı)
  
Veya basınç bazlı:
  Ex_out = Q × ΔP

Pompa exergy verimi:
  η_ex = Ex_out / Ex_in × 100%
```

#### 4.6 Throttling Kaybı
```
Throttle valve exergy yıkımı:
  Ex_throttle = Q × ΔP_valve

Burada ΔP_valve = sistem ΔP - pompa ΔP (at operating point)

Throttling'in exergy verimi etkisi:
  Throttle olmadan: η_ex = η_pump × η_motor
  Throttle ile: η_ex = η_pump × η_motor × (H_required/H_pump)
```

#### 4.7 Sistem Eğrisi
```
Sistem head'i:
  H_system = H_static + K × Q²

Burada:
  H_static = Statik head (m) - yükseklik farkı + tank basıncı
  K = Sistem sabiti (sürtünme)
  Q = Debi

Operasyon noktası: Pompa eğrisi ve sistem eğrisinin kesişimi
```

#### 4.8 NPSH Hesabı
```
NPSH available:
  NPSH_a = (P_atm - P_vapor)/ρg + H_suction - H_loss

Kavitasyon koşulu:
  NPSH_a > NPSH_r + güvenlik marjı (tipik 0.5-1m)
```

---

## 💡 BÖLÜM 5: Çözüm Önerileri (Solutions)

Her çözüm için ayrı dosya:

### `/knowledge/solutions/pump_vsd.md`
**Değişken Hız Sürücü (VSD/VFD) Uygulaması**
- Affinity laws ve gerçek tasarruf
- Uygulama kriterleri (ne zaman VSD?)
- Minimum hız limitleri
- Kavitasyon riski düşük hızda
- Motor uyumluluğu
- Tasarruf potansiyeli: %20-60
- Yatırım maliyeti: pompa gücüne göre €/kW
- Tipik ROI: 1-3 yıl
- Sistem eğrisi türüne göre tasarruf (yüksek statik head = düşük tasarruf)

### `/knowledge/solutions/pump_impeller_trimming.md`
**İmpeller Kesme/Değiştirme**
- İmpeller çapı ve performans ilişkisi
- Kesme limitleri (genelde max %15-20)
- Verimlilik etkisi
- Kalıcı çözüm olarak avantaj
- VSD ile karşılaştırma
- Tasarruf potansiyeli: %10-25

### `/knowledge/solutions/pump_right_sizing.md`
**Pompa Boyutlandırma Optimizasyonu**
- Oversizing problemi (çok yaygın: %30-50 fazla kapasite)
- Doğru boyut seçimi kriterleri
- Paralel pompa alternatifi
- Değişken talep için yaklaşım
- Tasarruf potansiyeli: %15-40

### `/knowledge/solutions/pump_parallel_operation.md`
**Paralel Pompa Operasyonu**
- İki pompa eğrisinin birleşimi
- Sequencing stratejileri
- Lead-lag operasyon
- Duty/standby
- Verimlilik optimizasyonu
- Tasarruf potansiyeli: %10-20

### `/knowledge/solutions/pump_system_optimization.md`
**Sistem Optimizasyonu**
- Boru çapı artırma (sürtünme azaltma)
- Dirsek ve vana kayıpları
- Bypass eliminasyonu
- Deadhead protection alternatifleri
- Tasarruf potansiyeli: %5-15

### `/knowledge/solutions/pump_motor_upgrade.md`
**Motor Yükseltme (IE2 → IE3/IE4)**
- Verimlilik farkları
- Maliyet-fayda analizi
- Geri ödeme süresi hesabı
- Hangi durumlarda değer?
- Tasarruf potansiyeli: %2-8

### `/knowledge/solutions/pump_maintenance.md`
**Bakım ve Performans İzleme**
- Aşınma etkisi (impeller, wear rings)
- Verim degradasyonu (%1-2/yıl tipik)
- Titreşim analizi
- Performans testi (flow, head, power)
- Predictive maintenance
- Wear ring değişimi etkisi

### `/knowledge/solutions/pump_throttle_elimination.md`
**Throttle Valf Eliminasyonu**
- Throttling'in enerji israfı
- Alternatifler: VSD, bypass, impeller trim
- Hangi durumda hangisi?
- Tasarruf potansiyeli: %20-50

### `/knowledge/solutions/pump_cavitation_prevention.md`
**Kavitasyon Önleme**
- Kavitasyon nedenleri ve belirtileri
- NPSH margin artırma
- Impeller hasarı ve verim kaybı
- Çözüm yaklaşımları

### `/knowledge/solutions/pump_control_optimization.md`
**Kontrol Optimizasyonu**
- On-off vs modulating kontrol
- Pressure setpoint optimization
- Demand-based kontrol
- Building automation entegrasyonu
- Hidrofor sistemleri için özel öneriler

---

## 📋 BÖLÜM 6: Audit Metodolojisi

### `/knowledge/methodology/pump_audit.md`

**Kapsamlı pompa audit prosedürü:**

#### 6.1 Ön Hazırlık
- Pompa nameplate bilgileri
- Motor nameplate bilgileri
- Pompa eğrileri (varsa)
- Elektrik faturaları
- Proses gereksinimleri (debi, basınç)
- Çalışma profili (saat/gün, gün/yıl)

#### 6.2 Saha Ölçümleri
**Elektrik ölçümleri:**
- Güç (kW) - power analyzer
- Akım (A)
- Gerilim (V)
- Güç faktörü (PF)
- Harmonik (varsa VSD)

**Hidrolik ölçümler:**
- Emme basıncı (bar veya mSS)
- Basma basıncı (bar veya mSS)
- Debi (m³/h) - ultrasonik veya manyetik flowmeter

**Diğer:**
- Titreşim
- Sıcaklık (motor, rulman)
- Ses seviyesi

#### 6.3 Verimlilik Hesaplama
- Hidrolik güç hesabı
- Şaft gücü tahmini
- Motor verimi (eğriden veya ölçüm)
- Wire-to-water verim
- Exergy verimi

#### 6.4 BEP Analizi
- Mevcut operasyon noktası
- BEP'e göre konum
- Sapmanın verim etkisi

#### 6.5 Standart Referanslar
- ISO 9906 (Pompa test standardı)
- Europump Guides
- Hydraulic Institute Standards
- IEC 60034-30 (Motor verimlilik)
- ISO 50001 (Enerji yönetimi)

#### 6.6 Audit Checklist
- [ ] Nameplate bilgileri kaydedildi
- [ ] Elektrik ölçümleri yapıldı
- [ ] Basınç ölçümleri yapıldı
- [ ] Debi ölçümü yapıldı (veya tahmin)
- [ ] Throttle valf pozisyonu not edildi
- [ ] Çalışma profili belirlendi
- [ ] Pompa eğrisi üzerinde nokta işaretlendi
- [ ] Titreşim kontrolü yapıldı

---

## 🔍 BÖLÜM 7: Araştırma Kaynakları

**Claude Code, şu kaynaklardan derin araştırma yap:**

### 7.1 Akademik Kaynaklar
- Google Scholar: "pump exergy analysis", "pumping system efficiency"
- ResearchGate: "centrifugal pump optimization"
- Anahtar makaleler:
  - "Energy efficiency of pumping systems" (European Commission)
  - Europump Guide to Variable Speed Pumping
  - "Exergy analysis of pumping systems" araştırmaları

### 7.2 Endüstri Kaynakları
- US DOE "Improving Pumping System Performance"
- Hydraulic Institute (HI) Energy Rating Program
- Europump Guides
- BPMA (British Pump Manufacturers Association)

### 7.3 Standartlar
- ISO 9906 (Hydraulic performance testing)
- IEC 60034-30 (Motor efficiency classes)
- ISO 50001/50002 (Energy management)
- EN 16480 (Minimum efficiency - Extended Product)

### 7.4 Üretici Kaynakları
- Grundfos (pump sizing tools, white papers)
- KSB (technical documentation)
- Sulzer
- Flowserve
- Xylem (Bell & Gossett, Goulds)
- Wilo
- DAB

---

## 📁 BÖLÜM 8: Oluşturulacak Dosyalar Özeti

```
/knowledge/
├── equipment/
│   ├── pump_centrifugal.md           # Santrifüj pompa
│   ├── pump_positive_displacement.md # PD pompalar
│   ├── pump_submersible.md           # Dalgıç pompa
│   ├── pump_vertical_turbine.md      # Dikey türbin
│   ├── pump_axial_mixed.md           # Eksenel/karışık akış
│   ├── pump_vacuum.md                # Vakum pompaları
│   ├── pump_booster.md               # Hidrofor sistemleri
│   ├── pump_motors_drives.md         # Motor ve sürücüler
│   └── pumping_systems_overview.md   # Sistem genel bakış
│
├── solutions/
│   ├── pump_vsd.md                   # VSD uygulaması
│   ├── pump_impeller_trimming.md     # İmpeller kesme
│   ├── pump_right_sizing.md          # Boyut optimizasyonu
│   ├── pump_parallel_operation.md    # Paralel operasyon
│   ├── pump_system_optimization.md   # Sistem optimizasyonu
│   ├── pump_motor_upgrade.md         # Motor yükseltme
│   ├── pump_maintenance.md           # Bakım
│   ├── pump_throttle_elimination.md  # Throttle eliminasyonu
│   ├── pump_cavitation_prevention.md # Kavitasyon önleme
│   └── pump_control_optimization.md  # Kontrol optimizasyonu
│
├── benchmarks/
│   └── pump_benchmarks.md            # Tüm benchmark verileri
│
├── formulas/
│   └── pump_exergy.md                # Exergy formülleri
│
└── methodology/
    └── pump_audit.md                 # Audit metodolojisi
```

**Toplam: 21 dosya** (kazan ile aynı)

---

## ⚠️ Önemli Notlar

1. **Format tutarlılığı:** Kompresör dosyalarındaki format ve yapıyı AYNEN koru
2. **Birim sistemi:** SI birimleri (kW, kJ, m, m³/h, bar)
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

- [ ] Tüm 21 dosya oluşturuldu
- [ ] Her dosya en az 100 satır (kapsamlı içerik)
- [ ] Formüller matematiksel olarak doğru
- [ ] Benchmark değerleri kaynaklı
- [ ] Türkçe başlıklar, tutarlı format
- [ ] Kompresör dosyalarıyla aynı yapı

---

**Bu brief pompa knowledge base için tek kaynak noktasıdır.**
