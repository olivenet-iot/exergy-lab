---
title: "Exergoekonomik Optimizasyon (Exergoeconomic Optimization)"
category: factory
equipment_type: factory
keywords: [optimizasyon, maliyet minimizasyonu, f_k, r_k, Pareto, NSGA-II, iteratif]
related_files:
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/exergoeconomic/advanced_exergoeconomic.md
  - factory/exergoeconomic/sensitivity_analysis.md
  - factory/exergoeconomic/exergoeconomic_balance.md
use_when:
  - "Exergoekonomik optimizasyon yapılırken"
  - "Ċ_D + Ż minimizasyonu hedeflenirken"
  - "f_k/r_k tabanlı iteratif iyileştirme uygulanırken"
  - "Çok amaçlı optimizasyon planlanırken"
priority: medium
last_updated: 2026-02-01
---
# Exergoekonomik Optimizasyon (Exergoeconomic Optimization)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Exergoekonomik optimizasyonun amacı, toplam ürün maliyetini minimize etmektir. Bu, bileşen bazında exergy yıkım maliyeti (Ċ_D) ile yatırım maliyeti (Ż) arasındaki dengeyi (trade-off) optimize etmeyi gerektirir.

```
Amaç Fonksiyonu:

min Ċ_P,toplam = Σ (Ċ_D,k + Ż_k)  ∀ bileşen k

veya eşdeğer olarak:
min c_P,ürün  (birim ürün exergy maliyetini minimize et)

Trade-off:
  Yatırım ↑ (daha verimli ekipman) → Ė_D ↓ → Ċ_D ↓
  Yatırım ↓ (daha ucuz ekipman) → Ė_D ↑ → Ċ_D ↑
  Optimum: Ċ_D + Ż minimum olduğu nokta
```

## 2. İteratif Tsatsaronis Yaklaşımı (f_k / r_k Tabanlı)

### 2.1 Metodoloji

Bu yaklaşım, matematiksel optimizasyon yerine mühendislik bilgisine dayalı iteratif bir yöntemdir. Tsatsaronis tarafından önerilen bu yöntem pratikte en yaygın kullanılan exergoekonomik optimizasyon yaklaşımıdır.

```
İteratif Optimizasyon Adımları:

Adım 1: Standart exergoekonomik analiz yap
  → Ċ_D,k, Ż_k, f_k, r_k hesapla

Adım 2: Bileşenleri Ċ_D+Ż'ye göre sırala
  → En yüksek 3-5 bileşene odaklan

Adım 3: Her odak bileşen için f_k değerlendir
  f_k < 0.25 → Verimlilik artır (η_is ↑, ΔT ↓, vb.)
  0.25 < f_k < 0.70 → Her iki yönde ince ayar dene
  f_k > 0.70 → Maliyet azalt (ucuz malzeme, küçük boyut)

Adım 4: Tasarım değişikliğini uygula
  → İlgili parametreyi değiştir (η_is, A, ΔT_min, vb.)

Adım 5: Sistemi yeniden simüle et ve exergoekonomik analizi tekrarla

Adım 6: Toplam maliyet azaldı mı?
  Evet → Adım 2'ye dön (iyileştirmeye devam)
  Hayır → Son iterasyona geri dön → Optimum bulundu

Yakınsama kriteri: |ΔĊ_P,toplam| < ε (örn. <%1 değişim)
```

### 2.2 Parametre Ayarlama Rehberi

