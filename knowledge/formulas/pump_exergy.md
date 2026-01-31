# Pompa Exergy Hesaplamaları

> Son güncelleme: 2026-01-31

## Temel İlkeler

Pompa elektrik enerjisini (saf exergy) sıvı basınç exergy'sine dönüştürür.
Dönüşüm sırasında entropi üretilir ve exergy yok edilir.
Sıvı pompalarında, kompresörden farklı olarak, sıcaklık değişimi ihmal edilebilir
düzeydedir (sıkıştırılamaz sıvı kabulü).

## 1. Temel Hesaplama Adımları

### 1.1 Giren Exergy (Elektrik)

Elektrik saf exergy'dir:
```
Ex_in = P_electric [kW]
```

### 1.2 Hidrolik Güç (Hydraulic Power)

Pompanın sıvıya verdiği faydalı güç:
```
P_hyd = ρ × g × Q × H / 1000   [kW]

Burada:
- ρ = sıvı yoğunluğu [kg/m³] (su için ~1000 kg/m³)
- g = yerel çekim ivmesi = 9.81 m/s²
- Q = hacimsel debi [m³/s]
- H = toplam hat (total head) [m]
```

Alternatif (basınç cinsinden):
```
P_hyd = Q × ΔP / 1000   [kW]

Burada:
- Q = debi [m³/s]
- ΔP = basınç artışı [kPa]
```

Alternatif (pratik birimlerle):
```
P_hyd = ρ × g × Q_h × H / (3.6 × 10⁶)   [kW]

Burada:
- Q_h = debi [m³/h]
- Diğer birimler aynı
```

### 1.3 Çıkan Exergy (Faydalı İş — Basınç Exergy'si)

Sıkıştırılamaz sıvı için basınç exergy'si:
```
Ex_out = Q × (P₂ - P₁) / 1000   [kW]

Burada:
- Q = hacimsel debi [m³/s]
- P₂ = pompa çıkış basıncı [kPa, mutlak]
- P₁ = pompa giriş basıncı [kPa, mutlak]
```

Yükseklik cinsinden:
```
Ex_out = ρ × g × Q × H / 1000 = P_hyd   [kW]
```

Not: Sıkıştırılamaz sıvılarda, basınç exergy'si = hidrolik güç.
Kompresörden farklı olarak termal exergy bileşeni ihmal edilebilir.

### 1.4 Exergy Yıkımı

```
Ex_destroyed = Ex_in - Ex_out   [kW]
Ex_destroyed = P_electric - P_hyd   [kW]
```

### 1.5 Exergy Verimi

```
η_ex = Ex_out / Ex_in × 100   [%]
η_ex = P_hyd / P_electric × 100   [%]
```

Not: Pompalarda exergy verimi = wire-to-water verimi'dir (sıcaklık değişimi ihmal edildiğinde).

### 1.6 Yıllık Maliyet

```
Yıllık_kayıp_kWh = Ex_destroyed × çalışma_saati
Yıllık_kayıp_EUR = Yıllık_kayıp_kWh × elektrik_fiyatı
```

## 2. Şaft Gücü ve Verimler

### 2.1 Pompa Verimi

```
η_pump = P_hyd / P_shaft × 100   [%]

Burada:
- P_hyd = hidrolik güç [kW]
- P_shaft = şaft gücü (brake power) [kW]
```

Pompa verimi üç bileşenden oluşur:
```
η_pump = η_hydraulic × η_volumetric × η_mechanical

Burada:
- η_hydraulic = hidrolik verim (sürtünüm ve şok kayıpları)
- η_volumetric = volümetrik verim (iç kaçak, aşınma halka boşlukları)
- η_mechanical = mekanik verim (rulman, salmastra sürtünümü)
```

### 2.2 Motor Verimi

```
η_motor = P_shaft / P_electric × 100   [%]

Burada:
- P_electric = motora giren elektrik gücü [kW]
- P_shaft = motor çıkış gücü (şaft gücü) [kW]
```

Motor kayıpları: bakır kaybı, demir kaybı, mekanik kayıp, ek kayıplar.

### 2.3 VSD Verimi

```
η_VSD = P_motor_giriş / P_şebeke × 100   [%]

Tipik değerler:
- Tam yükte: %95-98
- Kısmi yükte (%50): %92-96
- Düşük yükte (%25): %88-93
```

VSD kayıpları: anahtarlama kayıpları, harmonik kayıplar, filtre kayıpları.

### 2.4 Wire-to-Water Verimi

```
η_w2w = η_pump × η_motor × η_VSD   [ondalık]
η_w2w = P_hyd / P_electric_şebeke × 100   [%]
```

