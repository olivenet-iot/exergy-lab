---
title: "Veri Toplama ve Yönetimi (Data Collection and Management)"
category: factory
equipment_type: factory
keywords: [veri toplama, ölçüm, fabrika]
related_files: [factory/measurement_verification.md, factory/methodology.md, factory/system_boundaries.md]
use_when: ["Veri toplama planı hazırlanırken", "Ölçüm noktaları belirlenirken"]
priority: low
last_updated: 2026-01-31
---
# Veri Toplama ve Yönetimi (Data Collection and Management)

> Son güncelleme: 2026-01-31

## Genel Bakış

Enerji audit ve enerji yönetim sistemlerinin etkinliği, doğru ve güvenilir veriye dayanır. Bu dosya; enerji etüdlerinde kullanılan ölçüm cihazlarını, teknik spesifikasyonlarını, kalibrasyon gereksinimlerini, veri toplama protokollerini, SCADA/BMS entegrasyonunu, veri kalite güvencesi ve ölçüm belirsizliği analizini (GUM yöntemi) kapsar. ISO 50001 enerji yönetim sistemi ve ISO 50015 ölçüm-doğrulama çerçevesiyle uyumludur.

## 1. Ölçüm Cihazları ve Spesifikasyonlar (Measurement Instruments)

### 1.1 Elektrik Güç Analizörleri (Power Analyzers)

| Parametre | Taşınabilir Analizör | Sabit Analizör (Panel) | Kayıtçı (Logger) |
|---|---|---|---|
| Örnek Model | Fluke 435-II | Schneider PM8000 | Onset HOBO UX120 |
| Ölçüm aralığı | 1-1000 V, 0.5-6000 A | 57-690 V, 1-10000 A | 0-600 V, 0-200 A |
| Doğruluk (güç) | ±%0.5 (okuma) | ±%0.2 (okuma) | ±%1.0 (okuma) |
| Harmonik analiz | 50. harmoniğe kadar | 63. harmoniğe kadar | Yok |
| Kayıt kapasitesi | 600+ parametre | Sürekli (SD kart) | 1.9M veri noktası |
| İletişim | USB, Wi-Fi, Bluetooth | Modbus, Ethernet, RS-485 | USB |
| Tipik maliyet | €5,000-12,000 | €1,500-4,000 | €200-600 |
| Kullanım | Geçici ölçüm, audit | Sürekli izleme | Uzun süreli kayıt |

### 1.2 Baca Gazı Analizörleri (Flue Gas Analyzers)

| Parametre | Temel Model | Gelişmiş Model | Endüstriyel Model |
|---|---|---|---|
| Örnek Model | Testo 310 | Testo 340 | Testo 350 |
| O₂ aralığı | 0-21% | 0-25% | 0-25% |
| CO aralığı | 0-4,000 ppm | 0-10,000 ppm | 0-50,000 ppm |
| CO₂ (hesaplanan) | Evet | Evet | Evet |
| NO/NOx | Yok | Opsiyonel | 0-3,000 ppm |
| SO₂ | Yok | Opsiyonel | 0-5,000 ppm |
| Baca gazı sıcaklığı | -40...+400°C | -40...+600°C | -40...+1,200°C |
| Doğruluk (O₂) | ±%0.2 abs. | ±%0.2 abs. | ±%0.1 abs. |
| Doğruluk (CO) | ±20 ppm | ±5 ppm | ±2 ppm |
| Yanma verimi hesabı | Otomatik | Otomatik + kayıt | Sürekli + veri iletimi |
| Tipik maliyet | €800-1,500 | €2,000-4,000 | €5,000-10,000 |

### 1.3 Ultrasonik Kaçak Detektörleri (Ultrasonic Leak Detectors)

