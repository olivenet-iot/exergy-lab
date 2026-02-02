---
title: "Exergoekonomik Maliyet Denge Denklemleri (Exergoeconomic Cost Balance)"
category: factory
equipment_type: factory
keywords: [exergoekonomik denge, maliyet dengesi, cost balance, SPECO, akış maliyeti, Ċ_P, Ċ_F, Ż, birim exergy maliyeti]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/fuel_product_definitions.md
  - factory/exergoeconomic/auxiliary_equations.md
  - factory/exergoeconomic/matrix_formulation.md
  - factory/exergoeconomic/evaluation_criteria.md
use_when:
  - "Exergoekonomik maliyet denge denklemleri kurulurken"
  - "Bileşen bazlı maliyet dengesi yazılırken"
  - "Sistem genelinde maliyet denklem sistemi oluşturulurken"
  - "Sayısal örnek ile maliyet dengesi çözülürken"
  - "Rankine çevrimi exergoekonomik analiz yapılırken"
priority: high
last_updated: 2026-02-01
---
# Exergoekonomik Maliyet Denge Denklemleri (Exergoeconomic Cost Balance)

> Son güncelleme: 2026-02-01

## 1. Giriş ve Temel Kavram

Exergoekonomik maliyet dengesi (exergoeconomic cost balance), bir termal sistemdeki her bileşenin giriş ve
çıkış akışlarına parasal değer atanmasını sağlayan temel denklemdir. Bu denklem, termodinamiğin ikinci yasası
ile maliyet muhasebesini birleştirerek, exergy akışlarının birim maliyetlerinin sistematik olarak
hesaplanmasına olanak tanır.

### 1.1 Temel Prensip

Her bileşende çıkış maliyet akışları, giriş maliyet akışları ve bileşenin kendi yatırım maliyetinin
toplamına eşittir:

```
Ċ_P,k = Ċ_F,k + Ż_k

Burada:
- Ċ_P,k = k. bileşenin ürün (product) maliyet akışı [€/saat]
- Ċ_F,k = k. bileşenin yakıt (fuel) maliyet akışı [€/saat]
- Ż_k   = k. bileşenin seviyelendirilmiş yatırım + işletme-bakım maliyet akışı [€/saat]
```

### 1.2 Fiziksel Anlam

Bu denklem şunu söyler: Bir bileşenin ürettiği ürünün maliyeti, o ürünü üretmek için harcanan yakıt
maliyeti ile bileşenin kendisinin maliyetinin toplamından oluşur. Başka bir deyişle, exergoekonomik
analizde maliyet artışının iki kaynağı vardır:

1. **Yakıt maliyeti (Ċ_F,k):** Bileşene giren exergy akışlarının taşıdığı maliyet
2. **Bileşen maliyeti (Ż_k):** Ekipmanın yatırım ve işletme-bakım maliyetinin saatlik payı

### 1.3 Enerji Dengesi ile Analoji

```
Enerji dengesi:      Σ Ė_çıkış = Σ Ė_giriş - Ė_D
Maliyet dengesi:     Σ Ċ_çıkış = Σ Ċ_giriş + Ż_k

Önemli fark:
- Enerji (ve exergy) bileşende AZALIR (yıkım/kayıp)
- Maliyet bileşende ARTAR (yatırım ve işletme giderleri eklenir)
```

## 2. Akış Bazlı Maliyet Denge Denklemi (Stream-Level Formulation)

### 2.1 Genel Formülasyon

Temel maliyet dengesi, akış (stream) bazında şu şekilde yazılır:

```
Σ (c_j · Ė_j)_çıkış + c_Ẇ · Ẇ_k = Σ (c_j · Ė_j)_giriş + c_Q · Ė_Q,k + Ż_k

Burada:
- c_j   = j. akışın birim exergy maliyeti [€/kJ veya €/GJ]
- Ė_j   = j. akışın exergy hızı [kW]
- Ẇ_k   = k. bileşenin iş (power) akışı [kW] (pozitif: üretim; negatif: tüketim)
- Ė_Q,k = k. bileşenin ısı transfer exergy'si [kW]
- Ż_k   = k. bileşenin seviyelendirilmiş maliyet akışı [€/saat]
```

### 2.2 Maliyet Akışı Tanımı

Her akışın maliyet akışı, birim exergy maliyeti ile exergy hızının çarpımıdır:

```
Ċ_j = c_j · Ė_j  [€/saat]

Burada:
- Ċ_j = j. akışın maliyet akışı [€/saat]
- c_j  = j. akışın birim exergy maliyeti [€/kJ]
- Ė_j  = j. akışın exergy hızı [kW = kJ/s]

Birim dönüşüm:
  Ċ [€/saat] = c [€/kJ] × Ė [kW] × 3.6 [kJ·saat⁻¹/kW⁻¹·s]

veya doğrudan:
  Ċ [€/s] = c [€/kJ] × Ė [kW]
  Ċ [€/saat] = Ċ [€/s] × 3600
```

### 2.3 İş ve Isı Akışlarının Maliyeti

İş (power) ve ısı transferi akışları da birer maliyet akışına sahiptir:

```
İş maliyet akışı:
  Ċ_Ẇ = c_Ẇ · |Ẇ|  [€/saat]

Isı transferi maliyet akışı:
  Ċ_Q = c_Q · Ė_Q  [€/saat]

Isı transfer exergy'si:
  Ė_Q = Q̇ · (1 - T₀/T_b)  [kW]

Burada:
- T_b = Sınır (boundary) sıcaklığı [K]
- T₀  = Referans ortam sıcaklığı [K]
- Q̇   = Isı transfer hızı [kW]
```

### 2.4 Ż Bileşenleri

Seviyelendirilmiş maliyet akışı iki bileşenden oluşur:

```
Ż_k = Ż_CI,k + Ż_OM,k

Burada:
- Ż_CI,k = Sermaye yatırımı (Capital Investment) bileşeni [€/saat]
- Ż_OM,k = İşletme ve bakım (Operating & Maintenance) bileşeni [€/saat]

Hesaplama:
  Ż_CI,k = (CRF × TCI_k) / τ
  Ż_OM,k = (γ_k × PEC_k) / τ

Burada:
- CRF = Sermaye geri kazanım faktörü [-]
- TCI_k = Toplam yatırım maliyeti [€]
- PEC_k = Satın alma maliyeti [€]
- τ = Yıllık çalışma saati [saat/yıl]
- γ_k = Yıllık bakım oranı [-]
```

> **Detaylı Ż hesabı:** `levelized_cost.md` dosyasına bakınız.

## 3. Bileşen Bazlı Maliyet Denge Denklemleri

Bu bölümde, SPECO metoduna uygun olarak her ekipman tipi için maliyet denge denklemi, yakıt/ürün tanımı
ve gerekli yardımcı denklemler sunulmaktadır.

### 3.1 Kompresör (Compressor)

```
Şema:
                 ┌───────────────┐
  Ẇ_C ────────→ │               │
                 │  KOMPRESÖR    │ ────→  Ė_2 (yüksek basınçlı gaz)
  Ė_1 ────────→ │               │
                 └───────────────┘

Maliyet dengesi:
  c_2 · Ė_2 = c_1 · Ė_1 + c_Ẇ · Ẇ_C + Ż_C

Yakıt-Ürün tanımı:
  Yakıt:  Ė_F = Ẇ_C
  Ürün:   Ė_P = Ė_2 - Ė_1

Yardımcı denklem: Yok
  → Bilinmeyen: c_2 (c_1 ve c_Ẇ genellikle bilinen veya dış kaynak)
  → 1 denklem, 1 bilinmeyen → Çözülebilir

Birim ürün maliyeti:
  c_P = (c_1 · Ė_1 + c_Ẇ · Ẇ_C + Ż_C) / Ė_2
  veya
  c_P = (Ċ_F + Ż_C) / Ė_P = (c_Ẇ · Ẇ_C + Ż_C) / (Ė_2 - Ė_1)
  (c_1 = 0 ise, ortam havası girişi)
```

### 3.2 Türbin (Turbine)

```
Şema:
                 ┌───────────────┐
  Ė_1 ────────→ │               │ ────→  Ẇ_T (iş çıkışı)
                 │    TÜRBİN     │
                 │               │ ────→  Ė_2 (düşük basınçlı akışkan)
                 └───────────────┘

Maliyet dengesi:
  c_Ẇ · Ẇ_T + c_2 · Ė_2 = c_1 · Ė_1 + Ż_T

Yakıt-Ürün tanımı:
  Yakıt:  Ė_F = Ė_1 - Ė_2
  Ürün:   Ė_P = Ẇ_T

Yardımcı denklem (F-kuralı):
  c_1 = c_2
  → Yakıt, giriş ile çıkış arasındaki exergy farkından oluşur
  → SPECO F-kuralı: Fark oluşturan akışların birim maliyeti eşittir

Bilinmeyenler: c_Ẇ, c_2 (c_1 biliniyorsa → 2 bilinmeyen, 2 denklem)

Birim ürün maliyeti:
  c_P = c_Ẇ = (c_1 · (Ė_1 - Ė_2) + Ż_T) / Ẇ_T
```

