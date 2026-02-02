---
title: "M&V İstatistiksel Yöntemler (M&V Statistical Methods)"
category: factory
equipment_type: factory
keywords: [regresyon analizi, ASHRAE Guideline 14, CV-RMSE, NMBE, belirsizlik, güven aralığı, HDD, CDD, derece-gün, t-testi, F-testi]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/mv_ipmvp.md, factory/energy_management/mv_planning.md, factory/energy_management/baseline_enpi.md, factory/energy_management/cusum_analysis.md, factory/measurement_verification.md]
use_when: ["M&V regresyon analizi yapılacağında", "Model doğrulama kriterleri sorgulandığında", "Belirsizlik hesaplanacağında", "HDD/CDD analizi gerektiğinde"]
priority: medium
last_updated: 2026-02-01
---

# M&V İstatistiksel Yöntemler (M&V Statistical Methods)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

İstatistiksel yöntemler, M&V (Measurement & Verification) sürecinin teknik temelini oluşturur. Enerji tüketimi ile bağımsız değişkenler arasındaki ilişkiyi modellemek, modelin güvenilirliğini doğrulamak ve tasarrufun belirsizliğini hesaplamak için istatistiksel araçlar kullanılır.

### 1.1 Temel Referanslar

- **ASHRAE Guideline 14-2014:** M&V istatistiksel kriterlerinin temel kaynağı
- **IPMVP Core Concepts 2022, Annex B:** Belirsizlik analizi çerçevesi
- **ISO 50015:2014:** Enerji performansının ölçülmesi ve doğrulanması

### 1.2 İstatistiksel Yöntemlerin M&V'deki Rolü

```
M&V İstatistiksel Süreç Akışı:
═══════════════════════════════════════════════════════════
[Veri Toplama] → [Keşifsel Analiz] → [Model Kurma]
                                           ↓
[Raporlama] ← [Belirsizlik Hesabı] ← [Model Doğrulama]
═══════════════════════════════════════════════════════════
```

## 2. Regresyon Analizi Temelleri (Regression Analysis Fundamentals)

### 2.1 Basit Doğrusal Regresyon (Simple Linear Regression)

Tek bağımsız değişken ile enerji tüketimi arasındaki ilişki:

```
Model:
  E = a + b × V + ε

Burada:
  E : Enerji tüketimi [kWh/dönem]
  V : Bağımsız değişken (üretim hacmi, HDD, CDD vb.)
  a : Sabit terim (kesim noktası — intercept)
  b : Eğim katsayısı (slope)
  ε : Hata terimi (rastgele, N(0, σ²) dağılımlı)
```

### 2.2 Çoklu Doğrusal Regresyon (Multiple Linear Regression)

Birden fazla bağımsız değişken ile model:

```
Model:
  E = a + b₁V₁ + b₂V₂ + ... + bₖVₖ + ε

Örnek (endüstriyel tesis):
  E = a + b₁ × Üretim + b₂ × HDD + b₃ × CDD + b₄ × Çalışma_Saati
```

### 2.3 OLS (Ordinary Least Squares) Yöntemi

Regresyon katsayılarının hesaplanması:

```
OLS Formülleri (Basit Doğrusal):
─────────────────────────────────────────────
b = Σ(Vᵢ − V̄)(Eᵢ − Ē) / Σ(Vᵢ − V̄)²

a = Ē − b × V̄

Matris Formu (Çoklu):
β̂ = (XᵀX)⁻¹ Xᵀy

Burada:
  X : Bağımsız değişkenler matrisi (n × k+1)
  y : Bağımlı değişken vektörü (n × 1)
  β̂ : Katsayılar vektörü [(k+1) × 1]
─────────────────────────────────────────────
```

### 2.4 Değişken Seçimi (Variable Selection)

| Yöntem | Açıklama | Avantaj | Dezavantaj |
|---|---|---|---|
| Forward Selection | Boş modelden başla, en anlamlı değişkeni ekle | Basit | Etkileşimleri kaçırabilir |
| Backward Elimination | Tam modelden başla, en anlamsız değişkeni çıkar | Kapsamlı | Çok değişkende yavaş |
| Stepwise | Forward + Backward kombinasyonu | Dengeli | Yerel optimuma takılabilir |
| Best Subset | Tüm kombinasyonları değerlendir | Optimal | k > 15 için pratik değil |

