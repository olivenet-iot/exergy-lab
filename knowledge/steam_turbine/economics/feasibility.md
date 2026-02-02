---
title: "CHP/Türbin Fizibilite Analizi — CHP/Turbine Feasibility Analysis"
category: economics
equipment_type: steam_turbine
keywords: [fizibilite, CHP, kojenerasyon, NPV, IRR, SPP, hassasiyet analizi, risk değerlendirme, yatırım kararı]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, factory/economic_analysis.md, factory/energy_pricing.md]
use_when: ["CHP yatırım kararı verilirken", "Buhar türbini fizibilite raporu hazırlanırken", "Yatırım ekonomik analiz gerektiğinde", "Hassasiyet ve risk analizi yapılırken"]
priority: medium
last_updated: 2026-01-31
---
# CHP/Türbin Fizibilite Analizi — CHP/Turbine Feasibility Analysis

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu dosya, endüstriyel buhar türbini ve CHP (Combined Heat and Power — kojenerasyon) projelerinin fizibilite değerlendirmesi için kapsamlı bir çerçeve sunar. Teknik ön koşullar, ekonomik değerlendirme yöntemleri, hassasiyet analizi, risk değerlendirme ve karar kriterleri ele alınmaktadır.

## 1. Teknik Ön Koşullar (Technical Prerequisites)

### 1.1 Minimum Çalışma Saati Gereksinimleri

CHP projelerinin ekonomik olabilmesi için yeterli çalışma süresi kritik öneme sahiptir.

```
Çalışma saati gereksinimleri:

| Parametre                     | Minimum     | Önerilen    | İdeal       |
|-------------------------------|-------------|-------------|-------------|
| Yıllık çalışma saati         | >4,000 h    | >5,500 h    | >7,000 h    |
| Yük faktörü (load factor)    | >50%        | >65%        | >80%        |
| Eş zamanlılık (simultaneity) | >60%        | >75%        | >85%        |

Not: 4,000 h/yıl altında CHP genellikle ekonomik değildir.
Kampanya tipi endüstriler (örn. şeker fabrikası ~3,500-5,000 h)
özel değerlendirme gerektirir.
```

### 1.2 Kararlı Termal Talep (Stable Thermal Demand)

```
Termal talep gereksinimleri:

1. Baz ısı yükü (base thermal load):
   - Minimum: >500 kW_th (sürekli)
   - CHP boyutlandırma hedefi: Baz ısı yükünün %80-100'ü
   - Kural: CHP'yi baz yüke göre boyutlandır, piki kazan ile karşıla

2. Isı talep profili:
   - Düz profil (flat demand): En uygun — gıda, kimya, kağıt
   - Değişken profil (variable demand): Dikkatli boyutlandırma gerekli
   - Mevsimsel profil (seasonal): Yaz-kış farkı >%50 ise sorunlu

3. Buhar basıncı ve sıcaklık:
   - Proses buhar basıncı: Tipik 2-15 bar
   - Türbin giriş-çıkış basınç farkı: Minimum 15-20 bar
   - Düşük basınç farkı → düşük elektrik üretimi → düşük getiri

4. Isı/güç oranı (HPR — Heat-to-Power Ratio):
   - Buhar türbini CHP: HPR = 3-10
   - Gaz türbini CHP: HPR = 1.5-2.5
   - Uygun HPR aralığında olmalı
```

### 1.3 Yakıt Mevcudiyeti (Fuel Availability)

```
Yakıt değerlendirme kriterleri:

| Yakıt Tipi        | Uygunluk       | Dikkat Noktası                      |
|--------------------|----------------|-------------------------------------|
| Doğalgaz           | En uygun       | Fiyat volatilitesi, arz güvenliği   |
| Biyokütle          | Uygun (teşvik) | Tedarik sürekliliği, depolama       |
| Kömür              | Uygun (büyük)  | Emisyon sınırları, CBAM riski       |
| Atık yakıt (RDF)   | Özel değerlendir| Lisans, emisyon, kalori değişkenliği|
| Proses atık gazı   | Çok uygun      | Mevcut ise öncelikli değerlendir    |

Yakıt arz güvenliği kontrol listesi:
□ Uzun vadeli tedarik sözleşmesi (>10 yıl)
□ Alternatif tedarikçi mevcudiyeti
□ Yakıt depolama kapasitesi (minimum 7 gün)
□ Taşıma altyapısı (boru hattı, karayolu, demiryolu)
□ Fiyat formülü ve escalasyon mekanizması
```

