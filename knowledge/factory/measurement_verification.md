---
title: "Ölçüm ve Doğrulama Protokolleri (Measurement and Verification — M&V)"
category: factory
equipment_type: factory
keywords: [ölçüm, doğrulama, M&V]
related_files: [factory/data_collection.md, factory/kpi_definitions.md, factory/reporting.md]
use_when: ["Ölçüm ve doğrulama planı hazırlanırken", "M&V protokolü belirlenirken"]
priority: low
last_updated: 2026-01-31
---
# Ölçüm ve Doğrulama Protokolleri (Measurement and Verification — M&V)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji verimlilik projelerinin gerçek tasarruflarının doğrulanması, ölçüm ve doğrulama (M&V — Measurement and Verification) protokollerinin uygulanmasını gerektirir. Bu dosya; IPMVP (International Performance Measurement and Verification Protocol) çerçevesini kapsamlı olarak ele alır. Dört IPMVP opsiyonu, temel hat (baseline) ayarlama metodolojisi, rutin dışı düzeltmeler, etkileşim etkileri, tasarruf belirsizlik analizi, ASHRAE Guideline 14 istatistiksel kriterleri, M&V planı geliştirme ve raporlama dönemleri detaylı olarak incelenmektedir.

Doğru M&V uygulaması; ESCO sözleşmeleri, enerji performans garantileri, teşvik/hibe programları ve kurumsal enerji hedeflerinin izlenmesi için zorunludur.

## 1. IPMVP Opsiyon Seçimi (IPMVP Option Selection)

### 1.1 Opsiyon Karşılaştırma Tablosu

| Özellik | Opsiyon A | Opsiyon B | Opsiyon C | Opsiyon D |
|---|---|---|---|---|
| Tam Adı | Retrofit Isolation — Key Parameter | Retrofit Isolation — All Parameter | Whole Facility | Calibrated Simulation |
| Türkçe | Yalıtılmış Retrofit — Anahtar Parametre | Yalıtılmış Retrofit — Tüm Parametre | Tesis Geneli | Kalibre Edilmiş Simülasyon |
| Ölçüm sınırı | Etkilenen ekipman | Etkilenen ekipman | Tüm tesis (sayaç) | Tüm tesis veya alt sistem |
| Ölçülen parametre | Sadece anahtar parametre | Tüm enerji parametreleri | Tesis enerji faturaları | Model parametreleri |
| Tasarruf hesaplama | Mühendislik hesabı + ölçüm | Doğrudan ölçüm (önce/sonra) | Regresyon analizi | Simülasyon (EnergyPlus vb.) |
| Doğruluk | Orta (±%15-30) | Yüksek (±%5-15) | Orta-yüksek (±%10-20) | Değişken (±%10-30) |
| Maliyet | Düşük (%1-3 proje) | Orta-yüksek (%3-10) | Düşük (%1-5) | Yüksek (%5-15) |
| Süre | Kısa | Uzun (sürekli ölçüm) | Orta (12+ ay) | Uzun (model geliştirme) |
| En uygun durum | Tek ekipman, stabil koşul | Performans garantisi, ESCO | Çoklu proje, bina | Yeni bina, karmaşık etkileşim |

### 1.2 Opsiyon Seçimi Karar Ağacı

```
IPMVP opsiyon seçim rehberi:

Soru 1: Tasarruf tek bir ekipman/sistemden mi geliyor?
  EVET → Soru 2'ye git
  HAYIR → Soru 4'e git

Soru 2: Ekipmanın enerji tüketimi kolay ölçülebilir mi?
  EVET → Soru 3'e git
  HAYIR → Opsiyon A (anahtar parametre ölçümü yeterli)

Soru 3: Performans garantisi veya yüksek doğruluk gerekli mi?
  EVET → Opsiyon B (tüm parametreleri ölç)
  HAYIR → Opsiyon A (maliyet avantajlı)

Soru 4: Birden fazla proje aynı anda mı uygulanıyor?
  EVET → Soru 5'e git
  HAYIR → Opsiyon B (her proje ayrı izole edilebilir)

Soru 5: Tesis geneli fatura verisi yeterli ve güvenilir mi?
  EVET → Opsiyon C (regresyon bazlı)
  HAYIR → Soru 6'ya git

Soru 6: Karmaşık etkileşim etkileri var mı?
  EVET → Opsiyon D (simülasyon modeli)
  HAYIR → Opsiyon C (basitleştirilmiş)

Ek kriterler:
  - ESCO sözleşmesi → Opsiyon B veya C (garanti doğrulaması)
  - Bütçe kısıtı → Opsiyon A veya C (düşük M&V maliyeti)
  - Yeni bina → Opsiyon D (baz yılı yok)
  - Endüstriyel proses → Opsiyon A veya B (izole ölçüm)
  - HVAC optimizasyonu → Opsiyon C veya D (iklim etkisi)
```

