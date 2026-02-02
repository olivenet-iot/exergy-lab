---
title: "Türkiye Enerji Verimliliği Teşvikleri ve Finansman (Turkey Energy Efficiency Incentives and Financing)"
category: factory
equipment_type: factory
keywords: [VAP, verimlilik artırıcı proje, EPC, beyaz sertifika, ESCO, KOSGEB, enerji verimliliği teşviki, YEGM, hibe, kredi]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/turkey_legislation.md, factory/energy_management/mv_ipmvp.md, factory/economic_analysis.md, factory/implementation.md]
use_when: ["Türkiye teşvik mekanizmaları sorgulandığında", "VAP başvurusu planlandığında", "ESCO/EPC modeli değerlendirilirken", "Finansman kaynakları araştırılırken"]
priority: high
last_updated: 2026-02-01
---

# Türkiye Enerji Verimliliği Teşvikleri ve Finansman

> Son güncelleme: 2026-02-01

## Genel Bakış

Türkiye'de enerji verimliliği yatırımlarının teşviki; hibe, düşük faizli kredi, vergi avantajı ve performans bazlı sözleşme modelleri olmak üzere çok katmanlı bir ekosistem içinde yürütülmektedir. YEGM (Yenilenebilir Enerji Genel Müdürlüğü), VAP (Verimlilik Artırıcı Proje) programı aracılığıyla doğrudan hibe desteği sunarken, ESCO (Energy Service Company) ve EPC (Energy Performance Contract) modelleri özel sektör finansmanını harekete geçirmektedir. Bu dosya, mevcut teşvik mekanizmalarını, başvuru süreçlerini ve ExergyLab entegrasyon potansiyelini detaylı olarak ele alır.

## 1. Teşvik Ekosistemi Haritası (Incentive Ecosystem Map)

```
Türkiye Enerji Verimliliği Teşvik Ekosistemi:

Kamu Destekleri:
├── YEGM — VAP Hibe Desteği (%20-30)
├── KOSGEB — KOBİ Enerji Verimliliği Desteği
├── Kalkınma Ajansları — Bölgesel Proje Hibeleri
├── TÜBİTAK — Ar-Ge ve İnovasyon Projeleri
└── Vergi Avantajları — Gönüllü Anlaşma Kapsamı

Uluslararası Finansman:
├── EBRD — Enerji Verimliliği Kredi Hatları (TurSEFF, MidSEFF)
├── IFC — Kaynak Verimliliği Finansmanı
├── KfW — Yeşil Ekonomi Finansmanı
├── AFD — Enerji Dönüşümü Programı
└── GCF (Green Climate Fund) — İklim Projeleri

Özel Sektör Modelleri:
├── ESCO — Garantili Tasarruf Modeli
├── EPC — Performans Sözleşmesi
├── Leasing — Verimli Ekipman Kiralanması
└── Beyaz Sertifika — Piyasa Mekanizması (pilot)
```

## 2. VAP (Verimlilik Artırıcı Proje) Desteği

### 2.1 VAP Tanımı

VAP, 5627 sayılı Enerji Verimliliği Kanunu kapsamında, yıllık enerji tüketimi ≥1.000 TEP olan endüstriyel tesislerin enerji verimlilik yatırımlarına sağlanan hibe desteğidir. YEGM tarafından yürütülen VAP programı, Türkiye'nin en önemli doğrudan teşvik mekanizmasıdır.

### 2.2 Başvuru Koşulları

| Koşul | Gereksinim | Detay |
|-------|-----------|-------|
| Tesis türü | Sanayi tesisi | ≥1.000 TEP/yıl tüketim |
| Geri ödeme süresi | ≤5 yıl | Basit geri ödeme hesabı |
| Minimum tasarruf | Anlamlı TEP tasarrufu | Proje bazında değerlendirilir |
| Ölçüm planı | M&V planı gerekli | Tasarrufun doğrulanabilirliği |
| EVD onayı | Yetkilendirilmiş EVD şirketi raporu | Teknik fizibilite |
| Mevzuat uyumu | 5627 zorunlulukları yerine getirilmiş | Enerji yöneticisi, bildirim |

