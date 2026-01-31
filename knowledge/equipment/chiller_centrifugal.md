# Santrifüj Kompresörlü Chiller — Centrifugal Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı, santrifüj (turbo) kompresörlü
- Kapasite aralığı: 300-10,000+ kW soğutma (85-2,800+ ton)
- Kompresör aşama sayısı: Tek kademeli (single stage) veya çok kademeli (multi-stage, 2-6 kademe)
- Soğutkan: R-134a, R-1234ze(E), R-513A, R-123 (phase-out), R-514A, R-1233zd(E)
- COP (tam yük, su soğutmalı): 6.0-7.5
- IPLV/NPLV: 7.0-11.5+ (VSD ile 10.0-11.5+)
- kW/ton (tam yük): 0.47-0.58
- Exergy verimi: %25-45
- Tipik ömür: 25-30+ yıl
- Yaygın markalar: Carrier (19XR/19DV), Trane (CenTraVac CVGF/CVHF), York (YK/YZ), Daikin (Magnitude), Mitsubishi (AART), Danfoss Turbocor (TT/TG/TTS), Smardt, LG (inverter centrifugal)

## Çalışma Prensibi

Santrifüj kompresörlü chillerlar, yüksek hızda dönen bir çark (impeller) ile soğutkan gazına kinetik enerji kazandırır ve bu kinetik enerjiyi difüzör ve volütte basınç enerjisine dönüştürür. Pompalara benzer bir prensiple çalışırlar, ancak çalışma akışkanı gaz fazdaki soğutkandır.

### Temel Bileşenler
- **İmpeller (Çark):** Yüksek hızda dönen, radyal veya geriye eğik kanatlı kapalı veya yarı açık çark. Uç hızı 200-350 m/s.
- **Difüzör:** İmpeller çıkışındaki yüksek hızlı gazı yavaşlatarak basınca dönüştüren sabit veya ayarlanabilir kanatlı bileşen.
- **Volüt:** Difüzör çıkışında gazı toplayan spiral gövde.
- **İnlet Guide Vane (IGV):** İmpeller girişindeki ayarlanabilir kanatçıklar — kapasite kontrolü sağlar.
- **Ekonomizer:** Çok kademeli kompresörlerde ara basınçta soğutkan enjeksiyonu ile verimi artıran bileşen.

### Tek Kademeli vs Çok Kademeli

| Özellik | Tek Kademeli | İki Kademeli | Üç+ Kademeli |
|---------|-------------|-------------|--------------|
| Basınç oranı | 3-5:1 | 6-12:1 | 12-25:1 |
| Kapasite | 300-3,000 kW | 500-10,000+ kW | 1,000-10,000+ kW |
| Verim | İyi | Çok iyi | En yüksek |
| Soğutkan | R-134a, R-1234ze | R-134a, R-1234ze | R-134a, R-123 (eski), R-1233zd |
| Maliyet | Düşük-orta | Orta-yüksek | Yüksek |
| Tipik uygulama | Standart HVAC | Büyük binalar | Büyük tesisler, district cooling |

### Açık Tahrik vs Hermetik Tasarım
- **Açık tahrik (open drive):** Motor ve kompresör ayrı, kaplin ile bağlı. Bakım kolaylığı, motor değiştirilebilirliği. Mil keçesi sızıntı riski var.
- **Hermetik (hermetic/semi-hermetic):** Motor ve kompresör aynı gövde içinde. Sızıntı riski düşük, kompakt. Bakımı daha zor.
- **Doğrudan tahrikli (direct-drive):** Dişli kutusu yok, yüksek hızlı motor doğrudan impelleri çevirir. Manyetik yataklı türbin kompresörlerinde (Danfoss Turbocor) yaygın.

## İnlet Guide Vane (IGV) Kapasite Kontrolü

IGV, santrifüj chillerlarda en yaygın kapasite kontrol yöntemidir:

### Çalışma Prensibi
- İmpeller girişindeki ayarlanabilir kanatçıkların açısı değiştirilir
- Tam açık: %100 kapasite, gaz akışına minimum direnç
- Kısmen kapalı: Gaz akışını kısar ve pre-rotation (ön dönüş) verir
- Tipik kontrol aralığı: %15-100 kapasite

### IGV Kısmi Yük Performansı

| Yük Oranı (%) | IGV Açısı (°) | Güç Oranı (%) | COP (% Tam Yük) |
|---------------|--------------|----------------|-----------------|
| 100 | 90 (tam açık) | 100 | %100 |
| 90 | 78 | 88 | %102 |
| 75 | 62 | 70 | %107 |
| 60 | 48 | 53 | %113 |
| 50 | 38 | 42 | %119 |
| 40 | 28 | 33 | %121 |
| 30 | 18 | 26 | %115 |
| 20 | 10 | 21 | %95 |

