---
title: "Yatırım Analizi Metodları (Economic Analysis Methods)"
category: factory
equipment_type: factory
keywords: [ekonomik analiz, maliyet, geri ödeme]
related_files: [factory/life_cycle_cost.md, factory/prioritization.md, factory/energy_pricing.md]
use_when: ["Ekonomik fizibilite hesaplanırken", "Geri ödeme süresi analiz edilirken"]
priority: medium
last_updated: 2026-01-31
---
# Yatırım Analizi Metodları (Economic Analysis Methods)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji verimlilik projelerinin ekonomik değerlendirmesi, doğru yatırım kararları için kritik öneme sahiptir. Bu dosya; basit geri ödeme süresi (SPP), iskontolu geri ödeme (DPP), net bugünkü değer (NPV), iç verim oranı (IRR), yatırım getirisi (ROI) ve duyarlılık analizi yöntemlerini kapsar.

## 1. Basit Geri Ödeme Süresi — SPP (Simple Payback Period)

### 1.1 Tanım ve Formül

```
SPP = C₀ / S_yıllık [yıl]

Burada:
- C₀ = Başlangıç yatırım maliyeti [€]
- S_yıllık = Yıllık net tasarruf [€/yıl]
```

### 1.2 Performans Sınıflandırması

| SPP | Değerlendirme | Öncelik | Tipik Projeler |
|---|---|---|---|
| <1 yıl | Mükemmel | Hemen uygula | Kaçak onarımı, basınç düşürme, kontrol |
| 1-2 yıl | Çok iyi | Yüksek öncelik | VSD, economizer, izolasyon |
| 2-3 yıl | İyi | Normal öncelik | Ekipman yenileme, ısı geri kazanımı |
| 3-5 yıl | Kabul edilebilir | Planlı yatırım | CHP, büyük sistem değişiklikleri |
| 5-7 yıl | Düşük | Stratejik değerlendirme | Bina iyileştirme, proses değişikliği |
| >7 yıl | Sınır | Özel gerekçe gerekli | Altyapı, uzun ömürlü yatırımlar |

### 1.3 Hesaplama Örneği

```
VSD Retrofit — Basınçlı hava kompresörü:
Yatırım: €18,000
Enerji tasarrufu: 85,000 kWh/yıl
Elektrik fiyatı: €0.12/kWh
Yıllık tasarruf: 85,000 × 0.12 = €10,200/yıl
Ek bakım maliyeti: €500/yıl

SPP = 18,000 / (10,200 - 500) = 18,000 / 9,700 = 1.86 yıl
```

### 1.4 SPP Sınırlamaları

```
SPP yöntemi dikkate ALMAZ:
- Paranın zaman değerini (iskonto oranı)
- Projenin ekonomik ömrünü
- Nakit akışlarının zamanlama farklarını
- Enflasyon ve enerji fiyat artışlarını
- Ekipman hurda/kalıntı değerini

Bu nedenle SPP, ön eleme ve hızlı karşılaştırma aracı olarak kullanılmalı,
kesin yatırım kararları için NPV/IRR ile desteklenmelidir.
```

## 2. Net Bugünkü Değer — NPV (Net Present Value)

### 2.1 Tanım ve Formül

```
NPV = -C₀ + Σᵢ₌₁ⁿ [Sᵢ / (1 + r)ⁱ]

Burada:
- C₀ = Başlangıç yatırım maliyeti [€]
- Sᵢ = i-inci yıl net tasarruf (nakit akışı) [€]
- r = İskonto oranı (discount rate) [oran]
- n = Proje ekonomik ömrü [yıl]

Sabit yıllık tasarruf için (anüite formülü):
NPV = -C₀ + S × [(1 + r)ⁿ - 1] / [r × (1 + r)ⁿ]
```

### 2.2 Karar Kriteri

| NPV Değeri | Karar |
|---|---|
| NPV > 0 | Proje kabul edilir (değer yaratır) |
| NPV = 0 | Marjinal proje (risk değerlendirmesi gerekli) |
| NPV < 0 | Proje reddedilir (ekonomik olarak uygun değil) |

### 2.3 Hesaplama Örneği

```
Economizer Yatırımı:
- C₀ = €35,000
- Yıllık yakıt tasarrufu: €12,000/yıl
- Ek bakım: €1,000/yıl
- Net yıllık tasarruf: S = €11,000/yıl
- Ekonomik ömür: n = 15 yıl
- İskonto oranı: r = %8

NPV = -35,000 + 11,000 × [(1.08)¹⁵ - 1] / [0.08 × (1.08)¹⁵]
    = -35,000 + 11,000 × [3.172 - 1] / [0.08 × 3.172]
    = -35,000 + 11,000 × 2.172 / 0.2538
    = -35,000 + 11,000 × 8.559
    = -35,000 + 94,152
    = €59,152

NPV > 0 → Proje kabul edilir.
```

