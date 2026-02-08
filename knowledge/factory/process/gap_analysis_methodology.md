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

### 2.4 ESI'nin 2. Yasa Türetimi (Derivation from Second Law)

Termodinamiğin 2. yasası uyarınca, herhangi bir gerçek proses entropi üretir:

$$\dot{S}_{gen} = \dot{S}_{out} - \dot{S}_{in} \geq 0$$

Gouy-Stodola teoremi, entropi üretimini exergy yıkımına bağlar:

$$\dot{Ex}_{yıkım} = T_0 \cdot \dot{S}_{gen}$$

Bir prosesin exergy dengesi:

$$Ex_{in} = Ex_{ürün} + Ex_{yıkım} + Ex_{atık}$$

Tersinir (ideal) durumda Ex_yıkım = 0 ve Ex_atık = 0:

$$Ex_{in,min} = Ex_{ürün} = Ex_{min}$$

ESI, gerçek girişin ideal girişe oranıdır:

$$ESI = \frac{Ex_{min}}{Ex_{actual}} = \frac{Ex_{min}}{Ex_{min} + Ex_{yıkım} + Ex_{atık}}$$

**Fiziksel anlam:** ESI = 1 − (yıkım + atık oranı). ESI ne kadar yüksekse, proses termodinamik ideale o kadar yakındır.

> **Kaynak:** Dincer & Rosen (2013), Bölüm 2.7, s. 38-42; Kotas (1985), Bölüm 2, s. 15-28.

### 2.5 Ekonomik Etki Formülü (Economic Impact)

İyileştirilebilir boşluğun yıllık ekonomik etkisi:

$$C_{tasarruf} = \Delta Ex_{imp} \times c_{yakıt} \times t_{yıl} \times \varphi$$

| Sembol | Tanım | Birim | Tipik Değer |
|--------|-------|-------|-------------|
| ΔEx_imp | İyileştirilebilir exergy boşluğu | kW | Ex_actual − Ex_BAT |
| c_yakıt | Yakıt birim maliyeti | €/kWh | 0.03-0.06 (doğal gaz) |
| t_yıl | Yıllık çalışma süresi | h/yıl | 4.000-8.760 |
| φ | Exergy/enerji oranı düzeltmesi | — | 1.04 (doğal gaz) |

**Örnek:**
```
ΔEx_imp = 500 kW
c_yakıt = 0.04 €/kWh
t_yıl = 7.200 h/yıl
φ = 1.04

C_tasarruf = 500 × 0.04 × 7200 × 1.04 = 149.760 €/yıl ≈ 150.000 €/yıl
```

> **Not:** Bu basitleştirilmiş bir hesaptır. Gerçek ekonomik analiz yatırım maliyetini, bakım giderlerini ve fırsat maliyetini de içermelidir. Detaylı exergoekonomik analiz için bkz. `factory/exergoeconomic/evaluation_criteria.md`.

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

## 4b. Çözümlü Örnek: Basınçlı Hava Sistemi

### Veriler
- Proses: 7 bar_g basınçlı hava üretimi
- Kompresör: 75 kW vidalı, yağlı
- Üretim kapasitesi: 10 m³/min (FAD)
- Kaçak oranı: %25 (ultrasonik testle belirlenmiş)
- T₀ = 25 °C (298.15 K)

### Adım 1: Minimum Exergy (İzotermik Sıkıştırma)
```
ṁ = 10 m³/min × 1.205 kg/m³ / 60 = 0.2008 kg/s
P₂/P₁ = (7 + 1.013) / 1.013 = 7.912

W_min = ṁ × R × T₀ × ln(P₂/P₁)
      = 0.2008 × 0.287 × 298.15 × ln(7.912)
      = 0.2008 × 0.287 × 298.15 × 2.068
      = 35.5 kW

Ex_min = W_min = 35.5 kW (sadece yararlı basınçlı hava)
```

### Adım 2: BAT Değeri
DOE Air Master+ ve ENE BREF 2009 → BAT spesifik güç: 5.0 kW/(m³/min) (sistem seviyesi)
Engine değeri: bat_references.py → compressed_air/general = 0.005 kWh/m³ (birim farklı)

