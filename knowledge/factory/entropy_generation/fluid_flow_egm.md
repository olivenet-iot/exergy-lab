---
title: "Akış Sistemlerinde EGM (Entropy Generation Minimization in Fluid Flow)"
category: factory
equipment_type: factory
keywords: [akış sürtünmesi, basınç düşüşü, S_gen_ΔP, Darcy-Weisbach, Reynolds, boru akışı, türbülans]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/bejan_number.md, factory/entropy_generation/pipe_flow_egm.md]
use_when: ["Akış kaynaklı entropi üretimi hesaplanacakken", "Boru sistemi optimizasyonu yapılacakken", "Sürtünme irreversibility analizi gerektiğinde"]
priority: high
last_updated: 2026-02-01
---

# Akış Sistemlerinde EGM (Entropy Generation Minimization in Fluid Flow)

> Son güncelleme: 2026-02-01

## Genel Bakış

Endüstriyel tesislerde akışkan taşıma sistemleri — borular, vanalar, bağlantı elemanları, pompalar — toplam enerji tüketiminin önemli bir kısmını oluşturur. Ancak enerji analizi bu sistemlerdeki gerçek termodinamik kayıpları ortaya koymakta yetersiz kalır. EGM (Entropy Generation Minimization) yaklaşımı, akış sistemlerindeki her basınç düşüşünü, her sürtünme kaybını ve her türbülans bölgesini entropi üretimi (S_gen) cinsinden ölçerek gerçek tersinmezlikleri (irreversibilities) nicelleştirir.

Bu dosya, akış sistemlerindeki entropi üretiminin fiziksel kaynaklarını, hesaplama yöntemlerini ve minimize etme stratejilerini kapsar.

---

## 1. Sürtünme Kaynaklı Entropi Üretimi (Friction-Induced Entropy Generation)

### 1.1 Temel Fizik

Bir boru içinde akan akışkan, boru duvarıyla ve kendi iç katmanlarıyla etkileşime girer. Bu etkileşimde organize kinetik enerji (akışkanın düzenli hareketi) düzensiz termal enerjiye (moleküler titreşimlere) dönüşür. Bu dönüşüm tek yönlüdür — termal enerjiyi geri organize kinetik enerjiye çeviremezsiniz. İşte tam da bu yüzden sürtünme saf bir tersinmezlik (pure irreversibility) kaynağıdır.

**Fiziksel sezgi:** Bir boru boyunca akan suyun basıncının düştüğünü düşünün. Bu basınç düşüşü, pompanın akışkana verdiği mekanik enerjinin bir kısmının sürtünme yoluyla ısıya dönüştüğünü gösterir. Bu ısı çevreye yayılır ve artık yararlı iş üretemez. Entropi üretimi, bu kayıp iş kapasitesinin tam ölçüsüdür.

**Temel İlke:** Bir akışkan sisteminde her ΔP (basınç düşüşü), kaçınılmaz olarak entropi üretir. Basınç düşüşü sıfır olmadığı sürece, entropi üretimi de sıfır olmaz.

#### Birinci ve İkinci Yasa'dan Türetim

Kararlı hal (steady-state) akışta, açık bir kontrol hacmi için birinci yasa (enerji dengesi):

```
ṁ × (h_giriş - h_çıkış) + Q̇ - Ẇ = 0
```

Burada adyabatik (Q̇ = 0) ve iş çıkışı olmayan (Ẇ = 0) bir boru segmenti için:

```
h_giriş ≈ h_çıkış  (sıkıştırılamaz akışkanlarda entalpi değişimi ihmal edilebilir)
```

İkinci yasa (entropi dengesi) ise:

```
Ṡ_gen = ṁ × (s_çıkış - s_giriş) - Q̇/T_sınır ≥ 0
```

**Fiziksel sezgi:** İkinci yasa bize der ki, akışkanın çıkıştaki entropisi girişe göre mutlaka artmıştır. Bu artışın kaynağı sürtünme kaynaklı tersinmezliktir.

Sıkıştırılamaz bir akışkan (incompressible fluid) için termodinamik ilişki:

```
T × ds = dh - (1/ρ) × dP
```

Adyabatik akışta dh ≈ 0 olduğundan:

```
T × ds = -(1/ρ) × dP
```

İşareti düzenleyerek (dP negatif, yani basınç düşüyor):

```
ds = -dP / (ρ × T)
```

Boru boyunca integre edersek ve kütlesel debi ile çarparsak:

```
Ṡ_gen_ΔP = ṁ × ΔP / (ρ × T)
```

**Bu nihai formül şunu söyler:** Entropi üretim hızı, kütlesel debinin ve basınç düşüşünün çarpımıyla doğru orantılı; yoğunluğun ve mutlak sıcaklığın çarpımıyla ters orantılıdır.

#### Değişkenlerin Açıklaması

| Sembol | Açıklama | Birim |
|--------|----------|-------|
| Ṡ_gen_ΔP | Basınç düşüşü kaynaklı entropi üretim hızı | kW/K |
| ṁ | Kütlesel debi (mass flow rate) | kg/s |
| ΔP | Basınç düşüşü (pressure drop) | Pa (veya kPa) |
| ρ | Akışkan yoğunluğu (density) | kg/m³ |
| T | Akışkanın mutlak sıcaklığı (absolute temperature) | K |

**Sayısal Örnek:**

Bir fabrikada DN100 boruda 10 kg/s su akıyor. Boru boyunca 50 kPa basınç düşüşü ölçülmüş.
Su sıcaklığı: 80°C = 353.15 K, ρ = 972 kg/m³.

```
Ṡ_gen_ΔP = ṁ × ΔP / (ρ × T)
Ṡ_gen_ΔP = 10 × 50,000 / (972 × 353.15)
Ṡ_gen_ΔP = 500,000 / 343,261.8
Ṡ_gen_ΔP = 1.457 W/K = 0.001457 kW/K
```

