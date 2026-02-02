---
title: "Enerji Performans Göstergeleri Rehberi (Energy Performance Indicators Guide — ISO 50006)"
category: factory
equipment_type: factory
keywords: [EnPI, enerji performans göstergesi, ISO 50006, SEC, exergy EnPI, spesifik enerji tüketimi, normalleştirme, sektörel EnPI]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/baseline_enpi.md, factory/energy_management/cusum_analysis.md, factory/energy_management/monitoring_targeting.md, factory/kpi_definitions.md, factory/performance_indicators.md]
use_when: ["EnPI seçimi yapılacağında", "Sektörel EnPI karşılaştırması gerektiğinde", "Exergy bazlı EnPI sorgulandığında"]
priority: high
last_updated: 2026-02-01
---

# Enerji Performans Göstergeleri Rehberi (ISO 50006)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

Enerji Performans Göstergesi (EnPI — Energy Performance Indicator), bir organizasyonun enerji performansını ölçmek için kullanılan nicel değer veya ölçüdür. ISO 50006:2014, ISO 50001:2018 standardının zorunlu kıldığı EnPI ve EnB (Energy Baseline) oluşturma sürecine detaylı rehberlik sağlar.

### 1.1 EnPI vs KPI Farkı

| Özellik | EnPI | KPI |
|---------|------|-----|
| Odak | Enerji performansı | Genel iş performansı |
| Standart | ISO 50006 / ISO 50001 | Çeşitli (ISO 9001, BSC, vb.) |
| Normalizasyon | Zorunlu (ilgili değişkenler) | Opsiyonel |
| Baseline | EnB ile karşılaştırma zorunlu | Hedef bazlı |
| Örnek | kWh/ton ürün, exergy verimi | OEE, fire oranı, müşteri memnuniyeti |
| Termodinamik boyut | Var (enerji/exergy bazlı) | Genellikle yok |

### 1.2 EnPI Hiyerarşisi

```
EnPI hiyerarşisi (üstten alta):

Tesis Seviyesi:
├── Toplam enerji tüketimi [TEP/yıl]
├── Enerji yoğunluğu [TEP/ton ürün]
├── Enerji maliyeti oranı [TL/ton ürün]
└── Fabrika exergy verimi [%]

Sistem Seviyesi:
├── Buhar sistemi SEC [kg buhar/ton ürün]
├── Basınçlı hava SPC [kW/(m³/min)]
├── Soğutma sistemi COP [—]
├── Aydınlatma LPD [W/m²]
└── Her sistem exergy verimi [%]

Ekipman Seviyesi:
├── Kazan yanma verimi [%]
├── Kompresör özgül güç [kW/(m³/min)]
├── Chiller COP [—]
├── Pompa verimi [%]
└── Her ekipman exergy verimi [%]

Raporlama sıklığı:
  Tesis seviyesi → Üst yönetime çeyreklik
  Sistem seviyesi → Enerji ekibine aylık
  Ekipman seviyesi → Operasyona haftalık/günlük
```

## 2. EnPI Türleri ve Seçim (EnPI Types and Selection)

### 2.1 Altı EnPI Türü

**Tür 1 — Mutlak Tüketim (Absolute Consumption)**

```
Formül: EnPI = E_toplam [kWh/yıl veya TEP/yıl]

Avantajlar:
├── Hesaplaması kolay
├── Toplam enerji maliyetini gösterir
└── İklim hedefleri ile uyumlu (toplam CO₂)

Dezavantajlar:
├── Üretim değişikliklerini yansıtmaz
├── Kapasite artışında yanıltıcı olabilir
└── Normalizasyon yok

Uygun durum:
├── Sabit üretimli tesisler
├── Genel enerji bütçe takibi
└── Ulusal enerji istatistikleri
```

**Tür 2 — Spesifik Enerji Tüketimi (Specific Energy Consumption — SEC)**

