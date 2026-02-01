# Yardımcı Sistemler Analizi (Utility Systems Analysis)

> Son güncelleme: 2026-01-31

## Genel Bakış

Yardımcı (utility) sistemler, fabrika ana proseslerini destekleyen enerji altyapısını oluşturur. Buhar üretim ve dağıtım, basınçlı hava, soğutma suyu, chiller ve HVAC sistemlerini kapsar. Toplam fabrika enerji tüketiminin %30-60'ını oluşturan utility sistemlerindeki kayıplar genellikle düşük maliyetle giderilebilir. Bu dosya, her utility sisteminin enerji ve exergy analizini, benchmark değerlerini, tipik kayıplarını ve iyileştirme fırsatlarını sunar.

## 1. Buhar Sistemleri (Steam Systems)

### 1.1 Buhar Sistemi Bileşenleri

```
Buhar sistemi döngüsü:
Su arıtma → Besleme suyu ısıtma → Kazan → Buhar dağıtım
→ Kullanım noktaları → Kondensat toplama → Geri dönüş

Ana bileşenler:
1. Kazanlar (kapasite, tip, yakıt)
2. Deaeratör (çözünmüş gaz giderme)
3. Economizer (baca gazı ısı geri kazanımı)
4. Dağıtım hatları (headerlar, vanalar, genleşme)
5. Buhar kapanları (steam traps)
6. Kondensat geri dönüş sistemi
7. Blowdown sistemi
```

### 1.2 Buhar Sistemi Enerji / Exergy Verimi

```
Enerji verimi (1. Yasa):
η_enerji = Q_buhar / Q_yakıt × 100 [%]
         = ṁ_buhar × (h_buhar - h_besleme) / (ṁ_yakıt × LHV) × 100

Exergy verimi (2. Yasa):
η_exergy = Ex_buhar / Ex_yakıt × 100 [%]
         = ṁ_buhar × (ex_buhar - ex_besleme) / (ṁ_yakıt × ex_yakıt) × 100

Burada:
- ex_buhar = (h_buhar - h₀) - T₀ × (s_buhar - s₀)  [kJ/kg]
- ex_yakıt ≈ φ × LHV  (φ = 1.04 doğalgaz, 1.06 fuel oil)

Örnek (10 bar doymuş buhar, doğalgaz):
η_enerji ≈ %85-92 (iyi çalışan kazan)
η_exergy ≈ %25-40 (gerçek termodinamik performans)
```

### 1.3 Buhar Sistemi Benchmark Değerleri

| Parametre | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Kazan enerji verimi [%] | <80 | 80-85 | 85-90 | >90 |
| Kazan exergy verimi [%] | <25 | 25-32 | 32-38 | >38 |
| Kondensat geri dönüş oranı [%] | <40 | 40-65 | 65-85 | >85 |
| Buhar kapanı arıza oranı [%] | >25 | 15-25 | 5-15 | <5 |
| Baca gazı sıcaklığı [°C] | >250 | 200-250 | 150-200 | <150 |
| Baca gazı O₂ [%] | >6 | 4-6 | 2.5-4 | 2-2.5 |
| Dağıtım kaybı [%] | >12 | 8-12 | 4-8 | <4 |
| Blowdown oranı [%] | >10 | 5-10 | 2-5 | <2 |

### 1.4 Buhar Sistemi Tipik Kayıplar

