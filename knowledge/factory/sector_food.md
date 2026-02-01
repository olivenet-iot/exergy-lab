---
title: "Gıda ve İçecek Sektörü Enerji Profili ve Optimizasyon (Food and Beverage Sector Energy Profile)"
category: factory
equipment_type: factory
keywords: [gıda, sektör, soğutma, enerji]
related_files: [factory/factory_benchmarks.md, factory/heat_integration.md, factory/cross_equipment.md]
use_when: ["Gıda fabrikası analiz edilirken", "Gıda sektörü benchmarkları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Gıda ve İçecek Sektörü Enerji Profili ve Optimizasyon (Food and Beverage Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Gıda ve içecek sektörü, Türkiye sanayisinin en büyük alt sektörlerinden biri olup toplam sanayi üretiminin %12-15'ini oluşturur. Sektör, hem ısıtma (pastörizasyon, sterilizasyon, pişirme) hem soğutma (depolama, dondurma) gerektiren ikili enerji profiline sahiptir. Toplam enerji tüketiminde termal enerji payı %55-70, elektrik payı %30-45 aralığındadır. Hijyen gereksinimleri enerji seçimlerini doğrudan etkiler ve sektörde soğuk zincir yönetimi kritik öneme sahiptir.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Toplam tesis sayısı: ~35,000 (kayıtlı gıda üretim tesisi)
- İstihdam: ~500,000 doğrudan çalışan
- Yıllık ihracat: ~22-25 milyar USD
- Enerji maliyetinin üretim maliyetindeki payı: %5-12
- Türkiye, dünya gıda üretiminde ilk 10 içinde yer almakta
- Başlıca üretim merkezleri: İstanbul, İzmir, Bursa, Mersin, Gaziantep

### 1.2 Alt Sektörler ve Enerji Yoğunlukları

| Alt Sektör | Enerji Yoğunluğu | Baskın Enerji Türü | Kritik Proses |
|---|---|---|---|
| Süt ürünleri (Dairy) | Orta-Yüksek | Termal + soğutma | Pastörizasyon, UHT, soğuk depo |
| Et işleme (Meat) | Orta | Soğutma ağırlıklı | Soğuk zincir, pişirme |
| Unlu mamul/Fırın (Bakery) | Yüksek | Termal ağırlıklı | Fırınlama, fermantasyon |
| İçecek (Beverage) | Orta | Termal + soğutma | Pastörizasyon, soğutma |
| Dondurulmuş gıda (Frozen) | Çok Yüksek | Soğutma ağırlıklı | -25 ile -40°C dondurma |
| Konserve | Yüksek | Termal ağırlıklı | Sterilizasyon, otoklav |
| Şekerleme/çikolata | Orta-Yüksek | Termal + soğutma | Pişirme, soğutma tüneli |
| Yağ üretimi | Yüksek | Termal ağırlıklı | Ekstraksiyon, rafinasyon |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Doğalgaz | 45-60 | Kazan, fırın, CHP |
| Elektrik | 35-45 | Soğutma, motorlar, basınçlı hava, otomasyon |
| Fuel oil / LPG | 0-5 | Yedek yakıt, portatif ısıtma |
| Biyogaz (kendi üretimi) | 0-5 | Bazı büyük tesislerde atık arıtmadan |

### 2.2 Proses Bazlı Enerji Dağılımı (Genel Gıda Tesisi)

| Proses | Termal Enerji [%] | Elektrik [%] | Toplam Pay [%] |
|---|---|---|---|
| Soğutma/dondurma (refrigeration) | 0 | 25-40 | 18-30 |
| Pastörizasyon/sterilizasyon | 20-30 | 2-4 | 15-25 |
| Pişirme/fırınlama | 15-25 | 1-3 | 12-18 |
| Buhar üretimi ve dağıtımı | 10-15 | 1-2 | 8-12 |
| CIP (temizlik) | 5-10 | 2-3 | 5-8 |
| Basınçlı hava | 0 | 5-10 | 4-7 |
| HVAC (üretim alanı klima) | 3-8 | 5-10 | 5-10 |
| Aydınlatma | 0 | 3-6 | 2-4 |
| Paketleme | 0 | 3-5 | 2-4 |

### 2.3 Alt Sektör Bazlı Enerji Profili

```
Süt fabrikası tipik enerji dağılımı:
  Soğutma kompresörleri: %30-35 (elektrik)
  Pastörizasyon/UHT:     %20-25 (buhar)
  CIP temizlik:          %8-12 (buhar + elektrik)
  HVAC:                  %8-10 (elektrik)
  Basınçlı hava:         %5-8 (elektrik)
  Diğer:                 %10-15

Fırın/unlu mamul tipik enerji dağılımı:
  Fırınlama:             %50-60 (doğalgaz/elektrik)
  Fermantasyon odası:    %8-12 (buhar, elektrik)
  Soğutma:               %8-15 (elektrik)
  Basınçlı hava:         %5-8 (elektrik)
  Diğer:                 %10-15
```

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 Orta Ölçekli Süt Fabrikası (Kapasite ~200 ton/gün)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Buhar kazanı (ateş borulu) | 4-8 ton/h | 2 | 25-35 | Doğalgaz |
| Soğutma kompresörü (amonyak/R-507) | 200-500 kW soğ. | 3-5 | 25-35 | Elektrik |
| Pastörizatör (PHE) | 10,000-30,000 L/h | 2-4 | 8-12 | Buhar |
| UHT sistemi | 5,000-15,000 L/h | 1-2 | 5-8 | Buhar |
| Soğuk depo evaporatörleri | 50-200 kW | 4-8 | 5-8 | Elektrik |
| CIP sistemi | 5,000-15,000 L | 2-3 | 5-8 | Buhar + Elektrik |
| Basınçlı hava kompresörü | 30-75 kW | 2-3 | 4-6 | Elektrik |
| Homojenizatör | 15-55 kW | 2-3 | 2-4 | Elektrik |
| Soğutma kulesi | 200-500 kW atık ısı | 2-3 | 1-3 | Elektrik |
| HVAC (üretim alanı) | 100-300 kW | 1-2 | 3-5 | Elektrik |

### 3.2 Ekipman Referansları

- Kazan sistemleri: bkz. `../boiler/equipment/systems_overview.md`
- Soğutma sistemleri: bkz. `../chiller/equipment/systems_overview.md`
- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik Gıda Tesisi)

