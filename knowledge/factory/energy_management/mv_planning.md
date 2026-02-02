---
title: "M&V Plan Hazırlama Rehberi (M&V Plan Development Guide)"
category: factory
equipment_type: factory
keywords: [M&V planı, ölçüm planı, doğrulama planı, tasarruf hesaplama, ölçüm sınırı, bağımsız değişken, etkileşim, rapor dönemleri]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/mv_ipmvp.md, factory/energy_management/mv_statistics.md, factory/measurement_verification.md, factory/data_collection.md]
use_when: ["M&V planı hazırlanacağında", "Ölçüm sınırı belirlenecekken", "Tasarruf hesaplama metodolojisi tanımlanacağında"]
priority: medium
last_updated: 2026-02-01
---

# M&V Plan Hazırlama Rehberi (M&V Plan Development Guide)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

M&V planı (M&V Plan), bir enerji verimliliği projesinde (ECM — Energy Conservation Measure) elde edilen tasarrufların nasıl hesaplanacağını, ölçüleceğini ve raporlanacağını tanımlayan teknik belgedir. IPMVP Core Concepts 2022'ye göre her M&V uygulaması bir M&V planı ile başlamalıdır.

### 1.1 M&V Planının Amacı

- ECM öncesi ve sonrası karşılaştırma metodolojisini tanımlamak
- Ölçüm noktalarını, cihazları ve veri toplama sıklığını belirlemek
- Bağımsız değişkenleri ve regresyon modelini dokümante etmek
- Tarafların (müşteri, ESCO, bağımsız denetçi) sorumluluklarını belirlemek
- İhtilaf durumunda referans belge olarak kullanılmak

### 1.2 IPMVP'nin Plan Gereksinimleri

IPMVP, her M&V planının asgari 12 bileşen içermesini gerektirir. Bu bileşenler Bölüm 2'de detaylı olarak açıklanmaktadır.

### 1.3 Planın Yasal Bağlayıcılığı

ESCO/EPC sözleşmelerinde M&V planı, sözleşmenin eki olarak yasal bağlayıcılık taşır. Türkiye'de VAP (Verimlilik Artırıcı Proje) başvurularında da M&V planı zorunlu belgeler arasındadır. Planın imza aşamasından önce tüm taraflarca onaylanması kritik öneme sahiptir.

## 2. M&V Planı Bileşenleri (M&V Plan Components)

IPMVP'ye göre 12 zorunlu bileşen aşağıda detaylı olarak açıklanmıştır:

### Bileşen 1: ECM Tanımı (ECM Description)

ECM'nin teknik tanımı, kapsamı, etkilenen ekipman listesi ve beklenen tasarruf mekanizması.

> **Örnek:** "Soğutma suyu pompalarına (P-101, P-102, P-103) değişken hız sürücüsü (VSD) eklenerek, sabit debili çalışma yerine talebe göre debi ayarlaması yapılacaktır."

### Bileşen 2: Ölçüm Sınırı (Measurement Boundary)

ECM'nin etkisinin ölçüleceği fiziksel sınır. Opsiyon A/B'de ekipman bazlı, Opsiyon C'de tesis geneli.

> **Örnek:** "Ölçüm sınırı: soğutma suyu pompaları (P-101, P-102, P-103) elektrik besleme panosu. Sınır içi: pompa motorları, VSD üniteleri. Sınır dışı: soğutma kulesi fanları, chiller."

### Bileşen 3: Temel Dönem (Baseline Period)

ECM uygulaması öncesi referans veri toplama süresi. Minimum 12 ay önerilir (mevsimselliği kapsamak için).

> **Örnek:** "Temel dönem: 01.01.2025 — 31.12.2025 (12 ay). Veri kaynağı: BMS sistemi, 15-dakikalık aralıklarla güç ölçümü."

### Bileşen 4: Seçilen IPMVP Opsiyonu (Selected IPMVP Option)

