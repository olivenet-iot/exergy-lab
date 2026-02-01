---
title: "Performans Göstergeleri ve Hedefler (Performance Indicators and Targets)"
category: factory
equipment_type: factory
keywords: [performans, gösterge, KPI]
related_files: [factory/kpi_definitions.md, factory/factory_benchmarks.md, factory/reporting.md]
use_when: ["Performans göstergeleri değerlendirilirken", "İzleme metrikleri belirlenirken"]
priority: medium
last_updated: 2026-01-31
---
# Performans Göstergeleri ve Hedefler (Performance Indicators and Targets)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji performansının etkin yönetimi, doğru göstergelerin seçimi, gerçekçi hedeflerin belirlenmesi ve sürekli izleme ile mümkündür. Bu dosya; hedef belirleme metodolojisi, trend analizi teknikleri, performans takip yöntemleri, istatistiksel proses kontrolü (SPC), boşluk analizi (gap analysis) ve KPI dashboard tasarım ilkelerini kapsar. ISO 50001 enerji yönetim sistemi çerçevesinde EnPI (Energy Performance Indicator) yönetimi için rehber niteliğindedir.

## 1. Hedef Türleri ve Tanımları (Target Types)

### 1.1 Mutlak Azaltma Hedefleri (Absolute Reduction Targets)

```
Mutlak hedef = Referans yılı tüketiminden % azaltma

Tanım:
  E_hedef = E_baz × (1 - r_hedef)

Burada:
  E_hedef = Hedef yılı enerji tüketimi [kWh/yıl veya GJ/yıl]
  E_baz = Baz yılı (referans) enerji tüketimi [kWh/yıl veya GJ/yıl]
  r_hedef = Hedef azaltma oranı [oran, 0-1]

Avantajlar:
  - Basit ve anlaşılır
  - Toplam emisyon azaltımıyla doğrudan ilişkili
  - Regülasyon ve raporlamada yaygın (AB ETS, Paris Anlaşması)

Dezavantajlar:
  - Üretim artışında hedef tutmak zorlaşır
  - Ekonomik dalgalanmalardan etkilenir
  - Kapasite artışı hedefi anlamsızlaştırabilir

Örnek:
  Baz yılı (2023): 12,000,000 kWh/yıl
  Hedef: %15 azaltma (5 yılda)
  E_hedef = 12,000,000 × (1 - 0.15) = 10,200,000 kWh/yıl
  Yıllık azaltma: ~360,000 kWh/yıl (%3/yıl)
```

### 1.2 Spesifik Tüketim İyileştirme Hedefleri (Specific Consumption Improvement)

```
Spesifik hedef = SEC'de % iyileştirme

Tanım:
  SEC_hedef = SEC_baz × (1 - r_sec)

Burada:
  SEC_hedef = Hedef spesifik enerji tüketimi [kWh/ton]
  SEC_baz = Baz yılı SEC [kWh/ton]
  r_sec = Hedef iyileştirme oranı [oran, 0-1]

Avantajlar:
  - Üretim miktarından bağımsız
  - Verimlilik artışını doğrudan ölçer
  - Sektörel karşılaştırma yapmaya uygun

Dezavantajlar:
  - Ürün karması değişikliğinden etkilenir
  - Kapasite kullanım oranına duyarlı
  - Sınır etkisi (diminishing returns) — düşük SEC'te iyileştirme zorlaşır

Örnek:
  Baz yılı SEC: 3,500 kWh/ton
  Sektör en iyi uygulama: 2,800 kWh/ton
  Hedef: %10 iyileştirme (3 yılda)
  SEC_hedef = 3,500 × (1 - 0.10) = 3,150 kWh/ton
  Kapatılacak boşluk: (3,500 - 3,150) / (3,500 - 2,800) = %50
```

### 1.3 Exergy Verimlilik İyileştirme Hedefleri

```
Exergy hedefi = η_ex artışı

Tanım:
  η_ex_hedef = η_ex_mevcut + Δη_ex

Burada:
  η_ex_hedef = Hedef exergy verimliliği [%]
  η_ex_mevcut = Mevcut exergy verimliliği [%]
  Δη_ex = Hedef exergy verimlilik artışı [puan]

Avantajlar:
  - Termodinamik olarak en anlamlı gösterge
  - Gerçek iyileştirme potansiyelini gösterir
  - Farklı enerji türlerini adil karşılaştırır

Dezavantajlar:
  - Hesaplaması karmaşık
  - Endüstride yaygın tanınmıyor
  - Referans ortam koşullarına bağımlı

Örnek:
  Mevcut η_ex = 22%
  Sektör en iyi uygulama η_ex = 35%
  Hedef: 5 puan artış (5 yılda)
  η_ex_hedef = 22 + 5 = 27%
  Uygulanabilir potansiyelin kapatma oranı: 5 / (35 - 22) = %38
```

