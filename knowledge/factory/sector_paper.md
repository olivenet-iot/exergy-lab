---
title: "Kağıt ve Selüloz Sektörü Enerji Profili ve Optimizasyon (Paper and Pulp Sector Energy Profile)"
category: factory
equipment_type: factory
keywords: [kağıt, sektör, kurutma, enerji]
related_files: [factory/factory_benchmarks.md, factory/waste_heat_recovery.md, factory/heat_integration.md]
use_when: ["Kağıt fabrikası analiz edilirken", "Kağıt sektörü benchmarkları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Kağıt ve Selüloz Sektörü Enerji Profili ve Optimizasyon (Paper and Pulp Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Kağıt ve selüloz sektörü, yüksek enerji tüketimine sahip endüstriler arasında yer almaktadır. Türkiye'de yıllık kağıt ve karton üretimi 10-12 milyon ton civarında olup büyüme trendindedir. Sektör, buhar ve kurutma yoğun prosesleriyle karakterize edilir. Kojenerasyon (CHP) uygulaması sektörde yaygın olup birçok tesiste biyokütle (siyah likör, ağaç atığı) yakıt olarak kullanılmaktadır. Termal enerji payı %60-70, elektrik payı %30-40 arasındadır. Pres bölümünde mekanik su alma optimizasyonu, termal kurutmadan önce yapılacak en kritik enerji tasarrufu fırsatıdır.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Toplam üretim kapasitesi: ~13 milyon ton/yıl kağıt ve karton
- Gerçek üretim: ~10-12 milyon ton/yıl
- Selüloz (hamur) üretimi: ~1-1.5 milyon ton/yıl (büyük kısmı ithal)
- Tesis sayısı: ~120 kağıt fabrikası
- Geri dönüşüm oranı: %70-80 (atık kağıt bazlı üretim dominant)
- Enerji maliyetinin üretim maliyetindeki payı: %20-35
- Başlıca üretim merkezleri: Kocaeli, Afyon, Kahramanmaraş, Adana, İzmir

### 1.2 Alt Sektörler ve Enerji Yoğunlukları

| Alt Sektör | Enerji Yoğunluğu | Baskın Enerji Türü | Kritik Proses |
|---|---|---|---|
| Selüloz (kimyasal hamur, Kraft) | Çok Yüksek | Termal (%75-85) | Pişirme, yıkama, ağartma |
| Selüloz (mekanik hamur, TMP) | Yüksek | Elektrik (%60-70) | Rafine etme (refining) |
| Gazete kağıdı | Yüksek | Termal (%65-75) | Kurutma |
| Ambalaj kağıdı/karton | Orta-Yüksek | Termal (%60-70) | Kurutma |
| Temizlik kağıdı (tissue) | Yüksek | Termal (%70-80) | Yankee kurutucu |
| Özel kağıtlar | Orta-Yüksek | Termal (%60-70) | Kaplama, kurutma |
| Atık kağıt bazlı (geri dönüşüm) | Orta | Termal (%55-65) | Kurutma, de-inking |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Doğalgaz | 40-60 | Kazan, CHP, kurutucu |
| Biyokütle (siyah likör, ağaç atığı) | 10-40 | Geri kazanım kazanı (Kraft tesislerinde) |
| Elektrik (şebekeden) | 15-30 | Motorlar, rafinerler, pompalar, vakum |
| Elektrik (kendi CHP üretimi) | 10-25 | Buhar türbini / gaz türbini |
| Kömür / fuel oil | 0-10 | Yedek ve bazı eski tesislerde |

### 2.2 Proses Bazlı Enerji Dağılımı (Kağıt Fabrikası — Atık Kağıt Bazlı)

| Proses | Termal Enerji [%] | Elektrik [%] | Toplam Pay [%] |
|---|---|---|---|
| Kurutma bölümü (dryer section) | 50-65 | 3-5 | 40-50 |
| Hamur hazırlama (stock preparation) | 0-5 | 15-25 | 10-18 |
| Pres bölümü (press section) | 0 | 5-8 | 4-6 |
| Elek bölümü (forming/wire section) | 0 | 3-5 | 2-4 |
| Vakum sistemi | 0 | 8-15 | 6-10 |
| Buhar üretimi ve dağıtımı | 15-25 | 1-2 | 12-18 |
| Basınçlı hava | 0 | 3-5 | 2-4 |
| Su arıtma ve pompalama | 0 | 3-5 | 2-4 |
| Aydınlatma ve HVAC | 0 | 2-4 | 1-3 |

### 2.3 Kraft Selüloz Tesisi Enerji Profili

```
Kraft selüloz tesisi enerji dağılımı (tipik):

Termal enerji kaynakları:
  Siyah likör (geri kazanım kazanı): %55-70
  Biyokütle (ağaç kabuğu, atık):    %10-20
  Doğalgaz/fuel oil:                  %10-25

Termal enerji kullanımı:
  Pişirme (digester):               %20-30
  Buharlaştırma (evaporators):       %25-35
  Kurutma:                           %20-30
  Ağartma (bleaching):               %5-10
  Diğer:                             %5-10

Elektrik kullanımı:
  Rafinerler (TMP ise çok yüksek):   %20-35
  Vakum pompaları:                   %10-15
  Pompalar:                          %15-20
  Fanlar:                            %8-12
  Basınçlı hava:                     %5-8
  Aydınlatma ve diğer:               %5-10

CHP (kojenerasyon) ile kendi elektrik üretimi:
  Tipik oran: %50-80 kendi elektrik ihtiyacını karşılar
```

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 Orta Ölçekli Kağıt Fabrikası (Kapasite ~500 ton/gün, atık kağıt bazlı)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Buhar kazanı | 20-40 ton/h | 2-3 | 55-65 (termal) | Doğalgaz |
| CHP (gaz türbini veya buhar türbini) | 5-15 MW_e | 1 | (enerji dönüşümü) | Doğalgaz/buhar |
| Kağıt makinesi kurutucu silindirler | 4-6 m genişlik | 30-60 | 40-50 (termal) | Buhar |
| Vakum pompaları (su ring/turbo) | 100-300 kW | 3-6 | 6-10 (elektrik) | Elektrik |
| Rafiner (LC/HC) | 200-500 kW | 2-4 | 5-10 (elektrik) | Elektrik |
| Sirkülasyon pompaları | 15-100 kW | 15-30 | 5-8 (elektrik) | Elektrik |
| Fan (kurutucu hood, HVAC) | 30-150 kW | 5-10 | 4-6 (elektrik) | Elektrik |
| Basınçlı hava kompresörü | 55-150 kW | 2-4 | 2-4 (elektrik) | Elektrik |
| Su arıtma | - | 1-2 | 1-2 (elektrik) | Elektrik |

### 3.2 Ekipman Referansları

- Kazan sistemleri: bkz. `../boiler/equipment/systems_overview.md`
- Biyokütle kazanı: bkz. `../boiler/equipment/biomass.md`
- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`
- Pompa sistemleri: bkz. `../pump/equipment/systems_overview.md`
- Vakum pompaları: bkz. `../pump/equipment/vacuum.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik Kağıt Fabrikası)

