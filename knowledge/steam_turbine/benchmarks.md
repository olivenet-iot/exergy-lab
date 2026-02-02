---
title: "Buhar Türbini Sektörel Karşılaştırma Verileri — Steam Turbine Benchmarks"
category: reference
equipment_type: steam_turbine
keywords: [buhar türbini, benchmark, izentropik verim, exergy verimi, CHP, kısmi yük, bozunma]
related_files: [steam_turbine/formulas.md, steam_turbine/audit.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/condensing.md, steam_turbine/equipment/orc.md]
use_when: ["Türbin verimlilik karşılaştırması yapılırken", "Performans sınıflandırması gerektiğinde", "Benchmark değerleri referans alınırken"]
priority: high
last_updated: 2026-01-31
---
# Buhar Türbini Sektörel Karşılaştırma Verileri — Steam Turbine Benchmarks

> Son güncelleme: 2026-01-31

## 1. İzentropik Verim Aralıkları (Isentropic Efficiency Ranges)

### 1.1 Boyuta Göre İzentropik Verim

| Güç Aralığı [MW] | Kademe Sayısı | η_is [%] | Açıklama |
|-------------------|---------------|----------|----------|
| <0.5 | 1-2 | 45-65 | Mikro türbin, tek kademe, PRV ikamesi |
| 0.5-1 | 2-5 | 55-72 | Küçük endüstriyel |
| 1-5 | 5-10 | 65-80 | Orta endüstriyel |
| 5-20 | 8-15 | 75-85 | Büyük endüstriyel |
| 20-100 | 12-25 | 82-90 | Santral tipi |
| >100 | 20-40 | 88-93 | Büyük santral, reheatli |

### 1.2 Türbin Tipine Göre İzentropik Verim

| Türbin Tipi | η_is [%] | SSC [kg/kWh] | Açıklama |
|-------------|----------|--------------|----------|
| Karşı basınçlı (back-pressure), küçük | 55-72 | 15-25 | <2 MW, tek kademe |
| Karşı basınçlı, orta | 70-82 | 10-18 | 2-10 MW |
| Karşı basınçlı, büyük | 78-88 | 8-14 | >10 MW |
| Yoğuşmalı (condensing), küçük | 60-75 | 5-7 | <5 MW |
| Yoğuşmalı, orta | 75-85 | 4-5.5 | 5-50 MW |
| Yoğuşmalı, büyük | 85-93 | 3.2-4.2 | >50 MW, reheatli |
| Çekişli (extraction), küçük | 60-75 | — | <5 MW |
| Çekişli, orta-büyük | 72-86 | — | >5 MW |

## 2. Exergy Verimi Benchmarkları (Exergy Efficiency Benchmarks)

### 2.1 Türbin Tipine Göre Exergy Verimi

| Türbin Tipi | η_ex [%] Düşük | η_ex [%] Ortalama | η_ex [%] İyi | η_ex [%] Mükemmel |
|-------------|----------------|--------------------|--------------|--------------------|
| Karşı basınçlı (sadece iş) | <60 | 60-72 | 72-82 | >82 |
| Karşı basınçlı (CHP toplam) | <25 | 25-32 | 32-38 | >38 |
| Yoğuşmalı | <30 | 30-38 | 38-44 | >44 |
| Çekişli (CHP toplam) | <28 | 28-35 | 35-42 | >42 |
| ORC (düşük T) | <20 | 20-35 | 35-50 | >50 |

### 2.2 CHP Sistemi Exergy Verimi (Türbin Bazlı)

| CHP Konfigürasyonu | η_enerji [%] | η_exergy [%] | HPR | Açıklama |
|---------------------|-------------|--------------|-----|----------|
| BP türbin + proses buhar | 80-92 | 25-38 | 3-10 | Düşük elektrik, yüksek ısı |
| Extraction türbin + proses | 75-88 | 28-42 | 2-6 | Esnek HPR |
| Condensing-extraction | 60-80 | 32-45 | 0.5-4 | En esnek |
| Gaz türbini + HRSG + ST | 75-88 | 40-52 | 1.5-3 | Kombine çevrim CHP |
| Gaz motoru CHP | 75-90 | 38-52 | 0.8-1.5 | Yüksek elektrik oranı |

### 2.3 Performans Sınıflandırma Matrisi

