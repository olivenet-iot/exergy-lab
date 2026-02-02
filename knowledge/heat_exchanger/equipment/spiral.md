---
title: "Spiral Eşanjörler (Spiral Heat Exchangers)"
category: equipment
equipment_type: heat_exchanger
subtype: "Spiral"
keywords: [eşanjör, spiral, spiral heat exchanger, SHE, öz temizleme, yüksek viskozite, çamur]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md]
use_when: ["Spiral eşanjör analizi yapılırken", "Kirli veya yüksek viskoziteli akışkan servisi değerlendirilirken", "Öz temizleme özelliği gereken uygulamalarda"]
priority: medium
last_updated: 2026-02-01
---
# Spiral Eşanjörler — Spiral Heat Exchangers (SHE)

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Spiral eşanjörler (spiral heat exchangers — SHE), iki ayrı metal levhanın spiral şeklinde sarılmasıyla oluşturulan iki ayrı spiral kanala sahip ısı değiştiricileridir. Bu benzersiz geometri, yüksek türbülans, öz temizleme özelliği ve kompakt yapı sağlar. Özellikle kirli, çamurlı ve yüksek viskoziteli akışkanlarda üstün performans gösterir.

- Kapasite aralığı: 10 kW - 30 MW
- Basınç aralığı: Vakum - 25 bar (standart), 40 bar'a kadar (özel)
- Sıcaklık aralığı: -50°C ile 400°C
- Tipik U değeri: 500-4,000 W/(m²·K)
- Kanal genişliği: 5-25 mm
- Plaka kalınlığı: 2-10 mm (basınç ve korozyona bağlı)
- Plaka malzemeleri: Karbon çelik, SS304, SS316, SS316L, Duplex SS, Hastelloy, Titanyum

## Yapı ve Çalışma Prensibi

### Spiral Kanal Oluşumu

```
Spiral eşanjör kesiti (üstten görünüm):

    ┌──────────────────┐
    │   ╭─────╮        │
    │  ╭│     │╮       │
    │ ╭ │  ○  │ ╮      │
    │  ╰│     │╯       │
    │   ╰─────╯        │
    └──────────────────┘

  ○ = Merkez (center post)
  İki spiral kanal: Akışkan A ve Akışkan B
  Her kanal tek geçişli (single pass)
  Akışkanlar karşı yönde akar (karşı akış)

Kanal oluşumu:
  İki ayrı metal levha merkez direkte birleştirilir
  Levhalar arası mesafe ayırıcı çubuklarla (spacer studs) sabitlenir
  Her levha tam bir spiral kanalın iki duvarını oluşturur
```

### Akış Düzenleri

| Tip | Akışkan A | Akışkan B | Uygulama |
|-----|-----------|-----------|----------|
| Tip I — Spiral/Spiral | Spiral akış | Spiral akış (karşı yön) | Sıvı/sıvı ısı transferi |
| Tip II — Spiral/Çapraz | Spiral akış | Eksenel (çapraz) akış | Yoğuşma veya buharlaşma |
| Tip III — Çapraz/Çapraz | Eksenel akış | Eksenel akış | Özel uygulamalar |

### Tip I — Spiral-Spiral (En Yaygın)

```
Tip I akış düzeni (kesit):

  Akışkan A: Merkezden dışarı spiral → (sıcak)
  Akışkan B: Dışarıdan merkeze spiral ← (soğuk)

  Saf karşı akış sağlanır (F = 1.00)
  Her kanal tek geçişlidir

  Giriş/çıkış bağlantıları:
    A giriş: Merkez (veya dış çevre)
    A çıkış: Dış çevre (veya merkez)
    B giriş: Dış çevre (veya merkez)
    B çıkış: Merkez (veya dış çevre)
```

### Tip II — Spiral-Çapraz

