---
title: "Bejan Sayısı ve Entropi Üretim Sayısı (Bejan Number & Entropy Generation Number)"
category: factory
equipment_type: factory
keywords: [Bejan sayısı, entropi üretim sayısı, N_s, Be, irreversibility dağılımı]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/heat_transfer_egm.md, factory/entropy_generation/fluid_flow_egm.md]
use_when: ["Irreversibility kaynaklarını ayırt etmek gerektiğinde", "Isı transferi vs sürtünme baskınlığı belirlenecekken", "Bejan sayısı referans alınacakken"]
priority: high
last_updated: 2026-02-01
---

# Bejan Sayısı ve Entropi Üretim Sayısı (Bejan Number & Entropy Generation Number)

Endüstriyel sistemlerde entropi üretiminin (entropy generation) toplam büyüklüğünü bilmek
yeterli değildir. Mühendislik açısından kritik soru şudur: **bu geri dönüşümsüzlük
(irreversibility) nereden kaynaklanıyor?** Bejan sayısı (Be) ve entropi üretim sayısı (N_s),
bu soruyu sistematik ve boyutsuz (dimensionless) biçimde yanıtlayan iki temel göstergedir.

Bu dosya, her iki parametrenin tanımını, türetmesini, fiziksel yorumunu ve endüstriyel
uygulamalarını kapsamlı olarak ele almaktadır.

---

## 1. Bejan Sayısı (Bejan Number — Be)

### 1.1 Tanım ve Türetme

#### Fiziksel Sezgi (Physical Intuition)

Bir akışkan bir boru veya ısı değiştirici içinden geçerken iki temel mekanizma entropi üretir:

1. **Isı transferi sonlu sıcaklık farkıyla (finite temperature difference):** Sıcak taraftan
   soğuk tarafa ısı geçerken sıcaklık gradyanı boyunca tersinmezlik oluşur. Sıcaklık farkı
   (ΔT) ne kadar büyükse, üretilen entropi o kadar fazladır.

2. **Akışkan sürtünmesi (fluid friction / viscous dissipation):** Akışkan hareket ederken
   basınç düşümü (ΔP) yaşar. Bu basınç kaybı, mekanik enerjinin ısıya dönüşmesinden
   kaynaklanır ve geri dönüşümsüzdür.

Bejan sayısı, toplam entropi üretiminin ne kadarının ısı transferi kaynaklı olduğunu ifade
eden boyutsuz bir orandır. Başka bir deyişle: **"Toplam geri dönüşümsüzlüğün hangi kesri
ısı transferinden, hangi kesri sürtünmeden geliyor?"** sorusunu yanıtlar.

#### Matematiksel Tanım

Toplam entropi üretim hızı (total entropy generation rate) iki bileşene ayrılır:

**Adım 1 — Bileşenlerin tanımlanması:**

Isı transferi kaynaklı entropi üretimi:

```
Ṡ_gen,ΔT = Q̇² / (k × T² × A)     [W/K]
```

Burada:
- Q̇ : Isı transfer hızı [W]
- k  : Isıl iletkenlik katsayısı (thermal conductivity) [W/(m·K)]
- T  : Mutlak sıcaklık [K]
- A  : Isı transfer alanı [m²]

Akışkan sürtünmesi kaynaklı entropi üretimi:

```
Ṡ_gen,ΔP = ṁ × ΔP / (ρ × T)       [W/K]
```

Burada:
- ṁ  : Kütle debisi (mass flow rate) [kg/s]
- ΔP : Basınç düşümü (pressure drop) [Pa]
- ρ  : Akışkan yoğunluğu [kg/m³]
- T  : Mutlak sıcaklık [K]

**Adım 2 — Toplam entropi üretimi:**

```
Ṡ_gen,toplam = Ṡ_gen,ΔT + Ṡ_gen,ΔP     [W/K]
```

**Adım 3 — Bejan sayısının tanımlanması:**

```
Be = Ṡ_gen,ΔT / (Ṡ_gen,ΔT + Ṡ_gen,ΔP)
```

Veya eşdeğer olarak:

```
Be = Ṡ_gen,ΔT / Ṡ_gen,toplam
```

**Sınır değerler:**
- Be = 1 → Tüm geri dönüşümsüzlük ısı transferi kaynaklı (sürtünme ihmal edilebilir)
- Be = 0 → Tüm geri dönüşümsüzlük sürtünme kaynaklı (ısı transferi ihmal edilebilir)
- 0 ≤ Be ≤ 1

**Adım 4 — Tamamlayıcı oran:**

Sürtünme baskınlık oranı (friction irreversibility ratio) şu şekilde tanımlanır:

```
φ = Ṡ_gen,ΔP / Ṡ_gen,ΔT
```

Bu durumda Bejan sayısı ile ilişkisi:

```
Be = 1 / (1 + φ)
```

Bu ifade, φ → 0 iken Be → 1 (ısı transferi baskın), φ → ∞ iken Be → 0 (sürtünme baskın)
sonucunu verir ve fiziksel beklentiyle tam uyumludur.

---

### 1.2 Fiziksel Yorumlama

#### Be > 0.5 — Isı Transferi Baskın Rejim (Heat Transfer Dominant Regime)

Bejan sayısı 0.5'in üzerindeyse, sistemdeki toplam entropi üretiminin yarısından fazlası
sonlu sıcaklık farkı kaynaklıdır. Bu durumda mühendislik stratejisi:

- **Isı transfer alanını artırmak:** Daha büyük ısı değiştirici yüzeyi ΔT'yi azaltır.
  Örneğin, kanatçıklı yüzeyler (finned surfaces) veya ek plaka eklemek.
- **Karşı akış (counterflow) düzenine geçmek:** Paralel akışa kıyasla ortalama sıcaklık
  farkını düşürür, böylece Ṡ_gen,ΔT azalır.
- **Isı geri kazanımı (heat recovery) eklemek:** Atık ısıyı kullanarak sisteme giren
  akışkanı ön ısıtmak, dış kaynak ile aradaki ΔT'yi küçültür.
- **Kademe sayısını artırmak:** Çok kademeli (multi-stage) ısıtma/soğutma ile her kademede
  daha küçük ΔT elde edilir.

**Pratik örnek:** Bir buhar kazanında (boiler) yanma gazları 1200°C iken su 180°C'de
buharlaşıyor. ΔT ≈ 1020°C gibi çok büyük bir değerdir. Bu sistemde Be tipik olarak
0.7–0.9 aralığındadır, yani iyileştirme önceliği ısı transferi tarafındadır.

#### Be < 0.5 — Sürtünme Baskın Rejim (Friction Dominant Regime)

Bejan sayısı 0.5'in altındaysa, akışkan sürtünmesi toplam geri dönüşümsüzlüğe baskın
katkıda bulunur. Bu durumda:

- **Boru çapını artırmak:** Daha büyük çap, Reynolds sayısını düşürür ve sürtünme kayıplarını
  azaltır. Basınç düşümü çap ile ters orantılı olarak azalır (ΔP ∝ 1/D⁵ türbülanslı akış).
- **Yüzey pürüzlülüğünü (surface roughness) azaltmak:** Daha düzgün iç yüzeyler sürtünme
  faktörünü (friction factor, f) düşürür.
- **Vana ve dirsek sayısını azaltmak:** Her lokal kayıp elemanı ek basınç düşümü yaratır.
  Boru hattı güzergahını optimize etmek toplam ΔP'yi azaltır.
- **Debileri gözden geçirmek:** Gereğinden fazla debi, sürtünme kayıplarını kuadratik olarak
  artırır (ΔP ∝ ṁ²).

**Pratik örnek:** Uzun bir soğutma suyu hattında pompa 150 kPa basınç düşümüne karşı
çalışıyor, ancak ΔT sadece 5°C. Bu sistemde Be ≈ 0.15–0.30 olabilir; iyileştirme önceliği
boru hattı ve akış direncindedir.

#### Be = 0.5 — Denge Noktası (Optimal Balance Point)

Bejan sayısı tam olarak 0.5 olduğunda, ısı transferi ve sürtünme kaynaklı entropi üretimi
eşittir:

```
Ṡ_gen,ΔT = Ṡ_gen,ΔP    →    Be = 0.5
```

Bu nokta, bazı optimizasyon problemlerinde (özellikle ısı değiştiricilerin boyutlandırılmasında)
**termodinamik optimum** olarak ortaya çıkar. Sebebi şudur:

- Isı transfer alanını artırmak Ṡ_gen,ΔT'yi düşürür ama akış direncini (dolayısıyla
  Ṡ_gen,ΔP'yi) artırabilir.
- Boru çapını artırmak Ṡ_gen,ΔP'yi düşürür ama kompakt tasarımda ısı transfer etkinliğini
  azaltabilir.

Bu iki karşıt etki arasındaki denge noktası, toplam entropi üretiminin minimuma ulaştığı
noktadır ve burada sıklıkla Be ≈ 0.5 gözlemlenir. Ancak bu her zaman geçerli değildir;
spesifik geometri ve çalışma koşullarına bağlıdır.

---

### 1.3 Endüstriyel Tipik Be Değerleri

Aşağıdaki tablo, yaygın endüstriyel ekipman ve bileşenler için tipik Bejan sayısı
aralıklarını, baskın geri dönüşümsüzlük kaynağını ve öncelikli iyileştirme aksiyonunu
özetlemektedir.

| Ekipman / Bileşen                      | Tipik Be Aralığı | Baskın Kaynak        | Öncelikli Aksiyon                          |
|-----------------------------------------|-------------------|----------------------|--------------------------------------------|
| Borulu ısı değiştirici (shell & tube)   | 0.50 – 0.80       | Isı transferi (ΔT)  | Transfer alanı artırma, karşı akış düzeni  |
| Plakalı ısı değiştirici (plate HX)     | 0.30 – 0.60       | Karışık / sürtünme   | Plaka aralığı ve kanal geometrisi optimize |
| Borular ve kanallar (pipes/ducts)       | 0.10 – 0.40       | Sürtünme (ΔP)        | Çap artırma, yüzey pürüzlülüğü azaltma    |
| Kazanlar (boilers)                      | 0.70 – 0.90       | Isı transferi (ΔT)   | Ekonomizer, hava ön ısıtıcı, kademeli ısı  |
| Chiller — kondenser (condenser)         | 0.60 – 0.80       | Isı transferi (ΔT)   | Kondenser temizliği, yaklaşma ΔT azaltma   |
| Chiller — evaporatör (evaporator)       | 0.50 – 0.70       | Karışık               | Soğutucu akışkan seçimi, alan artırma      |
| Kompresörler (compressors)              | 0.20 – 0.50       | Sürtünme / mekanik   | Kademe sayısı artırma, ara soğutma          |
| Soğutma kuleleri (cooling towers)       | 0.60 – 0.80       | Isı transferi (ΔT)   | Dolgu malzemesi iyileştirme, hava debisi    |
| Pompalar (pumps)                        | 0.10 – 0.35       | Sürtünme / mekanik   | Pompa verimliliği, debi optimizasyonu       |
| Buhar türbinleri (steam turbines)       | 0.25 – 0.55       | Karışık               | Kademe tasarımı, sızdırmazlık iyileştirme   |
| Kurutucular (dryers)                    | 0.65 – 0.85       | Isı transferi (ΔT)   | Egzoz ısısı geri kazanımı, ön ısıtma       |
| Yoğuşturucular (condensers — genel)    | 0.55 – 0.75       | Isı transferi (ΔT)   | Soğutma suyu sıcaklığı, fouling kontrolü   |

