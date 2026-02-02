---
title: "İyileştirme Önceliklendirme — İleri Exergy Tabanlı (Improvement Priority — Advanced Exergy Based)"
category: factory
equipment_type: factory
keywords: [IPN, improvement priority number, theta sınıflandırma, kaçınılabilir exergy, avoidable exergy destruction, quick win, stratejik proje, bütçe dağılımı, önceliklendirme, ROI, ileri exergy, advanced exergy, decision matrix]
related_files:
  - factory/advanced_exergy/overview.md
  - factory/advanced_exergy/avoidable_unavoidable.md
  - factory/advanced_exergy/endogenous_exogenous.md
  - factory/advanced_exergy/four_way_splitting.md
  - factory/prioritization.md
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/cross_equipment.md
  - factory/economic_analysis.md
use_when:
  - "İleri exergy analizine dayalı iyileştirme önceliği belirlenirken"
  - "Geleneksel ve ileri exergy sıralaması karşılaştırılırken"
  - "IPN (Improvement Priority Number) hesaplanırken"
  - "Theta sınıflandırması yapılırken"
  - "Quick win ve stratejik proje ayrımı yapılırken"
  - "Bütçe dağılımı ileri exergy verileriyle optimize edilirken"
priority: high
last_updated: 2025-05-15
---
# İyileştirme Önceliklendirme — İleri Exergy Tabanlı (Improvement Priority — Advanced Exergy Based)

> Son güncelleme: 2025-05-15

## Genel Bakış

Geleneksel exergy analizinde iyileştirme önceliği, bileşenlerin **toplam exergy yıkımına (I_total)** göre sıralanmasıyla belirlenir. Ancak bu yaklaşım yanıltıcı olabilir: toplam yıkımı en yüksek bileşenin, iyileştirme potansiyeli en yüksek bileşen olması gerekmez. Çünkü yıkımın büyük bir kısmı **kaçınılamaz (unavoidable)** olabilir.

Bu dosya, ileri exergy analizinin sonuçlarını kullanarak daha gerçekçi ve eyleme dönüştürülebilir bir önceliklendirme çerçevesi sunar. Temel araçlar:

- **IPN (Improvement Priority Number):** Kaçınılabilir exergy yıkımının ekonomik etkisine göre normalize edilmiş öncelik numarası
- **Theta (θ) sınıflandırması:** Kaçınılabilir/toplam exergy yıkımı oranına göre iyileştirme potansiyel sınıfı
- **Kombine skor:** Mevcut ROI tabanlı önceliklendirme ile ileri exergy göstergelerinin entegrasyonu

## 1. IPN Formülü ve Uygulama (Improvement Priority Number)

### 1.1 Tanım

IPN, her bileşenin kaçınılabilir exergy yıkımının ekonomik etkisini, tüm sistem içindeki payına göre normalize eder. Tsatsaronis ve Morosuk (2006) tarafından önerilen bu yaklaşım, yatırım kararlarını geleneksel sıralamaya göre daha isabetli yönlendirir.

```
IPN_k = (I_AV,k x c_F,k x t_annual) / Sigma_j(I_AV,j x c_F,j x t_annual)

Burada:
  I_AV,k  : Bileşen k'nın kaçınılabilir exergy yıkımı [kW]
  c_F,k   : Bileşen k'nın yakıt exergetik birim maliyeti [EUR/kWh]
  t_annual : Yıllık çalışma süresi [h]
  j       : Sistemdeki tüm bileşenler (1, 2, ..., n)

Özellikler:
  IPN_k in [0, 1]
  Sigma_k(IPN_k) = 1.0
  En yüksek IPN = en yüksek yatırım önceliği
```

### 1.2 Formül Bileşenleri

```
Yıllık kaçınılabilir exergy maliyeti:
  AC_AV,k = I_AV,k x c_F,k x t_annual  [EUR/yıl]

Toplam yıllık kaçınılabilir exergy maliyeti:
  AC_AV,total = Sigma_j(I_AV,j x c_F,j x t_annual)  [EUR/yıl]

IPN_k = AC_AV,k / AC_AV,total
```

### 1.3 IPN Yorumlama Rehberi

| IPN Aralığı | Yorum | Aksiyon |
|---|---|---|
| > 0.30 | Baskın kaynak — en yüksek iyileştirme etkisi | Hemen detaylı fizibilite ve yatırım planı |
| 0.15 - 0.30 | Anlamlı kaynak — önemli iyileştirme etkisi | Bütçe dahilinde planlı yatırım |
| 0.05 - 0.15 | Orta kaynak — toplamda katkı sağlar | Maliyet-fayda analizi ile karar |
| < 0.05 | Küçük kaynak — düşük etki | Düşük öncelik, fırsatçı iyileştirme |

