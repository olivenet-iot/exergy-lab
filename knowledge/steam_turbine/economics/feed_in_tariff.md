---
title: "Türkiye Elektrik Piyasası ve Düzenleyici Çerçeve — Turkey Electricity Market and Regulatory Framework"
category: economics
equipment_type: steam_turbine
keywords: [elektrik piyasası, EPDK, YEKDEM, CHP sertifikası, şebeke satışı, öz tüketim, lisanssız üretim, tarife, serbest tüketici, 6446 sayılı kanun]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/economics/feasibility.md, factory/economic_analysis.md, factory/energy_pricing.md]
use_when: ["CHP üretim fazlası elektrik satışı değerlendirilirken", "Lisans ve mevzuat gereksinimleri araştırılırken", "Türkiye elektrik tarifeleri analiz edilirken", "Yüksek verimli CHP sertifikası gerektiğinde"]
priority: low
last_updated: 2026-01-31
---
# Türkiye Elektrik Piyasası ve Düzenleyici Çerçeve — Turkey Electricity Market and Regulatory Framework

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu dosya, Türkiye'de endüstriyel CHP/buhar türbini projelerinin elektrik piyasası perspektifinden değerlendirilmesini kapsar. Öz tüketim (self-consumption) ve şebeke satışı (grid export) seçenekleri, EPDK düzenlemeleri, lisans gereksinimleri, yüksek verimli CHP sertifikası ve tarife yapıları ele alınmaktadır.

## 1. Öz Tüketim vs. Şebeke Satışı (Self-Consumption vs. Grid Export)

### 1.1 Öz Tüketim Modeli

```
Öz tüketim (self-consumption):
- CHP tarafından üretilen elektriğin tamamı tesis içinde tüketilir
- Şebekeye satış yapılmaz
- En basit düzenleyici yapı (lisanssız üretim yeterli, <1 MW için)

Avantajlar:
+ Şebeke satış fiyatından bağımsız
+ Tarife değişiklik riskinden korunaklı
+ Dağıtım ve iletim bedeli tasarrufu
+ Basit lisans süreci
+ Arz güvenliği (kesintilere karşı koruma)

Dezavantajlar:
- Üretim fazlası elektrik kaybı (curtailment)
- Tüketim profili ile üretim uyumu gerekli
- Yatırım kapasitesi tüketime sınırlı

Ekonomik değerlendirme:
Öz tüketim tasarrufu = Ẇ_elek × t × p_tüketim_fiyatı [EUR/yıl]

Burada p_tüketim_fiyatı: Şebekeden alınan toplam birim maliyet
(enerji + dağıtım + iletim + vergi + fon)
Tipik: 0.090-0.130 EUR/kWh (OG sanayi)
```

### 1.2 Şebeke Satışı Modeli (Grid Export)

```
Şebeke satışı modeli:
- CHP tarafından üretilen fazla elektrik şebekeye verilir
- Üretim lisansı gerektirir (>1 MW)
- Piyasa fiyatı veya ikili anlaşma ile satış

Satış kanalları:
1. EPIAS Gün Öncesi Piyasası (Day-Ahead Market — DAM)
   - Saatlik fiyat belirleme
   - Ortalama fiyat: 0.050-0.080 EUR/kWh (değişken)

2. EPIAS Gün İçi Piyasası (Intra-Day Market — IDM)
   - Gün içi fiyat düzeltme

3. İkili Anlaşmalar (Bilateral Contracts)
   - Tedarikçi firma ile uzun vadeli sözleşme
   - Daha öngörülebilir gelir akışı
   - Fiyat: Piyasa ortalamasına yakın, ±%5-10

4. Dengeleme Güç Piyasası (Balancing Power Market)
   - Sistem dengeleme hizmeti
   - Daha yüksek fiyatlar ama düzensiz gelir

Kritik fark:
Öz tüketim birim değeri: 0.090-0.130 EUR/kWh
Şebeke satış birim değeri: 0.050-0.080 EUR/kWh
Fark: ~0.030-0.060 EUR/kWh (dağıtım/iletim/vergi bileşenleri)
→ Öz tüketim her zaman şebeke satışından daha değerlidir
```

