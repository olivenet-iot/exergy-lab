---
title: "Soğuk Depolama Prosesi (Cold Storage Process)"
category: factory
equipment_type: factory
keywords: [soğuk depolama, cold storage, dondurma, derin dondurma, COP, enerji tüketimi, izolasyon, buharlaşma sıcaklığı]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/cooling.md, chiller/benchmarks.md]
use_when: ["Soğuk depolama prosesi exergy analizi yapılacakken", "Depo enerji performansı değerlendirilecekken", "Soğuk depo BAT karşılaştırması gerektiğinde"]
priority: medium
last_updated: 2026-02-08
---

# Soğuk Depolama Prosesi (Cold Storage Process)

---

## 1. Proses Tanımı

### Nedir?
Soğuk depolama, bozulabilir ürünlerin (gıda, ilaç, kimyasal) belirli sıcaklık aralıklarında uzun süreli muhafazası için sürekli soğutma sağlama prosesidir. Soğutma prosesinden farkı: sürekli termal yük yönetimi, yüksek izolasyon gereksinimleri ve sıcaklık katmanlama (tiering).

### Nerede Kullanılır?
- Gıda soğuk zincirleri (lojistik, market, üretim)
- İlaç depoları (2-8 °C, kontrollü)
- Mezbaha ve et işleme tesisleri
- Dondurulmuş gıda üretimi ve depolama
- Tarımsal ürün soğuk depoları

### 3 Sıcaklık Katmanı

| Katman | Sıcaklık Aralığı | Tipik Ürünler | Evaporatör T |
|--------|-------------------|---------------|-------------|
| **Soğuk** | 0 °C – +5 °C | Taze meyve, süt, ilaç | −5 °C ile −8 °C |
| **Donmuş** | −18 °C – −22 °C | Dondurulmuş gıda, et | −25 °C ile −28 °C |
| **Derin Dondurma** | −28 °C – −35 °C | Dondurma, balık, özel gıda | −35 °C ile −40 °C |

### İlgili Ekipmanlar
- Soğutma kompresörleri (vidalı, pistonlu, kademeli)
- Evaporatörler (statik, fan-coil, plaka)
- Kondenserler (evaporatif, hava soğutmalı)
- Soğutucu akışkan (NH₃, R404A, R744/CO₂)
- İzolasyon panelleri (PUR/PIR, 80-250 mm)
- Kapı sistemleri (hızlı kapı, hava perdesi, dock shelter)

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Soğuk depolama için sürekli exergy gereksinimi, depo termal yüküne bağlıdır:

$$Ex_{min} = Q_{yük} \times \left(\frac{T_0}{T_{depo}} - 1\right)$$

Depo termal yükü bileşenleri:
$$Q_{yük} = Q_{duvar} + Q_{ürün} + Q_{infiltrasyon} + Q_{iç\_yük} + Q_{defrost}$$

| Bileşen | Açıklama | Tipik Pay |
|---------|----------|-----------|
| Q_duvar | İzolasyon üzerinden ısı kazancı | %30 – %50 |
| Q_ürün | Ürün soğutma/dondurma yükü | %15 – %30 |
| Q_infiltrasyon | Kapı açılma, hava sızıntısı | %15 – %25 |
| Q_iç_yük | Aydınlatma, forklift, personel | %5 – %15 |
| Q_defrost | Evaporatör buz çözme | %5 – %10 |

### 2.2 Katman Bazlı Minimum Exergy (T₀ = 35 °C = 308.15 K)

| Katman | T_depo (K) | (T₀/T_depo − 1) | Ex_min/kW_soğutma | COP_Carnot |
|--------|-----------|-----------------|-------------------|------------|
| Soğuk (+2 °C) | 275.15 | 0.120 | 0.120 kW_ex/kW_th | 8.34 |
| Donmuş (−20 °C) | 253.15 | 0.217 | 0.217 kW_ex/kW_th | 4.60 |
| Derin dondurma (−30 °C) | 243.15 | 0.267 | 0.267 kW_ex/kW_th | 3.74 |

### 2.3 Çözümlü Örnek

**Problem:** 1.000 m³ donmuş gıda deposu (−20 °C), toplam termal yük 80 kW, T₀ = 35 °C.

