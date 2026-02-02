---
title: "Motor CHP Sistemleri — Reciprocating Engine CHP"
category: systems
equipment_type: steam_turbine
keywords: [motor CHP, reciprocating engine, Otto çevrim, Diesel çevrim, ısı geri kazanım, jacket water, egzoz, biyogaz, exergy, kojenerasyon]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/systems/gas_turbine_chp.md, steam_turbine/systems/trigeneration.md, factory/cogeneration.md, boiler/equipment/waste_heat.md]
use_when: ["Motor CHP analizi yapılırken", "Isı geri kazanım katmanları değerlendirilirken", "Motor CHP exergy analizi yapılırken", "Biyogaz CHP değerlendirilirken", "Kısmi yük performansı karşılaştırılırken"]
priority: medium
last_updated: 2026-01-31
---
# Motor CHP Sistemleri — Reciprocating Engine CHP

> Son güncelleme: 2026-01-31

## Genel Bakış

Motor CHP (Reciprocating Engine CHP) sistemleri, pistonlu içten yanmalı motorların (otto veya diesel çevrim) mekanik enerjisinden elektrik üretirken, motorun birden fazla ısı reddediş noktasından termal enerji geri kazanımı yapan kojenerasyon tesisleridir. Buhar türbini veya gaz türbini CHP'ye göre daha yüksek elektrik verimi (%35-45) ve daha düşük HPR (0.8-1.5) sunarak elektrik ağırlıklı uygulamalarda avantaj sağlar. Bu dosya, motor CHP'yi buhar türbini bilgi tabanı perspektifinden, karşılaştırmalı olarak ele alır.

**Temel Fark:** Motor CHP'nin exergy verimi (%40-52), buhar türbini CHP'den (%25-38) belirgin şekilde yüksektir. Bunun nedeni, motorun yüksek elektrik verimi ve elektriğin saf exergy olmasıdır.

## 1. Çevrim Temelleri (Cycle Fundamentals)

### 1.1 Otto Çevrimi (Spark Ignition)

```
Otto çevrimi — kıvılcım ateşlemeli motor:
- Yakıt: Doğalgaz, biyogaz, LPG
- Sıkıştırma oranı: 10-14:1
- Çalışma prensibi: Sabit hacimde ısı ekleme (ideal)
- Devir: 1,000-1,800 RPM (büyük endüstriyel)
- Güç aralığı: 0.1-10 MW (tek motor)

Termal verim (ideal Otto çevrimi):
η_Otto = 1 - 1 / r^(γ-1)
r = sıkıştırma oranı, γ = 1.35 (doğalgaz karışımı)

Gerçek verim: %35-42 (mekanik + termal kayıplar)

Doğalgaz motor tipleri:
- Lean-burn (yalın karışım): λ = 1.5-2.0, düşük NOx, %38-42 verim
- Rich-burn (zengin karışım): λ = 1.0-1.1, 3-way katalitik, %34-38 verim
  λ = hava fazlalık katsayısı (excess air ratio)
```

### 1.2 Diesel Çevrimi (Compression Ignition)

```
Diesel çevrimi — sıkıştırma ateşlemeli motor:
- Yakıt: Dizel, HFO, biyodizel, dual-fuel (gaz + pilot dizel)
- Sıkıştırma oranı: 14-24:1
- Çalışma prensibi: Sabit basınçta ısı ekleme (ideal)
- Devir: 500-1,000 RPM (orta hızlı), 100-300 RPM (düşük hızlı)
- Güç aralığı: 0.5-80+ MW (tek motor)

Termal verim (ideal Diesel çevrimi):
η_Diesel = 1 - [1 / (r^(γ-1))] × [(r_c^γ - 1) / (γ × (r_c - 1))]
r_c = cut-off oranı (yakıt enjeksiyon süresi)

Gerçek verim: %38-48 (büyük düşük hızlı motorlar en yüksek)

Dual-fuel motorlar:
- %95-98 doğalgaz + %2-5 pilot dizel
- Doğalgaz modu verimi: %42-48
- Dizel modu verimi: %45-50
- Uygulama: Büyük endüstriyel ve denizcilik
```

## 2. Isı Geri Kazanım Katmanları (Heat Recovery Layers)

### 2.1 Motor Isı Dağılımı

```
Doğalgaz motor ısı dengesi (tipik 1 MW_e lean-burn):
Yakıt girişi:         2,500 kW (%100)
├── Elektrik çıkışı:  1,000 kW (%40.0)
├── Egzoz ısısı:        625 kW (%25.0)  → T = 350-500°C
├── Jacket water ısısı: 475 kW (%19.0)  → T = 80-95°C
├── Yağ soğutucu:       100 kW  (%4.0)  → T = 70-80°C
├── Şarj havası (intercooler): 125 kW  (%5.0) → T = 40-60°C
├── Radyasyon kaybı:    100 kW  (%4.0)
└── Diğer kayıplar:      75 kW  (%3.0)

Toplam geri kazanılabilir ısı: 1,325 kW (%53)
Pratik geri kazanım: 1,000-1,200 kW (%40-48)
→ HPR = 1.0-1.2
```

