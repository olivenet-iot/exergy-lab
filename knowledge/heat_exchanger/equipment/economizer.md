---
title: "Ekonomizerler (Boiler Economizers)"
category: equipment
equipment_type: heat_exchanger
subtype: "Ekonomizer"
keywords: [ekonomizer, economizer, baca gazı, ısı geri kazanımı, yoğuşmalı, asit çiğ noktası, kanatlı boru]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md, boiler/solutions/economizer.md, boiler/equipment/systems_overview.md]
use_when: ["Ekonomizer analizi yapılırken", "Baca gazı ısı geri kazanımı değerlendirilirken", "Yoğuşmalı ekonomizer potansiyeli incelenirken"]
priority: high
last_updated: 2026-02-01
---
# Ekonomizerler — Boiler Economizers

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Ekonomizerler (economizers), kazan baca gazının artık ısısını kullanarak besleme suyunu veya prosese giden akışkanı ön ısıtan ısı eşanjörleridir. Kazan sistemlerinde en etkili enerji geri kazanım yatırımlarından biridir. Tipik olarak %3-10 yakıt tasarrufu sağlar.

- Kapasite aralığı: 50 kW - 50 MW (baca gazı tarafı)
- Baca gazı sıcaklığı (giriş): 150-450°C
- Baca gazı sıcaklığı (çıkış): 80-180°C (yoğuşmasız), 30-60°C (yoğuşmalı)
- Besleme suyu sıcaklığı artışı: 20-80°C
- Tipik U değeri: 30-200 W/(m²·K) (baca gazı tarafı kontrollü)
- Tipik exergy verimi: 30-65%

## Ekonomizer Tipleri

### Yoğuşmasız (Non-Condensing) Ekonomizer

Baca gazını asit çiğ noktasının (acid dew point) üzerinde tutar. Konvansiyonel ekonomizer tipidir.

```
Yoğuşmasız ekonomizer çalışma aralığı:

  Baca gazı giriş: 200-450°C
  Baca gazı çıkış: 120-180°C (asit çiğ noktası üzerinde)
  Besleme suyu giriş: 60-105°C
  Besleme suyu çıkış: 100-150°C

  Minimum baca gazı çıkış sıcaklığı sınırı:
    Doğalgaz:  T_çiğ ≈ 60-80°C  → T_min = 90-100°C (güvenlik marjı ile)
    Fuel oil:  T_çiğ ≈ 120-150°C → T_min = 140-170°C
    Kömür:     T_çiğ ≈ 110-140°C → T_min = 130-160°C
    Biyokütle: T_çiğ ≈ 90-130°C  → T_min = 110-150°C

Burada:
  T_çiğ : Asit çiğ noktası (acid dew point) (°C)
  Kükürt içeriği arttıkça asit çiğ noktası yükselir
```

### Yoğuşmalı (Condensing) Ekonomizer

Baca gazını çiğ noktasının altına soğutarak su buharının yoğuşma ısısını da geri kazanır. Sadece doğalgaz yakıtlı kazanlarda yaygındır (düşük kükürt).

```
Yoğuşmalı ekonomizer çalışma aralığı:

  Baca gazı giriş: 150-250°C
  Baca gazı çıkış: 30-60°C (su çiğ noktasının altında)
  Besleme/dönüş suyu giriş: 20-60°C
  Besleme/dönüş suyu çıkış: 60-90°C

  Su çiğ noktası (doğalgaz yanma ürünü):
    T_su_çiğ ≈ 55-60°C (%10-12 H₂O baca gazında)

  Geri kazanılan ek enerji:
    Su buharı yoğuşma gizli ısısı: ~2,450 kJ/kg_su
    Doğalgaz baca gazında: ~1.6 kg_su / Nm³_gaz
    Potansiyel ek verim: %5-12 (LHV bazında)
    HHV bazlı verim: %95-99 (teorik)
```

### Tip Karşılaştırma Tablosu

| Özellik | Yoğuşmasız | Yoğuşmalı |
|---------|------------|-----------|
| Baca gazı çıkış sıcaklığı | 120-180°C | 30-60°C |
| Verim artışı (LHV bazlı) | %3-6 | %8-15 |
| Yakıt sınırlaması | Tüm yakıtlar | Genellikle doğalgaz |
| Malzeme gereksinimleri | Karbon çelik veya düşük alaşım | Paslanmaz çelik, polimer kaplama |
| Korozyon riski | Düşük (çiğ noktası üzerinde) | Yüksek (asidik yoğuşma) |
| Yatırım maliyeti | Düşük-Orta | Orta-Yüksek |
| Geri ödeme süresi | 1-3 yıl | 2-5 yıl |
| Bakım gereksinimi | Düşük | Orta (korozyon izleme) |

