---
title: "Exergoekonomik Değerlendirme Kriterleri (Evaluation Criteria — Ċ_D, f_k, r_k)"
category: factory
equipment_type: factory
keywords: [exergoekonomik faktör, göreli maliyet farkı, exergy yıkım maliyeti, f_k, r_k, C_D_dot]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/exergoeconomic/advanced_exergoeconomic.md
  - factory/exergoeconomic/optimization.md
  - factory/exergoeconomic/overview.md
use_when:
  - "Exergoekonomik analiz sonuçları yorumlanırken"
  - "Bileşen iyileştirme öncelikleri belirlenirken"
  - "f_k ve r_k eşik değerleri değerlendirilirken"
  - "Ċ_D sıralaması yapılırken"
priority: high
last_updated: 2026-02-01
---
# Exergoekonomik Değerlendirme Kriterleri (Evaluation Criteria)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Exergoekonomik değerlendirme üç temel gösterge üzerinden yapılır:

```
1. Ċ_D,k — Exergy yıkım maliyet akışı [€/saat]
   → "Bu bileşen saat başına ne kadar para kaybettiriyor?"

2. f_k — Exergoekonomik faktör [-]
   → "Kaybın sebebi yüksek yatırım mı, yoksa düşük verimlilik mi?"

3. r_k — Göreli maliyet farkı [-]
   → "Bu bileşende ne kadar iyileştirme potansiyeli var?"

Bu üç gösterge birlikte değerlendirildiğinde:
→ Hangi bileşene öncelik verilmeli?
→ Ne tür bir iyileştirme yapılmalı?
→ Yatırım artırılmalı mı, azaltılmalı mı?
```

## 2. Exergy Yıkım Maliyet Akışı (Ċ_D,k)

### 2.1 Tanım ve Formül

```
Ċ_D,k = c_F,k · Ė_D,k  [€/saat]

Burada:
- c_F,k = k. bileşenin yakıt exergy'si birim maliyeti [€/kJ]
- Ė_D,k = k. bileşendeki exergy yıkım hızı [kW]

Yıllık exergy yıkım maliyeti:
Ċ_D,k,yıllık = Ċ_D,k × τ  [€/yıl]
  (τ = yıllık çalışma saati)

Alternatif formülasyon:
Ċ_D,k = c_F,k · Ė_F,k · (1 - ε_k)
  (ε_k = exergy verimi)
```

### 2.2 Yorumlama

```
Ċ_D,k, k. bileşendeki termodinamik verimsizliğin parasal karşılığıdır.

Sıralama: Ċ_D değerleri azalan sırada sıralanır
  → En yüksek Ċ_D olan bileşen, en fazla "para kaybettiren" bileşendir
  → İyileştirme önceliği için birincil gösterge

Dikkat:
  Yüksek Ċ_D ≠ Mutlaka iyileştirme yapılmalı
  → f_k ve r_k ile birlikte değerlendirilmeli
  → Bazı yıkımlar kaçınılmazdır (unavoidable)
```

### 2.3 Exergy Kaybı Maliyet Akışı (Ċ_L,k)

```
Ċ_L,k = c_F,k · Ė_L,k  [€/saat]

Burada:
- Ė_L,k = Sistem dışına çıkan exergy kaybı [kW]
  (baca gazı, soğutma suyu atığı vb.)

Not: Ė_L sistemden çıkar, Ė_D sistem içinde yok olur.
  Ċ_L genellikle Ċ_D'den daha küçüktür ancak ihmal edilmemelidir.

Toplam maliyet etkisi:
Ċ_D,k + Ċ_L,k = Toplam termodinamik verimsizlik maliyeti
```

## 3. Exergoekonomik Faktör (f_k)

### 3.1 Tanım ve Formül

