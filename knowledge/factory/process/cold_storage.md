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

### 2.2b Termal Yük Hesabı Detayı — 2.000 m³ Depo Örneği

**Problem:** 2.000 m³ donmuş gıda deposu (−20 °C), dış sıcaklık T₀ = 35 °C.

**Depo boyutları:** 20m × 10m × 10m (uzunluk × genişlik × yükseklik)

**Bileşen 1: Duvar ısı kazancı (Q_duvar)**
```
Toplam dış yüzey alanı:
  Duvarlar: 2 × (20×10 + 10×10) = 600 m²
  Tavan: 20×10 = 200 m²
  Taban: 20×10 = 200 m² (ısıtmalı — don önleme)
  Toplam: 1.000 m²

İzolasyon: 150 mm PUR, U = 0.15 W/(m²·K)
ΔT = 35 − (−20) = 55 °C

Q_duvar = U × A × ΔT = 0.15 × 1000 × 55 = 8.250 W = 8.25 kW
```

**Bileşen 2: Ürün yükü (Q_ürün)**
```
Günlük ürün girişi: 20 ton (−5 °C'den −20 °C'ye dondurma)
Spesifik ısı (donmuş gıda): 1.8 kJ/(kg·K)
ΔT = −5 − (−20) = 15 °C

Q_ürün = 20.000 × 1.8 × 15 / (24×3600) = 6.25 kW
```

**Bileşen 3: İnfiltrasyon (Q_inf)**
```
Kapı açılma: 20 kez/gün, her biri 2 dakika, kapı boyutu 3m × 3m
Hava değişim katsayısı: 0.05 m³/(m²·s·açık)
Hava entalpisi farkı: Δh ≈ 85 kJ/kg (35°C doymuş → −20°C)

Q_inf ≈ kapı_alanı × katsayı × Δh × ρ × açık_süre / toplam_süre
      ≈ 9 × 0.05 × 85 × 1.2 × (20×120)/(86400)
      ≈ 9 × 0.05 × 85 × 1.2 × 0.028
      ≈ 1.29 kW (ortalama)

Hızlı kapı ve hava perdesi ile: Q_inf ≈ 0.65 kW (%50 azaltma)
```

**Bileşen 4: İç yükler (Q_iç)**
```
Aydınlatma: 5 W/m² × 200 m² = 1.0 kW (LED, hareket sensörlü)
Forklift: 2 adet × 3 kW = 6.0 kW (elektrikli)
Personel: 3 kişi × 0.27 kW = 0.81 kW

Q_iç = 1.0 + 6.0 + 0.81 = 7.81 kW
```

**Bileşen 5: Defrost (Q_def)**
```
Defrost sıklığı: 4 kez/gün, her biri 20 dakika
Defrost güç: 3 kW/evaporatör × 4 evaporatör = 12 kW
Ek soğutma yükü: 12 × (4 × 20/60) / 24 = 0.67 kW (ortalama)
```

**Toplam termal yük:**

| Bileşen | kW | % |
|---------|-----|---|
| Duvar ısı kazancı | 8.25 | 35.1% |
| İnfiltrasyon (hızlı kapı ile) | 0.65 | 2.8% |
| Ürün yükü | 6.25 | 26.6% |
| İç yükler | 7.81 | 33.2% |
| Defrost | 0.67 | 2.9% |
| Güvenlik faktörü (%10) | 2.36 | — |
| **Toplam** | **26.0 kW** | **100%** |

**Exergy hesabı:**
```
Ex_min = 26.0 × (308.15/253.15 − 1) = 26.0 × 0.217 = 5.64 kW

COP (NH₃/CO₂ kaskad, −20 °C) = 2.2
W_actual = 26.0 / 2.2 = 11.8 kW

ESI = 5.64 / 11.8 = 0.478 → Derece B
```

> **Gözlem:** Küçük depo (2000 m³) ile büyük depo (20.000+ m³) arasında hacim/yüzey oranı farkı nedeniyle SEC (kWh/m³·yıl) büyük depoda daha düşüktür (ölçek etkisi).

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

