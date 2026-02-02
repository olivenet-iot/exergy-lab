---
title: "Çözümlü Örnek: Boru Çapı Optimizasyonu (Worked Example: Pipe Sizing Optimization)"
category: factory
equipment_type: factory
keywords: [boru çapı, D_opt, çözümlü örnek, pompalama maliyeti, sürtünme, entropi üretimi]
related_files: [factory/entropy_generation/pipe_flow_egm.md, factory/entropy_generation/fluid_flow_egm.md, pump/formulas.md]
use_when: ["Boru çapı EGM optimizasyonu örneği gerektiğinde", "D_opt hesaplama pratiği yapılacakken"]
priority: high
last_updated: 2026-02-01
---

# Çözümlü Örnek: Boru Çapı Optimizasyonu (Worked Example: Pipe Sizing Optimization)

> Son güncelleme: 2026-02-01

Bu çözümlü örnek, Entropi Üretiminin Minimizasyonu (Entropy Generation Minimization — EGM) yaklaşımını kullanarak endüstriyel bir su hattında optimum boru çapının nasıl belirleneceğini adım adım gösterir. Hesaplamalar gerçek sayısal değerlerle yapılır ve ekonomik analiz ile birleştirilir.

---

## Problem Tanımı

Bir endüstriyel tesiste, 60 °C sıcaklıktaki su bir proses hattı boyunca taşınmaktadır. Sistem parametreleri:

| Parametre | Değer | Birim |
|---|---|---|
| Boru uzunluğu (L) | 100 | m |
| Akışkan | Su (water), 60 °C | — |
| Yoğunluk (ρ) | 983 | kg/m³ |
| Dinamik viskozite (μ) | 4.67 × 10⁻⁴ | Pa·s |
| Özgül ısı (c_p) | 4.18 | kJ/(kg·K) |
| Kütlesel debi (ṁ) | 10 | kg/s |
| Boru malzemesi | Karbon çeliği (carbon steel) | — |
| Yüzey pürüzlülüğü (ε) | 0.045 | mm |
| Yıllık çalışma süresi | 8 000 | h/yıl |
| Elektrik birim fiyatı | 0.10 | €/kWh |
| Pompa verimi (η_pump) | 0.75 | — |
| Referans sıcaklık (T₀) | 298 | K |
| Akışkan sıcaklığı (T) | 333 | K (60 °C) |
| Boru durumu | Yalıtımlı (insulated — adiabatic) | — |

**Not:** Boru yalıtımlı olduğundan yalnızca sürtünme kaynaklı entropi üretimi (friction-induced entropy generation) hesaplanacaktır. Isı transferi bileşeni Ṡ_gen,ısı ≈ 0 kabul edilir.

---

## Çözüm Adımları

### Adım 1 — Standart Boru Çapları Belirleme (Standard Pipe Sizes)

Endüstriyel uygulamalarda standart DN (Diamètre Nominal) çapları kullanılır. Bu örnekte beş aday çap değerlendirilecektir:

| DN | İç çap D_i (mm) | İç çap D_i (m) |
|---|---|---|
| DN80 | 80.1 | 0.0801 |
| DN100 | 105.3 | 0.1053 |
| DN125 | 130.7 | 0.1307 |
| DN150 | 155.1 | 0.1551 |
| DN200 | 206.5 | 0.2065 |

---

### Adım 2 — Her Çap İçin Akış Hızı Hesaplama (Flow Velocity Calculation)

Süreklilik denklemi (continuity equation) ile akış hızı:

```
v = ṁ / (ρ × A) = ṁ / (ρ × π × D² / 4)
```

**DN80:**
```
A = π × (0.0801)² / 4 = 5.038 × 10⁻³ m²
v = 10 / (983 × 5.038 × 10⁻³) = 10 / 4.952 = 2.019 m/s
```

**DN100:**
```
A = π × (0.1053)² / 4 = 8.709 × 10⁻³ m²
v = 10 / (983 × 8.709 × 10⁻³) = 10 / 8.561 = 1.168 m/s
```

**DN125:**
```
A = π × (0.1307)² / 4 = 1.342 × 10⁻² m²
v = 10 / (983 × 1.342 × 10⁻²) = 10 / 13.19 = 0.758 m/s
```

**DN150:**
```
A = π × (0.1551)² / 4 = 1.889 × 10⁻² m²
v = 10 / (983 × 1.889 × 10⁻²) = 10 / 18.57 = 0.539 m/s
```

