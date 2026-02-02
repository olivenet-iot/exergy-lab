---
title: "CUSUM Analizi (Cumulative Sum Analysis)"
category: factory
equipment_type: factory
keywords: [CUSUM, kümülatif toplam, enerji izleme, performans takibi, trend analizi, sapma tespiti, kontrol grafiği]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/baseline_enpi.md, factory/energy_management/enpi_guide.md, factory/energy_management/monitoring_targeting.md, factory/energy_management/mv_statistics.md, factory/performance_indicators.md]
use_when: ["CUSUM analizi yapılacağında", "Enerji performans trendi izlenecekken", "Tasarruf doğrulaması gerektiğinde"]
priority: medium
last_updated: 2026-02-01
---

# CUSUM Analizi (Cumulative Sum Analysis)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

### 1.1 CUSUM Tanımı

CUSUM (Cumulative Sum — Kümülatif Toplam) analizi, enerji tüketimindeki küçük ve sürekli değişimleri tespit etmek için kullanılan güçlü bir istatistiksel izleme tekniğidir. Her dönem için gerçekleşen tüketim ile beklenen (baseline) tüketim arasındaki farkların kümülatif toplamını hesaplayarak, zaman içindeki performans eğilimini görselleştirir.

### 1.2 Tarihçe

CUSUM tekniği ilk olarak 1954 yılında E.S. Page tarafından kalite kontrol alanında geliştirilmiş, 1970'lerden itibaren İngiltere'de (özellikle Carbon Trust / ETSU çalışmalarıyla) enerji yönetimi alanına adapte edilmiştir. Günümüzde ISO 50001 enerji yönetim sistemlerinin performans izleme aracı olarak ve IPMVP Opsiyon C kapsamında yaygın olarak kullanılmaktadır.

### 1.3 Neden CUSUM?

```
CUSUM'un geleneksel trend analizine göre avantajları:

1. Küçük değişimleri yakalar:
   └── Aylık %1-2 sapma tek başına anlamsız görünür,
       CUSUM kümülatif olarak bu sapmayı büyüterek görünür kılar.

2. Değişim noktasını (change point) belirler:
   └── Hangi ayda performans değişikliği başladı?
       CUSUM eğrisinin eğim değişimi bunu gösterir.

3. Birden fazla müdahaleyi ayırır:
   └── Ocak'ta VSD kuruldu, Mayıs'ta trap onarımı yapıldı.
       Her ikisinin ayrı ayrı etkisi CUSUM'dan okunabilir.

4. Toplam tasarruf miktarını doğrudan verir:
   └── Son CUSUM değeri = Toplam kümülatif tasarruf (negatif ise)

5. Mevsimsel etkiden bağımsız:
   └── Baseline modeli normalizasyon sağlar,
       CUSUM yalnızca performans değişimini gösterir.
```

## 2. CUSUM Hesaplama Yöntemi (Calculation Method)

### 2.1 Temel Formül

```
CUSUM hesaplama formülü:

CUSUMₙ = Σᵢ₌₁ⁿ (Eᵢ,gerçek - Eᵢ,beklenen)

Burada:
  CUSUMₙ     = n. dönem sonundaki kümülatif toplam [kWh veya MWh]
  Eᵢ,gerçek  = i. dönemdeki gerçek enerji tüketimi [kWh]
  Eᵢ,beklenen = i. dönem için baseline modelden hesaplanan beklenen tüketim [kWh]
  n           = Toplam dönem sayısı

Tek dönem farkı:
  Δᵢ = Eᵢ,gerçek - Eᵢ,beklenen

CUSUM serisi:
  CUSUM₁ = Δ₁
  CUSUM₂ = Δ₁ + Δ₂ = CUSUM₁ + Δ₂
  CUSUMₙ = CUSUMₙ₋₁ + Δₙ
```

### 2.2 Baz Çizgisi (Baseline) Gereksinimi

