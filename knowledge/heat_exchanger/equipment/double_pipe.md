---
title: "Çift Borulu Eşanjörler (Double Pipe / Hairpin Heat Exchangers)"
category: equipment
equipment_type: heat_exchanger
subtype: "Çift Borulu"
keywords: [eşanjör, çift borulu, double pipe, hairpin, iç içe boru, kanatlı iç boru]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md, heat_exchanger/equipment/shell_and_tube.md]
use_when: ["Çift borulu eşanjör analizi yapılırken", "Küçük kapasiteli eşanjör seçimi gerektiğinde", "Yüksek basınç eşanjör gerektiğinde"]
priority: medium
last_updated: 2026-02-01
---
# Çift Borulu Eşanjörler — Double Pipe / Hairpin Heat Exchangers

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Çift borulu eşanjörler (double pipe heat exchangers), iç içe iki borudan oluşan en basit ısı eşanjörü yapısıdır. İç boru (inner tube) bir akışkanı taşırken, iç ve dış boru arasındaki halka şeklindeki boşluk (annulus) diğer akışkanı taşır. Saç tokası (hairpin) konfigürasyonunda, borular U-büküm ile geri döndürülerek kompakt bir yapı oluşturulur.

- Kapasite aralığı: 1 kW - 5 MW
- Basınç aralığı: Vakum - 500+ bar (en yüksek basınçlı eşanjör tipi)
- Sıcaklık aralığı: -200°C ile 600°C
- Tipik U değeri: 100-3,000 W/(m²·K) (akışkan kombinasyonuna bağlı)
- Akış düzeni: Saf karşı akış veya paralel akış (LMTD düzeltme faktörü F = 1.00)
- Tipik ömür: 15-25 yıl

## Yapı ve Çalışma Prensibi

### Temel Konfigürasyon

```
Basit çift borulu eşanjör:

  Dış boru (annulus): Akışkan B →→→→→→→→→→→→→→→→
  İç boru:           Akışkan A ←←←←←←←←←←←←←←←← (karşı akış)

  D_o : Dış boru iç çapı
  d_o : İç boru dış çapı
  d_i : İç boru iç çapı

Annulus hidrolik çapı:
  D_h = D_o - d_o   (ısı transfer için)
  D_h,sürtünme = D_o - d_o   (basınç düşüşü için)

  (Eşdeğer çap tanımlarına dikkat)
```

### Saç Tokası (Hairpin) Konfigürasyonu

```
Hairpin çift borulu eşanjör:

  ┌────────────────────────────┐
  │  İç boru → → → → → → → → U-büküm
  │  Annulus  ← ← ← ← ← ← ← │
  └────────────────────────────┘
    Giriş/Çıkış

  Tipik bacak uzunluğu: 3-6 m (taşıma ve montaj sınırı)
  Birden fazla hairpin seri veya paralel bağlanabilir
```

### Çoklu İç Borulu (Multi-Tube Hairpin)

Tek annulus içinde birden fazla iç boru kullanılarak ısı transfer alanı artırılır.

```
Multi-tube hairpin kesiti:

  ┌─────────────────┐
  │  ○  ○  ○  ○  ○  │  ← Dış boru (annulus)
  │  ○  ○  ○  ○  ○  │  ○ = İç borular
  │  ○  ○  ○  ○     │
  └─────────────────┘

Tipik iç boru sayısı: 2-19 (dış boru çapına bağlı)
Kapasite artışı: Tek borulunun 5-15 katı
```

## Ne Zaman Kullanılır?

### Tercih Edilen Durumlar

| Durum | Açıklama | Neden Çift Borulu? |
|-------|----------|---------------------|
| Küçük ısı yükü | Q < 500 kW | S&T aşırı boyut, PHE yeterli olmayabilir |
| Çok yüksek basınç | >100 bar (özellikle >200 bar) | Küçük çaplı boru yüksek basınca dayanır |
| Yüksek sıcaklık farkı | ΔT > 100°C | Termal genleşme toleransı (hairpin) |
| Saf karşı akış gereksinimi | F = 1.00 | Sıcaklık çaprazlaması mümkün |
| Düşük debi oranı | Bir akışkan çok düşük debili | İç boruda uygun hız sağlanır |
| Yüksek kirlenme | Kirli akışkanlar | İç boru kolayca çekilip temizlenebilir |
| Modüler genişleme | Kademeli kapasite artışı | Hairpin ekleme ile genişleme |
| Pilot tesis | Küçük ölçekli deneme | Basit, ucuz, çabuk temin |

### Tercih Edilmeyen Durumlar

| Durum | Açıklama | Alternatif |
|-------|----------|------------|
| Büyük ısı yükü | Q > 5 MW | S&T veya PHE |
| Büyük alan gereksinimi | >100 m² ısı transfer alanı | S&T |
| Küçük yaklaşma sıcaklığı | <3°C | PHE (daha yüksek U) |
| Kompakt alan kısıtı | Sınırlı yerleşim | PHE |
| Çok sayıda ünite | >20 hairpin seri | S&T tek ünite |

