---
title: "Aksiyon Planlama ve Hedef Belirleme (Action Planning and Target Setting)"
category: factory
equipment_type: factory
keywords: [aksiyon planı, hedef belirleme, EnPI hedefi, ECM, enerji koruma önlemi, SMART hedef, önceliklendirme, uygulama planı]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/iso_50001_overview.md, factory/energy_management/energy_review.md, factory/energy_management/baseline_enpi.md, factory/prioritization.md, factory/implementation.md]
use_when: ["Enerji hedefleri belirlenecekken", "Aksiyon planı hazırlanacakken", "ECM önceliklendirmesi yapılacağında"]
priority: medium
last_updated: 2026-02-01
---

# Aksiyon Planlama ve Hedef Belirleme (Action Planning and Target Setting)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

ISO 50001:2018 Madde 6.2 (Hedefler, enerji hedefleri ve bunları gerçekleştirmek için planlama), enerji performansının sürekli iyileştirilmesi için ölçülebilir hedefler ve yapılandırılmış eylem planları gerektirir. Bu dosya; hedef belirleme metodolojisi, ECM (Energy Conservation Measure) tanımlama ve önceliklendirme, aksiyon planı şablonları ve ilerleme izleme mekanizmalarını kapsar.

### 1.1 ISO 50001 Madde 6.2 Gereksinimleri

```
Organizasyon şunları yapmalıdır:

a) İlgili fonksiyonlar ve seviyelerde enerji hedefleri belirlemek
b) Hedefler belirlenirken şunları dikkate almak:
   ├── SEU'lar ve enerji inceleme çıktıları
   ├── İyileştirme fırsatları
   ├── Yasal ve diğer gereksinimler
   ├── Organizasyonun koşulları (finansal, teknik, operasyonel)
   └── Teknolojik seçenekler
c) Hedefleri gerçekleştirmek için eylem planları hazırlamak:
   ├── Ne yapılacak
   ├── Hangi kaynaklar gerekecek
   ├── Kim sorumlu olacak
   ├── Ne zaman tamamlanacak
   ├── Sonuçlar nasıl değerlendirilecek
   └── EnPI'daki iyileşme nasıl doğrulanacak
```

### 1.2 Hedef-Aksiyon İlişkisi

```
Hiyerarşi:

Enerji Politikası → Stratejik yön (sürekli iyileştirme taahhüdü)
    ↓
Enerji Hedefleri → Ölçülebilir sonuçlar (EnPI bazlı)
    ↓
Eylem Planları → Hedeflere ulaşmak için yapılacaklar (ECM'ler)
    ↓
Operasyonel Kontrol → Günlük uygulamalar
    ↓
İzleme ve Ölçme → Performans doğrulama (EnPI trend)
```

## 2. Hedef Belirleme (Target Setting)

### 2.1 SMART Kriterleri

```
SMART hedef örnekleri:

S — Specific (Belirli):
  ✗ "Enerji tüketimini azalt"
  ✓ "Basınçlı hava sistemi SPC'yi 7.2'den 6.5 kW/(m³/min)'e düşür"

M — Measurable (Ölçülebilir):
  ✗ "Kazan verimini artır"
  ✓ "Kazan yakma verimini %86'dan %91'e çıkar (baca gazı O₂ izleme ile)"

A — Achievable (Ulaşılabilir):
  ✗ "Exergy verimini %100'e çıkar" (termodinamik olarak imkansız)
  ✓ "Fabrika exergy verimini %28'den %32'ye çıkar (sektör üst çeyrek)"

R — Relevant (İlgili):
  ✗ "Ofis kağıt tüketimini azalt" (EnMS ile dolaylı ilişkili)
  ✓ "SEU-001 kompresör spesifik güç tüketimini düşür (enerji politikası hedefi)"

T — Time-bound (Zamanlı):
  ✗ "Bir gün yapacağız"
  ✓ "2026-Q4 sonuna kadar SPC ≤ 6.5 kW/(m³/min)"
```

### 2.2 Top-Down vs Bottom-Up Yaklaşım