### 3.3 Kazan (Boiler / Steam Generator)

```
Şema:
                 ┌───────────────┐
  Ė_yakıt ────→ │               │ ────→  Ė_buhar (kızgın buhar çıkışı)
  Ė_hava  ────→ │     KAZAN     │
  Ė_su    ────→ │               │ ────→  Ė_baca (baca gazı)
                 └───────────────┘

Maliyet dengesi (tam):
  c_buhar · Ė_buhar + c_baca · Ė_baca = c_yakıt · Ė_yakıt + c_hava · Ė_hava + c_su · Ė_su + Ż_B

Basitleştirilmiş (c_hava ≈ 0, baca gazı atık → Ċ_baca = 0):
  c_buhar · Ė_buhar = c_yakıt · Ė_yakıt + c_su · Ė_su + Ż_B

Yakıt-Ürün tanımı:
  Yakıt:  Ė_F = Ė_yakıt (kimyasal exergy)
  Ürün:   Ė_P = Ė_buhar - Ė_su

Yardımcı denklem:
  Baca gazı atık ise: Ċ_baca = 0 (birim maliyet sıfır değil, maliyet akışı sıfır)
  Baca gazı geri kazanılıyorsa (F-kuralı): c_baca = c_yakıt

Birim ürün maliyeti:
  c_P = (c_yakıt · Ė_yakıt + c_su · Ė_su + Ż_B) / Ė_buhar
  veya F/P bazında:
  c_P = (Ċ_F + Ż_B) / Ė_P
```

### 3.4 Isı Değiştirici (Heat Exchanger — HX)

```
Şema:
                 ┌───────────────┐
  Ė_h1 ────────→│               │────→  Ė_h2 (sıcak çıkış)
  (sıcak giriş) │  ISI DEĞİŞT.  │
  Ė_c1 ────────→│               │────→  Ė_c2 (soğuk çıkış)
  (soğuk giriş) └───────────────┘

Maliyet dengesi:
  c_h2 · Ė_h2 + c_c2 · Ė_c2 = c_h1 · Ė_h1 + c_c1 · Ė_c1 + Ż_HX

Yakıt-Ürün tanımı:
  Yakıt:  Ė_F = Ė_h1 - Ė_h2 (sıcak taraf exergy azalışı)
  Ürün:   Ė_P = Ė_c2 - Ė_c1 (soğuk taraf exergy artışı)

Yardımcı denklem (F-kuralı):
  c_h1 = c_h2
  → Sıcak taraf yakıt olarak harcanır; giriş ve çıkış birim maliyeti eşit

Bilinmeyenler: c_h2, c_c2 (c_h1 ve c_c1 biliniyorsa)
Denklemler: 1 maliyet dengesi + 1 F-kuralı = 2 → Çözülebilir

Birim ürün maliyeti:
  c_P = c_c2 = [c_h1·(Ė_h1 - Ė_h2) + c_c1·Ė_c1 + Ż_HX] / Ė_c2
```

### 3.5 Pompa (Pump)

```
Şema:
                 ┌───────────────┐
  Ẇ_P ────────→ │               │
                 │     POMPA     │ ────→  Ė_2 (yüksek basınçlı sıvı)
  Ė_1 ────────→ │               │
                 └───────────────┘

Maliyet dengesi:
  c_2 · Ė_2 = c_1 · Ė_1 + c_Ẇ · Ẇ_P + Ż_P

Yakıt-Ürün tanımı:
  Yakıt:  Ė_F = Ẇ_P
  Ürün:   Ė_P = Ė_2 - Ė_1

Yardımcı denklem: Yok
  → Yapısal olarak kompresör ile aynıdır (sıvı bazlı)

Birim ürün maliyeti:
  c_P = (c_1 · Ė_1 + c_Ẇ · Ẇ_P + Ż_P) / Ė_2
```

### 3.6 Chiller (Soğutma Makinesi)

```
Şema:
                 ┌───────────────┐
  Ẇ_ch ────────→│               │
                 │    CHİLLER    │ ────→  Ė_soğuk,çıkış (soğutulmuş akışkan)
  Ė_soğuk,giriş→│               │
                 │               │ ────→  Ė_kond (kondenser atık ısı)
                 └───────────────┘

Maliyet dengesi:
  c_sç · Ė_sç + c_kond · Ė_kond = c_Ẇ · Ẇ_ch + c_sg · Ė_sg + Ż_ch

Yakıt-Ürün tanımı:
  Yakıt:  Ė_F = Ẇ_ch
  Ürün:   Ė_P = Ė_soğuk,çıkış - Ė_soğuk,giriş  (T < T₀ ise exergy artar)

DİKKAT — Chiller'da exergy yönü:
  T_soğuk < T₀ olduğunda, sıcaklık referans ortamdan uzaklaştıkça exergy ARTAR.
  Bu nedenle Ė_soğuk,çıkış > Ė_soğuk,giriş olur.

Yardımcı denklem:
  Kondenser atığı → Ċ_kond = 0 (atık ısı maliyetsiz)

Birim ürün maliyeti:
  c_P = (c_Ẇ · Ẇ_ch + c_sg · Ė_sg + Ż_ch) / Ė_sç
```

### 3.7 Kondenser (Condenser)

```
Şema:
                 ┌───────────────┐
  Ė_1 ────────→ │               │ ────→  Ė_2 (yoğuşmuş sıvı)
  (buhar giriş)  │   KONDENSER   │
  Ė_cw1 ───────→│               │ ────→  Ė_cw2 (soğutma suyu çıkış)
  (soğ. suyu in) └───────────────┘

Kondenser DİSSİPATİF bir bileşendir — doğrudan bir ürün tanımlanamaz.

Maliyet dengesi:
  c_2 · Ė_2 + c_cw2 · Ė_cw2 = c_1 · Ė_1 + c_cw1 · Ė_cw1 + Ż_K

SPECO ele alış yöntemleri:

Yöntem A — Başka bileşene dahil etme:
  Kondenseri kazana veya türbine dahil et
  → Ayrı denklem yazmaya gerek yok
  → Ė_D,kond ilgili bileşenin Ė_D'sine eklenir
  → Ż_kond ilgili bileşenin Ż'sine eklenir

Yöntem B — Exergy yıkımını dağıtma:
  Ė_D,kond'u orantılı olarak diğer bileşenlere paylaştır
  → Ė_D,k_yeni = Ė_D,k + Ė_D,kond × (Ė_D,k / Σ Ė_D)

Yöntem C — Bağımsız bileşen olarak tutma:
  Maliyet dengesi yazılır:
    c_2 · Ė_2 = c_1 · Ė_1 + Ż_K
    (Soğutma suyu c_cw1 = 0 ve atık ısı Ċ_cw2 = 0)

  Yardımcı denklem:
    c_1 = c_2 (birim maliyet korunur, F-kuralı)
    veya
    Ċ_atık = 0 (atık ısının maliyet akışı sıfır)
```

### 3.8 Karıştırıcı (Mixer)

```
Şema:
  Ė_1 ────→ ┌─────────────┐
             │  KARIŞTIRICI │ ────→  Ė_3
  Ė_2 ────→ └─────────────┘

Maliyet dengesi:
  c_3 · Ė_3 = c_1 · Ė_1 + c_2 · Ė_2 + Ż_mixer

Not: Ż_mixer genellikle ihmal edilebilir düzeydedir (basit bağlantı noktası).

Yardımcı denklem: Yok (tek çıkış)
  → c_1 ve c_2 biliniyorsa, c_3 doğrudan hesaplanır

Exergy yıkımı:
  Ė_D = Ė_1 + Ė_2 - Ė_3 ≥ 0
  (Farklı sıcaklık/basınçtaki akışların karışması tersinmezlik üretir)

Birim çıkış maliyeti:
  c_3 = (c_1 · Ė_1 + c_2 · Ė_2) / Ė_3
  → Ağırlıklı ortalama maliyet
```

### 3.9 Ayırıcı (Splitter / Divider)

