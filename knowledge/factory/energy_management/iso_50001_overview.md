---
title: "ISO 50001 Enerji Yönetim Sistemi Standart Analizi (ISO 50001 Energy Management System Standard Analysis)"
category: factory
equipment_type: factory
keywords: [ISO 50001, enerji yönetim sistemi, EnMS, HLS, PDCA, enerji politikası, enerji planlaması, sürekli iyileştirme]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/iso_50001_implementation.md, factory/energy_management/energy_review.md, factory/energy_management/baseline_enpi.md, factory/energy_management/continuous_improvement.md, factory/energy_management/turkey_legislation.md, factory/energy_management.md]
use_when: ["ISO 50001 standart gereksinimleri sorgulandığında", "EnMS kurulumu planlandığında", "Madde bazlı analiz gerektiğinde"]
priority: high
last_updated: 2026-02-01
---

# ISO 50001:2018 Enerji Yönetim Sistemi Standart Analizi

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

ISO 50001:2018, organizasyonların enerji performansını (Energy Performance) sistematik ve sürekli olarak iyileştirmesini sağlayan uluslararası enerji yönetim sistemi (EnMS — Energy Management System) standardıdır. Uluslararası Standardizasyon Örgütü (ISO) tarafından ilk kez 2011 yılında yayınlanmış, 2018 yılında kapsamlı bir revizyonla Annex SL yüksek seviye yapısına (HLS — High Level Structure) uyumlu hale getirilmiştir.

### 1.1 Standardın Amacı ve Kapsamı

ISO 50001:2018 aşağıdaki hedeflere yönelik gereksinimler tanımlar:

- Enerji politikası (Energy Policy) oluşturma ve sürdürme
- Enerji performansını etkileyen faktörlerin sistematik analizi
- Ölçülebilir enerji hedefleri (Energy Objectives) ve eylem planları belirleme
- Enerji verilerine dayalı karar alma mekanizması kurma
- Enerji performansının sürekli iyileştirilmesi (Continual Improvement)

Standart; sektör, büyüklük veya coğrafi konum ayrımı gözetmeksizin her tür organizasyona uygulanabilir. Sertifikasyon zorunlu olmamakla birlikte, bağımsız denetim (Third-party Audit) ile belgelendirme mümkündür.

### 1.2 2011 Versiyonundan 2018 Versiyonuna Geçiş

| Özellik | ISO 50001:2011 | ISO 50001:2018 |
|---------|----------------|----------------|
| Yapı | Bağımsız madde sıralaması | Annex SL / HLS uyumlu (10 madde) |
| Risk odak | Mevcut değil | Risk ve fırsat bazlı düşünme (Madde 6.1) |
| Bağlam analizi | Mevcut değil | İç/dış bağlam analizi zorunlu (Madde 4.1) |
| EnPI / EnB | Genel gereksinim | Normalizasyon ve istatistiksel doğrulama zorunlu |
| Üst yönetim rolü | Enerji yöneticisi odaklı | Üst yönetim liderlik sorumluluğu güçlendirildi |
| Dokümantasyon | Prosedür (Procedure) bazlı | "Dokümante bilgi" (Documented Information) — esneklik |
| SEU (Önemli Enerji Kullanımı) | Genel tanım | SEU kriterleri ve operasyonel kontrol detaylandırıldı |
| Entegrasyon | Sınırlı | ISO 9001, 14001, 45001 ile kolay entegrasyon |

### 1.3 Temel Kavramlar ve Tanımlar

| Kavram | İngilizce Karşılığı | Tanım |
|--------|---------------------|-------|
| Enerji Yönetim Sistemi | EnMS (Energy Management System) | Enerji politikası, hedefler, süreçler ve kaynakların bütünü |
| Enerji Performans Göstergesi | EnPI (Energy Performance Indicator) | Enerji performansını ölçen ve izleyen nicel metrik |
| Enerji Temel Çizgisi | EnB (Energy Baseline) | Performans karşılaştırması için referans dönem verisi |
| Önemli Enerji Kullanımı | SEU (Significant Energy Use) | Toplam tüketimde büyük paya sahip veya iyileştirme potansiyeli yüksek alan |
| İlgili Değişkenler | Relevant Variables | Enerji tüketimini ölçülebilir biçimde etkileyen faktörler (üretim miktarı, hava sıcaklığı vb.) |
| Statik Faktörler | Static Factors | Sabit kalan ancak enerjiyi etkileyen koşullar (bina alanı, ekipman kapasitesi vb.) |
| Enerji İnceleme | Energy Review | Mevcut enerji kullanımının ve performansının sistematik analizi |

