---
title: "Finansman Modelleri ve Teşvikler — Financing Models and Incentives"
category: economics
equipment_type: steam_turbine
keywords: [finansman, ESCO, BOT, leasing, VAP, KOSGEB, teşvik, AB fonları, EIB, EBRD, karbon kredisi, Gold Standard, CHP finansman]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/economics/feasibility.md, steam_turbine/economics/feed_in_tariff.md, factory/economic_analysis.md, factory/energy_pricing.md]
use_when: ["CHP projesi finansmanı araştırılırken", "Teşvik ve hibe programları değerlendirilirken", "ESCO veya BOT modeli düşünüldüğünde", "Uluslararası enerji verimliliği fonları sorgulandığında"]
priority: low
last_updated: 2026-01-31
---
# Finansman Modelleri ve Teşvikler — Financing Models and Incentives

> Son güncelleme: 2026-01-31

## Genel Bakış

CHP ve buhar türbini projeleri yüksek sermaye yoğunluğuna sahip yatırımlardır. Bu dosya, Türkiye'de ve uluslararası arenada kullanılabilecek finansman modellerini, ulusal ve AB teşvik programlarını, uluslararası kredi hatlarını ve karbon kredisi mekanizmalarını ele almaktadır.

## 1. ESCO Modeli (Energy Service Company)

### 1.1 Model Tanımı

```
ESCO (Energy Service Company — Enerji Hizmet Şirketi):

Tanım: ESCO, enerji verimliliği projelerini kendi kaynaklarıyla
finanse eden, tasarruf garantisi veren ve proje riskini üstlenen
profesyonel hizmet şirketidir.

Çalışma prensibi:
1. ESCO, enerji denetimi yapar ve tasarruf potansiyelini belirler
2. Projeyi tasarlar, finanse eder, kurar ve işletir
3. Garanti edilen tasarrufun büyük kısmını (%70-90) alır
4. Sözleşme süresi sonunda tesis müşteriye devredilir
5. Tasarruf gerçekleşmezse farkı ESCO karşılar (garanti)

Sözleşme türleri:
a) Paylaşımlı tasarruf (Shared Savings):
   - Tasarruf önceden ölçülür, paylaşılır
   - Müşteri payı: %10-30 (sözleşme boyunca)
   - ESCO payı: %70-90 (sözleşme boyunca)
   - Sözleşme sonrası: %100 müşteriye

b) Garantili tasarruf (Guaranteed Savings):
   - ESCO minimum tasarrufu garanti eder
   - Finansman müşteri veya 3. taraftan
   - ESCO performans garantisi verir
   - Fazla tasarruf müşteriye kalır
```

### 1.2 ESCO ve CHP Projeleri

```
CHP projelerinde ESCO modeli:

Uygunluk değerlendirmesi:
| Parametre                  | ESCO İçin Uygun      | ESCO İçin Uygun Değil |
|----------------------------|----------------------|------------------------|
| Proje boyutu               | >500 kW_e            | <200 kW_e              |
| Çalışma saati              | >5,000 h/yıl         | <3,500 h/yıl           |
| Müşteri kredi notu         | İyi-mükemmel          | Düşük-belirsiz         |
| Tasarruf ölçülebilirliği   | Kolay ölçüm           | Karmaşık ölçüm         |
| Sözleşme süresi            | 5-15 yıl              | <3 yıl                 |
| Yıllık tasarruf            | >200,000 EUR          | <50,000 EUR            |

CHP ESCO finansman örneği:
Proje: 3 MW_e karşı basınçlı türbin CHP
Yatırım: 2,700,000 EUR
Yıllık tasarruf: 1,200,000 EUR/yıl
Sözleşme süresi: 7 yıl

ESCO payı (%80): 960,000 EUR/yıl × 7 yıl = 6,720,000 EUR
Müşteri payı (%20): 240,000 EUR/yıl × 7 yıl = 1,680,000 EUR
Sözleşme sonrası müşteri geliri: 1,200,000 EUR/yıl (tam)

Müşteri NPV (20 yıl, %10):
Yıl 1-7: 240,000 EUR/yıl
Yıl 8-20: 1,200,000 EUR/yıl
NPV = 240,000 × PVA(7,%10) + 1,200,000 × PVA(13,%10) × PVF(7,%10)
    = 240,000 × 4.868 + 1,200,000 × 7.103 × 0.513
    = 1,168,320 + 4,372,226 = 5,540,546 EUR
→ Müşteri sıfır yatırımla 5.5M EUR NPV elde eder
```

