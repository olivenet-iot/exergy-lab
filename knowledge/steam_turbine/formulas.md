---
title: "Buhar Türbini Exergy Hesaplama Formülleri — Steam Turbine Exergy Calculation Formulas"
category: reference
equipment_type: steam_turbine
keywords: [buhar türbini, exergy, izentropik verim, Rankine çevrimi, CHP, Baumann kuralı, çok kademeli türbin]
related_files: [steam_turbine/benchmarks.md, steam_turbine/audit.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/condensing.md, steam_turbine/systems/steam_turbine_chp.md]
use_when: ["Buhar türbini exergy hesaplaması yapılırken", "Türbin performans formülleri gerektiğinde", "CHP exergy verimi hesaplanırken"]
priority: high
last_updated: 2026-01-31
---
# Buhar Türbini Exergy Hesaplama Formülleri — Steam Turbine Exergy Calculation Formulas

> Son güncelleme: 2026-01-31

## 1. Temel Termodinamik Büyüklükler (Basic Thermodynamic Properties)

### 1.1 Buhar Durumu Tanımlama

```
Buhar durumunu belirlemek için iki bağımsız özellik gerekir:
- Giriş: Sıcaklık (T) ve Basınç (P) → kızdırılmış buhar bölgesi
- Çıkış: Basınç (P) ve kalite (x) veya T ve P → yaş/kızdırılmış bölge

Entalpi (enthalpy):
h = f(T, P)  [kJ/kg]

Entropi (entropy):
s = f(T, P)  [kJ/(kg·K)]

Yaş buhar bölgesinde (wet steam region):
h = h_f + x × h_fg   [kJ/kg]
s = s_f + x × s_fg   [kJ/(kg·K)]

Burada:
- h_f = doymuş sıvı entalpisi [kJ/kg]
- h_fg = buharlaşma entalpisi (latent heat) [kJ/kg]
- x = buhar kalitesi (dryness fraction) [0-1]
- s_f = doymuş sıvı entropisi [kJ/(kg·K)]
- s_fg = buharlaşma entropisi [kJ/(kg·K)]
```

### 1.2 Referans Durum (Dead State)

```
Referans çevre koşulları (dead state):
T₀ = 25°C = 298.15 K (standart)
P₀ = 101.325 kPa = 1.01325 bar

Referans entalpi: h₀ = h(T₀, P₀) = 104.89 kJ/kg (sıvı su)
Referans entropi: s₀ = s(T₀, P₀) = 0.3674 kJ/(kg·K)

Not: Türk endüstriyel koşulları için T₀ = 15-35°C
kullanılabilir (mevsimsel ortalama).
```

## 2. Türbin Güç Hesaplamaları (Turbine Power Calculations)

### 2.1 İdeal (İzentropik) Güç

```
İzentropik genişleme (isentropic expansion):
s_çıkış,is = s_giriş   (entropi sabit)

İzentropik çıkış entalpisi:
h_çıkış,is = h(P_çıkış, s = s_giriş)  [kJ/kg]

İdeal spesifik iş:
w_is = h_giriş - h_çıkış,is  [kJ/kg]

İdeal güç:
Ẇ_is = ṁ × (h_giriş - h_çıkış,is)  [kW]

Burada:
- ṁ = buhar kütle debisi [kg/s]
- h_giriş = türbin giriş entalpisi [kJ/kg]
- h_çıkış,is = izentropik çıkış entalpisi [kJ/kg]
```

### 2.2 Gerçek Güç ve İzentropik Verim

```
İzentropik verim (isentropic efficiency):
η_is = (h_giriş - h_çıkış) / (h_giriş - h_çıkış,is)

Gerçek çıkış entalpisi:
h_çıkış = h_giriş - η_is × (h_giriş - h_çıkış,is)  [kJ/kg]

Gerçek türbin gücü:
Ẇ_türbin = ṁ × (h_giriş - h_çıkış)  [kW]

Jeneratör çıkışı (net elektrik):
Ẇ_elek = Ẇ_türbin × η_mek × η_jen  [kW]

Burada:
- η_mek = mekanik verim [0.97-0.99] (sürtünme, yataklar)
- η_jen = jeneratör verimi [0.95-0.98]

Tipik izentropik verim değerleri:
- Küçük tek kademeli (<1 MW): %55-70
- Orta çok kademeli (1-10 MW): %70-82
- Büyük çok kademeli (10-100 MW): %82-90
- Büyük santral tipi (>100 MW): %88-93
```

