---
title: "Çözümlü Örnek: Tekstil Fabrikası Termoekonomik Optimizasyonu (Worked Example: Textile Factory Thermoeconomic Optimization)"
category: thermoeconomic_optimization
keywords: [çözümlü örnek, tekstil fabrikası, portföy optimizasyonu, bütçe kısıtı, çok ekipman]
related_files: [knowledge/factory/thermoeconomic_optimization/practical_guide.md, knowledge/factory/thermoeconomic_optimization/iterative_method.md, knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md]
use_when: ["Fabrika seviyesi termoekonomik optimizasyon örneği gerektiğinde", "Bütçe kısıtı altında portföy optimizasyonu yapılırken"]
priority: medium
last_updated: 2026-02-02
---

# Çözümlü Örnek: Tekstil Fabrikası Termoekonomik Optimizasyonu (Worked Example: Textile Factory Thermoeconomic Optimization)

Bu çözümlü örnek, Bursa'da faaliyet gösteren orta ölçekli bir tekstil fabrikasının termoekonomik
optimizasyonunu adım adım gerçekleştirir. SPECO yöntemi kullanılarak exergoekonomik analiz yapılmış,
iteratif yöntemle iyileştirme fırsatları belirlenmiş ve bütçe kısıtı altında portföy optimizasyonu
ile optimal yatırım paketi oluşturulmuştur.

---

## 1. Fabrika Tanımı (Plant Description)

### 1.1. Genel Bilgiler

| Parametre | Değer |
|-----------|-------|
| Sektör | Tekstil (boyama ve terbiye) |
| Konum | Bursa Organize Sanayi Bölgesi |
| Çalışma rejimi | 2 vardiya, 5,500 saat/yıl |
| Yıllık enerji faturası | ~320,000 EUR/yıl |
| Çalışan sayısı | 120 |
| Üretim kapasitesi | 3,000 ton kumaş/yıl |

### 1.2. Ana Ekipmanlar

| Ekipman | Tip | Kapasite | Çalışma Koşulları |
|---------|-----|----------|-------------------|
| Kazan | Doğalgaz, ateş borulu | 2,000 kW (termal) | 8 bar doymuş buhar, 170°C |
| Kompresör | Vidalı, hava soğutmalı | 75 kW (elektrik) | 7 bar, 380 m³/h (FAD) |
| Chiller | Santrifüj, R-134a | 300 kW (soğutma) | 7°C soğuk su, COP = 4.2 |
| Pompa sistemi | Santrifüj (2 adet) | 50 kW (toplam elektrik) | Kazan besleme + proses |

### 1.3. Ekonomik Parametreler (Türkiye, 2024)

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| Doğalgaz fiyatı | 0.038 EUR/kWh | Sanayi, EPDK |
| Elektrik fiyatı | 0.11 EUR/kWh | OG, sanayi |
| Referans ortam sıcaklığı (T₀) | 20°C (293.15 K) | Yıllık ortalama, Bursa |
| Referans basınç (P₀) | 1.013 bar | Deniz seviyesi |
| Reel iskonto oranı (i) | 8% | Endüstriyel |
| Ekonomik ömür (n) | 15 yıl | Tüm ekipmanlar |
| CRF | 0.1168 | CRF = i(1+i)^n / [(1+i)^n - 1] |
| Bakım çarpanı (phi) | 1.06 | Ż = phi x CRF x TCI / tau |

---

## 2. Mevcut Durum: Fabrika Seviyesi Exergy Akış Analizi (Baseline Exergy Flow Analysis)

### 2.1. Enerji ve Exergy Girişleri

Fabrikaya giren toplam enerji ve exergy akışları aşağıda özetlenmiştir.

**Kazan yakıt tüketimi hesabı:**
```
Kazan termal çıktı: Q̇_kazan = 2,000 kW
Kazan verimi (1. yasa): η_kazan = 0.88
Yakıt enerji girişi: Q̇_yakıt = Q̇_kazan / η_kazan = 2,000 / 0.88 = 2,273 kW

Doğalgaz kimyasal exergy / enerji oranı: φ = 1.04
Yakıt exergy girişi: Ėx_yakıt = Q̇_yakıt × φ = 2,273 × 1.04 = 2,364 kW
```

**Elektrik tüketimi:**
```
Kompresör: Ẇ_komp = 75 kW
Chiller: Ẇ_ch = 60 kW (kompresör gücü, COP=4.2 ile Q̇_soğutma = 252 kW)

Not: Chiller nominal soğutma kapasitesi 300 kW fakat mevcut kısmi yük
ortalaması ~%84 ile çalışmaktadır. Gerçek soğutma yükü ~252 kW.

Pompa sistemi: Ẇ_pompa = 50 kW (kazan besleme 30 kW + proses 20 kW)
Toplam elektrik: 75 + 60 + 50 = 185 kW

Elektrik exergy oranı: 1.0 (saf iş)
Ėx_elektrik = 185 kW
```

### 2.2. Fabrika Exergy Akış Tablosu

| Kaynak | Enerji Girişi [kW] | Exergy Girişi [kW] | Birim Maliyet [EUR/kWh] | Maliyet Hızı [EUR/h] |
|--------|---------------------|---------------------|-------------------------|----------------------|
| Doğalgaz (kazan) | 2,273 | 2,364 | 0.0365* | 86.38 |
| Elektrik (kompresör) | 75 | 75 | 0.11 | 8.25 |
| Elektrik (chiller) | 60 | 60 | 0.11 | 6.60 |
| Elektrik (pompa) | 50 | 50 | 0.11 | 5.50 |
| **Toplam** | **2,458** | **2,549** | - | **106.73** |

*Doğalgaz exergy birim maliyeti: c_fuel = 0.038 / 1.04 = 0.0365 EUR/kWh_ex

### 2.3. Faydalı Çıktı Exergysi

| Ürün | Enerji [kW] | Exergy [kW] | Hesaplama |
|------|-------------|-------------|-----------|
| 8 bar doymuş buhar (170°C) | 1,760 | 616 | ṁ × [(h-h₀) - T₀(s-s₀)] |
| Basınçlı hava (7 bar) | - | 28 | ṁ × T₀ × R × ln(P/P₀) |
| Soğuk su (7°C) | 252 | 14.5 | Q̇_soğ × |1 - T₀/T_soğ| (Carnot) |
| Pompalanmış su (basınç artışı) | - | 38 | ṁ × v × ΔP / η_pompa × η_pompa |
| **Toplam faydalı exergy** | - | **696.5** | - |

