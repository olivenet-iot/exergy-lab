---
title: "Yanma Ayarı — Combustion Tuning"
category: solutions
equipment_type: boiler
keywords: [yanma ayarı, O2, kazan, verimlilik]
related_files: [boiler/formulas.md, boiler/solutions/oxygen_control.md, boiler/benchmarks.md]
use_when: ["Yanma ayarı önerisi değerlendirilirken", "Fazla hava oranı optimize edilirken"]
priority: medium
last_updated: 2026-01-31
---
# Yanma Ayarı — Combustion Tuning

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Brülör drift'i, kirli nozullar ve değişen yakıt kalitesi nedeniyle hava-yakıt oranı zamanla bozulur. Fazla hava ile çalışan kazanlar baca gazı kayıplarını artırır; yetersiz hava ise eksik yanma, CO emisyonu ve güvenlik riski yaratır.

**Çözüm:** Profesyonel yanma analizi ve brülör ayarı (combustion tuning) ile hava-yakıt oranının optimum noktaya getirilmesi, düzenli bakım programı oluşturulması.

**Tipik Tasarruf:** %1-4 yakıt tüketiminden
**Tipik ROI:** <0.5 yıl

## Çalışma Prensibi

### Stokiyometrik Yanma vs Gerçek Yanma

Teorik (stokiyometrik) yanma, yakıtın tam yanması için gereken minimum hava miktarını tanımlar:

```
CH₄ + 2O₂ → CO₂ + 2H₂O   (metan için stokiyometrik denklem)
```

- **Stokiyometrik hava:** 1 m³ doğalgaz için yaklaşık 9.5-10 m³ hava gerekir
- **Gerçek yanmada** karışım homojen değildir; brülör geometrisi, hava kanalı koşulları ve yakıt basıncı değişkendir
- Bu nedenle pratikte stokiyometrik miktardan **fazla hava** (excess air) verilir
- Doğalgazda tipik fazla hava: %10-20 (yani toplam hava stokiyometriğin 1.10-1.20 katı)

### Hava-Yakıt Oranı Optimizasyonu

Hava-yakıt oranı (λ — lambda), verilen gerçek hava miktarının stokiyometrik hava miktarına oranıdır:

```
λ = Gerçek_hava / Stokiyometrik_hava
```

| λ Değeri | Durum | Sonuç |
|----------|-------|-------|
| λ < 1.0 | Yetersiz hava (zengin karışım) | Eksik yanma, CO üretimi, is, verim kaybı, patlama riski |
| λ = 1.0 | Stokiyometrik (teorik ideal) | Pratikte ulaşılamaz — karışım homojenliği yetersiz |
| λ = 1.10-1.20 | Optimum aralık (doğalgaz) | En yüksek verim, düşük CO, kabul edilebilir NOₓ |
| λ > 1.30 | Aşırı fazla hava | Baca gazı kayıpları artar, verim düşer |

### CO vs O₂ Dengesi — "Verim Penceresi"

Yanma verimi, O₂ (fazla hava göstergesi) ve CO (eksik yanma göstergesi) arasındaki dengeye bağlıdır:

- **O₂ azaldıkça** (hava azaltıldıkça): Baca gazı kayıpları düşer, verim artar
- **O₂ çok düştüğünde:** CO aniden yükselir (CO breakthrough noktası) — eksik yanma başlar
- **Optimum nokta:** CO breakthrough'un hemen üzerinde, O₂'nin mümkün olan en düşük seviyede olduğu "verim penceresi"dir

```
         Verim (%)
           │          ┌──── Verim Penceresi ────┐
     97 ── │         ╱ ████████████████████ ╲
     96 ── │        ╱                        ╲
     95 ── │       ╱  (optimum O₂: %2-3)      ╲──── Fazla hava kaybı
     94 ── │      ╱                              ╲
     93 ── │  CO ╱                                 ╲
           │ ↑↑ ╱                                    ╲
           └──┴────────────────────────────────────────→ O₂ (%)
              0    1    2    3    4    5    6    7    8
```

### Brülör Bakımı ve Nozul Durumu

Brülör performansı zamanla aşağıdaki nedenlerle bozulur:
- **Nozul aşınması/kirlenmesi:** Yakıt sprey paternini bozar, karışım kalitesini düşürür
- **Hava damperinin kayması:** Mekanik titreşim ile hava damper pozisyonu değişir
- **Ateşleme elektrotları:** Aşınma ile kıvılcım mesafesi artar, ateşleme güçleşir
- **Alev dedektörü kirlenmesi:** Yanlış alev algılama, gereksiz duruşlar
- **Refrakter/yanma odası:** Aşınma ile alev geometrisi ve ısı transferi bozulur

