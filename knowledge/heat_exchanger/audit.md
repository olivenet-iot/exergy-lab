---
title: "Isı Eşanjörü Enerji Denetimi Metodolojisi — Heat Exchanger Energy Audit"
category: reference
equipment_type: heat_exchanger
keywords: [enerji denetimi, ısı eşanjörü, performans testi, fouling, U-değer izleme]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/standards.md]
use_when: ["Isı eşanjörü enerji denetimi planlanırken", "Performans testi yapılırken", "Kirlenme değerlendirmesi gerektiğinde"]
priority: medium
last_updated: 2026-02-01
---
# Isı Eşanjörü Enerji Denetimi Metodolojisi — Heat Exchanger Energy Audit

> Son güncelleme: 2026-02-01

## Genel Bakış

Bu metodoloji, ASME PTC 12.5 "Single Phase Heat Exchangers" ve ilgili endüstriyel
standartlara dayalı olarak ısı eşanjörlerinin performans değerlendirmesi için
kapsamlı bir süreç tanımlar. Isı eşanjörleri endüstriyel tesislerdeki toplam
ısı transfer işlemlerinin büyük çoğunluğunu oluşturur ve verimlilik iyileştirmeleri
için önemli fırsatlar sunar.

## Standart Referanslar

| Standart | Açıklama |
|----------|----------|
| ASME PTC 12.5 | Single Phase Heat Exchangers — Performans test kodu |
| ASME PTC 19.1 | Test Uncertainty — Ölçüm belirsizliği |
| TEMA Standards | Tubular Exchanger Manufacturers Association — Tasarım standartları |
| API 660 | Shell-and-Tube Heat Exchangers — Gövde-boru eşanjör standardı |
| ISO 50001:2018 | Energy management systems — Enerji yönetim sistemleri |
| ISO 50002:2014 | Energy audits — Requirements with guidance for use |
| BS EN 1434 | Heat meters — Isı sayaçları |
| AHRI 400 | Liquid-to-Liquid Heat Exchangers — Performans standardı |

### Değerlendirme Seviyeleri

| Seviye | Açıklama | Kapsam |
|--------|----------|--------|
| Seviye 1 | Yürüyerek inceleme (walk-through) | Görsel kontrol, fatura analizi, genel durum tespiti |
| Seviye 2 | Detaylı değerlendirme | Ölçümler, U-değer hesabı, temizlik faktörü, kayıp analizi |
| Seviye 3 | Kapsamlı değerlendirme | Tam enstrümantasyon, exergy analizi, uzun süreli izleme, termoekonomik analiz |

## Adım 1: Ön Hazırlık (Pre-Audit)

### 1.1 Toplanacak Bilgiler

| Kategori | Detay |
|----------|-------|
| Tasarım verileri | Data sheet, mekanik çizimler, TEMA designation, U_tasarım |
| İşletme kayıtları | Sıcaklık, debi, basınç trend verileri (en az 12 ay) |
| Bakım geçmişi | Temizlik kayıtları, conta değişimleri, boru tapa işlemleri |
| Proses koşulları | Akışkan özellikleri, çalışma koşulları, mevsimsel değişimler |
| Enerji verileri | Pompa güç tüketimleri, yardımcı ekipman enerji kullanımı |

### 1.2 Ekipman Envanteri

Her eşanjör için aşağıdaki bilgiler derlenmeli:

```
Eşanjör Kimliği:
- Ekipman numarası / TAG
- Eşanjör tipi (gövde-boru, plakalı, spiral, vb.)
- TEMA tipi (AES, BEM, CFU, vb.) — gövde-boru için
- Yüzey alanı [m2]
- Boru malzemesi, çapı, uzunluğu
- Gövde çapı
- Geçiş sayısı (boru tarafı / gövde tarafı)
- Tasarım U değeri [W/(m2·K)]
- Tasarım ısı yükü [kW]
- Devreye alma tarihi
```

### 1.3 Gerekli Ölçüm Ekipmanları

| Ekipman | Doğruluk | Kullanım |
|---------|----------|----------|
| Sıcaklık sensörü (RTD/PT100) | ± 0.1°C | Giriş/çıkış sıcaklıkları |
| Ultrasonik debimetre | ± %1-2 | Akışkan debileri (tutarsız) |
| Elektromanyetik debimetre | ± %0.5 | İletken sıvılar (kalıcı) |
| Diferansiyel basınç transmiteri | ± %0.1 FS | Basınç düşüşü |
| Basınç transmiteri | ± %0.25 FS | Mutlak/göreceli basınç |
| Termal kamera (IR) | ± 2°C | Yüzey sıcaklığı, izolasyon |
| Titreşim analizörü | - | Mekanik durum, boru hasarı |
| Portatif baca gazı analizörü | - | Gaz sıcaklığı, bileşim |

