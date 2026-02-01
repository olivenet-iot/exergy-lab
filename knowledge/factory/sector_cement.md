# Çimento Sektörü Enerji Profili ve Optimizasyon (Cement Sector Energy Profile)

> Son güncelleme: 2026-01-31

## Genel Bakış

Çimento sektörü, Türkiye'nin en enerji yoğun sanayi kollarından biridir. Türkiye dünyada çimento üretiminde ilk 5 içinde yer almakta olup yıllık 70-80 milyon ton üretim kapasitesine sahiptir. Sektörde döner fırın (rotary kiln) baskın enerji tüketicisidir ve toplam enerjinin %85-90'ını kullanır. Termal enerji tüketimi 2,700-4,200 MJ/ton klinker, elektrik tüketimi 80-140 kWh/ton çimento arasındadır. Alternatif yakıt kullanımı (waste co-processing) ve klinker faktörü azaltma sektördeki en önemli dekarbonizasyon stratejileridir.

## 1. Sektör Genel Bakış (Sector Overview)

### 1.1 Türkiye Ölçeği ve Önemi

- Üretim kapasitesi: ~80 milyon ton/yıl çimento
- Gerçek üretim: ~65-75 milyon ton/yıl (kapasite kullanımı %80-90)
- Klinker üretimi: ~55-65 milyon ton/yıl
- Tesis sayısı: ~55 entegre fabrika + ~20 öğütme tesisi
- İhracat: ~8-12 milyon ton/yıl (dünyanın en büyük çimento ihracatçılarından)
- Enerji maliyetinin üretim maliyetindeki payı: %35-55
- Sektör toplam Türkiye CO₂ emisyonlarının %5-7'sinden sorumlu

### 1.2 Üretim Prosesi ve Enerji Yoğunlukları

| Proses Adımı | Enerji Türü | Enerji Payı [%] | Sıcaklık Aralığı |
|---|---|---|---|
| Hammadde hazırlama (kırma) | Elektrik | 2-3 | Ortam |
| Hammadde öğütme (farin) | Elektrik | 20-25 | Ortam-100°C |
| Ön ısıtma (preheater) | Termal | 15-20 | 300-900°C |
| Kalsinasyon (precalciner) | Termal | 35-45 | 850-900°C |
| Klinkerleşme (kiln) | Termal | 25-35 | 1,350-1,450°C |
| Klinker soğutma | Elektrik (fan) | 2-3 | 1,400→100°C |
| Çimento öğütme | Elektrik | 25-35 | Ortam-100°C |
| Paketleme ve yükleme | Elektrik | 1-2 | Ortam |

## 2. Enerji Tüketim Profili (Energy Consumption Profile)

### 2.1 Enerji Kaynağı Dağılımı

| Enerji Kaynağı | Tipik Pay [%] | Kullanım Alanı |
|---|---|---|
| Kömür (ithal + yerli) | 30-45 | Döner fırın yakıtı |
| Petrol koku (petcoke) | 20-35 | Döner fırın yakıtı |
| Alternatif yakıt (RDF, lastik, atık) | 5-25 | Döner fırın, precalciner |
| Doğalgaz | 0-10 | Fırın start-up, yardımcı |
| Elektrik | 20-30 (toplam enerjinin) | Öğütme, fanlar, taşıma |

### 2.2 Termal ve Elektrik Enerji Dağılımı

```
Termal enerji dağılımı (toplam: 2,700-4,200 MJ/ton klinker):
  Kalsinasyon reaksiyonu (CaCO₃→CaO+CO₂): ~1,760 MJ/ton (%45-55)
  Baca gazı ile kayıp:                     400-800 MJ/ton (%15-25)
  Klinker soğutma havası ile kayıp:        200-400 MJ/ton (%8-12)
  Radyasyon ve konveksiyon kaybı:          150-350 MJ/ton (%5-10)
  Toz ile kayıp:                           50-150 MJ/ton (%2-5)
  Nem buharlaştırma:                       50-200 MJ/ton (%2-6)

Elektrik enerji dağılımı (toplam: 80-140 kWh/ton çimento):
  Çimento öğütme:           30-45 kWh/ton (%30-40)
  Farin (hammadde) öğütme:  15-25 kWh/ton (%17-22)
  Fırın ana fan:             8-15 kWh/ton (%8-12)
  Klinker soğutucu fanları:  5-8 kWh/ton  (%5-7)
  Diğer fanlar:              5-10 kWh/ton (%5-8)
  Malzeme taşıma:            3-8 kWh/ton  (%3-7)
  Basınçlı hava:             2-5 kWh/ton  (%2-4)
  Aydınlatma ve yardımcı:    2-4 kWh/ton  (%2-3)
```

