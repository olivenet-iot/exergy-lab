---
title: "Soğutma Çevrimlerinde EGM (Entropy Generation Minimization in Refrigeration)"
category: factory
equipment_type: factory
keywords: [soğutma çevrimi, chiller, kompresör, kondenser, evaporatör, genleşme vanası, throttling, soğutucu akışkan]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/bejan_number.md, chiller/formulas.md, chiller/equipment/vapor_compression.md, chiller/equipment/absorption.md]
use_when: ["Soğutma sistemi EGM analizi yapılacakken", "Chiller entropi dağılımı değerlendirilecekken", "Genleşme vanası irreversibility analizi gerektiğinde"]
priority: medium
last_updated: 2026-02-01
---

# Soğutma Çevrimlerinde EGM (Entropy Generation Minimization in Refrigeration)

> Son güncelleme: 2026-02-01

## Genel Bakış

Soğutma çevrimleri, endüstriyel tesislerdeki en yaygın enerji tüketim kaynaklarından biridir ve toplam elektrik tüketiminin %15-40'ını oluşturabilir. Klasik enerji analizi yalnızca COP (Coefficient of Performance) değerine odaklanırken, entropi üretimi minimizasyonu (EGM) yaklaşımı her bileşendeki tersinmezliğin (irreversibility) kökenini, büyüklüğünü ve azaltma potansiyelini ortaya koyar. Bu dosya, buhar sıkıştırmalı (vapor compression) ve absorpsiyonlu (absorption) soğutma çevrimlerinde EGM analizinin kapsamlı bir çerçevesini sunar.

Soğutma çevrimlerinde EGM'nin temel değeri şudur: enerji "korunur" ancak kalitesi düşer. Bir chiller, düşük sıcaklıklı ortamdan ısıyı yüksek sıcaklıklı ortama taşırken, bu termodinamik olarak "doğal olmayan" yönde iş yapma sürecinde kaçınılmaz olarak entropi üretir. EGM, bu üretimi minimize ederek aynı soğutma kapasitesini daha az iş girdisiyle elde etmeyi hedefler.

---

## 1. Buhar Sıkıştırmalı Çevrimde Entropi Kaynakları (Entropy Sources in Vapor Compression Cycle)

### 1.1 Çevrim Bileşenleri ve S_gen

Standart buhar sıkıştırmalı soğutma çevrimi dört ana bileşenden oluşur. Her bileşen farklı mekanizmalarla entropi üretir ve toplam çevrim tersinmezliği bu bileşenlerin katkılarının toplamıdır.

**Fiziksel Sezgi:** Bir soğutma çevrimi düşünün: soğutucu akışkan (refrigerant), evaporatörde düşük basınçta buharlaşarak ortamdan ısı alır, kompresörde sıkıştırılarak basıncı ve sıcaklığı yükselir, kondenserde yüksek basınçta yoğuşarak ısıyı dış ortama verir, son olarak genleşme vanasında basıncı düşürülerek tekrar evaporatöre gönderilir. Bu dört adımın her birinde farklı tersinmezlik mekanizmaları entropi üretir.

```
Toplam Entropi Üretimi (Total Entropy Generation):

  Ṡ_gen,toplam = Ṡ_gen,komp + Ṡ_gen,kond + Ṡ_gen,exp + Ṡ_gen,evap

Burada:
  Ṡ_gen,toplam  = çevrimin toplam entropi üretim hızı [kW/K]
  Ṡ_gen,komp    = kompresör entropi üretimi [kW/K]
  Ṡ_gen,kond    = kondenser entropi üretimi [kW/K]
  Ṡ_gen,exp     = genleşme vanası entropi üretimi [kW/K]
  Ṡ_gen,evap    = evaporatör entropi üretimi [kW/K]
```

Her bileşenin entropi üretim mekanizmaları:

- **Kompresör (Compressor):** Sürtünme kayıpları (friction losses), ısı transferi kayıpları (heat transfer to/from surroundings), iç sızıntılar (internal leakage). Gerçek sıkıştırma izentropik olmadığından entropi üretilir.

- **Kondenser (Condenser):** Soğutucu akışkan ile soğutma suyu/havası arasındaki sonlu sıcaklık farkı (finite temperature difference) ana kaynaktır. Ayrıca akışkan tarafı ve hava/su tarafı basınç düşümleri (pressure drops) ek entropi üretir.

- **Genleşme vanası (Expansion Valve):** Throttling süreci — iş çıkışı olmaksızın basınç düşürme. Tamamen tersinmez bir süreçtir ve tipik olarak çevrimin en büyük tek entropi kaynağıdır.

- **Evaporatör (Evaporator):** Soğutulan ortam ile soğutucu akışkan arasındaki sonlu sıcaklık farkı. Düşük sıcaklıklarda çalıştığı için aynı ΔT, yüksek sıcaklıklara kıyasla daha fazla entropi üretir.

**Tipik S_gen dağılımı (metin tabanlı pasta grafik):**

```
Soğutma Çevrimi Entropi Üretim Dağılımı
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Genleşme Vanası   ████████████████████   35%  ← En büyük kaynak
  Kompresör          ██████████████         25%
  Kondenser          ████████████           20%
  Evaporatör         ████████████           20%

  Toplam             ████████████████████████████████  100%
```

### 1.2 S_gen Dağılım Tablosu

Aşağıdaki tablo, tipik bir endüstriyel buhar sıkıştırmalı chiller için bileşen bazında entropi üretim dağılımını, ana irreversibility kaynaklarını ve Bejan sayılarını özetler.

