---
title: "Isı Transferinde EGM (Entropy Generation Minimization in Heat Transfer)"
category: factory
equipment_type: factory
keywords: [ısı transferi, entropi üretimi, sıcaklık farkı, S_gen_ΔT, konveksiyon, kondüksiyon, approach temperature]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/bejan_number.md, factory/entropy_generation/heat_exchanger_egm.md]
use_when: ["Isı transferi kaynaklı entropi üretimi hesaplanacakken", "Optimum sıcaklık farkı belirlenecekken", "Isı transferi irreversibility analizi yapılacakken"]
priority: high
last_updated: 2026-02-01
---

# Isı Transferinde EGM (Entropy Generation Minimization in Heat Transfer)

> Son güncelleme: 2026-02-01

## Genel Bakış

Isı transferi, endüstriyel sistemlerde en yaygın tersinmezlik (irreversibility) kaynağıdır. Bir sıcaklık
farkı üzerinden gerçekleşen her ısı akışı, termodinamiğin ikinci yasası gereği entropi üretir ve exergy
yıkar. Entropi Üretimi Minimizasyonu (Entropy Generation Minimization — EGM), Adrian Bejan tarafından
sistematize edilen bu yaklaşım, ısı transferi süreçlerini termodinamik açıdan optimize etmeyi amaçlar.

Bu dosya, kondüksiyon (conduction), konveksiyon (convection) ve radyasyon (radiation) yoluyla
gerçekleşen ısı transferinde entropi üretiminin nasıl hesaplandığını, optimum sıcaklık farkının nasıl
belirlendiğini ve pratik endüstriyel kuralları kapsar.

**Temel ilke:** Sonlu sıcaklık farkı (finite temperature difference) termodinamik bir bedeldir.
Her gereksiz °C farkı, exergy yıkımına ve dolayısıyla ekonomik kayba yol açar.

---

## 1. Sıcaklık Farkından Entropi Üretimi (S_gen from Temperature Difference)

### 1.1 İki Rezervuar Arası Isı Transferi (Heat Transfer Between Two Reservoirs)

**Fiziksel Sezgi (Physical Intuition):**

Yüksek sıcaklıktaki bir kaynaktan düşük sıcaklıktaki bir havuza ısı aktarımı düşünün. Isı kendiliğinden
sıcaktan soğuğa akar — bu doğal bir süreçtir ve tersinmezdir (irreversible). Sıcaklık farkı ne kadar
büyükse, ısının "kalite kaybı" o kadar fazladır. Tıpkı yüksekten düşen suyun potansiyel enerji kaybetmesi
gibi, yüksek sıcaklıktan düşük sıcaklığa akan ısı da exergy kaybeder. Bu kayıp, entropi üretimi
(entropy generation) olarak ölçülür.

Tersinir (reversible) bir ısı transferi yalnızca sonsuz küçük sıcaklık farkında (dT → 0) mümkündür —
pratikte imkansızdır, ancak idealdir.

**Türetim (Derivation):**

Adım 1 — İkinci yasa ifadesi: Bir izole sistemde toplam entropi asla azalmaz.

```
dS_evren = dS_sistem + dS_çevre ≥ 0
```

Adım 2 — Sabit sıcaklıktaki iki rezervuar arasında Q̇ [kW] ısı transferi:

Sıcak rezervuar T_hot [K] sıcaklığında ısı verir:
```
dS_hot = -Q̇ / T_hot    (ısı kaybeden taraf, entropi azalır)
```

Soğuk rezervuar T_cold [K] sıcaklığında ısı alır:
```
dS_cold = +Q̇ / T_cold   (ısı alan taraf, entropi artar)
```

Adım 3 — Toplam entropi üretimi (evren bazında):
```
Ṡ_gen = dS_cold + dS_hot = Q̇ / T_cold - Q̇ / T_hot
```

**Sonuç formülü:**
```
Ṡ_gen_ΔT = Q̇ × (1/T_cold - 1/T_hot)   [kW/K]
```

Burada:
- Q̇ : Isı transfer hızı [kW]
- T_hot : Sıcak kaynak sıcaklığı [K] (mutlak sıcaklık!)
- T_cold : Soğuk havuz sıcaklığı [K]
- Ṡ_gen_ΔT : Sıcaklık farkından kaynaklanan entropi üretim hızı [kW/K]

**Önemli not:** Sıcaklıklar mutlaka Kelvin [K] cinsinden olmalıdır. Celsius kullanmak fiziksel olarak
anlamsız sonuçlar verir.

Adım 4 — Exergy yıkımına (irreversibility) dönüşüm:
```
İ = T₀ × Ṡ_gen_ΔT   [kW]
```

Burada T₀ = 298.15 K (25°C referans çevre sıcaklığı).

### 1.2 Sayısal Örnek: İki Rezervuar (Numerical Example)

**Problem:** Bir kazandan (boiler) proses akışkanına 100 kW ısı aktarılıyor.
- T_hot = 150°C = 423.15 K (kazan tarafı)
- T_cold = 50°C = 323.15 K (proses tarafı)
- T₀ = 25°C = 298.15 K (çevre sıcaklığı)

**Çözüm:**

```
Ṡ_gen_ΔT = Q̇ × (1/T_cold - 1/T_hot)
Ṡ_gen_ΔT = 100 × (1/323.15 - 1/423.15)
Ṡ_gen_ΔT = 100 × (0.003095 - 0.002363)
Ṡ_gen_ΔT = 100 × 0.000732
Ṡ_gen_ΔT = 0.0732 kW/K
```

Exergy yıkımı:
```
İ = T₀ × Ṡ_gen_ΔT = 298.15 × 0.0732 = 21.8 kW
```