### 2.4 Çözümlü Örnek: Çok Sıcaklıklı Depo

**Problem:** 3 bölmeli soğuk depo:
- Bölme A: +2 °C, 80 kW soğutma yükü (taze meyve)
- Bölme B: −20 °C, 120 kW (donmuş gıda)
- Bölme C: −35 °C, 40 kW (dondurma, balık)
- T₀ = 35 °C

```
Bölme A (+2 °C = 275.15 K):
  Ex_min_A = 80 × (308.15/275.15 − 1) = 80 × 0.120 = 9.6 kW
  COP_A (NH₃, tek kademe) = 4.5
  W_A = 80/4.5 = 17.8 kW, ESI_A = 9.6/17.8 = 0.539

Bölme B (−20 °C = 253.15 K):
  Ex_min_B = 120 × (308.15/253.15 − 1) = 120 × 0.217 = 26.0 kW
  COP_B (NH₃/CO₂ kaskad) = 2.0
  W_B = 120/2.0 = 60.0 kW, ESI_B = 26.0/60.0 = 0.433

Bölme C (−35 °C = 238.15 K):
  Ex_min_C = 40 × (308.15/238.15 − 1) = 40 × 0.294 = 11.8 kW
  COP_C (NH₃, çift kademe) = 1.3
  W_C = 40/1.3 = 30.8 kW, ESI_C = 11.8/30.8 = 0.383

Toplam:
  Ex_min_toplam = 9.6 + 26.0 + 11.8 = 47.4 kW
  W_toplam = 17.8 + 60.0 + 30.8 = 108.6 kW
  ESI_depo = 47.4 / 108.6 = 0.436 → Derece B

Ağırlıklı ESI = Σ(ESI_i × W_i) / Σ(W_i)
             = (0.539×17.8 + 0.433×60 + 0.383×30.8) / 108.6
             = (9.59 + 25.98 + 11.80) / 108.6 = 0.436
```

**Yorum:**
- Toplam ESI = 0.436 (Derece B) -- iyi tasarlanmis cok sicaklikli depo
- En dusuk ESI Bolme C (−35 °C, 0.383) -- derin dondurma en zorlu
- **Kaskad avantaji:** NH₃/CO₂ kaskad, tek kademeli yerine COP'u %30-50 artirir
- **Ortak kondenser:** Tum bolmeler ortak evaporatif kondenser kullanarak verimlilik kazanir

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

## 4b. Soğutucu Akışkan Karşılaştırma Tablosu (Soğuk Depo İçin)

| Soğutucu | GWP | COP (+2°C) | COP (−20°C) | COP (−35°C) | Avantaj | Dezavantaj |
|----------|-----|-----------|-------------|-------------|---------|------------|
| R717 (NH₃) | 0 | 5.0-5.5 | 1.8-2.5 | 1.0-1.5 | En yüksek COP, düşük maliyet | Toksik, güvenlik gereksinimleri |
| R744 (CO₂) | 1 | 3.5-4.5 | 1.5-2.0 | 1.0-1.5 | Güvenli, düşük T için iyi | Transkritik, yüksek basınç |
| NH₃/CO₂ kaskad | 0/1 | 5.0-5.5 | 2.0-2.8 | 1.5-2.0 | En iyi COP düşük T'de | Karmaşık, yüksek ilk maliyet |
| R404A | 3922 | 3.5-4.0 | 1.2-1.8 | 0.8-1.2 | Basit, yaygın | Yüksek GWP → kaldırılıyor |
| R449A (HFO karışım) | 1397 | 3.3-3.8 | 1.1-1.6 | 0.7-1.0 | R404A drop-in alternatifi | Hala yüksek GWP |
| R290 (propan) | 3 | 4.2-5.0 | 1.3-1.8 | 0.9-1.3 | Doğal, iyi COP | Yanıcı, şarj sınırı |

