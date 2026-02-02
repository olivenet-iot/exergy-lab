---
title: "Amaç Fonksiyonları (Objective Functions)"
category: thermoeconomic_optimization
keywords: [amaç fonksiyonu, maliyet modeli, yakıt maliyeti, yatırım maliyeti, CBAM, ekipman maliyet korelasyonu]
related_files: [knowledge/factory/thermoeconomic_optimization/overview.md, knowledge/factory/thermoeconomic_optimization/decision_variables.md, knowledge/factory/thermoeconomic_optimization/multi_objective.md]
use_when: ["Termoekonomik optimizasyon maliyet formülasyonu gerektiğinde", "Ekipman maliyet korelasyonları sorulduğunda"]
priority: high
last_updated: 2026-02-02
---

# Amaç Fonksiyonları (Objective Functions)

## 1. Genel Formülasyon

Termoekonomik optimizasyonun temel amacı, toplam yıllıklaştırılmış maliyeti minimize etmektir:

```
min C_total = C_fuel + C_invest + C_O&M + C_env

Burada:
  C_total  = Toplam yıllıklaştırılmış maliyet [€/yıl]
  C_fuel   = Yakıt (enerji) maliyeti [€/yıl]
  C_invest = Yıllıklaştırılmış yatırım maliyeti [€/yıl]
  C_O&M    = İşletme ve bakım maliyeti [€/yıl]
  C_env    = Çevre maliyeti (emisyon) [€/yıl]
```

Bu formülasyon, tüm maliyet bileşenlerini yıllık bazda birleştirerek karşılaştırılabilir kılar.

---

## 2. Yakıt Maliyeti Bileşeni (C_fuel)

### 2.1. Genel Formül

```
C_fuel = Σ (ṁ_fuel,j × LHV_j × c_fuel,j × τ)    [€/yıl]

Burada:
  ṁ_fuel,j = j-inci yakıtın kütle debisi [kg/s]
  LHV_j    = Alt ısıl değer [kJ/kg]
  c_fuel,j = Yakıt birim fiyatı [€/kJ]
  τ        = Yıllık çalışma süresi [s/yıl]
```

Alternatif olarak exergy bazlı:

```
C_fuel = Σ (Ėx_fuel,j × c_ex,fuel,j × τ)    [€/yıl]

Burada:
  Ėx_fuel,j   = j-inci yakıtın exergy akış hızı [kW]
  c_ex,fuel,j  = Exergy bazlı yakıt birim maliyeti [€/kWh]
```

### 2.2. Türkiye Enerji Fiyatları (2024-2025 Referans)

| Enerji Kaynağı | Birim | Fiyat Aralığı | Tipik Değer | Exergy Birim Maliyet |
|----------------|-------|---------------|-------------|---------------------|
| Doğalgaz (sanayi) | €/m³ | 0.30 – 0.45 | 0.38 | 0.037 €/kWh_ex |
| Elektrik (sanayi, OG) | €/kWh | 0.08 – 0.14 | 0.11 | 0.110 €/kWh_ex |
| Elektrik (sanayi, AG) | €/kWh | 0.10 – 0.16 | 0.13 | 0.130 €/kWh_ex |
| LPG (sanayi) | €/kg | 0.80 – 1.10 | 0.95 | 0.073 €/kWh_ex |
| Kömür (taş kömürü) | €/ton | 120 – 180 | 150 | 0.021 €/kWh_ex |
| Kömür (linyit) | €/ton | 40 – 80 | 60 | 0.017 €/kWh_ex |
| Buhar (fabrika içi) | €/ton | 20 – 40 | 30 | Hesaba bağlı |

> **Not:** Türkiye fiyatları TL bazlıdır ve kur dalgalanmalarından etkilenir.
> EUR cinsinden fiyatlar yaklaşıktır. Güncel dönüşüm için EPDK tarifelerini kontrol edin.

### 2.3. Yakıtın Exergy Oranı

| Yakıt | Kimyasal Exergy / LHV |
|-------|----------------------|
| Doğalgaz (CH₄) | 1.04 |
| Propan (C₃H₈) | 1.06 |
| Fuel oil | 1.04 – 1.08 |
| Kömür (bitümlü) | 1.06 – 1.10 |
| Linyit | 1.04 – 1.08 |

---

## 3. Yatırım Maliyeti Bileşeni (C_invest)

### 3.1. Yıllıklaştırma (Capital Recovery Factor)

