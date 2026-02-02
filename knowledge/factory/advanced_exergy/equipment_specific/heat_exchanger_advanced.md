---
title: "Isı Değiştirici İleri Exergy Analizi (Advanced Exergy Analysis for Heat Exchangers)"
category: "factory/advanced_exergy/equipment_specific"
keywords:
  - ileri exergy analizi (advanced exergy analysis)
  - ısı değiştirici (heat exchanger)
  - kaçınılabilir tersinmezlik (avoidable irreversibility)
  - kaçınılamaz tersinmezlik (unavoidable irreversibility)
  - endojen tersinmezlik (endogenous irreversibility)
  - ekzojen tersinmezlik (exogenous irreversibility)
  - pinch analizi (pinch analysis)
  - atık ısı geri kazanımı (waste heat recovery)
  - Bejan sayısı (Bejan number)
  - logaritmik ortalama sıcaklık farkı (LMTD)
  - shell and tube
  - plakalı ısı değiştirici (plate heat exchanger)
related_files:
  - knowledge/heat_exchanger/formulas.md
  - knowledge/heat_exchanger/benchmarks.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/heat_integration.md
  - knowledge/factory/pinch_analysis.md
  - knowledge/factory/waste_heat_recovery.md
  - knowledge/factory/pinch/grand_composite_curve.md
  - skills/equipment/heat_exchanger_expert.md
  - skills/factory/integration_expert.md
use_when:
  - Isı değiştiricilerde ileri exergy dekompozisyonu gerektiğinde
  - Atık ısı geri kazanım HX performans analizi yapılırken
  - Cross-equipment entegrasyon fırsatları değerlendirilirken
  - HX kaynaklı tersinmezliklerin kök neden analizi yapılırken
  - Pinch analizi ile HX ağı optimizasyonu birleştirilirken
priority: high
last_updated: 2025-05-15
---

# Isı Değiştirici İleri Exergy Analizi (Advanced Exergy Analysis for Heat Exchangers)

## 1. Genel Bakış

Konvansiyonel exergy analizi, bir ısı değiştiricideki (heat exchanger, HX) toplam tersinmezliği (irreversibility) tek bir değer olarak verir. Bu değer, iyileştirme potansiyelini anlamak için yeterli değildir. İleri exergy analizi (advanced exergy analysis), toplam tersinmezliği dört bileşene ayırarak karar vericilere çok daha fazla bilgi sunar:

- **Endojen (Endogenous, EN):** Bileşenin kendi iç tersinmezliklerinden kaynaklanan kısım
- **Ekzojen (Exogenous, EX):** Diğer bileşenlerin verimsizliklerinden kaynaklanan kısım
- **Kaçınılabilir (Avoidable, AV):** Teknolojik ve ekonomik olarak azaltılabilecek kısım
- **Kaçınılamaz (Unavoidable, UN):** Mevcut teknoloji ve fiziksel limitlerle azaltılamayan kısım

Bu dört bileşen birleştirilerek **4-yollu dekompozisyon** (4-way splitting) elde edilir.

## 2. Atık Isı Geri Kazanım HX Detaylı Çalışılmış Örnek (Worked Example)

### 2.1 Sistem Tanımı

Bir endüstriyel tesiste kompresör atık ısısının kazan besleme suyu ön ısıtması için kullanıldığı bir atık ısı geri kazanım (waste heat recovery) senaryosu ele alınmaktadır.

**Sistem Parametreleri:**

| Parametre | Sıcak Akış (Kompresör Soğutma Suyu) | Soğuk Akış (Kazan Besleme Suyu) |
|-----------|--------------------------------------|----------------------------------|
| Giriş sıcaklığı (T_in) | 85°C (358.15 K) | 25°C (298.15 K) |
| Çıkış sıcaklığı (T_out) | 45°C (318.15 K) | 65°C (338.15 K) |
| Kütle debisi (ṁ) | 1.2 kg/s | 0.8 kg/s |
| Basınç düşüşü (ΔP) | 0.15 bar | 0.08 bar |