### 2.3 Spesifik Buhar Tüketimi (Specific Steam Consumption — SSC)

```
SSC = ṁ / Ẇ_elek  [kg/kWh]

SSC = 3,600 / [(h_giriş - h_çıkış) × η_mek × η_jen]  [kg/kWh]

Tipik SSC değerleri:
- Karşı basınçlı (back-pressure): 10-25 kg/kWh
- Yoğuşmalı (condensing): 3.5-6.0 kg/kWh
- Çekişli (extraction): 5-15 kg/kWh

Düşük SSC → yüksek türbin verimi (daha az buhar/kWh)
```

## 3. Exergy Hesaplamaları (Exergy Calculations)

### 3.1 Buhar Akışının Spesifik Exergisi

```
Spesifik fiziksel exergy (specific physical exergy):
ex = (h - h₀) - T₀ × (s - s₀)  [kJ/kg]

Burada:
- h = buhar entalpisi [kJ/kg]
- h₀ = referans durum entalpisi [kJ/kg]
- s = buhar entropisi [kJ/(kg·K)]
- s₀ = referans durum entropisi [kJ/(kg·K)]
- T₀ = referans sıcaklık [K]

Exergy akış hızı:
Ėx = ṁ × ex  [kW]
```

### 3.2 Türbin Giriş ve Çıkış Exergisi

```
Giriş exergisi:
ex_giriş = (h_giriş - h₀) - T₀ × (s_giriş - s₀)  [kJ/kg]
Ėx_giriş = ṁ × ex_giriş  [kW]

Çıkış exergisi:
ex_çıkış = (h_çıkış - h₀) - T₀ × (s_çıkış - s₀)  [kJ/kg]
Ėx_çıkış = ṁ × ex_çıkış  [kW]

Türbin iş çıkışı (saf exergy):
Ẇ_türbin = ṁ × (h_giriş - h_çıkış)  [kW]
Not: İş (work) saf exergydir, Carnot sınırlaması yoktur.
```

### 3.3 Exergy Verimi (Exergy Efficiency)

```
Yoğuşmalı türbin exergy verimi (condensing turbine):
η_ex = Ẇ_türbin / (Ėx_giriş - Ėx_çıkış)
     = Ẇ_türbin / ΔĖx

Alternatif form:
η_ex = Ẇ_elek / Ėx_giriş  (brüt exergy verimi — gross exergy efficiency)

Karşı basınçlı türbin exergy verimi (back-pressure turbine):
η_ex = (Ẇ_elek + Ėx_proses_buhar) / Ėx_giriş

Burada Ėx_proses_buhar türbin çıkışından prosese giden buharın exergisidir.

CHP exergy verimi (combined heat and power):
η_ex,CHP = (Ẇ_elek + Ex_ısı) / Ex_yakıt

Isı exergisi:
Ex_ısı = Q̇_ısı × (1 - T₀/T_ısı)  [kW]

Not: T_ısı, ısı transferinin gerçekleştiği ortalama sıcaklıktır.
Düşük sıcaklıklı ısının exergy içeriği düşüktür.
```

### 3.4 Exergy Yıkımı ve Kaybı