```
C_invest = CRF × Σ Z_k    [€/yıl]

CRF = i × (1 + i)^n / ((1 + i)^n - 1)

Burada:
  CRF  = Capital Recovery Factor (sermaye geri kazanım faktörü)
  i    = İskonto oranı (reel) [oran]
  n    = Ekonomik ömür [yıl]
  Z_k  = k-inci bileşenin toplam yatırım maliyeti [€]
```

### 3.2. Türkiye İçin İskonto Oranları

| Senaryo | Nominal Oran | Enflasyon | Reel Oran |
|---------|-------------|-----------|-----------|
| İyimser | %15 | %8 | %6.5 |
| Baz durum | %20 | %12 | %7.1 |
| Kötümser | %30 | %20 | %8.3 |
| Uluslararası referans | %8 | %2 | %5.9 |

> **Tavsiye:** Türkiye projeleri için reel iskonto oranı %8-12 aralığında kullanılması
> önerilir. Duyarlılık analizi mutlaka yapılmalıdır.

### 3.3. Ekipman Maliyet Korelasyonları (PEC — Purchased Equipment Cost)

#### Kazan (Steam Boiler)

```
PEC_boiler = a × Q_boiler^b    [EUR, referans yılı 2020]

Q_boiler = Kazan kapasitesi [kW]

Parametreler (doğalgaz, buhar kazanı):
  a = 42.7, b = 0.79    (500 kW < Q < 10,000 kW)
  a = 101,  b = 0.72    (50 kW < Q < 500 kW)

Örnek: 3,000 kW kazan
  PEC = 42.7 × 3000^0.79 = 42.7 × 733.6 ≈ 31.315 EUR
  + Montaj çarpanı (2.5-3.5 × PEC) → TCI ≈ 78.000 - 110.000 EUR
```

#### Kompresör (Air Compressor)

```
PEC_comp = a × Ẇ_comp^b    [EUR, referans yılı 2020]

Ẇ_comp = Kompresör gücü [kW]

Parametreler (vidalı, yağlı):
  a = 535, b = 0.82    (20 kW < Ẇ < 500 kW)

Örnek: 75 kW kompresör
  PEC = 535 × 75^0.82 = 535 × 42.4 ≈ 22.684 EUR
```

#### Chiller (Vapor Compression)

```
PEC_chiller = a × Q_chiller^b    [EUR, referans yılı 2020]

Q_chiller = Soğutma kapasitesi [kW]

Parametreler (santrifüj, su soğutmalı):
  a = 359, b = 0.72    (100 kW < Q < 2,000 kW)

Örnek: 300 kW chiller
  PEC = 359 × 300^0.72 = 359 × 72.4 ≈ 25.992 EUR
```

#### Pompa (Centrifugal Pump)

```
PEC_pump = a × Ẇ_pump^b    [EUR, referans yılı 2020]

Ẇ_pump = Pompa gücü [kW]

Parametreler (santrifüj):
  a = 616, b = 0.72    (1 kW < Ẇ < 200 kW)

Örnek: 50 kW pompa
  PEC = 616 × 50^0.72 = 616 × 19.1 ≈ 11.766 EUR
```

#### Isı Değiştirici (Heat Exchanger)

```
PEC_HX = a × A_HX^b    [EUR, referans yılı 2020]

A_HX = Isı transfer yüzey alanı [m²]

Parametreler (shell-and-tube, karbon çeliği):
  a = 120, b = 0.78    (10 m² < A < 500 m²)

Parametreler (plakalı):
  a = 239, b = 0.72    (1 m² < A < 100 m²)
```

### 3.4. CEPCI Düzeltmesi

```
PEC_güncel = PEC_referans × (CEPCI_güncel / CEPCI_referans)

CEPCI değerleri:
  2020: 596.2
  2021: 708.0
  2022: 816.0
  2023: 797.9
  2024: ~810 (tahmin)
```

### 3.5. Türkiye Çarpanı

Uluslararası maliyet korelasyonlarını Türkiye'ye uyarlamak için:

```
TCI_Türkiye = PEC × f_CEPCI × f_kurulum × f_Türkiye

Burada:
  f_CEPCI    = CEPCI düzeltme faktörü
  f_kurulum  = Toplam kurulum çarpanı (TCI/PEC), tipik 2.5 – 3.5
  f_Türkiye  = Türkiye pazar düzeltmesi, tipik 0.85 – 1.15
               (işçilik ucuz ama ithal ekipman pahalı)
```

| Ekipman Tipi | f_kurulum | f_Türkiye | Toplam Çarpan |
|-------------|-----------|-----------|--------------|
| Kazan (yerli) | 2.5 | 0.85 | 2.13 |
| Kazan (ithal) | 3.0 | 1.10 | 3.30 |
| Kompresör | 2.8 | 1.05 | 2.94 |
| Chiller | 3.0 | 1.10 | 3.30 |
| Pompa (yerli) | 2.5 | 0.85 | 2.13 |
| Isı değiştirici (yerli) | 2.5 | 0.90 | 2.25 |