## Yanma Analizi Parametreleri

### Baca Gazı Ölçüm Tablosu

| Parametre | Birim | Optimum (Doğalgaz) | Kötü | Aksiyon |
|-----------|-------|---------------------|------|---------|
| O₂ | % | 2-3 | >5 veya <1.5 | Hava damper pozisyonunu ayarla |
| CO | ppm | <50 | >200 | Hava artır, nozul/brülör kontrol et |
| CO₂ | % | 9-11 (doğalgaz) | <8 | Fazla hava azalt (O₂ ile birlikte değerlendir) |
| Baca gazı sıcaklığı | °C | 120-180 (kondansasyonsuz) | >250 | Isı transfer yüzeylerini temizle |
| İs sayısı (Smoke) | Bacharach | 0 (doğalgaz) | >0 | Hava artır, brülör/nozul kontrol |
| NOₓ | ppm | <80 (Low-NOₓ brülör) | >150 | Alev sıcaklığını düşür, FGR kontrol |
| Yanma verimi | % | >85 (net) / >92 (brüt) | <80 | Kapsamlı yanma ayarı gerekli |

### Yakıt Tipine Göre Optimum Değerler

| Yakıt | O₂ (%) | CO₂ (%) | Fazla Hava (%) | İs (Bacharach) |
|-------|--------|---------|----------------|----------------|
| Doğalgaz | 2-3 | 9-11 | 10-20 | 0 |
| LPG | 2-3 | 11-12 | 10-20 | 0 |
| Motorin (No.2) | 3-4 | 12-13 | 15-25 | 0-1 |
| Fuel Oil (No.6) | 3-5 | 13-15 | 15-30 | 1-3 |

## Hava/Yakıt Oranı Optimizasyonu

### Fazla Hava Eğrisi

Fazla hava artışının verime etkisi yaklaşık olarak:

```
Verim_kaybı ≈ 0.4% × (O₂_gerçek - O₂_optimum)   [her %1 fazla O₂ için ~%0.4 kayıp]
```

Örnek: O₂ seviyesi %6 ise (optimum %2.5 yerine):
- Fazla O₂: %3.5
- Tahmini verim kaybı: 0.4 × 3.5 = **%1.4**

### CO Breakthrough Noktası

- Hava kısıldıkça bir noktada CO birden yükselir — bu "breakthrough" noktasıdır
- Güvenli çalışma: CO breakthrough'un **en az %0.5-1 O₂** üzerinde kalınmalıdır
- Modülasyonlu brülörlerde her yük noktasında ayrı ayrı kontrol gerekir (düşük ateşte CO riski daha yüksek)

### Verimlilik Tepe Noktası

Verim, yetersiz hava ile fazla hava arasında bir tepe noktasına sahiptir:

| Bölge | O₂ | Durum | Verim Etkisi |
|-------|-----|-------|-------------|
| Yetersiz hava | <1.5% | CO yüksek, eksik yanma | Verim düşük + güvenlik riski |
| Optimum bant | 2-3% | CO düşük, minimum fazla hava | Maksimum verim |
| Orta fazla hava | 4-5% | CO sıfır, fazla hava kaybı başlar | Verimden %0.5-1 kayıp |
| Aşırı fazla hava | 6-8% | Baca gazı kayıpları belirgin | Verimden %1.5-3 kayıp |

## Brülör Bakımı

### Nozul Temizlik/Değişim Programı

| Yakıt Tipi | Temizlik Periyodu | Değişim Periyodu | Not |
|------------|-------------------|------------------|-----|
| Doğalgaz | 6-12 ay | 2-3 yıl | Gaz nozullarında karbon birikimi az |
| LPG | 6-12 ay | 2-3 yıl | Doğalgaza benzer |
| Motorin | 3-6 ay | 1-2 yıl | Karbon ve lak birikimi |
| Fuel Oil | 1-3 ay | 6-12 ay | Yoğun karbon, sülfür birikimi |

### Ateşleme Elektrot Durumu

- **Kontrol periyodu:** Her 6-12 ayda bir
- **Elektrot mesafesi:** Üretici spesifikasyonuna göre (tipik: 3-4 mm)
- **Aşınma belirtileri:** Ateşleme gecikmesi, ateşleme başarısızlığı (lockout), görsel olarak yuvarlaklaşma
- **Porseleni:** Çatlak veya karbon birikimi durumunda değiştir

### Alev Dedektörü Kalibrasyonu

