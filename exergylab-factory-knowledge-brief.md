# ExergyLab Factory Knowledge Base - Kapsamlı Araştırma Brief

> **Claude Code için:** Bu brief, fabrika seviyesi enerji/exergy analizi için kapsamlı bir knowledge base oluşturmayı amaçlar. Derin akademik araştırma yap, endüstri standartlarını incele, gerçek mühendislik uygulamalarını araştır ve profesyonel kalitede MD dosyaları oluştur.

---

## 🎯 Genel Amaç

Tek ekipman analizinden **fabrika sistemi analizi**ne geçiş yapıyoruz. Bu, sadece ekipmanları toplamak değil:
- Ekipmanlar arası enerji/exergy akışlarını anlamak
- Entegrasyon fırsatlarını tespit etmek (atık ısı kullanımı, pinch analizi)
- Sistem seviyesi optimizasyon stratejileri geliştirmek
- Yatırım önceliklendirme ve ekonomik analiz yapmak

**Hedef:** Bir enerji danışmanının fabrika audit'i yaparken kullanacağı tüm bilgi ve metodolojileri içeren kapsamlı bir knowledge base.

---

## 📚 BÖLÜM 1: Önce Mevcut Yapıyı Anla

### 1.1 Mevcut Ekipman Knowledge Base'lerini Tara

```
knowledge/
├── compressor/
│   ├── equipment/*.md
│   ├── solutions/*.md
│   ├── benchmarks.md
│   ├── formulas.md
│   └── audit.md
├── boiler/
│   └── ... (aynı yapı)
├── chiller/
│   └── ... (aynı yapı)
├── pump/
│   └── ... (aynı yapı)
└── factory/           ← BU KLASÖRÜ DOLDURACAĞIZ
    └── (boş)
```

Her ekipman klasöründeki `audit.md` ve `benchmarks.md` dosyalarını oku — fabrika analizinde bunlara referans verilecek.

### 1.2 Format Tutarlılığı

Factory dosyaları da aynı formatta olmalı:
- Türkçe başlıklar, teknik terimler İngilizce parantez içinde
- SI birimleri (kW, kJ, °C, bar, ton/yıl)
- Para birimi: EUR (€)
- Tablolar, formüller, örnekler
- Minimum 150-200 satır/dosya (kapsamlı içerik)
- Pratik örnekler ve vaka çalışmaları

---

## 🏭 BÖLÜM 2: Factory Knowledge Base Yapısı

### Önerilen Dosya Yapısı

