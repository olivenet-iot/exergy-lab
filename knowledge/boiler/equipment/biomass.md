# Biyokütle Kazanı — Biomass Boiler

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Biyokütle yakıtlı kazan (solid biomass-fired boiler)
- Yakıt tipleri: Odun peleti (wood pellet), odun yongası (wood chip), tarımsal atık (agricultural waste), saman/sap (straw), pirina (olive pomace), fındık kabuğu (nut shells)
- Kapasite aralığı: 50 kW - 50 MW (termal)
- Basınç aralığı: 5 - 40 bar (buhar kazanları), 3 - 6 bar (sıcak su kazanları)
- Enerji verimi (LHV bazlı): %75-90 (pelette en yüksek, yaş odun yongasında en düşük)
- Ekserji verimi: %25-40 (yanma tersinmezliği nedeniyle düşük)
- Izgara tipleri: Sabit ızgara (fixed grate), hareketli ızgara (moving grate), akışkan yatak (fluidized bed)
- Yaygın markalar: KWB, Hargassner, Herz, Viessmann, Polytechnik, Schmid, Justsen, Uniconfort
- Biyokütle kazanları IPCC metodolojisinde karbon nötr kabul edilir; ancak ekserji analizinde yanma ekserjisi diğer yakıtlarla aynı prensiple hesaplanır
- Yakıt bazlı detaylar için bkz. `equipment/boiler_fuels.md`

## Çalışma Prensibi

### Yakıt Besleme Sistemleri (Fuel Feeding Systems)
Katı biyokütle yakıtlar otomatik veya yarı-otomatik sistemlerle yanma odasına taşınır:
- **Helezon (screw conveyor)**: En yaygın yöntem; pellet ve ince yonga için idealdir. Geri tutuşma riski nedeniyle döner vana (rotary valve) veya düşme bölgesi (drop section) gerektirir
- **Piston besleyici (ram feeder)**: Kaba yonga ve iri parçalı yakıtlar için uygundur. Aralıklı itme ile yanma odasına besleme yapar
- **Titreşimli ızgara beslemesi (vibrating grate feed)**: Düzensiz boyutlu tarımsal atıklar (saman balyası, pirina) için tercih edilir
- **Pnömatik besleme**: Toz halinde yakıtlar (talaş, un tozu) için kullanılır; pülverize yanma sistemlerinde

### Yanma Aşamaları (Combustion Stages)
Katı biyokütle yanması dört aşamada gerçekleşir:
1. **Kurutma (drying)**: Yakıttaki nem buharlaştırılır (100-150°C). Yüksek nemli yakıtlarda bu aşama toplam enerjinin önemli kısmını tüketir
2. **Piroliz (pyrolysis)**: Uçucu maddelerin salınımı (200-500°C). Gaz fazında yanıcı bileşenler açığa çıkar
3. **Gaz fazı yanması (volatile combustion)**: Piroliz gazlarının alev bölgesinde yanması (600-1,200°C)
4. **Kor/kömür yanması (char combustion)**: Kalan katı karbon ızgara üzerinde yanar (800-1,100°C). Bu aşama en yavaş adımdır ve ızgara tasarımını belirler

### Birincil ve İkincil Hava Kontrolü (Primary/Secondary Air)
- **Birincil hava (primary air)**: Izgaranın altından verilir; kor yanmasını kontrol eder. Tipik oran: toplam havanın %40-60'ı
- **İkincil hava (secondary air)**: Yanma odasının üst bölgesinden enjekte edilir; uçucu gazların tam yanmasını sağlar. Tipik oran: toplam havanın %40-60'ı
- Hava fazlası katsayısı (λ): 1.30-1.60 (ızgaralı), 1.15-1.30 (akışkan yataklı)

