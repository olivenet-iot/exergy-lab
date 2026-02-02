---
title: "Gaz Türbini CHP ve Kombine Çevrim — Gas Turbine CHP and Combined Cycle"
category: systems
equipment_type: steam_turbine
keywords: [gaz türbini, CHP, HRSG, kombine çevrim, CCGT, Brayton, supplementary firing, aero-derivatif, heavy-duty, exergy]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/systems/hrsg.md, steam_turbine/systems/trigeneration.md, factory/cogeneration.md, boiler/equipment/waste_heat.md]
use_when: ["Gaz türbini CHP analizi yapılırken", "Kombine çevrim exergy değerlendirmesi yapılırken", "GT + HRSG konfigürasyonu seçilirken", "Supplementary firing etkisi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Gaz Türbini CHP ve Kombine Çevrim — Gas Turbine CHP and Combined Cycle

> Son güncelleme: 2026-01-31

## Genel Bakış

Gaz türbini CHP (Combined Heat and Power) sistemleri, Brayton çevrimiyle elektrik üreten bir gaz türbini ve egzoz gazından buhar üreten bir HRSG'den (Heat Recovery Steam Generator) oluşur. Buhar, ya doğrudan prosese verilebilir (simple cycle CHP) ya da bir buhar türbininden geçirilerek ek elektrik üretilebilir (combined cycle — CCGT). Bu dosya, buhar türbini perspektifinden GT CHP ve kombine çevrim sistemlerini ele alır. HRSG iç detayları icin `steam_turbine/systems/hrsg.md` ve `boiler/equipment/waste_heat.md` referanslarına bakınız.

**Temel Fark:** Gaz türbini CHP'de egzoz sıcaklığı 450-600°C olup yüksek exergy iceriklidir. Bu exergyyi etkin kullanmak, sistem veriminin anahtarıdır.

## 1. Brayton Çevrimi Temelleri (Brayton Cycle Fundamentals)

### 1.1 Basit Brayton Çevrimi

```
Brayton çevrimi bileşenleri:
1. Kompresör: Hava sıkıştırma (T₁ → T₂)
2. Yanma odası: Yakıt yakma (T₂ → T₃)
3. Türbin: Genişleme ve iş üretimi (T₃ → T₄)
4. Egzoz: Sıcak gaz çıkışı (T₄ = 450-600°C)

Tipik sıcaklıklar:
T₁ = 15°C (hava giriş)
T₂ = 350-450°C (kompresör çıkış)
T₃ = 1,100-1,500°C (türbin giriş — TIT)
T₄ = 450-600°C (egzoz)

Basınç oranı (pressure ratio):
r_p = P₂/P₁ = 10-35 (modern gaz türbinlerinde)

Brayton çevrimi verimi:
η_Brayton = 1 - 1 / r_p^((γ-1)/γ)
γ = 1.4 (hava için, ideal)

Gerçek verimler:
- Basit çevrim: %25-40 (elektrik)
- Egzoz enerjisi: %55-65 (yakıt enerjisinin)
```

### 1.2 Gaz Türbini Tipleri

| Parametre | Aero-Derivatif | Heavy-Duty (Endüstriyel) |
|-----------|----------------|--------------------------|
| Güç aralığı [MW] | 2-50 | 20-500+ |
| Basınç oranı | 20-35 | 10-23 |
| TIT [°C] | 1,200-1,400 | 1,100-1,600 |
| Egzoz sıcaklığı [°C] | 400-500 | 500-650 |
| Elektrik verimi [%] | 30-42 | 28-42 |
| Ağırlık [kg/MW] | 5-15 | 30-80 |
| Başlangıç süresi | 5-10 dakika | 15-30 dakika |
| Bakım aralığı [saat] | 12,000-25,000 | 25,000-50,000 |
| Kısmi yük performansı | Orta-iyi | Orta |
| Uygulama | Offshore, hızlı tepki | Baz yük, endüstriyel |

## 2. GT + HRSG CHP Konfigürasyonları

### 2.1 Simple Cycle CHP (GT + HRSG)

```
Akış şeması:
Hava + Yakıt → [Gaz Türbini] → Elektrik
                     ↓ Egzoz (450-600°C)
                  [HRSG] → Buhar → Proses
                     ↓
                Baca Gazı (80-180°C)

Tipik performans:
- GT elektrik verimi: %25-40
- HRSG buhar üretimi: egzoz enerjisinin %60-85'i
- Toplam enerji verimi: %70-85
- Toplam exergy verimi: %35-48
- HPR: 1.5-2.5

Buhar üretim hesabı:
ṁ_buhar = ṁ_egzoz × c_p,gaz × (T_egzoz,giriş - T_baca) / (h_buhar - h_feedwater)
         × η_HRSG

Burada:
- ṁ_egzoz = gaz türbini egzoz debisi [kg/s]
- c_p,gaz = egzoz gazı spesifik ısısı ≈ 1.05-1.10 kJ/(kg·K)
- T_baca = baca gazı sıcaklığı [°C] (asit çiğ noktası üstü: >80-120°C)
- η_HRSG = HRSG verimi [0.85-0.95]
```

### 2.2 Combined Cycle (CCGT)

```
Akış şeması:
Hava + Yakıt → [Gaz Türbini] → Elektrik (1)
                     ↓ Egzoz
                  [HRSG] → HP Buhar
                     ↓        ↓
                Baca Gazı   [Buhar Türbini] → Elektrik (2)
                               ↓
                           [Kondenser]

Tipik performans:
- GT elektrik verimi: %35-42
- ST elektrik verimi: %15-22 (egzoz enerjisi bazında)
- Toplam kombine çevrim verimi: %57-62 (modern F/H/J sınıfı)
- En iyi: %63-64 (J sınıfı, 1,600°C TIT)

Güç dağılımı (tipik):
- GT: %65-70 toplam gücün
- ST: %30-35 toplam gücün

Exergy dağılımı:
Yakıt exergisi: %100
├── GT elektrik: %35-42
├── ST elektrik: %15-22
├── Baca gazı exergy kaybı: %3-8
├── Kondenser exergy kaybı: %3-5
├── GT iç kayıpları: %15-20
├── Yanma tersinmezliği: %20-28
└── HRSG exergy yıkımı: %5-10
```

### 2.3 Combined Cycle CHP (CCGT + Proses Buhar)

```
Kombine çevrim CHP modları:

Mod 1: Back-pressure ST + proses buhar
GT → HRSG → BP Buhar Türbini → Proses Buhar
- η_enerji: %80-88
- η_exergy: %40-52
- HPR: 1.0-2.0

Mod 2: Extraction ST + proses buhar
GT → HRSG → Extraction Buhar Türbini → Çekiş → Proses
                                     → Kondenser
- η_enerji: %70-85
- η_exergy: %42-55
- HPR: 0.5-2.5 (ayarlanabilir)

Mod 3: HRSG direct steam + GT elektrik
GT → HRSG → Buhar doğrudan prosese (ST yok)
- η_enerji: %75-85
- η_exergy: %35-45
- HPR: 1.5-3.0
- En basit, en düşük yatırım
```

## 3. Supplementary Firing (Ek Yakma)

### 3.1 Ek Yakma Prensibi

```
Supplementary firing (duct burner):
- HRSG girişine ek yakıcı konularak egzoz sıcaklığı artırılır
- Egzoz gazında %15-17 O₂ bulunur → ek yanma mümkün
- Sıcaklık: 500-600°C → 800-1,000°C artırılabilir
- Buhar üretimi %50-100 artırılabilir

Ek yakma kapasitesi:
Q̇_ek = ṁ_egzoz × c_p × (T_ek_yakma_sonrası - T_egzoz)

Ek buhar üretimi:
Δṁ_buhar = Q̇_ek × η_HRSG / (h_buhar - h_feedwater)
```

### 3.2 Ek Yakmanın Exergy Etkisi

```
UYARI: Ek yakma exergy verimini DÜŞÜRÜR!

Neden?
Ek yakma, yanma tersinmezliği yaratır.
Direkt yakıt → ısı dönüşümü yüksek tersinmezlik içerir.
Kazan ile benzer exergy yıkımı oluşur.

Karşılaştırma:
GT basit çevrim (ek yakma yok):
- η_exergy = %38-45

GT + supplementary firing:
- η_exergy = %32-40 (düşer!)
- η_enerji = %78-88 (artar!)

Exergy perspektifinden değerlendirme:
- Ek yakmasız HRSG: egzoz exergisinin %70-85'i geri kazanılır
- Ek yakmalı HRSG: yakıt exergisinin %40-55'i geri kazanılır
- Fark: Yanma tersinmezliği → %25-35 exergy yıkımı

Ne zaman ek yakma kabul edilebilir?
1. Proses buhar talebi GT egzozundan karşılanamıyorsa
2. Mevsimsel pik talep dönemlerinde (kısa süreli)
3. Yedek kapasite gerektiğinde
4. Ekonomik değerlendirme exergy kaybını haklı kılıyorsa
```

### 3.3 Ek Yakma Kademeli Etki Tablosu

| Ek Yakma Oranı | Egzoz T [°C] | Buhar Artışı [%] | η_enerji [%] | η_exergy [%] | Exergy Yıkım Artışı |
|-----------------|-------------|-------------------|--------------|--------------|---------------------|
| Yok | 500-600 | Referans | 70-80 | 38-45 | Referans |
| Düşük (%10-20) | 650-700 | +20-35 | 75-83 | 36-42 | +%5-8 |
| Orta (%20-40) | 700-800 | +35-60 | 78-86 | 34-40 | +%10-15 |
| Yüksek (%40-60) | 800-1,000 | +60-100 | 80-88 | 32-38 | +%15-22 |

## 4. HRSG Basınç Seviyesi Seçimi

### 4.1 Tek/Çift/Üçlü Basınç HRSG

```
Tek basınçlı HRSG (single pressure):
- Basit, düşük yatırım
- Baca gazı sıcaklığı nispeten yüksek (150-200°C)
- Exergy verimi düşük: egzoz exergisinin %60-70'i kullanılır
- Uygulama: Küçük CHP (<25 MW_e), basit proses buhar

Çift basınçlı HRSG (dual pressure):
- HP + LP buhar üretimi
- Baca gazı sıcaklığı düşer (120-160°C)
- Exergy verimi orta: egzoz exergisinin %70-80'i kullanılır
- Ek %8-12 buhar türbini gücü (tek basınca göre)
- Uygulama: Orta ölçek CCGT (25-100 MW_e)

Üçlü basınçlı HRSG (triple pressure + reheat):
- HP + IP + LP buhar + reheat
- Baca gazı sıcaklığı minimum (80-120°C)
- Exergy verimi yüksek: egzoz exergisinin %80-90'ı kullanılır
- Ek %15-20 buhar türbini gücü (tek basınca göre)
- Uygulama: Büyük CCGT (>100 MW_e), F/H/J sınıfı GT

Ayrıntılı HRSG bilgisi: → systems/hrsg.md
```

### 4.2 HRSG Basınç Seçim Kriterleri

| Kriter | Tek Basınç | Çift Basınç | Üçlü Basınç |
|--------|-----------|-------------|-------------|
| GT boyutu [MW] | <25 | 25-100 | >100 |
| Yatırım maliyeti | Düşük | Orta (+%15-25) | Yüksek (+%30-50) |
| Verim artışı | Referans | +%3-5 puan | +%5-7 puan |
| Baca gazı sıcaklığı [°C] | 150-200 | 120-160 | 80-120 |
| Karmaşıklık | Basit | Orta | Yüksek |
| Başlangıç süresi | Hızlı | Orta | Yavaş |

## 5. Cogeneration vs Combined Cycle Modu

### 5.1 Mod Karşılaştırma

```
Cogeneration modu (CHP):
- Amaç: Elektrik + proses ısısı birlikte üretmek
- Buhar türbini çıkışı prosese (back-pressure veya extraction)
- HPR: 1.0-2.5
- η_enerji: %75-88
- η_exergy: %35-52
- Avantaj: Yüksek toplam verim, PES > %10
- Dezavantaj: Proses talebi elektriği sınırlar

Combined cycle modu (sadece elektrik):
- Amaç: Maksimum elektrik üretimi
- Buhar türbini çıkışı kondensere
- HPR: 0 (ısı satılmaz)
- η_enerji: %57-64 (sadece elektrik)
- η_exergy: %52-60
- Avantaj: Yüksek elektrik verimi
- Dezavantaj: Kondenser ısısı atılır

Karşılaştırma notu:
CHP modunda enerji verimi yüksek (%85) ama exergy verimi düşüktür (%45).
Combined cycle modunda enerji verimi düşük (%60) ama exergy verimi yüksektir (%55).
Exergy perspektifinden combined cycle daha verimlidir,
ancak toplam enerji kullanımı açısından CHP üstündür.
```

## 6. Exergy Dağılımı — GT CHP Detay

### 6.1 Basit Çevrim GT CHP Exergy Akışı

```
Yakıt exergisi (doğalgaz φ=1.04):              100 MW (%100)
├── Yanma tersinmezliği:                         28 MW (%28)
│   └── Yüksek T yanma → düşük T egzoz dönüşümü
├── GT kompresör-türbin kayıpları:                5 MW  (%5)
├── GT net elektrik çıkışı:                      35 MW (%35)
├── HRSG exergy yıkımı:                           6 MW  (%6)
│   └── Büyük ΔT ısı transferi (500°C → 200°C buhar)
├── Proses buhar exergisi (faydalı):             12 MW (%12)
├── Baca gazı exergy kaybı:                       5 MW  (%5)
└── Diğer kayıplar (mekanik, jeneratör, boru):    9 MW  (%9)

η_ex,CHP = (35 + 12) / 100 = %47

Ana exergy yıkım noktaları:
1. Yanma odası: %28 (en büyük kaynak — kaçınılmaz)
2. HRSG ısı transferi: %6 (ΔT azaltılarak iyileştirilebilir)
3. GT iç kayıpları: %5 (türbin/kompresör verimi)
```

### 6.2 Kombine Çevrim Exergy Akışı

```
Yakıt exergisi:                                 100 MW (%100)
├── Yanma tersinmezliği:                         27 MW (%27)
├── GT iç kayıpları:                              5 MW  (%5)
├── GT net elektrik:                              38 MW (%38)
├── HRSG exergy yıkımı:                           4 MW  (%4)
├── ST elektrik:                                  21 MW (%21)
├── Kondenser exergy kaybı:                        2 MW  (%2)
└── Diğer kayıplar:                                3 MW  (%3)

η_ex,CC = (38 + 21) / 100 = %59

Kombine çevrim CHP (extraction ST):
η_ex,CC_CHP = (38 + 15 + 8_proses) / 100 = %61
```

## 7. Aero-Derivatif vs Heavy-Duty CHP Seçimi

### 7.1 Seçim Matrisi

| Kriter | Aero-Derivatif | Heavy-Duty |
|--------|----------------|------------|
| Hızlı başlangıç gerekli | Evet (5-10 dk) | Hayır (15-30 dk) |
| Kısmi yük sık | Evet (iyi performans) | Hayır (verim düşüşü fazla) |
| Baz yük sürekli çalışma | Hayır | Evet (en uygun) |
| Alan kısıtı var | Evet (kompakt) | Hayır (geniş alan) |
| Bakım kolaylığı | Modüler değişim | Yerinde bakım |
| Yakıt fiyatı düşük | Her ikisi | Heavy-duty daha avantajlı |
| Güç ihtiyacı >50 MW | Hayır | Evet |

## İlgili Dosyalar

- [Formüller](../formulas.md) -- Buhar türbini exergy hesaplama formülleri
- [Benchmarklar](../benchmarks.md) -- Karşılaştırmalı prime mover tablosu
- [HRSG](hrsg.md) -- HRSG tasarım, pinch point, eşleştirme detayları
- [Buhar Türbini CHP](steam_turbine_chp.md) -- BT CHP konfigürasyonları
- [Motor CHP](engine_chp.md) -- Motor CHP karşılaştırma
- [Trijenerasyon](trigeneration.md) -- CCHP konfigürasyonları
- [Kojenerasyon Temelleri](../../factory/cogeneration.md) -- Sistem seviyesi CHP
- [Atık Isı Kazanı](../../boiler/equipment/waste_heat.md) -- HRSG iç detayları
- [Verim İyileştirme](../solutions/efficiency_improvement.md) -- Türbin verim iyileştirme
- [Fizibilite](../economics/feasibility.md) -- CHP fizibilite analizi

## Referanslar

- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Horlock, J.H. (1997). *Cogeneration -- Combined Heat and Power (CHP): Thermodynamics and Economics*, Pergamon Press.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Boyce, M.P. (2012). *Gas Turbine Engineering Handbook*, 4th Edition, Butterworth-Heinemann.
- Kehlhofer, R. et al. (2009). *Combined-Cycle Gas & Steam Turbine Power Plants*, 3rd Edition, PennWell.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- ASME PTC 22 (2014). *Gas Turbines Performance Test Codes*, ASME.
- US DOE (2016). *Combined Heat and Power Technology Fact Sheet Series -- Gas Turbines*, DOE.
- Tsatsaronis, G. & Morosuk, T. (2012). "Advanced exergy-based methods used to understand and improve energy-conversion systems," *Energy*.
- EU Directive 2012/27/EU, "Energy Efficiency Directive -- High Efficiency Cogeneration."