```
DOĞALGAZ EXERGY (%55)  ─────────────────────────────┐
                                                      │
ELEKTRİK EXERGY (%35)  ────────────────────────────┐│
                                                    ││
BİYOKÜTLE EXERGY (%10)  ─────────────────────────┐ ││
                                                  │ ││
                   ┌──────────────────────────────┴─┴┤
                   │     TOPLAM EXERGY GİRİŞİ        │
                   │        (100%)                    │
                   ├──────────────────────────────────┘
                   │
   ┌───────────────┤ Yanma tersinmezliği (%16-22) ──────→ YIKIM
   │               │
   │  ┌────────────┤ Kurutma tersinmezliği (%10-16) ───→ YIKIM
   │  │            │
   │  │  ┌─────────┤ Isı transferi tersinmezliği (%6-10)→ YIKIM
   │  │  │         │
   │  │  │  ┌──────┤ Kurutucu egzoz gazı (%5-10) ─────→ ATIK
   │  │  │  │      │
   │  │  │  │  ┌───┤ Baca gazı exergisi (%4-7) ───────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   │ Vakum/pompa tersinmezliği (%3-6) ─→ YIKIM
   │  │  │  │  │   │ Atık su exergisi (%2-4) ──────────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   ├───────────────────────────────────┐
   │  │  │  │  │   │  ÜRÜN EXERGY (%30-45)             │
   │  │  │  │  │   │  (kağıt ürün exergisi)            │
   │  │  │  │  │   └───────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma tersinmezliği | 16-22 | Kazan ve CHP yanma odası |
| Kurutma tersinmezliği | 10-16 | Buhar → kağıt ısı transferi + buharlaşma |
| Isı transferi tersinmezliği | 6-10 | Eşanjörler, buhar sistemi |
| Kurutucu egzoz gazı | 5-10 | 80-120°C nemli egzoz havası |
| Baca gazı kaybı | 4-7 | Kazan baca gazı 150-250°C |
| Vakum ve pompa tersinmezliği | 3-6 | Su ring vakum, sirkülasyon pompaları |
| Atık su exergisi | 2-4 | Sıcak proses atık suyu |
| Buhar dağıtım kayıpları | 2-3 | İzolasyon, kapan arızaları |
| Basınçlı hava kayıpları | 1-2 | Kaçaklar |

### 4.3 Tipik Exergy Verimi

```
η_ex,kağıt = Ex_ürün / Ex_giriş × 100

