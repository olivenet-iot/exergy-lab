---
title: "İteratif Exergoekonomik Yöntem (Iterative Exergoeconomic Method)"
category: thermoeconomic_optimization
keywords: [iteratif yöntem, Tsatsaronis, exergoekonomik faktör, bağıl maliyet farkı, f_k, r_k]
related_files: [knowledge/factory/thermoeconomic_optimization/overview.md, knowledge/factory/thermoeconomic_optimization/parametric_optimization.md, knowledge/factory/thermoeconomic_optimization/practical_guide.md]
use_when: ["Mevcut sistemlerin exergoekonomik iyileştirmesi gerektiğinde", "f_k ve r_k değerlerinin yorumlanması istendiğinde"]
priority: high
last_updated: 2026-02-02
---

# İteratif Exergoekonomik Yöntem (Iterative Exergoeconomic Method)

## 1. Genel Bakış

Tsatsaronis ve arkadaşları tarafından geliştirilen iteratif exergoekonomik optimizasyon
yöntemi, formal matematiksel optimizasyon kullanmadan, exergoekonomik değişkenlerin
(f_k, r_k, Ċ_D,k) sistematik yorumlanmasıyla bileşen bazlı iyileştirme yapar.

### Yöntemin Özellikleri

| Özellik | Açıklama |
|---------|----------|
| Yaklaşım | Heuristik, mühendislik sezgisiyle uyumlu |
| Karmaşıklık | Düşük-orta |
| Global optimum | Garanti yok, ancak iyi çözümler üretir |
| Uygulama kolaylığı | Yüksek |
| Veri gereksinimi | Orta |
| Uygun sistemler | Mevcut tesisler, retrofit, 2-10 bileşenli sistemler |

---

## 2. Altı Adımlı Prosedür

### Adım 1: Exergy Analizi

Her bileşen (k) için exergy dengesi kur ve hesapla:

```
Ėx_F,k = Ėx_P,k + Ėx_D,k + Ėx_L,k

Hesaplanacaklar:
  Ėx_F,k  = Yakıt exergysi [kW]
  Ėx_P,k  = Ürün exergysi [kW]
  Ėx_D,k  = Exergy yıkımı [kW]
  Ėx_L,k  = Exergy kaybı [kW]
  ε_k     = Ėx_P,k / Ėx_F,k = Exergy verimi [%]
  y_D,k   = Ėx_D,k / Ėx_F,total = Exergy yıkım oranı [%]
```

### Adım 2: Ekonomik Analiz

Her bileşen için yatırım ve İ&B maliyet hızını hesapla:

```
Ż_k = (CRF × Z_k × φ_k) / τ    [€/h]

Burada:
  Z_k  = Toplam yatırım maliyeti (TCI) [€]
  φ_k  = İ&B çarpanı (tipik 1.06)
  τ    = Yıllık çalışma süresi [h/yıl]
  CRF  = Sermaye geri kazanım faktörü
```

### Adım 3: Exergoekonomik Denge

Her bileşen için maliyet dengesi denklemleri yaz ve çöz:

```
Ċ_P,k = Ċ_F,k + Ż_k - Ċ_L,k

veya detaylı:

Σ (c_j × Ėx_j)_çıkış + c_W × Ẇ_k = Σ (c_i × Ėx_i)_giriş + c_Q × Q̇_k + Ż_k
```

n bilinmeyen, n-1 denge denklemi → F-kuralı ve P-kuralı ile yardımcı denklemler ekle.

### Adım 4: Termoekonomik Değişkenleri Hesapla

Her bileşen için:

```
f_k = Ż_k / (Ż_k + Ċ_D,k + Ċ_L,k)    — Exergoekonomik faktör

r_k = (c_P,k - c_F,k) / c_F,k           — Bağıl maliyet farkı

Ċ_D,k = c_F,k × Ėx_D,k                  — Exergy yıkım maliyet hızı
```

### Adım 5: Değerlendir ve İyileştirme Yönü Belirle

f_k ve r_k değerlerine göre her bileşen için iyileştirme stratejisi belirle (Bölüm 3).

