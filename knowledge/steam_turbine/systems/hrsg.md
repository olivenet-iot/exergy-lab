---
title: "HRSG (Atık Isı Buhar Jeneratörü) — Heat Recovery Steam Generator"
category: systems
equipment_type: steam_turbine
subtype: "HRSG"
keywords: [HRSG, atık ısı, buhar jeneratörü, heat recovery, pinch point, approach temperature, duct firing, kombine çevrim, CCGT, exergy, tek basınçlı, çift basınçlı, üçlü basınçlı, baca gazı, stack temperature]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/systems/gas_turbine_chp.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/systems/trigeneration.md, factory/cogeneration.md, boiler/equipment/waste_heat.md, factory/waste_heat_recovery.md, factory/pinch_analysis.md]
use_when: ["HRSG exergy analizi yapılırken", "Pinch point ve approach temperature değerlendirilirken", "HRSG basınç seviyesi seçimi yapılırken", "Duct firing etkisi analiz edilirken", "Kombine çevrim alt çevrimi optimize edilirken"]
priority: medium
last_updated: 2026-02-02
---
# HRSG (Atık Isı Buhar Jeneratörü) — Heat Recovery Steam Generator

> Son güncelleme: 2026-02-02

## Genel Bakış

HRSG (Heat Recovery Steam Generator — Atık Isı Buhar Jeneratörü), gaz türbini egzoz gazındaki termal enerjiyi geri kazanarak buhar üreten bir ısı değiştirici sistemidir. Kombine çevrim (combined cycle — CCGT) ve kojenerasyon (CHP) tesislerinin kritik bir bileşeni olan HRSG, gaz türbini ile buhar türbini arasındaki köprü görevi görür.

Bu dosya, HRSG'yi **buhar türbini perspektifinden** ele alır: buhar türbinine beslenen buharın kalitesi, basıncı ve debisi doğrudan HRSG tasarımına bağlıdır. HRSG iç yapısı ve kazan perspektifinden detaylı bilgi için `boiler/equipment/waste_heat.md` dosyasına bakınız.

**Temel Prensip:** HRSG'de yanma gerçekleşmez (ek yakmalı tipler hariç). Isı transferi tamamen konveksiyon ağırlıklıdır. Bu nedenle HRSG'nin exergy yıkımı, ateşli kazanlara kıyasla daha düşüktür -- yanma tersinmezliği gaz türbininde zaten gerçekleşmiştir.

> **Exergy Perspektifi:** Gaz türbini egzozu 450-600°C sıcaklıkta olup yüksek exergy içerir. HRSG'nin görevi bu exergyyi minimum kayıpla buhara aktarmaktır. Sıcaklık farkı (pinch point) ne kadar küçükse exergy yıkımı o kadar azdır, ancak ısı transfer yüzeyi ve maliyet artar.

## 1. HRSG Tipleri (HRSG Types)

### 1.1 Tek Basınçlı HRSG (Single Pressure)

Tek basınçlı HRSG, en basit konfigürasyondur. Tek bir buharlaştırıcı devresinde tek basınç seviyesinde buhar üretir.

```
Akış şeması (Tek Basınçlı):
Egzoz Gazı (450-600°C) → [Kızdırıcı] → [Buharlaştırıcı] → [Ekonomizer] → Baca (150-200°C)
                           Buhar çıkış     Buhar/Su          Su giriş
                           (HP kızdırılmış)
```

- Basit tasarım, düşük yatırım maliyeti
- Baca gazı sıcaklığı nispeten yüksek kalır (150-200°C)
- Egzoz gazı enerjisinin %60-75'i geri kazanılır
- Küçük ve orta ölçekli CHP tesislerinde tercih edilir (<25 MW_e)

### 1.2 Çift Basınçlı HRSG (Dual Pressure)

Çift basınçlı HRSG, yüksek basınç (HP) ve alçak basınç (LP) olmak üzere iki buharlaştırıcı devresi içerir.

```
Akış şeması (Çift Basınçlı):
Egzoz Gazı → [HP Kızdırıcı] → [HP Buharlaştırıcı] → [LP Buharlaştırıcı] → [HP Ekonomizer] → [LP Ekonomizer] → Baca (120-160°C)
                   ↓                   ↓                      ↓
             HP Kızdırılmış      HP Doymuş Buhar        LP Buhar
                Buhar                                    (→ LP türbine
              (→ HP türbine)                              veya prosese)
```