**Fiziksel Sezgi:** Bejan sayısı (Be), toplam entropi üretiminin ne kadarının ısı transferi kaynaklı, ne kadarının sürtünme/akış kaynaklı olduğunu gösterir. Be → 1 ise ısı transferi baskın, Be → 0 ise sürtünme baskındır. Genleşme vanasında Bejan sayısı tanımsızdır çünkü throttling ne ısı transferi ne de klasik sürtünme mekanizmasıyla açıklanır — kendine özgü bir tersinmezliktir.

| Bileşen | S_gen Payı (%) | Ana İrreversibllik Kaynağı | Bejan Sayısı (Be) |
|---------|---------------|---------------------------|-------------------|
| Kompresör | 20-30 | Sürtünme, iç ısı transferi, sızıntı | Be ≈ 0.3-0.5 |
| Kondenser | 15-25 | Sonlu sıcaklık farkı (ΔT baskın) | Be ≈ 0.6-0.8 |
| Genleşme vanası | 30-40 | Throttling (tamamen irreversible) | N/A |
| Evaporatör | 15-25 | Sonlu sıcaklık farkı (ΔT baskın) | Be ≈ 0.5-0.7 |

**Önemli not:** Bu dağılım çalışma koşullarına göre değişir. Düşük evaporatör sıcaklıklarında (ör. -30°C dondurma uygulamaları) genleşme vanasının payı %45'e kadar çıkabilir. Yüksek kondenser sıcaklıklarında (sıcak iklim, kirli kondenser) kondenser payı artar.

---

## 2. Genleşme Vanası — En Büyük S_gen Kaynağı (Expansion Valve — Largest S_gen Source)

### 2.1 Throttling İrreversiblliği (Throttling Irreversibility)

**Fiziksel Sezgi:** Bir genleşme vanası, soğutucu akışkanın basıncını hiçbir iş çıkışı olmadan düşürür. Bunu şöyle düşünün: yüksek basınçlı bir akışkanı dar bir orifisten geçiriyorsunuz. Akışkanın basınç enerjisi (P×v) yararlı bir iş üretmek yerine tamamen iç sürtünme ile iç enerji formuna dönüşüyor. Bu, sanki bir şelalenin enerjisini türbin yerine kayalarla yutturmanız gibidir — enerji korunur ama iş potansiyeli (exergy) yok edilir.

Throttling sürecinin termodinamik özellikleri:

```
Throttling (Genleşme) Süreci — Temel İlkeler:

  İsenthalpik süreç:     h_giriş = h_çıkış     (entalpi korunur)
  Entropi artışı:        s_çıkış > s_giriş      (entropi artar)
  İş çıkışı:             W = 0                   (hiç iş üretilmez)
  Isı transferi:         Q ≈ 0                   (adyabatik varsayım)

Burada:
  h = özgül entalpi [kJ/kg]
  s = özgül entropi [kJ/(kg·K)]
```

**Fiziksel Sezgi:** Entalpi korunduğu halde entropi artması, sürecin tamamen tersinmez olduğunu kanıtlar. Birinci yasa (enerji korunumu) karşılanır ama ikinci yasa (entropi artışı) ihlal edilmez — entropi üretilir ve bu üretilen entropi, kaybedilen iş potansiyeline karşılık gelir.

```
Genleşme Vanasında Entropi Üretim Hızı:

  Ṡ_gen,exp = ṁ × (s_çıkış - s_giriş)

Burada:
  Ṡ_gen,exp  = genleşme vanasında entropi üretim hızı [kW/K]
  ṁ          = soğutucu akışkan kütle debisi [kg/s]
  s_çıkış    = vana çıkışındaki özgül entropi [kJ/(kg·K)]
  s_giriş    = vana girişindeki özgül entropi [kJ/(kg·K)]

Gouy-Stodola teoremi ile exergy yıkımı:

  Ėx_yıkım,exp = T₀ × Ṡ_gen,exp = T₀ × ṁ × (s_çıkış - s_giriş)

Burada:
  Ėx_yıkım,exp = genleşme vanasında exergy yıkım hızı [kW]
  T₀            = referans ortam sıcaklığı [K] (tipik: 298.15 K = 25°C)
```

**Kritik fark:** Genleşme vanası, çevrimin diğer bileşenlerinden farklı olarak, tersinmezliğin kaçınılmaz olduğu tek bileşendir. Kompresörü daha verimli yapabilirsiniz, kondenseri daha büyük yapabilirsiniz, ama klasik bir genleşme vanasının throttling tersinmezliğini ortadan kaldıramazsınız — yalnızca teknolojik alternatiflerle (ejektör, turbo-expander) azaltabilirsiniz.

**Sayısal Örnek:**

```
Tipik R-134a soğutma çevrimi:
  Kondenser basıncı:  P_kond = 12 bar, T_kond = 46°C
  Evaporatör basıncı:  P_evap = 3 bar,  T_evap = 1°C
  Akışkan debisi:      ṁ = 0.5 kg/s

Kondenser çıkışı (doymuş sıvı):
  h_giriş = 264.1 kJ/kg,  s_giriş = 1.224 kJ/(kg·K)

Vana çıkışı (ıslak buhar):
  h_çıkış = 264.1 kJ/kg,  s_çıkış = 1.283 kJ/(kg·K)

Entropi üretimi:
  Ṡ_gen,exp = 0.5 × (1.283 - 1.224) = 0.0295 kW/K

Exergy yıkımı (T₀ = 298.15 K):
  Ėx_yıkım,exp = 298.15 × 0.0295 = 8.80 kW
```

Bu, 100 kW soğutma kapasiteli bir chiller için toplam exergy yıkımının yaklaşık %35'ine karşılık gelir.

### 2.2 Alternatifler: Throttling S_gen Azaltma (Alternatives for Reducing Throttling S_gen)