```
Formül: EnPI = E_toplam / P_üretim [kWh/ton]

Avantajlar:
├── Üretim bazlı karşılaştırma imkanı
├── Sektörel benchmark ile kıyaslanabilir
├── Anlaşılması kolay
└── En yaygın kullanılan EnPI türü

Dezavantajlar:
├── Tek ürün için ideal, çoklu ürün karmaşık
├── Baseload'u hesaba katmaz
├── Doğrusal olmayan ilişkilerde yanıltıcı
└── Kapasite kullanım oranı etkisi

Uygun durum:
├── Tek ürün üreten tesisler
├── Sektörel benchmark karşılaştırma
└── Yönetime basit raporlama
```

**Tür 3 — Enerji Yoğunluğu (Energy Intensity)**

```
Formül: EnPI = E_toplam / Alan [kWh/m²] veya E_toplam / Ciro [kWh/M€]

Avantajlar:
├── Bina ve ofis sektörü için standart
├── Farklı büyüklükteki binaları karşılaştırır
└── Ekonomik enerji verimliliği ölçümü (ciro bazlı)

Dezavantajlar:
├── Proses yoğun sanayide yetersiz
├── İklim ve çalışma saati etkisi
└── Ciro bazlı → fiyat dalgalanmalarına duyarlı

Uygun durum:
├── Ticari binalar, AVM'ler
├── Ofis ve hizmet sektörü
└── Makro ekonomik karşılaştırma
```

**Tür 4 — Regresyon Bazlı (Regression-Based)**

```
Formül: EnPI = (E_gerçek - E_model) / E_model × 100 [%]
  veya: EnPI = E_gerçek / E_model [—]

Avantajlar:
├── Çoklu değişken etkisini normalize eder
├── İklim, üretim, çalışma saati etkisi ayıklanır
├── ISO 50006 tarafından en çok önerilen tür
└── İstatistiksel güvenilirlik ölçülebilir

Dezavantajlar:
├── Model kurulumu uzmanlık gerektirir
├── Veri kalitesi kritik
├── Anlaşılması daha zor
└── Model bakımı gerekir (periyodik revizyon)

Uygun durum:
├── Birden fazla etkileyen değişken varsa
├── Mevsimsel üretim yapan tesisler
├── ISO 50001 sertifikasyonu hedeflenen tesisler
└── M&V (ölçüm ve doğrulama) projeleri
```

**Tür 5 — Oran Bazlı (Ratio-Based)**

```
Formül: EnPI = E_kaynak / E_toplam × 100 [%]
  veya: EnPI = E_sistem / E_toplam × 100 [%]

Avantajlar:
├── Enerji dağılım analizi
├── Kaynak çeşitlendirme izleme
├── Yenilenebilir enerji payı takibi
└── Sistemler arası önceliklendirme

Dezavantajlar:
├── Toplam performans değişimini göstermez
├── Mutlak tüketim artışını maskeleyebilir
└── Yalnız başına yetersiz

Uygun durum:
├── Enerji kaynak portföyü yönetimi
├── Yenilenebilir enerji hedefleri
├── Sistemler arası enerji dağılımı izleme
└── Sera gazı azaltma stratejileri
```

**Tür 6 — Exergy Bazlı (Exergy-Based)**

```
Formül: EnPI = η_ex = Ė_çıkış / Ė_giriş × 100 [%]
  veya: EnPI = SEC_ex = Ė_giriş / P_üretim [kJ_ex/ton]

Avantajlar:
├── Termodinamik kaliteyi ölçer
├── Gerçek iyileştirme potansiyelini gösterir
├── Farklı enerji formlarını adil karşılaştırır
├── Düşük sıcaklık kayıplarını yakalar
└── ExergyLab'ın benzersiz katkısı

Dezavantajlar:
├── Hesaplama karmaşıklığı (CoolProp/tablo gerekli)
├── Yaygın olarak bilinmemesi
├── Sektörel benchmark veri tabanı sınırlı
└── Ölü durum (dead state) tanımı gerekli

Uygun durum:
├── Isı yoğun prosesler (buhar, kurutma, fırın)
├── Kojenerasyon / trigeneration değerlendirme
├── Cross-equipment entegrasyon analizi
├── Ileri düzey enerji etüdleri
└── ExergyLab kullanıcıları
```