```
Şema:
                 ┌─────────────┐ ────→  Ė_2
  Ė_1 ────────→ │   AYIRICI   │
                 └─────────────┘ ────→  Ė_3

Maliyet dengesi:
  c_2 · Ė_2 + c_3 · Ė_3 = c_1 · Ė_1 + Ż_splitter

Not: Ż_splitter ≈ 0 (genellikle ihmal edilir).

Yardımcı denklem (P-kuralı):
  c_2 = c_3
  → Ayırıcının iki çıkışı da aynı birim maliyete sahiptir
  → Fiziksel olarak aynı akışkanın bölünmesidir

İdeal ayırma: c_2 = c_3 = c_1 (exergy yıkımı yok)
Gerçek ayırma: c_2 = c_3 ≥ c_1 (küçük basınç kayıpları)

Genel kural (n çıkışlı ayırıcı):
  P-kuralı ile n-1 yardımcı denklem:
  c_2 = c_3 = c_4 = ... = c_n
```

### 3.10 Kısma Valfi (Throttling Valve / Expansion Valve)

```
Şema:
                 ┌─────────────┐
  Ė_1 ────────→ │    VALF     │ ────→  Ė_2
                 └─────────────┘

Kısma valfi DİSSİPATİF bir bileşendir.
İzoentalpik süreç: h_1 = h_2, ancak s_2 > s_1 → Ė_2 < Ė_1

Maliyet dengesi:
  c_2 · Ė_2 = c_1 · Ė_1 + Ż_valf

Not: Ż_valf genellikle çok küçüktür veya ihmal edilir.

SPECO yaklaşımları:
  Yöntem 1 — Birim maliyet korunumu:
    c_1 = c_2 (yardımcı denklem olarak)
    → c_2 · Ė_2 ≠ c_1 · Ė_1 → Fark, Ż_valf ile dengelenir
    → Pratikte: Ċ_kayıp = c_1 · (Ė_1 - Ė_2) → Ż_valf'e yüklenir veya ihmal edilir

  Yöntem 2 — Maliyet akışı korunumu (Ż_valf = 0):
    c_2 · Ė_2 = c_1 · Ė_1
    → c_2 = c_1 · (Ė_1 / Ė_2) > c_1
    → Birim maliyet artar (exergy azaldığı için)

  Yöntem 3 — Komşu bileşene dahil etme:
    Valf, hizmet ettiği bileşenle birleştirilir
    → Ayrı denklem yazılmaz

Exergy yıkımı:
  Ė_D = Ė_1 - Ė_2  [kW]
```

## 4. Sistem Genelinde Maliyet Denge Denklemleri

### 4.1 Denklem Sistemi Oluşturma

Bir termal sistemin tüm bileşenleri için maliyet denge denklemleri birlikte yazıldığında,
bilinmeyen birim exergy maliyetlerinin (c değerleri) hesaplanabileceği doğrusal bir denklem sistemi elde edilir.

```
Sistematik yaklaşım:

Adım 1 — Akışları numaralandır
  Her madde akışına, iş akışına ve ısı transfer akışına bir numara ata.
  Toplam akış sayısı: n_s

Adım 2 — Bilinmeyenleri belirle
  Her akış için bir bilinmeyen: c_j (j = 1, 2, ..., n_s)
  Toplam bilinmeyen: n_s

Adım 3 — Maliyet denge denklemlerini yaz
  Her bileşen için bir denklem: n_k adet
  (n_k = toplam bileşen sayısı)

Adım 4 — Sınır koşullarını belirle
  Dışarıdan bilinen c değerleri:
  - Yakıt fiyatı → c_yakıt
  - Elektrik fiyatı → c_elektrik
  - Ortam havası → c_hava = 0
  - Soğutma suyu girişi → c_cw = 0
  Toplam sınır koşulu: n_b

Adım 5 — Yardımcı denklemleri ekle
  Eksik denklem sayısı: n_aux = n_s - n_k - n_b
  F-kuralı ve P-kuralı ile n_aux adet yardımcı denklem yazılır

Kontrol:
  n_s = n_k + n_b + n_aux  → Çözülebilir doğrusal sistem
```

### 4.2 Matris Formülasyonu

Tüm denklemler matris formunda yazılabilir:

```
[A] · {c} = {b}

Burada:
- [A]  = n_s × n_s katsayı matrisi (exergy hızları ile oluşur)
- {c}  = n_s × 1 bilinmeyen vektörü (birim exergy maliyetleri)
- {b}  = n_s × 1 sağ taraf vektörü (Ż değerleri ve bilinen maliyetler)

Çözüm:
  {c} = [A]⁻¹ · {b}  (matris tersine çarpma)
  veya
  Gauss eliminasyonu, LU ayrıştırma vb. sayısal yöntemler
```

> **Detaylı matris formülasyonu:** `matrix_formulation.md` dosyasına bakınız.

### 4.3 Toplam Sistem Maliyet Dengesi

Tüm bileşenlerin maliyet dengeleri toplandığında, iç akışlar sadeleşir ve sistem sınırı
üzerinden bir toplam denge elde edilir:

```
Σ Ċ_ürün,sistem = Σ Ċ_kaynak,sistem + Σ Ż_k

Burada:
- Σ Ċ_ürün,sistem = Sistemin nihai ürünlerinin toplam maliyet akışı
- Σ Ċ_kaynak,sistem = Sisteme dışarıdan giren kaynakların toplam maliyet akışı
- Σ Ż_k = Tüm bileşenlerin toplam seviyelendirilmiş maliyeti

Bu denge, doğrulama (verification) için kullanılır:
  Sol taraf = Sağ taraf → Çözüm tutarlı
```

### 4.4 Birim Sayısı ve Yardımcı Denklem Gereksinimleri

Her bileşen tipi için gereken yardımcı denklem sayısını gösteren referans tablo:

| Bileşen Tipi | Çıkış Sayısı | Maliyet Dengesi | Yardımcı | Kural |
|--------------|-------------|----------------|----------|-------|
| Kompresör | 1 madde | 1 | 0 | — |
| Türbin | 1 iş + 1 madde | 1 | 1 | F-kuralı: c_in = c_out |
| Kazan | 1 buhar (+baca) | 1 | 0-1 | Baca atık → Ċ_baca = 0 |
| Isı değiştirici | 2 madde | 1 | 1 | F-kuralı: c_h,in = c_h,out |
| Pompa | 1 madde | 1 | 0 | — |
| Chiller | 1 madde (+kond.) | 1 | 0-1 | Kond. atık → Ċ_kond = 0 |
| Kondenser | 1-2 madde | 1 | 0-1 | Dissipative, yönteme bağlı |
| Karıştırıcı | 1 madde | 1 | 0 | Tek çıkış |
| Ayırıcı (2-çıkış) | 2 madde | 1 | 1 | P-kuralı: c_out1 = c_out2 |
| Kısma valfi | 1 madde | 1 | 0 | Dissipative, yönteme bağlı |

### 4.5 Denklem Sayısı Doğrulama Örneği

```
Örnek: Basit Rankine çevrimi (4 bileşen)

Akışlar: 1, 2, 3, 4 (madde) + Ẇ_T, Ẇ_P (iş) + yakıt = 7 akış
Bilinmeyenler: c_1, c_2, c_3, c_4, c_Ẇ = 5
  (c_yakıt bilinen, Ẇ_T ve Ẇ_P aynı c_Ẇ ile)

Maliyet denge denklemleri: 4 (kazan, türbin, kondenser, pompa)
Sınır koşulları: 1 (c_yakıt bilinen)
Yardımcı denklemler: 5 - 4 - 0 = 1
  → 1 yardımcı denklem gerekli → Türbin F-kuralı: c_1 = c_2

Kontrol: 4 + 1 + 1 (sınır) = 6 denklem, 5 bilinmeyen + 1 bilinen → OK
  (c_yakıt bilinen olduğu için etkin bilinmeyen 5, denklem 5)
```

## 5. Sınır Koşulları ve Dış Kaynak Maliyetleri

### 5.1 Yakıt Maliyetleri

```
Doğalgaz:
  c_NG = Fiyat_NG / (LHV × φ_CH)

  Burada:
  - Fiyat_NG = Doğalgaz birim fiyatı [€/m³ veya €/kWh_th]
  - LHV = Alt ısıl değer [kJ/m³]
  - φ_CH = Kimyasal exergy / LHV oranı ≈ 1.04 (doğalgaz için)

  Tipik: c_NG ≈ 0.007 - 0.012 €/kJ  (2024 Türkiye endüstriyel)

Kömür:
  c_kömür = Fiyat_kömür / (LHV × φ_CH)
  φ_CH ≈ 1.06 (bitümlü kömür)
  Tipik: c_kömür ≈ 0.003 - 0.006 €/kJ

Fuel oil:
  c_fueloil = Fiyat_fueloil / (LHV × φ_CH)
  φ_CH ≈ 1.06
  Tipik: c_fueloil ≈ 0.006 - 0.010 €/kJ
```

### 5.2 Elektrik Maliyeti