```
DOĞALGAZ EXERGY (%55)  ─────────────────────────────┐
                                                      │
ELEKTRİK EXERGY (%45) ─────────────────────────────┐│
                                                    ││
                   ┌────────────────────────────────┴┤
                   │     TOPLAM EXERGY GİRİŞİ        │
                   │        (100%)                    │
                   ├──────────────────────────────────┘
                   │
   ┌───────────────┤ Yanma tersinmezliği (%15-22) ──────→ YIKIM
   │               │
   │  ┌────────────┤ Isı transferi tersinmezliği (%10-16)→ YIKIM
   │  │            │
   │  │  ┌─────────┤ Soğutma sistemi tersinmezliği (%8-14)→ YIKIM
   │  │  │         │
   │  │  │  ┌──────┤ Kondenser atık ısısı (%6-10) ─────→ ATIK
   │  │  │  │      │
   │  │  │  │  ┌───┤ Baca gazı exergisi (%4-8) ────────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   │ Motor/pompa tersinmezliği (%3-6) ──→ YIKIM
   │  │  │  │  │   │ CIP atık suyu (%2-4) ─────────────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   ├────────────────────────────────────┐
   │  │  │  │  │   │  ÜRÜN EXERGY (%15-25)              │
   │  │  │  │  │   │  (pastörize/steril ürün + soğutma) │
   │  │  │  │  │   └────────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma tersinmezliği | 15-22 | Kazan ve fırın yanma odalarında |
| Isı transferi tersinmezliği | 10-16 | Pastörizatör, eşanjörler, kazan |
| Soğutma sistemi tersinmezliği | 8-14 | Kompresör, kısma vanası, evaporatör |
| Kondenser atık ısısı | 6-10 | Soğutma sistemi kondenseri |
| Baca gazı kaybı | 4-8 | Kazan ve fırın baca gazı |
| Motor/pompa tersinmezliği | 3-6 | Tüm elektrik motorları |
| CIP atık suyu | 2-4 | 70-85°C sıcak yıkama suyu |
| Buhar dağıtım kaybı | 2-4 | İzolasyon, kapan arızaları |
| Basınçlı hava kayıpları | 1-3 | Kaçak ve basınç düşüşleri |

### 4.3 Tipik Exergy Verimi

```
η_ex,gıda = Ex_ürün / Ex_giriş × 100