### Exergy Perspektifi — Soğutucu Seçiminin ESI Etkisi

| Senaryo (−20 °C, 500 kW) | COP | W (kW) | ESI | Yıllık Enerji (MWh) | CO₂ (ton/yıl) |
|---------------------------|-----|--------|-----|---------------------|----------------|
| R404A (eski sistem) | 1.3 | 385 | 0.282 | 3.080 | 1.355 |
| R449A (drop-in) | 1.5 | 333 | 0.326 | 2.667 | 1.173 |
| NH₃ vidalı | 2.0 | 250 | 0.434 | 2.000 | 0.880 |
| NH₃/CO₂ kaskad | 2.4 | 208 | 0.521 | 1.667 | 0.733 |

> **Engine değeri:** bat_references.py → cold_storage/general: exergy_efficiency_pct = 32%. NH₃/CO₂ kaskad ile %52 ulaşılabilir. Literatür aralığı: %28-55.

---

## 4c. ASHRAE ve Soğuk Zincir Standartları

### 4c.1 ASHRAE Handbook — Refrigeration (2022)

| Bölüm | Konu | ExergyLab İlgisi |
|-------|------|------------------|
| Ch. 1 | Halokarbon soğutma sistemleri | Chiller COP referansları |
| Ch. 2 | NH₃ soğutma sistemleri | Endüstriyel soğuk depo tasarımı |
| Ch. 3 | CO₂ soğutma sistemleri | Transkritik ve kaskad |
| Ch. 23 | Perakende gıda mağazası soğutma | Ticari soğutma SEC |
| Ch. 24 | Soğuk depo tesisleri | Termal yük, izolasyon, kapı |
| Ch. 25 | Gıda dondurma | Dondurma hızı ve kalitesi |

### 4c.2 Soğuk Zincir Düzenlemeleri

| Düzenleme | Sıcaklık Gereksinimi | Kapsam |
|-----------|---------------------|--------|
| ATP (Uluslararası) | Sınıf C: <7°C, F: <-18°C | Uluslararası taşımacılık |
| EU 853/2004 | Taze et: 0-4°C, Donmuş: <-18°C | AB gıda güvenliği |
| Türk Gıda Kodeksi | Taze: 0-4°C, Donmuş: <-18°C | Ulusal mevzuat |
| İlaç GDP | 2-8°C (çoğu ilaç) | İlaç dağıtım |

### 4c.3 Çok Sıcaklıklı Depo Tasarım Yaklaşımları

| Yaklaşım | Açıklama | Exergy Avantajı | Dezavantaj |
|----------|----------|-----------------|------------|
| Ayrı sistem | Her bölme bağımsız kompresör | Basit, yedekli | Düşük verim, yüksek maliyet |
| Kaskad | Yüksek T (NH₃) + düşük T (CO₂) | En iyi COP | Karmaşık |
| Çok basınçlı | Tek kompresör, çok evaporatör | Orta verim | Kontrol zor |
| Merkezi + VFD | Büyük merkezi kompresör | Ölçek avantajı | Tek nokta arızası |

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
| 6 | **Ekonomizer (ara soğutma)** | %5-12 enerji | 2-3 yıl | Flash gas ayrıştırma, ara basınç soğutma |
| 7 | **Atık ısı geri kazanımı** | %8-15 enerji | 1-3 yıl | Kondenser atık ısısı → sıcak su, taban ısıtma |
| 8 | **İzolasyon yenileme** | %5-15 enerji | 3-7 yıl | Eski panel değişimi, soğuk köprü giderme |

### 6.1 Detaylı Strateji Açıklamaları

#### 6.1.1 NH₃/CO₂ Kaskad Sistem Dönüşümü

Kaskad sistem, iki ayrı soğutma çevrimini seri bağlayarak çalışır:

```
Yüksek kademe (NH₃):
  Evaporatör: −5 °C ile −10 °C (kaskad ısı eşanjörü)
  Kondenser: +35 °C ile +40 °C (evaporatif)
  Basınç oranı: ~4:1

Düşük kademe (CO₂):
  Evaporatör: −25 °C ile −35 °C (depo)
  Kondenser: −5 °C ile −10 °C (kaskad ısı eşanjörü)
  Basınç oranı: ~3:1

Toplam basınç oranı iki kademeye bölünür → her kompresör verimli çalışır
```

**Maliyet analizi (500 kW soğutma kapasitesi):**

| Kalem | R404A Mevcut | NH₃/CO₂ Kaskad |
|-------|-------------|----------------|
| Kompresör gücü | 385 kW | 208 kW |
| Yıllık enerji | 3.080 MWh | 1.667 MWh |
| Enerji maliyeti (0.12 EUR/kWh) | 369.600 EUR | 200.000 EUR |
| Yıllık tasarruf | — | 169.600 EUR |
| Yatırım maliyeti | — | 450.000-600.000 EUR |
| Basit geri ödeme | — | 2.7-3.5 yıl |

#### 6.1.2 Kapı Yönetimi Detayı

| Çözüm | İnfiltrasyon Azaltma | Maliyet | Not |
|-------|---------------------|---------|-----|
| Hızlı kapı (high-speed door) | %40-60 | 5.000-15.000 EUR | Açılma hızı > 1 m/s |
| Hava perdesi (air curtain) | %60-80 | 3.000-10.000 EUR | Kapı üstü, yüksek hızlı hava jeti |
| Dock shelter | %70-90 | 8.000-20.000 EUR | Kamyon yükleme noktası |
| Çift kapı (air-lock) | %80-95 | 15.000-30.000 EUR | İki kapı arası tampon bölge |
| Şerit perde (strip curtain) | %20-40 | 500-2.000 EUR | Basit, düşük maliyetli |

**Exergy etkisi hesabı:**
```
Tipik donmuş depo (−20 °C), 4 kapı, günde 80 açılma:
  İnfiltrasyon yükü (şerit perde): 12 kW → Ex_inf = 12 × 0.217 = 2.6 kW
  İnfiltrasyon yükü (hızlı kapı + hava perdesi): 3 kW → Ex_inf = 0.65 kW
  Exergy tasarrufu: 1.95 kW sürekli → 17.1 MWh_ex/yıl
```

#### 6.1.3 Defrost Optimizasyonu

| Defrost Tipi | Verimlilik | Süre | Exergy Etkisi |
|-------------|-----------|------|---------------|
| Elektrik rezistans | Düşük | 20-30 dk | Yüksek ek yük |
| Sıcak gaz (hot gas) | Orta-Yüksek | 10-15 dk | Atık ısı kullanımı |
| Tersine çevrim (reverse cycle) | Yüksek | 8-12 dk | En az ek enerji |
| Talep bazlı kontrol | Ek %15-25 tasarruf | Değişken | Gereksiz defrost önlenir |

**Talep bazlı defrost:**
```
Sensörler: Evaporatör yüzey sıcaklığı + basınç farkı
Tetikleme: ΔT_evap > 3°C veya ΔP_hava > 50 Pa
Avantaj: Gereksiz defrost döngüsü önlenir
Tasarruf: Defrost enerjisi %30-50 azalır, defrost kaynaklı yük %40-60 azalır
```

#### 6.1.4 Atık Isı Geri Kazanımı

Kompresör kondenser atık ısısı değerli bir kaynak:

```
Tipik NH₃ sistemi (200 kW kompresör):
  Kondenser atık ısısı: ~250-280 kW (soğutma yükü + kompresör işi)
  Deşarj gazı sıcaklığı: 80-120 °C (desuperheating bölgesi)
  Kullanılabilir ısı (desuperheater): 40-60 kW @ 60-80 °C

Kullanım alanları:
  1. Taban ısıtma (don önleme): 5-15 kW
  2. Ofis/sosyal alan ısıtma: 10-20 kW
  3. Sıcak su üretimi: 15-30 kW
  4. Defrost için sıcak su: 5-10 kW
```

