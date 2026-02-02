---
title: "Eşanjör Optimizasyonu — EGM (Heat Exchanger Optimization via EGM)"
category: factory
equipment_type: factory
keywords: [eşanjör, ısı değiştirici, NTU, approach temperature, counter-flow, S_gen ayrıştırma, baffle]
related_files: [factory/entropy_generation/heat_transfer_egm.md, factory/entropy_generation/fluid_flow_egm.md, factory/heat_integration.md, factory/pinch_analysis.md]
use_when: ["Eşanjör termodinamik optimizasyonu yapılacakken", "Approach temperature belirlenecekken", "Eşanjör boyutlandırma ve EGM analizi gerektiğinde"]
priority: high
last_updated: 2026-02-01
---
# Eşanjör Optimizasyonu — EGM (Heat Exchanger Optimization via EGM)

> Son güncelleme: 2026-02-01

## Genel Bakış

Entropi Üretimini Minimize Etme (Entropy Generation Minimization — EGM) yöntemi, ısı eşanjörlerinin termodinamik açıdan optimum tasarımı ve işletilmesi için en güçlü araçlardan biridir. Bejan tarafından sistematize edilen bu yaklaşım, eşanjördeki tüm tersinmezlik kaynaklarını ayrıştırarak her birini bağımsız olarak analiz eder ve toplam entropi üretimini minimum yapan tasarım noktasını belirler. Geleneksel enerji bazlı analizin aksine, EGM exergy yıkımının kök nedenlerini ortaya koyar ve mühendise iki temel soru sorar: "Kayıp nerede oluşuyor?" ve "Bu kayıp nasıl azaltılabilir?"

Bir eşanjörde iki ana tersinmezlik mekanizması vardır: sonlu sıcaklık farkı üzerinden ısı transferi ve viskoz sürtünmeden kaynaklanan basınç düşüşü. Bu iki mekanizma birbiriyle yarışır — birini azaltmaya çalışmak diğerini artırır. EGM, bu yarışmanın dengelendiği optimum noktayı bulma sanatıdır.

---

## 1. Eşanjörde Entropi Üretimi Ayrıştırması (S_gen Decomposition)

### 1.1 Toplam Entropi Üretimi

Bir eşanjörde toplam tersinmezlik, iki bağımsız fiziksel mekanizmanın toplamıdır. Bunları anlamak, optimizasyon stratejisinin temelini oluşturur.

Fiziksel sezgi: Sıcak akışkandan soğuk akışkana ısı aktarılırken, sonlu bir sıcaklık farkı gerekir — bu fark ne kadar büyükse ısı o kadar kolay akar ama termodinamik kalite kaybı da o kadar büyük olur. Aynı zamanda akışkanlar borulardan ve kanal yüzeylerinden geçerken sürtünme nedeniyle basınç kaybeder — bu da mekanik enerjinin ısıya dönüşerek geri kazanılamaz hale gelmesidir.

```
Toplam entropi üretimi:
Ṡ_gen = Ṡ_gen,ΔT + Ṡ_gen,ΔP  [kW/K]

Burada:
- Ṡ_gen,ΔT = sonlu sıcaklık farkından kaynaklanan entropi üretimi (heat transfer irreversibility)
- Ṡ_gen,ΔP = basınç düşüşünden kaynaklanan entropi üretimi (fluid friction irreversibility)

Exergy yıkımı ile doğrudan bağlantı:
Ėx_yıkım = T₀ × Ṡ_gen  [kW]

Burada:
- T₀ = ölü durum (referans) sıcaklığı [K] (genellikle 298.15 K)
```

Bu iki bileşenin davranışı zıt yönlüdür ve bir U-eğrisi (U-curve) optimumu yaratır:

```
Eşanjör alanı (A) artırıldığında:
├── Ṡ_gen,ΔT AZALIR: Daha fazla alan → daha küçük sıcaklık farkı → daha az ısı transferi tersinmezliği
├── Ṡ_gen,ΔP ARTAR:  Daha fazla alan → daha fazla boru/kanal → daha fazla sürtünme yüzeyi
└── Ṡ_gen,toplam:    Bir minimum noktası (optimum) oluşur

         Ṡ_gen
          |
          |  \                    /
          |   \   Ṡ_gen,ΔP      /
          |    \    ↗           /
          |     \    --------  /
          |      \  /        \/
          |       \/          \
          |       /\   Ṡ_gen,toplam (U-eğrisi)
          |      /  \------
          |     /          -------
          |    / Ṡ_gen,ΔT    ↘
          |   /
          |__/_________________________________ A (alan)
                    ↑
              Optimum nokta
              (Ṡ_gen minimum)
```

### 1.2 Sıcaklık Farkı Bileşeni (S_gen,ΔT — Heat Transfer Irreversibility)

Fiziksel sezgi: İki farklı sıcaklıktaki cisim arasında ısı aktarımı doğal (spontan) bir süreçtir — ısı her zaman sıcaktan soğuğa akar. Ancak bu süreç tersinmezdir çünkü ısının sıcaklık farkı olmadan aktarılması sonsuz alan gerektirir (Carnot limiti). Sıcaklık farkı büyüdükçe ısı akışı kolaylaşır ama termodinamik "kalite" kaybı da büyür.

Basitleştirilmiş yaklaşım (sabit ısı kapasitesi ve ortalama sıcaklıklar için):

```
Ṡ_gen,ΔT = Q̇ × (1/T_cold,avg - 1/T_hot,avg)  [kW/K]

Burada:
- Q̇ = eşanjördeki ısı transfer hızı [kW]
- T_cold,avg = soğuk akışkan ortalama sıcaklığı [K]
- T_hot,avg = sıcak akışkan ortalama sıcaklığı [K]

Bu formülün fiziksel anlamı:
Soğuk tarafın entropi kazancı (Q̇/T_cold,avg) her zaman sıcak tarafın
entropi kaybından (Q̇/T_hot,avg) büyüktür. Aradaki fark = üretilen entropi.
```

Daha doğru hesaplama — eşanjör boyunca integrasyon (counter-flow için):

```
Ṡ_gen,ΔT = ṁ_hot × cp_hot × ln(T_hot,out / T_hot,in) + ṁ_cold × cp_cold × ln(T_cold,out / T_cold,in)

Burada:
- ṁ_hot, ṁ_cold = sıcak ve soğuk akışkan kütle debileri [kg/s]
- cp_hot, cp_cold = ortalama özgül ısı kapasiteleri [kJ/(kg·K)]
- T değerleri mutlak sıcaklık [K] olmalıdır

Not: Logaritmik terimler negatif ve pozitif olacaktır.
Sıcak taraf: ln(T_out/T_in) < 0 (soğuyor)
Soğuk taraf: ln(T_out/T_in) > 0 (ısınıyor)
Toplam her zaman pozitiftir (2. yasa gereği).
```

