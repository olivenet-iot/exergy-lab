---
title: "Santrifüj Pompa — Centrifugal Pump"
category: equipment
equipment_type: pump
subtype: "Santrifüj"
keywords: [santrifüj pompa, centrifugal, debi, basınç]
related_files: [pump/benchmarks.md, pump/formulas.md, pump/solutions/vsd.md]
use_when: ["Santrifüj pompa analizi yapılırken", "Pompa eğrisi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Santrifüj Pompa — Centrifugal Pump

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Kinetik (dinamik), radyal akışlı
- Kapasite aralığı: 1 - 10,000+ m³/h
- Basınç aralığı (head): 10 - 500+ m
- En yaygın pompa tipi — endüstriyel pompaların ~%70'ini oluşturur
- Yaygın markalar: Grundfos (CR, NB, NK), KSB (Etanorm, Movitec), Sulzer (CPE, MSD), Flowserve (Durco, Innomag), Xylem (Lowara, Goulds)

## Çalışma Prensibi
Motor tarafından döndürülen çark (impeller) sıvıya kinetik enerji kazandırır. Bu kinetik enerji volüt (spiral kasa) veya difüzörde basınç enerjisine dönüştürülür. Sıvı impeller göbeğinden (eye) girer, çark kanatları arasında radyal yönde hızlandırılır ve volüt çıkışından basınç altında sisteme verilir.

### Temel Bileşenler
- **Impeller (Çark):** Kapalı (closed), yarı açık (semi-open) veya açık (open) tip; malzeme: dökme demir, bronz, paslanmaz çelik
- **Volüt (Spiral Kasa):** Kinetik enerjiyi basınca dönüştüren salyangoz şekilli gövde
- **Difüzör:** Çok kademeli pompalarda kademeler arası yönlendirici kanatçıklar
- **Mil (Shaft):** Motor torku impellere iletir
- **Salmastra / Mekanik Conta (Mechanical Seal):** Mil geçiş noktasında sızdırmazlık
- **Yataklar (Bearings):** Radyal ve eksenel yükleri taşır

### Tek Kademeli vs Çok Kademeli
- **Tek kademeli (Single Stage):** 1 impeller, head 10-150 m, en yaygın tip
- **Çok kademeli (Multi Stage):** 2-20+ impeller seri bağlı, head 150-500+ m, yüksek basınç uygulamaları (besleme suyu, boru hatları)
- Her ek kademe toplam head'e katkı sağlar; debi aynı kalır

## Pompa Eğrileri (Pump Curves)
- **H-Q Eğrisi (Head vs Flow):** Debiye karşı üretilen basınç yüksekliği — debi arttıkça head düşer
- **P-Q Eğrisi (Power vs Flow):** Debiye karşı güç tüketimi — genellikle debi ile artar
- **η-Q Eğrisi (Efficiency vs Flow):** Debiye karşı verim — BEP noktasında maksimum
- Pompa seçimi bu eğrilerin sistem eğrisi ile kesişim noktasına göre yapılır

## Spesifik Hız (Ns) ve Tip Seçimi

| Ns Aralığı (SI) | Ns Aralığı (US, rpm·gpm^0.5/ft^0.75) | Çark Tipi | Head / Debi Oranı |
|------------------|---------------------------------------|-----------|-------------------|
| 10-35 | 500-2,000 | Radyal akışlı (kapalı çark) | Yüksek head, düşük debi |
| 35-80 | 2,000-4,000 | Francis tipi çark | Orta head, orta debi |
| 80-160 | 4,000-8,000 | Karışık akışlı (mixed flow) | Düşük head, yüksek debi |
| >160 | >8,000 | Eksenel akışlı (axial flow) | Çok düşük head, çok yüksek debi |

Maksimum verim genellikle Ns = 2,000-3,000 (US) aralığında elde edilir.

## BEP (Best Efficiency Point)
- Her pompa tek bir BEP noktasına sahiptir — bu noktada hidrolik verim, radyal yükler ve titreşim en uygun düzeydedir
- BEP'ten sapma etkileri:
  - Radyal yatak yükleri artar (özellikle düşük debide)
  - Titreşim ve gürültü artar
  - Kavitasyon riski yükselir
  - Mekanik conta ömrü kısalır
- **Önerilen çalışma aralığı:** BEP'in %80-110'u (Preferred Operating Range)
- **İzin verilen çalışma aralığı:** BEP'in %70-120'si (Allowable Operating Range)

## NPSH (Net Positive Suction Head) Kavramı
- **NPSHa (Available):** Sistemin emme tarafında pompaya sağlanan basınç yüksekliği (buhar basıncı üzeri)
- **NPSHr (Required):** Pompanın kavitasyonsuz çalışması için gerektirdiği minimum basınç (üretici verir)
- **Kural:** NPSHa > NPSHr + güvenlik marjı (min. 0.5-1.0 m)
- Kavitasyon oluşursa: verim düşer, gürültü/titreşim artar, impeller erozyona uğrar

## Enerji Dağılımı (Tipik)
- Faydalı hidrolik iş (useful hydraulic power): ~60-85% (boyuta bağlı)
- Hidrolik kayıplar (sürtünme, resirkülasyon, şok): ~15-25%
- Mekanik kayıplar (yatak, conta, disk sürtünmesi): ~2-5%
- Motor kayıpları: ~5-10%
- Hacimsel kayıplar (wear ring sızıntı, balans sızıntısı): ~1-3%

## Verimlilik Benchmarkları

| Pompa Boyutu | Düşük | Ortalama | İyi | Best-in-class |
|-------------|-------|----------|-----|---------------|
| Küçük (<5 kW) | <%55 | %55-65 | %65-75 | >%75 |
| Orta (5-50 kW) | <%70 | %70-78 | %78-85 | >%85 |
| Büyük (50-250 kW) | <%78 | %78-85 | %85-90 | >%90 |
| Çok büyük (>250 kW) | <%82 | %82-88 | %88-92 | >%92 |

Not: Değerler pompa verimi (wire-to-water değil) olarak verilmiştir. Wire-to-water verim = pompa verimi × motor verimi.

## Kısmi Yük Davranışı (Throttle Valve ile)

| Debi (% BEP) | Head (% BEP) | Güç (% BEP) | Pompa Verimi (% BEP) |
|---------------|--------------|-------------|---------------------|
| 100% | 100% | 100% | 100% |
| 80% | 110% | 90% | ~90% |
| 60% | 115% | 75% | ~80% |
| 40% | 118% | 60% | ~60% |
| 20% | 120% | 45% | ~35% |

Throttle valve ile debi kısma en yaygın fakat en verimsiz kontrol yöntemidir. Vana basınç kaybı tamamen ısıya dönüşür.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 0.5-1000+ | Güç analizörü veya CT + voltaj |
| Emme basıncı | bar | -0.5 ile +5 | Basınç sensörü (emme flanşı) |
| Basma basıncı | bar | 1-50+ | Basınç sensörü (basma flanşı) |
| Debi | m³/h | 1-10,000+ | Ultrasonik / elektromanyetik flowmeter |
| Sıvı sıcaklığı | °C | 5-200 | Termometre / termokupl |

### Opsiyonel (daha detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Motor devri | RPM | 1450-3500 | Takometre |
| Titreşim | mm/s | <4.5 (ISO 10816) | Titreşim sensörü |
| Yatak sıcaklığı | °C | 40-80 | Sıcaklık sensörü |
| Motor akımı | A | Motor etiketine göre | Pens ampermetre |
| Sıvı yoğunluğu | kg/m³ | 800-1200 | Yoğunluk ölçer veya tablo |
| Sıvı viskozitesi | cSt | 0.3-500 | Viskozimetre veya tablo |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç veya tahmin |

### Nameplate Bilgileri
- Marka ve model (örn. Grundfos CR 64-2-1)
- Nominal güç (kW)
- Nominal debi (m³/h veya l/s)
- Nominal head (m) veya basınç (bar)
- Kademe sayısı
- Nominal devir (RPM)
- NPSH required (m)
- İmpeller çapı (mm)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Sıvı yoğunluğu | 1000 kg/m³ | Su varsayımı |
| Sıvı sıcaklığı | 20°C | Ortam sıcaklığı |
| Pompa verimi | %70 | Genel endüstriyel ortalama |
| Motor verimi | %92 | IE3 motor varsayımı |
| Yük oranı | %75 | Endüstriyel ortalama |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| cosφ (güç faktörü) | 0.85 | Tipik motor değeri |
| Emme basıncı | 0 bar(g) | Atmosferik emme |

## Hidrolik Güç Hesabı

```
P_hydraulic = ρ × g × H × Q / 3600
```

Burada:
- P_hydraulic: Hidrolik güç (W)
- ρ: Sıvı yoğunluğu (kg/m³)
- g: Yerçekimi ivmesi (9.81 m/s²)
- H: Toplam manometrik yükseklik / head (m)
- Q: Debi (m³/h)

```
η_pump = P_hydraulic / P_shaft
η_motor = P_shaft / P_electric
η_overall = η_pump × η_motor = P_hydraulic / P_electric
```

## Exergy Verimi Hesabı

```
η_exergy = Ė_hydraulic / Ė_electric
Ė_hydraulic = ΔP × Q  (basınç farkı × hacimsel debi)
Ė_electric = P_electric  (elektrik gücü = saf exergy)
```

Pompalarda exergy verimi ≈ enerji verimi (wire-to-water), çünkü hem elektrik hem hidrolik iş saf exergydir.

## Dikkat Edilecekler

1. **Kavitasyon (Cavitation):** NPSHa < NPSHr durumunda impeller erozyona uğrar, verim düşer — emme koşullarını mutlaka kontrol edin
2. **BEP'ten sapma:** Pompa BEP'in %70'inin altında veya %120'sinin üzerinde çalıştırılmamalı — artan radyal yükler yatak ve conta ömrünü kısaltır
3. **Aşırı boyutlama (Oversizing):** Endüstride en yaygın sorun — pompalar genellikle %20-50 fazla boyutlandırılır, throttling israfına yol açar
4. **Throttling israfı:** Vana ile debi kontrolü enerji israfıdır — VSD veya impeller trimming değerlendirilmeli
5. **Wear ring aşınması:** Zamanla iç sızıntı artar, verim %5-15 düşebilir — periyodik kontrol ve değişim gerekli
6. **Viskozite etkisi:** >100 cSt viskozitede verim belirgin düşer, >500 cSt'de pozitif deplasmanlı pompa tercih edilmeli
7. **Paralel çalışma:** İki pompayı paralel çalıştırmak debiyi 2 katına çıkarmaz — sistem eğrisi ile birlikte değerlendirilmeli

## İlgili Dosyalar
- VSD uygulaması: `solutions/pump_vsd.md`
- İmpeller trimming: `solutions/pump_impeller_trimming.md`
- Benchmark verileri: `benchmarks/pump_benchmarks.md`
- Exergy hesaplamaları: `formulas/pump_exergy.md`
- Pozitif deplasmanlı alternatif: `equipment/pump_positive_displacement.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Hydraulic Institute Standards (ANSI/HI 1.1-1.2, 14.6 — Rotodynamic Pump Efficiency)
- Grundfos Pump Handbook, 3rd Edition
- KSB Centrifugal Pump Lexicon
- Europump Guide to Pump Selection and Energy Assessment
- Gülich, J.F., "Centrifugal Pumps," Springer, 3rd Edition
- Karassik, I.J. et al., "Pump Handbook," McGraw-Hill, 4th Edition
- ISO 9906:2012 — Rotodynamic Pumps — Hydraulic Performance Acceptance Tests