### Adım 6: Tasarım Değişikliği Uygula ve Tekrarla

- Değişiklikleri uygula
- Adım 1'den tekrar başla
- Yakınsama kontrolü yap (Bölüm 5)

---

## 3. f_k Değerlendirmesi

### 3.1. Karar Kuralları

```
f_k < 0.25 (Düşük):
  → Exergy yıkım maliyeti (Ċ_D) baskın
  → İyileştirme: Bileşen verimliliğini artır
  → Örnekler:
    - Daha verimli ekipman seç
    - Ek ısı transfer yüzeyi ekle
    - İzentropik verimi artır
    - NOT: Bu, yatırım maliyetini artıracaktır — ödünleşimi kontrol et

0.25 ≤ f_k ≤ 0.70 (Dengeli):
  → Yatırım ve exergy yıkım maliyetleri dengeli
  → İyileştirme: Her iki tarafı da dikkatli incele
  → Küçük iyileştirmeler yapılabilir ama büyük değişiklik gerekmez
  → r_k değerine bakarak öncelik belirle

f_k > 0.70 (Yüksek):
  → Yatırım maliyeti (Ż) baskın
  → İyileştirme: Bileşen maliyetini düşür
  → Örnekler:
    - Daha ucuz malzeme/üretici
    - Daha basit tasarım
    - Verimden taviz verilebilir
    - NOT: Bu, exergy yıkımını artırabilir — ödünleşimi kontrol et
```

### 3.2. Ekipman Bazlı Tipik f_k Değerleri

| Ekipman | Tipik f_k | Yorum |
|---------|-----------|-------|
| Kazan (büyük, >3 MW) | 0.15 – 0.30 | Genelde exergy yıkım baskın (yanma tersinmezliği) |
| Kazan (küçük, <500 kW) | 0.35 – 0.55 | Daha dengeli |
| Kompresör (vidalı) | 0.40 – 0.65 | Genelde dengeli |
| Kompresör (pistonlu) | 0.30 – 0.50 | Exergy yıkım biraz baskın |
| Isı değiştirici (shell-tube) | 0.35 – 0.65 | Yüzey alanına bağlı |
| Isı değiştirici (plakalı) | 0.45 – 0.70 | Daha pahalı, yüksek f_k |
| Pompa | 0.50 – 0.75 | Yatırım baskın olabilir |
| Türbin (gaz) | 0.35 – 0.55 | Dengeli |
| Türbin (buhar) | 0.40 – 0.60 | Dengeli |
| Chiller (santrifüj) | 0.45 – 0.65 | Dengeli - yatırım baskın |

---

## 4. r_k Değerlendirmesi

### 4.1. r_k Formülü ve Ayrıştırması

```
r_k = (c_P,k - c_F,k) / c_F,k

Ayrıştırma:
r_k = (1 - ε_k) / ε_k + Ż_k / (c_F,k × Ėx_P,k)

Burada:
  İlk terim  → Exergy yıkımından kaynaklanan maliyet artışı
  İkinci terim → Yatırımdan kaynaklanan maliyet artışı
```

### 4.2. Ekipman Bazlı r_k Benchmark Tablosu

| Ekipman | r_k Düşük | r_k Orta | r_k Yüksek | Alarm |
|---------|-----------|----------|------------|-------|
| Kompresör | < 0.25 | 0.25 - 0.45 | 0.45 - 0.60 | > 0.60 |
| Kazan | < 0.40 | 0.40 - 0.70 | 0.70 - 1.00 | > 1.00 |
| Türbin (gaz) | < 0.20 | 0.20 - 0.35 | 0.35 - 0.50 | > 0.50 |
| Türbin (buhar) | < 0.15 | 0.15 - 0.30 | 0.30 - 0.45 | > 0.45 |
| Isı değiştirici | < 0.15 | 0.15 - 0.30 | 0.30 - 0.45 | > 0.50 |
| Pompa | < 0.25 | 0.25 - 0.45 | 0.45 - 0.60 | > 0.60 |
| Chiller | < 0.50 | 0.50 - 0.90 | 0.90 - 1.20 | > 1.50 |

