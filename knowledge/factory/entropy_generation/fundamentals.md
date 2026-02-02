---
title: "Termodinamik Temeller — Gouy-Stodola Teoremi (Thermodynamic Fundamentals — Gouy-Stodola Theorem)"
category: factory
equipment_type: factory
keywords: [entropi üretimi, Gouy-Stodola, exergy yıkımı, ikinci yasa, irreversibility, Clausius]
related_files: [factory/entropy_generation/overview.md, factory/entropy_generation/bejan_number.md, factory/exergy_fundamentals.md]
use_when: ["EGM temel kavramları sorulduğunda", "Entropi üretimi ile exergy yıkımı ilişkisi açıklanacakken", "Gouy-Stodola teoremi referans alınacakken"]
priority: high
last_updated: 2026-02-01
---
# Termodinamik Temeller — Gouy-Stodola Teoremi (Thermodynamic Fundamentals)

> Son güncelleme: 2026-02-01

## Genel Bakış

Entropi üretimi (entropy generation), termodinamik tersinmezliğin (irreversibility) en temel ölçüsüdür. Doğadaki tüm gerçek süreçler — ısı transferi, sürtünme, karışma, yanma — entropi üretir ve bu üretim asla sıfırın altına düşemez. Gouy-Stodola teoremi, entropi üretimi ile exergy yıkımı arasındaki doğrudan ve nicel bağı kurar: bir sistemde üretilen her birim entropi, referans ortam sıcaklığıyla orantılı miktarda exergy yıkımına neden olur. Bu teorem, entropi üretimi minimizasyonunun (Entropy Generation Minimization — EGM) neden endüstriyel verimliliğin anahtarı olduğunu açıklar ve mühendislere kayıp kaynakları ile potansiyel tasarruf miktarlarını birleştiren güçlü bir analiz çerçevesi sunar.

## 1. Clausius Eşitsizliği ve Entropi Üretimi (Clausius Inequality)

### 1.1 Termodinamiğin İkinci Yasası

**Fiziksel Sezgi:** Doğadaki tüm süreçlerin bir yönü vardır. Sıcak kahve soğur ama soğuk kahve kendiğinden ısınmaz; gaz genişler ama kendiliğinden sıkışmaz. Bu asimetriyi açıklayan ikinci yasadır. Enerji korunsa bile, kalitesi her dönüşümde düşer — bu düşüşün ölçüsü entropi üretimidir.

Rudolf Clausius, 1865 yılında bu gözlemi matematiksel bir eşitsizlikle ifade etmiştir. Kapalı bir termodinamik çevrim boyunca, ısı transferlerinin mutlak sıcaklığa oranlarının toplamı asla sıfırdan büyük olamaz:

```
Clausius Eşitsizliği:

  ∮ (δQ / T) ≤ 0

Burada:
  δQ  = diferansiyel ısı transferi [kJ]
  T   = sınır sıcaklığı (ısı transferinin gerçekleştiği yüzey) [K]
  ∮   = çevrimsel integral (tam çevrim boyunca)

Özel durumlar:
  ∮ (δQ / T) = 0   →  Tersinir (reversible) çevrim — ideal limit
  ∮ (δQ / T) < 0   →  Tersinmez (irreversible) çevrim — tüm gerçek çevrimler
```

Bu eşitsizlik, yeni bir durum özelliğinin — entropinin — tanımlanmasına yol açar.

### 1.2 Entropi Üretimi Tanımı

**Fiziksel Sezgi:** Entropi üretimi, bir sürecin ideale ne kadar uzak olduğunun ölçüsüdür. Sıfır entropi üretimi yalnızca tersinir süreçlerde mümkündür ve gerçek dünyada asla ulaşılamaz. Entropi üretimi ne kadar büyükse, o kadar çok iş potansiyeli (exergy) kalıcı olarak yok edilmiştir.

```
Entropi Üretimi Tanımı:

  S_gen ≥ 0    (her zaman, her yerde, istisnasız)

Burada:
  S_gen = entropi üretimi [kJ/K] veya entropi üretim hızı [kW/K]

Özel durumlar:
  S_gen = 0    →  Tersinir süreç (ideal, doğada yok)
  S_gen > 0    →  Tersinmez süreç (tüm gerçek süreçler)
  S_gen < 0    →  İMKANSIZ (ikinci yasanın ihlali)
```

Bu, termodinamiğin en temel yasalarından biridir ve hiçbir makine, proses veya doğa olayı tarafından ihlal edilemez.

### 1.3 Entropi Dengesi (Entropy Balance)

**Fiziksel Sezgi:** Enerji dengesi (birinci yasa) bize "enerji korunur" der. Entropi dengesi (ikinci yasa) ise "entropi korunmaz, her gerçek süreçte artar" der. Bir kontrol hacmine giren entropiye, süreçte üretilen entropi eklenir ve toplam çıkan entropi elde edilir. Entropi üretimi terimi (S_gen) her zaman pozitiftir ve bu terim sistemdeki tersinmezliğin doğrudan ölçüsüdür.

Açık bir kontrol hacmi (control volume) için genel entropi dengesi:

```
Kontrol Hacmi Entropi Dengesi:

  dS_cv/dt = Σ(Q̇_i / T_i) + Σ(ṁ_in × s_in) - Σ(ṁ_out × s_out) + Ṡ_gen

Burada:
  dS_cv/dt  = kontrol hacmindeki entropi değişim hızı [kW/K]
  Q̇_i      = i-inci sınırdan transfer edilen ısı akısı [kW]
  T_i       = i-inci sınırın sıcaklığı [K]
  ṁ_in      = giriş kütle debisi [kg/s]
  s_in      = giriş spesifik entropisi [kJ/(kg·K)]
  ṁ_out     = çıkış kütle debisi [kg/s]
  s_out     = çıkış spesifik entropisi [kJ/(kg·K)]
  Ṡ_gen     = entropi üretim hızı [kW/K]

Birimlerin Kontrolü:
  [kW/K] = [kW/K] + [kg/s × kJ/(kg·K)] - [kg/s × kJ/(kg·K)] + [kW/K]
  → Tüm terimler [kW/K] birimine sahip ✓
```

**Türetmenin Adım Adım Açıklaması:**

1. **Isı transferi terimi** `Σ(Q̇_i / T_i)`: Dışarıdan sınır üzerinden giren/çıkan ısı, sınır sıcaklığında entropi taşır. Sıcaklık ne kadar düşükse, aynı ısı miktarı o kadar fazla entropi taşır.

2. **Kütle akış terimleri** `Σ(ṁ_in × s_in)` ve `Σ(ṁ_out × s_out)`: Her madde akışı kendi entropisiyle birlikte entropi taşır. Giren akışlar entropi ekler, çıkan akışlar entropi çıkarır.

3. **Entropi üretim terimi** `Ṡ_gen`: Kontrol hacmi içindeki tüm tersinmez süreçlerden (sürtünme, ısı transferi sonlu ΔT üzerinden, karışma vb.) kaynaklanan net entropi üretimi. Bu terim hiçbir zaman negatif olamaz.

4. **Depolama terimi** `dS_cv/dt`: Kontrol hacminde biriken veya azalan entropi. Kararlı hal (steady-state) analizinde bu terim sıfırdır.

## 2. Gouy-Stodola Teoremi

### 2.1 Teoremin Tarihsel Gelişimi

Gouy-Stodola teoremi, termodinamiğin en zarif ve pratik sonuçlarından biridir. İki bağımsız araştırmacı tarafından ortaya konmuştur:

- **Louis Georges Gouy** (1854-1926), Fransız fizikçi, 1889 yılında "Sur l'énergie utilisable" (Kullanılabilir enerji üzerine) başlıklı makalesinde, entropi üretimi ile kayıp iş arasındaki doğrudan ilişkiyi ilk kez matematiksel olarak ifade etmiştir.

- **Aurel Stodola** (1859-1942), Slovak-İsviçreli mühendis, 1910 yılında yayımlanan "Steam and Gas Turbines" kitabında aynı sonuca bağımsız olarak ulaşmış ve bunu buhar türbinlerinin termodinamik analizine uygulamıştır.

Her iki çalışma da aynı temel gerçeğe ulaşmıştır: **Kayıp iş potansiyeli, entropi üretimi ile referans ortam sıcaklığının çarpımına eşittir.**

### 2.2 Teoremin İfadesi ve Türetmesi

**Fiziksel Sezgi:** Bir sistemde entropi üretildiğinde, bu üretim kalıcı olarak iş yapma kapasitesini (exergyyi) yok eder. Her kW/K entropi üretimi, ortam sıcaklığı T₀ ile çarpıldığında kW cinsinden exergy yıkımını verir. Daha sıcak bir ortam, aynı entropi üretimi için daha fazla exergy yıkımı anlamına gelir — çünkü referans nokta yükselmiştir.

**Teorem İfadesi:**

```
Gouy-Stodola Teoremi:

  İ = T₀ × Ṡ_gen

Burada:
  İ     = exergy yıkımı (irreversibility) hızı [kW]
  T₀    = ölü durum (dead state) sıcaklığı [K]
  Ṡ_gen = entropi üretim hızı [kW/K]

Veya birim kütle bazında:
  i = T₀ × s_gen

Burada:
  i     = spesifik exergy yıkımı [kJ/kg]
  T₀    = ölü durum sıcaklığı [K]
  s_gen = spesifik entropi üretimi [kJ/(kg·K)]
```

**Adım Adım Türetme:**

Kararlı hal (steady-state) açık bir sistem düşünelim. Birinci yasa (enerji dengesi) ve ikinci yasa (entropi dengesi) birlikte ele alınır.

```
Adım 1 — Enerji Dengesi (Birinci Yasa):
  Ẇ_gerçek = Σ(ṁ_in × h_in) - Σ(ṁ_out × h_out) + Σ Q̇_i

Adım 2 — Entropi Dengesi (İkinci Yasa):
  0 = Σ(Q̇_i / T_i) + Σ(ṁ_in × s_in) - Σ(ṁ_out × s_out) + Ṡ_gen

Adım 3 — Entropi dengesinden Q̇ terimini çöz ve T₀ ile çarp:
  T₀ × Ṡ_gen = -Σ(T₀ × Q̇_i / T_i) + T₀ × [Σ(ṁ_out × s_out) - Σ(ṁ_in × s_in)]

Adım 4 — Tersinir (ideal) durumda Ṡ_gen = 0 olur, maksimum iş elde edilir:
  Ẇ_tersinir = Ẇ_gerçek + T₀ × Ṡ_gen

Adım 5 — Kayıp iş (exergy yıkımı):
  İ = Ẇ_tersinir - Ẇ_gerçek = T₀ × Ṡ_gen

Bu, Gouy-Stodola teoremidir. ∎
```

