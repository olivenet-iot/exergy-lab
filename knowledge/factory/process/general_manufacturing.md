---
title: "Genel Üretim Prosesleri (General Manufacturing Processes)"
category: factory
equipment_type: factory
keywords: [üretim, manufacturing, çimento, cam, kağıt, şeker, exergy, BAT, BREF, endüstriyel proses]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/heating.md, factory/process/drying.md, factory/process/steam_generation.md]
use_when: ["Spesifik üretim prosesi exergy analizi yapılacakken", "Sektörel üretim BAT karşılaştırması gerektiğinde", "Çimento/cam/kağıt/şeker prosesi değerlendirilecekken"]
priority: medium
last_updated: 2026-02-08
---

# Genel Üretim Prosesleri (General Manufacturing Processes)

Bu dosya, ExergyLab'da sıklıkla karşılaşılan enerji-yoğun üretim sektörlerinin exergy profilini, BAT referanslarını ve ESI değerlendirme kurallarını içerir. Her alt-bölüm bağımsız bir sektörü kapsar.

---

## 1. Çimento Üretimi (Cement Manufacturing)

### 1.1 Proses Tanımı
Çimento üretimi, hammaddelerin (kireçtaşı, kil) yüksek sıcaklıkta (~1450 °C) sinterleştirilmesi (klinker) ve öğütülmesi sürecidir. Enerji yoğun: 3.0 – 5.5 GJ/ton klinker.

### 1.2 Minimum Exergy
Klinker oluşumu için teorik minimum:
$$ex_{min,klinker} ≈ 1.700 \text{ kJ/kg\_klinker (tahmini)}$$

Bu değer, CaO oluşumu kalsinasyon reaksiyonundan gelir:
CaCO₃ → Cite + CO₂, ΔH ≈ 1.780 kJ/kg CaCO₃

> **Not:** Exergy minimum hesabı, reaksiyon Gibbs serbest enerjisine dayalıdır ve koşullara göre değişir. Verilen değer tahminidir, doğrulama gerekli.

### 1.3 BAT Referansı — EU BREF CLM 2013

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Klinker termal enerji | 3.000 – 3.400 MJ/ton klinker | Kuru proses, ön kalsinasyonlu |
| Elektrik tüketimi | 90 – 110 kWh/ton çimento | Öğütme dahil |
| CO₂ emisyonu | 0.55 – 0.70 t CO₂/t çimento | BAT-AEL |

### 1.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %15 – %30 | %25-30 |
| ESI | 0.10 – 0.25 | 0.20-0.25 |
| Ana kayıp | Yanma (%40) + radyasyon/soğutma (%25) | — |

### 1.5 İyileştirme Stratejileri
1. **Klinker soğutma ısı geri kazanımı:** %5-10 yakıt tasarrufu (1-3 yıl ROI)
2. **Ön kalsinasyon ile atık yakıt:** %15-30 birincil yakıt azaltma (2-5 yıl ROI)
3. **Atık ısı elektrik üretimi (ORC/Kalina):** 10-30 kWh/ton klinker (3-6 yıl ROI)
4. **Yüksek verimli öğütücüler (VRM):** %20-30 elektrik tasarrufu (2-4 yıl ROI)
5. **Çimentoda SCM kullanımı:** Klinker oranı azaltma → exergy/ton çimento düşer

### 1.6 Yorumlama Kuralı
```
EĞER çimento tesisi:
  → ESI > 0.20 "Çimento için iyi — modern kuru proses"
  → ESI 0.12-0.20 "Çimento için orta — iyileştirme potansiyeli var"
  → ESI < 0.12 "Çimento için düşük — yaş proses veya eski teknoloji"
```

---

## 2. Cam Üretimi (Glass Manufacturing)

### 2.1 Proses Tanımı
Cam üretimi, silika (SiO₂) ve diğer hammaddelerin yüksek sıcaklıkta (~1500-1600 °C) eritilmesi, şekillendirilmesi ve tavlanması sürecidir.

### 2.2 Minimum Exergy
Cam eritme minimum exergy (teorik):
$$ex_{min,cam} ≈ 2.500 - 3.000 \text{ kJ/kg cam (tahmini, doğrulama gerekli)}$$

### 2.3 BAT Referansı — EU BREF GLS 2012

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Eritme enerjisi (float cam) | 5.000 – 6.500 MJ/ton cam | Rejeneratif fırın |
| Eritme enerjisi (şişe camı) | 3.500 – 5.000 MJ/ton cam | Oxy-fuel veya rejeneratif |
| Elektrik tüketimi | 100 – 200 kWh/ton cam | İşleme dahil |

### 2.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %10 – %25 | %20-25 |
| ESI | 0.08 – 0.20 | 0.15-0.20 |
| Ana kayıp | Yanma (%35) + fırın duvarı/radyasyon (%30) + egzoz (%15) | — |