- HP buhar: buhar türbininin HP bölümüne beslenir
- LP buhar: LP türbine veya doğrudan prosese verilebilir
- Baca gazı sıcaklığı düşer, ısı geri kazanımı artar
- Tek basınca göre %8-12 daha fazla buhar türbini gücü

### 1.3 Üçlü Basınçlı HRSG (Triple Pressure with Reheat)

Üçlü basınçlı HRSG, HP + IP (intermediate pressure — ara basınç) + LP buhar üretir ve genellikle ara kızdırma (reheat) dahildir.

```
Akış şeması (Üçlü Basınçlı + Reheat):
Egzoz Gazı → [HP SH] → [RH] → [HP Evap] → [IP SH] → [IP Evap] → [LP SH] → [LP Evap] → [HP Eco] → [LP Eco] → Baca (80-120°C)
                ↓         ↓         ↓           ↓          ↓          ↓          ↓
           HP Buhar   Reheat    HP Drum     IP Buhar   IP Drum    LP Buhar   LP Drum
           (→ HP ST)  (→ IP ST)             (→ IP ST)             (→ LP ST)

SH = Kızdırıcı (Superheater)
RH = Ara Kızdırıcı (Reheater)
Evap = Buharlaştırıcı (Evaporator)
Eco = Ekonomizer
```

- Baca gazı sıcaklığı minimuma iner (80-120°C)
- Egzoz gazı exergisinin %80-90'ı geri kazanılır
- Büyük CCGT santralleri (>100 MW_e, F/H/J sınıfı gaz türbinleri)
- En yüksek yatırım maliyeti, en karmaşık kontrol

### 1.4 HRSG Tip Karşılaştırma Tablosu

| Parametre | Tek Basınçlı | Çift Basınçlı | Üçlü Basınçlı + RH |
|-----------|-------------|---------------|---------------------|
| HP buhar basıncı [bar] | 30-60 | 60-100 | 100-170 |
| HP buhar sıcaklığı [°C] | 400-480 | 480-540 | 540-600 |
| IP buhar basıncı [bar] | -- | -- | 20-40 |
| LP buhar basıncı [bar] | -- | 3-8 | 3-8 |
| Baca gazı sıcaklığı [°C] | 150-200 | 120-160 | 80-120 |
| Isı geri kazanım oranı [%] | 60-75 | 75-85 | 85-93 |
| Exergy verimi (HRSG) [%] | 55-65 | 65-78 | 78-88 |
| CC net verim katkısı [%puan] | Referans | +3-5 | +5-7 |
| Yatırım maliyeti [EUR/kW] | 150-250 | 250-400 | 400-600 |
| Karmaşıklık | Basit | Orta | Yüksek |
| Başlangıç süresi [dk] | 30-60 | 45-90 | 60-120 |
| Tipik GT boyutu [MW_e] | <25 | 25-100 | >100 |

## 2. Pinch ve Approach Analizi (Pinch and Approach Analysis)

### 2.1 Temel Kavramlar

**Pinch point (sıkışma noktası):** Egzoz gazı ile buharlaştırıcı (evaporator) içindeki su/buhar karışımı arasındaki minimum sıcaklık farkıdır. Bu nokta, buharlaştırıcının giriş tarafında (gaz açısından) oluşur ve HRSG tasarımının en kritik kısıtıdır.

**Approach temperature (yaklaşma sıcaklığı):** Ekonomizer çıkışındaki su sıcaklığı ile buharlaştırıcıdaki doyma sıcaklığı arasındaki farktır. Steaming (istenmeyen buharlaşma) riskini önlemek için minimum bir değerde tutulmalıdır.

**Stack temperature (baca gazı sıcaklığı):** HRSG'den çıkan egzoz gazının sıcaklığıdır. Asit çiğ noktası (acid dew point) üzerinde tutulmalıdır.

```
Tipik değerler:
- Pinch point: 8-15°C (tasarım), 15-25°C (kısmi yükte artabilir)
- Approach temperature: 5-10°C (tasarım)
- Stack temperature: >80°C (doğalgaz), >130°C (kükürtlü yakıt)
- Asit çiğ noktası: 60-70°C (doğalgaz), 120-150°C (kükürtlü yakıt)
```

### 2.2 T-Q Diyagramı (Temperature-Heat Duty Diagram)