| Geri kazanım | Yıllık tasarruf | ROI |
|-------------|----------------|-----|
| Desuperheater → sıcak su | 15.000-25.000 EUR | 1-2 yıl |
| Taban ısıtma entegrasyonu | 5.000-10.000 EUR | 2-3 yıl |
| Bina ısıtma | 10.000-20.000 EUR | 1.5-3 yıl |

---

## 6b. Termal Enerji Depolama (Cold TES)

### 6b.1 Buz Depolama

Gece (düşük elektrik tarifesi) buz üret, gündüz soğutma yükünü karşıla:

| Parametre | Değer |
|-----------|-------|
| Depolama kapasitesi | 334 kJ/kg (buz erime entalpisi) |
| Şarj sıcaklığı | −5 °C ile −10 °C |
| Deşarj sıcaklığı | 0-4 °C |
| Exergy yoğunluğu | ~10-15 kJ/kg (düşük Carnot) |
| Maliyet avantajı | %20-40 elektrik maliyeti azaltma |

### 6b.2 Eutectic Depolama

| Parametre | PCM (faz değişim malzemesi) |
|-----------|----------------------------|
| Sıcaklık aralığı | −25 °C ile +8 °C (malzemeye bağlı) |
| Uygulama | Soğuk zincir taşımacılığı |
| Avantaj | Sabit sıcaklık, uzun süre |
| Exergy notu | Düşük T depolama → düşük exergy, ama amaç sıcaklık kontrolü |

### 6b.3 Cold TES Exergy Analizi

```
Buz depolama exergy yoğunluğu:
  T_buz = 273.15 K, T₀ = 308.15 K
  ex_buz = 334 × (1 − 308.15/273.15) = 334 × (−0.128) → |ex| = 42.8 kJ/kg

  Gerçekte: Şarj COP < Deşarj COP → round-trip exergy verimi %50-65

Eutectic (−21 °C):
  T_eut = 252.15 K, T₀ = 308.15 K
  Erime entalpisi (tipik tuz-su): ~250 kJ/kg
  ex_eut = 250 × (1 − 308.15/252.15) = 250 × (−0.222) → |ex| = 55.5 kJ/kg
```

**Maliyet-exergy karşılaştırması:**

| TES Tipi | Exergy Yoğunluğu (kJ/kg) | Maliyet (EUR/kWh_th) | Ömür (yıl) |
|----------|--------------------------|---------------------|------------|
| Buz tankı | 42.8 | 15-30 | 20+ |
| Eutectic plaka (−21 °C) | 55.5 | 40-80 | 10-15 |
| Soğuk su tankı (+4 °C) | 8.4 | 5-15 | 25+ |

---

## 6c. Enerji Denetimi Kontrol Listesi (Soğuk Depo)

### 6c.1 Hızlı Değerlendirme (Quick Audit)

| # | Kontrol Noktası | Ölçüm | Hedef |
|---|----------------|-------|-------|
| 1 | Depo iç sıcaklığı kararlılığı | ΔT < ±2°C | Stabil, aşırı dalgalanma yok |
| 2 | Evaporatör buz birikimi | Görsel kontrol | Temiz yüzey, düzenli defrost |
| 3 | Kondenser temizliği | ΔT_kondenser | < 5°C tasarım değerinden sapma |
| 4 | Kapı contası durumu | Görsel + kağıt testi | Sızdırmazlık tam |
| 5 | İzolasyon yüzey sıcaklığı | IR termometre | Soğuk nokta yok (thermal bridge) |
| 6 | Kompresör çalışma saatleri | SCADA/log | %70-85 yük faktörü |
| 7 | Aydınlatma durumu | Görsel | LED, hareket sensörlü |
| 8 | Hava perdesi çalışması | Anemometre | Hız > 8 m/s kapı düzleminde |

### 6c.2 Detaylı Exergy Denetimi

