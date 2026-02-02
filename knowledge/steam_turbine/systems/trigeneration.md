---
title: "Trijenerasyon Sistemleri — CCHP (Combined Cooling, Heating and Power)"
category: systems
equipment_type: steam_turbine
keywords: [trijenerasyon, CCHP, absorpsiyon chiller, soğutma, ısıtma, elektrik, mevsimsel strateji, exergy, COP, LiBr]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/systems/gas_turbine_chp.md, steam_turbine/systems/engine_chp.md, factory/cogeneration.md, chiller/equipment/absorption.md, chiller/formulas.md]
use_when: ["Trijenerasyon sistemi değerlendirilirken", "CHP + absorpsiyon chiller entegrasyonu analiz edilirken", "Mevsimsel enerji stratejisi planlanırken", "Soğutma exergisi hesaplanırken", "CCHP ekonomik değerlendirme yapılırken"]
priority: medium
last_updated: 2026-01-31
---
# Trijenerasyon Sistemleri — CCHP (Combined Cooling, Heating and Power)

> Son güncelleme: 2026-01-31

## Genel Bakış

Trijenerasyon (CCHP -- Combined Cooling, Heating and Power), bir CHP sistemine absorpsiyonlu soğutma ünitesi eklenerek aynı anda elektrik, ısı ve soğutma üretilmesidir. Geleneksel CHP sistemlerinde yaz aylarında ısı talebi düştüğünde sistem verimsiz çalışır; trijenerasyon, atık ısıyı absorpsiyon chiller ile soğutma üretimine dönüştürerek mevsimsel kapasite kullanımını artırır. Ancak, exergy perspektifinden soğutma çıkışının exergy içeriği oldukça düşüktür ve bu durum sistem tasarımında dikkatle değerlendirilmelidir.

**Temel Fark:** Soğutma (7°C) exergisi, ısıtma (90°C) exergisinden ve elektrikten çok daha düşüktür. CCHP enerji verimini artırırken exergy verimini sınırlı iyileştirir.

## 1. CCHP Konfigürasyonları

### 1.1 Prime Mover + Absorpsiyon Chiller Kombinasyonları

```
Konfigürasyon 1: Gaz Motoru + Absorpsiyon Chiller
Motor egzozu (350-500°C) → tek etkili absorpsiyon chiller
Motor jacket water (80-95°C) → sıcak su ile absorpsiyon chiller
- Elektrik: %35-42
- Soğutma COP: 0.65-0.75 (tek etkili, sıcak su kaynaklı)
- Toplam verim: %70-85

Konfigürasyon 2: Gaz Türbini + HRSG + Absorpsiyon Chiller
GT egzozu → HRSG → buhar (6-10 bar)
Buhar → çift etkili absorpsiyon chiller
- Elektrik: %25-38
- Soğutma COP: 1.0-1.2 (çift etkili, buhar kaynaklı)
- Toplam verim: %75-88

Konfigürasyon 3: Buhar Türbini CHP + Absorpsiyon Chiller
Kazan → BT → proses buhar → çift etkili absorpsiyon chiller
Veya: BT çıkış buharı → tek etkili absorpsiyon chiller
- Elektrik: %12-25
- Soğutma COP: 0.65-1.2 (basınca bağlı)
- Toplam verim: %75-90

Konfigürasyon 4: Kombine Çevrim + Absorpsiyon Chiller
GT → HRSG → ST → düşük basınç buhar → absorpsiyon chiller
- En yüksek elektrik verimi + soğutma
- Elektrik: %45-55
- Toplam verim: %70-85
```

### 1.2 Konfigürasyon Karşılaştırma Tablosu

| Parametre | Motor CCHP | GT CCHP | BT CCHP | CCGT CCHP |
|-----------|-----------|---------|---------|-----------|
| Güç aralığı [MW_e] | 0.1-10 | 1-100+ | 0.5-50 | 10-500+ |
| Elektrik verimi [%] | 35-42 | 25-38 | 12-25 | 45-55 |
| COP (soğutma) | 0.65-0.75 | 1.0-1.2 | 0.65-1.2 | 1.0-1.2 |
| Toplam η_enerji [%] | 70-85 | 75-88 | 75-90 | 70-85 |
| Toplam η_exergy [%] | 38-48 | 35-48 | 24-36 | 45-58 |
| Yatırım [EUR/kW_e] | 1,200-2,000 | 1,500-2,500 | 1,000-1,800 | 2,000-3,500 |
| Mevsimsel esneklik | Yüksek | Orta-yüksek | Orta | Yüksek |