### 1.3 Hibrit Model (Net Metering Alternatifi)

```
Hibrit model (öz tüketim + fazla satış):
- Üretimin büyük kısmı (%70-90) öz tüketim
- Fazla üretim (%10-30) şebekeye satış
- En yaygın endüstriyel CHP modeli

Boyutlandırma kuralı:
CHP kapasitesi ≤ Minimum baz elektrik yükü
→ Öz tüketim oranını maksimize eder
→ Şebeke satışını minimumda tutar

Örnek:
Fabrika elektrik profili:
- Baz yük: 2,000 kW (sürekli)
- Ortalama yük: 3,000 kW
- Pik yük: 4,500 kW

CHP boyutu: 2,000 kW_e (baz yüke eşit)
Öz tüketim oranı: ~%95
Fazla satış: ~%5 (düşük yük saatlerinde)
```

## 2. YEKDEM ve Yenilenebilir Enerji Destekleri

### 2.1 YEKDEM (Yenilenebilir Enerji Kaynakları Destekleme Mekanizması)

```
YEKDEM — temel bilgiler:
- 6446 sayılı Elektrik Piyasası Kanunu kapsamında
- Yenilenebilir enerji kaynaklarına alım garantisi
- Biyokütle bazlı CHP projeleri yararlanabilir
- Doğalgaz bazlı CHP YEKDEM kapsamında DEĞİLDİR

YEKDEM fiyatları (2025-2026 güncel):
| Kaynak          | Alım Garantisi [EUR-ct/kWh] | Süre   | Not               |
|-----------------|------------------------------|--------|--------------------|
| Biyokütle       | 5.5-8.0*                     | 10 yıl | Tesis boyutuna bağlı|
| Biyogaz         | 5.5-8.0*                     | 10 yıl | Çöp gazı dahil     |
| Jeotermal       | 5.5-7.0*                     | 10 yıl |                    |
| Rüzgar          | 3.5-5.5*                     | 10 yıl | YEKA ihaleleri     |
| Güneş           | 3.0-5.0*                     | 10 yıl | YEKA ihaleleri     |

*Fiyatlar YEKA ihale sonuçlarına ve güncel EPDK düzenlemelerine
göre değişiklik gösterebilir. Yerli aksam katkı ilaveleri ayrıca.

CHP için önemli:
- Biyokütle/biyogaz yakıtlı CHP: YEKDEM kapsamında
- Doğalgaz CHP: YEKDEM kapsamı dışında, piyasa fiyatı ile satış
- Atık ısı (waste heat) → ORC: Duruma göre değerlendirilir
```

### 2.2 Biyokütle CHP ve YEKDEM

```
Biyokütle CHP YEKDEM avantajları:
1. Sabit alım garantisi (10 yıl)
2. Yerli aksam katkı ilavesi
3. Öncelikli şebeke bağlantı hakkı
4. Dengeleme yükümlülüğü muafiyeti (belirli kapasiteye kadar)

Biyokütle CHP fizibilite etkisi:
Baz senaryo (doğalgaz CHP, 5 MW_e):
- Satış fiyatı: 0.065 EUR/kWh (piyasa)
- Yıllık gelir: 5,000 × 7,000 × 0.065 = 2,275,000 EUR

Biyokütle CHP (5 MW_e, YEKDEM):
- Satış fiyatı: 0.075 EUR/kWh (YEKDEM)
- Yıllık gelir: 5,000 × 7,000 × 0.075 = 2,625,000 EUR
- Fark: +350,000 EUR/yıl
- Ek avantaj: 10 yıl fiyat garantisi (risk azaltma)
```

## 3. EPDK Düzenlemeleri (EPDK Regulations)

### 3.1 Elektrik Piyasası Kanunu (Kanun No: 6446)

