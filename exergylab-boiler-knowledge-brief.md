# ExergyLab Kazan (Boiler) Knowledge Base Araştırma Brief

> **Claude Code için:** Bu dosyayı oku ve kazan modülü için kapsamlı knowledge base oluştur.

---

## 🎯 Görev Özeti

ExergyLab projesine **kazan (boiler)** modülü ekliyoruz. Kompresör modülü zaten tamamlandı ve referans olarak kullanılacak.

**Görevin:**
1. Önce `/knowledge/` altındaki mevcut kompresör dosyalarını tara — format ve yapıyı anla
2. Aynı format ve derinlikte kazan knowledge base'i oluştur
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
│   ├── compressor_scroll.md
│   ├── compressor_centrifugal.md
│   └── compressed_air_systems.md
│
├── solutions/
│   ├── compressor_vsd.md
│   ├── compressor_air_leaks.md
│   ├── compressor_pressure_optimization.md
│   ├── compressor_heat_recovery.md
│   ├── compressor_maintenance.md
│   ├── compressor_dryer_optimization.md
│   ├── compressor_inlet_optimization.md
│   └── compressor_system_design.md
│
├── benchmarks/
│   └── compressor_benchmarks.md
│
├── formulas/
│   └── compressor_exergy.md
│
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

Kazan dosyaları **AYNI FORMAT**ta olmalı:
- Aynı başlık hiyerarşisi
- Aynı tablo yapısı
- Aynı birim sistemi (kW, %, €, yıl)
- Aynı benchmark kategorileri (poor, average, good, excellent)
- Aynı öneri yapısı (tasarruf potansiyeli, yatırım, ROI)

---

## 🔥 BÖLÜM 2: Kazan Araştırma Kapsamı

### 2.1 Kazan Tipleri (Equipment)

Her tip için ayrı dosya oluştur:

#### `/knowledge/equipment/boiler_steam_firetube.md`
**Ateş Borulu Buhar Kazanı (Fire-tube)**
- Çalışma prensibi (Scotch marine, ekonomizer entegrasyonu)
- Kapasite aralığı (tipik 1-30 ton/saat buhar)
- Basınç aralıkları (10-25 bar)
- Verimlilik karakteristikleri (%80-88 tipik)
- Exergy verimi aralıkları
- Avantaj/dezavantajlar
- Tipik uygulamalar (tekstil, gıda, kimya)
- Başlıca üreticiler ve model örnekleri

#### `/knowledge/equipment/boiler_steam_watertube.md`
**Su Borulu Buhar Kazanı (Water-tube)**
- Çalışma prensibi
- Kapasite aralığı (büyük kapasiteler, 30-500+ ton/saat)
- Yüksek basınç uygulamaları (40-100+ bar)
- Süperkritik uygulamalar
- Verimlilik karakteristikleri
- Exergy verimi aralıkları
- Tipik uygulamalar (enerji santralleri, büyük endüstri)

#### `/knowledge/equipment/boiler_hotwater.md`
**Sıcak Su Kazanı (Hot Water Boiler)**
- Düşük basınç sistemleri (<6 bar)
- Kapasite aralıkları
- Dönüş suyu sıcaklığı etkisi
- Kondensing vs non-condensing
- Verimlilik karakteristikleri
- Exergy verimi aralıkları
- Tipik uygulamalar (bina ısıtma, proses)

#### `/knowledge/equipment/boiler_condensing.md`
**Yoğuşmalı Kazan (Condensing Boiler)**
- Yoğuşma prensibi ve avantajı
- Baca gazı sıcaklığı ve çiğ noktası
- Dönüş suyu sıcaklığı kritikliği (<55°C ideal)
- Verimlilik >100% (LHV bazlı) açıklaması
- HHV vs LHV farkı
- Exergy verimi aralıkları
- Korozyon riskleri ve malzeme seçimi

#### `/knowledge/equipment/boiler_waste_heat.md`
**Atık Isı Kazanı (Waste Heat Recovery Boiler / HRSG)**
- Gaz türbini, motor vb. atık ısı kaynakları
- HRSG (Heat Recovery Steam Generator) tasarımı
- Pinch point analizi
- Supplementary firing
- Kombine çevrim entegrasyonu
- Exergy verimi karakteristikleri

