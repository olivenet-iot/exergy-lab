---
title: "SPECO Metodu (Specific Exergy Costing Method)"
category: factory
equipment_type: factory
keywords: [SPECO, exergoekonomik, Tsatsaronis, Lazzaretto, yakıt-ürün, maliyet denkliği]
related_files:
  - factory/exergoeconomic/overview.md
  - factory/exergoeconomic/fuel_product_definitions.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/exergoeconomic/auxiliary_equations.md
  - factory/exergoeconomic/evaluation_criteria.md
use_when:
  - "SPECO metodu adımları uygulanırken"
  - "Exergoekonomik denklem sistemi kurulurken"
  - "ECT veya TFA ile karşılaştırma yapılırken"
priority: high
last_updated: 2026-02-01
---
# SPECO Metodu (Specific Exergy Costing Method)

> Son güncelleme: 2026-02-01

## 1. Giriş

SPECO (Specific Exergy Costing), Lazzaretto ve Tsatsaronis tarafından 2006 yılında yayınlanan, termal sistemlerin exergoekonomik analizinde standart ve sistematik bir metodoloji sunan yaklaşımdır. SPECO, exergoekonomik analiz için en yaygın kullanılan yöntem olup ExergyLab platformunun referans metodolojisidir.

### 1.1 SPECO'nun Temel Farkları

| Özellik | SPECO | Diğer Yöntemler |
|---------|-------|-----------------|
| F/P tanımı | Exergy akış farkları (stream-based) | Önerme veya fonksiyon bazlı |
| Yardımcı denklemler | F-kuralı / P-kuralı | Propositions / Fonksiyonlar |
| Tutarlılık | Her zaman tutarlı, çözüm garantili | Yönteme ve uygulayıcıya bağlı |
| Öğrenme eğrisi | Orta — sistematik adımlar | Yüksek — kavramsal anlayış gerektirir |
| Endüstriyel uygulanabilirlik | Yüksek | Orta-Düşük |

## 2. SPECO Metodunun 4 Temel Adımı

```
SPECO Adımları:
┌─────────────────────────────────────────────┐
│ Adım 1: Exergy Analizi                      │
│   → Her akışın exergy'sini hesapla          │
│   → Bileşen bazlı Ė_D belirle              │
├─────────────────────────────────────────────┤
│ Adım 2: Yakıt (F) ve Ürün (P) Tanımları    │
│   → SPECO F/P kurallarını uygula           │
│   → Her bileşen için Ė_F ve Ė_P belirle    │
├─────────────────────────────────────────────┤
│ Adım 3: Maliyet Denklemleri                 │
│   → Her bileşen: 1 maliyet denklemi        │
│   → Yardımcı denklemler (F-kuralı/P-kuralı)│
│   → Doğrusal denklem sistemi oluştur       │
├─────────────────────────────────────────────┤
│ Adım 4: Değerlendirme                       │
│   → c_F,k, c_P,k hesapla                   │
│   → Ċ_D,k, f_k, r_k değerlendir           │
│   → İyileştirme öncelikleri belirle        │
└─────────────────────────────────────────────┘
```

## 3. Adım 1: Exergy Analizi

### 3.1 Akış Exergy'leri

Her akışın (stream) toplam exergy'si fiziksel ve kimyasal bileşenlerden oluşur:

```
Ė_j = ṁ_j · e_j = ṁ_j · (e_PH,j + e_CH,j)

Burada:
- Ė_j = j. akışın exergy hızı [kW]
- ṁ_j = Kütle debisi [kg/s]
- e_j = Spesifik exergy [kJ/kg]
- e_PH = Fiziksel (physical) exergy [kJ/kg]
- e_CH = Kimyasal (chemical) exergy [kJ/kg]

Fiziksel exergy:
e_PH = (h - h₀) - T₀·(s - s₀)

Burada:
- h, s = Akışın entalpi ve entropi değerleri
- h₀, s₀ = Referans ortam koşullarındaki değerler
- T₀ = Referans ortam sıcaklığı [K]
```

### 3.2 Bileşen Exergy Dengesi

```
Ė_F,k = Ė_P,k + Ė_D,k + Ė_L,k

Burada:
- Ė_F,k = k. bileşenin Yakıt exergy'si [kW]
- Ė_P,k = k. bileşenin Ürün exergy'si [kW]
- Ė_D,k = k. bileşendeki Exergy yıkımı [kW]
- Ė_L,k = k. bileşenin Exergy kaybı [kW] (sistem dışına çıkan)
```

### 3.3 Exergy Verimi

