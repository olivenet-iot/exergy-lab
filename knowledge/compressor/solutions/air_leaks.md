# Çözüm: Basınçlı Hava Kaçak Tespiti ve Onarımı

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Tipik bir endüstriyel tesiste basınçlı hava üretiminin %20-30'u kaçaklar yoluyla kaybedilir. Bu, doğrudan enerji ve maliyet israfıdır.

**Çözüm:** Sistematik ultrasonik kaçak tespiti, onarımı ve sürekli kaçak yönetim programı.

**Tipik Tasarruf:** %10-25 toplam enerji tüketiminden
**Tipik ROI:** 3-12 ay

## Kaçak Oranları

| Tesis Durumu | Kaçak Oranı |
|-------------|-------------|
| Yeni tesis (ilk 2 yıl) | ~%5 |
| İyi bakımlı, aktif kaçak programı | %5-10 |
| Ortalama endüstriyel tesis | %20-30 |
| İhmal edilmiş tesis | %30-50 |

Bakımsız bir tesiste kaçak oranı her 2-5 yılda %20-30'a çıkar.

## Kaçak Maliyet Tablosu

### Delik Çapına Göre Yıllık Maliyet (7 bar gauge)

| Delik Çapı | Yaklaşık Eşdeğer | Kaçak Debisi (l/s FAD) | Kaçak Debisi (m³/min) | Yıllık Enerji (kWh)* | Yıllık Maliyet (€)* |
|------------|-------------------|----------------------|---------------------|---------------------|---------------------|
| 0.5 mm | İğne ucu | ~0.2 | 0.012 | 624 | ~€62 |
| 1 mm | — | ~0.8 | 0.048 | 2,496 | ~€250 |
| 2 mm | — | ~3.1 | 0.186 | 9,672 | ~€967 |
| 3 mm | ~1/8" | ~7.0 | 0.420 | 21,840 | ~€2,184 |
| 5 mm | ~1/4" | ~19.5 | 1.170 | 60,840 | ~€6,084 |
| 10 mm | ~3/8" | ~78.0 | 4.680 | 243,360 | ~€24,336 |

*Varsayımlar: 8,000 saat/yıl, SPC = 6.5 kW/(m³/min), €0.10/kWh

### Maliyet Formülü
```
Yıllık_maliyet = V̇_kaçak × SPC × çalışma_saati × elektrik_fiyatı

Burada:
- V̇_kaçak = kaçak debisi [m³/min FAD]
- SPC = spesifik güç tüketimi [kW/(m³/min)]
- çalışma_saati = basınçlı hava sistemi çalışma süresi [saat/yıl]
- elektrik_fiyatı [€/kWh]
```

### Basınç Etkisi
- 6 bar'da: Maliyetler ~%12-15 daha düşük
- 8 bar'da: Maliyetler ~%12-15 daha yüksek
- 10 bar'da: Maliyetler ~%35-40 daha yüksek

## Tespit Yöntemleri

### 1. Ultrasonik Kaçak Dedektörleri (El Tipi)

Kaçaktan çıkan türbülanslı akışın ürettiği ultrasonik sesi (38-42 kHz) tespit eder.

| Cihaz | Marka | Fiyat Aralığı | Özellik |
|-------|-------|---------------|---------|
| SDT 270/340 | SDT Ultrasound | €3,000-8,000 | Endüstriyel, veri kayıt, raporlama |
| Ultraprobe 15000 | UE Systems | €2,500-7,000 | Spektral analiz, yaygın kullanım |
| LKS1000 | Kaeser | €1,500-3,000 | Temel kaçak tespit |

**Avantajlar:** Gürültülü ortamda çalışır, ekonomik, basınçlı ve vakum sistemlerde kullanılabilir
**Dezavantajlar:** Manuel tarama gerektirir, büyük tesislerde zaman alıcı, operatör becerisine bağlı

### 2. Akustik Görüntüleme Kameraları

MEMS mikrofon dizisi (32-128 adet) ile ses haritası oluşturur, gerçek zamanlı görsel olarak kaçak noktalarını gösterir.

| Cihaz | Marka | Mikrofon Sayısı | Fiyat Aralığı | Özellik |
|-------|-------|----------------|---------------|---------|
| ii900 | Fluke | 64 | €15,000-20,000 | Görsel bindirme, pratik |
| ii910 | Fluke | 64 | €25,000-35,000 | Yüksek hassasiyet, geniş alan |
| Si124-LD | FLIR | 124 | €25,000-40,000 | Otomatik kaçak boyutu tahmini, bulut analitik |
| Ultra Pro | Distran | 112 | €30,000-45,000 | Yüksek hassasiyet |

**Avantajlar:** El tipine göre 5-10 kat daha hızlı tarama, mesafeden tespit (5-10 m), düşük operatör bağımlılığı, fotoğraflı dokümantasyon
**Dezavantajlar:** Yüksek ilk yatırım

### 3. Sabun/Köpük Testi

Şüpheli noktalara sabun solüsyonu uygulanır, kabarcık oluşumu kaçak gösterir.
- **Avantaj:** Çok düşük maliyet, kesin doğrulama
- **Dezavantaj:** Çok yavaş, yalnızca erişilebilir ve görünür bağlantılarda

## Yaygın Kaçak Noktaları (Sıklık Sırasına Göre)

