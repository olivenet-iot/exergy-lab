# Çözüm: Chiller Sıralama Optimizasyonu — Chiller Sequencing Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Birden fazla chiller'ın bulunduğu tesislerde, kötü sıralama (sequencing) stratejisi enerji israfına yol açar. Gereğinden fazla chiller çalıştırma, yanlış chiller seçimi, yetersiz staging deadband'leri ve verim eğrilerinin göz ardı edilmesi yaygın sorunlardır. Tipik olarak operatörler alışkanlıkla aynı chiller'ı başlatır veya basit sıralı kontrol uygular — bu da toplam tesis verimini düşürür.

**Çözüm:** Chiller'ların verimlilik eğrilerine göre optimum start/stop sıralama stratejisi uygulamak. Yük durumuna göre en verimli chiller kombinasyonunu seçerek toplam tesis COP'unu maksimize etmek.

**Tipik Tasarruf:** %5-15 (chiller tesis enerji tüketiminde)
**Tipik ROI:** 0.5-2 yıl

## Çalışma Prensibi

Chiller sıralama optimizasyonu, birden fazla chiller'ın bulunduğu tesislerde toplam enerji tüketimini minimize etmeyi hedefler. Temel prensip: her yük koşulunda en verimli chiller kombinasyonunu çalıştırmaktır.

### Chiller Verim Eğrisi Karakteristikleri

Her chiller'ın COP'u yüke göre değişir:

| Chiller Tipi | Tam Yük COP | En İyi COP Yük Noktası | Minimum Yük Limiti | Kısmi Yük Davranışı |
|-------------|-------------|------------------------|--------------------|--------------------|
| Santrifüj (sabit hız) | 5.5-6.5 | %60-80 | %25-35 | Orta — IGV ile kapasite kontrolü |
| Santrifüj (VSD) | 5.5-6.5 | %40-60 | %10-20 | İyi — geniş verimli çalışma aralığı |
| Vidalı (sabit hız) | 4.5-5.5 | %70-90 | %20-30 | Düşük — slide valve ile verim düşer |
| Vidalı (VSD) | 4.5-5.5 | %50-70 | %15-25 | İyi — VSD ile kısmi yük verimi iyileşir |
| Scroll | 3.5-4.5 | %80-100 | %30-50 | Düşük — on/off veya kademeli kontrol |

### Neden Varsayılan Sıralama Verimsiz?

Tipik varsayılan sıralama sorunları:

1. **Sıralı start/stop:** Chiller 1 dolduğunda Chiller 2 başlar — ancak Chiller 2 daha verimli olabilir
2. **Eşit yük dağılımı:** Tüm chiller'lara eşit yük verilir — ancak bazı yük noktalarında tek chiller çalıştırmak daha verimlidir
3. **Yetersiz deadband:** Dar staging deadband'i sık start/stop'a (short cycling) yol açar
4. **Verim eğrisi göz ardı:** Farklı boyut/tip chiller'larda verim eğrileri farklıdır; en verimli kombinasyon hesaplanmaz

## Sıralama Stratejileri

### 1. Eşit Yük Dağılımı (Equal Loading)

Tüm çalışan chiller'lara eşit yük verilir:

```
Yük_chiller_i = Toplam_yük / Çalışan_chiller_sayısı
```

| Avantaj | Dezavantaj |
|---------|-----------|
| Basit kontrol | Her zaman en verimli değil |
| Eşit aşınma | Farklı boyut chiller'larda uygulanamaz |
| Öngörülebilir davranış | Verim eğrisi farklarını göz ardı eder |

### 2. Verimlilik Bazlı Yük Dağılımı (Efficiency-Based Loading)

Her chiller'a mevcut koşullarda en verimli olduğu yük verilir:

```
Minimize: Σ (Yük_i / COP_i(Yük_i))   (i = 1..n çalışan chiller)
Kısıt: Σ Yük_i = Toplam_yük
Kısıt: Yük_min_i ≤ Yük_i ≤ Yük_max_i
```

Burada:
- `Yük_i`: i. chiller'a atanan soğutma yükü [kW]
- `COP_i(Yük_i)`: i. chiller'ın ilgili yükteki COP değeri
- `Yük_min_i`: i. chiller'ın minimum yük limiti [kW]
- `Yük_max_i`: i. chiller'ın maximum kapasitesi [kW]

### 3. Staging Up/Down Stratejisi

Chiller ekleme (staging up) ve çıkarma (staging down) kararları:

```
Staging Up Koşulu:
  Tüm çalışan chiller'lar > %85-90 yükte VE
  Yük artış trendi > Eşik değer VE
  Bekleme süresi (deadband timer) dolmuş

Staging Down Koşulu:
  Bir chiller çıkarıldığında kalan chiller'lar < %80 yükte kalacaksa VE
  Yük azalma trendi > Eşik değer VE
  Bekleme süresi (deadband timer) dolmuş
```

### Staging Deadband Parametreleri

| Parametre | Tipik Değer | Açıklama |
|-----------|------------|----------|
| Staging up yük eşiği | %85-90 | Çalışan chiller'ların yük oranı |
| Staging down yük eşiği | %40-50 | Chiller çıkarma sonrası kalan yük oranı |
| Staging up bekleme süresi | 10-15 dakika | Short cycling önleme |
| Staging down bekleme süresi | 15-20 dakika | Short cycling önleme |
| Minimum çalışma süresi | 20-30 dakika | Kompresör koruması |
| Minimum bekleme süresi (stop sonrası) | 15-30 dakika | Kompresör ve motor koruması |
| Yük artış/azalış rampa hızı | %5-10/dakika | Ani yük değişimlerini filtrele |

## Minimum Yük Limitleri

Chiller'lar minimum yükün altında güvenle çalışamaz:

| Chiller Tipi | Minimum Yük (Sabit Hız) | Minimum Yük (VSD) | Altında Ne Olur |
|-------------|------------------------|-------------------|--------------------|
| Santrifüj | %25-35 | %10-20 | Surge riski, kararsız çalışma |
| Vidalı | %20-30 | %15-25 | Yağ dönüş problemi, verimsiz çalışma |
| Scroll | %30-50 | — | On/off geçiş, short cycling |
| Absorpsiyon | %25-40 | — | Kristalizasyon riski |

**Kritik:** Sıralama algoritması, hiçbir chiller'ı minimum yük limitinin altında çalıştırmamalıdır.

## Karışık Chiller Tesisi Optimizasyonu

Farklı boyut ve tipteki chiller'ların olduğu tesislerde sıralama daha karmaşıktır:

### Örnek Tesis: 3 Chiller Konfigürasyonu

| Chiller | Tip | Kapasite (kW) | Tam Yük COP | En İyi COP Yükü | VSD |
|---------|-----|---------------|-------------|------------------|-----|
| CH-1 | Santrifüj | 1,000 | 6.2 | %65 (650 kW) | Evet |
| CH-2 | Santrifüj | 1,000 | 6.0 | %75 (750 kW) | Hayır |
| CH-3 | Vidalı | 500 | 5.0 | %70 (350 kW) | Hayır |

**Toplam kapasite:** 2,500 kW

### Optimum Sıralama Tablosu

| Toplam Yük (kW) | Yük % | Optimum Kombinasyon | Yük Dağılımı | Tesis COP |
|-----------------|-------|--------------------|--------------| ----------|
| 0-200 | %0-8 | CH-1 (VSD) tek | 200 kW @ CH-1 | 5.8 |
| 200-650 | %8-26 | CH-1 (VSD) tek | Tümü CH-1 | 6.4 |
| 650-1,000 | %26-40 | CH-1 (VSD) tek | Tümü CH-1 | 6.0 |
| 1,000-1,350 | %40-54 | CH-1 + CH-3 | 850 kW CH-1 + 500 kW CH-3 | 5.7 |
| 1,350-2,000 | %54-80 | CH-1 + CH-2 | Eşit dağılım | 5.9 |
| 2,000-2,500 | %80-100 | CH-1 + CH-2 + CH-3 | Verim bazlı dağılım | 5.6 |

*Not: Gerçek optimizasyon üretici verim eğrileri ve anlık kondenser koşullarına göre yapılmalıdır.*

## Lead/Lag Rotasyonu

Eşit aşınma ve bakım dağılımı için chiller'lar sırayla lead (öncelikli) ve lag (ikincil) rolü üstlenir:

| Rotasyon Yöntemi | Açıklama | Avantaj |
|-----------------|----------|---------|
| Zaman bazlı | Her hafta/ay lead chiller değişir | Basit, öngörülebilir |
| Çalışma saati bazlı | En az çalışan chiller lead olur | Eşit aşınma |
| Verim bazlı | En verimli chiller her zaman lead | Minimum enerji tüketimi |
| Hibrit | Verim + çalışma saati kombinasyonu | Verimlilik + eşit aşınma dengesi |

### Çalışma Saati Dengeleme

```
Lead_chiller = MIN(Çalışma_saati_CH1, Çalışma_saati_CH2, ..., Çalışma_saati_CHn)
```