Tipik aralık: %30-45
Sektör ortalaması: %36
En iyi uygulama: %50-55

Alt proses exergy verimleri:
  Geri kazanım kazanı (Kraft): %25-35
  Buhar kazanı (doğalgaz):     %30-42
  CHP (buhar türbini):         %35-50
  Kurutma bölümü:              %15-25
  Pres bölümü:                 %40-60
  Vakum sistemi:               %10-20

Not: Kağıt sektörü CHP uygulamasının yaygınlığı nedeniyle
toplam exergy verimi diğer sektörlere göre nispeten yüksektir.
CHP, yakıt exergisini hem elektrik hem ısı olarak değerlendirerek
genel verimliliği artırır.
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Ürün Bazında

| Ürün | SEC Termal [GJ/ton] | SEC Elektrik [kWh/ton] | Kaynak |
|---|---|---|---|
| Kraft selüloz (ağartılmış) | 10-14 | 600-800 | EU BREF |
| Kraft selüloz (ağartılmamış) | 8-12 | 500-700 | EU BREF |
| TMP (termo-mekanik hamur) | 0-2 | 1,800-3,000 | EU BREF |
| Gazete kağıdı (TMP bazlı) | 4-7 | 1,200-2,000 | EU BREF |
| Ambalaj kağıdı (liner) | 4-6 | 400-600 | EU BREF |
| Oluklu mukavva kağıdı (fluting) | 3.5-5.5 | 350-550 | EU BREF |
| Temizlik kağıdı (tissue) | 5-8 | 500-800 | EU BREF |
| Yazı/baskı kağıdı | 5-8 | 600-900 | EU BREF |
| Atık kağıt bazlı (genel) | 3.5-6.0 | 350-650 | Tesis verisi |

### 5.2 Performans Sınıflandırması — Kağıt Fabrikası (Atık Kağıt Bazlı)

| Performans | SEC Termal [GJ/ton] | SEC Elektrik [kWh/ton] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|---|
| Mükemmel | <3.8 | <380 | >48 | Referans tesis |
| İyi | 3.8-4.5 | 380-480 | 40-48 | İnce ayar |
| Ortalama | 4.5-5.5 | 480-580 | 33-40 | Sistematik iyileştirme |
| Düşük | 5.5-7.0 | 580-700 | 25-33 | Ciddi program |
| Kritik | >7.0 | >700 | <25 | Acil müdahale |

### 5.3 EU BREF Karşılaştırması