```
f_k < 0.25 → Verimlilik Artırma:
┌────────────────────────────────────────────────┐
│ Kompresör/Türbin:                               │
│   η_is ↑ (+%2-5 artır)                         │
│   → Daha iyi kanat profili, çok kademeli       │
│                                                  │
│ Kazan:                                           │
│   Baca gazı T ↓ (ekonomizer ekle/genişlet)      │
│   Fazla hava % ↓ (O₂ kontrol)                  │
│   → Isı geri kazanım artır                     │
│                                                  │
│ Isı Değiştirici:                                 │
│   ΔT_min ↓ (alan A ↑)                          │
│   → Daha fazla transfer alanı                   │
│                                                  │
│ Pompa:                                           │
│   η_pompa ↑ (doğru boyutlandırma)               │
│   Çark profili optimize et                      │
│                                                  │
│ Chiller:                                         │
│   COP ↑ (kondenser optimize, VSD ekle)          │
└────────────────────────────────────────────────┘

f_k > 0.70 → Maliyet Azaltma:
┌────────────────────────────────────────────────┐
│ Tüm ekipmanlar:                                 │
│   Daha ucuz malzeme düşün (CS yerine SS?)       │
│   Daha küçük kapasite (right-sizing)            │
│   Standart boyut kullan (özel imalat yerine)    │
│   Verimlilikten küçük ödün kabul et             │
│   → PEC düşürmeye odaklan                       │
└────────────────────────────────────────────────┘
```

### 2.3 Gaz Türbin Sistemi İteratif Örnek

```
İterasyon 0 (Başlangıç Tasarım):
  Kompresör: η_is = 0.85, f_k = 0.12 → Verimlilik artır
  Yanma odası: f_k = 0.01 → Verimlilik artır (ama sınırlı)
  Türbin: η_is = 0.88, f_k = 0.68 → Dengeli
  c_P,elektrik = 42.5 €/MWh

İterasyon 1:
  Kompresör: η_is → 0.88 (+%3)
  → PEC ↑ %12, Ė_D ↓ %18
  → f_k = 0.17 → Hâlâ düşük, devam
  c_P,elektrik = 40.8 €/MWh (↓%4.0)

İterasyon 2:
  Kompresör: η_is → 0.90 (+%2)
  Yanma odası: Hava ön ısıtma eklendi → η_CC ↑ %1.5
  → f_k,kompresör = 0.24
  → f_k,CC = 0.02 (hâlâ çok düşük ama kaçınılmaz)
  c_P,elektrik = 39.2 €/MWh (↓%3.9)

İterasyon 3:
  Kompresör: η_is → 0.92 (+%2)
  → PEC ↑ %25, Ė_D ↓ %8 (azalan getiri)
  → f_k = 0.38 → Dengeli bölge
  c_P,elektrik = 39.0 €/MWh (↓%0.5 → yakınsadı)

Sonuç: Optimum η_is,kompresör ≈ 0.90-0.92
  Toplam iyileştirme: 42.5 → 39.0 €/MWh (%8.2 azalma)
```

## 3. Matematiksel Optimizasyon

### 3.1 Tek Amaçlı Optimizasyon

```
Formülasyon:

min f(x) = Ċ_P,toplam(x) = Σ [Ċ_D,k(x) + Ż_k(x)]

Kısıtlar:
  g_i(x) ≤ 0  (eşitsizlik kısıtları)
  h_j(x) = 0  (eşitlik kısıtları)
  x_L ≤ x ≤ x_U  (değişken sınırları)

Karar değişkenleri x:
  η_is,kompresör, η_is,türbin, ΔT_min,HX, P_buhar, T_buhar, ...

Kısıtlar:
  - Termodinamik denge (kütle, enerji, exergy)
  - Malzeme sıcaklık sınırları
  - Minimum/maksimum basınç
  - Emisyon limitleri
  - Kapasite gereksinimleri
```

### 3.2 Çok Amaçlı Optimizasyon

```
Formülasyon:

min f₁(x) = Ċ_P,toplam  (toplam maliyet)
min f₂(x) = Σ Ė_D,k     (toplam exergy yıkımı)
[opsiyonel] min f₃(x) = Σ Ḃ_D,k  (toplam çevresel etki)

→ Pareto-optimal çözüm kümesi elde edilir
→ Karar verici Pareto eğrisi üzerinden seçim yapar

Tipik trade-off:
  Yüksek verimlilik → Düşük Ė_D → Yüksek maliyet
  Düşük maliyet → Yüksek Ė_D → Düşük yatırım
  Pareto optimal → En iyi denge noktaları
```