### 2.3 Destek Oranları ve Tutarları

```
VAP destek oranları (2025-2026 güncel):

Standart destek:
├── Destek oranı: Proje bedelinin %20'si
├── Maksimum tutar: 5.000.000 TL (yıllık güncellenir)
└── Ödeme: Uygulama sonrası, M&V doğrulamasıyla

Öncelikli alan desteği:
├── Destek oranı: Proje bedelinin %30'u
├── Öncelikli alanlar:
│   ├── Kojenerasyon / trigeneration
│   ├── Atık ısı geri kazanımı
│   ├── Proses ısı entegrasyonu
│   ├── Yüksek verimli motor ve sürücüler
│   └── Endüstriyel IoT ve enerji izleme
└── Maksimum tutar: 8.000.000 TL (yıllık güncellenir)

Not: Tutarlar her yıl yeniden değerleme oranıyla güncellenir.
VAP bütçesi yıllık bazda belirlenir (sınırlı kaynak).
```

### 2.4 Başvuru Süreci (6 Adım)

```
VAP başvuru süreci:

Adım 1 — Ön Fizibilite (1-2 hafta):
├── Enerji tasarruf fırsatlarının belirlenmesi
├── ExergyLab analizi ile potansiyel tespiti
├── Ön maliyet-fayda hesabı
└── Geri ödeme süresi kontrolü (≤5 yıl)

Adım 2 — Detaylı Fizibilite Raporu (4-6 hafta):
├── EVD şirketi ile çalışma
├── Mevcut durum ölçümleri
├── Tasarruf hesabı (TEP/yıl, TL/yıl)
├── Yatırım maliyeti detayı
├── M&V planı oluşturma
└── Teknik şartname hazırlama

Adım 3 — ENVER Portalı Başvurusu (1 hafta):
├── Online form doldurma
├── Fizibilite raporu yükleme
├── EVD şirketi onayı
├── Destekleyici belgeler
└── Başvuru teyit numarası alma

Adım 4 — YEGM Değerlendirmesi (2-4 ay):
├── İdari uygunluk kontrolü
├── Teknik değerlendirme (komisyon)
├── Saha doğrulama (gerekli ise)
├── Puanlama ve sıralama
└── Onay/ret bildirimi

Adım 5 — Uygulama (3-12 ay):
├── Tedarik ve kurulum
├── Devreye alma
├── Performans testleri
├── Uygulama raporu hazırlama
└── YEGM'e bildirim

Adım 6 — M&V ve Ödeme (3-6 ay):
├── Tasarruf doğrulama ölçümleri
├── M&V raporu sunma
├── YEGM doğrulama denetimi
├── Hibe tutarı belirleme
└── Ödeme
```

### 2.5 Değerlendirme Kriterleri

| Kriter | Ağırlık | Açıklama |
|--------|---------|----------|
| TEP tasarrufu miktarı | %30 | Yıllık toplam tasarruf (TEP/yıl) |
| Geri ödeme süresi | %25 | Kısa geri ödeme daha yüksek puan |
| CO₂ azaltma potansiyeli | %15 | ton CO₂/yıl azaltma |
| Teknoloji yenilikçiliği | %10 | Yeni teknoloji kullanımı |
| Sektörel etki | %10 | Yaygınlaştırma potansiyeli |
| M&V kalitesi | %10 | Ölçüm ve doğrulama planının güvenilirliği |

### 2.6 Çalışılmış Örnek — Kazan Economizer VAP Başvurusu