```
Exergy dengesi (exergy balance):
Ėx_giriş = Ẇ_türbin + Ėx_çıkış + Ėx_yıkım + Ėx_kayıp

Exergy yıkımı (irreversibility):
Ėx_yıkım = T₀ × Ṡ_üretim  [kW]

Entropi üretim hızı:
Ṡ_üretim = ṁ × (s_çıkış - s_giriş)  [kW/K]

Exergy yıkım oranı:
y_D = Ėx_yıkım / Ėx_giriş  [%]

Türbin exergy yıkım kaynakları:
1. Kanat profil kayıpları (blade profile losses): %2-5
2. İkincil akış kayıpları (secondary flow losses): %1-3
3. Kanat ucu sızıntısı (tip leakage): %1-4
4. Nem kayıpları (moisture losses): %0-3 (yaş buhar bölgesinde)
5. Çıkış kinetik enerji kaybı (leaving loss): %0.5-2
6. Sızdırmazlık kayıpları (seal leakage): %0.5-2
7. Mekanik kayıplar (bearings, governor): %0.5-1
```

## 4. Karşı Basınçlı Türbin Formülleri (Back-Pressure Turbine)

### 4.1 Temel Hesaplama

```
Karşı basınçlı türbin:
- Giriş: Yüksek basınçlı buhar (tipik 20-80 bar, 350-500°C)
- Çıkış: Proses basıncında buhar (tipik 2-15 bar)
- Tüm çıkış buharı proseste kullanılır

Elektrik üretimi:
Ẇ_elek = ṁ × (h_giriş - h_çıkış) × η_mek × η_jen  [kW]

Proses ısısı:
Q̇_proses = ṁ × (h_çıkış - h_kondensat)  [kW]

Isı/Güç oranı (Heat-to-Power Ratio — HPR):
HPR = Q̇_proses / Ẇ_elek

Karşı basınçlı türbin HPR: 3-10 (tipik)
→ Yüksek HPR = düşük elektrik, yüksek ısı verimi

Toplam enerji verimi:
η_enerji = (Ẇ_elek + Q̇_proses) / Q̇_yakıt × 100  [%]
Tipik: %80-92

Toplam exergy verimi:
η_exergy = (Ẇ_elek + Ėx_proses) / Ėx_yakıt × 100  [%]
Tipik: %25-38
```

### 4.2 Hesaplama Örneği — Karşı Basınçlı Türbin

```
Senaryo: 5 MW karşı basınçlı buhar türbini CHP

Giriş koşulları:
- P_giriş = 40 bar, T_giriş = 400°C
- h_giriş = 3,214 kJ/kg
- s_giriş = 6.769 kJ/(kg·K)
- ex_giriş = (3,214 - 104.89) - 298.15 × (6.769 - 0.3674)
           = 3,109.1 - 1,908.8 = 1,200.3 kJ/kg

Çıkış koşulları:
- P_çıkış = 4 bar (proses buharı)
- η_is = 0.80

İzentropik çıkış (s_çıkış,is = 6.769 kJ/(kg·K) @ 4 bar):
- h_çıkış,is = 2,753 kJ/kg (kızdırılmış buhar)

Gerçek çıkış:
h_çıkış = 3,214 - 0.80 × (3,214 - 2,753) = 3,214 - 368.8 = 2,845.2 kJ/kg
s_çıkış = 7.051 kJ/(kg·K) (CoolProp ile)
ex_çıkış = (2,845.2 - 104.89) - 298.15 × (7.051 - 0.3674)
         = 2,740.3 - 1,992.8 = 747.5 kJ/kg

Buhar debisi (5 MW elektrik için):
ṁ = Ẇ_elek / [(h_giriş - h_çıkış) × η_mek × η_jen]
  = 5,000 / [(3,214 - 2,845.2) × 0.98 × 0.97]
  = 5,000 / [368.8 × 0.9506]
  = 5,000 / 350.6 = 14.26 kg/s = 51.3 ton/h

Exergy analizi:
Ėx_giriş = 14.26 × 1,200.3 = 17,116 kW
Ėx_çıkış = 14.26 × 747.5 = 10,659 kW
Ẇ_türbin = 14.26 × 368.8 = 5,259 kW

Exergy dengesi:
Ėx_yıkım = 17,116 - 5,259 - 10,659 = 1,198 kW
η_ex = (Ẇ_elek + Ėx_çıkış) / Ėx_giriş = (5,000 + 10,659) / 17,116 = %91.5

Sadece iş bazlı exergy verimi:
η_ex,iş = 5,259 / (17,116 - 10,659) = 5,259 / 6,457 = %81.4

Proses ısısı (kondensat dönüşü 80°C):
h_kondensat = 335 kJ/kg
Q̇_proses = 14.26 × (2,845.2 - 335) = 35,784 kW = 35.8 MW_th

HPR = 35,784 / 5,000 = 7.16

Toplam enerji verimi:
Yakıt (kazan η = 88%):
Q̇_yakıt = 14.26 × (3,214 - 335) / 0.88 = 46,663 kW
η_enerji = (5,000 + 35,784) / 46,663 = %87.4

CHP exergy verimi:
Ex_yakıt = 46,663 × 1.04 = 48,529 kW (φ = 1.04 doğalgaz)
Ex_proses = Q̇_proses × (1 - T₀/T_proses)
T_proses = (143.6 + 80) / 2 + 273.15 = 384.95 K (ortalama)
Ex_proses = 35,784 × (1 - 298.15/384.95) = 35,784 × 0.226 = 8,087 kW
η_ex,CHP = (5,000 + 8,087) / 48,529 = %27.0
```