## 2. Sektörel Hedef Belirleme (5 Yıllık İyileştirme Hedefleri)

### 2.1 Sektör Bazında Hedef Tablosu

| Sektör | Mevcut Ort. SEC | 5 Yıl Hedef SEC | İyileştirme [%] | Yıllık Hedef [%] | Exergy Hedef [puan] |
|---|---|---|---|---|---|
| Tekstil | 20 kWh/kg | 16 kWh/kg | %20 | %4.4 | +4 |
| Gıda (süt) | 0.15 kWh/L | 0.12 kWh/L | %20 | %4.4 | +3 |
| Çimento | 3,400 MJ/ton | 3,000 MJ/ton | %12 | %2.5 | +5 |
| Kimya (amonyak) | 36 GJ/ton | 32 GJ/ton | %11 | %2.3 | +4 |
| Metal (EAF) | 550 kWh/ton | 470 kWh/ton | %15 | %3.2 | +5 |
| Kağıt | 650 kWh/ton el. | 530 kWh/ton | %18 | %3.9 | +4 |
| Otomotiv | 3,800 kWh/araç | 2,800 kWh/araç | %26 | %5.9 | +6 |

### 2.2 Hedef Belirleme Yöntemi

```
Adım 1: Mevcut durum tespiti
  - Son 12-36 ay enerji tüketim verileri
  - Kapasite kullanım oranı ve üretim verileri
  - Mevcut SEC ve exergy verimliliği hesaplama

Adım 2: Benchmark karşılaştırma
  - Sektörel en iyi uygulama SEC değerleri (factory_benchmarks.md)
  - Boşluk analizi: Gap = SEC_mevcut - SEC_benchmark
  - Kapatılabilir boşluk: Teknik ve ekonomik kısıtlarla sınırlı

Adım 3: İyileştirme potansiyeli
  - Quick wins (düşük/sıfır yatırım): Boşluğun %20-30'u
  - Orta vadeli (yatırım gerektiren): Boşluğun %30-50'si
  - Stratejik (büyük yatırım): Boşluğun %20-40'ı
  - Toplam ulaşılabilir: Boşluğun %50-70'i (5 yılda)

Adım 4: Hedef oluşturma
  - Gerçekçi hedef = Mevcut SEC - (Boşluk × Ulaşılabilirlik × Zaman)
  - SMART kriterleri: Specific, Measurable, Achievable, Relevant, Time-bound
  - Yıllık ara hedefler (milestones) belirleme
```

## 3. Trend Analizi Teknikleri (Trend Analysis)

### 3.1 CUSUM Analizi (Cumulative Sum)

```
CUSUM — Kümülatif toplam analizi:

CUSUM_t = Σᵢ₌₁ᵗ (Eᵢ - Ê_i)

Burada:
  CUSUM_t = t dönemine kadar kümülatif sapma [kWh]
  Eᵢ = i döneminde gerçekleşen enerji tüketimi [kWh]
  Ê_i = i döneminde beklenen (referans) enerji tüketimi [kWh]
  Ê_i genellikle regresyon modeli ile hesaplanır

Yorumlama:
  - CUSUM artan eğilim: Tüketim beklenenin üzerinde (performans kötüleşiyor)
  - CUSUM azalan eğilim: Tüketim beklenenin altında (performans iyileşiyor)
  - CUSUM düz eğilim: Performans stabil
  - Eğim değişimi: Operasyonel veya yapısal değişiklik işareti

Örnek:
  Baz dönem regresyonu: Ê = 120,000 + 3.5 × P (kWh/ay)
  P = Üretim miktarı [ton/ay]

  Ay 1: E=145,000, P=8,000 → Ê=148,000 → Fark=-3,000 → CUSUM=-3,000
  Ay 2: E=142,000, P=7,500 → Ê=146,250 → Fark=-4,250 → CUSUM=-7,250
  Ay 3: E=160,000, P=8,200 → Ê=148,700 → Fark=+11,300 → CUSUM=+4,050
  → Ay 3'te anormal tüketim artışı → inceleme gerekli
```

### 3.2 Regresyon Analizi (Enerji — Üretim İlişkisi)

