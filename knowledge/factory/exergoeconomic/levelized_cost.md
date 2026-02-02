---
title: "Seviyelendirilmiş Maliyet Hesabı (Levelized Cost — CRF & Z-dot)"
category: factory
equipment_type: factory
keywords: [CRF, seviyelendirilmiş maliyet, Z-dot, sermaye geri kazanım, yatırım maliyeti]
related_files:
  - factory/exergoeconomic/cost_equations.md
  - factory/exergoeconomic/cost_databases.md
  - factory/exergoeconomic/exergoeconomic_balance.md
  - factory/economic_analysis.md
use_when:
  - "CRF hesaplanırken"
  - "Z-dot (seviyelendirilmiş maliyet akışı) hesaplanırken"
  - "CI ve OM bileşenleri ayrılırken"
  - "Yatırım ömrü ve faiz oranı belirlenirken"
priority: high
last_updated: 2026-02-01
---
# Seviyelendirilmiş Maliyet Hesabı (Levelized Cost — CRF & Z-dot)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Exergoekonomik analizde ekipman maliyetleri, saatlik maliyet akışına (Ż — "Z-dot") dönüştürülür. Bu, tek seferlik yatırım maliyetini (PEC) yıllık ve saatlik bazda seviyelendirerek exergy maliyet akışları (Ċ) ile doğrudan karşılaştırılabilir hale getirir.

```
Temel Dönüşüm Zinciri:

PEC [€] → TCI [€] → Yıllık maliyet [€/yıl] → Ż [€/saat]

Adımlar:
1. PEC → TCI (toplam yatırım maliyeti)
2. TCI → CRF × TCI (yıllık seviyelendirilmiş maliyet)
3. Yıllık maliyet / τ = Ż (saatlik maliyet akışı)
```

## 2. Sermaye Geri Kazanım Faktörü (CRF — Capital Recovery Factor)

### 2.1 Formül ve Türetimi

```
CRF = i · (1 + i)^n / ((1 + i)^n - 1)

Burada:
- i = İskonto oranı (reel faiz oranı) [-]
- n = Ekipman ekonomik ömrü [yıl]

Türetim:
  CRF, eşit yıllık ödeme serisinin bugünkü değerinden türetilir:
  PV = A × [(1+i)^n - 1] / [i·(1+i)^n]
  A = PV × CRF
  → CRF = 1 / Σ(1/(1+i)^t) for t=1 to n
```

### 2.2 CRF Hesaplama Tablosu

| i \ n | 5 yıl | 10 yıl | 15 yıl | 20 yıl | 25 yıl | 30 yıl |
|-------|-------|--------|--------|--------|--------|--------|
| %5 | 0.2310 | 0.1295 | 0.0963 | 0.0802 | 0.0710 | 0.0651 |
| %6 | 0.2374 | 0.1359 | 0.1030 | 0.0872 | 0.0782 | 0.0726 |
| %7 | 0.2439 | 0.1424 | 0.1098 | 0.0944 | 0.0858 | 0.0806 |
| %8 | 0.2505 | 0.1490 | 0.1168 | 0.1019 | 0.0937 | 0.0888 |
| %9 | 0.2571 | 0.1558 | 0.1241 | 0.1095 | 0.1018 | 0.0973 |
| **%10** | **0.2638** | **0.1627** | **0.1315** | **0.1175** | **0.1102** | **0.1061** |
| %11 | 0.2706 | 0.1698 | 0.1391 | 0.1256 | 0.1187 | 0.1150 |
| %12 | 0.2774 | 0.1770 | 0.1468 | 0.1339 | 0.1275 | 0.1241 |
| %14 | 0.2913 | 0.1917 | 0.1628 | 0.1510 | 0.1455 | 0.1428 |
| %15 | 0.2983 | 0.1993 | 0.1710 | 0.1598 | 0.1547 | 0.1523 |
| %18 | 0.3198 | 0.2225 | 0.1964 | 0.1868 | 0.1829 | 0.1813 |
| %20 | 0.3344 | 0.2385 | 0.2139 | 0.2054 | 0.2021 | 0.2008 |