| Kayıp Kaynağı | Tipik Kayıp [%] | İyileştirme Yöntemi | Tasarruf Potansiyeli |
|---|---|---|---|
| Yanma kayıpları | 8-15 | O₂ kontrolü, brülör bakımı | %3-5 yakıt |
| Baca gazı ısısı | 5-12 | Economizer, yoğuşmalı kazanlar | %4-8 yakıt |
| Yüzey kayıpları (radyasyon) | 1-3 | İzolasyon iyileştirme | %1-2 yakıt |
| Blowdown kayıpları | 1-5 | Blowdown ısı geri kazanımı, TDS kontrolü | %1-3 yakıt |
| Kondensat kayıpları | 3-15 | Kondensat geri dönüş sistemi | %5-10 yakıt + su |
| Buhar kapanı kaçakları | 5-20 | Düzenli bakım ve değişim | %5-15 buhar |
| İzolasyon eksiklikleri | 2-8 | Flanş, vana izolasyonu | %2-5 buhar |
| Flash buhar kaybı | 1-5 | Flash buhar geri kazanımı | %1-3 buhar |

### 1.5 Buhar Dağıtım Verimi Hesabı

```
η_dağıtım = ṁ_buhar,kullanım / ṁ_buhar,kazan × 100 [%]

Veya enerji bazında:
η_dağıtım = Σ(ṁᵢ × hᵢ)_kullanım / (ṁ_üretim × h_üretim) × 100 [%]

Kayıp bileşenleri:
Q_kayıp,dağıtım = Q_izolasyon + Q_kapan + Q_kaçak + Q_flash

Hesaplama örneği:
Kazan buhar üretimi: 8 ton/h (10 bar, doymuş, h = 2,778 kJ/kg)
Kullanım noktalarında ölçülen buhar: 6.8 ton/h
Kapan kaçakları (ultrasonik tespit): 0.4 ton/h
İzolasyon kayıpları (IR termografi): 0.3 ton/h
Bilinmeyen kayıplar: 0.5 ton/h

η_dağıtım = 6.8 / 8.0 = %85.0

İzolasyon kayıp hesabı (çıplak boru):
Q = h_c × A × (T_yüzey - T_ortam)
h_c ≈ 10 W/(m²·°C) (doğal konveksiyon, yatay boru)
10 bar buhar: T_yüzey ≈ 180°C (izolasyonsuz)
A = π × D × L
Q_100m = 10 × π × 0.15 × 100 × (180 - 25) = 73,000 W = 73 kW

İzolasyon sonrası (50mm taş yünü):
T_yüzey ≈ 40°C
Q_izolasyonlu = 10 × π × 0.25 × 100 × (40 - 25) = 11,800 W ≈ 12 kW
Tasarruf: 73 - 12 = 61 kW (%84 azalma)
```

## 2. Basınçlı Hava Sistemleri (Compressed Air Systems)

### 2.1 Sistem Bileşenleri

```
Basınçlı hava sistemi:
Giriş filtresi → Kompresör → Aftercooler → Kurutucu
→ Depolama tankı → Dağıtım hatları → Kullanım noktaları

Ana bileşenler:
1. Kompresörler (vida, piston, santrifüj)
2. Soğutucular (aftercooler, intercooler)
3. Kurutucular (soğutmalı, adsorpsiyonlu)
4. Filtreler (partikül, koalesör, aktif karbon)
5. Depolama tankları (alıcı)
6. Dağıtım hatları (ring, çatal)
7. Drenaj valfleri (otomatik, zamanlı)
```

### 2.2 Basınçlı Hava Sistemi Benchmark Değerleri

| Parametre | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Özgül güç [kW/(m³/min)] | >8.0 | 6.5-8.0 | 5.5-6.5 | <5.5 |
| Kaçak oranı [%] | >30 | 20-30 | 10-20 | <10 |
| Sistem basıncı [bar] | >8.5 | 7.5-8.5 | 6.5-7.5 | <6.5 |
| Basınç düşüşü (üretim→kullanım) [bar] | >1.5 | 1.0-1.5 | 0.5-1.0 | <0.5 |
| Kurutucu enerji payı [%] | >20 | 12-20 | 5-12 | <5 |
| Yüksüz çalışma oranı [%] | >30 | 15-30 | 5-15 | <5 |
| Atık ısı geri kazanım oranı [%] | 0 | 0-30 | 30-60 | >60 |