```
f_k = Ż_k / (Ż_k + Ċ_D,k + Ċ_L,k)

Basitleştirilmiş (Ė_L ihmal edilirse):
f_k = Ż_k / (Ż_k + Ċ_D,k)

Burada:
- Ż_k = k. bileşenin seviyelendirilmiş saatlik maliyeti [€/saat]
- Ċ_D,k = Exergy yıkım maliyet akışı [€/saat]
- Ċ_L,k = Exergy kaybı maliyet akışı [€/saat]

f_k ∈ [0, 1]
```

### 3.2 Yorumlama ve Karar Eşikleri

```
┌─────────────────────────────────────────────────────────────────────┐
│ f_k < 0.25 — Exergy Yıkımı Baskın                                 │
│                                                                     │
│ Durum: Ċ_D >> Ż                                                    │
│ Anlam: Bileşen ucuz ama verimsiz                                   │
│ Aksiyon:                                                            │
│   → Termodinamik verimlilik artırılmalı                            │
│   → Daha verimli (ve muhtemelen daha pahalı) ekipman düşünülmeli   │
│   → Proses parametreleri optimize edilmeli                         │
│                                                                     │
│ Örnek: Basit kazan, f_k = 0.12                                    │
│   → Yanma verimi artırılmalı (ekonomizer, hava ön ısıtıcı)        │
│   → Buhar parametreleri optimize edilmeli                          │
├─────────────────────────────────────────────────────────────────────┤
│ 0.25 ≤ f_k ≤ 0.70 — Dengeli Bölge                                │
│                                                                     │
│ Durum: Ż ve Ċ_D benzer büyüklükte                                 │
│ Anlam: Yatırım ve verimlilik dengesi yakın                         │
│ Aksiyon:                                                            │
│   → Optimizasyon ile ince ayar yapılabilir                         │
│   → r_k değerine bakarak yön belirle                              │
│   → Hem verimlilik hem maliyet düşürme fırsatı değerlendir        │
│                                                                     │
│ Örnek: VSD'li kompresör, f_k = 0.55                               │
│   → Mevcut tasarım makul                                          │
│   → Çalışma noktası optimizasyonu yapılabilir                     │
├─────────────────────────────────────────────────────────────────────┤
│ f_k > 0.70 — Yatırım Maliyeti Baskın                              │
│                                                                     │
│ Durum: Ż >> Ċ_D                                                    │
│ Anlam: Bileşen verimli ama çok pahalı                              │
│ Aksiyon:                                                            │
│   → Daha ucuz bileşen veya malzeme düşünülmeli                    │
│   → Kapasite azaltma (right-sizing) değerlendirilmeli             │
│   → Verimlilikten küçük ödün vererek maliyet düşürülebilir        │
│                                                                     │
│ Örnek: Titanyum HX, f_k = 0.85                                    │
│   → Paslanmaz çelik alternatifi değerlendirilmeli                 │
│   → Daha küçük alan ile tasarım düşünülmeli                       │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.3 Ekipman Türüne Göre Tipik f_k Değerleri

| Ekipman | Tipik f_k | Aralık | Not |
|---------|-----------|--------|-----|
| Kompresör | 0.40-0.65 | 0.25-0.80 | VSD'li daha yüksek |
| Türbin (buhar) | 0.60-0.85 | 0.45-0.95 | Yüksek PEC → yüksek f_k |
| Türbin (gaz) | 0.55-0.80 | 0.40-0.90 | Hot section maliyeti |
| Kazan | 0.10-0.30 | 0.05-0.45 | Düşük ε → düşük f_k |
| Isı değiştirici | 0.35-0.65 | 0.15-0.85 | Malzemeye bağlı |
| Pompa | 0.35-0.55 | 0.20-0.75 | Küçük ekipman |
| Chiller | 0.30-0.55 | 0.15-0.70 | Düşük exergy ürünü |
| Kondenser | 0.15-0.35 | 0.05-0.50 | Dissipative |
| Yanma odası | 0.05-0.20 | 0.02-0.30 | Büyük Ė_D |
| Ekonomizer | 0.40-0.70 | 0.25-0.85 | Sıcaklık farkına bağlı |

## 4. Göreli Maliyet Farkı (r_k)

### 4.1 Tanım ve Formül

```
r_k = (c_P,k - c_F,k) / c_F,k

