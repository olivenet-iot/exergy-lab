---
title: "Isı Eşanjörü Benchmark Verileri"
category: reference
equipment_type: heat_exchanger
keywords: [benchmark, ısı eşanjörü, U-değer, etkililik, exergy verimi, fouling]
related_files: [heat_exchanger/formulas.md, heat_exchanger/audit.md, heat_exchanger/standards.md]
use_when: ["Isı eşanjörü performansı değerlendirilirken", "Verimlilik karşılaştırması yapılırken", "Exergy verimi sınıflandırması gerektiğinde"]
priority: high
last_updated: 2026-02-01
---
# Isı Eşanjörü Benchmark Verileri

> Son güncelleme: 2026-02-01

## 1. Exergy Verimi Aralıkları (Exergy Efficiency Benchmarks)

Isı eşanjörleri için exergy verimi, enerji veriminden (effectiveness) çok farklıdır.
Enerji verimi genellikle %60-95+ arasında olurken, exergy verimi tipik olarak
%20-80 arasındadır. Bu fark, ısı transferi sırasında sıcaklık kalitesinin
(termodinamik "iş üretme potansiyeli") kaybolmasından kaynaklanır.

### 1.1 Eşanjör Tipine Göre Exergy Verimi

| Eşanjör Tipi | Düşük | Ortalama | İyi | Best-in-class |
|--------------|-------|----------|-----|---------------|
| Gövde-boru (shell & tube) | < 25% | 25-40% | 40-55% | > 55% |
| Plakalı (plate) | < 30% | 30-45% | 45-60% | > 60% |
| Hava soğutmalı (air-cooled) | < 15% | 15-25% | 25-35% | > 35% |
| Çift borulu (double pipe) | < 20% | 20-35% | 35-50% | > 50% |
| Spiral | < 25% | 25-40% | 40-55% | > 55% |
| Ekonomizer | < 20% | 20-35% | 35-50% | > 50% |
| Hava ön ısıtıcı | < 15% | 15-25% | 25-40% | > 40% |
| Reküperatör (yüksek T) | < 30% | 30-45% | 45-60% | > 60% |

**Not:** Exergy verimi hesabı:
```
eta_ex = (Ex_soğuk,çıkış - Ex_soğuk,giriş) / (Ex_sıcak,giriş - Ex_sıcak,çıkış)
```

### 1.2 Akışkan Kombinasyonuna Göre Exergy Verimi

| Akışkan Kombinasyonu | Tipik eta_ex | Açıklama |
|----------------------|-------------|----------|
| Su - Su (yakın sıcaklık) | %50 - %75 | Düşük DT_lm → yüksek exergy verimi |
| Su - Su (geniş aralık) | %25 - %50 | Büyük DT_lm → düşük exergy verimi |
| Buhar (yoğuşma) - Su | %30 - %55 | Sabit T_h → iyi profil eşlemesi |
| Gaz - Gaz | %15 - %35 | Düşük h → büyük DT gerekli |
| Yağ - Su | %20 - %40 | Yağ tarafı sınırlı |
| Baca gazı - Su/Buhar | %15 - %40 | Gaz tarafı sınırlı |
| Baca gazı - Hava | %10 - %30 | Düşük exergy içerikli akışkanlar |

### 1.3 Sıcaklık Seviyesine Göre Exergy Verimi

| Sıcaklık Aralığı | Tipik eta_ex | Açıklama |
|------------------|-------------|----------|
| Yüksek T (> 300°C) | %35 - %65 | Yüksek Carnot faktörü |
| Orta T (100 - 300°C) | %25 - %50 | Endüstriyel standart |
| Düşük T (50 - 100°C) | %15 - %35 | Düşük exergy içeriği |
| Çok düşük T (< 50°C) | %5 - %20 | Çevre sıcaklığına yakın |

**Önemli:** Çevre sıcaklığına (T_0 ≈ 25°C) yakın işlem yapan eşanjörlerin exergy verimi
doğal olarak düşüktür. Bu bir arıza değil, termodinamiğin bir sonucudur.

## 2. Toplam Isı Transfer Katsayısı (U-Değer) Aralıkları

### 2.1 Akışkan Kombinasyonuna Göre U-Değerleri