### 2.3 Fiziksel Anlam

Gouy-Stodola teoremi mühendislik açısından olağanüstü güçlü bir araçtır:

1. **Doğrudan bağlantı:** Entropi üretimi (soyut termodinamik kavram) ile exergy yıkımı (somut enerji kaybı, kW cinsinden) arasında doğrudan, çarpımsal bir ilişki kurar.

2. **Referans ortam etkisi:** T₀ değeri, exergy yıkımının büyüklüğünü doğrudan etkiler. Sıcak iklim bölgelerinde (yüksek T₀), aynı entropi üretimi daha fazla exergy yıkımına neden olur.

3. **Evrensellik:** Teorem her türlü süreç için geçerlidir — ısı transferi, sürtünme, yanma, karışma, kimyasal reaksiyon.

**Sayısal Örnek:**

```
Veri:
  T₀ = 25°C = 298.15 K (standart referans ortam)
  Ṡ_gen = 0.1 kW/K (bir eşanjörde ölçülen entropi üretim hızı)

Hesap:
  İ = T₀ × Ṡ_gen = 298.15 × 0.1 = 29.815 kW

Yorum:
  Bu eşanjörde her saniye 29.8 kW exergy kalıcı olarak yok ediliyor.
  Yıllık bazda (8,000 saat çalışma):
  E_yıkım = 29.8 × 8,000 = 238,400 kWh/yıl ≈ 238.4 MWh/yıl

  Elektrik fiyatı 0,09 EUR/kWh ile:
  Maliyet ≈ 238.400 × 0,09 = 21.456 EUR/yıl kayıp potansiyel
```

**Farklı T₀ Değerlerinin Etkisi:**

| Konum | T₀ [K] | Ṡ_gen = 0.1 kW/K → İ [kW] | Fark |
|---|---|---|---|
| Kuzey Avrupa (5°C) | 278.15 | 27.8 | Referans |
| Standart (25°C) | 298.15 | 29.8 | +7.2% |
| Orta Doğu (40°C) | 313.15 | 31.3 | +12.6% |
| Tropikal (35°C) | 308.15 | 30.8 | +10.8% |

## 3. Entropi Üretim Hızı (Entropy Generation Rate)

### 3.1 Ṡ_gen Tanımı ve Birimi

**Fiziksel Sezgi:** Entropi üretim hızı, bir sistemin birim zamanda ne kadar termodinamik kaliteyi geri dönüşümsüz olarak yok ettiğini ölçer. Tıpkı güç (kW) kavramının birim zamandaki enerji transferini ölçmesi gibi, Ṡ_gen de birim zamandaki entropi üretimini ölçer.

```
Entropi Üretim Hızı:

  Ṡ_gen [kW/K]  — sürekli süreçlerde (flow processes)
  S_gen  [kJ/K]  — kesikli süreçlerde (batch processes)

Dönüşüm:
  Ṡ_gen = S_gen / Δt

Burada:
  Δt = proses süresi [s]
```

### 3.2 Kontrol Hacminde Ṡ_gen Hesaplama

Kararlı hal (steady-state) koşullarında, entropi dengesi denklemi basitleşir:

```
Kararlı Hal Entropi Dengesi:

  dS_cv/dt = 0  (kararlı hal)

  0 = Σ(Q̇_i / T_i) + Σ(ṁ_in × s_in) - Σ(ṁ_out × s_out) + Ṡ_gen

Bu denklemden Ṡ_gen çözülür:

  Ṡ_gen = Σ(ṁ_out × s_out) - Σ(ṁ_in × s_in) - Σ(Q̇_i / T_i)

Burada:
  Σ(ṁ_out × s_out) = çıkış akışlarının entropi taşıma hızı [kW/K]
  Σ(ṁ_in × s_in)   = giriş akışlarının entropi taşıma hızı [kW/K]
  Σ(Q̇_i / T_i)     = ısı transferi ile entropi taşıma hızı [kW/K]
                       (sisteme giren ısı pozitif, çıkan negatif)
```

### 3.3 Farklı Süreçlerde Ṡ_gen

Aşağıdaki tablo, endüstriyel sistemlerde sık karşılaşılan süreçlerin entropi üretim formüllerini ve tipik büyüklüklerini özetler.

