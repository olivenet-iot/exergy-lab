# Chiller Exergy Hesaplamaları

> Son güncelleme: 2026-01-31

## Temel İlkeler

Chiller elektrik enerjisini (buhar sıkıştırmalı) veya termal enerjiyi (absorpsiyonlu) kullanarak
düşük sıcaklıkta soğutma exergy'si üretir. Soğutma exergy'si, referans ortam sıcaklığının altında
ısı transferi yapabilme kapasitesini temsil eder.

**Referans durumu:** T₀ = 25°C (298.15 K), P₀ = 1 atm

## 1. Soğutma Yükü Hesabı

### 1.1 Evaporatör Soğutma Kapasitesi

```
Q_evap = m_chw × Cp × ΔT_chw

Burada:
  Q_evap = Soğutma kapasitesi (kW)
  m_chw  = Soğutma suyu kütle debisi (kg/s)
  Cp     = Suyun özgül ısısı (4.186 kJ/kg·K)
  ΔT_chw = Soğutma suyu giriş-çıkış sıcaklık farkı (°C)
```

Hacimsel debi ile:
```
Q_evap = V̇_chw × ρ × Cp × ΔT_chw

Burada:
  V̇_chw = Hacimsel debi (m³/s veya l/s)
  ρ      = Suyun yoğunluğu (~998 kg/m³, ~7°C'de)
```

### 1.2 Tipik Tasarım Değerleri

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| CHW giriş (return) | 12°C | Konfor soğutma |
| CHW çıkış (supply) | 7°C | Konfor soğutma |
| ΔT_chw | 5°C | Standart tasarım |
| CHW giriş (proses) | 15-18°C | Endüstriyel |
| CHW çıkış (proses) | 5-10°C | Endüstriyel |

### 1.3 Ton-kW Dönüşümü

```
1 ton (soğutma) = 3.517 kW = 12,000 BTU/h

Q_evap (ton) = Q_evap (kW) / 3.517
```

## 2. COP (Performans Katsayısı) Hesabı

### 2.1 Buhar Sıkıştırmalı Chiller COP

```
COP = Q_evap / W_comp

Burada:
  Q_evap = Soğutma kapasitesi (kW)
  W_comp = Kompresör elektrik gücü (kW)
```

### 2.2 Carnot COP (Teorik Maksimum)

```
COP_Carnot = T_evap / (T_cond - T_evap)

Burada:
  T_evap = Evaporatör soğutucu akışkan sıcaklığı (K)
  T_cond = Kondenser soğutucu akışkan sıcaklığı (K)

Not: Sıcaklıklar mutlak (Kelvin) olmalıdır.
```

**Örnek:**
```
T_evap = 5°C = 278.15 K
T_cond = 35°C = 308.15 K

COP_Carnot = 278.15 / (308.15 - 278.15) = 278.15 / 30 = 9.27
```

### 2.3 kW/ton Dönüşümü

```
kW/ton = 3.517 / COP

Burada:
  kW/ton = Soğutma tonu başına güç tüketimi
  COP    = Performans katsayısı

Örnek: COP = 6.0 → kW/ton = 3.517 / 6.0 = 0.586 kW/ton
```

| COP | kW/ton | Değerlendirme |
|-----|--------|---------------|
| >7.0 | <0.50 | Mükemmel |
| 5.4-7.0 | 0.50-0.65 | İyi |
| 4.1-5.4 | 0.65-0.85 | Ortalama |
| <4.1 | >0.85 | Düşük |

## 3. Soğutma Exergy'si

### 3.1 Soğutma Exergy Formülü

Ortam sıcaklığının altındaki ısı transferinin exergy içeriği:
```
Ex_cool = Q_evap × |1 - T₀/T_cool|

Burada:
  Ex_cool = Soğutma exergy'si (kW)
  Q_evap  = Soğutma kapasitesi (kW)
  T₀      = Referans sıcaklık = 298.15 K (25°C)
  T_cool  = Soğutma suyu ortalama sıcaklığı (K)
```

Soğutma suyu ortalama sıcaklığı:
```
T_cool = (T_chw_in + T_chw_out) / 2

Örnek: T_cool = (12 + 7) / 2 = 9.5°C = 282.65 K
```

### 3.2 Carnot Faktörü (Soğutma)

```
τ_cool = |1 - T₀/T_cool| = (T₀ - T_cool) / T₀

Burada T_cool < T₀ (ortam altı soğutma)
```

**Önemli:** Soğutma exergy'si ısıtma exergy'sine göre çok daha düşüktür.
Çünkü soğutma sıcaklığı ortam sıcaklığına yakındır ve Carnot faktörü küçüktür.

### 3.3 Örnek Hesap