```
T_depo = −20 + 273.15 = 253.15 K
T₀ = 308.15 K

Ex_min = 80 × (308.15/253.15 − 1) = 80 × 0.217 = 17.4 kW

COP_Carnot = 253.15 / (308.15 − 253.15) = 253.15 / 55 = 4.60
COP_actual (tipik vidalı, NH₃) = 2.0

W_actual = 80 / 2.0 = 40 kW

ESI = Ex_min / W_actual = 17.4 / 40 = 0.435 → Derece B
```

**Kaynak:** ASHRAE Refrigeration Handbook; IIR Guidelines.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 Spesifik Enerji Tüketimi (SEC)

| Katman | SEC Aralığı | Birim | Not |
|--------|------------|-------|-----|
| Soğuk (+2 °C) | 15 – 40 | kWh/(m³·yıl) | Depo boyutu ve doluluk bağımlı |
| Donmuş (−20 °C) | 40 – 100 | kWh/(m³·yıl) | COP düşüklüğü + izolasyon yükü |
| Derin dondurma (−30 °C) | 80 – 180 | kWh/(m³·yıl) | Çift kademeli kompresör gerekli |

### 3.2 COP Aralıkları (Soğuk Depo Sistemleri)

| Sistem | COP (+2 °C) | COP (−20 °C) | COP (−30 °C) |
|--------|-------------|-------------|-------------|
| NH₃ vidalı + evaporatif kondenser | 4.0 – 5.5 | 1.8 – 2.5 | 1.2 – 1.8 |
| R404A vidalı + hava soğutmalı | 3.0 – 4.0 | 1.2 – 1.8 | 0.8 – 1.2 |
| CO₂ transkritik | 3.5 – 5.0 | 1.5 – 2.2 | 1.0 – 1.5 |
| NH₃/CO₂ kaskad | 4.0 – 5.5 | 2.0 – 2.8 | 1.5 – 2.0 |

### 3.3 Irreversibilite Kaynakları (Donmuş Depo)

1. **Kompresör irreversibilitesi:** %35 – %45 — Yüksek basınç oranı
2. **Kondenser ΔT:** %15 – %20 — Sıcak gaz → soğutma ortamı
3. **Evaporatör ΔT:** %10 – %15 — Soğutucu → depo havası
4. **Genleşme valfi:** %5 – %10 — Flash gas kaybı
5. **Defrost kayıpları:** %5 – %8 — Buz çözme ısısı → tekrar soğutma
6. **İnfiltrasyon:** %5 – %10 — Kapı açılma kayıpları

---

## 4. BAT Referansı

### 4.1 EU BREF ICS 2001 + BREF FDM 2019

| Parametre | BAT Değeri | Kaynak |
|-----------|-----------|--------|
| İzolasyon kalınlığı (−20 °C) | ≥ 150 mm PUR/PIR | ICS BREF, FDM BREF |
| İzolasyon kalınlığı (−30 °C) | ≥ 200 mm PUR/PIR | Mühendislik pratiği |
| Kapı yönetimi | Hızlı kapılar + hava perdesi | FDM BREF |
| Soğutucu akışkan | NH₃ veya CO₂ (düşük GWP) | F-gas Regulation |
| LED aydınlatma + hareket sensörü | Standart | Enerji verimliliği |

### 4.2 BAT COP ve ESI Değerleri

| Katman | BAT COP | BAT ESI | Kaynak |
|--------|---------|---------|--------|
| Soğuk (+2 °C) | 5.0 – 5.5 | 0.40 – 0.55 | ASHRAE + exergy hesabı |
| Donmuş (−20 °C) | 2.2 – 2.8 | 0.35 – 0.50 | NH₃/CO₂ kaskad referans |
| Derin dondurma (−30 °C) | 1.5 – 2.0 | 0.30 – 0.45 | Çift kademeli NH₃ referans |

### 4.3 İzolasyon U-Değeri Hedefleri

