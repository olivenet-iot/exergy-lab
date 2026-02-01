---
title: "Tekstil Sektoru Enerji Profili ve Optimizasyon (Textile Sector Energy Profile)"
category: factory
equipment_type: factory
keywords: [tekstil, sektör, boyama, enerji]
related_files: [factory/factory_benchmarks.md, factory/heat_integration.md, factory/waste_heat_recovery.md]
use_when: ["Tekstil fabrikası analiz edilirken", "Tekstil sektörü benchmarkları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Tekstil Sektoru Enerji Profili ve Optimizasyon (Textile Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Tekstil sektörü, Türkiye'nin en büyük sanayi kollarından biri olup toplam sanayi üretiminin yaklaşık %8'ini, ihracatın ise %15-18'ini oluşturur. Sektör yüksek enerji yoğunluğuna sahiptir ve özellikle boyama/terbiye prosesleri buhar ağırlıklı enerji tüketimi ile karakterize edilir. Yıllık enerji tüketimi Türkiye sanayisinin yaklaşık %5-7'sine karşılık gelir. Toplam enerji girdisinin %60-70'i termal (doğalgaz/buhar), %30-40'ı elektrik enerjisidir. Su tüketimi de son derece yüksek olup 1 kg kumaş başına 50-150 litre su kullanılmaktadır.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Toplam tesis sayısı: ~45,000 (kayıtlı tekstil işletmesi)
- İstihdam: ~1,000,000 doğrudan çalışan
- Yıllık ihracat: ~18-20 milyar USD
- Enerji maliyetinin üretim maliyetindeki payı: %8-15
- Başlıca üretim merkezleri: Bursa, Denizli, Gaziantep, İstanbul, Adana, Kahramanmaraş

### 1.2 Alt Sektörler ve Enerji Yoğunlukları

| Alt Sektör | Enerji Yoğunluğu | Termal/Elektrik Oranı | Baskın Proses |
|---|---|---|---|
| İplik (Spinning) | Orta | 30/70 | Elektrik motorları |
| Dokuma (Weaving) | Düşük-Orta | 25/75 | Tezgah motorları |
| Örme (Knitting) | Düşük | 20/80 | Örme makineleri |
| Boyama/Terbiye (Dyeing/Finishing) | Çok Yüksek | 70/30 | Buhar, sıcak su |
| Baskı (Printing) | Yüksek | 60/40 | Buhar, kurutma |
| Konfeksiyon (Garment) | Düşük | 40/60 | Ütü, basınçlı hava |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Doğalgaz | 55-65 | Kazan yakıtı, ram/stenter |
| Elektrik | 30-40 | Motorlar, pompalar, basınçlı hava, aydınlatma |
| Kömür/biyokütle | 0-10 | Bazı tesislerde kazan yakıtı |
| LPG/fuel oil | 0-5 | Yedek yakıt |

### 2.2 Proses Bazlı Enerji Dağılımı (Boyama/Terbiye Tesisi)

| Proses | Termal Enerji [%] | Elektrik [%] | Toplam Pay [%] |
|---|---|---|---|
| Boyama (dyeing) | 35-45 | 5-8 | 30-38 |
| Kurutma (drying) | 20-28 | 3-5 | 18-25 |
| Ram/Stenter (finishing) | 15-22 | 2-4 | 14-20 |
| Yıkama (washing) | 8-12 | 2-3 | 7-10 |
| Kazan dairesi kayıpları | 8-12 | 1-2 | 6-10 |
| Basınçlı hava | 0 | 5-8 | 4-6 |
| Aydınlatma ve HVAC | 0 | 3-5 | 2-4 |

### 2.3 Mevsimsel Değişim

```
Kış dönemi: +%10-15 enerji tüketimi artışı
  - Kazan besleme suyu sıcaklığı düşer (ΔT artar)
  - Ortam sıcaklığı düşer → yüzey kayıpları artar
  - Proses suyu ön ısıtma gereksinimi artar

Yaz dönemi: -%5-10 termal, +%5-8 elektrik
  - Soğutma ihtiyacı artar (boyahane iklimlendirme)
  - Termal kayıplar azalır
```

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 Orta Ölçekli Boyama/Terbiye Tesisi (Kapasitesi ~20 ton/gün)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Buhar kazanı (ateş borulu) | 6-10 ton/h buhar | 2 | 55-65 | Doğalgaz |
| Jet boyama makinesi | 200-1,000 kg/parti | 6-12 | 15-25 | Buhar |
| Ram/Stenter | 2-4 m genişlik | 2-3 | 12-18 | Doğalgaz (direkt) |
| Kurutma makinesi (silindir) | 2-4 m genişlik | 1-2 | 5-8 | Buhar |
| Basınçlı hava kompresörü | 30-75 kW | 2-3 | 4-6 | Elektrik |
| Sirkülasyon pompaları | 5-30 kW | 10-20 | 3-5 | Elektrik |
| Kasar (bleaching) makinesi | Sürekli | 1 | 3-5 | Buhar |
| Aydınlatma | - | - | 2-3 | Elektrik |
| Yumuşak su arıtma | - | 1-2 | <1 | Elektrik |

### 3.2 Ekipman Referansları

Ekipman detayları için:
- Kazan sistemleri: bkz. `../boiler/equipment/systems_overview.md`
- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik Boyama/Terbiye Tesisi)

