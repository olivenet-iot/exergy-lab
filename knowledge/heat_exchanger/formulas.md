---
title: "Isı Eşanjörü Exergy Hesaplamaları"
category: reference
equipment_type: heat_exchanger
keywords: [exergy, ısı eşanjörü, LMTD, NTU, epsilon, termodinamik, ısı transferi]
related_files: [heat_exchanger/benchmarks.md, heat_exchanger/audit.md, heat_exchanger/standards.md]
use_when: ["Isı eşanjörü exergy hesaplaması yapılırken", "Isı transferi formülleri gerektiğinde", "Exergy yıkım hesabı yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Isı Eşanjörü Exergy Hesaplamaları

> Son güncelleme: 2026-02-01

## Temel İlkeler

Isı eşanjörleri (heat exchangers), iki veya daha fazla akışkan arasında ısı transferi
sağlayan termodinamik cihazlardır. Exergy analizi açısından, eşanjörlerdeki
tersinmezliklerin iki temel kaynağı vardır:

1. **Sonlu sıcaklık farkı ile ısı transferi** — Sıcak ve soğuk akışkan arasındaki
   sıcaklık farkı büyüdükçe entropi üretimi ve dolayısıyla exergy yıkımı artar.
2. **Basınç kayıpları** — Boru, gövde ve plaka tarafındaki sürtünme kayıpları
   mekanik exergy yıkımına neden olur.

**Enerji verimi ile exergy verimi farkı:**
Isı eşanjörleri genellikle %95-99 enerji verimine sahiptir (kayıp sadece izolasyon
kaybı), ancak exergy verimi %20-80 arasında değişir. Bu büyük fark, ısı transferinin
sıcaklık kalitesini (exergy) düşürmesinden kaynaklanır.

## 1. Isı Yükleri Hesaplamaları (Heat Duty)

### 1.1 Temel Isı Transferi Denklemi

```
Q = U x A x LMTD x F

Burada:
- Q = ısı yükü [kW]
- U = toplam ısı transfer katsayısı [W/(m2·K)]
- A = ısı transfer yüzey alanı [m2]
- LMTD = logaritmik ortalama sıcaklık farkı [°C veya K]
- F = düzeltme faktörü (çok geçişli eşanjörler için, 0 < F <= 1)
```

Tek geçişli ters akış (counterflow) eşanjörlerde F = 1.0 alınır.
Çok geçişli (multi-pass) eşanjörlerde F < 1.0 olur ve TEMA grafiklerinden
veya korelasyonlardan belirlenir. Genellikle F >= 0.75 tasarım limiti uygulanır.

### 1.2 Logaritmik Ortalama Sıcaklık Farkı — LMTD

**Ters akış (counterflow):**
```
LMTD_cf = (DT_1 - DT_2) / ln(DT_1 / DT_2)

Burada:
- DT_1 = T_h,in - T_c,out  (sıcak giriş - soğuk çıkış)
- DT_2 = T_h,out - T_c,in  (sıcak çıkış - soğuk giriş)
```

**Paralel akış (parallel flow):**
```
LMTD_pf = (DT_1 - DT_2) / ln(DT_1 / DT_2)

Burada:
- DT_1 = T_h,in - T_c,in   (sıcak giriş - soğuk giriş)
- DT_2 = T_h,out - T_c,out (sıcak çıkış - soğuk çıkış)
```

**Özel Durum:** DT_1 = DT_2 ise LMTD = DT_1 = DT_2 (aritmetik eşitlik).

**Sayısal Örnek (Ters Akış):**
```
T_h,in = 150°C, T_h,out = 90°C
T_c,in = 30°C, T_c,out = 80°C

DT_1 = 150 - 80 = 70°C
DT_2 = 90 - 30 = 60°C

LMTD = (70 - 60) / ln(70/60) = 10 / ln(1.167) = 10 / 0.1542 = 64.9°C
```

### 1.3 Düzeltme Faktörü (F) — Çok Geçişli Eşanjörler

```
F = f(R, P)

Burada:
- R = (T_h,in - T_h,out) / (T_c,out - T_c,in) = kapasite oranı
- P = (T_c,out - T_c,in) / (T_h,in - T_c,in) = sıcaklık etkililiği
```

Tipik F değerleri:

| Konfigürasyon | F Aralığı | Not |
|---------------|-----------|-----|
| 1 gövde / 2 boru geçişi | 0.80 - 1.00 | En yaygın |
| 2 gövde / 4 boru geçişi | 0.85 - 1.00 | Daha iyi performans |
| Çapraz akış (cross flow) | 0.70 - 0.95 | Hava soğutmalı HX |
| Ters akış (counterflow) | 1.00 | Referans |

**Tasarım kuralı:** F < 0.75 ise gövde sayısı artırılmalıdır.

## 2. Toplam Isı Transfer Katsayısı (Overall U)

### 2.1 Temel U Hesaplaması

```
1/U = 1/h_i + R_f,i + (r_o × ln(r_o/r_i)) / k_w + R_f,o + (1/h_o) × (A_i/A_o)

Burada:
- h_i = iç taraf (boru/plaka) konveksiyon katsayısı [W/(m2·K)]
- h_o = dış taraf (gövde) konveksiyon katsayısı [W/(m2·K)]
- R_f,i = iç taraf kirlenme direnci [m2·K/W]
- R_f,o = dış taraf kirlenme direnci [m2·K/W]
- r_o, r_i = dış ve iç boru yarıçapları [m]
- k_w = boru duvarı ısı iletim katsayısı [W/(m·K)]
- A_i, A_o = iç ve dış yüzey alanları [m2]
```

### 2.2 Basitleştirilmiş U (İnce Duvar)

```
1/U = 1/h_i + R_f,i + t_w/k_w + R_f,o + 1/h_o

Burada:
- t_w = duvar kalınlığı [m]
- k_w = duvar ısı iletim katsayısı [W/(m·K)]
```

### 2.3 Tipik U Değerleri

| Akışkan Kombinasyonu | U [W/(m2·K)] | Not |
|----------------------|--------------|-----|
| Su - Su | 800 - 2,500 | En yüksek |
| Su - Yağ | 100 - 350 | Düşük h_yağ |
| Buhar - Su | 1,000 - 3,500 | Yoğuşma etkisi |
| Buhar (yoğuşma) - Su | 1,500 - 4,000 | Filmli yoğuşma |
| Gaz - Gaz | 10 - 50 | En düşük |
| Gaz - Su | 20 - 300 | Gaz tarafı sınırlı |
| Organik buhar - Su | 300 - 1,000 | ORC uygulamaları |
| Hava - Su (finli) | 25 - 60 | Hava soğutmalı HX |

### 2.4 Kirlenme Direnci (Fouling Resistance)

TEMA standartlarından tipik kirlenme direnci değerleri:

| Akışkan | R_f [m2·K/W] | Not |
|---------|--------------|-----|
| Şehir suyu (< 50°C) | 0.000176 | Temiz su |
| Şehir suyu (> 50°C) | 0.000352 | Kireç oluşumu |
| Soğutma kulesi suyu | 0.000176 - 0.000352 | İşleme bağlı |
| Kazan besleme suyu (arıtılmış) | 0.000088 | Arıtılmış |
| Buhar (temiz) | 0.000088 | Minimal kirlenme |
| Fuel oil | 0.000880 | Yüksek kirlenme |
| Doğalgaz (yanma ürünleri) | 0.000176 - 0.000528 | İs ve kül |
| Motor yağları | 0.000176 | Temiz yağ |
| Proses suyu (endüstriyel) | 0.000352 - 0.000528 | Değişken |

**Kirlenme Etkisi Örneği:**
```
U_temiz = 1,200 W/(m2·K)
R_f_toplam = 0.000352 + 0.000176 = 0.000528 m2·K/W

1/U_kirli = 1/U_temiz + R_f_toplam
1/U_kirli = 1/1200 + 0.000528 = 0.000833 + 0.000528 = 0.001361

U_kirli = 735 W/(m2·K)

Performans düşüşü = (1200 - 735) / 1200 = %38.7
```

## 3. Epsilon-NTU Yöntemi (Effectiveness-NTU)

### 3.1 Temel Tanımlar

```
NTU = (U x A) / C_min

Burada:
- NTU = Transfer Birim Sayısı (Number of Transfer Units) [boyutsuz]
- U = toplam ısı transfer katsayısı [W/(m2·K)]
- A = ısı transfer yüzey alanı [m2]
- C_min = min(m_h x cp_h, m_c x cp_c) [W/K]
```

```
C_r = C_min / C_max   (kapasite oranı, 0 <= C_r <= 1)
```

```
epsilon = Q / Q_max = Q / (C_min x (T_h,in - T_c,in))

Burada:
- epsilon = ısı eşanjörü etkililiği (effectiveness) [boyutsuz, 0-1]
- Q = gerçek ısı transferi [kW]
- Q_max = termodinamik olarak mümkün maksimum ısı transferi [kW]
```

### 3.2 Epsilon-NTU Korelasyonları

**Ters akış (counterflow):**
```
C_r < 1 için:
  epsilon = [1 - exp(-NTU × (1 - C_r))] / [1 - C_r × exp(-NTU × (1 - C_r))]

C_r = 1 için:
  epsilon = NTU / (1 + NTU)
```

**Paralel akış (parallel flow):**
```
epsilon = [1 - exp(-NTU × (1 + C_r))] / (1 + C_r)
```

**Gövde-boru (1 gövde geçişi, çift sayıda boru geçişi):**
```
epsilon = 2 / {(1 + C_r) + sqrt(1 + C_r^2) × [1 + exp(-NTU × sqrt(1 + C_r^2))] / [1 - exp(-NTU × sqrt(1 + C_r^2))]}
```

**Çapraz akış (her iki akışkan karışık değil):**
```
epsilon = 1 - exp{(NTU^0.22 / C_r) × [exp(-C_r × NTU^0.78) - 1]}
```

### 3.3 Sayısal Örnek (Epsilon-NTU)

```
Veriler:
- U = 500 W/(m2·K), A = 25 m2
- m_h = 2.0 kg/s, cp_h = 4.18 kJ/(kg·K) --> C_h = 8,360 W/K
- m_c = 3.0 kg/s, cp_c = 4.18 kJ/(kg·K) --> C_c = 12,540 W/K
- T_h,in = 95°C, T_c,in = 25°C

Hesaplama:
C_min = 8,360 W/K (sıcak taraf)
C_max = 12,540 W/K (soğuk taraf)
C_r = 8,360 / 12,540 = 0.667
NTU = (500 × 25) / 8,360 = 1.495

Ters akış:
epsilon = [1 - exp(-1.495 × (1 - 0.667))] / [1 - 0.667 × exp(-1.495 × (1 - 0.667))]
epsilon = [1 - exp(-0.498)] / [1 - 0.667 × exp(-0.498)]
epsilon = [1 - 0.608] / [1 - 0.667 × 0.608]
epsilon = 0.392 / 0.594 = 0.660

Q = epsilon × C_min × (T_h,in - T_c,in)
Q = 0.660 × 8,360 × (95 - 25) = 386.2 kW

T_h,out = T_h,in - Q/C_h = 95 - 386,200/8,360 = 95 - 46.2 = 48.8°C
T_c,out = T_c,in + Q/C_c = 25 + 386,200/12,540 = 25 + 30.8 = 55.8°C
```

## 4. Exergy Analizi

### 4.1 Akışkan Exergy Hesabı

Sıvı akışkanlar için spesifik exergy (çevre sıcaklığına göre):
```
ex = (h - h_0) - T_0 × (s - s_0)

Burada:
- ex = spesifik exergy [kJ/kg]
- h = entalpi [kJ/kg]
- h_0 = referans (çevre) durumu entalpisi [kJ/kg]
- s = entropi [kJ/(kg·K)]
- s_0 = referans (çevre) durumu entropisi [kJ/(kg·K)]
- T_0 = çevre sıcaklığı [K] (genellikle 25°C = 298.15 K)
```

İdeal sıvı (sıkıştırılamaz) yaklaşımı:
```
ex ≈ cp × [(T - T_0) - T_0 × ln(T/T_0)] + v × (P - P_0)

Burada:
- cp = özgül ısı [kJ/(kg·K)]
- T, T_0 = sıcaklık [K]
- v = özgül hacim [m3/kg]
- P, P_0 = basınç [Pa]
```

### 4.2 Entropi Üretimi (Entropy Generation)

Isı eşanjöründe toplam entropi üretimi:
```
S_gen = m_h × (s_h,out - s_h,in) + m_c × (s_c,out - s_c,in)

İdeal sıvı yaklaşımı:
S_gen = m_h × cp_h × ln(T_h,out / T_h,in) + m_c × cp_c × ln(T_c,out / T_c,in)
```

**Basınç düşüşünden kaynaklı ek entropi üretimi:**
```
S_gen,DP = m_h × v_h × DP_h / T_h,avg + m_c × v_c × DP_c / T_c,avg

Burada:
- v = özgül hacim [m3/kg]
- DP = basınç düşüşü [Pa]
- T_avg = ortalama akışkan sıcaklığı [K]
```

### 4.3 Exergy Yıkımı (Exergy Destruction)

Gouy-Stodola teoremi:
```
I = T_0 × S_gen

Burada:
- I = exergy yıkımı (irreversibility) [kW]
- T_0 = çevre (ölü durum) sıcaklığı [K]
- S_gen = toplam entropi üretimi [kW/K]
```

Bileşenlere göre exergy yıkımı:
```
I_toplam = I_DT + I_DP

I_DT = T_0 × S_gen,DT    (sıcaklık farkına bağlı)
I_DP = T_0 × S_gen,DP     (basınç düşüşüne bağlı)
```

Tipik dağılım:
- I_DT: toplam exergy yıkımının %85-95'i
- I_DP: toplam exergy yıkımının %5-15'i

### 4.4 Exergy Verimi (Exergy Efficiency)

**Tanımlanma 1 — Genel:**
```
eta_ex = 1 - (T_0 × S_gen) / (Ex_hot,in - Ex_hot,out)

Burada:
- Ex_hot,in = m_h × ex_h,in = sıcak akışkan giriş exergy'si [kW]
- Ex_hot,out = m_h × ex_h,out = sıcak akışkan çıkış exergy'si [kW]
```

**Tanımlanma 2 — Ürün/Yakıt:**
```
eta_ex = Ex_ürün / Ex_yakıt = (Ex_c,out - Ex_c,in) / (Ex_h,in - Ex_h,out)

Burada:
- Exergy yakıtı = sıcak akışkanın exergy azalması
- Exergy ürünü = soğuk akışkanın exergy artışı
```

**Tanımlanma 3 — Ekserjitik Etkinlik Katsayısı (Witte-Shamsundar):**
```
eta_ex = 1 - I / Ex_yakıt = 1 - (T_0 × S_gen) / (Ex_h,in - Ex_h,out)
```

### 4.5 Sayısal Örnek — Tam Exergy Analizi

```
Veriler (Bölüm 3.3'ten devam):
- T_0 = 25°C = 298.15 K
- T_h,in = 95°C = 368.15 K, T_h,out = 48.8°C = 321.95 K
- T_c,in = 25°C = 298.15 K, T_c,out = 55.8°C = 328.95 K
- m_h = 2.0 kg/s, cp_h = 4.18 kJ/(kg·K)
- m_c = 3.0 kg/s, cp_c = 4.18 kJ/(kg·K)
- Q = 386.2 kW

Entropi Üretimi:
S_gen = m_h × cp_h × ln(T_h,out/T_h,in) + m_c × cp_c × ln(T_c,out/T_c,in)
S_gen = 2.0 × 4.18 × ln(321.95/368.15) + 3.0 × 4.18 × ln(328.95/298.15)
S_gen = 8.36 × (-0.1340) + 12.54 × (0.0981)
S_gen = -1.120 + 1.230 = 0.110 kW/K

Exergy Yıkımı:
I = T_0 × S_gen = 298.15 × 0.110 = 32.8 kW

Sıcak Taraf Exergy Değişimi:
Ex_h,in = m_h × cp_h × [(T_h,in - T_0) - T_0 × ln(T_h,in/T_0)]
Ex_h,in = 2.0 × 4.18 × [(95 - 25) - 298.15 × ln(368.15/298.15)]
Ex_h,in = 8.36 × [70 - 298.15 × 0.2107]
Ex_h,in = 8.36 × [70 - 62.84] = 8.36 × 7.16 = 59.9 kW

Ex_h,out = m_h × cp_h × [(T_h,out - T_0) - T_0 × ln(T_h,out/T_0)]
Ex_h,out = 8.36 × [(48.8 - 25) - 298.15 × ln(321.95/298.15)]
Ex_h,out = 8.36 × [23.8 - 298.15 × 0.0767]
Ex_h,out = 8.36 × [23.8 - 22.87] = 8.36 × 0.93 = 7.8 kW

Soğuk Taraf Exergy Değişimi:
Ex_c,out = m_c × cp_c × [(T_c,out - T_0) - T_0 × ln(T_c,out/T_0)]
Ex_c,out = 12.54 × [(55.8 - 25) - 298.15 × ln(328.95/298.15)]
Ex_c,out = 12.54 × [30.8 - 298.15 × 0.0981]
Ex_c,out = 12.54 × [30.8 - 29.26] = 12.54 × 1.54 = 19.3 kW

Ex_c,in = 0 kW  (soğuk akışkan çevre sıcaklığında)

Exergy Verimi:
eta_ex = (Ex_c,out - Ex_c,in) / (Ex_h,in - Ex_h,out)
eta_ex = (19.3 - 0) / (59.9 - 7.8) = 19.3 / 52.1 = 0.370 = %37.0

Doğrulama:
I = (Ex_h,in - Ex_h,out) - (Ex_c,out - Ex_c,in) = 52.1 - 19.3 = 32.8 kW ✓
```

## 5. Basınç Düşüşü Exergy Kaybı

### 5.1 Basınç Düşüşü Hesabı

**Boru tarafı (Darcy-Weisbach):**
```
DP_t = f × (L/d_i) × (rho × v^2 / 2) + n × K_loss × (rho × v^2 / 2)

Burada:
- f = Darcy sürtünme faktörü [boyutsuz]
- L = boru uzunluğu [m]
- d_i = boru iç çapı [m]
- rho = akışkan yoğunluğu [kg/m3]
- v = akışkan hızı [m/s]
- n = kayıp sayısı (dirsek, giriş/çıkış, vb.)
- K_loss = yerel kayıp katsayısı
```

**Gövde tarafı (Bell-Delaware yöntemi):**
```
DP_s = f_s × N_b × (rho × v_s^2 / 2) × (D_s / D_e)

Burada:
- f_s = gövde tarafı sürtünme faktörü
- N_b = bafıl sayısı
- v_s = gövde tarafı referans hızı [m/s]
- D_s = gövde iç çapı [m]
- D_e = eşdeğer hidrolik çap [m]
```

### 5.2 Basınç Düşüşünden Exergy Kaybı

```
I_DP = m × v × DP × T_0 / T_avg

Burada:
- m = kütle debisi [kg/s]
- v = özgül hacim [m3/kg]
- DP = basınç düşüşü [Pa]
- T_0 = çevre sıcaklığı [K]
- T_avg = ortalama akışkan sıcaklığı [K]
```

Pompa işi gereksinimi olarak:
```
W_pompa = m × v × DP / eta_pompa

Exergy kaybı = W_pompa × (1 - eta_ex,pompa)
```

### 5.3 Sayısal Örnek — Basınç Düşüşü

```
Veriler:
- m = 5.0 kg/s (su)
- DP = 45 kPa = 45,000 Pa
- T_avg = 60°C = 333.15 K
- T_0 = 25°C = 298.15 K
- v = 0.001017 m3/kg
- eta_pompa = 0.70

Pompa işi: W = 5.0 × 0.001017 × 45,000 / 0.70 = 327 W = 0.327 kW

Exergy kaybı (basınç düşüşü):
I_DP = 5.0 × 0.001017 × 45,000 × (298.15/333.15) = 204.5 W = 0.205 kW
```

## 6. Yaklaşım Sıcaklığı (Approach Temperature)

### 6.1 Tanım

```
DT_approach = T_h,out - T_c,in    (ters akış, sıcak taraf yaklaşımı)

veya

DT_approach = T_c,out - T_h,in    (bu genellikle negatif, pratikte kullanılmaz)
```

Minimum yaklaşım sıcaklığı (minimum approach temperature):
```
DT_min = min(DT_1, DT_2)

DT_1 = T_h,in - T_c,out
DT_2 = T_h,out - T_c,in
```

### 6.2 Yaklaşım Sıcaklığı ve Exergy İlişkisi

Düşük yaklaşım sıcaklığı:
- Daha az entropi üretimi → daha yüksek exergy verimi
- Ancak: daha büyük transfer alanı → daha yüksek yatırım maliyeti

```
Yaklaşım azaldıkça:
  S_gen azalır → I = T_0 × S_gen azalır → eta_ex artar
  Ancak: A artar → maliyet artar
```

| DT_approach [°C] | Göreceli Exergy Verimi | Göreceli Maliyet |
|-------------------|----------------------|-----------------|
| 3 - 5 | Referans (%100) | Çok yüksek |
| 5 - 10 | %90 - %95 | Yüksek |
| 10 - 20 | %75 - %90 | Orta |
| 20 - 40 | %55 - %75 | Düşük |
| > 40 | < %55 | Çok düşük |

## 7. Özel Durumlar

### 7.1 Faz Değişimli Isı Transferi

Buhar yoğuşması veya kaynatma durumunda:
```
C_faz_değişimi = m × h_fg → sonsuz (C_max → sonsuz, C_r → 0)

Bu durumda:
epsilon = 1 - exp(-NTU)    (C_r = 0 özel durumu)
```

### 7.2 Ekonomizer (Baca Gazı → Su)

```
Q_eco = m_gaz × cp_gaz × (T_gaz,in - T_gaz,out)
Q_eco = m_su × cp_su × (T_su,out - T_su,in)

Tipik değerler:
- T_gaz,in = 250 - 400°C
- T_gaz,out = 120 - 180°C (asit çiğlenmesi sınırına dikkat!)
- T_su,in = 80 - 105°C (kondensat sıcaklığı)
- T_su,out = 120 - 170°C
```

Asit çiğlenmesi sınırı (doğalgaz için):
```
T_çiğlenmesi ≈ 55°C (doğalgaz, düşük kükürt)
T_çiğlenmesi ≈ 120 - 150°C (fuel oil, yüksek kükürt)
```

### 7.3 Isıl Kapasite Oranının Exergy Verimi Üzerindeki Etkisi

```
C_r = 0: Faz değişimi (yoğuşma/kaynatma) → En yüksek eta_ex
C_r = 1: Dengeli akış → Orta eta_ex
C_r >> 1 veya << 1: Dengesiz akış → Düşük eta_ex
```

Optimal tasarım için C_r = 1'e yakın olması istenir (faz değişimi yoksa).

## 8. Performans İzleme Formülleri

### 8.1 Temizlik Faktörü (Cleanliness Factor)

```
CF = U_gerçek / U_temiz

Burada:
- CF = temizlik faktörü [boyutsuz, 0-1]
- U_gerçek = ölçülen toplam ısı transfer katsayısı
- U_temiz = temiz durumdaki tasarım U değeri
```

| CF Değeri | Durum | Aksiyon |
|-----------|-------|---------|
| > 0.85 | İyi | Rutin izleme |
| 0.70 - 0.85 | Orta | Temizlik planla |
| 0.50 - 0.70 | Kötü | Acil temizlik |
| < 0.50 | Kritik | Derhal temizlik + kök neden |

### 8.2 U-Değer Hesaplama (Ölçümden)

```
U_ölçülen = Q / (A × LMTD × F)

Q = m × cp × DT  (sıcak veya soğuk taraftan)
```

## İlgili Dosyalar

- `heat_exchanger/benchmarks.md` — Performans karşılaştırma verileri
- `heat_exchanger/audit.md` — Denetim ve ölçüm metodolojisi
- `heat_exchanger/standards.md` — TEMA, ASME standart referansları
- `heat_exchanger/case_studies.md` — Hesaplama örnekleri ve vaka çalışmaları

## Referanslar

1. Bejan, A. (1982). *Entropy Generation through Heat and Fluid Flow*. Wiley.
2. Incropera, F.P. & DeWitt, D.P. (2011). *Fundamentals of Heat and Mass Transfer*. 7th ed., Wiley.
3. Shah, R.K. & Sekulic, D.P. (2003). *Fundamentals of Heat Exchanger Design*. Wiley.
4. Kakac, S., Liu, H. & Pramuanjaroenkij, A. (2012). *Heat Exchangers: Selection, Rating, and Thermal Design*. 3rd ed., CRC Press.
5. TEMA (2019). *Standards of the Tubular Exchanger Manufacturers Association*. 10th ed.
6. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
7. Szargut, J., Morris, D.R. & Steward, F.R. (1988). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*. Hemisphere.
8. ESDU 83038. (1983). *Effectiveness-NTU Relationships for Heat Exchangers*.
9. Bell, K.J. (1981). *Delaware Method for Shell-Side Design*. Heat Exchanger Design Handbook.
10. ASME PTC 12.5 (2000). *Single Phase Heat Exchangers*.
