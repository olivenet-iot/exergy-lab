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
| FUF | > %80 | %70-80 | < %70 |
| Güç/ısı oranı (exergy) | > 1.5 | 1.0-1.5 | < 1.0 |

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