#### `/knowledge/equipment/boiler_electric.md`
**Elektrikli Kazan (Electric Boiler)**
- Elektrot tipi vs rezistans tipi
- Verimlilik (%98-99.9)
- Exergy analizi (elektrik → ısı dönüşümü, yüksek exergy yıkımı)
- Kullanım senaryoları (peak shaving, yedek)
- Maliyet karşılaştırması

#### `/knowledge/equipment/boiler_biomass.md`
**Biyokütle Kazanı**
- Yakıt tipleri (pellet, odun yongası, tarımsal atık)
- Yanma karakteristikleri
- Kül yönetimi
- Verimlilik ve exergy analizi
- Emisyon özellikleri

#### `/knowledge/equipment/steam_systems_overview.md`
**Buhar Sistemleri Genel Bakış**
- Buhar üretim, dağıtım, kullanım döngüsü
- Kondensat geri dönüşü
- Flash buhar recovery
- Steam trap'ler ve önemi
- Deaerator
- Blowdown sistemi
- Sistem seviyesi exergy akışı

### 2.2 Yakıt Tipleri ve Özellikleri

`/knowledge/equipment/boiler_fuels.md` dosyasında:
- Doğalgaz (LHV, HHV, kompozisyon)
- LPG
- Fuel oil (No.2, No.6)
- Kömür (türleri, kalorifik değerler)
- Biyokütle
- Kimyasal exergy değerleri (kJ/kg veya kJ/m³)
- Stokiyometrik hava ihtiyacı
- Teorik yanma sıcaklıkları

---

## 📊 BÖLÜM 3: Benchmark Verileri

### `/knowledge/benchmarks/boiler_benchmarks.md`

**Araştırılacak benchmark metrikleri:**

#### 3.1 Yanma Verimi (Combustion Efficiency)
```
Mükemmel:  >92% (modern kondensing)
İyi:       88-92%
Ortalama:  82-88%
Düşük:     <82%
```

#### 3.2 Toplam Verimlilik (Overall Thermal Efficiency)
- Direkt yöntem: (Buhar entalpisi × debi) / (Yakıt × LHV)
- Indirekt yöntem: 100% - kayıplar toplamı
- LHV vs HHV bazlı farklar

#### 3.3 Exergy Verimi
```
Buhar kazanı tipik aralıklar:
  Mükemmel:  >45%
  İyi:       35-45%
  Ortalama:  25-35%
  Düşük:     <25%

Not: Exergy verimi HER ZAMAN enerji veriminden düşüktür
çünkü yanma tersinmezliği büyük exergy yıkımına neden olur.
```

#### 3.4 Spesifik Yakıt Tüketimi
- m³ doğalgaz / ton buhar
- kg fuel oil / ton buhar
- Basınç ve sıcaklığa göre düzeltme

#### 3.5 Kayıp Dağılımı Benchmarkları
| Kayıp Türü | İyi | Ortalama | Kötü |
|------------|-----|----------|------|
| Baca gazı (kuru) | <8% | 8-12% | >12% |
| Baca gazı (yaş) | <4% | 4-8% | >8% |
| Radyasyon | <1% | 1-2% | >2% |
| Blowdown | <1% | 1-3% | >3% |
| Yanmamış yakıt | <0.5% | 0.5-1% | >1% |

#### 3.6 Excess Air (Fazla Hava) Benchmarkları
| Yakıt | Optimum O₂ | Optimum Excess Air |
|-------|------------|-------------------|
| Doğalgaz | 2-3% | 10-15% |
| Fuel oil | 3-4% | 15-20% |
| Kömür | 4-6% | 20-30% |

#### 3.7 Yaşa Göre Verimlilik Degradasyonu
- Yeni kazan: Referans
- 5 yıl: -1-2%
- 10 yıl: -2-4%
- 15+ yıl: -3-6%
- Bakım kalitesine göre varyasyon

---

## 🔬 BÖLÜM 4: Formüller ve Hesaplamalar

### `/knowledge/formulas/boiler_exergy.md`

#### 4.1 Yakıt Exergy'si
```
Yakıt kimyasal exergy'si:
  Ex_fuel = m_fuel × ex_ch

Doğalgaz için:
  ex_ch ≈ 51,850 kJ/kg (veya ~38,200 kJ/m³ @ STP)
  
Fuel oil için:
  ex_ch ≈ 45,000-47,000 kJ/kg

Kömür için:
  ex_ch ≈ 25,000-32,000 kJ/kg (türüne göre)
```

