---
title: "Sonlu Zamanlı Termodinamik (Finite-Time Thermodynamics)"
category: factory
equipment_type: factory
keywords: [sonlu zamanlı termodinamik, Curzon-Ahlborn, endoreversible, maksimum güç, Carnot, verim-güç trade-off]
related_files: [factory/entropy_generation/fundamentals.md, factory/entropy_generation/overview.md, factory/entropy_generation/power_cycles_egm.md]
use_when: ["Gerçek çevrim verimleri değerlendirilecekken", "Carnot vs gerçek verim karşılaştırması yapılacakken", "Maksimum güç noktası analiz edilecekken"]
priority: medium
last_updated: 2026-02-01
---

# Sonlu Zamanlı Termodinamik (Finite-Time Thermodynamics)

Klasik termodinamik, tersinir (reversible) süreçlerin sonsuz yavaş gerçekleştiğini varsayar.
Ancak gerçek endüstriyel tesisler sonlu boyutlu ekipmanlarla, sonlu zamanda çalışır.
Sonlu zamanlı termodinamik, bu gerçekliği matematiksel olarak modelleyerek
mühendislere ulaşılabilir verim sınırları sunar.

---

## 1. Giriş: Carnot'nun Sınırları

### 1.1 Carnot Verimi — İdeal ama Erişilemez

Termodinamiğin en temel sonuçlarından biri, iki sıcaklık kaynağı arasında çalışan
bir ısı makinesinin maksimum veriminin Carnot verimi ile sınırlı olduğudur.

**Fiziksel sezgi:** Carnot çevrimi, tüm süreçlerin tersinir olduğunu varsayar.
Tersinir bir ısı transferi için sıcaklık farkının sıfıra yaklaşması gerekir (ΔT → 0).
Ancak ΔT → 0 olduğunda ısı transfer hızı da sıfıra yaklaşır (Q̇ → 0),
dolayısıyla üretilen güç de sıfıra gider (Ẇ → 0). Bu, Carnot'nun temel paradoksudur:
maksimum verim ancak sıfır güç çıkışında elde edilir.

**Carnot verimi formülü:**

```
η_Carnot = 1 - T_C / T_H
```

Burada:
- T_H = Sıcak kaynak sıcaklığı (K)
- T_C = Soğuk kaynak sıcaklığı (K)
- Sıcaklıklar mutlaka Kelvin cinsinden olmalıdır

**"Maksimum verim, sıfır güçte" paradoksu:**

Carnot çevriminde tüm süreçler kuasi-statik (quasi-static) olduğundan, bir çevrimin
tamamlanması sonsuz zaman alır. Sonuç olarak:

- Çevrim başına iş (W_net) sonlu bir değerdir
- Ancak çevrim süresi → ∞ olduğundan
- Güç = W_net / t_çevrim → 0

Bu, gerçek bir enerji santralinin asla Carnot verimine ulaşamayacağı anlamına gelir.
Gerçek tesislerde sonlu boyutlu ısı eşanjörleri, sonlu zamanda ısı transferi yapar
ve bu kaçınılmaz olarak entropi üretir.

### 1.2 Neden Sonlu Zamanlı Termodinamik?

Klasik termodinamik şu soruyu yanıtlar: "Teorik maksimum verim nedir?"
Sonlu zamanlı termodinamik ise şu soruyu yanıtlar: "Gerçekçi koşullarda ulaşılabilir
maksimum verim nedir?"

**Sonlu zamanlı termodinamiğin köprü rolü:**

```
Klasik Termodinamik          Sonlu Zamanlı Termodinamik          Gerçek Mühendislik
(İdeal, tersinir)      →     (Endoreversible, sonlu ΔT)     →   (Tüm kayıplar dahil)
η_Carnot = %64              η_CA = %40                          η_Gerçek = %35
Güç = 0 kW                  Güç = Maksimum                      Güç = Tasarım değeri
```

Sonlu zamanlı termodinamik şu faktörleri hesaba katar:
- Sonlu ısı transfer hızları (finite heat transfer rates)
- Sonlu boyutlu ısı eşanjörleri (finite-size heat exchangers)
- Sonlu çevrim süreleri (finite cycle times)
- Isı transfer alanı ve maliyet kısıtları

---

## 2. Curzon-Ahlborn Verimi (CA Efficiency)

### 2.1 Endoreversible Model

1975 yılında Curzon ve Ahlborn tarafından geliştirilen bu model, sonlu zamanlı
termodinamiğin temel taşıdır.

**Fiziksel sezgi:** Endoreversible (iç-tersinir) model, çevrim içindeki tüm süreçlerin
tersinir olduğunu kabul eder. Tek tersinmezlik kaynağı, ısı kaynaklarıyla çalışma
akışkanı arasındaki ısı eşanjörlerindeki sonlu sıcaklık farkıdır. Bu model,
gerçekliğin şaşırtıcı derecede iyi bir yaklaşımıdır çünkü endüstriyel sistemlerdeki
en büyük entropi üretimi genellikle ısı transfer süreçlerinde gerçekleşir.

