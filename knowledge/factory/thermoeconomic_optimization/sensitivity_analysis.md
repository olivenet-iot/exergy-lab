---
title: "Duyarlılık Analizi (Sensitivity Analysis)"
category: thermoeconomic_optimization
keywords: [duyarlılık analizi, tornado diyagramı, Monte Carlo, senaryo analizi, başabaş analizi, belirsizlik]
related_files: [knowledge/factory/thermoeconomic_optimization/practical_guide.md, knowledge/factory/thermoeconomic_optimization/objective_functions.md, knowledge/factory/thermoeconomic_optimization/trade_off_curves.md]
use_when: ["Optimizasyon sonuçlarının belirsizlik değerlendirmesi gerektiğinde", "Enerji fiyatı ve parametre duyarlılığı analizi yapılırken"]
priority: high
last_updated: 2026-02-02
---

# Duyarlılık Analizi (Sensitivity Analysis)

## 1. Neden Duyarlılık Analizi?

Termoekonomik optimizasyon sonuçları, giriş parametrelerine bağlıdır. Bu parametrelerdeki
belirsizlikler, optimal çözümü ve ekonomik sonuçları önemli ölçüde etkileyebilir.

### Belirsizlik Kaynakları

| Kategori | Parametre | Belirsizlik |
|----------|-----------|-------------|
| Ekonomik | Enerji fiyatı | Yüksek (kur, piyasa) |
| Ekonomik | İskonto oranı | Yüksek (enflasyon, risk) |
| Ekonomik | Ekipman maliyeti | Orta (CEPCI, Türkiye çarpanı) |
| Ekonomik | Karbon fiyatı (CBAM) | Çok yüksek (politik) |
| Operasyonel | Çalışma saati | Orta (talep değişimi) |
| Operasyonel | Yük profili | Orta (mevsimsellik) |
| Teknik | Ekipman verimi degradasyonu | Düşük-Orta |
| Teknik | Isı transfer katsayısı kirlenme | Orta |
| Çevresel | Referans ortam sıcaklığı (T₀) | Düşük-Orta |

---

## 2. Parametre Duyarlılığı (OAT — One-At-a-Time)

### 2.1. Yöntem

Her parametreyi birer birer değiştirerek amaç fonksiyonuna etkisini ölç.

```
Prosedür:
  1. Baz durum parametreleri belirle: p₁°, p₂°, ..., p_n°
  2. Her parametre p_i için:
     a. Alt değer: p_i,low (tipik -20% veya -30%)
     b. Üst değer: p_i,high (tipik +20% veya +30%)
     c. C_total(p_i,low) ve C_total(p_i,high) hesapla
     d. Duyarlılık: S_i = ΔC_total / Δp_i
  3. Sonuçları sırala (en hassas → en az hassas)
```

### 2.2. Tornado Diyagramı

Duyarlılık sonuçlarının görsel sunumu:

```
Parametre           C_total Değişimi [€/yıl]
                    -60k  -40k  -20k   0   +20k  +40k  +60k
                     |     |     |     |     |     |     |
Doğalgaz fiyatı     ████████████████████████████████████████  ← En hassas
İskonto oranı       ██████████████████████████████
Çalışma saati       █████████████████████████
Karbon fiyatı       ███████████████████
Ekipman maliyeti    ████████████████
T₀ (referans)       ██████████
φ (İ&B çarpanı)     ████████
                     |     |     |     |     |     |     |
                   -60k  -40k  -20k   0   +20k  +40k  +60k

Okuma: Çubuk ne kadar geniş → parametre o kadar etkili
```

### 2.3. Tipik Sonuçlar (3,000 kW Kazan Sistemi)

| Parametre | Baz Değer | Alt (-20%) | Üst (+20%) | ΔC_total |
|-----------|-----------|-----------|-----------|----------|
| Doğalgaz fiyatı [€/kWh] | 0.037 | 0.030 | 0.044 | ±102,000 |
| İskonto oranı [%] | 8 | 6.4 | 9.6 | ±8,500 |
| Çalışma saati [h/yıl] | 5,500 | 4,400 | 6,600 | ±85,000 |
| Karbon fiyatı [€/tCO₂] | 50 | 40 | 60 | ±18,000 |
| Ekipman maliyeti [€] | 100,000 | 80,000 | 120,000 | ±4,700 |
| T₀ [°C] | 20 | 15 | 25 | ±3,200 |
| φ (İ&B çarpanı) | 1.06 | 1.04 | 1.08 | ±1,800 |