## 2. Opsiyon A — Yalıtılmış Retrofit: Anahtar Parametre Ölçümü

### 2.1 Yöntem Açıklaması

```
Opsiyon A yaklaşımı:

Prensip:
  - Tasarrufu etkileyen ana (anahtar) parametre ölçülür
  - Diğer parametreler mühendislik tahminleri veya tek seferlik ölçümlerle belirlenir
  - Tasarruf, ölçülen parametre + tahminlerle hesaplanır

Formül:
  Tasarruf = (E_baz - E_sonra) ± düzeltmeler

  E_baz = f(anahtar_parametre_baz, tahmin_parametreler)
  E_sonra = f(anahtar_parametre_sonra, tahmin_parametreler)

Tipik kullanım:
  - VSD uygulaması: Güç ölçümü (anahtar), çalışma saati (tahmin)
  - Aydınlatma değişimi: Güç ölçümü (anahtar), açık kalma süresi (tahmin)
  - Motor değişimi: Motor verimliliği (anahtar), yük ve saat (tahmin)
  - İzolasyon: Yüzey sıcaklığı (anahtar), alan ve ortam koşulları (tahmin)

Avantaj: Düşük maliyet, basit uygulama
Dezavantaj: Tahmin edilen parametrelerdeki hata tasarruf doğruluğunu azaltır
```

### 2.2 Opsiyon A Örneği — Aydınlatma Retrofit

```
Proje: 500 adet T8 floresan → LED dönüşümü

Anahtar parametre (ölçülen): Güç tüketimi
  Önce: 500 × 58 W = 29,000 W (ölçüm: 28,500 W, ±%2)
  Sonra: 500 × 25 W = 12,500 W (ölçüm: 12,200 W, ±%2)
  ΔP = 28,500 - 12,200 = 16,300 W

Tahmin edilen parametre: Çalışma saati
  Vardiya bilgisi: 3 vardiya, 6 gün/hafta
  Tahmini yıllık saat: 6,240 saat/yıl (±%10 belirsizlik)

Tasarruf hesaplama:
  S = ΔP × t = 16,300 W × 6,240 h = 101,712,000 Wh = 101,712 kWh/yıl

Belirsizlik:
  u(ΔP)/ΔP = √(u(P_önce)² + u(P_sonra)²) / ΔP
  u(ΔP)/ΔP = √(570² + 244²) / 16,300 = 620/16,300 = %3.8
  u(t)/t = %10

  u(S)/S = √(%3.8² + %10²) = √(14.44 + 100) = %10.7
  U(S) = 2 × %10.7 = %21.4

  Tasarruf = 101,712 ± 21,766 kWh/yıl (%95 güven)
  Parasal: 101,712 × €0.12 = €12,205/yıl ± €2,612
```

## 3. Opsiyon B — Yalıtılmış Retrofit: Tüm Parametre Ölçümü

### 3.1 Yöntem Açıklaması