#### 4.2 Buhar Exergy'si
```
Buhar fiziksel exergy'si:
  Ex_steam = m × [(h - h₀) - T₀ × (s - s₀)]

Burada:
  h, s = Buhar entalpisi ve entropisi (kJ/kg, kJ/kg·K)
  h₀, s₀ = Referans durumu (25°C, 1 atm sıvı su)
  T₀ = Referans sıcaklığı (298.15 K)

Örnek (10 bar doymuş buhar):
  h = 2778 kJ/kg, s = 6.59 kJ/kg·K
  h₀ = 104.9 kJ/kg, s₀ = 0.367 kJ/kg·K
  Ex_steam = (2778-104.9) - 298.15×(6.59-0.367)
  Ex_steam ≈ 818 kJ/kg
```

#### 4.3 Baca Gazı Exergy Kaybı
```
Baca gazı exergy kaybı:
  Ex_flue = m_flue × [(h_flue - h₀) - T₀ × (s_flue - s₀)]

Basitleştirilmiş (sadece sensible heat):
  Ex_flue ≈ m_flue × Cp × (T_flue - T₀) × [1 - T₀/T_flue]

Not: T_flue ve T₀ Kelvin cinsinden
```

#### 4.4 Yanma İrreversibility'si
```
Yanma tersinmezliği (entropi üretimi):
  I_comb = T₀ × S_gen

Yaklaşık değer (doğalgaz):
  Yanma exergy yıkımı ≈ %25-30 yakıt exergy'si

Bu kayıp TERMODİNAMİK ZORUNLULUKTUR ve azaltılamaz!
(Sadece yakıt hücresi gibi direkt dönüşümle azaltılabilir)
```

#### 4.5 Toplam Exergy Verimi
```
η_ex = Ex_steam / Ex_fuel × 100%

Veya detaylı:
η_ex = Ex_steam / (Ex_fuel + Ex_air + Ex_water)
```

#### 4.6 İndirekt Yöntem (Kayıp Analizi)
```
Enerji verimi (indirekt):
  η_th = 100% - L_flue - L_radiation - L_blowdown - L_unburnt

Exergy verimi (indirekt):
  η_ex = 100% - I_combustion - Ex_flue - Ex_radiation - Ex_blowdown
  
Not: I_combustion (yanma tersinmezliği) EN BÜYÜK kayıptır (~25-30%)
```

#### 4.7 Economizer Etkisi
```
Baca gazı sıcaklığı düşürme etkisi:
  Her 20°C düşüş ≈ %1 verimlilik artışı

Economizer tasarruf hesabı:
  Q_econ = m_flue × Cp × (T_in - T_out)
  Yakıt tasarrufu = Q_econ / (LHV × η_boiler)
```

#### 4.8 Blowdown Kaybı
```
Blowdown enerji kaybı:
  L_blowdown = m_blowdown × h_blowdown / (m_feedwater × h_steam)

Blowdown oranı:
  Tipik: %1-3
  Kötü su kalitesi: %5-10
  
Blowdown heat recovery potansiyeli:
  Q_recovery = m_blowdown × (h_blowdown - h_makeup)
```

---

## 💡 BÖLÜM 5: Çözüm Önerileri (Solutions)

Her çözüm için ayrı dosya:

### `/knowledge/solutions/boiler_economizer.md`
**Economizer (Baca Gazı Isı Geri Kazanımı)**
- Çalışma prensibi
- Tasarım kriterleri (pinch point, approach temperature)
- Kondensing vs non-condensing economizer
- Asit çiğ noktası riski ve malzeme seçimi
- Tasarruf potansiyeli: %4-8
- Yatırım maliyeti: kapasite bazlı €/kW
- Tipik ROI: 1-3 yıl
- Uygulama kısıtları

### `/knowledge/solutions/boiler_air_preheater.md`
**Hava Ön Isıtıcı (Air Preheater)**
- Rejeneratif vs rekuperatif tipler
- Yanma verimi artışı
- Tasarruf potansiyeli: %2-5
- Economizer ile karşılaştırma
- Uygulama kriterleri