```
CUSUM için güvenilir bir baseline modeli şarttır:

Tercih sırası:
1. Regresyon modeli (en iyi): E = β₀ + β₁X₁ + β₂X₂ + ...
   ├── Üretim, iklim, çalışma saati normalize edilir
   ├── R² ≥ 0.75 (aylık veri için)
   └── CV-RMSE ≤ %25

2. Ortalama bazlı (basit): E_beklenen = E_ortalama (baseline dönemi)
   ├── Yalnızca sabit koşullarda geçerli
   ├── Üretim değişkenliği düşükse kullanılabilir
   └── Normalleştirme yok — dikkatli kullan

3. SEC bazlı: E_beklenen = SEC_baseline × P_dönem
   ├── Tek değişkenli basit normalleştirme
   ├── Baseload'u ihmal eder
   └── Düşük kapasitede yanıltıcı

Bkz: baseline_enpi.md — Regresyon modeli kurulumu detayları
```

### 2.3 Adım Adım CUSUM Hesaplama

```
Adım 1: Baseline dönemi belirle (min 12 ay)
Adım 2: Regresyon modeli kur (E vs ilgili değişkenler)
Adım 3: Model doğrulama (R², CV-RMSE, NMBE)
Adım 4: İzleme dönemi başlat
Adım 5: Her dönem için:
         a) Gerçek tüketimi ölç (Eᵢ,gerçek)
         b) Model ile beklenen tüketimi hesapla (Eᵢ,beklenen)
         c) Farkı hesapla (Δᵢ = Eᵢ,gerçek - Eᵢ,beklenen)
         d) Kümülatif toplamı güncelle (CUSUMₙ = CUSUMₙ₋₁ + Δₙ)
Adım 6: CUSUM grafiğini çiz ve yorumla
Adım 7: Kontrol sınırlarını kontrol et (UCL/LCL)
Adım 8: Gerekli ise aksiyon al
```

### 2.4 Örnek CUSUM Tablosu

| Ay | Üretim (ton) | E_gerçek (MWh) | E_beklenen (MWh) | Fark Δ (MWh) | CUSUM (MWh) |
|----|-------------|---------------|-----------------|-------------|-------------|
| Oca | 4.200 | 520 | 515 | +5 | +5 |
| Şub | 4.000 | 498 | 496 | +2 | +7 |
| Mar | 4.500 | 545 | 544 | +1 | +8 |
| Nis | 4.800 | 572 | 573 | -1 | +7 |
| May | 5.000 | 588 | 592 | -4 | +3 |
| Haz | 5.200 | 605 | 618 | -13 | -10 |
| Tem | 5.500 | 632 | 647 | -15 | -25 |
| Ağu | 5.300 | 612 | 628 | -16 | -41 |
| Eyl | 5.000 | 580 | 592 | -12 | -53 |
| Eki | 4.600 | 545 | 554 | -9 | -62 |
| Kas | 4.300 | 518 | 525 | -7 | -69 |
| Ara | 4.100 | 500 | 506 | -6 | -75 |

```
Yorum:
├── İlk 5 ay: CUSUM ≈ 0 civarı → Performans değişmemiş
├── Haziran'dan itibaren: CUSUM sürekli düşüyor → Tasarruf başlamış
├── Haziran'da ne oldu? → VSD (Variable Speed Drive) devreye alındı
├── Toplam tasarruf: 75 MWh (12 ayda)
└── VSD sonrası ortalama aylık tasarruf: ~11 MWh/ay
```

## 3. CUSUM Grafiği Yorumlama (Chart Interpretation)

### 3.1 Altı Tipik CUSUM Paterni

**Patern 1 — Düz Çizgi (Flat Line)**

```
CUSUM grafiği:
  ──────────────────── (yatay çizgi)

Yorum: Enerji performansı baseline ile aynı.
       Tasarruf yok, kötüleşme yok.
Aksiyon: Normal operasyon devam.
Kontrol: Model hâlâ geçerli mi? Residual kontrolü yap.
```

**Patern 2 — Aşağı Eğim (Downward Slope)**

```
CUSUM grafiği:
  ─┐
    └─┐
       └─┐
          └── (aşağı yönlü)

Yorum: Enerji tüketimi beklenenin altında.
       Sürekli tasarruf sağlanıyor.
       Eğim ne kadar dik → tasarruf oranı o kadar yüksek.
Aksiyon: İyileştirme etkisini doğrula. Başarılı müdahale.
         Tasarruf miktarı = Son CUSUM - İlk CUSUM (negatif değer).
```

