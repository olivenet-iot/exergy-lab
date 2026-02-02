---
title: "Exergoekonomik Duyarlılık Analizi (Sensitivity Analysis)"
category: factory
equipment_type: factory
keywords: [duyarlılık analizi, OAT, tornado diyagramı, Monte Carlo, parametre belirsizliği, senaryo analizi]
related_files:
  - factory/exergoeconomic/optimization.md
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/exergoeconomic/cost_equations.md
  - factory/exergoeconomic/cost_databases.md
  - factory/exergoeconomic/levelized_cost.md
use_when:
  - "Exergoekonomik sonuçların parametre değişimlerine duyarlılığı incelenirken"
  - "Girdi belirsizlikleri değerlendirilirken"
  - "Yatırım karar güvenilirliği sorgulanırken"
  - "Monte Carlo simülasyonu planlanırken"
priority: medium
last_updated: 2026-02-01
---
# Exergoekonomik Duyarlılık Analizi (Sensitivity Analysis)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Exergoekonomik analizde kullanılan girdi parametreleri (ekipman maliyetleri, yakıt fiyatları, faiz oranı, yıllık çalışma saati vb.) belirsizlik içerir. Duyarlılık analizi, bu belirsizliklerin sonuçlar üzerindeki etkisini sistematik olarak değerlendirir.

```
Neden Duyarlılık Analizi Gerekli?

1. Ekipman maliyet korelasyonları ±20-30% belirsizlik içerir
2. Yakıt fiyatları yıldan yıla %10-50 değişebilir
3. Faiz oranı ve ekonomik ömür varsayımlara dayalıdır
4. Termodinamik ölçümler ölçüm hatası taşır
5. Karar vericiler "en kötü durumda ne olur?" sorusuna yanıt ister

Amaç:
→ Hangi parametrelerin sonucu en çok etkilediğini belirlemek
→ Sonuçların güvenilirlik aralığını tespit etmek
→ Kararların farklı senaryolarda geçerliliğini doğrulamak
```

## 2. One-At-a-Time (OAT) Parametre Değişimi

### 2.1 Metodoloji

OAT yöntemi, her seferinde yalnızca bir parametre değiştirilerek sonuçlara etkisinin incelenmesidir. Basit ve yaygın kullanılan bir yöntemdir.

```
OAT Adımları:

Adım 1: Baz durum (base case) analizi yap
        → Tüm parametreler nominal değerlerinde
        → c_P,baz, Ċ_D,baz, f_k,baz hesapla

Adım 2: Her parametre için değişim aralığı tanımla
        → Genellikle ±10%, ±20%, ±30% veya ±50%

Adım 3: Her seferinde bir parametre değiştir
        → Diğer tüm parametreler sabit
        → Hedef değişkeni yeniden hesapla

Adım 4: Sonuçları normalize et ve karşılaştır
        → Δ(hedef) / Δ(parametre) oranını hesapla
        → En hassas parametreleri sırala
```

### 2.2 Tipik OAT Parametreleri

| Parametre | Tipik Aralık | Birim | Etki Yönü |
|-----------|-------------|-------|-----------|
| Yakıt birim fiyatı (c_fuel) | ±20-50% | €/GJ | c_P,ürün ↑↓ doğrudan |
| Elektrik birim fiyatı (c_el) | ±15-30% | €/kWh | Kompresör/pompa c_F ↑↓ |
| Ekipman satın alma maliyeti (PEC) | ±20-30% | € | Ż ↑↓, f_k ↑↓ |
| Faiz oranı (i) | ±3-5 puan | % | CRF ↑↓, Ż ↑↓ |
| Ekonomik ömür (n) | ±5 yıl | yıl | CRF ↑↓, Ż ↑↓ |
| Yıllık çalışma saati (τ) | ±500-1000 | saat/yıl | Ż [€/saat] ↓↑ |
| İsentropic verim (η_s) | ±3-5 puan | % | Ė_D ↑↓, Ċ_D ↑↓ |
| Çevre sıcaklığı (T₀) | ±5-10 | °C | Exergy akışları ↑↓ |
| Bakım faktörü (φ) | ±0.02-0.04 | — | Ż_OM ↑↓ |

### 2.3 OAT Hesaplama Örneği

