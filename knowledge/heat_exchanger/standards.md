---
title: "Isı Eşanjörü Standartları — Heat Exchanger Standards (TEMA, ASME, API)"
category: reference
equipment_type: heat_exchanger
keywords: [TEMA, ASME, API, standart, tasarım, gövde-boru, plakalı, hava soğutmalı]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/audit.md]
use_when: ["Eşanjör tasarım standartları referans alınırken", "TEMA sınıflandırması gerektiğinde", "Malzeme ve test gereksinimleri incelenirken"]
priority: medium
last_updated: 2026-02-01
---
# Isı Eşanjörü Standartları — Heat Exchanger Standards (TEMA, ASME, API)

> Son güncelleme: 2026-02-01

## Genel Bakış

Isı eşanjörleri endüstriyel tesislerde en yaygın basınç ekipmanlarından biridir.
Tasarım, imalat, test ve işletme aşamalarında çeşitli ulusal ve uluslararası standartlara
uygunluk zorunludur. Bu dosya, en önemli standartları ve uygulanma alanlarını özetler.

## 1. TEMA Standartları (Tubular Exchanger Manufacturers Association)

### 1.1 TEMA Sınıfları

TEMA, gövde-boru (shell & tube) eşanjörleri üç sınıfta tanımlar:

| TEMA Sınıfı | Ad | Uygulama Alanı | Mekanik Özellikler |
|-------------|-----|---------------|-------------------|
| **R** | Refinery | Petrol, petrokimya, gaz işleme | En katı gereksinimler; yüksek korozyon payı; kaldırma kulpları; tüm bağlantı bölgeleri flanşlı |
| **C** | Commercial | Genel ticari ve endüstriyel | Orta seviye gereksinimler; düşük maliyet; geniş sektör kullanımı |
| **B** | General Service | Kimya prosesleri | R ve C arası; kimya endüstrisi için optimize |

### 1.2 TEMA Sınıfı Detaylı Karşılaştırma

| Parametre | TEMA R | TEMA C | TEMA B |
|-----------|--------|--------|--------|
| Minimum gövde çapı | 6 inç (152 mm) | 6 inç (152 mm) | 6 inç (152 mm) |
| Minimum boru çapı | 3/4 inç (19 mm) OD | 1/2 inç (12.7 mm) OD | 5/8 inç (15.9 mm) OD |
| Minimum boru kalınlığı (BWG) | 14 BWG (karbon çelik) | 16 BWG | 14 BWG |
| Boru-plaka bağlantısı | Genişletme + kaynak | Yalnız genişletme veya kaynak | Genişletme + kaynak |
| Korozyon payı (karbon çelik) | 3.2 mm min | 1.6 mm min | 3.2 mm min |
| Başlangıç bölme (nozzle-baffle) | >= 1/6 merkez baffle aralığı | Sınır yok | >= 1/6 merkez baffle aralığı |
| Gövde flanşı | Flanşlı veya kaynak boyunlu | Lap-joint kabul | Flanşlı veya kaynak boyunlu |
| Kanal (bonnet) tipi | Kanal + kapak (ayrılab.) | Bonnet tipi kabul | Her iki tip kabul |
| Kaldırma kulpları | Zorunlu | Zorunlu değil | Zorunlu değil |
| Basınç test gereksinimleri | ASME Sec. VIII | ASME Sec. VIII | ASME Sec. VIII |

### 1.3 TEMA Tanımlama Sistemi (Type Designation)

TEMA, eşanjör konfigürasyonunu üç harfle tanımlar:

```
[Ön Kanal] [Gövde Tipi] [Arka Kanal]
     ↓          ↓           ↓
  1. harf    2. harf     3. harf
```

**Ön Kanal (Front End Stationary Head) Tipleri:**