Kayıp iş potansiyeli (lost work rate):

```
Ẇ_kayıp = T₀ × Ṡ_gen = 298.15 × 0.001457 = 0.434 kW
```

Bu, pompanın 0.434 kW'lık iş kapasitesinin sürtünme nedeniyle geri dönüşsüz biçimde kaybedildiği anlamına gelir.

### 1.2 Entropi Üretiminin Fiziksel Kaynakları

Akış sistemlerinde entropi üretiminin birden fazla fiziksel kaynağı vardır. Her birini anlamak, doğru optimizasyon stratejisi geliştirmek için kritiktir.

#### 1.2.1 Duvar Kayma Gerilmesi (Wall Shear Stress)

**Fiziksel sezgi:** Boru duvarına temas eden akışkan katmanı sıfır hıza sahiptir (kaymama koşulu — no-slip condition). Duvardan uzaklaştıkça hız artar. Bu hız gradyanı, komşu katmanlar arasında kayma gerilmesi yaratır ve enerji sürtünmeyle ısıya dönüşür.

```
τ_duvar = f × ρ × v² / 8

Burada:
τ_duvar = duvar kayma gerilmesi [Pa]
f = Darcy sürtünme faktörü (friction factor) [-]
ρ = akışkan yoğunluğu [kg/m³]
v = ortalama akış hızı [m/s]
```

Duvar kayma gerilmesi, laminer akışta entropi üretiminin birincil kaynağıdır.

#### 1.2.2 Türbülanslı Girdaplar ve Disipasyon (Turbulent Eddies)

**Fiziksel sezgi:** Türbülanslı akışta, büyük girdaplar (eddies) enerjilerini giderek daha küçük girdaplara aktarır. En küçük girdaplar (Kolmogorov ölçeği) enerjilerini viskoz sürtünmeyle ısıya dönüştürür. Bu "enerji kaskadı" (energy cascade), türbülanslı akıştaki entropi üretiminin ana mekanizmasıdır.

Türbülanslı disipasyon oranı (turbulent dissipation rate):

```
ε ≈ v³/L_karakteristik

Burada:
ε = türbülanslı kinetik enerji disipasyon oranı [m²/s³]
v = ortalama akış hızı [m/s]
L = karakteristik uzunluk (boru çapı) [m]
```

#### 1.2.3 Akış Ayrılması (Flow Separation)

**Fiziksel sezgi:** Ani genişlemeler, keskin dirsekler veya vana daralmalarında akış boru duvarından ayrılır. Ayrılan bölgede yeniden dolaşım (recirculation) meydana gelir. Bu bölgeler yoğun türbülans ve enerji disipasyonu yaratır — yani yüksek entropi üretimi.

#### 1.2.4 Ani Daralma ve Genişleme (Sudden Contraction/Expansion)

Kesit alanının ani değiştiği noktalarda kinetik enerji ve basınç enerjisi arasında dengesiz dönüşümler olur. Bu dönüşümler tersinmez (irreversible) olduğundan önemli entropi üretir.

#### 1.2.5 Vanalar, Bağlantı Elemanları ve Dirsekler (Fittings)

Her vana, dirsek, T-bağlantı ve redüksiyon parçası akış yolunu bozar, yerel türbülans yaratır ve ek entropi üretir. Karmaşık boru tesisatlarında bu yerel kayıplar, düz boru sürtünme kayıplarını aşabilir.

---

## 2. Laminer vs Türbülanslı Akışta Entropi Üretimi

### 2.1 Laminer Akış (Re < 2300)

**Fiziksel sezgi:** Laminer akışta akışkan katmanları düzgün ve paralel hareket eder. Sürtünme yalnızca viskoz kayma (viscous shear) yoluyla gerçekleşir. Bu, nispeten düşük entropi üretimi demektir, ancak ısı transferi kabiliyeti de düşüktür.

Laminer akışta Hagen-Poiseuille denklemi geçerlidir:

```
ΔP = 128 × μ × L × Q / (π × D⁴)

Burada:
μ = dinamik viskozite [Pa·s]
L = boru uzunluğu [m]
Q = hacimsel debi [m³/s]
D = boru iç çapı [m]
```

Laminer akışta Darcy sürtünme faktörü:

```
f = 64 / Re

Burada:
Re = ρ × v × D / μ  (Reynolds sayısı)
```

**Fiziksel sezgi:** f = 64/Re ilişkisi bize der ki, laminer akışta sürtünme faktörü yalnızca Reynolds sayısına bağlıdır ve yüzey pürüzlülüğünden bağımsızdır. Akış hızı arttıkça Re artar ve f düşer, ancak ΔP yine de artar çünkü hız karesi etkisi baskın olur.

Laminer akışta birim uzunluk başına entropi üretimi:

```
Ṡ'_gen_laminer = ṁ × f × v² / (2 × D × T)
                = ṁ × (64/Re) × v² / (2 × D × T)
                = 32 × μ × ṁ × v / (ρ × D² × T)

Burada:
Ṡ'_gen_laminer = birim uzunluk başına entropi üretim hızı [W/(K·m)]
```

**Sayısal Örnek (Laminer):**

Yağlama yağı, DN25 boruda laminer olarak akıyor.
- ṁ = 0.5 kg/s, v = 1.0 m/s, μ = 0.1 Pa·s
- ρ = 880 kg/m³, D = 0.025 m, T = 333.15 K (60°C)
- Re = 880 × 1.0 × 0.025 / 0.1 = 220 (laminer)
- f = 64 / 220 = 0.291

```
Ṡ'_gen = 0.5 × 0.291 × 1.0² / (2 × 0.025 × 333.15)
Ṡ'_gen = 0.1455 / 16.658
Ṡ'_gen = 0.00873 W/(K·m)
```

