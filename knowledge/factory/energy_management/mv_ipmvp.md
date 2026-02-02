---
title: "IPMVP Ölçüm ve Doğrulama Çerçevesi (IPMVP Measurement and Verification Framework)"
category: factory
equipment_type: factory
keywords: [IPMVP, M&V, ölçüm ve doğrulama, ESCO, EPC, opsiyon seçimi, dijital M&V, AMMV, otomatik M&V]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/mv_planning.md, factory/energy_management/mv_statistics.md, factory/measurement_verification.md, factory/energy_management/turkey_incentives.md, factory/economic_analysis.md]
use_when: ["M&V protokolü seçilecekken", "ESCO/EPC projesi değerlendirilirken", "Dijital M&V sorgulandığında"]
priority: high
last_updated: 2026-02-01
---

# IPMVP Ölçüm ve Doğrulama Çerçevesi (IPMVP Measurement and Verification Framework)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

IPMVP (International Performance Measurement and Verification Protocol), enerji verimliliği projelerinde (Energy Conservation Measures — ECM) elde edilen tasarrufların bağımsız, tekrarlanabilir ve güvenilir bir şekilde ölçülüp doğrulanması için uluslararası kabul görmüş protokoldür. EVO (Efficiency Valuation Organization) tarafından yayımlanan ve sürdürülen protokolün güncel sürümü **IPMVP Core Concepts 2022**'dir.

### 1.1 IPMVP'nin Temel Amacı

- Tasarrufların "ölçülebilir" ve "doğrulanabilir" olmasını sağlamak
- ESCO (Energy Service Company) sözleşmelerinde taraflar arasında ortak bir dil oluşturmak
- Enerji performans garantilerinin (Energy Performance Contracting — EPC) temelini oluşturmak
- Yatırımcı güvenini artırarak enerji verimliliği finansmanını kolaylaştırmak

### 1.2 Bu Dosyanın Kapsamı ve Mevcut Dosyalarla İlişkisi

Bu dosya, IPMVP çerçevesinin **strateji ve opsiyon seçimi** boyutuna odaklanır. Ayrıntılı formüller, opsiyon karşılaştırma tablosu ve temel hat (baseline) hesaplama formülleri için `factory/measurement_verification.md` dosyasına başvurunuz. İki dosya birbirini tamamlar:

| Bu Dosya (`mv_ipmvp.md`) | Mevcut Dosya (`measurement_verification.md`) |
|---|---|
| Protokol seçim stratejisi | Opsiyon formülleri ve hesaplama |
| ESCO/EPC bağlamı ve risk dağılımı | Baseline ayarlama formülleri |
| Dijital M&V (AMMV) teknolojileri | Rutin dışı düzeltme hesaplamaları |
| Maliyet-fayda analizi | Etkileşim etkileri formülleri |
| Karar ağacı ve rehber | İstatistiksel kriterler (özet) |

### 1.3 IPMVP Temel Kavramlar

- **Tasarruf (Savings):** Doğrudan ölçülemez; baseline ile raporlama dönemi farkından hesaplanır
- **Temel Hat (Baseline):** ECM öncesi enerji tüketim profili
- **Rutin Dışı Düzeltme (Non-routine Adjustment):** Üretim değişikliği, alan değişimi gibi kalıcı etkiler
- **Rutin Düzeltme (Routine Adjustment):** Hava durumu, üretim hacmi gibi döngüsel değişkenler
- **Ölçüm Sınırı (Measurement Boundary):** M&V kapsamına alınan fiziksel alan

```
Temel Tasarruf Formülü:
────────────────────────────────────────────
Tasarruf = (E_baseline,ayarlanmış) − (E_raporlama) ± (Rutin Dışı Düzeltmeler)
────────────────────────────────────────────
```

## 2. Opsiyon Seçim Rehberi (Option Selection Guide)

### 2.1 ECM Tipi × Uygun Opsiyon Matrisi (ECM Type × Suitable Option Matrix)

Aşağıdaki matris, yaygın ECM türlerinin hangi IPMVP opsiyonlarıyla en uyumlu olduğunu gösterir:

| ECM Tipi | Opsiyon A | Opsiyon B | Opsiyon C | Opsiyon D |
|---|:---:|:---:|:---:|:---:|
| VSD (Variable Speed Drive) retrofit | ★★ | ★★★ | ★ | ★ |
| Aydınlatma dönüşümü (LED retrofit) | ★★★ | ★★ | ★ | — |
| Kazan ekonomizer ekleme | ★★ | ★★★ | ★ | ★ |
| Bina yalıtımı | — | ★ | ★★★ | ★★ |
| Chiller değişimi | ★ | ★★★ | ★★ | ★ |
| Kompresör sistemi optimizasyonu | ★★ | ★★★ | ★ | — |
| Çoklu ECM (multi-measure) paketi | — | — | ★★★ | ★★ |
| Yeni bina tasarımı | — | — | — | ★★★ |
| Isı geri kazanımı (Heat Recovery) | ★★ | ★★★ | ★ | ★ |
| Buharlı kazan blowdown geri kazanımı | ★★★ | ★★ | ★ | — |

> ★★★: En uygun, ★★: Uygun, ★: Koşullu uygun, —: Uygunsuz

### 2.2 Karar Kuralları (Decision Rules)

Opsiyon seçiminde üç temel kriter değerlendirilir:

**Kriter 1 — İzolasyon Kolaylığı (Isolation Feasibility)**
- ECM etkisi tek bir ekipmana yalıtılabiliyorsa → Opsiyon A veya B
- Etkiler tesis genelinde yayılıyorsa → Opsiyon C veya D

**Kriter 2 — Ölçüm Maliyeti vs. Tasarruf Büyüklüğü**
- Beklenen yıllık tasarruf < 50.000 TL → Düşük maliyetli opsiyon tercih et (A veya C)
- Beklenen yıllık tasarruf > 500.000 TL → Yüksek doğruluk opsiyonu haklı (B)
- M&V maliyeti, proje ömrü boyunca tasarrufun %3-10'u arasında olmalı

**Kriter 3 — Etkileşim Düzeyi (Interaction Level)**
- Tek ECM, etkileşim yok → A veya B
- Birden fazla ECM, düşük etkileşim → Ayrı ayrı A/B + toplam C doğrulaması
- Yoğun etkileşim → C veya D

### 2.3 Karar Akış Şeması (Decision Flowchart)

```
IPMVP Opsiyon Seçim Karar Ağacı
═════════════════════════════════

[1] ECM tek ekipmana yalıtılabilir mi?
    │
    ├── EVET ──→ [2] Sürekli ölçüm bütçesi var mı?
    │               │
    │               ├── EVET ──→ [3] Performans garantisi gerekli mi?
    │               │               │
    │               │               ├── EVET ──→ OPSİYON B
    │               │               └── HAYIR ─→ OPSİYON A
    │               │
    │               └── HAYIR ─→ OPSİYON A (anahtar parametre)
    │
    └── HAYIR ─→ [4] Kalibre simülasyon modeli mevcut mu?
                    │
                    ├── EVET ──→ [5] Yeni bina veya karmaşık sistem mi?
                    │               │
                    │               ├── EVET ──→ OPSİYON D
                    │               └── HAYIR ─→ OPSİYON C
                    │
                    └── HAYIR ─→ OPSİYON C (tesis geneli)
```

## 3. ESCO ve EPC Bağlamı (ESCO and EPC Context)

### 3.1 Energy Performance Contracting (EPC) Tanımı

EPC (Enerji Performans Sözleşmesi), bir ESCO'nun müşteri tesisinde enerji verimliliği iyileştirmeleri gerçekleştirdiği, maliyeti elde edilen tasarruflardan geri ödenen sözleşme modelidir. M&V, bu sözleşmelerin **omurgasıdır** — çünkü ödeme, doğrulanmış tasarrufa bağlıdır.

### 3.2 Sözleşme Modelleri ve Risk Dağılımı