```
Şebekeden alınan elektrik:
  c_el = Fiyat_el / 3600  [€/kJ]

  (Elektrik zaten saf exergy'dir, dönüşüm gerekmez)

  Tipik: c_el ≈ 0.025 - 0.040 €/kJ  (≈ 90 - 144 €/MWh)
  (2024 Türkiye endüstriyel tarife)

  MWh bazında: c_el = Fiyat_el [€/MWh] / 3,600,000 [kJ/MWh]
```

### 5.3 Sıfır Maliyetli Akışlar

```
Ortam havası:       c_hava = 0
Soğutma suyu girişi: c_cw,in = 0  (deniz suyu, nehir suyu)
Ortam sıcaklığı:    c_T₀ = 0

Not: Soğutma suyu kuleden geliyorsa → c_cw > 0 (kule maliyeti dahil)
```

## 6. Yardımcı Denklemler — F-Kuralı ve P-Kuralı Detayları

### 6.1 F-Kuralı (Fuel Rule) — Formülasyon

```
F-Kuralı:
  Bir bileşenin Yakıt tanımı birden fazla exergy akışı farkından oluşuyorsa,
  bu farkı oluşturan akışların birim exergy maliyetleri eşittir.

Matematiksel ifade:
  Yakıt = (Ė_a - Ė_b) ise → c_a = c_b

Uygulama örnekleri:
  Türbin:   F = Ė_in - Ė_out → c_in = c_out
  HX:       F = Ė_h,in - Ė_h,out → c_h,in = c_h,out
  Kondenser: F = Ė_in - Ė_out → c_in = c_out

Fiziksel anlam:
  Yakıt olarak harcanan exergy azalışında, birim exergy'nin parasal değeri
  korunur. Yani giren ve çıkan akışkanın birim exergy kalitesi aynı fiyatla
  değerlendirilir.
```

### 6.2 P-Kuralı (Product Rule) — Formülasyon

```
P-Kuralı:
  Bir bileşenin Ürün tanımı birden fazla exergy akışı veya farkından oluşuyorsa,
  bu ürünlerin birim exergy maliyetleri eşittir.

Matematiksel ifade:
  Ürün = Ẇ + (Ė_a - Ė_b) ise → c_Ẇ = (Ċ_a - Ċ_b)/(Ė_a - Ė_b)

Uygulama örnekleri:
  Ayırıcı: P = Ė_2 + Ė_3 → c_2 = c_3
  CHP:     P = Ẇ + (Ė_ara - Ė_ref) → c_Ẇ = c_ısı

Fiziksel anlam:
  Bir bileşenin ürettiği farklı ürünler aynı birim exergy maliyetine sahiptir.
  Bu, üretim amacının birden fazla çıkışa eşit dağıtıldığı varsayımına dayanır.
```

### 6.3 Yardımcı Denklem Seçim Rehberi

```
Karar ağacı:

Bileşen çıkış sayısı > 1?
│
├─ Evet → Ürün tanımında birden fazla akış var mı?
│   │
│   ├─ Evet → P-kuralı uygula
│   │
│   └─ Hayır → Yakıt tanımında birden fazla akış farkı var mı?
│       │
│       ├─ Evet → F-kuralı uygula
│       │
│       └─ Hayır → Ek bilgi gerekli (sınır koşulu veya dissipative)
│
└─ Hayır → Yardımcı denklem gerekmez
```

> **Detaylı F/P kuralları:** `auxiliary_equations.md` dosyasına bakınız.

## 7. Tam Sayısal Örnek: Basit Rankine Çevrimi

Bu bölümde 4 bileşenli (kazan, türbin, kondenser, pompa) bir Rankine çevriminin tam exergoekonomik
maliyet dengesi analizi adım adım sunulmaktadır.

### 7.1 Sistem Tanımı ve Şema

```
Basit Rankine Çevrimi — Buhar Güç Santrali

Bileşenler:
  I.   Kazan (B)    — Doğalgaz yakarak buhar üretir
  II.  Türbin (T)   — Buhar genişletilerek elektrik üretilir
  III. Kondenser (K) — Buhar yoğuşturulur
  IV.  Pompa (P)    — Su yüksek basınca pompalanır

Yakıt: Doğalgaz (Stream 5)
Ürün: Net elektrik (Ẇ_net = Ẇ_T - Ẇ_P)
```

```
                       Ė₅ (yakıt)
                          │
                          ▼
                    ┌───────────┐
          Ė₄ ────→ │   KAZAN   │ ────→ Ė₁
          (su)      │   (B)     │        (buhar, yüksek P-T)
                    └───────────┘
                          │
                          ▼ (baca gazı — ihmal)

          ┌───────────────────────────────────┐
          │                                   │
          │    ┌───────────┐                  │
          │    │  TÜRBİN   │ ────→ Ẇ_T       │
  Ė₁ ────┘────│   (T)     │                  │
               └─────┬─────┘                  │
                     │                        │
                     ▼ Ė₂                     │
               ┌───────────┐                  │
               │ KONDENSER  │                  │
               │   (K)     │                  │
               └─────┬─────┘                  │
                     │                        │
                     ▼ Ė₃                     │
               ┌───────────┐                  │
     Ẇ_P ────→│   POMPA   │ ────→ Ė₄ ───────┘
               │   (P)     │
               └───────────┘
```

### 7.2 Akış Numaralandırması

| Akış No | Açıklama | Konum |
|---------|----------|-------|
| 1 | Kızgın buhar | Kazan çıkışı → Türbin girişi |
| 2 | Düşük basınçlı buhar | Türbin çıkışı → Kondenser girişi |
| 3 | Doymuş sıvı (su) | Kondenser çıkışı → Pompa girişi |
| 4 | Sıkıştırılmış sıvı (su) | Pompa çıkışı → Kazan girişi |
| 5 | Doğalgaz (yakıt) | Dış kaynak → Kazan |
| Ẇ_T | Türbin iş çıkışı | Türbin → Jeneratör |
| Ẇ_P | Pompa iş girişi | Motor → Pompa |

### 7.3 Termodinamik Veriler

```
Çevrim koşulları:
  Kazan basıncı:     80 bar
  Kazan çıkış sıcaklığı: 500°C (kızgın buhar)
  Kondenser basıncı: 0.1 bar (≈ 45.8°C doyma)
  Referans ortam:    T₀ = 25°C = 298.15 K, P₀ = 1.013 bar
  Kütle debisi:      ṁ = 14 kg/s
```

### 7.4 Akış Exergy Verileri

| Akış | T [°C] | P [bar] | h [kJ/kg] | s [kJ/kg·K] | e [kJ/kg] | Ė [kW] |
|------|--------|---------|-----------|-------------|-----------|---------|
| 1 | 500 | 80 | 3398.3 | 6.724 | 1453.6 | 20,350 |
| 2 | 45.8 | 0.1 | 2584.7 | 8.150 | 124.3 | 1,740 |
| 3 | 45.8 | 0.1 | 191.8 | 0.649 | 2.1 | 29 |
| 4 | 46.5 | 80 | 200.5 | 0.651 | 10.1 | 141 |
| 5 | — | — | — | — | — | 50,000 |

```
Exergy hesaplama detayı (Stream 1 örneği):

  e_1 = (h_1 - h₀) - T₀ · (s_1 - s₀)
      = (3398.3 - 104.9) - 298.15 × (6.724 - 0.367)
      = 3293.4 - 298.15 × 6.357
      = 3293.4 - 1895.1
      = 1398.3 kJ/kg  (fiziksel exergy)
      + 55.3 kJ/kg (kimyasal exergy su buharı — küçük, dahil edildi)
      ≈ 1453.6 kJ/kg

  Ė_1 = ṁ × e_1 = 14 × 1453.6 = 20,350 kW
```

### 7.5 İş Akışları

```
Türbin gücü (brüt):
  Ẇ_T = ṁ × (h_1 - h_2) = 14 × (3398.3 - 2584.7) = 14 × 813.6 = 11,390 kW

Pompa gücü:
  Ẇ_P = ṁ × (h_4 - h_3) = 14 × (200.5 - 191.8) = 14 × 8.7 = 122 kW

Net güç:
  Ẇ_net = Ẇ_T - Ẇ_P = 11,390 - 122 = 11,268 kW ≈ 11.27 MW
```

### 7.6 Yakıt/Ürün Tanımları ve Exergy Yıkımı

| Bileşen | Ė_F [kW] | Ė_P [kW] | Ė_D [kW] | ε [%] |
|---------|-----------|-----------|-----------|-------|
| Kazan (B) | 50,000 | 20,350 - 141 = 20,209 | 29,791 | 40.4 |
| Türbin (T) | 20,350 - 1,740 = 18,610 | 11,390 | 7,220 | 61.2 |
| Kondenser (K) | 1,740 - 29 = 1,711 | — (dissipative) | 1,711 | — |
| Pompa (P) | 122 | 141 - 29 = 112 | 10 | 91.8 |