**Isı Değiştirici Özellikleri:**

- Tip: Shell & tube (karşı akışlı / counter-flow)
- Isı transfer hızı: Q = 200 kW
- Logaritmik ortalama sıcaklık farkı: ΔT_LMTD = 20°C
- Toplam ısı transfer katsayısı × alan: UA = 10 kW/K
- Referans çevre sıcaklığı: T₀ = 25°C (298.15 K)

### 2.2 Konvansiyonel Exergy Analizi

Toplam tersinmezlik hesabı:

```
I_total = T₀ × S_gen

S_gen = ṁ_hot × cp × ln(T_hot_out/T_hot_in) + ṁ_cold × cp × ln(T_cold_out/T_cold_in)

S_gen = 1.2 × 4.18 × ln(318.15/358.15) + 0.8 × 4.18 × ln(338.15/298.15)
S_gen = 1.2 × 4.18 × (-0.1178) + 0.8 × 4.18 × (0.1263)
S_gen = -0.5909 + 0.4224
S_gen = -0.1685 + 0.4224 ≈ 0.0285 kW/K

I_total = 298.15 × 0.0285 = 8.5 kW
```

**Konvansiyonel exergy verimi:**

```
ε_HX = (ṁ_cold × Δex_cold) / (ṁ_hot × Δex_hot)

Δex_hot = cp × [(T_hot_in - T_hot_out) - T₀ × ln(T_hot_in/T_hot_out)]
Δex_hot = 4.18 × [(85 - 45) - 298.15 × ln(358.15/318.15)]
Δex_hot = 4.18 × [40 - 298.15 × 0.1178]
Δex_hot = 4.18 × [40 - 35.13] = 4.18 × 4.87 = 20.36 kJ/kg

Δex_cold = cp × [(T_cold_out - T_cold_in) - T₀ × ln(T_cold_out/T_cold_in)]
Δex_cold = 4.18 × [(65 - 25) - 298.15 × ln(338.15/298.15)]
Δex_cold = 4.18 × [40 - 298.15 × 0.1263]
Δex_cold = 4.18 × [40 - 37.67] = 4.18 × 2.33 = 9.74 kJ/kg

ε_HX = (0.8 × 9.74) / (1.2 × 20.36) = 7.79 / 24.43 = 0.319 ≈ 31.9%
```

Bu konvansiyonel analiz, toplam 8.5 kW kayıp olduğunu gösterir ancak bu kaybın ne kadarının iyileştirilebileceğini söylemez.

### 2.3 İleri Exergy Dekompozisyonu — 4-Yollu Ayrışım (4-Way Splitting)

#### Adım 1: Kaçınılamaz Koşulların Belirlenmesi (Unavoidable Conditions)

Shell & tube tipi HX için kaçınılamaz koşullar:

```
ΔT_min_UN = 5°C         (minimum yaklaşım sıcaklığı, teknolojik limit)
ΔP_UN_hot = 0.05 bar    (minimum kabul edilebilir basınç düşüşü — sıcak taraf)
ΔP_UN_cold = 0.03 bar   (minimum kabul edilebilir basınç düşüşü — soğuk taraf)
ε_UN = 0.97             (maksimum ulaşılabilir HX etkinliği)
```

#### Adım 2: Endojen/Ekzojen Ayrımı

Endojen tersinmezlik hesabı için tüm diğer bileşenler ideal (tersinir) kabul edilir ve yalnızca HX'in kendi gerçek koşulları kullanılır:

```
I_EN = I_total (diğer tüm bileşenler ideal çalışırken)
I_EN = 6.0 kW

I_EX = I_total - I_EN = 8.5 - 6.0 = 2.5 kW
```

Ekzojen bileşenin kaynakları:
- Kompresör isentropic verimi düşük → çıkış sıcaklığı beklenenden yüksek → HX'e giren ΔT daha büyük
- Kazan besleme suyu pompası verimsizliği → giriş basıncı dalgalanması → ΔP artışı
- Sistem konfigürasyonu (boru uzunlukları, vana kayıpları)