### 2.2 EnPI Seçim Karar Matrisi

| Durum | 1. Tercih | 2. Tercih | Kaçınılacak |
|-------|-----------|-----------|-------------|
| Tek ürün, stabil üretim | SEC | Regresyon | — |
| Çoklu ürün, değişken üretim | Regresyon | Ağırlıklı SEC | Mutlak |
| Isı yoğun proses | Exergy bazlı | SEC | Oran |
| Ofis/bina | Enerji yoğunluğu | Mutlak | SEC |
| ISO 50001 sertifikasyon | Regresyon | SEC | Mutlak |
| Yönetim raporu | SEC | Mutlak | Regresyon |
| Teknik analiz | Exergy bazlı | Regresyon | Mutlak |
| Kojenerasyon | Exergy bazlı | Regresyon | SEC |

## 3. Exergy Bazlı EnPI — ExergyLab Benzersiz Katkısı

### 3.1 Neden Exergy EnPI?

Enerji bazlı EnPI'lar (SEC, verimlilik), termodinamiğin 1. yasasına dayanır ve enerjinin kalitesini göz ardı eder. Örneğin, bir kazanın enerji verimi %90 olabilir; ancak 2000°C'lik yakma sıcaklığından 180°C buhar üretmek büyük bir exergy kaybıdır. Exergy EnPI, 2. yasa perspektifini katarak gerçek iyileştirme potansiyelini ortaya koyar.

### 3.2 Enerji EnPI'nın Sınırları

```
Örnek — Kazan analizi:

Enerji perspektifi:
  Yakıt giriş: 10.000 kW (LHV)
  Buhar çıkış: 9.000 kW (enthalpy bazlı)
  Baca gazı kaybı: 800 kW
  Yüzey kaybı: 200 kW
  Enerji verimi: 9.000 / 10.000 = %90 → "Verimli kazan"

Exergy perspektifi:
  Yakıt exergy giriş: 10.400 kW (kimyasal exergy)
  Buhar exergy çıkış: 3.640 kW (fiziksel exergy, T_buhar=180°C)
  Baca gazı exergy kaybı: 420 kW
  Yüzey exergy kaybı: 80 kW
  Exergy yıkımı (yanma irreversibilite): 6.260 kW
  Exergy verimi: 3.640 / 10.400 = %35 → "Büyük iyileşme potansiyeli"

Sonuç: Enerji EnPI %90 der, "iyi". Exergy EnPI %35 der, "6.260 kW potansiyel var."
Exergy EnPI gerçek termodinamik resmi gösterir.
```

### 3.3 Exergy Verim Formülleri

```
Kazan exergy verimi:
  η_ex = Ė_buhar / Ė_yakıt
  Ė_buhar = ṁ × [(h_buhar - h₀) - T₀ × (s_buhar - s₀)]
  Ė_yakıt ≈ LHV × φ   (φ: kimyasal exergy/LHV oranı, doğalgaz≈1.04)

Kompresör exergy verimi:
  η_ex = Ė_basınçlı_hava / Ẇ_kompresör
  Ė_basınçlı_hava = ṁ × R × T₀ × ln(P₂/P₁) (izotermale yakın)

Chiller exergy verimi:
  η_ex = Ė_soğutma / Ẇ_kompresör
  Ė_soğutma = Q̇_soğutma × (T₀/T_soğuk - 1) (ters Carnot)

Pompa exergy verimi:
  η_ex = Ė_basınç_artışı / Ẇ_pompa
  Ė_basınç_artışı = V̇ × ΔP (sıkıştırılamaz akışkan)
```

### 3.4 Sektörel Exergy EnPI Benchmark Tablosu