> **Not:** Bu değerler genel yönlendirme amaçlıdır. Gerçek Be değeri, spesifik tasarım
> parametreleri, işletme koşulları ve akışkan özelliklerine göre değişir. Ölçüm ve
> hesaplama ile doğrulanmalıdır.

---

### 1.4 Be Haritası — Ekipman Tipine Göre Aralıklar

Aşağıdaki şematik gösterim, farklı ekipman tiplerinin Bejan sayısı spektrumundaki
konumlarını görselleştirir:

```
Be = 0                    0.25                   0.5                    0.75                   1.0
 |                         |                      |                      |                      |
 |  SÜRTÜNME BASKIN        |                      | DENGE                |   ISI TRANSFERİ BASKIN|
 |  (Friction Dominant)    |                      | (Balance)            |   (Heat Transfer Dom.)|
 |                         |                      |                      |                      |
 |  ├─ Pompalar ──────┤    |                      |                      |                      |
 |  ├─ Borular/Kanallar ──────┤                   |                      |                      |
 |       ├─ Kompresörler ─────────────┤            |                      |                      |
 |                         |    ├─ Plakalı HX ─────────────┤             |                      |
 |                         |          ├─ Buhar Türbinleri ────────┤      |                      |
 |                         |                      | ├─ Evaporatörler ─────────┤                  |
 |                         |                      |    ├─ Yoğuşturucular ─────────┤              |
 |                         |                      |       ├─ Borulu HX ───────────────┤          |
 |                         |                      |          ├─ Soğutma Kuleleri ─────────┤      |
 |                         |                      |          ├─ Kondenser (Chiller) ──────────┤   |
 |                         |                      |             ├─ Kurutucular ──────────────┤   |
 |                         |                      |                ├─ Kazanlar ─────────────────┤ |
 |                         |                      |                      |                      |
```

**Okuma rehberi:**
- Sola yakın ekipmanlar → sürtünme/mekanik kayıplar baskın → ΔP azaltma stratejileri
- Sağa yakın ekipmanlar → ısı transferi kayıpları baskın → ΔT azaltma stratejileri
- Ortadaki ekipmanlar → her iki kaynağı da analiz etmek gerekir

---

## 2. Entropi Üretim Sayısı (Entropy Generation Number — N_s)

### 2.1 Bejan'ın N_s Tanımı

#### Fiziksel Sezgi (Physical Intuition)

Entropi üretiminin mutlak değeri (Ṡ_gen [W/K]) farklı ölçeklerdeki sistemleri karşılaştırmak
için uygun değildir. 100 MW'lık bir santralde 5 kW/K entropi üretimi kabul edilebilirken,
10 kW'lık küçük bir sistemde aynı değer felaket anlamına gelir. Bu nedenle, entropi üretimini
**sistemin kapasitesine göre normalize eden** boyutsuz bir sayıya ihtiyaç vardır.

Entropi üretim sayısı (N_s), entropi üretim hızını sistemin karakteristik entropi transfer
hızına bölerek elde edilen boyutsuz bir parametredir. N_s ne kadar küçükse, sistem o kadar
tersinir (reversible) çalışmaktadır.

#### Genel Tanım

Bejan'ın orijinal tanımında, N_s aşağıdaki gibi ifade edilir:

```
N_s = Ṡ_gen / (Q̇ / T_min)
```

Burada:
- Ṡ_gen   : Toplam entropi üretim hızı [W/K]
- Q̇       : Sisteme veya sistemden transfer edilen ısı hızı [W]
- T_min    : Sistemdeki en düşük mutlak sıcaklık [K]
- Q̇/T_min : Karakteristik entropi transfer hızı [W/K]

Bu normalizasyon, entropi üretimini "mümkün olan maksimum entropi transferine" oranlayarak
anlamlı bir karşılaştırma sağlar.

**Tersinir limit:**

```
N_s = 0    →    İdeal (tersinir) süreç, hiç geri dönüşümsüzlük yok
N_s → ∞    →    Son derece verimsiz, büyük kayıplar
```

Pratikte N_s değeri 0 ile 1 arasında kalmayabilir; 1'den büyük değerler de mümkündür ve
sistemin son derece yüksek entropi ürettiğini gösterir.

---