## Asit Çiğ Noktası (Acid Dew Point)

### Hesaplama ve Eşik Değerleri

```
SO₃ oluşumu ve asit çiğ noktası:

  Yanma sırasında: S + O₂ → SO₂
  Katalitik oksidasyon: SO₂ + ½O₂ → SO₃ (dönüşüm: %1-5)
  Su buharı ile: SO₃ + H₂O → H₂SO₄ (sülfürik asit)

Asit çiğ noktası tahmini (Verhoff & Banchero korelasyonu):

  T_ADP (K) = 1000 / [2.276 - 0.0294 × ln(P_H₂O) - 0.0858 × ln(P_SO₃) + 0.0062 × ln(P_H₂O × P_SO₃)]

Burada:
  P_H₂O : Su buharı kısmi basıncı (atm)
  P_SO₃ : SO₃ kısmi basıncı (atm)
  T_ADP : Asit çiğ noktası (K)

Yakıta göre tipik asit çiğ noktası:
  Doğalgaz (S ≈ 0):      T_ADP ≈ 60-75°C
  Düşük kükürtlü fuel oil: T_ADP ≈ 120-135°C
  Yüksek kükürtlü fuel oil: T_ADP ≈ 140-160°C
  Kömür (orta S):           T_ADP ≈ 115-140°C
```

### Güvenlik Marjı

| Yakıt | Asit Çiğ Noktası (°C) | Güvenlik Marjı (°C) | Min Baca Gazı Çıkışı (°C) |
|-------|------------------------|---------------------|---------------------------|
| Doğalgaz | 60-75 | 15-25 | 80-100 |
| LPG | 55-70 | 15-25 | 75-95 |
| Düşük S fuel oil | 120-135 | 15-20 | 140-155 |
| Yüksek S fuel oil | 140-160 | 15-20 | 160-180 |
| Kömür (orta S) | 115-140 | 15-25 | 135-165 |
| Biyokütle | 90-130 | 15-25 | 110-155 |

## Malzeme Seçimi

### Düşük Sıcaklık Korozyona Dirençli Malzemeler

| Malzeme | Maks Korozyon Direnci (°C) | Maliyet | Uygulama |
|---------|--------------------------|---------|----------|
| Karbon çelik | >Asit çiğ noktası | Düşük | Yoğuşmasız ekonomizer |
| Corten çelik (hava koşullarına dayanıklı) | 80-120°C | Düşük-Orta | Orta bölge koruma |
| Paslanmaz çelik 316L | 50-80°C (zayıf H₂SO₄) | Yüksek | Yoğuşmalı ekonomizer |
| Paslanmaz çelik 904L | 40-70°C | Çok yüksek | Agresif yoğuşma |
| Teflon kaplama | 30-60°C | Orta-Yüksek | Yoğuşmalı ekonomizer |
| Cam/emaye kaplama | 30-80°C | Orta | Yoğuşmalı ekonomizer |
| Polimer (PP/PVDF) | 30-60°C (düşük sıcaklık) | Orta | Yoğuşmalı, düşük sıcaklık |

### Kanatlı Boru vs Çıplak Boru

| Özellik | Kanatlı Boru (Finned Tube) | Çıplak Boru (Bare Tube) |
|---------|--------------------------|------------------------|
| Hava tarafı alan artışı | 5-15× | 1× (referans) |
| U değeri (baca gazı/su) | 60-150 W/(m²·K) | 30-60 W/(m²·K) |
| Boyut (aynı kapasite) | Kompakt | 2-4× daha büyük |
| Kirlenme eğilimi | Yüksek (kanatlar arası) | Düşük |
| Temizlik kolaylığı | Zor (kurum üfleme gerekli) | Kolay |
| Maliyet (aynı kapasite) | Düşük-Orta | Yüksek (büyük boyut) |
| Tipik uygulama | Temiz yakıt (doğalgaz) | Kirli yakıt (kömür, fuel oil) |

### Kanat Malzemeleri

| Kanat Malzemesi | Maks Sıcaklık (°C) | Kanat Verimi | Uygulama |
|----------------|---------------------|--------------|----------|
| Alüminyum | 200 | 0.90-0.95 | Düşük sıcaklık ekonomizer |
| Karbon çelik | 450 | 0.65-0.80 | Yüksek sıcaklık ekonomizer |
| Paslanmaz çelik | 600 | 0.55-0.70 | Korozif baca gazı |

## Enerji ve Exergy Tasarruf Hesaplamaları

### Enerji Tasarrufu

