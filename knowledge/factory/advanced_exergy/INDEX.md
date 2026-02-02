---
title: "İleri Exergy Analizi Bilgi Tabanı İndeks (Advanced Exergy Analysis Index)"
category: reference
keywords: [ileri exergy, advanced exergy, kaçınılabilir, endojen, dekompozisyon, indeks]
related_files: [knowledge/factory/INDEX.md, knowledge/factory/advanced_exergy/overview.md, knowledge/factory/advanced_exergy/four_way_splitting.md]
use_when: ["İleri exergy analizi bilgi tabanı navigasyonu gerektiğinde"]
priority: high
last_updated: 2026-02-02
---
# İleri Exergy Analizi Bilgi Tabanı İndeks

## Genel Bakış

İleri exergy analizi (advanced exergy analysis), konvansiyonel exergy analizini kaçınılabilir/kaçınılamaz ve endojen/ekzojen dekompozisyonlarla genişleterek gerçek iyileştirme potansiyelini ortaya koyan bir metodoloji ailesidir. Bu dizin, Tsatsaronis & Morosuk'un geliştirdiği çerçeveye dayalı 18 dosyadan oluşur.

## Dosya Listesi

### Çekirdek Teori Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `overview.md` | İleri exergy analizi genel bakış, tarihçe, 3 dekompozisyon tanıtımı | Yüksek | İlk giriş noktası |
| `avoidable_unavoidable.md` | Kaçınılabilir/kaçınılamaz (AV/UN) dekompozisyon | Yüksek | I_AV, I_UN hesaplama |
| `endogenous_exogenous.md` | Endojen/ekzojen (EN/EX) dekompozisyon | Yüksek | I_EN, I_EX hesaplama |
| `four_way_splitting.md` | 4-yollu dekompozisyon ve IPN | Yüksek | Tam analiz ve önceliklendirme |
| `ideal_conditions.md` | Ekipman bazında ideal/kaçınılamaz koşullar referans tablosu | Yüksek | Parametre seçimi |
| `methodology.md` | 8-adımlı hesaplama metodolojisi | Yüksek | Hesaplama rehberi |

### Ekipman Bazında Dosyalar (`equipment_specific/`)
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `equipment_specific/compressor_advanced.md` | 75 kW vidalı kompresör worked example | Yüksek | Kompresör ileri analizi |
| `equipment_specific/boiler_advanced.md` | 4 ton/h buhar kazanı worked example | Yüksek | Kazan ileri analizi |
| `equipment_specific/heat_exchanger_advanced.md` | Atık ısı geri kazanım HX worked example | Yüksek | Isı değiştirici ileri analizi |
| `equipment_specific/turbine_advanced.md` | Buhar türbini CHP worked example | Yüksek | Türbin ileri analizi |
| `equipment_specific/pump_advanced.md` | 15 kW pompa + kısma vanası worked example | Yüksek | Pompa ileri analizi |
| `equipment_specific/chiller_advanced.md` | 300 kW santrifüj chiller worked example | Yüksek | Chiller ileri analizi |

### Uygulama Dosyaları
| Dosya | Açıklama | Öncelik | Kullanım |
|-------|----------|---------|----------|
| `interpretation_guide.md` | Sonuç yorumlama rehberi, karar kuralları | Yüksek | AI yorumlama desteği |
| `improvement_priority.md` | IPN formülü, θ sınıflandırma, önceliklendirme | Yüksek | Yatırım sıralama |
| `visualization.md` | Görselleştirme yöntemleri (wheel, bar, waterfall, Grassmann) | Orta | Görsel çıktı tasarımı |
| `limitations.md` | Sınırlılıklar, uyarılar, hassasiyet analizi | Orta | Sonuç güvenilirliği |
| `case_studies.md` | 3 vaka çalışması (kombine çevrim, soğutma, tekstil fabrikası) | Orta | Referans örnekler |

## Dosya Açıklamaları (Detaylı)

### Çekirdek Teori

