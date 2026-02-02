---
title: "Enerji Temel Çizgisi ve EnPI Oluşturma (Energy Baseline and EnPI Development — ISO 50006)"
category: factory
equipment_type: factory
keywords: [enerji temel çizgisi, EnB, EnPI, ISO 50006, regresyon analizi, normalleştirme, model doğrulama, exergy EnPI]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/energy_review.md, factory/energy_management/enpi_guide.md, factory/energy_management/cusum_analysis.md, factory/energy_management/mv_statistics.md, factory/kpi_definitions.md]
use_when: ["Enerji temel çizgisi oluşturulacağında", "EnPI modeli geliştirilecekken", "Regresyon analizi yapılacağında"]
priority: high
last_updated: 2026-02-01
---

# Enerji Temel Çizgisi ve EnPI Oluşturma (Energy Baseline and EnPI Development — ISO 50006)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

ISO 50006:2014, enerji temel çizgisi (EnB — Energy Baseline) ve enerji performans göstergesi (EnPI — Energy Performance Indicator) oluşturmak için sistematik bir çerçeve sunar. EnB, performans karşılaştırma referans noktasıdır; EnPI ise enerji performansını ölçen nicel göstergedir. Birlikte, organizasyonun enerji performansındaki iyileşmeyi veya bozulmayı objektif biçimde ortaya koyarlar.

### 1.1 Temel Kavramlar

| Kavram | İngilizce | Tanım |
|--------|-----------|-------|
| Enerji Temel Çizgisi | Energy Baseline (EnB) | Enerji performansı karşılaştırma için nicel referans |
| Enerji Performans Göstergesi | Energy Performance Indicator (EnPI) | Enerji performansını ölçen metrik veya model |
| İlgili Değişken | Relevant Variable | Enerji tüketimini etkileyen ve düzenli değişen faktör |
| Statik Faktör | Static Factor | Normalde değişmeyen ancak enerjiyi etkileyen koşul |
| Normalleştirme | Normalization | Aynı koşullar altında karşılaştırma yapma |
| Raporlama Dönemi | Reporting Period | Performansın değerlendirildiği güncel dönem |

### 1.2 EnB/EnPI İlişkisi

```
EnB ve EnPI birlikte çalışır:

EnB → Referans noktası (geçmiş dönem performansı)
EnPI → Performans ölçüsü (mevcut dönem)

İyileşme = EnB_normalized - EnPI_raporlama
         = E_model(X_raporlama) - E_gerçek_raporlama

Pozitif fark → Tasarruf (iyileşme)
Negatif fark → Ek tüketim (bozulma)
Sıfır fark → Değişiklik yok
```

### 1.3 Temel Çizgi Dönem Seçimi

```
Baseline dönemi seçim kriterleri:

├── Minimum 12 ay (mevsimsel etkileri yakalamak için)
├── Tercihen 24-36 ay (istatistiksel güvenilirlik)
├── Temsili dönem (normal üretim koşulları)
├── Büyük değişiklik öncesi dönem
├── Güvenilir ölçüm verileri olan dönem
└── Veri noktası sayısı > 12 (aylık) veya > 52 (haftalık)

Uygun OLMAYAN dönemler:
├── Pandemi gibi anormal kısıtlama dönemleri
├── Büyük kapasite değişikliği geçiş dönemi
├── Uzun süreli ekipman arızası dönemleri
├── Mevsimsel üretim yapan tesislerde tek mevsim
└── Ölçüm cihazı kalibrasyonu yapılmamış dönemler
```

## 2. Enerji Temel Çizgisi (Energy Baseline — EnB)

### 2.1 EnB Oluşturma Adımları

