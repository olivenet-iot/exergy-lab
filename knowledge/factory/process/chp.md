---
title: "Kojenerasyon / CHP Prosesi (Combined Heat and Power Process)"
category: factory
equipment_type: factory
keywords: [CHP, kojenerasyon, kombine ısı güç, exergy verimi, fuel utilization, gaz türbini, buhar türbini, BAT, LCP BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/steam_generation.md, factory/process/heating.md, steam_turbine/systems/chp_configurations.md]
use_when: ["CHP/kojenerasyon prosesi exergy analizi yapılacakken", "CHP performansı değerlendirilecekken", "CHP BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Kojenerasyon / CHP Prosesi (Combined Heat and Power Process)

---

## 1. Proses Tanımı

### Nedir?
Kojenerasyon (CHP — Combined Heat and Power), tek bir yakıt kaynağından hem elektrik (veya mekanik güç) hem de yararlı ısıyı birlikte üretme prosesidir. Ayrı üretimle karşılaştırıldığında %15-40 birincil enerji tasarrufu sağlar.

### Nerede Kullanılır?
- Sürekli buhar + elektrik ihtiyacı olan tesisler (kağıt, kimya, gıda)
- Bölgesel ısıtma (district heating)
- Hastaneler, havalimanları, alışveriş merkezleri
- Endüstriyel tesislerin kendi elektriği (self-generation)
- Atık ısı geri kazanım potansiyeli yüksek tesisler

### CHP Konfigürasyonları

| Konfigürasyon | Elektrik Verimi | Isı Verimi | Toplam Verim | Ölçek |
|---------------|----------------|-----------|-------------|-------|
| Gaz türbini + HRSG | %25-40 | %35-50 | %70-85 | 1 – 500 MWe |
| Buhar türbini (karşı basınç) | %10-25 | %55-70 | %75-90 | 0.5 – 100 MWe |
| Gaz motoru + ısı geri kazanım | %35-45 | %30-45 | %75-90 | 0.1 – 10 MWe |
| Buhar türbini (kondansasyonlu-ekstraksiyon) | %15-35 | %30-55 | %65-80 | 5 – 200 MWe |
| Mikro CHP (mikro türbin, Stirling) | %25-35 | %40-55 | %75-90 | 1 – 500 kWe |
| CCHP (trigeneration) | %25-40 | %25-40 | %70-85 | 0.5 – 50 MWe |

### Ayrı Üretim Referansı

| Parametre | Ayrı Elektrik | Ayrı Isı | CHP |
|-----------|--------------|----------|-----|
| Yakıt verimi (enerji) | %35-55 | %85-95 | %75-90 |
| Yakıt verimi (exergy) | %35-55 | %25-40 | %35-55 |
| CO₂ emisyonu | Yüksek | Orta | Düşük (birleşik) |

---

## 2. Termodinamik Minimum Exergy

### 2.1 Exergy Verimi vs Fuel Utilization Factor

CHP'de **iki farklı verimlilik metriği** kullanılır:

**Fuel Utilization Factor (FUF) — 1. Yasa:**
$$FUF = \frac{W_{el} + Q_{ısı}}{Q_{yakıt}} \quad (\text{tipik: %70-90})$$

**Exergy Verimi — 2. Yasa:**
$$\eta_{ex,CHP} = \frac{W_{el} + Ex_{ısı}}{Ex_{yakıt}} \quad (\text{tipik: %35-55})$$

> **Kritik Fark:** FUF, ısı ve elektriği eşit sayar. Exergy verimi, ısının termodinamik kalitesini (Carnot faktörü) dikkate alır. **Düşük sıcaklık ısı çıkışı yüksek FUF verebilir ama exergy verimi düşük kalır.**

### 2.2 CHP Minimum Exergy

CHP'nin minimum exergy gereksinimi, ayrı üretim toplamıdır:
$$Ex_{min,CHP} = W_{el} + Q_{ısı} \times \left(1 - \frac{T_0}{T_{ısı}}\right)$$

### 2.2b Carnot Tabanlı CHP Exergy Türetimi (FUF vs η_ex Matematiksel İlişki)

CHP'de iki ürün vardır: elektrik (W) ve ısı (Q). FUF ve η_ex arasındaki matematiksel fark:

**FUF (1. Yasa):**
$$FUF = \frac{W + Q}{F}$$

Burada F = yakıt enerji girişi. FUF, W ve Q'yu eşit ağırlıkta toplar.

**Exergy Verimi (2. Yasa):**
$$\eta_{ex} = \frac{W + Q \times \theta_C}{F \times \phi}$$

Burada:
- θ_C = (1 − T₀/T_ısı) — Carnot faktörü, ısının exergy kalitesi
- φ = Ex_yakıt/LHV — yakıt exergy/enerji oranı (doğal gaz: 1.04)

**FUF ve η_ex arasındaki bağlantı:**
$$\eta_{ex} = \frac{W + Q \times \theta_C}{F \times \phi} = \frac{FUF \times F - Q \times (1 - \theta_C)}{F \times \phi}$$

$$\eta_{ex} = \frac{FUF}{\phi} - \frac{Q}{F \times \phi} \times (1 - \theta_C)$$

**Kritik gözlem:** η_ex = FUF/φ − (Q/F)/φ × (1−θ_C). Ikinci terim her zaman pozitiftir ve ısı payı (Q/F) büyüdükçe, sıcaklık (T_ısı) düştükçe artar. Bu nedenle:
- **Düşük sıcaklık ısı üreten CHP:** η_ex << FUF (büyük fark)
- **Yüksek sıcaklık ısı üreten CHP:** η_ex ≈ FUF/φ (küçük fark)
- **Sadece elektrik:** η_ex = FUF/φ ≈ FUF (Q = 0)

**Sayısal gösterim — sabit FUF = %85 ile:**

| T_ısı (°C) | θ_C | Q/F oranı | η_ex | FUF − η_ex |
|-------------|-----|-----------|------|------------|
| 60 | 0.105 | 0.50 | %43 | 42 puan |
| 90 | 0.179 | 0.50 | %47 | 38 puan |
| 150 | 0.295 | 0.50 | %52 | 33 puan |
| 200 | 0.370 | 0.50 | %55 | 30 puan |
| 300 | 0.482 | 0.50 | %60 | 25 puan |

> **Kaynak:** Kotas (1985), Bölüm 5, s. 98-115 — CHP exergy analizi türetimi; Tsatsaronis (2007), s. 250-251.

### 2.3 Çözümlü Örnek

**Problem:** 5 MWe gaz türbini CHP, 8 MW termal (10 bar doymuş buhar).

```
Gaz türbini verimi: η_el = 33%, yakıt tüketimi = 5/0.33 = 15.15 MW
HRSG ısı geri kazanımı: 8 MW termal (buhar)
Toplam yakıt tüketimi: 15.15 MW (doğal gaz)

FUF = (5 + 8) / 15.15 = 85.8% (çok iyi görünür)

Exergy hesabı:
Ex_yakıt = 15.15 × 1.04 = 15.76 MW (doğal gaz exergy)
Ex_el = 5 MW (elektrik = exergy)
Ex_ısı = 8 × (1 − 298.15/453.15) = 8 × 0.342 = 2.74 MW

η_ex,CHP = (5 + 2.74) / 15.76 = 49.1% (gerçek termodinamik verim)

Ex_min = 5 + 2.74 = 7.74 MW
ESI = 7.74 / 15.76 = 0.491 → Derece B
```

**Yorum:** FUF = %85.8 çok iyi görünürken, exergy verimi = %49.1 ve ESI = 0.491 daha gerçekçi bir tablo ortaya koyar. Isının termodinamik kalitesi düşük olduğu için exergy verimi FUF'tan çok daha düşüktür.

**Kaynak:** Kotas (1985), Ch. 5; Tsatsaronis (2007).

### 2.4 Çözümlü Örnek: Gaz Motoru CHP (2 MWe)

**Problem:** 2 MWe gaz motoru CHP. Egzoz ve ceket suyu ısı geri kazanımı ile 2.4 MW termal (90 °C sıcak su). Doğal gaz: 5.0 MW (LHV).

```
FUF = (2.0 + 2.4) / 5.0 = 88.0%

Exergy hesabı:
Ex_yakıt = 5.0 × 1.04 = 5.20 MW
Ex_el = 2.0 MW
Ex_ısı = 2.4 × (1 − 298.15/363.15) = 2.4 × 0.179 = 0.430 MW

η_ex = (2.0 + 0.430) / 5.20 = 46.7%

Ex_min = 2.0 + 0.430 = 2.430 MW
ESI = 2.430 / 5.20 = 0.467 → Derece B
```

**Kısmi yük analizi:**

| Yük (%) | W_el (MW) | Q_ısı (MW) | F (MW) | FUF | η_ex | ESI |
|---------|-----------|-----------|--------|-----|------|-----|
| 100 | 2.00 | 2.40 | 5.00 | 88.0% | 46.7% | 0.467 |
| 75 | 1.50 | 1.95 | 4.10 | 84.1% | 44.1% | 0.441 |
| 50 | 1.00 | 1.40 | 3.40 | 70.6% | 36.8% | 0.368 |

> **Kritik:** %50 yükte FUF %70.6'ya düşerken, η_ex %36.8'e düşer. Kısmi yükte çalışma CHP exergy performansını ciddi şekilde düşürür.

**Kaynak:** EPA CHP Partnership, Catalog of CHP Technologies (2017), Ch. 2 — Reciprocating Engines.

### 2.5 Çözümlü Örnek: CCGT CHP (100 MWe)

**Problem:** 100 MWe kombine çevrim (CCGT) CHP tesisi. Gaz türbini: 67 MWe, buhar türbini: 33 MWe. Proses buharı ekstraksiyon: 80 MW termal (10 bar doymuş). Doğal gaz: 200 MW (LHV).

```
FUF = (100 + 80) / 200 = 90.0%

Exergy hesabı:
Ex_yakıt = 200 × 1.04 = 208 MW
Ex_el = 100 MW
Ex_ısı = 80 × (1 − 298.15/453.15) = 80 × 0.342 = 27.36 MW

η_ex = (100 + 27.36) / 208 = 61.2%
ESI = 127.36 / 208 = 0.612 → Derece A

BPR: BAT η_ex (CCGT CHP) = %58 → Ex_BAT = 127.36/0.58 = 219.6 MW
BPR = 208 / 219.6 = 0.947 → BAT üzerinde!
```

**Yorum:**
- ESI = 0.612 → Derece A — dünya sınıfı CHP performansı
- CCGT'nin yüksek elektrik verimi (%50 GT + %16.5 ST) exergy verimini yukarı taşır
- 10 bar buharın Carnot faktörü (0.342) makul — daha düşük T ısı çıkışı olsaydı η_ex düşerdi
- BPR = 0.947 → BAT üzerinde performans (modern tesis avantajı)

**Kaynak:** LCP BREF 2017, Ch. 7, s. 310-345.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 CHP Exergy Verim Aralıkları

| CHP Tipi | η_ex Aralığı | Tipik η_ex | FUF |
|----------|-------------|------------|-----|
| Gaz türbini + HRSG | %35 – %50 | %42 | %75-85 |
| Buhar türbini (karşı basınç) | %25 – %40 | %32 | %80-90 |
| Gaz motoru + ısı kazanım | %40 – %55 | %48 | %80-90 |
| Kondansasyonlu-ekstraksiyon | %35 – %50 | %42 | %65-80 |
| CCGT + HRSG (kombine çevrim) | %45 – %60 | %52 | %75-85 |

### 3.2 ESI Aralıkları

| CHP Tipi | ESI Aralığı | Tipik ESI |
|----------|------------|-----------|
| Gaz türbini + HRSG (iyi) | 0.35 – 0.50 | 0.42 |
| Buhar türbini (karşı basınç) | 0.25 – 0.40 | 0.32 |
| Gaz motoru | 0.40 – 0.55 | 0.48 |
| CCGT + HRSG | 0.45 – 0.60 | 0.52 |

### 3.3 Irreversibilite Kaynakları

1. **Yanma:** %35 – %50 — Yakıt kimyasal exergy → termal exergy
2. **Türbin/motor:** %10 – %20 — İzentropik verim sınırı
3. **Baca gazı çıkışı:** %5 – %15 — HRSG sonrası sıcak gaz
4. **Isı transferi (HRSG/HX):** %8 – %15 — Sıcaklık farkı irreversibilitesi
5. **Mekanik/jeneratör:** %2 – %5 — Sürtünme, elektriksel kayıplar
6. **Yardımcı ekipman:** %2 – %5 — Pompalar, fanlar, kontrol

### 3.4 CHP Tipine Göre Detaylı Irreversibilite Dağılımı

**Gaz Türbini + HRSG CHP:**

| Bileşen | Exergy Yıkımı (%) | Açıklama |
|---------|-------------------|----------|
| Kompresör | 3 – 5 | Hava sıkıştırma irreversibilitesi |
| Yanma odası | 35 – 42 | Kimyasal → termal dönüşüm |
| Gaz türbini | 8 – 12 | İzentropik olmayan genişleme |
| HRSG | 10 – 15 | Sıcaklık farkı, pinch point |
| Baca gazı | 5 – 10 | Atılan termal exergy |
| Jeneratör | 1 – 3 | Elektriksel kayıplar |
| Yardımcı | 2 – 4 | Pompa, fan, kontrol |

**Gaz Motoru CHP:**

| Bileşen | Exergy Yıkımı (%) | Açıklama |
|---------|-------------------|----------|
| Yanma + motor | 40 – 50 | İçten yanmalı motor irreversibilitesi |
| Egzoz ısı kazanım | 5 – 10 | Egzoz → su/buhar transferi |
| Ceket suyu kazanım | 3 – 7 | Düşük T farkı ile kazanım |
| Egzoz çıkışı | 5 – 8 | Atılan egzoz exergy'si |
| Jeneratör | 2 – 4 | Elektriksel kayıplar |
| Yardımcı | 2 – 3 | Soğutma suyu pompası vb. |

### 3.5 Sektöre Göre CHP Exergy Performansı

| Sektör | Tipik CHP Tipi | Isı Kullanımı | Tipik η_ex | FUF |
|--------|---------------|--------------|------------|-----|
| Kağıt/selüloz | Buhar türbini (karşı basınç) | Proses buharı (3-10 bar) | %28-35 | %82-88 |
| Kimya | CCGT veya gaz türbini | Yüksek T proses ısısı | %45-55 | %75-85 |
| Gıda | Gaz motoru | Sıcak su + buhar | %40-48 | %80-88 |
| Tekstil | Gaz türbini + HRSG | Kurutma + boyama | %38-45 | %78-85 |
| Hastane/kampüs | Gaz motoru + CCHP | Isıtma + soğutma | %35-45 | %75-85 |
| Bölgesel ısıtma | Gaz türbini veya CCGT | Sıcak su (70-120 °C) | %35-42 | %80-90 |
| Seramik/cam | Gaz türbini | Yüksek T fırın | %42-50 | %72-82 |
| Rafineri | Buhar türbini + GT | Çoklu basınç buharı | %38-48 | %78-86 |

> **AI Kuralı:** Sektöre göre CHP benchmark'ı kullanırken, ısı kullanım sıcaklığını mutlaka dikkate al. Aynı FUF ile farklı sektörlerde η_ex ciddi şekilde farklılaşır.

---

## 3b. Kısmi Yük Performansı (Part-Load Analysis)

CHP tesislerinin büyük çoğunluğu tam yükte çalışmaz. Mevsimsel ısı talebi, üretim değişkenliği ve elektrik piyasası koşulları kısmi yük çalışmayı zorunlu kılar.

### 3b.1 Kısmi Yük Exergy Verimi Düşüşü

| CHP Tipi | 100% Yük η_ex | 75% Yük η_ex | 50% Yük η_ex | Minimum Yük |
|----------|---------------|---------------|---------------|-------------|
| Gaz türbini | %42 | %38 (−%10) | %33 (−%21) | %40-50 |
| Gaz motoru | %48 | %44 (−%8) | %37 (−%23) | %30-40 |
| Buhar türbini | %32 | %30 (−%6) | %27 (−%16) | %20-30 |
| CCGT | %52 | %48 (−%8) | %42 (−%19) | %40-50 |

### 3b.2 Mevsimsel Analiz Matrisi

| Sezon | Isı Talebi | Elektrik Talebi | CHP Yükü | η_ex Etkisi | Strateji |
|-------|-----------|-----------------|----------|-------------|----------|
| Kış | Yüksek | Orta | %80-100 | En iyi | Tam yük CHP |
| İlkbahar/Sonbahar | Orta | Orta | %50-80 | Orta | Modüler çalışma |
| Yaz | Düşük | Yüksek | %30-60 | En düşük | CHP + absorpsiyon (CCHP) |

> **AI Kuralı:** CHP ESI değerlendirmesinde yıllık ortalama yük profilini sor. Sadece tam yük ESI'si yanıltıcıdır. Kısmi yükte %10-20 ESI düşüşü tipiktir.

### 3b.3 Kısmi Yük Exergy Yıkımı Analizi

Kısmi yükte çalışan CHP'lerde exergy yıkım dağılımı tam yükten farklılaşır:

```
Tam yük (100%):
  Yanma: %40 | Türbin: %12 | HRSG: %12 | Baca: %8 | Diğer: %5

Kısmi yük (50%):
  Yanma: %38 | Türbin: %16 | HRSG: %14 | Baca: %12 | Diğer: %8
```

**Kısmi yükte değişen faktörler:**
- Türbin izentropik verimi düşer (kanat açısı uyumsuzluğu) → türbin exergy yıkımı artar
- HRSG gaz hızı düşer → ısı transfer katsayısı düşer → pinch point artar
- Baca gazı sıcaklığı değişir → atılan exergy oranı artar
- Yardımcı ekipman sabit güç çeker → oransal pay artar

### 3b.4 Termal Depolama ile Kısmi Yük Optimizasyonu

CHP'nin kısmi yükte çalışmasını önlemek için termal enerji depolama (TES — Thermal Energy Storage) kullanılabilir:

| TES Tipi | Depolama Ortamı | T Aralığı | Kapasite | CHP Etkisi |
|----------|----------------|-----------|----------|-----------|
| Sıcak su tankı | Su | 70-95 °C | 1-50 MWh_th | Isı yükü dengeleme |
| Buhar akümülatörü | Basınçlı su/buhar | 150-200 °C | 5-100 MWh_th | Buhar yükü dengeleme |
| Buz deposu (CCHP) | Su/buz | 0-7 °C | 0.5-20 MWh_th | Soğutma pik kesme |

**TES ile CHP exergy kazancı:** Termal depolama, CHP'nin tam yükte daha uzun süre çalışmasını sağlayarak yıllık ortalama η_ex'i %3-8 artırabilir.

> **AI Kuralı:** CHP kısmi yükte çalışıyorsa, termal depolama potansiyelini her zaman değerlendir. Yatırım maliyeti düşük, exergy kazancı yüksektir.

---

## 4. BAT Referansı

### 4.1 EU BREF LCP 2017

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Gaz türbini elektrik verimi | %36-41 | > 50 MWe, yeni tesis |
| CCGT elektrik verimi | %57-62 | > 100 MWe, yeni tesis |
| Gaz türbini CHP FUF | > %80 | BAT-AEPL |
| CCGT CHP FUF | > %75 | BAT-AEPL |
| Baca gazı çıkış sıcaklığı | < 120 °C | Kondenser/HRSG sonrası |

### 4.2 BAT Exergy Değerleri

| CHP Tipi | BAT η_ex | BAT ESI | Kaynak |
|----------|---------|---------|--------|
| Gaz türbini + HRSG | %45-50 | 0.45-0.50 | LCP BREF + exergy dönüşüm |
| Gaz motoru | %48-55 | 0.48-0.55 | LCP BREF + exergy dönüşüm |
| CCGT + HRSG | %52-58 | 0.52-0.58 | LCP BREF + exergy dönüşüm |
| Buhar türbini (karşı basınç) | %32-38 | 0.32-0.38 | Literatür |

### 4.3 CHP vs Ayrı Üretim — Exergy Karşılaştırması

| Senaryo | Yakıt Exergy (MW) | Elektrik (MW) | Isı Exergy (MW) | η_ex |
|---------|-------------------|---------------|-----------------|------|
| Ayrı: Grid + Kazan | 9.26 + 7.14 = 16.40 | 5.0 | 2.74 | %47.2 |
| CHP: Gaz türbini + HRSG | 15.76 | 5.0 | 2.74 | %49.1 |
| **Tasarruf** | **0.64 MW (%3.9)** | — | — | — |

> **Not:** Exergy bazlı tasarruf, enerji bazlı tasarruftan daha düşük görünür çünkü enerji karşılaştırması ısının kalitesini abartır.

---

## 4b. CHP Boyutlandırma Metodolojisi

### 4b.1 Isı Talebi Bazlı Boyutlandırma

```
Adım 1: Yıllık ısı yük profili çıkar (saatlik veya aylık)
Adım 2: Taban yükü belirle (yıl boyunca sürekli mevcut minimum ısı talebi)
Adım 3: CHP kapasitesi ≤ Taban ısı yükü (genellikle %60-80'i)
Adım 4: Güç/Isı oranı seç → CHP konfigürasyonu belirle
```

### 4b.2 Güç/Isı Oranı ve Konfigürasyon Seçimi

| Güç/Isı Oranı (elektrik/termal) | Önerilen CHP Tipi | Tipik η_ex |
|-----------------------------------|-------------------|-----------|
| < 0.5 | Buhar türbini (karşı basınç) | %25-35 |
| 0.5 – 0.8 | Gaz türbini + HRSG | %40-48 |
| 0.8 – 1.2 | Gaz motoru | %45-52 |
| > 1.2 | CCGT (yüksek elektrik payı) | %50-58 |

### 4b.3 Ekonomik Fizibilite Hızlı Tarama

| Parametre | Eşik Değer | Kaynak |
|-----------|-----------|--------|
| Yıllık çalışma süresi | > 4.500 h/yıl | COGEN Europe |
| Minimum ısı talebi | > 500 kW_th sürekli | DOE CHP |
| Elektrik/gaz fiyat oranı (spark spread) | > 2.5 | Ekonomik eşik |
| Yatırım geri dönüşü | < 5 yıl | Kabul edilebilir |

---

## 4c. EU CHP Direktifi (2012/27/EU) ve Yasal Çerçeve

### 4c.1 Yüksek Verimli CHP Tanımı

EU Enerji Verimliliği Direktifi (2012/27/EU), Ek II'de yüksek verimli CHP kriterlerini belirler:

| Kriter | Koşul | Açıklama |
|--------|-------|----------|
| Birincil enerji tasarrufu (PES) | > %10 | Ayrı üretimle karşılaştırma |
| Küçük ölçek (< 1 MWe) | PES > %0 | Daha düşük eşik |

**PES Hesaplama:**
$$PES = 1 - \frac{1}{\frac{\eta_{el,CHP}}{\eta_{el,ref}} + \frac{\eta_{th,CHP}}{\eta_{th,ref}}}$$

Referans verimlilikleri (2015 düzeltmeli):
- η_el_ref: %52.5 (doğal gaz, yeni tesis)
- η_th_ref: %90 (buhar/sıcak su)

### 4c.2 CCHP — Trigeneration (Soğutma + Isı + Güç)

Yaz aylarında ısı talebinin düşmesi ile CHP kullanım oranı azalır. CCHP (Combined Cooling, Heat and Power) bu sorunu çözer:

| Bileşen | Kış Modu | Yaz Modu |
|---------|----------|----------|
| CHP motor/türbin | Elektrik + ısı | Elektrik + ısı |
| Absorpsiyon chiller | Kapalı | Atık ısı → soğutma |
| Isı çıkışı | Proses/bina | Absorpsiyon chiller girişi |
| FUF | %80-90 | %75-85 (soğutma dahil) |
| η_ex | %42-55 | %38-50 (soğutma exergy'si düşük) |

**CCHP exergy avantajı:** Yaz aylarında atık ısıyı absorpsiyon chiller'a yönlendirmek, CHP'nin yıllık ortalama yük faktörünü %60-70'den %80-90'a çıkarır.

### 4c.3 ORC (Organic Rankine Cycle) — Düşük Sıcaklık CHP

Atık ısı kaynağı 80-300 °C arasında olduğunda, su buharı yerine organik akışkan (R245fa, R134a, pentan vb.) kullanılır:

| Parametre | Değer | Not |
|-----------|-------|-----|
| Kaynak sıcaklığı | 80-300 °C | Endüstriyel atık ısı |
| Elektrik verimi | %6-18 | Kaynak T'ye bağlı |
| Tipik ölçek | 50 kWe – 5 MWe | Modüler, standart paket |
| Exergy verimi | %20-35 | Kaynak exergy'sine göre |
| ROI | 3-7 yıl | Kaynak bedava ise |

> **AI Kuralı:** Atık ısı > 100 °C ve > 500 kW olan her tesiste ORC değerlendirmesini öner.

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Yanma odası | 35 – 50 | Düşük (termodinamik sınır) |
| 2 | Türbin/motor | 10 – 20 | Orta (daha verimli makine) |
| 3 | HRSG / ısı geri kazanım | 8 – 15 | Orta (ek yüzey, ekonomizer) |
| 4 | Baca gazı çıkışı | 5 – 15 | Yüksek (kondenser, LT geri kazanım) |
| 5 | Mekanik + jeneratör | 2 – 5 | Düşük (bakım odaklı) |
| 6 | Yardımcı sistemler | 2 – 5 | Orta (VFD, optimizasyon) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **HRSG optimizasyonu** | %3-8 yakıt | 2-3 yıl | Ek ekonomizer, süperısıtıcı; pinch point azaltma |
| 2 | **Isı/güç oranı optimizasyonu** | %5-15 exergy | 1-3 yıl | Mevsimsel yük profili analizi, iki modlu çalışma |
| 3 | **Emilme soğutma entegrasyonu (CCHP)** | %10-20 birincil | 3-6 yıl | Yaz aylarında atık ısı → soğutma; trigeneration |
| 4 | **Buhar seviye optimizasyonu** | %5-10 exergy | 1-2 yıl | Gereksiz yüksek basınçlı buhar → düşük basınca indirme |
| 5 | **Baca gazı ısı geri kazanımı** | %3-7 yakıt | 2-4 yıl | Düşük sıcaklık geri kazanım (kondenser, ısı pompası) |
| 6 | **Termal depolama (TES)** | %3-8 exergy | 2-4 yıl | Kısmi yük önleme, tam yükte çalışma süresi artırma |
| 7 | **Modüler CHP** | %5-12 exergy | 3-5 yıl | Birden fazla küçük ünite, yük takibi |
| 8 | **PRV → türbin ikamesi** | %2-5 exergy | 1-3 yıl | Basınç düşürme vanası yerine buhar türbini |

### 6.2 İyileştirme Stratejileri — Detaylı Açıklamalar

**1. HRSG Optimizasyonu:**
HRSG (Heat Recovery Steam Generator) CHP'nin ısı geri kazanım kalbidir. Optimizasyon yöntemleri:
- **Ekonomizer ekleme:** Baca gazından besleme suyu ön ısıtma, baca T'si 20-40 °C düşer
- **Süperısıtıcı ekleme:** Buhar kalitesi artırma, türbin verimi iyileştirme
- **Pinch point azaltma:** Tasarım pinch 8-15 °C → optimum 5-8 °C (dikkat: yüzey maliyeti)
- **Çift basınç HRSG:** Tek basınç yerine HP+LP buhar üretimi, baca T'si düşer

**2. Isı/Güç Oranı Optimizasyonu:**
- Mevsimsel yük profili analizi ile CHP çalışma modu belirleme
- Yaz: elektrik ağırlıklı (kondansasyon modu veya CCHP)
- Kış: ısı ağırlıklı (karşı basınç veya ekstraksiyon artırma)
- İki modlu çalışma: otomatik mod geçişi ile yıllık η_ex maksimizasyonu

**3. CCHP Entegrasyonu:**
- Tek etkili absorpsiyon chiller: COP_th = 0.7, kaynak > 80 °C
- Çift etkili absorpsiyon chiller: COP_th = 1.2, kaynak > 150 °C
- Adsorpsiyon chiller: COP_th = 0.5-0.6, kaynak > 60 °C (düşük T uygun)
- CCHP yıllık yük faktörünü %60-70'den %80-90'a çıkarır

**4. Buhar Seviye Optimizasyonu:**
- Proses ihtiyacından yüksek basınçta buhar üretmek exergy yıkımıdır
- Proses 3 bar buhar gerektiriyorsa, 10 bar üretip PRV ile düşürmek yerine 3 bar üret
- Çoklu basınç seviyesi: HP (40 bar), MP (10 bar), LP (3 bar) → her proses kendi seviyesinden

---

## 6b. Exergoekonomik Değerlendirme (CHP Özel)

### 6b.1 CHP Exergoekonomik Parametreler

| Parametre | Tanım | Tipik CHP Değeri |
|-----------|-------|-----------------|
| c_F (yakıt exergy birim maliyeti) | ₺/GJ veya €/GJ | 8-15 €/GJ (doğal gaz) |
| c_P,el (elektrik exergy birim maliyeti) | ₺/GJ veya €/GJ | 20-35 €/GJ |
| c_P,th (ısı exergy birim maliyeti) | ₺/GJ veya €/GJ | 12-25 €/GJ |
| Ċ_D (exergy yıkım maliyeti) | €/h veya €/yıl | Bileşene göre değişir |
| f_k (exergoekonomik faktör) | — | 0.15-0.65 |
| r_k (göreceli maliyet farkı) | — | 0.5-3.0 |

### 6b.2 CHP Bileşen Bazlı Exergoekonomik Analiz

```
Bileşen         | Ċ_D payı | f_k    | Öncelik
Yanma odası     | %40-50   | < 0.15 | Yüksek (Ċ_D dominant)
Türbin/motor    | %15-25   | 0.3-0.5| Orta
HRSG            | %10-20   | 0.2-0.4| Orta-Yüksek
Kompresör       | %5-10    | 0.4-0.6| Düşük-Orta
Jeneratör       | %3-5     | 0.5-0.7| Düşük
```

> **AI Kuralı:** CHP exergoekonomik analizinde yanma odası her zaman en yüksek Ċ_D'ye sahiptir ancak f_k < 0.15 olduğu için yatırımla iyileştirmesi sınırlıdır (termodinamik sınır). Türbin ve HRSG iyileştirme için daha uygun bileşenlerdir.

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER CHP prosesi:
  → HER ZAMAN hem FUF hem η_ex raporla — farkı açıkla
  → ESI > 0.50 "CHP için çok iyi — CCGT veya gaz motoru sınıfı"
  → ESI 0.35-0.50 "CHP için iyi — gaz türbini sınıfı"
  → ESI 0.25-0.35 "CHP için orta — buhar türbini veya düşük verimli GT"
  → ESI < 0.25 "CHP için düşük — sistem verimliliğini kontrol et"
```

### 7.2 FUF vs η_ex Uyarısı

```
EĞER FUF > %80 AMA η_ex < %35:
  → "Dikkat: Yüksek FUF düşük kaliteli ısı üretiminden kaynaklanıyor"
  → "Exergy açısından ısının termodinamik değeri düşük"
  → "Daha yüksek sıcaklık ısı üretimi veya elektrik payı artırma değerlendir"

EĞER FUF < %70:
  → "FUF düşük — ısı geri kazanım yetersiz"
  → "HRSG, egzoz ısı geri kazanım, proses entegrasyonu kontrol et"
```

### 7.3 CHP Potansiyel Değerlendirmesi

```
EĞER tesis buhar tüketiyor AMA CHP yok:
  → "Mevcut buhar kazanı önüne buhar türbini yerleştirme fizibilitesi değerlendir"
  → "Buhar basıncı farkı × debi = türbin güç potansiyeli"

EĞER CHP var AMA kısmi yükte çalışıyor:
  → "Kısmi yük CHP exergy verimi %10-20 düşer"
  → "Mevsimsel analiz ve termal depolama değerlendir"
```

### 7.4 Benchmark Referansları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| CHP η_ex (gaz türbini) | > %45 | %35-45 | < %35 |
| CHP η_ex (gaz motoru) | > %50 | %40-50 | < %40 |
| CHP η_ex (CCGT) | > %55 | %45-55 | < %45 |
| CHP η_ex (buhar türbini) | > %35 | %25-35 | < %25 |
| FUF | > %80 | %70-80 | < %70 |
| Güç/ısı oranı (exergy) | > 1.5 | 1.0-1.5 | < 1.0 |
| PES (EU Direktifi) | > %15 | %10-15 | < %10 |
| Yıllık yük faktörü | > %80 | %60-80 | < %60 |

### 7.5 CHP Tipi Tespit Kuralları

```
EĞER elektrik/ısı oranı > 1.0:
  → Muhtemelen gaz motoru veya CCGT
  → η_ex benchmark: %45-55

EĞER elektrik/ısı oranı < 0.5:
  → Muhtemelen buhar türbini (karşı basınç)
  → η_ex benchmark: %25-35

EĞER ısı sıcaklığı < 100 °C:
  → Düşük kalite ısı — FUF yüksek ama η_ex düşük olacak
  → Uyarı: "Isı exergy kalitesi düşük, FUF yanıltıcı olabilir"
```

### 7.6 CHP → Ayrı Üretim Karşılaştırma Kuralı

```
EĞER CHP η_ex < ayrı üretim η_ex:
  → "CHP exergy verimi ayrı üretimden düşük — sistem verimsiz"
  → "Olası nedenler: kısmi yük, düşük T ısı, eski ekipman"
  → "Acil eylem: konfigürasyon gözden geçirme"

Ayrı üretim referans η_ex hesabı:
  η_ex_ayrı = (W_el/η_el_grid × η_el_grid + Q_ısı×θ_C/η_th_kazan × η_th_kazan) /
              (W_el/η_el_grid + Q_ısı/η_th_kazan) × 1/φ
  Basitleştirilmiş: η_ex_ayrı ≈ %42-48 (tipik endüstriyel)
```

### 7.7 Yatırım Karar Matrisi

```
EĞER ESI < 0.35 VE yaş > 15 yıl:
  → "CHP yenileme (retrofit veya değiştirme) değerlendir"
  → "Modern gaz motoru veya mikro GT ile %10-20 η_ex artışı mümkün"

EĞER ESI > 0.50 VE yük faktörü > %80:
  → "CHP performansı iyi — mevcut durumu koru"
  → "Marjinal iyileştirmeler: HRSG optimizasyonu, VFD"

EĞER FUF > %85 AMA ESI < 0.40:
  → "Yüksek FUF düşük T ısı üretiminden — exergy kalitesi düşük"
  → "Daha yüksek T ısı kullanıcısı bul veya absorpsiyon chiller ekle"
```

### 7.8 Çevresel Değerlendirme Kuralları

```
CHP CO₂ tasarrufu hesaplama:
  CO₂_ayrı = W_el × EF_grid + Q_ısı/η_kazan × EF_gaz
  CO₂_CHP = F_CHP × EF_gaz
  CO₂_tasarruf = CO₂_ayrı − CO₂_CHP

Emisyon faktörleri (EF):
  EF_grid (Türkiye) ≈ 0.47 tCO₂/MWh_el
  EF_gaz ≈ 0.20 tCO₂/MWh_yakıt
  EF_grid (EU ortalama) ≈ 0.27 tCO₂/MWh_el

EĞER CO₂_tasarruf > 0:
  → "CHP çevresel fayda sağlıyor — yıllık {X} tCO₂ azaltma"
EĞER CO₂_tasarruf < 0:
  → "Dikkat: CHP ayrı üretimden daha fazla CO₂ — grid çok temiz veya CHP verimsiz"
```

---

## İlgili Dosyalar

- `factory/process/steam_generation.md` — Buhar üretim prosesi
- `factory/process/heating.md` — Isıtma prosesi
- `steam_turbine/systems/chp_configurations.md` — CHP konfigürasyonları
- `steam_turbine/economics/feasibility.md` — CHP fizibilite analizi
- `factory/cogeneration.md` — Kojenerasyon genel bilgi
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi

## Referanslar

1. European Commission, JRC (2017). *BAT Reference Document for Large Combustion Plants (LCP BREF)*. Ch. 7 — CHP BAT.
2. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — CHP exergy analizi.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — CHP exergy değerlendirmesi.
4. Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis." *Energy*, 32(4), 249-253.
5. EU Directive 2012/27/EU on Energy Efficiency — CHP referans verimlilikleri.
6. European Parliament (2012). *Directive 2012/27/EU on Energy Efficiency*. Annex II — High-Efficiency CHP criteria, PES calculation.
7. COGEN Europe (2020). *European Cogeneration Review*. — CHP pazar verileri ve teknoloji karşılaştırması.
8. EPA Combined Heat and Power Partnership (2017). *Catalog of CHP Technologies*. — Gaz motoru, gaz türbini, buhar türbini teknik verileri.
9. Tchanche, B.F. et al. (2011). "Low-grade heat conversion into power using organic Rankine cycles." *Renewable and Sustainable Energy Reviews*, 15(8), 3963-3979. — ORC teknolojisi.
10. Herold, K.E., Radermacher, R. & Klein, S.A. (2016). *Absorption Chillers and Heat Pumps*. 2nd ed., CRC Press. — Absorpsiyon soğutma CHP entegrasyonu.