Seçilen opsiyon ve gerekçesi. Opsiyon seçim kriterleri için `mv_ipmvp.md` dosyasına bakınız.

> **Örnek:** "Opsiyon B seçilmiştir. Gerekçe: performans garantisi gerekli, ekipman izolasyonu mümkün, sürekli ölçüm bütçesi mevcut."

### Bileşen 5: Ölçüm Noktaları ve Cihazları (Measurement Points and Instruments)

Her ölçüm noktası için: konum, parametre, cihaz tipi, doğruluk sınıfı, kalibrasyon takvimi.

| Nokta | Parametre | Cihaz | Doğruluk | Kalibrasyon |
|---|---|---|---|---|
| MP-01 | Elektrik güç (kW) | Güç analizörü, Sınıf 0.5 | ±0.5% | Yıllık |
| MP-02 | Debi (m³/h) | Ultrasonik debimetre | ±1.5% | 2 yılda bir |
| MP-03 | Basınç (bar) | Piezoelektrik transmitter | ±0.25% | Yıllık |
| MP-04 | Sıcaklık (°C) | PT100, 4-telli | ±0.15°C | Yıllık |

### Bileşen 6: Veri Toplama Sıklığı (Data Collection Frequency)

Ölçüm aralığı, kayıt yöntemi ve veri depolama.

| Parametre | Sıklık | Kayıt | Depolama |
|---|---|---|---|
| Elektrik güç | 15 dakika | Otomatik (BMS) | SQL veritabanı |
| Debi | 15 dakika | Otomatik (BMS) | SQL veritabanı |
| Üretim hacmi | Günlük | Manuel giriş | ERP sistemi |
| Hava sıcaklığı | Saatlik | Meteoroloji API | Bulut |

### Bileşen 7: Bağımsız Değişkenler (Independent Variables)

Enerji tüketimini etkileyen ve rutin düzeltme için kullanılacak değişkenler.

> **Örnek:** "Bağımsız değişken: soğutma yükü (kW_th), dış ortam sıcaklığı (°C), üretim hattı çalışma saati (h/gün)."

### Bileşen 8: Regresyon Modeli (Regression Model)

Baseline enerji tüketimi ile bağımsız değişkenler arasındaki matematiksel ilişki.

```
Baseline Regresyon Modeli:
─────────────────────────────────────────────
E_pompa = a + b₁ × Q_soğutma + b₂ × T_dış

Burada:
  E_pompa    : Pompa elektrik tüketimi [kWh/gün]
  Q_soğutma  : Soğutma yükü [kWh_th/gün]
  T_dış      : Günlük ortalama dış sıcaklık [°C]
  a, b₁, b₂  : Regresyon katsayıları

Model Doğrulama Kriterleri (ASHRAE Guideline 14):
  R²       ≥ 0.75
  CV(RMSE) ≤ 25% (aylık) veya ≤ 30% (günlük)
  NMBE     ≤ ±0.5% (aylık) veya ≤ ±10% (günlük)
─────────────────────────────────────────────
```

### Bileşen 9: Etkileşim Yönetimi (Interactive Effects Management)

Diğer ECM'ler veya operasyonel değişikliklerle olası etkileşimlerin tanımlanması ve yönetimi.

> **Örnek:** "VSD retrofit ile eşzamanlı yapılacak chiller optimizasyonu etkileşim yaratabilir. Etkileşim, ayrı alt sayaç ile izlenecektir."

### Bileşen 10: Raporlama Sıklığı (Reporting Frequency)

Tasarruf raporlarının üretim ve sunum takvimi.

| Rapor Tipi | Sıklık | İçerik | Alıcı |
|---|---|---|---|
| Operasyonel | Haftalık | Anlık performans özeti | Tesis yöneticisi |
| M&V raporu | Aylık | Tasarruf hesaplama + doğrulama | ESCO + Müşteri |
| Yıllık rapor | Yıllık | Kümülatif tasarruf + trend | Üst yönetim |
| Bağımsız denetim | Yıllık | Tüm hesaplamaların doğrulanması | Tüm taraflar |

