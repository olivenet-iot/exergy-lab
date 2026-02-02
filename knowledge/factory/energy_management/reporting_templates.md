---
title: "Enerji Yönetimi Rapor Şablonları (Energy Management Reporting Templates)"
category: factory
equipment_type: factory
keywords: [rapor şablonu, yönetim raporu, EnPI raporu, M&V raporu, YEGM raporu, enerji denetim raporu, yıllık enerji raporu]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/iso_50001_overview.md, factory/energy_management/enpi_guide.md, factory/energy_management/mv_planning.md, factory/energy_management/turkey_legislation.md, factory/reporting.md]
use_when: ["Enerji raporu hazırlanacağında", "Yönetime sunum yapılacağında", "YEGM raporlaması gerektiğinde", "M&V raporu yazılacağında"]
priority: medium
last_updated: 2026-02-01
---

# Enerji Yönetimi Rapor Şablonları (Energy Management Reporting Templates)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

Enerji yönetim sistemi (EnMS — Energy Management System) kapsamında raporlama, hem performans takibinin hem de yasal uyumluluğun temel aracıdır. ISO 50001:2018 Madde 9 (Performans Değerlendirme) ve Madde 7.4 (İletişim) gereksinimleri doğrultusunda, farklı hedef kitlelere yönelik raporlar hazırlanmalıdır.

### 1.1 Raporlama Türleri

| Rapor Türü | Hedef Kitle | Sıklık | Kapsam |
|------------|-------------|--------|--------|
| Yönetim Raporu (Executive Report) | Üst yönetim, yönetim kurulu | Aylık / Çeyreklik | Özet göstergeler, maliyet, stratejik kararlar |
| EnPI Performans Raporu | Enerji ekibi, teknik yönetim | Aylık | Detaylı EnPI trend, CUSUM, sapma analizi |
| M&V Raporu | Proje paydaşları, ESCO | Çeyreklik / Yıllık | Tasarruf doğrulama, baseline karşılaştırma |
| Enerji Denetim Raporu | Tüm paydaşlar, yasal makam | Proje bazlı | Tesis profili, bulgular, öneriler, finansal analiz |
| YEGM Yıllık Enerji Raporu | YEGM / ENVER | Yıllık (zorunlu) | Tüketim, üretim, SEC, iyileştirme projeleri |
| Operasyonel Rapor | Operatörler, vardiya amirleri | Haftalık / Günlük | SEU bazında performans, alarm, aksiyon |

### 1.2 Hedef Kitle Bazlı Raporlama İlkeleri

```
Üst Yönetim:
├── Maksimum 3-5 sayfa
├── Görsel ağırlıklı (grafik, trafik ışığı)
├── Finansal etki vurgusu (TL/€ tasarruf, ROI)
├── Stratejik kararlar ve aksiyon önerileri
└── Exergy Sankey ile termodinamik özet

Teknik Ekip:
├── 10-20 sayfa detaylı analiz
├── EnPI trend grafikleri (12-24 ay)
├── CUSUM ve regresyon analizi
├── Sapma kök neden analizi
├── Ekipman bazında exergy verim karşılaştırma
└── ECM ilerleme takibi

Yasal Makam (YEGM):
├── ENVER portal formatına uyumlu
├── Kaynak bazında tüketim tablosu (TEP)
├── Üretim verileri ve SEC hesaplama
├── İyileştirme projeleri ve tasarruf beyanı
└── Enerji yöneticisi onayı
```

## 2. Yönetim Raporu Şablonu (Executive Report Template)

Aylık veya çeyreklik dönemlerde üst yönetime sunulan özet rapor şablonu aşağıda verilmiştir.

### 2.1 Şablon Yapısı

| Bölüm No | Bölüm Adı | İçerik | Sayfa |
|-----------|-----------|--------|-------|
| 0 | Başlık Sayfası | Tesis adı, dönem, hazırlayan, onaylayan, tarih | 1 |
| 1 | Yönetici Özeti | 3-5 cümle dönem değerlendirmesi, trafik ışığı gösterge | 1 |
| 2 | Temel Göstergeler (EnPI Özet) | 3-5 EnPI hedef vs gerçek karşılaştırma | 1 |
| 3 | Enerji Maliyet Analizi | Toplam maliyet, kaynak bazında dağılım, önceki dönem karşılaştırma | 0.5 |
| 4 | Performans Karşılaştırma | EnPI trend (6-12 ay), CUSUM özet, benchmark | 1 |
| 5 | Önemli Olaylar | Arıza, kapasite değişimi, proje tamamlama | 0.5 |
| 6 | ECM / Proje İlerleme | Aktif projeler, %tamamlanma, beklenen tasarruf | 0.5 |
| 7 | Aksiyon Listesi | Sorumlu, termin, durum (açık/kapalı) | 0.5 |
| 8 | Sonraki Dönem Planı | Planlanan aksiyonlar, bütçe ihtiyacı | 0.5 |