| Harf | Tip | Açıklama |
|------|-----|----------|
| A | Channel & Removable Cover | Kanal + çıkarılabilir kapak, en yaygın |
| B | Bonnet (Integral Cover) | Entegre kapak, düşük maliyet |
| C | Channel Integral with Tubesheet | Boru plakasına entegre kanal |
| N | Channel Integral, Removable Cover | Entegre kanal, çıkarılabilir kapak |
| D | Special High Pressure Closure | Yüksek basınç kapaması |

**Gövde (Shell) Tipleri:**

| Harf | Tip | Açıklama |
|------|-----|----------|
| E | One Pass Shell | Tek geçiş gövde, en yaygın |
| F | Two Pass Shell (longitudinal baffle) | İki geçiş gövde, uzunlamasına bafıl |
| G | Split Flow | Bölünmüş akış |
| H | Double Split Flow | Çift bölünmüş akış |
| J | Divided Flow | Bölünen akış (giriş ortada) |
| K | Kettle Type Reboiler | Kazancı tip yeniden kaynatıcı |
| X | Cross Flow | Çapraz akış, düşük DP |

**Arka Kanal (Rear End Head) Tipleri:**

| Harf | Tip | Açıklama |
|------|-----|----------|
| L | Fixed Tubesheet (like A) | Sabit boru plakası |
| M | Fixed Tubesheet (like B) | Sabit boru plakası (bonnet tipi) |
| N | Fixed Tubesheet (like N) | Sabit boru plakası (entegre) |
| P | Outside Packed Floating Head | Dış salmastralı yüzer kafes |
| S | Floating Head with Backing Device | Destekli yüzer kafes |
| T | Pull-Through Floating Bundle | Çekilebilir yüzer demet |
| U | U-Tube Bundle | U-boru demeti |
| W | Externally Sealed Floating Tubesheet | Dış contalı yüzer plaka |

**Yaygın Konfigürasyonlar:**

| TEMA Tipi | Açıklama | Uygulama |
|-----------|----------|----------|
| AES | Kanal + tek geçiş gövde + yüzer kafes | Genel amaçlı, kolay temizlik |
| BEM | Bonnet + tek geçiş + sabit plaka | Düşük maliyet, temiz akışkanlar |
| AEU | Kanal + tek geçiş + U-boru | Termal genleşme esnekliği |
| AET | Kanal + tek geçiş + çekilebilir demet | Kolay bakım |
| CFU | Entegre kanal + iki geçiş gövde + U-boru | Yüksek NTU gerektiren uygulamalar |
| AKT | Kanal + kazancı + çekilebilir demet | Reboiler uygulamaları |
| AEP | Kanal + tek geçiş + dış contalı yüzer kafes | Orta basınç uygulamaları |

### 1.4 TEMA Kirlenme Direnci (Fouling Resistance) Standartları

TEMA, çeşitli akışkanlar için standart kirlenme direnci değerleri tanımlar.
Detaylı tablo için `benchmarks.md` Bölüm 5'e bakınız.

**Önemli Notlar:**
- TEMA kirlenme değerleri konservatiftir ve fazla tasarım (over-design) yaratabilir.
- Fazla tasarım, düşük akış hızlarına neden olarak kirlenmeyi hızlandırabilir.
- Modern yaklaşım: HTRI/HTFS verilerine dayalı dinamik kirlenme modelleri.

## 2. ASME Standartları

### 2.1 ASME Boiler and Pressure Vessel Code (BPVC)

| Bölüm | Açıklama | Eşanjör İlgisi |
|-------|----------|----------------|
| Section II | Materials | Malzeme spesifikasyonları (SA-106, SA-179, SA-213, vb.) |
| Section V | Nondestructive Examination | Tahribatsız muayene yöntemleri |
| Section VIII, Div. 1 | Pressure Vessels — Rules for Construction | Isı eşanjörü basınç parçaları tasarımı |
| Section VIII, Div. 2 | Alternative Rules | Daha detaylı analiz ile optimize tasarım |
| Section IX | Welding and Brazing Qualifications | Kaynak prosedür ve kaynakçı yeterliliği |

