---
title: "Fabrika Seviyesi Exergy Analizi Temelleri (Factory-Level Exergy Analysis Fundamentals)"
category: factory
equipment_type: factory
keywords: [exergy, temel kavramlar, termodinamik]
related_files: [factory/exergy_flow_analysis.md, factory/methodology.md, factory/energy_flow_analysis.md]
use_when: ["Exergy kavramları açıklanırken", "Termodinamik temel bilgiler gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Fabrika Seviyesi Exergy Analizi Temelleri (Factory-Level Exergy Analysis Fundamentals)

> Son güncelleme: 2026-01-31

## Genel Bakış

Exergy (kullanılabilirlik), bir sistemin çevresiyle tam termodinamik dengeye ulaşana kadar üretebileceği maksimum yararlı iştir. Fabrika seviyesinde exergy analizi, enerji analizinin ötesine geçerek enerji kalitesini ve gerçek termodinamik kayıpları ortaya koyar. Birinci yasa (enerji) analizi yalnızca miktarı değerlendirirken, ikinci yasa (exergy) analizi hem miktarı hem kaliteyi değerlendirir.

## 1. Temel Kavramlar (Basic Concepts)

### 1.1 Termodinamiğin İkinci Yasası ve Endüstriyel Sistemler

Termodinamiğin ikinci yasası, tüm gerçek proseslerde entropinin arttığını ve dolayısıyla exergynin yıkıldığını belirtir. Endüstriyel sistemlerde bu yasa şu sonuçları doğurur:

- Yüksek sıcaklıklı enerji kaynakları (yakıt, elektrik) daha değerlidir
- Her enerji dönüşümü kaçınılmaz olarak exergy yıkımı yaratır
- Düşük sıcaklıklı atık ısı düşük exergy içerir ve kullanımı sınırlıdır
- Proseslerin tersinmezliği (irreversibility) gerçek kayıpların ölçüsüdür

### 1.2 Ölü Durum (Dead State) Tanımı

Fabrika exergy analizinde referans çevre koşulları (ölü durum):

```
T₀ = 25°C = 298.15 K (referans sıcaklık)
P₀ = 101.325 kPa = 1 atm (referans basınç)
Referans ortam: %78.09 N₂, %20.95 O₂, %0.93 Ar, %0.03 CO₂

Not: Türkiye koşullarında mevsimsel ortalama sıcaklık kullanılması
önerilir (İstanbul: ~15°C, Ankara: ~12°C, İzmir: ~18°C).
Ancak karşılaştırılabilirlik için 25°C standart referans tercih edilir.
```

### 1.3 Exergy Bileşenleri

Bir madde akışının toplam exergisi dört bileşenden oluşur:

```
Ex_toplam = Ex_fiziksel + Ex_kimyasal + Ex_kinetik + Ex_potansiyel

Burada:
- Ex_fiziksel = (h - h₀) - T₀ × (s - s₀)    [kJ/kg]
- Ex_kimyasal = Σ(xᵢ × μᵢ) - Σ(xᵢ × μᵢ₀)  [kJ/kg]
- Ex_kinetik = V²/2                             [kJ/kg]  (genellikle ihmal edilir)
- Ex_potansiyel = g × z                         [kJ/kg]  (genellikle ihmal edilir)
```

Endüstriyel uygulamalarda fiziksel ve kimyasal exergy bileşenleri baskındır.

## 2. Fabrika Exergy Dengesi (Factory Exergy Balance)

### 2.1 Genel Denge Denklemi

Bir fabrikanın kararli hal (steady-state) exergy dengesi:

```
Ex_giriş = Ex_ürün + Ex_atık + Ex_yıkım

Burada:
Ex_giriş    = Ex_yakıt + Ex_elektrik + Ex_hammadde + Ex_su + Ex_hava
Ex_ürün     = Ex_ana_ürün + Ex_yan_ürünler
Ex_atık     = Ex_baca_gazı + Ex_soğutma_suyu + Ex_atık_malzeme + Ex_ses/titreşim
Ex_yıkım    = Σ Iₖ (tüm alt sistemlerdeki tersinmezlik)
```

### 2.2 Exergy Giriş Kalemleri

| Giriş Kalemi | Exergy Hesabı | Tipik Pay |
|---|---|---|
| Yakıt (doğalgaz) | ṁ_yakıt × ex_ch (φ × LHV) | %60-80 |
| Elektrik | Ẇ_elektrik (saf exergy) | %15-35 |
| Hammadde | Kimyasal exergy | %1-10 |
| Besleme suyu | ṁ_su × ex_su | <%1 |
| Ortam havası | İhmal edilir (T₀, P₀'da) | ~%0 |

### 2.3 Exergy Çıkış ve Kayıp Kalemleri

| Çıkış/Kayıp Kalemi | Exergy Hesabı | Tipik Pay |
|---|---|---|
| Ana ürün exergisi | Ürüne bağlı | %15-50 |
| Baca gazı exergisi | ṁ_bg × [(h-h₀) - T₀(s-s₀)] | %5-15 |
| Soğutma suyu exergisi | ṁ_ss × Cp × [(T-T₀) - T₀ln(T/T₀)] | %1-5 |
| Yanma tersinmezliği | T₀ × S_gen,yanma | %15-30 |
| Isı transferi tersinmezliği | T₀ × S_gen,ısı | %5-20 |
| Sürtünme/basınç düşüşü | T₀ × S_gen,sürtünme | %1-5 |
| Karışım tersinmezliği | T₀ × S_gen,karışım | %1-3 |

## 3. Exergy Verimlilik Tanımları (Exergy Efficiency Definitions)

### 3.1 Basit (Brüt) Exergy Verimi

```
η_ex,basit = Ex_ürün / Ex_giriş × 100 [%]

Örnek:
Ex_giriş = 10,000 kW (yakıt + elektrik)
Ex_ürün = 3,500 kW (buhar + basınçlı hava + soğutma exergisi)
η_ex,basit = 3,500 / 10,000 × 100 = %35.0
```

### 3.2 Rasyonel (Fonksiyonel) Exergy Verimi

Yalnızca istenen çıktının girişteki istenen kaynağa oranı:

```
η_ex,rasyonel = Ex_istenen_çıktı / (Ex_giriş - Ex_kaçınılmaz_kayıp) × 100 [%]
```

### 3.3 Görev (Task) Exergy Verimi

Minimum teorik exergy gereksiniminin gerçek exergy tüketimine oranı:

```
η_ex,görev = Ex_min,teorik / Ex_gerçek × 100 [%]

Bu tanım en düşük değerleri verir ancak en gerçekçi iyileştirme
potansiyelini gösterir.
```

### 3.4 Sektörel Exergy Verimlilikleri

| Sektör | η_ex Tipik Aralık | η_ex En İyi Uygulama | Ana Kayıp Kaynağı |
|---|---|---|---|
| Çimento | %25-35 | %40 | Klinker pişirme tersinmezliği |
| Kimya | %30-50 | %60 | Reaksiyon tersinmezliği |
| Gıda ve içecek | %15-25 | %35 | Düşük sıcaklık prosesleri |
| Tekstil | %20-30 | %40 | Boyama/kurutma kayıpları |
| Metal işleme | %25-40 | %50 | Fırın/ısıl işlem kayıpları |
| Kağıt ve selüloz | %30-45 | %55 | Kurutma tersinmezliği |
| Otomotiv | %20-30 | %38 | Boyahane, basınçlı hava |

## 4. Exergy Yıkım Kaynakları (Sources of Exergy Destruction)

### 4.1 Yanma Tersinmezliği (Combustion Irreversibility)

Endüstriyel sistemlerdeki en büyük exergy yıkım kaynağıdır:

```
I_yanma = T₀ × S_gen,yanma ≈ f_yanma × Ex_yakıt

Tipik değerler:
- Doğalgaz yanması: f_yanma = 0.25-0.30 (%25-30 yakıt exergisi)
- Kömür yanması: f_yanma = 0.30-0.35
- Biyokütle yanması: f_yanma = 0.30-0.38

Bu kayıp termodinamik bir zorunluluktur ve sıfıra indirilemez.
Yalnızca ön ısıtma (rejenerasyon) ile kısmen azaltılabilir.
```

### 4.2 Isı Transferi Tersinmezliği (Heat Transfer Irreversibility)

Sonlu sıcaklık farkı üzerinden ısı transferi exergy yıkımı yaratır:

```
I_ısı = Q̇ × T₀ × (1/T_soğuk - 1/T_sıcak)

Burada:
- Q̇ = transfer edilen ısı [kW]
- T_sıcak = sıcak akışkan sıcaklığı [K]
- T_soğuk = soğuk akışkan sıcaklığı [K]

Azaltma yöntemi: ΔT'yi küçültmek (daha büyük eşanjör alanı)
```

### 4.3 Sürtünme ve Basınç Düşüşü (Friction and Pressure Drop)

```
I_sürtünme = T₀ × ṁ × ΔP / (ρ × T)

Azaltma yöntemi: Boru boyutlarını artırmak, fitingleri azaltmak
```

### 4.4 Karışım Tersinmezliği (Mixing Irreversibility)

Farklı sıcaklık veya konsantrasyondaki akışların karıştırılması:

```
I_karışım = T₀ × Σ(ṁᵢ × sᵢ) - T₀ × ṁ_karışım × s_karışım

Azaltma yöntemi: Farklı sıcaklıklardaki akışları ayrı tutmak,
sıcaklık kademesini (cascading) kullanmak
```

### 4.5 Kısma (Throttling) Tersinmezliği

```
I_kısma = T₀ × ṁ × (s_çıkış - s_giriş) ≈ T₀ × ṁ × R × ln(P_giriş/P_çıkış)

Azaltma yöntemi: Basınç düşürme vanası yerine türbin kullanmak
```

## 5. Grassmann Diyagramları (Grassmann / Exergy Flow Diagrams)

### 5.1 Diyagram Prensipleri

Grassmann diyagramı, Sankey diyagramının exergy versiyonudur. Enerji Sankey diyagramından farklı olarak:

- Akış genişlikleri exergy değerlerini temsil eder
- Exergy yıkımı (tersinmezlik) ok genişliğinin azalmasıyla gösterilir
- Toplam çıkış her zaman toplam girişten küçüktür (exergy korunmaz)
- Kayıp exerginin nereye gittiğini (yıkım vs. atık) net gösterir

### 5.2 Tipik Fabrika Grassmann Diyagramı Yapısı

```
YAKIT EXERGY (%65)  ──────────────────────────────────┐
                                                       │
ELEKTRİK EXERGY (%30) ──────────────────────────────┐ │
                                                     │ │
HAMMADDE EXERGY (%5) ──────────────────────────────┐ │ │
                                                   │ │ │
                    ┌──────────────────────────────┴─┴─┤
                    │      TOPLAM EXERGY GİRİŞİ        │
                    │         (100%)                    │
                    ├──────────────────────────────────┘
                    │
    ┌───────────────┤ Yanma tersinmezliği (%15-25) ──────→ YIKIM
    │               │
    │  ┌────────────┤ Isı transferi tersinmezliği (%8-15) → YIKIM
    │  │            │
    │  │  ┌─────────┤ Motor/pompa tersinmezliği (%3-8) ──→ YIKIM
    │  │  │         │
    │  │  │  ┌──────┤ Baca gazı exergisi (%5-12) ────────→ ATIK
    │  │  │  │      │
    │  │  │  │  ┌───┤ Soğutma kayıpları (%2-5) ──────────→ ATIK
    │  │  │  │  │   │
    │  │  │  │  │   ├──────────────────────────────────────┐
    │  │  │  │  │   │  ÜRÜN EXERGY (%20-45)                │
    │  │  │  │  │   │  (buhar + basınçlı hava + ürün)      │
    │  │  │  │  │   └──────────────────────────────────────┘
```

### 5.3 Enerji vs. Exergy Diyagram Karşılaştırması

| Parametre | Sankey (Enerji) | Grassmann (Exergy) |
|---|---|---|
| Korunum | Enerji korunur (toplam sabit) | Exergy yıkılır (toplam azalır) |
| Atık ısı | Büyük görünür (%20-40) | Küçük görünür (%3-10) |
| Yanma kaybı | Görünmez (%0 enerji kaybı) | En büyük kayıp (%20-30) |
| Isı transferi | Kayıp yok gibi görünür | Önemli kayıp (%5-15) |
| Pratik değer | Miktarsal denge | Kalitesel denge + iyileştirme hedefleri |

## 6. Fabrika Alt Sistemlerinin Exergy Analizi

### 6.1 Buhar Sistemi

```
Exergy verimi (buhar üretimi):
η_ex,buhar = (ṁ_buhar × ex_buhar - ṁ_besleme × ex_besleme) / (ṁ_yakıt × ex_yakıt)

Tipik değerler: %25-45

Ana kayıp kaynakları:
1. Yanma tersinmezliği: %25-30
2. Isı transferi (alev → su/buhar): %15-25
3. Baca gazı kaybı: %5-15
4. Dağıtım kayıpları: %3-8
```

### 6.2 Basınçlı Hava Sistemi

```
Exergy verimi (basınçlı hava üretimi):
η_ex,hava = ṁ_hava × ex_hava / Ẇ_kompresör

Tipik değerler: %10-25

Ana kayıp kaynakları:
1. Sıkıştırma tersinmezliği: %30-45
2. Atık ısı (soğutucu): %40-55
3. Kaçaklar: %15-30
4. Basınç düşüşleri: %5-10
```

### 6.3 Soğutma Sistemi

```
Exergy verimi (soğutma üretimi):
η_ex,soğutma = Q̇_soğutma × |1 - T₀/T_soğutma| / Ẇ_kompresör

Tipik değerler: %15-35

Ana kayıp kaynakları:
1. Sıkıştırma tersinmezliği: %25-40
2. Kısma (genleşme vanası): %15-25
3. Isı transferi (evaporatör/kondenser): %10-20
4. Soğutucu akışkan kayıpları: %1-5
```

## 7. Hesaplama Örneği: Fabrika Exergy Analizi

### 7.1 Senaryo

Orta ölçekli tekstil fabrikası:
- Doğalgaz tüketimi: 500 Nm³/h (LHV = 34.5 MJ/Nm³)
- Elektrik tüketimi: 800 kW
- Buhar üretimi: 6 ton/h (10 bar, doymuş)
- Basınçlı hava: 15 m³/min (7 bar)
- Soğutma: 200 kW (7°C chilled water)
- Çalışma: 6,000 saat/yıl

### 7.2 Exergy Giriş Hesabı

```
1. Yakıt exergisi:
   Ex_yakıt = 500/3600 × 34.5 × 10³ × 1.04 = 4,983 kW
   (φ = 1.04 doğalgaz için)

2. Elektrik exergisi:
   Ex_elektrik = 800 kW (elektrik saf exerjidir)

3. Toplam exergy girişi:
   Ex_giriş = 4,983 + 800 = 5,783 kW
```

### 7.3 Exergy Çıkış Hesabı

```
1. Buhar exergisi (10 bar doymuş, ex = 858 kJ/kg, besleme suyu 80°C ex = 28.8 kJ/kg):
   Ex_buhar = (6,000/3,600) × (858 - 28.8) = 1,382 kW

2. Basınçlı hava exergisi (7 bar, 25°C):
   Ex_hava = ṁ × R × T₀ × ln(P/P₀) = (15/60 × 1.225) × 0.287 × 298.15 × ln(8/1.013)
   Ex_hava ≈ 48 kW

3. Soğutma exergisi (7°C = 280.15 K):
   Ex_soğutma = 200 × |1 - 298.15/280.15| = 200 × 0.064 = 12.8 kW

4. Toplam faydalı exergy çıkışı:
   Ex_ürün = 1,382 + 48 + 12.8 = 1,443 kW
```

### 7.4 Fabrika Exergy Verimi

```
η_ex,fabrika = Ex_ürün / Ex_giriş = 1,443 / 5,783 = %24.9

Karşılaştırma: Enerji verimi ≈ %65-70 olacaktır.
Exergy analizi, gerçek termodinamik performansın çok daha düşük olduğunu gösterir.
```

### 7.5 Exergy Kayıp Dağılımı

| Kayıp Kalemi | Exergy [kW] | Pay [%] |
|---|---|---|
| Faydalı çıkış (buhar + hava + soğutma) | 1,443 | 24.9 |
| Yanma tersinmezliği | 1,370 | 23.7 |
| Isı transferi tersinmezliği (kazan) | 1,050 | 18.2 |
| Baca gazı exergisi | 320 | 5.5 |
| Kompresör tersinmezliği | 215 | 3.7 |
| Kompresör atık ısısı | 480 | 8.3 |
| Chiller tersinmezliği | 250 | 4.3 |
| Buhar dağıtım kayıpları | 310 | 5.4 |
| Basınçlı hava kaçakları | 75 | 1.3 |
| Diğer kayıplar | 270 | 4.7 |
| **TOPLAM** | **5,783** | **100.0** |

## 8. İyileştirme Potansiyelinin Belirlenmesi

### 8.1 Kaçınılabilir vs. Kaçınılamaz Exergy Yıkımı

| Kayıp Türü | Kaçınılamaz | Kaçınılabilir | İyileştirme Yöntemi |
|---|---|---|---|
| Yanma tersinmezliği | %20-25 | %3-8 | Hava ön ısıtma, oksijen zenginleştirme |
| Isı transferi | %8-12 | %5-10 | Daha büyük eşanjörler, pinch tasarım |
| Baca gazı kaybı | %2-3 | %3-10 | Economizer, yoğuşmalı geri kazanım |
| Kompresör ısısı | %5-8 | %30-50 | Isı geri kazanım (bina ısıtma, su ısıtma) |
| Kaçaklar | %0 | %100 | Kaçak tespiti ve onarımı |

### 8.2 Önceliklendirme Matrisi

```
Yüksek öncelik (kolay + yüksek tasarruf):
1. Basınçlı hava kaçak onarımı
2. Buhar kapanı bakımı
3. İzolasyon iyileştirme

Orta öncelik (orta yatırım + iyi tasarruf):
4. Kompresör atık ısı geri kazanımı
5. Economizer eklenmesi
6. VSD retrofit (kompresör/pompa)

Stratejik (yüksek yatırım + uzun vadeli):
7. Pinch analizi tabanlı ısı entegrasyonu
8. Kojenerasyon
9. Proses değişikliği
```

## 9. Exergy Analizi Uygulama Adımları

### 9.1 Veri Toplama

1. Tüm enerji giriş noktalarında debi ve kalite ölçümü
2. Tüm ürün çıkışlarında aynı ölçümler
3. Atık akışlarda sıcaklık, basınç, debi ölçümleri
4. Ortam koşulları (T₀, P₀, nem)

### 9.2 Analiz Süreci

1. Sistem sınırlarını tanımla (bkz. `system_boundaries.md`)
2. Kütle ve enerji dengesini kur
3. Her akış için exergy değerlerini hesapla
4. Alt sistem bazında exergy verimlerini belirle
5. Exergy yıkım dağılımını çıkar
6. Grassmann diyagramını çiz
7. İyileştirme fırsatlarını önceliklendir

## İlgili Dosyalar

- [Sistem Sınırları](system_boundaries.md) — Ölçüm noktaları ve kontrol hacimleri
- [Exergy Akış Analizi](exergy_flow_analysis.md) — Detaylı exergy akış metodolojisi
- [KPI Tanımları](kpi_definitions.md) — Exergy verimlilik göstergeleri
- [Kazan Exergy Formülleri](../boiler/formulas.md) — Kazan exergy hesaplamaları
- [Kompresör Exergy](../compressor/formulas.md) — Kompresör exergy hesaplamaları
- [Chiller Exergy](../chiller/formulas.md) — Soğutma sistemi exergy hesaplamaları
- [Fabrika Benchmarkları](factory_benchmarks.md) — Sektörel exergy verimlilik verileri

## Referanslar

- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 4th Edition, 2016
- Szargut, J., Morris, D.R., Steward, F.R., "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes," Hemisphere Publishing, 1988
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," Elsevier, 3rd Edition, 2021
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing, 1995
- Rosen, M.A. & Dincer, I. (2003), "Exergy-cost-energy-mass analysis of thermal systems and processes," Energy Conversion and Management, 44(10), 1633-1651
- Sciubba, E. & Wall, G. (2007), "A brief commented history of exergy from the beginnings to 2004," Int. J. of Thermodynamics, 10(1), 1-26
- Tsatsaronis, G. (2007), "Definitions and nomenclature in exergy analysis and exergoeconomics," Energy, 32(4), 249-253
