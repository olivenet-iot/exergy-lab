---
title: "Kompresör Exergy Hesaplamaları"
category: reference
equipment_type: compressor
keywords: [exergy, kompresör, termodinamik, hesaplama]
related_files: [compressor/benchmarks.md, compressor/audit.md, compressor/equipment/systems_overview.md]
use_when: ["Kompresör exergy hesaplaması yapılırken", "Termodinamik formüller gerektiğinde"]
priority: high
last_updated: 2026-01-31
---
# Kompresör Exergy Hesaplamaları

> Son güncelleme: 2026-01-31

## Temel İlkeler

Kompresör elektrik enerjisini (saf exergy) basınçlı hava exergy'sine dönüştürür.
Dönüşüm sırasında entropi üretilir ve exergy yok edilir.

## 1. Temel Hesaplama Adımları

### 1.1 Giren Exergy (Elektrik)

Elektrik saf exergy'dir:
```
Ex_in = P_electric [kW]
```

### 1.2 Kütle Debisi

Hacimsel debiden kütle debisine:
```
ṁ = V̇ × ρ_air

Burada:
- V̇ = Hacimsel debi [m³/s]
- ρ_air = Hava yoğunluğu ≈ 1.2 kg/m³ (25°C, 1 atm'de)
```

### 1.3 Çıkan Exergy (Basınçlı Hava)

İdeal gaz kabulüyle basınçlı havanın exergy'si (aftercooler sonrası, T ≈ T₀):
```
Ex_air = ṁ × R × T₀ × ln(P₂/P₁)

Burada:
- R = 0.287 kJ/kg·K (kuru hava için gaz sabiti)
- T₀ = 298.15 K (dead state sıcaklığı, ~25°C)
- P₂ = Çıkış basıncı [kPa, mutlak]
- P₁ = Giriş basıncı = 101.325 kPa
```

**Not:** Bu formül, aftercooler ile basınçlı havanın ortam sıcaklığına yakın soğutulduğu durumlarda geçerlidir. Çoğu endüstriyel sistemde bu kabul uygundur.

### 1.4 Çıkış Sıcaklığı T₀'dan Farklı ise (Genel Formül)

Basınçlı hava T₂ sıcaklığında ise (aftercooler yetersiz veya yok):
```
Ex_air = ṁ × [Cp × (T₂ - T₀) - T₀ × Cp × ln(T₂/T₀) + R × T₀ × ln(P₂/P₁)]
```
Bu formül hem termal hem mekanik (basınç) exergy bileşenlerini içerir.

### 1.5 Exergy Yıkımı

```
Ex_destroyed = Ex_in - Ex_air [kW]
```

### 1.6 Exergy Verimi

```
η_ex = Ex_air / Ex_in × 100 [%]
```

### 1.7 Atık Isı Exergy Potansiyeli

```
Q_waste ≈ Ex_destroyed [kW]  (büyük kısmı ısı olarak)

Ex_heat_recoverable = Q_waste × (1 - T₀/T_exhaust)

Burada:
- T_exhaust = Çıkış sıcaklığı [K]
```

### 1.8 Yıllık Maliyet

```
Yıllık_kayıp_kWh = Ex_destroyed × çalışma_saati
Yıllık_kayıp_EUR = Yıllık_kayıp_kWh × elektrik_fiyatı
```

## 2. Çok Kademeli Sıkıştırma

### 2.1 Tek Kademe Politropik Sıkıştırma İşi

```
W_stage = (n/(n-1)) × ṁ × R × T₁ × [(P₂/P₁)^((n-1)/n) - 1]

Burada:
- n = politropik indeks (1.0 < n < k, soğutmalı sıkıştırma; n = k = 1.4 adyabatik)
- ṁ = kütle debisi [kg/s]
- R = 0.287 kJ/kg·K
- T₁ = giriş sıcaklığı [K]
```

Hacimsel formda:
```
W_stage = (n/(n-1)) × P₁ × V̇ × [(P₂/P₁)^((n-1)/n) - 1]

Burada P₁ [kPa], V̇ [m³/s] → W [kW]
```

### 2.2 Optimal Ara Basınçlar (N Kademe)

Eşit basınç oranı kuralı:
```
r_stage = (P_final / P_initial)^(1/N)

Ara basınçlar:
P_k = P_initial × r_stage^k     (k = 0, 1, 2, ..., N)
```

İki kademe için:
```
P_intermediate = √(P₁ × P₂)
```

