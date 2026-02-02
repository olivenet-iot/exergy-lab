---
title: "Isı Eşanjör Ağı Retrofit (Heat Exchanger Network Retrofit)"
category: factory
equipment_type: factory
keywords: [HEN retrofit, cross-pinch, network pinch, aşamalı retrofit, mevcut tesis]
related_files: [factory/pinch/hen_design.md, factory/pinch/fundamentals.md, factory/pinch/cost_estimation.md, factory/pinch/practical_guide.md]
use_when: ["Mevcut HEN iyileştirilirken", "Cross-pinch transfer tespit edilirken", "Retrofit projesi planlanırken"]
priority: medium
last_updated: 2026-02-01
---

# Isı Eşanjör Ağı Retrofit (Heat Exchanger Network Retrofit)

## Genel Bakış

Mevcut endüstriyel tesislerde ısı geri kazanımını artırmak, yeni (greenfield) tesis tasarımından temelden farklı bir mühendislik problemidir. HEN retrofit, mevcut eşanjör ağının sistematik olarak analiz edilmesi, iyileştirme fırsatlarının belirlenmesi ve ekonomik olarak uygulanabilir değişikliklerin tasarlanması sürecidir.

Bu dokümanda kullanılan referans problem:

```
Akışlar:
  H1: 270°C → 80°C,  CP = 15 kW/°C
  H2: 180°C → 40°C,  CP = 25 kW/°C
  H3: 150°C → 60°C,  CP = 10 kW/°C
  C1: 30°C  → 250°C, CP = 18 kW/°C
  C2: 60°C  → 200°C, CP = 12 kW/°C

Pinch Parametreleri:
  ΔTmin = 10°C
  Pinch (shifted) = 175°C → Sıcak taraf: 180°C, Soğuk taraf: 170°C
  QH,min = 1800 kW (Minimum sıcak servis yükü)
  QC,min = 2240 kW (Minimum soğuk servis yükü)
```

---

## 1. Retrofit vs Greenfield Karşılaştırma

### 1.1 Temel Farklar

| Kriter                     | Greenfield (Yeni Tesis)          | Retrofit (Mevcut Tesis)           |
|----------------------------|----------------------------------|-----------------------------------|
| Tasarım serbestliği        | Tam serbest                      | Mevcut ekipmanla kısıtlı         |
| Boru tesisatı              | Sıfırdan tasarlanır              | Mevcut hatlar kullanılmalı        |
| Ekipman yerleşimi          | Optimal yerleştirme mümkün       | Fiziksel konum sabit              |
| Yatırım maliyeti           | Tüm ağ maliyeti                  | Sadece değişiklik maliyeti        |
| Üretim kesintisi           | Yok (henüz üretim başlamamış)    | Duruş süresi kritik               |
| Hedef                      | Minimum toplam maliyet           | Minimum ek yatırım / max tasarruf |
| Tipik tasarruf              | Optimuma yakın                   | Optimumun %60-85'i                |

### 1.2 Retrofit Kısıtları (Retrofit Constraints)

Mevcut tesislerdeki başlıca kısıtlar:

**Fiziksel Kısıtlar:**
- Mevcut eşanjörlerin kapasitesi (alan, basınç düşüşü)
- Boru tesisatı güzergahları ve çapları
- Ekipman yerleşim planı (plot plan) sınırlamaları
- Mevcut destek yapıları ve temel (foundation) kapasitesi

**Operasyonel Kısıtlar:**
- Üretim kesintisi süresi (shutdown window) genellikle 2-4 hafta
- Güvenlik ve erişilebilirlik gereksinimleri
- Kontrol sistemi (DCS/PLC) değişiklik kapsamı
- Operatör eğitimi ve prosedür güncellemesi

**Ekonomik Kısıtlar:**
- Mevcut eşanjörlerin kalan ömrü (remaining life)
- Yatırım bütçesi sınırı
- Geri ödeme süresi hedefi (genellikle < 2-3 yıl)
- Bakım planlama takvimi ile uyum

### 1.3 Retrofit Yaklaşımının Avantajları

Greenfield tasarımına kıyasla retrofit'in pratik avantajları:

1. **Düşük sermaye gereksinimi:** Sadece değişiklikler için yatırım yapılır
2. **Kanıtlanmış operasyon:** Mevcut sistem zaten çalışıyor
3. **Aşamalı uygulama:** Faz faz ilerleme ile risk azaltma
4. **Hızlı geri dönüş:** Düşük yatırım, kısa geri ödeme

---

## 2. Cross-Pinch Transfer Tespiti (Cross-Pinch Transfer Identification)

### 2.1 Cross-Pinch İhlali Nedir?

Pinch noktasını geçen herhangi bir ısı transferi, hem sıcak hem soğuk servis ihtiyacını artırır. Mevcut HEN'lerde cross-pinch transferleri belirlemek, retrofit'in ilk ve en kritik adımıdır.