```
VAP Örneği: Gıda Fabrikası — Kazan Economizer Projesi

Tesis: Süt işleme tesisi, 3.500 TEP/yıl toplam tüketim
Mevcut durum: 10 ton/h buhar kazanı, baca gazı sıcaklığı 240°C
Proje: Economizer + kondansasyon ısı geri kazanım ünitesi

Tasarruf hesabı:
  Baca gazı sıcaklığı: 240°C → 120°C (economizer sonrası)
  Geri kazanılan ısı: Q = ṁ_baca × Cp × ΔT
  Q = 12.500 Nm³/h × 1.35 kJ/(Nm³·°C) × 120°C = 2.025 MJ/h
  Yıllık çalışma: 7.200 saat
  Q_yıllık = 2.025 × 7.200 / 1.000 = 14.580 GJ/yıl
  Doğalgaz tasarrufu = 14.580 / 34.526 × 1000 = 422.300 Sm³/yıl
  TEP tasarrufu = 422.300 × 0.8244 / 1000 = 348 TEP/yıl

  ExergyLab exergy analizi:
  Mevcut kazan exergy verimi: %34.2
  Economizer sonrası beklenen: %41.5
  Exergy iyileşme: +7.3 puan

Ekonomik analiz:
  Yatırım maliyeti: 2.800.000 TL
  Yıllık tasarruf: 1.250.000 TL/yıl (doğalgaz fiyatı bazlı)
  Basit geri ödeme: 2.800.000 / 1.250.000 = 2.24 yıl ✓ (≤5 yıl)
  CO₂ azaltma: 348 × 2.34 = 814 ton CO₂/yıl

VAP desteği (%30 — atık ısı geri kazanım):
  Hibe tutarı: 2.800.000 × 0.30 = 840.000 TL
  Net yatırım: 2.800.000 - 840.000 = 1.960.000 TL
  Efektif geri ödeme: 1.960.000 / 1.250.000 = 1.57 yıl

Sonuç: VAP ile geri ödeme 2.24 yıldan 1.57 yıla düştü.
```

### 2.7 VAP Doküman Listesi

```
VAP başvurusu için gerekli belgeler:
☐ Başvuru formu (ENVER portalı)
☐ Tesis bilgi formu (kapasite, tüketim, üretim)
☐ Detaylı fizibilite raporu (EVD onaylı)
☐ Teknik şartname ve keşif özeti
☐ Proforma fatura veya teklif mektubu (min 3 adet)
☐ M&V planı (IPMVP uyumlu)
☐ Mevcut durum ölçüm raporları
☐ Son 3 yıl enerji fatura özetleri
☐ Üretim verileri (son 3 yıl)
☐ Enerji yöneticisi atama belgesi
☐ EVD şirketi yetki belgesi
☐ Ticaret sicil gazetesi
☐ Vergi levhası
☐ İmza sirküleri
```

## 3. Gönüllü Anlaşmalar (Voluntary Agreements)

### 3.1 Sistem Tanımı

```
Gönüllü anlaşma sistemi:
├── Taraflar: Sanayi tesisi ↔ Enerji ve Tabii Kaynaklar Bakanlığı
├── Hedef: 3 yıl içinde toplam enerjide %10 azaltma
├── Kapsam: ≥1.000 TEP/yıl tüketen tesisler
├── Süre: 3 yıllık anlaşma dönemi
└── Gönüllülük: Zorunlu değil, teşvik bazlı

Avantajlar:
├── Enerji etüdü muafiyeti (anlaşma süresi boyunca)
├── VAP başvurularında öncelik
├── Enerji verimliliği desteklerinde ek puan
├── YEGM tarafından teknik danışmanlık desteği
└── Kurumsal itibar ve sürdürülebilirlik imajı

Yükümlülükler:
├── Yıllık ilerleme raporu
├── EnPI izleme ve raporlama
├── Enerji yönetim sistemi kurulumu (ISO 50001 teşvikli)
├── 3 yıl sonunda toplam tasarruf doğrulaması
└── YEGM denetimlerine açıklık
```

### 3.2 Mevcut Durum

Gönüllü anlaşma sistemi Türkiye'de henüz yaygınlaşmamış olup, katılım oranı düşüktür. AB ülkelerindeki başarılı örneklere (Hollanda LTA, Danimarka) kıyasla geliştirilmesi beklenmektedir. 2024-2026 döneminde sistemin güncellenmesi ve teşviklerin artırılması planlanmaktadır.