> **Not:** CW sıcaklığının kısmi yükte düşmesi COP artışının ana faktörüdür.

## VSD (Değişken Hızlı Tahrik) Uygulaması

VSD, santrifüj chillerlarda IGV'ye göre çok daha üstün kısmi yük performansı sağlar:

```
W_VSD / W_nominal ≈ (n/n_nominal)³  (affinity law — yaklaşık)

Burada:
  W_VSD     = VSD ile çalışma gücü [kW]
  W_nominal = nominal (tam hız) güç [kW]
  n         = çalışma devri [RPM]
  n_nominal = nominal devir [RPM]
```

### VSD vs IGV Kısmi Yük Karşılaştırması

| Yük (%) | IGV Güç (%) | VSD Güç (%) | VSD Tasarrufu (%) |
|---------|------------|------------|-------------------|
| 100 | 100 | 100 | 0 |
| 90 | 88 | 82 | 7 |
| 75 | 70 | 60 | 14 |
| 60 | 53 | 40 | 25 |
| 50 | 42 | 30 | 29 |
| 40 | 33 | 22 | 33 |
| 30 | 26 | 15 | 42 |

- VSD ile IPLV değeri %15-30 iyileşir
- VSD + IGV kombinasyonu en iyi sonucu verir (çoğu üretici bu kombinasyonu sunar)
- Manyetik yataklı kompresörlerde VSD standart olarak bulunur

## Manyetik Yataklı (Oil-Free) Teknoloji

Manyetik yataklı santrifüj kompresörler (Danfoss Turbocor, Carrier 19DV, Smardt) modern chiller teknolojisinin en ileri noktasıdır:

### Özellikler
- Aktif manyetik yataklar (AMB — Active Magnetic Bearings) ile rotor temassız olarak havada asılı tutulur
- Yağ sistemi tamamen ortadan kalkar — yağsız (oil-free) çalışma
- Doğrudan tahrikli yüksek hızlı permanent magnet motor (10,000-48,000+ RPM)
- Entegre VSD standart
- Soğutkan: R-134a, R-1234ze(E), R-513A

### Manyetik Yatak Avantajları
- Mekanik sürtünme kaybı sıfır → %3-5 verim artışı
- Yağ sistemi yok → yağ-soğutkan ısı transfer engeli yok → evaporatör ve kondenser verimi artar
- Bakım maliyeti %40-60 düşük (yağ, filtre, yatak değişimi yok)
- Titreşim çok düşük (< 0.5 mm/s)
- Gürültü çok düşük (tipik 72-78 dBA)
- 30+ yıl yatak ömrü

### Dezavantajları
- Daha yüksek ilk yatırım maliyeti (%15-30 premium)
- Tek başına sınırlı kapasite (60-1,500 kW per kompresör), ancak çoklu kompresör modülleri ile 6,000+ kW'a ulaşılabilir
- Karmaşık elektronik kontrol sistemi

## Surge (Dalgalanma) ve Surge Kontrolü

Surge, santrifüj kompresörlere özgü kritik bir çalışma durumudur:

### Surge Nedir?
- Kompresör çıkış basıncı, sistem basıncının altına düştüğünde gaz geri akışı başlar
- Periyodik, şiddetli titreşim ve gürültü oluşur
- Mekanik hasara, yatak aşınmasına ve impeller yorulmasına yol açabilir
- Düşük debide (düşük yükte) veya yüksek kondenser basıncında oluşma olasılığı artar

### Surge Kontrol Yöntemleri
- **Hot gas bypass:** Basma hattından emme hattına gaz geri döndürme (en basit, enerji israfı yaratır)
- **IGV kontrolü:** Gaz akış açısını ayarlayarak surge sınırını genişletir
- **VSD ile hız kontrolü:** En etkili yöntem — kompresör hızını düşürerek surge sınırını kaydırır
- **Elektronik surge algılama:** Modern chillerlarda basınç oranı ve debi izlenerek otomatik surge önleme

```
Surge marjı = (Q_calisma - Q_surge) / Q_surge × 100

Burada:
  Q_calisma = mevcut çalışma debisi [m³/s]
  Q_surge   = surge noktasındaki debi [m³/s]
```

Minimum surge marjı: %10 (genellikle %15-20 önerilir)

## Exergy Verimi Hesabı

```
ψ = Ex_sogutma / W_toplam

Ex_sogutma = Q_evap × (T₀ / T_CHW - 1)

Burada:
  ψ           = exergy verimi [-]
  Ex_sogutma  = soğutma exergysi [kW]
  Q_evap      = soğutma kapasitesi [kW]
  T₀          = referans sıcaklığı = 298.15 K (25°C)
  T_CHW       = CHW ortalama sıcaklığı [K]
  W_toplam    = toplam sistem gücü (kompresör + pompalar + kule fanı) [kW]
```