```
6446 Sayılı Elektrik Piyasası Kanunu — CHP ile ilgili hükümler:

Temel ilkeler:
- Serbest piyasa yapısı (üretim, iletim, dağıtım, satış ayrımı)
- Rekabetçi piyasa ortamı
- Tüketici seçim hakkı
- Arz güvenliği

CHP özel hükümler:
- Otoprodüktör lisansı: Kendi tüketimi için üretim
- Üretim lisansı: Şebekeye satış için üretim
- Lisanssız üretim: <1 MW kurulu güç (yönetmelik kapsamı)
- Yüksek verimli CHP teşvikleri
```

### 3.2 Lisans Gereksinimleri

```
Lisans türleri ve kapsamları:

1. Lisanssız Üretim (<1 MW):
   - EPDK lisansı gerekmez
   - Dağıtım şirketi başvurusu yeterli
   - Bağlantı anlaşması + sistem kullanım anlaşması
   - Basit prosedür, süre: 3-6 ay
   - İlan bedeli: Yok

2. Otoprodüktör Lisansı:
   - Kendi ihtiyacı için üretim
   - Fazla üretimi piyasaya satabilir (%50'ye kadar)
   - Lisans süresi: 49 yıl (yenilenebilir)
   - Başvuru süreci: 6-12 ay

3. Üretim Lisansı (>1 MW):
   - Tam kapsamlı üretim ve satış hakkı
   - Detaylı fizibilite raporu gerekli
   - ÇED (Çevresel Etki Değerlendirmesi) gerekebilir
   - Lisans süresi: 49 yıl
   - Başvuru süreci: 12-24 ay

Lisans başvuru evrakları:
□ Fizibilite raporu
□ Ön proje (single line diagram, yerleşim planı)
□ ÇED kararı veya ÇED gerekli değildir belgesi
□ İmar durumu ve yapı izni
□ Bağlantı görüşü (TEİAŞ veya dağıtım şirketi)
□ Mali yeterlilik belgeleri
□ Tüzel kişilik belgeleri
```

## 4. Yüksek Verimli CHP Sertifikası (High-Efficiency CHP Certification)

### 4.1 EU 2012/27 Uyumlu Tanım

```
Yüksek verimli CHP tanımı (EU Energy Efficiency Directive 2012/27):

Birincil Enerji Tasarrufu (PES — Primary Energy Savings):
PES = 1 - 1 / (η_elek,CHP/η_elek,ref + η_ısı,CHP/η_ısı,ref)

Yüksek verimli CHP kriteri: PES ≥ %10

Referans verimler (harmonize değerler):
| Yakıt          | η_elek,ref [%] | η_ısı,ref (buhar) [%] | η_ısı,ref (sıcak su) [%] |
|----------------|----------------|------------------------|---------------------------|
| Doğalgaz       | 52.5           | 90                     | 92                        |
| Fuel oil       | 44.2           | 89                     | 91                        |
| Kömür          | 44.2           | 88                     | 90                        |
| Biyokütle      | 33.0           | 86                     | 88                        |

Not: Referans verimler AB Delegated Regulation ile periyodik güncellenir.
Düzeltme faktörleri: İklim, yıl, otokonsumasyon oranı.
```

### 4.2 PES Hesaplama Örneği

```
Senaryo: Doğalgaz bazlı buhar türbini CHP

CHP performansı:
- η_elek,CHP = %20 (net elektrik verimi)
- η_ısı,CHP = %65 (ısı verimi, buhar)
- η_toplam = %85

PES hesaplama:
PES = 1 - 1 / (0.20/0.525 + 0.65/0.90)
    = 1 - 1 / (0.381 + 0.722)
    = 1 - 1 / 1.103
    = 1 - 0.907
    = %9.3

Sonuç: PES = %9.3 < %10 → Yüksek verimli CHP şartını SAĞLAMIYOR

İyileştirme senaryosu (daha yüksek elektrik verimi):
η_elek,CHP = %22, η_ısı,CHP = %63
PES = 1 - 1 / (0.22/0.525 + 0.63/0.90)
    = 1 - 1 / (0.419 + 0.700)
    = 1 - 1 / 1.119
    = %10.6 → Yüksek verimli CHP ✓

Kural: Buhar türbini CHP'de PES ≥ %10 sağlamak için
elektrik verimi kritiktir. Düşük HPR (daha fazla elektrik)
PES'i artırır.
```