## Kanatlı İç Boru (Finned Inner Tube) Varyantları

### Boylamasına Kanatlı (Longitudinal Fins)

```
Boylamasına kanatlı iç boru kesiti:

      ╱╲
     ╱  ╲
  ──╱────╲──
  │   ○    │  ← İç boru
  ──╲────╱──
     ╲  ╱
      ╲╱

Kanat sayısı: 6-36 (tipik: 12-20)
Kanat yüksekliği: 6-25 mm
Kanat kalınlığı: 0.5-1.5 mm

Alan oranı: A_kanatlı / A_çıplak = 3-10×
U artışı: 2-5× (annulus tarafında düşük h varsa)
```

### Kanatlı Boru Performans Etkisi

| Durum | U_çıplak (W/(m²·K)) | U_kanatlı (W/(m²·K)) | İyileşme |
|-------|---------------------|----------------------|----------|
| Gaz/Sıvı | 30-80 | 80-250 | 2-4× |
| Viskoz sıvı/Su | 50-150 | 150-400 | 2-3× |
| Gaz/Gaz | 15-40 | 40-100 | 2-3× |
| Su/Su | 500-1,200 | 800-1,800 | 1.3-1.5× |

**Not:** Kanatlı boru, her iki tarafın ısı transfer direnci dengesiz olduğunda (bir taraf çok düşük h) en fazla fayda sağlar.

## Tasarım Hesaplamaları

### Isı Transfer

```
Toplam ısı geçiş katsayısı (iç boru dış alanına göre):

  1/(U_o × A_o) = 1/(h_i × A_i) + R_f,i/A_i + ln(d_o/d_i)/(2π×k_w×L) + R_f,o/A_o + 1/(h_o × A_o)

İç boru tarafı (türbülanslı akış):
  h_i = 0.023 × (k/d_i) × Re_i^0.8 × Pr_i^0.4

Annulus tarafı (türbülanslı akış):
  h_o = 0.023 × (k/D_h) × Re_o^0.8 × Pr_o^0.33 × (D_h/D_o)^0.14

Burada:
  D_h = D_o - d_o (annulus hidrolik çapı)
  Re_i = ρ × v_i × d_i / μ
  Re_o = ρ × v_o × D_h / μ

LMTD (karşı akış — düzeltme faktörü F = 1.00):
  ΔT₁ = T_h,in - T_c,out
  ΔT₂ = T_h,out - T_c,in
  LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)

Q = U_o × A_o × LMTD
```

### Basınç Düşüşü

```
İç boru basınç düşüşü:
  ΔP_iç = f × (L/d_i) × ρ × v²/2 + ρ × v² (giriş/çıkış kayıpları)
  + N_hairpin × ρ × v² × K_büküm (U-büküm kayıpları, K_büküm ≈ 1.5-2.0)

Annulus basınç düşüşü:
  ΔP_annulus = f × (L/D_h) × ρ × v²/2 + ρ × v²/2 (giriş/çıkış)

Tipik izin verilen ΔP:
  Sıvılar: 0.5-2.0 bar
  Gazlar: 0.05-0.20 bar
```

## Standart Boyutlar

### Tipik Boru Kombinasyonları

| İç Boru (NPS) | Dış Boru (NPS) | A (m²/m uzunluk) | Kapasite Aralığı |
|---------------|----------------|------------------|------------------|
| 3/4" (DN20) | 1-1/4" (DN32) | 0.060 | 1-50 kW |
| 1" (DN25) | 1-1/2" (DN40) | 0.080 | 5-100 kW |
| 1" (DN25) | 2" (DN50) | 0.080 | 5-150 kW |
| 1-1/2" (DN40) | 2-1/2" (DN65) | 0.120 | 10-300 kW |
| 2" (DN50) | 3" (DN80) | 0.159 | 20-500 kW |
| 3" (DN80) | 4" (DN100) | 0.219 | 50-1,000 kW |
| 4" (DN100) | 6" (DN150) | 0.273 | 100-2,000 kW |
| 6" (DN150) | 8" (DN200) | 0.406 | 200-5,000 kW |

### Malzeme Seçimi

| İç Boru | Dış Boru | Uygulama | Not |
|---------|----------|----------|-----|
| Karbon çelik | Karbon çelik | Genel endüstriyel | En ucuz |
| SS316 | Karbon çelik | Korozif iç akışkan | İç boru koruması |
| SS316 | SS316 | Çift taraf korozif | Kimya sanayi |
| Hastelloy | Karbon çelik | Agresif iç akışkan | Özel uygulama |
| Titanyum | Karbon çelik | Deniz suyu (iç) | Offshore |
| Bakır | Karbon çelik | Yüksek iletkenlik gerekli | Isı transferi öncelikli |

## Avantajlar ve Sınırlamalar

### Avantajlar

