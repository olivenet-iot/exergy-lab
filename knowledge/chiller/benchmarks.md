---
title: "Chiller Benchmark Verileri"
category: reference
equipment_type: chiller
keywords: [benchmark, chiller, COP, kW/RT]
related_files: [chiller/formulas.md, chiller/audit.md, chiller/solutions/vsd.md]
use_when: ["Chiller performansı değerlendirilirken", "COP karşılaştırması yapılırken"]
priority: high
last_updated: 2026-01-31
---
# Chiller Benchmark Verileri

> Son güncelleme: 2026-01-31

## 1. COP (Performans Katsayısı) Aralıkları

### 1.1 Su Soğutmalı Buhar Sıkıştırmalı Chiller (Tam Yük)

| Kompresör Tipi | Düşük | Ortalama | İyi | Mükemmel |
|----------------|-------|----------|-----|----------|
| Santrifüj (>500 kW) | <5.0 | 5.0-6.0 | 6.0-7.0 | >7.0 |
| Santrifüj VSD (>500 kW) | <5.5 | 5.5-6.5 | 6.5-7.5 | >7.5 |
| Vidalı (50-500 kW) | <4.5 | 4.5-5.5 | 5.5-6.5 | >6.5 |
| Scroll (10-200 kW) | <4.0 | 4.0-5.0 | 5.0-6.0 | >6.0 |
| Pistonlu (10-200 kW) | <3.5 | 3.5-4.5 | 4.5-5.5 | >5.5 |

### 1.2 Hava Soğutmalı Buhar Sıkıştırmalı Chiller (Tam Yük)

| Kompresör Tipi | Düşük | Ortalama | İyi | Mükemmel |
|----------------|-------|----------|-----|----------|
| Vidalı | <2.5 | 2.5-3.2 | 3.2-3.8 | >3.8 |
| Scroll | <2.3 | 2.3-3.0 | 3.0-3.5 | >3.5 |
| Pistonlu | <2.0 | 2.0-2.8 | 2.8-3.2 | >3.2 |

### 1.3 Absorpsiyonlu Chiller COP

| Tip | COP Aralığı | Not |
|-----|-------------|-----|
| Tek etkili (LiBr-Su) | 0.65-0.75 | Sıcak su/düşük basınçlı buhar |
| Çift etkili (LiBr-Su) | 1.0-1.4 | Yüksek basınçlı buhar/doğrudan ateşleme |
| Üç etkili (LiBr-Su) | 1.4-1.7 | Doğrudan ateşleme |
| Tek etkili (NH₃-Su) | 0.5-0.65 | Düşük sıcaklık uygulamaları |

### 1.4 ASHRAE 90.1-2019 Minimum COP Gereksinimleri

| Chiller Tipi | Kapasite | Min. COP (Tam Yük) | Min. IPLV |
|-------------|----------|--------------------|-----------|
| Su soğ. santrifüj | <264 kW | 5.8 | 9.6 |
| Su soğ. santrifüj | 264-528 kW | 5.8 | 9.6 |
| Su soğ. santrifüj | 528-1055 kW | 6.2 | 10.0 |
| Su soğ. santrifüj | >1055 kW | 6.2 | 10.0 |
| Su soğ. vidalı/scroll | <264 kW | 5.5 | 9.2 |
| Su soğ. vidalı/scroll | ≥264 kW | 5.5 | 9.2 |
| Hava soğ. tüm tipler | <264 kW | 3.0 | 3.9 |
| Hava soğ. tüm tipler | ≥264 kW | 3.0 | 3.9 |

## 2. IPLV/NPLV (Kısmi Yük Verimi)

### 2.1 IPLV Formülü

```
IPLV = 0.01×COP_100% + 0.42×COP_75% + 0.45×COP_50% + 0.12×COP_25%
```

### 2.2 IPLV Aralıkları (Su Soğutmalı)

| Kompresör Tipi | Düşük | Ortalama | İyi | Mükemmel |
|----------------|-------|----------|-----|----------|
| Santrifüj sabit hız | <5.5 | 5.5-7.0 | 7.0-8.5 | >8.5 |
| Santrifüj VSD | <7.0 | 7.0-9.0 | 9.0-11.0 | >11.0 |
| Vidalı sabit hız | <4.5 | 4.5-6.0 | 6.0-7.5 | >7.5 |
| Vidalı VSD | <6.0 | 6.0-8.0 | 8.0-9.5 | >9.5 |
| Scroll | <4.0 | 4.0-5.5 | 5.5-7.0 | >7.0 |

