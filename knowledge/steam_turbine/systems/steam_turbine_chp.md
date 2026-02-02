---
title: "Buhar Türbini CHP Konfigürasyonları — Steam Turbine CHP Configurations"
category: systems
equipment_type: steam_turbine
keywords: [buhar türbini, CHP, kojenerasyon, karşı basınçlı, çekişli, condensing-extraction, HPR, exergy, back-pressure, extraction]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/extraction.md, steam_turbine/equipment/condensing.md, steam_turbine/systems/gas_turbine_chp.md, steam_turbine/systems/trigeneration.md, factory/cogeneration.md, boiler/formulas.md]
use_when: ["Buhar türbini CHP konfigürasyonu seçilirken", "CHP exergy analizi yapılırken", "Türbin tipi ve exhaust koşulu optimize edilirken", "HPR ve yük profili değerlendirilirken"]
priority: high
last_updated: 2026-01-31
---
# Buhar Türbini CHP Konfigürasyonları — Steam Turbine CHP Configurations

> Son güncelleme: 2026-01-31

## Genel Bakış

Buhar türbini CHP (Combined Heat and Power) sistemleri, yüksek basınçlı buhardan hem elektrik hem de proses ısısı üreten endüstriyel kojenerasyon tesislerinin temelini oluşturur. Bu dosya, üç ana türbin CHP konfigürasyonunu **türbin perspektifinden** ele alır: karşı basınçlı CHP, çekişli CHP ve condensing-extraction CHP. Sistem seviyesi CHP temelleri için `factory/cogeneration.md` referansına bakınız.

**Temel Fark:** Enerji verimi (%80-92) ile exergy verimi (%25-42) arasındaki uçurum, buhar türbini CHP sistemlerinin termodinamik kalitesini anlamak için exergy analizini zorunlu kılar.

## 1. Karşı Basınçlı CHP (Back-Pressure CHP)

### 1.1 Konfigürasyon Detayları

```
Akış şeması:
Kazan → Yüksek Basınçlı Buhar → Buhar Türbini → Proses Buharı → Proses
                                       ↓
                                   Jeneratör → Elektrik

Çalışma prensibi:
- Tüm buhar türbinden geçtikten sonra prosese gönderilir
- Türbin çıkış basıncı = proses gereksinim basıncı (tipik 2-15 bar)
- Kondenser yok — tüm çıkış buharı faydalı kullanılır
- Elektrik üretimi, buhar talebine bağlıdır (slave mode)

Tipik parametreler:
- Giriş basıncı: 20-80 bar
- Giriş sıcaklığı: 350-520°C
- Çıkış basıncı: 2-15 bar (proses gereksinimi)
- HPR: 3-10 (yüksek ısı, düşük elektrik oranı)
- Elektrik verimi: %10-25 (yalnızca elektrik bazında)
- Toplam enerji verimi: %80-92
- Toplam exergy verimi: %25-38
```

### 1.2 Avantaj ve Dezavantajlar

| Avantaj | Dezavantaj |
|---------|------------|
| En yüksek enerji verimi (%80-92) | Elektrik üretimi buhar talebine bağlı |
| Basit sistem, düşük yatırım | Düşük elektrik/ısı oranı (PHR = 0.10-0.30) |
| Kondenser yok — soğutma suyu gereksiz | Buhar talebi düşerse elektrik de düşer |
| Düşük bakım maliyeti | Şebeke bağımsızlığı zor (import gerekli) |
| Yüksek güvenilirlik | Yaz aylarında düşük kapasite kullanımı |

### 1.3 Exergy Analizi Detay

```
Karşı basınçlı CHP exergy dağılımı (tipik):

Yakıt exergisi (input): %100
├── Kazan kayıpları: %30-40 (yanma tersinmezliği + ısı transferi)
├── Türbin iş çıkışı (elektrik): %10-20
├── Proses buharı exergisi: %15-30
├── Türbin iç kayıpları: %3-8
└── Boru/yardımcı kayıpları: %2-5

Önemli not:
Enerji verimi %85+ olmasına rağmen exergy verimi %25-38'dir.
Bunun nedeni: proses buharının sıcaklığı düşüktür (150-200°C)
ve Carnot faktörü (1 - T₀/T_proses) düşüktür.

Proses buharı exergy içeriği:
4 bar, doymuş buhar: ex ≈ 600 kJ/kg, h ≈ 2,738 kJ/kg
→ Exergy/Enerji oranı ≈ %22

10 bar, doymuş buhar: ex ≈ 760 kJ/kg, h ≈ 2,778 kJ/kg
→ Exergy/Enerji oranı ≈ %27
```

