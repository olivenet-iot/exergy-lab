# Atık Isı Geri Kazanım Teknolojileri (Waste Heat Recovery Technologies)

> Son güncelleme: 2026-01-31

## Genel Bakış

Endüstriyel atık ısı geri kazanımı (WHR — Waste Heat Recovery), proseslerden dışarıya verilen ısının yakalanıp faydalı bir amaç için yeniden kullanılmasıdır. Endüstriyel enerji tüketiminin %20-50'si atık ısı olarak kaybedilir. Bu potansiyelin %30-60'ı mevcut teknolojilerle geri kazanılabilir. Doğru teknoloji seçimi, atık ısının sıcaklık seviyesine, debisine, süreklilik profiline ve ekonomik koşullara bağlıdır.

## 1. Yüksek Sıcaklık Atık Isı Geri Kazanımı (>400°C)

### 1.1 Atık Isı Kazanları (Waste Heat Boilers)

```
Çalışma prensibi:
Yüksek sıcaklıktaki baca gazı veya proses gazından buhar üretimi.
Gaz akışı kazan tüplerinin dışından geçer, tüplerin içindeki
su buharlaşarak doymuş veya kızgın buhar üretir.

Sıcaklık aralığı: 400–1,200°C (giriş gazı)
Buhar basıncı: 5–60 bar (uygulamaya göre)
Verimlilik: %60–80 (baca gazı → buhar)
Yatırım maliyeti: 80–200 €/kW_termal
Ekonomik ömür: 20–30 yıl
Tipik ROI: 1–3 yıl

Uygulamalar:
- Cam fırını baca gazı (1,200°C)
- Çelik fırını baca gazı (800–1,000°C)
- Çimento döner fırını (600–800°C)
- Gaz türbini egzozu (450–550°C, CHP uygulaması)

Avantajlar:
+ Kanıtlanmış ve güvenilir teknoloji
+ Yüksek verimlilik
+ Uzun ömür
+ Mevcut buhar şebekesine entegrasyon kolay

Dezavantajlar:
- Büyük fiziksel boyut
- Yüksek başlangıç yatırımı (büyük kapasite)
- Kirli gazlarda fouling/korozyon riski
- Yardımcı ekipman gereksinimi (deaeratör, pompa vb.)
```

### 1.2 Reküperatörler (Recuperators)

```
Çalışma prensibi:
Sürekli akışlı ısı eşanjörü olarak baca gazından yakma havasını ön ısıtır.
Gaz-gaz ısı transferi; genellikle çapraz akış veya karşı akış tasarımlı.

Sıcaklık aralığı: 400–1,000°C (giriş gazı)
Hava ön ısıtma: 200–600°C
Verimlilik: %40–70 (sıcaklık geri kazanım oranı)
Yatırım maliyeti: 40–120 €/kW
Ekonomik ömür: 10–20 yıl

Malzeme seçimi:
- <600°C: Paslanmaz çelik (AISI 304, 316)
- 600–900°C: Inconel, Hastelloy
- >900°C: Seramik reküperatör

Avantajlar:
+ Kompakt tasarım (metalik tip)
+ Yakıt tasarrufu %10–30
+ Yanma verimliliğini artırır

Dezavantajlar:
- Yüksek sıcaklıkta malzeme maliyeti
- Termal gerilme → çatlak riski
- Kirli gazlarda bakım yoğun
```

### 1.3 Rejeneratörler (Regenerators)

```
Çalışma prensibi:
Döngüsel çalışma: Seramik veya metalik depolama kütlesi
önce sıcak gazla ısınır, sonra soğuk hava akışı ile ısısını verir.
Sabit yatak (iki oda, dönüşümlü) veya döner tip (Ljungström).

Sıcaklık aralığı: 800–1,500°C
Verimlilik: %70–90 (sıcaklık geri kazanım oranı)
Yatırım maliyeti: 60–150 €/kW

Uygulamalar:
- Cam eritme fırınları
- Çelik tavlama fırınları
- Yüksek sıcaklık pişirme fırınları

Avantajlar:
+ En yüksek verimlilik (gaz-gaz)
+ Çok yüksek sıcaklıklara dayanım (seramik)

Dezavantajlar:
- Büyük boyut ve ağırlık
- Hava kaçağı (döner tip)
- Karmaşık kontrol
```