```
Opsiyon B yaklaşımı:

Prensip:
  - Etkilenen ekipmanın tüm enerji parametreleri sürekli ölçülür
  - Baz dönem ve proje sonrası dönem ölçümleri karşılaştırılır
  - Tasarruf doğrudan ölçüm farkından hesaplanır

Formül:
  Tasarruf = E_baz_ayarlı - E_sonra

  E_baz_ayarlı = E_baz × (koşul_düzeltme_faktörleri)
  Düzeltme: Üretim miktarı, hava sıcaklığı, çalışma saati vb.

Tipik kullanım:
  - Büyük kompresör VSD uygulaması (sürekli güç ölçümü)
  - Chiller değişimi (COP sürekli izleme)
  - Kazan modernizasyonu (yakıt ve buhar sürekli ölçüm)
  - Motor/pompa değişimi (güç ve debi sürekli ölçüm)

Avantaj: Yüksek doğruluk, performans garantisi için ideal
Dezavantaj: Yüksek ölçüm maliyeti, sürekli izleme gerekli
```

### 3.2 Opsiyon B Örneği — Kompresör VSD

```
Proje: 90 kW kompresöre VSD uygulaması

Baz dönem ölçümü (30 gün sürekli güç kayıt):
  Ortalama güç: 72.3 kW
  Çalışma saati: 7,200 h/yıl
  Yıllık tüketim (baz): 520,560 kWh/yıl
  Hava debisi: 12.5 Nm³/dk ortalama
  Spesifik güç: 5.78 kW/(Nm³/dk)

Proje sonrası ölçüm (30 gün sürekli güç kayıt):
  Ortalama güç: 53.8 kW
  Çalışma saati: 7,200 h/yıl (aynı üretim)
  Yıllık tüketim (sonra): 387,360 kWh/yıl
  Hava debisi: 12.3 Nm³/dk ortalama (benzer)
  Spesifik güç: 4.37 kW/(Nm³/dk)

Üretim ayarlaması (normalize):
  Debi oranı: 12.3/12.5 = 0.984
  E_baz_ayarlı = 520,560 × 0.984 = 512,231 kWh/yıl

Doğrulanmış tasarruf:
  S = 512,231 - 387,360 = 124,871 kWh/yıl
  Parasal: 124,871 × €0.12 = €14,985/yıl

Belirsizlik (sürekli ölçüm, düşük):
  u(S)/S ≈ ±%8 (k=2)
  S = 124,871 ± 9,990 kWh/yıl
```

## 4. Opsiyon C — Tesis Geneli: Fatura Analizi ve Regresyon

### 4.1 Yöntem Açıklaması

```
Opsiyon C yaklaşımı:

Prensip:
  - Tesis geneli enerji faturaları (veya ana sayaç) kullanılır
  - Baz dönemde enerji-bağımsız değişken regresyon modeli kurulur
  - Proje sonrası dönemde beklenen tüketim (baz hat) hesaplanır
  - Tasarruf = Beklenen (ayarlı baz hat) - Gerçekleşen

Formül:
  Ê_sonra = β₀ + β₁×P + β₂×HDD + ... (regresyon modeli, baz dönem)
  Tasarruf_ay = Ê_sonra - E_gerçek_sonra
  Tasarruf_yıllık = Σ Tasarruf_ay

Burada:
  Ê_sonra = Proje olmasaydı beklenen tüketim [kWh/ay]
  E_gerçek_sonra = Proje sonrası gerçekleşen tüketim [kWh/ay]
  β₀, β₁, β₂ = Regresyon katsayıları (baz dönemden)
  P = Üretim miktarı [ton/ay]
  HDD = Isıtma derece-gün [°C·gün/ay]

Veri gereksinimleri:
  Baz dönem: Minimum 12 ay (tercihen 24-36 ay) aylık fatura
  Proje sonrası: Minimum 12 ay aylık fatura
  Bağımsız değişken: Üretim verisi, hava verileri (HDD/CDD)
```

### 4.2 ASHRAE Guideline 14 İstatistiksel Kriterleri

