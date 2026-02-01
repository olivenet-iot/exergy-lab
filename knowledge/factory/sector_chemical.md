---
title: "Kimya Sektörü Enerji Profili ve Optimizasyon (Chemical Sector Energy Profile)"
category: factory
equipment_type: factory
keywords: [kimya, sektör, proses, enerji]
related_files: [factory/factory_benchmarks.md, factory/process_integration.md, factory/heat_integration.md]
use_when: ["Kimya fabrikası analiz edilirken", "Kimya sektörü benchmarkları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Kimya Sektörü Enerji Profili ve Optimizasyon (Chemical Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Kimya sektörü, endüstriyel enerji tüketiminin en yüksek olduğu sektörlerden biridir. Türkiye'de sanayi enerjisinin yaklaşık %12-15'ini tüketir. Sektör, ekzotermik ve endotermik reaksiyonların karışımıyla karakterize edilen karmaşık enerji profiline sahiptir. Proses ısısı yoğun kullanılır ve pinch analizi tabanlı ısı entegrasyonu en kritik optimizasyon yöntemidir. Enerji girdisinin %60-75'i termal (doğalgaz, buhar), %25-40'ı elektrik enerjisidir. Exergy verimi sektör genelinde %30-50 aralığında olup diğer sektörlere göre nispeten yüksektir.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Toplam tesis sayısı: ~12,000 (kayıtlı kimya ve petrokimya tesisi)
- İstihdam: ~200,000 doğrudan çalışan
- Yıllık üretim değeri: ~35-40 milyar USD
- Enerji maliyetinin üretim maliyetindeki payı: %15-40 (alt sektöre göre)
- Başlıca üretim merkezleri: Kocaeli, İstanbul, İzmir, Adana, Mersin (Ceyhan)
- Türkiye'de petrokimya ithalat bağımlılığı yüksek (%60-70)

### 1.2 Alt Sektörler ve Enerji Yoğunlukları

| Alt Sektör | Enerji Yoğunluğu | Termal/Elektrik Oranı | Baskın Proses |
|---|---|---|---|
| Temel kimyasallar (Basic) | Çok Yüksek | 75/25 | Cracking, reforming |
| Petrokimya | Çok Yüksek | 70/30 | Distilasyon, polimerizasyon |
| Gübre (Fertilizer) | Yüksek | 80/20 | Amonyak sentezi, üre üretimi |
| Özel kimyasallar (Specialty) | Orta-Yüksek | 55/45 | Batch reaksiyonlar, kurutma |
| Boya ve kaplama | Orta | 50/50 | Karıştırma, dispersiyon, kurutma |
| Temizlik ürünleri | Düşük-Orta | 55/45 | Reaksiyon, karıştırma |
| Plastik işleme | Orta | 30/70 | Ekstrüzyon, enjeksiyon (elektrik) |
| İlaç (Pharmaceutical) | Orta | 55/45 | Batch reaksiyon, kurutma, HVAC |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Doğalgaz | 50-65 | Kazan, fırın, reaktör ısıtma, CHP |
| Elektrik | 25-40 | Kompresörler, pompalar, karıştırıcılar, soğutma |
| Buhar (harici alım) | 0-15 | Büyük komplekslerde merkezi buhar |
| Fuel oil / LPG | 0-5 | Yedek yakıt, bazı prosesler |
| Proses gazları (H₂, off-gas) | 0-10 | Yan ürün gazlarının yakılması |

### 2.2 Proses Bazlı Enerji Dağılımı (Genel Kimya Tesisi)

| Proses | Termal Enerji [%] | Elektrik [%] | Toplam Pay [%] |
|---|---|---|---|
| Reaksiyon ısıtma/soğutma | 25-40 | 5-10 | 25-35 |
| Distilasyon/ayırma | 20-30 | 3-5 | 18-25 |
| Buhar üretimi ve dağıtımı | 10-15 | 1-2 | 8-12 |
| Kurutma | 5-15 | 2-3 | 5-12 |
| Kompresörler (proses gazı) | 0 | 8-15 | 6-12 |
| Pompalar ve karıştırıcılar | 0 | 5-10 | 4-8 |
| Soğutma sistemi | 0 | 5-10 | 4-8 |
| HVAC ve aydınlatma | 2-4 | 3-5 | 3-5 |

### 2.3 Reaksiyon Enerji Profili

```
Endotermik reaksiyonlar (ısı gerektirir):
  - Termal cracking: 800-1,100°C
  - Steam reforming (H₂ üretimi): 700-900°C
  - Kalsinasyon: 800-1,000°C
  - Endotermik dehidrasyon: 100-400°C

Ekzotermik reaksiyonlar (ısı açığa çıkar):
  - Oksidasyon reaksiyonları: ΔH = -100 ile -500 kJ/mol
  - Polimerizasyon: ΔH = -50 ile -100 kJ/mol
  - Nötralizasyon: ΔH = -55 kJ/mol
  - Sülfürleme/klorürleme: ΔH = -80 ile -200 kJ/mol

Ekzotermik reaksiyonlardan açığa çıkan ısının geri kazanımı
exergy verimi açısından kritik öneme sahiptir.
```

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 Orta Ölçekli Kimya Tesisi (Özel Kimyasallar)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Buhar kazanı | 6-15 ton/h | 2-3 | 30-40 | Doğalgaz |
| Batch reaktör (ceketli) | 2-20 m³ | 5-15 | 15-25 | Buhar + soğutma |
| Distilasyon kolonu | 0.5-3 m çap | 2-6 | 12-20 | Buhar (reboiler) |
| Kurutucu (spray/drum) | 500-2,000 kg/h | 1-3 | 8-15 | Buhar / doğalgaz |
| Soğutma sistemi (chiller) | 200-800 kW | 2-4 | 5-10 | Elektrik |
| Proses kompresörü | 50-200 kW | 2-4 | 5-10 | Elektrik |
| Hava kompresörü | 30-75 kW | 2-3 | 3-5 | Elektrik |
| Sirkülasyon pompaları | 5-55 kW | 10-30 | 3-5 | Elektrik |
| Isı eşanjörleri | 50-500 kW | 10-20 | — | (pasif ekipman) |
| Karıştırıcılar | 3-30 kW | 5-15 | 1-3 | Elektrik |

### 3.2 Ekipman Referansları

- Kazan sistemleri: bkz. `../boiler/equipment/systems_overview.md`
- Soğutma sistemleri: bkz. `../chiller/equipment/systems_overview.md`
- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`
- Pompa sistemleri: bkz. `../pump/equipment/systems_overview.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik Kimya Tesisi)