**DN200:**
```
A = π × (0.2065)² / 4 = 3.350 × 10⁻² m²
v = 10 / (983 × 3.350 × 10⁻²) = 10 / 32.93 = 0.304 m/s
```

**Özet Tablo:**

| DN | D_i (m) | A (m²) | v (m/s) |
|---|---|---|---|
| DN80 | 0.0801 | 5.038 × 10⁻³ | 2.019 |
| DN100 | 0.1053 | 8.709 × 10⁻³ | 1.168 |
| DN125 | 0.1307 | 1.342 × 10⁻² | 0.758 |
| DN150 | 0.1551 | 1.889 × 10⁻² | 0.539 |
| DN200 | 0.2065 | 3.350 × 10⁻² | 0.304 |

**Kontrol:** Endüstriyel su hatlarında önerilen hız aralığı 1.0–3.0 m/s'dir. DN80 üst sınıra yakın, DN200 ise oldukça düşük — bu zaten maliyet dengesinin ipucunu verir.

---

### Adım 3 — Reynolds Sayısı ve Sürtünme Faktörü (Reynolds Number & Friction Factor)

Reynolds sayısı (Reynolds number):

```
Re = ρ × v × D / μ
```

Sürtünme faktörü için Swamee-Jain yaklaşımı (Swamee-Jain approximation) kullanılır. Bu, Colebrook-White denkleminin açık (explicit) formudur ve mühendislik pratiğinde %1 doğruluk sağlar:

```
f = 0.25 / [log₁₀(ε/(3.7×D) + 5.74/Re⁰·⁹)]²
```

**DN80:**
```
Re = 983 × 2.019 × 0.0801 / (4.67 × 10⁻⁴) = 158.87 / (4.67 × 10⁻⁴) = 340 200
ε/D = 0.000045 / 0.0801 = 5.618 × 10⁻⁴
f = 0.25 / [log₁₀(5.618×10⁻⁴/3.7 + 5.74/340200⁰·⁹)]²
f ≈ 0.0188
```

**DN100:**
```
Re = 983 × 1.168 × 0.1053 / (4.67 × 10⁻⁴) = 120.88 / (4.67 × 10⁻⁴) = 258 800
ε/D = 0.000045 / 0.1053 = 4.274 × 10⁻⁴
f ≈ 0.0185
```

**DN125:**
```
Re = 983 × 0.758 × 0.1307 / (4.67 × 10⁻⁴) = 97.35 / (4.67 × 10⁻⁴) = 208 500
ε/D = 0.000045 / 0.1307 = 3.443 × 10⁻⁴
f ≈ 0.0183
```

**DN150:**
```
Re = 983 × 0.539 × 0.1551 / (4.67 × 10⁻⁴) = 82.14 / (4.67 × 10⁻⁴) = 175 900
ε/D = 0.000045 / 0.1551 = 2.901 × 10⁻⁴
f ≈ 0.0182
```

**DN200:**
```
Re = 983 × 0.304 × 0.2065 / (4.67 × 10⁻⁴) = 61.67 / (4.67 × 10⁻⁴) = 132 100
ε/D = 0.000045 / 0.2065 = 2.179 × 10⁻⁴
f ≈ 0.0181
```

**Özet Tablo:**

| DN | Re | ε/D | f |
|---|---|---|---|
| DN80 | 340 200 | 5.62 × 10⁻⁴ | 0.0188 |
| DN100 | 258 800 | 4.27 × 10⁻⁴ | 0.0185 |
| DN125 | 208 500 | 3.44 × 10⁻⁴ | 0.0183 |
| DN150 | 175 900 | 2.90 × 10⁻⁴ | 0.0182 |
| DN200 | 132 100 | 2.18 × 10⁻⁴ | 0.0181 |

**Not:** Tüm durumlar tam türbülanslı akıştır (fully turbulent flow, Re > 4 000). Sürtünme faktörü f, çap arttıkça yalnızca hafifçe azalır çünkü baskın etki hız değişimidir, f değişimi değil.

---

### Adım 4 — Basınç Düşüşü Hesaplama (Pressure Drop Calculation)

Darcy-Weisbach denklemi (Darcy-Weisbach equation):

```
ΔP = f × (L / D) × (ρ × v² / 2)
```