### 4.3. Yüksek r_k Durumunda Aksiyon

```
Yüksek r_k + Düşük f_k:
  → Exergy yıkımı çok yüksek, bileşen ucuz ama verimsiz
  → Aksiyon: Daha verimli bileşen al (yatırım artacak ama r_k düşecek)

Yüksek r_k + Yüksek f_k:
  → Hem pahalı hem de maliyet artışı yüksek
  → Aksiyon: Farklı teknoloji veya konfigürasyon ara

Yüksek r_k + Orta f_k:
  → Bileşen optimize edilmemiş
  → Aksiyon: Parametre optimizasyonu yap (sıcaklık, basınç, alan)
```

---

## 5. Yakınsama Kriterleri

### 5.1. Durdurma Koşulları

```
Yakınsama koşullarından BİRİ sağlandığında dur:

1. |ΔC_total| / C_total < ε₁    (tipik ε₁ = 0.01 - 0.02, yani %1-2)
2. |Δf_k| < ε₂ ∀k              (tipik ε₂ = 0.02, tüm bileşenlerde)
3. İterasyon sayısı > N_max     (tipik N_max = 5 - 10)
4. Hiçbir bileşende anlamlı iyileştirme potansiyeli kalmadı
```

### 5.2. Tipik Yakınsama Davranışı

| İterasyon | C_total Değişimi | Açıklama |
|-----------|-----------------|----------|
| 1 → 2 | -%5 ile -%15 | En büyük iyileştirme, büyük değişiklikler |
| 2 → 3 | -%2 ile -%5 | Orta iyileştirmeler |
| 3 → 4 | -%1 ile -%3 | İnce ayarlar |
| 4 → 5 | -%0.5 ile -%1 | Yakınsama başlangıcı |
| 5+ | < -%0.5 | Durdurma bölgesi |

> **Dikkat:** İterasyonlar arasında bir bileşenin iyileştirilmesi başka bir bileşeni
> olumsuz etkileyebilir. Bu nedenle her iterasyonda TÜM bileşenleri yeniden değerlendir.

---

## 6. Hesaplama Örneği: 3 Bileşenli Sistem

### 6.1. Sistem Tanımı

Basit buhar üretim sistemi:
- **Kazan (K):** 2,000 kW, doğalgaz, 8 bar doymuş buhar
- **Pompa (P):** Besleme suyu pompası, 5 kW
- **Economizer (E):** Baca gazı → besleme suyu ön ısıtma

```
                     Baca gazı
                        ↑
                   ┌────┴────┐
    Doğalgaz ──→  │  Kazan   │ ──→ 8 bar buhar
                   │   (K)    │
                   └────┬────┘
                        │ Baca gazı (sıcak)
                   ┌────┴────┐
    Besleme suyu ←│Economizer│ ← Besleme suyu (soğuk)
    (ısınmış)      │   (E)    │
                   └────┬────┘
                        │ Baca gazı (soğuk)
                        ↓ Baca

    Besleme suyu ← ┌────┐
    (basınçlı)     │Pompa│ ← Besleme suyu (tank)
                   │ (P) │
                   └────┘
```

### 6.2. İterasyon 0 — Baz Durum

#### Exergy Analizi

| Bileşen | Ėx_F [kW] | Ėx_P [kW] | Ėx_D [kW] | ε [%] | y_D [%] |
|---------|-----------|-----------|-----------|-------|---------|
| Kazan (K) | 2,280 | 620 | 1,580 | 27.2 | 69.4 |
| Economizer (E) | 85 | 55 | 30 | 64.7 | 1.3 |
| Pompa (P) | 5.0 | 4.2 | 0.8 | 84.0 | 0.04 |
| **Toplam** | **2,280** | **620** | **1,611** | **27.2** | **70.7** |

> **Kazan:** Yanma tersinmezliği nedeniyle exergy yıkımının %98'i kazanda oluşur.

#### Ekonomik Analiz

Parametreler: i = 8%, n = 15 yıl → CRF = 0.1168, τ = 5,500 h/yıl