---

## 4. İşletme ve Bakım Maliyeti (C_O&M)

```
C_O&M = φ × C_invest    [€/yıl]

Burada:
  φ = İ&B çarpanı (O&M factor)
```

| Ekipman Tipi | φ Aralığı | Tipik φ |
|-------------|-----------|---------|
| Kazan | 1.04 – 1.08 | 1.06 |
| Kompresör | 1.06 – 1.12 | 1.08 |
| Chiller | 1.06 – 1.10 | 1.08 |
| Pompa | 1.04 – 1.08 | 1.06 |
| Isı değiştirici | 1.04 – 1.06 | 1.05 |
| CHP sistemi | 1.08 – 1.15 | 1.10 |

---

## 5. Çevre Maliyeti Bileşeni (C_env)

### 5.1. CO₂ Emisyon Maliyeti

```
C_env = ṁ_CO₂ × c_CO₂ × τ    [€/yıl]

Burada:
  ṁ_CO₂ = CO₂ emisyon hızı [ton/h]
  c_CO₂  = Karbon fiyatı [€/tCO₂]
  τ      = Yıllık çalışma süresi [h/yıl]
```

### 5.2. Yakıt Bazlı CO₂ Emisyon Faktörleri

| Yakıt | Emisyon Faktörü [kgCO₂/kWh_th] | Emisyon Faktörü [tCO₂/TJ] |
|-------|--------------------------------|---------------------------|
| Doğalgaz | 0.202 | 56.1 |
| LPG | 0.227 | 63.1 |
| Fuel oil | 0.268 | 74.4 |
| Kömür (bitümlü) | 0.341 | 94.6 |
| Linyit | 0.364 | 101.0 |
| Elektrik (Türkiye şebeke) | 0.440 | 122.0 |

### 5.3. CBAM (Carbon Border Adjustment Mechanism) Senaryoları

AB CBAM kapsamında, Türkiye'den AB'ye ihracat yapan sektörlerin karbon maliyeti:

| Senaryo | Karbon Fiyatı | Uygulama | Etki |
|---------|--------------|----------|------|
| Mevcut (2025) | ~50 €/tCO₂ | Geçiş dönemi, raporlama | Dolaylı maliyet |
| Orta vade (2027-2030) | ~80 €/tCO₂ | Tam uygulama | Doğrudan maliyet |
| Uzun vade (2030+) | ~100+ €/tCO₂ | Genişletilmiş kapsam | Yüksek maliyet etkisi |

#### CBAM Etkili Sektörler (Türkiye)

| Sektör | CBAM Kapsamı | Tipik CO₂ Yoğunluğu | Potansiyel Etki |
|--------|-------------|---------------------|----------------|
| Çimento | Evet (doğrudan) | 600-900 kgCO₂/ton | Çok yüksek |
| Demir-çelik | Evet (doğrudan) | 1,500-2,500 kgCO₂/ton | Çok yüksek |
| Alüminyum | Evet (doğrudan) | 1,500-2,000 kgCO₂/ton | Yüksek |
| Gübre | Evet (doğrudan) | 1,200-2,000 kgCO₂/ton | Yüksek |
| Kimya | Kısmen | 300-800 kgCO₂/ton | Orta |
| Gıda | Henüz değil | 100-300 kgCO₂/ton | Düşük (gelecekte olası) |
| Tekstil | Henüz değil | 80-250 kgCO₂/ton | Düşük (gelecekte olası) |

### 5.4. Çok Senaryolu Toplam Maliyet Karşılaştırması

Bir fabrika için yıllık maliyet bileşenleri örneği (2,000 kW kazan, 5,500 h/yıl):

| Bileşen | c_CO₂ = 0 | c_CO₂ = 50 €/t | c_CO₂ = 80 €/t | c_CO₂ = 100 €/t |
|---------|-----------|----------------|----------------|-----------------|
| C_fuel [€/yıl] | 380,000 | 380,000 | 380,000 | 380,000 |
| C_invest [€/yıl] | 25,000 | 25,000 | 25,000 | 25,000 |
| C_O&M [€/yıl] | 26,500 | 26,500 | 26,500 | 26,500 |
| C_env [€/yıl] | 0 | 62,000 | 99,200 | 124,000 |
| **C_total [€/yıl]** | **431,500** | **493,500** | **530,700** | **555,500** |
| C_env / C_total | 0% | 12.6% | 18.7% | 22.3% |

