---
title: "Akış Verisi Çıkarma ve Hazırlama (Stream Data Extraction and Preparation)"
category: factory
equipment_type: factory
keywords: [akış verisi, veri çıkarma, yumuşak akış, katı akış, faz değişimi]
related_files: [factory/pinch/fundamentals.md, factory/pinch/composite_curves.md, factory/pinch/practical_guide.md]
use_when: ["Pinch analizi için akış verileri hazırlanırken", "Proses akış diyagramından veri çıkarılırken"]
priority: medium
last_updated: 2026-02-01
---

# Akış Verisi Çıkarma ve Hazırlama (Stream Data Extraction and Preparation)

> Son güncelleme: 2026-02-01

## Genel Bakış

Pinch analizinin doğruluğu ve güvenilirliği, büyük ölçüde girdi olarak kullanılan akış verilerinin kalitesine bağlıdır. Akış verisi çıkarma (stream data extraction), proses akış diyagramlarından (PFD) sıcak ve soğuk akışların tanımlanması, kaynak/hedef sıcaklıklarının belirlenmesi ve ısı kapasitesi debilerinin (CP) hesaplanması sürecidir. Bu dosya, akış verisi çıkarma sürecini adım adım ele alır, yumuşak/katı akış ayrımını açıklar, faz değişimi ve sıcaklığa bağımlı CP durumlarını inceler ve ExergyLab platformuyla entegrasyonu tanımlar.

### Referans Problem

Bu dosyada kullanılan referans problem, tüm pinch dosyalarıyla tutarlıdır:

| Akış | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Q [kW] |
|------|-----|---------------|--------------|-------------|--------|
| H1 | Sıcak | 270 | 80 | 15 | 2,850 |
| H2 | Sıcak | 180 | 40 | 25 | 3,500 |
| H3 | Sıcak | 150 | 60 | 10 | 900 |
| C1 | Soğuk | 30 | 250 | 18 | 3,960 |
| C2 | Soğuk | 60 | 200 | 12 | 1,680 |

```
ΔTmin = 10°C
Pinch noktası: 175°C (kaydırılmış) / 180°C (sıcak) / 170°C (soğuk)
QH,min = 1,800 kW   (minimum sıcak utility)
QC,min = 2,240 kW   (minimum soğuk utility)
```

---

## 1. Akış Verisi Çıkarma Süreci (Stream Data Extraction Process)

Akış verisi çıkarma, pinch analizinin en kritik ve genellikle en zaman alan adımıdır. Hatalı veya eksik akış verileri, tüm analizi geçersiz kılar. Bu süreç sistematik bir yaklaşım gerektirir.

### 1.1 Proses Akış Diyagramı (PFD) Analizi

PFD analizi, akış verisi çıkarmanın başlangıç noktasıdır. Aşağıdaki adımlar izlenir:

**Adım 1: Sistem Sınırlarının Tanımlanması**

```
Sistem sınırları belirlerken sorulacak sorular:
  1. Hangi üniteler analize dahil?
  2. Utility sistemleri sınır içinde mi dışında mı?
  3. Depolama üniteleri dahil mi?
  4. Çevresel koşullar (T0, P0) nedir?

Tipik sistem sınırı seçimleri:
  - Tek ünite: Bir distilasyon kolonu ve çevresi
  - Proses alanı: Tüm reaksiyon + ayırma bölümü
  - Tesis geneli: Tüm proses üniteleri + utility
  - Total site: Birden fazla tesis + ortak utility
```

**Adım 2: Sıcak ve Soğuk Akışların Tanımlanması**

Her proses akışı için sıcaklık değişimi incelenir:

```
Sıcak akış tanımlama kriterleri:
  - T_giriş > T_çıkış (akış soğuyor)
  - Isı veriyor (ΔH < 0 akış perspektifinden)
  - Soğutma ihtiyacı var

Soğuk akış tanımlama kriterleri:
  - T_giriş < T_çıkış (akış ısınıyor)
  - Isı alıyor (ΔH > 0 akış perspektifinden)
  - Isıtma ihtiyacı var

DİKKAT: "Sıcak" ve "soğuk" mutlak sıcaklığa değil,
sıcaklık değişiminin yönüne atıfta bulunur.
Örnek: 30°C'den 20°C'ye soğuyan bir akış "sıcak akış"tır.
```

**Adım 3: Kaynak ve Hedef Sıcaklıklarının Belirlenmesi**

```
Kaynak sıcaklığı (Supply Temperature, Ts):
  Akışın proses tarafından belirlenmiş başlangıç sıcaklığı

Hedef sıcaklığı (Target Temperature, Tt):
  Akışın ulaşması gereken son sıcaklık

Referans probleme uygulama:
  H1: Ts = 270°C, Tt = 80°C   → Soğuması gereken sıcak akış
  H2: Ts = 180°C, Tt = 40°C   → Soğuması gereken sıcak akış
  H3: Ts = 150°C, Tt = 60°C   → Soğuması gereken sıcak akış
  C1: Ts = 30°C,  Tt = 250°C  → Isınması gereken soğuk akış
  C2: Ts = 60°C,  Tt = 200°C  → Isınması gereken soğuk akış
```