VSD yoksa η_VSD = 1.00 (doğrudan hat beslemesi).

## 3. Affinity Laws (Benzerlik Kanunları)

Santrifüj pompalar için geçerli olan temel ilişkiler.

### 3.1 Hız Değişimi Formülleri (Sabit İmpeller Çapı)

```
Q₂/Q₁ = N₂/N₁                      (Debi, hızla doğrudan orantılı)
H₂/H₁ = (N₂/N₁)²                   (Hat, hızın karesiyle orantılı)
P₂/P₁ = (N₂/N₁)³                   (Güç, hızın küpüyle orantılı)

Burada:
- Q = debi [m³/h]
- H = hat [m]
- P = güç [kW]
- N = devir sayısı [rpm]
```

### 3.2 İmpeller Çapı Değişimi Formülleri (Sabit Hız)

```
Q₂/Q₁ = D₂/D₁                      (Debi, çapla doğrudan orantılı)
H₂/H₁ = (D₂/D₁)²                   (Hat, çapın karesiyle orantılı)
P₂/P₁ = (D₂/D₁)³                   (Güç, çapın küpüyle orantılı — yaklaşık*)

Burada:
- D = impeller çapı [mm]
```

*Not: İmpeller trim için güç ilişkisi (D₂/D₁)³ değil, pratikte daha doğru
sonuç için (D₂/D₁)^(2 ila 2.5) arası kullanılır. Çap değişimi %10-15'i
aştığında affinity law'lar sapma gösterir.

### 3.3 VSD Tasarruf Hesabı

Saf sürtünüm sistemi (statik hat = 0):
```
Tasarruf_gücü = P_nominal × [1 - (Q_yeni/Q_nominal)³]   [kW]

Tasarruf(%) = [1 - (Q_yeni/Q_nominal)³] × 100

Örnek: Debi %80'e düşürülürse:
Tasarruf = [1 - 0.8³] × 100 = [1 - 0.512] × 100 = %48.8
```

Statik hat olan sistem:
```
P_yeni/P_eski = (Q_yeni/Q_eski) × [H_static + K × Q_yeni²] / [H_static + K × Q_eski²]

Burada:
- H_static = statik hat bileşeni [m]
- K = boru sürtünüm katsayısı
```

Statik hat oranı arttıkça VSD tasarrufu azalır.

### 3.4 Affinity Law Sınırları

