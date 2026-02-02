---
title: "Hava Geri Deviri (Drying Air Recirculation)"
category: dryer
equipment_type: dryer
keywords: [hava geri deviri, air recirculation, egzoz geri dönüşü, enerji tasarrufu]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/psychrometrics.md, dryer/solutions/exhaust_heat_recovery.md, dryer/equipment/tunnel_dryer.md, dryer/equipment/belt_dryer.md, dryer/equipment/spray_dryer.md]
use_when: ["Egzoz bağıl nemi < %60 olduğunda", "Kurutma havası geri devir potansiyeli değerlendirilirken"]
priority: high
last_updated: 2026-02-01
---
# Hava Geri Deviri (Drying Air Recirculation)

> Son güncelleme: 2026-02-01

## Genel Bakış

Endüstriyel kurutucularda egzoz havası çoğu zaman doyma noktasına ulaşmadan atmosfere atılır.
Egzoz bağıl neminin %30-60 aralığında olması, havanın hala önemli düzeyde nem taşıma
kapasitesine sahip olduğunu gösterir. Hava geri deviri (air recirculation), egzoz havasının
bir kısmını kurutucu girişine geri besleyerek taze hava ısıtma ihtiyacını azaltan, düşük
maliyetli ve yüksek getirili bir enerji optimizasyon stratejisidir.

**Problem:** Taze ortam havası her çevrimde sıfırdan ısıtılmak zorundadır. Egzoz havası
hala sıcak ve tam doyuma ulaşmamışken atmosfere bırakılması, kurutucuya verilen termal
enerjinin %15-30'unun boşa harcanması anlamına gelir.

**Çözüm:** Egzoz havasının R oranında (%30-70) kurutucu girişine geri beslenmesi. Geri
devredilen hava zaten sıcak olduğundan brülör/ısıtıcı yükü düşer; taze hava miktarı
azaldığından toplam enerji tüketimi belirgin ölçüde iner.

**Tipik Tasarruf:** %10-30 ısıtma enerjisinde azalma (toplam kurutucu enerjisinde %5-15)
**Tipik Yatırım:** 5,000-20,000 EUR
**Geri Ödeme Süresi (SPP):** 0.3-1.0 yıl

---

## Tetikleyici (Trigger Conditions)

Hava geri deviri çözümü aşağıdaki koşullarda tetiklenir:

| Tetikleyici Parametre | Eşik Değeri | Açıklama |
|------------------------|-------------|----------|
| Egzoz bağıl nemi (RH) | < %60 | Hava hala kurutma kapasitesine sahip |
| Egzoz sıcaklığı | > 50°C | Geri devredilen havanın ısıtma değeri var |
| T_exhaust - T_ambient | > 30°C | Sensible ısı geri kazanım potansiyeli yüksek |
| Kurutucu tipi | Konvektif (tünel, bant, döner) | Direkt sıcak hava ile çalışan sistemler |
| Çalışma modu | Sürekli (continuous) | Kararlı hal koşullarında en etkili |

**Ne zaman uygulanmamalı:**
- Egzoz nemi zaten yüksekse (> %80 RH) — geri devir kurutma hızını aşırı düşürür
- Egzoz havası toksik veya yanıcı gaz içeriyorsa (ATEX sınıflandırması gerektirir)
- Ürün kalitesi düşük giriş nemi gerektiriyorsa (ilaç, bazı gıda ürünleri)
- Batch kurutucularda kurutmanın son aşamasında egzoz nemi zaten düşükse

---

## Çalışma Prensibi (Operating Principle)

Hava geri deviri, kurutma döngüsüne dördüncü bir adım ekler:

```
STANDART KURUTMA DÖNGÜSÜ:
  Ortam havası → [Isıtıcı] → Kurutucu → Egzoz → Atmosfer

GERİ DEVİRLİ KURUTMA DÖNGÜSÜ:
  Ortam havası ─────┐
                    ├─→ [Karışım Odası] → [Isıtıcı] → Kurutucu → Egzoz ──┐
  Geri devir hattı ─┘                                                      │
       ↑                                                                    │
       └──────────────── R oranında geri besleme ──────────────────────────┘
                         (1-R) oranında atmosfere
```

