---
title: "Isıtma Prosesi (Heating Process)"
category: factory
equipment_type: factory
keywords: [ısıtma, heating, kazan, brülör, exergy verimi, yanma, BAT, LCP BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/steam_generation.md, factory/process/chp.md, boiler/benchmarks.md]
use_when: ["Isıtma prosesi exergy analizi yapılacakken", "Kazan/brülör performansı değerlendirilecekken", "Isıtma BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Isıtma Prosesi (Heating Process)

---

## 1. Proses Tanımı

### Nedir?
Isıtma prosesi, bir enerji kaynağından (yakıt, elektrik, buhar) alınan enerjiyi bir akışkana (su, hava, yağ, proses akışkanı) veya malzemeye ısı olarak aktarma işlemidir.

### Nerede Kullanılır?
- Proses ısıtma (gıda, kimya, tekstil, kağıt)
- Bina ısıtma (endüstriyel tesisler)
- Ön ısıtma (beslenme suyu, yanma havası)
- Isıl işlem (metal, seramik)

### İlgili Ekipmanlar
- Kazanlar (ateş tüplü, su borulu)
- Brülörler (gaz, sıvı yakıt)
- Elektrik ısıtıcılar (dirençli, indüksiyon)
- Isı eşanjörleri (geri kazanım için)
- Termik yağ sistemleri

### Tipik Ölçek
- Küçük: 50 – 500 kW termal
- Orta: 500 kW – 5 MW termal
- Büyük: 5 – 50+ MW termal

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Isı transferi ile yapılan ısıtma prosesi için minimum exergy gereksinimi:

$$Ex_{min} = Q \times \left(1 - \frac{T_0}{T_h}\right)$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| Q | Aktarılan ısı miktarı | kW |
| T₀ | Çevre (ölü hal) sıcaklığı | K |
| T_h | Isıtılan akışkanın ortalama sıcaklığı | K |

### 2.2 Varsayımlar
- Kararlı hal (steady-state) koşulları
- Sabit T_h (ortalama logaritmik sıcaklık kullanılabilir)
- T₀ = 298.15 K (25 °C) referans sıcaklığı
- Minimum exergy, Carnot faktörüne dayalıdır

### 2.3 Sıcaklığa Bağlı Carnot Faktörü

| T_h (°C) | T_h (K) | Carnot Faktörü (1−T₀/T_h) | Ex_min / Q |
|-----------|---------|---------------------------|------------|
| 60 | 333 | 0.105 | %10.5 |
| 100 | 373 | 0.201 | %20.1 |
| 150 | 423 | 0.295 | %29.5 |
| 200 | 473 | 0.370 | %37.0 |
| 400 | 673 | 0.557 | %55.7 |
| 800 | 1073 | 0.722 | %72.2 |
| 1200 | 1473 | 0.798 | %79.8 |

> **Kritik Bilgi:** Düşük sıcaklık ısıtma (60-100 °C) termodinamik olarak çok az exergy gerektirir. Bu proseslerde yüksek kaliteli yakıt (doğal gaz, exergy/enerji ≈ 1.04) kullanmak büyük exergy yıkımına yol açar.

### 2.4 Çözümlü Örnek

**Problem:** 2.000 kW termal kapasiteli, 180 °C'de proses ısıtma yapan bir sistem.

```
T_h = 180 + 273.15 = 453.15 K
T₀ = 298.15 K

Ex_min = 2000 × (1 − 298.15/453.15)
       = 2000 × (1 − 0.658)
       = 2000 × 0.342
       = 684 kW

(Termodinamik olarak bu ısıtma işi 684 kW exergy ile yapılabilir)
```

**Kaynak:** Kotas (1985), Bölüm 2; Dincer & Rosen (2013), Bölüm 3.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 SEC (Specific Exergy Consumption) Aralıkları

| Alt-kategori | SEC Aralığı | Birim | Not |
|-------------|-------------|-------|-----|
| Doğal gaz kazanı (yoğuşmalı) | 1.05 – 1.15 | kW_ex / kW_th | η_energy %95-105 (LHV) |
| Doğal gaz kazanı (konvansiyonel) | 1.10 – 1.30 | kW_ex / kW_th | η_energy %82-94 |
| Kömür kazanı | 1.20 – 1.60 | kW_ex / kW_th | η_energy %70-88 |
| Fuel oil kazanı | 1.15 – 1.40 | kW_ex / kW_th | η_energy %80-90 |
| Elektrikli ısıtıcı | 1.00 – 1.05 | kW_ex / kW_th | η_energy ~%98-100 |

### 3.2 Exergy Verim Aralıkları

| Alt-kategori | η_ex Aralığı | Tipik η_ex | Not |
|-------------|-------------|------------|-----|
| Düşük sıcaklık ısıtma (60-100 °C) | %5 – %15 | %10 | Carnot faktörü çok düşük |
| Orta sıcaklık ısıtma (100-250 °C) | %15 – %35 | %25 | Tipik proses ısıtma |
| Yüksek sıcaklık ısıtma (250-600 °C) | %25 – %50 | %35 | Isıl işlem, kurutma |
| Çok yüksek sıcaklık (600+ °C) | %30 – %55 | %40 | Fırınlar, refrakter |

### 3.3 Irreversibilite Kaynakları ve Payları

1. **Yanma irreversibilitesi:** %50 – %65 (baskın kaynak)
2. **Isı transferi ΔT:** %15 – %25 (baca gazı – proses akışkanı)
3. **Baca gazı kayıpları:** %8 – %15 (sıcak egzoz gazları)
4. **Yüzey kayıpları:** %3 – %8 (izolasyon yetersizliği)
5. **Kısmi yük kaybı:** %2 – %5 (değişken yüklerde)

---

## 4. BAT Referansı

### 4.1 EU BREF LCP 2017 (Large Combustion Plants)

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Kazan enerji verimi (doğal gaz) | %92 – %96 (LHV) | Yeni tesis |
| Kazan enerji verimi (kömür) | %86 – %92 (LHV) | Yeni tesis |
| Baca gazı sıcaklığı | 80 – 160 °C | Yakıt tipine bağlı |
| Hava fazlası oranı | %3 – %6 O₂ | Doğal gaz |

### 4.2 EU BREF ENE 2009 (Energy Efficiency)

| Parametre | BAT Değeri | Not |
|-----------|-----------|-----|
| Isı geri kazanım oranı | > %70 | Atık ısı → proses |
| İzolasyon yüzey sıcaklığı | < 40 °C | Dış yüzey |
| Ekonomizer uygulaması | Zorunlu (50+ °C düşüş) | Baca gazı geri kazanım |

### 4.3 BAT Exergy Verimi (ExergyLab Hesabı)

| Isıtma Tipi | BAT η_energy | BAT η_ex | Kaynak |
|-------------|-------------|---------|--------|
| Düşük sıcaklık (80 °C) | %96 | %12-15 | LCP BREF 2017 + exergy dönüşüm |
| Orta sıcaklık (200 °C) | %94 | %30-35 | LCP BREF 2017 + exergy dönüşüm |
| Yüksek sıcaklık (500 °C) | %90 | %40-50 | LCP BREF 2017 + exergy dönüşüm |

### 4.4 Alt-kategoriler

| Alt-kategori | BAT SEC (enerji) | BAT η_ex | Not |
|-------------|------------------|---------|-----|
| Yoğuşmalı kazan (doğal gaz) | 1.04 kW_fuel/kW_th | %30-38 | En iyi ticari teknoloji |
| Modüler kazan sistemi | 1.06 kW_fuel/kW_th | %28-36 | Kısmi yük avantajı |
| Atık ısı geri kazanım + kazan | 0.85 kW_fuel/kW_th | %35-45 | Entegre sistem |
| Isı pompası destekli | 0.30 kW_el/kW_th | %40-60 | T < 80 °C için en iyi |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | Açıklama |
|------|--------|---------|----------|
| 1 | Yanma | 50 – 65 | Kimyasal exergy → termal exergy dönüşümü |
| 2 | Isı transferi ΔT | 15 – 25 | Alev/baca gazı → proses akışkanı sıcaklık farkı |
| 3 | Baca gazı çıkışı | 8 – 15 | Sıcak gaz atmosfere atılıyor |
| 4 | Yüzey kayıpları | 3 – 8 | Yetersiz izolasyon, sıcak noktalar |
| 5 | Yakıt hazırlama | 1 – 3 | Atomizasyon, karışım |

> **Not:** Yanma irreversibilitesi termodinamik olarak kaçınılmazdır (UN); ancak hava ön ısıtma, oksijen zenginleştirme ve kademeli yakma ile kısmen azaltılabilir.

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Ekonomizer (baca gazı geri kazanım)** | %5-12 yakıt | 1-2 yıl | Baca gazı → beslenme suyu ön ısıtma; her 20 °C düşüş ≈ %1 verim artışı |
| 2 | **Hava ön ısıtıcı** | %3-8 yakıt | 2-3 yıl | Baca gazı → yanma havası; özellikle kömür ve fuel oil kazanlarında etkili |
| 3 | **Yoğuşmalı kazan dönüşümü** | %10-15 yakıt | 3-5 yıl | Doğal gaz kazanlarında su buharı latent ısısını geri kazanır |
| 4 | **Isı pompası entegrasyonu** | %40-60 exergy | 3-5 yıl | T < 80 °C ısıtmada; COP 3-5 ile exergy verimi dramatik artar |
| 5 | **Modüler kazan sistemi** | %5-10 yakıt | 2-4 yıl | Kısmi yüklerde birden fazla küçük kazan → daha yüksek verimlilik |

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER ısıtma sıcaklığı < 100 °C:
  → "Düşük sıcaklık ısıtma prosesi — exergy verimi doğası gereği düşüktür"
  → "Isı pompası alternatifini mutlaka değerlendir"
  → ESI > 0.10 ise "Düşük sıcaklık ısıtma için iyi"

EĞER ısıtma sıcaklığı 100-250 °C:
  → ESI < 0.20 ise "Orta sıcaklık ısıtma için düşük, iyileştirme gerekli"
  → ESI > 0.30 ise "Orta sıcaklık ısıtma için iyi"

EĞER ısıtma sıcaklığı > 250 °C:
  → ESI < 0.30 ise "Yüksek sıcaklık ısıtma için düşük"
  → ESI > 0.40 ise "Yüksek sıcaklık ısıtma için çok iyi"
```

### 7.2 Anahtar Karşılaştırma Noktaları

- Aynı sıcaklık seviyesi için **ısı pompası vs kazan** exergy karşılaştırması yap
- **Baca gazı sıcaklığı > 200 °C** → ekonomizer veya ön ısıtıcı eksik
- **Hava fazlası > %8 O₂** → yanma kontrolü yetersiz
- **Yüzey sıcaklığı > 60 °C** → izolasyon yetersiz

### 7.3 Benchmark Referansları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| Kazan exergy verimi | > %35 | %25-35 | < %25 |
| Baca gazı sıcaklığı | < 120 °C | 120-200 °C | > 200 °C |
| Hava fazlası (O₂) | < %4 | %4-7 | > %7 |
| Yüzey kaybı | < %2 | %2-5 | > %5 |

---

## İlgili Dosyalar

- `factory/process/steam_generation.md` — Buhar üretim prosesi (ısıtmanın özel hali)
- `factory/process/chp.md` — CHP/kojenerasyon (ısı + elektrik birlikte)
- `boiler/benchmarks.md` — Kazan ekipman seviyesi benchmark
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri
- `factory/heat_integration.md` — Isı entegrasyonu fırsatları

## Referanslar

1. European Commission, JRC (2017). *BAT Reference Document for Large Combustion Plants (LCP BREF)*. BAT Conclusions — Boiler Efficiency.
2. European Commission, JRC (2009). *Reference Document on Best Available Techniques for Energy Efficiency (ENE BREF)*.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Isıtma exergy analizi.
4. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
5. Rant, Z. (1956). "Exergie, ein neues Wort für technische Arbeitsfähigkeit." *Forschung auf dem Gebiet des Ingenieurwesens*, 22(1), 36-37.