| Süreç Tipi | Ṡ_gen Formülü | Tipik Değer Aralığı | Ana Parametre |
|---|---|---|---|
| Sonlu ΔT ısı transferi | Q̇ × (1/T_soğuk - 1/T_sıcak) | 0.01 - 1.0 kW/K | ΔT büyüklüğü |
| Akış sürtünmesi (ΔP) | ṁ × ΔP / (ρ × T) | 0.001 - 0.1 kW/K | ΔP ve debi |
| Akışkan karışması | -ṁ × Σ(x_i × R × ln(x_i)) | 0.005 - 0.05 kW/K | Konsantrasyon farkı |
| Yanma (combustion) | Kazan: 0.5 - 5.0 kW/K | 0.5 - 5.0 kW/K | Yakıt cinsi, alev T |
| Kısma (throttling) | ṁ × R × ln(P₁/P₂) / M | 0.01 - 0.5 kW/K | Basınç oranı |
| Çevre ile ısı kaybı | Q̇_kayıp × (1/T₀ - 1/T_yüzey) | 0.001 - 0.1 kW/K | İzolasyon kalitesi |

## 4. Entropi Üretim Sayısı (Entropy Generation Number)

### 4.1 N_s Tanımı

**Fiziksel Sezgi:** Farklı boyuttaki ekipmanları karşılaştırabilmek için boyutsuz bir sayıya ihtiyacımız vardır. Tıpkı Reynolds sayısının farklı boyuttaki borularda akış rejimini karşılaştırmayı sağlaması gibi, entropi üretim sayısı (N_s) da farklı kapasitedeki ekipmanların termodinamik performansını karşılaştırmayı sağlar.

Adrian Bejan tarafından tanımlanan entropi üretim sayısı:

```
Entropi Üretim Sayısı (Entropy Generation Number):

  N_s = Ṡ_gen / Ṡ_gen,max

  veya alternatif tanımlar:

  N_s = Ṡ_gen / (Q̇ / T_min)        — ısı transferi cihazları için
  N_s = Ṡ_gen / (ṁ × c_p)           — akışkan akış sistemleri için
  N_s = T₀ × Ṡ_gen / Ẇ             — iş üreten/tüketen cihazlar için

Burada:
  N_s = boyutsuz entropi üretim sayısı [-]
  Ṡ_gen,max = referans (maksimum) entropi üretim hızı [kW/K]
  Q̇ = ısı transfer hızı [kW]
  T_min = minimum sıcaklık [K]
  ṁ = kütle debisi [kg/s]
  c_p = sabit basınçta özgül ısı [kJ/(kg·K)]
  Ẇ = güç [kW]
```

### 4.2 Boyutsuz Analiz Avantajı

Boyutsuz sayılar kullanmanın mühendislik avantajları:

1. **Ölçek bağımsızlığı:** 100 kW'lık bir eşanjör ile 10,000 kW'lık bir eşanjör, N_s üzerinden doğrudan karşılaştırılabilir.
2. **Evrensel benchmark:** Sektör ve kapasite fark etmeksizin, N_s → 0 ideal (tersinir) sınırı, N_s → 1 ise maksimum tersinmezlik sınırını temsil eder.
3. **Optimizasyon kolaylığı:** Tasarım parametreleri (debi, boyut, malzeme) değiştirilirken N_s'nin minimumunu aramak, optimal tasarıma yol gösterir.
4. **Korelasyon geliştirme:** N_s, geometrik ve akış parametreleriyle ilişkilendirilerek genel tasarım korelasyonları oluşturulabilir.

### 4.3 N_s Benchmark Değerleri

| Ekipman Tipi | N_s Aralığı (Tipik) | N_s (En İyi Uygulama) | Açıklama |
|---|---|---|---|
| Karşı akışlı eşanjör | 0.01 - 0.10 | < 0.02 | Düşük ΔT, yüksek NTU |
| Paralel akışlı eşanjör | 0.05 - 0.30 | < 0.08 | Doğal ΔT sınırlaması |
| Buhar kazanı | 0.25 - 0.45 | 0.20 - 0.30 | Yanma baskın |
| Kompresör | 0.15 - 0.35 | 0.10 - 0.18 | İzentropik verime bağlı |
| Pompa | 0.05 - 0.20 | 0.03 - 0.08 | Sıvı sıkıştırma, düşük T artışı |
| Chiller | 0.20 - 0.40 | 0.15 - 0.25 | Kısma + ısı transferi |
| Buhar türbini | 0.10 - 0.25 | 0.05 - 0.12 | İzentropik verime bağlı |
| Soğutma kulesi | 0.05 - 0.15 | 0.03 - 0.08 | Kütle transferi baskın |

## 5. Entropi Üretiminin Kaynakları

### 5.1 Isı Transferi İrreversiblliği (Heat Transfer Irreversibility)

**Fiziksel Sezgi:** Isı her zaman sıcaktan soğuğa akar. Bu doğal akış yönü entropi üretir çünkü yüksek kaliteli (yüksek sıcaklıktaki) enerji düşük kaliteli (düşük sıcaklıktaki) enerjiye dönüşür. Sıcaklık farkı (ΔT) ne kadar büyükse, entropi üretimi o kadar fazladır. İdeal (tersinir) ısı transferi yalnızca sonsuz küçük ΔT ile mümkündür — ki bu sonsuz eşanjör alanı gerektirir.