**Patern 3 — Yukarı Eğim (Upward Slope)**

```
CUSUM grafiği:
          ┌── (yukarı yönlü)
       ┌─┘
    ┌─┘
  ─┘

Yorum: Enerji tüketimi beklenenin üstünde.
       Performans kötüleşiyor.
       Ekipman verimliliği düşmüş veya operasyonel sorun var.
Aksiyon: Neden araştırması yap.
         Olası nedenler: fouling, kaçak, arıza, operasyon değişikliği.
```

**Patern 4 — Kırılma Noktası (Change Point)**

```
CUSUM grafiği:
  ──────┐
         └─────── (belirgin eğim değişikliği)

Yorum: Belirli bir tarihte ani değişim olmuş.
       Kırılma noktası = Müdahale veya arıza tarihi.
Aksiyon: Kırılma noktasındaki olayı belirle.
         Olumlu ise: Başarılı proje uygulaması
         Olumsuz ise: Ekipman arızası, operasyon değişikliği
```

**Patern 5 — Mevsimsel Dalgalanma (Seasonal Oscillation)**

```
CUSUM grafiği:
     ╱╲    ╱╲
  ──╱  ╲──╱  ╲── (sinüzoidal dalgalanma)

Yorum: Baseline modeli mevsimsel etkiyi tam yakalayamıyor.
       CDD/HDD değişkeni modele dahil değil veya yetersiz.
Aksiyon: Modeli güncelle — iklim değişkeni ekle veya revize et.
         Mevsimsellik ayıklanana kadar CUSUM'a güvenilmez.
```

**Patern 6 — Drift (Gradual Drift)**

```
CUSUM grafiği:
  ─┐
    └──┐
        └───┐
              └────── (yavaş, sürekli kayma)

Yorum: Performans yavaş ve sürekli kötüleşiyor.
       Fouling, aging, kalibrasyon kayması, bakım eksikliği.
       Aylık fark küçük ama kümülatif etki büyük.
Aksiyon: Önleyici bakım programını gözden geçir.
         Ekipman durumu değerlendir.
         Bu tür kayıplar genellikle fark edilmez — CUSUM yakalıyor.
```

### 3.2 Patern Yorum Özet Tablosu

| Patern | CUSUM Eğilimi | Anlam | Tipik Neden | Aksiyon |
|--------|--------------|-------|-------------|---------|
| Düz çizgi | Yatay | Değişim yok | Normal operasyon | İzle |
| Aşağı eğim | Azalan | Tasarruf | Proje uygulaması | Doğrula |
| Yukarı eğim | Artan | Kayıp | Arıza, operasyon hatası | Araştır |
| Kırılma noktası | Ani eğim değişimi | Ani olay | Müdahale veya arıza | Olay tespiti |
| Dalgalanma | Periyodik | Model yetersizliği | Mevsimsel etki | Model güncelle |
| Drift | Yavaş kayma | Yavaş kötüleşme | Fouling, aging | Bakım planla |

## 4. CUSUM ile Tasarruf Hesaplama (Savings Calculation)

### 4.1 Toplam Tasarruf

```
Toplam kümülatif tasarruf:

Tasarruf_toplam = -CUSUMₙ  (CUSUM negatif ise tasarruf)
Kayıp_toplam = +CUSUMₙ     (CUSUM pozitif ise kayıp)

Örnek:
  12 aylık izleme sonunda CUSUM = -185 MWh
  → Toplam tasarruf = 185 MWh
  → Elektrik fiyatı: 2.50 TL/kWh
  → Maliyet tasarrufu: 185.000 × 2.50 = 462.500 TL/yıl
  → CO₂ azaltma: 185 × 0.47 = 86.95 ton CO₂/yıl (Türkiye grid EF)
```

### 4.2 Aylık Tasarruf Trendi