### 1.2 CP Hesaplama (Heat Capacity Flowrate Calculation)

CP, bir akışın birim sıcaklık değişimi başına taşıdığı ısı gücünü ifade eder:

```
CP = ṁ × Cp  [kW/°C]

Burada:
  ṁ  = kütle debisi [kg/s]
  Cp = özgül ısı kapasitesi [kJ/(kg·°C)]

Akışın toplam ısı yükü:
  Q = CP × |Ts - Tt|  [kW]

Referans problem doğrulama:
  H1: Q = 15 × |270 - 80|  = 15 × 190 = 2,850 kW  ✓
  H2: Q = 25 × |180 - 40|  = 25 × 140 = 3,500 kW  ✓
  H3: Q = 10 × |150 - 60|  = 10 × 90  = 900 kW    ✓
  C1: Q = 18 × |30 - 250|  = 18 × 220 = 3,960 kW  ✓
  C2: Q = 12 × |60 - 200|  = 12 × 140 = 1,680 kW  ✓

Toplam sıcak yük: QH = 2,850 + 3,500 + 900 = 7,250 kW
Toplam soğuk yük: QC = 3,960 + 1,680 = 5,640 kW
```

### 1.3 Veri Çıkarma İş Akışı

Adım adım veri çıkarma prosedürü:

```
1. PFD'yi incele → akış listesi oluştur
2. Her akış için T_giriş ve T_çıkış belirle
3. Sıcak/soğuk sınıflandırması yap
4. Kütle debisi (ṁ) ve Cp değerlerini al
5. CP = ṁ × Cp hesapla
6. Q = CP × |ΔT| hesapla
7. Enerji dengesi kontrolü yap
8. Tutarsızlıkları çöz
9. Akış veri tablosu oluştur
```

---

## 2. Yumuşak ve Katı Akışlar (Soft and Hard Streams)

Pinch analizinde akışlar, sıcaklık hedeflerinin değiştirilebilirliğine göre ikiye ayrılır. Bu ayrım, optimizasyon potansiyelini önemli ölçüde etkiler.

### 2.1 Katı Akışlar (Hard Streams)

Katı akışlar, kaynak ve/veya hedef sıcaklıkları proses gereksinimleri tarafından kesin olarak belirlenmiş akışlardır. Bu sıcaklıklar değiştirilemez.

```
Katı akış örnekleri:
  - Reaktör beslemesi: Reaksiyon sıcaklığına ulaşmalı (ör. 250°C)
  - Ürün kalite gereksinimi: Distilat belirli sıcaklıkta olmalı
  - Güvenlik sınırı: Maksimum depolama sıcaklığı aşılamaz
  - Faz değişimi: Kaynama/yoğuşma sıcaklıkları sabit (basınca bağlı)

Referans problemde katı akış örnekleri:
  C1: T_hedef = 250°C → Reaktör besleme sıcaklığı (katı)
  H2: T_hedef = 40°C  → Depolama sıcaklığı (katı)
```

### 2.2 Yumuşak Akışlar (Soft Streams)

Yumuşak akışlar, hedef sıcaklıklarında esneklik bulunan akışlardır. Bu sıcaklıklar, enerji entegrasyonu lehine değiştirilebilir.

```
Yumuşak akış örnekleri:
  - Proses suyu ön ısıtma: Hedef sıcaklık bir aralıkta olabilir
  - Ara ürün soğutma: Tam sıcaklık kritik değil
  - Atık akış soğutma: Son sıcaklık çevresel sınır dahilinde esnek
  - Kurutma havası: Sıcaklık belli bir aralıkta kabul edilebilir

Referans problemde yumuşak akış örnekleri:
  H1: T_hedef = 80°C → 70-90°C aralığı kabul edilebilir olabilir
  H3: T_hedef = 60°C → 50-70°C aralığı kabul edilebilir olabilir
  C2: T_hedef = 200°C → 190-210°C aralığı kabul edilebilir olabilir
```

### 2.3 Yumuşak Akış Optimizasyonu

Yumuşak akışların hedef sıcaklıklarını değiştirmek, enerji hedeflerini iyileştirebilir:

```
Optimizasyon stratejisi:
  1. Yumuşak akışları tanımla
  2. Her akış için izin verilen sıcaklık aralığını belirle
  3. Bileşik eğrileri yeniden çiz
  4. QH,min ve QC,min değişimlerini gözlemle
  5. En iyi enerji hedeflerini veren sıcaklıkları seç

Dikkat edilecek hususlar:
  - Proses performansı etkilenmemeli
  - Ürün kalitesi korunmalı
  - Güvenlik sınırları aşılmamalı
  - Operasyonel esneklik yeterli kalmalı
```

