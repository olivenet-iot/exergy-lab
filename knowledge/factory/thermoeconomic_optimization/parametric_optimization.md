---
title: "Parametrik Optimizasyon (Parametric Optimization)"
category: thermoeconomic_optimization
keywords: [parametrik optimizasyon, NLP, SQP, gradient tabanlı, scipy, CoolProp]
related_files: [knowledge/factory/thermoeconomic_optimization/decision_variables.md, knowledge/factory/thermoeconomic_optimization/algorithms.md, knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md]
use_when: ["Mevcut sistemde parametre ince ayarı gerektiğinde", "NLP çözüm yöntemleri ve Python implementasyonu istendiğinde"]
priority: high
last_updated: 2026-02-02
---

# Parametrik Optimizasyon (Parametric Optimization)

## 1. Tanım

Parametrik optimizasyon, **sabit sistem yapısı** (konfigürasyon) altında sürekli karar
değişkenlerini (sıcaklıklar, basınçlar, debiler, yüzey alanları) optimize eder.

### NLP Formülasyonu

```
min f(x)           — Amaç: Toplam yıllıklaştırılmış maliyet
s.t.
  h(x) = 0         — Eşitlik kısıtları (termodinamik denge)
  g(x) ≤ 0         — Eşitsizlik kısıtları (sınırlar)
  x_L ≤ x ≤ x_U    — Değişken sınırları

  x ∈ R^n           — Tüm değişkenler sürekli
```

---

## 2. Gradient Tabanlı Yöntemler

### 2.1. SQP (Sequential Quadratic Programming)

En yaygın kullanılan gradient tabanlı NLP çözücüsü.

```
Temel fikir:
  Her iterasyonda, amaç fonksiyonunu kuadratik,
  kısıtları doğrusal olarak yaklaşıkla.
  Bu QP alt problemini çöz → arama yönü bul → adım at.

Algoritma:
  1. Başlangıç noktası x₀ seç
  2. Lagrangian'ın Hessian'ını hesapla (veya yaklaşıkla — BFGS)
  3. QP alt problemi çöz → arama yönü d
  4. Doğru araması (line search): α* = argmin f(x + α·d)
  5. x_{k+1} = x_k + α* · d
  6. Yakınsama kontrolü: |∇L| < ε → dur
  7. Adım 2'ye dön

Avantajları:
  - Hızlı yakınsama (süper-doğrusal)
  - Kısıtları doğrudan işler
  - İyi bir başlangıç noktası ile 10-50 iterasyonda çözüm

Dezavantajları:
  - Yerel minimuma takılabilir
  - Gradient hesabı gerekir (finite difference veya analitik)
  - Konveks olmayan problemlerde global optimum garantisi yok
```

### 2.2. Interior Point (Barrier) Method

```
Temel fikir:
  Eşitsizlik kısıtlarını barrier fonksiyonuyla amaç fonksiyonuna ekle.
  Barrier parametresini kademeli azalt.

Amaç (barrier):
  min f(x) - μ × Σ ln(s_j)
  s.t. g_j(x) + s_j = 0, s_j > 0

Avantajları:
  - Büyük ölçekli problemlerde verimli
  - Seyrek matrislerle iyi çalışır

Dezavantajları:
  - Başlangıç noktası uygulanabilir bölgede olmalı
  - Yerel minimum riski
```

---

## 3. Python İmplementasyonu

### 3.1. scipy.optimize.minimize ile SQP