```
Doğrulama — Toplam exergy dengesi:

  Ė_F,toplam = Ė_yakıt + Ẇ_P = 50,000 + 122 = 50,122 kW
  Ė_P,toplam = Ẇ_T = 11,390 kW
  Ė_D,toplam = 29,791 + 7,220 + 1,711 + 10 = 38,732 kW

  Kontrol: Ė_F = Ė_P + Ė_D → 50,122 ≈ 11,390 + 38,732 = 50,122  ✓
```

### 7.7 Ekonomik Veriler ve Ż Hesabı

```
Ekonomik parametreler:
  CRF = 0.1175 (i = %10, n = 20 yıl)
  τ = 7,500 saat/yıl
  φ_TCI = 3.0 (yeni tesis)
  γ = 0.04 (bakım oranı, tüm bileşenler)
```

| Bileşen | PEC [€] | TCI [€] | Ż_CI [€/h] | Ż_OM [€/h] | Ż_toplam [€/h] |
|---------|---------|---------|-------------|-------------|-----------------|
| Kazan (B) | 1,800,000 | 5,400,000 | 84.60 | 9.60 | 94.20 |
| Türbin (T) | 4,200,000 | 12,600,000 | 197.40 | 22.40 | 219.80 |
| Kondenser (K) | 400,000 | 1,200,000 | 18.80 | 2.13 | 20.93 |
| Pompa (P) | 150,000 | 450,000 | 7.05 | 0.80 | 7.85 |
| **TOPLAM** | **6,550,000** | **19,650,000** | **307.85** | **34.93** | **342.78** |

```
Hesaplama örneği (Kazan):
  TCI_B = PEC_B × φ_TCI = 1,800,000 × 3.0 = 5,400,000 €
  Ż_CI,B = CRF × TCI_B / τ = 0.1175 × 5,400,000 / 7,500 = 84.60 €/h
  Ż_OM,B = γ × PEC_B / τ = 0.04 × 1,800,000 / 7,500 = 9.60 €/h
  Ż_B = 84.60 + 9.60 = 94.20 €/h
```

### 7.8 Maliyet Denge Denklemleri

Bu sistemde kondenseri Yöntem C (bağımsız bileşen) ile ele alıyoruz.

**Bilinmeyenler:** c₁, c₂, c₃, c₄, c_Ẇ (5 adet bilinmeyen)

**Bilinen (sınır koşulu):** c₅ = c_yakıt = 0.008 €/kJ (doğalgaz)

#### Denklem 1 — Kazan (B)

```
Çıkışların maliyeti = Girişlerin maliyeti + Ż_B

c₁ · Ė₁ = c₅ · Ė₅ + c₄ · Ė₄ + Ż_B

c₁ · 20,350 = 0.008 × 50,000 + c₄ · 141 + 94.20

Sayısal:
  20,350 · c₁ - 141 · c₄ = 400.00 + 94.20 = 494.20   ... (I)
```

#### Denklem 2 — Türbin (T)

```
Çıkışların maliyeti = Girişlerin maliyeti + Ż_T

c_Ẇ · Ẇ_T + c₂ · Ė₂ = c₁ · Ė₁ + Ż_T

c_Ẇ · 11,390 + c₂ · 1,740 = c₁ · 20,350 + 219.80

Sayısal:
  11,390 · c_Ẇ + 1,740 · c₂ - 20,350 · c₁ = 219.80   ... (II)
```

#### Denklem 3 — Kondenser (K)

```
Kondenser bağımsız bileşen olarak:
  Soğutma suyu maliyetsiz (c_cw = 0), atık ısı maliyetsiz

c₃ · Ė₃ = c₂ · Ė₂ - Ė_Q_atık_maliyeti + Ż_K

Basitleştirilmiş (Ė_Q atık, Ċ_atık = 0):
c₃ · Ė₃ = c₂ · Ė₂ + Ż_K

c₃ · 29 = c₂ · 1,740 + 20.93

Sayısal:
  29 · c₃ - 1,740 · c₂ = 20.93   ... (III)
```

#### Denklem 4 — Pompa (P)

```
c₄ · Ė₄ = c₃ · Ė₃ + c_Ẇ · Ẇ_P + Ż_P

c₄ · 141 = c₃ · 29 + c_Ẇ · 122 + 7.85

Sayısal:
  141 · c₄ - 29 · c₃ - 122 · c_Ẇ = 7.85   ... (IV)
```

#### Denklem 5 — Yardımcı Denklem (Türbin F-kuralı)

```
Türbin yakıtı = Ė₁ - Ė₂ (exergy farkı)
F-kuralı → c₁ = c₂   ... (V)
```

### 7.9 Denklem Sisteminin Matris Formülasyonu

```
5 denklem, 5 bilinmeyen: c₁, c₂, c₃, c₄, c_Ẇ

         c₁        c₂       c₃       c₄      c_Ẇ     | RHS
(I)    20,350       0        0      -141       0       | 494.20
(II)  -20,350     1,740      0        0     11,390     | 219.80
(III)    0       -1,740     29        0        0       | 20.93
(IV)     0          0      -29      141      -122      | 7.85
(V)      1         -1        0        0        0       | 0

[A] · {c} = {b}

     ┌  20350      0     0   -141      0   ┐   ┌ c₁ ┐   ┌ 494.20 ┐
     │ -20350   1740     0      0  11390   │   │ c₂ │   │ 219.80 │
     │      0  -1740    29      0      0   │ × │ c₃ │ = │  20.93 │
     │      0      0   -29    141   -122   │   │ c₄ │   │   7.85 │
     └      1     -1     0      0      0   ┘   └ c_Ẇ┘   └   0    ┘
```

### 7.10 Çözüm

Denklem sistemi adım adım çözülür:

```
Adım 1: Denklem (V)'den → c₁ = c₂

Adım 2: Denklem (I)'e c₂ yerine c₁ yazılır (ileriki adımlarda kullanılacak).
  Denklem (I): 20,350 · c₁ - 141 · c₄ = 494.20

Adım 3: Denklem (II)'de c₂ = c₁ yerine yazılır:
  -20,350 · c₁ + 1,740 · c₁ + 11,390 · c_Ẇ = 219.80
  -18,610 · c₁ + 11,390 · c_Ẇ = 219.80   ... (II')

Adım 4: Denklem (I)'den c₄ cinsinden c₁:
  c₄ = (20,350 · c₁ - 494.20) / 141   ... (I')

Adım 5: Denklem (III)'den c₃ cinsinden c₂ = c₁:
  29 · c₃ = 1,740 · c₁ + 20.93
  c₃ = (1,740 · c₁ + 20.93) / 29 = 60 · c₁ + 0.7214   ... (III')

Adım 6: Denklem (IV)'e (I') ve (III') yerleştirilir:
  141 · c₄ - 29 · c₃ - 122 · c_Ẇ = 7.85

  141 · [(20,350 · c₁ - 494.20) / 141] - 29 · [60 · c₁ + 0.7214] - 122 · c_Ẇ = 7.85

  (20,350 · c₁ - 494.20) - (1,740 · c₁ + 20.92) - 122 · c_Ẇ = 7.85

  20,350 · c₁ - 1,740 · c₁ - 122 · c_Ẇ = 7.85 + 494.20 + 20.92

  18,610 · c₁ - 122 · c_Ẇ = 522.97   ... (IV')

Adım 7: (II') ve (IV') iki bilinmeyenli iki denklem:
  -18,610 · c₁ + 11,390 · c_Ẇ = 219.80   ... (II')
   18,610 · c₁ -    122 · c_Ẇ = 522.97   ... (IV')

  Toplama:
  (11,390 - 122) · c_Ẇ = 219.80 + 522.97
  11,268 · c_Ẇ = 742.77
  c_Ẇ = 742.77 / 11,268
  c_Ẇ = 0.06592 €/kJ

Adım 8: c₁ hesabı (IV' kullanarak):
  18,610 · c₁ = 522.97 + 122 × 0.06592
  18,610 · c₁ = 522.97 + 8.04
  18,610 · c₁ = 531.01
  c₁ = 531.01 / 18,610
  c₁ = 0.02853 €/kJ

Adım 9: c₂ = c₁ = 0.02853 €/kJ

Adım 10: c₃ hesabı (III'):
  c₃ = 60 × 0.02853 + 0.7214
  c₃ = 1.7118 + 0.7214
  c₃ = 2.4332 €/kJ

Adım 11: c₄ hesabı (I'):
  c₄ = (20,350 × 0.02853 - 494.20) / 141
  c₄ = (580.58 - 494.20) / 141
  c₄ = 86.38 / 141
  c₄ = 0.6126 €/kJ
```

### 7.11 Sonuç Özeti