| Akışkan Kombinasyonu | U_min [W/(m2·K)] | U_tipik [W/(m2·K)] | U_max [W/(m2·K)] |
|----------------------|------------------|-------------------|------------------|
| Su - Su | 800 | 1,500 | 2,500 |
| Su - Yağ | 100 | 250 | 400 |
| Su - Organik solvent | 200 | 500 | 800 |
| Buhar - Su (ısıtma) | 1,000 | 2,500 | 3,500 |
| Buhar yoğuşması - Su | 1,500 | 3,000 | 4,500 |
| Buhar - Yağ | 50 | 200 | 400 |
| Gaz (1 atm) - Gaz (1 atm) | 10 | 30 | 50 |
| Gaz (yüksek P) - Gaz (yüksek P) | 50 | 150 | 300 |
| Gaz - Su | 20 | 100 | 300 |
| Gaz - Yağ | 10 | 50 | 100 |
| Organik buhar yoğuşması - Su | 300 | 700 | 1,200 |
| Baca gazı - Su (ekonomizer) | 30 | 60 | 120 |
| Baca gazı - Hava (ön ısıtıcı) | 15 | 30 | 60 |

### 2.2 Eşanjör Tipine Göre U-Değerleri

| Eşanjör Tipi | Tipik U Aralığı [W/(m2·K)] | Avantaj |
|--------------|---------------------------|---------|
| Gövde-boru (su-su) | 800 - 2,500 | Geniş uygulama |
| Plakalı (su-su) | 2,000 - 5,000 | Yüksek türbülansı |
| Plakalı (buhar-su) | 2,500 - 6,000 | Kompakt |
| Hava soğutmalı (gaz-hava) | 15 - 60 | Soğutma suyu gereksiz |
| Çift borulu | 300 - 1,400 | Basit, esnek |
| Spiral (sıvı-sıvı) | 700 - 2,500 | Kendinden temizleme |
| Finli boru (gaz-sıvı) | 25 - 100 | Gaz tarafı genişletilmiş |

## 3. Etkililik (Effectiveness, epsilon) Aralıkları

### 3.1 Eşanjör Tipine Göre Tipik Etkililik

| Eşanjör Tipi | Tipik epsilon | Üretilebilir Aralık | Not |
|--------------|--------------|---------------------|-----|
| Gövde-boru (1 gövde/2 boru geçişi) | 0.50 - 0.70 | 0.40 - 0.85 | En yaygın konfigürasyon |
| Gövde-boru (2 gövde/4 boru geçişi) | 0.60 - 0.80 | 0.50 - 0.90 | Daha iyi performans |
| Plakalı (ters akış) | 0.75 - 0.90 | 0.60 - 0.95 | Yüksek NTU ulaşılabilir |
| Hava soğutmalı | 0.40 - 0.60 | 0.30 - 0.70 | Hava tarafı sınırlı |
| Çift borulu (ters akış) | 0.60 - 0.80 | 0.40 - 0.90 | Küçük kapasiteler |
| Spiral | 0.60 - 0.80 | 0.50 - 0.85 | İyi ters akış yaklaşımı |
| Ekonomizer | 0.50 - 0.70 | 0.40 - 0.80 | Baca gazı tarafı sınırlı |
| Reküperatör (yüksek T) | 0.60 - 0.85 | 0.50 - 0.90 | Metalürjik sınırlar |

### 3.2 NTU ve epsilon İlişkisi (C_r = 0.5 için Referans)

| NTU | epsilon (Ters Akış) | epsilon (Paralel Akış) | epsilon (1-2 S&T) |
|-----|---------------------|----------------------|-------------------|
| 0.5 | 0.36 | 0.33 | 0.34 |
| 1.0 | 0.57 | 0.49 | 0.52 |
| 1.5 | 0.69 | 0.57 | 0.62 |
| 2.0 | 0.78 | 0.62 | 0.69 |
| 3.0 | 0.87 | 0.65 | 0.77 |
| 4.0 | 0.92 | 0.66 | 0.81 |
| 5.0 | 0.95 | 0.67 | 0.84 |

## 4. Yaklaşım Sıcaklığı Hedefleri (Approach Temperature Targets)