### Adımlar

1. **Egzoz havasının bölünmesi:** Kurutucu çıkışında motorlu damper, egzoz havasının R oranını geri devir hattına yönlendirir
2. **Karışım (Mixing):** Geri devredilen sıcak ve nemli egzoz havası, taze ortam havası ile karışım odasında birleşir
3. **Isıtma (Reheating):** Karışım havası brülör veya ısıtıcıda kurutma sıcaklığına yükseltilir — ancak başlangıç sıcaklığı ortam sıcaklığından yüksek olduğundan gereken enerji azalır
4. **Kurutma:** Isıtılmış hava kurutucudan geçerek üründen nem alır

---

## Psikrometrik Analiz (Psychrometric Analysis)

Geri devir sürecini Mollier (h-x) diyagramında dört noktayla izlemek kritik önem taşır:

```
  h (kJ/kg)
  ^
  |       C ← ← ← ← B  (Isıtma: ω sabit)
  |      / ↗
  |     / M (Karışım noktası)
  |    ↗
  |   A            D  (Egzoz: ω artar, T düşer)
  |
  +=========================> ω (g/kg)

Noktalar:
  A = Ortam havası (T_amb, φ_amb)
  M = Karışım noktası (taze + geri devir)
  B = Isıtılmış karışım havası (T_supply, düşük φ)
  C = Kurutucu girişi = B
  D = Egzoz havası (T_exhaust, yüksek φ)
```

### Karışım Hesaplamaları

Kuru termometre sıcaklığı ve mutlak nem için doğrusal karışım kuralı:

```
T_mix = R × T_exhaust + (1 - R) × T_ambient                    [°C]
ω_mix = R × ω_exhaust + (1 - R) × ω_ambient                    [kg/kg]
h_mix = R × h_exhaust + (1 - R) × h_ambient                     [kJ/kg]

Burada:
  R         = geri devir oranı [-]  (0 < R < 1, tipik 0.30 - 0.70)
  T_exhaust = egzoz sıcaklığı [°C]
  T_ambient = ortam sıcaklığı [°C]
  ω_exhaust = egzoz mutlak nemi [kg su/kg kuru hava]
  ω_ambient = ortam mutlak nemi [kg su/kg kuru hava]
  h_exhaust = egzoz entalpisi [kJ/kg kuru hava]
  h_ambient = ortam entalpisi [kJ/kg kuru hava]
```

**Dikkat:** Karışım sonrası bağıl nemin doyma noktasını (%100 RH) aşıp aşmadığı
kontrol edilmelidir. Aşarsa yoğuşma oluşur ve kanal ile ekipmanda korozyon riski artar.
Kontrol formülü:

```
φ_mix = ω_mix × P_atm / ((0.622 + ω_mix) × Pws(T_mix))

φ_mix > 1.0 → YOĞUŞMA TEHLİKESİ → R oranını düşür!
```

---

## Optimal Geri Devir Oranı (Optimal Recirculation Ratio)

Optimum R değeri ürüne, kurutucu tipine ve egzoz koşullarına bağlı olarak %30-70 arasında
değişir. Belirleyici faktörler:

| Faktör | Düşük R (%20-35) | Orta R (%35-55) | Yüksek R (%55-70) |
|--------|-------------------|------------------|--------------------|
| Ürün nem hassasiyeti | Yüksek (ilaç, elektronik) | Orta (gıda, tahıl) | Düşük (seramik, kum) |
| İlk ürün nemi | Düşük (< %30 wb) | Orta (%30-60 wb) | Yüksek (> %60 wb) |
| Egzoz RH | %40-60 | %30-50 | %20-40 |
| Kurutucu tipi | Spray dryer | Belt/tunnel dryer | Rotary dryer |
| Kurutma sıcaklığı | < 80°C | 80-150°C | > 150°C |