### 1.4 IPN'nin Avantajları

```
Geleneksel sıralama (I_total bazlı):
  - Büyük ama kaçınılamaz yıkımları en üste koyar
  - Enerji maliyetini dikkate almaz
  - Çalışma süresini dikkate almaz

IPN tabanlı sıralama:
  + Yalnızca kaçınılabilir yıkımı dikkate alır
  + Farklı enerji kaynaklarının birim maliyetini yansıtır
  + Yıllık çalışma süresini hesaba katar
  + Normalize edilmiş: farklı tesisler karşılaştırılabilir
```

## 2. Theta (θ) Sınıflandırma (Avoidability Ratio)

### 2.1 Tanım

Theta, bir bileşenin toplam exergy yıkımının ne kadarının kaçınılabilir olduğunu gösteren boyutsuz orandır.

```
theta_k = I_AV,k / I_total,k

Burada:
  I_AV,k    : Bileşen k'nın kaçınılabilir exergy yıkımı [kW]
  I_total,k : Bileşen k'nın toplam exergy yıkımı [kW]
  theta_k   : Kaçınılabilirlik oranı [-], 0 <= theta <= 1
```

### 2.2 Theta Sınıflandırma Tablosu

| θ Aralığı | Sınıf | Anlamı | Aksiyon |
|---|---|---|---|
| > 0.5 | Yüksek (High Avoidability) | Toplam yıkımın yarısından fazlası kaçınılabilir — büyük iyileştirme potansiyeli | Hemen yatırım planla, detaylı mühendislik çalışması başlat |
| 0.3 - 0.5 | Orta (Moderate Avoidability) | Anlamlı potansiyel var, ancak yıkımın önemli kısmı kaçınılamaz | Maliyet-fayda analizi yap, uygun koşullarda yatırım planla |
| < 0.3 | Düşük (Low Avoidability) | Yıkımın çoğunluğu kaçınılamaz — teknolojik sınırlara yakın | Düşük öncelik, yalnızca düşük maliyetli fırsatları değerlendir |

### 2.3 Tipik Theta Değerleri (Endüstriyel Ekipman)

| Ekipman Türü | Tipik θ Aralığı | Açıklama |
|---|---|---|
| Pompa (kısma vanası ile) | 0.55 - 0.75 | VSD ile önemli iyileştirme potansiyeli |
| Pompa (VSD ile) | 0.15 - 0.30 | Zaten optimize edilmiş, düşük potansiyel |
| Kompresör (sabit hız) | 0.30 - 0.50 | VSD, inter-cooling fırsatları |
| Kompresör (VSD) | 0.10 - 0.25 | Kalan potansiyel sınırlı |
| Chiller (eski model) | 0.35 - 0.55 | Kondenser, evaporator optimizasyonu |
| Chiller (yeni, verimli) | 0.15 - 0.30 | Sınırlı iyileştirme potansiyeli |
| Kazan (buhar) | 0.15 - 0.30 | Yanma tersinmezliği baskın ve kaçınılmaz |
| Eşanjör (heat exchanger) | 0.40 - 0.65 | Alan artırma ile iyileştirme mümkün |
| Kısma vanası (throttle valve) | 0.60 - 0.85 | Türbin veya genleştirici ile değiştirme |

### 2.4 Theta ve IPN Birlikte Kullanımı

```
Theta tek başına yatırım önceliği belirleyemez:
  - Küçük bir bileşenin theta = 0.8 olması, mutlaka yüksek öncelik değildir
    (çünkü mutlak yıkım düşük olabilir)
  - Büyük bir bileşenin theta = 0.2 olması düşük öncelik anlamına gelmez
    (çünkü mutlak kaçınılabilir yıkım yine de büyük olabilir)

Doğru yaklaşım: IPN ve theta birlikte değerlendirilmeli
  - IPN: Ekonomik etkiyi yakalar (ne kadar para kurtarılabilir?)
  - θ:   Teknik verimliliği yakalar (yatırım ne kadar etkili olur?)
```

## 3. Beş Ekipmanlı Fabrika Worked Example

### 3.1 Fabrika Tanımı

Orta ölçekli bir gıda işleme tesisi, 5 ana ekipman grubu ile çalışmaktadır. Her ekipmanın geleneksel ve ileri exergy analiz sonuçları aşağıda verilmiştir.

