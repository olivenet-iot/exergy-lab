---
title: "Yaşam Döngüsü Maliyet Analizi (Life Cycle Cost Analysis — LCC)"
category: factory
equipment_type: factory
keywords: [yaşam döngüsü, LCC, maliyet]
related_files: [factory/economic_analysis.md, factory/energy_pricing.md, factory/prioritization.md]
use_when: ["Yaşam döngüsü maliyeti hesaplanırken", "Uzun vadeli yatırım analizi yapılırken"]
priority: low
last_updated: 2026-01-31
---
# Yaşam Döngüsü Maliyet Analizi (Life Cycle Cost Analysis — LCC)

> Son güncelleme: 2026-01-31

## Genel Bakış

Yaşam döngüsü maliyet analizi (LCC), bir ekipmanın veya sistemin elde edilmesinden ömrünün sonuna kadar ortaya çıkan tüm maliyetlerin bugünkü değere indirgenerek toplam maliyetinin hesaplanmasıdır. Enerji ekipmanlarında satın alma maliyeti toplam maliyetin yalnızca %5-15'ini oluştururken, enerji maliyeti %70-90'ını oluşturabilir. Bu nedenle LCC, doğru ekipman seçimi ve yatırım kararları için kritik bir araçtır. TCO (Total Cost of Ownership — Toplam Sahip Olma Maliyeti) kavramı ile birlikte, AB Lot çalışmaları (ErP Direktifi) referans alınarak sunulmaktadır.

## 1. LCC Metodolojisi (LCC Methodology)

### 1.1 Maliyet Kategorileri

```
LCC = C_acq + C_inst + C_energy + C_maint + C_down + C_env + C_disp

Burada:
- C_acq    = Satın alma (acquisition) maliyeti [€]
- C_inst   = Kurulum (installation) maliyeti [€]
- C_energy = Enerji maliyeti (ömür boyu, bugünkü değer) [€]
- C_maint  = Bakım ve onarım maliyeti (ömür boyu, bugünkü değer) [€]
- C_down   = Duruş / arıza maliyeti (ömür boyu, bugünkü değer) [€]
- C_env    = Çevresel maliyet (CO₂ vergisi, emisyon vb.) [€]
- C_disp   = Bertaraf (disposal) / hurda maliyeti (veya geliri) [€]
```

### 1.2 Bugünkü Değer Hesabı (Present Value)

```
Yıllık sabit maliyet için bugünkü değer (anüite):
PV = C_yıllık × [(1 + r)ⁿ - 1] / [r × (1 + r)ⁿ]

Burada:
- C_yıllık = yıllık maliyet [€/yıl]
- r = iskonto oranı [oran]
- n = ekonomik ömür [yıl]

Bugünkü Değer Faktörü (PWF — Present Worth Factor):
PWF = [(1 + r)ⁿ - 1] / [r × (1 + r)ⁿ]

Yıllık artan maliyet için (escalasyon dahil):
PV = C_yıl0 × [(1 + e)/(1 + r)] × {1 - [(1 + e)/(1 + r)]ⁿ} / {1 - [(1 + e)/(1 + r)]}

Burada:
- e = yıllık maliyet artış oranı (enerji escalasyonu) [oran]
```

### 1.3 Yıllıklaştırılmış Maliyet Yöntemi (Annualized Cost)

```
Yıllık eşdeğer maliyet (Annualized LCC):
ALCC = LCC × CRF

CRF (Capital Recovery Factor):
CRF = [r × (1 + r)ⁿ] / [(1 + r)ⁿ - 1]

Bu yöntem, farklı ömürlere sahip alternatiflerin karşılaştırılmasında kullanılır.

Örnek:
LCC = €180,000, n = 15 yıl, r = %8
CRF = [0.08 × (1.08)¹⁵] / [(1.08)¹⁵ - 1] = 0.08 × 3.172 / 2.172 = 0.1168
ALCC = 180,000 × 0.1168 = €21,024/yıl
```