#### Adım 3: Kaçınılabilir/Kaçınılamaz Ayrımı

```
I_UN = I (kaçınılamaz koşullarda hesaplanan tersinmezlik)
I_UN = 4.2 kW

I_AV = I_total - I_UN = 8.5 - 4.2 = 4.3 kW
```

#### Adım 4: Birleşik 4-Yollu Dekompozisyon

| Kategori | Değer (kW) | Yüzde (%) | Açıklama |
|----------|------------|-----------|----------|
| I_EN^AV (Endojen-Kaçınılabilir) | 2.8 | 33 | HX tasarım iyileştirmesi ile azaltılabilir (ΔT azaltma, alan artırma) |
| I_EN^UN (Endojen-Kaçınılamaz) | 3.2 | 38 | ΔT_min = 5°C fiziksel limiti nedeniyle kaçınılamaz |
| I_EX^AV (Ekzojen-Kaçınılabilir) | 1.5 | 18 | Yukarı akış ekipmanı iyileştirmesi ile azaltılabilir (kompresör çıkış T düşürme) |
| I_EX^UN (Ekzojen-Kaçınılamaz) | 1.0 | 12 | Sistem konfigürasyonunun fiziksel limitleri |
| **Toplam** | **8.5** | **100** | — |

### 2.4 Sonuçların Yorumlanması

**Öncelik sıralaması (yatırım getirisi bazında):**

1. **I_EN^AV = 2.8 kW (%33):** En büyük iyileştirme potansiyeli. HX yüzey alanını artırmak, daha iyi türbülatörler kullanmak veya plakalı HX'e geçmek ile ΔT yaklaşım sıcaklığı düşürülebilir.

2. **I_EX^AV = 1.5 kW (%18):** Kompresörün isentropic verimini artırmak (örn. %75 → %85) HX'teki tersinmezliği de otomatik olarak azaltır. Bu "dolaylı iyileştirme" sıklıkla göz ardı edilir.

3. **I_EN^UN = 3.2 kW (%38):** Mevcut teknoloji ile kaçınılamaz. Ancak gelecekte mikro-kanallı HX veya nano-akışkan teknolojisi ile bu sınır düşebilir.

4. **I_EX^UN = 1.0 kW (%12):** Sistem tasarımının değiştirilmesi (yeni fabrika yerleşimi) gerektirdiğinden pratik olarak iyileştirilemez.

## 3. Tersinmezlik Bileşenleri: ΔT ve ΔP Ayrımı

Isı değiştiricilerdeki tersinmezlik iki temel kaynaktan oluşur:

### 3.1 Sıcaklık Farkından Kaynaklanan Tersinmezlik (I_ΔT)

```
I_ΔT = Q × (1/T_cold_avg - 1/T_hot_avg) × T₀

T_hot_avg = (T_hot_in + T_hot_out) / 2 = (358.15 + 318.15) / 2 = 338.15 K
T_cold_avg = (T_cold_in + T_cold_out) / 2 = (298.15 + 338.15) / 2 = 318.15 K

I_ΔT = 200 × (1/318.15 - 1/338.15) × 298.15
I_ΔT = 200 × (0.003143 - 0.002957) × 298.15
I_ΔT = 200 × 0.000186 × 298.15
I_ΔT ≈ 11.09 kW   (basitleştirilmiş, logaritmik ortalama ile detaylandırılabilir)
```

> **Not:** Bu basitleştirilmiş hesap, aritmetik ortalama sıcaklık kullanır. Daha doğru sonuç için logaritmik ortalama sıcaklık (LMTD) bazlı entropi üretimi hesabı kullanılmalıdır.

### 3.2 Basınç Düşüşünden Kaynaklanan Tersinmezlik (I_ΔP)

