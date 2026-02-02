---
title: "Yakıt ve Ürün Tanımları (Fuel & Product Definitions)"
category: factory
equipment_type: factory
keywords: [yakıt, ürün, F/P, SPECO, dissipative, kompresör, türbin, kazan, pompa, chiller]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/exergoeconomic/auxiliary_equations.md
  - factory/exergoeconomic/overview.md
use_when:
  - "Bileşen Yakıt/Ürün tanımları yapılırken"
  - "SPECO F/P kuralları uygulanırken"
  - "Dissipative bileşenler ele alınırken"
  - "Yardımcı denklem gereksinimleri belirlenirken"
priority: high
last_updated: 2026-02-01
---
# Yakıt ve Ürün Tanımları (Fuel & Product Definitions)

> Son güncelleme: 2026-02-01

## 1. Genel İlkeler

SPECO metodunda her bileşenin Yakıt (F) ve Ürün (P) exergy'si, bileşenin termodinamik amacına göre tanımlanır. Doğru F/P tanımı, exergoekonomik analizin tutarlılığı için kritiktir.

### 1.1 Temel Kurallar

```
Kural 1 — Ürün (P):
  Bileşenin amacına uygun exergy artışı → Ürün
  Exergy artışı = Ė_çıkış - Ė_giriş (pozitif fark, amaç doğrultusunda)

Kural 2 — Yakıt (F):
  Ürün elde etmek için harcanan exergy azalışı → Yakıt
  Exergy azalışı = Ė_giriş - Ė_çıkış (pozitif fark, harcanan kaynak)

Kural 3 — İş ve Isı Transferi:
  Bileşene giren iş → Yakıt
  Bileşenden çıkan iş → Ürün
  Isı transferi → Ė_Q = Q̇ · (1 - T₀/T)
```

### 1.2 Exergy Bileşenlerinin Ayrımı

Toplam exergy fiziksel ve kimyasal bileşenlerden oluşur. Bazı ekipmanlarda bu ayrım önemlidir:

```
Ė = Ė_PH + Ė_CH

Fiziksel exergy ayrımı (opsiyonel, ileri analiz):
Ė_PH = Ė_T + Ė_P  (termal + mekanik)

Burada:
- Ė_T = Termal exergy (sıcaklık kaynaklı)
- Ė_P = Mekanik exergy (basınç kaynaklı)
- Ė_CH = Kimyasal exergy (bileşim kaynaklı)
```

## 2. Üretken Bileşenler (Productive Components)

### 2.1 Kompresör (Compressor)

```
Amaç: Gazı basınçlandırmak (mekanik exergy artışı)

Yakıt: Ė_F = Ẇ_C (elektrik veya şaft işi)
Ürün: Ė_P = Ė_çıkış - Ė_giriş

┌───────────┐
Ẇ_C ──→│  KOMPRESÖR │──→ Ė_çıkış
Ė_giriş ──→│           │
└───────────┘

Maliyet dengesi:
c_çıkış · Ė_çıkış = c_giriş · Ė_giriş + c_Ẇ · Ẇ_C + Ż_C

Yardımcı denklem: Yok (tek giriş yakıt, tek çıkış ürün)
  → Giriş havası c_giriş = 0 ise, 0 bilinmeyen kalır

Exergy yıkımı:
Ė_D = Ẇ_C - (Ė_çıkış - Ė_giriş)

Tipik ε: %75-90

İleri analiz (termal/mekanik ayrımı):
  Yakıt: Ẇ_C
  Ürün: (Ė_P,çıkış - Ė_P,giriş) + (Ė_T,çıkış - Ė_T,giriş)
  Not: Termal exergy artışı genellikle istenmez → "Exergy atığı" olarak değerlendirilebilir
```

### 2.2 Türbin (Turbine)

```
Amaç: Akışkan exergy'sini iş olarak üretmek

Yakıt: Ė_F = Ė_giriş - Ė_çıkış
Ürün: Ė_P = Ẇ_T

┌─────────┐
Ė_giriş ──→│  TÜRBİN  │──→ Ẇ_T (iş çıkışı)
│         │──→ Ė_çıkış
└─────────┘

Maliyet dengesi:
c_Ẇ · Ẇ_T + c_çıkış · Ė_çıkış = c_giriş · Ė_giriş + Ż_T

Yardımcı denklem (F-kuralı):
c_giriş = c_çıkış
(Yakıt: exergy farkı → giriş ve çıkış birim maliyeti eşit)

Exergy yıkımı:
Ė_D = (Ė_giriş - Ė_çıkış) - Ẇ_T

Tipik ε: %85-95
```

