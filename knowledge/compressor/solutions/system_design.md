# Çözüm: Basınçlı Hava Sistem Tasarımı İyileştirmeleri

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Yetersiz tank boyutu, dar borular, ölü uçlu dağıtım, timer drenaj ve koordinasyonsuz çoklu kompresör kontrolü büyük enerji israfına neden olur.

**Çözüm:** Tank boyutlandırma, boru ağı optimizasyonu, ring main dağıtım, no-loss drenaj ve master controller uygulaması.

**Tipik Tasarruf:** %5-15
**Tipik ROI:** 1-3 yıl

## 1. Tank (Receiver) Boyutlandırma

### Islak Tank (Wet Receiver) — Kompresör ile Kurutucu Arası

**Amacı:** Pulsasyonları yumuşatır, ilk soğutma ve kondansat ayrımı sağlar, kısa süreli pik talepleri tamponlar.

#### Load/Unload Kompresör İçin Boyutlandırma
```
V (litre) = (Q × 60) / (N × (P_üst - P_alt))

Burada:
- Q = kompresör kapasitesi [l/s FAD]
- N = izin verilen yük/boşta döngüsü/saat (maks 10-12, tercih 6-8)
- P_üst = yükleme basıncı [bar mutlak]
- P_alt = boşaltma basıncı [bar mutlak]
```

**Pratik kural:** 5-10 litre depolama / (l/s kompresör kapasitesi)

**Örnek:** 75 kW kompresör, 200 l/s FAD, 7.0-7.5 bar arası çalışma:
```
V = (200 × 60) / (10 × (8.5 - 8.0)) = 12,000 / 5 = 2,400 litre
Önerilen: 2,000-3,000 litre (2-3 m³)
```

#### VSD Kompresör İçin
- VSD hız ayarlayarak debiyi talebe eşler → daha az depolama gerekli
- **Pratik kural:** 2-5 litre / (l/s kompresör kapasitesi) (sabit hızın yaklaşık yarısı)

#### Flow Controller Olan Sistem İçin
- Ek depolama: 10-20 litre / (l/s sistem kapasitesi)
- Kompresör ile flow controller arası konumlandırılır

### Kuru Tank (Dry Receiver) — Kurutucu Sonrası

**Amacı:** Arıtılmış havayı büyük/değişken talep noktalarına yakın depolar.
- Boyut: Islak tankın %50-100'ü
- Pik talep noktasına yakın konumlandır
- Hesap: `V = Q_pik × T_olay / ΔP`

## 2. Boru Tasarımı

### Boru Hızı Kuralı

| Boru Bölümü | Maks Hız |
|-------------|---------|
| Ana hat (header) | 6 m/s |
| Branş hatları | 10-15 m/s |
| Düşme boruları (drops) | 15-20 m/s |

### Boru Çapı Hesabı
```
d = √(4 × Q_actual / (π × v_max))

Burada:
- Q_actual = hat basıncındaki gerçek debi [m³/s] = Q_FAD × (P_atm / P_hat_mutlak)
- v_max = izin verilen maksimum hız [m/s]
```

### Pratik Boru Boyutlandırma Tablosu (7 bar, ana hat, 6 m/s)