```
Buhar türbini (tek başına — iş bazlı exergy verimi):
┌──────────────┬─────────────────┬─────────────────┐
│ Sınıf        │ η_ex (iş) [%]   │ Aksiyon          │
├──────────────┼─────────────────┼─────────────────┤
│ Mükemmel     │ > 82            │ İzleme ve bakım  │
│ İyi          │ 72-82           │ Küçük iyileştirme │
│ Ortalama     │ 60-72           │ Detaylı analiz    │
│ Düşük        │ < 60            │ Acil müdahale     │
└──────────────┴─────────────────┴─────────────────┘

CHP sistemi (exergy verimi):
┌──────────────┬──────────────┬─────────────────┐
│ Sınıf        │ η_ex,CHP [%] │ Aksiyon          │
├──────────────┼──────────────┼─────────────────┤
│ Mükemmel     │ > 38         │ En iyi uygulama  │
│ İyi          │ 32-38        │ Küçük iyileştirme │
│ Ortalama     │ 25-32        │ Optimizasyon      │
│ Düşük        │ < 25         │ Sistem revizyonu  │
└──────────────┴──────────────┴─────────────────┘
```

## 3. Kısmi Yük Performansı (Part-Load Performance)

### 3.1 Kısmi Yük Verim Tablosu

| Yük [%] | Karşı Basınçlı η_is/η_tam | Yoğuşmalı η_is/η_tam | Çekişli η_is/η_tam |
|---------|---------------------------|----------------------|---------------------|
| 100 | 1.00 | 1.00 | 1.00 |
| 90 | 0.99 | 0.99 | 0.99 |
| 80 | 0.97 | 0.97 | 0.97 |
| 70 | 0.94 | 0.95 | 0.95 |
| 60 | 0.90 | 0.92 | 0.91 |
| 50 | 0.85 | 0.88 | 0.86 |
| 40 | 0.78 | 0.82 | 0.80 |
| 30 | 0.70 | 0.74 | 0.72 |

### 3.2 Kontrol Yöntemine Göre Kısmi Yük

```
Kontrol yöntemleri ve verim etkisi:

1. Vana kısma (throttle control):
   - En yaygın, en basit
   - Kısmi yükte verim düşüşü fazla
   - %50 yükte: η/η_tam ≈ 0.85-0.88

2. Nozzle gruplu kontrol (nozzle group governing):
   - Daha iyi kısmi yük verimi
   - Birden fazla vana grubu
   - %50 yükte: η/η_tam ≈ 0.90-0.93

3. Değişken basınç (sliding pressure):
   - En iyi kısmi yük verimi
   - Kazan ile koordineli çalışma
   - %50 yükte: η/η_tam ≈ 0.93-0.96
   - Yalnızca yoğuşmalı veya büyük türbinlerde

4. Bypass kontrolü (extraction türbin):
   - Çekiş miktarı değiştirilerek HPR ayarı
   - Elektrik ve ısı yükü bağımsız kontrol
```

## 4. Buhar Koşullarına Göre Benchmark

### 4.1 Giriş Buhar Koşulları ve Verim

| Buhar Sınıfı | Basınç [bar] | Sıcaklık [°C] | h [kJ/kg] | ex [kJ/kg] | Uygulama |
|--------------|-------------|---------------|-----------|-----------|----------|
| Düşük basınç | 10-20 | 200-300 | 2,830-3,050 | 700-900 | Küçük endüstriyel |
| Orta basınç | 20-45 | 300-420 | 3,000-3,260 | 900-1,200 | Endüstriyel CHP |
| Yüksek basınç | 45-85 | 400-520 | 3,180-3,430 | 1,100-1,400 | Büyük endüstriyel |
| Çok yüksek basınç | 85-170 | 520-600 | 3,380-3,530 | 1,350-1,550 | Santral |
| Süperkritik | >221 | >374 | >3,500 | >1,500 | Büyük santral |

### 4.2 Çıkış Koşuluna Göre Performans

| Çıkış Koşulu | Çıkış Basıncı | Exergy Kaybı | Tipik Uygulama |
|---------------|---------------|-------------|----------------|
| Yüksek BP (proses) | 8-15 bar | Düşük (proses kullanır) | Kağıt, kimya |
| Orta BP (proses) | 3-8 bar | Düşük-Orta | Gıda, tekstil |
| Düşük BP (ısıtma) | 1-3 bar | Orta | Bina ısıtma, DH |
| İyi vakum | 0.05-0.08 bar | Yüksek (kondensere) | Santral |
| Kötü vakum | 0.08-0.15 bar | Çok yüksek | Eski, hava soğutmalı |

