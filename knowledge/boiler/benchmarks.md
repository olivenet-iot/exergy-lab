---
title: "Kazan Benchmark Verileri"
category: reference
equipment_type: boiler
keywords: [benchmark, kazan, verimlilik, kayıp]
related_files: [boiler/formulas.md, boiler/audit.md, boiler/solutions/economizer.md]
use_when: ["Kazan performansı değerlendirilirken", "Verimlilik karşılaştırması yapılırken"]
priority: high
last_updated: 2026-01-31
---
# Kazan Benchmark Verileri

> Son güncelleme: 2026-01-31

## 1. Exergy Verimi Aralıkları

| Kazan Tipi | Düşük | Ortalama | İyi | Best-in-class |
|------------|-------|----------|-----|---------------|
| Ateş borulu (doğalgaz) | <30% | 30-38% | 38-45% | >45% |
| Su borulu (doğalgaz) | <28% | 28-36% | 36-43% | >43% |
| Sıcak su kazanı | <25% | 25-33% | 33-40% | >40% |
| Yoğuşmalı kazan | <35% | 35-43% | 43-50% | >50% |
| Atık ısı kazanı (HRSG) | <35% | 35-45% | 45-55% | >55% |
| Elektrikli kazan | <10% | 10-15% | - | - |
| Kömür yakıtlı kazan | <22% | 22-30% | 30-38% | >38% |
| Biyokütle kazanı | <20% | 20-28% | 28-35% | >35% |
| Akışkan yataklı kazan | <25% | 25-33% | 33-40% | >40% |

Not: Elektrikli kazanın exergy verimi düşüktür çünkü elektrik saf exerjidir (iş potansiyeli %100).
Elektriğin ısıya dönüştürülmesi termodinamiğin 2. yasasına göre büyük exergy yıkımına neden olur.
Carnot faktörü (1 - T₀/T) nedeniyle düşük sıcaklıklı ısının exergy içeriği zaten düşüktür.

Exergy verimi hesaplama:

```
η_ex = (ṁ_buhar × ex_buhar - ṁ_besleme × ex_besleme) / (ṁ_yakıt × ex_yakıt)
```

Burada exergy içeriği:
- Doğalgaz exergy/enerji oranı ≈ 1.04
- Kömür exergy/enerji oranı ≈ 1.06-1.10
- Fuel oil exergy/enerji oranı ≈ 1.06
- Biyokütle exergy/enerji oranı ≈ 1.05-1.15

## 2. Enerji Verimi (Termal Verim) Aralıkları

### 2.1 Yanma Verimi

| Durum | Yanma Verimi | Açıklama |
|-------|-------------|----------|
| Mükemmel | >92% | Optimal brülör ayarı, düşük CO, düşük is |
| İyi | 88-92% | Standart performans |
| Ortalama | 82-88% | İyileştirme potansiyeli var |
| Kötü | <82% | Brülör bakımı/ayarı gerekli |

Yanma verimini etkileyen faktörler:
- Fazla hava oranı (en önemli faktör)
- Yakıt-hava karışım kalitesi
- Brülör tipi ve bakım durumu
- Yanma odası geometrisi ve sıcaklığı
- Atomizasyon kalitesi (sıvı yakıtlarda)

### 2.2 Toplam Termal Verim (LHV Bazlı)

| Kazan Tipi | Kötü | Ortalama | İyi | Mükemmel |
|------------|------|----------|-----|----------|
| Ateş borulu (doğalgaz) | <82% | 82-88% | 88-92% | >92% |
| Su borulu (doğalgaz) | <80% | 80-86% | 86-90% | >90% |
| Sıcak su kazanı (doğalgaz) | <84% | 84-89% | 89-93% | >93% |
| Yoğuşmalı kazan (doğalgaz) | <90% | 90-96% | 96-102% | >102%* |
| Kömür yakıtlı kazan | <78% | 78-84% | 84-88% | >88% |
| Fuel oil kazan | <80% | 80-86% | 86-90% | >90% |
| Biyokütle kazanı | <72% | 72-80% | 80-86% | >86% |
| Akışkan yataklı kazan | <82% | 82-87% | 87-91% | >91% |
| Atık ısı kazanı (HRSG) | <70% | 70-78% | 78-85% | >85% |

