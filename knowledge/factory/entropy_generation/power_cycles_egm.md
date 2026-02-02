---
title: "Güç Çevrimlerinde EGM (Entropy Generation Minimization in Power Cycles)"
category: factory
equipment_type: factory
keywords: [güç çevrimi, Rankine, Brayton, kojenerasyon, türbin, entropi dağılımı, reheat, basınç oranı]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/finite_time_thermo.md, factory/cogeneration.md]
use_when: ["Güç çevrimi optimizasyonu yapılacakken", "Türbin ve kompresör entropi analizi gerektiğinde", "Kojenerasyon sistemi EGM değerlendirmesi yapılacakken"]
priority: medium
last_updated: 2026-02-01
---
# Güç Çevrimlerinde EGM (Entropy Generation Minimization in Power Cycles)

> Son güncelleme: 2026-02-01

## Genel Bakış

Güç çevrimleri (power cycles), ısıl enerjiyi mekanik işe dönüştüren termodinamik sistemlerdir. Her gerçek güç çevriminde, her bileşen kaçınılmaz olarak entropi üretir. EGM (Entropy Generation Minimization), toplam entropi üretimini sistematik olarak azaltarak çevrim performansını artırmayı hedefleyen termodinamik optimizasyon yaklaşımıdır. Bu dosya, Rankine, Brayton, kojenerasyon ve içten yanmalı çevrimlerdeki entropi üretim mekanizmalarını ve EGM tabanlı optimizasyon stratejilerini kapsar.

---

## 1. Güç Çevrimlerinde Entropi Üretimi — Genel Çerçeve

### 1.1 Temel Prensip

Herhangi bir güç çevriminde, termodinamiğin ikinci yasası gereği her bileşen geri dönüşümsüzlük (irreversibility) üretir. Bir çevrimin toplam entropi üretimi, tüm bileşenlerin bireysel entropi üretimlerinin toplamıdır.

**Fiziksel sezgi:** Her bileşenin kendine özgü bir geri dönüşümsüzlük mekanizması vardır — yanma kimyasal geri dönüşümsüzlük yaratır, ısı transferi sıcaklık farkından kaynaklanan geri dönüşümsüzlük yaratır, türbin ve pompa sürtünme kayıpları yaratır. Toplam entropi üretimini azaltmak için öncelikle en büyük kaynağı hedeflemek gerekir.

```
Ṡ_gen,toplam = Ṡ_gen,kazan + Ṡ_gen,türbin + Ṡ_gen,kondenser + Ṡ_gen,pompa + Ṡ_gen,boru/vana

Burada:
- Ṡ_gen,toplam = toplam entropi üretim hızı (kW/K)
- Her terim, ilgili bileşenin entropi üretim hızıdır (kW/K)
```

### 1.2 Kayıp İş ve Entropi Üretimi İlişkisi

**Fiziksel sezgi:** Üretilen her birim entropi, doğrudan kayıp iş potansiyeline karşılık gelir. Çevre sıcaklığı ne kadar yüksekse, aynı miktarda entropi üretiminin iş kaybı etkisi de o kadar büyüktür. Bu ilişki Gouy-Stodola teoremi ile ifade edilir.

```
Ẇ_kayıp = T₀ × Ṡ_gen,toplam

Burada:
- Ẇ_kayıp = tersinmezliklerden kaynaklanan kayıp iş gücü (kW)
- T₀ = çevre (ölü hal) sıcaklığı (K), tipik olarak 298.15 K (25 °C)
- Ṡ_gen,toplam = toplam entropi üretim hızı (kW/K)
```

**Sayısal örnek:**
- Ṡ_gen,toplam = 12.5 kW/K, T₀ = 300 K ise
- Ẇ_kayıp = 300 × 12.5 = 3750 kW kayıp iş potansiyeli

### 1.3 Bileşen Önceliklendirme Stratejisi

EGM yaklaşımında, en yüksek Ṡ_gen değerine sahip bileşen birincil optimizasyon hedefidir. Ancak dikkat edilmesi gereken nokta: bazı bileşenlerdeki iyileştirme diğer bileşenleri olumsuz etkileyebilir (trade-off). Sistem düzeyinde toplam Ṡ_gen minimizasyonu yapılmalıdır.

```
Optimizasyon önceliklendirme kuralı:
1. Ṡ_gen katkısı en büyük bileşeni belirle
2. Bu bileşendeki geri dönüşümsüzlük kaynağını tanımla
3. İyileştirmenin diğer bileşenlere etkisini değerlendir
4. Net Ṡ_gen azalmasını hesapla → pozitifse uygula
```

---

## 2. Rankine Çevrimi (Steam Power Cycle)

### 2.1 Bileşen Bazlı Entropi Üretimi

Rankine çevrimi, buhar güç santrallerinin temelini oluşturur. Dört ana bileşeni vardır ve her birinin entropi üretim karakteristiği farklıdır.