## 2. Orta Sıcaklık Atık Isı Geri Kazanımı (100–400°C)

### 2.1 Ekonomizerler (Economizers)

```
Çalışma prensibi:
Kazan baca gazından çıkan ısıyla kazan besleme suyunu ön ısıtır.
Tipik olarak baca gazı sıcaklığını 200°C'den 120–140°C'ye düşürür.

Sıcaklık aralığı: 120–250°C (giriş baca gazı)
Besleme suyu ısıtma: 40–80°C sıcaklık artışı
Verimlilik artışı: Kazan veriminde +%3–5 puan
Yatırım maliyeti: 15–50 €/kW
Tipik geri ödeme: 0.5–2.0 yıl

Hesaplama:
Q̇_eco = ṁ_bg × Cp_bg × (T_bg,giriş - T_bg,çıkış) × η_eco [kW]

Dikkat: Baca gazı çıkış sıcaklığı asit çiğ noktasının
üzerinde tutulmalıdır.
- Doğalgaz: T_çiğ ≈ 55°C (kükürt yok, su buharı)
- Fuel oil: T_çiğ ≈ 130–150°C (kükürt trioksit)
- Kömür: T_çiğ ≈ 120–140°C

Avantajlar:
+ Düşük maliyet, kısa geri ödeme
+ Basit uygulama (mevcut kazana eklenebilir)
+ Bakım gereksinimi düşük

Dezavantajlar:
- Baca gazı basınç düşüşü → fan güç artışı
- Asit çiğ noktası altında korozyon riski
- Sınırlı sıcaklık artışı
```

### 2.2 Hava Ön Isıtıcılar (Air Preheaters)

```
Çalışma prensibi:
Baca gazından yakma havasını ısıtır. Reküperatif (sabit eşanjör)
veya rejeneratif (Ljungström döner tip) olabilir.

Sıcaklık aralığı: 150–400°C (giriş baca gazı)
Hava ön ısıtma: 100–250°C
Yakıt tasarrufu: %5–15
Yatırım maliyeti: 30–80 €/kW

Yakıt tasarrufu hesabı:
η_tasarruf = (T_hava,çıkış - T_hava,giriş) / (T_alev - T_hava,giriş) × (1 - η_mevcut) / η_mevcut

Avantajlar:
+ Önemli yakıt tasarrufu
+ Alev sıcaklığını artırarak proses verimini iyileştirir

Dezavantajlar:
- Hava kaçağı (döner tip, %5–15)
- Baca gazı tarafında korozyon riski
- Fan güç artışı
```

### 2.3 Organik Rankine Çevrimi — ORC (Organic Rankine Cycle)