```
DOĞALGAZ EXERGY (%62)  ─────────────────────────────┐
                                                      │
ELEKTRİK EXERGY (%35)  ────────────────────────────┐│
                                                    ││
HAMMADDE KİMYASAL EXERGY (%3) ───────────────────┐ ││
                                                  │ ││
                   ┌──────────────────────────────┴─┴┤
                   │     TOPLAM EXERGY GİRİŞİ        │
                   │        (100%)                    │
                   ├──────────────────────────────────┘
                   │
   ┌───────────────┤ Yanma tersinmezliği (%14-20) ──────→ YIKIM
   │               │
   │  ┌────────────┤ Reaksiyon tersinmezliği (%8-15) ───→ YIKIM
   │  │            │
   │  │  ┌─────────┤ Isı transferi tersinmezliği (%8-14)→ YIKIM
   │  │  │         │
   │  │  │  ┌──────┤ Distilasyon tersinmezliği (%5-10) ─→ YIKIM
   │  │  │  │      │
   │  │  │  │  ┌───┤ Baca gazı + atık ısı (%5-10) ─────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   │ Kompresör/pompa kayıpları (%3-6) ──→ YIKIM
   │  │  │  │  │   │
   │  │  │  │  │   ├────────────────────────────────────┐
   │  │  │  │  │   │  ÜRÜN EXERGY (%30-50)              │
   │  │  │  │  │   │  (kimyasal ürün exergisi)          │
   │  │  │  │  │   └────────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma tersinmezliği | 14-20 | Kazan ve fırınlarda |
| Reaksiyon tersinmezliği | 8-15 | Kimyasal reaksiyonlar (entropi üretimi) |
| Isı transferi tersinmezliği | 8-14 | Eşanjörler, reaktör ceketleri |
| Distilasyon tersinmezliği | 5-10 | Reboiler + kondenser + tray kayıpları |
| Baca gazı ve atık ısı | 5-10 | Kazan, fırın, reaktör egzoz |
| Kompresör tersinmezliği | 3-6 | Proses gazı ve hava kompresörleri |
| Karışım tersinmezliği | 2-5 | Farklı sıcaklık/konsantrasyondaki akışlar |
| Soğutma sistemi kayıpları | 2-5 | Chiller, soğutma kulesi |
| Pompa ve motor kayıpları | 1-3 | Elektrik motorları |

### 4.3 Tipik Exergy Verimi

```
η_ex,kimya = Ex_ürün / Ex_giriş × 100