### Bileşen 11: Kalite Güvence (Quality Assurance)

Veri kalitesi, cihaz kalibrasyonu ve kontrol prosedürleri.

> **Örnek:** "Eksik veri oranı %5'i aşamaz. %5-10 arasında enterpolasyon uygulanır. %10 üzerinde dönem geçersiz sayılır."

### Bileşen 12: Sorumluluklar (Responsibilities)

Her tarafın görev ve sorumlulukları.

| Görev | Sorumlu | Süre |
|---|---|---|
| Veri toplama | Tesis operatör | Sürekli |
| Cihaz bakımı | ESCO | Sözleşme süresi |
| Aylık rapor hazırlama | ESCO M&V mühendisi | Aylık |
| Rapor onaylama | Müşteri enerji yöneticisi | Aylık |
| Bağımsız denetim | 3. taraf denetçi | Yıllık |

## 3. M&V Plan Şablonu (M&V Plan Template)

Aşağıdaki şablon, herhangi bir ECM projesi için doldurulabilir:

```
╔══════════════════════════════════════════════════════════════════╗
║                    M&V PLAN ŞABLONU v2.0                       ║
║                    (IPMVP Uyumlu)                               ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Proje Adı       : ________________________________________    ║
║  Tesis            : ________________________________________    ║
║  Tarih            : ________________________________________    ║
║  Hazırlayan       : ________________________________________    ║
║  Onaylayan        : ________________________________________    ║
║  Revizyon No      : ________________________________________    ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  1. ECM Tanımı           : [Teknik açıklama]                   ║
║  2. Ölçüm Sınırı         : [Sınır tanımı + şema referansı]    ║
║  3. Temel Dönem           : [Başlangıç — Bitiş tarihi]        ║
║  4. IPMVP Opsiyonu        : [A / B / C / D + gerekçe]         ║
║  5. Ölçüm Noktaları       : [Tablo — nokta, parametre, cihaz] ║
║  6. Veri Toplama Sıklığı  : [Parametre × sıklık × yöntem]     ║
║  7. Bağımsız Değişkenler   : [Liste + veri kaynağı]            ║
║  8. Regresyon Modeli       : [Formül + doğrulama kriterleri]   ║
║  9. Etkileşim Yönetimi    : [Tanımlanan etkileşimler + strateji]║
║  10. Raporlama Sıklığı    : [Rapor tipi × sıklık × alıcı]    ║
║  11. Kalite Güvence        : [KG prosedürleri]                 ║
║  12. Sorumluluklar         : [RACI matrisi]                    ║
║                                                                  ║
║  Ekler:                                                         ║
║    Ek-A: Ölçüm sınırı şeması                                  ║
║    Ek-B: Baseline verileri (ham)                                ║
║    Ek-C: Regresyon analizi çıktıları                           ║
║    Ek-D: Cihaz kalibrasyon sertifikaları                       ║
║    Ek-E: İhtilaf çözüm prosedürü                               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

## 4. Tam Çalışılmış Örnek — VSD Retrofit Projesi (Worked Example — VSD Retrofit)

### 4.1 Proje Tanımı

**Tesis:** Bir kimya fabrikasında soğutma suyu sistemi
**ECM:** 3 adet 55 kW soğutma suyu pompasına (P-101, P-102, P-103) VSD uygulaması
**Beklenen Tasarruf:** ~185.000 kWh/yıl (%35 enerji tasarrufu)
**Yatırım:** 450.000 TL (VSD üniteleri + montaj)
**Sözleşme:** 5 yıllık garantili tasarruf EPC

### 4.2 M&V Planı — 12 Bileşen Doldurulmuş

**1. ECM Tanımı:**
Üç adet sabit hızlı santrifüj soğutma suyu pompasına (her biri 55 kW, toplam 165 kW kurulu güç) VSD (Variable Speed Drive) retrofiti uygulanarak, soğutma yükü değişimine göre otomatik debi kontrolü sağlanacaktır. Mevcut sistemde pompa debisi bypass vanası ile kontrol edilmektedir.

**2. Ölçüm Sınırı:**
```
Ölçüm Sınırı Şeması:
═══════════════════════════════════════════
                 ÖLÇÜM SINIRI
    ┌─────────────────────────────────────┐
    │                                     │
    │  [Pano] ──→ [VSD] ──→ [Motor/Pompa]│
    │    │                        │       │
    │   MP-01                   MP-02     │
    │  (kW)                    (m³/h)     │
    │                             │       │
    │                           MP-03     │
    │                          (bar)      │
    │                             │       │
    └─────────────────────────────────────┘
                     │
              Soğutma suyu hattı
                     ↓
           [Proses heat exchangers]