```
Ekonomizer enerji tasarrufu:

  Q_eko = m_baca × cp_baca × (T_baca,giriş - T_baca,çıkış)

  veya su tarafından:
  Q_eko = m_su × cp_su × (T_su,çıkış - T_su,giriş)

Yakıt tasarrufu:
  ΔYakıt = Q_eko / (η_kazan × LHV)

Verim artışı:
  Δη = Q_eko / Q_yakıt_giriş × 100%

Pratik kural:
  Her 20°C baca gazı sıcaklığı düşüşü ≈ %1 kazan verimi artışı

Burada:
  m_baca  : Baca gazı kütle debisi (kg/s)
  cp_baca : Baca gazı özgül ısısı (~1.05-1.10 kJ/(kg·K))
  LHV     : Yakıt alt ısıl değeri (kJ/kg veya kJ/m³)
```

### Yoğuşmalı Ekonomizer Ek Tasarruf

```
Yoğuşmalı ekonomizer ek enerji:

  Q_yoğuşma = m_su_yoğuşan × h_fg

Burada:
  m_su_yoğuşan : Yoğuşan su buharı debisi (kg/s)
  h_fg          : Suyun buharlaşma gizli ısısı (~2,450 kJ/kg @ 1 atm)

Doğalgaz yanma ürünlerinden:
  1 Nm³ doğalgaz → ~1.6 kg su buharı
  Tam yoğuşma ile geri kazanılabilir enerji: ~1.6 × 2,450 = 3,920 kJ/Nm³
  LHV doğalgaz: ~34,500 kJ/Nm³
  Potansiyel ek verim: 3,920 / 34,500 = %11.4 (teorik maksimum)
  Pratikte (%60-80 yoğuşma): %7-9 ek verim
```

### Exergy Analizi

```
Ekonomizer exergy analizi:

Baca gazı exergysi:
  Ex_baca = m_baca × cp_baca × [(T_baca - T₀) - T₀ × ln(T_baca/T₀)]

Su exergysi:
  Ex_su = m_su × cp_su × [(T_su - T₀) - T₀ × ln(T_su/T₀)]

Exergy verimi:
  η_ex = (Ex_su,çıkış - Ex_su,giriş) / (Ex_baca,giriş - Ex_baca,çıkış)

Exergy yıkımı:
  Ex_yıkım = (Ex_baca,giriş - Ex_baca,çıkış) - (Ex_su,çıkış - Ex_su,giriş)

Tipik exergy verimleri:

  Yoğuşmasız (doğalgaz):
    Baca gazı: 250°C → 130°C
    Su: 80°C → 120°C
    η_ex ≈ 40-55%

  Yoğuşmalı (doğalgaz):
    Baca gazı: 200°C → 45°C
    Su: 30°C → 70°C
    η_ex ≈ 25-40% (düşük sıcaklıkta düşük exergy kalitesi)
    Ancak enerji verimi çok yüksek!

Not: Yoğuşmalı ekonomizer yüksek enerji verimi sağlar ancak geri kazanılan
ısının exergy kalitesi düşüktür (düşük sıcaklık). Bu, exergy açısından
dikkatli değerlendirilmesi gereken bir noktadır.
```

### Exergy Yıkım Kaynakları

| Kaynak | Payı (%) | Azaltma Yöntemi |
|--------|---------|-----------------|
| Sonlu sıcaklık farkı (ΔT) | 70-85 | Daha büyük eşanjör, karşı akış |
| Basınç düşüşü (baca gazı tarafı) | 5-15 | Optimal kanat tasarımı, düşük hız |
| Kirlenme (kurum) | 5-15 | Düzenli kurum üfleme, temiz yakıt |
| Çevre kaybı (izolasyon) | 2-5 | Yeterli izolasyon |

## Kazan Sistemi Entegrasyonu

### Yerleşim ve Bağlantı

```
Tipik kazan sistemi ekonomizer yerleşimi:

  KAZAN → [Buhar/Su çıkış]
    ↓
  BACA GAZI (250-400°C)
    ↓
  [EKONOMİZER] → Besleme suyu ön ısıtma (80°C → 120°C)
    ↓
  BACA GAZI (130-180°C)
    ↓
  [HAVA ÖN ISITICI] → Yanma havası ısıtma (opsiyonel)
    ↓
  BACA GAZI (100-150°C)
    ↓
  [YOĞUŞMALI EKONOMİZER] → Düşük sıcaklık ısıtma (opsiyonel)
    ↓
  BACA GAZI (40-60°C)
    ↓
  BACA
```

### Entegrasyon Noktaları