### 2.2 Bölüm 2 — Temel Göstergeler Tablo Formatı

| Gösterge (EnPI) | Birim | Hedef | Gerçek | Sapma | Durum |
|-----------------|-------|-------|--------|-------|-------|
| Fabrika SEC | kWh/ton | 420 | 435 | +3.6% | Kırmızı |
| Buhar sistemi verimi | % | 82 | 84 | -2.4% | Yeşil |
| Basınçlı hava SPC | kW/(m³/min) | 6.8 | 6.9 | +1.5% | Sarı |
| Soğutma COP | — | 5.2 | 5.0 | +3.8% | Sarı |
| Fabrika exergy verimi | % | 38 | 36.5 | -3.9% | Kırmızı |

```
Trafik ışığı kriterleri:
├── Yeşil  : Hedefte veya daha iyi (sapma ≤ %2)
├── Sarı   : Hafif sapma (%2 < sapma ≤ %5)
├── Kırmızı: Önemli sapma (sapma > %5) → Aksiyon gerekli
└── Mavi   : Veri yok veya dönem dışı
```

### 2.3 Bölüm 3 — Maliyet Analizi Tablo Formatı

| Enerji Kaynağı | Tüketim | Birim | Maliyet (TL) | Pay (%) | Önceki Dönem (TL) | Değişim (%) |
|----------------|---------|-------|-------------|---------|-------------------|-------------|
| Elektrik | 1,250 | MWh | 3,125,000 | 52 | 2,980,000 | +4.9 |
| Doğalgaz | 850 | 1000 Sm³ | 2,380,000 | 40 | 2,210,000 | +7.7 |
| Motorin | 12 | ton | 480,000 | 8 | 460,000 | +4.3 |
| **Toplam** | — | — | **5,985,000** | **100** | **5,650,000** | **+5.9** |

## 3. EnPI Performans Raporu Şablonu (EnPI Performance Report Template)

### 3.1 Aylık EnPI İzleme Raporu Yapısı