```
EnB oluşturma prosedürü:

Adım 1: Veri toplama
├── Enerji tüketim verileri (SEU bazında)
├── İlgili değişken verileri (üretim, sıcaklık, vb.)
├── Minimum 12 aylık periyot
└── Veri kalitesi kontrol (eksik veri, outlier tarama)

Adım 2: Keşifsel analiz
├── Scatter plot (her değişken vs enerji)
├── Pearson korelasyon katsayısı (r)
├── Zaman serisi trendleri
└── Mevsimsel patern tespiti

Adım 3: Model seçimi
├── Tek değişkenli doğrusal: E = β₀ + β₁X
├── Çok değişkenli doğrusal: E = β₀ + β₁X₁ + β₂X₂ + ε
├── Parçalı doğrusal (change-point): E = β₀ + β₁max(X-CP, 0)
└── Polinom (gerekirse): E = β₀ + β₁X + β₂X²

Adım 4: Model kurulumu
├── OLS (Ordinary Least Squares) regresyon
├── Katsayıların hesaplanması
├── p-value kontrolü (< 0.05)
└── Fiziksel anlamlılık doğrulama

Adım 5: Model doğrulama
├── R² ≥ 0.75 (aylık veri)
├── CV-RMSE ≤ %25 (aylık veri)
├── NMBE ≤ ±%10
├── Residual analizi (normallik, pattern)
└── Outlier kontrolü

Adım 6: Dokümantasyon
├── Model formülü ve katsayılar
├── Baseline dönemi ve veri seti
├── Doğrulama sonuçları
├── Ayarlama kriterleri
└── Onay ve revizyon geçmişi
```

### 2.2 Veri Kalitesi Gereksinimleri

| Kriter | Kabul Eşiği | Kontrol Yöntemi |
|--------|-------------|-----------------|
| Eksik veri | < %10 toplam veri noktası | Veri sayımı |
| Outlier | < %5 toplam veri noktası | IQR veya 3σ kuralı |
| Ölçüm doğruluğu | Sayaç sınıfına uygun | Kalibrasyon sertifikası |
| Veri frekansı | Aylık minimum, haftalık tercih | Kayıt sistemi kontrolü |
| Enerji dengesi | Hata < %5 (ana sayaç vs alt sayaçlar toplamı) | Cross-check |

### 2.3 EnB Güncelleme Tetikleyicileri

```
EnB ayarlanması gereken durumlar (ISO 50001:2018, Madde 6.5):

1. EnPI artık enerji performansını yansıtmıyorsa:
   ├── Model R² düşmesi (< 0.75)
   ├── Sistematik sapma (bias) oluşması
   ├── Residual'larda patern ortaya çıkması
   └── Yeni süreç/ekipman modele dahil değilse

2. Statik faktörler değişmişse:
   ├── Üretim kapasitesi değişikliği (> %10)
   ├── Yeni ürün hattı / proses eklenmesi
   ├── Bina / tesis genişlemesi
   ├── Enerji kaynağı değişikliği (kömürden doğalgazagaz)
   └── Önemli ekipman değişikliği (yeni kompresör, kazan, vb.)

3. Önceden tanımlanmış yöntem:
   ├── Ayarlama kriterleri EnMS'de dokümante olmalı
   ├── Hangi durumda yeni baseline oluşturulacağı net tanımlı
   └── Tarihsel karşılaştırılabilirliğin korunma yöntemi

DİKKAT: Baseline ayarlama ≠ Baseline sıfırlama
  - Mevcut tasarruflar kaybolmamalıdır
  - Ayarlama gerekçesi dokümante edilmelidir
  - Denetim izlenebilirliği korunmalıdır
```

## 3. EnPI Türleri (EnPI Types)

### 3.1 EnPI Türleri ve Karşılaştırma