## 2. Absorpsiyon Chiller Entegrasyonu

### 2.1 Tek Etkili Absorpsiyon Chiller (Single-Effect)

```
Tek etkili absorpsiyon chiller (LiBr-Su):
- Isı kaynağı: Sıcak su (75-95°C) veya düşük basınçlı buhar (1-2 bar)
- COP: 0.65-0.75 (ısıl)
- Soğutma kapasitesi: 100-5,000 kW
- Chilled water çıkış: 6-7°C
- Soğutma suyu gereksinimi: ~3.5-4.0 kW_soğutma_suyu / kW_soğutma

Exergy performansı:
COP_exergy = Ėx_soğutma / Ėx_ısı_giriş

Soğutma exergisi:
Ėx_soğutma = Q̇_soğutma × |1 - T₀/T_soğutma|
            = Q̇_soğutma × |1 - 298/280|  (7°C chilled water)
            = Q̇_soğutma × 0.064

Isı giriş exergisi (90°C sıcak su):
Ėx_ısı = Q̇_ısı × (1 - T₀/T_ısı)
        = Q̇_ısı × (1 - 298/363) = Q̇_ısı × 0.179

COP_exergy = (Q̇_soğutma × 0.064) / (Q̇_ısı × 0.179)
           = COP_termal × 0.064 / 0.179
           = 0.70 × 0.358 = 0.25

Sonuç: Tek etkili absorpsiyon chiller exergy verimi %25
Elektrikli chiller exergy verimi: %35-45 (COP 5-7 ile)
```

### 2.2 Çift Etkili Absorpsiyon Chiller (Double-Effect)

```
Çift etkili absorpsiyon chiller (LiBr-Su):
- Isı kaynağı: Buhar (4-10 bar, 150-180°C) veya sıcak su (>140°C)
- COP: 1.0-1.2 (ısıl)
- Soğutma kapasitesi: 200-10,000+ kW
- Chilled water çıkış: 6-7°C
- Soğutma suyu gereksinimi: ~2.8-3.2 kW_soğutma_suyu / kW_soğutma

Exergy performansı:
Isı giriş exergisi (6 bar buhar, 159°C):
Ėx_ısı = Q̇_ısı × (1 - T₀/T_ısı)
        = Q̇_ısı × (1 - 298/432) = Q̇_ısı × 0.310

COP_exergy = COP_termal × (0.064 / 0.310)
           = 1.10 × 0.206 = 0.23

Not: Çift etkili COP termal olarak daha yüksek (%57 daha fazla),
ama exergy verimi tek etkili ile benzer.
Bunun nedeni: Daha yüksek sıcaklık kaynağı kullanılması.

Çift etkili chiller detayları: → chiller/equipment/absorption.md
```

### 2.3 Üç Etkili ve İleri Teknolojiler

| Tip | COP_termal | COP_exergy | Kaynak T [°C] | Durum |
|-----|-----------|-----------|---------------|-------|
| Tek etkili (sıcak su) | 0.65-0.75 | 0.22-0.28 | 75-95 | Yaygın |
| Tek etkili (buhar) | 0.70-0.80 | 0.18-0.24 | 100-120 | Yaygın |
| Çift etkili (buhar) | 1.0-1.2 | 0.20-0.25 | 150-180 | Yaygın |
| Çift etkili (direct-fired) | 1.0-1.4 | 0.06-0.08 | 800-1,000 | Yaygın |
| Üç etkili | 1.4-1.7 | 0.16-0.22 | 200-230 | Sınırlı |