## 2. Madde Analizi (Clause-by-Clause Analysis)

Aşağıdaki tablo, ISO 50001:2018 standardının 4 ila 10 numaralı maddelerinin anahtar gereksinimlerini, dikkat edilmesi gereken noktaları ve ExergyLab ile bağlantısını özetler.

| Madde No | Başlık | Anahtar Gereksinimler | Dikkat Edilecekler | ExergyLab Bağlantısı |
|----------|--------|----------------------|--------------------|-----------------------|
| 4.1 | Organizasyonun bağlamı (Context) | İç ve dış konuların belirlenmesi | Enerji fiyatları, mevzuat, teknoloji trendleri | Sektörel benchmark verisi sağlar |
| 4.2 | İlgili taraflar (Interested Parties) | İhtiyaç ve beklentilerin tespiti | Müşteri ESG beklentileri, YEGM zorunlulukları | — |
| 4.3 | Kapsam (Scope) | EnMS organizasyonel ve fiziksel sınırları | SEU kapsam dışı bırakılamaz | Fabrika sınır tanımı ile örtüşür |
| 4.4 | EnMS (Energy Management System) | Süreç bazlı EnMS kurulumu | PDCA döngüsü ile entegrasyon | — |
| 5.1 | Liderlik ve taahhüt (Leadership) | Üst yönetim sorumluluğu, kaynak tahsisi | CEO/GM görünürlüğü kritik | — |
| 5.2 | Enerji politikası (Energy Policy) | Politika oluşturma, iletme, gözden geçirme | Sürekli iyileştirme taahhüdü zorunlu | — |
| 5.3 | Roller ve sorumluluklar (Roles) | Enerji ekibi, yetki matrisi | Çapraz fonksiyonel ekip yapısı önerilir | — |
| 6.1 | Risk ve fırsatlar (Risks & Opportunities) | Stratejik risk değerlendirmesi | Exergy analizi bir "fırsat" olarak tanımlanabilir | Exergy kayıp analizi fırsat tespiti sağlar |
| 6.2 | Yasal gereksinimler (Legal Requirements) | Uygulanabilir mevzuatın belirlenmesi | 5627 sayılı Kanun, YEGM yönetmelikleri | — |
| 6.3 | Enerji inceleme (Energy Review) | SEU, ilgili değişkenler, iyileştirme fırsatları | Pareto ile SEU belirleme, 80/20 kuralı | Exergy verimlilik haritası, Sankey |
| 6.4 | EnPI (Energy Performance Indicators) | Performans göstergesi tanımlama ve izleme | Normalizasyon (regresyon) zorunlu | Exergy-bazlı EnPI tanımlama |
| 6.5 | EnB (Energy Baseline) | Referans dönemi belirleme, doğrulama | Statik faktör değişiminde EnB ayarlaması | Exergy baseline oluşturma |
| 6.6 | Hedefler ve eylem planları (Objectives) | SMART hedefler, ECM önceliklendirme | Her SEU için en az bir hedef | Exergy kayıp bazlı ECM sıralaması |
| 7.1 | Kaynaklar (Resources) | İnsan, altyapı, finansal kaynaklar | Alt sayaç altyapısı minimum gereksinim | — |
| 7.2 | Yetkinlik (Competence) | Eğitim ihtiyaç analizi, yetkinlik doğrulama | SEU operatörleri özel eğitim gerektirir | — |
| 7.3 | Farkındalık (Awareness) | Tüm personel farkındalık eğitimi | Enerji politikası ve hedefleri bilinmeli | — |
| 7.4 | İletişim (Communication) | İç ve dış iletişim planı | Enerji performansı görsel yönetimi | Dashboard ve Sankey görselleri |
| 7.5 | Dokümante bilgi (Documented Information) | Oluşturma, güncelleme, kontrol | Mevcut ISO 9001/14001 altyapısı kullanılabilir | — |
| 8.1 | Operasyonel kontrol (Operational Control) | SEU bazında kontrol prosedürleri | Bakım planı enerji perspektifli olmalı | Ekipman bazında exergy izleme |
| 8.2 | Tasarım ve satın alma (Design & Procurement) | Enerji verimli tasarım/satın alma kriterleri | LCC hesaplama zorunluluğu (>belirli eşik) | — |
| 9.1 | İzleme ve ölçme (Monitoring & Measurement) | EnPI izleme planı, kalibrasyon | Ölçüm sıklığı ve doğruluğu kritik | Gerçek zamanlı exergy izleme |
| 9.2 | İç denetim (Internal Audit) | Planlı denetim programı, denetçi yetkinliği | Tüm maddeler kapsanmalı | — |
| 9.3 | Yönetim gözden geçirme (Management Review) | Girdiler, çıktılar, kararlar | EnPI trendleri ve hedef sapmaları girdisi | Exergy raporları yönetim girdisi olarak |
| 10.1 | Uygunsuzluk (Nonconformity) | Düzeltici faaliyet, kök neden analizi | 5 Neden, Ishikawa yöntemleri | — |
| 10.2 | Sürekli iyileştirme (Continual Improvement) | EnMS etkinliği ve enerji performansı | Hem sistem hem performans iyileştirmesi | Exergy ile derinlemesine iyileştirme |