**Not:** Buhar exergy hesabı:
```
8 bar doymuş buhar: h = 2,769 kJ/kg, s = 6.663 kJ/(kg·K)
Besleme suyu (60°C): h₀_su = 251 kJ/kg, s₀_su = 0.831 kJ/(kg·K)
T₀ = 293.15 K

Buhar debisi: ṁ = Q̇ / (h_buhar - h_su) = 1,760 / (2,769 - 251) = 0.699 kg/s

Exergy artışı (su → buhar):
ex_buhar = (h - h₀) - T₀(s - s₀)  [referans ortam koşullarında]
ex_buhar = (2,769 - 84) - 293.15 × (6.663 - 0.296) = 2,685 - 1,866 = 819 kJ/kg

Ancak besleme suyu zaten 60°C (sıcak):
Ėx_ürün = ṁ × [ex_buhar - ex_besleme_suyu]
ex_besleme(60°C) = (251 - 84) - 293.15 × (0.831 - 0.296) = 167 - 156.8 = 10.2 kJ/kg
Ėx_P_kazan = 0.699 × (819 - 10.2) ≈ 565 kW

Not: Buhar dağıtım kayıpları ile hat boyunca ~8% exergy kaybı:
Ėx_kullanılabilir_buhar ≈ 565 × 0.92 ≈ 520 kW (hat kayıpları dahil kullanım noktası)

Tablo değeri (616 kW) hat kayıpları öncesi kazan çıkışındaki exergy ürünüdür.
```

### 2.4. Fabrika Seviyesi Exergy Verimi

```
ε_fabrika = Ėx_P,toplam / Ėx_F,toplam = 696.5 / 2,549 = 0.273 = %27.3

Tekstil sektörü tipik aralık: %20-30
Bu fabrika sektör ortalamasında yer almaktadır.

Toplam exergy yıkımı: Ėx_D,toplam = 2,549 - 696.5 = 1,852.5 kW
(baca gazı kaybı dahil)
```

---

## 3. Bileşen Bazlı Termoekonomik Analiz (Component-Level Thermoeconomic Analysis)

### 3.1. Bileşen Exergy Analizi

Her bileşenin yakıt (F), ürün (P) ve yıkım (D) exergy değerleri SPECO yöntemine göre:

| Bileşen | Ėx_F [kW] | Ėx_P [kW] | Ėx_D [kW] | Ėx_L [kW] | epsilon_k [%] |
|---------|-----------|-----------|-----------|-----------|---------------|
| Kazan - Yanma odası | 2,364 | 1,420 | 944 | - | 60.1 |
| Kazan - Isı transfer | 1,420 | 616 | 639 | 165* | 43.4** |
| Kompresör | 75 | 28 | 47 | - | 37.3 |
| Chiller | 60 | 14.5 | 45.5 | - | 24.2 |
| Pompa sistemi | 50 | 38 | 12 | - | 76.0 |
| **Toplam** | **2,549** | **696.5** | **1,687.5** | **165** | **27.3** |

*Baca gazı exergy kaybı: Baca gazı sıcaklığı 210°C, Ėx_L = 165 kW
**Isı transfer alt bileşeni: epsilon = Ėx_P / (Ėx_F - Ėx_L) = 616 / (1,420 - 165) = 49.1% (kayıp hariç)
Tablo değeri kayıp dahil: epsilon = 616 / 1,420 = 43.4%

### 3.2. Yatırım Maliyet Hızları (Ż_k)

Ekipman yatırım maliyetlerinin yıllıklaştırılmış değerleri:

```
Ż_k = phi × CRF × TCI_k / tau    [EUR/h]

Burada:
  phi = 1.06 (bakım çarpanı)
  CRF = 0.1168
  tau = 5,500 h/yıl
```

| Bileşen | TCI [EUR] | Ż_k [EUR/h] | Hesaplama |
|---------|-----------|-------------|-----------|
| Kazan (yanma + ısı transfer) | 85,000 | 1.91 | 1.06 × 0.1168 × 85,000 / 5,500 |
| - Yanma odası payı (%15) | 12,750 | 0.29 | Termodinamik ağırlık ile dağıtım |
| - Isı transfer payı (%85) | 72,250 | 1.62 | Yüzey alanı ağırlıklı |
| Kompresör | 42,000 | 0.94 | 1.06 × 0.1168 × 42,000 / 5,500 |
| Chiller | 55,000 | 1.24 | 1.06 × 0.1168 × 55,000 / 5,500 |
| Pompa sistemi | 18,000 | 0.40 | 1.06 × 0.1168 × 18,000 / 5,500 |
| **Toplam** | **200,000** | **4.49** | |

### 3.3. Exergoekonomik Denge ve Birim Maliyetler

SPECO yöntemi ile yakıt birim exergy maliyetleri (c_F) belirlenir:

**Kazan yanma odası:**
```
Yakıt: Doğalgaz kimyasal exergy → c_F = 0.0365 EUR/kWh
Ürün: Yanma gazı exergysi
```

**Kazan ısı transfer:**
```
Yakıt: Yanma gazı exergysi (yanma odasının ürünü)
c_F = (c_F_yanma × Ėx_F_yanma + Ż_yanma) / Ėx_P_yanma
c_F = (0.0365 × 2,364 + 0.29) / 1,420 = 86.57 / 1,420 = 0.0610 EUR/kWh
```

**Kompresör ve Chiller:**
```
Yakıt: Elektrik → c_F = 0.11 EUR/kWh
```

**Pompa sistemi:**
```
Yakıt: Elektrik → c_F = 0.11 EUR/kWh
```

### 3.4. Exergy Yıkım Maliyet Hızı (Ċ_D,k)

```
Ċ_D,k = c_F,k × Ėx_D,k    [EUR/h]
```

| Bileşen | c_F,k [EUR/kWh] | Ėx_D,k [kW] | Ċ_D,k [EUR/h] |
|---------|-----------------|-------------|---------------|
| Kazan - Yanma | 0.0365 | 944 | 34.46 |
| Kazan - Isı transfer | 0.0610 | 639 | 38.98 |
| Kazan - Baca gazı kayıp | 0.0610 | 165 (Ėx_L) | 10.07 |
| Kompresör | 0.11 | 47 | 5.17 |
| Chiller | 0.11 | 45.5 | 5.01 |
| Pompa sistemi | 0.11 | 12 | 1.32 |
| **Toplam** | - | **1,852.5** | **95.01** |