### Optimum R Belirleme Yöntemi

1. **Ön hesaplama:** Psikrometrik karışım hesabıyla farklı R değerleri için giriş nemi ve enerji tasarrufunu tablo halinde hesapla
2. **Kurutma hızı analizi:** Artan giriş neminin kurutma hızını ne kadar düşürdüğünü deneysel olarak belirle
3. **Kapasite-enerji dengesi:** Üretim kapasitesi kaybını enerji tasarrufuyla karşılaştır
4. **Optimum nokta:** Toplam işletme maliyetinin (enerji + kapasite kaybı) minimum olduğu R değeri

---

## Enerji Tasarrufu Hesabı (Energy Savings Calculation)

### Temel Formüller

```
Q_without = ṁ_air × Cp × (T_supply - T_ambient)                [kW]
Q_with    = ṁ_air × Cp × (T_supply - T_mix)                    [kW]

Tasarruf   = Q_without - Q_with
           = ṁ_air × Cp × (T_mix - T_ambient)
           = ṁ_air × Cp × R × (T_exhaust - T_ambient)          [kW]

Yüzde tasarruf (ısıtmada):
  S% = R × (T_exhaust - T_ambient) / (T_supply - T_ambient) × 100   [%]

Yakıt tasarrufu:
  Fuel_saving = Tasarruf / η_burner                              [kW]

Yıllık maliyet tasarrufu:
  Annual_saving = Fuel_saving × t_op × C_fuel                   [EUR/yıl]

Burada:
  ṁ_air    = toplam hava kütle debisi [kg/s]
  Cp       = havanın özgül ısısı (~1.005 kJ/(kg·°C))
  η_burner = brülör/ısıtıcı verimi [-]
  t_op     = yıllık çalışma süresi [h/yıl]
  C_fuel   = yakıt birim maliyeti [EUR/kWh]
```

### Geri Devir Oranına Göre Tasarruf Tablosu

Referans koşullar: T_supply = 130°C, T_exhaust = 85°C, T_ambient = 20°C

| R [%] | T_mix [°C] | Isıtma Tasarrufu [%] | Kurutma Hızı Etkisi | Önerilen Uygulama |
|-------|-----------|---------------------|--------------------|--------------------|
| %20 | 33.0 | %11.8 | Minimal etki | Hassas ürünler |
| %30 | 39.5 | %17.7 | Düşük etki | Genel endüstriyel |
| %40 | 46.0 | %23.6 | Orta etki | Standart kurutma |
| %50 | 52.5 | %29.5 | Belirgin etki | Nemli ürünler |
| %60 | 59.0 | %35.5 | Yüksek etki | Yüksek ilk nem |
| %70 | 65.5 | %41.4 | Çok yüksek etki | Sadece özel durumlar |

**Kural:** Her %10 geri devir oranı artışı yaklaşık %6 ısıtma enerjisi tasarrufu sağlar
(yukarıdaki koşullar için). Ancak kurutma hızı düşüşü dengelenmelidir.

---

## Hesaplama Örneği (Worked Example)

**Senaryo:** Tünel kurutucu (tunnel dryer), doğal gaz yakıtlı, %50 geri devir uygulaması

| Parametre | Değer |
|-----------|-------|
| Kurutucu giriş sıcaklığı (T_supply) | 130°C |
| Egzoz sıcaklığı (T_exhaust) | 85°C |
| Egzoz bağıl nemi | %45 RH |
| Ortam sıcaklığı (T_ambient) | 20°C |
| Ortam bağıl nemi | %50 RH |
| Toplam hava kütle debisi (ṁ_air) | 3.0 kg/s |
| Geri devir oranı (R) | 0.50 (%50) |
| Brülör verimi (η_burner) | %90 |
| Yıllık çalışma süresi | 5,500 h/yıl |
| Doğal gaz fiyatı | 0.045 EUR/kWh |

### Adım 1 — Karışım sıcaklığı ve nemi