| Debi (m³/min FAD) | Kompresör Gücü | Min Boru İç Çapı (mm) | Önerilen Anma Çapı |
|-------------------|----------------|----------------------|-------------------|
| 0.5 | ~4 kW | 20 | DN 25 (1") |
| 1.0 | ~7.5 kW | 28 | DN 32 (1¼") |
| 2.0 | ~15 kW | 39 | DN 40 (1½") |
| 3.5 | ~22 kW | 51 | DN 50 (2") |
| 6.0 | ~37 kW | 67 | DN 80 (3") |
| 10.0 | ~55 kW | 86 | DN 100 (4") |
| 16.0 | ~90 kW | 109 | DN 125 (5") |
| 25.0 | ~160 kW | 136 | DN 150 (6") |

**Kural:** Her zaman bir üst standart boru çapını seçin. Boru maliyeti yaşam döngüsü maliyetinin %1-3'üdür; yetersiz boru ömür boyu enerji israf eder.

### Ring (Halka) vs Lineer Dağıtım

#### Ring Main (Halka Hat) — Kesinlikle Önerilen
- Ana hat tesisin çevresinde kapalı döngü oluşturur
- Hava her noktaya iki yönden ulaşır → efektif boru kesiti 2 katına çıkar
- Basınç düşüşü lineer sisteme göre ~%50 daha az
- Tüm kullanım noktalarında daha kararlı basınç

#### Lineer (Ölü Uçlu) — Kaçınılmalı
- Hava tek yönden akar
- Hat sonundaki kullanıcılar en yüksek basınç düşüşünü yaşar
- Sadece çok küçük sistemlerde veya tek hatlı uygulamalarda kabul edilebilir

### Basınç Düşüşü

**Hedef toplam sistem basınç düşüşü:** <1.0 bar (en iyi uygulama: <0.5 bar)

| Bileşen | Tipik ΔP |
|---------|---------|
| Aftercooler + Kurutucu + Filtreler | 0.2-0.4 bar |
| Ana hat borulama | 0.05-0.15 bar |
| Branş hatları | 0.05-0.1 bar |
| FRL (kullanım noktası) | 0.1-0.3 bar |
| **Toplam** | **0.4-1.0 bar** |

#### Fitting Eşdeğer Uzunlukları

| Fitting | Eşdeğer Uzunluk (× boru çapı) |
|---------|-------------------------------|
| 90° dirsek (standart) | 30 |
| 90° dirsek (uzun radius) | 16 |
| 45° dirsek | 16 |
| T (düz geçiş) | 20 |
| T (branş çıkışı) | 60 |
| Küresel vana (açık) | 3 |
| Sürgülü vana (açık) | 7 |
| Glob vana (açık) | 340 |
| Çek valf | 135 |

**Uyarı:** Glob vanalar basınçlı hava sistemlerinde çok yüksek basınç düşüşü nedeniyle kullanılmamalıdır.

## 3. Kondansat Drenaj

### Timer Drenaj — Kaçınılmalı
- Belirlenen aralıklarla açılır (örn. 5 sn / 10 dk)
- **Sorun:** Her açılışta sıkıştırılmış hava kaybedilir (kondansat olsun veya olmasın)
- Tahmini kayıp: Sistem debisinin %1-5'i
- Maliyet: €50-200/adet

### Demand (Float/Level) Drenaj
- Kondansat seviye sensörü ile tetiklenir
- Timer'a göre daha az hava kaybı
- Maliyet: €100-400/adet

### No-Loss Drenaj (Sıfır Hava Kaybı) — Önerilen
- Kondansat varken açılır, hava kaçırmadan kapatılır
- Hemen hemen sıfır basınçlı hava kaybı
- Maliyet: €200-600/adet
- **Ürünler:** BEKO BEKOMAT (12/14/16/20/32/33 serisi), Jorc Puro, Kaeser ECO-DRAIN, Atlas Copco EWD serisi

### Timer → No-Loss Değişimi ROI
- Timer drenaj hava kaybı: ~0.025-0.067 l/s sürekli (her bir drenaj)
- Yıllık maliyet/drenaj: ~€50-200
- 10 drenaj noktası: €500-2,000/yıl israf
- No-loss yatırım: 10 × €400 = €4,000
- **Geri ödeme: 2-4 yıl** (+ bakım kolaylığı)

## 4. Master Controller (Çoklu Kompresör Sıralaması)

### Sorun
Koordinasyonsuz çoklu kompresörler:
- Birden fazla makine kısmi yükte çalışır
- Kaskad basınç bantları → geniş basınç salınımı
- Yüksek ortalama basınç = daha fazla enerji

### Master Controller Faydaları
- En verimli kompresör kombinasyonunu otomatik seçer
- Kısmi yükte çalışan makine sayısını minimize eder
- Basınç bandını daraltır (0.3-0.5 bar, kaskat'ta 1.0-1.5 bar)
- Düşük ortalama basınç = ek enerji tasarrufu
- Tipik tasarruf: %5-12

### Ürünler

| Controller | Üretici | Kapasite | Fiyat |
|-----------|---------|---------|-------|
| Optimizer 4.0 | Atlas Copco | 6 kompresör + kurutucu | €5,000-15,000 |
| SAM 4.0 | Kaeser | 16 kompresör, 3D kontrol | €8,000-20,000 |
| AirConnect | Gardner Denver | Çoklu kompresör, bulut | €5,000-12,000 |
| ES16 | Çeşitli | Karma marka kurulumlar | €3,000-10,000 |
| Air Optimizer | ABB | ABB sürücü entegrasyonu | €10,000-25,000 |

### En İyi Uygulama Tasarımı
1. Sabit hızlı kompresörler → baz yük (%100 yükte en verimli)
2. VSD kompresör → trim (değişken talep karşılama)
3. Master controller → her an yalnızca bir kompresör kısmi yükte
4. Basınç bandı: 0.3-0.5 bar (mümkün olan en dar)

## 5. Boru Malzemesi Seçimi

| Malzeme | Avantajlar | Dezavantajlar | Maliyet |
|---------|-----------|---------------|---------|
| Alüminyum (push-fit) | Korozyon yok, hızlı montaj, düşük sürtünme | Yüksek ilk maliyet | Yüksek |
| Paslanmaz çelik | Korozyon yok, uzun ömür | Yüksek maliyet, zor montaj | Çok yüksek |
| Galvanizli çelik | Yaygın, ekonomik | Zamanla korozyon, toz/kir | Orta |
| Siyah çelik | Ekonomik | Korozyon, pas parçacıkları | Düşük |
| Plastik (PE, PP) | Korozyon yok, hafif | Basınç/sıcaklık sınırları | Orta |
| Bakır | Korozyon dayanımı, kolay montaj | Maliyet, küçük çaplar | Orta-Yüksek |

**Önerilen:** Yeni tesislerde alüminyum push-fit sistemler (hızlı montaj, sıfır korozyon, düşük basınç düşüşü). Maliyet farkı, uzun vadede bakım ve enerji tasarrufu ile karşılanır.

## İlgili Dosyalar
- Basınç optimizasyonu: `solutions/compressor_pressure_optimization.md`
- VSD: `solutions/compressor_vsd.md`
- Sistem genel bakış: `equipment/compressed_air_systems.md`
- Benchmark: `benchmarks/compressor_benchmarks.md`

## Referanslar
- Compressed Air Challenge, "Best Practices" — Distribution and Controls Chapters
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- CAGI, "Selection Guide for Compressed Air Dryers and Filters"
- Atlas Copco, "Compressed Air Manual" — Piping and Storage Chapter
- BEKO Technologies, "Condensate Management" Documentation