## 2. Ekonomik Değerlendirme (Economic Evaluation)

### 2.1 Yatırım Maliyeti Tahmini (CAPEX Estimation)

```
CHP yatırım bileşenleri:

| Bileşen                               | Pay [%] | Birim Maliyet               |
|----------------------------------------|---------|------------------------------|
| Türbin + jeneratör                     | 30-40   | 400-1,200 EUR/kW_e          |
| Kazan (yeni veya modifikasyon)         | 15-25   | 50-120 EUR/kW_th            |
| Elektrik bağlantı (trafo, pano, koruma)| 8-12    | 30-80 EUR/kW_e              |
| Boru tesisatı ve yardımcı ekipman      | 8-12    | —                            |
| Kontrol ve otomasyon (DCS/PLC)         | 5-8     | —                            |
| İnşaat ve montaj                       | 10-15   | —                            |
| Mühendislik ve proje yönetimi          | 5-8     | —                            |
| Komisyonlama ve devreye alma           | 2-4     | —                            |

Toplam birim yatırım maliyeti (Türkiye, 2025-2026):
- Karşı basınçlı türbin CHP (1-5 MW): 800-1,500 EUR/kW_e
- Karşı basınçlı türbin CHP (5-20 MW): 600-1,000 EUR/kW_e
- Gaz türbini CHP (1-10 MW): 1,000-1,800 EUR/kW_e
- Gaz motoru CHP (0.5-5 MW): 900-1,500 EUR/kW_e
```

### 2.2 İşletme Maliyeti (OPEX)

```
Yıllık işletme giderleri:

| Kalem                          | Tipik Değer                    |
|--------------------------------|--------------------------------|
| Yakıt maliyeti                 | %65-80 toplam OPEX             |
| Bakım ve onarım               | 0.3-0.8 EUR-ct/kWh_e          |
| Personel (ek operatör)         | 1-3 kişi x 25,000-40,000 EUR  |
| Sigorta                        | %0.5-1.0 CAPEX/yıl            |
| Yedek parça stoğu              | %1-2 CAPEX/yıl                |
| Su ve kimyasal (DM su, vb.)   | 0.5-2.0 EUR/ton buhar         |
| Çevresel uyum (emisyon izleme) | 5,000-20,000 EUR/yıl          |
```

### 2.3 Net Bugünkü Değer Hesabı (NPV Calculation)

```
CHP projesi NPV hesaplama:

NPV = -C₀ + Σᵢ₌₁ⁿ [(R_elek,i + R_ısı,i - C_yakıt,i - C_opex,i) / (1 + r)ⁱ]

Burada:
- C₀ = Toplam başlangıç yatırımı [EUR]
- R_elek,i = Yıl i elektrik geliri/tasarrufu [EUR]
  = Ẇ_elek × t_çalışma × p_elektrik
- R_ısı,i = Yıl i ısı geliri/tasarrufu [EUR]
  = Q̇_ısı × t_çalışma × p_ısı (kazan yakıt tasarrufu)
- C_yakıt,i = Yıl i yakıt maliyeti [EUR]
- C_opex,i = Yıl i diğer işletme giderleri [EUR]
- r = İskonto oranı
- n = Proje ekonomik ömrü [yıl] (genellikle 15-25 yıl)

Karar: NPV > 0 ise proje değer yaratır.
```

### 2.4 İç Verim Oranı (IRR — Internal Rate of Return)