100 m boru için: Ṡ_gen = 0.873 W/K → Ẇ_kayıp = 298.15 × 0.873 = 260.3 W

### 2.2 Türbülanslı Akış (Re > 4000)

**Fiziksel sezgi:** Türbülanslı akışta düzensiz hız dalgalanmaları, girdaplar ve karışma meydana gelir. Bu düzensizlik sürtünme kayıplarını önemli ölçüde artırır (yani daha fazla entropi üretir), ancak ısı transferi katsayısını da büyük ölçüde iyileştirir. Bu, endüstriyel sistemlerin temel ödünleşimidir (trade-off).

Türbülanslı akışta sürtünme faktörü, Colebrook-White denklemiyle hesaplanır:

```
1/√f = -2.0 × log₁₀(ε_r/(3.7 × D) + 2.51/(Re × √f))

Burada:
ε_r = yüzey pürüzlülüğü (surface roughness) [m]
     Çelik boru: ε_r ≈ 0.045 mm
     Bakır boru: ε_r ≈ 0.0015 mm
     Plastik boru: ε_r ≈ 0.0 mm (pürüzsüz)
```

Bu denklem iteratif çözüm gerektirir. Pratik yaklaşım olarak Swamee-Jain açık formülü:

```
f = 0.25 / [log₁₀(ε_r/(3.7 × D) + 5.74/Re⁰·⁹)]²
```

Türbülanslı akışta birim uzunluk başına entropi üretimi:

```
Ṡ'_gen_türbülans = ṁ × f × v² / (2 × D × T)
```

**Fiziksel sezgi:** Formül yapısı laminer ile aynıdır, ancak f değeri farklıdır. Türbülanslı akışta f, hem Re hem de ε_r/D'ye bağlıdır. Bu, yüzey pürüzlülüğünün entropi üretimini doğrudan etkilediği anlamına gelir.

**Sayısal Örnek (Türbülanslı):**

Soğutma suyu, DN100 çelik boruda akıyor.
- ṁ = 15 kg/s, v = 2.0 m/s, D = 0.1023 m
- ρ = 998 kg/m³, μ = 0.001 Pa·s, T = 298.15 K (25°C)
- ε_r = 0.045 mm = 0.000045 m
- Re = 998 × 2.0 × 0.1023 / 0.001 = 204,181 (türbülanslı)
- f (Swamee-Jain) ≈ 0.0185

```
Ṡ'_gen = 15 × 0.0185 × 2.0² / (2 × 0.1023 × 298.15)
Ṡ'_gen = 1.11 / 61.0
Ṡ'_gen = 0.01820 W/(K·m)
```

100 m boru için: Ṡ_gen = 1.82 W/K → Ẇ_kayıp = 298.15 × 1.82 = 542.6 W

#### Ödünleşim: Sürtünme Entropisi vs Isı Transferi Entropisi

**Fiziksel sezgi:** Bir ısı eşanjöründe veya ısıtmalı boruda iki entropi üretim mekanizması birbiriyle yarışır. Akış hızını artırmak sürtünme entropisini (S_gen_ΔP) artırır ama sıcaklık farkından kaynaklanan ısı transferi entropisini (S_gen_ΔT) azaltır (çünkü konveksiyon katsayısı h artar). EGM, bu iki mekanizmanın toplamını minimize eder.

```
Ṡ_gen_toplam = Ṡ_gen_ΔP + Ṡ_gen_ΔT

Minimum Ṡ_gen_toplam → Optimum akış koşulları
```

### 2.3 Optimum Reynolds Sayısı (Re_opt) Kavramı

**Fiziksel sezgi:** Çok düşük Reynolds sayısında akış laminerdir: sürtünme entropisi düşüktür ama ısı transferi kötüdür (yüksek ΔT entropisi). Reynolds sayısı arttıkça ısı transferi iyileşir (ΔT entropisi düşer) ama sürtünme entropisi yükselir. İkisinin toplamının minimum olduğu noktada optimum Reynolds sayısı bulunur.

Tipik türbülanslı akış koşullarında:

```
Re_opt ≈ 2 × 10⁵  (genel yaklaşık değer)
```

Bu değer koşullara göre değişir:

| Senaryo | Re_opt | Açıklama |
|---------|--------|----------|
| Isıtmalı su borusu | 1.5 × 10⁵ – 3 × 10⁵ | Isı transferi baskın |
| Soğutma suyu | 2 × 10⁵ – 4 × 10⁵ | Orta düzey ödünleşim |
| Basınçlı hava (ısı transfersiz) | Mümkün olan en düşük Re | Yalnızca sürtünme önemli |
| Buhar dağıtım hattı | 5 × 10⁵ – 1 × 10⁶ | Yüksek hız kabul edilebilir |
| Viskoz yağ ısıtması | 5 × 10⁴ – 1 × 10⁵ | Isı transferi çok kritik |
| Proses suyu (izothermal) | Düşük → iyi | Sadece ΔP entropisi var |

**Not:** Isı transferi olmayan saf akış sistemlerinde (örn. basınçlı hava dağıtımı) Re_opt kavramı S_gen_ΔT = 0 olduğundan geçersizdir; burada hedef sürtünme entropisini minimize etmektir.

---

## 3. Darcy-Weisbach ve Moody Entegrasyonu

### 3.1 Darcy-Weisbach Denklemi

**Fiziksel sezgi:** Darcy-Weisbach, bir boru boyunca basınç düşüşünü hesaplamanın en genel ve güvenilir yoludur. Denklem, sürtünme faktörü (f), boru geometrisi (L/D) ve kinetik enerji (ρv²/2) arasındaki ilişkiyi kurar.