## 2. Ekipman Ekonomik Ömrü ve Maliyet Dağılımı

### 2.1 Tipik Ekonomik Ömürler

| Ekipman | Ekonomik Ömür [yıl] | Fiziksel Ömür [yıl] | Not |
|---|---|---|---|
| Elektrik motoru | 15-20 | 20-30 | IE sınıfına bağlı |
| Basınçlı hava kompresörü | 12-15 | 15-20 | Vida tipi |
| Kazan (buhar/sıcak su) | 20-25 | 25-35 | Bakım kalitesine bağlı |
| Chiller (santrifüj) | 20-25 | 25-30 | Soğutucu akışkan mevzuatı etkili |
| Chiller (vida) | 15-20 | 20-25 | — |
| Pompa (santrifüj) | 15-20 | 20-25 | — |
| Soğutma kulesi | 15-20 | 20-30 | Malzeme kalitesine bağlı |
| VSD (değişken hız sürücüsü) | 10-15 | 12-18 | Elektronik bileşen ömrü |
| LED aydınlatma | 10-15 | 15-20 | Sürücü ömrü belirleyici |
| Isı eşanjörü | 15-20 | 20-30 | Korozyon/kirlenme durumuna bağlı |
| HVAC klima santrali | 15-20 | 20-25 | — |
| Buhar kapanı | 5-10 | 8-15 | Tip ve kaliteye bağlı |
| Boru izolasyonu | 15-20 | 20-30 | Mekanik hasar olmazsa |

### 2.2 Tipik Maliyet Dağılımı (Ömür Boyu)

| Ekipman | Satın Alma [%] | Kurulum [%] | Enerji [%] | Bakım [%] | Bertaraf [%] |
|---|---|---|---|---|---|
| Elektrik motoru | 5-10 | 2-5 | 80-90 | 2-5 | <1 |
| Kompresör (vida) | 10-15 | 3-5 | 70-80 | 5-10 | 1-2 |
| Kazan | 8-12 | 5-8 | 70-80 | 5-10 | 1-3 |
| Chiller | 12-18 | 5-8 | 60-75 | 8-12 | 2-3 |
| Pompa | 8-12 | 3-5 | 75-85 | 5-8 | <1 |
| Fan | 8-12 | 3-5 | 75-85 | 5-8 | <1 |
| Aydınlatma (LED) | 25-35 | 5-10 | 50-65 | 3-5 | 1-2 |

```
Önemli sonuç:
Motor, kompresör, pompa gibi sürekli çalışan ekipmanlarda
enerji maliyeti toplam LCC'nin %70-90'ını oluşturur.
Bu nedenle:
- Satın alma fiyatına değil, verimlilik sınıfına odaklanılmalıdır
- %1-2 verimlilik farkı bile büyük LCC tasarrufu sağlar
- Yüksek verimli ekipman genellikle 1-3 yıl içinde ek maliyetini geri öder
```

## 3. LCC Hesaplama Örneği: Motor Seçimi

### 3.1 Senaryo

```
75 kW santrifüj pompa motoru seçimi:
- Yük faktörü: %80 (ortalama)
- Çalışma süresi: 6,000 saat/yıl
- Elektrik fiyatı: €0.12/kWh (sabit varsayım)
- İskonto oranı: %8
- Ekonomik ömür: 15 yıl

Alternatif A: IE2 (Standart verimlilik)
- Motor verimi: %93.5 (tam yükte), %93.0 (%75 yükte)
- Satın alma fiyatı: €3,200
- Kurulum: €800

Alternatif B: IE4 (Super premium verimlilik)
- Motor verimi: %96.0 (tam yükte), %95.8 (%75 yükte)
- Satın alma fiyatı: €5,800
- Kurulum: €800
```

### 3.2 Hesaplama