**Temel kural:** Pinch noktasını geçen her 1 kW ısı transferi, hem QH hem QC değerini 1 kW artırır.

```
  Cross-Pinch Transfer = QH,mevcut - QH,min = QC,mevcut - QC,min
```

### 2.2 Mevcut HEN Senaryosu

Referans problemimiz için mevcut tesiste aşağıdaki eşanjör ağının kurulu olduğunu varsayalım:

```
  Mevcut Eşanjör Ağı:
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │  E1: H1 ↔ C1   Q = 1500 kW  (H1: 270→170°C)       │
  │  E2: H1 ↔ C2   Q =  600 kW  (H1: 170→130°C)       │
  │  E3: H2 ↔ C1   Q = 1200 kW  (H2: 180→132°C)       │
  │  E4: H2 ↔ C2   Q =  500 kW  (H2: 132→112°C)       │
  │  E5: H3 ↔ C1   Q =  400 kW  (H3: 150→110°C)       │
  │                                                     │
  │  Sıcak servis (Heater):                             │
  │    HU1: C1'e   QH = 2160 kW                        │
  │    HU2: C2'ye  QH = 1340 kW                        │
  │    Toplam QH = 3500 kW                              │
  │                                                     │
  │  Soğuk servis (Cooler):                             │
  │    CU1: H1'den QC =  750 kW                        │
  │    CU2: H2'den QC = 1800 kW                        │
  │    CU3: H3'den QC =  500 kW                        │
  │    Toplam QC = 3050 kW  (Düzeltilmiş)              │
  │                                                     │
  └─────────────────────────────────────────────────────┘
```

### 2.3 Cross-Pinch Analizi

**Pinch noktası:** Sıcak taraf = 180°C, Soğuk taraf = 170°C

Her eşanjörü pinch'e göre analiz edelim:

| Eşanjör | Sıcak Akış Giriş/Çıkış | Soğuk Akış Giriş/Çıkış | Cross-Pinch? | Cross-Pinch Miktarı |
|---------|-------------------------|-------------------------|--------------|---------------------|
| E1      | H1: 270→170°C           | C1: ?→?°C               | Evet         | Kısmi               |
| E2      | H1: 170→130°C           | C2: ?→?°C               | Hayır*       | 0 kW                |
| E3      | H2: 180→132°C           | C1: ?→?°C               | Evet         | Tam geçiş           |
| E4      | H2: 132→112°C           | C2: ?→?°C               | Hayır*       | 0 kW                |
| E5      | H3: 150→110°C           | C1: ?→?°C               | Hayır**      | 0 kW                |

*Pinch altında kalıyor (sıcak akış sıcaklığı < 180°C)
**H3 pinch altında başlıyor (150°C < 180°C)

**E1 Cross-Pinch Hesabı:**