```
Fabrika: Gıda işleme tesisi
Sektör: Gıda (food)
Yıllık çalışma: 8000 h (ana ekipman), 6000 h (chiller, mevsimsel)
Enerji kaynakları:
  - Doğalgaz (kazan): c_F = 0.035 EUR/kWh
  - Elektrik (kompresör, chiller, pompa): c_F = 0.12 EUR/kWh
```

### 3.2 Geleneksel Exergy Analizi Sonuçları

| Ekipman | I_total [kW] | Geleneksel Sıra | Yorum |
|---|---|---|---|
| Kazan | 850.0 | 1 | En yüksek toplam yıkım |
| Chiller | 35.8 | 2 | Soğutma kayıpları |
| Kompresör | 22.5 | 3 | Basınçlı hava kayıpları |
| Pompa 1 (kısma vanası) | 5.8 | 4 | Kısma kayıpları |
| Pompa 2 (VSD) | 3.2 | 5 | Optimize edilmiş |

Geleneksel yorumlama: **"Kazana odaklanın — 850 kW exergy yıkımı var!"**

### 3.3 İleri Exergy Analizi — AV/UN Ayrımı

| Ekipman | I_total [kW] | I_UN [kW] | I_AV [kW] | θ = I_AV/I_total |
|---|---|---|---|---|
| Kazan | 850.0 | 661.0 | 189.0 | 0.22 |
| Chiller | 35.8 | 19.2 | 16.6 | 0.46 |
| Kompresör | 22.5 | 14.2 | 8.3 | 0.37 |
| Pompa 1 (kısma) | 5.8 | 1.9 | 3.9 | 0.67 |
| Pompa 2 (VSD) | 3.2 | 2.5 | 0.7 | 0.22 |

### 3.4 IPN Hesabı

```
IPN hesaplaması (adım adım):

Ekipman       | I_AV  | c_F    | t      | AC_AV = I_AV x c_F x t
              | [kW]  | [EUR/kWh]| [h]  | [EUR/yıl]
--------------+-------+--------+--------+------------------------
Kazan         | 189.0 | 0.035  | 8000   | 189.0 x 0.035 x 8000 = 52,920
Chiller       |  16.6 | 0.12   | 6000   |  16.6 x 0.12  x 6000 = 11,952
Kompresör     |   8.3 | 0.12   | 8000   |   8.3 x 0.12  x 8000 =  7,968
Pompa 1       |   3.9 | 0.12   | 8000   |   3.9 x 0.12  x 8000 =  3,744
Pompa 2       |   0.7 | 0.12   | 8000   |   0.7 x 0.12  x 8000 =    672
--------------+-------+--------+--------+------------------------
TOPLAM        |       |        |        |                 77,256

IPN_kazan     = 52,920 / 77,256 = 0.685
IPN_chiller   = 11,952 / 77,256 = 0.155
IPN_kompresör =  7,968 / 77,256 = 0.103
IPN_pompa1    =  3,744 / 77,256 = 0.048
IPN_pompa2    =    672 / 77,256 = 0.009
                                  ------
Toplam IPN                      = 1.000  (kontrol OK)
```

### 3.5 Geleneksel vs İleri Sıralama Karşılaştırması

| Ekipman | I_total [kW] | I_AV [kW] | c_F [EUR/kWh] | t [h] | AC_AV [EUR/yıl] | IPN | İleri Sıra |
|---|---|---|---|---|---|---|---|
| Kazan | 850.0 | 189.0 | 0.035 | 8000 | 52,920 | 0.685 | 1 |
| Chiller | 35.8 | 16.6 | 0.12 | 6000 | 11,952 | 0.155 | 2 |
| Kompresör | 22.5 | 8.3 | 0.12 | 8000 | 7,968 | 0.103 | 3 |
| Pompa 1 | 5.8 | 3.9 | 0.12 | 8000 | 3,744 | 0.048 | 4 |
| Pompa 2 | 3.2 | 0.7 | 0.12 | 8000 | 672 | 0.009 | 5 |

### 3.6 Theta Ağırlıklı Önceliklendirme (Revised Priority)

IPN tek başına mutlak ekonomik etkiyi gösterir. Ancak yatırımın etkinliğini anlamak icin theta ile birleştirmek faydalıdır. Yüksek theta, yatırılan her birim paranın daha büyük bir oranının gerçek iyileştirmeye dönüşeceği anlamına gelir.

```
Kombine Skor = IPN_k x theta_k

Hesaplama:
  Kazan:     0.685 x 0.22 = 0.151
  Chiller:   0.155 x 0.46 = 0.071
  Kompresör: 0.103 x 0.37 = 0.038
  Pompa 1:   0.048 x 0.67 = 0.032
  Pompa 2:   0.009 x 0.22 = 0.002
```

