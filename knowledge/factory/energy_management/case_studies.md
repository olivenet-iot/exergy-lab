---
title: "Enerji Yönetimi Vaka Çalışmaları (Energy Management Case Studies)"
category: factory
equipment_type: factory
keywords: [vaka çalışması, case study, ISO 50001, M&V, VAP, EnPI, ESCO, EPC, otomotiv, gıda, tekstil, çimento, kimya]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/iso_50001_implementation.md, factory/energy_management/mv_ipmvp.md, factory/energy_management/turkey_incentives.md, factory/energy_management/enpi_guide.md, factory/case_studies.md]
use_when: ["Sektörel vaka çalışması referans alınacağında", "ISO 50001 uygulama örneği istendiğinde", "M&V uygulama örneği gerektiğinde"]
priority: low
last_updated: 2026-02-01
---

# Enerji Yönetimi Vaka Çalışmaları (Energy Management Case Studies)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

Bu dosya, farklı sektörlerde gerçekleştirilen enerji yönetimi uygulamalarını vaka çalışması (case study) formatında sunar. Her vaka, ISO 50001, M&V, VAP/ESCO gibi farklı yaklaşımları örnekler ve exergy perspektifinden değerlendirme içerir.

### 1.1 Vaka Çalışmaları Özeti

| No | Sektör | Konu | Yaklaşım | Yıllık Tasarruf |
|----|--------|------|----------|-----------------|
| 1 | Otomotiv | ISO 50001 Sertifikasyon | EnMS kurulumu, 14 aylık yol haritası | 450,000 €/yıl |
| 2 | Gıda | M&V ile Tasarruf Doğrulaması | IPMVP Opsiyon C, VSD retrofit | 185,000 kWh/yıl |
| 3 | Tekstil | VAP Başvurusu ve Uygulama | Buhar sistemi optimizasyonu, %25 hibe | 620,000 kWh_th/yıl |
| 4 | Çimento | EnPI ve Sürekli İyileştirme | 3 yıllık CUSUM trendi, SEC odaklı | 1,200,000 €/yıl |
| 5 | Kimya | EPC/ESCO Uygulaması | Garantili tasarruf modeli, 7 yıl sözleşme | 380,000 €/yıl |

### 1.2 Kapsam ve Kullanım

Her vaka çalışması şu bölümleri içerir: tesis profili, başlangıç durumu, uygulama süreci, sonuçlar, exergy perspektifi ve çıkarılan dersler. Vakalar, ExergyLab kullanıcılarının kendi tesislerinde benzer uygulamalar planlarken referans olarak kullanılmak üzere tasarlanmıştır.

## 2. Vaka 1: Otomotiv Fabrikası — ISO 50001 Sertifikasyon Yolculuğu

### 2.1 Tesis Profili

| Parametre | Değer |
|-----------|-------|
| Konum | Bursa OSB |
| Sektör | Otomotiv (ana sanayi — gövde üretimi) |
| Çalışan sayısı | 1,200 |
| Yıllık enerji tüketimi | 15,000 TEP/yıl |
| Ana prosesler | Boya, kaynak, montaj, presleme |
| Enerji kaynakları | Doğalgaz (%62), elektrik (%35), motorin (%3) |
| Yıllık enerji maliyeti | ~3.8 milyon € |

### 2.2 Başlangıç Durumu

ISO 50001 gap analizi sonuçları:

| Madde | Uyumluluk | Açıklama |
|-------|-----------|----------|
| 4 — Bağlam | %20 | Paydaş analizi eksik |
| 5 — Liderlik | %50 | Politika taslak, roller belirsiz |
| 6 — Planlama | %30 | SEU belirlenmemiş, EnPI/EnB yok |
| 7 — Destek | %45 | Eğitim programı mevcut ama enerji odaklı değil |
| 8 — Operasyon | %35 | Prosedürler var ama enerji kontrolü zayıf |
| 9 — Değerlendirme | %25 | Enerji verisi toplanıyor ama analiz yok |
| 10 — İyileştirme | %15 | Sporadik projeler, sistematik değil |
| **Genel** | **%40** | — |

### 2.3 Uygulama — 14 Aylık Yol Haritası