| Avantaj | Açıklama |
|---------|----------|
| Saf karşı akış | F = 1.00, en yüksek LMTD ve etkinlik |
| Yüksek basınç dayanımı | Küçük çaplı borular çok yüksek basınca dayanır (>500 bar) |
| Termal genleşme toleransı | Hairpin konfigürasyonunda doğal genleşme absorpsiyonu |
| Kolay bakım | İç boru çekilerek mekanik temizlik yapılabilir |
| Modüler genişleme | Hairpin ekleme/çıkarma ile kapasite ayarı |
| Basit imalat | Standart borulardan imal edilir — düşük maliyet, kısa teslim süresi |
| Küçük envanter | Düşük akışkan tutma hacmi |
| Esneklik | Farklı malzeme kombinasyonları kolay |

### Sınırlamalar

| Sınırlama | Açıklama |
|-----------|----------|
| Düşük alan yoğunluğu | m²/m³ oranı düşük, büyük yerleşim alanı |
| Sınırlı kapasite | Büyük ısı yükleri için çok sayıda ünite gerekir |
| Çok sayıda bağlantı | Her hairpin'de flanş bağlantıları — sızıntı riski |
| Annulus temizliği | Annulus tarafının temizliği zor |
| Düşük U (kanatsız) | Annulus tarafı h düşük olabilir |

## Exergy Analizi — Çift Borulu Eşanjör

### Exergy Verimi Avantajı

```
Çift borulu eşanjör exergy avantajı:

  Saf karşı akış (F = 1.00) → minimum exergy yıkımı

  Karşılaştırma (aynı Q, aynı akışkanlar):
    Çift borulu (F=1.00): η_ex = 70-85%
    S&T 1-2 (F=0.85):    η_ex = 55-75%
    S&T 1-4 (F=0.80):    η_ex = 50-70%

Exergy yıkım hesabı:
  Ex_yıkım = T₀ × [m_c × cp_c × ln(T_c,out/T_c,in) + m_h × cp_h × ln(T_h,out/T_h,in)]

Saf karşı akışta, daha düşük LMTD ile aynı Q transfer edilebilir:
  Q = U × A × LMTD_karşıakış × 1.00   (çift borulu)
  Q = U × A × LMTD_karşıakış × F       (S&T, F < 1.00)

  Aynı A için: LMTD_çiftborulu < LMTD_S&T
  → Daha küçük sıcaklık farkı = daha düşük exergy yıkımı
```

### Exergy Optimizasyonu

| Parametre | Optimizasyon | Exergy Etkisi |
|-----------|-------------|---------------|
| Akış hızı dengesi | Her iki tarafta benzer Re sağla | ΔP exergysi minimize |
| Kanat kullanımı | Düşük h tarafına kanat ekle | ΔT exergysi minimize |
| Boru uzunluğu | Optimal L/D oranı | ΔT ve ΔP dengesi |
| Malzeme iletkenliği | Yüksek k malzeme | Duvar direnci azaltma |
| Temizlik | Düzenli iç boru temizliği | Kirlenme exergysi azaltma |

### Sayısal Örnek

```
Örnek: Yağ soğutma hairpin eşanjörü
  Sıcak taraf (yağ): 120°C giriş, 80°C çıkış, 2.0 kg/s, cp = 2.1 kJ/(kg·K)
  Soğuk taraf (su): 20°C giriş, 50°C çıkış, 2.8 kg/s, cp = 4.18 kJ/(kg·K)
  T₀ = 25°C = 298.15 K

  Q = 2.0 × 2.1 × (120-80) = 168 kW

  LMTD = [(120-50) - (80-20)] / ln[(120-50)/(80-20)]
       = [70 - 60] / ln(70/60) = 10 / 0.1542 = 64.85°C

  Exergy yıkımı:
    S_üretilen = 2.0 × 2.1 × ln(353.15/393.15) + 2.8 × 4.18 × ln(323.15/293.15)
               = 4.2 × (-0.1073) + 11.704 × (0.0975)
               = -0.4507 + 1.1412 = 0.6905 kW/K

    Ex_yıkım = 298.15 × 0.6905 = 205.9 kW... [hesap kontrolü gerekli]

  Not: Gerçek hesap için akışkan özelliklerinin sıcaklık ortalamasında alınması gerekir.
```

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Gövde-boru eşanjör: `heat_exchanger/equipment/shell_and_tube.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Fabrika ısı entegrasyonu: `factory/heat_integration.md`

## Referanslar

- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Serth, R.W. & Lestina, T.G. (2014). *Process Heat Transfer: Principles, Applications and Rules of Thumb*, 2nd Edition, Academic Press.
- Brown Fintube (2019). *Hairpin Heat Exchangers — Technical Manual*.
- Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, McGraw-Hill.
- Hewitt, G.F., Shires, G.L., Bott, T.R. (1994). *Process Heat Transfer*, CRC Press.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- ASME B31.3 — Process Piping Code.
- ASME Section VIII Division 1 — Boiler and Pressure Vessel Code.