```
Baz Durum:
  c_fuel = 5.0 €/GJ
  PEC_kazan = 200,000 €
  i = 10%, n = 20 yıl
  → c_P,buhar = 28.5 €/GJ
  → Ċ_D,kazan = 12.3 €/saat

Parametre Değişimi: c_fuel ±20%

c_fuel = 4.0 €/GJ → c_P,buhar = 24.2 €/GJ  (-15.1%)
c_fuel = 5.0 €/GJ → c_P,buhar = 28.5 €/GJ  (baz)
c_fuel = 6.0 €/GJ → c_P,buhar = 32.8 €/GJ  (+15.1%)

Duyarlılık katsayısı:
S = Δc_P / Δc_fuel = (32.8 - 24.2) / (6.0 - 4.0) = 4.3 [€/GJ per €/GJ]

Normalize duyarlılık:
S_norm = (Δc_P/c_P,baz) / (Δc_fuel/c_fuel,baz)
       = (15.1%) / (20%) = 0.755

Yorum: c_fuel'deki %1'lik değişim, c_P'de ~%0.76'lık değişime yol açar.
```

## 3. Tornado Diyagramları

### 3.1 Oluşturma Yöntemi

Tornado diyagramı, OAT sonuçlarını görsel olarak sıralayan bir çubuk grafiktir. En etkili parametre en üstte yer alır.

```
Tornado Diyagramı Oluşturma:

1. Tüm parametreleri ±20% (veya tanımlı aralık) değiştir
2. Her parametre için c_P alt ve üst sınırını hesapla
3. Parametreleri etki büyüklüğüne göre sırala (en büyük → en küçük)
4. Yatay çubuk grafiği olarak çiz:
   - Merkez çizgi: baz durum c_P
   - Sol çubuk: parametrenin alt sınır etkisi
   - Sağ çubuk: parametrenin üst sınır etkisi

Görsel Düzen:
                    24    26    28    30    32  [€/GJ]
                     |     |  baz |     |
c_fuel    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████
PEC_kazan   ▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████
η_s           ▓▓▓▓▓▓▓▓▓▓▓██████████████
i              ▓▓▓▓▓▓▓▓▓█████████████
τ                ▓▓▓▓▓▓▓███████████
n                  ▓▓▓▓▓████████
T₀                   ▓▓▓██████
φ                     ▓▓████

▓ = azalma yönü    █ = artış yönü
```

### 3.2 Tornado Diyagramı Yorumlama Kuralları

```
Yorum Kuralları:

1. Üst parametreler = kontrol edilmesi gereken parametreler
   → Yakıt fiyatı en üstte ise, yakıt değişim senaryolarına dikkat

2. Geniş çubuk = yüksek belirsizlik etkisi
   → Bu parametrenin daha iyi tahmin edilmesi gerekir

3. Asimetrik çubuk = doğrusal olmayan etki
   → Pozitif/negatif yönde farklı duyarlılık

4. Dar çubuk = düşük etki → bu parametre ihmal edilebilir

5. İlk 3-4 parametre toplam belirsizliğin ~%80'ini oluşturur (Pareto prensibi)
```

## 4. Senaryo Analizi

### 4.1 Tanım ve Yaklaşım

Senaryo analizi, birden fazla parametre aynı anda değiştirilerek tutarlı "dünya durumları" oluşturur. OAT'dan farklı olarak, parametreler arası korelasyonları yakalar.

```
Tipik Senaryolar:

Senaryo 1: İyimser (Optimistic)
  - Yakıt fiyatı: -20%
  - Faiz oranı: -3 puan
  - Ekipman maliyeti: -15%
  - Çalışma saati: +10%

Senaryo 2: Baz Durum (Base Case)
  - Tüm parametreler nominal değerlerinde

Senaryo 3: Kötümser (Pessimistic)
  - Yakıt fiyatı: +30%
  - Faiz oranı: +3 puan
  - Ekipman maliyeti: +25%
  - Çalışma saati: -10%

Senaryo 4: Yüksek Enerji Maliyeti
  - Yakıt fiyatı: +50%
  - Elektrik fiyatı: +40%
  - Diğer parametreler: nominal

Senaryo 5: Düşük Yatırım Ortamı (Türkiye Özgü)
  - Faiz oranı: +10 puan (yüksek WACC)
  - TL değer kaybı: +20%
  - Ekipman maliyeti: +30% (ithalat kuru etkisi)
```