```
Faz 1 — Temel Kurulum (Ay 1-4):
├── Enerji ekibi oluşturma (8 kişi, çapraz fonksiyonel)
├── Enerji politikası onayı (CEO imzalı)
├── Enerji inceleme (Energy Review) ve Pareto analizi
├── 8 SEU belirleme:
│   ├── SEU-1: Boya fırınları (3,200 TEP — %21)
│   ├── SEU-2: Boya kabin HVAC (1,800 TEP — %12)
│   ├── SEU-3: Kaynak robotları (1,500 TEP — %10)
│   ├── SEU-4: Basınçlı hava sistemi (1,350 TEP — %9)
│   ├── SEU-5: Buhar kazanları (1,200 TEP — %8)
│   ├── SEU-6: Soğutma sistemi (1,050 TEP — %7)
│   ├── SEU-7: Presleme (900 TEP — %6)
│   └── SEU-8: Aydınlatma (750 TEP — %5)
└── Alt sayaç kurulumu (12 sayaç)

Faz 2 — Sistem Kurulumu (Ay 5-9):
├── EnPI tanımlama (her SEU için en az 1)
├── EnB oluşturma (24 aylık baseline, regresyon modelleri)
├── Hedefler: Yıl 1 → %5, Yıl 2 → %8, Yıl 3 → %12 enerji azaltma
├── Operasyonel kontrol prosedürleri yazımı (8 SEU × SOP)
├── Eğitim programı: SEU operatörleri (120 kişi) + genel farkındalık (1,200 kişi)
├── Dokümantasyon sistemi (mevcut ISO 9001 altyapısına entegrasyon)
└── ECM önceliklendirme (15 ECM listelendi, 6 tanesi Yıl 1 hedefi)

Faz 3 — Uygulama ve Denetim (Ay 10-14):
├── 6 ECM projesinin uygulanması:
│   ├── Boya fırını yalıtım iyileştirme → 280 TEP/yıl
│   ├── Basınçlı hava kaçak onarımı → 120 TEP/yıl
│   ├── Soğutma kulesi optimizasyonu → 85 TEP/yıl
│   ├── LED dönüşüm (Faz 1) → 95 TEP/yıl
│   ├── Kazan O₂ trim kontrolü → 110 TEP/yıl
│   └── Kompresör VSD retrofit → 130 TEP/yıl
├── 1. İç denetim (2 Majör NC, 7 Minör NC → tamamı kapatıldı)
├── Yönetimin gözden geçirme toplantısı
├── Stage 1 denetim → geçildi (3 minör NC notu)
└── Stage 2 sertifikasyon denetimi → BAŞARILI
```

### 2.4 Sonuçlar

| Gösterge | Başlangıç | Yıl 1 Sonu | Yıl 2 Sonu | Değişim |
|----------|-----------|------------|------------|---------|
| Toplam tüketim (TEP/yıl) | 15,000 | 14,250 | 13,200 | -%12 |
| Fabrika SEC (kWh/araç) | 1,180 | 1,115 | 1,038 | -%12 |
| Enerji maliyeti (€/yıl) | 3,800,000 | 3,610,000 | 3,350,000 | -%11.8 |
| Yıllık tasarruf (€/yıl) | — | 190,000 | 450,000 | — |
| ISO 50001 sertifika | Yok | Alındı | Sürdürülüyor | — |

### 2.5 Exergy Perspektifi

ExergyLab ile yapılan analiz, boya fırınlarında (SEU-1) ciddi exergy yıkımı tespit etti:

```
Boya fırınları exergy analizi:
  Yakıt exergy girişi     : 3,800 kW
  Faydalı exergy çıkışı   : 760 kW (parça ısıtma)
  Exergy yıkımı (İ_D)     : 2,280 kW (%60)
  Exergy kaybı (İ_L)      : 760 kW (%20 — baca gazı + yüzey)
  Exergy verimi (η_ex)    : %20

Kök neden:
├── Yanma irreversibilitesi → kaçınılmaz ama optimize edilebilir
├── Yüksek baca gazı sıcaklığı (265°C) → ekonomizer fırsatı
├── Yüzey kayıpları (85°C yüzey) → yalıtım iyileştirme
└── Düşük yük çalışma → modülasyon kontrolü gerekli

Enerji denetimi bu ayrıntıyı vermedi (kazan verimi %88 olarak "iyi" raporlandı).
Exergy analizi, %60 yıkımı ortaya koyarak asıl iyileştirme potansiyelini gösterdi.
```

### 2.6 Çıkarılan Dersler