### 2.3 Fırın Tipi ve Enerji Tüketimi

| Fırın Tipi | Termal SEC [MJ/ton klinker] | Durum |
|---|---|---|
| 6 kademeli preheater + precalciner | 2,700-3,100 | En iyi uygulama |
| 5 kademeli preheater + precalciner | 2,900-3,300 | Yaygın modern tesis |
| 4 kademeli preheater + precalciner | 3,100-3,500 | Yaygın |
| 4 kademeli preheater (precalciner yok) | 3,300-3,800 | Eski teknoloji |
| Long dry kiln (ön ısıtmasız) | 3,800-4,500 | Çok eski, dönüşüm gerekli |
| Semi-dry (Lepol) | 3,200-3,800 | Nadir |
| Wet process | 5,000-7,000 | Artık kullanılmıyor |

## 3. Tipik Ekipman Envanteri (Typical Equipment Inventory)

### 3.1 Entegre Çimento Fabrikası (Kapasite ~5,000 ton/gün klinker)

| Ekipman | Tipik Kapasite | Adet | Enerji Payı [%] | Enerji Türü |
|---|---|---|---|---|
| Döner fırın (rotary kiln) | 4.5-5.5 m çap × 60-80 m | 1 | 70-80 (termal) | Kömür/petcoke |
| Preheater + precalciner | 5-6 kademe | 1 | (termal dahil) | Kömür/alt.yakıt |
| Farin değirmeni (VRM/BM) | 200-350 ton/h | 1-2 | 15-22 (elektrik) | Elektrik |
| Çimento değirmeni (VRM/BM) | 100-250 ton/h | 2-3 | 25-35 (elektrik) | Elektrik |
| Klinker soğutucu (grate cooler) | 5,000-7,000 ton/gün | 1 | 2-3 (elektrik) | Elektrik |
| Fırın ana fan | 300-800 kW | 1-2 | 6-10 (elektrik) | Elektrik |
| Kömür değirmeni | 30-60 ton/h | 1-2 | 3-5 (elektrik) | Elektrik |
| Basınçlı hava kompresörü | 75-200 kW | 3-5 | 2-4 (elektrik) | Elektrik |
| ESP/bag filter | 500,000-1,200,000 m³/h | 2-4 | 1-3 (elektrik) | Elektrik |

### 3.2 Ekipman Referansları

- Kompresör sistemleri: bkz. `../compressor/equipment/systems_overview.md`
- Kazan sistemleri (WHR): bkz. `../boiler/equipment/waste_heat.md`

## 4. Exergy Analizi (Exergy Analysis)

### 4.1 Exergy Akış Diyagramı (Tipik Çimento Fabrikası)