```
DOĞALGAZ EXERGY (%68)  ─────────────────────────────┐
                                                      │
ELEKTRİK EXERGY (%32) ─────────────────────────────┐│
                                                    ││
                   ┌────────────────────────────────┴┤
                   │     TOPLAM EXERGY GİRİŞİ        │
                   │        (100%)                    │
                   ├──────────────────────────────────┘
                   │
   ┌───────────────┤ Yanma tersinmezliği (%18-25) ──────→ YIKIM
   │               │
   │  ┌────────────┤ Isı transferi (kazan) (%12-18) ───→ YIKIM
   │  │            │
   │  │  ┌─────────┤ Boyama atık suyu exergisi (%8-14) ─→ ATIK
   │  │  │         │
   │  │  │  ┌──────┤ Ram/stenter baca gazı (%6-10) ────→ ATIK
   │  │  │  │      │
   │  │  │  │  ┌───┤ Kazan baca gazı (%5-8) ───────────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   │ Motor/pompa tersinmezliği (%4-7) ──→ YIKIM
   │  │  │  │  │   │
   │  │  │  │  │   ├────────────────────────────────────┐
   │  │  │  │  │   │  ÜRÜN EXERGY (%20-30)              │
   │  │  │  │  │   │  (kumaş ısıl işlemi tamamlanmış)   │
   │  │  │  │  │   └────────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma tersinmezliği | 18-25 | Kazan ve ram yakma odalarında |
| Isı transferi tersinmezliği | 12-18 | Kazan, boyama makinesi eşanjörleri |
| Boyama atık suyu | 8-14 | 60-95°C sıcak su drenaj edilir |
| Ram/stenter egzoz gazı | 6-10 | 150-200°C sıcak hava atılır |
| Baca gazı | 5-8 | Kazandan 150-250°C çıkış |
| Motor/pompa tersinmezliği | 4-7 | Sirkülasyon, transfer pompaları |
| Basınçlı hava kayıpları | 2-4 | Kaçak, basınç düşüşü |
| Buhar dağıtım kayıpları | 2-4 | İzolasyon, kapan arızaları |
| Kondensat kayıpları | 1-3 | Geri dönmeyen kondensat |

### 4.3 Tipik Exergy Verimi

```
η_ex,tekstil = Ex_ürün / Ex_giriş × 100

Tipik aralık: %20-30
Sektör ortalaması: %24
En iyi uygulama: %38-40

Not: Boyama prosesinin düşük sıcaklık gereksinimi (60-130°C) nedeniyle
yüksek kaliteli exergy (yakıt) düşük kaliteli exergy ihtiyacı için
kullanılmakta, bu da yüksek exergy yıkımına neden olmaktadır.
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Alt Proses Bazında