```
ε_k = Ė_P,k / Ė_F,k

veya

ε_k = 1 - (Ė_D,k + Ė_L,k) / Ė_F,k
```

## 4. Adım 2: Yakıt (F) ve Ürün (P) Tanımları

### 4.1 SPECO F/P Kuralları

SPECO metodunda F ve P tanımları exergy farklarına dayanır:

**Kural 1 — Ürün Tanımı:**
- Bileşenin amacına uygun olan exergy artışları Ürün'dür
- Ürün = (Çıkış exergy'si - Giriş exergy'si) artış olduğunda

**Kural 2 — Yakıt Tanımı:**
- Ürün elde etmek için harcanan exergy azalışları Yakıt'tır
- Yakıt = (Giriş exergy'si - Çıkış exergy'si) azalış olduğunda

**Kural 3 — İş ve Isı:**
- Bileşene giren iş (Ẇ) → Yakıt
- Bileşenden çıkan iş → Ürün
- Isı transferi → Exergy olarak değerlendirilir: Ė_Q = Q̇·(1 - T₀/T)

### 4.2 Temel Ekipman F/P Tanımları

| Ekipman | Yakıt (Ė_F) | Ürün (Ė_P) |
|---------|-------------|-------------|
| Kompresör | Ẇ_C | Ė_çıkış - Ė_giriş |
| Türbin | Ė_giriş - Ė_çıkış | Ẇ_T |
| Kazan | Ė_yakıt (kimyasal) | Ė_buhar,çıkış - Ė_su,giriş |
| Isı değiştirici | Ė_sıcak,giriş - Ė_sıcak,çıkış | Ė_soğuk,çıkış - Ė_soğuk,giriş |
| Pompa | Ẇ_P | Ė_çıkış - Ė_giriş |
| Chiller | Ẇ_kompresör | Ė_soğuk,giriş - Ė_soğuk,çıkış |
| Kondenser (dissipatif) | Ė_giriş - Ė_çıkış | — (dışsal olarak tanımlanır) |
| Valf | — | — (dissipatif) |

> **Detaylı F/P tanımları:** `fuel_product_definitions.md` dosyasına bakınız.

### 4.3 Dissipative Bileşenler

Kondenser, kısma valfi gibi dissipative bileşenlerde doğrudan bir ürün tanımlanamaz. SPECO bu bileşenleri şu şekilde ele alır:

```
Seçenek A: Dissipative bileşeni servis ettiği bileşene dahil et
Seçenek B: Exergy yıkımını servis ettiği bileşenler arasında dağıt
Seçenek C: Ayrı bileşen olarak tut, ürün olarak ısı atımını kullan

SPECO tavsiyesi: Seçenek A veya B (tercihen A)
```

## 5. Adım 3: Maliyet Denklemleri

### 5.1 Maliyet Denge Denklemi

Her bileşen k için:

```
Ċ_P,k = Ċ_F,k + Ż_k

veya akış bazlı:

Σ Ċ_çıkış,k + Ċ_Ẇ,k = Σ Ċ_giriş,k + Ċ_Q,k + Ż_k

Burada:
- Ċ_j = c_j · Ė_j — j. akışın maliyet akışı [€/saat]
- c_j = j. akışın birim exergy maliyeti [€/kJ]
- Ż_k = k. bileşenin seviyelendirilmiş yıllık maliyeti [€/saat]
```

### 5.2 Denklem Sayısı Kontrolü

```
Bilinmeyenler: n_stream adet c değeri (her akış için bir birim maliyet)
Denklemler: n_component adet maliyet dengesi
Eksik: n_stream - n_component adet → Yardımcı denklemlerle tamamlanır

Kontrol: n_yardımcı = n_stream - n_component
```

### 5.3 Yardımcı Denklemler — F-Kuralı ve P-Kuralı

**F-Kuralı (Fuel Rule):**
Bir bileşenin Yakıt'ı birden fazla akış farkından oluşuyorsa, bu akışların her biri için birim exergy maliyeti eşittir.

```
F-Kuralı: Yakıt akışlarında c_giriş = c_çıkış

Örnek — Türbin:
  Yakıt = Ė₁ - Ė₂ (basınç düşümü)
  F-kuralı: c₁ = c₂
```

**P-Kuralı (Product Rule):**
Bir bileşenin Ürün'ü birden fazla akış farkından oluşuyorsa, bu ürünlerin birim exergy maliyeti eşittir.