*Yoğuşmalı kazanlarda LHV bazlı verim %100'ü geçebilir çünkü referans alt ısıl değerdir ve
baca gazındaki su buharının yoğuşma ısısı da geri kazanılır.

### 2.3 HHV vs LHV Farkı

| Yakıt | HHV/LHV Oranı | Fark | Açıklama |
|-------|---------------|------|----------|
| Doğalgaz | ~1.11 | ~%10 | H/C oranı yüksek, fark büyük |
| Fuel Oil (No.6) | ~1.06 | ~%5-6 | Daha az hidrojen |
| Fuel Oil (No.2/Motorin) | ~1.07 | ~%6-7 | Orta düzey |
| Linyit | ~1.02-1.05 | ~%2-5 | Nem içeriğine bağlı |
| Taşkömürü | ~1.03-1.05 | ~%3-5 | Uçucu madde oranına bağlı |
| Biyokütle (kuru) | ~1.05-1.08 | ~%5-8 | Nem oranına çok bağlı |
| LPG | ~1.09 | ~%8-9 | Propan/bütan karışımı |

Dönüşüm formülleri:
```
η_HHV = η_LHV × (LHV / HHV)
η_LHV = η_HHV × (HHV / LHV)
```
Örnek (doğalgaz): η_LHV = %92 → η_HHV = 92 × (1/1.11) ≈ %82.9

## 3. Baca Gazı Kayıpları

### 3.1 Baca Gazı Sıcaklığı Benchmarkları

| Durum | Baca Gazı Sıcaklığı | Tahmini Kuru Baca Gazı Kaybı | Aksiyon |
|-------|---------------------|------------------------------|---------|
| Best practice | <120°C | <%5 | Ekonomizer + yoğuşma ön ısıtma |
| İyi | 120-180°C | %5-8 | Ekonomizer mevcut |
| Ortalama | 180-250°C | %8-13 | Ekonomizer eklenebilir |
| Kötü | 250-350°C | %13-19 | Ciddi enerji kaybı |
| Kritik | >350°C | >%19 | Acil müdahale gerekli |

Her 20°C baca gazı sıcaklık düşüşü ≈ %1 verim artışı sağlar (genel kural).

### 3.2 Kayıp Dağılımı

| Kayıp Türü | İyi | Ortalama | Kötü | Açıklama |
|------------|-----|----------|------|----------|
| Kuru baca gazı kaybı | <%8 | %8-12 | >%12 | En büyük kayıp kalemi |
| Islak baca gazı kaybı (nem) | <%4 | %4-8 | >%8 | Yakıttaki H₂ yanmasından |
| Radyasyon ve konveksiyon kaybı | <%1 | %1-2 | >%2 | Kazan yüzeyinden |
| Blowdown kaybı | <%1 | %1-3 | >%3 | Su kalitesine bağlı |
| Yanmamış yakıt kaybı (CO) | <%0.5 | %0.5-1 | >%1 | Eksik yanma |
| Yanmamış katı yakıt kaybı | <%1 | %1-3 | >%3 | Sadece katı yakıt kazanları |
| Dış yüzey sıcaklık kaybı | <%0.5 | %0.5-1.5 | >%1.5 | İzolasyon durumuna bağlı |

### 3.3 Kayıp Azaltma Potansiyeli

| Önlem | Tipik Tasarruf | Yatırım Geri Dönüş |
|-------|---------------|---------------------|
| Ekonomizer (baca gazı → besleme suyu) | %3-5 | 1-2 yıl |
| Hava ön ısıtıcı (baca gazı → yanma havası) | %2-4 | 1-3 yıl |
| Yoğuşma ısı geri kazanımı | %5-10 | 2-4 yıl |
| O₂ trim kontrol (otomatik fazla hava) | %1-3 | <1 yıl |
| Brülör yenileme/bakım | %1-3 | <1 yıl |
| Blowdown ısı geri kazanımı | %0.5-2 | 1-2 yıl |