### 2.4 İskonto Oranı Seçimi

| İskonto Oranı | Kullanım | Açıklama |
|---|---|---|
| %5-6 | Kamu/devlet projeleri | Düşük risk, sosyal fayda |
| %8-10 | Standart endüstriyel | Tipik WACC, orta risk |
| %12-15 | Yüksek risk projeleri | Yeni teknoloji, belirsizlik |
| %15-20 | Gelişmekte olan ülkeler | Yüksek enflasyon/risk ortamı |

```
Türkiye için önerilen iskonto oranları:
- Devlet destekli projeler: %8-10
- Özel sektör, düşük risk: %12-15
- Özel sektör, yüksek risk: %15-20
- ESCO projeleri: %10-15

Not: Enflasyon oranı yüksek olduğunda reel ve nominal
iskonto oranı ayrımına dikkat edilmelidir.
reel = (1 + nominal) / (1 + enflasyon) - 1
```

## 3. İç Verim Oranı — IRR (Internal Rate of Return)

### 3.1 Tanım

```
IRR: NPV = 0 yapan iskonto oranıdır.

NPV = -C₀ + Σᵢ₌₁ⁿ [Sᵢ / (1 + IRR)ⁱ] = 0

IRR analitik olarak çözülemez, iteratif yöntemlerle hesaplanır.
```

### 3.2 Karar Kriteri

| IRR vs. MARR | Karar |
|---|---|
| IRR > MARR | Proje kabul edilir |
| IRR = MARR | Marjinal proje |
| IRR < MARR | Proje reddedilir |

MARR = Minimum Acceptable Rate of Return (minimum kabul edilebilir getiri oranı)

### 3.3 Hesaplama Örneği

```
Economizer örneği (yukarıdaki):
- C₀ = €35,000
- S = €11,000/yıl (sabit)
- n = 15 yıl

Deneme-yanılma veya Excel IRR() fonksiyonu ile:
IRR ≈ %30.2

MARR = %12 varsayımıyla: IRR (%30.2) > MARR (%12) → Kabul
```

### 3.4 IRR Sınırlamaları

```
IRR'ın dikkat edilmesi gereken noktaları:
1. Birden fazla IRR: Nakit akışı işaret değiştirirse birden fazla IRR olabilir
2. Ölçek sorunu: Küçük ve büyük projeleri doğru karşılaştıramaz
   (€1,000 yatırım %100 IRR vs. €100,000 yatırım %30 IRR)
3. Yeniden yatırım varsayımı: IRR, ara nakit akışlarının IRR oranıyla
   yeniden yatırıldığını varsayar (gerçekçi olmayabilir)

Çözüm: MIRR (Modified IRR) veya NPV ile birlikte kullanmak
```

## 4. Yatırım Getirisi — ROI (Return on Investment)

### 4.1 Tanım

```
ROI = (Toplam_net_kazanç - Yatırım) / Yatırım × 100 [%]

Yıllık ROI:
ROI_yıllık = Yıllık_net_tasarruf / Yatırım × 100 [%]
```

### 4.2 Performans Sınıflandırması

| ROI (Yıllık) | Değerlendirme | Not |
|---|---|---|
| >%50 | Mükemmel | Quick win projeleri |
| %30-50 | Çok iyi | Standart enerji verimlilik projeleri |
| %15-30 | İyi | Orta vadeli projeler |
| %8-15 | Kabul edilebilir | Uzun vadeli, stratejik projeler |
| <%8 | Düşük | Özel gerekçe gerekli |

## 5. İskontolu Geri Ödeme Süresi — DPP (Discounted Payback Period)

### 5.1 Tanım

```
DPP: Σᵢ₌₁ᴰᴾᴾ [Sᵢ / (1 + r)ⁱ] ≥ C₀ koşulunu sağlayan minimum yıl sayısı

Sabit tasarruf için:
DPP = -ln(1 - C₀ × r / S) / ln(1 + r)
```

### 5.2 Hesaplama Örneği

```
Economizer örneği:
- C₀ = €35,000, S = €11,000/yıl, r = %8

DPP = -ln(1 - 35,000 × 0.08 / 11,000) / ln(1.08)
    = -ln(1 - 0.2545) / ln(1.08)
    = -ln(0.7455) / 0.07696
    = 0.2938 / 0.07696
    = 3.82 yıl

Karşılaştırma: SPP = 3.18 yıl, DPP = 3.82 yıl
DPP her zaman SPP'den büyüktür (paranın zaman değeri nedeniyle).
```