### 4.2 Türkiye'ye Özel Senaryo Parametreleri

```
Türkiye Ekonomik Senaryoları (2024-2026):

Parametre                 | İyimser | Baz     | Kötümser |
--------------------------|---------|---------|----------|
WACC (TL bazlı)          | %18     | %25     | %35      |
Doğalgaz fiyatı (€/GJ)   | 8.0     | 10.5    | 14.0     |
Elektrik fiyatı (€/kWh)  | 0.08    | 0.10    | 0.14     |
EUR/TL kuru               | 28      | 32      | 38       |
CEPCI düzeltme faktörü    | 1.0     | 1.15    | 1.35     |

Not: Türkiye'de yüksek enflasyon ortamı nedeniyle:
  - Reel faiz oranı kullanılmalıdır
  - Ekipman maliyetleri döviz bazlı güncellenmelidir
  - Enerji fiyatları düzenleyici değişikliklere duyarlıdır
```

### 4.3 Senaryo Sonuç Tablosu Formatı

```
Senaryo Karşılaştırma Tablosu:

                    | İyimser | Baz    | Kötümser | Değişim Aralığı |
--------------------|---------|--------|----------|-----------------|
c_P,buhar [€/GJ]   | 23.1    | 28.5   | 38.2     | -19% / +34%     |
c_P,elek [€/kWh]   | 0.071   | 0.089  | 0.121    | -20% / +36%     |
Ċ_D,toplam [€/saat]| 38.5    | 52.1   | 71.8     | -26% / +38%     |
Geri ödeme [yıl]    | 2.1     | 3.4    | 5.8      | -38% / +71%     |

Karar: Kötümser senaryoda bile geri ödeme < 6 yıl → yatırım güvenli
```

## 5. Monte Carlo Simülasyonu

### 5.1 Yöntem

Monte Carlo, girdi parametrelerine olasılık dağılımları atayarak sonuçların istatistiksel dağılımını elde eden bir yöntemdir. OAT ve senaryo analizinden daha kapsamlıdır.

```
Monte Carlo Adımları:

Adım 1: Her girdi parametresi için olasılık dağılımı tanımla
        → Normal, üçgen, uniform, lognormal vb.

Adım 2: N adet rastgele parametre seti üret (N = 1,000 - 100,000)
        → Latin Hypercube Sampling (LHS) tercih edilir

Adım 3: Her set için exergoekonomik analizi çalıştır
        → c_P, Ċ_D, f_k, r_k vb. hesapla

Adım 4: Sonuç dağılımlarını analiz et
        → Ortalama, standart sapma, %5-%95 güven aralığı
        → Histogram, kümülatif dağılım fonksiyonu (CDF)

Adım 5: Sonuçları raporla
        → c_P = 28.5 ± 4.2 €/GJ (%95 güven aralığı: 21.3 - 36.8)
```

### 5.2 Tipik Dağılım Seçimleri

| Parametre | Önerilen Dağılım | Parametreler | Gerekçe |
|-----------|-----------------|--------------|---------|
| Yakıt fiyatı | Lognormal | μ=ln(5.0), σ=0.20 | Pozitif değer, sağa çarpık |
| PEC | Üçgen | (min=0.7×, mod=1.0×, max=1.3×) | Maliyet tahminleri asimetrik |
| Faiz oranı | Normal | μ=10%, σ=2% | Finansal parametre |
| Çalışma saati | Normal | μ=7500, σ=500 | Yıllık dağılım yaklaşık normal |
| İsentropic verim | Üçgen | (min=η-5%, mod=η, max=η+2%) | Bozulma etkisi asimetrik |
| Çevre sıcaklığı | Normal | μ=25°C, σ=5°C | İklimsel değişim |
| Bakım faktörü | Uniform | [0.04, 0.08] | Belirsiz tahmin |

### 5.3 Python Implementasyonu