| Bölüm | İçerik |
|--------|--------|
| A | EnPI Özet Tablosu (tüm göstergeler, 12 aylık trend) |
| B | Grafik: EnPI Trend (çizgi grafik, hedef çizgisi ile) |
| C | CUSUM Grafik ve Yorumu |
| D | Sapma Analizi (hedeften sapan EnPI'lar için kök neden) |
| E | Düzeltici Aksiyon Takibi |
| F | Exergy Verim Trendi (ExergyLab entegrasyonu) |

### 3.2 EnPI Trend Tablosu Formatı

| EnPI | Birim | Oca | Şub | Mar | Nis | May | Haz | Tem | Ağu | Eyl | Eki | Kas | Ara | Ort. | Hedef |
|------|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|-------|
| SEC | kWh/ton | 430 | 425 | 440 | 435 | 432 | 445 | 450 | 448 | 438 | 430 | 428 | 420 | 435 | 420 |
| η_ex | % | 37.2 | 37.5 | 36.8 | 37.0 | 37.1 | 36.2 | 35.8 | 36.0 | 36.9 | 37.3 | 37.4 | 37.8 | 36.9 | 38.0 |

### 3.3 CUSUM Grafik Açıklaması

```
CUSUM (Cumulative Sum) Analizi:
────────────────────────────────
CUSUM_t = Σ(E_gerçek_i − E_model_i)  [i = 1, ..., t]

Yorum kuralları:
├── Düşen eğim → Performans iyileşmesi (gerçek < model)
├── Yükselen eğim → Performans bozulması (gerçek > model)
├── Yatay seyir → Sabit performans
├── Kırılma noktası → ECM etkisi veya sistem değişikliği
└── Sapma > 2σ → İstatistiksel olarak anlamlı değişim

Örnek CUSUM yorumu:
  Ocak-Haziran: Yatay → Baseline dönemi ile uyumlu
  Temmuz: Kırılma → VSD retrofit devreye alındı
  Ağustos-Aralık: Düşen eğim → Aylık ortalama 15 MWh tasarruf
  Toplam CUSUM = −75 MWh → 6 ayda 75 MWh doğrulanmış tasarruf
```

### 3.4 Sapma Analizi Şablonu

| EnPI | Sapma | Kök Neden | Kanıt | Düzeltici Aksiyon | Sorumlu | Termin |
|------|-------|-----------|-------|-------------------|---------|--------|
| SEC | +3.6% | Kompresör 2 arızası → yedek devreye girdi (düşük verimli) | Bakım kaydı #2847 | Kompresör 2 bakımı + verim testi | Bakım Md. | 15.03 |
| η_ex | -3.9% | Kazan baca sıcaklığı yükseldi (fouling) | Baca T: 245°C (hedef: 180°C) | Ekonomizer temizliği | Üretim Md. | 28.02 |

## 4. M&V Raporu Şablonu (M&V Report Template)

IPMVP uyumlu M&V rapor yapısı, 12 bölümden oluşur.

### 4.1 M&V Rapor Yapısı (12 Bölüm)

| Bölüm No | Başlık | İçerik Özeti |
|-----------|--------|-------------|
| 1 | Yönetici Özeti | Proje tanımı, doğrulanmış tasarruf, sonuç |
| 2 | Proje Tanımı | ECM açıklaması, kapsam, seçilen IPMVP opsiyonu |
| 3 | Ölçüm Sınırı | Fiziksel sınırlar, dahil/hariç ekipman |
| 4 | Temel Dönem Özeti | Baseline dönemi, veri kaynakları, ilgili değişkenler |
| 5 | Baseline Modeli | Regresyon denklemi, R², CV-RMSE, NMBE, grafik |
| 6 | Raporlama Dönemi Verileri | Gerçek tüketim, üretim, iklim verileri |
| 7 | Rutin Düzeltmeler | Üretim/iklim normalizasyonu hesaplama |
| 8 | Rutin Dışı Düzeltmeler | Statik faktör değişiklikleri ve etkileri |
| 9 | Normalleştirilmiş Tasarruf | Tasarruf = Baseline_ayarlanmış − Raporlama |
| 10 | Belirsizlik Analizi | Fractional savings uncertainty (FSU), güven aralığı |
| 11 | Grafik ve Görseller | Baseline vs gerçek, CUSUM, scatter plot |
| 12 | Sonuç ve Öneriler | Doğrulanmış tasarruf beyanı, sonraki adımlar |

### 4.2 Bölüm 9 — Normalleştirilmiş Tasarruf Hesaplama Örneği

```
Proje: Soğutma sistemi VSD retrofit
Opsiyon: IPMVP Opsiyon C (Tesis geneli)
Baseline modeli: E = 180 + 3.2 × Üretim + 1.8 × CDD  [MWh/ay]

Raporlama dönemi (Temmuz):
  Üretim = 300 ton
  CDD = 180 °C·gün
  E_gerçek = 1,250 MWh

Normalleştirilmiş baseline:
  E_baseline_ayar = 180 + 3.2 × 300 + 1.8 × 180
                  = 180 + 960 + 324
                  = 1,464 MWh

Tasarruf:
  ΔE = 1,464 − 1,250 = 214 MWh (%14.6)

Belirsizlik (FSU @ %90 güven):
  FSU = t × CV-RMSE / √n × √(1 + 1/n) / (ΔE/E_baseline)
  FSU ≈ ±%18 → Tasarruf = 214 ± 39 MWh

Sonuç: %90 güven düzeyinde 175-253 MWh/ay arası tasarruf doğrulandı.
```

## 5. Enerji Denetim Raporu Şablonu (Energy Audit Report Template)

ISO 50002:2014 ve EN 16247 serisi uyumlu enerji denetim raporu yapısı.

### 5.1 Denetim Raporu Bölümleri

| Bölüm | Başlık | Detay |
|-------|--------|-------|
| 0 | Başlık ve İçindekiler | Tesis, denetçi bilgileri, tarih, standart referans |
| 1 | Yönetici Özeti | 2-3 sayfa bulgular, toplam tasarruf potansiyeli, öncelikli öneriler |
| 2 | Tesis Profili | Lokasyon, sektör, ürün, kapasite, çalışma düzeni, bina bilgileri |
| 3 | Enerji Profili | Kaynak bazında tüketim (3 yıl), maliyet, Pareto, Sankey |
| 4 | SEU Analizi | Her SEU: tüketim payı, ekipman listesi, çalışma koşulları, exergy verimi |
| 5 | Bulgular (F-XX) | F-01, F-02, ... formatında; açıklama, kanıt, etki, referans fotoğraf |
| 6 | Öneriler (R-XX) | R-01, R-02, ... formatında; ECM tanımı, tasarruf, yatırım, ROI, öncelik |
| 7 | Finansal Özet | Tüm önerilerin toplam tasarruf, yatırım, basit geri ödeme, IRR |
| 8 | Uygulama Planı | Gantt diyagramı, kısa/orta/uzun vade sınıflandırma |
| 9 | Ekler | Ölçüm verileri, hesaplama detayları, kalibrasyon sertifikaları |

### 5.2 Bulgu Formatı (F-XX)

```
F-03: Kazan Baca Gazı Sıcaklığı Yüksek
═══════════════════════════════════════
Konum       : Kazan Dairesi — Kazan #2 (10 ton/h, doğalgaz)
Tespit      : Baca gazı çıkış sıcaklığı 248°C (hedef: <180°C)
Kanıt       : Baca gazı analizörü ölçümü (Ek-3, Sayfa 12)
Enerji etkisi: ~85 kW termal kayıp (baca gazı exergy kaybı: 62 kW)
Referans    : EN 12952, kazan best practice kılavuzu
İlişkili ECM: R-03 (ekonomizer ekleme)
```

### 5.3 Öneri Formatı (R-XX)

| Alan | Değer |
|------|-------|
| Kod | R-03 |
| Başlık | Kazan #2'ye kondensing ekonomizer eklenmesi |
| Açıklama | Baca gazı sıcaklığını 248°C → 65°C'ye düşürerek ısı geri kazanımı |
| Yıllık enerji tasarrufu | 680 MWh_th (72 TEP) |
| Yıllık exergy tasarrufu | 498 MWh_ex |
| Yıllık maliyet tasarrufu | 190,000 TL |
| Yatırım maliyeti | 320,000 TL |
| Basit geri ödeme | 1.7 yıl |
| Öncelik | Yüksek |
| Uygulama süresi | 3 ay |

## 6. YEGM Yıllık Enerji Raporu (YEGM Annual Energy Report)

5627 sayılı Enerji Verimliliği Kanunu ve ilgili yönetmelik kapsamında, yılda 1.000 TEP ve üzeri enerji tüketen sanayi tesisleri ENVER portalı üzerinden yıllık enerji raporu sunmak zorundadır.

### 6.1 Zorunlu Alanlar ve Format

| Bölüm | Zorunlu Alan | Açıklama |
|-------|-------------|----------|
| A — Tesis Bilgileri | Tesis adı, NACE kodu, adres, enerji yöneticisi TC kimlik | YEGM kayıt bilgileri ile tutarlı olmalı |
| B — Enerji Tüketim | Kaynak bazında yıllık tüketim (kWh, Sm³, ton, TEP) | Doğalgaz, elektrik, kömür, motorin, LPG, buhar, vb. |
| C — Üretim Verileri | Ürün bazında yıllık üretim miktarı (ton, adet, m², vb.) | Ana ürün ve yan ürünler |
| D — SEC Hesaplama | TEP/ton (veya uygun birim) | B/C oranı, yıllar arası karşılaştırma |
| E — İyileştirme Projeleri | Tamamlanan ve planlanan ECM'ler | Tasarruf miktarı (TEP), yatırım (TL) |
| F — Enerji Yöneticisi | Ad-soyad, YEGM sertifika no, imza | Aktif sertifika zorunlu |

### 6.2 ENVER Portal Tüketim Tablosu Formatı

| Enerji Kaynağı | Birim | Yıllık Tüketim | Çevrim Faktörü | TEP Eşdeğeri | Pay (%) |
|----------------|-------|----------------|----------------|-------------|---------|
| Doğalgaz | 1000 Sm³ | 3,200 | 0.858 TEP/1000 Sm³ | 2,746 | 58.5 |
| Elektrik | MWh | 12,500 | 0.086 TEP/MWh | 1,075 | 22.9 |
| Kömür (ithal) | ton | 1,800 | 0.450 TEP/ton | 810 | 17.3 |
| Motorin | ton | 55 | 1.015 TEP/ton | 56 | 1.2 |
| LPG | ton | 3 | 1.085 TEP/ton | 3 | 0.1 |
| **Toplam** | — | — | — | **4,690** | **100** |

### 6.3 SEC Hesaplama ve Trend

```
SEC hesaplama:
  SEC = Toplam enerji tüketimi [TEP] / Toplam üretim [ton]

Örnek:
  Toplam tüketim: 4,690 TEP
  Toplam üretim: 28,000 ton ürün
  SEC = 4,690 / 28,000 = 0.1675 TEP/ton

3 yıllık trend:
  2023: 0.178 TEP/ton
  2024: 0.172 TEP/ton (-%3.4)
  2025: 0.168 TEP/ton (-%2.3)
  → Kümülatif iyileşme: -%5.6 (2 yılda)
```

## 7. Rapor Kalite Kontrol Listesi (Report Quality Checklist)

### 7.1 Teknik Doğruluk Kontrol

| No | Kontrol Maddesi | Evet/Hayır |
|----|----------------|------------|
| 1 | Tüm birimlerin tutarlılığı kontrol edildi mi? (kW, kWh, TEP, TL) | |
| 2 | Toplam değerler alt kalemlerin toplamına eşit mi? | |
| 3 | EnPI hesaplamaları bağımsız olarak doğrulandı mı? | |
| 4 | Baseline modeli R² ≥ 0.75 kriterini karşılıyor mu? | |
| 5 | CUSUM grafiğinde açıklanamayan kırılma var mı? | |
| 6 | Exergy verim değerleri fiziksel olarak anlamlı mı? (0 < η_ex < 1) | |
| 7 | Maliyet hesaplamalarında güncel tarife kullanıldı mı? | |
| 8 | Tasarruf belirsizliği hesaplanıp rapor edildi mi? | |

### 7.2 Format Tutarlılığı Kontrol

| No | Kontrol Maddesi | Evet/Hayır |
|----|----------------|------------|
| 1 | Başlık sayfası standart formata uygun mu? | |
| 2 | Sayfa numaraları ve içindekiler tutarlı mı? | |
| 3 | Grafiklerde eksen etiketleri ve birimler mevcut mu? | |
| 4 | Tablolarda kaynak referansları belirtilmiş mi? | |
| 5 | Tüm kısaltmalar ilk kullanımda açıklanmış mı? | |

### 7.3 Yasal Uyumluluk Kontrol

| No | Kontrol Maddesi | Evet/Hayır |
|----|----------------|------------|
| 1 | ENVER portal formatına uygunluk kontrol edildi mi? | |
| 2 | Enerji yöneticisi sertifikası aktif mi? | |
| 3 | NACE kodu güncel ve doğru mu? | |
| 4 | TEP çevrim faktörleri YEGM güncel tablosuna uygun mu? | |
| 5 | Raporlama takvimi son teslim tarihine uygun mu? | |
| 6 | Enerji denetimi raporu ISO 50002/EN 16247'ye referans veriyor mu? | |

## 8. İlgili Dosyalar

- [Enerji Yönetimi Bilgi Tabanı İndeks](INDEX.md) — Energy management navigasyon haritası
- [ISO 50001 Standart Analizi](iso_50001_overview.md) — Madde bazlı gereksinimler ve raporlama bağlantısı
- [EnPI Rehberi](enpi_guide.md) — Detaylı EnPI tanımlama ve sektörel örnekler
- [Baseline ve EnPI](baseline_enpi.md) — Regresyon modeli ve normalizasyon detayları
- [M&V Plan Hazırlama](mv_planning.md) — M&V planı şablonu ve detaylı çalışılmış örnek
- [Türkiye Mevzuatı](turkey_legislation.md) — 5627 sayılı Kanun, YEGM yükümlülükleri
- [Raporlama (genel)](../reporting.md) — Genel raporlama çerçevesi

## 9. Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use" — Madde 7.4 (İletişim) ve Madde 9 (Performans Değerlendirme)
- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- EN 16247-1:2022, "Energy audits — Part 1: General requirements"
- EVO, "IPMVP Core Concepts 2022," — M&V raporlama gereksinimleri
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings" — Belirsizlik raporlama
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Enerji Kaynaklarının ve Enerjinin Kullanımında Verimliliğin Artırılmasına Dair Yönetmelik"
- YEGM, "ENVER Portalı Kullanım Kılavuzu"
- T.C. Resmi Gazete, 5627 sayılı Enerji Verimliliği Kanunu
- US DOE, "Superior Energy Performance (SEP) Measurement and Verification Protocol"
- UNIDO, "Practical Guide for Implementing an Energy Management System" — Raporlama bölümü