```
IRR: NPV = 0 yapan iskonto oranıdır.

CHP projeleri için tipik IRR değerleri:
| Proje Tipi                         | IRR [%]    | Değerlendirme |
|------------------------------------|------------|---------------|
| PRV → mikro türbin ikamesi         | 20-45      | Mükemmel      |
| Karşı basınçlı türbin CHP (yeni)  | 12-25      | İyi           |
| Çekişli türbin CHP (yeni)         | 10-20      | Kabul edilebilir |
| Gaz türbini CHP                    | 12-22      | İyi           |
| ORC atık ısı geri kazanımı        | 10-20      | Kabul edilebilir |

Minimum kabul edilebilir getiri oranı (MARR — Türkiye):
- Düşük risk projeleri: %12-15
- Orta risk projeleri: %15-20
- Yüksek risk projeleri: %20-25
```

### 2.5 Basit Geri Ödeme Süresi (SPP — Simple Payback Period)

```
SPP = C₀ / S_net_yıllık [yıl]

Burada:
S_net_yıllık = R_elek + R_ısı - C_yakıt - C_opex [EUR/yıl]

CHP projeleri için SPP hedefleri:
| SPP Aralığı | Değerlendirme      | Aksiyon                    |
|--------------|--------------------|----------------------------|
| <3 yıl       | Mükemmel           | Hemen uygula               |
| 3-5 yıl      | İyi                | Normal yatırım süreci      |
| 5-7 yıl      | Kabul edilebilir   | Stratejik değerlendirme    |
| 7-10 yıl     | Marjinal           | Teşvik/finansman araştır   |
| >10 yıl      | Ekonomik değil     | Reddet veya kapsam değiştir|
```

### 2.6 Hesaplama Örneği

```
Senaryo: 5 MW_e karşı basınçlı buhar türbini CHP

Teknik parametreler:
- Türbin gücü: 5 MW_e
- Proses ısısı: 35 MW_th (HPR = 7.0)
- Çalışma: 7,000 h/yıl
- Yakıt: Doğalgaz, kazan verimi %88

Yatırım:
C₀ = 5,000 × 900 = 4,500,000 EUR

Yıllık gelirler:
R_elek = 5,000 × 7,000 × 0.095 = 3,325,000 EUR/yıl
R_ısı = CHP ile kazan yakıt tasarrufu = 0 (mevcut kazan devam)
Not: Buhar türbini CHP'de mevcut kazandan yüksek basınçlı buhar
     üretilir, türbinden geçerek prosese gider. Ek yakıt
     maliyeti kazan yükü artışından kaynaklanır.

Yıllık ek yakıt maliyeti:
Q_ek_yakıt = Ẇ_elek / η_elek,CHP = 5,000 / 0.20 = 25,000 kW
Ek gaz: 25,000 × 7,000 / (10.33 × 1,000) = 16,942 Nm³/yıl (YANLIŞ)

Doğru hesap:
Ek buhar üretimi enerji karşılığı:
ṁ × (h_giriş - h_çıkış) = 5,000 kW → ṁ = 14.26 kg/s (formulas.md'den)
Ek kazan yükü: ṁ × (h_giriş - h_feedwater) / η_kazan
= 14.26 × (3,214 - 335) / 0.88 = 46,663 kW
Ek yakıt: 46,663 × 7,000 × 3.6 / (34,500 × 1,000) = 34,084 Nm³ (YANLIŞ birim)

Basitleştirilmiş yaklaşım:
Ek yakıt maliyeti = 46,663 × 7,000 / (10,330) × 0.32
                  = 46,663 × 7,000 / 10,330 × 0.32
                  = 31,627 × 0.32 = zaten buharı mevcut kazan üretiyor

DÜZELTME — Doğru yaklaşım:
Mevcut sistemde PRV ile basınç düşürme: Yakıt maliyeti aynı
CHP farkı: Türbin gücü = Ek gelir, ek yakıt = 0
Net yıllık tasarruf:
S_net = R_elek - C_bakım - C_diğer
      = 3,325,000 - (0.005 × 35,000,000) - 50,000
      = 3,325,000 - 175,000 - 50,000 = 3,100,000 EUR/yıl

SPP = 4,500,000 / 3,100,000 = 1.45 yıl
NPV (15 yıl, %12) = -4,500,000 + 3,100,000 × 6.811 = 16,614,100 EUR
IRR > %50

Not: Bu senaryo mevcut PRV ikamesi içindir (ek yakıt gerekmez).
Yeni tesis için ayrıca kazan yakıt maliyeti eklenir ve SPP uzar.
```