| Yaklaşım | Tanım | Avantaj | Dezavantaj | Uygun Durum |
|-----------|-------|---------|------------|-------------|
| Top-Down | Üst yönetim genel hedef belirler, birimlere dağıtır | Stratejik uyum, hızlı | Gerçekçi olmayabilir | İlk yıl, olgun organizasyon |
| Bottom-Up | ECM potansiyelleri toplanır, hedef oluşturulur | Gerçekçi, teknik dayanak | Yavaş, ambisyon düşük kalabilir | Energy review sonrası |
| Karma | Üst yönetim çerçeve, teknik ekip detay | Dengeli, doğrulanmış | Koordinasyon gerekli | Önerilen yaklaşım |

### 2.3 Yıllık Hedef Belirleme Metodolojisi

```
Adım adım hedef belirleme:

1. Energy review çıktılarını derle:
   ├── SEU listesi ve mevcut performanslar (EnPI)
   ├── Benchmark karşılaştırma sonuçları
   ├── Belirlenen iyileştirme fırsatları (ECM listesi)
   └── Exergy verimlilik haritası (ExergyLab)

2. Teknik potansiyeli hesapla:
   ├── Her ECM için teorik tasarruf potansiyeli
   ├── Gerçekleşme oranı uygula (%60-80 tipik)
   ├── Etkileşimleri dikkate al (overlap düzeltmesi)
   └── Net tasarruf potansiyeli = Σ(ECM_i × gerçekleşme_i × (1 - overlap))

3. Hedef düzeyini belirle:
   ├── Agresif: Net potansiyelin %80-100'ü
   ├── Gerçekçi: Net potansiyelin %50-80'i
   └── Muhafazakar: Net potansiyelin %30-50'si

4. Hedefi EnPI'lara çevir:
   ├── Fabrika SEC hedefi [kWh/ton]
   ├── Her SEU EnPI hedefi
   ├── Exergy verimi hedefi (ExergyLab ile)
   └── Mutlak tasarruf hedefi [MWh veya TEP]

5. Onay ve iletişim:
   ├── Enerji ekibi teknik doğrulama
   ├── Üst yönetim onayı
   └── İlgili birimlere dağıtım ve iletişim
```

### 2.4 Sektörel Referans Hedefler

| Sektör | Tipik İyileştirme [%/yıl] | Agresif Hedef [%/yıl] | Açıklama |
|--------|---------------------------|----------------------|----------|
| Çimento | 1-3 | 3-5 | Olgun sektör, marjinal iyileşme |
| Demir-Çelik | 2-4 | 4-6 | Enerji yoğun, büyük potansiyel |
| Kimya | 2-3 | 3-5 | Proses bağımlı |
| Gıda | 3-5 | 5-8 | Çeşitli fırsat, orta olgunluk |
| Tekstil | 3-5 | 5-8 | Buhar ve kurutma odaklı |
| Otomotiv | 2-4 | 4-6 | Boyahane ve basınçlı hava odaklı |
| Cam | 1-3 | 3-5 | Fırın dominant |
| Kağıt | 2-4 | 4-6 | Kurutma ve buhar odaklı |

## 3. ECM Belirleme ve Değerlendirme (ECM Identification and Evaluation)

### 3.1 ECM Tanımlama Kaynakları

```
ECM kaynakları:

1. Energy review bulguları:
   ├── Benchmark farkları (sektör, BAT, tedarikçi)
   ├── Exergy kayıp noktaları (ExergyLab)
   └── Cross-equipment fırsatlar

2. Enerji denetim sonuçları:
   ├── Walk-through gözlemler
   ├── Ölçüm ve analiz bulguları
   └── Termal kamera ve kaçak tespit

3. Teknoloji taraması:
   ├── BAT/BREF dokümanları
   ├── Ekipman tedarikçi önerileri
   └── Sektörel konferans ve yayınlar

4. Operasyonel deneyim:
   ├── Operatör önerileri
   ├── Bakım kayıtları analizi
   └── Benzer tesislerden öğrenme (best practice)
```

### 3.2 Ön Fizibilite ve Maliyet-Fayda Sınıflandırma

| Kategori | Yatırım Aralığı | Geri Ödeme | Karar Süreci | Örnekler |
|----------|-----------------|------------|-------------|----------|
| No-cost (sıfır maliyet) | €0 | Anında | Hemen uygula | Set point ayarı, zamanlama |
| Low-cost (düşük maliyet) | <€5.000 | <6 ay | Enerji ekibi onayı | Kaçak onarım, yalıtım tamir |
| Medium-cost (orta maliyet) | €5-50.000 | 6 ay-3 yıl | Enerji yöneticisi + finans | VSD, LED, ekonomizer |
| Capital (yüksek yatırım) | >€50.000 | >3 yıl | Üst yönetim onayı + fizibilite | CHP, GES, proses değişikliği |