| EnPI Türü | Tanım | Formül | Avantaj | Dezavantaj | Uygun Durum |
|-----------|-------|--------|---------|------------|-------------|
| Mutlak tüketim | Toplam enerji | E [kWh] | Basit, anlaşılır | Üretimden etkilenir | Trend izleme, raporlama |
| Spesifik (SEC) | Birim ürün başına | E/P [kWh/ton] | Normalize, benchmark | Ürün karışımı etkisi | Tek ürün tesisleri |
| Oran (Ratio) | Kaynak oranı | E_i/E_toplam [%] | Kaynak dağılımı | Performans göstermez | Enerji karışımı izleme |
| Regresyon bazlı | Model tahmin farkı | E_gerçek vs E_model | En doğru, normalize | Karmaşık hesaplama | Çok değişkenli durumlar |
| Exergy bazlı | Exergy verimi | η_ex = Ė_out/Ė_in [%] | Termodinamik kalite | Ölçüm altyapısı gerekli | İleri düzey tesisler |

### 3.2 Sektörel EnPI Örnekleri

| Sektör | SEU | Önerilen EnPI | Tipik Aralık | Birim |
|--------|-----|--------------|-------------|-------|
| Çimento | Klinker fırını | SEC | 700-900 | kcal/kg klinker |
| Çimento | Çimento öğütme | SEC | 30-45 | kWh/ton çimento |
| Tekstil | Boyahane buhar | Spesifik buhar | 3-6 | kg buhar/kg kumaş |
| Gıda | Soğutma | COP | 4.0-6.0 | — |
| Gıda | Kurutma | SEC | 800-1.500 | kJ/kg su buharlaştırma |
| Kimya | Distilasyon | SEC | 200-500 | kWh/ton ürün |
| Metal | Ergitme | SEC | 500-700 | kWh/ton döküm |
| Otomotiv | Boyahane | SEC | 800-1.200 | kWh/araç gövde |
| Kağıt | Kurutma | SEC | 150-300 | kWh/ton kağıt |
| Cam | Eritme fırını | SEC | 1.200-1.800 | kcal/kg cam |

## 4. Regresyon Modeli Oluşturma (Regression Model Development)

### 4.1 Adım Adım Prosedür

```
Adım 1: Veri toplama
  - SEU enerji tüketimi: E [kWh/ay veya MWh/ay]
  - Potansiyel değişkenler: Üretim [ton/ay], HDD [°C·gün/ay], CDD [°C·gün/ay]
  - Minimum 12 veri noktası (aylık bazda)

Adım 2: Scatter plot
  - Her potansiyel değişken vs E grafiği çizilir
  - Doğrusal, eğrisel veya ilişkisiz patern kontrol edilir

Adım 3: Korelasyon analizi
  - Pearson r hesaplanır
  - |r| > 0.7 → Model adayı
  - Değişkenler arası VIF kontrol (< 5 olmalı)

Adım 4: Model kurulumu (OLS)
  Tek değişkenli:
    E = β₀ + β₁ × X₁

  Çok değişkenli:
    E = β₀ + β₁ × X₁ + β₂ × X₂ + ε

  Katsayı yorumu:
    β₀ = Baseload enerji tüketimi (üretim sıfırken)
    β₁ = Marjinal enerji tüketimi (birim değişken başına enerji)

Adım 5: İstatistiksel anlamlılık
  - Genel model F-test: p < 0.05
  - Her katsayı t-test: p < 0.05
  - Anlamlı olmayan değişken → Modelden çıkar

Adım 6: Katsayı yorumlama
  Örnek: E [MWh/ay] = 200 + 2.5 × Üretim [ton/ay] + 1.2 × HDD [°C·gün/ay]

  β₀ = 200 MWh/ay → Sabit tüketim (aydınlatma, ofis, standby)
  β₁ = 2.5 MWh/ton → Her 1 ton üretim, 2.5 MWh ek enerji
  β₂ = 1.2 MWh/°C·gün → Her 1 °C·gün HDD, 1.2 MWh ısıtma enerjisi
```

### 4.2 Regresyon Formülleri

