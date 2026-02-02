---
title: "Plakalı Eşanjörler (Plate Heat Exchangers)"
category: equipment
equipment_type: heat_exchanger
subtype: "Plakalı"
keywords: [eşanjör, plakalı, plate heat exchanger, GPHE, BPHE, contalı, lehimli, chevron, herringbone]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md, heat_exchanger/equipment/shell_and_tube.md]
use_when: ["Plakalı eşanjör analizi yapılırken", "Kompakt eşanjör seçimi gerektiğinde", "GPHE veya BPHE karşılaştırması yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Plakalı Eşanjörler — Plate Heat Exchangers

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Plakalı eşanjörler (plate heat exchangers — PHE), ince metal plakalar arasında akışkan kanalları oluşturarak yüksek ısı transfer verimliliği sağlayan kompakt eşanjörlerdir. Gövde-boru eşanjörlere kıyasla 3-5 kat daha yüksek toplam ısı geçiş katsayısı (U) ve %80-90 daha az hacim ile aynı kapasiteyi sağlarlar.

- Kapasite aralığı: 1 kW - 50 MW
- U değeri aralığı: 1,000-8,000 W/(m²·K) (sıvı/sıvı servisler)
- Basınç aralığı: Vakum - 45 bar (tip bağımlı)
- Sıcaklık aralığı: -195°C ile 350°C (tip bağımlı)
- Plaka kalınlığı: 0.4-1.0 mm (tipik 0.5-0.6 mm)
- Plaka malzemeleri: AISI 304, AISI 316, Titanyum, Hastelloy, Nickel
- Yaklaşma sıcaklığı: 1-3°C (gövde-boru: 5-10°C)

## Plakalı Eşanjör Tipleri

### Tip Karşılaştırma Tablosu

| Özellik | Contalı (GPHE) | Lehimli (BPHE) | Kaynaklı (Welded) | Yarı Kaynaklı (Semi-Welded) |
|---------|---------------|----------------|-------------------|----------------------------|
| Basınç (maks) | 25 bar | 45 bar | 40 bar | 30 bar |
| Sıcaklık (maks) | 200°C | 225°C | 350°C | 300°C |
| Plaka sayısı | 10-700+ | 10-200 | 50-500 | 50-400 |
| Kapasite | 5 kW - 50 MW | 1 kW - 5 MW | 50 kW - 30 MW | 50 kW - 20 MW |
| Bakım | Sökülebilir, plaka eklenebilir | Sökülemez | Sökülemez (bazı tiplerde kısmen) | Bir taraf sökülebilir |
| Kirlenme direnci | Çok iyi (temizlenebilir) | Kötü (CIP ile sınırlı) | Orta | İyi (açık taraf) |
| Conta gereksinimi | Evet (her plakada) | Hayır | Hayır | Bir tarafta |
| Göreceli maliyet | Orta | Düşük | Yüksek | Orta-Yüksek |
| Tipik uygulama | Gıda, HVAC, kimya | HVAC, soğutma, DHW | Kimya, petrokimya | Amonyak, agresif akışkan |

### Contalı Plakalı Eşanjör (GPHE — Gasketed Plate Heat Exchanger)

- En yaygın plakalı eşanjör tipi
- Plakalar arasında elastomer contalar ile sızdırmazlık
- Plaka ekleme/çıkarma ile kapasite ayarlanabilir
- Söküp mekanik temizlik yapılabilir

**Conta malzemeleri:**

| Conta Malzemesi | Maks Sıcaklık (°C) | Kimyasal Uyumluluk | Tipik Uygulama |
|----------------|---------------------|---------------------|----------------|
| NBR (Nitril) | 140 | Yağlar, hafif asitler | Soğutma suyu, yağ soğutma |
| EPDM | 160 | Su, buhar, bazlar, HCl | HVAC, gıda, buhar |
| Viton (FKM) | 200 | Asitler, HC, çözücüler | Kimya, petrokimya |
| HNBR (Hidrojenlenmiş nitril) | 150 | Yağlar, yakıtlar | Otomotiv, yağ servisleri |
| Silikon | 180 | Gıda ürünleri | Gıda (özel uygulamalar) |

### Lehimli Plakalı Eşanjör (BPHE — Brazed Plate Heat Exchanger)

- Plakalar bakır veya nikel lehim ile birleştirilir
- Conta yoktur — daha yüksek basınç ve sıcaklık dayanımı
- Kompakt, hafif, düşük maliyetli
- Söküp temizlik yapılamaz — CIP (kimyasal temizlik) ile bakım

**Lehim malzemeleri:**

| Lehim | Maks Sıcaklık (°C) | Maks Basınç (bar) | Uyumluluk | Not |
|-------|---------------------|-------------------|-----------|-----|
| Bakır (Cu) | 225 | 45 | Su, glikol, soğutucu | En yaygın, en ucuz |
| Nikel (Ni) | 400 | 40 | Amonyak, agresif kimyasal | Bakır uyumsuz akışkanlar |

### Kaynaklı Plakalı Eşanjör (Welded PHE)

- Plakalar lazer veya TIG kaynağı ile birleştirilir
- Conta yoktur — yüksek sıcaklık ve basınç
- Agresif ve tehlikeli akışkanlarda güvenilir sızdırmazlık
- Sökülüp temizlenemez (bazı modellerde kısmen mümkün)

**Kaynaklı PHE alt tipleri:**
- Tam kaynaklı (Alfa Laval Compabloc, AlfaRex)
- Kabuk-plaka (Shell & Plate — Vahterus Pshe)
- Blok tip (Heatric PCHE — Printed Circuit Heat Exchanger)

### Yarı Kaynaklı Plakalı Eşanjör (Semi-Welded PHE)

- Plaka çiftleri kaynaklı, çiftler arası contalı
- Kaynaklı taraf: agresif, toksik veya yüksek basınçlı akışkan
- Contalı taraf: temiz, ılımlı akışkan (temizlenebilir)
- Amonyak soğutma sistemlerinde popüler

## Plaka Korügasyon (Corrugation) Tasarımı

### Chevron (Herringbone) Açısı

Plakalı eşanjör performansının en kritik parametresi plaka korügasyon açısıdır.

```
Chevron açısı (β): Akış yönüne göre korügasyon açısı

  β = 25-30° → "Düşük teta" (L plaka)
    - Düşük ΔP, düşük h, düşük NTU
    - Yüksek debi, düşük viskozite akışkanlar

  β = 45-50° → "Orta teta" (M plaka)
    - Orta ΔP, orta h, orta NTU
    - Genel amaçlı

  β = 60-65° → "Yüksek teta" (H plaka)
    - Yüksek ΔP, yüksek h, yüksek NTU
    - Düşük debi, yüksek viskozite veya yakın sıcaklık yaklaşması

Karıştırma stratejisi:
  H+H, H+L, L+L plaka çiftleri kullanılarak
  ΔP ve NTU optimizasyonu yapılabilir
```

### Korügasyon Geometrisi

| Parametre | Tipik Aralık | Etkisi |
|-----------|-------------|--------|
| Korügasyon derinliği (b) | 2-5 mm | Kanal yüksekliği, ΔP |
| Korügasyon dalgaboyu (λ) | 7-15 mm | Türbülans yapısı |
| Plaka kalınlığı (t) | 0.4-1.0 mm | Basınç dayanımı, ısı iletimi |
| Chevron açısı (β) | 25-65° | h ve ΔP dengesi |
| Alan büyütme faktörü (φ) | 1.15-1.30 | Gerçek/projeksiyon alan oranı |

### Isı Transfer ve Basınç Düşüşü Korelasyonları

```
Plakalı eşanjör ısı transfer katsayısı:

  Nu = C₁ × Re^n × Pr^(1/3) × (μ/μ_w)^0.17

  h = Nu × k / D_h

Burada:
  D_h = 4 × b × w / (2 × (b + w × φ)) ≈ 2 × b / φ   (dar kanal yaklaşımı)
  Re  = ρ × v × D_h / μ
  b   = Korügasyon derinliği (m)
  w   = Plaka genişliği (m)
  φ   = Alan büyütme faktörü

Tipik korelasyon sabitleri:
  β = 30°: C₁ = 0.40, n = 0.60
  β = 45°: C₁ = 0.30, n = 0.66
  β = 60°: C₁ = 0.20, n = 0.73

Basınç düşüşü:
  ΔP = f × (L_eff / D_h) × ρ × v² / 2 + 1.4 × ρ × v²_port / 2

  f = C₂ / Re^m

Tipik sürtünme faktörü sabitleri:
  β = 30°: C₂ = 10, m = 0.30
  β = 60°: C₂ = 40, m = 0.25
```

## Gövde-Boru ile Karşılaştırma

### Avantajlar

| Özellik | GPHE | S&T | Fark |
|---------|------|-----|------|
| U değeri (su/su) | 3,000-6,000 W/(m²·K) | 800-1,500 W/(m²·K) | 3-5× yüksek |
| Yaklaşma sıcaklığı | 1-3°C | 5-10°C | 2-5× daha yakın |
| Hacim (aynı kapasite) | 1 | 3-5 | %60-80 küçük |
| Ağırlık (aynı kapasite) | 1 | 3-6 | %65-85 hafif |
| Sıvı tutma hacmi | 1 | 5-10 | Hızlı yanıt, az atık |
| Kirlenme eğilimi | Düşük (yüksek türbülans) | Orta-yüksek | Daha temiz çalışma |
| NTU kapasitesi | 5-8 (tek ünite) | 1-2 (tek gövde geçişi) | Yüksek etkinlik |
| Temizlik (GPHE) | Kolay (sökme) | Orta (mekanik/CIP) | Daha hızlı bakım |
| Kapasite değişikliği | Plaka ekleme/çıkarma | Mümkün değil | Esnek |

### Sınırlamalar

| Kısıt | GPHE | S&T |
|-------|------|-----|
| Maksimum basınç | 25 bar | 300+ bar |
| Maksimum sıcaklık | 200°C (conta sınırı) | 600°C+ |
| Büyük kapasite | 50 MW'a kadar | 500 MW+ |
| Faz değişimi servisleri | Sınırlı (özel tasarım) | Geniş deneyim |
| Yüksek viskozite | >50 cP zor | Baffle ile daha iyi |
| Katı partikül | >2 mm sorunlu | >5 mm toleranslı |
| Conta uyumluluğu | Kimyasal sınırlama | Conta yok |

## Tipik Uygulamalar

| Uygulama | Tercih Edilen Tip | Kapasite | Not |
|----------|-------------------|----------|-----|
| HVAC — serbest soğutma | GPHE, BPHE | 100-5,000 kW | Soğutma suyu / kule suyu |
| HVAC — ısı geri kazanımı | BPHE | 10-500 kW | Sıcak su hazırlama |
| Süt pastörizasyonu | GPHE (SS316) | 50-5,000 kW | 72°C/15s, CIP |
| Bira/meyve suyu soğutma | GPHE (SS316) | 50-2,000 kW | Gıda onaylı |
| Soğutma sistemi evaporatör | BPHE (bakır lehim) | 10-2,000 kW | R410A, R134a |
| Soğutma sistemi kondenser | BPHE (bakır lehim) | 10-2,000 kW | R410A, R134a |
| Bölge ısıtma alt istasyonu | GPHE | 100-10,000 kW | İlk/ikincil devre ayırma |
| Amonyak soğutma | Yarı kaynaklı | 50-5,000 kW | NH₃ güvenliği |
| Kimyasal proses | Kaynaklı | 100-30,000 kW | Agresif akışkan |
| Sıcak su hazırlama (DHW) | BPHE, GPHE | 10-1,000 kW | Legionella dikkat |
| Yüzme havuzu ısıtma | BPHE (Ti) | 50-500 kW | Klorlu su |
| Motor/jeneratör soğutma | BPHE | 50-2,000 kW | Glikol/su |

## NTU Kapasitesi ve Etkinlik

### Plakalı Eşanjörlerin NTU Avantajı

```
NTU (Number of Transfer Units) = U × A / C_min

Plakalı eşanjör NTU kapasitesi:
  Tek ünite: NTU = 3-8 (gövde-boru: NTU = 1-2 tek geçiş)
  Etkinlik: ε = 0.90-0.98 (gövde-boru: ε = 0.60-0.85 tek gövde geçişi)

NTU-etkinlik ilişkisi (saf karşı akış):
  ε = [1 - exp(-NTU × (1 - C_r))] / [1 - C_r × exp(-NTU × (1 - C_r))]

Burada:
  C_r = C_min / C_max

Pratikte plakalı eşanjörde:
  NTU = 1 → ε ≈ 0.50-0.63
  NTU = 2 → ε ≈ 0.67-0.80
  NTU = 4 → ε ≈ 0.80-0.92
  NTU = 6 → ε ≈ 0.86-0.96
  NTU = 8 → ε ≈ 0.89-0.98
```

## Exergy Analizi — Plakalı Eşanjör

### Exergy Verimi Karşılaştırması

| Parametre | Plakalı (GPHE) | Gövde-Boru (S&T) | Not |
|-----------|---------------|-------------------|-----|
| Yaklaşma sıcaklığı | 2°C | 8°C | PHE avantajı |
| ΔT_lm (tipik) | 3-8°C | 10-25°C | Düşük ΔT = düşük exergy yıkımı |
| Exergy verimi | 75-92% | 50-75% | +15-25 puan avantaj |
| Basınç düşüşü exergy kaybı | 0.5-2.0 kW | 0.3-1.5 kW | PHE biraz daha yüksek |
| Net exergy verimi | 72-88% | 48-72% | PHE net kazanç |

### Exergy Yıkım Bileşenleri

```
Plakalı eşanjör exergy yıkımı:

  Ex_yıkım,toplam = Ex_yıkım,ΔT + Ex_yıkım,ΔP

Sıcaklık farkından:
  Ex_yıkım,ΔT = T₀ × [m_c × cp_c × ln(T_c,out/T_c,in) + m_h × cp_h × ln(T_h,out/T_h,in)]

Basınç düşüşünden:
  Ex_yıkım,ΔP = m_c × v_c × ΔP_c + m_h × v_h × ΔP_h
  (sıkıştırılamaz akışkan yaklaşımı)

Burada:
  v = Özgül hacim (m³/kg)
  ΔP = Akışkan basınç düşüşü (Pa)
  T₀ = Referans çevre sıcaklığı (K)

Tipik oran: Ex_yıkım,ΔT / Ex_yıkım,toplam = %80-95
  → Sıcaklık farkı dominant exergy yıkım kaynağıdır
```

### Exergy Optimizasyonu Stratejileri

| Strateji | Yöntem | Exergy İyileşmesi | Dezavantaj |
|----------|--------|-------------------|------------|
| Yaklaşma sıcaklığı azaltma | Daha fazla plaka | +%5-15 | Artan maliyet ve ΔP |
| Chevron açısı optimizasyonu | H/L plaka kombinasyonu | +%3-8 | Üretici ile işbirliği gerekli |
| Çok geçişli düzen | Seri/paralel plaka düzeni | +%5-10 | Karmaşıklık |
| Kirlenme minimizasyonu | CIP programı, filtrasyon | +%5-20 geri kazanım | İşletme maliyeti |
| Plaka malzemesi | Yüksek iletkenlikli plaka | +%1-3 | Maliyet |

## Boyutlandırma Hızlı Referans

```
Hızlı boyutlandırma (GPHE, su/su servisi):

  Gereken alan: A = Q / (U × ΔT_lm)

  Tipik U (su/su): 3,500 W/(m²·K) (orta kirlenme dahil)

  Örnek:
    Q = 500 kW, ΔT_lm = 5°C
    A = 500,000 / (3,500 × 5) = 28.6 m²
    Plaka alanı = 0.3 m²/plaka (orta boy)
    Plaka sayısı ≈ 28.6 / 0.3 ≈ 96 plaka (her kanal için bir plaka)

  Karşılaştırma (S&T, su/su):
    U = 1,000 W/(m²·K)
    A = 500,000 / (1,000 × 8) = 62.5 m² (ΔT_lm daha büyük)
    → PHE: %54 daha küçük alan
```

## Bakım ve İşletme

### Temizlik Yöntemleri

| Yöntem | Uygulama | Sıklık | Not |
|--------|----------|--------|-----|
| CIP (Clean-in-Place) | BPHE, GPHE (sökmeden) | 3-12 ayda bir | NaOH (yağ), HNO₃ (kireç), fosforik asit |
| Mekanik temizlik | GPHE (sökerek) | 1-3 yılda bir | Yüksek basınçlı su, fırça |
| Ultrasonik temizlik | Şiddetli kirlenme | Gerektiğinde | BPHE için tek seçenek |
| Geri yıkama (backflush) | Partikül kırılması | Gerektiğinde | Ters yönde akış |

### Conta Ömrü ve Değişim

| Conta Malzemesi | Tipik Ömür | Değişim Maliyeti | Not |
|----------------|-----------|-----------------|-----|
| NBR | 5-8 yıl | Eşanjör fiyatının %15-25'i | Yağ servisleri |
| EPDM | 8-12 yıl | Eşanjör fiyatının %15-25'i | Su/buhar servisleri |
| Viton (FKM) | 5-10 yıl | Eşanjör fiyatının %25-40'ı | Kimyasal servisler |

## Maliyet Tahmini

| Tip | Kapasite | Tahmini Maliyet (EUR) | Spesifik Maliyet (EUR/kW) |
|-----|----------|----------------------|--------------------------|
| BPHE | 50 kW | 300-800 | 6-16 |
| BPHE | 500 kW | 1,500-4,000 | 3-8 |
| GPHE (SS316) | 500 kW | 5,000-15,000 | 10-30 |
| GPHE (SS316) | 5,000 kW | 25,000-80,000 | 5-16 |
| Kaynaklı PHE | 1,000 kW | 15,000-50,000 | 15-50 |
| Yarı kaynaklı | 1,000 kW | 10,000-35,000 | 10-35 |

## Ölçülmesi Gereken Parametreler

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Sıcak giriş/çıkış sıcaklığı | °C | Servise bağlı | PT100 |
| Soğuk giriş/çıkış sıcaklığı | °C | Servise bağlı | PT100 |
| Debi (her taraf) | m³/h veya L/s | Servise bağlı | EM veya ultrasonik debimetre |
| Basınç düşüşü | kPa | 10-100 | Diferansiyel basınç sensörü |
| Conta durumu | — | — | Görsel muayene, sızıntı testi |

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Gövde-boru eşanjör: `heat_exchanger/equipment/shell_and_tube.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Chiller evaporatör/kondenser: `chiller/equipment/water_cooled.md`
- Serbest soğutma: `chiller/solutions/free_cooling.md`
- Fabrika ısı entegrasyonu: `factory/heat_integration.md`

## Referanslar

- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Shah, R.K. & Focke, W.W. (1988). "Plate Heat Exchangers and Their Design Theory," in *Heat Transfer Equipment Design*, Hemisphere.
- Alfa Laval (2023). *Plate Heat Exchanger — Technical Reference Manual*.
- SWEP International (2022). *Brazed Plate Heat Exchanger — Engineering Handbook*.
- Wang, L., Sundén, B., Manglik, R.M. (2007). *Plate Heat Exchangers: Design, Applications, and Performance*, WIT Press.
- Martin, H. (1996). "A Theoretical Approach to Predict the Performance of Chevron-Type Plate Heat Exchangers," *Chemical Engineering and Processing*, 35(4), 301-310.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- EN 14825:2022 — Air conditioners, liquid chilling packages and heat pumps.
- ASME BPVC Section VIII — Boiler and Pressure Vessel Code (basınçlı kaplar).
