---
title: "Termoekonomik Optimizasyon Genel Bakış (Thermoeconomic Optimization Overview)"
category: thermoeconomic_optimization
keywords: [termoekonomik optimizasyon, exergoekonomik analiz, SPECO, maliyet oluşumu, exergy maliyetleme]
related_files: [knowledge/factory/thermoeconomic_optimization/objective_functions.md, knowledge/factory/thermoeconomic_optimization/iterative_method.md, knowledge/factory/thermoeconomic_optimization/practical_guide.md]
use_when: ["Termoekonomik optimizasyon kavramları hakkında bilgi gerektiğinde", "Exergoekonomik analiz temelleri sorulduğunda"]
priority: high
last_updated: 2026-02-02
---

# Termoekonomik Optimizasyon: Genel Bakış (Thermoeconomic Optimization: Overview)

## 1. Tanım ve Kapsam

**Termoekonomik optimizasyon** (thermoeconomic optimization), termodinamik analiz (özellikle
exergy analizi) ile ekonomik analizin sistematik birleştirilmesiyle, enerji dönüşüm
sistemlerinin maliyet-etkin tasarım ve işletimini sağlayan disiplinler arası bir yaklaşımdır.

### Temel Felsefe

Klasik enerji verimliliği yaklaşımı yalnızca "ne kadar enerji kayboldu?" sorusunu sorar.
Termoekonomik yaklaşım ise şu soruyu sorar:

> **"Termodinamik kayıpların gerçek ekonomik maliyeti nedir ve bu maliyeti düşürmek için
> yapılacak yatırım ne kadardır?"**

Bu soru, enerji kalitesini (exergy) ve ekonomiyi aynı anda değerlendirmeyi gerektirir.

### Neden Exergy Bazlı Analiz?

| Karşılaştırma Kriteri | Enerji Analizi | Exergy Analizi | Termoekonomik Analiz |
|------------------------|----------------|----------------|----------------------|
| Temel yasa | 1. Yasa | 2. Yasa | 2. Yasa + Ekonomi |
| Kayıp tanımı | Enerjinin korunmadığı yer | Termodinamik kalite kaybı | Maliyet oluşum noktası |
| Atık ısı (80°C) | Yüksek enerji kaybı | Düşük exergy kaybı | Düşük maliyet etkisi |
| Atık ısı (400°C) | Yüksek enerji kaybı | Yüksek exergy kaybı | Yüksek maliyet etkisi |
| Karar desteği | "Ne kadar kayıp var?" | "Nerede gerçek kayıp var?" | "Hangi iyileştirme yapılmalı?" |
| Yatırım rehberliği | Hayır | Kısmen | Evet — optimal noktayı gösterir |

---

## 2. Tarihçe ve Gelişim

### Öncü Çalışmalar

| Yıl | Araştırmacı | Katkı |
|-----|-------------|-------|
| 1932 | Keenan | Exergy maliyetleme ilk kavramı |
| 1962 | Tribus & Evans | "Thermoeconomics" terimini ilk kez kullandı |
| 1970 | El-Sayed & Evans | Yapısal optimizasyon |
| 1984 | Tsatsaronis | Exergoekonomik analiz sistematik yöntemi |
| 1993 | Tsatsaronis & Pisa | Iteratif exergoekonomik optimizasyon |
| 1996 | Bejan, Tsatsaronis, Moran | *Thermal Design and Optimization* kitabı |
| 2006 | Lazzaretto & Tsatsaronis | **SPECO** yöntemi — standart metodoloji |
| 2003 | El-Sayed | *The Thermoeconomics of Energy Conversions* |
| 2010+ | Morosuk & Tsatsaronis | İleri exergy analizi (kaçınılabilir/kaçınılamaz) |

### Modern Gelişmeler (2015-2025)

- **Çok amaçlı optimizasyon:** Maliyet + verimlilik + çevre (NSGA-II, MOPSO)
- **CBAM etkisi:** Avrupa karbon sınır mekanizması ile çevre maliyetinin içselleştirilmesi
- **Dijitalleşme:** Gerçek zamanlı exergoekonomik izleme, dijital ikiz entegrasyonu
- **Yapay zeka:** Makine öğrenmesi ile surrogate modeller, hızlı optimizasyon

---