### `/knowledge/solutions/boiler_oxygen_control.md`
**O₂ Trim / Excess Air Kontrolü**
- Fazla hava etkisi (her %1 excess air ≈ %0.5 verim kaybı)
- O₂ analiz cihazları (zirkonya prob, paramanyetik)
- Modulating burner avantajı
- Tasarruf potansiyeli: %1-3
- Yatırım maliyeti: €2,000-10,000
- ROI: <1 yıl genellikle

### `/knowledge/solutions/boiler_blowdown_recovery.md`
**Blowdown Isı Geri Kazanımı**
- Flash tank sistemi
- Heat exchanger sistemi
- Otomatik blowdown kontrolü
- Tasarruf potansiyeli: %1-3
- Su kalitesi yönetimi ile entegrasyon

### `/knowledge/solutions/boiler_condensate_return.md`
**Kondensat Geri Dönüşü**
- Kondensat enerji içeriği (tipik 80-90°C)
- Geri dönüş oranı benchmarkları (iyi: >80%)
- Geri dönüşün yakıt tasarrufuna etkisi
- Su maliyeti tasarrufu
- Kontaminasyon riskleri

### `/knowledge/solutions/boiler_steam_trap_management.md`
**Buhar Kapanı (Steam Trap) Yönetimi**
- Steam trap tipleri (termodinamik, termostatic, mekanik)
- Arıza modları (açık kalma, kapalı kalma)
- Test yöntemleri (ultrasonik, sıcaklık)
- Arızalı trap maliyeti: ton/yıl buhar kaybı
- Survey programı oluşturma
- Tasarruf potansiyeli: %5-15 (ihmal edilmiş sistemlerde)

### `/knowledge/solutions/boiler_insulation.md`
**İzolasyon İyileştirme**
- Yüzey sıcaklığı ölçümü
- Izolasyon kalınlığı optimizasyonu
- Çıplak flanş, vana izolasyonu
- Radyasyon kaybı formülü
- Tasarruf potansiyeli: %1-3

### `/knowledge/solutions/boiler_load_optimization.md`
**Yük Optimizasyonu ve Çoklu Kazan Kontrolü**
- Kazan verimlilik eğrisi (yük vs verim)
- Optimal yük aralığı (tipik %50-80)
- Sequencing stratejileri (çoklu kazan)
- Standby kayıpları
- Turn-down ratio önemi

### `/knowledge/solutions/boiler_combustion_tuning.md`
**Yanma Ayarı (Combustion Tuning)**
- Hava-yakıt oranı optimizasyonu
- Brülör bakımı
- Alev kalitesi analizi
- CO vs O₂ dengesi
- Tasarruf potansiyeli: %1-4

### `/knowledge/solutions/boiler_feedwater_treatment.md`
**Besleme Suyu Arıtma**
- Sertlik, TDS, pH kontrolü
- Deaerator önemi (O₂ giderme)
- Blowdown oranı ile ilişki
- Korozyon ve kireç önleme
- Uzun vadeli verimlilik koruma

---

## 📋 BÖLÜM 6: Audit Metodolojisi

### `/knowledge/methodology/boiler_audit.md`

**Kapsamlı kazan audit prosedürü:**

#### 6.1 Ön Hazırlık
- Kazan nameplate bilgileri toplama
- Yakıt faturaları (son 12 ay)
- Üretim verileri (buhar tüketimi)
- Mevcut ölçüm cihazları envanteri
- Bakım kayıtları

#### 6.2 Saha Ölçümleri
**Baca gazı analizi:**
- O₂ (%)
- CO (ppm)
- CO₂ (%)
- Baca gazı sıcaklığı (°C)
- Ortam sıcaklığı (°C)

**Sıcaklık ölçümleri:**
- Besleme suyu sıcaklığı
- Buhar sıcaklığı
- Blowdown sıcaklığı
- Kazan yüzey sıcaklıkları
- Economizer giriş/çıkış

**Basınç ölçümleri:**
- Buhar basıncı
- Besleme suyu basıncı
- Yakıt basıncı

**Debi ölçümleri (varsa):**
- Buhar debisi
- Yakıt debisi
- Besleme suyu debisi

#### 6.3 Verimlilik Hesaplama
- Direkt yöntem formülü
- İndirekt yöntem (kayıp analizi)
- Exergy verimi hesabı

#### 6.4 Standart Referanslar
- ASME PTC 4 (Fired Steam Generators)
- EN 12952/12953 (Avrupa kazan standartları)
- BS 845 (UK verimlilik test standardı)
- ISO 50001 (Enerji yönetimi)

