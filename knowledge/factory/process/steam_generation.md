---
title: "Buhar Üretim Prosesi (Steam Generation Process)"
category: factory
equipment_type: factory
keywords: [buhar, steam, kazan, buhar üretimi, doymuş buhar, kızgın buhar, exergy, BAT, LCP BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/heating.md, factory/process/chp.md, boiler/benchmarks.md]
use_when: ["Buhar üretim prosesi exergy analizi yapılacakken", "Buhar sistemi performansı değerlendirilecekken", "Buhar BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Buhar Üretim Prosesi (Steam Generation Process)

---

## 1. Proses Tanımı

### Nedir?
Buhar üretim prosesi, yakıt enerjisini kullanarak suyu belirli basınç ve sıcaklıkta buhara dönüştürme işlemidir. Endüstriyel tesislerin en yaygın enerji taşıyıcı üretim prosesidir.

### Nerede Kullanılır?
- Proses ısıtma (kimya, gıda, tekstil, kağıt)
- Güç üretimi (buhar türbini çevrimleri)
- Sterilizasyon (gıda, ilaç, sağlık)
- Mekanik sürüş (buhar türbini ile pompa/kompresör)
- Isıtma (bina, sera)

### İlgili Ekipmanlar
- Ateş tüplü kazanlar (shell boilers): 0.5 – 25 ton/h
- Su borulu kazanlar (water-tube boilers): 10 – 500+ ton/h
- Atık ısı kazanları (HRSG): Türbin egzozu geri kazanımı
- Ekonomizer, süperısıtıcı, degazör, kondenstop
- Buhar dağıtım hatları, redüksiyon vanaları

### Tipik Ölçek
- Küçük: 0.5 – 5 ton/h buhar
- Orta: 5 – 50 ton/h buhar
- Büyük: 50 – 500+ ton/h buhar

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Buhar üretimi için minimum exergy, üretilen buharın spesifik exergy'sidir:

$$ex_{min} = (h_{steam} - h_0) - T_0 \times (s_{steam} - s_0)$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| h_steam | Buhar entalpisi | kJ/kg |
| h₀ | Ölü hal entalpisi (25 °C, 1 atm, sıvı su) | kJ/kg |
| s_steam | Buhar entropisi | kJ/(kg·K) |
| s₀ | Ölü hal entropisi | kJ/(kg·K) |
| T₀ | Çevre sıcaklığı | K (298.15 K) |

Ölü hal referans değerleri (25 °C, 101.325 kPa, sıvı su):
- h₀ = 104.9 kJ/kg
- s₀ = 0.3672 kJ/(kg·K)

### 2.2 Tipik Buhar Basınçlarında Minimum Exergy

| Basınç (bar) | Durum | T (°C) | h (kJ/kg) | s (kJ/(kg·K)) | ex_min (kJ/kg) |
|-------------|-------|--------|-----------|----------------|-----------------|
| 2 | Doymuş | 120.2 | 2.707 | 7.127 | 587 |
| 4 | Doymuş | 143.6 | 2.739 | 6.896 | 679 |
| 6 | Doymuş | 158.8 | 2.757 | 6.760 | 746 |
| 10 | Doymuş | 179.9 | 2.778 | 6.586 | 819 |
| 15 | Doymuş | 198.3 | 2.792 | 6.445 | 874 |
| 20 | Doymuş | 212.4 | 2.799 | 6.340 | 913 |
| 40 | Doymuş | 250.4 | 2.801 | 6.070 | 996 |
| 10 | Kızgın 300 °C | 300 | 3.052 | 7.124 | 935 |
| 40 | Kızgın 400 °C | 400 | 3.214 | 6.769 | 1.202 |

> **Anahtar Değer:** 10 bar doymuş buhar ≈ **819 kJ/kg** minimum exergy. Bu, proses boşluk analizinde en sık kullanılan referans noktasıdır.

### 2.3 Çözümlü Örnek

**Problem:** 8 ton/h, 10 bar doymuş buhar üreten kazan. Beslenme suyu 80 °C.

```
Buhar: h = 2778 kJ/kg, s = 6.586 kJ/(kg·K)
Ölü hal: h₀ = 104.9 kJ/kg, s₀ = 0.3672 kJ/(kg·K)
T₀ = 298.15 K

ex_buhar = (2778 − 104.9) − 298.15 × (6.586 − 0.3672)
         = 2673.1 − 1853.7
         = 819.4 kJ/kg

Beslenme suyu (80 °C): h_bw = 335 kJ/kg, s_bw = 1.075 kJ/(kg·K)
ex_bw = (335 − 104.9) − 298.15 × (1.075 − 0.3672) = 230.1 − 211.0 = 19.1 kJ/kg

Ex_min (net) = ṁ × (ex_buhar − ex_bw)
             = (8000/3600) × (819.4 − 19.1)
             = 2.222 × 800.3
             = 1778 kW
```

**Kaynak:** CoolProp steam tables; Kotas (1985), Tablo 2.1.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 SEC Aralıkları

| Alt-kategori | SEC (kJ_fuel/kg_buhar) | η_energy (LHV) | Not |
|-------------|------------------------|-----------------|-----|
| Doğal gaz kazanı (yoğuşmalı) | 2.700 – 2.900 | %92-98 | Latent ısı geri kazanımı |
| Doğal gaz kazanı (konvansiyonel) | 2.900 – 3.400 | %78-92 | Yaygın tesis tipi |
| Kömür kazanı | 3.200 – 4.000 | %70-86 | Kül ve kükürt etkisi |
| Atık ısı kazanı (HRSG) | 0 (atık ısı) | — | Yakıt tüketimi yok |

### 3.2 Exergy Verim Aralıkları

| Alt-kategori | η_ex Aralığı | Tipik η_ex |
|-------------|-------------|------------|
| Doğal gaz kazanı (en iyi) | %30 – %40 | %35 |
| Doğal gaz kazanı (tipik) | %25 – %35 | %30 |
| Kömür kazanı | %20 – %30 | %25 |
| HRSG | %45 – %65 | %55 |

### 3.3 Irreversibilite Payları

1. **Yanma:** %45 – %60 — Yakıtın kimyasal exergy'sinin yüksek sıcaklıkta termal exergy'ye dönüşümü
2. **Isı transferi (baca gazı → su/buhar):** %15 – %20 — Büyük ΔT (1200-1800 °C → 180-250 °C)
3. **Baca gazı çıkış kaybı:** %8 – %15 — Sıcak egzoz (120-250 °C)
4. **Blowdown kaybı:** %2 – %5 — TDS kontrolü için sıcak su atımı
5. **Yüzey ve radyasyon kaybı:** %2 – %4 — İzolasyon, sıcak noktalar
6. **Dağıtım hattı kaybı:** %3 – %8 — Kondenstop, izolasyon, kaçak

---

## 4. BAT Referansı

### 4.1 EU BREF LCP 2017

| Parametre | BAT Aralığı | Koşul |
|-----------|------------|-------|
| Kazan enerji verimi (doğal gaz) | %92 – %96 (LHV) | > 50 MW_th |
| Kazan enerji verimi (kömür) | %86 – %92 (LHV) | > 50 MW_th |
| Baca gazı sıcaklığı (doğal gaz) | 80 – 120 °C | Ekonomizer ile |
| Baca gazı sıcaklığı (kömür) | 120 – 160 °C | Asit çiğ noktası sınırı |
| O₂ fazlası (doğal gaz) | %1 – %3 | Otomatik kontrol |
| CO emisyonu (doğal gaz) | < 100 mg/Nm³ | BAT-AEL |

### 4.2 BAT Exergy Verimi (ExergyLab Hesabı)

| Buhar Koşulu | BAT η_energy | BAT η_ex | ESI_BAT |
|-------------|-------------|---------|---------|
| 10 bar doymuş, doğal gaz | %95 | %35-38 | 0.35-0.38 |
| 10 bar doymuş, kömür | %90 | %28-32 | 0.28-0.32 |
| 40 bar kızgın, doğal gaz | %94 | %38-42 | 0.38-0.42 |
| HRSG (atık ısıdan) | — | %50-60 | 0.50-0.60 |

### 4.3 Alt-kategoriler

| Alt-kategori | BAT SEC | BAT η_ex | Not |
|-------------|---------|---------|-----|
| Yoğuşmalı + ekonomizer + hava ön ısıtıcı | 2.750 kJ/kg | %36-40 | En iyi ticari paket |
| Oksijen zenginleştirilmiş yanma | — | %40-45 | Gelişen teknik |
| Flameless combustion | — | %42-48 | Gelişen teknik, R&D |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Yanma (kimyasal → termal) | 45 – 60 | Düşük (termodinamik sınır) |
| 2 | Isı transferi (baca gazı → su/buhar) | 15 – 20 | Orta (yüzey artırma, CHP) |
| 3 | Baca gazı kaybı | 8 – 15 | Yüksek (ekonomizer, air preheater) |
| 4 | Dağıtım kayıpları | 3 – 8 | Yüksek (izolasyon, trap bakımı) |
| 5 | Blowdown | 2 – 5 | Orta (flash steam geri kazanım) |
| 6 | Yüzey/radyasyon kaybı | 2 – 4 | Yüksek (izolasyon onarımı) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Ekonomizer** | %4-8 yakıt | 1-2 yıl | Baca gazı → beslenme suyu; her 20 °C ≈ %1 verim |
| 2 | **Kondens geri dönüşü artırma** | %5-15 yakıt + su | 0.5-1 yıl | %80→%95 kondens geri dönüşü büyük tasarruf |
| 3 | **Blowdown ısı geri kazanımı** | %1-3 yakıt | 1-2 yıl | Flash steam + ısı eşanjör |
| 4 | **Dağıtım hattı izolasyonu** | %3-8 kayıp azaltma | 0.5-1 yıl | Çıplak flanş, vana izolasyonu |
| 5 | **CHP dönüşümü** | %20-35 exergy | 3-7 yıl | Buhar türbini + jeneratör; en yüksek etki |

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER buhar basıncı < 5 bar (düşük basınç):
  → ESI > 0.30 "Düşük basınç buhar için iyi"
  → ESI < 0.20 "Düşük basınç buhar için zayıf — kazan verimi kontrol et"

EĞER buhar basıncı 5-20 bar (orta basınç):
  → ESI > 0.30 "Orta basınç buhar için iyi"
  → ESI < 0.25 "Orta basınç buhar için iyileştirme gerekli"

EĞER buhar basıncı > 20 bar (yüksek basınç):
  → ESI > 0.35 "Yüksek basınç buhar için iyi"
  → ESI < 0.28 "Yüksek basınç buhar için düşük"

EĞER CHP mevcut:
  → ESI > 0.40 "CHP sistemi etkin çalışıyor"
  → ESI < 0.30 "CHP avantajı yeterince kullanılamıyor"
```

### 7.2 Anahtar Karşılaştırma Noktaları

- **Baca gazı sıcaklığı:** < 120 °C (doğal gaz) veya < 160 °C (kömür) hedefle
- **Kondens geri dönüş oranı:** > %85 olmalı
- **Blowdown oranı:** < %5 TDS kontrolü ile
- **Dağıtım kaybı:** < %5 (iyi bakım ile %2-3 mümkün)

### 7.3 CHP Değerlendirmesi

Buhar prosesinde **her zaman** CHP potansiyelini değerlendir:
- Buhar basıncı > üretim gereksinimi + 5 bar → türbin yerleştir
- Buhar tüketimi > 5 ton/h ve sürekli → CHP fizibilitesi öner
- Detay için bkz. `process/chp.md`

---

## İlgili Dosyalar

- `factory/process/heating.md` — Isıtma prosesi (kazan exergy analizi)
- `factory/process/chp.md` — CHP/kojenerasyon prosesi
- `boiler/benchmarks.md` — Kazan ekipman benchmark
- `steam_turbine/systems/` — Buhar türbini CHP konfigürasyonları
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri

## Referanslar

1. European Commission, JRC (2017). *BAT Reference Document for Large Combustion Plants (LCP BREF)*. Ch. 3 — Boiler BAT-AELs.
2. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Buhar exergy tabloları.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Buhar üretim exergy analizi örnekleri.
4. Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis." *Energy*, 32(4), 249-253.
5. Spirax Sarco (2023). *Steam Engineering Tutorials*. — Kondens, blowdown, dağıtım kayıpları.
