# ExergyLab Brief: Enerji Yönetim Sistemi (ISO 50001 & Enerji Denetimi)

> **Claude Code için:** Bu brief kapsamında enerji yönetim sistemi, ISO 50001, enerji denetim standartları ve M&V protokolleri için derinlemesine knowledge base oluştur.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. Derin araştırma yap — ISO standartları, ASHRAE, IPMVP, Türkiye mevzuatı
2. Mevcut proje yapısını incele (`/home/ubuntu/exergy-lab/`)
3. Mevcut `knowledge/factory/energy_management.md` dosyasını incele ve genişlet
4. Mevcut `knowledge/factory/measurement_verification.md` dosyasını referans al
5. Türkiye enerji verimliliği mevzuatını detaylı araştır (YEGM, EVD, etüt zorunluluğu)
6. Eksik gördüğün bilgileri kendi insiyatifinle ekle

---

## 📋 BÖLÜM 1: Araştırma Konuları

### 1.1 ISO 50001 Enerji Yönetim Sistemi

- **Yapı ve gereksinimler** (Plan-Do-Check-Act)
- **Enerji politikası** oluşturma
- **Enerji planlaması:**
  - Enerji gözden geçirme (energy review)
  - Enerji temel çizgisi (energy baseline - EnB)
  - Enerji performans göstergeleri (EnPI)
  - Enerji hedefleri ve aksiyon planları
- **Uygulama ve operasyon:**
  - Yetkinlik, bilinç, iletişim
  - Operasyonel kontrol
  - Tasarım (yeni projeler)
  - Enerji hizmetleri satın alma
- **Performans değerlendirme:**
  - İzleme, ölçüm, analiz
  - İç denetim
  - Yönetim gözden geçirmesi
- **İyileştirme:**
  - Uygunsuzluk ve düzeltici faaliyet
  - Sürekli iyileştirme

### 1.2 Enerji Denetim Standartları

- **ISO 50002:** Enerji denetimleri - Gereksinimler
- **EN 16247 serisi:**
  - EN 16247-1: Genel gereksinimler
  - EN 16247-2: Binalar
  - EN 16247-3: Prosesler
  - EN 16247-4: Ulaşım
  - EN 16247-5: Denetçi yetkinliği
- **ASHRAE Seviyeleri:**
  - Level I: Walk-through audit (ön inceleme)
  - Level II: Energy survey (detaylı analiz)
  - Level III: Detailed analysis (yatırım seviyesi)

### 1.3 M&V Protokolleri (Ölçme ve Doğrulama)

- **IPMVP (International Performance Measurement & Verification Protocol):**
  - Option A: Retrofit isolation - Key parameter measurement
  - Option B: Retrofit isolation - All parameter measurement
  - Option C: Whole facility
  - Option D: Calibrated simulation
- **ASHRAE Guideline 14:** M&V prosedürleri
- **M&V planı hazırlama**
- **Baseline oluşturma**
- **Reporting period analizi**
- **Non-routine adjustments**
- **Statistical methods** (regresyon, CV-RMSE, NMBE)

### 1.4 Türkiye Enerji Verimliliği Mevzuatı

- **5627 sayılı Enerji Verimliliği Kanunu**
- **YEGM (Yenilenebilir Enerji Genel Müdürlüğü)** rolleri
- **EVD (Enerji Verimliliği Danışmanlık) şirketleri**
- **Enerji etüdü zorunluluğu:**
  - 1000 TEP üzeri endüstriyel tesisler
  - 500 TEP üzeri binalar
  - 4 yılda bir zorunlu etüt
- **Enerji yöneticisi atama zorunluluğu**
- **VAP (Verimlilik Artırıcı Projeler)** desteği
- **Gönüllü anlaşmalar**
- **ENVER teşvikleri**
- **EPC (Enerji Performans Sözleşmeleri)**
- **Beyaz sertifika sistemi** (mevcut/planlanan)

### 1.5 Enerji Performans Göstergeleri (EnPI)

- **Spesifik enerji tüketimi (SEC):** kWh/ton ürün
- **Enerji yoğunluğu:** kWh/€ ciro, kWh/m²
- **COP, EER** (soğutma)
- **Buhar verimi:** kg buhar/kg yakıt
- **Basınçlı hava spesifik güç:** kW/(m³/min)
- **CUSUM (Cumulative Sum) analizi**
- **Regresyon bazlı EnPI**
- **Sankey diyagramları**