## 4. Fazla Hava (Excess Air) Benchmarkları

### 4.1 Yakıt Tipine Göre Optimum Değerler

| Yakıt Tipi | Optimum O₂ (%) | Optimum CO₂ (%) | Optimum Fazla Hava (%) | Not |
|-----------|----------------|-----------------|----------------------|-----|
| Doğalgaz | 2.0-3.0 | 10.0-11.5 | 10-15 | En düşük fazla hava |
| LPG | 2.0-3.5 | 11.0-12.5 | 10-18 | Doğalgaza yakın |
| Fuel oil (No.2) | 3.0-4.0 | 12.0-13.5 | 15-20 | Atomizasyon gerekli |
| Fuel oil (No.6) | 3.5-4.5 | 12.5-14.0 | 18-25 | Ağır yakıt, ön ısıtma gerekli |
| Linyit | 4.0-6.0 | 13.0-15.0 | 25-35 | Yüksek nem, düşük kalori |
| Taşkömürü | 4.0-5.5 | 14.0-16.0 | 20-30 | Uçucu maddeye bağlı |
| Biyokütle (odun) | 5.0-8.0 | 10.0-14.0 | 30-50 | Heterojen yakıt |
| Biyokütle (pelet) | 4.0-6.0 | 12.0-15.0 | 25-35 | Homojen, daha kontrollü |
| Atık (RDF) | 6.0-10.0 | Değişken | 40-80 | Çok heterojen yakıt |

### 4.2 Fazla Hava Etkisi

| O₂ (%) | Fazla Hava (%) | Yaklaşık Verim Kaybı (bazdan) | Durum |
|---------|---------------|-------------------------------|-------|
| 2.0 | ~10 | Baz (%0) | Optimal (doğalgaz) |
| 3.0 | ~15 | ~%0.5 | Kabul edilebilir |
| 4.0 | ~22 | ~%1.0 | Üst sınır |
| 5.0 | ~30 | ~%1.5 | Fazla hava yüksek |
| 6.0 | ~38 | ~%2.2 | İyileştirme gerekli |
| 8.0 | ~58 | ~%3.5 | Ciddi israf |
| 10.0 | ~82 | ~%5.0 | Acil müdahale |

Not: O₂ < %1.5 olduğunda CO oluşumu hızla artar; güvenli aralıkta kalınmalıdır.
İdeal yaklaşım: O₂ trim sistemi ile sürekli otomatik kontrol.

### 4.3 Brülör Tipi ve Fazla Hava İlişkisi

| Brülör Tipi | Minimum Elde Edilebilir O₂ | Modülasyon Aralığı | Not |
|------------|--------------------------|-------------------|-----|
| On/Off | %4-6 | Yok | Düşük basınçlarda O₂ yükselir |
| High/Low/Off | %3-5 | 2 kademe | Basit kontrol |
| Tam modülasyonlu | %2-4 | 4:1 - 5:1 | Standart endüstriyel |
| Tam modülasyonlu + O₂ trim | %2-3 | 5:1 - 10:1 | Best practice |
| Premix (ön karışımlı) | %1.5-2.5 | 5:1 - 8:1 | Düşük emisyon |
| Flameless (FLOX) | %2-3 | 3:1 - 5:1 | Ultra düşük NOx |

## 5. Spesifik Yakıt Tüketimi

### 5.1 Doğalgaz — m³/ton Buhar (Doymuş)

| Buhar Basıncı (bar) | Buhar Sıcaklığı (°C) | İyi (m³/ton) | Ortalama (m³/ton) | Kötü (m³/ton) | Not |
|---------------------|----------------------|-------------|-------------------|---------------|-----|
| 5 | 152 | 72-76 | 76-84 | >84 | Düşük basınç |
| 7 | 165 | 74-78 | 78-86 | >86 | Yaygın basınç |
| 10 | 180 | 76-81 | 81-89 | >89 | Orta basınç |
| 15 | 198 | 79-84 | 84-93 | >93 | Yüksek basınç |
| 20 | 212 | 81-86 | 86-96 | >96 | Çok yüksek basınç |
| 25 | 224 | 83-89 | 89-99 | >99 | Endüstriyel |

