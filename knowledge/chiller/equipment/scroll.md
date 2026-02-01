---
title: "Scroll Kompresörlü Chiller — Scroll Compressor Chiller"
category: equipment
equipment_type: chiller
subtype: "Scroll"
keywords: [scroll chiller, küçük kapasite, sessiz]
related_files: [chiller/benchmarks.md, chiller/formulas.md, chiller/solutions/maintenance.md]
use_when: ["Scroll chiller analizi yapılırken", "Küçük ölçekli soğutma değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Scroll Kompresörlü Chiller — Scroll Compressor Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı, scroll (sarmal / salyangoz) kompresörlü
- Kapasite aralığı: 10-500 kW soğutma (3-140 ton)
- Kompresör yapısı: Orbital scroll hareketi (sabit + hareketli sarmal)
- Soğutkan: R-410A, R-407C, R-134a, R-32, R-1234ze(E), R-290 (propan)
- COP (tam yük, su soğutmalı): 4.5-6.0
- COP (tam yük, hava soğutmalı): 2.5-3.5
- IPLV/NPLV (su soğutmalı): 5.5-7.5
- Exergy verimi: %18-35
- Tipik ömür: 15-20 yıl
- Yaygın markalar: Carrier (30RB/30RQ), Trane (CGAM/CXAM), Daikin (EWAD/EWWD), Mitsubishi Electric, Climaveneta (Mitsubishi), Aermec, Clivet, Emerson Copeland (kompresör), Danfoss (kompresör)

## Çalışma Prensibi

Scroll kompresör, iki iç içe geçmiş sarmal (scroll) plakanın göreceli hareketi ile gazı sıkıştıran pozitif deplasmanlı bir kompresör tipidir. Basit yapısı, düşük gürültüsü ve yüksek güvenilirliği ile küçük-orta kapasite uygulamalarında en yaygın kullanılan kompresör tipidir.

### Orbital Scroll Hareketi

1. **Sabit scroll (fixed scroll):** Gövdeye sabitlenmiş sarmal plaka. Merkezi çıkış portuna sahiptir.
2. **Hareketli scroll (orbiting scroll):** Eksantrik mil (eccentric shaft) tarafından yörüngesel (orbital) hareketle döndürülen sarmal plaka. Kendi ekseni etrafında dönmez, sadece dairesel öteleme hareketi yapar.
3. **Sıkıştırma süreci:**
   - Gaz, sarmalların dış çevresinden emilir
   - İki scroll arasında oluşan cep (pocket) merkezine doğru ilerlerken hacmi küçülür
   - Gaz giderek sıkıştırılır ve merkezdeki çıkış portundan basılır
   - Her an birden fazla sıkıştırma cebi aktiftir → sürekli ve pulsasyonsuz basma

```
Sıkıştırma oranı (built-in):
  r_v = V_emme / V_basma

Burada:
  r_v    = dahili hacim oranı (tipik 2.0-4.0)
  V_emme = emme cebinin maksimum hacmi [cm³]
  V_basma = basma cebinin minimum hacmi [cm³]
```

### Scroll Kompresörün Temel Özellikleri
- Sadece 2 ana hareketli parça (sarmal + mil) → yüksek güvenilirlik
- Valf mekanizması yok (pistonlu kompresörün aksine) → düşük mekanik kayıp
- Sürekli sıkıştırma (pulsasyonsuz) → düşük titreşim ve gürültü
- Eksenel uyum (axial compliance): Sarmallar arasındaki mikro boşluk, basınç farkı ile kendiliğinden sıfırlanır → iyi sızdırmazlık
- Radyal uyum (radial compliance): Oldham bileziği (Oldham coupling) ile hareketli scrollun dönmesini engeller, sadece öteleme sağlar

## Kapasite Kontrolü

Scroll kompresörler yapıları gereği sabit kapasiteli (fixed speed) olarak çalışır. Kapasite kontrolü için farklı yöntemler kullanılır:

### 1. On/Off Kontrolü
- En basit yöntem: kompresör ya tam kapasitede çalışır ya da durur
- Sık start-stop (cycling) → verim kaybı, mekanik aşınma
- Küçük kapasitelerde ve tek kompresörlü sistemlerde yaygın

### 2. Tandem (Çoklu Kompresör) Çalışma
- 2-8 adet scroll kompresör paralel bağlanır
- Kademeli kapasite kontrolü sağlanır (örn. 4 kompresör: %25, %50, %75, %100)
- Her kompresör bağımsız on/off çalışır
- Eşit çalışma saati dağılımı (lead-lag rotation) yapılır

### 3. Digital Scroll Teknolojisi (Copeland)
- Emerson patentli teknoloji
- Üst scroll periyodik olarak kaldırılıp indirilir (yükleme-boşaltma)
- Yükleme süresi / toplam süre oranı ile kapasite ayarlanır
- Sürekli %10-100 kapasite kontrolü sağlar
- Konvansiyonel on/off'a göre %25-30 enerji tasarrufu (kısmi yükte)

```
Kapasite (digital scroll):
  Q = Q_nominal × (t_on / (t_on + t_off))

Burada:
  Q         = anlık soğutma kapasitesi [kW]
  Q_nominal = kompresörün nominal kapasitesi [kW]
  t_on      = yükleme süresi [s]
  t_off     = boşaltma süresi [s]
```

### 4. Inverter (VSD) Scroll
- Kompresör devri frekans konvertör ile değiştirilir
- Sürekli kapasite kontrolü: %25-100
- En iyi kısmi yük performansı
- Maliyet: standart scroll + %20-30
- DC inverter teknolojisi ile IE4+ motor verimleri

### Kısmi Yük Performans Karşılaştırması

| Yük (%) | On/Off COP (%) | Tandem COP (%) | Digital COP (%) | VSD COP (%) |
|---------|---------------|----------------|-----------------|-------------|
| 100 | %100 | %100 | %100 | %100 |
| 75 | %85 | %95 | %102 | %106 |
| 50 | %70 | %90 | %105 | %112 |
| 25 | %55 | %80 | %95 | %108 |

## Modüler Chiller Sistemleri

Scroll kompresörlerin en önemli uygulama alanlarından biri modüler chiller sistemleridir:

### Konsept
- 4-8 bağımsız soğutma modülü tek bir çerçevede birleştirilir
- Her modülde 1-2 scroll kompresör bulunur
- Toplam kapasite: 40-500 kW
- Kademeli kapasite kontrolü: örn. 8 modül = 8 kademe (%12.5 adım)

### Modüler Sistem Avantajları
- N+1 yedekleme (redundancy): Bir modül arızalansa diğerleri çalışmaya devam eder
- Kolay kapasite artışı: İhtiyaç arttıkça modül eklenir
- Kolay taşıma: Modüller ayrı ayrı taşınabilir (asansör, dar koridor)
- Düşük kısmi yük verimi kaybı: Çok sayıda kademe
- Bakım kolaylığı: Arızalı modül sistem çalışırken değiştirilebilir

## Enerji Dağılımı (Tipik Su Soğutmalı Scroll Chiller Sistemi)
- Kompresör elektrik tüketimi: ~%80-85
- Kondenser su pompası: ~%7-10
- CHW pompası: ~%5-8
- Soğutma kulesi fanı (su soğutmalı) veya kondenser fanı (hava soğutmalı): ~%3-7
- Kontrol ve yardımcı: ~%1-2

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

### Exergy Verimi Aralıkları

| Koşul | COP | Exergy Verimi (%) |
|-------|-----|-------------------|
| Su soğutmalı, tam yük | 5.0 | %23-28 |
| Su soğutmalı, %50 yük (tandem) | 5.2 | %24-30 |
| Su soğutmalı, %50 yük (VSD) | 5.8 | %27-33 |
| Hava soğutmalı, tam yük | 3.0 | %18-22 |
| Hava soğutmalı, %50 yük (VSD) | 3.5 | %20-26 |

**Scroll chillerların exergy veriminin santrifüj ve vidalıdan düşük olmasının sebepleri:**
- Daha küçük ısı değiştiriciler → daha yüksek yaklaşma sıcaklıkları → daha yüksek lift
- Scroll kompresörün kendisinin isentropik verimi (%65-78) santrifüj ve vidalıdan düşüktür
- Kapasite kontrolü (on/off, tandem) sürekli kontrol kadar verimli değildir

## Gürültü Seviyesi

Scroll kompresörlerin en önemli avantajlarından biri düşük gürültü seviyesidir:

| Kompresör Tipi | Tipik Gürültü (dBA @ 1m) | Karşılaştırma |
|---------------|--------------------------|---------------|
| Scroll | 62-72 | En sessiz |
| Vidalı (Screw) | 75-85 | Orta |
| Santrifüj | 68-80 | Düşük-orta |
| Pistonlu | 80-95 | En gürültülü |

Scroll kompresörün düşük gürültüsünün sebepleri:
- Pulsasyonsuz basma (valf darbesi yok)
- Az hareketli parça
- Dengeli orbital hareket (düşük titreşim)
- Bu özellik scroll chillerlari gürültüye hassas uygulamalarda (otel, hastane, ofis) öne çıkarır

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kompresör(ler) elektrik gücü | kW | 3-200 | Güç analizörü (3 faz) |
| CHW giriş sıcaklığı (return) | °C | 11-14 | PT100 sensör |
| CHW çıkış sıcaklığı (supply) | °C | 5-8 | PT100 sensör |
| CHW debisi | m³/h | Kapasiteye bağlı | Ultrasonik / EM flowmeter |
| CW giriş sıcaklığı (su soğutmalı) | °C | 28-35 | PT100 sensör |
| CW çıkış sıcaklığı (su soğutmalı) | °C | 33-40 | PT100 sensör |
| Ortam sıcaklığı (hava soğutmalı) | °C | 25-45 | Termometre |

### Opsiyonel
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| CW debisi | m³/h | Kapasiteye bağlı | Ultrasonik flowmeter |
| Emme basıncı | bar | 3-6 | Basınç transmiteri |
| Basma basıncı | bar | 10-25 | Basınç transmiteri |
| Kompresör akımı (her kompresör) | A | Etikete bağlı | Pens ampermetre |
| Kondenser fanı gücü (hava soğutmalı) | kW | 1-30 | Güç analizörü |
| Çalışan kompresör sayısı | adet | 1-8 | BMS / kontrol paneli |
| Kompresör çalışma saati | saat | — | Kontrol paneli |
| Start-stop sayısı | adet/saat | <6 | Kontrol paneli |
| Kompresör devri (VSD'li) | Hz | 25-70 | Frekans konvertör |

### Nameplate Bilgileri
- Marka ve model
- Nominal soğutma kapasitesi (kW veya ton)
- Nominal elektrik gücü (kW)
- Nominal COP / EER
- Kompresör sayısı ve tipleri
- Soğutkan tipi ve şarj miktarı (kg)
- Maksimum çalışma basıncı (bar)
- Nominal CHW sıcaklıkları
- Nominal CW sıcaklıkları veya dış ortam sıcaklığı
- Üretim yılı ve seri numarası

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| CHW supply sıcaklığı | 7°C | ARI standart |
| CHW return sıcaklığı | 12°C | ΔT = 5°C |
| CW giriş sıcaklığı | 30°C | Su soğutmalı, ARI standart |
| CW çıkış sıcaklığı | 35°C | ΔT = 5°C |
| Dış ortam sıcaklığı | 35°C | Hava soğutmalı, ARI standart |
| Tam yük COP (su soğutmalı) | 5.0 | Orta verimli scroll |
| Tam yük COP (hava soğutmalı) | 3.0 | Standart hava soğutmalı |
| Yük oranı (sezonluk) | %55 | Tipik ticari bina |
| Çalışma saati | 2000 saat/yıl | Küçük ticari, Türkiye |
| Kompresör sayısı | 2 | Tandem varsayım |
| Ortam sıcaklığı (T₀) | 25°C (298.15 K) | Exergy referansı |
| Elektrik birim fiyatı | 0.10 €/kWh | Ticari tarife |

## Performans Tablosu (Kapasiteye Göre)

| Kapasite (kW) | Komp. Sayısı | Tam Yük COP (Su Soğ.) | IPLV | kW/ton | Exergy Verimi (%) | Tahmini Yatırım (€) |
|--------------:|------------:|---------------------:|-----:|-------:|-------------------:|---------------------:|
| 10 | 1 | 4.2-4.8 | 5.0-6.0 | 0.73-0.84 | 18-22 | 5,000-10,000 |
| 30 | 1-2 | 4.5-5.2 | 5.5-6.5 | 0.68-0.78 | 20-25 | 10,000-22,000 |
| 60 | 2 | 4.8-5.5 | 5.8-7.0 | 0.64-0.73 | 22-28 | 18,000-38,000 |
| 100 | 2-4 | 5.0-5.6 | 6.0-7.2 | 0.63-0.70 | 23-29 | 28,000-55,000 |
| 200 | 4-6 | 5.2-5.8 | 6.2-7.5 | 0.61-0.68 | 24-31 | 50,000-100,000 |
| 300 | 4-8 | 5.3-5.9 | 6.5-7.5 | 0.60-0.66 | 25-32 | 75,000-150,000 |
| 500 | 6-8 | 5.5-6.0 | 6.5-7.5 | 0.59-0.64 | 26-35 | 120,000-240,000 |

> **Not:** Su soğutmalı, R-410A veya R-134a soğutkanlı chillerlar için ARI standart koşullarında verilmiştir. Hava soğutmalı için COP değerlerinden ~%40-45 düşürülmeli.

## Avantajlar ve Dezavantajlar

### Avantajlar
- **Basit yapı:** Az hareketli parça, yüksek güvenilirlik (MTBF > 80,000 saat)
- **Düşük gürültü:** Pulsasyonsuz sıkıştırma, gürültüye hassas uygulamalara uygun
- **Düşük titreşim:** Dengeli orbital hareket
- **Düşük bakım maliyeti:** Valf yok, basit yağlama sistemi, az parça
- **Kompakt boyut:** Kapasite başına küçük fiziksel ölçüler
- **Düşük ilk yatırım:** Vidalı ve santrifüje göre daha ekonomik
- **Modüler genişleme:** İhtiyaca göre kompresör/modül eklenmesi
- **Sıvı toleransı:** Kısa süreli sıvı dönüşüne (liquid slugging) dayanıklı (axial compliance sayesinde)
- **Hızlı başlatma:** Saniyeler içinde tam kapasiteye ulaşır

### Dezavantajlar
- **Sınırlı kapasite:** Tek kompresör maks. ~60-80 kW, sistem olarak 500 kW'a kadar
- **Düşük tam yük verimi:** Santrifüj ve vidalıya göre COP düşük (özellikle büyük kapasitelerde)
- **On/off kontrol kayıpları:** Standart scroll'da sürekli kapasite kontrolü yok (digital scroll ve VSD hariç)
- **Sabit hacim oranı:** Değişen koşullara uyum sağlayamaz (over/under compression)
- **Sınırlı basınç oranı:** Çok yüksek lift uygulamalarında verimsiz
- **Kısa ömür (nispeten):** Santrifüj (25-30 yıl) ve vidalıya (20-25 yıl) göre daha kısa (15-20 yıl)

## Tipik Uygulamalar
- Küçük-orta ticari binalar (ofisler, mağazalar, restoranlar)
- Otel ve butik otel
- Küçük hastane ve klinikler
- Okul ve eğitim binaları
- Küçük veri odaları (< 100 kW soğutma)
- Proses soğutma (plastik, baskı, lazer)
- Konfor soğutma (roof-top üniteleri)
- Isı pompası uygulamaları (reversible scroll)

## Dikkat Edilecekler

1. **Start-stop frekansı:** Kompresör saatte 6 defadan fazla start-stop yapmamalı. Sık cycling hem verim düşürür hem kompresör ömrünü kısaltır. Tampon tank (buffer tank) eklenmesi değerlendirilmeli.
2. **Minimum çalışma süresi:** Her start'ta en az 3 dakika çalışma süresi sağlanmalı. Kısa çalışma süreleri yağ dönüşünü olumsuz etkiler.
3. **Eşit çalışma saati:** Tandem veya modüler sistemlerde kompresörler arasında çalışma saati dengelemesi (lead-lag rotation) yapılmalı.
4. **Soğutkan şarjı:** Düşük şarj evaporatör superheat'i artırır (COP düşer), yüksek şarj sıvı dönüşü (liquid slugging) riskini artırır.
5. **Hava soğutmalıda kondenser bakımı:** Finli borulardaki toz ve kir birikimi kondenser basıncını artırır, COP %10-25 düşebilir. Mevsimsel temizlik yapılmalı.
6. **CHW debisi:** Minimum CHW debisi sağlanmalı. Düşük debi evaporatör donmasına yol açabilir. Minimum debi genellikle nominal debinin %50'sidir.
7. **Ortam sıcaklığı sınırları:** Hava soğutmalı scroll chillerlar genellikle 46-48°C'ye kadar çalışır. Türkiye'nin güneydoğu bölgelerinde yaz aylarında bu sınıra yaklaşılabilir.
8. **Exergy perspektifi:** Scroll chillerların exergy verimini iyileştirmek için: (a) VSD veya digital scroll seçimi, (b) CHW reset stratejisi (gerektiğinde daha yüksek CHW sıcaklığı), (c) hava soğutmalıda serbest soğutma (free cooling) ekonomizer entegrasyonu değerlendirilmelidir.

## İlgili Dosyalar
- Buhar sıkıştırmalı chiller (genel): `equipment/chiller_vapor_compression.md`
- Vidalı chiller: `equipment/chiller_screw.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Absorpsiyon chiller: `equipment/chiller_absorption.md`
- Soğutma kulesi: `equipment/cooling_tower.md`
- Chiller exergy hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller VSD uygulaması: `solutions/chiller_vsd.md`
- Free cooling: `solutions/free_cooling.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, 2024 (Chapter 38: Compressors)
- ARI Standard 550/590 — Performance Rating of Water-Chilling and Heat Pump Packages
- Emerson Climate Technologies — Copeland Scroll Compressor Handbook
- Carrier Engineering Newsletter — Scroll Chiller Technology
- Danfoss — Scroll Compressor Application Guide
- Kotas, T.J. "The Exergy Method of Thermal Plant Analysis", Krieger Publishing, 1995
- EUROVENT Certification Programme — Liquid Chilling Packages
- Stoecker, W.F., Jones, J.W. "Refrigeration and Air Conditioning", McGraw-Hill
- ASHRAE Standard 90.1 — Energy Standard for Buildings
- DOE/FEMP — Best Practices for Chiller Plant Optimization