```
Sonlu Sıcaklık Farkı Üzerinden Isı Transferi:

  Ṡ_gen,ΔT = Q̇ × (1/T_soğuk - 1/T_sıcak)

Burada:
  Q̇       = transfer edilen ısı akısı [kW]
  T_soğuk  = ısıyı alan (soğuk) tarafın sıcaklığı [K]
  T_sıcak  = ısıyı veren (sıcak) tarafın sıcaklığı [K]

Sayısal Örnek:
  Q̇ = 500 kW ısı transferi
  T_sıcak = 400°C = 673.15 K (baca gazı)
  T_soğuk = 200°C = 473.15 K (buhar)

  Ṡ_gen,ΔT = 500 × (1/473.15 - 1/673.15)
           = 500 × (0.002114 - 0.001485)
           = 500 × 0.000629
           = 0.315 kW/K

  Exergy yıkımı (T₀ = 298.15 K):
  İ_ΔT = 298.15 × 0.315 = 93.9 kW

Not: ΔT azaldıkça entropi üretimi azalır ancak eşanjör alanı
(ve dolayısıyla yatırım maliyeti) artar. Bu, termodinamik
optimizasyonun temelini oluşturur.
```

### 5.2 Akış Sürtünmesi İrreversiblliği (Fluid Friction Irreversibility)

**Fiziksel Sezgi:** Akışkan bir borudan veya ekipmandan geçerken basınç düşüşü (ΔP) yaşar. Bu basınç düşüşü, akışkan kinetik enerjisinin sürtünme ile ısıya dönüşmesinden kaynaklanır. Oluşan ısı düşük sıcaklıkta olduğu için düşük kaliteli enerjidir ve bu kalite düşüşü entropi üretimi olarak kendini gösterir.

```
Akış Sürtünmesinden Entropi Üretimi:

  Ṡ_gen,ΔP = ṁ × ΔP / (ρ × T)

Burada:
  ṁ  = kütle debisi [kg/s]
  ΔP = basınç düşüşü [kPa]
  ρ  = akışkan yoğunluğu [kg/m³]
  T  = akışkan sıcaklığı [K]

İdeal gaz için alternatif formül:
  Ṡ_gen,ΔP = ṁ × R × ln(P_giriş / P_çıkış) / M

Burada:
  R = evrensel gaz sabiti = 8.314 kJ/(kmol·K)
  M = mol kütlesi [kg/kmol]

Sayısal Örnek:
  Buhar hattında basınç düşüşü:
  ṁ = 2 kg/s, ΔP = 50 kPa, ρ = 5.0 kg/m³, T = 453.15 K (180°C)

  Ṡ_gen,ΔP = 2 × 50 / (5.0 × 453.15)
           = 100 / 2265.75
           = 0.0441 kW/K

  İ_ΔP = 298.15 × 0.0441 = 13.2 kW exergy yıkımı
```

### 5.3 Karışma İrreversiblliği (Mixing Irreversibility)

**Fiziksel Sezgi:** Farklı sıcaklıkta veya bileşimde iki akışkan karıştırıldığında, homojen bir karışım oluşur ancak bu süreç tersinmezdir. Karışımı geri ayırmak için iş gerekir. Endüstride bu durum; farklı sıcaklıktaki buhar hatlarının birleştirilmesinde, kondens ve taze su karıştırılmasında sık karşılaşılır.

```
Farklı Sıcaklıktaki İki Akışın Karışması:

  Ṡ_gen,karışım = ṁ₁ × c_p × ln(T_karışım/T₁) + ṁ₂ × c_p × ln(T_karışım/T₂)

Burada:
  T_karışım = (ṁ₁ × T₁ + ṁ₂ × T₂) / (ṁ₁ + ṁ₂)  [K]

Farklı Bileşimdeki İdeal Gazların Karışması:
  Ṡ_gen,karışım = -R_u × Σ(n_i × ln(x_i))

Burada:
  R_u = 8.314 kJ/(kmol·K)
  n_i = i-inci bileşenin mol akış hızı [kmol/s]
  x_i = karışımdaki mol oranı [-]
```

### 5.4 Kimyasal Reaksiyon İrreversiblliği (Chemical Reaction Irreversibility)

**Fiziksel Sezgi:** Yanma (combustion), endüstriyel sistemlerdeki en büyük tek entropi üretim kaynağıdır. Yakıtın kimyasal exergisi (yüksek kalite), yanma sonucunda ısı enerjisine (daha düşük kalite) dönüşür. Bu kalite düşüşü kaçınılmazdır ancak büyüklüğü azaltılabilir.

```
Yanma Entropi Üretimi:

  Ṡ_gen,yanma = Σ(n_ürün × s̄_ürün) - Σ(n_reaktif × s̄_reaktif) - Q̇_yanma / T_alev

Basitleştirilmiş Yaklaşım:
  Ṡ_gen,yanma ≈ ṁ_yakıt × ex_ch × f_irr / T₀

Burada:
  f_irr = tersinmezlik oranı (yakıt türüne bağlı)

Tipik f_irr Değerleri:
  Doğalgaz (CH₄):       f_irr ≈ 0.25 - 0.30
  Dizel/fuel oil:       f_irr ≈ 0.28 - 0.33
  Kömür:                f_irr ≈ 0.30 - 0.35
  Biyokütle (odun):     f_irr ≈ 0.32 - 0.38
  Hidrojen (H₂):        f_irr ≈ 0.18 - 0.22

Örnek — Doğalgaz Kazanı:
  ṁ_yakıt = 0.1 kg/s, LHV = 50,000 kJ/kg
  ex_ch = 1.04 × LHV = 52,000 kJ/kg
  Yakıt exergy girişi = 0.1 × 52,000 = 5,200 kW
  Yanma tersinmezliği ≈ 0.27 × 5,200 = 1,404 kW exergy yıkımı

  Bu, yakıt exergisinin %27'sinin yanma sırasında kalıcı olarak
  yok edildiği anlamına gelir — kazanın diğer tüm kayıplarından
  önce dahi %27 exergy kaybedilmiştir.
```