- Pompanın verim eğrisi sabittir varsayımı: Pratikte verim düşük hızlarda hafif azalır
- Sadece santrifüj (rotadinamik) pompalar için geçerlidir
- Aşırı hız azaltması (%40'ın altına) için dikkatli olunmalı (minimum hız sınırı)
- Spesifik hızı düşük pompalarda (Ns < 20) sapma daha belirgindir

## 4. Sistem Eğrisi (System Curve)

### 4.1 Toplam Sistem Hatı

```
H_system = H_static + H_friction

H_system = H_static + K × Q²

Burada:
- H_static = statik hat [m] (yükseklik farkı + tank basınç farkı)
- K = sistem sürtünüm direnç katsayısı [m/(m³/h)²]
- Q = debi [m³/h]
```

Statik hat bileşeni:
```
H_static = (z₂ - z₁) + (P₂ - P₁)/(ρ × g)

Burada:
- z₂ - z₁ = yükseklik farkı [m]
- P₂ - P₁ = basınç farkı (açık/kapalı tank) [Pa]
```

### 4.2 Operasyon Noktası Bulma

Pompa ve sistem eğrisinin kesişim noktası:
```
H_pump(Q) = H_system(Q)

Pompanın H-Q eğrisi tipik olarak parabola:
H_pump = A - B × Q²   (yaklaşık, 2. derece polinom)
```

Çözüm:
```
A - B × Q² = H_static + K × Q²
Q_op = √[(A - H_static) / (B + K)]
```

### 4.3 Throttling Kaybı Hesabı

Throttle valf ile debi azaltıldığında:
```
H_throttle = H_pump(Q_azaltılmış) - H_system(Q_azaltılmış)   [m]

P_throttle = ρ × g × Q_azaltılmış × H_throttle / 1000   [kW]

Yıllık_israf = P_throttle × çalışma_saati × elektrik_fiyatı / η_motor   [€/yıl]
```

Bu değer, VSD ile ortadan kaldırılabilir potansiyel tasarrufu gösterir.

## 5. NPSH Hesabı

### 5.1 NPSHa (Available — Mevcut)

```
NPSHa = (P_atm - P_vapor) / (ρ × g) + H_s - H_f   [m]

Burada:
- P_atm = atmosfer basıncı [Pa] (101325 Pa, deniz seviyesinde)
- P_vapor = sıvının buhar basıncı [Pa] (sıcaklığa bağlı)
- ρ = sıvı yoğunluğu [kg/m³]
- g = 9.81 m/s²
- H_s = statik emme yüksekliği [m] (pompa altında +, üstünde -)
- H_f = emme hattı sürtünüm kayıpları [m]
```

Açık tank, pompa tankın altında:
```
NPSHa = (P_atm - P_vapor)/(ρ × g) + z_sıvı - H_f
```

Açık tank, pompa tankın üstünde (emme):
```
NPSHa = (P_atm - P_vapor)/(ρ × g) - z_pompa - H_f
```

### 5.2 Kavitasyon Kriteri

```
NPSHa ≥ NPSHr + güvenlik payı

Güvenlik payı:
- Normal uygulamalar: 0.5-1.0 m
- Sıcak sıvılar veya kritik uygulamalar: 1.0-3.0 m
- API 610 standardı: NPSHa ≥ NPSHr + 1.0 m (minimum)
```

Kavitasyon tehlike işareti: NPSHa < 1.3 × NPSHr

### 5.3 Sıcaklık ve Yükseklik Etkisi

Su buhar basıncı (seçilmiş sıcaklıklar):
```
| Sıcaklık (°C) | P_vapor (kPa) | NPSH Etkisi |
| 20             | 2.34          | Referans     |
| 40             | 7.38          | -0.51 m      |
| 60             | 19.94         | -1.80 m      |
| 80             | 47.39         | -4.59 m      |
| 100            | 101.33        | -10.09 m     |
```

Yükseklik etkisi:
```
| Yükseklik (m) | P_atm (kPa) | NPSH Etkisi |
| 0 (deniz)     | 101.33       | Referans     |
| 500           | 95.46        | -0.60 m      |
| 1000          | 89.87        | -1.17 m      |
| 1500          | 84.56        | -1.71 m      |
| 2000          | 79.50        | -2.22 m      |
```

## 6. Spesifik Hız (Specific Speed)

### 6.1 Ns Formülü

```
Ns = N × √Q / H^(3/4)

Burada:
- N = devir sayısı [rpm]
- Q = debi [m³/s] (BEP noktasında)
- H = hat [m] (BEP noktasında, kademe başına)
```

Metrik birim sistemi (Avrupa — nq):
```
nq = N × √(Q_m³/s) / H^(3/4)

Burada Q, m³/s cinsindendir.
```

ABD birim sistemi (Ns):
```
Ns = N × √(Q_gpm) / H_ft^(3/4)

nq = Ns / 51.6 (yaklaşık dönüşüm)
```

### 6.2 Spesifik Hıza Göre Pompa Tipi Seçimi

| nq Aralığı | İmpeller Tipi | Tipik Verim | Tipik Uygulama |
|------------|---------------|-------------|----------------|
| 10-25 | Radyal, yüksek hat | %60-80 | Yüksek basınç, düşük debi |
| 25-50 | Radyal, orta hat | %75-88 | Genel endüstriyel |
| 50-80 | Radyal, düşük hat | %80-90 | Büyük debi, orta hat |
| 80-140 | Karışık akışlı | %82-92 | Büyük debi, düşük hat |
| 140-350 | Aksiyel | %84-93 | Çok büyük debi, çok düşük hat |

### 6.3 Spesifik Hız ve Verim İlişkisi

Genel kural: Spesifik hız arttıkça BEP verimi artar (büyük debi pompaları).
Ancak aksiyel pompalarda işletme aralığı daralır (dik verim eğrisi).

```
η_BEP_approx = 0.94 - 0.286 / (nq)^0.4   (yaklaşık, büyük pompalar için)
```

## 7. Sistem Seviyesi Exergy Analizi

### 7.1 Sistem Exergy Girişi

```
Ex_input = Σ(P_electric_i) + P_yardımcı   [kW]

Burada:
- P_electric_i = her bir pompanın elektrik gücü [kW]
- P_yardımcı = soğutma, kontrol vb. yardımcı güç [kW]
```

Not: Elektrik saf exergy'dir (%100 exergy içeriği).

### 7.2 Faydalı Exergy Çıkışı

```
Ex_useful = Σ(Q_j × ΔP_j / 1000)   [kW]

Burada:
- Q_j = j kullanım noktasına giden debi [m³/s]
- ΔP_j = j kullanım noktasında gerekli basınç artışı [kPa]
```

Veya yükseklik cinsinden:
```
Ex_useful = Σ(ρ × g × Q_j × H_useful_j / 1000)   [kW]
```

### 7.3 Exergy Kayıp Dağılımı

```
Ex_kayıp_toplam = Ex_input - Ex_useful

Bileşenler:
1. Ex_motor      = P_electric × (1 - η_motor)             — Motor kayıpları
2. Ex_VSD        = P_şebeke × (1 - η_VSD)                 — VSD kayıpları (varsa)
3. Ex_pompa      = P_shaft × (1 - η_pump)                 — Pompa iç kayıpları
                   (hidrolik, volümetrik, mekanik)
4. Ex_boru       = ρ × g × Q × H_f_boru / 1000            — Boru sürtünüm kaybı
5. Ex_throttle   = ρ × g × Q × H_throttle / 1000          — Throttle valf kaybı
6. Ex_bypass     = ρ × g × Q_bypass × H_system / 1000     — Bypass kaybı
7. Ex_recirk     = ρ × g × Q_recirk × H / 1000            — Min. debi resirkülasyonu
8. Ex_boyut      = (P_hyd_gerçek - P_hyd_gerekli)          — Aşırı boyutlandırma kaybı
9. Ex_kaçak      = ρ × g × Q_kaçak × H / 1000             — Sıvı kaçakları
```

### 7.4 Sistem Exergy Verimi

```
η_system = Ex_useful / Ex_input × 100   [%]
```

| Sistem Durumu | η_system | Açıklama |
|--------------|----------|----------|
| Zayıf yönetilen | %15-25 | Aşırı boyut, throttle, bakım yok |
| Ortalama endüstriyel | %25-40 | Kısmen optimize |
| İyi yönetilen | %40-55 | VSD, uygun boyut, iyi bakım |
| En iyi uygulama | %55-70 | Tam optimize, izleme, periyodik denetim |
| Teorik maksimum | ~%80-90 | Mükemmel pompa ve sistem, sıfır kayıp |

### 7.5 Grassmann Diyagramı (Exergy Akış Diyagramı)

```
Elektrik Girişi (100%)
  ├── Motor kayıpları (%4-10)
  ├── VSD kayıpları (%2-5, varsa)
  ├── Pompa iç kayıpları (%10-30)
  │     ├── Hidrolik kayıplar (sürtünüm, şok)
  │     ├── Volümetrik kayıplar (iç kaçak, aşınma halkası)
  │     └── Mekanik kayıplar (rulman, salmastra)
  ├── Boru sürtünüm kaybı (%3-10)
  ├── Throttle valf kaybı (%0-25, kontrole bağlı)
  ├── Bypass kaybı (%0-20, varsa)
  ├── Aşırı boyutlandırma kaybı (%0-15)
  ├── Kaçak kayıpları (%0-5)
  └── Net faydalı exergy (%25-70)
```

## 8. Örnek Hesaplamalar

### 8.1 Temel Exergy Hesabı

**Girdiler:**
- P_electric = 22 kW
- Q = 80 m³/h = 0.0222 m³/s
- H = 45 m (toplam hat)
- ρ = 1000 kg/m³ (su)
- Çalışma = 6000 saat/yıl
- Elektrik = €0.12/kWh

**Hesap:**
```
P_hyd = ρ × g × Q × H / 1000
      = 1000 × 9.81 × 0.0222 × 45 / 1000
      = 9.80 kW

Ex_out = P_hyd = 9.80 kW (sıkıştırılamaz sıvı)

Ex_destroyed = 22 - 9.80 = 12.20 kW

η_ex = 9.80 / 22 × 100 = 44.5%

Yıllık_kayıp = 12.20 × 6000 = 73,200 kWh
Maliyet = 73,200 × 0.12 = €8,784/yıl
```

### 8.2 VSD Tasarruf Hesabı

**Senaryo:** Yukarıdaki pompa, proses debisi %70'e düşürülmeli.
Mevcut durum: throttle valf ile kontrol.
Sistem: %40 statik hat, %60 sürtünüm hatı.

```
Mevcut durum (throttle):
- Pompa hala 22 kW civarı çeker (küçük azalma)
- Ölçülen güç: 19.5 kW (pompa eğrisi üzerinde kayma)
- Faydalı iş: ρ × g × 0.70 × Q × H_system(0.70Q) / 1000

VSD ile:
H_static = 0.40 × 45 = 18 m
H_friction_nominal = 0.60 × 45 = 27 m
H_friction_yeni = 27 × (0.70)² = 13.23 m
H_system_yeni = 18 + 13.23 = 31.23 m

P_hyd_yeni = 1000 × 9.81 × (0.0222 × 0.70) × 31.23 / 1000 = 4.75 kW

η_w2w tahmini (VSD ile) = %42 (kısmi hızda hafif düşüş)
P_electric_VSD = 4.75 / 0.42 = 11.31 kW

Tasarruf = 19.5 - 11.31 = 8.19 kW
Yıllık tasarruf = 8.19 × 6000 × 0.12 = €5,897/yıl
```

### 8.3 Throttle Eliminasyon Tasarrufu

**Senaryo:** Pompada sürekli 8 m throttle kaybı var.

```
P_throttle = ρ × g × Q × H_throttle / 1000
           = 1000 × 9.81 × 0.0222 × 8 / 1000
           = 1.74 kW (hidrolik kayıp)

Motor ve pompa verimi dahil gerçek elektrik kaybı:
P_electric_israf = 1.74 / (η_pump × η_motor)
                 = 1.74 / (0.72 × 0.93)
                 = 2.60 kW

Yıllık tasarruf = 2.60 × 6000 × 0.12 = €1,872/yıl
```

Çözüm: İmpeller trim veya VSD uygulaması ile throttle eliminasyonu.

### 8.4 İmpeller Trim Tasarrufu

**Senaryo:** 250 mm impeller, 230 mm'ye trim.

```
Çap oranı: D₂/D₁ = 230/250 = 0.92

Affinity law'lara göre:
Q_yeni/Q_eski = 0.92 → Q_yeni = Q_eski × 0.92
H_yeni/H_eski = 0.92² = 0.846 → H_yeni = H_eski × 0.846
P_yeni/P_eski = 0.92³ = 0.779 → P_yeni = P_eski × 0.779

Not: Pratikte çap değişimi %10-15 aralığında en doğru sonuçları verir.
Daha büyük değişimler için üretici eğrisi ile doğrulanmalıdır.

Güç tasarrufu tahmini = P_eski × (1 - 0.779) = 22 × 0.221 = 4.86 kW
Yıllık tasarruf = 4.86 × 6000 × 0.12 = €3,499/yıl

Maliyet: İmpeller trim işlemi ~€500-1,500
Geri ödeme: < 6 ay
```

### 8.5 Aşınma Halkası Yenileme Tasarrufu

**Senaryo:** Aşınma halkası boşluğu fabrika değerinin 3 katına ulaşmış.

```
Tipik verim kaybı: %3-5 (boşluğun 3 katında)
Ek güç tüketimi: 22 × 0.04 = 0.88 kW (varsayım: %4 kayıp)

Yıllık israf = 0.88 × 6000 × 0.12 = €634/yıl
Aşınma halkası değişim maliyeti: ~€300-800
Geri ödeme: < 1.5 yıl
```

## 9. Sınırlamalar

1. Sıkıştırılamaz sıvı kabulü yapılmıştır (su, %99+ uygulama için geçerli)
2. Sıcaklık değişimi ihmal edilmiştir (pompa sıcaklık artışı tipik 0.5-2°C)
3. Viskoz sıvılar için ek düzeltme gerekir (Hydraulic Institute viskozite düzeltmesi)
4. Affinity law'lar yaklaşık formüllerdir; büyük hız/çap değişimlerinde sapma olur
5. Kavitasyon durumunda verim ve hat formülleri geçerliliğini yitirir
6. Yük değişimi dinamikleri dahil değildir (ortalama kararlı hal analizi)
7. NPSH hesabında boru fitingleri kayıpları ayrıca hesaplanmalıdır
8. Çok fazlı akış (sıvı+gaz) ve bulamaç akış (sıvı+katı) için ek modeller gerekir

## 10. Referanslar

- Cengel & Boles, "Thermodynamics: An Engineering Approach," Chapter 7
- Bejan, "Advanced Engineering Thermodynamics"
- Kotas, "The Exergy Method of Thermal Plant Analysis"
- Dincer & Rosen, "Exergy: Energy, Environment and Sustainable Development"
- Hydraulic Institute Standards (ANSI/HI)
- ISO 9906:2012, "Rotodynamic Pumps — Hydraulic Performance Acceptance Tests"
- Karassik et al., "Pump Handbook," McGraw-Hill
- Europump & Hydraulic Institute, "Pump Life Cycle Costs"
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Saidur et al. (2010), "A review on exergy analysis of industrial sector," Renewable & Sustainable Energy Reviews
- Sarbu & Borza (1998), "Energetic optimization of water pumping in distribution systems"