```
T_mix = 0.50 × 85 + 0.50 × 20 = 52.5°C

ω_ambient ≈ 0.0073 kg/kg  (20°C, %50 RH)
ω_exhaust ≈ 0.0280 kg/kg  (85°C, %45 RH → egzoz yol boyu soğuması dikkate alındığında)

ω_mix = 0.50 × 0.0280 + 0.50 × 0.0073 = 0.01765 kg/kg
```

### Adım 2 — Isıtma enerjisi karşılaştırması

```
Q_without = 3.0 × 1.005 × (130 - 20) = 331.7 kW
Q_with    = 3.0 × 1.005 × (130 - 52.5) = 233.7 kW

Isıtma tasarrufu = 331.7 - 233.7 = 98.0 kW
Yüzde tasarruf   = 98.0 / 331.7 × 100 = %29.5
```

### Adım 3 — Yakıt ve maliyet tasarrufu

```
Yakıt tasarrufu = 98.0 / 0.90 = 108.9 kW (brülör girişinde)

Yıllık enerji tasarrufu = 108.9 × 5,500 = 598,950 kWh/yıl
Yıllık maliyet tasarrufu = 598,950 × 0.045 = 26,953 EUR/yıl
```

### Adım 4 — Yoğuşma kontrolü

```
Pws(52.5°C) ≈ 13,600 Pa  (Magnus formülü)
φ_mix = 0.01765 × 101,325 / ((0.622 + 0.01765) × 13,600)
      = 1,788 / 8,698
      = 0.206 = %20.6 RH → GÜVENLI (yoğuşma riski yok)
```

---

## Sınırlamalar (Limitations and Constraints)

### 1. Maksimum Nem Sınırı (Product Quality)

Giriş havasının mutlak nemi arttıkça kurutma itici kuvveti (driving force) azalır. Her
ürünün tolere edebileceği maksimum giriş nemi farklıdır:

| Ürün Grubu | Maks. Giriş ω [g/kg] | Maks. R [%] | Gerekçe |
|------------|----------------------|-------------|---------|
| İlaç/farmasötik | 15-20 | %20-30 | Ürün stabilitesi, mikrobiyel risk |
| Gıda (toz, granül) | 25-40 | %30-50 | Yapışma, aglomerasyon |
| Tekstil | 35-60 | %40-60 | Renk ve doku kalitesi |
| Seramik/tuğla | 60-100 | %50-70 | Çatlama riski düşük |
| Kum/mineral | 80-150 | %60-70 | Kalite kısıtı minimal |

### 2. Yoğuşma Riski (Condensation Risk)

Geri devir hattında, özellikle kanal bağlantılarında ve soğuk yüzeylerde yoğuşma oluşabilir.
Kanal iç yüzey sıcaklığının karışım havasının çiğ noktasının (dew point) en az 5°C
üzerinde kalmasını sağlayacak izolasyon gereklidir.

### 3. VOC Birikimi (Volatile Organic Compound Accumulation)

Bazı kurutma proseslerinde (boya, vernik, solvent bazlı kaplamalar) egzoz havası uçucu
organik bileşikler (VOC) içerir. Geri devir ile VOC konsantrasyonu kademeli olarak
artar ve patlama alt sınırına (LEL — Lower Explosive Limit) yaklaşabilir.

### 4. Patlama Riski (ATEX Considerations)

Toz veya solvent içeren ortamlarda ATEX Direktifi 2014/34/EU gereksinimlerine uyulmalıdır:
- Geri devir hattında sürekli VOC/toz konsantrasyonu izlenmeli
- LEL'in %25'ini aşmamalı (güvenlik faktörü)
- Patlama basınç tahliye (explosion relief) sistemi entegre edilmeli
- Zone 1/Zone 2 sınıflandırmasına göre ekipman seçilmeli

### 5. Koku ve Kontaminasyon

Gıda ve ilaç sektöründe geri devredilen havadaki koku bileşenleri ve partikül madde
ürün kalitesini olumsuz etkileyebilir. Filtre sistemi (HEPA/aktif karbon) gerekebilir.