```
Tip II akış düzeni:

  Akışkan A: Spiral akış (sıvı veya gaz)
  Akışkan B: Yukarıdan aşağı (veya tersi) eksenel akış (yoğuşan buhar veya kaynayan sıvı)

  Uygulamalar:
    - Buhar yoğuşturucusu (kondenser)
    - Evaporatör (buharlaştırıcı)
    - Üst (top) kondenser

  Buhar/gaz tarafı açık — eksenel akışa izin verir
  Sıvı tarafı kapalı — spiral akış zorlanır
```

## Öz Temizleme Özelliği (Self-Cleaning)

### Mekanizma

```
Öz temizleme prensibi:

  Tek kanallı spiral yapı → tüm akışkan tek bir kanaldan geçer
  Tıkanma başladığında → akış kesiti daralır
  Daralan kesit → yerel hız artar (süreklilik denklemi: A₁V₁ = A₂V₂)
  Artan hız → artan kesme gerilmesi (τ = μ × dv/dy)
  Artan kesme → birikinti koparak sürüklenir

Karşılaştırma:
  S&T eşanjörde: Bir boru tıkanırsa akışkan diğer borulara yönelir
                 → tıkanan boru temizlenmez, sorun büyür
  Spiral eşanjörde: Tek kanal → tıkanma otomatik temizlenir
```

### Öz Temizleme Performans Verisi

| Servis | S&T Temizlik Sıklığı | Spiral Temizlik Sıklığı | Tasarruf |
|--------|---------------------|------------------------|----------|
| Kağıt hamuru (siyah çözelti) | 1-2 hafta | 3-6 ay | %85-95 daha az bakım |
| Atıksu çamuru | 2-4 hafta | 6-12 ay | %80-90 daha az bakım |
| Gıda (şeker kristalizasyonu) | 1-3 hafta | 2-4 ay | %75-85 daha az bakım |
| Biyogaz çamuru | 2-4 hafta | 6-12 ay | %80-90 daha az bakım |
| Lif içeren süspansiyon | 1-2 hafta | 3-6 ay | %85-90 daha az bakım |

## Yüksek Viskoziteli Akışkan İşleme

### Viskozite ve Isı Transferi

```
Yüksek viskoziteli akışkanlarda spiral eşanjör avantajı:

  Spiral geometri → düşük Re'de bile türbülans
  Dean vorteksleri (secondary flow) → kanal eğriliğinden kaynaklanan ikincil akış

  Kritik Reynolds sayısı (türbülansa geçiş):
    Düz boru: Re_kr ≈ 2,300
    Spiral kanal: Re_kr ≈ 500-1,000 (eğrilik etkisi)

  Bu durum, viskoz akışkanlarda spiral eşanjörün h değerini
  S&T eşanjöre göre 2-5 kat daha yüksek yapabilir.

Dean sayısı:
  De = Re × √(D_h / 2R)

Burada:
  D_h : Kanal hidrolik çapı (m)
  R   : Spiral eğrilik yarıçapı (m)
  De > 40 → ikincil akış belirgin
```

### Viskozite Sınıflarına Göre Performans

| Viskozite (cP) | S&T h (W/(m²·K)) | Spiral h (W/(m²·K)) | Spiral Avantajı |
|----------------|-------------------|---------------------|-----------------|
| 1-10 (su benzeri) | 1,000-3,000 | 1,500-4,000 | 1.3-1.5× |
| 10-100 (hafif yağ) | 200-800 | 500-1,500 | 2-3× |
| 100-1,000 (ağır yağ) | 50-200 | 200-600 | 3-4× |
| 1,000-10,000 (çok viskoz) | 20-80 | 80-300 | 3-5× |

## Çamurlu Akışkan (Slurry) Servisi

### Spiral Eşanjörün Çamur Avantajı

| Özellik | Spiral | S&T | PHE |
|---------|--------|-----|-----|
| Katı partikül toleransı | <50 mm | <5 mm (boru çapına bağlı) | <2 mm |
| Lif toleransı | Yüksek | Düşük (tıkanma) | Çok düşük |
| Çamur konsantrasyonu | <%30 katı | <%5 katı | <%1 katı |
| Tıkanma riski | Çok düşük (öz temizleme) | Yüksek | Çok yüksek |
| Aşınma (erozyon) | Orta (sabit hız) | Yüksek (giriş bölgesinde) | Yüksek |