Tipik aralık: %30-50
Sektör ortalaması: %38
En iyi uygulama: %55-60

Alt sektör bazında:
  Petrokimya (büyük kompleks): %40-55
  Gübre (amonyak + üre):       %35-45
  Temel kimyasallar:           %35-50
  Özel kimyasallar:            %25-40
  İlaç:                        %20-35

Not: Kimyasal ürünlerin yüksek kimyasal exergy içeriği nedeniyle
ürün exergisi görece yüksektir, bu da sektörün exergy verimini artırır.
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Alt Proses Bazında

| Ürün/Proses | SEC | Birim | Kaynak |
|---|---|---|---|
| Amonyak (doğalgaz reforming) | 28-36 | GJ/ton NH₃ | EU BREF |
| Üre | 3.5-6.5 | GJ/ton üre | EU BREF |
| Etilen (steam cracking, nafta) | 14-20 | GJ/ton etilen | EU BREF |
| Polietilen (HDPE) | 2.5-5.0 | GJ/ton PE | IEA |
| PVC | 5.0-8.0 | GJ/ton PVC | IEA |
| Klor-alkali (membran) | 2,200-2,600 | kWh/ton Cl₂ | EU BREF |
| Soda ash (Solvay) | 8-12 | GJ/ton | EU BREF |
| Sülfürik asit | 0.5-1.5 | GJ/ton (net üretici) | EU BREF |
| Distilasyon (genel) | 0.3-2.0 | kWh/kg distilat | Tesis verisi |
| Kurutma (spray) | 3.5-6.0 | MJ/kg buharlaştırılan su | Endüstri |

### 5.2 Performans Sınıflandırması — Genel Kimya Tesisi

| Performans | SEC Konumu | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | < EU BAT alt sınır | >50 | Referans tesis, bilgi paylaşımı |
| İyi | EU BAT aralığında | 40-50 | İnce ayar, pinch güncellemesi |
| Ortalama | BAT üst sınır - ortalaması | 35-40 | Sistematik enerji yönetimi |
| Düşük | Sektör ortalaması +%20 | 25-35 | Ciddi iyileştirme programı |
| Kritik | Sektör ortalaması +%40 | <25 | Acil müdahale, kapsamlı audit |

### 5.3 EU BREF Karşılaştırması

