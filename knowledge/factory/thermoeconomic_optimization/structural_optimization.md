---
title: "Yapısal Optimizasyon (Structural Optimization)"
category: thermoeconomic_optimization
keywords: [yapısal optimizasyon, üst-yapı, MINLP, konfigürasyon seçimi, CHP]
related_files: [knowledge/factory/thermoeconomic_optimization/parametric_optimization.md, knowledge/factory/thermoeconomic_optimization/decision_variables.md, knowledge/factory/thermoeconomic_optimization/algorithms.md]
use_when: ["Yeni tesis tasarımı veya büyük retrofit kararı gerektiğinde", "Sistem konfigürasyonu optimizasyonu yapılırken"]
priority: medium
last_updated: 2026-02-02
---

# Yapısal Optimizasyon (Structural Optimization)

## 1. Tanım ve Kapsam

Yapısal optimizasyon, bir enerji sisteminin **konfigürasyonunu** (hangi bileşenlerin dahil
edileceği, nasıl bağlanacağı) optimize eder. Parametrik optimizasyondan farklı olarak,
yalnızca sürekli parametreleri değil, aynı zamanda **ikili kararları** da içerir.

### Yapısal vs Parametrik

| Özellik | Yapısal | Parametrik |
|---------|---------|-----------|
| Soru | "Hangi bileşenler, nasıl bağlansın?" | "Mevcut yapıda parametreler ne olsun?" |
| Değişken tipi | İkili + Sürekli | Yalnızca Sürekli |
| Problem tipi | MINLP | NLP |
| Çözüm zorluğu | Yüksek | Orta |
| Uygun durum | Yeni tesis, büyük retrofit | Mevcut tesis ince ayarı |

---

## 2. Üst-Yapı Yaklaşımı (Superstructure)

### 2.1. Kavram

Üst-yapı, olası tüm sistem konfigürasyonlarını kapsayan bir "süper" akış şemasıdır.
Optimizasyon, bu üst-yapıdan en iyi alt-yapıyı (subset) seçer.

```
Üst-yapı örneği — Endüstriyel Enerji Sistemi:

                    ┌─────────┐
  Doğalgaz ───────→│  Kazan  │──→ Buhar
                    │ (y₁=1?) │
                    └─────────┘

  Doğalgaz ───────→┌─────────┐
                    │ Gaz      │──→ Elektrik
                    │ Türbini  │──→ Baca gazı ───┐
                    │ (y₂=1?) │                  │
                    └─────────┘                  │
                                                  ↓
                                            ┌─────────┐
                                            │  HRSG   │──→ Buhar
                                            │ (y₃=1?) │
                                            └─────────┘
                                                  │
                                            ┌─────────┐
                                            │Abs.Chill│──→ Soğutma
                                            │ (y₄=1?) │
                                            └─────────┘

  Elektrik(şebeke)→┌─────────┐
                    │ Elektrik│──→ Soğutma
                    │ Chiller │
                    │ (y₅=1?) │
                    └─────────┘

  Elektrik ──────→ ┌─────────┐
                    │Kompresör│──→ Basınçlı hava
                    │ (y₆=1)  │    │
                    └─────────┘    │ Atık ısı
                                    ↓
                              ┌─────────┐
                              │ Isı GK  │──→ Sıcak su
                              │ (y₇=1?) │
                              └─────────┘
```

İkili değişkenler (y₁...y₇), her bileşenin dahil edilip edilmeyeceğini belirler.

### 2.2. Tipik Yapısal Kararlar

| Karar | Alternatifler | İkili Değişken |
|-------|-------------|---------------|
| Enerji üretim modu | Ayrı üretim vs CHP | y_CHP |
| CHP tipi | Gaz türbini vs ICE vs Buhar türbini | y_GT, y_ICE, y_ST |
| Soğutma sistemi | Elektrik chiller vs Absorpsiyonlu | y_VC, y_abs |
| Isı geri kazanım | Var vs yok (her eşleşme için) | y_HR,ij |
| Economizer | Var vs yok | y_eco |
| VSD | Var vs yok (her motor için) | y_VSD,k |
| Buhar basınç seviyesi | Tek vs çift vs üçlü | y_LP, y_MP, y_HP |
| Yedek ekipman | Var vs yok | y_spare |

---

## 3. MINLP Formülasyonu

### 3.1. Genel Form

```
min f(x, y) = C_total(x, y)

Subject to:
  h(x, y) = 0         — Eşitlik kısıtları (denge denklemleri)
  g(x, y) ≤ 0         — Eşitsizlik kısıtları (sınırlar)
  x ∈ X ⊂ R^n_c       — Sürekli değişkenler
  y ∈ {0, 1}^n_b       — İkili değişkenler

Burada:
  f      = Amaç fonksiyonu (toplam yıllıklaştırılmış maliyet)
  x      = Sürekli değişkenler (T, P, ṁ, A)
  y      = İkili değişkenler (ekipman var/yok)
  h(x,y) = Kütle, enerji, exergy dengeleri (bileşen aktifse)
  g(x,y) = Kapasite, sıcaklık, basınç sınırları
```