| Sektör | Tipik Enerji Verimi | Tipik Exergy Verimi | Exergy EnPI Hedef | Açıklama |
|--------|--------------------|--------------------|-------------------|----------|
| Çimento | %55-65 (termal) | %25-35 | ≥%30 | Yüksek sıcaklık prosesi |
| Kimya | %70-85 | %30-50 | ≥%40 | Proses bağımlı geniş aralık |
| Gıda | %60-80 | %15-30 | ≥%25 | Düşük sıcaklık, çok kayıp |
| Tekstil | %55-75 | %20-35 | ≥%28 | Kurutma ve boyama yoğun |
| Metal | %40-60 | %20-40 | ≥%30 | Ergitme yüksek exergy kaybı |
| Kağıt | %60-80 | %25-40 | ≥%32 | Kurutma seksiyonu kritik |
| Otomotiv | %45-65 | %20-35 | ≥%28 | Boyama + ısıl işlem |

## 4. Sektörel EnPI Örnekleri (Sectoral EnPI Examples)

### 4.1 Detaylı Sektörel Karşılaştırma

| Sektör | EnPI Türü | Birim | İyi | Ortalama | Zayıf | Açıklama |
|--------|-----------|-------|-----|----------|-------|----------|
| Çimento | SEC (klinker) | kWh/ton klinker | <95 | 95-115 | >115 | Elektrik tüketimi |
| Çimento | SEC (termal) | kcal/kg klinker | <720 | 720-850 | >850 | Fırın termal tüketim |
| Kimya | SEC (etilen) | kWh/ton | <4.500 | 4.500-5.500 | >5.500 | Steam cracking |
| Kimya | SEC (klor-alkali) | kWh/ton NaOH | <2.200 | 2.200-2.800 | >2.800 | Membran hücre |
| Gıda (süt) | SEC | kWh/ton süt | <80 | 80-120 | >120 | Pastörizasyon dahil |
| Gıda (bira) | SEC | kWh/hL bira | <8 | 8-14 | >14 | Fermantasyon + soğutma |
| Tekstil (boyama) | SEC | kWh/ton kumaş | <1.800 | 1.800-2.500 | >2.500 | Boyahane toplam |
| Tekstil (boyama) | Spesifik buhar | kg/kg kumaş | <8 | 8-15 | >15 | Buhar tüketimi |
| Metal (döküm) | SEC | kWh/ton döküm | <550 | 550-700 | >700 | İndüksiyon ocağı |
| Kağıt | SEC | kWh/ton kağıt | <600 | 600-900 | >900 | Toplam elektrik |
| Kağıt | Spesifik buhar | ton/ton kağıt | <1.5 | 1.5-2.5 | >2.5 | Kurutma buharı |
| Otomotiv | SEC | kWh/araç | <800 | 800-1.200 | >1.200 | Boyama + montaj |

### 4.2 Sektörel ExPI (Exergy Performance Indicator) Tablosu

| Sektör | ExPI Türü | Birim | İyi | Ortalama | Zayıf |
|--------|-----------|-------|-----|----------|-------|
| Çimento | Exergy verimi | % | >32 | 25-32 | <25 |
| Kimya | Exergy verimi | % | >45 | 30-45 | <30 |
| Gıda | Exergy verimi | % | >28 | 18-28 | <18 |
| Tekstil | Exergy verimi | % | >30 | 22-30 | <22 |
| Metal | Exergy verimi | % | >35 | 25-35 | <25 |
| Kağıt | Exergy verimi | % | >38 | 28-38 | <28 |

## 5. EnPI Oluşturma Adımları (EnPI Development Steps)

### 5.1 Sekiz Adımlı Süreç