### 3.5. Termoekonomik Değişkenler Tablosu (Ana Sonuç)

| Bileşen | Ėx_F [kW] | Ėx_P [kW] | Ėx_D [kW] | epsilon_k [%] | Ż_k [EUR/h] | Ċ_D,k [EUR/h] | Ċ_D+Ż [EUR/h] | f_k | r_k |
|---------|-----------|-----------|-----------|---------------|-------------|---------------|---------------|-----|-----|
| Kazan - Yanma | 2,364 | 1,420 | 944 | 60.1 | 0.29 | 34.46 | 34.75 | 0.008 | 0.67 |
| Kazan - Isı transfer | 1,420 | 616 | 639+165L | 43.4 | 1.62 | 49.05* | 50.67 | 0.032 | 0.92 |
| Kompresör | 75 | 28 | 47 | 37.3 | 0.94 | 5.17 | 6.11 | 0.154 | 1.68 |
| Chiller | 60 | 14.5 | 45.5 | 24.2 | 1.24 | 5.01 | 6.25 | 0.198 | 3.14 |
| Pompa sistemi | 50 | 38 | 12 | 76.0 | 0.40 | 1.32 | 1.72 | 0.233 | 0.32 |
| **Toplam** | **2,549** | **696.5** | **1,852.5** | **27.3** | **4.49** | **95.01** | **99.50** | - | - |

*Isı transfer Ċ_D dahil baca gazı kaybı: 38.98 + 10.07 = 49.05 EUR/h

### 3.6. Sonuçların Yorumlanması

**Ċ_D+Ż sıralaması (optimizasyon önceliği):**
1. **Kazan - Isı transfer:** 50.67 EUR/h -- En yüksek toplam maliyet etkisi
2. **Kazan - Yanma:** 34.75 EUR/h -- Yanma tersinmezliği baskın
3. **Chiller:** 6.25 EUR/h -- Düşük COP etkisi
4. **Kompresör:** 6.11 EUR/h -- Sıkıştırma verimsizliği
5. **Pompa:** 1.72 EUR/h -- En düşük öncelik

**f_k yorumları:**

| Bileşen | f_k | Yorum |
|---------|-----|-------|
| Kazan - Yanma | 0.008 | Neredeyse tamamen exergy yıkım maliyeti baskın. Yanma tersinmezliğinin ~%60-70'i kaçınılamazdır (unavoidable). Ancak fazla hava (excess air) optimizasyonu ile kaçınılabilir kısım azaltılabilir. |
| Kazan - Isı transfer | 0.032 | Exergy yıkım maliyeti baskın. Baca gazı sıcaklığı 210°C ile önemli kayıp. Economizer eklenerek baca gazı exergy kaybı azaltılabilir. |
| Kompresör | 0.154 | Exergy yıkım ağırlıklı. Basınç optimizasyonu, VSD ve kaçak giderme ile iyileştirme potansiyeli yüksek. |
| Chiller | 0.198 | Exergy yıkım baskın ama yatırım payı artmaya başlıyor. Kondenser temizliği ve kısmi yük VSD ile verim artırılabilir. |
| Pompa | 0.233 | f_k en yüksek ama toplam etki düşük. VSD retrofit ekonomik olabilir. |

**r_k yorumları:**

| Bileşen | r_k | Yorum |
|---------|-----|-------|
| Kazan - Yanma | 0.67 | Tekstil sektörü için tipik aralıkta (0.30-0.80). |
| Kazan - Isı transfer | 0.92 | Yüksek -- baca gazı kaybı ve sıcaklık farkı tersinmezliği. |
| Kompresör | 1.68 | Yüksek -- izentropik verim düşük (~%70) ve mekanik kayıplar. |
| Chiller | 3.14 | Çok yüksek -- soğutma exergysi doğası gereği düşük, maliyet artışı kaçınılmaz fakat COP iyileştirmesi ile azaltılabilir. |
| Pompa | 0.32 | Normal aralıkta -- pompa sistemi göreceli verimli. |

---

## 4. İyileştirme Fırsatları Belirleme (Improvement Opportunity Identification)

### 4.1. İteratif Yöntem Karar Matrisi

f_k ve r_k değerlerine göre her bileşen için iyileştirme yönü:

| Bileşen | f_k | r_k | Karar | İyileştirme Yönü |
|---------|-----|-----|-------|-----------------|
| Kazan - Yanma | 0.008 (cok dusuk) | 0.67 | Verimlilik artır | Fazla hava optimizasyonu (%25 → %15) |
| Kazan - Isı transfer | 0.032 (dusuk) | 0.92 (yuksek) | Verimlilik artır | Economizer, baca gazı T↓ |
| Kompresör | 0.154 (dusuk) | 1.68 (yuksek) | Verimlilik artır | VSD, basınç düşürme, kaçak giderme |
| Chiller | 0.198 (dusuk) | 3.14 (cok yuksek) | Verimlilik artır | Kondenser bakım, VSD, serbest soğutma |
| Pompa | 0.233 (dusuk-orta) | 0.32 (normal) | Verimlilik artır (küçük etki) | VSD retrofit |

**Genel gözlem:** Tüm bileşenlerde f_k < 0.25, yani exergy yıkım maliyeti baskın.
Bu, verimlilik artırıcı yatırımların ekonomik olarak haklı olduğunu gösterir.

### 4.2. Belirlenen Proje Listesi

| No | Proje | Hedef Bileşen | Tür |
|----|-------|---------------|-----|
| P1 | Kompresör basınç düşürme (7 → 6.5 bar) | Kompresör | Quick Win |
| P2 | Kazan fazla hava optimizasyonu (O₂ kontrol) | Kazan - Yanma | Quick Win |
| P3 | Kompresör kaçak giderme programı | Kompresör | Quick Win |
| P4 | Economizer ekleme (baca gazı ısı geri kazanım) | Kazan - Isı transfer | Parametrik |
| P5 | Kompresör VSD retrofit | Kompresör | Parametrik |
| P6 | Pompa VSD retrofit | Pompa | Parametrik |
| P7 | Chiller kondenser ısı geri kazanımı (kazan besleme suyu) | Chiller + Kazan | Yapısal |
| P8 | Kompresör atık ısı geri kazanımı (sıcak su) | Kompresör + Kazan | Yapısal |