```
Yıllık enerji tüketimi:
E = P_şaft × yük_faktörü × t_çalışma / η_motor [kWh/yıl]

IE2: E_A = 75 × 0.80 × 6,000 / 0.930 = 387,097 kWh/yıl
IE4: E_B = 75 × 0.80 × 6,000 / 0.958 = 375,783 kWh/yıl

Fark: ΔE = 387,097 - 375,783 = 11,314 kWh/yıl

Yıllık enerji maliyeti:
C_A = 387,097 × 0.12 = €46,452/yıl
C_B = 375,783 × 0.12 = €45,094/yıl
ΔC = €1,358/yıl

LCC Hesabı (15 yıl, %8):
PWF = [(1.08)¹⁵ - 1] / [0.08 × (1.08)¹⁵] = 2.172 / 0.2538 = 8.559

LCC_A = 3,200 + 800 + 46,452 × 8.559 = 4,000 + 397,587 = €401,587
LCC_B = 5,800 + 800 + 45,094 × 8.559 = 6,600 + 385,959 = €392,559

ΔLCC = 401,587 - 392,559 = €9,028 (IE4 lehine)

Ek yatırımın geri ödeme süresi:
SPP = (5,800 - 3,200) / 1,358 = 1.91 yıl
```

### 3.3 Sonuç Tablosu

| Parametre | IE2 (Standart) | IE4 (Super Premium) | Fark |
|---|---|---|---|
| Satın alma [€] | 3,200 | 5,800 | +2,600 |
| Kurulum [€] | 800 | 800 | 0 |
| Yıllık enerji [kWh] | 387,097 | 375,783 | -11,314 |
| Yıllık enerji maliyeti [€] | 46,452 | 45,094 | -1,358 |
| LCC (15 yıl) [€] | 401,587 | 392,559 | -9,028 |
| Ek yatırım SPP [yıl] | — | — | 1.91 |
| CO₂ azaltma [tCO₂/yıl] | — | — | 5.4 |

## 4. LCC Hesaplama Örneği: Kompresör Seçimi

### 4.1 Senaryo ve Hesaplama

```
90 kW vida kompresör seçimi (7 bar, 15 m³/min):
Çalışma: 6,000 saat/yıl, %70 ortalama yük
Elektrik: €0.12/kWh, İskonto: %8, Ömür: 12 yıl

Alternatif A: Sabit hızlı kompresör
- Özgül güç (tam yük): 6.2 kW/(m³/min)
- Kısmi yükte verim düşüşü: %15 (yüksüz çalışma)
- Satın alma: €28,000, Kurulum: €5,000
- Yıllık bakım: €3,000

Alternatif B: VSD kompresör
- Özgül güç (tam yük): 6.5 kW/(m³/min) (VSD kayıpları nedeniyle)
- Kısmi yükte: Debi ile orantılı güç
- Satın alma: €42,000, Kurulum: €6,000
- Yıllık bakım: €3,500

Yıllık enerji:
A: Tam yük saatleri: 4,200 h, Yüksüz: 1,800 h
   E_A = (93 × 4,200) + (93 × 0.25 × 1,800) = 390,600 + 41,850 = 432,450 kWh

B: VSD ile güç = 93 × (yük_oranı)^2.5 (ortalama)
   Ort. güç = 93 × 0.70 = 65.1 kW (basitleştirilmiş lineer)
   E_B = 65.1 × 6,000 = 390,600 kWh

   Gerçekçi hesap (affinite yaklaşımı):
   E_B ≈ 370,000 kWh/yıl (VSD kısmi yük avantajı ile)

PWF (12 yıl, %8) = 7.536

LCC_A = 28,000 + 5,000 + (432,450 × 0.12) × 7.536 + 3,000 × 7.536
      = 33,000 + 390,900 + 22,608 = €446,508

LCC_B = 42,000 + 6,000 + (370,000 × 0.12) × 7.536 + 3,500 × 7.536
      = 48,000 + 334,597 + 26,376 = €408,973

ΔLCC = 446,508 - 408,973 = €37,535 (VSD lehine)
SPP(ek yatırım) = (48,000 - 33,000) / [(432,450 - 370,000) × 0.12 - 500]
                = 15,000 / (7,494 - 500) = 15,000 / 6,994 = 2.14 yıl
```