## 2. Çekişli CHP (Extraction CHP)

### 2.1 Konfigürasyon Detayları

```
Akış şeması:
Kazan → HP Buhar → [HP Kademe] → Çekiş Noktası → Proses Buharı
                                       ↓
                                  [LP Kademe] → Kondenser
                                       ↓
                                   Jeneratör → Elektrik

Çalışma prensibi:
- Buhar bir kısmı ara basınçtan çekilerek prosese gönderilir
- Kalan buhar LP kademelerinden geçerek kondensere gider
- Elektrik ve ısı üretimi kısmen bağımsız kontrol edilebilir
- Çekiş miktarı ayarlanarak HPR değiştirilebilir

Tipik parametreler:
- Giriş basıncı: 30-85 bar
- Giriş sıcaklığı: 380-520°C
- Çekiş basıncı: 3-15 bar (proses gereksinimi)
- Çıkış basıncı: 0.05-0.10 bar (kondenser)
- HPR: 2-6 (ayarlanabilir)
- Elektrik verimi: %15-30
- Toplam enerji verimi: %75-88
- Toplam exergy verimi: %28-42
```

### 2.2 Tek ve Çift Çekiş Karşılaştırma

| Parametre | Tek Çekiş | Çift Çekiş |
|-----------|-----------|------------|
| Çekiş noktası | 1 (orta basınç) | 2 (yüksek + orta basınç) |
| Esneklik | Orta | Yüksek |
| Proses buhar basıncı | Tek seviye | İki seviye (ör. 10 bar + 3 bar) |
| Kontrol karmaşıklığı | Düşük | Orta-yüksek |
| Yatırım maliyeti | Orta | Yüksek |
| Exergy verimi | %28-38 | %30-42 |
| Uygulama | Tek proses hattı | Çok kademeli proses ısısı |

### 2.3 Exergy Analizi Detay

```
Çekişli CHP exergy dağılımı (tipik):

Yakıt exergisi (input): %100
├── Kazan kayıpları: %30-38
├── HP kademe iş: %8-15
├── LP kademe iş: %5-12
├── Proses buhar exergisi: %12-25
├── Kondenser exergy kaybı: %5-12
├── Türbin iç kayıpları: %4-8
└── Boru/yardımcı kayıpları: %2-5

Avantaj: Kondensere giden buhar miktarı ayarlanarak
exergy kaybı minimize edilebilir.

Çekiş oranı (extraction ratio) etkisi:
α = ṁ_çekiş / ṁ_giriş

α = 0.0 → Tam yoğuşma modu (maksimum elektrik, HPR ≈ 0)
α = 0.5 → Dengeli mod (orta elektrik, orta ısı, HPR ≈ 2-3)
α = 1.0 → Tam karşı basınç modu (minimum elektrik, HPR ≈ 6-10)
```

## 3. Condensing-Extraction CHP

### 3.1 Konfigürasyon Detayları

```
Condensing-extraction türbin:
- Çekişli türbinin tam esneklikli versiyonu
- Kondenser bölümü her zaman aktif (minimum akış gerekli)
- Elektrik üretimi buhar talebinden bağımsızlaştırılabilir
- En yüksek operasyonel esneklik

Çalışma modları:
1. Tam yoğuşma: Tüm buhar kondensere → maksimum elektrik
2. Kısmi çekiş: Proses talebi kadar çekiş → dengeli mod
3. Tam çekiş: Maksimum çekiş → karşı basınçlı moda yakın

Tipik parametreler:
- Giriş basıncı: 40-100 bar
- Giriş sıcaklığı: 420-540°C
- HPR: 0.5-4 (geniş aralık, yüke göre değişken)
- Elektrik verimi: %20-35
- Toplam enerji verimi: %60-85
- Toplam exergy verimi: %32-45
```

