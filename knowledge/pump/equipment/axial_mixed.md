---
title: "Eksenel ve Karışık Akışlı Pompalar — Axial and Mixed Flow Pumps"
category: equipment
equipment_type: pump
subtype: "Eksenel / Karışık Akışlı"
keywords: [eksenel pompa, karışık akışlı, yüksek debi]
related_files: [pump/benchmarks.md, pump/formulas.md, pump/equipment/centrifugal.md]
use_when: ["Eksenel/karışık akışlı pompa analizi yapılırken", "Yüksek debili uygulama değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Eksenel ve Karışık Akışlı Pompalar — Axial and Mixed Flow Pumps

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Kinetik (dinamik), eksenel (axial) ve karışık akışlı (mixed flow)
- Eksenel pompa: Propeller tipi, yüksek debi — düşük head
- Karışık akışlı pompa: Santrifüj ve eksenel arası hibrit tasarım
- Kapasite aralığı: 100 - 100,000+ m³/h (eksenel), 50 - 20,000 m³/h (karışık akışlı)
- Head aralığı: 1 - 15 m (eksenel), 5 - 50 m (karışık akışlı)
- Yaygın markalar: Flowserve (LNN, MNX), Sulzer (ABS), KSB (Amacan, CPKN), Xylem/Flygt (PS, CP), Grundfos (KPL), Bedford Pumps

## Çalışma Prensibi

### Eksenel Akışlı Pompa (Axial Flow Pump)
Propeller şeklindeki çark (impeller) sıvıyı döndürmek yerine eksenel yönde (şaft ekseni boyunca) iter. Çalışma prensibi uçak pervanesi veya gemi pervanesine benzer. Sıvı impellere paralel girer ve paralel çıkar — akış yönü 90° döndürülmez.

### Karışık Akışlı Pompa (Mixed Flow Pump)
İmpeller tasarımı santrifüj (radyal) ve eksenel akışın birleşimidir. Sıvı çark içinde hem radyal hem eksenel yönde hareket eder. İmpeller çıkış açısı tipik olarak 45-75° (eksen ile). Bu tasarım santrifüj pompanın head kapasitesi ile eksenel pompanın debi kapasitesini birleştirir.

### Temel Bileşenler
- **Propeller / İmpeller:** Eksenel pompada 3-6 kanatlı propeller; karışık akışlıda yarı açık (semi-open) veya kapalı çark
- **Kılavuz kanatçıklar (Guide Vanes):** İmpeller çıkışında rotasyonu basınca dönüştüren sabit kanatlar
- **Gövde (Casing):** Eksenel pompada boru tipi gövde (elbow veya düz); karışık akışlıda volüt veya difüzör gövde
- **Şaft ve yataklar:** Genellikle dikey montaj, büyük eksenel yükler nedeniyle güçlü thrust bearing
- **Emme çanı (Suction Bell):** Giriş akışını düzenleyen çan şeklinde parça

## Spesifik Hız (Ns) İlişkisi

| Pompa Tipi | Ns Aralığı (US, rpm·gpm^0.5/ft^0.75) | Ns Aralığı (SI) | Impeller Geometrisi |
|-----------|---------------------------------------|-----------------|-------------------|
| Radyal (santrifüj) | 500-4,000 | 10-80 | Kapalı çark, geniş çap, dar kanal |
| Karışık akışlı (mixed flow) | 4,000-8,000 | 80-160 | Yarı açık çark, orta çap |
| Eksenel (axial flow) | 8,000-20,000 | 160-400 | Propeller, küçük çap, geniş kanal |

Spesifik hız arttıkça: impeller çapı küçülür, kanal genişler, head düşer, debi artar.

## Pompa Eğrisi Karakteristikleri

### Eksenel Pompa — Dikkat: Ters Güç Eğrisi
- H-Q eğrisi çok dik (steep) — küçük debi değişiminde head büyük değişir
- **P-Q eğrisi ters davranır:** Debi azaldıkça güç ARTAR (santrifüjün tam tersi!)
- Sıfır debide (kapalı vana) güç maksimuma ulaşır — BEP gücünün 2-3 katı olabilir
- Bu nedenle eksenel pompalar asla kapalı vanaya karşı çalıştırılmamalı
- Motor boyutlandırma minimum debi (veya sıfır debi) gücüne göre yapılmalı

### Karışık Akışlı Pompa
- H-Q eğrisi santrifüj pompaya göre daha dik ama eksenel kadar aşırı değil
- P-Q eğrisi düz veya hafif artan (düşük debide)
- Kararlılık açısından eksenel pompadan daha güvenli çalışma

## Enerji Dağılımı (Tipik — Büyük Eksenel Pompa)
- Faydalı hidrolik iş: ~75-88%
- Hidrolik kayıplar (çark, kılavuz kanat, giriş/çıkış): ~8-15%
- Mekanik kayıplar (yatak, conta): ~2-4%
- Motor kayıpları: ~3-8%

## Verimlilik Benchmarkları — Eksenel Pompa

| Pompa Boyutu | Düşük | Ortalama | İyi | Best-in-class |
|-------------|-------|----------|-----|---------------|
| Küçük (<50 kW) | <%72 | %72-78 | %78-84 | >%84 |
| Orta (50-250 kW) | <%78 | %78-84 | %84-88 | >%88 |
| Büyük (250-1000 kW) | <%82 | %82-87 | %87-91 | >%91 |
| Çok büyük (>1000 kW) | <%84 | %84-88 | %88-92 | >%92 |

## Verimlilik Benchmarkları — Karışık Akışlı Pompa

| Pompa Boyutu | Düşük | Ortalama | İyi | Best-in-class |
|-------------|-------|----------|-----|---------------|
| Küçük (<50 kW) | <%70 | %70-77 | %77-83 | >%83 |
| Orta (50-250 kW) | <%76 | %76-82 | %82-87 | >%87 |
| Büyük (>250 kW) | <%80 | %80-85 | %85-90 | >%90 |

## Kısmi Yük Davranışı (Eksenel Pompa)

| Debi (% BEP) | Head (% BEP) | Güç (% BEP) | Pompa Verimi |
|---------------|--------------|-------------|-------------|
| 100% | 100% | 100% | Maksimum (BEP) |
| 80% | 140% | 115% | ~90% BEP |
| 60% | 170% | 135% | ~70% BEP |
| 40% | 200%+ | 170%+ | ~45% BEP |
| 0% (kapalı) | 250-300% | 200-300% | 0% — motor aşırı yüklenir! |

Not: Bu davranış eksenel pompayı diğer tüm pompalardan ayırır — düşük debide güç artışı ciddi risk oluşturur.

## Ayarlanabilir Kanatçıklar (Adjustable Blade Pitch)
- Büyük eksenel pompalarda impeller kanat açısı ayarlanabilir
- Sabit hız + değişken kanat açısı = verimli debi kontrolü
- Kanat açısı değiştirilerek BEP farklı debi noktalarına kaydırılabilir
- VSD ile kombinasyon en yüksek kısmi yük verimini sağlar

## Kavitasyon Riski
- Yüksek spesifik hızlı pompalar kavitasyona daha hassastır
- Eksenel pompalarda NPSH required değeri nispeten yüksek olabilir
- Düşük emme yüksekliği (suction head) uygulamalarında dikkat gerekli
- Kavitasyon impeller kanat uçlarında başlar → erozyon ve performans düşüşü

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 10-5000+ | Güç analizörü |
| Emme seviyesi / basıncı | m veya bar | 0-10 | Seviye / basınç sensörü |
| Basma basıncı / seviyesi | m veya bar | 1-15 (eksenel), 5-50 (karışık) | Basınç sensörü |
| Debi | m³/h | 100-100,000+ | Ultrasonik / elektromanyetik flowmeter |
| Sıvı sıcaklığı | °C | 5-40 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Motor devri | RPM | 200-1000 | Takometre |
| Kanat açısı (adjustable blade) | ° | -5 ile +15 | Kontrol paneli |
| Titreşim | mm/s | <4.5 | Titreşim sensörü |
| Su seviyesi (emme tarafı) | m | 0-10 | Seviye sensörü |
| Çalışma saati | saat/yıl | 2000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. KSB Amacan P 700-420)
- Nominal güç (kW)
- Nominal debi (m³/h veya m³/s)
- Nominal head (m)
- Impeller tipi: Eksenel (propeller) veya karışık akışlı
- Impeller çapı (mm)
- Kanat sayısı
- Kanat açısı ayar aralığı (varsa)
- Nominal devir (RPM)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Sıvı yoğunluğu | 1000 kg/m³ | Su varsayımı |
| Pompa verimi | %82 | Büyük eksenel/karışık pompa ortalaması |
| Motor verimi | %94 | Büyük motor, IE3 |
| Yük oranı | %85 | Genellikle yüksek yükte çalışır |
| Çalışma saati | 5000 saat/yıl | Su iletim / sulama uygulaması |
| cosφ (güç faktörü) | 0.88 | Büyük motor |
| Head | 8 m | Eksenel pompa varsayımı |

