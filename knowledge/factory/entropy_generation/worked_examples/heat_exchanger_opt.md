---
title: "Çözümlü Örnek: Eşanjör EGM Optimizasyonu (Worked Example: Heat Exchanger EGM Optimization)"
category: factory
equipment_type: factory
keywords: [eşanjör, çözümlü örnek, S_gen hesaplama, Bejan sayısı, approach temperature, maliyet-entropi]
related_files: [factory/entropy_generation/heat_exchanger_egm.md, factory/entropy_generation/heat_transfer_egm.md, factory/entropy_generation/bejan_number.md]
use_when: ["Eşanjör EGM hesaplama örneği gerektiğinde", "S_gen ayrıştırma pratiği yapılacakken"]
priority: high
last_updated: 2026-02-01
---

# Çözümlü Örnek: Eşanjör EGM Optimizasyonu (Worked Example: Heat Exchanger EGM Optimization)

> Son güncelleme: 2026-02-01

## Genel Bakış

Bu çözümlü örnek, bir karşı akışlı (counter-flow) ısı eşanjöründe (heat exchanger) entropi üretimi
minimizasyonu (EGM) analizinin tüm adımlarını kapsamlı biçimde göstermektedir. Problem, ısı transferi
ve basınç düşüşü kaynaklı entropi üretim bileşenlerinin ayrıştırılmasını, Bejan sayısının yorumlanmasını,
Gouy-Stodola teoremi ile exergy yıkımının hesaplanmasını ve optimum approach temperature belirlenmesini
içermektedir.

**Hedef:** Mühendislerin endüstriyel ısı eşanjörlerinde EGM tabanlı optimizasyonu adım adım
uygulayabilmesi için eksiksiz bir referans sağlamak.

---

## 1. Problem Tanımı (Problem Definition)

Bir endüstriyel tesiste 500 kW kapasiteli karşı akışlı (counter-flow) ısı eşanjörü incelenmektedir.

**Tasarım Verileri:**

| Parametre                          | Sembol       | Değer         | Birim       |
|------------------------------------|-------------|---------------|-------------|
| Isı transfer hızı                  | Q̇           | 500           | kW          |
| Sıcak akışkan giriş sıcaklığı     | T_h,giriş   | 120           | °C (393.15 K) |
| Sıcak akışkan çıkış sıcaklığı     | T_h,çıkış   | 80            | °C (353.15 K) |
| Soğuk akışkan giriş sıcaklığı     | T_c,giriş   | 30            | °C (303.15 K) |
| Soğuk akışkan çıkış sıcaklığı     | T_c,çıkış   | 70            | °C (343.15 K) |
| Sıcak taraf kütle debisi           | ṁ_hot       | 2.99          | kg/s        |
| Soğuk taraf kütle debisi           | ṁ_cold      | 2.99          | kg/s        |
| Özgül ısı (su, her iki taraf)      | c_p         | 4.18          | kJ/(kg·K)  |
| Sıcak taraf basınç düşüşü         | ΔP_hot      | 25            | kPa         |
| Soğuk taraf basınç düşüşü         | ΔP_cold     | 20            | kPa         |
| Su yoğunluğu                       | ρ           | 990           | kg/m³       |
| Referans çevre sıcaklığı           | T₀          | 298           | K (25°C)    |

**Debi doğrulama:**

Her iki tarafta da su kullanıldığından ve sıcaklık farkları eşit olduğundan (ΔT_hot = 40°C,
ΔT_cold = 40°C), enerji dengesi gereği kütle debileri eşittir:

```
Q̇ = ṁ_hot × c_p × (T_h,giriş − T_h,çıkış)
500 = ṁ_hot × 4.18 × (120 − 80)
500 = ṁ_hot × 4.18 × 40
ṁ_hot = 500 / 167.2 = 2.99 kg/s  ✓
```

---

## 2. Adım 1: Ortalama Sıcaklıkları Hesapla (Calculate Mean Temperatures)

Entropi üretimi bileşenlerinin hesaplanabilmesi için her iki akışkanın ortalama sıcaklıklarına
ihtiyaç vardır.

**Sıcak taraf ortalama sıcaklık (hot side mean temperature):**

```
T_hot_avg = (T_h,giriş + T_h,çıkış) / 2
T_hot_avg = (120 + 80) / 2
T_hot_avg = 100°C = 373.15 K
```