```
Aylık tasarruf (fark serisinden):

Pozitif tasarruf başladığı ay:
  Δᵢ negatife döndüğü ay = Tasarruf başlangıcı

Aylık ortalama tasarruf:
  Tasarruf_aylık = Tasarruf_toplam / Tasarruf dönem sayısı

Yıllık tasarruf projeksiyonu:
  Tasarruf_yıllık = Tasarruf_aylık × 12

Dikkat: Tasarruf projesinin tam yıl çalışması gerekir (mevsimsellik).
Yıllık projeksiyon yapılırken 12 aylık dönemin tamamlanması beklenmeli.
```

### 4.3 Kümülatif Tasarruf Grafiği

```
Kümülatif tasarruf grafik yapısı:

Y ekseni (+): Kümülatif tasarruf [MWh veya TL]
Y ekseni (-): Kümülatif kayıp
X ekseni: Zaman (ay)

Grafik unsurları:
├── Kümülatif enerji tasarrufu [MWh] — mavi çubuk
├── Kümülatif maliyet tasarrufu [TL] — yeşil çizgi (ikincil eksen)
├── Proje maliyeti çizgisi [TL] — kırmızı kesikli (yatay)
└── Başa baş noktası: Kümülatif tasarruf = Proje maliyeti

Bu grafik, yatırımın geri ödeme süresini görsel olarak gösterir.
```

## 5. Kontrol Sınırları (Control Limits)

### 5.1 UCL ve LCL Hesaplama

```
CUSUM kontrol sınırları:

Yöntem 1 — Standart sapma bazlı:
  UCL = +k × σ_Δ × √n
  LCL = -k × σ_Δ × √n

  Burada:
    k    = Kontrol faktörü (genellikle 2 veya 3)
    σ_Δ  = Baseline dönemindeki fark serisinin standart sapması
    n    = İzleme dönemi sayısı

  Pratikte:
    k=2 → %95.4 güven aralığı (uyarı sınırı)
    k=3 → %99.7 güven aralığı (aksiyon sınırı)

Yöntem 2 — V-mask (çift taraflı):
  İleri düzey CUSUM kontrol tekniği
  Açıklama: İki eğik çizgi (V şeklinde) ile CUSUM grafiği
  üzerine yerleştirilen maske; CUSUM eğrisi maskeyi aşarsa alarm.
  Parametreler: d (lead distance), θ (yarım açı)
  Genellikle enerji yönetiminde basit UCL/LCL tercih edilir.

Yöntem 3 — Pratik yaklaşım:
  UCL = +2 × σ_Δ × √12 (12 aylık sınır)
  LCL = -2 × σ_Δ × √12

  Örnek: σ_Δ = 15 MWh
  UCL = +2 × 15 × √12 = +103.9 MWh
  LCL = -2 × 15 × √12 = -103.9 MWh
```

### 5.2 Alarm Eşikleri ve Bildirim Kuralları

| Seviye | Koşul | Aksiyon | Sorumlu |
|--------|-------|---------|---------|
| Normal | CUSUM, kontrol sınırları içinde | İzlemeye devam | Enerji yöneticisi |
| Uyarı (Warning) | CUSUM, ±1.5σ√n aştı | Neden araştırması başlat | Enerji ekibi |
| Dikkat (Alert) | CUSUM, ±2σ√n aştı veya 5 ardışık aynı yönde | Detaylı analiz + aksiyon planı | Enerji yöneticisi + mühendislik |
| Kritik (Critical) | CUSUM, ±3σ√n aştı veya 7+ ardışık aynı yönde | Acil müdahale + yönetim bildirimi | Tesis müdürü |

### 5.3 Otomatik Bildirim Kuralları

```
CUSUM otomatik bildirim mantığı:

Kural 1: Tek dönem farkı:
  |Δᵢ| > 3σ_Δ → Acil bildirim (anomali)

Kural 2: Ardışık trend:
  5 ardışık dönem Δᵢ > 0 → Uyarı (performans düşüşü trendi)
  5 ardışık dönem Δᵢ < 0 → Bilgi (tasarruf trendi — olumlu)

Kural 3: Kümülatif eşik:
  |CUSUMₙ| > UCL → Alarm

Kural 4: Eğim değişikliği:
  CUSUM eğiminde ani değişim (≥2σ_Δ/dönem) → Change point tespiti

Bildirim kanalları:
├── E-posta: Enerji yöneticisi + ilgili mühendis
├── SMS: Kritik seviye için tesis müdürü
├── Dashboard: Trafik ışığı renk değişimi
└── Rapor: Aylık enerji performans raporu eki
```