### 3.3 Optimizasyon Algoritmaları

| Algoritma | Tip | Avantaj | Dezavantaj | Uygunluk |
|-----------|-----|---------|------------|----------|
| Gradient-based (SQP) | Tek amaçlı | Hızlı yakınsama | Lokal optimum riski | Pürüzsüz fonksiyonlar |
| Genetik Algoritma (GA) | Tek/çok amaçlı | Global arama | Yavaş | Karmaşık sistemler |
| NSGA-II | Çok amaçlı | Pareto seti | Çok değerlendirme | Çok amaçlı |
| PSO | Tek/çok amaçlı | Basit uygulama | Ayar hassas | Orta karmaşıklık |
| Simulated Annealing | Tek amaçlı | Global arama | Yavaş | Kesikli değişkenler |

### 3.4 Python ile Basit Optimizasyon Kodu

```python
import numpy as np
from scipy.optimize import minimize

def total_cost(x, system_params):
    """Toplam exergoekonomik maliyet hesabı.

    Args:
        x: Karar değişkenleri [eta_is_comp, eta_is_turb, DT_min_HX]
        system_params: Sistem sabit parametreleri

    Returns:
        C_total: Toplam maliyet [€/saat]
    """
    eta_comp, eta_turb, DT_min = x

    # Exergy yıkımları (basitleştirilmiş model)
    ED_comp = system_params['W_comp'] * (1 - eta_comp) / eta_comp
    ED_turb = system_params['W_turb'] * (1/eta_turb - 1)
    ED_HX = system_params['Q_HX'] * DT_min / system_params['T_avg']

    # PEC korelasyonları (basitleştirilmiş)
    PEC_comp = system_params['PEC_base_comp'] * (1 / (1 - eta_comp))**0.6
    PEC_turb = system_params['PEC_base_turb'] * (1 / (1 - eta_turb))**0.6
    PEC_HX = system_params['PEC_base_HX'] * (1 / DT_min)**0.7

    # Z-dot hesabı
    CRF = system_params['CRF']
    tau = system_params['tau']
    Z_comp = CRF * PEC_comp * 1.4 / tau  # 1.4 = (1 + phi_OM)
    Z_turb = CRF * PEC_turb * 1.4 / tau
    Z_HX = CRF * PEC_HX * 1.4 / tau

    # C_D hesabı
    cF = system_params['c_fuel']
    CD_comp = cF * ED_comp
    CD_turb = cF * ED_turb
    CD_HX = cF * ED_HX

    C_total = (CD_comp + Z_comp) + (CD_turb + Z_turb) + (CD_HX + Z_HX)
    return C_total

# Sistem parametreleri
params = {
    'W_comp': 5000,  # kW
    'W_turb': 8000,  # kW
    'Q_HX': 3000,    # kW
    'T_avg': 500,    # K
    'PEC_base_comp': 200000,  # €
    'PEC_base_turb': 400000,  # €
    'PEC_base_HX': 100000,    # €
    'CRF': 0.1175,
    'tau': 7500,      # saat/yıl
    'c_fuel': 0.008e-3,  # €/kJ
}

# Optimizasyon
x0 = [0.85, 0.88, 15.0]  # Başlangıç tahmin
bounds = [(0.80, 0.95), (0.82, 0.97), (3, 30)]

result = minimize(total_cost, x0, args=(params,),
                  method='L-BFGS-B', bounds=bounds)

print(f"Optimum: eta_comp={result.x[0]:.3f}, "
      f"eta_turb={result.x[1]:.3f}, DT_min={result.x[2]:.1f} K")
print(f"Min maliyet: {result.fun:.2f} €/saat")
```

## 4. Kısıtlar ve Pratik Hususlar