---

## 5. Üç Fazlı Optimizasyon Stratejisi (Three-Phase Optimization Strategy)

### Faz 1: Hızlı Kazanımlar (Quick Wins) -- Yatırım < 6,000 EUR

#### P1: Kompresör Basınç Düşürme (7 → 6.5 bar)

```
Mevcut: 7 bar, Ẇ = 75 kW
Proses gerçek ihtiyaç: 6 bar (regülatör sonrası)
0.5 bar fazla basınç, hat kayıpları için yeterli

Güç tasarrufu hesabı (politropik):
Ẇ_yeni / Ẇ_eski = [(P₂_yeni/P₁)^((n-1)/n) - 1] / [(P₂_eski/P₁)^((n-1)/n) - 1]
n = 1.35 (politropik üs, vidalı kompresör)

Ẇ_yeni / 75 = [(6.5/1.013)^(0.259) - 1] / [(7/1.013)^(0.259) - 1]
Ẇ_yeni / 75 = [1.595 - 1] / [1.636 - 1] = 0.595 / 0.636 = 0.936
Ẇ_yeni = 70.2 kW
ΔẆ = 75 - 70.2 = 4.8 kW → ~%6.4 azalma

Yıllık tasarruf: 4.8 × 5,500 × 0.11 = 2,904 EUR/yıl ≈ 2,900 EUR/yıl
Yatırım: ~500 EUR (basınç ayarı, regülatör kontrolü)
SPP: 500 / 2,900 = 0.17 yıl (~2 ay)
```

#### P2: Kazan Fazla Hava Optimizasyonu (%25 → %15)

```
Mevcut fazla hava: %25 (O₂ ≈ %4.3)
Hedef fazla hava: %15 (O₂ ≈ %2.8)

Baca gazı kayıp azalması (Siegert formülü yaklaşımı):
q_baca = (T_baca - T_ortam) × (A₂/(CO₂%) + B)

Mevcut: q_baca = (210 - 20) × (0.66/9.5 + 0.009) = 190 × 0.0785 = 14.9%
Hedef: q_baca = (205 - 20) × (0.66/10.8 + 0.009) = 185 × 0.0701 = 13.0%

Verim artışı: Δη ≈ 1.9 puan → 88.0% → 89.9%
Yakıt tasarrufu: 2,273 × (1 - 88.0/89.9) = 2,273 × 0.0211 = 48.0 kW

Yıllık tasarruf: 48.0 × 5,500 × 0.038 = 10,032 EUR/yıl ≈ 10,000 EUR/yıl
Yatırım: ~3,000 EUR (O₂ analizörü + trim kontrol)
SPP: 3,000 / 10,000 = 0.30 yıl (~3.6 ay)
```

#### P3: Kompresör Kaçak Giderme

```
Tipik tekstil fabrikası basınçlı hava kaçak oranı: %20-30
Mevcut tahmini kaçak: %25

Ultrasonik kaçak tespiti + onarım ile hedef: %10
Kaçak azalması: %25 - %10 = %15 puan

Güç tasarrufu: 75 × 0.15 × 0.80 (yük faktörü) = 9.0 kW
Yıllık tasarruf: 9.0 × 5,500 × 0.11 = 5,445 EUR/yıl ≈ 5,400 EUR/yıl

Not: Kaçak giderme etkisi P1 ile sinerji yapar, ancak burada bağımsız hesaplanmıştır.
Gerçekte P1 sonrası kaçak kayıpları da azalır (düşük basınçta daha az kaçak).

Yatırım: ~2,000 EUR (ultrasonik tespit + onarım malzemesi)
SPP: 2,000 / 5,400 = 0.37 yıl (~4.4 ay)
```

#### Faz 1 Toplam

| Proje | Yatırım [EUR] | Tasarruf [EUR/yıl] | SPP [yıl] |
|-------|--------------|-------------------|-----------|
| P1 - Basınç düşürme | 500 | 2,900 | 0.17 |
| P2 - Fazla hava opt. | 3,000 | 10,000 | 0.30 |
| P3 - Kaçak giderme | 2,000 | 5,400 | 0.37 |
| **Faz 1 Toplam** | **5,500** | **18,300** | **0.30** |

---

### Faz 2: Parametrik Optimizasyon -- Yatırım 31,000 EUR

#### P4: Economizer Ekleme (Baca Gazı Isı Geri Kazanımı)

```
Baca gazı mevcut çıkış sıcaklığı: 210°C
Economizer sonrası hedef: 130°C (asit çiğ noktası 120°C üzeri güvenli)

Geri kazanılabilir ısı:
Q̇_eco = ṁ_baca × cp_baca × (T_in - T_out)
ṁ_baca ≈ 0.95 kg/s (doğalgaz, %15 fazla hava sonrası)
cp_baca ≈ 1.08 kJ/(kg·K)

Q̇_eco = 0.95 × 1.08 × (210 - 130) = 82.1 kW

Kazan besleme suyu ön ısıtma:
T_su_giriş: 60°C → ~95°C (economizer çıkışı)

Yakıt tasarrufu: Q̇_eco / η_kazan_yeni = 82.1 / 0.90 ≈ 91.2 kW yakıt tasarrufu
Yeni kazan verimi: ~93.5% (LHV bazlı)

Yıllık tasarruf: 91.2 × 5,500 × 0.038 = 19,061 EUR/yıl ≈ 19,000 EUR/yıl

Economizer boyutlandırma:
LMTD ≈ [(210-95) - (130-60)] / ln[(210-95)/(130-60)] = [115 - 70] / ln(115/70)
LMTD = 45 / ln(1.643) = 45 / 0.497 = 90.5°C
U ≈ 25 W/(m²·K) (gaz tarafı kontrollü)
A = Q̇ / (U × LMTD) = 82,100 / (25 × 90.5) = 36.3 m² → 40 m² seçilir

Yatırım: ~18,000 EUR (40 m² paslanmaz çelik economizer, montaj dahil)
SPP: 18,000 / 19,000 = 0.95 yıl
```

#### P5: Kompresör VSD Retrofit