## 3. Hassasiyet Analizi (Sensitivity Analysis)

### 3.1 Yakıt Fiyatı Hassasiyeti

```
Doğalgaz fiyat değişiminin CHP ekonomisine etkisi:

Baz senaryo: p_gaz = 0.32 EUR/Nm³

| Gaz Fiyatı [EUR/Nm³] | Değişim [%] | Yıllık Yakıt Maliyeti [EUR] | NPV Etkisi [%] |
|------------------------|-------------|------------------------------|-----------------|
| 0.22                   | -31         | Düşük                        | +25-35          |
| 0.27                   | -16         | Orta-düşük                   | +12-18          |
| 0.32 (baz)             | 0           | Referans                     | 0               |
| 0.37                   | +16         | Orta-yüksek                  | -12-18          |
| 0.42                   | +31         | Yüksek                       | -25-35          |

Kural: CHP projeleri yakıt fiyatına yüksek duyarlıdır.
Doğalgaz fiyatı %10 artarsa, CHP NPV'si %10-20 düşer
(sadece elektrik üretim modunda).
```

### 3.2 Elektrik Fiyatı Hassasiyeti

```
Elektrik fiyatının CHP getirisine etkisi:

Baz senaryo: p_elek = 0.095 EUR/kWh

| Elektrik Fiyatı [EUR/kWh] | Değişim [%] | Yıllık Gelir [EUR] | SPP [yıl] |
|----------------------------|-------------|---------------------|-----------|
| 0.070                      | -26         | 2,450,000           | 1.84      |
| 0.080                      | -16         | 2,800,000           | 1.61      |
| 0.095 (baz)               | 0           | 3,325,000           | 1.45      |
| 0.110                      | +16         | 3,850,000           | 1.17      |
| 0.130                      | +37         | 4,550,000           | 0.99      |

Kural: CHP getirileri elektrik fiyatıyla doğru orantılıdır.
Elektrik/gaz fiyat oranı (spark spread) kritik göstergedir.
Spark spread = p_elek - (p_gaz / η_elek) [EUR/kWh]
```

### 3.3 Yük Faktörü Hassasiyeti

```
Çalışma saati ve yük faktörünün etkisi:

| Çalışma Saati [h/yıl] | Yük Faktörü [%] | Yıllık Üretim [MWh] | SPP [yıl] | IRR [%] |
|------------------------|------------------|----------------------|-----------|---------|
| 4,000                  | 46               | 20,000               | 2.54      | 35      |
| 5,000                  | 57               | 25,000               | 2.03      | 43      |
| 6,000                  | 68               | 30,000               | 1.69      | 53      |
| 7,000 (baz)           | 80               | 35,000               | 1.45      | >55     |
| 8,000                  | 91               | 40,000               | 1.27      | >60     |

Not: 4,000 h altında IRR hızla düşer, 3,000 h altında
çoğu CHP projesi ekonomik olmaz.
```

### 3.4 Tornado Diyagramı Özeti

```
Hassasiyet sıralaması (en duyarlıdan en az duyarlıya):

1. Elektrik fiyatı        ████████████████████  En yüksek etki
2. Çalışma saati           ██████████████████    Yüksek etki
3. Yakıt fiyatı            ████████████████      Yüksek etki (yeni tesis)
4. Yatırım maliyeti        ██████████            Orta etki
5. Bakım maliyeti          █████                 Düşük etki
6. İskonto oranı           ████                  Düşük etki

Kritik değişkenler: Elektrik fiyatı, çalışma saati, yakıt fiyatı
Kontrol edilebilir: Bakım maliyeti, yatırım maliyeti (teklif pazarlığı)
Kontrol edilemez: Enerji fiyatları, döviz kuru, mevzuat
```

## 4. Risk Değerlendirme (Risk Assessment)