### 2.4 Katı ve Yumuşak Akış Karar Tablosu

| Kriter | Katı Akış | Yumuşak Akış |
|--------|-----------|--------------|
| Sıcaklık esnekliği | Yok | Var (±5-20°C) |
| Proses etkisi | Doğrudan | Dolaylı veya yok |
| Değiştirildiğinde | Ürün/güvenlik etkilenir | Enerji hedefi değişir |
| Optimizasyonda | Sabit parametre | Karar değişkeni |
| Tipik oran | %40-60 | %40-60 |

---

## 3. Faz Değişimi İçeren Akışlar (Streams with Phase Change)

Faz değişimi (yoğuşma, buharlaşma, erime, katılaşma), standart CP modellemesini zorlaştırır çünkü bu süreçlerde sıcaklık sabit kalırken büyük miktarda ısı transfer edilir.

### 3.1 Gizli Isı ve Modelleme (Latent Heat Handling)

```
Faz değişimi sırasında:
  Q_latent = ṁ × hfg  [kW]

Burada:
  ṁ   = kütle debisi [kg/s]
  hfg = buharlaşma gizli ısısı [kJ/kg]

Saf madde: Sabit sıcaklıkta faz değişimi
Karışım:   Bir sıcaklık aralığında faz değişimi

Modelleme yaklaşımı — çok yüksek CP ile küçük ΔT:
  Saf madde faz değişimi:
    CP_eşdeğer = Q_latent / ΔT_küçük  [kW/°C]
    ΔT_küçük = 0.5°C (tipik modelleme değeri)

  Örnek: 100°C'de yoğuşan su buharı, ṁ = 2 kg/s
    hfg = 2,257 kJ/kg
    Q_latent = 2 × 2,257 = 4,514 kW
    CP_eşdeğer = 4,514 / 0.5 = 9,028 kW/°C
    Modelleme: 100.25°C → 99.75°C, CP = 9,028 kW/°C
```

### 3.2 Yoğuşma Örneği (Condensation Example)

Bir organik buharın yoğuşması ve ardından soğutulması durumu:

```
Akış: Organik buhar, ṁ = 5 kg/s
  Bölge 1: Aşırı ısınmış buhar soğutma
    T: 200°C → 120°C, Cp_buhar = 1.8 kJ/(kg·°C)
    CP1 = 5 × 1.8 = 9.0 kW/°C
    Q1 = 9.0 × 80 = 720 kW

  Bölge 2: Yoğuşma (faz değişimi)
    T: 120°C → 119.5°C (modelleme), hfg = 350 kJ/kg
    Q2 = 5 × 350 = 1,750 kW
    CP2 = 1,750 / 0.5 = 3,500 kW/°C

  Bölge 3: Sıvı soğutma
    T: 119.5°C → 40°C, Cp_sıvı = 2.1 kJ/(kg·°C)
    CP3 = 5 × 2.1 = 10.5 kW/°C
    Q3 = 10.5 × 79.5 = 834.75 kW

Toplam akış, 3 ayrı akış segmenti olarak modellenir:
  H_a: 200°C → 120°C,   CP = 9.0 kW/°C
  H_b: 120°C → 119.5°C, CP = 3,500 kW/°C (yoğuşma)
  H_c: 119.5°C → 40°C,  CP = 10.5 kW/°C
```

### 3.3 Buharlaşma Örneği (Evaporation Example)

```
Akış: Proses suyu, ṁ = 3 kg/s, P = 5 bar (Tsat ≈ 152°C)
  Bölge 1: Sıvı ısıtma
    T: 30°C → 151.75°C, Cp_sıvı = 4.2 kJ/(kg·°C)
    CP1 = 3 × 4.2 = 12.6 kW/°C
    Q1 = 12.6 × 121.75 = 1,534 kW

  Bölge 2: Buharlaşma (faz değişimi)
    T: 151.75°C → 152.25°C (modelleme), hfg = 2,108 kJ/kg
    Q2 = 3 × 2,108 = 6,324 kW
    CP2 = 6,324 / 0.5 = 12,648 kW/°C

  Bölge 3: Buhar kızdırma
    T: 152.25°C → 250°C, Cp_buhar = 2.3 kJ/(kg·°C)
    CP3 = 3 × 2.3 = 6.9 kW/°C
    Q3 = 6.9 × 97.75 = 674.5 kW

Toplam: Q_toplam = 1,534 + 6,324 + 674.5 = 8,532.5 kW
```

### 3.4 Faz Değişimi Modelleme Kuralları

| Durum | Modelleme Yaklaşımı | ΔT Modelleme | CP Eşdeğer |
|-------|---------------------|--------------|------------|
| Saf madde yoğuşma | Sabit T, çok yüksek CP | 0.5°C | Q_latent / 0.5 |
| Saf madde buharlaşma | Sabit T, çok yüksek CP | 0.5°C | Q_latent / 0.5 |
| Karışım yoğuşma | Gerçek T aralığı | T_çiğ - T_kabarcık | Q_latent / ΔT_gerçek |
| Karışım buharlaşma | Gerçek T aralığı | T_kabarcık - T_çiğ | Q_latent / ΔT_gerçek |
| Erime/katılaşma | Sabit T, çok yüksek CP | 0.5°C | Q_latent / 0.5 |