## 5. Yoğuşmalı Türbin Formülleri (Condensing Turbine)

### 5.1 Temel Hesaplama

```
Yoğuşmalı türbin:
- Giriş: Yüksek basınçlı buhar
- Çıkış: Vakum koşulları (tipik 0.05-0.10 bar)
- Maksimum güç çıkarımı, proses ısısı yok

Çıkış buhar kalitesi (yaş buhar bölgesinde):
x_çıkış = (h_çıkış - h_f) / h_fg

Yaş buhar nedeniyle verim kaybı — Baumann Kuralı:
η_is,yaş = η_is,kuru × [1 - α × (1 - x_ort)]

Burada:
- η_is,kuru = kuru buhar izentropik verimi
- α = Baumann faktörü ≈ 1.0 (genellikle)
- x_ort = ortalama buhar kalitesi = (x_giriş + x_çıkış) / 2

Pratik kural: Her %1 nem (moisture) ≈ %1 verim kaybı

Exhaust loss (çıkış kinetik enerji kaybı):
ΔH_exhaust = V²_çıkış / (2 × 1000)  [kJ/kg]

V_çıkış = ṁ × v_çıkış / A_çıkış  [m/s]

Tipik exhaust loss: 5-25 kJ/kg (kanat yüksekliğine bağlı)
```

### 5.2 Kondenser Performansı

```
Kondenser basıncı etkisi:
P_kond = P_doyma(T_soğutma_suyu + TTD + ΔT_soğutma)

Burada:
- T_soğutma_suyu = soğutma suyu giriş sıcaklığı [°C]
- TTD = Terminal Temperature Difference [3-8°C]
- ΔT_soğutma = soğutma suyu sıcaklık artışı [5-12°C]

Örnek:
T_soğutma = 20°C, TTD = 5°C, ΔT = 8°C
T_kond = 20 + 5 + 8 = 33°C → P_kond = 0.050 bar

Kondenser basıncının güce etkisi:
Her 10 mbar vakum iyileştirmesi ≈ %1-1.5 güç artışı

Kondenser ısı atımı:
Q̇_kond = ṁ × (h_çıkış - h_kondensat)  [kW]
(Bu ısı çevreye atılır, exergy kaybıdır)
```

## 6. Ara Çekişli Türbin Formülleri (Extraction Turbine)

### 6.1 Tek Çekiş Noktası

```
Çekişli türbin — tek çekiş noktası:
ṁ_giriş = ṁ_çekiş + ṁ_yoğuşma

HP kademe gücü:
Ẇ_HP = ṁ_giriş × (h_giriş - h_çekiş)  [kW]

LP kademe gücü:
Ẇ_LP = ṁ_yoğuşma × (h_çekiş - h_çıkış)  [kW]

Toplam güç:
Ẇ_toplam = Ẇ_HP + Ẇ_LP  [kW]

Proses ısısı:
Q̇_proses = ṁ_çekiş × (h_çekiş - h_kondensat)  [kW]

HPR (değişken):
HPR = Q̇_proses / Ẇ_elek

Çekiş oranı arttıkça:
→ Q̇_proses artar
→ Ẇ_LP azalır (ṁ_yoğuşma azalır)
→ HPR artar
→ Esneklik: HPR = 0 (tam yoğuşma) ile HPR = max (tam çekiş) arasında
```