```
Basit doğrusal regresyon:
  E = β₀ + β₁ × P + ε

Burada:
  E = Enerji tüketimi [kWh/dönem]
  P = Üretim miktarı [ton/dönem veya adet/dönem]
  β₀ = Sabit tüketim (base load) [kWh/dönem]
  β₁ = Marjinal enerji tüketimi [kWh/ton veya kWh/adet]
  ε = Hata terimi

Çoklu regresyon (iklim etkisi dahil):
  E = β₀ + β₁×P + β₂×HDD + β₃×CDD + ε

Burada:
  HDD = Isıtma derece-gün (Heating Degree Days)
  CDD = Soğutma derece-gün (Cooling Degree Days)

Model kalite kriterleri:
  R² > 0.75: Kabul edilebilir
  R² > 0.85: İyi
  R² > 0.95: Çok iyi
  CV-RMSE ≤ %25 (aylık veri): ASHRAE Guideline 14 uyumlu
  NMBE ≤ ±%10 (aylık veri): ASHRAE Guideline 14 uyumlu

Örnek:
  36 aylık veri ile regresyon:
  E = 85,000 + 4.2 × P [kWh/ay]
  R² = 0.91, CV-RMSE = %12, NMBE = +%2.1

  Yorumlama:
  - Sabit yük: 85,000 kWh/ay (aydınlatma, HVAC, standby)
  - Marjinal: Her ton üretim 4.2 kWh ek enerji
  - %91 varyans açıklanıyor → İyi model
```

## 4. İstatistiksel Proses Kontrolü — SPC (Statistical Process Control)

### 4.1 Enerji Kontrol Grafikleri (Control Charts)

```
X-bar kontrol grafiği enerji performansı için:

UCL = X̄ + k × σ  (Üst kontrol limiti)
CL  = X̄           (Merkez çizgisi)
LCL = X̄ - k × σ  (Alt kontrol limiti)

Burada:
  X̄ = Ortalama SEC veya enerji tüketimi [kWh/ton veya kWh/dönem]
  σ = Standart sapma
  k = Kontrol limit katsayısı (genellikle 3 — 3-sigma kuralı)
  UCL = Upper Control Limit
  LCL = Lower Control Limit

Uyarı sınırları (warning limits): k = 2 (2-sigma)

Alarm kuralları (Western Electric kuralları):
  1. Tek bir nokta kontrol limiti dışında → Anormal
  2. Ardışık 7 nokta merkez çizgisinin aynı tarafında → Trend
  3. Ardışık 7 nokta artan veya azalan → Drift
  4. 3 ardışık noktadan 2'si uyarı sınırında → Dikkat

Örnek:
  24 aylık SEC verisi:
  X̄ = 3,200 kWh/ton, σ = 180 kWh/ton
  UCL = 3,200 + 3 × 180 = 3,740 kWh/ton
  LCL = 3,200 - 3 × 180 = 2,660 kWh/ton
  Uyarı üst: 3,200 + 2 × 180 = 3,560 kWh/ton
  Uyarı alt: 3,200 - 2 × 180 = 2,840 kWh/ton
```

### 4.2 İstisna Raporlama (Exception Reporting)

| Durum | Tetikleyici | Aksiyon | Sorumlu | Süre |
|---|---|---|---|---|
| Yeşil | SEC < LCL veya hedefin altında | Mevcut uygulamayı kaydet | Enerji müdürü | — |
| Sarı (Uyarı) | Uyarı sınırları aşılıyor | Sebep araştırma başlat | Operasyon mühendisi | 48 saat |
| Turuncu (Alarm) | UCL aşılıyor (tek olay) | Detaylı analiz ve düzeltici aksiyon | Enerji ekibi | 24 saat |
| Kırmızı (Kritik) | UCL ardışık 3+ dönem | Yönetim bilgilendirme, acil müdahale | Fabrika müdürü | Derhal |

## 5. Boşluk Analizi (Gap Analysis)

### 5.1 Boşluk Analizi Çalışılmış Örnek