| Akış | Ė [kW] | c [€/kJ] | c [€/GJ] | Ċ [€/h] |
|------|---------|----------|----------|---------|
| 1 (buhar HP) | 20,350 | 0.02853 | 28.53 | 2,091.0 |
| 2 (buhar LP) | 1,740 | 0.02853 | 28.53 | 178.8 |
| 3 (sıvı su) | 29 | 2.4332 | 2,433.2 | 254.1 |
| 4 (su HP) | 141 | 0.6126 | 612.6 | 311.1 |
| 5 (yakıt) | 50,000 | 0.00800 | 8.00 | 1,440.0 |
| Ẇ_T (türbin işi) | 11,390 | 0.06592 | 65.92 | 2,704.3 |
| Ẇ_P (pompa işi) | 122 | 0.06592 | 65.92 | 29.0 |

```
Birim elektrik maliyeti:
  c_Ẇ = 0.06592 €/kJ = 65.92 €/GJ = 237.3 €/MWh

Karşılaştırma:
  Yakıt birim maliyeti:    c₅ = 8.00 €/GJ
  Buhar birim maliyeti:    c₁ = 28.53 €/GJ (yakıtın 3.57 katı)
  Elektrik birim maliyeti: c_Ẇ = 65.92 €/GJ (yakıtın 8.24 katı)
```

### 7.12 Doğrulama (Verification)

#### 7.12.1 Her Bileşen İçin Maliyet Dengesi Kontrolü

```
Kazan (B):
  Sol: c₁ · Ė₁ = 0.02853 × 20,350 = 580.58 €/h
  Sağ: c₅ · Ė₅ + c₄ · Ė₄ + Ż_B = 400.00 + 0.6126 × 141 + 94.20
       = 400.00 + 86.38 + 94.20 = 580.58 €/h  ✓

Türbin (T):
  Sol: c_Ẇ · Ẇ_T + c₂ · Ė₂ = 0.06592 × 11,390 + 0.02853 × 1,740
       = 751.03 + 49.64 = 800.67 €/h
  Sağ: c₁ · Ė₁ + Ż_T = 0.02853 × 20,350 + 219.80
       = 580.58 + 219.80 = 800.38 €/h  ≈ ✓ (fark: yuvarlama)

Kondenser (K):
  Sol: c₃ · Ė₃ = 2.4332 × 29 = 70.56 €/h
  Sağ: c₂ · Ė₂ + Ż_K = 0.02853 × 1,740 + 20.93
       = 49.64 + 20.93 = 70.57 €/h  ≈ ✓

Pompa (P):
  Sol: c₄ · Ė₄ = 0.6126 × 141 = 86.38 €/h
  Sağ: c₃ · Ė₃ + c_Ẇ · Ẇ_P + Ż_P = 2.4332 × 29 + 0.06592 × 122 + 7.85
       = 70.56 + 8.04 + 7.85 = 86.45 €/h  ≈ ✓ (fark: yuvarlama)
```

#### 7.12.2 Toplam Sistem Dengesi Kontrolü

```
Sistem sınırı üzerinden:

Giriş: Ċ₅ + Σ Ż = 1,440.00 + 342.78 = 1,782.78 €/h
Çıkış: Ċ_Ẇ,net + Ċ_atık = c_Ẇ · (Ẇ_T - Ẇ_P) + Ċ_atık

Ẇ_net maliyeti: 0.06592 × (11,390 - 122) = 0.06592 × 11,268 = 742.79 €/h

Exergy kaybı maliyeti (çevreye atılan):
  Kaybolan maliyet = Σ Ċ_D = Σ (c_F,k · Ė_D,k)

Toplam kontrol — Alternatif doğrulama:
  Σ Ċ_giren = Ċ₅ = 1,440.00 €/h
  Σ Ż = 342.78 €/h
  Σ Ċ_çıkan = Ċ_Ẇ,net = 742.79 €/h

  Fark = 1,440.00 + 342.78 - 742.79 = 1,039.99 €/h

  Bu fark, exergy yıkımı ve kaybının toplam maliyetidir:
  Σ Ċ_D + Σ Ċ_L = 1,040 €/h  (kondenser atığı dahil)
```

### 7.13 Exergoekonomik Değerlendirme Kriterleri

```
Bileşen bazlı kriterler:
  c_F,k = Ċ_F,k / Ė_F,k     (yakıt birim maliyeti)
  c_P,k = Ċ_P,k / Ė_P,k     (ürün birim maliyeti)
  Ċ_D,k = c_F,k · Ė_D,k     (exergy yıkım maliyeti)
  f_k = Ż_k / (Ż_k + Ċ_D,k) (exergoekonomik faktör)
  r_k = (c_P,k - c_F,k) / c_F,k  (göreli maliyet farkı)
```

| Bileşen | c_F [€/GJ] | c_P [€/GJ] | Ċ_D [€/h] | Ż [€/h] | Ċ_D+Ż [€/h] | f_k | r_k |
|---------|-----------|-----------|-----------|---------|-------------|------|------|
| Kazan (B) | 8.00 | 28.53 | 858.1 | 94.20 | 952.3 | 0.099 | 2.57 |
| Türbin (T) | 28.53 | 65.92 | 741.9 | 219.80 | 961.7 | 0.229 | 1.31 |
| Kondenser (K) | — | — | — | 20.93 | — | — | — |
| Pompa (P) | 65.92 | 612.6 | 2.37 | 7.85 | 10.22 | 0.768 | 8.29 |

```
Hesaplama detayı — Kazan:
  c_F,B = c₅ = 0.008 €/kJ = 8.00 €/GJ
  c_P,B = Ċ_P / Ė_P = (Ċ₁ - Ċ₄) / (Ė₁ - Ė₄)
        = (580.58 - 86.38) / (20,350 - 141)
        = 494.20 / 20,209 = 0.02446 €/kJ = 24.46 €/GJ

  Düzeltme: Aslında c_P tam olarak:
  c_P,B = (c₁·Ė₁ - c₄·Ė₄) / (Ė₁ - Ė₄)
        = (580.58 - 86.38) / 20,209
        = 494.20 / 20,209
        = 0.02446 €/kJ

  Ama daha basit yaklaşım — maliyet dengesi bazında:
  Ċ_P,B = Ċ_F,B + Ż_B = c₅·Ė₅ + Ż_B = 400.00 + 94.20 = 494.20 €/h
  c_P,B = 494.20 / 20,209 = 0.02446 €/kJ = 24.46 €/GJ

  Ċ_D,B = c_F,B · Ė_D,B = 0.008 × 29,791 = 238.33 €/h

  Alternatif hesaplama (toplam düzeltmeli):
  Ċ_D,B = c_F,B · Ė_D,B = 8.00 × 29,791 / 1000 = 238.33 €/h
  (birim dikkat: 8.00 €/GJ × 29,791 kW = 8.00 × 29,791 × 3.6 / 10⁶ × 10⁶ ...)

  Doğru birim hesabı:
  Ċ_D,B = c_F,B [€/kJ] × Ė_D,B [kW] × 3600 [s/h]
        = 0.008 × 29,791 × 3.6 = 858.0 €/h

  f_B = Ż_B / (Ż_B + Ċ_D,B) = 94.20 / (94.20 + 858.0) = 94.20 / 952.2 = 0.099
  r_B = (c_P,B - c_F,B) / c_F,B = (24.46 - 8.00) / 8.00 = 2.06

Hesaplama detayı — Türbin:
  c_F,T = c₁ = 0.02853 €/kJ = 28.53 €/GJ
  Ė_P,T = Ẇ_T = 11,390 kW
  Ċ_P,T = c_Ẇ · Ẇ_T = 0.06592 × 11,390 × 3.6 = 2,704.3 €/h
  c_P,T = c_Ẇ = 0.06592 €/kJ = 65.92 €/GJ

  Ċ_D,T = c_F,T × Ė_D,T × 3.6 = 0.02853 × 7,220 × 3.6 = 741.9 €/h
  f_T = Ż_T / (Ż_T + Ċ_D,T) = 219.80 / (219.80 + 741.9) = 219.80 / 961.7 = 0.229
  r_T = (65.92 - 28.53) / 28.53 = 37.39 / 28.53 = 1.31

Hesaplama detayı — Pompa:
  c_F,P = c_Ẇ = 0.06592 €/kJ = 65.92 €/GJ
  Ė_P,P = Ė₄ - Ė₃ = 141 - 29 = 112 kW
  Ċ_P,P = Ċ₄ - Ċ₃ = (86.38 - 70.56) = 15.82 €/h
  c_P,P = 15.82 / (112 × 3.6) = 15.82 / 403.2 = 0.03924 €/kJ = 39.24 €/GJ

  Düzeltilmiş hesaplama:
  c_P,P = Ċ_P,P / (Ė_P,P × 3.6) = (c_Ẇ·Ẇ_P·3.6 + Ż_P) / (Ė_P,P × 3.6)
        = (0.06592 × 122 × 3.6 + 7.85) / (112 × 3.6)
        = (28.96 + 7.85) / 403.2
        = 36.81 / 403.2
        = 0.09129 €/kJ = 91.29 €/GJ

  Ċ_D,P = c_F,P × Ė_D,P × 3.6 = 0.06592 × 10 × 3.6 = 2.37 €/h
  f_P = Ż_P / (Ż_P + Ċ_D,P) = 7.85 / (7.85 + 2.37) = 7.85 / 10.22 = 0.768
  r_P = (91.29 - 65.92) / 65.92 = 25.37 / 65.92 = 0.385
```

