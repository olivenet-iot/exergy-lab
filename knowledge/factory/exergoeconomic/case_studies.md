---
title: "Exergoekonomik Vaka Çalışmaları (Exergoeconomic Case Studies)"
category: factory
equipment_type: factory
keywords: [vaka çalışması, gaz türbini, kombine çevrim, jeotermal, çimento, soğutma, kağıt fabrikası, CHP]
related_files:
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/exergoeconomic/advanced_exergoeconomic.md
  - factory/exergoeconomic/optimization.md
  - factory/exergoeconomic/worked_examples/cogeneration.md
  - factory/exergoeconomic/worked_examples/industrial_plant.md
  - factory/case_studies.md
use_when:
  - "Akademik vaka çalışması referansı gerektiğinde"
  - "Exergoekonomik analiz sonuçlarının gerçek örneklerle desteklenmesi istendiğinde"
  - "Farklı sektörlerde tipik f_k ve r_k değerleri sorulduğunda"
  - "Karşılaştırmalı sektörel analiz yapılacakken"
priority: low
last_updated: 2026-02-01
---
# Exergoekonomik Vaka Çalışmaları (Case Studies)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Bu dosyada, akademik literatürdeki önemli exergoekonomik analiz vaka çalışmalarından 6 tanesi özetlenmektedir. Her vaka, farklı bir sistem/sektörü temsil eder ve tipik sonuçlar, f_k/r_k değerleri ve ders çıkarımları sunulur.

```
Vaka Çalışması Listesi:

No | Sistem                    | Sektör     | Yöntem                | Kaynak              |
---|---------------------------|------------|-----------------------|---------------------|
1  | Gaz türbini CHP          | Enerji     | SPECO + İleri         | Tsatsaronis (2010)  |
2  | Kombine çevrim santrali  | Enerji     | SPECO                 | Bejan (1996)        |
3  | Jeotermal santral         | Jeotermal  | SPECO                 | Yıldırım (2006)     |
4  | Çimento fabrikası         | Çimento    | SPECO + duyarlılık    | Utlu (2014)         |
5  | Endüstriyel soğutma       | Gıda       | SPECO + İleri         | Morosuk (2009)      |
6  | Kağıt fabrikası CHP       | Kağıt      | SPECO                 | Tsatsaronis (2008)  |
```

## 2. Vaka 1: Gaz Türbini CHP Sistemi

### 2.1 Sistem Açıklaması

```
Sistem: 30 MW gaz türbini + HRSG (ısı geri kazanım buhar jeneratörü)
Bileşenler: Hava kompresörü, yanma odası, gaz türbini, HRSG (3 bölüm)
Yakıt: Doğalgaz
Ürünler: Elektrik (30 MW) + Buhar (15 t/h, 20 bar)
Yer: Orta Avrupa referans
```

### 2.2 Sonuçlar

```
Exergoekonomik Değerlendirme:

Bileşen        | Ė_D [kW] | c_F [€/GJ] | Ċ_D [€/sa] | f_k   | r_k   |
---------------|----------|-----------|-----------|-------|-------|
Hava kompresörü| 2,450    | 18.2      | 160.5     | 0.52  | 0.15  |
Yanma odası    | 18,200   | 12.8      | 839.1     | 0.04  | 0.12  |
Gaz türbini    | 510      | 17.1      | 31.4      | 0.89  | 0.03  |
HRSG-SH        | 1,850    | 17.1      | 113.8     | 0.12  | 1.85  |
HRSG-EVAP      | 3,200    | 17.1      | 196.9     | 0.08  | 2.42  |
HRSG-ECO       | 850      | 17.1      | 52.3      | 0.22  | 0.95  |

Ürün maliyetleri:
  c_elektrik = 52.3 €/MWh
  c_buhar = 41.8 €/GJ (exergy bazlı)
```

### 2.3 Ders Çıkarımları