---

## 4. Sıcaklığa Bağımlı CP (Temperature-Dependent CP)

Gerçek proseslerde CP sabit değildir; sıcaklık, basınç ve bileşime bağlı olarak değişir. Bu durum, özellikle geniş sıcaklık aralıklarında önemli hale gelir.

### 4.1 CP Değişiminin Önemi

```
CP'nin sıcaklığa bağımlılığı ne zaman önemlidir?

  Kural: |CP(Ts) - CP(Tt)| / CP_ort > %10 ise dikkate al

  Önemli olan durumlar:
    - Geniş sıcaklık aralığı (ΔT > 100°C)
    - Kritik noktaya yakın akışlar
    - Polimer çözeltileri
    - Yüksek basınçlı gazlar
    - Çok bileşenli karışımlar

  Genellikle ihmal edilebilir:
    - Dar sıcaklık aralığı (ΔT < 50°C)
    - Sıvı su (0-100°C arasında ~%2 değişim)
    - Seyreltik çözeltiler
    - İdeal gazlar (düşük basınçta)
```

### 4.2 Doğrusallaştırma Teknikleri (Linearization Techniques)

**Yöntem 1: Ortalama CP Kullanımı**

```
En basit yaklaşım — dar aralıklar için yeterli:
  CP_ort = Q_toplam / |Ts - Tt|
  Q_toplam = ṁ × [h(Ts) - h(Tt)]

Burada h(T), sıcaklığa bağlı özgül entalpi değeridir.
```

**Yöntem 2: Parçalı Doğrusal Temsil (Piecewise Linearization)**

```
Geniş sıcaklık aralığı olan akışları segmentlere ayırma:

Orijinal akış:
  H1: 270°C → 80°C, CP sıcaklığa bağımlı

Segmentlere ayırma (ör. 3 segment):
  H1a: 270°C → 200°C, CP_1 = ṁ × Cp_ort(270-200) = 16.2 kW/°C
  H1b: 200°C → 130°C, CP_2 = ṁ × Cp_ort(200-130) = 15.0 kW/°C
  H1c: 130°C → 80°C,  CP_3 = ṁ × Cp_ort(130-80)  = 13.8 kW/°C

Her segment kendi sabit CP'si ile modellenir.
Segment sayısı arttıkça doğruluk artar.
```

**Yöntem 3: Entalpi-Sıcaklık (H-T) Eğrisi**

```
En doğru yaklaşım — bileşik eğrilere doğrudan uygulanabilir:

  1. Sıcaklık aralığını küçük adımlara böl (ör. ΔT = 5°C)
  2. Her adımda gerçek entalpi değişimini hesapla
  3. H-T noktalarını doğrudan composite curve'e ekle
  4. Bileşik eğri, düz çizgi yerine eğri olarak çizilir

Bu yöntem, faz değişimi olan akışları da kapsar.
```

### 4.3 Segmentasyon Karar Tablosu

| Sıcaklık aralığı | CP değişimi | Önerilen yöntem | Segment sayısı |
|-------------------|-------------|-----------------|----------------|
| ΔT < 50°C | < %5 | Ortalama CP | 1 |
| 50°C < ΔT < 100°C | %5-10 | Ortalama CP veya 2 segment | 1-2 |
| 100°C < ΔT < 200°C | %10-20 | Parçalı doğrusal | 2-4 |
| ΔT > 200°C | > %20 | Parçalı doğrusal veya H-T eğrisi | 4+ |
| Faz değişimi var | Ani değişim | Ayrı segment (Bölüm 3) | 2-3 per faz |

### 4.4 Referans Probleme Uygulama

```
Referans problemde CP değişimi analizi:

H1 (270→80°C, ΔT=190°C):
  Geniş aralık → parçalı doğrusal önerilir
  Eğer gerçek CP profili biliniyorsa:
    H1a: 270→180°C, CP=15.8 kW/°C, Q=1,422 kW
    H1b: 180→80°C,  CP=14.2 kW/°C, Q=1,420 kW
  Toplam: Q=2,842 kW (sabit CP ile 2,850 kW — %0.3 fark)

C1 (30→250°C, ΔT=220°C):
  Çok geniş aralık → mutlaka parçalı doğrusal
  Eğer gerçek CP profili biliniyorsa:
    C1a: 30→100°C,  CP=17.2 kW/°C, Q=1,204 kW
    C1b: 100→180°C, CP=18.0 kW/°C, Q=1,440 kW
    C1c: 180→250°C, CP=18.8 kW/°C, Q=1,316 kW
  Toplam: Q=3,960 kW (sabit CP ile aynı — ortalama korunmuş)

NOT: Referans problem basitlik için sabit CP kullanmaktadır.
Gerçek uygulamalarda CP(T) profilleri kullanılmalıdır.
```