Ṡ_gen,ΔT'yi etkileyen faktörler:

| Parametre | Artarsa Ṡ_gen,ΔT | Açıklama |
|---|---|---|
| Approach temperature (ΔT_app) | Artar | Sıcaklık farkı büyür → daha fazla tersinmezlik |
| Eşanjör alanı (A) | Azalır | Daha fazla alan → daha küçük ortalama ΔT |
| Isı transfer katsayısı (U) | Azalır | Daha iyi ısı transferi → daha küçük ΔT gerekli |
| Etkinlik (effectiveness, ε) | Azalır | Yüksek etkinlik → sıcaklıklar yakınlaşır |
| Akış düzeni (counter vs parallel) | Counter-flow'da düşük | Counter-flow'da daha homojen ΔT profili |

### 1.3 Basınç Düşüşü Bileşeni (S_gen,ΔP — Fluid Friction Irreversibility)

Fiziksel sezgi: Akışkan bir borudan veya kanaldan geçerken duvar sürtünmesi ve türbülans nedeniyle basınç kaybeder. Bu basınç kaybı, akışkanın mekanik enerjisinin ısıya dönüşmesidir — yani düzenli hareket enerjisinin düzensiz moleküler harekete dönüşmesi. Bu dönüşüm tamamen tersinmezdir.

```
Sıcak taraf basınç düşüşü entropi üretimi:
Ṡ_gen,ΔP_hot = ṁ_hot × ΔP_hot / (ρ_hot × T_hot,avg)  [kW/K]

Soğuk taraf basınç düşüşü entropi üretimi:
Ṡ_gen,ΔP_cold = ṁ_cold × ΔP_cold / (ρ_cold × T_cold,avg)  [kW/K]

Toplam basınç düşüşü entropi üretimi:
Ṡ_gen,ΔP = Ṡ_gen,ΔP_hot + Ṡ_gen,ΔP_cold  [kW/K]

Burada:
- ṁ = kütle debisi [kg/s]
- ΔP = basınç düşüşü [kPa]
- ρ = akışkan yoğunluğu [kg/m³]
- T_avg = akışkan ortalama mutlak sıcaklığı [K]

Dikkat: İdeal gaz için alternatif formül:
Ṡ_gen,ΔP = ṁ × R × ln(P_in / P_out) / M

Burada R = evrensel gaz sabiti [8.314 kJ/(kmol·K)], M = mol kütlesi [kg/kmol]
```

Ṡ_gen,ΔP'yi etkileyen faktörler:

| Parametre | Artarsa Ṡ_gen,ΔP | Açıklama |
|---|---|---|
| Akış hızı (v) | Artar (~ v²) | Sürtünme kuvveti hızın karesiyle orantılı |
| Boru uzunluğu (L) | Artar | Daha fazla sürtünme yüzeyi |
| Boru çapı (D) | Azalır | Büyük çap → düşük hız → az sürtünme |
| Yüzey pürüzlülüğü (ε/D) | Artar | Pürüzlü yüzey → daha fazla sürtünme |
| Baffle sayısı (N_b) | Artar | Her baffle geçişi ek basınç kaybı |
| Akışkan viskozitesi (μ) | Artar | Yüksek viskozite → daha fazla sürtünme |
| Reynolds sayısı (Re) | Karmaşık | Laminer → türbülansa geçişte sıçrama var |

---

## 2. Counter-flow vs Parallel-flow Entropi Karşılaştırması

### 2.1 Counter-flow (Karşı Akış)

Fiziksel sezgi: Karşı akışta sıcak ve soğuk akışkanlar zıt yönlerde akar. Bu düzenleme, eşanjör boyunca sıcaklık farkının (driving force) daha homojen dağılmasını sağlar. Homojen bir ΔT, toplam entropi üretimini minimize eder — çünkü entropi üretimi ΔT'nin karesi ile orantılıdır (küçük ama eşit ΔT'ler, büyük ve değişken ΔT'lerden her zaman iyidir).

```
Counter-flow sıcaklık profili (eşanjör boyunca):

Sıcaklık [°C]
    |
180 | ─────────___                    T_hot,in
    |              ───___
140 |                    ───___       T_hot,out
    |
120 |                    ───___       T_cold,out
    |              ───___
 80 | ─────────___                    T_cold,in
    |
    └──────────────────────────── Konum (L)
    Giriş                    Çıkış
    (sıcak taraf)           (sıcak taraf)

ΔT profili: Oldukça düzgün (homojen)
ΔT_giriş ≈ ΔT_çıkış ≈ ΔT_orta (ideal durumda)
```

Counter-flow avantajları:
- Daha düşük Ṡ_gen,ΔT: Homojen ΔT profili sayesinde
- Daha yüksek etkinlik (ε): Aynı NTU için ε_counter > ε_parallel
- Daha yakın approach temperature: T_cold,out, T_hot,in değerine yaklaşabilir
- Sıcaklık çaprazlaması (temperature cross) mümkün: T_cold,out > T_hot,out olabilir

### 2.2 Parallel-flow (Paralel Akış)

Fiziksel sezgi: Paralel akışta her iki akışkan aynı yönde akar. Girişte sıcaklık farkı çok büyükken çıkışta küçülür. Bu homojen olmayan ΔT dağılımı daha fazla entropi üretir. Ayrıca T_cold,out hiçbir zaman T_hot,out değerini aşamaz — bu da paralel akışın temel sınırlamasıdır.

```
Parallel-flow sıcaklık profili:

Sıcaklık [°C]
    |
180 | *                               T_hot,in
    |  \
    |    \___
140 |        ───___                   T_hot,out  ←  Çıkış sıcaklıkları
    |              ───────────────    (yakınlaşır ama asla eşitlenmez)
120 |              ───────────────    T_cold,out ←
    |        ___───
    |    /───
 80 |  /                              T_cold,in
    | *
    └──────────────────────────── Konum (L)
    Giriş                    Çıkış

ΔT profili: Girişte çok büyük, çıkışta küçük (homojen DEĞİL)
ΔT_giriş >> ΔT_çıkış (büyük asimetri → yüksek entropi üretimi)
```

Parallel-flow dezavantajları:
- Daha yüksek Ṡ_gen,ΔT: Girişte büyük ΔT → orantısız entropi üretimi
- Daha düşük etkinlik: Aynı NTU için daha az ısı transferi
- Sınırlı çıkış sıcaklığı: T_cold,out < T_hot,out (sıcaklık çaprazlaması imkansız)
- Daha büyük LMTD: Aynı Q̇ için daha küçük alan gerektirir gibi görünür ama exergy kaybı yüksektir