| Entegrasyon | Kaynak | Isıtılan Akışkan | Tipik Tasarruf |
|-------------|--------|-------------------|----------------|
| Besleme suyu ön ısıtma | Yüksek sıcaklık baca gazı | Kazan besleme suyu | %3-6 yakıt |
| Kondensat ısıtma | Orta sıcaklık baca gazı | Kondensat geri dönüş | %1-3 yakıt |
| Proses suyu ısıtma | Yoğuşmalı ekonomizer | Proses/DHW suyu | %5-10 yakıt |
| Hava ısıtma | Düşük sıcaklık baca gazı | Tesis/depo ısıtma havası | %2-5 yakıt |
| Sıcak su hazırlama | Yoğuşmalı ekonomizer | Kullanım sıcak suyu | %5-8 yakıt |

## Ekonomik Analiz

### Yatırım Maliyeti

| Tip | Kapasite | Malzeme | Maliyet (EUR) | EUR/kW |
|-----|----------|---------|---------------|--------|
| Yoğuşmasız (kanatlı boru) | 100 kW | Karbon çelik | 5,000-12,000 | 50-120 |
| Yoğuşmasız (kanatlı boru) | 500 kW | Karbon çelik | 15,000-35,000 | 30-70 |
| Yoğuşmasız (kanatlı boru) | 2,000 kW | Karbon çelik | 40,000-90,000 | 20-45 |
| Yoğuşmalı | 200 kW | SS316L | 15,000-30,000 | 75-150 |
| Yoğuşmalı | 1,000 kW | SS316L | 40,000-80,000 | 40-80 |
| Yoğuşmalı | 5,000 kW | SS316L | 120,000-250,000 | 24-50 |

### Geri Ödeme Hesabı

```
Ekonomizer geri ödeme süresi:

  Yıllık tasarruf = Q_eko × Çalışma_saati × Yakıt_fiyatı / (η_kazan × LHV)

Örnek (doğalgaz, yoğuşmasız):
  Q_eko = 200 kW
  Çalışma saati = 5,000 h/yıl
  Doğalgaz fiyatı = 0.35 EUR/m³
  LHV = 34.5 MJ/m³ = 9.583 kWh/m³
  η_kazan = 0.90

  Yıllık yakıt tasarrufu = 200 × 5,000 / (0.90 × 9,583) = 115,800 kWh/yıl
  Yakıt hacmi tasarrufu = 115,800 / 9,583 = 12,085 m³/yıl
  Yıllık maliyet tasarrufu = 12,085 × 0.35 = 4,230 EUR/yıl

  Yatırım maliyeti = 15,000 EUR (montaj dahil)
  Geri ödeme = 15,000 / 4,230 = 3.5 yıl
```

## Ölçülmesi Gereken Parametreler

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Baca gazı giriş sıcaklığı | °C | 150-450 | Termoeleman (K tipi) |
| Baca gazı çıkış sıcaklığı | °C | 40-180 | Termoeleman (K tipi) |
| Besleme suyu giriş sıcaklığı | °C | 20-105 | PT100 |
| Besleme suyu çıkış sıcaklığı | °C | 60-150 | PT100 |
| Besleme suyu debisi | m³/h veya kg/s | Sisteme bağlı | Debimetre |
| Baca gazı O₂ oranı | % | 2-6 | O₂ analizörü |
| Baca gazı basınç düşüşü | Pa | 50-500 | Diferansiyel basınç |
| Baca gazı SO₂/SO₃ | ppm | 0-500 | Gaz analizörü |
| Yoğuşma suyu pH | — | 2-5 (asidik) | pH ölçer |

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Kazan ekonomizer çözümü: `boiler/solutions/economizer.md`
- Kazan sistemi: `boiler/equipment/systems_overview.md`
- Hava ön ısıtıcı: `heat_exchanger/equipment/air_preheater.md`
- Kazan formülleri: `boiler/formulas.md`
- Kazan benchmark: `boiler/benchmarks.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`

## Referanslar

- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators: Design, Applications, and Calculations*, Marcel Dekker.
- U.S. DOE/AMO (2012). *Improving Steam System Performance: A Sourcebook for Industry*, 2nd Edition.
- Spirax Sarco (2023). *The Steam and Condensate Loop* — Chapter on Economizers.
- Verhoff, F.H. & Banchero, J.T. (1974). "Predicting Dew Points of Flue Gases," *Chemical Engineering Progress*, 70(8), 71-72.
- EN 12952 — Water-tube Boilers and Auxiliary Installations.
- EN 12953 — Shell Boilers.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*, Wiley.
- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- ASHRAE Handbook — HVAC Systems and Equipment (2024).