```
Çalışma prensibi:
Düşük kaynama noktalı organik akışkan (R245fa, n-pentane, siloksan vb.)
kullanarak atık ısıdan elektrik üretimi. Buhar Rankine çevrimine benzer
ancak düşük sıcaklıklarda çalışır.

Sıcaklık aralığı: 80–400°C (ısı kaynağı)
Elektriksel verimlilik: %8–18 (kaynak sıcaklığına bağlı)
Yatırım maliyeti: 1,500–4,000 €/kWe
Tipik güç aralığı: 50 kWe – 10 MWe
Tipik geri ödeme: 3–7 yıl

ORC akışkan seçimi (sıcaklığa göre):
| Kaynak Sıcaklığı [°C] | Uygun Akışkan | η_elek [%] |
|---|---|---|
| 80–120 | R134a, R245fa | 5–10 |
| 120–200 | R245fa, n-pentane | 10–14 |
| 200–300 | Siloksan (D4, MDM) | 12–16 |
| 300–400 | Toluene, siloksan | 15–20 |

ORC verimlilik hesabı:
η_ORC = η_Carnot × η_termal × η_mekanik × η_jeneratör
      = (1 - T_soğuk/T_sıcak) × 0.50 × 0.95 × 0.96

Örnek: T_sıcak = 250°C = 523 K, T_soğuk = 30°C = 303 K
η_ORC = (1 - 303/523) × 0.50 × 0.95 × 0.96
      = 0.421 × 0.50 × 0.95 × 0.96 = %19.2 (ideal)
Gerçek: ~%14–16

Avantajlar:
+ Düşük sıcaklıkta elektrik üretimi
+ Modüler ve kompakt tasarım
+ Bakım gereksinimi düşük (kapalı çevrim)
+ Otomatik çalışma

Dezavantajlar:
- Yüksek yatırım maliyeti
- Düşük verimlilik (özellikle <150°C)
- Soğutma suyu gereksinimi
- Bazı akışkanların GWP değeri yüksek
```

### 2.4 Isı Boruları (Heat Pipes)

```
Çalışma prensibi:
Kapalı bir boru içinde çalışma akışkanının buharlaşma-yoğuşma
döngüsü ile ısı transferi. Hareketli parça yok, çok yüksek
ısı iletkenliği (bakırın 100–1,000 katı).

Sıcaklık aralığı: 100–400°C (yüksek sıcaklık tipi)
Verimlilik: %60–80
Yatırım maliyeti: 50–150 €/kW

Çalışma akışkanı seçimi:
| Sıcaklık [°C] | Akışkan |
|---|---|
| 30–200 | Su |
| 200–600 | Dowtherm, termal yağ |
| 600–1,000 | Sodyum, potasyum |

Avantajlar:
+ Hareketli parça yok → bakım gerektirmez
+ Çok kompakt
+ Bağımsız ısı taşıma (mesafe bağımsız, kısa-orta mesafe)

Dezavantajlar:
- Kapasitesi sınırlı
- Yerçekimi bağımlı (bazı tiplerde)
- Özel imalat gerektirir
```

### 2.5 Runaround Coil Sistemleri

```
Çalışma prensibi:
İki ayrı eşanjör bir glikol-su karışımı döngüsüyle bağlanır.
Bir eşanjör ısı kaynağında, diğeri ısı kullanıcısında bulunur.
Kaynak ve kullanıcı birbirinden fiziksel olarak ayrıdır.

Sıcaklık aralığı: 100–250°C (kaynak tarafı)
Verimlilik: %40–65
Yatırım maliyeti: 60–120 €/kW

Avantajlar:
+ Kaynak ve kullanıcı fiziksel olarak ayrı olabilir
+ Kirli gazlarla temiz akışkan karışmaz (dolaylı transfer)
+ Esnek yerleşim

Dezavantajlar:
- Düşük verimlilik (çift eşanjör → çift ΔT kaybı)
- Pompa güç tüketimi
- Glikol bakımı ve değişimi
```

## 3. Düşük Sıcaklık Atık Isı Geri Kazanımı (<100°C)

### 3.1 Endüstriyel Isı Pompaları (Industrial Heat Pumps)