### 2.2 Isı Geri Kazanım Katmanları Detay

| Katman | Sıcaklık Aralığı [°C] | Kapasite [%yakıt] | Geri Kazanım Şekli | Exergy İçeriği |
|--------|------------------------|--------------------|--------------------|----------------|
| Egzoz gazı | 350-500 giriş, 120-180 çıkış | %15-22 | Egzoz ısı değiştiricisi → buhar veya sıcak su | Yüksek |
| Jacket water (gömlek suyu) | 80-95 | %15-22 | Plakalı ısı değiştirici → sıcak su 70-85°C | Düşük |
| Yağ soğutucu (lube oil) | 70-80 | %3-5 | Plakalı ısı değiştirici → sıcak su 60-70°C | Çok düşük |
| Şarj havası (charge air) | 40-60 | %4-6 | İntercooler → ılık su 35-50°C | Çok düşük |

### 2.3 Katmanlı Isı Geri Kazanım Stratejisi

```
Yüksek kaliteli ısı (high-grade heat):
Egzoz gazı → buhar üretimi veya yüksek sıcaklık sıcak su
- 350-500°C egzoz → 180-250°C buhar (5-15 bar) üretilebilir
- Veya 350-500°C egzoz → 90-110°C sıcak su (yüksek debi)
- Exergy Carnot faktörü: (1 - 298/623) = 0.52 (350°C'de)

Orta kaliteli ısı (medium-grade heat):
Jacket water → sıcak su kaynağı
- 80-95°C motor çıkışı → 70-85°C sıcak su üretimi
- Kapasite: 300-500 kW / MW_e (büyük potansiyel)
- Exergy Carnot faktörü: (1 - 298/358) = 0.17 (85°C'de)
- Uygulama: Bina ısıtma, proses ön ısıtma, absorpsiyon chiller

Düşük kaliteli ısı (low-grade heat):
Yağ soğutucu + şarj havası → düşük sıcaklık sıcak su
- 40-80°C → 35-65°C sıcak su
- Exergy Carnot faktörü: (1 - 298/338) = 0.12 (65°C'de)
- Uygulama: Kullanım suyu ön ısıtma, sera ısıtma

Bütünleşik geri kazanım sıralaması (cascade):
Egzoz → buhar/yüksek T → jacket water → sıcak su → yağ/şarj → ön ısıtma
```

## 3. Buhar Üretimi Potansiyeli

### 3.1 Egzozdan Buhar Üretimi

```
Egzoz gazından buhar üretimi hesabı:

Egzoz koşulları (tipik 1 MW_e doğalgaz motor):
- ṁ_egzoz = 1.8-2.5 kg/s
- T_egzoz = 400-480°C
- c_p = 1.06-1.10 kJ/(kg·K)

Buhar üretimi (10 bar doymuş buhar):
ṁ_buhar = ṁ_egzoz × c_p × (T_egzoz - T_baca) / (h_buhar - h_feedwater)

Örnek:
ṁ_buhar = 2.0 × 1.08 × (450 - 150) / (2,778 - 420)
        = 2.0 × 1.08 × 300 / 2,358
        = 648 / 2,358 = 0.275 kg/s = 0.99 ton/h

Buhar/elektrik oranı: ~1.0 ton buhar / MW_e
(Gaz türbininde bu oran 5-8 ton/MW_e)

Sonuç: Motor CHP'den buhar üretimi sınırlıdır.
Proses buhar talebi yüksekse gaz türbini veya buhar türbini tercih edilir.
```

### 3.2 Motor CHP vs Buhar Türbini CHP Buhar Karşılaştırma

| Parametre | Motor CHP (1 MW_e) | BT CHP (1 MW_e) |
|-----------|---------------------|------------------|
| Yakıt girişi [kW] | 2,500 | 4,500 |
| Elektrik [kW] | 1,000 | 1,000 |
| Proses buhar [ton/h] | 0.8-1.2 (egzozdan) | 8-15 (türbin çıkışından) |
| Sıcak su [kW] | 600-800 (jacket + yağ) | -- |
| HPR | 0.8-1.2 | 4-8 |
| η_enerji [%] | 80-88 | 82-92 |
| η_exergy [%] | 42-50 | 26-34 |
| Buhar basıncı [bar] | 5-12 (sınırlı) | 2-15 (esnek) |

## 4. Kısmi Yük Performansı (Part-Load Performance)

### 4.1 Kısmi Yük Verim Tablosu