> **Sonuç:** Enerji fiyatı ve çalışma saati en etkili parametrelerdir. Yatırım maliyeti
> ve İ&B çarpanı çok daha az etkilidir — termoekonomik optimizasyonda ekipman maliyeti
> değil, yakıt maliyeti baskındır.

---

## 3. Senaryo Analizi

### 3.1. Standart Senaryolar

| Senaryo | Enerji Fiyatı | İskonto | Karbon | Çalışma |
|---------|-------------|---------|--------|---------|
| İyimser | -15% | %6 | 30 €/t | +10% |
| Baz durum | 0% | %8 | 50 €/t | 0% |
| Kötümser | +25% | %12 | 80 €/t | -10% |
| Aşırı kötümser | +40% | %15 | 100 €/t | -20% |

### 3.2. Türkiye Spesifik Senaryolar

#### Senaryo A: TL Devalüasyonu

```
Durum: TL %30 değer kaybeder
Etki:
  - Doğalgaz fiyatı (EUR bağlantılı) → +30% TL bazında
  - İthal ekipman maliyeti → +30%
  - Yerli ekipman maliyeti → +10-15%
  - Elektrik fiyatı → +20-25% (kısmen düzenleme)
  - İşçilik → Değişmez (TL bazında)

Sonuç: C_total +25-30% artar
       Optimal nokta: Daha düşük yatırımlı çözüme kayar
       Enerji tasarrufu yatırımları: ROI iyileşir (enerji pahalanır)
```

#### Senaryo B: CBAM Tam Uygulaması (2027+)

```
Durum: AB sınırında karbon vergisi tam uygulanır
Etki (AB'ye ihracat yapan sektörler):
  - Karbon fiyatı: 0 → 80-100 €/tCO₂
  - Çimento: +50-80 €/ton ürün maliyeti
  - Çelik: +100-200 €/ton ürün maliyeti

Sonuç: C_total +15-25% artar (karbon bileşeni)
       Optimal nokta: Yüksek verimli, düşük emisyonlu çözüme kayar
       CHP, ısı geri kazanım: Daha çekici hale gelir
```

#### Senaryo C: Doğalgaz Arz Kesintisi / Fiyat Şoku

```
Durum: Doğalgaz fiyatı %50 artar (küresel enerji krizi)
Etki:
  - Yakıt maliyeti baskın hale gelir
  - Enerji verimliliği yatırımları çok cazip
  - Yakıt değiştirme (fuel switching) opsiyonu

Sonuç: C_total +40% artar
       Optimal nokta: Maksimum verime doğru kayar
       SPP: Tüm verimlilik yatırımlarında kısalır
```

### 3.3. Senaryo Sonuçları Karşılaştırma Tablosu

| Senaryo | C_total [€/yıl] | η_ex,opt [%] | NPV (15 yıl) | SPP [yıl] |
|---------|-----------------|-------------|--------------|-----------|
| İyimser | 430,000 | 30.5 | 380,000 | 1.8 |
| Baz durum | 510,000 | 31.8 | 280,000 | 2.5 |
| Kötümser | 640,000 | 33.2 | 195,000 | 3.2 |
| TL devalüasyon | 660,000 | 32.5 | 210,000 | 2.8 |
| CBAM tam | 620,000 | 34.0 | 320,000 | 2.0 |
| Gaz şoku | 750,000 | 34.5 | 450,000 | 1.2 |

---

## 4. Başabaş Analizi (Breakeven Analysis)

### 4.1. Enerji Fiyatı Başabaş

```
Soru: "Enerji tasarrufu yatırımı hangi enerji fiyatında ekonomik olur?"

Başabaş fiyatı:
  c_fuel,BE = C_invest / (ΔQ_fuel × τ)

Burada:
  C_invest   = Toplam ek yatırım maliyeti [€]
  ΔQ_fuel    = Yakıt tasarrufu [kW]
  τ          = Yıllık çalışma süresi [h/yıl]
```

#### Örnek: Economizer Yatırımı

| Parametre | Değer |
|-----------|-------|
| Ek yatırım | 25,000 € |
| Yakıt tasarrufu | 180 kW |
| Çalışma saati | 5,500 h/yıl |
| **Başabaş fiyatı** | **0.025 €/kWh** |
| Mevcut doğalgaz fiyatı | 0.037 €/kWh |
| **Yatırım ekonomik mi?** | **Evet** (0.037 > 0.025) |

