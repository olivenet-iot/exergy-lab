---
title: "Boru Akışı Optimizasyonu — EGM (Pipe Flow Optimization via EGM)"
category: factory
equipment_type: factory
keywords: [boru akışı, optimum çap, D_opt, pompalama maliyeti, sürtünme, boru boyutlandırma]
related_files: [factory/entropy_generation/fluid_flow_egm.md, factory/entropy_generation/fundamentals.md, pump/formulas.md, pump/solutions/system_optimization.md]
use_when: ["Boru çapı optimizasyonu yapılacakken", "Pompalama sistemi EGM analizi gerektiğinde", "Boru boyutlandırma kararı verilecekken"]
priority: medium
last_updated: 2026-02-01
---

# Boru Akışı Optimizasyonu — EGM (Pipe Flow Optimization via EGM)

> Son güncelleme: 2026-02-01

## Genel Bakış

Endüstriyel tesislerde boru sistemleri, toplam enerji tüketiminin %15-30'unu oluşturan pompalama enerjisinin doğrudan belirleyicisidir. Geleneksel boru boyutlandırma yöntemleri genellikle hız limitlerine veya basınç düşüşü tablolarına dayanır. Entropi Üretiminin Minimizasyonu (Entropy Generation Minimization — EGM) yaklaşımı ise termodinamiğin ikinci yasasını kullanarak boru çapının gerçek optimumunu belirler. Bu dosya, Bejan'ın boru akışı EGM formülasyonunu, optimum çap türetmesini ve endüstriyel uygulamaya dönüştürme adımlarını kapsar.

---

## 1. Boru Akışında Entropi Üretimi (Entropy Generation in Pipe Flow)

### 1.1 İki Bileşenli S_gen

Bir borudan akan akışkan iki temel tersinmezlik (irreversibility) kaynağıyla karşılaşır:

1. **Sürtünme (Friction):** Akışkanın boru duvarı ve kendi içindeki viskoz kesme gerilmeleri, mekanik enerjiyi ısıya dönüştürür. Bu, basınç düşüşü olarak gözlenir.
2. **Isı Transferi (Heat Transfer):** Boru duvarı ile akışkan arasındaki sıcaklık farkı üzerinden gerçekleşen ısı geçişi, sonlu sıcaklık farkından dolayı entropi üretir.

Her iki bileşen toplanarak toplam entropi üretim hızı elde edilir:

**Fiziksel sezgi:** Bir boru hem akışkanı taşıyarak sürtünmeye, hem de çevreyle ısı alışverişi yaparak sıcaklık farkı kaynaklı tersinmezliğe maruz kalır. Bu iki mekanizma birbirinden bağımsız olarak entropi üretir ve toplam termodinamik kayıp bunların toplamıdır.

```
Ṡ_gen = Ṡ_gen,sürtünme + Ṡ_gen,ısı transferi
```

Bejan'ın boru akışı için türettiği genel formül (Bejan's pipe flow entropy generation formula):

```
         32 × ṁ³ × f × L          q"² × π × D × L
Ṡ_gen = ────────────────────── + ──────────────────────
         π² × D⁵ × ρ² × T        k × T² × Nu
```

Burada:
- ṁ : kütle debisi (kg/s)
- f : Darcy sürtünme faktörü (dimensionless)
- L : boru uzunluğu (m)
- D : boru iç çapı (m)
- ρ : akışkan yoğunluğu (kg/m³)
- T : akışkan mutlak sıcaklığı (K)
- q" : birim alan başına ısı akısı (W/m²)
- k : akışkan ısıl iletkenliği (W/(m×K))
- Nu : Nusselt sayısı (dimensionless)

**Birinci terim — Sürtünme kaynaklı entropi üretimi:**

**Fiziksel sezgi:** Akışkan boruda ilerlerken, akış hızının karesiyle orantılı bir basınç düşüşü yaşar. Bu basınç düşüşü, akışkanın mekanik exergisinin sürtünme ısısına dönüşmesidir. Küçük çapta hız artar, sürtünme katlanarak büyür — bu nedenle birinci terim D⁵ ile ters orantılıdır (çap küçüldükçe sürtünme entropi üretimi çok hızlı artar).

Türetme adımları:

```
Adım 1: Basınç düşüşü (Darcy-Weisbach)
  ΔP = f × (L/D) × (ρ × v²/2)

Adım 2: Ortalama hız — debi ilişkisi
  v = ṁ / (ρ × A) = 4 × ṁ / (π × D² × ρ)

Adım 3: ΔP'yi ṁ cinsinden yaz
  ΔP = f × L × 8 × ṁ² / (π² × D⁵ × ρ)

Adım 4: Sürtünme kaynaklı entropi üretim hızı
  İzotermik bir boruda sürtünme kaynaklı entropi üretim hızı:
  Ṡ_gen,sürtünme = ṁ × ΔP / (ρ × T)

Adım 5: Birleştir
  Ṡ_gen,sürtünme = ṁ × [f × L × 8 × ṁ²/(π² × D⁵ × ρ)] / (ρ × T)
                 = 8 × f × L × ṁ³ / (π² × D⁵ × ρ² × T)

Not: Bazı kaynaklarda Fanning sürtünme faktörü (f_F = f/4) kullanılır.
Darcy faktörü (f) ile: katsayı 8; Fanning ile: katsayı 32.
Yukarıdaki Bejan formülünde 32 katsayısı Fanning konvansiyonunu yansıtır.
```

**İkinci terim — Isı transferi kaynaklı entropi üretimi:**