### 3.2. Big-M Formülasyonu

İkili değişkenlerle bileşen aktivasyonu:

```
Bileşen k aktifse (y_k = 1):
  h_k(x) = 0    — Denge denklemleri geçerli
  g_k(x) ≤ 0    — Kısıtlar geçerli
  Q_k,min ≤ Q_k ≤ Q_k,max

Bileşen k aktif değilse (y_k = 0):
  Q_k = 0
  Ż_k = 0
  Ėx_D,k = 0

Big-M yöntemiyle:
  Q_k ≤ M × y_k    (M çok büyük sayı)
  Q_k ≥ Q_k,min × y_k
```

---

## 4. Çözüm Yöntemleri

### 4.1. Deterministik Yöntemler

#### Branch-and-Bound (B&B)

```
Süreç:
1. İkili değişkenleri gevşet (0 ≤ y ≤ 1)
2. NLP alt problemini çöz (alt sınır)
3. En kesirli y_k'yı seç, dallan (y_k = 0 ve y_k = 1)
4. Her dalda NLP çöz
5. Alt sınır ≥ en iyi üst sınır → dalı buda
6. Tüm dallar değerlendirilince dur

Avantaj: Global optimum garantisi (konveks NLP'de)
Dezavantaj: Konveks olmayan NLP'lerde garanti yok
Karmaşıklık: O(2^n_b) en kötü durumda
```

#### Outer Approximation (OA)

```
Süreç:
1. NLP alt problemi çöz (sabit y ile)
2. Çözümden doğrusallaştırma (cutting plane) türet
3. MILP ana problemi çöz (yeni y belirle)
4. Yeni y ile NLP çöz
5. Yakınsama sağlanana kadar tekrarla

Avantaj: B&B'den daha hızlı olabilir
Dezavantaj: Konveks NLP gerektirir
```

### 4.2. Metaheuristik Yöntemler

#### Genetik Algoritma (GA) — Binary Encoding

```
Kromozom yapısı:
[y₁, y₂, ..., y_n | x₁, x₂, ..., x_m]
 └── İkili kısım ──┘ └── Sürekli kısım ──┘

İkili kısım: 0/1 kodlama (bileşen var/yok)
Sürekli kısım: Gerçek sayı kodlama (parametreler)

Operatörler:
  - Çaprazlama: İkili kısım için tek/iki noktalı; sürekli kısım için SBX
  - Mutasyon: İkili kısım için bit flip; sürekli kısım için Gaussian
  - Seçim: Turnuva veya rulet çarkı
  - Uygulanabilirlik: Ceza fonksiyonu veya onarım operatörü

Parametreler:
  Popülasyon: 50-200
  Nesil: 100-500
  Çaprazlama oranı: 0.7-0.9
  Mutasyon oranı: 0.01-0.05 (ikili), 0.1-0.3 (sürekli)
```

### 4.3. Yöntem Seçimi Karar Matrisi

| Kriter | B&B | OA | GA |
|--------|-----|----|----|
| Konveks problem | En iyi | İyi | Gereksiz |
| Konveks olmayan | Garanti yok | Garanti yok | İyi |
| İkili değişken < 10 | İyi | İyi | Gereksiz |
| İkili değişken 10-20 | Orta | İyi | İyi |
| İkili değişken > 20 | Kötü | Orta | En iyi |
| Çözüm kalitesi | Yüksek* | Yüksek* | İyi |
| Hesaplama süresi | Orta-Yüksek | Orta | Yüksek |
| Implementasyon | Zor | Zor | Orta |

*Konveks problemlerde

---

## 5. Türkiye Endüstriyel Örnekler

### 5.1. CHP vs Ayrı Üretim — Tekstil Fabrikası

**Senaryo:** Bursa tekstil fabrikası, 500 kW elektrik + 1,500 kW ısı talebi

| Konfigürasyon | C_total [€/yıl] | η_ex [%] | CO₂ [ton/yıl] |
|--------------|-----------------|---------|---------------|
| Ayrı üretim (şebeke + kazan) | 285,000 | 22.5 | 1,850 |
| Gaz türbini CHP | 245,000 | 31.2 | 1,420 |
| ICE CHP | 238,000 | 33.1 | 1,380 |
| ICE CHP + Abs. chiller | 252,000 | 35.8 | 1,350 |

**Sonuç:** ICE CHP en düşük maliyetli, ancak soğutma ihtiyacı yüksekse trijenerasyon
daha iyi exergy verimini sağlar.

### 5.2. Gıda Fabrikası — Isı Geri Kazanım Ağı