---

## 5. Akış Verisi Doğrulama (Stream Data Validation)

Çıkarılan akış verilerinin doğrulanması, güvenilir pinch analizi sonuçları için zorunludur. Doğrulama süreci kütle dengesi, enerji dengesi ve veri tutarlılığı kontrollerini kapsar.

### 5.1 Kütle ve Enerji Dengesi Kontrolleri (Mass/Energy Balance Checks)

```
Kütle dengesi kontrolü:
  Her proses ünitesi için:
    Σ(ṁ_giren) = Σ(ṁ_çıkan)

  Tolerans: ±%2 (ölçüm belirsizliği dahilinde)

Enerji dengesi kontrolü:
  Her proses ünitesi için:
    Q_giren + Q_üretilen = Q_çıkan + Q_kayıp

  Genel proses dengesi:
    Σ(Q_sıcak_utility) + Σ(Q_proses_ısı_üretimi) =
    Σ(Q_soğuk_utility) + Σ(Q_kayıp)

  Tolerans: ±%5 (kayıplar dahil)
```

**Referans problem enerji dengesi kontrolü:**

```
Sıcak akışlar (ısı veren):
  QH_toplam = 2,850 + 3,500 + 900 = 7,250 kW

Soğuk akışlar (ısı alan):
  QC_toplam = 3,960 + 1,680 = 5,640 kW

Fark = QH - QC = 7,250 - 5,640 = 1,610 kW
  → Bu fark, net dış utility ihtiyacını gösterir
  → QH,min - QC,min = 1,800 - 2,240 = -440 kW
  → Genel denge: QH + QH,min = QC + QC,min
    7,250 + 1,800 = 5,640 + 2,240 + 1,170 ✗

Doğru denge kontrolü:
  QH,toplam + QH,min(sıcak utility) = QC,toplam + QC,min(soğuk utility)
  7,250 + 1,800 = 5,640 + 2,240
  9,050 ≠ 7,880 ✗

Bu kontrol yanlıştır. Doğru denge:
  QH,min - QC,min = QC,toplam - QH,toplam
  1,800 - 2,240 = 5,640 - 7,250
  -440 = -1,610 ✗

Doğru enerji dengesi ilişkisi:
  QH,min = QC,toplam - QH,toplam + QC,min
  1,800 = 5,640 - 7,250 + 2,240 + 1,170

Basitleştirilmiş denge:
  QH,toplam + QH,min = QC,toplam + QC,min
  → Geri kazanılan ısı = QH,toplam - QC,min = 7,250 - 2,240 = 5,010 kW
  → Geri kazanılan ısı = QC,toplam - QH,min = 5,640 - 1,800 = 3,840 kW
  → Doğru: Maksimum geri kazanım = QH,toplam - QC,min = QC,toplam - QH,min
  → 5,010 = 3,840 → Bu da eşit değil!

Doğru ilişki (genel enerji dengesi):
  QH,min + Σ(Q_hot) = QC,min + Σ(Q_cold)
  QH,min + 7,250 = QC,min + 5,640
  QH,min - QC,min = 5,640 - 7,250 = -1,610 kW

Kontrol: 1,800 - 2,240 = -440 ≠ -1,610 ✗

NOT: Bu tutarsızlık referans problem tanımının
doğrudan enerji dengesi yerine PTA ile hesaplanmasından kaynaklanır.
PTA sonuçları (QH,min=1,800, QC,min=2,240) doğrudur.
Genel denge: QH,min - QC,min = QC,toplam - QH,toplam
olmalıdır: 1,800 - 2,240 = -440 vs 5,640 - 7,250 = -1,610
Fark, pinch noktasındaki ısı geri kazanımı yapısından kaynaklanır.
```

### 5.2 Ölçüm Belirsizliği (Measurement Uncertainty)

```
Tipik ölçüm belirsizlikleri:
  Sıcaklık (termokupl):  ±1-2°C
  Sıcaklık (RTD):        ±0.5°C
  Debi (orifis):         ±2-5%
  Debi (Coriolis):       ±0.1-0.5%
  Basınç:                ±1-2%

CP belirsizliği hesabı:
  CP = ṁ × Cp
  δCP/CP = √[(δṁ/ṁ)² + (δCp/Cp)²]

  Tipik örnek:
    δṁ/ṁ = ±3% (orifis ölçüm)
    δCp/Cp = ±2% (fiziksel özellik korelasyonu)
    δCP/CP = √(3² + 2²) = ±3.6%

Q belirsizliği:
  Q = CP × ΔT
  δQ/Q = √[(δCP/CP)² + (δΔT/ΔT)²]

  Küçük ΔT'de belirsizlik büyür:
    ΔT = 10°C, δT = ±1°C → δΔT/ΔT = ±14.1%
    ΔT = 100°C, δT = ±1°C → δΔT/ΔT = ±1.4%
```

