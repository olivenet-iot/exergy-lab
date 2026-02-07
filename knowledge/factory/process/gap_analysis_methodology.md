---
title: "Proses Boşluk Analizi Metodolojisi (Process Gap Analysis Methodology)"
category: factory
equipment_type: factory
keywords: [gap analysis, boşluk analizi, BAT, minimum exergy, termodinamik limit, iyileştirme potansiyeli, exergy sürdürülebilirlik indeksi]
related_files: [factory/process/bat_overview.md, factory/process/sustainability_index.md, factory/process/index.md, factory/factory_benchmarks.md]
use_when: ["Proses seviyesi boşluk analizi yapılacakken", "Termodinamik minimum ile gerçek tüketim karşılaştırılacakken", "İyileştirme potansiyeli hesaplanacakken"]
priority: high
last_updated: 2026-02-08
---

# Proses Boşluk Analizi Metodolojisi (Process Gap Analysis Methodology)

Bu dosya, ExergyLab'ın proses seviyesi boşluk analizi (Process Gap Analysis) için kullandığı **3 katmanlı modeli**, formülleri ve yorumlama kurallarını tanımlar. Boşluk analizi, bir prosesin termodinamik minimumundan ne kadar uzakta olduğunu ve BAT seviyesine göre konumunu nicelleştirir.

---

## 1. 3 Katmanlı Boşluk Modeli (Three-Layer Gap Model)

### 1.1 Kavramsal Çerçeve

Her endüstriyel proses üç exergy tüketim seviyesiyle tanımlanır:

```
Katman 1: Ex_min     — Termodinamik Minimum (Theoretical Minimum Exergy)
Katman 2: Ex_BAT     — En İyi Mevcut Teknik (Best Available Technique)
Katman 3: Ex_actual  — Gerçek Tüketim (Actual Consumption)

Ex_min ≤ Ex_BAT ≤ Ex_actual
```

| Katman | Tanım | Belirleyen |
|--------|-------|------------|
| Ex_min | Tersinir (reversible) proses limiti | Termodinamiğin 2. yasası |
| Ex_BAT | Ticari olarak kanıtlanmış en iyi teknoloji | EU BREF, DOE, sektörel standartlar |
| Ex_actual | Tesisin mevcut durumu | Ölçüm verileri |

### 1.2 Boşluk Tanımları

```
Toplam Boşluk (Total Gap):
  ΔEx_total = Ex_actual − Ex_min

Teknolojik Boşluk (Technology Gap):
  ΔEx_tech = Ex_BAT − Ex_min

İyileştirilebilir Boşluk (Improvable Gap):
  ΔEx_imp = Ex_actual − Ex_BAT

İyileştirilebilir oran:
  η_imp = ΔEx_imp / ΔEx_total × 100 (%)
```

**Fiziksel anlam:**
- **ΔEx_tech**: Mevcut teknoloji sınırlarıyla bile kapatılamayan boşluk (R&D gerektirir)
- **ΔEx_imp**: Mevcut BAT teknolojileri ile kapatılabilecek boşluk (yatırım kararı)

---

## 2. Temel Formüller

### 2.1 Exergy Sürdürülebilirlik İndeksi (Exergy Sustainability Index — ESI)

$$ESI = \frac{Ex_{min}}{Ex_{actual}}$$

ESI, 0 ile 1 arasında değişir:
- **ESI → 1**: Proses termodinamik limite yakın (mükemmel)
- **ESI → 0**: Proses çok verimsiz (büyük iyileştirme potansiyeli)

> **Not:** ESI, exergy verimi (η_ex) ile karıştırılmamalıdır. η_ex = Ex_product/Ex_fuel şeklinde tanımlanır ve prosesin iç verimidir. ESI ise termodinamik minimuma göre mutlak konumu ölçer.

Detaylı ESI derecelendirme tablosu için bkz. `sustainability_index.md`.

### 2.2 BAT Yakınlık Oranı (BAT Proximity Ratio)

$$BPR = \frac{Ex_{BAT}}{Ex_{actual}}$$