| Ekipman | IPN | θ | IPN x θ | Yeni Sıra | Yorum |
|---|---|---|---|---|---|
| Kazan | 0.685 | 0.22 | 0.151 | 1 | Hala en büyük ekonomik etki, ancak θ düşük — yatırım verimliliği orta |
| Chiller | 0.155 | 0.46 | 0.071 | 2 | Orta ekonomik etki, iyi θ — verimli yatırım |
| Kompresör | 0.103 | 0.37 | 0.038 | 3 | Orta IPN ve θ — dengeli |
| Pompa 1 | 0.048 | 0.67 | 0.032 | 4 | Küçük ama en yüksek θ — küçük yatırımla etkili sonuç |
| Pompa 2 | 0.009 | 0.22 | 0.002 | 5 | Hem IPN hem θ düşük — öncelik yok |

### 3.7 Kritik Yorum: Geleneksel vs İleri Analiz

```
Geleneksel analiz der ki:
  "Kazana odaklanın — 850 kW exergy yıkımı var!"

İleri analiz düzeltir:
  "Kazanın θ = 0.22 — yani 850 kW'nin yalnızca 189 kW'si kaçınılabilir.
   Yanma tersinmezliği doğası gereği yüksek ve azaltılamaz.
   Kazan hala 1. sırada ama beklentiler gerçekçi olmalı."

  "Pompa 1'in θ = 0.67 — toplam yıkımı küçük (5.8 kW) ama
   yıkımının %67'si kaçınılabilir. VSD veya kısma eliminasyonu
   ile küçük yatırımla yüksek verim artışı mümkün."

  "Chiller, θ = 0.46 ile orta potansiyelde. Kondenser optimizasyonu
   ve VSD ile anlamlı iyileştirme beklenir."

Sonuç: İleri analiz, yatırım beklentilerini gerçekçi kılar ve
küçük ama yüksek potansiyelli bileşenleri görünür yapar.
```

## 4. Mevcut prioritization.md ile Entegrasyon

### 4.1 Mevcut ROI Bazlı Sistem

Mevcut `prioritization.md` dosyasında MCDA (Multi-Criteria Decision Analysis) tabanlı bir önceliklendirme sistemi tanımlanmıştır:

```
Mevcut kriter ağırlıkları (MCDA):
  Ekonomik  : %40 (SPP %20, NPV/I %12, Tasarruf %8)
  Teknik    : %30 (Fizibilite %12, Kolaylık %10, Risk %8)
  Stratejik : %30 (CO2 %12, Sürdürülebilirlik %8, Güvenlik %5, Mevzuat %5)
```

### 4.2 İleri Exergy Göstergelerinin Eklenmesi

İleri exergy analiz sonuçları, mevcut MCDA çerçevesine ek kriterler veya ağırlık modifiyerleri olarak entegre edilebilir.

```
Entegrasyon Yaklaşım 1 — Ek Kriter Olarak Ekleme:

Genişletilmiş kriter ağırlıkları:
  Ekonomik  : %35 (SPP %17, NPV/I %10, Tasarruf %8)
  Teknik    : %25 (Fizibilite %10, Kolaylık %8, Risk %7)
  Stratejik : %25 (CO2 %10, Sürdürülebilirlik %7, Güvenlik %4, Mevzuat %4)
  İleri Exergy: %15 (IPN %8, θ %7)
    - IPN puanlama: >0.3 → 10, 0.15-0.3 → 8, 0.05-0.15 → 5, <0.05 → 2
    - θ puanlama:   >0.5 → 10, 0.3-0.5 → 7, <0.3 → 3

Yeni Toplam Puan:
  S_j = Sigma_i(w_i x s_ij)    (artık 12 kriter)
```

```
Entegrasyon Yaklaşım 2 — Ağırlık Modifiyeri Olarak:

Mevcut MCDA puanı korunur, ileri exergy bilgisi ile düzeltilir:

Modifiye_Skor_k = MCDA_Skor_k x (1 + alpha x theta_k) x (1 + beta x IPN_k)

Burada:
  alpha = 0.3 (theta etkisi ağırlığı)
  beta  = 0.5 (IPN etkisi ağırlığı)

Avantajı: Mevcut sıralamayı tamamen değiştirmez, ama ileri exergy
bilgisi olan projeleri yukarı/aşağı kaydırır.
```

### 4.3 Kombine Skor Formülü