Burada:
- `Çalışma_saati_CHi`: i. chiller'ın kümülatif çalışma saati

**Deadband:** Çalışma saati farkı <100 saat ise rotasyon yapma (gereksiz geçişleri önle).

## BMS Entegrasyon Gereksinimleri

| Gereksinim | Açıklama | Önem |
|-----------|----------|------|
| Chiller COP verisi | Her chiller'ın anlık kW/ton veya COP değeri | Yüksek |
| Yük ölçümü | CHW debi × ΔT ile anlık soğutma yükü | Yüksek |
| Chiller durumu | Çalışıyor/durdu/arıza/bakımda | Yüksek |
| Kondenser suyu sıcaklığı | Her chiller için giriş/çıkış | Orta |
| CHW sıcaklıkları | Giriş/çıkış sıcaklıkları | Yüksek |
| Çalışma saati sayacı | Her chiller için kümülatif saat | Orta |
| Trend kayıt | En az 1 yıllık veri saklama | Orta |
| Alarm yönetimi | Short cycling, düşük COP, yüksek yük alarmları | Yüksek |

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Tesiste 2 veya daha fazla chiller varsa
- Mevcut sıralama sabit sıralı (fixed lead/lag) ise
- Chiller'lar farklı boyut veya tipteyse (karışık tesis)
- Yük profili geniş bir aralıkta değişiyorsa
- BMS chiller kontrolü yapabiliyorsa
- Chiller tesis enerji maliyeti >€15,000/yıl ise

### Ne Zaman Uygulanmamalı
- Tek chiller'lı tesislerde (sıralama anlamsız)
- Tüm chiller'lar aynı tip ve boyutta ve sürekli tam yükte çalışıyorsa
- BMS veya kontrol sistemi chiller sıralama kontrolü yapamıyorsa
- Chiller'lar bağımsız devrelere hizmet ediyorsa (ortak yük paylaşımı yok)

## Yatırım Maliyeti

| Kalem | Maliyet Aralığı (€) | Açıklama |
|-------|---------------------|----------|
| BMS sıralama algoritması programlama | 5,000-15,000 | Verim bazlı sıralama, staging mantığı |
| Enerji ölçüm ekipmanı (kW metreler) | 2,000-5,000 | Her chiller için güç ölçümü |
| CHW debimetre (yük hesabı) | 1,500-5,000 | Ultrasonik veya elektromanyetik |
| Sıcaklık sensörleri (CHW/CW giriş/çıkış) | 500-2,000 | Her chiller için 4 adet |
| Motorlu izolasyon vanaları | 2,000-8,000 | Her chiller için CHW/CW vanaları |
| Kontrol paneli güncelleme | 1,000-3,000 | Eski BMS sistemlerinde |
| Devreye alma ve optimizasyon | 2,000-5,000 | Test, ayar, performans doğrulama |
| **Toplam** | **12,000-25,000** | **2-4 chiller'lı tipik tesis** |

## ROI Hesabı