### 5.5 Kısma İrreversiblliği (Throttling Irreversibility)

**Fiziksel Sezgi:** Kısma (throttling), basıncın bir kısıtlama (vana, orifis) üzerinden iş üretmeden düşürülmesidir. Entalpi korunur (h₁ = h₂) ancak basınç düşüşü entropi artışına neden olur. Mühendisler bu kaybı genellikle küçümser, oysa özellikle buhar ve soğutma sistemlerinde kısma kayıpları oldukça büyük olabilir.

```
Kısma Entropi Üretimi:

  İdeal gaz için:
  s_gen = c_p × ln(T₂/T₁) - R × ln(P₂/P₁) / M
        ≈ -R × ln(P₂/P₁) / M     (T₁ ≈ T₂ ideal gaz kısması)

  Buhar için:
  s_gen = s₂ - s₁   (buhar tablolarından, h₁ = h₂ koşulunda)

Sayısal Örnek — Buhar Kısması:
  10 bar doymuş buhar → 3 bar'a kısılıyor
  h₁ = 2,778 kJ/kg (10 bar doymuş buhar)
  h₂ = h₁ = 2,778 kJ/kg (kısma: izentalp)
  s₁ = 6.586 kJ/(kg·K)
  s₂ = 7.121 kJ/(kg·K) (3 bar, h = 2,778 kJ/kg → kızgın buhar)

  s_gen = 7.121 - 6.586 = 0.535 kJ/(kg·K)

  ṁ = 1 kg/s ise:
  Ṡ_gen = 1 × 0.535 = 0.535 kW/K
  İ = 298.15 × 0.535 = 159.5 kW exergy yıkımı!

  Bu örnekte, basit bir kısma vanası 159.5 kW exergy yok ediyor.
  Alternatif: Basınç düşürücü istasyonu yerine geri basınçlı türbin
  kullanılsaydı, bu exerginin bir kısmı elektrik olarak geri
  kazanılabilirdi.
```

## 6. Entropi Dengesi — Kontrol Hacmi Formülasyonu

### 6.1 Açık Sistem Entropi Dengesi (Open System)

**Fiziksel Sezgi:** Bir fabrikadaki her ekipman bir açık sistem (kontrol hacmi) olarak modellenebilir: madde girer, madde çıkar, ısı transfer olur ve iç süreçler entropi üretir. Tüm bu terimleri bir araya getiren tam formülasyon, her ekipmanın tersinmezliğini hesaplamanın temelidir.

```
Genel Açık Sistem Entropi Dengesi:

  dS_cv/dt = Σⱼ(Q̇ⱼ / Tⱼ) + Σᵢ(ṁᵢ,giriş × sᵢ,giriş) - Σₖ(ṁₖ,çıkış × sₖ,çıkış) + Ṡ_gen

  ┌─────────┐   ┌──────────┐   ┌──────────────┐   ┌───────────────┐   ┌──────┐
  │ Entropi  │ = │ Isı ile  │ + │ Kütle ile    │ - │ Kütle ile     │ + │Üretim│
  │ birikimi │   │ gelen    │   │ gelen entropi│   │ çıkan entropi │   │      │
  └─────────┘   └──────────┘   └──────────────┘   └───────────────┘   └──────┘
  [kW/K]         [kW/K]         [kW/K]              [kW/K]              [kW/K]

Her terim:
  dS_cv/dt           — kontrol hacmindeki entropi değişim hızı
  Q̇ⱼ / Tⱼ           — j-inci sınırdan ısı transferi ile entropi akısı
  ṁᵢ,giriş × sᵢ     — i-inci giriş akışının taşıdığı entropi
  ṁₖ,çıkış × sₖ     — k-inci çıkış akışının taşıdığı entropi
  Ṡ_gen              — iç tersinmezliklerden üretilen entropi (≥ 0)
```

### 6.2 Kararlı Hal Basitleştirmesi (Steady-State)

Endüstriyel ekipmanların büyük çoğunluğu kararlı halde çalışır. Bu durumda depolama terimi sıfır olur ve denklem önemli ölçüde basitleşir:

```
Kararlı Hal (dS_cv/dt = 0):

  Ṡ_gen = Σₖ(ṁₖ,çıkış × sₖ) - Σᵢ(ṁᵢ,giriş × sᵢ) - Σⱼ(Q̇ⱼ / Tⱼ)

Tek giriş — tek çıkış (birçok ekipman):

  Ṡ_gen = ṁ × (s_çıkış - s_giriş) - Q̇ / T_sınır

Adyabatik (ısı transferi yok, Q̇ = 0):

  Ṡ_gen = ṁ × (s_çıkış - s_giriş)    [her zaman ≥ 0]

Gouy-Stodola ile:
  İ = T₀ × Ṡ_gen   →  exergy yıkımı doğrudan hesaplanır
```