### 2.3 Kazan (Boiler)

```
Amaç: Yakıt kimyasal exergy'sini buhar/sıcak su exergy'sine dönüştürmek

Yakıt: Ė_F = Ė_yakıt (kimyasal exergy)
Ürün: Ė_P = Ė_buhar,çıkış - Ė_su,giriş

┌─────────┐
Ė_yakıt ──→│  KAZAN   │──→ Ė_buhar,çıkış
Ė_su,giriş ──→│         │──→ Ė_baca_gazı
Ė_hava ──→│         │
└─────────┘

Maliyet dengesi:
c_buhar · Ė_buhar + c_baca · Ė_baca = c_yakıt · Ė_yakıt + c_su · Ė_su + c_hava · Ė_hava + Ż_B

Basitleştirilmiş (c_hava ≈ 0):
c_buhar · Ė_buhar = c_yakıt · Ė_yakıt + c_su · Ė_su + Ż_B
(Baca gazı atık → c_baca = 0 veya F-kuralı ile)

Yardımcı denklem:
  Baca gazı varsa F-kuralı: c_baca = c_yakıt (yakıt exergy'sinin birim maliyeti)
  veya baca gazı atık ise: Ċ_baca = 0

Exergy yıkımı:
Ė_D = Ė_yakıt + Ė_hava + Ė_su - Ė_buhar - Ė_baca

Tipik ε: %25-50 (yüksek sıcaklık farkından dolayı)
```

### 2.4 Isı Değiştirici (Heat Exchanger — HX)

```
Amaç: Sıcak akışkandan soğuk akışkana exergy transferi

Yakıt: Ė_F = Ė_sıcak,giriş - Ė_sıcak,çıkış
Ürün: Ė_P = Ė_soğuk,çıkış - Ė_soğuk,giriş

┌──────────────┐
Ė_sıcak,giriş ──→│  ISI DEĞİŞTİRİCİ │──→ Ė_sıcak,çıkış
Ė_soğuk,giriş ──→│                  │──→ Ė_soğuk,çıkış
└──────────────┘

Maliyet dengesi:
c_sç · Ė_sç + c_ss · Ė_ss = c_sg · Ė_sg + c_sg · Ė_sg + Ż_HX
(sç: sıcak çıkış, ss: soğuk çıkış, sg: sıcak giriş, sg: soğuk giriş)

Yardımcı denklem (F-kuralı):
c_sıcak,giriş = c_sıcak,çıkış
(Yakıt: sıcak taraf exergy farkı → birim maliyet eşit)

Exergy yıkımı:
Ė_D = (Ė_sıcak,giriş - Ė_sıcak,çıkış) - (Ė_soğuk,çıkış - Ė_soğuk,giriş)

Tipik ε: %60-90 (sıcaklık farkına bağlı)
```

### 2.5 Pompa (Pump)

```
Amaç: Sıvıyı basınçlandırmak (mekanik exergy artışı)

Yakıt: Ė_F = Ẇ_P (elektrik veya şaft işi)
Ürün: Ė_P = Ė_çıkış - Ė_giriş

┌────────┐
Ẇ_P ──→│  POMPA  │──→ Ė_çıkış
Ė_giriş ──→│        │
└────────┘

Maliyet dengesi:
c_çıkış · Ė_çıkış = c_giriş · Ė_giriş + c_Ẇ · Ẇ_P + Ż_P

Yardımcı denklem: Yok (basit bileşen, tek bilinmeyen)

Exergy yıkımı:
Ė_D = Ẇ_P - (Ė_çıkış - Ė_giriş)

Tipik ε: %30-75 (küçük exergy artışı, mekanik kayıplar)
```

### 2.6 Chiller (Soğutma Makinesi)

```
Amaç: Düşük sıcaklık ortamından ısı çekmek (soğutma etkisi)

Yakıt: Ė_F = Ẇ_kompresör (elektrik işi)
Ürün: Ė_P = Ė_soğuk_su,giriş - Ė_soğuk_su,çıkış

DİKKAT: Chiller'da ürün exergy'si T < T₀ olduğunda
soğuk su çıkışı daha düşük sıcaklıkta → exergy ARTAR
(Referans ortamdan uzaklaşma → exergy artışı)

Düzeltilmiş F/P (T_soğuk < T₀):
Ürün: Ė_P = Ė_soğuk,çıkış - Ė_soğuk,giriş (çıkış > giriş, çünkü T₀'dan uzaklaşma)

┌──────────┐
Ẇ ──→│  CHİLLER  │──→ Ė_soğuk,çıkış (T < T₀)
Ė_soğuk,giriş ──→│          │──→ Ė_kondenser (atık ısı)
└──────────┘

Maliyet dengesi:
c_ss_çıkış · Ė_ss_çıkış + c_kond · Ė_kond = c_Ẇ · Ẇ + c_ss_giriş · Ė_ss_giriş + Ż_ch

Yardımcı denklem: Kondenser atık ise Ċ_kond = 0

Tipik ε: %15-40 (düşük sıcaklık exergy'si küçüktür)
```