## 5. LCC Hesaplama Örneği: Kazan Seçimi

### 5.1 Senaryo ve Hesaplama

```
2,000 kW buhar kazanı seçimi (10 bar, doymuş):
Çalışma: 5,000 saat/yıl, %75 ortalama yük
Doğalgaz fiyatı: €0.045/kWh, İskonto: %8, Ömür: 20 yıl

Alternatif A: Standart kazan (3 geçişli)
- Verim: %88 (tam yük), %85 (kısmi yük)
- Satın alma: €95,000, Kurulum: €25,000
- Yıllık bakım: €5,000

Alternatif B: Yüksek verimli kazan (economizer + O₂ kontrol)
- Verim: %93 (tam yük), %91 (kısmi yük)
- Satın alma: €135,000, Kurulum: €30,000
- Yıllık bakım: €6,000

Yıllık yakıt tüketimi:
A: Q_yakıt = 2,000 × 0.75 × 5,000 / 0.86 = 8,720,930 kWh/yıl
B: Q_yakıt = 2,000 × 0.75 × 5,000 / 0.92 = 8,152,174 kWh/yıl
ΔE = 568,756 kWh/yıl

Yıllık yakıt maliyeti:
A: 8,720,930 × 0.045 = €392,442/yıl
B: 8,152,174 × 0.045 = €366,848/yıl
ΔC = €25,594/yıl

PWF (20 yıl, %8) = 9.818

LCC_A = 95,000 + 25,000 + 392,442 × 9.818 + 5,000 × 9.818
      = 120,000 + 3,853,049 + 49,090 = €4,022,139

LCC_B = 135,000 + 30,000 + 366,848 × 9.818 + 6,000 × 9.818
      = 165,000 + 3,601,861 + 58,908 = €3,825,769

ΔLCC = 4,022,139 - 3,825,769 = €196,370 (yüksek verimli lehine)
SPP(ek yatırım) = (165,000 - 120,000) / (25,594 - 1,000) = 1.83 yıl
```

## 6. LCC Hesaplama Örneği: Chiller Seçimi

### 6.1 Senaryo ve Hesaplama

```
500 kW su soğutmalı chiller seçimi (7/12°C):
Çalışma: 3,000 saat/yıl (mevsimsel), %60 ortalama yük
Elektrik: €0.12/kWh, İskonto: %8, Ömür: 20 yıl

Alternatif A: Standart vida chiller
- COP tam yük: 4.8, IPLV: 5.5
- Satın alma: €85,000, Kurulum: €15,000
- Yıllık bakım: €6,000

Alternatif B: Yüksek verimli santrifüj + VSD
- COP tam yük: 6.2, IPLV: 8.5
- Satın alma: €145,000, Kurulum: €20,000
- Yıllık bakım: €7,000

Yıllık enerji tüketimi (IPLV bazlı):
A: E = Q_soğutma × LF × t / IPLV = 500 × 0.60 × 3,000 / 5.5 = 163,636 kWh
B: E = 500 × 0.60 × 3,000 / 8.5 = 105,882 kWh
ΔE = 57,754 kWh/yıl

Yıllık maliyet farkı:
ΔC = 57,754 × 0.12 = €6,931/yıl (enerji) - 1,000 (ek bakım) = €5,931/yıl

PWF (20 yıl, %8) = 9.818

LCC_A = 100,000 + 163,636 × 0.12 × 9.818 + 6,000 × 9.818
      = 100,000 + 192,776 + 58,908 = €351,684

LCC_B = 165,000 + 105,882 × 0.12 × 9.818 + 7,000 × 9.818
      = 165,000 + 124,779 + 68,726 = €358,505

ΔLCC = 351,684 - 358,505 = -€6,821 (standart vida chiller lehine!)

Not: Düşük çalışma saatlerinde (3,000 h/yıl) ve düşük yük faktöründe (%60),
yüksek verimli santrifüj chiller'ın ek maliyeti enerji tasarrufunu karşılamıyor.
Ancak 4,000+ saat/yıl veya yüksek yük faktöründe sonuç tersine döner.
```