**Değişken Seçim Kriterleri:**
- p-value < 0.05 (istatistiksel anlamlılık)
- Fiziksel anlamlılık (enerji mühendisliği perspektifi)
- VIF < 10 (çoklu doğrusal bağlılık kontrolü)
- Adjusted R² artışı anlamlı olmalı

### 2.5 Korelasyon Matrisi (Correlation Matrix)

Değişkenler arası ilişkiyi değerlendirmek için Pearson korelasyon katsayısı:

```
Korelasyon Katsayısı:
─────────────────────────────────────────────
r = Σ(xᵢ − x̄)(yᵢ − ȳ) / √[Σ(xᵢ − x̄)² × Σ(yᵢ − ȳ)²]

Yorumlama:
  |r| > 0.8  : Güçlü korelasyon
  0.5 < |r| ≤ 0.8 : Orta korelasyon
  |r| ≤ 0.5  : Zayıf korelasyon
─────────────────────────────────────────────
```

### 2.6 Temel İstatistiksel Metrikler

```
R² (Belirtme Katsayısı — Coefficient of Determination):
  R² = 1 − (SS_res / SS_tot)
  SS_res = Σ(Eᵢ − Êᵢ)²     (artık kareler toplamı)
  SS_tot = Σ(Eᵢ − Ē)²       (toplam kareler toplamı)

Adjusted R² (Düzeltilmiş R²):
  R²_adj = 1 − [(1 − R²)(n − 1) / (n − k − 1)]

  Burada:
    n : Gözlem sayısı
    k : Bağımsız değişken sayısı

p-value:
  H₀: βⱼ = 0 (değişken anlamsız)
  H₁: βⱼ ≠ 0 (değişken anlamlı)
  p-value < 0.05 → H₀ reddedilir → değişken anlamlıdır

t-istatistiği:
  t = β̂ⱼ / SE(β̂ⱼ)
  SE(β̂ⱼ) = √[MSE × (XᵀX)⁻¹ⱼⱼ]
```

## 3. ASHRAE Guideline 14 Kriterleri (ASHRAE Guideline 14 Criteria)

ASHRAE Guideline 14-2014, M&V modellerinin doğrulanması için endüstri standardı istatistiksel kriterleri tanımlar.

### 3.1 CV(RMSE) — Coefficient of Variation of Root Mean Square Error

```
CV(RMSE) Formülü:
─────────────────────────────────────────────
            √[Σ(Eᵢ − Êᵢ)² / (n − p)]
CV(RMSE) = ────────────────────────────── × 100  [%]
                      Ē

Burada:
  Eᵢ  : Gözlemlenen enerji tüketimi [kWh]
  Êᵢ  : Model tahmini [kWh]
  n   : Gözlem sayısı
  p   : Model parametresi sayısı (katsayı sayısı)
  Ē   : Ortalama gözlemlenen tüketim [kWh]
─────────────────────────────────────────────

Limitler:
  Aylık veri : CV(RMSE) ≤ %25
  Günlük veri: CV(RMSE) ≤ %30  (bazı kaynaklarda %35)
  Saatlik veri: CV(RMSE) ≤ %30

Anlam: Modelin ortalama tahmin hatasının yüzdesi.
Düşük CV(RMSE) → Model tahminleri gerçek verilere yakın.
```

### 3.2 NMBE — Normalized Mean Bias Error

```
NMBE Formülü:
─────────────────────────────────────────────
         Σ(Eᵢ − Êᵢ) / (n − p)
NMBE = ─────────────────────────── × 100  [%]
                  Ē

Limitler:
  Aylık veri : NMBE ≤ ±%0.5  (sıkı kriter)
  Günlük veri: NMBE ≤ ±%10

Anlam: Modelin sistematik sapma (bias) düzeyi.
Pozitif NMBE → Model düşük tahmin ediyor (underprediction)
Negatif NMBE → Model yüksek tahmin ediyor (overprediction)
─────────────────────────────────────────────
```

### 3.3 R² Kriteri

```
Minimum Gereksinim:
  R² ≥ 0.75

Yorumlama:
  R² = 0.75 : Modelin bağımsız değişkenlerle açıklayabildiği
               varyans oranı %75
  R² = 0.90 : Çok iyi model uyumu
  R² = 0.95+: Mükemmel uyum (overfitting riski kontrol edilmeli)
```