```
Mevcut çalışma: Yük/boşta kontrol, ortalama yük %80
VSD ile güç azalması (kübik yasa yaklaşımı):

Mevcut ortalama güç (yük/boşta):
Ẇ_mevcut = 75 × [0.80 + 0.20 × 0.25] = 75 × 0.85 = 63.8 kW

Not: P1 ve P3 sonrası yeni koşullar:
Ẇ_P1_P3_sonrası = (75 - 4.8 - 9.0) × 0.85 = 52.0 kW (yük/boşta)

VSD ile (P1 ve P3 sonrası bazda):
Ẇ_VSD = (75 - 4.8 - 9.0) × 0.80 × (0.80)^0.8 ≈ 61.2 × 0.80 × 0.842 = 41.2 kW

Not: VSD ile boşta çalışma elimine edilir ve kısmi yük verimi artar.
Gerçekçi tasarruf: 52.0 - 41.2 = 10.8 kW

Yıllık tasarruf: 10.8 × 5,500 × 0.11 = 6,534 EUR/yıl ≈ 6,500 EUR/yıl
Yatırım: ~8,000 EUR (75 kW VSD + montaj)
SPP: 8,000 / 6,500 = 1.23 yıl
```

#### P6: Pompa VSD Retrofit

```
Mevcut: 50 kW toplam, vana kontrolü ile debi ayarı
Ortalama yük faktörü: ~%75

Mevcut güç (vana kontrol): Ẇ ≈ 50 × 0.90 = 45 kW (vana ile güç düşüşü az)
VSD ile: Ẇ_VSD = 50 × (0.75)³ × 1.05 = 50 × 0.422 × 1.05 = 22.2 kW
(1.05 = VSD kayıp çarpanı)

Tasarruf: 45 - 22.2 = 22.8 kW

Not: Gerçekçi düzeltme -- affinite yasaları tam kübik ilişki sadece sürtünme
baskın sistemlerde geçerlidir. Statik basınç bileşeni ile düzeltme:
Statik basınç payı: ~%30 (kazan besleme)
Düzeltilmiş tasarruf: 22.8 × 0.65 = 14.8 kW → ~15 kW

Yıllık tasarruf: 15 × 5,500 × 0.11 = 9,075 EUR/yıl ≈ 9,000 EUR/yıl
Yatırım: ~5,000 EUR (2 × 25 kW VSD + montaj)
SPP: 5,000 / 9,000 = 0.56 yıl
```

#### Faz 2 Toplam

| Proje | Yatırım [EUR] | Tasarruf [EUR/yıl] | SPP [yıl] |
|-------|--------------|-------------------|-----------|
| P4 - Economizer | 18,000 | 19,000 | 0.95 |
| P5 - Kompresör VSD | 8,000 | 6,500 | 1.23 |
| P6 - Pompa VSD | 5,000 | 9,000 | 0.56 |
| **Faz 2 Toplam** | **31,000** | **34,500** | **0.90** |

---

### Faz 3: Yapısal Değişiklikler (Structural Changes) -- Yatırım 27,000 EUR

#### P7: Chiller Kondenser Isı Geri Kazanımı (Cross-Equipment)

```
Chiller kondenser atık ısısı:
Q̇_kond = Q̇_soğutma + Ẇ_kompresör = 252 + 60 = 312 kW
Kondenser sıcaklığı: ~38°C (hava soğutmalı)

Kazan besleme suyu ön ısıtma potansiyeli:
T_su_giriş: 20°C → 32°C (kondenser ile)
Not: Economizer zaten 60°C→95°C ısıtıyor; bu proje ek ön ısıtma sağlar.

Geri kazanılabilir ısı (su tarafı):
Besleme suyu debisi: ṁ_su = 0.699 kg/s
Q̇_geri = ṁ_su × cp × ΔT = 0.699 × 4.18 × (32 - 20) = 35.1 kW

Yakıt tasarrufu: 35.1 / 0.90 = 39.0 kW
Yıllık tasarruf: 39.0 × 5,500 × 0.038 = 8,151 EUR/yıl ≈ 8,000 EUR/yıl

Not: Soğutma sezonunda (Mayıs-Ekim, ~3,000 saat) tam kapasite,
kışın (Kasım-Nisan, ~2,500 saat) kısmi → ağırlıklı ortalama etki ~%70

Düzeltilmiş tasarruf: 8,000 × 0.70 = 5,600 EUR/yıl ≈ 5,500 EUR/yıl

Yatırım: ~12,000 EUR (plakalı HX + boru hattı + kontrol)
SPP: 12,000 / 5,500 = 2.18 yıl
```

#### P8: Kompresör Atık Isı Geri Kazanımı (Cross-Equipment)

```
Kompresör atık ısı potansiyeli (hava soğutmalı):
Q̇_atık = Ẇ × 0.60 = 75 × 0.60 = 45 kW (geri kazanılabilir, hava soğutmalı tip)

Not: P1, P3, P5 sonrası kompresör gücü azalmış olacak.
Düzeltilmiş güç: ~41 kW → Q̇_atık = 41 × 0.60 = 24.6 kW

Sıcak su üretimi: 50°C → 70°C (proses yıkama suyu, mutfak)
Sıcak su ihtiyacı: ~30 kW (yeterli)

Doğalgaz tasarrufu (mevcut boyler yerine):
Yıllık tasarruf: 24.6 × 5,500 × 0.038 = 5,141 EUR/yıl

Gerçekçi düzeltme (eş zamanlılık %80):
Düzeltilmiş tasarruf: 5,141 × 0.80 = 4,113 EUR/yıl ≈ 4,000 EUR/yıl

Ek etki: Kompresör soğutma yükü azalır → kompresör ömrü uzar

Yatırım: ~15,000 EUR (ısı geri kazanım ünitesi + boru + HX + kontrol)
SPP: 15,000 / 4,000 = 3.75 yıl
```

#### Faz 3 Toplam

| Proje | Yatırım [EUR] | Tasarruf [EUR/yıl] | SPP [yıl] |
|-------|--------------|-------------------|-----------|
| P7 - Chiller HRR | 12,000 | 5,500 | 2.18 |
| P8 - Kompresör HRR | 15,000 | 4,000 | 3.75 |
| **Faz 3 Toplam** | **27,000** | **9,500** | **2.84** |

---

## 6. Önce/Sonra Karşılaştırma (Before/After Comparison)

### 6.1. Aşamalı İyileştirme Tablosu