Aşağıdaki ASCII diyagram, tek basınçlı bir HRSG'deki sıcaklık-ısı yükü ilişkisini gösterir:

```
Sıcaklık [°C]
    ^
600 |  *
    |   *  Egzoz gazı soğuma eğrisi
550 |    *
    |     *
500 |      *
    |       *
450 |        *. . . . . . . . . . . . .
    |         *                         .
400 |          *                        .
    |           *                       .
350 |            *                      .
    |    pinch →  *----+                .
300 |    (ΔT_pp)  .    |                .
    |             .    |  Buharlaştırma  .
250 | T_sat ------+----+----------------+  ← Doyma sıcaklığı
    |        approach  |                |
    |        (ΔT_app)  |                |
200 |    ----+         |                |
    |   /              |                |
150 | /  Su ısınma     |                |
    |/   (ekonomizer)  |                |
100 +------------------------------------------→ Isı yükü Q [kW]
    0                                   Q_toplam

    ΔT_pp  = Pinch point = Egzoz gazı sıcaklığı (buharlaştırıcı giriş)
             - Doyma sıcaklığı
    ΔT_app = Approach = Doyma sıcaklığı
             - Ekonomizer çıkış su sıcaklığı
```

> **Kritik:** Pinch point küçüldükçe buhar üretimi artar ancak gerekli ısı transfer yüzeyi katlanarak büyür. Optimum pinch point, ekonomik analizle belirlenir (tipik: 8-15°C).

### 2.3 Pinch Point Etkisi

| Pinch Point [°C] | Buhar Üretimi [% değişim] | Isı Transfer Yüzeyi [% değişim] | Baca T [°C] (yaklaşık) |
|-------------------|---------------------------|----------------------------------|------------------------|
| 25 | Referans | Referans | 190 |
| 20 | +5 | +15 | 180 |
| 15 | +10 | +35 | 170 |
| 10 | +15 | +70 | 155 |
| 8 | +18 | +100 | 148 |
| 5 | +22 | +180 | 140 |

### 2.4 Baca Gazı Sıcaklığı Optimizasyonu

```
Baca gazı sıcaklığını belirleyen faktörler:
1. Pinch point: Düşük pinch → düşük baca T → yüksek geri kazanım
2. Approach temperature: Düşük approach → daha fazla ısı alımı
3. Basınç seviye sayısı: Çoklu basınç → düşük baca T
4. Feedwater sıcaklığı: Düşük feedwater T → düşük baca T
5. Asit çiğ noktası kısıtı: Baca T > çiğ noktası olmalı

Baca gazı ısı kaybı hesabı:
Q̇_baca = ṁ_gaz × c_p,gaz × (T_baca - T_referans)
Ex_baca = ṁ_gaz × c_p,gaz × [(T_baca - T₀) - T₀ × ln(T_baca/T₀)]

Burada:
- T₀ = çevre sıcaklığı [K] (tipik 288-298 K)
- T_baca = baca gazı sıcaklığı [K]
- c_p,gaz ≈ 1.05-1.10 kJ/(kg·K)
```

## 3. Duct Firing — Ek Yakma (Supplementary Firing)

### 3.1 Tanım ve Uygulama

Duct firing (kanal içi ek yakma), HRSG girişine yerleştirilen yakıcılar ile egzoz gazı sıcaklığının artırılmasıdır. Gaz türbini egzozunda %15-17 oranında oksijen bulunduğundan ek yanma için harici hava gerekmez.

```
Ek yakma şeması:
Gaz Türbini Egzozu (500-600°C, %15-17 O₂)
        ↓
   [Duct Burner] ← Yakıt (doğalgaz)
        ↓
  Sıcak Gaz (650-1,000°C)
        ↓
     [HRSG]
        ↓
   Baca Gazı (100-180°C)
```

### 3.2 Ek Yakma Etkileri

| Parametre | Ek Yakmasız | Düşük Ek Yakma | Orta Ek Yakma | Yüksek Ek Yakma |
|-----------|-------------|-----------------|---------------|-----------------|
| HRSG giriş T [°C] | 500-600 | 650-700 | 700-800 | 800-1,000 |
| Ek yakıt oranı [% GT yakıtı] | 0 | 10-20 | 20-40 | 40-60 |
| Buhar üretim artışı [%] | Referans | +20-35 | +35-60 | +60-100 |
| HRSG enerji verimi [%] | 80-90 | 82-90 | 83-90 | 83-90 |
| HRSG exergy verimi [%] | 65-80 | 55-70 | 48-62 | 42-55 |
| Marjinal exergy verimi [%] | -- | 40-50 | 35-45 | 30-40 |