**Yorum:** 100 kW'lık ısı transferinde, 100°C'lik sıcaklık farkı nedeniyle 21.8 kW exergy yıkılmaktadır.
Bu, aktarılan ısının %21.8'ine eşdeğer bir termodinamik kayıptır.

### 1.3 Sonlu Sıcaklık Farkının Termodinamik Bedeli (Thermodynamic Cost of Finite ΔT)

**Fiziksel Sezgi:** Her gereksiz sıcaklık farkı derecesi, geri kazanılamaz exergy kaybına neden olur.
Sıcaklık farkını artırmak ısı transferini hızlandırır (daha küçük eşanjör yüzeyi gerekir), ancak bunun
termodinamik bir bedeli vardır. Mühendislik, bu iki çelişen hedef arasında denge kurmaktır.

**Yaklaşım sıcaklığı (approach temperature) başına exergy bedeli:**

Q̇ = 100 kW, T_hot = 120°C (393.15 K) sabit tutularak, farklı T_cold değerleri için hesaplama:

| T_cold [°C] | ΔT [°C] | Ṡ_gen [kW/K] | İ = T₀ × Ṡ_gen [kW] | Exergy kaybı oranı [%] |
|-------------|---------|--------------|---------------------|----------------------|
| 115         | 5       | 0.000033     | 0.010               | 0.010                |
| 110         | 10      | 0.000067     | 0.020               | 0.020                |
| 100         | 20      | 0.000137     | 0.041               | 0.041                |
| 90          | 30      | 0.000211     | 0.063               | 0.063                |
| 80          | 40      | 0.000290     | 0.087               | 0.087                |
| 70          | 50      | 0.000375     | 0.112               | 0.112                |
| 60          | 60      | 0.000467     | 0.139               | 0.139                |
| 50          | 70      | 0.000566     | 0.169               | 0.169                |

**Pratik Kural:** Düşük sıcaklık seviyelerinde (< 100°C) aynı ΔT'nin exergy bedeli, yüksek sıcaklıklara
kıyasla oransal olarak çok daha yüksektir. Çünkü 1/T fonksiyonu düşük sıcaklıklarda daha diktir.

Genel ifade olarak, ΔT << T_ortalama olduğunda yaklaşık:
```
Ṡ_gen_ΔT ≈ Q̇ × (ΔT) / T_ortalama²   [kW/K]
```

Bu yaklaşım, entropi üretiminin ΔT ile doğrusal orantılı, T² ile ters orantılı olduğunu gösterir.

---

## 2. Kondüksiyon ile Entropi Üretimi (Entropy Generation in Conduction)

### 2.1 Fourier Yasası ve EGM (Fourier's Law and EGM)

**Fiziksel Sezgi:** Bir katı duvar boyunca ısı iletimi (conduction), moleküler düzeyde enerji
aktarımıdır. Duvar kalın ve iletkenliği düşükse, aynı ısıyı aktarmak için daha büyük sıcaklık farkı
gerekir ve bu da daha fazla entropi üretir. Entropi üretimi sıcaklık farkının karesiyle orantılıdır —
yani ΔT'yi iki katına çıkarmak entropi üretimini dört katına çıkarır.

**Fourier yasası** (bir boyutlu kararlı hal iletim):
```
Q̇ = k × A × (T_hot - T_cold) / L   [kW]
```

Burada:
- k : Isıl iletkenlik katsayısı (thermal conductivity) [kW/(m·K)]
- A : Isı transfer alanı [m²]
- L : Duvar kalınlığı [m]

**Kondüksiyonda yerel entropi üretimi (local entropy generation):**

Isı akışı yönünde (x yönü), sıcaklık gradyanı boyunca her diferansiyel hacim elemanı dx'te
entropi üretilir. Yerel entropi üretim yoğunluğu:

```
ṡ_gen''' = k × (dT/dx)² / T²   [kW/(m³·K)]
```

**Toplam entropi üretimi (integrated over wall thickness):**

Doğrusal sıcaklık profili varsayımıyla (sabit k):
```
Ṡ_gen_kond = k × A × (T_hot - T_cold)² / (L × T_hot × T_cold)   [kW/K]
```

veya eşdeğer olarak:
```
Ṡ_gen_kond = Q̇ × (T_hot - T_cold) / (T_hot × T_cold)   [kW/K]
```

**Fiziksel Anlam:** Entropi üretimi (ΔT)² ile orantılıdır. Bu, sıcaklık farkını azaltmanın
termodinamik açıdan güçlü bir motivasyon olduğunu gösterir.

### 2.2 Sayısal Örnek: Kazan Duvarı (Boiler Wall Example)

**Problem:** Bir kazanın çelik duvarı üzerinden ısı iletimi:
- k_çelik = 0.050 kW/(m·K)
- A = 10 m²
- L = 0.015 m (15 mm duvar kalınlığı)
- T_hot (iç yüzey) = 200°C = 473.15 K
- T_cold (dış yüzey) = 180°C = 453.15 K

**Çözüm:**

Isı transfer hızı:
```
Q̇ = 0.050 × 10 × (473.15 - 453.15) / 0.015
Q̇ = 0.050 × 10 × 20 / 0.015
Q̇ = 666.7 kW
```

Entropi üretimi:
```
Ṡ_gen = 0.050 × 10 × (20)² / (0.015 × 473.15 × 453.15)
Ṡ_gen = 0.050 × 10 × 400 / (0.015 × 214,393)
Ṡ_gen = 200 / 3215.9
Ṡ_gen = 0.0622 kW/K
```

Exergy yıkımı:
```
İ = 298.15 × 0.0622 = 18.5 kW
```

**Yorum:** 666.7 kW ısı iletiminde sadece 20°C'lik bir duvar ΔT'si 18.5 kW exergy yıkımına neden
olmaktadır. Bu, toplam ısının %2.8'ine karşılık gelir.

