---
title: "Çözüm: Isı Geri Kazanım — Chiller Heat Recovery"
category: solutions
equipment_type: chiller
keywords: [ısı geri kazanımı, chiller, atık ısı]
related_files: [chiller/formulas.md, chiller/benchmarks.md, factory/waste_heat_recovery.md]
use_when: ["Chiller ısı geri kazanımı önerilirken", "Kondenser atık ısısı değerlendirilirken"]
priority: high
last_updated: 2026-01-31
---
# Çözüm: Isı Geri Kazanım — Chiller Heat Recovery

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Chiller kondenser ısısı çevreye atılmaktadır. Bir chiller, ürettiği soğutma enerjisine ek olarak kompresör işini de kondenserde ısı olarak reddeder. Bu toplam ısı (Q_cond = Q_evap + W_comp) genellikle soğutma kulesi veya hava soğutmalı kondenser ile atmosfere verilir ve tamamen kaybolur. Özellikle eşzamanlı soğutma ve ısıtma gereksinimi olan tesislerde bu enerji kaybı çok yüksektir.

**Çözüm:** Kondenser ısısını kullanım sıcak suyu (DHW), mahal ısıtması veya proses amaçlı geri kazanmak. Desuperheater, tam ısı geri kazanım kondenseri veya çift borulu (double bundle) kondenser ile atık ısıyı faydalı ısıya dönüştürmek.

**Tipik Tasarruf:** %10-25 (ısıtma maliyetlerinden)
**Tipik ROI:** 2-5 yıl

## Çalışma Prensibi

Chiller buhar sıkıştırma çevriminde enerji dengesi:

```
Q_cond = Q_evap + W_comp

Burada:
  Q_cond  = Kondenser ısı atımı [kW]
  Q_evap  = Evaporatör soğutma kapasitesi [kW]
  W_comp  = Kompresör elektrik tüketimi [kW]
```

Tipik bir chiller'da (COP = 5.5):
- Q_evap = 1,000 kW soğutma üretilirken
- W_comp = 1,000 / 5.5 = 182 kW
- Q_cond = 1,000 + 182 = 1,182 kW ısı reddedilir

Bu ısının tamamı veya bir bölümü geri kazanılabilir. Geri kazanım yöntemine göre kullanılabilir sıcaklık seviyesi değişir:

### Kondenser Isı Sıcaklık Seviyeleri

| Isı Kaynağı | Sıcaklık Aralığı | Uygun Kullanım |
|-------------|-------------------|----------------|
| Desuperheater (kızgın gaz bölgesi) | 60-80°C | Kullanım sıcak suyu (DHW), ön ısıtma |
| Kondensasyon bölgesi | 35-45°C | Düşük sıcaklık ısıtma, havuz, yerden ısıtma |
| Subcooling bölgesi | 30-40°C | Ön ısıtma, düşük sıcaklık proses |
| Tam kondenser (ortalama) | 35-50°C | Genel ısıtma, DHW ön ısıtma |

## Isı Geri Kazanım Yöntemleri

### 1. Desuperheater (Kızgın Gaz Isı Eşanjörü)

Kompresör çıkışındaki kızgın (superheated) gazın kondensasyon sıcaklığına düşürülmesi sırasında açığa çıkan ısıyı geri kazanır:

- **Konum:** Kompresör çıkışı ile kondenser girişi arasına yerleştirilir
- **Geri kazanılabilir ısı:** Toplam Q_cond'un %15-25'i (superheat bölgesi)
- **Üretilen sıcak su sıcaklığı:** 55-65°C (DHW için yeterli)
- **Tip:** Kabuk-boru (shell & tube) veya plakalı ısı eşanjörü
- **Avantaj:** Düşük maliyet, mevcut sisteme kolay entegrasyon, chiller performansına minimal etki
- **Dezavantaj:** Sınırlı kapasite (toplam atık ısının küçük bölümü)