**Fiziksel Sezgi:** Throttling tersinmezliğini azaltmanın temel stratejisi, basınç düşümü sırasında akışkandan bir miktar yararlı iş geri kazanmak veya throttling aralığını daraltmaktır. Aşağıda endüstriyel ölçekte uygulanan alternatifler karşılaştırılmıştır.

**1. Elektronik Genleşme Vanası (Electronic Expansion Valve — EEV):**
- Throttling S_gen'i doğrudan azaltmaz (hala isenthalpik süreç)
- Ancak sürekli kızgınlık (superheat) kontrolü ile evaporatörü daha etkin kullanır
- Dolaylı olarak toplam çevrim S_gen'ini %5-8 azaltabilir

**2. Ejektör (Ejector):**

**Fiziksel Sezgi:** Ejektör, kondenser çıkışındaki yüksek basınçlı sıvının momentum enerjisini kullanarak evaporatör çıkışındaki düşük basınçlı buharı sürükler. Bu, throttling sırasında normalde kaybedilen basınç enerjisinin bir kısmını geri kazanır.

- Genleşme işinden bir kısım enerji geri kazanılır
- S_gen azaltımı: %10-20
- COP artışı: %5-15
- Hareketli parçası yok → düşük bakım maliyeti

**3. Turbo-Expander (Turbo-Expander):**

**Fiziksel Sezgi:** Bir türbin gibi çalışarak akışkanın genleşme sürecinde mil işi üretir. Bu iş, kompresöre yardımcı olarak kullanılabilir. İdeal durumda genleşme izentropik olurdu ve hiç entropi üretilmezdi.

- Genleşme işi mil işi olarak geri kazanılır
- S_gen azaltımı: %30-50
- COP artışı: %10-25
- Yüksek yatırım maliyeti, karmaşık mekanik tasarım
- Özellikle CO₂ (R-744) transkritik çevrimlerde verimli

**4. Flash Tank ile İki Kademeli Sıkıştırma (Flash Tank with Two-Stage Compression):**

**Fiziksel Sezgi:** Genleşmeyi tek büyük adım yerine iki küçük adıma bölerek, her adımdaki entropi artışını azaltır. Ayrıca ara basınçtaki buhar (flash gas) doğrudan ikinci kademe kompresöre gönderilir — evaporatörden geçmesi gerekmez.

- Throttling aralığını bölerek efektif S_gen azaltır
- S_gen azaltımı: %15-25
- Düşük sıcaklık uygulamalarında (<-20°C) özellikle etkili
- İki kompresör veya iki kademeli kompresör gerektirir

**5. Ekonomizer (Alt Soğutucu / Subcooler):**

**Fiziksel Sezgi:** Kondenser çıkışındaki sıvıyı genleşme vanasından önce daha fazla soğutarak, vana sonrası oluşan flash gazı (buhar) azaltır. Daha az flash gaz demek, evaporatöre daha fazla sıvı girmesi ve daha etkili buharlaşma demektir.

- S_gen azaltımı: %8-15
- COP artışı: %5-10
- Nispeten basit ve düşük maliyetli çözüm

**Alternatiflerin Karşılaştırma Tablosu:**

| Teknoloji | S_gen Azaltımı | COP Artışı | Maliyet | Karmaşıklık | Uygunluk |
|-----------|---------------|-----------|---------|-------------|----------|
| EEV | %0 (doğrudan) | %5-8 (dolaylı) | Düşük | Düşük | Her sistem |
| Ejektör | %10-20 | %5-15 | Orta | Orta | Orta-büyük sistemler |
| Turbo-expander | %30-50 | %10-25 | Yüksek | Yüksek | CO₂ ve büyük sistemler |
| Flash tank + 2 kademe | %15-25 | %10-20 | Yüksek | Yüksek | Düşük sıcaklık uyg. |
| Ekonomizer | %8-15 | %5-10 | Düşük-Orta | Düşük | Her sistem |

---

## 3. Kompresör Entropi Üretimi (Compressor Entropy Generation)

### 3.1 İzentropik Verim ve S_gen (Isentropic Efficiency and S_gen)

**Fiziksel Sezgi:** İdeal bir kompresör izentropik (sabit entropi) çalışır — yani sıkıştırma sırasında hiç entropi üretmez. Gerçek kompresörlerde sürtünme, iç sızıntılar ve ısı transferi nedeniyle sıkıştırma süreci izentropik olmaktan sapma gösterir. Bu sapmanın ölçüsü izentropik verimdir (η_is). Verim ne kadar yüksekse, gerçek süreç ideale o kadar yakındır ve entropi üretimi o kadar azdır.

```
Kompresör Entropi Üretim Hızı:

  Ṡ_gen,komp = ṁ × (s₂ - s₁)

Burada:
  s₁ = kompresör girişindeki özgül entropi [kJ/(kg·K)]
  s₂ = kompresör çıkışındaki gerçek özgül entropi [kJ/(kg·K)]

İzentropik verim ile ilişki:

  η_is = (h₂s - h₁) / (h₂ - h₁)

  h₂s = izentropik sıkıştırma sonrası entalpi [kJ/kg]  (s₂s = s₁)
  h₂  = gerçek sıkıştırma sonrası entalpi [kJ/kg]      (s₂ > s₁)

Exergy yıkımı:

  Ėx_yıkım,komp = T₀ × Ṡ_gen,komp = T₀ × ṁ × (s₂ - s₁)
```

**Fiziksel Sezgi:** η_is = 1.0 olduğunda s₂ = s₁ olur ve Ṡ_gen,komp = 0 olur (ideal durum). η_is düştükçe s₂ artar ve entropi üretimi yükselir. Düşük izentropik verim, aynı basınç oranı için daha fazla enerji harcandığı ve bu fazla enerjinin tamamen entropi olarak üretildiği anlamına gelir.