## Adım 2: Saha Ölçümleri (Field Measurements)

### 2.1 Ölçüm Noktaları

Her eşanjör için minimum ölçüm noktaları:

```
SICAK TARAF:
  ├── Giriş sıcaklığı (T_h,in) [°C]
  ├── Çıkış sıcaklığı (T_h,out) [°C]
  ├── Kütle debisi (m_h) [kg/s]
  ├── Giriş basıncı (P_h,in) [bar]
  └── Çıkış basıncı (P_h,out) [bar] veya DP_h [kPa]

SOĞUK TARAF:
  ├── Giriş sıcaklığı (T_c,in) [°C]
  ├── Çıkış sıcaklığı (T_c,out) [°C]
  ├── Kütle debisi (m_c) [kg/s]
  ├── Giriş basıncı (P_c,in) [bar]
  └── Çıkış basıncı (P_c,out) [bar] veya DP_c [kPa]

ÇEVRE:
  ├── Çevre sıcaklığı (T_0) [°C]
  ├── Nem [%RH]
  └── Rüzgar hızı (hava soğutmalı için) [m/s]
```

### 2.2 Ölçüm Prosedürü

1. **Kararlı durum (steady-state) bekleme:** Ölçümlerden önce en az 30 dakika kararlı
   durum sağlanmalıdır. Giriş sıcaklıklarının ±1°C içinde kalması kontrol edilir.

2. **Çoklu okuma:** Her ölçüm noktasında en az 5 ardışık okuma yapılır (2 dakika aralıkla).
   Ortalama değer ve standart sapma raporlanır.

3. **Enerji dengesi doğrulaması:**
```
Q_sıcak = m_h × cp_h × (T_h,in - T_h,out)
Q_soğuk = m_c × cp_c × (T_c,out - T_c,in)

Enerji dengesi hatası = |Q_sıcak - Q_soğuk| / Q_ortalama × 100

Kabul kriteri: Hata < %5 (ASME PTC 12.5 gereksinimi)
Tercih edilen: Hata < %3
```

4. **Aynı anda ölçüm:** Tüm giriş/çıkış parametreleri mümkün olduğunca aynı anda
   ölçülmelidir. Zamansal fark 30 saniyeyi geçmemelidir.

### 2.3 Termografik İnceleme

Termal kamera ile yapılacak kontroller:

| Kontrol Noktası | Beklenen | Anormal Bulgu |
|----------------|----------|---------------|
| Gövde yüzey sıcaklığı | İzolasyon altında düşük | Sıcak noktalar (izolasyon hasarı) |
| Flanşlardaki sızıntı | Çevre sıcaklığına yakın | Sıcak bölgeler (sızıntı belirtisi) |
| Boru plakası | Homojen dağılım | Noktasal sıcak/soğuk bölgeler (tıkalı borular) |
| Bafıl bölgeleri | Düzgün dağılım | Dengesiz dağılım (baypas akışı) |
| Nozzle bağlantıları | Homojen | Sıcak noktalar (erozyon/korozyon) |

## Adım 3: Performans Hesaplamaları

### 3.1 Mevcut U-Değer Hesabı

```
Q_ölçülen = m × cp × DT  (daha güvenilir taraftan, genellikle soğuk taraf)

LMTD = f(T_h,in, T_h,out, T_c,in, T_c,out)  -- formulas.md'ye bkz.

F = f(R, P)  -- çok geçişli eşanjörler için

U_mevcut = Q_ölçülen / (A × LMTD × F)
```

### 3.2 Temizlik Faktörü (Cleanliness Factor)

```
CF = U_mevcut / U_tasarım_temiz

Burada:
- U_tasarım_temiz = kirlenme payı eklenmemiş tasarım U değeri
```

| CF Değeri | Durum | Öneri |
|-----------|-------|-------|
| > 0.85 | İyi | Rutin izlemeye devam |
| 0.70 - 0.85 | Hafif kirlenme | Temizlik planla (3-6 ay içinde) |
| 0.50 - 0.70 | Orta kirlenme | Temizlik gerekli (1-3 ay içinde) |
| 0.30 - 0.50 | Ağır kirlenme | Acil temizlik gerekli |
| < 0.30 | Kritik kirlenme | Derhal temizlik + kök neden analizi |

### 3.3 Kirlenme Direnci Hesabı