### 2.2 ASME Performans Test Kodları (PTC)

| Standart | Açıklama | Kullanım |
|----------|----------|----------|
| PTC 12.5 | Single Phase Heat Exchangers | Tek fazlı eşanjör performans testi |
| PTC 46 | Overall Plant Performance | Santral genelinde (ekonomizer dahil) |
| PTC 4 | Fired Steam Generators | Kazan ekonomizerleri için |
| PTC 19.1 | Test Uncertainty | Ölçüm belirsizliği analizi |
| PTC 19.3 | Thermowells | Sıcaklık ölçüm noktası tasarımı |

### 2.3 ASME Section VIII Div. 1 — Temel Gereksinimler

| Parametre | Gereksinim |
|-----------|-----------|
| Tasarım basıncı | İşletme basıncının en az %10 veya 1.75 bar üstünde |
| Tasarım sıcaklığı | İşletme sıcaklığının en az 15°C üstünde |
| Korozyon payı | Minimum 1.6 mm (TEMA R için 3.2 mm) |
| Maksimum izin verilen gerilme | Malzemeye bağlı, UCS-23'e göre |
| Hidrostatik test basıncı | 1.3 × MAWP (en az) |
| Pnömatik test basıncı | 1.1 × MAWP |
| Radyografi | Kaynak sınıfına göre (tam, noktasal, veya yok) |

## 3. API Standartları

### 3.1 API 660 — Shell-and-Tube Heat Exchangers

API 660, petrol ve petrokimya endüstrisi için gövde-boru eşanjör gereksinimlerini tanımlar.
TEMA R sınıfını temel alır ve ek gereksinimler ekler.

| Konu | API 660 Gereksinimleri |
|------|----------------------|
| Tasarım ömrü | Minimum 20 yıl |
| Minimum gövde kalınlığı | 9.5 mm (korozyon payı hariç) |
| Boru malzemesi | SA-179 veya SA-213 (paslanmaz) |
| Boru-plaka bağlantısı | Genişletme + kuvvet kaynağı (strength weld) |
| Bafıl tipi | Segmentel veya disk-donut |
| Titreşim analizi | Zorunlu (FIV kontrolü) |
| PWHT | Kaynak sonrası ısı işlem gereksinimleri |
| Korozyon payı (gövde) | Minimum 3.0 mm |
| Test | Hidrostatik (her iki taraf ayrı ayrı) |

### 3.2 API 661 — Air-Cooled Heat Exchangers

API 661, hava soğutmalı ısı eşanjörleri (fin-fan coolers) için standart tanımlar.

| Konu | API 661 Gereksinimleri |
|------|----------------------|
| Boru tipi | Finli boru (embedded, extruded, L-foot, vb.) |
| Fin malzemesi | Alüminyum (en yaygın), karbon çelik |
| Fan tipi | Aksiyel, çekiş (induced) veya itiş (forced) draft |
| Tasarım hava sıcaklığı | Sahaya özgü meteorolojik veri |
| Motor sürme | V-kayış, doğrudan sürme, veya hidrolik |
| Titreşim sınırı | ISO 10816'ya göre |
| Gürültü sınırı | 85 dBA @ 1m (standart), sahaya özgü |
| Basınç testi | ASME Section VIII gereksinimlerine göre |
| Kapasite kontrolü | Değişken fanlı, louver, veya VFD |

### 3.3 API 662 — Plate Heat Exchangers

API 662, plakalı ısı eşanjörleri (plate heat exchangers) için standart tanımlar.
İki bölümden oluşur:

| Bölüm | Açıklama |
|-------|----------|
| Part 1 | Plate-and-Frame Heat Exchangers (conta tipi) |
| Part 2 | Brazed Plate Heat Exchangers (lehimli) |