### 3.3 ECM Değerlendirme Matrisi

```
ECM değerlendirme formülü:

ECM Skor = Σ(Ağırlık_i × Puan_i) / Σ(Ağırlık_i)

| Kriter | Ağırlık [%] | 1 (En düşük) | 3 (Orta) | 5 (En yüksek) |
|--------|-------------|-------------|----------|---------------|
| Tasarruf | 25 | <€2.000/yıl | €5-15.000/yıl | >€50.000/yıl |
| Geri ödeme | 25 | >7 yıl | 3-5 yıl | <1 yıl |
| Kolaylık | 20 | Major proje | Orta karmaşıklık | Hemen uygulanabilir |
| Risk | 15 | Yüksek üretim riski | Orta risk | Risksiz |
| Ek fayda | 15 | Ek fayda yok | Tek ek fayda | Çok yönlü fayda |

Sınıflandırma:
├── Skor ≥ 4.0 → Öncelik 1 — Hemen uygula (0-3 ay)
├── Skor 3.0-3.9 → Öncelik 2 — Kısa vadede planla (3-12 ay)
├── Skor 2.0-2.9 → Öncelik 3 — Orta vadede planla (12-24 ay)
└── Skor < 2.0 → Öncelik 4 — Stratejik değerlendir veya ertele
```

## 4. Önceliklendirme Metodolojisi (Prioritization Methodology)

### 4.1 Çoklu Kriter Değerlendirme

| Kriter | Tanım | Ağırlık [%] | Veri Kaynağı |
|--------|-------|-------------|-------------|
| ROI (Return on Investment) | Yatırım getirisi | 25 | Fizibilite analizi |
| Uygulama riski | Üretim/güvenlik/teknik risk | 15 | Risk değerlendirme |
| Uygulama kolaylığı | Teknik karmaşıklık, süre | 20 | Mühendislik değerlendirme |
| Stratejik uyum | Şirket stratejisi ile örtüşme | 10 | Yönetim politikası |
| Exergy etkisi | Exergy verimlilik iyileşmesi | 15 | ExergyLab analizi |
| Çevresel etki | CO₂ azaltma potansiyeli | 15 | Emisyon hesaplama |

### 4.2 Ağırlıklı Puanlama Tablosu

```
Örnek — 6 ECM'nin ağırlıklı puanlama ile önceliklendirmesi:

| ECM | ROI | Risk | Kolaylık | Strateji | Exergy | Çevre | TOPLAM |
|     | ×25 | ×15  | ×20      | ×10      | ×15    | ×15   | /100   |
|-----|-----|------|----------|----------|--------|-------|--------|
| A   | 5   | 5    | 5        | 3        | 3      | 3     | 4.20   |
| B   | 4   | 4    | 4        | 4        | 4      | 4     | 4.00   |
| C   | 3   | 4    | 3        | 5        | 5      | 5     | 3.90   |
| D   | 4   | 3    | 3        | 3        | 3      | 4     | 3.40   |
| E   | 2   | 4    | 2        | 4        | 4      | 5     | 3.15   |
| F   | 2   | 3    | 2        | 5        | 5      | 5     | 3.20   |

Sonuç: A ve B → Öncelik 1, C → Öncelik 2, D-F → Öncelik 2-3
```

### 4.3 ExergyLab ile Entegrasyon

```
ExergyLab'ın önceliklendirmeye katkısı:

1. Exergy bazlı kayıp sıralaması:
   ├── Her ekipman ve sistemin exergy yıkımı [kW]
   ├── İyileştirme potansiyeli: IP = (1 - η_ex) × Ė_giriş
   └── Exergy maliyet: €/kW_ex tasarruf

2. Cross-equipment fırsat tespiti:
   ├── Atık ısı → sıcak su/buhar eşleştirme
   ├── Sıcaklık seviyesi uyumu (pinch analizi)
   └── Entegrasyon tasarruf potansiyeli

3. Senaryo analizi:
   ├── ECM uygulaması öncesi/sonrası exergy haritası
   ├── Fabrika exergy veriminin tahmini iyileşmesi
   └── Sankey diyagramı ile görselleştirme
```

