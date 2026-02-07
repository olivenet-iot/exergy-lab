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