```
Motor CHP kısmi yük performansı:

| Yük [%] | η_elek/η_nominal | η_ısı/η_nominal | HPR Değişimi |
|---------|------------------|-----------------|--------------|
| 100     | 1.00             | 1.00            | Referans     |
| 90      | 0.99             | 1.01            | +%2          |
| 80      | 0.97             | 1.02            | +%5          |
| 70      | 0.94             | 1.04            | +%10         |
| 60      | 0.90             | 1.05            | +%15         |
| 50      | 0.85             | 1.06            | +%22         |
| 40      | 0.78             | 1.07            | +%30         |
| 30      | 0.70             | 1.08            | +%42         |

Motor CHP'nin kısmi yük avantajı:
- %50 yükte elektrik verimi %85 korunur (GT: %75-80, BT: %85-88)
- Minimum çalışma yükü: %30-40 (GT: %40-50, BT: %30-40)
- Çoklu motor konfigürasyonu ile verim daha da korunur
```

### 4.2 Çoklu Motor Stratejisi

```
Çoklu motor konfigürasyonu:
Tek büyük motor yerine birden fazla küçük motor kullanımı

Örnek: 4 MW_e CHP
Seçenek A: 1 × 4 MW motor
Seçenek B: 2 × 2 MW motor
Seçenek C: 4 × 1 MW motor

%50 yükte (2 MW_e gerekli):
A: 1 motor × %50 yük → η_elek = %85 nominal
B: 1 motor × %100 yük → η_elek = %100 nominal
C: 2 motor × %100 yük → η_elek = %100 nominal

Avantaj: Çoklu motor ile kısmi yükte tam verim korunur
Dezavantaj: Daha yüksek yatırım, daha fazla bakım noktası

Modüler yaklaşım:
- Yük artışında ek motor devreye alınır
- N+1 yedeklilik sağlanabilir
- Bakım sırasında kapasite korunur
```

## 5. Biyogaz Uygulamaları

### 5.1 Biyogaz Motor CHP

```
Biyogaz özellikleri:
- CH₄ içeriği: %50-70 (kaynağa bağlı)
- CO₂ içeriği: %30-45
- H₂S: 100-10,000 ppm (arıtma gerekli)
- Alt ısıl değer: 18-25 MJ/Nm³ (doğalgaz 36 MJ/Nm³)
- Nem: Doymuş (%100 RH)

Biyogaz kaynakları:
1. Biyolojik atık su arıtma (WWTP): %60-65 CH₄
2. Organik atık fermantasyonu: %55-65 CH₄
3. Çöp depo gazı (landfill gas): %45-55 CH₄
4. Tarımsal biyogaz: %50-60 CH₄

Biyogaz motor CHP performansı:
- Elektrik verimi: %32-40 (doğalgaza göre %3-5 düşük)
- Toplam verim: %75-85
- Derating faktörü: %5-15 (düşük ısıl değer nedeniyle)
- Motor ömrü: %10-20 kısa (H₂S korozyonu)

Biyogaz CHP exergy verimi:
η_exergy = %35-45 (doğalgaz CHP: %40-52)
Fark nedeni: Biyogaz kimyasal exergisi düşük + motor verimi düşük
```

### 5.2 Biyogaz Arıtma Gereksinimleri

| Parametre | Sınır Değer | Arıtma Yöntemi | Maliyet Etkisi |
|-----------|-------------|----------------|----------------|
| H₂S | <200 ppm | Aktif karbon, biyolojik desülfürizasyon | Düşük-orta |
| Nem | <80% RH | Soğutma/kurutma | Düşük |
| Siloksan | <10 mg/Nm³ | Aktif karbon adsorbsiyon | Orta |
| Partiküler | <10 mg/Nm³ | Filtrasyon | Düşük |

## 6. Motor CHP Exergy Analizi Detay

### 6.1 Exergy Dağılımı

```
Doğalgaz motor CHP exergy dağılımı (1 MW_e):
Yakıt exergisi (doğalgaz φ=1.04):     2,600 kW (%100)
├── Elektrik çıkışı (saf exergy):     1,000 kW (%38.5)
├── Yanma tersinmezliği:                520 kW (%20.0)
│   └── Motor silindirinde yüksek T yanma
├── Motor iç kayıpları:                 260 kW (%10.0)
│   └── Sürtünme, pompalama, ısı transferi
├── Egzoz exergisi (geri kazanılabilir): 325 kW (%12.5)
│   └── T = 450°C → Carnot = 0.52
├── Jacket water exergisi:               81 kW  (%3.1)
│   └── T = 85°C → Carnot = 0.17
├── Yağ/şarj hava exergisi:              26 kW  (%1.0)
│   └── T = 60°C → Carnot = 0.11
├── Egzoz geri kazanım kaybı:           130 kW  (%5.0)
│   └── Baca gazı 150°C'de çıkış
├── Radyasyon/konveksiyon kaybı:        104 kW  (%4.0)
└── Diğer kayıplar:                     154 kW  (%5.9)

Faydalı exergy çıkışı:
Elektrik: 1,000 kW + Egzoz exergy: 200 kW + JW exergy: 60 kW
= 1,260 kW → η_exergy = %48.5

Karşılaştırma:
Motor CHP η_exergy ≈ %48 vs BT CHP η_exergy ≈ %30
Motor CHP η_enerji ≈ %85 vs BT CHP η_enerji ≈ %87
→ Exergy perspektifinden motor CHP üstün, enerji perspektifinden benzer
```