| Parametre | Türkiye Ortalaması | EU BREF BAT | Fark |
|---|---|---|---|
| SEC termal (liner) | 5.0-6.5 GJ/ton | 3.5-5.0 GJ/ton | %20-30 yüksek |
| SEC elektrik (liner) | 450-600 kWh/ton | 350-500 kWh/ton | %15-25 yüksek |
| CHP penetrasyonu | %30-40 | %60-80 | %25-40 fark |
| Kurutucu hood ısı geri kazanımı | %20-40 | %50-70 | %20-30 fark |
| Su tüketimi | 12-25 m³/ton | 6-15 m³/ton | %40-70 yüksek |
| Pres çıkış kuruluğu | %38-42 | %42-48 | %3-8 fark |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Buhar kapanı bakımı | 2-5 | 5,000-15,000 | 2-6 ay | Kurutucu bölümü kapanları kritik |
| İzolasyon iyileştirme | 1-3 | 5,000-15,000 | 3-8 ay | Buhar hatları, silindirler |
| Basınçlı hava kaçak onarımı | 1-2 | 2,000-8,000 | <3 ay | Kaçak tespit ve onarım |
| Vakum pompa kontrolü | 1-3 | 3,000-10,000 | 3-6 ay | Gereksiz çalışma eliminasyonu |
| Kurutucu hood hava denge optimizasyonu | 2-4 | 5,000-20,000 | 3-6 ay | Hava giriş/çıkış dengesi |
| Kondensat geri dönüş iyileştirme | 1-3 | 3,000-10,000 | 3-6 ay | Kurutucu kondensat geri dönüşü |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Pres bölümü optimizasyonu (shoe press) | 5-12 | 200,000-800,000 | 2-3 yıl | Mekanik su alma → kurutma %20-40 azalma |
| Kurutucu egzoz ısı geri kazanımı | 5-10 | 50,000-200,000 | 1-3 yıl | Egzoz → taze hava ön ısıtma |
| VSD (vakum pompa, fan, pompa) | 3-8 | 30,000-100,000 | 1-3 yıl | Değişken yük optimizasyonu |
| CHP optimizasyonu | 3-8 | 50,000-200,000 | 1-3 yıl | Buhar/elektrik oranı iyileştirme |
| Ekonomizer eklenmesi | 3-5 | 20,000-50,000 | 1-2 yıl | Baca gazı → besleme suyu |
| Kapalı su döngüsü | 3-6 | 50,000-200,000 | 2-3 yıl | Taze su + enerji tasarrufu |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Yeni CHP sistemi (gaz türbini) | 15-25 | 1,000,000-5,000,000 | 3-6 yıl | Yüksek elektrik/ısı oranı |
| Biyokütle kazan entegrasyonu | 10-20 | 500,000-2,000,000 | 3-6 yıl | Fosil yakıt ikamesi |
| İmpuls kurutma / gelişmiş kurutma | 10-20 | 500,000-2,000,000 | 4-7 yıl | Yeni nesil kurutma teknolojisi |
| Isı pompası entegrasyonu | 5-10 | 100,000-400,000 | 3-6 yıl | Düşük sıcaklık ısı yükseltme |
| Dijital ikiz / AI kağıt makinesi kontrolü | 3-6 | 100,000-400,000 | 3-5 yıl | Kurutma/pres optimizasyonu |

### 6.4 Pres vs. Kurutma Enerji Dengesi