```
Temel formüller:

Doğrusal regresyon:
  E = β₀ + β₁ × V₁ + β₂ × V₂ + ... + c

R² (Determination Katsayısı):
  R² = 1 - (SS_res / SS_tot)
  SS_res = Σ(E_i - Ê_i)²  (residual kareler toplamı)
  SS_tot = Σ(E_i - Ē)²     (toplam kareler toplamı)

Adjusted R² (Düzeltilmiş R²):
  R²_adj = 1 - [(1 - R²)(n - 1) / (n - k - 1)]
  n = veri noktası sayısı
  k = değişken sayısı

RMSE (Root Mean Square Error):
  RMSE = √(Σ(E_i - Ê_i)² / n)

CV-RMSE (Coefficient of Variation of RMSE):
  CV-RMSE = (RMSE / Ē) × 100 [%]

NMBE (Normalized Mean Bias Error):
  NMBE = [Σ(E_i - Ê_i) / (n × Ē)] × 100 [%]
```

## 5. Model Doğrulama (Model Validation)

### 5.1 ASHRAE Guideline 14 Kriterleri

| Kriter | Formül | Aylık Veri Eşiği | Günlük Veri Eşiği | Saatlik Veri Eşiği |
|--------|--------|-------------------|--------------------|--------------------|
| R² | 1 - SS_res/SS_tot | ≥ 0.75 | ≥ 0.70 | ≥ 0.50 |
| CV-RMSE | (RMSE/Ē) × 100 | ≤ %25 | ≤ %30 | ≤ %30 |
| NMBE | [Σ(E_i-Ê_i)/(n×Ē)] × 100 | ±%0.5 | ±%10 | ±%10 |

```
Kriter yorumlama:

R² (açıklanan varyans):
├── R² ≥ 0.90 → Mükemmel model — Doğrudan kullan
├── 0.75 ≤ R² < 0.90 → İyi model — Kabul edilebilir
├── 0.50 ≤ R² < 0.75 → Orta model — İyileştirme gerekebilir
└── R² < 0.50 → Zayıf model — Yeniden modelleme gerekli

CV-RMSE (tahmin hatası):
├── CV-RMSE ≤ %15 → Yüksek doğruluk
├── %15 < CV-RMSE ≤ %25 → Kabul edilebilir
└── CV-RMSE > %25 → Model yetersiz

NMBE (sistematik sapma):
├── |NMBE| ≤ %0.5 → Sapma yok
├── %0.5 < |NMBE| ≤ %5 → Düşük sapma
└── |NMBE| > %5 → Sistematik sapma var → Modeli gözden geçir
```

### 5.2 Diagnostik Kontroller

```
Model diagnostik kontrol listesi:

1. Residual analizi:
   ├── Normallik: Residual'lar normal dağılmalı (Shapiro-Wilk test)
   ├── Homojenlik: Residual dağılımı sabit olmalı (no fan shape)
   ├── Bağımsızlık: Ardışık residual'lar korelasyonsuz (Durbin-Watson)
   └── Pattern: Sistematik patern olmamalı (rasgele dağılım)

2. Outlier tespiti:
   ├── Standardize residual |z| > 3 → Outlier adayı
   ├── Cook's distance > 4/n → Etkili nokta
   └── Leverage > 2(k+1)/n → Kaldıraç noktası

3. Çoklu doğrusallık:
   ├── VIF (Variance Inflation Factor) < 5
   ├── VIF > 10 → Ciddi çoklu doğrusallık
   └── Çözüm: Değişken çıkarma veya PCA

4. Fiziksel anlamlılık:
   ├── β₀ > 0 olmalı (negatif enerji olmaz)
   ├── β₁ > 0 olmalı (üretim arttıkça enerji artar)
   └── Katsayı büyüklüğü makul aralıkta mı?
```

## 6. Normalleştirme (Normalization)

### 6.1 Normalleştirme Kavramı

```
Normalleştirme neden gerekli?

Problem: Raporlama döneminde koşullar baseline'dan farklı olabilir
  - Üretim miktarı değişmiş
  - Hava sıcaklığı farklı
  - Vardiya düzeni değişmiş

Çözüm: Model ile "aynı koşullar" altında karşılaştırma

Normalized Baseline = E_model(X_raporlama)
Gerçek Tüketim = E_gerçek_raporlama
Tasarruf = E_model(X_raporlama) - E_gerçek_raporlama
```