### 3.2 Operasyonel Esneklik Diyagramı

```
Güç [MW]
    │
    │  ●──────────● Maksimum güç hattı
    │ /            \
    │/   İşletme    \
    │    Zarfı       \
    │                 ● Maksimum çekiş
    │                /
    │  ●────────────● Minimum güç hattı
    │
    └─────────────────── Proses Isısı [MW_th]

İşletme zarfı (operating envelope):
- Sol üst: Tam yoğuşma, minimum ısı, maksimum elektrik
- Sağ alt: Tam çekiş, maksimum ısı, minimum elektrik
- Orta bölge: Normal çalışma alanı
```

## 4. Türbin Seçim Kriterleri

### 4.1 HPR Bazlı Seçim

| HPR Aralığı | Önerilen Konfigürasyon | Gerekçe |
|-------------|------------------------|---------|
| >6 | Karşı basınçlı | Isı baskın, elektrik ikincil |
| 3-6 | Çekişli | Dengeli ısı/elektrik |
| 1-3 | Condensing-extraction | Elektrik ağırlıklı |
| <1 | Condensing + ayrı kazan | Elektrik baskın |

### 4.2 Buhar Koşulları Bazlı Seçim

```
Giriş buhar basıncı ve türbin tipi eşleştirmesi:

10-25 bar, 200-350°C (düşük basınç):
→ Tek kademeli karşı basınçlı
→ Güç: 0.1-2 MW
→ η_is: %55-72

25-45 bar, 350-420°C (orta basınç):
→ Çok kademeli karşı basınçlı veya tek çekişli
→ Güç: 1-10 MW
→ η_is: %70-82

45-85 bar, 420-520°C (yüksek basınç):
→ Çekişli veya condensing-extraction
→ Güç: 5-50 MW
→ η_is: %78-88

85+ bar, 520-600°C (çok yüksek basınç):
→ Condensing-extraction veya reheatli yoğuşmalı
→ Güç: 20-200+ MW
→ η_is: %85-93
```

### 4.3 Yük Profili Bazlı Seçim

```
Yük profili analizi — karar ağacı:

1. Buhar talebi sabit mi?
   Evet → Karşı basınçlı (en basit, en ucuz)
   Hayır → Devam

2. Buhar talebi ile elektrik talebi arasında korelasyon var mı?
   Evet → Çekişli türbin (HPR ayarlanabilir)
   Hayır → Devam

3. Elektrik bağımsız kontrol gerekli mi?
   Evet → Condensing-extraction (tam esneklik)
   Hayır → Çekişli + buhar akümülatörü

4. Mevsimsel değişim büyük mü?
   Evet → Condensing-extraction + trijenerasyon düşün
   Hayır → Çekişli yeterli
```

## 5. Exhaust Koşulu Optimizasyonu (Back-Pressure Seçimi)

### 5.1 Proses Basıncı ve Exergy Etkisi

| Çıkış Basıncı [bar] | T_doyma [°C] | Spesifik İş [kJ/kg]* | Proses Exergy [kJ/kg] | Enerji Verimi [%] | Exergy Verimi [%] |
|---------------------|-------------|---------------------|-----------------------|--------------------|--------------------|
| 2 | 120.2 | 420-520 | 430 | 88-92 | 24-30 |
| 4 | 143.6 | 350-450 | 600 | 85-90 | 26-34 |
| 6 | 158.8 | 300-400 | 700 | 83-88 | 28-36 |
| 10 | 179.9 | 240-340 | 760 | 80-86 | 30-38 |
| 15 | 198.3 | 180-280 | 820 | 78-84 | 32-40 |

*40 bar, 400°C girişten, η_is = %80

### 5.2 Optimum Back-Pressure Belirleme