```
P-Kuralı: Ürün akışlarında c değerleri eşit

Örnek — Kojenerasyon türbini (elektrik + buhar):
  Ürün = Ẇ + (Ė₃ - Ė₄) → farklı ürünler
  P-kuralı: c_Ẇ = c_ısı yani c_Ẇ = (Ċ₃ - Ċ₄)/(Ė₃ - Ė₄)
```

### 5.4 Sınır Koşulları

```
- Dış kaynak akışları: c bilinen (yakıt, elektrik fiyatı)
  Örnek: c_doğalgaz = Yakıt fiyatı / LHV exergy [€/kJ]
  Örnek: c_elektrik = Elektrik fiyatı / 3600 [€/kJ]

- Çevre sıcaklığında giren akışlar: c = 0 (veya ≈ 0)
  Örnek: c_hava = 0, c_soğutma_suyu_giriş = 0
```

## 6. Adım 4: Değerlendirme

### 6.1 Exergy Yıkım Maliyeti

```
Ċ_D,k = c_F,k · Ė_D,k  [€/saat]

Yıllık: Ċ_D,k,yıllık = Ċ_D,k × τ  [€/yıl]
  (τ = yıllık çalışma saati, tipik: 7000-8760 saat)
```

### 6.2 Exergoekonomik Faktör (f_k)

```
f_k = Ż_k / (Ż_k + Ċ_D,k)

Karar Rehberi:
┌─────────────────────────────────────────────────────────┐
│ f_k < 0.25                                              │
│ → Ċ_D baskın                                           │
│ → Termodinamik verimlilik iyileştirilmeli               │
│ → Daha verimli ekipman veya proses değişikliği          │
├─────────────────────────────────────────────────────────┤
│ 0.25 ≤ f_k ≤ 0.70                                      │
│ → Dengeli bölge                                         │
│ → Optimizasyon için en uygun aralık                     │
│ → İnce ayar (fine-tuning) ile iyileştirme yapılabilir   │
├─────────────────────────────────────────────────────────┤
│ f_k > 0.70                                              │
│ → Ż baskın                                              │
│ → Yatırım maliyeti çok yüksek                          │
│ → Daha ucuz bileşen veya azaltılmış kapasite düşünülür │
└─────────────────────────────────────────────────────────┘
```

### 6.3 Göreli Maliyet Farkı (r_k)

```
r_k = (c_P,k - c_F,k) / c_F,k

Basitleştirilmiş:
r_k = (1 - ε_k) / ε_k + Ż_k / (c_F,k · Ė_P,k)

Yorum:
- r_k düşük → Bileşen maliyet-etkin çalışıyor
- r_k yüksek → Hem termodinamik hem ekonomik iyileştirme potansiyeli var
```

## 7. Sayısal Örnek: 4-Bileşenli Basit Çevrim

### 7.1 Sistem Tanımı

```
Basit Rankine Çevrimi:
  1. Kazan (B): Su → Buhar
  2. Türbin (T): Buhar genişlemesi → Elektrik
  3. Kondenser (C): Buhar yoğuşması
  4. Pompa (P): Su basınçlandırma

Akışlar:
  1: Kazan çıkışı (yüksek basınç buhar)
  2: Türbin çıkışı (düşük basınç buhar)
  3: Kondenser çıkışı (sıvı su)
  4: Pompa çıkışı (yüksek basınç su)
  5: Yakıt (doğalgaz)
  6: Türbin işi (Ẇ_T)
  7: Pompa işi (Ẇ_P)
```

### 7.2 Exergy Verileri

| Akış | Ė [kW] | Açıklama |
|------|---------|----------|
| 1 | 15,200 | Yüksek basınç buhar |
| 2 | 8,100 | Düşük basınç buhar |
| 3 | 340 | Sıvı su (kondenser çıkışı) |
| 4 | 460 | Sıvı su (pompa çıkışı) |
| 5 | 42,000 | Yakıt exergy'si (doğalgaz) |
| Ẇ_T | 6,800 | Türbin gücü |
| Ẇ_P | 320 | Pompa gücü |

### 7.3 F/P Tanımları ve Exergy Yıkımı

| Bileşen | Ė_F [kW] | Ė_P [kW] | Ė_D [kW] | ε [%] |
|---------|-----------|-----------|-----------|-------|
| Kazan | 42,000 | 15,200 - 460 = 14,740 | 27,260 | 35.1 |
| Türbin | 15,200 - 8,100 = 7,100 | 6,800 | 300 | 95.8 |
| Kondenser | 8,100 - 340 = 7,760 | — (dissipatif) | 7,760* | — |
| Pompa | 320 | 460 - 340 = 120 | 200 | 37.5 |