### 2.5 İyileştirme Stratejileri
1. **Rejeneratif/rekuperatif fırın:** %15-25 yakıt tasarrufu (5-10 yıl ROI)
2. **Oxy-fuel yakma:** %10-20 yakıt tasarrufu + emisyon azaltma (5-8 yıl ROI)
3. **Cullet (kırık cam) oranı artırma:** Her %10 cullet ≈ %2.5 enerji tasarrufu
4. **Atık ısı geri kazanımı (batch preheating):** %5-15 tasarruf (3-5 yıl ROI)
5. **Elektrik boosting:** Hibrit eritme, kısmi elektrikleştirme (3-6 yıl ROI)

### 2.6 Yorumlama Kuralı
```
EĞER cam tesisi:
  → ESI > 0.18 "Cam için iyi — modern rejeneratif veya oxy-fuel"
  → ESI 0.10-0.18 "Cam için orta"
  → ESI < 0.10 "Cam için düşük — fırın teknolojisi eski"
```

---

## 3. Kağıt Üretimi (Pulp and Paper Manufacturing)

### 3.1 Proses Tanımı
Kağıt üretimi, selüloz liflerinin hamur haline getirilmesi (pulping), temizlenmesi, kağıt makinesinde şekillendirilmesi ve kurutulması sürecidir. Buhar ve elektrik yoğun; CHP yaygın.

### 3.2 Minimum Exergy
Kağıt kurutma baskın:
$$ex_{min,kağıt} ≈ 3.000 - 5.000 \text{ kJ/kg kuru kağıt (tahmini, ürüne bağlı)}$$

(Büyük kısmı su uzaklaştırma — bkz. `drying.md`)

### 3.3 BAT Referansı — EU BREF PP 2015

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Toplam enerji (entegre tesis) | 10 – 20 GJ/ton kağıt | Ürüne bağlı |
| Buhar tüketimi | 4 – 10 ton buhar/ton kağıt | Kurutma baskın |
| Elektrik tüketimi | 400 – 800 kWh/ton kağıt | Öğütme + makineler |
| CHP kullanımı | Yaygın (genellikle buhar türbini) | BAT olarak tanımlı |

### 3.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %15 – %30 | %25-30 |
| ESI | 0.12 – 0.28 | 0.22-0.28 |
| Ana kayıp | Kurutma (%40) + hamur hazırlama (%20) + kazan (%20) | — |

### 3.5 İyileştirme Stratejileri
1. **Mekanik ön su alma (pres verim artırma):** %10-20 buhar tasarrufu (2-4 yıl ROI)
2. **Buhar ve kondens geri dönüşü optimizasyonu:** %5-15 buhar (1-2 yıl ROI)
3. **CHP optimizasyonu (buhar türbini):** %5-10 birincil enerji (3-5 yıl ROI)
4. **Pinch analizi ile ısı entegrasyonu:** %10-25 termal enerji (2-5 yıl ROI)
5. **Hood egzoz ısı geri kazanımı:** %5-12 kurutma enerjisi (2-3 yıl ROI)

### 3.6 Yorumlama Kuralı
```
EĞER kağıt tesisi:
  → ESI > 0.25 "Kağıt için iyi — entegre ve CHP'li tesis"
  → ESI 0.15-0.25 "Kağıt için orta — ısı entegrasyon fırsatları var"
  → ESI < 0.15 "Kağıt için düşük — kurutma ve CHP incele"
```

---

## 4. Şeker Üretimi (Sugar Manufacturing)

### 4.1 Proses Tanımı
Şeker üretimi, şeker pancarı veya kamışından şeker kristallerinin çıkarılması sürecidir. Buhar yoğun: difüzyon, evaporasyon (çok kademeli), kristalizasyon, kurutma.

### 4.2 Minimum Exergy
Evaporasyon baskın:
$$ex_{min,şeker} ≈ 3.000 - 6.000 \text{ kJ/kg şeker (tahmini, hammaddeye bağlı)}$$

### 4.3 BAT Referansı — EU BREF FDM 2019

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Termal enerji (pancar) | 8 – 14 GJ/ton şeker | Çok kademeli evaporasyon |
| Elektrik | 100 – 200 kWh/ton şeker | CHP ile kendi üretimi |
| CHP kullanımı | Standart (buhar türbini) | BAT olarak tanımlı |

### 4.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %12 – %25 | %20-25 |
| ESI | 0.10 – 0.22 | 0.18-0.22 |
| Ana kayıp | Evaporasyon (%35) + kazan (%30) + kurutma (%15) | — |

