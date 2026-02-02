---
title: "Exergoekonomik Analize Genel Bakış (Exergoeconomic Analysis Overview)"
category: factory
equipment_type: factory
keywords: [exergoekonomik, termoekonomik, SPECO, Tsatsaronis, Bejan, maliyet, exergy]
related_files:
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/fuel_product_definitions.md
  - factory/exergoeconomic/cost_equations.md
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/economic_analysis.md
  - factory/exergy_fundamentals.md
use_when:
  - "Exergoekonomik analiz kavramı açıklanırken"
  - "Geleneksel ekonomik analizle karşılaştırma yapılırken"
  - "Termoekonomik analiz tarihçesi sorulduğunda"
priority: high
last_updated: 2026-02-01
---
# Exergoekonomik Analize Genel Bakış (Exergoeconomic Analysis Overview)

> Son güncelleme: 2026-02-01

## 1. Tanım ve Temel Kavram

Exergoekonomik analiz (exergoeconomic analysis), termodinamiğin ikinci yasası ile maliyet muhasebesini birleştiren bir mühendislik disiplinidir. Geleneksel enerji ekonomisi yalnızca birinci yasa verimini (enerji korunumu) temel alırken, exergoekonomik analiz **exergy yıkımının ekonomik maliyetini** hesaplar.

```
Temel Prensip:

Her exergy yıkımının bir maliyeti vardır → Ċ_D = c_F · Ė_D

Burada:
- Ċ_D = Exergy yıkımının maliyet akışı [€/saat veya $/saat]
- c_F = Yakıt (fuel) exergy'sinin birim maliyeti [€/kJ veya $/kJ]
- Ė_D = Exergy yıkım hızı [kW]
```

Bu yaklaşım sayesinde:
- Her bileşendeki termodinamik verimsizliğin **parasal karşılığı** belirlenir
- Yatırım maliyeti ile exergy yıkım maliyeti arasındaki **denge (trade-off)** analiz edilir
- Optimizasyon için **somut, ölçülebilir** hedefler ortaya konur

## 2. Tarihçe ve Gelişim

### 2.1 Öncü Çalışmalar (1960–1980)

| Yıl | Araştırmacı | Katkı |
|-----|-------------|-------|
| 1962 | Tribus & Evans | "Thermoeconomics" terimini ilk kullananlar; exergy ve maliyet birleştirmesi |
| 1970 | Gaggioli & Petit | Exergy maliyetlendirme ilkeleri, maliyet muhasebesi formülasyonu |
| 1977 | El-Sayed & Evans | Termoekonomik optimizasyon metodolojisi |
| 1980 | Tsatsaronis | "Exergoeconomics" terimini önerdi; sistematik metodoloji |

### 2.2 Metodoloji Olgunlaşması (1980–2000)

| Yıl | Araştırmacı | Katkı |
|-----|-------------|-------|
| 1984 | Frangopoulos | Termoekonomik Fonksiyonel Analiz (TFA) |
| 1987 | von Spakovsky | Mühendislik Fonksiyonel Analizi (EFA) |
| 1993 | Bejan, Tsatsaronis & Moran | "Thermal Design and Optimization" kitabı — referans eser |
| 1994 | Lozano & Valero | Exergetik Maliyet Teorisi (Exergetic Cost Theory — ECT) |
| 1996 | Bejan et al. | Kapsamlı PEC (Purchased Equipment Cost) korelasyonları |

### 2.3 Modern Dönem (2000–günümüz)

| Yıl | Araştırmacı | Katkı |
|-----|-------------|-------|
| 2006 | Lazzaretto & Tsatsaronis | **SPECO metodu** — standart formülasyon yayınlandı |
| 2008 | Tsatsaronis & Park | İleri (advanced) exergoekonomik analiz: AV/UN, EN/EX ayrımı |
| 2012 | Turton et al. | Güncel PEC korelasyonları ve maliyet faktörleri |
| 2013 | Morosuk & Tsatsaronis | İleri exergoekonomik yöntemin kapsamlı uygulaması |
| 2018+ | Çeşitli | Exergoenvironmental analiz, çok amaçlı optimizasyon, makine öğrenme entegrasyonu |

### 2.4 Temel Referans Eserler