**Soğuk taraf ortalama sıcaklık (cold side mean temperature):**

```
T_cold_avg = (T_c,giriş + T_c,çıkış) / 2
T_cold_avg = (30 + 70) / 2
T_cold_avg = 50°C = 323.15 K
```

**Logaritmik ortalama sıcaklık farkı (Log Mean Temperature Difference — LMTD):**

Karşı akışlı eşanjörde:

```
ΔT₁ = T_h,giriş − T_c,çıkış = 120 − 70 = 50°C
ΔT₂ = T_h,çıkış − T_c,giriş = 80 − 30 = 50°C
```

Bu özel durumda ΔT₁ = ΔT₂ olduğundan, LMTD doğrudan aritmetik ortalamaya eşittir:

```
LMTD = 50°C = 50 K
```

> **Not:** ΔT₁ = ΔT₂ olması, dengeli (balanced) bir eşanjör tasarımına işaret eder.
> Her iki tarafta eşit kapasite hızı (ṁ × c_p) bulunmaktadır.

---

## 3. Adım 2: Ṡ_gen,ΔT Hesapla — Isı Transferi Bileşeni (Heat Transfer Component)

Isı transferi kaynaklı entropi üretimi, eşanjördeki sonlu sıcaklık farkından (finite temperature
difference) kaynaklanır. Bu bileşen genellikle toplam entropi üretiminin en büyük kısmını oluşturur.

### 3.1 Yöntem 1: Basitleştirilmiş Yaklaşım (Simplified Approximation)

Bu yöntem, sıcak ve soğuk akışkanları sabit sıcaklıkta birer termal rezervuar olarak modeller:

```
Ṡ_gen,ΔT = Q̇ × (1/T_cold_avg − 1/T_hot_avg)
```

**Adım adım hesaplama:**

```
1/T_cold_avg = 1/323.15 = 0.003095 K⁻¹
1/T_hot_avg  = 1/373.15 = 0.002680 K⁻¹

Fark = 0.003095 − 0.002680 = 0.000415 K⁻¹

Ṡ_gen,ΔT (Yöntem 1) = 500 × 0.000415
Ṡ_gen,ΔT (Yöntem 1) = 0.2077 kW/K
```

### 3.2 Yöntem 2: Detaylı Entropi Dengesi (Detailed Entropy Balance)

Bu yöntem, her akışkanın entropi değişimini ayrı ayrı hesaplar ve daha doğru sonuç verir. Kapalı
sistem entropi dengesi yerine, açık sistem (open system) entropi üretimi kullanılır:

```
Ṡ_gen,ΔT = ṁ_hot × c_p × ln(T_h,çıkış / T_h,giriş) + ṁ_cold × c_p × ln(T_c,çıkış / T_c,giriş)
```

**Fiziksel Sezgi (Physical Intuition):** Sıcak akışkan soğuduğundan entropisi azalır (negatif
katkı), soğuk akışkan ısındığından entropisi artar (pozitif katkı). Toplam entropi üretimi, bu
iki değişimin net farkıdır ve termodinamiğin ikinci yasası gereği her zaman pozitiftir.

**Sıcak taraf entropi değişimi:**

```
ΔṠ_hot = ṁ_hot × c_p × ln(T_h,çıkış / T_h,giriş)
ΔṠ_hot = 2.99 × 4.18 × ln(353.15 / 393.15)
ΔṠ_hot = 12.498 × ln(0.8982)
ΔṠ_hot = 12.498 × (−0.10737)
ΔṠ_hot = −1.3420 kW/K
```

**Soğuk taraf entropi değişimi:**

```
ΔṠ_cold = ṁ_cold × c_p × ln(T_c,çıkış / T_c,giriş)
ΔṠ_cold = 2.99 × 4.18 × ln(343.15 / 303.15)
ΔṠ_cold = 12.498 × ln(1.1320)
ΔṠ_cold = 12.498 × 0.12411
ΔṠ_cold = 1.5512 kW/K
```

**Toplam ısı transferi kaynaklı entropi üretimi:**

```
Ṡ_gen,ΔT (Yöntem 2) = ΔṠ_hot + ΔṠ_cold
Ṡ_gen,ΔT (Yöntem 2) = −1.3420 + 1.5512
Ṡ_gen,ΔT (Yöntem 2) = 0.2092 kW/K
```

### 3.3 İki Yöntemin Karşılaştırması

