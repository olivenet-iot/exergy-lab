---
title: "Kurutma Prosesi (Drying Process)"
category: factory
equipment_type: factory
keywords: [kurutma, drying, SEC, SMER, psikrometri, buharlaştırma, exergy, BAT, FDM BREF, Mujumdar]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/heating.md, dryer/benchmarks.md]
use_when: ["Kurutma prosesi exergy analizi yapılacakken", "Kurutucu performansı değerlendirilecekken", "Kurutma BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Kurutma Prosesi (Drying Process)

---

## 1. Proses Tanımı

### Nedir?
Kurutma, bir malzemeden nemi (genellikle suyu) termal enerji kullanarak uzaklaştırma prosesidir. Endüstriyel enerji tüketiminin %10-25'ini temsil eden, exergy açısından en verimsiz proseslerden biridir.

### Nerede Kullanılır?
- Gıda endüstrisi (tahıl, meyve, süt tozu, çay, baharat)
- Kağıt ve selüloz endüstrisi (kağıt kurutma)
- Tekstil (kumaş, iplik kurutma)
- Kimya endüstrisi (pigment, polimer, ilaç)
- Kereste ve ahşap endüstrisi
- Çimento endüstrisi (klinker kurutma)
- Madencilik (mineral kurutma)

### Kurutucu Tipleri

| Tip | Prensip | Tipik Uygulama | η_th Aralığı |
|-----|---------|----------------|-------------|
| Konveksiyonel (sıcak hava) | Sıcak hava sirküle | Tahıl, gıda, kimya | %25-60 |
| Tamburlu (rotary) | Dönen silindir + sıcak hava | Mineral, kum, çamur | %35-65 |
| Sprey (spray dryer) | Sıvı → ince damlacık + sıcak hava | Süt tozu, kahve, seramik | %20-50 |
| Akışkan yataklı (FBD) | Sıcak hava → akışkanlaşma | İlaç, kimya, gıda | %30-60 |
| İletkenli (contact/drum) | Sıcak yüzey teması | Kağıt, kimya | %40-70 |
| Kızılötesi (IR) | Radyasyon | İnce film, kaplama | %20-40 |
| Mikrodalga / RF | Dielektrik ısıtma | İlaç, gıda (niş) | %30-50 |
| Isı pompalı | Nemli hava → ısı pompası | Hassas gıda, kereste | %40-70 |

### Tipik Ölçek
- Küçük: 10 – 100 kg_su/h
- Orta: 100 – 1.000 kg_su/h
- Büyük: 1.000 – 50.000+ kg_su/h

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Suyu sıvı halden buharlaştırmak için minimum exergy:

$$ex_{min} = (h_v - h_0) - T_0 \times (s_v - s_0)$$

Burada:
- h_v: Su buharı entalpisi (100 °C, 1 atm) ≈ 2.676 kJ/kg
- h₀: Sıvı su entalpisi (25 °C) ≈ 104.9 kJ/kg
- s_v: Su buharı entropisi (100 °C, 1 atm) ≈ 7.355 kJ/(kg·K)
- s₀: Sıvı su entropisi (25 °C) ≈ 0.367 kJ/(kg·K)

```
ex_min = (2676 − 104.9) − 298.15 × (7.355 − 0.367)
       = 2571.1 − 2083.1
       = 488 kJ/kg_su
```

> **Ancak**, kurutma havadaki suyu uzaklaştırmaktır. Difüzyon ve bağlı nem için ek exergy gerekir. Pratik minimum:

**Serbest su kurutma (free moisture):**
$$ex_{min,free} ≈ 200 - 500 \text{ kJ/kg\_su}$$

**Bağlı su kurutma (bound moisture):**
$$ex_{min,bound} ≈ 500 - 2000 \text{ kJ/kg\_su (ürüne bağlı)}$$

### 2.2 Alternatif: Psikrometrik Minimum

Kurutma havası yaklaşımı:
$$ex_{min,psych} = (h_{hava,out} - h_{hava,in}) - T_0 \times (s_{hava,out} - s_{hava,in})$$

### 2.3 Çözümlü Örnek

**Problem:** 500 kg/h su uzaklaştıran konveksiyonel kurutucu, giriş havası 120 °C, çıkış 70 °C.

```
Serbest su buharlaştırma minimum exergy ≈ 400 kJ/kg_su (tahmini)
Ex_min = 500/3600 × 400 = 55.6 kW

Gerçek enerji tüketimi: SEC = 4.500 kJ/kg_su (tipik konveksiyonel)
Q_actual = 500/3600 × 4500 = 625 kW (termal)
Ex_actual = 625 × 1.04 = 650 kW (doğal gaz exergy)

ESI = 55.6 / 650 = 0.086 → Derece E
```

**Yorum:** Kurutma prosesi ESI = 0.086 ile E derecesinde. Kurutma için bu tipik bir değerdir — proses doğası gereği düşük exergy verimlidir.

**Kaynak:** Mujumdar (2015), Ch. 1; Dincer & Rosen (2013), Ch. 14.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 SEC (Specific Energy Consumption) Aralıkları

| Kurutucu Tipi | SEC Aralığı (kJ/kg_su) | Tipik SEC | Latent Isı Oranı |
|---------------|------------------------|-----------|------------------|
| Konveksiyonel (sıcak hava) | 4.000 – 8.000 | 5.000 | 2.5 – 3.5× |
| Tamburlu (rotary) | 3.500 – 6.000 | 4.500 | 1.5 – 2.5× |
| Sprey (spray) | 4.500 – 9.000 | 6.000 | 2.5 – 4.0× |
| Akışkan yataklı (FBD) | 3.000 – 6.000 | 4.000 | 1.5 – 2.5× |
| İletkenli (contact) | 2.500 – 4.500 | 3.500 | 1.0 – 2.0× |
| Isı pompalı | 1.000 – 2.500 | 1.800 | — |
| Mikrodalga / RF | 2.500 – 5.000 | 3.500 | — |

> **SMER** (Specific Moisture Extraction Rate): SMER = 1/SEC (kg_su/kJ veya kg_su/kWh). Yüksek SMER = daha verimli.

### 3.2 Exergy Verim Aralıkları

| Kurutucu Tipi | η_ex Aralığı | Tipik η_ex | ESI Aralığı |
|---------------|-------------|------------|-------------|
| Konveksiyonel | %5 – %15 | %10 | 0.05 – 0.12 |
| Tamburlu | %8 – %20 | %14 | 0.06 – 0.15 |
| Sprey | %3 – %12 | %8 | 0.03 – 0.10 |
| Akışkan yataklı | %8 – %18 | %12 | 0.06 – 0.14 |
| İletkenli | %12 – %25 | %18 | 0.10 – 0.20 |
| Isı pompalı | %20 – %35 | %25 | 0.15 – 0.25 |

### 3.3 Irreversibilite Kaynakları

1. **Yanma (ısı üretimi):** %35 – %50 — Yakıt → sıcak hava dönüşümü
2. **Isı transferi (hava → ürün):** %15 – %25 — Büyük ΔT
3. **Egzoz havası kaybı:** %15 – %30 — Sıcak, nemli hava atmosfere atılır
4. **Kütle transferi irreversibilitesi:** %5 – %10 — Nem difüzyonu
5. **Ürün aşırı kurutma:** %3 – %8 — Hedefin altına kurutma
6. **Radyasyon ve yüzey kaybı:** %2 – %5 — İzolasyon eksikliği

---

## 4. BAT Referansı

### 4.1 EU BREF FDM 2019 (Food, Drink and Milk)

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| SEC (sprey kurutma, süt tozu) | 3.500 – 5.500 kJ/kg_su | Çok kademeli, entegre |
| SEC (konveksiyonel, tahıl) | 3.000 – 4.500 kJ/kg_su | Isı geri kazanımlı |
| Egzoz geri kazanım oranı | > %30 | Isı eşanjör veya resirkülasyon |
| Nem kontrol doğruluğu | ±%0.5 | Online nem ölçüm + kontrol |

### 4.2 Genel Kurutma BAT (Mujumdar, 2015)

| Kurutucu Tipi | BAT SEC (kJ/kg_su) | BAT η_ex | Kaynak |
|---------------|---------------------|---------|--------|
| Konveksiyonel + ısı geri kazanım | 3.000 – 3.800 | %15-20 | FDM BREF + Mujumdar |
| Sprey + akışkan yatak hibrit | 3.500 – 4.500 | %12-18 | FDM BREF |
| Isı pompalı kurutucu | 1.200 – 2.000 | %25-35 | Literatür, tahmini |
| Süperkritik CO₂ kurutma | — | %30-40 | Gelişen teknik |
| Mikrodalga destekli | 2.000 – 3.000 | %18-25 | Literatür |

### 4.3 BAT ESI Değerleri

| Uygulama | BAT ESI | Mevcut Ortalama ESI | Boşluk |
|----------|---------|---------------------|--------|
| Gıda kurutma (genel) | 0.12 – 0.18 | 0.05 – 0.10 | %40-80 iyileştirme |
| Kağıt kurutma | 0.15 – 0.22 | 0.08 – 0.14 | %30-60 iyileştirme |
| Tekstil kurutma | 0.10 – 0.16 | 0.04 – 0.08 | %50-100 iyileştirme |
| Kereste kurutma | 0.12 – 0.20 | 0.06 – 0.12 | %40-70 iyileştirme |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Yanma / ısı üretimi | 35 – 50 | Düşük-orta (CHP, ısı pompası geçişi) |
| 2 | Egzoz havası kaybı | 15 – 30 | Çok yüksek (geri kazanım, resirkülasyon) |
| 3 | Isı transferi ΔT | 15 – 25 | Orta (daha düşük T, daha uzun süre) |
| 4 | Kütle transferi | 5 – 10 | Düşük (proses doğası) |
| 5 | Aşırı kurutma | 3 – 8 | Yüksek (online nem kontrol) |
| 6 | Yüzey/izolasyon kaybı | 2 – 5 | Yüksek (izolasyon) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Egzoz havası ısı geri kazanımı** | %15-30 enerji | 1-3 yıl | Hava-hava eşanjör veya kısmi resirkülasyon; en büyük etki |
| 2 | **Isı pompalı kurutucu** | %40-65 enerji | 3-5 yıl | SEC < 2.000 kJ/kg_su; düşük T uygulamalar için ideal |
| 3 | **Çok kademeli kurutma** | %15-25 enerji | 2-4 yıl | Ön kurutma (mekanik) + son kurutma (termal) |
| 4 | **Online nem kontrol** | %5-15 enerji | 1-2 yıl | Aşırı kurutmayı önle; ürün kalitesi de artar |
| 5 | **Mekanik ön nem alma** | %20-40 termal yük | 1-3 yıl | Pres, santrifüj — mekanik enerji ile nem azaltma |

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER kurutma prosesi (genel):
  → ESI > 0.15 "Kurutma için çok iyi — ısı pompalı veya entegre sistem"
  → ESI 0.08-0.15 "Kurutma için iyi — BAT yakınında"
  → ESI 0.04-0.08 "Kurutma için orta — tipik konveksiyonel"
  → ESI < 0.04 "Kurutma için zayıf — acil iyileştirme gerekli"
```

> **Önemli:** Kurutma ESI'si doğası gereği çok düşüktür (%3-25). ESI A-F skalasında genellikle E-F aralığında kalır. Bu normal! Proses bazlı değerlendirme kullan.

### 7.2 SEC Bazlı Hızlı Değerlendirme

| SEC (kJ/kg_su) | Değerlendirme |
|-----------------|---------------|
| < 3.000 | Mükemmel — ısı pompalı veya ileri sistem |
| 3.000 – 4.500 | İyi — BAT seviyesinde |
| 4.500 – 6.000 | Orta — iyileştirme fırsatları var |
| 6.000 – 8.000 | Zayıf — ısı geri kazanım eksik |
| > 8.000 | Kritik — kapsamlı dönüşüm gerekli |

### 7.3 Özel Durumlar

```
EĞER egzoz sıcaklığı > 100 °C:
  → "Yüksek egzoz sıcaklığı — ısı geri kazanım potansiyeli yüksek"
  → "Her 20 °C düşüş ≈ %5-8 enerji tasarrufu"

EĞER SEC > 2.5 × latent ısı (2.257 kJ/kg):
  → "SEC, buharlaştırma enerjisinin 2.5 katından fazla"
  → "Ciddi termal verimsizlik — egzoz, izolasyon, kontrol incele"

EĞER ısı pompası uygulanabilir (T < 80 °C):
  → "Isı pompalı kurutma ile SEC %40-65 azaltılabilir"
  → "Ürün kalitesi de genellikle artar (düşük T)"
```

---

## İlgili Dosyalar

- `dryer/benchmarks.md` — Kurutucu ekipman benchmark
- `factory/process/heating.md` — Isıtma prosesi (kurutucu ısı kaynağı)
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi
- `factory/heat_integration.md` — Isı entegrasyonu (egzoz → proses)
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanım

## Referanslar

1. European Commission, JRC (2019). *BAT Reference Document for the Food, Drink and Milk Industries (FDM BREF)*. Ch. 5 — Drying operations.
2. Mujumdar, A.S. (2015). *Handbook of Industrial Drying*. 4th ed., CRC Press. — SEC tabloları ve kurutucu seçimi.
3. Kemp, I.C. (2012). "Fundamentals of energy analysis of dryers." In *Modern Drying Technology*, Wiley.
4. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Kurutma exergy analizi (Ch. 14).
5. Aghbashlo, M. et al. (2013). "A review of exergy analysis of drying processes." *Drying Technology*, 31(10), 1156-1170.