### 7.14 Düzeltilmiş Değerlendirme Sonuçları

| Bileşen | c_F [€/GJ] | c_P [€/GJ] | Ċ_D [€/h] | Ż [€/h] | Ċ_D+Ż [€/h] | f_k | r_k |
|---------|-----------|-----------|-----------|---------|-------------|------|------|
| Kazan (B) | 8.00 | 24.46 | 858.0 | 94.20 | 952.2 | 0.099 | 2.06 |
| Türbin (T) | 28.53 | 65.92 | 741.9 | 219.80 | 961.7 | 0.229 | 1.31 |
| Pompa (P) | 65.92 | 91.29 | 2.37 | 7.85 | 10.22 | 0.768 | 0.385 |

### 7.15 Sonuçların Yorumlanması

```
Önceliklendirme — Ċ_D + Ż sıralamasına göre:

1. Türbin (T):  Ċ_D + Ż = 961.7 €/h
   f_T = 0.229 (düşük) → Exergy yıkım maliyeti baskın
   r_T = 1.31 (yüksek) → Önemli iyileştirme potansiyeli
   Öneri: Türbin izentropik verimini artırmak öncelikli.
   → Daha verimli kanat profili, azaltılmış kaçak akışlar
   → %1 verim artışı ≈ 72 kW daha az Ė_D ≈ 7.4 €/h tasarruf

2. Kazan (B):   Ċ_D + Ż = 952.2 €/h
   f_B = 0.099 (çok düşük) → Termodinamik verimlilik çok kötü
   r_B = 2.06 (çok yüksek) → En büyük iyileştirme potansiyeli
   Öneri: Yanma verimi artırılmalı, baca gazı sıcaklığı düşürülmeli.
   → Ekonomizer eklenmesi, hava ön ısıtıcısı
   → Oksijen fazlalığı optimizasyonu

3. Pompa (P):   Ċ_D + Ż = 10.22 €/h
   f_P = 0.768 (yüksek) → Yatırım maliyeti baskın
   r_P = 0.385 (düşük) → Verimli çalışıyor
   Öneri: Pompa zaten verimli, daha ucuz alternatif değerlendirilebilir.
   → Düşük öncelikli; kazan ve türbine odaklanılmalı

4. Kondenser (K): Dissipative bileşen
   Ż_K = 20.93 €/h
   Ė_D,K = 1,711 kW (kaçınılmaz büyük oranda)
   Öneri: Kondenser basıncı optimizasyonu (trade-off: düşük basınç
   → daha fazla türbin güç çıkışı ama daha büyük kondenser)
```

## 8. Özel Durumlar ve Dikkat Edilecek Noktalar

### 8.1 Birim Tutarlılığı

Exergoekonomik hesaplamalarda en sık yapılan hata birim uyumsuzluğudur:

```
Birim dönüşüm tablosu:

| Büyüklük | SI Birimi | Pratik Birim | Dönüşüm |
|----------|-----------|-------------|---------|
| c | €/kJ | €/GJ | × 10⁶ |
| c | €/kJ | €/MWh | × 3.6 × 10⁶ |
| Ċ | €/s | €/h | × 3600 |
| Ė | kW | MW | / 1000 |

Dikkat: Ċ = c · Ė hesaplanırken
  Ċ [€/s] = c [€/kJ] × Ė [kW]  (çünkü kW = kJ/s)
  Ċ [€/h] = c [€/kJ] × Ė [kW] × 3600 [s/h]
  Ċ [€/h] = c [€/GJ] × Ė [kW] × 3600 / 10⁶ = c [€/GJ] × Ė [kW] × 0.0036
```

### 8.2 Çok Düşük Exergy'li Akışlar

```
Sorun: Ė → 0 olduğunda, c = Ċ / Ė → ∞ olur.

Örnek: Kondenser çıkışındaki sıvı su (Stream 3)
  Ė₃ = 29 kW (çok düşük), c₃ = 2.4332 €/kJ (çok yüksek)

Bu fiziksel bir anlamsızlık değildir:
  Ċ₃ = c₃ · Ė₃ = 2.4332 × 29 × 3.6 = 254.1 €/h → Makul bir değer

Birim maliyet yüksek çünkü:
  - Bu akışkan, üzerine harcanan tüm maliyeti taşır
  - Exergy'si düşük olsa da, maliyet akışı sıfır değildir
  - Çevrim tamamlamak için gerekli bir akıştır

Pratik kural:
  c çok yüksek ancak Ċ makul ise → Sorun yok
  c çok yüksek VE Ċ çok yüksek ise → Denklem veya tanım hatası kontrol et
```

### 8.3 Negatif Exergy Farkları

```
Sorun: Ė_çıkış - Ė_giriş < 0 olması beklenirken > 0 çıkması (veya tersi)

Olası nedenler:
1. Yanlış F/P tanımı (soğutma uygulamasında yön hatası)
2. Referans ortam sıcaklığı yanlış seçilmiş
3. Kimyasal exergy dahil edilmemiş (reaksiyonlu sistemlerde)

Çözüm:
  F/P tanımını fuel_product_definitions.md ile kontrol et
  T₀ ve P₀ değerlerini doğrula
  Ė_D > 0 koşulunu kontrol et (negatif olamaz)
```

### 8.4 Kapalı Çevrimlerde Yakınsama

```
Kapalı çevrimlerde (Rankine, Brayton vb.) akışlar birbirine bağlıdır.
Doğrusal denklem sistemi her zaman tek çözüme sahiptir
(yardımcı denklemler doğru yazılmışsa).

Dikkat: İteratif çözüm GEREKMEZ — Doğrusal denklem sistemidir.
Matris çözümü veya analitik çözüm doğrudan uygulanır.

Yaygın hata: Maliyet dengesini iteratif çözmeye çalışmak
→ Doğrusal denklem sistemi → Matris çözümü yeterli ve kesin
```

## 9. Çoklu Bileşen Sistemleri İçin Genel Kurallar

### 9.1 Seri Bağlı Bileşenler

```
A → B → C (seri bağlı)

Her bileşenin çıkış maliyeti, bir sonraki bileşenin giriş maliyetidir:
  c_çıkış,A = c_giriş,B
  c_çıkış,B = c_giriş,C

Maliyet zincirleme olarak artar:
  c_A < c_B < c_C (her bileşen maliyet ekler)
```

### 9.2 Paralel Bağlı Bileşenler

```
     ┌→ A →┐
X →  │     │ → Y
     └→ B →┘

Ayırıcı + Karıştırıcı kullanılır:
  Ayırıcı (P-kuralı): c_A,giriş = c_B,giriş = c_X
  Karıştırıcı: c_Y = (Ċ_A,çıkış + Ċ_B,çıkış) / Ė_Y
```

### 9.3 Geri Besleme (Recycle) Döngüleri

```
        ┌─────────────────┐
        │                 │
X → A → B → C → Y        │
              │           │
              └─→ R ──────┘

Geri besleme akışı (R) ek bir bilinmeyen ekler.
Doğrusal denklem sistemine dahil edilir; ek yardımcı denklem gerekmez
(geri besleme karıştırıcıda birleşir).
```

## 10. ExergyLab Platformunda Uygulama Notları

### 10.1 Mevcut Altyapı ile Entegrasyon

```
ExergyLab mevcut çıktılar:
  - Ė_D (her bileşen için exergy yıkımı) ✓
  - ε (exergy verimi) ✓
  - Yıllık kayıp [€/yıl] (basitleştirilmiş) ✓

Exergoekonomik analiz için ek gereksinimler:
  - PEC verileri (kullanıcı girdisi veya korelasyon)
  - CRF parametreleri (i, n, τ)
  - Yakıt birim maliyetleri (c_yakıt, c_elektrik)
  - Maliyet denge denklem sistemi çözücüsü
```

### 10.2 Hesaplama Akışı