### 6.2 Statik Faktörler vs İlgili Değişkenler

```
Statik faktörler (normalde değişmeyen):
├── Bina yapısı (yalıtım, pencere tipi)
├── Ekipman kapasitesi (motor gücü, kompresör kapasitesi)
├── Proses tipi (batch vs sürekli)
├── Tesis lokasyonu (iklim bölgesi)
├── Vardiya sayısı (sabit ise)
└── Üretim hattı sayısı

İlgili değişkenler (düzenli değişen):
├── Üretim miktarı/hızı [ton/ay]
├── Ortam sıcaklığı/nemi [°C, %RH]
├── HDD/CDD [°C·gün/ay]
├── Ürün karışımı [oran]
├── Hammadde nemi/sıcaklığı [%, °C]
└── Çalışma saatleri [saat/ay]

NOT: Statik faktör değiştiğinde → EnB ayarlanmalıdır (ISO 50001:2018, 6.5)
     İlgili değişken değiştiğinde → Normalleştirme uygulanır
```

### 6.3 Normalleştirme Prosedürü ve Örneği

```
Normalleştirme prosedürü:

1. Baseline model: E_baseline = β₀ + β₁X₁ + β₂X₂
2. Raporlama dönemi değişken değerlerini modele gir
3. Normalized baseline = E_model(X_raporlama_dönemi)
4. Tasarruf = Normalized baseline - Gerçek tüketim

Örnek:
  Baseline model: E [MWh/ay] = 180 + 3.2 × Üretim [ton] + 1.8 × CDD [°C·gün]

  Raporlama dönemi (Temmuz):
    Üretim = 300 ton, CDD = 150 °C·gün
    E_normalized = 180 + 3.2×300 + 1.8×150 = 180 + 960 + 270 = 1.410 MWh
    E_gerçek = 1.320 MWh

  Tasarruf = 1.410 - 1.320 = 90 MWh (%6.4 iyileşme)
  → Üretim ve hava koşulları normalize edilmiş durumda %6.4 enerji tasarrufu
```

## 7. Exergy Bazlı EnPI (Exergy-Based EnPI)

### 7.1 Exergy Veriminin EnPI Olarak Kullanımı

```
Exergy verimi (genel):
  η_ex = Ė_çıkış / Ė_giriş × 100 [%]

Burada:
  Ė_çıkış = Faydalı exergy çıkışı [kW]
  Ė_giriş = Toplam exergy girişi [kW]

Ekipman bazında exergy EnPI:
  Kompresör: η_ex = (ṁ × ex_kompresyon) / Ẇ_elektrik
  Kazan:     η_ex = (ṁ_buhar × ex_buhar) / (ṁ_yakıt × ex_yakıt)
  Chiller:   η_ex = (Q̇_soğutma × ex_soğutma/Q̇) / Ẇ_elektrik
  Pompa:     η_ex = (ṁ × Δex_akışkan) / Ẇ_elektrik

Fabrika seviyesinde exergy EnPI:
  η_ex_fabrika = Σ(Ė_faydalı_çıkış_i) / Σ(Ė_giriş_j) × 100 [%]

Exergy-bazlı SEC:
  SEC_ex = Ė_giriş / P [kW·h_ex/ton] veya [MJ_ex/ton]

Exergy iyileşme potansiyeli:
  IP = (1 - η_ex) × Ė_giriş [kW]
```

### 7.2 Exergy EnPI Avantajları

| Enerji EnPI | Exergy EnPI | Exergy Avantajı |
|-------------|-------------|-----------------|
| Kazan verimi %90 | Exergy verimi %42 | Yanma/transfer kayıplarını gerçek gösterir |
| COP = 5.0 | Exergy verimi %30 | Carnot sınırına referansla değerlendirir |
| Motor verimi %93 | Exergy verimi %91 | Elektrik→mekanik tutarlı |
| Buhar verimli dağılıyor | Exergy %50 kayıp | Sıcaklık düşürme kayıplarını yakalar |
| SEC = 450 kWh/ton | SEC_ex = 180 kWh_ex/ton | Enerji kalitesini dikkate alır |

