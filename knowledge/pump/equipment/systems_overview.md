# Pompalama Sistemleri Genel Bakış — Pumping Systems Overview

> Son güncelleme: 2026-01-31

## Genel Bilgiler

Pompalama sistemleri, endüstriyel elektrik tüketiminin %20-60'ını oluşturabilir ve toplam motor tahrikli enerji tüketiminin yaklaşık %25'ini temsil eder. Tipik bir pompalama sisteminde yalnızca %18-40 oranında enerji faydalı işe dönüştürülür — geri kalan %60-82 çeşitli kayıp noktalarında harcanır.

- Tip: Akışkan taşıma ve basınçlandırma sistemi
- Bileşenler: Pompa + motor + VSD + borulama + vanalar + tanklar + kontrol
- Kapasite aralığı: 0.1 - 10,000+ m³/h
- Basınç aralığı: 0.1 - 100+ bar
- Sektörler: Su/atıksu, petrokimya, enerji, gıda, kimya, maden, HVAC

### Sektörel Enerji Tüketim Payı

| Sektör | Pompalama Enerji Payı (%) | Tipik Uygulama |
|--------|--------------------------|----------------|
| Su ve atıksu | %80-90 | Terfi, dağıtım, arıtma |
| Petrol ve gaz | %50-60 | Transfer, boru hattı, proses |
| Kimya | %25-30 | Proses, transfer, soğutma |
| Kağıt ve selüloz | %25-30 | Stok, proses, fan pompaları |
| Gıda ve içecek | %15-25 | CIP, transfer, soğutma |
| HVAC | %15-25 | Sirkülasyon, soğutma kulesi |
| Madencilik | %20-40 | Susuzlaştırma, proses, şlam |

## Sistem Bileşenleri

### 1. Pompa
- **Santrifüj pompa:** En yaygın (%80+ uygulama), kinetik enerji → basınç
- **Pozitif deplasmanlı pompa:** Dişli, vidalı, pistonlu — yüksek viskozite, yüksek basınç
- **Dalma pompa:** Kuyu, havuz, tank içi uygulamalar

### 2. Motor
- Asenkron (indüksiyon) motor — en yaygın
- Verimlilik sınıfları: IE1-IE5 (detay için bkz. `equipment/pump_motors_drives.md`)

### 3. VSD (Değişken Hız Sürücüsü)
- Frekans konvertörü ile motor hız kontrolü
- AC-DC-AC dönüşüm
- Detay: `equipment/pump_motors_drives.md`

### 4. Borulama Sistemi
- Emme ve basma boruları
- Dirsekler, T-parçalar, redüksiyonlar
- Boru malzemeleri: çelik, paslanmaz, PVC, HDPE, GRP

### 5. Vanalar
- İzolasyon vanaları (gate, ball, butterfly)
- Kontrol vanaları (globe, butterfly + aktüatör)
- Çek vanalar (swing, wafer, tilting disc)

### 6. Enstrümantasyon
- Basınç transmitterleri
- Debimetreler (elektromanyetik, ultrasonik, vortex)
- Sıcaklık sensörleri
- Seviye sensörleri

## Sistem Eğrisi (System Curve) Kavramı

Sistem eğrisi, pompalama sisteminin farklı debilerdeki toplam direnç (basma yüksekliği) gereksinimini gösterir.

```
Sistem eğrisi formülü:

H_system = H_static + K × Q²

Burada:
  H_system  = Sistem basma yüksekliği (m)
  H_static  = Statik yükseklik farkı (m) — geodezik + tank basıncı
  K         = Sistem direnç katsayısı (m/(m³/h)²) — boru, vana, dirsek sürtünmeleri
  Q         = Debi (m³/h)

Statik head bileşenleri:
  H_static = (z₂ - z₁) + (P₂ - P₁) / (ρ × g)

Burada:
  z₂ - z₁ = Geometrik yükseklik farkı (m)
  P₂ - P₁ = Basınç farkı (Pa)
  ρ        = Akışkan yoğunluğu (kg/m³)
  g        = Yer çekimi ivmesi (9.81 m/s²)
```