```
knowledge/factory/
│
├── ─────────────────────────────────────────
│   METODOLOJİ VE TEMEL KAVRAMLAR
├── ─────────────────────────────────────────
├── methodology.md              # Fabrika enerji audit metodolojisi
├── energy_management.md        # ISO 50001 ve enerji yönetim sistemleri
├── exergy_fundamentals.md      # Fabrika seviyesi exergy analizi temelleri
├── system_boundaries.md        # Sistem sınırları ve ölçüm noktaları
│
├── ─────────────────────────────────────────
│   ANALİZ TEKNİKLERİ
├── ─────────────────────────────────────────
├── energy_flow_analysis.md     # Enerji akış analizi (Sankey)
├── exergy_flow_analysis.md     # Exergy akış analizi
├── pinch_analysis.md           # Pinch analizi ve ısı entegrasyonu
├── mass_balance.md             # Kütle dengesi ve materyal akışı
├── utility_analysis.md         # Utilities analizi (buhar, basınçlı hava, soğutma)
│
├── ─────────────────────────────────────────
│   ENTEGRASYON VE OPTİMİZASYON
├── ─────────────────────────────────────────
├── heat_integration.md         # Isı entegrasyonu ve atık ısı kullanımı
├── waste_heat_recovery.md      # Atık ısı geri kazanım teknolojileri
├── cogeneration.md             # Kojenerasyon ve trijenerasyon
├── process_integration.md      # Proses entegrasyonu
├── cross_equipment.md          # Ekipmanlar arası optimizasyon fırsatları
│
├── ─────────────────────────────────────────
│   EKONOMİK ANALİZ
├── ─────────────────────────────────────────
├── economic_analysis.md        # Yatırım analizi metodları (NPV, IRR, ROI)
├── prioritization.md           # Proje önceliklendirme matrisi
├── life_cycle_cost.md          # Yaşam döngüsü maliyet analizi (LCC)
├── energy_pricing.md           # Enerji fiyatlandırma ve tarifeler
│
├── ─────────────────────────────────────────
│   SEKTÖREL YAKLAŞIMLAR
├── ─────────────────────────────────────────
├── sector_textile.md           # Tekstil sektörü enerji profili
├── sector_food.md              # Gıda ve içecek sektörü
├── sector_chemical.md          # Kimya sektörü
├── sector_metal.md             # Metal ve makine sektörü
├── sector_cement.md            # Çimento ve yapı malzemeleri
├── sector_paper.md             # Kağıt ve selüloz sektörü
├── sector_automotive.md        # Otomotiv sektörü
│
├── ─────────────────────────────────────────
│   BENCHMARK VE GÖSTERGELER
├── ─────────────────────────────────────────
├── factory_benchmarks.md       # Fabrika seviyesi benchmark verileri
├── kpi_definitions.md          # Enerji KPI tanımları (SEC, EUI, exergy eff.)
├── performance_indicators.md   # Performans göstergeleri ve hedefler
│
├── ─────────────────────────────────────────
│   UYGULAMA VE DOĞRULAMA
├── ─────────────────────────────────────────
├── measurement_verification.md # Ölçüm ve Doğrulama (M&V) protokolleri
├── data_collection.md          # Veri toplama ve analiz
├── reporting.md                # Raporlama formatları ve şablonları
├── implementation.md           # Uygulama stratejileri ve engeller
│
└── ─────────────────────────────────────────
    VAKA ÇALIŞMALARI
├── ─────────────────────────────────────────
└── case_studies.md             # Gerçek fabrika vaka çalışmaları
```

---

## 📖 BÖLÜM 3: Her Dosyanın Detaylı İçerik Rehberi

### 3.1 methodology.md — Fabrika Enerji Audit Metodolojisi

**Araştırılacak konular:**
- ASHRAE Level I, II, III audit seviyeleri
- ISO 50002 Enerji audit standardı
- US DOE Industrial Assessment Center (IAC) metodolojisi
- Türkiye YEGM enerji etüdü yönetmelikleri
- Avrupa EN 16247 enerji audit standardı

**İçerik yapısı:**
```markdown
# Fabrika Enerji Audit Metodolojisi

## 1. Audit Seviyeleri
### 1.1 Ön İnceleme (Walk-through Audit)
- Amaç ve kapsam
- Tipik süre: 1-2 gün
- Çıktılar: Quick wins listesi

### 1.2 Standart Audit (ASHRAE Level II)
- Detaylı ölçümler
- Tipik süre: 1-2 hafta
- Çıktılar: Enerji tasarruf fırsatları, fizibilite

### 1.3 Yatırım Seviyesi Audit (ASHRAE Level III)
- Mühendislik analizi
- Simülasyon ve modelleme
- Çıktılar: Detaylı proje dosyaları

## 2. Audit Süreci
### 2.1 Ön Hazırlık
- Veri toplama (faturalar, proses akışı, ekipman listesi)
- Hedef belirleme
- Ekip oluşturma

### 2.2 Saha Çalışması
- Ölçüm noktaları
- Kullanılacak ekipmanlar
- Güvenlik prosedürleri

### 2.3 Analiz
- Enerji dengesi
- Exergy analizi
- Benchmark karşılaştırma
- Fırsat tespiti

### 2.4 Raporlama
- Rapor formatı
- Sunum teknikleri
- Yönetim özeti

## 3. Standart Referanslar
- ISO 50002:2014
- ASHRAE Procedures for Commercial Building Energy Audits
- EN 16247-1:2012
- US DOE Save Energy Now guides
```

---

### 3.2 energy_management.md — ISO 50001 ve Enerji Yönetim Sistemleri

