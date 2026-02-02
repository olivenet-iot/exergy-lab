---
title: "Kesikli Proses Isı Entegrasyonu (Batch Process Heat Integration)"
category: factory
equipment_type: factory
keywords: [kesikli proses, batch entegrasyon, zaman dilimi, TES, termal depolama, üretim programı]
related_files: [factory/pinch/fundamentals.md, factory/pinch/total_site.md, factory/pinch/utility_systems.md, factory/pinch/practical_guide.md]
use_when: ["Kesikli proses entegrasyonu yapılırken", "Zaman dilimi analizi uygulanırken", "Termal depolama değerlendirilirken"]
priority: medium
last_updated: 2026-02-01
---

# Kesikli Proses Isı Entegrasyonu (Batch Process Heat Integration)

> Son güncelleme: 2026-02-01

## Genel Bakış

Kesikli (batch) prosesler, endüstriyel üretimin önemli bir bölümünü oluşturur. Gıda, ilaç, boya, bira ve tekstil gibi sektörlerde üretim döngüleri belirli zaman aralıklarında gerçekleşir ve proses akışları sürekli değil, zamanla değişken yapıdadır. Klasik Linnhoff pinch analizi sürekli prosesler için geliştirilmiş olsa da, kesikli proseslere uyarlanması özel yöntemler gerektirir.

Kesikli proseslerde ısı entegrasyonu, sürekli proseslere göre daha karmaşıktır çünkü ısı kaynakları ve kullanıcıları aynı anda mevcut olmayabilir. Bu durum, termal enerji depolama (TES — Thermal Energy Storage) sistemlerinin kullanılmasını ve üretim programlarının optimize edilmesini zorunlu kılar. Doğru uygulandığında kesikli proseslerde %15-40 enerji tasarrufu sağlanabilir.

---

## 1. Kesikli vs Sürekli Proses (Batch vs Continuous)

### 1.1 Temel Farklar

Pinch analizi açısından kesikli ve sürekli prosesler arasındaki temel farklar aşağıda özetlenmiştir:

| Özellik | Sürekli Proses (Continuous) | Kesikli Proses (Batch) |
|---|---|---|
| Akış sürekliliği | Sabit, zamandan bağımsız | Zamanla değişken, döngüsel |
| Isı yükü | Sabit [kW] | Zamana bağlı [kW veya kJ/batch] |
| Pinch noktası | Tek, sabit | Her zaman diliminde farklı olabilir |
| Eşanjör kullanımı | %100 sürekli | Döngünün bir kısmında aktif |
| Entegrasyon fırsatı | Doğrudan eşleştirme yeterli | Termal depolama gerekebilir |
| Analiz karmaşıklığı | Orta | Yüksek — zaman boyutu eklenir |
| Tipik sektörler | Petrokimya, çimento, kağıt | Gıda, ilaç, boya, bira, tekstil |

### 1.2 Zaman Bağımlılığı Sorunu (Time Dependency Challenge)

Sürekli bir proseste, sıcak akış H1 ve soğuk akış C1 aynı anda mevcutsa, aralarına doğrudan bir eşanjör yerleştirmek mümkündür. Ancak kesikli bir proseste aşağıdaki durumlar ortaya çıkar:

1. **Zamansal uyumsuzluk (Temporal mismatch):** H1 akışı t=0-30 dk arasında, C1 akışı t=45-90 dk arasında mevcut olabilir. Doğrudan eşleştirme yapılamaz.

2. **Değişken yükler (Variable loads):** Aynı akışın ısı yükü döngü boyunca değişebilir (reaksiyon başlangıcı vs kararlı hal).

3. **Çoklu ürün kampanyaları (Multi-product campaigns):** Aynı ekipman farklı ürünler için farklı sıcaklıklarda çalıştırılabilir.

4. **Temizlik ve geçiş süreleri (Cleaning and transition):** Batchler arası temizlik ısı dengesini bozar.

Bu sorunları çözmek için iki temel model geliştirilmiştir: Zaman Dilimi Modeli (Time Slice Model) ve Zaman Ortalama Modeli (Time Average Model).

### 1.3 Kesikli Proses Örnek Problemi

Bu dosya boyunca aşağıdaki referans problemi kullanılacaktır:

```
Bir süt ürünleri fabrikası, 4 saatlik bir batch döngüsü ile çalışmaktadır:

Akış Verileri:
  H1: Pastörizasyon soğutma   72→4°C,   t=0-60 dk,   ṁ·Cp=5 kW/°C,  Q=340 kW
  H2: CIP yıkama atık suyu    80→25°C,  t=120-180 dk, ṁ·Cp=3 kW/°C,  Q=165 kW
  C1: Süt ön ısıtma            4→72°C,   t=0-60 dk,   ṁ·Cp=5 kW/°C,  Q=340 kW
  C2: CIP çözelti ısıtma      15→80°C,  t=90-150 dk,  ṁ·Cp=2.5 kW/°C, Q=162.5 kW
  C3: Kazan besleme suyu       20→60°C,  t=0-240 dk,  ṁ·Cp=1 kW/°C,   Q=40 kW

ΔTmin = 5°C
Batch döngü süresi = 240 dk (4 saat)
```

---