```
Temel Bulgular:
1. Yanma odası en büyük Ċ_D kaynağı (%58) ama f_k=0.04 → çoğu kaçınılamaz
2. HRSG bölümleri yüksek r_k → büyük iyileştirme potansiyeli
3. İleri analiz: CC'nin %75'i kaçınılamaz, HRSG'nin %55'i kaçınılabilir
4. Optimizasyon önceliği: HRSG > CC > AC (ileri analize göre)
5. Geleneksel analiz CC'yi #1 yapar, ileri analiz HRSG'yi #1 yapar
```

## 3. Vaka 2: Kombine Çevrim Santrali

### 3.1 Sistem Açıklaması

```
Sistem: 2×GT + 2×HRSG + 1×Buhar Türbini (500 MW sınıfı)
Konfigürasyon: 2-on-1 kombine çevrim
Bileşenler: 11 ana bileşen
Yakıt: Doğalgaz
Net güç: ~490 MW
Referans: Bejan, Tsatsaronis, Moran (1996) — "Thermal Design and Optimization"
```

### 3.2 Sonuçlar

```
Özet Exergoekonomik Tablo:

Bileşen grubu   | Ė_D [MW] | Ċ_D [€/sa] | Ż [€/sa] | f_k   | r_k   |
----------------|----------|-----------|---------|-------|-------|
GT alt sistemi  | 125.4    | 4,890     | 2,150   | 0.31  | —     |
  - Yanma odaları| 95.2    | 3,480     | 85      | 0.02  | 0.10  |
  - Kompresörler | 18.5    | 745       | 680     | 0.48  | 0.14  |
  - Gaz türbinleri| 11.7   | 485       | 1,385   | 0.74  | 0.04  |
HRSG'ler        | 42.8     | 1,820     | 520     | 0.22  | 1.65  |
Buhar türbini   | 8.5      | 385       | 890     | 0.70  | 0.06  |
Kondenser       | 15.2     | 650       | 180     | 0.22  | —     |
Pompalar        | 0.8      | 42        | 35      | 0.45  | 0.18  |

Sistem:
  Enerji verimi: η_I = 57.2%
  Exergy verimi: ε = 54.8%
  c_elektrik = 48.5 €/MWh
```

### 3.3 Ders Çıkarımları

```
Temel Bulgular:
1. Yanma odaları Ė_D'nin %50'si ama f_k=0.02 → mühendislik limiti
2. HRSG'ler en kritik iyileştirme bölgesi (r_k=1.65, f_k=0.22)
3. Buhar türbini f_k=0.70 → pahalı ama verimli, doğru yatırım
4. Kombine çevrim, basit çevrimi c_elektrik bazında %35 iyileştiriyor
5. Optimal basınç oranı: exergoekonomik analiz ile belirlenmiş
```

## 4. Vaka 3: Jeotermal Santral

### 3.1 Sistem Açıklaması

```
Sistem: Binary cycle jeotermal santral (ORC)
Bileşenler: Kuyu pompası, preheater, evaporatör, türbin, kondenser, feed pump
Jeotermal kaynak: 165°C, 100 kg/s
Çalışma akışkanı: R-245fa (veya izobütan)
Net güç: ~5.2 MW
Yer: Türkiye (Denizli/Aydın bölgesi referans)
```

### 3.2 Sonuçlar

```
Exergoekonomik Değerlendirme:

Bileşen        | Ė_D [kW] | c_F [€/GJ] | Ċ_D [€/sa] | f_k   | r_k   |
---------------|----------|-----------|-----------|-------|-------|
Preheater      | 1,850    | 3.2       | 21.3      | 0.38  | 1.42  |
Evaporatör     | 2,400    | 3.2       | 27.6      | 0.32  | 1.88  |
Türbin         | 420      | 8.5       | 12.9      | 0.78  | 0.08  |
Kondenser      | 980      | 8.5       | 30.0      | 0.15  | —     |
Feed pump      | 35       | 12.1      | 1.5       | 0.42  | 0.21  |
Kuyu pompası   | 280      | 12.1      | 12.2      | 0.25  | 0.35  |

c_jeotermal_kaynak = 3.2 €/GJ (düşük — "bedava" kaynak, kuyu yatırımı maliyeti)
c_elektrik = 78.5 €/MWh (jeotermal, küçük ölçek)
```

### 3.3 Ders Çıkarımları