## 4. Beyaz Sertifika (White Certificate)

### 4.1 Sistem Tasarımı

```
Beyaz sertifika mekanizması:

Temel prensip:
├── Enerji dağıtıcılarına tasarruf yükümlülüğü verilmesi
├── Tasarruf sağlayan her TEP için 1 sertifika düzenlenmesi
├── Sertifikaların piyasada alınıp satılabilmesi
└── Yükümlülüğü yerine getiremeyen şirketlere ceza

Türkiye pilot uygulaması:
├── 2025-2026 döneminde pilot çalışma planlanmaktadır
├── İlk aşamada büyük elektrik dağıtım şirketleri
├── TEP bazlı sertifikasyon
├── YEGM tarafından sertifika doğrulama
└── Elektronik kayıt ve takip sistemi
```

### 4.2 AB Örnekleri ve Karşılaştırma

| Ülke | Başlangıç | Yükümlü Taraf | Hedef | Sertifika Fiyatı |
|------|-----------|---------------|-------|-----------------|
| İtalya (TEE) | 2005 | Elektrik/gaz dağıtıcıları | Yıllık TEP hedefi | ~250 €/TEP |
| Fransa (CEE) | 2006 | Enerji tedarikçileri | 4 yıllık kWh cumFin hedefi | ~8 €/MWh |
| Polonya | 2013 | Enerji tedarikçileri | TEP bazlı | ~35 €/TEP |
| Danimarka | 2006 | Dağıtım şirketleri | GJ bazlı | ~15 €/GJ |
| Türkiye (plan) | 2026+ | Elektrik dağıtım şirketleri | TEP bazlı (belirlenmedi) | Henüz belirsiz |

### 4.3 Beyaz Sertifika ve ExergyLab

ExergyLab platformu, beyaz sertifika sistemi hayata geçtiğinde tasarruf doğrulaması için kritik bir araç olacaktır. Exergy analizi ile tasarruf miktarının hesaplanması ve M&V raporlaması, sertifika başvurularının temelini oluşturur.

## 5. ESCO ve EPC Modelleri (Energy Service Companies and Energy Performance Contracts)

### 5.1 Garantili Tasarruf Modeli (Guaranteed Savings)

```
Garantili tasarruf modeli:

Yapı:
├── Tesis: Finansman sağlar (banka kredisi)
├── ESCO: Tasarruf garantisi verir
├── Banka: Kredi sağlar (tesis garantisi + ESCO performans garantisi)
└── M&V: Bağımsız doğrulama

Nakit akışı:
  Yıl 0: Tesis → ESCO'ya proje bedeli (bankadan kredi ile)
  Yıl 1-N: Tasarruf → Tesisin kredi geri ödemesi
  Garantili tasarruf < Gerçekleşen → ESCO farkı tazmin eder
  Garantili tasarruf > Gerçekleşen → Tasarruf fazlası tesis kalır

Avantajlar:
├── Tesis, tasarruf garantisi ile riskini azaltır
├── ESCO, teknik performansı garanti eder
├── Banka, iki taraflı güvence ile kredi kullandırır
└── Sözleşme süresi genellikle 5-10 yıl
```

### 5.2 Paylaşımlı Tasarruf Modeli (Shared Savings)

```
Paylaşımlı tasarruf modeli:

Yapı:
├── ESCO: Finansman + uygulama + garanti
├── Tesis: Minimum yükümlülük (mevcut enerji harcamasını sürdürme)
├── Tasarruf: Önceden belirlenen oranla paylaşılır
└── M&V: Genellikle ESCO tarafından

Nakit akışı:
  Yıl 0: ESCO → Yatırım yapar (kendi sermayesi veya kredi)
  Yıl 1-N: Tasarruf paylaşımı (örn: %70 ESCO, %30 tesis)
  Sözleşme sonu: Ekipman tesise devredilir
  Sözleşme sonrası: %100 tasarruf tesisin

Avantajlar:
├── Tesis için sıfır veya düşük ön yatırım
├── ESCO riski üstlenir (hem teknik hem finansal)
├── Tesis bilançosunu etkilemez (off-balance-sheet)
└── Sözleşme süresi genellikle 7-15 yıl
```

