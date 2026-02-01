---
title: "Metal İşleme Sektörü Enerji Profili ve Optimizasyon (Metal Processing Sector Energy Profile)"
category: factory
equipment_type: factory
keywords: [metal, sektör, ergitme, enerji]
related_files: [factory/factory_benchmarks.md, factory/waste_heat_recovery.md, factory/heat_integration.md]
use_when: ["Metal fabrikası analiz edilirken", "Metal sektörü benchmarkları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Metal İşleme Sektörü Enerji Profili ve Optimizasyon (Metal Processing Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Metal işleme sektörü, Türkiye'nin en enerji yoğun sanayi kollarından biridir. Türkiye dünyada ham çelik üretiminde ilk 8 içinde yer almakta olup yıllık 35-40 milyon ton çelik üretmektedir. Sektörde Elektrik Ark Ocağı (EAF) çelik üretimi baskın olup toplam çelik üretiminin %70'inden fazlasını oluşturur. Fırın bazlı prosesler (ergitme, ısıl işlem, dövme) enerji tüketiminin ana bileşenidir. Toplam enerji girdisinin %50-70'i elektrik (EAF tesisleri için), %30-50'si termal (doğalgaz) enerjidir. Exergy verimi alt sektöre göre %25-40 aralığında değişir.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Çelik üretimi: ~35-40 milyon ton/yıl (dünya sıralamasında 7-8.)
- Alüminyum üretimi: ~0.3-0.4 milyon ton/yıl (birincil + ikincil)
- Toplam tesis sayısı: ~25,000 (çelik, döküm, dövme, talaşlı imalat dahil)
- İstihdam: ~400,000 doğrudan çalışan
- Enerji maliyetinin üretim maliyetindeki payı: %20-40 (çelik), %30-50 (alüminyum)
- Başlıca üretim merkezleri: İskenderun, İstanbul, İzmit, Karabük, Aliağa

### 1.2 Alt Sektörler ve Enerji Yoğunlukları

| Alt Sektör | Enerji Yoğunluğu | Baskın Enerji Türü | Kritik Proses |
|---|---|---|---|
| Çelik (EAF) | Çok Yüksek | Elektrik (%70-85) | Elektrik ark ergitme |
| Çelik (BOF/Entegre) | Çok Yüksek | Termal (%80-90) | Yüksek fırın, kok |
| Alüminyum (birincil) | Aşırı Yüksek | Elektrik (%90) | Elektroliz (Hall-Heroult) |
| Alüminyum (ikincil/geri dönüşüm) | Yüksek | Termal (%60-70) | Ergitme fırını |
| Döküm (Foundry) | Yüksek | Elektrik + termal | İndüksiyon/kupol fırını |
| Dövme (Forging) | Yüksek | Termal (%70-80) | Isıtma fırını, pres |
| Talaşlı imalat (Machining) | Orta | Elektrik (%85-95) | CNC, tezgahlar |
| Isıl işlem (Heat treatment) | Yüksek | Termal (%70-85) | Sertleştirme, temperlenme |
| Yüzey işlem (Surface treatment) | Orta | Termal + elektrik | Galvanizleme, kaplama |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı — EAF Çelik Tesisi

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Elektrik | 60-75 | EAF, haddeleme motorları, basınçlı hava |
| Doğalgaz | 20-35 | Tav fırını, ısıl işlem, kazan |
| Kimyasal enerji (kömür/O₂) | 5-10 | EAF'da enjeksiyon (köpük cüruf) |
| Oksijen | 2-5 | EAF oksijen üflemesi |

### 2.2 Proses Bazlı Enerji Dağılımı (EAF Çelik Tesisi)

| Proses | Elektrik [%] | Termal [%] | Toplam Pay [%] |
|---|---|---|---|
| EAF (ergitme) | 55-65 | 0 | 45-55 |
| Haddeleme (sıcak) | 5-10 | 15-25 | 15-22 |
| Tav/ısıl işlem fırınları | 1-3 | 10-18 | 8-15 |
| Basınçlı hava | 3-5 | 0 | 3-5 |
| Su soğutma sistemi | 3-5 | 0 | 3-5 |
| Toz toplama/baca gazı arıtma | 2-4 | 0 | 2-4 |
| Aydınlatma ve yardımcı | 2-3 | 0 | 2-3 |
| Vinç ve malzeme taşıma | 2-3 | 0 | 2-3 |

### 2.3 EAF Enerji Dengesi

```
Tipik EAF enerji girdisi (1 ton sıvı çelik):

Elektrik enerjisi:       350-450 kWh/ton  (%55-65)
Kimyasal enerji:
  Oksijen üflemesi:       80-120 kWh/ton  (%12-18)
  Kömür enjeksiyonu:       60-100 kWh/ton  (%10-15)
  Doğalgaz brülör:         30-60 kWh/ton   (%5-9)
  Ekzotermik reaksiyonlar: 30-50 kWh/ton   (%5-8)
─────────────────────────────────────────
Toplam giriş:             550-780 kWh/ton  (%100)

Enerji çıkışları:
  Sıvı çelik entalpisi:  370-420 kWh/ton  (%55-60)
  Baca gazı (sıcak):      90-140 kWh/ton  (%15-20)
  Cüruf entalpisi:         40-70 kWh/ton   (%7-10)
  Soğutma suyu kaybı:      30-60 kWh/ton   (%5-8)
  Yüzey kayıpları:         20-40 kWh/ton   (%3-5)
  Diğer kayıplar:          20-50 kWh/ton   (%3-7)
```

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 EAF Çelik Tesisi (Kapasite ~1 milyon ton/yıl)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Elektrik Ark Ocağı (EAF) | 100-150 ton/döküm | 1-2 | 45-55 | Elektrik |
| Pota Fırını (LF) | 100-150 ton | 1-2 | 5-8 | Elektrik |
| Sıcak haddeleme hattı | 150-300 ton/h | 1 | 12-18 | Doğalgaz + Elektrik |
| Tav fırını | 100-300 ton/h | 1-2 | 8-12 | Doğalgaz |
| Basınçlı hava kompresörü | 150-500 kW | 3-5 | 3-5 | Elektrik |
| Su soğutma sistemi | 5,000-15,000 kW | 1 | 3-5 | Elektrik |
| Oksijen tesisi (ASU) | 1,000-5,000 Nm³/h O₂ | 1 | 3-5 | Elektrik |
| Toz toplama (bag filter) | 500,000-1,500,000 m³/h | 1 | 2-4 | Elektrik |
| Vinç ve taşıma | 20-100 ton | 5-10 | 2-3 | Elektrik |

### 3.2 Ekipman Referansları

- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`
- Pompa sistemleri: bkz. `../pump/equipment/systems_overview.md`
- Kazan sistemleri: bkz. `../boiler/equipment/systems_overview.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik EAF Çelik Tesisi)