### 3.4 Kriterlerin Özet Tablosu

| Kriter | Aylık Veri | Günlük Veri | Saatlik Veri | Anlam |
|---|---|---|---|---|
| CV(RMSE) | ≤ %25 | ≤ %30 | ≤ %30 | Tahmin doğruluğu |
| NMBE | ≤ ±%0.5 | ≤ ±%10 | ≤ ±%10 | Sistematik sapma |
| R² | ≥ 0.75 | ≥ 0.75 | ≥ 0.75 | Açıklanan varyans |
| n (min) | ≥ 12 | ≥ 90 | ≥ 2160 | Örneklem büyüklüğü |

> **Önemli:** Tüm kriterlerin **aynı anda** sağlanması gerekir. Tek bir kriterin ihlali modelin revize edilmesini gerektirir.

## 4. Model Diagnostik (Model Diagnostics)

### 4.1 Artık (Residual) Analizi

Artıklar (eᵢ = Eᵢ − Êᵢ) aşağıdaki varsayımları karşılamalıdır:

| Varsayım | Test | Kriter | Yorum |
|---|---|---|---|
| Rastgelelik (Independence) | Durbin-Watson | 1.5 < DW < 2.5 | Otokorelasyon yok |
| Normallik (Normality) | Shapiro-Wilk | p > 0.05 | Normal dağılım |
| Homojenlik (Homoscedasticity) | Breusch-Pagan | p > 0.05 | Sabit varyans |
| Sıfır ortalamalılık | Histogram/Q-Q plot | E(eᵢ) ≈ 0 | Sistematik sapma yok |

### 4.2 Durbin-Watson Testi (Autocorrelation)

```
Durbin-Watson İstatistiği:
─────────────────────────────────────────────
DW = Σ(eᵢ − eᵢ₋₁)² / Σeᵢ²     (i = 2, ..., n)

Yorumlama:
  DW ≈ 2.0 : Otokorelasyon yok (ideal)
  DW < 1.5 : Pozitif otokorelasyon var → Model yapısı yetersiz
  DW > 2.5 : Negatif otokorelasyon var → Aşırı uyum riski

Çözüm (otokorelasyon varsa):
  - Gecikme (lag) değişkeni ekle
  - Fark (differencing) uygula
  - ARIMA tipi model düşün
─────────────────────────────────────────────
```

### 4.3 Outlier (Aykırı Değer) Tespiti

**Cook's Distance (Cook's D):**

```
Cook's Distance:
─────────────────────────────────────────────
Dᵢ = (Êᵢ − Ê₍ᵢ₎)² / (p × MSE)

Burada:
  Ê₍ᵢ₎ : i. gözlem çıkarıldığında elde edilen tahmin
  p    : Parametre sayısı
  MSE  : Ortalama kare hata

Kural: Dᵢ > 4/n → i. gözlem etkili (influential) noktadır
       Dᵢ > 1.0 → Ciddi aykırı değer, incelenmeli
─────────────────────────────────────────────
```

**Leverage (Kaldıraç):**

```
Leverage Değeri:
  hᵢᵢ = [H]ᵢᵢ  (Hat matrisi köşegen elemanı)
  H = X(XᵀX)⁻¹Xᵀ

Kural: hᵢᵢ > 2(p+1)/n → Yüksek kaldıraçlı nokta
```

### 4.4 Çoklu Doğrusal Bağlılık (Multicollinearity — VIF)

```
VIF (Variance Inflation Factor):
─────────────────────────────────────────────
VIFⱼ = 1 / (1 − R²ⱼ)

Burada R²ⱼ : j. değişkenin diğer bağımsız değişkenlerle
              regresyonunun R² değeri

Yorumlama:
  VIF < 5  : Kabul edilebilir
  5 ≤ VIF < 10 : Dikkatli olunmalı
  VIF ≥ 10 : Ciddi multicollinearity → Değişken çıkarılmalı

Çözüm: Korelasyonlu değişkenlerden birini çıkar veya
        PCA (Principal Component Analysis) uygula
─────────────────────────────────────────────
```

## 5. Belirsizlik Analizi (Uncertainty Analysis)