| Parametre | Temel Model | Gelişmiş Model | Akıllı Model |
|---|---|---|---|
| Örnek Model | Fluke ii900 | UE Systems Ultraprobe 15000 | SONOTEC SONAPHONE E |
| Frekans aralığı | 2-100 kHz | 20-100 kHz | 20-100 kHz |
| Algılama mesafesi | 15-20 m | 15-30 m | 10-25 m |
| Görüntüleme | Akustik kamera | Parabola + kulaklık | Renkli ekran + kamera |
| Kaçak boyutu tahmini | Evet (hesaplama) | Yazılım destekli | Otomatik L/dk tahmini |
| Veri kaydı | Dahili | PC yazılımı | Bulut bağlantılı |
| Tipik maliyet | €6,000-10,000 | €3,000-8,000 | €4,000-9,000 |
| Kullanım | Basınçlı hava kaçağı, buhar kaçağı, vakum kaçağı, elektrik ark tespiti |

### 1.4 Kızılötesi Kameralar — IR Termografi (IR Cameras)

| Parametre | Temel Model | Profesyonel | Araştırma |
|---|---|---|---|
| Örnek Model | FLIR E54 | FLIR T540 | FLIR T1020 |
| Çözünürlük | 320×240 | 464×348 | 1024×768 |
| Termal hassasiyet (NETD) | <40 mK | <30 mK | <20 mK |
| Sıcaklık aralığı | -20...+650°C | -20...+1,500°C | -20...+2,000°C |
| Doğruluk | ±2°C veya ±%2 | ±1°C veya ±%1 | ±1°C veya ±%1 |
| Emisivite ayarı | 0.01-1.00 | 0.01-1.00 | 0.01-1.00 |
| Tipik maliyet | €3,000-6,000 | €8,000-15,000 | €25,000-50,000 |
| Enerji audit kullanımı | İzolasyon kaybı, elektrik pano, buhar kaçağı, motor ısınma, kapan kontrolü |

### 1.5 Akışölçerler (Flow Meters)

| Tip | Akışkan | Doğruluk | Basınç kaybı | Maliyet [€] | Not |
|---|---|---|---|---|---|
| Ultrasonik (clamp-on) | Sıvı | ±%1-2 | Yok | 2,000-8,000 | Tahribatsız, geçici ölçüm |
| Ultrasonik (transit-time) | Sıvı/gaz | ±%0.5-1 | Yok | 3,000-12,000 | Sabit montaj |
| Elektromanyetik | İletken sıvı | ±%0.5 | Çok düşük | 1,500-5,000 | Su, kimyasal sıvılar |
| Vortex | Buhar, gaz, sıvı | ±%0.75-1.5 | Orta | 2,000-6,000 | Buhar ölçümüne uygun |
| Orifis plakası | Gaz, buhar | ±%1-2 | Yüksek | 500-2,000 | Basit, yaygın |
| Coriolis | Sıvı, gaz | ±%0.1-0.2 | Orta | 5,000-15,000 | Kütle akış, yüksek doğruluk |
| Turbine | Sıvı | ±%0.5-1 | Orta | 1,000-4,000 | Temiz sıvılar |
| Pitot tüpü | Hava, gaz | ±%2-5 | Çok düşük | 200-800 | Kanal hava hızı |

### 1.6 Sıcaklık Sensörleri (Temperature Sensors)

| Tip | Aralık [°C] | Doğruluk | Yanıt süresi | Maliyet [€] | Kullanım |
|---|---|---|---|---|---|
| Termokupl Tip K | -200...+1,260 | ±1.5°C | Hızlı | 10-50 | Genel amaçlı, yüksek sıcaklık |
| Termokupl Tip T | -200...+350 | ±0.5°C | Hızlı | 10-50 | Düşük sıcaklık, soğutma |
| Termokupl Tip J | -40...+750 | ±1.5°C | Hızlı | 10-50 | Vakum/inert ortam |
| RTD Pt100 | -200...+600 | ±0.15°C (Class A) | Orta | 30-150 | Yüksek doğruluk |
| Termistör NTC | -40...+300 | ±0.1°C | Hızlı | 5-30 | Dar aralık, hassas |
| IR termometre | -50...+3,000 | ±1-2°C | Anlık | 100-500 | Temassız, hareketli yüzey |
| Yüzey sıcaklık bandı | 0...+200 | ±1-2°C | Orta | 20-80 | Boru, tank yüzeyi |

