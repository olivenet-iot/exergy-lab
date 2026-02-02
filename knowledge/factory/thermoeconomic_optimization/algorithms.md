---
title: "Optimizasyon Algoritmaları (Optimization Algorithms)"
category: thermoeconomic_optimization
keywords: [optimizasyon algoritmaları, SQP, genetik algoritma, PSO, NSGA-II, diferansiyel evrim, hibrit yöntem]
related_files: [knowledge/factory/thermoeconomic_optimization/parametric_optimization.md, knowledge/factory/thermoeconomic_optimization/multi_objective.md, knowledge/factory/thermoeconomic_optimization/structural_optimization.md]
use_when: ["Optimizasyon algoritması seçimi gerektiğinde", "Algoritma performans karşılaştırması istendiğinde"]
priority: medium
last_updated: 2026-02-02
---

# Optimizasyon Algoritmaları (Optimization Algorithms)

## 1. Algoritma Sınıflandırması

```
Optimizasyon Algoritmaları
├── Deterministik
│   ├── Gradient tabanlı
│   │   ├── SQP (Sequential Quadratic Programming)
│   │   ├── Interior Point
│   │   └── Conjugate Gradient
│   └── Gradyansız
│       ├── Nelder-Mead (Simplex)
│       └── Pattern Search
│
├── Stokastik (Metaheuristik)
│   ├── Evrimsel
│   │   ├── GA (Genetic Algorithm)
│   │   ├── DE (Differential Evolution)
│   │   └── NSGA-II (çok amaçlı)
│   ├── Sürü tabanlı
│   │   ├── PSO (Particle Swarm Optimization)
│   │   └── MOPSO (çok amaçlı)
│   └── Diğer
│       ├── SA (Simulated Annealing)
│       └── Tabu Search
│
└── Hibrit
    ├── GA + SQP
    ├── PSO + SQP
    └── DE + Interior Point
```

---

## 2. Deterministik Algoritmalar

### 2.1. SQP (Sequential Quadratic Programming)

```
Tip: Gradient tabanlı, kısıtlı NLP çözücü
Teori: Her iterasyonda kuadratik alt problem (QP) çöz

Matematiksel formülasyon:
  min  ½ d^T B_k d + ∇f(x_k)^T d
  s.t. ∇h(x_k)^T d + h(x_k) = 0
       ∇g(x_k)^T d + g(x_k) ≤ 0

Burada:
  d    = Arama yönü
  B_k  = Lagrangian Hessian yaklaşımı (BFGS ile)
  x_k  = Mevcut iterasyon noktası

Yakınsama: Süper-doğrusal (Q-süper-doğrusal), 10-50 iterasyon
```

**Parametreler:**

| Parametre | Tipik Değer | Açıklama |
|-----------|------------|----------|
| maxiter | 200 | Maksimum iterasyon |
| ftol | 1e-8 | Fonksiyon toleransı |
| Gradient | Finite difference | Analitik tercih edilir |
| Hessian | BFGS yaklaşımı | Otomatik |

**Avantajlar/Dezavantajlar:**

| Avantaj | Dezavantaj |
|---------|-----------|
| Hızlı yakınsama | Yerel minimum riski |
| Kısıt desteği (doğrudan) | Gradient gerekir |
| Az fonksiyon değerlendirme | Başlangıç noktası hassasiyeti |
| İyi teorik temel | Konveks olmayan problemlerde garanti yok |

### 2.2. Interior Point (IP)

```
Tip: Barrier method, kısıtlı NLP
Teori: Eşitsizlik kısıtlarını logaritmik barrier ile amaç fonksiyonuna ekle

  min f(x) - μ Σ ln(s_j)
  s.t. g_j(x) + s_j = 0, s_j > 0

μ → 0 olarak azaltılır (barrier parametresi)
```

**Ne zaman kullanılmalı:**
- Büyük ölçekli seyrek problemler (100+ değişken)
- Doğrusal kısıtlar ağırlıklı problemler
- IPOPT (açık kaynak IP çözücü) kullanılabilir

---

## 3. Stokastik (Metaheuristik) Algoritmalar