### 2.2 N_s Alternatifleri

Farklı mühendislik uygulamaları için özelleştirilmiş N_s tanımları geliştirilmiştir. Her
birinin ayrı fiziksel sezgisi ve kullanım alanı vardır.

#### 2.2.1 Isı Değiştiriciler İçin N_s

**Fiziksel sezgi:** Bir ısı değiştiricinin "ne kadar iyi" çalıştığını, ürettiği entropiyi
minimum kapasite akımının (minimum capacity rate) taşıyabileceği entropi ile kıyaslayarak
anlayabiliriz. Bu normalizasyon, farklı boyuttaki ısı değiştiricileri adil biçimde
karşılaştırır.

```
N_s,HX = Ṡ_gen / (ṁ × c_p)_min
```

Burada:
- (ṁ × c_p)_min : Minimum kapasite hızı (minimum capacity rate) [W/K]
- İki akışkandan hangisinin kapasite hızı küçükse o kullanılır

**Tipik değerler:**
- N_s,HX < 0.01 : Mükemmel tasarım
- N_s,HX = 0.01 – 0.05 : İyi tasarım
- N_s,HX = 0.05 – 0.15 : Kabul edilebilir
- N_s,HX > 0.15 : İyileştirme gerekli

#### 2.2.2 Akışkan Akışı İçin N_s

**Fiziksel sezgi:** Bir boru hattında akışkan taşımanın termodinamik maliyetini, basınç
düşümünün yarattığı entropi üretimini debiye oranlayarak ölçeriz. Yüksek N_s, boru hattının
termodinamik açıdan "pahalı" olduğunu gösterir.

```
N_s,akış = Ṡ_gen,ΔP × T / (ṁ × ΔP / ρ)
```

veya daha yaygın kullanılan basitleştirilmiş form:

```
N_s,akış = (f × L / D) × (Re)^n / geometri_faktörü
```

Burada:
- f  : Darcy sürtünme faktörü (friction factor) [-]
- L  : Boru uzunluğu [m]
- D  : Boru çapı [m]
- Re : Reynolds sayısı [-]

#### 2.2.3 Güç Çevrimleri İçin N_s

**Fiziksel sezgi:** Bir güç çevriminin (power cycle) ideallikten ne kadar saptığını, entropi
üretimini çevrime giren ısının yüksek sıcaklık kaynağı ile oranını kıyaslayarak ölçeriz.
Bu, Carnot veriminden sapmayı doğrudan yansıtır.

```
N_s,çevrim = Ṡ_gen / (Q̇_H / T_H)
```

Burada:
- Q̇_H : Yüksek sıcaklık kaynağından alınan ısı [W]
- T_H  : Yüksek sıcaklık kaynağının mutlak sıcaklığı [K]

Bu tanımda N_s ile verim arasında doğrudan ilişki kurulabilir:

```
η_II = 1 − N_s,çevrim × (T_H / T_L − 1)⁻¹
```

Bu ifade, N_s arttıkça ikinci yasa veriminin (η_II) düştüğünü açıkça gösterir.

#### 2.2.4 Soğutma Sistemleri İçin N_s

**Fiziksel sezgi:** Soğutma sistemlerinde entropi üretimi, soğutma kapasitesine göre
normalize edilir. Bu, farklı kapasitedeki chiller'ları karşılaştırmayı sağlar.

```
N_s,soğutma = Ṡ_gen × T_0 / Q̇_evap
```

Burada:
- T_0     : Çevre (referans) sıcaklığı [K]
- Q̇_evap : Evaporatördeki soğutma kapasitesi [W]

---

### 2.3 N_s Benchmark Değerleri

Aşağıdaki tablo, farklı ekipman tipleri için N_s aralıklarını ve karşılık gelen performans
seviyelerini göstermektedir.

#### Isı Değiştiriciler (N_s,HX)

| Performans Seviyesi | N_s,HX Aralığı  | Yorum                                         |
|---------------------|------------------|-----------------------------------------------|
| Mükemmel            | < 0.01           | Yeni, iyi tasarlanmış, optimum koşullarda     |
| İyi                 | 0.01 – 0.05     | Standart endüstriyel uygulama                 |
| Ortalama            | 0.05 – 0.15     | Fouling veya kısmi yük etkisi olabilir        |
| Zayıf               | 0.15 – 0.30     | Ciddi fouling veya tasarım hatası             |
| Kritik              | > 0.30           | Acil müdahale gerekli                         |

#### Güç Çevrimleri (N_s,çevrim)

| Performans Seviyesi | N_s,çevrim Aralığı | Yorum                                       |
|---------------------|---------------------|---------------------------------------------|
| Mükemmel            | < 0.05              | Modern kombine çevrim santral seviyesi      |
| İyi                 | 0.05 – 0.15        | İyi tasarlanmış Rankine çevrimi             |
| Ortalama            | 0.15 – 0.30        | Eski veya bakımsız sistemler                |
| Zayıf               | > 0.30              | Büyük termodinamik kayıplar, yenileme gerekli|

#### Boru Hatları (N_s,akış)