```
Optimum çıkış basıncı seçimi:

Kural 1: Proses gereksinim basıncının 0.5-1.0 bar üstü
→ Boru kayıpları ve kontrol vanası basınç düşümü telafisi

Kural 2: Doyma sıcaklığı, proses sıcaklığının 10-20°C üstü
→ Yeterli ısı transferi sürücü kuvveti (ΔT)

Kural 3: Exergy optimizasyonu
→ Proses buhar sıcaklığını gereksiz yüksek tutma
→ Her 10°C fazla kızdırma ≈ %0.5-1.0 exergy kaybı artışı

Örnek:
Proses gereksinimi: 3.5 bar, 140°C doymuş buhar
Boru kaybı: 0.3 bar
Kontrol vanası: 0.2 bar
Optimum türbin çıkışı: 3.5 + 0.3 + 0.2 = 4.0 bar
T_doyma(4 bar) = 143.6°C ✓
```

## 6. Giriş Buhar Optimizasyonu

### 6.1 Basınç ve Sıcaklık Artırmanın Etkisi

```
Giriş koşullarını yükseltmenin exergy etkisi:

Senaryo 1 (mevcut): 30 bar, 350°C
- ex_giriş = 1,050 kJ/kg
- Spesifik iş (→ 4 bar, η_is=0.80) = 310 kJ/kg

Senaryo 2 (basınç artışı): 45 bar, 400°C
- ex_giriş = 1,210 kJ/kg (+%15)
- Spesifik iş (→ 4 bar, η_is=0.80) = 395 kJ/kg (+%27)

Senaryo 3 (yüksek basınç): 60 bar, 480°C
- ex_giriş = 1,370 kJ/kg (+%30)
- Spesifik iş (→ 4 bar, η_is=0.80) = 475 kJ/kg (+%53)

Sonuç: Giriş basıncını %50 artırmak, spesifik işi %27 artırır.
Giriş sıcaklığını artırmak hem verimi hem de çıkış buhar kalitesini iyileştirir.
Ancak kazan yatırım ve işletme maliyetleri artar.
```

### 6.2 Kazan-Türbin Eşleştirme Optimizasyonu

```
Optimal eşleştirme kriterleri:

1. Kazan çıkış basıncı → türbin giriş basıncı - boru kayıpları (1-3 bar)
2. Buhar sıcaklığı → yeterli kızdırma: minimum 50°C superheat
3. Buhar debisi → türbin kapasitesinin %70-100 aralığında
4. Kazan verimi etkisi: Yüksek basınç → kazan verimi %1-3 düşebilir
5. Net exergy etkisi: Türbin kazancı > kazan kaybı olmalı

Kontrol listesi:
□ Giriş sıcaklığı kızdırılmış bölgede mi? (wet steam riski)
□ Buhar debisi minimum akışın üstünde mi?
□ Kısmi yükte verim kabul edilebilir mi?
□ Bakım aralığı ve maliyet bütçe dahilinde mi?
```

## 7. CHP Exergy Analizi Detay

### 7.1 Konfigürasyon Karşılaştırma Tablosu

| Parametre | Karşı Basınçlı | Çekişli | Condensing-Ext. |
|-----------|-----------------|---------|-----------------|
| Giriş koşulları | 20-60 bar | 30-85 bar | 40-100 bar |
| Çıkış basıncı | 2-15 bar | 0.05-0.10 bar | 0.05-0.10 bar |
| HPR aralığı | 3-10 (sabit) | 2-6 (ayarlanabilir) | 0.5-4 (geniş) |
| η_enerji [%] | 80-92 | 75-88 | 60-85 |
| η_exergy [%] | 25-38 | 28-42 | 32-45 |
| PES [%] | 10-22 | 12-28 | 15-30 |
| Esneklik | Düşük | Orta | Yüksek |
| Yatırım [EUR/kW] | 600-1,000 | 800-1,200 | 1,000-1,500 |
| Karmaşıklık | Basit | Orta | Yüksek |

### 7.2 Exergy Akış Karşılaştırması