```
EnPI oluşturma akış şeması:

Adım 1 — Kapsam Belirleme:
├── SEU'ları belirle (enerji incelemesinden)
├── Sınır koşullarını tanımla (tesis, sistem, ekipman)
├── Hangi seviyede EnPI gerekli?
└── Çıktı: Kapsam dokümanı

Adım 2 — Veri Toplama:
├── Enerji tüketim verileri (fatura, sayaç, SCADA)
├── Üretim verileri (ton, adet, m²)
├── İlgili değişkenler (iklim, çalışma saati, hammadde)
├── Minimum 12 ay (tercihen 24-36 ay)
└── Çıktı: Veri tablosu (aylık/haftalık/günlük)

Adım 3 — Değişken Seçimi:
├── Enerji tüketimini etkileyen değişkenleri belirle
├── Scatter plot analizi (görsel korelasyon)
├── Pearson korelasyon katsayısı (|r| > 0.7 hedef)
├── Kontrol edilebilir vs kontrol edilemez değişkenler
└── Çıktı: İlgili değişken listesi

Adım 4 — EnPI Modeli Seçimi:
├── Tek değişken → SEC veya basit regresyon
├── Çok değişken → Çoklu regresyon
├── Isı yoğun → Exergy bazlı EnPI ekleme
├── Karar matrisi kullan (Bölüm 2.2)
└── Çıktı: Seçilen EnPI tipi ve formül

Adım 5 — Model Doğrulama:
├── R² kontrolü (≥0.75 aylık veri için)
├── CV-RMSE kontrolü (≤%25 aylık veri için)
├── NMBE kontrolü (±%10)
├── Residual analizi (normallik, pattern)
└── Çıktı: Doğrulama raporu

Adım 6 — Hedef Belirleme:
├── Baseline dönemi performans (EnB)
├── Hedef: %X iyileşme (yıllık)
├── Sektörel benchmark ile karşılaştırma
├── Ulaşılabilir ve zorlayıcı hedef
└── Çıktı: EnPI hedef değeri

Adım 7 — İzleme Süreci:
├── Veri toplama sıklığı belirleme
├── Kontrol grafikleri oluşturma
├── Alarm eşikleri tanımlama
├── CUSUM analizi başlatma
├── Raporlama formatı ve sıklığı
└── Çıktı: İzleme prosedürü

Adım 8 — Periyodik Revizyon:
├── Yıllık model doğrulama
├── EnB ayarlama gereksinimi kontrolü
├── Yeni değişken ekleme değerlendirmesi
├── Hedef güncelleme
└── Çıktı: Revizyon raporu
```

## 6. EnPI Raporlama ve Görselleştirme (Reporting and Visualization)

### 6.1 Kontrol Grafikleri

```
EnPI kontrol grafiği yapısı:

Y ekseni: EnPI değeri (örn: kWh/ton)
X ekseni: Zaman (ay veya hafta)

Çizgiler:
├── Hedef çizgisi (target line) — kesikli yeşil
├── UCL (Upper Control Limit) — kırmızı üst sınır (+2σ)
├── LCL (Lower Control Limit) — kırmızı alt sınır (-2σ)
├── Uyarı sınırı — turuncu (±1.5σ)
├── Ortalama — mavi düz çizgi
└── Gerçek EnPI — siyah nokta ve çizgi

Renk kodlaması:
├── Yeşil bölge: LCL altı (hedefin altında — iyi performans)
├── Sarı bölge: Ortalama civarı (normal)
└── Kırmızı bölge: UCL üstü (kötü performans — aksiyon gerekli)
```

### 6.2 Dashboard Tasarımı

| Hedef Kitle | İçerik | Güncelleme | Format |
|-------------|--------|-----------|--------|
| Üst yönetim | Fabrika SEC, toplam maliyet, trend | Çeyreklik | Özet dashboard, trafik ışığı |
| Enerji ekibi | SEU EnPI'ları, CUSUM, alarm | Aylık | Detaylı grafik, tablo |
| Operasyon | Ekipman EnPI, anlık değer | Günlük/saatlik | Ekran göstergeleri, alarm |
| Denetçi | EnB vs gerçek, normalizasyon | Yıllık | ISO 50001 uyumlu rapor |

### 6.3 Yönetime Sunum Formatı