### 7.3 Sektörel Exergy Referansları

| Sektör | Tipik η_ex [%] | En İyi Uygulama [%] | Teorik Sınır [%] |
|--------|---------------:|---------------------:|------------------:|
| Çimento | 25-35 | 40-45 | ~55 |
| Demir-Çelik | 30-40 | 45-50 | ~60 |
| Kimya | 25-35 | 40-48 | ~55 |
| Gıda | 15-25 | 30-38 | ~45 |
| Tekstil | 12-20 | 25-32 | ~40 |
| Kağıt | 25-35 | 38-45 | ~55 |

### 7.4 ExergyLab'ın Benzersiz Katkısı

```
ExergyLab EnPI entegrasyonu:

Ekipman seviyesi:
├── η_ex_kompresör: İzentropik exergy verimi [%]
├── η_ex_kazan: Yanma + ısı transfer exergy verimi [%]
├── η_ex_chiller: Soğutma exergy verimi [%]
├── η_ex_pompa: Pompa exergy verimi [%]
├── Ė_destroyed: Exergy yıkımı [kW]
└── IP: İyileşme potansiyeli [kW]

Fabrika seviyesi:
├── η_ex_fabrika: Toplam exergy verimi [%]
├── SEC_ex_fabrika: Fabrika exergy SEC [MJ_ex/ton]
├── Exergy Sankey: Kayıp akış diyagramı
└── Cross-equipment: Entegrasyon fırsatları

ExergyLab η_ex → ISO 50001 EnPI eşleştirme:
- Aylık η_ex trendi = enerji performans iyileşmesinin "kalite" göstergesi
- Sektörel η_ex benchmarking
- Hedef: η_ex ≥ sektör üst çeyrek
```

## 8. Çalışılmış Örnek — Çimento Fabrikası

### 8.1 Fabrika Profili

```
Fabrika: Orta ölçekli çimento üretim tesisi
Kapasite: 1.500.000 ton/yıl klinker
Enerji kaynakları: Elektrik (öğütme), petrol koku + doğalgaz (fırın)
Yıllık enerji tüketimi: 125.000 TEP
SEU: Döner fırın sistemi (%65), çimento öğütme (%20), hammadde öğütme (%10)
```

### 8.2 Veri ve Regresyon Modeli

```
12 aylık veri (döner fırın sistemi — doğalgaz tüketimi):

| Ay     | Klinker [kton] | Ortalama Sıcaklık [°C] | Doğalgaz [bin m³] |
|--------|---------------:|------------------------:|-------------------:|
| Ocak   | 110            | 2                       | 7.800              |
| Şubat  | 105            | 4                       | 7.500              |
| Mart   | 120            | 10                      | 8.200              |
| Nisan  | 130            | 16                      | 8.600              |
| Mayıs  | 135            | 22                      | 8.700              |
| Haziran| 140            | 28                      | 8.900              |
| Temmuz | 138            | 32                      | 8.850              |
| Ağustos| 142            | 30                      | 9.000              |
| Eylül  | 132            | 24                      | 8.550              |
| Ekim   | 125            | 16                      | 8.300              |
| Kasım  | 115            | 8                       | 7.900              |
| Aralık | 108            | 3                       | 7.650              |

Regresyon modeli:
  E [bin m³/ay] = 2.100 + 48.5 × Klinker [kton/ay] + 5.2 × T_dış [°C/ay]

İstatistikler:
  R² = 0.94       → ≥ 0.75 ✓
  CV-RMSE = %8.3  → ≤ %25 ✓
  NMBE = +%0.3    → ±%0.5 ✓ (ASHRAE 14 — aylık)
  p(β₁) < 0.001   → < 0.05 ✓ (klinker üretimi anlamlı)
  p(β₂) = 0.018   → < 0.05 ✓ (sıcaklık anlamlı)

Katsayı yorumu:
  β₀ = 2.100 bin m³/ay → Baseload (fırın idle, yardımcı sistemler)
  β₁ = 48.5 bin m³/kton → Her 1 kton klinker üretimi 48.5 bin m³ doğalgaz
  β₂ = 5.2 bin m³/°C → Her 1°C sıcaklık artışı 5.2 bin m³ ek tüketim
       (NOT: Hammadde nemi arttıkça kurutma enerjisi artar — sıcaklık proxy)
```