### Formül
```
Yıllık_enerji_mevcut = Σ (Yük_i × Saat_i) / COP_mevcut_ort
Yıllık_enerji_optimize = Σ (Yük_i × Saat_i) / COP_optimize_ort
Yıllık_tasarruf_kWh = Yıllık_enerji_mevcut - Yıllık_enerji_optimize
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

Burada:
- `Yük_i`: i. zaman dilimindeki soğutma yükü [kW]
- `Saat_i`: i. zaman diliminin süresi [saat]
- `COP_mevcut_ort`: Mevcut sıralama ile ağırlıklı ortalama COP
- `COP_optimize_ort`: Optimize sıralama ile ağırlıklı ortalama COP
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap
- 3 chiller'lı tesis (2×1,000 kW + 1×500 kW), toplam 2,500 kW
- Yıllık soğutma yükü: 4,500,000 kWh_t (soğutma)
- Mevcut sıralama COP (ağırlıklı ortalama): 4.8
- Optimize sıralama COP (ağırlıklı ortalama): 5.3
- Elektrik fiyatı: €0.12/kWh
- Yatırım: €18,000

```
Yıllık_enerji_mevcut = 4,500,000 / 4.8 = 937,500 kWh_e
Yıllık_enerji_optimize = 4,500,000 / 5.3 = 849,057 kWh_e
Yıllık_tasarruf = 937,500 - 849,057 = 88,443 kWh_e
Yıllık_tasarruf_EUR = 88,443 × 0.12 = €10,613/yıl
Geri_ödeme = 18,000 / 10,613 = 1.70 yıl
```

- **Geri ödeme süresi: ~1.7 yıl**

## Uygulama Adımları

1. **Mevcut durum analizi:** Her chiller'ın kapasitesi, tipi, yaşı, verim eğrisi ve mevcut çalışma saatlerini belirle. Mevcut sıralama stratejisini ve staging parametrelerini kaydet
2. **Yük profili ölçümü:** En az 1 aylık (tercihen mevsimsel) soğutma yükü profili ölç. Saatlik yük dağılımını, pik yükleri ve minimum yükleri belirle
3. **Verim eğrisi haritalama:** Her chiller için farklı yük noktalarında (25/50/75/100%) COP ölçümü yap. Üretici verilerini saha ölçümleri ile doğrula
4. **Optimum sıralama algoritması tasarımı:** Yük profiline ve verim eğrilerine göre her yük bölgesi için optimum chiller kombinasyonunu belirle. Staging up/down eşiklerini ve deadband'leri tanımla
5. **BMS programlama:** Sıralama algoritmasını BMS'te programla. Lead/lag rotasyon mantığını, minimum çalışma/bekleme sürelerini ve güvenlik kilitlelerini tanımla
6. **Motorlu vana ve enstrümantasyon kurulumu:** Gerekli izolasyon vanaları, debimetreler, güç ölçerler ve sıcaklık sensörlerini kur
7. **Kademeli devreye alma:** İlk aşamada mevcut sıralama ile paralel izleme yap. Optimize sıralamanın doğru çalıştığını doğruladıktan sonra aktif moda geç
8. **Performans izleme ve sürekli optimizasyon:** Aylık enerji raporları ile tasarrufu doğrula. Mevsimsel değişimlere göre staging parametrelerini ince ayarla

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Short cycling | Sık start/stop kompresör, motor ve starter'a zarar verir | Minimum çalışma süresi (20-30 dk), minimum bekleme süresi (15-30 dk), yeterli deadband |
| Yetersiz kapasite (fast load change) | Ani yük artışında staging up gecikmesi yetersiz soğutmaya yol açar | Hızlı yük artışı algılama, staging up bekleme süresini kısaltma, yedek kapasite marjı |
| Chiller arızasında acil staging | Çalışan chiller arızalandığında yedek chiller'ın hızla devreye girmesi gerekir | Otomatik arıza algılama ve acil staging, bekleme süresini bypass etme |
| Eşit olmayan aşınma | Verim bazlı sıralama en verimli chiller'ı sürekli çalıştırabilir | Çalışma saati dengeleme algoritması (verim + saat hibrit) |
| BMS iletişim arızası | BMS-chiller iletişimi kesilirse sıralama kontrolü kaybedilir | Manuel override imkanı, iletişim arızasında güvenli mod tanımla |
| Yanlış verim verisi | Güncel olmayan verim eğrileri yanlış sıralama kararına yol açar | Yıllık COP doğrulama ölçümü, verim eğrilerini güncelle |
| Hidrolik dengesizlik | Chiller start/stop'unda CHW debisinde ani değişiklik | Değişken debili primer sistemde bypass kontrolü, sıralı vana açma/kapama |
| Kısmi yük surge (santrifüj) | Düşük yükte çalışan sabit hızlı santrifüj chiller'da surge | Minimum yük limitini sıralama algoritmasına tanımla, staging down'da dikkat |

## İlgili Dosyalar
- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller VSD çözümü: `solutions/chiller_vsd.md`
- Kondenser optimizasyonu: `solutions/chiller_condenser_optimization.md`
- Soğutma suyu sıcaklık reset: `solutions/chiller_chilled_water_reset.md`
- Serbest soğutma: `solutions/chiller_free_cooling.md`
- Chiller exergy formülleri: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`

## Referanslar
- ASHRAE Handbook — HVAC Applications, "Supervisory Control Strategies and Optimization"
- ASHRAE Guideline 36, "High-Performance Sequences of Operation for HVAC Systems"
- ASHRAE Standard 90.1, "Energy Standard for Buildings Except Low-Rise Residential Buildings"
- Taylor, S.T., "Optimizing Design & Control of Chilled Water Plants," ASHRAE Journal
- Hartman, T., "All-Variable Speed Centrifugal Chiller Plants," ASHRAE Journal
- DOE/FEMP, "Chiller Management Best Practices"
- AHRI Standard 550/590, "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages"
- BSRIA, "Rules of Thumb — Guidelines for Building Services" 5th Edition
- Carrier/Trane/York, "Application Guide — Chiller Plant Design and Control"