### 3.2 Kompresör Tipi Seçiminin Etkisi (Effect of Compressor Type Selection)

**Fiziksel Sezgi:** Farklı kompresör tipleri, farklı mekanik ve termodinamik özellikler nedeniyle farklı izentropik verimlere sahiptir. Büyük kapasiteli santrifüj kompresörler, küçük kapasiteli pistonlu kompresörlerden daha yüksek verime sahip olma eğilimindedir — ölçek etkisi. Ancak her kompresör tipinin optimal çalışma aralığı farklıdır.

| Kompresör Tipi | η_is Aralığı | Göreceli S_gen | Kapasite Aralığı | En Uygun Uygulama |
|---------------|-------------|---------------|-----------------|-------------------|
| Pistonlu (Reciprocating) | 0.65-0.80 | Yüksek | 1-100 kW | Küçük ticari, değişken yük |
| Scroll | 0.70-0.85 | Orta-Yüksek | 2-50 kW | Küçük-orta ticari, split |
| Vidalı (Screw) | 0.75-0.85 | Orta | 50-1000 kW | Endüstriyel, sürekli yük |
| Santrifüj (Centrifugal) | 0.80-0.90 | Düşük | 200-10000 kW | Büyük endüstriyel, HVAC |

**Pratik çıkarım:** Aynı soğutma yükü için santrifüj kompresör seçimi, pistonlu kompresöre kıyasla kompresör S_gen'ini %25-40 azaltabilir. Ancak santrifüj kompresörler düşük yüklerde verim kaybeder — kısmi yükte (part load) vidalı kompresör daha avantajlı olabilir.

---

## 4. Kondenser ve Evaporatör Optimizasyonu (Condenser and Evaporator Optimization)

### 4.1 Optimum Kondenser Boyutu (Optimum Condenser Size)

**Fiziksel Sezgi:** Kondenserde entropi üretiminin ana kaynağı, yoğuşan soğutucu akışkan ile soğutma ortamı (su veya hava) arasındaki sıcaklık farkıdır. Daha büyük kondenser, daha fazla ısı transfer alanı sağlar → aynı ısıyı daha düşük sıcaklık farkıyla aktarır → daha düşük yoğuşma sıcaklığı → daha az entropi üretimi. Ancak daha büyük kondenser aynı zamanda daha fazla fan/pompa gücü gerektirir (basınç düşümü artar) ve bu da ek entropi üretir. İşte tam burada EGM optimizasyonu devreye girer — toplam S_gen'i minimize eden boyutu bulmak.

```
Kondenser Entropi Üretimi:

  Isı transferi kaynaklı:
  Ṡ_gen,ΔT = Q̇_kond × (1/T_soğutma - 1/T_yoğuşma)

  Basınç düşümü kaynaklı:
  Ṡ_gen,ΔP = ṁ_soğutma × (ΔP_soğutma) / (ρ × T_ort)

  Toplam kondenser S_gen:
  Ṡ_gen,kond = Ṡ_gen,ΔT + Ṡ_gen,ΔP

Burada:
  Q̇_kond     = kondenserde atılan ısı [kW]
  T_soğutma   = soğutma ortamı sıcaklığı [K]
  T_yoğuşma   = yoğuşma sıcaklığı [K]
  ṁ_soğutma   = soğutma akışkanı debisi [kg/s]
  ΔP_soğutma  = soğutma tarafı basınç düşümü [kPa]
  ρ            = soğutma akışkanı yoğunluğu [kg/m³]
  T_ort        = ortalama soğutma akışkanı sıcaklığı [K]
```

Optimum yaklaşım sıcaklıkları (approach temperature):

- **Su soğutmalı (water-cooled):** Optimum ΔT_approach = 3-5°C
  - ΔT < 3°C → çok büyük kondenser, ΔP artışı baskınlaşır
  - ΔT > 5°C → ısı transferi S_gen'i aşırı yüksek
  - Be ≈ 0.7 (ısı transferi baskın)

- **Hava soğutmalı (air-cooled):** Optimum ΔT_approach = 8-12°C
  - Havanın düşük ısı transfer katsayısı nedeniyle daha yüksek ΔT gerekli
  - ΔT < 8°C → devasa fan gücü ve alan gereksinimi
  - ΔT > 12°C → COP önemli ölçüde düşer
  - Be ≈ 0.6-0.7

### 4.2 Optimum Evaporatör Boyutu (Optimum Evaporator Size)