Varsayımlar: Besleme suyu sıcaklığı 80°C, doğalgaz alt ısıl değeri 34.5 MJ/m³,
kazan verimi %88-92 (iyi), %80-88 (ortalama), <%80 (kötü).

### 5.2 Fuel Oil (No.6) — kg/ton Buhar (Doymuş)

| Buhar Basıncı (bar) | İyi (kg/ton) | Ortalama (kg/ton) | Kötü (kg/ton) | Not |
|---------------------|-------------|-------------------|---------------|-----|
| 5 | 64-68 | 68-76 | >76 | Düşük basınç |
| 7 | 66-70 | 70-78 | >78 | Yaygın basınç |
| 10 | 68-73 | 73-81 | >81 | Orta basınç |
| 15 | 71-76 | 76-85 | >85 | Yüksek basınç |
| 20 | 73-78 | 78-88 | >88 | Çok yüksek basınç |

Varsayım: Fuel oil No.6 alt ısıl değeri ≈ 39.5 MJ/kg.

### 5.3 Basınca Göre Buhar Entalpisi ve Düzeltme

| Basınç (bar) | Doymuş Buhar Sıcaklığı (°C) | Buhar Entalpisi hg (kJ/kg) | Sıvı Entalpisi hf (kJ/kg) | Buharlaşma Isısı hfg (kJ/kg) |
|-------------|------------------------------|---------------------------|--------------------------|------------------------------|
| 1.013 | 100 | 2,676 | 419 | 2,257 |
| 3 | 134 | 2,725 | 561 | 2,164 |
| 5 | 152 | 2,749 | 640 | 2,109 |
| 7 | 165 | 2,763 | 697 | 2,066 |
| 10 | 180 | 2,778 | 763 | 2,015 |
| 15 | 198 | 2,792 | 845 | 1,947 |
| 20 | 212 | 2,800 | 909 | 1,891 |
| 25 | 224 | 2,803 | 962 | 1,841 |
| 30 | 234 | 2,804 | 1,008 | 1,796 |
| 40 | 250 | 2,801 | 1,087 | 1,714 |

Basınç arttıkça buharlaşma ısısı azalır ancak buhar sıcaklığı artar.
Yüksek basınçta daha fazla yakıt tüketimi beklenir (besleme suyu sıcaklığı sabit iken).

### 5.4 Kızdırma (Superheat) Etkisi

| Kızdırma Derecesi (°C) | Ek Yakıt Tüketimi (%) | Tipik Uygulama |
|------------------------|----------------------|----------------|
| 0 (doymuş) | Baz | Proses buharı |
| 20-50 | +%1-2 | Hat kayıplarını kompanze |
| 50-100 | +%2-4 | Türbin girişi (küçük) |
| 100-200 | +%4-8 | Türbin girişi (orta) |
| 200-350 | +%8-14 | Güç santrali türbinleri |

## 6. Kondensat Geri Dönüş Oranı

| Durum | Geri Dönüş Oranı | Yakıt Tasarrufu | Not |
|-------|-------------------|----------------|-----|
| Best practice | >90% | %10-15 | Kapalı devre, yüksek sıcaklık geri dönüşü |
| İyi | 70-90% | %7-10 | Çoğu kondensat toplanıyor |
| Ortalama | 50-70% | %4-7 | Kısmi toplama |
| Kötü | 30-50% | %2-4 | Çok sayıda açık deşarj |
| Kritik | <30% | <%2 | Hemen hemen tüm kondensat kaybediliyor |

### 6.1 Kondensat Geri Dönüşünün Ekonomik Etkisi

Her %10 kondensat geri dönüş artışı yaklaşık:
- %1-1.5 yakıt tasarrufu
- %1-2 su tasarrufu
- %0.5-1 kimyasal tasarrufu (su arıtma)
- Azalan blowdown gereksinimi

### 6.2 Kondensat Sıcaklığına Göre Enerji Tasarrufu