### Izgara Tipleri (Grate Types)
| Izgara Tipi | Kapasite Aralığı | Uygun Yakıtlar | Avantaj | Dezavantaj |
|-------------|------------------|----------------|---------|------------|
| Sabit ızgara (fixed grate) | 50 kW - 2 MW | Pellet, kuru yonga | Basit, düşük maliyet | Düşük kapasite, kül çıkarma manuel |
| Hareketli ızgara (moving grate) | 500 kW - 30 MW | Her tür biyokütle | Otomatik kül çıkarma, geniş yakıt esnekliği | Mekanik bakım gereksinimi |
| Akışkan yatak (fluidized bed) | 5 MW - 50+ MW | Düşük kaliteli yakıt, karışımlar | Çok yakıtlı çalışma, düşük emisyon | Yüksek yatırım maliyeti, fan enerjisi |

## Yakıt Tipleri ve Özellikleri

| Yakıt | LHV (kJ/kg) | Nem (%) | Kül (%) | Kimyasal Ekserji (kJ/kg) | φ (ekserji/enerji) | Yığın Yoğunluğu (kg/m³) |
|-------|-------------|---------|---------|--------------------------|---------------------|--------------------------|
| Odun peleti (wood pellet) | 17,000-19,000 | 8-10 | 0.5-1.0 | 19,500-22,000 | 1.12-1.16 | 600-700 |
| Odun yongası — kuru (wood chip, dry) | 12,000-15,000 | 20-30 | 1-3 | 14,000-17,500 | 1.10-1.18 | 200-300 |
| Odun yongası — yaş (wood chip, wet) | 8,000-10,000 | 40-50 | 1-3 | 9,500-12,000 | 1.10-1.18 | 300-450 |
| Saman (straw) | 14,000-15,000 | 10-20 | 5-8 | 16,000-17,500 | 1.12-1.15 | 80-150 |
| Pirina (olive pomace) | 16,000-18,000 | 10-15 | 3-5 | 18,500-21,000 | 1.14-1.17 | 550-700 |
| Fındık kabuğu (nut shells) | 15,000-17,000 | 8-12 | 1-3 | 17,500-20,000 | 1.13-1.16 | 300-450 |

Nem içeriğinin ısıl değere etkisi:

```
LHV_yaş = LHV_kuru × (1 - W) - 2,443 × W

Burada:
  LHV_yaş  : Yaş bazda alt ısıl değer (kJ/kg)
  LHV_kuru : Kuru bazda alt ısıl değer (kJ/kg)
  W        : Nem oranı (kg su / kg yaş yakıt), 0-1 arası
  2,443    : Suyun buharlaşma ısısı (kJ/kg, 25°C'de)
```

## Enerji Dağılımı (Tipik — Hareketli Izgaralı, Odun Peleti)
- Faydalı ısı çıkışı (buhar veya sıcak su): ~85-88%
- Baca gazı kayıpları (flue gas losses): ~8-12%
- Kül ile taşınan ısı kaybı (unburnt in ash): ~0.5-2%
- Radyasyon ve konveksiyon kayıpları (radiation/convection): ~1-2%
- Nem buharlaştırma kaybı (moisture evaporation): ~2-5% (yakıt nemine bağlı)

Yaş odun yongası (%45 nem) ile enerji dağılımı önemli ölçüde değişir:
- Faydalı ısı çıkışı: ~75-80%
- Baca gazı kayıpları: ~10-15%
- Nem buharlaştırma kaybı: ~6-10%
- Kül ve radyasyon kayıpları: ~2-3%

## Kül Yönetimi (Ash Management)

### Kül Tipleri
- **Taban külü (bottom ash)**: Izgaradan düşen kül; toplam külün %60-80'i. Mekanik olarak toplanır
- **Uçucu kül (fly ash)**: Baca gazı ile taşınan ince kül; toplam külün %20-40'ı. Siklon veya torba filtre ile tutulur

### Kül Miktarları (Tipik)
| Yakıt | Kül Oranı (%) | Kül Miktarı (kg/MWh) |
|-------|---------------|----------------------|
| Odun peleti | 0.5-1.0 | 2-5 |
| Odun yongası | 1-3 | 5-15 |
| Saman | 5-8 | 25-45 |
| Pirina | 3-5 | 15-25 |
| Fındık kabuğu | 1-3 | 5-15 |