Burada:
- c_P,k = k. bileşenin ürün exergy'si birim maliyeti [€/kJ]
- c_F,k = k. bileşenin yakıt exergy'si birim maliyeti [€/kJ]

Alternatif formülasyon:
r_k = (1 - ε_k) / ε_k + Ż_k / (c_F,k · Ė_P,k)

r_k ≥ 0 (her zaman pozitif)
```

### 4.2 Bileşenler

```
r_k = r_k,termodinamik + r_k,ekonomik

r_k,termodinamik = (1 - ε_k) / ε_k
  → Exergy yıkımından kaynaklanan maliyet artışı

r_k,ekonomik = Ż_k / (c_F,k · Ė_P,k)
  → Yatırım maliyetinden kaynaklanan maliyet artışı

Yorum:
  r_k yüksek → Ürün maliyeti yakıt maliyetine göre çok artıyor
  r_k düşük → Verimli maliyet dönüşümü
```

### 4.3 Yorumlama

```
r_k Yorumlama Rehberi:

r_k < 0.5:
  → Bileşen maliyet-etkin çalışıyor
  → İyileştirme potansiyeli düşük
  → Öncelik sıralamasında alt sıralarda

0.5 ≤ r_k ≤ 2.0:
  → Orta düzeyde iyileştirme potansiyeli
  → f_k ile birlikte değerlendir
  → Ċ_D + Ż azaltma hedeflenebilir

r_k > 2.0:
  → Yüksek iyileştirme potansiyeli
  → Acil dikkat gerektirir
  → Bileşen tasarımı veya çalışma koşulları gözden geçirilmeli

r_k > 5.0:
  → Aşırı yüksek — tasarım hatası veya uyumsuzluk olabilir
  → Bileşen yeniden boyutlandırılmalı
```

### 4.4 Ekipman Türüne Göre Tipik r_k Değerleri

| Ekipman | Tipik r_k | Aralık | Not |
|---------|-----------|--------|-----|
| Kompresör | 0.30-0.80 | 0.15-1.50 | Exergy verimi yüksekse düşük |
| Türbin (buhar) | 0.20-0.60 | 0.10-1.00 | Yüksek ε → düşük r_k |
| Türbin (gaz) | 0.25-0.70 | 0.15-1.20 | — |
| Kazan | 1.50-4.00 | 0.80-8.00 | Düşük ε → yüksek r_k |
| Isı değiştirici | 0.30-1.50 | 0.10-3.00 | ΔT'ye bağlı |
| Pompa | 1.00-5.00 | 0.50-15.00 | Küçük Ė_P → yüksek r_k |
| Chiller | 1.50-5.00 | 0.80-10.00 | Düşük exergy ürünü |
| Yanma odası | 0.30-0.80 | 0.15-1.50 | Yüksek Ė_D ama düşük Ż |

## 5. Birleşik Değerlendirme: f_k vs r_k Karar Matrisi

### 5.1 Dört Kadran Analizi

```
                    r_k düşük              r_k yüksek
                   (< 1.0)                 (> 1.0)
              ┌─────────────────────┬─────────────────────┐
              │                     │                     │
  f_k yüksek │  KADRAN I           │  KADRAN II          │
  (> 0.50)   │  "Pahalı ama verimli"│  "Pahalı ve         │
              │  → Daha ucuz bileşen │   verimsiz"         │
              │  → Kapasite azaltma  │  → Maliyet azalt    │
              │  → Düşük öncelik     │  → Verimlilik artır │
              │                     │  → YÜK. ÖNCELİK    │
              ├─────────────────────┼─────────────────────┤
              │                     │                     │
  f_k düşük  │  KADRAN III         │  KADRAN IV          │
  (< 0.50)   │  "Ucuz ve verimli"  │  "Ucuz ama verimsiz"│
              │  → İYİ DURUM        │  → Verimlilik artır │
              │  → Optimizasyon     │  → Daha iyi ekipman │
              │    potansiyeli az   │  → ORTA ÖNCELİK    │
              │  → EN DÜŞÜK         │                     │
              │    ÖNCELİK          │                     │
              └─────────────────────┴─────────────────────┘