| Performans Seviyesi | Gösterge                    | Yorum                                    |
|---------------------|-----------------------------|------------------------------------------|
| Mükemmel            | ΔP/P_giriş < 0.02          | Düzgün tasarlanmış, kısa hat             |
| İyi                 | ΔP/P_giriş = 0.02 – 0.05  | Standart endüstriyel boru hattı          |
| Ortalama            | ΔP/P_giriş = 0.05 – 0.10  | Uzun hat veya çok dirsek                 |
| Zayıf               | ΔP/P_giriş > 0.10          | Aşırı basınç kaybı, yeniden tasarım      |

#### Soğutma Sistemleri (N_s,soğutma)

| Performans Seviyesi | N_s,soğutma Aralığı | Yorum                                       |
|---------------------|----------------------|---------------------------------------------|
| Mükemmel            | < 0.10               | Yüksek COP, iyi eşleşmiş kapasite         |
| İyi                 | 0.10 – 0.25         | Standart ticari chiller performansı         |
| Ortalama            | 0.25 – 0.45         | Kısmi yük veya fouling etkisi               |
| Zayıf               | > 0.45               | Düşük COP, ciddi geri dönüşümsüzlük        |

---

## 3. Be ve N_s'nin Birlikte Kullanımı

### 3.1 İki Boyutlu Analiz (Two-Dimensional Analysis)

Tek başına N_s veya tek başına Be, bir sistemin termodinamik performansını tam olarak
tanımlayamaz. İkisini birlikte kullanmak gerekir:

- **N_s → BÜYÜKLÜK:** Toplam geri dönüşümsüzlüğün ne kadar olduğunu söyler. Yüksek N_s
  "çok entropi üretiliyor" demektir, düşük N_s "az entropi üretiliyor" demektir.

- **Be → DAĞILIM:** Geri dönüşümsüzlüğün nereden kaynaklandığını söyler. Yüksek Be
  "ısı transferi tarafında" demektir, düşük Be "sürtünme tarafında" demektir.

**Analoji:** Bir hastanın durumunu değerlendirmek gibidir:
- N_s = ateş derecesi (ne kadar hasta?)
- Be = semptom dağılımı (neden hasta? — baş ağrısı mı, karın ağrısı mı?)

Tedaviye karar vermek için her ikisini de bilmek gerekir.

#### İki Boyutlu Performans Uzayı

Bir sistemin performansı, N_s-Be düzleminde bir nokta olarak temsil edilebilir:

```
N_s (yüksek)
    │
    │   Bölge C:              Bölge D:
    │   Yüksek N_s,           Yüksek N_s,
    │   Düşük Be              Yüksek Be
    │   → Ciddi sürtünme      → Ciddi ısı transferi
    │     kayıpları             kayıpları
    │
    │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
    │
    │   Bölge A:              Bölge B:
    │   Düşük N_s,            Düşük N_s,
    │   Düşük Be              Yüksek Be
    │   → İyi, sürtünme       → İyi, ısı transferi
    │     hafif baskın          hafif baskın
    │
    └──────────────────────────────────── Be (yüksek)
         0                 0.5                 1.0
```

**Hedef:** Her sistemin Bölge A veya Bölge B'de (düşük N_s) olması istenir. Bölge C veya
Bölge D'deki sistemler öncelikli iyileştirme adaylarıdır.

---

### 3.2 Karar Matrisi (Decision Matrix)

Aşağıdaki karar matrisi, N_s ve Be değerlerine göre alınması gereken aksiyonları
sistematik olarak özetler:

| N_s Durumu      | Be Durumu        | Teşhis                             | Önerilen Aksiyon                                                |
|-----------------|------------------|-------------------------------------|-----------------------------------------------------------------|
| Düşük (< 0.05) | Düşük (< 0.3)   | İyi performans, sürtünme hafif      | İzlemeye devam, küçük ΔP optimizasyonları                       |
| Düşük (< 0.05) | Orta (0.3–0.7)  | İyi performans, dengeli             | Mevcut durumu koru, periyodik kontrol                           |
| Düşük (< 0.05) | Yüksek (> 0.7)  | İyi performans, ΔT hafif baskın     | İzlemeye devam, fouling takibi                                  |
| Orta (0.05–0.15)| Düşük (< 0.3)  | Orta performans, sürtünme baskın    | Boru çapı gözden geçir, vana/dirsek azalt, pompa optimize et   |
| Orta (0.05–0.15)| Orta (0.3–0.7) | Orta performans, her iki kaynak     | Hem ΔT hem ΔP analizleri yap, maliyet-fayda değerlendir        |
| Orta (0.05–0.15)| Yüksek (> 0.7) | Orta performans, ısı transferi baskın| Isı transfer alanı artır, fouling temizle, ΔT düşür           |
| Yüksek (> 0.15)| Düşük (< 0.3)  | Kötü performans, ciddi sürtünme     | **Acil:** Boru hattı yeniden tasarla, bypass düşün, debi azalt |
| Yüksek (> 0.15)| Orta (0.3–0.7) | Kötü performans, yaygın sorunlar    | **Acil:** Kapsamlı denetim, her iki kaynağı birlikte ele al    |
| Yüksek (> 0.15)| Yüksek (> 0.7) | Kötü performans, ciddi ΔT sorunu    | **Acil:** Isı değiştirici yenile, kademe ekle, geri kazanım    |

---

### 3.3 Uygulama Örneği (Worked Example)

**Senaryo:** Bir gıda fabrikasında kazan ön ısıtıcısı olarak kullanılan borulu ısı
değiştirici (shell & tube heat exchanger) incelenmektedir.