```
Q_evap = 500 kW
T_chw_out = 7°C, T_chw_in = 12°C
T_cool = 9.5°C = 282.65 K
T₀ = 298.15 K

τ_cool = (298.15 - 282.65) / 298.15 = 15.5 / 298.15 = 0.0520

Ex_cool = 500 × 0.0520 = 26.0 kW
```

Soğutma exergy'si sadece %5.2 — yani 500 kW soğutma kapasitesinin
exergy içeriği yalnızca 26 kW'tır.

### 3.4 Soğutma Sıcaklığına Göre Carnot Faktörü

| T_cool (°C) | T_cool (K) | τ_cool | 500 kW için Ex_cool |
|-------------|-----------|--------|---------------------|
| -10 | 263.15 | 0.133 | 66.5 kW |
| -5 | 268.15 | 0.112 | 56.0 kW |
| 0 | 273.15 | 0.092 | 45.8 kW |
| 5 | 278.15 | 0.072 | 36.0 kW |
| 7 | 280.15 | 0.064 | 32.1 kW |
| 10 | 283.15 | 0.053 | 26.5 kW |
| 15 | 288.15 | 0.035 | 17.4 kW |

## 4. Chiller Exergy Verimi

### 4.1 Buhar Sıkıştırmalı Chiller

```
η_ex = Ex_cool / W_comp × 100%

Veya Carnot bazlı:
η_ex = COP / COP_Carnot × 100%

Veya açık formül:
η_ex = COP × (T₀ - T_cool) / T_cool × 100%
```

**Örnek:**
```
Q_evap = 500 kW, W_comp = 83 kW (COP = 6.02)
T_evap = 3°C = 276.15 K, T_cond = 35°C = 308.15 K
T_cool = 9.5°C = 282.65 K

COP_Carnot = 276.15 / (308.15 - 276.15) = 8.63

η_ex = 6.02 / 8.63 × 100% = 69.8%

Veya:
Ex_cool = 500 × (298.15 - 282.65) / 298.15 = 26.0 kW
η_ex = 26.0 / 83 × 100% = 31.3%
```

**Not:** İki yöntem farklı sonuç verir çünkü referans sıcaklıklar farklıdır.
İlki evaporatör soğutucu akışkan sıcaklığını, ikincisi soğutma suyu sıcaklığını kullanır.
ExergyLab'da ikinci yöntem (soğutma suyu bazlı) tercih edilir.

### 4.2 Absorpsiyonlu Chiller

```
Termal COP:
COP_th = Q_evap / Q_gen

Exergy verimi:
η_ex = Ex_cool / Ex_heat_input × 100%

Ex_heat_input = Q_gen × (1 - T₀/T_gen)

Burada:
  Q_gen = Jeneratör ısı girdisi (kW)
  T_gen = Jeneratör sıcaklığı (K)
```

**Örnek:**
```
Q_evap = 500 kW, Q_gen = 714 kW (COP_th = 0.70)
T_gen = 90°C = 363.15 K
T_cool = 9.5°C = 282.65 K

Ex_heat_input = 714 × (1 - 298.15/363.15) = 714 × 0.179 = 127.8 kW
Ex_cool = 500 × (298.15 - 282.65) / 298.15 = 26.0 kW

η_ex = 26.0 / 127.8 × 100% = 20.3%
```

## 5. Kondenser Isı Atımı

### 5.1 Enerji Dengesi

```
Q_cond = Q_evap + W_comp   (buhar sıkıştırmalı)
Q_cond = Q_evap + Q_gen    (absorpsiyonlu, yaklaşık)
```

### 5.2 Kondenser Exergy Kaybı

```
Ex_cond_loss = Q_cond × (1 - T₀/T_cond)

Burada:
  T_cond = Kondenser soğutucu akışkan sıcaklığı (K)
```

Kondenser sıcaklığı ortama yakın olduğunda exergy kaybı düşüktür.

## 6. Bileşen Bazlı Exergy Yıkımı

### 6.1 Kompresör İrreversibilitesi

```
I_comp = W_comp - (Ex_out - Ex_in)_refrigerant

İzentropik verimlilik:
η_is = W_isentropic / W_actual
```

| Kompresör Tipi | Tipik η_is |
|----------------|-----------|
| Santrifüj | 0.75-0.85 |
| Vidalı | 0.70-0.80 |
| Scroll | 0.65-0.75 |
| Pistonlu | 0.65-0.78 |

### 6.2 Genleşme Valfi (Throttling) Kaybı

```
I_throttle = m_ref × T₀ × (s_out - s_in)

Burada:
  m_ref = Soğutucu akışkan kütle debisi (kg/s)
  s_out, s_in = Genleşme valfi çıkış/giriş entropisi (kJ/kg·K)
```

Bu kayıp termodinamik zorunluluktur. Azaltma yöntemleri:
- Ekonomizer (flash gas bypass)
- İki kademeli genleşme
- Ejektör kullanımı