```
Temel Bulgular:
1. Jeotermal c_F çok düşük → Ċ_D mutlak değeri düşük
2. Evaporatör en büyük Ė_D (%35) ve yüksek r_k → öncelik #1
3. Kondenser f_k=0.15, Ċ_D=30 €/sa → dissipative ama önemli kayıp
4. Türbin f_k=0.78 → yüksek yatırım yapılmış, verimli çalışıyor
5. Çalışma akışkanı seçimi c_P'yi %15-25 değiştirebilir
6. Türkiye jeotermal kaynakları exergoekonomik açıdan avantajlı
   (düşük c_F, yüksek kapasite faktörü >90%)
```

## 5. Vaka 4: Çimento Fabrikası

### 5.1 Sistem Açıklaması

```
Sistem: Çimento üretim hattı (klinker fırını + atık ısı geri kazanım)
Bileşenler: Preheater (5 kademeli), kalsiner, döner fırın, klinker soğutucu,
            çimento değirmeni, WHR (atık ısı geri kazanım) santrali
Kapasite: 5,000 ton/gün klinker
Yakıt: Kömür + alternatif yakıt (%15)
Yer: Türkiye referans (güneydoğu)
```

### 5.2 Sonuçlar

```
Exergoekonomik Değerlendirme (ana bileşenler):

Bileşen          | Ė_D [kW] | c_F [€/GJ] | Ċ_D [€/sa] | f_k   | r_k   |
-----------------|----------|-----------|-----------|-------|-------|
Preheater        | 12,500   | 5.8       | 261.0     | 0.08  | 0.82  |
Kalsiner         | 28,400   | 5.8       | 593.1     | 0.03  | 0.45  |
Döner fırın      | 35,200   | 5.8       | 735.2     | 0.02  | 0.38  |
Klinker soğutucu | 8,800    | 5.8       | 183.7     | 0.12  | 1.55  |
Çimento değirmeni| 4,500    | 18.5      | 299.7     | 0.35  | 0.62  |
WHR santrali     | 3,200    | 5.8       | 66.8      | 0.45  | 0.85  |

c_klinker = 14.2 €/GJ (exergy bazlı)
c_çimento = 18.5 €/GJ (öğütme dahil)
```

### 5.3 Ders Çıkarımları

```
Temel Bulgular:
1. Döner fırın + kalsiner → toplam Ė_D'nin %72'si
2. f_k < 0.05: Yanma/kalsinasyon prosesleri termodinamik limitlerde
3. Klinker soğutucu r_k=1.55 → en büyük iyileştirme potansiyeli
   → Soğutucu verimliliği artışı ve atık ısı kalitesi yükseltme
4. WHR santrali f_k=0.45 → dengeli yatırım/performans
5. Duyarlılık analizi: Kömür fiyatı %30 değiştiğinde c_klinker %18 değişiyor
6. Alternatif yakıt oranı %15→%30 artışı: c_klinker %8 düşüyor
7. Çimento sektörü exergoekonomik açıdan enerji-yoğun:
   Spesifik exergy tüketimi: 3.5-4.5 GJ/ton klinker
```

## 6. Vaka 5: Endüstriyel Soğutma Sistemi

### 6.1 Sistem Açıklaması

```
Sistem: Çift kademeli buhar sıkıştırmalı soğutma çevrimi
Bileşenler: 2 kompresör, 2 evaporatör, kondenser, genleşme vanası,
            flash tank (ara soğutucu)
Soğutucu akışkan: R-134a
Soğutma kapasitesi: 500 kW (-20°C evaporatör)
Yer: Gıda soğuk hava deposu referans
```

### 6.2 Sonuçlar