```
ELEKTRİK EXERGY (%65)  ────────────────────────────┐
                                                     │
DOĞALGAZ EXERGY (%25)  ───────────────────────────┐│
                                                   ││
KİMYASAL ENERJI (%10)  ────────────────────────┐  ││
                                                │  ││
                   ┌────────────────────────────┴──┴┤
                   │     TOPLAM EXERGY GİRİŞİ       │
                   │        (100%)                   │
                   ├─────────────────────────────────┘
                   │
   ┌───────────────┤ EAF tersinmezliği (%20-28) ───────→ YIKIM
   │               │
   │  ┌────────────┤ Baca gazı exergisi (%8-14) ───────→ ATIK
   │  │            │
   │  │  ┌─────────┤ Fırın tersinmezliği (%6-12) ─────→ YIKIM
   │  │  │         │
   │  │  │  ┌──────┤ Cüruf exergisi (%4-7) ────────────→ ATIK
   │  │  │  │      │
   │  │  │  │  ┌───┤ Soğutma suyu kaybı (%3-6) ───────→ ATIK
   │  │  │  │  │   │
   │  │  │  │  │   │ Motor/yardımcı kayıplar (%3-5) ──→ YIKIM
   │  │  │  │  │   │
   │  │  │  │  │   ├───────────────────────────────────┐
   │  │  │  │  │   │  ÜRÜN EXERGY (%25-40)             │
   │  │  │  │  │   │  (çelik ürün exergisi)            │
   │  │  │  │  │   └───────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| EAF tersinmezliği | 20-28 | Ark plazma, kimyasal reaksiyonlar |
| Baca gazı exergisi | 8-14 | 1,200-1,600°C → filtre sonrası 200-300°C |
| Fırın tersinmezliği | 6-12 | Tav/ısıl işlem fırınlarında yanma + ısı transferi |
| Cüruf exergisi | 4-7 | 1,500-1,650°C sıvı cüruf |
| Soğutma suyu kaybı | 3-6 | EAF panel, fırın soğutma |
| Motor ve yardımcı kayıplar | 3-5 | Haddeleme motorları, pompalar |
| Yüzey radyasyon kayıpları | 2-4 | Fırın ve EAF dış yüzeyleri |
| Basınçlı hava kayıpları | 1-3 | Kaçaklar, basınç düşüşü |

### 4.3 Tipik Exergy Verimi

```
η_ex,metal = Ex_ürün / Ex_giriş × 100