```
Q_desuperheater = ṁ_ref × (h_comp_çıkış - h_kond_giriş)

Burada:
  Q_desuperheater   = Desuperheater ısı geri kazanımı [kW]
  ṁ_ref             = Soğutucu akışkan kütle debisi [kg/s]
  h_comp_çıkış      = Kompresör çıkış entalpisi [kJ/kg]
  h_kond_giriş      = Kondenser giriş entalpisi (doymuş buhar) [kJ/kg]
```

### 2. Tam Isı Geri Kazanım Kondenseri (Full Heat Recovery Condenser)

Kondenserin tamamını veya büyük bölümünü ısı geri kazanım amaçlı kullanır:

- **Konum:** Standart kondenserin yerine veya yanına paralel olarak yerleştirilir
- **Geri kazanılabilir ısı:** Q_cond'un %80-100'ü
- **Üretilen sıcak su sıcaklığı:** 40-50°C (uygulamaya göre değişir)
- **Çalışma modu:** Isı talebi olduğunda su kondenserine, talep yoksa soğutma kulesine yönlendirilir
- **Avantaj:** Yüksek ısı geri kazanım kapasitesi, önemli yakıt tasarrufu
- **Dezavantaj:** Yüksek yatırım maliyeti, kontrol karmaşıklığı, ısı talebi yoksa soğutma kulesine geçiş gerekir

### 3. Eşzamanlı Isıtma ve Soğutma (Isı Pompası Modu)

Chiller aynı anda hem soğutma hem ısıtma yapar; kondenser ısısının tamamı ısıtma amaçlı kullanılır:

- **Uygulama:** Eşzamanlı soğutma ve ısıtma gereksinimi olan tesisler (otel, hastane, gıda sanayi)
- **COP_ısıtma:** COP_soğutma + 1 (teorik); tipik 6.0-7.5
- **Fayda:** Isıtma kazan verimi %85-95 iken, ısı pompası COP 6-7 → %300-400 daha verimli
- **Sınırlama:** Soğutma ve ısıtma yüklerinin eşzamanlı ve dengelenmiş olması gerekir

### 4. Çift Borulu Kondenser (Double Bundle Condenser)

Kondenser içinde iki ayrı boru demeti bulunur: biri ısı geri kazanım, diğeri soğutma kulesi suyu için:

- **Çalışma:** Isı talebi olduğunda ısı geri kazanım demeti öncelikli çalışır; karşılanamayan ısı soğutma kulesi demetine yönlendirilir
- **Avantaj:** Tek kondenser gövdesi, otomatik yük paylaşımı, güvenilir geçiş
- **Dezavantaj:** Özel üretim, daha büyük kondenser, yüksek maliyet
- **Uygulama:** Büyük santrifüj chiller'larda (>500 kW)

## Isı Geri Kazanım Potansiyeli

### Soğutma Kapasitesine Göre Sıcak Su Üretim Potansiyeli

| Chiller Kapasitesi (kW soğutma) | COP | Kondenser Isısı (kW) | DHW Üretimi — Desuperheater (L/h @ 50°C) | DHW Üretimi — Tam HR (L/h @ 45°C) |
|---------------------------------|-----|----------------------|-------------------------------------------|------------------------------------|
| 200 | 5.0 | 240 | 520 | 3,440 |
| 500 | 5.5 | 591 | 1,280 | 8,470 |
| 1,000 | 5.5 | 1,182 | 2,560 | 16,940 |
| 2,000 | 6.0 | 2,333 | 5,050 | 33,430 |
| 5,000 | 6.0 | 5,833 | 12,630 | 83,570 |

**Varsayımlar:** Desuperheater: Q_cond'un %20'si, ΔT=33°C (15→48°C); Tam HR: Q_cond'un %90'ı, ΔT=15°C (30→45°C)