### 1.6 Enerji Denetim Metodolojisi

- **Hazırlık:** Veri toplama, planlama
- **Saha incelemesi:** Ölçüm, gözlem
- **Analiz:** Enerji denge, verim hesaplama
- **Fırsatların belirlenmesi:** ECM (Energy Conservation Measures)
- **Fizibilite:** Teknik + ekonomik değerlendirme
- **Raporlama:** Standart rapor formatı
- **Uygulama izleme:** M&V

---

## 📋 BÖLÜM 2: Knowledge Base Genişletme

### 2.1 Yeni Dosyalar

```
knowledge/factory/energy_management/
├── INDEX.md
├── iso_50001_overview.md      # ISO 50001 genel yapı
├── iso_50001_implementation.md # Uygulama rehberi
├── energy_review.md           # Enerji gözden geçirme
├── baseline_enpi.md           # Temel çizgi ve EnPI
├── action_planning.md         # Hedef ve aksiyon planlama
├── monitoring_targeting.md    # İzleme ve hedefleme (M&T)
├── audit_methodology.md       # Enerji denetim metodolojisi
├── audit_levels.md            # ASHRAE Level I/II/III
├── iso_50002.md               # ISO 50002 gereksinimleri
├── en_16247.md                # EN 16247 serisi
├── mv_ipmvp.md                # IPMVP M&V protokolü
├── mv_planning.md             # M&V planı hazırlama
├── mv_statistics.md           # İstatistiksel yöntemler
├── turkey_legislation.md      # Türkiye mevzuatı (5627, YEGM)
├── turkey_incentives.md       # Türkiye teşvikleri (VAP, EPC)
├── enpi_guide.md              # EnPI seçim ve uygulama rehberi
├── cusum_analysis.md          # CUSUM ve regresyon analizi
├── reporting_templates.md     # Rapor şablonları
├── continuous_improvement.md  # Sürekli iyileştirme döngüsü
└── case_studies.md            # Türkiye ve dünya örnekleri
```

### 2.2 Dosya Kuralları

- YAML frontmatter
- Türkçe başlıklar
- Minimum 150 satır
- Cross-reference
- Pratik şablonlar ve formlar (mümkün olduğunca)
- Türkiye'ye özel detaylar (TEP hesaplama, YEGM formatları)

---

## 📋 BÖLÜM 3: Skill Güncelleme

### 3.1 Factory Skills

Mevcut factory skill'lerine enerji yönetimi tavsiyeleri ekle:

```
Her fabrika yorumunda:
1. Sektörel SEC benchmark karşılaştırması
2. ISO 50001 uyumluluk önerisi (eğer uygunsa)
3. Türkiye mevzuatı referansı (1000 TEP kontrolü)
4. M&V planı önerisi (büyük yatırımlar için)
```

---

## 📋 BÖLÜM 4: Araştırma Kaynakları

### Standartlar
- ISO 50001:2018
- ISO 50002:2014
- ISO 50004:2020 (uygulama rehberi)
- ISO 50006:2014 (EnPI ve EnB)
- ISO 50015:2014 (M&V)
- EN 16247 serisi
- IPMVP (EVO)
- ASHRAE Guideline 14

### Türkiye
- 5627 sayılı Enerji Verimliliği Kanunu
- Enerji Kaynaklarının ve Enerjinin Kullanımında Verimliliğin Artırılmasına Dair Yönetmelik
- YEGM web sitesi ve yayınları
- Türkiye Ulusal Enerji Verimliliği Eylem Planı (UEVEP)
- ETKB (Enerji ve Tabii Kaynaklar Bakanlığı) istatistikleri

### Akademik
- Morvay, Z.K. "Applied Industrial Energy and Environmental Management"
- Turner, W.C. "Energy Management Handbook"
- Thumann, A. "Handbook of Energy Audits"

---

## ✅ Tamamlama Kontrol Listesi

- [ ] knowledge/factory/energy_management/ dizini oluşturuldu (~21 dosya)
- [ ] Her dosya minimum 150 satır
- [ ] Türkiye mevzuatı detaylı araştırıldı
- [ ] M&V protokolleri dahil edildi
- [ ] Skills güncellendi
- [ ] Cross-reference'lar kuruldu
- [ ] Commit ve push yapıldı

**Hedef: ~21 dosya, her biri minimum 150 satır, pratik uygulamaya yönelik.**