**Senaryo:** Gaziantep gıda fabrikası, 4 sıcak akış + 3 soğuk akış

| Konfigürasyon | HX Sayısı | A_total [m²] | C_total [€/yıl] |
|--------------|-----------|-------------|-----------------|
| Isı GK yok | 0 | 0 | 420,000 |
| Minimum HX (pinch) | 3 | 45 | 365,000 |
| Maksimum GK | 6 | 120 | 348,000 |
| Optimal yapı | 4 | 75 | 340,000 |

**Sonuç:** Optimal yapı, pinch analizinden 1 fazla HX ekleyerek %19 maliyet düşüşü sağlar.

---

## 6. Pratik Zorluklar

### 6.1. Modelleme Zorlukları

1. **Konveks olmayan fonksiyonlar:** Ekipman maliyet korelasyonları genellikle konveks değil
2. **Kesikli doğrulama:** Çözümün gerçek ekipman boyutlarıyla uyumu
3. **Dinamik koşullar:** Mevsimsel yük değişimleri, tepe/düşük saat fiyatları
4. **Veri kalitesi:** Maliyet korelasyonları yaklaşıktır

### 6.2. Hesaplama Zorlukları

1. **Kombinatorik patlama:** 20 ikili değişken = 1 milyon konfigürasyon
2. **NLP alt problem zorluğu:** Her konfigürasyon için ayrı NLP çözmek gerekir
3. **Yakınsama:** Metaheuristikler global optimuma yakınsamayı garanti etmez

### 6.3. Ne Zaman Yapısal Optimizasyon Kullanılmalı?

| Durum | Yapısal Opt. | Alternatif |
|-------|-------------|-----------|
| Yeni tesis (greenfield) | Evet | - |
| Büyük retrofit (>500k € yatırım) | Evet | - |
| CHP kararı | Evet | Basit karşılaştırma |
| 2-3 alternatif konfigürasyon | Gereksiz | Manuel karşılaştırma |
| Isı geri kazanım ağı tasarımı | Evet | Pinch analizi + sezgisel |
| Mevcut sistem parametre ayarı | Hayır | Parametrik optimizasyon |
| Bütçe < 100k € | Genellikle gereksiz | İteratif yöntem |

---

## 7. Yazılım Araçları

| Yazılım | MINLP Desteği | Maliyet | Kullanım |
|---------|-------------|---------|----------|
| GAMS | Tam | Ticari | Profesyonel optimizasyon |
| Pyomo (Python) | Tam | Açık kaynak | Akademik + endüstriyel |
| MATLAB fmincon + GA | Kısmi | Ticari | Akademik |
| EES | Sınırlı | Ticari | Termodinamik + basit opt. |
| pymoo (Python) | Metaheuristik | Açık kaynak | Çok amaçlı |

### Python ile Basit MINLP Örneği (Pyomo)

```python
from pyomo.environ import *

model = ConcreteModel()

# İkili değişkenler
model.y_CHP = Var(within=Binary)
model.y_abs = Var(within=Binary)
model.y_eco = Var(within=Binary)

# Sürekli değişkenler
model.Q_boiler = Var(bounds=(0, 5000))  # kW
model.W_CHP = Var(bounds=(0, 2000))     # kW

# Amaç fonksiyonu
def obj_rule(m):
    C_fuel = fuel_cost(m)
    C_invest = investment_cost(m)
    C_env = emission_cost(m)
    return C_fuel + C_invest + C_env
model.obj = Objective(rule=obj_rule, sense=minimize)

# Kısıtlar
def heat_balance(m):
    return m.Q_boiler + heat_from_CHP(m) >= Q_demand
model.heat_bal = Constraint(rule=heat_balance)

# Bileşen aktivasyonu
def chp_activation(m):
    return m.W_CHP <= 2000 * m.y_CHP
model.chp_act = Constraint(rule=chp_activation)
```

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `parametric_optimization.md` — NLP çözüm yöntemleri
- `decision_variables.md` — Karar değişkenleri ve kısıtlar
- `algorithms.md` — Optimizasyon algoritmaları detayı
- `worked_examples/chp_optimization.md` — CHP optimizasyon örneği
- `factory/cogeneration.md` — Kojenerasyon bilgileri
- `factory/heat_integration.md` — Isı entegrasyonu
- `factory/pinch_analysis.md` — Pinch analizi

## Referanslar

- Frangopoulos, C.A. (2009). "A method to determine the power capacity and efficiency limits of combined cycle power plants." *Thermochimica Acta*, 382, 233-241.
- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Floudas, C.A. (1995). *Nonlinear and Mixed-Integer Optimization*. Oxford University Press.
- Grossmann, I.E. & Biegler, L.T. (2004). "Part I. An overview of existing techniques." *Computers & Chemical Engineering*, 28, 1209-1239.