### Kül Eritme Sıcaklığı (Ash Fusion Temperature)
Kül eritme sıcaklığı düşük olan yakıtlarda (saman, tarımsal atık) ızgara üzerinde cüruflaşma (slagging) riski yüksektir:
- Odun: 1,200-1,400°C (düşük risk)
- Saman: 800-1,000°C (yüksek risk — potasyum ve silisyum etkisi)
- Pirina: 1,000-1,200°C (orta risk)

Cüruflaşma riski yüksek yakıtlarda yanma odası sıcaklığının 900°C altında tutulması önerilir.

## Emisyon Özellikleri

| Emisyon Parametresi | Pellet Kazan | Yonga Kazan | Saman Kazan | AB Sınır Değeri (1-50 MW) |
|---------------------|-------------|-------------|-------------|--------------------------|
| Partikül madde (PM) | 10-30 mg/Nm³ | 30-80 mg/Nm³ | 50-150 mg/Nm³ | 20-50 mg/Nm³ |
| NOx (NO₂ olarak) | 100-200 mg/Nm³ | 150-300 mg/Nm³ | 200-400 mg/Nm³ | 300-500 mg/Nm³ |
| CO | 20-100 mg/Nm³ | 50-200 mg/Nm³ | 100-400 mg/Nm³ | 200-500 mg/Nm³ |
| SOx | <10 mg/Nm³ | <20 mg/Nm³ | 20-80 mg/Nm³ | 200-400 mg/Nm³ |

### Baca Gazı Temizleme Gereksinimleri
- **Siklon (cyclone)**: Temel partikül tutucu; büyük parçaları ayırır. Genellikle tüm tesislerde standart
- **Elektrostatik çöktürücü (ESP)** veya **torba filtre (bag filter)**: Katı AB emisyon limitleri için gerekli; PM'yi 10 mg/Nm³ altına indirebilir
- **SNCR/SCR**: Yüksek NOx'lu yakıtlarda (saman, tarımsal atık) azot oksit kontrolü için gerekebilir

### Karbon Nötr Değerlendirme
- Biyokütle yanması IPCC metodolojisinde karbon nötr kabul edilir — yaşam döngüsünde CO₂ dengesi sıfır
- Ancak tedarik zinciri emisyonları (hasat, taşıma, işleme) dahil edildiğinde net emisyon 5-25 kg CO₂/GJ arasındadır
- Ekserji analizinde karbon nötrlük muafiyeti uygulanmaz; yanma tersinmezliği diğer yakıtlarla aynı şekilde hesaplanır

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Yakıt tüketimi | kg/h veya ton/gün | 10-10,000 | Tartı bandı, silo seviye farkı |
| Yakıt nemi | % | 8-50 | Nem ölçer (moisture meter), laboratuvar analizi |
| Buhar/sıcak su debisi | ton/h veya m³/h | 0.1-60 | Debimetre (flowmeter) |
| Buhar basıncı | bar | 5-40 | Manometre veya basınç transmitteri |
| Buhar/su çıkış sıcaklığı | °C | 80-350 | Termokupl veya PT100 |
| Besleme suyu sıcaklığı | °C | 40-120 | Termokupl veya PT100 |
| Baca gazı sıcaklığı | °C | 120-250 | Termokupl |
| Baca gazı O₂ içeriği | % | 4-10 | Zirconia O₂ analizörü |