Alt sektör bazında:
  Çelik (EAF):               %28-38
  Çelik (Entegre BOF):       %30-42
  Alüminyum (birincil):      %12-20
  Alüminyum (ikincil):       %20-30
  Döküm (indüksiyon):        %22-32
  Dövme:                     %18-28
  Isıl işlem:                %15-25
  Talaşlı imalat:            %8-15

Sektör ortalaması: %30 (çelik ağırlıklı)
En iyi uygulama: %45-50

Not: Elektrik ark prosesinde elektriğin (saf exergy) doğrudan
ısıya dönüştürülmesi yüksek tersinmezlik yaratır.
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Alt Sektör Bazında

| Ürün/Proses | SEC | Birim | Kaynak |
|---|---|---|---|
| Çelik (EAF → kütük) | 400-550 | kWh/ton sıvı çelik | Worldsteel |
| Çelik (EAF → nihai ürün) | 500-700 | kWh/ton çelik | Worldsteel |
| Çelik (Entegre BOF, toplam) | 4,500-6,500 | MJ/ton çelik | Worldsteel |
| Alüminyum (birincil, elektroliz) | 13,000-16,000 | kWh/ton Al | IAI |
| Alüminyum (ikincil, ergitme) | 500-1,000 | kWh/ton Al | IAI |
| Döküm (demir, indüksiyon) | 550-800 | kWh/ton döküm | AFS |
| Döküm (demir, kupol) | 800-1,200 | kWh/ton döküm | AFS |
| Dövme (çelik) | 300-600 | kWh/ton (ısıtma) | Endüstri |
| Isıl işlem (sertleştirme) | 200-500 | kWh/ton | Endüstri |
| Galvanizleme (sıcak daldırma) | 150-350 | kWh/ton | Endüstri |

### 5.2 Performans Sınıflandırması — EAF Çelik Tesisi

| Performans | SEC [kWh/ton sıvı çelik] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | <380 | >40 | Referans tesis, yeni nesil teknoloji |
| İyi | 380-430 | 34-40 | İnce ayar optimizasyonu |
| Ortalama | 430-500 | 28-34 | Sistematik enerji yönetimi |
| Düşük | 500-600 | 22-28 | Ciddi iyileştirme programı |
| Kritik | >600 | <22 | Acil müdahale, teknoloji yenileme |

### 5.3 EU BREF Karşılaştırması