#### 6.5 Audit Checklist
- [ ] Nameplate bilgileri kaydedildi
- [ ] Baca gazı analizi yapıldı
- [ ] Yüzey sıcaklıkları ölçüldü
- [ ] Blowdown oranı belirlendi
- [ ] Steam trap survey yapıldı
- [ ] Kondensat geri dönüş oranı ölçüldü
- [ ] İzolasyon durumu değerlendirildi
- [ ] Brülör durumu incelendi

---

## 🔍 BÖLÜM 7: Araştırma Kaynakları

**Claude Code, şu kaynaklardan derin araştırma yap:**

### 7.1 Akademik Kaynaklar
- Google Scholar: "boiler exergy analysis"
- ResearchGate: "steam boiler efficiency optimization"
- ScienceDirect: "combustion irreversibility exergy"
- Anahtar makaleler:
  - Bejan "Advanced Engineering Thermodynamics" (exergy teori)
  - Kotas "The Exergy Method" (endüstriyel uygulamalar)
  - Rosen, Dincer makaleleri (exergy efficiency)

### 7.2 Endüstri Kaynakları
- US DOE Steam Guides (energy.gov)
- CIBO (Council of Industrial Boiler Owners)
- ABMA (American Boiler Manufacturers Association)
- Spirax Sarco teknik dökümanlar
- Cleaver-Brooks teknik kılavuzlar

### 7.3 Standartlar
- ASME PTC 4 (Performance Test Code)
- EN 12952/12953 (European Standards)
- BS 845 (British Standard)
- ISO 50001/50002 (Energy Management)

### 7.4 Üretici Kaynakları
- Bosch (Buderus)
- Viessmann
- Cleaver-Brooks
- Miura
- Fulton
- Aalborg (HRSG)

---

## 📁 BÖLÜM 8: Oluşturulacak Dosyalar Özeti

```
/knowledge/
├── equipment/
│   ├── boiler_steam_firetube.md      # Ateş borulu buhar kazanı
│   ├── boiler_steam_watertube.md     # Su borulu buhar kazanı
│   ├── boiler_hotwater.md            # Sıcak su kazanı
│   ├── boiler_condensing.md          # Yoğuşmalı kazan
│   ├── boiler_waste_heat.md          # Atık ısı kazanı / HRSG
│   ├── boiler_electric.md            # Elektrikli kazan
│   ├── boiler_biomass.md             # Biyokütle kazanı
│   ├── boiler_fuels.md               # Yakıt özellikleri
│   └── steam_systems_overview.md     # Buhar sistemi genel bakış
│
├── solutions/
│   ├── boiler_economizer.md          # Economizer
│   ├── boiler_air_preheater.md       # Hava ön ısıtıcı
│   ├── boiler_oxygen_control.md      # O₂ kontrolü
│   ├── boiler_blowdown_recovery.md   # Blowdown geri kazanım
│   ├── boiler_condensate_return.md   # Kondensat geri dönüşü
│   ├── boiler_steam_trap.md          # Steam trap yönetimi
│   ├── boiler_insulation.md          # İzolasyon
│   ├── boiler_load_optimization.md   # Yük optimizasyonu
│   ├── boiler_combustion_tuning.md   # Yanma ayarı
│   └── boiler_feedwater_treatment.md # Besleme suyu arıtma
│
├── benchmarks/
│   └── boiler_benchmarks.md          # Tüm benchmark verileri
│
├── formulas/
│   └── boiler_exergy.md              # Exergy formülleri
│
└── methodology/
    └── boiler_audit.md               # Audit metodolojisi
```

**Toplam: 21 dosya**

---

## ⚠️ Önemli Notlar

1. **Format tutarlılığı:** Kompresör dosyalarındaki format ve yapıyı AYNEN koru
2. **Birim sistemi:** SI birimleri (kW, kJ, °C, bar, kg/s)
3. **Para birimi:** EUR (€) — Türkiye için TRY notu eklenebilir
4. **Exergy referans durumu:** T₀ = 25°C (298.15 K), P₀ = 1 atm
5. **Benchmark kategorileri:** poor, average, good, excellent (kompresörle aynı)
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

**Bu brief kazan knowledge base için tek kaynak noktasıdır.**