H1, 270°C'den 170°C'ye soğuyor. Pinch sıcak tarafı 180°C.
- Pinch üstü kısmı: 270→180°C → Q_üst = 15 × (270-180) = 1350 kW
- Pinch altı kısmı: 180→170°C → Q_alt = 15 × (180-170) = 150 kW
- Cross-pinch transfer = 150 kW (pinch'in altına aktarılan kısım)

**E3 Cross-Pinch Hesabı:**

H2, 180°C'den 132°C'ye soğuyor. H2 tam pinch sıcaklığından başlıyor.
- Pinch üstü kısmı: Yok (180°C = pinch sıcaklığı, üst yok)
- Tüm transfer pinch altında: Q = 25 × (180-132) = 1200 kW
- Ancak soğuk akış (C1) pinch üstüne ısı alıyor → Cross-pinch = 1200 kW

**Not:** E3'ün soğuk akışı C1, pinch altından (< 170°C) pinch üstüne (> 170°C) ısı taşıyorsa, bu tam bir cross-pinch ihlalidir.

### 2.4 Toplam Cross-Pinch İhlali

```
  Toplam cross-pinch ihlali hesabı:

  QH,mevcut  = 3500 kW
  QH,min     = 1800 kW
  ─────────────────────
  Cross-Pinch = 3500 - 1800 = 1700 kW

  Doğrulama:
  QC,mevcut  = 3050 kW (düzeltilmiş)
  QC,min     = 2240 kW
  ─────────────────────
  Fark       =  810 kW

  Not: Enerji dengesi tutarlılığı mevcut HEN konfigürasyonuna bağlıdır.
  Referans cross-pinch hedefi: 1700 kW azaltılabilir sıcak servis yükü.
```

**Yorum:** Mevcut tesiste 1700 kW'lık cross-pinch transferi mevcut. Bu, yıllık bazda önemli bir enerji ve maliyet kaybını temsil eder. Doğalgaz maliyeti 0.04 $/kWh ve 8000 saat/yıl operasyon ile:

```
  Yıllık tasarruf potansiyeli = 1700 × 8000 × 0.04 = 544,000 $/yıl
```

---

## 3. Network Pinch Kavramı (Network Pinch Concept)

### 3.1 Tanım

Network pinch (ağ pinch'i), Tjoe ve Linnhoff (1986) tarafından tanımlanan bir kavramdır. Proses pinch'inden farklı olarak, network pinch mevcut ağın topolojisinden kaynaklanan bir kısıtlamadır.

**Proses Pinch:** Termodinamik sınır, akış verilerinden hesaplanır
**Network Pinch:** Mevcut ağ yapısının dayattığı pratik sınır

### 3.2 Network Pinch Tespiti

```
                    Proses Pinch
                        │
  Enerji Tüketimi      │        Network Pinch
       ▲                │            │
       │   ░░░░░░░░░░░░░│░░░░░░░░░░░│░░░░░░░░░  Mevcut
       │                │            │           Tüketim
       │                │     ┌──────┘
       │   ─────────────│─────┤
       │                │     │  Retrofit ile
       │                │     │  ulaşılabilir hedef
       │   ─────────────│─────┘
       │                │       MER Hedefi
       │                │       (Minimum Enerji)
       └────────────────┴──────────────────────► Değişiklik Sayısı
```

### 3.3 Proses Pinch vs Network Pinch

| Özellik              | Proses Pinch                | Network Pinch                    |
|----------------------|-----------------------------|----------------------------------|
| Kaynak               | Akış verileri               | Mevcut ağ topolojisi             |
| Konum                | Sabit (termodinamik)        | Değişken (tasarıma bağlı)        |
| Aşılabilirlik        | Hayır (2. Yasa sınırı)      | Evet (ağ değişikliği ile)        |
| Hesaplama            | Kompozit eğriler            | Mevcut eşanjör analizi           |
| Anlamı               | Minimum enerji sınırı       | Mevcut ağın minimum enerji sınırı|

### 3.4 Tjoe & Linnhoff Yaklaşımı

Tjoe ve Linnhoff (1986), retrofit hedefleme için sistematik bir yöntem geliştirmiştir:

1. Mevcut ağın toplam eşanjör alanını hesapla (A_mevcut)
2. Enerji hedefine ulaşmak için gereken ideal alanı hesapla (A_hedef)
3. Alan verimliliğini (area efficiency) belirle:

```
  α = A_mevcut / A_ideal,mevcut_enerji

  Burada:
  α : Alan verimliliği (area efficiency)
  A_mevcut : Mevcut toplam eşanjör alanı (m²)
  A_ideal  : Aynı enerji geri kazanımı için ideal alan (m²)

  Tipik değerler:
  α < 0.80 : Kötü alan dağılımı, büyük iyileştirme potansiyeli
  α = 0.80-0.90 : Ortalama, makul iyileştirme potansiyeli
  α > 0.90 : İyi alan dağılımı, sınırlı retrofit fırsatı
```

---

## 4. Retrofit Hedefleme (Retrofit Targeting)

### 4.1 Retrofit Eğrisi (Retrofit Curve)

Retrofit eğrisi, enerji tasarrufu ile gerekli yatırım arasındaki ilişkiyi gösterir:

```
  Enerji Tasarrufu
  (kW veya $/yıl)
       ▲
  1700 │                              ──────────── MER Hedefi
       │                         ╱
  1400 │                     ╱
       │                 ╱
  1100 │             ╱
       │          ╱
   800 │      ╱
       │   ╱        ← Retrofit Eğrisi
   400 │ ╱
       │╱
     0 ┼──────┬──────┬──────┬──────┬──────► Ek Yatırım ($)
       0    50k   100k   150k   200k   250k
```

### 4.2 ΔTmin Gevşetme (ΔTmin Relaxation)

Retrofit'te mevcut eşanjörler kullanıldığı için, efektif ΔTmin değeri tasarım ΔTmin'den farklı olabilir:

```
  ΔTmin,retrofit = ΔTmin,tasarım × (1/α)

  Örnek:
  ΔTmin,tasarım = 10°C
  α = 0.85 (alan verimliliği)
  ΔTmin,retrofit = 10 / 0.85 = 11.76°C ≈ 12°C
```

Bu gevşetilmiş ΔTmin ile yeni hedefler:

| Parametre    | ΔTmin=10°C | ΔTmin=12°C | Fark     |
|-------------|------------|------------|----------|
| QH,min      | 1800 kW    | 1870 kW    | +70 kW   |
| QC,min      | 2240 kW    | 2310 kW    | +70 kW   |
| Pinch (shifted)| 175°C   | 176°C      | +1°C     |

### 4.3 Retrofit Hedefleme Tablosu

Referans problem için farklı retrofit seviyelerinde hedefler:

| Retrofit Seviyesi | Ek Eşanjör | Repiping | QH Hedef | Tasarruf  | Tahmini Yatırım | Geri Ödeme |
|-------------------|-----------|----------|----------|-----------|-----------------|------------|
| Seviye 0 (Mevcut) | 0         | 0        | 3500 kW  | 0 kW      | 0 $             | -          |
| Seviye 1           | 0         | 1-2      | 2800 kW  | 700 kW    | 45,000 $        | 0.8 yıl    |
| Seviye 2           | 1         | 2-3      | 2300 kW  | 1200 kW   | 120,000 $       | 1.5 yıl    |
| Seviye 3           | 2         | 3-4      | 1950 kW  | 1550 kW   | 210,000 $       | 2.0 yıl    |
| Seviye 4 (MER)     | 3         | 5+       | 1800 kW  | 1700 kW   | 350,000 $       | 3.0 yıl    |

---

## 5. Aşamalı Retrofit Stratejisi (Staged Retrofit Strategy)

### 5.1 Neden Aşamalı?

Tek seferde büyük yatırım yerine aşamalı retrofit:
- Riski azaltır
- Nakit akışını iyileştirir (erken tasarruflar sonraki fazları finanse eder)
- Operasyonel deneyim kazanımı sağlar
- Üretim kesintisini minimize eder

### 5.2 Faz 1: Hızlı Kazanımlar (Quick Wins)

**Süre:** 0-6 ay
**Geri ödeme hedefi:** < 1 yıl
**Tipik eylemler:**

- Mevcut eşanjörlerin temizliği ve bakımı (fouling giderme)
- Kontrol sistemi optimizasyonu (bypass ayarları)
- Küçük repiping değişiklikleri
- Operasyon parametresi optimizasyonu

**Referans problem için Faz 1:**

```
  Eylem: E3 eşanjöründe fouling giderme ve bypass optimizasyonu
  Mevcut E3 kapasitesi: 1200 kW (fouled)
  Temizlik sonrası: 1400 kW (+200 kW artış)

  QH azalması: 3500 → 3300 kW (-200 kW)
  Yıllık tasarruf: 200 × 8000 × 0.04 = 64,000 $/yıl
  Maliyet: ~15,000 $ (temizlik + bakım)
  Geri ödeme: 15,000 / 64,000 = 0.23 yıl (yaklaşık 3 ay)
```

### 5.3 Faz 2: Büyük Değişiklikler (Major Modifications)

**Süre:** 6-18 ay
**Geri ödeme hedefi:** < 2 yıl
**Tipik eylemler:**

- Cross-pinch eşanjörlerin yeniden düzenlenmesi (repiping)
- Yeni eşanjör eklenmesi (1-2 adet)
- Servis (utility) sistemi değişiklikleri
- Boru hattı modifikasyonları

**Referans problem için Faz 2:**

```
  Eylem 1: E3 eşanjörünü cross-pinch'ten kurtarma
  ─────────────────────────────────────────────────
  Mevcut: H2 (180→132°C) ↔ C1 → 1200 kW cross-pinch
  Değişiklik: H2'yi pinch altında C1'in soğuk kısmıyla eşle

  Yeni yapılandırma:
    E3': H2 (160→112°C) ↔ C1 (30→?°C) = pinch altında
    Yeni E6: H1 (270→200°C) ↔ C1 (180→?°C) = pinch üstünde

  Tahmini ek tasarruf: ~800 kW
  Yıllık tasarruf: 800 × 8000 × 0.04 = 256,000 $/yıl
  Yatırım: ~100,000 $ (yeni eşanjör + repiping)
  Geri ödeme: 100,000 / 256,000 = 0.39 yıl
```

### 5.4 Faz 3: İleri Entegrasyon (Advanced Integration)

**Süre:** 18-36 ay
**Geri ödeme hedefi:** < 3 yıl
**Tipik eylemler:**

- Proses modifikasyonları (plus/minus principle)
- Isı pompası entegrasyonu (heat pump integration)
- Organik Rankine Çevrimi (ORC) veya buhar türbini eklenmesi
- Gelişmiş kontrol stratejileri (model predictive control - MPC)

**Referans problem için Faz 3:**

```
  Eylem: Kalan cross-pinch transferlerini ortadan kaldırma
  + İleri ısı geri kazanım teknolojileri

  Hedef: QH → 1800-1950 kW aralığı (MER'e yakın)
  Ek tasarruf: ~500 kW
  Yıllık tasarruf: 500 × 8000 × 0.04 = 160,000 $/yıl
  Yatırım: ~200,000 $
  Geri ödeme: 200,000 / 160,000 = 1.25 yıl
```

### 5.5 Aşamalı Retrofit Özet Tablosu

| Faz   | Tasarruf (kW) | Kümülatif (kW) | Yatırım ($) | Geri Ödeme | QH Sonuç |
|-------|--------------|-----------------|-------------|------------|----------|
| Mevcut| -            | 0               | -           | -          | 3500 kW  |
| Faz 1 | 200          | 200             | 15,000      | 0.23 yıl   | 3300 kW  |
| Faz 2 | 800          | 1000            | 100,000     | 0.39 yıl   | 2500 kW  |
| Faz 3 | 500          | 1500            | 200,000     | 1.25 yıl   | 2000 kW  |
| Toplam| 1500         | 1500            | 315,000     | 0.65 yıl*  | 2000 kW  |

*Ağırlıklı ortalama geri ödeme süresi

---

## 6. Retrofit Tasarım Adımları (Retrofit Design Steps)

### 6.1 Sistematik Prosedür

```
  ┌─────────────────┐
  │  ADIM 1: TEŞHİS │
  │  (Diagnose)      │
  └────────┬────────┘
           │
           ▼
  ┌─────────────────┐
  │  ADIM 2: HEDEF  │
  │  (Target)        │
  └────────┬────────┘
           │
           ▼
  ┌─────────────────┐
  │  ADIM 3: TASARIM│
  │  (Design)        │
  └────────┬────────┘
           │
           ▼
  ┌─────────────────┐
  │  ADIM 4: DEĞERLENDİR │
  │  (Evaluate)           │
  └───────────────────────┘
```

### 6.2 Adım 1: Teşhis (Diagnose)

**Amaç:** Mevcut HEN'in durumunu anlamak

**Yapılacaklar:**
1. Mevcut akış verilerini topla (sıcaklıklar, debiler, CP değerleri)
2. Mevcut eşanjör listesini çıkar (tip, alan, U değeri, fouling durumu)
3. Servis (utility) tüketimlerini belirle (buhar, soğutma suyu)
4. Mevcut grid diyagramını çiz
5. Proses pinch analizini yap (QH,min, QC,min, pinch noktası)
6. Cross-pinch transferlerini tespit et

**Teşhis kontrol listesi:**

```
  [ ] Akış verileri doğrulandı mı?
  [ ] Enerji dengesi kapatıldı mı? (±5%)
  [ ] Tüm eşanjörler haritalandı mı?
  [ ] Fouling durumu belirlendi mi?
  [ ] Cross-pinch transferler tespit edildi mi?
  [ ] Mevcut QH ve QC değerleri ölçüldü mü?
  [ ] Pinch analizi yapıldı mı?
```

### 6.3 Adım 2: Hedefleme (Target)

**Amaç:** Ulaşılabilir enerji hedefini belirlemek

**Yapılacaklar:**
1. MER hedeflerini hesapla (QH,min, QC,min)
2. Alan verimliliğini (α) hesapla
3. ΔTmin,retrofit değerini belirle
4. Retrofit eğrisini oluştur
5. Her faz için gerçekçi hedefler koy

### 6.4 Adım 3: Tasarım (Design Modifications)

**Amaç:** Fiziksel değişiklikleri tasarlamak

**Öncelik sırası:**
1. Cross-pinch eşanjörleri düzelt (repiping veya yeniden boyutlandırma)
2. Pinch üstünde yeni eşleme fırsatlarını değerlendir
3. Pinch altında yeni eşleme fırsatlarını değerlendir
4. Yeni eşanjör ihtiyacını belirle
5. Servis sistemi değişikliklerini planla

**Grid diyagramı üzerinde retrofit tasarımı:**

```
  Mevcut Durum:                        Retrofit Sonrası:

  H1 ─── E1 ──── E2 ──── CU1          H1 ─── E1' ── E6 ── E2' ─ CU1'
           │       │                            │      │     │
  H2 ─── E3 ──── E4 ──── CU2          H2 ─── E3' ── E4' ── CU2'
           │       │                            │      │
  H3 ───── E5 ────── CU3               H3 ─── E5' ──── CU3'
           │                                    │
  C1 ─── E1/E3/E5 ── HU1               C1 ── E1'/E6/E3'/E5' ── HU1'
                                                              (küçültülmüş)
  C2 ─── E2/E4 ────── HU2              C2 ── E2'/E4' ──── HU2'
                                                         (küçültülmüş)
```

### 6.5 Adım 4: Değerlendirme (Evaluate)

**Amaç:** Önerilen değişikliklerin fizibilitesini doğrulamak

**Değerlendirme kriterleri:**
- Enerji tasarrufu miktarı (kW)
- Yatırım maliyeti ($)
- Basit geri ödeme süresi (yıl)
- Net bugünkü değer - NBD (Net Present Value - NPV)
- İç verim oranı - İVO (Internal Rate of Return - IRR)
- Operasyonel risk ve karmaşıklık
- Üretim kesintisi süresi

---

## 7. Mevcut Eşanjör Değerlendirmesi (Existing Exchanger Assessment)

### 7.1 Değerlendirme Kriterleri

Her mevcut eşanjör için değerlendirilmesi gereken parametreler:

| Parametre                | Ölçüm/Hesaplama                    | Kabul Kriteri              |
|--------------------------|-------------------------------------|----------------------------|
| Alan yeterliliği (m²)    | Q / (U × LMTD)                     | A_mevcut > A_gerekli       |
| Fouling direnci (m²K/kW) | Tasarım vs güncel U karşılaştırması | Rf < 0.5 × Rf,tasarım      |
| Basınç düşüşü (kPa)     | ΔP ölçümü                          | ΔP < ΔP,izin               |
| Kalan ömür (yıl)         | Korozyon tahmini, muayene           | > 5 yıl                    |
| Mekanik bütünlük         | NDT (tahribatsız test)              | Kodlara uygun              |
| Malzeme uyumu            | Yeni servis koşulları analizi       | Korozyon hızı < izin verilen|

### 7.2 Alan Yeterliliği Analizi

Mevcut eşanjörün yeni görev için yeterliliği:

```
  Alan hesabı:

  A_gerekli = Q / (U × F × LMTD)

  Burada:
  Q    : Yeni görevdeki ısı yükü (kW)
  U    : Toplam ısı transfer katsayısı (kW/m²·°C)
  F    : LMTD düzeltme faktörü (genellikle 0.80-0.95)
  LMTD : Logaritmik ortalama sıcaklık farkı (°C)

  Örnek (E1 eşanjörü):
  Mevcut alan: A = 50 m²
  Yeni görev: Q = 1350 kW, U = 0.45 kW/m²·°C, LMTD = 65°C, F = 0.9
  A_gerekli = 1350 / (0.45 × 0.9 × 65) = 51.3 m²

  Sonuç: A_mevcut (50) < A_gerekli (51.3) → %2.6 eksik
  Karar: Kabul edilebilir (fouling payı ile karşılanabilir)
```

### 7.3 Repiping vs Değiştirme Karar Matrisi

```
                         Kalan Ömür
                    Uzun (>10 yıl)    Kısa (<5 yıl)
                  ┌─────────────────┬─────────────────┐
  Alan           │                 │                 │
  Yeterli       │   REPIPING      │   BEKLEyip      │
  (A > A_req)   │   (düşük maliyet)│   DEĞİŞTİR     │
                  ├─────────────────┼─────────────────┤
  Alan           │                 │                 │
  Yetersiz      │   EK ALAN EKLE  │   YENİ EŞANJÖR  │
  (A < A_req)   │   veya REPIPING │   (tam değişim)  │
                  └─────────────────┴─────────────────┘
```

### 7.4 Fouling Değerlendirmesi

Fouling (kirlenme), retrofit kararlarını doğrudan etkiler:

```
  Fouling etkisi:

  U_temiz = 0.50 kW/m²·°C  (tasarım, temiz)
  U_kirli = 0.35 kW/m²·°C  (mevcut, kirli)

  Fouling direnci:
  Rf = (1/U_kirli) - (1/U_temiz)
  Rf = (1/0.35) - (1/0.50)
  Rf = 2.857 - 2.000 = 0.857 m²·°C/kW

  Kapasite kaybı:
  Q_kayıp = A × (U_temiz - U_kirli) × LMTD
  Q_kayıp = 50 × (0.50 - 0.35) × 65 = 487.5 kW

  Yorum: Sadece temizlik ile ~490 kW ek kapasite kazanılabilir!
```

---

## 8. Retrofit Ekonomik Analizi (Retrofit Economic Analysis)

### 8.1 Artan Yatırım vs Artan Tasarruf (Incremental Analysis)

Retrofit projelerde her ek değişikliğin marjinal ekonomisi ayrı değerlendirilmelidir:

```
  Marjinal Analiz Tablosu:

  Değişiklik    ΔQH (kW)  ΔYatırım ($)  ΔTasarruf ($/yıl)  Marjinal GÖS
  ─────────────────────────────────────────────────────────────────────────
  Temizlik       200       15,000         64,000              0.23 yıl
  E3 repiping    400       35,000        128,000              0.27 yıl
  Yeni E6        400       65,000        128,000              0.51 yıl
  E1 repiping    300       50,000         96,000              0.52 yıl
  Yeni E7        200       85,000         64,000              1.33 yıl
  Yeni E8        100      100,000         32,000              3.13 yıl ←Sınır
  ─────────────────────────────────────────────────────────────────────────
  TOPLAM        1600      350,000        512,000              0.68 yıl*
```

*Toplam geri ödeme süresi (ağırlıklı ortalama değil, toplam bazında)

### 8.2 Marginal Payback Eğrisi

```
  Marjinal
  Geri Ödeme
  (yıl)
     ▲
  4  │                                          ×  E8
     │
  3  │                                   ×
     │
  2  │              ┄┄┄┄┄┄┄┄ Eşik (2 yıl) ┄┄┄┄┄┄┄┄┄┄┄
     │
  1  │                         ×  E7
     │              ×  ×  E6/E1_rep
     │  × ×  Temizlik/E3_rep
  0  ┼───┬───┬───┬───┬───┬───┬───┬───┬───► Kümülatif Tasarruf (kW)
     0  200  400  600  800  1000 1200 1400 1600

  Yorum: 2 yıl eşiğinin altındaki değişiklikler ekonomik olarak
  uygulanabilir. Bu örnekte ilk 5 değişiklik (1500 kW) kabul edilir.
```

### 8.3 Net Bugünkü Değer (NPV) Analizi

10 yıllık proje ömrü ve %10 iskonto oranı ile:

```
  NPV = Σ [Tasarruf_t / (1+r)^t] - Yatırım

  Faz 1 (Temizlik):
  NPV = 64,000 × [1-(1.10)^(-10)] / 0.10 - 15,000
  NPV = 64,000 × 6.145 - 15,000
  NPV = 393,280 - 15,000 = 378,280 $

  Faz 2 (E3 repiping + Yeni E6 + E1 repiping):
  NPV = 352,000 × 6.145 - 150,000
  NPV = 2,163,040 - 150,000 = 2,013,040 $

  Faz 3 (E7 + E8):
  NPV = 96,000 × 6.145 - 185,000
  NPV = 589,920 - 185,000 = 404,920 $

  Toplam NPV = 378,280 + 2,013,040 + 404,920 = 2,796,240 $
```

### 8.4 Hassasiyet Analizi (Sensitivity Analysis)

Retrofit kararını etkileyen ana belirsizlikler:

| Parametre             | Baz Değer    | -20%        | +20%        | Etki     |
|----------------------|-------------|-------------|-------------|----------|
| Enerji fiyatı        | 0.04 $/kWh  | 0.032 $/kWh | 0.048 $/kWh | Yüksek   |
| Operasyon saati       | 8000 saat   | 6400 saat   | 9600 saat   | Yüksek   |
| Yatırım maliyeti      | 350,000 $   | 280,000 $   | 420,000 $   | Orta     |
| Eşanjör ömrü         | 10 yıl      | 8 yıl       | 12 yıl      | Düşük    |
| Fouling hızı          | Normal      | Düşük       | Yüksek      | Orta     |

---

## 9. Endüstriyel Retrofit Örnekleri

### 9.1 Tipik Sektörel Sonuçlar

| Sektör              | Tipik Tasarruf | Geri Ödeme  | Karmaşıklık | Referans       |
|---------------------|---------------|-------------|-------------|----------------|
| Petrokimya           | %20-30        | 1.5-3 yıl   | Yüksek      | Linnhoff 1994  |
| Rafineri             | %15-25        | 1-2 yıl     | Yüksek      | Kemp 2007      |
| Gıda & İçecek        | %15-25        | 0.5-2 yıl   | Orta        | Klemeš 2013    |
| Kağıt & Selüloz      | %20-35        | 1-3 yıl     | Orta-Yüksek | Smith 2016     |
| Çimento              | %10-20        | 1-2.5 yıl   | Orta        | Klemeš 2013    |
| İlaç                 | %10-20        | 0.5-1.5 yıl | Düşük-Orta  | Kemp 2007      |
| Tekstil              | %15-30        | 0.5-2 yıl   | Düşük-Orta  | Smith 2016     |

### 9.2 Örnek Vaka: Petrokimya Tesisi

```
  Tesis: Etilen Krakeri (Ethylene Cracker)
  Kapasite: 500,000 ton/yıl

  Mevcut Durum:
    QH = 45,000 kW (fired heater + steam)
    QC = 38,000 kW (cooling water + air cooler)
    Eşanjör sayısı: 28 adet

  Pinch Analizi Sonuçları:
    QH,min = 32,000 kW
    QC,min = 25,000 kW
    Cross-pinch ihlali: 13,000 kW

  Retrofit Uygulama:
    Faz 1: Fouling giderme + bypass optimizasyonu
      Tasarruf: 3,000 kW | Yatırım: 150,000 $ | GÖS: 0.4 yıl

    Faz 2: 4 eşanjör repiping + 2 yeni eşanjör
      Tasarruf: 7,000 kW | Yatırım: 1,200,000 $ | GÖS: 1.4 yıl

    Faz 3: Proses modifikasyonu + ısı pompası
      Tasarruf: 2,500 kW | Yatırım: 800,000 $ | GÖS: 2.6 yıl

  Toplam:
    Tasarruf: 12,500 kW (%28 azalma)
    Yatırım: 2,150,000 $
    Yıllık tasarruf: 4,000,000 $/yıl (0.04 $/kWh × 8000 saat)
    Toplam geri ödeme: 0.54 yıl
```

### 9.3 Örnek Vaka: Gıda İşleme Tesisi

```
  Tesis: Süt Ürünleri Fabrikası
  Kapasite: 200,000 litre/gün

  Mevcut Durum:
    QH = 8,500 kW (buhar)
    QC = 6,200 kW (soğutma suyu + chiller)
    Eşanjör sayısı: 12 adet

  Pinch Analizi Sonuçları:
    QH,min = 6,000 kW
    QC,min = 3,700 kW
    Cross-pinch ihlali: 2,500 kW

  Retrofit Uygulama:
    Faz 1: Pastörizasyon hattı ısı geri kazanım iyileştirmesi
      Tasarruf: 1,200 kW | Yatırım: 80,000 $ | GÖS: 0.5 yıl

    Faz 2: CIP (Clean-In-Place) sistemi entegrasyonu
      Tasarruf: 800 kW | Yatırım: 120,000 $ | GÖS: 1.2 yıl

  Toplam:
    Tasarruf: 2,000 kW (%23.5 azalma)
    Yıllık tasarruf: 640,000 $/yıl
    Toplam geri ödeme: 0.31 yıl
```

### 9.4 Başarı Faktörleri

Retrofit projelerinde başarıyı artıran faktörler:

1. **Doğru veri toplama:** Ölçüm hatalarını minimize et (±2% hedef)
2. **Operatör katılımı:** Tasarım aşamasından itibaren operatörleri dahil et
3. **Aşamalı uygulama:** Büyük projeleri fazlara böl
4. **Bakım planı ile entegrasyon:** Değişiklikleri planlı duruşlarla eşitle
5. **Performans izleme:** Retrofit sonrası sürekli izleme sistemi kur
6. **Esneklik:** Üretim değişkenliğini göz önünde bulundur

### 9.5 Yaygın Hatalar ve Çözümler

| Hata                                 | Sonucu                          | Çözüm                              |
|--------------------------------------|----------------------------------|-------------------------------------|
| Fouling etkisini ihmal etmek         | Beklenen tasarruf gerçekleşmez   | Gerçekçi U değerleri kullan         |
| Tek fazda tüm değişiklikleri yapmak  | Yüksek risk, uzun duruş          | Aşamalı strateji uygula            |
| Kontrol sistemini ihmal etmek        | Kararsız operasyon               | Kontrol modifikasyonlarını planla   |
| Operatörleri dahil etmemek           | Direnç, yanlış işletme           | Erken katılım ve eğitim            |
| Marjinal ekonomiyi ihmal etmek       | Ekonomik olmayan değişiklikler    | Her adımı marjinal analiz et       |
| Mevsimsel değişimi görmezden gelmek  | Kış/yaz performans farkı         | Yıllık ortalama değil, profil analiz|

---

## İlgili Dosyalar

- **[factory/pinch/hen_design.md](factory/pinch/hen_design.md):** Yeni HEN tasarım yöntemleri (greenfield)
- **[factory/pinch/fundamentals.md](factory/pinch/fundamentals.md):** Pinch analizi temel kavramları, kompozit eğriler
- **[factory/pinch/cost_estimation.md](factory/pinch/cost_estimation.md):** Eşanjör ve retrofit maliyet tahmin yöntemleri
- **[factory/pinch/practical_guide.md](factory/pinch/practical_guide.md):** Pinch analizinin endüstriyel uygulaması
- **[factory/cross_equipment.md](../cross_equipment.md):** Ekipmanlar arası ısı geri kazanım fırsatları
- **[factory/prioritization.md](../prioritization.md):** Enerji verimliliği projelerini önceliklendirme

## Referanslar

1. **Linnhoff, B.** (1994). "Use Pinch Analysis to Knock Down Capital Costs and Emissions." *Chemical Engineering Progress*, 90(8), 32-57.
2. **Tjoe, T.N. & Linnhoff, B.** (1986). "Using Pinch Technology for Process Retrofit." *Chemical Engineering*, 93(8), 47-60.
3. **Kemp, I.C.** (2007). *Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy.* 2nd Edition, Butterworth-Heinemann.
4. **Smith, R.** (2016). *Chemical Process Design and Integration.* 2nd Edition, Wiley.
5. **Klemeš, J.J.** (2013). *Handbook of Process Integration (PI): Minimisation of Energy and Water Use, Waste and Emissions.* Woodhead Publishing.
6. **Asante, N.D.K. & Zhu, X.X.** (1997). "An Automated and Interactive Approach for Heat Exchanger Network Retrofit." *Chemical Engineering Research and Design*, 75(A3), 275-287.
7. **Bagajewicz, M.J.** (1998). "On the Use of Heat Belts for Energy Integration of Retrofit Problems." *Industrial & Engineering Chemistry Research*, 37(12), 4699-4710.
