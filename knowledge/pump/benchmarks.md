---
title: "Pompa Benchmark Verileri"
category: reference
equipment_type: pump
keywords: [benchmark, pompa, özgül enerji, verimlilik]
related_files: [pump/formulas.md, pump/audit.md, pump/solutions/vsd.md]
use_when: ["Pompa performansı değerlendirilirken", "Özgül enerji karşılaştırması yapılırken"]
priority: high
last_updated: 2026-01-31
---
# Pompa Benchmark Verileri

> Son güncelleme: 2026-01-31

## 1. Exergy Verimi Aralıkları

| Pompa Tipi | Düşük | Ortalama | İyi | Best-in-class |
|------------|-------|----------|-----|---------------|
| Santrifüj (küçük <10 kW) | <%35 | %35-50 | %50-60 | >%60 |
| Santrifüj (orta 10-100 kW) | <%45 | %45-55 | %55-65 | >%65 |
| Santrifüj (büyük >100 kW) | <%50 | %50-60 | %60-70 | >%70 |
| PD - Pistonlu (küçük) | <%30 | %30-45 | %45-55 | >%55 |
| PD - Pistonlu (büyük) | <%40 | %40-50 | %50-60 | >%60 |
| PD - Diyafram | <%25 | %25-40 | %40-50 | >%50 |
| Dalgıç (submersible) | <%35 | %35-50 | %50-60 | >%60 |
| Dalgıç (derin kuyu) | <%30 | %30-45 | %45-55 | >%55 |
| Aksiyel (propeller) | <%50 | %50-60 | %60-72 | >%72 |
| Karışık akışlı (mixed flow) | <%45 | %45-58 | %58-68 | >%68 |

Not: Exergy verimi, pompa çıkışındaki basınç exergy'sinin elektrik girişine oranını ifade eder.
Enerji (birinci yasa) verimi ile karıştırılmamalıdır.

## 2. Pompa Verimi (BEP Bazında) — Tip ve Kapasiteye Göre

### 2.1 Santrifüj Pompalar — Radyal

| Nominal Güç (kW) | Debi Aralığı (m³/h) | BEP Verimi | Not |
|-------------------|---------------------|------------|-----|
| 0.5-2 | 1-10 | %40-55 | Küçük domestik |
| 2-5 | 5-30 | %50-65 | Küçük endüstriyel |
| 5-15 | 15-80 | %60-72 | Orta |
| 15-37 | 50-200 | %68-78 | Orta-büyük |
| 37-75 | 100-500 | %72-82 | Büyük |
| 75-150 | 200-1000 | %78-86 | Çok büyük |
| 150-500 | 500-3000 | %82-88 | Endüstriyel |
| >500 | >2000 | %85-92 | Ağır endüstriyel |

### 2.2 Dalgıç Pompalar (Submersible)

| Nominal Güç (kW) | Debi Aralığı (m³/h) | BEP Verimi | Not |
|-------------------|---------------------|------------|-----|
| 1-5 | 2-20 | %40-55 | Küçük dalgıç |
| 5-15 | 10-60 | %55-68 | Orta dalgıç |
| 15-55 | 30-200 | %65-76 | Büyük dalgıç |
| 55-150 | 100-800 | %72-82 | Endüstriyel dalgıç |
| >150 | >500 | %78-86 | Ağır hizmet dalgıç |

### 2.3 Pozitif Deplasmalı (PD) Pompalar

| Alt Tip | BEP Verimi | Tipik Uygulama |
|---------|------------|----------------|
| Pistonlu (plunger), küçük (<5 kW) | %60-75 | Dozlama, yıkama |
| Pistonlu (plunger), büyük (>5 kW) | %75-90 | Yüksek basınç, proses |
| Diyafram | %50-70 | Kimyasal dozlama |
| Vidalı (screw) | %60-80 | Viskoz sıvılar |
| Loblu (lobe) | %50-70 | Gıda, kozmetik |
| Dişli (gear) | %60-80 | Hidrolik, yağ transferi |
| Peristaltik | %30-50 | Aşındırıcı sıvılar |