## 2. Zaman Dilimi Modeli (Time Slice Model)

### 2.1 Temel Kavram

Zaman Dilimi Modeli, batch döngüsünü, akışların başlangıç ve bitiş zamanlarına göre ayrık zaman aralıklarına böler. Her zaman aralığında mevcut akışlar belirlenir ve o aralık için standart pinch analizi uygulanır.

### 2.2 Zaman Dilimlerinin Oluşturulması

Referans problemimiz için zaman dilimleri şöyle oluşturulur:

**Adım 1:** Tüm akışların başlangıç ve bitiş zamanlarını listele:
```
Zamanlar: 0, 60, 90, 120, 150, 180, 240 dk
```

**Adım 2:** Bu zamanlardan ayrık aralıklar oluştur:

```
Zaman Dilimi (Time Slice)  |  Süre   |  Mevcut Akışlar
─────────────────────────────────────────────────────────
TS1:   0 —  60 dk          |  60 dk  |  H1, C1, C3
TS2:  60 —  90 dk          |  30 dk  |  C3
TS3:  90 — 120 dk          |  30 dk  |  C2, C3
TS4: 120 — 150 dk          |  30 dk  |  H2, C2, C3
TS5: 150 — 180 dk          |  30 dk  |  H2, C3
TS6: 180 — 240 dk          |  60 dk  |  C3
```

**Adım 3:** Gantt diyagramı ile görselleştirme:

```
Akış     0    30    60    90   120   150   180   210   240 [dk]
         |     |     |     |     |     |     |     |     |
H1  ████████████████████
H2                              ████████████████████
C1  ████████████████████
C2                        ███████████████████
C3  ████████████████████████████████████████████████████████
         |     |     |     |     |     |     |     |     |
TS:  |---TS1---|---TS2-|--TS3--|--TS4--|--TS5--|---TS6---|
```

### 2.3 Her Dilimde Pinch Analizi

**TS1 (0-60 dk): H1, C1, C3 mevcut**

```
Sıcak akışlar:  H1: 72→4°C,  CP=5 kW/°C,  Q=340 kW
Soğuk akışlar:  C1: 4→72°C,  CP=5 kW/°C,  Q=340 kW
                C3: 20→60°C, CP=1 kW/°C,   Q=40 kW

Toplam soğuk ihtiyaç = 340 + 40 = 380 kW
Toplam sıcak arz     = 340 kW

ΔTmin = 5°C ile pinch analizi:
  QH,min = 45 kW    (minimum dış ısıtma)
  QC,min = 5 kW     (minimum dış soğutma)
  Pinch = 72°C (sıcak) / 67°C (soğuk)
```

Doğrudan entegrasyon: H1 ile C1 arasında rejeneratif eşanjör yerleştirilebilir (pastörizasyon rejenerasyonu). Bu, sürekli bir proses gibi ele alınır çünkü her iki akış da aynı anda mevcuttur.

**TS4 (120-150 dk): H2, C2, C3 mevcut**

```
Sıcak akışlar:  H2: 80→25°C, CP=3 kW/°C,  Q=165 kW
Soğuk akışlar:  C2: 15→80°C, CP=2.5 kW/°C, Q=162.5 kW
                C3: 20→60°C, CP=1 kW/°C,    Q=40 kW

Toplam soğuk ihtiyaç = 162.5 + 40 = 202.5 kW
Toplam sıcak arz     = 165 kW

ΔTmin = 5°C ile pinch analizi:
  QH,min = 47.5 kW
  QC,min = 10 kW
  Pinch = 25°C (sıcak) / 20°C (soğuk)
```

### 2.4 Bileşik Zaman Dilimleri (Composite Time Slices)

Tüm zaman dilimleri birleştirilerek döngü bazında toplam hedefler hesaplanır:

```
Zaman Dilimi | Süre [dk] | QH,min [kW] | QC,min [kW] | QH,min·t [kJ]  | QC,min·t [kJ]
─────────────────────────────────────────────────────────────────────────────────────────
TS1          |    60     |    45        |     5        |  162,000        |   18,000
TS2          |    30     |    40        |     0        |   72,000        |        0
TS3          |    30     |   105        |     0        |  189,000        |        0
TS4          |    30     |    47.5      |    10        |   85,500        |   18,000
TS5          |    30     |    40        |   115        |   72,000        |  207,000
TS6          |    60     |    40        |     0        |  144,000        |        0
─────────────────────────────────────────────────────────────────────────────────────────
TOPLAM       |   240     |    —        |     —        |  724,500        |  243,000
```

Döngü başına toplam dış ısıtma ihtiyacı: 724,500 kJ = 201.25 kWh
Döngü başına toplam dış soğutma ihtiyacı: 243,000 kJ = 67.5 kWh

### 2.5 Zaman Dilimi Modelinin Avantaj ve Dezavantajları

| Avantaj | Dezavantaj |
|---|---|
| Her dilimde tam pinch analizi yapılır | Çok sayıda dilim oluşabilir |
| Doğru entegrasyon hedefleri verir | TES boyutlandırma için ek analiz gerekir |
| Zamansal uyumsuzlukları tespit eder | Karmaşık proseslerde hesap yükü artar |
| Gerçekçi sonuçlar üretir | Yazılım desteği genellikle gereklidir |