```
DHW_debisi = Q_gerikazanım / (Cp × ΔT_su)

Burada:
  DHW_debisi        = Sıcak su debisi [L/h]
  Q_gerikazanım     = Geri kazanılan ısı [kW]
  Cp                = Suyun özgül ısısı ≈ 4.186 [kJ/kg·°C]
  ΔT_su             = Su sıcaklık artışı [°C]
```

## Uygulama Senaryoları

### Senaryo 1: Otel — Desuperheater ile DHW

- Otel kapasitesi: 200 oda
- Günlük sıcak su ihtiyacı: ~15,000 L/gün @ 55°C
- Chiller kapasitesi: 500 kW, COP 5.5
- Desuperheater kapasitesi: ~118 kW (Q_cond'un %20'si)
- Günlük üretim: ~5,100 L/gün @ 55°C (chiller 10 saat çalışma)
- Karşılama oranı: ~%34 günlük DHW ihtiyacının
- Yıllık doğalgaz tasarrufu: ~210,000 kWh

### Senaryo 2: Hastane — Tam Isı Geri Kazanım

- Hastane: 300 yatak
- Eşzamanlı soğutma + ısıtma gereksinimi: 12 ay (laundry, sterilizasyon, DHW)
- Chiller kapasitesi: 1,000 kW, COP 5.5
- Tam HR kapasitesi: ~1,060 kW (Q_cond'un %90'ı)
- Yıllık doğalgaz tasarrufu: ~1,500,000 kWh
- Yıllık yakıt maliyet tasarrufu: ~€67,500 (€0.045/kWh doğalgaz)

### Senaryo 3: Gıda Sanayi — Eşzamanlı Isıtma/Soğutma

- Gıda işleme tesisi: sürekli proses soğutma + sıcak su ihtiyacı
- Proses soğutma: 2,000 kW (yıl boyu)
- Sıcak su ihtiyacı: 1,500 kW (temizlik, pastörizasyon)
- Kondenser ısısı: 2,333 kW → %65'i kullanılabilir (1,517 kW)
- Yıllık doğalgaz tasarrufu: ~8,000,000 kWh
- Yıllık yakıt maliyet tasarrufu: ~€360,000

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı

- Eşzamanlı soğutma ve ısıtma gereksinimi varsa (otel, hastane, gıda sanayi, yüzme havuzu)
- DHW tüketimi yüksekse (>5,000 L/gün)
- Chiller yıl boyu veya uzun süreli çalışıyorsa (>4,000 saat/yıl)
- Düşük sıcaklık ısıtma sistemi mevcutsa (yerden ısıtma, fan-coil: 40-45°C)
- Doğalgaz veya yakıt maliyeti yüksekse
- Mevcut ısıtma kazanı verimi düşükse veya kapasite artışı gerekiyorsa
- Karbon emisyonu azaltma hedefi varsa

### Ne Zaman Uygulanmamalı

- Eşzamanlı soğutma ve ısıtma gereksinimi yoksa veya çok sınırlıysa
- Isı talebi sadece kış aylarında, soğutma sadece yaz aylarındaysa (örtüşme yok)
- Chiller çalışma süresi düşükse (<2,000 saat/yıl)
- Yüksek sıcaklık ısıtma gereksinimi varsa (>60°C, radyatör sistemi) — desuperheater sınırlı kalır
- Mevcut ısıtma sistemi yüksek verimli kondansasyon kazanı ise ve yakıt ucuzsa

## Yatırım Maliyeti