### 2.7 Karıştırıcı (Mixer)

```
Amaç: İki veya daha fazla akışı birleştirmek

Yakıt: Ė_F = Σ Ė_giriş - Ė_çıkış (exergy azalışı)
Ürün: — (genellikle dissipative olarak ele alınır)

Alternatif tanım (akışlar farklı maliyetliyse):
Yakıt: En pahalı akışın exergy artışı
Ürün: Ucuz akışın exergy artışı

┌──────────┐
Ė₁ ──→│  KARIŞTIRICI │──→ Ė_çıkış
Ė₂ ──→│             │
└──────────┘

Maliyet dengesi:
c_çıkış · Ė_çıkış = c₁ · Ė₁ + c₂ · Ė₂ + Ż_mixer

Yardımcı denklem: Yok (tek çıkış, denklem yeterli)

Exergy yıkımı:
Ė_D = Ė₁ + Ė₂ - Ė_çıkış ≥ 0

Not: Farklı sıcaklık/basınçtaki akışların karışması her zaman exergy yıkımına neden olur
```

### 2.8 Ayırıcı (Splitter)

```
Amaç: Tek akışı ikiye (veya daha fazlaya) ayırmak

┌──────────┐
Ė_giriş ──→│  AYIRICI   │──→ Ė_çıkış₁
│          │──→ Ė_çıkış₂
└──────────┘

İdeal ayırma (aynı koşullar): Ė_D = 0
Gerçek ayırma: Küçük basınç düşüşü → Ė_D > 0

Maliyet dengesi:
c₁ · Ė₁ + c₂ · Ė₂ = c_giriş · Ė_giriş + Ż_splitter

Yardımcı denklem (P-kuralı):
c₁ = c₂ = c_giriş
(İdeal ayırma: tüm çıkışlar aynı birim maliyete sahip)

Not: Ż_splitter ≈ 0 (genellikle ihmal edilir)
```

### 2.9 Kısma Valfi (Throttling Valve)

```
Amaç: Basınç düşürme (genellikle istenmeyen, dissipative)

┌─────────┐
Ė_giriş ──→│  VALF    │──→ Ė_çıkış
└─────────┘

Yakıt: Ė_giriş - Ė_çıkış
Ürün: — (dissipative, doğrudan ürün yok)

SPECO Yaklaşımı:
  Seçenek A: Valfi servis ettiği bileşene dahil et
    → Valf + bileşen birlikte değerlendirilir
  Seçenek B: Exergy yıkımını bitişik bileşenlere dağıt
    → Ė_D,valf → komşu bileşenlerin Ė_D'sine eklenir
  Seçenek C: Ayrı tut, nominal F/P ata
    → Maliyet dengesi: c_çıkış · Ė_çıkış = c_giriş · Ė_giriş + Ż_valf
    → F-kuralı: c_giriş = c_çıkış (birim maliyet korunur)

Exergy yıkımı:
Ė_D = Ė_giriş - Ė_çıkış (izoentalpik süreç, h_giriş = h_çıkış)

Tipik Ė_D: Önemli olabilir (özellikle buhar sistemlerinde)
```

### 2.10 Kojenerasyon Türbini (CHP Turbine)

```
Amaç: Hem elektrik hem ısı (buhar) üretmek

Yakıt: Ė_F = Ė_giriş - Ė_çıkış₁ - Ė_çıkış₂
  (veya basitleştirilmiş: Ė_giriş - Σ Ė_çıkış)

Ürün: Ė_P = Ẇ_T + (Ė_ara_çekim - Ė_referans)
  Ẇ_T: Üretilen elektrik
  Ara çekim: Proses buharı (ısı ürünü)

┌──────────────┐
Ė_giriş ──→│  CHP TÜRBİN  │──→ Ẇ_T (elektrik)
│              │──→ Ė_ara_çekim (proses buharı)
│              │──→ Ė_çıkış (düşük basınç)
└──────────────┘

Maliyet dengesi:
c_Ẇ · Ẇ_T + c_ara · Ė_ara + c_çıkış · Ė_çıkış = c_giriş · Ė_giriş + Ż_CHP

Yardımcı denklemler:
  F-kuralı: c_giriş = c_çıkış (yakıt tarafı)
  P-kuralı: c_Ẇ = (c_ara · Ė_ara - c_ref · Ė_ref) / (Ė_ara - Ė_ref)
  → Elektrik ve ısı ürününe eşit birim maliyet atanır

Not: CHP'de F/P tanımı en karmaşık ekipmanlardan biridir.
     Detaylı örnek için: worked_examples/cogeneration.md
```