| Kondensat Sıcaklığı (°C) | Geri Kazanılan Enerji (kJ/kg) | Tasarruf (%) |
|--------------------------|------------------------------|-------------|
| 60 | 251 | ~%4 |
| 70 | 293 | ~%5 |
| 80 | 335 | ~%6 |
| 90 | 377 | ~%6.5 |
| 95 | 398 | ~%7 |

Referans: Besleme suyu sıcaklığı 25°C, 10 bar doymuş buhar üretimi.

## 7. Buhar Kapanı (Steam Trap) Arıza Oranı

### 7.1 Sistem Durumu Sınıflandırması

| Sistem Durumu | Arıza Oranı | Aksiyon |
|-------------|-------------|---------|
| Mükemmel | <%5 | Koruyucu bakım programı devam |
| İyi | %5-10 | Yıllık test ve bakım yeterli |
| Kabul edilebilir | %10-20 | 6 ayda bir test, onarım planı |
| Kötü | %20-30 | Acil kapsamlı test ve onarım |
| Kritik | >%30 | Tüm kapanların değişimi değerlendirilmeli |

### 7.2 Arızalı Kapandan Buhar Kaybı

| Kapan Orifis Çapı (mm) | Basınç (bar) | Buhar Kaybı (kg/h) | Yıllık Enerji Kaybı (GJ) | Yıllık Maliyet* |
|------------------------|-------------|--------------------|--------------------------|--------------------|
| 3 | 7 | ~8 | ~140 | ~€1,700 |
| 5 | 7 | ~22 | ~390 | ~€4,700 |
| 8 | 7 | ~56 | ~980 | ~€11,800 |
| 10 | 7 | ~88 | ~1,540 | ~€18,500 |
| 3 | 10 | ~11 | ~200 | ~€2,400 |
| 5 | 10 | ~32 | ~560 | ~€6,700 |
| 8 | 10 | ~80 | ~1,400 | ~€16,800 |
| 10 | 10 | ~125 | ~2,190 | ~€26,300 |

*Varsayım: 8,000 saat/yıl, doğalgaz maliyeti €0.035/kWh, kazan verimi %88.

### 7.3 Kapan Tipi ve Beklenen Ömür

| Kapan Tipi | Beklenen Ömür (yıl) | Tipik Arıza Modu | Not |
|-----------|--------------------|--------------------|-----|
| Termodinamik (disk) | 3-5 | Açık kalma (buhar kaçırma) | Ucuz, yaygın |
| Termostatic (bimetal) | 5-8 | Kapalı kalma (kondensat birikimi) | Orta fiyat |
| Mekanik (şamandıralı) | 8-12 | Açık/kapalı kalma | Güvenilir, endüstriyel |
| Inverted bucket | 5-10 | Açık kalma | Ağır hizmet |

## 8. İzolasyon Durumu

### 8.1 Yüzey Sıcaklığı Benchmarkları

| Durum | Yüzey Sıcaklığı | Not |
|-------|-----------------|-----|
| İyi izolasyon | <50°C | Standart, güvenli temas |
| Kabul edilebilir | 50-70°C | Hafif iyileştirme gerekli |
| Kötü izolasyon | 70-120°C | Yalıtım yenileme gerekli |
| İzolasyonsuz | >120°C | Ciddi enerji kaybı + güvenlik riski |

İş güvenliği sınırı: Temas edilebilir yüzeylerde maksimum 60°C (EN 563).

### 8.2 İzolasyonsuz Yüzeylerden Isı Kaybı

| Boru Çapı (DN) | Buhar Sıcaklığı 150°C | Buhar Sıcaklığı 200°C | Buhar Sıcaklığı 250°C | Birim |
|----------------|----------------------|----------------------|----------------------|-------|
| DN25 | 95 | 145 | 200 | W/m |
| DN50 | 155 | 240 | 330 | W/m |
| DN100 | 270 | 415 | 575 | W/m |
| DN150 | 370 | 575 | 790 | W/m |
| DN200 | 470 | 730 | 1,005 | W/m |
| DN300 | 660 | 1,020 | 1,410 | W/m |

### 8.3 İzolasyon Kalınlığı ve Tasarruf