---

## 3. Zaman Ortalama Modeli (Time Average Model — TAM)

### 3.1 Temel Kavram

Zaman Ortalama Modeli, tüm akışların ısı yüklerini batch döngüsü üzerinden ortalamasını alarak tek bir sürekli proses gibi ele alır. Bu yaklaşım, standart pinch analizinin doğrudan uygulanmasına olanak tanır.

### 3.2 Hesaplama Yöntemi

Her akışın zaman-ortalama ısı yükü (time-averaged heat duty) şöyle hesaplanır:

```
Q̄ = Q_akış × (t_akış / t_döngü)
```

Burada:
- Q̄: Zaman-ortalama ısı yükü [kW]
- Q_akış: Akışın anlık ısı yükü [kW]
- t_akış: Akışın mevcut olduğu süre [dk]
- t_döngü: Toplam batch döngü süresi [dk]

### 3.3 Referans Problem İçin TAM Uygulaması

```
Akış | Q [kW] | t_akış [dk] | t_döngü [dk] | Q̄ [kW]
─────────────────────────────────────────────────────────
H1   |  340   |     60      |     240       |  85.0
H2   |  165   |     60      |     240       |  41.25
C1   |  340   |     60      |     240       |  85.0
C2   |  162.5 |     60      |     240       |  40.625
C3   |   40   |    240      |     240       |  40.0
```

Not: H2 ve C2 akışlarının mevcut olduğu zaman aralıkları farklıdır (H2: 120-180, C2: 90-150), ancak her ikisinin toplam süresi 60 dk'dır.

TAM ile standart pinch analizi uygulanır:

```
Zaman-ortalama akışlar:
  H1̄: 72→4°C,   CP̄=1.25 kW/°C   (5×60/240)
  H2̄: 80→25°C,  CP̄=0.75 kW/°C   (3×60/240)
  C1̄: 4→72°C,   CP̄=1.25 kW/°C   (5×60/240)
  C2̄: 15→80°C,  CP̄=0.625 kW/°C  (2.5×60/240)
  C3̄: 20→60°C,  CP̄=1.0 kW/°C    (1×240/240)

Toplam sıcak arz (ortalama)  = 85.0 + 41.25 = 126.25 kW
Toplam soğuk ihtiyaç (ortalama) = 85.0 + 40.625 + 40.0 = 165.625 kW

ΔTmin = 5°C ile pinch analizi:
  QH,min ≈ 45.5 kW (ortalama)
  QC,min ≈ 6.125 kW (ortalama)
```

### 3.4 TAM Ne Zaman Uygun?

TAM, aşağıdaki koşullarda makul sonuçlar verir:

1. **Yüksek zamansal örtüşme:** Akışların büyük bölümü eş zamanlı mevcut olduğunda
2. **Kısa batch döngüleri:** Döngü süresi eşanjör zaman sabitlerine göre kısa olduğunda
3. **Ön fizibilite:** Detaylı zaman dilimi analizinden önce hızlı değerlendirme gerektiğinde
4. **Düşük TES maliyeti:** Termal depolamanın ekonomik olarak uygulanabilir olduğu durumlarda

### 3.5 TAM'ın Sınırlamaları

| Sınırlama | Sonuç |
|---|---|
| Zamansal uyumsuzlukları görmezden gelir | TES ihtiyacını hafife alabilir |
| Ortalama pinch, gerçek pinch'ten farklı olabilir | Yanlış eşanjör tasarımına yol açabilir |
| Eş zamanlı olmayan akışları eşleştirebilir | Fiziksel olarak uygulanamayan tasarımlar |
| Pik yükleri maskeleyebilir | Utility yetersiz kalabilir |

### 3.6 TAM vs Zaman Dilimi Modeli Karşılaştırması

```
                  TAM          Zaman Dilimi
  Doğruluk:      Düşük-Orta   Yüksek
  Hız:           Hızlı        Yavaş
  TES analizi:   Dolaylı      Doğrudan
  Yazılım:       Standart     Özel gerekli
  Kullanım:      Ön tasarım   Detaylı tasarım
```

---

## 4. Termal Enerji Depolama — TES (Thermal Energy Storage)

### 4.1 TES Gerekliliği

Kesikli proseslerde, ısı kaynakları ve kullanıcıları farklı zamanlarda mevcut olduğunda, ısı enerjisinin zamanda kaydırılması (time-shifting) gerekir. Bu, termal enerji depolama (TES) sistemleri ile gerçekleştirilir.

Referans problemimizde:
- H1 (0-60 dk) ile C2 (90-150 dk) arasında doğrudan eşleştirme yapılamaz
- H1'in atık ısısının bir kısmı sıcak su tankında depolanabilir ve C2'ye sonradan aktarılabilir

### 4.2 Sıcak ve Soğuk Depolama Tankları (Hot/Cold Storage Tanks)

TES sistemi genellikle iki tank içerir:

```
                   Isı yüklemesi                  Isı boşaltması
                   (t = 0-60 dk)                  (t = 90-150 dk)

  H1 (72°C) ──→ [Sıcak Eşanjör] ──→ H1 (çıkış)
                      │
                      ↓ (sıcak su)
               ┌──────────────┐
               │  SICAK TANK  │
               │  T = 65°C    │       ──→ [Soğuk Eşanjör] ──→ C2 (80°C)
               │  V = ? m³    │                  ↑
               └──────────────┘           (soğuk su)
                      ↑              ┌──────────────┐
                      └───────────── │  SOĞUK TANK  │
                                     │  T = 20°C    │
                                     │  V = ? m³    │
                                     └──────────────┘
```

### 4.3 Tank Boyutlandırması (Sizing from Time-Shifted Heat Loads)

TES tank hacmi, zamanda kaydırılacak ısı miktarına göre hesaplanır:

**Formül:**
```
V_tank = Q_depolama / (ρ × Cp × ΔT_tank)
```

Burada:
- V_tank: Tank hacmi [m³]
- Q_depolama: Depolanacak ısı enerjisi [kJ]
- ρ: Su yoğunluğu [kg/m³] (~985 kg/m³ @ 60°C)
- Cp: Su özgül ısısı [kJ/(kg·°C)] (~4.18)
- ΔT_tank: Tank sıcaklık farkı [°C]

**Referans problem için hesaplama:**

H1'den C2'ye zamanda kaydırılacak ısı:
```
Q_kaydırma = 100 kW × 60 dk × 60 s/dk = 360,000 kJ

Tank sıcaklık seviyeleri:
  T_sıcak = 65°C  (H1 çıkışından 5°C düşük, ΔTmin koşulu)
  T_soğuk = 20°C  (C2 girişinden 5°C yüksek)
  ΔT_tank = 65 - 20 = 45°C

V_tank = 360,000 / (985 × 4.18 × 45) = 1.94 m³ ≈ 2.0 m³
```

Pratikte, %15-20 güvenlik faktörü eklenerek V_tank ≈ 2.4 m³ alınır.

### 4.4 Tank Sıcaklık Seviyeleri ve Katmanlaşma (Stratification)

Etkin bir TES sistemi için sıcaklık katmanlaşması (thermal stratification) kritik öneme sahiptir:

```
Tank Kesiti (Dikey):

  ───────────────── T = 65°C  (sıcak bölge — üst)
  │               │
  │  Termoklin    │ ← Sıcaklık geçiş bölgesi (0.3-0.5 m)
  │               │
  ───────────────── T = 20°C  (soğuk bölge — alt)
```

**Katmanlaşma tasarım kuralları:**
- Tank yükseklik/çap oranı (H/D): 2.5-4.0 (yüksek oranlar daha iyi katmanlaşma sağlar)
- Giriş/çıkış hızı: < 0.5 m/s (türbülansı minimize etmek için)
- Difüzör kullanımı: Radyal difüzörler önerilir
- Richardson sayısı: Ri > 3.5 hedeflenir

```
Ri = g × β × ΔT × H / v²
```

Burada:
- g: Yerçekimi ivmesi [m/s²]
- β: Termal genleşme katsayısı [1/°C]
- ΔT: Sıcak-soğuk fark [°C]
- H: Tank yüksekliği [m]
- v: Giriş hızı [m/s]

### 4.5 TES Ekonomik Değerlendirme

| Parametre | Tipik Değer | Birim |
|---|---|---|
| Tank yatırım maliyeti | 500-1,500 | EUR/m³ |
| Eşanjör maliyeti (ek) | 200-500 | EUR/kW |
| Isı kaybı (izolasyonlu) | 1-3 | %/gün |
| Ekonomik ömür | 15-25 | yıl |
| Tipik geri ödeme süresi | 1.5-4 | yıl |

---

## 5. Üretim Programı Optimizasyonu (Production Schedule Optimization)

### 5.1 Temel Kavram

Üretim programının yeniden düzenlenmesi (rescheduling), ısı kaynakları ve kullanıcıları arasındaki zamansal örtüşmeyi artırarak TES ihtiyacını azaltabilir veya ortadan kaldırabilir. Bu, sıfır yatırımlı bir enerji tasarrufu stratejisidir.

### 5.2 Gantt Diyagramı Analizi (Gantt Chart Analysis)

Referans problemin mevcut ve optimize edilmiş üretim programları:

**Mevcut program:**
```
Operasyon    0    30    60    90   120   150   180   210   240 [dk]
             |     |     |     |     |     |     |     |     |
Pastöriz. ██████████████████████
Soğutma   ██████████████████████
Dolum                    ████████████████
CIP Hazır                       ████████████
CIP Yıkam                             ████████████████████
Paketleme              ████████████████████████████████
             |     |     |     |     |     |     |     |     |
```

**Optimize edilmiş program (örtüşme maksimize edilmiş):**
```
Operasyon    0    30    60    90   120   150   180   210   240 [dk]
             |     |     |     |     |     |     |     |     |
CIP Hazır ████████████
CIP Yıkam       ████████████████████
Pastöriz.             ██████████████████████
Soğutma              ██████████████████████
Dolum                                ████████████████
Paketleme                           ████████████████████████
             |     |     |     |     |     |     |     |     |
```

### 5.3 Enerji Tüketimine Etkisi

Üretim programı optimizasyonu ile elde edilen iyileştirmeler:

```
Karşılaştırma:

Parametre                     | Mevcut    | Optimize  | Tasarruf
──────────────────────────────────────────────────────────────────
H-C zamansal örtüşme          | %25       | %65       | —
Doğrudan entegrasyon [kWh]    | 35        | 82        | +47 kWh
TES ihtiyacı [kWh]            | 55        | 18        | -37 kWh
TES tank hacmi [m³]           | 2.4       | 0.8       | -1.6 m³
Dış ısıtma ihtiyacı [kWh]    | 201       | 152       | -49 kWh (%24)
Dış soğutma ihtiyacı [kWh]   | 67.5      | 48        | -19.5 kWh (%29)
```

### 5.4 Programlama Kısıtları

Üretim programı optimizasyonu yapılırken aşağıdaki kısıtlar göz önünde bulundurulmalıdır:

1. **Sıralama kısıtları (Precedence):** Pastörizasyon, dolumdan önce tamamlanmalıdır
2. **Ekipman paylaşımı (Equipment sharing):** Aynı tank iki işlem için aynı anda kullanılamaz
3. **Temizlik gereksinimleri (CIP):** Gıda güvenliği nedeniyle CIP zamanı kısaltılamaz
4. **Depolama kapasitesi:** Ara ürün depolama tankı kapasitesi sınırlıdır
5. **İş gücü:** Vardiya saatleri ve personel mevcudiyeti
6. **Müşteri termin tarihleri:** Teslimat programları bozulamaz

---

## 6. Kesikli Pinch Analizi Adımları (Batch Pinch Analysis Steps)

### 6.1 Tam Metodoloji

Kesikli proses ısı entegrasyonu için sistematik yaklaşım aşağıdaki adımlardan oluşur:

**Adım 1: Veri Toplama (Data Collection)**
- Tüm ısı kaynakları ve kullanıcılarını tanımla
- Her akışın sıcaklık, debi, CP ve ısı yükünü belirle
- Her akışın başlangıç ve bitiş zamanlarını kaydet
- Batch döngü süresini belirle
- Proses akış diyagramını (PFD) çiz

**Adım 2: Gantt Diyagramı Oluşturma**
- Tüm proses operasyonlarını zaman ekseninde göster
- Isı kaynakları ve kullanıcılarını işaretle
- Zamansal örtüşmeleri tespit et

**Adım 3: Zaman Dilimlerini Belirle**
- Akış başlangıç/bitiş zamanlarından dilimleri oluştur
- Her dilimde mevcut akışları listele

**Adım 4: Zaman Dilimi Pinch Analizi**
- Her dilim için standart pinch analizi uygula
- QH,min ve QC,min değerlerini hesapla
- Pinch noktalarını belirle

**Adım 5: TAM ile Doğrulama**
- Zaman-ortalama yüklerle basitleştirilmiş analiz yap
- Sonuçları Zaman Dilimi Modeli ile karşılaştır

**Adım 6: TES Potansiyelini Değerlendir**
- Zamansal uyumsuzlukları tespit et
- Depolanacak ısı miktarını hesapla
- Tank boyutlandırması yap

**Adım 7: Üretim Programını Optimize Et**
- Zamansal örtüşmeyi artıracak yeniden düzenleme seçeneklerini değerlendir
- Proses kısıtlarını kontrol et
- Optimize edilmiş programın enerji etkisini hesapla

**Adım 8: Eşanjör Ağı Tasarımı (HEN Design)**
- Doğrudan eşleştirme yapılabilecek akış çiftlerini belirle
- TES gerektiren eşleştirmeleri tasarla
- Grid diyagramını çiz

**Adım 9: Ekonomik Değerlendirme**
- Eşanjör ve TES yatırım maliyetlerini hesapla
- Yıllık enerji tasarrufunu hesapla
- Geri ödeme süresini belirle (NPV, IRR)

**Adım 10: Uygulama ve Doğrulama**
- Pilot uygulama ile doğrula
- Tam ölçekli kurulum
- Ölçüm ve izleme (M&V)

### 6.2 Karar Akış Diyagramı

```
                    [Başla]
                       │
                       ▼
            ┌──────────────────┐
            │ Veri topla:      │
            │ akışlar, zamanlar│
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Gantt diyagramı  │
            │ oluştur          │
            └────────┬─────────┘
                     │
                     ▼
          ┌────────────────────┐      Evet    ┌─────────────────┐
          │ Tüm akışlar eş    │─────────────→ │ Standart sürekli│
          │ zamanlı mı?        │              │ pinch analizi    │
          └────────┬───────────┘              └─────────────────┘
                   │ Hayır
                   ▼
          ┌────────────────────┐
          │ Ön değerlendirme:  │
          │ TAM analizi yap    │
          └────────┬───────────┘
                   │
                   ▼
          ┌────────────────────┐      Düşük   ┌─────────────────┐
          │ TES potansiyeli    │─────────────→ │ Yalnızca program│
          │ yüksek mi?         │              │ optimizasyonu    │
          └────────┬───────────┘              └─────────────────┘
                   │ Yüksek
                   ▼
          ┌────────────────────┐
          │ Zaman Dilimi       │
          │ detaylı analiz yap │
          └────────┬───────────┘
                   │
                   ▼
          ┌────────────────────┐
          │ TES boyutlandırması│
          │ + HEN tasarımı     │
          └────────┬───────────┘
                   │
                   ▼
          ┌────────────────────┐
          │ Ekonomik analiz    │
          │ ve uygulama planı  │
          └────────────────────┘
```