### 2.4 Aksiyel ve Karışık Akışlı Pompalar

| Tip | BEP Verimi | Tipik Uygulama |
|-----|------------|----------------|
| Aksiyel (propeller) | %80-92 | Düşük hat, yüksek debi |
| Karışık akışlı (mixed flow) | %78-88 | Orta hat, yüksek debi |

## 3. Wire-to-Water Verim

### 3.1 Genel Wire-to-Water Sınıflandırması

| Sistem Durumu | W2W Verimi | Açıklama |
|---------------|------------|----------|
| Mükemmel | >%70 | VSD, optimum boyut, düşük sürtünüm, iyi bakım |
| İyi | %55-70 | Modern ekipman, uygun boyut, periyodik bakım |
| Ortalama | %40-55 | Standart endüstriyel, kısmi throttle |
| Düşük | %25-40 | Aşırı boyutlu, sürekli throttle, eski ekipman |
| Çok düşük | <%25 | Ciddi boyutlandırma hatası, bakımsız, eski |

### 3.2 Wire-to-Water Verim Bileşenleri

| Bileşen | Tipik Verim Aralığı | Not |
|---------|---------------------|-----|
| Motor verimi (η_motor) | %88-96 | IE sınıfına ve boyutuna bağlı |
| VSD verimi (η_VSD) | %95-98 | Varsa; yoksa %100 (doğrudan hat) |
| Pompa verimi (η_pump) | %50-90 | Tip ve boyutuna bağlı |
| Mekanik verim (salmastra, rulman) | %96-99 | Bakım durumuna bağlı |

```
W2W = η_motor × η_VSD × η_pump × η_mekanik
```

Örnek: %93 × %97 × %78 × %98 = %69 (iyi sistem)

## 4. Spesifik Enerji Tüketimi (kWh/m³)

Teorik minimum: 0.002725 kWh/m³ hat başına metre (ideal pompa, %100 verim).

### 4.1 H = 20 m (düşük basınç) için Benchmark

| Sınıf | SEC [kWh/m³] | W2W Verimi | Açıklama |
|-------|-------------|------------|----------|
| Best-in-class | <0.065 | >%83 | Optimum boyut, VSD |
| İyi | 0.065-0.080 | %67-83 | Modern, uygun boyut |
| Ortalama | 0.080-0.110 | %49-67 | Standart endüstriyel |
| Düşük | 0.110-0.160 | %34-49 | Aşırı boyutlu, throttle |
| Çok düşük | >0.160 | <%34 | Acil müdahale |

### 4.2 H = 50 m (orta basınç) için Benchmark

| Sınıf | SEC [kWh/m³] | W2W Verimi | Açıklama |
|-------|-------------|------------|----------|
| Best-in-class | <0.16 | >%85 | Büyük, optimize |
| İyi | 0.16-0.21 | %65-85 | Modern, iyi bakım |
| Ortalama | 0.21-0.30 | %45-65 | Standart |
| Düşük | 0.30-0.45 | %30-45 | Verimsiz |
| Çok düşük | >0.45 | <%30 | Acil müdahale |

### 4.3 H = 100 m (yüksek basınç) için Benchmark

| Sınıf | SEC [kWh/m³] | W2W Verimi | Açıklama |
|-------|-------------|------------|----------|
| Best-in-class | <0.32 | >%85 | Çok kademeli, VSD |
| İyi | 0.32-0.42 | %65-85 | İyi boyutlandırılmış |
| Ortalama | 0.42-0.60 | %45-65 | Standart |
| Düşük | 0.60-0.90 | %30-45 | Ciddi iyileştirme potansiyeli |
| Çok düşük | >0.90 | <%30 | Acil müdahale |

### 4.4 SEC Hesap Formülü