**Endoreversible model şeması (text-based):**

```
   T_H (Sıcak Kaynak, sabit)
    │
    │  Q̇_H = (UA)_H × (T_H - T_HW)       ← Sonlu ΔT (irreversible)
    │
    ▼
   T_HW (Çalışma akışkanı, sıcak taraf)
    │
    │  Tersinir Carnot Çevrimi              ← İç süreçler reversible
    │  η_iç = 1 - T_CW / T_HW
    │
    ▼
   T_CW (Çalışma akışkanı, soğuk taraf)
    │
    │  Q̇_C = (UA)_C × (T_CW - T_C)       ← Sonlu ΔT (irreversible)
    │
    ▼
   T_C (Soğuk Kaynak, sabit)
```

Burada:
- T_H = Sıcak kaynak sıcaklığı (K) — sabit
- T_HW = Çalışma akışkanının sıcak taraftaki sıcaklığı (K) — optimize edilecek
- T_CW = Çalışma akışkanının soğuk taraftaki sıcaklığı (K) — optimize edilecek
- T_C = Soğuk kaynak sıcaklığı (K) — sabit
- (UA)_H = Sıcak taraf ısı eşanjörü iletkenliği (kW/K)
- (UA)_C = Soğuk taraf ısı eşanjörü iletkenliği (kW/K)

**Anahtar nokta:** T_HW < T_H ve T_CW > T_C olmak zorundadır, aksi takdirde
ısı transferi gerçekleşmez. Bu zorunlu sıcaklık farkları, kaçınılmaz entropi üretir.

### 2.2 Türetme (Derivation)

Curzon-Ahlborn veriminin adım adım türetilmesi:

**Adım 1: Isı transfer denklemleri**

**Fiziksel sezgi:** Newton'un soğuma yasasına göre, ısı transfer hızı sıcaklık farkıyla
orantılıdır. Büyük sıcaklık farkı → hızlı ısı transferi → yüksek güç, ama düşük verim.

Sıcak taraf ısı transferi:
```
Q̇_H = (UA)_H × (T_H - T_HW)                    ... (1)
```

Soğuk taraf ısı transferi:
```
Q̇_C = (UA)_C × (T_CW - T_C)                    ... (2)
```

**Adım 2: İç Carnot verimi**

**Fiziksel sezgi:** Çalışma akışkanı, T_HW ve T_CW sıcaklıkları arasında tersinir
bir Carnot çevrimi gerçekleştirir. Bu iç çevrimin verimi, Carnot formülüne uyar
ancak kaynak sıcaklıkları yerine çalışma akışkanı sıcaklıklarını kullanır.

```
η_iç = 1 - T_CW / T_HW                          ... (3)
```

**Adım 3: Güç ifadesi**

**Fiziksel sezgi:** Güç çıkışı, sıcak taraftan alınan ısı ile iç Carnot veriminin
çarpımıdır. Amacımız bu güçü maksimize eden T_HW ve T_CW değerlerini bulmaktır.

```
Ẇ = Q̇_H × η_iç = (UA)_H × (T_H - T_HW) × (1 - T_CW / T_HW)    ... (4)
```

**Adım 4: Enerji dengesi (iç tersinirlik koşulu)**

**Fiziksel sezgi:** İç çevrim tersinir olduğundan, çevrime giren entropi akışı
çevrinden çıkan entropi akışına eşittir. Bu koşul, T_HW ve T_CW arasında
bir bağıntı kurar ve problemi tek değişkenli hale getirir.

Tersinir çevrim entropi dengesi:
```
Q̇_H / T_HW = Q̇_C / T_CW                       ... (5)
```

Denklem (1) ve (2)'yi (5)'e yerleştirirsek:
```
(UA)_H × (T_H - T_HW) / T_HW = (UA)_C × (T_CW - T_C) / T_CW    ... (6)
```

**Adım 5: Simetrik durum için sadeleştirme**

Türetmeyi netleştirmek için (UA)_H = (UA)_C = UA varsayalım (simetrik ısı eşanjörleri):

```
(T_H - T_HW) / T_HW = (T_CW - T_C) / T_CW
```

Bu ifade şu şekilde düzenlenir:
```
T_H / T_HW - 1 = 1 - T_C / T_CW
```
```
T_H / T_HW + T_C / T_CW = 2                     ... (7)
```

**Adım 6: Güç maksimizasyonu**

**Fiziksel sezgi:** Gücü maksimize etmek için, güç ifadesinin T_HW'ye (veya
eşdeğer olarak x = T_CW / T_HW oranına) göre türevini alıp sıfıra eşitleriz.
Bu, verimi artırmanın (T_HW → T_H) güç çıkışını azaltması ile güç çıkışını
artırmanın (büyük ΔT) verimi düşürmesi arasındaki optimal dengeyi bulur.

x = T_CW / T_HW oranını tanımlayalım. Güç fonksiyonu:
```
Ẇ = UA × (T_H - T_HW) × (1 - x)
```