| İzolasyon Kalınlığı (mm) | Isı Kaybı Azalması | Tipik Uygulama |
|--------------------------|-------------------|----------------|
| 25 | %80-85 | İç mekan, düşük sıcaklık |
| 40 | %87-90 | Standart endüstriyel |
| 50 | %90-93 | Orta-yüksek sıcaklık |
| 75 | %93-95 | Yüksek sıcaklık hatları |
| 100 | %95-97 | Çok yüksek sıcaklık, uzun hatlar |

Not: Ekonomik izolasyon kalınlığı, enerji maliyeti ve yalıtım maliyetinin dengelenmesiyle belirlenir.
Genellikle 40-75 mm aralığı endüstriyel uygulamalar için optimaldir.

### 8.4 Yaygın İzolasyonsuz Noktalar

| Nokta | Tipik Kayıp | Çözüm |
|-------|------------|-------|
| Flanş bağlantıları | 5-10 × düz boru kaybı | Sökülebilir izolasyon ceketleri |
| Vana gövdeleri | 5-15 × düz boru kaybı | Sökülebilir izolasyon ceketleri |
| Buhar kapanları | Her biri 50-200 W | Kapan ceketleri |
| Genleşme kompansatörleri | Flanş ile benzer | Esnek izolasyon |
| Manometre/enstrüman bağlantıları | Her biri 20-80 W | İzolasyon kapakları |

## 9. Yaşa Göre Verimlilik Degradasyonu

### 9.1 Bakım Kalitesine Göre Model

| Kazan Yaşı | İyi Bakım | Ortalama Bakım | Kötü Bakım |
|-----------|-----------|----------------|------------|
| 0-3 yıl | %0 | %0-1 | %0-2 |
| 3-5 yıl | %0-1 | %1-2 | %2-4 |
| 5-10 yıl | %1-2 | %2-4 | %4-8 |
| 10-15 yıl | %2-3 | %4-6 | %8-12 |
| 15-20 yıl | %3-5 | %6-10 | %12-18 |
| 20-30 yıl | %5-8 | %10-15 | %18-25 |
| >30 yıl | %8-12 | %15-22 | %25-35 |

### 9.2 Bozulma Mekanizmaları

**Isı transfer yüzeylerinde kirlenme (fouling):**
- Baca gazı tarafı: Kurum, kül birikimi → ısı transferi azalır
- Her 1 mm kurum birikimi baca gazı sıcaklığını ~60-70°C artırır
- Her 1 mm kireç birikimi (su tarafı) ~%2-3 verim kaybına neden olur
- Temizlik periyodu: 6-12 ayda bir (koşullara bağlı)

**Kireçlenme (scaling):**
- Su tarafında CaCO₃, CaSO₄, SiO₂ birikimi
- Termal iletkenliği düşürür (kireç: ~1 W/m·K vs çelik: ~50 W/m·K)
- Yerel aşırı ısınma ve tüp hasarı riski
- Su arıtma programı ile önlenebilir

**Refrakter (ateş tuğlası) bozulması:**
- Yanma odası refrakter aşınması/çatlaması
- Artan radyasyon kaybı
- Flame impingement hasarı
- Ömrü: Tipik 5-15 yıl (koşullara bağlı)

**Brülör aşınması:**
- Nozzle erozyonu (özellikle fuel oil)
- Flame shape bozulması → düzensiz yanma
- Ignition elektrot aşınması
- Bakım aralığı: Yılda 1-2 kez kontrol

**Korozyon:**
- Baca gazı tarafı: Düşük sıcaklık korozyonu (asit çiğlenme noktası altı)
- Su tarafı: Oksijen korozyonu (deaerator arızası)
- Dış korozyon: Yalıtım altı korozyon (CUI)

## 10. Sektörel Karşılaştırma

### 10.1 Sektöre Göre Tipik Verimler