### 6.3 Uygulama Örneği — Eşanjör Entropi Üretimi

**Problem:** Bir karşı akışlı (counterflow) eşanjörde, sıcak akışkan (yağ) soğuk akışkanı (su) ısıtmaktadır. Eşanjördeki entropi üretimini ve exergy yıkımını hesaplayınız.

```
Veriler:
  Sıcak Akışkan (Yağ):
    ṁ_h = 3.0 kg/s
    T_h,giriş = 150°C = 423.15 K
    T_h,çıkış = 90°C = 363.15 K
    c_p,h = 2.1 kJ/(kg·K)

  Soğuk Akışkan (Su):
    ṁ_c = 2.0 kg/s
    T_c,giriş = 30°C = 303.15 K
    T_c,çıkış = 80°C = 353.15 K
    c_p,c = 4.18 kJ/(kg·K)

  Ortam: T₀ = 25°C = 298.15 K
  Varsayım: Adyabatik eşanjör (dışa ısı kaybı yok)

Adım 1 — Enerji Dengesi Kontrolü:
  Q̇_h = ṁ_h × c_p,h × (T_h,giriş - T_h,çıkış)
       = 3.0 × 2.1 × (150 - 90) = 378 kW

  Q̇_c = ṁ_c × c_p,c × (T_c,çıkış - T_c,giriş)
       = 2.0 × 4.18 × (80 - 30) = 418 kW

  Not: Hafif fark (378 vs 418 kW) veri yuvarlamasından. Gerçek
  analizde Q̇_h = Q̇_c olmalıdır. Devam için Q̇ = 378 kW kullanılır
  ve soğuk çıkış sıcaklığı buna göre düzeltilir:
  T_c,çıkış_düzeltme = 30 + 378/(2.0 × 4.18) = 75.2°C = 348.35 K

Adım 2 — Entropi Değişimleri:
  ΔṠ_h = ṁ_h × c_p,h × ln(T_h,çıkış / T_h,giriş)
        = 3.0 × 2.1 × ln(363.15 / 423.15)
        = 6.3 × ln(0.8582)
        = 6.3 × (-0.1529)
        = -0.9633 kW/K

  ΔṠ_c = ṁ_c × c_p,c × ln(T_c,çıkış / T_c,giriş)
        = 2.0 × 4.18 × ln(348.35 / 303.15)
        = 8.36 × ln(1.1490)
        = 8.36 × 0.1390
        = 1.1620 kW/K

Adım 3 — Entropi Üretimi (adyabatik eşanjör):
  Ṡ_gen = ΔṠ_h + ΔṠ_c
        = -0.9633 + 1.1620
        = 0.1987 kW/K

  Kontrol: Ṡ_gen > 0 ✓ (ikinci yasa sağlanıyor)

Adım 4 — Exergy Yıkımı (Gouy-Stodola):
  İ = T₀ × Ṡ_gen
    = 298.15 × 0.1987
    = 59.24 kW

Sonuç: Bu eşanjörde 59.24 kW exergy kalıcı olarak yok ediliyor.
Transfer edilen 378 kW ısının yaklaşık %15.7'sine karşılık gelen
bu exergy yıkımı, sıcak ve soğuk akışkanlar arasındaki sıcaklık
farkından kaynaklanmaktadır.
```

## 7. Pratik Mühendislik Kuralları

Entropi üretimi minimizasyonunu (EGM) günlük mühendislik pratiğine bağlayan pratik kurallar:

### 7.1 Isı Transferi Kuralları

```
Kural 1: Her 10°C gereksiz ΔT, yaklaşık 0.001-0.003 kW/K entropi üretir
         (100 kW ısı transferi başına).

  Örnek: 100 kW, ΔT = 50°C → Ṡ_gen ≈ 0.015 kW/K → İ ≈ 4.5 kW
         100 kW, ΔT = 20°C → Ṡ_gen ≈ 0.005 kW/K → İ ≈ 1.5 kW
         %67 azalma!

Kural 2: Eşanjör approach temperature (yaklaşma sıcaklığı) her 5°C
         düşürüldüğünde, exergy verimi yaklaşık %2-4 artar.

Kural 3: Isı kademesi (cascading) her zaman doğrudan ısı transferinden
         termodinamik olarak üstündür.
         500°C baca gazı → doğrudan 80°C su ısıtma YERINE
         500°C → 200°C buhar → 80°C su (kademeli) tercih edilmeli.
```

### 7.2 Basınç Düşüşü Kuralları

```
Kural 4: Boru çapını %20 artırmak, basınç düşüşünü yaklaşık %50 azaltır
         (hız karesine bağlı). Bu da sürtünme entropi üretimini yarılar.

Kural 5: Her 1 bar gereksiz basınç düşüşü, kompresörlerde yaklaşık
         %6-8 ek enerji tüketimi (ve karşılık gelen entropi üretimi)
         demektir.
```

