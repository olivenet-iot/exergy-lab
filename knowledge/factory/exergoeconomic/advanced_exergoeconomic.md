---
title: "İleri Exergoekonomik Analiz (Advanced Exergoeconomic Analysis)"
category: factory
equipment_type: factory
keywords: [ileri analiz, kaçınılabilir, kaçınılmaz, endojen, eksojen, AV/UN, EN/EX]
related_files:
  - factory/exergoeconomic/evaluation_criteria.md
  - factory/exergoeconomic/speco_method.md
  - factory/exergoeconomic/optimization.md
  - factory/exergoeconomic/exergoeconomic_balance.md
use_when:
  - "İleri exergoekonomik analiz yapılırken"
  - "Kaçınılabilir/kaçınılmaz exergy yıkımı ayrımı yapılırken"
  - "Endojen/eksojen exergy yıkımı belirlenirken"
  - "Gerçek iyileştirme potansiyeli değerlendirilirken"
priority: medium
last_updated: 2026-02-01
---
# İleri Exergoekonomik Analiz (Advanced Exergoeconomic Analysis)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Standart (conventional) exergoekonomik analiz, her bileşendeki toplam exergy yıkımını değerlendirir. Ancak bu yıkımın tamamı iyileştirilebilir olmayabilir. İleri exergoekonomik analiz, exergy yıkımını ve yatırım maliyetini daha gerçekçi bileşenlere ayırır.

```
Standart Analiz:
  Ė_D,k → Ċ_D,k, f_k, r_k

İleri Analiz — İki Boyutlu Ayrım:
  Boyut 1: Kaçınılabilir (AV) vs Kaçınılmaz (UN)
    → "Bu yıkımın ne kadarı teknolojik olarak azaltılabilir?"

  Boyut 2: Endojen (EN) vs Eksojen (EX)
    → "Bu yıkım bileşenin kendisinden mi, başka bileşenlerden mi kaynaklanıyor?"

  4-Yollu Matris:
  ┌──────────────────────────────────────┐
  │          │ Endojen (EN)  │ Eksojen (EX) │
  │──────────│──────────────│──────────────│
  │ AV       │ AV-EN         │ AV-EX         │
  │          │ (Birincil     │ (Sistem       │
  │          │  hedef)       │  entegrasyon) │
  │──────────│──────────────│──────────────│
  │ UN       │ UN-EN         │ UN-EX         │
  │          │ (Kaçınılmaz,  │ (Kaçınılmaz,  │
  │          │  bileşen)     │  sistem)      │
  └──────────────────────────────────────┘
```

## 2. Kaçınılabilir / Kaçınılmaz Ayrımı (AV/UN Splitting)

### 2.1 Tanım

```
Ė_D,k = Ė_D,k^AV + Ė_D,k^UN

Kaçınılmaz (Unavoidable — UN):
  Mevcut ve öngörülebilir teknoloji ile azaltılamayan exergy yıkımı.
  → Termodinamik, teknolojik ve ekonomik kısıtlamalardan kaynaklanır.

Kaçınılabilir (Avoidable — AV):
  Teknolojik ve ekonomik olarak azaltılabilecek exergy yıkımı.
  → Gerçek iyileştirme potansiyelini temsil eder.
```

### 2.2 Kaçınılmaz Koşulların Belirlenmesi

```
Ė_D,k^UN hesaplamak için:
  Bileşen k'yı "en iyi ulaşılabilir" koşullarda çalıştır

  Bu koşullar:
  - Mevcut teknolojinin en iyi verimi
  - Ekonomik olarak makul sınırlar
  - Fiziksel kısıtlamalar (malzeme, boyut)

Pratik yaklaşım:
  ε_k^max tanımla (teknolojik üst sınır)
  Ė_D,k^UN = Ė_F,k × (1 - ε_k^max)  (yaklaşık)
  Ė_D,k^AV = Ė_D,k - Ė_D,k^UN
```

### 2.3 Ekipman Türüne Göre Kaçınılmaz Koşullar