Denklem (7) kısıtı altında optimizasyon yapıldığında:
```
∂Ẇ/∂T_HW = 0
```

Çözüm, optimal çalışma akışkanı sıcaklıklarını verir:
```
T_HW_opt = √(T_H × T_C) × √(T_H / T_C)^(1/2) = T_H^(3/4) × T_C^(1/4) / (bazı faktör)
```

Simetrik durum için daha temiz bir ifade:
```
T_HW_opt = √(T_H) × ( √(T_H) + √(T_C) ) / 2     (yaklaşık)
T_CW_opt = √(T_C) × ( √(T_H) + √(T_C) ) / 2     (yaklaşık)
```

**Adım 7: Optimal verim — Curzon-Ahlborn formülü**

Optimal sıcaklıkları iç Carnot verimine yerleştirdiğimizde:
```
η_CA = 1 - T_CW_opt / T_HW_opt = 1 - √(T_C / T_H)
```

**Sonuç — Curzon-Ahlborn Verimi:**

```
┌─────────────────────────────────────────────┐
│                                             │
│   η_CA = 1 - √(T_C / T_H)                 │
│                                             │
│   T_C, T_H: Kelvin cinsinden               │
│   Maksimum güç noktasındaki verim           │
│                                             │
└─────────────────────────────────────────────┘
```

**Fiziksel anlam:** Curzon-Ahlborn verimi, Carnot veriminin karekökü ile ilişkilidir.
Carnot verimi η_C = 1 - T_C/T_H iken, CA verimi η_CA = 1 - √(T_C/T_H) olup
her zaman Carnot'dan düşüktür: η_CA < η_Carnot.

### 2.3 Sayısal Karşılaştırma

Aşağıdaki tablo, farklı tesis tipleri için Carnot, Curzon-Ahlborn ve gerçek verimleri
karşılaştırmaktadır. T_C = 25°C = 298 K olarak alınmıştır.

| Tesis Tipi               | T_H (°C) | T_H (K) | T_C (°C) | η_Carnot (%) | η_CA (%) | η_Gerçek (%) | η_Gerçek/η_CA |
|---------------------------|-----------|---------|-----------|---------------|----------|---------------|----------------|
| Kömür santrali            | 550       | 823     | 25        | 63.8          | 39.8     | 33-38         | 0.83-0.95      |
| Gaz türbini (basit)      | 1200      | 1473    | 25        | 79.8          | 55.0     | 30-38         | 0.55-0.69      |
| Kombine çevrim (CCGT)    | 1200      | 1473    | 25        | 79.8          | 55.0     | 55-62         | 1.00-1.13*     |
| Nükleer (PWR)            | 330       | 603     | 25        | 50.6          | 29.7     | 32-34         | 1.08-1.14*     |
| Jeotermal (flash)        | 300       | 573     | 25        | 48.0          | 27.8     | 20-25         | 0.72-0.90      |
| Jeotermal (binary/ORC)   | 150       | 423     | 25        | 29.6          | 16.1     | 10-14         | 0.62-0.87      |
| ORC (düşük sıcaklık)     | 100       | 373     | 25        | 20.1          | 10.6     | 6-10          | 0.57-0.94      |
| Atık ısı geri kazanımı   | 80        | 353     | 25        | 15.6          | 7.9      | 4-7           | 0.51-0.89      |
| Biyokütle kazanı          | 450       | 723     | 25        | 58.8          | 35.8     | 25-30         | 0.70-0.84      |
| Güneş termal (parabolik) | 400       | 673     | 25        | 55.7          | 33.4     | 20-25         | 0.60-0.75      |
| Dizel motoru              | 600       | 873     | 25        | 65.9          | 41.6     | 35-45         | 0.84-1.08*     |

(*) η_Gerçek/η_CA > 1 olan durumlar: Kombine çevrimler ve dizel motorları gibi
sistemlerde iç tersinmezlik etkisi az olduğunda veya çok kademeli çevrim
kullanıldığında CA verimini aşmak mümkündür. Bu, endoreversible modelin sınırlarını
gösterir — model sadece ısı transfer tersinmezliklerini dikkate alır.

**Sayısal Örnek — Kömür Santrali:**

Bir kömür santrali T_H = 550°C = 823 K, T_C = 25°C = 298 K'de çalışmaktadır.

```
η_Carnot = 1 - 298/823 = 1 - 0.362 = 0.638 = %63.8
η_CA    = 1 - √(298/823) = 1 - √(0.362) = 1 - 0.602 = 0.398 = %39.8
η_Gerçek ≈ %36 (tipik modern kömür santrali)

η_Gerçek / η_Carnot = 0.36 / 0.638 = 0.564 → Carnot'un %56.4'ü
η_Gerçek / η_CA    = 0.36 / 0.398 = 0.905 → CA'nın %90.5'i
```

Bu sonuç önemlidir: Gerçek verim Carnot'un sadece %56'sı gibi görünürken,
CA veriminin %90'ından fazlasına ulaşılmaktadır. Bu, tesisin aslında oldukça
iyi optimize edildiğini gösterir.