| Eleman | BAT U-değeri (W/(m²·K)) | Not |
|--------|--------------------------|-----|
| Duvar paneli (−20 °C) | < 0.15 | 150 mm PUR |
| Tavan | < 0.12 | 180-200 mm PUR |
| Taban | < 0.20 | Isıtmalı taban (don önleme) |
| Kapı | < 0.50 | Yalıtımlı hızlı kapı |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Kompresör (yüksek basınç oranı) | 35 – 45 | Orta (kaskad, kademeli sıkıştırma) |
| 2 | Kondenser ΔT | 15 – 20 | Yüksek (evaporatif kondenser bakımı) |
| 3 | Evaporatör ΔT + defrost | 10 – 18 | Orta (defrost optimizasyonu) |
| 4 | İnfiltrasyon (kapı açılma) | 5 – 10 | Yüksek (hızlı kapı, hava perdesi) |
| 5 | İzolasyon yaşlanması | 3 – 8 | Orta (panel yenileme) |
| 6 | Genleşme valfi | 5 – 8 | Düşük (ekonomizer) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **NH₃/CO₂ kaskad sistem** | %15-25 enerji | 3-5 yıl | Düşük sıcaklıklarda tek kademeli yerine; COP artışı |
| 2 | **Kapı yönetimi iyileştirme** | %8-15 enerji | 0.5-2 yıl | Hızlı kapılar, hava perdeleri, dock shelter |
| 3 | **Defrost optimizasyonu** | %5-10 enerji | 0.5-1 yıl | Zamanlayıcı → talep tabanlı defrost; sıcak gaz defrost |
| 4 | **Evaporatif kondenser** | %10-20 enerji | 2-4 yıl | Hava soğutmalı → evaporatif; kondenser sıcaklığı düşer |
| 5 | **Değişken hız kontrol** | %10-20 enerji | 2-3 yıl | Kompresör + kondenser fan + evaporatör fan VFD |

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER Soğuk depo (+2 °C):
  → ESI > 0.40 "Soğuk depo için çok iyi"
  → ESI 0.25-0.40 "İyi — izolasyon ve COP kontrol et"
  → ESI < 0.25 "Düşük — infiltrasyon ve kompresör verimi incele"

EĞER Donmuş depo (−20 °C):
  → ESI > 0.35 "Donmuş depo için çok iyi"
  → ESI 0.20-0.35 "İyi — kademeli sıkıştırma ve izolasyon kontrol et"
  → ESI < 0.20 "Düşük — kapsamlı sistem analizi gerekli"

EĞER Derin dondurma (−30 °C):
  → ESI > 0.30 "Derin dondurma için iyi"
  → ESI 0.15-0.30 "Kabul edilebilir — kaskad sistem değerlendir"
  → ESI < 0.15 "Zayıf — sistem yenileme gerekli"
```

### 7.2 Anahtar Kontrol Noktaları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| COP (−20 °C, NH₃) | > 2.5 | 1.8-2.5 | < 1.8 |
| İzolasyon U (−20 °C) | < 0.15 | 0.15-0.25 | > 0.25 |
| İnfiltrasyon payı | < %8 | %8-15 | > %15 |
| Defrost sıklığı | Talep bazlı | Zamanlayıcı | Sürekli |

### 7.3 Özel Durumlar

```
EĞER birden fazla sıcaklık katmanı var:
  → "Kaskad veya çift kademeli sistem avantajı değerlendir"
  → "Her katmanı ayrı ESI ile değerlendir"

EĞER depo doluluk oranı < %50:
  → "Düşük doluluk — SEC artışı beklenir, ESI geçici olarak düşük olabilir"

EĞER R404A kullanılıyor:
  → "Yüksek GWP soğutucu — NH₃ veya CO₂'ye geçiş planla (F-gas Regulation)"
```

---

## İlgili Dosyalar

- `factory/process/cooling.md` — Soğutma prosesi (genel)
- `chiller/benchmarks.md` — Chiller ekipman benchmark
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi
- `factory/process/sustainability_index.md` — ESI derecelendirme

## Referanslar

1. European Commission, JRC (2001). *Reference Document — Industrial Cooling Systems (ICS BREF)*.
2. European Commission, JRC (2019). *BAT Reference Document for the Food, Drink and Milk Industries (FDM BREF)*.
3. ASHRAE (2022). *ASHRAE Handbook — Refrigeration*. Ch. 23-24 — Cold Storage.
4. International Institute of Refrigeration — IIR (2019). *Guide to Cold Storage Design*.
5. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Soğutma depolama exergy analizi.