## 6. Çalışılmış Örnek 1 — Kompresör VSD Projesi

### 6.1 Proje Tanımı

```
Tesis: Otomotiv yedek parça fabrikası
Ekipman: 2 × 110 kW vidalı kompresör (sabit hız)
Proje: 1 kompresöre VSD (Variable Speed Drive) eklenmesi
Uygulama tarihi: Temmuz (13. ay)
Baseline dönemi: Ocak-Aralık (12 ay)
İzleme dönemi: Ocak-Aralık (sonraki 12 ay)
```

### 6.2 Baseline Modeli

```
Regresyon modeli:
E_kompresör [MWh/ay] = 22.5 + 0.018 × Üretim [adet/ay]

İstatistikler:
  R² = 0.82
  CV-RMSE = %16.4
  NMBE = +%0.8
  σ_Δ = 4.2 MWh (baseline dönem fark standart sapması)
```

### 6.3 CUSUM Tablosu (24 Ay: 12 Baseline + 12 İzleme)

| Ay | Dönem | Üretim (adet) | E_gerçek (MWh) | E_beklenen (MWh) | Δ (MWh) | CUSUM (MWh) |
|----|-------|--------------|---------------|-----------------|---------|-------------|
| 1 | Baseline | 12.000 | 237 | 238.5 | -1.5 | -1.5 |
| 2 | Baseline | 11.500 | 232 | 229.5 | +2.5 | +1.0 |
| 3 | Baseline | 13.000 | 260 | 256.5 | +3.5 | +4.5 |
| 4 | Baseline | 13.500 | 264 | 265.5 | -1.5 | +3.0 |
| 5 | Baseline | 14.000 | 276 | 274.5 | +1.5 | +4.5 |
| 6 | Baseline | 14.500 | 281 | 283.5 | -2.5 | +2.0 |
| 7 | Baseline | 15.000 | 295 | 292.5 | +2.5 | +4.5 |
| 8 | Baseline | 14.800 | 287 | 288.9 | -1.9 | +2.6 |
| 9 | Baseline | 13.800 | 272 | 270.9 | +1.1 | +3.7 |
| 10 | Baseline | 12.500 | 248 | 247.5 | +0.5 | +4.2 |
| 11 | Baseline | 11.800 | 233 | 234.9 | -1.9 | +2.3 |
| 12 | Baseline | 12.200 | 244 | 242.1 | +1.9 | +4.2 |
| 13 | İzleme | 12.300 | 240 | 243.9 | -3.9 | +0.3 |
| 14 | İzleme | 11.800 | 228 | 234.9 | -6.9 | -6.6 |
| 15 | İzleme | 13.200 | 249 | 260.1 | -11.1 | -17.7 |
| 16 | İzleme | 13.800 | 257 | 270.9 | -13.9 | -31.6 |
| 17 | İzleme | 14.500 | 268 | 283.5 | -15.5 | -47.1 |
| 18 | İzleme | 15.200 | 278 | 296.1 | -18.1 | -65.2 |
| 19 | İzleme | 15.500 | 281 | 301.5 | -20.5 | -85.7 |
| 20 | İzleme | 15.000 | 272 | 292.5 | -20.5 | -106.2 |
| 21 | İzleme | 14.000 | 255 | 274.5 | -19.5 | -125.7 |
| 22 | İzleme | 13.000 | 240 | 256.5 | -16.5 | -142.2 |
| 23 | İzleme | 12.000 | 222 | 238.5 | -16.5 | -158.7 |
| 24 | İzleme | 12.500 | 230 | 247.5 | -17.5 | -176.2 |

### 6.4 Sonuç Yorumu