```
1. Kullanıcı girişleri:
   ├── Ekipman PEC değerleri (veya korelasyondan)
   ├── Ekonomik parametreler (CRF, τ, φ_TCI, γ)
   └── Kaynak maliyetleri (c_yakıt, c_elektrik)

2. Engine hesaplamaları:
   ├── Exergy analizi (mevcut) → Ė, Ė_D, ε
   ├── Ż hesabı (yeni) → Ż_CI, Ż_OM
   ├── Maliyet denge denklem sistemi kurulumu (yeni)
   ├── Matris çözümü (yeni) → c değerleri
   └── Değerlendirme kriterleri (yeni) → Ċ_D, f_k, r_k

3. AI yorumlama:
   ├── Bileşen önceliklendirmesi (Ċ_D + Ż sıralaması)
   ├── f_k yorumu (verimlilik mi yatırım mı?)
   ├── r_k yorumu (iyileştirme potansiyeli)
   └── Somut öneriler (benchmark karşılaştırması ile)
```

### 10.3 Tipik Endüstriyel Değer Aralıkları

| Parametre | Tipik Aralık | Birim | Not |
|-----------|-------------|-------|-----|
| c_doğalgaz | 7-12 | €/GJ | Türkiye endüstriyel |
| c_elektrik | 70-150 | €/MWh | Türkiye endüstriyel |
| c_buhar (10 bar) | 20-40 | €/GJ | Kazan veriminden bağımlı |
| c_buhar (40 bar) | 25-50 | €/GJ | Yüksek basınç |
| c_soğuk_su (7°C) | 80-200 | €/GJ | Chiller COP'una bağlı |
| c_basınçlı_hava | 100-300 | €/GJ | Kompresör veriminden bağımlı |
| f_k (tipik) | 0.15-0.65 | — | Bileşen tipine bağlı |
| r_k (tipik) | 0.2-3.0 | — | Bileşen tipine bağlı |

### 10.4 Benchmark Karşılaştırma Tablosu

| Bileşen | f_k Tipik | f_k İyi | f_k Kötü | Yorum |
|---------|----------|---------|---------|-------|
| Kompresör | 0.35-0.55 | > 0.40 | < 0.20 | Ż ve Ċ_D dengeli olmalı |
| Türbin | 0.25-0.50 | > 0.30 | < 0.15 | Verimlilik kritik |
| Kazan | 0.10-0.30 | > 0.15 | < 0.08 | Yüksek Ė_D, düşük f_k beklenir |
| Pompa | 0.40-0.70 | > 0.45 | < 0.25 | Küçük bileşen, Ż görece yüksek |
| HX | 0.30-0.60 | > 0.35 | < 0.15 | ΔT'ye çok bağımlı |
| Chiller | 0.25-0.50 | > 0.30 | < 0.15 | COP kritik |
| Kondenser | — | — | — | Dissipative, f_k tanımsız |

## 11. Adım Adım Uygulama Kontrol Listesi

```
Exergoekonomik Maliyet Dengesi — Kontrol Listesi:

□ 1. Sistem şemasını çiz, bileşenleri numaralandır
□ 2. Tüm akışları (madde + iş + ısı) numaralandır
□ 3. Her akışın exergy hızını (Ė) hesapla veya al
□ 4. Her bileşen için F/P tanımı yap → fuel_product_definitions.md
□ 5. Ė_D ve ε hesapla (her bileşen)
□ 6. PEC değerlerini belirle → cost_equations.md
□ 7. CRF hesapla (i, n) → levelized_cost.md
□ 8. Ż_CI ve Ż_OM hesapla (her bileşen)
□ 9. Dış kaynak c değerlerini belirle (c_yakıt, c_elektrik)
□ 10. Bilinmeyen sayısını kontrol et:
     n_bilinmeyen = n_akış - n_bilinen_sınır_koşulu
□ 11. Her bileşen için maliyet denge denklemi yaz
□ 12. Yardımcı denklem gereksinimi hesapla:
     n_aux = n_bilinmeyen - n_bileşen
□ 13. F-kuralı ve P-kuralı ile yardımcı denklemleri yaz → auxiliary_equations.md
□ 14. Doğrusal denklem sistemini kur ([A]{c} = {b})
□ 15. Çöz → Tüm c değerlerini bul → matrix_formulation.md
□ 16. Ċ = c · Ė · 3600 hesapla (her akış, €/h cinsinden)
□ 17. Her bileşen için maliyet dengesi doğrula (sol = sağ?)
□ 18. Toplam sistem dengesi doğrula
□ 19. Ċ_D,k = c_F,k · Ė_D,k · 3.6 hesapla
□ 20. f_k = Ż_k / (Ż_k + Ċ_D,k) hesapla
□ 21. r_k = (c_P,k - c_F,k) / c_F,k hesapla
□ 22. Bileşenleri Ċ_D + Ż'ye göre sırala
□ 23. f_k ve r_k ile iyileştirme yönünü belirle → evaluation_criteria.md
□ 24. Sonuçları raporla
```

## 12. Sıkça Yapılan Hatalar

### 12.1 Denklem Kurulum Hataları

| Hata | Sonuç | Düzeltme |
|------|-------|---------|
| İş akışını bilinmeyen olarak saymamak | Eksik denklem | Her Ẇ ve Q̇ transfer akışı bir c bilinmeyeni |
| F-kuralı yerine P-kuralı uygulamak | Yanlış c değerleri | Yakıt tarafı → F-kuralı; Ürün tarafı → P-kuralı |
| Dissipative bileşene ürün atamak | Tutarsız denklem sistemi | Kondenser, valf → Dissipative yöntem uygula |
| c_ortam ≠ 0 almak | Maliyet şişmesi | Çevre sıcaklığındaki hava, su → c = 0 |
| Aynı c_Ẇ kullanmamak | Tutarsız fiyatlandırma | Aynı kaynak (şebeke) → Aynı c_Ẇ |

### 12.2 Hesaplama Hataları

| Hata | Sonuç | Düzeltme |
|------|-------|---------|
| Birim karışıklığı (€/kJ vs €/GJ) | Büyüklük sırası hata | Tutarlı birim seti seç, dönüşümleri kontrol et |
| Ċ [€/s] ile Ż [€/h] toplamak | Yanlış f_k | Tüm değerleri aynı birime (€/h) çevir |
| Negatif c değeri elde etmek | Fiziksel anlamsızlık | Denklem sistemini, F/P tanımlarını kontrol et |
| c_3 yüksek diye alarm vermek | Gereksiz endişe | Ċ₃ = c₃ · Ė₃'e bak; düşük Ė ile yüksek c beklenir |

### 12.3 Yorumlama Hataları

| Hata | Sonuç | Düzeltme |
|------|-------|---------|
| Sadece Ċ_D'ye göre sıralamak | Ż'yi göz ardı etmek | Ċ_D + Ż toplamını kullan |
| f_k = 0.5'i ideal saymak | Yanlış hedef | f_k optimum değeri sisteme bağlıdır |
| Küçük bileşeni ihmal etmek | Fırsat kaybı | Ċ_D + Ż toplamı küçükse bile kontrol et |
| Kondenser Ė_D'sini tek başına değerlendirmek | Yanıltıcı | Dissipative bileşenin Ė_D'si bağlamla değerlendirilmeli |

## İlgili Dosyalar

- `factory/exergoeconomic/speco_method.md` — SPECO metodolojisi detayları ve 4 temel adım
- `factory/exergoeconomic/fuel_product_definitions.md` — Her ekipman tipi için F/P tanımları
- `factory/exergoeconomic/auxiliary_equations.md` — F-kuralı ve P-kuralı detaylı açıklama
- `factory/exergoeconomic/matrix_formulation.md` — Matris formülasyonu ve sayısal çözüm yöntemleri
- `factory/exergoeconomic/evaluation_criteria.md` — f_k, r_k, Ċ_D değerlendirme kriterleri
- `factory/exergoeconomic/levelized_cost.md` — CRF ve Ż hesaplama detayları
- `factory/exergoeconomic/cost_equations.md` — PEC korelasyonları
- `factory/exergoeconomic/overview.md` — Exergoekonomik analize genel bakış

## Referanslar

1. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs in thermal systems." *Energy*, 31(8-9), 1257-1289.
2. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Chapters 7-9.
3. Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
4. Tsatsaronis, G., Winhold, M. (1985). "Exergoeconomic analysis and evaluation of energy-conversion plants." *Energy*, 10(1), 69-94.
5. Lozano, M.A., Valero, A. (1993). "Theory of the exergetic cost." *Energy*, 18(9), 939-960.
6. Frangopoulos, C.A. (1987). "Thermo-economic functional analysis and optimization." *Energy*, 12(7), 563-571.
7. Tsatsaronis, G., Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
8. Turton, R., Bailie, R.C., Whiting, W.B., Shaeiwitz, J.A. (2012). *Analysis, Synthesis, and Design of Chemical Processes*. 4th Ed.