### 5.3 Model Karşılaştırma Tablosu

| Kriter | Garantili Tasarruf | Paylaşımlı Tasarruf |
|--------|-------------------|---------------------|
| Finansman kaynağı | Tesis (banka kredisi) | ESCO |
| Teknik risk | ESCO üstlenir | ESCO üstlenir |
| Finansal risk | Paylaşımlı | ESCO üstlenir |
| Ön yatırım (tesis) | Var (kredi ile) | Yok veya düşük |
| Tasarruf paylaşımı | %100 tesisin (garanti dahilinde) | Oransal (%50-80 ESCO) |
| Sözleşme süresi | 5-10 yıl | 7-15 yıl |
| Bilanço etkisi | On-balance-sheet | Off-balance-sheet |
| Uygun tesis ölçeği | Orta-büyük | Büyük |
| Türkiye'de yaygınlık | Daha yaygın | Gelişmekte |
| M&V karmaşıklığı | Orta | Yüksek |

### 5.4 ESCO Seçim Kriterleri

```
ESCO seçerken değerlendirme kontrol listesi:

Teknik yeterlilik:
☐ Sektörel deneyim (referans projeler)
☐ Mühendislik ekibi kalifikasyonu
☐ M&V kapasitesi (CMVP sertifikalı personel)
☐ Teknoloji portföyü (çoklu çözüm yeteneği)
☐ Enerji denetimi ve fizibilite kapasitesi

Finansal güvenilirlik:
☐ Finansal tablolar (son 3 yıl)
☐ Banka referans mektupları
☐ Tamamlanmış proje tutarları
☐ Sigorta kapsamı (mesleki sorumluluk)
☐ Garanti mektubu verme kapasitesi

Sözleşme şartları:
☐ Performans garantisi detayı ve kapsamı
☐ M&V protokolü (IPMVP uyumlu)
☐ Ceza/bonus mekanizması
☐ Sözleşme fesih koşulları
☐ Ekipman sahipliği ve devir koşulları
```

## 6. KOSGEB ve Diğer Destekler

### 6.1 KOSGEB Enerji Verimliliği Destekleri

| Destek Programı | Kapsam | Destek Oranı | Üst Limit |
|-----------------|--------|-------------|-----------|
| KOBİ Proje Desteği | Enerji verimlilik projeleri | %60 | 1.500.000 TL |
| Stratejik Ürün Desteği | Verimli ekipman üretimi | %50 | 5.000.000 TL |
| Ar-Ge ve İnovasyon | Enerji teknolojisi geliştirme | %75 | 1.000.000 TL |
| KOBİ Teknoloji Desteği | Dijital enerji yönetimi | %60 | 500.000 TL |

### 6.2 Kalkınma Ajansı Hibeleri

```
Kalkınma ajansı enerji verimliliği hibeleri:

Özellikler:
├── Bölgesel bazlı programlar (26 kalkınma ajansı)
├── Mali destek: %25-75 (bölge ve programa göre)
├── Üst limit: Genellikle 500.000-2.000.000 TL
├── Dönemsel çağrı usulü (yılda 1-2 kez)
└── Değerlendirme: Bağımsız komisyon

Enerji verimliliği kapsamındaki proje konuları:
├── Enerji etüdü ve fizibilite
├── Verimli ekipman yatırımı
├── Enerji izleme sistemi kurulumu
├── Yenilenebilir enerji entegrasyonu
├── Atık ısı değerlendirme
└── Enerji yönetim sistemi (ISO 50001)
```

### 6.3 Uluslararası Kredi Hatları