```python
import numpy as np
from scipy import stats

def monte_carlo_exergoeconomic(base_params, n_samples=10000, seed=42):
    """Monte Carlo duyarlılık analizi.

    Args:
        base_params: Baz durum parametreleri dict
        n_samples: Örneklem sayısı
        seed: Rastgele sayı tohumu
    """
    rng = np.random.default_rng(seed)

    # Parametre dağılımlarını tanımla
    c_fuel = rng.lognormal(
        mean=np.log(base_params['c_fuel']),
        sigma=0.20,
        size=n_samples
    )
    pec_factor = rng.triangular(
        left=0.70, mode=1.00, right=1.30,
        size=n_samples
    )
    interest_rate = rng.normal(
        loc=base_params['interest_rate'],
        scale=0.02,
        size=n_samples
    )
    interest_rate = np.clip(interest_rate, 0.01, 0.50)  # Fiziksel sınırlar

    hours = rng.normal(
        loc=base_params['annual_hours'],
        scale=500,
        size=n_samples
    )
    hours = np.clip(hours, 2000, 8760)

    # Her örneklem için hesapla
    results = {
        'c_P': np.zeros(n_samples),
        'C_D_dot_total': np.zeros(n_samples),
        'payback': np.zeros(n_samples),
    }

    for i in range(n_samples):
        params_i = base_params.copy()
        params_i['c_fuel'] = c_fuel[i]
        params_i['pec_factor'] = pec_factor[i]
        params_i['interest_rate'] = interest_rate[i]
        params_i['annual_hours'] = hours[i]

        # Exergoekonomik hesaplama fonksiyonu (dış bağımlılık)
        result_i = run_exergoeconomic_analysis(params_i)
        results['c_P'][i] = result_i['c_P_product']
        results['C_D_dot_total'][i] = result_i['C_D_dot_total']
        results['payback'][i] = result_i['payback_years']

    # İstatistiksel özet
    summary = {}
    for key, values in results.items():
        summary[key] = {
            'mean': np.mean(values),
            'std': np.std(values),
            'p5': np.percentile(values, 5),
            'p50': np.percentile(values, 50),
            'p95': np.percentile(values, 95),
        }

    return summary, results
```

### 5.4 Monte Carlo Sonuç Yorumlama

```
Monte Carlo Sonuç Raporu (N = 10,000):

c_P,buhar [€/GJ]:
  Ortalama: 28.8  |  Medyan: 28.3  |  Std: 4.1
  %5 güven:  22.1  |  %95 güven: 36.4
  Dağılım: hafif sağa çarpık (yakıt fiyatı etkisi)

Ċ_D,toplam [€/saat]:
  Ortalama: 53.2  |  Medyan: 51.8  |  Std: 8.7
  %5 güven:  39.5  |  %95 güven: 69.1

Geri Ödeme [yıl]:
  Ortalama: 3.6   |  Medyan: 3.3   |  Std: 1.2
  %5 güven:  2.0   |  %95 güven: 6.1
  P(geri ödeme < 5 yıl) = 87.3%

Yorum:
→ %95 güven aralığında bile c_P < 37 €/GJ
→ Geri ödemenin 5 yılı aşma olasılığı yalnızca %12.7
→ Yakıt fiyatı en baskın belirsizlik kaynağı
```

## 6. Global Duyarlılık Analizi

### 6.1 Sobol İndeksleri

OAT yalnızca lokal duyarlılığı ölçerken, Sobol indeksleri global etkileşimleri hesaplar.

```
Sobol İndeksleri:

S_i     = Birinci derece indeks (first-order)
          → Parametre i'nin tek başına toplam varyansa katkısı

S_Ti    = Toplam etki indeksi (total-order)
          → Parametre i'nin tüm etkileşimler dahil toplam katkısı

S_Ti - S_i = Etkileşim katkısı

Hesaplama:
  S_i = V[E(Y|X_i)] / V(Y)

Burada:
  Y     = hedef değişken (ör. c_P)
  X_i   = i. parametre
  V(Y)  = Y'nin toplam varyansı
  V[E(Y|X_i)] = X_i koşullu beklenen değerin varyansı
```

### 6.2 Tipik Sobol Sonuçları