### 3.3 Ek Yakmanın Exergy Etkisi

```
Ek yakma NEDEN exergy verimini düşürür?

Ek yakma = Yakıt → Yanma → Sıcak gaz (tersinmezlik!)
Bu, ateşli kazanla benzer bir termodinamik süreçtir.

Yanma tersinmezliği:
- Yakıt kimyasal exergisi yüksektir (doğalgaz φ ≈ 1.04)
- Yanma sonucu oluşan sıcak gaz exergisi düşüktür
- Exergy yıkımı: yakıt exergisinin %25-35'i
- Marjinal exergy verimi: %35-50 (GT çıkışı exergy verimi %50-60 iken)

Sonuç:
- Ek yakma → toplam enerji verimi ARTAR (Q_buhar artar)
- Ek yakma → toplam exergy verimi AZALIR (yanma tersinmezliği)
- Her ek yakma birimi, ortalamadan düşük marjinal verimle çalışır
```

> **Karar kuralı:** Ek yakma yalnızca şu durumlarda haklıdır: (1) proses buhar talebi GT egzozundan karşılanamıyorsa, (2) mevsimsel pik dönemlerinde kısa süreli kullanım gerekiyorsa, (3) ekonomik analiz exergy kaybını tolere ediyorsa. Sürekli yüksek ek yakma yerine daha büyük GT veya ek GT değerlendirilmelidir.

### 3.4 Ekonomik Değerlendirme

```
Ek yakma yatırım ve işletme maliyetleri:

Yatırım maliyeti (duct burner):
- Kapasite: 10-100 MW_termal
- Maliyet: 20-50 EUR/kW_termal (HRSG'nin %5-10'u)
- Montaj ve kontrol: +%20-30

İşletme maliyeti (marjinal):
- Yakıt: doğalgaz fiyatına doğrudan bağlı
- Marjinal buhar maliyeti: Ateşli kazana yakın (exergy açısından)
- Bakım: Düşük ek maliyet

Ekonomik karar kriteri:
- Ek yakma marjinal maliyeti < alternatif buhar kaynağı maliyeti ise uygulanır
- Ek yakma > yılda 4,000 saat kullanılacaksa, daha büyük GT düşünülmeli
- Peak shaving için ek yakma ekonomik olabilir
```

## 4. Exergy Analizi (Exergy Analysis of HRSG)

### 4.1 HRSG Exergy Yıkım Kaynakları

HRSG'deki exergy yıkımı üç ana kaynaktan oluşur:

```
HRSG Exergy Yıkım Kaynakları:

1. Isı transferi sıcaklık farkı (ΔT): %70-85
   - Egzoz gazı ile su/buhar arasındaki sonlu ΔT
   - En büyük kaynak: buharlaştırıcı bölgesi (sabit T_sat vs düşen T_gaz)
   - Azaltma: Çoklu basınç seviyesi, düşük pinch point

2. Basınç düşüşleri (Pressure drops): %10-20
   - Gaz tarafı basınç düşüşü: 20-40 mbar (GT back-pressure etkisi!)
   - Su/buhar tarafı basınç düşüşü: 2-8 bar
   - GT back-pressure etkisi: Her 10 mbar → %0.3-0.5 GT güç kaybı

3. Karışım ve diğer kayıplar: %5-10
   - Attemperasyon (desuperheating) suyu karışımı
   - Blowdown kayıpları
   - Isı yalıtım kayıpları
   - Bypass ve sızıntılar
```

### 4.2 HRSG Exergy Verimi Formülü