## 5. Aksiyon Planı Şablonu (Action Plan Template)

### 5.1 Detaylı Aksiyon Planı Tablosu

| ECM Kodu | ECM Açıklaması | SEU | Sorumlu | Başlangıç | Bitiş | Bütçe [€] | Tasarruf [€/yıl] | EnPI Etkisi | Durum |
|----------|---------------|-----|---------|-----------|-------|-----------|-----------------|-------------|-------|
| ECM-001 | Kompresör basınç optimizasyonu (7.5→6.8 bar) | B.Hava | Üretim Müh. | 2026-03 | 2026-05 | 1.500 | 12.000 | SPC -8% | Planlandı |
| ECM-002 | Basınçlı hava kaçak onarımı | B.Hava | Bakım | 2026-03 | 2026-04 | 5.000 | 18.000 | SPC -5% | Planlandı |
| ECM-003 | Kazan ekonomizer kurulumu | Buhar | Proje Müh. | 2026-06 | 2026-10 | 35.000 | 22.000 | η +4% | Fizibilite |
| ECM-004 | VSD retrofit (soğuk su pompası) | Soğutma | Proje Müh. | 2026-05 | 2026-08 | 18.000 | 9.500 | η_pompa +12% | Teklif |
| ECM-005 | Buhar kapanı onarım/değişim | Buhar | Bakım | 2026-04 | 2026-05 | 8.000 | 15.000 | Kaçak -%80 | Planlandı |

### 5.2 ISO 50001 Uyumlu Eylem Planı Detayı

```
EYLEM PLANI — ECM-001: Kompresör Basınç Optimizasyonu
═══════════════════════════════════════════════════════

Genel Bilgiler:
  Plan No        : EP-2026-001
  SEU            : Basınçlı hava sistemi (SEU-001)
  EnPI           : SPC [kW/(m³/min)]
  Mevcut EnPI    : 7.2 kW/(m³/min)
  Hedef EnPI     : 6.5 kW/(m³/min) (ECM-001 + ECM-002 kombine)
  Hedef tarihi   : 2026-09-30
  Sorumlu        : [Üretim Mühendisi Adı]
  Sponsor        : [Fabrika Müdürü]

Eylem Adımları:
  1. Mevcut basınç profili ölçümü
     - Sorumlu: Bakım Ekibi
     - Kaynak: Basınç kaydedici (7 gün sürekli)
     - Başlangıç: 2026-03-01
     - Bitiş: 2026-03-15
     - Bütçe: €500

  2. Kullanım noktası minimum basınç tespiti
     - Sorumlu: Üretim Mühendisi
     - Kaynak: Nokta bazlı ölçüm, ekipman kılavuzları
     - Başlangıç: 2026-03-15
     - Bitiş: 2026-03-31
     - Bütçe: €0

  3. Basınç düşürme testi (7.5 → 7.0 → 6.8 bar)
     - Sorumlu: Üretim Mühendisi
     - Kaynak: Kademeli test, operatör geri bildirimi
     - Başlangıç: 2026-04-01
     - Bitiş: 2026-05-15
     - Bütçe: €1.000 (basınç düzenleyici ayar/değişim)

Doğrulama:
  Yöntem: Haftalık SPC ölçümü (SCADA verisi)
  Baseline SPC: 7.2 kW/(m³/min) (2025 yılı 12 ay ortalaması)
  Ara hedef: SPC ≤ 6.9 (2026-06-30)
  Nihai hedef: SPC ≤ 6.5 (2026-09-30, ECM-002 ile birlikte)
  Beklenen tasarruf: 85 MWh/yıl = €8.500/yıl (ECM-001 payı)
  Tasarruf doğrulama: 3 aylık ortalama SPC ile M&V

Risk Değerlendirme:
  ├── Düşük basınçta ekipman çalışmama riski → Kademeli test ile azaltma
  ├── Operatör tepkisi → Bilgilendirme ve test katılımı
  └── Pik talep anlarında basınç düşmesi → Kompresör kaskad kontrol ayarı
```

## 6. İzleme ve Raporlama (Monitoring and Reporting)

### 6.1 Aylık İzleme Mekanizması