**Araştırılacak konular:**
- ISO 50001:2018 yapısı ve gereksinimleri
- Plan-Do-Check-Act (PDCA) döngüsü
- Enerji temel çizgisi (EnB) ve enerji performans göstergeleri (EnPI)
- Enerji hedefleri ve eylem planları
- Sürekli iyileştirme
- Türkiye'de enerji yönetimi mevzuatı

**İçerik yapısı:**
```markdown
# Enerji Yönetim Sistemleri (ISO 50001)

## 1. ISO 50001 Yapısı
### 1.1 Bağlam ve Liderlik (Madde 4-5)
### 1.2 Planlama (Madde 6)
### 1.3 Destek ve Operasyon (Madde 7-8)
### 1.4 Performans Değerlendirme (Madde 9)
### 1.5 İyileştirme (Madde 10)

## 2. Enerji Performans Göstergeleri (EnPI)
### 2.1 EnPI Türleri
- Mutlak göstergeler (kWh/yıl)
- Spesifik göstergeler (kWh/ton ürün)
- Normalize göstergeler (hava koşulları, üretim)

### 2.2 EnPI Seçim Kriterleri
### 2.3 EnPI Hesaplama Örnekleri

## 3. Enerji Temel Çizgisi (EnB)
### 3.1 Baseline oluşturma
### 3.2 Normalizasyon faktörleri
### 3.3 Regresyon analizi

## 4. Önemli Enerji Kullanımları (SEU)
### 4.1 SEU belirleme kriterleri
### 4.2 Pareto analizi
### 4.3 Önceliklendirme

## 5. Türkiye Mevzuatı
### 5.1 Enerji Verimliliği Kanunu
### 5.2 Zorunlu enerji yöneticisi ataması
### 5.3 VAP (Verimlilik Artırıcı Proje) destekleri
```

---

### 3.3 exergy_fundamentals.md — Fabrika Seviyesi Exergy Analizi

**Araştırılacak konular:**
- Termodinamiğin II. Yasası ve endüstriyel sistemler
- Exergy dengesi fabrika seviyesinde
- Exergy yıkımı kaynakları (yanma, ısı transferi, karışım, sürtünme)
- Grassmann diyagramları
- Exergy verimlilik tanımları (rational, functional, task)
- Akademik makaleler: "Exergy analysis of industrial processes"

**Formüller:**
```
Fabrika Exergy Dengesi:
Ex_in = Ex_product + Ex_waste + Ex_destroyed

Ex_in = Ex_fuel + Ex_electricity + Ex_raw_materials
Ex_product = Ex_main_product + Ex_byproducts
Ex_waste = Ex_flue_gas + Ex_cooling_water + Ex_other_waste
Ex_destroyed = Σ I_k (tüm proseslerdeki irreversibility)

Fabrika Exergy Verimi:
η_ex,factory = Ex_product / Ex_in

Sektörel Karşılaştırma:
Çimento: η_ex ≈ 25-35%
Kimya: η_ex ≈ 30-50%
Gıda: η_ex ≈ 15-25%
Tekstil: η_ex ≈ 20-30%
```

---

### 3.4 pinch_analysis.md — Pinch Analizi ve Isı Entegrasyonu