| Uygulama | Hedef DT_approach [°C] | İyi | Ortalama | Kötü |
|----------|----------------------|-----|----------|------|
| Proses ısı geri kazanımı | 5 - 10 | < 8 | 8 - 15 | > 15 |
| Ekonomizer (gaz-sıvı) | 15 - 25 | < 20 | 20 - 35 | > 35 |
| Hava ön ısıtıcı (gaz-gaz) | 25 - 40 | < 30 | 30 - 50 | > 50 |
| Yoğuşturucu | 3 - 8 | < 5 | 5 - 12 | > 12 |
| Buharlaştırıcı | 3 - 5 | < 5 | 5 - 10 | > 10 |
| Plakalı HX (sıvı-sıvı) | 2 - 5 | < 3 | 3 - 8 | > 8 |
| Soğutma kulesi suyu | 5 - 10 | < 8 | 8 - 15 | > 15 |

**Not:** Düşük yaklaşım sıcaklığı daha iyi termodinamik performans ancak
daha büyük transfer alanı ve yatırım maliyeti demektir.

## 5. Kirlenme Faktörleri (Fouling Factors) — TEMA Standardı

### 5.1 TEMA Önerilen Kirlenme Direnci Değerleri

| Akışkan | R_f [m2·K/W] | Açıklama |
|---------|--------------|----------|
| **Sular** | | |
| Deniz suyu (< 50°C) | 0.000088 | Temiz |
| Deniz suyu (> 50°C) | 0.000176 | Biyo-kirlenme riski |
| Nehir suyu (temiz) | 0.000176 | Mevsimsel değişim |
| Nehir suyu (kirli) | 0.000352 | Askıda katı maddeler |
| Soğutma kulesi suyu (işlem görmüş) | 0.000176 | Standart |
| Soğutma kulesi suyu (işlenmemiş) | 0.000528 | Kireç ve biyo-kirlenme |
| Şehir suyu (< 50°C) | 0.000176 | Standart |
| Şehir suyu (> 50°C) | 0.000352 | Kireç oluşumu |
| Kazan besleme suyu (arıtılmış) | 0.000088 | Temiz |
| Kondensat (temiz) | 0.000088 | Minimal kirlenme |
| **Buhar ve Gazlar** | | |
| Buhar (yağ izi yok) | 0.000088 | Temiz |
| Buhar (yağ izli) | 0.000176 | Yağ filmi |
| Soğutma havası | 0.000176 | Toz bağlı |
| Baca gazı (doğalgaz) | 0.000176 | Düşük kirlenme |
| Baca gazı (fuel oil) | 0.000528 | Kül ve is |
| Baca gazı (kömür) | 0.000880 | Yüksek kül |
| Sıcak hava (temiz) | 0.000088 | Temiz |
| **Yağlı Akışkanlar** | | |
| Motor yağı | 0.000176 | Standart |
| Hidrolik yağ | 0.000176 | Temiz |
| Termal yağ (250°C altı) | 0.000176 | Normal |
| Termal yağ (250°C üstü) | 0.000352 | Cracking riski |
| Fuel oil (No. 2) | 0.000352 | Orta |
| Fuel oil (No. 6 / bunker) | 0.000880 | Yüksek kirlenme |
| Ham petrol | 0.000352 - 0.000528 | Değişken |
| **Proses Akışkanları** | | |
| Organik solventler | 0.000176 | Genel |
| Glikol çözeltileri | 0.000176 | Anti-freeze |
| Polimerler | 0.000528 - 0.000880 | Viskoz |
| Gıda ürünleri (süt) | 0.000176 - 0.000352 | Protein birikmesi |

### 5.2 Kirlenme Etkisi — U-Değer Düşüşü Tablosu

| Temiz U [W/(m2·K)] | R_f_toplam [m2·K/W] | Kirli U [W/(m2·K)] | U Düşüşü [%] |
|---------------------|---------------------|---------------------|-------------|
| 500 | 0.000176 | 458 | 8.4 |
| 500 | 0.000352 | 423 | 15.4 |
| 500 | 0.000528 | 392 | 21.6 |
| 1,000 | 0.000176 | 851 | 14.9 |
| 1,000 | 0.000352 | 740 | 26.0 |
| 1,000 | 0.000528 | 654 | 34.6 |
| 2,000 | 0.000176 | 1,471 | 26.5 |
| 2,000 | 0.000352 | 1,149 | 42.6 |
| 2,000 | 0.000528 | 944 | 52.8 |
| 3,000 | 0.000176 | 1,899 | 36.7 |
| 3,000 | 0.000352 | 1,383 | 53.9 |
| 3,000 | 0.000528 | 1,087 | 63.8 |