```

### 5.2 Karar Akış Diyagramı

```
Başla: Bileşen k analiz ediliyor
│
├── Adım 1: Ċ_D,k + Ż_k hesapla → Toplam maliyet etkisi
│
├── Adım 2: Tüm bileşenleri Ċ_D+Ż'ye göre sırala
│   → En yüksek 3 bileşene odaklan
│
├── Adım 3: f_k kontrol et
│   │
│   ├── f_k < 0.25 → Verimlilik İyileştirmesi
│   │   ├── Daha verimli ekipman seç
│   │   ├── Proses parametrelerini optimize et
│   │   └── Isı geri kazanımı ekle
│   │
│   ├── 0.25 ≤ f_k ≤ 0.70 → Dengeleme
│   │   ├── r_k kontrol et
│   │   │   ├── r_k > 2 → Hem verimlilik hem maliyet iyileştir
│   │   │   └── r_k < 2 → İnce ayar (fine-tuning) yeterli
│   │   └── Çalışma koşullarını optimize et
│   │
│   └── f_k > 0.70 → Maliyet Azaltma
│       ├── Daha ucuz malzeme/bileşen
│       ├── Kapasite azaltma
│       └── Verimlilikten küçük ödün kabul edilebilir
│
└── Adım 4: Tavsiye oluştur
    └── Ċ_D+Ż, f_k, r_k birlikte raporla
```

## 6. Beş Bileşenli Değerlendirme Örneği

### 6.1 Sistem Verileri

Fabrika sistemindeki 5 bileşenin exergoekonomik analiz sonuçları:

| Bileşen | Ė_F [kW] | Ė_P [kW] | Ė_D [kW] | ε [%] | Ż [€/h] | c_F [€/GJ] |
|---------|-----------|-----------|-----------|-------|----------|-------------|
| Kazan | 42,000 | 14,740 | 27,260 | 35.1 | 28.50 | 8.0 |
| Kompresör | 150 | 120 | 30 | 80.0 | 3.34 | 25.0 |
| Chiller | 200 | 52 | 148 | 26.0 | 5.20 | 25.0 |
| Pompa | 45 | 32 | 13 | 71.1 | 0.85 | 25.0 |
| HX (Ekonomizer) | 850 | 680 | 170 | 80.0 | 4.10 | 12.0 |

### 6.2 Hesaplamalar

```
Ċ_D hesabı (c_F × Ė_D, birimler: €/GJ × kW = €/GJ × kJ/s):