1. **Üst yönetim desteği kritik:** CEO'nun enerji politikasını bizzat duyurması katılımı artırdı
2. **Mevcut ISO 9001 altyapısı avantaj:** Dokümantasyon ve denetim kültürü zaten mevcuttu
3. **Alt sayaçlar vazgeçilmez:** SEU bazında ölçüm olmadan EnPI anlamını yitirir
4. **Exergy analizi derinlik katar:** Enerji denetimi "iyi" dediği kazanda exergy %60 yıkım bulundu
5. **14 ay yeterli ama sıkı:** Daha büyük tesislerde 18-24 ay planlanmalı

## 3. Vaka 2: Gıda Fabrikası — M&V ile Tasarruf Doğrulaması

### 3.1 Tesis Profili

| Parametre | Değer |
|-----------|-------|
| Konum | Bolu |
| Sektör | Gıda (süt işleme — UHT süt, yoğurt, peynir) |
| Çalışan sayısı | 320 |
| Yıllık enerji tüketimi | 4,500 TEP/yıl |
| Ana prosesler | Pastörizasyon, UHT, soğutma, paketleme |
| Soğutma sistemi | 3 × 90 kW vida kompresörlü chiller (R-134a) |
| Soğutma yükü | Sürekli, mevsimsel değişken (CDD bağımlı) |

### 3.2 Proje Tanımı

Soğutma sistemi VSD (Variable Speed Drive) retrofit projesi:

```
Mevcut durum:
├── 3 × 90 kW sabit hızlı vida kompresör
├── Kapasite kontrolü: Slide valve (%50-100)
├── Ortalama yük faktörü: %65
├── Yıllık soğutma elektrik tüketimi: 1,420 MWh
├── Mevcut enerji COP: 3.8
└── Mevcut exergy verimi: %18

Retrofit:
├── 3 kompresöre VSD eklenmesi
├── Kademeli çalışma optimizasyonu (1 VSD lead, 2 sabit lag)
├── Beklenen tasarruf: 200,000 kWh/yıl (%14)
├── Yatırım maliyeti: 145,000 €
└── Basit geri ödeme: 2.9 yıl (0.40 €/kWh)
```

### 3.3 M&V Yaklaşımı — IPMVP Opsiyon C

```
M&V Plan özeti:
═══════════════
Opsiyon          : IPMVP Opsiyon C (Whole-facility — soğutma tesis geneli)
Ölçüm sınırı     : Soğutma makine dairesi (3 chiller + yardımcı ekipman)
Baseline dönemi   : Temmuz 2023 — Haziran 2024 (12 ay)
Raporlama dönemi  : Temmuz 2024 — Haziran 2025 (12 ay)
Veri sıklığı      : Aylık (kWh + üretim ton + CDD)

Regresyon modeli:
  E [MWh/ay] = a + b × Üretim [ton/ay] + c × CDD [°C·gün/ay]

Baseline sonuçları:
  E = 42.5 + 0.018 × Üretim + 0.35 × CDD
  R² = 0.91 → ≥ 0.75 ✓
  CV-RMSE = %11.8 → ≤ %25 ✓
  NMBE = −%1.2 → ±%10 ✓

Değişkenler:
  a = 42.5 MWh/ay → Baseload (pompa, kontrol, aydınlatma)
  b = 0.018 MWh/ton → Üretim bağımlı soğutma
  c = 0.35 MWh/°C·gün → İklim bağımlı soğutma
```

### 3.4 Sonuçlar

| Ay | Üretim (ton) | CDD | E_baseline_ayar (MWh) | E_gerçek (MWh) | Tasarruf (MWh) |
|----|-------------|-----|----------------------|----------------|----------------|
| Tem 24 | 2,800 | 310 | 201 | 174 | 27 |
| Ağu 24 | 2,650 | 295 | 193 | 165 | 28 |
| Eyl 24 | 2,900 | 180 | 157 | 140 | 17 |
| Eki 24 | 3,100 | 65 | 121 | 110 | 11 |
| Kas 24 | 2,750 | 15 | 97 | 88 | 9 |
| Ara 24 | 2,400 | 5 | 87 | 80 | 7 |
| Oca 25 | 2,500 | 3 | 89 | 83 | 6 |
| Şub 25 | 2,600 | 8 | 92 | 85 | 7 |
| Mar 25 | 2,850 | 25 | 102 | 91 | 11 |
| Nis 25 | 2,700 | 85 | 121 | 106 | 15 |
| May 25 | 2,950 | 175 | 157 | 135 | 22 |
| Haz 25 | 3,000 | 250 | 184 | 159 | 25 |
| **Toplam** | — | — | **1,601** | **1,416** | **185** |