| Model | Tanım | M&V Rolü | Risk Dağılımı |
|---|---|---|---|
| Garantili Tasarruf (Guaranteed Savings) | ESCO minimum tasarrufu garanti eder | M&V ile garanti doğrulanır | Performans riski: ESCO; Finans riski: Müşteri |
| Paylaşımlı Tasarruf (Shared Savings) | Doğrulanan tasarruf taraflar arasında paylaşılır | M&V paylaşım oranını belirler | Her iki risk: ESCO (büyük pay) |
| Chauffage (Enerji Tedarik) | ESCO tesisin enerji yönetimini üstlenir | Baseline'dan sapma takibi | Operasyonel risk: ESCO |
| Hibrit Model | Garanti + paylaşım kombinasyonu | Katmanlı M&V gerektirir | Paylaşımlı risk |

### 3.3 Türkiye'de ESCO Pazarı

Türkiye'de ESCO pazarı gelişmekte olup önemli dinamikler şunlardır:

- **Yasal Çerçeve:** 5627 sayılı Enerji Verimliliği Kanunu ve Enerji Kaynaklarının ve Enerjinin Kullanımında Verimliliğin Artırılmasına Dair Yönetmelik
- **VAP (Verimlilik Artırıcı Proje):** Sanayi tesisleri için devlet desteği mekanizması
- **YEGM (Yenilenebilir Enerji Genel Müdürlüğü):** Denetim ve teşvik sürecinin yönetimi
- **Zorluklar:** Sözleşme hukuku altyapısının yetersizliği, bankabilite sorunları, M&V uzman eksikliği
- **Fırsatlar:** Sanayide yüksek enerji yoğunluğu, artan enerji maliyetleri, AB uyum süreci

### 3.4 EPC Projelerinde M&V Planının Sözleşmedeki Yeri

M&V planı, EPC sözleşmesinin ayrılmaz bir ekidir ve şu unsurları içermelidir:

1. Seçilen IPMVP opsiyonu ve gerekçesi
2. Baseline dönemi tanımı ve verileri
3. Raporlama dönemleri ve sıklığı
4. Bağımsız M&V denetçisi atanması
5. İhtilaf çözüm mekanizması
6. M&V maliyetinin paylaşımı

## 4. Dijital M&V — Otomatik M&V (Automated M&V — AMMV)

### 4.1 Geleneksel vs. Dijital M&V Karşılaştırması

| Özellik | Geleneksel M&V | Dijital M&V (AMMV) |
|---|---|---|
| Model güncelleme | Manuel, yılda 1-2 kez | Otomatik, gerçek zamanlı |
| Veri kaynağı | Fatura + spot ölçüm | IoT sensörleri + BMS + SCADA |
| Model tipi | Doğrusal regresyon | ML modelleri (RF, GBM, LSTM) |
| Rapor sıklığı | Aylık/çeyreklik | Günlük/saatlik |
| Değişken sayısı | 1-3 bağımsız değişken | 10-100+ değişken |
| Rutin dışı düzeltme | Manuel analiz | Otomatik tespit (anomali algılama) |
| Doğruluk (CV-RMSE) | %15-25 (aylık) | %5-15 (saatlik) |
| Maliyet | Yüksek (danışman) | Platform lisansı (ölçeklenebilir) |
| İnsan müdahalesi | Yoğun | Minimal (doğrulama odaklı) |

### 4.2 Makine Öğrenmesi Modelleri (Machine Learning Models)

Dijital M&V'de kullanılan temel ML modelleri:

| Model | Avantaj | Dezavantaj | Kullanım Alanı |
|---|---|---|---|
| Random Forest (RF) | Yüksek doğruluk, overfitting'e dirençli | Düşük yorumlanabilirlik | Endüstriyel tesisler |
| Gradient Boosting (XGBoost, LightGBM) | En yüksek doğruluk, hız | Hiperparametre hassasiyeti | Büyük veri setleri |
| LSTM (Long Short-Term Memory) | Zaman serisi bağımlılığı yakalama | Eğitim süresi uzun, veri ihtiyacı yüksek | Mevsimsel paternler |
| Elastic Net | Şeffaf, yorumlanabilir | Doğrusal olmayan ilişkilerde zayıf | Basit sistemler |
| Ensemble (Topluluk) | Model hatalarını dengelemek | Karmaşıklık | Kritik projeler |

