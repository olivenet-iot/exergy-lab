---
title: "Çözüm: Chiller VSD (Değişken Hızlı Sürücü) Uygulaması"
category: solutions
equipment_type: chiller
keywords: [VSD, değişken hız, chiller, enerji tasarrufu]
related_files: [chiller/formulas.md, chiller/benchmarks.md, chiller/equipment/centrifugal.md]
use_when: ["Chiller'a VSD önerisi değerlendirilirken", "Değişken soğutma yükü analiz edilirken"]
priority: high
last_updated: 2026-01-31
---
# Çözüm: Chiller VSD (Değişken Hızlı Sürücü) Uygulaması

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Sabit hızlı chiller'lar kısmi yüklerde enerji israf eder. Santrifüj chiller'larda giriş yönlendirme kanatları (IGV — Inlet Guide Vanes) ve vidalı chiller'larda sürgülü vana (slide valve) ile kapasite kontrolü yapılır; ancak bu yöntemler kompresör hızını değiştirmediği için kısmi yüklerde COP önemli ölçüde düşer. Özellikle %50 yükün altında enerji israfı belirgin hale gelir.

**Çözüm:** VSD (Variable Speed Drive / Değişken Hızlı Sürücü) ile kompresör hızını gerçek zamanlı soğutma yüküne göre ayarlamak. Kompresör devri düşürülerek enerji tüketimi yükle orantılı hale getirilir.

**Tipik Tasarruf:** %15-35 (yıllık enerji tüketiminde)
**Tipik ROI:** 2-4 yıl

## Çalışma Prensibi

VSD, chiller kompresör motorunun hızını soğutma talebine göre sürekli olarak ayarlar:

- **Santrifüj chiller'da VSD:** IGV yerine devir kontrolü ile kapasite ayarı yapılır. Surge limiti ortadan kalkar, çalışma aralığı genişler. Düşük devirlerde kompresör daha geniş bir yük aralığında verimli çalışır
- **Vidalı chiller'da VSD:** Slide valve ile kombine çalışarak kısmi yüklerde COP'u önemli ölçüde artırır. Sabit hızlı vidalı kompresörde %50 yükte COP yaklaşık %30 düşerken, VSD ile bu kayıp %10-15'e iner
- **Devir-kapasite ilişkisi:** Kompresör devri düştükçe soğutma kapasitesi yaklaşık doğrusal olarak azalır
- **Devir-güç ilişkisi:** Güç tüketimi devirle yaklaşık kübik orantılıdır (Affinity Laws benzeri etki), ancak chiller'larda lift (basınç farkı) sabit kaldığı için gerçek tasarruf kübik yasadan biraz düşüktür
- **Surge eliminasyonu (santrifüj):** Sabit hızlı santrifüj chiller'larda düşük yükte surge riski vardır; VSD ile devir düşürülerek surge sınırı aşağıya kaydırılır ve chiller daha düşük yüklere kadar güvenle çalışabilir

### Santrifüj vs Vidalı Chiller'da VSD Etkisi

| Parametre | Santrifüj Chiller + VSD | Vidalı Chiller + VSD |
|-----------|------------------------|---------------------|
| Kapasite kontrol mekanizması | Devir kontrolü (IGV devre dışı veya tam açık) | Devir kontrolü + slide valve |
| Surge riski | Eliminasyon — VSD surge limitini ortadan kaldırır | Surge yok (vidalı kompresörde zaten yok) |
| Minimum yük | %10-15 (VSD ile genişletilmiş) | %15-25 |
| Kısmi yük COP iyileşmesi | %20-40 (%50 yükte) | %15-30 (%50 yükte) |
| Tam yük etkisi | %0-2 kayıp (VSD elektroniği nedeniyle) | %0-2 kayıp |
| Motor tipi | Yüksek hızlı PM veya indüksiyon motor | Standart indüksiyon motor |
| Maliyet farkı | Yüksek (özellikle yüksek hızlı motorlarda) | Orta |

## Kısmi Yük Karşılaştırması: Sabit Hız vs VSD

| Yük Oranı | Sabit Hız kW/ton | VSD kW/ton | COP Sabit Hız | COP VSD | VSD Tasarrufu |
|------------|------------------|------------|---------------|---------|---------------|
| %100 | 0.60 | 0.61 | 5.86 | 5.77 | -%2 (VSD kayıp) |
| %75 | 0.62 | 0.50 | 5.68 | 7.03 | %19 |
| %50 | 0.68 | 0.38 | 5.18 | 9.26 | %44 |
| %25 | 0.82 | 0.30 | 4.29 | 11.73 | %63 |
| IPLV/NPLV | 0.65 | 0.42 | 5.41 | 8.38 | %35 |

*Not: Değerler tipik 500 ton su soğutmalı santrifüj chiller içindir. Gerçek değerler üreticiye ve çalışma koşullarına göre değişir.*

## Uygulanabilirlik Kriterleri