| Sektör | Tipik Enerji Verimi | Tipik Exergy Verimi | Not |
|--------|---------------------|---------------------|-----|
| Gıda ve içecek | %82-88 | %28-36 | Düşük basınç buhar, temizlik yükleri |
| Tekstil | %80-87 | %26-34 | Boyahane buhar yükü yüksek |
| Kimya | %84-90 | %32-40 | Yüksek basınç, iyi bakım |
| Kağıt ve selüloz | %82-88 | %30-38 | Yüksek buhar tüketimi, kojenerasyon |
| İlaç | %84-90 | %30-38 | Temiz buhar gereksinimi |
| Otomotiv | %83-89 | %30-37 | Boyahane, ısıtma |
| Petrokimya | %85-92 | %35-43 | Proses entegrasyonu, atık ısı |
| Hastane | %78-85 | %25-33 | Düşük yük faktörü, on/off çalışma |
| Otel/AVM | %80-86 | %24-32 | Mevsimsel yük değişimi |
| Seramik/cam | %75-83 | %28-36 | Yüksek sıcaklık, katı yakıt |

### 10.2 Sektöre Göre Tipik Buhar Tüketimi

| Sektör | Spesifik Buhar Tüketimi | Birim | Not |
|--------|-------------------------|-------|-----|
| Gıda (süt) | 0.3-0.8 | ton buhar / ton ürün | Pastörizasyon, sterilizasyon |
| Gıda (bira) | 0.15-0.30 | ton buhar / m³ bira | Kaynatma, sterilizasyon |
| Tekstil (boyama) | 2-5 | ton buhar / ton kumaş | Proses sıcaklığına bağlı |
| Kağıt | 1.5-3.0 | ton buhar / ton kağıt | Kurutma yoğun |
| Şeker | 0.4-0.6 | ton buhar / ton pancar | Evaporasyon, kristalizasyon |
| Kimya (genel) | Değişken | - | Prosese özel |
| Lastik | 1.0-2.0 | ton buhar / ton ürün | Vulkanizasyon |
| İlaç | 0.5-2.0 | ton buhar / ton ürün | Prosese çok bağlı |

## 11. Blowdown Oranı Benchmarkları

### 11.1 Su Kalitesine Göre Blowdown Oranı

| Su Kalitesi / Arıtma | Blowdown Oranı | Not |
|----------------------|----------------|-----|
| RO + yumuşatma | <%2 | Best practice |
| İyi yumuşatma (0-5 ppm sertlik) | %2-4 | Standart endüstriyel |
| Ortalama yumuşatma (5-15 ppm) | %4-6 | İyileştirme potansiyeli |
| Zayıf arıtma (>15 ppm sertlik) | %6-10 | Yüksek kimyasal tüketimi |
| Arıtmasız ham su | >%10 | Ciddi kireçlenme riski |

### 11.2 Blowdown Kaybı Hesabı

| Blowdown Oranı | Enerji Kaybı (% yakıt tüketiminden) | Not |
|----------------|-------------------------------------|-----|
| %1 | ~%0.3-0.5 | Minimal kayıp |
| %3 | ~%1.0-1.5 | Kabul edilebilir |
| %5 | ~%1.7-2.5 | Isı geri kazanımı değerlendir |
| %8 | ~%2.8-4.0 | Isı geri kazanımı gerekli |
| %10 | ~%3.5-5.0 | Su arıtma iyileştirmesi acil |

### 11.3 Blowdown Isı Geri Kazanımı

| Yöntem | Geri Kazanım Oranı | Yatırım | Not |
|--------|--------------------|---------|----|
| Flash buhar tankı | %30-50 | Düşük | Flash buharı deaeratöre |
| Isı eşanjörü (blowdown → besleme suyu) | %40-60 | Orta | Sıcaklık yükseltme |
| Flash tank + ısı eşanjörü (kombinasyon) | %60-80 | Orta-yüksek | Best practice |
| Sürekli blowdown kontrolü (TDS sensörü) | %20-40 tasarruf | Düşük-orta | Gereksiz blowdown'u önler |

## 12. Kazan Yük Faktörü ve Verimlilik

### 12.1 Yük-Verim İlişkisi

