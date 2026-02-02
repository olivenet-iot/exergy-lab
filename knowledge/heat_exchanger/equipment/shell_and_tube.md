---
title: "Gövde-Boru Eşanjörler (Shell and Tube Heat Exchangers)"
category: equipment
equipment_type: heat_exchanger
subtype: "Gövde-Boru"
keywords: [eşanjör, gövde-boru, shell and tube, TEMA, baffle, tüp düzeni, U-boru]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md]
use_when: ["Shell and tube eşanjör analizi yapılırken", "TEMA tip seçimi gerektiğinde", "Gövde-boru eşanjör tasarım değerlendirmesi yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Gövde-Boru Eşanjörler — Shell and Tube Heat Exchangers

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Gövde-boru (shell and tube) eşanjörler, endüstrideki en yaygın ısı eşanjörü tipidir. Tüm ısı eşanjörlerinin yaklaşık %65-70'ini oluşturur. Geniş sıcaklık, basınç ve kapasite aralığında güvenilir çalışma sağlar.

- Kapasite aralığı: 10 kW - 500+ MW
- Basınç aralığı: Vakum (0.01 bar) - 300+ bar
- Sıcaklık aralığı: -200°C ile 600°C (özel alaşımlarla 800°C+)
- Alan/hacim oranı: 50-300 m²/m³ (kompakt eşanjörlere göre düşük)
- Tipik ömür: 15-30 yıl (malzeme ve servise bağlı)

## TEMA Sınıflandırma Sistemi

TEMA (Tubular Exchanger Manufacturers Association) standardı, gövde-boru eşanjörleri üç harfli bir kodla tanımlar:

### TEMA Harf Sistemi

```
TEMA Kodu: [Ön Kapak Tipi] [Gövde Tipi] [Arka Kapak Tipi]

Örnek: AES
  A = Ön kapak (Removable Channel and Cover)
  E = Gövde (One-Pass Shell)
  S = Arka kapak (Floating Head with Backing Device)
```

### Ön Kapak (Front End) Tipleri

| Harf | Tip | Açıklama | Kullanım |
|------|-----|----------|----------|
| A | Çıkarılabilir kanal ve kapak | Bağımsız sökme imkanı | Temizlik gereken servisler |
| B | Tek parça kanal (Bonnet) | Basit, ucuz | Temiz akışkanlar |
| C | İntegral tüp plakası, çıkarılabilir kapak | Yüksek basınç | Yüksek basınç uygulamaları |
| N | Sabit tüp plakası, çıkarılabilir kapak | N tipi gövde ile | Özel tasarımlar |
| D | Özel yüksek basınç kapağı | Reaktör bağlantısı | >150 bar uygulamalar |

### Gövde (Shell) Tipleri

| Harf | Tip | Akış Düzeni | Kullanım |
|------|-----|-------------|----------|
| E | Tek geçiş | Tek geçiş, en basit | Genel amaçlı, en yaygın |
| F | İki geçiş (boylamasına bölme plakası) | Karşı akış yaklaşımı | Yüksek etkinlik gerektiğinde |
| G | Bölünmüş akış (split flow) | Merkezden iki yana | Düşük ΔP gerektiğinde |
| H | Çift bölünmüş akış (double split flow) | Merkezden dört yana | Çok düşük ΔP gerektiğinde |
| J | Bölünmüş akış (divided flow) | Orta giriş, iki uçtan çıkış | Yoğuşma servisleri |
| K | Kettle tip (buharlaştırıcı) | Genişletilmiş gövde | Reboiler, buharlaştırıcı |
| X | Çapraz akış | Gövde tarafında çapraz geçiş | Vakum yoğuşma, düşük ΔP |

### Arka Kapak (Rear End) Tipleri

| Harf | Tip | Genleşme | Tüp Demeti Çıkarılabilir mi? | Maliyet |
|------|-----|----------|-------------------------------|---------|
| L | Sabit tüp plakası (Fixed tubesheet) | Genleşme bağlantısı ile | Hayır | Düşük |
| M | Sabit tüp plakası | Genleşme bağlantısı ile | Hayır | Düşük |
| N | Sabit tüp plakası, kanal ile | Genleşme bağlantısı ile | Hayır | Düşük |
| P | Dış yüzüklü yüzen kafa (Outside-packed floating head) | Evet — yüzen | Evet | Orta-Yüksek |
| S | Yüzen kafa, destek cihazlı (Floating head with backing device) | Evet — yüzen | Evet | Yüksek |
| T | Çekilebilir yüzen kafa (Pull-through floating head) | Evet — yüzen | Evet | En yüksek |
| U | U-boru | Evet — U bükümü | Evet | Orta |
| W | Dıştan conta yüzen kafa (Externally sealed floating tubesheet) | Evet — yüzen | Evet | Orta |

### Yaygın TEMA Konfigürasyonları

| TEMA Kodu | Kullanım Alanı | Avantaj | Dezavantaj |
|-----------|---------------|---------|------------|
| BEM | Temiz akışkanlar, düşük-orta basınç | Ekonomik, basit | Tüp demeti çıkarılamaz |
| AES | Kirli akışkanlar, orta basınç | Tüp demeti çıkarılabilir, temizlenebilir | Daha pahalı |
| AEL | Sabit tüp plakası, temiz gövde tarafı | Sızdırmaz, düşük maliyet | Gövde tarafı mekanik temizlik yok |
| BEU | Genel amaçlı, ısıl genleşme | U-boru ile genleşme absorbe | İç boru temizliği zor |
| AEP | Kirli servisler, orta basınç | Tüp demeti çıkarılabilir | Sızıntı riski (conta) |
| AET | Ağır kirli servisler | Tüp demeti kolayca çıkarılır | En pahalı yüzen kafa tipi |
| AKT | Kettle tipi reboiler | Buharlaşma için geniş gövde | Büyük boyut, yüksek maliyet |
| CFU | Yüksek basınç, ısıl genleşme | Yüksek basınç dayanımı | Özel imalat, pahalı |

## Bölme Plakası (Baffle) Tasarımı

Bölme plakaları gövde tarafında akışkan akışını yönlendirerek ısı transfer katsayısını artırır.

### Bölme Plakası Tipleri

| Tip | Açıklama | h_gövde Artışı | ΔP Etkisi | Kullanım |
|-----|----------|---------------|-----------|----------|
| Segmental (tek) | En yaygın, tek kesim | Referans | Referans | Genel amaçlı |
| Segmental (çift) | İki segmental bölme | +%15-25 | -%30-40 | Düşük ΔP gerektiğinde |
| Disk-ve-halka (disc-and-donut) | Dairesel iç/dış bölme | +%10-20 | -%20-30 | Vibrasyon azaltma |
| Helisel (helical) | Spiral açıda yerleştirilmiş | +%20-40 | -%40-60 | Yüksek verimlilik, düşük ΔP |
| Bölme plakasız pencere (NTIW) | Pencere bölgesinde tüp yok | Değişken | -%10-20 | Vibrasyon hassas servisler |
| Rod baffle | Çubuk destekli | Orta | -%50-70 | Düşük ΔP, vibrasyon önleme |

### Baffle Kesim Oranı (Baffle Cut)

```
Baffle kesim oranı = h_kesim / D_gövde_iç × 100%

Burada:
  h_kesim    : Kesilen yükseklik (m)
  D_gövde_iç : Gövde iç çapı (m)

Tipik aralık: %20-35 (en yaygın: %25)

  %20 baffle cut → Yüksek h_gövde, yüksek ΔP
  %25 baffle cut → Optimal denge (çoğu uygulama)
  %35 baffle cut → Düşük h_gövde, düşük ΔP

Baffle aralığı (baffle spacing):
  Minimum: D_gövde/5 veya 50 mm (hangisi büyükse)
  Maksimum: D_gövde veya 700 mm (TEMA sınırı)
  Optimal: D_gövde × 0.3 - 0.5 (çoğu uygulama)
```

## Tüp Yerleşim Düzenleri (Tube Layout Patterns)

| Düzen | Açı | Avantaj | Dezavantaj | Kullanım |
|-------|-----|---------|------------|----------|
| Üçgen (triangular) | 30° | En fazla tüp/alan, yüksek U | Mekanik temizlik zor | Temiz gövde tarafı |
| Döndürülmüş üçgen (rotated triangular) | 60° | İyi akış dağılımı | Daha az tüp | Özel uygulamalar |
| Kare (square) | 90° | Mekanik temizlik imkanı | Daha az tüp/alan | Kirli gövde tarafı |
| Döndürülmüş kare (rotated square) | 45° | Yüksek U + mekanik temizlik | Orta tüp yoğunluğu | Kirli + yüksek U gereken |

### Tüp Aralığı (Tube Pitch)

```
Tüp aralığı (pitch), P_t:
  Minimum: P_t ≥ 1.25 × d_o  (TEMA minimum)

Burada:
  d_o : Tüp dış çapı (mm)

Tipik değerler:
  d_o = 19.05 mm (3/4") → P_t = 23.81 mm (min), genellikle 25.40 mm (1")
  d_o = 25.40 mm (1")   → P_t = 31.75 mm (min), genellikle 31.75 mm (1-1/4")

Tüp aralığı oranı: P_t / d_o
  Üçgen düzen: 1.25-1.50 (genellikle 1.25)
  Kare düzen: 1.25-1.50 (genellikle 1.25)
```

## Tüp Boyutları ve Malzemeleri

### Standart Tüp Boyutları

| Dış Çap (mm) | Et Kalınlığı (mm) — BWG | Tipik Uygulama |
|-------------|-------------------------|----------------|
| 15.88 (5/8") | 1.24 (BWG 18), 1.65 (BWG 16) | Temiz servisler, yoğuşma |
| 19.05 (3/4") | 1.24 (BWG 18), 1.65 (BWG 16), 2.11 (BWG 14) | En yaygın boyut |
| 25.40 (1") | 1.65 (BWG 16), 2.11 (BWG 14), 2.77 (BWG 12) | Kirli servisler, büyük kapasiteler |
| 31.75 (1-1/4") | 2.11 (BWG 14), 2.77 (BWG 12) | Ağır kirli, korozif servisler |
| 38.10 (1-1/2") | 2.11 (BWG 14), 2.77 (BWG 12) | Özel uygulamalar |
| 50.80 (2") | 2.77 (BWG 12), 3.40 (BWG 10) | Yoğun kirli servisler |

### Tüp Malzemeleri

| Malzeme | Isı İletkenliği (W/(m·K)) | Maks Sıcaklık (°C) | Uygulama | Göreceli Maliyet |
|---------|---------------------------|---------------------|----------|------------------|
| Karbon çelik (CS) | 50 | 450 | Genel amaçlı, temiz servisler | 1.0 (referans) |
| Paslanmaz çelik 304 (SS304) | 16 | 800 | Korozif, gıda, ilaç | 3-4× |
| Paslanmaz çelik 316 (SS316) | 16 | 800 | Deniz suyu, klorürlü ortam | 4-5× |
| Bakır (Cu) | 385 | 250 | Yüksek iletkenlik, temiz su | 5-6× |
| Admiralty pirinç (CuZn) | 111 | 260 | Soğutma suyu, kondenser | 3-4× |
| Cupronickel 90/10 | 52 | 300 | Deniz suyu kondenser | 6-8× |
| Cupronickel 70/30 | 29 | 350 | Ağır deniz suyu servisi | 8-10× |
| Titanyum Gr2 | 22 | 315 | Agresif korozif, deniz suyu | 10-15× |
| Inconel 625 | 10 | 650 | Yüksek sıcaklık, korozif | 20-30× |
| Hastelloy C276 | 12 | 650 | Çok agresif kimyasal servis | 25-35× |

## Akışkan Tahsisi (Fluid Allocation)

### Tüp Tarafı vs Gövde Tarafı Seçim Kuralları

| Kriter | Tüp Tarafına | Gövde Tarafına |
|--------|-------------|----------------|
| Basınç | Yüksek basınçlı akışkan | Düşük basınçlı akışkan |
| Korozyon | Korozif akışkan (ucuz tüp malzemesi) | Daha az korozif akışkan |
| Kirlenme | Kirli akışkan (kolay temizlik) | Daha temiz akışkan |
| Sıcaklık | Yüksek sıcaklıklı akışkan | Düşük sıcaklıklı akışkan |
| Viskozite | Düşük viskoziteli akışkan | Yüksek viskoziteli akışkan (baffle etkisi) |
| Debi | Düşük debili akışkan | Yüksek debili akışkan |
| Faz değişimi | — | Yoğuşan veya kaynayan akışkan (kettle hariç) |
| Toksik akışkan | Toksik akışkan (sızdırmazlık kolay) | — |

### Akışkan Tahsisi Karar Öncelikleri

```
Öncelik sırası (en önemliden başlayarak):

1. Basınç → Yüksek basınçlı akışkan tüp tarafına
2. Korozyon → Korozif akışkan tüp tarafına (ucuz özel malzeme)
3. Kirlenme → Kirli akışkan tüp tarafına (kolay temizlik)
4. Sıcaklık → Yüksek sıcaklıklı akışkan tüp tarafına (küçük kesit)
5. Viskozite → Viskoz akışkan gövde tarafına (baffle türbülans)
6. Debi → Düşük debili akışkan tüp tarafına (çoklu geçiş)
```

## Termal Tasarım

### Tipik U Değerleri (Temiz, Kirlenme Hariç)

| Sıcak Akışkan | Soğuk Akışkan | U (W/(m²·K)) | Not |
|----------------|---------------|-------------|-----|
| Su | Su | 800-1,500 | Genel servis |
| Su | Havayısı (ince sıvı) | 600-1,200 | Gıda prosesi |
| Buhar (yoğuşan) | Su | 1,500-4,000 | Isıtma servisi |
| Buhar (yoğuşan) | Hafif HC sıvısı | 500-1,000 | Petrokimya |
| Buhar (yoğuşan) | Ağır yağ | 50-300 | Isıtma, viskoz |
| HC gaz | Su | 50-250 | Gaz soğutma |
| HC sıvı | Su | 300-800 | Soğutma servisi |
| HC sıvı | HC sıvı | 100-400 | Proses eşanjörü |
| Gaz | Gaz | 20-80 | Gaz-gaz eşanjör |
| Organik buhar (yoğuşan) | Su | 500-1,500 | Kondenser |
| Amonyak (yoğuşan) | Su | 1,000-2,500 | Soğutma sistemi |
| Su (kaynayan) | Buhar (yoğuşan) | 1,500-5,000 | Reboiler, buhar jeneratörü |

### Gövde Tarafı Isı Transfer Katsayısı

```
Bell-Delaware yöntemi (gövde tarafı katsayısı):

h_gövde = h_ideal × J_c × J_l × J_b × J_s × J_r

Burada:
  h_ideal : İdeal çapraz akış katsayısı (W/(m²·K))
  J_c     : Baffle kesim düzeltme faktörü (0.53-1.15)
  J_l     : Baffle sızıntı düzeltme faktörü (0.44-1.00)
  J_b     : Demet bypass düzeltme faktörü (0.50-1.00)
  J_s     : Değişken baffle aralığı düzeltme faktörü (0.85-1.00)
  J_r     : Olumsuz sıcaklık gradyeni düzeltme faktörü (0.40-1.00, laminer akış)
```

### Tüp Tarafı Isı Transfer Katsayısı

```
Türbülanslı akış (Re > 10,000):
  Dittus-Boelter korelasyonu:
  Nu = 0.023 × Re^0.8 × Pr^n
  n = 0.4 (ısıtma), n = 0.3 (soğutma)

  h_tüp = Nu × k / d_i

Burada:
  Re = ρ × v × d_i / μ
  Pr = cp × μ / k
  d_i = Tüp iç çapı (m)
  k   = Akışkan ısı iletkenliği (W/(m·K))
  v   = Akışkan hızı (m/s)
  μ   = Dinamik viskozite (Pa·s)
```

## Basınç Düşüşü Hesabı

### Tüp Tarafı

```
ΔP_tüp = N_p × [f × L × ρ × v² / (2 × d_i) + 4 × ρ × v² / 2]

Burada:
  N_p : Tüp geçiş sayısı
  f   : Sürtünme faktörü (Moody diyagramı)
  L   : Tüp uzunluğu (m)
  ρ   : Akışkan yoğunluğu (kg/m³)
  v   : Akışkan hızı (m/s)
  d_i : Tüp iç çapı (m)

Tipik izin verilen ΔP: 0.3-1.0 bar (sıvılar), 0.03-0.10 bar (gazlar)
```

### Gövde Tarafı

```
ΔP_gövde = N_b × ΔP_çapraz + (N_b + 1) × ΔP_pencere + 2 × ΔP_uç

Burada:
  N_b          : Baffle sayısı
  ΔP_çapraz    : Çapraz akış bölgesi basınç düşüşü (Pa)
  ΔP_pencere   : Pencere bölgesi basınç düşüşü (Pa)
  ΔP_uç        : Giriş/çıkış uç bölge basınç düşüşü (Pa)
```

## Gövde-Boru Eşanjör Exergy Analizi

### Exergy Dengesi

```
Eşanjör exergy dengesi:

  Ex_giriş = Ex_çıkış + Ex_yıkım + Ex_kayıp

Sıcak akışkan:
  Ex_h,in = m_h × [(h_h,in - h₀) - T₀ × (s_h,in - s₀)]
  Ex_h,out = m_h × [(h_h,out - h₀) - T₀ × (s_h,out - s₀)]

Soğuk akışkan:
  Ex_c,in = m_c × [(h_c,in - h₀) - T₀ × (s_c,in - s₀)]
  Ex_c,out = m_c × [(h_c,out - h₀) - T₀ × (s_c,out - s₀)]

Exergy verimi:
  η_ex = (Ex_c,out - Ex_c,in) / (Ex_h,in - Ex_h,out)

Exergy yıkım oranı:
  Ex_yıkım = (Ex_h,in - Ex_h,out) - (Ex_c,out - Ex_c,in)
  Ex_yıkım = T₀ × S_üretilen

Entropi üretimi:
  S_üretilen = m_c × (s_c,out - s_c,in) + m_h × (s_h,out - s_h,in) + Q_kayıp/T₀
```

### Tipik Exergy Verimi Değerleri (Gövde-Boru)

| Servis | Exergy Verimi (%) | Açıklama |
|--------|-------------------|----------|
| Sıvı/sıvı (yakın sıcaklıklar) | 65-85 | Düşük ΔT → düşük exergy yıkımı |
| Sıvı/sıvı (uzak sıcaklıklar) | 40-65 | Yüksek ΔT → yüksek exergy yıkımı |
| Buhar/su (ısıtma) | 35-60 | Faz değişim tersinmezliği |
| Gaz/gaz | 25-50 | Düşük U → büyük ΔT gerekir |
| Gaz/sıvı | 30-55 | Asimetrik ısı transfer dirençleri |
| Reboiler | 30-55 | Kaynama tersinmezliği |
| Kondenser | 35-60 | Yoğuşma tersinmezliği |

### Exergy Verimini Artırma Stratejileri

| Strateji | Uygulanma Yöntemi | Beklenen İyileşme |
|----------|-------------------|-------------------|
| ΔT_min azaltma | Daha fazla ısı transfer alanı | +%5-15 exergy verimi |
| Karşı akış yaklaşma | Gövde geçiş sayısını artırma (F tipi) | +%3-8 exergy verimi |
| Baffle optimizasyonu | Helisel baffle kullanımı | +%5-10 exergy verimi (ΔP azalması ile) |
| Kirlenme azaltma | Düzenli temizlik programı | +%5-20 exergy verimi geri kazanımı |
| Uygun malzeme seçimi | Yüksek iletkenlikli tüp | +%2-5 exergy verimi |
| Tüp takviyesi | Kanatlı tüp, insert | +%5-15 exergy verimi (ΔP dikkat) |

## Mekanik Tasarım Hususları

### ASME ve PED Gereksinimleri

| Standart | Kapsam | Sertifikasyon |
|----------|--------|---------------|
| ASME Section VIII Div.1 | Basınçlı kaplar (standart) | U Stamp |
| ASME Section VIII Div.2 | Basınçlı kaplar (alternatif) | U2 Stamp |
| PED 2014/68/EU | Avrupa basınçlı ekipman | CE Marking |
| EN 13445 | Avrupa basınçlı kaplar | EN standardı |
| TEMA R | Rafineri servisi (sıkı tolerans) | — |
| TEMA C | Ticari/genel servis | — |
| TEMA B | Kimyasal proses servisi | — |

### Titreşim (Vibration) Kontrolü

```
Tüp doğal frekansı:
  f_n = (C_n / (2π)) × √(E × I / (ρ_t × A_t × L_eff⁴))

Burada:
  C_n    : Sınır koşulu sabiti (3.52 ankastre-serbest, 9.87 ankastre-ankastre)
  E      : Tüp elastik modülü (Pa)
  I      : Tüp kesit atalet momenti (m⁴)
  ρ_t    : Tüp yoğunluğu (akışkan dahil) (kg/m³)
  A_t    : Tüp kesit alanı (m²)
  L_eff  : Desteksiz tüp uzunluğu (m)

Kritik kural: f_n > 1.5 × f_uyarım (güvenlik faktörü)

Uyarım kaynakları:
  - Vortex kopması (Strouhal sayısı: St = f × d_o / V)
  - Türbülanslı tamponlama
  - Akustik rezonans
```

## Ölçülmesi Gereken Parametreler

### Zorunlu Parametreler

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Sıcak giriş sıcaklığı | °C | Servise bağlı | Termoeleman (PT100) |
| Sıcak çıkış sıcaklığı | °C | Servise bağlı | Termoeleman (PT100) |
| Soğuk giriş sıcaklığı | °C | Servise bağlı | Termoeleman (PT100) |
| Soğuk çıkış sıcaklığı | °C | Servise bağlı | Termoeleman (PT100) |
| Sıcak taraf debisi | kg/s veya m³/h | Servise bağlı | Debimetre (vortex, EM, orifis) |
| Soğuk taraf debisi | kg/s veya m³/h | Servise bağlı | Debimetre |
| Basınç düşüşü (her taraf) | bar veya kPa | 0.1-2.0 bar | Diferansiyel basınç transmitteri |

### Varsayılan Değerler

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Kirlenme direnci (su) | 0.000176 m²·K/W | TEMA arıtılmış su |
| Kirlenme direnci (HC sıvı) | 0.000352 m²·K/W | Hafif hidrokarbon |
| Tüp iletkenliği (CS) | 50 W/(m·K) | Karbon çelik |
| Referans sıcaklık (T₀) | 25°C (298.15 K) | Exergy referansı |
| Tüp dış çapı | 19.05 mm (3/4") | En yaygın boyut |
| Baffle kesim oranı | %25 | TEMA standart |
| Tüp düzeni | 30° üçgen | Temiz servis varsayımı |

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Plakalı eşanjör: `heat_exchanger/equipment/plate.md`
- Çift borulu eşanjör: `heat_exchanger/equipment/double_pipe.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Fabrika ısı entegrasyonu: `factory/heat_integration.md`
- Pinch analizi: `factory/pinch_analysis.md`

## Referanslar

- TEMA (2019). *Standards of the Tubular Exchanger Manufacturers Association*, 10th Edition.
- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Hewitt, G.F., Shires, G.L., Bott, T.R. (1994). *Process Heat Transfer*, CRC Press.
- Mukherjee, R. (1998). "Effectively Design Shell-and-Tube Heat Exchangers," *Chemical Engineering Progress*, 94(2), 21-37.
- Bell, K.J. (1981). "Delaware Method for Shell-Side Design," *Heat Exchangers: Thermal-Hydraulic Fundamentals and Design*, Hemisphere.
- Taborek, J. (1983). "Shell-and-Tube Heat Exchangers: Single Phase Flow," in *Heat Exchanger Design Handbook*, Hemisphere.
- ASME Section VIII Division 1 — *Boiler and Pressure Vessel Code*.
- Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, McGraw-Hill.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- Bejan, A. (2013). *Convection Heat Transfer*, 4th Edition, Wiley.