```
I_ΔP_hot = ṁ_hot × v_hot × ΔP_hot × T₀ / T_hot_avg

v_hot ≈ 0.001015 m³/kg  (suyun özgül hacmi, ~65°C ortalama)
I_ΔP_hot = 1.2 × 0.001015 × 15000 × 298.15 / 338.15
I_ΔP_hot = 1.2 × 0.001015 × 15000 × 0.8817
I_ΔP_hot ≈ 0.016 kW

I_ΔP_cold = ṁ_cold × v_cold × ΔP_cold × T₀ / T_cold_avg

v_cold ≈ 0.001003 m³/kg  (suyun özgül hacmi, ~45°C ortalama)
I_ΔP_cold = 0.8 × 0.001003 × 8000 × 298.15 / 318.15
I_ΔP_cold = 0.8 × 0.001003 × 8000 × 0.9372
I_ΔP_cold ≈ 0.006 kW
```

### 3.3 Bejan Sayısı (Bejan Number)

Bejan sayısı, ısı transferi kaynaklı tersinmezliğin toplam tersinmezliğe oranını ifade eder:

```
Be = I_ΔT / (I_ΔT + I_ΔP)

I_ΔP_total = I_ΔP_hot + I_ΔP_cold = 0.016 + 0.006 = 0.022 kW

Be = I_ΔT / (I_ΔT + I_ΔP_total)
```

**Tipik Bejan sayısı aralıkları:**

| HX Tipi | Be Aralığı | Yorum |
|---------|-----------|-------|
| Shell & tube | 0.80 - 0.95 | ΔT baskın, ΔP düşük |
| Plakalı (plate) | 0.70 - 0.85 | ΔP daha belirgin, dar kanallar |
| Finned tube | 0.85 - 0.95 | Hava tarafı ΔP ihmal edilebilir |
| Compact (mikro-kanal) | 0.60 - 0.80 | ΔP önemli, çok dar kanallar |
| Döner (rotary) | 0.75 - 0.90 | Sızıntı kayıpları ek faktör |

**Tasarım kuralı:** Be > 0.85 ise ΔT azaltmaya odaklan; Be < 0.70 ise ΔP azaltmaya odaklan.

## 4. Ekzojen Bileşenin Önemi ve Yukarı Akış Etkisi

### 4.1 Neden Ekzojen Bileşen Yüksektir?

Isı değiştiriciler, tanımları gereği iki akış arasında enerji transferi yapan bileşenlerdir. Bu nedenle, giriş koşulları doğrudan diğer ekipmanlar tarafından belirlenir:

- **Kompresör çıkış sıcaklığı:** İsentropic verim düşükse → T_out yükselir → HX'e giren sıcaklık farkı artar → I_ΔT artar
- **Pompa performansı:** Besleme suyu debisi veya basıncında sapma → HX'te off-design çalışma → ek tersinmezlik
- **Kazan geri dönüş hattı:** Kazan verimsizliği → geri dönüş suyu sıcaklığı değişir → HX giriş koşulları değişir

Tipik olarak HX'lerde ekzojen tersinmezlik oranı:

| Senaryo | I_EX / I_total (%) | Açıklama |
|---------|---------------------|----------|
| Tek HX, iyi eşleşmiş akışlar | 15 - 25 | Düşük ekzojen etki |
| Atık ısı geri kazanım HX | 25 - 40 | Yukarı akış ekipmanına bağımlı |
| HX ağı (network) içinde | 30 - 50 | Komşu HX'lerden yayılan etki |
| Rejeneratif döngüde HX | 20 - 35 | Döngü iç bağımlılığı |

### 4.2 Kompresör Verimsizliğinin HX'e Yayılması (Propagation of Inefficiency)

Sayısal gösterim:

```
Senaryo A: Kompresör ηis = 0.85 (iyi)
  → T_comp_out = 78°C
  → HX giriş ΔT = 78 - 25 = 53°C
  → I_HX_total = 6.2 kW
  → I_EX = 0.8 kW (%13)

Senaryo B: Kompresör ηis = 0.70 (kötü)
  → T_comp_out = 95°C
  → HX giriş ΔT = 95 - 25 = 70°C
  → I_HX_total = 11.4 kW
  → I_EX = 4.2 kW (%37)

Fark: ΔI_EX = 3.4 kW → kompresörü iyileştirmek HX'te 3.4 kW tasarruf sağlar
```