**Veriler:**
- Sıcak akışkan (baca gazı): ṁ_h = 2.5 kg/s, c_p,h = 1.05 kJ/(kg·K), T_h,giriş = 350°C,
  T_h,çıkış = 180°C
- Soğuk akışkan (besleme suyu): ṁ_c = 3.0 kg/s, c_p,c = 4.18 kJ/(kg·K), T_c,giriş = 60°C,
  T_c,çıkış = 95°C
- Sıcak taraf basınç düşümü: ΔP_h = 8 kPa, ρ_h = 0.85 kg/m³
- Soğuk taraf basınç düşümü: ΔP_c = 15 kPa, ρ_c = 985 kg/m³

**Adım 1 — Isı transfer hızının doğrulanması:**

```
Q̇ = ṁ_h × c_p,h × (T_h,giriş − T_h,çıkış)
Q̇ = 2.5 × 1.05 × (350 − 180) = 446.25 kW
```

Soğuk taraf kontrolü:

```
Q̇_c = ṁ_c × c_p,c × (T_c,çıkış − T_c,giriş)
Q̇_c = 3.0 × 4.18 × (95 − 60) = 438.9 kW
```

Fark ≈ %1.7 — ısı kaybı olarak kabul edilebilir.

**Adım 2 — Entropi üretimi bileşenleri:**

Isı transferi kaynaklı (her iki akışkan için ayrı hesaplanır):

```
Ṡ_gen,ΔT,sıcak = ṁ_h × c_p,h × ln(T_h,çıkış / T_h,giriş)
                = 2.5 × 1.05 × ln(453.15 / 623.15)
                = 2.625 × (−0.3185)
                = −0.836 kW/K

Ṡ_gen,ΔT,soğuk = ṁ_c × c_p,c × ln(T_c,çıkış / T_c,giriş)
                = 3.0 × 4.18 × ln(368.15 / 333.15)
                = 12.54 × 0.1001
                = 1.255 kW/K
```

Toplam ısı transferi kaynaklı entropi üretimi:

```
Ṡ_gen,ΔT = Ṡ_gen,ΔT,sıcak + Ṡ_gen,ΔT,soğuk
          = −0.836 + 1.255
          = 0.419 kW/K
```

**Adım 3 — Sürtünme kaynaklı entropi üretimi:**

```
Ṡ_gen,ΔP,sıcak = ṁ_h × ΔP_h / (ρ_h × T_h,ort)
T_h,ort = (623.15 + 453.15) / 2 = 538.15 K
Ṡ_gen,ΔP,sıcak = 2.5 × 8000 / (0.85 × 538.15)
               = 20000 / 457.4
               = 0.0437 kW/K

Ṡ_gen,ΔP,soğuk = ṁ_c × ΔP_c / (ρ_c × T_c,ort)
T_c,ort = (333.15 + 368.15) / 2 = 350.65 K
Ṡ_gen,ΔP,soğuk = 3.0 × 15000 / (985 × 350.65)
               = 45000 / 345390
               = 0.000130 kW/K
```

Toplam sürtünme kaynaklı entropi üretimi:

```
Ṡ_gen,ΔP = 0.0437 + 0.000130 = 0.0438 kW/K
```

> **Not:** Soğuk taraftaki basınç düşümü kaynaklı entropi üretimi, sıvının yüksek
> yoğunluğu (ρ_c = 985 kg/m³) nedeniyle çok küçüktür. Gaz tarafı baskındır.

**Adım 4 — Bejan sayısı hesabı:**

```
Be = Ṡ_gen,ΔT / (Ṡ_gen,ΔT + Ṡ_gen,ΔP)
Be = 0.419 / (0.419 + 0.0438)
Be = 0.419 / 0.4628
Be = 0.905
```

**Adım 5 — Entropi üretim sayısı (N_s):**

```
(ṁ × c_p)_min = min(2.5 × 1.05, 3.0 × 4.18)
              = min(2.625, 12.54)
              = 2.625 kW/K

Ṡ_gen,toplam = 0.419 + 0.0438 = 0.4628 kW/K

N_s = Ṡ_gen,toplam / (ṁ × c_p)_min
N_s = 0.4628 / 2.625
N_s = 0.176
```

**Adım 6 — Yorumlama:**

| Parametre | Değer | Yorum                                                        |
|-----------|-------|--------------------------------------------------------------|
| Be        | 0.905 | Çok yüksek — ısı transferi kaynaklı entropi üretimi baskın  |
| N_s       | 0.176 | Yüksek — toplam geri dönüşümsüzlük önemli düzeyde           |

**Karar matrisi sonucu:** Yüksek N_s + Yüksek Be → **Acil iyileştirme gerekli, odak noktası
ısı transferi tarafı.**

**Öneriler (öncelik sırasına göre):**
1. Isı transfer alanını artırmak (ek boru demetleri veya daha uzun borular)
2. Karşı akış (counterflow) düzenine geçiş değerlendirmesi
3. Baca gazı tarafında kanatçıklı borular (finned tubes) kullanımı
4. Yaklaşma sıcaklık farkının (approach temperature difference) düşürülmesi
5. Fouling kontrolü — baca gazı tarafında kurum birikimi özellikle artırıcı etki yapar

---

## 4. İleri Konular (Advanced Topics)