### 1.7 Basınç Ölçerler (Pressure Gauges)

| Tip | Aralık | Doğruluk | Maliyet [€] | Kullanım |
|---|---|---|---|---|
| Dijital manometre | 0-1,000 bar | ±%0.05-0.1 | 200-1,000 | Referans, kalibrasyon |
| Diferansiyel basınç | 0-2,000 mbar | ±%0.5 | 500-2,000 | Filtre, ısı değiştirici |
| Pitot tüpü + manometre | 0-100 Pa | ±%2-3 | 300-800 | Hava hızı, kanal basıncı |
| Bourdon tüpü | 0-600 bar | ±%0.5-1.6 | 20-100 | Genel endüstriyel |
| Basınç transmitteri | Özel aralık | ±%0.1-0.5 | 200-800 | Sürekli izleme, SCADA |

### 1.8 Veri Kaydediciler (Data Loggers)

| Parametre | Çok kanallı | Tek kanallı | Kablosuz |
|---|---|---|---|
| Örnek Model | Yokogawa GP10 | Onset HOBO U12 | Onset MX1101 |
| Kanal sayısı | 10-100 | 1-4 | 1-2 |
| Örnekleme hızı | 100 ms — 60 min | 1 s — 18 saat | 1 s — 18 saat |
| Depolama | 8 GB+ | 43,000-512,000 veri | Bulut (BLE) |
| Batarya ömrü | Şebeke | 1-5 yıl | 1-2 yıl |
| Tipik maliyet | €2,000-8,000 | €50-300 | €80-200 |
| Kullanım | Çoklu parametre izleme | Sıcaklık/nem kaydı | Uzaktan izleme |

## 2. Ölçüm Noktası Matrisi (Measurement Point Matrix)

### 2.1 Sistem Bazında Minimum Ölçüm Noktaları

| Sistem | Parametre | Cihaz Tipi | Konum | Süre | Sıklık |
|---|---|---|---|---|---|
| Kazan | Baca gazı (O₂, CO, T) | Baca gazı analizörü | Baca çıkışı | Min 4 saat | Farklı yüklerde |
| Kazan | Yakıt debisi | Akışölçer / sayaç | Yakıt hattı girişi | Sürekli | — |
| Kazan | Besleme suyu / buhar T, P | RTD + basınç transmitter | Giriş/çıkış | Sürekli | — |
| Kompresör | Elektrik güç | Güç analizörü | Motor terminali | 7 gün | 1 dk |
| Kompresör | Hava debisi | Akışölçer / indirekt | Çıkış hattı | 7 gün | 1 dk |
| Kompresör | Basınç (hat) | Basınç transmitter | Kullanım noktaları | 7 gün | 1 dk |
| Chiller | Elektrik güç | Güç analizörü | Kompresör girişi | 7 gün | 1 dk |
| Chiller | Soğuk su T (gidiş/dönüş) | RTD Pt100 | Boru girişi/çıkışı | 7 gün | 1 dk |
| Chiller | Su debisi | Ultrasonik (clamp-on) | Evaporatör hattı | 7 gün | 1 dk |
| Pompa | Elektrik güç | Güç analizörü | Motor terminali | 7 gün | 1 dk |
| Pompa | Basınç (emiş/basma) | Basınç transmitter | Emiş/basma flanşı | 7 gün | 1 dk |
| Pompa | Debi | Ultrasonik (clamp-on) | Basma hattı | 7 gün | 1 dk |
| Genel | Elektrik (ana pano) | Güç analizörü | Ana dağıtım panosu | 30 gün | 15 dk |
| Genel | Doğalgaz (ana sayaç) | Sayaç okuma / logger | Fabrika girişi | 30 gün | Saatlik |
| Genel | Hava koşulları (T, nem) | Sıcaklık/nem logger | Dış ortam | 30 gün | 15 dk |

## 3. Veri Yönetimi ve Kalite Güvencesi

### 3.1 Veri Toplama Protokolü

