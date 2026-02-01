---
title: "Kazan Yakıtları ve Özellikleri — Boiler Fuels & Properties"
category: equipment
equipment_type: boiler
subtype: "Yakıt Tipleri"
keywords: [yakıt, doğalgaz, LPG, kalorifer yakıtı]
related_files: [boiler/benchmarks.md, boiler/equipment/steam_firetube.md, boiler/equipment/condensing.md]
use_when: ["Yakıt karşılaştırması yapılırken", "Yakıt dönüşümü değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Kazan Yakıtları ve Özellikleri — Boiler Fuels & Properties

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Kapsam: Endüstriyel kazanlarda kullanılan tüm yakıt türlerinin termodinamik ve ekserji özellikleri
- Yakıt seçimi, kazan verimini, ekserji yıkımını, emisyon profilini ve işletme maliyetini doğrudan etkiler
- Ekserji analizinde yakıtın kimyasal ekserjisi (chemical exergy) birincil girdi olarak kullanılır
- Bu dosya yakıt bazlı verileri sunar; kazan tiplerine göre analiz için bkz. `equipment/boiler_steam_firetube.md`

## 1. Doğalgaz (Natural Gas)

### Bileşim (Tipik Türkiye Şebeke Gazı)
| Bileşen | Hacimsel Oran (%) |
|---------|-------------------|
| Metan (CH₄) | 92-97 |
| Etan (C₂H₆) | 1.5-4.0 |
| Propan (C₃H₈) | 0.2-1.5 |
| Karbondioksit (CO₂) | 0.1-1.0 |
| Azot (N₂) | 0.5-2.0 |
| Diğer (H₂S, He, vb.) | <0.5 |

### Termodinamik Özellikler
| Özellik | Değer | Birim |
|---------|-------|-------|
| Alt ısıl değer (LHV) | ~36,000 | kJ/m³ |
| Alt ısıl değer (LHV) | ~50,000 | kJ/kg |
| Üst ısıl değer (HHV) | ~40,000 | kJ/m³ |
| Üst ısıl değer (HHV) | ~55,500 | kJ/kg |
| Kimyasal ekserji | ~51,850 | kJ/kg |
| Kimyasal ekserji | ~38,200 | kJ/m³ |
| Yoğunluk (0°C, 1 atm) | 0.72 | kg/m³ |
| Tutuşma sıcaklığı | ~580 | °C |
| Teorik alev sıcaklığı | ~1,950 | °C |

### Yanma Özellikleri
- Stokiyometrik hava gereksinimi: ~10 m³ hava / m³ gaz (~17.2 kg hava / kg gaz)
- Pratik hava fazlası katsayısı (λ): 1.05-1.20
- CO₂ emisyon faktörü: ~56 kg CO₂/GJ (IPCC)
- Baca gazı çiğ noktası (asit): Kükürt içermediğinden ~55°C (su buharı çiğ noktası)
- Yoğuşmalı (condensing) kazanlara uygundur

### Ekserji/Enerji Oranı (φ)

```
φ = ex_ch / LHV
φ_doğalgaz ≈ 51,850 / 50,000 ≈ 1.04

Burada:
  ex_ch : Yakıtın kimyasal ekserjisi (kJ/kg)
  LHV   : Alt ısıl değer (kJ/kg)
  φ     : Ekserji/enerji oranı (boyutsuz)
```

### Avantajlar ve Dezavantajlar
- Temiz yanma — düşük partikül, düşük SOₓ emisyonu
- Yoğuşmalı kazanlarla %105+ verim (LHV bazlı) elde edilebilir
- Depolama gerektirmez (şebeke bağlantısı)
- Fiyat dalgalanmalarına maruz kalır

## 2. LPG (Liquefied Petroleum Gas — Sıvılaştırılmış Petrol Gazı)

### Bileşim
| Bileşen | Hacimsel Oran (%) |
|---------|-------------------|
| Propan (C₃H₈) | 30-70 |
| Bütan (C₄H₁₀) | 30-70 |
| Propen, büten | <5 |

### Termodinamik Özellikler
| Özellik | Değer | Birim |
|---------|-------|-------|
| Alt ısıl değer (LHV) | ~46,000 | kJ/kg |
| Üst ısıl değer (HHV) | ~50,000 | kJ/kg |
| Kimyasal ekserji | ~48,000 | kJ/kg |
| Yoğunluk (sıvı, 15°C) | ~540 | kg/m³ |
| Tutuşma sıcaklığı | ~470 | °C |
| Teorik alev sıcaklığı | ~1,980 | °C |

### Yanma Özellikleri
- Stokiyometrik hava gereksinimi: ~15.5 kg hava / kg LPG
- Pratik hava fazlası katsayısı (λ): 1.05-1.15
- CO₂ emisyon faktörü: ~63 kg CO₂/GJ
- Kükürt içermez — asit çiğ noktası düşük

### Ekserji/Enerji Oranı (φ)

```
φ_LPG ≈ 48,000 / 46,000 ≈ 1.04

Burada:
  ex_ch  : ~48,000 kJ/kg (propan/bütan karışımı)
  LHV    : ~46,000 kJ/kg
```

### Kullanım Alanları
- Doğalgaz şebekesi olmayan tesisler
- Yedek yakıt (dual-fuel) sistemleri
- Mevsimsel talep olan tesisler
- Gıda endüstrisinde temiz ısı kaynağı olarak

## 3. Fuel Oil (Akaryakıt)

### Sınıflandırma
| Özellik | No. 2 (Hafif — Diesel/Gasoil) | No. 6 (Ağır — Heavy Fuel Oil) |
|---------|-------------------------------|-------------------------------|
| Viskozite (50°C) | 2-6 cSt | 180-700 cSt |
| Yoğunluk (15°C) | 830-860 kg/m³ | 950-1010 kg/m³ |
| Kükürt içeriği | 0.1-1.0 % | 1.0-3.5 % |
| Ön ısıtma gereksinimi | Yok | 70-120°C |

### Termodinamik Özellikler
| Özellik | No. 2 | No. 6 | Birim |
|---------|-------|-------|-------|
| Alt ısıl değer (LHV) | ~42,500 | ~39,500 | kJ/kg |
| Üst ısıl değer (HHV) | ~45,000 | ~42,000 | kJ/kg |
| Kimyasal ekserji | ~47,000 | ~45,000 | kJ/kg |
| Tutuşma sıcaklığı | ~260 | ~400 | °C |
| Teorik alev sıcaklığı | ~2,050 | ~2,000 | °C |

### Yanma Özellikleri
- Stokiyometrik hava gereksinimi: ~14.0-14.5 kg hava / kg yakıt
- Pratik hava fazlası katsayısı (λ): 1.10-1.25
- CO₂ emisyon faktörü: ~77 kg CO₂/GJ (No. 6)
- CO₂ emisyon faktörü: ~74 kg CO₂/GJ (No. 2)

### Asit Çiğ Noktası ve Kükürt Etkisi

```
Asit çiğ noktası ≈ 120-160°C (kükürt içeriğine bağlı)

Burada:
  S%  = 1.0 → Tçiğ ≈ 120°C
  S%  = 2.0 → Tçiğ ≈ 140°C
  S%  = 3.0 → Tçiğ ≈ 155°C
```

Baca gazı sıcaklığı asit çiğ noktasının altına düşürülmemelidir — aksi halde baca ve ekonomizerde korozyon oluşur. Bu durum, fuel oil yakıtlı kazanlarda baca gazı çıkış sıcaklığını sınırlar ve enerji verimini düşürür.

### Ekserji/Enerji Oranı (φ)

```
φ_fuel_oil ≈ 1.06 (ortalama)

Burada:
  No.2 : φ ≈ 47,000 / 42,500 ≈ 1.106
  No.6 : φ ≈ 45,000 / 39,500 ≈ 1.139
```

### Ağır Yakıt (No. 6) İçin Özel Gereksinimler
- Yakıt ön ısıtması: 70-120°C (pompanabilirlik ve atomizasyon için)
- Buhar veya elektrikli ön ısıtıcı gerekli — ek enerji tüketimi
- Atomizasyon basıncı: 10-30 bar (mekanik) veya buhar atomizasyon
- Periyodik baca temizliği gerekli (kurum ve kül birikimi)
- SOₓ emisyon kontrol sistemi gerekebilir (scrubber veya düşük kükürtlü yakıt)

## 4. Kömür (Coal)

### Türler ve Özellikleri
| Özellik | Linyit (Lignite) | Bitümlü (Bituminous) | Antrasit (Anthracite) |
|---------|------------------|----------------------|-----------------------|
| Karbon içeriği | %25-45 | %45-86 | %86-98 |
| Nem içeriği | %25-60 | %5-15 | %3-7 |
| Kül içeriği | %10-50 | %5-20 | %5-15 |
| Uçucu madde | %25-35 | %20-45 | %3-8 |
| Kükürt içeriği | %0.5-6 | %0.5-3 | %0.5-1 |

### Termodinamik Özellikler
| Özellik | Linyit | Bitümlü | Antrasit | Birim |
|---------|--------|---------|----------|-------|
| Alt ısıl değer (LHV) | 10,000-15,000 | 22,000-30,000 | 28,000-32,000 | kJ/kg |
| Üst ısıl değer (HHV) | 12,000-17,000 | 24,000-32,000 | 30,000-34,000 | kJ/kg |
| Kimyasal ekserji | 12,000-17,000 | 25,000-30,000 | 28,000-32,000 | kJ/kg |
| Teorik alev sıcaklığı | ~1,500-1,700 | ~1,800-2,000 | ~2,000-2,100 | °C |

### Yanma Özellikleri
- Stokiyometrik hava gereksinimi: 5-11 kg hava / kg kömür (türüne bağlı)
- Pratik hava fazlası katsayısı (λ): 1.20-1.50 (ızgaralı), 1.15-1.25 (pülverize)
- CO₂ emisyon faktörü: ~95-115 kg CO₂/GJ (türüne bağlı)
- Asit çiğ noktası: 125-170°C (kükürt içeriğine bağlı)

### Kül ve Nem Etkisi

```
LHV_yaş = LHV_kuru × (1 - W) - 2,443 × W

Burada:
  LHV_yaş  : Yaş bazda alt ısıl değer (kJ/kg)
  LHV_kuru : Kuru bazda alt ısıl değer (kJ/kg)
  W        : Nem oranı (kg su / kg yaş kömür), 0-1 arası
  2,443    : Suyun buharlaşma ısısı (kJ/kg, 25°C'de)
```

Yüksek nem içeriği (%25-60 linyitte) ısıl değeri önemli ölçüde düşürür. Her %10 nem artışı yaklaşık %10 LHV kaybına karşılık gelir.

### Ekserji/Enerji Oranı (φ)

```
φ_kömür ≈ 1.05 - 1.15 (türüne göre değişir)

Burada:
  Linyit    : φ ≈ 1.05-1.08
  Bitümlü   : φ ≈ 1.06-1.10
  Antrasit   : φ ≈ 1.05-1.08
```

Szargut formülü ile kömür kimyasal ekserjisi hesaplanabilir:

```
ex_ch = 363.439 × C + 1,075.633 × H - 86.308 × O + 4.147 × N + 190.798 × S - 21.1 × Kül

Burada:
  C, H, O, N, S, Kül : Elemental analiz sonuçları (kütle fraksiyonu olarak, 0-1 arası)
  ex_ch              : Kimyasal ekserji (kJ/kg)
```

## 5. Biyokütle (Biomass)

### Türler ve Özellikleri
| Özellik | Odun Peleti | Odun Yongası | Tarımsal Atık | Birim |
|---------|-------------|--------------|---------------|-------|
| Nem içeriği | 6-10 | 25-45 | 10-35 | % |
| Kül içeriği | 0.5-1.5 | 0.5-2.0 | 3-15 | % |
| Kükürt içeriği | <0.05 | <0.05 | 0.05-0.3 | % |
| Yoğunluk (bulk) | 600-700 | 200-350 | 100-400 | kg/m³ |

### Termodinamik Özellikler
| Özellik | Odun Peleti | Odun Yongası (kuru) | Tarımsal Atık | Birim |
|---------|-------------|---------------------|---------------|-------|
| Alt ısıl değer (LHV) | 16,500-19,000 | 14,000-16,000 | 12,000-17,000 | kJ/kg |
| Üst ısıl değer (HHV) | 18,500-21,000 | 16,000-18,000 | 14,000-19,000 | kJ/kg |
| Kimyasal ekserji | 19,000-22,000 | 16,000-19,000 | 14,000-19,500 | kJ/kg |
| Teorik alev sıcaklığı | ~1,300-1,500 | ~1,200-1,400 | ~1,100-1,400 | °C |

### Yanma Özellikleri
- Stokiyometrik hava gereksinimi: 4.5-6.5 kg hava / kg biyokütle
- Pratik hava fazlası katsayısı (λ): 1.30-1.60 (ızgaralı), 1.15-1.30 (akışkan yataklı)
- CO₂ emisyon faktörü: ~100-120 kg CO₂/GJ (brüt), ancak karbon nötr olarak kabul edilir (IPCC)
- Biyojenik karbon döngüsü sebebiyle net emisyon ≈ 0 kg CO₂/GJ

### Nem İçeriğinin Kritik Etkisi

```
η_kazan ≈ η_kuru - 0.12 × W

Burada:
  η_kazan : Kazan verimi (0-1 arası)
  η_kuru  : Kuru yakıtta beklenen verim (~0.85 odun peleti için)
  W       : Nem oranı (0-1 arası)
```

Nem içeriği %50'nin üzerinde olan biyokütle, ek kurutma olmadan verimli yakmak çok güçtür. Her %10 nem artışı kazan verimini yaklaşık %1.2 düşürür.

### Ekserji/Enerji Oranı (φ)

```
φ_biyokütle ≈ 1.10 - 1.20 (türüne göre değişir)

Burada:
  Odun peleti    : φ ≈ 1.12-1.16
  Odun yongası   : φ ≈ 1.10-1.18
  Tarımsal atık  : φ ≈ 1.10-1.15
```

### Karbon Nötr Yaklaşım
Biyokütle, yaşam döngüsünde atmosferden CO₂ absorbe ettiği için IPCC metodolojisinde karbon nötr kabul edilir. Ancak ekserji analizinde bu muafiyet uygulanmaz — yanma ekserjisi diğer yakıtlarla aynı prensiple hesaplanır.

## 6. Yakıt Karşılaştırma Tablosu

| Özellik | Doğalgaz | LPG | Fuel Oil No.2 | Fuel Oil No.6 | Bitümlü Kömür | Odun Peleti |
|---------|----------|-----|---------------|---------------|----------------|-------------|
| LHV (kJ/kg) | ~50,000 | ~46,000 | ~42,500 | ~39,500 | ~26,000 | ~17,500 |
| HHV (kJ/kg) | ~55,500 | ~50,000 | ~45,000 | ~42,000 | ~28,000 | ~19,500 |
| Kimyasal ekserji (kJ/kg) | ~51,850 | ~48,000 | ~47,000 | ~45,000 | ~28,000 | ~20,500 |
| Stokiyometrik hava (kg/kg) | ~17.2 | ~15.5 | ~14.2 | ~14.0 | ~8.5 | ~5.5 |
| Teorik alev sıcaklığı (°C) | ~1,950 | ~1,980 | ~2,050 | ~2,000 | ~1,900 | ~1,400 |
| CO₂ faktörü (kg CO₂/GJ) | ~56 | ~63 | ~74 | ~77 | ~95 | ~0* |
| Tipik kazan verimi (%, LHV) | 90-95** | 88-93 | 85-90 | 83-88 | 80-87 | 82-90 |
| φ (ekserji/enerji) | ~1.04 | ~1.04 | ~1.11 | ~1.14 | ~1.08 | ~1.14 |

\* Biyokütle karbon nötr kabul edilir (IPCC).
\*\* Yoğuşmalı kazanlarla LHV bazında %105'e kadar çıkabilir.

## 7. Stokiyometrik Hava Hesabı

Genel bir hidrokarbonun yanma denklemi:

```
CₓHᵧOₙSₖ + (x + y/4 - n/2 + k) × O₂ → x × CO₂ + (y/2) × H₂O + k × SO₂

Burada:
  CₓHᵧOₙSₖ : Yakıtın elementel formülü
  x, y, n, k : Karbon, hidrojen, oksijen, kükürt atom sayıları
```

Stokiyometrik hava miktarı:

```
m_hava_st = (1 / 0.233) × [(32x + 8y - 16n + 32k) / M_yakıt]   (kg hava / kg yakıt)

Burada:
  0.233    : Havanın kütle bazında oksijen oranı
  x, y, n, k : Elementel analiz sonuçları (mol bazında)
  M_yakıt  : Yakıtın molar kütlesi (g/mol)
```

Gerçek hava miktarı:

```
m_hava_gerçek = λ × m_hava_st

Burada:
  λ : Hava fazlası katsayısı (excess air ratio)
      Doğalgaz : λ = 1.05-1.20
      Fuel oil : λ = 1.10-1.25
      Kömür    : λ = 1.20-1.50
      Biyokütle: λ = 1.30-1.60
```

## 8. Yakıt Exergy/Enerji Oranı (φ)

φ oranı, yakıtın ekserji içeriğinin enerji içeriğine (LHV) oranını ifade eder. Bu oran, farklı yakıtlar için ekserji analizinde önemli bir parametredir.

### φ Değerleri (Szargut ve Bejan Referanslarına Göre)

| Yakıt | φ Aralığı | Tipik Değer | Kaynak |
|-------|-----------|-------------|--------|
| Doğalgaz (CH₄) | 1.03-1.05 | 1.04 | Szargut (2005) |
| LPG (C₃/C₄) | 1.03-1.06 | 1.04 | Kotas (1985) |
| Fuel Oil No.2 | 1.07-1.12 | 1.11 | Szargut (2005) |
| Fuel Oil No.6 | 1.10-1.16 | 1.14 | Szargut (2005) |
| Linyit | 1.05-1.08 | 1.06 | Bejan (1996) |
| Bitümlü kömür | 1.06-1.10 | 1.08 | Szargut (2005) |
| Antrasit | 1.05-1.08 | 1.06 | Bejan (1996) |
| Odun peleti | 1.10-1.18 | 1.14 | Kotas (1985) |
| Odun yongası | 1.10-1.20 | 1.15 | Ptasinski (2016) |

### Hesaplama

```
ex_yakıt = φ × LHV

Burada:
  ex_yakıt : Yakıtın kimyasal ekserjisi (kJ/kg)
  φ        : Ekserji/enerji oranı (boyutsuz)
  LHV      : Yakıtın alt ısıl değeri (kJ/kg)
```

Gaz yakıtlar için φ değeri 1'e yakındır — enerji ve ekserji miktarları birbirine çok yakındır. Katı ve sıvı yakıtlarda hidrojen/karbon oranının düşmesiyle φ artar.

## Varsayılan Değerler (Ölçüm Yoksa)

Aşağıdaki değerler, tesis verisi mevcut olmadığında ekserji hesaplamalarında başlangıç değeri olarak kullanılabilir.

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Doğalgaz LHV | 36,000 kJ/m³ | Türkiye şebeke gazı tipik |
| Doğalgaz φ | 1.04 | Szargut referansı |
| LPG LHV | 46,000 kJ/kg | %50 propan / %50 bütan |
| Fuel Oil No.2 LHV | 42,500 kJ/kg | Düşük kükürtlü gasoil |
| Fuel Oil No.6 LHV | 39,500 kJ/kg | Ağır yakıt, %2 kükürt |
| Kömür LHV | 15,000 kJ/kg | Türkiye linyiti (ortalama) |
| Odun peleti LHV | 17,500 kJ/kg | EN-Plus A1 sertifikalı |
| Hava fazlası (λ) doğalgaz | 1.10 | İyi ayarlanmış brülör |
| Hava fazlası (λ) fuel oil | 1.15 | İyi ayarlanmış brülör |
| Hava fazlası (λ) kömür | 1.35 | Pülverize sistem |
| Baca gazı sıcaklığı — gaz | 150°C | Ekonomizersiz |
| Baca gazı sıcaklığı — fuel oil | 200°C | Asit çiğ noktası sınırı |
| Baca gazı sıcaklığı — kömür | 180°C | Ekonomizerli |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |

## İlgili Dosyalar
- Ateş borulu buhar kazanları: `equipment/boiler_steam_firetube.md`
- Su borulu buhar kazanları: `equipment/boiler_steam_watertube.md`
- Sıcak su kazanları: `equipment/boiler_hotwater.md`
- Kazan ekserji hesaplamaları: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Brülör ayarı ve hava/yakıt oranı: `solutions/boiler_combustion_optimization.md`
- Baca gazı ısı geri kazanımı: `solutions/boiler_flue_gas_recovery.md`

## Referanslar
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths. (Reprinted by Krieger, 1995.)
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
- Ptasinski, K.J. (2016). *Efficiency of Biomass Energy: An Exergy Approach to Biofuels, Power, and Biorefineries*, Wiley.
- ASME PTC 4 (2013). *Fired Steam Generators — Performance Test Codes*, ASME.
- Spirax Sarco (2023). *The Steam and Condensate Loop*, Technical Reference Guide.
- IPCC (2006). *Guidelines for National Greenhouse Gas Inventories*, Volume 2: Energy.
- EN 14961-2 (2011). *Solid Biofuels — Fuel Specifications and Classes*, CEN.
- TS 4045 (Türk Standardı). *Doğalgaz — Özellikleri ve Kalite Standartları*.