### 2.3 Duvar Kalınlığı Optimizasyonu (Wall Thickness Optimization)

**Fiziksel Sezgi:** Yalıtım (insulation) kalınlığını artırmak ısı kaybını azaltır, ancak bir noktadan
sonra yalıtım maliyeti tasarruftan fazla olur. EGM yaklaşımı, optimum yalıtım kalınlığını
termodinamik temelde belirler.

Yalıtımlı bir boru veya duvar için:
- Yalıtım kalınlığı artarsa → Q̇_kayıp azalır → Ṡ_gen_ΔT azalır
- Ancak yalıtım üretimi de exergy gerektirir (embodied exergy)
- Optimum nokta: toplam exergy tüketiminin (operasyonel + yalıtım) minimum olduğu kalınlık

```
L_optimum: dṠ_gen_toplam / dL = 0  noktasında bulunur
```

**Pratik kural:** Endüstriyel uygulamalarda ekonomik yalıtım kalınlığı genellikle
termodinamik optimumun yakınındadır (enerji fiyatı makul olduğunda).

---

## 3. Konveksiyon ile Entropi Üretimi (Entropy Generation in Convection)

### 3.1 Newton Soğutma Yasası ve EGM (Newton's Cooling Law and EGM)

**Fiziksel Sezgi:** Konvektif ısı transferinde, bir yüzey ile üzerinden akan akışkan arasında ısı
alışverişi gerçekleşir. Bu süreçteki entropi üretimi iki kaynaktan gelir:

1. **Isı transferi tersinmezliği (heat transfer irreversibility):** Yüzey ile akışkan arasındaki
   sıcaklık farkından kaynaklanan entropi üretimi
2. **Akışkan sürtünmesi tersinmezliği (fluid friction irreversibility):** Akışkanın hareket etmesi
   için gereken basınç düşüşünden kaynaklanan entropi üretimi

Her ikisi de birlikte değerlendirilmelidir — bu EGM'nin konveksiyondaki temel zorluğudur.

**Newton soğutma yasası:**
```
Q̇ = h × A × (T_s - T_∞)   [kW]
```

Burada:
- h : Konveksiyon ısı transfer katsayısı (convection heat transfer coefficient) [kW/(m²·K)]
- A : Isı transfer yüzey alanı [m²]
- T_s : Yüzey sıcaklığı (surface temperature) [K]
- T_∞ : Akışkan sıcaklığı (fluid/free-stream temperature) [K]

**Konveksiyondan entropi üretimi (sadece ısı transferi bileşeni):**

```
Ṡ_gen_konv = h × A × (T_s - T_∞)² / (T_s × T_∞)   [kW/K]
```

**Fiziksel Anlam:** Kondüksiyondaki gibi, entropi üretimi yine (ΔT)² ile orantılıdır. Konveksiyon
katsayısı h'yi artırmak, aynı Q̇ için daha küçük ΔT gerektireceğinden, entropi üretimini azaltır.
Ancak h'yi artırmak genellikle daha yüksek akış hızı gerektirir, bu da sürtünme kaybını artırır.

### 3.2 İç Akış Konveksiyonu (Internal Flow Convection)

**Fiziksel Sezgi:** Bir boru içinden akan akışkan için (örneğin eşanjör boruları), entropi üretimi
hem ısı transferinden hem de basınç düşüşünden (pressure drop) kaynaklanır. Bu iki mekanizma
birbiriyle çelişir: akış hızını artırmak ısı transfer katsayısını artırır (h ↑, dolayısıyla
Ṡ_gen_ΔT ↓) ancak sürtünme kaybını da artırır (ΔP ↑, dolayısıyla Ṡ_gen_ΔP ↑).

**Toplam entropi üretimi (iki bileşenli):**

```
Ṡ_gen_toplam = Ṡ_gen_ΔT + Ṡ_gen_ΔP   [kW/K]
```

Isı transferi bileşeni:
```
Ṡ_gen_ΔT = Q̇² / (ṁ × c_p × T² × Nu × π × k_f)   [kW/K]
```

Burada:
- ṁ : Kütle debisi [kg/s]
- c_p : Özgül ısı [kJ/(kg·K)]
- Nu : Nusselt sayısı (dimensionless)
- k_f : Akışkan ısıl iletkenliği [kW/(m·K)]

Basınç düşüşü bileşeni:
```
Ṡ_gen_ΔP = (32 × ṁ³ × f × L) / (π² × ρ² × D⁵ × T)   [kW/K]
```

Burada:
- f : Darcy sürtünme faktörü (friction factor) [-]
- L : Boru uzunluğu [m]
- ρ : Akışkan yoğunluğu [kg/m³]
- D : Boru iç çapı [m]

**Nusselt Sayısı İlişkisi (Nusselt Number Relationship):**

Nusselt sayısı, konvektif ısı transferinin iletim ısı transferine oranını ifade eder:
```
Nu = h × D / k_f
```

Türbülanslı akış için Dittus-Boelter korelasyonu:
```
Nu = 0.023 × Re^0.8 × Pr^n
```

n = 0.4 (ısıtma), n = 0.3 (soğutma)

Nu artarsa → h artar → ΔT azalır → Ṡ_gen_ΔT azalır
Ancak Re artarsa → f de artar → ΔP artar → Ṡ_gen_ΔP artar

Bu çelişki, EGM'nin konveksiyondaki temel optimizasyon problemidir.

### 3.3 Sayısal Örnek: Boru İçi Akış (Pipe Flow Example)