| Yöntem                  | Ṡ_gen,ΔT [kW/K] | Fark [%]       |
|-------------------------|------------------|----------------|
| Yöntem 1 (basit)        | 0.2077           | Referans       |
| Yöntem 2 (detaylı)      | 0.2092           | +0.72%         |

**Yorum:** İki yöntem arasındaki fark yalnızca %0.72'dir. Bu, sıcaklık aralığının dar olduğu
(ΔT/T_avg küçük) durumlarda basitleştirilmiş yaklaşımın yeterli doğruluğa sahip olduğunu gösterir.
Büyük sıcaklık farkları söz konusu olduğunda (ΔT > 100°C) detaylı yöntem tercih edilmelidir.

**Bundan sonraki hesaplamalarda Yöntem 2'nin sonucu olan Ṡ_gen,ΔT = 0.2092 kW/K kullanılacaktır.**

---

## 4. Adım 3: Ṡ_gen,ΔP Hesapla — Basınç Düşüşü Bileşeni (Pressure Drop Component)

Akışkan sürtünmesi kaynaklı entropi üretimi, basınç düşüşünün (pressure drop) akışkan
sıcaklığında ısıya dönüşmesinden kaynaklanır.

**Genel formül:**

```
Ṡ_gen,ΔP = ṁ × ΔP / (ρ × T_avg)   [kW/K]
```

Burada ΔP [kPa], ρ [kg/m³], T_avg [K] cinsinden kullanılır.

### 4.1 Sıcak Taraf Basınç Düşüşü Kaynaklı Entropi Üretimi

```
Ṡ_gen,ΔP,hot = ṁ_hot × ΔP_hot / (ρ × T_hot_avg)
Ṡ_gen,ΔP,hot = 2.99 × 25 / (990 × 373.15)
Ṡ_gen,ΔP,hot = 74.75 / 369,418.5
Ṡ_gen,ΔP,hot = 0.0002024 kW/K
```

### 4.2 Soğuk Taraf Basınç Düşüşü Kaynaklı Entropi Üretimi

```
Ṡ_gen,ΔP,cold = ṁ_cold × ΔP_cold / (ρ × T_cold_avg)
Ṡ_gen,ΔP,cold = 2.99 × 20 / (990 × 323.15)
Ṡ_gen,ΔP,cold = 59.80 / 319,918.5
Ṡ_gen,ΔP,cold = 0.0001869 kW/K
```

### 4.3 Toplam Basınç Düşüşü Kaynaklı Entropi Üretimi

```
Ṡ_gen,ΔP = Ṡ_gen,ΔP,hot + Ṡ_gen,ΔP,cold
Ṡ_gen,ΔP = 0.0002024 + 0.0001869
Ṡ_gen,ΔP = 0.0003893 kW/K
```

> **Gözlem:** Basınç düşüşü kaynaklı entropi üretimi, ısı transferi kaynaklı olandan yaklaşık
> 537 kat daha küçüktür (0.0003893 vs 0.2092). Bu, sıvı-sıvı eşanjörlerde tipik bir durumdur:
> suyun yüksek yoğunluğu (ρ = 990 kg/m³) basınç düşüşü bileşenini son derece küçük tutar.
> Gaz-gaz eşanjörlerde bu oran çok daha dengelidir.

---

## 5. Adım 4: Toplam Ṡ_gen ve Bejan Sayısı (Total S_gen and Bejan Number)

### 5.1 Toplam Entropi Üretimi

```
Ṡ_gen,toplam = Ṡ_gen,ΔT + Ṡ_gen,ΔP
Ṡ_gen,toplam = 0.2092 + 0.0003893
Ṡ_gen,toplam = 0.2096 kW/K
```

### 5.2 Bejan Sayısı (Bejan Number)

Bejan sayısı, toplam entropi üretiminin ne kadarının ısı transferi kaynaklı olduğunu ifade eder:

```
Be = Ṡ_gen,ΔT / Ṡ_gen,toplam
Be = 0.2092 / 0.2096
Be = 0.9981
```

### 5.3 Bejan Sayısı Yorumu