```
Exergoekonomik Değerlendirme:

Bileşen             | Ė_D [kW] | c_F [€/GJ]| Ċ_D [€/sa] | f_k   | r_k   |
---------------------|----------|----------|-----------|-------|-------|
LP kompresör         | 18.5     | 27.8     | 1.85      | 0.48  | 0.22  |
HP kompresör         | 12.8     | 27.8     | 1.28      | 0.52  | 0.18  |
Kondenser            | 22.4     | 35.2     | 2.84      | 0.18  | —     |
Genleşme vanası (LP) | 8.5      | 35.2     | 1.08      | 0.00  | —     |
Genleşme vanası (HP) | 5.2      | 35.2     | 0.66      | 0.00  | —     |
Flash tank           | 3.8      | 35.2     | 0.48      | 0.15  | 0.45  |
Evaporatör           | 28.5     | 35.2     | 3.61      | 0.22  | 2.85  |

c_soğutma = 95.2 €/GJ (exergy bazlı, düşük sıcaklık nedeniyle yüksek)
COP_exergy = 0.28
```

### 6.3 Ders Çıkarımları

```
Temel Bulgular:
1. Evaporatör en büyük Ė_D + en yüksek r_k → #1 öncelik
2. Genleşme vanaları f_k=0.00 → tamamen termodinamik kayıp
   → Ejektör veya genleşme türbini ile değiştirilebilir
3. Kompresörler f_k≈0.50 → dengeli, iyi yatırım yapılmış
4. İleri analiz (AV-EN): Evaporatör kaybının %60'ı kaçınılabilir
5. Akışkan değişimi (R-134a → R-1234yf): ε %3-5 artış, c_soğutma %4 düşüş
6. Düşük sıcaklık soğutma exergy açısından çok pahalı:
   c_soğutma_(-20°C) = 95 €/GJ vs c_soğutma_(+7°C) = 35 €/GJ
   → Sıcaklık yükseldikçe exergy maliyeti düşer
```

## 7. Vaka 6: Kağıt Fabrikası CHP

### 7.1 Sistem Açıklaması

```
Sistem: Kağıt fabrikası CHP (kazan + karşı basınçlı buhar türbini)
Bileşenler: Doğalgaz kazanı, buhar türbini (karşı basınçlı),
            deaeratör, kondansat sistemi, buhar dağıtım
Kapasite: 25 t/h buhar (40 bar) → 18 t/h proses buharı (6 bar) + 4 MW elektrik
Yer: Türkiye (Marmara bölgesi kağıt fabrikası referans)
```

### 7.2 Sonuçlar

```
Exergoekonomik Değerlendirme:

Bileşen           | Ė_D [kW] | c_F [€/GJ] | Ċ_D [€/sa] | f_k   | r_k   |
-------------------|----------|-----------|-----------|-------|-------|
Kazan              | 22,500   | 11.2      | 907.2     | 0.02  | 3.85  |
Buhar türbini      | 850      | 28.5      | 87.2      | 0.62  | 0.12  |
Deaeratör          | 320      | 28.5      | 32.8      | 0.08  | 0.92  |
Kondansat sistemi  | 180      | 28.5      | 18.5      | 0.25  | 0.55  |
Buhar dağıtım     | 450      | 28.5      | 46.2      | 0.05  | 0.38  |

Ürün maliyetleri:
  c_elektrik = 0.058 €/kWh (CHP, karşı basınçlı türbinden)
  c_buhar_6bar = 35.2 €/GJ (exergy bazlı)

Not: Karşı basınçlı türbin elektrik maliyeti düşük çünkü:
→ Buhar zaten proses için üretiliyor
→ Elektrik "yan ürün" olarak neredeyse bedava
→ Bu, CHP'nin exergoekonomik avantajıdır
```

### 7.3 Ders Çıkarımları

```
Temel Bulgular:
1. Kazan yine baskın Ė_D kaynağı (%93) — sektörden bağımsız bulgu
2. CHP elektrik maliyeti (0.058 €/kWh) < şebeke (0.10 €/kWh) → CHP avantajlı
3. Deaeratör f_k=0.08 → flash buhar kaybı önemli, iyileştirilebilir
4. Buhar dağıtım kayıpları (yalıtım, kaçak, buhar kapanı) f_k=0.05
   → Düşük maliyetli bakım ile tasarruf
5. Karşı basınçlı türbin f_k=0.62 → optimal bölgede
6. Kağıt sektörü buhar tüketimi yoğun → CHP exergoekonomik açıdan ideal
7. Kondansat geri dönüş oranı %80→%95 artışı → c_buhar %8 düşüş
```

## 8. Karşılaştırma Özet Tablosu