```
R_f,mevcut = (1/U_mevcut) - (1/U_temiz)

Burada:
- U_temiz = tasarım verisinden veya temiz durumdaki ölçümden
```

### 3.4 Basınç Düşüşü Analizi

```
DP_ölçülen = P_giriş - P_çıkış  [kPa]

DP_oranı = DP_ölçülen / DP_tasarım

Değerlendirme:
- DP_oranı < 1.1: Normal
- DP_oranı 1.1 - 1.3: Hafif kirlenme/tıkanma
- DP_oranı 1.3 - 1.5: Orta kirlenme, temizlik gerekli
- DP_oranı > 1.5: Ciddi tıkanma veya mekanik sorun
```

### 3.5 Exergy Analizi (Seviye 3)

Seviye 3 denetimde tam exergy analizi yapılır:

```
1. Giriş/çıkış exergy hesabı:
   Ex = m × [(h - h_0) - T_0 × (s - s_0)]

2. Entropi üretimi:
   S_gen = m_h × (s_h,out - s_h,in) + m_c × (s_c,out - s_c,in)

3. Exergy yıkımı:
   I = T_0 × S_gen

4. Exergy verimi:
   eta_ex = (Ex_c,out - Ex_c,in) / (Ex_h,in - Ex_h,out)

5. Exergy yıkım dağılımı:
   I_DT = sıcaklık farkına bağlı exergy yıkımı
   I_DP = basınç düşüşüne bağlı exergy yıkımı
```

## Adım 4: Titreşim Analizi ve Mekanik Değerlendirme

### 4.1 Titreşim Ölçüm Noktaları

| Ölçüm Noktası | Kabul Edilebilir | Uyarı | Alarm |
|--------------|-----------------|-------|-------|
| Gövde (radyal) | < 4 mm/s RMS | 4-7 mm/s | > 7 mm/s |
| Nozzle bağlantısı | < 3 mm/s RMS | 3-5 mm/s | > 5 mm/s |
| Destek ayakları | < 2 mm/s RMS | 2-4 mm/s | > 4 mm/s |

### 4.2 Boru Hasarı Göstergeleri

| Bulgu | Olası Neden | Aksiyon |
|-------|-------------|---------|
| Yüksek titreşim | Akış kaynaklı titreşim (FIV) | Bafıl aralığı kontrolü |
| Aşırı basınç düşüşü | Boru tıkanması veya ezilmesi | Hidrostatik test |
| Sıcaklık anomalisi | İç sızıntı (boru delinmesi) | Boru testi (helium/su) |
| Gövde deformasyonu | Termal gerilme | Genleşme bağlantısı kontrolü |

## Adım 5: Tipik Denetim Bulguları ve Aksiyonlar

### 5.1 En Yaygın Bulgular

| # | Bulgu | Sıklık | Tipik Etki | Öncelik |
|---|-------|--------|-----------|---------|
| 1 | Kirlenme (fouling) | %60-70 | U düşüşü %15-40 | Yüksek |
| 2 | Yetersiz izolasyon | %40-50 | Ek kayıp %3-8 | Orta |
| 3 | Debi dengesizliği | %30-40 | epsilon düşüşü %10-20 | Orta |
| 4 | Yüksek yaklaşım sıcaklığı | %50-60 | Exergy verimi düşük | Yüksek |
| 5 | Aşırı basınç düşüşü | %20-30 | Pompaj maliyeti artışı | Orta |
| 6 | Hava birikimi (air pocket) | %10-20 | Lokal ısı transfer düşüşü | Düşük |
| 7 | Baypas akışı | %15-25 | Efektif alan azalması | Orta |
| 8 | Boru tıkanması | %10-15 | Kapasite kaybı | Yüksek |

### 5.2 Kirlenme Tipleri ve Tespit Yöntemleri

| Kirlenme Tipi | Belirtiler | Tespit Yöntemi |
|---------------|-----------|----------------|
| Kimyasal (kireç) | U düşüşü, DP artışı | Su analizi, görsel muayene |
| Biyolojik | U düşüşü, koku, DP artışı | Mikrobiyolojik test |
| Partikül (çökelme) | U düşüşü, dengesiz akış | Filtrasyon kontrolü |
| Korozyon | Gövde/boru incelme | UT kalınlık ölçümü |
| Termal (cracking) | Karbon birikimi, U düşüşü | Görsel + kimyasal analiz |

### 5.3 İyileştirme Fırsatları — Hızlı Kazanımlar (Quick Wins)