```
En kapsamlı kombine skor:

  Score_k = w1 x ROI_k + w2 x IPN_k + w3 x theta_k

Burada:
  w1 = 0.50 (ekonomik getiri ağırlığı)
  w2 = 0.30 (ileri exergy öncelik ağırlığı)
  w3 = 0.20 (iyileştirme potansiyel ağırlığı)

ROI_k: Normalize edilmiş yatırım getirisi [0-1]
  ROI_k = (Yıllık Tasarruf / Yatırım) / max_j(Yıllık Tasarruf / Yatırım)

IPN_k: Improvement Priority Number [0-1] (zaten normalize)

theta_k: Avoidability ratio [0-1]
```

### 4.4 Cross-Reference Kuralı

```
Theta bazlı otomatik kategori yükseltme:

Kural: theta > 0.5 olan ekipmanlar "Quick Win Adayı" kategorisine yükseltilir

Koşullar:
  1. theta_k > 0.5
  2. Yatırım < EUR 15,000
  3. SPP < 2 yıl (ileri exergy bazlı kaçınılabilir tasarruf ile hesaplanmış)

Üç koşul da sağlanırsa → Kategori: "Quick Win — İleri Exergy Onaylı"
İlk iki koşul sağlanırsa → Kategori: "Potansiyel Quick Win — SPP değerlendir"
Yalnızca theta > 0.5 ise → Kategori: "Yüksek Potansiyel — Bütçe değerlendir"
```

## 5. Quick Win Tanımlama Metodolojisi (Quick Win Identification)

### 5.1 İleri Exergy Tabanlı Quick Win Kriterleri

Geleneksel quick win tanımı yalnızca SPP ve yatırım miktarına bakar. İleri exergy analizi ile zenginleştirilmiş kriterler:

```
İleri Quick Win kriterleri:

A. Zorunlu Kriterler (hepsi sağlanmalı):
  1. theta_k > 0.40  (anlamlı iyileştirme potansiyeli)
  2. IPN_k > 0.03    (minimum ekonomik etki eşiği)
  3. SPP < 1.5 yıl   (kısa geri ödeme)
  4. Yatırım < EUR 15,000  (düşük maliyet)

B. Ek Güçlendiriciler (bonuş):
  + Endojen oranı > %70  (sorun bileşenin kendisinde, kolay çözüm)
  + Teknik risk düşük     (kanıtlanmış teknoloji)
  + Duruş gerektirmez     (üretim kaybı yok)
```

### 5.2 Quick Win Tarama Tablosu

| Kriter | Pompa 1 (Kısma) | Chiller (Eski) | Kompresör | Kazan | Pompa 2 (VSD) |
|---|---|---|---|---|---|
| θ > 0.40 | 0.67 EVET | 0.46 EVET | 0.37 HAYIR | 0.22 HAYIR | 0.22 HAYIR |
| IPN > 0.03 | 0.048 EVET | 0.155 EVET | 0.103 EVET | 0.685 EVET | 0.009 HAYIR |
| SPP < 1.5 yıl | 0.8 yıl EVET | 2.3 yıl HAYIR | 1.8 yıl HAYIR | 4.2 yıl HAYIR | N/A |
| Yatırım < EUR 15K | EUR 4,500 EVET | EUR 28,000 HAYIR | EUR 18,000 HAYIR | EUR 45,000 HAYIR | N/A |
| **Quick Win?** | **EVET** | HAYIR | HAYIR | HAYIR | HAYIR |

Sonuc: Yalnızca **Pompa 1 (kısma vanası eliminasyonu / VSD retrofit)** tüm quick win kriterlerini karşılamaktadır.

### 5.3 Quick Win Detay Kartı Örneği

```
QUICK WIN KARTI
========================================
Ekipman:       Pompa 1 (kısma vanası kontrollü)
Önlem:         Kısma vanası eliminasyonu + VSD retrofit
Theta:         0.67 (Yüksek Potansiyel)
IPN:           0.048
I_AV:          3.9 kW
Yıllık Tasarruf: 3,744 EUR/yıl (= I_AV x c_F x t)
Tahmini Yatırım: 4,500 EUR
SPP:           4,500 / 3,744 = 1.20 yıl -> 14.4 ay
Teknik Risk:   Düşük (kanıtlanmış teknoloji)
Duruş:         < 2 gün (planlı bakımda)
Endojen oranı: %82 (sorun bileşenin kendisinde)
Kategori:      QUICK WIN — İleri Exergy Onaylı
========================================
```

## 6. Stratejik Proje vs Quick Win Sınıflandırması

### 6.1 İleri Exergy Tabanlı Proje Sınıflandırma Matrisi