```
Aylık enerji ekibi toplantısı gündemi:

1. EnPI performans güncellemesi:
   ├── Her SEU EnPI → Hedef vs Gerçek → Trafik ışığı (Y/K/R)
   ├── Fabrika SEC → Trend grafik
   ├── Exergy verimi → Trend grafik (ExergyLab)
   └── CUSUM → Kümülatif tasarruf grafik

2. ECM uygulama durumu:
   ├── Gantt chart güncelleme
   ├── Geride kalan projeler → Engeller ve çözüm
   ├── Tamamlanan projeler → M&V sonuçları
   └── Yeni fırsat değerlendirme

3. Kaynak ve bütçe:
   ├── Harcama vs bütçe karşılaştırma
   ├── Ek kaynak ihtiyaçları
   └── Tasarruf değeri kümülatif

4. Aksiyonlar:
   ├── Düzeltici aksiyonlar (sapma varsa)
   ├── Bir sonraki ay öncelikleri
   └── Yönetime eskalasyon gereken konular
```

### 6.2 Çeyreklik Yönetim Raporu

| Rapor Bölümü | İçerik | Gösterim |
|-------------|--------|----------|
| Yönetici özeti | 1 sayfa özet: hedef, gerçekleşme, tasarruf | Trafik ışığı |
| EnPI performansı | Tüm EnPI'lar hedef vs gerçek | Tablo + trend grafik |
| ECM ilerleme | Tamamlanan, devam eden, planlanan | Gantt chart |
| Finansal özet | Yatırım harcama, tasarruf değeri, ROI | Tablo + grafik |
| Risk ve engeller | Projeleri etkileyen sorunlar | Liste + aksiyon |
| Sonraki çeyrek planı | Planlanan faaliyetler ve bütçe | Tablo |

### 6.3 Sapma Analizi

```
EnPI sapma değerlendirme ve aksiyon:

| Sapma Düzeyi | Tanım | Aksiyon |
|-------------|-------|---------|
| Yeşil | EnPI hedeften ≤%5 iyi veya hedefte | Devam, başarıyı kaydet |
| Sarı | EnPI hedeften %5-10 kötü | Kök neden araştır, izle |
| Kırmızı | EnPI hedeften >%10 kötü | Acil müdahale, düzeltici faaliyet |
| Trend bozulma | Ardışık 3 ay kötüleşme | Sistematik analiz, yönetim bilgilendir |

Düzeltici faaliyet süreci:
1. Sapma tespiti (aylık EnPI izleme)
2. Ön değerlendirme (veri kalitesi kontrol, dış faktör analizi)
3. Kök neden analizi (5 Neden, Ishikawa)
4. Düzeltici faaliyet planı (sorumlu, tarih, kaynak)
5. Uygulama ve etkinlik doğrulama
6. Kayıt ve raporlama (ISO 50001 Madde 10.1 uyumu)
```

## 7. Çalışılmış Örnek — Otomotiv Fabrikası Aksiyon Planı

### 7.1 Fabrika Profili

```
Fabrika: Otomotiv parça üretim tesisi
Yıllık enerji tüketimi: 15.000 TEP
Yıllık enerji maliyeti: €2.100.000
SEU'lar: Basınçlı hava (%25), Isıl işlem (%20), Boyahane (%18),
         Buhar sistemi (%15), CNC tezgahlar (%10)
Hedef: %8 yıllık enerji tasarrufu (1.200 TEP = €168.000)
```

### 7.2 5 ECM'li Aksiyon Planı

```
ECM Portföyü — 2026 Yılı:

┌──────────────────────────────────────────────────────────────────────────┐
│ ECM  │ Açıklama                  │ Tasarruf │ Yatırım │ GÖS  │ Öncelik │
│ Kodu │                           │ [TEP/y]  │ [€]     │ [yıl]│         │
├──────┼───────────────────────────┼──────────┼─────────┼──────┼─────────┤
│ E-01 │ VSD retrofit (5 kompresör)│ 350      │ 45.000  │ 1.3  │ 1       │
│ E-02 │ Isı geri kazanım         │ 280      │ 65.000  │ 1.8  │ 1       │
│      │ (kompresör → kazan ön    │          │         │      │         │
│      │  ısıtma)                  │          │         │      │         │
│ E-03 │ LED aydınlatma dönüşüm   │ 120      │ 35.000  │ 2.3  │ 2       │
│ E-04 │ Buhar kapanı onarım/     │ 200      │ 12.000  │ 0.5  │ 1       │
│      │ değişim (42 adet)         │          │         │      │         │
│ E-05 │ Basınç optimizasyonu     │ 250      │ 3.000   │ 0.1  │ 1       │
│      │ (7.5 → 6.5 bar)          │          │         │      │         │
├──────┼───────────────────────────┼──────────┼─────────┼──────┼─────────┤
│ TOP. │                           │ 1.200    │ 160.000 │ 1.1  │         │
└──────────────────────────────────────────────────────────────────────────┘

Toplam tasarruf: 1.200 TEP/yıl = %8 = €168.000/yıl
Toplam yatırım: €160.000
Ortalama geri ödeme: 1.1 yıl (ağırlıklı)
```