| Metrik | Mevcut | Faz 1 Sonrası | Faz 1+2 Sonrası | Tüm Fazlar |
|--------|--------|--------------|-----------------|------------|
| Toplam yakıt girişi [kW] | 2,273 | 2,225 | 2,134 | 2,070 |
| Toplam elektrik [kW] | 185 | 171 | 127 | 127 |
| Toplam exergy girişi [kW] | 2,549 | 2,489 | 2,363 | 2,281 |
| Faydalı exergy çıktı [kW] | 696.5 | 696.5 | 696.5 | 696.5 |
| Exergy yıkımı [kW] | 1,852.5 | 1,792.5 | 1,666.5 | 1,584.5 |
| Fabrika exergy verimi [%] | 27.3 | 28.0 | 29.5 | 30.5 |
| Yıllık enerji maliyeti [EUR/yıl] | 320,000 | 302,000 | 268,000 | 258,000 |
| Exergy yıkım maliyeti [EUR/h] | 95.01 | 88.35 | 74.80 | 69.50 |
| CO₂ emisyonu [ton/yıl] | 1,850 | 1,795 | 1,680 | 1,620 |

### 6.2. Kümülatif Yatırım ve Getiri

| Faz | Kümülatif Yatırım [EUR] | Kümülatif Tasarruf [EUR/yıl] | Kümülatif SPP [yıl] |
|-----|------------------------|-----------------------------|--------------------|
| Faz 1 | 5,500 | 18,300 | 0.30 |
| Faz 1+2 | 36,500 | 52,800 | 0.69 |
| Tüm Fazlar | 63,500 | 62,300 | 1.02 |

### 6.3. CO₂ Azaltma Detayı

```
Mevcut CO₂ emisyonu:
  Doğalgaz: 2,273 × 5,500 × 0.000202 = 2,525 tCO₂/yıl (0.202 kgCO₂/kWh)
  Elektrik: 185 × 5,500 × 0.000440 = 448 tCO₂/yıl (0.44 kgCO₂/kWh şebeke)

Not: Tablo yukarıda toplam 1,850 ton göstermektedir -- bu doğalgaz kaynaklı
ana emisyondur. Elektrik dahil toplam: ~2,973 tCO₂/yıl.

Tüm fazlar sonrası:
  Doğalgaz: 2,070 × 5,500 × 0.000202 = 2,300 tCO₂/yıl
  Elektrik: 127 × 5,500 × 0.000440 = 307 tCO₂/yıl
  Toplam: 2,607 tCO₂/yıl

CO₂ azaltma: 2,973 - 2,607 = 366 tCO₂/yıl (~%12.3 azalma)
```

---

## 7. Bütçe Kısıtı Altında Portföy Optimizasyonu (Budget-Constrained Portfolio Optimization)

### 7.1. Problem Tanımı

Fabrika yönetimi, termoekonomik analiz sonuçlarına dayanarak iyileştirme yatırımlarını
planlamaktadır. Ancak cari yıl için kullanılabilir yatırım bütçesi **40,000 EUR** ile sınırlıdır.

**Soru:** Hangi proje kombinasyonu, 40,000 EUR bütçe kısıtı altında maksimum NPV sağlar?

### 7.2. Proje Verileri (NPV Hesaplı)

NPV hesabı: NPV = -I + S × [((1+i)^n - 1) / (i × (1+i)^n)]
Burada i = 0.08, n = 15 yıl, annuity factor = 8.559

| Proje | I [EUR] | S [EUR/yıl] | NPV [EUR] | SPP [yıl] | IRR [%] |
|-------|---------|-------------|-----------|-----------|---------|
| P1 - Basınç düşürme | 500 | 2,900 | 24,322 | 0.17 | >100 |
| P2 - Fazla hava opt. | 3,000 | 10,000 | 82,590 | 0.30 | >100 |
| P3 - Kaçak giderme | 2,000 | 5,400 | 44,218 | 0.37 | >100 |
| P4 - Economizer | 18,000 | 19,000 | 144,621 | 0.95 | >100 |
| P5 - Kompresör VSD | 8,000 | 6,500 | 47,634 | 1.23 | 81 |
| P6 - Pompa VSD | 5,000 | 9,000 | 72,031 | 0.56 | >100 |
| P7 - Chiller HRR | 12,000 | 5,500 | 35,075 | 2.18 | 45 |
| P8 - Kompresör HRR | 15,000 | 4,000 | 19,236 | 3.75 | 25 |
| **Tümü** | **63,500** | **62,300** | **469,727** | **1.02** | - |

### 7.3. Knapsack Formülasyonu

```
Amaç: max Σ (NPV_j × x_j)
Kısıt: Σ (I_j × x_j) ≤ B = 40,000 EUR
       x_j ∈ {0, 1}  (her proje ya seçilir ya seçilmez)
       j = 1, 2, ..., 8

Bağımlılık kısıtları:
  - P5 (VSD kompresör) bağımsız uygulanabilir
  - P7 (Chiller HRR) bağımsız uygulanabilir
  - P8 (Kompresör HRR), P5 ile birlikte uygulanırsa daha verimli (opsiyonel sinerji)
```

### 7.4. Greedy Yöntem (SPP Sıralaması ile)

SPP sırasına göre seçim (en kısa geri ödeme önce):

| Sıra | Proje | I [EUR] | Kümülatif I [EUR] | Bütçe Kalan [EUR] | Karar |
|------|-------|---------|-------------------|--------------------|-------|
| 1 | P1 (SPP=0.17) | 500 | 500 | 39,500 | SECILDI |
| 2 | P2 (SPP=0.30) | 3,000 | 3,500 | 36,500 | SECILDI |
| 3 | P3 (SPP=0.37) | 2,000 | 5,500 | 34,500 | SECILDI |
| 4 | P6 (SPP=0.56) | 5,000 | 10,500 | 29,500 | SECILDI |
| 5 | P4 (SPP=0.95) | 18,000 | 28,500 | 11,500 | SECILDI |
| 6 | P5 (SPP=1.23) | 8,000 | 36,500 | 3,500 | SECILDI |
| 7 | P7 (SPP=2.18) | 12,000 | - | 3,500 < 12,000 | REDDEDILDI |
| 8 | P8 (SPP=3.75) | 15,000 | - | 3,500 < 15,000 | REDDEDILDI |

**Greedy sonuç:** P1+P2+P3+P4+P5+P6 = 36,500 EUR yatırım, NPV = 415,416 EUR

### 7.5. Optimal Çözüm (Tam Enumeration)

40,000 EUR bütçe ile tüm olası kombinasyonlar incelendiğinde:

| Senaryo | Projeler | Toplam I [EUR] | Toplam NPV [EUR] |
|---------|----------|---------------|-------------------|
| Greedy | P1+P2+P3+P4+P5+P6 | 36,500 | 415,416 |
| Alt. 1 | P1+P2+P3+P4+P6+P7 | 40,000 | 402,857 |
| Alt. 2 | P1+P2+P3+P4+P5+P8 | 46,500 | Bütçe aşımı |
| Alt. 3 | P1+P2+P3+P6+P7 | 22,000 | 258,236 |

**Optimal senaryo: Greedy seçim (P1+P2+P3+P4+P5+P6)**

Bu durumda greedy (SPP sıralaması) ve NPV optimali aynı portföyü vermektedir.
Bunun nedeni, yüksek NPV'li projelerin aynı zamanda kısa SPP'ye sahip olmasıdır.

**Not:** Kalan 3,500 EUR, Faz 3 projelerinden hiçbirini karşılayamaz.
Bir sonraki yıl bütçesiyle P7 (12,000 EUR) öncelikli değerlendirilmelidir.

### 7.6. Greedy vs Optimal Karşılaştırma

```
Bu örnekte greedy ve optimal çözüm çakışmaktadır. Ancak genel olarak greedy
yöntem her zaman optimal değildir. Karşı örnek durumları:

- Büyük NPV'li ancak uzun SPP'li bir proje, greedy ile atlanabilir
- Küçük yatırımlı düşük NPV projeleri bütçeyi erken doldurarak,
  büyük NPV projelerine yer bırakmayabilir

Knapsack problemi NP-hard olmasına rağmen, 8 proje ile tam enumeration
(2^8 = 256 kombinasyon) pratik sürede çözülebilir.

Büyük portföylerde (>20 proje): Dinamik programlama veya MILP kullanılmalıdır.
```

---

## 8. Duyarlılık Analizi (Sensitivity Analysis)

### 8.1. Enerji Fiyatı Duyarlılığı (+-30%)

Greedy portföy (P1-P6) için toplam yıllık tasarruf duyarlılığı:

| Senaryo | Doğalgaz [EUR/kWh] | Elektrik [EUR/kWh] | Yıllık Tasarruf [EUR/yıl] | NPV [EUR] | SPP [yıl] |
|---------|-------------------|--------------------|-----------------------------|-----------|-----------|
| Düşük (-30%) | 0.027 | 0.077 | 37,100 | 281,100 | 0.98 |
| Baz | 0.038 | 0.110 | 52,800 | 415,416 | 0.69 |
| Yüksek (+30%) | 0.049 | 0.143 | 68,700 | 551,400 | 0.53 |

**Yorum:** Enerji fiyatları %30 düşse bile, portföy NPV'si 281,100 EUR ile güçlü pozitif
kalır ve SPP < 1 yıl. Yatırım kararı enerji fiyat dalgalanmalarına karşı dayanıklıdır (robust).

### 8.2. İskonto Oranı Duyarlılığı

| İskonto Oranı [%] | Annuity Factor | Portföy NPV [EUR] | Değişim |
|--------------------|---------------|-------------------|---------|
| 6 | 9.712 | 476,200 | +14.6% |
| 8 (baz) | 8.559 | 415,416 | - |
| 10 | 7.606 | 365,100 | -12.1% |
| 12 | 6.811 | 323,300 | -22.2% |

**Yorum:** İskonto oranı %12'ye çıksa bile NPV > 323,000 EUR. Yatırımlar tüm
finansman senaryolarında ekonomik olarak haklıdır.

### 8.3. Çalışma Saati Duyarlılığı

| Çalışma Saati [h/yıl] | Yıllık Tasarruf [EUR/yıl] | SPP [yıl] | NPV [EUR] |
|------------------------|---------------------------|-----------|-----------|
| 4,000 (1.5 vardiya) | 38,400 | 0.95 | 292,300 |
| 5,500 (baz, 2 vardiya) | 52,800 | 0.69 | 415,416 |
| 7,500 (3 vardiya) | 72,000 | 0.51 | 579,900 |

**Yorum:** 3 vardiyaya geçiş halinde NPV %40 artar. Üretim artışı planlanıyorsa
enerji verimliliği yatırımlarının getirisi de orantılı artar.

### 8.4. CBAM Etkisi (Karbon Fiyatı Senaryoları)

Portföyün CO₂ azaltma etkisi: 366 tCO₂/yıl (Bölüm 6.3)

| CBAM Senaryosu | Karbon Fiyatı [EUR/tCO₂] | Ek Tasarruf [EUR/yıl] | Toplam Tasarruf [EUR/yıl] | NPV Artışı [EUR] |
|----------------|--------------------------|----------------------|---------------------------|-------------------|
| Mevcut (yok) | 0 | 0 | 52,800 | - |
| 2026 geçiş | 50 | 18,300 | 71,100 | +156,600 |
| 2030 tam uygulama | 80 | 29,280 | 82,080 | +250,600 |
| 2035 yüksek senaryo | 100 | 36,600 | 89,400 | +313,300 |

**Yorum:** CBAM tam uygulamaya geçtiğinde (80 EUR/tCO₂), enerji verimliliği
yatırımlarının NPV'si %60 artar. Bu, AB'ye ihracat yapan tekstil fabrikaları
için kritik bir rekabet avantajı faktörüdür.

### 8.5. Tornado Diyagramı (Parametrik Etki Sıralaması)

```
NPV üzerindeki parametrelerin etkisi (+-30% değişim):

                        ← NPV Azalma    NPV Artış →
                              |              |
Doğalgaz fiyatı        ██████████████████████████████  ±134,300 EUR
Çalışma saati          █████████████████████████████   ±123,500 EUR
Elektrik fiyatı        ████████████████████            ± 85,200 EUR
İskonto oranı          ██████████████                  ± 60,100 EUR
Ekipman maliyeti       ████████                        ± 34,200 EUR
Bakım çarpanı          ██                              ±  8,500 EUR
```

**En etkili parametre:** Doğalgaz fiyatı (kazan dominant sistem).
**Dikkat:** Türkiye'de doğalgaz fiyatı devlet tarafından düzenlenmektedir;
ani artışlar NPV'yi olumlu etkiler (tasarruf artar).

---

## 9. Sonuçlar ve Yol Haritası (Conclusions and Roadmap)

### 9.1. Termoekonomik Analiz Özeti