### Statik Head vs Dinamik Head

| Bileşen | Tanım | Debi Bağımlılığı | Örnek |
|---------|-------|-------------------|-------|
| Statik head | Yükseklik + basınç farkı | Sabit (Q'dan bağımsız) | Kuyu derinliği, bina yüksekliği |
| Dinamik head (sürtünme) | Boru + vana + fittings kayıpları | Q² ile artar | Uzun boru hattı, çok dirsekli sistem |

**Önemli:** Statik head oranı yüksek sistemlerde VSD tasarrufu sınırlıdır. Dinamik head oranı yüksek sistemlerde VSD çok etkilidir.

## Operasyon Noktası (Operating Point)

Pompa eğrisi ile sistem eğrisinin kesiştiği nokta, gerçek çalışma noktasıdır.

```
Operasyon noktası:

Pompa eğrisi:     H_pump = f(Q)  — üretici katalog eğrisi
Sistem eğrisi:    H_sys  = H_static + K × Q²
Kesişim noktası:  H_pump(Q_op) = H_sys(Q_op) → Q_op, H_op

Pompa BEP (Best Efficiency Point):
  Pompanın en yüksek verimle çalıştığı nokta (Q_BEP, H_BEP)
  İdeal: Q_op = Q_BEP ± %10
  Kabul edilebilir: Q_op = %70-120 × Q_BEP
```

## Seri ve Paralel Pompa Operasyonu

### Seri Pompa Operasyonu
- Basma yükseklikleri toplanır: H_toplam = H₁ + H₂
- Debi aynı kalır: Q_toplam = Q₁ = Q₂
- Uygulama: Çok yüksek basınç gereken sistemler
- Dikkat: Her iki pompa aynı debide çalışmalı

### Paralel Pompa Operasyonu
- Debiler toplanır: Q_toplam = Q₁ + Q₂ (sabit head'de)
- Basma yüksekliği aynı kalır: H_toplam ≈ H₁ ≈ H₂
- Uygulama: Değişken debi gereken sistemler, yedeklilik
- Dikkat: Paralel pompaların performans eğrileri benzer olmalı

### Paralel Pompa — Verim Etkisi

| Konfigürasyon | Avantaj | Dezavantaj |
|---------------|---------|------------|
| 1 büyük pompa | Yüksek BEP verimi | Esneklik yok, kısmi yükte verimsiz |
| 2 küçük pompa | Bir pompa kapatılabilir | Her pompa biraz daha düşük verimli |
| 3+ küçük pompa | En esnek, en iyi kısmi yük | Yüksek yatırım, karmaşık kontrol |
| N × pompa + VSD | Optimal verim tüm yük aralığında | En yüksek yatırım |

## Kontrol Yöntemleri Karşılaştırması

### 1. Throttling (Vana Kontrolü) — En Verimsiz
- Kontrol vanası ile debi kısılır
- Pompa aynı hızda çalışır, vana ek direnç ekler
- Enerji vanada ısıya dönüşür — tam israf
- Tipik verimlilik: %30-50 (kontrol dahil)

### 2. Bypass — İsraf
- Pompa çıkışının bir kısmı emme tarafına geri döndürülür
- Pompa sürekli tam yükte çalışır
- Bypass edilen akış = saf enerji israfı
- Sadece minimum akış koruması için kabul edilebilir

### 3. VSD (Değişken Hız Sürücü) — En Verimli
- Motor hızı ayarlanarak debi ve basınç kontrol edilir
- Kübik yasa: P ∝ N³ → küçük hız düşüşü = büyük tasarruf
- Tipik verimlilik: %60-85 (kontrol dahil)
- En iyi çözüm: Değişken talep + yüksek dinamik head oranı

### 4. On-Off Kontrol — Basit Sistemler
- Pompa tamamen açılır veya kapanır
- Basınç tankı veya seviye kontrolü ile çalışır
- Sık başlatma mekanik stres yapar
- Küçük ve basit uygulamalar için uygundur

### 5. İmpeller Trimming — Kalıcı Çözüm
- Çark çapı küçültülerek kalıcı kapasite düşürme
- Geri dönüşü zor — yeni çark gerekir
- Sabit yüklü, aşırı boyutlu pompalarda etkili
- Tipik tasarruf: %10-25

### Kontrol Yöntemleri Karşılaştırma Tablosu

| Yöntem | Enerji Verimi | Yatırım Maliyeti | Esneklik | Uygulama |
|--------|--------------|-------------------|----------|----------|
| Throttling (vana) | Düşük (%30-50) | Düşük | Orta | Eski sistemler |
| Bypass | Çok düşük (%20-40) | Düşük | Düşük | Minimum akış koruması |
| VSD | Yüksek (%60-85) | Yüksek | Çok yüksek | Değişken talep |
| On-off | Orta (%40-60) | Düşük | Düşük | Basit sistemler |
| İmpeller trim | İyi (%55-75) | Orta (tek seferlik) | Düşük | Kalıcı boyut azaltma |

## Minimum Akış Koruma (Deadhead Protection)

```
Minimum akış nedenleri:
- Pompa aşırı ısınması (mekanik kayıplar → ısı)
- Kavitasyon riski
- Recirculation (iç geri akış)
- Titreşim ve gürültü artışı
- Mekanik hasar (yatak, conta, çark)

Tipik minimum akış: %10-30 × Q_BEP (pompa tipine bağlı)

Koruma yöntemleri:
1. Minimum akış vanası (bypass) — basit ama israf
2. VSD minimum hız ayarı — daha verimli
3. Akış anahtarı + alarm — koruma
4. Recirculation hattı + orifis — kontrollü bypass
```

## Sistem Seviyesi Exergy Akışı

### Grassmann Diyagramı Benzeri — Enerji/Exergy Akışı

```
Elektrik Girişi (100%)
  ├── VSD kayıpları: %2-5
  │     └── Isı olarak atılır
  ├── Motor kayıpları: %5-10
  │     └── Bakır, demir, mekanik kayıplar → ısı
  ├── Kaplin/transmisyon kaybı: %1-2
  ├── Pompa hidrolik kayıpları: %15-25
  │     ├── Çark kayıpları (disk friction, leakage)
  │     ├── Volüt/difüzör kayıpları
  │     └── Mekanik kayıplar (yatak, conta)
  ├── Boru sürtünme kayıpları: %5-15
  │     ├── Düz boru sürtünmesi
  │     ├── Dirsek, T-parça, redüksiyon
  │     └── Vana direnci (açık konumda bile)
  ├── Kontrol/throttle kayıpları: %10-30
  │     ├── Kontrol vanası basınç düşüşü
  │     ├── Bypass akış kaybı
  │     └── Aşırı basınç (oversizing) kaybı
  └── Faydalı Hidrolik İş: %18-50
        └── ρ × g × H_net × Q (gerçek ihtiyaç karşılığı)
```

### Exergy Verimi Hesabı

```
Pompalama sistemi exergy verimi:

η_ex = Ex_faydalı / Ex_giriş

Ex_giriş = W_elektrik (kW)  — elektrik exergysi = %100 exergy

Ex_faydalı = ρ × g × Q × H_net / 3.6×10⁶

Burada:
  ρ      = Akışkan yoğunluğu (kg/m³)
  g      = 9.81 m/s²
  Q      = Net debi (m³/h) — gerçek ihtiyaç
  H_net  = Net basma yüksekliği (m) — gerçek ihtiyaç

Tipik pompa sistemi exergy verimi: %15-40
En iyi uygulama: %40-60
```

## Enerji Dağılımı (Tipik Pompa Sistemi)

### DOE Verilerine Göre Tipik Dağılım

| Kayıp Kategorisi | Enerji Payı (%) | Exergy Yıkımı |
|------------------|----------------|----------------|
| Motor kayıpları | 5-10 | Düşük sıcaklıkta ısı — düşük exergy |
| VSD kayıpları | 2-5 | Düşük sıcaklıkta ısı |
| Pompa hidrolik kayıpları | 15-25 | Sürtünme → ısı |
| Boru sürtünme kayıpları | 5-15 | Basınç düşüşü → tersinmez kayıp |
| Throttle/kontrol kayıpları | 10-30 | En büyük israf — vana basınç düşüşü |
| **Faydalı iş** | **18-50** | **Net exergy çıkışı** |

### Verimlilik Kıyaslaması (Benchmarks) — Sistem Seviyesi

| Kategori | Wire-to-Water Verim (%) | Tipik Durum |
|----------|------------------------|-------------|
| Düşük | <30 | Aşırı boyutlu pompa, throttle kontrol, eski motor |
| Ortalama | 30-45 | Standart pompa, kısmen VSD, orta bakım |
| İyi | 45-60 | Doğru boyutlama, VSD, IE3+ motor, optimum boru |
| Best-in-class | >60 | Optimal tasarım, tam VSD, IE4/5 motor, minimum kayıp |

## Kavitasyon ve NPSH

### Kavitasyon Nedir?
Pompa emme tarafında basınç, akışkanın buhar basıncının altına düştüğünde buhar kabarcıkları oluşur. Bu kabarcıklar yüksek basınç bölgesine ulaştığında çökerek (implode) aşırı basınç dalgaları üretir — malzeme erozyonuna, gürültüye ve performans düşüşüne neden olur.

```
NPSH (Net Positive Suction Head):

NPSHa (Available — Mevcut):
NPSHa = (P_emme - P_buhar) / (ρ × g) + v²/(2g) + z_emme

NPSHr (Required — Gerekli):
Pompa üreticisi tarafından belirtilir (test ile belirlenir)

Kavitasyon koşulu: NPSHa < NPSHr → KAVİTASYON!
Güvenlik marjı: NPSHa > NPSHr + 0.5-1.0 m (önerilir)

Burada:
  P_emme   = Emme noktasındaki mutlak basınç (Pa)
  P_buhar  = Akışkanın buhar basıncı (Pa) — sıcaklığa bağlı
  ρ        = Akışkan yoğunluğu (kg/m³)
  g        = 9.81 m/s²
  v        = Emme hızı (m/s)
  z_emme   = Emme seviye farkı (m) — negatif ise vakum emme
```

### Kavitasyon Önleme
- Emme borusu çapını büyütme (hız düşürme)
- Pompa montaj yüksekliğini düşürme
- Emme tankı basınçlandırma
- Sıvı sıcaklığını düşürme (P_buhar düşer)
- Emme borusu kayıplarını azaltma (kısa, düz, geniş boru)

## Aşırı Boyutlama Sorunu

Pompalama sistemlerinde en yaygın ve maliyetli sorunlardan biri aşırı boyutlamadır.

### Neden Oluşur?
- Tasarım aşamasında güvenlik marjları üst üste eklenir (%10+%10+%10...)
- Gelecek kapasite artışı düşüncesi
- Gerçek sistem direnci hesaplanandan düşük çıkar
- "Büyük olan güçlüdür" yanılgısı

### Sonuçları
- Pompa BEP'ten uzakta çalışır → düşük verim
- Kontrol vanası kısılarak fazla basınç yakılır → enerji israfı
- Kavitasyon ve recirculation riski
- Motor düşük yükte çalışır → düşük güç faktörü
- Tesisat ömrü boyunca %20-40 ek enerji maliyeti

### Çözümler
- İmpeller trimming (çark kesimi) — düşük maliyetli, kalıcı
- VSD eklenmesi — esnek, en iyi çözüm
- Pompa değişimi — yatırım yüksek ama verimli
- Doğru boyutlandırma kılavuzları takip edilmeli

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Elektrik gücü (pompa + motor) | kW | 0.5-5000+ | Güç analizörü |
| Çıkış basıncı | bar | 0.5-100+ | Basınç transmitteri |
| Giriş (emme) basıncı | bar | -1 ile +10 | Basınç transmitteri |
| Debi | m³/h | 0.1-10,000+ | Debimetre |
| Akışkan sıcaklığı | °C | 5-200 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Motor devri | RPM | 300-3600 | Takometre |
| Kontrol vanası pozisyonu | % | 0-100 | Aktüatör geri besleme |
| Titreşim | mm/s | <4.5 | Titreşim sensörü |
| Viskozite | cP veya mm²/s | 0.3-10,000 | Viskozimetre |
| Çalışma saati | saat/yıl | 1000-8760 | Sayaç |

### Nameplate Bilgileri
- Pompa markası, modeli, seri numarası
- Pompa tipi (santrifüj, dişli, vidalı vb.)
- Nominal debi (m³/h), nominal basma yüksekliği (m veya bar)
- Nominal güç (kW) ve devir (RPM)
- Çark çapı (mm) ve malzeme
- Motor IE sınıfı
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Pompa verimi | %70 | Santrifüj, BEP yakını |
| Motor verimi | %91 | IE3, 10-20 kW |
| VSD verimi | %97 | Modern frekans konvertörü |
| Boru kayıp oranı | %15 | Toplam basma yüksekliğinin |
| Throttle kaybı oranı | %20 | Vana kontrollü sistemde |
| Çalışma saati | 4000 saat/yıl | Tek vardiya |
| Yük profili (ortalama) | %65 | Değişken talep uygulaması |
| Su sıcaklığı | 20°C | Standart koşullar |
| Su yoğunluğu | 998 kg/m³ | 20°C'de |

## Dikkat Edilecekler

1. **Aşırı boyutlama:** Pompalama sistemlerinin %60'ı aşırı boyutlu — bu en yaygın ve en maliyetli sorundur
2. **Throttle kontrol:** Vana ile debi kontrolü en verimsiz yöntem — VSD'ye geçiş değerlendirilmeli
3. **BEP sapması:** Pompa BEP'ten %30'dan fazla uzakta çalışıyorsa verim ve ömür ciddi şekilde düşer
4. **Zamanla verim düşüşü:** Aşınma, korozyon ve kirlenme nedeniyle pompa verimi yılda %1-2 düşebilir — periyodik performans testi
5. **Boru tasarımı:** Boru çapı ve güzergah optimizasyonu genellikle ihmal edilir — küçük boru = yüksek sürtünme = sürekli enerji kaybı
6. **Kontrol stratejisi:** Sistem kontrol yöntemi toplam verimliliği pompa seçiminden daha fazla etkiler
7. **Kavitasyon belirtileri:** Gürültü, titreşim, performans düşüşü varsa NPSH kontrol edilmeli
8. **Enerji izleme:** Pompa başına enerji ölçümü olmadan optimizasyon yapılamaz — alt ölçüm şart

## İlgili Dosyalar
- Pompa motorları ve sürücüler: `equipment/pump_motors_drives.md`
- Hidrofor: `equipment/pump_booster.md`
- Vakum pompaları: `equipment/pump_vacuum.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition (2006)
- Hydraulic Institute, "Pump System Assessment and Optimization"
- Europump & Hydraulic Institute, "Variable Speed Pumping — A Guide to Successful Applications"
- Grundfos, "Pump Handbook" ve "The Centrifugal Pump" (Grundfos Research and Technology)
- KSB, "Selecting Centrifugal Pumps — KSB Know-How Series"
- Karassik, I.J. et al., "Pump Handbook," 4th Edition, McGraw-Hill
- Gülich, J.F., "Centrifugal Pumps," 3rd Edition, Springer
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing, 1995
- Bejan, A., Tsatsaronis, G., Moran, M., "Thermal Design and Optimization," Wiley, 1996