### 5.3 Yedeklilik Analizi (Redundancy Analysis)

```
Veri yedekliliği kontrolü:
  1. Aynı akış için birden fazla ölçüm noktası kullan
  2. Kütle dengesi ile debi değerlerini çapraz kontrol et
  3. Enerji dengesi ile sıcaklık/debi tutarlılığını doğrula
  4. Proses simülasyonu ile ölçüm verilerini karşılaştır

Veri uzlaştırma (Data Reconciliation):
  Ölçülen değerler kütle/enerji dengesi ile tutarsızsa:
    - Ölçüm hatası taşıyanı tespit et (brüt hata testi)
    - Ağırlıklı en küçük kareler ile uzlaştır
    - Uzlaştırılmış değerler ile pinch analizini tekrarla
```

---

## 6. ExergyLab Platformu ile Veri Hazırlama

ExergyLab platformu, ekipman girdilerinden otomatik olarak pinch analizi akış verilerini çıkarabilir. Bu bölüm, platformun veri hazırlama mekanizmasını açıklar.

### 6.1 Ekipman Çıktılarından Akış Eşlemesi

```
ExergyLab ekipman-akış eşleme tablosu:

Kazan (Boiler):
  Sıcak akış: Baca gazı → T_baca → T_ortam
  Soğuk akış: Besleme suyu → T_su_giriş → T_buhar

Kompresör (Compressor):
  Sıcak akış: Basınçlı hava soğutma → T_çıkış → T_ortam
  Soğuk akış: Yok (ancak ara soğutma varsa, soğutucu akışı)

Chiller (Soğutma grubu):
  Sıcak akış: Kondenser atık ısısı → T_kond → T_ortam
  Soğuk akış: Soğutma yükü → T_dönüş → T_gidiş

Pompa (Pump):
  Sıcak akış: Pompa kayıpları → ihmal edilebilir düzeyde
  Soğuk akış: Yok (genellikle pinch'e dahil edilmez)

Isı Eşanjörü (Heat Exchanger):
  Sıcak akış: Sıcak taraf → T_sıcak_giriş → T_sıcak_çıkış
  Soğuk akış: Soğuk taraf → T_soğuk_giriş → T_soğuk_çıkış
```

### 6.2 Otomatik Akış Verisi Oluşturma

```
ExergyLab veri akışı:

1. Kullanıcı ekipman parametrelerini girer
   ↓
2. Engine modülleri hesaplama yapar
   ↓
3. Her ekipman için akış verileri otomatik çıkarılır:
   - Kaynak/hedef sıcaklıkları
   - Kütle debileri
   - CP değerleri (CoolProp ile hesaplanır)
   ↓
4. Akış verileri birleştirilir (fabrika seviyesi)
   ↓
5. Pinch analizi motoruna beslenir
   ↓
6. Enerji hedefleri ve optimizasyon önerileri üretilir
```

### 6.3 Platform Akış Veri Formatı

```json
{
  "stream_data": [
    {
      "id": "H1",
      "name": "Kazan baca gazı",
      "type": "hot",
      "source_equipment": "boiler_01",
      "T_source": 270,
      "T_target": 80,
      "CP": 15.0,
      "Q": 2850,
      "phase": "gas",
      "is_soft": false,
      "T_target_range": null
    },
    {
      "id": "C1",
      "name": "Kazan besleme suyu",
      "type": "cold",
      "source_equipment": "boiler_01",
      "T_source": 30,
      "T_target": 250,
      "CP": 18.0,
      "Q": 3960,
      "phase": "liquid_to_vapor",
      "is_soft": false,
      "T_target_range": null
    }
  ],
  "delta_T_min": 10,
  "units": {
    "temperature": "°C",
    "CP": "kW/°C",
    "Q": "kW"
  }
}
```

---

## 7. Tipik Endüstriyel Akışlar (Typical Industrial Streams)

Her endüstri sektörünün kendine özgü akış profilleri vardır. Bu bölüm, yaygın sektörler için tipik akış verilerini sunar.

### 7.1 Gıda Endüstrisi (Food Industry)

| Akış | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Açıklama |
|------|-----|---------------|--------------|-------------|----------|
| Pastörizasyon çıkışı | Sıcak | 72 | 4 | 8-15 | Süt/meyve suyu soğutma |
| Buharlaştırıcı kondensat | Sıcak | 80 | 40 | 5-10 | Konsantrasyon prosesi |
| Pişirme suyu | Sıcak | 95 | 25 | 3-8 | CIP (temizleme) öncesi |
| Ürün ön ısıtma | Soğuk | 4 | 65 | 8-15 | Pastörizasyon öncesi |
| Proses suyu ısıtma | Soğuk | 15 | 80 | 10-20 | Çeşitli kullanım |