```
W_BAT_sistem = 5.0 × 10 = 50 kW (sistem düzeyinde)
Ex_BAT = 50 kW
```

### Adım 3: Gerçek Tüketim
```
Kompresör gücü: 75 kW
Kaçak kayıpları: %25 → yararlı debi = 10 × 0.75 = 7.5 m³/min
Ancak kompresör hala 75 kW çekiyor (kaçakları da besliyor)

Ex_actual = 75 kW (kompresör elektrik = exergy)
```

### Adım 4: Boşluk Analizi
```
ESI = Ex_min / Ex_actual = 35.5 / 75 = 0.473 → Derece B (kompresör seviyesi)

Ancak GERÇEK sistem ESI (kaçak dahil):
Yararlı Ex_min = 35.5 × 0.75 = 26.6 kW (yararlı debi oranında)
ESI_sistem = 26.6 / 75 = 0.355 → Hala iyi görünüyor

BPR = Ex_BAT / Ex_actual = 50 / 75 = 0.667

ΔEx_total = 75 − 26.6 = 48.4 kW
ΔEx_imp = 75 − 50 = 25 kW
η_imp = 25 / 48.4 = 51.6%
```

### Yorumlama
- **ESI_sistem = 0.355 (Derece C):** Basınçlı hava için iyi — ancak proses bazlı (tipik 0.05-0.15) ile karıştırma! Burada kompresör ESI'si hesaplandı.
- **BPR = 0.667:** BAT'tan %33 uzakta — kaçak giderme ile büyük iyileştirme mümkün
- **η_imp = %51.6:** Boşluğun yarısından fazlası BAT ile kapatılabilir
- **Öncelikli aksiyon:** Kaçak tespiti ve onarımı (%25 → %10 hedef), VFD değerlendirmesi

---

## 4c. Çözümlü Örnek: Kurutma Prosesi

### Veriler
- Proses: Konveksiyonel sıcak hava kurutma
- Ürün: Tahıl (mısır)
- Su uzaklaştırma hızı: 1.000 kg/h
- Giriş havası: 120 °C, çıkış: 65 °C
- Yakıt: Doğal gaz, ölçülen SEC: 5.500 kJ/kg su
- T₀ = 25 °C (298.15 K)

### Adım 1: Minimum Exergy
Serbest su buharlaştırma minimum exergy (psikrometrik yaklaşım):
```
ex_min ≈ 400 kJ/kg su (serbest su, tipik referans)

Not: Bu değer şu şekilde türetilebilir:
  - Suyun buharlaşma entalpisi: h_fg = 2.257 kJ/kg
  - Ancak buharlaşma T₀'da olabilir: Carnot faktörü ≈ 0.17 (75 °C ort.)
  - Psikrometrik minimum daha karmaşık — bkz. drying.md detay

Ex_min = (1000/3600) × 400 = 111.1 kW
```

### Adım 2: BAT Değeri
FDM BREF 2019 → Tahıl kurutma BAT SEC: 3.000-3.800 kJ/kg su (ısı geri kazanımlı)
Engine değeri: bat_references.py → drying/food_grain = 0.18 kWh/kg su = 648 kJ/kg su

```
BAT SEC = 3.400 kJ/kg su (ortalama)
Q_BAT = (1000/3600) × 3400 = 944.4 kW (termal)
Ex_BAT = 944.4 × 1.04 = 982.2 kW (doğal gaz exergy)
```

### Adım 3: Gerçek Tüketim
```
Q_actual = (1000/3600) × 5500 = 1527.8 kW (termal)
Ex_actual = 1527.8 × 1.04 = 1588.9 kW (doğal gaz exergy)
```

### Adım 4: Boşluk Analizi
```
ESI = Ex_min / Ex_actual = 111.1 / 1588.9 = 0.070 → Derece E
BPR = Ex_BAT / Ex_actual = 982.2 / 1588.9 = 0.618

ΔEx_total = 1588.9 − 111.1 = 1477.8 kW
ΔEx_imp = 1588.9 − 982.2 = 606.7 kW
η_imp = 606.7 / 1477.8 = 41.1%
```