```
Doğrulanmış yıllık tasarruf: 185 MWh/yıl (%11.6)

CUSUM analizi:
├── Tüm aylar negatif kümülatif sapma → tutarlı tasarruf
├── Yaz aylarında (Tem-Ağu) en yüksek tasarruf → VSD yüksek yükte etkili
├── Kış aylarında düşük tasarruf → düşük yükte VSD etkisi sınırlı
└── Trend kararlı, anomali yok

Belirsizlik (%90 güven): ±%15 → 185 ± 28 MWh/yıl
Minimum doğrulanmış tasarruf: 157 MWh/yıl
```

### 3.5 Exergy Perspektifi

| Parametre | Retrofit Öncesi | Retrofit Sonrası | İyileşme |
|-----------|----------------|-----------------|----------|
| Enerji COP | 3.8 | 4.5 | +18% |
| Exergy verimi (η_ex) | %18 | %26 | +44% |
| Exergy yıkımı (İ_D) | 195 kW | 148 kW | −24% |
| Kompresör exergy kaybı | 85 kW | 52 kW | −39% |

Exergy analizi, enerji COP'undan çok daha derin bir iyileşme ortaya koydu: enerji bazında %18 iyileşme varken, exergy bazında %44 iyileşme tespit edildi. Bunun nedeni, VSD'nin kısmi yükte kompresör irreversibilitesini önemli ölçüde azaltmasıdır.

### 3.6 Çıkarılan Dersler

1. **Opsiyon C soğutma sistemleri için uygun:** İklim ve üretim etkisi regresyon ile iyi yakalanıyor
2. **Mevsimsel veri şart:** Yalnızca yaz verileri ile baseline kurmak yanıltıcı olur
3. **VSD tasarrufu yüke bağlı:** Tam yükte %15-20, kısmi yükte %5-10 tasarruf
4. **Exergy COP'dan daha bilgilendirici:** %18 vs %44 iyileşme farkı stratejik karar etkiler

## 4. Vaka 3: Tekstil Fabrikası — VAP Başvurusu ve Uygulama

### 4.1 Tesis Profili

| Parametre | Değer |
|-----------|-------|
| Konum | Denizli OSB |
| Sektör | Tekstil (iplik + dokuma + boya-terbiye) |
| Çalışan sayısı | 580 |
| Yıllık enerji tüketimi | 8,200 TEP/yıl |
| Ana prosesler | İplik eğirme, dokuma, boyama, terbiye, kurutma |
| Buhar sistemi | 2 × 10 ton/h doğalgaz kazanı, 8 bar doymuş buhar |
| Buhar tüketimi | ~12 ton/h (ortalama) |

### 4.2 Proje — Buhar Sistemi Optimizasyonu

```
Proje kapsamı (3 ECM paketi):
══════════════════════════════
ECM-1: Kondensat geri kazanımı iyileştirme
├── Mevcut: %45 kondensat geri dönüşü (kayıp + açık deşarj)
├── Hedef: %85 kondensat geri dönüşü
├── Yatırım: Kondensat pompası, boru hattı, filtre → 85,000 €
└── Beklenen tasarruf: 280,000 kWh_th/yıl

ECM-2: Boru ve vana yalıtımı
├── Mevcut: 45 noktada eksik/hasarlı yalıtım tespit edildi
├── Yalıtım kaybı: ~120 kW termal (infrared kamera ile tespit)
├── Yatırım: Yalıtım malzeme + işçilik → 32,000 €
└── Beklenen tasarruf: 180,000 kWh_th/yıl

ECM-3: Buhar kapanı bakım ve değişim
├── Mevcut: 85 kapandan 22'si arızalı (ultrasonik test)
│   ├── 12 adet: Açık pozisyonda kalmış (canlı buhar kaçağı)
│   ├── 7 adet: Kapalı pozisyonda kalmış (kondensat birikmesi)
│   └── 3 adet: Sürekli buhar geçirme
├── Yatırım: Kapan değişimi + test → 18,000 €
└── Beklenen tasarruf: 160,000 kWh_th/yıl

Toplam yatırım: 135,000 €
Toplam beklenen tasarruf: 620,000 kWh_th/yıl
```

### 4.3 VAP Başvuru Süreci