### 4.3 AMMV Avantajları

- **Gerçek Zamanlı İzleme:** Tasarruf sapması anında tespit edilir
- **Düşük Maliyet:** Platform bazlı çözümler ölçek ekonomisi sağlar
- **Yüksek Doğruluk:** ML modelleri ile CV(RMSE) < %15 saatlik bazda
- **Çoklu Değişken:** İklim, üretim, vardiya, tatil gibi tüm etkenler modele dahil
- **Otomatik Raporlama:** Periyodik tasarruf raporları insan müdahalesi olmadan üretilir

### 4.4 Dijital M&V Zorlukları

- **Veri Kalitesi:** Eksik, hatalı veya tutarsız sensör verileri model performansını düşürür
- **Model Şeffaflığı (Interpretability):** "Kara kutu" modeller sözleşme ihtilaflarında sorun yaratabilir
- **Standardizasyon Eksikliği:** IPMVP'de AMMV henüz tam olarak kodifiye edilmemiştir
- **Siber Güvenlik:** IoT altyapısının güvenlik riskleri
- **Uzman İhtiyacı:** Veri bilimi + enerji mühendisliği kavşağında uzman gereksinimi

### 4.5 Dijital M&V Yazılım Araçları

| Araç | Geliştirici | Model Tipi | Özellik |
|---|---|---|---|
| OpenEEmeter | CalTRACK | Açık kaynak regresyon | ABD düzenleyici uyumlu |
| LBNL NMEC Toolkit | Lawrence Berkeley Lab | İstatistiksel | Araştırma odaklı |
| EnergyRM | EnergyRM Inc. | Hibrit ML | Ticari platform |
| Gridium | Gridium | GBM/RF | Bina odaklı |
| dEXA Platform (ExergyLab) | ExergyLab | Exergy-bazlı ML | 2. yasa entegrasyonu |

## 5. M&V Maliyet-Fayda Analizi (M&V Cost-Benefit Analysis)

### 5.1 M&V Maliyeti Kılavuzu

M&V maliyeti, projenin ömrü boyunca beklenen tasarrufun belirli bir yüzdesidir:

| Proje Büyüklüğü (Yıllık Tasarruf) | M&V Maliyet Oranı | Açıklama |
|---|---|---|
| < 100.000 TL/yıl | %5-10 | Basit opsiyon (A veya C) tercih edilmeli |
| 100.000 — 500.000 TL/yıl | %3-7 | Standart M&V planı |
| 500.000 — 2.000.000 TL/yıl | %3-5 | Detaylı M&V (Opsiyon B) haklı olabilir |
| > 2.000.000 TL/yıl | %2-4 | Sürekli ölçüm ve bağımsız denetçi |

### 5.2 Opsiyon Bazlı Maliyet Karşılaştırma

```
Opsiyon Bazlı Yaklaşık M&V Maliyetleri (endüstriyel tesis):
══════════════════════════════════════════════════════════════
Opsiyon A: 15.000 — 50.000 TL/ECM (bir kerelik + yıllık rapor)
Opsiyon B: 30.000 — 150.000 TL/ECM (sürekli ölçüm sistemi dahil)
Opsiyon C: 25.000 — 100.000 TL/tesis (fatura analizi + regresyon)
Opsiyon D: 80.000 — 300.000 TL/tesis (simülasyon modeli geliştirme)
AMMV:      20.000 — 80.000 TL/yıl (platform lisansı + kurulum)
══════════════════════════════════════════════════════════════
```

### 5.3 Maliyet Optimizasyonu Stratejileri

1. **Mevcut Altyapı Kullanımı:** BMS/SCADA verilerini M&V'ye entegre et
2. **Örnekleme (Sampling):** Aynı tipte çok sayıda ECM varsa istatistiksel örnekleme uygula
3. **Hibrit Yaklaşım:** Büyük ECM'lere Opsiyon B, küçüklere Opsiyon A uygula
4. **Dijital M&V Geçişi:** Uzun vadeli projelerde AMMV platform maliyeti düşer
5. **Grup M&V:** Aynı sektörde birden fazla tesis için ortak M&V planı