### 4.3 Sertifika Avantajları

```
Yüksek verimli CHP sertifikası avantajları:

1. Enerji verimliliği teşvikleri:
   - VAP (Verimlilik Arttırıcı Proje) desteği kapsamına girer
   - Yatırım desteği: %20-30 hibe (VAP)

2. Şebeke bağlantı önceliği:
   - Dağıtım şebekesine bağlantıda öncelik

3. Dağıtım bedeli indirimi:
   - Yüksek verimli CHP üretimi için dağıtım bedeli
     indirimli uygulanabilir (EPDK kararına bağlı)

4. CBAM avantajı:
   - Yüksek verimli CHP sertifikası, AB'ye ihraç edilen
     ürünlerin karbon ayak izini azaltır
   - CBAM beyanında CHP verimliliği dikkate alınır

5. ISO 50001 ve enerji yönetimi:
   - CHP sertifikası, enerji yönetim sistemi
     performans göstergesi olarak kullanılır

6. Kurumsal sürdürülebilirlik:
   - ESG raporlamada olumlu etki
   - CDP (Carbon Disclosure Project) puanlamasına katkı
```

## 5. Türkiye Elektrik Tarifeleri (Turkey Electricity Tariffs)

### 5.1 Tarife Tipleri

```
Türkiye elektrik tarife yapısı:

1. Düzenlemeye Tabi Tarife (Regulated Tariff):
   - EPDK tarafından belirlenir
   - Serbest olmayan tüketiciler için
   - Tek zamanlı veya çok zamanlı seçeneği

2. Serbest Tüketici Tarifesi (Eligible Consumer):
   - Yıllık tüketim eşiği: >1,400 kWh (2025, EPDK güncellenebilir)
   - Pratikte tüm endüstriyel tüketiciler serbest tüketici
   - Tedarikçi firma ile serbest pazarlık
   - Son kaynak tarifesi: Güvence mekanizması

3. Çok Zamanlı Tarife (Time-of-Use — TT):
   - Gece (T1): 22:00-06:00 → En düşük fiyat
   - Gündüz (T2): 06:00-17:00 → Orta fiyat
   - Puant (T3): 17:00-22:00 → En yüksek fiyat
   - CHP üretim planlaması için kritik

4. OSB Tarifesi:
   - Organize Sanayi Bölgesi özel tarife
   - Genellikle düzenlemeye tabi tarifeden düşük
   - OSB kendi iç dağıtımını yapar
```

### 5.2 CHP İçin Tarife Optimizasyonu

```
CHP üretiminin tarife etkisi:

Senaryo: 3 MW_e CHP, 7,000 h/yıl çalışma

Öz tüketim tasarrufu (çok zamanlı tarife):
| Dönem   | Saat     | CHP Üretim [MWh] | Tarife [EUR/kWh] | Tasarruf [EUR] |
|---------|----------|-------------------|-------------------|----------------|
| Gece    | 2,400 h  | 7,200             | 0.055             | 396,000        |
| Gündüz  | 3,200 h  | 9,600             | 0.090             | 864,000        |
| Puant   | 1,400 h  | 4,200             | 0.140             | 588,000        |
| TOPLAM  | 7,000 h  | 21,000            | ort: 0.088        | 1,848,000      |

Karşılaştırma — tek zamanlı tarife:
Tasarruf = 21,000 × 0.095 = 1,995,000 EUR (tek zamanlı daha yüksek)

Not: Çok zamanlı tarifede ortalama birim değer tek zamanlıdan düşük
olabilir. CHP sabit çalışırsa gece döneminin düşük fiyatı ortalamayı
düşürür. Tek zamanlı tarife CHP için avantajlı olabilir.

Optimizasyon stratejisi:
1. CHP gece durdurulabilir mi? (gece: düşük tarife, az fayda)
2. CHP puant saatte tam yükte çalışmalı (yüksek fayda)
3. Tarife seçimi: CHP ile tek zamanlı mı, çok zamanlı mı daha avantajlı?
```

