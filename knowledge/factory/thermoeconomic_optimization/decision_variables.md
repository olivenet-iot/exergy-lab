---
title: "Karar Değişkenleri ve Kısıtlar (Decision Variables and Constraints)"
category: thermoeconomic_optimization
keywords: [karar değişkenleri, kısıtlar, sınırlar, optimizasyon modeli, ekipman parametreleri]
related_files: [knowledge/factory/thermoeconomic_optimization/objective_functions.md, knowledge/factory/thermoeconomic_optimization/parametric_optimization.md, knowledge/factory/thermoeconomic_optimization/structural_optimization.md]
use_when: ["Optimizasyon model kurulumu yapılırken", "Ekipman bazlı karar değişkenleri ve sınırlar belirlenirken"]
priority: medium
last_updated: 2026-02-02
---

# Karar Değişkenleri ve Kısıtlar (Decision Variables and Constraints)

## 1. Değişken Sınıflandırması

Termoekonomik optimizasyonda karar değişkenleri üç temel türde sınıflandırılır:

### 1.1. Sürekli Değişkenler (Continuous Variables)

Belirli bir aralıkta herhangi bir değer alabilen değişkenler:

```
x_i ∈ [x_i,min, x_i,max]    i = 1, 2, ..., n_c

Örnekler:
  - Sıcaklıklar [°C veya K]
  - Basınçlar [bar veya kPa]
  - Debiler [kg/s veya m³/h]
  - Isı transfer yüzey alanları [m²]
  - Fazla hava oranı [%]
  - İzentropik verimler [%]
```

### 1.2. Kesikli Değişkenler (Discrete Variables)

Yalnızca belirli değerler alabilen değişkenler:

```
x_j ∈ {v₁, v₂, ..., v_m}    j = 1, 2, ..., n_d

Örnekler:
  - Boru çapları [DN]: {25, 32, 40, 50, 65, 80, 100, ...}
  - Ekipman boyutları (standart kapasite): {50, 75, 110, 150, 200, ... kW}
  - Kademe sayısı (kompresör): {1, 2, 3}
  - Geçiş sayısı (ısı değiştirici): {1, 2, 4, 6}
```

### 1.3. İkili Değişkenler (Binary Variables)

Açık/kapalı, var/yok kararları için:

```
y_k ∈ {0, 1}    k = 1, 2, ..., n_b

Örnekler:
  - Ekipman dahil mi? (y = 1: evet, y = 0: hayır)
  - CHP sistemi kurulsun mu?
  - Economizer eklensin mi?
  - VSD takılsın mı?
  - Absorpsiyonlu chiller kullanılsın mı?
```

---

## 2. Ekipman Bazlı Karar Değişkenleri ve Sınırlar

### 2.1. Kazan (Boiler)

| Değişken | Sembol | Birim | Alt Sınır | Üst Sınır | Tipik Optimal |
|----------|--------|-------|-----------|-----------|---------------|
| Fazla hava oranı | λ | % | 5 | 30 | 8-12 |
| Baca gazı sıcaklığı | T_stack | °C | 120 | 300 | 130-160 |
| Buhar basıncı | P_steam | bar | 4 | 25 | Prosese bağlı |
| Buhar sıcaklığı (kızgın) | T_sh | °C | T_sat | T_sat + 150 | Prosese bağlı |
| Economizer yüzey alanı | A_eco | m² | 0 | 200 | 20-80 |
| Besleme suyu sıcaklığı | T_fw | °C | 60 | 105 | 80-95 |
| Blowdown oranı | r_bd | % | 1 | 10 | 2-5 |
| Air preheater (var/yok) | y_aph | - | 0 | 1 | Q > 3 MW ise 1 |
| Economizer (var/yok) | y_eco | - | 0 | 1 | T_stack > 200°C ise 1 |
| Kapasite | Q_boiler | kW | 100 | 20,000 | Yüke bağlı |

**Önemli kısıtlar:**
- T_stack > T_asit çiğlenme (doğalgaz: ~55°C, fuel oil: ~130°C, kömür: ~120°C)
- Doğalgazda: T_stack > 120°C (korozyon güvenliği)
- P_steam × V_steam ≤ Kazan tasarım basıncı × güvenlik faktörü

### 2.2. Kompresör (Air Compressor)