| Konu | API 662 Gereksinimleri |
|------|----------------------|
| Plaka malzemesi | SS 316L (standart), Titanium, Hastelloy, vb. |
| Conta malzemesi | NBR, EPDM, FKM (Viton) — proses koşuluna göre |
| Maksimum çalışma sıcaklığı | 250°C (conta tipi), 400°C (kaynak/lehim) |
| Maksimum çalışma basıncı | 25 bar (conta tipi), 30 bar (lehimli) |
| Test basıncı | 1.3 × tasarım basıncı |
| Conta test gereksinimleri | Sızıntı testi, conta sertlik testi |
| Plaka kalınlığı | Minimum 0.5 mm (paslanmaz çelik) |

## 4. HTRI ve HTFS — Termal Tasarım Yöntemleri

### 4.1 HTRI (Heat Transfer Research Institute)

| Konu | Açıklama |
|------|----------|
| Organizasyon | Üye tabanlı araştırma kurumu, Houston TX |
| Yazılım | Xist (gövde-boru), Xphe (plakalı), Xace (hava soğutmalı) |
| Yöntem | Bell-Delaware yerine HTRI deneysel korelasyonlar |
| Avantaj | Daha doğru sonuçlar (özellikle gövde tarafı) |
| Kapsam | Tek fazlı, yoğuşma, kaynatma, iki fazlı |

### 4.2 HTFS (Heat Transfer and Fluid Flow Service)

| Konu | Açıklama |
|------|----------|
| Organizasyon | Aspen Technology bünyesinde (eskiden AERE Harwell) |
| Yazılım | TASC (gövde-boru), MUSE (çok akımlı) |
| Yöntem | HTFS deneysel korelasyonlar |
| Avantaj | Geniş deneysel veri tabanı |

### 4.3 Bell-Delaware Yöntemi

Açık kaynak gövde tarafı termal tasarım yöntemi:

| Parametre | Açıklama |
|-----------|----------|
| İdeal çapraz akış katsayısı | j_i, f_i (Kern yöntemi baz alınır) |
| Bafıl pencere düzeltmesi | J_c (baffle cut correction) |
| Bafıl sızıntı düzeltmesi | J_l (gövde-bafıl ve boru-bafıl sızıntısı) |
| Demet baypas düzeltmesi | J_b (gövde-demet arasındaki baypas) |
| Advers sıcaklık gradyanı | J_r (laminer akış için) |
| Giriş/çıkış düzeltmesi | J_s (bafıl aralığı düzensizliği) |

```
h_gövde = h_ideal × J_c × J_l × J_b × J_r × J_s
```

## 5. Malzeme Standartları

### 5.1 Yaygın Boru Malzemeleri

| ASTM/ASME | Malzeme | Kullanım | Maks. T [°C] |
|-----------|---------|----------|-------------|
| SA-179 | Karbon çelik (dikişsiz) | Genel amaçlı | 425 |
| SA-214 | Karbon çelik (ERW) | Düşük basınç | 425 |
| SA-213 T11 | 1.25Cr-0.5Mo | Yüksek sıcaklık | 565 |
| SA-213 T22 | 2.25Cr-1Mo | Yüksek sıcaklık | 600 |
| SA-213 TP304 | Östenitik paslanmaz (304) | Korozyon | 815 |
| SA-213 TP316L | Östenitik paslanmaz (316L) | Klorür ortamları | 815 |
| SA-213 TP321 | Östenitik paslanmaz (321) | Yüksek T korozyon | 815 |
| SB-111 C70600 | CuNi 90/10 | Deniz suyu | 260 |
| SB-111 C71500 | CuNi 70/30 | Agresif deniz suyu | 260 |
| SB-338 Gr. 2 | Titanyum | Yüksek korozyon | 315 |
| SB-622 N06625 | Inconel 625 | Aşırı korozyon | 650 |
| SB-619 N10276 | Hastelloy C-276 | Kuvvetli asit ortamı | 650 |

### 5.2 Malzeme Seçim Kılavuzu