| Ekipman | Parametre | Gerçek Değer | Kaçınılmaz Koşul | Not |
|---------|-----------|--------------|-------------------|-----|
| Kompresör | η_is | %80-88 | %92-95 | En iyi ticari verim |
| Türbin (buhar) | η_is | %82-90 | %94-97 | — |
| Türbin (gaz) | η_is | %85-92 | %95-97 | — |
| Kazan | ε | %25-45 | %50-60 | Min. ΔT ve kayıp |
| HX | ΔT_min | 10-25 K | 3-5 K | Ekonomik sınır |
| Pompa | η_is | %70-85 | %90-95 | — |
| Chiller | COP_ex | %15-35 | %40-55 | Carnot sınırına yaklaşma |
| Yanma odası | η_yanma | %95-99 | %99.5 | Kimyasal kısıt |

### 2.4 Kaçınılmaz Maliyet

```
Yatırım maliyeti de ayrılır:

Ż_k = Ż_k^AV + Ż_k^UN

Kaçınılmaz Ż:
  Ż_k^UN = En ucuz kabul edilebilir ekipman maliyeti
  → Minimum verim ve güvenilirlik standartlarını karşılayan en ucuz seçenek

Kaçınılabilir Ż:
  Ż_k^AV = Ż_k - Ż_k^UN
  → Daha ucuz alternatif ile tasarruf edilebilecek yatırım maliyeti
```

## 3. Endojen / Eksojen Ayrımı (EN/EX Splitting)

### 3.1 Tanım

```
Ė_D,k = Ė_D,k^EN + Ė_D,k^EX

Endojen (Endogenous — EN):
  Bileşen k'nın kendi verimsizliğinden kaynaklanan exergy yıkımı.
  → Diğer tüm bileşenler ideal çalışsa bile oluşacak yıkım.

Eksojen (Exogenous — EX):
  Diğer bileşenlerin verimsizliğinden kaynaklanan exergy yıkımı.
  → Bileşen k'ya gelen akışların bozulması nedeniyle oluşan ek yıkım.

Fiziksel anlam:
  Ė_D,k^EN → Bileşenin kendi sorumluluğu
  Ė_D,k^EX → Başka bileşenlerin bileşen k'ya etkisi
```

### 3.2 Hesaplama Yöntemi

```
Endojen exergy yıkımı hesabı:

Adım 1: Bileşen k, GERÇEK koşullarda çalışır
Adım 2: Diğer TÜM bileşenler İDEAL (veya teorik) koşullarda çalışır
Adım 3: Sistem bu "hibrit" koşullarla simüle edilir
Adım 4: Bileşen k'daki exergy yıkımı = Ė_D,k^EN

Ė_D,k^EX = Ė_D,k - Ė_D,k^EN

İdeal koşullar (diğer bileşenler için):
  Türbin/kompresör: η_is = 1.0 (izentropik)
  HX: ΔT_min = 0 (sonsuz alan)
  Karıştırıcı: İdeal karışım (aynı T, P)
  Valf: ΔP = 0 (yok farz et)
```

### 3.3 Pratik Yaklaşım (Mühendislik Yöntemi)

```
Tam EN/EX hesabı her bileşen kombinasyonu için simülasyon gerektirir.
n bileşenli sistemde: n adet hibrit simülasyon

Basitleştirilmiş yaklaşım (Kelly, Tsatsaronis, Morosuk 2009):

Ė_D,k^EN ≈ Ė_P,k^gerçek × (Ė_D,k / Ė_P,k)_ideal_diğerleri

Burada "ideal diğerleri" koşulunda:
- Diğer bileşenler ideal → akış koşulları değişir
- Bileşen k gerçek verimi ile bu değişen koşullarda çalışır
- Sonuçtaki Ė_D,k = Ė_D,k^EN
```

## 4. Dört Yollu Matris (4-Way Splitting)

### 4.1 Tanım