| Parametre | Türkiye Ortalaması | EU BREF BAT | Fark |
|---|---|---|---|
| EAF SEC (elektrik) | 400-480 kWh/ton | 330-400 kWh/ton | %10-25 yüksek |
| Haddeleme ısıtma fırını | 1.8-2.5 GJ/ton | 1.2-1.8 GJ/ton | %30-40 yüksek |
| Toz toplama enerji tüketimi | 15-25 kWh/ton | 10-15 kWh/ton | %40-65 yüksek |
| Baca gazı ısı geri kazanım oranı | %10-30 | %40-60 | %20-30 fark |
| Hurda ön ısıtma penetrasyonu | %5-10 | %30-50 | %25-40 fark |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| EAF elektrik profili optimizasyonu | 2-5 | 10,000-30,000 | 3-6 ay | Güç eğrisi, oksijen zamanlama |
| Basınçlı hava kaçak onarımı | 1-3 | 5,000-15,000 | <3 ay | Büyük tesislerde ciddi kaçak |
| Fırın brülör ayarı | 1-3 | 2,000-10,000 | <6 ay | O₂ trim, fazla hava azaltma |
| Fırın kapak/kapı disiplini | 1-2 | 2,000-5,000 | <3 ay | Radyasyon kaybı azaltma |
| Aydınlatma LED dönüşümü | 0.5-1 | 10,000-30,000 | 6-12 ay | Büyük tesis alanlarında |
| Soğutma suyu optimizasyonu | 0.5-1 | 5,000-15,000 | 3-6 ay | Gereksiz soğutma azaltma |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| EAF baca gazı ısı geri kazanımı | 5-10 | 200,000-600,000 | 2-3 yıl | Buhar üretimi, hurda ön ısıtma |
| Hurda ön ısıtma sistemi (Consteel) | 8-15 | 500,000-2,000,000 | 2-4 yıl | 60-80 kWh/ton tasarruf |
| VSD (fan, pompa, kompresör) | 3-8 | 50,000-200,000 | 1-3 yıl | Toz toplama fanları kritik |
| Fırın reküperatör/rejeneratif brülör | 5-12 | 100,000-400,000 | 2-3 yıl | Yanma havası ön ısıtma |
| EAF şarj optimizasyonu (otomasyon) | 2-5 | 50,000-150,000 | 1-2 yıl | Hurda sepeti optimizasyonu |
| Isıl işlem fırını izolasyon iyileştirme | 3-8 | 30,000-100,000 | 1-3 yıl | Seramik fiber yalıtım |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Yeni nesil EAF teknolojisi | 10-20 | 5,000,000-20,000,000 | 5-8 yıl | Shaft furnace, twin-shell |
| ORC (Organik Rankine) atık ısı elektrik | 3-5 | 500,000-2,000,000 | 4-7 yıl | Baca gazı/soğutma suyundan |
| Cüruf ısı geri kazanımı | 2-4 | 200,000-800,000 | 4-7 yıl | 1,500°C cüruftan enerji |
| Hidrojel bazlı DRI (gelecek) | 30-50 | >50,000,000 | >10 yıl | Yeşil çelik üretimi |
| Dijital ikiz / AI optimizasyonu | 2-5 | 100,000-500,000 | 3-5 yıl | EAF proses optimizasyonu |

### 6.4 Toplam Tasarruf Potansiyeli