### 7.3 Uygulama Zaman Çizelgesi

```
2026 Yılı ECM Uygulama Takvimi:

        Q1          Q2          Q3          Q4
   J  F  M    A  M  J    J  A  S    O  N  D
E-05 ████            (Basınç opt. — hemen başla)
E-04 ██████          (Buhar kapanı — bakım koordinasyonu)
E-01      ██████████  (VSD — tedarik + kurulum)
E-02          ██████████████  (Isı geri kazanım — proje)
E-03              ████████████  (LED — faz bazlı dönüşüm)

Kontrol noktaları:
├── 2026-03-31: E-05 ve E-04 tamamlanmış olmalı → Quick win tasarruf başlar
├── 2026-06-30: E-01 tamamlanmış olmalı → EnPI ara değerlendirme
├── 2026-09-30: E-02 ve E-03 büyük ölçüde tamamlanmış → Nihai değerlendirme
└── 2026-12-31: Tüm ECM tamamlanmış → Yıl sonu M&V
```

### 7.4 Exergy Perspektifi

```
ExergyLab ile ECM etki analizi:

Uygulama öncesi fabrika exergy durumu:
  Toplam exergy girişi: 8.500 kW
  Faydalı exergy çıkışı: 2.380 kW
  Fabrika η_ex: %28.0

ECM etkileri (exergy):
  E-01 VSD: Kompresör η_ex %12 → %18 (+6 puan)
  E-02 Isı geri kazanım: Cross-equipment η_ex artışı → Fabrika +2 puan
  E-04 Buhar kapanı: Buhar sistemi η_ex %35 → %39 (+4 puan)
  E-05 Basınç opt.: Kompresör η_ex +2 puan (düşük basınç → düşük exergy yıkımı)

Uygulama sonrası tahmini:
  Fabrika η_ex: %28.0 → %32.5 (+4.5 puan)
  Exergy iyileşme potansiyeli azalması: 520 kW (5.720 → 5.200 kW)

→ ExergyLab Sankey diyagramı: Uygulama öncesi ve sonrası görsel karşılaştırma
→ Bu analiz, klasik enerji analizinin gösteremediği "termodinamik kalite"
  iyileşmesini somutlaştırır
```

## 8. İlgili Dosyalar

- [Enerji Yönetimi INDEX](INDEX.md) — Bilgi tabanı navigasyonu
- [ISO 50001 Genel Bakış](iso_50001_overview.md) — Standart gereksinimleri (Madde 6.2)
- [Enerji İnceleme](energy_review.md) — İyileştirme fırsatlarının belirlenmesi
- [Baseline ve EnPI](baseline_enpi.md) — Hedef belirleme altyapısı
- [ISO 50001 Uygulama](iso_50001_implementation.md) — Uygulama yol haritası
- [Önceliklendirme (genel)](../prioritization.md) — Fabrika çapında önceliklendirme
- [Uygulama Rehberi (genel)](../implementation.md) — ECM uygulama detayları

## 9. Referanslar

- ISO 50001:2018, Clause 6.2 "Objectives, energy targets and action plans"
- ISO 50004:2020, Chapter 6 "Planning" — Hedef belirleme rehberliği
- ISO 50006:2014, "Measuring energy performance using EnB and EnPI"
- US DOE, "Energy Project Management Guide"
- UNIDO, "Practical Guide for Implementing an Energy Management System", Chapter 5
- IEA, "Energy Efficiency Indicators: Fundamentals on Statistics"
- Tsatsaronis, G. & Park, M-H., "On avoidable and unavoidable exergy destructions"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