| Be Değeri | Anlam                              | Mühendislik Aksiyonu                         |
|-----------|------------------------------------|----------------------------------------------|
| Be = 1.0  | Tamamı ısı transferi kaynaklı      | Yalnızca ΔT azaltma                          |
| Be > 0.5  | Isı transferi baskın               | Öncelikle ΔT azaltma                         |
| Be = 0.5  | Denge noktası                      | Her iki tarafı da değerlendir                |
| Be < 0.5  | Sürtünme baskın                    | Öncelikle ΔP azaltma                         |

**Bu eşanjör için yorum:** Be = 0.998 ile entropi üretiminin neredeyse tamamı ısı transferi
kaynaklıdır. Bu, sıvı-sıvı eşanjörler için beklenen bir sonuçtur. İyileştirme stratejisi
kesinlikle sıcaklık farkının (approach temperature) azaltılmasına odaklanmalıdır. Basınç
düşüşü kaynaklı entropi üretimi ihmal edilebilir düzeydedir.

---

## 6. Adım 5: Exergy Yıkımı — Gouy-Stodola Teoremi (Exergy Destruction)

Gouy-Stodola teoremi, entropi üretimini exergy yıkımına (irreversibility) dönüştürür:

```
İ = T₀ × Ṡ_gen,toplam
```

### 6.1 Anlık Exergy Yıkımı

```
İ = 298 × 0.2096
İ = 62.46 kW
```

**Yorum:** 500 kW ısı transferi yapan bu eşanjörde, her an 62.46 kW exergy yıkılmaktadır.
Bu, aktarılan ısının %12.5'ine karşılık gelir — önemli bir termodinamik kayıptır.

### 6.2 Yıllık Exergy Yıkımı ve Maliyet

Yıllık çalışma süresi: t_çalışma = 8,000 saat/yıl
Elektrik birim fiyatı: c_el = 0.18 TL/kWh (2026 yılı endüstriyel tarife tahmini)

```
İ_yıllık = İ × t_çalışma
İ_yıllık = 62.46 × 8,000
İ_yıllık = 499,680 kWh/yıl ≈ 499.7 MWh/yıl
```

Yıllık exergy yıkım maliyeti:

```
C_exergy = İ_yıllık × c_el
C_exergy = 499,680 × 0.18
C_exergy = 89,942 TL/yıl ≈ 90,000 TL/yıl
```

> **Kritik sonuç:** Bu eşanjör yıllık yaklaşık 90,000 TL'lik exergy yıkımına neden olmaktadır.
> Bu bedelin azaltılması, approach temperature optimizasyonu ile mümkündür.

---

## 7. Adım 6: Optimum Approach Temperature Analizi (Optimal Approach Temperature Analysis)

### 7.1 Mevcut Durum

Mevcut karşı akışlı eşanjörde approach temperature (yaklaşım sıcaklığı) değerleri:

```
ΔT_approach,1 = T_h,giriş − T_c,çıkış = 120 − 70 = 50°C   (sıcak giriş − soğuk çıkış)
ΔT_approach,2 = T_h,çıkış − T_c,giriş = 80 − 30 = 50°C    (sıcak çıkış − soğuk giriş)
```

Bu dengeli tasarımda her iki approach temperature eşittir: ΔT_app = 50°C.

### 7.2 Farklı Approach Temperature Değerleri İçin Ṡ_gen Hesabı

Sabit Q̇ = 500 kW ve dengeli (balanced) eşanjör varsayımıyla, approach temperature azaltıldığında
sıcaklık profilleri yaklaşır. Her senaryoda ṁ × c_p × ΔT_akışkan = 500 kW korunur.

**Hesaplama yöntemi:** Her approach temperature ΔT_app için, sıcak ve soğuk akışkan sıcaklıkları
yeniden belirlenir. Dengeli eşanjörde ΔT_approach her iki uçta eşittir.

Sıcak taraf: T_h,giriş = T_c,çıkış + ΔT_app, T_h,çıkış = T_c,giriş + ΔT_app
Soğuk taraf: T_c,giriş = 30°C (sabit), T_c,çıkış = 70°C (sabit)

Dolayısıyla: T_h,giriş = 70 + ΔT_app, T_h,çıkış = 30 + ΔT_app

Her ΔT_app değeri için Ṡ_gen detaylı yöntemle hesaplanır:

```
Ṡ_gen,ΔT = ṁ × c_p × [ln(T_h,çıkış/T_h,giriş) + ln(T_c,çıkış/T_c,giriş)]
```

Soğuk taraf sıcaklıkları sabit olduğundan, soğuk taraf entropi değişimi de sabittir:

```
ΔṠ_cold = 2.99 × 4.18 × ln(343.15/303.15) = 1.5512 kW/K (sabit)
```

| ΔT_app [°C] | T_h,giriş [K] | T_h,çıkış [K] | ΔṠ_hot [kW/K] | Ṡ_gen,ΔT [kW/K] | İ = T₀ × Ṡ_gen [kW] |
|--------------|---------------|----------------|----------------|------------------|---------------------|
| 5            | 348.15        | 308.15         | −1.5137        | 0.0375           | 11.18               |
| 10           | 353.15        | 313.15         | −1.4885        | 0.0627           | 18.68               |
| 15           | 358.15        | 318.15         | −1.4642        | 0.0870           | 25.93               |
| 20           | 363.15        | 323.15         | −1.4406        | 0.1106           | 32.96               |
| 30           | 373.15        | 333.15         | −1.3953        | 0.1559           | 46.46               |
| 50 (mevcut)  | 393.15        | 353.15         | −1.3420        | 0.2092           | 62.34               |

**Eğilim:** Approach temperature arttıkça entropi üretimi ve exergy yıkımı belirgin biçimde
artmaktadır. ΔT_app = 5°C'de exergy yıkımı 11.18 kW iken, ΔT_app = 50°C'de 62.34 kW'a
yükselmektedir — yaklaşık 5.6 kat artış.

### 7.3 Isı Transfer Alanı Tahmini

Eşanjör alanı, approach temperature ile ters orantılıdır:

```
A = Q̇ / (U × LMTD)
```

Toplam ısı geçiş katsayısı U = 1.5 kW/(m²·K) varsayımıyla (sıvı-sıvı eşanjör için tipik):

| ΔT_app [°C] | LMTD [K] | A = Q̇/(U×LMTD) [m²] | Göreli Alan |
|--------------|----------|----------------------|-------------|
| 5            | 5.0      | 66.7                 | 10.0×       |
| 10           | 10.0     | 33.3                 | 5.0×        |
| 15           | 15.0     | 22.2                 | 3.3×        |
| 20           | 20.0     | 16.7                 | 2.5×        |
| 30           | 30.0     | 11.1                 | 1.67×       |
| 50 (mevcut)  | 50.0     | 6.67                 | 1.0× (ref)  |

> **Önemli gözlem:** Approach temperature'ı 50°C'den 5°C'ye düşürmek, eşanjör alanını 10 kat
> artırmayı gerektirmektedir. Bu dramatik alan artışı, çok düşük approach temperature'ların
> ekonomik açıdan uygulanabilir olmadığını göstermektedir.

---

## 8. Adım 7: Maliyet-Entropi Trade-off Analizi (Cost-Entropy Trade-off Analysis)

### 8.1 Maliyet Varsayımları

Bu analizde aşağıdaki ekonomik parametreler kullanılmaktadır:

| Parametre                          | Değer              | Birim          |
|------------------------------------|--------------------|----------------|
| Eşanjör birim alan maliyeti        | b = 1,200          | TL/m²          |
| Eşanjör ekonomik ömür              | n = 15             | yıl            |
| Faiz oranı (sermaye maliyeti)      | i = 10%            | —              |
| Yıllık amortizasyon faktörü        | CRF = 0.1315       | —              |
| Elektrik birim fiyatı              | c_el = 0.18        | TL/kWh         |
| Yıllık çalışma süresi             | t = 8,000          | saat/yıl       |
| Referans çevre sıcaklığı           | T₀ = 298           | K              |

**Sermaye geri kazanım faktörü (Capital Recovery Factor — CRF):**

```
CRF = i × (1 + i)^n / [(1 + i)^n − 1]
CRF = 0.10 × (1.10)^15 / [(1.10)^15 − 1]
CRF = 0.10 × 4.177 / (4.177 − 1)
CRF = 0.4177 / 3.177
CRF = 0.1315
```

### 8.2 Yıllık Maliyet Hesabı

**Yıllık amortize edilmiş eşanjör maliyeti:**

```
C_ekipman = b × A × CRF   [TL/yıl]
```

**Yıllık exergy yıkım maliyeti:**

```
C_exergy = T₀ × Ṡ_gen,ΔT × t × c_el   [TL/yıl]
```

**Toplam yıllık maliyet:**

```
C_toplam = C_ekipman + C_exergy   [TL/yıl]
```

