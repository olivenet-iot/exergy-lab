---
title: "Çok Amaçlı Optimizasyon (Multi-Objective Optimization)"
category: thermoeconomic_optimization
keywords: [çok amaçlı optimizasyon, Pareto, NSGA-II, TOPSIS, epsilon-constraint, MOPSO]
related_files: [knowledge/factory/thermoeconomic_optimization/algorithms.md, knowledge/factory/thermoeconomic_optimization/trade_off_curves.md, knowledge/factory/thermoeconomic_optimization/objective_functions.md]
use_when: ["Maliyet-verimlilik-çevre dengesi kurulurken", "Pareto analizi ve karar destek yöntemleri gerektiğinde"]
priority: high
last_updated: 2026-02-02
---

# Çok Amaçlı Optimizasyon (Multi-Objective Optimization)

## 1. Temel Kavramlar

### 1.1. Neden Çok Amaçlı?

Endüstriyel enerji sistemlerinde genellikle birbirleriyle çelişen birden fazla hedef vardır:

| Amaç 1 | vs | Amaç 2 | Çelişki |
|--------|----|--------|---------|
| min Maliyet | ↔ | max Exergy Verimi | Verim artışı yatırım gerektirir |
| min Maliyet | ↔ | min CO₂ | Temiz teknoloji daha pahalı |
| max Verim | ↔ | min CO₂ | Yüksek verim her zaman düşük emisyon değil |
| min Yatırım | ↔ | min İşletme Maliyeti | Ucuz ekipman daha çok yakıt tüketir |

### 1.2. Pareto Optimalliği

```
Tanım: Çözüm A, Çözüm B'yi Pareto-baskılar (dominates) eğer:
  1. A, tüm amaçlarda B'den kötü değil VE
  2. A, en az bir amaçta B'den iyi

Pareto-optimal çözüm: Hiçbir çözüm tarafından baskılanmayan çözüm.
Pareto cephesi: Tüm Pareto-optimal çözümlerin kümesi.
```

### 1.3. Çok Amaçlı Formülasyon

```
min F(x) = [f₁(x), f₂(x), ..., f_m(x)]

s.t.
  h(x) = 0
  g(x) ≤ 0
  x_L ≤ x ≤ x_U

Tipik termoekonomik bi-objective:
  min f₁(x) = Ċ_total(x)    [€/h]    — Toplam maliyet hızı
  min f₂(x) = -η_ex(x)      [%]      — Exergy verimi (negatif çünkü min)

Tri-objective:
  min f₁(x) = Ċ_total(x)    [€/h]
  min f₂(x) = -η_ex(x)      [%]
  min f₃(x) = ṁ_CO₂(x)      [kg/h]
```

---

## 2. Çözüm Yöntemleri

### 2.1. NSGA-II (Non-dominated Sorting Genetic Algorithm II)

En yaygın kullanılan çok amaçlı evrimsel algoritma (Deb et al., 2002).

```
Algoritma:
  1. Rastgele N popülasyon oluştur
  2. Baskınlık sıralaması (non-dominated sorting):
     - Cephe 1: Hiç baskılanmayan çözümler
     - Cephe 2: Yalnızca Cephe 1 tarafından baskılananlar
     - ...
  3. Kalabalık mesafesi (crowding distance) hesapla
     - Pareto cephesinde iyi dağılım sağlar
  4. Turnuva seçimi (cephe sırası + kalabalık mesafesi)
  5. Çaprazlama (SBX) ve mutasyon (polinom)
  6. Birleşik popülasyondan N seç (elitizm)
  7. Nesil sayısı dolana kadar tekrarla

Parametreler:
  Popülasyon (N): 100-300
  Nesil: 200-500
  Çaprazlama oranı: 0.9
  Mutasyon oranı: 1/n (n = değişken sayısı)
  SBX η_c: 20
  Mutasyon η_m: 20
```

### 2.2. MOPSO (Multi-Objective Particle Swarm Optimization)

```
Algoritma:
  1. Parçacık sürüsü başlat (konum + hız)
  2. Her parçacık için:
     - Kişisel en iyi (pbest) güncelle
     - Global en iyi (gbest) → Harici arşivden seç
  3. Hız güncelle:
     v = w·v + c₁·r₁·(pbest - x) + c₂·r₂·(gbest - x)
  4. Konum güncelle: x = x + v
  5. Harici arşivi Pareto-optimal çözümlerle güncelle
  6. Tekrarla

Avantaj: NSGA-II'den daha az parametre, daha hızlı yakınsama
Dezavantaj: Çeşitlilik kaybı riski (arşiv yönetimi kritik)
```