### 6.2 Chiller LCC Duyarlılık

| Çalışma Saati [h/yıl] | LCC_A [€] | LCC_B [€] | Fark [€] | Uygun Seçim |
|---|---|---|---|---|
| 2,000 | 228,851 | 248,186 | -19,335 | A (Standart) |
| 3,000 | 351,684 | 358,505 | -6,821 | A (Standart) |
| 4,000 | 474,517 | 468,824 | +5,693 | B (Yüksek verimli) |
| 5,000 | 597,350 | 579,143 | +18,207 | B (Yüksek verimli) |
| 6,000 | 720,183 | 689,462 | +30,721 | B (Yüksek verimli) |

```
Kritik çalışma saati (break-even):
LCC_A = LCC_B noktası ≈ 3,500 h/yıl

Karar kuralı:
- < 3,500 h/yıl: Standart verimli chiller
- > 3,500 h/yıl: Yüksek verimli chiller
- Bu eşik, enerji fiyatı ve iskonto oranına göre değişir
```

## 7. LCC Hesaplama Örneği: Aydınlatma

### 7.1 Senaryo ve Hesaplama

```
Fabrika üretim alanı aydınlatma yenileme (1,000 m²):
Mevcut: 200 adet × 58W T8 floresan (balast dahil: 70W)
Öneri: 200 adet × 30W LED panel
Çalışma: 4,500 saat/yıl
Elektrik: €0.12/kWh, İskonto: %8

Mevcut (T8):
- Güç: 200 × 70 = 14,000 W = 14.0 kW
- Enerji: 14.0 × 4,500 = 63,000 kWh/yıl
- Maliyet: 63,000 × 0.12 = €7,560/yıl
- Lamba ömrü: 15,000 h → Değişim: 4,500/15,000 = 0.3/yıl
- Lamba değişim maliyeti: 200 × 0.3 × €8 = €480/yıl (malzeme + işçilik)

LED panel:
- Güç: 200 × 30 = 6,000 W = 6.0 kW
- Enerji: 6.0 × 4,500 = 27,000 kWh/yıl
- Maliyet: 27,000 × 0.12 = €3,240/yıl
- Ömür: 50,000 h → 11 yıl (4,500 h/yıl baz)
- Bakım: Pratik olarak sıfır (ömür boyu)

Yatırım:
- LED panel + sürücü: 200 × €45 = €9,000
- Montaj: 200 × €15 = €3,000
- Toplam: €12,000

Yıllık tasarruf: (7,560 + 480) - 3,240 = €4,800/yıl
SPP = 12,000 / 4,800 = 2.5 yıl

LCC (11 yıl, %8):
PWF (11 yıl) = 7.139
LCC_mevcut = 0 + (7,560 + 480) × 7.139 = €57,378
LCC_LED = 12,000 + 3,240 × 7.139 = 12,000 + 23,130 = €35,130

ΔLCC = 57,378 - 35,130 = €22,248 (LED lehine)
```

## 8. TCO — Toplam Sahip Olma Maliyeti (Total Cost of Ownership)

### 8.1 TCO ve LCC Farkı

```
TCO, LCC'ye ek olarak şunları içerir:
- Eğitim maliyetleri
- Yedek parça stoğu maliyeti
- Üretim kaybı (duruş süreleri)
- Yönetim ve idari maliyetler
- Yazılım/lisans maliyetleri
- Kalite etkileri

TCO = LCC + C_eğitim + C_stok + C_duruş + C_yönetim + C_yazılım + C_kalite

TCO genellikle LCC'den %10-30 daha yüksektir.
Büyük yatırım kararlarında TCO tercih edilmelidir.
```

### 8.2 TCO Değerlendirme Matrisi