```
EAF çelik tesisi tipik tasarruf potansiyeli:

Hızlı kazanımlar:         %5-12
Orta vadeli projeler:     %12-25
Stratejik projeler:       %15-35

Gerçekçi toplam tasarruf: %20-40
Tipik yatırım geri dönüşü (toplam paket): 2-5 yıl

Not: Enerji maliyeti çelik üretiminin %25-35'ini oluşturduğundan
tasarruf projelerinin ekonomik etkisi çok yüksektir.
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 EAF Optimizasyonu

1. Elektrik ve kimyasal enerji dengesinin optimize edilmesi (oxy-fuel brülör + O₂ lance)
2. Foamy slag (köpüklü cüruf) uygulaması ile ark kararlılığı ve verim artışı
3. Elektrot tüketiminin minimize edilmesi (yüksek akım regülasyonu)
4. Döküm-döküm arası (tap-to-tap) süresinin minimize edilmesi
5. Hurda kalitesi yönetimi (homojen şarj, düşük safsızlık)

### 7.2 Fırın Yönetimi

1. Rejeneratif brülör kullanımı (ısıl işlem ve tav fırınlarında)
2. Fırın basıncı kontrolü (pozitif basınç, hava sızıntısı engelleme)
3. Optimum fırın sıcaklık profili (gereksiz aşırı ısıtmadan kaçınma)
4. Seramik fiber yalıtım uygulaması (geleneksel tuğla yerine)
5. Kontrollü atmosfer fırınlarda gaz tüketimi optimizasyonu

### 7.3 Atık Isı Yönetimi

1. EAF baca gazı ısısının hurda ön ısıtma veya buhar üretiminde kullanılması
2. Soğutma suyu atık ısısının tesis ısıtma veya ön ısıtmada kullanılması
3. Cüruf ısı geri kazanım potansiyelinin değerlendirilmesi
4. Fırın egzoz gazı reküperatör/rejeneratör uygulaması
5. Haddeleme soğutma suyundan ısı geri kazanımı

### 7.4 Yardımcı Sistemler

1. Toz toplama fan'larında VSD uygulaması (en büyük elektrik tüketicilerinden)
2. Basınçlı hava sisteminin optimize edilmesi (kaçak onarımı, basınç düşürme)
3. Su soğutma sisteminde kademeli soğutma (free cooling + chiller)
4. Enerji izleme ve yönetim sistemi (EAF bazlı real-time monitoring)
5. Elektrik kalitesi yönetimi (harmonik filtreleme, güç faktörü düzeltme)

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: Hatay/İskenderun, Türkiye
Tesis tipi: EAF çelik üretimi (uzun ürünler — inşaat çeliği)
Kapasite: 1,200,000 ton/yıl sıvı çelik
Çalışma: 7,800 saat/yıl, sürekli üretim (3 vardiya)
Ekipman: 1 × 120 ton EAF, 1 × 120 ton LF, sürekli döküm,
         sıcak haddeleme hattı, 5 × 300 kW basınçlı hava kompresörü,
         toz toplama sistemi (1,200,000 m³/h)
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Elektrik tüketimi | 540,000,000 | kWh/yıl |
| Doğalgaz tüketimi | 45,000,000 | Nm³/yıl |
| Toplam enerji | 1,005,000,000 | kWh/yıl |
| Çelik üretimi | 1,200,000 | ton/yıl |
| SEC (toplam) | 838 | kWh/ton çelik |
| SEC (EAF elektrik) | 435 | kWh/ton sıvı çelik |
| Enerji maliyeti | 78,000,000 | €/yıl |
| Exergy verimi | %29.5 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | EAF baca gazı ısı geri kazanımı (buhar üretimi) | 1,800,000 |
| 2 | VSD toz toplama fanları (4 adet ana fan) | 350,000 |
| 3 | EAF oksijen/kömür enjeksiyon optimizasyonu | 250,000 |
| 4 | Haddeleme fırını rejeneratif brülör | 650,000 |
| 5 | Basınçlı hava sistemi optimizasyonu (VSD + kaçak) | 120,000 |
| 6 | Enerji izleme sistemi (real-time, döküm bazlı) | 180,000 |
| 7 | Elektrik kalitesi iyileştirme (harmonik filtre) | 400,000 |
| **Toplam** | | **3,750,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| Elektrik tüketimi | 540,000 MWh/yıl | 468,000 MWh/yıl | 72,000 MWh/yıl | -13.3 |
| Doğalgaz tüketimi | 45,000,000 Nm³/yıl | 37,800,000 Nm³/yıl | 7,200,000 Nm³/yıl | -16.0 |
| SEC (toplam) | 838 kWh/ton | 720 kWh/ton | 118 kWh/ton | -14.1 |
| SEC (EAF elektrik) | 435 kWh/ton | 395 kWh/ton | 40 kWh/ton | -9.2 |
| Enerji maliyeti | 78,000,000 €/yıl | 66,520,000 €/yıl | 11,480,000 €/yıl | -14.7 |
| Exergy verimi | %29.5 | %34.8 | +5.3 puan | +18.0 |
| CO₂ emisyonu | 290,000 ton/yıl | 248,500 ton/yıl | 41,500 ton/yıl | -14.3 |

### 8.5 Ekonomik Analiz

```
Toplam yatırım:           3,750,000 €
Yıllık tasarruf:         11,480,000 €
Basit geri ödeme süresi: 3,750,000 / 11,480,000 = 0.33 yıl ≈ 4 ay
Net bugünkü değer (NPV): 73,300,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):    >%300

Tasarruf dağılımı:
  Elektrik: 72,000 MWh × €0.10/kWh  = 7,200,000 €/yıl (%63)
  Doğalgaz: 7,200,000 Nm³ × €0.40/Nm³ = 2,880,000 €/yıl (%25)
  Bakım + elektrik kalitesi:          = 1,400,000 €/yıl (%12)
```

### 8.6 Öğrenilen Dersler

1. EAF baca gazı ısı geri kazanımı en yüksek mutlak tasarrufu sağladı ancak kirli gaz koşulları eşanjör bakımını zorlaştırdı
2. VSD toz toplama fanlarında %30-40 enerji tasarrufu elde edildi (fan'lar sürekli tam devir yerine ihtiyaç bazlı çalıştı)
3. EAF oksijen/kömür optimizasyonu üretim hızını da artırdı (tap-to-tap süresinde %5 azalma)
4. Enerji izleme sistemi döküm bazlı performans takibi sağlayarak operatör farkındalığını artırdı
5. Büyük ölçekli tesislerde küçük yüzdelik tasarruflar bile mutlak değer olarak çok büyüktür

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 EAF Enerji Dengesi

```
E_toplam = E_elektrik + E_kimyasal + E_oksijen