## 3. High Level Structure — HLS (Yüksek Seviye Yapı)

ISO 50001:2018, Annex SL (şimdiki adı: ISO/IEC Directives Part 1, Appendix 2) uyumlu yüksek seviye yapıyı benimser. Bu yapı, tüm ISO yönetim sistemi standartlarında ortak bir çerçeve sunar.

### 3.1 HLS Madde Yapısı

```
ISO 50001:2018 HLS Yapısı:

Madde 1 — Kapsam (Scope)
Madde 2 — Atıf yapılan standartlar (Normative References)
Madde 3 — Terimler ve tanımlar (Terms and Definitions)
Madde 4 — Organizasyonun bağlamı (Context of the Organization)
├── 4.1 İç ve dış konular
├── 4.2 İlgili taraflar
├── 4.3 EnMS kapsamı
└── 4.4 EnMS
Madde 5 — Liderlik (Leadership)
├── 5.1 Liderlik ve taahhüt
├── 5.2 Enerji politikası
└── 5.3 Roller, sorumluluklar, yetkiler
Madde 6 — Planlama (Planning)
├── 6.1 Risk ve fırsatlar
├── 6.2 Yasal gereksinimler
├── 6.3 Enerji inceleme (Energy Review)
├── 6.4 EnPI
├── 6.5 EnB
└── 6.6 Hedefler ve eylem planları
Madde 7 — Destek (Support)
├── 7.1 Kaynaklar
├── 7.2 Yetkinlik
├── 7.3 Farkındalık
├── 7.4 İletişim
└── 7.5 Dokümante bilgi
Madde 8 — Operasyon (Operation)
├── 8.1 Operasyonel planlama ve kontrol
└── 8.2 Tasarım ve satın alma
Madde 9 — Performans değerlendirme (Performance Evaluation)
├── 9.1 İzleme, ölçme, analiz, değerlendirme
├── 9.2 İç denetim
└── 9.3 Yönetim gözden geçirme
Madde 10 — İyileştirme (Improvement)
├── 10.1 Uygunsuzluk ve düzeltici faaliyet
└── 10.2 Sürekli iyileştirme
```

### 3.2 HLS Entegrasyon Avantajı

HLS yapısı sayesinde ISO 50001:2018, diğer yönetim sistemi standartları ile doğrudan entegre edilebilir:

| HLS Maddesi | ISO 9001:2015 (Kalite) | ISO 14001:2015 (Çevre) | ISO 50001:2018 (Enerji) | ISO 45001:2018 (İSG) |
|-------------|------------------------|------------------------|-------------------------|-----------------------|
| 4 — Bağlam | İç/dış kalite konuları | Çevresel konular | Enerji konuları | İSG konuları |
| 5 — Liderlik | Kalite politikası | Çevre politikası | Enerji politikası | İSG politikası |
| 6 — Planlama | Risk/fırsat, hedefler | Çevresel boyutlar, hedefler | Energy review, SEU, EnPI, hedefler | Tehlike tanımlama, risk |
| 7 — Destek | Kaynaklar, yetkinlik, iletişim | Kaynaklar, yetkinlik, iletişim | Kaynaklar, yetkinlik, iletişim | Kaynaklar, yetkinlik, iletişim |
| 8 — Operasyon | Ürün/hizmet gerçekleştirme | Çevresel kontrol | Operasyonel kontrol, tasarım | İSG kontrolü |
| 9 — Değerlendirme | KPI izleme, iç denetim | İzleme, iç denetim | EnPI izleme, iç denetim | İSG izleme, iç denetim |
| 10 — İyileştirme | Düzeltici faaliyet, sürekli iyileştirme | Düzeltici faaliyet, sürekli iyileştirme | Düzeltici faaliyet, sürekli iyileştirme | Düzeltici faaliyet, sürekli iyileştirme |

## 4. PDCA Döngüsü Detay (Plan-Do-Check-Act Cycle)

ISO 50001:2018 standardı, enerji yönetim sisteminin PDCA (Plan-Do-Check-Act — Planla-Uygula-Kontrol Et-Önlem Al) döngüsü üzerine inşa edilmiştir. Her aşama enerji yönetimine özgü gereksinimler içerir.

### 4.1 Plan (Planla)

```
Plan aşaması — ISO 50001 maddeleri: 4, 5, 6

Temel faaliyetler:
├── Organizasyonun bağlamını anlamak (4.1, 4.2)
├── EnMS kapsamını belirlemek (4.3)
├── Enerji politikası oluşturmak (5.2)
├── Enerji ekibini kurmak (5.3)
├── Risk ve fırsatları değerlendirmek (6.1)
├── Yasal gereksinimleri belirlemek (6.2)
├── Enerji inceleme yapmak (6.3)
│   ├── Enerji kaynaklarını ve tüketimi analiz etmek
│   ├── SEU'ları belirlemek
│   ├── İlgili değişkenleri tanımlamak
│   └── İyileştirme fırsatlarını listelemek
├── EnPI tanımlamak (6.4)
├── EnB oluşturmak (6.5)
└── Hedefler ve eylem planları belirlemek (6.6)

Enerji-spesifik gereksinimler:
- EnPI normalizasyonu (ilgili değişkenlere göre regresyon)
- EnB istatistiksel doğrulaması (R² ≥ 0.75 önerilir)
- SEU bazında iyileştirme hedefleri (SMART formatında)
```

### 4.2 Do (Uygula)

```
Do aşaması — ISO 50001 maddeleri: 7, 8

Temel faaliyetler:
├── Kaynak tahsisi (7.1)
│   ├── İnsan kaynağı (enerji ekibi, eğitimli operatörler)
│   ├── Altyapı (alt sayaçlar, SCADA, yazılım)
│   └── Finansal (EnMS bütçesi, ECM yatırım fonları)
├── Yetkinlik geliştirme ve eğitim (7.2, 7.3)
├── İç/dış iletişim planı uygulaması (7.4)
├── Dokümantasyon yönetimi (7.5)
├── SEU operasyonel kontrolleri (8.1)
│   ├── Kontrol prosedürleri yazılması
│   ├── Sapma tespit mekanizması kurulması
│   └── Bakım planının enerji perspektifinden güncellenmesi
└── Tasarım ve satın alma kriterlerinin uygulanması (8.2)
    ├── LCC hesaplama şablonu
    └── Minimum verimlilik kriterleri (IE3/IE4 motor, vb.)
```

### 4.3 Check (Kontrol Et)