## 6. Şebeke Bağlantı Prosedürü (Grid Connection Procedure)

### 6.1 Bağlantı Adımları

```
CHP şebeke bağlantı süreci:

Adım 1: Ön başvuru (1-2 ay)
- Dağıtım şirketine kapasite sorgusu
- Bağlantı noktası belirleme
- Teknik uygunluk ön değerlendirmesi

Adım 2: Kapasite tahsisi (2-4 ay)
- TEİAŞ/dağıtım şirketi kapasite tahsis onayı
- Bağlantı görüş yazısı
- Trafo merkezi ve hat kapasitesi kontrolü

Adım 3: Bağlantı anlaşması (1-2 ay)
- Teknik koşullar (koruma, ölçme, senkronizasyon)
- Bağlantı ücreti belirlenmesi
- Sistem kullanım anlaşması

Adım 4: Tesis kurulumu (12-24 ay)
- Türbin, jeneratör, trafo kurulumu
- Koruma sistemi (röle koordinasyonu)
- Ölçme sistemi (OSOS — Otomatik Sayaç Okuma)
- Senkronizasyon paneli

Adım 5: Geçici kabul ve devreye alma (2-4 ay)
- Dağıtım şirketi teknik kontrol
- Koruma testleri
- Geçici kabul belgesi
- 1 yıl izleme dönemi

Adım 6: Kesin kabul
- 1 yıl sonunda performans değerlendirmesi
- Kesin kabul belgesi

Toplam süre: 18-36 ay (başvurudan üretime)
```

### 6.2 Teknik Bağlantı Gereksinimleri

```
Şebeke bağlantı teknik şartları:

1. Koruma sistemi:
   - Aşırı/düşük gerilim koruma
   - Aşırı/düşük frekans koruma
   - Ters güç (reverse power) koruma
   - Ada modu algılama (anti-islanding)
   - Toprak arızası koruma

2. Güç kalitesi:
   - Gerilim regülasyonu: ±%5 nominal değer
   - Frekans: 50 Hz ±%1
   - Harmonik distorsiyon: THD < %5 (IEEE 519)
   - Flicker: IEC 61000-3-7 sınırları

3. Ölçme:
   - Çift yönlü sayaç (alış-veriş)
   - 15 dakikalık profil kayıt
   - OSOS entegrasyonu (uzaktan okuma)
   - Reaktif enerji ölçümü

4. Senkronizasyon:
   - Otomatik senkronizasyon ünitesi
   - Gerilim, frekans, faz açısı eşleştirme
   - Paralel çalışma kapasitesi
```

## 7. Lisanssız Üretim (<1 MW)

```
Lisanssız CHP üretimi (<1 MW kurulu güç):

Avantajlar:
+ EPDK üretim lisansı gerekmez
+ Basit başvuru süreci (dağıtım şirketi)
+ Daha kısa devreye alma süresi
+ Düşük bürokrasi maliyeti

Kapsam:
- Mikro türbin (PRV ikamesi): Tipik 50-500 kW → Lisanssız
- Küçük buhar türbini: 500-1,000 kW → Lisanssız
- Büyük türbin: >1,000 kW → Lisans gerekli

Prosedür:
1. Dağıtım şirketine başvuru
2. Bağlantı anlaşması
3. Kurulum ve devreye alma
4. Sistem kullanım anlaşması

Şebeke satışı:
- Lisanssız üretim fazlası şebekeye verilebilir
- Satış fiyatı: EPIAS piyasa takas fiyatı (PTF)
- Dağıtım bedeli indirimi uygulanabilir

Örnek: 300 kW PRV → mikro türbin ikamesi
- Lisans: Gerekmez
- Şebeke bağlantı: Mevcut bağlantı üzerinden
- Süre: 6-12 ay (başvurudan üretime)
- Öz tüketim: %100 (tüm üretim fabrika içi)
```