## 5. Yaşa Bağlı Bozunma Benchmarkları (Age-Related Degradation)

### 5.1 Verim Bozunma Profili

| Çalışma Süresi [bin saat] | η_is Bozunma [%] | Heat Rate Artışı [%] | Aksiyon |
|---------------------------|-------------------|-----------------------|---------|
| 0-20 | 0-1.5 | 0-2 | Normal bakım |
| 20-40 | 1.5-4.0 | 2-5 | Sızdırmazlık değişimi öner |
| 40-60 | 4.0-8.0 | 5-10 | Major overhaul planla |
| 60-80 | 6.0-12.0 | 8-15 | Overhaul acil veya değiştirme |
| >80 | 8.0-15.0+ | 10-20+ | Ekonomik ömür analizi yap |

### 5.2 Bozunma Kaynakları ve Ölçüleri

| Bozunma Kaynağı | Verim Etkisi [%] | Tespit Yöntemi | Çözüm |
|------------------|-----------------|----------------|-------|
| Kanat aşınması (erosion) | 1-4 | Endoskopi, η_is ölçümü | Kanat değişimi/kaplama |
| Kanat ucu boşluğu (tip clearance) | 0.5-2 | Boşluk ölçümü | Sızdırmazlık yenileme |
| Sızdırmazlık aşınması (seal wear) | 0.5-3 | Buhar kaçağı izleme | Seal değişimi |
| Fouling/birikinti | 0.5-2 | Kademe basınçları | Temizlik |
| Titreşim/dengesizlik | 0.2-1 | Titreşim analizi | Balans/onarım |
| Vana iç kaçağı | 0.5-2 | Çıkış sıcaklığı izleme | Vana bakımı |

### 5.3 Major Overhaul Sonrası İyileşme

```
Overhaul kapsamı ve beklenen iyileşme:

Küçük bakım (minor overhaul — 8-15K saat):
- Sızdırmazlık değişimi
- Vana bakımı
- Beklenen iyileşme: %0.5-1.5 η_is

Orta bakım (intermediate — 20-30K saat):
- Sızdırmazlık + kanat muayenesi
- Rulman değişimi
- Governor kalibrasyonu
- Beklenen iyileşme: %1-3 η_is

Major overhaul (40-60K saat):
- Rotor çıkarma, tam muayene
- Kanat değişimi/onarımı
- Gövde alignment
- Tüm sızdırmazlıklar yenileme
- Beklenen iyileşme: %2-5 η_is
```

## 6. Sektörel Benchmark Karşılaştırması

### 6.1 Sektöre Göre Tipik Buhar Türbini Profili

| Sektör | Tipik Boyut [MW] | Türbin Tipi | η_is [%] | Buhar Koşulları | HPR |
|--------|-----------------|-------------|----------|-----------------|-----|
| Kağıt | 5-30 | Extraction | 75-85 | 40-60 bar, 420-480°C | 4-8 |
| Şeker | 2-15 | Back-pressure | 65-78 | 20-40 bar, 350-420°C | 5-10 |
| Kimya | 5-50 | Ext/Cond | 78-88 | 40-85 bar, 420-520°C | 2-5 |
| Çimento | 5-20 | Condensing | 72-82 | 30-60 bar, 400-480°C | — |
| Çelik | 10-100 | Ext/Cond | 80-90 | 40-100 bar, 480-540°C | 1-4 |
| Gıda | 0.5-5 | Back-pressure | 55-72 | 10-25 bar, 250-350°C | 6-12 |
| Rafineri | 10-80 | Extraction | 78-88 | 40-85 bar, 420-520°C | 2-5 |
| Enerji santral | 50-600+ | Cond/Reheat | 88-93 | 100-250 bar, 540-600°C | — |

### 6.2 Sektörel CHP Performans Karşılaştırma