Üç kademe için:
```
P_int1 = P₁ × (P₂/P₁)^(1/3)
P_int2 = P₁ × (P₂/P₁)^(2/3)
```

### 2.3 N Kademeli Toplam İş (Mükemmel Intercooling)

Tüm kademelerde eşit basınç oranı ve T₁'e geri soğutma varsayımı:
```
W_total = N × (n/(n-1)) × ṁ × R × T₁ × [r_stage^((n-1)/n) - 1]
```

### 2.4 Çok Kademeli Tasarruf

Tek kademeye kıyasla tasarruf:
```
Tasarruf(%) = [1 - N × (r^(1/N·(n-1)/n) - 1) / (r^((n-1)/n) - 1)] × 100

Burada r = P_final / P_initial (toplam basınç oranı)
```

| Toplam Basınç Oranı | 2 Kademe Tasarruf | 3 Kademe Tasarruf |
|---------------------|------------------|------------------|
| 7:1 (7 bar) | %10-14 | %13-17 |
| 10:1 (10 bar) | %14-17 | %17-22 |
| 20:1 (20 bar) | %18-22 | %22-28 |
| 40:1 (40 bar) | %22-28 | %30-35 |

## 3. Politropik Verim

### 3.1 Temel Formül

```
η_p = [(k-1)/k] × [ln(P₂/P₁)] / [ln(T₂/T₁)]

Burada:
- k = 1.4 (hava için ısı kapasiteleri oranı)
- T₂ = gerçek çıkış sıcaklığı [K]
- T₁ = giriş sıcaklığı [K]
```

### 3.2 Politropik İndeks ile İlişki

```
(n-1)/n = (k-1) / (k × η_p)

Burada n = politropik indeks
```

### 3.3 Politropik-İzentropik Verim İlişkisi

Sıkıştırma için (P₂ > P₁):
```
η_isentropic = [r^((k-1)/k) - 1] / [r^((k-1)/(k·η_p)) - 1]

Burada r = P₂/P₁
```

**Önemli:** Kompresörlerde η_polytropic > η_isentropic'tir (türbinlerde tersi). Fark, basınç oranı arttıkça büyür.

| Basınç Oranı | η_polytropic | η_isentropic |
|-------------|-------------|-------------|
| 3:1 | %85 | %83.5 |
| 5:1 | %85 | %82.0 |
| 8:1 | %85 | %80.0 |
| 10:1 | %85 | %78.8 |

### 3.4 Kompresör Tipine Göre Politropik Verim

| Kompresör Tipi | Tipik η_p Aralığı |
|----------------|-------------------|
| Vidalı (yağlı) | %72-85 |
| Vidalı (yağsız) | %65-80 |
| Pistonlu (tek etkili) | %70-82 |
| Pistonlu (çift etkili) | %75-88 |
| Scroll | %70-80 |
| Santrifüj (tek kademe) | %78-85 |
| Santrifüj (çok kademe) | %80-88 |

## 4. İzentropik → Exergy Verim Dönüşümü

### 4.1 Doğrudan Exergy Verimi (Tercih Edilen Yöntem)

ExergyLab engine'de kullanılan formül:
```
η_exergy = ṁ × R × T₀ × ln(P₂/P₁) / W_electric
```
Bu formül, ölçülen elektrik gücünü doğrudan kullandığı için en doğru sonucu verir.

### 4.2 İzentropik Verimden Dönüşüm

İzentropik verim bilindiğinde:
```
η_exergy = η_isentropic × [R × T₀ × ln(P₂/P₁)] / [Cp × (T₂s - T₁)]

Burada:
- T₂s = T₁ × (P₂/P₁)^((k-1)/k)   (izentropik çıkış sıcaklığı)
- Cp = 1.005 kJ/kg·K (hava için)
- R/Cp = (k-1)/k = 0.2857
```

### 4.3 Sıcaklık Tabanlı Yaklaşım

Yalnızca sıcaklık verileri mevcutsa:
```
η_exergy = [(k-1)/k] × [T₀ × ln(P₂/P₁)] / [T₂_actual - T₁]

Hava için (k = 1.4):
η_exergy = 0.2857 × T₀ × ln(P₂/P₁) / (T₂ - T₁)
```

**DİKKAT:** Bu formül yalnızca gaz entalpisi üzerinden çalışır ve motor/mekanik kayıpları hesaba katmaz. Gerçek elektrik gücü biliniyorsa Bölüm 4.1'deki formül tercih edilmelidir.