```
Adım 1: Planlama
  - Ölçüm noktalarının belirlenmesi (yukarıdaki matrise göre)
  - Cihaz seçimi ve hazırlığı (kalibrasyon kontrolü)
  - Ölçüm süresinin planlanması (normal üretim döneminde)
  - İzin ve güvenlik prosedürleri

Adım 2: Kurulum
  - Cihaz montajı ve bağlantı
  - Sıfır noktası ve aralık kontrolü
  - İlk okuma doğrulaması (referans cihaz ile karşılaştırma)
  - Zaman senkronizasyonu (tüm loggerlar aynı saat)

Adım 3: Veri Toplama
  - Minimum süre: Taşınabilir 7 gün, sabit 30 gün
  - En az 2 farklı yük koşulu (düşük ve yüksek üretim)
  - Eşzamanlı üretim verisi kaydı (MES/ERP'den)
  - Günlük veri kontrolü (eksik veri, aşırı değer tarama)

Adım 4: Veri İndirme ve Doğrulama
  - Ham veri yedekleme (orijinal format)
  - Zaman damgası kontrolü
  - Aykırı değer (outlier) tespiti: |x - X̄| > 3σ
  - Eksik veri interpolasyonu (max %5 boşluk)
  - Veri bütünlük raporu oluşturma
```

### 3.2 Veri Kalite Kontrol Listesi

| Kontrol | Kriter | Aksiyon (Başarısız) |
|---|---|---|
| Kalibrasyon geçerliliği | Kalibrasyon süresi dolmamış | Cihazı kalibrasyona gönder |
| Örnekleme süresi | Minimum 7 gün (kısa süreli) | Ölçüm süresini uzat |
| Eksik veri oranı | <%5 toplam veri noktası | Eksik dönemleri tekrarla |
| Aykırı değer oranı | <%2 (3-sigma dışı) | Aykırı değerleri incele, gerekirse çıkar |
| Zaman senkronizasyonu | Cihazlar arası fark <30 sn | Zaman damgalarını düzelt |
| Üretim korelasyonu | Enerji-üretim eşzamanlılığı | Üretim verilerini kontrol et |
| Referans karşılaştırma | Fatura/sayaç ile ±%5 uyum | Ölçüm faktörünü kontrol et |
| Yük çeşitliliği | Min 2 farklı yük seviyesi | Ölçüm dönemini genişlet |
| Operasyonel koşullar | Normal üretim döneminde | Anormal dönemleri işaretle |

### 3.3 SCADA/BMS Entegrasyonu

```
Mevcut otomasyon sistemlerinden veri alma:

SCADA (Supervisory Control and Data Acquisition):
  Protokoller: Modbus TCP/RTU, OPC-UA, OPC-DA, MQTT, BACnet
  Veri türleri: Anlık değerler, trend verileri, alarm logları
  Tipik kayıt sıklığı: 1 sn — 15 dk (parametreye göre)
  Veri depolama: Historian (PI, Wonderware, iFIX)

BMS (Building Management System):
  Protokoller: BACnet/IP, LonWorks, KNX, Modbus
  Veri türleri: HVAC, aydınlatma, elektrik pano
  Tipik kayıt sıklığı: 1-15 dk

Entegrasyon adımları:
  1. Mevcut tag listesinin alınması
  2. Enerji ile ilgili tag'lerin seçimi
  3. Birim ve ölçek doğrulaması
  4. Veri export formatı belirleme (CSV, SQL, API)
  5. Otomatik veri aktarım kurulumu
  6. Veri doğrulama rutin oluşturma

Önemli notlar:
  - SCADA verisi ölçüm doğruluğu olarak audit cihazlarından düşük olabilir
  - Transmitter kalibrasyonlarını kontrol et (son kalibrasyon tarihi)
  - Totalizer (sayaç) verileri anlık değerlerden daha güvenilirdir
  - Veri sürekliliği: >%95 kullanılabilirlik hedefle
```

## 4. Ölçüm Belirsizliği Analizi — GUM Yöntemi

### 4.1 Belirsizlik Kavramları