### 1.3 Türkiye ESCO Piyasası

```
Türkiye ESCO pazarı durumu (2025-2026):

Aktif ESCO firmaları:
- Büyük uluslararası firmalar (Siemens, Schneider, ABB enerji hizmetleri)
- Yerel ESCO firmaları (ENVER, MESKO, ve benzerleri)
- Mühendislik firmaları ESCO hizmeti sunanlar

Düzenleyici çerçeve:
- 5627 Sayılı Enerji Verimliliği Kanunu (EVK)
- ESCO tanımı ve yetkilendirme çerçevesi mevcut
- EVK kapsamında ESCO yetki belgesi gerekliliği

Zorluklar:
- Sınırlı ESCO piyasası olgunluğu
- Müşteri güven eksikliği (performans garantisi)
- Ölçüm ve doğrulama (M&V) standartları yetersiz
- Uzun sözleşme süreleri endişesi
- Küçük proje boyutları (transaction cost)

Gelişme alanları:
- IPMVP (International Performance Measurement & Verification Protocol)
  standartlarının yaygınlaşması
- Süper ESCO kavramı (kamu projelerinde)
- AB uyum sürecinde ESCO düzenlemelerinin güçlenmesi
```

## 2. BOT Modeli (Build-Operate-Transfer)

### 2.1 Model Tanımı

```
BOT (Build-Operate-Transfer — Yap-İşlet-Devret):

Tanım: Yatırımcı/sponsor, tesisi kendi kaynaklarıyla kurar,
belirli süre işletir ve süre sonunda müşteriye/devlete devreder.

CHP projelerinde BOT:
1. Sponsor firma (enerji şirketi) CHP tesisini kurar
2. Uzun süreli enerji satış sözleşmesi imzalanır (10-20 yıl)
3. Sponsor, üretilen elektrik ve ısıyı fabrikaya satar
4. Sözleşme sonunda tesis fabrikaya devredilir
5. Fabrika sıfır yatırımla CHP avantajından yararlanır

BOT fiyatlandırma:
Elektrik satış fiyatı: Şebeke fiyatının %85-95'i
Isı satış fiyatı: Kazan üretim maliyetinin %80-90'ı
→ Müşteri hem elektrikte hem ısıda tasarruf sağlar
→ Sponsor kar marjını yatırım geri dönüşünden elde eder

BOT sözleşme yapısı:
| Parametre          | Tipik Değer               |
|--------------------|---------------------------|
| Sözleşme süresi    | 10-20 yıl                 |
| Elektrik indirimi  | %5-15 (şebekeye göre)     |
| Isı indirimi       | %10-20 (kazan maliyetine)  |
| Devir koşulları    | İyi çalışır durumda       |
| Performans garantisi| Minimum üretim miktarı    |
| Fiyat escalasyonu  | TÜFE veya enerji endeksi  |
```

### 2.2 BOT Avantaj ve Dezavantajları

```
Avantajlar (müşteri perspektifi):
+ Sıfır veya düşük başlangıç yatırımı
+ Performans riski sponsorda
+ Profesyonel işletme
+ Bilançoda borç görünmez (off-balance sheet)
+ Enerji maliyetinde indirim (1. günden itibaren)

Dezavantajlar:
- Uzun süreli bağımlılık (vendor lock-in)
- Toplam maliyet öz yatırımdan daha yüksek
- Sözleşme esneklik kısıtları
- Tesisin bakım kalitesi endişesi (devir öncesi)
- Karmaşık sözleşme müzakeresi

BOT vs. Öz Yatırım karşılaştırma (3 MW CHP örneği):

| Parametre            | Öz Yatırım     | BOT                |
|----------------------|-----------------|--------------------|
| Başlangıç maliyeti   | 2,700,000 EUR   | 0 EUR              |
| Yıllık tasarruf (net)| 1,200,000 EUR   | 180,000 EUR*       |
| SPP                  | 2.25 yıl        | N/A                |
| NPV (20 yıl, %10)   | 7,512,000 EUR   | 1,532,000 EUR      |
| Risk                 | Müşteride       | Sponsorda          |

*BOT'ta müşteri fayda: Enerji indirimi (~%15) = 180,000 EUR/yıl
 Sözleşme sonrası (yıl 16-20): Tam tasarruf 1,200,000 EUR/yıl
```

