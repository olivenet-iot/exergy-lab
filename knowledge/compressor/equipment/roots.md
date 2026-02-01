---
title: "Roots Blower (Roots Üfleyici)"
category: equipment
equipment_type: compressor
subtype: "Roots Üfleyici"
keywords: [roots üfleyici, düşük basınç, pnömatik]
related_files: [compressor/benchmarks.md, compressor/formulas.md, compressor/solutions/system_design.md]
use_when: ["Roots üfleyici analizi yapılırken", "Düşük basınç uygulaması değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Roots Blower (Roots Üfleyici)

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Pozitif deplasmanlı, döner loblu
- Basınç aralığı: 0.3 - 1.2 bar (üfleyici olarak), vakum uygulamalarında -0.5 bar'a kadar
- Kapasite aralığı: 2 - 500+ kW
- Debi aralığı: 5 - 15,000+ m³/saat
- Yaygın markalar: Aerzen, Kaeser (Omega), Atlas Copco (ZB), Howden, Gardner Denver (Robuschi), Continental

## Çalışma Prensibi
İki loblu (genellikle 3 loblu veya helisel) rotor, zamanlama dişlileri ile senkronize döner. Rotorlar birbirine ve gövdeye temas etmeden havayı giriş tarafından çıkış tarafına iter. Sıkıştırma kompresör içinde değil, çıkış tarafındaki karşı basınç ile gerçekleşir (izokhorik — sabit hacimli sıkıştırma).

### Temel Özellikler
- **İzokhorik sıkıştırma:** Hava gövde içinde sıkıştırılmaz, çıkışta ani basınç artışı olur
- **Yağsız:** Sıkıştırma odasında yağ yoktur
- **Sürekli debi:** Sabit devir = sabit debi (basınçtan bağımsız)
- **Düşük basınç oranı:** Tipik olarak 1.3-2.2:1

## Roots vs Vidalı Blower Karşılaştırma

| Özellik | Roots Blower | Vidalı Blower | Turbo Blower |
|---------|-------------|---------------|--------------|
| Basınç aralığı | 0.3-1.2 bar | 0.3-2.5 bar | 0.3-1.5 bar |
| İzentropik verim | %50-70 | %70-85 | %75-85 |
| Enerji tüketimi | Baz (yüksek) | %20-30 daha düşük | %25-35 daha düşük |
| Gürültü | 85-100 dB(A) | 70-80 dB(A) | 65-75 dB(A) |
| Bakım | Basit | Orta | Düşük (mag-lev) |
| Yatırım maliyeti | Düşük | Orta | Yüksek |
| Kısmi yük | VSD ile iyi | VSD ile iyi | VSD ile çok iyi |

## Verimlilik

| Parametre | Roots Blower | Not |
|-----------|-------------|-----|
| İzentropik verim | %50-70 | Basınç oranına bağlı |
| Tipik güç tüketimi | 0.02-0.04 kWh/m³ | 0.5 bar'da, ortama bağlı |
| Spesifik güç (0.5 bar) | ~20-35 kW/(m³/min) | Düşük basınçta yüksek özgül güç |

**Verim düşüklüğünün nedeni:** İzokhorik sıkıştırma termodinamik olarak en verimsiz yöntemdir. Hava gövde içinde sıkıştırılmadan çıkışa itildiğinde, çıkıştaki yüksek basınçlı hava geriye doğru genleşir ve enerji kaybına neden olur.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü | kW | 2-500+ | Güç analizörü |
| Çıkış basıncı | bar (gauge) | 0.3-1.2 | Basınç sensörü |
| Hava/gaz debisi | m³/saat | 5-15,000+ | Flowmeter |
| Ortam sıcaklığı | °C | 15-40 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Çıkış sıcaklığı | °C | 50-180 | Termometre |
| Motor devri | RPM | 500-4000 | Kontrol paneli / takometre |
| Titreşim | mm/s | <7.1 (ISO 10816) | Titreşim sensörü |
| Çalışma saati | saat/yıl | 4000-8760 | Sayaç |

### Nameplate Bilgileri
- Marka ve model
- Nominal güç (kW)
- Nominal debi (m³/saat veya m³/min)
- Nominal basınç farkı (mbar veya bar)
- Rotor konfigürasyonu (2 loblu, 3 loblu, helisel)
- Motor devri (RPM)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| İzentropik verim | %60 | Ortalama roots blower |
| Çıkış sıcaklığı | Ortam + 40°C | 0.5 bar basınçta tipik |
| Çalışma saati | 8000 saat/yıl | Sürekli proses uygulamaları |
| Yük oranı | 90% | Genelde sabit yükte çalışır |

## Uygulama Alanları

### Atıksu Arıtma (En Yaygın Uygulama)
- Biyolojik arıtma havuzlarına hava üfleme (havalandırma)
- Tipik basınç: 0.3-0.8 bar (havuz derinliğine bağlı)
- Sürekli çalışma (7/24)
- Enerji tüketiminin %50-70'i blower'lara gider
- **En büyük enerji tasarrufu fırsatı:** Roots'dan turbo veya vidalı blower'a geçiş → %20-35 tasarruf

### Diğer Uygulamalar
- **Pnömatik taşıma:** Toz, granül, tane malzeme taşıma
- **Fluidizasyon:** Çimento fabrikaları, kimya tesisleri
- **Gaz üfleme:** Biyogaz sıkıştırma, yanma havası
- **Vakum:** Ambalajlama, kağıt taşıma, CNC tezgah vakum
- **Akuakültür:** Balık çiftliklerinde havalandırma

## Enerji Tasarrufu Fırsatları

### 1. VSD Retrofit
- Sabit devirli roots blower'a VSD eklenmesi
- Debi kontrolü damper yerine hız kontrolü ile yapılır
- Tipik tasarruf: %15-30 (damper kontrolüne kıyasla)

### 2. Teknoloji Değişikliği
| Mevcut | Yeni Teknoloji | Tipik Tasarruf | Yatırım Geri Dönüşü |
|--------|---------------|---------------|---------------------|
| Roots blower | Vidalı blower | %20-30 | 2-4 yıl |
| Roots blower | Turbo blower (mag-lev) | %25-35 | 3-5 yıl |
| Roots + damper | Roots + VSD | %15-30 | 1-3 yıl |

### 3. Basınç Optimizasyonu
- Atıksu arıtmada: Difüzör bakımı ve basınç düşürme
- Tıkalı difüzörler basınç kaybına neden olur → daha fazla enerji
- Her 0.1 bar basınç düşüşü → ~%8-10 enerji tasarrufu

## Exergy Analizi Notları
- Düşük basınç oranı nedeniyle exergy çıkışı düşüktür
- İzokhorik sıkıştırma yüksek entropi üretir → düşük exergy verimi
- Tipik exergy verimi: %20-40 (kompresörlere kıyasla çok düşük)
- Tasarruf fırsatları genellikle teknoloji değişikliği ve VSD yoluyla

## Dikkat Edilecekler

1. **Düşük verim:** İzokhorik sıkıştırma doğası gereği verimsiz — alternatif teknolojileri değerlendir
2. **Gürültü:** Çok yüksek (85-100 dB) — ses izolasyonu gerekli
3. **Sıcaklık:** Çıkış sıcaklığı yüksek olabilir — yüksek basınç oranlarında dikkat
4. **Basınç bağımsız debi:** Basınç artınca güç artar ama debi değişmez — tıkanma riski yok
5. **Bakım kolaylığı:** Basit yapı — zamanlama dişlisi ve yatak bakımı yeterli
6. **Atıksu arıtma:** En büyük enerji tüketim kalemi — mutlaka değerlendirilmeli

## Referanslar
- Aerzen Technical Documentation — Positive Displacement Blowers
- Atlas Copco Low Pressure Compressor & Blower Manual
- Kaeser Omega Blower Technical Handbook
- DOE/AMO — Wastewater Treatment Plant Energy Efficiency Best Practices
- CAGI Compressed Air & Gas Handbook, 7th Edition