```
Dikkat: Direct-fired (doğrudan yakmalı) absorpsiyon chiller exergy verimi
çok düşüktür (%6-8). Yüksek sıcaklık yakıtın (exergy yoğun) düşük
sıcaklık soğutmaya (exergy fakir) dönüşümü büyük tersinmezlik yaratır.

Öneri: CCHP'de CHP atık ısısı ile çalışan absorpsiyon chiller tercih edin.
Direct-fired absorpsiyon chiller exergy açısından verimsizdir.
```

## 3. Mevsimsel Strateji

### 3.1 Kış-Yaz Çalışma Modları

```
Kış modu (ısıtma sezonu — Kasım-Mart):
- CHP tam kapasite çalışır
- Atık ısı → bina/proses ısıtma
- Absorpsiyon chiller devre dışı (veya düşük kapasite)
- HPR: 1.0-2.5 (ısı ağırlıklı)
- Toplam η_enerji: %80-90
- Toplam η_exergy: %35-48

Yaz modu (soğutma sezonu — Haziran-Eylül):
- CHP tam kapasite çalışır
- Atık ısı → absorpsiyon chiller → soğutma
- HPR → "Cooling-to-Power Ratio" (CPR): 0.5-2.0
- Toplam η_enerji: %70-85
- Toplam η_exergy: %32-42 (soğutma exergisi düşük)

Geçiş dönemi (Nisan-Mayıs, Ekim):
- Azaltılmış kapasite veya ısı/soğutma karışık mod
- Isı akümülatörü faydalı olabilir
- HPR değişken

Mevsimsel kapasite faktörü karşılaştırma:
- Salt CHP (ısıtma): CF = %50-65 (yaz aylarında düşük)
- CCHP (ısıtma + soğutma): CF = %70-85 (yıl boyu yüksek)
```

### 3.2 Türk İklim Koşullarında Mevsimsel HPR

```
Türkiye iklim bölgelerine göre CCHP mevsimsel performans:

Bölge 1 — Akdeniz/Ege (Antalya, İzmir):
Kış: HPR = 0.8-1.5 (ılıman, düşük ısıtma)
Yaz: CPR = 1.5-2.5 (yüksek soğutma talebi)
Yıllık CF: %75-85
Sonuç: Soğutma ağırlıklı CCHP çok uygun

Bölge 2 — Marmara (İstanbul, Bursa):
Kış: HPR = 1.5-2.5 (orta ısıtma)
Yaz: CPR = 1.0-2.0 (orta soğutma)
Yıllık CF: %70-80
Sonuç: Dengeli CCHP uygun

Bölge 3 — İç Anadolu (Ankara, Konya):
Kış: HPR = 2.0-3.0 (soğuk kış, yüksek ısıtma)
Yaz: CPR = 1.0-1.5 (sıcak-kuru yaz)
Yıllık CF: %70-80
Sonuç: Isıtma ağırlıklı, soğutma ek avantaj

Bölge 4 — Doğu Anadolu (Erzurum, Kars):
Kış: HPR = 3.0-5.0 (çok soğuk, uzun kış)
Yaz: CPR = 0.3-0.8 (kısa, ılıman yaz)
Yıllık CF: %65-75
Sonuç: CHP yeterli, CCHP marjinal katkı
```

## 4. CCHP Exergy Analizi

### 4.1 Soğutma Exergisinin Düşüklüğü

```
Exergy perspektifinden enerji formları sıralaması:
1. Elektrik: %100 exergy (saf iş)
2. Yüksek T ısı (>300°C): %40-60 exergy
3. Orta T ısı (100-200°C): %15-35 exergy
4. Düşük T ısı (60-90°C): %8-18 exergy
5. Soğutma (5-7°C): %5-7 exergy ← ÇOK DÜŞÜK

Soğutma exergisi hesabı:
Ėx_soğutma = Q̇_soğutma × |1 - T₀/T_soğutma|

Örnekler (T₀ = 25°C = 298 K):
- 7°C soğutma: |1 - 298/280| = 0.064 → %6.4 exergy
- 0°C soğutma: |1 - 298/273| = 0.092 → %9.2 exergy
- -18°C soğutma: |1 - 298/255| = 0.169 → %16.9 exergy

Karşılaştırma — 1,000 kW ısı kaynağı ile:
Absorpsiyon chiller (COP=0.70): 700 kW soğutma × 0.064 = 45 kW exergy
Isıtma (90°C sıcak su): 1,000 kW × 0.179 = 179 kW exergy
Elektrik üretimi (η=0.30): 300 kW × 1.00 = 300 kW exergy

Sonuç: Aynı ısı kaynağından üretilen soğutma exergisi,
ısıtma exergisinin %25'i, elektrik exergisinin %15'idir.
```