```
Çalışma prensibi:
Düşük sıcaklıktaki atık ısıyı, elektrik enerjisi kullanarak
daha yüksek ve kullanılabilir bir sıcaklık seviyesine çıkarır.
Buhar sıkıştırmalı, absorpsiyonlu veya hibrit tip olabilir.

Sıcaklık aralığı (kaynak): 20–80°C
Sıcaklık aralığı (çıkış): 50–150°C (yüksek sıcaklık HP ile)
COP: 2.5–6.0 (sıcaklık kaldırma mesafesine bağlı)
Yatırım maliyeti: 300–800 €/kW_termal
Tipik güç aralığı: 50 kW – 10 MW termal

COP vs. sıcaklık kaldırma ilişkisi:
| Sıcaklık Kaldırma ΔT [°C] | Tipik COP | Carnot COP |
|---|---|---|
| 20 | 5.0–6.0 | 14.9 |
| 30 | 3.5–5.0 | 10.1 |
| 40 | 3.0–4.0 | 7.7 |
| 50 | 2.5–3.5 | 6.2 |
| 60 | 2.0–3.0 | 5.2 |
| 80 | 1.8–2.5 | 4.0 |

COP hesabı:
COP = Q̇_çıkış / Ẇ_kompresör
Carnot COP_ısıtma = T_sıcak / (T_sıcak - T_soğuk) [K cinsinden]
Gerçek COP ≈ 0.35–0.55 × Carnot COP

Ekonomik fizibilite koşulu:
COP > c_elektrik / c_yakıt
Örnek: c_elek = €0.12/kWh, c_yakıt = €0.045/kWh
COP_min = 0.12 / 0.045 = 2.67
→ COP > 2.67 ise ısı pompası ekonomik olarak avantajlı

Avantajlar:
+ Düşük sıcaklık atık ısıyı değerlendirir
+ Yüksek COP → enerji çarpanı etkisi
+ Çevresel fayda (CO₂ azaltımı)

Dezavantajlar:
- Yüksek yatırım maliyeti
- Elektrik fiyatına duyarlılık
- Bakım gereksinimi (kompresör)
- Sınırlı çıkış sıcaklığı (konvansiyonel tip)
```

### 3.2 Kondenserli Ekonomizerler (Condensing Economizers)

```
Çalışma prensibi:
Doğalgaz kazanlarında baca gazı sıcaklığını çiğ noktasının altına
düşürerek su buharının yoğuşmasından gizli ısıyı geri kazanır.

Sıcaklık aralığı: 55–120°C (giriş baca gazı, doğalgaz)
Çıkış sıcaklığı: 25–50°C (baca gazı)
Verimlilik artışı: +%5–12 (LHV bazında; HHV'ye göre)
Yatırım maliyeti: 30–80 €/kW
Tipik geri ödeme: 1.0–3.0 yıl

Koşullar:
- Yalnızca doğalgaz (düşük kükürt) kazanlarında uygulanır
- Dönüş suyu sıcaklığı <50°C olmalı (yoğuşma için)
- Korozyona dayanıklı malzeme (paslanmaz, PTFE kaplama)

Verimlilik hesabı:
η_toplam = η_kazan + Q̇_kondens / Q̇_yakıt
Q̇_kondens = ṁ_bg × (h_bg,giriş - h_bg,çıkış) [kW]
  (entalpi farkı yoğuşma gizli ısısını içerir)

Avantajlar:
+ En yüksek kazan verimi (>%100 LHV bazında)
+ Kompakt ekipman
+ Düşük emisyon (NOx azaltımı)

Dezavantajlar:
- Düşük dönüş suyu sıcaklığı gerektirir
- Korozyon riski → özel malzeme
- Kondensat drenajı ve nötralizasyon
```

### 3.3 Absorpsiyonlu Soğutma (Absorption Chillers)

```
Çalışma prensibi:
Atık ısı ile soğutma üretimi. LiBr-su çifti (>80°C kaynak ile)
veya amonyak-su çifti (düşük sıcaklık uygulamaları).
Elektrik yerine ısı enerjisi ile çalışır.

Sıcaklık aralığı (ısı kaynağı):
- Tek etkili (single effect): 80–120°C, COP 0.65–0.75
- Çift etkili (double effect): 140–180°C, COP 1.0–1.2
- Doğrudan yakmalı: >180°C, COP 1.0–1.2

Soğutma kapasitesi: 50 kW – 10 MW
Yatırım maliyeti: 200–500 €/kW_soğutma
Tipik geri ödeme: 3–7 yıl

Avantajlar:
+ Atık ısıyı soğutmaya dönüştürür
+ Düşük elektrik tüketimi
+ Sessiz çalışma (mekanik kompresör yok)

Dezavantajlar:
- Düşük COP (buhar sıkıştırmalıya göre)
- Büyük boyut ve ağırlık
- Soğutma kulesi gereksinimi
- LiBr korozyon ve kristalizasyon riski
```