```
YAKIT EXERGY (%78)  ────────────────────────────────┐
                                                     │
ELEKTRİK EXERGY (%20)  ───────────────────────────┐│
                                                   ││
HAMMADDE KİMYASAL EXERGY (%2) ──────────────────┐ ││
                                                 │ ││
                  ┌──────────────────────────────┴─┴┤
                  │     TOPLAM EXERGY GİRİŞİ        │
                  │        (100%)                    │
                  ├──────────────────────────────────┘
                  │
  ┌───────────────┤ Yanma tersinmezliği (%18-25) ──────→ YIKIM
  │               │
  │  ┌────────────┤ Kalsinasyon tersinmezliği (%8-12) ─→ YIKIM
  │  │            │
  │  │  ┌─────────┤ Isı transferi tersinmezliği (%6-10)→ YIKIM
  │  │  │         │
  │  │  │  ┌──────┤ Baca gazı exergisi (%6-10) ────────→ ATIK
  │  │  │  │      │
  │  │  │  │  ┌───┤ Klinker soğutma havası (%4-7) ────→ ATIK
  │  │  │  │  │   │
  │  │  │  │  │   │ Öğütme tersinmezliği (%5-8) ──────→ YIKIM
  │  │  │  │  │   │ Yüzey kayıpları (%2-4) ───────────→ ATIK
  │  │  │  │  │   │
  │  │  │  │  │   ├───────────────────────────────────┐
  │  │  │  │  │   │  ÜRÜN EXERGY (%25-35)             │
  │  │  │  │  │   │  (çimento kimyasal exergisi)      │
  │  │  │  │  │   └───────────────────────────────────┘
```

### 4.2 Ana Exergy Kayıp Noktaları

| Kayıp Noktası | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma tersinmezliği | 18-25 | Fırın ve precalciner yanma odası |
| Kalsinasyon tersinmezliği | 8-12 | CaCO₃→CaO+CO₂ reaksiyon entropi üretimi |
| Isı transferi tersinmezliği | 6-10 | Fırın iç duvarı → malzeme, preheater |
| Baca gazı exergisi | 6-10 | 250-400°C çıkış sıcaklığında |
| Öğütme tersinmezliği | 5-8 | Mekanik→ısı dönüşüm kaybı |
| Klinker soğutma havası | 4-7 | 200-350°C sıcak hava fazlası |
| Yüzey radyasyon kayıpları | 2-4 | Fırın kabuk sıcaklığı 250-400°C |
| Toz kayıpları | 1-3 | Bypass toz, filtre tozu |

### 4.3 Tipik Exergy Verimi

```
η_ex,çimento = Ex_ürün / Ex_giriş × 100

Tipik aralık: %25-35
Sektör ortalaması: %30
En iyi uygulama: %38-40

Alt proses exergy verimleri:
  Fırın (pişirme):       %25-35
  Preheater/precalciner: %35-50
  Klinker soğutucu:      %30-45
  Farin öğütme (VRM):    %3-8 (çok düşük)
  Çimento öğütme (VRM):  %3-8 (çok düşük)

Not: Öğütme proseslerinin exergy verimi son derece düşüktür.
Elektrik enerjisinin (saf exergy) büyük kısmı sürtünme ısısına
dönüşmekte, yalnızca küçük bir kısım yeni yüzey oluşturma (kırma)
exergisine dönüşmektedir.
```

## 5. Benchmark Verileri (Benchmark Data)

### 5.1 Spesifik Enerji Tüketimi (SEC) — Proses Bazında

| Proses | SEC Termal [MJ/ton klinker] | SEC Elektrik [kWh/ton çimento] | Kaynak |
|---|---|---|---|
| Klinker üretimi (termal) | 2,700-4,200 | — | CSI/GCCA |
| Farin öğütme (bilyalı) | — | 18-25 | VDZ |
| Farin öğütme (VRM) | — | 12-17 | VDZ |
| Çimento öğütme (bilyalı) | — | 35-45 | VDZ |
| Çimento öğütme (VRM) | — | 22-30 | VDZ |
| Çimento öğütme (kombine) | — | 28-38 | VDZ |
| Kömür öğütme | — | 15-25 | VDZ |
| Toplam elektrik | — | 80-140 | CSI |

### 5.2 Performans Sınıflandırması — Entegre Çimento Fabrikası

| Performans | SEC Termal [MJ/t klinker] | SEC Elektrik [kWh/t çimento] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|---|
| Mükemmel | <2,900 | <85 | >38 | Referans tesis |
| İyi | 2,900-3,200 | 85-100 | 33-38 | İnce ayar |
| Ortalama | 3,200-3,500 | 100-120 | 28-33 | Sistematik iyileştirme |
| Düşük | 3,500-4,000 | 120-140 | 22-28 | Ciddi program |
| Kritik | >4,000 | >140 | <22 | Acil müdahale |