### 4.2 CCHP Exergy Dağılımı (Tipik Motor CCHP)

```
Motor CCHP exergy dağılımı (1 MW_e, yaz modu):
Yakıt exergisi (doğalgaz):              2,600 kW (%100)
├── Elektrik çıkışı:                    1,000 kW (%38.5)
├── Yanma tersinmezliği:                  520 kW (%20.0)
├── Motor iç kayıpları:                   260 kW (%10.0)
├── Absorpsiyon chiller:
│   ├── Soğutma exergisi:                  45 kW  (%1.7)
│   │   └── 700 kW soğutma × 0.064
│   ├── Chiller exergy yıkımı:           180 kW  (%6.9)
│   ├── Soğutma kulesi exergy atımı:      55 kW  (%2.1)
│   └── Toplam ısı kullanım:             280 kW (%10.8)
├── Kullanılmayan ısı (radyasyon vb.):   260 kW (%10.0)
└── Diğer kayıplar:                      280 kW (%10.8)

η_ex,CCHP = (1,000 + 45) / 2,600 = %40.2 (yaz)

Kış modu (ısıtma):
η_ex,CCHP = (1,000 + 120_ısı) / 2,600 = %43.1 (kış)

Fark: Soğutma exergisi çok düşük olduğundan yaz exergy verimi kıştan düşük.
Ancak enerji verimi yaz ve kış benzerdir (%80-85).
```

## 5. CCHP Ekonomik Avantaj

### 5.1 Ekonomik Fayda Kaynakları

```
CCHP'nin ekonomik avantajları:

1. Artan kapasite faktörü:
   CHP: CF = %50-65 → CCHP: CF = %70-85
   Yıllık ek çalışma: 1,500-2,500 saat
   Ek gelir: Elektrik satışı + soğutma tasarrufu

2. Elektrikli chiller tasarrufu:
   Absorpsiyon chiller COP = 0.70 (ısıl)
   Elektrikli chiller COP = 5.0 (elektriksel)
   Eşdeğer elektrik tasarrufu: Q̇_soğutma / COP_elektrikli
   700 kW soğutma → 140 kW elektrik tasarrufu

3. Pik elektrik talebi azaltma:
   Soğutma sezonu = elektrik pik sezonu
   CCHP ile pik şebeke talebi azalır
   Demand charge tasarrufu: %10-30

4. Teşvik ve tarife avantajı:
   Yüksek verimli CHP teşviki (PES > %10)
   CCHP, CHP kapasite faktörünü artırarak PES'i iyileştirir

Tipik geri ödeme süreleri:
- Motor CCHP (doğalgaz): 3-6 yıl
- GT CCHP: 4-7 yıl
- BT CCHP: 4-8 yıl (mevcut CHP'ye absorpsiyon ekleme: 2-4 yıl)
```

### 5.2 CCHP vs CHP + Elektrikli Chiller Karşılaştırma

| Parametre | CCHP (absorpsiyon) | CHP + Elektrikli Chiller |
|-----------|--------------------|-----------------------------|
| Toplam η_enerji [%] | 75-88 | 70-82 |
| Toplam η_exergy [%] | 35-48 | 38-50 |
| Elektrik tüketimi (soğutma) | ~5 kW/100 kW | ~20 kW/100 kW |
| Soğutma suyu gereksinimi | Yüksek | Orta |
| Yatırım maliyeti | Yüksek (+absorpsiyon) | Orta (+elektrikli chiller) |
| İşletme maliyeti | Düşük (atık ısı) | Orta (elektrik) |
| CO₂ emisyonu | Düşük | Orta |
| Alan gereksinimi | Geniş | Kompakt |
| Bakım karmaşıklığı | Yüksek (LiBr, vakum) | Orta |
| Elektrik pik yükü | Düşük | Yüksek |