### Tipik Çamur Uygulamaları

| Uygulama | Katı Oranı | Sıcaklık | Not |
|----------|-----------|----------|-----|
| Atıksu çamuru ısıtma | %3-8 | 20-60°C | Anaerobik çürütücü besleme |
| Biyogaz digestat | %5-12 | 35-55°C | Mezofilik/termofilik |
| Kağıt hamuru | %3-15 | 40-180°C | Siyah/beyaz çözelti |
| Maden çamuru | %10-25 | 20-80°C | Flotasyon, liç |
| Gıda çamuru | %5-20 | 20-130°C | Şeker, nişasta |
| Boya/pigment | %10-30 | 20-100°C | Kimya sanayi |

## Avantajlar ve Sınırlamalar

### Avantajlar

| Avantaj | Açıklama |
|---------|----------|
| Öz temizleme | Tek kanallı yapı ile otomatik tıkanma önleme |
| Yüksek türbülans | Spiral eğrilik ile Dean vorteksleri — düşük Re'de bile |
| Saf karşı akış | Tip I'de F = 1.00 |
| Kompakt yapı | S&T'ye göre %40-60 daha küçük (aynı kapasite) |
| Düşük kirlenme | Yüksek türbülans + öz temizleme |
| Viskoz akışkanlar | Düşük Re'de yüksek h |
| Çamur/lif toleransı | Büyük partikül ve liflere dayanıklı |
| Tek nokta bakım | Üst/alt kapaklar açılarak erişim (Tip I) |

### Sınırlamalar

| Sınırlama | Açıklama |
|-----------|----------|
| Basınç limiti | Standart: 25 bar, maksimum 40 bar |
| Sıcaklık limiti | 400°C (conta ve malzeme sınırı) |
| Büyük kapasiteler | >30 MW için S&T tercih edilir |
| İmalat karmaşıklığı | Özel imalat, sınırlı üretici sayısı |
| Onarım zorluğu | Kanal hasarında onarım zor |
| Conta değişimi | Kapak contaları büyük ve pahalı |
| Çoklu akışkan | İkiden fazla akışkan desteklenmez |

## Maliyet Analizi

### Yatırım Maliyeti

| Kapasite | Malzeme | Tahmini Maliyet (EUR) | Spesifik (EUR/kW) |
|----------|---------|----------------------|-------------------|
| 100 kW | SS316 | 8,000-15,000 | 80-150 |
| 500 kW | SS316 | 20,000-45,000 | 40-90 |
| 1,000 kW | SS316 | 35,000-80,000 | 35-80 |
| 5,000 kW | SS316 | 100,000-250,000 | 20-50 |
| 500 kW | Karbon çelik | 12,000-25,000 | 24-50 |
| 1,000 kW | Karbon çelik | 20,000-45,000 | 20-45 |

### Toplam Sahip Olma Maliyeti (TCO) Karşılaştırması

```
10 yıllık TCO karşılaştırması (1,000 kW, kirli servis):

Gövde-Boru (S&T):
  Yatırım: 30,000 EUR
  Yıllık bakım (sık temizlik): 8,000 EUR/yıl
  Enerji kaybı (kirlenme): 5,000 EUR/yıl
  10 yıl TCO: 30,000 + 10×(8,000+5,000) = 160,000 EUR

Spiral:
  Yatırım: 55,000 EUR
  Yıllık bakım (nadir temizlik): 1,500 EUR/yıl
  Enerji kaybı (düşük kirlenme): 1,000 EUR/yıl
  10 yıl TCO: 55,000 + 10×(1,500+1,000) = 80,000 EUR

Spiral avantajı: 80,000 EUR (%50 tasarruf)
Geri ödeme süresi: (55,000-30,000)/(8,000+5,000-1,500-1,000) = 2.4 yıl
```