```
Regresyon modeli kalite kriterleri:

1. CV-RMSE (Coefficient of Variation of Root Mean Square Error):
   CV-RMSE = [√(Σ(yᵢ - ŷᵢ)² / (n - p))] / ȳ × 100

   Burada:
     yᵢ = Gerçek değer (ölçülen enerji)
     ŷᵢ = Model tahmini
     n = Veri noktası sayısı
     p = Model parametre sayısı
     ȳ = Ortalama gerçek değer

   Kriter:
     Aylık veri: CV-RMSE ≤ %25
     Günlük veri: CV-RMSE ≤ %30 (daha gevşek, daha fazla gürültü)
     Saatlik veri: CV-RMSE ≤ %40

2. NMBE (Normalized Mean Bias Error):
   NMBE = Σ(yᵢ - ŷᵢ) / (n × ȳ) × 100

   Kriter:
     Aylık veri: NMBE ≤ ±%10 (ortalama sapma sınırlı)
     NMBE pozitif → Model düşük tahmin (tüketim tahmininin altında)
     NMBE negatif → Model yüksek tahmin

3. R² (Belirleme katsayısı):
   R² = 1 - Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)²

   Kriter:
     R² > 0.75 → Kabul edilebilir
     R² > 0.85 → İyi
     R² > 0.95 → Çok iyi

4. t-istatistiği:
   Her regresyon katsayısı için |t| > 2.0 (anlamlılık)
   p-değeri < 0.05
```

### 4.3 Opsiyon C Çalışılmış Örnek — Regresyon Bazlı Tasarruf Hesaplama

```
Tekstil fabrikası — Çoklu enerji verimlilik projesi:

Baz dönem verileri (24 ay):
  Enerji: Aylık doğalgaz faturaları [kWh/ay]
  Üretim: Aylık kumaş üretimi [ton/ay]
  İklim: Aylık HDD [°C·gün/ay]

Regresyon modeli (baz dönem):
  E = 450,000 + 5.2 × P + 1,800 × HDD [kWh/ay]

  Model istatistikleri:
    R² = 0.92
    CV-RMSE = %11.3 (< %25 → Uygun)
    NMBE = +%1.8 (< ±%10 → Uygun)
    β₁ (P): t = 8.4, p < 0.001 → Anlamlı
    β₂ (HDD): t = 4.2, p < 0.001 → Anlamlı

Proje sonrası dönem (12 ay):
  Uygulanan projeler: Economizer, kondansat geri kazanımı, izolasyon

  | Ay | P [ton] | HDD | Ê (Beklenen) | E (Gerçek) | Tasarruf |
  |----|---------|-----|-------------|------------|---------|
  | 1  | 780     | 420 | 5,262,600   | 4,650,000  | 612,600 |
  | 2  | 810     | 380 | 5,346,000   | 4,720,000  | 626,000 |
  | 3  | 850     | 250 | 5,320,000   | 4,780,000  | 540,000 |
  | 4  | 900     | 120 | 5,346,000   | 4,850,000  | 496,000 |
  | 5  | 920     | 30  | 5,338,000   | 4,910,000  | 428,000 |
  | 6  | 880     | 0   | 5,026,000   | 4,600,000  | 426,000 |
  | 7  | 870     | 0   | 4,974,000   | 4,550,000  | 424,000 |
  | 8  | 850     | 0   | 4,870,000   | 4,460,000  | 410,000 |
  | 9  | 900     | 40  | 5,202,000   | 4,750,000  | 452,000 |
  | 10 | 880     | 180 | 5,370,000   | 4,820,000  | 550,000 |
  | 11 | 820     | 310 | 5,322,000   | 4,700,000  | 622,000 |
  | 12 | 790     | 400 | 5,328,000   | 4,680,000  | 648,000 |

  Yıllık doğrulanmış tasarruf: 6,234,600 kWh/yıl
  Tasarruf oranı: ~%11.5 (baz hat ortalamasına göre)
  Parasal tasarruf: 6,234,600 × €0.05/kWh (gaz) = €311,730/yıl

Tasarruf belirsizliği:
  Tasarruf belirsizliği ≈ 1.26 × CV-RMSE / (F × √n)
  F = Tasarruf oranı = 0.115
  n = 12 ay
  u(S)/S ≈ 1.26 × 0.113 / (0.115 × √12) = 0.142 / 0.398 = %35.7
  U(S) = 2 × %35.7 = %71.4 → oldukça yüksek

  Not: Düşük tasarruf oranı (%11.5) belirsizliği artırır.
  Daha uzun raporlama süresi (24 ay) belirsizliği azaltır.
```

## 5. Opsiyon D — Kalibre Edilmiş Simülasyon (Calibrated Simulation)

### 5.1 Yöntem Açıklaması