| Sektör | η_enerji [%] | η_exergy [%] | PES [%] | Çalışma Saati [h/yıl] |
|--------|-------------|-------------|---------|------------------------|
| Kağıt | 80-88 | 30-40 | 15-28 | 7,500-8,500 |
| Şeker | 78-88 | 25-35 | 10-22 | 3,500-5,000 (kampanya) |
| Kimya | 82-90 | 35-45 | 18-30 | 7,000-8,500 |
| Gıda | 75-85 | 22-32 | 10-20 | 5,000-7,000 |
| Rafineri | 80-88 | 35-48 | 20-32 | 8,000-8,500 |

## 7. ORC Benchmark Verileri

### 7.1 ORC Termal ve Exergy Verimi

| Kaynak Sıcaklığı [°C] | Akışkan | η_th [%] | η_ex [%] | Güç [kW] | Uygulama |
|------------------------|---------|----------|----------|----------|----------|
| 80-100 | R245fa | 5-8 | 25-40 | 10-200 | Jeotermal, endüstriyel |
| 100-150 | R245fa | 8-13 | 35-50 | 50-1,000 | Endüstriyel atık ısı |
| 150-200 | R245fa/SES36 | 12-18 | 40-55 | 100-3,000 | Baca gazı, motor egzoz |
| 200-300 | Siloksan/Tolüen | 18-25 | 45-60 | 200-5,000 | Yüksek T endüstriyel |
| 300-400 | Siloksan | 22-28 | 50-65 | 500-10,000 | Çimento, cam |

### 7.2 ORC vs. Buhar Türbini Karşılaştırma

| Parametre | ORC | Küçük Buhar Türbini |
|-----------|-----|---------------------|
| Kaynak sıcaklığı [°C] | 80-350 | 200-600 |
| Güç aralığı [kW] | 10-10,000 | 100-50,000+ |
| Termal verim [%] | 5-25 | 15-42 |
| Exergy verimi [%] | 25-60 | 50-90 |
| Su ihtiyacı | Düşük/yok (hava soğutmalı) | Yüksek (DM su) |
| Bakım | Düşük (kapalı çevrim) | Orta-yüksek |
| Otomasyon | Tam otomatik | Operatör gerekli |
| Kısmi yük | İyi | Orta |
| Yatırım [EUR/kW] | 1,500-4,000 | 400-1,500 |

## 8. Ekonomik Benchmark

### 8.1 Yatırım Maliyeti (CAPEX)

| Türbin Tipi | Güç [MW] | Birim Maliyet [EUR/kW] | Toplam Maliyet [EUR] |
|-------------|----------|------------------------|----------------------|
| Mikro türbin (PRV ikamesi) | 0.05-0.5 | 1,500-3,000 | 75K-1.5M |
| Karşı basınçlı (küçük) | 0.5-2 | 800-1,500 | 400K-3M |
| Karşı basınçlı (orta) | 2-10 | 600-1,000 | 1.2M-10M |
| Karşı basınçlı (büyük) | 10-50 | 400-700 | 4M-35M |
| Yoğuşmalı (endüstriyel) | 5-50 | 700-1,200 | 3.5M-60M |
| Yoğuşmalı (santral) | 50-500 | 500-900 | 25M-450M |
| ORC modülü | 0.05-5 | 1,500-4,000 | 75K-20M |

### 8.2 İşletme Maliyeti (OPEX)

| Türbin Tipi | Bakım [EUR-ct/kWh] | Major Overhaul [EUR/MW] | Overhaul Aralığı |
|-------------|---------------------|-------------------------|------------------|
| Karşı basınçlı | 0.2-0.5 | 30,000-60,000 | 40-60K saat |
| Yoğuşmalı | 0.3-0.8 | 50,000-100,000 | 30-50K saat |
| ORC | 0.5-1.5 | 20,000-40,000 | 50-80K saat |

### 8.3 Tipik Geri Ödeme Süreleri

| Uygulama | SPP [yıl] | NPV/Yatırım | IRR [%] |
|----------|-----------|-------------|---------|
| PRV → Mikro türbin ikamesi | 2-5 | 1.0-3.0 | 20-45 |
| Yeni karşı basınçlı CHP | 3-6 | 0.8-2.5 | 15-30 |
| Yeni çekişli CHP | 3-7 | 0.7-2.0 | 12-25 |
| Overhaul (verim iyileştirme) | 0.5-2 | 3.0-8.0 | 50-150 |
| ORC atık ısı | 3-7 | 0.5-2.0 | 12-25 |