```
HRSG Exergy Verimi:

η_ex,HRSG = Ėx_buhar,çıkış / Ėx_gaz,giriş

Burada:
Ėx_gaz,giriş = ṁ_gaz × [(h_gaz,giriş - h₀) - T₀ × (s_gaz,giriş - s₀)]

Ėx_buhar,çıkış = Σ ṁ_buhar,i × [(h_buhar,i - h_fw,i) - T₀ × (s_buhar,i - s_fw,i)]
                  (tüm basınç seviyeleri için toplam)

Basitleştirilmiş form (ideal gaz varsayımı, gaz tarafı):
Ėx_gaz = ṁ_gaz × c_p × [(T_giriş - T₀) - T₀ × ln(T_giriş/T₀)]

HRSG Exergy Yıkımı:
Ėx_yıkım = Ėx_gaz,giriş - Ėx_buhar,çıkış - Ėx_baca

Exergy yıkım oranı:
y_D,HRSG = Ėx_yıkım / Ėx_yakıt,toplam
(Toplam kombine çevrim yakıt exergisine göre: tipik %4-10)
```

### 4.3 Hesap Örneği (Worked Example)

```
Örnek: Tek basınçlı HRSG exergy analizi

Veriler:
- Egzoz gazı debisi: ṁ_gaz = 200 kg/s
- Egzoz giriş sıcaklığı: T_gaz,giriş = 550°C = 823 K
- Baca gazı sıcaklığı: T_baca = 170°C = 443 K
- c_p,gaz = 1.08 kJ/(kg·K) (ortalama)
- Buhar çıkış: 45 bar, 450°C (h = 3,334 kJ/kg, s = 6.98 kJ/(kg·K))
- Feedwater giriş: 45 bar, 105°C (h = 447 kJ/kg, s = 1.37 kJ/(kg·K))
- Buhar debisi: ṁ_buhar = 28 kg/s
- T₀ = 25°C = 298 K, P₀ = 1.013 bar

Adım 1: Gaz tarafı exergy girişi
Ėx_gaz,giriş = 200 × 1.08 × [(823 - 298) - 298 × ln(823/298)]
             = 216 × [525 - 298 × 1.016]
             = 216 × [525 - 302.8]
             = 216 × 222.2
             = 47,995 kW ≈ 48.0 MW

Adım 2: Baca gazı exergy kaybı
Ėx_baca = 200 × 1.08 × [(443 - 298) - 298 × ln(443/298)]
        = 216 × [145 - 298 × 0.397]
        = 216 × [145 - 118.3]
        = 216 × 26.7
        = 5,767 kW ≈ 5.8 MW

Adım 3: Buhar tarafı exergy çıkışı
Ėx_buhar = 28 × [(3,334 - 447) - 298 × (6.98 - 1.37)]
         = 28 × [2,887 - 298 × 5.61]
         = 28 × [2,887 - 1,671.8]
         = 28 × 1,215.2
         = 34,026 kW ≈ 34.0 MW

Adım 4: Exergy yıkımı
Ėx_yıkım = 48.0 - 34.0 - 5.8 = 8.2 MW

Adım 5: HRSG exergy verimi
η_ex,HRSG = 34.0 / 48.0 = %70.8

Adım 6: Exergy dağılımı
- Buhara aktarılan: %70.8 (faydalı çıktı)
- Baca gazı kaybı:  %12.1 (geri kazanılabilir potansiyel)
- HRSG iç yıkım:    %17.1 (ΔT + basınç düşüşü + diğer)
```

### 4.4 Tek vs Çift vs Üçlü Basınç Exergy Karşılaştırması

```
Aynı gaz türbini egzozu için karşılaştırma:
(GT egzoz: 200 kg/s, 550°C, Ėx_gaz = 48 MW)

                    Tek Basınç    Çift Basınç    Üçlü Basınç+RH
                    ----------    -----------    ----------------
Buhar exergisi:     34.0 MW       37.5 MW        40.5 MW
Baca exergisi:       5.8 MW        3.6 MW         1.9 MW
Exergy yıkımı:      8.2 MW        6.9 MW         5.6 MW
η_ex,HRSG:          %70.8         %78.1          %84.4
ST elektrik (net):  11.5 MW       13.8 MW        15.6 MW
CC net verim:       %52.5         %55.1          %57.3

Neden çoklu basınç daha verimli?
1. Daha düşük ortalama ΔT → düşük exergy yıkımı
2. Daha düşük baca T → düşük exergy kaybı
3. Buhar eğrileri gaz soğuma eğrisine daha iyi uyum sağlar
4. Her basınç seviyesi, farklı sıcaklık aralığında optimum çalışır
```

## 5. Tasarım Parametreleri (Design Parameters)

### 5.1 Anahtar Tasarım Parametreleri Tablosu