| Ekipman | Maliyet (€) | Açıklama |
|---------|-------------|----------|
| Desuperheater (200-500 kW chiller) | 5,000-12,000 | Plakalı veya kabuk-boru HEX, piping |
| Desuperheater (500-2,000 kW chiller) | 10,000-20,000 | Büyük kapasite, montaj dahil |
| Tam HR kondenser (200-500 kW chiller) | 20,000-40,000 | İkinci kondenser + vana + kontrol |
| Tam HR kondenser (500-2,000 kW chiller) | 40,000-80,000 | Büyük kapasite, piping modifikasyonu |
| Çift borulu kondenser (yeni chiller) | Chiller fiyatına ek %10-20 | Fabrikada entegre |
| DHW depolama tankı (2,000-5,000 L) | 3,000-10,000 | Paslanmaz çelik, izolasyonlu |
| DHW depolama tankı (5,000-20,000 L) | 8,000-25,000 | Büyük kapasite |
| Kontrol sistemi ve enstrümantasyon | 3,000-10,000 | Vana, sensör, BMS entegrasyonu |
| Piping modifikasyonu | 5,000-20,000 | Boru, izolasyon, pompa |

## ROI Hesabı

### Formül

```
Q_gerikazanım_yıllık = Q_HR × Çalışma_saati × Kullanım_oranı [kWh/yıl]
Yakıt_tasarrufu = Q_gerikazanım_yıllık / η_kazan [kWh/yıl]
Yıllık_tasarruf_EUR = Yakıt_tasarrufu × Yakıt_fiyatı [€/yıl]
Ek_elektrik_maliyeti = ΔW_pompa × Çalışma_saati × Elektrik_fiyatı [€/yıl]
Net_yıllık_tasarruf = Yıllık_tasarruf_EUR - Ek_elektrik_maliyeti [€/yıl]
Geri_ödeme_yıl = Toplam_yatırım / Net_yıllık_tasarruf
```

Burada:
- `Q_HR`: Isı geri kazanım kapasitesi [kW]
- `Çalışma_saati`: Chiller yıllık çalışma süresi [saat/yıl]
- `Kullanım_oranı`: Geri kazanılan ısının fiili kullanım oranı (0-1) [-]
- `η_kazan`: Mevcut ısıtma kazanı verimi [%]
- `Yakıt_fiyatı`: Birim yakıt fiyatı [€/kWh]
- `ΔW_pompa`: Ek pompa gücü [kW]
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap — Desuperheater (Otel)

- 500 kW chiller, COP 5.5
- Kondenser ısısı: 591 kW
- Desuperheater kapasitesi: 118 kW (Q_cond'un %20'si)
- Chiller çalışma: 4,500 saat/yıl
- DHW kullanım oranı: %70 (gece düşük talep)
- Mevcut kazan verimi: %90 (doğalgaz)
- Doğalgaz fiyatı: €0.045/kWh
- Ek pompa gücü: 1.5 kW
- Elektrik fiyatı: €0.12/kWh

```
Q_gerikazanım_yıllık = 118 × 4,500 × 0.70 = 371,700 kWh/yıl
Yakıt_tasarrufu = 371,700 / 0.90 = 413,000 kWh/yıl
Yıllık_tasarruf_EUR = 413,000 × 0.045 = €18,585/yıl
Ek_elektrik_maliyeti = 1.5 × 4,500 × 0.12 = €810/yıl
Net_yıllık_tasarruf = 18,585 - 810 = €17,775/yıl
```

- Yatırım: Desuperheater €10,000 + DHW tank €5,000 + Piping €5,000 + Kontrol €3,000 = **€23,000**
- **Geri ödeme: 23,000 / 17,775 = 1.29 yıl**

**Not:** Desuperheater uygulaması düşük yatırım maliyeti ve kısa geri ödeme süresi ile en cazip ısı geri kazanım yöntemidir.

## Uygulama Adımları

