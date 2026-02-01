---
title: "Çözüm: Termal Depolama — Thermal Energy Storage"
category: solutions
equipment_type: chiller
keywords: [termal depolama, buz, chiller, pik]
related_files: [chiller/solutions/sequencing.md, chiller/benchmarks.md, factory/economic_analysis.md]
use_when: ["Termal depolama önerilirken", "Pik yük yönetimi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Termal Depolama — Thermal Energy Storage

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Pik soğutma talebi yüksek elektrik talep ücretlerine (demand charge) ve büyük chiller boyutlandırmasına neden olur. Soğutma talebi gün içinde büyük dalgalanmalar gösterir; pik saatlerde elektrik birim fiyatı %30-100 daha yüksektir. Ayrıca chiller'lar pik kapasite için boyutlandırılır ancak yılın büyük bölümünde kısmi yükte çalışır.

**Çözüm:** Gece (off-peak) saatlerinde soğutma enerjisini depolayarak pik saatlerde kullanmak. Buz depolama, soğuk su depolama (stratifiye tank) veya faz değişim malzemeleri (PCM) ile termal enerji depolama.

**Tipik Tasarruf:** %10-30 (maliyet tasarrufu; ayrıca talep azaltma)
**Tipik ROI:** 3-7 yıl

## Çalışma Prensibi

Termal enerji depolama (TES — Thermal Energy Storage), soğutma enerjisinin ucuz elektrik saatlerinde üretilip depolanması ve pahalı pik saatlerde kullanılması prensibine dayanır:

- **Şarj modu (gece):** Chiller düşük tarifeli saatlerde çalışarak depolama ortamını (buz, soğuk su, PCM) soğutur/dondurur
- **Deşarj modu (gündüz pik):** Depolanan soğutma enerjisi, pik saatlerde bina veya proses soğutma talebini karşılar; chiller kapasitesi azaltılır veya tamamen kapatılır
- **Eşzamanlı mod:** Chiller kısmen çalışır, depolama kalan yükü karşılar

### Termal Depolama Türleri Karşılaştırması

| Parametre | Buz Depolama | Soğuk Su Depolama | PCM (Faz Değişim Malzemesi) |
|-----------|-------------|-------------------|----------------------------|
| Depolama sıcaklığı | 0°C (buz/su faz değişimi) | 4-6°C (soğuk su) | Malzemeye göre (5-15°C) |
| Enerji yoğunluğu (kWh/m³) | 50-70 | 7-10 | 30-50 |
| Depolama hacmi (m³/MWh) | 14-20 | 100-140 | 20-33 |
| Chiller COP etkisi | Düşük (buz üretimi için -5 ile -7°C) | Normal (standart CHW) | Normal veya hafif düşük |
| Glikol gereksinimi | Evet (%25-30 etilen glikol) | Hayır | Genellikle hayır |
| COP cezası | %20-40 (düşük evaporatör sıcaklığı) | Yok | %5-10 |
| Sistem karmaşıklığı | Yüksek | Düşük-orta | Orta |
| Maliyet (€/kWh depolama) | 100-200 | 50-150 | 150-300 |

## Buz Depolama Sistemleri

### İç Eritme (Internal Melt)

- **Prensip:** Serpantin boruları içinden glikollü su dolaşır; şarj sırasında buz oluşur, deşarj sırasında buz erir
- **Glikol sistemi:** Chiller -5 ile -7°C'de glikollü su üretir; glikol serpantinlerden geçerek buz oluşturur
- **Deşarj:** Aynı glikol sirkülasyonu ile buz eritilir, soğutulmuş glikol sisteme gönderilir
- **Avantaj:** Kompakt, basit piping, düşük debi
- **Dezavantaj:** Glikol COP cezası, glikol ısı transfer kaybı (%5-15)

### Dış Eritme (External Melt)

- **Prensip:** Şarj sırasında serpantinlerde buz oluşur; deşarj sırasında tankın su tarafından buz eritilir
- **Deşarj:** Tank içindeki su doğrudan buz yüzeyinden soğur ve sisteme pompalanır (glikol gerektirmez)
- **Avantaj:** Daha yüksek deşarj hızı, glikol gerektirmez (deşarj tarafında)
- **Dezavantaj:** Daha büyük hacim, buzun topaklanma riski

### Buz Topları (Ice Balls / Capsules)

- **Prensip:** Küresel kapsüller (polietilen) içinde su dondurulur; glikollü su kapsüller arasından geçerek ısı alışverişi yapar
- **Avantaj:** Mevcut sisteme entegrasyon kolaylığı, modüler kapasite artışı
- **Dezavantaj:** Daha yüksek hacim gereksinimi, kapsül ömrü

## Soğuk Su Depolama (Stratifiye Tank)

Stratifiye (katmanlı) soğuk su tankı, sıcaklık farkından kaynaklanan yoğunluk farkını kullanarak soğuk ve sıcak su katmanlarını ayırır:

- **Prensip:** Soğuk su (4-6°C) tankın altına, sıcak su (12-14°C) tankın üstüne yerleşir; termoklin (sıcaklık geçiş katmanı) bu iki bölgeyi ayırır
- **Termoklin kalınlığı:** İyi tasarlanmış tankta 30-60 cm; daha ince termoklin = daha yüksek verimlilik
- **Tank boyutlandırma:** 1 MWh depolama için yaklaşık 100-140 m³ tank hacmi (ΔT=7°C için)
- **Verimlilik:** %90-95 (termal kayıplar düşük)
- **Avantaj:** Basit teknoloji, COP cezası yok, yangın suyu rezervi olarak çift kullanım
- **Dezavantaj:** Büyük hacim gereksinimi, yapısal yük (beton veya çelik tank)

```
V_tank = Q_depolama / (ρ × Cp × ΔT × η_depolama)

Burada:
  V_tank         = Tank hacmi [m³]
  Q_depolama     = Depolama kapasitesi [kWh]
  ρ              = Suyun yoğunluğu ≈ 1000 [kg/m³]
  Cp             = Suyun özgül ısısı ≈ 4.186 [kJ/kg·°C] = 1.163 [Wh/kg·°C]
  ΔT             = Soğuk-sıcak sıcaklık farkı [°C]
  η_depolama     = Depolama verimi (tipik 0.90-0.95) [-]
```

## Faz Değişim Malzemeleri (PCM)

PCM, belirli bir sıcaklıkta katıdan sıvıya veya sıvıdan katıya faz değiştirerek büyük miktarda latent ısı depolar/salar:

| PCM Tipi | Faz Değişim Sıcaklığı | Latent Isı (kJ/kg) | Kullanım Alanı |
|----------|----------------------|--------------------|-----------------|
| Su/Buz | 0°C | 334 | Buz depolama |
| Parafin bazlı | 5-15°C | 150-200 | Bina soğutma |
| Tuz hidrat | 5-13°C | 150-250 | Bina soğutma |
| Ötektik tuz | 8-12°C | 120-180 | Soğutma/iklimlendirme |

## Tam Depolama vs Kısmi Depolama Stratejileri

### Tam Depolama (Full Storage)

- Tüm pik soğutma yükü depolamadan karşılanır; chiller pik saatlerde çalışmaz
- **Avantaj:** Maksimum talep azaltma, en yüksek tarife tasarrufu
- **Dezavantaj:** Büyük depolama hacmi, yüksek yatırım

### Kısmi Depolama (Partial Storage)

- Pik yükün bir bölümü depolamadan, kalanı chiller'dan karşılanır
- **Load-Leveling (Yük Dengeleme):** Chiller gece-gündüz eşit kapasitede çalışır
- **Demand-Limiting:** Chiller belirli bir güç limitinin altında tutulur
- **Avantaj:** Daha küçük depolama, daha düşük yatırım, daha kısa ROI
- **Dezavantaj:** Kısmi talep azaltma

| Strateji | Depolama Boyutu | Chiller Boyutu | Talep Azaltma | Yatırım |
|----------|----------------|----------------|---------------|---------|
| Tam depolama | %100 pik yük | Küçük (gece üretimi) | %80-100 | Çok yüksek |
| Kısmi — yük dengeleme | %40-60 pik yük | Orta | %40-60 | Orta |
| Kısmi — talep limitleme | %30-50 pik yük | Mevcut | %30-50 | Düşük-orta |

## Pik Talep Azaltma ve Tarife Optimizasyonu

### Elektrik Tarifesi Etkileri

| Tarife Bileşeni | Açıklama | Termal Depolama Etkisi |
|-----------------|----------|------------------------|
| Talep ücreti (€/kW/ay) | Aylık pik güç tüketimine göre | %30-100 azaltma |
| Puant enerji fiyatı (€/kWh) | Yüksek tarife saatleri (09:00-22:00) | Tüketimi off-peak'e kaydırma |
| Gece enerji fiyatı (€/kWh) | Düşük tarife saatleri (22:00-06:00) | Üretimi gece saatlerine kaydırma |
| Reaktif güç cezası | Düşük güç faktörü cezası | Değişmez |

### Tarife Arbitrajı Hesabı

```
Yıllık_tarife_tasarrufu = Talep_tasarrufu + Enerji_arbitrajı

Talep_tasarrufu = Talep_azaltma_kW × Talep_ücreti_EUR_kW_ay × 12

Enerji_arbitrajı = Q_kaydırılan_kWh × (Puant_fiyat - Gece_fiyat) - Q_kaydırılan_kWh × (1/COP_gece - 1/COP_gündüz) × Gece_fiyat

Burada:
  Talep_azaltma_kW  = Pik güç azaltması [kW]
  Talep_ücreti      = Aylık talep ücreti [€/kW/ay]
  Q_kaydırılan_kWh  = Pik saatlerden gece saatlerine kaydırılan enerji [kWh/yıl]
  Puant_fiyat       = Puant saati elektrik fiyatı [€/kWh]
  Gece_fiyat        = Gece saati elektrik fiyatı [€/kWh]
  COP_gece          = Gece üretim COP'u (buz: daha düşük, CHW: aynı) [-]
  COP_gündüz        = Gündüz üretim COP'u [-]
```

## Chiller Küçültme Potansiyeli

Termal depolama ile yeni tesis projelerinde veya chiller değişimlerinde daha küçük kapasiteli chiller seçilebilir:

| Senaryo | Chiller Kapasitesi | Depolama | Toplam Pik Karşılama |
|---------|-------------------|----------|---------------------|
| Geleneksel (depolamasız) | 1,000 kW | — | 1,000 kW |
| Kısmi depolama | 600 kW | 400 kWh | 1,000 kW |
| Tam depolama | 350 kW | 1,000 kWh | 1,000 kW |

**Chiller maliyet tasarrufu:** Kapasite azaltma × chiller birim maliyeti (tipik €150-300/kW)

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı

- Elektrik tarifesinde yüksek talep ücreti varsa (>€10/kW/ay)
- Puant-gece tarife farkı >%30 ise
- Pik soğutma talebi ortalama talebin 2 katından fazlaysa
- Chiller kapasite artışı gerekiyorsa (depolama ile kaçınılabilir)
- Acil durum soğutma yedekliliği isteniyorsa
- Yeni bina/tesis projelerinde chiller boyutlandırma optimizasyonu hedefleniyorsa
- Enerji şebekesi kısıtları nedeniyle pik güç sınırlaması varsa

### Ne Zaman Uygulanmamalı

- Elektrik tarifesinde talep ücreti düşükse veya flat tarifeyse
- Soğutma yükü profili gece-gündüz dengeliyse (düz profil)
- Yeterli alan yoksa (özellikle CHW tankı için)
- Yıllık soğutma sezonu çok kısaysa (<3 ay)
- Chiller kapasitesi yeterliyse ve tarife avantajı sınırlıysa

## Yatırım Maliyeti

| Depolama Tipi | Birim Maliyet (€/kWh) | 500 kWh Sistem | 2,000 kWh Sistem | Açıklama |
|---------------|----------------------|----------------|------------------|----------|
| Buz depolama (iç eritme) | 100-200 | €50,000-100,000 | €200,000-400,000 | Tank + serpantin + glikol sistemi |
| Buz depolama (dış eritme) | 120-220 | €60,000-110,000 | €240,000-440,000 | Tank + serpantin + su sistemi |
| Buz topları | 130-250 | €65,000-125,000 | €260,000-500,000 | Kapsüller + tank + glikol |
| Soğuk su tankı (stratifiye) | 50-150 | €25,000-75,000 | €100,000-300,000 | Beton/çelik tank + difüzörler |
| PCM sistemi | 150-300 | €75,000-150,000 | €300,000-600,000 | PCM kapsüller + tank + kontrol |

**Ek maliyetler:** Pompa ve piping modifikasyonu (€10,000-50,000), kontrol sistemi (€5,000-20,000), yapısal temel (CHW tankı için €10,000-50,000)

## ROI Hesabı

### Formül

```
Yıllık_tasarruf = Talep_tasarrufu + Enerji_arbitrajı - Ek_enerji_maliyeti

Talep_tasarrufu = Talep_azaltma_kW × Talep_ücreti × 12 [€/yıl]
Enerji_arbitrajı = Kaydırılan_enerji × (Puant_fiyat - Gece_fiyat) [€/yıl]
Ek_enerji_maliyeti = Kaydırılan_enerji × (1/COP_depolama - 1/COP_normal) × Gece_fiyat [€/yıl]

Geri_ödeme_yıl = Toplam_yatırım / Yıllık_tasarruf
```

Burada:
- `Talep_azaltma_kW`: Pik elektrik güç azaltması [kW]
- `Talep_ücreti`: Aylık talep ücreti [€/kW/ay]
- `Kaydırılan_enerji`: Pik saatlerden gece saatlerine kaydırılan soğutma enerjisi [kWh/yıl]
- `COP_depolama`: Depolama modu COP'u (buz: 3.0-4.0, CHW: 5.0-6.0) [-]
- `COP_normal`: Normal çalışma COP'u (5.0-6.5) [-]

### Örnek Hesap — Buz Depolama (Kısmi Depolama)

- Tesis pik soğutma yükü: 1,000 kW, 8 saat/gün pik süresi
- Depolama kapasitesi: 2,000 kWh (250 kW × 8 saat pik karşılama)
- Talep azaltma: 250 kW
- Soğutma sezonu: 150 gün/yıl
- Talep ücreti: €15/kW/ay
- Puant elektrik fiyatı: €0.15/kWh
- Gece elektrik fiyatı: €0.08/kWh
- COP (buz üretimi, gece): 3.5
- COP (normal, gündüz): 5.5

```
Talep_tasarrufu = 250 × 15 × 6 (soğutma sezonu ayları) = €22,500/yıl

Kaydırılan_enerji = 2,000 × 150 = 300,000 kWh/yıl
Enerji_arbitrajı = 300,000/5.5 × 0.15 - 300,000/3.5 × 0.08
                 = 54,545 × 0.15 - 85,714 × 0.08
                 = 8,182 - 6,857 = €1,325/yıl

Toplam_yıllık_tasarruf = 22,500 + 1,325 = €23,825/yıl
```

- Yatırım: Buz depolama €300,000 + Piping €30,000 + Kontrol €15,000 = **€345,000**
- **Geri ödeme: 345,000 / 23,825 = 14.5 yıl** (yalnızca talep ücreti ile)

**Not:** Bu örnekte talep ücreti düşük varsayılmıştır. Talep ücreti €30/kW/ay olan bölgelerde geri ödeme süresi 5-7 yıla düşer. Ayrıca chiller küçültme potansiyeli (yeni tesis) ROI'yi önemli ölçüde iyileştirir.

## Uygulama Adımları

1. **Yük profili analizi:** Saatlik soğutma yükü profili çıkar, pik/off-peak dağılımını belirle
2. **Tarife analizi:** Elektrik tarifesini incele; talep ücreti, puant/gece fiyat farkını hesapla
3. **Depolama stratejisi seçimi:** Tam vs kısmi depolama, yük dengeleme vs talep limitleme kararı ver
4. **Teknoloji seçimi:** Buz vs CHW vs PCM; mevcut alana, chiller tipine ve bütçeye göre karar ver
5. **Boyutlandırma:** Depolama kapasitesi, chiller kapasitesi ve pompa boyutlandırmasını yap
6. **Detay mühendislik:** Piping, kontrol stratejisi, glikol sistemi (buz için), tank tasarımı
7. **İhale ve tedarik:** En az 3 tedarikçiden teklif al, referans projeleri incele
8. **Kurulum:** Tank/depolama sistemi, piping bağlantıları, pompa ve vana montajı
9. **Kontrol sistemi programlama:** Şarj/deşarj geçiş mantığı, tarife bazlı optimizasyon, güvenlik interlokları
10. **Devreye alma:** Şarj ve deşarj testleri, kapasite doğrulama, kontrol senaryoları test etme
11. **Performans izleme:** Depolama verimi, talep azaltma ve tasarruf verilerini izle ve raporla

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Alan gereksinimi | CHW tankı büyük alan kaplar; buz tankı da önemli yer gerektirir | Erken aşamada alan planlama, yeraltı veya çatı üstü değerlendirme |
| Kontrol karmaşıklığı | Şarj/deşarj geçişleri, chiller koordinasyonu, tarife optimizasyonu | Deneyimli kontrol programcısı, kapsamlı test, otomasyon |
| Glikol verimlilik cezası (buz) | %25-30 glikol karışımı pompa gücünü %15-20, ısı transferini %10-15 düşürür | Glikol konsantrasyonunu minimumda tut, ısı eşanjörü boyutlandırmasında dikkat |
| Buz birikimi dengesizliği | Eşit olmayan buz oluşumu depolama kapasitesini azaltır | Glikol dağılım manifoldunu dengele, termal görüntüleme ile izle |
| Termoklin bozulması (CHW) | Kötü difüzör tasarımı termoklini bozar, depolama verimi düşer | Düşük hızlı difüzörler (Froude sayısı <1), tankta türbülans önleme |
| Legionella riski (CHW) | Durağan sıcak su katmanında bakteri üremesi | Periyodik tank pastörizasyonu, su arıtma |
| Yapısal yük (CHW) | Dolu su tankı çok ağırdır (100 m³ = 100 ton) | Yapısal mühendislik hesabı, zemin taşıma kapasitesi doğrulama |
| Tarife değişikliği | Elektrik tarifesi yapısı değişirse ROI bozulabilir | Uzun vadeli tarife analizi, esnek kontrol stratejisi |

## İlgili Dosyalar

- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller bakım: `solutions/chiller_maintenance.md`
- Delta-T optimizasyonu: `solutions/chiller_delta_t.md`
- Isı geri kazanım: `solutions/chiller_heat_recovery.md`
- Soğutma yükü azaltma: `solutions/chiller_load_reduction.md`

## Referanslar

- ASHRAE Handbook — HVAC Applications, Chapter 51: "Thermal Storage"
- ASHRAE Design Guide for Cool Thermal Storage, 2nd Edition
- ASHRAE RP-1054, "Field Monitoring and Evaluation of Cool Storage Systems"
- IEA — ECES Annex 28, "Thermal Energy Storage for Cost-Effective Energy Management"
- EPRI, "Commercial Cool Storage Design Guide"
- Dorgan, C.E., Elleson, J.S., "Design Guide for Cool Thermal Storage," ASHRAE
- Trane, "Ice Storage Systems — Application Engineering Manual"
- CIBSE TM46, "Energy Benchmarks" — Thermal Storage Applications
- Dincer, I., Rosen, M.A., "Thermal Energy Storage: Systems and Applications," 2nd Edition