### 2.3 Basınçlı Hava Özgül Güç Hesabı

```
Özgül güç (Specific Power):
SP = P_kompresör / Q_FAD [kW/(m³/min)]

Burada:
- P_kompresör = kompresör şaft gücü [kW]
- Q_FAD = Free Air Delivery (serbest hava debisi) [m³/min]

Teorik izothermal güç:
P_iso = P₁ × Q₁ × ln(P₂/P₁)

Burada:
- P₁ = giriş basıncı [kPa]
- Q₁ = giriş hava debisi [m³/s]
- P₂ = çıkış basıncı [kPa]

Örnek:
Q_FAD = 15 m³/min, P₂ = 7 bar(g) = 8.013 bar(a)
P_iso = 101.325 × (15/60) × ln(801.3/101.3) = 101.325 × 0.25 × 2.069
P_iso = 52.4 kW

Gerçek güç (vida kompresör):
P_gerçek = P_iso / (η_izo × η_motor) = 52.4 / (0.70 × 0.93) = 80.5 kW
SP = 80.5 / 15 = 5.37 kW/(m³/min)  → İyi seviye
```

### 2.4 Basınçlı Hava Kaçak Maliyet Hesabı

```
Kaçak debisi hesaplama (sistem durdurma testi):
Q_kaçak = V_tank × (P_1 - P_2) / (P_atm × t_düşüş) [m³/min]

Veya yükleme oranından:
Q_kaçak = Q_FAD × (t_yüklü / t_toplam) × (1 - yük_faktörü_üretim)

Maliyet hesabı:
Yıllık kaçak maliyeti = Q_kaçak × SP × t_çalışma × C_elektrik

Örnek:
Q_kaçak = 4.5 m³/min (%30 kaçak oranı, 15 m³/min sistemde)
SP = 5.5 kW/(m³/min)
Çalışma: 6,000 saat/yıl
Elektrik fiyatı: €0.12/kWh

Kaçak güç: 4.5 × 5.5 = 24.75 kW
Yıllık kaçak maliyeti: 24.75 × 6,000 × 0.12 = €17,820/yıl

Kaçak onarım maliyeti: ~€2,000-5,000
SPP = 3,500 / 17,820 = 0.2 yıl (2.4 ay)
```

### 2.5 Basınç Optimizasyonu

```
Her 1 bar basınç düşürme ≈ %6-8 enerji tasarrufu

Basınç optimizasyon adımları:
1. Tüm kullanım noktalarında gerçek basınç gereksinimini belirle
2. En yüksek gerekli basıncı tespit et
3. Dağıtım basınç kayıplarını ölç
4. Kompresör set basıncını minimize et
5. Yüksek basınç ihtiyaçlarını ayrı karşıla (booster)

Örnek:
Mevcut set basıncı: 8.5 bar(g)
Gerekli maksimum kullanım basıncı: 6.0 bar(g)
Dağıtım basınç kaybı: 0.8 bar
Yeni set basıncı: 6.0 + 0.8 = 6.8 bar(g)
Düşürme: 8.5 - 6.8 = 1.7 bar

Tasarruf: 1.7 × %7/bar ≈ %12 enerji tasarrufu
Güç tasarrufu: 80 kW × 0.12 = 9.6 kW
Yıllık tasarruf: 9.6 × 6,000 × 0.12 = €6,912/yıl
Yatırım: €0 (basınç ayarı) + regülatör/vana: €500
SPP: 0.07 yıl (1 ay) → Quick win
```

## 3. Soğutma Suyu Sistemleri (Cooling Water Systems)

### 3.1 Sistem Tipleri