### 6.3 Evaporatör ve Kondenser Exergy Yıkımı

```
I_evap = m_ref × T₀ × [(s_out - s_in)_ref - Q_evap / T_chw_avg]

I_cond = m_ref × T₀ × [(s_out - s_in)_ref + Q_cond / T_cw_avg]
```

Isı değiştiricilerdeki exergy yıkımı, sıcaklık farkına (approach) bağlıdır.
Approach ne kadar küçükse, exergy yıkımı o kadar düşüktür.

### 6.4 Tipik Exergy Yıkım Dağılımı

| Bileşen | Exergy Yıkım Payı |
|---------|-------------------|
| Kompresör | %35-45 |
| Kondenser | %15-25 |
| Evaporatör | %10-20 |
| Genleşme valfi | %15-25 |
| Boru ve yardımcılar | %2-5 |

## 7. IPLV (Entegre Kısmi Yük Değeri)

### 7.1 AHRI 550/590 IPLV Formülü

```
IPLV = 0.01×COP_100% + 0.42×COP_75% + 0.45×COP_50% + 0.12×COP_25%

Burada katsayılar yıllık tipik yük dağılımını temsil eder:
  %100 yük → %1 zaman
  %75 yük  → %42 zaman
  %50 yük  → %45 zaman
  %25 yük  → %12 zaman
```

### 7.2 IPLV Koşulları (Su Soğutmalı)

| Yük | Kondenser Suyu Giriş |
|-----|---------------------|
| %100 | 29.4°C (85°F) |
| %75 | 23.9°C (75°F) |
| %50 | 18.3°C (65°F) |
| %25 | 18.3°C (65°F) |

### 7.3 NPLV (Non-Standard Part Load Value)

Bina veya tesis spesifik koşullarında hesaplanan kısmi yük değeri:
```
NPLV = 0.01×COP_A + 0.42×COP_B + 0.45×COP_C + 0.12×COP_D

A, B, C, D değerleri gerçek kondenser suyu sıcaklıklarına göre belirlenir.
```

### 7.4 Örnek IPLV Hesabı

```
Santrifüj VSD chiller (500 kW):
  COP @ 100% = 6.5 (kondenser suyu 29.4°C)
  COP @ 75%  = 8.0 (kondenser suyu 23.9°C)
  COP @ 50%  = 10.0 (kondenser suyu 18.3°C)
  COP @ 25%  = 9.5 (kondenser suyu 18.3°C)

IPLV = 0.01×6.5 + 0.42×8.0 + 0.45×10.0 + 0.12×9.5
     = 0.065 + 3.36 + 4.50 + 1.14
     = 9.07

kW/ton_IPLV = 3.517 / 9.07 = 0.388 kW/ton
```

## 8. Sistem Seviyesi Exergy Analizi

### 8.1 Toplam Sistem Girdisi

```
Ex_input = W_chiller + W_pumps + W_tower + W_AHU_fans

Burada:
  W_chiller  = Chiller kompresör gücü (kW)
  W_pumps    = CHW + CW pompa gücü (kW)
  W_tower    = Soğutma kulesi fan gücü (kW)
  W_AHU_fans = Klima santrali fan gücü (soğutma katkısı, kW)
```

### 8.2 Sistem Exergy Verimi

```
η_system = Ex_cool / Ex_input × 100%
```

| Sistem Durumu | η_system | Açıklama |
|--------------|----------|----------|
| Düşük | <%15 | Eski sistem, bakımsız, sabit hız |
| Ortalama | %15-25 | Standart sistem |
| İyi | %25-35 | VSD, optimize kontrol |
| Mükemmel | >%35 | Tam optimize, free cooling |

### 8.3 Exergy Akış Dağılımı (Tipik Sistem)

```
Elektrik Girişi (100%)
  ├── Chiller kompresör tersinmezliği (%25-40)
  ├── Kondenser exergy kaybı (%10-20)
  ├── Evaporatör exergy kaybı (%5-15)
  ├── Genleşme valfi kaybı (%5-10)
  ├── Pompa kayıpları (%5-15)
  ├── Soğutma kulesi kayıpları (%3-8)
  ├── Dağıtım kayıpları (%2-5)
  └── Net faydalı soğutma exergy'si (%5-15)
```

## 9. Lift ve COP İlişkisi

### 9.1 Lift Tanımı

```
Lift = T_cond - T_evap

Burada:
  T_cond = Kondenser yoğuşma sıcaklığı (°C)
  T_evap = Evaporatör buharlaşma sıcaklığı (°C)
```

### 9.2 Lift Etkisi

```
Her 1°C lift azalması ≈ %2-3 COP artışı

COP yaklaşım:
COP ≈ K / Lift

Burada K sabit (kompresör tipine bağlı)
```