**Önemli Gözlem:** Yüksek U değerli eşanjörlerde (plakalı, buhar-su) kirlenme etkisi
orantısal olarak daha büyüktür. Örneğin, temiz U = 3,000 olan bir plakalı eşanjörde
R_f = 0.000352 ile %53.9 performans kaybı oluşurken, temiz U = 500 olan bir gaz-su
ekonomizerde aynı kirlenme yalnızca %15.4 kayba neden olur.

## 6. Basınç Düşüşü Benchmarkları

### 6.1 Eşanjör Tipine Göre Tipik Basınç Düşüşü

| Eşanjör Tipi | Taraf | Tipik DP [kPa] | Maksimum Önerilen DP [kPa] |
|--------------|-------|---------------|--------------------------|
| Gövde-boru | Boru | 15 - 70 | 100 |
| Gövde-boru | Gövde | 20 - 80 | 100 |
| Plakalı | Her plaka tarafı | 20 - 100 | 150 |
| Hava soğutmalı | Boru (proses) | 10 - 50 | 70 |
| Hava soğutmalı | Hava tarafı | 0.1 - 0.5 | 1.0 |
| Çift borulu | İç boru | 10 - 50 | 70 |
| Çift borulu | Halkalı bölge | 15 - 60 | 80 |
| Spiral | Her taraf | 30 - 100 | 150 |
| Ekonomizer | Gaz tarafı | 0.5 - 3.0 | 5.0 |
| Ekonomizer | Su tarafı | 50 - 200 | 300 |

### 6.2 Kabul Edilebilir DP/Q Oranları

| Akışkan | DP/Q [kPa/kW] | Açıklama |
|---------|-------------|----------|
| Su (düşük viskozite) | < 0.05 | İdeal |
| Su (yüksek debi) | 0.05 - 0.15 | Kabul edilebilir |
| Yağ | 0.10 - 0.50 | Yüksek viskozite |
| Gaz (atmosferik) | 0.001 - 0.01 | Düşük yoğunluk |
| Buhar | 0.01 - 0.05 | Faz değişimi |

## 7. Performans Sınıflandırma Tablosu

### 7.1 Genel Performans Değerlendirmesi

| Parametre | Düşük | Ortalama | İyi | Best-in-class |
|-----------|-------|----------|-----|---------------|
| Exergy verimi (eta_ex) | < 25% | 25-40% | 40-55% | > 55% |
| Etkililik (epsilon) | < 0.50 | 0.50-0.70 | 0.70-0.85 | > 0.85 |
| Temizlik faktörü (CF) | < 0.60 | 0.60-0.75 | 0.75-0.85 | > 0.85 |
| DP/Tasarım DP | > 1.50 | 1.20-1.50 | 1.00-1.20 | < 1.00 |
| DT_approach/Tasarım | > 2.00 | 1.30-2.00 | 1.00-1.30 | ≈ 1.00 |

### 7.2 Eşanjör Tipine Göre Özet Puan Kartı

| Eşanjör Tipi | Tipik eta_ex | Tipik epsilon | Tipik CF | Öneri |
|--------------|-------------|--------------|---------|-------|
| Gövde-boru (yeni) | %35-45 | 0.65-0.75 | > 0.90 | Referans |
| Gövde-boru (eski) | %20-30 | 0.50-0.65 | 0.60-0.80 | Temizlik + denetim |
| Plakalı (yeni) | %45-55 | 0.80-0.90 | > 0.90 | Referans |
| Plakalı (eski) | %30-40 | 0.65-0.80 | 0.65-0.85 | Conta + temizlik |
| Ekonomizer | %25-35 | 0.55-0.70 | 0.70-0.85 | Kurum temizliği |
| Hava soğutmalı | %18-28 | 0.45-0.60 | 0.75-0.90 | Fan optimizasyonu |