```
1. Açık devre (once-through):
   Kaynak su → Kullanım → Deşarj
   Avantaj: Basit, düşük yatırım
   Dezavantaj: Yüksek su tüketimi, çevre kısıtları

2. Kapalı devre (recirculating — evaporatif):
   Soğutma kulesi → Pompa → Kullanım → Soğutma kulesi
   Avantaj: Düşük su tüketimi (%2-5 taze su)
   Dezavantaj: Kule bakımı, su arıtma, Legionella riski

3. Kuru soğutma (dry cooler):
   Hava soğutmalı eşanjör → Pompa → Kullanım → Eşanjör
   Avantaj: Susuz, düşük bakım
   Dezavantaj: Performans ortam sıcaklığına bağlı
```

### 3.2 Soğutma Kulesi Performans Göstergeleri

| Parametre | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Yaklaşım sıcaklığı [°C] | >8 | 5-8 | 3-5 | <3 |
| Range (T_giriş - T_çıkış) [°C] | <3 | 3-6 | 6-10 | >10 |
| L/G oranı (su/hava) | >2.0 | 1.2-2.0 | 0.8-1.2 | Optimize |
| Drift kaybı [%] | >0.2 | 0.1-0.2 | 0.01-0.1 | <0.01 |
| Pompa özgül güç [kW/100kW soğutma] | >5 | 3-5 | 2-3 | <2 |
| Fan özgül güç [kW/100kW soğutma] | >3 | 2-3 | 1-2 | <1 |
| Su arıtma cycles of concentration | <3 | 3-5 | 5-8 | >8 |

### 3.3 Soğutma Kulesi Yaklaşım Sıcaklığı Analizi

```
Yaklaşım sıcaklığı (Approach):
T_yaklaşım = T_soğutma_suyu_çıkış - T_yaş_termometre [°C]

Burada:
- T_soğutma_suyu_çıkış = kuleden çıkan suyun sıcaklığı
- T_yaş_termometre = ortam yaş termometre sıcaklığı (wet bulb)

Yaklaşım sıcaklığı arttığında:
- Soğutma kapasitesi düşer
- Chiller condenser basıncı artar → COP düşer
- Proses soğutma verimi düşer

Her 1°C yaklaşım artışı → Chiller enerji tüketiminde %2-3 artış

Örnek:
Mevcut: T_yaklaşım = 7°C, T_wb = 22°C → T_soğutma = 29°C
İyileştirme sonrası: T_yaklaşım = 4°C → T_soğutma = 26°C
Chiller tasarrufu: 3 × %2.5 = %7.5
Chiller gücü: 200 kW → Tasarruf: 15 kW → €10,800/yıl
```

### 3.4 Soğutma Suyu Pompa Optimizasyonu

```
Pompa gücü:
P_pompa = (Q × ΔP) / (η_pompa × η_motor) [kW]

Burada:
- Q = debi [m³/s]
- ΔP = basınç farkı [Pa]
- η_pompa = pompa verimi [oran]
- η_motor = motor verimi [oran]

Optimizasyon fırsatları:
1. VSD ile debi kontrolü (kısma vanası yerine)
   Tasarruf: Affinite yasası → P ∝ Q³
   %20 debi azalma → %49 güç tasarrufu

2. Paralel pompa sekanslaması
   Düşük yükte tek pompa, yüksek yükte çoklu pompa

3. Boru hattı iyileştirme
   Basınç kayıplarını azaltma → pompa gücü düşer
```

## 4. Chiller Sistemleri (Chiller Systems)

### 4.1 Chiller Performans Göstergeleri

| Parametre | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| COP (su soğutmalı, tam yük) | <4.5 | 4.5-5.5 | 5.5-6.5 | >6.5 |
| COP (hava soğutmalı, tam yük) | <2.5 | 2.5-3.2 | 3.2-3.8 | >3.8 |
| IPLV/NPLV | <5.0 | 5.0-7.0 | 7.0-9.0 | >9.0 |
| kW/ton (su soğutmalı) | >0.75 | 0.55-0.75 | 0.45-0.55 | <0.45 |
| Evaporatör yaklaşım [°C] | >4 | 2.5-4 | 1.5-2.5 | <1.5 |
| Condenser yaklaşım [°C] | >3 | 2-3 | 1-2 | <1 |
| Soğutucu akışkan şarjı farkı [%] | >10 | 5-10 | 2-5 | <2 |