- **`overview.md`** — İleri exergy analizinin tarihsel gelişimi (Tsatsaronis 1990'lardan itibaren), konvansiyonel exergy analizinin sınırlamaları, 3 temel dekompozisyon türünün tanıtımı. Her analizin başlangıç noktası.

- **`avoidable_unavoidable.md`** — Kaçınılabilir (AV) ve kaçınılamaz (UN) exergy yıkımı ayrıştırması. Gerçek iyileştirme potansiyelini ortaya koyar. Temel soru: "Bu kayıpların ne kadarını teknolojik olarak azaltabiliriz?"

- **`endogenous_exogenous.md`** — Endojen (EN) ve ekzojen (EX) exergy yıkımı ayrıştırması. Bileşenler arası etkileşimi ortaya koyar. Temel soru: "Bu kayıplar bileşenin kendisinden mi, yoksa diğer bileşenlerin etkisinden mi?"

- **`four_way_splitting.md`** — AV/UN ve EN/EX birleştirmesi ile 4-yollu matris: AV-EN, AV-EX, UN-EN, UN-EX. IPN (Improvement Priority Number) formülü. En güçlü karar destek aracı.

- **`ideal_conditions.md`** — Her ekipman tipi için ideal çalışma koşulları ve kaçınılamaz minimum değerler referans tablosu. Parametrik simülasyon girdisi.

- **`methodology.md`** — 8 adımlı sistematik hesaplama prosedürü: (1) Sistem modeli → (2) Konvansiyonel analiz → (3) İdeal koşullar → (4) Hibrit simülasyonlar → (5) AV/UN → (6) EN/EX → (7) 4-yollu → (8) Yorumlama.

### Ekipman Bazında Worked Examples

Her dosya, gerçekçi endüstriyel parametrelerle tam hesaplama örneği içerir:

| Ekipman | Dosya | Senaryo | Çıktı |
|---------|-------|---------|-------|
| Kompresör | `compressor_advanced.md` | 75 kW vidalı, basınç oranı 8:1 | AV-EN = %62 → VSD + soğutma opt. |
| Kazan | `boiler_advanced.md` | 4 ton/h buhar, doğalgaz | AV-EN = %35 → ekonomizer + O₂ trim |
| Isı Değiştirici | `heat_exchanger_advanced.md` | Atık ısı geri kazanım HX | AV-EN = %45 → yüzey artışı + ΔT azaltma |
| Türbin | `turbine_advanced.md` | Buhar türbini CHP | AV-EN = %28 → blade iyileştirme + yük eşleştirme |
| Pompa | `pump_advanced.md` | 15 kW + kısma vanası | AV-EN = %71 → VSD + vana eliminasyonu |
| Chiller | `chiller_advanced.md` | 300 kW santrifüj | AV-EN = %40 → kondenser opt. + VSD |

### Uygulama ve Yorumlama

- **`interpretation_guide.md`** — Sonuç yorumlama kuralları: AV-EN yüksek → bileşen iyileştirme, AV-EX yüksek → sistem yeniden tasarım, UN yüksek → teknoloji değişikliği gerekli. AI karar kuralları ve eşik değerleri.

- **`improvement_priority.md`** — IPN = I_AV,EN × (c_F / c_F,ref) × w_k formülü. θ sınıflandırma sistemi (θ > 0.7: acil, 0.4-0.7: planlı, < 0.4: izle). Fabrika seviyesi `../prioritization.md` ile entegrasyon.

- **`visualization.md`** — Exergy wheel diyagramı, stacked bar chart (4-yollu), waterfall chart (iyileştirme potansiyeli), Grassmann diyagramı adaptasyonu. Frontend entegrasyon notları.

- **`limitations.md`** — İdeal koşul tanımlarının subjektifliği, doğrusal süperpozisyon varsayımı, veri gereksinimleri, hassasiyet analizi yöntemleri. Sonuç güvenilirlik değerlendirmesi.

- **`case_studies.md`** — (1) 100 MW kombine çevrim santrali, (2) 500 kW soğutma sistemi, (3) Tekstil fabrikası 5-ekipman analizi. Her vakada tam 4-yollu sonuçlar ve yatırım önerileri.

## Çapraz Referans İlişkileri

İleri exergy analizi, diğer ileri analiz yöntemleriyle tamamlayıcıdır:

| İlişkili Yöntem | Bağlantı | Kullanım Senaryosu |
|-----------------|----------|---------------------|
| Exergoekonomik Analiz | `../exergoeconomic/advanced_exergoeconomic.md` | AV/UN ve EN/EX'in maliyet boyutu — Ċ_D dekompozisyonu |
| EGM (Entropi Üretim Min.) | `../entropy_generation/overview.md` | Entropi üretim kaynakları ↔ exergy yıkım kaynakları karşılaştırma |
| Termoekonomik Optimizasyon | `../thermoeconomic_optimization/iterative_method.md` | IPN sonuçları → iteratif optimizasyon girdisi |
| Pinch Analizi | `../pinch/fundamentals.md` | Isı entegrasyonu potansiyeli ↔ AV-EX exergy yıkımı |
| Konvansiyonel Exergy | `../../{equipment}/formulas.md` | Temel exergy hesaplamaları → ileri analiz girdisi |

## Navigasyon Kuralları

### Önerilen Okuma Sırası
```
1. overview.md                    → Genel kavram ve tarihçe
2. avoidable_unavoidable.md       → AV/UN dekompozisyon (Adım 1)
   + endogenous_exogenous.md      → EN/EX dekompozisyon (Adım 2, paralel okunabilir)
3. four_way_splitting.md          → 4-yollu birleştirme (Adım 3)
4. ideal_conditions.md            → Parametre referansı (gerektiğinde)
   + methodology.md               → Hesaplama adımları (gerektiğinde)
5. equipment_specific/{tip}.md    → İlgili ekipman detayı
6. interpretation_guide.md        → Sonuç yorumlama
7. improvement_priority.md        → Önceliklendirme
```

### AI Yorumlama İçin Yükleme Kuralları
1. İleri exergy analizi talep edildiğinde → `overview.md` + `four_way_splitting.md` yükle
2. Belirli ekipman için → `equipment_specific/{tip}_advanced.md` + `ideal_conditions.md` yükle
3. Önceliklendirme gerektiğinde → `improvement_priority.md` + `interpretation_guide.md` yükle
4. Metodoloji sorusu → `methodology.md` yükle
5. Sınırlılık/güvenilirlik sorusu → `limitations.md` yükle

### Bağımlılık İlişkileri
- `overview.md` → Tüm dosyalar (temel kavramlar)
- `ideal_conditions.md` → `equipment_specific/*.md` (parametre referansı)
- `methodology.md` → `avoidable_unavoidable.md` + `endogenous_exogenous.md` (adımlar)
- `four_way_splitting.md` → `avoidable_unavoidable.md` + `endogenous_exogenous.md` (birleştirme)
- `interpretation_guide.md` → `four_way_splitting.md` (sonuç okuma)
- `improvement_priority.md` → `four_way_splitting.md` + `../prioritization.md` (entegrasyon)

## Hızlı Karar Rehberi

```
İleri exergy analizi sonuçlarını yorumla:
  |
  +-- I_AV,EN yüksek (>%50)?
  |     |-- Evet → Bileşenin kendisini iyileştir (VSD, bakım, boyut)
  |     |-- Hayır → Aşağıya devam
  |
  +-- I_AV,EX yüksek (>%30)?
  |     |-- Evet → Diğer bileşenleri iyileştir veya sistem yeniden tasarla
  |     |-- Hayır → Aşağıya devam
  |
  +-- I_UN yüksek (>%60)?
  |     |-- Evet → Mevcut teknolojiyle sınırlı. Teknoloji değişikliği düşün.
  |     |-- Hayır → Bileşen iyi durumda, başka bileşenlere odaklan
  |
  +-- IPN ile önceliklendir → improvement_priority.md
```

## Dosya Sayısı Özeti

| Kategori | Dosya Sayısı |
|----------|-------------|
| Çekirdek teori | 6 |
| Ekipman bazında worked examples | 6 |
| Uygulama ve yorumlama | 5 |
| Navigasyon (INDEX.md) | 1 |
| **Toplam** | **18** |

## İlgili Dosyalar

### Bu Dizindeki Dosyalar
- `overview.md` — İleri exergy analizi genel bakış ve tarihçe
- `avoidable_unavoidable.md` — Kaçınılabilir/kaçınılamaz dekompozisyon
- `endogenous_exogenous.md` — Endojen/ekzojen dekompozisyon
- `four_way_splitting.md` — 4-yollu dekompozisyon ve IPN
- `ideal_conditions.md` — Ekipman bazında ideal koşullar referans tablosu
- `methodology.md` — 8-adımlı hesaplama metodolojisi
- `interpretation_guide.md` — Sonuç yorumlama rehberi
- `improvement_priority.md` — IPN formülü ve önceliklendirme
- `visualization.md` — Görselleştirme yöntemleri
- `limitations.md` — Sınırlılıklar ve uyarılar
- `case_studies.md` — Vaka çalışmaları

### Ekipman Bazında İleri Analiz
- `equipment_specific/compressor_advanced.md` — Kompresör ileri exergy analizi
- `equipment_specific/boiler_advanced.md` — Kazan ileri exergy analizi
- `equipment_specific/heat_exchanger_advanced.md` — Isı değiştirici ileri analizi
- `equipment_specific/turbine_advanced.md` — Türbin ileri exergy analizi
- `equipment_specific/pump_advanced.md` — Pompa ileri exergy analizi
- `equipment_specific/chiller_advanced.md` — Chiller ileri exergy analizi

### İlişkili Üst Dizin ve Çapraz Referanslar
- `../INDEX.md` — Fabrika bilgi tabanı ana indeks
- `../../INDEX.md` — ExergyLab bilgi tabanı ana indeks
- `../exergoeconomic/advanced_exergoeconomic.md` — İleri exergoekonomik analiz (maliyet dekompozisyonu)
- `../entropy_generation/overview.md` — EGM ile karşılaştırma
- `../prioritization.md` — Yatırım önceliklendirme (IPN entegrasyonu)

## Referanslar

1. Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
2. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391.
3. Morosuk, T. & Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258.
4. Tsatsaronis, G. & Morosuk, T. (2010). "Advanced exergetic analysis of a novel system for generating electricity and vaporizing liquefied natural gas." *Energy*, 35(2), 820-829.
5. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
