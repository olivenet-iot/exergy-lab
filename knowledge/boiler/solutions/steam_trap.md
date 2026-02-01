# Buhar Kapanı Yönetimi — Steam Trap Management

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Arızalı buhar kapanları (steam trap) canlı buharın doğrudan kondansat hattına kaçmasına neden olur. Bakımsız sistemlerde kapanların %15-25'i arızalıdır ve toplam buhar üretiminin %5-15'i bu yolla kaybedilir.

**Çözüm:** Sistematik buhar kapanı survey (tarama) ve onarım programı. Ultrasonik test, sıcaklık ölçümü ve görsel muayene ile arızalı kapanların tespiti ve zamanında değiştirilmesi.

**Tipik Tasarruf:** %5-15 (bakımsız sistemlerde)
**Tipik ROI:** <0.5 yıl

## Steam Trap Tipleri

Buhar kapanları, buhar hatlarından kondansatı (yoğuşan su) ve hava gibi yoğuşmayan gazları otomatik olarak tahliye ederken canlı buharın geçişini engeller. Üç ana mekanizma kullanılır:

### 1. Termodinamik Kapanlar (Thermodynamic Disc)

Buhar ve kondansat arasındaki hız ve basınç farkından yararlanarak çalışır. Disk elemanlı yapıdadır.

- **Çalışma prensibi:** Kondansat geldiğinde diski kaldırır ve geçer; buhar geldiğinde yüksek hız düşük basınç yaratarak diski oturtur
- **Avantajlar:** Kompakt, ucuz, hareketli parçası az, dondurma dayanıklı, yüksek basınç ve sıcaklığa uygun
- **Dezavantajlar:** Gürültülü çalışır, süperheat buharda performans düşer, düşük basınçta zayıf, karşı basınca duyarlı
- **Tipik uygulama:** Ana buhar hatları, tracer hatları, drip noktaları
- **Basınç aralığı:** 0.5-42 bar
- **Ömür beklentisi:** 3-5 yıl (orta)

### 2. Termostatik Kapanlar (Thermostatic)

Buhar ile kondansat arasındaki sıcaklık farkını algılayan bir termal eleman kullanır.

#### a) Dengeli Basınç Termostatik (Balanced Pressure)
- Sıvı dolgulu kapsül, buhar sıcaklığında genleşerek vanayı kapatır
- Kondansat biraz soğuduğunda (~15-25 °C subcooling) kapsül büzülür ve vana açılır
- **Uygulamalar:** Isı eşanjörleri, tracer hatları, proses ekipmanları

#### b) Bimetalik (Bimetallic)
- Farklı genleşme katsayılı iki metal şerit sıcaklıkla bükülür
- Daha dayanıklı, daha yüksek subcooling (~30-50 °C)
- **Uygulamalar:** Yüksek basınç superheated buhar hatları, drip noktaları

- **Avantajlar:** Hava tahliyesi mükemmel, kompakt, enerji verimli, düşük maliyet
- **Dezavantajlar:** Subcooling gerektirir (kondansat birikimi), su darbelerine duyarlı, ani yük değişimlerine yavaş yanıt
- **Basınç aralığı:** 0.5-40 bar
- **Ömür beklentisi:** 3-7 yıl

### 3. Mekanik Kapanlar (Mechanical)

Buhar ile kondansat arasındaki yoğunluk farkından yararlanarak çalışır. Yüzer (float) mekanizması kullanır.

#### a) Float & Thermostatic (F&T)
- Küresel şamandıra kondansat seviyesiyle yükselir ve düşer
- Termostatik hava tahliye elemanı ile birlikte çalışır
- Sürekli ve değişken debili kondansat tahliyesine en uygun tip
- **Uygulamalar:** Isı eşanjörleri, buhar kazanları, proses ekipmanları, klimatizasyon üniteleri

#### b) Ters Kova (Inverted Bucket)
- Ters çevrilmiş kova buharla yüzer (kapalı), kondansatla batar (açık)
- Sağlam ve güvenilir mekanizma
- **Uygulamalar:** Ana buhar hatları, yüksek basınç sistemleri, proses ekipmanları