## 5. Kaçak Exergy Kaybı

### 5.1 Kaçak Exergy Formülü

```
Ex_leak = ṁ_leak × R × T₀ × ln(P_system / P₀)   [kW]

Burada:
- ṁ_leak = kaçak kütle debisi [kg/s]
- ṁ_leak = V̇_leak_FAD × ρ_std
- V̇_leak_FAD = kaçak debisi, serbest hava eşdeğeri [m³/s]
- P_system = sistem basıncı [kPa, mutlak]
- P₀ = atmosfer basıncı = 101.325 kPa
```

### 5.2 Kaçak Maliyet Formülü

```
Yıllık_maliyet = V̇_leak_FAD × SPC × çalışma_saati × elektrik_fiyatı

Burada:
- V̇_leak_FAD = kaçak debisi [m³/min]
- SPC = sistem spesifik güç tüketimi [kW/(m³/min)]
- çalışma_saati [saat/yıl]
- elektrik_fiyatı [€/kWh]
```

### 5.3 Kaçak Debisi — Delik Çapına Göre (7 bar)

| Delik Çapı (mm) | Kaçak Debisi (l/s FAD) | Yıllık Maliyet* |
|-----------------|----------------------|----------------|
| 0.5 | ~0.2 | ~€100 |
| 1.0 | ~0.8 | ~€400 |
| 2.0 | ~3.1 | ~€1,500 |
| 3.0 | ~7.0 | ~€3,400 |
| 5.0 | ~19.5 | ~€9,500 |
| 10.0 | ~78.0 | ~€38,000 |

*Varsayımlar: 8000 saat/yıl, SPC = 6.5 kW/(m³/min), €0.10/kWh

### 5.4 Sistem Toplam Kaçak Oranı Tespiti

**Tank düşürme testi:**
```
V̇_leak = V_tank × (P_start - P_end) / (t × P_atm)   [m³/min FAD]

Burada:
- V_tank = toplam sistem hacmi (tanklar + borulama) [litre]
- P_start, P_end = gösterge basınçları [bar]
- t = basınç düşme süresi [dakika]
- P_atm = 1.013 bar
```

**Yük/boşta zamanlaması (üretim dışı saatlerde):**
```
Kaçak_yüzdesi = [T_yüklü / (T_yüklü + T_boşta)] × 100   [%]
```

## 6. Sistem Seviyesi Exergy Analizi

### 6.1 Sistem Exergy Girişi

```
Ex_input = Σ(W_kompresör_i) + W_kurutucu + W_yardımcı   [kW]
```
Not: Elektrik saf exergy'dir (%100 exergy içeriği).

### 6.2 Faydalı Exergy Çıkışı

```
Ex_useful = Σ(ṁ_kullanım_j × R × T₀ × ln(P_kullanım_j / P₀))   [kW]
```

### 6.3 Exergy Kayıp Dağılımı

```
Ex_kayıp_toplam = Ex_input - Ex_useful

Bileşenler:
1. Ex_motor      = W_electric × (1 - η_motor)              — Motor kayıpları
2. Ex_sıkıştırma = Tersinmezlik, iç sürtünme, iç kaçak     — Kompresör iç kayıplar
3. Ex_ısı        = Σ(Q_waste_i × (1 - T₀/T_waste_i))       — Atık ısı
4. Ex_kurutucu   = Purge kaybı + ısıtıcı enerji             — Kurutucu kayıpları
5. Ex_basınç     = ṁ_total × R × T₀ × ln(P_komp/P_kullanım) — Dağıtım basınç düşüşü
6. Ex_kaçak      = ṁ_leak × R × T₀ × ln(P_system/P₀)       — Hava kaçakları
7. Ex_kontrol    = W_boşta + W_blowoff + W_modülasyon        — Kontrol kayıpları
8. Ex_uygunsuz   = Uygunsuz kullanım exergy'si               — Açık üfleme, vakum vb.
```

### 6.4 Sistem Exergy Verimi

```
η_system = Ex_useful / Ex_input × 100   [%]
```

| Sistem Durumu | η_system | Açıklama |
|--------------|----------|----------|
| Zayıf yönetilen | %5-15 | Yüksek kaçak, VSD yok, aşırı boyutlu |
| Ortalama endüstriyel | %15-25 | Kısmen optimize |
| İyi yönetilen | %25-35 | Aktif kaçak yönetimi, VSD, iyi kontrol |
| En iyi uygulama | %35-50 | Tam optimize arz ve talep tarafı |
| Teorik maksimum | ~%60-70 | Mükemmel sıkıştırma, sıfır kayıp |