### 9.3 Lift Optimizasyonu

| Strateji | Lift Azalması | COP Artışı |
|----------|---------------|------------|
| CHW setpoint +1°C | ~1°C | %2-3 |
| Kondenser suyu -1°C | ~1°C | %2-3 |
| Approach iyileştirme | 1-3°C | %2-9 |
| Toplam potansiyel | 3-5°C | %6-15 |

## 10. Örnek Hesaplamalar

### 10.1 Tam Sistem Exergy Analizi

**Girdiler:**
```
Su soğutmalı santrifüj chiller, 500 kW soğutma
  W_comp = 83 kW (COP = 6.02)
  W_chw_pump = 8 kW
  W_cw_pump = 12 kW
  W_tower = 7 kW
  CHW: 12°C giriş, 7°C çıkış
  CW: 30°C giriş, 35°C çıkış
  T₀ = 25°C = 298.15 K
```

**Hesap:**
```
1. Soğutma exergy'si:
   T_cool = (12 + 7) / 2 = 9.5°C = 282.65 K
   τ_cool = (298.15 - 282.65) / 298.15 = 0.0520
   Ex_cool = 500 × 0.0520 = 26.0 kW

2. Toplam enerji girişi:
   Ex_input = 83 + 8 + 12 + 7 = 110 kW

3. Sistem exergy verimi:
   η_system = 26.0 / 110 × 100% = 23.6%

4. Exergy yıkımı:
   Ex_destroyed = 110 - 26.0 = 84.0 kW

5. Chiller-only exergy verimi:
   η_chiller = 26.0 / 83 × 100% = 31.3%
```

### 10.2 Absorpsiyonlu Chiller Exergy Analizi

**Girdiler:**
```
Çift etkili LiBr-Su absorpsiyonlu chiller
  Q_evap = 500 kW, COP_th = 1.2
  Q_gen = 417 kW (buhar, 8 bar, 170°C)
  W_pump = 5 kW (solusyon pompası)
  CHW: 12°C giriş, 7°C çıkış
  T_gen = 170°C = 443.15 K
```

**Hesap:**
```
1. Soğutma exergy'si:
   Ex_cool = 500 × (298.15 - 282.65) / 298.15 = 26.0 kW

2. Jeneratör ısı exergy'si:
   Ex_heat = 417 × (1 - 298.15/443.15) = 417 × 0.327 = 136.4 kW

3. Toplam exergy girişi:
   Ex_input = 136.4 + 5 = 141.4 kW

4. Exergy verimi:
   η_ex = 26.0 / 141.4 × 100% = 18.4%
```

### 10.3 Free Cooling Exergy Tasarrufu

**Senaryo:** Kış aylarında soğutma kulesi suyu ile direkt soğutma
```
Chiller COP = 6.0, W_comp = 83 kW
Free cooling pompa gücü = 15 kW
Free cooling saat = 2000 saat/yıl
Chiller saat = 4000 saat/yıl
Elektrik fiyatı = €0.12/kWh

Tasarruf = (83 - 15) × 2000 = 136,000 kWh/yıl
Maliyet tasarrufu = 136,000 × 0.12 = €16,320/yıl
```

## Sınırlamalar

1. Soğutucu akışkan termodinamik özellikleri ideal gaz kabulüne dayanmaz — gerçek akışkan tabloları gereklidir
2. Kısmi yük performansı lineer olmayan özellik gösterir — IPLV formülü yaklaşıktır
3. Geçici (transient) durumlar dahil değildir — kararlı hal analizi yapılır
4. Soğutucu akışkan miktarı ve şarj durumu verimi etkiler — ideal şarj varsayılır
5. Fouling (kirlenme) etkisi ayrıca modellenmemiştir

## İlgili Dosyalar
- Benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Buhar sıkıştırmalı chiller: `equipment/chiller_vapor_compression.md`
- Absorpsiyonlu chiller: `equipment/chiller_absorption.md`
- Soğutucu akışkanlar: `equipment/chiller_refrigerants.md`
- Audit metodolojisi: `methodology/chiller_audit.md`

## Referanslar
- Cengel & Boles, "Thermodynamics: An Engineering Approach," Chapter 11 — Refrigeration Cycles
- Bejan, "Advanced Engineering Thermodynamics" — Low Temperature Systems
- Kotas, "The Exergy Method of Thermal Plant Analysis"
- Dincer & Rosen, "Exergy: Energy, Environment and Sustainable Development"
- AHRI Standard 550/590, "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages"
- ASHRAE Handbook — HVAC Systems and Equipment, Chapter 42: Centrifugal Chillers
- Şencan et al. (2006), "Exergy analysis of lithium bromide/water absorption systems," Renewable Energy
- Morosuk & Tsatsaronis (2008), "Advanced exergetic evaluation of refrigeration machines," Energy