**Fiziksel Sezgi:** Evaporatörde daha yüksek buharlaşma sıcaklığı (T_evap) elde etmek, kompresörün daha düşük basınç oranıyla çalışmasını sağlar. Bu, hem kompresör işini azaltır hem de kompresör entropi üretimini düşürür. Evaporatör boyutunu artırmak (daha fazla ısı transfer alanı), aynı soğutma yükünü daha küçük sıcaklık farkıyla karşılamayı mümkün kılar → T_evap artar. Ancak düşük sıcaklıklarda çalışılan uygulamalarda, evaporatördeki her birim ΔT, yüksek sıcaklıklara kıyasla daha fazla entropi üretir (çünkü S_gen ∝ ΔT/T², düşük T'de T² küçüktür).

```
Evaporatör Entropi Üretimi:

  Ṡ_gen,evap = Q̇_evap × (1/T_evap - 1/T_soğutulan)

Burada:
  Q̇_evap     = evaporatör soğutma kapasitesi [kW]
  T_evap      = buharlaşma sıcaklığı [K]
  T_soğutulan = soğutulan ortam sıcaklığı [K]

Not: T_soğutulan > T_evap olmalı (ısı soğutulan ortamdan akışkana geçer)
```

**Pratik kurallar:**
- Buharlaşma sıcaklığında her 1°C artış → COP %2-4 iyileşir
- Bu iyileşme düşük sıcaklıklarda daha belirgindir (ör. -30°C'de %4, +5°C'de %2)
- Be ≈ 0.5-0.7 (ısı transferi ile basınç düşümü arasında daha dengeli)

### 4.3 Kondenser vs Evaporatör: Hangisi Öncelikli? (Condenser vs Evaporator: Which to Prioritize?)

**Fiziksel Sezgi:** Sınırlı bütçeyle yalnızca bir ısı değiştiriciyi büyütebilirseniz, hangisini tercih etmelisiniz? Genel kural: kondenser optimizasyonu daha yüksek etkiye sahiptir. Bunun nedeni, kondenserin dış ortama (genellikle daha yüksek sıcaklık ve daha büyük ΔT) ısı attığı, dolayısıyla entropi üretim potansiyelinin daha yüksek olmasıdır.

Karar kriterleri:

```
Karar Matrisi — Kondenser mi Evaporatör mü?

  1. Göreceli S_gen payına bak:
     Ṡ_gen,kond / Ṡ_gen,evap > 1.2  → Kondenser öncelikli
     Ṡ_gen,kond / Ṡ_gen,evap < 0.8  → Evaporatör öncelikli
     0.8 ≤ oran ≤ 1.2               → Maliyet-fayda analizi yap

  2. Mevcut yaklaşım sıcaklıklarına bak:
     ΔT_kond >> optimum → Kondenser öncelikli (temizlik veya büyütme)
     ΔT_evap >> optimum → Evaporatör öncelikli

  3. Kirlilik durumunu kontrol et:
     Kirli kondenser → önce temizle (düşük maliyet, yüksek etki)
```

Genel olarak, endüstriyel uygulamalarda kondenser optimizasyonu %60 oranında daha fazla tercih edilir çünkü:
- Kondenser kirlenmeye daha yatkındır (dış ortam ile temas)
- Hava soğutmalı kondenserlerde ΔT zaten yüksektir
- Kondenser optimizasyonu aynı zamanda kompresör S_gen'ini de düşürür (daha düşük yoğuşma basıncı)

---

## 5. Soğutucu Akışkan Seçiminin Entropi Etkisi (Refrigerant Selection and Entropy Impact)

### 5.1 Akışkan Özellikleri ve S_gen (Fluid Properties and S_gen)

**Fiziksel Sezgi:** Farklı soğutucu akışkanlar, aynı soğutma yükü için farklı termodinamik döngüler oluşturur. Kritik sıcaklığı yüksek olan akışkanlar, kondenserde daha düşük basınç oranıyla çalışır → kompresör S_gen'i düşer. Gizli ısısı (latent heat) yüksek olan akışkanlar, daha düşük kütle debisiyle aynı kapasiteyi sağlar → genleşme vanası S_gen'i düşer. Ancak her akışkanın farklı transport özellikleri (viskozite, ısıl iletkenlik) ısı transfer S_gen'ini farklı şekilde etkiler.

S_gen'i etkileyen temel akışkan özellikleri:

- **Gizli ısı (Latent heat):** Yüksek → düşük kütle debisi → düşük S_gen (özellikle throttling)
- **Özgül ısı (Specific heat):** Buhar fazında düşük → daha az kızgınlık (superheat) → daha düşük kondenser girişi
- **Basınç oranı (Pressure ratio):** Düşük → düşük kompresör S_gen
- **Isıl iletkenlik (Thermal conductivity):** Yüksek → daha iyi ısı transferi → düşük ΔT → düşük S_gen
- **Viskozite (Viscosity):** Düşük → düşük basınç düşümü → düşük S_gen,ΔP

### 5.2 R-134a vs R-410A vs R-290 vs R-744 Karşılaştırma

**Fiziksel Sezgi:** Aynı soğutma görevi (100 kW soğutma, T_evap = 5°C, T_kond = 40°C) için farklı akışkanların entropi üretim profillerini karşılaştırmak, akışkan seçiminin EGM perspektifinden etkisini ortaya koyar.

| Parametre | R-134a | R-410A | R-290 (Propan) | R-744 (CO₂) |
|-----------|--------|--------|-----------------|--------------|
| Buharlaşma basıncı [bar] | 3.5 | 9.3 | 5.3 | 40.7 |
| Yoğuşma basıncı [bar] | 10.2 | 24.3 | 13.7 | 100+ (transkritik) |
| Basınç oranı | 2.9 | 2.6 | 2.6 | 2.5+ |
| Kütle debisi [kg/s] | 0.56 | 0.43 | 0.29 | 0.77 |
| S_gen,komp (göreceli) | 1.00 | 0.90 | 0.85 | 0.80 |
| S_gen,exp (göreceli) | 1.00 | 1.10 | 0.80 | 1.50-2.00* |
| S_gen,toplam (göreceli) | 1.00 | 0.95 | 0.88 | 1.10-1.30* |
| GWP | 1430 | 2088 | 3 | 1 |
| ODP | 0 | 0 | 0 | 0 |

*Not: R-744 transkritik çevrimde throttling kayıpları çok yüksektir, bu nedenle turbo-expander veya ejektör kullanımı kritik önem taşır. Turbo-expander ile S_gen,toplam R-134a seviyesine yaklaşır.

**CO₂ (R-744) transkritik çevrim — Özel durum:**

**Fiziksel Sezgi:** CO₂'nin kritik sıcaklığı (31.1°C) düşük olduğundan, sıcak iklimlerde kondenserde yoğuşma gerçekleşmez — akışkan transkritik bölgede çalışır. Bu, çok yüksek throttling S_gen demektir çünkü basınç farkı büyüktür. Ancak CO₂'nin mükemmel transport özellikleri (yüksek ısıl iletkenlik, düşük viskozite), ısı değiştiricilerdeki S_gen'i düşürür. Net sonuç: mutlaka iş geri kazanımı (turbo-expander) ile birlikte tasarlanmalıdır.

**Doğal soğutucu akışkanlar — EGM perspektifi:**
- R-290 (Propan): En düşük toplam S_gen profili, ancak yanıcılık riski (A3 sınıfı)
- R-717 (Amonyak): Yüksek gizli ısı → düşük S_gen,exp; endüstriyel uygulamalarda yaygın
- R-744 (CO₂): Turbo-expander ile rekabetçi; düşük GWP avantajı

---

## 6. Absorpsiyonlu vs Buhar Sıkıştırmalı — EGM Karşılaştırma (Absorption vs Vapor Compression — EGM Comparison)

### 6.1 Absorpsiyon Çevrimi S_gen Kaynakları (Absorption Cycle S_gen Sources)

**Fiziksel Sezgi:** Absorpsiyonlu soğutma çevrimi, mekanik kompresör yerine termal kompresyon kullanır. Bir jeneratör (generator), emici (absorber), çözelti ısı değiştiricisi (solution heat exchanger), genleşme vanaları, kondenser ve evaporatörden oluşur. Daha fazla bileşen, daha fazla entropi üretim noktası demektir. Ancak giriş enerjisi ısı olduğundan (elektrik değil), birincil enerji düzeyinde değerlendirme farklı sonuçlar verebilir.

Absorpsiyon çevrimi bileşenleri ve S_gen kaynakları:

```
Absorpsiyon Çevrimi Entropi Üretim Dağılımı:

  Ṡ_gen,toplam = Ṡ_gen,jen + Ṡ_gen,abs + Ṡ_gen,SHX + Ṡ_gen,exp1
                + Ṡ_gen,exp2 + Ṡ_gen,kond + Ṡ_gen,evap

Burada:
  Ṡ_gen,jen   = jeneratör entropi üretimi (ısı kaynağı ile çözelti arası ΔT)
  Ṡ_gen,abs   = emici entropi üretimi (absorpsiyon ısısının uzaklaştırılması)
  Ṡ_gen,SHX   = çözelti ısı değiştiricisi (solution heat exchanger)
  Ṡ_gen,exp1  = soğutucu akışkan genleşme vanası
  Ṡ_gen,exp2  = çözelti genleşme vanası
  Ṡ_gen,kond  = kondenser
  Ṡ_gen,evap  = evaporatör
```

Tipik dağılım (LiBr-H₂O, tek etkili):
- Jeneratör: %25-35 (en büyük kaynak — yüksek ΔT ile ısı transferi)
- Emici: %20-30 (absorpsiyon reaksiyonu + ısı uzaklaştırma)
- Çözelti ısı değiştiricisi: %10-15
- Genleşme vanaları: %10-15
- Kondenser + Evaporatör: %15-20

### 6.2 Karşılaştırma Tablosu (Comparison Table)

**Fiziksel Sezgi:** Buhar sıkıştırmalı çevrim daha düşük toplam S_gen üretir ve daha yüksek COP'a sahiptir. Ancak bu karşılaştırma aldatıcı olabilir: buhar sıkıştırmalı çevrim elektrik kullanır ve bu elektriğin üretiminde (ör. termik santral) önemli miktarda entropi üretilir. Absorpsiyonlu çevrim doğrudan ısı kullanır — eğer bu ısı atık ısıysa (waste heat), birincil enerji düzeyinde toplam S_gen çok daha düşük olabilir.

| Parametre | Buhar Sıkıştırmalı | Absorpsiyonlu (Tek Etkili) | Absorpsiyonlu (Çift Etkili) |
|-----------|-------------------|--------------------------|---------------------------|
| COP | 3.0-6.0 | 0.65-0.80 | 1.0-1.4 |
| Exergy verimi (η_ex) | %30-45 | %15-25 | %20-30 |
| Toplam Ṡ_gen (göreceli) | 1.0 | 3.5-5.0 | 2.5-3.5 |
| Birincil enerji S_gen* | 2.5-3.0 | 3.5-5.0 | 2.5-3.5 |
| Birincil enerji S_gen (atık ısıyla)** | 2.5-3.0 | 0.8-1.5 | 0.6-1.2 |
| Elektrik tüketimi | Yüksek | Çok düşük (sadece pompalar) | Çok düşük |
| Isı kaynağı sıcaklığı | N/A | 80-110°C | 150-180°C |

*Birincil enerji S_gen: Elektrik üretim santralinin (η_santral ≈ 0.35-0.40) S_gen'i dahil
**Atık ısı kullanımında, ısı kaynağının S_gen'i sıfır kabul edilir (zaten üretilecekti)

### 6.3 Ne Zaman Absorption Tercih Edilir? (When to Prefer Absorption?)

**Fiziksel Sezgi:** Absorpsiyon çevrimi, kendi başına her zaman daha fazla entropi üretir. Ancak sistem düzeyinde bakıldığında, eğer kullanılabilir atık ısı varsa (fabrikada buhar kazanı, baca gazı, kojenerasyon atık ısısı), bu ısıyı absorpsiyon chiller'da kullanmak toplam sistem S_gen'ini dramatik olarak düşürebilir.

Absorpsiyon tercih kriterleri:

1. **Bedava veya düşük maliyetli atık ısı mevcut** (>80°C): Evet → Absorpsiyon güçlü aday
2. **Elektrik maliyeti yüksek, gaz maliyeti düşük**: Çift etkili absorpsiyon değerlendir
3. **Kojenerasyon (CHP) sistemi mevcut**: Atık ısı absorpsiyon chiller'a yönlendirilir → trijenerasyon
4. **Güneş enerjisi entegrasyonu**: Güneş kolektörleri + absorpsiyon chiller
5. **Gürültü ve titreşim kısıtlaması**: Absorpsiyon chiller neredeyse sessiz (büyük kompresör yok)

**Sistem düzeyinde EGM karar kuralı:**

```
Sistem Düzeyinde Karar:

  Buhar sıkıştırmalı toplam S_gen:
  Ṡ_gen,VS = Ṡ_gen,santral + Ṡ_gen,iletim + Ṡ_gen,chiller_VS

  Absorpsiyonlu toplam S_gen (atık ısıyla):
  Ṡ_gen,ABS = Ṡ_gen,chiller_ABS    (atık ısı S_gen'i = 0)

  Karar:
  Ṡ_gen,ABS < Ṡ_gen,VS  →  Absorpsiyon tercih edilir
  Ṡ_gen,ABS ≥ Ṡ_gen,VS  →  Buhar sıkıştırmalı tercih edilir
```

---

## 7. Sistem Düzeyinde EGM — Chiller + Soğutma Kulesi (System-Level EGM — Chiller + Cooling Tower)

### 7.1 Entegre Sistem Analizi (Integrated System Analysis)

**Fiziksel Sezgi:** Bir chiller tek başına çalışmaz — su soğutmalı sistemlerde bir soğutma kulesi (cooling tower), pompa ve boru sistemiyle entegre çalışır. Sistem düzeyinde EGM, yalnızca chiller'ın değil, tüm yardımcı ekipmanların entropi üretimini birlikte optimize eder. Soğutma kulesi, buharlaştırmalı soğutma (evaporative cooling) ile çalışır ve su-hava karışımı sırasında ek irreversibility üretir.

```
Entegre Sistem Toplam Entropi Üretimi:

  Ṡ_gen,sistem = Ṡ_gen,chiller + Ṡ_gen,kule + Ṡ_gen,pompalar + Ṡ_gen,fanlar + Ṡ_gen,borular

Burada:
  Ṡ_gen,chiller  = chiller iç bileşenlerinin toplam S_gen [kW/K]
  Ṡ_gen,kule     = soğutma kulesi S_gen (karışma + buharlaşma + ΔT) [kW/K]
  Ṡ_gen,pompalar = kondenser suyu ve chilled water pompaları [kW/K]
  Ṡ_gen,fanlar   = soğutma kulesi fanları [kW/K]
  Ṡ_gen,borular  = boru sürtünme kayıpları [kW/K]
```

Soğutma kulesi S_gen kaynakları:
- **Karışma irreversibility'si (mixing):** Su ve hava doğrudan temas eder → konsantrasyon ve sıcaklık gradyanları
- **Buharlaştırma:** Suyun buharlaşması tersinmez bir kütle transfer sürecidir
- **Fan gücü:** Hava basınç düşümünü yenmek için harcanan enerji
- **Sıcaklık farkı:** Kulenin dış hava ile çalışma sıcaklığı arasındaki ΔT

### 7.2 Optimum Sistem Çalışma Noktası (Optimum System Operating Point)

**Fiziksel Sezgi:** Kondenser su sıcaklığını düşürmek chiller COP'unu artırır ama soğutma kulesinin daha fazla çalışmasını (daha fazla fan gücü, daha fazla su buharlaştırma) gerektirir. Optimum nokta, chiller'ın kazancı ile kulenin ek maliyetinin dengelendiği yerdir.

```
Optimum Kondenser Suyu Sıcaklığı Dengesi:

  Düşük T_kond_su:
  + Chiller COP artar → Ṡ_gen,chiller düşer
  + Kompresör gücü azalır
  - Kule fan gücü artar → Ṡ_gen,fan artar
  - Su buharlaştırma artar → Ṡ_gen,kule artar

  Yüksek T_kond_su:
  + Kule fan gücü düşer → Ṡ_gen,fan düşer
  + Su tüketimi azalır
  - Chiller COP düşer → Ṡ_gen,chiller artar
  - Kompresör gücü artar

  Optimum T_kond_su: Tipik olarak ıslak termometre sıcaklığının 3-5°C üzerinde
  (wet bulb approach = 3-5°C)
```

**Değişken hız sürücü (VSD) entegrasyonu:**

Fan hızı ve pompa hızının değişken hız sürücülerle (VSD / VFD) kontrol edilmesi, kısmi yükte sistem S_gen'ini önemli ölçüde azaltır:

- Kule fanı VSD: Tam yük yerine kısmi yükte fan gücü P_fan ∝ n³ (küp yasası) → %50 hızda %87.5 güç tasarrufu
- Kondenser suyu pompası VSD: Kısmi yükte debi azaltılarak pompa S_gen düşürülür
- Chiller kompresörü VSD: Kapasiteye uyum → on/off çevrimleri yerine sürekli optimum çalışma

---

## 8. Pratik Mühendislik Kuralları (Practical Engineering Rules)

**Fiziksel Sezgi:** Aşağıdaki kurallar, onlarca yıllık endüstriyel deneyim ve sayısız EGM analizinin kristalize edilmiş sonuçlarıdır. Her bir kural, arkasındaki termodinamik mekanizmayı yansıtır ve hızlı mühendislik kararları için rehber niteliğindedir.

### Kural 1: Genleşme vanası #1 entropi kaynağıdır
Çevrim S_gen'inin %30-40'ı genleşme vanasından gelir. Ejektör veya alt soğutucu (subcooling) sistemi eklemeyi değerlendir. ROI genellikle 2-4 yıl arasındadır.

### Kural 2: Temiz kondenser kritiktir
Kondenser kirlenme (fouling) S_gen'i %20-40 artırabilir. Kirlenme, yoğuşma sıcaklığını yükselterek hem kondenser S_gen'ini hem de kompresör S_gen'ini artırır. Düzenli temizlik en düşük maliyetli EGM iyileştirmesidir.

### Kural 3: Her 1°C düşük yoğuşma sıcaklığı → %2-3 COP artışı
Yoğuşma sıcaklığını düşürmek (daha büyük kondenser, daha temiz kondenser, daha düşük soğutma suyu sıcaklığı) doğrudan COP'u artırır ve toplam S_gen'i düşürür.

### Kural 4: Her 1°C yüksek buharlaşma sıcaklığı → %2-4 COP artışı
Buharlaşma sıcaklığını gereğinden düşük tutmak yaygın bir hatadır. Örneğin, 7°C chilled water gerektiren bir sistemde T_evap = -5°C yerine T_evap = 2°C çalışmak çok daha verimlidir. Gerekli soğutma seviyesini yeniden değerlendirin.

### Kural 5: Su soğutmalı her zaman hava soğutmalıdan iyidir (EGM perspektifinden)
Su soğutmalı kondenserlerde yaklaşım sıcaklığı (ΔT_approach) 3-5°C iken, hava soğutmalıda 8-12°C'dir. Bu, su soğutmalı sistemlerin kondenser S_gen'inin tipik olarak %40-60 daha düşük olduğu anlamına gelir.

### Kural 6: VSD kompresör kısmi yükte S_gen'i büyük ölçüde azaltır
Sabit hızlı kompresörler, kısmi yükte on/off çevrimleri veya slide valve ile kapasite kontrolü yapar — her ikisi de ek S_gen üretir. VSD kompresör, kapasiteyi yüke uyumlu şekilde ayarlayarak kısmi yükte S_gen'i %20-35 azaltır.

### Kural 7: Düşük sıcaklık uygulamalarında kademeli sıkıştırma düşün
T_evap < -20°C olan uygulamalarda (dondurulmuş gıda depolama, dondurma üretimi) tek kademeli sıkıştırmanın basınç oranı çok yüksektir → kompresör S_gen çok yüksek. İki kademeli sıkıştırma ile ara soğutma (intercooling), kompresör S_gen'ini %20-30 azaltır.

### Kural 8: Sistem düzeyinde düşün — bileşen düzeyinde değil
Tek bir bileşeni optimize etmek, sistemi kötüleştirebilir. Örneğin, evaporatörü daha büyük yapmak T_evap'ı artırır (iyi) ama evaporatör fan gücünü artırır (kötü). EGM her zaman toplam Ṡ_gen,sistem'i minimize etmelidir.

### Özet Tablo — Hızlı Referans:

| Önlem | S_gen Azaltımı | COP Artışı | Maliyet | Öncelik |
|-------|---------------|-----------|---------|---------|
| Kondenser temizliği | %10-25 | %5-15 | Çok düşük | 1 (ilk yapılacak) |
| T_evap optimizasyonu | %5-15 | %5-20 | Sıfır | 2 |
| VSD kompresör | %15-30 | %15-30 | Orta-Yüksek | 3 |
| Ekonomizer / subcooling | %8-15 | %5-10 | Düşük-Orta | 4 |
| Su soğutmaya geçiş | %20-40 | %15-30 | Yüksek | 5 (yeni tesis) |
| Ejektör | %10-20 | %5-15 | Orta | 6 |
| Kademeli sıkıştırma | %15-25 | %10-20 | Yüksek | 7 (düşük T uyg.) |
| Turbo-expander | %25-40 | %10-25 | Çok yüksek | 8 (CO₂ / büyük sist.) |

---

## İlgili Dosyalar (Related Files)

- `factory/entropy_generation/fundamentals.md` — Gouy-Stodola teoremi ve temel EGM kavramları
- `factory/entropy_generation/bejan_number.md` — Bejan sayısı ile irreversibility dağılımı
- `chiller/formulas.md` — Chiller exergy hesaplama formülleri
- `chiller/equipment/vapor_compression.md` — Buhar sıkıştırmalı chiller detayları
- `chiller/equipment/absorption.md` — Absorpsiyonlu chiller detayları
- `factory/entropy_generation/heat_transfer_egm.md` — Isı transferinde EGM
- `factory/cross_equipment.md` — Ekipmanlar arası enerji entegrasyonu (atık ısı → absorpsiyon chiller)

---

## Referanslar (References)

1. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press. — EGM'nin temel referans eseri, soğutma çevrimleri bölümü özellikle detaylı.

2. Bejan, A. (2006). *Advanced Engineering Thermodynamics*. 3rd ed., Wiley. — Soğutma ve ısı pompası çevrimlerinde entropi üretimi analizi.

3. Ahamed, J.U., Saidur, R., & Masjuki, H.H. (2011). "A review on exergy analysis of vapor compression refrigeration system." *Renewable and Sustainable Energy Reviews*, 15(3), 1593-1600.

4. Self, S.J., Reddy, B.V., & Rosen, M.A. (2013). "Geothermal heat pump systems: Status review and comparison with other heating options." *Applied Energy*, 101, 341-348.

5. Herold, K.E., Radermacher, R., & Klein, S.A. (2016). *Absorption Chillers and Heat Pumps*. 2nd ed., CRC Press. — Absorpsiyon çevrimlerinin exergy ve entropi analizi.

6. ASHRAE Handbook — Fundamentals (2021). Chapter 2: Thermodynamics and Refrigeration Cycles. — Endüstri standardı referans.

7. Dinçer, İ. & Kanoğlu, M. (2010). *Refrigeration Systems and Applications*. 2nd ed., Wiley. — Soğutma sistemlerinin exergy analizi, Türk yazarlar.

8. Çengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*. 9th ed., McGraw-Hill. — Bölüm 11: Soğutma çevrimleri ve ikinci yasa analizi.