### 5.1 Tasarruf Belirsizliği Çerçevesi

IPMVP'ye göre, doğrulanmış tasarruf bir belirsizlik aralığı ile raporlanmalıdır:

```
Tasarruf = Ŝ ± U_s     (belirli bir güven düzeyinde)

Burada:
  Ŝ  : Hesaplanan tasarruf (noktasal tahmin)
  U_s : Tasarruf belirsizliği
```

### 5.2 Belirsizlik Bileşenleri

Toplam belirsizlik iki ana bileşenden oluşur:

```
Toplam Belirsizlik:
─────────────────────────────────────────────
U_toplam = √(U_ölçüm² + U_model²)

U_ölçüm : Ölçüm cihazı belirsizliği (instrument uncertainty)
U_model  : İstatistiksel model belirsizliği (sampling uncertainty)

Model Belirsizliği (IPMVP Annex B):
U_model = t(n−p, α/2) × (CV(RMSE)/100) × Ē × √(m/n) × F

Burada:
  t(n−p, α/2) : t-dağılımı kritik değeri
  m            : Raporlama dönemindeki gözlem sayısı
  n            : Baseline dönemindeki gözlem sayısı
  F            : Düzeltme faktörü
─────────────────────────────────────────────
```

### 5.3 Güven Aralığı (Confidence Interval)

| Güven Düzeyi | α | t kritik (df=∞) | Kullanım |
|---|---|---|---|
| %80 | 0.20 | 1.282 | Ön fizibilite |
| %90 | 0.10 | 1.645 | IPMVP önerisi |
| %95 | 0.05 | 1.960 | ESCO sözleşmesi |
| %99 | 0.01 | 2.576 | Yasal gereksinim |

### 5.4 Çalışılmış Örnek — Belirsizlik Hesaplama

```
Örnek: VSD Pompa Retrofit — Aylık M&V
═══════════════════════════════════════════════
Veriler:
  Baseline dönem    : n = 12 ay
  Raporlama dönem   : m = 12 ay
  CV(RMSE)          : 14.2%
  Ē (baseline ort)  : 44.000 kWh/ay
  Hesaplanan tasarruf: Ŝ = 15.400 kWh/ay
  Güven düzeyi      : %90
  Serbestlik derecesi: df = 12 − 3 = 9
  t(9, 0.05)        : 1.833

Model Belirsizliği:
  U_model = 1.833 × (14.2/100) × 44.000 × √(12/12) × 1.0
  U_model = 1.833 × 0.142 × 44.000
  U_model = 11.454 kWh/ay (yıllık: 137.448 kWh)

Ölçüm Belirsizliği (güç analizörü ±0.5%):
  U_ölçüm = 0.005 × 44.000 = 220 kWh/ay

Toplam Belirsizlik:
  U_toplam = √(11.454² + 220²) = √(131.194.116 + 48.400)
  U_toplam ≈ 11.456 kWh/ay

Göreceli Belirsizlik:
  U_göreceli = U_toplam / Ŝ × 100 = 11.456 / 15.400 × 100 = %74.4

Sonuç:
  Tasarruf = 15.400 ± 11.456 kWh/ay (%90 güvenle)
  veya: 3.944 — 26.856 kWh/ay aralığında

NOT: Göreceli belirsizlik yüksek (%74) — bu modelin
iyileştirilmesi veya ölçüm süresinin uzatılması gerektiğini
gösterir. IPMVP ≤ %50 göreceli belirsizlik önerir.
═══════════════════════════════════════════════
```

### 5.5 Belirsizliği Azaltma Stratejileri

| Strateji | Etki | Açıklama |
|---|---|---|
| Gözlem sayısını artır | U_model ↓ | √(m/n) faktörü düşer |
| Model doğruluğunu artır | U_model ↓ | CV(RMSE) düşer |
| Daha doğru cihaz kullan | U_ölçüm ↓ | Cihaz belirsizliği düşer |
| Ölçüm sıklığını artır | U_model ↓ | Daha fazla veri noktası |
| Daha iyi değişken seç | U_model ↓ | R² artar, CV(RMSE) düşer |

## 6. Derece-Gün Analizi (Degree-Day Analysis — HDD/CDD)

### 6.1 Tanımlar