> **Çıkarım:** Karbon fiyatı 100 €/tCO₂ olduğunda, çevre maliyeti toplam maliyetin
> %22'sini oluşturur — bu durum optimal sistem tasarımını önemli ölçüde değiştirir.

---

## 6. Maliyet Hızı Formülasyonu (Cost Rate)

Optimizasyon için maliyet hızı cinsinden:

```
min Ċ_total = Ċ_fuel + Σ Ż_k + Ċ_env    [€/h]

Burada:
  Ċ_fuel = Toplam yakıt maliyet hızı [€/h]
  Ż_k    = k-inci bileşenin (yatırım + İ&B) maliyet hızı [€/h]
  Ċ_env  = Çevre maliyet hızı [€/h]
```

Ż_k hesaplama:

```
Ż_k = (CRF × Z_k × φ_k) / τ    [€/h]

Burada:
  Z_k  = k-inci bileşenin TCI'si [€]
  φ_k  = İ&B çarpanı
  τ    = Yıllık çalışma süresi [h/yıl]
```

---

## 7. Çok Amaçlı Fonksiyonlara Giriş

Tek amaçlı min C_total yerine, birden fazla amaç eşzamanlı optimize edilebilir:

### 7.1. Tipik Amaç Fonksiyonları

| Amaç | Formül | Birim |
|------|--------|-------|
| Toplam maliyet minimizasyonu | min C_total | €/yıl |
| Exergy verimi maksimizasyonu | max η_ex = Ėx_P / Ėx_F | % |
| CO₂ emisyon minimizasyonu | min ṁ_CO₂ | ton/yıl |
| Exergy yıkım minimizasyonu | min Σ Ėx_D,k | kW |
| Ürün maliyeti minimizasyonu | min c_P | €/kWh |

### 7.2. Çok Amaçlı Formülasyon

```
min F(x) = [f₁(x), f₂(x), ..., f_m(x)]

Tipik bi-objective:
  min f₁(x) = C_total(x)         — Toplam maliyet
  max f₂(x) = η_ex(x)            — Exergy verimi
              (veya min -η_ex(x))

Tri-objective:
  min f₁(x) = C_total(x)         — Toplam maliyet
  max f₂(x) = η_ex(x)            — Exergy verimi
  min f₃(x) = ṁ_CO₂(x)           — CO₂ emisyonu
```

> **Detay:** `multi_objective.md` dosyasında Pareto analizi ve karar destek yöntemleri

---

## 8. Özel Durumlar

### 8.1. CHP Sistemi Amaç Fonksiyonu

```
C_total,CHP = C_fuel,CHP + C_invest,CHP + C_O&M,CHP + C_env,CHP
            - C_avoided_electricity - C_avoided_heat

Burada:
  C_avoided_electricity = Şebekeden alınmayan elektrik maliyeti [€/yıl]
  C_avoided_heat        = Ayrı üretimle üretilmeyen ısı maliyeti [€/yıl]
```

### 8.2. Retrofit Durumu

Mevcut sisteme yapılacak iyileştirme için:

```
min ΔC_total = (C_fuel,yeni - C_fuel,mevcut) + C_invest,ek + C_O&M,ek + (C_env,yeni - C_env,mevcut)

NPV = -C_invest,ek + Σ_{t=1}^{n} (ΔC_fuel + ΔC_env - C_O&M,ek) / (1+i)^t
```

### 8.3. Birim Ürün Maliyeti Minimizasyonu

```
min c_P = Ċ_P / Ėx_P = (Ċ_F + Σ Ż_k) / Ėx_P    [€/kWh]

Bu formülasyon, en ucuz exergy ürünü üretmeyi hedefler.
```

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `decision_variables.md` — Karar değişkenleri ve kısıtlar
- `multi_objective.md` — Çok amaçlı optimizasyon detayı
- `sensitivity_analysis.md` — Parametre duyarlılığı
- `practical_guide.md` — Türkiye maliyet verileri ve uygulama
- `factory/economic_analysis.md` — NPV, IRR, SPP hesaplama
- `factory/energy_pricing.md` — Enerji fiyatlandırma detayı
- `factory/life_cycle_cost.md` — Yaşam döngüsü maliyet analizi

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Turton, R. et al. (2018). *Analysis, Synthesis and Design of Chemical Processes*. 5th ed.
- EPDK (Enerji Piyasası Düzenleme Kurumu). Tarife tabloları.
- EU CBAM Regulation (EU) 2023/956.
- Chemical Engineering Plant Cost Index (CEPCI), Chemical Engineering Magazine.