### 4.1 Teknik Riskler

```
| Risk                               | Olasılık | Etki   | Azaltma Yöntemi                   |
|------------------------------------|----------|--------|------------------------------------|
| Türbin performans düşüklüğü       | Orta     | Orta   | Garanti performans testi, PTC 6    |
| Kazan kapasitesi yetersizliği      | Düşük    | Yüksek | Detaylı enerji ölçümü              |
| Termal talep değişimi              | Orta     | Yüksek | Çok yıllık veri analizi            |
| Grid bağlantı sorunları           | Düşük    | Yüksek | Ön fizibilite, dağıtım şirketiyle |
| Buhar kalitesi sorunları           | Düşük    | Orta   | Su kimyası programı                |
| Gürültü ve titreşim                | Düşük    | Düşük  | Akustik tasarım, temel izolasyonu  |
```

### 4.2 Ekonomik Riskler

```
| Risk                               | Olasılık | Etki   | Azaltma Yöntemi                   |
|------------------------------------|----------|--------|------------------------------------|
| Enerji fiyat düşüşü               | Orta     | Yüksek | Hassasiyet analizi, hedge          |
| Döviz kuru dalgalanması            | Yüksek   | Orta   | EUR cinsinden sözleşme             |
| Enflasyon artışı                   | Yüksek   | Orta   | Reel bazlı analiz                  |
| Beklenenden yüksek CAPEX           | Orta     | Orta   | %10-15 beklenmedik gider payı      |
| Üretim düşüşü (talep kaybı)       | Orta     | Yüksek | Esnek boyutlandırma                |
| Ek yakıt maliyeti artışı           | Orta     | Yüksek | Çift yakıt sistemi düşün           |
```

### 4.3 Mevzuat ve Düzenleyici Riskler

```
| Risk                               | Olasılık | Etki   | Azaltma Yöntemi                   |
|------------------------------------|----------|--------|------------------------------------|
| Tarife değişikliği (EPDK)          | Yüksek   | Yüksek | Senaryo analizi, serbest tüketici  |
| Emisyon sınırı sıkılaşması        | Orta     | Orta   | Temiz yakıt, SCR/SNCR hazırlığı   |
| Lisans gereksinimleri değişimi     | Düşük    | Orta   | Hukuki danışmanlık                 |
| CBAM / karbon fiyatlaması          | Yüksek   | Orta   | Yüksek verimli CHP sertifikası    |
| Teşvik programı sonlanması         | Orta     | Düşük  | Teşviki NPV'ye dahil etme         |
```

## 5. Fizibilite Raporu Yapısı (Feasibility Report Structure)

```
Fizibilite raporu standart bölümleri:

1. Yönetici Özeti (Executive Summary)
   - Proje tanımı, boyut, yatırım
   - Temel ekonomik göstergeler (NPV, IRR, SPP)
   - Tavsiye kararı

2. Teknik Değerlendirme
   - Mevcut enerji sistemi analizi
   - Termal ve elektrik yük profili
   - CHP konfigürasyon seçenekleri
   - Seçilen konfigürasyon ve boyutlandırma
   - Enerji dengesi ve exergy analizi

3. Ekonomik Değerlendirme
   - CAPEX tahmini (±%15 doğruluk)
   - OPEX projeksiyonu (25 yıl)
   - Gelir projeksiyonu
   - NPV, IRR, SPP, DPP sonuçları

4. Hassasiyet ve Risk Analizi
   - Tek değişken hassasiyet tabloları
   - Monte Carlo simülasyonu (isteğe bağlı)
   - Risk matrisi ve azaltma planı

5. Mevzuat ve Lisanslama
   - EPDK gereksinimler
   - Çevre izinleri
   - Şebeke bağlantı koşulları

6. Uygulama Planı
   - Zaman çizelgesi (tipik 18-36 ay)
   - Tedarik stratejisi
   - İşletme organizasyonu

7. Ekler
   - Detaylı hesaplamalar
   - Teklif mektupları
   - Ölçüm verileri
```

## 6. Karar Kriterleri Tablosu (Decision Criteria Matrix)