```
Isıtma Derece-Gün (Heating Degree Day — HDD):
─────────────────────────────────────────────
HDD_gün = max(T_baz − T_ort,gün , 0)
HDD_ay  = Σ HDD_gün (ay boyunca)
HDD_yıl = Σ HDD_ay  (yıl boyunca)

Soğutma Derece-Gün (Cooling Degree Day — CDD):
─────────────────────────────────────────────
CDD_gün = max(T_ort,gün − T_baz , 0)
CDD_ay  = Σ CDD_gün (ay boyunca)
CDD_yıl = Σ CDD_ay  (yıl boyunca)

Burada:
  T_baz    : Baz sıcaklık [°C]
  T_ort,gün: Günlük ortalama dış sıcaklık [°C]
─────────────────────────────────────────────
```

### 6.2 Baz Sıcaklık Seçimi (Base Temperature)

| Amaç | Türkiye Standart | Avrupa Standart | Açıklama |
|---|---|---|---|
| Isıtma (HDD) | 18°C | 15.5°C (UK), 18°C (Kıta Avrupası) | İç mekan kazancı dikkate alınır |
| Soğutma (CDD) | 24°C | 18°C (bazı kaynaklarda) | İç mekan yükü bağımlı |
| Endüstriyel proses | Proses sıcaklığına göre | — | Özel hesaplama gerekir |

> **Not:** Baz sıcaklık, binanın veya prosesin özelliklerine göre optimize edilebilir. Değişim noktası (change-point) analizi ile optimal baz sıcaklık bulunabilir.

### 6.3 Enerji-Derece Gün Regresyonu

```
Model Tipleri:
─────────────────────────────────────────────
Sadece ısıtma:   E = a + b × HDD
Sadece soğutma:  E = a + b × CDD
Her ikisi:       E = a + b₁ × HDD + b₂ × CDD
Üretimle birlikte: E = a + b₁ × HDD + b₂ × CDD + b₃ × Üretim
─────────────────────────────────────────────
```

### 6.4 Türkiye Büyük Şehirler HDD/CDD Referans Tablosu

Aşağıdaki değerler uzun yıllar ortalamasıdır (baz sıcaklık: ısıtma 18°C, soğutma 24°C):

| Şehir | HDD (°C·gün/yıl) | CDD (°C·gün/yıl) | İklim Bölgesi | Karakter |
|---|---|---|---|---|
| İstanbul | 1.680 | 95 | Geçiş bölgesi | Isıtma ağırlıklı |
| Ankara | 2.710 | 55 | Karasal | Yoğun ısıtma |
| İzmir | 1.180 | 230 | Akdeniz | Dengeli |
| Bursa | 1.850 | 120 | Marmara | Isıtma ağırlıklı |
| Antalya | 680 | 350 | Sıcak Akdeniz | Soğutma ağırlıklı |
| Adana | 780 | 480 | Sıcak Akdeniz | Soğutma ağırlıklı |
| Kayseri | 3.020 | 35 | Yüksek karasal | Çok yoğun ısıtma |
| Gaziantep | 2.150 | 210 | Güneydoğu | Karma |
| Erzurum | 4.520 | 5 | Doğu Anadolu | Ekstrem ısıtma |
| Samsun | 1.750 | 25 | Karadeniz | Isıtma ağırlıklı |

> **Kaynak:** T.C. Çevre, Şehircilik ve İklim Değişikliği Bakanlığı / Meteoroloji Genel Müdürlüğü verileri. Değerler yaklaşık olup detaylı proje çalışmalarında yerel meteoroloji verileri kullanılmalıdır.

### 6.5 Endüstriyel Tesislerde Derece-Gün Kullanımı

Endüstriyel tesislerde derece-gün analizi genellikle **HVAC ve bina enerji** bileşeni için kullanılır. Proses enerji tüketimi derece-gün ile korelasyon göstermeyebilir. Bu nedenle:

1. Enerji tüketimini bileşenlerine ayır (proses + HVAC + aydınlatma)
2. HVAC bileşeni için HDD/CDD regresyonu kur
3. Proses bileşeni için üretim değişkeni kullan
4. Çoklu regresyon ile birleştir

## 7. İleri İstatistiksel Yöntemler (Advanced Statistical Methods)

### 7.1 Değişim Noktası Modelleri (Change-Point Models)

