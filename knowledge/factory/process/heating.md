---
title: "Isıtma Prosesi (Heating Process)"
category: factory
equipment_type: factory
keywords: [ısıtma, heating, kazan, brülör, exergy verimi, yanma, BAT, LCP BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/steam_generation.md, factory/process/chp.md, boiler/benchmarks.md]
use_when: ["Isıtma prosesi exergy analizi yapılacakken", "Kazan/brülör performansı değerlendirilecekken", "Isıtma BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Isıtma Prosesi (Heating Process)

---

## 1. Proses Tanımı

### Nedir?
Isıtma prosesi, bir enerji kaynağından (yakıt, elektrik, buhar) alınan enerjiyi bir akışkana (su, hava, yağ, proses akışkanı) veya malzemeye ısı olarak aktarma işlemidir.

### Nerede Kullanılır?
- Proses ısıtma (gıda, kimya, tekstil, kağıt)
- Bina ısıtma (endüstriyel tesisler)
- Ön ısıtma (beslenme suyu, yanma havası)
- Isıl işlem (metal, seramik)

### İlgili Ekipmanlar
- Kazanlar (ateş tüplü, su borulu)
- Brülörler (gaz, sıvı yakıt)
- Elektrik ısıtıcılar (dirençli, indüksiyon)
- Isı eşanjörleri (geri kazanım için)
- Termik yağ sistemleri

### Tipik Ölçek
- Küçük: 50 – 500 kW termal
- Orta: 500 kW – 5 MW termal
- Büyük: 5 – 50+ MW termal

### Isıtma Sınıflandırması (Sıcaklık Bandına Göre)

| Sınıf | Sıcaklık Aralığı | Tipik Uygulama | Ana Enerji Kaynağı |
|-------|-------------------|----------------|---------------------|
| Çok düşük sıcaklık | 30 – 60 °C | Bina HVAC, sıcak su | Isı pompası, güneş |
| Düşük sıcaklık | 60 – 120 °C | Gıda prosesi, CIP, pastörizasyon | Isı pompası + kazan |
| Orta sıcaklık | 120 – 250 °C | Kimyasal reaktör, distilasyon, kağıt kurutma | Buhar, termik yağ |
| Yüksek sıcaklık | 250 – 600 °C | Çimento klinker ön ısıtma, cam tavlama | Doğal gaz fırını |
| Çok yüksek sıcaklık | 600 – 1500 °C | Metal ergitme, seramik pişirme, ısıl işlem | Gaz/elektrik fırını |

> **Exergy İlkesi:** Sıcaklık bandı yükseldikçe Carnot faktörü artar ve ısıtma prosesinin exergy değeri yükselir. Düşük sıcaklık ısıtmada exergy kalitesi çok düşüktür — bu nedenle yüksek exergy'li yakıt kullanmak termodinamik olarak israftır.

### Isıtma Medyumları (Heat Transfer Fluids)

| Medyum | Kullanılabilir Aralık | Avantaj | Dezavantaj |
|--------|----------------------|---------|------------|
| Su (sıcak su) | 30 – 100 °C | Ucuz, güvenli, yüksek c_p | Buharlaşma sınırı |
| Basınçlı sıcak su | 100 – 200 °C | Buhardan daha homojen | Basınçlı sistem gerekli |
| Buhar (doymuş) | 100 – 250 °C | Yüksek latent ısı, hızlı transfer | Yoğuşma suyu dönüşü gerekli |
| Termik yağ | 150 – 400 °C | Basınçsız, geniş aralık | Düşük c_p, pompalama maliyeti |
| Kızgın hava | 100 – 800 °C | Basit, doğrudan temas | Düşük ısı transfer katsayısı |
| Radyasyon (doğrudan) | 500 – 1500+ °C | En yüksek T mümkün | Homojenlik problemi |

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Isı transferi ile yapılan ısıtma prosesi için minimum exergy gereksinimi:

$$Ex_{min} = Q \times \left(1 - \frac{T_0}{T_h}\right)$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| Q | Aktarılan ısı miktarı | kW |
| T₀ | Çevre (ölü hal) sıcaklığı | K |
| T_h | Isıtılan akışkanın ortalama sıcaklığı | K |

### 2.2 Varsayımlar
- Kararlı hal (steady-state) koşulları
- Sabit T_h (ortalama logaritmik sıcaklık kullanılabilir)
- T₀ = 298.15 K (25 °C) referans sıcaklığı
- Minimum exergy, Carnot faktörüne dayalıdır

### 2.2b Carnot Türetimi — Isıtma Exergy'sinin 2. Yasa Temeli

Termodinamiğin 2. yasası, ısı transfer prosesinin tersinirlik sınırını belirler. T₀ sıcaklığındaki çevreden T_h sıcaklığındaki bir proses akışkanına Q kadar ısı aktarmak için gereken minimum iş:

**Adım 1:** Carnot ısı pompası modeli
Tersinir bir Carnot ısı pompası, T₀'dan T_h'ye ısı transfer eder:
$$COP_{Carnot,HP} = \frac{Q_h}{W_{min}} = \frac{T_h}{T_h - T_0}$$

**Adım 2:** Minimum iş (exergy)
$$W_{min} = \frac{Q_h}{COP_{Carnot,HP}} = Q_h \times \frac{T_h - T_0}{T_h} = Q_h \times \left(1 - \frac{T_0}{T_h}\right)$$

**Adım 3:** Bu, ısının exergy'sidir (Carnot faktörü)
$$Ex_{ısı} = Q \times \left(1 - \frac{T_0}{T_h}\right) = Q \times \theta_C$$

Burada θ_C = (1 − T₀/T_h) **Carnot faktörü** olarak adlandırılır.

**Fiziksel anlam:** Carnot faktörü, ısının "iş yapabilme potansiyelini" ölçer. Yüksek sıcaklıklarda Carnot faktörü 1'e yaklaşır (ısı neredeyse tamamen işe dönüşebilir). Düşük sıcaklıklarda (T_h → T₀) Carnot faktörü 0'a yaklaşır — düşük sıcaklık ısısının exergy değeri çok düşüktür.

> **Kritik tasarım çıkarımı:** 60 °C sıcak su üretmek için doğal gaz yakmak (θ_C = 0.105) büyük exergy yıkımıdır. Yakıtın exergy'si ~1.0 iken, ürünün exergy'si sadece ~0.1. Bu nedenle düşük sıcaklık ısıtmada **ısı pompası** termodinamik olarak çok daha uygundur.

**Kaynak:** Kotas (1985), Bölüm 2, s. 18-25; Dincer & Rosen (2013), Bölüm 3, s. 55-68.

### 2.3 Sıcaklığa Bağlı Carnot Faktörü

| T_h (°C) | T_h (K) | Carnot Faktörü (1−T₀/T_h) | Ex_min / Q |
|-----------|---------|---------------------------|------------|
| 60 | 333 | 0.105 | %10.5 |
| 100 | 373 | 0.201 | %20.1 |
| 150 | 423 | 0.295 | %29.5 |
| 200 | 473 | 0.370 | %37.0 |
| 400 | 673 | 0.557 | %55.7 |
| 800 | 1073 | 0.722 | %72.2 |
| 1200 | 1473 | 0.798 | %79.8 |

> **Kritik Bilgi:** Düşük sıcaklık ısıtma (60-100 °C) termodinamik olarak çok az exergy gerektirir. Bu proseslerde yüksek kaliteli yakıt (doğal gaz, exergy/enerji ≈ 1.04) kullanmak büyük exergy yıkımına yol açar.

### 2.4 Çözümlü Örnek

**Problem:** 2.000 kW termal kapasiteli, 180 °C'de proses ısıtma yapan bir sistem.

```
T_h = 180 + 273.15 = 453.15 K
T₀ = 298.15 K

Ex_min = 2000 × (1 − 298.15/453.15)
       = 2000 × (1 − 0.658)
       = 2000 × 0.342
       = 684 kW

(Termodinamik olarak bu ısıtma işi 684 kW exergy ile yapılabilir)
```

**Kaynak:** Kotas (1985), Bölüm 2; Dincer & Rosen (2013), Bölüm 3.

### 2.5 Çözümlü Örnek: Düşük Sıcaklık Gıda Isıtma

**Problem:** 500 kW termal kapasiteli, 60 °C'de proses suyu üreten doğal gaz kazanı (gıda sektörü). Kazan verimi η_en = %90 (LHV).

```
T_h = 60 + 273.15 = 333.15 K
T₀ = 298.15 K
Q = 500 kW

Ex_min = 500 × (1 − 298.15/333.15)
       = 500 × (1 − 0.895)
       = 500 × 0.105
       = 52.5 kW

Q_yakıt = Q / η_en = 500 / 0.90 = 555.6 kW (LHV)
Ex_actual = 555.6 × 1.04 = 577.8 kW (doğal gaz exergy)

ESI = 52.5 / 577.8 = 0.091 → Derece E
η_ex = 52.5 / 577.8 = %9.1
```

**Yorum:**
- ESI = 0.091 → Derece E. Çok düşük görünse de düşük sıcaklık ısıtma için bu normaldir.
- Kazan enerji verimi %90 ile iyi, AMA exergy verimi sadece %9.1.
- **Neden?** Doğal gaz yakarak (~1900 °C alev) 60 °C su üretmek devasa bir termodinamik uyumsuzluktur.
- **Isı pompası alternatifi:** COP = 4.0 ile:
  ```
  W_HP = 500 / 4.0 = 125 kW (elektrik = exergy)
  ESI_HP = 52.5 / 125 = 0.42 → Derece B
  ```
  Isı pompası ile ESI **4.6 kat** artar!

**Kaynak:** Dincer & Rosen (2013), Bölüm 7 — Isı pompası exergy analizi.

### 2.6 Çözümlü Örnek: Yüksek Sıcaklık Metal Isıl İşlem

**Problem:** 3.000 kW kapasiteli, 850 °C'de metal ısıl işlem fırını. Doğal gaz, η_en = %75 (LHV).

```
T_h = 850 + 273.15 = 1123.15 K
T₀ = 298.15 K
Q = 3000 kW

Ex_min = 3000 × (1 − 298.15/1123.15)
       = 3000 × (1 − 0.265)
       = 3000 × 0.735
       = 2204 kW

Q_yakıt = 3000 / 0.75 = 4000 kW (LHV)
Ex_actual = 4000 × 1.04 = 4160 kW

ESI = 2204 / 4160 = 0.530 → Derece A
η_ex = 2204 / 4160 = %53.0
```

**Yorum:**
- ESI = 0.530 → Derece A! Yüksek sıcaklık ısıtmada exergy verimi doğal olarak yüksektir.
- Carnot faktörü = 0.735 → ısının %73.5'i exergy'dir.
- **Kazan enerji verimi %75 ile iyi değil**, ama yüksek T'de bile exergy verimi %53 çıkıyor.
- **İyileştirme:** Rejeneratif brülör ile hava ön ısıtma → η_en = %85-90, η_ex = %60-65 mümkün.
- **Not:** Bu sıcaklıkta ısı pompası uygulanabilir DEĞİLDİR — yakma tek pratik seçenektir.

**Kaynak:** Kotas (1985), Bölüm 5, s. 120-135 — Endüstriyel fırın exergy analizi.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 SEC (Specific Exergy Consumption) Aralıkları

| Alt-kategori | SEC Aralığı | Birim | Not |
|-------------|-------------|-------|-----|
| Doğal gaz kazanı (yoğuşmalı) | 1.05 – 1.15 | kW_ex / kW_th | η_energy %95-105 (LHV) |
| Doğal gaz kazanı (konvansiyonel) | 1.10 – 1.30 | kW_ex / kW_th | η_energy %82-94 |
| Kömür kazanı | 1.20 – 1.60 | kW_ex / kW_th | η_energy %70-88 |
| Fuel oil kazanı | 1.15 – 1.40 | kW_ex / kW_th | η_energy %80-90 |
| Elektrikli ısıtıcı | 1.00 – 1.05 | kW_ex / kW_th | η_energy ~%98-100 |

### 3.2 Exergy Verim Aralıkları

| Alt-kategori | η_ex Aralığı | Tipik η_ex | Not |
|-------------|-------------|------------|-----|
| Düşük sıcaklık ısıtma (60-100 °C) | %5 – %15 | %10 | Carnot faktörü çok düşük |
| Orta sıcaklık ısıtma (100-250 °C) | %15 – %35 | %25 | Tipik proses ısıtma |
| Yüksek sıcaklık ısıtma (250-600 °C) | %25 – %50 | %35 | Isıl işlem, kurutma |
| Çok yüksek sıcaklık (600+ °C) | %30 – %55 | %40 | Fırınlar, refrakter |

### 3.3 Irreversibilite Kaynakları ve Payları

1. **Yanma irreversibilitesi:** %50 – %65 (baskın kaynak)
2. **Isı transferi ΔT:** %15 – %25 (baca gazı – proses akışkanı)
3. **Baca gazı kayıpları:** %8 – %15 (sıcak egzoz gazları)
4. **Yüzey kayıpları:** %3 – %8 (izolasyon yetersizliği)
5. **Kısmi yük kaybı:** %2 – %5 (değişken yüklerde)

## 3b. Sektörel Varyasyonlar

### 3b.1 Gıda Sektörü (T_h: 40-100 °C)

| Uygulama | T_h (°C) | Carnot Faktörü | Tipik η_ex | Tercih Edilen Teknoloji |
|----------|----------|----------------|------------|------------------------|
| CIP (clean-in-place) yıkama | 70-85 | 0.12-0.17 | %8-14 | Isı pompası + kazan hibrit |
| Pastörizasyon | 72-85 | 0.13-0.17 | %10-15 | Isı geri kazanımlı PHE + kazan |
| Pişirme | 80-100 | 0.17-0.20 | %12-18 | Buhar ile dolaylı ısıtma |
| Kurutma | 60-120 | 0.11-0.22 | %5-15 | Sıcak hava (bkz. drying.md) |

**Gıda sektörü özelliği:** Düşük sıcaklık baskın → exergy verimi yapısal olarak düşük. Isı pompası potansiyeli çok yüksek.

### 3b.2 Kimya Sektörü (T_h: 100-400 °C)

| Uygulama | T_h (°C) | Carnot Faktörü | Tipik η_ex | Tercih Edilen Teknoloji |
|----------|----------|----------------|------------|------------------------|
| Reaktör ısıtma | 150-300 | 0.30-0.48 | %20-35 | Termik yağ + doğal gaz |
| Distilasyon | 100-250 | 0.20-0.41 | %15-30 | Buhar ile dolaylı |
| Evaporasyon | 80-120 | 0.17-0.22 | %12-18 | Çok kademeli + MVR |
| Polimerizasyon | 150-350 | 0.30-0.53 | %22-38 | Elektrik + buhar |

**Kimya sektörü özelliği:** Geniş sıcaklık aralığı. Pinch analizi ile ısı entegrasyonu büyük tasarruf sağlar.

### 3b.3 Metal Sektörü (T_h: 500-1500 °C)

| Uygulama | T_h (°C) | Carnot Faktörü | Tipik η_ex | Tercih Edilen Teknoloji |
|----------|----------|----------------|------------|------------------------|
| Isıl işlem | 800-950 | 0.72-0.76 | %40-55 | Doğal gaz fırını |
| Dövme/haddeleme ön ısıtma | 1000-1250 | 0.77-0.82 | %45-60 | Rejeneratif fırın |
| Eritme (demir dışı) | 650-1100 | 0.65-0.78 | %35-55 | İndüksiyon / gaz fırını |
| Sertleştirme + temperleme | 500-900 | 0.60-0.73 | %35-50 | Atmosfer kontrollü fırın |

**Metal sektörü özelliği:** Yüksek sıcaklık → Carnot faktörü yüksek → exergy verimi yapısal olarak daha iyi. Rejeneratif brülörler ile %15-25 ek iyileştirme.

### 3b.4 Tekstil Sektörü (T_h: 80-180 °C)

| Uygulama | T_h (°C) | Carnot Faktörü | Tipik η_ex | Tercih Edilen Teknoloji |
|----------|----------|----------------|------------|------------------------|
| Boyama (dyeing) | 80-130 | 0.17-0.25 | %12-20 | Buhar + ısı geri kazanımlı PHE |
| Kurutma/ramöz | 120-180 | 0.22-0.32 | %10-22 | Doğal gaz direkt ısıtma |
| Yıkama | 60-90 | 0.11-0.18 | %8-14 | Isı pompası + kazan hibrit |
| Apreleme (finishing) | 100-160 | 0.20-0.29 | %15-22 | Buhar ile dolaylı |

**Tekstil sektörü özelliği:** Yoğun su kullanımı, atık sıcak su geri kazanımı yüksek potansiyel taşır. Boya banyosu atık suyu 60-80 °C → ısı pompası kaynağı olarak kullanılabilir.

### 3b.5 Sektörler Arası Ölçek Karşılaştırması

| Sektör | Tipik Termal Kapasite | T_h Aralığı | Tipik ESI | Best-in-Class ESI |
|--------|----------------------|-------------|-----------|-------------------|
| Gıda | 100 – 2.000 kW | 40-120 °C | 0.06-0.15 | 0.30-0.50 (HP) |
| Kimya | 500 – 20.000 kW | 100-400 °C | 0.15-0.30 | 0.35-0.45 |
| Metal | 1.000 – 50.000 kW | 500-1500 °C | 0.35-0.55 | 0.55-0.65 |
| Tekstil | 200 – 5.000 kW | 80-180 °C | 0.10-0.25 | 0.30-0.40 |
| Seramik | 500 – 10.000 kW | 800-1400 °C | 0.30-0.50 | 0.50-0.60 |

---

## 4. BAT Referansı

### 4.1 EU BREF LCP 2017 (Large Combustion Plants)

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Kazan enerji verimi (doğal gaz) | %92 – %96 (LHV) | Yeni tesis |
| Kazan enerji verimi (kömür) | %86 – %92 (LHV) | Yeni tesis |
| Baca gazı sıcaklığı | 80 – 160 °C | Yakıt tipine bağlı |
| Hava fazlası oranı | %3 – %6 O₂ | Doğal gaz |

### 4.2 EU BREF ENE 2009 (Energy Efficiency)

| Parametre | BAT Değeri | Not |
|-----------|-----------|-----|
| Isı geri kazanım oranı | > %70 | Atık ısı → proses |
| İzolasyon yüzey sıcaklığı | < 40 °C | Dış yüzey |
| Ekonomizer uygulaması | Zorunlu (50+ °C düşüş) | Baca gazı geri kazanım |

### 4.3 BAT Exergy Verimi (ExergyLab Hesabı)

| Isıtma Tipi | BAT η_energy | BAT η_ex | Kaynak |
|-------------|-------------|---------|--------|
| Düşük sıcaklık (80 °C) | %96 | %12-15 | LCP BREF 2017 + exergy dönüşüm |
| Orta sıcaklık (200 °C) | %94 | %30-35 | LCP BREF 2017 + exergy dönüşüm |
| Yüksek sıcaklık (500 °C) | %90 | %40-50 | LCP BREF 2017 + exergy dönüşüm |

### 4.4 Alt-kategoriler

| Alt-kategori | BAT SEC (enerji) | BAT η_ex | Not |
|-------------|------------------|---------|-----|
| Yoğuşmalı kazan (doğal gaz) | 1.04 kW_fuel/kW_th | %30-38 | En iyi ticari teknoloji |
| Modüler kazan sistemi | 1.06 kW_fuel/kW_th | %28-36 | Kısmi yük avantajı |
| Atık ısı geri kazanım + kazan | 0.85 kW_fuel/kW_th | %35-45 | Entegre sistem |
| Isı pompası destekli | 0.30 kW_el/kW_th | %40-60 | T < 80 °C için en iyi |

### 4.5 Teknoloji Detayları

#### 4.5.1 Yoğuşmalı Kazan (Condensing Boiler)

Yoğuşmalı kazanlar, baca gazındaki su buharının latent ısısını geri kazanarak enerji verimini LHV bazında %100'ün üzerine çıkarabilir:

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| Teori | η > %100 (LHV) | HHV bazında hala < %100 |
| Koşul | Dönüş suyu < 55 °C | Çiğ noktası altında yoğuşma |
| Tipik verim | %95-107 (LHV) | %87-95 (HHV) |
| Exergy etkisi | +%3-8 η_ex artışı | Latent ısı düşük exergy, ama kayıp azalır |
| Yatırım | 1.5-2x konvansiyonel | Paslanmaz çelik eşanjör gerekli |
| Baca gazı T | 40-60 °C | Korozyon riski → uygun malzeme |

**Exergy perspektifi:** Yoğuşmalı kazan enerji verimini çok artırır ama exergy verimini sınırlı artırır çünkü geri kazanılan latent ısının exergy'si çok düşüktür (T ≈ 50 °C → θ_C ≈ 0.08).

#### 4.5.2 Isı Pompası Entegrasyonu

Düşük sıcaklık ısıtma uygulamalarında ısı pompası, exergy verimini dramatik artırır:

| COP | T_h (°C) | ESI Artışı | Karşılaştırma (kazan η=%90) |
|-----|----------|------------|----------------------------|
| 3.0 | 60 | 0.035 → 0.105 (3x) | Kazan ESI = 0.035 |
| 4.0 | 60 | 0.035 → 0.140 (4x) | %300 ESI artışı |
| 5.0 | 50 | 0.026 → 0.132 (5x) | Düşük T'de daha etkili |
| 3.5 | 80 | 0.058 → 0.202 (3.5x) | 80 °C'de bile avantajlı |

**Engine değeri karşılaştırması:** bat_references.py → heating/water_low: exergy_efficiency_pct = 45%, technology = "Yoğuşmalı kazan + ısı geri kazanımı + ısı pompası". Literatür aralığı: %35-60 (ısı pompası dahil).

> **AI Kuralı:** T_ısıtma < 80 °C olan HER ısıtma uygulamasında ısı pompası alternatifini değerlendir ve exergy avantajını sayısal olarak göster.

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | Açıklama |
|------|--------|---------|----------|
| 1 | Yanma | 50 – 65 | Kimyasal exergy → termal exergy dönüşümü |
| 2 | Isı transferi ΔT | 15 – 25 | Alev/baca gazı → proses akışkanı sıcaklık farkı |
| 3 | Baca gazı çıkışı | 8 – 15 | Sıcak gaz atmosfere atılıyor |
| 4 | Yüzey kayıpları | 3 – 8 | Yetersiz izolasyon, sıcak noktalar |
| 5 | Yakıt hazırlama | 1 – 3 | Atomizasyon, karışım |

> **Not:** Yanma irreversibilitesi termodinamik olarak kaçınılmazdır (UN); ancak hava ön ısıtma, oksijen zenginleştirme ve kademeli yakma ile kısmen azaltılabilir.

### 5b. Exergy Yıkım Pareto Analizi

Kümülatif Pareto eğrisi — tipik 2.000 kW doğal gaz kazanı (η_en = %88, T_h = 180 °C):

| Sıra | Kaynak | Yıkım (kW) | Pay | Kümülatif | İyileştirilebilir? |
|------|--------|-----------|-----|-----------|---------------------|
| 1 | Yanma irreversibilitesi | 680 | %52 | %52 | Kısmen (hava ön ısıtma: −80 kW) |
| 2 | Isı transferi ΔT | 250 | %19 | %71 | Kısmen (CHP: çıkarılabilir) |
| 3 | Baca gazı kaybı | 160 | %12 | %83 | Evet (ekonomizer: −120 kW) |
| 4 | Yüzey kayıpları | 85 | %7 | %90 | Evet (izolasyon: −60 kW) |
| 5 | Kısmi yük | 65 | %5 | %95 | Evet (modüler kazan: −45 kW) |
| 6 | Diğer | 60 | %5 | %100 | Kısmen |
| **Toplam** | | **1300 kW** | **%100** | | **~305 kW kapatılabilir** |

> **Yorum:** İlk iki kaynak (yanma + ısı transferi = %71) büyük ölçüde **unavoidable (UN)** dir — termodinamik sınır. Ekonomizer ve izolasyon (%19) ise **avoidable (AV)** ve düşük maliyetli. Toplam 305 kW kapatılabilir boşluk ≈ %23 tasarruf.

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Ekonomizer (baca gazı geri kazanım)** | %5-12 yakıt | 1-2 yıl | Baca gazı → beslenme suyu ön ısıtma; her 20 °C düşüş ≈ %1 verim artışı |
| 2 | **Hava ön ısıtıcı** | %3-8 yakıt | 2-3 yıl | Baca gazı → yanma havası; özellikle kömür ve fuel oil kazanlarında etkili |
| 3 | **Yoğuşmalı kazan dönüşümü** | %10-15 yakıt | 3-5 yıl | Doğal gaz kazanlarında su buharı latent ısısını geri kazanır |
| 4 | **Isı pompası entegrasyonu** | %40-60 exergy | 3-5 yıl | T < 80 °C ısıtmada; COP 3-5 ile exergy verimi dramatik artar |
| 5 | **Modüler kazan sistemi** | %5-10 yakıt | 2-4 yıl | Kısmi yüklerde birden fazla küçük kazan → daha yüksek verimlilik |
| 6 | **Oksijen zenginleştirme (oxygen enrichment)** | %5-15 yakıt | 3-6 yıl | Yanma havasına O₂ ekleme → alev T artışı, baca gazı hacmi azalır |
| 7 | **Rejeneratif brülör** | %15-25 yakıt | 3-5 yıl | T > 600 °C fırınlarda; hava ön ısıtma ile yanma verimi artışı |
| 8 | **Isı geri kazanım ağı (HEN) entegrasyonu** | %10-30 toplam | 2-5 yıl | Pinch analizi ile sıcak/soğuk akış eşleştirme |
| 9 | **Kademeli yakma (staged combustion)** | %3-8 yakıt | 2-4 yıl | NOx azaltma + yanma homojenliği artışı |
| 10 | **Otomatik yanma kontrolü (O₂ trim)** | %2-5 yakıt | 0.5-1.5 yıl | Sürekli O₂ ölçümü ile hava fazlası optimizasyonu |

### 6.2 Strateji Seçim Matrisi (Sıcaklık Bandına Göre)

| Strateji | T < 80 °C | 80-200 °C | 200-600 °C | > 600 °C |
|----------|-----------|-----------|------------|----------|
| Isı pompası | +++ | ++ | - | - |
| Yoğuşmalı kazan | +++ | ++ | - | - |
| Ekonomizer | + | +++ | +++ | ++ |
| Hava ön ısıtıcı | - | ++ | +++ | +++ |
| Rejeneratif brülör | - | - | ++ | +++ |
| Modüler kazan | ++ | +++ | ++ | + |
| O₂ trim kontrolü | ++ | +++ | +++ | +++ |
| Pinch entegrasyonu | ++ | +++ | +++ | ++ |

(+++ = birincil strateji, ++ = etkili, + = marjinal, - = uygulanabilir değil)

### 6.3 Yatırım Önceliklendirme

**Kural:** Düşük maliyetli operasyonel iyileştirmeler her zaman önce uygulanır, ardından sermaye yoğun yatırımlar:

```
Öncelik 1 (Operasyonel — 0 yatırım):
  → Hava fazlası ayarı (O₂ trim)
  → Kısmi yük yönetimi
  → Izolasyon tamiri

Öncelik 2 (Düşük yatırım — ROI < 2 yıl):
  → Ekonomizer
  → Otomatik yanma kontrolü
  → Kondenstop bakımı

Öncelik 3 (Orta yatırım — ROI 2-5 yıl):
  → Yoğuşmalı kazan dönüşümü
  → Isı pompası (T < 80 °C)
  → Modüler kazan sistemi

Öncelik 4 (Stratejik yatırım — ROI > 5 yıl):
  → CHP sistemi (bkz. chp.md)
  → Tam HEN yeniden tasarımı
  → Rejeneratif fırın dönüşümü
```

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER ısıtma sıcaklığı < 100 °C:
  → "Düşük sıcaklık ısıtma prosesi — exergy verimi doğası gereği düşüktür"
  → "Isı pompası alternatifini mutlaka değerlendir"
  → ESI > 0.10 ise "Düşük sıcaklık ısıtma için iyi"

EĞER ısıtma sıcaklığı 100-250 °C:
  → ESI < 0.20 ise "Orta sıcaklık ısıtma için düşük, iyileştirme gerekli"
  → ESI > 0.30 ise "Orta sıcaklık ısıtma için iyi"

EĞER ısıtma sıcaklığı > 250 °C:
  → ESI < 0.30 ise "Yüksek sıcaklık ısıtma için düşük"
  → ESI > 0.40 ise "Yüksek sıcaklık ısıtma için çok iyi"
```

### 7.2 Anahtar Karşılaştırma Noktaları

- Aynı sıcaklık seviyesi için **ısı pompası vs kazan** exergy karşılaştırması yap
- **Baca gazı sıcaklığı > 200 °C** → ekonomizer veya ön ısıtıcı eksik
- **Hava fazlası > %8 O₂** → yanma kontrolü yetersiz
- **Yüzey sıcaklığı > 60 °C** → izolasyon yetersiz

### 7.3 Benchmark Referansları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| Kazan exergy verimi | > %35 | %25-35 | < %25 |
| Baca gazı sıcaklığı | < 120 °C | 120-200 °C | > 200 °C |
| Hava fazlası (O₂) | < %4 | %4-7 | > %7 |
| Yüzey kaybı | < %2 | %2-5 | > %5 |

### 7.4 Sıcaklık-Teknoloji Eşleştirme Kuralları

```
EĞER T_h < 60 °C:
  → "Isı pompası tek başına yeterli — kazan kullanımı exergy israfıdır"
  → Öner: Hava kaynaklı veya su kaynaklı ısı pompası (COP 4-6)

EĞER 60 °C < T_h < 80 °C:
  → "Isı pompası birincil, kazan yedek (hibrit sistem)"
  → Öner: Isı pompası + peak yük için yoğuşmalı kazan

EĞER 80 °C < T_h < 120 °C:
  → "Yüksek sıcaklık ısı pompası + buhar kazanı hibrit değerlendir"
  → Öner: CO₂ (R744) veya su (R718) soğutucu akışkanlı HP

EĞER 120 °C < T_h < 250 °C:
  → "Buhar bazlı ısıtma en yaygın — ekonomizer ve hava ön ısıtıcı kontrol et"
  → Öner: Yoğuşmalı kazan + ekonomizer + hava ön ısıtıcı

EĞER T_h > 250 °C:
  → "Doğrudan yakma kaçınılmaz — rejeneratif brülör ve izolasyon odaklı iyileştir"
  → Öner: Rejeneratif brülör, O₂ kontrolü, yüzey izolasyonu
```

### 7.5 Cross-Equipment Sinerjiler

Isıtma prosesi, fabrikanın diğer ekipmanlarıyla güçlü sinerjiler oluşturur:

| Kaynak Ekipman | Atık Isı T (°C) | Hedef Isıtma Uygulaması | Potansiyel Tasarruf |
|----------------|-----------------|------------------------|---------------------|
| Kompresör (aftercooler) | 60-90 | Düşük T proses suyu, bina ısıtma | %30-60 kompresör atık ısısı |
| Chiller (condenser) | 30-45 | Ön ısıtma, defrost | %15-25 chiller atık ısısı |
| Fırın baca gazı | 200-500 | Beslenme suyu, yanma havası | %10-20 yakıt tasarrufu |
| Motor/jeneratör | 80-120 | CIP, proses suyu | %25-40 motor atık ısısı |
| Buhar türbini çıkış | 100-180 | Orta T proses ısıtma | CHP sinerjisi |

> **AI Kuralı:** Fabrika analizi sırasında, her ısıtma prosesi için önce mevcut atık ısı kaynaklarını kontrol et. Sıcaklık seviyesi uygun bir atık ısı varsa, doğrudan kullanım veya ısı pompası ile yükseltme öner.

### 7.6 Yaygın Hatalar ve Uyarılar

| Hata | Açıklama | Doğru Yaklaşım |
|------|----------|----------------|
| η_en ile η_ex karıştırma | Kazan η=%92 → "verimli" deme | η_ex hesapla, T'ye göre değerlendir |
| LHV vs HHV karışıklığı | Yoğuşmalı kazan η>100% (LHV) | HHV bazında her zaman < %100 |
| Düşük T'de düşük ESI → "kötü" | ESI=0.08 → "çok kötü" deme | Düşük T'de ESI doğal olarak düşüktür |
| Isı pompası her yerde | T>120 °C'de HP önerme | HP sıcaklık sınırını belirt |
| Yanma kaybını "sıfırlayabilirsiniz" | Yanma irreversibilitesi UN | AV/UN ayrımını yap |

### 7.7 Gap Analysis Entegrasyonu

Isıtma prosesi gap analysis sonuçlarını yorumlarken:

```
ESI Derece A (> 0.50):
  → Yüksek T ısıtma olmalı → "Exergy eşleşmesi iyi"
  → İyileştirme: İnce ayar (O₂ trim, izolasyon)

ESI Derece B (0.35-0.50):
  → Orta-yüksek T ısıtma → "İyi performans, marjinal iyileştirme mümkün"
  → İyileştirme: Ekonomizer, hava ön ısıtıcı

ESI Derece C (0.20-0.35):
  → Orta T ısıtma → "Tipik performans"
  → İyileştirme: Isı geri kazanım, pinch analizi

ESI Derece D (0.10-0.20):
  → Düşük-orta T ısıtma → "Isı pompası alternatifini değerlendir"
  → İyileştirme: HP hibrit, yoğuşmalı kazan

ESI Derece E (0.05-0.10):
  → Düşük T ısıtma → "Doğal gaz ile düşük T ısıtma = exergy israfı"
  → İyileştirme: Isı pompası geçişi zorunlu

ESI Derece F (< 0.05):
  → Çok düşük T veya çok verimsiz sistem → "Acil müdahale gerekli"
  → İyileştirme: Sistem yeniden tasarımı
```

---

## İlgili Dosyalar

- `factory/process/steam_generation.md` — Buhar üretim prosesi (ısıtmanın özel hali)
- `factory/process/chp.md` — CHP/kojenerasyon (ısı + elektrik birlikte)
- `factory/process/drying.md` — Kurutma prosesi (ısıtma alt-türü)
- `factory/process/cooling.md` — Soğutma prosesi (ters yön analiz)
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri
- `factory/process/sustainability_index.md` — ESI hesaplama ve derecelendirme
- `boiler/benchmarks.md` — Kazan ekipman seviyesi benchmark
- `boiler/solutions/economizer.md` — Ekonomizer detayları
- `heat_exchanger/benchmarks.md` — Isı eşanjörü benchmark
- `factory/heat_integration.md` — Isı entegrasyonu fırsatları
- `factory/pinch/fundamentals.md` — Pinch analizi temelleri
- `factory/advanced_exergy/overview.md` — AV/UN dekompozisyon

## Referanslar

1. European Commission, JRC (2017). *BAT Reference Document for Large Combustion Plants (LCP BREF)*. BAT Conclusions — Boiler Efficiency.
2. European Commission, JRC (2009). *Reference Document on Best Available Techniques for Energy Efficiency (ENE BREF)*.
3. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Isıtma exergy analizi.
4. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*. 2nd ed., Elsevier.
5. Rant, Z. (1956). "Exergie, ein neues Wort für technische Arbeitsfähigkeit." *Forschung auf dem Gebiet des Ingenieurwesens*, 22(1), 36-37.
6. Bejan, A. (2006). *Advanced Engineering Thermodynamics*. 3rd ed., Wiley. — Yanma exergy analizi, Bölüm 10.
7. IEA Heat Pump Centre (2020). *Industrial Heat Pumps*. IEA HPT Annex 48 — Endüstriyel ısı pompası uygulama alanları.
8. ASHRAE (2023). *ASHRAE Handbook — HVAC Applications*. Ch. 50 — Industrial heating.
9. Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions." *Energy Conversion and Management*, 43(9-12), 1259-1270.