## Exergy Verimi Hesabı

```
η_exergy = Ė_hydraulic / Ė_electric
Ė_hydraulic = ρ × g × H × Q / 3600
Ė_electric = P_measured

η_pump = P_hydraulic / P_shaft
η_overall = η_pump × η_motor = P_hydraulic / P_electric
```

Eksenel ve karışık akışlı pompalarda head düşük olduğundan, mutlak enerji tasarrufu potansiyeli genellikle debiye bağlıdır. Yüksek debili uygulamalarda %1'lik verim artışı bile önemli enerji tasarrufu sağlar.

```
Yıllık tasarruf örneği:
- Debi: 10,000 m³/h, Head: 8 m, Verim artışı: %2
- Güç tasarrufu ≈ (1000 × 9.81 × 8 × 10000) / (3600 × 0.82) - (1000 × 9.81 × 8 × 10000) / (3600 × 0.84)
- ≈ 265.8 - 259.5 ≈ 6.3 kW
- Yıllık: 6.3 × 5000 = 31,500 kWh → ~3,150 EUR/yıl (@ 0.10 EUR/kWh)
```

## Tipik Uygulama Alanları

| Uygulama | Pompa Tipi | Tipik Debi (m³/h) | Tipik Head (m) |
|----------|-----------|-------------------|----------------|
| Sulama pompaj istasyonu | Eksenel / karışık | 1,000-50,000 | 2-15 |
| Drenaj ve taşkın kontrolü | Eksenel | 5,000-100,000+ | 1-8 |
| İçme suyu iletimi (ham su) | Karışık akışlı | 500-10,000 | 10-40 |
| Soğutma suyu (enerji santrali) | Eksenel / karışık | 5,000-50,000 | 5-20 |
| Evaporatör sirkülasyonu | Eksenel | 1,000-20,000 | 2-8 |
| Atıksu terfi (lift station) | Karışık akışlı | 500-5,000 | 5-25 |
| Deniz suyu soğutma | Eksenel | 10,000-100,000+ | 3-12 |