### 4.2 Chiller Exergy Analizi

```
Chiller exergy verimi:
η_ex = Q_soğutma × |1 - T₀/T_soğutma| / W_kompresör × 100 [%]

Burada:
- Q_soğutma = soğutma kapasitesi [kW]
- T₀ = ortam sıcaklığı [K]
- T_soğutma = soğutulan ortam sıcaklığı [K]
- W_kompresör = kompresör gücü [kW]

Örnek:
Q_soğutma = 500 kW, T_soğutma = 7°C = 280.15 K
T₀ = 35°C = 308.15 K, W_kompresör = 100 kW

COP = 500 / 100 = 5.0
Carnot COP = T_soğutma / (T₀ - T_soğutma) = 280.15 / 28 = 10.0

Exergy çıktısı: 500 × |1 - 308.15/280.15| = 500 × 0.0999 = 49.9 kW
η_ex = 49.9 / 100 = %49.9

Exergy verimi ile COP ilişkisi:
η_ex = COP / COP_Carnot × 100 = 5.0 / 10.0 × 100 = %50
```

### 4.3 Chiller Optimizasyon Fırsatları

| İyileştirme | Tipik Tasarruf [%] | Yatırım | SPP [yıl] |
|---|---|---|---|
| Condenser suyu sıcaklığı düşürme (1°C) | 2-3 | Düşük | <0.5 |
| Chilled water sıcaklık sıfırlama (reset) | 3-8 | Düşük | <1 |
| VSD kompresör | 15-25 | Orta | 2-4 |
| Soğutma kulesi optimizasyonu | 5-10 | Düşük-Orta | 1-2 |
| Free cooling (economizer) | 20-40 | Orta | 2-3 |
| Chiller sekanslaması | 5-15 | Düşük | <1 |
| Evaporatör/condenser temizliği | 2-5 | Düşük | <0.5 |

## 5. HVAC Sistemleri

### 5.1 HVAC Enerji Benchmark

| Parametre | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Toplam HVAC özgül enerji [kWh/m²·yıl] | >200 | 120-200 | 60-120 | <60 |
| Isıtma özgül enerji [kWh/m²·yıl] | >100 | 60-100 | 30-60 | <30 |
| Soğutma özgül enerji [kWh/m²·yıl] | >80 | 50-80 | 25-50 | <25 |
| Fan özgül güç (SFP) [W/(l/s)] | >3.0 | 2.0-3.0 | 1.2-2.0 | <1.2 |
| Taze hava oranı kontrolü | Sabit | Zamanlı | CO₂ bazlı | Optimum |

### 5.2 HVAC Tipik Kayıplar ve İyileştirmeler

| Kayıp Kaynağı | Tipik Kayıp | İyileştirme | Tasarruf |
|---|---|---|---|
| Aşırı havalandırma | %20-40 fazla enerji | DCV (Demand Controlled Ventilation) | %15-30 |
| Eşzamanlı ısıtma/soğutma | %10-20 enerji israfı | Deadband ayarı, zon kontrolü | %10-15 |
| Filter basınç düşüşü | %5-10 fan enerjisi | Düzenli değişim programı | %5-8 |
| Isı geri kazanımsız egzoz | %30-50 ısı kaybı | Enerji geri kazanım cihazı | %40-70 (egzoz ısısının) |
| Kötü izolasyonlu kanal | %5-15 enerji kaybı | Kanal izolasyonu/sızdırmazlık | %5-10 |

## 6. Total Site Profile ve Utility Pinch

### 6.1 Total Site Profile Kavramı