---

## Kontrol Stratejisi (Control Strategy)

En etkili kontrol yaklaşımı nem tabanlı (humidity-based) otomatik kontroldür:

### Kontrol Döngüsü

```
[Egzoz Kanalı Nem Sensörü] ──→ [PLC/PID Kontrolör] ──→ [Motorlu Damper]

Setpoint: Egzoz RH = %70-80 (ürüne göre ayarlanır)

Kontrol mantığı:
  IF   egzoz_RH < setpoint_RH  →  geri devir oranını ARTIR  (R↑)
  IF   egzoz_RH > setpoint_RH  →  geri devir oranını AZALT  (R↓)
  IF   egzoz_RH > %90          →  geri deviri KAPAT (bypass mode)
  IF   sensör_arızası          →  geri deviri KAPAT (%100 taze hava)
```

### Sensör Gereksinimleri

| Sensör | Konum | Aralık | Doğruluk |
|--------|-------|--------|----------|
| Nem + sıcaklık (kapasitif) | Egzoz kanalı | 0-100% RH, 0-200°C | ±2% RH, ±0.5°C |
| Nem + sıcaklık (yedek) | Egzoz kanalı | Aynı | Aynı |
| Sıcaklık (Pt100) | Karışım odası çıkışı | 0-200°C | ±0.3°C |
| Ürün nemi (opsiyonel) | Kurutucu çıkışı | NIR veya mikrodalga | ±0.5% nem |

### Mevsimsel Ayar

Yaz aylarında ortam sıcaklığı ve nemi yüksek olduğundan geri devir oranı otomatik olarak
düşürülmelidir. Kış aylarında ise soğuk ve kuru ortam havası geri devir potansiyelini artırır.
Mevsimsel R optimumu için PLC'de sezon programı veya adaptif kontrol algoritması kullanılabilir.

---

## Yatırım ve ROI (Investment and Return)

### Yatırım Maliyeti

| Bileşen | Maliyet Aralığı (EUR) | Açıklama |
|---------|----------------------|----------|
| Motorlu damper (modulating) | 800 - 3,000 | Paslanmaz çelik, yüksek sıcaklık |
| Geri devir kanalı (ductwork) | 1,500 - 6,000 | İzoleli galvaniz veya paslanmaz çelik |
| Karışım odası (mixing chamber) | 500 - 2,000 | Homojen karışım için tasarlanmış |
| Nem sensörü (kapasitif tip) | 500 - 1,500 | Endüstriyel tip, yüksek sıcaklık |
| PLC/kontrolör programlama | 1,000 - 3,000 | Mevcut sisteme entegrasyon |
| Montaj ve devreye alma | 1,500 - 5,000 | İşçilik, test, kalibrasyon |
| **Toplam** | **5,000 - 20,000** | Kurutucu büyüklüğüne göre |

### Sistem Tipine Göre Toplam Yatırım

| Sistem Tipi | Maliyet (EUR) | Açıklama |
|-------------|--------------|----------|
| Basit damper sistemi (sabit oranlı) | 2,000 - 5,000 | Manuel ayar, düşük kontrol |
| Motorlu damper + PLC kontrolü | 5,000 - 12,000 | Otomatik oransal kontrol |
| Nem sensörlü tam otomasyon | 10,000 - 20,000 | PID kontrol + VFD fan + sensör |
| Çok bölgeli kademeli geri devir | 15,000 - 25,000 | Büyük tünel/bant kurutucular |

### ROI Hesabı (Yukarıdaki Tünel Kurutucu Örneği)

```
Yatırım (nem sensörlü tam otomasyon):  15,000 EUR
Yıllık tasarruf:                        26,953 EUR/yıl
Geri ödeme süresi (SPP):                15,000 / 26,953 = 0.56 yıl

Net Bugünkü Değer (NPV, 10 yıl, %8 iskonto):
  NPV = 26,953 × [(1 - 1.08^-10) / 0.08] - 15,000
      = 26,953 × 6.71 - 15,000
      = 180,855 - 15,000
      = 165,855 EUR
```

