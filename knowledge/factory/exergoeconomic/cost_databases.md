---
title: "Maliyet Veritabanları ve Endeksler (Cost Databases & Indices)"
category: factory
equipment_type: factory
keywords: [CEPCI, Marshall Swift, maliyet endeksi, Türkiye, enflasyon, döviz]
related_files:
  - factory/exergoeconomic/cost_equations.md
  - factory/exergoeconomic/levelized_cost.md
  - factory/exergoeconomic/sensitivity_analysis.md
  - factory/economic_analysis.md
use_when:
  - "Maliyet endeksi güncellemesi yapılırken"
  - "Tarihsel PEC verisi güncellenirken"
  - "Türkiye'ye özgü maliyet parametreleri aranırken"
priority: medium
last_updated: 2026-02-01
---
# Maliyet Veritabanları ve Endeksler (Cost Databases & Indices)

> Son güncelleme: 2026-02-01

## 1. Maliyet Endeksleri

Ekipman maliyet korelasyonları belirli bir referans yılına göre geliştirilmiştir. Güncel maliyeti elde etmek için maliyet endeksleri ile zaman düzeltmesi yapılır.

```
Genel Formül:

PEC_güncel = PEC_referans × (Endeks_güncel / Endeks_referans)

Örnek:
  PEC_2012 = 92.000 EUR (Turton 2012 korelasyonu)
  CEPCI_2012 = 584.6
  CEPCI_2024 = 810
  PEC_2024 = 92.000 × (810 / 584.6) = 127.474 EUR
```

### 1.1 CEPCI (Chemical Engineering Plant Cost Index)

CEPCI, Chemical Engineering Magazine tarafından aylık yayınlanan ve kimya/enerji endüstrisinde en yaygın kullanılan maliyet endeksidir.

| Yıl | CEPCI | Not |
|-----|-------|-----|
| 1990 | 357.6 | — |
| 1994 | 368.1 | Bejan et al. (1996) referans yılı |
| 1996 | 381.7 | — |
| 2000 | 394.1 | — |
| 2001 | 394.3 | Turton (2003) referans yılı |
| 2002 | 395.6 | — |
| 2003 | 402.0 | — |
| 2004 | 444.2 | — |
| 2005 | 468.2 | — |
| 2006 | 499.6 | — |
| 2007 | 525.4 | — |
| 2008 | 575.4 | — |
| 2009 | 521.9 | Ekonomik kriz etkisi |
| 2010 | 550.8 | — |
| 2011 | 585.7 | — |
| 2012 | 584.6 | Turton (2012) referans yılı |
| 2013 | 567.3 | — |
| 2014 | 576.1 | — |
| 2015 | 556.8 | Düşük emtia fiyatları |
| 2016 | 541.7 | — |
| 2017 | 567.5 | — |
| 2018 | 603.1 | — |
| 2019 | 607.5 | — |
| 2020 | 596.2 | COVID-19 etkisi |
| 2021 | 708.0 | Tedarik zinciri krizi |
| 2022 | 816.0 | Enflasyon/enerji krizi |
| 2023 | 797.9 | Kısmi normalleşme |
| 2024 | 810 | Tahmini |
| 2025 | 825 | Tahmini |

### 1.2 Marshall & Swift Equipment Cost Index

| Yıl | M&S Index | Not |
|-----|-----------|-----|
| 1990 | 915.1 | — |
| 1996 | 1039.2 | — |
| 2000 | 1089.0 | — |
| 2005 | 1244.5 | — |
| 2010 | 1457.4 | — |
| 2012 | 1536.5 | — |
| 2015 | 1556.8 | — |
| 2018 | 1638.2 | — |
| 2020 | 1596.7 | — |
| 2022 | 1850 | Tahmini (yayın durduruldu) |

> **Not:** Marshall & Swift endeksi 2012 sonrasında düzensiz yayınlanmıştır. CEPCI kullanımı önerilir.

### 1.3 Diğer Endeksler

| Endeks | Kapsam | Kaynak |
|--------|--------|--------|
| Nelson-Farrar (NF) | Rafineri ekipmanları | Oil & Gas Journal |
| ENR Building Cost | İnşaat | Engineering News-Record |
| Handy-Whitman | Enerji santralleri | Whitman, Requardt & Associates |
| IHS Downstream Capital Cost Index | Petrokimya | IHS Markit |

## 2. Türkiye'ye Özel Maliyet Parametreleri

### 2.1 Enerji Fiyatları (Exergy Maliyeti Girdisi)