```
Total Site Profile (TSP), fabrikanın tüm proseslerinin utility
sistemi üzerinden birbirine bağlandığını gösteren analiz aracıdır.

Adımlar:
1. Her proses birimi için ayrı pinch analizi yap
2. Her birimin GCC'sinden utility gereksinimlerini çıkar
3. Site-level sıcak ve soğuk utility profillerini birleştir
4. Site Composite Curves oluştur
5. CHP (kojenerasyon) potansiyelini değerlendir

TSP ile belirlenen potansiyeller:
- Prosesler arası ısı entegrasyonu (utility üzerinden)
- Optimum buhar header basınçları
- CHP boyutlandırma
- Utility tasarım parametreleri
```

### 6.2 Buhar Header Optimizasyonu

```
Tipik buhar header yapısı:
HP Buhar (40 bar, 250°C) → Türbin/PRV → MP Buhar (10 bar, 180°C)
                                        → Türbin/PRV → LP Buhar (3 bar, 134°C)

Optimizasyon kriterleri:
1. Her header'da üretim = tüketim dengesini sağla
2. Artık buharı minimize et (venting)
3. Letdown (PRV) yerine back-pressure türbin kullan
4. Kondensat geri dönüşünü her seviyede maksimize et

Header basınç optimizasyonu:
- Her header basıncını proses ihtiyaçlarına göre belirle
- GCC analizi ile optimum header sayısı ve basınçlarını tespit et
- HP buhar üretimi ile elektrik kojenerasyonu değerlendir

Örnek:
Mevcut: 3 header (HP/MP/LP)
MP letdown: 2 ton/h PRV ile → Exergy yıkımı
Çözüm: Back-pressure türbin (500 kW elektrik üretimi)
Yatırım: €120,000
Elektrik tasarrufu: 500 kW × 6,000 h × €0.12 = €360,000/yıl
SPP: 0.33 yıl
```

### 6.3 Utility Pinch Kavramı

```
Utility pinch, utility sisteminin darboğaz noktasıdır:
- Buhar pinch: Belirli bir header'da üretim-tüketim darboğazı
- Soğutma pinch: Soğutma kapasitesi sınırı
- Elektrik pinch: Trafo veya hat kapasitesi sınırı

Utility pinch'in belirlenmesi:
1. Her utility için zaman bazlı üretim ve tüketim profilini çıkar
2. En yüksek talep anını (peak) tespit et
3. Peak / ortalama oranını hesapla (peak factor)
4. Tepe yönetimi stratejileri geliştir

Peak factor değerlendirme:
< 1.2: Düz profil, iyi yönetilen sistem
1.2-1.5: Kabul edilebilir, tepe kaydırma fırsatı olabilir
1.5-2.0: Yüksek tepe, ciddi optimizasyon potansiyeli
> 2.0: Çok yüksek, depolama veya kapasite artırımı gerekli
```

## 7. Entegre Utility Sistemi Verimi

### 7.1 Toplam Utility Sistemi Enerji Dengesi

```
Toplam utility enerji girişi:
E_utility = E_yakıt + E_elektrik(utility) [kWh/yıl]

Toplam faydalı enerji çıkışı:
E_faydalı = E_buhar(kullanım) + E_basınçlı_hava(kullanım) + E_soğutma(kullanım)
           + E_HVAC(kullanım) [kWh/yıl]

Utility sistemi verimi:
η_utility = E_faydalı / E_utility × 100 [%]

Tipik değerler:
- Kötü yönetilen tesis: %40-55
- Ortalama tesis: %55-70
- İyi yönetilen tesis: %70-85
- Mükemmel: >%85
```

### 7.2 Utility Maliyeti Dağılımı