```
Tekstil fabrikası boşluk analizi:

Mevcut durum:
  Toplam SEC = 22 kWh/kg kumaş
  Exergy verimi (η_ex) = %9

Benchmark değerler (factory_benchmarks.md'den):
  Sektör ortalaması SEC = 18 kWh/kg
  En iyi uygulama SEC = 10 kWh/kg
  En iyi uygulama η_ex = %20

Boşluk hesaplama:
  Ortalamaya boşluk = 22 - 18 = 4 kWh/kg (%18 iyileştirme)
  Best practice'e boşluk = 22 - 10 = 12 kWh/kg (%55 iyileştirme)
  Exergy boşluğu = 20 - 9 = 11 puan

Boşluk dağılımı (audit bulgularına göre):
  1. Boyama prosesi (flotte oranı yüksek): 3.5 kWh/kg → %29
  2. Kurutma (ram/stenter verimsiz): 2.8 kWh/kg → %23
  3. Buhar dağıtım kayıpları: 2.0 kWh/kg → %17
  4. Basınçlı hava kaçakları: 1.2 kWh/kg → %10
  5. Aydınlatma ve HVAC: 0.8 kWh/kg → %7
  6. Motor/tahrik verimsizlikleri: 0.7 kWh/kg → %6
  7. Diğer: 1.0 kWh/kg → %8
  Toplam boşluk: 12.0 kWh/kg → %100

Ulaşılabilir hedef (5 yılda):
  Quick wins (0-6 ay): 2.5 kWh/kg kapatılabilir
  Orta vade (6-24 ay): 4.0 kWh/kg kapatılabilir
  Uzun vade (2-5 yıl): 2.5 kWh/kg kapatılabilir
  Toplam kapatılabilir: 9.0 kWh/kg → Hedef SEC = 13 kWh/kg
```

## 6. Öncü ve Gecikmeli Göstergeler (Leading vs Lagging Indicators)

### 6.1 Gösterge Sınıflandırması

| Gösterge Tipi | Tanım | Örnekler | Avantajı | Dezavantajı |
|---|---|---|---|---|
| Öncü (Leading) | Gelecek performansı öngören | Bakım uyum oranı, eğitim saati, audit sayısı | Proaktif müdahale | Sonuçla ilişki dolaylı |
| Gecikmeli (Lagging) | Gerçekleşmiş performans | SEC, toplam tüketim, maliyet, emisyon | Kesin ve ölçülebilir | Geçmişe dönük, reaktif |
| Karma | İkisinin kombinasyonu | CUSUM, trend slope, SPC alarm oranı | Erken uyarı + doğrulama | Karmaşık hesaplama |

### 6.2 Öncü Gösterge Örnekleri

| Öncü Gösterge | Hedef | Ölçüm Sıklığı | İlişkili Gecikmeli Gösterge |
|---|---|---|---|
| Enerji eğitimi katılım oranı | >%90 | Aylık | SEC iyileştirme |
| Planlı bakım uyum oranı | >%95 | Haftalık | Ekipman verimliliği |
| Enerji aksiyon tamamlama oranı | >%80 | Aylık | Toplam tasarruf |
| Kaçak onarım süresi | <48 saat | Olay bazlı | Basınçlı hava SEC |
| Ölçüm sistemi kullanılabilirliği | >%98 | Sürekli | Veri kalitesi, raporlama |
| SPC alarm sayısı | Azalan trend | Aylık | SEC varyansı |
| Enerji toplantısı katılımı | >%85 | Aylık | Enerji kültürü |

## 7. Enerji Yoğunluğu ve Mutlak Tüketim Tartışması

### 7.1 Karşılaştırmalı Değerlendirme

```
Senaryo: Fabrika büyümesi ve enerji hedefleri

Baz yılı (2023):
  Üretim: 10,000 ton/yıl
  Enerji: 50,000,000 kWh/yıl
  SEC: 5,000 kWh/ton

Hedef yılı (2028) — Senaryo A (Mutlak hedef: -%10):
  Üretim: 15,000 ton/yıl (büyüme)
  Enerji hedefi: 45,000,000 kWh/yıl
  Gerekli SEC: 3,000 kWh/ton (-%40 iyileştirme → gerçekçi değil)

Hedef yılı (2028) — Senaryo B (Spesifik hedef: -%15):
  Üretim: 15,000 ton/yıl
  SEC hedefi: 4,250 kWh/ton
  Enerji: 63,750,000 kWh/yıl (+%28 artış → emisyon artışı)

Çözüm: Hibrit hedef
  Spesifik hedef: SEC -%15 → 4,250 kWh/ton
  Mutlak tavan: Toplam enerji ≤ 55,000,000 kWh/yıl
  Bu durumda üretim sınırlaması: 55,000,000 / 4,250 = 12,941 ton
  → Daha fazla üretim için daha agresif verimlilik gerekir
```

## 8. KPI Dashboard Tasarım İlkeleri

### 8.1 Dashboard Katmanları

| Katman | Kullanıcı | KPI Sayısı | Güncelleme | İçerik |
|---|---|---|---|---|
| Üst yönetim | Genel müdür, CFO | 4-6 | Aylık | Toplam maliyet, SEC trend, hedef sapma, ROI |
| Orta yönetim | Fabrika/enerji müdürü | 8-12 | Haftalık | Sistem bazlı SEC, CUSUM, alarm, aksiyon durum |
| Operasyonel | Vardiya mühendisi | 12-20 | Anlık/saatlik | Ekipman verim, akış, sıcaklık, basınç, alarm |
| Analitik | Enerji uzmanı | Sınırsız | İstendiğinde | Ham veri, regresyon, benchmark, what-if |