### 8.3 Tahmin vs Gerçek Karşılaştırma

```
Raporlama dönemi — Sonraki yıl Ocak:
  Klinker = 118 kton, T_dış = 1°C

  E_model = 2.100 + 48.5 × 118 + 5.2 × 1 = 2.100 + 5.723 + 5.2 = 7.828 bin m³
  E_gerçek = 7.450 bin m³

  Tasarruf = 7.828 - 7.450 = 378 bin m³ (%4.8 iyileşme)

  Sonuç: Klinker üretimi ve hava sıcaklığı normalize edildiğinde,
  fabrika önceki yıla göre %4.8 enerji tasarrufu sağlamıştır.

CUSUM başlangıcı:
  Kümülatif tasarruf Ocak: +378 bin m³
  → Pozitif CUSUM trendi → Sürekli iyileşme kanıtı
  → Detay: cusum_analysis.md
```

### 8.4 Exergy Perspektifi

```
Çimento fabrikası exergy analizi:

Döner fırın sistemi:
  Yakıt exergy girişi: 45.000 kW
  Klinker exergy çıkışı: 15.750 kW
  Baca gazı exergy kaybı: 8.100 kW
  Radyasyon kaybı: 4.500 kW
  Diğer exergy yıkımı: 16.650 kW

  η_ex_fırın = 15.750 / 45.000 = %35.0
  IP = (1 - 0.35) × 45.000 = 29.250 kW

Exergy EnPI hedef:
  Mevcut: η_ex = %35.0
  Sektör ortalaması: η_ex = %30.0
  En iyi uygulama: η_ex = %42.0
  Hedef (12 ay): η_ex ≥ %37.0 (+2 puan)

ExergyLab katkısı:
  → Baca gazı exergy kaybının büyüklüğünü görselleştirir (8.100 kW)
  → Preheater + precalciner optimizasyonu önerir
  → Alternatif yakıt (AF) exergy etkisini modelleyebilir
```

## 9. İlgili Dosyalar

- [Enerji Yönetimi INDEX](INDEX.md) — Bilgi tabanı navigasyonu
- [Enerji İnceleme](energy_review.md) — SEU belirleme ve değişken tanımlama
- [EnPI Rehberi](enpi_guide.md) — Detaylı EnPI tanımlama ve sektörel örnekler
- [CUSUM Analizi](cusum_analysis.md) — Kümülatif toplam analizi
- [M&V İstatistikleri](mv_statistics.md) — Regresyon ve belirsizlik analizi
- [KPI Tanımları (genel)](../kpi_definitions.md) — Genel KPI çerçevesi
- [Eylem Planlama](action_planning.md) — Hedef belirleme ve ECM önceliklendirme

## 10. Referanslar

- ISO 50006:2014, "Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI)"
- ISO 50015:2014, "Measurement and verification of energy performance of organizations"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- ISO 50001:2018, Clauses 6.4 and 6.5
- Kissock, K. et al., "Inverse modeling toolkit: numerical algorithms"
- US DOE, "EnPI Tool v5.0" (ucretsiz Excel aracı)
- SEE Action, "Energy Performance Baseline Methodology"
- IPMVP (International Performance Measurement and Verification Protocol), EVO 10000-1:2012
- Tsatsaronis, G., "Definitions and nomenclature in exergy analysis and exergoeconomics"