### VSD Ne Zaman Uygulanmalı
- Chiller yıllık çalışma süresinin >%60'ı kısmi yükte çalışıyorsa
- Ortalama yük oranı <%75 ise
- Chiller kapasitesi >200 kW (57 ton) ise
- Yıllık çalışma süresi >3,000 saat ise
- Elektrik fiyatı yüksek olan tesislerde (>€0.10/kWh)
- Mevcut chiller'da IGV veya slide valve ile kapasite kontrolü yapılıyorsa
- Birden fazla chiller'ın paralel çalıştığı tesislerde (sıralama + VSD kombinasyonu)

### VSD Ne Zaman Uygulanmamalı
- Chiller sürekli tam yükte (%90-100) çalışıyorsa — VSD %2-3 ek kayıp yaratır
- Chiller kapasitesi <100 kW ise — maliyet/fayda dengesizliği
- Chiller ekonomik ömrünün sonuna yaklaşmışsa (<3 yıl kalan ömür)
- Mevcut motor VSD uyumlu değilse ve motor değişimi bütçeyi aşıyorsa
- Elektrik altyapısı harmonik filtrelemeyi desteklemiyorsa

## Motor Uyumluluğu ve Harmonik Filtrasyon

### Motor Uyumluluğu

| Faktör | Gereksinim | Açıklama |
|--------|-----------|----------|
| Motor sınıfı | IE3 veya IE4 (invertör uyumlu) | Standart motor VSD ile aşırı ısınabilir |
| İzolasyon sınıfı | Sınıf F veya H | VSD gerilim tepe değerleri izolasyonu zorlar |
| Rulman izolasyonu | Seramik izoleli veya topraklama fırçası | VSD kaynaklı şaft akımları rulman hasarına yol açar |
| Soğutma | Ayrı fan veya sıvı soğutma | Düşük devirde yetersiz soğutma riski |
| Encoder/sensör | Hız geri bildirimi (sensorless veya encoder) | Hassas hız kontrolü için |

### Harmonik Filtrasyon

| Çözüm | THD Seviyesi | Maliyet | Uygulama |
|--------|-------------|---------|----------|
| 6 darbeli sürücü (filtresiz) | %30-40 | Düşük | Küçük yükler, güçlü şebeke |
| AC/DC reaktör (choke) | %15-25 | Düşük-orta | Standart uygulama |
| 12 darbeli sürücü | %8-12 | Orta | Orta boy chiller'lar |
| 18 darbeli sürücü | %3-5 | Yüksek | Büyük chiller'lar |
| Aktif ön uç (AFE) | <%5 | Yüksek | Premium çözüm, enerji geri kazanımı |
| Pasif harmonik filtre | %5-8 | Orta-yüksek | Retrofit uygulamalar |

## Yatırım Maliyeti

| Chiller Kapasitesi (kW) | Chiller Kapasitesi (ton) | VSD Retrofit Maliyeti (€) | Yeni VSD Chiller Ek Maliyeti (€) | Yeni VSD Chiller Toplam (€) |
|--------------------------|--------------------------|---------------------------|----------------------------------|----------------------------|
| 100 | 28 | 10,000-18,000 | 8,000-15,000 | 50,000-80,000 |
| 300 | 85 | 18,000-30,000 | 15,000-25,000 | 90,000-150,000 |
| 500 | 142 | 25,000-40,000 | 20,000-35,000 | 130,000-220,000 |
| 1,000 | 284 | 35,000-55,000 | 30,000-50,000 | 200,000-350,000 |
| 1,500 | 427 | 45,000-65,000 | 40,000-60,000 | 280,000-420,000 |
| 2,000 | 569 | 55,000-75,000 | 50,000-70,000 | 350,000-480,000 |
| 3,000 | 853 | 65,000-80,000 | 60,000-80,000 | 420,000-500,000 |

**Not:** VSD retrofit maliyeti; sürücü ünitesi, harmonik filtre, kablolama, kontrol entegrasyonu ve devreye alma dahildir. Yeni VSD chiller ek maliyeti, standart sabit hızlı chiller'a göre fark tutarıdır.

## ROI Hesabı