### 4.1 Modifiye Bejan Sayıları

#### 4.1.1 Çok Akışlı Sistemler İçin Be (Multi-Stream Systems)

**Fiziksel sezgi:** Gerçek endüstriyel sistemlerde genellikle ikiden fazla akışkan aynı
ısı değiştirici ağında yer alır. Bu durumda, her akışkan çifti arasındaki ısı transferi
kaynaklı entropi üretimi ayrı ayrı hesaplanmalı ve toplanmalıdır.

```
Be_çok-akış = Σᵢⱼ Ṡ_gen,ΔT,ij / (Σᵢⱼ Ṡ_gen,ΔT,ij + Σₖ Ṡ_gen,ΔP,k)
```

Burada:
- i, j : Isı transferi yapan akışkan çiftleri
- k    : Tüm akışkan hatları (basınç düşümü bileşeni)

Bu genelleştirilmiş tanım, pinch analizi (pinch analysis) uygulamalarında ısı değiştirici
ağlarının (HEN — Heat Exchanger Network) entropik performansını değerlendirmek için
kullanılır.

#### 4.1.2 Kimyasal Süreçler İçin Genişletilmiş Be

**Fiziksel sezgi:** Reaktörlerde ve karıştırma süreçlerinde entropi üretiminin üçüncü bir
bileşeni daha vardır: kimyasal reaksiyonlar ve karışım (chemical reaction and mixing). Bu
bileşeni de dahil eden genişletilmiş Bejan sayısı:

```
Be_kimyasal = Ṡ_gen,ΔT / (Ṡ_gen,ΔT + Ṡ_gen,ΔP + Ṡ_gen,kimyasal)
```

Kimyasal entropi üretimi:

```
Ṡ_gen,kimyasal = −Σᵢ (μᵢ / T) × (dNᵢ/dt)    [W/K]
```

Burada:
- μᵢ     : i bileşeninin kimyasal potansiyeli [J/mol]
- dNᵢ/dt : i bileşeninin mol sayısındaki değişim hızı [mol/s]

Bu tanımda Be < 0.33 olması sürtünme baskın, Be ≈ 0.33 tüm kaynaklar eşit, Be > 0.67 ise
ısı transferi baskın anlamına gelir. Ancak üç bileşenin her birinin payını ayrı ayrı
raporlamak daha bilgilendiricidir.

---

### 4.2 Zamana Bağlı Be Analizi (Time-Dependent Be Analysis)

#### 4.2.1 Yük Değişimi Etkisi (Load Variation Effect)

**Fiziksel sezgi:** Endüstriyel ekipmanlar nadiren tam yükte çalışır. Kısmi yük (part-load)
koşullarında akış hızları, sıcaklık farkları ve basınç düşümleri değişir. Bu değişimler
Be sayısını doğrudan etkiler.

Genel eğilim:
- Yük azaldıkça debi düşer → ΔP azalır → Ṡ_gen,ΔP azalır
- Yük azaldıkça ΔT genellikle artar (özellikle ısı değiştiricilerde) → Ṡ_gen,ΔT artar
- Sonuç: **Kısmi yükte Be artma eğilimindedir** (ısı transferi daha da baskın hale gelir)

```
Be(yük) = f(ṁ(yük), ΔT(yük), ΔP(yük))
```

**Pratik kullanım:** Yıl boyunca Be değerlerini izlemek, mevsimsel ve yük bazlı
optimizasyon fırsatlarını ortaya çıkarır.

#### 4.2.2 Fouling Etkisi (Fouling Effect)

Kirlenme (fouling) zamanla ısı transfer direncini artırır:

- Fouling → ısı transfer katsayısı (U) düşer → ΔT artar → Ṡ_gen,ΔT artar
- Fouling → geçiş alanı daralır → ΔP artar → Ṡ_gen,ΔP artar

Ancak ΔT etkisi genellikle daha baskındır, bu nedenle:

```
Fouling arttıkça → Be hafif artar (tipik olarak 0.02–0.08 puan artış)
```

Be değerindeki sistematik artış, fouling'in başladığının erken göstergesi olarak
kullanılabilir.

#### 4.2.3 Mevsimsel Değişimler (Seasonal Variations)

Soğutma kulelerive hava kaynaklı kondenserlerde dış hava sıcaklığı Be'yi etkiler:

- **Yaz ayları:** T_dış yüksek → ΔT küçülür → Ṡ_gen,ΔT azalır → Be düşer
- **Kış ayları:** T_dış düşük → ΔT büyür → Ṡ_gen,ΔT artar → Be yükselir

Bu mevsimsel eğilim, soğutma sistemlerinin yıllık optimizasyon planlamasında dikkate
alınmalıdır.

---

## 5. Pratik Mühendislik Kuralları (Rules of Thumb)

### 5.1 Enerji Denetimlerinde Hızlı Be Tahmini

Sahada detaylı hesaplama yapılmadan önce, aşağıdaki kısa yol kuralları Be hakkında ön fikir
verir:

1. **Sıcaklık farkı kuralı:** Eğer sıcak ve soğuk akışkan arasındaki ortalama ΔT > 50°C
   ise, büyük olasılıkla Be > 0.6'dır. ΔT > 100°C ise Be > 0.8 beklenebilir.