### 4.1 Tipik Kısıtlar

```
Termodinamik:
  - 0.75 ≤ η_is ≤ 0.97 (türbomakineler)
  - ΔT_min ≥ 3 K (ısı değiştiriciler)
  - T_max ≤ T_malzeme_sınırı
  - P_max ≤ P_tasarım

Ekonomik:
  - TCI ≤ Bütçe_max
  - SPP ≤ SPP_hedef (genellikle ≤ 5 yıl)

Çevresel:
  - CO₂ ≤ Emisyon_limiti
  - NOx ≤ Emisyon_limiti

Operasyonel:
  - Q̇_ürün ≥ Talep_min
  - Ẇ_net ≥ Güç_talebi
```

### 4.2 Azalan Getiri (Diminishing Returns)

```
Her bileşende verimlilik artışının maliyeti artan bir fonksiyondur:

PEC ∝ (1/(1-η))^α  →  η ↑ → PEC üstel artış

Sonuç:
  η: %85 → %90: PEC +%20, Ė_D -%33 → Net kazanç yüksek
  η: %90 → %95: PEC +%60, Ė_D -%50 → Net kazanç orta
  η: %95 → %98: PEC +%200, Ė_D -%60 → Net kazanç düşük/negatif

Bu nedenle optimum η genellikle mevcut en iyi değerin altındadır.
```

## 5. Optimizasyon Sonuçlarının Doğrulanması

```
Doğrulama Kontrol Listesi:

□ Optimum noktada f_k değerleri 0.25-0.70 aralığında mı?
  (Hayır ise optimizasyon yetersiz olabilir)

□ Enerji ve kütle dengeleri sağlanıyor mu?

□ Karar değişkenleri fiziksel sınırlar içinde mi?

□ Farklı başlangıç noktalarıyla aynı optimuma yakınsıyor mu?
  (Hayır ise lokal optimum riski)

□ Duyarlılık analizi yapıldı mı?
  (Optimumun komşuluğunda maliyet nasıl değişiyor?)

□ Sonuçlar mühendislik sezgisi ile uyumlu mu?
```

## 6. Exergoenvironmental Optimizasyon (Kısa Giriş)

```
Exergoekonomik optimizasyonun çevresel versiyonu:

min f₁ = Σ (Ċ_D,k + Ż_k)  — Toplam maliyet
min f₂ = Σ (Ḃ_D,k + Ẏ_k)  — Toplam çevresel etki

Burada:
- Ḃ_D,k = b_F,k · Ė_D,k — Exergy yıkımının çevresel etkisi
- Ẏ_k = Bileşenin yaşam döngüsü çevresel etkisi
- b_F,k = Yakıt exergy'sinin birim çevresel etkisi [mPt/kJ]

→ İki boyutlu Pareto eğrisi: Maliyet vs Çevresel etki
→ Karar verici tercihlerine göre çözüm seçimi
```

## İlgili Dosyalar

- `factory/exergoeconomic/evaluation_criteria.md` — f_k, r_k, Ċ_D değerlendirme
- `factory/exergoeconomic/advanced_exergoeconomic.md` — AV/UN, EN/EX ayrımı
- `factory/exergoeconomic/sensitivity_analysis.md` — Duyarlılık analizi yöntemleri
- `factory/exergoeconomic/exergoeconomic_balance.md` — Maliyet denge denklemleri
- `factory/exergoeconomic/worked_examples/cogeneration.md` — CHP optimizasyon örneği

## Referanslar

1. Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
2. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Chapter 9.
3. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
4. Deb, K. (2002). "A fast and elitist multiobjective genetic algorithm: NSGA-II." *IEEE Trans. Evolutionary Computation*, 6(2), 182-197.
5. Ahmadi, P., Dincer, I. (2011). "Thermodynamic and exergoenvironmental analyses, and multi-objective optimization of a gas turbine power plant." *Applied Thermal Engineering*, 31(14-15), 2529-2540.