### 7.3 Kısma ve Genleşme Kuralları

```
Kural 6: Kısma, mühendislerin en çok hafife aldığı entropi üretim
         kaynağıdır. Basınç düşürücü vana yerine geri basınçlı türbin,
         genleşme vanası yerine ejektör veya ekspander düşünülmelidir.

Kural 7: Buhar sistemlerinde, 10 bar → 3 bar kısma yaklaşık 160 kW/ton
         exergy yok eder. Bu, küçük bir türbinle %40-60 oranında
         elektriğe dönüştürülebilir.
```

### 7.4 Yanma Kuralları

```
Kural 8: Yanma tersinmezliği yakıt exergisinin %25-35'idir ve
         sıfıra indirilemez. Ancak şu yöntemlerle %3-8 azaltılabilir:
         - Yanma havası ön ısıtma (recuperator): %2-4 azalma
         - Oksijen zenginleştirme: %3-5 azalma
         - Flameless combustion (FLOX): %2-3 azalma

Kural 9: Adyabatik alev sıcaklığını artırmak yanma tersinmezliğini
         azaltır. Ancak NOx oluşumu ile çelişir — bu optimizasyon
         dikkatli yapılmalıdır.

Kural 10: Yakıt hücresi (fuel cell), yanma yerine elektrokimyasal
          reaksiyon kullandığı için yanma tersinmezliğini büyük ölçüde
          (%50-70) azaltır. Uzun vadeli strateji olarak değerlendirilmelidir.
```

### 7.5 Hızlı Değerlendirme Tablosu

| Entropi Üretim Kaynağı | Tipik Pay (Toplam İ İçinde) | Azaltma Potansiyeli | Yatırım Seviyesi |
|---|---|---|---|
| Yanma | %35-50 | %5-15 | Orta-Yüksek |
| Isı transferi (sonlu ΔT) | %20-35 | %30-50 | Orta |
| Kısma (throttling) | %5-15 | %40-70 | Düşük-Orta |
| Akış sürtünmesi | %3-8 | %30-50 | Düşük |
| Karışma | %2-5 | %50-80 | Düşük |
| Çevreye ısı kaybı | %3-10 | %60-80 | Düşük |

## 8. İleri Konulara Köprü

### 8.1 Bejan Sayısı (Bejan Number)

Gouy-Stodola teoremi, entropi üretiminin toplam miktarını verir. Bejan sayısı (Be), bu toplam entropi üretiminin ne kadarının ısı transferinden, ne kadarının akış sürtünmesinden kaynaklandığını ayırt eder:

```
Be = Ṡ_gen,ΔT / (Ṡ_gen,ΔT + Ṡ_gen,ΔP)

Be → 1: Isı transferi tersinmezliği baskın
Be → 0: Akış sürtünmesi tersinmezliği baskın
Be ≈ 0.5: Optimal tasarım noktası (EGM optimizasyonu)

Detay için bkz: bejan_number.md
```

### 8.2 Thermoeconomics ile Bağlantı

Gouy-Stodola teoremi, termoekonomik analizin (thermoeconomics) temelidir. Exergy yıkımına parasal değer atandığında:

```
Ċ_yıkım = c_F × İ = c_F × T₀ × Ṡ_gen  [EUR/saat]

Burada:
  c_F = yakıt exergisinin birim maliyeti [EUR/kWh]

Bu formül, entropi üretiminin doğrudan mali sonucunu gösterir.
```

## İlgili Dosyalar

- [overview.md](factory/entropy_generation/overview.md) — EGM genel bakış ve yol haritası
- [bejan_number.md](factory/entropy_generation/bejan_number.md) — Bejan sayısı detaylı analiz
- [exergy_fundamentals.md](factory/exergy_fundamentals.md) — Exergy temelleri ve fabrika analizi
- [cross_equipment.md](factory/cross_equipment.md) — Ekipmanlar arası exergy entegrasyonu
- [prioritization.md](factory/prioritization.md) — İyileştirme önceliklendirme metodolojisi

## Referanslar

- Bejan, A. "Entropy Generation Minimization" (CRC Press, 1996)
- Bejan, A. "Advanced Engineering Thermodynamics" (Wiley, 4th ed., 2016)
- Bejan, A. "Entropy Generation Through Heat and Fluid Flow" (Wiley, 1982)
- Gouy, G. "Sur l'énergie utilisable" Journal de Physique, Théorique et Appliquée, 8(1), 501-518 (1889)
- Stodola, A. "Steam and Gas Turbines" (McGraw-Hill, 1910; revised 1927)
- Clausius, R. "Über verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie" (1865)
- Szargut, J., Morris, D.R., Steward, F.R. "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes" (Hemisphere Publishing, 1988)
- Dincer, I. & Rosen, M.A. "Exergy: Energy, Environment and Sustainable Development" (Elsevier, 3rd ed., 2021)
- Tsatsaronis, G. "Definitions and nomenclature in exergy analysis and exergoeconomics" Energy, 32(4), 249-253 (2007)
- Sciubba, E. "Exergy as a direct measure of environmental impact" ASME AES, 39, 573-581 (1999)