```
Opsiyon D yaklaşımı:

Prensip:
  - Tesisin enerji simülasyon modeli oluşturulur (EnergyPlus, TRNSYS, vb.)
  - Model, gerçek enerji verileriyle kalibre edilir
  - Proje öncesi ve sonrası senaryolar modelde çalıştırılır
  - Tasarruf = Model (baz senaryo) - Model (proje senaryosu)

Kalibrasyon kriterleri (ASHRAE Guideline 14):
  Aylık: CV-RMSE ≤ %15, NMBE ≤ ±%5
  Saatlik: CV-RMSE ≤ %30, NMBE ≤ ±%10

Tipik kullanım:
  - Yeni bina (baz yılı verisi yok)
  - Karmaşık HVAC etkileşimleri
  - Bina kabuğu iyileştirmeleri
  - Çoklu etkileşimli projeler

Avantaj: Etkileşim etkileri modellenir, yeni bina için uygun
Dezavantaj: Yüksek maliyet, model geliştirme uzmanlık gerektirir
```

## 6. Temel Hat Ayarlama Metodolojisi (Baseline Adjustment)

### 6.1 Rutin Düzeltmeler (Routine Adjustments)

```
Rutin düzeltmeler: Baz hat modelinde zaten yer alan değişkenler

Üretim düzeltmesi:
  E_baz_ayarlı = β₀ + β₁ × P_sonra
  Baz model üretim-enerji ilişkisini kullanarak, proje sonrası
  üretim miktarına göre beklenen tüketimi hesaplar.

İklim düzeltmesi:
  E_baz_ayarlı = β₀ + β₁ × P_sonra + β₂ × HDD_sonra
  Isıtma/soğutma derecesi gün verisi ile iklim etkisi düzeltilir.

Önemli: Rutin düzeltmeler otomatiktir — regresyon modeli zaten bu
değişkenleri içerir. Proje sonrası dönemin gerçek üretim ve iklim
verileri modele girildiğinde düzeltme otomatik yapılır.
```

### 6.2 Rutin Dışı Düzeltmeler (Non-Routine Adjustments — NRA)

```
Rutin dışı düzeltmeler: Regresyon modelinde olmayan, beklenen değişiklikler

Tipik NRA durumları:
  1. Üretim hattı eklenmesi/kaldırılması
  2. Çalışma saatlerinde kalıcı değişiklik
  3. Tesis genişleme veya küçülme
  4. Yeni ekipman eklenmesi (M&V kapsamı dışı)
  5. Yakıt değişikliği
  6. Tarife yapısı değişikliği (parasal tasarruf için)

NRA hesaplama:
  E_baz_ayarlı_final = E_baz_ayarlı_rutin + NRA

  NRA = ΔE_değişiklik = E_yeni_koşul - E_eski_koşul

Örnek:
  Baz dönemde 2 vardiya, proje sonrası 3 vardiya
  Ek vardiya enerji tüketimi: +150,000 kWh/ay (hesaplanan)
  NRA = +150,000 kWh/ay (baz hat yukarı düzeltilir)
  Aksi halde tasarruf olduğundan düşük görünür

Belgeleme: Her NRA için gerekçe, hesaplama ve onay kaydı tutulmalıdır.
```

### 6.3 Etkileşim Etkileri (Interactive Effects)

```
Etkileşim etkisi: Bir projenin başka bir sistemin enerji tüketimini etkilemesi

Tipik örnekler:
  1. Aydınlatma → HVAC: LED'e geçiş ısı üretimini azaltır
     → Kışın ısıtma yükü artar (+), yazın soğutma yükü azalır (-)
     Etkileşim: 0.12-0.25 kW_soğutma/kW_aydınlatma tasarrufu

  2. Kompresör → Isıtma: Verimli kompresör daha az atık ısı üretir
     → Isı geri kazanımından faydalanıyorsa ısıtma tüketimi artar
     Etkileşim: 0.50-0.80 kW_ısı_kayıp/kW_kompresör_tasarrufu

  3. Bina kabuğu → HVAC: İzolasyon iyileştirme
     → Isıtma ve soğutma yükleri değişir
     Etkileşim: Hesabı simülasyon gerektirir

Etkileşim hesaplama yaklaşımları:
  - Basit: Katsayı yöntemi (yukarıdaki oranlar)
  - Orta: Mühendislik hesabı (enerji dengesi)
  - Gelişmiş: Simülasyon (Opsiyon D)

IPMVP yaklaşımı:
  Opsiyon A/B: Etkileşim ayrıca hesaplanır ve raporlanır
  Opsiyon C: Etkileşim otomatik olarak fatura verisine yansır
  Opsiyon D: Etkileşim model tarafından hesaplanır
```