- **UV dedektörler:** Yılda 1-2 kez lens temizliği ve sinyal seviyesi kontrolü
- **İyonizasyon dedektörleri:** Elektrot temizliği, mikro amper değeri kontrolü (tipik: >5 µA)
- **IR dedektörler:** Lens temizliği, filtre kontrolü
- **Sinyal seviyesi:** Üretici minimum değerinin en az 2 katı olmalı

### Alev Paterni / Kalite Görsel Kontrol

- Her brülör bakımında yanma odasını gözleme camından kontrol et
- Alev stabilitesi, simetrisi ve rengi değerlendir
- Refrakter duvarına çarpma veya geri tepme olup olmadığını kontrol et

## Alev Kalitesi

### İyi vs Kötü Alev Özellikleri

| Özellik | İyi Alev | Kötü Alev |
|---------|----------|-----------|
| Renk (doğalgaz) | Mavi-mor, hafif sarı uçlar | Sarı, turuncu, koyu |
| Renk (sıvı yakıt) | Parlak beyaz-sarı | Koyu turuncu, siyah uçlar |
| Şekil | Simetrik, kararlı, tanımlı | Asimetrik, sallanır, dağınık |
| Stabilite | Sabit, titreşimsiz | Titreşimli, sönme eğilimi |
| Uzunluk | Yanma odasıyla orantılı | Çok uzun (duvara çarpma) veya çok kısa |
| Ses | Düzenli, kararlı yanma sesi | Patlama sesleri, düzensiz gürültü |
| Koku | Yok (tam yanma) | Yakıt kokusu (eksik yanma) |

### Renk Göstergeleri (Doğalgaz)

- **Mavi:** İdeal — tam yanma, yeterli hava
- **Mavi + sarı uçlar:** Kabul edilebilir — çok az miktarda eksik yanma
- **Sarı:** Dikkat — karbon parçacıkları ışıma yapıyor, hava yetersiz olabilir
- **Turuncu/kırmızı:** Tehlike — ciddi eksik yanma, acil müdahale gerekli

## Uygulanabilirlik Kriterleri

### Yanma Ayarı Ne Zaman Gereklidir

- O₂ seviyesi optimum aralığın dışında (doğalgazda >%4 veya <%1.5)
- CO emisyonu >100 ppm
- Baca gazı sıcaklığı beklenenden yüksek
- Brülöre son 12 ayda bakım yapılmamış
- Yakıt tipi veya kalitesi değişmiş
- Kazan kapasitesi/yük profili önemli ölçüde değişmiş
- Yeni refrakter veya ısı transfer yüzeyi bakımı sonrası
- Mevsimsel sıcaklık değişimleri (hava yoğunluğu etkisi)

### Yanma Ayarı Uygulanamayacak Durumlar

- Brülör mekanik olarak arızalı (motor, fan, valf hasarı) — önce onarım gerekli
- Yakıt basıncı/kalitesi spesifikasyon dışı — önce yakıt sistemi düzelt
- Yanma odası refrakterleri ciddi hasarlı — önce onarım gerekli
- Baca çekişi yetersiz veya tıkalı — önce baca sistemi düzelt

## Yatırım Maliyeti

| Hizmet | Maliyet Aralığı | Açıklama |
|--------|----------------|----------|
| Tek seferlik profesyonel yanma ayarı | €500-2,000 | Kazan kapasitesine ve karmaşıklığa bağlı |
| Yıllık bakım sözleşmesi (2-4 ziyaret) | €1,000-5,000 | Düzenli yanma analizi + ayar + rapor |
| Taşınabilir yanma analizörü (tesis içi) | €2,000-8,000 | Testo, Bacharach, Kane marka cihazlar |
| Sürekli baca gazı izleme sistemi (CEMS) | €10,000-50,000 | Büyük kazanlar (>10 MW) için ekonomik |
| Brülör nozul seti değişimi | €100-1,000 | Yakıt tipine ve brülör kapasitesine bağlı |
| O₂ trim kontrol sistemi (otomatik) | €5,000-20,000 | Sürekli otomatik hava-yakıt oranı kontrolü |

## ROI Hesabı

### Formül

```
Verim_artışı_% = 0.4 × (O₂_mevcut - O₂_optimum)
Yıllık_yakıt_tasarrufu = Yıllık_yakıt_maliyeti × Verim_artışı_% / 100
Geri_ödeme_ay = Yatırım / (Yıllık_yakıt_tasarrufu / 12)
```

### Örnek Hesap