Altı aydan kısa geri ödeme süresi ve yüksek NPV, hava geri devirinin en hızlı geri
dönüşlü kurutma optimizasyonlarından biri olduğunu göstermektedir.

### Sektörel ROI Karşılaştırması

| Sektör | Tipik R [%] | Yıllık Tasarruf [EUR] | SPP [yıl] |
|--------|------------|----------------------|-----------|
| Gıda (tahıl, makarna) | 30-50 | 15,000 - 40,000 | 0.5 - 1.0 |
| Tekstil | 40-60 | 20,000 - 50,000 | 0.5 - 1.2 |
| Kağıt/Selüloz | 30-50 | 25,000 - 80,000 | 0.6 - 1.5 |
| Seramik/Tuğla | 50-70 | 10,000 - 30,000 | 0.8 - 1.5 |
| Kimya (granül, toz) | 30-50 | 20,000 - 60,000 | 0.5 - 1.2 |

---

## Uygulama Adımları (Implementation Steps)

1. **Egzoz analizi:** Egzoz havası sıcaklığını, bağıl nemini ve mutlak nemini en az 1 hafta
   boyunca sürekli ölç. Farklı yük koşullarında, farklı ürünlerde ve farklı mevsimlerde
   veri topla. Ortalama egzoz RH < %60 ise geri devir uygulanabilir

2. **Ürün toleransı belirleme:** Kurutulan ürünün denge nemi (EMC — Equilibrium Moisture
   Content) eğrisini belirle. Pilot ölçekte artan giriş nemiyle kurutma deneyleri yap.
   Maksimum tolere edilebilir giriş nemini ve hedef R oranını belirle

3. **Psikrometrik hesap:** Mollier diyagramında veya hesaplama yazılımında karışım
   noktasını (M) hesapla. Yoğuşma olup olmadığını kontrol et. Farklı R değerleri için
   enerji tasarruf tablosu oluştur

4. **Kanal tasarımı:** Egzoz kanalından kurutucu girişine geri devir hattını tasarla.
   Kanal çapını hava hızı 10-15 m/s olacak şekilde boyutlandır. İzolasyon kalınlığını
   yoğuşma analizine göre belirle (minimum 50 mm mineral yün)

5. **Damper seçimi:** Modulating (oransal) motorlu damper seç. Damper sızdırmazlık
   sınıfını EN 1751'e göre belirle. Minimum Sınıf 3 önerilir

6. **Karışım odası tasarımı:** Taze ve geri devir havasının homojen karışmasını
   sağlayacak bir karışım odası veya statik mikser yerleştir. Kısa devre akışını önle

7. **Sensör ve kontrol sistemi:** Egzoz kanalına kapasitif nem sensörü yerleştir.
   PLC'de PID kontrol döngüsü programla. Setpoint: egzoz RH = %70-80

8. **Fan kapasitesi kontrolü:** Geri devir ile sistem basınç kayıpları değişir.
   Fan VFD (Variable Frequency Drive) ile ayarlanabilir olmalıdır

9. **Güvenlik sistemleri:** Aşırı nem durumunda geri deviri kapat. Sıcaklık alarmı,
   VOC izleme (gerekiyorsa) ve yangın güvenlik sistemi entegre et. ATEX
   gereksinimlerini değerlendir

10. **Devreye alma:** Düşük geri devir oranı (%20) ile başla. Ürün kalitesini her
    aşamada kontrol ederek R oranını kademeli olarak artır. Kararlı hal performansını
    en az 2 hafta boyunca izle

---