### 5.3 EU BREF Karşılaştırması

| Parametre | Türkiye Ortalaması | EU BREF BAT | Fark |
|---|---|---|---|
| Termal SEC | 3,200-3,600 MJ/ton | 2,700-3,100 MJ/ton | %10-20 yüksek |
| Elektrik SEC | 100-125 kWh/ton | 80-100 kWh/ton | %15-25 yüksek |
| Alternatif yakıt oranı | %5-15 | %30-80 | %25-65 fark |
| Klinker faktörü | 0.80-0.85 | 0.65-0.75 | 0.10-0.15 fark |
| WHR penetrasyonu | %5-10 | %20-40 | %15-30 fark |

## 6. Optimizasyon Fırsatları (Optimization Opportunities)

### 6.1 Hızlı Kazanımlar (Quick Wins) — Geri Dönüş <1 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Fırın operasyon optimizasyonu | 2-5 | 10,000-50,000 | <6 ay | Besleme hızı, sıcaklık profili |
| Basınçlı hava kaçak onarımı | 0.5-1 | 5,000-15,000 | <3 ay | Kaçak tespit ve onarım |
| Fan vane optimizasyonu | 1-3 | 5,000-20,000 | 3-6 ay | Mevcut fan kontrol iyileştirme |
| Soğutucu grate optimizasyonu | 1-3 | 10,000-30,000 | 3-6 ay | Hava dağılımı iyileştirme |
| Bypass oranı azaltma | 1-2 | 5,000-20,000 | <6 ay | Ham madde kalitesi yönetimi |

### 6.2 Orta Vadeli Projeler — Geri Dönüş 1-3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Alternatif yakıt sistemi kurulumu | 5-15 | 500,000-2,000,000 | 1-3 yıl | RDF, lastik, atık yağ |
| VRM dönüşümü (çimento öğütme) | 5-10 (elektrik) | 2,000,000-5,000,000 | 2-4 yıl | Bilyalı → VRM |
| VSD ana fan | 3-6 | 100,000-300,000 | 1-2 yıl | Fırın ana fan, soğutucu fan |
| Preheater kademe artırma | 3-8 | 500,000-2,000,000 | 2-3 yıl | 4 → 5/6 kademe |
| Soğutucu modernizasyonu | 3-5 | 300,000-1,000,000 | 2-3 yıl | 2. jenerasyon → 3./4. jenerasyon |
| Klinker faktörü azaltma | 3-8 | 200,000-800,000 | 1-3 yıl | Cüruf, uçucu kül, kalker katma |

### 6.3 Stratejik Projeler — Geri Dönüş >3 Yıl

| Önlem | Tasarruf [%] | Yatırım [€] | Geri Dönüş | Açıklama |
|---|---|---|---|---|
| Atık ısı geri kazanımı (ORC/Buhar) | 3-6 | 2,000,000-8,000,000 | 4-7 yıl | Preheater + soğutucu egzoz |
| Yeni nesil öğütme (HPGR + VRM) | 5-15 (elektrik) | 3,000,000-8,000,000 | 4-7 yıl | Yüksek basınçlı öğütme |
| CCS (Carbon Capture & Storage) | CO₂ %60-90 | 20,000,000-80,000,000 | >10 yıl | Karbon yakalama (gelecek) |
| Dijital ikiz / AI fırın kontrolü | 2-5 | 200,000-800,000 | 3-5 yıl | Gerçek zamanlı optimizasyon |
| Güneş enerjisi (PV) | 2-5 (elektrik) | 500,000-2,000,000 | 5-8 yıl | Tesis elektriği |

### 6.4 Toplam Tasarruf Potansiyeli