**Problem:** Bir eşanjörün boru tarafında su akışı:
- Q̇ = 50 kW ısı transfer hızı
- ṁ = 2.0 kg/s su debisi
- T_giriş = 40°C = 313.15 K
- T_çıkış = 46°C = 319.15 K (ΔT_su = 6°C)
- D = 0.025 m (25 mm boru çapı)
- f = 0.025 (sürtünme faktörü)
- L = 5 m boru uzunluğu
- ρ = 992 kg/m³

Su tarafı ortalama sıcaklık: T_ort = 316.15 K

Entropi üretimi (ısı transferi bileşeni) — basitleştirilmiş hesap:

Boru yüzeyi ile su arasındaki ortalama ΔT = 15°C ise:
```
T_s_ort ≈ 331.15 K, T_∞_ort ≈ 316.15 K
Ṡ_gen_ΔT ≈ Q̇ × (T_s - T_∞) / (T_s × T_∞)
Ṡ_gen_ΔT ≈ 50 × 15 / (331.15 × 316.15)
Ṡ_gen_ΔT ≈ 750 / 104,672
Ṡ_gen_ΔT ≈ 0.00717 kW/K
```

Basınç düşüşü bileşeni:
```
ΔP = f × (L/D) × (ρ × v²/2)
v = ṁ / (ρ × A) = 2.0 / (992 × π × 0.025²/4) = 2.0 / (992 × 0.000491) = 4.11 m/s
ΔP = 0.025 × (5/0.025) × (992 × 4.11²/2) = 5 × 200 × 8,379 = ... → basitleştirilmiş
Ṡ_gen_ΔP = ṁ × ΔP / (ρ × T_ort) ≈ küçük değer (genellikle Ṡ_gen_ΔT'nin %5-15'i)
```

**Yorum:** Tipik endüstriyel ısı eşanjörlerinde, ısı transferi kaynaklı entropi üretimi
basınç düşüşü kaynaklı olandan genellikle 5-20 kat daha büyüktür. Ancak yüksek viskoziteli
akışkanlarda veya çok uzun boru hatlarında basınç düşüşü baskın hale gelebilir.

---

## 4. Radyasyon ile Entropi Üretimi (Entropy Generation in Radiation)

### 4.1 Stefan-Boltzmann Yasası ve EGM (Stefan-Boltzmann Law and EGM)

**Fiziksel Sezgi:** Radyasyonla (thermal radiation) ısı transferi, diğer mekanizmalardan temelden
farklıdır. Fotonlar (photons) taşıyıcıdır ve radyasyonun kendisi bir entropi taşır. Madde
entropisi ile radyasyon entropisi farklı hesaplanır. Bu nedenle, radyasyondaki entropi üretimi
hesabı kondüksiyon ve konveksiyona göre daha karmaşıktır.

**Stefan-Boltzmann yasası (net radyasyon):**
```
Q̇_rad = ε × σ × A × (T_hot⁴ - T_cold⁴)   [kW]
```

Burada:
- ε : Yayınırlık (emissivity) [-] (0 < ε ≤ 1)
- σ : Stefan-Boltzmann sabiti = 5.67 × 10⁻¹¹ kW/(m²·K⁴)
- T_hot, T_cold : Yüzey sıcaklıkları [K]

**Radyasyonun entropi akısı (entropy flux of radiation):**

Siyah cisim (blackbody) radyasyonunun entropi akısı:
```
L_rad = (4/3) × σ × T³   [kW/(m²·K)]
```

Bu, madde entropi akısından (Q̇/T) farklıdır — 4/3 çarpanı radyasyonun termodinamik doğasından gelir.

**Radyasyonda entropi üretimi:**

İki yüzey arasındaki radyasyon ısı transferinde entropi üretimi:
```
Ṡ_gen_rad = Q̇_rad × (1/T_cold - 1/T_hot) + (radyasyon entropi düzeltmesi)
```

Basitleştirilmiş form (mühendislik uygulamaları için):
```
Ṡ_gen_rad ≈ ε × σ × A × [(T_hot⁴ - T_cold⁴) × (1/T_cold - 1/T_hot)
             + (4/3) × (T_cold³ - T_hot³ + T_hot⁴/T_cold - T_cold⁴/T_hot) × ...]
```

Pratikte tam formül karmaşık olduğundan, endüstriyel uygulamalarda genellikle şu yaklaşım kullanılır:

**Mühendislik yaklaşımı:**
```
Ṡ_gen_rad ≈ Q̇_rad × (1/T_cold - 1/T_hot)   [kW/K]
```

Bu yaklaşım, T_hot ve T_cold arasındaki fark çok büyük olmadığında (%20-30 hata payı ile) kabul
edilebilir sonuçlar verir.

### 4.2 Radyasyon vs Madde Entropisi Karşılaştırma

| Özellik                | Madde (Matter)   | Radyasyon (Radiation) |
|------------------------|------------------|-----------------------|
| Entropi akısı          | Q̇ / T           | (4/3) × σ × T³ × A   |
| Sıcaklık bağımlılığı   | T⁻¹             | T³                    |
| Taşıyıcı              | Moleküller       | Fotonlar              |
| Geri dönüşümlülük      | Çeşitli         | Genellikle yüksek     |
| Endüstriyel ilgi       | Tüm sistemler   | Fırınlar, kazanlar    |

**Pratik not:** Radyasyon entropi üretimi özellikle şu endüstriyel uygulamalarda önemlidir:
- Yüksek sıcaklık fırınları (> 500°C)
- Kazan yanma odaları
- Cam ve çimento endüstrisi
- Güneş enerjisi kolektörleri

---

## 5. Optimum ΔT Kavramı (Optimal Temperature Difference Concept)

### 5.1 Maliyet-Entropi Trade-off (Cost-Entropy Trade-off)