```
ΔP = f × (L/D) × (ρ × v² / 2)

Burada:
ΔP = basınç düşüşü [Pa]
f = Darcy sürtünme faktörü [-]
L = boru uzunluğu [m]
D = boru iç çapı [m]
ρ = akışkan yoğunluğu [kg/m³]
v = ortalama akış hızı [m/s]
```

Bu denklemi S_gen formülüne yerleştirerek:

**Fiziksel sezgi:** Basınç düşüşünü entropi üretimine dönüştürmek, kaybedilen iş potansiyelini doğrudan ölçmemizi sağlar. Darcy-Weisbach'ı S_gen ile birleştirmek, boru tasarımını termodinamik optimizasyona taşır.

```
Ṡ_gen = ṁ × ΔP / (ρ × T)
      = ṁ × f × L × v² / (2 × D × T)

veya hacimsel debi Q cinsinden:
Ṡ_gen = (8 × f × L × ṁ × Q²) / (π² × D⁵ × T)
```

**Sayısal Örnek:**

DN150 çelik boru, L = 200 m, su akışı.
- ṁ = 25 kg/s, v = 1.5 m/s, D = 0.1508 m
- f = 0.018, T = 313.15 K (40°C)

```
Ṡ_gen = 25 × 0.018 × 200 × 1.5² / (2 × 0.1508 × 313.15)
Ṡ_gen = 202.5 / 94.44
Ṡ_gen = 2.145 W/K

Ẇ_kayıp = 298.15 × 2.145 = 639.5 W ≈ 0.64 kW
```

Yıllık kayıp (8000 saat çalışma): 0.64 × 8000 = 5,120 kWh/yıl

### 3.2 Moody Diyagramı ile EGM

**Fiziksel sezgi:** Moody diyagramı, sürtünme faktörünü Reynolds sayısı ve bağıl pürüzlülük (ε_r/D) cinsinden gösterir. EGM perspektifinden bakıldığında, Moody diyagramındaki her nokta farklı bir entropi üretim seviyesine karşılık gelir. Pürüzlü borular, aynı Reynolds sayısında daha yüksek f → daha yüksek S_gen üretir.

#### Pürüzlülüğün Entropi Üretimine Etkisi

| Boru Malzemesi | ε_r [mm] | ε_r/D (DN100) | f (Re=2×10⁵) | S_gen oranı (pürüzsüze göre) |
|----------------|----------|---------------|---------------|------------------------------|
| Çekme bakır | 0.0015 | 0.000015 | 0.0158 | 1.00 (referans) |
| Yeni çelik | 0.045 | 0.00044 | 0.0185 | 1.17 |
| Galvanize çelik | 0.15 | 0.0015 | 0.0220 | 1.39 |
| Dökme demir | 0.26 | 0.0025 | 0.0255 | 1.61 |
| Korozyonlu çelik | 1.0 | 0.0098 | 0.0380 | 2.41 |
| Beton | 1.5 | 0.0147 | 0.0445 | 2.82 |

**Sonuç:** Korozyonlu bir çelik boru, yeni bir çelik boruya göre %106 daha fazla sürtünme entropisi üretir. Boru bakımı ve iç yüzey temizliği, EGM açısından kritik öneme sahiptir.

---

## 4. Yerel Kayıplar ve Entropi Karşılığı (Minor Losses)

**Fiziksel sezgi:** "Yerel kayıplar" (minor losses) terimi yanıltıcıdır. Kısa boru hatlarında veya çok sayıda fitting içeren sistemlerde, yerel kayıplar düz boru sürtünme kayıplarını aşabilir. Her yerel kayıp, akış yolunun bozulması nedeniyle ek entropi üretir.

Genel yerel kayıp formülü:

```
ΔP_yerel = K × ρ × v² / 2

Burada K = kayıp katsayısı (loss coefficient) [-]
```

Buna karşılık gelen entropi üretimi:

```
Ṡ_gen_yerel = ṁ × K × v² / (2 × T)
```

### 4.1 Vana Kayıpları

**Fiziksel sezgi:** Vanalar akışı kontrol etmek için akış yolunu kasıtlı olarak daraltır. Bu daralma, kinetik enerji artışı ve ardından türbülanslı genişleme yaratır. Vana tipi ve açıklık derecesi, K değerini ve dolayısıyla entropi üretimini belirler. Kısma vanaları (throttling valves) %100 tersinmez olduğundan, EGM perspektifinden en kötü seçenektir.

| Vana Tipi | K (tam açık) | S_gen/S_gen_küresel | Açıklama |
|-----------|-------------|---------------------|----------|
| Küresel vana (ball valve) | 0.05 – 0.1 | 1.0 (referans) | En düşük kayıp |
| Kelebek vana (butterfly valve) | 0.2 – 0.5 | 3 – 5 × | Orta kayıp, kompakt |
| Sürgülü vana (gate valve) | 0.1 – 0.2 | 1.5 – 2 × | Düşük kayıp, tam açık/kapalı |
| Küresel gövdeli vana (globe valve) | 4.0 – 10.0 | 50 – 100 × | Çok yüksek kayıp |
| Çek vana (check valve) | 1.0 – 2.5 | 15 – 25 × | Geri akışı önler |
| Kısma vanası (throttle valve) | 2.0 – 20.0 | Değişken | Tam tersinmez kontrol |

**Kritik Uyarı:** Bir küresel gövdeli vana (globe valve), bir küresel vanaya (ball valve) göre 50-100 kat daha fazla entropi üretir. Vana seçimi, EGM'de büyük fark yaratır.

**Sayısal Örnek:**

DN100 hatta, v = 2.0 m/s su akışı, T = 303.15 K, ṁ = 16 kg/s.

Küresel vana (K = 0.08):
```
Ṡ_gen = 16 × 0.08 × 2.0² / (2 × 303.15) = 5.12 / 606.3 = 0.00845 W/K
```