## 9. Türbin Eksüre ve Çıkış Kaybı Benchmarkları

### 9.1 Exhaust Loss (Son Kademe Çıkış Kaybı)

| Son Kademe Kanat Boy [mm] | Annüler Alan [m²] | Exhaust Loss [kJ/kg] | V_çıkış [m/s] |
|---------------------------|--------------------|-----------------------|---------------|
| 200-350 | 0.2-0.8 | 20-40 | 200-300 |
| 350-500 | 0.5-1.5 | 12-25 | 150-220 |
| 500-750 | 1.0-3.0 | 8-15 | 100-180 |
| 750-1,000 | 2.0-5.0 | 5-10 | 80-150 |
| >1,000 | 3.5-8.0 | 3-8 | 60-120 |

### 9.2 Yardımcı Ekipman Enerji Tüketimi

| Yardımcı Ekipman | Tüketim [% brüt güç] | Açıklama |
|-------------------|----------------------|----------|
| Besleme suyu pompası | 1.5-3.5 | Yüksek basınçta fazla |
| Yoğuşma suyu pompası | 0.1-0.3 | |
| Soğutma suyu pompası | 0.5-1.5 | Yoğuşmalı türbinlerde |
| Soğutma kulesi fanı | 0.3-1.0 | Yaş kule |
| Vakum pompası/ejektör | 0.1-0.3 | |
| Yağ sistemi | 0.1-0.2 | |
| Toplam yardımcı | 3-7 | Net güç = Brüt - Yardımcı |

## 10. Karşılaştırmalı Prime Mover Tablosu (CHP İçin)

| Parametre | Buhar Türbini | Gaz Türbini | Gaz Motoru | Yakıt Hücresi |
|-----------|---------------|-------------|------------|---------------|
| Elektrik verimi [%] | 15-30 (CHP) | 25-40 | 35-45 | 40-60 |
| Isı verimi [%] | 50-70 | 40-50 | 35-45 | 30-40 |
| Toplam verim [%] | 75-92 | 70-85 | 75-90 | 75-90 |
| Exergy verimi [%] | 25-38 | 35-48 | 40-52 | 48-62 |
| HPR | 3-10 | 1.5-2.5 | 0.8-1.5 | 0.5-1.0 |
| Yakıt esnekliği | Herhangi | Gaz/sıvı | Gaz/sıvı | H₂/gaz |
| Ömür [yıl] | 25-35+ | 20-30 | 15-25 | 10-20 |
| Başlangıç süresi | 1-8 saat | 10-30 dk | 1-5 dk | 1-3 saat |
| Yatırım [EUR/kWe] | 600-1,200 | 800-1,500 | 700-1,400 | 3,000-6,000 |
| Bakım [EUR-ct/kWh] | 0.3-0.5 | 0.5-1.0 | 1.0-2.0 | 1.5-3.0 |

## İlgili Dosyalar

- [Formüller](formulas.md) — Exergy hesaplama formülleri
- [Denetim](audit.md) — Performans testi metodolojisi
- [Karşı Basınçlı Türbin](equipment/back_pressure.md) — BP türbin detayları
- [Yoğuşmalı Türbin](equipment/condensing.md) — Condensing türbin detayları
- [ORC](equipment/orc.md) — Organic Rankine Cycle benchmarkları
- [Mikro Türbin](equipment/micro_turbine.md) — Mikro türbin PRV ikamesi
- [CHP Sistemleri](systems/steam_turbine_chp.md) — CHP konfigürasyonları
- [Fizibilite](economics/feasibility.md) — CHP fizibilite kriterleri
- [Kazan Benchmarkları](../boiler/benchmarks.md) — Kazan verim karşılaştırma
- [Fabrika Benchmarkları](../factory/factory_benchmarks.md) — Fabrika sektörel benchmark
- [İleri Exergy Analizi](../factory/advanced_exergy/overview.md) — AV/UN, EN/EX dekompozisyon

## Referanslar

- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition.
- US DOE (2012). *Improving Steam System Performance — A Sourcebook for Industry*, 2nd Edition.
- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration"
- IEA (2020). *World Energy Outlook*, International Energy Agency.
- Tsatsaronis, G. & Morosuk, T. (2012). "Advanced exergy-based methods used to understand and improve energy-conversion systems," *Energy*.