### 2.3 IPLV / COP Oranı (Kısmi Yük Avantajı)

| Kontrol Tipi | IPLV/COP Oranı | Açıklama |
|-------------|----------------|----------|
| Sabit hız + slide valve | 1.0-1.2 | Düşük kısmi yük avantajı |
| Sabit hız + IGV | 1.1-1.3 | Orta kısmi yük avantajı |
| VSD (vidalı) | 1.3-1.6 | İyi kısmi yük avantajı |
| VSD + IGV (santrifüj) | 1.4-1.7 | Yüksek kısmi yük avantajı |

## 3. kW/ton Benchmark

### 3.1 Genel Sınıflandırma

```
1 ton soğutma = 3.517 kW
kW/ton = 3.517 / COP
```

| Sınıf | kW/ton (Tam Yük) | COP Karşılığı | Değerlendirme |
|-------|-------------------|---------------|---------------|
| Mükemmel | <0.50 | >7.0 | Modern VSD santrifüj |
| İyi | 0.50-0.65 | 5.4-7.0 | Verimli su soğutmalı |
| Ortalama | 0.65-0.85 | 4.1-5.4 | Standart su soğutmalı |
| Düşük | 0.85-1.20 | 2.9-4.1 | Hava soğutmalı veya eski |
| Çok Düşük | >1.20 | <2.9 | Eski/bakımsız hava soğutmalı |

### 3.2 Sistem Seviyesi kW/ton (Chiller + Pompa + Kule)

| Sınıf | Sistem kW/ton | Açıklama |
|-------|---------------|----------|
| Mükemmel | <0.70 | VSD chiller + VSD pompalar + optimize kule |
| İyi | 0.70-0.90 | İyi tasarlanmış modern sistem |
| Ortalama | 0.90-1.20 | Standart sistem |
| Düşük | >1.20 | Eski veya optimize edilmemiş sistem |

## 4. Exergy Verimi Aralıkları

### 4.1 Chiller Exergy Verimi (Soğutma Suyu Bazlı)

| Chiller Tipi | Düşük | Ortalama | İyi | Mükemmel |
|-------------|-------|----------|-----|----------|
| Santrifüj (su soğ.) | <25% | 25-35% | 35-45% | >45% |
| Vidalı (su soğ.) | <20% | 20-30% | 30-40% | >40% |
| Scroll (su soğ.) | <18% | 18-28% | 28-35% | >35% |
| Hava soğutmalı | <12% | 12-20% | 20-28% | >28% |
| Absorpsiyonlu (tek etkili) | <10% | 10-15% | 15-22% | >22% |
| Absorpsiyonlu (çift etkili) | <15% | 15-20% | 20-28% | >28% |

### 4.2 Sistem Exergy Verimi (Chiller + Yardımcılar)

| Sistem Durumu | η_system | Açıklama |
|--------------|----------|----------|
| Düşük | <%15 | Eski, sabit hız, bakımsız |
| Ortalama | %15-25 | Standart sistem |
| İyi | %25-35 | VSD, optimize edilmiş |
| Mükemmel | >%35 | Tam optimize, free cooling dahil |

## 5. Yaklaşım Sıcaklıkları (Approach Temperature)

### 5.1 Kondenser Yaklaşım (Su Soğutmalı)

```
Approach_cond = T_cond_ref_out - T_cw_in

Burada:
  T_cond_ref_out = Kondenser soğutucu akışkan yoğuşma sıcaklığı
  T_cw_in = Kondenser suyu giriş sıcaklığı
```

| Durum | Approach (°C) | Aksiyon |
|-------|---------------|---------|
| Mükemmel | <1.5 | Yeni veya temizlenmiş |
| İyi | 1.5-2.5 | Normal çalışma |
| Ortalama | 2.5-4.0 | Temizlik planla |
| Düşük | >4.0 | Acil temizlik gerekli |

### 5.2 Kondenser Yaklaşım (Hava Soğutmalı)

```
Approach_cond = T_cond_ref - T_ambient
```

| Durum | Approach (°C) | Aksiyon |
|-------|---------------|---------|
| Mükemmel | <10 | Yeni, temiz fanlar |
| İyi | 10-15 | Normal |
| Ortalama | 15-20 | Fan/yüzey temizliği |
| Düşük | >20 | Acil bakım |