## 3. Leasing (Finansal Kiralama)

```
Leasing modeli CHP projeleri:

Tanım: Leasing şirketi ekipmanı satın alır, müşteriye kiralar.
Sözleşme sonunda müşteri sembolik bedelle satın alır.

Leasing yapısı:
- Leasing süresi: 5-10 yıl
- Faiz oranı: %8-15 (EUR bazlı, Türkiye)
- Peşinat: %10-20
- Sözleşme sonu: Sembolik bedel ile devir (%1-5)

Avantajlar:
+ Başlangıçta düşük nakit çıkışı
+ Vergi avantajı (kira gideri olarak düşülebilir)
+ Hızlı amortisman imkanı
+ KDV'li fatura ile KDV indirimi

Dezavantajlar:
- Toplam maliyet doğrudan alımdan yüksek (faiz)
- Ekipman leasing şirketi adına kayıtlı
- Erken sonlandırma cezası
- Leasing şirketi CHP teknik bilgisi sınırlı

Leasing hesaplama örneği:
CHP yatırım: 2,700,000 EUR
Peşinat (%15): 405,000 EUR
Leasing tutarı: 2,295,000 EUR
Süre: 7 yıl, Faiz: %10/yıl
Aylık kira: ~46,000 EUR
Toplam geri ödeme: 405,000 + 46,000 × 84 = 4,269,000 EUR
Toplam faiz: 1,569,000 EUR (ek maliyet)
```

## 4. Öz Kaynak + Banka Kredisi (Equity + Bank Loan)

```
Geleneksel finansman yapısı:

Tipik CHP proje finansmanı:
| Kaynak          | Pay [%] | Maliyet         | Not                    |
|-----------------|---------|-----------------|------------------------|
| Öz kaynak       | 30-40   | Fırsat maliyeti | Şirket nakit akışından |
| Banka kredisi   | 40-50   | %8-14 (EUR)     | Yatırım kredisi        |
| Teşvik/hibe     | 10-30   | %0 (hibe)       | VAP, AB fonu           |

Banka kredisi koşulları (Türkiye, 2025-2026):
- Kredi tutarı: Yatırımın %50-70'i
- Vade: 5-10 yıl
- Faiz: %8-14 (EUR bazlı) veya %25-40 (TL bazlı)
- Geri ödeme: Aylık veya 3 aylık taksitler
- Teminat: Ekipman ipoteği + şirket kefaleti
- Ödemesiz dönem (grace period): 6-18 ay

Finansman yapısı optimizasyonu:
1. Teşvik/hibe oranını maksimize et
2. Düşük faizli kredi hatlarını araştır (EIB, EBRD)
3. Öz kaynak payını minimum tut (kaldıraç etkisi)
4. Leasing vs. kredi vergi avantajını karşılaştır
5. Döviz cinsi seçimi: EUR gelir varsa EUR kredi, yoksa TL

Örnek finansman planı (5 MW CHP, 4,500,000 EUR):
| Kaynak           | Tutar [EUR]  | Pay [%] | Maliyet [%/yıl] |
|------------------|-------------|---------|-------------------|
| Öz kaynak        | 900,000     | 20      | %12 (fırsat)      |
| VAP hibesi       | 675,000     | 15      | %0                |
| EBRD kredi hattı | 1,800,000   | 40      | %6                |
| Banka kredisi    | 1,125,000   | 25      | %10               |
| TOPLAM           | 4,500,000   | 100     | WACC ≈ %7.4       |

WACC = 0.20×0.12 + 0.15×0 + 0.40×0.06 + 0.25×0.10 = %7.4
```

## 5. Türk Teşvikleri (Turkish Incentives)

### 5.1 VAP — Verimlilik Arttırıcı Proje Desteği