2. **Basınç düşümü kuralı:** Eğer toplam basınç düşümü giriş basıncının %5'inden fazla
   ise ve ΔT < 20°C ise, büyük olasılıkla Be < 0.4'tür.

3. **Gaz vs sıvı kuralı:** Gaz tarafının basınç düşümü kaynaklı entropi üretimi, sıvı
   tarafına kıyasla 100–1000 kat daha büyük olabilir (düşük yoğunluk nedeniyle). Bu nedenle
   gaz-sıvı ısı değiştiricilerinde sürtünme bileşeni daha önemlidir.

4. **Reynolds sayısı kuralı:** Re > 10⁵ olan türbülanslı akışlarda sürtünme kayıpları
   hızla artar; Be düşer. Re < 2300 olan laminer akışlarda sürtünme nispeten düşüktür;
   Be yükselir.

5. **Ekipman yaşı kuralı:** 10 yıldan eski ekipmanlarda fouling etkisi ile Be tipik olarak
   yeni duruma göre 0.03–0.10 puan daha yüksektir.

### 5.2 Hızlı N_s Kontrol Listesi

Bir endüstriyel sistemin N_s performansını hızla değerlendirmek için:

| Kontrol Sorusu                                         | Evet → N_s Yükselir | Hayır → N_s Düşük |
|--------------------------------------------------------|----------------------|--------------------|
| Ortalama ΔT > 100°C mi?                               | Evet → +0.05–0.15   | —                  |
| Toplam ΔP/P_giriş > %5 mi?                            | Evet → +0.02–0.05   | —                  |
| Ekipman kısmi yükte (< %50) mi?                       | Evet → +0.03–0.08   | —                  |
| Son temizlik/bakım > 12 ay önce mi?                   | Evet → +0.02–0.06   | —                  |
| Tasarım 15 yıldan eski mi?                             | Evet → +0.03–0.10   | —                  |

> **Uyarı:** Bu değerler kaba tahmindir. Kesin sonuçlar için Ṡ_gen bileşenlerinin ayrıntılı
> hesaplanması gerekir.

### 5.3 Fabrika Düzeyinde Kullanım

Fabrika genelinde birden fazla ekipman analiz edildiğinde:

1. **Önce N_s ile sırala:** En yüksek N_s değerine sahip ekipmanlar en çok entropi üreten
   (en verimsiz) birimlerdir. Bunları öncelikli iyileştirme adayı olarak belirle.

2. **Sonra Be ile yönlendir:** Yüksek N_s'li ekipmanların Be değerine bakarak iyileştirme
   stratejisini belirle (ΔT mi yoksa ΔP mi azaltılacak).

3. **Çapraz entegrasyon fırsatları:** Be > 0.7 olan ekipmanlardan çıkan atık ısı, Be < 0.3
   olan ekipmanların ön ısıtmasında kullanılabilir. Bu tür çapraz entegrasyon (cross-equipment
   integration), fabrika genelinde N_s'yi düşürür.

4. **İzleme paneli:** Tüm ekipmanlar için Be ve N_s değerlerini aylık bazda izleyen bir
   dashboard oluştur. Trend sapmaları bakım ihtiyacını erken tespit ettirir.

---

## İlgili Dosyalar

- `factory/entropy_generation/fundamentals.md` — Entropi üretimi temel kavramları ve yasaları
- `factory/entropy_generation/heat_transfer_egm.md` — Isı transferi kaynaklı entropi üretimi minimizasyonu (EGM)
- `factory/entropy_generation/fluid_flow_egm.md` — Akışkan akışı kaynaklı entropi üretimi minimizasyonu
- `factory/cross_equipment.md` — Ekipmanlar arası entegrasyon fırsatları
- `factory/prioritization.md` — Fabrika düzeyinde iyileştirme önceliklendirmesi
- `factory/factory_benchmarks.md` — Sektörel entropi ve exergy benchmark değerleri
- `factory/pinch_analysis.md` — Pinch analizi ve ısı değiştirici ağ optimizasyonu
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanımı stratejileri

---

## Referanslar

1. Bejan, A. (1982). *Entropy Generation through Heat and Fluid Flow*. Wiley, New York.
2. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press, Boca Raton.
3. Bejan, A. (2013). *Convection Heat Transfer*, 4th Edition. Wiley.
4. Hesselgreaves, J.E. (2001). *Compact Heat Exchangers: Selection, Design and Operation*. Pergamon.
5. Ratts, E.B. & Raut, A.G. (2004). "Entropy generation minimization of fully developed internal flow with constant heat flux." *Journal of Heat Transfer*, 126(4), 656–659.
6. Zimparov, V. (2001). "Extended performance evaluation criteria for enhanced heat transfer surfaces: heat transfer through a wall." *International Journal of Heat and Mass Transfer*, 44(1), 169–180.
7. Şara, O.N., Yapıcı, S., Çomaklı, Ö. (2001). "Second law analysis of rectangular channels with square pin-fins." *International Communications in Heat and Mass Transfer*, 28(5), 617–630.
8. Yılmaz, M., Sara, O.N., Karsli, S. (2001). "Performance evaluation criteria for heat exchangers based on second law analysis." *Exergy, An International Journal*, 1(4), 278–294.
9. TS EN ISO 50001:2018 — Enerji Yönetim Sistemleri standardı
10. ASHRAE Handbook — Fundamentals (2021), Chapter 4: Heat Transfer.