```
                       IPN
                Düşük (<0.05)    Orta (0.05-0.20)    Yüksek (>0.20)
             +------------------+-------------------+------------------+
   Yüksek    | Küçük Quick Win  | Quick Win /       | Stratejik        |
   (θ > 0.5) | (küçük ama       |  Orta Vadeli      |  Öncelik 1       |
             | verimli)         | (etkili yatırım)  | (hemen planla)   |
             +------------------+-------------------+------------------+
θ  Orta      | Fırsatçı         | Planlı Yatırım    | Stratejik        |
   (0.3-0.5) | (uygun zamanda)  | (bütçe döneminde) |  Öncelik 2       |
             +------------------+-------------------+------------------+
   Düşük     | Pas Geç          | Düşük Öncelik     | Dikkatli         |
   (θ < 0.3) | (kaçınılamaz     | (büyük ama sınırlı|  Değerlendir     |
             |  baskın)         |  potansiyel)      | (beklenti yönet) |
             +------------------+-------------------+------------------+
```

### 6.2 Her Kategorinin Aksiyonu

| Kategori | IPN-θ Bölgesi | Yatırım Stratejisi | Beklenen Etki |
|---|---|---|---|
| Stratejik Öncelik 1 | Yüksek IPN, Yüksek θ | Bütçe ayır, hemen başla | Yüksek tasarruf, yüksek verim |
| Stratejik Öncelik 2 | Yüksek IPN, Orta θ | Planlı yatırım, faz 1-2 | Yüksek tasarruf, orta verim |
| Quick Win / Orta Vadeli | Orta IPN, Yüksek θ | Hızlı uygula | Orta tasarruf, yüksek verim |
| Planlı Yatırım | Orta IPN, Orta θ | Bütçe döneminde | Orta tasarruf, orta verim |
| Küçük Quick Win | Düşük IPN, Yüksek θ | Hemen, düşük maliyet | Küçük tasarruf, yüksek verim |
| Fırsatçı | Düşük IPN, Orta θ | Bakım sırasında | Küçük tasarruf, orta verim |
| Dikkatli Değerlendir | Yüksek IPN, Düşük θ | Detaylı fizibilite | Büyük mutlak tasarruf ama sınırlı potansiyel |
| Düşük Öncelik | Orta IPN, Düşük θ | Ertelenebilir | Sınırlı etki |
| Pas Geç | Düşük IPN, Düşük θ | Yatırım yapma | Etki yok |

### 6.3 Fabrika Örneğindeki Sınıflandırma

```
Fabrika ekipmanları matrise yerleştirme:

Kazan:     IPN=0.685 (Yüksek), θ=0.22 (Düşük) → "Dikkatli Değerlendir"
  → Büyük ekonomik etki var ama potansiyel sınırlı
  → Beklenti: Economizer, hava ön ısıtma ile 189 kW'nin 120-150 kW'si kurtarılabilir
  → Yanma tersinmezliği azaltılamaz, kabul et

Chiller:   IPN=0.155 (Orta), θ=0.46 (Orta) → "Planlı Yatırım"
  → Bütçe döneminde kondenser optimizasyonu + VSD planla
  → Beklenen tasarruf: 11,952 EUR/yıl

Kompresör: IPN=0.103 (Orta), θ=0.37 (Orta) → "Planlı Yatırım"
  → VSD retrofit ve basınç optimizasyonu
  → Beklenen tasarruf: 7,968 EUR/yıl

Pompa 1:   IPN=0.048 (Düşük), θ=0.67 (Yüksek) → "Küçük Quick Win"
  → Kısma eliminasyonu + VSD
  → Küçük ama çok verimli yatırım

Pompa 2:   IPN=0.009 (Düşük), θ=0.22 (Düşük) → "Pas Geç"
  → Zaten VSD var, ek potansiyel yok
```

## 7. Bütçe Dağılımı Önerileri (Budget Allocation)

### 7.1 IPN Bazlı Bütçe Dağılımı

IPN değerleri, bütçe dağılımı için doğal bir rehber sunar. Her bileşenin IPN'si, toplam iyileştirme bütçesinden alması gereken payı temsil eder.

```
Bütçe Dağılım Formülü:

Budget_k = Total_Budget x IPN_k

Örnek: Toplam yıllık iyileştirme bütçesi = EUR 100,000

  Kazan:     100,000 x 0.685 = EUR 68,500
  Chiller:   100,000 x 0.155 = EUR 15,500
  Kompresör: 100,000 x 0.103 = EUR 10,300
  Pompa 1:   100,000 x 0.048 = EUR  4,800
  Pompa 2:   100,000 x 0.009 = EUR    900
```

### 7.2 Theta Düzeltmeli Bütçe Dağılımı

Saf IPN bazlı dağılım, düşük theta bileşenlerine gereğinden fazla bütçe ayırabilir. Theta düzeltmesi ile daha verimli bir dağılım elde edilir.