## 8. Enerji Verimi vs Exergy Verimi Karşılaştırması

Bu ExergyLab'ın temel farklılaşma noktasıdır. Aşağıdaki tablo, aynı eşanjör
için enerji ve exergy verimliliğinin neden farklı olduğunu gösterir:

| Senaryo | Q [kW] | epsilon | eta_ex | Yorum |
|---------|--------|---------|--------|-------|
| Su-su, DT_lm=5°C | 500 | 0.90 | 0.72 | Düşük DT, yüksek exergy verimi |
| Su-su, DT_lm=30°C | 500 | 0.65 | 0.38 | Yüksek DT, düşük exergy verimi |
| Buhar-su, 150°C→80°C | 1,000 | 0.85 | 0.45 | Faz değişimi, orta exergy verimi |
| Gaz-su, 400°C→180°C | 800 | 0.55 | 0.32 | Büyük DT, düşük exergy verimi |
| Gaz-hava, 250°C→120°C | 200 | 0.48 | 0.18 | İki taraf da düşük h |

**Anahtar Gözlem:** Enerji verimi (epsilon) yüksek olsa bile, sıcaklık farkı
büyükse exergy verimi düşük olabilir. ExergyLab bu farkı ortaya koyar ve
gerçek termodinamik iyileştirme potansiyelini gösterir.

### 8.1 Neden Exergy Analizi Gerekli?

1. **Enerji analizi yanıltıcı olabilir:** %90 enerji verimli bir eşanjör,
   exergy açısından %30 verimli olabilir.
2. **Exergy, iyileştirme potansiyelini gösterir:** Yüksek exergy yıkımı olan
   noktalar öncelikli iyileştirme alanlarını işaretler.
3. **Ekonomik optimizasyon:** Exergy yıkımının parasal değeri, termoekonomik
   analiz ile hesaplanabilir.
4. **Cross-equipment fırsatlar:** Bir ekipmanın atık exergy'si başkasının
   girdisi olabilir (örneğin, baca gazı ekonomizeri).

## 9. Sektörel Benchmark Değerleri

| Sektör | Tipik HX Tipi | Tipik eta_ex | İyileştirme Potansiyeli |
|--------|--------------|-------------|------------------------|
| Petrokimya | Gövde-boru, finli boru | %30-45 | %10-20 (fouling azaltma) |
| Gıda | Plakalı, kazıyıcılı | %25-40 | %15-25 (CIP optimizasyonu) |
| Enerji (santraller) | Ekonomizer, ön ısıtıcı | %25-40 | %10-15 (yüzey temizliği) |
| HVAC | Plakalı, cross-flow | %20-35 | %10-20 (kontrol iyileştirme) |
| Kimya | Gövde-boru, spiral | %30-50 | %10-15 (tasarım optimizasyonu) |
| Metal işleme | Reküperatör | %25-45 | %15-25 (izolasyon + kontrol) |
| Kağıt/Selüloz | Ekonomizer, hava ön ısıtıcı | %20-35 | %10-20 (kirlenme yönetimi) |

## İlgili Dosyalar

- `heat_exchanger/formulas.md` — Exergy hesaplama formülleri
- `heat_exchanger/audit.md` — Performans denetim metodolojisi
- `heat_exchanger/standards.md` — TEMA, ASME standartları
- `heat_exchanger/case_studies.md` — Uygulama örnekleri

## Referanslar

1. TEMA (2019). *Standards of the Tubular Exchanger Manufacturers Association*. 10th ed.
2. Shah, R.K. & Sekulic, D.P. (2003). *Fundamentals of Heat Exchanger Design*. Wiley.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
4. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
5. Kakac, S., Liu, H. & Pramuanjaroenkij, A. (2012). *Heat Exchangers: Selection, Rating, and Thermal Design*. 3rd ed., CRC Press.
6. ESDU Data Items 86018, 87019, 98003. *Heat Exchanger Fouling*.
7. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press.
8. ASME PTC 12.5 (2000). *Single Phase Heat Exchangers Performance Test Code*.
9. Linnhoff, B. et al. (1982). *User Guide on Process Integration for the Efficient Use of Energy*. IChemE.