```
Sobol İndeksleri — c_P,buhar hedef değişkeni:

Parametre     | S_i (1.derece) | S_Ti (Toplam) | Etkileşim |
--------------|----------------|---------------|-----------|
c_fuel        | 0.42           | 0.48          | 0.06      |
PEC           | 0.22           | 0.28          | 0.06      |
η_s           | 0.15           | 0.19          | 0.04      |
i (faiz)      | 0.09           | 0.12          | 0.03      |
τ (saat)      | 0.07           | 0.10          | 0.03      |
n (ömür)      | 0.03           | 0.05          | 0.02      |
T₀            | 0.02           | 0.03          | 0.01      |
Toplam S_i    | 1.00           |               |           |

Yorum:
→ c_fuel tek başına varyansın %42'sini açıklıyor
→ İlk 3 parametre birlikte %79'u açıklıyor
→ Etkileşim terimleri küçük (|S_Ti - S_i| < 0.07)
  → Doğrusal varsayım bu sistem için geçerli
```

## 7. Çözümlü Endüstriyel Örnek

### 7.1 Problem Tanımı

```
Sistem: Buhar kazanı + hava kompresörü + pompa
Amaç: c_P,buhar duyarlılık analizi (OAT + Monte Carlo)

Baz Durum Parametreleri:
  Kazan PEC: 180,000 €
  Kompresör PEC: 45,000 €
  Pompa PEC: 12,000 €
  Doğalgaz fiyatı: 10.5 €/GJ
  Elektrik fiyatı: 0.10 €/kWh
  Faiz oranı: 12% (Türkiye reel WACC)
  Ekonomik ömür: 15 yıl
  Çalışma saati: 7200 saat/yıl
  Bakım faktörü: 0.06
```

### 7.2 OAT Sonuçları

```
OAT ±20% Değişim Sonuçları — c_P,buhar [€/GJ]:

Parametre          | -20%    | Baz    | +20%   | Δ aralık |
-------------------|---------|--------|--------|----------|
Doğalgaz fiyatı    | 26.1    | 31.4   | 36.7   | 10.6     |
Kazan PEC          | 29.8    | 31.4   | 33.0   | 3.2      |
Faiz oranı         | 30.1    | 31.4   | 32.8   | 2.7      |
Çalışma saati      | 32.6    | 31.4   | 30.5   | 2.1      |
Kazan verimi       | 33.8    | 31.4   | 29.5   | 4.3      |
Ekonomik ömür       | 32.1    | 31.4   | 30.9   | 1.2      |
Bakım faktörü      | 30.8    | 31.4   | 32.0   | 1.2      |
Çevre sıcaklığı    | 31.2    | 31.4   | 31.6   | 0.4      |

Sıralama: Doğalgaz > Kazan verimi > Kazan PEC > Faiz > Çalışma saati
```

### 7.3 Senaryo Karşılaştırması

```
3 Senaryo Karşılaştırması:

                         | İyimser | Baz   | Kötümser |
-------------------------|---------|-------|----------|
c_P,buhar [€/GJ]        | 25.8    | 31.4  | 42.1     |
Ċ_D,kazan [€/saat]      | 8.2     | 11.5  | 16.8     |
f_k,kazan                | 0.38    | 0.32  | 0.24     |
Toplam tasarruf [€/yıl]  | 28,500  | 22,100| 14,200   |
Geri ödeme [yıl]         | 2.3     | 3.5   | 6.1      |

İyimser senaryo: Doğalgaz -15%, PEC -10%, faiz -3puan
Kötümser senaryo: Doğalgaz +30%, PEC +25%, faiz +5puan

Karar:
→ İyimser durumda geri ödeme 2.3 yıl — kesinlikle yapılmalı
→ Baz durumda 3.5 yıl — yapılması önerilir
→ Kötümser durumda 6.1 yıl — yüksek risk, dikkatli değerlendirilmeli
→ Tüm senaryolarda f_k < 0.40 → termodinamik iyileştirme öncelikli
```

### 7.4 Monte Carlo Özeti

```
Monte Carlo (N = 10,000) Sonuçları:

c_P,buhar [€/GJ]:
  Ortalama: 31.8 ± 4.5 (1σ)
  %5 - %95 güven aralığı: [24.9 - 40.2]

Ċ_D,toplam [€/saat]:
  Ortalama: 15.1 ± 3.2
  %5 - %95 güven aralığı: [10.2 - 21.5]

Geri ödeme [yıl]:
  Ortalama: 3.7 ± 1.3
  P(< 3 yıl) = 38.2%
  P(< 5 yıl) = 81.5%
  P(< 7 yıl) = 95.8%

Sonuç:
→ %95 güvenle geri ödeme < 7 yıl
→ En olası geri ödeme aralığı: 2.5 - 5.0 yıl
→ Yatırım kararı: YAPILMALI (beklenen değer pozitif, risk kabul edilebilir)
```