```
VAP (Verimlilik Arttırıcı Proje) — ETKB programı:

Yasal dayanak: 5627 Sayılı Enerji Verimliliği Kanunu
Yürütücü kurum: T.C. Enerji ve Tabii Kaynaklar Bakanlığı (ETKB)
Uygulama: Enerji İşleri Genel Müdürlüğü (EİGM)

Destek kapsamı:
- Enerji verimliliği artırıcı proje yatırımları
- CHP/kojenerasyon projeleri (yüksek verimli CHP)
- Atık ısı geri kazanım projeleri
- Proses optimizasyonu projeleri

Destek miktarı ve koşulları:
| Parametre              | Değer                           |
|------------------------|---------------------------------|
| Hibe oranı             | %20-30 (proje maliyetinin)      |
| Maksimum destek        | ~500,000-1,000,000 TL*          |
| Minimum tasarruf       | >500 TEP/yıl (ton eşdeğer petrol)|
| Geri ödeme süresi      | <5 yıl (SPP)                    |
| Başvuru dönemi         | Yıllık (ETKB duyurusu)         |

*Güncel limitler için ETKB web sitesi kontrol edilmeli.

Başvuru süreci:
1. Enerji etüdü raporu hazırla (yetkilendirilmiş firma)
2. VAP başvuru formu doldur
3. Teknik fizibilite raporu ekle
4. EİGM değerlendirme (3-6 ay)
5. Onay sonrası uygulama (12-18 ay)
6. Tamamlama ve doğrulama

CHP projeleri için VAP uygunluk:
- Yüksek verimli CHP sertifikası (PES ≥ %10) gerekli
- Tasarruf ≥ 500 TEP/yıl koşulu genellikle sağlanır
  (5 MW CHP ≈ 2,000-5,000 TEP/yıl tasarruf)
```

### 5.2 KOSGEB Destekleri

```
KOSGEB (Küçük ve Orta Ölçekli İşletmeleri Geliştirme ve
Destekleme İdaresi Başkanlığı):

CHP ile ilgili KOSGEB destekleri:
- Proje bazlı destek programları
- Makine-teçhizat desteği
- Ar-Ge ve yenilik projeleri (ORC, mikro türbin gibi)

Uygunluk kriterleri:
- KOBİ tanımına uygunluk (<250 çalışan, <125M TL ciro)
- KOSGEB veri tabanına kayıtlı olma
- Sektörel uygunluk

Destek limitleri:
| Program             | Destek Oranı | Üst Limit           |
|---------------------|-------------|----------------------|
| Proje destek        | %60 (hibe)  | ~600,000-1,000,000 TL|
| Makine-teçhizat     | %60 (hibe)  | ~300,000-500,000 TL  |
| Ar-Ge               | %75 (hibe)  | ~1,000,000 TL        |

Not: KOBİ büyüklüğü CHP projelerine genellikle sınırlıdır.
Küçük ölçekli mikro türbin veya ORC projeleri için uygundur.
```

### 5.3 Kalkınma Ajansı Destekleri

```
Kalkınma ajansı mali destek programları:

26 kalkınma ajansı bölgesel destek programları sunar.
Enerji verimliliği projeleri genellikle kapsamdadır.

Destek yapısı:
- Hibe oranı: %25-50 (proje bütçesi)
- Üst limit: Programa göre değişken (100,000 - 1,000,000 TL)
- Süre: 12-24 ay uygulama
- Başvuru: Yıllık çağrı dönemi

CHP projeleri uygunluk:
- "Rekabetçi Sektörler" mali destek programı
- "Sürdürülebilir Üretim" mali destek programı
- "Enerji Verimliliği" özel çağrılar

Başvuru ipuçları:
- Proje sosyal fayda boyutunu vurgula
- İstihdam etkisini göster
- Çevresel faydayı (CO₂ azaltma) belgele
- Yenilikçi teknoloji kullanımını öne çıkar
- Bölgesel kalkınma planıyla uyumu göster
```

### 5.4 Yatırım Teşvik Sistemi