```
6 Vaka Çalışması Karşılaştırması:

Vaka              | ε_sys | c_ürün      | En büyük  | En büyük | Ana        |
                  | [%]   | [€/GJ]     | Ė_D payı  | f_k<0.10 | iyileştirme|
------------------|-------|-------------|-----------|----------|------------|
1. GT CHP         | 46    | 52 (elek.) | CC (%58)  | CC       | HRSG       |
2. Kombine çevrim | 55    | 48 (elek.) | CC (%50)  | CC       | HRSG       |
3. Jeotermal      | 32    | 78 (elek.) | Evap.(%35)| Kond.    | Evaporatör |
4. Çimento        | 25    | 14 (klin.) | Fırın(%40)| Fırın,kal| Soğutucu  |
5. Soğutma        | 28    | 95 (soğut.)| Evap.(%30)| Vanalar  | Evaporatör |
6. Kağıt CHP      | 38    | 58 (elek.) | Kazan(%93)| Kazan    | Dağıtım   |

Ortak Bulgular:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Yanma/reaksiyon bileşenleri her zaman en büyük Ė_D → ama f_k çok düşük
2. Isı değiştiriciler genellikle en yüksek r_k → gerçek iyileştirme fırsatı
3. Türbinler/kompresörler f_k = 0.40-0.80 → genellikle dengeli
4. Genleşme vanaları f_k = 0 → tamamen termodinamik kayıp
5. İleri analiz (AV/UN) geleneksel sıralamayı değiştirebilir
6. Sektörden bağımsız: Yanma f_k << 0.10, ısı transferi r_k >> 1.0
```

## 9. ExergyLab İçin Çıkarımlar

```
ExergyLab Platformu Tasarım Notları:

Bu vaka çalışmalarından AI yorumlama sistemi için:

1. Kazan analizinde:
   → f_k < 0.05 beklenmeli, bu normal — yanma limiti
   → r_k > 2.0 beklenmeli → büyük iyileştirme potansiyeli var demek değil
   → Gerçek potansiyel: ekonomizer, hava ön ısıtma, CHP

2. Chiller/soğutma analizinde:
   → Düşük sıcaklık = yüksek c_P (Carnot etkisi)
   → Evaporatör genellikle #1 iyileştirme hedefi
   → Set point artışı en kolay tasarruf

3. Kompresör/pompa analizinde:
   → f_k = 0.20-0.50 tipik → orta bölge
   → Atık ısı geri kazanımı çapraz ekipman fırsatı

4. Çapraz ekipman analizinde:
   → Yanma → ısı transferi zincirinde her adımda exergy kaybı
   → Doğrudan kullanım (direct use) her zaman daha iyi
   → CHP = exergoekonomik açıdan en etkili entegrasyon
```

## İlgili Dosyalar

- [Değerlendirme Kriterleri](evaluation_criteria.md) — f_k, r_k, Ċ_D tanımları
- [İleri Exergoekonomik](advanced_exergoeconomic.md) — AV/UN, EN/EX analiz
- [Optimizasyon](optimization.md) — Maliyet minimizasyonu yöntemleri
- [CHP Çözümlü Örnek](worked_examples/cogeneration.md) — Detaylı CHP analizi
- [Endüstriyel Tesis Örneği](worked_examples/industrial_plant.md) — ExergyLab örneği
- [Fabrika Vaka Çalışmaları](../case_studies.md) — Genel fabrika vakaları

## Referanslar

1. Tsatsaronis, G., Morosuk, T. (2010). "Advanced exergetic analysis..." *Energy*, 35(2), 820-829.
2. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
3. Yıldırım, D., Özgener, L. (2012). "Thermodynamics and thermoeconomic analysis of geothermal power plants." *Renewable and Sustainable Energy Reviews*, 16(8), 6438-6454.
4. Utlu, Z., Hepbasli, A. (2014). "Thermoeconomic analysis of a cement plant." *Applied Thermal Engineering*, 66(1-2), 435-444.
5. Morosuk, T., Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines..." *Energy*, 34(12), 2248-2258.
6. Tsatsaronis, G., Park, M.H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