Tipik aralık: %15-25
Sektör ortalaması: %20
En iyi uygulama: %32-35

Düşük exergy verimi nedenleri:
1. Düşük sıcaklık prosesleri (60-135°C) yüksek kaliteli yakıtla
   karşılanmakta → büyük sıcaklık farkı = yüksek tersinmezlik
2. Soğutma proseslerinde Carnot sınırı düşük (T_soğuk/T₀ yakın) →
   düşük exergy içeriği, yüksek güç tüketimi
3. Hijyen gereksinimleri nedeniyle ısı geri kazanımı kısıtlı
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Alt Sektör Bazında

| Alt Sektör | SEC Termal | SEC Elektrik | SEC Toplam | Birim |
|---|---|---|---|---|
| Süt işleme | 200-450 | 80-180 | 300-600 | kWh/ton süt |
| Peynir üretimi | 400-800 | 150-300 | 600-1,100 | kWh/ton süt |
| Bira üretimi | 100-200 | 60-120 | 180-320 | kWh/hL bira |
| Meşrubat | 20-50 | 40-80 | 60-130 | kWh/hL |
| Unlu mamul (ekmek) | 200-400 | 80-150 | 300-550 | kWh/ton ekmek |
| Et işleme | 200-500 | 150-350 | 400-800 | kWh/ton et |
| Dondurulmuş gıda | 100-250 | 300-600 | 450-850 | kWh/ton ürün |
| Konserve | 300-600 | 50-150 | 400-750 | kWh/ton ürün |
| Şeker (pancar) | 250-400 | 30-60 | 300-450 | kWh/ton pancar |
| Bitkisel yağ | 400-800 | 100-250 | 550-1,050 | kWh/ton yağ |

### 5.2 Performans Sınıflandırması — Genel Gıda Tesisi

| Performans | SEC [kWh/ton] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | <300 | >30 | Referans tesis, teknoloji paylaşımı |
| İyi | 300-500 | 22-30 | İnce ayar optimizasyonu |
| Ortalama | 500-750 | 18-22 | Sistematik enerji yönetimi |
| Düşük | 750-1,100 | 12-18 | Ciddi iyileştirme programı |
| Kritik | >1,100 | <12 | Acil müdahale, kapsamlı audit |

### 5.3 EU BREF Karşılaştırması