Küresel gövdeli vana (K = 6.0):
```
Ṡ_gen = 16 × 6.0 × 2.0² / (2 × 303.15) = 384 / 606.3 = 0.6335 W/K
```

Fark: 0.6335 / 0.00845 = 75 kat!

### 4.2 Dirsek Kayıpları

**Fiziksel sezgi:** Dirsekler akış yönünü değiştirir. Yön değişimi sırasında dış duvardaki basınç artar, iç duvarda düşer. Bu basınç gradyanı sekonder akışlar (secondary flows) ve akış ayrılması yaratarak entropi üretir. Uzun yarıçaplı dirsekler, akış ayrılmasını azaltarak entropiyi düşürür.

| Dirsek Tipi | K | Eşdeğer Boru Uzunluğu (L_eq/D) | S_gen açıklaması |
|-------------|---|----------------------------------|------------------|
| 90° standart dirsek | 0.75 | 30 | Referans |
| 90° uzun yarıçaplı | 0.45 | 18 | %40 daha az S_gen |
| 45° standart dirsek | 0.35 | 14 | Kısa yön değişimi |
| 180° U-dirsek | 1.50 | 60 | Çok yüksek |
| 90° miter (köşeli) | 1.10 | 44 | Akış ayrılması şiddetli |

**Sayısal Karşılaştırma (v = 2.5 m/s, ṁ = 20 kg/s, T = 313.15 K):**

90° standart (K = 0.75):
```
Ṡ_gen = 20 × 0.75 × 2.5² / (2 × 313.15) = 93.75 / 626.3 = 0.1497 W/K
```

90° uzun yarıçaplı (K = 0.45):
```
Ṡ_gen = 20 × 0.45 × 2.5² / (2 × 313.15) = 56.25 / 626.3 = 0.0898 W/K
```

Tasarruf: 0.0599 W/K × 298.15 = 17.9 W/dirsek. 50 dirsekli bir tesisatta: 895 W = 0.895 kW.

### 4.3 Daralma ve Genişleme (Contraction and Expansion)

#### Ani Daralma (Sudden Contraction)

**Fiziksel sezgi:** Akışkan ani bir daralmaya geldiğinde, kesit alanı küçülür ve hız artar. Daralma noktasının hemen arkasında bir "vena contracta" (daralan jet) oluşur ve akış tekrar genişlerken enerji kaybeder. Bu, çekme-genişleme sürecindeki tersinmezliktir.

```
K_daralma = 0.5 × (1 - A₂/A₁)

Burada:
A₁ = büyük kesit alanı [m²]
A₂ = küçük kesit alanı [m²]
```

| A₂/A₁ | K_daralma | Entropi etkisi |
|--------|-----------|---------------|
| 0.8 | 0.10 | Düşük |
| 0.5 | 0.25 | Orta |
| 0.2 | 0.40 | Yüksek |
| 0.1 | 0.45 | Çok yüksek |

#### Ani Genişleme (Sudden Expansion) — Borda-Carnot Formülü

**Fiziksel sezgi:** Ani genişlemede akışkan, dar kesitten geniş kesine geçer. Hız düşer ve kinetik enerji basınç enerjisine dönüşmeye çalışır, ancak bu dönüşüm tamamen tersinmez değildir. Borda-Carnot formülü bu kaybı tam olarak ifade eder. Bu, akış mekaniğinde nadir bulunan tam analitik çözümlerden biridir.

```
K_genişleme = (1 - A₁/A₂)²

ΔP_kayıp = ρ × (v₁ - v₂)² / 2

Ṡ_gen = ṁ × (v₁ - v₂)² / (2 × T)
```

| A₁/A₂ | K_genişleme | v₁/v₂ oranı | Entropi etkisi |
|--------|------------|-------------|---------------|
| 0.8 | 0.04 | 1.25 | Düşük |
| 0.5 | 0.25 | 2.0 | Orta |
| 0.2 | 0.64 | 5.0 | Yüksek |
| 0.1 | 0.81 | 10.0 | Çok yüksek |

#### Kademeli vs Ani Geçiş: Entropi Tasarrufu

**Fiziksel sezgi:** Kademeli (gradual) daralma veya genişleme, akışa yeterli mesafe tanıyarak uyum sağlamasını sağlar. Bu, akış ayrılmasını önler veya azaltır ve entropi üretimini dramatik biçimde düşürür.

| Geçiş Tipi | K (tipik) | S_gen tasarrufu |
|------------|-----------|----------------|
| Ani daralma | 0.5 × (1 - A₂/A₁) | Referans |
| Kademeli daralma (θ ≤ 30°) | 0.05 – 0.10 | %70-90 |
| Ani genişleme | (1 - A₁/A₂)² | Referans |
| Kademeli genişleme (θ ≤ 7°) | 0.10 – 0.20 | %60-80 |
| Difüzör (θ ≈ 5-7°) | 0.05 – 0.15 | %75-90 |

### 4.4 T-bağlantılar ve Birleşme/Ayrılma (Tee Junctions)

**Fiziksel sezgi:** T-bağlantılarda iki akışın birleşmesi (mixing) veya tek akışın ikiye ayrılması (dividing) söz konusudur. Birleşme noktasında farklı hızdaki akışkanlar karışır ve bu karışma tersinmez bir süreçtir. Ayrılma noktasında ise akış yeniden dağılımı kayıplar yaratır.

| T-bağlantı Tipi | K (düz geçiş) | K (dal — branch) | Açıklama |
|-----------------|---------------|------------------|----------|
| Birleştirme (converging) | 0.5 – 1.0 | 1.0 – 1.5 | Karışma tersinmezliği |
| Ayırma (diverging) | 0.5 – 0.8 | 1.0 – 2.0 | Akış ayrılması |
| Yönlendirmeli T | 0.2 – 0.4 | 0.5 – 0.8 | Optimize edilmiş tasarım |

---