| Değişken | Sembol | Birim | Alt Sınır | Üst Sınır | Tipik Optimal |
|----------|--------|-------|-----------|-----------|---------------|
| Deşarj basıncı | P_out | bar | 4 | 13 | Minimum gerekli + %5 |
| Emme sıcaklığı | T_in | °C | 10 | 45 | Mümkün olan en düşük |
| Kademe sayısı | n_stage | - | 1 | 3 | P > 8 bar ise 2 |
| Ara soğutma sıcaklığı | T_ic | °C | 25 | 45 | 30-35 |
| VSD (var/yok) | y_vsd | - | 0 | 1 | Değişken yük ise 1 |
| Isı geri kazanım (var/yok) | y_hr | - | 0 | 1 | Isı ihtiyacı varsa 1 |
| Motor verimi sınıfı | η_motor | - | IE2 | IE4 | IE3 veya IE4 |
| Kapasite | Ẇ_comp | kW | 5 | 500 | Yüke bağlı |

**Önemli kısıtlar:**
- P_out ≥ P_min,proses + ΔP_dağıtım + ΔP_filtre
- T_out ≤ T_max,yağ (vidalı: ~110°C)
- Kademe başına basınç oranı ≤ 4-5

### 2.3. Chiller (Vapor Compression)

| Değişken | Sembol | Birim | Alt Sınır | Üst Sınır | Tipik Optimal |
|----------|--------|-------|-----------|-----------|---------------|
| Evaporatör sıcaklığı | T_evap | °C | -10 | 15 | Prosese bağlı |
| Kondenser sıcaklığı | T_cond | °C | 25 | 50 | Mümkün olan en düşük |
| Chilled water set point | T_chw | °C | 4 | 15 | 6-8 |
| Kondenser suyu sıcaklığı | T_cw | °C | 20 | 40 | 28-32 |
| Kompresör tipi | type_comp | - | scroll | centrifugal | Kapasiteye bağlı |
| VSD (var/yok) | y_vsd | - | 0 | 1 | Değişken yük ise 1 |
| Kapasite | Q_chiller | kW | 20 | 5,000 | Yüke bağlı |
| Serbest soğutma (var/yok) | y_fc | - | 0 | 1 | T_amb < T_chw ise 1 |

**Önemli kısıtlar:**
- T_evap < T_chw - ΔT_yaklaşım (tipik 3-5°C)
- T_cond > T_cw + ΔT_yaklaşım (tipik 3-5°C)
- COP ≥ COP_min (enerji sınıfı gereksinimi)

### 2.4. Pompa (Pump)

| Değişken | Sembol | Birim | Alt Sınır | Üst Sınır | Tipik Optimal |
|----------|--------|-------|-----------|-----------|---------------|
| Debi | V̇ | m³/h | 1 | 500 | Prosese bağlı |
| Basma yüksekliği | H | m | 5 | 150 | Minimum gerekli |
| Çark çapı | D_imp | mm | D_min | D_max | BEP yakınında |
| Devir (VSD ile) | n | rpm | 600 | 3,000 | Yüke göre |
| VSD (var/yok) | y_vsd | - | 0 | 1 | Değişken yük ise 1 |
| Pompa tipi | type | - | - | - | Kapasiteye bağlı |
| Motor verimi sınıfı | η_motor | - | IE2 | IE4 | IE3 veya IE4 |

**Önemli kısıtlar:**
- NPSHa > NPSHr + %10 güvenlik
- Pompa BEP'in %80-110'unda çalışmalı
- V̇ × H ≤ Pompa eğrisi sınırları

---

## 3. Fabrika Seviyesi Karar Değişkenleri

### 3.1. CHP / Trijenerasyon Değişkenleri

| Değişken | Sembol | Birim | Alt Sınır | Üst Sınır |
|----------|--------|-------|-----------|-----------|
| CHP kapasitesi (elektrik) | Ẇ_CHP | kW | 0 | 10,000 |
| CHP tipi | type_CHP | - | GT | ICE / GT / ST |
| CHP kurulsun mu? | y_CHP | - | 0 | 1 |
| HRSG buhar basıncı | P_HRSG | bar | 4 | 40 |
| Absorpsiyonlu chiller kapasitesi | Q_abs | kW | 0 | 2,000 |
| Abs. chiller kurulsun mu? | y_abs | - | 0 | 1 |

### 3.2. Isı Geri Kazanım Ağı Değişkenleri

| Değişken | Sembol | Birim | Alt Sınır | Üst Sınır |
|----------|--------|-------|-----------|-----------|
| ΔT_min (pinch) | ΔT_min | °C | 5 | 30 |
| HX yüzey alanı (her eşleşme) | A_HX,ij | m² | 0 | 200 |
| Eşleşme var/yok | y_HX,ij | - | 0 | 1 |
| Kompresör atık ısı geri kazanım oranı | r_HR,comp | % | 0 | 70 |
| Baca gazı ısı geri kazanım oranı | r_HR,stack | % | 0 | 80 |