**Kritik çıkarım:** HX'i iyileştirmek yerine yukarı akış ekipmanını (kompresör) iyileştirmek bazen daha yüksek getiri sağlar. Bu, yalnızca ileri exergy analizi ile ortaya çıkar.

## 5. Pinch Analizi ile İleri Exergy Bağlantısı

### 5.1 Cross-Pinch Isı Transferi ve Kaçınılabilirlik

Pinch analizi, minimum enerji tüketimi için HX ağı tasarımının temelini oluşturur. İleri exergy analizi ile birleştirildiğinde:

```
Cross-pinch ısı transferi miktarı = Q_cross-pinch

Bu miktarın tamamı kaçınılabilir (avoidable) tersinmezliktir:
I_cross-pinch ⊆ I_AV

Pinch kuralları ihlal ediliyorsa:
  Kural 1: Pinch üstünde soğutma kullanma → I_AV artışı
  Kural 2: Pinch altında ısıtma kullanma → I_AV artışı
  Kural 3: Cross-pinch transfer yapma → I_AV artışı
```

### 5.2 ΔT_min Seçimi ve Kaçınılamaz Tersinmezlik

ΔT_min (minimum yaklaşım sıcaklığı) seçimi doğrudan I_UN'u belirler:

| ΔT_min (°C) | HX Alanı (m²) | I_UN (kW) | Yatırım Maliyeti (x1000 €) | Yorum |
|-------------|---------------|-----------|---------------------------|-------|
| 3 | 67 | 1.8 | 85 | Çok büyük alan, yüksek maliyet |
| 5 | 40 | 3.2 | 55 | Endüstriyel standart |
| 10 | 20 | 6.5 | 32 | Kompakt, düşük maliyet |
| 15 | 13 | 9.8 | 22 | Çok kompakt, yüksek kayıp |
| 20 | 10 | 13.1 | 18 | Küçük alan, çok yüksek kayıp |

### 5.3 Grand Composite Curve (GCC) ile Utility Yerleştirme

Grand Composite Curve kullanarak utility entegrasyonu optimize edildiğinde, ekzojen tersinmezlik minimize edilir:

```
GCC bazlı utility yerleştirme →
  → Her utility, ihtiyaç duyulan sıcaklık seviyesine uygun yerleştirilir
  → Yüksek sıcaklıklı utility, düşük sıcaklık ihtiyacı için kullanılmaz
  → I_EX_utility = Σ [Q_utility,i × (1 - T₀/T_utility,i) - Q_utility,i × (1 - T₀/T_process,i)]
  → Minimum I_EX → optimum utility seçimi
```

## 6. HX Tip Bazlı İleri Exergy Karşılaştırma Tablosu

### 6.1 Farklı HX Tiplerinin Kaçınılamaz Koşulları

| HX Tipi | ΔT_min^UN (°C) | ΔP/P^UN (%) | ε_max^UN | Tipik I_EN^UN Payı (%) |
|---------|----------------|-------------|----------|----------------------|
| Shell & tube (karşı akışlı) | 5 | 1.0 | 0.97 | 35 - 45 |
| Shell & tube (paralel akışlı) | 8 | 1.0 | 0.90 | 45 - 55 |
| Plakalı (gasketed plate) | 3 | 2.5 | 0.98 | 25 - 35 |
| Kaynaklı plakalı (welded plate) | 2 | 2.0 | 0.98 | 20 - 30 |
| Spiral | 4 | 3.0 | 0.96 | 30 - 40 |
| Finned tube (kanatçıklı boru) | 10 | 0.5 | 0.92 | 40 - 55 |
| Mikro-kanal (microchannel) | 1 | 5.0 | 0.99 | 15 - 25 |
| Döner rejeneratör (rotary) | 5 | 1.5 | 0.95 | 35 - 45 |
| Isı borusu (heat pipe) | 3 | 0.2 | 0.97 | 25 - 35 |