### 4.2. Çalışma Saati Başabaş

```
τ_BE = C_invest / (ΔC_fuel_per_hour)

Örnek:
  C_invest = 25,000 €
  ΔC_fuel/h = 180 × 0.037 = 6.66 €/h
  τ_BE = 25,000 / 6.66 = 3,753 h/yıl

Yorum: 3,753 h/yıl'dan fazla çalışırsa yatırım ekonomik.
       Mevcut 5,500 h/yıl > 3,753 → Ekonomik.
```

### 4.3. Karbon Fiyatı Başabaş

```
Soru: "CHP yatırımı hangi karbon fiyatında ayrı üretimden ucuz olur?"

c_CO₂,BE = (C_CHP - C_ayrı + ΔC_invest) / (ṁ_CO₂,ayrı - ṁ_CO₂,CHP) / τ

Bu analiz, CBAM kararlarında kritiktir.
```

---

## 5. Monte Carlo Simülasyonu

### 5.1. Yöntem

Birden fazla belirsiz parametreyi eşzamanlı olarak rastgele örnekleyerek, sonuçların
istatistiksel dağılımını elde et.

```
Prosedür:
  1. Her belirsiz parametrenin olasılık dağılımını tanımla
  2. N rastgele senaryo üret (tipik N = 5,000-10,000)
  3. Her senaryo için C_total hesapla
  4. Sonuçların istatistiğini analiz et (ortalama, std, yüzdelikler)
```

### 5.2. Türkiye Spesifik Belirsizlik Tablosu

| Parametre | Dağılım | Ortalama | Std/Aralık | Birim |
|-----------|---------|----------|-----------|-------|
| Doğalgaz fiyatı | Log-normal | 0.037 | σ = 0.008 | €/kWh |
| Elektrik fiyatı | Log-normal | 0.11 | σ = 0.025 | €/kWh |
| İskonto oranı | Üçgen | 8% | [6%, 12%] | % |
| Çalışma saati | Normal | 5,500 | σ = 400 | h/yıl |
| Karbon fiyatı | Üçgen | 50 | [0, 100] | €/tCO₂ |
| Ekipman maliyeti (ithal) | Normal | 1.00 | σ = 0.15 | çarpan |
| Ekipman maliyeti (yerli) | Normal | 1.00 | σ = 0.10 | çarpan |
| EUR/TL kuru | Log-normal | güncel | σ = 20% | TL/€ |
| Ekipman ömrü | Üçgen | 15 | [12, 20] | yıl |
| Yük faktörü | Beta | 0.75 | [0.50, 0.95] | oran |

### 5.3. Python İmplementasyonu

```python
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_thermoeconomic(n_simulations=10000):
    """
    Monte Carlo simülasyonu ile termoekonomik belirsizlik analizi.
    3,000 kW kazan sistemi örneği.
    """
    np.random.seed(42)

    # Belirsiz parametreler — rastgele örnekleme
    c_fuel = np.random.lognormal(
        np.log(0.037), 0.20, n_simulations)  # €/kWh
    c_elec = np.random.lognormal(
        np.log(0.11), 0.22, n_simulations)   # €/kWh
    discount_rate = np.random.triangular(
        0.06, 0.08, 0.12, n_simulations)     # oran
    tau = np.random.normal(
        5500, 400, n_simulations)             # h/yıl
    c_CO2 = np.random.triangular(
        0, 50, 100, n_simulations)            # €/tCO₂
    equip_cost_factor = np.random.normal(
        1.0, 0.15, n_simulations)             # çarpan

    # Sabit parametreler
    Q_boiler = 3000  # kW
    eta_ex = 0.318   # optimal exergy verimi
    Q_fuel = Q_boiler / (eta_ex * 3.8)  # yaklaşık yakıt gücü

    # CO₂ emisyonu
    m_CO2 = Q_fuel * 0.202 / 1000  # ton/h

    # Yatırım
    Z_base = 120000  # € (baz ekipman maliyeti)
    n_years = 15

    # Her senaryo için C_total hesapla
    C_fuel = Q_fuel * c_fuel * tau
    CRF = discount_rate * (1 + discount_rate)**n_years / \
          ((1 + discount_rate)**n_years - 1)
    C_invest = CRF * Z_base * equip_cost_factor * 1.06
    C_env = m_CO2 * c_CO2 * tau
    C_total = C_fuel + C_invest + C_env

    # İstatistikler
    print(f"Monte Carlo Sonuçları (n={n_simulations:,}):")
    print(f"  C_total ortalama: {np.mean(C_total):,.0f} €/yıl")
    print(f"  C_total std:      {np.std(C_total):,.0f} €/yıl")
    print(f"  C_total P10:      {np.percentile(C_total, 10):,.0f} €/yıl")
    print(f"  C_total P50:      {np.percentile(C_total, 50):,.0f} €/yıl")
    print(f"  C_total P90:      {np.percentile(C_total, 90):,.0f} €/yıl")

    return C_total

# Çalıştır
C_total = monte_carlo_thermoeconomic()
```