### Exergy Verimi Karşılaştırması

| Chiller Tipi | COP | Exergy Verimi (%) |
|-------------|-----|-------------------|
| Santrifüj (standart IGV) | 6.0-6.5 | 28-35 |
| Santrifüj (VSD) | 6.5-7.0 | 32-40 |
| Santrifüj (manyetik yatak, VSD) | 7.0-7.5 | 35-45 |
| Santrifüj (IPLV koşullarında, VSD) | 9.0-11.5 | 38-45 |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kompresör elektrik gücü | kW | 150-5000+ | Güç analizörü (3 faz) |
| CHW giriş sıcaklığı (return) | °C | 11-14 | PT100 sensör |
| CHW çıkış sıcaklığı (supply) | °C | 5-8 | PT100 sensör |
| CHW debisi | m³/h | Kapasiteye bağlı | Ultrasonik / EM flowmeter |
| CW giriş sıcaklığı | °C | 28-35 | PT100 sensör |
| CW çıkış sıcaklığı | °C | 33-40 | PT100 sensör |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| CW debisi | m³/h | Kapasiteye bağlı | Ultrasonik flowmeter |
| Evaporatör basıncı | bar | 2-5 | Basınç transmiteri |
| Kondenser basıncı | bar | 6-14 | Basınç transmiteri |
| IGV pozisyonu | % | 10-100 | Chiller kontrol paneli |
| Kompresör devri (VSD) | RPM/Hz | Değişken | Frekans konvertör |
| Motor akımı (her faz) | A | Etikete bağlı | Pens ampermetre |
| Yağ basıncı (konvansiyonel) | bar | 2-6 | Basınç transmiteri |
| Yağ sıcaklığı (konvansiyonel) | °C | 40-60 | Sıcaklık sensörü |
| Yatak titreşimi | mm/s | <2.5 | Titreşim sensörü |
| Evaporatör yaklaşma sıcaklığı | °C | 1-4 | Hesaplama (T_CHW_out - T_evap) |
| Kondenser yaklaşma sıcaklığı | °C | 1-3 | Hesaplama (T_cond - T_CW_out) |

### Nameplate Bilgileri
- Marka ve model
- Nominal soğutma kapasitesi (kW veya ton)
- Nominal kompresör gücü (kW)
- Nominal COP ve IPLV
- Soğutkan tipi ve şarj miktarı (kg)
- Kademe sayısı
- Maksimum çalışma basıncı (yüksek/düşük taraf)
- Nominal CHW ve CW sıcaklıkları
- Motor tipi ve gücü (kW, V, Hz, RPM)
- Üretim yılı ve seri numarası

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| CHW supply sıcaklığı | 6.7°C | ARI 550/590 standart |
| CHW return sıcaklığı | 12.2°C | ΔT = 5.5°C |
| CW giriş sıcaklığı | 29.4°C | ARI 550/590 standart |
| CW çıkış sıcaklığı | 35.0°C | ΔT = 5.6°C |
| Tam yük COP | 6.3 | Orta-yüksek verimli santrifüj |
| IPLV | 9.0 | VSD'li modern chiller |
| Yük oranı (sezonluk) | %55 | Tipik bina profili |
| Çalışma saati | 2500 saat/yıl | Türkiye soğutma sezonu |
| Ortam sıcaklığı (T₀) | 25°C (298.15 K) | Exergy referansı |
| Evaporatör yaklaşma | 2°C | Temiz, bakımlı evaporatör |
| Kondenser yaklaşma | 1.5°C | Temiz, bakımlı kondenser |
| Elektrik birim fiyatı | 0.10 €/kWh | Endüstriyel tarife |
| CHW pompa gücü | Kapasitenin %5'i | Yaklaşık |
| CW pompa gücü | Kapasitenin %7'si | Yaklaşık |
| Kule fanı gücü | Kapasitenin %3'ü | Yaklaşık |

## Performans Tablosu (Kapasiteye Göre)