```
Aylık enerji performans raporu yapısı:

Sayfa 1 — Yönetici özeti:
├── Bu ay fabrika SEC: 142 kWh/ton (hedef: 135)
├── Trend: Son 3 ayda %2.1 artış (olumsuz)
├── CUSUM: +45 MWh kümülatif (performans düşüşü)
├── Exergy verimi: %26.8 (sektör ort: %28)
└── Aksiyon: Kompresör bakımı + buhar kaçak onarımı

Sayfa 2 — SEU detay:
├── Her SEU için EnPI tablo + grafik
├── En çok sapma gösteren 3 SEU
└── Planlanan aksiyonlar ve takvim

Sayfa 3 — CUSUM ve trend grafikleri
Sayfa 4 — Ekonomik etki (TL/ay sapma)
```

## 7. Yaygın Hatalar ve Çözümleri (Common Mistakes)

| # | Hata | Sonuç | Çözüm |
|---|------|-------|-------|
| 1 | Yanlış normalleştirme — üretimi göz ardı etme | Kapasite artışı tasarruf gibi görünür | Regresyon modeli veya SEC kullan |
| 2 | Yetersiz veri — <12 ay ile model kurma | Mevsimsel etkiler yakalanamaz | Min. 12 ay, tercihen 24 ay veri topla |
| 3 | Aşırı karmaşık model — >5 değişken | Overfitting, yorumlanması zor | KISS prensibi: 2-3 değişken yeterli |
| 4 | Baseload'u göz ardı etme | Düşük üretimde SEC şişer | Regresyon sabitini (β₀) dahil et |
| 5 | Tek EnPI ile yetinme | Kısmi görünüm, saklı sorunlar | Hiyerarşik EnPI seti kullan |
| 6 | Exergy boyutunu atlama | Kalite kaybını görememe | Enerji + exergy EnPI birlikte kullan |
| 7 | Eski baseline ile karşılaştırma | Model artık geçerli değil | 3-5 yılda bir EnB revize et |
| 8 | Alarm eşiği koymama | Sapmalara geç müdahale | ±2σ kontrol limiti belirle |
| 9 | Veri kalitesini kontrol etmeme | Hatalı ölçüm → hatalı EnPI | Sayaç kalibrasyonu + veri temizleme |
| 10 | EnPI'yı paylaşmama | İyileştirme motivasyonu düşük | Dashboard ile şeffaf paylaşım |

## 8. Çalışılmış Örnek — Gıda Fabrikasında EnPI Seçimi ve İzleme

### 8.1 Tesis Tanımı

```
Tesis: Süt işleme fabrikası (pastörize süt, yoğurt, peynir)
Kapasite: 200 ton/gün süt işleme
Yıllık tüketim: 3.200 TEP (elektrik + doğalgaz)
Çalışma: 365 gün, 3 vardiya
SEU'lar: Buhar kazanları (%42), soğutma (%28), pastörizasyon (%15), diğer (%15)
```

### 8.2 EnPI Seçimi

```
EnPI seti:

Tesis seviyesi:
├── SEC_enerji = Toplam enerji / Toplam süt işleme [kWh/ton süt]
│   Baseline: 108 kWh/ton (24 ay ortalaması)
│   Hedef: 100 kWh/ton (%7.4 iyileşme)
│
└── η_ex_fabrika = Exergy çıkışı / Exergy girişi [%]
    Baseline: %22.4
    Hedef: %26.0

Sistem seviyesi:
├── SEC_buhar = Doğalgaz / Buhar üretimi [Sm³/ton buhar]
│   Baseline: 78 Sm³/ton (kazan verimi ~%87)
│   Hedef: 72 Sm³/ton
│
├── COP_soğutma = Q_soğutma / W_kompresör [—]
│   Baseline: 4.2
│   Hedef: 4.8
│
└── SEC_pastörizasyon = Enerji / Süt [kWh/ton süt]
    Baseline: 16.5 kWh/ton
    Hedef: 14.0 kWh/ton

Regresyon modeli (fabrika toplam):
E [MWh/ay] = 85 + 0.095 × Üretim [ton/ay] + 1.2 × CDD [°C·gün/ay]
R² = 0.91, CV-RMSE = %11.8, NMBE = +%1.2
```

