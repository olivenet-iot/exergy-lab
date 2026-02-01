---
title: "Soğutucu Akışkanlar — Refrigerants"
category: equipment
equipment_type: chiller
subtype: "Soğutucu Akışkanlar"
keywords: [soğutucu akışkan, R134a, R410A, GWP]
related_files: [chiller/equipment/systems_overview.md, chiller/benchmarks.md, chiller/equipment/vapor_compression.md]
use_when: ["Soğutucu akışkan seçimi değerlendirilirken", "Çevresel etki analizi yapılırken"]
priority: medium
last_updated: 2026-01-31
---
# Soğutucu Akışkanlar — Refrigerants

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Konu: Soğutma sistemlerinde kullanılan soğutucu akışkanların sınıflandırılması, termodinamik özellikleri, çevresel etkileri ve seçim kriterleri
- Uygulama alanı: Chiller sistemleri, split klimalar, endüstriyel soğutma, ısı pompaları, soğuk hava depoları
- Referans çevre koşulları: T₀ = 25°C (298.15 K), P₀ = 1 atm (101.325 kPa)
- Geçerli mevzuat: AB F-gaz Tüzüğü (EU 517/2014), Kigali Değişikliği (Montreal Protokolü), Türkiye F-gaz yönetmeliği
- Kritik trend: HFC'lerden düşük GWP'li alternatiflerine (HFO'lar ve doğal soğutucu akışkanlar) geçiş süreci hızlanmaktadır
- Güvenlik sınıflandırması: ASHRAE Standard 34 ve ISO 817

## Çalışma Prensibi

Soğutucu akışkanlar, buhar sıkıştırmalı soğutma çevriminde (vapour compression cycle) faz değişimi yoluyla ısı taşırlar. Temel çevrim:

1. **Evaporatör (buharlaştırıcı):** Düşük basınç ve sıcaklıkta sıvı soğutucu akışkan buharlaşarak ortamdan ısı çeker
2. **Kompresör:** Düşük basınçlı buharı yüksek basınca sıkıştırır — iş girdisi gerektirir
3. **Kondenser (yoğuşturucu):** Yüksek basınç ve sıcaklıkta buhar yoğuşarak ortama ısı verir
4. **Genleşme vanası:** Yüksek basınçlı sıvının basıncını ve sıcaklığını düşürür (izentalpik süreç)

Soğutucu akışkan seçimi, çevrimin verimini, çalışma basınçlarını, kompresör boyutunu ve güvenlik gereksinimlerini doğrudan belirler.

### İdeal Carnot COP ve Gerçek COP

```
COP_Carnot = T_evap / (T_cond - T_evap)

COP_gerçek = Q_evap / W_comp

Burada:
  T_evap   : Evaporatör sıcaklığı (K)
  T_cond   : Kondenser sıcaklığı (K)
  Q_evap   : Soğutma kapasitesi (kW)
  W_comp   : Kompresör gücü (kW)
  COP      : Performans katsayısı (boyutsuz)
```

Gerçek COP, Carnot COP'un %40-65'i arasındadır. Soğutucu akışkanın termodinamik özellikleri bu oranı etkiler.

## HFC Soğutucu Akışkanlar (Hidroflorokarbonlar)

### R-134a (1,1,1,2-Tetrafloroetan)
- Kimyasal formül: CH₂FCF₃
- Güvenlik sınıfı: A1 (düşük toksisite, yanmaz)
- Kritik sıcaklık: 101.1°C — orta sıcaklık uygulamaları için uygun
- Normal kaynama noktası: -26.1°C
- GWP₁₀₀: 1,430
- ODP: 0
- Uygulama: Orta kapasiteli su soğutma grupları (chiller), otomotiv klima, ticari soğutma
- Chiller tipi: Santrifüj chiller (büyük kapasite), vidalı chiller
- Durum: F-gaz tüzüğü kapsamında kademeli azaltma — yeni sistemlerde kullanımı kısıtlanmaktadır

### R-410A (R-32/R-125 karışımı, %50/%50 kütle)
- Tip: Zeotropik karışıma yakın (near-azeotropic), ancak pratikte azeotropik gibi davranır
- Güvenlik sınıfı: A1
- Kritik sıcaklık: 72.5°C — yüksek dış hava sıcaklıklarında performans düşer
- Normal kaynama noktası: -51.4°C
- GWP₁₀₀: 2,088
- ODP: 0
- Çalışma basıncı: R-22'den ~%60 daha yüksek — daha güçlü kompresör ve boru bağlantısı gerektirir
- Uygulama: Split klimalar, VRF/VRV sistemleri, küçük-orta chiller
- Durum: Yüksek GWP nedeniyle R-32 veya R-454B ile değiştirilmektedir

### R-407C (R-32/R-125/R-134a karışımı, %23/%25/%52 kütle)
- Tip: Zeotropik karışım — sıcaklık kayması (glide) ~7°C
- Güvenlik sınıfı: A1
- Kritik sıcaklık: 87.3°C
- Normal kaynama noktası: -43.6°C
- GWP₁₀₀: 1,774
- ODP: 0
- Uygulama: R-22 retrofit uygulamalarında yaygın, mevcut sistemlerin dönüşümü
- Özellik: Sıcaklık kayması nedeniyle karşı akışlı ısı değiştiricilerde avantajlı olabilir
- Durum: Kademeli olarak azaltılmaktadır

### R-32 (Diflorometan)
- Kimyasal formül: CH₂F₂
- Güvenlik sınıfı: A2L (düşük yanıcılık)
- Kritik sıcaklık: 78.1°C
- Normal kaynama noktası: -51.7°C
- GWP₁₀₀: 675
- ODP: 0
- Uygulama: Yeni nesil split klimalar, VRF sistemleri — R-410A'nın halefi
- Avantaj: R-410A'ya göre %68 daha düşük GWP, daha yüksek hacimsel soğutma kapasitesi
- Dezavantaj: A2L sınıfı — ek güvenlik önlemleri gerektirir (algılama, havalandırma)

## HFO Soğutucu Akışkanlar (Hidrofloroolefinler)

### R-1234ze(E) (Trans-1,3,3,3-Tetrafloropropen)
- Kimyasal formül: CHF=CHCF₃ (trans izomeri)
- Güvenlik sınıfı: A2L
- Kritik sıcaklık: 109.4°C — geniş çalışma aralığı
- Normal kaynama noktası: -19.0°C
- GWP₁₀₀: 7
- ODP: 0
- Uygulama: Büyük kapasiteli santrifüj chiller, yüksek sıcaklık ısı pompaları
- Avantaj: Ultra düşük GWP, iyi termodinamik özellikler, yüksek kritik sıcaklık
- Dezavantaj: R-134a'ya göre ~%20-25 daha düşük hacimsel kapasite — daha büyük kompresör gerektirir
- Durum: Yeni büyük chiller projelerinde hızla yaygınlaşmaktadır

### R-1234yf (2,3,3,3-Tetrafloropropen)
- Kimyasal formül: CH₂=CFCF₃
- Güvenlik sınıfı: A2L
- Kritik sıcaklık: 94.7°C
- Normal kaynama noktası: -29.5°C
- GWP₁₀₀: 4
- ODP: 0
- Uygulama: Otomotiv klima (R-134a'nın halefi), küçük soğutma sistemleri
- AB mevzuatı: 2017'den itibaren yeni otomobillerde zorunlu (MAC Direktifi 2006/40/EC)
- Not: Chiller uygulamalarında yaygın değil — daha çok otomotiv sektöründe kullanılır

## Doğal Soğutucu Akışkanlar

### R-290 (Propan)
- Kimyasal formül: C₃H₈
- Güvenlik sınıfı: A3 (düşük toksisite, yüksek yanıcılık)
- Kritik sıcaklık: 96.7°C
- Normal kaynama noktası: -42.1°C
- GWP₁₀₀: 3
- ODP: 0
- Uygulama: Küçük ticari soğutma, ısı pompaları, su soğutucuları (≤500 g şarj limiti IEC 60335-2-89)
- Avantaj: Mükemmel termodinamik özellikler, ucuz, doğada mevcut, R-22'ye çok benzer çalışma basıncı
- Dezavantaj: A3 yanıcılık — şarj miktarı sınırlaması, ATEX gereksinimi, kapalı alan kullanımı kısıtlı
- Termodinamik: R-22 ve R-404A ile benzer buharlaşma basıncı; COP açısından üstün

### R-717 (Amonyak)
- Kimyasal formül: NH₃
- Güvenlik sınıfı: B2L (yüksek toksisite, düşük yanıcılık)
- Kritik sıcaklık: 132.3°C
- Normal kaynama noktası: -33.3°C
- GWP₁₀₀: 0
- ODP: 0
- Uygulama: Büyük endüstriyel soğutma, soğuk hava depoları, gıda işleme, buz pistleri
- Avantaj: En yüksek termodinamik verim (COP), sıfır çevresel etki, sızıntı kolayca tespit edilir (koku)
- Dezavantaj: Toksik (TLV-TWA: 25 ppm), bakır ve bakır alaşımlarına korozif, makine dairesi gereksinimi
- Kapasite: Tipik olarak 100 kW - 10+ MW — küçük sistemlerde kullanılmaz

### R-744 (Karbondioksit / CO₂)
- Kimyasal formül: CO₂
- Güvenlik sınıfı: A1
- Kritik sıcaklık: 31.0°C — çoğu uygulamada transkritik çevrim gerektirir
- Normal kaynama noktası: -78.5°C (süblime)
- GWP₁₀₀: 1 (referans değer)
- ODP: 0
- Çalışma basıncı: 35-130 bar — çok yüksek basınç, özel ekipman gerektirir
- Uygulama: Süpermarket soğutma (transkritik booster), su ısıtma (ısı pompası), endüstriyel soğutma
- Avantaj: Yanmaz, toksik değil, ucuz, yüksek hacimsel kapasite, düşük sıcaklıkta iyi COP
- Dezavantaj: Yüksek çalışma basıncı, düşük kritik sıcaklık (sıcak iklimlerde COP düşer), özel kompresör

## ODP ve GWP Değerleri Tablosu

| Soğutucu Akışkan | Kimyasal Formül / Bileşim | Tip | ODP | GWP₁₀₀ | Güvenlik Sınıfı | Kaynama Noktası (°C) |
|-------------------|---------------------------|-----|-----|---------|-----------------|----------------------|
| R-12 (Freon-12) | CCl₂F₂ | CFC | 1.0 | 10,900 | A1 | -29.8 |
| R-22 | CHClF₂ | HCFC | 0.055 | 1,810 | A1 | -40.8 |
| R-134a | CH₂FCF₃ | HFC | 0 | 1,430 | A1 | -26.1 |
| R-410A | R-32/R-125 | HFC | 0 | 2,088 | A1 | -51.4 |
| R-407C | R-32/R-125/R-134a | HFC | 0 | 1,774 | A1 | -43.6 |
| R-32 | CH₂F₂ | HFC | 0 | 675 | A2L | -51.7 |
| R-404A | R-125/R-143a/R-134a | HFC | 0 | 3,922 | A1 | -46.2 |
| R-507A | R-125/R-143a | HFC | 0 | 3,985 | A1 | -46.7 |
| R-1234ze(E) | CHF=CHCF₃ | HFO | 0 | 7 | A2L | -19.0 |
| R-1234yf | CH₂=CFCF₃ | HFO | 0 | 4 | A2L | -29.5 |
| R-513A | R-1234yf/R-134a | HFO blend | 0 | 631 | A1 | -29.2 |
| R-514A | R-1234yf/R-134a | HFO blend | 0 | 2 | B1 | 29.0 |
| R-290 (Propan) | C₃H₈ | Doğal | 0 | 3 | A3 | -42.1 |
| R-717 (Amonyak) | NH₃ | Doğal | 0 | 0 | B2L | -33.3 |
| R-744 (CO₂) | CO₂ | Doğal | 0 | 1 | A1 | -78.5 |
| R-600a (İzobütan) | C₄H₁₀ | Doğal | 0 | 3 | A3 | -11.7 |
| R-718 (Su) | H₂O | Doğal | 0 | 0 | A1 | 100.0 |

## Enerji Dağılımı (Tipik Soğutma Çevrimi — Su Soğutma Grubu)

| Enerji Akışı | Oran (%) | Açıklama |
|--------------|----------|----------|
| Soğutma kapasitesi (evaporatör) | 100 (referans) | Faydalı soğutma işi |
| Kompresör gücü | 17-33 | COP 3.0-6.0 arasına karşılık gelir |
| Kondenser ısı atımı | 117-133 | Soğutma kapasitesi + kompresör gücü |
| Ekserji yıkımı — kompresör | 5-10 | İzentropik olmayan sıkıştırma |
| Ekserji yıkımı — kondenser | 3-7 | Sonlu sıcaklık farkı |
| Ekserji yıkımı — evaporatör | 2-5 | Sonlu sıcaklık farkı |
| Ekserji yıkımı — genleşme vanası | 3-8 | İzentalpik (tersinmez) genleşme |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Soğutucu akışkan tipi | — | Etiket | Nameplate bilgisi |
| Evaporatör giriş/çıkış su sıcaklığı | °C | 6-15 / 5-12 | PT100 sensör |
| Kondenser giriş/çıkış su sıcaklığı | °C | 28-35 / 33-42 | PT100 sensör |
| Soğutma kapasitesi | kW veya ton | Sisteme bağlı | Enerji sayacı veya hesaplama |
| Kompresör elektrik tüketimi | kW | Sisteme bağlı | Güç analizörü |
| Emme basıncı (evaporatör) | bar | Akışkana bağlı | Basınç sensörü (manometre) |
| Basma basıncı (kondenser) | bar | Akışkana bağlı | Basınç sensörü (manometre) |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kızgınlık (superheat) | K | 3-10 | Emme hattı sıcaklık - doyma sıcaklığı |
| Alt soğuma (subcooling) | K | 2-8 | Doyma sıcaklığı - kondenser çıkış sıcaklığı |
| Kompresör devri | RPM | 1000-6000 | Takometre / VSD okuma |
| Yağ sıcaklığı | °C | 40-70 | Sıcaklık sensörü |
| Elektrik akımı | A | Motora bağlı | Pens ampermetre |
| Soğutucu akışkan şarj miktarı | kg | Sisteme bağlı | Tartım veya kayıt |

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Soğutucu akışkan (chiller) | R-134a | Mevcut stokta en yaygın |
| Soğutucu akışkan (split/VRF) | R-410A | Türkiye pazarında en yaygın |
| Evaporatör çıkış suyu sıcaklığı | 7°C | Standart konfor soğutma |
| Kondenser giriş suyu sıcaklığı | 30°C | Soğutma kulesi ile tipik |
| Kızgınlık (superheat) | 5 K | Normal çalışma |
| Alt soğuma (subcooling) | 4 K | Normal çalışma |
| COP (su soğutmalı chiller) | 5.0 | Tam yükte, R-134a |
| COP (hava soğutmalı chiller) | 3.0 | Tam yükte, 35°C dış hava |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |
| Yıllık çalışma saati | 2,500 saat/yıl | Türkiye, ticari bina soğutma sezonu |

## Performans Tablosu — Soğutucu Akışkana Göre Chiller Karşılaştırması

| Soğutucu Akışkan | Chiller Tipi | Kapasite Aralığı (kW) | Tipik COP | Ekserji Verimi (%) | GWP₁₀₀ | Yaklaşık Fiyat Farkı (%) |
|-------------------|--------------|-----------------------|-----------|---------------------|---------|--------------------------|
| R-134a | Santrifüj, vidalı | 200-10,000 | 5.0-6.5 | 35-50 | 1,430 | Referans |
| R-1234ze(E) | Santrifüj | 300-10,000 | 4.8-6.3 | 33-48 | 7 | +10-20 |
| R-513A | Santrifüj, vidalı | 200-8,000 | 4.9-6.4 | 34-49 | 631 | +5-15 |
| R-410A | Scroll, vidalı | 20-2,000 | 3.0-5.5 | 25-40 | 2,088 | Referans |
| R-32 | Scroll, vidalı | 20-1,500 | 3.2-5.7 | 27-42 | 675 | +0-5 |
| R-290 (Propan) | Scroll, vidalı | 10-500 | 3.3-5.8 | 28-43 | 3 | +5-15 |
| R-717 (Amonyak) | Vidalı, pistonlu | 100-10,000+ | 3.5-6.0 | 30-48 | 0 | +15-30 |
| R-744 (CO₂) | Pistonlu, transkritik | 10-500 | 2.5-4.5 | 20-35 | 1 | +20-40 |

## Termodinamik Özellikler Karşılaştırma Tablosu

| Özellik | R-134a | R-1234ze(E) | R-410A | R-32 | R-290 | R-717 | R-744 |
|---------|--------|-------------|--------|------|-------|-------|-------|
| Molekül ağırlığı (g/mol) | 102.0 | 114.0 | 72.6 | 52.0 | 44.1 | 17.0 | 44.0 |
| Kritik sıcaklık (°C) | 101.1 | 109.4 | 72.5 | 78.1 | 96.7 | 132.3 | 31.0 |
| Kritik basınç (bar) | 40.6 | 36.4 | 49.0 | 57.8 | 42.5 | 113.3 | 73.8 |
| Buharlaşma ısısı @ 0°C (kJ/kg) | 198 | 184 | 221 | 315 | 374 | 1,262 | 234 |
| Hacimsel kapasite @ 0°C (kJ/m³) | 2,868 | 2,296 | 6,763 | 7,307 | 3,907 | 4,382 | — |
| Basınç @ 0°C (bar) | 2.93 | 2.14 | 7.99 | 8.13 | 4.74 | 4.30 | 34.9 |
| Basınç @ 40°C (bar) | 10.2 | 7.67 | 24.3 | 24.8 | 13.7 | 15.6 | 102 |
| Basınç oranı (40°C/0°C) | 3.48 | 3.59 | 3.04 | 3.05 | 2.89 | 3.63 | 2.92 |

## Güvenlik Sınıflandırması (ASHRAE 34 / ISO 817)

| Sınıf | Toksisite | Yanıcılık | Açıklama | Örnekler |
|-------|-----------|-----------|----------|----------|
| A1 | Düşük (OEL >400 ppm) | Yanmaz | En güvenli — makine dairesi gereksinimi minimum | R-134a, R-410A, R-407C, R-744, R-513A |
| A2L | Düşük | Düşük yanıcılık (yanma hızı ≤10 cm/s) | Hafif yanıcı — algılama ve havalandırma gerekli | R-32, R-1234ze(E), R-1234yf |
| A2 | Düşük | Yanıcı | Yanıcı — güvenlik önlemleri gerekli | R-152a |
| A3 | Düşük | Yüksek yanıcılık | Patlayıcı ortam riski — ATEX gereksinimi | R-290, R-600a |
| B1 | Yüksek (OEL ≤400 ppm) | Yanmaz | Toksik — makine dairesi zorunlu | R-123, R-514A |
| B2L | Yüksek | Düşük yanıcılık | Toksik ve hafif yanıcı — özel makine dairesi | R-717 (Amonyak) |

## F-gaz Tüzüğü ve Kademeli Azaltma Takvimi

### AB F-gaz Tüzüğü (EU 517/2014) — HFC Kota Azaltma

| Yıl | AB HFC Kotası (2015 bazlı CO₂-eq %) | Açıklama |
|-----|--------------------------------------|----------|
| 2015 | %100 | Referans yıl |
| 2016-2017 | %93 | Başlangıç azaltma |
| 2018-2020 | %63 | Birinci büyük azaltma |
| 2021-2023 | %45 | İkinci büyük azaltma |
| 2024-2026 | %31 | Üçüncü büyük azaltma |
| 2027-2029 | %24 | Dördüncü azaltma |
| 2030 ve sonrası | %21 | Kalıcı seviye |

### AB F-gaz — Önemli Yasaklar

| Yürürlük Tarihi | Yasak | Etkilenen Ekipman |
|------------------|-------|-------------------|
| 2020 | GWP ≥2,500 sabit soğutma | R-404A, R-507A ile yeni sistemler |
| 2022 | GWP ≥150 split klima ≤3 kg şarj | Küçük split sistemler |
| 2025 | GWP ≥750 monoblok klima ≤3 kg | Monoblok klimalar |
| Servis yasakları | 2030'dan itibaren GWP ≥2,500 geri dönüşümsüz soğutucu ile servis yasağı | Mevcut sistemler |

### Kigali Değişikliği (2016) — Küresel HFC Azaltma

```
Grup 1 ülkeler (gelişmiş): 2019 başlangıç, 2036'da %85 azaltma
Grup 2 ülkeler (gelişmekte olan çoğunluk): 2024 başlangıç, 2045'te %80 azaltma
Grup 3 ülkeler (sıcak iklim): 2028 başlangıç, 2047'de %85 azaltma

Burada:
  Azaltma oranları referans yıl bazında CO₂ eşdeğeri olarak hesaplanır
  Türkiye: Grup 2 kapsamında — 2024'ten itibaren kademeli azaltma
```

## Soğutucu Akışkan Seçim Kriterleri

Seçimde aşağıdaki kriterler değerlendirilmelidir:

1. **Kapasite gereksinimi:** Hacimsel soğutma kapasitesi — kompresör boyutunu belirler
2. **Çalışma sıcaklık aralığı:** Evaporatör ve kondenser sıcaklıklarına uygunluk
3. **Güvenlik sınıfı:** A1 (yanmaz, toksik değil) en az kısıtlama gerektirir
4. **GWP değeri:** Düşük GWP, mevzuat uyumu ve gelecek güvencesi sağlar
5. **Enerji verimliliği:** Daha yüksek COP, daha düşük işletme maliyeti
6. **Çalışma basıncı:** Yüksek basınç, daha güçlü ve pahalı ekipman gerektirir
7. **Malzeme uyumluluğu:** O-ring, conta, yağ ve malzeme uyumu kontrol edilmeli
8. **Maliyet:** Soğutucu akışkan fiyatı, ekipman fiyatı ve toplam sahip olma maliyeti
9. **Servis ve bakım:** Yerel tedarik, teknisyen yetkinliği, kaçak algılama

## Chiller Tipi ve Soğutucu Akışkan Eşleştirme Tablosu

| Chiller Tipi | Kapasite (kW) | Yaygın Soğutucu Akışkanlar | Gelecek Alternatifler |
|--------------|---------------|----------------------------|-----------------------|
| Scroll (hava soğutmalı) | 20-500 | R-410A, R-407C | R-32, R-290, R-454B |
| Vidalı (su soğutmalı) | 200-2,000 | R-134a, R-407C | R-1234ze(E), R-513A |
| Vidalı (hava soğutmalı) | 200-1,500 | R-134a, R-410A | R-1234ze(E), R-513A |
| Santrifüj (su soğutmalı) | 500-10,000+ | R-134a, R-123 | R-1234ze(E), R-514A |
| Absorpsiyon (tek etkili) | 100-5,000 | Su/LiBr | Su/LiBr (değişmez) |
| Absorpsiyon (çift etkili) | 200-10,000 | Su/LiBr | Su/LiBr (değişmez) |
| Amonyak vidalı | 200-10,000+ | R-717 | R-717 (değişmez) |
| CO₂ transkritik | 10-500 | R-744 | R-744 (değişmez) |

## Çevresel Etki Karşılaştırması

Toplam eşdeğer ısınma etkisi (TEWI — Total Equivalent Warming Impact):

```
TEWI = GWP × m × L × n + GWP × m × (1 - α) + n × E × β

Burada:
  GWP   : Soğutucu akışkanın küresel ısınma potansiyeli (kg CO₂-eq/kg)
  m     : Toplam soğutucu akışkan şarjı (kg)
  L     : Yıllık kaçak oranı (oran, tipik 0.02-0.10)
  n     : Sistem ömrü (yıl)
  α     : Ömür sonu geri kazanım oranı (tipik 0.80-0.95)
  E     : Yıllık enerji tüketimi (kWh/yıl)
  β     : Elektrik üretimi emisyon faktörü (kg CO₂/kWh, Türkiye ~0.47)
```

Çoğu uygulamada dolaylı emisyon (enerji tüketimi) toplam etkinin %70-90'ını oluşturur. Bu nedenle enerji verimliliği, düşük GWP'den bile daha önemli olabilir.

## Dikkat Edilecekler

1. **Mevzuat takibi:** F-gaz tüzüğü ve Kigali Değişikliği kapsamında GWP sınırları sürekli sıkılaşmaktadır — yeni yatırımlarda düşük GWP'li akışkanlar tercih edilmelidir
2. **A2L güvenlik gereksinimleri:** R-32 ve HFO'lar A2L sınıfındadır — makine dairesinde gaz algılama, havalandırma ve elektrik sınıflandırması gerektirir
3. **Retrofit uyumluluğu:** Mevcut sistemlerde soğutucu akışkan değişimi yapılırken yağ, conta, genleşme vanası ve kontrol sistemi uyumluluğu mutlaka kontrol edilmelidir
4. **Kaçak önleme:** Yüksek GWP'li akışkanlarda düzenli kaçak kontrolü zorunludur (AB: ≥5 ton CO₂-eq sistemlerde yılda en az 1 kez)
5. **Şarj miktarı sınırlamaları:** R-290 (A3) için IEC 60335-2-89'a göre şarj limitleri mevcuttur — 150 g/m³ oda hacmi veya 500 g toplam şarj
6. **Transkritik CO₂ sınırlamaları:** Sıcak iklimlerde (Türkiye güney kıyıları gibi) R-744 transkritik sistemlerin COP'u önemli ölçüde düşer — paralel sıkıştırmalı veya ejektörlü tasarımlar değerlendirilmelidir
7. **Amonyak güvenliği:** R-717 kullanan sistemlerde EN 378'e uygun makine dairesi, gaz algılama, havalandırma ve acil durum prosedürleri zorunludur

## İlgili Dosyalar
- Soğutma kulesi: `equipment/cooling_tower.md`
- Soğutma suyu sistemleri genel bakış: `equipment/chilled_water_systems.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Chiller seçim ve boyutlandırma: `solutions/chiller_selection.md`
- VSD chiller optimizasyonu: `solutions/chiller_vsd.md`
- Serbest soğutma (free cooling): `solutions/chiller_free_cooling.md`
- Soğutma benchmark verileri: `benchmarks/chiller_benchmarks.md`

## Referanslar
- ASHRAE Standard 34-2022. *Designation and Safety Classification of Refrigerants*. ASHRAE.
- ASHRAE Handbook — Fundamentals (2025), Chapter 29: Thermophysical Properties of Refrigerants.
- EU Regulation No 517/2014 of the European Parliament and of the Council on fluorinated greenhouse gases.
- Directive 2006/40/EC (MAC Directive) relating to emissions from air-conditioning systems in motor vehicles.
- Montreal Protocol, Kigali Amendment (2016). HFC Phase-down Schedule.
- IEC 60335-2-89:2019. *Household and similar electrical appliances — Safety — Part 2-89: Commercial refrigerating appliances*.
- EN 378-1:2016. *Refrigerating systems and heat pumps — Safety and environmental requirements*.
- ISO 817:2014. *Refrigerants — Designation and safety classification*.
- Calm, J.M. & Hourahan, G.C. (2011). "Physical, Safety, and Environmental Data for Current and Alternative Refrigerants," Proc. 23rd IIR Int. Congress of Refrigeration.
- McLinden, M.O. et al. (2017). "New Refrigerants and System Configurations for Vapor-Compression Refrigeration," *Science*, 355(6329), 1062-1066.
- Mota-Babiloni, A. et al. (2017). "Analysis based on EU Regulation No 517/2014 of new HFC/HFO mixtures as alternatives of high GWP refrigerants," *Int. J. Refrig.*, 82, 97-106.
- Dincer, I. & Kanoglu, M. (2010). *Refrigeration Systems and Applications*, 2nd Edition, Wiley.
- UNEP (2023). *Technology and Economic Assessment Panel (TEAP) Report on HFC Phase-Down*.