### 3.1. GA (Genetic Algorithm)

```
Tip: Evrimsel, popülasyon tabanlı
İlham: Doğal seçilim ve genetik

Algoritma:
  1. Popülasyon başlat (rastgele veya sezgisel)
  2. Uygunluk (fitness) değerlendirmesi
  3. Seçim (Selection): Turnuva / Rulet çarkı
  4. Çaprazlama (Crossover): SBX / tek noktalı / iki noktalı
  5. Mutasyon (Mutation): Polinom / Gauss / uniform
  6. Yeni nesil oluştur
  7. Durdurma kriterine kadar tekrarla

Kodlama:
  - Gerçek sayı (real-valued): Sürekli değişkenler için
  - İkili (binary): 0/1 kararları için
  - Karışık: MINLP için
```

**Parametreler:**

| Parametre | Tipik Değer | Etki |
|-----------|------------|------|
| Popülasyon | 50-200 | Büyük → daha iyi arama, yavaş |
| Nesil | 100-500 | Daha fazla → daha iyi yakınsama |
| Çaprazlama oranı (p_c) | 0.7-0.9 | Yüksek → daha fazla arama (exploration) |
| Mutasyon oranı (p_m) | 0.01-0.10 | Düşük → ince ayar, yüksek → çeşitlilik |
| Turnuva boyutu | 2-5 | Büyük → daha agresif seçim |
| Elitizm | 1-5 birey | En iyileri koru |

### 3.2. PSO (Particle Swarm Optimization)

```
Tip: Sürü tabanlı, popülasyon tabanlı
İlham: Kuş sürüsü davranışı

Hız güncelleme:
  v_i(t+1) = w·v_i(t) + c₁·r₁·(pbest_i - x_i(t)) + c₂·r₂·(gbest - x_i(t))

Konum güncelleme:
  x_i(t+1) = x_i(t) + v_i(t+1)

Burada:
  w    = İnersia ağırlığı (tipik 0.4-0.9, azalan)
  c₁   = Bilişsel çarpan (tipik 1.5-2.0)
  c₂   = Sosyal çarpan (tipik 1.5-2.0)
  r₁,r₂ = [0,1] rastgele sayılar
  pbest = Parçacığın kişisel en iyisi
  gbest = Sürünün global en iyisi
```

**Parametreler:**

| Parametre | Tipik Değer | Etki |
|-----------|------------|------|
| Parçacık sayısı | 30-100 | Büyük → daha iyi arama |
| İterasyonlar | 100-500 | Daha fazla → daha iyi yakınsama |
| w (inersia) | 0.9 → 0.4 (azalan) | Başta arama, sonda ince ayar |
| c₁ (bilişsel) | 1.5-2.0 | Kişisel deneyim etkisi |
| c₂ (sosyal) | 1.5-2.0 | Sürü bilgisi etkisi |
| v_max | x_max - x_min | Hız sınırı |

### 3.3. DE (Differential Evolution)

```
Tip: Evrimsel, popülasyon tabanlı
İlham: Vektör farkı ile evrim

Mutasyon:
  v_i = x_r1 + F × (x_r2 - x_r3)    (DE/rand/1)

Çaprazlama:
  u_ij = v_ij  eğer rand < CR veya j = j_rand
  u_ij = x_ij  diğer durumlarda

Seçim (greedy):
  x_i(t+1) = u_i  eğer f(u_i) < f(x_i)
  x_i(t+1) = x_i  diğer durumlarda
```

**Parametreler:**

| Parametre | Tipik Değer | Etki |
|-----------|------------|------|
| Popülasyon (NP) | 5×n ile 10×n | n = değişken sayısı |
| Ölçek faktörü (F) | 0.5-0.9 | Mutasyon şiddeti |
| Çaprazlama oranı (CR) | 0.7-0.9 | Vektör karışımı |
| Strateji | DE/rand/1/bin | En yaygın |

**DE Avantajları:**
- Az parametre, kolay ayar
- GA'ya göre genellikle daha iyi yakınsama
- Kısıt işleme basit (ceza fonksiyonu)

