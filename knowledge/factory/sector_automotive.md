---
title: "Otomotiv Sektörü Enerji Profili ve Optimizasyon (Automotive Sector Energy Profile)"
category: factory
equipment_type: factory
keywords: [otomotiv, sektör, fabrika, enerji]
related_files: [factory/factory_benchmarks.md, factory/cross_equipment.md, factory/heat_integration.md]
use_when: ["Otomotiv fabrikası analiz edilirken", "Otomotiv sektörü benchmarkları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Otomotiv Sektörü Enerji Profili ve Optimizasyon (Automotive Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Otomotiv sektörü, Türkiye'nin en büyük ihracat kalemlerinden biri olup yıllık 1.2-1.5 milyon araç üretim kapasitesine sahiptir. Sektörde boyahane (paint shop) toplam fabrika enerjisinin %50-70'ini tüketir ve enerji verimliliği çalışmalarının birincil hedefidir. Basınçlı hava tüketimi de kritik olup pres, kaynak ve montaj hatlarında yaygın kullanılmaktadır. Toplam enerji girdisinin %40-55'i termal (doğalgaz), %45-60'ı elektrik enerjisidir. Spesifik enerji tüketimi 800-2,500 kWh/araç arasında değişmekte olup karmaşıklığa ve üretim hacmine bağlıdır.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Toplam üretim kapasitesi: ~1.5 milyon araç/yıl
- Gerçek üretim: ~1.2-1.4 milyon araç/yıl
- İhracat: ~900,000-1,100,000 araç/yıl (toplam ihracatın %15-18'i)
- Tesis sayısı: 15 OEM üretici + ~4,000 tedarikçi
- İstihdam: ~200,000 doğrudan çalışan (OEM + tedarikçi)
- Enerji maliyetinin üretim maliyetindeki payı: %3-8
- Başlıca üretim merkezleri: Bursa, Kocaeli, Sakarya, Ankara, Aksaray

### 1.2 Üretim Prosesleri ve Enerji Yoğunlukları

| Proses | Enerji Yoğunluğu | Baskın Enerji Türü | Kritik Ekipman |
|---|---|---|---|
| Presleme (Stamping) | Düşük-Orta | Elektrik (%90-95) | Pres hatları, basınçlı hava |
| Kaynak/Gövde (Body/Welding) | Orta | Elektrik (%85-95) | Robot kaynak, basınçlı hava |
| Boyama (Paint Shop) | Çok Yüksek | Termal (%60-75) | Fırınlar, HVAC, RTO |
| Montaj (Assembly) | Düşük | Elektrik (%80-90) | Aletler, konveyör, test |
| Test (End of Line) | Düşük | Elektrik (%70-80) | Dinamometre, test sistemleri |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Doğalgaz | 40-55 | Boyahane fırınları, RTO, kazan, HVAC |
| Elektrik | 45-60 | Motorlar, robotlar, HVAC, aydınlatma, basınçlı hava |

### 2.2 Proses Bazlı Enerji Dağılımı (Tam Üretim Tesisi)

| Proses | Termal [%] | Elektrik [%] | Toplam Pay [%] |
|---|---|---|---|
| Boyahane (paint shop) — toplam | 35-50 | 15-25 | 50-70 |
|   — Boya fırınları | 15-22 | 0-2 | 14-18 |
|   — RTO/TAR (emisyon yakma) | 8-15 | 1-2 | 8-14 |
|   — Boya kabin HVAC | 8-14 | 8-14 | 15-25 |
|   — Ön işlem/e-kaplama | 5-8 | 3-5 | 6-10 |
| Kaynak/gövde (body shop) | 0-2 | 10-18 | 8-14 |
| Presleme (stamping) | 0 | 6-12 | 5-8 |
| Montaj (assembly) | 2-5 | 6-12 | 6-10 |
| Yardımcı sistemler | 3-5 | 5-8 | 6-10 |
|   — Basınçlı hava | 0 | 4-7 | 3-5 |
|   — Aydınlatma | 0 | 2-4 | 2-3 |
|   — Su arıtma/pompalama | 1-2 | 1-2 | 1-2 |

### 2.3 Boyahane Enerji Profili (Detay)

```
Tipik boyahane enerji dağılımı (araç başına):

Boya fırınları (curing ovens):
  E-coat fırını:          30-50 kWh/araç
  Primer fırını:          40-60 kWh/araç
  Topcoat fırını:         50-70 kWh/araç
  Clearcoat fırını:       40-60 kWh/araç

RTO/TAR (Regenerative Thermal Oxidizer):
  VOC yakma:              80-150 kWh/araç
  (Boya uygulama sırasında çözücü giderme)

HVAC (boya kabin klima):
  Sıcaklık kontrolü:      60-120 kWh/araç (22±2°C, %55-65 RH)
  Filtreleme:              15-30 kWh/araç
  Hava dağıtımı (fanlar): 30-60 kWh/araç

Ön işlem:
  Fosfatlama/yıkama:       20-40 kWh/araç
  E-kaplama (elektroliz):  15-30 kWh/araç

Toplam boyahane:           380-670 kWh/araç
Tesis toplamının:          %50-70'i
```

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 OEM Otomotiv Tesisi (Kapasite ~200,000 araç/yıl)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Boya fırını (konveyörlü) | 1-3 MW/fırın | 4-6 | 15-20 | Doğalgaz |
| RTO (Regenerative Thermal Oxidizer) | 2-5 MW | 1-3 | 8-14 | Doğalgaz |
| HVAC (boya kabin) | 2-8 MW termal + 1-3 MW_e | 4-8 | 15-25 | Doğalgaz + Elektrik |
| Buhar/sıcak su kazanı | 10-20 MW | 2-4 | 8-12 | Doğalgaz |
| Chiller (boya kabin soğutma) | 1-4 MW soğutma | 2-4 | 3-5 | Elektrik |
| Kaynak robotları | 5-15 kW/robot | 200-500 | 8-14 | Elektrik |
| Pres hattı | 2,000-5,000 ton | 3-6 | 5-8 | Elektrik |
| Basınçlı hava kompresörü | 100-250 kW | 5-10 | 4-6 | Elektrik |
| Konveyör sistemleri | 10-50 kW/hat | 20-40 | 2-4 | Elektrik |
| Aydınlatma | - | - | 2-4 | Elektrik |
| Su arıtma (DI water, atık su) | - | - | 1-2 | Elektrik |

### 3.2 Ekipman Referansları

- Kazan sistemleri: bkz. `../boiler/equipment/systems_overview.md`
- Soğutma sistemleri: bkz. `../chiller/equipment/systems_overview.md`
- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`
- Pompa sistemleri: bkz. `../pump/equipment/systems_overview.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik Otomotiv Tesisi)

```
DOĞALGAZ EXERGY (%48)  ─────────────────────────────┐
                                                      │
ELEKTRİK EXERGY (%52)  ────────────────────────────┐│
                                                    ││
                   ┌────────────────────────────────┴┤
                   │     TOPLAM EXERGY GİRİŞİ        │
                   │        (100%)                    │
                   ├──────────────────────────────────┘
                   │
   ┌───────────────┤ Yanma tersinmezliği (%14-20) ──────→ YIKIM
   │               │
   │  ┌────────────┤ HVAC tersinmezliği (%10-16) ──────→ YIKIM
   │  │            │
   │  │  ┌─────────┤ Fırın ısı transferi (%6-10) ─────→ YIKIM
   │  │  │         │
   │  │  │  ┌──────┤ RTO egzoz/baca gazı (%5-10) ─────→ ATIK
   │  │  │  │      │
   │  │  │  │  ┌───┤ Motor/robot tersinmezliği (%5-8) ─→ YIKIM
   │  │  │  │  │   │
   │  │  │  │  │   │ Basınçlı hava kayıpları (%3-5) ──→ YIKIM
   │  │  │  │  │   │ Boya kabin egzoz (%3-5) ─────────→ ATIK
   │  │  │  │  │   │ Soğutma atık ısısı (%2-4) ──────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   ├───────────────────────────────────┐
   │  │  │  │  │   │  ÜRÜN EXERGY (%20-30)             │
   │  │  │  │  │   │  (boyalı/montajlı araç gövdesi)   │
   │  │  │  │  │   └───────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma tersinmezliği | 14-20 | Fırın, RTO, kazan yanma odaları |
| HVAC tersinmezliği | 10-16 | Boya kabin klima (sıcaklık+nem kontrol) |
| Fırın ısı transferi | 6-10 | Boya fırınlarında ürün/hava ısıtma |
| RTO/baca gazı exergisi | 5-10 | RTO egzoz 250-350°C, kazan baca gazı |
| Motor ve robot tersinmezliği | 5-8 | Kaynak robotları, presler, konveyörler |
| Basınçlı hava kayıpları | 3-5 | Kaçaklar, kısma, basınç düşüşü |
| Boya kabin egzoz | 3-5 | Filtrelenmiş sıcak hava deşarjı |
| Soğutma atık ısısı | 2-4 | Chiller kondenser atık ısısı |
| Aydınlatma ısı dönüşümü | 1-2 | Aydınlatma → ısıya dönüşüm |

### 4.3 Tipik Exergy Verimi

```
η_ex,otomotiv = Ex_ürün / Ex_giriş × 100

Tipik aralık: %20-30
Sektör ortalaması: %25
En iyi uygulama: %36-38

Alt proses exergy verimleri:
  Presleme:         %12-20 (elektrik → mekanik şekillendirme)
  Kaynak/gövde:     %8-15 (elektrik → ısı → kaynak)
  Boyahane:         %10-18 (toplam boyahane)
    Fırınlar:       %15-25
    HVAC:           %5-12
    RTO:            %20-35 (ısı geri kazanımla)
  Montaj:           %15-25

Not: Boya kabini HVAC sistemi en düşük exergy verimli alt sistemdir.
Büyük hacimli havanın hassas sıcaklık/nem kontrolü yüksek kaliteli
enerjinin düşük kaliteli amaç için kullanılması demektir.
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Araç Bazında

| Tesis Tipi | SEC Termal [kWh/araç] | SEC Elektrik [kWh/araç] | SEC Toplam [kWh/araç] |
|---|---|---|---|
| Binek araç (tam fabrika) | 400-900 | 500-1,200 | 900-2,000 |
| Hafif ticari araç | 500-1,100 | 600-1,400 | 1,100-2,500 |
| Sadece boyahane | 250-500 | 200-400 | 450-850 |
| Sadece kaynak/gövde | 10-30 | 200-400 | 220-430 |
| Sadece montaj | 20-50 | 100-250 | 130-300 |
| Sadece presleme | 5-15 | 100-250 | 110-260 |

### 5.2 Performans Sınıflandırması — Tam Üretim Tesisi

| Performans | SEC [kWh/araç] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | <900 | >34 | Referans tesis, yeni nesil boyahane |
| İyi | 900-1,200 | 28-34 | İnce ayar optimizasyonu |
| Ortalama | 1,200-1,600 | 22-28 | Sistematik enerji yönetimi |
| Düşük | 1,600-2,200 | 16-22 | Ciddi iyileştirme programı |
| Kritik | >2,200 | <16 | Acil müdahale, kapsamlı audit |

### 5.3 EU Karşılaştırması ve Endüstri Liderleri

| Parametre | Türkiye Ortalaması | Avrupa En İyi | Fark |
|---|---|---|---|
| SEC toplam | 1,400-1,800 kWh/araç | 750-1,100 kWh/araç | %30-50 yüksek |
| Boyahane SEC | 550-750 kWh/araç | 350-500 kWh/araç | %30-50 yüksek |
| Basınçlı hava SEC | 60-100 kWh/araç | 30-55 kWh/araç | %50-80 yüksek |
| RTO ısı geri kazanım oranı | %85-90 | %95-97 | %5-10 fark |
| Boyahane HVAC resirkülasyon | %60-75 | %80-95 | %15-25 fark |
| Boya kabin VOC içeriği | Solvent bazlı | Su bazlı/toz boya | — |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Basınçlı hava kaçak onarımı | 2-5 | 5,000-20,000 | <3 ay | Sistematik kaçak programı |
| Robot standby yönetimi | 1-3 | 5,000-15,000 | 3-6 ay | Boşta robotları uyku moduna |
| Aydınlatma LED dönüşümü | 1-3 | 20,000-80,000 | 6-12 ay | Büyük tesis alanlarında |
| Fırın izolasyon iyileştirme | 1-2 | 10,000-30,000 | 3-8 ay | Boya fırını kapı sızdırmazlığı |
| HVAC çalışma saati optimizasyonu | 1-3 | 2,000-10,000 | <3 ay | Üretim dışı saatlerde azaltma |
| Buhar kapanı bakımı | 1-2 | 3,000-10,000 | 2-6 ay | Boyahane buhar sistemi |
| Soğutma sistemi temizlik/bakım | 1-2 | 2,000-8,000 | 2-4 ay | Chiller kondenser temizliği |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| RTO ısı geri kazanım iyileştirme | 3-8 | 50,000-200,000 | 1-2 yıl | %90 → %95+ geri kazanım |
| Boya kabin hava resirkülasyonu artırma | 5-12 | 100,000-400,000 | 1-3 yıl | %65 → %85 resirkülasyon |
| VSD (HVAC fanları, pompalar) | 3-6 | 30,000-120,000 | 1-3 yıl | Değişken yük optimizasyonu |
| Boyahane egzoz ısı geri kazanımı | 3-8 | 80,000-250,000 | 2-3 yıl | Fırın/RTO egzoz → ön ısıtma |
| Basınçlı hava sistemi yenileme (VSD) | 2-4 | 50,000-150,000 | 1-3 yıl | VSD kompresör + basınç optimize |
| Chiller serbest soğutma (free cooling) | 2-4 | 30,000-100,000 | 1-3 yıl | Kış aylarında chiller bypass |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Su bazlı / toz boya teknolojisi | 15-30 | 2,000,000-10,000,000 | 5-10 yıl | RTO ihtiyacı %60-90 azalma |
| Yeni nesil boyahane (compact) | 20-40 | 5,000,000-20,000,000 | 5-10 yıl | Daha az katman, düşük VOC |
| CHP entegrasyonu | 10-20 | 500,000-2,000,000 | 3-6 yıl | Boyahane ısı + elektrik |
| Dijital ikiz / AI HVAC kontrolü | 3-8 | 100,000-400,000 | 3-5 yıl | Gerçek zamanlı optimizasyon |
| Güneş enerjisi (PV) | 3-8 | 200,000-1,000,000 | 5-8 yıl | Geniş çatı/park alanı |
| Isı pompası (boyahane HVAC) | 5-12 | 200,000-800,000 | 3-6 yıl | Atık ısı → HVAC ön ısıtma |

### 6.4 Toplam Tasarruf Potansiyeli

```
Otomotiv tesisi tipik tasarruf potansiyeli:

Hızlı kazanımlar:         %8-18
Orta vadeli projeler:     %12-28
Stratejik projeler:       %20-45

Gerçekçi toplam tasarruf: %25-45
Tipik yatırım geri dönüşü (toplam paket): 2-4 yıl

Boyahane odaklı tasarruf:
  Boyahane tek başına toplam tasarrufun %60-75'ini oluşturur.
  Boyahane SEC hedefi: <450 kWh/araç (mevcut dünyada en iyi)
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 Boyahane Enerji Yönetimi

1. Boya kabin hava resirkülasyon oranı >%80 (aktif karbon filtreleme ile)
2. RTO termal geri kazanım oranı >%95
3. Fırın izolasyon ve sızdırmazlık kontrolü (termal kamera ile yıllık)
4. Su bazlı boya teknolojisine geçiş (VOC ve enerji azaltma)
5. Boya kabin sıcaklık/nem bant genişletme (kalite izin verdiği ölçüde)
6. E-coat banyosu sıcaklık kontrolü ve ısı geri kazanımı
7. Üretim dışı saatlerde boyahane HVAC setback (düşük mod)

### 7.2 Basınçlı Hava Yönetimi

1. Merkezi kaçak tespit ve onarım programı (aylık denetim)
2. VSD kompresör kullanımı (baz yük + trim kontrol stratejisi)
3. Basınçlı hava yerine alternatif: elektrikli aletler, blower (düşük basınç)
4. Sistem basıncı optimizasyonu (her 1 bar azalma ≈ %7 tasarruf)
5. Soğutucu/kurutucu enerji tüketiminin optimize edilmesi

### 7.3 Kaynak ve Gövde

1. Robot standby/uyku modu programlaması (enerji tüketimi %50-70 azalma)
2. Kaynak transformatör verimlilik iyileştirme (yeni nesil MFDC)
3. Pnömatik tutuculardan elektrikli tutucalara geçiş (basınçlı hava azaltma)
4. Aydınlatma zoning (üretim alanı bazlı aydınlatma kontrolü)

### 7.4 Genel Tesis

1. ISO 50001 enerji yönetim sistemi uygulanması
2. Alt ölçüm sistemi (her departman/hat bazlı enerji izleme)
3. Araç başına SEC (kWh/araç) günlük takibi
4. Enerji yöneticisi ve departman enerji şampiyonları atanması
5. Yıllık enerji hedefi belirleme ve performans takibi

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: Bursa, Türkiye
Tesis tipi: Binek otomobil üretimi (tam fabrika)
Kapasite: 180,000 araç/yıl
Çalışma: 4,800 saat/yıl (2 vardiya), 250 iş günü/yıl
Prosesler: Presleme, kaynak/gövde, boyama (solvent bazlı),
           montaj, son test
Ekipman: 5 boya fırını, 2 RTO, 6 boya kabini (HVAC), 3 × 15 MW kazan,
         2 × 1.5 MW chiller, 8 × 150 kW hava kompresörü,
         350+ kaynak robotu
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Doğalgaz tüketimi | 18,000,000 | Nm³/yıl |
| Elektrik tüketimi | 75,000,000 | kWh/yıl |
| Toplam enerji (birincil) | 261,000,000 | kWh/yıl |
| Araç üretimi | 175,000 | araç/yıl |
| SEC toplam | 1,491 | kWh/araç |
| SEC boyahane | 620 | kWh/araç |
| Basınçlı hava SEC | 85 | kWh/araç |
| Enerji maliyeti | 16,200,000 | €/yıl |
| Exergy verimi | %23.5 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | Boya kabin hava resirkülasyonu artırma (%65→%82) | 350,000 |
| 2 | RTO ısı geri kazanım iyileştirme (%87→%95) | 180,000 |
| 3 | Boyahane fırın egzoz ısı geri kazanımı | 120,000 |
| 4 | VSD (HVAC fanları 12 adet + pompa 8 adet) | 95,000 |
| 5 | Basınçlı hava: VSD kompresör + kaçak programı | 85,000 |
| 6 | Robot standby yönetim sistemi (350 robot) | 45,000 |
| 7 | LED aydınlatma dönüşümü (tüm fabrika) | 180,000 |
| 8 | Free cooling chiller sistemi | 65,000 |
| 9 | Fırın izolasyon ve sızdırmazlık iyileştirme | 35,000 |
| 10 | HVAC üretim dışı setback kontrolü | 25,000 |
| **Toplam** | | **1,180,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| Doğalgaz tüketimi | 18,000,000 Nm³/yıl | 14,040,000 Nm³/yıl | 3,960,000 Nm³/yıl | -22.0 |
| Elektrik tüketimi | 75,000,000 kWh/yıl | 61,500,000 kWh/yıl | 13,500,000 kWh/yıl | -18.0 |
| Toplam enerji | 261,000,000 kWh/yıl | 206,500,000 kWh/yıl | 54,500,000 kWh/yıl | -20.9 |
| SEC toplam | 1,491 kWh/araç | 1,180 kWh/araç | 311 kWh/araç | -20.9 |
| SEC boyahane | 620 kWh/araç | 468 kWh/araç | 152 kWh/araç | -24.5 |
| Basınçlı hava SEC | 85 kWh/araç | 58 kWh/araç | 27 kWh/araç | -31.8 |
| Enerji maliyeti | 16,200,000 €/yıl | 12,620,000 €/yıl | 3,580,000 €/yıl | -22.1 |
| Exergy verimi | %23.5 | %30.2 | +6.7 puan | +28.5 |
| CO₂ emisyonu | 56,300 ton/yıl | 43,900 ton/yıl | 12,400 ton/yıl | -22.0 |

### 8.5 Ekonomik Analiz

```
Toplam yatırım:          1,180,000 €
Yıllık tasarruf:         3,580,000 €
Basit geri ödeme süresi: 1,180,000 / 3,580,000 = 0.33 yıl ≈ 4 ay
Net bugünkü değer (NPV): 22,840,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):    >%300