```
Karşı basınçlı CHP (5 MW_e, 40 bar/400°C → 4 bar):
Yakıt exergisi:          48,500 kW (%100)
├── Kazan exergy yıkımı: 17,000 kW (%35.1)
├── Türbin iş çıkışı:     5,260 kW (%10.8)
├── Türbin exergy yıkımı:  1,200 kW  (%2.5)
├── Proses buhar exergisi: 10,660 kW (%22.0)
├── Proses kullanım kaybı:  8,900 kW (%18.3)
└── Diğer kayıplar:        5,480 kW (%11.3)

η_ex,CHP = (5,260 + 10,660) / 48,500 = %32.8

Çekişli CHP (10 MW_e, 60 bar/480°C → 6 bar çekiş + 0.07 bar):
Yakıt exergisi:           78,000 kW (%100)
├── Kazan exergy yıkımı:  27,300 kW (%35.0)
├── HP kademe iş:          6,200 kW  (%7.9)
├── LP kademe iş:          4,500 kW  (%5.8)
├── Çekiş buhar exergisi: 14,800 kW (%19.0)
├── Kondenser exergy kaybı: 6,200 kW  (%7.9)
├── Türbin exergy yıkımı:  3,100 kW  (%4.0)
└── Diğer kayıplar:       15,900 kW (%20.4)

η_ex,CHP = (10,700 + 14,800) / 78,000 = %32.7
```

## 8. Kıyaslama Tablosu — CHP Prime Mover Karşılaştırma

| Parametre | Buhar Türbini CHP | Gaz Türbini CHP | Motor CHP | Yakıt Hücresi CHP |
|-----------|-------------------|-----------------|-----------|-------------------|
| Güç aralığı [MW] | 0.5-200+ | 1-300+ | 0.1-20 | 0.001-50 |
| Elektrik verimi [%] | 15-30 | 25-40 | 35-45 | 40-60 |
| Toplam enerji verimi [%] | 80-92 | 70-85 | 75-90 | 75-90 |
| Exergy verimi [%] | 25-38 | 35-48 | 40-52 | 48-62 |
| HPR | 3-10 | 1.5-2.5 | 0.8-1.5 | 0.5-1.0 |
| Yakıt esnekliği | Herhangi | Doğalgaz/sıvı | Doğalgaz/biyogaz | H₂/doğalgaz |
| Başlangıç süresi | 1-8 saat | 10-30 dakika | 1-5 dakika | 1-3 saat |
| Kısmi yük performansı | İyi (%50+) | Orta (%40+) | Çok iyi (%30+) | İyi (%30+) |
| Ömür [yıl] | 25-35+ | 20-30 | 15-25 | 10-20 |
| Bakım maliyeti [EUR-ct/kWh] | 0.3-0.5 | 0.5-1.0 | 1.0-2.0 | 1.5-3.0 |

## İlgili Dosyalar

- [Formüller](../formulas.md) -- Buhar türbini exergy hesaplama formülleri
- [Benchmarklar](../benchmarks.md) -- Verimlilik karşılaştırma verileri
- [Karşı Basınçlı Türbin](../equipment/back_pressure.md) -- BP türbin teknik detayları
- [Çekişli Türbin](../equipment/extraction.md) -- Extraction türbin detayları
- [Yoğuşmalı Türbin](../equipment/condensing.md) -- Condensing türbin detayları
- [Gaz Türbini CHP](gas_turbine_chp.md) -- Gaz türbini + HRSG konfigürasyonları
- [Motor CHP](engine_chp.md) -- Reciprocating engine CHP
- [Trijenerasyon](trigeneration.md) -- CCHP konfigürasyonları
- [HRSG](hrsg.md) -- HRSG türbin perspektifi
- [Kojenerasyon Temelleri](../../factory/cogeneration.md) -- Sistem seviyesi CHP karşılaştırma
- [Kazan Formülleri](../../boiler/formulas.md) -- Kazan verimlilik hesaplamaları
- [Verim İyileştirme](../solutions/efficiency_improvement.md) -- Türbin verim iyileştirme yöntemleri
- [Yük Eşleştirme](../solutions/load_matching.md) -- Termal/elektrik yük eşleştirme

## Referanslar

- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Horlock, J.H. (1997). *Cogeneration — Combined Heat and Power (CHP): Thermodynamics and Economics*, Pergamon Press.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- US DOE (2012). *Improving Steam System Performance -- A Sourcebook for Industry*, 2nd Edition.
- EU Directive 2012/27/EU, "Energy Efficiency Directive -- High Efficiency Cogeneration."
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- Moran, M.J. et al. (2018). *Fundamentals of Engineering Thermodynamics*, 9th Edition, Wiley.
- Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis and exergoeconomics," *Energy*, 32(4), pp. 249-253.