### 2.3 Sayısal Karşılaştırma

Aynı görev (duty), aynı UA değeri ve aynı giriş koşulları için iki düzenlemenin karşılaştırması:

```
Örnek koşullar:
- Sıcak akışkan: Su, ṁ_hot = 2.0 kg/s, T_hot,in = 180°C, cp = 4.2 kJ/(kg·K)
- Soğuk akışkan: Su, ṁ_cold = 3.0 kg/s, T_cold,in = 30°C, cp = 4.2 kJ/(kg·K)
- Q̇ = 300 kW (hedef ısı transferi)
- UA = 15 kW/K
```

| Parametre | Counter-flow | Parallel-flow | Fark |
|---|---|---|---|
| T_hot,out [°C] | 144.3 | 144.3 | Aynı (aynı Q̇) |
| T_cold,out [°C] | 53.8 | 53.8 | Aynı (aynı Q̇) |
| LMTD [°C] | 117.2 | 123.8 | Counter %5.3 düşük |
| ε (effectiveness) | 0.238 | 0.238 | Aynı (aynı Q̇/Q̇_max) |
| Ṡ_gen,ΔT [kW/K] | 0.0612 | 0.0697 | Counter %12.2 düşük |
| Ṡ_gen,ΔP [kW/K] | ~aynı | ~aynı | Geometriye bağlı |
| Ėx_yıkım [kW] | 18.2 | 20.8 | Counter 2.6 kW daha az |

```
Daha yüksek etkinlik değerlerinde (ε > 0.7) fark dramatik şekilde artar:

| Etkinlik (ε) | Ṡ_gen,ΔT Counter [kW/K] | Ṡ_gen,ΔT Parallel [kW/K] | Counter Avantajı [%] |
|---|---|---|---|
| 0.3 | 0.068 | 0.075 | 10 |
| 0.5 | 0.055 | 0.068 | 19 |
| 0.7 | 0.038 | 0.055 | 31 |
| 0.85 | 0.022 | 0.041 | 46 |
| 0.95 | 0.008 | 0.030 | 73 |

Not: Etkinlik arttıkça counter-flow'un entropi avantajı katlanarak büyür.
ε > 0.85 durumlarında counter-flow ZORUNLUDUR.
```

---

## 3. NTU-Entropi İlişkisi (NTU-Entropy Relationship)

### 3.1 NTU Tanımı ve EGM Bağlantısı

Fiziksel sezgi: NTU (Number of Transfer Units — Transfer Birimi Sayısı), bir eşanjörün "ısı transferi kapasitesinin" boyutsuz ölçüsüdür. Yüksek NTU, büyük eşanjör anlamına gelir — daha fazla alan, daha iyi ısı transferi, ama aynı zamanda daha fazla sürtünme. NTU, etkinlik ile doğrudan bağlantılıdır ve optimum bir NTU değeri entropi üretimini minimize eder.

```
NTU tanımı:
NTU = UA / C_min  [boyutsuz]

Burada:
- U = toplam ısı transfer katsayısı [kW/(m²·K)]
- A = eşanjör ısı transfer alanı [m²]
- C_min = (ṁ × cp)_min = minimum ısı kapasitesi akış hızı [kW/K]

Kapasite oranı:
C_r = C_min / C_max  [0 ≤ C_r ≤ 1]

Etkinlik-NTU ilişkisi (counter-flow):
ε = [1 - exp(-NTU × (1 - C_r))] / [1 - C_r × exp(-NTU × (1 - C_r))]

Özel durum (C_r = 1, dengeli akış):
ε = NTU / (1 + NTU)
```

NTU ile entropi üretiminin ilişkisi — temel davranış:

```
Düşük NTU (NTU < 1):
├── Küçük eşanjör → büyük sıcaklık farkı → yüksek Ṡ_gen,ΔT
├── Az sürtünme yüzeyi → düşük Ṡ_gen,ΔP
└── Ṡ_gen,ΔT baskın → toplam entropi üretimi yüksek

Orta NTU (optimum bölge):
├── Orta boy eşanjör → makul sıcaklık farkı → orta Ṡ_gen,ΔT
├── Orta sürtünme → orta Ṡ_gen,ΔP
└── İki bileşen dengelenmiş → Ṡ_gen,toplam MİNİMUM

Yüksek NTU (NTU > 5):
├── Büyük eşanjör → küçük sıcaklık farkı → düşük Ṡ_gen,ΔT
├── Çok fazla sürtünme yüzeyi → yüksek Ṡ_gen,ΔP
└── Ṡ_gen,ΔP baskın → toplam entropi üretimi tekrar artar

Bu davranış her eşanjör tipi için U-eğrisi yaratır.
```

### 3.2 Etkinlik-Entropi Grafiği

Fiziksel sezgi: NTU arttıkça etkinlik de artar ama azalan getiri yasası devreye girer — NTU'yu iki katına çıkarmak etkinliği iki katına çıkarmaz. Buna karşılık basınç düşüşü (ve dolayısıyla Ṡ_gen,ΔP) yaklaşık doğrusal artar. Bu asimetri, optimum noktanın varlığını garanti eder.

```
Ṡ_gen vs NTU grafiği (counter-flow, C_r = 0.5):

  Ṡ_gen [kW/K]
    |
0.12|*
    | \
0.10|  \   Ṡ_gen,ΔT (azalan)
    |   \
0.08|    \                                    *  Ṡ_gen,ΔP (artan)
    |     \                                /
0.06|      \                            /
    |       \                        /
0.04|        \___               ___/
    |            \___       ___/
0.02|                \_____/        ← Ṡ_gen,toplam (U-eğrisi, minimum)
    |                  ↑
0.00|__________________|_________________________ NTU
    0     1     2     3     4     5     6     7

                NTU_opt ≈ 2.5 (bu örnekte)

Not: NTU_opt değeri akışkan türüne, geometriye ve işletme koşullarına bağlıdır.
```

Boyutsuz entropi üretimi sayısı (N_S — Bejan tarafından tanımlanmıştır):

```
N_S = Ṡ_gen / C_min  [boyutsuz]

Bu boyutsuz sayı farklı eşanjörlerin karşılaştırılmasını kolaylaştırır.

N_S'nin NTU ile değişimi (counter-flow):
N_S = N_S,ΔT + N_S,ΔP

N_S,ΔT = (1/ε) × ln[(1 + ε×(τ-1)) / τ] + (C_r/ε) × ln[(1 + C_r×ε×(τ-1)/τ)]
  (burada τ = T_hot,in / T_cold,in)

N_S,ΔP ∝ NTU × f × Re^a  (geometriye bağlı orantı)
```

---

## 4. Optimum Approach Temperature Belirleme