```
Check aşaması — ISO 50001 maddesi: 9

Temel faaliyetler:
├── EnPI izleme ve analiz (9.1.1)
│   ├── Periyodik veri toplama (sürekli/günlük/haftalık/aylık)
│   ├── EnPI trend analizi
│   ├── Hedef sapma değerlendirmesi
│   └── CUSUM analizi ile performans takibi
├── Yasal uyum değerlendirmesi (9.1.2)
├── İç denetim (9.2)
│   ├── Denetim planı (tüm maddeler kapsanmalı)
│   ├── Denetçi bağımsızlığı ve yetkinliği
│   └── Bulgu ve uygunsuzluk raporları
└── Yönetim gözden geçirme (9.3)
    ├── Girdiler: EnPI trendleri, denetim sonuçları, yasal uyum
    ├── Çıktılar: Kararlar, kaynak tahsisi, hedef güncellemeleri
    └── Sıklık: Minimum yılda 1, önerilen 6 ayda 1
```

### 4.4 Act (Önlem Al)

```
Act aşaması — ISO 50001 maddesi: 10

Temel faaliyetler:
├── Uygunsuzluk yönetimi (10.1)
│   ├── Tespit → Acil müdahale → Kök neden analizi
│   ├── Düzeltici faaliyet planlama ve uygulama
│   └── Etkinlik doğrulama
└── Sürekli iyileştirme (10.2)
    ├── EnMS etkinliğinin iyileştirilmesi (sistem boyutu)
    ├── Enerji performansının iyileştirilmesi (teknik boyut)
    ├── Yeni ECM projelerinin başlatılması
    └── EnPI hedeflerinin yükseltilmesi

Kök neden analizi yöntemleri:
- 5 Neden (5 Why) analizi
- Ishikawa (balık kılçığı) diyagramı
- Hata Türü ve Etkileri Analizi (FMEA — Failure Mode and Effects Analysis)
- Pareto analizi (en sık tekrar eden uygunsuzluklar)
```

## 5. EnMS Olgunluk Modeli (EnMS Maturity Model)

ISO 50004:2020 rehber standardı temel alınarak, beş seviyeli bir EnMS olgunluk modeli tanımlanmıştır. Bu model, organizasyonların mevcut durumunu değerlendirmesi ve hedef seviyeye ulaşmak için yol haritası oluşturması amacıyla kullanılır.

### 5.1 Beş Seviyeli Olgunluk Tanımları

| Seviye | Ad | İngilizce | Genel Tanım |
|--------|----|-----------|-------------|
| 1 | Başlangıç | Initial | Enerji yönetimi reaktif, sistematik değil, bireysel çabalara dayalı |
| 2 | Gelişen | Developing | Temel yapı oluşturulmuş, enerji verisi toplanıyor, SEU'lar belirlenmiş |
| 3 | Tanımlı | Defined | EnMS dokümante ve uygulanmış, EnPI izleniyor, ISO 50001 sertifika aşamasında |
| 4 | Yönetilen | Managed | Veriye dayalı proaktif yönetim, CUSUM analizi, hedefler tutuyor |
| 5 | Lider | Optimizing | Sürekli iyileştirme kültürü, ileri analiz (exergy, AI), sektörel liderlik |

### 5.2 Olgunluk Değerlendirme Matrisi

| Değerlendirme Boyutu | Seviye 1 — Başlangıç | Seviye 2 — Gelişen | Seviye 3 — Tanımlı | Seviye 4 — Yönetilen | Seviye 5 — Lider |
|----------------------|----------------------|--------------------|---------------------|----------------------|-------------------|
| **Politika** | Yok | Taslak mevcut | Onaylı ve tüm personele iletilmiş | Periyodik gözden geçirme yapılıyor | İş stratejisine entegre |
| **Planlama** | Reaktif müdahale | SEU'lar belirlenmiş | EnB + EnPI tanımlı ve izleniyor | Hedefler SMART ve ölçülebilir | Exergy-bazlı stratejik planlama |
| **Uygulama** | Ad hoc iyileştirmeler | Manuel kontroller | Prosedür bazlı operasyonel kontrol | Otomatik kontrol (VSD, O₂ trim) | Prediktif kontrol, AI optimizasyon |
| **Ölçüm** | Yalnızca fatura takibi | Ana sayaç izleme | Alt sayaçlar + SEU bazında ölçüm | Gerçek zamanlı SCADA/BMS | IoT sensörler + dijital ikiz |
| **İzleme** | Yıllık enerji raporu | Aylık EnPI takibi | Haftalık CUSUM analizi | Günlük dashboard izleme | Gerçek zamanlı alarm + anomali tespiti |
| **İyileştirme** | Sporadik, plansız | Planlı ECM projeleri | Sistematik ECM önceliklendirme | Sürekli iyileştirme döngüsü | İnovasyon odaklı (ORC, TES, GES) |
| **Kültür** | Bireysel ilgi | Enerji yöneticisi aktif | Enerji ekibi aktif | Tüm departmanlar katılıyor | Organizasyonel enerji kültürü |