Tasarruf dağılımı:
  Doğalgaz: 3,960,000 Nm³ × €0.40/Nm³   = 1,584,000 €/yıl (%44)
  Elektrik: 13,500,000 kWh × €0.12/kWh   = 1,620,000 €/yıl (%45)
  Bakım ve operasyonel:                   =   376,000 €/yıl (%11)
```

### 8.6 Öğrenilen Dersler

1. Boya kabin resirkülasyon artışı en yüksek boyahane tasarrufunu sağladı (%35 toplam boyahane tasarrufunun)
2. RTO ısı geri kazanım iyileştirmesi beklenen %5 yerine %8 doğalgaz tasarrufu sağladı
3. Robot standby yönetimi yatırım/getiri oranı en yüksek önlemdi (45,000 € yatırım → 180,000 €/yıl tasarruf)
4. Basınçlı hava kaçak oranı %30'dan %12'ye düşürüldü; düzenli takip programı kuruldu
5. LED aydınlatma hem elektrik hem de soğutma yükü azaltma ile çift etki sağladı

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 Boya Kabin HVAC Enerji Tüketimi

```
Q_HVAC = ṁ_hava × (h_istenilen - h_ortam) + Q_proses

Burada:
- ṁ_hava = kabin hava debisi [kg/s]
- h_istenilen = istenen hava entalpisi (22°C, %60 RH) [kJ/kg]
- h_ortam = ortam havası entalpisi [kJ/kg]
- Q_proses = proses ısı yükleri (boya kurutma, aydınlatma) [kW]