```
T.C. Cumhurbaşkanlığı Yatırım Teşvik Belgesi:

CHP yatırımları için geçerli teşvikler:
| Teşvik                       | Bölgesel | Stratejik |
|------------------------------|----------|-----------|
| KDV istisnası                | Var      | Var       |
| Gümrük vergisi muafiyeti     | Var      | Var       |
| Vergi indirimi               | %15-90*  | %90       |
| SGK işveren payı desteği     | 2-12 yıl*| 10 yıl   |
| Faiz desteği                 | Var*     | Var       |
| Yatırım yeri tahsisi         | Var      | Var       |
| KDV iadesi                   | Hayır    | Var       |

*Bölgeye göre değişir (1. bölge en düşük, 6. bölge en yüksek)

CHP yatırımı teşvik belgesi:
- "Enerji" sektörü altında başvuru
- Minimum yatırım tutarı: 1,000,000 TL (bölgesel)
- Başvuru: T.C. Sanayi ve Teknoloji Bakanlığı
- Süre: 1-3 ay (onay)
```

## 6. AB Fonları (EU Funds)

### 6.1 IPA (Instrument for Pre-Accession Assistance)

```
IPA — Katılım Öncesi Yardım Aracı:

Türkiye aday ülke statüsünde IPA fonlarına erişebilir.
Enerji verimliliği, IPA programının temel alanlarından biridir.

IPA enerji verimliliği projeleri:
- Endüstriyel enerji verimliliği (CHP dahil)
- Bina enerji verimliliği
- Yenilenebilir enerji entegrasyonu

Destek yapısı:
- Hibe oranı: %50-85 (proje tipine bağlı)
- Proje boyutu: 200,000 - 10,000,000 EUR
- Süre: 18-48 ay
- Ortaklık: AB ülkesi ortağı gerekebilir

Başvuru süreci:
1. Çağrı ilanı takibi (EuropeAid, AB Türkiye Delegasyonu)
2. Konsept notu (Concept Note) hazırlama
3. Ön değerlendirme
4. Tam başvuru (Full Application)
5. Değerlendirme ve onay (6-12 ay)
```

### 6.2 Horizon Europe — Enerji Verimliliği

```
Horizon Europe (2021-2027) enerji verimliliği alanı:

Cluster 5: Climate, Energy and Mobility
- Destination: Efficient, sustainable and inclusive energy use
- CHP ve endüstriyel enerji verimliliği projeleri desteklenir

Proje tipleri:
| Tip              | Hibe Oranı | Bütçe           | Not                |
|------------------|------------|-----------------|---------------------|
| RIA (Research)   | %100       | 2-8 M EUR       | Temel araştırma     |
| IA (Innovation)  | %70        | 5-20 M EUR      | Demonstrasyon       |
| CSA (Coordination)| %100      | 1-3 M EUR       | Koordinasyon        |

Türkiye erişimi:
- Türkiye Horizon Europe asosiye ülke statüsünde
- Türk kuruluşları tam ortaklıkla katılabilir
- TÜBİTAK ulusal irtibat noktası

CHP ile ilgili çağrılar:
- Industrial heat decarbonisation
- Waste heat recovery and utilization
- Smart energy systems and integration
- Energy efficiency in SMEs
```

## 7. Uluslararası Kredi Hatları (International Credit Lines)

### 7.1 EIB (European Investment Bank) Enerji Verimliliği Kredileri

```
EIB — Avrupa Yatırım Bankası:

Türkiye'de enerji verimliliği kredi hatları:
- Türk bankaları aracılığıyla (on-lending)
- Doğrudan proje finansmanı (>25M EUR)

Koşullar:
| Parametre         | Değer                              |
|-------------------|------------------------------------|
| Kredi tutarı      | 50,000 - 25,000,000 EUR (aracı)   |
| Vade              | 5-15 yıl                          |
| Faiz              | %3-6 (EUR bazlı, tercihli)        |
| Geri ödemesiz     | 1-3 yıl                           |
| Teminat           | Proje bazlı + kurumsal            |

Uygunluk kriterleri:
- Enerji tasarrufu ≥ %20 (mevcut duruma göre)
- CO₂ azaltma hesaplaması
- Teknik fizibilite raporu
- Çevresel uyum

Aracı bankalar (Türkiye):
- TEB, Garanti BBVA, İş Bankası, Akbank
- TSKB (Türkiye Sınai Kalkınma Bankası)
- Kalkınma ve Yatırım Bankası

CHP projesi EIB kredi avantajı:
Piyasa faizi: %10-14 (EUR)
EIB kredi faizi: %4-6 (EUR)
Fark: %4-10 → Önemli faiz tasarrufu
```