**DN80:**
```
ΔP = 0.0188 × (100 / 0.0801) × (983 × 2.019² / 2)
   = 0.0188 × 1248.4 × 2002.6
   = 47 005 Pa ≈ 47.01 kPa ≈ 0.470 bar
```

**DN100:**
```
ΔP = 0.0185 × (100 / 0.1053) × (983 × 1.168² / 2)
   = 0.0185 × 949.7 × 670.7
   = 11 785 Pa ≈ 11.79 kPa ≈ 0.118 bar
```

**DN125:**
```
ΔP = 0.0183 × (100 / 0.1307) × (983 × 0.758² / 2)
   = 0.0183 × 765.1 × 282.3
   = 3 953 Pa ≈ 3.95 kPa ≈ 0.040 bar
```

**DN150:**
```
ΔP = 0.0182 × (100 / 0.1551) × (983 × 0.539² / 2)
   = 0.0182 × 644.7 × 142.7
   = 1 674 Pa ≈ 1.67 kPa ≈ 0.017 bar
```

**DN200:**
```
ΔP = 0.0181 × (100 / 0.2065) × (983 × 0.304² / 2)
   = 0.0181 × 484.3 × 45.4
   = 398 Pa ≈ 0.40 kPa ≈ 0.004 bar
```

**Özet Tablo:**

| DN | ΔP (Pa) | ΔP (kPa) | ΔP (bar) |
|---|---|---|---|
| DN80 | 47 005 | 47.01 | 0.470 |
| DN100 | 11 785 | 11.79 | 0.118 |
| DN125 | 3 953 | 3.95 | 0.040 |
| DN150 | 1 674 | 1.67 | 0.017 |
| DN200 | 398 | 0.40 | 0.004 |

**Gözlem:** Basınç düşüşü çap ile dramatik biçimde azalır. DN80'den DN200'e geçişte ΔP yaklaşık 118 kat düşer. Bu, ΔP ∝ D⁻⁵ bağıntısından kaynaklanır (sabit ṁ için).

---

### Adım 5 — Entropi Üretimi Hesaplama (Entropy Generation Calculation)

Adyabatik (insulated) boru için sürtünme kaynaklı entropi üretim hızı (friction-induced entropy generation rate):

```
Ṡ_gen = ṁ × ΔP / (ρ × T)
```

Burada T = 333 K (60 °C akışkan sıcaklığı).

**DN80:**
```
Ṡ_gen = 10 × 47 005 / (983 × 333) = 470 050 / 327 339 = 1.436 W/K
```

**DN100:**
```
Ṡ_gen = 10 × 11 785 / (983 × 333) = 117 850 / 327 339 = 0.360 W/K
```

**DN125:**
```
Ṡ_gen = 10 × 3 953 / (983 × 333) = 39 530 / 327 339 = 0.1208 W/K
```

**DN150:**
```
Ṡ_gen = 10 × 1 674 / (983 × 333) = 16 740 / 327 339 = 0.05114 W/K
```

**DN200:**
```
Ṡ_gen = 10 × 398 / (983 × 333) = 3 980 / 327 339 = 0.01216 W/K
```

**Özet Tablo:**

| DN | Ṡ_gen (W/K) | Ṡ_gen (kW/K) |
|---|---|---|
| DN80 | 1.436 | 1.436 × 10⁻³ |
| DN100 | 0.360 | 3.60 × 10⁻⁴ |
| DN125 | 0.1208 | 1.208 × 10⁻⁴ |
| DN150 | 0.05114 | 5.114 × 10⁻⁵ |
| DN200 | 0.01216 | 1.216 × 10⁻⁵ |

**Yorum:** Saf EGM perspektifinden en büyük çap (DN200) en az entropi üretir. Ancak pratik mühendislikte boru maliyeti de göz önüne alınmalıdır — bir sonraki adımlarda ekonomik optimumu bulacağız.

---

### Adım 6 — Exergy Yıkımı ve Yıllık Pompalama Maliyeti (Exergy Destruction & Annual Pumping Cost)

#### 6.1 Exergy Yıkımı (Exergy Destruction)

Gouy-Stodola teoremi (Gouy-Stodola theorem) ile exergy yıkım hızı:

```
İ = T₀ × Ṡ_gen (kW)
```

#### 6.2 Pompalama Gücü (Pumping Power)

```
P_pump = ṁ × ΔP / (ρ × η_pump) (kW)
```

#### 6.3 Yıllık Pompalama Maliyeti (Annual Pumping Cost)

```
C_pump = P_pump × 8000 h × 0.10 €/kWh
```