### 3.3. Enerji Dağıtım Değişkenleri

| Değişken | Sembol | Birim | Açıklama |
|----------|--------|-------|----------|
| Buhar dağıtım basıncı | P_dist | bar | Tek basınç vs çoklu basınç |
| Basınçlı hava dağıtım basıncı | P_air | bar | Bölgesel basınç azaltma |
| Chilled water set point | T_chw | °C | Merkezi vs bölgesel set point |

---

## 4. Kısıt Türleri

### 4.1. Eşitlik Kısıtları (Equality Constraints)

```
h(x) = 0    — Fiziksel denge denklemleri
```

| Kısıt Tipi | Formül | Açıklama |
|------------|--------|----------|
| Kütle dengesi | Σ ṁ_giriş = Σ ṁ_çıkış | Her bileşen ve birleşim noktası |
| Enerji dengesi | Σ Ḣ_giriş + Q̇ = Σ Ḣ_çıkış + Ẇ | 1. Yasa |
| Exergy dengesi | Σ Ėx_giriş = Σ Ėx_çıkış + Ėx_D + Ėx_L | 2. Yasa |
| Maliyet dengesi | Σ Ċ_çıkış + Ċ_W = Σ Ċ_giriş + Ċ_Q + Ż | Exergoekonomik denge |
| Termodinamik ilişki | h = f(T, P) | CoolProp ile durum denklemleri |
| Proses talebi | Q̇_proses = Q̇_gerekli | Prosesin ısı talebi karşılanmalı |
| Elektrik dengesi | Ẇ_üretim + Ẇ_şebeke = Ẇ_tüketim | Elektrik arz-talep dengesi |

### 4.2. Eşitsizlik Kısıtları (Inequality Constraints)

```
g(x) ≤ 0    — Sınır ve güvenlik kısıtları
```

| Kısıt Tipi | Formül | Açıklama |
|------------|--------|----------|
| Sıcaklık sınırı | T_material ≤ T_max,material | Malzeme dayanım sınırı |
| Basınç sınırı | P ≤ P_design × SF | Tasarım basıncı × güvenlik |
| Kapasite sınırı | Q̇ ≤ Q̇_max | Ekipman kapasite sınırı |
| Verim sınırı | η ≤ η_max | Fiziksel verim üst sınırı |
| Emisyon sınırı | ṁ_CO₂ ≤ ṁ_CO₂,izin | Çevresel düzenleme |
| Baca gazı sıcaklığı | T_stack ≥ T_asit_çiğlenme | Korozyon önleme |
| NPSH | NPSHa ≥ NPSHr × 1.1 | Kavitasyon önleme |
| Yük aralığı | Q̇_min ≤ Q̇ ≤ Q̇_max | Stabil çalışma aralığı |
| Bütçe kısıtı | Σ Z_k ≤ Budget | Toplam yatırım bütçesi |

### 4.3. Çevresel Kısıtlar

| Kısıt | Limit | Kaynak |
|-------|-------|--------|
| NOx emisyonu | < 100 mg/Nm³ (doğalgaz) | Türkiye ÇED yönetmeliği |
| CO emisyonu | < 100 mg/Nm³ | Türkiye ÇED yönetmeliği |
| PM emisyonu | < 20 mg/Nm³ (gaz) | Türkiye ÇED yönetmeliği |
| Gürültü | < 85 dB(A) (çalışma alanı) | İş güvenliği yönetmeliği |
| Toplam CO₂ | Sektörel üst sınır | CBAM / ETS (gelecekte) |

---

## 5. Kısıt İşleme Yöntemleri

### 5.1. Ceza Fonksiyonu (Penalty Function)

Kısıtsız optimizasyona dönüştürmek için:

```
F_penalized(x) = f(x) + Σ μ_j × max(0, g_j(x))² + Σ λ_k × h_k(x)²

Burada:
  μ_j  = Eşitsizlik kısıtı ceza çarpanı (büyük sayı, tipik 10³-10⁶)
  λ_k  = Eşitlik kısıtı ceza çarpanı
  g_j  = j-inci eşitsizlik kısıtı
  h_k  = k-inci eşitlik kısıtı
```

**Avantajları:**
- Basit implementasyon
- Her algoritma ile kullanılabilir (GA, PSO dahil)