Basit doğrusal regresyon yetersiz kaldığında, enerji tüketim profili farklı bölgelerde farklı davranış gösterebilir:

```
3-Parametreli Model (3P — Heating only):
  E = a + b × max(T_baz − T_dış, 0)

4-Parametreli Model (4P — Heating with base load):
  E = a            eğer T_dış ≥ T_baz
  E = a + b(T_baz − T_dış)  eğer T_dış < T_baz

5-Parametreli Model (5P — Heating + Cooling):
  E = a + b_h × max(T_h − T_dış, 0) + b_c × max(T_dış − T_c, 0)

Burada:
  T_h : Isıtma değişim noktası sıcaklığı [°C]
  T_c : Soğutma değişim noktası sıcaklığı [°C]
  b_h : Isıtma eğimi [kWh/°C]
  b_c : Soğutma eğimi [kWh/°C]
```

### 7.2 TOWT — Time-of-Week-and-Temperature

Saatlik M&V modellerinde kullanılan gelişmiş yöntem:

| Özellik | Açıklama |
|---|---|
| Zaman çözünürlüğü | Haftanın her saati (168 profil) |
| Sıcaklık etkisi | Her saat dilimi için ayrı sıcaklık katsayısı |
| Avantaj | Vardiya, hafta sonu, tatil etkilerini yakalar |
| Dezavantaj | Çok sayıda parametre → overfitting riski |
| Minimum veri | ≥ 9 ay saatlik veri |

### 7.3 Bayesian Yaklaşımı (Bayesian Approach)

- Önsel bilgi (prior) + gözlem verisi → sonsal dağılım (posterior)
- Belirsizlik, doğal olarak modelin içinde
- Küçük veri setlerinde klasik regresyondan daha güvenilir
- ESCO sözleşmelerinde henüz yaygın kullanım yok

### 7.4 Ne Zaman Basit Regresyon Yetmez?

| Durum | İşaret | Alternatif |
|---|---|---|
| Mevsimsel patern | Artıklarda sinüzoidal yapı | TOWT veya harmonik regresyon |
| Birden fazla rejim | R² düşük, artıklarda yapı | Change-point model |
| Doğrusal olmayan ilişki | Artık-tahmin grafiğinde eğri | Polinom veya ML modeli |
| Çok sayıda değişken | Multicollinearity (VIF > 10) | PCA + regresyon veya ridge |
| Zaman bağımlılığı | DW < 1.5 | ARIMA veya gecikme değişkeni |

## 8. Çalışılmış Örnek — Bina HVAC Sistemi M&V (Worked Example)

### 8.1 Proje Tanımı

Bir ofis binasının HVAC sistemi iyileştirmesi (chiller değişimi + otomasyon). IPMVP Opsiyon C ile tesis geneli M&V uygulanacaktır.

### 8.2 Baseline Veriler (12 Ay)

| Ay | Tüketim (kWh) | HDD (°C·gün) | CDD (°C·gün) | Çalışma Günü |
|---|---|---|---|---|
| Ocak | 82.500 | 420 | 0 | 22 |
| Şubat | 78.200 | 380 | 0 | 20 |
| Mart | 62.100 | 250 | 0 | 23 |
| Nisan | 48.500 | 95 | 5 | 22 |
| Mayıs | 44.200 | 15 | 35 | 22 |
| Haziran | 58.700 | 0 | 120 | 22 |
| Temmuz | 72.300 | 0 | 195 | 23 |
| Ağustos | 68.900 | 0 | 170 | 21 |
| Eylül | 52.400 | 0 | 75 | 22 |
| Ekim | 46.800 | 80 | 10 | 23 |
| Kasım | 63.500 | 240 | 0 | 21 |
| Aralık | 79.800 | 390 | 0 | 22 |

### 8.3 Regresyon Modeli