- **Avantajlar:** Sürekli kondansat tahliyesi (F&T), yüksek kapasite, su darbesine dayanıklı (ters kova), düşük subcooling
- **Dezavantajlar:** Büyük boyutlu, yüksek maliyet, donma riski (F&T), buhar kilidi riski (ters kova)
- **Basınç aralığı:** 0.5-80 bar (ters kova: 175 bar'a kadar)
- **Ömür beklentisi:** 5-10 yıl

### Tip Karşılaştırma Tablosu

| Özellik | Termodinamik | Termostatik (Dengeli) | Termostatik (Bimetalik) | F&T | Ters Kova |
|---------|-------------|----------------------|------------------------|-----|-----------|
| Hava tahliyesi | Zayıf | Mükemmel | İyi | İyi (ek eleman) | Sınırlı |
| Subcooling | Yok | 15-25 °C | 30-50 °C | ~0 °C | ~0 °C |
| Buhar kaçak riski | Orta | Düşük | Düşük | Düşük | Düşük |
| Su darbesi dayanımı | İyi | Zayıf | Orta | Orta | İyi |
| Karşı basınç toleransı | Düşük (<%50) | Yüksek | Yüksek | Yüksek | Orta (%80) |
| Superheated buhar | Zayıf | Uyumsuz | İyi | Uyumsuz | İyi |
| Boyut | Küçük | Küçük | Küçük-orta | Büyük | Orta-büyük |
| Göreceli maliyet | Düşük | Düşük-orta | Orta | Yüksek | Orta-yüksek |
| Tipik ömür | 3-5 yıl | 3-5 yıl | 5-7 yıl | 5-10 yıl | 7-10 yıl |
| Arıza modu | Açık kalma | Açık/kapalı | Açık/kapalı | Açık kalma | Açık kalma |

## Arıza Modları (Failure Modes)

### 1. Açık Kalma (Stuck Open / Failed Open) — En Maliyetli

Kapan sürekli açık kalır ve canlı buhar doğrudan kondansat hattına geçer.

- **Belirtiler:** Kondansat hattı aşırı sıcak, flash buhar aşırı, kondansat tankı basıncı yüksek
- **Nedenleri:** Aşınma, erozyon, kir/tortu birikimi, mekanik hasar, yanlış boyutlandırma
- **Enerji kaybı:** Trap boyutuna ve basınca bağlı olarak 25-500+ kg/h buhar kaybı
- **Maliyet etkisi:** Tek bir açık kalmış büyük kapan yılda €5,000-50,000+ kayba neden olabilir

### 2. Kapalı Kalma (Stuck Closed / Failed Closed)

Kapan kapalı kalır, kondansat tahliye edilemez ve sistemde birikir.

- **Belirtiler:** Isıtma kapasitesinde düşüş, su darbesi (water hammer), ekipman korozyonu, eşanjör performans kaybı
- **Nedenleri:** Kir birikimi, korozyon ürünleri, yanlış montaj, aşırı karşı basınç
- **Enerji kaybı:** Doğrudan buhar kaybı yoktur ancak ısı transferi verimsizliği ve ekipman hasarı oluşur
- **Güvenlik riski:** Su darbesi boru yırtılmasına ve ciddi yaralanmalara neden olabilir

### 3. Aralıklı Arıza (Intermittent Failure)

Kapan zaman zaman düzgün çalışır, zaman zaman buhar kaçırır veya kondansat biriktir.

- **Tespit zorluğu:** Anlık test yanıltıcı olabilir, tekrarlı veya uzun süreli izleme gerektirir
- **Nedenleri:** Kısmen aşınmış iç parçalar, düzensiz yük koşulları, uygun olmayan tip seçimi

### Tipik Arıza Oranları

| Bakım Durumu | Arıza Oranı | Açıklama |
|-------------|-------------|----------|
| İyi bakımlı (yıllık survey + zamanında onarım) | <%5 | Düzenli test ve proaktif değişim |
| Ortalama bakım (2-3 yılda bir survey) | %10-15 | Tipik endüstriyel tesis |
| Zayıf bakım (survey yok veya düzensiz) | %15-25 | Yaygın durum, ciddi kayıplar |
| İhmal edilmiş (hiç bakım yapılmamış) | %25-40 | Çok yüksek enerji kaybı |

**Genel kural:** Survey yapılmayan sistemlerde arıza oranı her yıl yaklaşık %5-7 artar.

## Test Yöntemleri

### 1. Ultrasonik Test

Buhar kapanından geçen akışın ultrasonik frekans bileşenlerini tespit eder. En yaygın ve güvenilir yöntemdir.

- **Prensip:** Buhar geçişi yüksek frekanslı (>20 kHz) titreşim üretir; kondansat geçişi daha düşük frekanslı ses üretir
- **Ekipman:** SDT 270/340, UE Ultraprobe 15000, CTRL UL101
- **Avantajlar:** Gürültülü ortamda çalışır, nicel veri sağlar, trendi izleme imkanı, operasyonda test edilir
- **Dezavantajlar:** Deneyimli operatör gerektirir, yorumlama becerisi önemli
- **Doğruluk:** %85-95 (deneyimli operatör ile)
- **Hız:** Trap başına 2-5 dakika

### 2. Sıcaklık Ölçümü (Infrared / Kızılötesi)

Kapan giriş ve çıkış sıcaklıkları arasındaki farkı değerlendirir.

- **Prensip:** Normal çalışan kapanda giriş buhar sıcaklığı, çıkış daha düşük; açık kalmışsa her iki taraf da yaklaşık buhar sıcaklığında
- **Ekipman:** El tipi IR termometre, termal kamera (FLIR, Fluke Ti)
- **Referans değerler:**
  - Normal: Giriş ≈ buhar sıcaklığı, Çıkış < buhar sıcaklığı (subcooling kadar)
  - Açık kalmış: Giriş ≈ Çıkış ≈ buhar sıcaklığı
  - Kapalı kalmış: Çıkış sıcaklığı ortam sıcaklığına yakın
- **Avantajlar:** Hızlı, temassız, görsel kanıt (termal kamera)
- **Dezavantajlar:** Ortam koşullarından etkilenir, yalıtımlı hatlarda güçlük, kesinliği ultrasonikten düşük
- **Doğruluk:** %70-85

### 3. Görsel Muayene (Sight Glass / Gözetleme Camı)

Kapan çıkışına monte edilen sight glass ile akış gözlemlenir.

- **Prensip:** Kondansat berrak akar, buhar beyaz bulut/sis oluşturur
- **Avantajlar:** Kesin sonuç, anlık gözlem, düşük maliyet
- **Dezavantajlar:** Her trap'a sight glass monte etmek gerekir, flash buhar ile canlı buhar karıştırılabilir
- **Not:** Flash buhar (kondansatın düşük basınçta buharlaşması) normaldir; canlı buhar sürekli ve yoğun bir akış gösterir

### 4. Akustik Görüntüleme Kameraları

Ultrasonik mikrofon dizisi ile ses haritası oluşturur.

- **Ekipman:** Fluke ii910, FLIR Si124, Distran Ultra Pro
- **Avantajlar:** Hızlı tarama, mesafeden tespit, görsel belgeleme, düşük operatör bağımlılığı
- **Dezavantajlar:** Yüksek yatırım maliyeti (€15,000-45,000), buhar ve kondansat akışını ayırt etmek için deneyim gerekir
- **Hız:** Trap başına 30-60 saniye

### Test Yöntemi Karşılaştırması

| Yöntem | Doğruluk | Hız | Maliyet | Deneyim Gereksinimi |
|--------|----------|-----|---------|---------------------|
| Ultrasonik | %85-95 | Orta | Düşük-orta | Yüksek |
| Infrared | %70-85 | Hızlı | Düşük | Orta |
| Sight glass | %90-98 | Anlık | Düşük (montaj gerekir) | Düşük |
| Akustik kamera | %80-90 | Çok hızlı | Yüksek | Orta |

**En iyi uygulama:** Ultrasonik + infrared kombinasyonu en güvenilir sonucu verir.

## Arızalı Trap Maliyet Hesabı

### Orifis Formülü ile Buhar Kaybı

```
Steam_loss_kg/h = C × A × P (orifice formula)

Burada:
- C = akış katsayısı (discharge coefficient, tipik 0.6-0.9)
- A = orifis alanı [m²]
- P = buhar basıncı [bar gauge]

Basitleştirilmiş yaklaşım (Spirax Sarco):
Steam_loss_kg/h = 0.0929 × d² × (P + 1.013)

Burada:
- d = orifis çapı [mm]
- P = manometre basıncı [bar gauge]

Annual_cost = steam_loss_kg/h × annual_hours × steam_cost_per_kg
```

### Trap Boyutu ve Arıza Moduna Göre Tipik Buhar Kaybı

| Trap Bağlantı Boyutu | Orifis Çapı (mm) | Buhar Kaybı @ 5 bar (kg/h) | Buhar Kaybı @ 10 bar (kg/h) | Buhar Kaybı @ 15 bar (kg/h) | Yıllık Maliyet @ 10 bar* |
|----------------------|-------------------|---------------------------|----------------------------|----------------------------|--------------------------|
| DN15 (1/2") | 3-5 | 4-12 | 7-20 | 10-28 | €2,100-6,000 |
| DN20 (3/4") | 5-8 | 12-30 | 20-50 | 28-72 | €6,000-15,000 |
| DN25 (1") | 8-12 | 30-68 | 50-115 | 72-160 | €15,000-34,500 |
| DN32 (1-1/4") | 10-16 | 47-120 | 80-200 | 115-290 | €24,000-60,000 |
| DN40 (1-1/2") | 12-20 | 68-190 | 115-320 | 160-450 | €34,500-96,000 |
| DN50 (2") | 16-25 | 120-295 | 200-500 | 290-720 | €60,000-150,000 |

*Varsayımlar: 6,000 saat/yıl, buhar maliyeti €0.030/kg (doğalgaz bazlı), tamamen açık kalmış kapan

**Not:** Kısmen açık kalmış kapanlarda kayıp bu değerlerin %20-60'ı olabilir.

## Survey Programı

### Tarama Sıklığı Önerileri

| Sistem Kritisite Düzeyi | Önerilen Sıklık | Açıklama |
|------------------------|-----------------|----------|
| Kritik proses ekipmanları | 3-6 ayda bir | Üretim kaybı riski yüksek |
| Ana buhar hatları | 6-12 ayda bir | Yüksek basınç, büyük orifis |
| Tracer hatları / bina ısıtma | 12 ayda bir | Mevsimsel kullanım |
| Düşük basınç / küçük kapanlar | 12-24 ayda bir | Düşük kayıp potansiyeli |

### Dokümantasyon Gereksinimleri

Her buhar kapanı için aşağıdaki bilgiler kayıt altında tutulmalıdır:

- **Kapan kimliği:** Benzersiz etiket numarası (ör. ST-B01-001)
- **Konum:** Bina, hat, ekipman referansı
- **Tip ve marka/model:** Termodinamik, F&T, ters kova vb.
- **Bağlantı boyutu:** DN15, DN20 vb.
- **Çalışma basıncı ve sıcaklığı**
- **Montaj tarihi ve son değişim tarihi**
- **Test geçmişi:** Tarih, test yöntemi, sonuç (sağlam/arızalı/şüpheli)
- **Onarım geçmişi:** Tarih, yapılan işlem, malzeme

### Önceliklendirme Kriterleri

Arızalı kapanlar tespit edildikten sonra onarım/değişim önceliği:

1. **Acil (1 hafta içinde):** Güvenlik riski, su darbesi tehlikesi, kapalı kalmış yüksek kritik kapanlar
2. **Yüksek öncelik (1 ay içinde):** Açık kalmış büyük kapanlar (>50 kg/h kayıp), yüksek basınç hatlarındaki arızalar
3. **Orta öncelik (3 ay içinde):** Açık kalmış orta boy kapanlar (10-50 kg/h kayıp)
4. **Düşük öncelik (planlı bakımda):** Küçük kapanlar (<10 kg/h kayıp), düşük basınç hatları

## Uygulanabilirlik Kriterleri

Bu çözüm aşağıdaki durumlarda uygulanmalıdır:

- Tesiste 50+ buhar kapanı bulunuyorsa
- Son 12 ayda kapsamlı bir trap survey yapılmamışsa
- Kondansat geri dönüş sıcaklığı beklenenden yüksekse
- Kondansat tankında aşırı flash buhar gözleniyorsa
- Buhar tüketiminde açıklanamayan artış varsa
- Su darbesi (water hammer) şikayetleri alınıyorsa
- Kazan kapasite yetersizliği yaşanıyorsa (arızalı traplerden kaynaklı kayıp nedeniyle)
- Enerji denetimi veya ISO 50001 kapsamında iyileştirme aranıyorsa

## Yatırım Maliyeti

### Trap Değişim Maliyetleri

| Trap Tipi | DN15 | DN20 | DN25 | DN32 | DN40 | DN50 |
|-----------|------|------|------|------|------|------|
| Termodinamik | €30-60 | €40-80 | €50-100 | €70-140 | €90-180 | €120-250 |
| Termostatik | €40-80 | €50-100 | €70-140 | €100-200 | €130-260 | €180-360 |
| F&T | €80-180 | €100-250 | €150-350 | €200-500 | €300-700 | €450-1,000 |
| Ters Kova | €70-150 | €90-200 | €130-300 | €180-400 | €250-600 | €380-850 |

**Not:** Fiyatlar malzeme içindir. İşçilik trap başına €50-150 eklenmelidir (erişilebilirliğe bağlı).

### Survey Maliyetleri

| Hizmet Tipi | Maliyet | Açıklama |
|-------------|---------|----------|
| Dış firma ile survey | €5-15 / trap | Uzman firma, rapor dahil |
| Kendi ekiple survey (ekipman yatırımı) | €3,000-8,000 (ultrasonik cihaz) | Tek seferlik yatırım |
| Akustik kamera ile survey | €15,000-45,000 (cihaz) | Hızlı tarama, çoklu kullanım |
| Kablosuz izleme sistemi | €50-200 / sensör | Sürekli izleme, IoT tabanlı |

## ROI Hesabı

### Formül
```
Arızalı_trap_sayısı = Toplam_trap × Arıza_oranı / 100
Toplam_buhar_kaybı_kg/h = Arızalı_trap_sayısı × Ort_kayıp_per_trap
Yıllık_kayıp_maliyet = Toplam_buhar_kaybı_kg/h × Çalışma_saati × Buhar_maliyeti_per_kg
Yıllık_tasarruf = Yıllık_kayıp_maliyet × Onarım_başarı_oranı
Toplam_yatırım = Survey_maliyeti + (Arızalı_trap_sayısı × Ort_değişim_maliyeti)
Geri_ödeme_ay = (Toplam_yatırım / Yıllık_tasarruf) × 12
```

### Örnek Hesap — 200 Trap'lı Tesis

- **Toplam trap sayısı:** 200 adet (karma boyut ve tip)
- **Arıza oranı:** %15 (bakımsız sistem)
- **Arızalı trap sayısı:** 200 × 0.15 = 30 adet
- **Ortalama buhar kaybı:** 25 kg/h per arızalı trap (orta boy, 8 bar)
- **Toplam buhar kaybı:** 30 × 25 = 750 kg/h
- **Çalışma süresi:** 6,000 saat/yıl
- **Buhar maliyeti:** €0.030/kg
- **Yıllık kayıp maliyet:** 750 × 6,000 × 0.030 = **€135,000/yıl**
- **Onarım başarı oranı:** %90
- **Yıllık tasarruf:** €135,000 × 0.90 = **€121,500/yıl**
- **Survey maliyeti:** 200 trap × €10 = €2,000
- **Değişim maliyeti:** 30 trap × €200 (ortalama malzeme + işçilik) = €6,000
- **Toplam yatırım:** €2,000 + €6,000 = **€8,000**
- **Geri ödeme:** (€8,000 / €121,500) × 12 = **0.8 ay (yaklaşık 3.5 hafta)**

**Sonuç:** Buhar kapanı survey ve onarımı, endüstriyel enerji verimliliği projelerinin en yüksek ROI'ye sahip uygulamalarından biridir.

## Uygulama Adımları

1. **Envanter oluşturma:** Tesisteki tüm buhar kapanlarını listele, etiketle ve konumlandır (P&ID ve saha doğrulaması)
2. **İlk survey:** Tüm kapanları ultrasonik + infrared yöntemiyle test et ve durumlarını kaydet
3. **Analiz ve raporlama:** Arızalı kapanları belirle, kayıp hesaplamalarını yap, önceliklendirme listesi oluştur
4. **Acil onarım/değişim:** Büyük kayıplı ve güvenlik riski olan kapanları öncelikli olarak değiştir
5. **Planlı değişim:** Kalan arızalı kapanları üretim planına uygun olarak sistematik değiştir
6. **Doğrulama testi:** Değişim sonrası her kapanı yeniden test et, düzgün çalıştığını doğrula
7. **Periyodik survey programı oluştur:** Kritisite düzeyine göre 3-12 aylık tarama takvimi belirle
8. **KPI takibi:** Arıza oranını, buhar kaybını ve tasarrufları düzenli olarak izle ve raporla
9. **Eğitim:** Bakım ekibine buhar kapanı test yöntemleri ve arıza tespiti eğitimi ver
10. **Sürekli iyileştirme:** Tekrarlayan arızaları analiz et, tip/marka değişikliği veya sistem modifikasyonu değerlendir

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yanlış tip seçimi | Uygulamaya uygun olmayan trap tipi erken arızaya neden olur | Çalışma koşullarına göre doğru tip/boyut seçimi, üretici teknik danışmanlığı |
| Yanlış boyutlandırma | Aşırı büyük trap: buhar kaçırma; aşırı küçük trap: kondansat birikimi | Gerçek kondansat yüküne göre boyutlandır, %2-3 güvenlik faktörü uygula |
| Karşı basınç etkisi | Yüksek karşı basınç trap performansını düşürür | Kondansat hattı boyutlandırmasını kontrol et, karşı basınçı <%50 diferansiyelde tut |
| Flash buhar ile canlı buhar karıştırılması | Test sırasında sağlam trap arızalı olarak değerlendirilebilir | Deneyimli personel, birden fazla test yöntemi kombinasyonu |
| Montaj hataları | Yanlış yön, eksik strainer, drip pocket hatası | Üretici montaj kılavuzuna uyum, standart montaj prosedürleri |
| Su darbesi (onarım sonrası) | Uzun süre kapalı kalmış trap değiştirildiğinde biriken kondansat su darbesine neden olabilir | Yavaş vana açılışı, hat drenajı, warm-up prosedürü |
| Korozyon ve erozyon | Agresif kondansat veya yüksek hızlı akış iç parçaları aşındırır | Paslanmaz çelik iç parçalar, kondansat kimyası kontrolü |
| Donma | Dış ortamda bulunan kapanlar kışın donabilir | Yalıtım, ısı bantı (heat tracing), drenaj imkanı |

## İlgili Dosyalar

- Kazan ekipman bilgisi: `equipment/boiler_firetube.md`, `equipment/boiler_watertube.md`
- Kazan exergy formülleri: `formulas/boiler_exergy.md`
- Kondansat geri kazanımı: `solutions/boiler_condensate_recovery.md`
- Buhar sistemi yalıtım: `solutions/boiler_insulation.md`
- Benchmark verileri: `benchmarks/boiler_benchmarks.md`

## Referanslar

- Spirax Sarco, "The Steam and Condensate Loop" — Chapter 11: Steam Trapping, Chapter 12: Steam Trap Selection
- Spirax Sarco, "Steam Trap Management: Best Practices Guide"
- Armstrong International, "Steam Trap Management Program" — Technical Documentation
- Armstrong International, "Steam Conservation Guidelines for Condensate Drainage"
- TLV Co., Ltd., "Steam Trap Engineering Handbook"
- TLV Co., Ltd., "TrapMan — Steam Trap Management System" Documentation
- DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition
- DOE Steam Tip Sheet #1, "Inspect and Repair Steam Traps"
- ASME Research Report, "Steam Trap Performance Assessment"
- ISO 50001:2018 — Energy Management Systems, Clause 8: Operation (Steam Systems)