**DN80:**
```
İ = 298 × 1.436 × 10⁻³ = 0.4279 kW
P_pump = 10 × 47 005 / (983 × 0.75) = 470 050 / 737.25 = 637.7 W = 0.638 kW
C_pump = 0.638 × 8000 × 0.10 = 510 €/yıl
```

**DN100:**
```
İ = 298 × 3.60 × 10⁻⁴ = 0.1073 kW
P_pump = 10 × 11 785 / (983 × 0.75) = 117 850 / 737.25 = 159.9 W = 0.160 kW
C_pump = 0.160 × 8000 × 0.10 = 128 €/yıl
```

**DN125:**
```
İ = 298 × 1.208 × 10⁻⁴ = 0.03600 kW
P_pump = 10 × 3 953 / (983 × 0.75) = 39 530 / 737.25 = 53.62 W = 0.0536 kW
C_pump = 0.0536 × 8000 × 0.10 = 43 €/yıl
```

**DN150:**
```
İ = 298 × 5.114 × 10⁻⁵ = 0.01524 kW
P_pump = 10 × 1 674 / (983 × 0.75) = 16 740 / 737.25 = 22.71 W = 0.0227 kW
C_pump = 0.0227 × 8000 × 0.10 = 18 €/yıl
```

**DN200:**
```
İ = 298 × 1.216 × 10⁻⁵ = 0.003624 kW
P_pump = 10 × 398 / (983 × 0.75) = 3 980 / 737.25 = 5.40 W = 0.0054 kW
C_pump = 0.0054 × 8000 × 0.10 = 4 €/yıl
```

**Özet Tablo:**

| DN | İ (kW) | P_pump (kW) | C_pump (€/yıl) |
|---|---|---|---|
| DN80 | 0.4279 | 0.638 | 510 |
| DN100 | 0.1073 | 0.160 | 128 |
| DN125 | 0.0360 | 0.0536 | 43 |
| DN150 | 0.0152 | 0.0227 | 18 |
| DN200 | 0.0036 | 0.0054 | 4 |

---

### Adım 7 — Boru Maliyeti ve Yıllık Amortisman (Pipe Cost & Annualized Cost)

Tipik endüstriyel karbon çeliği boru fiyatları (montaj dahil, yaklaşık değerler):

| DN | Boru fiyatı (€/m) | Toplam maliyet, 100 m (€) |
|---|---|---|
| DN80 | 35 | 3 500 |
| DN100 | 48 | 4 800 |
| DN125 | 65 | 6 500 |
| DN150 | 82 | 8 200 |
| DN200 | 120 | 12 000 |

Yıllık amortisman (annualized cost) hesabı için sermaye geri kazanım faktörü (Capital Recovery Factor — CRF):

```
CRF = i × (1 + i)ⁿ / [(1 + i)ⁿ − 1]
```

Paramtreler: i = 0.08 (faiz oranı, interest rate), n = 10 yıl (ekonomik ömür, economic life).

```
CRF = 0.08 × (1.08)¹⁰ / [(1.08)¹⁰ − 1]
    = 0.08 × 2.1589 / [2.1589 − 1]
    = 0.17271 / 1.1589
    = 0.14903
```

Yıllık boru maliyeti (annualized pipe cost):

```
C_pipe_yıllık = Toplam maliyet × CRF
```

| DN | Toplam maliyet (€) | C_pipe_yıllık (€/yıl) |
|---|---|---|
| DN80 | 3 500 | 522 |
| DN100 | 4 800 | 715 |
| DN125 | 6 500 | 969 |
| DN150 | 8 200 | 1 222 |
| DN200 | 12 000 | 1 788 |

---

### Adım 8 — Toplam Maliyet ve Optimum Seçim (Total Cost & Optimal Selection)

Toplam yıllık maliyet (total annual cost):

```
C_toplam = C_pipe_yıllık + C_pump_yıllık
```

| DN | C_pipe (€/yıl) | C_pump (€/yıl) | C_toplam (€/yıl) | Ṡ_gen (W/K) |
|---|---|---|---|---|
| DN80 | 522 | 510 | **1 032** | 1.436 |
| DN100 | 715 | 128 | **843** | 0.360 |
| DN125 | 969 | 43 | **1 012** | 0.121 |
| DN150 | 1 222 | 18 | **1 240** | 0.051 |
| DN200 | 1 788 | 4 | **1 792** | 0.012 |