| Alt Proses | SEC [kWh/kg kumaş] | Birim | Kaynak |
|---|---|---|---|
| İplik üretimi (ring) | 3.0-5.0 | kWh/kg iplik | BREF Textiles |
| İplik üretimi (open-end) | 1.5-3.0 | kWh/kg iplik | BREF Textiles |
| Dokuma | 0.5-1.5 | kWh/kg kumaş | BREF Textiles |
| Örme | 0.3-0.8 | kWh/kg kumaş | BREF Textiles |
| Boyama (parti, jet) | 2.5-6.0 | kWh/kg kumaş | BREF Textiles |
| Boyama (sürekli, pad) | 1.5-3.5 | kWh/kg kumaş | BREF Textiles |
| Ram/stenter kurutma | 1.0-3.0 | kWh/kg kumaş | BREF Textiles |
| Baskı (rotary) | 1.5-4.0 | kWh/kg kumaş | BREF Textiles |
| Entegre tesis (toplam) | 3.0-15.0 | kWh/kg kumaş | Tesis denetimleri |

### 5.2 Performans Sınıflandırması — Boyama/Terbiye Tesisi

| Performans | SEC [kWh/kg] | Exergy Verimi [%] | Su Tüketimi [L/kg] | Aksiyon |
|---|---|---|---|---|
| Mükemmel | <3.5 | >35 | <40 | Referans tesis, bilgi paylaşımı |
| İyi | 3.5-5.5 | 28-35 | 40-70 | İnce ayar optimizasyonu |
| Ortalama | 5.5-8.0 | 22-28 | 70-100 | Sistematik enerji yönetimi |
| Düşük | 8.0-12.0 | 15-22 | 100-150 | Ciddi iyileştirme programı |
| Kritik | >12.0 | <15 | >150 | Acil müdahale, kapsamlı audit |

### 5.3 EU BREF Karşılaştırması

| Parametre | Türkiye Ortalaması | EU BREF BAT | Fark |
|---|---|---|---|
| SEC (boyama, jet) | 5.5-7.0 kWh/kg | 2.5-4.5 kWh/kg | %30-50 yüksek |
| Su tüketimi | 80-120 L/kg | 30-60 L/kg | %50-100 yüksek |
| Kondensat geri dönüş | %40-60 | >%80 | %20-40 fark |
| Baca gazı sıcaklığı | 200-280°C | <150°C | 50-130°C fark |
| Boyama flotte oranı | 1:8 - 1:12 | 1:4 - 1:6 | Yüksek su/enerji |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Basınçlı hava kaçak onarımı | 2-4 | 1,000-5,000 | <3 ay | Ultrasonik kaçak tespiti |
| Buhar kapanı bakımı | 2-5 | 2,000-8,000 | 2-6 ay | Tüm kapanların testi |
| İzolasyon iyileştirme | 1-3 | 3,000-10,000 | 3-8 ay | Vanalar, flanşlar, borular |
| Brülör ayarı/bakımı | 1-2 | 500-2,000 | <3 ay | O₂ trim optimizasyonu |
| Aydınlatma LED dönüşümü | 1-2 | 5,000-15,000 | 6-12 ay | Elektrik tasarrufu |
| Boyama makinesi kapaklarının kapatılması | 1-2 | 500-2,000 | <3 ay | Buharlaşma kaybı azaltma |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Boyama atık suyu ısı geri kazanımı | 8-15 | 30,000-80,000 | 1-2 yıl | Eşanjör ile taze su ön ısıtma |
| Kondensat geri dönüş iyileştirme | 3-6 | 10,000-30,000 | 1-2 yıl | %50 → %80+ geri dönüş |
| Ekonomizer eklenmesi | 3-5 | 15,000-40,000 | 1-2 yıl | Baca gazı → besleme suyu |
| VSD (pompa/fan) retrofit | 3-8 | 10,000-40,000 | 1-3 yıl | Sirkülasyon pompaları |
| Ram/stenter egzoz ısı geri kazanımı | 5-10 | 25,000-60,000 | 1.5-3 yıl | 150-200°C egzoz gazı |
| Düşük flotte boyama teknolojisi | 5-12 | 50,000-150,000 | 2-3 yıl | 1:4 flotte oranı |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Kojenerasyon (CHP) | 15-25 | 200,000-500,000 | 3-5 yıl | Eşzamanlı elektrik+buhar |
| Güneş enerjisi ön ısıtma | 5-10 | 50,000-150,000 | 4-7 yıl | Proses suyu ön ısıtma |
| Proses suyu geri kazanımı (MBR) | 10-20 | 100,000-300,000 | 3-5 yıl | Su + enerji tasarrufu |
| Dijital ikiz/otomasyon | 5-10 | 50,000-200,000 | 3-5 yıl | Gerçek zamanlı optimizasyon |
| Isı pompası entegrasyonu | 8-15 | 80,000-250,000 | 3-6 yıl | Atık sıcak su → buhar ön ısıtma |