```
Türkiye Enerji Fiyatları (2024-2025 tahmini):

Elektrik (endüstriyel):
  Düşük gerilim:  0.08-0.12 €/kWh
  Orta gerilim:   0.06-0.10 €/kWh
  Yüksek gerilim: 0.05-0.08 €/kWh
  → c_elektrik = fiyat / 3600 [€/kJ]
  → Tipik: 0.022-0.033 ×10⁻³ €/kJ

Doğalgaz (endüstriyel):
  Fiyat: 0.025-0.040 €/kWh_th (HHV bazlı)
  LHV: ~36 MJ/m³ (karışıma bağlı)
  Exergy/LHV oranı: ~1.04
  → c_doğalgaz = fiyat / (exergy/birim)
  → Tipik: 0.007-0.011 ×10⁻³ €/kJ

Kömür (endüstriyel):
  Fiyat: 80-150 €/ton (kaliteye bağlı)
  LHV: 15-25 MJ/kg
  → c_kömür = 0.004-0.008 ×10⁻³ €/kJ

Fuel oil:
  Fiyat: 0.45-0.70 €/kg
  LHV: ~40 MJ/kg
  → c_fueloil = 0.011-0.018 ×10⁻³ €/kJ

Biyokütle:
  Fiyat: 40-80 €/ton (tiplerine bağlı)
  LHV: 10-18 MJ/kg
  → c_biokütle = 0.003-0.006 ×10⁻³ €/kJ
```

### 2.2 Finansal Parametreler

```
Türkiye Ekonomik Parametreleri (2024-2025):

Faiz oranı (nominal):
  TCMB politika faizi: %42.5 (2024 Q4)
  Ticari kredi faizi: %45-55 (TRY)
  Döviz kredisi: %6-9 (EUR)

Enflasyon:
  TÜFE: %44.4 (2024 yıllık)
  ÜFE: %36.4 (2024 yıllık)
  Hedef: %5 (uzun vadeli)

Reel faiz oranı:
  TRY bazlı: %0-10 (nominal - enflasyon)
  EUR bazlı: %3-6 (tipik proje değerlendirme)

WACC (Ağırlıklı Ortalama Sermaye Maliyeti):
  TRY projeler: %35-50 (nominal)
  EUR projeler: %8-12 (reel)

ExergyLab önerisi:
  Exergoekonomik analiz EUR bazlı yapılmalı
  Reel iskonto oranı: %8-12
  → CRF hesabında i = 0.10 (önerilen)
```

### 2.3 İşgücü ve Bakım Maliyetleri

```
Türkiye İşgücü Maliyetleri:
  Mühendis (enerji): 30,000-60,000 €/yıl
  Teknisyen: 15,000-30,000 €/yıl
  Operatör: 12,000-25,000 €/yıl

Bakım Maliyeti (PEC'in yüzdesi):
  Kompresör: %3-5/yıl
  Kazan: %2-4/yıl
  Türbin: %3-6/yıl
  Pompa: %2-4/yıl
  HX: %1-3/yıl
  Chiller: %3-5/yıl

OM (Operating & Maintenance) faktörü:
  Ż_OM = γ × PEC (yıllık)
  Tipik γ = 0.015-0.060

  veya Ż_OM = φ × Ż_CI
  Tipik φ = 0.3-0.6
```

## 3. Dönüşüm Tabloları

### 3.1 Birim Exergy Maliyeti Dönüşümleri

```
€/kJ → €/MWh:     × 3,600,000 / 1000 = × 3600
€/kJ → €/GJ:      × 1,000,000
€/kJ → ct/kWh:    × 360,000
€/MWh → €/kJ:     / 3600

Örnek:
  c = 0.025 ×10⁻³ €/kJ = 0.025 €/MJ = 25 €/GJ = 90 €/MWh = 9.0 ct/kWh
```

### 3.2 Yaygın Exergy Birim Maliyetleri

| Kaynak | c [€/GJ] | c [€/MWh] | c [×10⁻³ €/kJ] | Not |
|--------|----------|-----------|-----------------|-----|
| Doğalgaz | 7-11 | 25-40 | 0.007-0.011 | Türkiye, 2024 |
| Kömür | 4-8 | 14-29 | 0.004-0.008 | Kaliteye bağlı |
| Elektrik (şebeke) | 17-33 | 60-120 | 0.017-0.033 | Endüstriyel |
| Buhar (10 bar) | 20-35 | 72-126 | 0.020-0.035 | Üretim yöntemine bağlı |
| Buhar (40 bar) | 15-25 | 54-90 | 0.015-0.025 | Yüksek basınç |
| Soğutma suyu (7°C) | 30-60 | 108-216 | 0.030-0.060 | Düşük exergy |
| Basınçlı hava (7 bar) | 25-45 | 90-162 | 0.025-0.045 | Kompresör çıkışı |

## 4. Online Kaynaklar ve Veritabanları

### 4.1 Ücretsiz Kaynaklar