### 4.1 Approach Temperature Tanımı

Fiziksel sezgi: Approach temperature, bir eşanjörde sıcak ve soğuk akışkanlar arasındaki en küçük sıcaklık farkıdır. Bu fark sıfıra ne kadar yaklaşırsa ısı transferi o kadar "termodinamik olarak mükemmel" olur — ama sonsuz alan gerektirir. Pratikte sonlu bir approach temperature zorunludur ve optimum değer, termodinamik kayıp ile yatırım maliyeti arasındaki dengeye bağlıdır.

```
Farklı eşanjör tipleri için approach temperature tanımları:

Counter-flow eşanjör:
  ΔT_approach = min(T_hot,out - T_cold,in , T_hot,in - T_cold,out)

Parallel-flow eşanjör:
  ΔT_approach = T_hot,out - T_cold,out  (çıkıştaki fark)

Kondenser / evaporatör (faz değişimi olan):
  ΔT_approach = T_sat - T_fluid,out  (doyma ile çıkış arasındaki fark)

LMTD (Logarithmic Mean Temperature Difference):
  LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁ / ΔT₂)  [K veya °C]

  Burada ΔT₁ ve ΔT₂ eşanjörün iki ucundaki sıcaklık farkları.
  Eğer ΔT₁ = ΔT₂ ise: LMTD = ΔT₁ = ΔT₂

Isı transfer denklemi:
  Q̇ = U × A × LMTD  [kW]
  → A = Q̇ / (U × LMTD) [m²]

Approach temperature küçüldükçe:
  LMTD ↓ → Gerekli A ↑ → Yatırım maliyeti ↑ → Ṡ_gen,ΔT ↓
```

### 4.2 Optimum Approach — Termodinamik vs Ekonomik

Fiziksel sezgi: Saf termodinamik açıdan approach temperature sıfıra yaklaştırılmalıdır (minimum entropi üretimi). Ancak bu sonsuz alan ve sonsuz maliyet gerektirir. Ekonomik optimum, yıllık exergy yıkım maliyeti ile yatırım amortisman maliyetinin toplamını minimize eden noktadır.

```
Saf EGM optimumu (sadece termodinamik):
  min Ṡ_gen,ΔT → ΔT_approach → 0  (sonsuz alan, pratik değil)

Ekonomik optimum:
  min [C_yatırım_yıllık + C_exergy_yıkım]

  C_yatırım_yıllık = (CRF) × C_eşanjör(A)  [€/yıl]
  C_exergy_yıkım = T₀ × Ṡ_gen × c_ex × t_çalışma  [€/yıl]

  Burada:
  - CRF = sermaye geri kazanım faktörü (Capital Recovery Factor) [1/yıl]
  - C_eşanjör(A) = eşanjör yatırım maliyeti, alan fonksiyonu [€]
  - c_ex = exergy birim maliyeti [€/kWh]
  - t_çalışma = yıllık çalışma süresi [saat]

Toplam yıllık maliyet:
  C_toplam(ΔT_app) = C_yatırım(ΔT_app) + C_exergy_yıkım(ΔT_app)

  dC_toplam / d(ΔT_app) = 0  → Optimum ΔT_approach
```

Uygulama bazında optimum approach temperature değerleri:

| Uygulama | Tipik Approach [°C] | Optimum EGM Aralığı [°C] | Açıklama |
|---|---|---|---|
| Process-process HX | 5–15 | 3–8 | Yüksek çalışma saati, yüksek kazanım |
| Economizer (baca gazı) | 15–30 | 10–20 | Asit çiğ noktası sınırlaması |
| Kondenser (buhar) | 3–7 | 2–5 | Faz değişimi, yüksek U değeri |
| Evaporatör (soğutma) | 3–7 | 2–5 | COP doğrudan etkilenir |
| Cooling tower | 3–8 | 3–5 | Yaş termometre sınırlaması |
| Atık ısı kazanı (WHR) | 20–50 | 15–30 | Fouling ve korozyon kısıtları |
| Plakalı eşanjör (PHE) | 2–5 | 1–3 | Yüksek U, kompakt tasarım |
| Hava soğutmalı HX | 10–25 | 8–15 | Düşük hava tarafı U değeri |

```
Pratik karar ağacı:
Eğer approach temperature > tablo üst sınırı → EGM ile iyileştirme potansiyeli VAR
Eğer approach temperature ≈ EGM aralığı → yakın-optimum çalışma
Eğer approach temperature < EGM alt sınırı → aşırı yatırım, ekonomik değil

Örnek: Process-process eşanjör, mevcut ΔT_app = 25°C
  → Optimum aralık 3-8°C → büyük iyileştirme potansiyeli
  → Eşanjör alanı artırımı veya değişimi değerlendirilmeli
```

---

## 5. Geometrik Optimizasyon

### 5.1 Baffle Aralığı Optimizasyonu (Shell-and-Tube — Gövde-Boru Eşanjörler)

Fiziksel sezgi: Bafflelar (saptırma plakaları), gövde tarafındaki akışkanı boru demetinin üzerinden geçmeye zorlayarak çapraz akış oluşturur. Bu, ısı transfer katsayısını artırır ama aynı zamanda basınç kaybını da artırır. Baffle aralığı azaldıkça akışkan daha fazla kez yön değiştirir — daha iyi ısı transferi ama daha fazla sürtünme.

```
Baffle aralığı (B) ile entropi üretimi ilişkisi:

Gövde tarafı ısı transfer katsayısı (yaklaşık):
h_shell ∝ 1 / B^0.4  (baffle aralığı azalınca h artar)

Gövde tarafı basınç düşüşü (yaklaşık):
ΔP_shell ∝ 1 / B^3  (baffle aralığı azalınca ΔP dramatik artar!)

Entropi bileşenleri:
Ṡ_gen,ΔT ∝ B^0.4   (B azalınca Ṡ_gen,ΔT azalır)
Ṡ_gen,ΔP ∝ 1/B^3    (B azalınca Ṡ_gen,ΔP hızla artar)

→ Optimum baffle aralığı: dṠ_gen,toplam / dB = 0
```

Optimum baffle aralığı pratik kuralları:

```
TEMA standartları önerileri:
- Minimum baffle aralığı: B_min = max(D_shell/5, 50 mm)
- Maksimum baffle aralığı: B_max = D_shell (gövde çapı)
- Optimum baffle aralığı (EGM): B_opt ≈ 0.3 × D_shell ile 0.5 × D_shell arası

| Gövde Çapı D_shell [mm] | B_min [mm] | B_opt (EGM) [mm] | B_max [mm] |
|---|---|---|---|
| 250 | 50 | 75–125 | 250 |
| 500 | 100 | 150–250 | 500 |
| 750 | 150 | 225–375 | 750 |
| 1000 | 200 | 300–500 | 1000 |
| 1500 | 300 | 450–750 | 1500 |

Helical baffle (helisel saptırma plakaları):
- Geleneksel segmental baffleye göre %20-35 daha az ΔP (aynı h için)
- EGM açısından üstün: Ṡ_gen,ΔP önemli ölçüde düşer
- Yatırım maliyeti %10-20 daha yüksek ama exergy tasarrufu ile karşılanır
```