### Formül
```
Yıllık_enerji_sabit = Kapasite_kW × Çalışma_saati × Ort_yük × kW_ton_sabit / COP_sabit
Yıllık_enerji_VSD = Kapasite_kW × Çalışma_saati × Ort_yük × kW_ton_VSD / COP_VSD
Yıllık_tasarruf_kWh = Yıllık_enerji_sabit - Yıllık_enerji_VSD
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

Burada:
- `Kapasite_kW`: Chiller nominal soğutma kapasitesi [kW]
- `Çalışma_saati`: Yıllık chiller çalışma süresi [saat/yıl]
- `Ort_yük`: Ortalama yük oranı (0-1 arası)
- `kW_ton_sabit`: Sabit hızlı chiller'ın IPLV değeri [kW/ton]
- `kW_ton_VSD`: VSD chiller'ın IPLV değeri [kW/ton]
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap
- 1,000 kW (284 ton) su soğutmalı santrifüj chiller, 4,500 saat/yıl, ortalama %60 yük
- Sabit hızlı IPLV: 0.65 kW/ton → ortalama tüketim: 284 × 0.65 = 184.6 kW
- VSD IPLV: 0.42 kW/ton → ortalama tüketim: 284 × 0.42 = 119.3 kW
- Elektrik fiyatı: €0.12/kWh

```
Yıllık_tasarruf_kWh = (184.6 - 119.3) × 4,500 = 293,850 kWh
Yıllık_tasarruf_EUR = 293,850 × 0.12 = €35,262/yıl
VSD retrofit yatırımı = €45,000
Geri_ödeme = 45,000 / 35,262 = 1.28 yıl
```

- **Geri ödeme süresi: ~1.3 yıl**

## Uygulama Adımları

1. **Yük profili analizi:** En az 1 aylık chiller yük verisi toplayarak kısmi yük dağılımını belirle. Saatlik soğutma yükü, giriş/çıkış suyu sıcaklıkları ve kompresör güç tüketimini kaydet
2. **Chiller tipi ve uyumluluk değerlendirmesi:** Mevcut chiller'ın VSD retrofit'e uygunluğunu üretici ile doğrula. Motor tipi, rulman yapısı ve kontrol kartı uyumluluğunu kontrol et
3. **Tasarruf hesabı:** Gerçek yük profili ve üretici VSD performans eğrileri kullanılarak yıllık enerji tasarrufunu hesapla. Bin-saat analizi ile IPLV karşılaştırması yap
4. **Elektrik altyapısı değerlendirmesi:** Mevcut elektrik panosu kapasitesi, harmonik filtre gereksinimi ve kablo boyutunu kontrol et. IEEE 519 harmonik uyumluluğunu doğrula
5. **VSD seçimi ve tedarik:** Chiller üreticisinin onaylı VSD modeli tercih edilmeli. Harmonik filtre, EMC filtre ve bypass kontaktörü dahil paket temin et
6. **Kurulum ve kablolama:** VSD ünitesini chiller yakınına monte et. Motor kablolamasını ekranlı kablo ile yap, topraklamayı EMC standartlarına uygun gerçekleştir
7. **Devreye alma ve optimizasyon:** VSD parametrelerini (minimum/maksimum frekans, rampa süreleri, PID ayarları) optimize et. Surge sınır haritasını (santrifüj tip) VSD kontrolcüsüne tanımla. En az 2 haftalık test periyodunda tüm yük koşullarında performansı doğrula

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Surge (santrifüj) | Düşük devirde ve yüksek lift koşullarında surge riski devam edebilir | VSD kontrolcüsüne surge haritası yükle, anti-surge algoritması aktif et |
| Harmonikler | VSD elektrik şebekesine harmonik bozulma yaratır (THD artışı) | Harmonik filtre (pasif veya aktif), 18 darbeli sürücü veya AFE kullan |
| Motor ısınma | Düşük devirde motor soğutması yetersiz kalır | IE3+ invertör uyumlu motor, ayrı soğutma fanı veya sıvı soğutmalı motor |
| Rulman aşınması | VSD kaynaklı şaft akımları (bearing currents) rulman hasarına yol açar | Seramik izoleli rulman veya şaft topraklama fırçası kullan |
| Minimum hız limiti | Çok düşük devirde yağ dönüşü bozulur, yağlama yetersiz kalır | Minimum devir limitini %20-30 nominal hızda tut |
| Yağ dönüş problemi | Düşük soğutucu akışkan debisinde yağ evaporatörde birikir | Yağ geri dönüş sistemi kontrolü, minimum çalışma süresi ayarı |
| Kontrol karmaşıklığı | VSD + chiller kontrol entegrasyonu karmaşık olabilir | Chiller üreticisi onaylı VSD ve entegre kontrol sistemi kullan |
| EMC parazit | Elektromanyetik girişim hassas ekipmanları etkileyebilir | Ekranlı kablo, uygun topraklama, EMC filtre |

## İlgili Dosyalar
- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller exergy formülleri: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Kondenser optimizasyonu: `solutions/chiller_condenser_optimization.md`
- Chiller sıralama optimizasyonu: `solutions/chiller_sequencing.md`
- Soğutma suyu sıcaklık reset: `solutions/chiller_chilled_water_reset.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, "Compressors" and "Liquid Chilling Systems" chapters
- ASHRAE Standard 90.1, "Energy Standard for Buildings Except Low-Rise Residential Buildings"
- DOE/FEMP, "Chiller Management Best Practices"
- Carrier/Trane/York, "Application Guide — Variable Speed Centrifugal Chillers"
- AHRI Standard 550/590, "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages"
- Europump/Hydraulic Institute, "Variable Speed Pumping — A Guide to Successful Applications"
- IEEE 519, "Recommended Practice for Harmonic Control in Electric Power Systems"
- BSRIA, "Rules of Thumb — Guidelines for Building Services" 5th Edition