| Bileşen | Z [€] | φ | Ż [€/h] |
|---------|-------|---|---------|
| Kazan (K) | 85,000 | 1.06 | 1.91 |
| Economizer (E) | 12,000 | 1.05 | 0.27 |
| Pompa (P) | 4,500 | 1.06 | 0.10 |

#### Exergoekonomik Analiz

Doğalgaz exergy maliyeti: c_fuel = 0.037 €/kWh

Denge denklemlerinin çözümünden:

| Bileşen | c_F [€/kWh] | c_P [€/kWh] | Ċ_D [€/h] | Ż [€/h] | f_k | r_k |
|---------|------------|------------|-----------|---------|-----|-----|
| Kazan (K) | 0.037 | 0.158 | 58.46 | 1.91 | 0.032 | 3.27 |
| Economizer (E) | 0.037 | 0.063 | 1.11 | 0.27 | 0.196 | 0.70 |
| Pompa (P) | 0.110 | 0.138 | 0.088 | 0.10 | 0.532 | 0.25 |

### 6.3. İterasyon 0 — Değerlendirme

#### Kazan (K): f_k = 0.032, r_k = 3.27

- f_k çok düşük (<<0.25) → Exergy yıkım maliyeti baskın
- r_k çok yüksek → Ürün maliyeti yakıt maliyetinin 4.27 katı
- **Yorum:** Yanma tersinmezliği çok yüksek. Ancak bu büyük ölçüde kaçınılamaz kayıptır.
- **Aksiyon:** Fazla hava azalt (%20 → %10), baca gazı sıcaklığını düşür (economizer büyüt)
- **Beklenti:** Ėx_D,K azalır, Ż_E artar

#### Economizer (E): f_k = 0.196, r_k = 0.70

- f_k düşük (<0.25) → Exergy yıkım maliyeti biraz baskın
- r_k orta-yüksek → İyileştirme potansiyeli var
- **Aksiyon:** Yüzey alanını artır (ΔT yaklaşımı azalt)
- **Beklenti:** ε_E artar, Ż_E artar ama Ċ_D,E azalır

#### Pompa (P): f_k = 0.532, r_k = 0.25

- f_k orta (dengeli) → İyi denge
- r_k düşük → Maliyet artışı kabul edilebilir
- **Aksiyon:** Düşük öncelik, değişiklik gerekmez

#### İyileştirme Önceliği: K > E > P (Ċ_D bazlı)

### 6.4. İterasyon 1 — Değişiklikler

Yapılan değişiklikler:
1. Kazan fazla hava: %20 → %10 (η_yanma artışı)
2. Economizer yüzey alanı: 15 m² → 30 m² (ΔT_yaklaşım: 40°C → 25°C)
3. Baca gazı sıcaklığı: 220°C → 160°C

#### Güncellenen Exergoekonomik Tablo

| Bileşen | c_F [€/kWh] | c_P [€/kWh] | Ċ_D [€/h] | Ż [€/h] | f_k | r_k |
|---------|------------|------------|-----------|---------|-----|-----|
| Kazan (K) | 0.037 | 0.148 | 52.17 | 1.91 | 0.035 | 3.00 |
| Economizer (E) | 0.037 | 0.056 | 0.74 | 0.42 | 0.362 | 0.51 |
| Pompa (P) | 0.110 | 0.138 | 0.088 | 0.10 | 0.532 | 0.25 |

#### Karşılaştırma

| Metrik | İter. 0 | İter. 1 | Değişim |
|--------|---------|---------|---------|
| Ċ_total [€/h] | 62.0 | 55.5 | -10.5% |
| C_total [€/yıl] | 341,000 | 305,250 | -35,750 |
| Toplam Ėx_D [kW] | 1,611 | 1,440 | -10.6% |
| η_ex (sistem) | 27.2% | 29.8% | +2.6 pp |

### 6.5. İterasyon 2 — İnce Ayar

Yapılan değişiklikler:
1. Besleme suyu sıcaklığı: 60°C → 85°C (deaeratör optimizasyonu)
2. Economizer yüzey alanı: 30 m² → 40 m²