### 6.4 Toplam Tasarruf Potansiyeli

```
Toplam tasarruf potansiyeli hesabı:

Hızlı kazanımlar:         %8-18
Orta vadeli projeler:     %15-30
Stratejik projeler:       %20-40

Not: Önlemler kümülatif değildir. Gerçekçi toplam tasarruf: %25-45
Tipik yatırım geri dönüşü (toplam paket): 2-4 yıl
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 Enerji Yönetimi

1. ISO 50001 enerji yönetim sistemi uygulanması
2. Alt ölçüm sistemi ile proses bazlı izleme (boyama makinesi, ram, kazan ayrı ayrı)
3. Spesifik enerji tüketimi (SEC) KPI'larının günlük takibi
4. Enerji yöneticisi atanması ve enerji takımı oluşturulması
5. Operatör enerji farkındalık eğitimi (yılda en az 2 kez)

### 7.2 Buhar Sistemi

1. Kondensat geri dönüş oranı >%80 hedefi
2. Tüm buhar kapanlarının yılda 2 kez testi
3. Ekonomizer ile baca gazı sıcaklığı <150°C hedefi
4. Buhar basıncı optimizasyonu (gereksiz yüksek basınçtan kaçınma)
5. Flash buhar geri kazanımı (kondensat hatlarında)

### 7.3 Boyama Prosesi

1. Düşük flotte oranı (1:4 - 1:6) boyama teknolojisi kullanımı
2. Soğuk pad-batch boyama yönteminin değerlendirilmesi (enerji tasarrufu %50-70)
3. Boyama atık suyundan ısı geri kazanımı (eşanjör ile >%60 geri kazanım)
4. Boyama reçetelerinin enerji verimliliği açısından optimize edilmesi
5. Makine doluluk oranının >%85 tutulması (kısmi yükten kaçınma)

### 7.4 Kurutma ve Terbiye

1. Mekanik sıkma/vakum suyu alma sonra termal kurutma (enerji tasarrufu %20-40)
2. Ram/stenter egzoz gazı ısı geri kazanımı
3. Ram hava sirkülasyon optimizasyonu
4. Kurutma hızı ve sıcaklık profillerinin ürün bazlı optimizasyonu
5. Nem kontrol sensörleri ile otomatik ram kontrolü

### 7.5 Basınçlı Hava

1. Sistem basıncı optimizasyonu (gereksiz yüksek basınçtan kaçınma)
2. Düzenli kaçak tespiti ve onarımı (üç ayda bir)
3. VSD kompresör kullanımı (değişken yükte %15-30 tasarruf)
4. Kompresör atık ısısının kazan besleme suyu ön ısıtmada kullanılması

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: Bursa, Türkiye
Tesis tipi: Boyama ve terbiye (pamuklu kumaş)
Kapasite: 18 ton/gün kumaş boyama
Çalışma: 6,500 saat/yıl, 3 vardiya
Ekipman: 2 × 8 ton/h buhar kazanı (doğalgaz), 10 jet boyama makinesi,
         3 ram/stenter, 2 kurutma silindiri, 3 × 55 kW kompresör
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Doğalgaz tüketimi | 3,200,000 | Nm³/yıl |
| Elektrik tüketimi | 4,800,000 | kWh/yıl |
| Toplam enerji (birincil) | 37,856,000 | kWh/yıl |
| Kumaş üretimi | 5,400 | ton/yıl |
| SEC | 7.01 | kWh/kg kumaş |
| Su tüketimi | 540,000 | m³/yıl (100 L/kg) |
| Enerji maliyeti | 1,620,000 | €/yıl |
| Exergy verimi | %22.5 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | Boyama atık suyu ısı geri kazanımı (3 × plaka eşanjör) | 65,000 |
| 2 | Kondensat geri dönüş iyileştirme (%45 → %82) | 22,000 |
| 3 | Ekonomizer eklenmesi (2 kazan) | 38,000 |
| 4 | VSD retrofit (6 sirkülasyon pompası + 2 fan) | 28,000 |
| 5 | Basınçlı hava kaçak onarımı + VSD kompresör | 18,000 |
| 6 | Ram egzoz ısı geri kazanımı (2 ram) | 45,000 |
| 7 | İzolasyon iyileştirme (vanalar, flanşlar) | 8,000 |
| 8 | LED aydınlatma dönüşümü | 12,000 |
| **Toplam** | | **236,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| Doğalgaz tüketimi | 3,200,000 Nm³/yıl | 2,400,000 Nm³/yıl | 800,000 Nm³/yıl | -25.0 |
| Elektrik tüketimi | 4,800,000 kWh/yıl | 4,080,000 kWh/yıl | 720,000 kWh/yıl | -15.0 |
| Toplam enerji | 37,856,000 kWh/yıl | 28,872,000 kWh/yıl | 8,984,000 kWh/yıl | -23.7 |
| SEC | 7.01 kWh/kg | 5.35 kWh/kg | 1.66 kWh/kg | -23.7 |
| Su tüketimi | 540,000 m³/yıl | 432,000 m³/yıl | 108,000 m³/yıl | -20.0 |
| Enerji maliyeti | 1,620,000 €/yıl | 1,215,000 €/yıl | 405,000 €/yıl | -25.0 |
| Exergy verimi | %22.5 | %29.8 | +7.3 puan | +32.4 |
| CO₂ emisyonu | 8,250 ton/yıl | 6,190 ton/yıl | 2,060 ton/yıl | -25.0 |

### 8.5 Ekonomik Analiz

```
Toplam yatırım:          236,000 €
Yıllık tasarruf:         405,000 €
Basit geri ödeme süresi: 236,000 / 405,000 = 0.58 yıl ≈ 7 ay
Net bugünkü değer (NPV): 2,150,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):    >%150