Resirkülasyon etkisi:
ṁ_taze = ṁ_toplam × (1 - f_resirkülasyon)
Q_HVAC,yeni = ṁ_taze × (h_istenilen - h_ortam) + Q_proses

Hesaplama örneği:
ṁ_toplam = 50 kg/s, h_istenilen = 47 kJ/kg (22°C, %60 RH)
h_ortam = 35 kJ/kg (kış, 5°C, %70 RH), Q_proses = 100 kW

f_resirkülasyon = 0.65 (mevcut):
Q_HVAC = 50 × (1-0.65) × (47-35) + 100 = 17.5 × 12 + 100 = 310 kW

f_resirkülasyon = 0.85 (iyileştirilmiş):
Q_HVAC = 50 × (1-0.85) × (47-35) + 100 = 7.5 × 12 + 100 = 190 kW

Tasarruf = 310 - 190 = 120 kW (%39 HVAC tasarrufu)
```

### 9.2 RTO Enerji Dengesi

```
Q_RTO,yakıt = Q_VOC_yanma + Q_taze_hava_ısıtma - Q_geri_kazanım

Burada:
- Q_VOC_yanma = VOC yanma enerjisi [kW] (genellikle küçük)
- Q_taze_hava_ısıtma = taze havayı yanma sıcaklığına ısıtma [kW]
- Q_geri_kazanım = rejeneratif seramik yatak geri kazanımı [kW]