1. **Isı talebi analizi:** Eşzamanlı soğutma ve ısıtma profilini belirle. DHW tüketimi, mahal ısıtma ve proses ısı gereksinimlerini saatlik bazda çıkar
2. **Chiller çalışma profili:** Chiller yıllık çalışma saatleri, yük profili ve COP değerlerini kaydet
3. **Eşleşme analizi:** Soğutma ve ısıtma yük profillerini karşılaştır; eşzamanlılık oranını belirle
4. **Isı geri kazanım yöntemi seçimi:** Desuperheater, tam HR, çift borulu veya ısı pompası modu kararı ver
5. **Boyutlandırma:** Isı eşanjörü, DHW tankı, pompa ve piping boyutlandırmasını yap
6. **Detay mühendislik:** Piping güzergahı, vana yerleşimi, kontrol stratejisi (HR ↔ soğutma kulesi geçiş mantığı)
7. **Tedarik:** Isı eşanjörü, DHW tankı, pompa, vana ve kontrol ekipmanlarını temin et
8. **Kurulum:** Desuperheater/HR kondenser montajı, piping bağlantıları, DHW tank entegrasyonu
9. **Kontrol sistemi:** HR aktif/pasif geçiş mantığı, DHW sıcaklık kontrolü, güvenlik interlokları
10. **Devreye alma:** Debi, sıcaklık ve basınç ölçümleri ile performans doğrulama
11. **Performans izleme:** Geri kazanılan ısı miktarını izle, yakıt tasarrufunu doğrula, mevsimsel optimizasyon yap

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yetersiz ısı talebi | Geri kazanılan ısıya yeterli talep yoksa kondenser basıncı yükselir | DHW tank kapasitesini yeterli tut, talep yoksa soğutma kulesine geçiş |
| Kirlenme (fouling) | DHW tarafında kireç ve korozyon birikimi ısı transferini düşürür | Su arıtma, periyodik temizlik, paslanmaz çelik HEX |
| Kontrol karmaşıklığı | HR-soğutma kulesi geçiş mantığı hatalı olursa chiller performansı düşer | Kapsamlı kontrol senaryosu testi, fail-safe tasarım (soğutma kulesi varsayılan) |
| Legionella riski | DHW depolama sıcaklığı <55°C ise bakteri üremesi riski | Depolama sıcaklığı min. 60°C, periyodik termal dezenfeksiyon (70°C) |
| Kondenser basıncı artışı | HR modu kondenser basıncını yükseltebilir, COP düşer | HR su sıcaklığını izle, üst limit aşılırsa soğutma kulesine geçiş |
| Glikol karışımı riski | Soğutucu akışkan-su eşanjöründe sızıntı DHW'yi kirletebilir | Çift duvarlı HEX, ara devre (intermediate loop), basınç izleme |
| Mevsimsel dengesizlik | Yaz'da soğutma fazla ısıtma az, kış'ta ters | Depolama tankı, yardımcı ısı kaynağı (kazan yedek) |
| Yatırım maliyeti (tam HR) | Tam HR kondenser yüksek yatırım gerektirir | Fizibilite çalışması, faz bazlı uygulama (önce desuperheater) |

## İlgili Dosyalar

- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller bakım: `solutions/chiller_maintenance.md`
- Delta-T optimizasyonu: `solutions/chiller_delta_t.md`
- Termal depolama: `solutions/chiller_thermal_storage.md`
- Kazan kondansat geri kazanımı: `solutions/boiler_condensate_return.md`

## Referanslar

- ASHRAE Handbook — HVAC Systems and Equipment, Chapter 2: "Decentralized Cooling and Heating"
- ASHRAE Handbook — HVAC Applications, Chapter 9: "Applied Heat Pump and Heat Recovery Systems"
- CIBSE Guide F, "Energy Efficiency in Buildings" — Heat Recovery from Cooling Systems
- Carrier Corporation, "Application Guide — Heat Recovery Chillers"
- Trane, "Heat Recovery in Chiller Systems — Application Engineering Manual"
- DOE/FEMP, "Federal Technology Alert: Heat Recovery from Chiller Systems"
- EUROVENT, "Heat Recovery from Refrigeration — Best Practice Guide"
- EN 14511, "Air conditioners, liquid chilling packages and heat pumps for space heating and cooling"
- IEA Heat Pump Centre, "Heat Pumps in Industrial Applications"
- Türkiye Enerji Verimliliği Derneği (ENVER), "Isı Pompası ve Isı Geri Kazanım Rehberi"