| Parametre | Tipik Aralık | Birim | Etki |
|-----------|-------------|-------|------|
| Egzoz gazı debisi | 50-700 | kg/s | HRSG boyutu ve buhar kapasitesi |
| Egzoz giriş sıcaklığı | 450-650 | °C | Buhar basıncı ve sıcaklığı üst sınırı |
| HP buhar basıncı | 30-170 | bar | Buhar türbini verimi |
| HP buhar sıcaklığı | 400-600 | °C | Exergy içeriği, malzeme seçimi |
| Pinch point | 8-25 | °C | Buhar üretimi, yüzey alanı |
| Approach temperature | 5-15 | °C | Steaming riski, ekonomizer boyutu |
| Gaz tarafı basınç düşüşü | 20-40 | mbar | GT back-pressure kaybı |
| Baca gazı sıcaklığı | 80-200 | °C | Isı geri kazanım oranı |
| HRSG enerji verimi | 75-93 | % | Toplam ısı geri kazanımı |
| HRSG exergy verimi | 55-88 | % | Termodinamik kalite |

### 5.2 Gaz Türbini Sınıfına Göre HRSG Eşleştirme

| GT Sınıfı | Egzoz T [°C] | Egzoz Debisi [kg/s] | Önerilen HRSG | HP Basınç [bar] |
|-----------|-------------|---------------------|---------------|-----------------|
| Aero-derivatif (25 MW) | 450-500 | 70-90 | Tek/Çift basınç | 30-60 |
| E sınıfı (50-80 MW) | 530-560 | 150-200 | Çift basınç | 60-90 |
| F sınıfı (150-250 MW) | 580-620 | 400-500 | Üçlü basınç + RH | 100-140 |
| H sınıfı (300-400 MW) | 600-640 | 550-700 | Üçlü basınç + RH | 130-170 |
| J sınıfı (350-500 MW) | 620-660 | 600-750 | Üçlü basınç + RH | 140-170 |

## 6. Operasyonel Dikkat Noktaları (Operational Considerations)

### 6.1 Devreye Alma ve Yük Değişimleri

```
HRSG başlangıç tipleri:

Soğuk başlangıç (cold start): >48 saat durma sonrası
- Süre: 3-6 saat (üçlü basınç)
- HP drum sıcaklık artış hızı: <3°C/dakika
- Termal gerilme yönetimi kritik
- Bypass damper açık başlanır, kademeli yükleme

Ilık başlangıç (warm start): 8-48 saat durma sonrası
- Süre: 1.5-3 saat
- HP drum sıcaklık artış hızı: <5°C/dakika
- Kısmen basınçlı drumlar avantaj sağlar

Sıcak başlangıç (hot start): <8 saat durma sonrası
- Süre: 0.5-1.5 saat
- HP drum hala basınç altında
- Hızlı GT yükleme → hızlı HRSG tepki

Termal döngü etkisi:
- Her soğuk başlangıç: HRSG ömründen ~%0.01-0.05 tüketim
- Günlük başlangıç/durdurma: yıllık 300-365 döngü → bakım maliyeti artar
- Cycling duty HRSG tasarımı: kalınlaştırılmış drum, esnek bağlantılar
```

### 6.2 Korozyon ve Çiğ Noktası (Corrosion and Dew Point)

```
Asit çiğ noktası korozyonu:

Doğalgaz yakıtlı GT:
- SO₂ oluşumu minimal → çiğ noktası düşük (~60-70°C)
- Baca gazı sıcaklığı 80°C'ye kadar düşürülebilir
- Düşük korozyon riski

Kükürtlü yakıt (fuel oil, biogaz):
- SO₃ oluşumu → H₂SO₄ yoğuşması (acid dew point: 120-150°C)
- Baca gazı sıcaklığı > çiğ noktası + 15-20°C tutulmalı
- Korozyon dirençli malzeme (Corten çeliği, enamel kaplama)
- Ekonomizer bypass/recirculation gerekebilir

Soğuk uç korozyonu önleme:
1. Baca gazı sıcaklığını izleme (sürekli ölçüm)
2. Ekonomizer bypass damper kontrolü
3. LP ekonomizer recirculation sistemi
4. Feedwater sıcaklığı kontrolü (>60°C)
```

### 6.3 Termal Döngü ve Ömür Yönetimi