```
VAP (Verimlilik Artırıcı Proje) süreci:
═══════════════════════════════════════
1. Enerji denetim raporu hazırlama (yetkili şirket)        → 2 ay
2. Fizibilite raporu (mühendislik detayı, ROI hesaplama)    → 1 ay
3. YEGM/ENVER portal üzerinden başvuru                      → 1 hafta
4. YEGM teknik değerlendirme                                → 2-4 ay
5. Onay ve hibe sözleşmesi                                  → 1 ay
6. Uygulama (12 ay içinde tamamlanmalı)                     → 8 ay
7. Tamamlanma raporu ve yerinde doğrulama                    → 1 ay
8. Hibe ödemesi                                             → 2 ay

Hibe detayları:
├── Oran: Yatırımın %25'i (VAP-2024 dönemi)
├── Başvuru tutarı: 135,000 × %25 = 33,750 €
├── Onaylanan tutar: 33,750 € (tam onay)
└── Net yatırım: 135,000 − 33,750 = 101,250 €
```

### 4.4 Sonuçlar

| Gösterge | Değer |
|----------|-------|
| Gerçekleşen tasarruf (doğrulanmış) | 620,000 kWh_th/yıl (53 TEP) |
| Doğalgaz tasarrufu | ~62,000 Sm³/yıl |
| Maliyet tasarrufu | 74,000 €/yıl (doğalgaz + su + kimyasal) |
| Net yatırım (hibe sonrası) | 101,250 € |
| Basit geri ödeme | 1.4 yıl (hibe ile) / 1.8 yıl (hibesiz) |
| CO₂ azaltma | ~125 ton CO₂/yıl |

### 4.5 Çıkarılan Dersler

1. **Buhar sistemi düşük maliyetli/yüksek getirili:** Kondensat, yalıtım, kapan projeleri kısa ROI sağlar
2. **VAP %25 hibe önemli:** Net yatırımı düşürüp geri ödeme süresini kısaltır
3. **Ultrasonik kapan testi zorunlu:** %26 arızalı kapan oranı sektör ortalamasına uygun (tipik %15-30)
4. **Kondensat geri kazanımı çok boyutlu:** Enerji + su + kimyasal tasarruf sağlar

## 5. Vaka 4: Çimento Fabrikası — EnPI ve Sürekli İyileştirme

### 5.1 Tesis Profili

| Parametre | Değer |
|-----------|-------|
| Konum | Kayseri |
| Sektör | Çimento (entegre — ham madde + klinker + öğütme) |
| Kapasite | 1.2 milyon ton klinker/yıl |
| Yıllık enerji tüketimi | 120,000 TEP/yıl |
| Ana prosesler | Ham madde hazırlama, fırın (klinker), çimento öğütme |
| Enerji kaynakları | Petcoke (%55), kömür (%25), elektrik (%18), alternatif yakıt (%2) |
| Yıllık enerji maliyeti | ~15 milyon €/yıl |

### 5.2 EnPI Tanımları

| EnPI | Tanım | Birim | Başlangıç Değeri | Hedef |
|------|-------|-------|-------------------|-------|
| SEC_termal | Termal enerji / klinker üretimi | kcal/kg klinker | 842 | <800 |
| SEC_elektrik | Elektrik / çimento üretimi | kWh/ton çimento | 105 | <98 |
| Exergy verimi (fırın) | Klinker exergy / toplam yakıt exergy | % | 34.2 | >37 |
| Alternatif yakıt oranı | Alternatif yakıt / toplam termal | % | 2 | >10 |

### 5.3 Regresyon Modeli — Fırın SEC

```
Fırın termal SEC regresyon modeli:
══════════════════════════════════
SEC_termal [kcal/kg] = β₀ + β₁ × (1/Üretim_oranı) + β₂ × Nem + β₃ × LSF

Değişkenler:
├── Üretim_oranı: Anlık üretim / nominal kapasite [%]
├── Nem: Ham madde nem oranı [%]
└── LSF: Lime Saturation Factor [—]

Baseline modeli (2022):
  SEC = 680 + 12,500/Üretim_oranı + 8.5 × Nem + 1.2 × LSF
  R² = 0.87, CV-RMSE = %8.4, NMBE = +%0.6

Yorum:
├── β₀ = 680 kcal/kg → Optimum koşullarda minimum SEC
├── 12,500/Üretim_oranı → Düşük yükte SEC artar (sabit kayıplar)
├── 8.5 × Nem → Her %1 nem artışı → +8.5 kcal/kg (buharlaştırma)
└── 1.2 × LSF → Klinker kimyası etkisi
```

### 5.4 Sürekli İyileştirme — 3 Yıllık CUSUM