| Parametre | Türkiye Ortalaması | EU BREF BAT | Fark |
|---|---|---|---|
| Amonyak SEC | 34-40 GJ/ton | 28-33 GJ/ton | %15-25 yüksek |
| Etilen SEC | 18-24 GJ/ton | 14-18 GJ/ton | %25-35 yüksek |
| Distilasyon enerji kullanımı | BAT ×1.3-1.8 | BAT değeri | %30-80 yüksek |
| Isı entegrasyon oranı | %30-50 | %60-80 | %20-30 fark |
| CHP penetrasyonu | %15-25 | %40-60 | %20-35 fark |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Brülör ayarı (O₂ trim) | 1-3 | 1,000-5,000 | <3 ay | Fazla hava optimizasyonu |
| Buhar kapanı bakımı | 2-4 | 2,000-8,000 | 2-6 ay | Tüm kapanların testi |
| İzolasyon iyileştirme | 1-3 | 5,000-15,000 | 3-8 ay | Reaktör, boru, vanalar |
| Basınçlı hava kaçak onarımı | 1-2 | 1,000-5,000 | <3 ay | Kaçak tespit ve onarım |
| Soğutma suyu sıcaklık optimizasyonu | 1-3 | 500-3,000 | <3 ay | Gereksiz soğutma azaltma |
| Distilasyon reflux oranı optimizasyonu | 2-5 | 0-2,000 | <1 ay | Enerji-ürün kalitesi dengesi |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Pinch analizi tabanlı ısı entegrasyonu | 10-25 | 50,000-200,000 | 1-3 yıl | En yüksek potansiyelli önlem |
| Ekonomizer eklenmesi | 3-5 | 15,000-40,000 | 1-2 yıl | Baca gazı → besleme suyu |
| VSD retrofit (pompa/kompresör) | 3-8 | 15,000-60,000 | 1-3 yıl | Değişken yük optimizasyonu |
| Ekzotermik reaksiyon ısı geri kazanımı | 5-15 | 30,000-100,000 | 1-3 yıl | Reaksiyon ısısı → buhar/ön ısıtma |
| Distilasyon kolon iyileştirme | 5-15 | 20,000-100,000 | 1-3 yıl | Tray/packing, feed preheating |
| Kondensat geri dönüş iyileştirme | 2-4 | 10,000-25,000 | 1-2 yıl | %50 → %80+ geri dönüş |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Kojenerasyon (CHP) | 15-25 | 300,000-1,000,000 | 3-5 yıl | Elektrik + proses buharı |
| Proses yoğunlaştırma (intensification) | 10-30 | 100,000-500,000 | 3-7 yıl | Reaktif distilasyon, mikro-reaktörler |
| Isı pompası entegrasyonu | 5-15 | 50,000-200,000 | 3-6 yıl | Düşük sıcaklık ısı yükseltme |
| Membran separasyon (distilasyon yerine) | 10-40 | 100,000-400,000 | 3-7 yıl | Termal ayırma → membran |
| Dijital ikiz / model prediktif kontrol | 3-8 | 80,000-250,000 | 3-5 yıl | Gerçek zamanlı optimizasyon |

### 6.4 Pinch Analizi Potansiyeli