### 7.2 EBRD (European Bank for Reconstruction and Development)

```
EBRD — Avrupa İmar ve Kalkınma Bankası:

Türkiye enerji verimliliği programları:
- TurSEFF (Turkey Sustainable Energy Financing Facility)
- Mid-size Sustainable Energy Financing Facility (MidSEFF)
- TuREEFF (Turkey Residential Energy Efficiency Financing)

TurSEFF/MidSEFF CHP projeleri:
| Parametre         | TurSEFF           | MidSEFF             |
|-------------------|-------------------|---------------------|
| Kredi limiti      | 50,000-5,000,000  | 5,000,000-50,000,000|
| Vade              | 5-10 yıl          | 5-15 yıl            |
| Faiz              | Tercihli (%4-7)   | Tercihli (%3-6)     |
| Teşvik bonusu     | %10-15 geri ödeme | %10 geri ödeme      |
| Teknik destek     | Ücretsiz enerji etüdü| Ücretsiz        |

EBRD teşvik bonusu:
- Proje başarıyla tamamlanırsa kredi tutarının %10-15'i
  hibe olarak geri ödenir (incentive payment)
- Bu, efektif faiz oranını daha da düşürür

Örnek:
CHP kredi: 2,000,000 EUR (EBRD TurSEFF)
Faiz: %5, Vade: 8 yıl
Teşvik bonusu: %15 → 300,000 EUR geri ödeme
Efektif maliyet: 2,000,000 - 300,000 = 1,700,000 EUR net kredi
→ Efektif faiz: ~%2-3 (çok avantajlı)
```

## 8. Karbon Kredisi (Carbon Credits)

### 8.1 Gönüllü Karbon Piyasası (Voluntary Carbon Market)

```
Gönüllü karbon piyasası — CHP projeleri:

CHP projeleri, şebekeden alınan elektriği azaltarak
(grid displacement) CO₂ emisyonunu düşürür ve
karbon kredisi üretebilir.

CO₂ azaltma hesabı:
ΔCO₂ = Ẇ_elek × t × EF_grid + Q̇_ısı × t × EF_kazan - Q̇_yakıt,CHP × t × EF_yakıt

Burada:
- EF_grid = Şebeke emisyon faktörü [tCO₂/MWh]
  Türkiye: ~0.45-0.50 tCO₂/MWh (2025)
- EF_kazan = Kazan emisyon faktörü [tCO₂/MWh_th]
  Doğalgaz: 0.202 tCO₂/MWh_th
- EF_yakıt = CHP yakıt emisyon faktörü

Örnek (5 MW_e CHP):
Elektrik üretimi: 35,000 MWh/yıl
Isı üretimi: 245,000 MWh_th/yıl (HPR=7)
CHP yakıt tüketimi: 326,700 MWh_th/yıl (η_toplam=%85.7)

Baseline emisyon:
- Şebeke elektriği: 35,000 × 0.47 = 16,450 tCO₂
- Kazan ısısı: 245,000 × 0.202 / 0.88 = 56,250 tCO₂
- Toplam baseline: 72,700 tCO₂

CHP emisyon:
- CHP yakıt: 326,700 × 0.202 = 65,993 tCO₂

Net CO₂ azaltma: 72,700 - 65,993 = 6,707 tCO₂/yıl
```

### 8.2 Gold Standard Sertifikası