## Riskler ve Dikkat Edilecekler (Risks and Precautions)

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Kurutma hızı düşüşü | Giriş neminin artması kurutma itici kuvvetini azaltır | Optimum R oranını deneysel olarak belirle; üretim kapasitesini izle |
| Ürün kalitesi bozulması | Aşırı nem ürünün renk, doku veya mekanik özelliklerini etkileyebilir | Her ürün için kalite testleri yap; R oranını ürüne göre ayarla |
| Yoğuşma (condensation) | Soğuk yüzeylerde veya kanal bağlantılarında yoğuşma oluşabilir | Kanalları izole et; çiğ noktası hesabıyla soğuk noktaları ortadan kaldır |
| Nem birikimi (buildup) | Uzun süreli geri devir ile sistemde nem seviyesi kademeli artabilir | Periyodik olarak %100 taze hava ile "flush" uygula (vardiya başı) |
| VOC birikimi ve patlama | Organik solvent veya toz içeren proseslerde LEL'e yaklaşma riski | Sürekli LEL izleme; LEL > %25 olduğunda geri deviri durdur |
| Koku ve kontaminasyon | Gıda/ilaç uygulamalarında koku bileşenleri birikebilir | Aktif karbon filtre veya ozon sistemi ekle |
| Sensör arızası | Nem sensörü arızalanırsa geri devir kontrolden çıkar | Yedek sensör; arıza durumunda %100 taze hava moduna otomatik geçiş |
| Dengesiz dağılım | Geri devredilen havanın kurutucu içinde eşit dağılmaması | Karışım odası (mixing chamber) ile düzgün dağılım sağla |
| Mevsimsel değişim | Yaz/kış ortam koşulları geri devir optimumunu değiştirir | Mevsimsel R oranı ayarı; adaptif kontrol algoritması |
| Korozyon | Yüksek nemli hava metal kanallarda korozyon hızlandırır | Paslanmaz çelik veya epoksi kaplamalı kanal kullan |

---

## İlgili Dosyalar

- Kurutma exergy formülleri: `dryer/formulas.md`
- Kurutucu benchmarkları: `dryer/benchmarks.md`
- Nemli hava termodinamiği: `dryer/psychrometrics.md`
- Egzoz ısı geri kazanımı: `dryer/solutions/exhaust_heat_recovery.md`
- Tünel kurutucu detaylı analiz: `dryer/equipment/tunnel_dryer.md`
- Bant kurutucu detaylı analiz: `dryer/equipment/belt_dryer.md`
- Spray kurutucu detaylı analiz: `dryer/equipment/spray_dryer.md`
- Isı pompası retrofit: `dryer/solutions/heat_pump_retrofit.md`
- Mekanik ön su alma: `dryer/solutions/mechanical_dewatering.md`
- Fabrika çapraz ekipman fırsatları: `factory/cross_equipment.md`

---

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014 — Chapter 42: Energy Aspects in Drying
- Kemp, I.C., "Fundamentals of Energy Analysis of Dryers," in Modern Drying Technology, Vol. 4, Wiley-VCH, 2012
- Kemp, I.C., "Pinch Analysis and Process Integration," 2nd Edition, Butterworth-Heinemann, 2007
- US DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry," 3rd Edition
- Carbon Trust, "Industrial Energy Efficiency Accelerator — Guide to the Drying and Dehydration Sector," CTG053, 2011
- ASHRAE Handbook — Fundamentals, Chapter 1: Psychrometrics, 2021
- Bahu, R.E., "Energy Considerations in Dryer Design," Drying Technology Journal, Vol. 9, No. 4
- Kudra, T., "Energy Aspects in Drying," Drying Technology, Vol. 22, No. 5, 2004
- ATEX Directive 2014/34/EU — Equipment and Protective Systems Intended for Use in Potentially Explosive Atmospheres
- EN 1751:2014, "Ventilation for Buildings — Air Terminal Devices — Aerodynamic Testing of Dampers and Valves"
- Aghbashlo, M. et al., "A Review on Exergy Analysis of Drying Processes and Systems," Renewable and Sustainable Energy Reviews, 22, 1-22, 2013
- Perry's Chemical Engineers' Handbook, 9th Edition — Section 12: Psychrometry, Evaporative Cooling, and Solids Drying