═══════════════════════════════════════════
```

**3. Temel Dönem:** 01.01.2025 — 31.12.2025 (12 ay, tüm mevsimler dahil)

**4. IPMVP Opsiyonu:** Opsiyon B — Retrofit Isolation, All Parameters
- Gerekçe: EPC sözleşmesinde performans garantisi mevcut, sürekli ölçüm bütçesi ayrılmış, ekipman izolasyonu teknik olarak mümkün.

**5. Ölçüm Noktaları:**

| Nokta | Konum | Parametre | Cihaz | Doğruluk | Kaynak |
|---|---|---|---|---|---|
| MP-01 | Pompa pano çıkışı | Toplam güç (kW) | Schneider PM5350 | ±0.5% | BMS |
| MP-02 | Pompa çıkış kolektörü | Toplam debi (m³/h) | Endress+Hauser Prosonic | ±1.5% | BMS |
| MP-03 | Pompa çıkış hattı | Basınç (bar) | Siemens SITRANS P | ±0.25% | BMS |
| MP-04 | Gidiş/dönüş hattı | Sıcaklık (°C) | PT100, Sınıf A | ±0.15°C | BMS |
| MP-05 | Dış ortam | Sıcaklık (°C) | Meteoroloji istasyonu | ±0.5°C | API |

**6. Veri Toplama Sıklığı:** Tüm BMS noktaları: 15 dakika aralıklı. Üretim verisi: günlük (ERP). Meteoroloji: saatlik (API).

**7. Bağımsız Değişkenler:**
- Q_soğutma: Soğutma yükü [kWh_th/gün] — hesaplama: debi × ΔT × cp
- T_dış: Günlük ortalama dış ortam sıcaklığı [°C]
- H_üretim: Günlük üretim hattı çalışma süresi [h/gün]

**8. Regresyon Modeli:**

```
Baseline Model:
  E_pompa = 12.4 + 0.082 × Q_soğutma + 1.15 × T_dış

Model İstatistikleri:
  R²       = 0.89 (> 0.75 ✓)
  CV(RMSE) = 14.2% (< 25% aylık ✓)
  NMBE     = −0.3% (< ±0.5% ✓)
  n        = 365 gün
  p-value  = < 0.001

Tasarruf Hesaplama:
  Tasarruf_ay = Σ(E_baseline,ayarlanmış − E_ölçülen) [kWh/ay]
  E_baseline,ayarlanmış = 12.4 + 0.082 × Q_soğutma,gerçek + 1.15 × T_dış,gerçek