### 2.3. Epsilon-Constraint Yöntemi

```
Bir amaç fonksiyonunu optimize et, diğerlerini kısıta dönüştür:

min f₁(x)
s.t.
  f₂(x) ≤ ε₂
  f₃(x) ≤ ε₃
  ...
  h(x) = 0, g(x) ≤ 0

ε₂'yi sistematik olarak değiştirerek Pareto cephesi oluştur:
  ε₂ ∈ {ε₂,min, ε₂,min + Δε, ε₂,min + 2Δε, ..., ε₂,max}

Her ε değeri için bir NLP çöz → Pareto noktası bul.

Avantaj: Deterministik, kontrollü çözüm kalitesi
Dezavantaj: m-1 boyutta ε taraması (curse of dimensionality)
```

### 2.4. Weighted Sum (Ağırlıklı Toplam)

```
min F(x) = w₁·f₁(x) + w₂·f₂(x) + ... + w_m·f_m(x)

s.t. Σw_i = 1, w_i > 0

w₁ ve w₂'yi sistematik değiştirerek farklı çözümler bul.

Avantaj: Basit implementasyon
Dezavantaj: Konveks olmayan Pareto cephelerinde çözüm üretemez
           Ağırlık-çözüm ilişkisi doğrusal değil
```

---

## 3. Karar Destek Yöntemleri

Pareto cephesinden tek bir "en iyi" çözüm seçmek gerektiğinde:

### 3.1. TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)

```
Adımlar:
  1. Karar matrisini normalize et:
     r_ij = f_ij / sqrt(Σ f_ij²)

  2. Ağırlıklandır:
     v_ij = w_j × r_ij

  3. İdeal (A⁺) ve negatif ideal (A⁻) çözüm belirle:
     A⁺_j = min(v_ij) (minimize amaçlar için)
     A⁻_j = max(v_ij)

  4. Her çözümün ideal ve negatif ideale uzaklığını hesapla:
     S⁺_i = sqrt(Σ (v_ij - A⁺_j)²)
     S⁻_i = sqrt(Σ (v_ij - A⁻_j)²)

  5. Göreceli yakınlık:
     C_i = S⁻_i / (S⁺_i + S⁻_i)

  6. En yüksek C_i → En iyi çözüm
```

### 3.2. LINMAP (Linear Programming Technique for Multidimensional Analysis of Preference)

```
İdeal noktaya en yakın Pareto çözümünü seç:

min d_i = sqrt(Σ w_j × (f_ij - f_j^ideal)²)

Burada f_j^ideal her amaç fonksiyonunun tek başına optimal değeri.
```

### 3.3. Diz Noktası (Knee Point)

```
Pareto cephesindeki "diz" noktası: Marjinal ödünleşimin en fazla değiştiği nokta.

Geometrik tanım:
  Pareto cephesinin iki uç noktası arasındaki doğruya
  en uzak Pareto noktası = diz noktası.

Avantaj: Ağırlıklara bağlı değil, "doğal" denge noktası
```

---

## 4. Türkiye Bağlamı: Sektör Bazlı Ağırlık Önerileri

| Sektör | w_maliyet | w_verim | w_CO₂ | Gerekçe |
|--------|-----------|---------|-------|---------|
| Çimento | 0.35 | 0.25 | 0.40 | CBAM doğrudan etkili |
| Demir-çelik | 0.30 | 0.25 | 0.45 | CBAM çok yüksek etkili |
| Gıda | 0.50 | 0.30 | 0.20 | CBAM kapsamı dışında, maliyet kritik |
| Tekstil | 0.45 | 0.35 | 0.20 | Rekabetçilik önemli |
| Kimya | 0.35 | 0.30 | 0.35 | CBAM kısmen etkili |
| Otomotiv | 0.40 | 0.25 | 0.35 | Yeşil tedarik zinciri baskısı |
| Kağıt | 0.40 | 0.35 | 0.25 | Biyokütle fırsatı |