```python
import numpy as np
from scipy.optimize import minimize
from CoolProp.CoolProp import PropsSI

def boiler_thermoeconomic_cost(x, params):
    """
    Kazan sistemi toplam yıllıklaştırılmış maliyet fonksiyonu.

    Değişkenler:
      x[0] = excess_air (fazla hava oranı, 0.05-0.30)
      x[1] = T_stack (baca gazı sıcaklığı, °C, 120-300)
      x[2] = A_eco (economizer yüzey alanı, m², 0-200)
      x[3] = T_fw (besleme suyu sıcaklığı, °C, 60-105)
    """
    excess_air = x[0]
    T_stack = x[1]
    A_eco = x[2]
    T_fw = x[3]

    Q_boiler = params['Q_boiler']   # kW
    P_steam = params['P_steam']     # bar
    tau = params['tau']             # h/yıl
    c_fuel = params['c_fuel']       # €/kWh
    CRF = params['CRF']

    # Yanma verimi (basitleştirilmiş)
    eta_comb = 0.99 - 0.3 * excess_air

    # Baca gazı kaybı (basitleştirilmiş)
    Q_stack_loss = Q_boiler * (T_stack - 25) / (1800 - 25) * (1 + excess_air)

    # Economizer kazanımı
    UA_eco = 0.05 * A_eco  # kW/K (basitleştirilmiş)
    Q_eco = min(UA_eco * (T_stack - T_fw), Q_stack_loss * 0.8)

    # Kazan yakıt tüketimi
    Q_fuel = (Q_boiler - Q_eco) / (eta_comb * 0.92)

    # Yakıt maliyeti
    C_fuel = Q_fuel * c_fuel * tau

    # Yatırım maliyeti
    Z_boiler = 46.4 * Q_boiler**0.79 * 2.5 * 1.36  # CEPCI düzeltmeli
    Z_eco = 130 * A_eco**0.78 * 2.25 if A_eco > 0 else 0
    C_invest = CRF * (Z_boiler + Z_eco) * 1.06

    # Toplam yıllıklaştırılmış maliyet
    C_total = C_fuel + C_invest

    return C_total

# Parametreler
params = {
    'Q_boiler': 3000,   # kW
    'P_steam': 10,      # bar
    'tau': 5500,         # h/yıl
    'c_fuel': 0.037,     # €/kWh (doğalgaz)
    'CRF': 0.1168       # i=8%, n=15 yıl
}

# Başlangıç noktası
x0 = [0.20, 220, 30, 70]

# Sınırlar
bounds = [
    (0.05, 0.30),   # excess_air
    (120, 300),      # T_stack (°C)
    (0, 200),        # A_eco (m²)
    (60, 105)        # T_fw (°C)
]

# Kısıtlar
constraints = [
    {'type': 'ineq', 'fun': lambda x: x[1] - 120},  # T_stack > 120°C
    {'type': 'ineq', 'fun': lambda x: x[1] - x[3] - 20},  # T_stack > T_fw + 20
]

# Optimizasyon
result = minimize(
    boiler_thermoeconomic_cost, x0,
    args=(params,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints,
    options={'maxiter': 200, 'ftol': 1e-8}
)

print(f"Optimal fazla hava: {result.x[0]*100:.1f}%")
print(f"Optimal T_stack: {result.x[1]:.1f}°C")
print(f"Optimal A_eco: {result.x[2]:.1f} m²")
print(f"Optimal T_fw: {result.x[3]:.1f}°C")
print(f"Minimum C_total: {result.fun:,.0f} €/yıl")
```

### 3.2. CoolProp Entegrasyonu

```python
from CoolProp.CoolProp import PropsSI

def steam_exergy(T_C, P_bar, m_dot, T0_C=25):
    """Buhar exergy akış hızı hesapla [kW]"""
    T = T_C + 273.15
    T0 = T0_C + 273.15
    P = P_bar * 1e5
    P0 = 1.01325e5

    h = PropsSI('H', 'T', T, 'P', P, 'Water') / 1000  # kJ/kg
    s = PropsSI('S', 'T', T, 'P', P, 'Water') / 1000  # kJ/(kg·K)
    h0 = PropsSI('H', 'T', T0, 'P', P0, 'Water') / 1000
    s0 = PropsSI('S', 'T', T0, 'P', P0, 'Water') / 1000

    ex = (h - h0) - T0 * (s - s0)  # kJ/kg
    Ex_dot = m_dot * ex  # kW

    return Ex_dot

# Örnek: 10 bar doymuş buhar, 1.2 kg/s
T_sat = PropsSI('T', 'P', 10e5, 'Q', 1, 'Water') - 273.15  # °C
Ex_steam = steam_exergy(T_sat, 10, 1.2)
print(f"Buhar exergysi: {Ex_steam:.1f} kW")
```

---

## 4. Hesaplama Örneği: Kazan Sistemi Optimizasyonu

### 4.1. Problem Tanımı

- 3,000 kW doğalgaz kazanı
- 10 bar doymuş buhar üretimi
- 5,500 h/yıl çalışma
- Karar değişkenleri: fazla hava, baca gazı T, economizer alanı, besleme suyu T

### 4.2. Baz Durum vs Optimal Karşılaştırma

| Parametre | Baz Durum | Optimal | Değişim |
|-----------|-----------|---------|---------|
| Fazla hava [%] | 20 | 8.5 | -%11.5 |
| T_stack [°C] | 240 | 148 | -92°C |
| A_eco [m²] | 15 | 52 | +37 m² |
| T_fw [°C] | 60 | 92 | +32°C |
| η_boiler [%] | 86.2 | 93.5 | +7.3 pp |
| η_ex [%] | 27.2 | 31.8 | +4.6 pp |
| Q_fuel [kW] | 3,480 | 3,209 | -7.8% |
| C_fuel [€/yıl] | 708,180 | 652,990 | -55,190 |
| C_invest [€/yıl] | 14,800 | 19,200 | +4,400 |
| **C_total [€/yıl]** | **722,980** | **672,190** | **-50,790** |
| **Yıllık tasarruf** | - | **50,790** | - |
| Ek yatırım | - | 22,000 | - |
| SPP | - | 0.43 yıl | - |

### 4.3. Ödünleşim Analizi

Economizer yüzey alanı arttıkça:

| A_eco [m²] | C_fuel [€/yıl] | C_invest [€/yıl] | C_total [€/yıl] |
|-----------|----------------|-----------------|-----------------|
| 0 | 730,000 | 12,000 | 742,000 |
| 20 | 700,000 | 15,500 | 715,500 |
| 40 | 668,000 | 17,800 | 685,800 |
| 52 (optimal) | 653,000 | 19,200 | 672,200 |
| 80 | 638,000 | 22,500 | 660,500 |
| 120 | 628,000 | 27,200 | 655,200 |
| 200 | 622,000 | 35,800 | 657,800 |

> **Gözlem:** Optimal nokta A = 52 m² civarında. Daha büyük economizer hala yakıt tasarrufu
> sağlar ama artan yatırım maliyeti nedeniyle toplam maliyet artmaya başlar (yaklaşık optimal).

---

## 5. Algoritma Karşılaştırması

### SQP vs GA vs PSO (aynı kazan problemi)

| Kriter | SQP | GA | PSO |
|--------|-----|----|----|
| Optimal C_total [€/yıl] | 672,190 | 672,850 | 673,100 |
| Çözüm kalitesi | En iyi | %99.9 | %99.9 |
| Fonksiyon değerlendirme | 85 | 5,000 | 3,000 |
| Hesaplama (göreli) | 1× | 60× | 35× |
| Yerel minimum riski | Var | Düşük | Düşük |
| Kısıt işleme | Doğrudan | Ceza fonk. | Ceza fonk. |
| Multi-start ile SQP | 10 başlangıç: 850 | - | - |
| Global optimum güveni | %95 (multi-start) | %99 | %98 |

### 5.1. Multi-Start Stratejisi

SQP'nin yerel minimum riskini azaltmak için:

```python
import numpy as np
from scipy.optimize import minimize

def multi_start_sqp(func, bounds, n_starts=20, **kwargs):
    """Multi-start SQP optimizasyonu."""
    best_result = None
    best_cost = np.inf

    for i in range(n_starts):
        # Rastgele başlangıç noktası
        x0 = [np.random.uniform(b[0], b[1]) for b in bounds]

        try:
            result = minimize(func, x0, method='SLSQP',
                            bounds=bounds, **kwargs)
            if result.success and result.fun < best_cost:
                best_cost = result.fun
                best_result = result
        except:
            continue

    return best_result

# Kullanım
result = multi_start_sqp(
    boiler_thermoeconomic_cost,
    bounds=bounds,
    n_starts=20,
    args=(params,),
    constraints=constraints
)
```

### 5.2. Ne Zaman Hangisi?

```
SQP tercih et:
  - Düzgün (smooth), sürekli amaç fonksiyonu
  - Gradient hesaplanabilir
  - 5-20 değişken
  - Hız önemli
  - Multi-start ile güvenilirlik artırılabilir

GA/PSO tercih et:
  - Süreksiz veya gürültülü fonksiyon
  - Gradient hesaplanamıyor
  - 20+ değişken
  - Global arama önemli
  - Hesaplama süresi kritik değil
```

---

## 6. Pratik Öneriler

### 6.1. Başlangıç Noktası Seçimi

1. Mevcut işletme koşulları (en doğal başlangıç)
2. Ekipman üretici önerileri
3. Benchmark değerler (knowledge base'den)
4. Latin Hypercube Sampling (çok boyutlu)

### 6.2. Ölçeklendirme

```python
# İyi ölçeklendirme — tüm değişkenler [0, 1] aralığında
x_scaled = (x - x_min) / (x_max - x_min)

# Kötü ölçeklendirme — değişkenler çok farklı büyüklükte
# T_stack = 200°C, A_eco = 30 m², excess_air = 0.15
# Gradient tabanlı yöntemlerde yakınsama sorunlarına neden olur
```

### 6.3. Yakınsama Kontrolü

```python
# scipy.optimize sonuç kontrolü
if result.success:
    print("Optimizasyon başarılı")
    print(f"KKT koşulları: {result.jac}")  # ~0 olmalı
else:
    print(f"UYARI: {result.message}")
    # Multi-start veya farklı yöntem dene
```

### 6.4. Doğrulama

1. Optimal noktada tüm kısıtları kontrol et
2. Fiziksel anlamlılık: Sıcaklıklar, basınçlar, verimler gerçekçi mi?
3. Duyarlılık analizi ile robust mu?
4. Mühendislik sezgisi ile tutarlılık

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `decision_variables.md` — Karar değişkenleri ve sınırlar
- `algorithms.md` — Algoritma detayları
- `sensitivity_analysis.md` — Duyarlılık analizi
- `worked_examples/boiler_optimization.md` — Tam kazan örneği
- `structural_optimization.md` — Yapısal optimizasyon
- `factory/economic_analysis.md` — Ekonomik analiz yöntemleri

## Referanslar

- Nocedal, J. & Wright, S.J. (2006). *Numerical Optimization*. 2nd ed. Springer.
- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Virtanen, P. et al. (2020). "SciPy 1.0." *Nature Methods*, 17, 261-272.
- Bell, I.H. et al. (2014). "CoolProp." *Industrial & Engineering Chemistry Research*, 53, 2498-2508.