```
3 yıllık sürekli iyileştirme programı:
═════════════════════════════════════
Yıl 1 (2022): Baseline oluşturma + ilk ECM'ler
├── Klinker soğutucu fan optimizasyonu → SEC −8 kcal/kg
├── Fırın sızdırmazlık (false air) azaltma → SEC −5 kcal/kg
├── Ham değirmen ayar optimizasyonu → −2 kWh/ton
└── Yıllık iyileşme: SEC_termal −1.5%, SEC_elektrik −1.9%

Yıl 2 (2023): Orta ölçekli projeler
├── Çimento değirmeni seperatör değişimi → −3.5 kWh/ton
├── Alternatif yakıt oranı artışı (%2 → %5) → maliyet azalma
├── Fırın bypass optimizasyonu → SEC −6 kcal/kg
├── VSD uygulamaları (ID fan, raw mill fan) → −1.8 kWh/ton
└── Yıllık iyileşme: SEC_termal −2.4%, SEC_elektrik −2.8%

Yıl 3 (2024): İleri projeler
├── Atık ısı geri kazanımı (WHR) fizibilite çalışması
├── Alternatif yakıt oranı artışı (%5 → %10)
├── Prediktif bakım ile fırın refrakter optimizasyonu
├── ExergyLab entegrasyonu → exergy bazlı izleme başladı
└── Yıllık iyileşme: SEC_termal −2.1%, SEC_elektrik −2.5%

CUSUM (kümülatif tasarruf — 36 ay):
  Termal: −48 kcal/kg klinker → toplam −57,600 TEP (3 yılda)
  Elektrik: −8.2 kWh/ton çimento → toplam −12,300 MWh (3 yılda)
```

### 5.5 Sonuçlar

| Gösterge | 2022 (Başlangıç) | 2024 (Yıl 3 Sonu) | Değişim |
|----------|-------------------|-------------------|---------|
| SEC_termal (kcal/kg klinker) | 842 | 775 | −%8.0 |
| SEC_elektrik (kWh/ton çimento) | 105 | 96.8 | −%7.8 |
| Exergy verimi (fırın) | %34.2 | %37.8 | +3.6 pp |
| Alternatif yakıt oranı | %2 | %10 | +8 pp |
| Yıllık maliyet tasarrufu | — | 1,200,000 € | — |
| CO₂ azaltma (3 yılda) | — | 42,000 ton CO₂ | — |

### 5.6 Çıkarılan Dersler

1. **Yıllık %2-3 iyileşme sürdürülebilir:** Çimento sektöründe bu oran gerçekçi ve kanıtlanmış
2. **CUSUM kilit araç:** Aylık dalgalanmalar yanıltıcı, CUSUM gerçek trendi gösterir
3. **Alternatif yakıt çifte fayda:** Hem maliyet hem CO₂ azaltma (karbon piyasası geliri potansiyeli)
4. **Exergy analizi fırın optimizasyonunu derinleştirir:** Enerji %8 iyileşirken exergy +3.6 puan iyileşti

## 6. Vaka 5: Kimya Fabrikası — EPC/ESCO Uygulaması

### 6.1 Tesis Profili

| Parametre | Değer |
|-----------|-------|
| Konum | Kocaeli (Dilovası OSB) |
| Sektör | Kimya (petrokimya yan sanayi — plastik katkı) |
| Çalışan sayısı | 280 |
| Yıllık enerji tüketimi | 6,800 TEP/yıl |
| Ana prosesler | Reaktörler, distilasyon, kurutma, paketleme |
| Enerji kaynakları | Doğalgaz (%58), elektrik (%40), LPG (%2) |
| Yıllık enerji maliyeti | ~2.2 milyon € |

### 6.2 EPC Sözleşme Yapısı

```
EPC modeli: Garantili Tasarruf (Guaranteed Savings)
═══════════════════════════════════════════════════
Sözleşme süresi   : 7 yıl
Toplam yatırım     : 1,100,000 €
Finans             : Müşteri kendi finansmanı (banka kredisi)
Garanti            : ESCO minimum 380,000 €/yıl tasarruf garanti eder
Risk dağılımı      : Performans riski → ESCO; Finans riski → Müşteri
M&V                : Bağımsız M&V danışmanı (yıllık doğrulama)
Garanti altı ödeme : Gerçekleşen tasarruf < garanti ise ESCO farkı öder
Garanti üstü       : Gerçekleşen > garanti ise fazla %50-%50 paylaşılır
```

