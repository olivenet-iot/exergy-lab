---
title: "Soğutma Prosesi (Cooling Process)"
category: factory
equipment_type: factory
keywords: [soğutma, cooling, chiller, COP, ters Carnot, exergy, endüstriyel soğutma, BAT, ICS BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/cold_storage.md, chiller/benchmarks.md]
use_when: ["Soğutma prosesi exergy analizi yapılacakken", "Chiller sistemi performansı değerlendirilecekken", "Soğutma BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Soğutma Prosesi (Cooling Process)

---

## 1. Proses Tanımı

### Nedir?
Soğutma prosesi, bir ortam veya akışkandan ısıyı alarak çevre sıcaklığının altına veya belirli bir hedef sıcaklığa düşürme işlemidir. Termodinamiğin 2. yasasına göre ısının düşük sıcaklıktan yüksek sıcaklığa transferi için dışarıdan iş (exergy) girişi gerekir.

### Nerede Kullanılır?
- Proses soğutma (kimya, plastik, metal işleme)
- İklimlendirme (endüstriyel bina, sunucu odası)
- Gıda soğutma (süt, et, içecek üretim hattı)
- Soğutmalı depolama (bkz. `cold_storage.md`)
- Kurutma sonrası soğutma

### İlgili Ekipmanlar
- Santrifüj chillerlar: 200 – 10.000+ kW
- Vidalı chillerlar: 50 – 1.500 kW
- Scroll chillerlar: 10 – 200 kW
- Absorpsiyon chillerlar: 100 – 5.000 kW (atık ısı ile çalışır)
- Soğutma kuleleri (wet/dry/hybrid)
- Free cooling (serbest soğutma) üniteleri

### Tipik Ölçek
- Küçük: 10 – 100 kW soğutma
- Orta: 100 – 1.000 kW soğutma
- Büyük: 1.000 – 10.000+ kW soğutma

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Soğutma prosesi için minimum exergy gereksinimi (ters Carnot çevriminden):

$$Ex_{min} = Q_{cold} \times \left(\frac{T_0}{T_{cold}} - 1\right)$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| Q_cold | Soğutma yükü (uzaklaştırılan ısı) | kW |
| T₀ | Çevre (kondenser) sıcaklığı | K |
| T_cold | Soğutulan ortamın sıcaklığı | K |

### 2.1b Ters Carnot Türetimi (2. Yasa Temeli)

Soğutma prosesinin termodinamik temeli, ters Carnot çevrimidir:

**Adım 1: 2. Yasa — ısı transferi yönü**
Isı doğal olarak sıcaktan soğuğa akar. Soğuk bir ortamdan ısı çekmek için dışarıdan iş (exergy) girişi gerekir.

**Adım 2: Carnot soğutma çevrimi**
Tersinir soğutma çevriminde:
$$COP_{Carnot} = \frac{Q_{cold}}{W_{min}} = \frac{T_{cold}}{T_0 - T_{cold}}$$

**Adım 3: Minimum iş**
$$W_{min} = \frac{Q_{cold}}{COP_{Carnot}} = Q_{cold} \times \frac{T_0 - T_{cold}}{T_{cold}} = Q_{cold} \times \left(\frac{T_0}{T_{cold}} - 1\right)$$

**Adım 4: Bu, soğutmanın exergy'sidir**
$$Ex_{min} = Q_{cold} \times \left(\frac{T_0}{T_{cold}} - 1\right)$$

**Fiziksel anlam:** Soğutma sıcaklığı düştükçe, aynı miktarda ısıyı çekmek için daha fazla iş gerekir. Bu termodinamik zorunluluk, derin dondurma sistemlerinin neden daha fazla enerji tükettiğini açıklar.

**Sıcaklık etkisinin görselleştirilmesi:**

| ΔT = T₀ − T_cold | T_cold (°C) | COP_Carnot | W_min/Q_cold | Yorum |
|-------------------|-------------|------------|-------------|-------|
| 20 °C | 15 | 14.4 | 0.069 | Çok az iş gerekir |
| 28 °C | 7 | 10.0 | 0.100 | Standart chiller |
| 35 °C | 0 | 7.8 | 0.128 | Donma noktası |
| 55 °C | −20 | 4.6 | 0.217 | Donmuş gıda |
| 65 °C | −30 | 3.7 | 0.267 | Derin dondurma |
| 75 °C | −40 | 3.2 | 0.322 | Ultra düşük sıcaklık |

> **Tasarım kuralı:** Her 10 °C soğutma sıcaklığı düşüşü, exergy gereksinimini yaklaşık %15-25 artırır. Bu nedenle "gerçekten gerekli olan minimum sıcaklığı kullan" en temel tasarruf stratejisidir.

**Kaynak:** Kotas (1985), Bölüm 2, s. 20-24; ASHRAE Handbook — Fundamentals (2021), Ch. 2.

### 2.2 Sıcaklığa Bağlı Minimum COP ve Exergy

| T_cold (°C) | T₀ (°C) | COP_Carnot | Ex_min/Q_cold | Ex_min oranı |
|-------------|---------|------------|---------------|-------------|
| 15 | 35 | 14.4 | 0.069 | %6.9 |
| 7 | 35 | 10.0 | 0.100 | %10.0 |
| 0 | 35 | 7.80 | 0.128 | %12.8 |
| −10 | 35 | 5.85 | 0.171 | %17.1 |
| −18 | 35 | 4.81 | 0.208 | %20.8 |
| −30 | 35 | 4.00 | 0.267 | %26.7 |
| −40 | 35 | 3.23 | 0.322 | %32.2 |

> **Kritik Bilgi:** Soğutma sıcaklığı düştükçe exergy gereksinimi dramatik artar. −30 °C soğutma, +7 °C soğutmadan ~2.7 kat daha fazla exergy gerektirir.

### 2.3 Çözümlü Örnek

**Problem:** 500 kW soğutma kapasiteli chiller, T_cold = 7 °C, T₀ = 35 °C.

```
T_cold = 7 + 273.15 = 280.15 K
T₀ = 35 + 273.15 = 308.15 K

Ex_min = 500 × (308.15/280.15 − 1)
       = 500 × (1.100 − 1)
       = 500 × 0.100
       = 50 kW

COP_Carnot = T_cold / (T₀ − T_cold) = 280.15 / 28 = 10.0
COP_actual (tipik santrifüj) = 5.0

W_actual = Q_cold / COP_actual = 500 / 5.0 = 100 kW

ESI = Ex_min / W_actual = 50 / 100 = 0.50 → Derece A
```

**Not:** Chiller ESI = 0.50 çok yüksek görünür çünkü modern santrifüj chillerlar yüksek COP'ta çalışır. Ancak kondenser sıcaklığı yükseldiğinde veya kısmi yükte ESI düşer.

**Kaynak:** ASHRAE Handbook — Fundamentals; Dincer & Rosen (2013).

### 2.4 Çözümlü Örnek: Dondurulmuş Gıda Soğutma (−18 °C)

**Problem:** 200 kW soğutma kapasiteli donmuş gıda hattı. T_cold = −18 °C, T₀ = 35 °C. NH₃ vidalı kompresör, COP = 1.8.

```
T_cold = −18 + 273.15 = 255.15 K
T₀ = 308.15 K

Ex_min = 200 × (308.15/255.15 − 1) = 200 × 0.208 = 41.6 kW

W_actual = Q_cold / COP = 200 / 1.8 = 111.1 kW

ESI = 41.6 / 111.1 = 0.374 → Derece B
η_ex (2. yasa COP) = COP_actual / COP_Carnot = 1.8 / 4.81 = 0.374
```

**Yorum:**
- ESI = 0.374 (Derece B) — donmuş gıda soğutma için çok iyi
- NH₃ kompresör COP = 1.8 → Carnot veriminin %37.4'ü
- R404A kullansaydık (COP ≈ 1.3): ESI = 41.6/153.8 = 0.270 → Derece C
- **NH₃ avantajı:** Aynı koşullarda %38 daha az enerji → önemli exergy tasarrufu

### 2.5 Çözümlü Örnek: Proses Soğutma (15 °C)

**Problem:** 1.000 kW kapasiteli proses soğutma. T_cold = 15 °C, T₀ = 35 °C. Santrifüj chiller COP = 6.5.

```
T_cold = 15 + 273.15 = 288.15 K
T₀ = 308.15 K

Ex_min = 1000 × (308.15/288.15 − 1) = 1000 × 0.069 = 69.4 kW

W_actual = 1000 / 6.5 = 153.8 kW

ESI = 69.4 / 153.8 = 0.451 → Derece B
```

**Free cooling potansiyeli (T_dış < 12 °C olan aylar):**
```
Türkiye (İstanbul), yıllık T_dış < 12 °C: ~2.800 saat (%32)
Free cooling modunda: W = sadece pompa/fan ≈ 25 kW

Ağırlıklı yıllık ESI:
  ESI_chiller (5960 h) = 0.451
  ESI_free (2800 h) = 69.4 / 25 = 2.78 → efektif ESI >> 1 (neredeyse bedava)

  Ağırlıklı: (0.451 × 5960 + 2.78 × 2800) / 8760 = 1.20 (!)
  Ancak pratikte: yıllık enerji tasarrufu ≈ %35 → etkili ESI ≈ 0.70
```

> **Sonuç:** 15 °C proses soğutmada free cooling büyük avantaj sağlar. Ağırlıklı yıllık ESI 0.451'den ~0.70'e yükselir.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 COP Aralıkları (Endüstriyel)

| Chiller Tipi | COP Aralığı | Tipik COP | T_cold |
|-------------|------------|-----------|--------|
| Santrifüj (su soğutmalı) | 5.0 – 7.0 | 5.5 | 7 °C |
| Vidalı (su soğutmalı) | 4.0 – 5.5 | 4.5 | 7 °C |
| Scroll (hava soğutmalı) | 2.5 – 3.5 | 3.0 | 7 °C |
| Absorpsiyon (tek etkili) | 0.6 – 0.8 | 0.7 | 7 °C |
| Absorpsiyon (çift etkili) | 1.0 – 1.4 | 1.2 | 7 °C |
| Amonyak (endüstriyel, −30 °C) | 1.5 – 2.5 | 2.0 | −30 °C |

### 3.2 Sistem ESI Aralıkları

| Soğutma Sistemi | ESI Aralığı | Tipik ESI | Not |
|----------------|------------|-----------|-----|
| Santrifüj + soğutma kulesi | 0.25 – 0.45 | 0.35 | En verimli ticari |
| Vidalı + soğutma kulesi | 0.20 – 0.35 | 0.27 | Yaygın endüstriyel |
| Hava soğutmalı scroll | 0.10 – 0.20 | 0.15 | Küçük tesisler |
| Absorpsiyon (atık ısı) | 0.15 – 0.30 | 0.22 | Atık ısı varsa avantajlı |

### 3.3 Irreversibilite Kaynakları

1. **Kompresör irreversibilitesi:** %30 – %45 — İzentropik verim sınırı
2. **Kondenser ΔT:** %15 – %25 — Soğutma suyu/hava ile sıcaklık farkı
3. **Evaporatör ΔT:** %10 – %20 — Soğutulan akışkan ile soğutucu akışkan farkı
4. **Genleşme valfi (kısılma):** %5 – %10 — İsentalpik genleşme irreversibilitesi
5. **Pompa ve fan:** %3 – %8 — Soğutma kulesi fanı, soğuk su pompası
6. **Boru ve izolasyon kayıpları:** %2 – %5 — Soğuk hat ısı kazancı

---

## 4. BAT Referansı

### 4.1 EU BREF ICS 2001 (Industrial Cooling Systems)

| Parametre | BAT Açıklaması | Not |
|-----------|----------------|-----|
| Soğutma kulesi yaklaşımı | 3 – 5 °C | Wet cooling tower |
| Free cooling entegrasyonu | Kış/geçiş mevsimlerinde | T_dış < T_soğuk su + 3 °C |
| Değişken debi kontrolü | VFD pompa + VFD fan | Kısmi yükte tasarruf |
| Su tüketimi | Minimizasyon, blowdown kontrolü | Çevresel BAT |

> **Not:** ICS BREF 2001 yılına ait olup güncel değildir. Modern chiller performans değerleri bu dokümanı aşmıştır.

### 4.2 ASHRAE / ARI Standartları (Güncel Referans)

| Chiller Tipi | BAT COP (ARI 550/590) | Tam Yük | IPLV |
|-------------|----------------------|---------|------|
| Santrifüj (su soğutmalı) | 6.0 – 7.0 | Tam yük | 8.0 – 10.0 |
| Vidalı (su soğutmalı) | 4.5 – 5.5 | Tam yük | 6.0 – 7.5 |
| Hava soğutmalı scroll | 3.0 – 3.5 | Tam yük | 4.0 – 4.5 |

### 4.3 BAT Exergy Değerleri

| Sistem | BAT COP | BAT ESI (7 °C, T₀=35 °C) | Kaynak |
|--------|---------|--------------------------|--------|
| Santrifüj + wet tower + VFD | 6.5 | 0.33 – 0.38 | ASHRAE 90.1 + exergy dönüşüm |
| Free cooling + chiller hibrit | — | 0.40 – 0.55 | Tahmini, mevsime bağlı |
| Absorpsiyon (atık ısı, exergy bazlı) | — | 0.30 – 0.50 | Exergy bazlı COP, literatür |

---

## 4b. Absorpsiyon Chiller Detayı

### 4b.1 Çalışma Prensibi

Absorpsiyon chillerlar, kompresör yerine termal enerji (ısı) ile çalışır. Kompresyon soğutma çevrimindeki mekanik kompresörün yerini "termal kompresör" (jeneratör + absorber çifti) alır. Bu, düşük kaliteli ısı kaynaklarını soğutma üretimi için kullanma imkanı verir.

Soğutucu akışkan çifti:
- **LiBr-Su:** Soğutma > 0 °C (konfor ve proses soğutma). Su soğutucu akışkan, LiBr absorber. Kristalizasyon riski nedeniyle evaporatör sıcaklığı 4 °C altına düşemez.
- **NH₃-Su:** Soğutma < 0 °C (endüstriyel, dondurma). NH₃ soğutucu akışkan, su absorber. Rektifikasyon kolonu gerektirir (su buharını ayırmak için).

**Absorpsiyon çevrimi adımları:**
1. **Jeneratör (Generator):** Isı girişi ile zayıf çözeltiden soğutucu akışkan buharlaştırılır
2. **Kondenser:** Soğutucu akışkan buharı yoğuşur, ısı dışarı atılır
3. **Genleşme valfi:** Sıvı soğutucu akışkan basınç düşürülerek evaporatöre gönderilir
4. **Evaporatör (Evaporator):** Soğutucu akışkan buharlaşarak soğutma üretir
5. **Absorber:** Buhar, güçlü çözelti tarafından absorbe edilir, ısı dışarı atılır
6. **Çözelti pompası:** Zayıf çözelti jeneratöre geri pompalanır (çok az elektrik)

### 4b.2 Performans Karşılaştırması

| Tip | Sürücü Isı T (°C) | COP_termal | COP_exergy | Ex Kaynak |
|-----|-------------------|------------|-----------|-----------|
| Tek etkili (LiBr) | 80-110 | 0.65-0.80 | 0.25-0.40 | Atık ısı, buhar |
| Çift etkili (LiBr) | 120-170 | 1.00-1.40 | 0.30-0.50 | Yüksek T buhar, doğrudan yakma |
| Üç etkili (LiBr) | 200+ | 1.40-1.70 | 0.35-0.55 | Doğrudan yakma |
| Tek etkili (NH₃-Su) | 100-150 | 0.50-0.65 | 0.20-0.35 | Atık ısı |

### 4b.3 Exergy Perspektifi — Ne Zaman Absorpsiyon?

Absorpsiyon chiller'ın exergy avantajı, **ısı kaynağının maliyetine** bağlıdır:

```
Senaryo A: Doğal gaz ile çalışan çift etkili absorpsiyon
  COP_th = 1.2, T_kaynak = 150 °C, T_cold = 7 °C
  Ex_giriş = Q_cool/COP_th × (1 − 298.15/423.15) = Q × 0.833 × 0.295 = 0.246 × Q
  ESI = 0.10 × Q / 0.246 × Q = 0.407

Senaryo B: BEDAVA atık ısı (100 °C) ile tek etkili
  COP_th = 0.70, T_kaynak = 100 °C (atık ısı, exergy maliyeti ≈ 0)
  Ex_giriş ≈ pompa/fan gücü ≈ 0.05 × Q_cool
  ESI = 0.10 × Q / 0.05 × Q = 2.0 (!) → pratikte çok yüksek

Senaryo C: Elektrikli santrifüj chiller
  COP = 5.5, Ex_giriş = Q/5.5 = 0.182 × Q
  ESI = 0.10 × Q / 0.182 × Q = 0.549
```

**Sonuç:** Atık ısı bedavaysa absorpsiyon her zaman kazanır. Doğal gaz ile çalışıyorsa, elektrikli chiller daha iyi exergy verir.

> **AI Kuralı:** Absorpsiyon chiller önerirken HER ZAMAN ısı kaynağını sor. Atık ısı → kesinlikle öner. Yakıt → elektrikli chiller ile exergy karşılaştırması yap.

---

## 4c. Doğal Soğutucu Akışkan Karşılaştırması

### 4c.1 F-Gas Regulation (517/2014) Bağlamı

EU F-Gas Yönetmeliği, yüksek GWP soğutucu akışkanların kademeli olarak azaltılmasını gerektirmektedir. 2030'a kadar HFC kullanımı 2015 seviyesinin %21'ine düşürülecektir.

**Kademeli azaltım takvimi (HFC phase-down):**

| Yıl | İzin verilen miktar (2015 bazlı) | Etkisi |
|-----|----------------------------------|--------|
| 2015 | %100 (baz yıl) | Referans |
| 2018 | %63 | İlk ciddi kısıtlama |
| 2021 | %45 | R404A fiyat artışı |
| 2024 | %31 | GWP > 2500 yasağı (yeni sistemler) |
| 2027 | %24 | GWP > 750 yasağı (yeni split AC) |
| 2030 | %21 | Kapsamlı kısıtlama |

**Exergy bağlantısı:** Doğal soğutucu akışkanlar (NH₃, CO₂, propan) genellikle HFC'lerden daha iyi termodinamik özelliklere sahiptir. F-Gas geçişi, exergy verimini artırma fırsatıdır.

> **AI Kuralı:** Soğutucu akışkan önerirken GWP değerini ve F-Gas uyumluluğunu belirt. Yeni tesis → doğal soğutucu akışkan öner. Mevcut tesis → retrofit maliyeti vs. yeni sistem değerlendirmesi yap.

### 4c.2 Soğutucu Akışkan Karşılaştırma Tablosu

| Soğutucu | Tip | GWP | ODP | T_buharlaşma (°C) | COP (7°C) | COP (−30°C) | Güvenlik | Maliyet |
|----------|-----|-----|-----|-------------------|----------|-------------|----------|---------|
| R717 (NH₃) | Doğal | 0 | 0 | −33 | 5.5-6.0 | 1.5-2.0 | B2L (toksik) | Düşük |
| R744 (CO₂) | Doğal | 1 | 0 | −56 (transkritik) | 3.5-4.5 | 1.2-1.8 | A1 (güvenli) | Düşük |
| R290 (propan) | Doğal | 3 | 0 | −42 | 4.5-5.5 | 1.3-1.8 | A3 (yanıcı) | Düşük |
| R600a (izobütan) | Doğal | 3 | 0 | −12 | 4.0-5.0 | — | A3 (yanıcı) | Düşük |
| R134a | HFC | 1430 | 0 | −26 | 5.0-5.5 | — | A1 | Orta |
| R404A | HFC karışım | 3922 | 0 | −46 | 3.5-4.0 | 1.0-1.5 | A1 | Yüksek |
| R1234yf | HFO | <1 | 0 | −29 | 4.5-5.0 | — | A2L (düşük yanıcı) | Çok yüksek |

### 4c.3 Exergy Perspektifinde Soğutucu Seçimi

NH₃ ve CO₂'nin termodinamik avantajları exergy analizinde belirginleşir:

| Senaryo (−20 °C, T₀ = 35 °C) | COP | ESI | Yıllık Exergy Tasarrufu (500kW) |
|-------------------------------|-----|-----|----------------------------------|
| R404A vidalı | 1.3 | 0.282 | Referans |
| NH₃ vidalı | 2.0 | 0.434 | 52.5 kW (%36 daha az) |
| NH₃/CO₂ kaskad | 2.4 | 0.521 | 78.4 kW (%51 daha az) |

> **Engine değeri:** bat_references.py → cooling/process: exergy_efficiency_pct = 35%. NH₃ ile %43-52 ulaşılabilir. Literatür aralığı: %28-55.

---

## 4d. Bölge Soğutma (District Cooling) ve İklim Bazlı Free Cooling

### 4d.1 Bölge Soğutma Sistemi

Büyük endüstriyel bölgelerde merkezi soğutma tesisi + dağıtım ağı ile:
- Ölçek avantajı: Büyük santrifüj chiller COP > 6.0
- Termal depolama entegrasyonu (gece/gündüz dengeleme)
- Atık ısı kaynağı paylaşımı (absorpsiyon)
- Çeşitlendirme etkisi: Farklı kullanıcıların pik yükleri örtüşmez → daha küçük toplam kapasite

| Parametre | Bireysel Chiller | Bölge Soğutma |
|-----------|-----------------|---------------|
| Tipik COP | 4.0-5.5 | 5.5-7.0 |
| Yedeklilik | N+1 pahalı | Havuz avantajı |
| Bakım | Dağınık | Merkezi, uzman |
| ESI (7 °C) | 0.25-0.35 | 0.35-0.50 |
| Yatırım (€/kW soğutma) | 200-400 | 400-800 (dağıtım dahil) |
| İşletme maliyeti (€/MWh_cool) | 30-50 | 20-35 |

**Termal enerji depolama (TES) entegrasyonu:**

| TES Tipi | Kapasite (kWh/m³) | Avantaj | Dezavantaj |
|----------|-------------------|---------|------------|
| Soğuk su tankı | 5-7 | Basit, düşük maliyet | Büyük hacim |
| Buz depolama | 40-50 | Kompakt | Düşük COP (−5 °C üretim) |
| Ötektik PCM | 20-30 | Orta kompakt | Yüksek maliyet |

```
TES ile exergy avantajı:
  Gece üretimi (T_dış = 22 °C): COP_chiller = 7.0 → ESI = 0.45
  Gündüz üretimi (T_dış = 38 °C): COP_chiller = 4.5 → ESI = 0.29

  TES ile ağırlıklı ESI: ~0.40 (gece üretim ağırlıklı)
  TES olmadan: ~0.32 (gündüz pik ağırlıklı)

  Tasarruf: %25 daha iyi exergy performansı
```

> **Sonuç:** TES, soğutma üretimini düşük çevre sıcaklığı saatlerine kaydırarak hem enerji maliyetini hem de exergy yıkımını azaltır.

### 4d.2 İklim Bölgesi Bazlı Free Cooling Potansiyeli

| İklim Bölgesi | Örnek Şehir | T_dış < 12°C Saat/Yıl | Free Cooling Potansiyeli (15°C soğutma) | Yıllık Tasarruf |
|---------------|-------------|------------------------|----------------------------------------|-----------------|
| Soğuk kıta | Helsinki | 6.500 h | %74 | %60-70 |
| Ilıman okyanus | Londra | 5.500 h | %63 | %50-60 |
| Ilıman kıta | İstanbul | 2.800 h | %32 | %25-35 |
| Sıcak Akdeniz | Antalya | 1.500 h | %17 | %12-18 |
| Sıcak çöl | Dubai | 200 h | %2 | %1-3 |

> **AI Kuralı:** Free cooling değerlendirmesinde tesisin iklim bölgesini ve proses soğutma sıcaklığını sor. T_cold > 10 °C ve ılıman iklim → kesinlikle öner.

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Kompresör | 30 – 45 | Orta (daha verimli kompresör) |
| 2 | Kondenser ΔT | 15 – 25 | Yüksek (soğutma kulesi bakımı) |
| 3 | Evaporatör ΔT | 10 – 20 | Orta (yüzey temizliği, ΔT azaltma) |
| 4 | Kısılma valfi | 5 – 10 | Düşük (ekonomizer, ejektör) |
| 5 | Pompa / fan | 3 – 8 | Yüksek (VFD) |
| 6 | Boru/izolasyon | 2 – 5 | Yüksek (izolasyon onarımı) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Soğutma kulesi bakımı + optimizasyonu** | %5-15 enerji | 0-1 yıl | Kondenser ΔT azaltma; her 1 °C düşüş ≈ %2.5 COP artışı |
| 2 | **Free cooling (serbest soğutma)** | %20-50 enerji | 1-3 yıl | Kış/geçiş mevsimlerinde kompresör devre dışı; iklime bağlı |
| 3 | **VFD (pompa + fan + kompresör)** | %15-30 enerji | 2-4 yıl | Kısmi yükte dramatik tasarruf |
| 4 | **Soğuk su sıcaklığı artırma** | %3-8 enerji | 0 (operasyonel) | Her 1 °C artış ≈ %2-3 COP artışı; kullanıcı ihtiyacını kontrol et |
| 5 | **Atık ısı ile absorpsiyon** | %30-60 birincil enerji | 3-7 yıl | Atık ısı kaynağı varsa; exergy bazlı değerlendirme gerekli |
| 6 | **Termal enerji depolama (TES)** | %10-25 enerji | 3-5 yıl | Gece üretim + gündüz deşarj; elektrik pik tasarrufu |
| 7 | **Kaskad soğutma (NH₃/CO₂)** | %20-40 enerji | 4-7 yıl | Düşük sıcaklık (< −20 °C) uygulamalarında |
| 8 | **Kondenser basınç optimizasyonu** | %3-10 enerji | 0-1 yıl | Floating head pressure; T_dış'a göre otomatik ayar |
| 9 | **Ekonomizer / alt-soğutucu** | %5-12 enerji | 2-3 yıl | Flash gas ekonomizer veya mekanik alt-soğutucu |
| 10 | **Doğal soğutucu akışkana geçiş** | %5-20 enerji | 5-10 yıl | NH₃, CO₂ veya propan; daha iyi termodinamik özellikler |

### 6.1 Strateji Detayları

**Strateji 1 — Soğutma Kulesi Bakımı:**
```
Kirli kondenser etkisi:
  Temiz: T_cond = 35 °C → COP = 5.5
  Kirli (+3 °C): T_cond = 38 °C → COP = 4.8 (%13 düşüş)
  Çok kirli (+6 °C): T_cond = 41 °C → COP = 4.2 (%24 düşüş)

Bakım maliyeti: ~500-2.000 €/yıl
Enerji tasarrufu: 500 kW chiller × 5000 h × %13 COP artışı ≈ 11.800 € /yıl
```

**Strateji 3 — VFD Tasarruf Profili:**

| Yük Oranı (%) | Sabit Hız Güç (%) | VFD Güç (%) | Tasarruf (%) |
|----------------|-------------------|-------------|-------------|
| 100 | 100 | 100 | 0 |
| 75 | 85 | 60 | 29 |
| 50 | 70 | 35 | 50 |
| 25 | 55 | 18 | 67 |

> **Not:** Küp yasası (affinity laws): Güç ∝ Debi³. VFD ile %50 yük → ~%35 güç tüketimi. Soğutma kulesi fanları ve pompaları için çok etkili.

**Strateji 8 — Floating Head Pressure (Kondenser basınç optimizasyonu):**
```
Sabit kondenser basıncı yaklaşımı (geleneksel):
  T_cond = 40 °C sabit → yaz aylarında gerekli, kışın aşırı

Floating head pressure (optimum):
  T_cond = T_dış_yaş + 5 °C (minimum 25 °C)
  Kış (T_dış = 5 °C): T_cond = 25 °C → COP = 7.5
  Yaz (T_dış = 35 °C): T_cond = 40 °C → COP = 4.5
  Ağırlıklı yıllık COP artışı: %8-15

Exergy etkisi:
  Düşük T_cond → düşük kompresör basınç oranı → düşük irreversibilite
```

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER T_cold > 0 °C (proses soğutma):
  → ESI > 0.35 "Soğutma prosesi için çok iyi"
  → ESI 0.20-0.35 "İyi, iyileştirme fırsatları var"
  → ESI < 0.20 "Düşük — COP ve sistem kayıpları incele"

EĞER T_cold: −18 °C ile 0 °C arası (orta dereceli):
  → ESI > 0.25 "Orta sıcaklık soğutma için çok iyi"
  → ESI 0.15-0.25 "Kabul edilebilir"
  → ESI < 0.15 "Zayıf — kompresör verimi ve izolasyon kontrol et"

EĞER T_cold < −18 °C (derin dondurma):
  → ESI > 0.20 "Derin dondurma için iyi"
  → ESI 0.10-0.20 "Ortalama"
  → ESI < 0.10 "Zayıf — kademeli soğutma ve süperizolayon öner"
```

### 7.2 Anahtar Kontrol Noktaları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| COP (7 °C su, su soğutmalı) | > 5.5 | 4.0-5.5 | < 4.0 |
| Kondenser yaklaşımı | < 3 °C | 3-5 °C | > 5 °C |
| Evaporatör yaklaşımı | < 3 °C | 3-5 °C | > 5 °C |
| Kısmi yük verimi (IPLV/NPLV) | > 7.0 | 5.0-7.0 | < 5.0 |

### 7.3 Free Cooling Potansiyeli

```
EĞER T_cold > 10 °C VE iklim ılıman/soğuk:
  → "Yıllık saatlerin %30-60'ında free cooling mümkün"
  → "Yıllık enerji tasarrufu %20-40 olabilir"

EĞER T_cold < 5 °C:
  → "Free cooling potansiyeli sınırlı — sadece kış ayları"
```

### 7.4 Soğutucu Akışkan Değerlendirmesi

```
EĞER soğutucu = R404A veya R507A:
  → "Yüksek GWP (>3900) — F-Gas Yönetmeliği kapsamında 2024'ten itibaren yeni sistemlerde yasak"
  → "NH₃ veya CO₂ alternatifi değerlendir — hem GWP hem COP avantajı"

EĞER soğutucu = R134a:
  → "Orta GWP (1430) — kısa vadede kullanılabilir ancak uzun vadede geçiş planla"
  → "R1234yf veya R290 alternatifi değerlendir"

EĞER soğutucu = NH₃ veya CO₂:
  → "Doğal soğutucu akışkan — mükemmel GWP profili"
  → "Güvenlik gereksinimlerini (NH₃: toksisite, CO₂: yüksek basınç) kontrol et"
```

### 7.5 Absorpsiyon Chiller Karar Ağacı

```
EĞER atık_ısı_mevcut VE T_atık > 80 °C VE Q_atık > Q_cool/0.7:
  → "Absorpsiyon chiller kesinlikle değerlendir"
  → "Atık ısı bedavaysa ESI çok yüksek olabilir (>1.0)"
  → EĞER T_atık > 140 °C:
    → "Çift etkili absorpsiyon — COP 1.0-1.4"
  → DEĞİLSE:
    → "Tek etkili absorpsiyon — COP 0.6-0.8"

EĞER atık_ısı_yok:
  → "Absorpsiyon önermeden önce yakıt maliyeti ile elektrik maliyetini karşılaştır"
  → "Genellikle elektrikli chiller daha iyi exergy verir"
```

### 7.6 Sektör Bazlı Soğutma Yorumu

| Sektör | Tipik T_cold | Öncelikli Strateji | Dikkat Noktası |
|--------|-------------|-------------------|----------------|
| Gıda — süt işleme | 2-4 °C | Hijyen standartları, soğuk zincir | HACCP uyumu |
| Gıda — dondurulmuş | −18 ile −25 °C | NH₃ kaskad, süperizolasyon | Enerji yoğun |
| Kimya — reaktör soğutma | 5-15 °C | Proses kararlılığı, free cooling | Sıcaklık hassasiyeti |
| Plastik — kalıp soğutma | 10-25 °C | Free cooling, soğuk su T artır | Geniş T_cold aralığı |
| Metal — hadde soğutma | 30-40 °C | Soğutma kulesi yeterli olabilir | Exergy gereksinimi çok düşük |
| Veri merkezi | 12-18 °C | Free cooling, adiabatik soğutma | 7/24 yük |
| İlaç — temiz oda | 18-22 °C | Hassas nem kontrolü | Enerji yoğun HVAC |

```
EĞER sektör = "metal" VE T_cold > 25 °C:
  → "Soğutma kulesi (wet/dry) yeterli olabilir — chiller gereksiz"
  → "Exergy gereksinimi çok düşük, basit çözümler öncelikli"

EĞER sektör = "veri_merkezi":
  → "Free cooling + adiabatik soğutma hibrit sistemi değerlendir"
  → "ASHRAE A1 sınıfı: inlet 18-27 °C → geniş free cooling penceresi"
  → "PUE (Power Usage Effectiveness) hedefi < 1.3"
```

### 7.7 Kısmi Yük Davranışı

Endüstriyel soğutma sistemleri genellikle tam yük kapasitesinin %40-70'inde çalışır. Kısmi yük performansı, yıllık exergy verimliliği için kritiktir.

```
Kısmi yük ESI düzeltmesi:
  EĞER VFD var VE yük_oranı < 0.7:
    → ESI_kısmi ≈ ESI_tam × 1.10 (VFD'li chiller kısmi yükte daha verimli)
  EĞER VFD yok VE yük_oranı < 0.5:
    → ESI_kısmi ≈ ESI_tam × 0.70 (on/off veya inlet vane kontrol → kayıp artar)

Çoklu chiller stratejisi:
  EĞER N_chiller > 2:
    → "Sıralı yükleme (sequential loading) ile her chiller optimum noktada çalıştır"
    → "1 büyük + 1 küçük chiller kombinasyonu → geniş yük aralığında yüksek COP"
```

---

## İlgili Dosyalar

- `factory/process/cold_storage.md` — Soğuk depolama prosesi (uzun süreli)
- `chiller/benchmarks.md` — Chiller ekipman benchmark
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri
- `factory/heat_integration.md` — Isı entegrasyonu (atık ısı → absorpsiyon)
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanım teknolojileri

## Referanslar

1. European Commission, JRC (2001). *Reference Document on the Application of Best Available Techniques to Industrial Cooling Systems (ICS BREF)*.
2. ASHRAE (2021). *ASHRAE Handbook — Fundamentals*. Ch. 2 — Thermodynamics.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Soğutma çevrimi exergy analizi.
4. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
5. ARI Standard 550/590 (2023). *Performance Rating of Water-Chilling Packages*.
6. EU Regulation 517/2014 on Fluorinated Greenhouse Gases (F-Gas Regulation). — Soğutucu akışkan GWP sınırlamaları.
7. Herold, K.E., Radermacher, R. & Klein, S.A. (2016). *Absorption Chillers and Heat Pumps*. 2nd ed., CRC Press. — Absorpsiyon chiller termodinamiği.
8. Pearson, A. (2008). "Refrigeration with ammonia." *International Journal of Refrigeration*, 31(4), 545-551. — NH₃ soğutma avantajları.
9. Gullo, P. et al. (2018). "Transcritical R744 refrigeration systems for supermarket applications." *International Journal of Refrigeration*, 93, 269-282. — CO₂ transkritik sistemler.
10. IEA (2018). *The Future of Cooling*. IEA Technology Report. — Küresel soğutma talebi ve verimlilik.