```
Tipik utility maliyet dağılımı (endüstriyel tesis):

| Utility | Enerji Payı [%] | Maliyet Payı [%] |
|---------|-----------------|------------------|
| Buhar sistemi | 45-65 | 35-55 |
| Basınçlı hava | 10-25 | 12-25 |
| Soğutma | 5-20 | 8-20 |
| HVAC | 5-15 | 5-12 |
| Aydınlatma | 3-8 | 3-8 |
| Diğer | 2-10 | 2-8 |

Maliyet hesabı:
C_utility = Σ(Eᵢ × Cᵢ) + C_su + C_arıtma + C_bakım [€/yıl]

Burada:
- Eᵢ = i-inci utility enerji tüketimi [kWh/yıl]
- Cᵢ = i-inci enerji birim fiyatı [€/kWh]
- C_su = su maliyeti [€/yıl]
- C_arıtma = su arıtma maliyeti [€/yıl]
- C_bakım = bakım maliyeti [€/yıl]
```

### 7.3 Kapsamlı Hesaplama Örneği

```
Orta ölçekli fabrika utility sistemi:

Buhar sistemi:
- Doğalgaz: 400 Nm³/h × 10.5 kWh/Nm³ = 4,200 kW (yakıt)
- Kazan enerji verimi: %87
- Buhar üretimi: 4,200 × 0.87 = 3,654 kW (buhar)
- Dağıtım verimi: %90
- Faydalı buhar: 3,654 × 0.90 = 3,289 kW
- Buhar sistemi toplam verim: 3,289 / 4,200 = %78.3

Basınçlı hava:
- Kompresör gücü: 120 kW
- Kaçak oranı: %25
- Faydalı hava gücü: 120 × (1-0.25) × (exergy/enerji) ≈ 120 × 0.75 × 0.12 = 10.8 kW
- Exergy verimi: 10.8 / 120 = %9.0

Soğutma sistemi:
- Chiller gücü: 80 kW
- COP = 5.0
- Soğutma kapasitesi: 400 kW
- Exergy çıktısı: 400 × |1-308/280| = 40 kW
- Exergy verimi: 40 / 80 = %50

HVAC:
- Elektrik: 60 kW (fan + pompa + kontrol)
- Faydalı ısıtma/soğutma: 180 kW
- COP eşdeğeri: 180/60 = 3.0

Toplam utility enerji girişi: 4,200 + 120 + 80 + 60 = 4,460 kW
Toplam faydalı çıkış (enerji): 3,289 + 90(hava) + 400 + 180 = 3,959 kW
Utility enerji verimi: 3,959 / 4,460 = %88.8 (görünüşte iyi)

Toplam utility exergy girişi: 4,200×1.04 + 120 + 80 + 60 = 4,628 kW
Toplam faydalı exergy çıkışı: 1,100(buhar) + 10.8 + 40 + 15 = 1,166 kW
Utility exergy verimi: 1,166 / 4,628 = %25.2 (gerçek performans)
```

## 8. Utility Sistemi İyileştirme Yol Haritası

### 8.1 Hızlı Kazanımlar (Quick Wins — 0-6 ay)

| Önlem | Yatırım [€] | Yıllık Tasarruf [€] | SPP |
|---|---|---|---|
| Basınçlı hava kaçak onarımı | 2,000-5,000 | 10,000-25,000 | 1-3 ay |
| Kompresör basınç optimizasyonu | 0-500 | 5,000-15,000 | <1 ay |
| Buhar kapanı bakım/değişimi | 3,000-10,000 | 8,000-30,000 | 2-6 ay |
| Kazan yanma ayarı (O₂ kontrolü) | 500-2,000 | 5,000-15,000 | 1-2 ay |
| Kondensat geri dönüş artırımı | 2,000-8,000 | 10,000-25,000 | 2-6 ay |
| Chiller set noktası optimizasyonu | 0 | 3,000-8,000 | 0 |
| HVAC zamanlama programı | 0-500 | 5,000-15,000 | <1 ay |

### 8.2 Orta Vadeli Projeler (6-24 ay)