```
Pres bölümünde %1 kuruluğa artışın kurutma bölümüne etkisi:

Kural: Pres çıkış kuruluğunun %1 artması → kurutma buhar tüketiminde
       %3-5 azalma sağlar

Hesaplama örneği:
Kağıt üretimi: 500 ton/gün, kurutma öncesi nem: %58 → %42
Gerekli buharlaştırma: 500 × (0.58/0.42 - 1) = 500 × 0.381 = 190 ton su/gün

Pres iyileştirme ile: %58 → %48 nem (shoe press)
Yeni buharlaştırma: 500 × (0.48/0.52 - 1) = 500 × (-0.077) →
Düzeltme: Kuru madde bazlı: 500×0.42 = 210 ton kuru kağıt
Eski: 210/0.42 - 210 = 290 ton su buharlaştırma
Yeni: 210/0.52 - 210 = 194 ton su buharlaştırma
Tasarruf: 96 ton su/gün × 2,260 kJ/kg = 216,960 MJ/gün ≈ 60.3 MWh/gün

Yıllık: 60.3 × 340 gün = 20,500 MWh/yıl
Maliyet: 20,500 × 3.6 / 34.5 / 0.88 × 0.40 = 685,000 €/yıl
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 Kurutma Bölümü

1. Kurutucu silindir kondensat tahliyesinin optimize edilmesi (siphon bakımı)
2. Kurutucu hood kapalı devre ısı geri kazanımı (%50-70 geri kazanım hedefi)
3. Kurutucu bezlerin (felt) düzenli temizlik ve değişimi (ısı transferi iyileştirme)
4. Kurutucu grubu buhar basınç kademesinin optimize edilmesi (cascade)
5. Nem profil kontrolü (CD ve MD nem kontrolü) ile düzgün kurutma

### 7.2 Pres Bölümü

1. Shoe press (geniş nip presi) kullanımı (%5-8 daha yüksek kuruluğa)
2. Pres keçelerinin (felt) düzenli temizlik ve değişimi
3. Pres nip yükünün optimize edilmesi (maksimum su alma)
4. Uhle kutusu vakum optimizasyonu
5. Su alma elemanlarının düzenli bakımı

### 7.3 Buhar ve Enerji Sistemi

1. Kojenerasyon (CHP) ile eşzamanlı elektrik ve buhar üretimi
2. Buhar basıncı kademeli kullanım (high-medium-low pressure cascade)
3. Flash buhar geri kazanımı (kurutucu kondensat hattından)
4. Kondensat geri dönüş oranı >%90 hedefi
5. Kazan baca gazı sıcaklığı <150°C (ekonomizer ile)

### 7.4 Su ve Fiber Yönetimi

1. Kapalı su döngüsü ile taze su ve enerji tüketimi azaltma
2. Fiber geri kazanımı (kısa fiber, dolgu maddesi)
3. Beyaz su sıcaklığı yönetimi (gereksiz soğutmadan kaçınma)
4. Su dengesinin optimize edilmesi (su pinch analizi)
5. Proses suyunun kademeli kullanımı (counter-current washing)

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: Kocaeli, Türkiye
Tesis tipi: Oluklu mukavva kağıdı (fluting + testliner)
Kapasite: 600 ton/gün kağıt
Hammadde: %100 atık kağıt (OCC — old corrugated containers)
Çalışma: 7,500 saat/yıl, sürekli üretim
Ekipman: 2 × 25 ton/h buhar kazanı (doğalgaz), 1 × kağıt makinesi
         (4.5 m genişlik, 700 m/min), 4 × 200 kW vakum pompası,
         3 × 75 kW basınçlı hava kompresörü, 2 × LC refiner
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Doğalgaz tüketimi | 12,000,000 | Nm³/yıl |
| Elektrik tüketimi (şebekeden) | 35,000,000 | kWh/yıl |
| Toplam enerji (birincil) | 159,000,000 | kWh/yıl |
| Kağıt üretimi | 180,000 | ton/yıl |
| SEC termal | 5.8 | GJ/ton kağıt |
| SEC elektrik | 530 | kWh/ton kağıt |
| Enerji maliyeti | 9,000,000 | €/yıl |
| Exergy verimi | %32.0 | — |
| Pres çıkış kuruluğu | %39 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | Shoe press kurulumu (mevcut pres değişimi) | 650,000 |
| 2 | Kurutucu hood ısı geri kazanımı (hava-hava eşanjör) | 120,000 |
| 3 | CHP (5 MW gaz türbini + HRSG) | 2,800,000 |
| 4 | VSD retrofit (4 vakum pompası + 6 pompa + 3 fan) | 85,000 |
| 5 | Ekonomizer (2 kazan) | 38,000 |
| 6 | Buhar kapanı onarımı + izolasyon | 25,000 |
| 7 | Kapalı su döngüsü iyileştirme | 95,000 |
| 8 | Basınçlı hava kaçak onarımı + optimizasyon | 12,000 |
| **Toplam** | | **3,825,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| Doğalgaz tüketimi | 12,000,000 Nm³/yıl | 13,500,000 Nm³/yıl* | +1,500,000 Nm³/yıl | +12.5* |
| Elektrik (şebekeden) | 35,000,000 kWh/yıl | 6,000,000 kWh/yıl | 29,000,000 kWh/yıl | -82.9 |
| CHP elektrik üretimi | 0 | 33,000,000 kWh/yıl | — | — |
| SEC termal | 5.8 GJ/ton | 4.4 GJ/ton | 1.4 GJ/ton | -24.1 |
| SEC elektrik (toplam) | 530 kWh/ton | 500 kWh/ton | 30 kWh/ton | -5.7 |
| Pres çıkış kuruluğu | %39 | %46 | +7 puan | +17.9 |
| Enerji maliyeti | 9,000,000 €/yıl | 6,350,000 €/yıl | 2,650,000 €/yıl | -29.4 |
| Exergy verimi | %32.0 | %42.5 | +10.5 puan | +32.8 |
| CO₂ emisyonu | 26,800 ton/yıl | 22,400 ton/yıl | 4,400 ton/yıl | -16.4 |

*Doğalgaz tüketimi CHP nedeniyle arttı ancak şebekeden elektrik alımı %83 azaldı.

### 8.5 Ekonomik Analiz

```
Toplam yatırım:            3,825,000 €
Yıllık tasarruf:           2,650,000 €
Basit geri ödeme süresi:   3,825,000 / 2,650,000 = 1.44 yıl ≈ 17 ay
Net bugünkü değer (NPV):  13,950,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):     >%65

