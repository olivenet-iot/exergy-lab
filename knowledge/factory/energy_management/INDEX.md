---
title: "Enerji Yönetim Sistemi Bilgi Tabanı Indeks (Energy Management System Knowledge Base Index)"
category: factory
equipment_type: factory
keywords: [enerji yönetimi, indeks, navigasyon, ISO 50001, denetim, M&V, mevzuat, EnMS]
related_files: [factory/INDEX.md, factory/energy_management.md]
use_when: ["Enerji yönetim sistemi bilgisine erişim gerektiğinde", "Energy management alt dizininde gezinirken"]
priority: high
last_updated: 2026-02-01
---

# Enerji Yönetim Sistemi Bilgi Tabanı Indeks

> Son güncelleme: 2026-02-01

## Genel Bakış

Bu dizin, endüstriyel tesislerde enerji yönetim sistemi (EnMS — Energy Management System) kurulumu, işletimi ve sürekli iyileştirilmesi için kapsamlı bir bilgi tabanı sunar. Toplam **21 dosya** halinde organize edilen içerik; ISO 50001 standart analizi ve uygulama rehberinden, Türkiye mevzuatı ve teşvik mekanizmalarına, enerji denetim standartlarından ölçüm ve doğrulama (M&V) protokollerine, performans göstergesi (EnPI) tanımlamadan sürekli iyileştirme (Continuous Improvement) metodolojisine kadar geniş bir yelpazede bilgi sağlar. ExergyLab'ın exergy (2. yasa) perspektifi, klasik enerji yönetimi yaklaşımına ek derinlik katarak mevzuat gereksinimlerinin ötesinde gerçek termodinamik kayıpları görünür kılar.

## Dosya Listesi

### ISO 50001 Cerçevesi (ISO 50001 Framework)

| Dosya | Aciklama | Oncelik | Kullanim |
|-------|----------|---------|----------|
| `iso_50001_overview.md` | Madde madde standart analizi, HLS, PDCA, olgunluk modeli | Yuksek | Standart gereksinimleri sorgulandiginda |
| `iso_50001_implementation.md` | Gap analizi, sertifikasyon yol haritasi, butce planlama | Yuksek | EnMS kurulumu projelendirilirken |
| `energy_review.md` | Enerji gozden gecirme, SEU tanimlama, Pareto analizi | Orta | Madde 6.3 detaylari gerektiginde |
| `baseline_enpi.md` | ISO 50006, regresyon modeli, EnB/EnPI olusturma | Yuksek | Baseline ve performans gostergesi tanimlanirken |
| `action_planning.md` | Hedef belirleme, ECM onceliklendirme, eylem planlari | Orta | Madde 6.6 ve iyilestirme plani gerektiginde |

### Denetim Standartlari (Audit Standards)

| Dosya | Aciklama | Oncelik | Kullanim |
|-------|----------|---------|----------|
| `audit_methodology.md` | Pratik saha denetim rehberi, checklist'ler, olcum plani | Orta | Enerji denetimi uygulanirken |
| `audit_levels.md` | ASHRAE Level I/II/III detay, Turkiye eslestirmesi | Orta | Denetim seviyesi secimi yapilirken |
| `iso_50002.md` | ISO 50002:2014 madde analizi, denetim sureci | Dusuk | ISO bazli denetim standardi gerektiginde |
| `en_16247.md` | EN 16247 serisi (5 part), AB EED uyum karsilastirmasi | Dusuk | Avrupa denetim standardi referansi gerektiginde |

### Olcum ve Dogrulama — M&V (Measurement & Verification)

| Dosya | Aciklama | Oncelik | Kullanim |
|-------|----------|---------|----------|
| `mv_ipmvp.md` | IPMVP cerceve, Option A-D, ESCO, dijital M&V | Yuksek | Tasarruf dogrulamasi planlanirken |
| `mv_planning.md` | M&V plan sablonu, tam ornek, belirsizlik hesabi | Orta | M&V plani olusturulurken |
| `mv_statistics.md` | Regresyon analizi, ASHRAE Guideline 14, CV-RMSE | Orta | Istatistiksel dogrulama yapilirken |

### Uygulamali Rehberler (Applied Guides)