### 3.4. NSGA-II (Çok Amaçlı)

Detaylı açıklama `multi_objective.md` dosyasında.

---

## 4. Hibrit Yöntemler

### 4.1. GA + SQP Kombinasyonu

```
Strateji:
  1. GA ile global arama yap (50-100 nesil, geniş popülasyon)
  2. GA'nın en iyi N çözümünü al
  3. Her çözümü SQP'ye başlangıç noktası olarak ver
  4. SQP ile yerel iyileştirme yap

                 ┌─────────┐     ┌─────────┐
  Başla ──→      │   GA    │ ──→ │   SQP   │ ──→ Optimal
  (Global)       │(arama)  │     │(iyileşt.)│     Çözüm
                 └─────────┘     └─────────┘
                 50-100 nesil     10-50 iter.
                 1000-5000        50-200
                 değerlendirme    değerlendirme

Avantaj: GA'nın global arama + SQP'nin hassas yakınsama
Toplam maliyet: ~5000-7000 fonksiyon değerlendirme (yalnız GA: 10000+)
```

### 4.2. Uygulama Önerisi

```python
from scipy.optimize import minimize, differential_evolution

def hybrid_optimization(func, bounds, constraints=None):
    """GA(DE) + SQP hibrit optimizasyon."""

    # Faz 1: Global arama (DE)
    de_result = differential_evolution(
        func, bounds,
        maxiter=100,
        popsize=15,
        tol=1e-4,
        seed=42
    )

    # Faz 2: Yerel iyileştirme (SQP)
    sqp_result = minimize(
        func, de_result.x,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'maxiter': 200, 'ftol': 1e-10}
    )

    return sqp_result
```

---

## 5. Yazılım Araçları

### 5.1. Genel Karşılaştırma

| Yazılım | Dil | Maliyet | Tek Amaçlı | Çok Amaçlı | MINLP | Termodinamik |
|---------|-----|---------|-----------|-----------|-------|-------------|
| scipy | Python | Açık kaynak | SQP, DE, NM | Hayır | Hayır | CoolProp ile |
| pymoo | Python | Açık kaynak | Hayır | NSGA-II, NSGA-III | GA ile | CoolProp ile |
| DEAP | Python | Açık kaynak | GA, PSO | NSGA-II | GA ile | CoolProp ile |
| pyomo | Python | Açık kaynak | IPOPT, BONMIN | Hayır | BONMIN | CoolProp ile |
| MATLAB fmincon | MATLAB | Ticari | SQP, IP | Hayır | Hayır | - |
| MATLAB gamultiobj | MATLAB | Ticari | - | NSGA-II | - | - |
| GAMS | GAMS | Ticari | CONOPT, IPOPT | Hayır | BARON, DICOPT | - |
| EES | EES | Ticari | Newton-Raphson | Hayır | Hayır | Dahili |
| jMetalPy | Python | Açık kaynak | - | NSGA-II, MOEA/D | - | CoolProp ile |

### 5.2. Python Ekosistemi Detay

```
Temel paketler:
  scipy.optimize    — minimize (SLSQP, L-BFGS-B), differential_evolution
  pymoo             — NSGA-II, NSGA-III, MOEA/D, çok amaçlı
  DEAP              — GA, PSO, özelleştirilebilir EA
  pyomo + IPOPT     — NLP/MINLP, algebrik modelleme
  CoolProp          — Termodinamik özellikler (su/buhar, soğutucu)
  numpy/pandas      — Veri işleme
  matplotlib        — Pareto front görselleştirme

Kurulum:
  pip install scipy pymoo deap pyomo coolprop matplotlib

IPOPT (pyomo ile):
  conda install -c conda-forge ipopt
```

### 5.3. EES (Engineering Equation Solver)

```
Özellikler:
  - Dahili termodinamik kütüphaneler (su, hava, soğutucu, ideal gaz)
  - Newton-Raphson çözücü (eşitlik sistemleri)
  - min/max komutu ile basit optimizasyon
  - Parametrik tablolar
  - Diagram penceresi

Avantaj: Termodinamik problemler için hızlı geliştirme
Dezavantaj: Sınırlı optimizasyon yetenekleri, MINLP yok
Kullanım: Akademik çalışmalar, hızlı prototipleme
```