### 5.3 Seviye Geçiş Gereksinimleri ve Süreleri

```
Seviye 1 → 2 (Tipik süre: 3-6 ay):
├── Enerji yöneticisi atanması (YEGM sertifikalı)
├── Son 12-36 ay enerji tüketim verilerinin toplanması
├── Pareto analizi ile SEU'ların belirlenmesi
├── Enerji politikası taslağı hazırlanması
└── İlk farkındalık eğitiminin verilmesi

Seviye 2 → 3 (Tipik süre: 6-12 ay):
├── EnMS dokümantasyonunun tamamlanması
├── EnB oluşturma ve istatistiksel doğrulama
├── EnPI tanımlama (her SEU için en az 1 adet)
├── Operasyonel kontrol prosedürlerinin yazılması
├── İç denetim planının hazırlanması ve ilk uygulanması
└── ISO 50001 gap analizi sonuçlarına göre kapanış

Seviye 3 → 4 (Tipik süre: 12-18 ay):
├── Alt sayaç altyapısının tamamlanması (SEU bazında)
├── CUSUM analizi uygulamasının başlatılması
├── Aylık EnPI trend analizi ve sapma raporlamasının rutinleşmesi
├── Yönetim gözden geçirme etkinliğinin artması
├── Dijital eylem planı takip sistemi kurulması
└── En az 2 başarılı ECM projesinin tamamlanması

Seviye 4 → 5 (Tipik süre: 18-36 ay):
├── Exergy analizi yetkinliği (ExergyLab entegrasyonu)
├── Dijital M&V (AMMV — Automated M&V) uygulaması
├── AI destekli anomali tespiti ve optimizasyon
├── Enerji kültürü programı (öneri sistemi, ödül mekanizması)
├── Sektörel benchmark liderliği (üst çeyrek — top quartile)
└── İleri teknoloji projesi (ORC, termal depolama, yenilenebilir entegrasyon)
```

### 5.4 Hızlı Olgunluk Değerlendirme Aracı

Aşağıdaki formül ile hızlı bir olgunluk puanı hesaplanabilir:

```
Olgunluk Puanı = Σ (Boyut_Puanı) / Boyut_Sayısı

Her boyut 1-5 arası puanlanır (yukarıdaki matrise göre).
Toplam 7 boyut × 5 maks puan = 35 maks.

Değerlendirme:
├──  7-11 puan → Seviye 1 (Başlangıç)
├── 12-17 puan → Seviye 2 (Gelişen)
├── 18-24 puan → Seviye 3 (Tanımlı)
├── 25-30 puan → Seviye 4 (Yönetilen)
└── 31-35 puan → Seviye 5 (Lider)
```

## 6. ISO 50001 ve Exergy İlişkisi (ISO 50001 & Exergy Relationship)

### 6.1 Mevcut Standart Perspektifi

ISO 50001:2018, enerji yönetimini büyük ölçüde termodinamiğin 1. yasasına (enerji korunumu — Energy Conservation) dayalı olarak ele alır. Standart metni "enerji performansı" (energy performance) kavramını kullanır; ancak açıkça "exergy" terimini içermez. Bu durum, düşük sıcaklıktaki atık ısı (Low-grade Waste Heat) gibi düşük exergy içerikli kayıpların standart enerji denetimlerinde fark edilememesine yol açabilir.

### 6.2 ExergyLab'ın ISO 50001 Süreçlerine Katkısı