| Kaynak | Program | Faiz | Vade | Kapsam |
|--------|---------|------|------|--------|
| EBRD | TurSEFF | Piyasa altı | 5-10 yıl | Enerji verimliliği + yenilenebilir |
| EBRD | MidSEFF | Piyasa altı | 5-10 yıl | Orta ölçekli sürdürülebilir enerji |
| IFC | CIFI | Değişken | 5-12 yıl | İklim yatırımları |
| KfW | DEG | Uygun koşullu | 7-12 yıl | Yeşil sanayi |
| AFD | SUNREF | Düşük | 5-10 yıl | Sürdürülebilir enerji |

### 6.4 TÜBİTAK Ar-Ge Projeleri

```
TÜBİTAK enerji verimliliği Ar-Ge destekleri:

1001 — Bilimsel ve Teknolojik Araştırma Projesi:
├── Enerji verimliliği temel araştırma
├── %100 destek (akademik)
└── 36 ay süre

1501 — Sanayi Ar-Ge Desteği:
├── Yenilikçi enerji verimlilik teknolojisi
├── %75 destek (KOBİ), %60 (büyük)
├── 36 ay süre
└── Prototip + ticarileştirme

1507 — KOBİ Ar-Ge Başlangıç Desteği:
├── İlk Ar-Ge projesi
├── %75 destek
└── 18 ay süre

TEYDEB 1511 — Öncelikli Alanlar Programı:
├── Enerji teknolojileri
├── %60-75 destek
└── Çağrı bazlı
```

## 7. Başvuru Süreci Rehberi (Application Process Guide)

### 7.1 Hangi Teşvik İçin Nereye Başvurulur?

| Tesis Profili | Öncelikli Teşvik | Başvuru Yeri | Zaman Çizelgesi |
|---------------|-----------------|-------------|-----------------|
| ≥1.000 TEP sanayi tesisi | VAP | YEGM / ENVER portalı | 6-12 ay |
| KOBİ (<250 çalışan) | KOSGEB Proje Desteği | KOSGEB e-devlet | 3-9 ay |
| Büyük tesis + ESCO istiyorsa | ESCO/EPC + VAP | ESCO + ENVER | 6-18 ay |
| Ar-Ge / inovasyon projesi | TÜBİTAK 1501 | TÜBİTAK PRODİS | 9-15 ay |
| Bölgesel proje | Kalkınma Ajansı | İlgili ajans KAYS | 3-9 ay |
| Uluslararası kredi | EBRD/IFC hatları | Aracı banka | 3-6 ay |

### 7.2 Gerekli Belgeler Kontrol Listesi

```
Temel belgeler (tüm teşvikler için):
☐ Ticaret sicil gazetesi
☐ Vergi levhası
☐ İmza sirküleri
☐ Son 3 yıl mali tablolar
☐ Enerji fatura özetleri (3 yıl)
☐ Üretim verileri (3 yıl)

VAP spesifik:
☐ EVD fizibilite raporu
☐ M&V planı
☐ Proforma faturalar (min 3)
☐ Enerji yöneticisi belgesi
☐ Mevcut ölçüm raporları

KOSGEB spesifik:
☐ KOBİ beyannamesi
☐ Proje başvuru formu (KOSGEB formatı)
☐ İş planı / fizibilite
☐ Teklif mektupları

ESCO/EPC spesifik:
☐ Enerji tüketim profili (detaylı)
☐ Ekipman envanteri
☐ Operasyonel parametreler
☐ Mevcut bakım kayıtları
```

### 7.3 Genel Zaman Çizelgesi

```
Teşvik başvuru zaman çizelgesi (ortalama):

Ay 1-2:   Enerji analizi + fırsat tespiti (ExergyLab ile)
Ay 2-3:   EVD şirketi/ESCO ile görüşme
Ay 3-5:   Detaylı fizibilite raporu hazırlama
Ay 5-6:   Başvuru dosyası hazırlama ve sunma
Ay 6-10:  Değerlendirme süreci (kurum bazlı)
Ay 10-11: Onay + sözleşme imzalama
Ay 11-18: Uygulama + devreye alma
Ay 18-24: M&V + hibe/ödeme alma

Toplam süre: 18-24 ay (başvurudan ödemeye)
```