### 8.3 Toplam Maliyet Optimizasyon Tablosu

| ΔT_app [°C] | Alan [m²] | C_ekipman [TL/yıl] | İ [kW]  | C_exergy [TL/yıl] | C_toplam [TL/yıl] |
|--------------|-----------|---------------------|---------|--------------------|--------------------|
| 5            | 66.7      | 10,524              | 11.18   | 16,099             | 26,623             |
| 10           | 33.3      | 5,257               | 18.68   | 26,899             | 32,156             |
| 15           | 22.2      | 3,504               | 25.93   | 37,339             | 40,843             |
| 20           | 16.7      | 2,635               | 32.96   | 47,462             | 50,097             |
| 30           | 11.1      | 1,752               | 46.46   | 66,902             | 68,654             |
| 50 (mevcut)  | 6.67      | 1,052               | 62.34   | 89,770             | 90,822             |

**Hesaplama detayı (ΔT_app = 5°C örneği):**

```
C_ekipman = 1,200 × 66.7 × 0.1315 = 10,524 TL/yıl
C_exergy  = 11.18 × 8,000 × 0.18  = 16,099 TL/yıl
C_toplam  = 10,524 + 16,099        = 26,623 TL/yıl
```

**Hesaplama detayı (ΔT_app = 50°C mevcut durum):**

```
C_ekipman = 1,200 × 6.67 × 0.1315 = 1,052 TL/yıl
C_exergy  = 62.34 × 8,000 × 0.18  = 89,770 TL/yıl
C_toplam  = 1,052 + 89,770         = 90,822 TL/yıl
```

### 8.4 Maliyet Eğrisi Yorumu (Text-Based)

```
Yıllık Maliyet [TL]
    |
100k|  ×                                       ← C_exergy (entropi bedeli)
    |   ×
 90k|    ×
    |     ×
 80k|
    |       ×
 70k|         ×
    |
 60k|
    |
 50k|             ×
    |
 40k|                 ×
    |                       ← C_toplam
 30k|        ×
    |   ★ Optimum
 25k|  ×
    |
 20k|  ×          ← C_ekipman (alan maliyeti)
    |
 10k|  ×
    |    ×   ×   ×   ×   ×
  0 +---|---|---|---|---|---|---- ΔT_app [°C]
        5  10  15  20  30  50
```

### 8.5 Optimum Sonucu

Tablodan görüldüğü gibi, **ΔT_app = 5°C** toplam yıllık maliyet açısından en düşük değeri
(26,623 TL/yıl) vermektedir. Ancak pratikte daha düşük approach temperature değerleri
(3-4°C) de değerlendirilebilir.

**Analitik optimum tahmini:**

Maliyet fonksiyonunun türevini sıfıra eşitleyerek:

```
dC_toplam/d(ΔT_app) = 0
```

Basitleştirilmiş analizde:

```
ΔT_opt ≈ √(b × CRF / (T₀ × c_el × t × dṠ_gen/dΔT))
```

Sayısal türev yaklaşımıyla dṠ_gen/dΔT ≈ 0.0038 kW/(K·°C) alınırsa:

```
ΔT_opt ≈ √(1,200 × 0.1315 / (298 × 0.18 × 8,000 × 0.0038))
ΔT_opt ≈ √(157.8 / 1,634)
ΔT_opt ≈ √(0.0966)
ΔT_opt ≈ 0.31 → çok düşük çıkması, alan maliyetinin exergy maliyetine göre
                  küçük olduğunu gösterir
```

> **Pratik yorum:** Bu analiz, mevcut enerji fiyatları ile eşanjör maliyetleri arasındaki
> dengeye göre, mümkün olduğunca düşük approach temperature'ın ekonomik açıdan yararlı
> olduğunu göstermektedir. Ancak pratik sınırlar (fouling marjı, kontrol hassasiyeti,
> mevsimsel yük değişimleri) göz önüne alındığında **ΔT_app = 5-10°C** endüstriyel
> sıvı-sıvı eşanjörler için uygulama açısından optimal aralıktır.

---

## 9. Mevcut Durumdan Optimuma Geçiş — Beklenen Tasarruf (Expected Savings)

### 9.1 Mevcut vs Optimum Karşılaştırma