## 3. Dissipative Bileşenler — Detaylı Ele Alış

### 3.1 Dissipative Bileşen Nedir?

Dissipative bileşenler, termodinamik olarak zorunlu olan ancak doğrudan bir ürün tanımlanamayan bileşenlerdir.

```
Yaygın Dissipative Bileşenler:
├── Kondenser (soğutma sistemi)
├── Kısma valfi
├── Soğutma kulesi
├── Ejektör (bazı uygulamalarda)
└── Karıştırıcı (bazı konfigürasyonlarda)
```

### 3.2 Kondenser — Özel Durum

```
Kondenser (Rankine çevrimi):
  Amaç: Buharı yoğuşturarak çevrimi tamamlamak
  Exergy giriş: Ė_buhar (türbin çıkışı)
  Exergy çıkış: Ė_sıvı (pompa girişi) + Ė_soğutma_suyu_çıkış
  Ė_D = Ė_buhar - Ė_sıvı - Ė_soğutma_değişimi

SPECO Yaklaşımları:

Yöntem A — Kazan ile birleştirme:
  Kazan + Kondenser → Birleşik bileşen
  F: Ė_yakıt
  P: Ė_buhar,çıkış - Ė_su,giriş (değişmez)
  → Kondenserin Ė_D'si kazana eklenir

Yöntem B — Exergy yıkımını dağıtma:
  Ė_D,kondenser → %X kazan, %Y türbin (orantılı)
  → Her bileşenin Ė_D'si artar
  → Yeni ε_k ve Ċ_D,k hesaplanır

Yöntem C — Bağımsız bileşen:
  F: Ė_buhar,giriş - Ė_sıvı,çıkış
  P: Yok (Ė_P = 0)
  → c_P tanımsız, sadece Ċ_D hesaplanır
  → f_k ve r_k hesaplanamaz

Önerilen: Yöntem A (basit sistemlerde) veya Yöntem B (karmaşık sistemlerde)
```

### 3.3 Dissipative Bileşen Karar Ağacı

```
Dissipative bileşen mi?
│
├─ Evet → Servis ettiği bileşen(ler) belirli mi?
│   │
│   ├─ Evet → Birleştirebilir misin?
│   │   │
│   │   ├─ Evet → Yöntem A (birleştir)
│   │   │
│   │   └─ Hayır → Yöntem B (Ė_D dağıt)
│   │
│   └─ Hayır → Yöntem C (bağımsız, sadece Ċ_D)
│
└─ Hayır → Üretken bileşen, standart F/P tanımı uygula
```

## 4. F/P Tanımları Özet Tablosu

| Bileşen | Ė_F (Yakıt) | Ė_P (Ürün) | Yardımcı Denklem | Tipi |
|---------|-------------|-------------|-------------------|------|
| Kompresör | Ẇ_C | Ė_çıkış - Ė_giriş | — | Üretken |
| Türbin | Ė_giriş - Ė_çıkış | Ẇ_T | F: c_in = c_out | Üretken |
| Kazan | Ė_yakıt | Ė_buhar - Ė_su | F: c_baca = c_yakıt | Üretken |
| Isı değiştirici | Ė_sıcak,in - Ė_sıcak,out | Ė_soğuk,out - Ė_soğuk,in | F: c_sıcak,in = c_sıcak,out | Üretken |
| Pompa | Ẇ_P | Ė_çıkış - Ė_giriş | — | Üretken |
| Chiller | Ẇ_ch | Ė_soğuk,out - Ė_soğuk,in | — | Üretken |
| Karıştırıcı | Σ Ė_in - Ė_out | — | — | Dissipative* |
| Ayırıcı | Ė_in | Σ Ė_out | P: c₁ = c₂ | Üretken |
| Kısma valfi | Ė_in - Ė_out | — | c_in = c_out | Dissipative |
| CHP Türbin | Ė_in - Σ Ė_out | Ẇ_T + (Ė_ara - Ė_ref) | F + P kuralları | Üretken |