```
Entegre çimento fabrikası tipik tasarruf potansiyeli:

Hızlı kazanımlar:         %5-12
Orta vadeli projeler:     %10-25
Stratejik projeler:       %10-20

Gerçekçi toplam tasarruf: %20-40
Tipik yatırım geri dönüşü (toplam paket): 3-6 yıl

Alternatif yakıt etkisi (ek):
  %10 alt. yakıt oranı → %5-8 yakıt maliyeti azalma
  %30 alt. yakıt oranı → %15-25 yakıt maliyeti azalma
  %50 alt. yakıt oranı → %30-45 yakıt maliyeti azalma
```

## 7. Sektörel En İyi Uygulamalar (Best Practices)

### 7.1 Fırın ve Pişirme

1. 6 kademeli preheater + precalciner (termal SEC <3,000 MJ/ton hedefi)
2. Fırın kabuğu kızılötesi tarama ile refrakter izleme
3. Optimum fırın besleme hızı ve yakıt dozajı (AI/model prediktif kontrol)
4. Koçan kısmı (clinker zone) sıcaklık profilinin optimize edilmesi
5. Bypass oranının minimum tutulması (ham madde klor/alkali yönetimi)

### 7.2 Öğütme

1. Dikey merdaneli değirmen (VRM) kullanımı (bilyalı değirmen yerine %30-40 tasarruf)
2. HPGR (High Pressure Grinding Roll) + separator kombinasyonu
3. Yüksek verimli separator (3. jenerasyon) kullanımı
4. Çimento öğütme sırasında su enjeksiyonu optimizasyonu
5. Öğütme yardımcıları (grinding aids) kullanımı (%3-5 enerji tasarrufu)

### 7.3 Alternatif Yakıt ve Hammadde

1. Alternatif yakıt oranının kademeli artırılması (hedef >%30)
2. RDF (Refuse Derived Fuel) hazırlama ve dozajlama sistemi
3. Lastik, atık yağ, endüstriyel atık kullanımı
4. Alternatif hammadde (cüruf, uçucu kül) ile klinker faktörü azaltma
5. Biyokütle bazlı yakıtların değerlendirilmesi

### 7.4 Atık Isı Yönetimi

1. ORC (Organik Rankine Çevrimi) ile elektrik üretimi (preheater + soğutucu egzoz)
2. Soğutucu fazla sıcak havasının farin kurutmada kullanılması
3. Fırın kabuğu radyasyon kaybının izlenmesi ve refrakter bakımı
4. Baca gazı ısısının ham madde kurutmada kullanılması
5. WHR (Waste Heat Recovery) sistem verimliliğinin sürekli izlenmesi

## 8. Vaka Çalışması (Case Study)

### 8.1 Tesis Tanımı

```
Lokasyon: Mersin, Türkiye
Tesis tipi: Entegre çimento fabrikası
Kapasite: 5,500 ton/gün klinker (~2 milyon ton/yıl çimento)
Çalışma: 7,500 saat/yıl, sürekli üretim
Fırın: 4.8 m × 72 m döner fırın, 5 kademeli preheater + precalciner
Öğütme: 2 × bilyalı çimento değirmeni, 1 × bilyalı farin değirmeni
```

### 8.2 Enerji Tüketimi (Önce — Before)

| Parametre | Değer | Birim |
|---|---|---|
| Termal enerji (kömür + petcoke) | 5,800,000 | GJ/yıl |
| Elektrik tüketimi | 220,000,000 | kWh/yıl |
| Klinker üretimi | 1,650,000 | ton/yıl |
| Çimento üretimi | 2,000,000 | ton/yıl |
| SEC termal | 3,515 | MJ/ton klinker |
| SEC elektrik | 110 | kWh/ton çimento |
| Klinker faktörü | 0.825 | — |
| Alternatif yakıt oranı | %3 | — |
| Enerji maliyeti | 42,000,000 | €/yıl |
| Exergy verimi | %27.5 | — |

### 8.3 Uygulanan Önlemler