### 6.2 Willans Çizgisi (Willans Line)

```
Türbin buhar tüketimi yaklaşımı:
ṁ = a + b × Ẇ  [kg/s]

Burada:
- a = boş çalışma (no-load) buhar tüketimi [kg/s]
- b = yük katsayısı [kg/(s·kW)]

Willans çizgisi parametreleri:
a = 0.10 × ṁ_nominal  (tipik)
b = (ṁ_nominal - a) / Ẇ_nominal

Kullanım:
Kısmi yükte buhar tüketimi hızlı tahmin için.
Doğrusal yaklaşım, %30-100 yük aralığında geçerli.
```

## 7. CHP Formülleri (Combined Heat and Power)

### 7.1 Birincil Enerji Tasarrufu (Primary Energy Savings — PES)

```
PES = 1 - 1 / (η_elek,CHP/η_elek,ref + η_ısı,CHP/η_ısı,ref)

EU 2012/27/EU Directive referans verimleri:
- η_elek,ref = %52.5 (doğalgaz, kombine çevrim — harmonize değer)
  Buhar türbini CHP için: η_elek,ref = %44.2 (katı yakıt)
- η_ısı,ref = %90 (buhar), %92 (sıcak su)

Yüksek verimli CHP tanımı: PES > %10

Örnek: Buhar türbini CHP
η_elek,CHP = %20, η_ısı,CHP = %65
PES = 1 - 1 / (0.20/0.442 + 0.65/0.90)
    = 1 - 1 / (0.452 + 0.722)
    = 1 - 1 / 1.175 = 1 - 0.851 = %14.9 → Yüksek verimli CHP ✓
```

### 7.2 Isı/Güç Oranı (Power-to-Heat Ratio — PHR)

```
PHR = Ẇ_elek / Q̇_ısı  (1/HPR)

Buhar türbini CHP PHR değerleri:
- Karşı basınçlı (düşük basınç): PHR = 0.10-0.20
- Karşı basınçlı (orta basınç): PHR = 0.15-0.30
- Çekişli: PHR = 0.15-0.40 (değişken)

Gaz türbini CHP:
- PHR = 0.40-0.67

Gaz motoru CHP:
- PHR = 0.67-1.25
```

### 7.3 Eşdeğer Elektrik Verimi (Equivalent Electric Efficiency)

```
Eşdeğer elektrik verimi (tüm çıktıyı elektrik olarak değerlendirme):
η_elek,eşdeğer = Ẇ_elek / (Q̇_yakıt - Q̇_ısı / η_kazan_ref)

Burada:
- Q̇_yakıt = CHP yakıt girişi [kW]
- Q̇_ısı = CHP ısı çıkışı [kW]
- η_kazan_ref = referans kazan verimi [0.90]

Bu formül, CHP'nin elektrik üretim performansını ayrı
bir elektrik santrali ile karşılaştırmaya olanak verir.

Örnek:
Q̇_yakıt = 10,000 kW, Ẇ_elek = 2,000 kW, Q̇_ısı = 6,500 kW
η_elek,eşdeğer = 2,000 / (10,000 - 6,500/0.90)
               = 2,000 / (10,000 - 7,222) = 2,000 / 2,778 = %72.0
```

## 8. Çok Kademeli Türbin Hesaplamaları (Multi-Stage Calculations)

### 8.1 Kademe Verimi (Stage Efficiency)