## 6. ExergyLab ile M&V Entegrasyonu (ExergyLab M&V Integration)

### 6.1 Exergy Bazlı Tasarruf Doğrulaması

Geleneksel M&V yalnızca enerji (1. yasa) tasarrufunu doğrular. ExergyLab, **exergy (2. yasa) bazlı tasarruf doğrulaması** sağlar:

```
Enerji Tasarrufu (1. Yasa):
  ΔE = E_baseline − E_raporlama

Exergy Tasarrufu (2. Yasa):
  ΔEx = Ex_baseline − Ex_raporlama

Exergy İyileştirme Oranı:
  η_ex,iyileştirme = (ψ_raporlama − ψ_baseline) / ψ_baseline × 100  [%]
```

Exergy bazlı M&V, özellikle **ısıl sistemlerde** (kazan, chiller, ısı geri kazanımı) gerçek termodinamik iyileşmeyi gösterir. Örneğin, bir ekonomizer ekleme projesi enerji bazında %5 tasarruf sağlarken, exergy bazında %12 iyileşme gösterebilir — çünkü baca gazı exergy'sinin geri kazanılması termodinamik kaliteyi artırır.

### 6.2 Platform Desteği

ExergyLab platformunun M&V sürecine katkıları:

| Süreç Adımı | ExergyLab Desteği |
|---|---|
| Baseline oluşturma | Ekipman bazlı exergy baseline hesaplama |
| Raporlama dönemi | Gerçek zamanlı exergy verimi izleme |
| Sapma tespiti | Exergy kaybı anomali algılama |
| Raporlama | Otomatik exergy M&V raporu |
| Önceliklendirme | Exergy kaybı büyüklüğüne göre ECM sıralama |

## 7. İlgili Dosyalar

- [M&V Formül Detayları](../../factory/measurement_verification.md) — IPMVP opsiyon formülleri, baseline ayarlama, rutin dışı düzeltmeler
- [M&V Plan Hazırlama](mv_planning.md) — M&V planı şablonu ve tam çalışılmış örnek
- [M&V İstatistiksel Yöntemler](mv_statistics.md) — Regresyon analizi, ASHRAE Guideline 14, belirsizlik
- [Türkiye Teşvikleri](turkey_incentives.md) — VAP, EPC, ESCO destekleri
- [Ekonomik Analiz](../../factory/economic_analysis.md) — Yatırım geri dönüş hesaplamaları
- [Energy Management INDEX](INDEX.md) — Enerji yönetimi bilgi tabanı ana dizin

## 8. Referanslar (References)

1. EVO (Efficiency Valuation Organization), "IPMVP Core Concepts 2022," EVO 10400-1:2022.
2. ASHRAE, "ASHRAE Guideline 14-2014: Measurement of Energy, Demand, and Water Savings," ASHRAE, 2014.
3. EVO, "IPMVP Application Guide: Automating M&V 2.0," EVO 10400-AG-2, 2021.
4. U.S. DOE, "M&V Guidelines: Measurement and Verification for Performance-Based Contracts," Version 4.0, 2015.
5. ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations."
6. FEMP (Federal Energy Management Program), "M&V Guidelines 4.0," U.S. Department of Energy.
7. T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Enerji Kaynaklarının ve Enerjinin Kullanımında Verimliliğin Artırılmasına Dair Yönetmelik," Resmi Gazete, 2008 (değişikliklerle).
8. Granderson, J., et al., "Automated Measurement and Verification: Performance of Public Domain Whole-Building Electric Baseline Models," Applied Energy, 2017.
9. Gallagher, C.V., et al., "The suitability of machine learning to minimise uncertainty in the measurement and verification of energy savings," Energy and Buildings, 2018.
10. CalTRACK, "CalTRACK Methods 2.0," California Technical Reference for Automated Customer Tracking, 2020.