| İyileştirme | Tipik Tasarruf | Yatırım | GDS |
|-------------|---------------|---------|-----|
| Kimyasal temizlik | %10-25 ısı geri kazanımı | 2,000 - 8,000 EUR | < 3 ay |
| İzolasyon onarımı/iyileştirme | %2-5 enerji tasarrufu | 1,000 - 5,000 EUR | < 6 ay |
| Conta değişimi (plakalı HX) | %5-15 kapasite artışı | 500 - 3,000 EUR | < 2 ay |
| Debi dengeleme | %5-10 verim artışı | 500 - 2,000 EUR | < 3 ay |
| Hava tahliye (vent) kontrolü | %2-5 ısı transfer iyileştirme | 100 - 500 EUR | < 1 ay |
| Filtrasyon iyileştirme | Kirlenme hızını %30-50 azaltma | 1,000 - 5,000 EUR | < 6 ay |

### 5.4 Orta/Uzun Vadeli İyileştirmeler

| İyileştirme | Tipik Tasarruf | Yatırım | GDS |
|-------------|---------------|---------|-----|
| Eşanjör yükseltmesi (upgrade) | %15-30 verim artışı | 10,000 - 50,000 EUR | 1-3 yıl |
| Ekonomizer eklenmesi | %5-12 yakıt tasarrufu | 15,000 - 80,000 EUR | 1-2 yıl |
| Plakalı HX'e geçiş | %20-40 verim artışı | 8,000 - 40,000 EUR | 1-2 yıl |
| Isı geri kazanım ağı | %10-25 toplam tasarruf | 50,000 - 500,000 EUR | 2-5 yıl |
| Online temizlik sistemi | Sürekli yüksek CF | 5,000 - 30,000 EUR | 1-3 yıl |

## Adım 6: Raporlama

### 6.1 Denetim Rapor İçeriği

```
1. Yönetici Özeti
   - Anahtar bulgular
   - Toplam tasarruf potansiyeli [kW ve EUR/yıl]
   - Öncelikli aksiyonlar

2. Eşanjör Envanteri ve Mevcut Durum
   - Her eşanjör için kimlik ve tasarım bilgileri
   - Mevcut performans parametreleri
   - Benchmark karşılaştırması

3. Detaylı Analiz Sonuçları
   - U-değer trend grafikleri
   - Temizlik faktörü hesapları
   - Basınç düşüşü analizi
   - Exergy analizi (Seviye 3 ise)

4. İyileştirme Önerileri
   - Önceliklendirilmiş aksiyon listesi
   - Her öneri için: teknik açıklama, beklenen tasarruf, maliyet tahmini, GDS
   - Uygulama zaman çizelgesi

5. İzleme Planı
   - KPI tanımları
   - Ölçüm sıklığı
   - Hedef değerler
```

### 6.2 Anahtar Performans Göstergeleri (KPIs)

| KPI | Birim | Ölçüm Sıklığı | Hedef |
|-----|-------|--------------|-------|
| U_mevcut / U_tasarım | — | Haftalık | > 0.75 |
| Temizlik faktörü (CF) | — | Haftalık | > 0.80 |
| DT_approach | °C | Günlük | < Tasarım × 1.2 |
| DP_mevcut / DP_tasarım | — | Haftalık | < 1.30 |
| Exergy verimi (eta_ex) | % | Aylık | > Benchmark "İyi" |
| Enerji maliyeti | EUR/GJ | Aylık | Azalan trend |
| Temizlik arası süre | gün | Her temizlikte | Artan trend |

## İlgili Dosyalar

- `heat_exchanger/formulas.md` — Hesaplama formülleri
- `heat_exchanger/benchmarks.md` — Performans benchmark verileri
- `heat_exchanger/standards.md` — TEMA, ASME standartları
- `heat_exchanger/case_studies.md` — Vaka çalışmaları

## Referanslar

1. ASME PTC 12.5 (2000). *Single Phase Heat Exchangers Performance Test Code*.
2. ASME PTC 19.1 (2018). *Test Uncertainty*.
3. ISO 50002:2014. *Energy audits — Requirements with guidance for use*.
4. ISO 50001:2018. *Energy management systems — Requirements with guidance for use*.
5. TEMA (2019). *Standards of the Tubular Exchanger Manufacturers Association*. 10th ed.
6. API 660 (2015). *Shell-and-Tube Heat Exchangers*.
7. BS EN 1434 (2015). *Heat meters*.
8. Thulukkanam, K. (2013). *Heat Exchanger Design Handbook*. 2nd ed., CRC Press.
9. Bott, T.R. (1995). *Fouling of Heat Exchangers*. Elsevier.
10. EPTR (2009). *Reference Document on Best Available Techniques for Energy Efficiency*. European Commission.
