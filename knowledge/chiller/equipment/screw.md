---
title: "Vidalı Kompresörlü Chiller — Screw Compressor Chiller"
category: equipment
equipment_type: chiller
subtype: "Vidalı (Screw)"
keywords: [vidalı chiller, screw, orta kapasite]
related_files: [chiller/benchmarks.md, chiller/formulas.md, chiller/solutions/vsd.md]
use_when: ["Vidalı chiller analizi yapılırken", "Orta kapasite soğutma değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Vidalı Kompresörlü Chiller — Screw Compressor Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı, vidalı (helical rotary screw) kompresörlü
- Kapasite aralığı: 50-1,500 kW soğutma (14-430 ton)
- Kompresör tipleri: Tek vidalı (single screw), çift vidalı (twin screw)
- Soğutkan: R-134a, R-407C, R-410A, R-1234ze(E), R-513A, R-717 (NH₃)
- COP (tam yük, su soğutmalı): 5.0-6.5
- COP (tam yük, hava soğutmalı): 2.8-3.5
- IPLV/NPLV (su soğutmalı): 6.0-9.0
- Exergy verimi: %20-40
- Tipik ömür: 20-25 yıl
- Yaygın markalar: Carrier (30XA/30XW), Trane (RTHD/RTAF), York (YVAA/YVWA), Daikin (ZUW/ZUA), Bitzer (OSN/OSKA), Dunham-Bush, McQuay (Daikin Applied)

## Çalışma Prensibi

Vidalı kompresörlü chillerlar, helisel (vida şeklinde) rotorların dönmesiyle soğutkan gazı emen, sıkıştıran ve yüksek basınçta basan pozitif deplasmanlı makinelerdir. Diğer chiller bileşenleri (evaporatör, kondenser, genleşme vanası) standart buhar sıkıştırmalı çevrimle aynıdır.

### Tek Vidalı (Single Screw) Kompresör
- Bir ana helisel rotor ve iki yıldız çark (star rotor / gate rotor) bulunur
- Ana rotor dönerken yıldız çarklar ile arasındaki hacim değişir
- Avantaj: Dengeli radyal kuvvetler, düşük titreşim, uzun yatak ömrü
- Dezavantaj: Yıldız çark aşınması, sınırlı üretici sayısı
- Tipik marka: Carrier (Vilter)

### Çift Vidalı (Twin Screw) Kompresör
- Bir erkek rotor (4-6 lob) ve bir dişi rotor (5-7 oluk) birbirine geçerek döner
- Loblar arasındaki hacim giriş tarafında artar (emme), çıkış tarafında azalır (basma)
- Sabit hacim oranı (Vi — built-in volume ratio): genellikle 2.5-5.0
- Avantaj: Yüksek verim, güvenilirlik, geniş kapasite aralığı
- Dezavantaj: Yağ yönetimi gerekli (yağlı tipte), gürültü (dişli profili)
- Tipik markalar: Bitzer, Trane, York, Daikin, Hanbell

### Vi (Volume Ratio) Seçimi

```
Vi = V_emme / V_basma

Burada:
  Vi     = kompresörün dahili hacim oranı (built-in volume ratio)
  V_emme = emme tarafındaki hacim [m³]
  V_basma = basma tarafındaki hacim [m³]
```

Vi seçimi çalışma koşullarına uygun olmalıdır:
- Vi çok düşük → aşırı sıkıştırma eksikliği (under-compression) → verim kaybı
- Vi çok yüksek → aşırı sıkıştırma (over-compression) → verim kaybı
- Değişken Vi özelliğine sahip kompresörler her iki durumu da optimize eder

## Kapasite Kontrolü — Slide Valve (Kayar Vana)

Vidalı kompresörlerin en karakteristik özelliği **slide valve** (kayar vana) ile sürekli (stepless) kapasite kontrolüdür.

### Slide Valve Çalışma Prensibi
- Rotorlar boyunca kayabilen bir vana, etkin sıkıştırma uzunluğunu değiştirir
- Tam açık pozisyon: %100 kapasite
- Kısmen kapalı: Emilen gaz bir kısmı tekrar emme tarafına geri bypass edilir
- Tipik kapasite kontrol aralığı: %25-100 (sürekli)
- Bazı modellerde %10'a kadar inebilir (çift slide valve)

### Kısmi Yük Performansı

| Yük Oranı (%) | Güç Oranı (%) | COP (% Tam Yük COP) | Açıklama |
|---------------|----------------|---------------------|----------|
| 100 | 100 | %100 | Tam yük, nominal koşullar |
| 90 | 90 | %100 | Neredeyse lineer |
| 75 | 72 | %104 | Hafif verim artışı |
| 60 | 55 | %109 | Düşen CW sıcaklığı etkisi |
| 50 | 43 | %116 | IPLV hesabında ağırlıklı |
| 40 | 34 | %118 | CW sıcaklığı düştükçe verim artar |
| 25 | 22 | %114 | Slide valve verim kaybı belirginleşir |

> **Not:** Yukarıdaki tablo su soğutmalı chiller için verilmiştir. CW sıcaklığının düşmesi (azalan kondenser basıncı) kısmi yükte COP artışının ana sebebidir.

## IPLV/NPLV Değerleri

IPLV (Integrated Part Load Value) ve NPLV (Non-standard Part Load Value) kısmi yük performansını tek bir değerle ifade eder:

```
IPLV = 0.01×A + 0.42×B + 0.45×C + 0.12×D

Burada:
  A = %100 yükte COP (CW giriş: 30.0°C)
  B = %75 yükte COP  (CW giriş: 24.5°C)
  C = %50 yükte COP  (CW giriş: 19.0°C)
  D = %25 yükte COP  (CW giriş: 19.0°C)
```

Tipik IPLV değerleri (su soğutmalı vidalı chiller):
- Standart verim: 6.0-7.0
- Yüksek verim: 7.0-8.5
- Premium verim (VSD ile): 8.0-9.0+

## Su Soğutmalı vs Hava Soğutmalı Karşılaştırma

| Parametre | Su Soğutmalı | Hava Soğutmalı |
|-----------|-------------|----------------|
| Tam yük COP | 5.0-6.5 | 2.8-3.5 |
| IPLV | 6.0-9.0 | 3.5-5.0 |
| kW/ton (tam yük) | 0.54-0.70 | 1.00-1.25 |
| Kondenser tipi | Shell & tube (boru-kabuk) | Finli boru + fan |
| Soğutma kulesi | Gerekli | Gerekli değil |
| Kurulum yeri | İç mekan (mekanik oda) | Dış mekan (çatı/bahçe) |
| Bakım | Daha fazla (kule + chiller) | Daha az (sadece chiller) |
| Gürültü | Düşük (iç mekan) | Yüksek (fan gürültüsü) |
| Su tüketimi | Var (buharlaşma kaybı) | Yok |
| İlk yatırım (chiller) | 100-200 €/kW | 120-250 €/kW |
| İlk yatırım (toplam sistem) | 200-400 €/kW | 150-300 €/kW |
| Uygun kapasite | 100-1,500 kW | 50-1,200 kW |
| Exergy verimi (tam yük) | %25-40 | %18-28 |

## Enerji Dağılımı (Tipik Su Soğutmalı Vidalı Chiller Sistemi)
- Kompresör elektrik tüketimi: ~%80-85
- Kondenser su pompası: ~%8-10
- CHW pompası: ~%5-8
- Soğutma kulesi fanı: ~%3-5
- Yağ pompası ve kontrol: ~%1-2

## Exergy Verimi Hesabı

```
ψ = Ex_sogutma / W_toplam

Ex_sogutma = Q_evap × (T₀ / T_CHW - 1)

Burada:
  ψ           = exergy verimi [-]
  Ex_sogutma  = soğutma exergysi [kW]
  Q_evap      = soğutma kapasitesi [kW]
  T₀          = referans sıcaklığı = 298.15 K (25°C)
  T_CHW       = CHW ortalama sıcaklığı [K] = (T_CHW_giris + T_CHW_cikis) / 2
  W_toplam    = toplam elektrik gücü (kompresör + pompalar + fan) [kW]
```

**Tipik exergy verimleri:**

| Koşul | COP | Exergy Verimi |
|-------|-----|---------------|
| Su soğutmalı, tam yük | 5.5 | %28-32 |
| Su soğutmalı, %50 yük | 6.5 | %30-36 |
| Hava soğutmalı, tam yük | 3.0 | %18-22 |
| Hava soğutmalı, %50 yük | 3.5 | %20-25 |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kompresör elektrik gücü | kW | 30-500 | Güç analizörü (3 faz) |
| CHW giriş sıcaklığı (return) | °C | 11-14 | PT100 sensör |
| CHW çıkış sıcaklığı (supply) | °C | 5-8 | PT100 sensör |
| CHW debisi | m³/h | Kapasiteye bağlı | Ultrasonik / EM flowmeter |
| CW giriş sıcaklığı | °C | 28-35 | PT100 sensör |
| CW çıkış sıcaklığı | °C | 33-40 | PT100 sensör |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| CW debisi | m³/h | Kapasiteye bağlı | Ultrasonik flowmeter |
| Emme basıncı | bar | 2-5 | Basınç transmiteri |
| Basma basıncı | bar | 8-18 | Basınç transmiteri |
| Yağ sıcaklığı | °C | 40-65 | Sıcaklık sensörü |
| Yağ basıncı | bar | 3-8 | Basınç transmiteri |
| Slide valve pozisyonu | % | 25-100 | Chiller kontrol paneli |
| Motor akımı | A | Etikete bağlı | Pens ampermetre |
| Kompresör devri (VSD'li) | RPM | 20-60 Hz | Frekans konvertör |
| Titreşim | mm/s | <4.5 (ISO 10816) | Titreşim sensörü |

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| CHW supply sıcaklığı | 7°C | ARI standart |
| CHW return sıcaklığı | 12°C | ΔT = 5°C |
| CW giriş sıcaklığı | 30°C | ARI standart |
| CW çıkış sıcaklığı | 35°C | ΔT = 5°C |
| Tam yük COP (su soğutmalı) | 5.5 | Orta verimli vidalı |
| Tam yük COP (hava soğutmalı) | 3.0 | Standart hava soğutmalı |
| Yük oranı (sezonluk) | %55 | Tipik ofis binası |
| Çalışma saati | 2500 saat/yıl | Türkiye soğutma sezonu |
| Yağ sıcaklığı | 50°C | Normal çalışma |
| Ortam sıcaklığı (T₀) | 25°C (298.15 K) | Exergy referansı |
| Elektrik birim fiyatı | 0.10 €/kWh | Endüstriyel tarife |

## Performans Tablosu (Kapasiteye Göre)

| Kapasite (kW) | Tam Yük COP | IPLV | kW/ton | Exergy Verimi (%) | Tahmini Yatırım (€) |
|--------------:|------------:|-----:|-------:|-------------------:|---------------------:|
| 50 | 4.8-5.2 | 5.8-6.5 | 0.68-0.73 | 20-25 | 15,000-30,000 |
| 100 | 5.0-5.5 | 6.0-7.0 | 0.64-0.70 | 22-28 | 25,000-50,000 |
| 200 | 5.2-5.8 | 6.5-7.5 | 0.61-0.68 | 25-32 | 40,000-80,000 |
| 500 | 5.5-6.2 | 7.0-8.5 | 0.57-0.64 | 28-35 | 80,000-160,000 |
| 800 | 5.6-6.3 | 7.2-8.8 | 0.56-0.63 | 29-37 | 120,000-240,000 |
| 1,000 | 5.7-6.4 | 7.5-9.0 | 0.55-0.62 | 30-38 | 150,000-300,000 |
| 1,500 | 5.8-6.5 | 7.5-9.0 | 0.54-0.61 | 30-40 | 220,000-450,000 |

> **Not:** Değerler su soğutmalı, R-134a soğutkanlı chillerlar için verilmiştir. ARI 550/590 standart koşullarında.

## Yağ Yönetimi

Vidalı kompresörlerde yağ yönetimi kritik bir konudur:

- **Yağ enjeksiyonlu (oil-flooded/oil-injected):** En yaygın tip. Yağ sıkıştırma sırasında rotor soğutması, sızdırmazlık ve yağlama sağlar.
- **Yağ ayırıcı (oil separator):** Basma hattında yağı soğutkandan ayırır. Ayırma verimi >%99.9 olmalı.
- **Yağ soğutucu (oil cooler):** Yağ sıcaklığını kontrol eder (tipik 40-60°C).
- **Yağ filtresi:** Kontaminasyonu önler, periyodik değişim gerekli (2000-4000 saat).
- **Yağ seviye kontrolü:** Düşük yağ seviyesi rotor hasarına yol açabilir.
- **Yağsız (oil-free) vidalı:** Mevcuttur ancak daha düşük verimli ve daha yüksek maliyetli. Farmasötik, gıda gibi yağ kontaminasyonuna hassas uygulamalarda tercih edilir.

## Avantajlar ve Dezavantajlar

### Avantajlar
- Sürekli (stepless) kapasite kontrolü (%25-100)
- Yüksek güvenilirlik ve uzun ömür (20-25 yıl)
- İyi kısmi yük performansı (özellikle su soğutmalıda)
- Kompakt tasarım (kapasite başına düşük hacim)
- Geniş kapasite aralığı (50-1,500 kW)
- Az sayıda hareketli parça (pistonluya göre)
- Sıvı soğutkan toleransı (sınırlı)

### Dezavantajlar
- Yağ yönetimi gerektirmesi (yağlı tipte)
- Scroll ve santrifüje göre daha yüksek gürültü seviyesi
- Vi uyumsuzluğunda verim kaybı
- Rotor profilinin zamanla aşınması
- Santrifüje göre daha düşük tam yük verimi (>500 kW'da)
- Bakım maliyeti scroll kompresöre göre daha yüksek

## Tipik Uygulamalar
- Orta ölçekli ticari binalar (AVM, otel, hastane)
- Endüstriyel proses soğutma
- Bölgesel soğutma (district cooling) — yardımcı chiller olarak
- Veri merkezi soğutma (orta kapasite)
- Gıda ve içecek endüstrisi
- Plastik enjeksiyon kalıp soğutma

## Dikkat Edilecekler

1. **Vi seçimi:** Kompresörün dahili hacim oranı (Vi) çalışma koşullarına uygun olmalı. Yanlış Vi seçimi %5-15 verim kaybına yol açar.
2. **Yağ sıcaklığı:** 65°C üzerinde yağ bozulması hızlanır, 40°C altında viskozite artar. 45-60°C aralığında tutulmalı.
3. **Slide valve pozisyonu:** Uzun süreli %25 altı çalışma kompresör yatağı ve rotorları için zararlıdır.
4. **Soğutkan şarjı:** Düşük soğutkan şarjı evaporatör performansını düşürür, yüksek şarj kondenseri su basabilir.
5. **Evaporatör kirlenme:** Yaklaşma sıcaklığı >5°C ise ısı transfer yüzeyleri temizlenmeli.
6. **Kondenser kirlenme:** CW tarafında kireç birikimi %10-20 kapasite kaybına yol açar. Yıllık kimyasal temizlik önerilir.
7. **Titreşim izleme:** Yatak aşınması veya rotor dengesizliği titreşim artışıyla kendini gösterir. ISO 10816 sınırları takip edilmeli.
8. **Exergy perspektifi:** Vidalı chillerlarda en büyük exergy iyileştirme fırsatı lift azaltmadır. CHW reset ve kondenser su optimizasyonu öncelikli değerlendirilmelidir.

## İlgili Dosyalar
- Buhar sıkıştırmalı chiller (genel): `equipment/chiller_vapor_compression.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Scroll chiller: `equipment/chiller_scroll.md`
- Soğutma kulesi: `equipment/cooling_tower.md`
- Chiller exergy hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller VSD uygulaması: `solutions/chiller_vsd.md`
- Chiller sistem optimizasyonu: `solutions/chiller_optimization.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, 2024 (Chapter 38: Compressors)
- ARI Standard 550/590 — Performance Rating of Water-Chilling and Heat Pump Packages
- Bitzer Screw Compressor Handbook, 2023
- Carrier Engineering Newsletter — Screw Chiller Technology
- Stoecker, W.F. "Industrial Refrigeration Handbook", McGraw-Hill, 1998
- Kotas, T.J. "The Exergy Method of Thermal Plant Analysis", Krieger Publishing, 1995
- EUROVENT Certification Programme — Liquid Chilling Packages
- ISO 10816 — Mechanical Vibration — Evaluation of Machine Vibration
- Trane Engineers Newsletter — Chiller Plant Design and Optimization
- DOE/FEMP — Best Practices for Chiller Plant Efficiency