> **ExergyLab önerisi:** i = %10, n = 20 yıl → CRF = 0.1175

### 2.3 Ekipman Türüne Göre Ekonomik Ömür

| Ekipman | Tipik Ömür [yıl] | Aralık | Not |
|---------|-------------------|--------|-----|
| Kompresör | 15-20 | 10-25 | VSD ömrü daha kısa |
| Türbin (buhar) | 25-30 | 20-35 | Bakıma bağlı |
| Türbin (gaz) | 20-25 | 15-30 | Hot section ömrü |
| Kazan | 20-25 | 15-30 | Tüp ömrü kritik |
| Isı değiştirici | 15-20 | 10-25 | Korozyona bağlı |
| Pompa | 15-20 | 10-25 | — |
| Chiller | 15-20 | 12-25 | Kompresöre bağlı |
| Kondenser | 15-20 | 10-25 | — |
| Soğutma kulesi | 20-25 | 15-30 | Malzemeye bağlı |
| Boru/vana | 25-30 | 20-40 | — |

## 3. Z-dot (Ż) Hesaplaması

### 3.1 Temel Formül

```
Ż_k = Ż_CI,k + Ż_OM,k  [€/saat]

Burada:
- Ż_CI,k = Sermaye yatırım (Capital Investment) bileşeni
- Ż_OM,k = İşletme ve bakım (Operating & Maintenance) bileşeni
```

### 3.2 CI Bileşeni

```
Ż_CI,k = (CRF × TCI_k) / τ  [€/saat]

Burada:
- CRF = Sermaye geri kazanım faktörü [-]
- TCI_k = k. bileşenin toplam yatırım maliyeti [€]
- τ = Yıllık çalışma saati [saat/yıl]

TCI hesabı:
  TCI = PEC × φ_TCI

  φ_TCI değerleri:
  Yeni tesis (grassroots):  φ_TCI = 4.0-6.0
  Retrofit (ekleme):        φ_TCI = 2.5-3.5
  Modifikasyon:             φ_TCI = 1.5-2.0
  Sadece ekipman:           φ_TCI = 1.0 (PEC = TCI)
```

### 3.3 OM Bileşeni

```
Yöntem A — PEC yüzdesi:
  Ż_OM,k = (γ_k × PEC_k) / τ  [€/saat]

  γ_k değerleri:
  Kompresör:    γ = 0.03-0.05 (%3-5/yıl)
  Türbin:       γ = 0.03-0.06
  Kazan:        γ = 0.02-0.04
  HX:           γ = 0.01-0.03
  Pompa:        γ = 0.02-0.04
  Chiller:      γ = 0.03-0.05

Yöntem B — CI oranı:
  Ż_OM,k = φ_OM × Ż_CI,k

  φ_OM = 0.3-0.6 (tipik)
  → Ż_k = Ż_CI,k × (1 + φ_OM)

Yöntem C — Detaylı (büyük sistemler):
  Ż_OM = (İşçilik + Yedek parça + Sarf malzeme + Sigorta + Genel gider) / τ
```

### 3.4 Toplam Ż

```
Ż_k = Ż_CI,k + Ż_OM,k

Basitleştirilmiş (Yöntem B):
Ż_k = CRF × TCI_k × (1 + φ_OM) / τ

En basit (PEC bazlı, φ_TCI = 1):
Ż_k = CRF × PEC_k × (1 + φ_OM) / τ
```

## 4. Tam Hesaplama Örneği

### 4.1 Veriler

```
Ekipman: Vidalı kompresör
PEC = 75,000 €
i = %10 (reel, EUR bazlı)
n = 20 yıl
τ = 7,500 saat/yıl
φ_TCI = 2.5 (retrofit)
γ = 0.04 (%4 bakım)
```

### 4.2 Adım Adım Hesaplama