Tasarruf dağılımı:
  Doğalgaz:    800,000 Nm³ × €0.40/Nm³ = 320,000 €/yıl (%79)
  Elektrik:    720,000 kWh × €0.12/kWh  =  86,400 €/yıl (%21)
  (Su tasarrufu ek gelir olarak hesaba katılmamıştır)
```

### 8.6 Öğrenilen Dersler

1. Boyama atık suyu ısı geri kazanımı en yüksek getiriyi sağladı (%35 toplam tasarrufun)
2. Kondensat geri dönüş iyileştirmesi düşük yatırım/yüksek getiri oranı ile dikkat çekti
3. VSD retrofit beklenenden iyi sonuç verdi (sirkülasyon pompaları ortalama %50 yükte çalışıyordu)
4. Operatör eğitimi ve bilinçlendirme, teknik önlemlerin kalıcılığı için kritik öneme sahip
5. Ölçüm sistemi (alt sayaçlar) olmadan tasarrufların doğrulanması güçtür

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 Boyama Atık Suyu Isı Geri Kazanım Potansiyeli

```
Q_gerikazanım = ṁ_atıksu × Cp × (T_atıksu - T_tazeSu) × η_eşanjör

Burada:
- ṁ_atıksu = atık su debisi [kg/s]
- Cp = suyun özgül ısısı = 4.18 kJ/(kg·K)
- T_atıksu = atık su sıcaklığı [°C]
- T_tazeSu = taze su sıcaklığı [°C]
- η_eşanjör = eşanjör verimi (tipik: 0.70-0.85)