Bu çalışmada, Bursa'daki orta ölçekli bir tekstil fabrikasının termoekonomik
optimizasyonu sistematik olarak gerçekleştirilmiştir.

**Temel bulgular:**

1. Fabrika exergy verimi %27.3 ile sektör ortalamasında -- iyileştirme potansiyeli var.
2. Toplam exergy yıkım maliyeti 95.01 EUR/h (yıllık ~522,555 EUR).
3. En büyük maliyet etkisi kazan ısı transfer bölümünde (50.67 EUR/h) --
   baca gazı kaybı ve sıcaklık farkı tersinmezliği baskın.
4. Tüm bileşenlerde f_k < 0.25, exergy yıkım maliyeti baskın --
   verimlilik artırıcı yatırımlar haklıdır.

### 9.2. Optimal Yatırım Portföyü

| Parametre | Değer |
|-----------|-------|
| Seçilen projeler | P1, P2, P3, P4, P5, P6 |
| Toplam yatırım | 36,500 EUR |
| Toplam yıllık tasarruf | 52,800 EUR/yıl |
| Toplam SPP | 0.69 yıl |
| NPV (15 yıl, i=%8) | 415,416 EUR |
| CO₂ azaltma | 366 ton/yıl |
| Exergy verimi artışı | %27.3 → %29.5 |

### 9.3. Uygulama Yol Haritası

```
Ay 1-2: FAZ 1 — Quick Wins
  ├─ P1: Kompresör basınç ayarı (1 gün)
  ├─ P2: O₂ analizörü kurulumu + kalibrasyon (2 hafta)
  └─ P3: Ultrasonik kaçak tespiti + onarım (1 hafta)
  Beklenen etki: 18,300 EUR/yıl, %5.7 enerji maliyeti azalma

Ay 3-6: FAZ 2 — Parametrik İyileştirmeler
  ├─ P4: Economizer sipariş + montaj (6-8 hafta)
  ├─ P5: Kompresör VSD montajı (1 hafta)
  └─ P6: Pompa VSD montajı (1 hafta)
  Beklenen etki: +34,500 EUR/yıl, toplam %16.5 azalma

Ay 12-18: FAZ 3 — Yapısal Değişiklikler (gelecek yıl bütçesi)
  ├─ P7: Chiller HRR (4 hafta mühendislik + 2 hafta montaj)
  └─ P8: Kompresör HRR (4 hafta mühendislik + 2 hafta montaj)
  Beklenen etki: +9,500 EUR/yıl, toplam %19.5 azalma
```

### 9.4. Nihai Durum Özeti

| Metrik | Mevcut | Hedef (Tüm Fazlar) | İyileşme |
|--------|--------|---------------------|----------|
| Fabrika exergy verimi | %27.3 | %30.5 | +3.2 puan |
| Yıllık enerji maliyeti | 320,000 EUR | 258,000 EUR | -62,000 EUR (%19.4) |
| Exergy yıkım maliyet hızı | 95.01 EUR/h | 69.50 EUR/h | -25.51 EUR/h (%26.9) |
| CO₂ emisyonu | 2,973 ton/yıl | 2,607 ton/yıl | -366 ton (%12.3) |
| Toplam yatırım | - | 63,500 EUR | - |
| NPV (15 yıl) | - | ~470,000 EUR | - |
| Aggregate SPP | - | 1.02 yıl | - |

### 9.5. Öneriler

1. **Faz 1 derhal başlatılmalıdır.** 5,500 EUR yatırım ile 18,300 EUR/yıl tasarruf,
   risk neredeyse sıfır.

2. **Faz 2 için teklif süreci 1. ayda başlatılmalıdır.** Economizer tedarik süresi
   6-8 hafta olabilir.

3. **CBAM hazırlığı yapılmalıdır.** AB'ye ihracat yapılıyorsa, karbon ayak izi
   raporlaması başlatılmalı ve enerji verimliliği yatırımları CBAM kredisi
   olarak değerlendirilmelidir.

4. **Yıllık takip analizi yapılmalıdır.** Uygulama sonrası ölçüm ve doğrulama
   (M&V) ile gerçekleşen tasarruflar karşılaştırılmalıdır.

5. **Dijital ikiz entegrasyonu değerlendirilmelidir.** ExergyLab platformu ile
   sürekli exergoekonomik izleme, ek optimizasyon fırsatlarını ortaya çıkarabilir.

---

## İlgili Dosyalar

- `knowledge/factory/thermoeconomic_optimization/overview.md` -- Termoekonomik analiz temelleri
- `knowledge/factory/thermoeconomic_optimization/objective_functions.md` -- Maliyet fonksiyonları
- `knowledge/factory/thermoeconomic_optimization/iterative_method.md` -- İteratif optimizasyon yöntemi
- `knowledge/factory/thermoeconomic_optimization/practical_guide.md` -- Uygulama rehberi
- `knowledge/factory/thermoeconomic_optimization/multi_objective.md` -- Çok amaçlı optimizasyon
- `knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md` -- Duyarlılık analizi
- `knowledge/factory/cross_equipment.md` -- Ekipmanlar arası fırsatlar
- `knowledge/factory/prioritization.md` -- Önceliklendirme yöntemi
- `knowledge/factory/economic_analysis.md` -- Ekonomik analiz
- `knowledge/factory/case_studies.md` -- Endüstriyel vaka çalışmaları

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
- Lazzaretto, A. & Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs." *Energy*, 31(8-9), 1257-1289.
- Morosuk, T. & Tsatsaronis, G. (2019). "Advanced exergy-based methods used to understand and improve energy-conversion systems." *Energy*, 169, 238-246.
- El-Sayed, Y.M. (2003). *The Thermoeconomics of Energy Conversions*. Elsevier.
- Utlu, Z. & Hepbasli, A. (2007). "A review on analyzing and evaluating the energy utilization efficiency of countries." *Renewable and Sustainable Energy Reviews*, 11(1), 1-29.
- Rosen, M.A. & Dincer, I. (2003). "Thermoeconomic analysis of power plants: an application to a coal fired electrical generating station." *Energy Conversion and Management*, 44(17), 2743-2761.
- EPDK (2024). Doğalgaz ve elektrik sanayi tarifeleri. https://www.epdk.gov.tr
- Türkiye Enerji Verimliliği Strateji Belgesi (2012/1).
- ISO 50001:2018 -- Energy Management Systems.