| Parametre                   | Mevcut (ΔT=50°C) | Optimize (ΔT=10°C) | Fark           |
|-----------------------------|-------------------|---------------------|----------------|
| Ṡ_gen,toplam [kW/K]        | 0.2096            | 0.0631              | −0.1465 (−70%) |
| Be [-]                      | 0.998             | 0.994               | −0.004         |
| İ (exergy yıkımı) [kW]    | 62.46             | 18.80               | −43.66 (−70%)  |
| Eşanjör alanı [m²]         | 6.67              | 33.3                | +26.6 (+399%)  |
| C_ekipman [TL/yıl]         | 1,052             | 5,257               | +4,205         |
| C_exergy [TL/yıl]          | 89,770            | 26,899              | −62,871        |
| **C_toplam [TL/yıl]**      | **90,822**        | **32,156**          | **−58,666**    |

### 9.2 Yatırım Geri Dönüş Analizi

Yeni (daha büyük) eşanjör toplam maliyeti:

```
C_yatırım = b × A_yeni = 1,200 × 33.3 = 39,960 TL
```

Mevcut eşanjörün hurda değeri ihmal edilerek (pessimistic yaklaşım):

Yıllık net tasarruf (exergy maliyeti farkı − ekstra amortizasyon):

```
Δ_net = (C_exergy,mevcut − C_exergy,yeni) − (C_ekipman,yeni − C_ekipman,mevcut)
Δ_net = (89,770 − 26,899) − (5,257 − 1,052)
Δ_net = 62,871 − 4,205
Δ_net = 58,666 TL/yıl
```

Basit geri ödeme süresi (Simple Payback Period — SPP):

```
SPP = C_yatırım / Δ_net_yıllık
SPP = 39,960 / 58,666
SPP ≈ 0.68 yıl ≈ 8.2 ay
```

> **Sonuç:** Eşanjör yenileme yatırımı, yaklaşık **8 ayda** kendini amorti etmektedir.
> Bu, endüstriyel enerji verimliliği projelerinde son derece kısa bir geri dönüş süresidir.

---

## 10. Sonuç ve Mühendislik Yorumu (Conclusion and Engineering Interpretation)

### 10.1 Analiz Özeti

Bu çözümlü örnekte, 500 kW kapasiteli sıvı-sıvı karşı akışlı eşanjörün EGM analizi
tamamlanmıştır. Temel bulgular:

1. **Entropi üretimi dağılımı:** Toplam entropi üretiminin %99.8'i ısı transferi kaynaklı
   (Bejan sayısı Be = 0.998). Basınç düşüşü katkısı ihmal edilebilir düzeydedir.

2. **Exergy yıkımı:** Mevcut durumda (ΔT_app = 50°C) 62.46 kW exergy yıkılmaktadır.
   Bu, aktarılan ısının %12.5'ine karşılık gelir.

3. **Optimum approach temperature:** Maliyet-entropi trade-off analizi, ΔT_app = 5-10°C
   aralığının ekonomik optimum olduğunu göstermektedir.

4. **Tasarruf potansiyeli:** Approach temperature 50°C'den 10°C'ye düşürülürse yıllık
   yaklaşık 58,666 TL tasarruf sağlanabilir. Yatırım 8 ayda amorti olur.

### 10.2 Bejan Sayısı Yorumu

Be = 0.998 değeri, bu eşanjörde iyileştirme stratejisinin net olarak belirlenmesini sağlar:

- **Yapılması gereken:** Isı transfer alanını artırarak approach temperature'ı düşürmek
- **Yapılmaması gereken:** Basınç düşüşünü azaltmaya odaklanmak (zaten ihmal edilebilir)

### 10.3 Pratik Öneriler (Practical Recommendations)

1. **Kısa vadeli (0-3 ay):** Mevcut eşanjörün fouling durumunu kontrol et. Temizlik ile
   bile performans iyileşebilir.

2. **Orta vadeli (3-12 ay):** Eşanjörü daha büyük alanlı bir plakalı eşanjör (plate heat
   exchanger) ile değiştir. Hedef ΔT_app ≤ 10°C.

3. **Uzun vadeli (1-3 yıl):** Fabrika genelinde tüm eşanjörlerin EGM analizini yap.
   Approach temperature > 30°C olan tüm eşanjörleri öncelikli iyileştirme adayı olarak
   işaretle.

4. **İzleme:** Eşanjör giriş/çıkış sıcaklıklarını sürekli izle. Approach temperature'daki
   artış trendi fouling'in erken göstergesidir.