## Exergy Analizi — Spiral Eşanjör

### Exergy Verimi Avantajları

```
Spiral eşanjör exergy avantajları:

1. Saf karşı akış (Tip I): F = 1.00 → minimum ΔT → minimum exergy yıkımı
2. Yüksek U değeri → küçük ΔT_lm → düşük exergy yıkımı
3. Düşük kirlenme → U zamanla düşmez → exergy verimi korunur

Exergy verimi:
  η_ex = (Ex_soğuk,çıkış - Ex_soğuk,giriş) / (Ex_sıcak,giriş - Ex_sıcak,çıkış)

Tipik exergy verimleri:
  Sıvı/sıvı (temiz): η_ex = 70-88%
  Sıvı/sıvı (kirli): η_ex = 65-85% (düşük kirlenme nedeniyle yüksek kalır)
  Çamur/sıvı: η_ex = 55-75%
  Yoğuşma (Tip II): η_ex = 50-70%

Karşılaştırma (aynı kirli servis):
  S&T (temiz): η_ex = 60-75%
  S&T (kirli, 6 ay sonra): η_ex = 40-55%
  Spiral (temiz): η_ex = 70-88%
  Spiral (6 ay sonra): η_ex = 65-82% (öz temizleme ile korunur)
```

### Exergy Yıkım Bileşenleri

```
Spiral eşanjör exergy yıkım analizi:

  Ex_yıkım = Ex_ΔT + Ex_ΔP

Sıcaklık farkından (dominant — %80-95):
  Ex_ΔT = T₀ × [m_c × cp_c × ln(T_c,out/T_c,in) + m_h × cp_h × ln(T_h,out/T_h,in)]

Basınç düşüşünden (%5-20):
  Ex_ΔP = m_c × ΔP_c / ρ_c + m_h × ΔP_h / ρ_h

Spiral eşanjörlerde basınç düşüşü:
  ΔP = f × (L_spiral / D_h) × ρ × v² / 2

  L_spiral : Spiral kanal uzunluğu (m) — genellikle 3-20 m
  D_h = 2 × kanal_genişliği (dikdörtgen kanal yaklaşımı)
```

## Ölçülmesi Gereken Parametreler

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Sıcak giriş/çıkış sıcaklığı | °C | Servise bağlı | PT100 veya termoeleman |
| Soğuk giriş/çıkış sıcaklığı | °C | Servise bağlı | PT100 veya termoeleman |
| Debi (her taraf) | m³/h veya kg/s | Servise bağlı | EM veya ultrasonik debimetre |
| Basınç düşüşü (her taraf) | kPa | 10-150 | Diferansiyel basınç sensörü |
| Akışkan yoğunluğu | kg/m³ | Akışkana bağlı | Laboratuvar veya proses verisi |
| Akışkan viskozitesi | cP veya Pa·s | Akışkana bağlı | Viskozimetre |

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Gövde-boru eşanjör: `heat_exchanger/equipment/shell_and_tube.md`
- Plakalı eşanjör: `heat_exchanger/equipment/plate.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Fabrika ısı entegrasyonu: `factory/heat_integration.md`
- Kağıt sanayi: `factory/sector_paper.md`

## Referanslar

- Alfa Laval (2023). *Spiral Heat Exchanger — Technical Reference Manual*.
- Minton, P.E. (1970). "Designing Spiral Plate Heat Exchangers," *Chemical Engineering*, 77(9), 103-112.
- Rajavel, R. & Saravanan, K. (2008). "Heat Transfer Studies on Spiral Plate Heat Exchanger," *Thermal Science*, 12(3), 85-90.
- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Hewitt, G.F., Shires, G.L., Bott, T.R. (1994). *Process Heat Transfer*, CRC Press.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*, Wiley.
- ASME Section VIII Division 1 — Boiler and Pressure Vessel Code.
- Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, McGraw-Hill.