### 5.3 Evaporatör Yaklaşım

```
Approach_evap = T_chw_out - T_evap_ref

Burada:
  T_chw_out = Soğutma suyu çıkış sıcaklığı
  T_evap_ref = Evaporatör soğutucu akışkan buharlaşma sıcaklığı
```

| Durum | Approach (°C) | Aksiyon |
|-------|---------------|---------|
| Mükemmel | <1.5 | Yeni/temiz evaporatör |
| İyi | 1.5-2.5 | Normal |
| Ortalama | 2.5-4.0 | Fouling başlamış |
| Düşük | >4.0 | Temizlik/tube cleaning gerekli |

### 5.4 Soğutma Kulesi Yaklaşım

```
Tower_approach = T_cw_out - T_wb

Burada:
  T_cw_out = Soğutma kulesi çıkış suyu sıcaklığı
  T_wb = Ortam yaş termometre sıcaklığı
```

| Durum | Approach (°C) | Aksiyon |
|-------|---------------|---------|
| Mükemmel | <3 | Yeni, optimize fill |
| İyi | 3-5 | Normal performans |
| Ortalama | 5-8 | Fill/nozzle kontrolü |
| Düşük | >8 | Kule revizyonu gerekli |

## 6. Lift Benchmark

### 6.1 Lift Tanımı ve Aralıkları

```
Lift = T_cond - T_evap (soğutucu akışkan sıcaklıkları)
```

| Durum | Lift (°C) | COP Etkisi | Açıklama |
|-------|-----------|------------|----------|
| Düşük (optimum) | <25 | En yüksek COP | Düşük ambient, yüksek CHW |
| Normal | 25-35 | Normal COP | Standart çalışma |
| Yüksek | 35-45 | Düşük COP | Sıcak ambient, düşük CHW |
| Çok yüksek | >45 | Çok düşük COP | Aşırı koşullar |

### 6.2 Lift-COP İlişkisi (Tipik Santrifüj)

| Lift (°C) | Beklenen COP | kW/ton |
|-----------|-------------|--------|
| 20 | 8.0-9.0 | 0.39-0.44 |
| 25 | 6.5-7.5 | 0.47-0.54 |
| 30 | 5.5-6.5 | 0.54-0.64 |
| 35 | 4.8-5.5 | 0.64-0.73 |
| 40 | 4.0-4.8 | 0.73-0.88 |
| 45 | 3.5-4.0 | 0.88-1.00 |

## 7. Yaş-Verim İlişkisi

### 7.1 Bakım Kalitesine Göre COP Düşüşü

| Yaş | İyi Bakım | Ortalama Bakım | Kötü Bakım |
|-----|-----------|----------------|------------|
| 0-3 yıl | %0-2 | %0-3 | %0-5 |
| 3-5 yıl | %1-3 | %3-5 | %5-10 |
| 5-10 yıl | %3-7 | %5-12 | %10-20 |
| 10-15 yıl | %5-12 | %10-20 | %15-30 |
| 15-20 yıl | %8-15 | %15-25 | %25-40 |
| >20 yıl | %12-20 | %20-35 | %35-50 |

### 7.2 COP Bozulma Nedenleri

| Neden | COP Etkisi | Tespit Yöntemi |
|-------|-----------|----------------|
| Kondenser fouling | %5-15 düşüş | Approach artışı |
| Evaporatör fouling | %3-10 düşüş | Approach artışı |
| Soğutucu akışkan kaçağı | %5-20 düşüş | Basınç/sıcaklık anomalisi |
| Yağ birikimi (evaporatör) | %2-8 düşüş | Yağ seviyesi azalması |
| Non-condensable gaz | %5-15 düşüş | Yüksek head pressure |
| Kompresör aşınması | %3-10 düşüş | Amper artışı, kapasite düşüşü |

### 7.3 Yenileme Kararı Kuralları

- Yıllık enerji maliyeti farkı > yeni chiller maliyetinin %12'si → değiştirmeyi değerlendir
- Bakım maliyeti > yeni chiller yıllık amortisman maliyetinin %50'si → değiştirmeyi değerlendir
- Yaş >20 yıl VE COP düşüşü >%20 VE soğutucu akışkan phase-out → kesinlikle değiştir
- R-22 kullanan chiller → 2030'a kadar değiştirme planlanmalı (EU F-gas)

## 8. Sektörel Karşılaştırma

### 8.1 Sektöre Göre Tipik Chiller Performansı