| Yük Faktörü (%) | Verim Değişimi | Durum | Not |
|-----------------|----------------|-------|-----|
| <20% | -%5 ile -%12 | Çok düşük yük | On/off çalışma, yüksek kayıp |
| 20-30% | -%3 ile -%8 | Düşük yük | Sık çevrim, radyasyon kaybı yüksek |
| 30-50% | -%1 ile -%4 | Orta-düşük yük | Modülasyon başlar |
| 50-80% | %0 ile +%1 | Optimal aralık | En yüksek verim bölgesi |
| 80-100% | %0 ile -%1 | Tam yüke yakın | Fazla hava artabilir |
| >100% (aşırı yük) | -%2 ile -%5 | Aşırı yükleme | Güvenlik riski, kaçınılmalı |

Optimal çalışma aralığı: %50-80 nominal kapasite.

### 12.2 On/Off Çalışma Kayıpları

| Çevrim Sıklığı | Ek Kayıp | Açıklama |
|----------------|----------|----------|
| <2 çevrim/saat | <%1 | Kabul edilebilir |
| 2-4 çevrim/saat | %1-3 | Ön/son havalandırma kayıpları |
| 4-8 çevrim/saat | %3-6 | Ciddi verim kaybı |
| >8 çevrim/saat | >%6 | Kazan kapasitesi aşırı büyük |

Her başlatma/durdurmada ön havalandırma (pre-purge) ile kazan gövdesinden
sıcak hava atılır; bu enerji doğrudan kayıptır. Modülasyonlu brülör çevrim sayısını azaltır.

### 12.3 Çoklu Kazan Yönetimi

| Strateji | Açıklama | Tasarruf Potansiyeli |
|----------|----------|---------------------|
| Sıralı çalıştırma (sequencing) | Toplam yüke göre kazan sayısı optimizasyonu | %5-10 |
| Yük dengeleme (load balancing) | Her kazanı optimal aralıkta çalıştırma | %3-7 |
| Tepe yük kazanı ayrımı | Baz yük + tepe yük kazan ayrımı | %5-12 |
| Küçük kazan ekleme | Düşük yük dönemlerinde küçük kazan devreye alma | %5-15 |
| Otomasyon (BMS) | Tüm stratejilerin otomasyonu | %8-18 |

## 13. Ekonomizer Performans Benchmarkları

### 13.1 Ekonomizer Tip ve Performans

| Ekonomizer Tipi | Baca Gazı ΔT | Besleme Suyu ΔT | Verim Artışı | Not |
|----------------|-------------|-----------------|-------------|-----|
| Çelik borulu (standart) | 50-80°C | 20-40°C | %3-5 | Yaygın, asit çiğlenme üstü |
| Paslanmaz çelik | 80-120°C | 30-60°C | %5-8 | Asit korozyonuna dayanıklı |
| Yoğuşmalı (condensing) | 100-160°C | 40-80°C | %8-12 | Düşük dönüş suyu sıcaklığı gerekli |
| Cam borulu | 80-130°C | 30-55°C | %5-9 | Korozyona dayanıklı |

### 13.2 Ekonomizer Verimlilik Kontrol

| Parametre | Hedef | Alarm | Açıklama |
|----------|-------|-------|----------|
| Yaklaşım sıcaklığı (approach) | <30°C | >50°C | Baca gazı çıkış - su giriş farkı |
| Baca gazı ΔP | <5 mbar | >10 mbar | Kirlenme göstergesi |
| Su tarafı ΔP | <0.5 bar | >1.0 bar | Kireçlenme göstergesi |

## Referanslar

- DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition
- ASME PTC 4, "Fired Steam Generators — Performance Test Codes"
- Spirax Sarco, "The Steam and Condensate Loop" (Design of Fluid Systems)
- Carbon Trust, "Steam and High Temperature Hot Water Boilers" (CTG060)
- CIBO (Council of Industrial Boiler Owners), "Energy Efficiency Handbook"
- EN 12952, "Water-tube Boilers and Auxiliary Installations"
- EN 12953, "Shell Boilers"
- ASME Boiler and Pressure Vessel Code (BPVC)
- Beér, J.M., "Combustion Technology Developments in Power Generation"
- Ganapathy, V., "Steam Generators and Waste Heat Boilers"
- Turkish Energy Efficiency Law (No. 5627) and related regulations
- TÜBİTAK MAM Enerji Enstitüsü yayınları