## 6. Enerji Verimlilik Projelerinin Karşılaştırmalı Analizi

### 6.1 Tipik Enerji Verimlilik Projeleri Ekonomik Göstergeleri

| Proje | Yatırım [€] | Yıllık Tasarruf [€] | SPP [yıl] | NPV [€]* | IRR [%] |
|---|---|---|---|---|---|
| Hava kaçağı onarımı | 2,000 | 15,000 | 0.13 | 88,000 | >%500 |
| Basınç düşürme (1 bar) | 0 | 8,000 | 0 | 54,000 | ∞ |
| Kompresör VSD | 18,000 | 10,200 | 1.8 | 43,000 | %55 |
| Economizer | 35,000 | 11,000 | 3.2 | 39,000 | %30 |
| Isı geri kazanımı (kompresör) | 12,000 | 5,500 | 2.2 | 19,000 | %44 |
| Buhar kapanı değişimi | 5,000 | 8,000 | 0.6 | 49,000 | >%100 |
| İzolasyon iyileştirme | 8,000 | 4,500 | 1.8 | 22,000 | %55 |
| LED aydınlatma | 25,000 | 9,000 | 2.8 | 26,000 | %35 |
| Chiller optimizasyonu | 15,000 | 6,000 | 2.5 | 21,000 | %39 |
| CHP sistemi (500 kWe) | 350,000 | 85,000 | 4.1 | 227,000 | %23 |
| Proses ısı entegrasyonu | 80,000 | 30,000 | 2.7 | 122,000 | %37 |

*NPV: 15 yıl, %8 iskonto oranı

### 6.2 Karar Matrisi

```
Çoklu proje değerlendirmesi:

1. Ön eleme: SPP < 7 yıl (veya kuruluş politikası)
2. Sıralama: NPV büyükten küçüğe
3. Bütçe kısıtı: Kümülatif yatırım ≤ Bütçe
4. Ek kriter: Stratejik uyum, risk, uygulama kolaylığı

Yatırım bütçesi: €100,000
Seçilen projeler (NPV sırasıyla):
1. Hava kaçağı onarımı: €2,000 (NPV: €88,000) → Kümülatif: €2,000
2. Basınç düşürme: €0 (NPV: €54,000) → Kümülatif: €2,000
3. Buhar kapanı değişimi: €5,000 (NPV: €49,000) → Kümülatif: €7,000
4. Kompresör VSD: €18,000 (NPV: €43,000) → Kümülatif: €25,000
5. Economizer: €35,000 (NPV: €39,000) → Kümülatif: €60,000
6. LED aydınlatma: €25,000 (NPV: €26,000) → Kümülatif: €85,000
7. İzolasyon: €8,000 (NPV: €22,000) → Kümülatif: €93,000

Toplam yatırım: €93,000, Toplam NPV: €321,000
```

## 7. Duyarlılık Analizi (Sensitivity Analysis)

### 7.1 Tek Değişken Duyarlılık

```
NPV'nin ana değişkenlere duyarlılığı:

Baz senaryo (Economizer): NPV = €59,152
                          C₀ = €35,000, S = €11,000/yıl, r = %8, n = 15

| Değişken | -20% | Baz | +20% | Duyarlılık |
|----------|------|-----|------|------------|
| Yatırım maliyeti | €66,152 | €59,152 | €52,152 | Orta |
| Yıllık tasarruf | €40,322 | €59,152 | €77,982 | Yüksek |
| İskonto oranı (6.4%-9.6%) | €68,523 | €59,152 | €50,987 | Orta |
| Ekonomik ömür (12-18 yıl) | €49,145 | €59,152 | €67,232 | Düşük-orta |
```

### 7.2 Senaryo Analizi

```
Üç senaryo yaklaşımı:

Kötü senaryo (Pessimistic):
- Yatırım: +%20
- Tasarruf: -%20
- İskonto: %12

Baz senaryo (Base case):
- Yatırım: Tahmin
- Tasarruf: Tahmin
- İskonto: %8

İyi senaryo (Optimistic):
- Yatırım: -%10
- Tasarruf: +%10
- İskonto: %6

| Senaryo | NPV [€] | IRR [%] | SPP [yıl] |
|---------|---------|---------|-----------|
| Kötü | €12,000 | %16 | 4.8 |
| Baz | €59,152 | %30 | 3.2 |
| İyi | €89,000 | %42 | 2.6 |
```

### 7.3 Enerji Fiyat Duyarlılığı