---

## 3. Maksimum Güç vs Maksimum Verim Trade-off

### 3.1 Güç-Verim Eğrisi

**Fiziksel sezgi:** Bir ısı makinesi iki aşırı uç arasında çalışabilir:
(a) Carnot verimi — sıfır güç çıkışı, veya (b) sıfır verim — sıfır güç çıkışı
(tüm ısı doğrudan geçer). Her iki uçta da güç sıfırdır. Arada bir maksimum
güç noktası vardır ve bu nokta CA verimine karşılık gelir.

**Güç-Verim eğrisi (text-based):**

```
Güç (kW)
  │
  │            ╭──── Maksimum Güç Noktası
  │           ╱╲     (η ≈ η_CA)
  │          ╱  ╲
  │         ╱    ╲
  │        ╱      ╲        ← Tipik çalışma bölgesi
  │       ╱        ╲
  │      ╱          ╲
  │     ╱            ╲
  │    ╱              ╲
  │   ╱                ╲
  │  ╱                  ╲
  │ ╱                    ╲
  │╱                      ╲
  ├────────────────────────────── Verim (η)
  0          η_CA       η_Carnot

  Güç = 0    Güç = Max   Güç = 0
  η = 0      η = η_CA    η = η_Carnot
```

**Çalışma bölgeleri:**

| Bölge              | Verim Aralığı        | Güç Durumu       | Uygun Tesis Tipi         |
|---------------------|----------------------|------------------|--------------------------|
| Düşük verim         | 0 < η < η_CA/2      | Düşük güç        | Nadiren tercih edilir     |
| Maksimum güç civari | η_CA/2 < η < η_CA   | Yüksek güç       | Baz yük santralleri       |
| Optimal bölge       | η_CA < η < 0.8×η_C  | Orta-yüksek güç  | Yakıt maliyeti yüksek ise |
| Yüksek verim        | 0.8×η_C < η < η_C   | Düşük güç        | Pahalı yakıt, düşük talep |

### 3.2 Entropi Üretim Hızı (Ṡ_gen) ve Güç İlişkisi

**Fiziksel sezgi:** Sıfır entropi üretimi tersinir sürece, yani Carnot çevrimine
karşılık gelir — ama güç çıkışı sıfırdır. Entropi üretimi arttıkça güç artar
(çünkü ısı daha hızlı transfer edilir), ancak bir noktadan sonra tersinmezlikler
o kadar büyür ki güç düşmeye başlar. Dolayısıyla optimal bir entropi üretim hızı
vardır — ve bu sıfır değildir!

```
Ṡ_gen → 0      →  η → η_Carnot,  Ẇ → 0           (tersinir limit)
Ṡ_gen = optimal →  η ≈ η_CA,      Ẇ = Ẇ_max       (maksimum güç)
Ṡ_gen → ∞      →  η → 0,          Ẇ → 0           (tamamen tersinmez)
```

**Güç — Entropi üretimi ilişkisi:**

**Fiziksel sezgi:** Gouy-Stodola teoremi, kayıp gücün çevre sıcaklığı ile entropi
üretim hızının çarpımına eşit olduğunu söyler. Bu teorem, entropi üretiminin
doğrudan ekonomik kayba dönüştürülmesini sağlar.

```
Ẇ_kayıp = T_0 × Ṡ_gen                            (Gouy-Stodola teoremi)
```

Burada:
- Ẇ_kayıp = Tersinmezliklerden dolayı kaybedilen güç (kW)
- T_0 = Çevre sıcaklığı (K), genellikle 298 K
- Ṡ_gen = Entropi üretim hızı (kW/K)

**Sayısal Örnek:**

Bir santralde Ṡ_gen = 50 kW/K ve T_0 = 298 K ise:
```
Ẇ_kayıp = 298 × 50 = 14 900 kW = 14.9 MW
```
Bu, santralin tersinmezlikler nedeniyle 14.9 MW güç kaybettiği anlamına gelir.

### 3.3 Optimal Çalışma Noktası