Tasarruf dağılımı:
  CHP elektrik üretimi vs. şebeke alımı:  = 1,650,000 €/yıl (%62)
  Shoe press (kurutma buharı azalma):      =   520,000 €/yıl (%20)
  Hood ısı geri kazanımı:                  =   210,000 €/yıl (%8)
  VSD + kaçak + izolasyon + diğer:         =   270,000 €/yıl (%10)
```

### 8.6 Öğrenilen Dersler

1. Shoe press kurutma öncesi kuruluğu %39'dan %46'ya çıkararak kurutma buhar tüketimini %25 azalttı
2. CHP sistemi en büyük maliyet tasarrufunu sağladı (%62) ancak en yüksek yatırımı da gerektirdi
3. Hood ısı geri kazanımı tesis içi sıcaklığı da iyileştirdi (operatör konforu)
4. VSD vakum pompalarında %25-35 tasarruf elde edildi (kağıt gramajı değişimlerinde)
5. Kapalı su döngüsü enerji tasarrufuna ek olarak fiber geri kazanımı artırdı (%2 verim artışı)

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 Kurutma Bölümü Buhar Tüketimi

```
ṁ_buhar = ṁ_kağıt × (X_giriş - X_çıkış) × h_fg / (h_buhar × η_kurutucu)

Burada:
- ṁ_kağıt = kağıt üretim hızı [ton/h]
- X_giriş = kurutma girişi nem oranı [kg su/kg kuru]
- X_çıkış = kurutma çıkışı nem oranı [kg su/kg kuru] (~0.05-0.08)
- h_fg = suyun buharlaşma ısısı ≈ 2,260 kJ/kg
- h_buhar = buhar entalpisi [kJ/kg]
- η_kurutucu = kurutucu termal verimi (tipik: 0.55-0.70)

Hesaplama örneği:
ṁ_kağıt = 25 ton/h (kuru bazda), X_giriş = 1.22 (nem %55), X_çıkış = 0.06 (nem %5.5)