```
AV/UN ve EN/EX ayrımları birleştirildiğinde:

Ė_D,k = Ė_D,k^(AV,EN) + Ė_D,k^(AV,EX) + Ė_D,k^(UN,EN) + Ė_D,k^(UN,EX)

Aynı şekilde maliyet:
Ċ_D,k = Ċ_D,k^(AV,EN) + Ċ_D,k^(AV,EX) + Ċ_D,k^(UN,EN) + Ċ_D,k^(UN,EX)

Ve yatırım maliyeti:
Ż_k = Ż_k^(AV,EN) + Ż_k^(AV,EX) + Ż_k^(UN,EN) + Ż_k^(UN,EX)
```

### 4.2 Her Kombinasyonun Anlamı

```
AV-EN (Kaçınılabilir-Endojen):
  → Bileşenin KENDİ verimsizliğinden kaynaklanan İYİLEŞTİRİLEBİLİR yıkım
  → BİRİNCİL İYİLEŞTİRME HEDEFİ
  → Bu bileşenin verimini artır

AV-EX (Kaçınılabilir-Eksojen):
  → BAŞKA bileşenlerin etkisiyle oluşan İYİLEŞTİRİLEBİLİR yıkım
  → Sistem entegrasyonu ile çözülebilir
  → Kaynak bileşeni iyileştir

UN-EN (Kaçınılmaz-Endojen):
  → Bileşenin kendi doğasından kaynaklanan AZALTILAMAZ yıkım
  → Teknolojik sınır, müdahale yapılamaz
  → Kabul et

UN-EX (Kaçınılmaz-Eksojen):
  → Başka bileşenlerin etkisiyle oluşan AZALTILAMAZ yıkım
  → Sistem yapısından kaynaklanan kaçınılmaz etki
  → Kabul et
```

### 4.3 Önceliklendirme

```
İyileştirme Öncelik Sırası:

1. ★★★★★ Ċ_D^(AV,EN) + Ż^(AV,EN) → Bileşen kendisi iyileştirilmeli
2. ★★★★  Ċ_D^(AV,EX) + Ż^(AV,EX) → Sistem entegrasyonu yapılmalı
3. ★★★   Ċ_D^(UN,EN) + Ż^(UN,EN) → Teknolojik sınır, yalnızca izle
4. ★★    Ċ_D^(UN,EX) + Ż^(UN,EX) → Sistem sınırı, izle
```

## 5. İleri Değerlendirme Göstergeleri

### 5.1 İleri Exergoekonomik Faktör

```
f_k^AV = Ż_k^AV / (Ż_k^AV + Ċ_D,k^AV)

Yorumlama (aynı eşikler, ama kaçınılabilir kısma odaklı):
  f_k^AV < 0.25 → Kaçınılabilir verimlilik kaybı baskın
  0.25 ≤ f_k^AV ≤ 0.70 → Dengeli
  f_k^AV > 0.70 → Kaçınılabilir yatırım maliyeti baskın
```

### 5.2 İleri Göreli Maliyet Farkı

```
r_k^AV = (c_P,k^AV - c_F,k) / c_F,k

Burada c_P,k^AV yalnızca kaçınılabilir maliyetler dikkate alınarak hesaplanır.
```

### 5.3 Standart vs İleri Karşılaştırma

| Gösterge | Standart | İleri | Fark |
|----------|----------|-------|------|
| Ċ_D,k | Toplam yıkım maliyeti | Yalnızca AV kısım | Daha gerçekçi |
| f_k | Ż/(Ż+Ċ_D) toplam | Ż^AV/(Ż^AV+Ċ_D^AV) | Daha kesin yönlendirme |
| r_k | Toplam bazlı | AV bazlı | Daha az abartılı |
| Sıralama | Yanıltıcı olabilir | Gerçek potansiyeli yansıtır | Sıralama değişebilir |

## 6. CHP Sistemi Tam Örneği

### 6.1 Sistem Tanımı