---

## 7. Endüstriyel Uygulamalar (Industrial Applications)

### 7.1 Süt Ürünleri Fabrikası (Dairy)

Süt işleme tesisleri, kesikli pinch analizinin en yaygın uygulama alanlarından biridir.

```
Tipik süt fabrikası batch döngüsü:

Operasyon          | Sıcaklık [°C] | Süre [dk] | Tip   | Q [kW]
───────────────────────────────────────────────────────────────────
Pastörizasyon      | 4 → 72        | 60        | Soğuk | 340
Pastörizasyon soğ. | 72 → 4        | 60        | Sıcak | 340
UHT ısıtma        | 72 → 140      | 30        | Soğuk | 510
UHT soğutma       | 140 → 20      | 30        | Sıcak | 900
CIP yıkama (sıcak)| 15 → 85       | 45        | Soğuk | 350
CIP atık su       | 85 → 30       | 45        | Sıcak | 275

Sonuçlar:
  Mevcut enerji tüketimi: 850 kWh/batch
  Entegrasyon sonrası:    520 kWh/batch
  Tasarruf: %39
  TES tank hacmi: 3.5 m³
  Geri ödeme: 2.2 yıl
```

### 7.2 Bira Fabrikası (Brewery)

Bira üretimi, kaynatma ve soğutma aşamalarının zamansal uyumsuzluğu nedeniyle TES'ten önemli fayda sağlar.

```
Tipik bira fabrikası batch döngüsü:

Operasyon          | Sıcaklık [°C] | Süre [dk] | Tip   | Q [kW]
───────────────────────────────────────────────────────────────────
Şıra ısıtma       | 20 → 100      | 90        | Soğuk | 800
Şıra kaynatma     | 100 → 100     | 90        | Soğuk | 1,200
Şıra soğutma      | 100 → 12      | 30        | Sıcak | 2,200
CIP ısıtma        | 15 → 80       | 45        | Soğuk | 325
CIP atık su       | 80 → 25       | 45        | Sıcak | 275
Fermantasyon soğ.  | 12 → 8        | 7,200     | Sıcak | 15

Sonuçlar:
  Mevcut enerji tüketimi: 1,450 kWh/batch (kaynatma hariç)
  Entegrasyon sonrası:    890 kWh/batch
  Tasarruf: %38
  TES tank hacmi: 8.0 m³ (sıcak su @ 85°C)
  Geri ödeme: 1.8 yıl
```

### 7.3 Tekstil Boyama Tesisi (Dyeing)

Tekstil boyama, çok sayıda küçük batchle çalışır ve boyama banyosu atık suyu önemli bir ısı kaynağıdır.

```
Tipik tekstil boyama batch döngüsü:

Operasyon          | Sıcaklık [°C] | Süre [dk] | Tip   | Q [kW]
───────────────────────────────────────────────────────────────────
Banyo hazırlama    | 15 → 60       | 20        | Soğuk | 225
Boyama ısıtma      | 60 → 130      | 45        | Soğuk | 700
Boyama tutma       | 130 → 130     | 60        | —     | —
Boyama soğutma     | 130 → 70      | 30        | Sıcak | 600
Durulama (sıcak)   | 15 → 70       | 20        | Soğuk | 275
Atık su boşaltma   | 70 → 25       | 15        | Sıcak | 450
Durulama (soğuk)   | 15 → 15       | 15        | —     | —

Sonuçlar:
  Mevcut enerji tüketimi: 620 kWh/batch
  Entegrasyon sonrası:    400 kWh/batch
  Tasarruf: %35
  TES tank hacmi: 5.0 m³
  Geri ödeme: 2.5 yıl
```

### 7.4 İlaç Fabrikası (Pharmaceutical)

İlaç üretimi, sıkı GMP (Good Manufacturing Practice) gereksinimleri nedeniyle ısı entegrasyonunda özel dikkat gerektirir.

```
Tipik ilaç fabrikası batch döngüsü:

Operasyon          | Sıcaklık [°C] | Süre [dk] | Tip   | Q [kW]
───────────────────────────────────────────────────────────────────
Reaktör ısıtma     | 20 → 80       | 60        | Soğuk | 150
Reaksiyon (egzot.) | 80 → 80       | 120       | Sıcak | 50
Reaktör soğutma    | 80 → -5       | 90        | Sıcak | 213
Kristalizasyon     | -5 → -5       | 180       | Sıcak | 25
WFI ısıtma         | 15 → 80       | 30        | Soğuk | 163
CIP/SIP steriliz.  | 20 → 121      | 45        | Soğuk | 303
CIP atık           | 121 → 30      | 30        | Sıcak | 455

Sonuçlar:
  Mevcut enerji tüketimi: 480 kWh/batch
  Entegrasyon sonrası:    320 kWh/batch
  Tasarruf: %33
  TES tank hacmi: 2.0 m³ (GMP uyumlu paslanmaz çelik)
  Geri ödeme: 3.5 yıl (yüksek malzeme maliyeti nedeniyle)
```