### 5.4. Tipik Monte Carlo Sonuçları

```
Monte Carlo Sonuçları (n=10,000):
  C_total ortalama: 525,000 €/yıl
  C_total std:      85,000 €/yıl
  C_total P10:      420,000 €/yıl
  C_total P50:      515,000 €/yıl
  C_total P90:      640,000 €/yıl

Yorum:
  - %80 olasılıkla C_total, 420,000 ile 640,000 €/yıl arasında
  - Enerji fiyatı belirsizliği en büyük katkıyı yapar
  - Risk-averse karar vericiler P90 değerine bakmalı
```

---

## 6. Robust vs Hassas Çözüm Yorumlama

### 6.1. Tanımlar

```
Hassas (brittle) çözüm:
  - Baz durumda en düşük maliyet
  - Parametre değişimine çok duyarlı
  - Kötü senaryoda ciddi maliyet artışı

Robust (sağlam) çözüm:
  - Baz durumda biraz daha yüksek maliyet
  - Parametre değişimine az duyarlı
  - Tüm senaryolarda kabul edilebilir performans
```

### 6.2. Karşılaştırma Örneği

| Metrik | Çözüm A (Hassas) | Çözüm B (Robust) |
|--------|------------------|-------------------|
| C_total (baz durum) | 450,000 | 465,000 |
| C_total (iyimser) | 380,000 | 410,000 |
| C_total (kötümser) | 680,000 | 540,000 |
| C_total (P90, MC) | 650,000 | 530,000 |
| Maks-min farkı | 300,000 | 130,000 |
| **Tavsiye** | Risk seven | **Çoğu durumda tercih** |

### 6.3. Robustness İndeksi

```
RI = (C_total,P90 - C_total,P10) / C_total,P50

RI < 0.3: Yüksek robustness → Güvenli yatırım
RI 0.3-0.5: Orta robustness → Dikkatli değerlendir
RI > 0.5: Düşük robustness → Risk analizi gerekir
```

---

## 7. Duyarlılık Analizi Uygulama Rehberi

### 7.1. Ne Zaman Hangi Yöntem?

| Yöntem | Parametre Sayısı | Etkileşim | Hesaplama | Kullanım |
|--------|-----------------|-----------|-----------|----------|
| OAT (tornado) | 3-10 | Hayır | Düşük | Hızlı tarama |
| Senaryo analizi | 3-5 | Kısmen | Düşük | Stratejik planlama |
| Başabaş | 1-2 | Hayır | Çok düşük | Karar eşikleri |
| Monte Carlo | 5-15 | Evet | Yüksek | Kapsamlı belirsizlik |

### 7.2. Minimum Rapor İçeriği

Her termoekonomik optimizasyon raporunda bulunması gereken duyarlılık analizleri:

1. **Enerji fiyatı duyarlılığı** (±20-30%) — zorunlu
2. **Çalışma saati duyarlılığı** (±20%) — zorunlu
3. **İskonto oranı duyarlılığı** — önerilir
4. **Karbon fiyatı senaryoları** (CBAM etkili sektörlerde zorunlu)
5. **Monte Carlo** (büyük yatırımlarda, >200k €, önerilir)
6. **Tornado diyagramı** — her durumda önerilir

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `objective_functions.md` — Maliyet bileşenleri
- `practical_guide.md` — Endüstriyel uygulama rehberi
- `trade_off_curves.md` — Ödünleşim eğrileri
- `factory/economic_analysis.md` — NPV, IRR hesaplama

## Referanslar

- Saltelli, A. et al. (2008). *Global Sensitivity Analysis*. Wiley.
- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- Rubinstein, R.Y. & Kroese, D.P. (2016). *Simulation and the Monte Carlo Method*. 3rd ed. Wiley.