### 6.5 Grassmann Diyagramı (Exergy Akış Diyagramı)

```
Elektrik Girişi (100%)
  ├── Motor kayıpları (%5-8)
  ├── Sıkıştırma tersinmezliği (%30-40) → Atık ısı
  │     └── HRU ile geri kazanılabilir: atık ısının %60-70'i
  ├── Aftercooler termal exergy kaybı (%5-10)
  ├── Kurutucu kayıpları (%2-15, tipe bağlı)
  ├── Dağıtım basınç düşüşü (%3-8)
  ├── Kaçak kayıpları (%15-30)
  ├── Kontrol kayıpları (%5-20, load/unload; ~%0 VSD)
  ├── Uygunsuz kullanım (%0-20, değişken)
  └── Net faydalı exergy (%10-30)
```

## 7. Örnek Hesaplamalar

### 7.1 Temel Exergy Hesabı

**Girdiler:**
- P_electric = 32 kW
- V̇ = 6.2 m³/min = 0.103 m³/s
- P₂ = 7.5 bar(mutlak) = 750 kPa
- T_exhaust = 85°C = 358 K
- Çalışma = 6000 saat/yıl
- Elektrik = €0.10/kWh

**Hesap:**
```
ṁ = 0.103 × 1.2 = 0.124 kg/s

Ex_air = 0.124 × 0.287 × 298.15 × ln(750/101.325)
       = 0.124 × 0.287 × 298.15 × 2.002
       = 21.25 kW

Ex_destroyed = 32 - 21.25 = 10.75 kW

η_ex = 21.25 / 32 × 100 = 66.4%

Ex_heat = 10.75 × (1 - 298.15/358) = 1.80 kW

Yıllık_kayıp = 10.75 × 6000 = 64,500 kWh
Maliyet = 64,500 × 0.10 = €6,450/yıl
```

### 7.2 Çok Kademeli Tasarruf Hesabı

**Senaryo:** 40 bar PET şişirme, tek kademe vs 3 kademe

```
r = 40 (toplam basınç oranı)
n = 1.35 (tipik politropik indeks)

Tek kademe işi ∝ (r^((n-1)/n) - 1) = (40^0.259 - 1) = 2.22

3 kademe:
r_stage = 40^(1/3) = 3.42
W_3kademe ∝ 3 × (3.42^0.259 - 1) = 3 × 0.367 = 1.10

Tasarruf = (1 - 1.10/2.22) × 100 = %50.5
```

### 7.3 Kaçak Exergy Kaybı Hesabı

**Senaryo:** 3 mm delik, 7 bar sistem
```
V̇_leak = 7.0 l/s FAD = 0.42 m³/min FAD
ṁ_leak = (0.42/60) × 1.2 = 0.0084 kg/s

Ex_leak = 0.0084 × 0.287 × 298.15 × ln(8.013/1.013)
        = 0.0084 × 0.287 × 298.15 × 2.07
        = 1.49 kW

Yıllık maliyet = 0.42 × 6.5 × 8000 × 0.10 = €2,184/yıl (enerji bazlı)
```

## Sınırlamalar

1. İdeal gaz kabulü yapılmıştır (yüksek basınçlarda sapma olabilir — >40 bar'da dikkat)
2. Nem etkisi ihmal edilmiştir (nemli havada exergy biraz farklı)
3. Yük değişimi dinamikleri dahil değildir (ortalama kararlı hal analizi)
4. Motor verimi ayrıca modellenmemiştir (elektrik girişi ölçülen değerdir)
5. Politropik formüller sabit n kabulü yapar (gerçekte n basınçla değişebilir)

## Referanslar
- Cengel & Boles, "Thermodynamics: An Engineering Approach," Chapter 7
- Bejan, "Advanced Engineering Thermodynamics"
- Kotas, "The Exergy Method of Thermal Plant Analysis"
- Dincer & Rosen, "Exergy: Energy, Environment and Sustainable Development"
- ASME PTC-10, "Performance Test Code on Compressors and Exhausters"
- Schultz (1962), "The Polytropic Analysis of Centrifugal Compressors," ASME J. Eng. Power
- Saidur et al. (2010), "A review on exergy analysis of industrial sector," Renewable & Sustainable Energy Reviews