### Opsiyonel (Detaylı Ekserji Analizi)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Baca gazı CO içeriği | ppm | 20-400 | NDIR gaz analizörü |
| Baca gazı CO₂ içeriği | % | 8-16 | NDIR gaz analizörü |
| Kül miktarı ve yanmamış karbon | % | 0.5-5 | Laboratuvar analizi |
| Yakıt elemental analizi (C, H, O, N, S) | % | - | Laboratuvar analizi |
| Yakıt kalorifik değer (LHV) | kJ/kg | 8,000-19,000 | Bomba kalorimetre |
| Ortam sıcaklığı | °C | 0-40 | Termometre |
| Birincil/ikincil hava debisi | m³/h | - | Anemometre veya pitot tüp |

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Odun peleti LHV | 17,500 kJ/kg | EN-Plus A1 sertifikalı |
| Odun yongası (kuru) LHV | 13,500 kJ/kg | %25 nem bazında |
| Odun yongası (yaş) LHV | 9,000 kJ/kg | %45 nem bazında |
| Pirina LHV | 17,000 kJ/kg | %12 nem bazında |
| Saman LHV | 14,500 kJ/kg | %15 nem bazında |
| Fındık kabuğu LHV | 16,000 kJ/kg | %10 nem bazında |
| Pellet kazan verimi | %88 | LHV bazlı, iyi bakımlı |
| Kuru yonga kazan verimi | %83 | LHV bazlı, %25 nem |
| Yaş yonga kazan verimi | %76 | LHV bazlı, %45 nem |
| Hava fazlası katsayısı (λ) | 1.40 | Hareketli ızgaralı kazan |
| Baca gazı sıcaklığı | 160°C | Ekonomizersiz, pellet |
| Baca gazı O₂ | %7 | Hareketli ızgara, tipik |
| Kül oranı — pellet | %0.7 | EN-Plus A1 |
| Kül oranı — yonga | %1.5 | Kabuk dahil |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |
| φ (ekserji/enerji) — pellet | 1.14 | Kotas (1985) referansı |
| Elektrik tüketimi (fan, besleme) | Termal kapasitenin %2-4'ü | Yardımcı ekipman |

## Performans Tablosu (Yakıt Tipine Göre)

| Yakıt Tipi | Enerji Verimi (%, LHV) | Ekserji Verimi (%) | Baca Gazı T (°C) | Tipik λ | Yatırım Maliyeti (EUR/kW) |
|------------|------------------------|---------------------|-------------------|---------|--------------------------|
| Odun peleti | 85-92 | 30-40 | 130-170 | 1.3-1.5 | 150-350 |
| Odun yongası (kuru, %25 nem) | 80-87 | 27-35 | 150-200 | 1.3-1.5 | 200-450 |
| Odun yongası (yaş, %45 nem) | 72-80 | 22-30 | 160-220 | 1.4-1.6 | 200-450 |
| Saman | 78-85 | 25-33 | 150-200 | 1.4-1.6 | 250-500 |
| Pirina | 80-88 | 28-36 | 140-190 | 1.3-1.5 | 200-450 |
| Fındık kabuğu | 82-88 | 28-36 | 140-190 | 1.3-1.5 | 200-400 |

### Ekserji Verimi Hesabı

```
ψ_kazan = Ex_çıkış / Ex_giriş

Ex_giriş = m_yakıt × ex_ch_yakıt
Ex_çıkış = m_buhar × (ex_buhar - ex_besleme)

Burada:
  ψ_kazan     : Kazan ekserji verimi (0-1 arası)
  Ex_giriş    : Yakıt ekserjisi (kW)
  Ex_çıkış    : Akışkana (buhar/su) aktarılan ekserji (kW)
  m_yakıt     : Yakıt debisi (kg/s)
  ex_ch_yakıt : Yakıtın kimyasal ekserjisi (kJ/kg)
  m_buhar     : Buhar/su debisi (kg/s)
  ex_buhar    : Buhar/suyun spesifik ekserjisi (kJ/kg)
  ex_besleme  : Besleme suyunun spesifik ekserjisi (kJ/kg)
```