```

**9. Etkileşim Yönetimi:** Chiller optimizasyonu aynı dönemde planlanmamıştır. Soğutma kulesi fan kontrolü mevcut otomasyon ile sabit kalacaktır. Etkileşim riski: düşük.

**10. Raporlama:** Aylık M&V raporu (ESCO → Müşteri), yıllık bağımsız denetim raporu.

**11. Kalite Güvence:** Eksik veri < %5 kabul, %5-10 lineer enterpolasyon, > %10 dönem iptal. Cihaz kalibrasyonu yıllık. BMS veri yedekleme günlük.

**12. Sorumluluklar:**

| Görev | ESCO | Müşteri | Bağımsız Denetçi |
|---|:---:|:---:|:---:|
| Veri toplama | — | S | — |
| Cihaz bakım/kalibrasyon | S | Y | — |
| Aylık tasarruf hesaplama | S | O | — |
| Yıllık doğrulama | — | — | S |
| Rapor onay | H | O | D |

> S: Sorumlu, O: Onaylayan, H: Haberdar, Y: Yardımcı, D: Danışılan

### 4.3 Beklenen Tasarruf Hesabı

```
Yıllık Beklenen Tasarruf:
═══════════════════════════════════════════════
Baseline yıllık tüketim  : 528.000 kWh/yıl
Beklenen raporlama tüketim: 343.000 kWh/yıl
Beklenen enerji tasarrufu  : 185.000 kWh/yıl (%35)

Elektrik birim fiyat       : 3.20 TL/kWh
Yıllık parasal tasarruf    : 592.000 TL/yıl
Basit geri ödeme süresi    : 450.000 / 592.000 = 0.76 yıl

M&V maliyeti (yıllık)      : 35.000 TL (%5.9 — kabul edilebilir)
═══════════════════════════════════════════════
```

## 5. Etkileşim (Interactive Effects) Yönetimi

### 5.1 Etkileşim Türleri

| Tür | Tanım | Örnek | Etki |
|---|---|---|---|
| Pozitif Etkileşim | Bir ECM diğerinin tasarrufunu artırır | VSD pompa + VSD fan → toplam tasarruf > bireysel toplamı | Toplam tasarruf artışı |
| Negatif Etkileşim | Bir ECM diğerinin tasarrufunu azaltır | LED aydınlatma → azalan iç ısı kazancı → artan ısıtma | Toplam tasarruf azalışı |
| Nötr | ECM'ler birbirini etkilemez | Kazan ekonomizer + kompresör VSD (farklı sistemler) | Etki yok |

### 5.2 Etkileşim Matrisi Örneği

Bir fabrikada eşzamanlı uygulanan ECM'ler arasındaki etkileşim haritası:

| ECM ↓ / ECM → | LED Aydınlatma | VSD Pompa | Kompresör VFD | Kazan Ekonomizer |
|---|:---:|:---:|:---:|:---:|
| LED Aydınlatma | — | ○ | ○ | ○ |
| VSD Pompa | ○ | — | ● Pozitif | ○ |
| Kompresör VFD | ○ | ● Pozitif | — | ○ |
| Kazan Ekonomizer | ○ | ○ | ○ | — |
| HVAC Optimizasyonu | ◐ Negatif | ● Pozitif | ○ | ◐ Negatif |

> ●: Önemli etkileşim, ◐: Orta etkileşim, ○: Etkileşim yok

### 5.3 Yönetim Stratejileri

1. **Ayrı Ölçüm:** Her ECM için bağımsız alt sayaç ile izole ölçüm (Opsiyon B)
2. **Sıralı Uygulama:** ECM'leri ardışık uygulayarak etkileşimi ayrıştırma
3. **Tesis Geneli:** Etkileşim yoğunsa Opsiyon C ile toplam tasarrufu doğrulama
4. **Mühendislik Hesabı:** Bilinen etkileşimleri formülle düzeltme

```
Etkileşim Düzeltme Formülü:
───────────────────────────────────────────
Toplam_Tasarruf ≠ Σ(Bireysel_Tasarruflar)
Toplam_Tasarruf = Σ(Bireysel_Tasarruflar) + Etkileşim_Düzeltmesi

Etkileşim_Düzeltmesi = Σᵢ Σⱼ (δᵢⱼ × Sᵢ × Sⱼ)