### 3.4 Termoelektrik Jeneratörler (TEG — Thermoelectric Generators)

```
Çalışma prensibi:
Seebeck etkisi ile sıcaklık farkından doğrudan elektrik üretimi.
Hareketli parça yok, tamamen katı hal.

Sıcaklık aralığı: ΔT = 50–300°C
Verimlilik: %3–8
Yatırım maliyeti: 5,000–15,000 €/kWe
Güç aralığı: 1 W – 10 kW (endüstriyel)

Avantajlar:
+ Hareketli parça yok → bakımsız
+ Kompakt, ölçeklenebilir
+ Uzun ömür (>20 yıl)

Dezavantajlar:
- Çok düşük verimlilik
- Çok yüksek maliyet (€/kWe)
- Sınırlı güç kapasitesi
- Şu an niş uygulamalar için uygun
```

### 3.5 Termal Enerji Depolama — TES (Thermal Energy Storage)

```
Çalışma prensibi:
Atık ısının zaman kaydırması yapılarak farklı zamanda
kullanılması. Duyulur ısı (su, kaya), gizli ısı (PCM — Phase
Change Material) veya termokimyasal depolama.

Duyulur ısı depolama (sensible):
- Ortam: Su (tank), kaya yatağı, beton
- Sıcaklık: 40–95°C (su), 200–500°C (kaya/beton)
- Enerji yoğunluğu: 40–60 kWh/m³
- Maliyet: 10–50 €/kWh_th

Gizli ısı depolama (PCM):
- Ortam: Parafin, tuz hidratlari, ötektik karışımlar
- Sıcaklık: 20–200°C (PCM türüne bağlı)
- Enerji yoğunluğu: 80–200 kWh/m³
- Maliyet: 50–150 €/kWh_th

Erimiş tuz depolama (Molten salt):
- Ortam: NaNO₃/KNO₃ karışımı (solar salt)
- Sıcaklık: 250–565°C
- Enerji yoğunluğu: 100–150 kWh/m³
- Maliyet: 20–80 €/kWh_th (büyük ölçek)

Avantajlar:
+ Zaman uyumsuzluğunu çözer (kaynak-kullanıcı)
+ Pik talebi karşılama (peak shaving)
+ Kesikli proseslerde ısı düzenleme

Dezavantajlar:
- Ek yatırım maliyeti
- Alan gereksinimi
- Isı kaybı (depolama süresi ile artar)
- PCM: Düşük ısı iletkenliği
```

## 4. Teknoloji Karşılaştırma Tablosu (Comprehensive Comparison)

| Teknoloji | T_kaynak [°C] | Verimlilik [%] | Yatırım [€/kW] | SPP [yıl] | Olgunluk |
|---|---|---|---|---|---|
| Atık ısı kazanı | 400–1,200 | 60–80 | 80–200 | 1–3 | Olgun |
| Reküperatör | 400–1,000 | 40–70 | 40–120 | 1–3 | Olgun |
| Rejeneratör | 800–1,500 | 70–90 | 60–150 | 2–4 | Olgun |
| Ekonomizer | 120–250 | 60–85 | 15–50 | 0.5–2 | Olgun |
| Hava ön ısıtıcı | 150–400 | 50–70 | 30–80 | 1–3 | Olgun |
| ORC | 80–400 | 8–18 | 1,500–4,000 | 3–7 | Ticari |
| Isı borusu | 100–400 | 60–80 | 50–150 | 2–4 | Olgun |
| Runaround coil | 100–250 | 40–65 | 60–120 | 2–4 | Olgun |
| Endüstriyel ısı pompası | 20–80 | COP 2.5–6.0 | 300–800 | 2–5 | Ticari |
| Kondenserli ekonomizer | 55–120 | +5–12 puan | 30–80 | 1–3 | Olgun |
| Absorpsiyon chiller | 80–180 | COP 0.65–1.2 | 200–500 | 3–7 | Olgun |
| TEG (termoelektrik) | ΔT 50–300 | 3–8 | 5,000–15,000 | >10 | Gelişmekte |
| TES (duyulur, su) | 40–95 | 85–95 | 10–50/kWh | 2–5 | Olgun |
| TES (PCM) | 20–200 | 75–90 | 50–150/kWh | 4–8 | Ticari |