```
Gaz Türbin Kojenerasyon (CHP) Sistemi:
  1. Hava kompresörü (AC)
  2. Yanma odası (CC)
  3. Gaz türbin (GT)
  4. HRSG (atık ısı kazanı)
  5. Pompa (P)

Akışlar:
  1: Hava girişi (25°C, 1 bar)
  2: Sıkıştırılmış hava (400°C, 12 bar)
  3: Yanma gazları (1200°C, 11.5 bar)
  4: Türbin çıkışı (550°C, 1.05 bar)
  5: Baca gazı (150°C, 1 bar)
  6: Besleme suyu (60°C, 20 bar)
  7: Buhar (250°C, 20 bar)
  F: Doğalgaz (yakıt)
  Ẇ_net: Net elektrik üretimi
```

### 6.2 Standart Analiz Sonuçları

| Bileşen | Ė_D [kW] | ε [%] | Ż [€/h] | c_F [€/GJ] | Ċ_D [€/h] | f_k | r_k |
|---------|-----------|-------|----------|-------------|------------|-----|-----|
| AC | 1,850 | 88.5 | 12.40 | 18.5 | 123.2 | 0.091 | 0.48 |
| CC | 12,400 | 72.0 | 3.80 | 8.0 | 357.1 | 0.011 | 0.39 |
| GT | 2,100 | 93.5 | 22.60 | 14.2 | 107.4 | 0.174 | 0.28 |
| HRSG | 3,200 | 68.0 | 8.50 | 14.2 | 163.6 | 0.049 | 0.47 |
| P | 15 | 75.0 | 0.30 | 18.5 | 1.0 | 0.231 | 0.67 |

### 6.3 İleri Analiz — AV/UN Ayrımı

| Bileşen | Ė_D [kW] | Ė_D^UN [kW] | Ė_D^AV [kW] | Ż^UN [€/h] | Ż^AV [€/h] |
|---------|-----------|-------------|-------------|-------------|-------------|
| AC | 1,850 | 650 | 1,200 | 8.20 | 4.20 |
| CC | 12,400 | 9,500 | 2,900 | 2.50 | 1.30 |
| GT | 2,100 | 580 | 1,520 | 14.80 | 7.80 |
| HRSG | 3,200 | 1,800 | 1,400 | 5.10 | 3.40 |
| P | 15 | 5 | 10 | 0.18 | 0.12 |

### 6.4 İleri Analiz — EN/EX Ayrımı

| Bileşen | Ė_D^AV [kW] | Ė_D^(AV,EN) [kW] | Ė_D^(AV,EX) [kW] |
|---------|-------------|-------------------|-------------------|
| AC | 1,200 | 980 | 220 |
| CC | 2,900 | 2,500 | 400 |
| GT | 1,520 | 1,100 | 420 |
| HRSG | 1,400 | 850 | 550 |
| P | 10 | 8 | 2 |

### 6.5 Dört Yollu Maliyet Matrisi

| Bileşen | Ċ_D^(AV,EN) [€/h] | Ċ_D^(AV,EX) [€/h] | Ċ_D^(UN,EN) [€/h] | Ċ_D^(UN,EX) [€/h] |
|---------|---------------------|---------------------|---------------------|---------------------|
| AC | 65.3 | 14.7 | 29.8 | 13.4 |
| CC | 72.0 | 11.5 | 246.2 | 27.4 |
| GT | 56.2 | 21.5 | 22.5 | 7.2 |
| HRSG | 43.5 | 28.1 | 64.8 | 27.2 |
| P | 0.5 | 0.1 | 0.3 | 0.1 |

### 6.6 Standart vs İleri Karşılaştırma

| Bileşen | Standart Sıra (Ċ_D+Ż) | İleri Sıra (Ċ_D^AV,EN + Ż^AV) | Değişim |
|---------|------------------------|-------------------------------------|---------|
| CC | 1. (360.9 €/h) | 2. (73.3 €/h) | ↓ Öncelik düştü |
| HRSG | 3. (172.1 €/h) | 3. (46.9 €/h) | = Aynı kaldı |
| AC | 4. (135.6 €/h) | 1. (69.5 €/h) | ↑ Öncelik arttı |
| GT | 2. (130.0 €/h) | 4. (64.0 €/h) | ↓ Öncelik düştü |
| P | 5. (1.3 €/h) | 5. (0.6 €/h) | = Aynı kaldı |