| Akışkan / Ortam | Önerilen Malzeme | Alternatif |
|-----------------|-----------------|-----------|
| Temiz su (< 100°C) | Karbon çelik (SA-179) | — |
| Soğutma kulesi suyu | SS 316L veya CuNi 90/10 | Titanium |
| Deniz suyu | CuNi 70/30 veya Titanium | SS 254 SMO |
| Seyreltik asitler | SS 316L | Hastelloy C-276 |
| Konsantre asitler | Hastelloy C-276, Titanium | Tantalum |
| Amonyak | Karbon çelik | SS 304 |
| H2S içeren gazlar | Karbon çelik (NACE MR0175) | SS 316L |
| Yüksek sıcaklık gaz (> 500°C) | Cr-Mo alaşımları, SS 321 | Inconel |
| Gıda ürünleri | SS 316L (elektropolişli) | Titanium |

## 6. Test ve Muayene Gereksinimleri

### 6.1 Üretim Sırasında Testler

| Test | Standart | Açıklama |
|------|----------|----------|
| Hidrostatik test | ASME VIII UG-99 | 1.3 × MAWP, 30 dakika |
| Pnömatik test | ASME VIII UG-100 | 1.1 × MAWP (risk değerlendirmesi gerekli) |
| Sızıntı testi | ASME V | Helium veya halojen |
| Kaynak radyografisi | ASME V, Article 2 | Tam veya noktasal RT |
| UT (ultrasonik) | ASME V, Article 4 | Kalınlık ve kusur tarama |
| Boru-plaka genişletme testi | TEMA RCB-7 | Genişletme derecesi kontrolü |
| PWHT (kaynak sonrası ısı işlem) | ASME VIII UCS-56 | Kalınlık ve malzemeye bağlı |
| Sertlik testi | ASTM E10/E18 | PWHT sonrası |

### 6.2 İşletme Sırasında Muayeneler

| Muayene | Sıklık | Açıklama |
|---------|--------|----------|
| UT kalınlık ölçümü | Yıllık | Korozyon/erozyon izleme |
| Boru eddy current | 2-5 yılda | Boru duvar incelme tespiti |
| Görsel iç muayene | Her bakım duruşunda | Kirlenme, korozyon, erozyon |
| Basınç testi | Her bakım sonrası | Bütünlük doğrulaması |
| Titreşim ölçümü | 6 aylık | Mekanik durum izleme |
| Conta durumu (plakalı) | Yıllık | Deformasyon, sertleşmiş conta |

## İlgili Dosyalar

- `heat_exchanger/formulas.md` — Hesaplama formülleri
- `heat_exchanger/benchmarks.md` — Performans benchmark verileri
- `heat_exchanger/audit.md` — Denetim metodolojisi
- `heat_exchanger/case_studies.md` — Uygulama örnekleri

## Referanslar

1. TEMA (2019). *Standards of the Tubular Exchanger Manufacturers Association*. 10th ed.
2. ASME (2021). *Boiler and Pressure Vessel Code, Section VIII, Division 1*.
3. API 660 (2015). *Shell-and-Tube Heat Exchangers*. 9th ed.
4. API 661 (2013). *Air-Cooled Heat Exchangers for General Refinery Service*. 7th ed.
5. API 662 Part 1 (2006). *Plate-and-Frame Heat Exchangers for General Refinery Service*.
6. API 662 Part 2 (2004). *Brazed Aluminum Plate-Fin Heat Exchangers*.
7. ASME PTC 12.5 (2000). *Single Phase Heat Exchangers*.
8. HTRI (2023). *Design Manual*. Heat Transfer Research Institute.
9. Bell, K.J. (1981). *Delaware Method for Shell-Side Design*. Heat Exchanger Design Handbook, Hemisphere.
10. Mukherjee, R. (1998). *Effectively Design Shell-and-Tube Heat Exchangers*. Chemical Engineering Progress, Feb. 1998.
11. NACE MR0175/ISO 15156 (2015). *Materials for use in H2S-containing environments in oil and gas production*.