## 5. Endüstriyel Boru Sistemlerinde Tipik S_gen_ΔP Değerleri

**Fiziksel sezgi:** Aşağıdaki tablo, farklı endüstriyel akışkanlar ve boru boyutları için beklenen entropi üretim değerlerini sunar. Bu değerler, mevcut sisteminizi değerlendirmek ve iyileştirme potansiyelini belirlemek için bir referans noktası oluşturur.

### 5.1 Su Sistemleri

| Boru Çapı | v [m/s] | ṁ [kg/s] | Re | f | ΔP/m [Pa/m] | Ṡ_gen/m [W/(K·m)] | Ẇ_kayıp/m [W/m] |
|-----------|---------|----------|---------|-------|------------|-------------------|-----------------|
| DN50 | 1.0 | 2.0 | 51,000 | 0.021 | 108 | 7.2 × 10⁻⁴ | 0.215 |
| DN50 | 2.0 | 4.0 | 102,000 | 0.019 | 389 | 5.2 × 10⁻³ | 1.55 |
| DN100 | 1.5 | 12.0 | 153,000 | 0.018 | 198 | 7.9 × 10⁻³ | 2.36 |
| DN100 | 2.5 | 20.0 | 255,000 | 0.017 | 520 | 3.5 × 10⁻² | 10.4 |
| DN150 | 1.5 | 27.0 | 230,000 | 0.017 | 128 | 1.15 × 10⁻² | 3.43 |
| DN200 | 2.0 | 63.0 | 408,000 | 0.016 | 162 | 3.4 × 10⁻² | 10.1 |
| DN300 | 1.5 | 106.0 | 460,000 | 0.015 | 68 | 2.4 × 10⁻² | 7.16 |

Koşullar: Su, 25°C, çelik boru (ε_r = 0.045 mm)

### 5.2 Buhar Sistemleri

| Boru Çapı | P [bar] | v [m/s] | ṁ [kg/s] | ΔP/m [Pa/m] | Ṡ_gen/m [W/(K·m)] | Ẇ_kayıp/m [W/m] |
|-----------|---------|---------|----------|------------|-------------------|-----------------|
| DN80 | 10 | 20 | 1.5 | 520 | 1.7 × 10⁻³ | 0.51 |
| DN100 | 10 | 25 | 3.2 | 680 | 4.7 × 10⁻³ | 1.40 |
| DN150 | 10 | 30 | 8.5 | 550 | 1.0 × 10⁻² | 2.98 |
| DN100 | 4 | 25 | 1.3 | 310 | 2.0 × 10⁻³ | 0.60 |
| DN150 | 4 | 30 | 3.5 | 250 | 4.5 × 10⁻³ | 1.34 |

Koşullar: Doymuş buhar, çelik boru

### 5.3 Basınçlı Hava Sistemleri

| Boru Çapı | P [bar] | v [m/s] | ṁ [kg/s] | ΔP/m [Pa/m] | Ṡ_gen/m [W/(K·m)] | Ẇ_kayıp/m [W/m] |
|-----------|---------|---------|----------|------------|-------------------|-----------------|
| DN50 | 7 | 8 | 0.25 | 85 | 7.1 × 10⁻⁵ | 0.021 |
| DN50 | 7 | 15 | 0.47 | 280 | 4.4 × 10⁻⁴ | 0.131 |
| DN80 | 7 | 10 | 0.62 | 72 | 1.5 × 10⁻⁴ | 0.045 |
| DN100 | 7 | 8 | 0.82 | 35 | 9.6 × 10⁻⁵ | 0.029 |
| DN100 | 7 | 15 | 1.54 | 115 | 5.9 × 10⁻⁴ | 0.176 |

Koşullar: Basınçlı hava, 25°C, çelik boru

### 5.4 Glikol Sistemleri (Soğutma)

| Boru Çapı | Glikol [%] | v [m/s] | ṁ [kg/s] | Re | ΔP/m [Pa/m] | Ṡ_gen/m [W/(K·m)] |
|-----------|------------|---------|----------|--------|------------|-------------------|
| DN80 | 30 | 1.5 | 8.0 | 42,000 | 380 | 1.05 × 10⁻² |
| DN80 | 50 | 1.5 | 8.5 | 15,000 | 620 | 1.82 × 10⁻² |
| DN100 | 30 | 1.5 | 12.5 | 56,000 | 250 | 1.08 × 10⁻² |
| DN100 | 50 | 1.5 | 13.3 | 20,000 | 410 | 1.88 × 10⁻² |
| DN150 | 30 | 1.5 | 28.0 | 84,000 | 165 | 1.60 × 10⁻² |

Koşullar: Etilen glikol-su karışımı, -5°C ile 10°C arası, çelik boru

**Not:** Glikol konsantrasyonu arttıkça viskozite yükselir, Re düşer ve sürtünme faktörü artar. %50 glikol, %30 glikole göre yaklaşık %70-80 daha fazla entropi üretir.

---

## 6. Entropi Üretimini Azaltma Stratejileri

### 6.1 Boru Çapı Artırma (Pipe Upsizing)

**Fiziksel sezgi:** Boru çapını artırmak akış hızını düşürür. S_gen ∝ v² olduğundan, hız yarıya düşürüldüğünde entropi üretimi dörtte birine iner. Ancak azalan getiri (diminishing returns) vardır: büyük çaplı borular daha pahalıdır ve ek yalıtım gerektirir.

```
Çap artışının etkisi (sabit ṁ için):

v ∝ 1/D²  →  v² ∝ 1/D⁴

ΔP ∝ f × L × v² / D ∝ 1/D⁵ (türbülanslı akışta f ≈ sabit varsayımıyla)

Ṡ_gen ∝ ΔP/T ∝ 1/D⁵
```