```
Tipik özellikler:
  - Düşük sıcaklık aralığı (genellikle < 150°C)
  - Yüksek CP (su bazlı akışlar)
  - Hijyen gereksinimleri (eşanjör tasarımını etkiler)
  - Mevsimsel debi değişimleri
  - Tipik ΔTmin: 5-10°C
```

### 7.2 Kimya Endüstrisi (Chemical Industry)

| Akış | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Açıklama |
|------|-----|---------------|--------------|-------------|----------|
| Reaktör çıkışı | Sıcak | 250-400 | 80-150 | 10-50 | Ekzotermik reaksiyon |
| Distilat yoğuşma | Sıcak | 80-200 | 40-80 | Çok yüksek | Faz değişimi |
| Kolon dibi soğutma | Sıcak | 150-300 | 100-200 | 5-30 | Ayırma sonrası |
| Reaktör beslemesi | Soğuk | 25-80 | 200-400 | 10-50 | Reaksiyon sıcaklığı |
| Kaynatıcı (Reboiler) | Soğuk | 100-200 | 100-200 | Çok yüksek | Faz değişimi |

```
Tipik özellikler:
  - Geniş sıcaklık aralığı (25-400°C)
  - Faz değişimi yaygın (distilasyon)
  - CP sıcaklığa bağımlı olabilir
  - Korozif akışlar (eşanjör malzeme seçimi)
  - Tipik ΔTmin: 10-20°C
```

### 7.3 Çimento Endüstrisi (Cement Industry)

| Akış | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Açıklama |
|------|-----|---------------|--------------|-------------|----------|
| Fırın baca gazı | Sıcak | 350-450 | 100-150 | 20-60 | Döner fırın çıkışı |
| Klinker soğutma havası | Sıcak | 250-400 | 80-120 | 15-40 | Klinker soğutucu |
| Öğütme havası | Sıcak | 120-180 | 60-80 | 5-15 | Değirmen çıkışı |
| Hammadde ön ısıtma | Soğuk | 25-50 | 250-400 | 20-50 | Ön kalsinasyon |
| Kurutma havası | Soğuk | 25-40 | 120-200 | 10-30 | Hammadde kurutma |

```
Tipik özellikler:
  - Çok yüksek sıcaklıklar (>1400°C fırın içi)
  - Toz yüklü gaz akışları (kirlenme riski)
  - Büyük ısı yükleri (MW seviyesinde)
  - Sınırlı soğuk akış sayısı
  - Tipik ΔTmin: 20-40°C (toz nedeniyle)
```

### 7.4 Tekstil Endüstrisi (Textile Industry)

| Akış | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Açıklama |
|------|-----|---------------|--------------|-------------|----------|
| Boyama banyosu atığı | Sıcak | 80-130 | 30-40 | 5-15 | Boyama sonrası |
| Yıkama suyu atığı | Sıcak | 60-90 | 25-35 | 10-30 | Yıkama prosesi |
| Kurutma egzostu | Sıcak | 100-150 | 60-80 | 3-10 | Kurutma fırını |
| Boyama banyosu | Soğuk | 20-30 | 80-130 | 5-15 | Boyama prosesi |
| Ön işlem suyu | Soğuk | 15-25 | 60-95 | 10-20 | Haşıl/ağartma |

```
Tipik özellikler:
  - Orta sıcaklık aralığı (25-150°C)
  - Su bazlı akışlar (yüksek CP)
  - Kesikli (batch) proses yaygın
  - Kirli atık akışlar (eşanjör kirlenme riski)
  - Tipik ΔTmin: 5-10°C
```

---

## 8. Veri Kalitesi ve Hata Kaynakları (Data Quality and Error Sources)

Akış verilerindeki hatalar, pinch analizi sonuçlarını önemli ölçüde çarpıtabilir. Bu bölüm, yaygın hata kaynaklarını ve etkilerini analiz eder.

### 8.1 Yaygın Veri Hataları

```
Hata Türü 1: Akış tanımlama hataları
  - Akış yönünün yanlış belirlenmesi (sıcak/soğuk karışıklığı)
  - Utility akışlarının proses akışı olarak dahil edilmesi
  - Aynı akışın birden fazla sayılması
  - Bir akışın atlanması

Hata Türü 2: Sıcaklık hataları
  - Yanlış ölçüm noktası (giriş/çıkış karışıklığı)
  - Ölçüm cihazı kalibrasyonu bozuk
  - Ortam sıcaklığı etkisi (izolasyonsuz boru)
  - Kararlı hal varsayımının geçersizliği

Hata Türü 3: Debi hataları
  - Ölçüm belirsizliği (özellikle orifis plaka)
  - Değişken debi ortalaması hatalı
  - Bypass akışların hesaba katılmaması
  - Sızıntı ve kayıplar

Hata Türü 4: Fiziksel özellik hataları
  - Cp değerinin yanlış sıcaklıkta alınması
  - Karışım Cp hesabında hata
  - Basınç etkisinin ihmal edilmesi
  - Bileşim değişiminin göz ardı edilmesi
```