```
HRSG ömrünü etkileyen faktörler:
- Başlangıç/durdurma sayısı (cycling)
- Sıcaklık artış/düşüş hızları
- Basınç dalgalanmaları
- Korozyon ve erozyon
- Su kimyası kalitesi

Önleyici tedbirler:
1. Drum sıcaklık değişim hızı limitleri (EN 12952)
2. Başlangıç prosedürlerine uyum
3. Azot konservasyon (uzun duruşlarda)
4. Condensate pot drenajları (termal şok önleme)
5. Attemperasyon sistemi kalibrasyonu
```

## 7. Boiler Knowledge Base Referansı

HRSG, boiler knowledge base'inde `boiler/equipment/waste_heat.md` altında detaylı olarak ele alınmaktadır. Bu dosyadaki (buhar türbini perspektifi) ve kazan perspektifindeki bilgiler birbirini tamamlar:

| Konu | Bu dosya (steam_turbine/systems/hrsg.md) | boiler/equipment/waste_heat.md |
|------|------------------------------------------|-------------------------------|
| Odak | Buhar türbini besleme kalitesi, CC verimi | HRSG iç yapı, ısı transferi |
| Basınç seviyeleri | Türbin eşleştirme, ST verim etkisi | Drum tasarımı, sirkülasyon |
| Pinch analizi | Buhar üretimi ve CC etkisi | Isı yüzeyi tasarımı |
| Exergy | Sistem seviyesi exergy dağılımı | Bileşen seviyesi exergy |
| Ek yakma | Exergy etkisi, karar kriteri | Yakıcı tasarımı, kontrol |
| Korozyon | Baca T kısıtı, sistem etkisi | Malzeme seçimi, kaplama |

> **Çapraz referans:** Fabrika seviyesi atık ısı geri kazanım stratejileri için `factory/waste_heat_recovery.md`, pinch analizi metodolojisi için `factory/pinch_analysis.md` dosyalarına bakınız.

## İlgili Dosyalar

- [Formüller](../formulas.md) -- Buhar türbini exergy hesaplama formülleri
- [Benchmarklar](../benchmarks.md) -- Karşılaştırmalı verimlilik tabloları
- [Gaz Türbini CHP](gas_turbine_chp.md) -- GT + HRSG CHP konfigürasyonları ve kombine çevrim
- [Buhar Türbini CHP](steam_turbine_chp.md) -- BT CHP konfigürasyonları, back-pressure/extraction
- [Motor CHP](engine_chp.md) -- Motor CHP ve HRSG karşılaştırması
- [Trijenerasyon](trigeneration.md) -- CCHP konfigürasyonları
- [Atık Isı Kazanı (Kazan perspektifi)](../../boiler/equipment/waste_heat.md) -- HRSG iç yapı ve kazan tasarım detayları
- [Kojenerasyon Temelleri](../../factory/cogeneration.md) -- Sistem seviyesi CHP
- [Atık Isı Geri Kazanımı](../../factory/waste_heat_recovery.md) -- Fabrika seviyesi stratejiler
- [Pinch Analizi](../../factory/pinch_analysis.md) -- Pinch analiz metodolojisi
- [Verim İyileştirme](../solutions/efficiency_improvement.md) -- Türbin verim iyileştirme yöntemleri
- [Fizibilite](../economics/feasibility.md) -- CHP fizibilite analizi

## Referanslar

- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Horlock, J.H. (1997). *Cogeneration -- Combined Heat and Power (CHP): Thermodynamics and Economics*, Pergamon Press.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Edition, McGraw-Hill.
- Kehlhofer, R. et al. (2009). *Combined-Cycle Gas & Steam Turbine Power Plants*, 3rd Edition, PennWell.
- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators: Design, Applications, and Calculations*, Marcel Dekker.
- Franco, A. & Casarosa, C. (2002). "On some perspectives for increasing the efficiency of combined cycle power plants," *Applied Thermal Engineering*, 22(13), 1501-1518.
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- ASME PTC 4.4 (2008). *Gas Turbine Heat Recovery Steam Generators Performance Test Codes*, ASME.
- Reddy, B.V. et al. (2002). "Second law analysis of a waste heat recovery steam generator," *International Journal of Heat and Mass Transfer*, 45(9), 1807-1814.
- Mansouri, M.T. et al. (2012). "Exergetic and economic evaluation of the effect of HRSG configurations on the performance of combined cycle power plants," *Energy Conversion and Management*, 58, 47-58.