| Sıra | Kaçak Noktası | Toplam Kaçaklar İçindeki Oran |
|------|-------------|------------------------------|
| 1 | Quick-connect bağlantılar (hızlı kaplinler) | %30-35 |
| 2 | Hortum bağlantıları ve yıpranan hortumlar | %15-20 |
| 3 | Dişli boru bağlantıları | %10-15 |
| 4 | Vanalar (küresel, piston, selenoid) | %5-10 |
| 5 | Basınç regülatörleri / FRL üniteleri | %5-10 |
| 6 | Silindir piston/rot contaları | %5-10 |
| 7 | Filtre gövdesi O-ring'leri | %3-5 |
| 8 | Kondansat drenajları (açık kalan) | %3-5 |
| 9 | Flanş bağlantıları | %2-3 |
| 10 | Kullanılmayan ekipman (basınçlı bırakılan) | Değişken |

## Onarım Maliyetleri

| Onarım Tipi | Malzeme Maliyeti (€) | Süre | Not |
|-------------|---------------------|------|-----|
| Bağlantı sıkma | 0 (işçilik) | 2-5 dk | En yaygın, ücretsiz |
| Teflon bant/macun yenileme | €2-10 | 10-20 dk | Dişli bağlantılar |
| Hortum kelepçesi değişimi | €1-5 | 5-10 dk | |
| Quick-connect değişimi | €5-25 | 10-15 dk | Kaliteli ürün tercih edin |
| O-ring değişimi | €2-15 | 15-30 dk | |
| Silindir conta seti | €20-100 | 30-120 dk | Boyuta bağlı |
| Regülatör diyafram değişimi | €15-50 | 20-45 dk | |
| Vana değişimi | €20-200 | 30-60 dk | Boyut ve tipe bağlı |
| Hortum bölüm değişimi | €10-50 | 15-45 dk | |
| Boru onarımı | €50-300 | 1-4 saat | Kapatma gerekebilir |
| Kondansat drenaj değişimi | €50-500 | 30-120 dk | No-loss: €200-500 |

**Ortalama onarım maliyeti kaçak başına:** €10-30 (çoğunluk basit sıkma veya conta)

## ROI Hesabı

### Formül
```
Yıllık_tasarruf = Yıllık_enerji_maliyeti × (Mevcut_kaçak% - Hedef_kaçak%) / 100
Geri_ödeme = (Tespit_maliyeti + Onarım_maliyeti) / Yıllık_tasarruf
```

### Örnek Hesap
- 100 kW kompresör, 6,000 saat/yıl, €0.12/kWh
- Yıllık enerji maliyeti: 100 × 6,000 × 0.12 = €72,000
- Mevcut kaçak: %25 → Hedef: %10 → Azaltma: %15
- Yıllık tasarruf: %15 × €72,000 = €10,800
- Tespit + onarım maliyeti: €5,000
- **Geri ödeme: €5,000 / €10,800 = 5.6 ay**

## Kaçak Yönetim Programı

### Adım 1: İlk Kapsamlı Tarama
- Tüm sistemi sistematik olarak tara (kompresör odasından başla, ana hat → branş hatları)
- Her kaçağı numaralı etiketle işaretle
- Fotoğrafla, konumu ve tahmini boyutunu kaydet

### Adım 2: Önceliklendirme
- 80/20 kuralı: Kaçakların %20'si toplam kaybın %80'ini oluşturur
- Büyük kaçakları öncelikli onar
- Güvenlik riski olan kaçaklar en öncelikli

### Adım 3: Onarım
- Üretim planına göre onarım planla
- Mümkünse anında onar (basit sıkma, conta değişimi)
- Kapatma gerektiren onarımları programlı duruşlara planla

### Adım 4: Doğrulama
- Onarım sonrası kaçağın durduğunu doğrula
- Sistem basıncı ve kompresör yükünü izle

### Adım 5: Düzenli Tarama Programı
- Minimum: 6-12 ayda bir kapsamlı tarama
- En iyi uygulama: 3 ayda bir kritik alanlar
- İdeal: Sabit ultrasonik sensörlerle sürekli izleme

### Adım 6: KPI Takibi
- Bulunan / onarılan kaçak sayısı
- Tahmini kaçak debisi (toplam üretimin %'si olarak)
- Spesifik güç trendi
- Sistem basınç kararlılığı

### Adım 7: Önleyici Tedbirler
- Kaliteli bağlantı elemanları ve kaplinler kullan
- Kullanılmayan hatları izole et (kesme vanası kapat)
- Her makine için kesme vanası kur
- Üretim dışı saatlerde bölgesel basınç kapatma
- Operatörleri kaçak farkındalığı konusunda eğit

### Hedef
- Yıllık hedef: Kaçak oranını <%10'da tut (en iyi uygulama: <%5)

## Sistem Toplam Kaçak Tespiti

### Tank Düşürme Testi
Üretim dışı saatlerde tüm tüketicileri kapat, kompresörü durdur:
```
V̇_kaçak = V_sistem × (P_başlangıç - P_bitiş) / (t × P_atm)   [m³/min]
Kaçak% = V̇_kaçak / V̇_toplam_üretim × 100
```

### Yük/Boşta Zamanlaması
Üretim dışı saatlerde kompresörü çalıştır:
```
Kaçak% = [T_yüklü / (T_yüklü + T_boşta)] × 100
```

## İlgili Dosyalar
- Benchmark verileri: `benchmarks/compressor_benchmarks.md` (Bölüm 4: Kaçak Oranları)
- Exergy kaçak formülü: `formulas/compressor_exergy.md` (Bölüm 5)
- Audit metodolojisi: `methodology/compressed_air_audit.md`
- Basınç optimizasyonu: `solutions/compressor_pressure_optimization.md`

## Referanslar
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- DOE Compressed Air Tip Sheet #3, "Minimize Compressed Air Leaks"
- Carbon Trust, "Compressed Air — Opportunities for Businesses" (CTG027)
- SDT International, Leak Quantification Methodology
- Fluke, ii900/ii910 Acoustic Imaging Camera Technical Documentation
- FLIR, Si124-LD Product Documentation