**Ekonomik optimum (economic optimum): DN100** — Toplam yıllık maliyet en düşük: **843 €/yıl**

**Saf EGM optimumu (pure EGM optimum): DN200** — Entropi üretimi en düşük: **0.012 W/K**

### Maliyet Dağılımı Görselleştirmesi (Cost Breakdown Visualization)

```
DN80  |████████████████████████████ 522  |██████████████████████████ 510  | Toplam: 1 032 €
DN100 |████████████████████████████████████ 715  |██████ 128              | Toplam:   843 € ← OPTİMUM
DN125 |████████████████████████████████████████████████ 969  |██ 43       | Toplam: 1 012 €
DN150 |████████████████████████████████████████████████████████████ 1222 |█ 18 | Toplam: 1 240 €
DN200 |████████████████████████████████████████████████████████████████████████████████████████ 1788 | 4 | Toplam: 1 792 €
       [Boru maliyeti — koyu]                                   [Pompalama — açık]
```

**Kritik gözlem:** DN80'de iki maliyet bileşeni neredeyse eşittir (522 vs 510). DN100'de boru maliyeti baskın hale gelir (715 vs 128). Bu dönüm noktası, ekonomik optimumun DN100 civarında olduğunu doğrular.

---

### Adım 9 — Sonuçların Karşılaştırması (Comparison of Results)

| Kriter | Seçim | Gerekçe |
|---|---|---|
| Ekonomik optimum (economic optimum) | DN100 | En düşük toplam yıllık maliyet (843 €/yıl) |
| EGM optimum (minimum Ṡ_gen) | DN200 | En düşük entropi üretimi (0.012 W/K) |
| Hız sınırı uyumu (velocity compliance) | DN80–DN125 | 0.7–2.0 m/s endüstriyel aralıkta |
| Pratik mühendislik önerisi | **DN100 veya DN125** | Güvenlik marjı ile ekonomik optimum |

**Neden ekonomik optimum, EGM optimumundan farklıdır?**

Ekonomik optimum, boru maliyeti (çap arttıkça artar) ile pompalama maliyeti (çap arttıkça azalır) arasındaki dengeyi yansıtır. Saf EGM yaklaşımı yalnızca termodinamik tersinmezliği minimize eder ve malzeme maliyetini dikkate almaz. Gerçek mühendislik kararlarında ekonomik optimum tercih edilir, ancak EGM analizi termodinamik iyileştirme potansiyelini gösterir.

**Önemli pratik kural:** Şüphe durumunda bir üst çapı seçin. Alt boyutlandırmanın (under-sizing) cezası çok daha ağırdır — pompalama maliyeti D⁻⁵ ile artar, boru maliyeti ise yalnızca D ile doğru orantılıdır. Yani küçük bir çap hatası, pompalama maliyetini orantısız biçimde artırır.

---

## Sonuç ve Mühendislik Yorumu

1. **Optimum boru çapı: DN100 (iç çap 105.3 mm)** — Yıllık toplam maliyet 843 €/yıl ile en düşük değerdedir.

2. **Tasarruf potansiyeli:** DN80 yerine DN100 seçildiğinde yıllık **189 €** tasarruf sağlanır (1 032 − 843). DN200 yerine DN100 seçildiğinde ise yıllık **949 €** tasarruf sağlanır (1 792 − 843).

3. **Entropi üretimi azaltma:** DN80'den DN100'e geçişte Ṡ_gen %75 azalır (1.436 → 0.360 W/K). Bu, termodinamik kalitenin önemli ölçüde korunduğunu gösterir.

4. **Exergy yıkımı:** DN100 için İ = 0.107 kW. Bu, T₀ × Ṡ_gen = 298 × 0.360 × 10⁻³ ile doğrulanır. Bu exergy yıkımı, pompanın şaftına iletilen mekanik enerjinin tersinmez biçimde kaybedilen kısmını temsil eder.

5. **Pratik öneri:** DN100 seçimi hem ekonomik hem de termodinamik olarak sağlam bir karardır. Gelecekte debi artışı bekleniyorsa (örn. kapasite genişletme), DN125 seçimi daha uygun olabilir.

---

## Duyarlılık Analizi (Sensitivity Analysis)

### Senaryo A — Elektrik fiyatı iki katına çıkarsa (0.10 → 0.20 €/kWh)

Pompalama maliyeti iki katına çıkar, boru maliyeti değişmez:

| DN | C_pipe (€/yıl) | C_pump (€/yıl) | C_toplam (€/yıl) |
|---|---|---|---|
| DN80 | 522 | 1 020 | 1 542 |
| DN100 | 715 | 256 | **971** |
| DN125 | 969 | 86 | **1 055** |
| DN150 | 1 222 | 36 | 1 258 |
| DN200 | 1 788 | 8 | 1 796 |

**Sonuç:** Optimum hala DN100 kalır, ancak DN100 ile DN125 arasındaki fark daralır (971 vs 1 055). Elektrik fiyatı daha da artarsa (örn. 0.30 €/kWh), optimum DN125'e kayar.

### Senaryo B — Çalışma süresi yarıya düşerse (8 000 → 4 000 h/yıl)

Pompalama maliyeti yarıya düşer, boru maliyeti değişmez:

| DN | C_pipe (€/yıl) | C_pump (€/yıl) | C_toplam (€/yıl) |
|---|---|---|---|
| DN80 | 522 | 255 | **777** |
| DN100 | 715 | 64 | **779** |
| DN125 | 969 | 22 | 991 |
| DN150 | 1 222 | 9 | 1 231 |
| DN200 | 1 788 | 2 | 1 790 |

**Sonuç:** Optimum DN80 ile DN100 arasında neredeyse eşit hale gelir (777 vs 779). Düşük kullanım saatlerinde daha küçük çap ekonomik olarak kabul edilebilir.

### Senaryo C — Debi değişimi: ṁ = 15 kg/s

Debi artışı, basınç düşüşünü ve dolayısıyla pompalama maliyetini dramatik biçimde artırır (ΔP ∝ ṁ²):

| DN | v (m/s) | ΔP (kPa) | C_pump (€/yıl) | C_toplam (€/yıl) |
|---|---|---|---|---|
| DN80 | 3.03 | 105.8 | 1 148 | 1 670 |
| DN100 | 1.75 | 26.5 | 288 | 1 003 |
| DN125 | 1.14 | 8.9 | 97 | **1 066** |
| DN150 | 0.81 | 3.8 | 41 | 1 263 |
| DN200 | 0.46 | 0.9 | 10 | 1 798 |

**Sonuç:** ṁ = 15 kg/s durumunda optimum yine DN100 kalır (1 003 €/yıl), ancak DN80 artık kabul edilemez (v = 3.03 m/s, hız limitinin üzerinde; ayrıca pompalama maliyeti 1 148 €/yıl). Bu, debi artışlarına karşı DN100'ün sağlam bir seçim olduğunu gösterir.

### Ölçekleme İlişkileri (Scaling Relationships)

Sabit sürtünme faktörü varsayımı altında temel ölçekleme ilişkileri:

```
ΔP ∝ ṁ² × D⁻⁵           (basınç düşüşü)
Ṡ_gen ∝ ṁ³ × D⁻⁵         (entropi üretimi)
P_pump ∝ ṁ³ × D⁻⁵         (pompalama gücü)
C_pipe ∝ D¹·⁵              (boru maliyeti, yaklaşık)
```

Bu ilişkiler, D_opt'un ṁ ile nasıl değiştiğini gösterir:

```
D_opt ∝ ṁ^(3/6.5) ≈ ṁ^0.46
```

Yani debi iki katına çıktığında optimum çap yaklaşık %38 artar (2^0.46 ≈ 1.38).

---

## İlgili Dosyalar

- `factory/entropy_generation/pipe_flow_egm.md` — Boru akışı EGM teorisi ve D_opt türetimi
- `factory/entropy_generation/fluid_flow_egm.md` — Akış sistemlerinde genel EGM yaklaşımı
- `pump/formulas.md` — Pompa hesaplama formülleri ve verimlilik tanımları

## Referanslar

1. Bejan, A. (1982). *Entropy Generation through Heat and Fluid Flow.* Wiley.
2. Bejan, A. (1996). *Entropy Generation Minimization.* CRC Press.
3. White, F. M. (2011). *Fluid Mechanics.* 7th Ed., McGraw-Hill.
4. Swamee, P. K. & Jain, A. K. (1976). "Explicit equations for pipe-flow problems." *J. Hydraulics Division, ASCE*, 102(5), 657–664.
5. Peters, M. S. & Timmerhaus, K. D. (2003). *Plant Design and Economics for Chemical Engineers.* 5th Ed., McGraw-Hill.