## 7. Tasarruf Hesaplama Formülleri

### 7.1 Temel Tasarruf Formülü

```
Genel IPMVP tasarruf formülü:

Tasarruf = (E_baz_ayarlı - E_sonra) ± NRA

Burada:
  E_baz_ayarlı = Baz hat modeli ile hesaplanan beklenen tüketim
                  (proje sonrası koşullara göre düzeltilmiş)
  E_sonra = Proje sonrası dönemde ölçülen gerçek tüketim
  NRA = Rutin dışı düzeltmeler (±)

Detaylı form:
  E_baz_ayarlı = f(x₁_sonra, x₂_sonra, ...) + Σ NRAᵢ

  Burada:
    f() = Baz dönem regresyon modeli
    x₁_sonra, x₂_sonra = Proje sonrası bağımsız değişken değerleri
    NRAᵢ = i-inci rutin dışı düzeltme
```

### 7.2 Aylık ve Yıllık Tasarruf

```
Aylık tasarruf:
  S_ay_j = Ê_j - E_j + NRA_j

Yıllık tasarruf:
  S_yıl = Σⱼ₌₁¹² S_ay_j = Σⱼ₌₁¹² (Ê_j - E_j + NRA_j)

Kümülatif tasarruf (sözleşme dönemi):
  S_kümülatif = Σₖ₌₁ᴺ S_yıl_k

Burada:
  Ê_j = j. ayda beklenen (ayarlı baz hat) tüketim
  E_j = j. ayda gerçekleşen tüketim
  NRA_j = j. ayda rutin dışı düzeltme
  N = Sözleşme süresi (yıl)
```

### 7.3 Parasal Tasarruf

```
Parasal tasarruf hesaplama:

Enerji bazlı:
  S_€ = S_kWh × p_kWh + S_Nm³ × p_Nm³

Burada:
  S_kWh = Elektrik tasarrufu [kWh]
  p_kWh = Elektrik birim fiyatı [€/kWh]
  S_Nm³ = Doğalgaz tasarrufu [Nm³]
  p_Nm³ = Doğalgaz birim fiyatı [€/Nm³]

Talep (demand) tasarrufu dahil:
  S_€_toplam = S_€_enerji + S_€_talep + S_€_reaktif

  S_€_talep = ΔP_peak × p_demand × 12 [€/yıl]
  S_€_reaktif = ΔQ × p_reaktif [€/yıl]

Burada:
  ΔP_peak = Puant güç azalması [kW]
  p_demand = Talep bedeli [€/kW/ay]
```

## 8. Tipik M&V Maliyetleri

| Proje büyüklüğü | Opsiyon A | Opsiyon B | Opsiyon C | Opsiyon D |
|---|---|---|---|---|
| Küçük (<€50,000) | €500-1,500 | €1,500-5,000 | €1,000-3,000 | €5,000-15,000 |
| Orta (€50-200,000) | €1,000-3,000 | €3,000-10,000 | €2,000-5,000 | €10,000-30,000 |
| Büyük (€200,000-1M) | €2,000-8,000 | €5,000-25,000 | €3,000-10,000 | €15,000-50,000 |
| Çok büyük (>€1M) | €5,000-15,000 | €10,000-50,000 | €5,000-20,000 | €25,000-80,000 |
| M&V/Proje oranı | %1-3 | %3-10 | %1-5 | %5-15 |

## 9. M&V Planı Geliştirme

### 9.1 M&V Planı Şablon Taslağı