```
Herbir kademe (stage) için:
η_is,kademe = (h_in,kademe - h_out,kademe) / (h_in,kademe - h_out,is,kademe)

Toplam türbin verimi, kademe verimlerinin geometrik ortalamasına yakındır:

η_is,toplam ≈ 1 - (1 - η_is,kademe)^n × düzeltme_faktörü

Burada n = kademe sayısı.

Pratik yaklaşım (Parsons tipi türbin):
η_is,toplam ≈ η_is,kademe + 0.02 × (n - 1)  (yaklaşık, n<10)

Kural: Daha fazla kademe = daha yüksek toplam verim
(ama artan maliyet ve karmaşıklık)
```

### 8.2 Reheat (Tekrar Kızdırma) Etkisi

```
Reheat ile çıkış neminin azaltılması:

Reheatsız:
h_çıkış = h_giriş - η_is × (h_giriş - h_çıkış,is)
x_çıkış = kontrol et

Reheatli:
HP türbin: h_giriş → h_HP_çıkış (orta basınç)
Reheat: h_HP_çıkış → h_reheat (tekrar kızdırma)
LP türbin: h_reheat → h_LP_çıkış

Reheat avantajı:
- %2-4 izentropik verim artışı
- Son kademe nemi azalır → kanat erozyonu azalır
- Net çıkış gücü artar

Reheat exergy etkisi:
ΔĖx_reheat = ṁ × [(h_reheat - h_HP_çıkış) - T₀ × (s_reheat - s_HP_çıkış)]
```

## 9. Isı Hızı ve Verim İlişkileri (Heat Rate Relations)

### 9.1 Isı Hızı (Heat Rate — HR)

```
Brüt ısı hızı:
HR_brüt = Q̇_yakıt / Ẇ_brüt  [kJ/kWh]

Net ısı hızı:
HR_net = Q̇_yakıt / Ẇ_net  [kJ/kWh]
Ẇ_net = Ẇ_brüt - Ẇ_yardımcı  [kW]

Verim-Isı hızı ilişkisi:
η = 3,600 / HR  [%] (HR kJ/kWh cinsinden)

Tipik heat rate değerleri:
- Yoğuşmalı türbin (iyi): HR = 8,000-10,000 kJ/kWh (η = %36-45)
- Karşı basınçlı CHP: HR = 12,000-20,000 kJ/kWh (yalnızca elektrik bazında)
- Kombine çevrim: HR = 5,800-6,300 kJ/kWh (η = %57-62)

Isı hızı sapma düzeltmeleri:
HR_düzeltilmiş = HR_test × K_P × K_T × K_v × K_kondensat

Burada:
K_P = giriş basıncı düzeltme faktörü
K_T = giriş sıcaklığı düzeltme faktörü
K_v = vakum düzeltme faktörü
K_kondensat = kondenser temizlik faktörü
```

### 9.2 Bozunma Analizi (Degradation Analysis)

```
Türbin performans bozunması (aging degradation):

Yıllık verim bozunması (tipik):
- İlk 5 yıl: %0.2-0.5/yıl
- 5-15 yıl: %0.3-0.8/yıl
- 15+ yıl: %0.5-1.0/yıl (overhaul öncesi)

Bozunma sonrası heat rate:
HR_bozunmuş = HR_yeni × (1 + bozunma_oranı)^t

Bozunma kaynakları:
1. Kanat aşınması (erosion/corrosion): %1-3 toplam
2. Sızdırmazlık aşınması (seal wear): %0.5-2 toplam
3. Kanat ucu boşluğu artışı (tip clearance): %0.5-1.5 toplam
4. Fouling/birikinti: %0.5-1 toplam

Major overhaul sonrası verim iyileşmesi:
%2-5 heat rate iyileşmesi (30-50K saatte bir overhaul)
```

## 10. ORC (Organic Rankine Cycle) Hesaplamaları

### 10.1 ORC Temel Formülleri