| BPR Aralığı | Yorum |
|-------------|-------|
| > 0.90 | BAT seviyesinde veya çok yakın |
| 0.70 – 0.90 | İyi, ama iyileştirme fırsatları var |
| 0.50 – 0.70 | Orta, ciddi iyileştirme potansiyeli |
| < 0.50 | Zayıf, acil müdahale gerekli |

### 2.3 Proses Exergy Verimi (Process Exergy Efficiency)

$$\eta_{ex,process} = \frac{Ex_{min}}{Ex_{actual}} = ESI$$

Proses seviyesinde exergy verimi, ESI ile eşdeğerdir.

---

## 3. Hesaplama Adımları

### Adım 1: Proses Tanımlama
- Proses tipi belirleme (ısıtma, soğutma, basınçlı hava, vb.)
- Giriş/çıkış akışları tanımlama
- Sistem sınırları belirleme

### Adım 2: Termodinamik Minimum Hesaplama
- Proses tipine özel Ex_min formülü uygula
- Çevre sıcaklığı T₀ = 298.15 K (25 °C) kabul et (aksi belirtilmedikçe)
- Referans basıncı P₀ = 101.325 kPa

### Adım 3: BAT Referans Değeri Belirleme
- İlgili EU BREF dokümanına başvur
- Sektörel ve alt-kategori BAT değerini seç
- BAT SEC → Ex_BAT dönüşümü yap

### Adım 4: Gerçek Tüketim Hesaplama
- Ölçüm verilerinden Ex_actual hesapla
- Tüm girişlerin exergy katkısını dahil et

### Adım 5: Boşluk Analizi
- ΔEx_total, ΔEx_imp, η_imp hesapla
- ESI ve BPR hesapla
- Sonuçları yorumla

---

## 4. Çözümlü Örnek: Buhar Üretim Prosesi

### Veriler
- Proses: 10 bar doymuş buhar üretimi
- Beslenme suyu: 25 °C, 1 atm
- Buhar üretimi: 5.000 kg/h
- Kullanılan yakıt: Doğal gaz
- Gerçek SEC: 3.200 kJ/kg buhar

### Adım 1: Minimum Exergy
Doymuş buhar (10 bar): h = 2.778 kJ/kg, s = 6.586 kJ/(kg·K)
Ölü hal (25 °C, 1 atm): h₀ = 104.9 kJ/kg, s₀ = 0.367 kJ/(kg·K)

```
ex_min = (h − h₀) − T₀(s − s₀)
       = (2778 − 104.9) − 298.15 × (6.586 − 0.367)
       = 2673.1 − 1853.7
       = 819.4 kJ/kg
```

### Adım 2: BAT Değeri
EU BREF LCP 2017 → Kazan verimi (BAT): %94 (LHV bazlı)
Doğal gaz LHV: 47.100 kJ/kg, exergy/enerji oranı: ~1.04

```
SEC_BAT = (h − h_beslenme) / η_BAT = (2778 − 104.9) / 0.94 = 2843 kJ/kg (enerji)
Ex_BAT = SEC_BAT × (exergy/energy) ≈ 2843 × 1.04 ≈ 2957 kJ/kg (exergy)
```

Daha doğrudan yaklaşım: kazan exergy verimi BAT ≈ %38 (Tsatsaronis, 2013)
```
Ex_BAT = ex_min / η_ex_BAT = 819.4 / 0.38 = 2156 kJ/kg (exergy girişi)
```

### Adım 3: Gerçek Tüketim
```
Ex_actual = SEC_actual × (exergy/energy) ≈ 3200 × 1.04 ≈ 3328 kJ/kg
```

### Adım 4: Boşluk Analizi
```
ESI = Ex_min / Ex_actual = 819.4 / 3328 = 0.246 → Derece: C
BPR = Ex_BAT / Ex_actual = 2156 / 3328 = 0.648

ΔEx_total = 3328 − 819.4 = 2508.6 kJ/kg
ΔEx_imp = 3328 − 2156 = 1172 kJ/kg
η_imp = 1172 / 2508.6 = 46.7%
```

