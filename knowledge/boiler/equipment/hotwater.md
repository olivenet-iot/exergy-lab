---
title: "Sıcak Su Kazanı — Hot Water Boiler"
category: equipment
equipment_type: boiler
subtype: "Sıcak Su Kazanı"
keywords: [sıcak su kazanı, ısıtma, kazan]
related_files: [boiler/benchmarks.md, boiler/formulas.md, boiler/solutions/insulation.md]
use_when: ["Sıcak su kazanı analizi yapılırken", "Isıtma sistemi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Sıcak Su Kazanı — Hot Water Boiler

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Sıcak su kazanı (<110°C), kızgın su kazanı / pressurized hot water (>110°C, 180°C'ye kadar)
- Kapasite aralığı: 50 kW - 20 MW (termik)
- Basınç aralığı: 2-6 bar (tipik kapalı devre ısıtma), 16 bar'a kadar (kızgın su sistemleri)
- Besleme sıcaklığı (supply): 60-90°C (bina ısıtma), 110-180°C (proses, kızgın su)
- Dönüş sıcaklığı (return): 40-70°C (bina ısıtma), 70-120°C (proses)
- Verimlilik (LHV bazlı): %85-95 (non-condensing), %97-107 (condensing, LHV referansla >%100)
- Exergy verimi: %8-25 (düşük — sebebi aşağıda açıklanmıştır)
- Yakıt tipleri: Doğalgaz, LPG, fuel-oil, motorin, biyokütle, hidrojen karışımları
- Yaygın markalar: Viessmann, Buderus, Bosch (Loos), Riello, De Dietrich, Alarko, E.C.A.

## Çalışma Prensibi
Sıcak su kazanı, yakıtın yanma odasında yakılmasıyla oluşan sıcak gazların ısı değiştirici
yüzeylerden geçirilerek suya ısı aktarması prensibine dayanır. Buhar kazanından temel farkı,
suyun faz değişimine uğramamasıdır — su sıvı fazda kalır ve kapalı bir devre içinde
sirkülasyon yapar.

**Temel çalışma adımları:**
1. Yakıt brülörde (burner) yakılır, alev sıcaklığı ~1800-1950°C (doğalgaz)
2. Sıcak yanma gazları kazan gövdesindeki konveksiyon yüzeylerinden geçer
3. Isı, metal yüzeyler aracılığıyla dolaşım suyuna transfer edilir
4. Sıcak su, pompa ile dağıtım sistemine basılır (supply line)
5. Isıyı kullanıcılara verdikten sonra soğumuş su kazana geri döner (return line)
6. Yanma gazları bacadan atılır (flue gas), sıcaklık tipik 120-200°C (non-condensing)

**Dönüş suyu sıcaklığının önemi:**
- Düşük dönüş suyu sıcaklığı kazan verimini artırır (daha fazla ısı transfer edilir)
- Condensing kazanlarda dönüş suyu <55°C olmalı ki baca gazındaki su buharı yoğunlaşsın
- Non-condensing kazanlarda dönüş suyu >60°C tutulmalı — aksi halde asit yoğunlaşması (acid condensation) korozyona yol açar

**Condensing vs Non-Condensing:**
- Non-condensing: Baca gazı sıcaklığı 120-200°C, verim %85-95 (LHV)
- Condensing: Baca gazı sıcaklığı 40-80°C, su buharı yoğunlaşarak latent ısıyı geri verir, verim %97-107 (LHV bazlı)
- Condensing operasyon ancak düşük dönüş suyu sıcaklığıyla (<55°C doğalgaz için) mümkündür

**Brülör kontrol tipleri:**
- On/Off: Basit, küçük kazanlar, düşük verim kısmi yükte
- Hi/Lo/Off: İki kademeli, orta ölçek
- Modulating (oransal): %30-100 aralığında sürekli ayar, en yüksek verim
- Tam modülasyonlu brülörler hava/yakıt oranını (air-fuel ratio) otomatik optimize eder (O₂ trim control)

## Enerji Dağılımı (Tipik — Non-Condensing Kazan, Doğalgaz)
- Sıcak suya aktarılan faydalı ısı: ~%88-92
- Baca gazı kaybı (flue gas loss): ~%5-8
- Radyasyon ve konveksiyon kayıpları (casing loss): ~%1-2
- Yakılmamış yakıt kaybı (unburnt loss): ~%0.5
- Blöf kaybı (blow-down): yok (kapalı devre, buhar kazanından farkı)
- Diğer kayıplar (start/stop, purge): ~%0.5-1

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Yakıt tüketimi | m³/h veya kg/h | Kapasiteye bağlı | Gaz sayacı veya yakıt debimetresi |
| Besleme suyu sıcaklığı (supply) | °C | 60-90 | Termokuple veya PT100 sensör |
| Dönüş suyu sıcaklığı (return) | °C | 40-70 | Termokuple veya PT100 sensör |
| Su debisi | m³/h | Kapasiteye bağlı | Ultrasonik flowmeter veya orifis |
| Baca gazı sıcaklığı | °C | 80-200 | Baca gazı analizörü veya termokuple |
| Baca gazı O₂ | % | 2-6 | Baca gazı analizörü (Testo, Kane vb.) |

### Opsiyonel (daha detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Baca gazı CO | ppm | 0-100 | Baca gazı analizörü |
| Baca gazı CO₂ | % | 8-12 | Baca gazı analizörü |
| Ortam sıcaklığı | °C | 5-40 | Termometre |
| Kazan gövde yüzey sıcaklığı | °C | 30-60 | Infrared termometre |
| Elektrik tüketimi (pompa, fan) | kW | 0.5-50 | Güç analizörü |
| Yük oranı (modülasyon) | % | 0-100 | BMS veya kontrol paneli |
| Çalışma saati / start-stop sayısı | saat / adet | — | Kazan kontrol paneli |

### Nameplate Bilgileri
- Marka ve model
- Nominal termik kapasite (kW veya kcal/h)
- Nominal yakıt tüketimi (m³/h veya kg/h)
- Maksimum çalışma basıncı (bar)
- Maksimum çalışma sıcaklığı (°C)
- Nominal verim (%)
- Üretim yılı
- Seri numarası

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Besleme sıcaklığı | 80°C | Bina ısıtma tipik değeri |
| Dönüş sıcaklığı | 60°C | ΔT = 20°C tipik |
| Baca gazı sıcaklığı | 160°C | Non-condensing, orta yaşlı kazan |
| Baca gazı O₂ | %4 | Makul bakımlı brülör |
| Kazan verimi (LHV) | %90 | Non-condensing doğalgaz kazanı |
| Kazan verimi (LHV) | %104 | Condensing doğalgaz kazanı |
| Ortam sıcaklığı | 20°C | Kazan dairesi |
| Su basıncı | 3 bar | Kapalı devre ısıtma |
| Yük oranı | %65 | Sezonluk ortalama (ısıtma) |
| Çalışma saati | 3000 saat/yıl | Türkiye ikliminde ısıtma sezonu |
| Yakıt alt ısıl değeri (LHV) doğalgaz | 34.02 MJ/m³ | Türkiye şebeke doğalgazı tipik |
| Yakıt üst ısıl değeri (HHV) doğalgaz | 37.78 MJ/m³ | LHV × 1.11 |
| Radyasyon kaybı | %1.5 | İzolasyonlu kazan |
| Fazla hava oranı (excess air) | %25 | O₂ ≈ %4'e karşılık gelir |

## Exergy Verimi Açıklaması

Sıcak su kazanlarının exergy verimi **%8-25** aralığındadır ve bu değer enerji verimine
(%85-95) kıyasla çok düşüktür. Bunun temel sebebi **sıcaklık kalitesi uyumsuzluğudur**
(temperature quality mismatch).

**Exergy yıkımının fiziksel açıklaması:**

Doğalgaz yanma sıcaklığı ~1900°C iken, üretilen sıcak su yalnızca 60-90°C'dir.
Termodinamik açıdan yüksek kaliteli enerji (yüksek sıcaklıktaki yanma) düşük
kaliteli bir çıktıya (ılık su) dönüştürülmektedir. Bu süreçte muazzam miktarda
exergy yıkılır (destroyed). Carnot faktörü ile düşünürsek:

```
Yakıt exergy faktörü (doğalgaz):
  φ_fuel ≈ 1.04  (kimyasal exergy / LHV oranı)

Sıcak su Carnot faktörü:
  η_Carnot = 1 - T₀/T_supply
  T₀ = 293 K (20°C ortam)
  T_supply = 353 K (80°C)
  η_Carnot = 1 - 293/353 = 0.170 (%17)

Burada:
  φ_fuel  = yakıtın exergy faktörü (doğalgaz için ~1.04)
  η_Carnot = Carnot faktörü (sıcak suyun teorik iş üretme kapasitesi)
  T₀      = referans (ortam) sıcaklığı [K]
  T_supply = besleme suyu sıcaklığı [K]
```

Bu demektir ki 80°C'lik sıcak suyun taşıdığı exergy, enerjisinin yalnızca %17'sidir.
Kazan %90 enerji veriminde çalışsa bile:

```
Exergy verimi (yaklaşık):
  ψ = (Q_dot × η_Carnot) / (m_fuel × LHV × φ_fuel)
  ψ ≈ 0.90 × 0.170 / 1.04
  ψ ≈ 0.147 = %14.7

Burada:
  ψ        = exergy verimi (psi)
  Q_dot    = faydalı ısı transfer hızı [kW]
  η_Carnot = Carnot faktörü (çıkış sıcaklığına bağlı)
  m_fuel   = yakıt kütle debisi [kg/s]
  LHV      = yakıt alt ısıl değeri [kJ/kg]
  φ_fuel   = yakıtın exergy faktörü [-]
```

**Daha hassas hesaplama (logaritmik ortalama sıcaklık ile):**

```
Sıcak su exergy akışı:
  Ex_water = m_w × Cp × [(T_s - T_r) - T₀ × ln(T_s / T_r)]

Burada:
  Ex_water = suyun exergy akışı [kW]
  m_w      = su kütle debisi [kg/s]
  Cp       = suyun özgül ısısı [kJ/(kg·K)] ≈ 4.18
  T_s      = besleme suyu sıcaklığı [K]
  T_r      = dönüş suyu sıcaklığı [K]
  T₀       = referans sıcaklığı [K] = 293 K (20°C)
```

**Sıcaklık seviyesine göre exergy verimi karşılaştırması:**

| Çıkış Sıcaklığı | Uygulama | Carnot Faktörü | Yaklaşık Exergy Verimi |
|------------------|----------|----------------|----------------------|
| 40°C | Yerden ısıtma | %6.4 | %5-6 |
| 60°C | Düşük sıcaklık ısıtma | %12.0 | %10-11 |
| 80°C | Radyatör ısıtma | %17.0 | %14-15 |
| 90°C | Yüksek sıcaklık ısıtma | %19.2 | %16-17 |
| 120°C | Proses (kızgın su) | %25.4 | %21-22 |
| 160°C | Proses (kızgın su) | %33.2 | %27-29 |

**Sonuç:** Sıcak su kazanı enerji açısından verimli (%90+) olsa da, exergy açısından
son derece verimsizdir. Bunun sebebi termodinamik bir zorunluluktur — düşük sıcaklık
gereksinimleri için yüksek sıcaklıklı yanma kullanmak kaçınılmaz exergy yıkımı yaratır.
Isı pompası, güneş enerjisi veya atık ısı geri kazanımı gibi alternatifler exergy
açısından çok daha üstündür.

## Performans Tablosu

| Parametre | Eski Kazan (>15 yıl) | Modern Non-Condensing | Modern Condensing |
|-----------|-----------------------|-----------------------|-------------------|
| Verim (LHV) | %82-88 | %90-95 | %97-107 |
| Baca gazı sıcaklığı | 180-250°C | 120-160°C | 40-80°C |
| Baca gazı O₂ | %5-8 | %3-5 | %3-4 |
| Fazla hava | %30-60 | %15-30 | %15-20 |
| CO emisyonu | 50-200 ppm | 10-50 ppm | <20 ppm |
| NOₓ emisyonu | 100-250 mg/m³ | 40-100 mg/m³ | <30 mg/m³ |
| Radyasyon kaybı | %2-4 | %1-1.5 | %0.5-1 |
| Exergy verimi (80°C) | %11-13 | %14-15 | %15-17 |
| Yatırım maliyeti | — | 15-30 €/kW | 25-50 €/kW |
| Geri ödeme süresi | — | — | 2-5 yıl (eski kazana göre) |

## Tipik İyileştirme Fırsatları

| İyileştirme | Enerji Tasarrufu | Exergy İyileşmesi | Tahmini Maliyet |
|-------------|------------------|---------------------|-----------------|
| Condensing kazana geçiş | %10-15 | %2-4 puan | 25-50 €/kW |
| Brülör optimizasyonu (O₂ trim) | %2-4 | %0.5-1 puan | 2.000-10.000 € |
| Ekonomizer ekleme | %3-5 | %0.5-1 puan | 5.000-20.000 € |
| İzolasyon iyileştirme | %1-2 | %0.2-0.3 puan | 1.000-5.000 € |
| Modulating brülör | %3-8 | %0.5-1.5 puan | 3.000-15.000 € |
| Dönüş suyu sıcaklığını düşürme | %2-5 | %1-3 puan | Sistem optimizasyonu |
| Isı pompası hibrit sistem | %30-50 | %15-30 puan | 100-300 €/kW |

## Dikkat Edilecekler

1. **Dönüş suyu sıcaklığı**: Non-condensing kazanlarda dönüş suyu <60°C'ye düşmemeli — asit yoğunlaşması (SO₂ + H₂O → H₂SO₃) kazan ömrünü kısaltır. Condensing kazanlarda ise düşük dönüş suyu sıcaklığı hedeflenmeli (<55°C)
2. **Fazla hava kontrolü**: O₂ seviyesi %3-4 aralığında tutulmalı. Yüksek fazla hava baca gazı kaybını artırır — her %1 O₂ fazlası ≈ %0.5 verim kaybı
3. **Start/stop kayıpları**: Sık start-stop (cycling) hem verim düşürür hem mekanik aşınma yaratır — modulating brülör ve tampon tankı (buffer tank) değerlendirilmeli
4. **Baca gazı sıcaklığı trendi**: Zamanla artan baca gazı sıcaklığı ısı transfer yüzeylerinde kirlenme (fouling) göstergesidir — yıllık kazan temizliği planlanmalı
5. **İzolasyon kontrolü**: Kazan gövde yüzey sıcaklığı IR termometre ile kontrol edilmeli — 50°C üzeri yüzey sıcaklığı yetersiz izolasyon göstergesidir
6. **Sistem dengeleme**: Dengesiz dağıtım devresi bazı bölgelerin aşırı ısıtılmasına (overheating) yol açar — bu hem enerji hem exergy kaybıdır
7. **Exergy perspektifi**: Düşük sıcaklık gereksinimleri (yerden ısıtma, 35-40°C) için sıcak su kazanı kullanmak exergy açısından son derece verimsizdir — bu uygulamalar için ısı pompası (COP 3-5) exergy verimini 3-5 kat artırabilir

## İlgili Dosyalar
- Buhar kazanı: `equipment/boiler_steam.md`
- Ekonomizer: `equipment/economizer.md`
- Brülör bilgileri: `equipment/burner.md`
- Baca gazı ısı geri kazanımı: `solutions/flue_gas_heat_recovery.md`
- Condensing kazan dönüşümü: `solutions/condensing_boiler_upgrade.md`
- Isı pompası hibrit sistem: `solutions/heat_pump_hybrid.md`
- Kazan exergy hesaplamaları: `formulas/boiler_exergy.md`
- Benchmark verileri: `benchmarks/boiler_benchmarks.md`

## Referanslar
- Bejan, A., Tsatsaronis, G., Moran, M. "Thermal Design and Optimization", Wiley, 1996
- Kotas, T.J. "The Exergy Method of Thermal Plant Analysis", Krieger Publishing, 1995
- ASHRAE Handbook — HVAC Systems and Equipment, 2024
- Viessmann Technical Guide — Hot Water Boilers
- Bosch Thermotechnology — Kazan Teknik Dokümantasyonu
- EN 15502-1: Gaz yakan merkezi ısıtma kazanları standardı
- TSE (Türk Standartları Enstitüsü), TS EN 303-5: Katı yakıtlı kazanlar
- DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry" (applicable principles)
