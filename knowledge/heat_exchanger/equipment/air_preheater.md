---
title: "Hava Ön Isıtıcıları (Air Preheaters)"
category: equipment
equipment_type: heat_exchanger
subtype: "Hava Ön Isıtıcı"
keywords: [hava ön ısıtıcı, air preheater, APH, Ljungström, döner, borulu, plakalı, yanma verimi]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md, heat_exchanger/equipment/economizer.md, boiler/solutions/air_preheater.md]
use_when: ["Hava ön ısıtıcı analizi yapılırken", "Yanma havası ön ısıtma değerlendirilirken", "Döner tip APH kaçak analizi yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Hava Ön Isıtıcıları — Air Preheaters (APH)

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Hava ön ısıtıcıları (air preheaters — APH), kazan baca gazının artık ısısını kullanarak yanma havasını ön ısıtan ısı eşanjörleridir. Yanma havasının ön ısıtılması yanma odasında alev sıcaklığını artırarak yakıt tasarrufu sağlar ve yanma stabilitesini iyileştirir.

- Kapasite aralığı: 100 kW - 100+ MW
- Baca gazı giriş sıcaklığı: 200-500°C (ekonomizer çıkışı veya doğrudan)
- Baca gazı çıkış sıcaklığı: 100-180°C
- Yanma havası giriş sıcaklığı: 0-35°C (ortam havası)
- Yanma havası çıkış sıcaklığı: 150-400°C (yakıt ve tasarıma bağlı)
- Tipik yakıt tasarrufu: %2-5 (baca gazı sıcaklığı düşüşüne bağlı)
- Tipik exergy verimi: 30-55%

## Hava Ön Isıtıcı Tipleri

### Tip Karşılaştırma Tablosu

| Özellik | Döner (Ljungström) | Borulu (Tubular) | Plakalı (Plate) |
|---------|-------------------|------------------|-----------------|
| Çalışma prensibi | Rejeneratif (döner matris) | Rekuperatif (sürekli) | Rekuperatif (sürekli) |
| Kapasite aralığı | 5-100+ MW | 0.1-50 MW | 0.5-30 MW |
| Hava sızıntısı | %5-15 (kaçınılmaz) | ~0% | ~0% |
| Isı transfer alanı yoğunluğu | Çok yüksek (100-300 m²/m³) | Düşük (30-80 m²/m³) | Orta (50-150 m²/m³) |
| Kompaktlık | Çok kompakt | Büyük | Orta |
| Basınç düşüşü | Düşük-Orta | Orta | Orta-Yüksek |
| Korozyon riski | Yüksek (soğuk uç) | Orta | Orta |
| Bakım | Sık (conta, element değişimi) | Nadir | Nadir |
| Maliyet (aynı kapasite) | Referans | 1.5-2.5× | 1.2-1.8× |
| Endüstriyel yaygınlık | Büyük santraller (%75+) | Orta ölçekli kazanlar | Endüstriyel kazanlar |

## Döner Hava Ön Isıtıcı (Ljungström Tipi)

### Çalışma Prensibi

```
Ljungström döner hava ön ısıtıcı:

  Döner disk (rotor):
    Metal matris elemanları ile dolu
    Yavaş dönme: 1-3 rpm

  Çalışma döngüsü:
    1. Sıcak baca gazı → matris elemanlarını ısıtır (depolama)
    2. Rotor 180° döner
    3. Soğuk yanma havası → ısınmış matris elemanlarından ısı alır
    4. Rotor tekrar döner → sürekli çevrim

  Kesit görünümü (üstten):

    BACA GAZI tarafı  |  HAVA tarafı
    (sıcak → soğuk)   |  (soğuk → sıcak)
    ─────────────────  ↻  ─────────────────
    ←←←←← Sıcak baca  |  Soğuk hava →→→→→
    ←←←←← gazı         |  Ön ısıtılmış hava →→→
    ─────────────────  ↻  ─────────────────

  Dönme yönü: Baca gazı tarafından hava tarafına (saat yönü veya tersi)
```

### Matris Elemanı Tipleri

| Eleman Tipi | Malzeme | Isı Transfer Alanı | Kirlenme Eğilimi | Uygulama |
|-------------|---------|--------------------|--------------------|----------|
| Dalgalı levha (corrugated) | Karbon çelik, düşük alaşım | Çok yüksek | Orta | Sıcak uç (hot end) |
| Ondüle (undulated) | Karbon çelik | Yüksek | Düşük | Genel amaçlı |
| Kasetli (basket) | Emaye kaplı çelik | Orta | Düşük | Soğuk uç (cold end) |
| Seramik | Alümina, kordierit | Yüksek | Düşük | Çok yüksek sıcaklık |

### Sıcak Uç ve Soğuk Uç

```
Ljungström APH sıcaklık bölgeleri:

  SICAK UÇ (Hot End):
    Baca gazı giriş: 300-500°C
    Hava çıkış: 250-400°C
    Malzeme: Karbon çelik, düşük alaşım çelik
    Sorun: Yüksek sıcaklık oksidasyonu

  SOĞUK UÇ (Cold End):
    Baca gazı çıkış: 100-170°C
    Hava giriş: 0-35°C
    Malzeme: Emaye kaplı, Corten çelik, SS
    Sorun: Asit yoğuşması, korozyon, kirlenme

  Kritik bölge: Soğuk uçta metal sıcaklığı asit çiğ noktasının
  altına düşebilir → sülfürik asit yoğuşması → korozyon ve tıkanma
```

### Sızıntı (Leakage) Analizi

Döner APH'lerin en önemli dezavantajı kaçınılmaz hava sızıntısıdır.

```
Sızıntı kaynakları:

  1. Radyal conta (radial seal): %40-50 toplam sızıntının
     → Rotor kenarı ile sabit yapı arasındaki boşluk
  2. Eksenel conta (axial seal): %25-35 toplam sızıntının
     → Bölme plakaları ile rotor arasındaki boşluk
  3. Çevresel conta (circumferential seal): %15-25 toplam sızıntının
     → Rotor dış çevresi ile gövde arasındaki boşluk

Sızıntı oranı hesabı:
  Sızıntı (%) = (V_hava,çıkış - V_hava,giriş) / V_hava,giriş × 100

  veya O₂ bazlı:
  Sızıntı (%) ≈ (O₂_APH_çıkış - O₂_APH_giriş) / (21 - O₂_APH_çıkış) × 100

Burada:
  O₂ değerleri kuru bazda (%) ölçülür
  21 = Havanın O₂ oranı (%)

Sızıntı oranı benchmarkları:
  Yeni APH: %5-8
  Bakımlı APH: %8-12
  Eski/bakımsız APH: %12-20+

Sızıntının enerji etkisi:
  Her %1 ek sızıntı ≈ %0.5-1.0 baca gazı kayıp artışı
  (Fazla hava → baca gazı sıcaklığı yükselir)
```

### Sızıntı Azaltma Yöntemleri

| Yöntem | Azaltma | Maliyet | Not |
|--------|---------|---------|-----|
| Conta değişimi (seal replacement) | -%3-5 puan | Orta | Her 3-5 yılda bir |
| Sıcak sektör ayarı | -%1-2 puan | Düşük | Periyodik bakım |
| Çift conta sistemi | -%2-4 puan | Yüksek | Yeni APH tasarımları |
| Otomatik conta ayar sistemi | -%2-3 puan | Yüksek | Sürekli optimizasyon |

## Borulu Hava Ön Isıtıcı (Tubular APH)

### Yapı ve Çalışma

```
Borulu APH yapısı:

  Borular içinde: Baca gazı (sıcak)
  Borular dışında: Yanma havası (soğuk)

  ┌─────────────────────────────────┐
  │  → → → → → → → → → → → (baca gazı, boru içi)
  │  ← ← ← ← ← ← ← ← ← ← ← (hava, boru dışı)
  │  → → → → → → → → → → →
  │  ← ← ← ← ← ← ← ← ← ← ←
  └─────────────────────────────────┘

  Akış düzeni: Genellikle karşı akış veya çapraz akış
  Boru malzemesi: Karbon çelik (standart), emaye (soğuk uç)
  Boru çapı: 40-65 mm (standart)
  Boru et kalınlığı: 1.5-3.0 mm
```

### Avantajlar ve Dezavantajlar

| Avantaj | Dezavantaj |
|---------|------------|
| Sızıntı yok (sızdırmaz kaynak) | Büyük boyut ve ağırlık |
| Basit yapı, düşük bakım | Termal genleşme sorunu |
| Kolay temizlik (boru iç/dış) | Tıkanma riski (dar boru) |
| Güvenilir çalışma | Soğuk uç korozyonu |
| Uzun ömür (15-25 yıl) | Yüksek maliyet (büyük ölçekte) |

## Plakalı Hava Ön Isıtıcı (Plate Type APH)

### Yapı ve Çalışma

```
Plakalı APH yapısı:

  Paralel plakalar arasında alternatif kanallar:
    Kanal 1: Baca gazı →
    Kanal 2: Hava ←
    Kanal 3: Baca gazı →
    Kanal 4: Hava ←
    ...

  Akış düzeni: Karşı akış veya çapraz akış
  Plaka malzemesi: Karbon çelik, paslanmaz çelik
  Plaka kalınlığı: 1.0-3.0 mm
  Kanal aralığı: 5-15 mm
```

### Avantajlar ve Dezavantajlar

| Avantaj | Dezavantaj |
|---------|------------|
| Sızıntı yok | Büyük basınç düşüşü (dar kanal) |
| Orta kompaktlık | Kirlenme hassasiyeti (dar kanal) |
| Kolay modüler genişleme | Temizlik zorluğu |
| Düşük-orta maliyet | Termal genleşme yönetimi gerekli |

## Yanma Verimi İyileştirmesi

### Hava Ön Isıtma ve Yanma İlişkisi

```
Hava ön ısıtmanın yanma verimine etkisi:

  Teorik alev sıcaklığı artışı:
    ΔT_alev ≈ ΔT_hava × (cp_hava × m_hava) / (cp_yanma_ürünleri × m_yanma_ürünleri)

  Pratik kural:
    Her 20°C hava ön ısıtma → alev sıcaklığı ~25-30°C artar
    Her 20°C hava ön ısıtma → %1 yakıt tasarrufu

  Hava ön ısıtma yakıt tasarrufu formülü:
    η_tasarruf = cp_hava × (T_hava,çıkış - T_hava,giriş) / (LHV/m_hava_stok)

Burada:
  cp_hava       : Havanın özgül ısısı (~1.005 kJ/(kg·K))
  T_hava,çıkış  : Ön ısıtılmış hava sıcaklığı (°C)
  T_hava,giriş  : Ortam hava sıcaklığı (°C)
  LHV           : Yakıt alt ısıl değeri (kJ/kg)
  m_hava_stok   : Stokiyometrik hava miktarı (kg_hava/kg_yakıt)
```

### Yakıta Göre Tipik Hava Ön Isıtma Sıcaklıkları

| Yakıt | Hava Ön Isıtma (°C) | Yakıt Tasarrufu (%) | Not |
|-------|---------------------|---------------------|-----|
| Doğalgaz | 150-300 | %2-5 | Düşük asit çiğ noktası avantajı |
| Fuel oil (düşük S) | 150-250 | %2-4 | Asit yoğuşma dikkat |
| Fuel oil (yüksek S) | 120-200 | %1-3 | Soğuk uç korozyonu sınırlayıcı |
| Kömür (bitümlü) | 200-350 | %3-5 | Kül tıkanma ve korozyon dikkat |
| Kömür (linyit) | 150-300 | %2-4 | Yüksek nem, düşük ısıl değer |
| Biyokütle | 150-250 | %2-4 | Kül ergiyen sıcaklık dikkat |

## Soğuk Uç Korozyonu

### Korozyon Mekanizması

```
Soğuk uç korozyon süreci:

  1. Baca gazında SO₃ + H₂O → H₂SO₄ (sülfürik asit buharı)
  2. Metal yüzey sıcaklığı asit çiğ noktasının altına düşer
  3. H₂SO₄ yoğuşması → sıvı asit film oluşur
  4. Asidik korozyon başlar
  5. Korozyon ürünleri + kül partikülleri → yapışkan birikim
  6. Birikim → akış kanalı daralması → kapasite düşüşü

Korozyon hızı (yaklaşık):
  Karbon çelik: 2-5 mm/yıl (asit yoğuşma bölgesinde)
  Corten çelik: 1-3 mm/yıl
  Emaye kaplı: 0.05-0.2 mm/yıl
  SS316: 0.5-1.5 mm/yıl (zayıf H₂SO₄'te sınırlı direnç)
```

### Korozyon Önleme Stratejileri

| Strateji | Yöntem | Etkinlik | Maliyet |
|----------|--------|----------|---------|
| Minimum metal sıcaklığı kontrolü | Hava bypass ile soğuk uç sıcaklığını artırma | Yüksek | Düşük |
| Buhar serpantini (steam coil) | Hava girişini ön ısıtarak soğuk uç sıcaklığını artırma | Yüksek | Orta |
| Korozyona dayanıklı malzeme | Emaye kaplı veya Corten çelik eleman | Yüksek | Orta-Yüksek |
| Sıcak hava resirkülasyonu | Çıkış havasının bir kısmını girişe geri besleme | Orta | Düşük |
| Düşük kükürt yakıt | Doğalgaz veya düşük kükürt yakıta geçiş | Çok yüksek | Yakıt fiyatına bağlı |
| Nötrleştirme enjeksiyonu | Ca(OH)₂ veya NaHCO₃ enjeksiyonu | Orta | Orta |

## Exergy Analizi — Hava Ön Isıtıcı

### Exergy Verimi

```
Hava ön ısıtıcı exergy verimi:

  η_ex = (Ex_hava,çıkış - Ex_hava,giriş) / (Ex_baca,giriş - Ex_baca,çıkış)

Hava exergysi (ideal gaz yaklaşımı):
  Ex_hava = m_hava × cp_hava × [(T - T₀) - T₀ × ln(T/T₀)]

Baca gazı exergysi:
  Ex_baca = m_baca × cp_baca × [(T - T₀) - T₀ × ln(T/T₀)]

Sızıntı etkisi (döner APH):
  Sızıntı exergy kaybı:
    Ex_sızıntı = m_sızıntı × ex_hava

  Düzeltilmiş exergy verimi:
    η_ex,net = η_ex × (1 - sızıntı_oranı)

Tipik exergy verimleri:
  Borulu APH: η_ex = 40-55% (sızıntı yok)
  Döner APH (yeni): η_ex,net = 35-50% (sızıntı ile)
  Döner APH (eski): η_ex,net = 25-40% (yüksek sızıntı ile)
  Plakalı APH: η_ex = 38-52% (sızıntı yok)
```

### Exergy Yıkım Kaynakları

| Kaynak | Payı (%) | Not |
|--------|---------|-----|
| Sonlu sıcaklık farkı (ΔT) | 50-70 | Gaz/gaz düşük U → büyük ΔT |
| Sızıntı kaybı (döner tip) | 10-25 | Yalnızca Ljungström |
| Basınç düşüşü | 5-15 | Fan gücü olarak ortaya çıkar |
| Kirlenme/tıkanma | 5-15 | Soğuk uç birikimi |
| Çevre kaybı | 2-5 | İzolasyon eksikliği |

### Exergy Optimizasyonu Stratejileri

| Strateji | Yöntem | Beklenen İyileşme |
|----------|--------|-------------------|
| Sızıntı azaltma | Conta bakımı, otomatik ayar | +%3-8 exergy verimi |
| Eleman yenileme | Sıcak/soğuk uç element değişimi | +%5-10 exergy verimi |
| Kirlenme temizleme | Kurum üfleme optimizasyonu | +%3-8 exergy verimi |
| Optimal boyutlandırma | Daha büyük APH (düşük ΔT) | +%5-15 exergy verimi |
| Tip seçimi | Borulu APH (sızıntısız) | +%5-10 exergy verimi (vs döner) |

## Bakım ve İzleme

### Periyodik Bakım Gereksinimleri

| Bakım İşlemi | Sıklık | Süre | Maliyet (EUR) |
|--------------|--------|------|---------------|
| Conta kontrolü ve ayarı (döner) | 3-6 ay | 4-8 saat | 500-2,000 |
| Kurum üfleme sistemi kontrolü | 1-3 ay | 2-4 saat | 200-500 |
| Soğuk uç element muayenesi | 6-12 ay | 8-16 saat | 1,000-3,000 |
| Element değişimi (soğuk uç) | 2-5 yıl | 2-5 gün | 10,000-50,000 |
| Element değişimi (sıcak uç) | 5-10 yıl | 3-7 gün | 15,000-80,000 |
| Tam yenileme (döner APH) | 15-25 yıl | 2-4 hafta | 100,000-500,000 |

### İzleme Parametreleri

| Parametre | Alarm Değeri | Kritik Değer |
|-----------|-------------|-------------|
| Baca gazı çıkış ΔT (giriş-çıkış) | <%30 azalma | <%50 azalma |
| Sızıntı oranı (O₂ artışı) | >%12 | >%18 |
| Basınç düşüşü (baca gazı tarafı) | >%150 tasarım | >%200 tasarım |
| Soğuk uç metal sıcaklığı | <asit çiğ noktası + 10°C | <asit çiğ noktası |
| Titreşim (döner) | >4 mm/s | >7 mm/s |

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Ekonomizer: `heat_exchanger/equipment/economizer.md`
- Reküperatör: `heat_exchanger/equipment/recuperator.md`
- Kazan hava ön ısıtıcı çözümü: `boiler/solutions/air_preheater.md`
- Kazan sistemi: `boiler/equipment/systems_overview.md`
- Kazan formülleri: `boiler/formulas.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`

## Referanslar

- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators: Design, Applications, and Calculations*, Marcel Dekker.
- Howden Group (2022). *Ljungström Air Preheater — Technical Reference*.
- U.S. DOE/AMO (2012). *Improving Steam System Performance: A Sourcebook for Industry*, 2nd Edition.
- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Shah, R.K. & Sekulić, D.P. (2003). *Fundamentals of Heat Exchanger Design*, John Wiley & Sons.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*, Wiley.
- EN 12952 — Water-tube Boilers and Auxiliary Installations.
- ASME PTC 4.3 — Air Heaters: Performance Test Codes.
- Verhoff, F.H. & Banchero, J.T. (1974). "Predicting Dew Points of Flue Gases," *Chemical Engineering Progress*, 70(8), 71-72.