| Metrik | İter. 1 | İter. 2 | Değişim |
|--------|---------|---------|---------|
| Ċ_total [€/h] | 55.5 | 54.2 | -2.3% |
| C_total [€/yıl] | 305,250 | 298,100 | -7,150 |

### 6.6. Sonuç

| Metrik | Baz Durum | Optimum | İyileşme |
|--------|-----------|---------|----------|
| C_total [€/yıl] | 341,000 | 298,100 | -12.6% |
| Yıllık tasarruf | - | 42,900 | - |
| Ek yatırım | - | 18,000 | - |
| SPP | - | 0.42 yıl | - |
| η_ex (sistem) | 27.2% | 30.5% | +3.3 pp |

---

## 7. Yaygın Hatalar ve Tuzaklar

1. **Kaçınılamaz exergy yıkımını görmezden gelmek:** Kazan yanma tersinmezliğinin büyük
   kısmı kaçınılamazdır. f_k düşük diye kazanı değiştirmek çözüm değildir.

2. **Bileşen etkileşimlerini ihmal etmek:** Economizer büyütmek kazan baca gazı basıncını
   artırabilir (fan gücü artar).

3. **Yalnızca Ċ_D,k'ya bakıp Ż_k etkisini görmemek:** Büyük iyileştirmeler büyük
   yatırım gerektirebilir.

4. **Çok erken durdurmak:** 1-2 iterasyon genellikle yetmez, 3-5 iterasyon önerilir.

5. **Çok geç durdurmak:** %0.5'ten az iyileşme varsa durulmalı, aksi halde zaman kaybı.

6. **f_k ve r_k değerlerini mutlak kabul etmek:** Bu değerler referans koşullara ve
   maliyet verilerine bağlıdır. Duyarlılık analizi mutlaka yapılmalıdır.

---

## 8. İteratif vs Formal Optimizasyon Karşılaştırması

| Özellik | İteratif Yöntem | Formal Optimizasyon |
|---------|----------------|---------------------|
| Global optimum garantisi | Hayır | Kısmen (NLP), Hayır (MINLP) |
| Uygulama kolaylığı | Yüksek | Düşük-Orta |
| Mühendislik sezgisi | Doğrudan kullanılır | Model içine gömülü |
| Çok amaçlı | Zorlaştırır | Doğal destek |
| Yapısal karar | Desteklemez | Destekler (MINLP) |
| Hesaplama maliyeti | Düşük | Orta-Yüksek |
| Sonuç kalitesi | İyi (optimal yakın) | İyi-Çok İyi |
| Veri gereksinimi | Orta | Yüksek |
| Öğrenme eğrisi | Düşük | Yüksek |

### Ne Zaman Hangisi?

```
İteratif yöntem tercih et:
  - Mevcut sistemin retrofit analizi
  - 2-5 bileşenli basit sistemler
  - Hızlı değerlendirme gerektiğinde
  - Mühendislik sezgisi ile doğrulama

Formal optimizasyon tercih et:
  - Yeni tesis tasarımı (greenfield)
  - 5+ bileşenli karmaşık sistemler
  - Çok amaçlı karar gerektiğinde
  - Yapısal kararlar (CHP, konfigürasyon)
  - CBAM etkili büyük yatırımlar
```

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `parametric_optimization.md` — Formal parametrik optimizasyon
- `structural_optimization.md` — Yapısal optimizasyon
- `practical_guide.md` — Endüstriyel uygulama rehberi
- `worked_examples/boiler_optimization.md` — Kazan optimizasyon örneği
- `factory/prioritization.md` — Yatırım önceliklendirme

## Referanslar

- Tsatsaronis, G. & Pisa, J. (1994). "Exergoeconomic evaluation and optimization of energy systems." *Energy*, 19(3), 287-321.
- Tsatsaronis, G. (2008). "Recent developments in exergy analysis and exergoeconomics." *International Journal of Exergy*, 5(5-6), 489-499.
- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Lazzaretto, A. & Tsatsaronis, G. (2006). "SPECO." *Energy*, 31(8-9), 1257-1289.