> *Kondenser dissipative bileşendir; exergy yıkımı kazan ile türbine dağıtılır.

### 7.4 Ekonomik Veriler

| Bileşen | PEC [€] | Ż [€/saat] |
|---------|---------|-------------|
| Kazan | 1,200,000 | 28.50 |
| Türbin | 2,800,000 | 66.50 |
| Kondenser | 350,000 | 8.30 |
| Pompa | 120,000 | 2.85 |

### 7.5 Maliyet Denklemleri

**Bilinmeyenler:** c₁, c₂, c₃, c₄, c_Ẇ (5 bilinmeyen)

**Maliyet denge denklemleri (4 adet):**

```
Kazan:    c₁·Ė₁ - c₄·Ė₄ = c₅·Ė₅ + Ż_B
          c₁·15200 - c₄·460 = 0.008·42000 + 28.50

Türbin:   c_Ẇ·Ẇ_T + c₂·Ė₂ = c₁·Ė₁ + Ż_T
          c_Ẇ·6800 + c₂·8100 = c₁·15200 + 66.50

Kond.:    c₃·Ė₃ = c₂·Ė₂ + Ż_C (atık ısı maliyetsiz)
          c₃·340 = c₂·8100 + 8.30

Pompa:    c₄·Ė₄ - c₃·Ė₃ = c_Ẇ·Ẇ_P + Ż_P
          c₄·460 - c₃·340 = c_Ẇ·320 + 2.85
```

**Yardımcı denklem (1 adet):**

```
Türbin F-kuralı: c₁ = c₂
(Yakıt: Ė₁ - Ė₂ → giriş ve çıkış birim maliyeti eşit)
```

### 7.6 Çözüm

```
c₅ = 0.008 €/kJ (doğalgaz — veri)
c₁ = c₂ = 0.0252 €/kJ (F-kuralı ile)
c₃ = 0.624 €/kJ
c₄ = 0.487 €/kJ
c_Ẇ = 0.0378 €/kJ = 136.1 €/MWh
```

### 7.7 Değerlendirme Sonuçları

| Bileşen | Ċ_D [€/h] | Ż [€/h] | Ċ_D+Ż [€/h] | f_k | r_k |
|---------|------------|----------|--------------|-----|-----|
| Kazan | 218.1 | 28.50 | 246.6 | 0.116 | 1.85 |
| Türbin | 7.56 | 66.50 | 74.06 | 0.898 | 0.50 |
| Pompa | 5.04 | 2.85 | 7.89 | 0.361 | 16.75 |

**Yorumlama:**
- **Kazan:** f_k = 0.116 (çok düşük) → Termodinamik verimlilik iyileştirilmeli. r_k = 1.85 → Yüksek iyileştirme potansiyeli.
- **Türbin:** f_k = 0.898 (çok yüksek) → Yatırım maliyeti baskın, daha ucuz alternatif değerlendirilebilir.
- **Pompa:** f_k = 0.361 (dengeli) → Optimizasyon ile ince ayar yapılabilir.

## 8. SPECO vs ECT vs TFA Detaylı Karşılaştırma

### 8.1 Exergetik Maliyet Teorisi (ECT — Valero et al.)

```
ECT Yaklaşımı:
- "Önerme" (proposition) bazlı yardımcı denklemler
- Exergetik maliyet (k*) ve birim exergetik maliyet (k) kullanır
- Proposition P1: Dış kaynak akışlarının exergetik maliyeti = exergy'si
- Proposition P2: Atık akışların birim exergetik maliyeti = sıfır
- Proposition P3: Aynı bileşenden çıkan aynı tip akışların birim maliyeti eşit

Avantajlar:
+ Teorik açıdan tutarlı
+ Atık tanımı ile temiz formülasyon

Dezavantajlar:
- "Atık" ve "ürün" ayrımı subjektif olabilir
- Karmaşık sistemlerde proposition seçimi zor
```

### 8.2 Termoekonomik Fonksiyonel Analiz (TFA — Frangopoulos)

```
TFA Yaklaşımı:
- Her bileşenin "fonksiyonel ürünü" tanımlanır
- Fonksiyonel diyagram ile akış ilişkileri kurulur
- Matris formülasyonu farklı — fonksiyonel matris

Avantajlar:
+ Fiziksel anlam açık
+ Fonksiyonel ilişkiler net

Dezavantajlar:
- Karmaşık sistemlerde fonksiyonel diyagram oluşturma zor
- Uygulamada subjektif seçimler gerektirir
- Standardizasyon eksik
```

### 8.3 Karşılaştırma Tablosu