| Maliyet Kategorisi | Düşük Etkili | Orta Etkili | Yüksek Etkili |
|---|---|---|---|
| Enerji maliyeti | Aydınlatma, HVAC | Pompalar, fanlar | Kompresörler, kazanlar |
| Bakım maliyeti | LED, VSD | Pompalar, vanalar | Kazanlar, chillerlar |
| Duruş maliyeti | Aydınlatma | HVAC, pompalar | Kompresörler, kazanlar |
| Yedek parça | LED, izolasyon | Pompalar, motorlar | Kompresörler, chillerlar |

## 9. AB Lot Çalışmaları ve ErP Direktifi

### 9.1 AB Ekodizayn (ErP) Direktifi LCC Yaklaşımı

```
AB Ekodizayn Direktifi (2009/125/EC):
Enerji ile İlgili Ürünler (ErP — Energy-related Products)

LCC yaklaşımı:
1. Ürün grubunu tanımla (Lot)
2. Referans (base case) ürünü belirle
3. LCC analizi ile minimum enerji verimlilik gereksinimlerini hesapla
4. LLCC (Least Life Cycle Cost) noktasını bul
5. BAT (Best Available Technology) ile karşılaştır
6. Minimum verimlilik standardını belirle

LLCC: Toplam yaşam döngüsü maliyetinin minimum olduğu verimlilik seviyesi
Bu seviye, hem üretici hem de kullanıcı için optimum noktadır.
```

### 9.2 İlgili Lot Çalışmaları

| Lot No | Ürün Grubu | Minimum Verimlilik | Yürürlük |
|---|---|---|---|
| Lot 11 | Elektrik motorları | IE3 (≥0.75 kW) | 2017 |
| Lot 11 | Elektrik motorları | IE4 (≥75 kW, bazı tipler) | 2023 |
| Lot 21 | Merkezi ısıtma kazanları | %86 (ERP rating) | 2015 |
| Lot 28 | Kompresörler | Ürün bazlı | Devam ediyor |
| Lot 1 | Kazanlar (ticari) | Yoğuşmalı standart | 2015 |
| Lot 6 | Klima ve ısı pompaları | SEER/SCOP minimumları | 2013/2018 |
| Lot 29 | Chillerlar | SEER minimumları | Geliştirilmekte |

### 9.3 LCC ve ErP İlişkisi

```
ErP minimum verimlilik gereksinimleri LCC analizine dayanır:

1. Piyasadaki ürünlerin verimlilik dağılımını belirle
2. Her verimlilik seviyesi için LCC hesapla
3. LLCC noktasını bul → Bu seviye civarında minimum standart belirlenir
4. BAT noktasını bul → Gelecekteki sıkılaştırma hedefi

Sonuç:
- ErP minimumları altındaki ekipmanlar AB pazarına giremez
- Türkiye'de ENVER etiketi benzer yaklaşım izler
- Enerji etiketleri (A+++/A/G) LCC perspektifini tüketiciye aktarır
```

## 10. LCC Performans Değerlendirmesi

### 10.1 LCC Tasarruf Oranı Sınıflandırması

| LCC Tasarrufu (Yüksek verimli vs. Standart) | Değerlendirme | Karar |
|---|---|---|
| >%25 | Mükemmel | Kesinlikle yüksek verimli seçilmeli |
| %15-25 | İyi | Yüksek verimli tercih edilmeli |
| %5-15 | Ortalama | Duyarlılık analizi ile karar verilmeli |
| %0-5 | Düşük | Stratejik faktörlerle değerlendirilmeli |
| <%0 (negatif) | Kritik değil | Standart verimli yeterli olabilir |

### 10.2 LCC Karar Ağacı