```
SEC = (ρ × g × H) / (η_w2w × 3.6 × 10⁶)   [kWh/m³]

Burada:
- ρ = 1000 kg/m³ (su için)
- g = 9.81 m/s²
- H = toplam hat [m]
- η_w2w = wire-to-water verimi (ondalık)
- 3.6 × 10⁶ = J'den kWh'ye dönüşüm
```

## 5. Kısmi Yük Verimliliği

### 5.1 Throttle Kontrol (Kelebek Vana ile Debi Kontrolü)

| Debi % (BEP'e göre) | Güç % | Efektif SEC % | Not |
|----------------------|-------|---------------|-----|
| 100% | 100% | 100% | Tam debi |
| 90% | 95% | 106% | Hafif throttle |
| 80% | 90% | 113% | Orta throttle |
| 70% | 85% | 121% | Belirgin kayıp |
| 60% | 80% | 133% | Ciddi israf |
| 50% | 75% | 150% | Çok verimsiz |
| 40% | 70% | 175% | Kritik israf |
| 30% | 65% | 217% | Kabul edilemez |

Not: Değerler tipik bir sürtünüm-ağırlıklı sistem içindir. Statik hat oranı arttıkça throttle kaybı azalır.

### 5.2 VSD Kontrol (Değişken Hızlı Sürücü)

| Debi % | Güç % (saf sürtünüm) | Güç % (%30 statik hat) | Not |
|--------|----------------------|------------------------|-----|
| 100% | 100% | 100% | Tam hız |
| 90% | 73% | 79% | Affinity law etkisi |
| 80% | 51% | 61% | Belirgin tasarruf |
| 70% | 34% | 46% | Önemli tasarruf |
| 60% | 22% | 34% | Büyük tasarruf |
| 50% | 13% | 25% | Çok büyük tasarruf |
| 40% | 6% | 18% | Minimum hıza yakın |

Saf sürtünüm sistemi (statik hat = 0): P ∝ N³ (küp kanunu).
Statik hat varsa tasarruf azalır çünkü statik hat VSD ile düşmez.

### 5.3 VSD vs Throttle Tasarruf Karşılaştırması (sürtünüm-ağırlıklı sistem)

| Debi % | Throttle Güç % | VSD Güç % | VSD Tasarrufu |
|--------|----------------|-----------|---------------|
| 100% | 100% | 100% | %0 (VSD hafif dezavantajlı) |
| 80% | ~90% | ~51% | ~%43 |
| 60% | ~80% | ~22% | ~%73 |
| 50% | ~75% | ~13% | ~%83 |
| 40% | ~70% | ~6% | ~%91 |

### 5.4 Bypass Kontrol

| Debi % | Güç % | Not |
|--------|-------|-----|
| 100% | 100% | Bypass kapalı |
| 80% | ~100% | Pompa tam hızda, %20 bypass |
| 60% | ~100% | Pompa tam hızda, %40 bypass |
| 40% | ~100% | Pompa tam hızda, %60 bypass |

Bypass kontrolü en verimsiz yöntemdir — pompa sürekli tam güçte çalışır.

## 6. Motor Verimlilik Sınıfı Etkisi

| Motor Sınıfı | Tipik Verim (15-75 kW) | SEC Etkisi (IE3 bazlı) |
|-------------|----------------------|----------------------|
| IE1 (Standart) | %87.0-90.5 | %3-5 daha yüksek SEC |
| IE2 (Yüksek) | %90.5-92.5 | %1.5-3 daha yüksek SEC |
| IE3 (Premium) | %92.5-94.5 | Baz değer |
| IE4 (Süper Premium) | %94.5-95.5 | %1-1.5 daha düşük SEC |
| IE5 (Ultra Premium) | %95.5-96.5 | %2-2.5 daha düşük SEC |

Not: AB'de 2021'den itibaren 0.75-1000 kW motorlarda IE3 minimum zorunlu (EU 2019/1781).
2023'ten itibaren 75-200 kW motorlarda IE4 zorunlu.

## 7. BEP'ten Sapma Etkisi

| BEP'ten Sapma | Verim Kaybı | Ömür Etkisi | Not |
|---------------|-------------|-------------|-----|
| ±%10 | <%2 | İhmal edilebilir | Tercih edilen çalışma aralığı (POR) |
| ±%20 | %2-5 | Hafif | Kabul edilebilir işletme aralığı (AOR) |
| ±%30 | %5-12 | Orta | Rulman ve salmastra ömrü azalır |
| ±%40 | %12-25 | Ciddi | Kavitasyon riski, yüksek titreşim |
| ±%50+ | >%25 | Kritik | Erken arıza, ciddi mekanik hasar |

### 7.1 BEP Sapmasının Mekanik Etkileri

**BEP altında çalışma (düşük debi):**
- Radyal kuvvet artışı (salyangoz basınç dengesizliği)
- Emme resirkülasyonu (kavitasyon riski)
- Sıcaklık artışı (iç sürtünüm)
- Rulman ömrü kısalır (ekstra radyal yük)

**BEP üstünde çalışma (yüksek debi):**
- NPSHr artışı (kavitasyon riski)
- Şaft defleksiyonu artışı
- Salmastra/mekanik conta ömrü azalır
- Güç tüketimi artışı (motor aşırı yük riski)

## 8. Yaşa Göre Verim Düşüşü

### 8.1 Bakım Kalitesine Göre Detaylı Model

| Yaş | İyi Bakım | Ortalama Bakım | Kötü Bakım |
|-----|-----------|----------------|------------|
| 0-3 yıl | %0-2 | %0-3 | %0-5 |
| 3-5 yıl | %1-3 | %3-6 | %5-10 |
| 5-8 yıl | %2-5 | %5-10 | %10-18 |
| 8-12 yıl | %3-8 | %8-15 | %15-25 |
| 12-15 yıl | %5-10 | %12-20 | %20-35 |
| 15-20 yıl | %8-15 | %18-30 | %30-50 |
| >20 yıl | %12-20 | %25-40 | %40-60+ |

### 8.2 Bozulma Mekanizmaları (Pompa Tipine Göre)

**Santrifüj pompa:**
- İmpeller aşınması (verim düşüşü, basınç kaybı): Kademeli, sıvıyla değişir
- Aşınma halkaları (wear ring) açıklığı artışı: İç resirkülasyon artışı
- Mekanik conta aşınması: Kaçak artışı
- Rulman bozulması: Titreşim artışı, hizalama kaybı
- Gövde/karkas korozyonu: Akış yolu bozulması

**Dalgıç pompa:**
- İmpeller korozyonu/aşınması: Özellikle kumlu sularda hızlı
- Sızmalı motor sargısı: İzolasyon bozulması
- Kablo hasarı: Sıcaklık ve nem kaynakları
- Mil contası: Su girişi riski

**PD pompa (pistonlu):**
- Valf aşınması: Debi kaybı, verim düşüşü
- Piston/plunger salmastrası: Kaçak artışı
- Diyafram yorulması: Yırtılma riski
- Silindir aşınması: Uzun vadeli

### 8.3 Bakım Etkisi Tablosu

| Bakım Kalemi | İhmal Cezası | Önerilen Aralık |
|-------------|-------------|----------------|
| Aşınma halkası değişimi | +%2-8 enerji (iç kaçak artışı) | Boşluğun 2 katına ulaştığında |
| Mekanik conta bakımı | Kaçak, çevre riski | Kaçak görüldüğünde |
| Rulman değişimi | Titreşim, hizalama kaybı | Titreşim analizi ile veya 20,000-40,000 saat |
| İmpeller temizliği | %1-5 verim kaybı (kirlenme) | Yılda bir veya verim izlemeye göre |
| Salmastra sıkıştırma/değiştirme | Kaçak, güç kaybı | Kaçak kontrolü ile |
| Kaplin hizalama kontrolü | %1-3 enerji kaybı, titreşim | Yılda bir veya titreşim analizi ile |
| Yağ/gres değişimi | Rulman hasarı, ısı artışı | Üretici tavsiyesine göre |
| Emme filtresi temizliği | NPSHa düşmesi, kavitasyon riski | Basınç farkına göre |

### 8.4 Yenileme Kararı — Pratik Kurallar

- Yıllık verimsizlik enerji maliyeti > yeni pompa maliyetinin %20'si → değiştirmeyi değerlendir
- Bakım maliyeti > yenileme maliyetinin %50'si → değiştirmeyi değerlendir
- Yaş >15 yıl VE verim düşüşü >%15 → yenileme değerlendirmesi yap
- Aşınma halkası boşluğu fabrika değerinin 2 katını aştı → onarım veya değiştirme

## 9. Sektörel Karşılaştırma

### 9.1 Sektöre Göre Tipik Exergy Verimi

| Sektör | Tipik Exergy Verimi | Not |
|--------|---------------------|-----|
| Su/atıksu arıtma | %40-55 | Büyük pompalar, genelde iyi boyutlu |
| Petrokimya/rafineri | %45-60 | Mühendislik standartları yüksek, iyi bakım |
| Enerji santrali | %50-65 | Büyük pompalar, sürekli izleme |
| Gıda ve içecek | %35-50 | Hijyen öncelikli, değişken operasyon |
| Kimya | %40-55 | Proses değişkenliğine bağlı |
| Madencilik | %30-45 | Aşındırıcı sıvılar, zor koşullar |
| HVAC/bina | %25-40 | Genelde aşırı boyutlu, eski sistemler |
| Genel üretim | %35-50 | Karma |
| Tarım/sulama | %30-45 | Mevsimsel, değişken koşullar |

### 9.2 Sektöre Göre Tipik Wire-to-Water Verimi

| Sektör | Tipik W2W Verimi | Açıklama |
|--------|-----------------|----------|
| Büyük su iletim (>500 kW) | %65-80 | Büyük pompalar, sabit debi, iyi optimize |
| Atıksu terfi (100-500 kW) | %55-70 | Orta-büyük, değişken debi |
| Endüstriyel proses (50-500 kW) | %50-65 | Boyutlandırma ve kontrol kalitesine bağlı |
| HVAC sirkülasyon (5-50 kW) | %35-55 | Genelde aşırı boyutlu |
| Küçük endüstriyel (<15 kW) | %30-50 | Boyut ve bakım kalitesine bağlı |

### 9.3 Tipik Tasarruf Potansiyeli (Sektöre Göre)

| Sektör | Tipik Tasarruf | Ana Fırsatlar |
|--------|---------------|---------------|
| Su/atıksu | %15-30 | VSD, boyut optimizasyonu, pompa yenileme |
| Endüstriyel proses | %20-40 | Throttle eliminasyonu, VSD, sistem optimizasyonu |
| HVAC | %30-50 | VSD, aşırı boyut düzeltme, kontrol iyileştirme |
| Tarım/sulama | %15-25 | Pompa yenileme, boru optimizasyonu |

## 10. Referanslar

- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- Hydraulic Institute, "Pump Life Cycle Costs: A Guide to LCC Analysis for Pumping Systems" (HI/Europump)
- Hydraulic Institute, "Optimizing Pumping Systems" (ANSI/HI)
- Europump & Hydraulic Institute, "Pump Life Cycle Costs" Guide
- ISO/ASME 14414:2019, "Pump System Energy Assessment"
- ISO 9906:2012, "Rotodynamic Pumps — Hydraulic Performance Acceptance Tests"
- IEC 60034-30-1:2014, "Rotating Electrical Machines — Efficiency Classification"
- Europump, "Variable Speed Pumping: A Guide to Successful Applications"
- Grundfos, "Pump Handbook"
- KSB, "Selecting Centrifugal Pumps" Technical Documentation
- Saidur et al. (2010), "A review on exergy analysis of industrial sector," Renewable & Sustainable Energy Reviews