| ISO 50001 Süreci | 1. Yasa (Enerji) Yaklaşımı | 2. Yasa (Exergy) Yaklaşımı — ExergyLab |
|-------------------|----------------------------|----------------------------------------|
| Enerji inceleme (6.3) | kW bazlı enerji dengesi, Sankey | Exergy dengesi, termodinamik kalite haritası |
| SEU belirleme (6.3) | En çok enerji tüketen ekipman | En çok exergy yıkan ekipman (kayıp kalitesi dahil) |
| EnPI tanımlama (6.4) | SEC (Specific Energy Consumption) — kWh/ton | Exergy verimi (ψ), exergy yıkım oranı (İ_D/İ_F) |
| Benchmark (6.3) | Enerji yoğunluğu karşılaştırma | Exergy verimlilik karşılaştırma (sektörel) |
| ECM önceliklendirme (6.6) | TEP tasarruf ve TL/yıl bazlı sıralama | Exergy kayıp × iyileştirme potansiyeli × ROI |
| İzleme (9.1) | Enerji tüketim trendi | Exergy verim trendi, Sankey zaman serisi |
| Raporlama (9.3) | Enerji maliyeti ve tüketim raporu | Exergy Sankey + AI yorumlu yönetim raporu |

### 6.3 Exergy-bazlı EnPI Örnekleri

```
Klasik EnPI (1. Yasa):
  SEC_kompresör = Elektrik tüketimi [kWh] / Hava üretimi [Nm³]
  SEC_kazan     = Yakıt tüketimi [kW] / Buhar üretimi [ton/h]
  COP_chiller   = Soğutma kapasitesi [kW] / Elektrik tüketimi [kW]

Exergy-bazlı EnPI (2. Yasa):
  ψ_kompresör = Havanın exergy artışı [kW] / Şaft gücü [kW]
  ψ_kazan     = Buharın exergy [kW] / Yakıtın exergy [kW]
  ψ_chiller   = Soğuk suyun exergy [kW] / (Kompresör gücü + Pompa gücü) [kW]
  η_fabrika   = Toplam ürün exergy [kW] / Toplam yakıt exergy [kW]

Avantaj: Exergy-bazlı EnPI, gerçek termodinamik kayıpları gösterir.
Örneğin: Bir kazan %92 enerji verimine sahip olabilir ancak exergy verimi
yalnızca %35-45 olabilir — fark, yanma irreversibilitesinden kaynaklanır.
```

## 7. İlgili Dosyalar

- [Enerji Yönetimi Bilgi Tabanı İndeks](INDEX.md) — Energy management navigasyon haritası
- [ISO 50001 Uygulama Rehberi](iso_50001_implementation.md) — Gap analizi, sertifikasyon yol haritası, bütçe planlama
- [Enerji İnceleme](energy_review.md) — Madde 6.3 detayları, SEU belirleme, Pareto analizi
- [Baseline ve EnPI](baseline_enpi.md) — Madde 6.4 ve 6.5 detayları, regresyon modeli
- [Sürekli İyileştirme](continuous_improvement.md) — Madde 10 detayları, PDCA ileri uygulamaları
- [Türkiye Mevzuatı](turkey_legislation.md) — 5627 sayılı Kanun, YEGM zorunlulukları
- [Enerji Yönetimi (genel)](../energy_management.md) — Genel bakış ve operasyonel kontroller

## 8. Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50003:2021, "Requirements for bodies providing audit and certification of energy management systems"
- ISO 50004:2020, "Guidance for the implementation, maintenance and improvement of an ISO 50001 energy management system"
- ISO 50006:2014, "Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI)"
- ISO 50015:2014, "Measurement and verification of energy performance of organizations"
- Annex SL (ISO/IEC Directives Part 1, Appendix 2), "Proposals for management system standards"
- CEN/CLC JTC 14, "Energy Management and Energy Audits"
- UNIDO, "Practical Guide for Implementing an Energy Management System"
- US DOE, "50001 Ready Navigator" ve "Superior Energy Performance (SEP) Program"
- Bejan, A. (2006), "Advanced Engineering Thermodynamics" — Exergy ve 2. yasa analizi
- Tsatsaronis, G. (1993), "Thermoeconomic analysis and optimization of energy systems" — Exergy-bazlı performans göstergeleri