> *Karıştırıcı duruma göre üretken veya dissipative olabilir

## 5. Denklem Sayısı Hesaplama Rehberi

### 5.1 Genel Formül

```
n_bilinmeyen = n_akış + n_iş_akışı  (her akış için bir c değeri)
n_denklem = n_bileşen  (her bileşen için bir maliyet dengesi)
n_sınır = verilen c değerleri  (yakıt fiyatı, çevre akışları)
n_yardımcı = n_bilinmeyen - n_denklem - n_sınır

Kontrol: n_yardımcı ≥ 0 → Çözülebilir
         n_yardımcı < 0 → Fazla belirlenmiş (tutarsızlık kontrol et)
```

### 5.2 Pratik Kılavuz

```
Her bileşen türü için gerekli yardımcı denklem sayısı:

Kompresör:     0 (tek giriş yakıt: Ẇ; tek çıkış: gaz)
Türbin:        1 (F-kuralı: c_in = c_out)
Kazan:         1 (F-kuralı: c_baca = c_yakıt veya baca atık)
Isı değiştirici: 1 (F-kuralı: c_sıcak,in = c_sıcak,out)
Pompa:         0 (tek giriş yakıt: Ẇ; tek çıkış: sıvı)
Chiller:       0 veya 1 (kondenser atık → +0; değilse → +1)
Karıştırıcı:   0 (tek çıkış)
Ayırıcı:       n_çıkış - 1 (P-kuralı)
CHP Türbin:    2+ (F-kuralı + P-kuralı)
```

## 6. Özel Durumlar ve İpuçları

### 6.1 Negatif Exergy Farkı

```
Sorun: Ė_çıkış - Ė_giriş < 0 olduğunda

Durum: Isı değiştiricinin soğuk tarafında sıcaklık T₀'ın altına düşüyorsa
  → Exergy artışı değil, azalışı olur
  → F/P tanımı tersine çevrilmeli

Çözüm:
  |Ė_fark| kullanılır veya termal/mekanik exergy ayrımı yapılır
```

### 6.2 Çok Ürünlü Bileşenler

```
Bir bileşenin birden fazla ürünü varsa P-kuralı uygulanır:
  → Her ürünün birim exergy maliyeti eşit atanır

Örnek: CHP türbini
  Ürün 1: Ẇ_T (elektrik)
  Ürün 2: Ė_buhar - Ė_ref (ısı)
  P-kuralı: c_Ẇ = (Ċ_buhar - Ċ_ref)/(Ė_buhar - Ė_ref)
```

### 6.3 Çok Yakıtlı Bileşenler

```
Bir bileşenin birden fazla yakıtı varsa F-kuralı uygulanır:
  → Her yakıtın birim exergy maliyeti eşit atanır

Örnek: Isı değiştirici (iki sıcak akış)
  Yakıt 1: Ė_sıcak1,in - Ė_sıcak1,out
  Yakıt 2: Ė_sıcak2,in - Ė_sıcak2,out
  F-kuralı: c_sıcak1,in = c_sıcak1,out = c_sıcak2,in = c_sıcak2,out
```

## 7. ExergyLab Ekipman Tipleri için F/P Özeti

ExergyLab platformundaki dört ana ekipman tipi:

| Ekipman | ExergyLab Tipi | Ė_F | Ė_P | ε Tipik |
|---------|----------------|-----|-----|---------|
| Kompresör | `compressor` | Ẇ_C | Ė_out - Ė_in | %75-90 |
| Kazan | `boiler` | Ė_fuel (CH) | Ė_steam - Ė_water | %25-50 |
| Chiller | `chiller` | Ẇ_ch | Ė_cold,out - Ė_cold,in | %15-40 |
| Pompa | `pump` | Ẇ_P | Ė_out - Ė_in | %30-75 |

## İlgili Dosyalar

- `factory/exergoeconomic/speco_method.md` — SPECO adımları detayı
- `factory/exergoeconomic/exergoeconomic_balance.md` — Maliyet denge denklemleri
- `factory/exergoeconomic/auxiliary_equations.md` — F-kuralı, P-kuralı detayları
- `factory/exergoeconomic/worked_examples/industrial_plant.md` — ExergyLab ekipmanları ile tam örnek

## Referanslar

1. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs in thermal systems." *Energy*, 31(8-9), 1257-1289.
2. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Bölüm 8: Thermoeconomic analysis.
3. Tsatsaronis, G., Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
4. Kelly, S., Tsatsaronis, G., Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391.