| No | Önlem | Yatırım [€] |
|---|---|---|
| 1 | VRM çimento değirmeni (1 × yeni, 1 bilyalı yedek) | 4,500,000 |
| 2 | Alternatif yakıt sistemi (RDF + lastik) | 1,200,000 |
| 3 | Preheater 5. kademe optimizasyonu + sızdırmazlık | 350,000 |
| 4 | ORC atık ısı elektrik üretimi (4.5 MW) | 5,800,000 |
| 5 | VSD ana fan + soğutucu fanları | 280,000 |
| 6 | Klinker faktörü azaltma (kalker + cüruf katkısı) | 600,000 |
| 7 | Dijital fırın kontrol sistemi (model prediktif) | 450,000 |
| **Toplam** | | **13,180,000** |

### 8.4 Sonuçlar (Sonra — After)

| Parametre | Önce | Sonra | Tasarruf | Değişim [%] |
|---|---|---|---|---|
| SEC termal | 3,515 MJ/ton klinker | 3,080 MJ/ton klinker | 435 MJ/ton | -12.4 |
| SEC elektrik | 110 kWh/ton çimento | 88 kWh/ton çimento | 22 kWh/ton | -20.0 |
| Klinker faktörü | 0.825 | 0.74 | -0.085 | -10.3 |
| Alternatif yakıt oranı | %3 | %22 | +19 puan | +633 |
| ORC elektrik üretimi | 0 | 28,000 MWh/yıl | +28,000 MWh | — |
| Enerji maliyeti | 42,000,000 €/yıl | 33,200,000 €/yıl | 8,800,000 €/yıl | -21.0 |
| Exergy verimi | %27.5 | %34.2 | +6.7 puan | +24.4 |
| CO₂ emisyonu | 1,550,000 ton/yıl | 1,250,000 ton/yıl | 300,000 ton/yıl | -19.4 |

### 8.5 Ekonomik Analiz

```
Toplam yatırım:           13,180,000 €
Yıllık tasarruf:           8,800,000 €
Basit geri ödeme süresi:  13,180,000 / 8,800,000 = 1.50 yıl ≈ 18 ay
Net bugünkü değer (NPV):  45,800,000 € (10 yıl, %8 iskonto)
İç verim oranı (IRR):     >%60

Tasarruf dağılımı:
  VRM elektrik tasarrufu:    44,000 MWh × €0.10/kWh = 4,400,000 €/yıl (%50)
  Alternatif yakıt (maliyet farkı):                  = 2,100,000 €/yıl (%24)
  ORC elektrik üretimi:     28,000 MWh × €0.10/kWh  = 2,800,000 €/yıl (%32)
  Termal tasarruf (fırın):                            = 1,500,000 €/yıl (%17)
  VSD + kontrol tasarrufu:                            =   500,000 €/yıl (%6)
  Klinker faktörü etkisi:                            = -2,500,000 €/yıl (ek maliyet)*

  *Klinker faktörü azaltma: katkı malzemesi maliyeti ek gider oluşturur
  ancak toplam CO₂ azalma ve ETS avantajı ile netleşir.
```

### 8.6 Öğrenilen Dersler

1. VRM dönüşümü en yüksek elektrik tasarrufunu sağladı (%30-35 öğütme enerjisi azalma)
2. ORC sistemi beklenen performansı tutturdu ancak ilk yıl devreye alma sorunları yaşandı
3. Alternatif yakıt oranı artışı kademeli olmalı; kalite kontrol ve dozajlama kritik
4. Fırın dijital kontrol sistemi operatör kabul sürecinde eğitim ve değişim yönetimi gerektirdi
5. Klinker faktörü azaltma çimento kalite standartlarıyla uyum gerektirir (EN 197-1)

## 9. Formüller ve Hesaplama Örnekleri

### 9.1 Klinker Termal Enerji Dengesi