```
Ekipman LCC karar süreci:

1. Çalışma profilini belirle (saat/yıl, yük faktörü)
2. Alternatifleri listele (standart, yüksek verimli, premium)
3. Her alternatif için LCC hesapla
4. Duyarlılık analizi yap (enerji fiyatı, çalışma saati, iskonto)
5. Break-even noktalarını belirle
6. TCO etkilerini değerlendir (duruş, bakım, kalite)
7. Çevresel faydaları hesapla (CO₂, emisyon)
8. Final kararı ver

Pratik kurallar:
- Yıllık 4,000+ saat çalışan ekipmanlarda: Daima en verimli seçeneği seç
- Yıllık 2,000-4,000 saat: LCC analizi ile karar ver
- Yıllık <2,000 saat: Standart verimli genellikle yeterli
- Enerji fiyatı arttıkça break-even saati düşer
```

## 11. LCC Duyarlılık Analizi

### 11.1 Ana Değişkenler

```
LCC'yi en çok etkileyen faktörler (duyarlılık sırası):

1. Enerji fiyatı (en yüksek etki)
   ±%20 enerji fiyatı → LCC'de ±%14-18 değişim

2. Çalışma saati
   ±%20 çalışma saati → LCC'de ±%12-16 değişim

3. Yük faktörü
   ±%20 yük faktörü → LCC'de ±%10-14 değişim

4. İskonto oranı
   ±%25 iskonto → LCC'de ±%5-10 değişim

5. Satın alma fiyatı
   ±%20 fiyat → LCC'de ±%2-5 değişim (düşük etki!)

Bu sıralama, satın alma fiyatının LCC kararlarında
neden az önemli olduğunu açıkça göstermektedir.
```

### 11.2 Duyarlılık Tablosu (Motor Örneği)

| Parametre | -20% | Baz | +20% | LCC Etkisi |
|---|---|---|---|---|
| Elektrik fiyatı [€/kWh] | 0.096 | 0.120 | 0.144 | ±%16 |
| Çalışma saati [h/yıl] | 4,800 | 6,000 | 7,200 | ±%14 |
| Motor fiyat farkı [€] | 2,080 | 2,600 | 3,120 | ±%0.3 |
| İskonto oranı [%] | 6.4 | 8.0 | 10.0 | ±%6 |
| Ekonomik ömür [yıl] | 12 | 15 | 18 | ±%4 |

## İlgili Dosyalar

- [Ekonomik Analiz](economic_analysis.md) — NPV, IRR, SPP detaylı hesaplama
- [Önceliklendirme](prioritization.md) — LCC sonuçlarının karar sürecine entegrasyonu
- [Yardımcı Sistemler](utility_analysis.md) — Utility ekipman LCC referansları
- [Pinch Analizi](pinch_analysis.md) — Eşanjör yatırımlarında LCC
- [KPI Tanımları](kpi_definitions.md) — Verimlilik sınıfları ve performans göstergeleri
- [Kazan Ekipman](../boiler/equipment/systems_overview.md) — Kazan tipleri ve verimlilikleri
- [Kompresör Ekipman](../compressor/equipment/systems_overview.md) — Kompresör seçim kriterleri
- [Chiller Ekipman](../chiller/equipment/systems_overview.md) — Chiller tipleri ve COP değerleri

## Referanslar

- Fuller, S.K. & Petersen, S.R., "Life-Cycle Costing Manual for the Federal Energy Management Program," NIST Handbook 135, 1996 (revised 2016)
- European Commission, "Methodology for Ecodesign of Energy-related Products (MEErP)," 2011
- IEC 60300-3-3:2017, "Dependability management — Part 3-3: Application guide — Life cycle costing"
- Barringer, H.P., "Life Cycle Cost and Good Practices," NPRA Maintenance Conference, 1998
- Europump & Hydraulic Institute, "Life Cycle Costs: A Guide to LCC Analysis for Pumping Systems," 2001
- US DOE, "Improving Motor and Drive System Performance," 2014
- AB Ekodizayn Direktifi 2009/125/EC ve uygulama tüzükleri
- ISO 15686-5:2017, "Buildings and constructed assets — Service life planning — Part 5: Life-cycle costing"
- Dhillon, B.S., "Life Cycle Costing for Engineers," CRC Press, 2009