## Eksenel vs Karışık vs Santrifüj Karşılaştırma

| Özellik | Eksenel | Karışık Akışlı | Santrifüj (Radyal) |
|---------|---------|---------------|-------------------|
| Ns aralığı (US) | 8,000-20,000 | 4,000-8,000 | 500-4,000 |
| Debi kapasitesi | Çok yüksek | Yüksek | Düşük-orta |
| Head kapasitesi | Çok düşük (1-15 m) | Düşük-orta (5-50 m) | Orta-yüksek (10-500+ m) |
| Eğri dikliği | Çok dik | Dik | Düz-orta |
| Kapalı vana gücü | BEP'in 2-3 katı | BEP'in 1.2-1.5 katı | BEP'in 0.3-0.6 katı |
| Kavitasyon hassasiyeti | Yüksek | Orta | Düşük |
| Tipik verim (büyük) | %85-92 | %82-90 | %80-93 |

## Dikkat Edilecekler

1. **Kapalı vana çalışma yasağı:** Eksenel pompalarda kapalı vanaya karşı çalışma motoru aşırı yükler ve yakabilir — debi kontrolü vana kısma ile yapılmamalı
2. **Motor boyutlandırma:** Eksenel pompalarda motor, minimum debi gücüne göre boyutlandırılmalı (santrifüjün tersi!) — aksi halde aşırı yük koruması devreye girer
3. **Kavitasyon:** Yüksek Ns nedeniyle kavitasyon riski yüksek — yeterli batma derinliği (submergence) sağlanmalı
4. **Kanat açısı ayarı:** Adjustable blade sistemlerde mekanik bağlantıların periyodik kontrolü gerekli
5. **Sediment ve yabancı cisim:** Büyük debili uygulamalarda emme ızgarası temizliği kritik — tıkanma head ve verimliliği düşürür
6. **Girdap oluşumu (Vortex):** Yetersiz batma derinliğinde emme tarafında girdap oluşabilir — hava emmesine ve performans düşüşüne neden olur
7. **Çalıştırma prosedürü:** Eksenel pompalar açık vana ile çalıştırılmalı (santrifüjün tersi) — başlangıç akımını sınırlamak için soft starter veya VSD gerekli

## İlgili Dosyalar
- Santrifüj pompa: `equipment/pump_centrifugal.md`
- Dikey türbin pompa: `equipment/pump_vertical_turbine.md`
- VSD uygulaması: `solutions/pump_vsd.md`
- Benchmark verileri: `benchmarks/pump_benchmarks.md`
- Exergy hesaplamaları: `formulas/pump_exergy.md`

## Referanslar
- Hydraulic Institute Standards (ANSI/HI 2.1-2.2 — Rotodynamic Vertical Pumps)
- Hydraulic Institute Pump Principles — Centrifugal, Mixed and Axial Flow (datatool.pumps.org)
- KSB Amacan / CPKN Axial and Mixed Flow Pump Technical Documentation
- Flowserve LNN Series Axial Flow Pump Engineering Data
- Xylem/Flygt Submersible Propeller Pump Technical Catalog
- Stepanoff, A.J., "Centrifugal and Axial Flow Pumps," Wiley, 2nd Edition
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Gülich, J.F., "Centrifugal Pumps," Springer — Axial and Semi-Axial Pump Chapter