RTO termal verim (geri kazanım oranı):
η_RTO = Q_geri_kazanım / Q_taze_hava_ısıtma × 100

Hesaplama örneği:
ṁ_hava = 30,000 Nm³/h = 10.8 kg/s, T_yanma = 800°C, T_ortam = 20°C
Cp = 1.05 kJ/(kg·K)

Q_taze_hava_ısıtma = 10.8 × 1.05 × (800-20) = 8,845 kW

η_RTO = %90 (mevcut):
Q_geri_kazanım = 8,845 × 0.90 = 7,961 kW
Q_RTO,yakıt = 8,845 - 7,961 = 884 kW

η_RTO = %95 (iyileştirilmiş):
Q_geri_kazanım = 8,845 × 0.95 = 8,403 kW
Q_RTO,yakıt = 8,845 - 8,403 = 442 kW

Tasarruf = 884 - 442 = 442 kW (%50 yakıt azalma)
Yıllık = 442 × 3.6 × 4,800 / 34,500 × 0.40 = 88,600 €/yıl
```

### Isı Eşanjörü Uygulamaları (Heat Exchanger Applications)

Otomotiv sektöründe ısı eşanjörleri üretim süreçlerinin kritik bileşenleridir:

| Eşanjör Uygulaması | Proses | Tipik Tip | Referans Dosya |
|---------------------|--------|-----------|----------------|
| Boya kabini hava ısıtma | Boya kurutma/pişirme | Gaz-gaz reküperatör | `../../heat_exchanger/equipment/recuperator.md` |
| Proses soğutma suyu | CNC, kaynak, döküm soğutma | Plakalı eşanjör | `../../heat_exchanger/equipment/plate.md` |
| Kompresör ara soğutma | Basınçlı hava sistemi | Hava soğutmalı HX | `../../heat_exchanger/equipment/air_cooled.md` |
| Baca gazı ısı geri kazanım | Fırın/kazan egzozu | Ekonomizer | `../../heat_exchanger/equipment/economizer.md` |
| Hidrolik yağ soğutma | Pres, enjeksiyon | Gövde-boru HX | `../../heat_exchanger/equipment/shell_and_tube.md` |

**Exergy optimizasyon fırsatları:**
- Boya fırını egzoz ısısı geri kazanımı → taze hava ön ısıtma (%20-35 tasarruf)
- Proses soğutma suyu ısısı → kış ısıtma veya kazan besleme suyu ön ısıtma
- Kompresör atık ısısı → eşanjör → bina ısıtma: `../../heat_exchanger/solutions/heat_recovery.md`
- Eşanjör kirlenme yönetimi (cutting oil kontaminasyonu): `../../heat_exchanger/solutions/fouling_management.md`

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Enerji Yönetimi](energy_management.md) -- ISO 50001 uygulama rehberi
- [Sistem Sınırları](system_boundaries.md) -- Ölçüm noktaları ve kontrol hacimleri
- [Kazan Benchmarkları](../boiler/benchmarks.md) -- Kazan verimlilik karşılaştırma verileri
- [Chiller Benchmarkları](../chiller/benchmarks.md) -- Soğutma sistemi benchmark verileri
- [Serbest Soğutma](../chiller/solutions/free_cooling.md) -- Free cooling uygulamaları
- [Chiller VSD](../chiller/solutions/vsd.md) -- Soğutma kompresörü VSD uygulamaları
- [Kompresör Benchmarkları](../compressor/benchmarks.md) -- Basınçlı hava verimlilik verileri
- [Hava Kaçakları](../compressor/solutions/air_leaks.md) -- Basınçlı hava kaçak yönetimi
- [Kompresör VSD](../compressor/solutions/vsd.md) -- Değişken hız sürücü uygulamaları
- [Kompresör Isı Geri Kazanım](../compressor/solutions/heat_recovery.md) -- Atık ısı değerlendirme
- [Metal İşleme Sektörü](sector_metal.md) -- Otomotiv tedarik zinciri
- [Kimya Sektörü](sector_chemical.md) -- Boya/kaplama kimyasalları

## Referanslar

- Volkswagen AG, "Environmental Report — Energy and CO₂ Reduction in Manufacturing," 2023
- BMW Group, "Sustainability Report — Production Resource Efficiency," 2023
- ACEA, "European Automobile Manufacturers' Association — Environmental Report," 2023
- US DOE, "Improving Compressed Air System Performance — A Sourcebook for Industry," 2003
- Carbon Trust, "Automotive Manufacturing — Industrial Energy Efficiency," CTG072
- Galitsky, C. & Worrell, E. (2008), "Energy Efficiency Improvement and Cost Saving Opportunities for the Vehicle Assembly Industry," LBNL
- Giampieri, A. et al. (2020), "A review of the current automotive manufacturing practice from an energy perspective," Applied Energy, 261, 114074
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Otomotiv Sektörü Enerji Verimliliği Potansiyeli," 2022
- OSD (Otomotiv Sanayii Derneği), "Otomotiv Sanayii Genel ve İstatistik Bülteni," 2024
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