```
Adım 1: Enerji faturaları analizi (son 12 ay)
  → SEC hesapla: kWh/(m³·yıl)
  → Mevsimsel trend: yaz/kış oranı

Adım 2: Termal yük profili
  → Her bileşeni ölç veya hesapla (duvar, ürün, infiltrasyon, iç, defrost)
  → En büyük bileşeni belirle

Adım 3: Sistem COP ölçümü
  → Kompresör güç ölçümü (kW) + soğutma kapasitesi (kW)
  → Gerçek COP vs tasarım COP karşılaştırması

Adım 4: Exergy analizi
  → Ex_min hesapla (termal yük × Carnot faktörü)
  → ESI = Ex_min / W_actual
  → BAT ile karşılaştır

Adım 5: İyileştirme önceliklendirme
  → En yüksek exergy yıkım kaynağı → önce iyileştir
  → ROI sıralaması yap
```

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

EĞER SEC > 120 kWh/(m³·yıl) (donmuş depo):
  → "Yüksek SEC — izolasyon yaşlanması, kapı sızıntısı veya düşük COP"
  → "Termal yük dağılımını analiz et"

EĞER kondenser ΔT > 8°C (tasarımdan sapma):
  → "Kondenser kirli veya yetersiz kapasite"
  → "Temizlik ve bakım öncelikli"

EĞER evaporatör defrost sıklığı > 6 kez/gün:
  → "Aşırı defrost — evaporatör boyutlandırma veya hava sirkülasyonu sorunu"
```

### 7.4 Sektörel ESI Kıyaslama

| Sektör | Tipik ESI | En İyi ESI | Ana Fark Kaynağı |
|--------|----------|-----------|-----------------|
| Gıda dağıtım (multi-temp) | 0.30-0.40 | 0.50+ | Kaskad sistem, VFD |
| Et işleme | 0.25-0.35 | 0.45 | Yüksek infiltrasyon yükü |
| Dondurulmuş gıda üretimi | 0.20-0.30 | 0.40 | Ürün yükü baskın |
| İlaç deposu (+2-8°C) | 0.35-0.50 | 0.60+ | Yüksek T, kolay COP |
| Balık/deniz ürünleri (−35°C) | 0.15-0.25 | 0.35 | Çok düşük T, zorlayıcı |

### 7.5 Ölçek Etkisi (Scale Effect)

```
Küçük depo (< 1.000 m³):
  → Hacim/yüzey oranı düşük → izolasyon kaybı oranı yüksek
  → SEC: 80-150 kWh/(m³·yıl) (donmuş)
  → Tipik ESI: 0.20-0.30

Orta depo (1.000-10.000 m³):
  → Denge noktası
  → SEC: 50-90 kWh/(m³·yıl) (donmuş)
  → Tipik ESI: 0.30-0.40

Büyük depo (> 10.000 m³):
  → Hacim/yüzey oranı yüksek → verimli
  → SEC: 30-60 kWh/(m³·yıl) (donmuş)
  → Tipik ESI: 0.35-0.50
  → Merkezi NH₃ sistemi + ekonomizer + atık ısı geri kazanımı avantajı
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
6. ASHRAE (2022). *ASHRAE Handbook — Refrigeration*. Ch. 23-25 — Soğuk depo ve gıda dondurma.
7. GCCA — Global Cold Chain Alliance (2020). *Cold Storage Construction Guide*. — Tasarım standartları.
8. EU Regulation 517/2014 on Fluorinated Greenhouse Gases. — Soğutucu akışkan GWP sınırlamaları.
9. ATP — Agreement on International Carriage of Perishable Foodstuffs (2022). — Uluslararası soğuk taşımacılık.
10. Pearson, A. (2008). "Refrigeration with ammonia." *Int. J. Refrigeration*, 31(4), 545-551.
11. Sawalha, S. et al. (2017). "Investigation of NH₃/CO₂ cascade system for supermarket refrigeration." *Int. J. Refrigeration*, 73, 211-221. — Kaskad sistem performansı.