Hesaplama örneği:
ṁ_atıksu = 5 kg/s (18 m³/h)
T_atıksu = 75°C, T_tazeSu = 15°C, η_eşanjör = 0.80

Q_gerikazanım = 5 × 4.18 × (75 - 15) × 0.80 = 1,003 kW

Yıllık tasarruf = 1,003 × 6,000 h × 3.6 MJ/kWh / (34.5 MJ/Nm³ × 0.88)
              = 713,000 Nm³/yıl doğalgaz
              ≈ 285,200 €/yıl (@€0.40/Nm³)
```

### 9.2 Ram/Stenter Enerji Tüketimi

```
SEC_ram = (ṁ_hava × Cp_hava × ΔT + ṁ_su_buh × h_fg) / ṁ_kumaş

Burada:
- ṁ_hava = sirkülasyon hava debisi [kg/s]
- Cp_hava = havanın özgül ısısı ≈ 1.01 kJ/(kg·K)
- ΔT = hava sıcaklık farkı [°C]
- ṁ_su_buh = kumaştan buharlaşan su debisi [kg/s]
- h_fg = suyun buharlaşma ısısı ≈ 2,260 kJ/kg
- ṁ_kumaş = kumaş üretim hızı [kg/s]

Hesaplama örneği:
ṁ_hava = 8 kg/s, ΔT = 120°C, ṁ_su_buh = 0.15 kg/s, ṁ_kumaş = 0.5 kg/s

SEC_ram = (8 × 1.01 × 120 + 0.15 × 2,260) / 0.5
       = (969.6 + 339.0) / 0.5 = 2,617 kJ/kg = 0.727 kWh/kg
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Enerji Yönetimi](energy_management.md) -- ISO 50001 uygulama rehberi
- [Sistem Sınırları](system_boundaries.md) -- Ölçüm noktaları ve kontrol hacimleri
- [Kazan Benchmarkları](../boiler/benchmarks.md) -- Kazan verimlilik karşılaştırma verileri
- [Kazan Formülleri](../boiler/formulas.md) -- Buhar sistemi exergy hesaplamaları
- [Ekonomizer](../boiler/solutions/economizer.md) -- Baca gazı ısı geri kazanımı
- [Kondensat Geri Dönüş](../boiler/solutions/condensate_return.md) -- Kondensat sistemi optimizasyonu
- [Kompresör Benchmarkları](../compressor/benchmarks.md) -- Basınçlı hava verimlilik verileri
- [Kompresör VSD](../compressor/solutions/vsd.md) -- Değişken hız sürücü uygulamaları
- [Hava Kaçakları](../compressor/solutions/air_leaks.md) -- Kaçak tespit ve onarım
- [Gıda Sektörü](sector_food.md) -- Benzer ısıl proses gereksinimleri
- [Kimya Sektörü](sector_chemical.md) -- Proses ısı entegrasyonu karşılaştırması

## Referanslar

- EU BREF, "Best Available Techniques (BAT) Reference Document for the Textiles Industry," European Commission, 2003 (revision ongoing)
- IPPC, "Reference Document on Best Available Techniques for the Textiles Industry," 2003
- UNIDO, "Textile Industry: Energy Efficiency Improvement Opportunities," 2017
- Carbon Trust, "Industrial Energy Efficiency Accelerator — Textiles Sector," CTG064
- Hasanbeigi, A., "Energy-Efficiency Improvement Opportunities for the Textile Industry," LBNL, 2010
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Sanayi Sektörü Enerji Verimliliği Potansiyeli," 2022
- TÜBITAK MAM, "Tekstil Sektörü Enerji Verimliliği Rehberi," 2019
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- Çay, A. et al. (2017), "Energy consumption and carbon dioxide emissions in the textile industry," Energy, 141, 56-67
- Ozturk, E. et al. (2020), "Textile sector environmental and energy profile in Turkey," Journal of Cleaner Production, 272, 122706