```
Pinch analizi tasarruf tahmini:

Mevcut ısı entegrasyon oranı (Türkiye ortalaması): %30-50
Pinch analizi sonrası hedef:                       %60-80
Ek tasarruf potansiyeli:                           %10-25 toplam enerji

ΔT_min seçimi:
  - Gaz-gaz eşanjörler:    ΔT_min = 20-40°C
  - Gaz-sıvı eşanjörler:   ΔT_min = 15-25°C
  - Sıvı-sıvı eşanjörler:  ΔT_min = 10-15°C
  - Yoğuşma/buharlaşma:    ΔT_min = 3-8°C

Yatırım: Tipik olarak 50,000-200,000 € (retrofit eşanjör ağı)
Geri dönüş: 1-3 yıl
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 Isı Entegrasyonu

1. Kapsamlı pinch analizi uygulanması (en az 5 yılda bir güncelleme)
2. Sıcak ve soğuk akış eşleştirmelerinin sistematik optimize edilmesi
3. Ekzotermik reaksiyon ısısının düşük basınç buhar üretiminde kullanılması
4. Distilasyon kolonlarında besleme ön ısıtması (feed preheating)
5. Çoklu kolon sistemlerinde ısı kademesi (multi-effect) uygulanması

### 7.2 Distilasyon Optimizasyonu

1. Reflux oranının minimum düzeyde tutulması (ürün kalitesi izin verdiği ölçüde)
2. Besleme konum ve sıcaklık optimizasyonu
3. İleri proses kontrol (APC) ile optimum çalışma noktasının korunması
4. Vakum distilasyonunda düşük basınç ile sıcaklık azaltma
5. Isı pompalı distilasyon değerlendirmesi (yakın kaynar nokta sistemleri)

### 7.3 Reaksiyon Sistemi

1. Reaktör sıcaklık profilinin optimize edilmesi
2. Ekzotermik reaksiyon ısısının anlık geri kazanımı
3. Batch reaktör ısıtma/soğutma çevrimlerinin minimize edilmesi
4. Katalitik alternatiflerin değerlendirilmesi (düşük aktivasyon enerjisi)
5. Reaktif distilasyon fırsatlarının araştırılması

### 7.4 Yardımcı Sistemler

1. Buhar basıncı optimizasyonu (gereksiz yüksek basınçtan kaçınma)
2. Soğutma suyu sıcaklığının mevsimsel optimizasyonu
3. VSD uygulaması (pompalar, kompresörler, karıştırıcılar)
4. Basınçlı hava ve proses gazı kaçak yönetimi
5. Atık gaz yakma (flare) minimizasyonu

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: Kocaeli, Türkiye
Tesis tipi: Özel kimyasallar (reçine ve katkı maddeleri)
Kapasite: 45,000 ton/yıl
Çalışma: 7,500 saat/yıl, sürekli proses
Ekipman: 3 × 10 ton/h buhar kazanı (doğalgaz), 8 batch reaktör (5-15 m³),
         4 distilasyon kolonu, 2 spray kurutucu, 3 × 150 kW soğutma chiller,
         3 × 75 kW hava kompresörü
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Doğalgaz tüketimi | 5,200,000 | Nm³/yıl |
| Elektrik tüketimi | 8,500,000 | kWh/yıl |
| Toplam enerji (birincil) | 62,216,000 | kWh/yıl |
| Üretim miktarı | 45,000 | ton/yıl |
| SEC | 1,383 | kWh/ton ürün |
| Enerji maliyeti | 3,100,000 | €/yıl |
| Exergy verimi | %33.2 | — |
| Isı entegrasyon oranı | %35 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | Pinch analizi + ek 6 eşanjör kurulumu | 145,000 |
| 2 | Ekonomizer (3 kazan) | 48,000 |
| 3 | VSD retrofit (12 pompa + 2 kompresör) | 65,000 |
| 4 | Ekzotermik reaktör ısı geri kazanımı (3 reaktör) | 85,000 |
| 5 | Distilasyon besleme ön ısıtma (2 kolon) | 35,000 |
| 6 | Kondensat geri dönüş iyileştirme (%40 → %78) | 22,000 |
| 7 | İzolasyon iyileştirme (reaktörler, borular) | 18,000 |
| 8 | Basınçlı hava kaçak onarımı + VSD | 12,000 |
| **Toplam** | | **430,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| Doğalgaz tüketimi | 5,200,000 Nm³/yıl | 3,848,000 Nm³/yıl | 1,352,000 Nm³/yıl | -26.0 |
| Elektrik tüketimi | 8,500,000 kWh/yıl | 7,310,000 kWh/yıl | 1,190,000 kWh/yıl | -14.0 |
| Toplam enerji | 62,216,000 kWh/yıl | 47,079,000 kWh/yıl | 15,137,000 kWh/yıl | -24.3 |
| SEC | 1,383 kWh/ton | 1,046 kWh/ton | 337 kWh/ton | -24.3 |
| Enerji maliyeti | 3,100,000 €/yıl | 2,317,000 €/yıl | 783,000 €/yıl | -25.3 |
| Exergy verimi | %33.2 | %42.8 | +9.6 puan | +28.9 |
| Isı entegrasyon oranı | %35 | %68 | +33 puan | +94.3 |
| CO₂ emisyonu | 14,600 ton/yıl | 11,050 ton/yıl | 3,550 ton/yıl | -24.3 |

### 8.5 Ekonomik Analiz

```
Toplam yatırım:          430,000 €
Yıllık tasarruf:         783,000 €
Basit geri ödeme süresi: 430,000 / 783,000 = 0.55 yıl ≈ 7 ay
Net bugünkü değer (NPV): 4,820,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):    >%180

Tasarruf dağılımı:
  Doğalgaz: 1,352,000 Nm³ × €0.40/Nm³ = 540,800 €/yıl (%69)
  Elektrik: 1,190,000 kWh × €0.12/kWh = 142,800 €/yıl (%18)
  Bakım azalma + su:                   =  99,400 €/yıl (%13)
```

### 8.6 Öğrenilen Dersler

1. Pinch analizi tek başına toplam tasarrufun %45'ini sağladı; ancak gerçek potansiyelin ortaya çıkması detaylı mühendislik gerektirdi
2. Ekzotermik reaktörlerden ısı geri kazanımı operasyonel zorluklar içerdi; reaktör kontrol sistemi güncellemesi gerekti
3. Distilasyon kolon optimizasyonu ürün kalitesi riskini beraberinde getirdi; kademeli geçiş stratejisi uygulandı
4. VSD retrofit pompalarında %35-45 enerji tasarrufu elde edildi (özellikle sirkülasyon hatlarında)
5. Proses güvenliği (HAZOP) ile enerji verimliliği çalışmaları paralel yürütülmelidir

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 Pinch Analizi — Minimum Isıtma/Soğutma Gereksinimi

```
Kompozit eğri analizi:

Q_H,min = Minimum dış ısıtma gereksinimi [kW]
Q_C,min = Minimum dış soğutma gereksinimi [kW]

İlişki: Q_H,min - Q_C,min = Σ(H_sıcak) - Σ(H_soğuk) = sabit

Hesaplama örneği (basitleştirilmiş):
Sıcak akışlar: 3 adet → toplam soğutma ihtiyacı = 2,800 kW
Soğuk akışlar: 4 adet → toplam ısıtma ihtiyacı = 3,500 kW

Mevcut dış ısıtma: 2,200 kW, Mevcut dış soğutma: 1,500 kW
Pinch analizi sonrası:
  Q_H,min = 1,400 kW (dış ısıtma %36 azalma)
  Q_C,min = 700 kW (dış soğutma %53 azalma)

Tasarruf = (2,200 - 1,400) × 3,600 / (34,500 × 0.88) × 0.40 × 7,500
        = 328,000 €/yıl
```

### 9.2 Distilasyon Kolon Exergy Verimi

```
η_ex,distilasyon = Ex_ayırma / (Q_reboiler × (1 - T₀/T_reb) + W_pompa)

Burada:
- Ex_ayırma = ürünlerin karışım exergisindeki artış [kW]
- Q_reboiler = reboiler ısı yükü [kW]
- T_reb = reboiler sıcaklığı [K]
- W_pompa = pompa ve reflux drum gücü [kW]

Hesaplama örneği:
Q_reboiler = 500 kW, T_reb = 150°C = 423 K, T₀ = 298 K
Ex_ayırma = 45 kW, W_pompa = 8 kW

η_ex = 45 / (500 × (1 - 298/423) + 8)
     = 45 / (500 × 0.296 + 8)
     = 45 / 156 = %28.8

Tipik distilasyon exergy verimi: %5-40 (ayırma zorluğuna bağlı)
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Sistem Sınırları](system_boundaries.md) -- Ölçüm noktaları ve kontrol hacimleri
- [Metodoloji](methodology.md) -- Exergy analiz metodolojisi
- [Kazan Benchmarkları](../boiler/benchmarks.md) -- Kazan verimlilik karşılaştırma verileri
- [Kazan Formülleri](../boiler/formulas.md) -- Buhar sistemi exergy hesaplamaları
- [Ekonomizer](../boiler/solutions/economizer.md) -- Baca gazı ısı geri kazanımı
- [Kompresör Benchmarkları](../compressor/benchmarks.md) -- Basınçlı hava verimlilik verileri
- [Kompresör VSD](../compressor/solutions/vsd.md) -- Değişken hız sürücü uygulamaları
- [Pompa VSD](../pump/solutions/vsd.md) -- Pompa VSD uygulamaları
- [Chiller Benchmarkları](../chiller/benchmarks.md) -- Soğutma sistemi benchmark verileri
- [Tekstil Sektörü](sector_textile.md) -- Benzer ısıl proses gereksinimleri
- [Gıda Sektörü](sector_food.md) -- Benzer hijyen gereksinimleri (ilaç alt sektörü)

## Referanslar

- EU BREF, "Best Available Techniques (BAT) Reference Document for the Production of Large Volume Organic Chemicals," European Commission, 2017
- EU BREF, "Best Available Techniques Reference Document for the Manufacture of Large Volume Inorganic Chemicals," 2007
- EU BREF, "Energy Efficiency," European Commission, 2009
- IEA, "Energy Technology Perspectives — Chemical and Petrochemical Sector," 2022
- CEFIC, "European Chemical Industry Facts and Figures Report," 2023
- Dimian, A.C. et al., "Integrated Design and Simulation of Chemical Processes," Elsevier, 2nd Edition, 2014
- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1982
- Smith, R., "Chemical Process Design and Integration," Wiley, 2nd Edition, 2016
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Kimya Sektörü Enerji Verimliliği Potansiyeli," 2022
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