### 7.5 Sektörel Karşılaştırma Tablosu

| Sektör | Tipik Tasarruf [%] | TES Hacmi [m³/MW] | Geri Ödeme [yıl] | Karmaşıklık |
|---|---|---|---|---|
| Süt ürünleri (Dairy) | 30-45 | 3-6 | 1.5-3 | Orta |
| Bira (Brewery) | 30-40 | 5-10 | 1.5-2.5 | Orta |
| Tekstil boyama (Dyeing) | 25-40 | 4-8 | 2-4 | Yüksek |
| İlaç (Pharmaceutical) | 25-35 | 2-4 | 3-5 | Çok yüksek |
| Kağıt (Pulp & Paper) | 15-25 | 8-15 | 2-4 | Orta |
| Gıda konserve (Canning) | 20-35 | 3-7 | 1.5-3 | Düşük-Orta |

---

## 8. Zorluklar ve Çözümler (Challenges and Solutions)

### 8.1 Değişken Batch Boyutları (Variable Batch Sizes)

**Zorluk:** Aynı ürün için farklı sipariş miktarlarına göre batch boyutları değişebilir. Bu, ısı yüklerinin tahminini zorlaştırır.

**Çözüm:**
1. **İstatistiksel yaklaşım:** Son 6-12 aylık üretim verilerinden ortalama ve standart sapma hesapla
2. **Tasarım noktası:** Ortalama batch boyutunun %75-85'i için tasarla (aşırı boyutlandırmayı önle)
3. **Modüler TES:** Birden fazla küçük tank kullanarak esneklik sağla
4. **Bypass hatları:** Küçük batchlerde eşanjörlerin bypass edilebilmesi

```
Tasarım yaklaşımı:

  Q_tasarım = Q_ortalama + 0.5 × σ_Q

  Burada σ_Q = ısı yükünün standart sapması

  Örnek: Q_ort = 300 kW, σ_Q = 60 kW
  Q_tasarım = 300 + 0.5 × 60 = 330 kW
```

### 8.2 Çoklu Ürünler (Multiple Products)

**Zorluk:** Aynı üretim hattında farklı ürünler işlendiğinde her ürünün sıcaklık profili ve zamanlaması farklıdır.

**Çözüm:**
1. **Dominant ürün yaklaşımı:** En yüksek üretim hacmine sahip ürün için optimize et
2. **Ağırlıklı ortalama:** Ürün dağılımına göre ağırlıklı ısı yükleri hesapla
3. **Kampanya bazlı analiz:** Her ürün kampanyası için ayrı optimizasyon yap
4. **Esnek TES:** Farklı sıcaklık seviyelerinde çalışabilen çok-tanklı sistem

```
Ağırlıklı ortalama hesabı:

  Q̄_toplam = Σ (f_i × Q_i)

  Burada:
    f_i = Ürün i'nin üretim frekansı (yıllık batch sayısı / toplam batch)
    Q_i = Ürün i'nin batch ısı yükü [kW]

  Örnek:
    Ürün A: f=0.5, Q=300 kW  → 150 kW
    Ürün B: f=0.3, Q=450 kW  → 135 kW
    Ürün C: f=0.2, Q=200 kW  →  40 kW
    Q̄_toplam = 325 kW
```

### 8.3 Temizlik Gereksinimleri (Cleaning Requirements — CIP/SIP)

**Zorluk:** CIP (Clean-In-Place) ve SIP (Sterilize-In-Place) işlemleri hem ısı tüketir hem de operasyonlar arasında bekleme süreleri yaratır.

**Çözüm:**
1. **CIP ısı geri kazanımı:** CIP atık suyundan ısı geri kazanımı (genellikle %40-60 mümkün)
2. **CIP sıcak su tankı:** CIP çözeltisi sıcak tutularak ön ısıtma enerjisi azaltılır
3. **CIP programı optimizasyonu:** CIP zamanlamasını diğer ısı kaynakları ile senkronize et
4. **Cross-contamination riski:** Gıda/ilaç sektörlerinde ısı eşanjörlerinin ürünle doğrudan temas etmemesi sağlanmalı

### 8.4 Fouling ve Bakım

**Zorluk:** Batch proseslerde sık ürün değişimi eşanjörlerde fouling riskini artırır.

**Çözüm:**
1. **Fouling faktörü:** Tasarımda %15-25 ek alan ekle
2. **Kolay temizlenebilir eşanjörler:** Plakalı eşanjörler tercih et (sökülebilir tip)
3. **Online temizleme:** CIP döngüsü sırasında eşanjör temizliği
4. **Fouling monitörü:** Basınç düşüşü ve sıcaklık izleme ile proaktif bakım

### 8.5 Kontrol ve Otomasyon

**Zorluk:** Kesikli proseslerde akışlar ve sıcaklıklar dinamik olarak değişir; kontrol sistemi bu değişikliklere uyum sağlamalıdır.