```
CUSUM analiz sonuçları:

Baseline dönemi (Ay 1-12):
├── CUSUM aralığı: -1.5 ~ +4.5 MWh → Normal dalgalanma
├── Net değişim: ~0 → Performans sabit
└── Model geçerli

İzleme dönemi (Ay 13-24):
├── Ay 13 (VSD devreye alınma): CUSUM eğimi negatife döndü
├── VSD etkisi giderek artıyor (kısmi yük avantajı)
├── Son CUSUM: -176.2 MWh → Toplam tasarruf: 176.2 MWh
├── 12 aylık ortalama tasarruf: 176.2 / 12 = 14.7 MWh/ay
└── VSD sonrası net tasarruf oranı: ~%6.2

Ekonomik değerlendirme:
├── Yıllık elektrik tasarrufu: 176.2 MWh
├── Elektrik birim fiyat: 2.80 TL/kWh
├── Yıllık maliyet tasarrufu: 176.200 × 2.80 = 493.360 TL/yıl
├── VSD yatırım maliyeti: 680.000 TL
├── Geri ödeme süresi: 680.000 / 493.360 = 1.38 yıl
└── CO₂ azaltma: 176.2 × 0.47 = 82.8 ton CO₂/yıl

Exergy perspektifi (ExergyLab):
├── Baseline kompresör exergy verimi: %42.5
├── VSD sonrası exergy verimi: %51.8
├── Exergy iyileşme: +9.3 puan
└── Kalan exergy yıkımı: Isı geri kazanım potansiyeli → cross-equipment fırsatı
```

## 7. Çalışılmış Örnek 2 — Buhar Sistemi İyileştirme

### 7.1 Proje Tanımı

```
Tesis: Kimya fabrikası
Buhar sistemi: 15 ton/h kazanlar (2 adet), 8 bar doymuş buhar
Müdahale 1 (Ay 4): Buhar kapanı (steam trap) denetimi ve onarımı — 35 kapan değiştirildi
Müdahale 2 (Ay 10): Kondensat geri dönüş hattı iyileştirmesi — geri dönüş %45→%75
Baseline: Önceki yıl 12 ay verisi
İzleme: 18 ay
```

### 7.2 Baseline Modeli

```
Regresyon modeli:
E_doğalgaz [Sm³/ay] = 35.000 + 95 × Üretim [ton/ay] + 450 × HDD [°C·gün/ay]

İstatistikler:
  R² = 0.88
  CV-RMSE = %12.1
  NMBE = -0.5%
  σ_Δ = 8.500 Sm³
```

### 7.3 CUSUM Tablosu (18 Ay İzleme)

| Ay | Üretim (ton) | HDD | E_gerçek (Sm³) | E_beklenen (Sm³) | Δ (Sm³) | CUSUM (Sm³) |
|----|-------------|-----|---------------|-----------------|---------|-------------|
| 1 | 850 | 280 | 242.000 | 241.350 | +650 | +650 |
| 2 | 820 | 250 | 235.500 | 235.400 | +100 | +750 |
| 3 | 880 | 180 | 233.200 | 229.700 | +3.500 | +4.250 |
| 4 | 900 | 80 | 214.000 | 226.500 | -12.500 | -8.250 |
| 5 | 920 | 20 | 210.000 | 231.400 | -21.400 | -29.650 |
| 6 | 950 | 0 | 209.500 | 225.250 | -15.750 | -45.400 |
| 7 | 980 | 0 | 211.000 | 228.100 | -17.100 | -62.500 |
| 8 | 960 | 0 | 208.000 | 226.200 | -18.200 | -80.700 |
| 9 | 900 | 15 | 200.000 | 227.250 | -27.250 | -107.950 |
| 10 | 870 | 80 | 192.000 | 253.650 | -61.650 | -169.600 |
| 11 | 850 | 180 | 212.000 | 267.350 | -55.350 | -224.950 |
| 12 | 830 | 290 | 228.000 | 279.350 | -51.350 | -276.300 |
| 13 | 860 | 300 | 230.000 | 286.700 | -56.700 | -333.000 |
| 14 | 840 | 260 | 225.000 | 271.800 | -46.800 | -379.800 |
| 15 | 880 | 170 | 216.000 | 255.100 | -39.100 | -418.900 |
| 16 | 910 | 60 | 198.000 | 248.450 | -50.450 | -469.350 |
| 17 | 950 | 10 | 196.000 | 229.750 | -33.750 | -503.100 |
| 18 | 970 | 0 | 195.000 | 227.150 | -32.150 | -535.250 |

