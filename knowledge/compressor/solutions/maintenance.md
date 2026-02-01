---
title: "Çözüm: Bakım Tabanlı Enerji Verimliliği"
category: solutions
equipment_type: compressor
keywords: [bakım, kompresör, izleme, yağ analizi]
related_files: [compressor/audit.md, compressor/benchmarks.md, compressor/solutions/air_leaks.md]
use_when: ["Kompresör bakım programı önerilirken", "Performans izleme sistemi kurulurken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Bakım Tabanlı Enerji Verimliliği

> Son güncelleme: 2026-01-31

## Özet

**Problem:** İhmal edilen bakım, kompresör enerji tüketimini %3-15 artırır ve ekipman ömrünü kısaltır.

**Çözüm:** Sistematik filtre, yağ, soğutucu bakımı ve prediktif bakım teknolojileri uygulaması.

**Tipik Tasarruf:** %3-15
**Tipik ROI:** Anlık - 6 ay

## 1. Filtre Bakımı

### 1.1 Hava Giriş Filtresi (Inlet Air Filter)

| Parametre | Değer |
|-----------|-------|
| Temiz ΔP | 10-30 mbar |
| Değişim eşiği | 50-100 mbar |
| Enerji etkisi | +%0.5-1.0 / 50 mbar ΔP artışı |
| Değişim aralığı | Her 2,000-4,000 saat |
| Eleman maliyeti | €20-100 |

**Kritik risk:** Aşırı tıkanmış filtre yırtılabilir → kontaminantlar airend'e girer → katastrofik hasar (€10,000-50,000 onarım maliyeti). Filtre bakımını asla ertellemeyin.

### 1.2 Yağ Filtresi (Oil Filter)

| Parametre | Değer |
|-----------|-------|
| Temiz ΔP | 0.3-0.5 bar |
| Değişim eşiği | 0.8-1.2 bar |
| Enerji etkisi | +%0.5-2.0 / tıkandıkça |
| Değişim aralığı | Her 2,000-4,000 saat |
| Eleman maliyeti | €30-80 |

**Risk:** Yetersiz yağ akışı → aşırı ısınma → airend tutulması.

### 1.3 Yağ Separatörü (Oil Separator Element)

| Parametre | Değer |
|-----------|-------|
| Temiz ΔP | 0.2-0.3 bar |
| Değişim eşiği | 0.8-1.0 bar |
| Enerji etkisi | +%1-5 (her 0.1 bar ≈ %0.5-0.7) |
| **Ciddi tıkanma** | **+0.5-1.5 bar → %3-10 enerji artışı** |
| Değişim aralığı | Her 4,000-8,000 saat |
| Eleman maliyeti | €100-500 |

**Not:** Separator tıkanması doğrudan kompresör çıkış basıncına eklenir — en yüksek enerji etkisine sahip filtredir.

### 1.4 Hat Filtreleri (Line Filters)

Kompresör sonrası filtreler: partikül, koalesan, aktif karbon.

| Parametre | Değer |
|-----------|-------|
| Temiz ΔP (her biri) | 0.05-0.15 bar |
| Değişim eşiği | 0.3-0.5 bar |
| Seri filtre sorunu | 3 filtre seri → ihmal edildiğinde toplam 1.0-2.0 bar |
| Toplam enerji etkisi | +%3-14 (ihmal edilmiş çoklu filtre) |
| Değişim aralığı | Yılda bir veya ΔP'ye göre |
| Eleman seti maliyeti | €50-200 |

**En iyi uygulama:** Her filtre elemanını ayrı diferansiyel basınç göstergesi ile izle.

## 2. Yağ Kalitesi ve Yönetimi

### 2.1 Yağ Analizi Programı

| Parametre | Açıklama | Alarm Seviyesi |
|-----------|----------|---------------|
| Viskozite | Temel yağlama parametresi | ±%15 yeni yağ değerinden |
| TAN (Toplam Asit Sayısı) | Oksidasyon göstergesi | Üretici limitini aşınca |
| Su içeriği | Soğutucu sızıntısı göstergesi | >500 ppm uyarı, >1000 ppm alarm |
| Partikül sayısı | Temizlik seviyesi | ISO 4406 sınıfına göre |
| Aşınma metalleri | Komponent aşınması göstergesi | Fe, Cu, Pb artış trendi |
| Katkı tükenmesi | Yağ ömür sonu | Üretici spesifikasyonuna göre |

**Analiz sıklığı:** Her 1,000-2,000 saat veya 3 ayda bir (hangisi önce gelirse)

### 2.2 Yağ Değişim Aralıkları

| Yağ Tipi | Tipik Değişim Aralığı | Maliyet (yaklaşık) |
|---------|---------------------|-------------------|
| Mineral yağ | 2,000-4,000 saat | Düşük |
| Yarı sentetik | 4,000-6,000 saat | Orta |
| Tam sentetik (PAO/diester) | 6,000-8,000 saat | Yüksek |
| Uzun ömürlü sentetik | 8,000-12,000 saat | Çok yüksek |

**Durum bazlı değişim önerisi:** Analiz sonuçlarına göre değiştir — sabit aralıktan daha ekonomik ve güvenli.

### 2.3 Bozulmuş Yağın Enerji Etkisi

- Artan viskozite → daha fazla sürtünme → +%1-3 güç tüketimi
- Kötüleşen soğutma → daha yüksek çalışma sıcaklığı → düşen verim
- Kötüleşen sızdırmazlık → artan iç kaçak → düşen volumetrik verim

### 2.4 Yağ Tipi Yükseltme

Mineral → sentetik yağa geçiş:
- Değişim aralığı uzar (2-3 kat)
- Verim iyileşmesi: %1-2 (düşük sürtünme, daha iyi termal iletkenlik)
- Sentetik yağ 2-5 kat daha pahalı ama uzun aralık → benzer yaşam döngüsü maliyeti

## 3. Soğutucu Bakımı

### 3.1 Aftercooler (Hava veya Su Soğutmalı)

| Parametre | Değer |
|-----------|-------|
| Kirliliğin etkisi | +5-15°C çıkış sıcaklığı artışı |
| Sonuçlar | Daha fazla nem → kurutucu aşırı yüklenir |
| Ciddi kirlilik | Yüksek sıcaklık alarmı → duruş |
| Temizlik aralığı | 1-3 ayda bir (ortama bağlı) |
| Yöntem | Basınçlı hava ile üfleme veya yıkama (hava soğutmalı) |

### 3.2 Yağ Soğutucu

| Parametre | Değer |
|-----------|-------|
| Kirliliğin etkisi | Yağ sıcaklığı artışı → viskozite düşüşü → verim kaybı (%1-3) |
| **Kritik kural** | Her 10°C yağ sıcaklığı artışı → yağ ömrü %50 azalır (Arrhenius) |
| Ciddi kirlilik | Yüksek sıcaklık duruşu riski |
| Temizlik aralığı | Aftercooler ile aynı program |

## 4. Valf Bakımı (Pistonlu Kompresörler)

Emme ve basma valfleri pistonlu kompresörlerin kritik aşınma parçalarıdır.

### Aşınmış Valfların Etkileri
- İç geri genleşme kayıpları
- Volumetrik verim düşüşü
- Çıkış sıcaklığı artışı
- **Enerji tüketimi artışı: %5-15**

### Belirtiler
- Artan çıkış sıcaklığı
- Kapasite düşüşü (basıncı korumak için daha uzun yüklü çalışma)
- Anormal ses veya titreşim
- Normalden yüksek akım çekişi

### Bakım
- Valf kontrolü: Her 8,000-16,000 saat veya durum izlemeye göre
- Valf revizyon maliyeti: €500-5,000/kademe (kompresör boyutuna bağlı)

## 5. Prediktif Bakım Teknolojileri

### 5.1 Titreşim Analizi

| Parametre | Değer |
|-----------|-------|
| İzlenen arızalar | Yatak durumu, rotor balansı, kaplin hizası, motor durumu |
| Yöntemler | Toplam titreşim (mm/s), spektral analiz (FFT), zarf analizi |
| Standartlar | ISO 10816 / ISO 20816 (titreşim şiddeti) |
| Program | Aylık (portatif) veya sürekli (online sensörler) |
| Portatif cihaz maliyeti | €5,000-20,000 |
| Online sistem maliyeti | €500-2,000/ölçüm noktası |
| Ürünler | SKF Microlog, Fluke 810, SKF Axios, ABB Ability Smart Sensor |

### 5.2 Sıcaklık İzleme

| İzlenen Noktalar | Alarm Göstergesi |
|-----------------|-----------------|
| Çıkış sıcaklığı trendi | Kirli soğutucu, bozulmuş yağ, aşınmış iç parçalar |
| Yatak sıcaklığı | Yatak bozulması |
| Motor sargı sıcaklığı | İzolasyon bozulması veya aşırı yük |

Çoğu modern kompresörde entegre sensörler mevcuttur — kontrol panelinden trend takibi yeterli.

### 5.3 Yağ Analizi (Bölüm 2 ile ilişkili)

Aşınma metallerinin trend analizi:
- Fe (demir) = airend rotor/gövde aşınması
- Cu (bakır) = yatak kafesi aşınması
- Pb (kurşun), Sn (kalay) = yatak kaplama aşınması
- Si (silikon) = giriş filtrasyonu problemi (toz girişi)

### 5.4 Akım/Güç İzleme

| Gösterge | Anlam |
|----------|-------|
| Kademeli akım artışı (aynı yükte) | Mekanik bozulma (yatak, sürtünme artışı) |
| Ani akım değişimi | Valf arızası, iç kaçak, kontrol sorunu |

Maliyet: €200-1,000/izleme noktası (CT + veri kaydedici)

### 5.5 Hava Kalitesi İzleme

- Yağ buharı, partikül sayısı, çiğ noktası izleme
- Filtre/kurutucu bozulmasını üretimi etkilemeden tespit
- **Ürünler:** SUTO/CS Instruments S120 (yağ buharı), S110 (çiğ noktası), BEKO METPOINT serisi

## 6. Bakım Etkisi Özet Tablosu

| Bakım Kalemi | İhmal Cezası (Enerji) | Bakım Maliyeti | Enerji Tasarrufu |
|-------------|----------------------|----------------|-----------------|
| Giriş filtresi | +%0.5-1.0 | €20-100/eleman | %0.5-1.0 |
| Yağ filtresi | +%0.5-2.0 | €30-80/eleman | %0.5-2.0 |
| Yağ separatörü | +%3-10 | €100-500/eleman | %3-10 |
| Hat filtreleri (tümü) | +%3-14 | €50-200/eleman seti | %3-14 |
| Yağ kalitesi | +%1-3 | €200-600 (yağ + analiz) | %1-3 |
| Soğutucu temizliği | Dolaylı (duruş riski) | €0 (işçilik) | %0.5-2 |
| Valf revizyonu (pistonlu) | +%5-15 | €500-5,000 | %5-15 |
| Kayış gerginliği/değişimi | -%2-5 kapasite | €20-100 | %1-5 |

## 7. Bakım Programı Şablonu

### Günlük Kontroller
- [ ] Kompresör çalışma durumu (hata kodu yok)
- [ ] Çıkış basıncı normal aralıkta
- [ ] Yağ seviyesi yeterli
- [ ] Kondansat drenaj çalışıyor
- [ ] Anormal ses veya titreşim yok

### Haftalık Kontroller
- [ ] Kondansat drenaj testi (manuel)
- [ ] Kompresör odası sıcaklığı (<35°C)
- [ ] Filtre diferansiyel basınç kontrolleri

### Aylık Kontroller
- [ ] Soğutucu kanatçık temizliği (hava soğutmalı)
- [ ] Kayış kontrolü (kayış tahrikli ise)
- [ ] Genel görsel muayene (sızıntı, korozyon)

### 3 Aylık Kontroller
- [ ] Yağ analizi numunesi al
- [ ] Titreşim ölçümü (portatif ise)
- [ ] Kompresör performans kontrolü (SPC hesapla)

### 6 Aylık / Yıllık Kontroller
- [ ] Giriş filtresi değişimi (veya ΔP'ye göre)
- [ ] Yağ filtresi değişimi
- [ ] Tüm hat filtreleri kontrolü/değişimi
- [ ] Kurutucu performans testi
- [ ] Emniyet valfi testi
- [ ] Kaçak taraması

### 4,000-8,000 Saat Kontroller
- [ ] Yağ separatörü değişimi (veya ΔP'ye göre)
- [ ] Yağ değişimi (veya analiz sonucuna göre)
- [ ] Valf kontrolü (pistonlu kompresörler)
- [ ] Kapsamlı mekanik muayene

## İlgili Dosyalar
- Benchmark verileri: `benchmarks/compressor_benchmarks.md` (Bölüm 5: Yaş/Bakım Etkisi)
- Vidalı kompresör: `equipment/compressor_screw.md`
- Pistonlu kompresör: `equipment/compressor_piston.md`
- Giriş havası: `solutions/compressor_inlet_optimization.md`

## Referanslar
- DOE/AMO, "Improving Compressed Air System Performance" — Maintenance Chapter
- Compressed Air Challenge, "Fundamentals" and "Advanced" Training Materials
- ISO 10816 / ISO 20816 — Machinery Vibration
- ISO 8573 — Compressed Air Quality
- Atlas Copco, "Service Solutions" Documentation
- SKF, "Condition Monitoring" Handbook