## 5. Teknoloji Seçim Karar Akışı (Decision Flowchart)

```
                        ┌─────────────────────┐
                        │  Atık ısı kaynağı    │
                        │  mevcut mu?          │
                        └──────────┬───────────┘
                                   │ Evet
                        ┌──────────▼───────────┐
                        │  Kaynak sıcaklığı?    │
                        └──────────┬───────────┘
                  ┌────────────────┼─────────────────┐
                  │                │                  │
           ┌──────▼──────┐ ┌──────▼──────┐  ┌───────▼──────┐
           │  >400°C      │ │ 100-400°C   │  │ <100°C       │
           │  (Yüksek)    │ │ (Orta)      │  │ (Düşük)      │
           └──────┬──────┘ └──────┬──────┘  └───────┬──────┘
                  │               │                  │
           ┌──────▼──────┐       │           ┌──────▼───────┐
           │ Buhar iht.  │       │           │ Isıtma iht.  │
           │ var mı?     │       │           │ var mı?      │
           └───┬────┬────┘       │           └───┬─────┬────┘
           Evet│    │Hayır       │           Evet│     │Hayır
               │    │            │               │     │
        ┌──────▼┐ ┌─▼──────┐    │        ┌──────▼┐ ┌──▼─────┐
        │WHB    │ │Güç ür. │    │        │Isı    │ │Abs.    │
        │(Atık  │ │ORC/    │    │        │pompası│ │chiller │
        │ısı    │ │Buhar   │    │        │       │ │veya    │
        │kazanı)│ │türbin  │    │        │       │ │TES     │
        └───────┘ └────────┘    │        └───────┘ └────────┘
                                │
                    ┌───────────┼───────────┐
                    │           │           │
             ┌──────▼──┐ ┌─────▼───┐ ┌─────▼──────┐
             │Su ısıtma│ │Hava ön │ │Güç üretimi │
             │gerekli? │ │ısıtma? │ │potansiyeli?│
             └────┬────┘ └────┬───┘ └─────┬──────┘
                  │           │            │
            ┌─────▼────┐ ┌───▼─────┐ ┌────▼──────┐
            │Ekonomizer│ │Hava ön  │ │ORC        │
            │          │ │ısıtıcı │ │(>100 kWth)│
            └──────────┘ └─────────┘ └───────────┘
```

## 6. ORC Detaylı Değerlendirme (ORC Deep Dive)

### 6.1 Çalışma Akışkanları ve Karakteristikleri

| Akışkan | Kaynama [°C] | Kritik T [°C] | ODP | GWP | Uygun Kaynak T [°C] |
|---|---|---|---|---|---|
| R134a | -26 | 101 | 0 | 1,430 | 80–120 |
| R245fa | 15 | 154 | 0 | 1,030 | 100–180 |
| R1233zd(E) | 18 | 166 | 0 | 1 | 100–180 |
| n-Pentane | 36 | 197 | 0 | ~5 | 120–220 |
| Toluene | 111 | 319 | 0 | ~3 | 200–350 |
| MDM (siloksan) | 152 | 291 | 0 | ~0 | 200–300 |
| MM (siloksan) | 100 | 246 | 0 | ~0 | 150–250 |