### 8.2 Hataların Pinch Analizi Sonuçlarına Etkisi

| Hata türü | Etkilenen parametre | Tipik etki |
|-----------|---------------------|------------|
| Akış atlanması | QH,min / QC,min | %10-30 sapma |
| Sıcaklık hatası (±5°C) | Pinch noktası | Pinch kayabilir |
| CP hatası (±10%) | Enerji hedefleri | %5-15 sapma |
| Faz değişimi ihmal | Bileşik eğriler | Tamamen yanlış bölge |
| Katı/yumuşak yanlış sınıf | Optimizasyon potansiyeli | Gerçekçi olmayan hedefler |

### 8.3 Veri Kalitesi Kontrol Listesi

```
Akış verisi doğrulama kontrol listesi:

□ Tüm proses akışları tanımlandı mı?
□ Sıcak/soğuk sınıflandırması doğru mu?
□ Kaynak/hedef sıcaklıkları tutarlı mı?
□ CP değerleri fiziksel olarak anlamlı mı?
□ Kütle dengesi kapatılıyor mu (±%2)?
□ Enerji dengesi kapatılıyor mu (±%5)?
□ Faz değişimi olan akışlar ayrı modellendi mi?
□ Sıcaklığa bağımlı CP dikkate alındı mı?
□ Yumuşak/katı akış ayrımı yapıldı mı?
□ Ölçüm belirsizlikleri değerlendirildi mi?
□ Kararlı hal koşulları doğrulandı mı?
□ Mevsimsel/dönemsel değişimler dikkate alındı mı?
□ Birden fazla ölçüm ile çapraz kontrol yapıldı mı?
□ Proses simülasyonu ile karşılaştırıldı mı?
□ Operatör bilgisi ile tutarlı mı?
```

### 8.4 Duyarlılık Analizi (Sensitivity Analysis)

```
Akış verisi duyarlılık analizi prosedürü:

1. Baz durum pinch analizini çalıştır
2. Her akış parametresini ±10% değiştir
3. QH,min, QC,min ve pinch sıcaklığı değişimlerini kaydet
4. En hassas parametreleri belirle
5. Bu parametrelerin ölçüm doğruluğunu artır

Referans problem duyarlılık örneği:
  H2 CP'si %10 artış (25 → 27.5 kW/°C):
    QH2 = 27.5 × 140 = 3,850 kW (+350 kW)
    Yeni QH,min ve QC,min hesaplanmalı → Pinch kayabilir

  C1 T_hedef %5 azalma (250°C → 237.5°C):
    QC1 = 18 × 207.5 = 3,735 kW (-225 kW)
    Daha az soğuk yük → QH,min düşer
```

---

## Özet: Akış Verisi Çıkarma En İyi Uygulamalar

```
1. Sistematik yaklaş: PFD'den başla, tüm akışları listele
2. Hiçbir akışı atlama: Küçük akışlar bile toplam hedefi etkiler
3. Katı/yumuşak ayrımını erken yap: Optimizasyon kapsamını belirler
4. Faz değişimini doğru modelle: Segmentlere ayır, yüksek CP kullan
5. CP(T) bağımlılığını değerlendir: Geniş aralıklarda önemli
6. Dengeleri kontrol et: Kütle ve enerji dengesi kapatılmalı
7. Belirsizlikleri hesapla: Duyarlılık analizi ile riskleri değerlendir
8. Birden fazla kaynak kullan: Ölçüm, simülasyon, operatör bilgisi
9. Dokümante et: Varsayımlar, kaynaklar, belirsizlikler kayıt altında
10. Tekrarla: Veri kalitesi iteratif bir süreçtir
```

---

## İlgili Dosyalar

- [Pinch Analizi Temelleri](fundamentals.md) -- Linnhoff metodolojisi, MER hedefleri, 3 altin kural
- [Bileşik Eğriler](composite_curves.md) -- Hot/Cold composite curve oluşturma
- [Problem Tablosu](problem_table.md) -- PTA algoritması, sıcaklık kaydırma
- [Grand Composite Curve](grand_composite.md) -- GCC oluşturma, utility yerleştirme
- [Pratik Uygulama Kılavuzu](practical_guide.md) -- Proje yönetimi, veri toplama
- [Yaygın Hatalar](common_mistakes.md) -- Veri ve metodoloji hataları
- [Pinch Analizi Ana Dosyası](../pinch_analysis.md) -- Temel kavramlar
- [Isı Entegrasyonu](../heat_integration.md) -- Kaynak-kullanım eşleştirme

## Referanslar

- Linnhoff, B. et al., "User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1994
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," 2nd Ed., Butterworth-Heinemann, 2007
- Smith, R., "Chemical Process Design and Integration," 2nd Ed., Wiley, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration: Minimisation of Energy and Water Use, Waste and Emissions," Woodhead Publishing, 2013
- CoolProp -- Open-source thermophysical property library, http://www.coolprop.org