### 7.4 İki Müdahalenin Etkisini Ayırma

```
CUSUM eğim analizi:

Dönem 1 (Ay 1-3): Müdahale öncesi
├── Ortalama Δ ≈ +1.400 Sm³/ay → Baseline ile uyumlu (hafif sapma)
├── CUSUM eğimi ≈ düz
└── Henüz iyileştirme yok

Dönem 2 (Ay 4-9): Buhar kapanı onarımı sonrası
├── Ay 4'te kırılma noktası (CUSUM aşağı dönüş)
├── Ortalama Δ ≈ -18.700 Sm³/ay
├── CUSUM eğimi = -18.700 Sm³/ay
├── Buhar kapanı onarımının etkisi ≈ 18.700 Sm³/ay doğalgaz tasarrufu
└── Yıllık projeksiyon: 18.700 × 12 = 224.400 Sm³/yıl

Dönem 3 (Ay 10-18): Kondensat geri dönüş sonrası
├── Ay 10'da ikinci kırılma noktası (CUSUM daha dik aşağı)
├── Ortalama Δ ≈ -45.150 Sm³/ay
├── CUSUM eğimi = -45.150 Sm³/ay
├── Toplam etki: 45.150 Sm³/ay
├── Kondensat geri dönüşün ek etkisi: 45.150 - 18.700 = 26.450 Sm³/ay
└── Yıllık projeksiyon: 26.450 × 12 = 317.400 Sm³/yıl

Toplam CUSUM ayrıştırma:
├── Buhar kapanı etkisi: ~224.400 Sm³/yıl (%42)
├── Kondensat geri dönüş etkisi: ~317.400 Sm³/yıl (%58)
├── Toplam yıllık tasarruf: ~541.800 Sm³/yıl doğalgaz
├── TEP tasarrufu: 541.800 × 0.8244 / 1000 = 447 TEP/yıl
└── CO₂ azaltma: 541.800 × 1.96 / 1000 = 1.062 ton CO₂/yıl
```

## 8. CUSUM ve M&V İlişkisi (CUSUM and M&V Relationship)

### 8.1 IPMVP Opsiyon C'de CUSUM Kullanımı

```
IPMVP (International Performance Measurement and Verification Protocol)
Opsiyon C — Tesis Bütünü (Whole Facility):

Özellikler:
├── Tüm tesisin enerji tüketimini izler
├── Regresyon modeli ile baseline oluşturur
├── CUSUM ile kümülatif tasarruf hesaplar
├── Birden fazla ECM'in toplam etkisini ölçer
└── Alt ölçüm gerektirmez (fatura bazlı yeterli)

CUSUM'un Opsiyon C'deki rolü:
├── Tasarruf = -CUSUM (negatif = tasarruf)
├── Belirsizlik: σ_tasarruf = σ_Δ × √n
├── Güven aralığı: Tasarruf ± t × σ_tasarruf (%90 güven)
├── Anlamlılık: Tasarruf > 2 × σ_tasarruf → İstatistiksel anlamlı
└── Raporlama: Aylık CUSUM grafiği + yıllık özet tablo

M&V raporu CUSUM bölümü:
1. Baseline modeli tanımı ve doğrulama
2. İzleme dönemi verileri ve beklenen tüketim
3. CUSUM tablosu ve grafiği
4. Kontrol sınırları ve istatistiksel anlamlılık
5. Toplam tasarruf ve belirsizlik
6. Kırılma noktası analizi (uygulanmış projelerin etkisi)
```

### 8.2 M&V Raporlarında CUSUM Sunumu