**Dezavantajları:**
- Ceza çarpanı seçimi zor
- Kısıt sınırı yakınında hassasiyet düşük
- Uygulanabilir olmayan bölgede zaman kaybı

### 5.2. Lagrange Çarpanı (Lagrangian Relaxation)

```
L(x, λ, μ) = f(x) + Σ λ_k × h_k(x) + Σ μ_j × g_j(x)

KKT koşulları:
  ∇_x L = 0
  h_k(x) = 0
  μ_j × g_j(x) = 0
  μ_j ≥ 0
```

**Kullanım:** Gradient tabanlı yöntemlerde (SQP, Interior Point)

### 5.3. Onarım Operatörü (Repair Operator)

Evrimsel algoritmalarda (GA, PSO) kısıt ihlali düzeltmesi:

```python
# Örnek: Sınır onarımı
def repair_solution(x, bounds):
    for i in range(len(x)):
        if x[i] < bounds[i][0]:
            x[i] = bounds[i][0]
        elif x[i] > bounds[i][1]:
            x[i] = bounds[i][1]
    return x

# Örnek: Enerji dengesi onarımı
def repair_energy_balance(x, Q_demand):
    Q_total = sum(x[equipment_capacities])
    if Q_total < Q_demand:
        scale = Q_demand / Q_total
        x[equipment_capacities] *= scale
    return x
```

### 5.4. Kısıt Baskınlığı (Constraint Domination)

Çok amaçlı optimizasyonda (NSGA-II):

```
Çözüm A, Çözüm B'yi baskılar eğer:
  1. A uygulanabilir, B değil → A baskın
  2. Her ikisi de uygulanabilir → Normal Pareto baskınlık
  3. Her ikisi de uygulanabilir değil → Daha az kısıt ihlali olan baskın
```

---

## 6. Değişken Ölçeklendirme

Farklı büyüklükteki değişkenler için ölçeklendirme kritiktir:

```
x_scaled,i = (x_i - x_i,min) / (x_i,max - x_i,min)    ∈ [0, 1]

veya

x_scaled,i = x_i / x_i,ref    (referans değere göre)
```

| Değişken | Tipik Büyüklük | Ölçeklendirme Önerisi |
|----------|---------------|----------------------|
| Sıcaklık | 100-500°C | (T - T_min) / (T_max - T_min) |
| Basınç | 1-25 bar | P / P_ref |
| Güç | 10-10,000 kW | Ẇ / Ẇ_ref |
| Yüzey alanı | 1-500 m² | A / A_ref |
| Maliyet | 10,000-1,000,000 € | Z / Z_ref |

> **Önemli:** Ölçeklendirmesiz optimizasyon, gradient tabanlı yöntemlerde sayısal
> problemlere (ill-conditioning) ve yavaş yakınsamaya yol açar.

---

## 7. Tipik Optimizasyon Model Boyutu

| Sistem Tipi | Sürekli Değ. | Kesikli Değ. | İkili Değ. | Kısıt |
|-------------|-------------|-------------|-----------|-------|
| Tek kazan | 5-8 | 0-2 | 1-3 | 8-15 |
| Tek kompresör | 4-6 | 0-1 | 1-3 | 6-12 |
| CHP sistemi | 10-20 | 2-5 | 3-8 | 20-40 |
| Isı geri kazanım ağı | 5-15 | 0-5 | 5-20 | 15-30 |
| Fabrika (4 ekipman) | 20-35 | 3-8 | 8-15 | 40-70 |
| Fabrika (10 ekipman) | 50-80 | 5-15 | 15-30 | 80-150 |

> **Kural:** İkili değişken sayısı arttıkça çözüm zorlaşır (2^n olası konfigürasyon).
> 15+ ikili değişkende MINLP çözücü veya metaheuristik gereklidir.

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `objective_functions.md` — Amaç fonksiyonları detayı
- `parametric_optimization.md` — NLP çözüm yöntemleri
- `structural_optimization.md` — MINLP çözüm yöntemleri
- `algorithms.md` — Optimizasyon algoritmaları
- `practical_guide.md` — Endüstriyel uygulama

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Edgar, T.F., Himmelblau, D.M., & Lasdon, L.S. (2001). *Optimization of Chemical Processes*. McGraw-Hill.
- Floudas, C.A. (1995). *Nonlinear and Mixed-Integer Optimization*. Oxford University Press.
- Türk ÇED Yönetmeliği, Çevre, Şehircilik ve İklim Değişikliği Bakanlığı.