### 6.2 ORC Ekonomik Analiz Örneği

```
Senaryo: Çimento fabrikası klinker soğutucu egzoz gazı
- Kaynak: 320°C, 15,000 Nm³/h
- Mevcut durum: Atmosfere atılıyor
- Termal güç: ~1,200 kW_th (kullanılabilir)

ORC sistemi:
- Akışkan: Siloksan (MDM)
- Elektrik çıkışı: 1,200 × 0.16 = 192 kWe (net)
- Yardımcı güç: ~15 kWe
- Net çıkış: 177 kWe

Ekonomik değerlendirme:
- Yatırım: 177 kWe × €3,000/kWe = €531,000
- Yıllık çalışma: 7,500 saat
- Elektrik üretimi: 177 × 7,500 = 1,327,500 kWh/yıl
- Elektrik değeri: 1,327,500 × €0.12 = €159,300/yıl
- Bakım maliyeti: €15,000/yıl
- Net yıllık tasarruf: €144,300/yıl
- SPP = 531,000 / 144,300 = 3.68 yıl
- NPV (15 yıl, %10): €567,000
- IRR: %27
```

## 7. Endüstriyel Isı Pompası Detaylı Değerlendirme

### 7.1 COP ve Sıcaklık Kaldırma Eğrisi

```
COP
 6 |  *
   |   *
 5 |    *
   |     *
 4 |      *
   |       *
 3 |        *
   |         *
 2 |          *  *  *
   |
 1 |
   └──────────────────── ΔT [°C]
   0   20   40   60   80

Pratik kural:
COP ≈ 0.45 × T_çıkış / (T_çıkış - T_kaynak)   [K cinsinden]
```

### 7.2 Ekonomik Analiz Örneği

```
Senaryo: Gıda fabrikası, soğutma sistemi atık ısısı
- Kaynak: Chiller kondenserinden 38°C su (200 kW termal)
- Hedef: Proses sıcak su üretimi (65°C)
- Sıcaklık kaldırma: ΔT = 27°C

Isı pompası seçimi:
- Tip: Buhar sıkıştırmalı (R134a/R1234ze)
- COP = 0.45 × 338 / (338 - 311) = 0.45 × 338 / 27 = 5.63
  Gerçek COP ≈ 4.5 (kayıplar dahil)
- Termal çıkış: 200 kW
- Elektrik gücü: 200 / 4.5 = 44.4 kWe

Ekonomik değerlendirme:
- Yatırım: 200 kW × €500/kW = €100,000
- Yıllık çalışma: 5,000 saat
- Isı üretimi: 200 × 5,000 = 1,000,000 kWh_th/yıl
- Kazan yakıtı tasarrufu: 1,000,000 / 0.90 × €0.045 = €50,000/yıl
- HP elektrik maliyeti: 44.4 × 5,000 × €0.12 = €26,640/yıl
- Net yıllık tasarruf: €50,000 - €26,640 = €23,360/yıl
- SPP = 100,000 / 23,360 = 4.28 yıl
- NPV (15 yıl, %10): €77,700
```

## 8. Performans Sınıflandırması (WHR Performans)

| Performans Kriteri | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| WHR uygulanma oranı | <%1 kaynak | 1–3 kaynak | 3–5 kaynak | >5 kaynak |
| Isı geri kazanım oranı | <%10 | %10–25 | %25–40 | >%40 |
| WHR yatırım geri dönüşü | >5 yıl | 3–5 yıl | 1.5–3 yıl | <1.5 yıl |
| Kademe kullanımı | Yok | Tek kademe | 2 kademe | >2 kademe |
| Toplam yakıt tasarrufu | <%3 | %3–10 | %10–20 | >%20 |