## 3. Temel Kavramlar

### 3.1. Exergy Maliyetleme (Exergy Costing)

Her exergy akışına bir birim maliyet atanır:

```
c_k = Ċ_k / Ėx_k    [€/kJ] veya [€/kWh]

Burada:
  c_k  = k-inci akışın birim exergy maliyeti (specific exergy cost)
  Ċ_k  = k-inci akışın maliyet akış hızı (cost rate) [€/s] veya [€/h]
  Ėx_k = k-inci akışın exergy akış hızı [kW]
```

### 3.2. Exergoekonomik Denge (Exergoeconomic Balance)

Her bileşen (k) için maliyet dengesi:

```
Σ Ċ_çıkış,k + Ċ_W,k = Σ Ċ_giriş,k + Ċ_Q,k + Ż_k

Burada:
  Ċ_çıkış  = Çıkış akışlarının toplam maliyet hızı [€/h]
  Ċ_W      = İş çıkışının maliyet hızı [€/h]
  Ċ_giriş  = Giriş akışlarının toplam maliyet hızı [€/h]
  Ċ_Q      = Isı transferinin maliyet hızı [€/h]
  Ż_k      = Bileşenin yatırım + İ&B maliyet hızı [€/h]
```

### 3.3. SPECO Yöntemi (Specific Exergy Costing)

Lazzaretto & Tsatsaronis (2006) tarafından geliştirilen standart metodoloji:

**Adım 1:** Her bileşen için yakıt (F) ve ürün (P) tanımla
**Adım 2:** Her akışa exergy maliyeti ata
**Adım 3:** Yardımcı (auxiliary) denklemler yaz (F veya P kuralı)
**Adım 4:** Doğrusal denklem sistemini çöz

#### F ve P Kuralı

| Kural | Açıklama | Uygulama |
|-------|----------|----------|
| **F kuralı** | Yakıttan çıkan akışların birim maliyeti = yakıta giren akışların birim maliyeti | Birden fazla yakıt çıkışı olduğunda |
| **P kuralı** | Ürünlerin hepsinin birim maliyeti eşit | Birden fazla ürün olduğunda |

#### Ekipman Bazlı F ve P Tanımları

| Ekipman | Yakıt (F) | Ürün (P) |
|---------|-----------|----------|
| Kompresör | Elektrik gücü (Ẇ) | Hava exergy artışı (Ėx_çıkış - Ėx_giriş) |
| Kazan | Yakıt kimyasal exergysi | Buhar exergy artışı (Ėx_buhar - Ėx_su) |
| Türbin | Akışkan exergy azalması | Üretilen güç (Ẇ) |
| Isı değiştirici | Sıcak akış exergy azalması | Soğuk akış exergy artışı |
| Pompa | Elektrik gücü (Ẇ) | Akışkan exergy artışı |
| Chiller | Elektrik gücü (Ẇ) | Soğutma exergysi |

---

## 4. Termoekonomik Değişkenler

### 4.1. Exergoekonomik Faktör (f_k)

```
f_k = Ż_k / (Ż_k + Ċ_D,k + Ċ_L,k)

Burada:
  f_k   = Exergoekonomik faktör [boyutsuz, 0-1 arası]
  Ż_k   = Bileşenin yatırım + İ&B maliyet hızı [€/h]
  Ċ_D,k = Exergy yıkım maliyet hızı = c_F,k × Ėx_D,k [€/h]
  Ċ_L,k = Exergy kaybı maliyet hızı [€/h]
```

#### f_k Yorumlama Rehberi

| f_k Aralığı | Yorum | Öneri |
|-------------|-------|-------|
| f_k < 0.25 | Exergy yıkım maliyeti baskın | Bileşen verimliliğini artır (daha iyi teknoloji, ek yüzey) |
| 0.25 ≤ f_k ≤ 0.70 | Dengeli durum | Her iki tarafı da incele, küçük iyileştirmeler |
| f_k > 0.70 | Yatırım maliyeti baskın | Daha ucuz bileşen ara, karmaşıklığı azalt |

### 4.2. Bağıl Maliyet Farkı (r_k)

```
r_k = (c_P,k - c_F,k) / c_F,k

Burada:
  r_k   = Bağıl maliyet farkı [boyutsuz]
  c_P,k = Bileşenin ürün birim exergy maliyeti [€/kWh]
  c_F,k = Bileşenin yakıt birim exergy maliyeti [€/kWh]
```