### 6.3 ECM Kapsamı ve M&V Opsiyonları

| ECM No | Tanım | Yatırım (€) | Beklenen Tasarruf (€/yıl) | IPMVP Opsiyon |
|--------|-------|-------------|---------------------------|---------------|
| ECM-1 | Buhar sistemi optimizasyonu (ekonomizer + kondensat + yalıtım) | 280,000 | 125,000 | B |
| ECM-2 | Basınçlı hava sistemi (VSD + kaçak onarımı + kontrol) | 195,000 | 85,000 | B |
| ECM-3 | Aydınlatma LED dönüşüm (fabrika geneli) | 120,000 | 48,000 | A |
| ECM-4 | HVAC optimizasyonu (VSD + serbest soğutma + otomasyon) | 310,000 | 95,000 | B |
| ECM-5 | Proses ısı geri kazanımı (reaktör → ön ısıtma) | 195,000 | 52,000 | B |
| **Toplam** | — | **1,100,000** | **405,000** | — |

### 6.4 M&V Detayları

```
Her ECM için ayrı M&V planı:
════════════════════════════
ECM-1 (Buhar — Opsiyon B):
├── Sürekli ölçüm: Buhar debimetre + baca gazı analizörü
├── EnPI: Kazan yakma verimi [%], buhar SEC [kg/ton ürün]
├── Baseline: 12 aylık sürekli veri
└── Raporlama: Aylık + yıllık doğrulama

ECM-2 (Basınçlı hava — Opsiyon B):
├── Sürekli ölçüm: kW metre + debi ölçüm
├── EnPI: SPC [kW/(m³/min)], kaçak oranı [%]
├── Baseline: 12 aylık sürekli veri
└── Raporlama: Aylık + yıllık doğrulama

ECM-3 (Aydınlatma — Opsiyon A):
├── Bir kerelik ölçüm: Güç ölçümü (anahtar parametre)
├── Stipulated: Çalışma saatleri (vardiya programından)
├── Hesaplama: ΔP × saat = tasarruf
└── Raporlama: Yıllık

ECM-4 (HVAC — Opsiyon B):
├── Sürekli ölçüm: kW metre + sıcaklık/nem sensörleri
├── EnPI: kW/m² soğutma/ısıtma, COP
├── Baseline: CDD/HDD regresyon modeli
└── Raporlama: Aylık + yıllık doğrulama

ECM-5 (Isı geri kazanımı — Opsiyon B):
├── Sürekli ölçüm: Termal enerji sayacı (ΔT × debi)
├── EnPI: Geri kazanılan enerji [kWh_th/ay]
├── Baseline: Proje öncesi sıfır (yeni sistem)
└── Raporlama: Aylık + yıllık doğrulama

Toplam M&V maliyeti: 45,000 €/yıl (danışman + platform + kalibrasyon)
M&V maliyet oranı: 45,000 / 405,000 = %11 → kabul edilebilir (7 yıllık sözleşmede)
```

### 6.5 Sonuçlar (Yıl 1)

| ECM | Garanti (€/yıl) | Gerçekleşen (€/yıl) | Durum |
|-----|-----------------|---------------------|-------|
| ECM-1 — Buhar | 110,000 | 128,000 | Garanti üstü |
| ECM-2 — Basınçlı hava | 75,000 | 82,000 | Garanti üstü |
| ECM-3 — Aydınlatma | 45,000 | 47,500 | Garanti üstü |
| ECM-4 — HVAC | 85,000 | 78,000 | Garanti altı (ESCO ödeme: 7,000 €) |
| ECM-5 — Isı geri kazanımı | 65,000 | 55,000 | Garanti altı (ESCO ödeme: 10,000 €) |
| **Toplam** | **380,000** | **390,500** | **Garanti üstü (+%2.8)** |

```
Yıl 1 değerlendirme:
├── Toplam doğrulanmış tasarruf: 390,500 €/yıl
├── Garanti: 380,000 €/yıl → Karşılandı ✓
├── Garanti altı ECM'ler için ESCO ödemesi: 17,000 €
├── Garanti üstü fazla: 10,500 € → %50 müşteri = 5,250 €
├── Müşteri net kazanç: 390,500 + 17,000 − 5,250 = 402,250 €/yıl
└── Basit geri ödeme: 1,100,000 / 402,250 = 2.7 yıl
```

### 6.6 Çıkarılan Dersler

