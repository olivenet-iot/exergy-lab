---
title: "Soğutma Prosesi (Cooling Process)"
category: factory
equipment_type: factory
keywords: [soğutma, cooling, chiller, COP, ters Carnot, exergy, endüstriyel soğutma, BAT, ICS BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/cold_storage.md, chiller/benchmarks.md]
use_when: ["Soğutma prosesi exergy analizi yapılacakken", "Chiller sistemi performansı değerlendirilecekken", "Soğutma BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Soğutma Prosesi (Cooling Process)

---

## 1. Proses Tanımı

### Nedir?
Soğutma prosesi, bir ortam veya akışkandan ısıyı alarak çevre sıcaklığının altına veya belirli bir hedef sıcaklığa düşürme işlemidir. Termodinamiğin 2. yasasına göre ısının düşük sıcaklıktan yüksek sıcaklığa transferi için dışarıdan iş (exergy) girişi gerekir.

### Nerede Kullanılır?
- Proses soğutma (kimya, plastik, metal işleme)
- İklimlendirme (endüstriyel bina, sunucu odası)
- Gıda soğutma (süt, et, içecek üretim hattı)
- Soğutmalı depolama (bkz. `cold_storage.md`)
- Kurutma sonrası soğutma

### İlgili Ekipmanlar
- Santrifüj chillerlar: 200 – 10.000+ kW
- Vidalı chillerlar: 50 – 1.500 kW
- Scroll chillerlar: 10 – 200 kW
- Absorpsiyon chillerlar: 100 – 5.000 kW (atık ısı ile çalışır)
- Soğutma kuleleri (wet/dry/hybrid)
- Free cooling (serbest soğutma) üniteleri

### Tipik Ölçek
- Küçük: 10 – 100 kW soğutma
- Orta: 100 – 1.000 kW soğutma
- Büyük: 1.000 – 10.000+ kW soğutma

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Soğutma prosesi için minimum exergy gereksinimi (ters Carnot çevriminden):

$$Ex_{min} = Q_{cold} \times \left(\frac{T_0}{T_{cold}} - 1\right)$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| Q_cold | Soğutma yükü (uzaklaştırılan ısı) | kW |
| T₀ | Çevre (kondenser) sıcaklığı | K |
| T_cold | Soğutulan ortamın sıcaklığı | K |

### 2.2 Sıcaklığa Bağlı Minimum COP ve Exergy

| T_cold (°C) | T₀ (°C) | COP_Carnot | Ex_min/Q_cold | Ex_min oranı |
|-------------|---------|------------|---------------|-------------|
| 15 | 35 | 14.4 | 0.069 | %6.9 |
| 7 | 35 | 10.0 | 0.100 | %10.0 |
| 0 | 35 | 7.80 | 0.128 | %12.8 |
| −10 | 35 | 5.85 | 0.171 | %17.1 |
| −18 | 35 | 4.81 | 0.208 | %20.8 |
| −30 | 35 | 4.00 | 0.267 | %26.7 |
| −40 | 35 | 3.23 | 0.322 | %32.2 |

> **Kritik Bilgi:** Soğutma sıcaklığı düştükçe exergy gereksinimi dramatik artar. −30 °C soğutma, +7 °C soğutmadan ~2.7 kat daha fazla exergy gerektirir.

### 2.3 Çözümlü Örnek

**Problem:** 500 kW soğutma kapasiteli chiller, T_cold = 7 °C, T₀ = 35 °C.

```
T_cold = 7 + 273.15 = 280.15 K
T₀ = 35 + 273.15 = 308.15 K

Ex_min = 500 × (308.15/280.15 − 1)
       = 500 × (1.100 − 1)
       = 500 × 0.100
       = 50 kW

COP_Carnot = T_cold / (T₀ − T_cold) = 280.15 / 28 = 10.0
COP_actual (tipik santrifüj) = 5.0

W_actual = Q_cold / COP_actual = 500 / 5.0 = 100 kW

ESI = Ex_min / W_actual = 50 / 100 = 0.50 → Derece A
```

**Not:** Chiller ESI = 0.50 çok yüksek görünür çünkü modern santrifüj chillerlar yüksek COP'ta çalışır. Ancak kondenser sıcaklığı yükseldiğinde veya kısmi yükte ESI düşer.

**Kaynak:** ASHRAE Handbook — Fundamentals; Dincer & Rosen (2013).

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 COP Aralıkları (Endüstriyel)

| Chiller Tipi | COP Aralığı | Tipik COP | T_cold |
|-------------|------------|-----------|--------|
| Santrifüj (su soğutmalı) | 5.0 – 7.0 | 5.5 | 7 °C |
| Vidalı (su soğutmalı) | 4.0 – 5.5 | 4.5 | 7 °C |
| Scroll (hava soğutmalı) | 2.5 – 3.5 | 3.0 | 7 °C |
| Absorpsiyon (tek etkili) | 0.6 – 0.8 | 0.7 | 7 °C |
| Absorpsiyon (çift etkili) | 1.0 – 1.4 | 1.2 | 7 °C |
| Amonyak (endüstriyel, −30 °C) | 1.5 – 2.5 | 2.0 | −30 °C |

### 3.2 Sistem ESI Aralıkları

| Soğutma Sistemi | ESI Aralığı | Tipik ESI | Not |
|----------------|------------|-----------|-----|
| Santrifüj + soğutma kulesi | 0.25 – 0.45 | 0.35 | En verimli ticari |
| Vidalı + soğutma kulesi | 0.20 – 0.35 | 0.27 | Yaygın endüstriyel |
| Hava soğutmalı scroll | 0.10 – 0.20 | 0.15 | Küçük tesisler |
| Absorpsiyon (atık ısı) | 0.15 – 0.30 | 0.22 | Atık ısı varsa avantajlı |

### 3.3 Irreversibilite Kaynakları

1. **Kompresör irreversibilitesi:** %30 – %45 — İzentropik verim sınırı
2. **Kondenser ΔT:** %15 – %25 — Soğutma suyu/hava ile sıcaklık farkı
3. **Evaporatör ΔT:** %10 – %20 — Soğutulan akışkan ile soğutucu akışkan farkı
4. **Genleşme valfi (kısılma):** %5 – %10 — İsentalpik genleşme irreversibilitesi
5. **Pompa ve fan:** %3 – %8 — Soğutma kulesi fanı, soğuk su pompası
6. **Boru ve izolasyon kayıpları:** %2 – %5 — Soğuk hat ısı kazancı

---

## 4. BAT Referansı

### 4.1 EU BREF ICS 2001 (Industrial Cooling Systems)

| Parametre | BAT Açıklaması | Not |
|-----------|----------------|-----|
| Soğutma kulesi yaklaşımı | 3 – 5 °C | Wet cooling tower |
| Free cooling entegrasyonu | Kış/geçiş mevsimlerinde | T_dış < T_soğuk su + 3 °C |
| Değişken debi kontrolü | VFD pompa + VFD fan | Kısmi yükte tasarruf |
| Su tüketimi | Minimizasyon, blowdown kontrolü | Çevresel BAT |

> **Not:** ICS BREF 2001 yılına ait olup güncel değildir. Modern chiller performans değerleri bu dokümanı aşmıştır.

### 4.2 ASHRAE / ARI Standartları (Güncel Referans)

| Chiller Tipi | BAT COP (ARI 550/590) | Tam Yük | IPLV |
|-------------|----------------------|---------|------|
| Santrifüj (su soğutmalı) | 6.0 – 7.0 | Tam yük | 8.0 – 10.0 |
| Vidalı (su soğutmalı) | 4.5 – 5.5 | Tam yük | 6.0 – 7.5 |
| Hava soğutmalı scroll | 3.0 – 3.5 | Tam yük | 4.0 – 4.5 |

### 4.3 BAT Exergy Değerleri

| Sistem | BAT COP | BAT ESI (7 °C, T₀=35 °C) | Kaynak |
|--------|---------|--------------------------|--------|
| Santrifüj + wet tower + VFD | 6.5 | 0.33 – 0.38 | ASHRAE 90.1 + exergy dönüşüm |
| Free cooling + chiller hibrit | — | 0.40 – 0.55 | Tahmini, mevsime bağlı |
| Absorpsiyon (atık ısı, exergy bazlı) | — | 0.30 – 0.50 | Exergy bazlı COP, literatür |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Kompresör | 30 – 45 | Orta (daha verimli kompresör) |
| 2 | Kondenser ΔT | 15 – 25 | Yüksek (soğutma kulesi bakımı) |
| 3 | Evaporatör ΔT | 10 – 20 | Orta (yüzey temizliği, ΔT azaltma) |
| 4 | Kısılma valfi | 5 – 10 | Düşük (ekonomizer, ejektör) |
| 5 | Pompa / fan | 3 – 8 | Yüksek (VFD) |
| 6 | Boru/izolasyon | 2 – 5 | Yüksek (izolasyon onarımı) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Soğutma kulesi bakımı + optimizasyonu** | %5-15 enerji | 0-1 yıl | Kondenser ΔT azaltma; her 1 °C düşüş ≈ %2.5 COP artışı |
| 2 | **Free cooling (serbest soğutma)** | %20-50 enerji | 1-3 yıl | Kış/geçiş mevsimlerinde kompresör devre dışı; iklime bağlı |
| 3 | **VFD (pompa + fan + kompresör)** | %15-30 enerji | 2-4 yıl | Kısmi yükte dramatik tasarruf |
| 4 | **Soğuk su sıcaklığı artırma** | %3-8 enerji | 0 (operasyonel) | Her 1 °C artış ≈ %2-3 COP artışı; kullanıcı ihtiyacını kontrol et |
| 5 | **Atık ısı ile absorpsiyon** | %30-60 birincil enerji | 3-7 yıl | Atık ısı kaynağı varsa; exergy bazlı değerlendirme gerekli |

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER T_cold > 0 °C (proses soğutma):
  → ESI > 0.35 "Soğutma prosesi için çok iyi"
  → ESI 0.20-0.35 "İyi, iyileştirme fırsatları var"
  → ESI < 0.20 "Düşük — COP ve sistem kayıpları incele"

EĞER T_cold: −18 °C ile 0 °C arası (orta dereceli):
  → ESI > 0.25 "Orta sıcaklık soğutma için çok iyi"
  → ESI 0.15-0.25 "Kabul edilebilir"
  → ESI < 0.15 "Zayıf — kompresör verimi ve izolasyon kontrol et"

EĞER T_cold < −18 °C (derin dondurma):
  → ESI > 0.20 "Derin dondurma için iyi"
  → ESI 0.10-0.20 "Ortalama"
  → ESI < 0.10 "Zayıf — kademeli soğutma ve süperizolayon öner"
```

### 7.2 Anahtar Kontrol Noktaları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| COP (7 °C su, su soğutmalı) | > 5.5 | 4.0-5.5 | < 4.0 |
| Kondenser yaklaşımı | < 3 °C | 3-5 °C | > 5 °C |
| Evaporatör yaklaşımı | < 3 °C | 3-5 °C | > 5 °C |
| Kısmi yük verimi (IPLV/NPLV) | > 7.0 | 5.0-7.0 | < 5.0 |

### 7.3 Free Cooling Potansiyeli

```
EĞER T_cold > 10 °C VE iklim ılıman/soğuk:
  → "Yıllık saatlerin %30-60'ında free cooling mümkün"
  → "Yıllık enerji tasarrufu %20-40 olabilir"

EĞER T_cold < 5 °C:
  → "Free cooling potansiyeli sınırlı — sadece kış ayları"
```

---

## İlgili Dosyalar

- `factory/process/cold_storage.md` — Soğuk depolama prosesi (uzun süreli)
- `chiller/benchmarks.md` — Chiller ekipman benchmark
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri
- `factory/heat_integration.md` — Isı entegrasyonu (atık ısı → absorpsiyon)
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanım teknolojileri

## Referanslar

1. European Commission, JRC (2001). *Reference Document on the Application of Best Available Techniques to Industrial Cooling Systems (ICS BREF)*.
2. ASHRAE (2021). *ASHRAE Handbook — Fundamentals*. Ch. 2 — Thermodynamics.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Soğutma çevrimi exergy analizi.
4. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
5. ARI Standard 550/590 (2023). *Performance Rating of Water-Chilling Packages*.