| Mevcut Çap | Yeni Çap | Hız oranı | S_gen oranı | Yatırım artışı (tipik) |
|------------|----------|-----------|-------------|----------------------|
| DN50 | DN65 | 0.59 | 0.25 | %30-40 |
| DN80 | DN100 | 0.64 | 0.30 | %25-35 |
| DN100 | DN125 | 0.64 | 0.30 | %25-35 |
| DN100 | DN150 | 0.44 | 0.10 | %50-70 |
| DN150 | DN200 | 0.56 | 0.21 | %40-55 |

**Karar Kuralı:** Boru çapı artırma yatırımının geri dönüş süresi tipik olarak 2-5 yıldır. Yıllık pompa enerji tasarrufu > yıllık boru yatırım maliyeti amortismanı ise çap artırma ekonomiktir.

### 6.2 Akış Hızı Optimize Etme

**Fiziksel sezgi:** Her akışkan tipi için optimum hız aralıkları vardır. Çok düşük hız büyük boru çapı (yüksek yatırım) ve potansiyel çökelme sorunları yaratır. Çok yüksek hız aşırı sürtünme entropisi ve erozyon riski getirir.

| Akışkan | Optimum Hız Aralığı [m/s] | Maks. Kabul Edilebilir [m/s] | Gerekçe |
|---------|--------------------------|------------------------------|---------|
| Soğuk su (emiş) | 0.5 – 1.5 | 2.0 | Kavitasyon riski |
| Soğuk su (basma) | 1.0 – 2.5 | 3.0 | Erozyon sınırı |
| Sıcak su | 1.0 – 2.0 | 2.5 | Genleşme/darbe |
| Kızgın su (>100°C) | 1.5 – 3.0 | 4.0 | Yüksek enerji içeriği |
| Doymuş buhar | 15 – 25 | 35 | Yoğuşma/erozyon |
| Kızgın buhar | 20 – 40 | 60 | Isı stresi |
| Basınçlı hava | 6 – 8 | 15 | Gürültü/titreşim |
| Glikol (soğutma) | 1.0 – 2.0 | 2.5 | Yüksek viskozite |
| Termal yağ | 0.5 – 1.5 | 2.0 | Çok yüksek viskozite |
| Kondens | 0.5 – 1.0 | 1.5 | İki fazlı akış riski |

### 6.3 Fitting Sayısını Azaltma (Layout Optimization)

**Fiziksel sezgi:** Her fitting (dirsek, T-bağlantı, vana) ek entropi üretir. Boru tesisat düzenini (layout) optimize ederek fitting sayısını minimize etmek, düşük maliyetli ama yüksek etkili bir stratejidir.

Tipik tasarruf potansiyeli:

| Optimizasyon Aksiyonu | Azaltılan Fitting | Eşdeğer Boru Uzunluğu Tasarrufu | S_gen azalması |
|-----------------------|-------------------|--------------------------------|----------------|
| 2 gereksiz dirsek kaldırma | 2 × 90° dirsek | ~60D | %5-10 (kısa hatlarda) |
| Direkt bağlantı rotası | 3-4 dirsek | ~100-120D | %10-15 |
| Manifold yerine header | 5-6 T-bağlantı | ~200D | %15-25 |
| Gereksiz vana kaldırma | 1-2 globe vana | ~400-600D | %20-40 |

### 6.4 Vana Tipini Değiştirme

**Fiziksel sezgi:** Aynı işlevi gören ancak farklı entropi üreten vana tipleri vardır. Değiştirme genellikle düşük maliyetli ve yüksek getirili bir aksiyondur.

| Mevcut Vana | Alternatif | K azalması | S_gen tasarrufu | Yatırım |
|-------------|-----------|------------|----------------|---------|
| Globe vana → Ball vana | K: 6.0 → 0.08 | %98.7 | %98.7 | Düşük |
| Globe vana → Butterfly vana | K: 6.0 → 0.3 | %95.0 | %95.0 | Düşük |
| Swing check → Wafer check | K: 2.0 → 0.8 | %60.0 | %60.0 | Orta |
| Gate vana (kısma) → VSD pompa | K: değişken → 0 | %100 | %100 | Yüksek |

**En Önemli Kural:** Kısma vanasıyla (throttling valve) debi kontrolü yapılan her sistemde, vana tamamen kaldırılıp değişken hızlı sürücü (VSD — Variable Speed Drive) kullanılması en etkili EGM stratejisidir. Kısma vanası %100 tersinmezdir; VSD ise yalnızca motor kayıpları kadar entropi üretir.

---

## 7. Pratik Mühendislik Kuralları

### 7.1 Hız Kuralları

**Fiziksel sezgi:** Aşağıdaki pratik kurallar, yüzlerce endüstriyel uygulamadan elde edilen deneyime dayanır ve entropi üretimini kabul edilebilir seviyelerde tutan hız sınırlarını tanımlar.

- **Su:** 1 – 3 m/s (optimal: 1.5 – 2.0 m/s)
- **Buhar:** 15 – 25 m/s (doymuş), 20 – 40 m/s (kızgın)
- **Basınçlı hava:** 6 – 8 m/s (dağıtım hatları), 15 – 20 m/s (ana hatlar kısa mesafede)
- **Glikol:** 1.0 – 2.0 m/s

### 7.2 Eşdeğer Boru Uzunluğu Kuralı

**Fiziksel sezgi:** Her fitting, belirli bir düz boru uzunluğu kadar entropi üretir. Bu "eşdeğer boru uzunluğu" (equivalent pipe length) kavramı, karmaşık bir sistemin toplam entropi üretimini hızlıca tahmin etmek için kullanılır.

```
L_toplam = L_düz_boru + Σ (L_eq,i)

Burada L_eq = K × D / f  (her fitting için)
```

Yaygın yaklaşımlar:

| Eleman | Eşdeğer Uzunluk (L_eq/D) |
|--------|--------------------------|
| 90° standart dirsek | 30 |
| 90° uzun yarıçaplı dirsek | 18 |
| 45° dirsek | 14 |
| T-bağlantı (düz geçiş) | 20 |
| T-bağlantı (dal — branch) | 60 |
| Sürgülü vana (tam açık) | 8 |
| Küresel vana (tam açık) | 3 |
| Küresel gövdeli vana (tam açık) | 340 |
| Çek vana (swing) | 100 |
| Kelebek vana (tam açık) | 15 |

**Örnek:** DN100 (D = 0.102 m) hatta 5 adet 90° dirsek, 2 adet T-bağlantı (dal) ve 1 adet globe vana:

```
L_eq = (5 × 30 + 2 × 60 + 1 × 340) × 0.102
L_eq = (150 + 120 + 340) × 0.102
L_eq = 610 × 0.102
L_eq = 62.2 m eşdeğer boru uzunluğu
```

Bu, fittinglerden kaynaklanan entropi üretiminin 62.2 m düz boruya eşdeğer olduğu anlamına gelir. 100 m düz boru + 62.2 m eşdeğer = 162.2 m toplam eşdeğer uzunluk.

### 7.3 Kısma Vanası vs VSD Kuralı

**Fiziksel sezgi:** Kısma vanası, akışkanın enerjisini ısıya dönüştürerek debiyi azaltır — %100 tersinmez bir süreç. VSD (Variable Speed Drive) ise pompanın devrini düşürerek debiyi azaltır — çok daha verimli.

```
Kısma vanası ile kontrol:
  Ẇ_pompa = sabit (tam hızda çalışır)
  ΔP_vana = Ẇ_pompa × (1 - Q_istenen/Q_maks)  (basitleştirilmiş)
  Ṡ_gen_vana = ṁ × ΔP_vana / (ρ × T)

VSD ile kontrol:
  Ẇ_pompa ∝ (Q_istenen/Q_maks)³  (afinite yasaları)
  ΔP_vana = 0
  Ṡ_gen_vana = 0

Tasarruf oranı: Genellikle %30-60 enerji tasarrufu
```

**Altın Kural:** Endüstriyel bir tesiste kısma vanasıyla kontrol edilen her pompa sistemi, VSD'ye dönüştürme için adaydır. Geri ödeme süresi tipik olarak 1-3 yıldır.

### 7.4 Hızlı Kontrol Tablosu

| Parametre | İyi | Kabul Edilebilir | Kötü | Çok Kötü |
|-----------|------|------------------|------|----------|
| Su hızı [m/s] | < 1.5 | 1.5 – 2.5 | 2.5 – 3.5 | > 3.5 |
| Buhar hızı [m/s] | < 20 | 20 – 30 | 30 – 40 | > 40 |
| Hava hızı [m/s] | < 8 | 8 – 12 | 12 – 18 | > 18 |
| ΔP/L (su) [Pa/m] | < 100 | 100 – 300 | 300 – 500 | > 500 |
| ΔP/L (buhar) [Pa/m] | < 200 | 200 – 500 | 500 – 800 | > 800 |
| ΔP/L (hava) [Pa/m] | < 50 | 50 – 150 | 150 – 300 | > 300 |

---

## İlgili Dosyalar

- **[factory/entropy_generation/fundamentals.md](factory/entropy_generation/fundamentals.md):** Entropi üretimi temel kavramları ve genel EGM çerçevesi
- **[factory/entropy_generation/bejan_number.md](factory/entropy_generation/bejan_number.md):** Bejan sayısı — sürtünme vs ısı transferi entropi katkılarının oranı
- **[factory/entropy_generation/pipe_flow_egm.md](factory/entropy_generation/pipe_flow_egm.md):** Boru akışına özel detaylı EGM hesaplamaları
- **[factory/exergy_fundamentals.md](factory/exergy_fundamentals.md):** Fabrika seviyesi exergy analizi temelleri
- **[factory/waste_heat_recovery.md](factory/waste_heat_recovery.md):** Atık ısı geri kazanımı ve akış sistemi entegrasyonu
- **[factory/process_integration.md](factory/process_integration.md):** Proses entegrasyonu ve boru ağı optimizasyonu

---

## Referanslar

1. **Bejan, A.** (1996). *Entropy Generation Minimization*. CRC Press. — EGM alanının temel referans eseri.
2. **Bejan, A.** (1982). *Entropy Generation Through Heat and Fluid Flow*. Wiley. — Akış ve ısı transferinde entropi üretiminin ilk kapsamlı analizi.
3. **Çengel, Y.A. & Cimbala, J.M.** (2018). *Fluid Mechanics: Fundamentals and Applications*. McGraw-Hill. — Darcy-Weisbach, Moody diyagramı ve yerel kayıplar.
4. **White, F.M.** (2016). *Fluid Mechanics*. McGraw-Hill. — Boru akışı ve sürtünme faktörü hesaplamaları.
5. **Incropera, F.P. et al.** (2017). *Fundamentals of Heat and Mass Transfer*. Wiley. — Isı transferi ve akış entropi üretimi etkileşimi.
6. **Crane Co.** (2009). *Flow of Fluids Through Valves, Fittings, and Pipe* (Technical Paper No. 410). — Endüstriyel kayıp katsayıları referansı.
7. **ASHRAE Handbook — Fundamentals** (2021). — HVAC sistemlerinde boru boyutlandırma ve basınç düşüşü rehberi.
8. **ISO 5167** — Akış ölçüm cihazlarında basınç düşüşü standartları.
9. **Kotas, T.J.** (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Termal tesislerde exergy ve entropi analizi.
10. **Dinçer, I. & Rosen, M.A.** (2013). *Exergy: Energy, Environment and Sustainable Development*. Elsevier. — Exergy analizi ve sürdürülebilirlik bağlantısı.