Kazan:      Ċ_D = 8.0×10⁻⁶ × 27,260 = 0.2181 €/s = 785.1 €/h
Kompresör:  Ċ_D = 25.0×10⁻⁶ × 30 = 0.000750 €/s = 2.70 €/h
Chiller:    Ċ_D = 25.0×10⁻⁶ × 148 = 0.003700 €/s = 13.32 €/h
Pompa:      Ċ_D = 25.0×10⁻⁶ × 13 = 0.000325 €/s = 1.17 €/h
HX:         Ċ_D = 12.0×10⁻⁶ × 170 = 0.002040 €/s = 7.34 €/h
```

### 6.3 Değerlendirme Tablosu

| Bileşen | Ċ_D [€/h] | Ż [€/h] | Ċ_D+Ż [€/h] | f_k | r_k | Kadran |
|---------|------------|----------|--------------|-----|-----|--------|
| Kazan | 785.1 | 28.50 | 813.6 | 0.035 | 1.85 | IV |
| Chiller | 13.32 | 5.20 | 18.52 | 0.281 | 2.85 | IV→II |
| HX | 7.34 | 4.10 | 11.44 | 0.358 | 0.25 | III |
| Kompresör | 2.70 | 3.34 | 6.04 | 0.553 | 0.25 | III→I |
| Pompa | 1.17 | 0.85 | 2.02 | 0.421 | 0.41 | III |

### 6.4 Sıralama ve Öncelikler

```
Ċ_D + Ż Sıralaması (öncelik):
1. Kazan:      813.6 €/h — f_k=0.035 → Verimlilik iyileştirmesi ZORUNLU
2. Chiller:    18.52 €/h — f_k=0.281, r_k=2.85 → Verimlilik iyileştirmesi
3. HX:         11.44 €/h — f_k=0.358, r_k=0.25 → Dengeli, düşük öncelik
4. Kompresör:  6.04 €/h  — f_k=0.553 → Dengeli, maliyet azaltma düşünülebilir
5. Pompa:      2.02 €/h  — f_k=0.421 → Dengeli, en düşük öncelik
```

### 6.5 Yorumlama ve Tavsiyeler

```
Kazan (öncelik: çok yüksek):
  f_k = 0.035 → Exergy yıkımı çok baskın
  r_k = 1.85 → Yüksek iyileştirme potansiyeli
  → Ekonomizer eklenmeli veya genişletilmeli
  → Hava ön ısıtıcı değerlendirilmeli
  → Baca gazı sıcaklığı düşürülmeli
  → Yıllık potansiyel tasarruf: 785.1 × 0.20 × 7500 = 1,177,650 €
     (%20 iyileştirme varsayımı)

Chiller (öncelik: yüksek):
  f_k = 0.281 → Verimlilik iyileştirmesi öncelikli
  r_k = 2.85 → Önemli iyileştirme potansiyeli
  → VSD eklenmeli
  → Kondenser optimizasyonu yapılmalı
  → Soğutma sıcaklığı yükseltilmeli (mümkünse)

HX — Ekonomizer (öncelik: düşük):
  f_k = 0.358 → Dengeli
  r_k = 0.25 → Düşük iyileştirme potansiyeli
  → Mevcut tasarım makul
  → Fouling kontrolü yeterli

Kompresör (öncelik: düşük):
  f_k = 0.553 → Yatırım biraz baskın
  r_k = 0.25 → İyi maliyet dönüşümü
  → Mevcut durumda kalabilir
  → Right-sizing değerlendirilebilir

Pompa (öncelik: en düşük):
  f_k = 0.421 → Dengeli
  r_k = 0.41 → Düşük iyileştirme potansiyeli
  → Müdahale gerekli değil
```

## 7. Ek Değerlendirme Göstergeleri

### 7.1 Ürün Maliyet Akışı Artışı (ΔĊ_k)

```
ΔĊ_k = Ċ_D,k + Ż_k  [€/saat]

Bu gösterge bileşenlerin toplam maliyet etkisini gösterir.
Sıralama için birincil göstergedir.
```

### 7.2 Exergy Yıkım Oranı (y_D,k)

```
y_D,k = Ė_D,k / Ė_F,toplam

Burada:
- Ė_F,toplam = Sisteme giren toplam yakıt exergy'si

y_D,k, k. bileşenin toplam sisteme göre exergy yıkım payını gösterir.
```

### 7.3 Birim Ürün Maliyeti Artışı

```
Δc_k = c_P,k - c_F,k  [€/GJ]