### 5.2 Boru Sayısı ve Çapı

Fiziksel sezgi: Boru demeti tasarımı doğrudan her iki entropi bileşenini etkiler. Daha fazla sayıda ince boru toplam ısı transfer alanını artırır (daha düşük Ṡ_gen,ΔT) ancak her borunun çapı küçüldükçe akış hızı yükselir ve sürtünme artar (daha yüksek Ṡ_gen,ΔP). Ayrıca ince borularda fouling (kirlenme) riski yükselir ve temizlik zorlaşır.

```
Boru tarafı basınç düşüşü:
ΔP_tube = f × (L/D_i) × (ρ × v²/2) × N_pass  [Pa]

Burada:
- f = sürtünme faktörü (Fanning veya Darcy-Weisbach)
- L = boru uzunluğu [m]
- D_i = boru iç çapı [m]
- v = akış hızı [m/s]
- N_pass = boru geçiş sayısı

Boru tarafı ısı transfer katsayısı (türbülans, Dittus-Boelter):
h_tube = 0.023 × (k/D_i) × Re^0.8 × Pr^0.4

Dikkat: h ∝ v^0.8 ama ΔP ∝ v^2
→ Basınç düşüşü ısı transfer katsayısından daha hızlı artar!
→ Aşırı hız artışı EGM açısından her zaman zararlıdır.
```

Optimum boru çapı seçimi:

| Boru Dış Çapı [mm] | Duvar [mm] | İç Çap [mm] | Tipik Uygulama | EGM Notu |
|---|---|---|---|---|
| 15.88 (5/8") | 1.24 | 13.40 | Temiz akışkanlar, soğutma suyu | Yüksek U, yüksek ΔP |
| 19.05 (3/4") | 1.65 | 15.75 | Genel endüstriyel, en yaygın | Dengeli U/ΔP |
| 25.40 (1") | 1.65 | 22.10 | Kirli akışkanlar, viskoz sıvılar | Düşük ΔP, düşük U |
| 31.75 (1-1/4") | 2.11 | 27.53 | Ağır fouling, korozif akışkan | En düşük ΔP |
| 50.80 (2") | 2.77 | 45.26 | Özel uygulamalar, çok kirli | Temizlik kolaylığı |

### 5.3 Akış Hızı Optimizasyonu

Fiziksel sezgi: Akış hızı hem ısı transfer katsayısını hem basınç düşüşünü belirler. Düşük hız durumunda ısı transferi kötüdür (büyük ΔT gerekir, yüksek Ṡ_gen,ΔT). Yüksek hız durumunda sürtünme baskındır (yüksek Ṡ_gen,ΔP). Optimum hız, iki mekanizmanın dengelendiği noktadadır.

```
Optimum hız belirleme kriteri (EGM):
d(Ṡ_gen,toplam) / d(v) = 0

Basitleştirilmiş analitik çözüm (türbülans, pürüzsüz boru):
v_opt ∝ (Pr × k × ΔT / (f × T_avg × D))^(1/3)

Pratik sonuç: Optimum hız, akışkan özelliklerine ve sıcaklık farkına bağlıdır.
```

Farklı akışkanlar için önerilen hız aralıkları:

| Akışkan | Konum | Ekonomik Hız [m/s] | EGM Optimum Hız [m/s] | Maksimum Hız [m/s] |
|---|---|---|---|---|
| Su (temiz) | Boru tarafı | 1.0–2.5 | 1.2–2.0 | 3.0 |
| Su (soğutma) | Boru tarafı | 1.5–2.5 | 1.5–2.2 | 3.0 |
| Su | Gövde tarafı | 0.5–1.5 | 0.6–1.2 | 2.0 |
| Buhar (yoğuşan) | Gövde tarafı | 10–30 | 15–25 | 50 |
| Hava (basınçlı) | Boru tarafı | 10–25 | 12–20 | 30 |
| Yağ (ısıl) | Boru tarafı | 0.5–1.5 | 0.8–1.2 | 2.0 |
| Organik sıvılar | Boru tarafı | 0.8–2.0 | 1.0–1.5 | 2.5 |
| Baca gazı | Gövde tarafı | 8–20 | 10–15 | 25 |

```
Dikkat: EGM optimum hızı genellikle ekonomik hız aralığının
alt-orta bölgesindedir. Çünkü ekonomik hız yalnızca pompalama
maliyetini düşünürken, EGM exergy yıkımını da hesaba katar.
```

---

## 6. Fouling ve EGM (Kirlenme Etkisi)

Fiziksel sezgi: Fouling (kirlenme), eşanjör yüzeylerinde zaman içinde oluşan birikintilerdir. Bu birikinti hem ek bir termal direnç katmanı oluşturur (LMTD'yi artırmak gerekir → daha büyük ΔT → daha fazla Ṡ_gen,ΔT) hem de akış kesitini daraltır (hız artar → daha fazla ΔP → daha fazla Ṡ_gen,ΔP). Fouling bir "çifte ceza" mekanizmasıdır — her iki entropi bileşenini de artırır.

```
Fouling'in toplam ısı transfer katsayısına etkisi:
1/U_kirli = 1/U_temiz + R_f,hot + R_f,cold

Burada:
- U_temiz = temiz eşanjör toplam ısı transfer katsayısı [kW/(m²·K)]
- U_kirli = kirli eşanjör toplam ısı transfer katsayısı [kW/(m²·K)]
- R_f,hot = sıcak taraf fouling direnci [m²·K/kW]
- R_f,cold = soğuk taraf fouling direnci [m²·K/kW]

Fouling nedeniyle ek entropi üretimi:
ΔṠ_gen,ΔT = Q̇ × R_f × (Q̇/A) / (T_hot,avg × T_cold,avg)  (yaklaşık)

Fouling nedeniyle ek basınç düşüşü:
ΔP_fouling / ΔP_temiz ≈ (D_i / (D_i - 2×δ_f))^5

Burada δ_f = fouling katmanı kalınlığı [m]
→ 1 mm fouling, küçük borularda ΔP'yi %30-50 artırabilir!
```

Fouling'in entropi üretimi üzerindeki etkisi — sayısal örnek:

| Fouling Durumu | R_f [m²·K/kW] | U [kW/(m²·K)] | ΔT_app [°C] | Ṡ_gen,ΔT [kW/K] | Ṡ_gen,ΔP [kW/K] | Ṡ_gen,toplam [kW/K] |
|---|---|---|---|---|---|---|
| Temiz (yeni) | 0 | 2.50 | 5.0 | 0.032 | 0.008 | 0.040 |
| Hafif kirli | 0.10 | 2.17 | 7.5 | 0.041 | 0.010 | 0.051 (+28%) |
| Orta kirli | 0.25 | 1.82 | 11.2 | 0.054 | 0.013 | 0.067 (+68%) |
| Ağır kirli | 0.50 | 1.43 | 17.8 | 0.078 | 0.018 | 0.096 (+140%) |

```
Fouling önleme ve temizlik stratejisi (EGM perspektifi):

1. Düzenli temizlik programı:
   - CIP (Clean-In-Place) her 3-6 ayda → Ṡ_gen,ΔT %20-40 azalır
   - Mekanik temizlik yılda 1 kez → fouling katmanı sıfırlanır

2. Tasarım önlemleri:
   - Minimum akış hızı korunsun (v > 0.8 m/s su için) → fouling azalır
   - Uygun malzeme seçimi (paslanmaz çelik, titanyum)
   - Döner (self-cleaning) boru ekleri

3. İzleme:
   - ΔP artışı izlenmeli → %20 artış = temizlik zamanı
   - U değeri düşüşü izlenmeli → %15 düşüş = temizlik zamanı
   - Online fouling monitor ile gerçek zamanlı Ṡ_gen takibi

4. Ekonomik analiz:
   - Temizlik maliyeti << fouling kaynaklı exergy yıkım maliyeti
   - Tipik olarak: 1 € temizlik yatırımı = 5-15 € exergy tasarrufu
```

---

## 7. Eşanjör Tipi Karşılaştırması — EGM Perspektifi

Fiziksel sezgi: Farklı eşanjör geometrileri farklı Ṡ_gen,ΔT / Ṡ_gen,ΔP dengeleri sunar. Kompakt eşanjörler (plakalı, spiral) birim hacim başına daha fazla alan sağlar ve genellikle daha düşük entropi üretir, ancak basınç ve sıcaklık sınırlamaları vardır.

| Eşanjör Tipi | Ṡ_gen,ΔT (göreceli) | Ṡ_gen,ΔP (göreceli) | Ṡ_gen,toplam (göreceli) | Tipik ε Aralığı |
|---|---|---|---|---|
| Shell-and-tube (S&T) | 1.00 (referans) | 1.00 (referans) | 1.00 (referans) | 0.3–0.85 |
| Plakalı (PHE) | 0.65 | 1.20 | 0.70 | 0.5–0.95 |
| Spiral eşanjör | 0.70 | 0.90 | 0.72 | 0.5–0.90 |
| Double-pipe (çift borulu) | 0.95 | 0.85 | 0.92 | 0.3–0.80 |
| Finned tube (kanatlı boru) | 0.85 | 1.30 | 0.90 | 0.4–0.85 |
| Plate-fin (plakalı kanatlı) | 0.55 | 1.10 | 0.60 | 0.6–0.95 |

```
EGM perspektifinden eşanjör tipi seçim rehberi:

Plakalı eşanjör (PHE) tercih edilecek durumlar:
  ✓ Approach temperature < 5°C gerektiğinde (düşük Ṡ_gen,ΔT)
  ✓ Sıcaklık < 200°C ve basınç < 25 bar olduğunda
  ✓ Temizlik kolaylığı gerektiğinde (fouling azaltma → düşük Ṡ_gen)
  ✓ Alan sınırlı olduğunda (kompakt tasarım)
  → Tipik olarak S&T'ye göre %20-40 daha az toplam Ṡ_gen

Shell-and-tube tercih edilecek durumlar:
  ✓ Yüksek sıcaklık (>200°C) veya yüksek basınç (>25 bar)
  ✓ Faz değişimi olan uygulamalar (kondenser, reboiler)
  ✓ Çok kirli akışkanlar (mekanik temizlik gerekli)
  ✓ Büyük kapasite (>1 MW)
```

---

## 8. Pratik Mühendislik Kuralları (Rules of Thumb)

Yıllarca endüstriyel deneyimden elde edilen ve EGM teorisi ile tutarlı pratik kurallar:

```
KURAL 1 — Akış Düzeni:
Counter-flow her zaman EGM açısından tercih edilmelidir.
Counter-flow, parallel-flow'a göre %15-30 daha az Ṡ_gen üretir (aynı görev için).
Çapraz akış (cross-flow) ikisinin arasındadır.
→ İstisna: Çok düşük etkinlik gereken durumlarda (ε < 0.3) fark önemsizdir.

KURAL 2 — Baffle Aralığı:
Shell-and-tube eşanjörlerde optimum baffle aralığı ≈ 0.3–0.5 × gövde çapı.
Bu aralığın altına inmek Ṡ_gen,ΔP'yi patlama noktasına getirir (ΔP ∝ 1/B³).
Bu aralığın üstüne çıkmak Ṡ_gen,ΔT'yi kabul edilemez seviyelere taşır.

KURAL 3 — Plakalı Eşanjör Avantajı:
Plakalı eşanjörler, aynı görev için shell-and-tube'a göre
tipik olarak %20-40 daha az toplam Ṡ_gen üretir.
Sebebi: Daha yüksek U değeri + gerçek counter-flow + kompakt yapı.

KURAL 4 — Temizlik:
Eşanjörlerinizi temiz tutun! Fouling, Ṡ_gen'i %30-50 artırabilir.
Düzenli temizlik (CIP veya mekanik) en etkili EGM stratejisidir.
Temizlik yatırımının geri dönüşü tipik olarak 3-6 aydır.

KURAL 5 — Optimum NTU:
Çoğu endüstriyel uygulama için optimum NTU = 2-4 aralığındadır.
NTU < 1: Eşanjör yetersiz, büyütülmeli.
NTU > 6: Aşırı boyutlandırma, pompalama maliyeti yüksek, küçültme değerlendirilmeli.

KURAL 6 — Approach Temperature:
Process-process eşanjörlerde optimum approach temperature 3-8°C.
Ekonomizerlerde 10-20°C (asit çiğ noktası dikkat!).
Kondenser/evaporatörde 2-5°C (COP doğrudan etkilenir).
Mevcut approach > optimumun 2 katı ise → retrofit değerlendir.

KURAL 7 — Akış Hızı:
Boru tarafı su hızı: 1.2-2.0 m/s (EGM optimum bölge).
0.8 m/s altı → fouling riski artar + zayıf ısı transferi.
2.5 m/s üstü → erozyon riski + aşırı ΔP.

KURAL 8 — Ṡ_gen Bileşen Oranı:
İyi tasarlanmış bir eşanjörde: Ṡ_gen,ΔP / Ṡ_gen,toplam ≈ %15-30.
Eğer bu oran %50'yi aşıyorsa → basınç düşüşü sorunu, geometri optimize edilmeli.
Eğer bu oran %5'in altındaysa → eşanjör aşırı büyük, küçültme değerlendirilmeli.
```

---

## 9. Hesaplama Örneği: Shell-and-Tube Eşanjör EGM Optimizasyonu

### 9.1 Problem Tanımı

```
Bir kimya fabrikasında proses soğutma suyu ile kazan besleme suyunun
ısıtılması için bir shell-and-tube eşanjör tasarlanacaktır.

Sıcak akışkan (gövde tarafı): Proses soğutma suyu
  ṁ_hot = 5.0 kg/s
  T_hot,in = 85°C
  T_hot,out = 55°C (hedef)
  cp_hot = 4.18 kJ/(kg·K)
  ρ_hot = 980 kg/m³

Soğuk akışkan (boru tarafı): Kazan besleme suyu
  ṁ_cold = 4.0 kg/s
  T_cold,in = 25°C
  cp_cold = 4.18 kJ/(kg·K)
  ρ_cold = 998 kg/m³

Isı yükü: Q̇ = 5.0 × 4.18 × (85-55) = 627 kW
Soğuk çıkış: T_cold,out = 25 + 627/(4.0 × 4.18) = 62.5°C

Referans sıcaklık: T₀ = 25°C = 298.15 K
Çalışma süresi: 7,500 saat/yıl
Exergy birim maliyeti: c_ex = 0.04 €/kWh
```

### 9.2 EGM Ayrıştırma Hesabı

```
Adım 1: Ṡ_gen,ΔT hesabı (integral yöntemi)

Ṡ_gen,ΔT = ṁ_hot × cp_hot × ln(T_hot,out/T_hot,in)
          + ṁ_cold × cp_cold × ln(T_cold,out/T_cold,in)

T_hot,in  = 85 + 273.15 = 358.15 K
T_hot,out = 55 + 273.15 = 328.15 K
T_cold,in = 25 + 273.15 = 298.15 K
T_cold,out = 62.5 + 273.15 = 335.65 K

Ṡ_gen,ΔT = 5.0 × 4.18 × ln(328.15/358.15) + 4.0 × 4.18 × ln(335.65/298.15)
          = 20.90 × (-0.0876) + 16.72 × (0.1185)
          = -1.831 + 1.982
          = 0.151 kW/K

Adım 2: Ṡ_gen,ΔP hesabı (geometriye bağlı)

Tasarım A: Baffle aralığı = 200 mm (dar)
  ΔP_shell = 45 kPa, ΔP_tube = 25 kPa
  T_hot,avg = (85+55)/2 + 273.15 = 343.15 K
  T_cold,avg = (25+62.5)/2 + 273.15 = 316.90 K

  Ṡ_gen,ΔP = 5.0 × 45 / (980 × 343.15) + 4.0 × 25 / (998 × 316.90)
           = 225 / 336,287 + 100 / 316,267
           = 0.000669 + 0.000316
           = 0.000985 kW/K

Tasarım B: Baffle aralığı = 350 mm (optimum)
  ΔP_shell = 15 kPa, ΔP_tube = 25 kPa (aynı, boru tarafı değişmez)
  Ṡ_gen,ΔP = 5.0 × 15 / (980 × 343.15) + 4.0 × 25 / (998 × 316.90)
           = 0.000223 + 0.000316
           = 0.000539 kW/K

Adım 3: Toplam ve exergy yıkımı

Tasarım A: Ṡ_gen = 0.151 + 0.000985 = 0.1520 kW/K
  Ėx_yıkım = 298.15 × 0.1520 = 45.3 kW

Tasarım B: Ṡ_gen = 0.151 + 0.000539 = 0.1515 kW/K
  Ėx_yıkım = 298.15 × 0.1515 = 45.2 kW

Not: Bu örnekte Ṡ_gen,ΔT >> Ṡ_gen,ΔP (ısı transferi baskın).
Approach temperature azaltılarak daha büyük kazanım sağlanabilir.
```

### 9.3 Optimizasyon Alternatifleri

```
Alternatif 1: Approach temperature'ı azalt (daha büyük eşanjör)
  Mevcut approach: ΔT_app = 55 - 25 = 30°C (çok yüksek!)
  Hedef: ΔT_app = 10°C (T_hot,out = 35°C)
  Yeni Q̇ = 5.0 × 4.18 × (85-35) = 1,045 kW
  Yeni T_cold,out = 25 + 1045/(4.0 × 4.18) = 87.5°C (counter-flow gerekli!)

  Ṡ_gen,ΔT (yeni) = 5.0×4.18×ln(308.15/358.15) + 4.0×4.18×ln(360.65/298.15)
                   = 20.90×(-0.1509) + 16.72×(0.1897)
                   = -3.154 + 3.172
                   = 0.018 kW/K  → %88 azalma!

  Ek exergy kurtarımı = 298.15 × (0.151 - 0.018) = 39.7 kW
  Yıllık tasarruf = 39.7 × 7,500 × 0.04 = 11,910 €/yıl

Alternatif 2: Plakalı eşanjöre geçiş
  PHE ile ΔT_app = 3°C mümkün
  U_PHE ≈ 4.0 kW/(m²·K) vs U_S&T ≈ 1.5 kW/(m²·K)
  Daha küçük alan, daha düşük Ṡ_gen,ΔT
  Ancak ΔP daha yüksek olabilir → Ṡ_gen,ΔP artabilir
  Net sonuç: Tipik olarak %25-35 daha az toplam Ṡ_gen
```

---

## 10. Bejan Sayısı ve Tersinmezlik Dağılımı

Fiziksel sezgi: Bejan sayısı (Be), toplam entropi üretiminin ne kadarının ısı transferinden (sıcaklık farkı) kaynaklandığını gösteren boyutsuz bir göstergedir. Bu sayı, bir eşanjörün iyileştirme yönünü belirler — ısı transfer alanı mı artırılmalı, yoksa basınç düşüşü mü azaltılmalı?

```
Bejan sayısı tanımı:
Be = Ṡ_gen,ΔT / Ṡ_gen,toplam = Ṡ_gen,ΔT / (Ṡ_gen,ΔT + Ṡ_gen,ΔP)

Aralık: 0 ≤ Be ≤ 1

Be = 1: Tüm tersinmezlik ısı transferinden kaynaklanıyor (ΔP = 0 ideal durumu)
Be = 0: Tüm tersinmezlik sürtünmeden kaynaklanıyor (ΔT = 0 ideal durumu)
Be_opt ≈ 0.5: İki mekanizma dengede (bazı analizlerde optimum)

Pratik yorumlama:
| Be Değeri | Baskın Tersinmezlik | Optimizasyon Yönü |
|---|---|---|
| Be > 0.85 | Isı transferi baskın | Alan artır, approach düşür |
| 0.50 < Be < 0.85 | Isı transferi ağırlıklı | Önce alan, sonra geometri |
| 0.30 < Be < 0.50 | Dengeli | Optimum yakın, ince ayar |
| Be < 0.30 | Sürtünme baskın | Basınç kaybını azalt |
```

```
Tipik eşanjör tipleri için Be değerleri:

| Eşanjör Tipi | Tipik Be Aralığı | Yorum |
|---|---|---|
| Shell-and-tube (standart) | 0.70–0.95 | Genellikle ΔT baskın |
| Plakalı (PHE) | 0.50–0.80 | Daha dengeli |
| Kompakt (plate-fin) | 0.40–0.70 | ΔP etkisi belirgin |
| Air-cooled (hava soğutmalı) | 0.60–0.85 | Hava tarafı ΔP önemli |
| Ekonomizer (baca gazı) | 0.80–0.95 | Gaz tarafı ΔT baskın |

Çoğu endüstriyel eşanjörde Be > 0.7 → ısı transfer alanı artırımı
en etkili EGM stratejisidir.
```

---

## 11. Çok Akışlı Eşanjör Ağlarında EGM

Fiziksel sezgi: Gerçek fabrikalarda tek bir eşanjör yerine birbirine bağlı eşanjör ağları (Heat Exchanger Networks — HEN) vardır. EGM, ağ seviyesinde de uygulanabilir ve her bir eşanjörün katkısı ayrıştırılabilir. Pinch analizi ile birleştirildiğinde, EGM hem bireysel eşanjörlerin hem de tüm ağın optimize edilmesini sağlar.

```
Eşanjör ağı toplam entropi üretimi:
Ṡ_gen,ağ = Σᵢ Ṡ_gen,i = Σᵢ (Ṡ_gen,ΔT,i + Ṡ_gen,ΔP,i)

Burada i = ağdaki her bir eşanjör

Optimizasyon stratejisi:
1. En yüksek Ṡ_gen,i değerine sahip eşanjörü tespit et (darboğaz)
2. Bu eşanjörün Be sayısına bak → iyileştirme yönünü belirle
3. İyileştirmenin ağ genelindeki etkisini değerlendir
4. Tekrarla (iteratif)

Pinch analizi + EGM entegrasyonu:
- Pinch analizi: Minimum utility hedefini belirler (HEN topolojisi)
- EGM: Her eşanjörün bireysel tasarımını optimize eder
- Birlikte: Hem yapısal hem parametrik optimizasyon
```

---

## 12. ExergyLab Platformunda Kullanım

```
ExergyLab platformu, eşanjör EGM analizini aşağıdaki şekilde uygular:

1. Giriş verileri:
   - Akışkan debileri ve sıcaklıkları
   - Eşanjör tipi ve geometrisi (opsiyonel)
   - Basınç düşüşü ölçümleri (varsa)

2. Hesaplama motoru (engine/factory.py):
   - Ṡ_gen,ΔT otomatik hesaplanır (giriş/çıkış sıcaklıklarından)
   - Ṡ_gen,ΔP tahmin edilir (geometri verilmişse) veya tipik oranlardan
   - Bejan sayısı hesaplanır
   - Exergy yıkımı = T₀ × Ṡ_gen

3. AI yorumlama (knowledge + skills):
   - Be > 0.85 → "Approach temperature azaltılmalı" önerisi
   - Be < 0.50 → "Basınç düşüşü optimize edilmeli" önerisi
   - Fouling etkisi değerlendirmesi
   - Eşanjör tipi değişikliği önerisi (PHE vs S&T)

4. Raporlama:
   - Sankey diyagramında exergy akışları
   - Entropi üretimi ayrıştırma çubuk grafiği
   - Benchmark karşılaştırması
```

---

## İlgili Dosyalar

- [Isı Transferi EGM](heat_transfer_egm.md) -- Genel ısı transferi entropi üretimi teorisi
- [Akışkan Akışı EGM](fluid_flow_egm.md) -- Basınç düşüşü ve sürtünme tersinmezliği detayları
- [Isı Entegrasyonu](../heat_integration.md) -- Kaynak-kullanım eşleştirme ve sıcaklık kademesi
- [Pinch Analizi](../pinch_analysis.md) -- Eşanjör ağı tasarımı ve enerji hedefleri
- [Atık Isı Geri Kazanım](../waste_heat_recovery.md) -- WHR teknolojileri ve eşanjör seçimi
- [Proses Entegrasyonu](../process_integration.md) -- Fabrika seviyesinde proses entegrasyonu
- [Ekonomik Analiz](../economic_analysis.md) -- Yatırım değerlendirme ve NPV hesaplamaları
- [Exergy Temelleri](../exergy_fundamentals.md) -- Exergy tanımları ve temel denklemler
- [KPI Tanımları](../kpi_definitions.md) -- Performans göstergeleri ve eşik değerler
- [Kazan Çözümleri](../../boiler/solutions/) -- Economizer ve baca gazı ısı geri kazanımı

## Referanslar

- Bejan, A., "Entropy Generation Minimization," CRC Press, 1996
- Bejan, A., "Advanced Engineering Thermodynamics," 4th Edition, Wiley, 2016
- Bejan, A., "Entropy Generation Through Heat and Fluid Flow," Wiley, 1982
- Shah, R.K. & Sekulic, D.P., "Fundamentals of Heat Exchanger Design," Wiley, 2003
- Hesselgreaves, J.E., Law, R. & Reay, D., "Compact Heat Exchangers," 2nd Edition, Butterworth-Heinemann, 2017
- Kakaç, S., Liu, H. & Pramuanjaroenkij, A., "Heat Exchangers: Selection, Rating, and Thermal Design," 3rd Edition, CRC Press, 2012
- Incropera, F.P. et al., "Fundamentals of Heat and Mass Transfer," 7th Edition, Wiley, 2011
- TEMA Standards, "Standards of the Tubular Exchanger Manufacturers Association," 10th Edition, 2019
- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1994
- Yilmaz, M., Sara, O.N. & Karsli, S., "Performance evaluation criteria for heat exchangers based on second law analysis," Exergy, An International Journal, 1(4), 278-294, 2001
- Ogulata, R.T. & Doba, F., "Experiments and entropy generation minimization analysis of a cross-flow heat exchanger," International Journal of Heat and Mass Transfer, 41(2), 373-381, 1998