**Fiziksel sezgi:** Ekonomik optimum, termodinamik optimumdan farklıdır.
Yakıt maliyeti yüksekse verim önemlidir (η_CA'dan yukarı çalış).
Sermaye maliyeti yüksekse güç çıkışı önemlidir (η_CA civarında çalış).
Elektrik fiyatı yüksekse mümkün olduğunca çok güç üret.

**Ekonomik optimizasyon fonksiyonu:**

```
Kâr = (Ẇ × e_fiyat) - (Q̇_H × c_yakıt) - (C_yatırım / t_ömür)
```

Burada:
- e_fiyat = Elektrik satış fiyatı ($/kWh)
- c_yakıt = Yakıt birim maliyeti ($/kWh_termal)
- C_yatırım = Toplam yatırım maliyeti ($)
- t_ömür = Tesis ekonomik ömrü (saat)

**Farklı senaryolarda optimal çalışma noktaları:**

| Senaryo                        | Optimal Verim Bölgesi   | Açıklama                            |
|---------------------------------|-------------------------|--------------------------------------|
| Ucuz yakıt, pahalı yatırım     | η ≈ η_CA               | Maksimum güç, hızlı amortisman      |
| Pahalı yakıt, ucuz yatırım     | η_CA < η < η_Carnot    | Yüksek verim, yakıt tasarrufu       |
| Baz yük santrali                | η ≈ η_CA               | Sürekli yüksek güç çıkışı           |
| Pik yük santrali                | η < η_CA (kısa süre)   | Hızlı devreye girme öncelikli       |
| CHP (kojenerasyon) sistemi      | η_CA < η < 0.85×η_C    | Toplam enerji kullanımı optimize     |

---

## 4. Feidt'in Fiziksel Boyut Modeli

### 4.1 Sonlu Fiziksel Boyutlu Termodinamik (Finite Physical Dimensions Thermodynamics)

**Fiziksel sezgi:** Curzon-Ahlborn modeli sonsuz boyutlu ısı eşanjörleri varsayar
ve sadece sıcaklık farklarını kısıtlar. Feidt'in modeli, ısı eşanjörlerinin gerçek
fiziksel boyutlarını (UA değerlerini) açıkça hesaba katar. Bu, maliyet optimizasyonu
ile termodinamik optimizasyonu birleştirir.

**Model parametreleri:**

```
Tasarım değişkenleri:  (UA)_H, (UA)_C, T_HW, T_CW
Kısıtlamalar:          (UA)_H + (UA)_C = (UA)_toplam = sabit
Amaç fonksiyonu:       Ẇ_max veya η_max veya (Ẇ/Maliyet)_max
```

**Fiziksel sezgi:** Toplam ısı eşanjörü alanı (veya UA değeri) sabit tutulduğunda,
bu alanın sıcak ve soğuk taraf arasında nasıl dağıtılacağı kritik bir tasarım
kararıdır. Eşit dağılım her zaman optimal değildir.

### 4.2 Üç Boyutlu Optimizasyon

Feidt'in modeli üç boyutlu bir trade-off yüzeyi tanımlar:

**Fiziksel sezgi:** Mühendisler üç rakip hedefle karşı karşıyadır: yüksek güç,
yüksek verim ve küçük (ucuz) ekipman. Herhangi ikisini iyileştirmek genellikle
üçüncüsünü kötüleştirir.

```
                    Yüksek Güç (Ẇ_max)
                         ╱╲
                        ╱  ╲
                       ╱    ╲
                      ╱ OPT  ╲         ← Optimal çalışma noktası
                     ╱  BÖLGE ╲          (trade-off yüzeyinde)
                    ╱──────────╲
   Yüksek Verim ──╱──────────────╲── Küçük Boyut
   (η_max)                             ((UA)_min)
```

**Optimal UA dağılımı formülü:**

**Fiziksel sezgi:** Isı eşanjörü alanının sıcak ve soğuk taraf arasındaki dağılımı,
kaynak sıcaklıklarının oranına bağlıdır. Sıcak taraftaki sıcaklık farkı büyükse,
soğuk taraf eşanjörüne daha fazla alan ayırmak mantıklıdır ve tersi.

```
(UA)_H_opt / (UA)_C_opt = √(T_C / T_H)           (simetrik optimum için)
```

**Sayısal Örnek — Optimal UA Dağılımı:**

T_H = 823 K (550°C), T_C = 298 K (25°C), (UA)_toplam = 500 kW/K

```
Oran = √(298/823) = √(0.362) = 0.602

(UA)_H = 500 × 0.602 / (1 + 0.602) = 500 × 0.376 = 188 kW/K
(UA)_C = 500 - 188 = 312 kW/K
```

Yani soğuk taraf eşanjörüne daha fazla alan ayrılmalıdır (%62.4 vs %37.6).

---

## 5. Endoreversible Modelin Genişletilmesi

### 5.1 İç Tersinmezlik Eklenmesi (Internal Irreversibility Factor)

**Fiziksel sezgi:** Gerçek çevrimlerde sadece ısı eşanjörlerinde değil, çevrimin
içinde de tersinmezlikler vardır: sürtünme, karışma, sonlu hızlı genleşme/sıkıştırma,
vana kayıpları gibi. Bu iç tersinmezlikler, φ < 1 olan bir düzeltme faktörü ile
modellenebilir.

**Modifiye edilmiş entropi dengesi:**

```
Q̇_H / T_HW = φ × Q̇_C / T_CW        (φ < 1: iç tersinmezlik faktörü)
```

Burada φ = 1 ise endoreversible (CA modeli), φ < 1 ise iç kayıplar dahil.

**Modifiye Curzon-Ahlborn verimi:**

```
η_mod = 1 - √(T_C / (φ × T_H))
```

**Tipik φ değerleri:**

| Sistem Tipi               | φ Değeri    | Açıklama                                |
|----------------------------|-------------|------------------------------------------|
| Modern buhar türbini       | 0.95-0.98   | Düşük iç kayıp                          |
| Gaz türbini                | 0.90-0.95   | Orta düzey iç kayıp                     |
| Dizel motoru               | 0.85-0.92   | Sürtünme ve yanma kayıpları             |
| Küçük ölçekli ORC          | 0.80-0.90   | Ekspander verimsizlikleri               |
| Stirling motoru            | 0.75-0.88   | Rejeneratör ve sürtünme kayıpları       |

**Sayısal Örnek — İç Tersinmezlik Etkisi:**

Bir gaz türbini: T_H = 1473 K (1200°C), T_C = 298 K, φ = 0.92

```
η_CA  = 1 - √(298/1473) = 1 - √(0.2023) = 1 - 0.4498 = %55.0
η_mod = 1 - √(298/(0.92 × 1473)) = 1 - √(298/1355) = 1 - √(0.2199) = 1 - 0.469 = %53.1
```

φ'nin 1.00'den 0.92'ye düşmesi, verimi %55.0'den %53.1'e düşürmüştür (1.9 puan).

### 5.2 Çok Kaynaklı Sistemler (Multi-Source Systems)

**Fiziksel sezgi:** Endüstriyel tesislerde genellikle tek bir sıcak kaynak yerine
farklı sıcaklıklarda birden fazla atık ısı kaynağı bulunur. Bunların kademeli
(cascade) olarak kullanılması, tek kaynağa göre çok daha yüksek toplam güç ve
verim sağlar.

**İki kaynaklı sistem modeli:**

```
T_H1 (yüksek sıcaklık kaynağı, örn. baca gazı 400°C)
  │
  ▼
Çevrim 1 (η₁ ≈ η_CA₁)  →  Ẇ₁
  │
  ▼ Atık ısı (T_ara ≈ 150-200°C)
  │
T_H2 (düşük sıcaklık kaynağı, örn. proses atığı 120°C)
  │
  ▼
Çevrim 2 (η₂ ≈ η_CA₂)  →  Ẇ₂
  │
  ▼
T_C (soğuk kaynak, 25°C)

Toplam güç: Ẇ_toplam = Ẇ₁ + Ẇ₂ > Ẇ_tek_kademe
```

**Kademeli kullanımın avantajı:**

Bir fabrikada 300°C baca gazı ve 100°C proses atık ısısı varsa:

Tek kademeli (sadece baca gazı kullanımı):
```
η_CA = 1 - √(298/573) = 1 - 0.721 = %27.9
```

İki kademeli:
```
Kademe 1: η_CA₁ = 1 - √(298/573) = %27.9 (baca gazından güç)
Kademe 2: η_CA₂ = 1 - √(298/373) = %10.6 (atık ısıdan ek güç)
```

İki kademeli sistem, tek kademeye göre %25-40 daha fazla toplam güç üretebilir.

---

## 6. Gerçek Tesislerde Karşılaştırma Tablosu

Aşağıdaki kapsamlı tablo, dünya genelindeki farklı tesis tiplerinin gerçek verimlerini
Carnot ve CA verimleriyle karşılaştırmaktadır.

| #  | Tesis Tipi                        | T_H (°C) | T_C (°C) | η_Carnot (%) | η_CA (%) | η_Gerçek (%) | η_G/η_CA | Değerlendirme                |
|----|-----------------------------------|-----------|-----------|---------------|----------|---------------|-----------|-------------------------------|
| 1  | Ultra-süperkritik kömür santrali  | 600       | 25        | 65.9          | 41.6     | 42-47         | 1.01-1.13 | CA'yı aşar (çok kademeli)    |
| 2  | Süperkritik kömür santrali        | 550       | 25        | 63.8          | 39.8     | 38-42         | 0.95-1.06 | CA civarında                  |
| 3  | Subkritik kömür santrali          | 500       | 25        | 61.5          | 37.7     | 33-37         | 0.88-0.98 | İyi optimize edilmiş          |
| 4  | Gaz türbini (basit çevrim)        | 1200      | 25        | 79.8          | 55.0     | 30-38         | 0.55-0.69 | İç kayıplar baskın            |
| 5  | Kombine çevrim (CCGT)             | 1200      | 25        | 79.8          | 55.0     | 55-63         | 1.00-1.15 | İki kademeli avantaj          |
| 6  | Nükleer (PWR)                     | 330       | 25        | 50.6          | 29.7     | 32-34         | 1.08-1.14 | Düşük iç kayıp               |
| 7  | Nükleer (BWR)                     | 290       | 25        | 47.1          | 27.3     | 30-32         | 1.10-1.17 | Düşük iç kayıp               |
| 8  | Jeotermal (dry steam)             | 250       | 25        | 43.0          | 24.5     | 18-22         | 0.73-0.90 | Düşük sıcaklık sınırı        |
| 9  | Jeotermal (flash)                 | 200       | 25        | 37.0          | 20.7     | 12-16         | 0.58-0.77 | Önemli iyileşme potansiyeli   |
| 10 | ORC (orta sıcaklık)               | 200       | 25        | 37.0          | 20.7     | 14-18         | 0.68-0.87 | Akışkan seçimi kritik         |
| 11 | ORC (düşük sıcaklık)              | 100       | 25        | 20.1          | 10.6     | 6-10          | 0.57-0.94 | Sıcaklık farkı çok düşük     |
| 12 | Atık ısı (80°C kaynak)            | 80        | 25        | 15.6          | 7.9      | 4-7           | 0.51-0.89 | Ekonomik fizibilite sınırında |
| 13 | Güneş termal (tower)              | 600       | 25        | 65.9          | 41.6     | 22-28         | 0.53-0.67 | Güneş toplayıcı kayıpları    |
| 14 | Güneş termal (parabolik)          | 400       | 25        | 55.7          | 33.4     | 20-25         | 0.60-0.75 | Optik kayıplar dahil          |
| 15 | Biyokütle (direkt yanma)          | 450       | 25        | 58.8          | 35.8     | 22-28         | 0.61-0.78 | Nem ve kül etkisi             |

**Tablo yorumu — Kritik çıkarımlar:**

1. **η_Gerçek/η_CA ≥ 0.90:** Tesis iyi optimize edilmiştir, daha fazla iyileşme
   zordur (kömür santralleri, nükleer).

2. **0.70 ≤ η_Gerçek/η_CA < 0.90:** Orta düzey iyileşme potansiyeli vardır.
   Isı eşanjörü büyütme, çok kademeli genleşme düşünülebilir.

3. **η_Gerçek/η_CA < 0.70:** Önemli iyileşme potansiyeli vardır. Sistem tasarımı
   gözden geçirilmeli, iç tersinmezlikler azaltılmalıdır.

4. **η_Gerçek/η_CA > 1.00:** Sistem CA modelinin varsayımlarını aşmıştır
   (çok kademeli çevrim, düşük iç kayıp). Bu, modelin sınırlarını gösterir.

---

## 7. Endüstriyel Sonuçlar ve Pratik Kurallar

### 7.1 Temel Pratik Kurallar

**Kural 1: CA verimi, gerçekçi üst sınırdır**

**Fiziksel sezgi:** Bir tesis için beklenen maksimum verimi tahmin ederken
Carnot değil, CA verimini kullanın. Carnot verimi yalnızca termodinamik bir sınırdır,
CA verimi ise mühendislik açısından anlamlı bir hedeftir.

```
Hızlı tahmin:  η_hedef ≈ 0.85 × η_CA
              = 0.85 × (1 - √(T_C/T_H))
```

**Kural 2: Verim oranı ile iyileşme potansiyeli**

| η_Gerçek / η_CA | Durum                    | Aksiyon                                |
|------------------|--------------------------|----------------------------------------|
| > 0.95           | Teorik limite çok yakın  | Farklı çevrim tipi veya T_H artışı    |
| 0.85 - 0.95      | İyi optimize             | Küçük iyileştirmeler (bakım, kontrol)  |
| 0.70 - 0.85      | Orta düzey               | Isı eşanjörü iyileştirme, sızıntı önl.|
| 0.50 - 0.70      | Önemli potansiyel        | Sistem yeniden tasarımı düşünülmeli    |
| < 0.50           | Ciddi sorunlar           | Acil müdahale gerekli                  |

**Kural 3: Düşük sıcaklık kaynakları için CA verimi hızla düşer**

**Fiziksel sezgi:** Kaynak sıcaklığı düştükçe CA verimi Carnot'tan çok daha hızlı
düşer. Bu, düşük sıcaklıklı atık ısı geri kazanımının neden ekonomik olarak zor
olduğunu açıklar.

```
T_H = 500°C:  η_Carnot = %61.5,  η_CA = %37.7  (fark: 23.8 puan)
T_H = 200°C:  η_Carnot = %37.0,  η_CA = %20.7  (fark: 16.3 puan)
T_H = 100°C:  η_Carnot = %20.1,  η_CA = %10.6  (fark: 9.5 puan)
T_H = 60°C:   η_Carnot = %10.5,  η_CA = %5.2   (fark: 5.3 puan)
```

60°C'nin altındaki atık ısı kaynaklarından güç üretimi ekonomik olarak genellikle
uygun değildir (η_CA < %5).

### 7.2 Atık Isı Geri Kazanımında CA Verimi Kullanımı

**Fiziksel sezgi:** Bir fabrikadaki atık ısı kaynağından ne kadar güç üretilebileceğini
hızlıca tahmin etmek için CA verimi kullanılabilir.

**Hızlı tahmin formülü:**

```
Ẇ_elde_edilebilir ≈ 0.85 × η_CA × Q̇_atık
                   = 0.85 × (1 - √(T_C/T_H)) × Q̇_atık
```

**Sayısal Örnek — Fabrika Atık Isı Değerlendirmesi:**

Bir gıda fabrikasında 150°C'de 2000 kW atık ısı mevcuttur. T_çevre = 25°C.

```
η_CA = 1 - √(298/423) = 1 - √(0.705) = 1 - 0.839 = %16.1

Ẇ_maks = η_CA × Q̇_atık = 0.161 × 2000 = 322 kW    (teorik maksimum)
Ẇ_gerçekçi = 0.85 × 322 = 274 kW                     (gerçekçi tahmin)
Ẇ_muhafazakâr = 0.70 × 322 = 225 kW                  (muhafazakâr tahmin)
```

Yıllık tasarruf (7500 saat/yıl, 0.10 $/kWh):
```
Yıllık tasarruf_gerçekçi = 274 × 7500 × 0.10 = 205 500 $/yıl
```

Bu tahmin, fizibilite çalışması başlatmak için yeterli bir ön değerlendirmedir.

### 7.3 CHP (Kojenerasyon) Sistemlerinde Uygulama

**Fiziksel sezgi:** CHP sistemlerinde sadece güç değil, atık ısı da faydalı bir
çıktıdır. Bu durumda, güç verimini biraz düşürerek toplam enerji kullanım verimini
önemli ölçüde artırmak mümkündür.

```
CHP Verimi (Toplam) = (Ẇ + Q̇_faydalı) / Q̇_H

CHP Exergy Verimi = (Ẇ + Q̇_faydalı × ψ_ısı) / (Q̇_H × ψ_yakıt)
```

Burada ψ_ısı = 1 - T_0/T_ısı (ısının exergy faktörü), tipik olarak 0.10-0.30
aralığındadır.

CHP sistemleri CA veriminin altında güç verimi ile çalışabilir ancak toplam
exergy verimi daha yüksek olabilir.

### 7.4 Karar Ağacı — Tesis Değerlendirmesi

Aşağıdaki karar ağacı, bir endüstriyel tesisin sonlu zamanlı termodinamik
açısından değerlendirilmesini sistematize eder:

```
                        Tesis Analizi
                             │
                ┌────────────┼────────────┐
                │            │            │
          η_G/η_CA > 0.9  0.7-0.9     < 0.7
                │            │            │
         Limit yakın    Orta düzey    İyileşme var
                │            │            │
          ┌─────┘       ┌────┘        ┌───┘
          │             │             │
   T_H artırılabilir  HX iyileştir  Sistem yeniden
   mi? Çevrim tipi    İç kayıpları   tasarla.
   değiştir. Çok      azalt.         İç + dış
   kademeli düşün.    Bakım kontrol  tersinmezlikleri
                      et.             analiz et.
```

---

## İlgili Dosyalar

- [`factory/entropy_generation/fundamentals.md`](fundamentals.md) — Entropi üretimi temel kavramları
- [`factory/entropy_generation/overview.md`](overview.md) — Entropi üretimi minimizasyonu genel bakış
- [`factory/entropy_generation/power_cycles_egm.md`](power_cycles_egm.md) — Güç çevrimlerinde entropi üretimi minimizasyonu
- [`factory/cross_equipment.md`](../cross_equipment.md) — Ekipmanlar arası enerji entegrasyonu
- [`factory/prioritization.md`](../prioritization.md) — İyileştirme önceliklendirmesi

---

## Referanslar

1. Curzon, F.L., Ahlborn, B. "Efficiency of a Carnot Engine at Maximum Power Output,"
   *American Journal of Physics*, 43(1), 22-24, 1975.

2. Novikov, I.I. "The Efficiency of Atomic Power Stations,"
   *Journal of Nuclear Energy II*, 7(1-2), 125-128, 1958.
   (1957'de Rusça olarak yayımlanmış bağımsız türetme)

3. Bejan, A. *Entropy Generation Minimization*,
   CRC Press, Boca Raton, FL, 1996.

4. Bejan, A. *Advanced Engineering Thermodynamics*, 4th Edition,
   John Wiley & Sons, 2016.

5. Feidt, M. *Finite Physical Dimensions Optimal Thermodynamics 1:
   Fundamentals*, ISTE Press / Elsevier, 2017.

6. De Vos, A. *Endoreversible Thermodynamics of Solar Energy Conversion*,
   Oxford University Press, 1992.

7. Andresen, B. "Current Trends in Finite-Time Thermodynamics,"
   *Angewandte Chemie International Edition*, 50(12), 2690-2704, 2011.

8. Chen, L., Wu, C., Sun, F. "Finite Time Thermodynamic Optimization
   or Entropy Generation Minimization of Energy Systems,"
   *Journal of Non-Equilibrium Thermodynamics*, 24(4), 327-359, 1999.

9. Esposito, M., Kawai, R., Lindenberg, K., Van den Broeck, C.
   "Efficiency at Maximum Power of Low-Dissipation Carnot Engines,"
   *Physical Review Letters*, 105, 150603, 2010.

10. Hoffmann, K.H., Burzler, J.M., Schubert, S. "Endoreversible Thermodynamics,"
    *Journal of Non-Equilibrium Thermodynamics*, 22(4), 311-355, 1997.