**Araştırılacak konular:**
- Pinch teknolojisi temelleri (Linnhoff & Hindmarsh)
- Composite curves (bileşik eğriler)
- Grand composite curve
- Minimum enerji hedefleri (QH,min ve QC,min)
- Heat exchanger network (HEN) tasarımı
- ΔTmin seçimi ve trade-off'lar
- Pinch kuralları (don't cross the pinch)
- Retrofit vs grassroot tasarım
- Yazılım araçları (Aspen Energy Analyzer, HINT)

**İçerik yapısı:**
```markdown
# Pinch Analizi ve Isı Entegrasyonu

## 1. Temel Kavramlar
### 1.1 Isı Entegrasyonunun Önemi
- Tipik tasarruf potansiyeli: %20-40 yakıt
- Yatırım geri dönüşü: 1-3 yıl

### 1.2 Sıcak ve Soğuk Akımlar
- Tanımlar ve örnekler
- Stream data extraction

### 1.3 Composite Curves
- Hot composite curve (HCC)
- Cold composite curve (CCC)
- Enerji hedefleri

### 1.4 Pinch Noktası
- Pinch tanımı
- ΔTmin seçimi
- Pinch kuralları

## 2. Grand Composite Curve (GCC)
### 2.1 GCC oluşturma
### 2.2 Utility yerleştirme
### 2.3 Heat pocket'lar

## 3. Heat Exchanger Network (HEN) Tasarımı
### 3.1 Eşleştirme kuralları
### 3.2 Pinch üstü ve altı
### 3.3 Loop breaking ve path relaxation

## 4. Endüstriyel Uygulama Örnekleri
### 4.1 Petrokimya tesisi örneği
### 4.2 Gıda fabrikası örneği
### 4.3 Tekstil boyahane örneği

## 5. Pratik Hususlar
### 5.1 Veri toplama
### 5.2 Akım seçimi kriterleri
### 5.3 Güvenlik ve operasyonel kısıtlar
### 5.4 Retrofit zorlukları

## 6. Pinch Analizi Yazılımları
- Aspen Energy Analyzer
- HINT (Heat INTegration)
- SuperTarget
- Excel tabanlı araçlar
```

---

### 3.5 heat_integration.md — Isı Entegrasyonu ve Atık Isı Kullanımı

**Araştırılacak konular:**
- Atık ısı kaynakları endüstride (baca gazı, soğutma suyu, kondenser, basınçlı hava, proses)
- Atık ısı sıcaklık seviyeleri ve kullanım alanları
- Heat recovery teknolojileri (economizer, air preheater, heat pipe, recuperator, regenerator)
- Organic Rankine Cycle (ORC)
- Heat pumps endüstriyel uygulamalar
- Thermal energy storage
- District heating bağlantısı

**Kaynak-Kullanım Matrisi:**
```
Atık Isı Kaynağı          | Sıcaklık  | Potansiyel Kullanım
--------------------------|-----------|---------------------
Kazan baca gazı           | 150-250°C | Besleme suyu, hava ön ısıtma
Kompresör atık ısısı      | 70-90°C   | Bina ısıtma, sıcak su
Chiller kondenser         | 35-45°C   | Düşük sıcaklık ısıtma
Fırın baca gazı           | 300-600°C | Buhar üretimi, ORC
Kurutma egzozu            | 80-150°C  | Giriş havası ön ısıtma
Proses soğutma suyu       | 40-60°C   | Isı pompası kaynağı
```

---

### 3.6 waste_heat_recovery.md — Atık Isı Geri Kazanım Teknolojileri

**Araştırılacak konular:**
- Ekonomizer (su/buhar)
- Air preheater (regenerative, recuperative)
- Heat pipe heat exchangers
- Runaround coil systems
- Condensing economizers
- ORC (Organic Rankine Cycle) sistemleri
- Termoelektrik jeneratörler
- Absorption chiller (atık ısı ile soğutma)
- Heat pumps (yüksek sıcaklık endüstriyel)
- Thermal energy storage (molten salt, PCM)

**Her teknoloji için:**
- Çalışma prensibi
- Uygulama sıcaklık aralığı
- Verimlilik karakteristikleri
- Yatırım maliyeti (€/kW)
- Avantaj ve dezavantajlar
- Tipik ROI

---

### 3.7 cogeneration.md — Kojenerasyon ve Trijenerasyon

**Araştırılacak konular:**
- CHP (Combined Heat and Power) temelleri
- Prime mover türleri: Gaz türbini, buhar türbini, gaz motoru, fuel cell
- Topping vs bottoming cycle
- CCHP (Combined Cooling, Heating and Power) / Trijenerasyon
- Absorption chiller entegrasyonu
- Elektrik/ısı oranı optimizasyonu
- Şebeke bağlantısı ve self-consumption
- Türkiye'de kojenerasyon mevzuatı ve teşvikler
- Fizibilite kriterleri

**Benchmark:**
```
Kojenerasyon Verimlilikleri:
                    | Elektrik | Isı   | Toplam | Exergy
--------------------|----------|-------|--------|--------
Gaz Türbini CHP     | 30-40%   | 40-50%| 80-90% | 45-55%
Gaz Motoru CHP      | 35-45%   | 35-45%| 80-90% | 50-60%
Buhar Türbini CHP   | 15-35%   | 50-70%| 80-90% | 35-50%
Fuel Cell CHP       | 40-60%   | 30-40%| 80-90% | 55-70%
```

---

### 3.8 cross_equipment.md — Ekipmanlar Arası Optimizasyon

**Bu dosya kritik — ExergyLab'ın asıl değeri burada!**

**İçerik:**
```markdown
# Ekipmanlar Arası Optimizasyon Fırsatları

## 1. Kompresör → Kazan Entegrasyonu
### 1.1 Atık Isı Geri Kazanımı
- Kompresör yağ soğutucusu → Kazan besleme suyu ön ısıtma
- Tipik sıcaklık: 70-90°C (uygun)
- Hesaplama örneği:
  - 37 kW kompresör, %70 ısı geri kazanılabilir
  - Q_recovery = 37 × 0.70 = 26 kW termal
  - Besleme suyu 15°C → 45°C (30°C artış)
  - Yakıt tasarrufu: ~2-3%

### 1.2 Uygulama Dikkat Noktaları
- Mesafe ve boru kayıpları
- Soğutucu tip (yağ/hava/su)
- Kazan yük profili ile eşleşme

## 2. Kompresör → Bina Isıtma
### 2.1 HVAC Entegrasyonu
### 2.2 Sıcak Su Üretimi

## 3. Kazan → Absorption Chiller
### 3.1 Buhar ile Soğutma
- Tek etkili absorption chiller
- COP: 0.7-0.8
- Elektrik tasarrufu hesabı

### 3.2 Atık Isı ile Soğutma
- Baca gazı → hot water absorption chiller
- Blowdown ısısı kullanımı

## 4. Chiller → Isıtma Entegrasyonu
### 4.1 Kondenser Isısı Geri Kazanımı
- Desuperheater ile sıcak su
- Heat recovery chiller
- Eşzamanlı ısıtma-soğutma

## 5. Utility Sharing
### 5.1 Ortak Soğutma Kulesi
### 5.2 Ortak Basınçlı Hava Hattı
### 5.3 Buhar Dağıtım Optimizasyonu

## 6. Karar Matrisi
| Kaynak | Hedef | Uyumluluk | Tasarruf | Yatırım | ROI |
|--------|-------|-----------|----------|---------|-----|
| Kompresör → Kazan | Yüksek | €5K-15K | €3-8K/yıl | 1-3 yıl |
| Kazan → Abs.Chiller | Orta | €50K-150K | €15-40K/yıl | 3-5 yıl |
| ...

## 7. Entegrasyon Değerlendirme Kriterleri
### 7.1 Teknik Uygunluk
- Sıcaklık eşleşmesi
- Yük profili uyumu
- Mesafe ve erişim

### 7.2 Ekonomik Uygunluk
- Mevcut enerji maliyeti
- Yatırım büyüklüğü
- Geri ödeme süresi

### 7.3 Operasyonel Hususlar
- Bakım etkileri
- Esneklik kaybı
- Yedekleme ihtiyacı
```

---

### 3.9 economic_analysis.md — Yatırım Analizi Metodları

**Araştırılacak konular:**
- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Simple Payback Period (SPP)
- Discounted Payback Period (DPP)
- Return on Investment (ROI)
- Levelized Cost of Energy (LCOE)
- Total Cost of Ownership (TCO)
- Sensitivity analysis
- Monte Carlo simulation
- Risk assessment

**Formüller ve örnekler:**
```
NPV = Σ (Ct / (1+r)^t) - C0

IRR: NPV = 0 için r değeri

SPP = Initial Investment / Annual Savings

DPP: Σ (Ct / (1+r)^t) = C0 için minimum t

Örnek:
VSD yatırımı: €5,000
Yıllık tasarruf: €2,500
Ömür: 15 yıl
İskonto oranı: %10

SPP = 5000/2500 = 2 yıl
NPV = €14,000
IRR = %48
```

---

### 3.10 prioritization.md — Proje Önceliklendirme

**Araştırılacak konular:**
- Multi-criteria decision analysis (MCDA)
- Weighted scoring model
- Risk-return matrix
- Implementation difficulty matrix
- Quick wins vs strategic projects
- Resource allocation
- Portfolio optimization

**İçerik:**
```markdown
# Proje Önceliklendirme Matrisi

## 1. Önceliklendirme Kriterleri
### 1.1 Ekonomik Kriterler (Ağırlık: %40)
- ROI / Geri ödeme süresi
- Yatırım büyüklüğü
- Risk seviyesi

### 1.2 Teknik Kriterler (Ağırlık: %30)
- Uygulama kolaylığı
- Teknoloji olgunluğu
- Operasyonel etki

### 1.3 Stratejik Kriterler (Ağırlık: %30)
- Emisyon azaltımı
- Sürdürülebilirlik hedefleri
- Kurumsal öncelikler

## 2. Karar Matrisi
|             | ROI | Uygulama | Risk | Skor |
|-------------|-----|----------|------|------|
| VSD retrofit| 9   | 8        | 9    | 8.7  |
| Economizer  | 7   | 7        | 8    | 7.3  |
| CHP sistemi | 6   | 4        | 5    | 5.0  |

## 3. Quick Wins (< €10K, < 2 yıl ROI)
- Hava kaçağı tamiri
- Aydınlatma optimizasyonu
- Motor sürücü eşleştirme
- İzolasyon iyileştirme

## 4. Medium Projects (€10-100K, 2-5 yıl ROI)
- VSD retrofit
- Economizer
- Heat recovery
- Boiler optimization

## 5. Strategic Projects (> €100K, > 5 yıl ROI)
- CHP sistemi
- Bina enerji iyileştirme
- Proses değişikliği
- Yeniden boyutlandırma
```

---

### 3.11 factory_benchmarks.md — Fabrika Seviyesi Benchmark

**Araştırılacak konular:**
- Specific Energy Consumption (SEC) sektörel değerler
- Energy Use Intensity (EUI)
- Exergy efficiency by sector
- Türkiye endüstri ortalamaları
- EU BREF (Best Available Techniques Reference) documents
- US DOE Industrial Assessment Database
- Carbon intensity (kgCO2/ton ürün)

**İçerik:**
```markdown
# Fabrika Seviyesi Benchmark Verileri

## 1. Sektörel Spesifik Enerji Tüketimi (SEC)

### 1.1 Tekstil
| Proses | Birim | Düşük | Ortalama | Yüksek | En İyi Uygulama |
|--------|-------|-------|----------|--------|-----------------|
| İplik | kWh/kg | 2.5 | 4.0 | 6.0 | 2.0 |
| Dokuma | kWh/kg | 0.8 | 1.5 | 2.5 | 0.6 |
| Boyama | kWh/kg | 8 | 15 | 25 | 6 |
| Terbiye | kWh/kg | 5 | 10 | 18 | 4 |

### 1.2 Gıda ve İçecek
| Proses | Birim | Düşük | Ortalama | Yüksek | En İyi |
|--------|-------|-------|----------|--------|--------|
| Süt işleme | kWh/L | 0.08 | 0.15 | 0.25 | 0.06 |
| Bira | kWh/hL | 25 | 45 | 80 | 20 |
| Et işleme | kWh/kg | 0.5 | 1.0 | 2.0 | 0.4 |

### 1.3 Çimento
| | Düşük | Ortalama | Yüksek | En İyi |
|--|-------|----------|--------|--------|
| Elektrik (kWh/ton) | 90 | 110 | 140 | 80 |
| Termal (MJ/ton) | 2900 | 3500 | 4200 | 2700 |

### 1.4 Kimya
(Ürüne göre çok değişken - örnek prosesler)

### 1.5 Metal
| Proses | kWh/ton |
|--------|---------|
| Çelik EAF | 400-700 |
| Alüminyum | 13000-16000 |

## 2. Fabrika Exergy Verimliliği
| Sektör | Tipik Aralık | En İyi Uygulama |
|--------|--------------|-----------------|
| Çimento | 25-35% | 40% |
| Kimya | 30-50% | 60% |
| Gıda | 15-25% | 35% |
| Tekstil | 20-30% | 40% |
| Metal | 25-40% | 50% |
| Kağıt | 30-45% | 55% |

## 3. Kaynak
- EU BREF documents
- US DOE IAC database
- IEA Industrial Energy Efficiency
- Türkiye YEGM verileri
```

---

### 3.12 Sektörel Dosyalar (sector_*.md)

Her sektör için ayrı dosya oluştur. Her biri:

**Yapı:**
```markdown
# [Sektör] Enerji Profili ve Optimizasyon

## 1. Sektör Genel Bakış
- Türkiye'deki ölçek ve önem
- Enerji yoğunluğu
- Tipik fabrika yapısı

## 2. Enerji Tüketim Profili
### 2.1 Enerji Dağılımı
- Elektrik: X%
- Doğalgaz: Y%
- Buhar: Z%

### 2.2 Ana Enerji Tüketicileri
- Proses 1: X%
- Proses 2: Y%
- Utilities: Z%

## 3. Tipik Ekipman Envanteri
| Ekipman | Tipik Kapasite | Enerji Payı |
|---------|----------------|-------------|
| Kazan | X ton/h | Y% |
| Kompresör | X kW | Y% |
| ... | | |

## 4. Exergy Analizi
### 4.1 Exergy Akış Diyagramı
### 4.2 Ana Kayıp Noktaları
### 4.3 Tipik Exergy Verimi

## 5. Optimizasyon Fırsatları
### 5.1 Yüksek Potansiyel (Quick Wins)
### 5.2 Orta Vadeli Projeler
### 5.3 Stratejik Projeler

## 6. Sektörel En İyi Uygulamalar
- Best practice 1
- Best practice 2

## 7. Vaka Çalışması
Gerçek fabrika örneği (anonim)
```

---

### 3.13 measurement_verification.md — Ölçüm ve Doğrulama

**Araştırılacak konular:**
- IPMVP (International Performance Measurement and Verification Protocol)
- ASHRAE Guideline 14
- M&V Options (A, B, C, D)
- Baseline adjustment
- Non-routine adjustments
- Uncertainty analysis
- Savings calculation methodologies

---

### 3.14 case_studies.md — Vaka Çalışmaları

**Gerçek dünya örnekleri araştır:**
- US DOE Industrial Assessment Center case studies
- Carbon Trust case studies
- IEA industrial efficiency examples
- EU ESCO project examples
- Türkiye VAP proje örnekleri

Her vaka için:
- Fabrika profili (sektör, ölçek)
- Başlangıç durumu
- Yapılan iyileştirmeler
- Sonuçlar (tasarruf, yatırım, ROI)
- Lessons learned

---

## 🔍 BÖLÜM 4: Araştırma Kaynakları

### 4.1 Akademik Kaynaklar
```
Google Scholar araması:
- "exergy analysis industrial plant"
- "factory energy efficiency"
- "pinch analysis industrial application"
- "heat integration process industry"
- "industrial waste heat recovery"
- "energy audit methodology industry"

Önemli dergiler:
- Energy (Elsevier)
- Applied Energy
- Energy Conversion and Management
- Journal of Cleaner Production
- International Journal of Exergy

Önemli yazarlar:
- Linnhoff (Pinch analysis)
- Bejan (Exergy analysis)
- Rosen (Industrial exergy)
- Szargut (Exergy fundamentals)
```

### 4.2 Endüstri Kaynakları
```
US Department of Energy:
- Industrial Assessment Center Database (iac.university)
- Better Plants Program
- Save Energy Now guides
- Steam, Compressed Air, Motor, Pump Sourcebooks

European Commission:
- BREF documents (Best Available Techniques)
- EU Energy Efficiency Directive

IEA (International Energy Agency):
- Industrial Energy Efficiency
- Energy Technology Perspectives

ASHRAE:
- Energy Audit guides
- Measurement and Verification

Carbon Trust:
- Industry sector guides
- Case studies
```

### 4.3 Türkiye Kaynakları
```
YEGM (Yenilenebilir Enerji Genel Müdürlüğü):
- Enerji verimliliği raporları
- Sektörel etüdler
- VAP proje örnekleri

TMMOB / MMO:
- Enerji verimliliği el kitapları
- Teknik yayınlar

Sanayi ve Teknoloji Bakanlığı:
- Verimlilik raporları
- Sektörel analizler
```

---

## ✅ BÖLÜM 5: Tamamlama Kontrol Listesi

### Dosya Listesi (En az 25 dosya)

**Metodoloji ve Temel (4 dosya):**
- [ ] methodology.md
- [ ] energy_management.md
- [ ] exergy_fundamentals.md
- [ ] system_boundaries.md

**Analiz Teknikleri (5 dosya):**
- [ ] energy_flow_analysis.md
- [ ] exergy_flow_analysis.md
- [ ] pinch_analysis.md
- [ ] mass_balance.md
- [ ] utility_analysis.md

**Entegrasyon (5 dosya):**
- [ ] heat_integration.md
- [ ] waste_heat_recovery.md
- [ ] cogeneration.md
- [ ] process_integration.md
- [ ] cross_equipment.md

**Ekonomik (4 dosya):**
- [ ] economic_analysis.md
- [ ] prioritization.md
- [ ] life_cycle_cost.md
- [ ] energy_pricing.md

**Sektörel (7 dosya):**
- [ ] sector_textile.md
- [ ] sector_food.md
- [ ] sector_chemical.md
- [ ] sector_metal.md
- [ ] sector_cement.md
- [ ] sector_paper.md
- [ ] sector_automotive.md

**Benchmark (3 dosya):**
- [ ] factory_benchmarks.md
- [ ] kpi_definitions.md
- [ ] performance_indicators.md

**Uygulama (4 dosya):**
- [ ] measurement_verification.md
- [ ] data_collection.md
- [ ] reporting.md
- [ ] implementation.md

**Vaka (1 dosya):**
- [ ] case_studies.md

### Kalite Kontrolleri
- [ ] Her dosya minimum 150 satır
- [ ] Tablolar ve formüller var
- [ ] Akademik referanslar var
- [ ] Pratik örnekler var
- [ ] Türkçe başlıklar, teknik terimler İngilizce
- [ ] SI birimleri kullanılmış
- [ ] Mevcut ekipman dosyalarıyla tutarlı format

---

## 🚀 BÖLÜM 6: Uygulama Talimatları

### Claude Code için Adımlar:

1. **ÖNCE** mevcut knowledge base'deki formatı anla:
   - `/knowledge/compressor/audit.md` oku
   - `/knowledge/boiler/benchmarks.md` oku
   - Format, stil, derinlik öğren

2. **Web araştırması yap:**
   - Akademik makaleler (Google Scholar)
   - Endüstri kaynakları (DOE, IEA, EU BREF)
   - Standartlar (ISO, ASHRAE, EN)
   - Her konuda derinlemesine araştır

3. **Dosyaları oluştur:**
   - `/knowledge/factory/` altında
   - Yukarıdaki yapıya uygun
   - Kapsamlı ve detaylı

4. **Kalite kontrol:**
   - Her dosya en az 150 satır
   - Formüller matematiksel doğru
   - Tablolar okunabilir
   - Referanslar belirtilmiş

5. **Sonunda özet ver:**
   - Kaç dosya oluşturuldu
   - Toplam satır sayısı
   - Kapsanan konular

---

**Bu brief, fabrika knowledge base için tek kaynak noktasıdır. Kapsamlı araştırma ve yüksek kaliteli içerik beklenmektedir.**