---

## 6. Algoritma Seçim Rehberi

### 6.1. Karar Matrisi

| Problem Tipi | Değişken | Kısıt | Önerilen Algoritma |
|-------------|---------|-------|-------------------|
| NLP, konveks, <10 değ. | Sürekli | Var | SQP |
| NLP, konveks olmayan, <10 değ. | Sürekli | Var | Multi-start SQP |
| NLP, konveks olmayan, 10-30 değ. | Sürekli | Var | DE + SQP (hibrit) |
| NLP, konveks olmayan, 30+ değ. | Sürekli | Var | DE veya PSO |
| MINLP, <10 ikili | Karışık | Var | B&B veya GA |
| MINLP, 10+ ikili | Karışık | Var | GA (binary+real) |
| Çok amaçlı, 2 amaç | Sürekli | Var | NSGA-II |
| Çok amaçlı, 3+ amaç | Sürekli | Var | NSGA-III veya MOEA/D |
| Çok amaçlı + MINLP | Karışık | Var | NSGA-II (binary+real) |

### 6.2. Termoekonomik Problemler İçin Öneriler

| Termoekonomik Problem | Algoritma | Gerekçe |
|----------------------|-----------|---------|
| Tek kazan parametrik opt. | SQP (multi-start) | Basit, hızlı, yeterli |
| CHP sistemi parametrik | DE + SQP | Konveks olmayan, 10-15 değişken |
| CHP yapısal + parametrik | GA (binary+real) | MINLP, ikili kararlar |
| Fabrika çok amaçlı | NSGA-II | Pareto cephesi gerekli |
| Isı geri kazanım ağı | GA + SQP | Eşleşme kararları + parametre |
| Hızlı tarama (enerji denetimi) | SQP | Hız kritik |

---

## 7. Performans Karşılaştırma (Tipik Termoekonomik Problem)

10 değişkenli CHP sistemi optimizasyonu:

| Algoritma | Opt. Değer | Fonk. Değ. | Güvenilirlik | Süre (göreli) |
|-----------|-----------|-----------|-------------|--------------|
| SQP (tek başlangıç) | 458,200 | 85 | %70 | 1× |
| SQP (10 başlangıç) | 457,500 | 850 | %95 | 10× |
| GA (pop=100, gen=200) | 457,800 | 20,000 | %90 | 230× |
| DE (pop=100, gen=200) | 457,600 | 20,000 | %95 | 230× |
| PSO (n=50, iter=200) | 457,900 | 10,000 | %85 | 115× |
| DE + SQP (hibrit) | 457,500 | 5,200 | %99 | 60× |
| NSGA-II (2 amaç) | Pareto (50 nk.) | 60,000 | %95 | 700× |

> **Sonuç:** Tek amaçlı parametrik problemde, DE+SQP hibrit yöntem en iyi
> güvenilirlik/maliyet dengesini sunar. Çok amaçlı problemde NSGA-II standarttır.

---

## İlgili Dosyalar

- `parametric_optimization.md` — NLP çözüm yöntemleri
- `structural_optimization.md` — MINLP çözüm yöntemleri
- `multi_objective.md` — Çok amaçlı optimizasyon
- `sensitivity_analysis.md` — Duyarlılık analizi
- `practical_guide.md` — Uygulama rehberi

## Referanslar

- Nocedal, J. & Wright, S.J. (2006). *Numerical Optimization*. 2nd ed. Springer.
- Deb, K. (2001). *Multi-Objective Optimization Using Evolutionary Algorithms*. Wiley.
- Storn, R. & Price, K. (1997). "Differential Evolution." *J. of Global Optimization*, 11, 341-359.
- Kennedy, J. & Eberhart, R. (1995). "Particle Swarm Optimization." *IEEE ICNN*.
- Virtanen, P. et al. (2020). "SciPy 1.0." *Nature Methods*, 17, 261-272.
- Blank, J. & Deb, K. (2020). "pymoo." *IEEE Access*, 8, 89497-89509.