## 8. Duyarlılık Analizi Raporlama Kontrol Listesi

```
Raporlama Kontrol Listesi:

□ Baz durum açıkça tanımlanmış mı?
□ Parametre aralıkları gerekçelendirilmiş mi?
□ OAT sonuçları tablo halinde sunulmuş mu?
□ Tornado diyagramı çizilmiş mi?
□ En az 3 senaryo (iyimser/baz/kötümser) analiz edilmiş mi?
□ Monte Carlo olasılık dağılımları belirtilmiş mi?
□ Güven aralıkları (%5-%95) raporlanmış mı?
□ Karar değişkeni net mi? (c_P, geri ödeme, NPV?)
□ Kötümser senaryoda bile karar geçerli mi?
□ En hassas parametreler belirlenmiş mi?
□ Veri kalitesi iyileştirme önerileri var mı?
```

## 9. Sık Yapılan Hatalar

```
Hata 1: Yalnızca OAT kullanmak
→ OAT parametre etkileşimlerini yakalaYAMAZ
→ Çözüm: Monte Carlo veya Sobol ile destekle

Hata 2: Keyfi parametre aralıkları
→ "Hepsine ±20% uygula" gerçekçi değil
→ Çözüm: Her parametre için gerçekçi belirsizlik aralığı belirle

Hata 3: Korelasyonları ihmal etmek
→ Enerji fiyatları birbiriyle korelasyonludur (gaz ↑ → elektrik ↑)
→ Çözüm: Korelasyon matrisi tanımla veya senaryo analizi kullan

Hata 4: Çok az örneklem
→ N = 100 ile Monte Carlo güvenilir değil
→ Çözüm: N ≥ 5,000, tercihen 10,000+

Hata 5: Yalnızca ortalamayı raporlamak
→ Karar vericiler risk bilgisi ister
→ Çözüm: Güven aralıkları ve olasılık ifadeleri kullan

Hata 6: Türkiye'de sabit döviz kuru varsaymak
→ PEC genellikle euro bazlıdır
→ Çözüm: Kur senaryosu ekle
```

## 10. ExergyLab Entegrasyon Notu

```
ExergyLab Platformunda Duyarlılık Analizi:

Mevcut Durum:
→ Tek nokta exergoekonomik analiz destekleniyor
→ Duyarlılık analizi modülü henüz implementasyonda değil

Planlanan Özellikler:
→ OAT parametre kaydırıcıları (slider) ile anlık güncelleme
→ Tornado diyagramı otomatik oluşturma
→ 3-senaryo karşılaştırma tablosu
→ Monte Carlo modülü (Python backend entegrasyonu)

Geçici Çözüm:
→ Kullanıcı baz analizi yapıp parametreleri manuel değiştirebilir
→ Her değişiklikte yeni analiz çalıştırarak OAT simüle edilebilir
→ Sonuçlar dışa aktarılarak Excel/Python'da ileri analiz yapılabilir
```

## İlgili Dosyalar

- [Exergoekonomik Optimizasyon](optimization.md) — Optimizasyon yöntemleri
- [Değerlendirme Kriterleri](evaluation_criteria.md) — f_k, r_k, Ċ_D tanımları
- [Maliyet Denklemleri](cost_equations.md) — PEC korelasyonları ve belirsizlikleri
- [Maliyet Veritabanları](cost_databases.md) — CEPCI ve fiyat kaynakları
- [Seviyelendirilmiş Maliyet](levelized_cost.md) — CRF ve Ż hesaplamaları
- [İleri Exergoekonomik](advanced_exergoeconomic.md) — AV/UN ayrıştırma

## Referanslar

1. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
2. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology for calculating efficiencies..." *Energy*, 31(8-9), 1257-1289.
3. Saltelli, A., et al. (2008). *Global Sensitivity Analysis: The Primer*. Wiley.
4. Smith, R. (2005). *Chemical Process Design and Integration*. Wiley.
5. Türkiye Cumhuriyet Merkez Bankası — Politika faiz oranları ve enflasyon verileri.