```
Enerji fiyatı etkisi (Ekonomizer örneği):

| Doğalgaz Fiyatı [€/Nm³] | Yıllık Tasarruf [€] | SPP [yıl] | NPV [€] |
|--------------------------|---------------------|-----------|---------|
| 0.30 | 8,000 | 4.4 | €33,500 |
| 0.35 | 9,300 | 3.8 | €44,600 |
| 0.40 | 10,700 | 3.3 | €56,500 |
| 0.45 (baz) | 12,000 | 2.9 | €67,700 |
| 0.50 | 13,300 | 2.6 | €78,800 |
| 0.55 | 14,700 | 2.4 | €90,700 |

Enerji fiyatı %10 artarsa NPV %16 artar → Yüksek duyarlılık
```

## 8. Enerji Performans Sözleşmesi — EPC (Energy Performance Contract)

### 8.1 ESCO Modeli

```
ESCO (Energy Service Company) iş modeli:

1. ESCO yatırımı finanse eder
2. Tasarruf garantisi verir
3. Tasarruftan pay alır (genellikle %70-90, ilk 5-10 yıl)
4. Sözleşme bitiminde tüm tasarruf müşteriye geçer
5. Risk ESCO'da (tasarruf gerçekleşmezse ESCO karşılar)

Tipik EPC yapısı:
- Sözleşme süresi: 5-15 yıl
- Garanti edilen tasarruf: Yıllık €X minimum
- ESCO payı: Gerçekleşen tasarrufun %80-90'ı
- Müşteri payı: Gerçekleşen tasarrufun %10-20'si
- Ölçüm: IPMVP protokolüne göre
```

### 8.2 EPC Ekonomik Değerlendirme

| Parametre | Müşteri Perspektifi | ESCO Perspektifi |
|---|---|---|
| Başlangıç yatırımı | €0 (sıfır) | Tam yatırım |
| Risk | Düşük (garanti var) | Yüksek (garanti vermeli) |
| Getiri (sözleşme dönemi) | Tasarrufın %10-20'si | Tasarrufın %80-90'ı |
| Getiri (sözleşme sonrası) | Tasarrufın %100'ü | %0 |
| NPV (müşteri, 20 yıl) | Genellikle pozitif | — |

## 9. Para Birimi ve Enflasyon Düzeltmesi

### 9.1 Nominal vs. Reel Analiz

```
Reel (sabit fiyatlarla) analiz:
- Nakit akışları bugünkü fiyatlarla
- Reel iskonto oranı kullanılır

Nominal (cari fiyatlarla) analiz:
- Nakit akışları enflasyonlu fiyatlarla
- Nominal iskonto oranı kullanılır

İlişki:
r_reel = (1 + r_nominal) / (1 + π) - 1

Burada:
- π = yıllık enflasyon oranı [oran]

Örnek (Türkiye):
r_nominal = %20, π = %12
r_reel = 1.20 / 1.12 - 1 = %7.14
```

### 9.2 Enerji Fiyat Escalasyon

```
Enerji fiyatlarının genel enflasyonun üzerinde artma eğilimi:

S_yıl_i = S_baz × (1 + e)ⁱ

Burada:
- e = reel enerji fiyat escalasyon oranı
- Tipik: %1-3/yıl (genel enflasyon üzeri)
- Türkiye: %2-5/yıl reel escalasyon (volatil)

Bu etki dikkate alındığında, enerji verimlilik projelerinin
gerçek NPV'si baz hesaplamadan daha yüksek çıkar.
```

## İlgili Dosyalar

- [Yaşam Döngüsü Maliyet](life_cycle_cost.md) — LCC analizi detayları
- [Önceliklendirme](prioritization.md) — Proje önceliklendirme matrisi
- [Enerji Fiyatlandırma](energy_pricing.md) — Tarife yapıları ve maliyetler
- [Ölçüm ve Doğrulama](measurement_verification.md) — IPMVP tasarruf doğrulama
- [Uygulama](implementation.md) — ESCO modelleri ve uygulama stratejileri
- [Metodoloji](methodology.md) — Audit raporlama formatı

## Referanslar

- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- ASHRAE, "Procedures for Commercial Building Energy Audits," 2nd Edition, 2011
- Thumann, A. & Younger, W., "Handbook of Energy Audits," 9th Edition, Fairmont Press, 2012
- Fuller, S.K. & Petersen, S.R., "Life-Cycle Costing Manual for the Federal Energy Management Program," NIST Handbook 135, 1996
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- US DOE, "Guidelines for Techno-Economic Analysis of Energy Technologies"
- European Commission, "Guide to Cost-Benefit Analysis of Investment Projects"