### 6.2 HX Tipi Seçim Kriterleri (İleri Exergy Perspektifi)

```
Karar ağacı:

1. I_ΔT >> I_ΔP (Be > 0.85)?
   → Evet: ΔT_min düşük HX tipi seç (plakalı, mikro-kanal)
   → Hayır: ΔP düşük HX tipi seç (finned tube, heat pipe)

2. I_EX / I_total > 0.30?
   → Evet: Önce yukarı akış ekipmanını optimize et, sonra HX seç
   → Hayır: HX tasarımına odaklan

3. I_AV / I_total > 0.40?
   → Evet: Mevcut HX'i değiştir veya yükselt (retrofit)
   → Hayır: Mevcut HX yeterli, başka ekipmana odaklan
```

## 7. Tasarım ve İşletme Optimizasyonu Stratejileri

### 7.1 Tasarım Aşaması Optimizasyonu (Design Optimization)

**Hedef:** I_EN^AV ve I_EN^UN'u minimize etmek.

| Strateji | Etkilediği Bileşen | Beklenen Tasarruf (%) | Yatırım Seviyesi |
|----------|--------------------|-----------------------|-------------------|
| HX alanını artırma | I_EN^AV ↓ | 15 - 30 | Orta |
| Karşı akış konfigürasyonu | I_EN^AV ↓, I_EN^UN ↓ | 10 - 20 | Düşük |
| Türbülatör ekleme | I_EN^AV ↓ | 5 - 15 | Düşük |
| Daha verimli HX tipine geçiş | I_EN^AV ↓, I_EN^UN ↓ | 20 - 40 | Yüksek |
| Çok geçişli tasarım (multi-pass) | I_EN^AV ↓ | 8 - 18 | Orta |
| Nano-akışkan kullanımı | I_EN^AV ↓ | 5 - 12 | Orta |

### 7.2 İşletme Aşaması Optimizasyonu (Operational Optimization)

**Hedef:** I_EX^AV'yi minimize etmek ve off-design performansı iyileştirmek.

| Strateji | Etkilediği Bileşen | Beklenen Tasarruf (%) | Uygulama Kolaylığı |
|----------|--------------------|-----------------------|---------------------|
| Debi oranı optimizasyonu (ṁ_hot/ṁ_cold) | I_EN^AV ↓ | 5 - 15 | Kolay |
| Fouling yönetimi (temizlik periyodu) | I_EN^AV ↓ | 10 - 25 | Orta |
| Yukarı akış ekipman bakımı | I_EX^AV ↓ | 15 - 35 | Orta |
| By-pass vana kontrolü | I_EN^AV ↓ | 3 - 10 | Kolay |
| Yük takibi (load following) | I_EX^AV ↓ | 8 - 20 | Orta |
| Kompresör verimi iyileştirme | I_EX^AV ↓ | 10 - 25 | Zor |

### 7.3 Bütünleşik Optimizasyon Yaklaşımı

En etkili iyileştirme, hem tasarım hem de işletme stratejilerini birleştiren bütünleşik yaklaşımdır:

```
Adım 1: Konvansiyonel exergy analizi → I_total hesapla
Adım 2: İleri exergy dekompozisyonu → 4-yollu ayrımı yap
Adım 3: I_EN^AV / I_total oranını kontrol et
         → > 0.25 ise: HX tasarım iyileştirmesine odaklan
         → < 0.25 ise: Adım 4'e geç
Adım 4: I_EX^AV / I_total oranını kontrol et
         → > 0.15 ise: Yukarı akış ekipman iyileştirmesine odaklan
         → < 0.15 ise: Mevcut sistem yeterince optimize
Adım 5: Exergoekonomik analiz ile yatırım karar analizi
Adım 6: Pinch analizi ile sistem geneli optimizasyon
```

## 8. Endüstriyel Uygulama Örnekleri

### 8.1 Gıda Endüstrisi — Pastörizasyon HX