#### r_k Yorumlama Rehberi

| Ekipman Tipi | Tipik r_k | Yüksek r_k Sınırı | Yorum |
|-------------|-----------|-------------------|-------|
| Kompresör | 0.20 – 0.50 | > 0.60 | Sıkıştırma verimsizliği veya aşırı yatırım |
| Kazan | 0.30 – 0.80 | > 1.00 | Yanma tersinmezliği yüksek |
| Isı değiştirici | 0.10 – 0.40 | > 0.50 | ΔT çok yüksek veya kirlenme |
| Türbin | 0.15 – 0.40 | > 0.50 | İzentropik verim düşük |
| Pompa | 0.20 – 0.50 | > 0.60 | Aşırı boyutlanmış veya düşük verim |
| Chiller | 0.40 – 1.20 | > 1.50 | COP düşük veya aşırı yatırım |

### 4.3. Exergy Yıkım Maliyet Hızı (Ċ_D)

```
Ċ_D,k = c_F,k × Ėx_D,k    [€/h]

Burada:
  c_F,k  = Bileşenin yakıt birim exergy maliyeti [€/kWh]
  Ėx_D,k = Bileşendeki exergy yıkımı [kW]
```

Bu değer, termodinamik verimsizliğin parasal karşılığıdır. Ċ_D,k değeri yüksek olan
bileşenler, optimizasyon öncelikli hedeflerdir.

### 4.4. Değişkenlerin Birlikte Yorumlanması

| Ċ_D,k | f_k | Yorum | Aksiyon |
|--------|-----|-------|---------|
| Yüksek | Düşük (<0.25) | Büyük termodinamik kayıp, ucuz bileşen | Verimliliği artır |
| Yüksek | Yüksek (>0.70) | Büyük kayıp ama bileşen zaten pahalı | Daha ucuz alternatif bul |
| Düşük | Düşük (<0.25) | Küçük kayıp, ucuz bileşen | Düşük öncelik |
| Düşük | Yüksek (>0.70) | Küçük kayıp, pahalı bileşen | Bileşen maliyetini düşür |

---

## 5. Termoekonomik Optimizasyonun Endüstriyel Değeri

### Türkiye Bağlamında Önemi

Türkiye'nin enerji yoğun endüstrisi için termoekonomik optimizasyon kritik öneme sahiptir:

1. **Enerji ithalat bağımlılığı:** Türkiye doğalgaz ve petrolün büyük çoğunluğunu ithal eder.
   Exergy bazlı optimizasyon, yakıt tüketimini gerçekçi şekilde minimize eder.

2. **CBAM etkisi:** AB'ye ihracat yapan sektörler (çimento, çelik, kimya, gübre, alüminyum)
   karbon sınır mekanizmasıyla karşı karşıyadır. Termoekonomik optimizasyon, CO₂ maliyetini
   doğrudan amaç fonksiyonuna dahil eder.

3. **Kur volatilitesi:** TL/EUR dalgalanmaları, ithal ekipman maliyetlerini etkiler.
   Duyarlılık analizi, kur riskini değerlendirmeye olanak tanır.

4. **Sanayi dönüşümü:** Yeşil dönüşüm ve Sanayi 4.0 kapsamında, termoekonomik analiz
   yatırım kararlarını bilimsel temele oturtur.

### Klasik ROI Analizine Göre Avantajları

| Özellik | Klasik ROI | Termoekonomik Optimizasyon |
|---------|------------|---------------------------|
| Termodinamik temel | 1. Yasa (enerji) | 2. Yasa (exergy) |
| Kayıp lokalizasyonu | Genel | Bileşen bazlı |
| Maliyet atfetme | Enerji bazlı | Exergy bazlı (gerçekçi) |
| Çoklu iyileştirme kararı | Her biri ayrı ROI | Bütünleşik optimizasyon |
| Yapısal karar | Desteklemez | Destekler (MINLP) |
| Çok amaçlı karar | Desteklemez | Destekler (Pareto) |
| Belirsizlik analizi | Basit | Kapsamlı (Monte Carlo) |

---

## 6. Termoekonomik Optimizasyon Türleri