| Rapor Bölümü | CUSUM İçeriği | Format |
|-------------|-------------|--------|
| Yönetici özeti | Son CUSUM, toplam tasarruf, maliyet | 1 paragraf + 1 tablo |
| Metodoloji | CUSUM formülü, baseline model | Formüller + açıklama |
| Sonuçlar | CUSUM tablosu + grafik | Tablo + çizgi grafik |
| İstatistiksel analiz | Kontrol sınırları, güven aralığı | Formül + sonuç |
| Proje ayrıştırma | Kırılma noktası analizi | Eğim karşılaştırma |
| Sonuç | Yıllık tasarruf, geri ödeme | Özet tablo |

## 9. ExergyLab ile CUSUM (CUSUM in ExergyLab)

### 9.1 CUSUM Hesaplama ve Görselleştirme Önerisi

```
ExergyLab CUSUM modülü tasarım önerisi:

Girdi:
├── Baseline dönem: Kullanıcı seçimi (12-36 ay)
├── Enerji verisi: Aylık tüketim (otomatik veya manuel)
├── İlgili değişkenler: Üretim, iklim (CDD/HDD), çalışma saati
└── İzleme dönemi: Otomatik (baseline sonrası)

İşleme:
├── Regresyon modeli otomatik kurulumu (OLS)
├── Model doğrulama (R², CV-RMSE, NMBE)
├── CUSUM hesaplama (dönemsel ve kümülatif)
├── Kontrol sınırları (±2σ√n)
├── Change point tespiti (eğim analizi)
└── Alarm kontrolü

Çıktı:
├── CUSUM grafiği (interaktif, zoom, hover)
├── Tasarruf/kayıp özet tablosu
├── Kontrol sınırları görselleştirme
├── Change point işaretleme (proje tarihleri ile eşleştirme)
├── Aylık rapor (PDF export)
└── Exergy CUSUM — Exergy bazlı CUSUM (η_ex trendi)

Exergy CUSUM (benzersiz):
├── CUSUMₙ,ex = Σ(η_ex,i,gerçek - η_ex,i,baseline)
├── Exergy verimi baseline'ına göre kümülatif sapma
├── Termodinamik kalite değişimini izler
└── Enerji CUSUM + Exergy CUSUM birlikte → tam resim
```

### 9.2 ExergyLab Veri Akışı

```
ExergyLab mevcut analiz → CUSUM entegrasyonu:

Adım 1: Ekipman analizi yapılır (exergy verim, kayıp)
Adım 2: Sonuçlar zamanla biriktirilir (aylık snapshot)
Adım 3: 12+ aylık veri biriktiğinde baseline oluşturulur
Adım 4: CUSUM izleme başlar
Adım 5: Yeni analiz yapıldığında CUSUM güncellenir
Adım 6: Alarm ve bildirim kontrolü
Adım 7: Periyodik rapor üretimi
```

## 10. İlgili Dosyalar

- [Enerji Yönetimi INDEX](INDEX.md) — Dosya navigasyonu
- [Baseline ve EnPI](baseline_enpi.md) — Regresyon modeli ve EnB oluşturma
- [EnPI Rehberi](enpi_guide.md) — Enerji performans göstergeleri
- [M&T Sistemi](monitoring_targeting.md) — İzleme ve hedefleme
- [M&V İstatistikleri](mv_statistics.md) — Regresyon ve belirsizlik analizi
- [Performans Göstergeleri](../performance_indicators.md) — Fabrika seviyesi göstergeler

## 11. Referanslar

- Page, E.S., "Continuous Inspection Schemes", Biometrika, Vol.41, 1954
- Carbon Trust, "Monitoring and Targeting in Large Companies", CTG008
- CIBSE, "TM22: Energy Assessment and Reporting Methodology"
- ISO 50015:2014, "Measurement and verification of energy performance of organizations"
- IPMVP, "International Performance Measurement and Verification Protocol, Volume I", EVO 10000-1:2012
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- ETSU/Carbon Trust, "Energy Management Priorities — A Self Assessment Tool"
- Kissock, K., Seryak, J., "Understanding Manufacturing Energy Use Through Statistical Analysis", ACEEE, 2004
- Montgomery, D.C., "Statistical Quality Control", 8th ed., Wiley, 2019
- US DOE, "M&V Guidelines: Measurement and Verification for Performance-Based Contracts"