**Fiziksel sezgi:** Rankine çevriminde entropi üretiminin aslan payı kazan/buhar jeneratöründedir, çünkü yanma ve yüksek sıcaklık farkıyla ısı transferi en büyük geri dönüşümsüzlük kaynaklarıdır. Türbin ve kondenser daha az katkıda bulunur; pompa ise ihmal edilebilir düzeyde entropi üretir.

| Bileşen | Ṡ_gen Payı (%) | Ana Geri Dönüşümsüzlük Kaynağı | Tipik Değer Aralığı (kW/K) |
|---------|----------------|--------------------------------|---------------------------|
| Kazan — yanma (combustion) | 55 – 65 | Kimyasal geri dönüşümsüzlük (chemical irreversibility) | 8 – 25 |
| Kazan — ısı transferi (heat transfer) | 15 – 20 | Alev-buhar sıcaklık farkı (ΔT) | 3 – 8 |
| Türbin (turbine) | 8 – 12 | Sürtünme, kanat kayıpları, sızıntı | 1 – 4 |
| Kondenser (condenser) | 5 – 10 | Buhar-soğutma suyu sıcaklık farkı | 0.8 – 3 |
| Pompa (pump) | 1 – 2 | Sürtünme, sıkıştırılamaz akışkan | 0.1 – 0.5 |
| Boru ve vanalar (piping & valves) | 2 – 5 | Basınç düşüşü (pressure drop) | 0.3 – 1.5 |

### 2.2 Kazan / Buhar Jeneratörü (Boiler / Steam Generator)

#### 2.2.1 Yanma Geri Dönüşümsüzlüğü (Combustion Irreversibility)