- 5 MW buhar kazanı, doğalgaz, 4,000 saat/yıl tam yükte eşdeğer çalışma
- Doğalgaz fiyatı: €0.045/kWh (€45/MWh)
- Mevcut O₂: %5.5, hedef O₂: %2.5 (3 puan iyileştirme)
- Mevcut yanma verimi: ~%88, beklenen: ~%89.2

**Hesap:**
```
Yıllık yakıt tüketimi = 5,000 kW × 4,000 saat / 0.88 = 22,727 MWh
Yıllık yakıt maliyeti = 22,727 × €45 = €1,022,727
Verim artışı = 0.4 × (5.5 - 2.5) = %1.2
Yıllık tasarruf = €1,022,727 × 1.2 / 100 = €12,273
Yanma ayarı maliyeti = €1,500
Geri ödeme = €1,500 / €12,273 = 0.12 yıl = **~1.5 ay**
```

## Uygulama Adımları

1. **Mevcut durum tespiti:** Taşınabilir yanma analizörü ile baca gazı ölçümü (O₂, CO, CO₂, baca sıcaklığı, is)
2. **Brülör görsel kontrolü:** Nozul, elektrot, alev dedektörü, hava damper durumu
3. **Alev kalitesi değerlendirmesi:** Gözlem camından alev rengi, şekli, stabilitesi
4. **Yük eğrisi boyunca ölçüm:** Düşük ateş, orta yük ve tam yükte ayrı ayrı ölçüm
5. **Hava damper/yakıt oranı ayarı:** Her yük noktasında O₂ ve CO hedeflerine göre ince ayar
6. **Nozul/elektrot bakımı:** Gerekirse temizlik veya değişim
7. **Otomatik kontrol kalibrasyonu:** O₂ trim sistemi varsa sensör kalibrasyonu ve setpoint ayarı
8. **Doğrulama ölçümü:** Ayar sonrası tüm yük noktalarında tekrar ölçüm ve kayıt
9. **Raporlama:** Önceki ve sonraki değerlerin karşılaştırmalı raporu
10. **Periyodik takip planı:** 3-6 ay sonra kontrol ölçümü planla

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| CO zehirlenmesi | Hava çok azaltılırsa CO seviyesi tehlikeli boyuta ulaşır | CO sürekli izleme, minimum O₂ alt sınırı belirle (>%1.5) |
| Yanmamış yakıt | Zengin karışımda yanmamış yakıt baca gazına karışır | CO ölçümü ile doğrulama, is testleri |
| Brülör geri tepmesi | Hava/yakıt oranı denge dışına çıkarsa alev kararsızlaşır | Alev dedektörü çalışır durumda olmalı, güvenlik kilitleri aktif |
| Termal stres | Ani ve büyük ayar değişiklikleri refrakter ve boruları strese sokar | Kademeli ayar yapılmalı, ani büyük değişikliklerden kaçın |
| NOₓ artışı | O₂ azaltıldıkça alev sıcaklığı artar, NOₓ yükselebilir | NOₓ emisyon limitlerini takip et, Low-NOₓ brülör tekniklerini uygula |
| Kondansasyon korozyonu | Baca gazı sıcaklığı çok düşürülürse asidik kondansasyon oluşur | Baca gazı sıcaklığını asit çiğ noktasının üzerinde tut (doğalgaz: >57°C, fuel oil: >130°C) |
| Ölçüm hatası | Kalibrasyon dışı analizör yanlış sonuç verir | Analizörü yılda 1 kez kalibre ettir, referans gazlarla kontrol |

## İlgili Dosyalar

- Kazan ekipman bilgisi: `equipment/boiler_steam.md`
- Kazan exergy formülleri: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer çözümü: `solutions/boiler_economizer.md`
- Kondens geri kazanımı: `solutions/boiler_condensate_recovery.md`
- Kazan izolasyon: `solutions/boiler_insulation.md`
- Buhar kaçak tespiti: `solutions/boiler_steam_leaks.md`

## Referanslar

- ASME PTC 4, "Fired Steam Generators — Performance Test Codes"
- DOE/AMO, "Improve Your Boiler's Combustion Efficiency" (Steam Tip Sheet #4)
- DOE/AMO, "Benchmark the Fuel Cost of Steam Generation"
- CIBO (Council of Industrial Boiler Owners), "Energy Efficiency Handbook"
- European Industrial Boiler Group (EIBG), "Best Available Techniques for Industrial Combustion"
- Testo AG, "Practical Guide to Combustion Analysis"
- Bacharach Inc., "Combustion Analysis Fundamentals"
- Cleaver-Brooks, "Boiler Efficiency Guide"
- ABMA (American Boiler Manufacturers Association), "Operating Guidelines for Firetube Boilers"