```
CHP fizibilite karar matrisi:

| Kriter                    | Ağırlık [%] | Eşik Değer       | Puan (1-5)        |
|---------------------------|-------------|-------------------|-------------------|
| NPV                       | 25          | >0 EUR            | 5: NPV/C₀ > 2.0  |
|                           |             |                   | 4: NPV/C₀ = 1-2  |
|                           |             |                   | 3: NPV/C₀ = 0.5-1|
|                           |             |                   | 2: NPV/C₀ = 0-0.5|
|                           |             |                   | 1: NPV < 0        |
| IRR                       | 20          | >MARR             | 5: IRR > %30      |
|                           |             |                   | 3: IRR = %15-30   |
|                           |             |                   | 1: IRR < %15      |
| SPP                       | 15          | <7 yıl            | 5: SPP < 3 yıl    |
|                           |             |                   | 3: SPP = 3-5 yıl  |
|                           |             |                   | 1: SPP > 7 yıl    |
| Teknik uygunluk           | 15          | Puan > 3          | 5: İdeal koşullar |
|                           |             |                   | 3: Uygun koşullar |
|                           |             |                   | 1: Zorlayıcı      |
| Risk seviyesi             | 10          | Düşük-orta        | 5: Düşük risk     |
|                           |             |                   | 3: Orta risk      |
|                           |             |                   | 1: Yüksek risk    |
| Stratejik uyum            | 10          | Olumlu            | 5: Tam uyumlu     |
|                           |             |                   | 3: Kısmen uyumlu  |
|                           |             |                   | 1: Uyumsuz        |
| Çevresel fayda            | 5           | CO₂ azaltma > 0   | 5: >%20 azaltma   |
|                           |             |                   | 3: %5-20 azaltma  |
|                           |             |                   | 1: <% 5 azaltma   |

Toplam puan değerlendirmesi:
- ≥ 4.0: Kesinlikle uygulanabilir — Yatırım önerilir
- 3.0-3.9: Uygulanabilir — Detaylı mühendislik aşamasına geç
- 2.0-2.9: Marjinal — Koşullu kabul, koşullar izlensin
- < 2.0: Uygulanabilir değil — Reddet
```

## İlgili Dosyalar

- [Formüller](../formulas.md) — CHP exergy ve verim hesaplama formülleri
- [Benchmarklar](../benchmarks.md) — Türbin ve CHP verimlilik karşılaştırma verileri
- [CHP Sistemleri](../systems/steam_turbine_chp.md) — Buhar türbini CHP konfigürasyonları
- [Tarife ve Piyasa](feed_in_tariff.md) — Türkiye elektrik piyasası ve düzenleyici çerçeve
- [Finansman](financing.md) — Finansman modelleri ve teşvikler
- [Fabrika Ekonomik Analiz](../../factory/economic_analysis.md) — NPV, IRR, SPP yatırım metodolojisi
- [Enerji Fiyatlandırma](../../factory/energy_pricing.md) — Tarife yapıları ve enerji maliyetleri
- [Boyutlandırma Rehberi](../solutions/sizing_guide.md) — Türbin boyutlandırma metodolojisi
- [Yük Eşleştirme](../solutions/load_matching.md) — Termal ve elektrik yük eşleştirme

## Referanslar

- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition.
- US DOE (2016). *Combined Heat and Power Technology Fact Sheet Series*.
- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration."
- ASHRAE (2020). *ASHRAE Handbook — HVAC Systems and Equipment*, Chapter 7: Combined Heat and Power Systems.
- EPA (2017). *Catalog of CHP Technologies*, U.S. Environmental Protection Agency.
- IEA (2022). *Energy Efficiency — CHP/DHC Country Scorecards*.
- Thumann, A. & Younger, W. (2012). *Handbook of Energy Audits*, 9th Edition, Fairmont Press.
- EPDK, "Elektrik Piyasası Lisans Yönetmeliği" ve ilgili tebliğler.
- Fuller, S.K. & Petersen, S.R. (1996). *Life-Cycle Costing Manual*, NIST Handbook 135.