### Yorumlama
- **ESI = 0.070 (Derece E):** Kurutma için tipik — proses doğası gereği düşük exergy verimli
- **BPR = 0.618:** BAT'tan %38 uzakta — ısı geri kazanım potansiyeli yüksek
- **η_imp = %41.1:** Boşluğun %41'i BAT ile kapatılabilir → ~607 kW exergy tasarrufu
- **Ekonomik etki:** 606.7 kW × 0.04 €/kWh × 7.200 h/yıl × 1.04 ≈ 182.000 €/yıl
- **Öncelikli aksiyon:** Egzoz ısı geri kazanımı (hava-hava eşanjör), online nem kontrol

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

## 6b. T₀ Duyarlılık Analizi ve Ölçüm Belirsizliği

### 6b.1 Çevre Sıcaklığı (T₀) Etkisi

ESI hesaplaması T₀'a bağlıdır. Farklı iklim bölgelerinde T₀ değişkenliği ESI'yi etkiler:

| Parametre | T₀ = 15 °C | T₀ = 25 °C (ref) | T₀ = 35 °C | T₀ = 45 °C |
|-----------|-----------|-------------------|-----------|-----------|
| Isıtma (180 °C) Carnot | 0.363 | 0.342 | 0.320 | 0.297 |
| Soğutma (7 °C) ters Carnot | 0.028 | 0.100 | 0.178 | 0.262 |
| Basınçlı hava ln(P₂/P₁) | Değişmez | Değişmez | Değişmez | Değişmez |

**Gözlemler:**
- **Isıtma:** T₀ arttıkça Carnot faktörü azalır → ESI düşer (daha az exergy gerekir, ama oran da değişir)
- **Soğutma:** T₀ arttıkça ters Carnot exergy'si dramatik artar → T₀ = 35 °C'de ESI çok farklı
- **Basınçlı hava:** İzotermik sıkıştırma formülünde T₀ hem payda hem paydada → net etki düşük

> **AI Kuralı:** Tropik ve çöl iklimlerinde (T₀ > 35 °C) soğutma ESI'si önemli ölçüde farklılaşır. Raporda T₀ değerini mutlaka belirt.

### 6b.2 Ölçüm Belirsizliği (Measurement Uncertainty)

| Ölçüm | Tipik Belirsizlik | ESI Etkisi | Not |
|--------|-------------------|-----------|-----|
| Sıcaklık (T) | ±1-2 °C | ±%2-5 | Termoçift doğruluğu |
| Basınç (P) | ±%1-2 | ±%1-3 | Transmitter kalibrasyonu |
| Debi (ṁ) | ±%2-5 | ±%2-5 | Orifis/ultrasonik doğruluğu |
| Elektrik güç (W) | ±%1-2 | ±%1-2 | Güç analizörü |
| Yakıt tüketimi | ±%2-3 | ±%2-3 | Sayaç kalibrasyonu |

**Toplam ESI belirsizliği (tipik):** ±%5-10 (propagasyon ile)

**Belirsizlik propagasyonu formülü:**

$$\frac{\delta ESI}{ESI} = \sqrt{\left(\frac{\delta Ex_{min}}{Ex_{min}}\right)^2 + \left(\frac{\delta Ex_{actual}}{Ex_{actual}}\right)^2}$$

> **Pratik kural:** ESI farkı %10'dan küçükse "aynı seviyede" olarak yorumla. ESI = 0.20 ile ESI = 0.22 arasında anlamlı fark yoktur.

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
6. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press. — Gouy-Stodola teoremi ve exergy yıkım
7. Moran, M.J. & Shapiro, H.N. (2014). *Fundamentals of Engineering Thermodynamics*. 8th ed., Wiley. — Exergy dengesi ve 2. yasa formülasyonu
8. Wall, G. (1977). "Exergy — a useful concept within resource accounting." *Report No. 77-42*, Institute of Theoretical Physics, Chalmers University of Technology. — ESI ilk kullanımları
9. JCGM 100:2008. *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*. — Ölçüm belirsizliği metodolojisi