1. **Bejan, A., Tsatsaronis, G., Moran, M.** (1996). *Thermal Design and Optimization*. Wiley. — Alan için temel başvuru kitabı
2. **Lazzaretto, A., Tsatsaronis, G.** (2006). "SPECO: A systematic and general methodology for calculating efficiencies and costs in thermal systems." *Energy*, 31(8-9), 1257-1289.
3. **Tsatsaronis, G.** (2008). "Recent developments in exergy analysis and exergoeconomics." *Int. J. Exergy*, 5(5-6), 489-499.
4. **Turton, R., Bailie, R.C., Whiting, W.B., Shaeiwitz, J.A.** (2012). *Analysis, Synthesis, and Design of Chemical Processes*. 4th Ed.

## 3. Neden Exergoekonomik Analiz?

### 3.1 Geleneksel Ekonomik Analizin Sınırları

Geleneksel yatırım değerlendirmesi (NPV, IRR, SPP) aşağıdaki soruları cevaplayamaz:

| Soru | Geleneksel | Exergoekonomik |
|------|------------|----------------|
| Hangi bileşende en çok para kaybediliyor? | ✗ | ✓ — Ċ_D hesabı |
| Yatırım mı yoksa verimlilik mi artırılmalı? | ✗ | ✓ — f_k analizi |
| Optimizasyon potansiyeli ne kadar? | Kısmi | ✓ — r_k analizi |
| Verimsizlik dış etkilerden mi kaynaklanıyor? | ✗ | ✓ — EN/EX analizi |
| Hangi verimsizlik kaçınılmaz? | ✗ | ✓ — AV/UN analizi |

### 3.2 Exergoekonomik Analizin Avantajları

1. **Termodinamik-ekonomik bütünleşme:** Enerji kalitesini (exergy) doğrudan parasal değere çevirir
2. **Bileşen bazlı maliyet takibi:** Her ekipmanın ürettiği ürünün birim maliyetini verir
3. **Rasyonel karar desteği:** Yatırım kararlarını nesnel verilere dayandırır
4. **Gizli kayıpları ortaya çıkarır:** Enerji analizinde görünmeyen termodinamik kayıplar parasal karşılık kazanır
5. **Optimizasyon yönlendirmesi:** f_k ve r_k göstergeleri ile her bileşen için iyileştirme yönünü belirler

### 3.3 Uygulama Alanları

```
Endüstriyel Uygulamalar:
├── Enerji Üretimi
│   ├── Gaz türbin santralleri
│   ├── Kombine çevrim santralleri
│   ├── Kojenerasyon (CHP) sistemleri
│   └── Jeotermal santraller
│
├── Soğutma ve Isıtma
│   ├── Chiller sistemleri
│   ├── Isı pompaları
│   └── Absorpsiyon soğutma
│
├── Endüstriyel Proses
│   ├── Kimya tesisleri
│   ├── Çimento fabrikaları
│   ├── Kağıt hamuru ve kağıt
│   └── Gıda işleme
│
└── Yenilenebilir Enerji
    ├── Güneş enerjisi sistemleri
    ├── Biyokütle tesisleri
    └── Organik Rankine çevrimi (ORC)
```

## 4. Geleneksel Yaklaşımla Karşılaştırma

### 4.1 Enerji Analizi vs Exergy Analizi vs Exergoekonomik Analiz

| Özellik | Enerji Analizi | Exergy Analizi | Exergoekonomik Analiz |
|---------|----------------|----------------|-----------------------|
| Temel yasa | 1. Yasa | 1. + 2. Yasa | 1. + 2. Yasa + Ekonomi |
| Verimlilik | η_enerji | η_exergy (ε) | c_P (birim maliyet) |
| Kayıp ölçümü | Enerji kaybı | Exergy yıkımı | Ċ_D (maliyet akışı) |
| Sonuç birimi | kW, kWh | kW, kWh | €/GJ, €/saat |
| Optimizasyon | Isı geri kazanım | Termodinamik verim | Maliyet minimizasyonu |
| Karar desteği | Düşük | Orta | Yüksek |
| Yatırım rehberliği | Hayır | Kısmi | Evet (f_k, r_k) |

### 4.2 Somut Örnek: Kazan Değerlendirmesi