### 6.7 Yorumlama

```
Standart Analiz Söylüyor:
  "Yanma odası en çok para kaybettiriyor → Önce onu iyileştir"

İleri Analiz Düzeltiyor:
  "Yanma odasının yıkımının %77'si kaçınılmaz → Gerçek potansiyel sınırlı"
  "Hava kompresörünün AV-EN yıkımı en yüksek → Önce kompresörü iyileştir"

Sonuç:
  1. AC (kompresör): ε artır → VSD, inter-cooling düşün
  2. CC (yanma odası): Kaçınılabilir kısım sınırlı → Hava ön ısıtma ile iyileştir
  3. HRSG: AV-EX yüksek → Üst akış bileşenlerini iyileştirerek dolaylı kazanım
  4. GT: AV-EX yüksek → Kompresör iyileştirmesi türbine de fayda sağlar
```

## 7. Uygulama Kılavuzu

### 7.1 Ne Zaman İleri Analiz Gerekir?

```
İleri analiz önerilir:
  ✓ Sistem 4+ bileşen içeriyorsa
  ✓ Standart analizde kazan/yanma odası en yüksek Ċ_D'ye sahipse
    (büyük kısmı kaçınılmaz olabilir)
  ✓ Bileşenler arası etkileşim güçlüyse (CHP, kombine çevrim)
  ✓ Detaylı optimizasyon planlanıyorsa
  ✓ Yatırım bütçesi sınırlıysa (doğru önceliklendirme kritik)

İleri analiz gereksiz:
  ✗ 2-3 bileşenli basit sistemler
  ✗ Ön fizibilite aşaması
  ✗ Tek ekipman analizi (kompresör, pompa tek başına)
```

### 7.2 Kaçınılmaz Koşul Belirleme Rehberi

```
Her bileşen için:
1. Teknolojik üst sınırı belirle (en iyi ticari verim)
2. Ekonomik sınırı belirle (makul maliyetli en iyi teknoloji)
3. İkisinin daha düşük olanını al

Kaynak:
  - Üretici katalogları (en verimli modeller)
  - Akademik literatur (state-of-the-art)
  - Endüstri standartları (ISO, API)

Dikkat: Kaçınılmaz koşullar subjektiftir → Duyarlılık analizi yapılmalı
```

## 8. Sınırlamalar

```
1. Hesaplama yoğunluğu: n bileşenli sistem → n+1 simülasyon gerekli
2. Kaçınılmaz koşul tanımı subjektif → Sonuçlar uzman yargısına bağlı
3. Eksojen yıkımın kaynak bileşenini belirlemek her zaman kolay değil
4. Geçici (transient) rejimler için uygulanabilirlik sınırlı
5. Doğrulama zorluğu — deneysel karşılaştırma sınırlı
```

## İlgili Dosyalar

- `factory/exergoeconomic/evaluation_criteria.md` — Standart değerlendirme (f_k, r_k, Ċ_D)
- `factory/exergoeconomic/speco_method.md` — SPECO adımları
- `factory/exergoeconomic/optimization.md` — Optimizasyon yöntemleri
- `factory/exergoeconomic/worked_examples/cogeneration.md` — CHP tam örneği
- `factory/exergoeconomic/sensitivity_analysis.md` — Kaçınılmaz koşul duyarlılığı

## Referanslar

1. Tsatsaronis, G., Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270.
2. Kelly, S., Tsatsaronis, G., Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391.
3. Morosuk, T., Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(3), 229-238.
4. Morosuk, T., Tsatsaronis, G. (2013). "Advanced exergoeconomic analysis of a refrigeration machine." *Proceedings of ECOS 2013*, Paper #295.
5. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T., Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152.
6. Tsatsaronis, G. (2008). "Recent developments in exergy analysis and exergoeconomics." *Int. J. Exergy*, 5(5-6), 489-499.