```
Exergy perspektifinden ilginç sonuç:
CHP + elektrikli chiller, exergy verimi açısından CCHP'den
bazen daha yüksek olabilir. Bunun nedeni:
- Elektrikli chiller COP 5-7 → exergy verimi %35-45
- Absorpsiyon chiller exergy verimi %20-25

Ancak toplam enerji kullanımı ve birincil enerji tasarrufu
açısından CCHP genellikle avantajlıdır.

Karar kriteri: Atık ısı bedava mi?
Evet → CCHP ekonomik
Hayır (ek yakıt gerekli) → Exergy analizi ile optimize et
```

## 6. Absorpsiyon Chiller Boyutlandırma

### 6.1 CHP Atık Isıdan Soğutma Kapasitesi

```
Mevcut CHP'ye absorpsiyon chiller ekleme:

Kullanılabilir ısı hesabı:
Q̇_mevcut_ısı = CHP atık ısı kapasitesi [kW]
Q̇_yaz_ısı_talebi = Yaz aylarında ısı talebi [kW] (genellikle düşük)
Q̇_absorpsiyon_için = Q̇_mevcut_ısı - Q̇_yaz_ısı_talebi [kW]

Soğutma kapasitesi:
Q̇_soğutma = Q̇_absorpsiyon_için × COP_absorpsiyon [kW]

Örnek (2 MW_e motor CHP):
Q̇_mevcut_ısı = 2,000 kW (egzoz + jacket water)
Q̇_yaz_ısı_talebi = 400 kW (sıcak su)
Q̇_absorpsiyon_için = 1,600 kW
Q̇_soğutma = 1,600 × 0.70 = 1,120 kW (320 ton)

Absorpsiyon chiller boyutu: ~1,200 kW (güvenlik marjı ile)
```

## İlgili Dosyalar

- [Formüller](../formulas.md) -- CHP exergy hesaplama formülleri
- [Benchmarklar](../benchmarks.md) -- CHP ve prime mover karşılaştırma
- [Buhar Türbini CHP](steam_turbine_chp.md) -- BT CHP konfigürasyonları
- [Gaz Türbini CHP](gas_turbine_chp.md) -- GT + HRSG CHP
- [Motor CHP](engine_chp.md) -- Motor CHP detayları
- [HRSG](hrsg.md) -- HRSG türbin perspektifi
- [Absorpsiyon Chiller](../../chiller/equipment/absorption.md) -- Absorpsiyon chiller teknik detayları
- [Chiller Formülleri](../../chiller/formulas.md) -- Chiller exergy hesaplamaları
- [Kojenerasyon Temelleri](../../factory/cogeneration.md) -- Sistem seviyesi CHP/CCHP
- [Fizibilite](../economics/feasibility.md) -- CHP/CCHP fizibilite analizi
- [Yük Eşleştirme](../solutions/load_matching.md) -- Mevsimsel yük eşleştirme

## Referanslar

- Horlock, J.H. (1997). *Cogeneration -- Combined Heat and Power (CHP): Thermodynamics and Economics*, Pergamon Press.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Herold, K.E., Radermacher, R. & Klein, S.A. (2016). *Absorption Chillers and Heat Pumps*, 2nd Edition, CRC Press.
- ASHRAE (2020). *ASHRAE Handbook -- HVAC Systems and Equipment*, Chapter 2: Absorption Equipment.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- US DOE (2017). *Combined Heat and Power and Microgrid Installation Databases*, DOE.
- Dossat, R.J. & Horan, T.J. (2001). *Principles of Refrigeration*, 5th Edition, Prentice Hall.
- Wu, D.W. & Wang, R.Z. (2006). "Combined cooling, heating and power: A review," *Progress in Energy and Combustion Science*, 32(5-6), pp. 459-495.
- EU Directive 2012/27/EU, "Energy Efficiency Directive -- High Efficiency Cogeneration."