### 6.1. İteratif Exergoekonomik Yöntem

Tsatsaronis'in geliştirdiği yöntem:
- Mevcut sistemi analiz et → f_k ve r_k hesapla → iyileştirme yönünü belirle → tekrarla
- **Avantaj:** Basit, mühendislik sezgisiyle uyumlu
- **Dezavantaj:** Global optimuma garanti yok
- **Detay:** `iterative_method.md`

### 6.2. Yapısal Optimizasyon (Structural Optimization)

Sistem konfigürasyonunu optimize et:
- Hangi ekipmanlar dahil edilmeli?
- CHP mi yoksa ayrı üretim mi?
- Hangi ısı geri kazanım ağı?
- **Yöntem:** MINLP (Mixed-Integer Nonlinear Programming)
- **Detay:** `structural_optimization.md`

### 6.3. Parametrik Optimizasyon (Parametric Optimization)

Sabit yapı, sürekli değişken optimizasyonu:
- Sıcaklıklar, basınçlar, debiler, yüzey alanları
- **Yöntem:** NLP (SQP, Interior Point, GA, PSO)
- **Detay:** `parametric_optimization.md`

### 6.4. Çok Amaçlı Optimizasyon (Multi-Objective Optimization)

Birden fazla amaçı eş zamanlı optimize et:
- min Maliyet vs max Exergy Verimi vs min CO₂
- **Yöntem:** NSGA-II, MOPSO, epsilon-constraint
- **Detay:** `multi_objective.md`

---

## 7. Termoekonomik Analiz Adımları (Genel Akış)

```
1. Sistem tanımı ve sınır belirleme
   ↓
2. Exergy analizi (her bileşen için Ėx_F, Ėx_P, Ėx_D, Ėx_L)
   ↓
3. Ekonomik analiz (yatırım maliyeti, İ&B, yakıt maliyeti)
   ↓
4. Exergoekonomik denge denklemleri + yardımcı denklemler → c ve Ċ hesapla
   ↓
5. Termoekonomik değişkenler: f_k, r_k, Ċ_D,k hesapla
   ↓
6. Yorumlama ve iyileştirme yönü belirleme
   ↓
7. Optimizasyon (iteratif / parametrik / yapısal / çok amaçlı)
   ↓
8. Duyarlılık analizi
   ↓
9. Sonuç ve karar
```

---

## 8. Sınırlılıklar ve Dikkat Edilmesi Gerekenler

1. **Veri kalitesi:** Termoekonomik analiz, doğru termodinamik ve ekonomik veriye bağlıdır.
   Eksik veya hatalı veri, sonuçları önemli ölçüde etkiler.

2. **Referans ortam:** Exergy hesaplamaları referans ortam koşullarına (T₀, P₀) bağlıdır.
   Türkiye'de mevsimsel sıcaklık farkları büyüktür (T₀ = 15-25°C).

3. **Maliyet korelasyonları:** Ekipman maliyet fonksiyonları yaklaşıktır ve CEPCI ile
   güncellenmeli, Türkiye pazar koşullarına uyarlanmalıdır.

4. **Doğrusal olmayan davranış:** Ekipman performans eğrileri doğrusal değildir; kısmi
   yükte davranış farklıdır.

5. **Dinamik koşullar:** Mevsimsel ve günlük yük değişimleri, statik optimizasyon sonuçlarını
   etkileyebilir. Yıllık ortalama ile çalışmak yaygın basitleştirmedir.

---

## İlgili Dosyalar

- `objective_functions.md` — Maliyet bileşenleri detayı
- `decision_variables.md` — Karar değişkenleri ve kısıtlar
- `iterative_method.md` — İteratif yöntem detayı
- `practical_guide.md` — Endüstriyel uygulama rehberi
- `factory/exergy_fundamentals.md` — Exergy temel kavramlar
- `factory/economic_analysis.md` — Ekonomik analiz yöntemleri

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
- Lazzaretto, A. & Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs." *Energy*, 31(8-9), 1257-1289.
- El-Sayed, Y.M. (2003). *The Thermoeconomics of Energy Conversions*. Elsevier.
- Morosuk, T. & Tsatsaronis, G. (2019). "Advanced exergy-based methods used to understand and improve energy-conversion systems." *Energy*, 169, 238-246.