```
Adım 1: CRF
  CRF = 0.10 × (1.10)^20 / ((1.10)^20 - 1)
  CRF = 0.10 × 6.7275 / (6.7275 - 1)
  CRF = 0.6728 / 5.7275
  CRF = 0.1175

Adım 2: TCI
  TCI = PEC × φ_TCI = 75,000 × 2.5 = 187,500 €

Adım 3: Ż_CI
  Ż_CI = CRF × TCI / τ
  Ż_CI = 0.1175 × 187,500 / 7,500
  Ż_CI = 22,031 / 7,500
  Ż_CI = 2.937 €/saat

Adım 4: Ż_OM
  Ż_OM = γ × PEC / τ
  Ż_OM = 0.04 × 75,000 / 7,500
  Ż_OM = 3,000 / 7,500
  Ż_OM = 0.400 €/saat

Adım 5: Ż_toplam
  Ż = Ż_CI + Ż_OM = 2.937 + 0.400 = 3.337 €/saat

Kontrol:
  Yıllık: 3.337 × 7,500 = 25,028 €/yıl
  PEC'in %'si: 25,028 / 75,000 = %33.4/yıl
```

### 4.3 Exergoekonomik Bağlam

```
Bu kompresör için:
  Ė_D = 25 kW (exergy analizi sonucu)
  c_F = c_elektrik = 0.025 ×10⁻³ €/kJ

  Ċ_D = c_F × Ė_D = 0.000025 × 25 = 0.000625 €/s = 2.25 €/saat

  f_k = Ż / (Ż + Ċ_D) = 3.337 / (3.337 + 2.250) = 0.597

  Yorum: f_k = 0.60 → Dengeli bölge (Ż biraz baskın)
  → Termodinamik iyileştirme potansiyeli orta düzeyde
  → Daha ucuz alternatif değerlendirilebilir
```

## 5. Parametrik Duyarlılık

### 5.1 CRF Duyarlılığı

```
i = %10 sabit, n değişken:
  n = 10 → CRF = 0.1627 → Ż ↑%38.5 (referans: n=20)
  n = 15 → CRF = 0.1315 → Ż ↑%11.9
  n = 20 → CRF = 0.1175 → Ż = referans
  n = 25 → CRF = 0.1102 → Ż ↓%6.2
  n = 30 → CRF = 0.1061 → Ż ↓%9.7

n = 20 sabit, i değişken:
  i = %5  → CRF = 0.0802 → Ż ↓%31.7
  i = %8  → CRF = 0.1019 → Ż ↓%13.3
  i = %10 → CRF = 0.1175 → Ż = referans
  i = %12 → CRF = 0.1339 → Ż ↑%14.0
  i = %15 → CRF = 0.1598 → Ż ↑%36.0
```

### 5.2 τ (Çalışma Saati) Etkisi

```
τ doğrudan Ż'yi etkiler (ters orantılı):

  τ = 4,000 saat → Ż ↑%87.5 (referans: 7,500)
  τ = 6,000 saat → Ż ↑%25.0
  τ = 7,500 saat → Ż = referans
  τ = 8,000 saat → Ż ↓%6.25
  τ = 8,760 saat → Ż ↓%14.4

Önemli: Düşük τ, Ż'yi artırır → f_k artar → Termodinamik iyileştirme daha az öncelikli görünür
→ Bu yanıltıcı olabilir, τ düzeltmesi yapılmalı
```

## 6. Çoklu Ekipman Sistemi İçin Ż Hesaplama

### 6.1 Fabrika Seviyesi Ż Tablosu Şablonu

| Bileşen | PEC [€] | TCI [€] | CRF | Ż_CI [€/h] | Ż_OM [€/h] | Ż_toplam [€/h] |
|---------|---------|---------|-----|-------------|-------------|-----------------|
| Kazan | — | — | — | — | — | — |
| Kompresör | — | — | — | — | — | — |
| Chiller | — | — | — | — | — | — |
| Pompa | — | — | — | — | — | — |
| HX | — | — | — | — | — | — |
| **TOPLAM** | — | — | — | — | — | — |