**Fiziksel Sezgi:** Isı eşanjörü (heat exchanger) tasarımında temel bir çelişki vardır:

- **ΔT artarsa:**
  - Isı transfer alanı A azalır → ekipman maliyeti düşer (C_ekipman ↓)
  - Ancak Ṡ_gen artar → exergy yıkımı artar → işletme maliyeti artar (C_exergy ↑)

- **ΔT azalırsa:**
  - Isı transfer alanı A artar → ekipman maliyeti yükselir (C_ekipman ↑)
  - Ancak Ṡ_gen azalır → exergy yıkımı azalır → işletme maliyeti düşer (C_exergy ↓)

Bu iki çelişen eğilim, bir optimum noktanın varlığını garanti eder.

**Toplam maliyet fonksiyonu:**
```
C_toplam = C_ekipman(A) + C_exergy(Ṡ_gen)
```

Isı transfer alanı ile ΔT ilişkisi:
```
A = Q̇ / (U × ΔT_lm)
```

Burada U: toplam ısı geçiş katsayısı [kW/(m²·K)], ΔT_lm: logaritmik ortalama sıcaklık farkı [K].

Ekipman maliyeti (basitleştirilmiş):
```
C_ekipman ≈ a + b × A^n   [TL/yıl, amortize edilmiş]
```

Exergy maliyeti:
```
C_exergy = c_ex × T₀ × Ṡ_gen × t_çalışma   [TL/yıl]
```

Burada c_ex: exergy birim fiyatı [TL/kWh], t_çalışma: yıllık çalışma süresi [saat/yıl].

### 5.2 Ṡ_gen vs ΔT Eğrisi Açıklaması (S_gen vs ΔT Curve — Text-Based)

Toplam maliyet (veya toplam tersinmezlik) eğrisi U-şekilli (U-shaped) bir profil çizer:

```
Toplam Maliyet
    |
    |  \                          /
    |   \                        /
    |    \                      /    ← C_ekipman (alan maliyeti)
    |     \                    /
    |      \        ___       /
    |       \      /   \     /
    |        \    /     \   /
    |         \  /       \ /
    |          \/         \         ← C_toplam (U-eğrisi)
    |          *  Optimum  \
    |         / \           \
    |        /   \
    |       /     ← C_exergy (entropi bedeli)
    |      /
    |     /
    +-----|-------*----------|----- ΔT
        küçük   ΔT_opt     büyük
        ΔT                   ΔT
```

**Eğri yorumu:**
- Sol taraf (küçük ΔT): Ekipman maliyeti baskın — çok büyük eşanjör gerekiyor
- Sağ taraf (büyük ΔT): Exergy yıkım maliyeti baskın — çok fazla entropi üretiliyor
- Minimum nokta (ΔT_opt): Toplam maliyetin en düşük olduğu optimum yaklaşım sıcaklığı

### 5.3 Optimum Approach Temperature Hesaplama (Optimal Approach Temperature Calculation)

**Genel Metodoloji:**

Adım 1 — Toplam maliyet fonksiyonunu oluştur:
```
C_toplam(ΔT) = C_ekipman(ΔT) + C_exergy(ΔT)
```

Adım 2 — Minimum noktayı bul:
```
dC_toplam / dΔT = 0
```

Adım 3 — İkinci türev kontrolü:
```
d²C_toplam / dΔT² > 0  (minimum olduğunu doğrula)
```

**Basitleştirilmiş analitik çözüm** (sabit U, doğrusal maliyet varsayımı):

```
ΔT_opt ≈ √(b × U × Q̇ / (c_ex × T₀ × t_çalışma))
```

**Farklı Uygulamalar İçin Tipik Optimum Approach Temperature Değerleri:**

| Uygulama                          | Tipik ΔT_opt [°C] | Gerekçe                          |
|-----------------------------------|--------------------|----------------------------------|
| Gaz-gaz eşanjör (gas-gas HX)     | 25 - 40            | Düşük h, büyük alan gereksinimi  |
| Gaz-sıvı eşanjör (gas-liquid HX) | 15 - 25            | Orta h değerleri                 |
| Sıvı-sıvı eşanjör (liquid-liquid)| 5 - 15             | Yüksek h, kompakt tasarım        |
| Buharlaştırıcı (evaporator)      | 3 - 8              | Faz değişimi, yüksek h           |
| Yoğuşturucu (condenser)          | 3 - 8              | Faz değişimi, yüksek h           |
| Kazan ekonomizer (economizer)     | 15 - 25            | Baca gazı → su, korozyon sınırı  |
| Chiller evaporatör                | 3 - 5              | COP hassasiyeti yüksek           |
| Chiller kondenser                 | 5 - 10             | COP hassasiyeti yüksek           |
| Hava soğutucu (air cooler)       | 10 - 20            | Hava tarafı direnci yüksek       |
| Atık ısı geri kazanım (WHR)      | 10 - 30            | Kaynak kalitesine bağlı          |

**Önemli:** Bu değerler genel kılavuzdur. Gerçek optimum, enerji fiyatları, ekipman maliyeti ve
çalışma koşullarına bağlıdır.

---

## 6. Pratik Kurallar (Rules of Thumb)

### 6.1 Her 10°C Approach Temperature Artışının Exergy Bedeli

**Fiziksel Sezgi:** Mühendisler için hızlı karar verme aracı olarak, farklı ΔT değerlerinde
oluşan exergy kaybı aşağıda tablo halinde verilmiştir. Bu değerler, tipik bir endüstriyel
ortamda (T₀ = 25°C = 298.15 K) hesaplanmıştır.

**Tablo: ΔT'ye bağlı entropi üretimi ve exergy kaybı**

Referans: Q̇ = 100 kW, T_ortalama = 100°C = 373.15 K