**Çözüm:**
1. **Batch yönetim sistemi (BMS):** ISA-88 standardına uygun batch kontrol
2. **Vana sıralama (Valve sequencing):** PLC tabanlı otomatik vana yönlendirme
3. **TES seviye kontrolü:** Tank doluluk ve sıcaklık izleme
4. **Prediktif kontrol (MPC):** İleri kontrol algoritmaları ile sıcaklık optimizasyonu

### 8.6 Zorluk-Çözüm Özet Tablosu

| Zorluk | Çözüm Stratejisi | Karmaşıklık | Maliyet Etkisi |
|---|---|---|---|
| Değişken batch boyutu | Modüler TES + bypass | Orta | +%10-15 yatırım |
| Çoklu ürünler | Ağırlıklı ortalama + esnek TES | Yüksek | +%15-25 yatırım |
| CIP/SIP gereksinimleri | CIP ısı geri kazanımı | Düşük | Tasarruf artışı |
| Fouling | Plakalı eşanjör + bakım planı | Düşük | +%5-10 yatırım |
| Kontrol karmaşıklığı | BMS + PLC otomasyon | Yüksek | +%20-30 yatırım |
| Mevsimsel değişkenlik | Çok modlu TES tasarımı | Orta | +%10-20 yatırım |

---

## Sayısal Örnek: Tam Batch Pinch Analizi

Referans süt fabrikası problemi için tam çözüm:

```
Girdi Özeti:
  6 akış, 4 saatlik döngü, ΔTmin = 5°C

Zaman Dilimi Modeli Sonuçları:
  Toplam döngü ısıtma ihtiyacı:  724.5 MJ = 201.25 kWh
  Toplam döngü soğutma ihtiyacı: 243.0 MJ = 67.5 kWh
  Doğrudan entegrasyon potansiyeli: 120 kWh
  TES ile ek entegrasyon: 35 kWh
  Toplam tasarruf: 155 kWh/batch (%42)

TAM Sonuçları:
  Ortalama ısıtma hedefi: 45.5 kW × 4 saat = 182 kWh
  Ortalama soğutma hedefi: 6.125 kW × 4 saat = 24.5 kWh
  Fark (TAM vs Zaman Dilimi): %9.5 — kabul edilebilir

Ekonomik Analiz:
  Yıllık batch sayısı: 5 batch/gün × 300 gün = 1,500 batch
  Yıllık enerji tasarrufu: 155 × 1,500 = 232,500 kWh
  Doğalgaz birim fiyatı: 0.04 EUR/kWh
  Yıllık parasal tasarruf: 232,500 × 0.04 = 9,300 EUR

  Yatırım kalemi                | Maliyet [EUR]
  ─────────────────────────────────────────────
  Plakalı eşanjörler (3 adet)  |   6,500
  TES tankı (2.4 m³, SS304)    |   4,800
  Boru, vana, izolasyon         |   3,200
  Otomasyon (PLC, sensör)       |   4,500
  Montaj ve devreye alma        |   3,000
  ─────────────────────────────────────────────
  TOPLAM                        |  22,000

  Basit geri ödeme: 22,000 / 9,300 = 2.4 yıl
  NPV (10 yıl, %8 iskonto): 40,400 EUR
  IRR: %38
```

---

## İlgili Dosyalar

- [Pinch Analizi Temelleri](fundamentals.md) — Linnhoff metodolojisi, MER hedefleri, 3 altın kural
- [Total Site Analizi](total_site.md) — Çok-tesisli entegrasyon, site profilleri
- [Utility Sistemleri](utility_systems.md) — Çoklu utility seviyeleri, CHP, ısı pompası
- [Pratik Uygulama Rehberi](practical_guide.md) — Proje yönetimi, veri toplama, uygulama
- [Fabrika Isı Entegrasyonu](../heat_integration.md) — Kaynak-kullanım eşleştirme
- [Atık Isı Geri Kazanımı](../waste_heat_recovery.md) — Isı geri kazanım teknolojileri
- [Çapraz Ekipman Analizi](../cross_equipment.md) — Ekipmanlar arası fırsatlar

## Referanslar

- Linnhoff, B., Hindmarsh, E., "The Pinch Design Method for Heat Exchanger Networks," Chemical Engineering Science, 38(5), pp. 745-763, 1983
- Linnhoff, B. et al., "User Guide on Process Integration for the Efficient Use of Energy," IChemE, Rugby, UK, 1994
- Obeng, E.D.A., Ashton, G.J., "On Pinch Technology Based Procedures for the Design of Batch Process Heat Recovery Systems," Chemical Engineering Research and Design, 66(3), pp. 255-268, 1988
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," 2nd Edition, Butterworth-Heinemann, 2007
- Klemes, J.J. (Ed.), "Handbook of Process Integration: Minimisation of Energy and Water Use, Waste and Emissions," Woodhead Publishing, Cambridge, 2013
- Vaselenak, J.A., Grossmann, I.E., Westerberg, A.W., "Heat Integration in Batch Processing," Industrial & Engineering Chemistry Process Design and Development, 25(2), pp. 357-366, 1986
- Foo, D.C.Y., El-Halwagi, M.M., Tan, R.R., "Recent Advances in Sustainable Process Design and Optimization," World Scientific, 2012
- Majozi, T., "Batch Chemical Process Integration: Analysis, Synthesis and Optimization," Springer, 2010