> **Not:** Bu ağırlıklar başlangıç önerisidir. Her fabrikanın stratejik öncelikleri
> farklı olabilir. Karar verici ile birlikte belirlenmelidir.

---

## 5. Hesaplama Örneği: Bi-objective Utility System

### 5.1. Problem Tanımı

- Gıda fabrikası yardımcı tesis sistemi
- Kazan (3,000 kW) + Kompresör (75 kW) + Chiller (300 kW)
- Amaçlar: min C_total vs max η_ex
- 6 karar değişkeni

### 5.2. Pareto Front Verisi

NSGA-II ile elde edilen 10 temsili Pareto noktası:

| # | η_ex [%] | C_total [€/yıl] | T_stack [°C] | λ [%] | A_eco [m²] | COP |
|---|---------|-----------------|-------------|-------|-----------|-----|
| A | 24.1 | 485,000 | 250 | 20 | 10 | 4.5 |
| B | 25.8 | 478,000 | 220 | 16 | 20 | 4.8 |
| C | 27.5 | 470,000 | 195 | 13 | 32 | 5.0 |
| D | 29.0 | 464,000 | 175 | 11 | 42 | 5.2 |
| E | 30.2 | 460,000 | 160 | 9.5 | 50 | 5.3 |
| F | 31.1 | 458,000 | 150 | 8.5 | 58 | 5.4 |
| **G** | **31.8** | **457,500** | **145** | **8.0** | **62** | **5.5** |
| H | 32.5 | 460,000 | 138 | 7.5 | 72 | 5.6 |
| I | 33.0 | 465,000 | 132 | 7.0 | 85 | 5.7 |
| J | 33.8 | 478,000 | 125 | 6.5 | 110 | 5.8 |

### 5.3. TOPSIS Karar Analizi

Ağırlıklar: w_maliyet = 0.50, w_verim = 0.50

```
Normalizasyon ve TOPSIS uygulaması:

İdeal çözüm: (C_total = 457,500; η_ex = 33.8%)
Negatif ideal: (C_total = 485,000; η_ex = 24.1%)

TOPSIS sıralaması:
  1. Nokta G: C_i = 0.742 ← EN İYİ
  2. Nokta F: C_i = 0.718
  3. Nokta H: C_i = 0.703
  4. Nokta E: C_i = 0.685
  ...
```

### 5.4. Diz Noktası Analizi

```
Pareto cephesinin uç noktaları: A (düşük verim/ucuz) ve J (yüksek verim/pahalı)
A-J doğrusuna en uzak nokta: G (mesafe = 0.82)

Diz noktası = G → TOPSIS ile uyumlu!
```

### 5.5. Sonuç

| Karar Yöntemi | Seçilen Nokta | η_ex [%] | C_total [€/yıl] |
|--------------|-------------|---------|-----------------|
| Minimum maliyet | F | 31.1 | 458,000 |
| Maksimum verim | J | 33.8 | 478,000 |
| TOPSIS (50/50) | G | 31.8 | 457,500 |
| Diz noktası | G | 31.8 | 457,500 |
| TOPSIS (70/30 maliyet) | F | 31.1 | 458,000 |
| TOPSIS (30/70 verim) | H | 32.5 | 460,000 |

**Yorum:** Nokta G, hem TOPSIS hem de diz noktası yöntemlerinin seçtiği robust
(sağlam) bir çözümdür. Bu noktada %31.8 exergy verimi, 457,500 €/yıl maliyetle elde edilir.

---

## 6. Karbon Fiyatlaması ile Tri-objective

### 6.1. Ek Amaç: min CO₂

Aynı sisteme CO₂ emisyon minimizasyonu eklendiğinde:

| c_CO₂ [€/tCO₂] | Optimal η_ex [%] | C_total [€/yıl] | CO₂ [ton/yıl] |
|----------------|-----------------|-----------------|---------------|
| 0 (karbon yok) | 31.8 | 457,500 | 2,180 |
| 50 | 32.8 | 495,000 | 1,950 |
| 80 | 33.5 | 525,000 | 1,820 |
| 100 | 34.0 | 548,000 | 1,740 |

> **Çıkarım:** Karbon fiyatı arttıkça, optimal çözüm daha yüksek exergy verimine kayar.
> Bu, enerji tasarrufu yatırımlarını ekonomik olarak daha çekici hale getirir.

---

## 7. Python İmplementasyonu (pymoo)