```
GUM (Guide to the Expression of Uncertainty in Measurement) yöntemi:

Standart belirsizlik (Standard uncertainty):
  Tip A: İstatistiksel analiz ile belirlenen belirsizlik
    u_A = s / √n
    Burada:
      s = Ölçüm serisi standart sapması
      n = Ölçüm sayısı

  Tip B: Diğer bilgilerle belirlenen belirsizlik
    u_B = a / √3 (düzgün dağılım) veya
    u_B = a / 2 (normal dağılım, %95 güven)
    Burada:
      a = Cihaz doğruluğu veya tolerans yarı-genişliği

Bileşik standart belirsizlik (Combined standard uncertainty):
  u_c = √(Σ cᵢ² × uᵢ²)
  Burada:
    cᵢ = Duyarlılık katsayısı (∂f/∂xᵢ)
    uᵢ = i-inci girdi büyüklüğünün standart belirsizliği

Genişletilmiş belirsizlik (Expanded uncertainty):
  U = k × u_c
  Burada:
    k = Kapsama faktörü (k=2 → %95 güven seviyesi)
```

### 4.2 Hesaplama Örneği — Kazan Verimi Belirsizliği

```
Kazan termal verimi hesaplama ve belirsizliği:

η = Q_fayda / Q_yakıt = (ṁ × Δh) / (V̇_yakıt × H_d)

Burada:
  ṁ = Buhar debisi [kg/s]
  Δh = Buhar-besleme entalpisi farkı [kJ/kg]
  V̇_yakıt = Yakıt hacimsel debisi [Nm³/s]
  H_d = Yakıtın alt ısıl değeri [kJ/Nm³]

Ölçüm belirsizlikleri:
  u(ṁ) / ṁ = ±%2.0 (vortex flowmeter)
  u(Δh) / Δh = ±%1.0 (sıcaklık ve basınç ölçüm belirsizliğinden)
  u(V̇) / V̇ = ±%1.5 (gaz sayacı)
  u(H_d) / H_d = ±%0.5 (gaz analizi)

Bileşik belirsizlik (bağıl):
  u_c(η) / η = √(u(ṁ)/ṁ)² + (u(Δh)/Δh)² + (u(V̇)/V̇)² + (u(H_d)/H_d)²)
  u_c(η) / η = √(0.02² + 0.01² + 0.015² + 0.005²)
  u_c(η) / η = √(0.0004 + 0.0001 + 0.000225 + 0.000025)
  u_c(η) / η = √0.00075 = 0.0274 = %2.74

Genişletilmiş belirsizlik (k=2, %95 güven):
  U(η) / η = 2 × %2.74 = %5.48

Sonuç:
  η = %88.5 ± %4.9 (mutlak belirsizlik) → η = %83.6...%93.4 (%95 güven)

Yorumlama:
  Ölçülen verim %88.5 ise, gerçek verim %95 güven seviyesinde
  %83.6 ile %93.4 arasındadır. Bu belirsizlik kabul edilebilir seviyededir.
```

### 4.3 Enerji Tasarrufu Belirsizliği

```
Tasarruf = E_baz - E_sonra (sadeleştirilmiş)

Tasarruf belirsizliği:
  u(S) = √(u(E_baz)² + u(E_sonra)²)

Burada:
  u(E_baz) = Baz dönem enerji ölçümü belirsizliği
  u(E_sonra) = Proje sonrası enerji ölçümü belirsizliği

Örnek:
  E_baz = 500,000 ± 15,000 kWh/yıl (±%3)
  E_sonra = 420,000 ± 12,600 kWh/yıl (±%3)
  S = 80,000 kWh/yıl

  u(S) = √(15,000² + 12,600²) = √(225,000,000 + 158,760,000)
  u(S) = √383,760,000 = 19,591 kWh/yıl

  Bağıl belirsizlik: 19,591 / 80,000 = %24.5
  Genişletilmiş (k=2): ±%49

  Tasarruf = 80,000 ± 39,182 kWh/yıl (%95 güven)

  Not: Tasarruf belirsizliği, enerji ölçüm belirsizliğinden çok daha yüksektir.
  Küçük tasarruflar (<10% baz) daha yüksek bağıl belirsizliğe sahiptir.
  Bu nedenle IPMVP, tasarruf/belirsizlik oranının ≥2 olmasını önerir.
```