| ΔT [°C] | Ṡ_gen [kW/K] | İ = T₀ × Ṡ_gen [kW] | Exergy kayıp oranı [%] | Yıllık kayıp* [MWh] |
|---------|--------------|---------------------|----------------------|---------------------|
| 5       | 0.00359      | 1.07                | 1.07                 | 8.6                 |
| 10      | 0.00718      | 2.14                | 2.14                 | 17.1                |
| 15      | 0.01078      | 3.21                | 3.21                 | 25.7                |
| 20      | 0.01438      | 4.29                | 4.29                 | 34.3                |
| 25      | 0.01799      | 5.36                | 5.36                 | 42.9                |
| 30      | 0.02160      | 6.44                | 6.44                 | 51.5                |
| 40      | 0.02884      | 8.60                | 8.60                 | 68.8                |
| 50      | 0.03611      | 10.77               | 10.77                | 86.1                |

*Yıllık çalışma: 8,000 saat/yıl varsayımı

**Farklı sıcaklık seviyelerine göre exergy bedeli (Q̇ = 100 kW, ΔT = 10°C):**

| T_ortalama [°C] | T_ortalama [K] | Ṡ_gen [kW/K] | İ [kW]  | Exergy kayıp oranı [%] |
|-----------------|----------------|--------------|---------|----------------------|
| 50              | 323.15         | 0.00958      | 2.86    | 2.86                 |
| 75              | 348.15         | 0.00824      | 2.46    | 2.46                 |
| 100             | 373.15         | 0.00718      | 2.14    | 2.14                 |
| 150             | 423.15         | 0.00559      | 1.67    | 1.67                 |
| 200             | 473.15         | 0.00447      | 1.33    | 1.33                 |
| 300             | 573.15         | 0.00305      | 0.91    | 0.91                 |
| 500             | 773.15         | 0.00167      | 0.50    | 0.50                 |

**Kritik sonuç:** Aynı ΔT (10°C), düşük sıcaklıklarda (50°C civarı) yüksek sıcaklıklara (500°C)
göre yaklaşık 6 kat daha fazla exergy yıkımına neden olur. Bu nedenle, chiller ve soğutma
sistemlerinde approach temperature optimizasyonu özellikle önemlidir.

### 6.2 Endüstriyel Uygulamalar İçin Tipik Ṡ_gen_ΔT Değerleri

**Tablo: Ekipman bazında tipik ısı transferi entropi üretimi**

| Ekipman Türü                | Tipik Q̇ [kW] | Tipik ΔT [°C] | Ṡ_gen_ΔT [kW/K] | İ [kW] | Yıllık maliyet** |
|-----------------------------|---------------|---------------|------------------|--------|-----------------|
| Buhar kazanı (steam boiler) | 2,000         | 30 - 80       | 0.12 - 0.45     | 36-134 | 50,000-190,000  |
| Kondensing kazan            | 500           | 10 - 25       | 0.02 - 0.06     | 6-18   | 8,000-25,000    |
| Chiller evaporatör          | 300           | 3 - 8         | 0.008 - 0.022   | 2.4-6.6| 3,500-9,500     |
| Chiller kondenser           | 350           | 5 - 12        | 0.012 - 0.030   | 3.6-9.0| 5,000-13,000    |
| Kabuk-boru eşanjör (S&T HX)| 500           | 10 - 30       | 0.03 - 0.10     | 9-30   | 12,000-42,000   |
| Plakalı eşanjör (plate HX) | 500           | 3 - 10        | 0.009 - 0.03    | 2.7-9  | 3,800-12,600    |
| Soğutma kulesi (cooling tw.)| 1,000         | 5 - 15        | 0.04 - 0.12     | 12-36  | 17,000-50,000   |
| Ekonomizer (economizer)     | 300           | 15 - 40       | 0.02 - 0.07     | 6-21   | 8,400-29,000    |
| Hava ön ısıtıcı (air preh.)| 400           | 20 - 50       | 0.04 - 0.12     | 12-36  | 17,000-50,000   |

**Yıllık maliyet: 8,000 saat/yıl, exergy birim fiyatı ≈ 0.18 TL/kWh varsayımı (2026 yılı)

**Gözlem:** Plakalı eşanjörler, kabuk-boru eşanjörlerine göre 3-5 kat daha düşük approach temperature
ile çalışabilir ve dolayısıyla entropi üretimi önemli ölçüde azaltılabilir.

---

## 7. Çok Akışlı Sistemler (Multi-stream Systems)

### 7.1 Çok Akışlı Entropi Üretimi (Multi-stream Entropy Generation)

**Fiziksel Sezgi:** Gerçek endüstriyel tesislerde genellikle birden fazla sıcak ve soğuk akış
(multiple hot and cold streams) vardır. Her akış çifti arasındaki ısı transferi ayrı ayrı
entropi üretir. Toplam entropi üretimi, tüm bu çiftlerin toplamıdır. Bu noktada EGM, Pinch
Analizi (Pinch Analysis) ile kesişir.

**N adet akış çifti için toplam entropi üretimi:**

```
Ṡ_gen_toplam = Σᵢ Ṡ_gen_i = Σᵢ Q̇ᵢ × (1/T_cold_i - 1/T_hot_i)   [kW/K]
```

Her akış çifti i için:
- Q̇ᵢ : i-inci çiftteki ısı transfer hızı [kW]
- T_hot_i : i-inci sıcak akış sıcaklığı [K]
- T_cold_i : i-inci soğuk akış sıcaklığı [K]

### 7.2 Pinch Analizi ile EGM Bağlantısı (Connection to Pinch Analysis)

**Fiziksel Sezgi:** Pinch analizi, ısı eşanjör ağının (Heat Exchanger Network — HEN) minimum
enerji gereksinimini belirler. EGM ise bu ağın minimum entropi üretimini belirler. İkisi
birbirini tamamlar:

- **Pinch analizi:** "Minimum ne kadar ısı (Q̇_min) gerekir?" → Enerji hedefi (energy target)
- **EGM:** "Bu ısı transferi minimum ne kadar entropi üretir?" → Entropi hedefi (entropy target)

**Pinch noktasının EGM yorumu:**

Pinch noktası (pinch point), sıcak ve soğuk bileşik eğrilerin (composite curves) en yakın
olduğu noktadır. Pinch noktasındaki minimum yaklaşım sıcaklığı (ΔT_min) arttıkça:

```
ΔT_min ↑  →  Q̇_utility ↑ (daha fazla dış enerji gerekir)
           →  A_eşanjör ↓ (daha küçük eşanjör alanı)
           →  Ṡ_gen ↑ (daha fazla entropi üretimi)
```

```
ΔT_min ↓  →  Q̇_utility ↓ (daha az dış enerji gerekir)
           →  A_eşanjör ↑ (daha büyük eşanjör alanı)
           →  Ṡ_gen ↓ (daha az entropi üretimi)
```

Optimum ΔT_min, toplam yıllık maliyeti (enerji + ekipman amortismanı + entropi bedeli) minimize eder.

### 7.3 Sayısal Örnek: Üç Akışlı Sistem (Three-stream Example)

**Problem:** Bir gıda fabrikasında aşağıdaki ısı transferleri gerçekleşmektedir:

| Akış çifti | Q̇ [kW] | T_hot [°C/K]    | T_cold [°C/K]   |
|-----------|---------|-----------------|-----------------|
| 1         | 200     | 120 / 393.15    | 80 / 353.15     |
| 2         | 150     | 90 / 363.15     | 60 / 333.15     |
| 3         | 100     | 70 / 343.15     | 40 / 313.15     |

**Çözüm:**

Akış çifti 1:
```
Ṡ_gen_1 = 200 × (1/353.15 - 1/393.15) = 200 × (0.002832 - 0.002544) = 200 × 0.000288 = 0.0576 kW/K
```

Akış çifti 2:
```
Ṡ_gen_2 = 150 × (1/333.15 - 1/363.15) = 150 × (0.003002 - 0.002754) = 150 × 0.000248 = 0.0372 kW/K
```

Akış çifti 3:
```
Ṡ_gen_3 = 100 × (1/313.15 - 1/343.15) = 100 × (0.003193 - 0.002914) = 100 × 0.000279 = 0.0279 kW/K
```

Toplam:
```
Ṡ_gen_toplam = 0.0576 + 0.0372 + 0.0279 = 0.1227 kW/K
```

Toplam exergy yıkımı:
```
İ_toplam = 298.15 × 0.1227 = 36.6 kW
```

**Yorum:** 450 kW toplam ısı transferinde 36.6 kW exergy yıkılmaktadır (%8.1). En büyük katkı
akış çifti 1'den gelmektedir (0.0576 kW/K, toplam entropi üretiminin %47'si). Bunun nedeni hem
en yüksek Q̇ değerine sahip olması hem de en büyük ΔT'ye (40°C) sahip olmasıdır. İyileştirme
önceliği bu akış çiftine verilmelidir.

### 7.4 Çok Akışlı Optimizasyon Stratejisi

1. **Akış çiftlerini Ṡ_gen değerlerine göre sırala** — en yüksek entropi üreteni öncelikle ele al
2. **ΔT'yi azalt** — daha büyük veya daha verimli eşanjör kullan
3. **Isı entegrasyonunu artır** — atık ısıyı başka akışlarla eşleştir (pinch kurallarına uyarak)
4. **Kademeli ısı transferi** — büyük ΔT'li tek eşanjör yerine, kademeli küçük ΔT'li seri eşanjörler
5. **Isı pompaları** — pinch noktası etrafında, termodinamik açıdan uygun ise

---

## 8. Isı Transferi Mekanizmalarının Karşılaştırması (Comparison of Heat Transfer Mechanisms)

### 8.1 Entropi Üretimi Formülleri Özet Tablosu

| Mekanizma                    | Ṡ_gen Formülü                                          | ΔT Bağımlılığı | Anahtar Parametre    |
|-----------------------------|---------------------------------------------------------|----------------|---------------------|
| İki rezervuar (two-res.)    | Q̇ × (1/T_cold - 1/T_hot)                              | ~ΔT/T²         | Q̇, ΔT              |
| Kondüksiyon (conduction)    | k×A×(ΔT)²/(L×T_hot×T_cold)                            | (ΔT)²          | k, L, A             |
| Konveksiyon (convection)    | h×A×(T_s-T_∞)²/(T_s×T_∞)                              | (ΔT)²          | h, A                |
| İç akış (pipe flow)        | Ṡ_gen_ΔT + Ṡ_gen_ΔP                                    | (ΔT)² + ΔP     | Nu, f, Re           |
| Radyasyon (radiation)       | ≈ Q̇_rad × (1/T_cold - 1/T_hot) + düzeltme             | T⁴ farkları    | ε, A                |

### 8.2 Hangi Mekanizma Ne Zaman Baskındır?

| Sıcaklık Aralığı | Baskın Mekanizma              | Endüstriyel Örnek                |
|-------------------|-------------------------------|----------------------------------|
| T > 800°C         | Radyasyon (%60-80)            | Çimento fırını, cam fırını       |
| 200°C < T < 800°C | Radyasyon + Konveksiyon       | Buhar kazanı yanma odası         |
| 50°C < T < 200°C  | Konveksiyon (%70-90)          | Eşanjörler, ekonomizerler        |
| T < 50°C          | Konveksiyon + Kondüksiyon     | Chiller, soğutma sistemleri      |