```python
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.optimize import minimize as pymoo_minimize
from pymoo.termination import get_termination
import numpy as np

class ThermoeconomicProblem(Problem):
    def __init__(self):
        super().__init__(
            n_var=6,
            n_obj=2,
            n_ieq_constr=2,
            xl=np.array([0.05, 120, 0, 60, 4.0, 25]),
            xu=np.array([0.30, 300, 200, 105, 6.0, 45])
        )

    def _evaluate(self, X, out, *args, **kwargs):
        # X sütunları: excess_air, T_stack, A_eco, T_fw, COP, T_cond
        f1 = np.array([self.total_cost(x) for x in X])    # min C_total
        f2 = np.array([-self.exergy_eff(x) for x in X])   # max η_ex (min -η_ex)

        # Kısıtlar
        g1 = X[:, 1] - X[:, 3] - 20   # T_stack > T_fw + 20
        g2 = 120 - X[:, 1]            # T_stack > 120

        out["F"] = np.column_stack([f1, f2])
        out["G"] = np.column_stack([-g1, g2])

    def total_cost(self, x):
        # Basitleştirilmiş toplam maliyet hesabı
        # ... (detaylı implementasyon)
        return cost

    def exergy_eff(self, x):
        # Sistem exergy verimi
        # ... (detaylı implementasyon)
        return eta_ex

# NSGA-II çalıştır
algorithm = NSGA2(
    pop_size=200,
    crossover=SBX(prob=0.9, eta=20),
    mutation=PM(eta=20),
    eliminate_duplicates=True
)

problem = ThermoeconomicProblem()
termination = get_termination("n_gen", 300)

res = pymoo_minimize(
    problem, algorithm, termination,
    seed=42, verbose=True
)

# Pareto cephesi
pareto_costs = res.F[:, 0]
pareto_eff = -res.F[:, 1]  # Negatifi geri çevir

print(f"Pareto çözüm sayısı: {len(res.F)}")
print(f"C_total aralığı: {pareto_costs.min():,.0f} - {pareto_costs.max():,.0f} €/yıl")
print(f"η_ex aralığı: {pareto_eff.min():.1f} - {pareto_eff.max():.1f} %")
```

---

## 8. Pratik Öneriler

### 8.1. Amaç Fonksiyonu Sayısı

- **2 amaç (bi-objective):** En yaygın, yorumlanması kolay, 2D Pareto cephesi
- **3 amaç (tri-objective):** Karbon dahil, 3D Pareto yüzeyi — görselleştirme zor
- **4+ amaç:** Akademik olarak mümkün ama pratikte gereksiz — karar vermek zorlaşır

### 8.2. Popülasyon Boyutu Seçimi

| Değişken Sayısı | Amaç Sayısı | Önerilen Popülasyon |
|----------------|-------------|-------------------|
| 3-6 | 2 | 100-200 |
| 6-15 | 2 | 200-300 |
| 3-6 | 3 | 200-300 |
| 15+ | 2 | 300-500 |

### 8.3. Yakınsama Doğrulaması

1. Nesil sayısını artır, Pareto cephesi değişmiyorsa yakınsamış
2. Farklı seed değerleriyle tekrarla, benzer cephe çıkmalı
3. Hypervolume indikatörünü izle (artık artmıyorsa yakınsamış)

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `objective_functions.md` — Amaç fonksiyonları detayı
- `algorithms.md` — Algoritma detayları (NSGA-II, MOPSO)
- `trade_off_curves.md` — Ödünleşim eğrileri ve yorumlama
- `sensitivity_analysis.md` — Duyarlılık analizi
- `worked_examples/chp_optimization.md` — CHP çok amaçlı örnek
- `factory/economic_analysis.md` — Ekonomik analiz

## Referanslar

- Deb, K. et al. (2002). "A fast and elitist multiobjective genetic algorithm: NSGA-II." *IEEE Transactions on Evolutionary Computation*, 6(2), 182-197.
- Hwang, C.L. & Yoon, K. (1981). *Multiple Attribute Decision Making*. Springer.
- Coello Coello, C.A. et al. (2007). *Evolutionary Algorithms for Solving Multi-Objective Problems*. 2nd ed. Springer.
- Blank, J. & Deb, K. (2020). "pymoo: Multi-Objective Optimization in Python." *IEEE Access*, 8, 89497-89509.