| Parametre | Türkiye Ortalaması | EU BREF BAT | Fark |
|---|---|---|---|
| SEC (süt, pastörizasyon) | 350-500 kWh/ton | 200-320 kWh/ton | %30-50 yüksek |
| SEC (bira) | 200-280 kWh/hL | 130-200 kWh/hL | %25-40 yüksek |
| Soğutma COP | 3.0-4.0 | 4.5-6.0 | %30-50 düşük |
| Isı geri kazanım oranı | %20-40 | %50-75 | %25-35 fark |
| Su tüketimi (süt) | 2.0-4.0 L/L süt | 1.0-2.0 L/L süt | %50-100 yüksek |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Soğutma kondenser temizliği | 2-5 | 1,000-3,000 | <3 ay | Kirli kondenser COP düşürür |
| Basınçlı hava kaçak onarımı | 1-3 | 1,000-5,000 | <3 ay | Ultrasonik kaçak tespiti |
| Buhar kapanı bakımı | 2-4 | 2,000-6,000 | 2-6 ay | Tüm kapanların testi |
| İzolasyon iyileştirme | 1-3 | 3,000-8,000 | 3-8 ay | Buhar hatları, vanalar |
| Soğuk depo kapı disiplini | 1-3 | 500-2,000 | <3 ay | Hızlı kapanma, PVC perde |
| Defrost optimizasyonu | 1-2 | 1,000-5,000 | 3-6 ay | Zamanlama, talep bazlı |
| Aydınlatma LED dönüşümü | 1-2 | 5,000-12,000 | 6-12 ay | Soğuk depolarda ek soğutma tasarrufu |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Soğutma kondenser atık ısısı → sıcak su | 5-10 | 20,000-60,000 | 1-2 yıl | CIP/temizlik sıcak suyu |
| Ekonomizer eklenmesi | 3-5 | 15,000-35,000 | 1-2 yıl | Baca gazı → besleme suyu |
| VSD (soğutma kompresörü) | 5-12 | 20,000-80,000 | 1-3 yıl | Kısmi yükte büyük tasarruf |
| Isı pompası entegrasyonu | 5-15 | 30,000-100,000 | 2-3 yıl | Düşük sıcaklık atık ısı → sıcak su |
| Evaporatör basınç optimizasyonu | 3-6 | 5,000-20,000 | 1-2 yıl | Yükseltilmiş evaporatör sıcaklığı |
| CIP optimizasyonu | 2-5 | 10,000-30,000 | 1-2 yıl | Sıcaklık, süre, su optimizasyonu |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Kojenerasyon (CHP) | 15-25 | 200,000-600,000 | 3-5 yıl | Elektrik + buhar/sıcak su |
| CO₂ transkritik soğutma | 10-20 | 150,000-400,000 | 4-6 yıl | Yüksek COP + ısı geri kazanım |
| Biyogaz tesisi (atık arıtma) | 5-15 | 200,000-500,000 | 4-7 yıl | Organik atıktan enerji |
| Merkezi enerji yönetim sistemi | 5-10 | 50,000-200,000 | 3-5 yıl | SCADA + AI optimizasyonu |
| Güneş enerjisi (PV + termal) | 5-10 | 100,000-300,000 | 5-8 yıl | Elektrik + sıcak su |

### 6.4 Toplam Tasarruf Potansiyeli