| WHR Teknoloji Seçim Puanı | Düşük | Ortalama | İyi | Mükemmel | Kritik |
|---|---|---|---|---|---|
| Kaynak sıcaklık uyumu | Kötü eşleşme | Kısmi | İyi | Mükemmel | — |
| Yatırım/tasarruf oranı | SPP >5 yıl | 3–5 yıl | 1.5–3 yıl | <1.5 yıl | Negatif NPV |
| Teknik risk | Yüksek | Orta | Düşük | Minimal | — |
| Entegrasyon kolaylığı | Zor | Orta | Kolay | Plug-and-play | — |

## 9. ExergyLab Platformunda WHR Değerlendirmesi

### 9.1 Platform Algoritması

```
ExergyLab WHR değerlendirme süreci:

1. Ekipman verilerinden atık ısı kaynaklarını tanımla
   - Kazan: baca gazı sıcaklığı → economizer potansiyeli
   - Kompresör: soğutma sistemi → ısı geri kazanım potansiyeli
   - Chiller: kondenser → desuperheater, ısı pompası

2. Her kaynak için uygun WHR teknolojilerini listele
   - Sıcaklık bazlı filtreleme
   - Kapasite uyumu

3. Ekonomik değerlendirme
   - Tahmini yatırım (kapasite bazlı €/kW)
   - Yıllık tasarruf hesabı
   - SPP ve NPV hesabı

4. Entegrasyon fırsatları
   → cross_equipment.md ile bağlantı
   → heat_integration.md ile eşleştirme
```

## İlgili Dosyalar

- [Isı Entegrasyonu](heat_integration.md) — Kaynak-kullanım eşleştirme metodolojisi
- [Kojenerasyon Sistemleri](cogeneration.md) — CHP/CCHP ile atık ısı değerlendirme
- [Proses Entegrasyonu](process_integration.md) — Proses düzeyinde WHR
- [Ekipmanlar Arası Optimizasyon](cross_equipment.md) — Çapraz ekipman WHR fırsatları
- [Ekonomik Analiz](economic_analysis.md) — Yatırım analizi metodları
- [Kazan Formülleri](../boiler/formulas.md) — Kazan verimlilik ve baca gazı hesabı
- [Kazan Çözümleri](../boiler/solutions/) — Economizer ve baca gazı geri kazanım
- [Kompresör Benchmarkları](../compressor/benchmarks.md) — Kompresör atık ısı verileri
- [Kompresör Çözümleri](../compressor/solutions/) — Kompresör ısı geri kazanım
- [Chiller Formülleri](../chiller/formulas.md) — Chiller performans hesaplamaları
- [Chiller Çözümleri](../chiller/solutions/) — Kondenser ısı geri kazanım
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy analizi temelleri

## Referanslar

- US DOE, "Waste Heat Recovery: Technology and Opportunities in U.S. Industry," 2008
- Johansson, M.T. & Söderström, M., "Options for the Swedish steel industry — Energy efficiency measures and fuel conversion," Energy, 2011
- Brückner, S. et al., "Industrial waste heat recovery technologies: An economic analysis of heat transformation technologies," Applied Energy, 2015
- Quoilin, S. et al., "Techno-economic survey of Organic Rankine Cycle (ORC) systems," Renewable and Sustainable Energy Reviews, 2013
- Arpagaus, C. et al., "High temperature heat pumps: Market overview, state of the art, research status, refrigerants, and application potentials," Energy, 2018
- IEA, "Application of Industrial Heat Pumps," IEA Heat Pump Centre, 2014
- European Commission, "Reference Document on Best Available Techniques for Energy Efficiency," 2009
- Dincer, I. & Rosen, M.A., "Thermal Energy Storage: Systems and Applications," Wiley, 2nd Edition, 2011
- Tchanche, B.F. et al., "Low-grade heat conversion into power using organic Rankine cycles — A review," Renewable and Sustainable Energy Reviews, 2011
- Law, R. et al., "Opportunities for low-grade heat recovery in the UK food processing industry," Applied Thermal Engineering, 2013