### Yorumlama
- **ESI = 0.246 (Derece C):** Buhar üretim prosesi termodinamik minimumun ~4 katı exergy tüketiyor — tipik endüstriyel seviye
- **BPR = 0.648:** BAT seviyesinden %35 uzakta — ciddi iyileştirme potansiyeli
- **η_imp = %46.7:** Toplam boşluğun neredeyse yarısı mevcut teknolojilerle kapatılabilir
- **Öneri:** Ekonomizer, hava ön ısıtıcı, kondensing kazan teknolojisi araştır

---

## 5. Yorumlama Kuralları (AI Kullanımı İçin)

### 5.1 ESI Bazlı Genel Değerlendirme
```
EĞER ESI > 0.50 → "Dünya sınıfı verimlilik, ince ayar önerileri sun"
EĞER 0.35 ≤ ESI ≤ 0.50 → "Çok iyi, BAT yakınında, spesifik iyileştirmeler öner"
EĞER 0.20 ≤ ESI < 0.35 → "İyi ama ciddi fırsatlar var, sistematik analiz öner"
EĞER 0.10 ≤ ESI < 0.20 → "Ortalama, acil aksiyon planı oluştur"
EĞER 0.05 ≤ ESI < 0.10 → "Zayıf, kapsamlı modernizasyon öner"
EĞER ESI < 0.05 → "Kritik, büyük dönüşüm projesi gerekli"
```

### 5.2 BPR Bazlı Teknoloji Değerlendirmesi
```
EĞER BPR > 0.90 → "BAT seviyesinde, teknoloji güncel"
EĞER BPR 0.70-0.90 → "İyi teknoloji, bakım/operasyon odaklı iyileştirme"
EĞER BPR 0.50-0.70 → "Teknoloji güncellemesi gerekli, BAT retrofit öner"
EĞER BPR < 0.50 → "Eski teknoloji, komple yenileme değerlendir"
```

### 5.3 Sektörel Bağlam
Her zaman ESI/BPR sonuçlarını ilgili proses dosyasındaki sektörel tipik değerlerle karşılaştır. Bir ESI = 0.15 çimento sektörü için "normal" olabilirken, basınçlı hava için "çok zayıf" anlamına gelir.

---

## 6. Sınırlılıklar ve Uyarılar

1. **Ex_min idealdir:** Gerçekte bile tersinir proses mümkün değildir; Ex_min alt sınırdır
2. **BAT bölgeseldir:** EU BREF değerleri Avrupa koşullarını yansıtır; tropikal/soğuk iklimlerde T₀ farklı olabilir
3. **Sistem sınırları kritiktir:** Aynı proses, farklı sistem sınırlarıyla farklı ESI verir
4. **Dinamik etkiler:** Kısmi yük, geçici rejimler ESI'yi düşürebilir — kararlı hal verileri tercih et
5. **Exergy kalitesi:** Aynı kW exergy farklı uygulanabilirliğe sahip olabilir (elektrik vs düşük sıcaklık ısı)

---

## İlgili Dosyalar

- `factory/process/bat_overview.md` — BAT kavramı ve EU BREF sistemi
- `factory/process/sustainability_index.md` — ESI derecelendirme detayları
- `factory/process/index.md` — Proses bilgi tabanı navigasyon haritası
- `factory/factory_benchmarks.md` — Fabrika seviyesi sektörel benchmark
- `factory/exergoeconomic/evaluation_criteria.md` — Ċ_D, f_k, r_k değerlendirmesi

## Referanslar

1. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier. — ESI tanımı (Bölüm 2.7)
2. Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis and exergoeconomics." *Energy*, 32(4), 249-253.
3. EU Commission (2009). *Reference Document on Best Available Techniques for Energy Efficiency*. JRC BREF.
4. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Minimum exergy kavramı
5. Sciubba, E. (2001). "Beyond thermoeconomics? The concept of Extended Exergy Accounting." *Energy*, 26(1), 29-44.