| Dosya | Aciklama | Oncelik | Kullanim |
|-------|----------|---------|----------|
| `turkey_legislation.md` | 5627 sayili Kanun, YEGM, TEP hesaplama, zorunluluklar | Yuksek | Turkiye mevzuati sorgulandiginda |
| `turkey_incentives.md` | VAP, EPC, beyaz sertifika, ESCO modelleri, fonlama | Orta | Tesvik ve destekler arastirilirken |
| `enpi_guide.md` | ISO 50006 derinlesme, EnPI turleri, exergy-EnPI | Yuksek | Performans gostergesi tanimlanirken |
| `cusum_analysis.md` | CUSUM hesaplama, yorumlama, sapma tespiti | Orta | Performans trend analizi yapilirken |
| `monitoring_targeting.md` | M&T sistemi, dashboard tasarimi, SCADA entegrasyonu | Orta | Izleme altyapisi planlanirken |

### Sentez ve Iyilestirme (Synthesis & Improvement)

| Dosya | Aciklama | Oncelik | Kullanim |
|-------|----------|---------|----------|
| `reporting_templates.md` | Rapor sablonlari (yonetim, EnPI, M&V, YEGM) | Dusuk | Raporlama formati gerektiginde |
| `continuous_improvement.md` | PDCA detay, ic denetim, olgunluk modeli gecisi | Orta | Surekli iyilestirme mekanizmasi kurulurken |
| `case_studies.md` | 5 vaka calismasi (tekstil, gida, cimento, kimya, metal) | Dusuk | Referans ornek aradiginda |

## Navigasyon Kurallari

### ISO 50001 Danismanligi
1. `iso_50001_overview.md` — Standart genel yapisi ve olgunluk modeli
2. `iso_50001_implementation.md` — Uygulama yol haritasi ve gap analizi
3. `energy_review.md` — Enerji gozden gecirme sureci
4. `baseline_enpi.md` — EnB ve EnPI olusturma
5. `action_planning.md` — Eylem plani ve hedef belirleme

### Enerji Denetimi
1. `audit_levels.md` — Denetim seviyesi secimi
2. `audit_methodology.md` — Saha denetim rehberi
3. `iso_50002.md` veya `en_16247.md` — Standart uyumu

### M&V Uygulamasi
1. `mv_ipmvp.md` — Protokol secimi
2. `mv_planning.md` — M&V plani olusturma
3. `mv_statistics.md` — Istatistiksel analiz

### Turkiye Mevzuati
1. `turkey_legislation.md` — Yasal zorunluluklar
2. `turkey_incentives.md` — Tesvik ve destekler

### Performans Izleme
1. `enpi_guide.md` — EnPI tanimlama ve izleme
2. `cusum_analysis.md` — CUSUM ile performans analizi
3. `monitoring_targeting.md` — M&T sistemi tasarimi

## Mevcut Dosyalarla Iliski

| Bu Dizin | Mevcut Dosya | Iliski |
|----------|-------------|--------|
| `iso_50001_overview.md` | `../energy_management.md` | Derinlestirme (madde analizi + olgunluk modeli) |
| `mv_ipmvp.md` | `../measurement_verification.md` | Protokol secimi odakli; formuller mevcut dosyada |
| `audit_methodology.md` | `../methodology.md` | Pratik checklist; teori mevcut dosyada |
| `baseline_enpi.md` | `../kpi_definitions.md` | ISO 50006 derinlesme; genel KPI tanimlari mevcut dosyada |
| `enpi_guide.md` | `../performance_indicators.md` | EnPI odakli; genel gostergeler mevcut dosyada |

## İlgili Dosyalar

- [Fabrika Indeks](../INDEX.md) — Ust dizin navigasyon haritasi
- [Enerji Yonetimi (genel)](../energy_management.md) — Genel bakis ve PDCA
- [Olcum ve Dogrulama](../measurement_verification.md) — IPMVP formul detaylari
- [Metodoloji](../methodology.md) — Audit teorik cercevesi

## Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- ISO 50006:2014, "Measuring energy performance using EnB and EnPI"
- EN 16247-1:2022 serisi (Parts 1-5)
- IPMVP 2022, "International Performance Measurement and Verification Protocol"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- 5627 sayili Enerji Verimliligi Kanunu (2007, degisikliklerle)
- YEGM, "Enerji Yoneticisi Egitim Programi Mufredati"