Buharlaştırılacak su = 25 × (1.22 - 0.06) = 29.0 ton su/h
ṁ_buhar = 29.0 × 2,260 / (2,066 × 0.65) = 48.8 ton buhar/h (7 bar doymuş)

Spesifik buhar tüketimi = 48.8 / 25 = 1.95 ton buhar/ton kağıt
```

### 9.2 CHP Exergy Verimi

```
η_ex,CHP = (W_elektrik + Ex_buhar) / Ex_yakıt × 100

Burada:
- W_elektrik = elektrik gücü [kW] (saf exergy)
- Ex_buhar = buhar exergisi [kW]
- Ex_yakıt = yakıt exergisi [kW]

Hesaplama örneği (gaz türbini + HRSG):
W_elektrik = 5,000 kW
Buhar üretimi = 12 ton/h, 10 bar doymuş (ex = 858 kJ/kg)
Besleme suyu ex = 28.8 kJ/kg
Ex_buhar = (12,000/3,600) × (858 - 28.8) = 2,764 kW
Yakıt tüketimi = 1,800 Nm³/h doğalgaz
Ex_yakıt = (1,800/3,600) × 34,500 × 1.04 = 17,940 kW

η_ex,CHP = (5,000 + 2,764) / 17,940 = %43.3

Karşılaştırma:
  Ayrı elektrik (şebeke, %35 ex verim): 5,000/0.35 = 14,286 kW yakıt
  Ayrı kazan (%38 ex verim): 2,764/0.38 = 7,274 kW yakıt
  Ayrı üretim toplam: 21,560 kW yakıt
  CHP: 17,940 kW yakıt → %16.8 birincil enerji tasarrufu
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Enerji Yönetimi](energy_management.md) -- ISO 50001 uygulama rehberi
- [Kazan Benchmarkları](../boiler/benchmarks.md) -- Kazan verimlilik karşılaştırma verileri
- [Biyokütle Kazanı](../boiler/equipment/biomass.md) -- Biyokütle kazan teknolojileri
- [Atık Isı Kazanı](../boiler/equipment/waste_heat.md) -- HRSG ve atık ısı kazanları
- [Kondensat Geri Dönüş](../boiler/solutions/condensate_return.md) -- Kondensat optimizasyonu
- [Buhar Kapanı](../boiler/solutions/steam_trap.md) -- Buhar kapanı bakımı
- [Pompa Benchmarkları](../pump/benchmarks.md) -- Pompa verimlilik verileri
- [Vakum Pompaları](../pump/equipment/vacuum.md) -- Vakum sistemi ekipmanları
- [Pompa VSD](../pump/solutions/vsd.md) -- Pompa VSD uygulamaları
- [Kompresör Kaçakları](../compressor/solutions/air_leaks.md) -- Basınçlı hava kaçak yönetimi
- [Tekstil Sektörü](sector_textile.md) -- Benzer kurutma yoğun proses
- [Çimento Sektörü](sector_cement.md) -- Benzer ölçekte enerji tüketimi

## Referanslar

- EU BREF, "Best Available Techniques (BAT) Reference Document for the Production of Pulp, Paper and Board," European Commission, 2015
- IEA, "Pulp and Paper Industry Energy Efficiency and CO₂ Emissions Reduction," 2020
- CEPI, "Key Statistics — European Pulp and Paper Industry," 2023
- Bajpai, P., "Pulp and Paper Industry: Energy Conservation," Elsevier, 2016
- Suhr, M. et al. (2015), "Best Available Techniques (BAT) Reference Document for the Production of Pulp, Paper and Board," EUR 27235 EN
- Laurijssen, J. et al. (2010), "Optimizing the energy efficiency of conventional multi-cylinder dryers in the paper industry," Energy, 35(9), 3738-3750
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Kağıt Sektörü Enerji Verimliliği Potansiyeli," 2022
- TAPPI, "TIPs (Technical Information Papers) for Energy Conservation," 2019
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- Kong, L. et al. (2016), "Energy conservation and CO₂ mitigation potentials in the Chinese pulp and paper industry," Resources, Conservation and Recycling, 117, 74-84