| Önlem | Yatırım [€] | Yıllık Tasarruf [€] | SPP |
|---|---|---|---|
| Kompresör VSD retrofit | 15,000-30,000 | 8,000-18,000 | 1.5-3 yıl |
| Economizer ekleme | 25,000-50,000 | 10,000-25,000 | 2-3 yıl |
| Kompresör atık ısı geri kazanımı | 8,000-20,000 | 5,000-12,000 | 1-2 yıl |
| Soğutma kulesi yenileme | 20,000-50,000 | 8,000-20,000 | 2-3 yıl |
| İzolasyon iyileştirme (tesis geneli) | 10,000-30,000 | 5,000-15,000 | 1.5-3 yıl |
| Enerji izleme sistemi (BMS) | 30,000-80,000 | 15,000-40,000 | 2-3 yıl |

### 8.3 Stratejik Yatırımlar (2-5 yıl)

| Önlem | Yatırım [€] | Yıllık Tasarruf [€] | SPP |
|---|---|---|---|
| CHP (kojenerasyon) sistemi | 200,000-1,000,000 | 60,000-300,000 | 3-5 yıl |
| Pinch tabanlı ısı entegrasyonu | 100,000-500,000 | 50,000-200,000 | 2-4 yıl |
| Buhar türbin jeneratör | 80,000-300,000 | 30,000-120,000 | 2-4 yıl |
| Merkezi soğutma sistemi yenileme | 150,000-500,000 | 40,000-150,000 | 3-5 yıl |
| Isı pompası entegrasyonu | 50,000-200,000 | 20,000-80,000 | 2-4 yıl |

## İlgili Dosyalar

- [Pinch Analizi](pinch_analysis.md) — Isı entegrasyonu ve HEN tasarımı
- [Exergy Temelleri](exergy_fundamentals.md) — Utility sistemi exergy hesapları
- [Ekonomik Analiz](economic_analysis.md) — Utility yatırım değerlendirmesi
- [Enerji Yönetimi](energy_management.md) — Utility izleme ve hedef belirleme
- [KPI Tanımları](kpi_definitions.md) — Utility performans göstergeleri
- [Yaşam Döngüsü Maliyet](life_cycle_cost.md) — Utility ekipmanları LCC analizi
- [Kazan Formülleri](../boiler/formulas.md) — Kazan hesaplamaları
- [Kazan Economizer](../boiler/solutions/economizer.md) — Baca gazı ısı geri kazanımı
- [Kazan Buhar Kapanı](../boiler/solutions/steam_trap.md) — Buhar kapanı analizi
- [Kompresör Benchmark](../compressor/benchmarks.md) — Basınçlı hava benchmark verileri
- [Kompresör Isı Geri Kazanımı](../compressor/solutions/heat_recovery.md) — Atık ısı kullanımı
- [Kompresör VSD](../compressor/solutions/vsd.md) — Değişken hız sürücüsü
- [Kompresör Kaçak](../compressor/solutions/air_leaks.md) — Kaçak tespit ve onarım
- [Chiller Benchmark](../chiller/benchmarks.md) — Soğutma sistemi performans verileri
- [Chiller Condenser](../chiller/solutions/condenser_optimization.md) — Condenser optimizasyonu

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1994
- Smith, R., "Chemical Process Design and Integration," Wiley, 2nd Edition, 2016
- US DOE, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition, 2012
- US DOE, "Improving Compressed Air System Performance: A Sourcebook for Industry," 2003
- ASHRAE Handbook — HVAC Systems and Equipment, 2020
- Saidur, R. et al. (2010), "A review on compressed-air energy use and energy savings," Renewable and Sustainable Energy Reviews, 14(4), 1135-1153
- Kemp, I.C., "Pinch Analysis and Process Integration," Butterworth-Heinemann, 2nd Edition, 2007
- Klemes, J.J. et al. (2013), "Total Site Heat Integration," Handbook of Process Integration, Woodhead Publishing
- European Commission, "Reference Document on Best Available Techniques for Energy Efficiency," 2009
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