| Kapasite (kW) | Tam Yük COP | IPLV (VSD) | kW/ton | Exergy Verimi (%) | Tahmini Yatırım (€) |
|--------------:|------------:|----------:|-------:|-------------------:|---------------------:|
| 300 | 5.8-6.2 | 7.5-9.0 | 0.57-0.61 | 25-32 | 60,000-120,000 |
| 500 | 6.0-6.5 | 8.0-10.0 | 0.54-0.59 | 28-35 | 90,000-180,000 |
| 1,000 | 6.2-6.8 | 8.5-10.5 | 0.52-0.57 | 30-38 | 160,000-320,000 |
| 2,000 | 6.3-7.0 | 9.0-11.0 | 0.50-0.56 | 32-40 | 280,000-560,000 |
| 3,500 | 6.4-7.2 | 9.5-11.5 | 0.49-0.55 | 33-42 | 450,000-900,000 |
| 5,000 | 6.5-7.3 | 9.5-11.5+ | 0.48-0.54 | 34-43 | 600,000-1,200,000 |
| 7,000 | 6.5-7.4 | 9.5-11.5+ | 0.48-0.54 | 34-44 | 850,000-1,700,000 |
| 10,000 | 6.5-7.5 | 9.5-11.5+ | 0.47-0.54 | 35-45 | 1,100,000-2,200,000 |

> **Not:** VSD'li, R-134a soğutkanlı modern santrifüj chillerlar için ARI 550/590 koşullarında verilmiştir.

## Tipik Uygulamalar
- Büyük ticari binalar (AVM, otel kompleksleri, havalimanı terminalleri)
- Yüksek katlı ofis binaları
- Hastaneler ve sağlık tesisleri
- Veri merkezleri (yüksek kapasite)
- Bölgesel soğutma (district cooling) sistemleri
- Endüstriyel proses soğutma (petrokimya, ilaç, gıda)
- Üniversite kampüsleri
- Serbest bölge / organize sanayi soğutma şebekeleri

## Dikkat Edilecekler

1. **Surge riski:** Düşük yükte ve yüksek kondenser basıncında surge oluşabilir. Surge algılama ve önleme sistemi aktif tutulmalı.
2. **Evaporatör donma riski:** CHW çıkış sıcaklığı 3°C'nin altına düşmemeli. Düşük akış koruması aktif olmalı.
3. **Kondenser kirlenme:** Yaklaşma sıcaklığı tasarım değerinin 1°C üzerine çıkması halinde tüp temizliği yapılmalı. Kirli kondenser COP'yi %5-15 düşürür.
4. **Soğutkan sızıntı:** Santrifüj chillerlar düşük basınçlı soğutkanlarla (R-123, R-1233zd) çalıştığında negatif basınçtaki bölümlerden hava sızması olabilir — purge (hava tahliye) ünitesi bakımı kritiktir.
5. **VSD harmonik:** Büyük VSD'li chillerlarda elektrik şebekesine harmonik akım enjeksiyonu değerlendirilmeli. IEEE 519 sınırlarına uyum gerekebilir.
6. **Kule suyu kalitesi:** Kondenser suyundaki Legionella riski, kireç birikimi ve korozyon kontrolü için kimyasal dozajlama ve su analizi düzenli yapılmalı.
7. **Başlatma akımı:** Büyük santrifüj chillerların motor başlatma akımı şebeke kapasitesini zorlayabilir. Soft starter veya VSD ile yumuşak başlatma tercih edilmeli.
8. **Exergy perspektifi:** Santrifüj chillerlar kompresör tipleri arasında en yüksek exergy verimine sahiptir. VSD + manyetik yatak kombinasyonu ile %40-45 exergy verimine ulaşılabilir. CHW reset stratejisi ve değişken CW debisi ek exergy kazanımı sağlar.

## İlgili Dosyalar
- Buhar sıkıştırmalı chiller (genel): `equipment/chiller_vapor_compression.md`
- Vidalı chiller: `equipment/chiller_screw.md`
- Scroll chiller: `equipment/chiller_scroll.md`
- Absorpsiyon chiller: `equipment/chiller_absorption.md`
- Soğutma kulesi: `equipment/cooling_tower.md`
- Chiller exergy hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller VSD uygulaması: `solutions/chiller_vsd.md`
- Bölgesel soğutma: `solutions/district_cooling.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, 2024 (Chapters 38-43)
- ARI Standard 550/590 — Performance Rating of Water-Chilling and Heat Pump Packages
- Carrier Engineering Newsletter — Centrifugal Chiller Technology
- Trane Engineers Newsletter — CenTraVac Chiller Design and Optimization
- Danfoss Turbocor — Oil-Free Compressor Technology White Paper
- Kotas, T.J. "The Exergy Method of Thermal Plant Analysis", Krieger Publishing, 1995
- Bejan, A., Tsatsaronis, G., Moran, M. "Thermal Design and Optimization", Wiley, 1996
- EUROVENT Certification Programme — Liquid Chilling Packages
- IEEE 519 — Recommended Practice for Harmonic Control in Electrical Power Systems
- ASHRAE Standard 90.1 — Energy Standard for Buildings
- DOE/FEMP — Best Practices for Chiller Plant Optimization