```
Toplam tasarruf potansiyeli:

Hızlı kazanımlar:         %8-20
Orta vadeli projeler:     %15-35
Stratejik projeler:       %20-45

Gerçekçi toplam tasarruf: %25-45
Tipik yatırım geri dönüşü (toplam paket): 2-4 yıl
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 Soğutma Sistemi

1. Kondenser basıncını ortam koşullarına göre değişken tutma (floating head pressure)
2. Evaporatör yaklaşım sıcaklığı <3°C hedefi (temizlik ve bakım ile)
3. VSD soğutma kompresörü ile kısmi yük optimizasyonu
4. Soğutma kondenser atık ısısının CIP/temizlik sıcak suyu için kullanılması
5. Soğuk depo kapılarında hızlı kapanma sistemleri ve hava perdeleri
6. Defrost sisteminin talep bazlı kontrol ile optimize edilmesi
7. Soğutucu akışkan seçiminde düşük GWP alternatiflerinin değerlendirilmesi (CO₂, NH₃)

### 7.2 Isıtma Sistemi

1. Pastörizatörlerde rejeneratif ısı geri kazanım oranı >%90 hedefi
2. Kazan baca gazı sıcaklığı <150°C (ekonomizer ile)
3. Kondensat geri dönüş oranı >%80
4. CIP temizlik sıcak suyunun soğutma atık ısısıyla üretilmesi
5. Buhar basıncı proses gereksinimine göre optimize edilmesi

### 7.3 Proses Optimizasyonu

1. CIP programlarının ürün bazlı optimize edilmesi (sıcaklık, konsantrasyon, süre)
2. Üretim planlamasında enerji verimliliğinin dikkate alınması (batch sıralaması)
3. Merkezi izleme sistemi ile anlık enerji tüketimi takibi
4. Atık ısı haritalama ve pinch analizi uygulaması
5. Hijyen standartlarıyla uyumlu ısı geri kazanım fırsatlarının belirlenmesi

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: İzmir, Türkiye
Tesis tipi: Süt işleme ve peynir üretimi
Kapasite: 250 ton/gün süt işleme
Çalışma: 7,000 saat/yıl, 3 vardiya
Ekipman: 2 × 6 ton/h buhar kazanı (doğalgaz), 4 × 250 kW amonyak soğutma
         kompresörü, 3 pastörizatör, 2 UHT hattı, 4 CIP istasyonu,
         2 × 55 kW hava kompresörü
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Doğalgaz tüketimi | 2,800,000 | Nm³/yıl |
| Elektrik tüketimi | 6,500,000 | kWh/yıl |
| Toplam enerji (birincil) | 35,424,000 | kWh/yıl |
| Süt işleme miktarı | 75,000 | ton/yıl |
| SEC | 472 | kWh/ton süt |
| Enerji maliyeti | 1,900,000 | €/yıl |
| Exergy verimi | %18.5 | — |
| Soğutma COP (ortalama) | 3.2 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | Soğutma kondenser atık ısısı → CIP sıcak su (ısı eşanjörü) | 45,000 |
| 2 | VSD retrofit (2 soğutma kompresörü) | 55,000 |
| 3 | Ekonomizer eklenmesi (2 kazan) | 32,000 |
| 4 | Kondensat geri dönüş iyileştirme (%50 → %85) | 18,000 |
| 5 | Floating head pressure kontrol sistemi | 15,000 |
| 6 | CIP optimizasyonu (sıcaklık ve süre) | 8,000 |
| 7 | Soğuk depo LED aydınlatma + kapı iyileştirme | 22,000 |
| 8 | Basınçlı hava kaçak onarımı + bakım | 5,000 |
| **Toplam** | | **200,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| Doğalgaz tüketimi | 2,800,000 Nm³/yıl | 2,184,000 Nm³/yıl | 616,000 Nm³/yıl | -22.0 |
| Elektrik tüketimi | 6,500,000 kWh/yıl | 5,330,000 kWh/yıl | 1,170,000 kWh/yıl | -18.0 |
| Toplam enerji | 35,424,000 kWh/yıl | 27,890,000 kWh/yıl | 7,534,000 kWh/yıl | -21.3 |
| SEC | 472 kWh/ton | 372 kWh/ton | 100 kWh/ton | -21.3 |
| Enerji maliyeti | 1,900,000 €/yıl | 1,487,000 €/yıl | 413,000 €/yıl | -21.7 |
| Exergy verimi | %18.5 | %24.8 | +6.3 puan | +34.1 |
| Soğutma COP | 3.2 | 4.4 | +1.2 | +37.5 |
| CO₂ emisyonu | 7,400 ton/yıl | 5,780 ton/yıl | 1,620 ton/yıl | -21.9 |

### 8.5 Ekonomik Analiz

```
Toplam yatırım:          200,000 €
Yıllık tasarruf:         413,000 €
Basit geri ödeme süresi: 200,000 / 413,000 = 0.48 yıl ≈ 6 ay
Net bugünkü değer (NPV): 2,350,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):    >%200

Tasarruf dağılımı:
  Doğalgaz:    616,000 Nm³ × €0.40/Nm³  = 246,400 €/yıl (%60)
  Elektrik:  1,170,000 kWh × €0.12/kWh  = 140,400 €/yıl (%34)
  Su + kimyasal:                         =  26,200 €/yıl (%6)
```

### 8.6 Öğrenilen Dersler

1. Soğutma kondenser atık ısısının CIP sıcak suyu için kullanılması çift fayda sağladı (hem soğutma COP artışı hem kazan yakıt tasarrufu)
2. VSD retrofit soğutma kompresörlerinde beklenenden yüksek tasarruf verdi (%30 kısmi yükte çalışma)
3. Floating head pressure kontrolü kış aylarında %15-20 kompresör enerji tasarrufu sağladı
4. Hijyen endişeleri nedeniyle bazı ısı geri kazanım fırsatları başlangıçta reddedildi; gıda güvenliği uzmanı ile ortak çalışma çözüm üretti
5. CIP optimizasyonu su ve kimyasal tasarrufuna ek olarak enerji tasarrufu sağladı

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 Soğutma Kondenser Atık Isı Geri Kazanım Potansiyeli

```
Q_kondenser = Q_soğutma × (1 + 1/COP)