```
Gold Standard — CHP projeleri için:

Gold Standard, en güvenilir gönüllü karbon standartlarından biridir.
CHP projelerinin sürdürülebilir kalkınma katkısını belgeler.

Sertifikasyon süreci:
1. PIN (Project Idea Note) hazırlama
2. PDD (Project Design Document) geliştirme
3. Yerel paydaş istişaresi (stakeholder consultation)
4. Doğrulama (validation) — bağımsız denetçi
5. Kayıt (registration)
6. İzleme (monitoring)
7. Doğrulama (verification) — yıllık
8. Kredi çıkarma (issuance)

Maliyetler:
| Kalem                  | Maliyet [EUR]         |
|------------------------|-----------------------|
| PDD hazırlama          | 15,000-30,000         |
| Doğrulama              | 15,000-25,000         |
| Kayıt ücreti           | 5,000-10,000          |
| Yıllık doğrulama       | 10,000-20,000         |
| Toplam (ilk yıl)       | 45,000-85,000         |
| Toplam (sonraki yıllar)| 10,000-20,000/yıl     |

Karbon kredi geliri (2025-2026):
Gönüllü piyasa fiyatı: 5-25 EUR/tCO₂ (proje tipine bağlı)
Gold Standard primi: 10-30 EUR/tCO₂ (yüksek kalite)

Örnek CHP gelir:
CO₂ azaltma: 6,707 tCO₂/yıl
Fiyat: 15 EUR/tCO₂ (Gold Standard)
Yıllık gelir: 6,707 × 15 = 100,605 EUR/yıl

Net gelir (sertifikasyon maliyeti düşüldükten sonra):
Yıl 1: 100,605 - 65,000 = 35,605 EUR
Sonraki yıllar: 100,605 - 15,000 = 85,605 EUR/yıl
```

### 8.3 Türkiye Gönüllü Karbon Piyasası

```
Türkiye karbon piyasası durumu:

Mevcut durum:
- Gönüllü karbon piyasası aktif
- Türkiye ETS (Emisyon Ticaret Sistemi) planlanıyor
  (CBAM uyumu için zorunlu olacak)
- MRV (Monitoring, Reporting, Verification) altyapısı gelişiyor

CHP projeleri için fırsatlar:
1. Gold Standard / Verra VCS sertifikalı karbon kredisi
2. CBAM uyumu için emisyon azaltma belgeleme
3. Gelecek Türkiye ETS'de emisyon hakkı tasarrufu
4. CDP/ESG raporlamasında düşük emisyon avantajı

Gelecek projeksiyonu:
| Yıl  | Gönüllü Fiyat [EUR/tCO₂] | ETS Fiyat [EUR/tCO₂]* |
|------|---------------------------|------------------------|
| 2025 | 5-20                      | N/A                    |
| 2026 | 8-25                      | 15-25 (başlangıç)      |
| 2028 | 10-30                     | 25-45                  |
| 2030 | 15-40                     | 40-70                  |

*Türkiye ETS henüz yürürlüğe girmemiştir, tahminlerdir.
```

## 9. Finansman Karar Matrisi (Financing Decision Matrix)

```
CHP projesi finansman seçimi:

| Kriter              | Öz Kaynak  | Banka Kredisi | ESCO     | BOT      | Leasing  |
|----------------------|-----------|---------------|----------|----------|----------|
| Başlangıç maliyeti   | Yüksek    | Orta          | Sıfır    | Sıfır    | Düşük    |
| Toplam maliyet        | En düşük  | Orta          | Yüksek   | En yüksek| Orta-yüks|
| Kontrol               | Tam       | Tam           | Sınırlı  | Sınırlı  | Tam      |
| Risk                  | Müşteride | Müşteride     | ESCO'da  | Sponsorda| Müşteride|
| Vergi avantajı        | Amortisman| Faiz gideri   | Hizmet alımı| Hizmet| Kira gid.|
| Bilanço etkisi        | Varlık    | Borç          | Yok      | Yok      | Borç/Yok |
| Esneklik              | Yüksek    | Orta          | Düşük    | Düşük    | Orta     |
| Uygulama hızı         | Hızlı     | Orta          | Yavaş    | Yavaş    | Orta     |

Karar rehberi:
- Güçlü nakit pozisyonu → Öz kaynak + teşvik
- Orta nakit, iyi kredi notu → Banka kredisi + EIB/EBRD
- Sınırlı nakit, yüksek yük → ESCO veya BOT
- KOBİ, küçük proje → Leasing + KOSGEB
- Büyük proje, uluslararası → EIB/EBRD + karbon kredisi
```