- ΔT_min = 3°C (plakalı HX kullanımı zorunlu)
- Fouling hızlı → I_EN^AV zamanla artar
- Periyodik CIP (Clean-in-Place) ile I_EN^AV geri kazanılır
- Tipik I_EX payı: %20 (pompa ve proses koşullarından)

### 8.2 Kimya Endüstrisi — Reaktör Soğutma HX

- Yüksek sıcaklık ve basınç → shell & tube zorunlu
- I_EN^UN yüksek (büyük ΔT kaçınılamaz, emniyet marjı)
- I_EX çok yüksek olabilir (reaktör koşulları dalgalı)
- İleri exergy analizi, reaktör optimizasyonunun HX'ten daha öncelikli olduğunu gösterir

### 8.3 Enerji Santrali — Kondenser

- Çok büyük ΔT (buhar → soğutma suyu)
- I_EN^UN baskın (%50-65): Carnot limiti nedeniyle
- I_EX^AV düşük: Sistem tasarımı neredeyse optimal
- Fokus: Soğutma suyu sıcaklığını düşürmek (kule optimizasyonu)

## 9. Sınırlamalar ve Dikkat Edilmesi Gerekenler

1. **Kaçınılamaz koşulların belirlenmesi subjektiftir.** Farklı analistler farklı ΔT_min^UN değerleri kullanabilir. Sonuçlar bu varsayımlara duyarlıdır.

2. **Ekzojen bileşen hesabı iteratiftir.** Her bileşen diğerlerini etkiler; bu nedenle tam sistem simülasyonu gerekir.

3. **Dinamik koşullar göz ardı edilir.** Gerçek tesislerde yük değişimleri, başlatma/durdurma döngüleri ek tersinmezlik yaratır.

4. **Fouling etkisi zamanla değişir.** Başlangıçta I_EN^UN olan bileşen, fouling ile I_EN^AV'ye dönüşebilir (temizlik ile giderilebilir hale gelir).

## İlgili Dosyalar

- `knowledge/heat_exchanger/formulas.md` — Temel HX exergy formülleri ve hesaplama yöntemleri
- `knowledge/heat_exchanger/benchmarks.md` — HX tip bazlı verimlilik referans değerleri
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası exergy entegrasyon fırsatları
- `knowledge/factory/heat_integration.md` — Isı entegrasyonu genel çerçevesi
- `knowledge/factory/pinch_analysis.md` — Pinch analizi temel kavramları ve uygulama
- `knowledge/factory/pinch/grand_composite_curve.md` — GCC ile utility optimizasyonu
- `knowledge/factory/waste_heat_recovery.md` — Atık ısı geri kazanım stratejileri
- `knowledge/factory/exergoeconomic/` — Exergoekonomik analiz yöntemleri
- `skills/equipment/heat_exchanger_expert.md` — HX uzman AI beceri tanımı
- `skills/factory/integration_expert.md` — Fabrika entegrasyon uzmanı AI beceri tanımı

## Referanslar

1. Tsatsaronis, G. & Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. — İleri exergy analizinin temel metodolojisi ve 4-yollu dekompozisyon çerçevesinin tanımlandığı referans çalışma.

2. Morosuk, T. & Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258. — Endojen/ekzojen ayrımının ısı transfer ekipmanlarına uygulanması ve ekipmanlar arası etkileşim analizi.

3. Bejan, A. (1996). "Entropy Generation Minimization: The Method of Thermodynamic Optimization of Finite-Size Systems and Finite-Time Processes." *CRC Press*. — Bejan sayısının tanımı, ısı değiştiricilerde entropi üretimi minimizasyonu ve ΔT/ΔP kaynaklı tersinmezlik ayrımının matematiksel temeli.

4. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. — Endojen/ekzojen ayrımı için farklı hesaplama yaklaşımlarının karşılaştırması ve HX ağlarına uygulama örnekleri.

5. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. — Kombine çevrim santrali içindeki ısı değiştiricilere (kondenser, ekonomizer, HRSG) ileri exergy analizinin uygulanması ve çapraz ekipman etkileşimlerinin kantitatif gösterimi.