| Kriter | SPECO | ECT | TFA |
|--------|-------|-----|-----|
| F/P tanım kolaylığı | ★★★★ | ★★★ | ★★ |
| Yardımcı denklem sistematikliği | ★★★★★ | ★★★ | ★★ |
| Dissipative bileşen işleme | ★★★★ | ★★★ | ★★★ |
| Büyük sistem uygulanabilirliği | ★★★★ | ★★★ | ★★ |
| Sonuç tekrarlanabilirliği | ★★★★★ | ★★★★ | ★★★ |
| Yazılım entegrasyonu | ★★★★★ | ★★★ | ★★ |
| Akademik kabul | ★★★★★ | ★★★★ | ★★★ |

> **Not:** ExergyLab SPECO metodunu standart olarak kullanır. Bu karşılaştırma bilgi amaçlıdır.

## 9. SPECO Uygulama Kontrol Listesi

```
□ 1. Sistem şemasını çiz, bileşenleri numaralandır
□ 2. Tüm akışları numaralandır
□ 3. Her akışın exergy'sini hesapla (fiziksel + kimyasal)
□ 4. Her bileşen için F ve P tanımı yap (Tablo kullan)
□ 5. Ė_D = Ė_F - Ė_P hesapla (her bileşen)
□ 6. ε_k = Ė_P / Ė_F hesapla
□ 7. PEC korelasyonlarından ekipman maliyetlerini belirle
□ 8. CRF ile seviyelendirilmiş Ż hesapla
□ 9. Her bileşen için maliyet denge denklemini yaz
□ 10. Denklem sayısı kontrolü: n_bilinmeyen = n_denklem + n_yardımcı?
□ 11. Yardımcı denklemleri ekle (F-kuralı / P-kuralı)
□ 12. Doğrusal sistemi çöz → c değerlerini bul
□ 13. Ċ_D,k, f_k, r_k hesapla
□ 14. Sonuçları yorumla ve iyileştirme önceliklerini belirle
```

## 10. Yaygın Hatalar ve Dikkat Edilecek Noktalar

### 10.1 F/P Tanımı Hataları

| Hata | Doğru Yaklaşım |
|------|-----------------|
| Kondensere ürün atamak | Dissipative bileşen olarak ele al |
| İş akışlarını akış olarak numaralandırmamak | Her Ẇ ve Q̇ bir maliyet akışı olmalı |
| Fiziksel ve kimyasal exergy'yi ayırmamak | Kazan gibi bileşenlerde ayırım kritik |
| Negatif exergy farkını göz ardı etmek | F veya P negatifse tanım gözden geçirilmeli |

### 10.2 Denklem Sistemi Hataları

| Hata | Doğru Yaklaşım |
|------|-----------------|
| Denklem sayısını kontrol etmemek | n_bilinmeyen = n_maliyet_dengesi + n_yardımcı + n_sınır |
| F-kuralı yerine P-kuralı uygulamak | Kuralları doğru bileşene uygula |
| Sınır koşullarını unutmak | Dış kaynak maliyetleri (yakıt, elektrik) bilinmelidir |
| Tutarsız birimler | Tüm c değerleri aynı birimde olmalı (€/kJ) |

## İlgili Dosyalar

- `factory/exergoeconomic/overview.md` — Exergoekonomik analize genel bakış
- `factory/exergoeconomic/fuel_product_definitions.md` — Detaylı F/P tanımları (10 ekipman)
- `factory/exergoeconomic/exergoeconomic_balance.md` — Maliyet denge denklemleri detayı
- `factory/exergoeconomic/auxiliary_equations.md` — F-kuralı, P-kuralı detayları
- `factory/exergoeconomic/evaluation_criteria.md` — f_k, r_k detaylı yorumlama
- `factory/exergoeconomic/matrix_formulation.md` — Matris formülasyonu ve Python kodu

## Referanslar

1. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs in thermal systems." *Energy*, 31(8-9), 1257-1289.
2. Tsatsaronis, G., Winhold, M. (1985). "Exergoeconomic analysis and evaluation of energy-conversion plants." *Energy*, 10(1), 69-94.
3. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
4. Tsatsaronis, G. (2008). "Recent developments in exergy analysis and exergoeconomics." *Int. J. Exergy*, 5(5-6), 489-499.
5. Valero, A., et al. (1994). "Application of the exergetic cost theory to the CGAM problem." *Energy*, 19(3), 365-381.
6. Frangopoulos, C.A. (1987). "Thermo-economic functional analysis and optimization." *Energy*, 12(7), 563-571.