### 6.2 Toplu Hesaplama Formülü

```
Tüm bileşenler aynı i, n, τ kullanıyorsa:

Ż_k = PEC_k × φ_TCI × CRF × (1 + φ_OM) / τ

Sayısal katsayı (tipik değerler: i=%10, n=20, τ=7500, φ_TCI=2.5, φ_OM=0.4):
  Ż_k = PEC_k × 2.5 × 0.1175 × 1.4 / 7500
  Ż_k = PEC_k × 5.48 × 10⁻⁵  [€/saat per € PEC]

Pratik kural:
  Ż [€/saat] ≈ PEC [€] × 0.0000548
  veya
  Ż [€/saat] ≈ PEC [€] / 18,250
```

## 7. Özel Durumlar

### 7.1 Farklı Ekonomik Ömürlü Bileşenler

```
Bileşenler farklı n değerine sahipse:
  Her bileşen için ayrı CRF hesapla:
  CRF_kazan (n=25), CRF_pompa (n=15), CRF_HX (n=20)

  veya

  Ağırlıklı ortalama CRF kullan:
  CRF_ort = Σ(CRF_k × TCI_k) / Σ(TCI_k)
```

### 7.2 Mevcut (Amortisman Tamamlanmış) Ekipman

```
Mevcut ekipman için iki yaklaşım:

Yaklaşım A — Tam maliyet (önerilen):
  TCI yerine yerine koyma maliyeti (replacement cost) kullan
  → Fırsat maliyeti yansıtılır

Yaklaşım B — Kalan değer:
  TCI yerine kalan defter değeri kullan
  → Daha düşük Ż, gerçekçi olmayabilir

ExergyLab önerisi: Yaklaşım A (yerine koyma maliyeti)
```

### 7.3 Kira/Leasing ile Edinim

```
Kiralanan ekipman:
  Ż_CI yerine kira bedeli kullanılır:
  Ż_kira = Kira_yıllık / τ  [€/saat]

  Ż_OM ayrıca hesaplanır (bakım kiracıya aitse)
```

## 8. Türkiye'ye Özel Parametreler — Özet

```
ExergyLab Türkiye Parametre Seti:

Faiz oranı (reel, EUR bazlı): i = 0.10 (%10)
Ekonomik ömür: n = 20 yıl (genel)
CRF: 0.1175
Çalışma saati: τ = 7,500 saat/yıl (tipik endüstriyel)
TCI faktörü: φ_TCI = 2.5 (retrofit)
OM faktörü: φ_OM = 0.4

Hızlı hesaplama:
  Ż [€/saat] ≈ PEC [€] / 18,250
  Ż [€/yıl] ≈ PEC [€] × 0.411
```

## İlgili Dosyalar

- `factory/exergoeconomic/cost_equations.md` — PEC korelasyonları
- `factory/exergoeconomic/cost_databases.md` — CEPCI, fiyat verileri
- `factory/exergoeconomic/exergoeconomic_balance.md` — Ż'nin maliyet dengesindeki kullanımı
- `factory/exergoeconomic/evaluation_criteria.md` — f_k hesaplaması (Ż / (Ż + Ċ_D))
- `factory/economic_analysis.md` — SPP, NPV, IRR yöntemleri

## Referanslar

1. Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*. Wiley. Section 8.2.
2. Lazzaretto, A., Tsatsaronis, G. (2006). "SPECO: A systematic and general methodology..." *Energy*, 31(8-9), 1257-1289.
3. Turton, R., et al. (2012). *Analysis, Synthesis, and Design of Chemical Processes*. 4th Ed. Chapter 9.
4. Peters, M.S., Timmerhaus, K.D., West, R.E. (2003). *Plant Design and Economics for Chemical Engineers*. 5th Ed.
5. EPDK (2024). Türkiye enerji tarifeleri. epdk.gov.tr
6. TCMB (2024). Faiz oranları ve makroekonomik göstergeler. tcmb.gov.tr