## 8. Dağıtım Bedeli İndirimi

```
CHP üretimi dağıtım bedeli etkisi:

Dağıtım bedeli yapısı:
- Dağıtım bedeli: ~0.010-0.020 EUR/kWh (kullanım bazlı)
- İletim bedeli: ~0.003-0.008 EUR/kWh
- Kayıp bedeli: ~0.005-0.010 EUR/kWh

CHP öz tüketim durumunda:
- Şebekeden çekiş azalır → Dağıtım + iletim + kayıp bedeli azalır
- Tasarruf: 0.018-0.038 EUR/kWh (öz tüketim kısmı)

Yüksek verimli CHP ilave indirimi:
- EPDK düzenlemesine bağlı olarak ek indirim uygulanabilir
- Güncel düzenlemeler için EPDK kararları kontrol edilmeli

Endüstriyel öz tüketim toplam birim fayda:
Enerji bedeli: 0.070-0.095 EUR/kWh
Dağıtım bedeli: 0.010-0.020 EUR/kWh
İletim bedeli: 0.003-0.008 EUR/kWh
Kayıp katkısı: 0.005-0.010 EUR/kWh
Vergi/fonlar: 0.005-0.012 EUR/kWh
TOPLAM: 0.093-0.145 EUR/kWh

Bu nedenle öz tüketim, piyasa fiyatından (0.050-0.080 EUR/kWh)
önemli ölçüde daha değerlidir.
```

## İlgili Dosyalar

- [Fizibilite](feasibility.md) — CHP fizibilite analizi ve ekonomik değerlendirme
- [Finansman](financing.md) — Finansman modelleri ve teşvikler
- [Formüller](../formulas.md) — PES, CHP verimlilik hesaplama formülleri
- [Benchmarklar](../benchmarks.md) — CHP performans karşılaştırma verileri
- [CHP Sistemleri](../systems/steam_turbine_chp.md) — Buhar türbini CHP konfigürasyonları
- [Fabrika Ekonomik Analiz](../../factory/economic_analysis.md) — NPV, IRR yatırım metodolojisi
- [Enerji Fiyatlandırma](../../factory/energy_pricing.md) — Tarife yapıları ve maliyet analizi
- [Kojenerasyon](../../factory/cogeneration.md) — CHP temelleri ve karşılaştırma

## Referanslar

- 6446 Sayılı Elektrik Piyasası Kanunu, T.C. Resmi Gazete, 2013.
- EPDK, "Elektrik Piyasası Lisans Yönetmeliği," güncel versiyon.
- EPDK, "Elektrik Piyasası Bağlantı ve Sistem Kullanım Yönetmeliği."
- EPDK, "Lisanssız Elektrik Üretimine İlişkin Yönetmelik."
- 5346 Sayılı Yenilenebilir Enerji Kaynaklarının Elektrik Enerjisi Üretimi Amaçlı Kullanımına İlişkin Kanun.
- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration."
- European Commission Delegated Regulation (EU) 2015/2402, "Harmonised Efficiency Reference Values."
- EPIAS (Enerji Piyasaları İşletme A.Ş.), "Piyasa Takas Fiyatı Verileri."
- TEİAŞ, "Türkiye Elektrik İletim Sistemi Bağlantı ve Sistem Kullanım Yönetmeliği."
- IEA (2022). *Energy Efficiency — CHP/DHC Country Scorecards*, International Energy Agency.
- OECD/IEA (2021). *Turkey Energy Policy Review*, OECD.
