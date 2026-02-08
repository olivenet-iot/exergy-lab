---
title: "Exergy Sürdürülebilirlik İndeksi — ESI (Exergy Sustainability Index)"
category: factory
equipment_type: factory
keywords: [ESI, sürdürülebilirlik indeksi, exergy sustainability index, derecelendirme, A-F skala, proses performansı]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/bat_overview.md, factory/process/index.md]
use_when: ["ESI skoru yorumlanacakken", "Proses performans derecelendirmesi yapılacakken", "Sektörel ESI karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Exergy Sürdürülebilirlik İndeksi — ESI (Exergy Sustainability Index)

Bu dosya, ExergyLab'ın proses seviyesi performans değerlendirmesinde kullandığı **Exergy Sürdürülebilirlik İndeksi** (ESI) derecelendirme sistemini tanımlar.

---

## 1. ESI Tanımı

### 1.1 Formül

$$ESI = \frac{Ex_{min}}{Ex_{actual}}$$

| Terim | Tanım | Birim |
|-------|-------|-------|
| Ex_min | Termodinamik minimum exergy gereksinimi | kW veya kJ/kg |
| Ex_actual | Gerçek exergy tüketimi | kW veya kJ/kg |

### 1.2 Fiziksel Anlam

ESI, bir prosesin termodinamik olarak mümkün olan en düşük exergy tüketiminin, gerçek tüketime oranıdır:

- **ESI = 1.0**: Tersinir (reversible) proses — pratik olarak ulaşılamaz
- **ESI = 0.5**: Proseste minimum gereksinimin 2 katı exergy tüketiliyor
- **ESI = 0.1**: Proseste minimum gereksinimin 10 katı exergy tüketiliyor
- **ESI → 0**: Neredeyse tüm exergy yıkılıyor

### 1.3 ESI vs Exergy Verimi

| Metrik | Tanım | Aralık | Kullanım |
|--------|-------|--------|----------|
| ESI | Ex_min / Ex_actual | 0 – 1 | Proses seviyesi termodinamik sınıra uzaklık |
| η_ex | Ex_product / Ex_fuel | 0 – 1 | Ekipman seviyesi exergy dönüşüm verimi |

> **Fark:** ESI, prosesin "ne kadar exergy tüketmesi gerektiğini" baz alır. η_ex ise "tüketilen exergy'nin ne kadarının ürüne aktarıldığını" ölçer. Düşük sıcaklık ısıtma proseslerinde ESI << η_ex olabilir.

---

## 2. ESI Derecelendirme Tablosu

### 2.1 A-F Skalası

| Derece | ESI Aralığı | Anlam | Aksiyon |
|--------|-------------|-------|---------|
| **A** | > 0.50 | Dünya sınıfı (World-class) | İnce ayar, en iyi uygulamaları koru |
| **B** | 0.35 – 0.50 | Çok iyi, BAT yakınında | Spesifik iyileştirmeler, bakım optimizasyonu |
| **C** | 0.20 – 0.35 | İyi, ciddi iyileştirme fırsatları | Sistematik analiz, orta ölçekli yatırımlar |
| **D** | 0.10 – 0.20 | Ortalama, ciddi potansiyel | Acil aksiyon planı, teknoloji değerlendirmesi |
| **E** | 0.05 – 0.10 | Zayıf, acil iyileştirme gerekli | Kapsamlı modernizasyon programı |
| **F** | < 0.05 | Kritik, büyük dönüşüm gerekli | Temel tasarım değişikliği, süreç yeniden mühendisliği |

### 2.2 Renk Kodlaması (Frontend İçin)

| Derece | Renk | Hex Kodu | Tailwind Sınıfı |
|--------|------|----------|------------------|
| A | Koyu yeşil | #059669 | `text-emerald-600` |
| B | Yeşil | #10B981 | `text-emerald-500` |
| C | Sarı | #F59E0B | `text-amber-500` |
| D | Turuncu | #F97316 | `text-orange-500` |
| E | Kırmızı | #EF4444 | `text-red-500` |
| F | Koyu kırmızı | #DC2626 | `text-red-600` |

---

## 3. Sektörel / Proses Tipik ESI Değerleri

### 3.1 Proses Bazlı Tipik Aralıklar

| Proses | Tipik ESI | Tipik Derece | Açıklama |
|--------|-----------|-------------|----------|
| Basınçlı hava üretimi | 0.05 – 0.15 | E – D | İzotermik sıkıştırma çok uzak |
| Isıtma (kazan) | 0.15 – 0.35 | D – C | Yanma irreversibilitesi yüksek |
| Buhar üretimi | 0.20 – 0.35 | D – C | Kazan + dağıtım kayıpları |
| Soğutma (chiller) | 0.10 – 0.30 | D – C | Ters Carnot'dan uzaklık |
| Soğuk depolama | 0.08 – 0.20 | E – D | Düşük T → düşük Carnot COP |
| Kurutma | 0.03 – 0.15 | F – D | Çok düşük exergy verimli proses |
| CHP / Kojenerasyon | 0.25 – 0.45 | C – B | Elektrik + ısı birlikte üretim |
| Çimento fırını | 0.10 – 0.25 | D – C | Yüksek sıcaklık, yüksek kayıp |
| Cam eritme | 0.08 – 0.20 | E – D | Radyasyon ve soğutma kayıpları |
| Kağıt üretimi | 0.12 – 0.28 | D – C | Kurutma baskın, ısı geri kazanım |

### 3.2 Önemli Not: Proses Doğası

Bazı proseslerin ESI'si doğası gereği düşüktür:

- **Kurutma:** Düşük sıcaklık farkında buharlaştırma — ESI = 0.10 bile "iyi" sayılır
- **Basınçlı hava:** Sistem verimsizlikleri çok yaygın — ESI = 0.10 "ortalama"
- **CHP:** Çift ürün avantajı — ESI > 0.35 hedeflenebilir

> **AI Kuralı:** ESI'yi yorumlarken **mutlaka proses tipini** dikkate al. Her prosesin kendi "iyi/kötü" skalası vardır.

### 3.3 Genişletilmiş Sektörel ESI Referans Tablosu

| Proses | En Kötü Çeyrek ESI | Tipik ESI | BAT ESI | Best-in-Class ESI | Kaynak |
|--------|---------------------|-----------|---------|---------------------|--------|
| Basınçlı hava | < 0.05 | 0.05-0.15 | 0.14-0.15 | 0.20-0.25 (ısı geri kazanımlı) | DOE Air Master+ |
| Isıtma (düşük T) | < 0.08 | 0.08-0.18 | 0.12-0.15 | 0.40-0.60 (ısı pompası) | LCP BREF 2017 |
| Isıtma (yüksek T) | < 0.20 | 0.20-0.40 | 0.35-0.45 | 0.50+ (rejeneratif) | Kotas (1985) |
| Buhar üretimi | < 0.18 | 0.20-0.35 | 0.35-0.42 | 0.50-0.60 (HRSG) | LCP BREF 2017 |
| Soğutma (7°C) | < 0.15 | 0.15-0.40 | 0.33-0.38 | 0.50-0.55 (free cooling) | ASHRAE 90.1 |
| Soğuk depolama (−20°C) | < 0.15 | 0.15-0.40 | 0.35-0.50 | 0.55+ (NH₃/CO₂ kaskad) | IIR Guide |
| Kurutma | < 0.04 | 0.03-0.15 | 0.12-0.18 | 0.25-0.35 (ısı pompalı) | Mujumdar (2015) |
| CHP (gaz türbini) | < 0.30 | 0.35-0.50 | 0.45-0.50 | 0.55-0.60 (CCGT) | LCP BREF 2017 |
| CHP (gaz motoru) | < 0.35 | 0.40-0.55 | 0.48-0.55 | 0.58+ (yüksek η_el) | EPA CHP |
| Çimento | < 0.10 | 0.10-0.25 | 0.20-0.25 | 0.28+ (atık ısı ORC) | CLM BREF 2013 |
| Cam | < 0.08 | 0.08-0.20 | 0.15-0.20 | 0.25+ (oxy-fuel) | GLS BREF 2012 |
| Kağıt | < 0.10 | 0.12-0.28 | 0.22-0.28 | 0.30+ (entegre CHP) | PP BREF 2015 |
| Şeker | < 0.10 | 0.10-0.22 | 0.18-0.22 | 0.25+ (MVR) | FDM BREF 2019 |

> **Kullanım:** "En kötü çeyrek" = endüstrideki en düşük %25'lik dilim. "Best-in-class" = dünyada kanıtlanmış en iyi değerler (pilot veya özel koşullar dahil). AI yorumunda mevcut ESI'yi bu skalada konumlandır.

---

## 4. ESI Hesaplama Örnekleri

### 4.1 Örnek: Basınçlı Hava Sistemi

**Veriler:**
- Kompresör: 75 kW, 7 bar, 150 Nm³/h
- T₀ = 298.15 K (25 °C)

```
Ex_min = ṁRT₀ ln(P₂/P₁)
       = (150/60 × 1.293) kg/s × 0.287 kJ/(kg·K) × 298.15 K × ln(8.013/1.013)
       = 3.2295 × 0.287 × 298.15 × 2.069
       = 572 kJ/min = 9.53 kW

Ex_actual = W_kompresör = 75 kW (elektrik = exergy)

ESI = 9.53 / 75 = 0.127 → Derece: D
```

**Yorum:** Basınçlı hava sistemi termodinamik minimumun ~8 katı exergy tüketiyor. Basınçlı hava için tipik ESI aralığında (0.05-0.15). Kaçak tespiti, basınç optimizasyonu ve VFD değerlendirmesi önerilir.

### 4.2 Örnek: Endüstriyel Soğutma

**Veriler:**
- Chiller: 500 kW soğutma kapasitesi
- T_cold = 7 °C (280.15 K), T₀ = 35 °C (308.15 K)
- Kompresör güç tüketimi: 165 kW

```
Ex_min = Q_cold × (T₀/T_cold − 1) = 500 × (308.15/280.15 − 1) = 500 × 0.1 = 50 kW

Ex_actual = W_kompresör = 165 kW

ESI = 50 / 165 = 0.303 → Derece: C
```

**Yorum:** Soğutma prosesi ESI = 0.303 ile C derecesinde. Soğutma için bu iyi bir seviye. Condenser bakımı, kısmi yük optimizasyonu ve serbest soğutma (free cooling) değerlendirmesi ile B derecesine ulaşılabilir.

### 4.3 Örnek: CHP Sistemi — FUF vs ESI Karşılaştırması

CHP'de FUF (Fuel Utilization Factor) yüksek görünürken ESI farklı bir tablo ortaya koyar:

**Veriler:**
- Gaz motoru CHP: 2 MWe elektrik + 2.5 MW termal (sıcak su 90 °C)
- Doğal gaz tüketimi: 5.2 MW (LHV)
- T₀ = 25 °C (298.15 K)

```
FUF = (W_el + Q_ısı) / Q_yakıt = (2.0 + 2.5) / 5.2 = 86.5%

Exergy hesabı:
Ex_yakıt = 5.2 × 1.04 = 5.408 MW
Ex_el = 2.0 MW (elektrik = exergy)
Ex_ısı = 2.5 × (1 − 298.15/363.15) = 2.5 × 0.179 = 0.448 MW
  (90 °C sıcak su Carnot faktörü düşük!)

Ex_min = W_el + Ex_ısı = 2.0 + 0.448 = 2.448 MW

ESI = Ex_min / Ex_yakıt = 2.448 / 5.408 = 0.453 → Derece B
η_ex = Ex_min / Ex_yakıt = %45.3
```

**Karşılaştırma:**

| Metrik | Değer | Yorum |
|--------|-------|-------|
| FUF (1. yasa) | %86.5 | "Çok iyi" — ama ısının kalitesini abartır |
| η_ex (2. yasa) | %45.3 | Daha gerçekçi — ısının exergy'si düşük |
| ESI | 0.453 | Derece B — CHP için iyi |

**Kritik ders:** Aynı sistem FUF = %86.5 ve ESI = 0.453. Düşük sıcaklık ısı üreten CHP'lerde FUF ile ESI arasındaki uçurum büyür. **AI kuralı:** CHP yorumlarında HER ZAMAN her iki metriği de raporla.

---

## 5. ESI İyileştirme Yol Haritası

### 5.1 Derece Bazlı Aksiyon Matrisi

| Mevcut → Hedef | Tipik Aksiyon | Tahmini Yatırım | Geri Dönüş |
|----------------|---------------|-----------------|-------------|
| F → E | Acil bakım, kaçak giderme, kontrol düzeltme | Düşük | 0-6 ay |
| E → D | Operasyonel optimizasyon, VFD, izolasyon | Orta-düşük | 6-12 ay |
| D → C | Ekipman upgrade, ısı geri kazanım | Orta | 1-2 yıl |
| C → B | BAT teknoloji adaptasyonu, sistem entegrasyonu | Orta-yüksek | 2-3 yıl |
| B → A | İleri kontrol, proses yeniden tasarım | Yüksek | 3-5 yıl |

### 5.2 Hızlı Kazanımlar (Quick Wins) — Her Derece İçin

**F Derecesi:**
- Kaçak tespiti ve onarımı
- Temel izolasyon
- Çalışma koşullarının düzeltilmesi

**E Derecesi:**
- Değişken hız sürücü (VFD) eklenmesi
- Isı geri kazanım başlatılması
- Bakım programı oluşturulması

**D Derecesi:**
- Sistem basınç/sıcaklık optimizasyonu
- Kısmi yük kontrolü iyileştirmesi
- Ekonomizer / pre-heater eklenmesi

**C Derecesi:**
- BAT ekipman değerlendirmesi
- Proses entegrasyonu (pinch analizi)
- İleri kontrol sistemleri

**B Derecesi:**
- Exergoekonomik optimizasyon
- Çok değişkenli kontrol (MPC)
- Proses yoğunlaştırma (intensification)

---

## 5b. Proses Bazlı İyileştirme Yol Haritası — Beklenen ESI Deltaları

Her iyileştirme müdahalesi için beklenen ESI artışı (delta):

### 5b.1 Isıtma Prosesi

| Müdahale | Beklenen ΔESI | Ön Koşul | Yatırım Seviyesi |
|----------|---------------|----------|------------------|
| Ekonomizer ekleme | +0.02 – +0.05 | Baca gazı > 160 °C | Düşük |
| Hava ön ısıtıcı | +0.01 – +0.03 | Kömür/fuel oil kazan | Orta |
| Yoğuşmalı kazan dönüşümü | +0.03 – +0.08 | Doğal gaz, T_dönüş < 55 °C | Orta-yüksek |
| Isı pompası entegrasyonu | +0.10 – +0.30 | T_ısıtma < 80 °C | Yüksek |
| Modüler kazan | +0.02 – +0.05 | Değişken yük profili | Orta |

### 5b.2 Basınçlı Hava

| Müdahale | Beklenen ΔESI | Ön Koşul | Yatırım Seviyesi |
|----------|---------------|----------|------------------|
| Kaçak giderme | +0.01 – +0.04 | Kaçak > %15 | Çok düşük |
| VFD ekleme | +0.01 – +0.03 | Değişken yük profili | Orta |
| Basınç optimizasyonu | +0.005 – +0.01 | Basınç > ihtiyaç + 1 bar | Yok (operasyonel) |
| Isı geri kazanım | +0.03 – +0.08 | Isı talebi mevcut | Orta |
| Master controller | +0.005 – +0.01 | 2+ kompresör | Orta |

### 5b.3 Soğutma

| Müdahale | Beklenen ΔESI | Ön Koşul | Yatırım Seviyesi |
|----------|---------------|----------|------------------|
| Kondenser bakımı | +0.02 – +0.05 | Kondenser ΔT > 5 °C | Düşük |
| Free cooling | +0.05 – +0.15 | T_cold > 10 °C, ılıman iklim | Orta |
| VFD (pompa+fan) | +0.02 – +0.05 | Sabit hız mevcut | Orta |
| Soğuk su T artırma | +0.01 – +0.03 | Kullanıcı toleransı var | Yok (operasyonel) |
| Absorpsiyon chiller | +0.05 – +0.15 | Atık ısı > 80 °C mevcut | Yüksek |

### 5b.4 Kurutma

| Müdahale | Beklenen ΔESI | Ön Koşul | Yatırım Seviyesi |
|----------|---------------|----------|------------------|
| Egzoz ısı geri kazanım | +0.01 – +0.04 | Egzoz T > 80 °C | Orta |
| Isı pompalı kurutma | +0.05 – +0.15 | T_kurutma < 80 °C | Yüksek |
| Online nem kontrol | +0.005 – +0.02 | Aşırı kurutma mevcut | Düşük-orta |
| Mekanik ön nem alma | +0.02 – +0.05 | Yüksek başlangıç nemi | Orta |
| Çok kademeli kurutma | +0.01 – +0.03 | Tek kademe mevcut | Orta-yüksek |

> **Not:** ΔESI değerleri tahminidir ve mevcut duruma göre değişir. Zayıf durumda (düşük ESI) müdahalelerin etkisi daha büyüktür.

---

## 6. AI Yorumlama Kuralları

### 6.1 ESI Raporlama Formatı

AI yorumunda ESI aşağıdaki formatta sunulmalıdır:

```json
{
  "esi": {
    "value": 0.246,
    "grade": "C",
    "label": "İyi — ciddi iyileştirme fırsatları",
    "process_context": "Buhar üretimi için tipik aralıkta (0.20-0.35)",
    "improvement_potential": "BAT seviyesine ulaşıldığında ESI ≈ 0.38 beklenir"
  }
}
```

### 6.2 Karşılaştırma Kuralları

```
EĞER ESI > sektör_üst_sınır → "Sektör ortalamasının üzerinde, best-in-class"
EĞER ESI ∈ [sektör_alt, sektör_üst] → "Sektör ortalamasında, iyileştirme fırsatları var"
EĞER ESI < sektör_alt_sınır → "Sektör ortalamasının altında, acil aksiyon gerekli"
```

### 6.3 Çoklu Proses Karşılaştırması

Fabrika seviyesinde birden fazla proses varsa:
1. Her prosesin ESI'sini ayrı hesapla
2. Ağırlıklı ortalama ESI hesapla: ESI_fabrika = Σ(ESI_i × Ex_actual_i) / Σ(Ex_actual_i)
3. En düşük ESI'li prosesi öncelikli hedef olarak belirle
4. Exergy yıkım payına göre önceliklendirme yap

---

## 6b. CO₂ Korelasyonu

### 6b.1 ESI-CO₂ İlişkisi

ESI iyileşmesi doğrudan CO₂ emisyon azalmasına karşılık gelir:

$$\Delta CO_2 = \Delta Ex_{tasarruf} \times EF_{yakıt} \times t_{yıl}$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| ΔEx_tasarruf | Exergy tasarrufu | kW |
| EF_yakıt | Yakıt emisyon faktörü | kg CO₂/kWh |
| t_yıl | Yıllık çalışma süresi | h |

**Emisyon faktörleri:**

| Yakıt | EF (kg CO₂/kWh) | Kaynak |
|-------|------------------|--------|
| Doğal gaz | 0.202 | IPCC 2006 |
| Kömür (bitümlü) | 0.341 | IPCC 2006 |
| Fuel oil | 0.267 | IPCC 2006 |
| Elektrik (EU avg) | 0.275 | EEA 2023 |
| Elektrik (Türkiye) | 0.440 | TEİAŞ 2023 |

### 6b.2 Çözümlü Örnek

**Problem:** Isıtma prosesinde ESI 0.18'den 0.28'e yükseltildi. Doğal gaz kazanı, Q = 2.000 kW termal, 7.200 h/yıl.

```
Mevcut: Ex_actual = Ex_min / ESI_eski = (2000 × 0.342) / 0.18 = 3800 kW_ex
Hedef:  Ex_hedef  = Ex_min / ESI_yeni = (2000 × 0.342) / 0.28 = 2443 kW_ex

ΔEx = 3800 − 2443 = 1357 kW
ΔQ_yakıt ≈ 1357 / 1.04 = 1305 kW (enerji)

ΔCO₂ = 1305 × 0.202 × 7200 / 1000 = 1898 ton CO₂/yıl

(Veya: Her 0.01 ESI artışı ≈ ~190 ton CO₂/yıl azalma — bu ölçek için)
```

> **AI Kuralı:** ESI iyileştirme önerilerinde CO₂ etkisini de belirt. "ESI'yi C derecesinden B derecesine yükseltmek yıllık ~X ton CO₂ azalma sağlar."

---

## İlgili Dosyalar

- `factory/process/gap_analysis_methodology.md` — 3 katmanlı boşluk modeli
- `factory/process/bat_overview.md` — BAT kavramı ve EU BREF sistemi
- `factory/process/index.md` — Proses bilgi tabanı navigasyon haritası
- Her proses dosyası — Proses bazlı tipik ESI değerleri
- `factory/exergoeconomic/evaluation_criteria.md` — Ċ_D, f_k, r_k değerlendirmesi

## Referanslar

1. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier. — ESI tanımı ve örnekleri (Bölüm 2.7, 18.3)
2. Rosen, M.A., Dincer, I. & Kanoglu, M. (2008). "Role of exergy in increasing efficiency and sustainability and reducing environmental impact." *Energy Policy*, 36(1), 128-137.
3. Connelly, L. & Koshland, C.P. (2001). "Exergy and industrial ecology." *Exergy, An International Journal*, 1(3), 146-165.
4. Sciubba, E. & Wall, G. (2007). "A brief commented history of exergy from the beginnings to 2004." *Int. J. of Thermodynamics*, 10(1), 1-26.
5. IPCC (2006). *Guidelines for National Greenhouse Gas Inventories*. Vol. 2, Ch. 2 — Stationary Combustion Emission Factors.
6. European Environment Agency (2023). *CO₂ emission intensity of electricity generation in Europe*. EEA Indicator.
7. Hammond, G.P. & Winnett, A.B. (2006). "Interdisciplinary perspectives on environmental appraisal and valuation techniques." *Proceedings of the ICE — Waste and Resource Management*, 159(3), 117-130.
8. Wall, G. (2003). "Exergy tools." *Proceedings of the Institution of Mechanical Engineers, Part A*, 217(4), 401-412.