## 8. ExergyLab ile Teşvik Entegrasyonu

### 8.1 Platform Verilerinin Teşvik Başvurularında Kullanımı

```
ExergyLab → Teşvik başvurusu veri akışı:

1. Mevcut Durum Tespiti:
   ├── Ekipman bazında exergy analizi → Verimsizlik kaynağı
   ├── Fabrika exergy Sankey diyagramı → Kayıp haritası
   ├── Cross-equipment fırsat analizi → Entegrasyon potansiyeli
   └── Sektörel benchmark karşılaştırma → İyileşme potansiyeli

2. Tasarruf Hesaplama:
   ├── Exergy yıkımı miktarı → Teorik tasarruf potansiyeli
   ├── Pratik tasarruf hesabı → TEP/yıl ve TL/yıl
   ├── CO₂ azaltma hesabı → ton CO₂/yıl
   └── Geri ödeme süresi → VAP uygunluk kontrolü

3. VAP Dosyası Desteği:
   ├── Mevcut durum ölçüm verileri → Başvuru eki
   ├── Exergy verim grafiği → Fizibilite raporu görseli
   ├── Benchmark konumlandırma → Gerekçelendirme
   └── M&V planı önerisi → IPMVP opsiyon seçimi

4. Proje Sonrası İzleme:
   ├── Uygulama öncesi-sonrası karşılaştırma
   ├── CUSUM ile tasarruf doğrulama
   ├── M&V raporu veri kaynağı
   └── Yıllık performans takibi
```

### 8.2 ExergyLab Teşvik Rapor Çıktıları

| Rapor Türü | İçerik | Kullanım Alanı |
|-----------|--------|----------------|
| Exergy Durum Raporu | Ekipman ve fabrika exergy verimlilikleri | EVD fizibilite raporu eki |
| Tasarruf Potansiyeli Raporu | TEP, TL, CO₂ bazlı tasarruf hesabı | VAP başvurusu |
| Benchmark Karşılaştırma | Sektörel konumlandırma | Gerekçelendirme |
| Sankey Diyagramı | Enerji ve exergy akış görseli | Yönetim sunumu |
| M&V Önerisi | IPMVP uyumlu doğrulama planı | Sözleşme eki |

## 9. İlgili Dosyalar

- [Türkiye Mevzuatı](turkey_legislation.md) — 5627 Kanunu, YEGM zorunlulukları, TEP hesaplama
- [Enerji Yönetimi INDEX](INDEX.md) — Enerji yönetimi dosya navigasyonu
- [M&V ve IPMVP](mv_ipmvp.md) — Ölçüm ve doğrulama protokolleri
- [Ekonomik Analiz](../economic_analysis.md) — Geri ödeme, NPV, IRR hesaplama
- [Uygulama Rehberi](../implementation.md) — Proje uygulama adımları
- [EnPI Rehberi](enpi_guide.md) — Performans göstergeleri ve izleme
- [CUSUM Analizi](cusum_analysis.md) — Tasarruf doğrulama yöntemi

## 10. Referanslar

- 5627 sayılı Enerji Verimliliği Kanunu (2007, değişikliklerle)
- YEGM, "Verimlilik Artırıcı Proje (VAP) Uygulama Usul ve Esasları"
- YEGM, "Gönüllü Anlaşma Yönetmeliği"
- KOSGEB, "KOBİ Proje Destek Programı Uygulama Esasları"
- EBRD, "TurSEFF — Turkey Sustainable Energy Financing Facility"
- IFC, "Resource Efficiency Financing in Turkey"
- EU Directive 2012/27/EU — Energy Efficiency Directive (EED), Article 7
- Carbon Trust, "Energy Performance Contracting — A Partnership to Save Energy"
- ESCO Europe, "European ESCO Market Report 2023"
- IPMVP, "International Performance Measurement and Verification Protocol (Volume I)"