**Fiziksel sezgi:** Yanma, yüksek kaliteli kimyasal enerjiyi (yakıt exergy'si) daha düşük kaliteli ısıl enerjiye dönüştürür. Bu dönüşüm doğası gereği geri dönüşümsüzdür ve yakıt exergy'sinin %25-30'u bu aşamada yok olur. Yanma sıcaklığı ne kadar yüksekse, entropi üretimi o kadar düşük olur — bu nedenle adyabatik alev sıcaklığına yakın yanma hedeflenir.

```
Ṡ_gen,yanma = ṁ_yakıt × (s_ürünler - s_reaktanlar) - Q̇_kayıp / T_sınır

Burada:
- ṁ_yakıt = yakıt kütle debisi (kg/s)
- s_ürünler = yanma ürünlerinin özgül entropisi (kJ/kg·K)
- s_reaktanlar = reaktanların özgül entropisi (kJ/kg·K)
- Q̇_kayıp = kazan cidarından kaçak ısı (kW)
- T_sınır = kaçak ısının geçtiği yüzeyin sıcaklığı (K)
```

Yanma geri dönüşümsüzlüğünü azaltma stratejileri:
- Hava/yakıt oranını optimize etme (fazla hava azaltma)
- Yanma havası ön ısıtma (air preheating) → alev sıcaklığını artırır
- Oksijen zenginleştirmeli yanma (oxygen-enriched combustion)

#### 2.2.2 Isı Transferi Geri Dönüşümsüzlüğü (Heat Transfer Irreversibility)

**Fiziksel sezgi:** Sıcak yanma gazlarından (1200–1800 °C) buhar/suya (200–550 °C) ısı transferi büyük sıcaklık farkıyla gerçekleşir. Bu fark ne kadar büyükse, entropi üretimi o kadar fazladır. Ekonomizer ve hava ön ısıtıcı gibi ekipmanlar, sıcak gazların enerjisini daha düşük ΔT ile geri kazanarak toplam Ṡ_gen'i azaltır.

```
Ṡ_gen,ısı_transferi = Q̇ × (1/T_soğuk - 1/T_sıcak)

Burada:
- Q̇ = transfer edilen ısı gücü (kW)
- T_soğuk = ısıyı alan akışkanın ortalama termodinamik sıcaklığı (K)
- T_sıcak = ısıyı veren akışkanın ortalama termodinamik sıcaklığı (K)

Not: T_soğuk < T_sıcak olduğundan (1/T_soğuk > 1/T_sıcak) ve Ṡ_gen her zaman ≥ 0'dır.
```

**Pratik iyileştirmeler:**
- Ekonomizer (economizer): Baca gazıyla besleme suyunu ön ısıtma → ΔT azalır
- Hava ön ısıtıcı (air preheater): Baca gazıyla yanma havasını ısıtma
- Süperısıtıcı (superheater): Buhar sıcaklığını artırarak ΔT azaltma
- Her 20 °C'lik baca gazı sıcaklığı düşürme ≈ %1 kazan verimi artışı

### 2.3 Buhar Türbini (Steam Turbine)

**Fiziksel sezgi:** İdeal (isentropik) bir türbinde buhar genişlerken entropisi sabit kalır. Gerçek türbinde ise kanat sürtünmesi, nozul kayıpları, buhar sızıntısı ve yaş buhar damlacık etkisi entropi üretir. Bu üretilen entropi, türbinin isentropik verimden sapma derecesini gösterir.

```
Ṡ_gen,türbin = ṁ × (s_çıkış - s_giriş)

Burada:
- ṁ = buhar kütle debisi (kg/s)
- s_çıkış = türbin çıkışında özgül entropi (kJ/kg·K)
- s_giriş = türbin girişinde özgül entropi (kJ/kg·K)

(Adyabatik türbin varsayımı altında — dış ısı transferi ihmal)
```

Türbin isentropik verimi ile entropi üretimi ilişkisi:

```
η_is,türbin = (h_giriş - h_çıkış) / (h_giriş - h_çıkış,s)

Burada:
- h_giriş = türbin giriş entalpisi (kJ/kg)
- h_çıkış = gerçek türbin çıkış entalpisi (kJ/kg)
- h_çıkış,s = isentropik türbin çıkış entalpisi (kJ/kg)

Tipik değerler:
- Büyük buhar türbinleri: η_is = %85 – 92
- Küçük endüstriyel türbinler: η_is = %75 – 85
- Ṡ_gen katkısı: Toplam çevrim Ṡ_gen'in %8 – 12'si
```

Türbin geri dönüşümsüzlük kaynakları ve payları:
- Kanat profili kayıpları (blade profile losses): %35 – 45
- İkincil akış kayıpları (secondary flow losses): %20 – 30
- Sızıntı kayıpları (leakage losses): %10 – 20
- Yaş buhar damlacık kayıpları (moisture losses): %5 – 15
- Mekanik kayıplar (mechanical losses): %3 – 5

### 2.4 Kondenser (Condenser)

**Fiziksel sezgi:** Kondenserde, düşük basınçlı buhar yoğuşarak ısısını soğutma suyuna (veya havaya) aktarır. Buhar ve soğutma suyu arasındaki sonlu sıcaklık farkı (finite ΔT) entropi üretir. Daha düşük kondenser basıncı çevrim verimini artırır ancak yoğuşma sıcaklığı ile çevre sıcaklığı arasındaki farkı azaltarak daha büyük kondenser yüzey alanı gerektirir.

```
Ṡ_gen,kondenser = Q̇_kondenser × (1/T_soğutma_su,ort - 1/T_yoğuşma)

Burada:
- Q̇_kondenser = kondenserde atılan ısı gücü (kW)
- T_soğutma_su,ort = soğutma suyunun ortalama sıcaklığı (K)
- T_yoğuşma = buharın yoğuşma sıcaklığı (K)

Tipik değerler:
- T_yoğuşma ≈ 35 – 50 °C (kondenser basıncı 0.05 – 0.12 bar)
- Soğutma suyu giriş: 20 – 30 °C, çıkış: 30 – 40 °C
- Optimum terminal sıcaklık farkı (TTD): 3 – 5 °C
```

**Optimum kondenser basıncı seçimi:**
- Daha düşük P_kondenser → daha yüksek çevrim verimi (daha fazla iş)
- Daha düşük P_kondenser → daha büyük kondenser yüzey alanı (maliyet artar)
- Daha düşük P_kondenser → daha yüksek yaş buhar oranı (türbin hasarı riski)
- EGM optimumu: Toplam Ṡ_gen (kondenser + türbin yaşlık kaybı) minimize edilir

### 2.5 Pompa (Pump)

**Fiziksel sezgi:** Pompa sıkıştırılamaz sıvıyı (condensate/feed water) basınçlandırır. Sıvı sıkıştırmak gazı sıkıştırmaya kıyasla çok az iş gerektirir, bu nedenle pompadaki entropi üretimi çevrim toplamının %1-2'si gibi çok küçük bir paydır. Yine de yüksek debili büyük sistemlerde mutlak değer olarak dikkate alınmalıdır.

```
Ṡ_gen,pompa = ṁ × (s_çıkış - s_giriş)

Burada:
- ṁ = besleme suyu kütle debisi (kg/s)
- s_çıkış = pompa çıkışında özgül entropi (kJ/kg·K)
- s_giriş = pompa girişinde özgül entropi (kJ/kg·K)

Tipik değerler:
- η_is,pompa = %75 – 88
- Ṡ_gen katkısı: Toplam çevrim Ṡ_gen'in %1 – 2'si
- Pompa işi / türbin işi oranı (back work ratio): %1 – 3
```

### 2.6 Rankine Çevrimi Sayısal Örnek

Tipik 100 MW buhar güç santrali (T_buhar = 540 °C, P_buhar = 100 bar, P_kondenser = 0.08 bar):

```
Bileşen              | Ṡ_gen (kW/K) | Pay (%)  | Ẇ_kayıp (kW) [T₀=300K]
---------------------|-------------|---------|------------------------
Kazan (yanma)        | 14.2        | 57.3    | 4260
Kazan (ısı transferi)| 4.5         | 18.1    | 1350
Türbin               | 2.8         | 11.3    | 840
Kondenser            | 1.9         | 7.7     | 570
Pompa                | 0.3         | 1.2     | 90
Boru/vana            | 1.1         | 4.4     | 330
---------------------|-------------|---------|------------------------
TOPLAM               | 24.8        | 100.0   | 7440

Çevrim exergy verimi: Ψ_çevrim ≈ %38 – 42
Toplam kayıp iş: Ẇ_kayıp = 7440 kW
```

---

## 3. Brayton Çevrimi (Gas Turbine Cycle)

### 3.1 Kompresör Entropi Üretimi (Compressor Entropy Generation)

**Fiziksel sezgi:** Brayton çevrimindeki kompresör, Rankine çevrimindeki pompanın aksine sıkıştırılabilir gazı (hava) yüksek basınca çıkarır. Bu işlem çok daha fazla iş gerektirir ve dolayısıyla çok daha fazla entropi üretir. Kompresör, Brayton çevriminde türbinin ürettiği işin %40-60'ını tüketir (yüksek back work ratio).

```
Ṡ_gen,kompresör = ṁ × [c_p × ln(T_çıkış/T_giriş) - R × ln(P_çıkış/P_giriş)]

Burada:
- ṁ = hava kütle debisi (kg/s)
- c_p = havanın sabit basınçta özgül ısısı ≈ 1.005 kJ/kg·K
- R = havanın gaz sabiti ≈ 0.287 kJ/kg·K
- T_giriş, T_çıkış = kompresör giriş ve çıkış sıcaklıkları (K)
- P_giriş, P_çıkış = kompresör giriş ve çıkış basınçları (bar)

İdeal (isentropik) durumda Ṡ_gen = 0, yani:
c_p × ln(T_çıkış,s/T_giriş) = R × ln(P_çıkış/P_giriş)
```

Kompresör isentropik verimi:

```
η_is,kompresör = (h_çıkış,s - h_giriş) / (h_çıkış - h_giriş)
               = (T_çıkış,s - T_giriş) / (T_çıkış - T_giriş)   [ideal gaz varsayımı]

Tipik değerler:
- Endüstriyel gaz türbini kompresörleri: η_is = %85 – 90
- Havacılık türbin kompresörleri: η_is = %88 – 92
- Ṡ_gen katkısı: Toplam çevrim Ṡ_gen'in %15 – 25'i
```

### 3.2 Yanma Odası (Combustion Chamber)

**Fiziksel sezgi:** Brayton çevriminin yanma odası, Rankine çevriminin kazanı gibi en büyük entropi kaynağıdır. Yakıtın kimyasal exergy'si, yüksek sıcaklıklı gaz ısıl exergy'sine dönüştürülür. Bu dönüşümde kimyasal geri dönüşümsüzlük kaçınılmazdır. Ek olarak, stokiyometrik oranın çok üzerinde hava ile seyreltme (dilution) ek geri dönüşümsüzlük yaratır.

```
Ṡ_gen,yanma_odası = (ṁ_hava + ṁ_yakıt) × s_ürünler - ṁ_hava × s_hava_giriş - ṁ_yakıt × s_yakıt

Kimyasal geri dönüşümsüzlük bileşenleri:
1. Yanma reaksiyonu geri dönüşümsüzlüğü: Ṡ_gen,kimyasal
2. Seyreltme geri dönüşümsüzlüğü: Ṡ_gen,seyreltme (fazla hava karışımı)
3. Isı kaybı: Ṡ_gen,kayıp (cidar ısı kaçağı)

Ṡ_gen,yanma_odası = Ṡ_gen,kimyasal + Ṡ_gen,seyreltme + Ṡ_gen,kayıp

Tipik dağılım:
- Kimyasal: %70 – 80
- Seyreltme: %15 – 25
- Isı kaybı: %2 – 5
```

Yanma odası basınç kaybı da ek entropi üretir:

```
Ṡ_gen,basınç_kaybı ≈ ṁ × R × (ΔP/P_giriş)

Tipik ΔP/P_giriş = %3 – 5 (basınç düşüşü)
```

### 3.3 Gaz Türbini (Gas Turbine)

**Fiziksel sezgi:** Gaz türbini, buhar türbiniyle benzer mekanizmalarla entropi üretir ancak çok daha yüksek sıcaklıklarda (1200–1600 °C türbin giriş sıcaklığı — TIT) çalışır. Bu yüksek sıcaklık, kanat soğutma gerektirir ve soğutma havası karışımı ek geri dönüşümsüzlük kaynağı olur.

```
Ṡ_gen,gaz_türbin = ṁ × (s_çıkış - s_giriş)   [adyabatik türbin]

Soğutmalı türbinde ek terim:
Ṡ_gen,soğutma = ṁ_soğutma × (s_karışım_sonrası - s_soğutma_havası)

Tipik değerler:
- η_is,gaz_türbin = %87 – 93
- TIT (Turbine Inlet Temperature): 1200 – 1600 °C
- Soğutma havası oranı: Toplam hava debisinin %15 – 25'i
- Ṡ_gen katkısı: Toplam çevrim Ṡ_gen'in %8 – 15'i
```

### 3.4 Optimum Basınç Oranı (Optimal Pressure Ratio)

**Fiziksel sezgi:** Brayton çevriminde basınç oranı (r_p = P_çıkış/P_giriş) çevrimin en kritik tasarım parametresidir. Düşük r_p'de çevrim verimi düşüktür, yüksek r_p'de kompresör çıkış sıcaklığı artar ve yanma odasına eklenen ısı azalır. Önemli EGM bulgusu: **Maksimum verim için optimum basınç oranı ile maksimum güç için optimum basınç oranı farklıdır.** Bu ayrım, mühendislik tasarımında kritik bir karar noktasıdır.

```
İdeal Brayton çevrimi verimi:
η_Brayton = 1 - 1 / r_p^((γ-1)/γ)

Burada:
- r_p = basınç oranı (P₂/P₁)
- γ = özgül ısı oranı (hava için ≈ 1.4)

Maksimum verim: r_p → ∞ (pratik sınır: malzeme dayanımı, kompresör kademesi)

Maksimum güç çıkışı için optimum basınç oranı:
r_p,opt_güç = (T_max / T_min)^(γ/(2(γ-1)))

Burada:
- T_max = türbin giriş sıcaklığı — TIT (K)
- T_min = kompresör giriş sıcaklığı (K)

Örnek: T_max = 1500 K, T_min = 300 K, γ = 1.4
r_p,opt_güç = (1500/300)^(1.4/(2×0.4)) = 5^1.75 ≈ 16.7

Minimum Ṡ_gen için optimum basınç oranı:
r_p,opt_EGM, gerçek bileşen verimleriyle birlikte çözülmelidir:
- η_is,kompresör ve η_is,türbin dahil edildiğinde
- r_p,opt_EGM < r_p,opt_güç (genellikle)
- Tipik endüstriyel gaz türbinleri: r_p = 10 – 35
```

### 3.5 Brayton Çevrimi Ṡ_gen Dağılımı

```
Bileşen              | Ṡ_gen Payı (%) | Ana Kaynak
---------------------|----------------|---------------------------
Yanma odası          | 55 – 70        | Kimyasal geri dönüşümsüzlük
Kompresör            | 15 – 25        | Sıkıştırma geri dönüşümsüzlüğü
Gaz türbini          | 8 – 15         | Genişleme geri dönüşümsüzlüğü
Egzoz (atık ısı)     | 5 – 15         | Çevreye ısı atma
Mekanik kayıplar     | 1 – 3          | Yatak sürtünmesi
```

---

## 4. Kojenerasyon (CHP) Sistemlerinde EGM

### 4.1 CHP'nin Termodinamik Avantajı (Thermodynamic Advantage of CHP)

**Fiziksel sezgi:** Konvansiyonel bir güç santralinde, kondenserde atılan ısı büyük miktarda exergy kaybına neden olur. CHP sistemi bu atık ısıyı endüstriyel proseslere veya bina ısıtmasına yönlendirerek, aslında çevreye atılacak olan entropiyi "faydalı" hale getirir. CHP, ayrı elektrik ve ısı üretimine kıyasla toplam entropi üretimini önemli ölçüde azaltır.

```
Ayrı üretimde toplam Ṡ_gen:
Ṡ_gen,ayrı = Ṡ_gen,santral + Ṡ_gen,kazan

CHP'de toplam Ṡ_gen:
Ṡ_gen,CHP = Ṡ_gen,CHP_sistemi

Tasarruf:
ΔṠ_gen = Ṡ_gen,ayrı - Ṡ_gen,CHP > 0 (her zaman pozitif)

CHP ile Ṡ_gen azalma oranı: tipik olarak %30 – 50
```

### 4.2 Karşı Basınçlı vs Çekme Türbin Karşılaştırması

**Fiziksel sezgi:** Karşı basınçlı türbin (back-pressure turbine), buharın tamamını proses basıncında çıkarır ve kondensere ihtiyaç duymaz — böylece kondenser Ṡ_gen'i tamamen elimine edilir. Çekme türbin (extraction turbine) ise buharın bir kısmını proses için çeker, kalanını daha düşük basınca genişleterek ek güç üretir. Her birinin EGM açısından avantajı farklıdır.

```
Karşı basınçlı türbin (back-pressure):
- Ṡ_gen,kondenser = 0 (kondenser yok)
- Tüm atık ısı faydalı kullanılır
- Elektrik/ısı oranı sabit ve düşük (0.1 – 0.3)
- Ṡ_gen,toplam daha düşük AMA esneklik az

Çekme türbin (extraction):
- Ṡ_gen,kondenser > 0 (kondenser var)
- Elektrik/ısı oranı ayarlanabilir (0.3 – 0.8)
- Ṡ_gen,toplam daha yüksek AMA operasyonel esneklik fazla
- Kısmi yüklerde karşı basınçlıdan daha verimli olabilir
```

### 4.3 Optimum Buhar Çıkış Basıncı (Optimal Extraction Pressure)

**Fiziksel sezgi:** Çıkış basıncı yükseldikçe proses için daha yüksek kaliteli ısı elde edilir ancak türbinde daha az genişleme olur (daha az güç). Çıkış basıncı düştükçe daha fazla güç üretilir ancak proses ısısının sıcaklığı (ve dolayısıyla exergy'si) düşer. EGM optimumu, bu iki etkinin dengelendiği noktadadır.

```
Optimizasyon problemi:
min Ṡ_gen,toplam(P_çıkış)
    = Ṡ_gen,kazan + Ṡ_gen,türbin(P_çıkış) + Ṡ_gen,kondenser(P_çıkış) + Ṡ_gen,proses_ısıtıcı(P_çıkış)

Kısıtlar:
- Q̇_proses = sabit (proses ısı talebi karşılanmalı)
- T_proses ≥ T_proses,min (minimum proses sıcaklığı)
- Ẇ_net ≥ Ẇ_talep (elektrik talebi karşılanmalı)

Tipik optimum çıkış basıncı:
- Düşük sıcaklık prosesi (60 – 100 °C): P_çıkış = 1.5 – 3 bar
- Orta sıcaklık prosesi (120 – 180 °C): P_çıkış = 3 – 10 bar
- Yüksek sıcaklık prosesi (200 – 300 °C): P_çıkış = 15 – 40 bar
```

### 4.4 Endüstriyel CHP Örneği — EGM Analizi

**Senaryo:** Bir kağıt fabrikası, 15 MW elektrik ve 25 MW proses buharı (150 °C, 5 bar) talebi olan bir CHP sistemi tasarlamaktadır.

```
Sistem parametreleri:
- Yakıt: Doğalgaz, LHV = 42000 kJ/kg
- Kazan buhar koşulları: 480 °C, 60 bar
- Proses buharı: 150 °C, 5 bar
- Çevre sıcaklığı: T₀ = 298 K (25 °C)
- Yakıt debisi: ṁ_yakıt = 2.1 kg/s
- Buhar debisi: ṁ_buhar = 22 kg/s

Bileşen bazlı Ṡ_gen analizi:
Bileşen              | Ṡ_gen (kW/K) | Ẇ_kayıp (kW) | Pay (%)
---------------------|-------------|-------------|--------
Kazan (yanma)        | 28.5        | 8493        | 58.2
Kazan (ısı transferi)| 8.2         | 2444        | 16.7
Türbin               | 4.1         | 1222        | 8.4
Proses ısı değiştirici| 3.8        | 1133        | 7.8
Boru/vana            | 2.5         | 745         | 5.1
Pompa + diğer        | 1.8         | 537         | 3.8
---------------------|-------------|-------------|--------
TOPLAM               | 48.9        | 14574       | 100.0

CHP exergy verimi: Ψ_CHP ≈ %42
Ayrı üretimde toplam Ṡ_gen ≈ 72 kW/K olurdu
CHP ile Ṡ_gen tasarrufu: 72 - 48.9 = 23.1 kW/K (%32 azalma)
```

---

## 5. Optimum Reheat Sıcaklığı (Optimal Reheat Temperature)

### 5.1 Reheat'in Entropi Etkisi (Entropy Effect of Reheat)

**Fiziksel sezgi:** Reheat (ara kızdırma), buharı türbinin yüksek basınç kademesinden çıktıktan sonra tekrar kazana göndererek yeniden ısıtmayı ifade eder. Bu işlem iki temel fayda sağlar: (1) türbin çıkışındaki buhar kalitesini artırır (yaş buhar azalır → türbinde sürtünme ve erozyon kayıpları düşer → Ṡ_gen,türbin azalır), (2) çevrime ısı eklendiği ortalama sıcaklık yükselir (Carnot verimi artar). Ancak yeniden ısıtıcıdaki (reheater) ısı transferi de kendi geri dönüşümsüzlüğünü yaratır. Net etki genellikle olumludur.

```
Reheat olmadan:
- Ṡ_gen,türbin = ṁ × (s_çıkış - s_giriş)   [tek kademeli genişleme]
- Türbin çıkışında yaşlık (moisture): x = %8 – 14

Reheat ile:
- Ṡ_gen,HP_türbin + Ṡ_gen,LP_türbin < Ṡ_gen,tek_kademe   (genellikle)
- Türbin çıkışında yaşlık: x = %3 – 8 (azalma)
- Ek entropi üretimi: Ṡ_gen,reheater (ısı transferi)

Net Ṡ_gen değişimi:
ΔṠ_gen,reheat = (Ṡ_gen,HP + Ṡ_gen,LP + Ṡ_gen,reheater) - Ṡ_gen,tek_kademe

Tipik olarak ΔṠ_gen,reheat < 0 → Reheat toplam Ṡ_gen'i azaltır
Tipik Ṡ_gen azalma oranı: %5 – 8
```

### 5.2 Optimum Reheat Basıncı (Optimal Reheat Pressure)

**Fiziksel sezgi:** Reheat basıncı çok yüksekse, yüksek basınç türbininde yeterli genişleme olmaz ve reheat'in faydası azalır. Çok düşükse, reheat sonrası buharın sıcaklığı yeterince yükselemez. Optimum reheat basıncı, genellikle başlangıç kazan basıncının %20-25'i civarındadır.

```
Optimum reheat basıncı:
P_reheat,opt ≈ (0.20 – 0.25) × P_kazan

Örnek:
- P_kazan = 100 bar → P_reheat,opt ≈ 20 – 25 bar
- P_kazan = 160 bar → P_reheat,opt ≈ 32 – 40 bar

EGM tabanlı optimizasyon:
min Ṡ_gen,toplam(P_reheat)
    = Ṡ_gen,kazan + Ṡ_gen,HP_türbin(P_reheat) + Ṡ_gen,reheater(P_reheat)
      + Ṡ_gen,LP_türbin(P_reheat) + Ṡ_gen,kondenser

Not: Çift reheat (double reheat) sistemlerinde:
- P_reheat1 ≈ %40 × P_kazan
- P_reheat2 ≈ %10 × P_kazan
- Ek Ṡ_gen azalması: %2 – 4 (tek reheat'e kıyasla)
```

### 5.3 Reheat ile Verimlilik Kazanımı Tablosu

```
Konfigürasyon       | η_çevrim (%) | Ṡ_gen,toplam (kW/K) | Yaşlık (%)
---------------------|-------------|---------------------|----------
Basit Rankine        | 36.2        | 24.8                | 12.5
Tek reheat           | 38.8        | 23.1                | 7.2
Çift reheat          | 39.5        | 22.4                | 5.1
```

---

## 6. Diesel ve Diğer İçten Yanmalı Çevrimler (Internal Combustion Cycles)

### 6.1 Otto Çevrimi (Spark Ignition)

**Fiziksel sezgi:** Otto çevriminde sıkıştırma oranı (r) arttıkça verim artar, ancak çok yüksek sıkıştırma oranlarında vuruntu (knock) oluşur ve bu da ek geri dönüşümsüzlük kaynağıdır. EGM, vuruntu sınırı dahilinde optimum sıkıştırma oranını belirler.

```
İdeal Otto çevrimi verimi:
η_Otto = 1 - 1 / r^(γ-1)

Burada:
- r = sıkıştırma oranı (V_max / V_min)
- γ = özgül ısı oranı ≈ 1.35 (yanma gazları)

EGM yaklaşımı ile Ṡ_gen:
Ṡ_gen,Otto = ṁ × c_v × [ln(T₃/T₂) - ln(T₃/T₂)_ideal] + Ṡ_gen,yanma

Tipik sıkıştırma oranları:
- Benzinli motor: r = 8 – 13
- Vuruntu sınırlı optimum: r ≈ 10 – 12 (oktan sayısına bağlı)
```

### 6.2 Diesel Çevrimi (Compression Ignition)

**Fiziksel sezgi:** Diesel çevrimi, Otto çevrimine kıyasla daha yüksek sıkıştırma oranlarında çalışabilir (vuruntu sorunu yok) ve bu nedenle daha yüksek termal verime ulaşabilir. Ancak yakıt enjeksiyonu ve difüzyon yanması ek geri dönüşümsüzlük kaynağıdır.

```
İdeal Diesel çevrimi verimi:
η_Diesel = 1 - (1/r^(γ-1)) × [(r_c^γ - 1) / (γ × (r_c - 1))]

Burada:
- r = sıkıştırma oranı (tipik: 14 – 25)
- r_c = kesme oranı (cut-off ratio) = V₃/V₂
- γ = özgül ısı oranı

Diesel'de Ṡ_gen dağılımı:
- Yanma: %60 – 70 (difüzyon yanması geri dönüşümsüzlüğü dahil)
- Isı transferi (silindir duvarlarına): %15 – 20
- Genişleme kayıpları: %5 – 10
- Egzoz: %5 – 10
- Mekanik sürtünme: %3 – 5
```

### 6.3 İçten Yanmalı Çevrimlerde EGM Optimizasyonu

```
Genel optimizasyon parametreleri:
1. Sıkıştırma oranı: ↑ r → ↓ Ṡ_gen (belirli sınıra kadar)
2. Yakıt/hava oranı: Stokiyometrik değere yakın → ↓ Ṡ_gen,yanma
3. Yanma zamanlaması: Optimum ateşleme/enjeksiyon zamanı → ↓ Ṡ_gen
4. Egzoz gaz geri dönüşümü (EGR): NOx azaltır ama Ṡ_gen artabilir
5. Turboşarj: Atık egzoz exergy'sini geri kazanır → ↓ Ṡ_gen,toplam
```

---

## 7. Pratik Mühendislik Kuralları (Practical Engineering Rules)

### 7.1 Genel EGM İlkeleri — Güç Çevrimleri

1. **Yanma her zaman en büyük Ṡ_gen kaynağıdır.** Kazan veya yanma odası tabanlı her sistemde, yanma geri dönüşümsüzlüğü toplam Ṡ_gen'in %55-70'ini oluşturur. Yakıt türünü değiştirmeden bu oranı dramatik olarak azaltmak mümkün değildir.

2. **Türbin isentropik veriminde %1'lik iyileşme:**
   - Özgül Ṡ_gen ≈ %0.8 – 1.2 azalır
   - 100 MW santralde ≈ 80 – 120 kW ek güç
   - Yıllık enerji tasarrufu ≈ 600 – 900 MWh

3. **Reheat uygulaması:**
   - Toplam Ṡ_gen'i %5 – 8 azaltır
   - Çevrim verimini 2 – 3 puan artırır
   - Ekonomik fizibilite: Genellikle ≥ 50 MW kapasitede

4. **CHP dönüşümü:**
   - Toplam Ṡ_gen'i %30 – 50 azaltabilir (ayrı üretime kıyasla)
   - Enerji kullanım oranı (energy utilization factor): %75 – 90
   - Exergy verimi: %35 – 50

5. **Kondenser optimizasyonu:**
   - Her 1 °C'lik TTD (terminal temperature difference) azalması ≈ %0.3 – 0.5 verim artışı
   - Ancak kondenser yüzey alanı maliyeti ile dengelenmeli

### 7.2 Hızlı Karşılaştırma Tablosu

```
Çevrim Tipi            | Tipik η_termal (%) | Tipik Ψ_exergy (%) | Ana Ṡ_gen Kaynağı
-----------------------|--------------------|--------------------|-------------------
Basit Rankine          | 33 – 38           | 35 – 40            | Kazan yanması
Reheat Rankine         | 36 – 42           | 38 – 44            | Kazan yanması
Superkritik Rankine    | 40 – 47           | 42 – 48            | Kazan yanması
Basit Brayton          | 28 – 35           | 30 – 37            | Yanma odası
Rejenratif Brayton     | 35 – 42           | 37 – 44            | Yanma odası
Kombine çevrim (CCGT)  | 55 – 63           | 52 – 58            | Yanma odası
Diesel                 | 35 – 45           | 33 – 42            | Yanma
Otto (benzinli)        | 25 – 35           | 24 – 32            | Yanma
CHP (gaz türbini)      | 75 – 88 (EUF)     | 40 – 52            | Yanma odası
CHP (buhar türbini)    | 80 – 90 (EUF)     | 35 – 48            | Kazan yanması
```

### 7.3 EGM Tabanlı Tasarım Kontrol Listesi

Güç çevrimi tasarımı veya optimizasyonunda kullanılacak EGM kontrol listesi:

```
[ ] Bileşen bazlı Ṡ_gen dağılımı hesaplandı mı?
[ ] En büyük Ṡ_gen kaynağı belirlendi mi?
[ ] Yanma parametreleri (hava/yakıt oranı, ön ısıtma) optimize edildi mi?
[ ] Türbin isentropik verimi hedef değerde mi (≥ %88)?
[ ] Kompresör isentropik verimi hedef değerde mi (≥ %86)?
[ ] Kondenser basıncı/sıcaklığı optimize edildi mi?
[ ] Reheat uygulanması değerlendirildi mi (≥ 50 MW için)?
[ ] Rejenrasyon (feed water heating / recuperator) değerlendirildi mi?
[ ] CHP potansiyeli analiz edildi mi (ısı talebi varsa)?
[ ] Boru/vana basınç düşüşleri minimize edildi mi?
[ ] Toplam Ẇ_kayıp = T₀ × Ṡ_gen,toplam hesaplandı mı?
[ ] Sonuçlar sektörel benchmark ile karşılaştırıldı mı?
```

---

## İlgili Dosyalar

- `factory/entropy_generation/fundamentals.md` — Entropi üretim temelleri ve Gouy-Stodola teoremi
- `factory/entropy_generation/finite_time_thermo.md` — Sonlu zamanlı termodinamik ve optimum güç çıkışı
- `factory/cogeneration.md` — Kojenerasyon sistemleri detaylı analiz
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanım yöntemleri
- `factory/cross_equipment.md` — Ekipmanlar arası entegrasyon fırsatları
- `factory/exergy_fundamentals.md` — Exergy analizi temel kavramları

## Referanslar

1. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press — EGM metodolojisinin temel kaynağı
2. Bejan, A. (2006). *Advanced Engineering Thermodynamics*, 3rd Ed. Wiley — Güç çevrimleri entropi analizi
3. Moran, M.J., Shapiro, H.N. (2014). *Fundamentals of Engineering Thermodynamics*, 8th Ed. Wiley — Rankine ve Brayton çevrim temelleri
4. Dincer, I., Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Ed. Elsevier — Exergy analizi ve güç çevrimleri
5. Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*. Krieger — Endüstriyel ısıl tesis exergy analizi
6. Ibrahim, D., Al-Muslim, H. (2001). "Thermodynamic analysis of reheat cycle steam power plants." *International Journal of Energy Research*, 25(8), 727-739
7. Rosen, M.A., Dincer, I. (2003). "Thermoeconomic analysis of power plants: an application to a coal-fired electrical generating station." *Energy Conversion and Management*, 44(17), 2743-2761
8. Regulagadda, P., Dincer, I., Naterer, G.F. (2010). "Exergy analysis of a thermal power plant with measured boiler and turbine losses." *Applied Thermal Engineering*, 30(8-9), 970-976
