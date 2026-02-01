---
title: "Kazan/Buhar Sistemi Enerji Denetimi Metodolojisi — Boiler/Steam System Energy Audit"
category: reference
equipment_type: boiler
keywords: [enerji denetimi, kazan, baca gazı, analiz]
related_files: [boiler/formulas.md, boiler/benchmarks.md, boiler/equipment/systems_overview.md]
use_when: ["Kazan enerji denetimi planlanırken", "Baca gazı analizi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Kazan/Buhar Sistemi Enerji Denetimi Metodolojisi — Boiler/Steam System Energy Audit

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu metodoloji, ASME PTC 4 "Fired Steam Generators" ve EN 12952/12953 standartlarına dayalı olarak kazan ve buhar sistemlerinin enerji verimliliği değerlendirmesi için 5 adımlı bir süreç tanımlar. Endüstriyel kazanlar, buhar dağıtım şebekeleri, kondensat geri dönüş hatları ve buhar kapanları dahil olmak üzere tüm buhar sistemi bileşenlerini kapsar.

## Standart Referanslar

| Standart | Açıklama |
|----------|----------|
| ASME PTC 4 | Fired Steam Generators — Performans test kodu |
| EN 12952 | Water-tube boilers — Su borulu kazanlar |
| EN 12953 | Shell boilers — Silindirik (ateş borulu) kazanlar |
| BS 845 | Methods for assessing thermal performance of boilers |
| ISO 50001:2018 | Energy management systems — Enerji yönetim sistemleri |
| ISO 50002:2014 | Energy audits — Requirements with guidance for use |
| ISO 14414 | Pump system assessment — Besleme suyu pompaları için |
| EN 12828 | Heating systems in buildings — Design |
| ASME PTC 19.10 | Flue and Exhaust Gas Analyses |

### Değerlendirme Seviyeleri

| Seviye | Açıklama | Kapsam |
|--------|----------|--------|
| Seviye 1 | Yürüyerek inceleme (walk-through) | Kalitatif, genel durum tespiti, fatura analizi |
| Seviye 2 | Detaylı değerlendirme | Kantitatif ölçümler, verimlilik hesabı, kayıp analizi |
| Seviye 3 | Kapsamlı değerlendirme | Tam enstrümantasyon, exergy analizi, uzun süreli izleme |

### Sistem Sınırları

1. **Yakıt girişi:** Yakıt depolama/beslemeden yanma odasına
2. **Kazan:** Yanma, ısı transferi, buhar üretimi
3. **Yardımcı ekipman:** Ekonomizer, ön ısıtıcı, besleme suyu pompası, fan
4. **Buhar dağıtım:** Ana hat, branş hatları, basınç düşürme istasyonları
5. **Buhar kapanları:** Kondensat tahliyesi ve geri dönüşü
6. **Kondensat sistemi:** Geri dönüş hatları, kondensat tankı, flash buhar geri kazanımı
7. **Talep tarafı:** Isı eşanjörleri, proses ekipmanları, kullanım noktaları

## Adım 1: Ön Hazırlık (Pre-Audit)

### 1.1 Toplanacak Bilgiler (En az 12 aylık)

| Kategori | Detay |
|----------|-------|
| Yakıt faturaları | Aylık yakıt tüketimi (m³, ton, lt), birim fiyat, toplam maliyet |
| Buhar üretim kayıtları | Aylık buhar üretimi (ton/ay), çalışma saatleri |
| Elektrik faturaları | Yardımcı ekipman (pompalar, fanlar) elektrik tüketimi |
| Bakım kayıtları | Servis geçmişi, boru/tüp değişimleri, korozyon raporları |
| Su arıtma kayıtları | Su kalitesi analizleri, kimyasal dozajlama, blöf miktarları |
| Ekipman datasheetleri | Kazan, brülör, ekonomizer, pompa nameplate bilgileri |
| P&ID diyagramları | Proses akış şeması, boru yerleşimi |
| Önceki denetim raporları | Varsa önceki verimlilik testleri ve denetimler |
| Emisyon ölçüm raporları | Periyodik baca gazı ölçüm sonuçları |
| Üretim programı | Vardiya düzeni, mevsimsel değişimler, duruş dönemleri |
| Su tüketim verileri | Şebeke suyu, yumuşatılmış su, deiyonize su |

### 1.2 Ön Görüşme Soruları (Tesis Yönetimine)

1. Kaç kazan kurulu? Tipleri, kapasiteleri ve yaşları?
2. Hangi yakıt(lar) kullanılıyor? İkincil yakıt imkanı var mı?
3. Tipik çalışma basıncı ve sıcaklığı? Kızgın buhar mı, doymuş buhar mı?
4. Buhar ne amaçla kullanılıyor (proses, ısıtma, güç üretimi)?
5. Ortalama ve pik buhar talebi ne kadar (ton/saat)?
6. Kondensat geri dönüş oranı nedir?
7. Son buhar kapanı taraması ne zaman yapıldı?
8. Su arıtma sistemi nasıl, blöf otomatik mi manuel mi?
9. Ekonomizer veya hava ön ısıtıcısı mevcut mu?
10. Baca gazı sürekli izleme sistemi var mı?
11. Bilinen izolasyon eksiklikleri veya buhar kaçakları var mı?
12. Kazan kontrol sistemi nasıl (on/off, modülasyon, O₂ trim)?
13. Son verimlilik testi ne zaman yapıldı?
14. Genişleme veya kapasite artırma planları var mı?

### 1.3 Denetim Ekipman Listesi

| Ekipman | Örnek Model | Amacı | Yaklaşık Maliyet |
|---------|-------------|-------|-----------------|
| Baca gazı analizörü | Testo 350, Kane 9206 | O₂, CO, CO₂, NOx, baca gazı sıcaklığı | €3,000-8,000 |
| IR termometre | Fluke 62 MAX+ | Yüzey sıcaklığı hızlı ölçüm | €50-150 |
| Termal kamera | FLIR E96, Testo 890 | Izolasyon kaybı, sıcak nokta tespiti | €5,000-20,000 |
| Yüzey sıcaklık probu | Testo kontak prob | Boru/vana yüzey sıcaklığı | €50-200 |
| Ultrasonik kalınlık ölçer | Olympus 38DL Plus | Boru/tüp et kalınlığı kontrolü | €2,000-5,000 |
| Güç analizörü | Fluke 435-II, Hioki PW3198 | Pompa/fan güç profilleme | €4,000-8,000 |
| Ultrasonik buhar kapanı test cihazı | SDT 270, UE UP100 | Buhar kapanı arıza tespiti | €2,000-6,000 |
| Akustik görüntüleme kamerası | Fluke ii910, FLIR Si124 | Buhar kaçağı görselleştirme | €15,000-30,000 |
| Veri kaydedici | Onset HOBO, Yokogawa | Uzun süreli T, P kayıt | €500-2,000 |
| Su kalitesi test kiti | Hach DR900 | pH, iletkenlik, sertlik, O₂ | €500-2,000 |
| Dijital manometre | Keller LEO 2 | Basınç ölçümü (0-25 bar) | €200-400 |
| Pitot tüpü / anemometre | Testo 480 | Yanma havası debisi | €500-1,500 |
| Kamera | Akıllı telefon/dijital | Durum belgeleme | — |

## Adım 2: Saha Çalışması (Field Work)

### 2.1 Kazan Envanteri

#### Her Kazan İçin Kaydedilecekler
- Üretici, model, seri numarası
- Kazan tipi (ateş borulu/su borulu/dökme dilimli)
- Nominal kapasite (ton/saat buhar veya MW termal)
- Çalışma basıncı (bar) ve sıcaklığı (°C)
- Yakıt tipi (doğalgaz, fuel oil, LPG, kömür, biyokütle)
- Brülör tipi ve modeli (on/off, yüksek-düşük, modülasyonlu)
- Üretim yılı
- Kontrol tipi (mekanik, PLC, DCS, O₂ trim)
- Çalışma saati (sayaçtan veya tahmini)
- Ekonomizer/hava ön ısıtıcı varlığı ve tipi
- Blöf sistemi (manuel/otomatik, sürekli/intermittent)

#### Her Yardımcı Ekipman İçin
- Besleme suyu pompası: güç (kW), debi (m³/h), basma yüksekliği (bar)
- Yanma havası fanı (FD fan): güç, debi
- Baca gazı fanı (ID fan): güç, debi
- Kondensat pompası: güç, debi
- Su arıtma sistemi: tip, kapasite

### 2.2 Baca Gazı Analizi (KRİTİK ÖLÇÜM)

#### Ölçüm Parametreleri
- O₂ konsantrasyonu (%)
- CO konsantrasyonu (ppm)
- CO₂ konsantrasyonu (%)
- NOx konsantrasyonu (ppm)
- SO₂ konsantrasyonu (ppm, kükürtlü yakıtlar için)
- Baca gazı sıcaklığı (°C)
- Ortam sıcaklığı (°C)
- İs sayısı (Bacharach, sıvı yakıtlar için)

#### Ölçüm Protokolü
1. Kazan en az 30 dakika kararlı rejimde çalışıyor olmalı
2. Ölçüm, baca gazı analizörü ile en az 3 farklı yükte yapılmalı:
   - Düşük yük (brülör minimum kapasitesi, ~%30)
   - Orta yük (~%60)
   - Tam yük (~%100)
3. Her yük seviyesinde en az 5 dakika stabil ölçüm
4. Ölçüm noktası: ekonomizer sonrası (varsa), bacaya girmeden önce
5. Ortam koşulları (sıcaklık, nem, basınç) kaydedilmeli
6. Tüm sonuçlar referans O₂ değerine (%3 kuru) normalize edilmeli

#### Hedef Değerler (Doğalgaz Yakıtlı Kazan)
| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| O₂ (%) | 1.5-3.0 | 3.0-5.0 | >5.0 |
| CO (ppm) | <50 | 50-200 | >200 |
| Baca gazı sıcaklığı (°C) | <150 | 150-200 | >200 |
| Fazla hava (%) | 8-15 | 15-30 | >30 |

### 2.3 Sıcaklık Ölçümleri

- Besleme suyu sıcaklığı (ekonomizer girişi)
- Ekonomizer çıkış suyu sıcaklığı
- Buhar sıcaklığı (kızgın buhar sistemlerinde)
- Blöf suyu sıcaklığı
- Kazan yüzey sıcaklıkları (termal kamera ile)
- Boru yüzey sıcaklıkları (izolasyonlu ve izolasyonsuz)
- Kondensat geri dönüş sıcaklığı
- Baca gazı sıcaklığı (farklı yüklerde)
- Yanma havası sıcaklığı
- Yakıt sıcaklığı (fuel oil sistemlerinde)

### 2.4 Basınç Ölçümleri

- Buhar ana hat basıncı (kazan çıkışı)
- Buhar dağıtım basıncı (çeşitli noktalarda)
- Basınç düşürme vanaları giriş/çıkış basıncı
- Besleme suyu basıncı
- Yakıt basıncı (gaz veya sıvı)
- Deaeratör çalışma basıncı
- Kondensat hat basıncı

### 2.5 Debi Ölçümleri

- Buhar debisi (sayaç okuması veya dolaylı hesaplama, ton/saat)
- Yakıt debisi (sayaç okuması veya fatura verisi, m³/saat veya kg/saat)
- Besleme suyu debisi (m³/saat)
- Blöf debisi (tahmin: iletkenlik oranı yöntemi)
- Kondensat geri dönüş debisi (m³/saat)
- Makyaj suyu debisi (m³/saat)

### 2.6 Buhar Kapanı Taraması (Steam Trap Survey)

#### Tarama Protokolü
1. Tüm buhar kapanlarının envanterini çıkar (konum, tip, boyut, basınç)
2. Her kapanı ultrasonik test cihazı ve/veya sıcaklık ölçümü ile kontrol et
3. Durumu sınıflandır:
   - **Çalışıyor (OK):** Normal çalışma
   - **Canlı buhar geçiriyor (Failed Open):** Sürekli buhar kaçağı — ACİL
   - **Tıkalı (Failed Closed):** Kondensat geçirmiyor — proses sorunu
   - **Belirsiz:** Tekrar kontrol gerekli
4. Her arızalı kapanın buhar kaybını tahmin et
5. Onarım/değişim önceliğini belirle

#### Buhar Kaybı Tahmini (Arızalı Kapan)

```
ṁ_kayıp = C_d × A_orifis × √(2 × ρ × ΔP)   [kg/h]

Basitleştirilmiş tahmin (ortalama):
- DN15 kapan, 5 bar: ~25 kg/h buhar kaybı
- DN20 kapan, 5 bar: ~40 kg/h buhar kaybı
- DN25 kapan, 10 bar: ~90 kg/h buhar kaybı
```

#### Maliyet Hesabı
```
Yıllık_kayıp_maliyeti = ṁ_kayıp × çalışma_saati × buhar_maliyeti   [€/yıl]
```

### 2.7 İzolasyon Değerlendirmesi

#### Ölçüm Protokolü
1. Termal kamera ile tüm buhar hatlarını, vanaları, flanşları tara
2. Sıcak noktaları (>60°C yüzey sıcaklığı) belirle ve kaydet
3. İzolasyonsuz veya hasarlı izolasyonlu bölümleri ölç:
   - Boru çapı ve uzunluğu
   - Yüzey sıcaklığı
   - Ortam sıcaklığı
4. Isı kaybı hesabı (EN ISO 12241 veya 3E Plus yazılımı ile)

#### Isı Kaybı Hesabı (İzolasyonsuz Boru)
```
Q_kayıp = h × A × (T_yüzey - T_ortam)   [W]

h = doğal konveksiyon + radyasyon ısı transfer katsayısı ≈ 10-15 W/(m²·K)
A = π × D_dış × L   [m²]

Yıllık_enerji_kaybı = Q_kayıp × çalışma_saati / 1000   [kWh/yıl]
```

### 2.8 Görsel İnceleme Kontrol Listeleri

#### Kazan Dairesi Kontrol Listesi
- [ ] Oda havalandırması yeterli mi (yanma havası kaynağı)?
- [ ] Yanma havası giriş kanalları açık ve temiz mi?
- [ ] Brülör durumu (elektrot, nozul, difüzör, ateşleme sistemi)
- [ ] Alev gözlem penceresi temiz mi, alev rengi/şekli normal mi?
- [ ] Kontrol paneli aktif alarmlar veya uyarılar var mı?
- [ ] Emniyet vanaları test tarihleri güncel mi?
- [ ] Su seviye göstergesi temiz ve doğru çalışıyor mu?
- [ ] Blöf vanaları sızıntı yapıyor mu?
- [ ] Su arıtma ekipmanı çalışıyor mu (yumuşatıcı, RO, deaeratör)?
- [ ] Besleme suyu tankı sıcaklığı yeterli mi (>80°C)?
- [ ] Kimyasal dozajlama sistemi aktif mi?
- [ ] Kazan yüzeylerinde sıcak nokta veya renk değişimi var mı?
- [ ] Baca durumu (korozyon, sızıntı, çökelme)?
- [ ] Ekonomizer varsa yoğuşma koruması aktif mi?
- [ ] Yakıt sistemi (gaz basıncı, sıvı yakıt sıcaklığı/basıncı) normal mi?

#### Buhar Dağıtım Kontrol Listesi
- [ ] Boru izolasyonu sağlam ve eksiksiz mi?
- [ ] Vanalar, flanşlar, kompansatörler izolasyonlu mu?
- [ ] Görünür buhar kaçağı var mı (vana sızıntıları, flanş kaçakları)?
- [ ] Buhar kapanları düzenli kontrol ediliyor mu?
- [ ] Basınç düşürme istasyonları doğru çalışıyor mu?
- [ ] Kondensat geri dönüş hatları izolasyonlu mu?
- [ ] Flash buhar geri kazanım sistemi var mı?
- [ ] Boru eğimleri doğru mu (su çekici riski)?
- [ ] Drenaj noktaları ve cep (drip leg) düzeni uygun mu?
- [ ] Boru destekleri ve askıları sağlam mı?

#### Talep Tarafı Kontrol Listesi
- [ ] Isı eşanjörleri verimli çalışıyor mu (yaklaşma sıcaklığı)?
- [ ] Proses ekipmanında kondensat tahliyesi düzgün mü?
- [ ] Kondensat geri dönüşü sağlanıyor mu yoksa drenaja mı gidiyor?
- [ ] Buhar kullanımı gerçekten gerekli mi (alternatif ısı kaynağı)?
- [ ] Isı geri kazanım fırsatları var mı?
- [ ] Buhar basıncı ihtiyaçtan fazla mı (aşırı basınç)?
- [ ] Kullanılmayan ekipman hala buhar alıyor mu?

### 2.9 Operatör Görüşmeleri

1. Tipik kazan yük profili nasıl, hangi saatlerde pik talep?
2. Kazanlar hangi sırayla devreye giriyor?
3. Blöf ne sıklıkla ve ne kadar süre yapılıyor?
4. Su kalitesi kontrolleri ne sıklıkla yapılıyor?
5. Brülör bakımı en son ne zaman yapıldı?
6. Baca gazı sıcaklığı son dönemde arttı mı?
7. Kondensat geri dönüşünde sorun var mı (kontaminasyon vb.)?
8. Buhar kapanlarında bilinen arıza var mı?
9. İzolasyon hasarı bildirilen yerler var mı?
10. Mevsimsel talep değişimleri neler?

## Adım 3: Veri Analizi

### 3.1 Verimlilik Hesaplama — Direkt Yöntem (Input-Output)

```
η_direct = (ṁ_steam × (h_steam - h_fw)) / (ṁ_fuel × LHV) × 100   [%]

Burada:
ṁ_steam = Buhar üretim debisi [kg/h]
h_steam = Üretilen buharın entalpisi [kJ/kg]
h_fw    = Besleme suyunun entalpisi [kJ/kg]
ṁ_fuel  = Yakıt debisi [kg/h veya m³/h]
LHV     = Yakıtın alt ısıl değeri [kJ/kg veya kJ/m³]
```

**Not:** Direkt yöntem basit ve hızlıdır ancak ölçüm belirsizlikleri yüksek olabilir; özellikle buhar debimetre kalibrasyonu kritiktir.

### 3.2 Verimlilik Hesaplama — İndirekt Yöntem (Kayıp Yöntemi, ASME PTC 4)

```
η_indirect = 100 - L_kuru_baca - L_nemli_baca - L_radyasyon - L_blöf - L_yanmamış   [%]
```

#### Kayıp Bileşenleri

**1. Kuru baca gazı kaybı:**
```
L_kuru = (ṁ_kuru_baca × Cp_baca × (T_baca - T_ortam)) / (ṁ_fuel × LHV) × 100   [%]

Basitleştirilmiş (Siegert formülü):
L_kuru = k × (T_baca - T_ortam) / CO₂%

k = 0.56 (doğalgaz), 0.68 (fuel oil), 0.63 (kömür)
```

**2. Baca gazı nem kaybı (H₂ yanmasından):**
```
L_nem = (ṁ_H₂O × (h_buhar_baca - h_su_ref)) / (ṁ_fuel × LHV) × 100   [%]

ṁ_H₂O = 9 × H₂_yakıt + W_yakıt   [kg/kg yakıt]
```

**3. Radyasyon ve konveksiyon kaybı:**
```
L_radyasyon ≈ 1.0 - 2.0% (tam yükte)
L_radyasyon ≈ 2.0 - 4.0% (kısmi yükte, %50)

ABMA tablosu veya ölçüm ile belirlenir.
```

**4. Blöf kaybı:**
```
L_blöf = (ṁ_blöf × (h_blöf - h_makyaj)) / (ṁ_fuel × LHV) × 100   [%]

ṁ_blöf = ṁ_fw × TDS_fw / (TDS_blöf - TDS_fw)   [kg/h]
```

**5. Yanmamış kayıplar:**
```
L_yanmamış_gaz = f(CO, H₂, CH₄ baca gazında)   [%]
L_yanmamış_katı = f(karbon cürufu, toz) — katı yakıtlar için   [%]
```

### 3.3 Exergy Analizi

ExergyLab engine kullanarak:

1. **Yakıt exergy girişi hesapla:**
```
Ex_yakıt = ṁ_fuel × (LHV × φ)   [kW]

φ = exergy/enerji oranı
φ_doğalgaz ≈ 1.04
φ_fuel_oil ≈ 1.06
φ_kömür ≈ 1.06-1.10
```

2. **Buhar/su exergy çıkışı hesapla:**
```
Ex_buhar = ṁ_steam × [(h_steam - h₀) - T₀ × (s_steam - s₀)]   [kW]
Ex_fw = ṁ_fw × [(h_fw - h₀) - T₀ × (s_fw - s₀)]   [kW]

Ex_net_çıkış = Ex_buhar - Ex_fw   [kW]
```

3. **Yanma tersinmezliğini belirle:**
```
Ex_yıkım_yanma = Ex_yakıt + Ex_hava - Ex_yanma_ürünleri   [kW]
```

4. **Baca gazı exergy kaybını hesapla:**
```
Ex_baca = ṁ_baca × [(h_baca - h₀) - T₀ × (s_baca - s₀)]   [kW]
```

5. **Diğer exergy kayıplarını hesapla:**
```
Ex_blöf = ṁ_blöf × [(h_blöf - h₀) - T₀ × (s_blöf - s₀)]   [kW]
Ex_radyasyon = Q_radyasyon × (1 - T₀/T_yüzey)   [kW]
```

6. **Sistem exergy verimini hesapla:**
```
ψ_kazan = Ex_net_çıkış / Ex_yakıt × 100   [%]

Tipik değerler:
ψ_enerji ≈ 80-92% (enerji verimi)
ψ_exergy ≈ 30-45% (exergy verimi — yanma tersinmezliği nedeniyle düşük)
```

7. **Benchmark ile karşılaştır:** Bkz. `benchmarks/boiler_benchmarks.md`

### 3.4 Kayıp Dağılımı Analizi

| Kayıp Bileşeni | Enerji Kaybı (%) | Exergy Yıkımı (%) | Notlar |
|-----------------|-------------------|--------------------| -------|
| Kuru baca gazı | | | O₂ ve T_baca'ya bağlı |
| Nem kaybı (H₂ yanması) | | | Yakıt H içeriğine bağlı |
| Radyasyon/konveksiyon | | | Yük faktörüne bağlı |
| Blöf kaybı | | | TDS/iletkenlik kontrolü |
| Yanmamış kayıp | | | CO seviyesine bağlı |
| Yanma tersinmezliği | — | | Exergy'ye özgü |
| **Toplam kayıp** | | | |
| **Net verimlilik** | | | |

### 3.5 Benchmark Karşılaştırması

| Parametre | En İyi Uygulama | İyi | Ortalama | Kötü |
|-----------|-----------------|-----|----------|------|
| Kazan verimi (LHV, doğalgaz) | >95% | 90-95% | 85-90% | <85% |
| Kazan verimi (LHV, fuel oil) | >92% | 88-92% | 83-88% | <83% |
| Baca gazı O₂ (doğalgaz) | 1.5-3.0% | 3.0-4.0% | 4.0-6.0% | >6.0% |
| Baca gazı sıcaklığı (ekonomizerli) | <120°C | 120-160°C | 160-200°C | >200°C |
| Baca gazı sıcaklığı (ekonomizersiz) | <180°C | 180-220°C | 220-260°C | >260°C |
| Kondensat geri dönüş oranı | >90% | 70-90% | 50-70% | <50% |
| Buhar kapanı arıza oranı | <5% | 5-10% | 10-20% | >20% |
| Blöf oranı | <3% | 3-5% | 5-8% | >8% |

Detaylı benchmark verileri: `benchmarks/boiler_benchmarks.md`

## Adım 4: Raporlama

### Rapor Yapısı

#### 1. Yönetici Özeti (1 sayfa)
- Sistem genel bakışı (kazan sayısı, toplam kapasite, yıllık yakıt maliyeti)
- Temel bulgular (3-5 madde)
- Toplam tasarruf potansiyeli (kWh/yıl, m³ gaz/yıl ve €/yıl)
- Öncelikli öneriler ve ROI
- Uygulama zaman çizelgesi özeti

#### 2. Sistem Tanımı (2-4 sayfa)
- Ekipman envanter tablosu (kazanlar, brülörler, yardımcı ekipman)
- Sistem şeması/yerleşimi
- Buhar dağıtım şeması (basınç seviyeleri, tüketiciler)
- Çalışma koşulları (basınç, sıcaklık, vardiya, üretim)
- Su arıtma sistemi açıklaması

#### 3. Mevcut Durum Değerlendirmesi (3-5 sayfa)
- Enerji tüketimi analizi (yakıt miktarı, maliyet, trend)
- Kazan verimlilik hesapları (direkt ve indirekt yöntem)
- Kayıp dağılımı analizi (Sankey diyagramı)
- Sistem exergy verimi
- Benchmark karşılaştırması

#### 4. Bulgular ve Analiz (5-10 sayfa)
Her bulgu için:
- Açıklama, ölçüm verileri, fotoğraflar/termal görüntüler
- Mevcut durum niceliği
- Temel neden
- Etki (kWh/yıl, m³ gaz/yıl, €/yıl, CO₂ ton/yıl)

#### 5. İyileştirme Önerileri (3-5 sayfa)

Öncelik matrisi formatında:

| # | Öneri | Yatırım | Yıllık Tasarruf | Geri Ödeme | Öncelik |
|---|-------|---------|----------------|------------|---------|
| 1 | Yanma optimizasyonu (O₂ trim) | €5,000 | €18,000 | 0.3 yıl | YÜKSEK |
| 2 | Arızalı buhar kapanı değişimi | €3,000 | €25,000 | 0.1 yıl | YÜKSEK |
| 3 | Ekonomizer montajı | €40,000 | €22,000 | 1.8 yıl | ORTA |
| 4 | İzolasyon tamamlama | €5,000 | €8,000 | 0.6 yıl | YÜKSEK |
| 5 | Kondensat geri kazanımı artırma | €15,000 | €12,000 | 1.3 yıl | ORTA |
| 6 | Otomatik blöf sistemi | €8,000 | €6,000 | 1.3 yıl | ORTA |
| 7 | Flash buhar geri kazanımı | €12,000 | €7,000 | 1.7 yıl | ORTA |
| 8 | Yük optimizasyonu (çoklu kazan) | €2,000 | €10,000 | 0.2 yıl | YÜKSEK |

Her öneri için:
- Teknik açıklama
- Yatırım maliyet tahmini
- Yıllık tasarruf hesabı (varsayımlarla)
- Basit geri ödeme süresi
- CO₂ azaltma (ton/yıl)
- Uygulama karmaşıklığı (düşük/orta/yüksek)

#### 6. ROI Hesapları (2-3 sayfa)
- Her öneri için detaylı hesaplama
- Anahtar varsayımlara duyarlılık analizi (yakıt fiyatı, çalışma saati)
- Birden fazla önlem uygulandığında kombine tasarruf (interaksiyon etkileri)
- Büyük yatırımlar için net bugünkü değer (NPV)

#### 7. Uygulama Yol Haritası (1-2 sayfa)
- **Faz 1:** Hızlı kazanımlar (0-3 ay) — yanma ayarı, kapan onarımı, izolasyon, blöf ayarı
- **Faz 2:** Orta vadeli (3-12 ay) — ekonomizer, otomatik blöf, kondensat geri kazanımı
- **Faz 3:** Uzun vadeli (1-3 yıl) — kazan değişimi, kojenerasyon, sistem yeniden tasarımı
- Tasarruf doğrulama izleme planı

#### 8. Ekler
- A: Ham ölçüm verileri (baca gazı analiz sonuçları, sıcaklık logları)
- B: Ekipman nameplate fotoğrafları
- C: Buhar kapanı tarama logu (fotoğraflı)
- D: Termal kamera görüntüleri
- E: Hesaplama detayları (verimlilik, exergy)
- F: Ekipman teknik şartnameleri (önerilmiş ise)

### Öncelik Matrisi

| Yatırım | Düşük Tasarruf | Yüksek Tasarruf |
|---------|---------------|-----------------|
| Düşük yatırım | İzolasyon tamamlama, blöf ayarı | Yanma optimizasyonu, kapan onarımı |
| Yüksek yatırım | Yoğuşma ekonomizeri | Ekonomizer, kojenerasyon |

### Tipik Bulgular ve Tasarruf Aralıkları

| Kategori | Tipik Bulgu | Tipik Tasarruf |
|----------|------------|---------------|
| Fazla hava / yanma optimizasyonu | O₂ seviyesi >5%, CO yüksek | %1-3 |
| Ekonomizer montajı/iyileştirme | Baca gazı sıcaklığı >200°C | %4-8 |
| Buhar kapanı onarımı | Kapanların %15-30'u arızalı | %5-15 |
| Kondensat geri kazanımı | Geri dönüş oranı <%50 | %5-15 |
| İzolasyon tamamlama | İzolasyonsuz borular, vanalar | %1-3 |
| Blöf optimizasyonu | Manuel blöf, aşırı blöf | %1-3 |
| Yük optimizasyonu | Kötü kazan sıralaması, düşük yük | %3-8 |
| Yanma havası ön ısıtma | Soğuk yanma havası kullanımı | %1-2 |
| Flash buhar geri kazanımı | Yüksek basınçlı kondensat atmosfere atılıyor | %1-3 |
| Baca gazı yoğuşma geri kazanımı | Doğalgaz kazanlarında yoğuşma ekonomizeri | %5-10 |

## Adım 5: Doğrulama ve Takip

### Uygulama Sonrası Doğrulama
- Öneri uygulandıktan sonra 2-4 haftalık baca gazı ölçüm kampanyası
- Önceki/sonraki verimlilik karşılaştırması (aynı yük koşullarında)
- IPMVP (International Performance Measurement and Verification Protocol) yöntemiyle doğrulama
- Yakıt tüketimi trend analizi (hava sıcaklığı/üretim normalizasyonu ile)

### Sürekli İzleme KPI'ları

| KPI | Formül | Ölçüm Sıklığı |
|-----|--------|---------------|
| Kazan verimi | η = Q_buhar / Q_yakıt × 100 | Aylık (veya sürekli) |
| Baca gazı O₂ | Analizör okuması (%) | Haftalık (veya sürekli) |
| Baca gazı sıcaklığı | Analizör okuması (°C) | Haftalık (veya sürekli) |
| Buhar-yakıt oranı | kg_buhar / m³_gaz (veya kg_yakıt) | Aylık |
| Blöf oranı | ṁ_blöf / ṁ_fw × 100 (%) | Aylık |
| Kondensat geri dönüş oranı | ṁ_kondensat / ṁ_buhar × 100 (%) | Aylık |
| Buhar kapanı arıza oranı | Arızalı kapan / Toplam kapan × 100 (%) | 6 ayda bir |
| Spesifik buhar tüketimi | kg_buhar / üretim_birimi | Aylık |
| Makyaj suyu oranı | ṁ_makyaj / ṁ_fw × 100 (%) | Aylık |
| Sistem exergy verimi | Ex_çıkış / Ex_giriş × 100 (%) | Yıllık (denetimde) |

## İlgili Dosyalar
- Tüm kazan ekipman dosyaları: `equipment/boiler_*.md`, `equipment/steam_systems_overview.md`
- Tüm çözüm dosyaları: `solutions/boiler_*.md`
- Benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Exergy formülleri: `formulas/boiler_exergy.md`
- Yakıt bilgileri: `equipment/boiler_fuels.md`

## Referanslar
- ASME PTC 4, "Fired Steam Generators — Performance Test Codes"
- EN 12952, "Water-tube boilers and auxiliary installations"
- EN 12953, "Shell boilers"
- BS 845, "Methods for assessing thermal performance of boilers"
- ISO 50001:2018, "Energy management systems"
- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry"
- Spirax Sarco, "The Steam and Condensate Loop" (Learning Modules)
- CIBO (Council of Industrial Boiler Owners), "Energy Efficiency Handbook"
- ABMA (American Boiler Manufacturers Association), "Radiation Loss Charts"
- Carbon Trust, "Steam and High Temperature Hot Water Boilers" (CTG052)
- IPMVP, "International Performance Measurement and Verification Protocol"
