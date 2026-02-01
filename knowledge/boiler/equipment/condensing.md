---
title: "Yoğuşmalı Kazan — Condensing Boiler"
category: equipment
equipment_type: boiler
subtype: "Yoğuşmalı Kazan"
keywords: [yoğuşmalı kazan, condensing, verimlilik]
related_files: [boiler/benchmarks.md, boiler/formulas.md, boiler/equipment/fuels.md]
use_when: ["Yoğuşmalı kazan analizi yapılırken", "Yüksek verimli kazan seçimi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Yoğuşmalı Kazan — Condensing Boiler

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Yoğuşmalı (condensing) — baca gazındaki su buharının gizli ısısını (latent heat) geri kazanır
- Kapasite aralığı: 20 kW - 20 MW (konut tipi 20-150 kW, ticari/endüstriyel 150 kW - 20 MW)
- Yakıt: Doğalgaz (en yaygın), LPG, propan, hafif fuel oil (düşük kükürt)
- Enerji verimi: %95-99 (LHV bazlı), %86-90 (HHV bazlı)
- Ekserji verimi (exergy efficiency): %10-30 — düşük sıcaklıklı çıkış nedeniyle ekserji yıkımı yüksektir
- Dönüş suyu sıcaklığı: Etkin yoğuşma için <55°C olmalıdır (doğalgazda çiğ noktası ~57°C)
- Yaygın markalar: Viessmann, Buderus, Vaillant, Baxi, Wolf, De Dietrich, Bosch (Junkers)
- Uygulama: Kalorifer, yerden ısıtma, sıcak su hazırlama, düşük sıcaklıklı proses ısıtma
- Avantaj: Konvansiyonel kazanlara göre %10-15 daha düşük yakıt tüketimi, düşük NOₓ emisyonu

## Çalışma Prensibi

Yoğuşmalı kazanlar, baca gazı sıcaklığını su buharının çiğ noktasının (dew point) altına düşürerek baca gazındaki su buharının yoğuşmasını sağlar. Bu sayede:

1. **Duyulur ısı (sensible heat)**: Baca gazının soğumasıyla geri kazanılır (konvansiyonel kazanlarda da mevcut)
2. **Gizli ısı (latent heat)**: Su buharının yoğuşması sırasında açığa çıkan enerji — yoğuşmalı kazanların farkı budur

Doğalgaz yanma reaksiyonu:

```
CH₄ + 2O₂ → CO₂ + 2H₂O + ΔH

Burada:
  CH₄   : Metan (doğalgazın ana bileşeni, ~%95)
  H₂O   : Yanma ürünü su buharı — 1 m³ doğalgaz başına ~1.6 kg su buharı oluşur
  ΔH    : Yanma entalpisi
```

Her 1 m³ doğalgaz yanmasında yaklaşık 1.6 kg su buharı oluşur. Bu su buharının yoğuşma ısısı:

```
Q_latent = m_su × h_fg ≈ 1.6 × 2,443 ≈ 3,900 kJ/m³ doğalgaz

Burada:
  m_su   : Oluşan su buharı kütlesi (kg/m³ doğalgaz)
  h_fg   : Suyun buharlaşma entalpisi (kJ/kg, 25°C'de)
  Q_latent : Geri kazanılabilir gizli ısı (kJ/m³ doğalgaz)
```

Bu gizli ısı, doğalgazın LHV değerinin yaklaşık %10-11'ine karşılık gelir.

### Farklı Yakıtlar İçin Çiğ Noktası Tablosu

| Yakıt | Baca Gazı Çiğ Noktası (°C) | H₂O Oranı Baca Gazında (hacimsel %) | Gizli Isı / LHV (%) |
|-------|----------------------------|--------------------------------------|----------------------|
| Doğalgaz (CH₄) | ~57 | ~18 | ~11 |
| LPG (C₃H₈/C₄H₁₀) | ~52 | ~14 | ~9 |
| Hafif fuel oil (No. 2) | ~47 | ~11 | ~6 |
| Propan (C₃H₈) | ~53 | ~15 | ~9 |

Doğalgaz, yüksek H/C oranı sayesinde en çok su buharı üretir ve yoğuşmalı teknoloji için en uygun yakıttır.

## Enerji Dağılımı (Tipik — Doğalgaz Yakıtlı)

| Enerji Akışı | Konvansiyonel Kazan (%) | Yoğuşmalı Kazan (%) |
|---------------|-------------------------|----------------------|
| Faydalı ısı (suya aktarılan) | 85-90 | 95-99 (LHV bazlı) |
| Baca gazı duyulur ısı kaybı | 5-8 | 1-3 |
| Baca gazı gizli ısı kaybı | 8-11 | 1-4 (kısmen geri kazanılır) |
| Radyasyon ve konveksiyon kaybı | 1-2 | 0.5-1.5 |
| Toplam kayıp | 10-15 | 1-5 |

## LHV vs HHV Karşılaştırması

### Tanımlar

- **Alt ısıl değer (LHV — Lower Heating Value)**: Yanma ürünlerindeki suyun buhar fazında kaldığı varsayılır. Gizli ısı dahil değildir.
- **Üst ısıl değer (HHV — Higher Heating Value)**: Yanma ürünlerindeki suyun tamamen yoğuştığı varsayılır. Gizli ısı dahildir.

### Doğalgaz İçin Karşılaştırma

| Parametre | LHV Bazlı | HHV Bazlı | Birim |
|-----------|-----------|-----------|-------|
| Isıl değer | ~36,000 | ~40,000 | kJ/m³ |
| Isıl değer | ~50,000 | ~55,500 | kJ/kg |
| Fark (HHV - LHV) / LHV | — | ~%11 | — |
| Konvansiyonel kazan verimi | 88-92 | 80-83 | % |
| Yoğuşmalı kazan verimi | 95-109 | 86-98 | % |

### >%100 Verim Açıklaması

LHV bazında >%100 verim, fizik yasalarına aykırı değildir. LHV tanım gereği gizli ısıyı dışarıda bırakır. Yoğuşmalı kazan bu gizli ısıyı kısmen geri kazandığında, çıkış enerjisi LHV girdisini aşabilir:

```
η_LHV = Q_faydalı / (m_yakıt × LHV) × 100

Burada:
  Q_faydalı  : Suya aktarılan toplam ısı (kW veya kJ/s)
  m_yakıt    : Yakıt debisi (kg/s veya m³/s)
  LHV        : Alt ısıl değer (kJ/kg veya kJ/m³)
  η_LHV      : LHV bazlı verim (%)

Yoğuşma gerçekleştiğinde Q_faydalı, gizli ısıyı da içerir,
dolayısıyla η_LHV > 100% olabilir.
```

HHV bazında verim her zaman <%100 kalır, çünkü HHV tüm enerjiyi (gizli ısı dahil) zaten referans olarak içerir:

```
η_HHV = Q_faydalı / (m_yakıt × HHV) × 100

Burada:
  η_HHV her zaman < 100% (termodinamiğin ikinci yasasına uygundur)
  Tipik yoğuşmalı kazan: η_HHV ≈ %86-90
```

## Dönüş Suyu Sıcaklığı Etkisi

Dönüş suyu sıcaklığı, yoğuşma miktarını ve dolayısıyla verim kazanımını doğrudan belirler. Doğalgazda baca gazı çiğ noktası ~57°C olduğundan, dönüş suyu bu değerin altında olmalıdır.

| Dönüş Suyu Sıcaklığı | Yoğuşma Durumu | Verim Kazanımı (konvansiyonele göre) | Tipik Uygulama |
|-----------------------|----------------|---------------------------------------|----------------|
| <40°C | Maksimum yoğuşma | +%10-12 | Yerden ısıtma (30/35°C) |
| 40-50°C | İyi yoğuşma | +%6-10 | Düşük sıcaklık radyatör, fan-coil |
| 50-55°C | Kısmi yoğuşma | +%3-6 | Modernize radyatör sistemi |
| 55-60°C | Minimum yoğuşma | +%1-3 | Eski tip radyatör (geçiş bölgesi) |
| >60°C | Yoğuşma yok | ~%0 | Geleneksel yüksek sıcaklık sistemi |

Yerden ısıtma sistemleri (30/35°C dönüş) yoğuşmalı kazanlar için ideal uygulamadır. Yüksek sıcaklıklı radyatör sistemlerinde (70/80°C) yoğuşmalı kazan avantajı büyük ölçüde kaybolur.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Yakıt tüketimi | m³/h veya kg/h | Kapasiteye bağlı | Gaz sayacı veya debimetre |
| Gidiş suyu sıcaklığı | °C | 35-80 | Termometre / PT100 sensör |
| Dönüş suyu sıcaklığı | °C | 25-60 | Termometre / PT100 sensör |
| Su debisi | m³/h | Kapasiteye bağlı | Ultrasonik debimetre |
| Baca gazı sıcaklığı | °C | 40-80 | Baca gazı analizörü (Testo, Kane) |
| Baca gazı O₂ oranı | % | 3-6 | Baca gazı analizörü |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Baca gazı CO oranı | ppm | <50 | Baca gazı analizörü |
| Baca gazı CO₂ oranı | % | 8-11 | Baca gazı analizörü |
| Baca gazı NOₓ | ppm | <30 | Baca gazı analizörü |
| Kondensasyon debisi | L/h | Kapasiteye bağlı | Ölçüm kabı |
| Kondensat pH değeri | — | 3-5 | pH metre |
| Elektrik tüketimi (pompa, fan) | kW | 0.05-5 | Güç analizörü |
| Ortam sıcaklığı | °C | 5-35 | Termometre |

### Nameplate Bilgileri
- Marka ve model
- Nominal kapasite (kW)
- LHV bazlı verim (%)
- HHV bazlı verim (%)
- Maksimum çalışma basıncı (bar)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Yakıt | Doğalgaz | Türkiye'de en yaygın |
| LHV | 36,000 kJ/m³ | Türkiye şebeke gazı tipik |
| Gidiş suyu sıcaklığı | 50°C | Düşük sıcaklık sistemi varsayımı |
| Dönüş suyu sıcaklığı | 40°C | Yoğuşmanın gerçekleşeceği değer |
| Baca gazı sıcaklığı | 55°C | Yoğuşma bölgesinde |
| Baca gazı O₂ | %4.5 | İyi ayarlanmış brülör |
| Hava fazlası katsayısı (λ) | 1.25 | Yoğuşmalı kazan tipik |
| LHV bazlı verim | %98 | İyi çalışan yoğuşmalı kazan |
| HHV bazlı verim | %88 | Karşılık gelen HHV verimi |
| Ekserji verimi | %18 | Düşük sıcaklık çıkışı nedeniyle |
| Radyasyon kaybı | %1 | İyi izolasyonlu kazan |
| Çalışma saati | 3,000 saat/yıl | Isıtma sezonu (Türkiye, Marmara Bölgesi) |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |
| Kondensat pH | 4.0 | Doğalgaz yanma ürünü (karbonik asit) |

## Performans Tablosu

### Kapasite ve Verime Göre Tipik Değerler (Doğalgaz)

| Kapasite (kW) | LHV Verimi (%) | HHV Verimi (%) | Ekserji Verimi (%) | Tipik Uygulama | Yaklaşık Fiyat (EUR) |
|---------------|----------------|----------------|---------------------|----------------|----------------------|
| 20-35 | 97-99 | 87-89 | 12-18 | Konut — daire | 1,500-3,500 |
| 35-60 | 97-98 | 87-88 | 14-20 | Konut — villa, müstakil | 3,000-6,000 |
| 60-150 | 96-98 | 86-88 | 15-22 | Ticari — ofis, mağaza | 5,000-15,000 |
| 150-500 | 95-97 | 86-87 | 16-24 | Endüstriyel — küçük tesis | 12,000-40,000 |
| 500-2,000 | 94-97 | 85-87 | 18-26 | Endüstriyel — orta tesis | 35,000-120,000 |
| 2,000-20,000 | 93-96 | 84-86 | 20-30 | Büyük endüstriyel / bölgesel ısıtma | 100,000-500,000 |

### Ekserji Analizi — Neden Ekserji Verimi Düşük?

Yoğuşmalı kazanlar enerji verimliliği açısından mükemmel olmasına rağmen (%95-99 LHV), ekserji verimi oldukça düşüktür (%10-30). Bunun sebebi:

```
η_ex = Ex_çıkış / Ex_giriş × 100

Ex_giriş ≈ m_yakıt × ex_ch ≈ m_yakıt × φ × LHV   (yakıtın kimyasal ekserjisi)

Ex_çıkış = m_su × cp × [(T_gidiş - T_dönüş) - T₀ × ln(T_gidiş / T_dönüş)]

Burada:
  Ex_çıkış  : Sıcak suyun ekserji artışı (kW)
  Ex_giriş  : Yakıtın kimyasal ekserjisi (kW)
  m_su      : Su debisi (kg/s)
  cp        : Suyun özgül ısısı (~4.18 kJ/kg·K)
  T_gidiş   : Gidiş suyu sıcaklığı (K)
  T_dönüş   : Dönüş suyu sıcaklığı (K)
  T₀        : Referans çevre sıcaklığı (K)
  φ         : Yakıtın ekserji/enerji oranı (~1.04 doğalgaz için)
```

Temel sorun: Yakıtın kimyasal ekserjisi ~1,950°C alev sıcaklığına karşılık gelirken, çıkış suyunun sıcaklığı yalnızca 40-80°C'dir. Bu büyük sıcaklık farkı, Carnot faktörünü düşürür ve tersinmezliği (irreversibility) artırır.

## Korozyon Riskleri ve Malzeme Seçimi

### Kondensat Özellikleri

Yoğuşmalı kazanlarda oluşan kondensat asidiktir:

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| pH aralığı | 3.0-5.0 | CO₂ kaynaklı karbonik asit (H₂CO₃) |
| Tipik pH (doğalgaz) | 3.5-4.5 | Kükürt içermez, sadece karbonik asit |
| Tipik pH (fuel oil) | 2.5-3.5 | Sülfürik asit (H₂SO₄) ek katkısı |
| Kondensat debisi | ~0.14 L / kWh | Tam yoğuşma durumunda (doğalgaz) |
| Kondensat sıcaklığı | 40-55°C | Baca gazı çiğ noktasına yakın |

### Malzeme Gereksinimleri

| Bileşen | Uygun Malzeme | Uygun Olmayan Malzeme | Not |
|---------|---------------|------------------------|-----|
| Isı değiştirici | AISI 316L paslanmaz çelik, alüminyum-silisyum alaşımı | Karbon çelik, dökme demir | Asidik kondensata dayanım |
| Baca sistemi | PP (polipropilen), PVDF, paslanmaz çelik | Galvaniz çelik, tuğla | Islak çalışma koşullarına uygunluk |
| Kondensat borusu | PP, PVC, PVDF | Bakır, karbon çelik | Asit direnci |
| Kondensat drenajı | Nötralizasyon ünitesi ile kanalizasyona | Doğrudan deşarj (yerel mevzuata bağlı) | pH 3-5 asidik atıksu |

### Nötralizasyon

Kondensat, kanalizasyona deşarj edilmeden önce nötralize edilmelidir (pH > 6.5). Yaygın yöntemler:

- Kalsit (CaCO₃) granül nötralizasyon ünitesi — en yaygın, düşük maliyetli
- Otomatik dozajlı NaOH sistemi — büyük kapasiteler için
- Nötralizasyon gereksinimi yerel su/kanalizasyon yönetmeliğine göre değişir

## Dikkat Edilecekler

1. **Dönüş suyu sıcaklığı**: <55°C olmalıdır — aksi halde yoğuşma gerçekleşmez ve kazan konvansiyonel kazan gibi çalışır; yatırımın geri dönüşü sağlanamaz
2. **Baca sistemi**: Yoğuşmalı kazanlarda baca, ıslak çalışır (kondensat oluşur) — geleneksel tuğla veya galvaniz baca kullanılamaz; PP, PVDF veya paslanmaz çelik baca gereklidir
3. **Kondensat drenajı**: Asidik kondensat (pH 3-5) düzenli olarak drene edilmeli; nötralizasyon ünitesi zorunlu olabilir (yerel mevzuata bağlı)
4. **Hava/yakıt oranı ayarı**: Hava fazlası katsayısı (λ) düzenli kontrol edilmeli — fazla hava baca gazı sıcaklığını yükseltir ve yoğuşmayı azaltır; tipik λ: 1.15-1.30
5. **Düşük sıcaklık sistemi tasarımı**: Maksimum verim için yerden ısıtma (30/35°C) veya fan-coil (40/45°C) gibi düşük sıcaklık sistemleri tercih edilmeli
6. **Yakıt uygunluğu**: Yüksek kükürtlü yakıtlar (fuel oil No. 6, yüksek kükürtlü kömür) yoğuşmalı kazanlarda kullanılamaz — sülfürik asit korozyonu riski çok yüksektir
7. **Geri dönüş suyu kontrol vanası**: Karışık (mixing valve) veya üç yollu vana ile dönüş suyu sıcaklığı kontrol edilmeli — özellikle geçiş dönemlerinde ve kademeli yüklenmede önemlidir

## İlgili Dosyalar
- Kazan yakıt özellikleri: `equipment/boiler_fuels.md`
- Sıcak su kazanları: `equipment/boiler_hotwater.md`
- Ateş borulu buhar kazanları: `equipment/boiler_steam_firetube.md`
- Kazan ekserji hesaplamaları: `formulas/boiler_exergy.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Baca gazı ısı geri kazanımı: `solutions/boiler_flue_gas_recovery.md`
- Brülör ayarı ve hava/yakıt oranı: `solutions/boiler_combustion_optimization.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`

## Referanslar
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths. (Reprinted by Krieger, 1995.)
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
- ASME PTC 4 (2013). *Fired Steam Generators — Performance Test Codes*, ASME.
- EN 15502-1 (2021). *Gas-fired heating boilers — Part 1: General requirements and tests*, CEN.
- EN 677 (1998). *Gas-fired central heating boilers — Specific requirements for condensing boilers*, CEN.
- Viessmann Technical Guide (2024). *Condensing Technology — Design and Application Manual*.
- Buderus Handbook (2023). *Heating Technology — Condensing Boiler Systems*.
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 32: Boilers.
- Spirax Sarco (2023). *The Steam and Condensate Loop*, Technical Reference Guide.
- TS 7363 (Türk Standardı). *Merkezi ısıtma kazanları — Yoğuşmalı kazanlar — Deney ve hesaplama yöntemleri*.