---

## 9. EGM ile Tasarım İyileştirme Örnekleri (Design Improvement Examples with EGM)

### 9.1 Eşanjör Approach Temperature İyileştirme

**Mevcut durum:** Kabuk-boru eşanjör, ΔT_approach = 25°C, Q̇ = 500 kW

```
T_hot = 120°C (393.15 K), T_cold = 95°C (368.15 K)
Ṡ_gen_mevcut = 500 × (1/368.15 - 1/393.15) = 500 × 0.000173 = 0.0865 kW/K
İ_mevcut = 298.15 × 0.0865 = 25.8 kW
```

**İyileştirilmiş durum:** Plakalı eşanjöre geçiş, ΔT_approach = 8°C

```
T_hot = 120°C (393.15 K), T_cold = 112°C (385.15 K)
Ṡ_gen_yeni = 500 × (1/385.15 - 1/393.15) = 500 × 0.0000529 = 0.0265 kW/K
İ_yeni = 298.15 × 0.0265 = 7.9 kW
```

**Tasarruf:**
```
ΔṠ_gen = 0.0865 - 0.0265 = 0.0600 kW/K
Δİ = 25.8 - 7.9 = 17.9 kW (exergy tasarrufu)
Yıllık tasarruf = 17.9 × 8,000 × 0.18 / 1000 = 25.8 MWh × 0.18 TL/kWh = ... ≈ 25,800 TL/yıl
```

### 9.2 Kademeli Isı Transferi Stratejisi (Staged Heat Transfer)

**Fiziksel Sezgi:** Tek bir büyük ΔT'li eşanjör yerine, birden fazla kademeli eşanjör kullanmak
entropi üretimini önemli ölçüde azaltır. Bunun nedeni, entropi üretiminin (ΔT)² ile orantılı
olmasıdır — büyük bir ΔT'yi küçük parçalara bölmek toplam entropi üretimini azaltır.

**Matematiksel gösterim:**

Tek eşanjör (ΔT toplam):
```
Ṡ_gen_tek ∝ (ΔT)²
```

N kademeli eşanjör (her biri ΔT/N):
```
Ṡ_gen_N = N × (ΔT/N)² = (ΔT)² / N
```

Entropi azalma oranı:
```
Ṡ_gen_N / Ṡ_gen_tek = 1/N
```

**Örnek:** ΔT = 40°C olan bir ısı transferini 4 kademeye bölmek (her kademe 10°C):
```
Entropi üretimi 4 kat azalır → Exergy yıkımı 4 kat azalır
```

Ancak pratikte 4 ayrı eşanjör maliyeti de değerlendirilmelidir (maliyet-performans dengesi).

---

## 10. Sıkça Yapılan Hatalar ve Uyarılar (Common Mistakes and Warnings)

1. **Celsius kullanmak:** Entropi hesaplarında mutlaka Kelvin kullanın. T = 50°C ≠ 50, T = 323.15 K.

2. **Ortalama sıcaklık yaklaşımı:** Değişken sıcaklıklı akışlarda aritmetik ortalama yerine
   logaritmik ortalama sıcaklık farkı (LMTD) kullanın.

3. **Basınç düşüşünü ihmal etmek:** Özellikle yüksek viskoziteli akışkanlarda veya uzun boru
   hatlarında, basınç düşüşü kaynaklı entropi üretimi göz ardı edilmemelidir.

4. **Radyasyonu ihmal etmek:** T > 300°C olan sistemlerde radyasyon katkısı önemli olabilir.

5. **Yerel vs global optimizasyon:** Tek bir eşanjörü optimize etmek, sistem genelinde suboptimal
   olabilir. Her zaman fabrika genelinde EGM yaklaşımı benimsenmelidir.

6. **Sabit çevre sıcaklığı varsayımı:** Mevsimsel değişimler exergy hesaplarını etkiler. Yıllık
   ortalama T₀ veya mevsimsel analiz düşünülmelidir.

---

## İlgili Dosyalar

- `factory/entropy_generation/fundamentals.md` — Entropi üretimi temel kavramları
- `factory/entropy_generation/bejan_number.md` — Bejan sayısı ve tersinmezlik dağılımı
- `factory/entropy_generation/heat_exchanger_egm.md` — Isı eşanjörlerinde EGM uygulaması
- `factory/exergy_fundamentals.md` — Exergy temelleri ve ölü durum tanımı
- `factory/heat_integration.md` — Isı entegrasyonu ve pinch analizi
- `factory/pinch_analysis.md` — Pinch analizi detayları
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanımı
- `factory/cross_equipment.md` — Ekipmanlar arası enerji fırsatları

## Referanslar

1. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press.
2. Bejan, A. (2013). *Convection Heat Transfer*, 4th Edition. Wiley.
3. Çengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition. McGraw-Hill.
4. Herwig, H. & Kock, F. (2007). "Direct and indirect methods of calculating entropy generation rates in turbulent convective heat transfer problems." *Heat and Mass Transfer*, 43(3), 207-215.
5. Naterer, G.F. & Camberos, J.A. (2008). *Entropy-Based Design and Analysis of Fluids Engineering Systems*. CRC Press.
6. Hesselgreaves, J.E. (2000). "Rationalisation of second law analysis of heat exchangers." *International Journal of Heat and Mass Transfer*, 43(22), 4189-4204.
7. Wenterodt, T. & Herwig, H. (2014). "The Entropic Potential Concept: a New Way to Look at Energy Transfer Operations." *Entropy*, 16(4), 2071-2084.
8. Sciubba, E. (2005). "From Engineering Economics to Extended Exergy Accounting." *Energy*, 30(11-12), 2168-2182.