| Kaynak | URL/Erişim | İçerik |
|--------|------------|--------|
| Chemical Engineering CEPCI | chemengonline.com | Aylık CEPCI (abonelik) |
| NIST WebBook | webbook.nist.gov | Termodinamik özellikler |
| EPDK (Türkiye) | epdk.gov.tr | Enerji fiyatları |
| TÜİK | tuik.gov.tr | Enflasyon, endeksler |
| TCMB | tcmb.gov.tr | Faiz, döviz kuru |

### 4.2 Ticari Veritabanları

| Kaynak | İçerik | Not |
|--------|--------|-----|
| Aspen In-Plant Cost Estimator | Detaylı PEC | Lisans gerekli |
| IHS Markit | Ekipman maliyetleri | Abonelik |
| Matches (matche.com) | Hızlı PEC tahmini | Ücretsiz (temel) |
| CostMine | Maden/enerji ekipmanı | Abonelik |

### 4.3 Akademik Referanslar

| Kitap | Yıl | PEC Kapsamı |
|-------|-----|-------------|
| Turton et al. — Analysis, Synthesis, and Design | 2012 | En kapsamlı korelasyonlar |
| Peters, Timmerhaus & West — Plant Design | 2003 | Klasik referans |
| Couper et al. — Chemical Process Equipment | 2012 | Ekipman seçimi odaklı |
| Bejan et al. — Thermal Design | 1996 | Exergoekonomik odaklı |

## 5. Maliyet Tahmini Doğrulama Yöntemleri

```
Doğrulama Yaklaşımı:

1. Birden fazla korelasyon ile tahmin yap
2. Sonuçları karşılaştır (sapma < %40 kabul edilebilir)
3. Varsa üretici teklifleri ile doğrula
4. Benzer tesis verisi ile kıyasla

Kalite Sınıflandırması:
  Sınıf 5 (fikir aşaması):     ±30-50%  ← Korelasyon tahmini
  Sınıf 4 (ön fizibilite):     ±20-30%  ← Korelasyon + düzeltme
  Sınıf 3 (fizibilite):        ±10-20%  ← Üretici ön teklifi
  Sınıf 2 (bütçe):             ±5-15%   ← Detaylı teklif
  Sınıf 1 (kesin):             ±3-5%    ← Sözleşme fiyatı
```

## 6. Enflasyon ve Döviz Kuru Etkisi

### 6.1 Çoklu Para Birimi Analizi

```
ExergyLab analizi EUR bazlı yapılır:

Döviz dönüşümü:
  Akademik korelasyonlar genellikle EUR bazlı referans alınır.
  Farklı para birimlerinden dönüşüm:
    PEC_EUR = PEC_TRY / (EUR/TRY kuru)
    2024 ortalama: 1 EUR ≈ 34-36 TRY

Dikkat:
  - Tüm maliyet analizleri EUR bazlı yapılmalı
  - Türkiye'de yerli üretim TRY bazlı → EUR'ya çevrilmeli
  - Analiz tutarlılığı için tek para birimi kullanılmalı
```

### 6.2 Reel vs Nominal Analiz

```
Exergoekonomik analizde reel (sabit fiyat) analiz tercih edilir:

Nominal analiz:
  Tüm maliyetler güncel TRY ile → Enflasyon etkisi dahil
  Ż_nominal = Ż_reel × (1 + enflasyon)^n

Reel analiz (önerilen):
  EUR bazlı → Düşük enflasyon etkisi
  Reel iskonto oranı = (1 + i_nominal)/(1 + enflasyon) - 1

ExergyLab: EUR bazlı reel analiz (i_reel = %8-12)
```

## İlgili Dosyalar

- `factory/exergoeconomic/cost_equations.md` — PEC korelasyonları
- `factory/exergoeconomic/levelized_cost.md` — CRF ve Ż hesaplaması
- `factory/exergoeconomic/sensitivity_analysis.md` — Maliyet belirsizliği analizi
- `factory/economic_analysis.md` — Geleneksel ekonomik analiz
- `factory/energy_pricing.md` — Enerji fiyatlandırma detayları

## Referanslar

1. Chemical Engineering Magazine — CEPCI Historical Data. chemengonline.com
2. Turton, R., et al. (2012). *Analysis, Synthesis, and Design of Chemical Processes*. 4th Ed.
3. Peters, M.S., Timmerhaus, K.D., West, R.E. (2003). *Plant Design and Economics for Chemical Engineers*. 5th Ed.
4. EPDK (2024). Enerji Piyasası Düzenleme Kurumu — Tarife tabloları. epdk.gov.tr
5. TCMB (2024). Türkiye Cumhuriyet Merkez Bankası — İstatistikler. tcmb.gov.tr
6. TÜİK (2024). Türkiye İstatistik Kurumu — Fiyat endeksleri. tuik.gov.tr