```
Düzeltilmiş Bütçe Dağılım Formülü:

Budget_k = Total_Budget x (IPN_k x theta_k) / Sigma_j(IPN_j x theta_j)

Normalize Faktör:
  Sigma_j(IPN_j x theta_j) = 0.151 + 0.071 + 0.038 + 0.032 + 0.002 = 0.294

Düzeltilmiş dağılım (EUR 100,000):
  Kazan:     100,000 x 0.151/0.294 = EUR 51,361
  Chiller:   100,000 x 0.071/0.294 = EUR 24,150
  Kompresör: 100,000 x 0.038/0.294 = EUR 12,925
  Pompa 1:   100,000 x 0.032/0.294 = EUR 10,884
  Pompa 2:   100,000 x 0.002/0.294 = EUR    680
```

### 7.3 IPN vs Theta-Düzeltmeli Bütçe Karşılaştırması

| Ekipman | IPN Bazlı [EUR] | θ-Düzeltmeli [EUR] | Fark [EUR] | Yorum |
|---|---|---|---|---|
| Kazan | 68,500 | 51,361 | -17,139 | θ düşük, bütçe azaltıldı |
| Chiller | 15,500 | 24,150 | +8,650 | θ orta-yüksek, bütçe artırıldı |
| Kompresör | 10,300 | 12,925 | +2,625 | θ orta, bütçe artırıldı |
| Pompa 1 | 4,800 | 10,884 | +6,084 | θ yüksek, bütçe artırıldı |
| Pompa 2 | 900 | 680 | -220 | Değişim yok |

```
Theta düzeltmesinin etkisi:
  - Kazanın bütçe payı %68.5 → %51.4'e düştü (θ = 0.22, potansiyel sınırlı)
  - Pompa 1'in payı %4.8 → %10.9'a yükseldi (θ = 0.67, verimli yatırım)
  - Chiller'ın payı %15.5 → %24.2'ye yükseldi (θ = 0.46, iyi potansiyel)

Sonuç: θ düzeltmesi, parayı potansiyeli yüksek bileşenlere yönlendirir.
```

### 7.4 Bütçe Senaryo Analizi

| Senaryo | Bütçe [EUR] | Strateji | Kapsam |
|---|---|---|---|
| Kısıtlı | 15,000 | Yalnızca Quick Win | Pompa 1 (VSD) + kompresör bakım |
| Normal | 50,000 | Quick Win + Planlı | Pompa 1 + Kazan economizer ön çalışma + Chiller bakım |
| Geniş | 100,000 | Kapsamlı | Tüm ekipmanlar, θ-düzeltmeli dağılım |
| Stratejik | 200,000 | Transformasyon | Kapsamlı + ısı entegrasyonu + pinch analizi |

## 8. Uygulama Yol Haritası

### 8.1 Faz Bazlı Uygulama

```
Faz 0 — Hemen (0-3 ay): Quick Win'ler
  - Pompa 1: Kısma eliminasyonu + VSD → EUR 4,500
  - Kompresör: Kaçak onarımı → EUR 2,000
  - Toplam yatırım: EUR 6,500
  - Beklenen tasarruf: EUR 5,700/yıl
  - SPP: 1.14 yıl

Faz 1 — Planlı (3-12 ay): Orta vadeli projeler
  - Kazan: Economizer → EUR 35,000
  - Chiller: Kondenser optimizasyonu → EUR 12,000
  - Toplam yatırım: EUR 47,000
  - Beklenen tasarruf: EUR 18,000/yıl
  - SPP: 2.61 yıl

Faz 2 — Stratejik (12-24 ay): Büyük projeler
  - Kompresör: VSD retrofit → EUR 18,000
  - Chiller: VSD + kontrol optimizasyonu → EUR 28,000
  - Kazan: Hava ön ısıtıcı → EUR 22,000
  - Toplam yatırım: EUR 68,000
  - Beklenen tasarruf: EUR 24,000/yıl
  - SPP: 2.83 yıl

Toplam (3 yıl): Yatırım EUR 121,500, Tasarruf EUR 47,700/yıl
Portföy SPP: 2.55 yıl
```

### 8.2 Kümülatif Tasarruf Projeksiyonu

```
Yıl   | Kümülatif Yatırım | Kümülatif Tasarruf | Net Pozisyon
------|-------------------|--------------------|-----------
0     | 0                 | 0                  | 0
0.25  | 6,500             | 1,425              | -5,075
1     | 53,500            | 9,975              | -43,525
2     | 121,500           | 33,675             | -87,825
3     | 121,500           | 81,375             | -40,125
4     | 121,500           | 129,075            | +7,575   ← Break-even
5     | 121,500           | 176,775            | +55,275

Break-even: ~3.8 yıl (tüm faz yatırımları dahil)
5 yıllık net kazanç: EUR 55,275
```