### 4.5 İyileştirme Stratejileri
1. **Çok kademeli evaporasyon (5+ kademe):** %15-30 buhar tasarrufu (3-5 yıl ROI)
2. **Termal buhar sıkıştırma (MVR/TVR):** %20-40 buhar tasarrufu (3-6 yıl ROI)
3. **Pinch analizi:** %10-25 termal enerji (2-4 yıl ROI)
4. **CHP optimizasyonu:** %5-15 birincil enerji (3-5 yıl ROI)
5. **Biyokütle yakma (pancar posası):** %30-50 dış yakıt azaltma (2-4 yıl ROI)

### 4.6 Yorumlama Kuralı
```
EĞER şeker tesisi:
  → ESI > 0.20 "Şeker için iyi — çok kademeli ve CHP entegre"
  → ESI 0.12-0.20 "Şeker için orta — evaporasyon optimizasyonu gerekli"
  → ESI < 0.12 "Şeker için düşük — MVR ve pinch analizi değerlendir"
```

---

## 5. Sektörler Arası Karşılaştırma

### 5.1 ESI Karşılaştırma Tablosu

| Sektör | Tipik ESI | BAT ESI | Ana Exergy Kaybı |
|--------|-----------|---------|-------------------|
| Çimento | 0.10 – 0.25 | 0.20-0.25 | Yanma + radyasyon |
| Cam | 0.08 – 0.20 | 0.15-0.20 | Yanma + fırın duvarı |
| Kağıt | 0.12 – 0.28 | 0.22-0.28 | Kurutma + hamur |
| Şeker | 0.10 – 0.22 | 0.18-0.22 | Evaporasyon + kazan |

### 5.2 Ortak İyileştirme Fırsatları

Tüm üretim sektörlerinde geçerli:
1. **Atık ısı geri kazanımı** — Baca gazı, soğutma, proses egzozu
2. **CHP entegrasyonu** — Buhar ihtiyacı olan her tesis
3. **Pinch analizi** — Karmaşık ısı akışları olan tesisler
4. **VFD uygulamaları** — Fan, pompa, kompresörlerde
5. **İzolasyon iyileştirmesi** — Yüksek sıcaklık ekipmanları

---

## 6. Genel Yorumlama Rehberi (AI Kullanımı İçin)

### 6.1 Sektör Belirleme

```
EĞER sektör bilgisi var:
  → İlgili alt-bölümdeki ESI skalasını kullan
  → Sektörel BAT referansı ile karşılaştır

EĞER sektör bilinmiyor AMA üretim tesisi:
  → Genel ESI skalasını kullan (sustainability_index.md)
  → "Sektörel BAT karşılaştırması için sektör bilgisi gerekli" notu ekle
```

### 6.2 Çapraz Proses Değerlendirme

Bir üretim tesisinde birden fazla proses varsa:
1. Her prosesi ayrı ESI ile değerlendir
2. En düşük ESI'li prosesi öncelikli hedef olarak belirle
3. Exergy yıkım payına göre sırala
4. Prosesler arası entegrasyon fırsatlarını ara (pinch analizi)

### 6.3 BAT Değer Güvenilirliği

| Sektör | BAT Kaynak | Güvenilirlik | Not |
|--------|-----------|-------------|-----|
| Çimento | BREF CLM 2013 | B — Güvenilir | Exergy dönüşümü tahmini |
| Cam | BREF GLS 2012 | B — Güvenilir | Exergy dönüşümü tahmini |
| Kağıt | BREF PP 2015 | B — Güvenilir | Geniş ürün yelpazesi |
| Şeker | BREF FDM 2019 | B — Güvenilir | Bölgesel farklar var |

---

## İlgili Dosyalar

- `factory/process/heating.md` — Isıtma prosesi (tüm sektörlerde mevcut)
- `factory/process/drying.md` — Kurutma prosesi (kağıt, gıda, çimento)
- `factory/process/steam_generation.md` — Buhar üretimi (tüm sektörlerde)
- `factory/process/chp.md` — CHP (kağıt, şeker, kimya)
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi
- `factory/sector_cement.md` — Çimento sektörü detayları
- `factory/sector_paper.md` — Kağıt sektörü detayları
- `factory/sector_food.md` — Gıda sektörü detayları

## Referanslar

1. European Commission, JRC (2013). *BAT Reference Document for the Production of Cement, Lime and Magnesium Oxide (CLM BREF)*.
2. European Commission, JRC (2012). *BAT Reference Document for the Manufacture of Glass (GLS BREF)*.
3. European Commission, JRC (2015). *BAT Reference Document for the Production of Pulp, Paper and Board (PP BREF)*.
4. European Commission, JRC (2019). *BAT Reference Document for the Food, Drink and Milk Industries (FDM BREF)*.
5. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
6. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier.
7. Szargut, J., Morris, D.R. & Steward, F.R. (1988). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*. Hemisphere.