```
Q_toplam = Q_kalsinasyon + Q_baca + Q_soğutma + Q_yüzey + Q_nem + Q_toz

Burada:
- Q_kalsinasyon = kalsinasyon reaksiyon enerjisi ≈ 1,760 MJ/ton klinker
- Q_baca = baca gazı ile kayıp [MJ/ton klinker]
- Q_soğutma = soğutucu fazla havası ile kayıp [MJ/ton klinker]
- Q_yüzey = fırın kabuk radyasyon kaybı [MJ/ton klinker]
- Q_nem = hammadde nem buharlaştırma [MJ/ton klinker]
- Q_toz = sıcak toz ile kayıp [MJ/ton klinker]

Hesaplama örneği:
Q_kalsinasyon = 1,760 MJ/ton
Q_baca = 650 MJ/ton (baca gazı 320°C)
Q_soğutma = 300 MJ/ton (soğutucu egzoz 280°C)
Q_yüzey = 250 MJ/ton (fırın kabuk)
Q_nem = 120 MJ/ton (hammadde nem %5)
Q_toz = 80 MJ/ton

Q_toplam = 1,760 + 650 + 300 + 250 + 120 + 80 = 3,160 MJ/ton klinker
```

### 9.2 ORC Atık Isı Elektrik Üretimi Potansiyeli

```
W_ORC = (Q_preheater + Q_soğutucu) × η_ORC

Burada:
- Q_preheater = preheater egzoz gazından alınan ısı [kW]
- Q_soğutucu = soğutucu egzoz gazından alınan ısı [kW]
- η_ORC = ORC termal verimi (tipik: %18-24)

Hesaplama örneği (5,500 ton/gün klinker):
Q_preheater = 12,000 kW (320°C → 200°C, 80 kg/s baca gazı)
Q_soğutucu = 8,000 kW (280°C → 130°C, 60 kg/s hava)

W_ORC = (12,000 + 8,000) × 0.20 = 4,000 kW = 4.0 MW

Yıllık üretim = 4,000 × 7,500 × 0.90 / 1,000 = 27,000 MWh/yıl
Yıllık gelir = 27,000 × €0.10/kWh = 2,700,000 €/yıl
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) -- Fabrika exergy analiz metodolojisi
- [KPI Tanımları](kpi_definitions.md) -- SEC, exergy verimlilik göstergeleri
- [Ekonomik Analiz](economic_analysis.md) -- Yatırım değerlendirme yöntemleri
- [Enerji Yönetimi](energy_management.md) -- ISO 50001 uygulama rehberi
- [Atık Isı Kazanı](../boiler/equipment/waste_heat.md) -- WHR kazan sistemleri
- [Kompresör Benchmarkları](../compressor/benchmarks.md) -- Basınçlı hava verimlilik verileri
- [Kompresör VSD](../compressor/solutions/vsd.md) -- Değişken hız sürücü uygulamaları
- [Metal İşleme Sektörü](sector_metal.md) -- Benzer yüksek sıcaklık prosesleri
- [Kimya Sektörü](sector_chemical.md) -- Benzer sürekli proses karakteristiği
- [Kağıt Sektörü](sector_paper.md) -- Benzer ölçekte enerji tüketimi

## Referanslar

- EU BREF, "Best Available Techniques (BAT) Reference Document for the Production of Cement, Lime and Magnesium Oxide," European Commission, 2013
- CSI/GCCA, "Getting the Numbers Right (GNR) Database," Global Cement and Concrete Association, 2023
- IEA, "Technology Roadmap — Low-Carbon Transition in the Cement Industry," 2018
- WBCSD/CSI, "Cement Sustainability Initiative — Energy Efficiency Improvement Opportunities," 2017
- VDZ, "Zement-Taschenbuch (Cement Pocket Book)," 52nd Edition, 2019
- Madlool, N.A. et al. (2011), "A critical review on energy use and savings in the cement industries," Renewable and Sustainable Energy Reviews, 15(4), 2042-2060
- Atmaca, A. & Yumrutaş, R. (2014), "Analysis of the parameters affecting energy consumption of a rotary kiln in cement industry," Applied Thermal Engineering, 66(1-2), 435-444
- Çamdali, Ü. et al. (2004), "Energy and exergy analyses in a rotary burner with pre-calcinations in cement production," Energy Conversion and Management, 45(18-19), 3017-3031
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Çimento Sektörü Enerji Verimliliği Potansiyeli," 2022
- EN 197-1, "Cement — Part 1: Composition, specifications and conformity criteria for common cements"