Burada:
- E_elektrik = elektrik enerjisi [kWh/ton]
- E_kimyasal = kömür + doğalgaz kimyasal enerjisi [kWh/ton]
- E_oksijen = oksijen ile oksidasyon enerjisi [kWh/ton]

Hesaplama örneği:
E_elektrik = 400 kWh/ton
Kömür: 15 kg/ton × 8.0 kWh/kg = 120 kWh/ton
Doğalgaz: 5 Nm³/ton × 10.33 kWh/Nm³ = 52 kWh/ton
O₂ oksidasyonu: ~80 kWh/ton (Fe, Si, Mn oksidasyonu)

E_toplam = 400 + 120 + 52 + 80 = 652 kWh/ton
Exergy girişi ≈ 400 + (120+52)×1.04 + 80 = 659 kW·h/ton
```

### 9.2 Baca Gazı Isı Geri Kazanım Potansiyeli

```
Q_gerikazanım = ṁ_baca × Cp_baca × (T_giriş - T_çıkış) × η

Burada:
- ṁ_baca = baca gazı debisi [kg/s]
- Cp_baca = baca gazı özgül ısısı ≈ 1.05 kJ/(kg·K)
- T_giriş = giriş sıcaklığı [°C] (EAF çıkışı 800-1,200°C)
- T_çıkış = çıkış sıcaklığı [°C] (hedef 200-250°C)
- η = geri kazanım verimi (tipik: 0.60-0.80)

Hesaplama örneği:
ṁ_baca = 40 kg/s (120 ton EAF, döküm sırasında)
T_giriş = 900°C, T_çıkış = 250°C, η = 0.70

Q_gerikazanım = 40 × 1.05 × (900 - 250) × 0.70 = 19,110 kW ≈ 19.1 MW

Yıllık enerji (EAF çalışma saati 6,000 h, ortalama %40 kapasitede):
= 19,110 × 6,000 × 0.40 / 1,000 = 45,864 MWh/yıl
= 45,864 × €0.10/kWh = 4,586,400 €/yıl
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Enerji Yönetimi](energy_management.md) -- ISO 50001 uygulama rehberi
- [Kompresör Benchmarkları](../compressor/benchmarks.md) -- Basınçlı hava verimlilik verileri
- [Kompresör VSD](../compressor/solutions/vsd.md) -- Değişken hız sürücü uygulamaları
- [Hava Kaçakları](../compressor/solutions/air_leaks.md) -- Kaçak tespit ve onarım
- [Kompresör Isı Geri Kazanım](../compressor/solutions/heat_recovery.md) -- Atık ısı değerlendirme
- [Pompa VSD](../pump/solutions/vsd.md) -- Pompa VSD uygulamaları
- [Kazan Benchmarkları](../boiler/benchmarks.md) -- Kazan verimlilik verileri
- [Çimento Sektörü](sector_cement.md) -- Benzer yüksek sıcaklık prosesleri
- [Otomotiv Sektörü](sector_automotive.md) -- Metal işleme müşterisi

## Referanslar

- EU BREF, "Best Available Techniques (BAT) Reference Document for Iron and Steel Production," European Commission, 2012
- EU BREF, "Best Available Techniques Reference Document for the Non-Ferrous Metals Industries," 2017
- Worldsteel Association, "Energy Use in the Steel Industry," Fact Sheet, 2023
- International Aluminium Institute (IAI), "Global Aluminium Cycle and Energy Use," 2022
- US DOE, "Improving Process Heating System Performance — A Sourcebook for Industry," 2007
- Kirschen, M. et al. (2009), "Energy efficiency and the influence of gas burners to the energy related carbon dioxide emissions of electric arc furnaces in steel industry," Energy, 34(9), 1065-1072
- Çamdali, Ü. & Tunç, M. (2003), "Exergy analysis and efficiency in an industrial AC electric ARC furnace," Applied Thermal Engineering, 23(17), 2255-2267
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Demir-Çelik Sektörü Enerji Verimliliği," 2022
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- American Foundry Society (AFS), "Energy Best Practices for Metalcasting," 2019