### 8.2 Dashboard Tasarım Kuralları

```
Etkili enerji dashboard tasarımı:

1. Hiyerarşi: Fabrika → Sistem → Ekipman (drill-down)
2. Görsellik: Renk kodlaması (Yeşil-Sarı-Turuncu-Kırmızı)
3. Bağlam: Her KPI yanında hedef ve benchmark göster
4. Trend: Son 12 ay + hedef çizgisi
5. Alarm: Sadece aksiyon gerektiren durumları vurgula
6. Basitlik: Ekran başına max 6-8 widget
7. Güncelleme: Veri tazeliği açıkça belirtilmeli
8. Erişim: Mobil uyumlu, rol bazlı görünüm

Dashboard widget örnekleri:
  - Gauge (gösterge): Anlık SEC vs hedef
  - Line chart: SEC trend (12 ay)
  - Bar chart: Sistem bazlı enerji dağılımı
  - Heatmap: Saatlik tüketim profili
  - Pareto: En büyük kayıp kaynakları
  - Waterfall: Baz yıldan bugüne tasarruf akışı
  - Scatter: Enerji-üretim korelasyonu
  - Table: SPC alarm listesi
```

## 9. Performans İzleme Şablonu (Performance Tracking Template)

### 9.1 Aylık İzleme Tablosu

| Ay | Üretim [ton] | Elektrik [kWh] | Gaz [Nm³] | SEC [kWh/ton] | Hedef SEC | Sapma [%] | CUSUM | Durum |
|---|---|---|---|---|---|---|---|---|
| Ocak | 800 | 3,200,000 | 280,000 | 7,613 | 7,200 | +%5.7 | +330,400 | Uyarı |
| Şubat | 750 | 3,050,000 | 265,000 | 7,716 | 7,200 | +%7.2 | +717,150 | Alarm |
| Mart | 900 | 3,500,000 | 310,000 | 7,453 | 7,200 | +%3.5 | +944,850 | Uyarı |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### 9.2 Yıllık Hedef Takip

| KPI | Baz Yılı | Yıl 1 | Yıl 2 | Yıl 3 | Yıl 4 | Yıl 5 | Birim |
|---|---|---|---|---|---|---|---|
| SEC (toplam) | 3,500 | 3,350 | 3,200 | 3,060 | 2,930 | 2,800 | kWh/ton |
| Exergy verimi | 22.0 | 23.0 | 24.2 | 25.4 | 26.6 | 27.0 | % |
| Enerji maliyeti | 1,200,000 | 1,150,000 | 1,100,000 | 1,050,000 | 1,000,000 | 960,000 | €/yıl |
| CO₂ emisyonu | 5,000 | 4,750 | 4,500 | 4,250 | 4,000 | 3,800 | ton/yıl |
| Tasarruf (kümülatif) | 0 | 50,000 | 120,000 | 210,000 | 320,000 | 450,000 | € |

## İlgili Dosyalar

- [KPI Tanımları](kpi_definitions.md) — Enerji performans göstergeleri detay tanımları
- [Fabrika Benchmarkları](factory_benchmarks.md) — Sektörel karşılaştırma verileri
- [Veri Toplama](data_collection.md) — Ölçüm ve veri yönetimi
- [Ölçüm ve Doğrulama](measurement_verification.md) — IPMVP protokolü ve tasarruf doğrulama
- [Enerji Yönetimi](energy_management.md) — ISO 50001 enerji yönetim sistemi
- [Metodoloji](methodology.md) — Audit metodolojisi
- [Raporlama](reporting.md) — Audit rapor formatları
- [Kazan Benchmarkları](../boiler/benchmarks.md) — Kazan verim aralıkları
- [Kompresör Benchmarkları](../compressor/benchmarks.md) — Kompresör performans verileri
- [Chiller Benchmarkları](../chiller/benchmarks.md) — Chiller COP karşılaştırma

## Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50006:2014, "Energy management systems — Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI)"
- ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- Montgomery, D.C., "Introduction to Statistical Quality Control," 8th Edition, Wiley, 2019
- Worell, E. & Galitsky, C., "Energy Efficiency Improvement and Cost Saving Opportunities for Petroleum Refineries," LBNL, 2005
- DOE, "Superior Energy Performance — Measurement and Verification Protocol," US Department of Energy, 2012
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- Capehart, B.L., Turner, W.C. & Kennedy, W.J., "Guide to Energy Management," 8th Edition, Fairmont Press, 2016