## 10. Tipik CHP Proje Finansman Yapısı (Typical CHP Financing Structure)

```
Örnek: 5 MW_e buhar türbini CHP projesi

Toplam yatırım: 4,500,000 EUR

Optimum finansman yapısı:
┌─────────────────────────────────────────────────┐
│ Kaynak              │ Tutar [EUR] │ Pay [%] │   │
├─────────────────────┼─────────────┼─────────┤   │
│ Öz kaynak           │   900,000   │   20    │   │
│ VAP hibesi          │   675,000   │   15    │   │
│ EBRD kredi (TurSEFF)│ 1,800,000   │   40    │   │
│ Banka kredisi       │ 1,125,000   │   25    │   │
│ TOPLAM              │ 4,500,000   │  100    │   │
└─────────────────────┴─────────────┴─────────┘   │

Ek gelir kaynakları:
│ Karbon kredisi      │  85,000/yıl │   —     │   │
│ EBRD teşvik bonusu  │ 270,000     │  1 kez  │   │

Efektif yatırım maliyeti:
4,500,000 - 675,000 (VAP) - 270,000 (EBRD bonus) = 3,555,000 EUR

WACC hesabı:
WACC = 0.20 × 0.12 + 0.15 × 0 + 0.40 × 0.05 + 0.25 × 0.10
     = 0.024 + 0 + 0.020 + 0.025 = %6.9

Efektif WACC (teşvikler dahil):
≈ %5.0-5.5 → Düşük sermaye maliyeti ile yüksek NPV

NPV (20 yıl, WACC = %6.9):
NPV ≈ -3,555,000 + 1,200,000 × PVA(20, %6.9) + 85,000 × PVA(20, %6.9)
    ≈ -3,555,000 + 1,285,000 × 10.59
    ≈ -3,555,000 + 13,608,000 = 10,053,000 EUR

IRR ≈ %35 (teşvikler dahil)
SPP = 3,555,000 / 1,285,000 = 2.77 yıl
```

## İlgili Dosyalar

- [Fizibilite](feasibility.md) — CHP fizibilite analizi ve ekonomik değerlendirme
- [Tarife ve Piyasa](feed_in_tariff.md) — Türkiye elektrik piyasası ve düzenleyici çerçeve
- [Formüller](../formulas.md) — CHP verimlilik ve PES hesaplama formülleri
- [Benchmarklar](../benchmarks.md) — Ekonomik benchmark verileri (CAPEX, OPEX, SPP)
- [CHP Sistemleri](../systems/steam_turbine_chp.md) — Buhar türbini CHP konfigürasyonları
- [Fabrika Ekonomik Analiz](../../factory/economic_analysis.md) — NPV, IRR, SPP yatırım metodolojisi
- [Enerji Fiyatlandırma](../../factory/energy_pricing.md) — Tarife yapıları ve maliyet analizi
- [Yaşam Döngüsü Maliyet](../../factory/life_cycle_cost.md) — LCC analizi detayları

## Referanslar

- 5627 Sayılı Enerji Verimliliği Kanunu, T.C. Resmi Gazete, 2007.
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Verimlilik Arttırıcı Proje (VAP) Uygulama Usul ve Esasları."
- KOSGEB, "KOBİ Proje Destek Programı Uygulama Esasları."
- EIB (European Investment Bank), "Energy Efficiency Lending Criteria," 2023.
- EBRD (European Bank for Reconstruction and Development), "TurSEFF Program Guidelines."
- Gold Standard Foundation, "GS4GG — Gold Standard for the Global Goals," Version 1.2.
- Verra (VCS — Verified Carbon Standard), "Methodology for Grid Connected Electricity Generation from Cogeneration," VM0029.
- EU Regulation 2023/956, "Carbon Border Adjustment Mechanism (CBAM)."
- IFC (International Finance Corporation), "Utility-Scale CHP Market Assessment — Turkey," 2020.
- OECD (2021). *Blended Finance for Energy Efficiency*, OECD Publishing.
- Turner, W.C. & Doty, S. (2013). *Energy Management Handbook*, 9th Edition, Fairmont Press.
- Thumann, A. et al. (2012). *Handbook of Energy Audits*, 9th Edition, Fairmont Press.