Burada:
- Q_soğutma = soğutma kapasitesi [kW]
- COP = soğutma katsayısı

Geri kazanılabilir ısı:
Q_gerikazanım = Q_kondenser × η_eşanjör × (1 - f_kayıp)

Hesaplama örneği:
Q_soğutma = 600 kW, COP = 3.5, η_eşanjör = 0.80, f_kayıp = 0.10

Q_kondenser = 600 × (1 + 1/3.5) = 600 × 1.286 = 771 kW
Q_gerikazanım = 771 × 0.80 × (1 - 0.10) = 555 kW

Yıllık tasarruf (6,500 h, kazan verimi %88, gaz fiyatı €0.40/Nm³):
= 555 × 3.6 × 6,500 / (34.5 × 0.88 × 1,000) × 0.40
= 143,400 €/yıl
```

### 9.2 Isı Pompası COP ve Exergy Analizi

```
COP_ısıpompası = Q_sıcak / W_kompresör
COP_Carnot = T_sıcak / (T_sıcak - T_soğuk)
η_ex,ısıpompası = COP_gerçek / COP_Carnot

Hesaplama örneği (atık ısıdan sıcak su üretimi):
T_soğuk = 35°C = 308.15 K (soğutma kondenser çıkışı)
T_sıcak = 70°C = 343.15 K (CIP sıcak su)
COP_Carnot = 343.15 / (343.15 - 308.15) = 9.8
COP_gerçek = 4.5 (ticari ısı pompası)
η_ex = 4.5 / 9.8 = %45.9

Tasarruf: 1 kWh elektrik ile 4.5 kWh ısı
Doğalgaz eşdeğeri: 4.5 / 0.88 = 5.11 kWh doğalgaz tasarrufu
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Enerji Yönetimi](energy_management.md) -- ISO 50001 uygulama rehberi
- [Kazan Benchmarkları](../boiler/benchmarks.md) -- Kazan verimlilik karşılaştırma verileri
- [Kondensat Geri Dönüş](../boiler/solutions/condensate_return.md) -- Kondensat optimizasyonu
- [Chiller Benchmarkları](../chiller/benchmarks.md) -- Soğutma sistemi benchmark verileri
- [Chiller VSD](../chiller/solutions/vsd.md) -- Soğutma kompresörü VSD uygulamaları
- [Serbest Soğutma](../chiller/solutions/free_cooling.md) -- Free cooling uygulamaları
- [Chiller Isı Geri Kazanım](../chiller/solutions/heat_recovery.md) -- Kondenser atık ısı değerlendirme
- [Kompresör Kaçakları](../compressor/solutions/air_leaks.md) -- Basınçlı hava kaçak tespiti
- [Tekstil Sektörü](sector_textile.md) -- Benzer buhar sistemi gereksinimleri
- [Kimya Sektörü](sector_chemical.md) -- Proses ısı entegrasyonu karşılaştırması

## Referanslar

- EU BREF, "Best Available Techniques (BAT) Reference Document for Food, Drink and Milk Industries," European Commission, 2019
- Carbon Trust, "Food and Drink Processing — Industrial Energy Efficiency," CTG034
- UNIDO, "Energy Efficiency in the Food and Beverage Industry," 2014
- US DOE, "Improving Process Heating System Performance — A Sourcebook for Industry," 2007
- IIF-IIR, "Guidebook on Energy-Efficient Refrigeration Technology in the Food and Drink Sector," 2015
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Gıda Sektörü Enerji Verimliliği Potansiyeli," 2022
- Ramirez, C.A. et al. (2006), "From fluid milk to milk powder: Energy use and energy efficiency in the European dairy industry," Energy, 31(12), 1984-2004
- Thumann, A. & Mehta, D., "Handbook of Energy Engineering," 7th Edition, Fairmont Press, 2013
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- Masanet, E. et al. (2008), "Energy Efficiency Improvement and Cost Saving Opportunities for the Fruit and Vegetable Processing Industry," LBNL