---

## 11. Doğrulama (Verification)

### 11.1 Enerji Dengesi Kontrolü (Energy Balance Check)

```
Q̇_hot  = ṁ_hot × c_p × (T_h,giriş − T_h,çıkış)
Q̇_hot  = 2.99 × 4.18 × (120 − 80) = 500.0 kW  ✓

Q̇_cold = ṁ_cold × c_p × (T_c,çıkış − T_c,giriş)
Q̇_cold = 2.99 × 4.18 × (70 − 30) = 500.0 kW  ✓

Enerji dengesi: Q̇_hot = Q̇_cold = 500 kW  ✓ (Isı kaybı ihmal edilmiştir)
```

### 11.2 Entropi Dengesi Kontrolü (Entropy Balance Check)

Termodinamiğin ikinci yasası gereği Ṡ_gen ≥ 0 olmalıdır:

```
Ṡ_gen,ΔT = 0.2092 kW/K > 0  ✓
Ṡ_gen,ΔP = 0.0003893 kW/K > 0  ✓
Ṡ_gen,toplam = 0.2096 kW/K > 0  ✓
```

### 11.3 Makullük Kontrolü (Reasonableness Check)

Tipik değerlerle karşılaştırma:

| Parametre              | Bu örnekteki değer | Tipik endüstriyel aralık | Durum |
|------------------------|-------------------|--------------------------|-------|
| Ṡ_gen,ΔT [kW/K]       | 0.209             | 0.01 − 0.50             | ✓     |
| Be [-]                 | 0.998             | 0.50 − 0.80 (S&T HX)   | Yüksek* |
| N_s (= Ṡ_gen/C_min)   | 0.209/12.50=0.017 | 0.01 − 0.30             | ✓     |
| İ/Q̇ [%]               | 12.5%             | 2% − 25%                | ✓     |

*Be = 0.998, tipik aralığın üzerindedir. Bunun nedeni, her iki tarafta da sıvı (su)
kullanılmasıdır. Sıvıların yüksek yoğunluğu, basınç düşüşü bileşenini son derece küçük
tutarak Be'yi 1'e yaklaştırır. Gaz-sıvı veya gaz-gaz eşanjörlerde Be daha düşük olur.

### 11.4 Birimler Kontrolü (Units Check)

```
Ṡ_gen,ΔT: [kg/s] × [kJ/(kg·K)] × [-] = [kW/K]  ✓
Ṡ_gen,ΔP: [kg/s] × [kPa] / ([kg/m³] × [K]) = [kW/K]  ✓
İ:        [K] × [kW/K] = [kW]  ✓
C_exergy: [kW] × [saat] × [TL/kWh] = [TL]  ✓
```

---

## İlgili Dosyalar

- `factory/entropy_generation/heat_exchanger_egm.md` — Isı eşanjörlerinde EGM uygulaması (kapsamlı)
- `factory/entropy_generation/heat_transfer_egm.md` — Isı transferi kaynaklı entropi üretimi temelleri
- `factory/entropy_generation/bejan_number.md` — Bejan sayısı tanım, yorumlama ve benchmark değerleri
- `factory/entropy_generation/fundamentals.md` — Entropi üretimi temel kavramları
- `factory/entropy_generation/fluid_flow_egm.md` — Akışkan akışı kaynaklı entropi üretimi
- `factory/cross_equipment.md` — Ekipmanlar arası entegrasyon fırsatları
- `factory/pinch_analysis.md` — Pinch analizi ve ısı değiştirici ağ optimizasyonu

## Referanslar

1. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press.
2. Bejan, A. (2013). *Convection Heat Transfer*, 4th Edition. Wiley.
3. Çengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition. McGraw-Hill.
4. Hesselgreaves, J.E. (2000). "Rationalisation of second law analysis of heat exchangers." *International Journal of Heat and Mass Transfer*, 43(22), 4189-4204.
5. Shah, R.K. & Sekulic, D.P. (2003). *Fundamentals of Heat Exchanger Design*. Wiley.
6. Sciubba, E. (2005). "From Engineering Economics to Extended Exergy Accounting." *Energy*, 30(11-12), 2168-2182.
7. Naterer, G.F. & Camberos, J.A. (2008). *Entropy-Based Design and Analysis of Fluids Engineering Systems*. CRC Press.