## 5. Veri Doğrulama Kuralları (Data Validation Rules)

### 5.1 Otomatik Doğrulama Kuralları

| Kural | Açıklama | Tetikleyici | Aksiyon |
|---|---|---|---|
| Aralık kontrolü | Değer fiziksel sınırlar içinde mi? | T_baca < 0°C veya > 600°C | Veri işaretle, insan kontrolü |
| Değişim hızı | Ardışık okumalar arası fark makul mü? | ΔT > 50°C/dk | Ani değişim alarmı |
| Tutarlılık | İlişkili parametreler uyumlu mu? | Enerji artıyor, üretim sıfır | Çapraz kontrol alarmı |
| Sabit değer | Uzun süre aynı değer — sensör donuk mu? | 60 dk aynı okuma | Sensör kontrol et |
| Enerji dengesi | Girdi ≈ Çıktı + Kayıp? | Dengesizlik > %10 | Ölçüm noktalarını kontrol et |
| Negatif değer | Negatif olmaması gereken değer negatif mi? | Güç < 0 (jeneratör hariç) | CT yönünü kontrol et |
| NULL/boş | Eksik veri noktası | Veri yok | İnterpolasyon veya tekrar ölçüm |
| İstatistiksel | Z-skor > 3 | Ortalamadan 3σ uzak | Aykırı değer incelemesi |

### 5.2 Manuel Doğrulama

```
Enerji fatura doğrulaması:

Adım 1: Fatura verisi — sayaç verisi karşılaştırma
  Fark = |E_fatura - E_sayaç| / E_fatura × 100
  Kabul edilebilir: <%5

Adım 2: Enerji yoğunluğu kontrolü
  SEC_hesaplanan vs SEC_tarihsel (son 12 ay)
  Kabul edilebilir sapma: ±%15 (mevsimsel düzeltmeli)

Adım 3: Enerji dengesi
  E_girdi = Σ E_alt_sayaçlar + E_kayıp
  Dengesizlik oranı = |E_girdi - Σ E_çıktı| / E_girdi
  Kabul edilebilir: <%10 (sayaç doğruluğu + kayıplar)

Adım 4: Çapraz kontrol
  Kompresör: kWh/Nm³ → Spesifik güç karşılaştırma
  Kazan: Nm³ gaz → kg buhar → Termal verim karşılaştırma
  Chiller: kWh → kW_soğutma → COP karşılaştırma
```

## İlgili Dosyalar

- [Ölçüm ve Doğrulama](measurement_verification.md) — IPMVP protokolü, M&V planı
- [Performans Göstergeleri](performance_indicators.md) — KPI izleme ve trend analizi
- [Fabrika Benchmarkları](factory_benchmarks.md) — Doğrulama için referans değerler
- [Metodoloji](methodology.md) — Audit prosedürü ve ölçüm entegrasyonu
- [KPI Tanımları](kpi_definitions.md) — Performans gösterge hesaplama formülleri
- [Kazan Audit](../boiler/audit.md) — Kazan ölçüm protokolü
- [Kompresör Audit](../compressor/audit.md) — Kompresör ölçüm prosedürü
- [Chiller Audit](../chiller/audit.md) — Chiller ölçüm noktaları

## Referanslar

- JCGM 100:2008, "Evaluation of Measurement Data — Guide to the Expression of Uncertainty in Measurement (GUM)"
- ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- IEC 61557, "Electrical safety in low voltage distribution systems"
- ISO 5167, "Measurement of fluid flow by means of pressure differential devices"
- Fluke Corporation, "Energy Measurement and Audit Handbook," Application Notes
- Testo AG, "Practical Guide to Flue Gas Analysis," Technical Documentation
- FLIR Systems, "Thermal Imaging Guidebook for Industrial Applications"
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
- Capehart, B.L., Turner, W.C. & Kennedy, W.J., "Guide to Energy Management," 8th Edition, Fairmont Press, 2016