```
M&V Planı İçindekiler:

1. Proje Tanımı
   1.1 Proje kapsamı ve açıklaması
   1.2 Uygulanan enerji verimlilik önlemleri (EVO)
   1.3 Beklenen tasarruf (hesaplama)

2. IPMVP Opsiyon Seçimi
   2.1 Seçilen opsiyon ve gerekçesi
   2.2 Ölçüm sınırı tanımı (metering boundary)
   2.3 Etkileşim etkileri değerlendirmesi

3. Baz Dönem
   3.1 Baz dönem tarihleri
   3.2 Baz dönem enerji verileri
   3.3 Baz dönem bağımsız değişkenler
   3.4 Baz hat modeli (regresyon/hesaplama)
   3.5 Model istatistikleri (R², CV-RMSE, NMBE)

4. Raporlama Dönemi
   4.1 Raporlama dönemi tarihleri
   4.2 Ölçüm periyodikliği
   4.3 Veri toplama yöntemi

5. Ölçüm ve Cihazlar
   5.1 Ölçüm noktaları
   5.2 Cihaz spesifikasyonları
   5.3 Kalibrasyon programı
   5.4 Veri doğrulama prosedürü

6. Tasarruf Hesaplama Yöntemi
   6.1 Tasarruf formülleri
   6.2 Rutin düzeltme prosedürü
   6.3 Rutin dışı düzeltme prosedürü
   6.4 Belirsizlik analizi

7. Raporlama
   7.1 Rapor formatı ve sıklığı
   7.2 Rapor dağıtımı ve onay
   7.3 Anlaşmazlık çözüm mekanizması

8. Kalite Güvence
   8.1 Veri kalite kontrol
   8.2 Sorumluluklar
   8.3 Revizyon prosedürü
```

### 9.2 Ölçüm ve Raporlama Dönemleri

| Dönem | Süre | Amaç | Çıktı |
|---|---|---|---|
| Ön değerlendirme | 1-3 ay | M&V planı geliştirme | M&V planı dokümanı |
| Baz dönem ölçümü | 12-24 ay | Baz hat modeli oluşturma | Regresyon modeli, istatistikler |
| Uygulama dönemi | 1-6 ay | Projelerin uygulanması | Uygulama raporu |
| Raporlama dönemi (yıl 1) | 12 ay | İlk yıl tasarruf doğrulama | Yıllık M&V raporu |
| Raporlama dönemi (yıl 2+) | 12 ay/dönem | Devam eden doğrulama | Yıllık M&V raporu |
| Sözleşme sonu | — | Final değerlendirme | Kümülatif tasarruf raporu |

## İlgili Dosyalar

- [Veri Toplama](data_collection.md) — Ölçüm cihazları ve veri yönetimi
- [Performans Göstergeleri](performance_indicators.md) — KPI izleme, trend analizi, CUSUM
- [Ekonomik Analiz](economic_analysis.md) — Tasarruf ekonomik değerlendirmesi, ESCO
- [Raporlama](reporting.md) — M&V rapor formatları
- [Uygulama](implementation.md) — Proje uygulama ve ESCO modelleri
- [Fabrika Benchmarkları](factory_benchmarks.md) — Sektörel referans değerler
- [Kazan Formüller](../boiler/formulas.md) — Kazan verim hesaplama formülleri
- [Kompresör Formüller](../compressor/formulas.md) — Kompresör güç ve tasarruf formülleri
- [Chiller Formüller](../chiller/formulas.md) — Chiller COP ve exergy formülleri

## Referanslar

- EVO, "International Performance Measurement and Verification Protocol (IPMVP)," Efficiency Valuation Organization, 2022
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations"
- FEMP, "M&V Guidelines: Measurement and Verification for Performance-Based Contracts," Version 4.0, US DOE, 2015
- Reddy, T.A. et al., "Baselining Methodology for Facility-Level Monthly Energy Use," ASHRAE Transactions, 1997
- Kissock, K. et al., "Measuring Industrial Energy Savings," Applied Energy, 2008
- Granderson, J. et al., "Accuracy of Automated Measurement and Verification (M&V) Techniques for Energy Savings in Commercial Buildings," Applied Energy, 2016
- JCGM 100:2008, "Guide to the Expression of Uncertainty in Measurement (GUM)"