### 8.3 İzleme Sonuçları (12 Ay)

| Ay | Üretim (ton) | E_gerçek (MWh) | E_model (MWh) | Fark (MWh) | SEC (kWh/ton) | CUSUM (MWh) |
|----|-------------|---------------|---------------|------------|---------------|-------------|
| Oca | 5.800 | 642 | 636 | +6 | 110.7 | +6 |
| Şub | 5.500 | 618 | 608 | +10 | 112.4 | +16 |
| Mar | 6.000 | 649 | 655 | -6 | 108.2 | +10 |
| Nis | 6.200 | 660 | 679 | -19 | 106.5 | -9 |
| May | 6.500 | 698 | 718 | -20 | 107.4 | -29 |
| Haz | 6.800 | 745 | 762 | -17 | 109.6 | -46 |
| Tem | 7.000 | 770 | 793 | -23 | 110.0 | -69 |
| Ağu | 6.800 | 738 | 762 | -24 | 108.5 | -93 |
| Eyl | 6.300 | 680 | 699 | -19 | 107.9 | -112 |
| Eki | 6.000 | 638 | 655 | -17 | 106.3 | -129 |
| Kas | 5.700 | 600 | 627 | -27 | 105.3 | -156 |
| Ara | 5.600 | 588 | 617 | -29 | 105.0 | -185 |

### 8.4 Sonuç Yorumu

```
12 aylık izleme sonuçları:

CUSUM: -185 MWh (negatif = tasarruf sağlanmış)
Yıllık tasarruf: ~185 MWh = 15.9 TEP
Maliyet tasarrufu: ~185.000 kWh × 2.5 TL/kWh = 462.500 TL/yıl
SEC iyileşmesi: 108 → ~107.1 kWh/ton (%0.8 iyileşme — henüz hedefe ulaşılmadı)

ExergyLab exergy analizi ek bulguları:
├── Kazan exergy verimi %34.2 → Economizer ile %41 hedeflenebilir
├── Soğutma exergy verimi %18.5 → Kondenser temizliği ile %22 hedeflenebilir
├── Pastörizasyon ısı geri kazanımı exergy potansiyeli: 45 kW
└── Fabrika toplam exergy verimi %22.4 → %26 hedefi için ek projeler gerekli

Aksiyon planı:
1. Kazan economizer (VAP başvurusu — Bkz: turkey_incentives.md)
2. Chiller kondenser temizleme programı
3. Pastörizasyon plakalı eşanjör optimizasyonu
4. Buhar kaçak onarımı (trap audit)
```

## 9. İlgili Dosyalar

- [Enerji Yönetimi INDEX](INDEX.md) — Dosya navigasyonu
- [Baseline ve EnPI (ISO 50006)](baseline_enpi.md) — Regresyon modeli ve baseline oluşturma detayı
- [CUSUM Analizi](cusum_analysis.md) — Kümülatif toplam analizi ile performans izleme
- [M&T Sistemi](monitoring_targeting.md) — Ölçüm hiyerarşisi ve hedefleme
- [KPI Tanımları](../kpi_definitions.md) — Genel performans gösterge çerçevesi
- [Performans Göstergeleri](../performance_indicators.md) — Fabrika seviyesi göstergeler
- [Sektörel Benchmark](../factory_benchmarks.md) — Sektör karşılaştırma verileri

## 10. Referanslar

- ISO 50006:2014, "Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI) — General principles and guidance"
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50015:2014, "Measurement and verification of energy performance of organizations"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- US DOE, "EnPI Tool v5.0 — User Guide" (regression-based EnPI tool)
- Bejan, A., Tsatsaronis, G., Moran, M., "Thermal Design and Optimization", Wiley, 1996
- Dincer, I., Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development", 3rd ed., Elsevier, 2021
- Carbon Trust, "Energy Management — A Comprehensive Guide to Controlling Energy Use"
- YEGM, "Enerji Etüdü Usul ve Esasları"
- SEE Action, "A National Assessment of Demand Response Potential"