Ekserji yıkımının ana kaynakları:
- Yanma tersinmezliği: Toplam ekserji yıkımının %60-70'i (alev sıcaklığı ile akışkan sıcaklığı arasındaki fark)
- Isı transferi tersinmezliği: %15-25 (büyük sıcaklık farkı üzerinden ısı geçişi)
- Baca gazı ekserjisi: %5-15 (çevreye atılan ekserji)
- Kül ile kaybedilen ekserji: %1-3

## Dikkat Edilecekler

1. **Yakıt nemi kontrolü**: Nem içeriği %50'nin üzerinde olan biyokütle ekonomik olarak yakılamaz. Her %10 nem artışı kazan verimini yaklaşık %1.2 düşürür. Depolamada kapalı alan veya üstü kapalı silo tercih edilmeli
2. **Cüruflaşma riski (slagging/fouling)**: Saman ve tarımsal atıklarda potasyum ve silisyum içeriği yüksektir; kül eritme sıcaklığı düşüktür. Yanma odası sıcaklığı izlenmeli, gerektiğinde katkı maddeleri (kireç, kaolin) kullanılmalı
3. **Geri tutuşma önleme (backfire protection)**: Helezon besleyici ve silo arasında döner vana, düşme bölgesi veya sprinkler sistemi bulunmalı. Yangın riski en kritik güvenlik konusudur
4. **Kül temizleme periyodu**: Otomatik kül çıkarma sistemi olmayan kazanlarda düzenli kül temizliği yapılmazsa ısı transfer yüzeyleri kirlenip verim düşer. Saman ve pirina gibi yüksek küllü yakıtlarda sık temizlik gerekir
5. **Baca gazı sıcaklığı**: Biyokütle kazanlarında asit çiğ noktası riski düşüktür (düşük kükürt); ancak nem yoğuşması riski vardır. Baca gazı sıcaklığı 120°C altına düşürülmemelidir (ekonomizersiz durumda)
6. **Yakıt kalite tutarlılığı**: Farklı partiler arasında nem, boyut ve kalorifik değer farklılıkları performansı önemli ölçüde etkiler. Mümkünse EN 14961 (EN ISO 17225) sertifikalı yakıt kullanılmalı
7. **Yardımcı ekipman enerji tüketimi**: Besleme helezonları, fanlar, kül çıkarma sistemleri toplam termal kapasitenin %2-4'ü kadar elektrik tüketir. Bu enerji, toplam sistem ekserji analizine dahil edilmelidir

## İlgili Dosyalar
- Kazan yakıtları ve özellikleri: `equipment/boiler_fuels.md`
- Ateş borulu buhar kazanları: `equipment/boiler_steam_firetube.md`
- Su borulu buhar kazanları: `equipment/boiler_steam_watertube.md`
- Sıcak su kazanları: `equipment/boiler_hotwater.md`
- Kazan ekserji hesaplamaları: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Baca gazı ısı geri kazanımı: `solutions/boiler_flue_gas_recovery.md`
- Brülör ayarı ve hava/yakıt oranı: `solutions/boiler_combustion_optimization.md`

## Referanslar
- Ptasinski, K.J. (2016). *Efficiency of Biomass Energy: An Exergy Approach to Biofuels, Power, and Biorefineries*, Wiley.
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths. (Reprinted by Krieger, 1995.)
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- van Loo, S., Koppejan, J. (2008). *The Handbook of Biomass Combustion and Co-firing*, Earthscan/Routledge.
- Nussbaumer, T. (2003). *Combustion and Co-combustion of Biomass: Fundamentals, Technologies, and Primary Measures for Emission Reduction*, Energy & Fuels, 17(6).
- EN ISO 17225 (2021). *Solid Biofuels — Fuel Specifications and Classes*, CEN.
- EU Medium Combustion Plant Directive (MCPD) 2015/2193. *Emission Limits for 1-50 MW Combustion Plants*.
- ASME PTC 4 (2013). *Fired Steam Generators — Performance Test Codes*, ASME.
- IPCC (2006). *Guidelines for National Greenhouse Gas Inventories*, Volume 2: Energy.