```
ORC — düşük sıcaklık kaynakları için:

Termal verim:
η_th,ORC = Ẇ_net / Q̇_giriş  [%]

Net güç:
Ẇ_net = Ẇ_türbin - Ẇ_pompa  [kW]

ORC exergy verimi:
η_ex,ORC = Ẇ_net / Ėx_ısı_kaynağı  [%]

Ėx_ısı_kaynağı = Q̇_kaynak × (1 - T₀/T_kaynak)  [kW]

Tipik ORC performansı:
| Kaynak sıcaklığı [°C] | η_th [%] | η_ex [%] |
|------------------------|----------|----------|
| 80-120 | 5-10 | 25-45 |
| 120-200 | 10-18 | 35-55 |
| 200-350 | 15-25 | 40-60 |

ORC akışkan seçimi:
- R245fa: 80-150°C (en yaygın)
- Siloksan (MDM): 200-350°C
- n-Pentan: 100-200°C
- R1233zd(E): 80-180°C (düşük GWP alternatif)
```

## 11. Türbin Boyutlandırma Formülleri (Sizing)

### 11.1 Buhar Debisi Tahmini

```
PRV (Pressure Reducing Valve) yerine türbin:

Mevcut PRV akışı:
ṁ_PRV = Q̇_proses / (h_LP - h_kondensat)  [kg/s]

Türbin güç potansiyeli:
Ẇ_potansiyel = ṁ_PRV × (h_HP - h_LP) × η_is × η_mek × η_jen  [kW]

Yıllık enerji üretimi:
E_yıllık = Ẇ_potansiyel × t_çalışma  [kWh/yıl]

Ekonomik tasarruf:
C_tasarruf = E_yıllık × c_elektrik  [EUR/yıl]
```

### 11.2 Hacimsel Akış ve Boyut

```
Çıkış hacimsel akış (sizing parametresi):
V̇_çıkış = ṁ × v_çıkış  [m³/s]

Burada:
v_çıkış = spesifik hacim @ çıkış koşulları [m³/kg]

Son kademe kanat yüksekliği:
L_kanat ∝ √V̇_çıkış

Yoğuşmalı türbinlerde V̇_çıkış çok büyük:
- 0.05 bar'da v ≈ 28 m³/kg
- 4 bar'da v ≈ 0.46 m³/kg
→ Yoğuşmalı türbin son kademesi büyük kanat yüksekliği gerektirir
```

## 12. Birimler ve Dönüşümler

```
Güç: 1 MW = 1,000 kW
Buhar debisi: 1 ton/h = 0.2778 kg/s
Basınç: 1 bar = 100 kPa = 14.504 psi
Sıcaklık: T[K] = T[°C] + 273.15
Enerji: 1 kWh = 3,600 kJ
Isı hızı: 1 BTU/kWh = 1.055 kJ/kWh
```

## İlgili Dosyalar

- [Benchmarklar](benchmarks.md) — Türbin verimlilik karşılaştırma verileri
- [Denetim](audit.md) — Performans testi metodolojisi
- [Karşı Basınçlı Türbin](equipment/back_pressure.md) — Detaylı BP türbin bilgisi
- [Yoğuşmalı Türbin](equipment/condensing.md) — Detaylı yoğuşmalı türbin bilgisi
- [Çekişli Türbin](equipment/extraction.md) — Ara çekişli türbin bilgisi
- [ORC](equipment/orc.md) — Organic Rankine Cycle detayları
- [CHP Sistemleri](systems/steam_turbine_chp.md) — Buhar türbini CHP konfigürasyonları
- [Kazan Formülleri](../boiler/formulas.md) — Kazan verimlilik hesaplamaları
- [Kojenerasyon](../factory/cogeneration.md) — CHP temelleri ve karşılaştırma

## Referanslar

- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Horlock, J.H. (1966). *Axial Flow Turbines*, Butterworths.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Edition, Wiley.
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- API 612 (2005). *Petroleum, Petrochemical and Natural Gas Industries — Steam Turbines — Special-Purpose Applications*, API.
- Baumann, K. (1921). "Some recent developments in large steam turbine practice," *Journal of the Institution of Electrical Engineers*, 59(302), pp. 565-623.
- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration"
- Moran, M.J. et al. (2018). *Fundamentals of Engineering Thermodynamics*, 9th Edition, Wiley.