Birim bazlı maliyet artışı. r_k'nin mutlak versiyonu.
Bileşenler arası karşılaştırma için r_k tercih edilir (boyutsuz).
```

## 8. Raporlama Şablonu

### 8.1 Bileşen Değerlendirme Tablosu

```
| Sıra | Bileşen | Ė_D | ε | Ż | Ċ_D | Ċ_D+Ż | f_k | r_k | Öncelik | Aksiyon |
|------|---------|-----|---|---|-----|--------|-----|-----|---------|---------|
| 1 | ... | ... |...|...|...| ... | ... | ... | Yüksek | ... |
| 2 | ... | ... |...|...|...| ... | ... | ... | Orta | ... |
| 3 | ... | ... |...|...|...| ... | ... | ... | Düşük | ... |
```

### 8.2 Özet Metrikleri

```
Raporda yer alması gereken özet bilgiler:

□ Toplam Ċ_D (tüm bileşenler): Σ Ċ_D,k
□ Toplam Ż (tüm bileşenler): Σ Ż_k
□ Sistem f (genel): Σ Ż / (Σ Ż + Σ Ċ_D)
□ Ürün birim maliyeti: c_P,sistem
□ En yüksek Ċ_D olan 3 bileşen
□ En düşük f_k olan 3 bileşen
□ En yüksek r_k olan 3 bileşen
□ Tahmini toplam iyileştirme potansiyeli [€/yıl]
```

## 9. Sık Yapılan Hatalar

| Hata | Doğru Yaklaşım |
|------|-----------------|
| Sadece Ċ_D'ye göre sıralama | Ċ_D + Ż birlikte değerlendirilmeli |
| f_k'yı tek başına yorumlama | f_k + r_k birlikte; Ċ_D+Ż ile öncelik |
| Tüm bileşenleri iyileştirmeye çalışmak | En yüksek Ċ_D+Ż olan 2-3 bileşene odaklan |
| Dissipative bileşenlerde f_k hesaplama | Dissipative bileşenler özel ele alınmalı |
| Kaçınılmaz yıkımı iyileştirmeye çalışmak | AV/UN ayrımı yap (ileri analiz) |
| Farklı birim maliyetleri karşılaştırma | c_F farklı → Ċ_D doğrudan karşılaştırılmaz |

## 10. İleri Değerlendirme: AV/UN ve EN/EX

Standart f_k ve r_k analizi, bileşendeki tüm exergy yıkımının iyileştirilebilir olduğunu varsayar. İleri (advanced) exergoekonomik analiz ile:

```
Ė_D,k = Ė_D,k^AV + Ė_D,k^UN

Ċ_D,k^AV = c_F,k · Ė_D,k^AV  (iyileştirilebilir)
Ċ_D,k^UN = c_F,k · Ė_D,k^UN  (kaçınılmaz)

İleri f_k:
f_k^AV = Ż_k^AV / (Ż_k^AV + Ċ_D,k^AV)

→ Sadece iyileştirilebilir kısma odaklanır
→ Daha gerçekçi önceliklendirme sağlar
```

> Detay için: `advanced_exergoeconomic.md`

## İlgili Dosyalar

- `factory/exergoeconomic/speco_method.md` — SPECO adımları (Adım 4: Değerlendirme)
- `factory/exergoeconomic/advanced_exergoeconomic.md` — İleri AV/UN, EN/EX analizi
- `factory/exergoeconomic/optimization.md` — Ċ_D+Ż minimizasyonu
- `factory/exergoeconomic/exergoeconomic_balance.md` — Maliyet dengesi (c_F, c_P hesabı)
- `factory/exergoeconomic/worked_examples/industrial_plant.md` — Tam değerlendirme örneği

## Referanslar

1. Tsatsaronis, G. (1993). "Thermoeconomic analysis and optimization of energy systems." *Progress in Energy and Combustion Science*, 19(3), 227-257.
2. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
3. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Chapter 8.
4. Tsatsaronis, G., Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions..." *Energy Conversion and Management*, 43(9-12), 1259-1270.
5. Morosuk, T., Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines." *Int. J. Refrigeration*, 32(6), 1193-1202.