Burada:
  δᵢⱼ : Etkileşim katsayısı (−1 ile +1 arası)
  Sᵢ  : ECM i tasarrufu [kWh/yıl]
  Sⱼ  : ECM j tasarrufu [kWh/yıl]
───────────────────────────────────────────
```

## 6. Kalite Güvence (Quality Assurance)

### 6.1 Veri Doğrulama Prosedürü

| Kontrol | Yöntem | Eşik | Aksiyon |
|---|---|---|---|
| Eksik veri | Otomatik sayım | < %5 kabul | Enterpolasyon |
| Aykırı değer | 3σ kuralı | > 3 standart sapma | İnceleme + karar |
| Sensör kayması | Trend analizi | > %2/yıl | Kalibrasyon |
| Veri tutarlılığı | Çapraz kontrol | Enerji dengesi ±%3 | Araştırma |

### 6.2 Cihaz Kalibrasyonu

- Güç analizörü: yıllık kalibrasyon (ISO 17025 akrediteli laboratuvar)
- Debimetre: 2 yılda bir kalibrasyon + yıllık saha doğrulama
- Sıcaklık sensörü: yıllık 3 nokta kalibrasyonu (0°C, 25°C, 50°C)
- Basınç transmitter: yıllık kalibrasyon

### 6.3 Bağımsız Doğrulama

Bağımsız M&V denetçisinin yıllık kontrolü şunları kapsar:

1. Ölçüm cihazlarının kalibrasyon durumu
2. Veri toplama sürecinin doğruluğu
3. Regresyon modelinin uygunluğu (ASHRAE Guideline 14 kriterleri)
4. Tasarruf hesaplamalarının matematiksel doğruluğu
5. Rutin dışı düzeltmelerin geçerliliği

### 6.4 İhtilaf Çözüm Mekanizması

```
İhtilaf Çözüm Süreci:
═══════════════════════════════════════
Adım 1: Teknik Uzlaşı
  → ESCO ve müşteri M&V mühendisleri birlikte inceler
  → Süre: 15 iş günü

Adım 2: Bağımsız Denetçi Hakemliği
  → Bağımsız M&V denetçisi karar verir
  → Süre: 30 iş günü

Adım 3: Teknik Hakem Heyeti
  → 3 kişilik bağımsız uzman heyet
  → Süre: 60 iş günü
  → Karar bağlayıcıdır
═══════════════════════════════════════
```

## 7. İlgili Dosyalar

- [IPMVP Çerçevesi](mv_ipmvp.md) — Protokol seçimi, ESCO bağlamı, dijital M&V
- [İstatistiksel Yöntemler](mv_statistics.md) — Regresyon analizi, ASHRAE Guideline 14, belirsizlik
- [M&V Formül Detayları](../../factory/measurement_verification.md) — IPMVP opsiyon formülleri ve baseline ayarlama
- [Veri Toplama](../../factory/data_collection.md) — Veri toplama altyapısı ve yöntemleri
- [Energy Management INDEX](INDEX.md) — Enerji yönetimi bilgi tabanı ana dizin

## 8. Referanslar (References)

1. EVO (Efficiency Valuation Organization), "IPMVP Core Concepts 2022," EVO 10400-1:2022.
2. ASHRAE, "ASHRAE Guideline 14-2014: Measurement of Energy, Demand, and Water Savings," ASHRAE, 2014.
3. ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations."
4. U.S. DOE, "M&V Guidelines: Measurement and Verification for Performance-Based Contracts," Version 4.0, 2015.
5. FEMP, "M&V Best Practices Guide," Version 3.0, Federal Energy Management Program.
6. T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Verimlilik Artırıcı Proje (VAP) Başvuru Kılavuzu," YEGM.
7. Reddy, T.A., "Applied Data Analysis and Modeling for Energy Engineers and Scientists," Springer, 2011.
8. IPMVP Committee, "IPMVP Statistics and Uncertainty for IPMVP," EVO 10400-1:2014, Annex B.