1. **Garantili tasarruf modeli güven verir:** Müşteri yatırımı banka kredisi ile yapabildi (garanti = bankabilite)
2. **Her ECM ayrı M&V şart:** Toplam garanti yetiyor ama hangi ECM'nin altında kaldığı bilinmeli
3. **HVAC mevsimsel risk taşır:** Yıl 1'de beklenenden ılıman kış → ısıtma tasarrufu düşük
4. **Isı geri kazanımı devreye alma süresi:** Proses entegrasyonu 3 ay gecikti → yıllık toplam etkilendi
5. **M&V maliyeti planlanmalı:** %11 oranı 7 yıllık sözleşmede kabul edilebilir, kısa sözleşmede pahalı

## 7. Karşılaştırma Tablosu (Comparison Table)

| Parametre | Vaka 1 — Otomotiv | Vaka 2 — Gıda | Vaka 3 — Tekstil | Vaka 4 — Çimento | Vaka 5 — Kimya |
|-----------|-------------------|---------------|------------------|------------------|----------------|
| **Konum** | Bursa | Bolu | Denizli | Kayseri | Kocaeli |
| **Tüketim (TEP/yıl)** | 15,000 | 4,500 | 8,200 | 120,000 | 6,800 |
| **Yaklaşım** | ISO 50001 | M&V (IPMVP) | VAP | EnPI + Sürekli İyileştirme | EPC/ESCO |
| **Kapsam** | Tesis geneli EnMS | Soğutma VSD | Buhar sistemi | Fırın + öğütme | 5 ECM paketi |
| **Yatırım** | ~500,000 € | 145,000 € | 135,000 € (101,250 € net) | ~2,500,000 € | 1,100,000 € |
| **Yıllık tasarruf** | 450,000 €/yıl | 74,000 €/yıl | 74,000 €/yıl | 1,200,000 €/yıl | 390,500 €/yıl |
| **ROI (basit geri ödeme)** | 1.1 yıl | 2.0 yıl | 1.4 yıl (hibe ile) | 2.1 yıl | 2.7 yıl |
| **Enerji azaltma** | %12 | %11.6 (soğutma) | ~%7.5 (buhar) | %8 (3 yılda) | %17 (toplam) |
| **Exergy bulgusu** | Boya fırını η_ex=%20 | Chiller η_ex %18→%26 | — | Fırın η_ex +3.6 pp | — |
| **Anahtar ders** | Üst yönetim desteği | Mevsimsel M&V | VAP hibe avantajı | CUSUM ile trend | EPC bankabilite |

## 8. İlgili Dosyalar

- [Enerji Yönetimi Bilgi Tabanı İndeks](INDEX.md) — Energy management navigasyon haritası
- [ISO 50001 Uygulama Rehberi](iso_50001_implementation.md) — Gap analizi, sertifikasyon yol haritası (Vaka 1 referans)
- [IPMVP M&V Çerçevesi](mv_ipmvp.md) — Opsiyon seçimi ve EPC bağlamı (Vaka 2, 5 referans)
- [Türkiye Teşvikleri](turkey_incentives.md) — VAP başvuru detayları (Vaka 3 referans)
- [EnPI Rehberi](enpi_guide.md) — Sektörel EnPI tanımlama (Vaka 4 referans)
- [Vaka Çalışmaları (genel)](../case_studies.md) — Genel vaka çalışmaları çerçevesi

## 9. Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- EVO, "IPMVP Core Concepts 2022" — M&V protokolü (Vaka 2, 5)
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Verimlilik Artırıcı Proje (VAP) Yönetmeliği" — VAP başvuru kriterleri (Vaka 3)
- WBCSD/CSI, "Getting the Numbers Right (GNR) Database" — Çimento sektörel benchmark (Vaka 4)
- IEA, "Technology Roadmap: Low-Carbon Transition in the Cement Industry" — Çimento enerji verimliliği
- UNIDO, "Textile Industry Energy Efficiency" — Tekstil sektörel kılavuz (Vaka 3)
- European Commission, "Reference Document on Best Available Techniques (BREF)" — Sektörel en iyi teknikler
- Bejan, A. (2006), "Advanced Engineering Thermodynamics" — Exergy analizi temel referans
- Tsatsaronis, G. (2007), "Definitions and nomenclature in exergy analysis and exergoeconomics" — Exergy verimlilik tanımları
- T.C. Resmi Gazete, 5627 sayılı Enerji Verimliliği Kanunu — Yasal çerçeve