```
Kazan Verisi:
- Yakıt giriş: 10,000 kW (HHV)
- Buhar çıkış: 8,500 kW (enerji)
- Exergy giriş: 10,400 kW
- Exergy çıkış: 3,800 kW

Enerji Analizi Sonucu:
  η_enerji = 8,500/10,000 = %85 → "İyi performans"

Exergy Analizi Sonucu:
  ε = 3,800/10,400 = %36.5 → "Ciddi exergy yıkımı: 6,600 kW"

Exergoekonomik Analiz Sonucu:
  c_F = 0.008 €/kJ (doğalgaz)
  Ċ_D = 0.008 × 6,600 = 52.8 €/saat = 422,400 €/yıl
  → "Exergy yıkımı yıllık 422,400 € maliyete neden oluyor"
  → f_k = 0.35 → "Verimlilik iyileştirmesi öncelikli"
```

Bu örnekte enerji analizi "iyi performans" derken, exergoekonomik analiz yıllık 422.400 €'luk somut bir iyileştirme potansiyeli ortaya koyar.

## 5. Exergoekonomik Analiz Adımları (Genel Çerçeve)

```
Adım 1: Sistem Tanımlama
├── Bileşenleri tanımla
├── Akış (stream) numaralandırması yap
└── Kontrol hacimleri belirle

Adım 2: Exergy Analizi
├── Her akışın exergy'sini hesapla
├── Her bileşenin Yakıt (F) ve Ürün (P) exergy'sini tanımla
├── Exergy yıkımını (Ė_D) hesapla
└── Exergy verimini (ε_k) hesapla

Adım 3: Ekonomik Analiz
├── Ekipman satın alma maliyetlerini (PEC) belirle
├── Yıllık seviyelendirilmiş maliyeti (Ż) hesapla
│   ├── Sermaye yatırımı (CI) bileşeni
│   └── İşletme-bakım (OM) bileşeni
└── CRF (Capital Recovery Factor) ile yıllıklaştır

Adım 4: Exergoekonomik Denge
├── Her bileşen için maliyet denklemini kur
│   └── Ċ_P,k = Ċ_F,k + Ż_k
├── Yardımcı denklemleri ekle (F-kuralı, P-kuralı)
├── Doğrusal denklem sistemi oluştur
└── Çözerek birim exergy maliyetlerini (c) bul

Adım 5: Değerlendirme
├── Ċ_D,k — Exergy yıkım maliyeti
├── f_k — Exergoekonomik faktör
├── r_k — Göreli maliyet farkı
└── İyileştirme önceliklerini belirle
```

## 6. Temel Formüller Özeti

### 6.1 Exergy Yıkım Maliyeti

```
Ċ_D,k = c_F,k · Ė_D,k  [€/saat]

Burada:
- c_F,k = k. bileşenin yakıt exergy'si birim maliyeti [€/kJ]
- Ė_D,k = k. bileşendeki exergy yıkım hızı [kW]
```

### 6.2 Exergoekonomik Faktör

```
f_k = Ż_k / (Ż_k + Ċ_D,k)

Yorumlama:
- f_k < 0.25 → Termodinamik verimlilik iyileştirmesi gerekli
- 0.25 ≤ f_k ≤ 0.70 → Dengeli bölge (optimizasyon için aday)
- f_k > 0.70 → Yatırım maliyeti baskın, daha ucuz bileşen düşünülmeli
```

### 6.3 Göreli Maliyet Farkı

```
r_k = (c_P,k - c_F,k) / c_F,k

Burada:
- c_P,k = k. bileşenin ürün exergy'si birim maliyeti [€/kJ]
- c_F,k = k. bileşenin yakıt exergy'si birim maliyeti [€/kJ]

Yorumlama:
- r_k düşük → Verimli maliyet dönüşümü
- r_k yüksek → İyileştirme potansiyeli var
```

### 6.4 Toplam Maliyet Minimizasyonu

```
min Ċ_total = Σ (Ċ_D,k + Ż_k)  ∀ bileşen k

→ Bileşen bazında: Ċ_D,k + Ż_k azaltılmalı
→ Trade-off: Yatırım ↑ → Exergy yıkımı ↓ (ve tersi)
```

## 7. ExergyLab Platformunda Kullanım

ExergyLab'ın mevcut exergy analiz altyapısı, exergoekonomik analize zemin hazırlar:

| ExergyLab Çıktısı | Exergoekonomik Girdi |
|--------------------|-----------------------|
| Ė_D (exergy yıkımı) | Ċ_D hesabında kullanılır |
| ε (exergy verimi) | f_k ve r_k hesaplamalarında referans |
| Benchmark değerleri | Hedef verim belirleme |
| Isı geri kazanım potansiyeli | Entegrasyon fırsatı maliyetlendirmesi |
| Yıllık kayıp (€) | Basitleştirilmiş Ċ_D proxy'si |

## 8. Metodoloji Karşılaştırması: SPECO vs ECT vs TFA

| Özellik | SPECO | ECT | TFA |
|---------|-------|-----|-----|
| Geliştirici | Tsatsaronis & Lazzaretto | Valero et al. | Frangopoulos |
| F/P tanımı | Stream bazlı | Propositions (önerme) bazlı | Fonksiyonel ürün bazlı |
| Yardımcı denklemler | F-kuralı, P-kuralı | Maliyet önermeleri | Fonksiyonel denklemler |
| Karmaşıklık | Orta | Yüksek | Yüksek |
| Uygulama kolaylığı | Yüksek | Orta | Düşük |
| Yaygınlık | En yaygın | Akademik | Sınırlı |
| ExergyLab uyumu | ✓ Tercih edilen | — | — |

> **Not:** ExergyLab, SPECO (Specific Exergy Costing) metodunu temel alır. Detaylar için `speco_method.md` dosyasına bakınız.

## 9. Sınırlamalar ve Dikkat Edilecek Noktalar

1. **Veri hassasiyeti:** PEC korelasyonları ±30% belirsizlik içerebilir; duyarlılık analizi gereklidir
2. **Referans ortam etkisi:** Exergy hesaplaması referans çevre koşullarına bağımlıdır (T₀, P₀)
3. **Sabit-hal varsayımı:** Standart analiz kararlı hal (steady-state) varsayar; geçici rejimler ek modelleme gerektirir
4. **Ekonomik parametreler:** Faiz oranı, enflasyon, döviz kuru gibi parametreler zaman ve coğrafyaya bağlıdır
5. **Dissipative bileşenler:** Kısmak valfi, kondenser gibi bileşenler özel F/P tanımı gerektirir

## 10. İleriye Dönük: Exergoenvironmental Analiz

Exergoekonomik analizin doğal uzantısı, çevresel etki değerlendirmesidir:

```
Exergoekonomik:  Ċ_D,k = c_F,k · Ė_D,k  (maliyet etkisi)
Exergoenvironmental: Ḃ_D,k = b_F,k · Ė_D,k  (çevresel etki)

Burada:
- b_F,k = Yakıt exergy'sinin birim çevresel etkisi [mPt/kJ]
- Ḃ_D,k = Exergy yıkımının çevresel etki akışı [mPt/saat]
```

Bu paralel yapı, ekonomik ve çevresel optimizasyonun birlikte değerlendirilmesine olanak tanır (çok amaçlı optimizasyon).

## İlgili Dosyalar

- `factory/exergoeconomic/speco_method.md` — SPECO metodolojisi detayları
- `factory/exergoeconomic/fuel_product_definitions.md` — Yakıt/Ürün tanımları
- `factory/exergoeconomic/evaluation_criteria.md` — Değerlendirme kriterleri (f_k, r_k, Ċ_D)
- `factory/exergoeconomic/cost_equations.md` — Ekipman maliyet korelasyonları
- `factory/economic_analysis.md` — Geleneksel ekonomik analiz yöntemleri
- `factory/exergy_fundamentals.md` — Exergy temel kavramları

## Referanslar

1. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
2. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
3. Tsatsaronis, G. (2008). "Recent developments in exergy analysis and exergoeconomics." *Int. J. Exergy*, 5(5-6), 489-499.
4. Valero, A., Lozano, M.A., Serra, L., Torres, C. (1994). "Application of the exergetic cost theory to the CGAM problem." *Energy*, 19(3), 365-381.
5. Frangopoulos, C.A. (1987). "Thermo-economic functional analysis and optimization." *Energy*, 12(7), 563-571.
6. El-Sayed, Y.M., Evans, R.B. (1970). "Thermoeconomics and the design of heat systems." *ASME J. Eng. Power*, 92(1), 27-35.