```
Model:
  E = a + b₁ × HDD + b₂ × CDD

Regresyon Sonuçları:
═══════════════════════════════════════════════
  Katsayı    Değer     SE        t-stat   p-value
  a (sabit)  42.850    1.245     34.42    < 0.001
  b₁ (HDD)   93.2      5.8      16.07    < 0.001
  b₂ (CDD)  152.4      8.1      18.81    < 0.001

Model İstatistikleri:
  R²       = 0.986
  Adj R²   = 0.983
  CV(RMSE) = 4.8%  (< %25 aylık ✓)
  NMBE     = 0.1%  (< ±%0.5 aylık ✓)
  n        = 12
  p        = 3

ASHRAE Guideline 14 Doğrulama:
  R²       = 0.986 ≥ 0.75  ✓
  CV(RMSE) = 4.8%  ≤ 25%   ✓
  NMBE     = 0.1%  ≤ ±0.5% ✓
  → Model KABUL edilir
═══════════════════════════════════════════════
```

### 8.4 Raporlama Dönemi Tasarruf Hesaplama

```
Raporlama Dönemi — Ocak (ECM sonrası):
─────────────────────────────────────────────
Gerçek HDD_ocak    = 435 °C·gün (daha soğuk bir ocak)
Gerçek CDD_ocak    = 0 °C·gün
Ölçülen E_ocak     = 68.200 kWh

Ayarlanmış Baseline:
  E_baseline,ayarlanmış = 42.850 + 93.2 × 435 + 152.4 × 0
  E_baseline,ayarlanmış = 42.850 + 40.542
  E_baseline,ayarlanmış = 83.392 kWh

Tasarruf (Ocak):
  S_ocak = E_baseline,ayarlanmış − E_ölçülen
  S_ocak = 83.392 − 68.200
  S_ocak = 15.192 kWh

Tasarruf Oranı:
  %Tasarruf = 15.192 / 83.392 × 100 = %18.2
─────────────────────────────────────────────
```

### 8.5 Belirsizlik Hesabı

```
Belirsizlik (%90 güven):
─────────────────────────────────────────────
  t(9, 0.05) = 1.833
  CV(RMSE)   = 4.8%
  Ē          = 63.158 kWh/ay
  n = 12, m = 1 (tek ay)

  U_model = 1.833 × 0.048 × 63.158 × √(1/12)
  U_model = 1.833 × 0.048 × 63.158 × 0.289
  U_model = 1.604 kWh

  Sonuç:
  S_ocak = 15.192 ± 1.604 kWh (%90 güvenle)
  Aralık: 13.588 — 16.796 kWh
  Göreceli belirsizlik: ±%10.6 (IPMVP ≤ %50 ✓)
─────────────────────────────────────────────
```

## 9. İlgili Dosyalar

- [IPMVP Çerçevesi](mv_ipmvp.md) — Protokol seçimi, ESCO bağlamı, dijital M&V
- [M&V Plan Hazırlama](mv_planning.md) — M&V planı şablonu ve tam çalışılmış örnek
- [Baseline ve EnPI](baseline_enpi.md) — ISO 50006, EnB oluşturma, EnPI tanımlama
- [CUSUM Analizi](cusum_analysis.md) — Kümülatif toplam ile performans sapma tespiti
- [M&V Formül Detayları](../../factory/measurement_verification.md) — IPMVP opsiyon formülleri ve baseline ayarlama
- [Energy Management INDEX](INDEX.md) — Enerji yönetimi bilgi tabanı ana dizin

## 10. Referanslar (References)

1. ASHRAE, "ASHRAE Guideline 14-2014: Measurement of Energy, Demand, and Water Savings," ASHRAE, 2014.
2. EVO (Efficiency Valuation Organization), "IPMVP Core Concepts 2022," EVO 10400-1:2022.
3. ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations."
4. ISO 50006:2014, "Energy management systems — Measuring energy performance using energy baselines and energy performance indicators."
5. Reddy, T.A., "Applied Data Analysis and Modeling for Energy Engineers and Scientists," Springer, 2011.
6. Kissock, J.K., et al., "Inverse Modeling Toolkit: Numerical Algorithms," ASHRAE Transactions, 2003.
7. Granderson, J., et al., "Building Energy Information Systems: User Case Studies," Energy Efficiency, 2011.
8. T.C. Meteoroloji Genel Müdürlüğü, "İllere Göre Uzun Yıllar Ortalama Sıcaklık Verileri."
9. IPMVP Committee, "IPMVP Statistics and Uncertainty for IPMVP," EVO 10400-1:2014, Annex B.
10. Montgomery, D.C., et al., "Introduction to Linear Regression Analysis," 6th Edition, Wiley, 2021.