**Fiziksel sezgi:** Isı transferi her zaman sıcaklık farkı gerektirir. Bu fark ne kadar büyükse, entropi üretimi o kadar fazladır. Nusselt sayısı (Nu) arttıkça ısı transferi katsayısı iyileşir, sıcaklık farkı azalır ve entropi üretimi düşer. Boru çapı büyüdükçe ısı transfer yüzey alanı artar, dolayısıyla aynı toplam ısı akısı daha geniş alana yayılarak birim alan başına ısı akısı azalır.

```
Adım 1: Duvar-akışkan sıcaklık farkı
  ΔT = q" / h    (h = konveksiyon katsayısı)

Adım 2: h ve Nu ilişkisi
  Nu = h × D / k  →  h = Nu × k / D

Adım 3: Isı transferi kaynaklı birim uzunluk başına entropi üretimi
  Ṡ'_gen,ısı = q"² × π × D / (k × T² × Nu)

Adım 4: Toplam boru uzunluğu için
  Ṡ_gen,ısı = q"² × π × D × L / (k × T² × Nu)
```

### 1.2 İzotermik Akış — Yalnızca Sürtünme (No Heat Transfer Case)

Endüstriyel tesislerdeki birçok boru hattı yalıtılmıştır veya çevre sıcaklığına yakın akışkan taşır. Bu durumlarda ısı transferi ihmal edilebilir (q" ≈ 0) ve yalnızca sürtünme bileşeni kalır.

**Fiziksel sezgi:** Yalıtılmış bir boruda tüm termodinamik kayıp, akışkanın basınç düşüşünden kaynaklanır. Pompa bu basınç düşüşünü karşılamak için enerji harcar. Entropi üretimi doğrudan pompalama gücü ihtiyacıyla orantılıdır — dolayısıyla Ṡ_gen'i minimize etmek, pompalama maliyetini minimize etmekle özdeştir.

```
Ṡ_gen = ṁ × ΔP / (ρ × T)

ΔP'yi açık yazarsak:
Ṡ_gen = ṁ × f × L × v² / (2 × D × T)

veya kütle debisi cinsinden:
Ṡ_gen = 8 × f × L × ṁ³ / (π² × D⁵ × ρ² × T)
```

Bu formülün pratik anlamı:
- D iki katına çıkarsa → Ṡ_gen, 2⁵ = 32 kat azalır (sabit ṁ için)
- ṁ iki katına çıkarsa → Ṡ_gen, 2³ = 8 kat artar
- Boru çapının entropi üretimine etkisi, debi etkisinden çok daha güçlüdür

Bu, birçok endüstriyel boru sistemi için baskın durumdur. Soğuk su dağıtım hatları, basınçlı hava hatları ve yalıtılmış buhar hatlarında ısı transferi bileşeni küçüktür.

---

## 2. Optimum Boru Çapı (Optimal Pipe Diameter)

### 2.1 D_opt Türetmesi (Derivation of Optimal Diameter)

**Fiziksel sezgi:** Boru çapını artırmak sürtünme entropi üretimini azaltır (hız düşer, sürtünme azalır). Ancak aynı zamanda ısı transferi entropi üretimini artırır (yüzey alanı büyür). Bu iki karşıt etki bir optimum noktada dengelenir. EGM, bu dengenin tam olarak nerede olduğunu matematiksel olarak belirler.

Toplam Ṡ_gen'i D'ye göre türev alıp sıfıra eşitleyelim:

```
         32 × ṁ³ × f × L          q"² × π × D × L
Ṡ_gen = ────────────────────── + ──────────────────────
         π² × D⁵ × ρ² × T        k × T² × Nu

dṠ_gen/dD = 0 alalım:

Adım 1: Her terimi D'ye göre türevle

  d/dD [32 × ṁ³ × f × L / (π² × D⁵ × ρ² × T)]
  = -5 × 32 × ṁ³ × f × L / (π² × D⁶ × ρ² × T)
  = -160 × ṁ³ × f × L / (π² × D⁶ × ρ² × T)

  d/dD [q"² × π × D × L / (k × T² × Nu)]
  = q"² × π × L / (k × T² × Nu)

Adım 2: Sıfıra eşitle

  -160 × ṁ³ × f × L / (π² × D⁶ × ρ² × T) + q"² × π × L / (k × T² × Nu) = 0

Adım 3: D⁶ için çöz

  D⁶ = 160 × ṁ³ × f × k × T² × Nu / (π³ × ρ² × T × q"² × Nu)

  Sadeleştirme:
  D⁶ = 160 × ṁ³ × f × k × T / (π³ × ρ² × q"²)  ← (Nu sadeleşir dikkat!)

  Düzeltme — Nu sadeleşmez, tekrar yazalım:
  D⁶ = 160 × ṁ³ × f × k × T × Nu / (π³ × ρ² × q"²)

Adım 4: D_opt

  D_opt = [160 × ṁ³ × f × k × T × Nu / (π³ × ρ² × q"²)]^(1/6)
```

Bejan'ın sonucu orantı olarak:

```
D_opt ∝ (ṁ³ × f × k × T × Nu / (ρ² × q"²))^(1/6)
```

veya boyutsuz yazılırsa:

```
D_opt ∝ (ṁ × f / Nu)^(1/6)   — Bejan'ın oransal sonucu
```

> **Önemli:** Bu oransal sonuç, f ve Nu'nun D'ye bağımlılığının ihmal edildiği basitleştirilmiş durumu gösterir. Tam çözüm iterasyon gerektirir.

### 2.2 Pratik D_opt Hesaplama Adımları

Gerçek mühendislik uygulamalarında D_opt'u bulmak iteratif bir süreçtir:

**Fiziksel sezgi:** Sürtünme faktörü (f) ve Nusselt sayısı (Nu) boru çapına bağlıdır, çünkü Reynolds sayısı çap ile değişir. Bu nedenle doğrudan analitik çözüm yerine yakınsama (convergence) yöntemi kullanılır.

```
Adım 1: Başlangıç verilerini belirle
  - Kütle debisi: ṁ (kg/s)
  - Akışkan özellikleri: ρ (kg/m³), μ (Pa×s), k (W/(m×K)), c_p (J/(kg×K))
  - Boru uzunluğu: L (m)
  - Isı akısı: q" (W/m²) — yalıtılmış borularda q" = 0
  - Akışkan sıcaklığı: T (K)

Adım 2: Başlangıç D tahmini yap
  İlk tahmin: D₀ = (4 × ṁ / (π × ρ × v_hedef))^(0.5)
  v_hedef = akışkan türüne göre tipik hız (bkz. Bölüm 4)

Adım 3: Reynolds sayısını hesapla
  Re = 4 × ṁ / (π × D × μ)

Adım 4: Sürtünme faktörünü hesapla
  Colebrook-White (türbülanslı akış için):
  1/√f = -2 × log₁₀(ε/(3.7×D) + 2.51/(Re×√f))

  veya açık yaklaşım (Swamee-Jain):
  f = 0.25 / [log₁₀(ε/(3.7×D) + 5.74/Re^0.9)]²

Adım 5: Nusselt sayısını hesapla (ısı transferi varsa)
  Dittus-Boelter: Nu = 0.023 × Re^0.8 × Pr^0.4
  Pr = μ × c_p / k

Adım 6: D_opt formülüne yerleştir
  D_opt_yeni = [160 × ṁ³ × f × k × T × Nu / (π³ × ρ² × q"²)]^(1/6)

  İzotermik durumda (q" = 0): Optimum, yalnızca sürtünme minimizasyonu
  ile belirlenir — ekonomik optimizasyona geçilir (Bölüm 3).

Adım 7: Yakınsamayı kontrol et
  |D_opt_yeni - D| / D < 0.01 ise → yakınsadı
  Değilse → D = D_opt_yeni ile Adım 3'e dön

Adım 8: En yakın standart boru çapını seç
  D_opt'a en yakın DN boyutunu belirle
```

### 2.3 Standart Boru Çaplarıyla Karşılaştırma

**Fiziksel sezgi:** Hesaplanan D_opt hemen hemen hiçbir zaman standart boru çapına denk gelmez. Bu durumda bir üst veya bir alt standart çapın entropi üretimi hesaplanarak karşılaştırılmalıdır. Entropi üretimi D⁵ ile ters orantılı olduğundan, bir alt çapa inmek bir üst çapa çıkmaktan çok daha fazla cezaya neden olur.

| Senaryo | Boru Çapı | Ṡ_gen (W/K) | Pompa Gücü (kW) | Not |
|---------|-----------|-------------|------------------|-----|
| Bir alt standart | DN80 (iç çap: 80.1 mm) | 0.0485 | 4.82 | %62 fazla Ṡ_gen |
| **D_opt hesaplanan** | **95.3 mm** | **0.0300** | **2.98** | **Referans** |
| Bir üst standart | DN100 (iç çap: 105.3 mm) | 0.0265 | 2.12 | %12 az Ṡ_gen |
| İki üst standart | DN125 (iç çap: 130.7 mm) | 0.0195 | 1.10 | %35 az Ṡ_gen |

> **Karar kuralı:** D_opt iki standart çap arasında kaldığında:
> - Bir alt çaptaki Ṡ_gen artışı > %30 ise → kesinlikle üst çapı seç
> - Bir alt çaptaki Ṡ_gen artışı %10-30 arası ise → ekonomik analiz yap
> - Bir alt çaptaki Ṡ_gen artışı < %10 ise → alt çap kabul edilebilir

**Asimetri kuralı:** Çap küçültmenin Ṡ_gen cezası, çap büyütmenin Ṡ_gen kazancından her zaman daha büyüktür. Bu nedenle tereddüt durumunda bir üst çapı seçmek termodinamik olarak daha güvenlidir.

---

## 3. Ekonomik Optimizasyon — Üçlü Trade-off

### 3.1 Boru Maliyeti vs Pompalama Maliyeti vs Entropi Bedeli

**Fiziksel sezgi:** Mühendislik tasarımı her zaman bir denge (trade-off) arar. Büyük çaplı boru daha az sürtünme ve daha az pompalama enerjisi demektir — ama daha pahalıdır. Küçük çaplı boru daha ucuzdur ama ömür boyu pompalama maliyeti çok yüksek olabilir. EGM bu dengeye bir de exergy yıkımının ekonomik değerini ekler.

```
Büyük boru (D ↑):
  + Düşük sürtünme → düşük pompalama maliyeti
  + Düşük Ṡ_gen → düşük exergy yıkımı
  - Yüksek boru yatırım maliyeti
  - Daha fazla yalıtım maliyeti (büyük yüzey alanı)

Küçük boru (D ↓):
  + Düşük boru yatırım maliyeti
  + Daha az yalıtım maliyeti
  - Yüksek sürtünme → yüksek pompalama maliyeti
  - Yüksek Ṡ_gen → yüksek exergy yıkımı
  - Erozyon ve gürültü riski
```

### 3.2 Toplam Maliyet Minimizasyonu (Total Cost Minimization)

**Fiziksel sezgi:** Toplam sahip olma maliyeti (Total Cost of Ownership), boru yatırımı ve işletme maliyetlerinin toplamıdır. Yatırım maliyeti D ile artar, pompalama maliyeti D ile azalır. Bu iki eğrinin kesişim noktası (veya minimum toplam maliyet noktası) ekonomik optimum çapı verir.

```
C_toplam(D) = C_boru(D) + C_pompa(D) + C_exergy(D)

Her bileşen:

1. Boru maliyeti (yıllık amortisman):
   C_boru = a × L × c₁ × D^n₁
   Burada:
   - a = amortisman faktörü (CRF = i×(1+i)^n / ((1+i)^n - 1))
   - c₁ = birim uzunluk, birim çap başına boru maliyeti (TL/(m×m^n₁))
   - n₁ ≈ 1.0-1.5 (çelik borular için tipik üs)

2. Pompalama maliyeti (yıllık):
   C_pompa = (ṁ × ΔP / (ρ × η_pompa)) × t_çalışma × c_elektrik
   ΔP = f × (L/D) × (ρ × v²/2) = 8 × f × L × ṁ² / (π² × D⁵ × ρ)

   C_pompa = [8 × f × L × ṁ³ / (π² × D⁵ × ρ² × η_pompa)] × t_çalışma × c_elektrik

3. Exergy yıkım maliyeti (yıllık):
   C_exergy = T₀ × Ṡ_gen × t_çalışma × c_exergy
   c_exergy = exergy birim maliyeti (TL/kWh) — genellikle elektrik fiyatına yakın
```

Toplam maliyeti D'ye göre türev alıp sıfıra eşitleyelim:

```
dC_toplam/dD = 0

d/dD [a × L × c₁ × D^n₁] + d/dD [8 × f × L × ṁ³ × t × c_e / (π² × D⁵ × ρ² × η)] + ... = 0

a × L × c₁ × n₁ × D^(n₁-1) - 5 × 8 × f × L × ṁ³ × t × c_e / (π² × D⁶ × ρ² × η) = 0

D^(n₁+5) = 40 × f × ṁ³ × t × c_e / (π² × ρ² × η × a × c₁ × n₁)

D_opt,ekonomik = [40 × f × ṁ³ × t × c_e / (π² × ρ² × η × a × c₁ × n₁)]^(1/(n₁+5))
```

### 3.3 Ekonomik vs Termodinamik Optimum (Economic vs Thermodynamic Optimum)

**Fiziksel sezgi:** Termodinamik optimum yalnızca entropi üretimini minimize eder — maliyeti göz ardı eder. Ekonomik optimum ise termodinamik kaybın parasal değerini, boru yatırımı ile tartır. Çoğu durumda ekonomik optimum, termodinamik optimumdan biraz daha küçük bir çap verir, çünkü boru yatırım maliyeti somut ve anlıktır, oysa exergy yıkımı genellikle "görünmez" bir kayıptır.

```
Karşılaştırma:

D_opt,termodinamik ≥ D_opt,ekonomik  (hemen hemen her zaman)

Fark nedenleri:
1. Boru yatırım maliyeti somut → mühendisler küçük çapa yönelir
2. Exergy yıkım maliyeti genellikle hesaplanmaz → göz ardı edilir
3. Pompa enerji maliyeti kısmen hesaplanır ama tam değil

Pratik sonuç:
- Enerji fiyatları düşükken: D_opt,ekonomik << D_opt,termodinamik
- Enerji fiyatları yüksekken: D_opt,ekonomik → D_opt,termodinamik
- Karbon vergisi eklendiğinde: D_opt,ekonomik daha da büyür
```

> **Endüstriyel gerçek:** Türkiye'de 2024-2026 enerji fiyat artışlarıyla birlikte, ekonomik optimum çap termodinamik optimuma her zamankinden daha yakın hale gelmiştir. EGM analizi artık "akademik alıştırma" değil, gerçek tasarruf aracıdır.

---

## 4. Farklı Akışkanlar İçin Optimum Hız Aralıkları

**Fiziksel sezgi:** Her akışkanın yoğunluğu, viskozitesi ve kullanım koşulları farklıdır. Yoğun akışkanlarda (su) düşük hızlar yeterlidir, düşük yoğunluklu akışkanlarda (buhar, hava) daha yüksek hızlar gerekir. EGM optimum hızları, geleneksel "pratik kural" hızlarına genellikle yakın düşer — bu, mühendislik deneyiminin termodinamik temele sahip olduğunu gösterir.

| Akışkan | Tipik Hız (m/s) | Optimum EGM Hızı (m/s) | D_opt Eğilimi | Not |
|---------|-----------------|------------------------|---------------|-----|
| Su (soğuk, <30°C) | 1.0 - 3.0 | 1.5 - 2.5 | Geleneksele yakın | Korozyon hızla artar > 3 m/s |
| Su (sıcak, 60-90°C) | 1.0 - 2.5 | 1.0 - 2.0 | Biraz büyük çap | Düşük viskozite → düşük f |
| Buhar (düşük basınç, <3 bar) | 15 - 25 | 20 - 30 | Büyük çap gerekli | Düşük yoğunluk → yüksek hız |
| Buhar (yüksek basınç, >10 bar) | 25 - 40 | 30 - 40 | Orta çap | Yüksek yoğunluk yardımcı |
| Basınçlı hava (6-8 bar) | 6 - 10 | 6 - 8 | Mümkünse büyük | Sıkıştırılabilirlik etkisi |
| Termal yağ | 0.5 - 2.0 | 1.0 - 1.5 | Büyük çap | Yüksek viskozite → yüksek f |
| Glikol çözeltisi (%30-50) | 1.0 - 2.5 | 1.5 - 2.0 | Büyük çap | Yüksek viskozite dikkat |
| Kondensat (geri dönüş) | 1.0 - 2.0 | 1.0 - 1.5 | Büyük çap tercih | Flash buhar riski |
| Doğalgaz (düşük basınç) | 15 - 25 | 15 - 20 | Emniyet öncelikli | Basınç düşüşü kritik |

> **Pratik kural:** EGM optimum hızları, geleneksel mühendislik kurallarının alt-orta bölgesine denk gelir. Bu, geleneksel kuralların genellikle biraz "üst limitli" (küçük çaplı, ucuz tasarım) olduğunu gösterir.

---

## 5. Boru Ağı Optimizasyonu (Pipe Network Optimization)

### 5.1 Seri Boru Sistemleri (Series Pipe Systems)

**Fiziksel sezgi:** Seri bağlı borularda aynı kütle debisi tüm segmentlerden geçer. Her segmentin kendi çapı, uzunluğu ve sürtünme faktörü vardır. Toplam entropi üretimi, her segmentin entropi üretiminin toplamıdır. Optimizasyon her segmenti bağımsız olarak ele alabilir.

```
Ṡ_gen,toplam = Σᵢ Ṡ_gen,i = Σᵢ [8 × f_i × L_i × ṁ³ / (π² × D_i⁵ × ρ_i² × T_i)]

Her segment için D_opt,i bağımsız olarak hesaplanır.
Kısıtlar:
- Toplam basınç düşüşü ≤ Mevcut pompa basıncı
- D geçişlerinde kayıp katsayıları eklenir (genişleme/daralma)
```

**Önemli:** Seri segmentler arasında çap değişimi, ek lokal kayıplar (ani genişleme, ani daralma, vana, dirsek) yaratır. Bu lokal kayıplar da Ṡ_gen'e katkıda bulunur ve eşdeğer uzunluk (equivalent length) yöntemiyle hesaba katılmalıdır:

```
L_eşdeğer = L_gerçek + Σ (K_lokal × D / f)
Burada K_lokal = lokal kayıp katsayısı (dirsek: 0.3-1.5, vana: 0.2-10, genişleme/daralma: 0.1-0.5)
```

### 5.2 Paralel Boru Sistemleri (Parallel Pipe Systems)

**Fiziksel sezgi:** Paralel boru sistemlerinde toplam debi, kollar arasında dağıtılır. Her kola giden debi, kolun direnciyle ters orantılıdır. EGM açısından, debiyi kollar arasında öyle dağıtmalısınız ki toplam entropi üretimi minimum olsun. Bu, her kolda eşit basınç düşüşü şartıyla sağlanır (zaten doğal olarak gerçekleşir).

```
Paralel sistemde:
  ΔP₁ = ΔP₂ = ... = ΔPₙ  (basınç düşüşü eşitliği)
  ṁ_toplam = ṁ₁ + ṁ₂ + ... + ṁₙ

EGM optimizasyonu:
  Minimize Ṡ_gen,toplam = Σᵢ [8 × f_i × L_i × ṁ_i³ / (π² × D_i⁵ × ρ_i² × T_i)]
  Kısıt: ṁ_toplam = Σ ṁ_i ve ΔP_i = sabit

Lagrange çarpanları ile çözüm:
  Optimum dağılım, her kolda birim debi başına Ṡ_gen'in eşit olması koşulunu verir.
```

### 5.3 Manifold Tasarımı (Manifold Design)

**Fiziksel sezgi:** Bir ana hat birden fazla kola dağıtım yapıyorsa (manifold), akış dağılımının homojenliği toplam Ṡ_gen'i doğrudan etkiler. Homojen olmayan dağılım bazı kollarda aşırı hız (yüksek sürtünme), bazılarında ise düşük hız (yetersiz kullanım) yaratır. Homojen dağılım her zaman minimum toplam Ṡ_gen'i verir.

```
Manifold optimizasyon kuralları:
1. Ana hat çapı, toplam debiye göre boyutlandırılmalı
2. Branşman çıkışları eşit aralıkta ve simetrik olmalı
3. Son branşmana doğru ana hat çapı kademeli olarak azaltılabilir
   (azalan debi → azalan çap → malzeme tasarrufu)

Konstrüktal teori (Constructal Theory) bağlantısı:
Bejan'ın konstrüktal yasasına göre, akış sistemleri zamanla direnci
minimize eden ağaç yapısına (tree-like) evrilir. Optimum manifold
tasarımı, doğadaki damar/ağaç yapısına benzer dallanma kalıpları gösterir:
  D_ana / D_dal = n^(1/3)   (Murray yasası, n = dal sayısı)
```

---

## 6. Yalıtım ve EGM (Insulation and EGM)

### 6.1 Isı Kayıplı Borularda Entropi Üretimi (Entropy Generation in Uninsulated Pipes)

**Fiziksel sezgi:** Sıcak akışkan taşıyan yalıtımsız bir boruda, ısı kaybı exergy yıkımı demektir. Yüksek sıcaklıktaki ısı akışkanından düşük sıcaklıktaki çevreye akar — bu geçiş sırasında ısının "iş yapma potansiyeli" (exergy) büyük ölçüde kaybolur. Hem sürtünme hem ısı kaybı entropi üretir.

```
Yalıtımsız boru — her iki Ṡ_gen bileşeni aktif:

Ṡ_gen,toplam = Ṡ_gen,sürtünme + Ṡ_gen,ısı kaybı

Ṡ_gen,ısı kaybı = Q̇_kayıp × (1/T_çevre - 1/T_akışkan)

Burada:
  Q̇_kayıp = U × A × (T_akışkan - T_çevre)
  U = toplam ısı geçiş katsayısı (W/(m²×K))
  A = π × D_dış × L (dış yüzey alanı)

Örnek: 100 m yalıtımsız DN100 buhar hattı (150°C, T_çevre = 20°C)
  Q̇_kayıp ≈ 15-25 kW (boru yüzey durumuna göre)
  Ṡ_gen,ısı ≈ Q̇_kayıp × (1/293 - 1/423) ≈ 0.030 - 0.050 kW/K
  Exergy yıkımı = T₀ × Ṡ_gen,ısı ≈ 293 × 0.040 ≈ 11.7 kW
```

### 6.2 Optimum Yalıtım Kalınlığı (Optimal Insulation Thickness)

**Fiziksel sezgi:** Yalıtım eklemek ısı kaybını ve dolayısıyla Ṡ_gen,ısı'yı azaltır. Ancak yalıtımın kendisi bir maliyet taşır. EGM perspektifinden, yalıtım kalınlığı artırıldıkça Ṡ_gen,ısı azalır ama azalma hızı da düşer (logaritmik davranış — silindirik geometri). Bir noktadan sonra ek yalıtımın entropi kazancı, maliyetini karşılamaz.

```
Yalıtılmış boru ısı kaybı:
  Q̇_kayıp = 2 × π × L × (T_akışkan - T_çevre) /
             [1/(h_iç × r_iç) + ln(r_dış/r_iç)/k_boru + ln(r_yalıtım/r_dış)/k_yalıtım + 1/(h_dış × r_yalıtım)]

Yalıtım kalınlığı (δ) arttıkça:
  r_yalıtım = r_dış + δ
  Q̇_kayıp azalır → Ṡ_gen,ısı azalır

Optimum yalıtım kalınlığı — ekonomik EGM:
  C_yalıtım(δ) = c_yalıtım × π × [(r_dış + δ)² - r_dış²] × L
  C_ısı_kaybı(δ) = T₀ × Ṡ_gen,ısı(δ) × t_çalışma × c_exergy

  dC_toplam/dδ = 0 → δ_opt

Tipik sonuçlar (buhar hatları):
  - DN50, 150°C → δ_opt ≈ 40-50 mm
  - DN100, 150°C → δ_opt ≈ 50-60 mm
  - DN100, 250°C → δ_opt ≈ 60-80 mm
  - DN200, 200°C → δ_opt ≈ 60-75 mm
```

> **Kritik yalıtım yarıçapı uyarısı:** Küçük çaplı borularda (< DN25) yalıtım eklemek dış yüzey alanını artırarak ısı kaybını artırabilir — bu "kritik yalıtım yarıçapı" (r_kritik = k_yalıtım / h_dış) kavramıdır. Ancak endüstriyel boru çaplarında bu durum pratikte oluşmaz.

---

## 7. Sayısal Örnek (Numerical Example)

### Problem Tanımı

Bir fabrikada soğutma suyu hattı tasarlanacaktır:
- Boru uzunluğu: L = 100 m
- Kütle debisi: ṁ = 10 kg/s
- Su sıcaklığı: T = 60°C = 333.15 K
- Boru malzemesi: Çelik (yüzey pürüzlülüğü ε = 0.045 mm)
- Yalıtılmış hat (q" ≈ 0, yalnızca sürtünme bileşeni)
- Su özellikleri (60°C): ρ = 983.2 kg/m³, μ = 4.67 × 10⁻⁴ Pa×s

### Adım 1: İlk Tahmin

```
v_hedef = 2.0 m/s (soğuk/ılık su için tipik)
A = ṁ / (ρ × v) = 10 / (983.2 × 2.0) = 0.005085 m²
D₀ = √(4 × A / π) = √(4 × 0.005085 / π) = 0.0805 m ≈ 80.5 mm
```

### Adım 2: Standart Çaplar İçin Hesaplama

DN80, DN100, DN125 ve DN150 için ayrı ayrı hesaplayalım:

```
┌─────────┬────────────┬──────────┬───────────────┬────────────┬────────────┬──────────────┐
│ Boru    │ İç Çap     │ Hız      │ Re            │ f (Darcy)  │ ΔP         │ Ṡ_gen        │
│ Boyutu  │ D (mm)     │ v (m/s)  │               │            │ (kPa)      │ (W/K)        │
├─────────┼────────────┼──────────┼───────────────┼────────────┼────────────┼──────────────┤
│ DN80    │ 80.1       │ 1.99     │ 3.36 × 10⁵   │ 0.0178     │ 43.7       │ 1.332        │
│ DN100   │ 105.3      │ 1.15     │ 2.56 × 10⁵   │ 0.0170     │ 10.8       │ 0.330        │
│ DN125   │ 130.7      │ 0.75     │ 2.06 × 10⁵   │ 0.0164     │ 3.55       │ 0.108        │
│ DN150   │ 155.1      │ 0.53     │ 1.74 × 10⁵   │ 0.0161     │ 1.48       │ 0.045        │
└─────────┴────────────┴──────────┴───────────────┴────────────┴────────────┴──────────────┘
```

### Adım 3: Hesaplama Detayı (DN100 için)

```
v = 4 × ṁ / (π × D² × ρ)
  = 4 × 10 / (π × 0.1053² × 983.2)
  = 40 / (0.03482 × 983.2)
  = 40 / 34.24
  = 1.168 m/s ≈ 1.15 m/s (yuvarlama)

Re = ρ × v × D / μ
   = 983.2 × 1.168 × 0.1053 / (4.67 × 10⁻⁴)
   = 120.94 / (4.67 × 10⁻⁴)
   = 2.59 × 10⁵

f (Swamee-Jain):
  = 0.25 / [log₁₀(ε/(3.7×D) + 5.74/Re^0.9)]²
  = 0.25 / [log₁₀(0.000045/(3.7×0.1053) + 5.74/(259000)^0.9)]²
  = 0.25 / [log₁₀(0.000115 + 0.0000396)]²
  = 0.25 / [log₁₀(0.000155)]²
  = 0.25 / [-3.810]²
  = 0.25 / 14.52
  = 0.0172 ≈ 0.0170

ΔP = f × (L/D) × (ρ × v²/2)
   = 0.0170 × (100/0.1053) × (983.2 × 1.168²/2)
   = 0.0170 × 949.7 × 670.5
   = 10,820 Pa ≈ 10.8 kPa

Pompa gücü = ṁ × ΔP / (ρ × η_pompa)
           = 10 × 10820 / (983.2 × 0.75)
           = 108200 / 737.4
           = 146.7 W ≈ 0.147 kW

Ṡ_gen = ṁ × ΔP / (ρ × T)
      = 10 × 10820 / (983.2 × 333.15)
      = 108200 / 327550
      = 0.330 W/K

Exergy yıkımı = T₀ × Ṡ_gen = 298.15 × 0.000330 = 0.0984 kW
```

### Adım 4: Ekonomik Karşılaştırma

```
Varsayımlar:
  - Elektrik fiyatı: c_e = 0,09 EUR/kWh = 3,20 TL/kWh
  - Çalışma süresi: t = 8000 saat/yıl
  - Pompa verimi: η = 0.75
  - Boru maliyeti: DN80 ≈ 85 TL/m, DN100 ≈ 120 TL/m, DN125 ≈ 165 TL/m, DN150 ≈ 220 TL/m
  - Amortisman: 15 yıl, %8 faiz → CRF = 0.117

┌─────────┬──────────────┬───────────────┬───────────────┬──────────────┐
│ Boyut   │ Boru Maliyeti│ Pompa Maliyeti│ Exergy Maliyet│ TOPLAM       │
│         │ (TL/yıl)     │ (TL/yıl)     │ (TL/yıl)      │ (TL/yıl)     │
├─────────┼──────────────┼───────────────┼───────────────┼──────────────┤
│ DN80    │ 994          │ 4,678         │ 1,026         │ 6,698        │
│ DN100   │ 1,404        │ 1,126         │ 251           │ 2,781        │
│ DN125   │ 1,931        │ 364           │ 83            │ 2,378        │
│ DN150   │ 2,574        │ 152           │ 35            │ 2,761        │
└─────────┴──────────────┴───────────────┴───────────────┴──────────────┘

→ Ekonomik optimum: DN125 (en düşük toplam maliyet)
→ Termodinamik optimum: DN150 (en düşük Ṡ_gen)
→ DN125 hem ekonomik hem termodinamik olarak iyi bir seçimdir
```

### Adım 5: Sonuç ve Yorum

```
Sonuç Özeti:
  - D_opt (EGM, saf termodinamik) → DN150 yönünde (Ṡ_gen minimum)
  - D_opt (ekonomik EGM) → DN125 (toplam maliyet minimum)
  - Geleneksel seçim → DN80 veya DN100 (hız kuralına göre)

EGM kazancı:
  DN100 → DN125 geçişi:
  - Ek boru maliyeti: +527 TL/yıl (%38 artış)
  - Pompalama tasarrufu: -762 TL/yıl (%68 azalış)
  - Exergy tasarrufu: -168 TL/yıl (%67 azalış)
  - Net tasarruf: 403 TL/yıl
  - Geri ödeme süresi: (165-120) × 100 / 403 = 11.2 ay
```

---

## 8. Pratik Mühendislik Kuralları (Practical Engineering Rules)

**Fiziksel sezgi:** EGM analizi her boru hattı için detaylı hesap gerektirir. Ancak aşağıdaki pratik kurallar, hızlı karar vermek için güvenilir yaklaşımlar sunar. Bu kurallar, çok sayıda EGM optimizasyonunun ortalamasından türetilmiştir.

### 8.1 Hız Bazlı Kurallar

```
Su (soğuk/sıcak):
  D_opt → v ≈ 1.5 - 2.5 m/s hız verir
  v > 3.0 m/s ise kesinlikle çap artır (erozyon + yüksek Ṡ_gen)
  v < 0.5 m/s ise çap küçültülebilir (korozyon riski var ama Ṡ_gen çok düşük)

Buhar:
  D_opt → v ≈ 20 - 30 m/s (düşük basınç, <3 bar)
  D_opt → v ≈ 30 - 40 m/s (yüksek basınç, >10 bar)
  Buhar hızı 50 m/s'yi aşarsa erozyon ve su çekiçi riski çok yükselir

Basınçlı hava:
  D_opt → v ≈ 6 - 8 m/s
  v > 10 m/s ise basınç düşüşü kabul edilemez seviyeye çıkar (%10+)
  Basınçlı havada her 1 bar ek basınç düşüşü → kompresörde %7-8 ek enerji
```

### 8.2 Çap Seçim Kuralları

```
Kural 1 — Asimetri kuralı:
  Bir alt standart çapa inmek, bir üst standart çapa çıkmaktan
  her zaman daha kötüdür. Tereddütte büyük çapı seç.

Kural 2 — %5-10 vs %20-40 kuralı:
  Bir üst standart çapa çıkmak:
  → Boru maliyetinde %5-10 artış (yatırım)
  → Pompalama enerjisinde %20-40 azalış (işletme)
  → Çoğu durumda 1-3 yıl geri ödeme süresi

Kural 3 — Gelecek büyüme kuralı:
  Debi artışı bekleniyorsa, EGM optimumu mevcut debi ile değil,
  beklenen maksimum debi ile hesaplanmalıdır. Ṡ_gen ∝ ṁ³ olduğundan,
  %20 debi artışı → %73 Ṡ_gen artışı demektir.

Kural 4 — Uzun hat kuralı:
  L > 200 m ise bir üst çap seçmek neredeyse her zaman ekonomiktir.
  Ṡ_gen ∝ L olduğundan, uzun hatlarda pompalama maliyeti baskındır.

Kural 5 — Sık kullanılan hat kuralı:
  t_çalışma > 6000 saat/yıl ise bir üst çap tercih et.
  Yıllık pompalama maliyeti çalışma saatiyle doğru orantılıdır.
```

### 8.3 Sık Yapılan Hatalar

```
Hata 1: Sadece yatırım maliyetine bakmak
  → Boru ömrü 20-30 yıl. Pompalama maliyeti genellikle boru maliyetinin
     3-10 katıdır (ömür boyu toplam).

Hata 2: Basınç düşüşünü ihmal etmek
  → %5 basınç düşüşü "kabul edilebilir" görülür ama yıllık binlerce
     TL pompalama maliyeti demektir.

Hata 3: Lokal kayıpları unutmak
  → Dirsepler, vanalar, genişleme/daralma parçaları toplam basınç
     düşüşünün %30-50'sini oluşturabilir. EGM analizine dahil edilmeli.

Hata 4: Akışkan özelliklerini sabit kabul etmek
  → Sıcaklık değişimiyle ρ ve μ değişir. Özellikle yağ ve glikol
     sistemlerinde bu fark çok büyüktür (μ 10 kat değişebilir).

Hata 5: Boruyu bağımsız değerlendirmek
  → Boru sistemi pompaya, vanaya, ısı eşanjörüne bağlıdır.
     Sistem düzeyinde EGM optimizasyonu, bileşen düzeyinden farklı
     sonuçlar verebilir.
```

### 8.4 Hızlı Kontrol Tablosu (Quick Reference)

```
Su sistemleri için pratik D_opt tahmini:
  D_opt (mm) ≈ 18.8 × ṁ^0.45   (ṁ kg/s cinsinden, 1-50 kg/s aralığı)

Örnek doğrulama:
  ṁ = 10 kg/s → D_opt ≈ 18.8 × 10^0.45 ≈ 18.8 × 2.82 ≈ 53 mm ... (*)

  (*) Bu ampirik formül kısa hatlar içindir. L > 50 m için:
  D_opt (mm) ≈ 18.8 × ṁ^0.45 × (L/50)^0.15

  ṁ = 10 kg/s, L = 100 m → D_opt ≈ 53 × (100/50)^0.15 ≈ 53 × 1.11 ≈ 59 mm

  Bu, DN65 veya DN80 arasında bir değerdir — ekonomik analizle doğrulanmalıdır.

Basınçlı hava için pratik D_opt tahmini:
  D_opt (mm) ≈ 25 × Q^0.38   (Q: serbest hava debisi m³/min cinsinden)
```

---

## İlgili Dosyalar

- `factory/entropy_generation/fluid_flow_egm.md` — Genel akışkan akışı EGM formülasyonu
- `factory/entropy_generation/fundamentals.md` — EGM temel kavramları ve Gouy-Stodola teoremi
- `pump/formulas.md` — Pompa exergy analizi formülleri
- `pump/solutions/system_optimization.md` — Pompa sistemi optimizasyonu çözümleri
- `factory/cross_equipment.md` — Ekipmanlar arası entegrasyon (pompa-boru sistemi)
- `factory/heat_integration.md` — Isı entegrasyonu (yalıtım kararlarıyla bağlantılı)
- `factory/economic_analysis.md` — Ekonomik analiz yöntemleri (yatırım kararları)
- `factory/utility_analysis.md` — Yardımcı sistem analizi (boru ağı değerlendirmesi)

## Referanslar

1. **Bejan, A.** (1996). "Entropy Generation Minimization." CRC Press. — Boru akışı EGM formülasyonunun orijinal kaynağı
2. **Bejan, A.** (2000). "Shape and Structure, from Engineering to Nature." Cambridge University Press. — Konstrüktal teori ve manifold tasarımı
3. **Bejan, A., Tsatsaronis, G., Moran, M.** (1996). "Thermal Design and Optimization." Wiley. — Termoekonomik boru optimizasyonu
4. **Swamee, P.K., Jain, A.K.** (1976). "Explicit equations for pipe-flow problems." ASCE Journal of the Hydraulics Division. — Swamee-Jain sürtünme faktörü formülü
5. **White, F.M.** (2015). "Fluid Mechanics." 8th Edition, McGraw-Hill. — Boru akışı temelleri
6. **Çengel, Y.A., Cimbala, J.M.** (2017). "Akışkanlar Mekaniği: Temelleri ve Uygulamaları." McGraw-Hill. — Türkçe referans
7. **Kakaç, S., Liu, H., Pramuanjaroenkij, A.** (2012). "Heat Exchangers: Selection, Rating, and Thermal Design." CRC Press. — Boru içi ısı transferi
8. **ASHRAE Handbook — HVAC Systems and Equipment** (2024). — Endüstriyel boru boyutlandırma standartları
9. **TS EN 13480** — Metalik endüstriyel boru hatları standartı (Türk Standartları)