| Sektör | Tipik COP | Tipik kW/ton | Not |
|--------|-----------|-------------|-----|
| Data center | 5.5-7.0 | 0.50-0.64 | Yüksek güvenilirlik, yıl boyu |
| Ticari bina (ofis) | 4.5-6.0 | 0.59-0.78 | Mevsimsel, primer-sekonder |
| Hastane | 4.0-5.5 | 0.64-0.88 | 7/24 çalışma, güvenilirlik |
| Alışveriş merkezi | 4.5-5.5 | 0.64-0.78 | Yüksek iç kazanç |
| Endüstriyel proses | 3.5-6.5 | 0.54-1.00 | Çok değişken |
| İlaç | 4.5-6.0 | 0.59-0.78 | Yedeklilik gerekli |
| Otel | 4.0-5.5 | 0.64-0.88 | Mevsimsel, değişken yük |

### 8.2 İklim Bölgesine Göre Yıllık Performans

| İklim Bölgesi | Yıllık Ort. COP | Soğutma Saati | Free Cooling Potansiyeli |
|---------------|-----------------|---------------|--------------------------|
| Soğuk (Kuzey Avrupa) | 5.5-7.0 | 1500-3000 | %30-50 |
| Ilıman (Orta Avrupa) | 5.0-6.5 | 2500-4000 | %15-30 |
| Sıcak-kuru (Akdeniz) | 4.5-5.5 | 3500-5500 | %5-15 |
| Sıcak-nemli (Tropik) | 4.0-5.0 | 5000-8000 | <%5 |
| İstanbul (tipik) | 4.8-6.0 | 3000-4500 | %10-25 |

## 9. Soğutucu Akışkan Performans Karşılaştırması

| Akışkan | Tipik COP (Su Soğ.) | GWP | ODP | Durum |
|---------|---------------------|-----|-----|-------|
| R-134a | 5.5-6.5 | 1430 | 0 | Phase-down |
| R-410A | 5.0-6.0 | 2088 | 0 | Phase-down |
| R-1234ze(E) | 5.3-6.3 | 7 | 0 | Yeni standart |
| R-1234yf | 5.0-6.0 | 4 | 0 | Otomotiv, küçük chiller |
| R-513A | 5.3-6.3 | 631 | 0 | Geçiş akışkanı |
| R-290 (propan) | 5.0-6.0 | 3 | 0 | Küçük kapasite |
| R-717 (amonyak) | 5.5-7.0 | 0 | 0 | Endüstriyel |
| R-744 (CO₂) | 3.5-5.0 | 1 | 0 | Transkritik, düşük T |

## 10. Isı Geri Kazanım Potansiyeli

| Chiller Gücü (kW) | Kondenser Isısı (kW) | Geri Kazanılabilir (kW) | Tipik Kullanım |
|-------------------|---------------------|------------------------|----------------|
| 100 | 120 | 50-80 | Kullanım suyu |
| 300 | 350 | 150-250 | Bina ısıtma + kullanım suyu |
| 500 | 580 | 250-400 | Proses + bina |
| 1000 | 1150 | 500-800 | Merkezi ısıtma |
| 3000 | 3500 | 1500-2500 | District heating |

Geri kazanılabilir ısı ≈ Q_cond × %70 × HRU verimi (%80-90)

## İlgili Dosyalar
- Exergy formülleri: `formulas/chiller_exergy.md`
- Buhar sıkıştırmalı chiller: `equipment/chiller_vapor_compression.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Vidalı chiller: `equipment/chiller_screw.md`
- Absorpsiyonlu chiller: `equipment/chiller_absorption.md`
- Soğutucu akışkanlar: `equipment/chiller_refrigerants.md`
- VSD çözümü: `solutions/chiller_vsd.md`
- Audit metodolojisi: `methodology/chiller_audit.md`

## Referanslar
- AHRI Standard 550/590, "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages"
- AHRI Standard 560, "Absorption Water-Chilling and Water-Heating Packages"
- ASHRAE Standard 90.1-2019, "Energy Standard for Buildings"
- ASHRAE Handbook — HVAC Systems and Equipment (2020)
- Eurovent Certification Programme
- US DOE, "Federal Energy Management Program — Chiller Efficiency"
- Carrier, Trane, York/Johnson Controls, Daikin Technical Documentation
- Lawrence Berkeley National Laboratory, "Chiller Plant Optimization"