## 9. IPN ve Theta Hesaplama Kontrol Listesi

```
IPN Hesaplama Adımları:
  [ ] 1. Her bileşenin toplam exergy yıkımını belirle (I_total,k)
  [ ] 2. Her bileşenin kaçınılabilir exergy yıkımını belirle (I_AV,k)
         → AV/UN ayrımı: avoidable_unavoidable.md dosyasına referans
  [ ] 3. Her bileşenin yakıt exergetik birim maliyetini belirle (c_F,k)
         → Doğalgaz: ~0.030-0.040 EUR/kWh
         → Elektrik:  ~0.10-0.15 EUR/kWh
  [ ] 4. Her bileşenin yıllık çalışma süresini belirle (t_annual,k)
  [ ] 5. Her bileşen için AC_AV,k = I_AV,k x c_F,k x t_annual,k hesapla
  [ ] 6. Toplam AC_AV,total = Sigma(AC_AV,k) hesapla
  [ ] 7. Her bileşen için IPN_k = AC_AV,k / AC_AV,total hesapla
  [ ] 8. Sigma(IPN_k) = 1.0 olduğunu doğrula

Theta Hesaplama:
  [ ] 1. I_AV,k ve I_total,k'yı kullanarak theta_k = I_AV,k / I_total,k hesapla
  [ ] 2. theta sınıflandırma tablosuna göre sınıf ata
  [ ] 3. Sonuçları IPN ile birlikte değerlendir
```

## 10. Sınırlamalar ve Dikkat Edilecek Noktalar

```
1. Kaçınılmaz koşul tanımına duyarlılık:
   I_AV (ve dolayısıyla IPN ve θ) kaçınılmaz koşul tanımına bağlıdır.
   Farklı uzmanlar farklı sınırlar tanımlayabilir.
   → Duyarlılık analizi yapılmalı (epsilon_max +/- %5)

2. Enerji maliyeti duyarlılığı:
   c_F değiştiğinde IPN sıralaması değişebilir.
   → Elektrik/gaz fiyat oranı kritik: ratio > 3 ise elektrikli
      ekipmanlar öne çıkar

3. Çalışma süresi varsayımları:
   Mevsimsel ekipmanlar (chiller) düşük t_annual ile dezavantajlıdır.
   → Mevsimsellik açıkça belirtilmeli

4. Endojen/eksojen ayrımı dahil edilmemiştir:
   Bu dosya AV/UN bazlı IPN'e odaklanır. Tam 4-yollu analiz için
   four_way_splitting.md dosyasına bakınız.

5. Dinamik etkiler:
   IPN statik bir anlık görüntüdür. Yük profili, mevsimsellik ve
   kısmi yük davranışı IPN'i etkileyebilir.
   → Yıllık ortalama değerler kullanılmalı
```

## İlgili Dosyalar

- [İleri Exergy Genel Bakış](overview.md) -- İleri exergy analizi kavramsal çerçeve
- [Kaçınılabilir/Kaçınılamaz Ayrımı](avoidable_unavoidable.md) -- I_AV ve I_UN hesaplama detayları
- [Endojen/Ekzojen Ayrımı](endogenous_exogenous.md) -- EN/EX dekompozisyon yöntemi
- [Dört Yollu Bölünme](four_way_splitting.md) -- AV-EN, AV-EX, UN-EN, UN-EX tam analiz
- [Proje Önceliklendirme (Geleneksel)](../prioritization.md) -- MCDA, ROI, risk-getiri matrisi
- [Exergoekonomik Değerlendirme](../exergoeconomic/evaluation_criteria.md) -- f_k, r_k, maliyet göstergeleri
- [Ekipmanlar Arası Entegrasyon](../cross_equipment.md) -- Çapraz ekipman fırsatları
- [Ekonomik Analiz](../economic_analysis.md) -- NPV, IRR, SPP detayları

## Referanslar

1. Tsatsaronis, G., Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
2. Kelly, S., Tsatsaronis, G., Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391.
3. Morosuk, T., Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(3), 229-238.
4. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T., Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152.
5. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. John Wiley & Sons, New York.
6. Tsatsaronis, G. (2008). "Recent developments in exergy analysis and exergoeconomics." *International Journal of Exergy*, 5(5-6), 489-499.
7. Morosuk, T., Tsatsaronis, G. (2019). "Advanced exergy-based methods used to understand and improve energy-conversion systems." *Energy*, 169, 238-246.