### 6.2 Isı Geri Kazanım Katmanlarının Exergy Katkısı

| Katman | Q [kW] | T_ortalama [°C] | Carnot Faktörü | Ex [kW] | Exergy/Enerji [%] |
|--------|--------|-----------------|----------------|---------|-------------------|
| Egzoz (buhar) | 500 | 300 | 0.48 | 240 | %48 |
| Egzoz (sıcak su) | 500 | 200 | 0.37 | 185 | %37 |
| Jacket water | 475 | 85 | 0.17 | 81 | %17 |
| Yağ soğutucu | 100 | 75 | 0.14 | 14 | %14 |
| Şarj havası | 125 | 50 | 0.08 | 10 | %8 |

```
Sonuç: Egzoz ısısının exergy kalitesi jacket water'ın 3 katı.
Egzozdan buhar üretimi exergy açısından tercih edilmeli.
Jacket water ısısı yüksek hacimli ama düşük kaliteli.
```

## 7. Türk Endüstrisinde Motor CHP Uygulamaları

### 7.1 Tipik Uygulama Alanları

| Sektör | Güç [MW_e] | Yakıt | HPR | Isı Kullanımı | Yıllık Çalışma [saat] |
|--------|-----------|-------|-----|---------------|----------------------|
| Sera ısıtma | 0.5-5 | Doğalgaz | 1.0-1.5 | Sıcak su 60-80°C | 6,000-7,500 |
| Hastane/otel | 0.2-2 | Doğalgaz | 0.8-1.2 | Sıcak su + buhar | 6,000-8,000 |
| Gıda | 0.5-5 | Doğalgaz | 1.0-1.5 | Sıcak su + buhar | 5,000-7,000 |
| Atık su arıtma | 0.2-5 | Biyogaz | 0.8-1.2 | Çürütücü ısıtma | 7,500-8,500 |
| Çöp depo | 0.5-10 | LFG | 0.6-1.0 | Sınırlı | 7,000-8,000 |
| Tekstil | 1-10 | Doğalgaz | 1.0-1.5 | Sıcak su + buhar | 5,500-7,500 |

## İlgili Dosyalar

- [Formüller](../formulas.md) -- CHP exergy hesaplama formülleri
- [Benchmarklar](../benchmarks.md) -- Karşılaştırmalı prime mover tablosu
- [Buhar Türbini CHP](steam_turbine_chp.md) -- BT CHP konfigürasyonları
- [Gaz Türbini CHP](gas_turbine_chp.md) -- GT + HRSG CHP
- [Trijenerasyon](trigeneration.md) -- CCHP konfigürasyonları (motor ile trijenerasyon)
- [HRSG](hrsg.md) -- HRSG türbin perspektifi
- [Kojenerasyon Temelleri](../../factory/cogeneration.md) -- Sistem seviyesi CHP
- [Atık Isı Kazanı](../../boiler/equipment/waste_heat.md) -- Egzoz ısı geri kazanım kazanı
- [Absorpsiyon Chiller](../../chiller/equipment/absorption.md) -- Motor CHP + absorpsiyon soğutma
- [Yük Eşleştirme](../solutions/load_matching.md) -- Termal/elektrik yük eşleştirme
- [Fizibilite](../economics/feasibility.md) -- CHP fizibilite analizi

## Referanslar

- Heywood, J.B. (2018). *Internal Combustion Engine Fundamentals*, 2nd Edition, McGraw-Hill.
- US DOE (2016). *CHP Technology Fact Sheet Series -- Reciprocating Engines*, DOE.
- Horlock, J.H. (1997). *Cogeneration -- Combined Heat and Power (CHP): Thermodynamics and Economics*, Pergamon Press.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- IEA Bioenergy (2020). *Biogas in the Energy Sector*, Task 37.
- ASUE (2011). *BHKW-Kenndaten*, Arbeitsgemeinschaft fur sparsamen und umweltfreundlichen Energieverbrauch.
- EU Directive 2012/27/EU, "Energy Efficiency Directive -- High Efficiency Cogeneration."
- Tsatsaronis, G. & Morosuk, T. (2012). "Advanced exergy-based methods," *Energy*.
