---
title: "Kurutma Prosesi (Drying Process)"
category: factory
equipment_type: factory
keywords: [kurutma, drying, SEC, SMER, psikrometri, buharlaştırma, exergy, BAT, FDM BREF, Mujumdar]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/heating.md, dryer/benchmarks.md]
use_when: ["Kurutma prosesi exergy analizi yapılacakken", "Kurutucu performansı değerlendirilecekken", "Kurutma BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Kurutma Prosesi (Drying Process)

---

## 1. Proses Tanımı

### Nedir?
Kurutma, bir malzemeden nemi (genellikle suyu) termal enerji kullanarak uzaklaştırma prosesidir. Endüstriyel enerji tüketiminin %10-25'ini temsil eden, exergy açısından en verimsiz proseslerden biridir.

### Nerede Kullanılır?
- Gıda endüstrisi (tahıl, meyve, süt tozu, çay, baharat)
- Kağıt ve selüloz endüstrisi (kağıt kurutma)
- Tekstil (kumaş, iplik kurutma)
- Kimya endüstrisi (pigment, polimer, ilaç)
- Kereste ve ahşap endüstrisi
- Çimento endüstrisi (klinker kurutma)
- Madencilik (mineral kurutma)

### Kurutucu Tipleri

| Tip | Prensip | Tipik Uygulama | η_th Aralığı |
|-----|---------|----------------|-------------|
| Konveksiyonel (sıcak hava) | Sıcak hava sirküle | Tahıl, gıda, kimya | %25-60 |
| Tamburlu (rotary) | Dönen silindir + sıcak hava | Mineral, kum, çamur | %35-65 |
| Sprey (spray dryer) | Sıvı → ince damlacık + sıcak hava | Süt tozu, kahve, seramik | %20-50 |
| Akışkan yataklı (FBD) | Sıcak hava → akışkanlaşma | İlaç, kimya, gıda | %30-60 |
| İletkenli (contact/drum) | Sıcak yüzey teması | Kağıt, kimya | %40-70 |
| Kızılötesi (IR) | Radyasyon | İnce film, kaplama | %20-40 |
| Mikrodalga / RF | Dielektrik ısıtma | İlaç, gıda (niş) | %30-50 |
| Isı pompalı | Nemli hava → ısı pompası | Hassas gıda, kereste | %40-70 |

### Tipik Ölçek
- Küçük: 10 – 100 kg_su/h
- Orta: 100 – 1.000 kg_su/h
- Büyük: 1.000 – 50.000+ kg_su/h

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Suyu sıvı halden buharlaştırmak için minimum exergy:

$$ex_{min} = (h_v - h_0) - T_0 \times (s_v - s_0)$$

Burada:
- h_v: Su buharı entalpisi (100 °C, 1 atm) ≈ 2.676 kJ/kg
- h₀: Sıvı su entalpisi (25 °C) ≈ 104.9 kJ/kg
- s_v: Su buharı entropisi (100 °C, 1 atm) ≈ 7.355 kJ/(kg·K)
- s₀: Sıvı su entropisi (25 °C) ≈ 0.367 kJ/(kg·K)

```
ex_min = (2676 − 104.9) − 298.15 × (7.355 − 0.367)
       = 2571.1 − 2083.1
       = 488 kJ/kg_su
```

> **Ancak**, kurutma havadaki suyu uzaklaştırmaktır. Difüzyon ve bağlı nem için ek exergy gerekir. Pratik minimum:

**Serbest su kurutma (free moisture):**
$$ex_{min,free} ≈ 200 - 500 \text{ kJ/kg\_su}$$

**Bağlı su kurutma (bound moisture):**
$$ex_{min,bound} ≈ 500 - 2000 \text{ kJ/kg\_su (ürüne bağlı)}$$

### 2.2 Nemli Hava Exergy Türetimi (Psychrometric Approach)

Kurutma prosesinde çalışma akışkanı nemli havadır. Nemli havanın exergy'si iki bileşenden oluşur:

**Termal exergy (sıcaklık farkından):**
$$ex_{th} = (c_{pa} + \omega \cdot c_{pv}) \times \left[(T - T_0) - T_0 \ln\left(\frac{T}{T_0}\right)\right]$$

**Kimyasal exergy (nem farkından):**
$$ex_{ch} = R_a T_0 \times \left[(1+\tilde{\omega}) \ln\frac{1+\tilde{\omega}_0}{1+\tilde{\omega}} + \tilde{\omega} \ln\frac{\tilde{\omega}}{\tilde{\omega}_0}\right]$$

Burada:
- ω: Nem oranı (kg su/kg kuru hava)
- ω₀: Çevre nem oranı
- ω̃ = 1.608 × ω (mol oranı dönüşümü)
- c_pa = 1.005 kJ/(kg·K), c_pv = 1.87 kJ/(kg·K)
- R_a = 0.287 kJ/(kg·K)

**Toplam nemli hava exergy'si:**
$$ex_{moist air} = ex_{th} + ex_{ch}$$

**Kurutma prosesi exergy dengesi:**
$$Ex_{giriş hava} = Ex_{çıkış hava} + Ex_{ürün nem değişimi} + Ex_{yıkım}$$

**Minimum kurutma exergy'si:**
Tersinir durumda, egzoz havası çevre koşullarında (T₀, ω₀) çıkar:
$$Ex_{min,kurutma} = Ex_{giriş hava} - Ex_{çıkış hava,tersinir}$$

Pratikte minimum exergy, buharlaştırılacak suyun çevre koşullarında serbest su olarak uzaklaştırılması için gereken minimum iştir:
$$ex_{min,serbest su} ≈ 200 - 500 \text{ kJ/kg su}$$

Bu geniş aralık, giriş havası sıcaklığı, nem oranı ve kurutma sıcaklığına bağlıdır.

> **Kaynak:** Dincer & Rosen (2013), Bölüm 14, s. 380-395 — Kurutma exergy analizi; Mujumdar (2015), Bölüm 1, s. 15-28.

### 2.3 Çözümlü Örnek

**Problem:** 500 kg/h su uzaklaştıran konveksiyonel kurutucu, giriş havası 120 °C, çıkış 70 °C.

```
Serbest su buharlaştırma minimum exergy ≈ 400 kJ/kg_su (tahmini)
Ex_min = 500/3600 × 400 = 55.6 kW

Gerçek enerji tüketimi: SEC = 4.500 kJ/kg_su (tipik konveksiyonel)
Q_actual = 500/3600 × 4500 = 625 kW (termal)
Ex_actual = 625 × 1.04 = 650 kW (doğal gaz exergy)

ESI = 55.6 / 650 = 0.086 → Derece E
```

**Yorum:** Kurutma prosesi ESI = 0.086 ile E derecesinde. Kurutma için bu tipik bir değerdir — proses doğası gereği düşük exergy verimlidir.

**Kaynak:** Mujumdar (2015), Ch. 1; Dincer & Rosen (2013), Ch. 14.

### 2.4 Çözümlü Örnek: İlaç Sprey Kurutma (50 kg/h)

**Problem:** Sprey kurutucu, 50 kg/h su uzaklaştırma. Giriş: 180 °C, çıkış: 85 °C. Doğal gaz. SEC = 7.500 kJ/kg su.

```
ṁ_su = 50 / 3600 = 0.0139 kg/s

Minimum exergy (serbest su yaklaşımı):
  T_ort = (180 + 85)/2 = 132.5 °C → Carnot faktörü ≈ 0.265
  ex_min ≈ 2257 × 0.265 / (SEC/ex_min oranı) ≈ 450 kJ/kg su (tahmini)

  Not: Sprey kurutmada ince damlacıklar → hızlı buharlaşma → difüzyon direnci düşük
  ex_min = 450 kJ/kg su (literatür referansı)

  Ex_min = 0.0139 × 450 = 6.25 kW

Gerçek tüketim:
  Q_actual = 0.0139 × 7500 = 104.2 kW (termal)
  Ex_actual = 104.2 × 1.04 = 108.3 kW

ESI = 6.25 / 108.3 = 0.058 → Derece E
```

**Yorum:**
- ESI = 0.058 (Derece E) — sprey kurutma için tipik (en düşük exergy verimli kurutucu tipi)
- SEC = 7.500 kJ/kg su → buharlaştırma enerjisinin 3.3 katı → ciddi kayıp
- **İyileştirme potansiyeli:**
  - Akışkan yataklı son kurutma (hibrit): SEC → 5.000 kJ/kg, ESI → 0.09
  - Egzoz ısı geri kazanımı: SEC → 6.000 kJ/kg, ESI → 0.075
  - Kapalı devre (ısı pompalı): SEC → 3.000 kJ/kg, ESI → 0.15

**Kaynak:** Mujumdar (2015), Tablo 4.2 — Sprey kurutucu SEC aralıkları.

### 2.5 Çözümlü Örnek: Kağıt Silindir Kurutma (2.000 kg/h)

**Problem:** Kağıt makinesi kurutma bölümü. 2.000 kg/h su uzaklaştırma. Buhar ile dolaylı ısıtma (6 bar doymuş buhar). SEC = 3.200 kJ/kg su.

```
ṁ_su = 2000 / 3600 = 0.556 kg/s

Minimum exergy:
  İletkenli kurutmada ex_min daha düşük (direkt temas):
  ex_min ≈ 350 kJ/kg su (iletkenli kurutma referansı)
  Ex_min = 0.556 × 350 = 194.4 kW

Gerçek tüketim:
  Q_buhar = 0.556 × 3200 = 1778 kW (termal)

  Buhar exergy'si (6 bar doymuş):
  ex_buhar = 746 kJ/kg (tablodan)
  h_fg (6 bar) = 2085 kJ/kg (buharlaşma entalpisi)

  Buhar tüketimi: 1778 / 2085 = 0.853 kg/s
  Ex_actual = 0.853 × 746 = 636.1 kW

ESI = 194.4 / 636.1 = 0.306 → Derece C
```

**Yorum:**
- ESI = 0.306 (Derece C) — kağıt kurutma için iyi
- İletkenli kurutma (silindir), konveksiyonel kurutmadan daha verimli
- **Buhar kullanımı avantajı:** Buhar latent ısısı sabit T'de transfer → daha düşük ΔT → daha az irreversibilite
- **İyileştirme:**
  - Shoe press ile mekanik ön su alma: %10-20 buhar tasarrufu
  - Hood ısı geri kazanımı: %5-12 buhar
  - CHP ile buhar üretimi: fabrika toplam exergy verimi artar

**Kaynak:** PP BREF 2015, Ch. 6 — Kağıt kurutma BAT.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 SEC (Specific Energy Consumption) Aralıkları

| Kurutucu Tipi | SEC Aralığı (kJ/kg_su) | Tipik SEC | Latent Isı Oranı |
|---------------|------------------------|-----------|------------------|
| Konveksiyonel (sıcak hava) | 4.000 – 8.000 | 5.000 | 2.5 – 3.5× |
| Tamburlu (rotary) | 3.500 – 6.000 | 4.500 | 1.5 – 2.5× |
| Sprey (spray) | 4.500 – 9.000 | 6.000 | 2.5 – 4.0× |
| Akışkan yataklı (FBD) | 3.000 – 6.000 | 4.000 | 1.5 – 2.5× |
| İletkenli (contact) | 2.500 – 4.500 | 3.500 | 1.0 – 2.0× |
| Isı pompalı | 1.000 – 2.500 | 1.800 | — |
| Mikrodalga / RF | 2.500 – 5.000 | 3.500 | — |

> **SMER** (Specific Moisture Extraction Rate): SMER = 1/SEC (kg_su/kJ veya kg_su/kWh). Yüksek SMER = daha verimli.

### 3.2 Exergy Verim Aralıkları

| Kurutucu Tipi | η_ex Aralığı | Tipik η_ex | ESI Aralığı |
|---------------|-------------|------------|-------------|
| Konveksiyonel | %5 – %15 | %10 | 0.05 – 0.12 |
| Tamburlu | %8 – %20 | %14 | 0.06 – 0.15 |
| Sprey | %3 – %12 | %8 | 0.03 – 0.10 |
| Akışkan yataklı | %8 – %18 | %12 | 0.06 – 0.14 |
| İletkenli | %12 – %25 | %18 | 0.10 – 0.20 |
| Isı pompalı | %20 – %35 | %25 | 0.15 – 0.25 |

### 3.3 Irreversibilite Kaynakları

1. **Yanma (ısı üretimi):** %35 – %50 — Yakıt → sıcak hava dönüşümü
2. **Isı transferi (hava → ürün):** %15 – %25 — Büyük ΔT
3. **Egzoz havası kaybı:** %15 – %30 — Sıcak, nemli hava atmosfere atılır
4. **Kütle transferi irreversibilitesi:** %5 – %10 — Nem difüzyonu
5. **Ürün aşırı kurutma:** %3 – %8 — Hedefin altına kurutma
6. **Radyasyon ve yüzey kaybı:** %2 – %5 — İzolasyon eksikliği

## 3b. Sektörel Kurutma Profilleri

### 3b.1 İlaç Sektörü

| Uygulama | Kurutucu Tipi | SEC (kJ/kg su) | ESI | Özel Gereksinimler |
|----------|--------------|-----------------|-----|---------------------|
| Tablet granülasyon | Akışkan yataklı | 3.500-5.000 | 0.08-0.14 | GMP, kontamine olmama |
| API kurutma | Vakum tava | 4.000-6.000 | 0.06-0.12 | Çözücü geri kazanımı |
| Sprey kurutma (excipient) | Sprey | 6.000-9.000 | 0.04-0.08 | Dar nem kontrolü |
| Liyofilizasyon (freeze-dry) | Dondurarak kurutma | 10.000-20.000 | 0.02-0.04 | En yüksek kalite, en düşük verim |

**İlaç özelliği:** Kalite gereksinimleri (GMP, partikül boyutu) enerji verimliliğinin önüne geçer. Liyofilizasyon ESI açısından en kötü ama bazı ürünler için zorunlu.

**İlaç sektörü exergy iyileştirme fırsatları:**
- Akışkan yataklı kurutucuda hava resirkülasyonu: %10-15 SEC azaltma (GMP uyumlu filtre ile)
- Vakum tavada kondens ısı geri kazanımı: %5-10 enerji tasarrufu
- Sprey kurutucuda giriş konsantrasyonu artırma (ön evaporasyon): her %5 konsantrasyon artışı ≈ %8-12 SEC azaltma
- Liyofilizasyonda raf sıcaklık profili optimizasyonu: sublimation rate artışı → süre kısalması → %5-15 enerji

> **Regülasyon notu:** İlaç kurutmada her değişiklik validasyon gerektirir (IQ/OQ/PQ). Bu, enerji projelerinin ROI hesabına 6-12 ay ek süre ekler.

### 3b.2 Kağıt Sektörü

| Uygulama | Kurutucu Tipi | SEC (kJ/kg su) | ESI | Not |
|----------|--------------|-----------------|-----|-----|
| Kağıt makinesi (yazı kağıdı) | Silindir + hood | 2.800-3.500 | 0.12-0.18 | Shoe press ile birlikte |
| Karton | Silindir | 3.000-4.000 | 0.10-0.15 | Daha kalın → daha zor |
| Tissue (Yankee) | Yankee silindir + TAD | 3.500-5.500 | 0.08-0.14 | Through-Air Drying enerji yoğun |
| Selüloz kurutma | Flash dryer | 3.000-4.500 | 0.10-0.16 | Yüksek debili |

**Kağıt sektörü exergy iyileştirme fırsatları:**
- Shoe press teknolojisi: mekanik olarak %5-7 daha fazla su çıkarma → %10-20 buhar tasarrufu
- Closed hood sistemi: egzoz nemini artırarak ısı geri kazanım potansiyeli yükselir
- Yanma gazı direkt kullanımı (Yankee hood): buhar kaybını elimine eder
- CHP entegrasyonu: backpressure türbin ile buhar üretimi → elektrik + ısı birlikte

> **Kağıt sektörü notu:** Kağıt makinesi kurutma bölümü, fabrikanın toplam enerji tüketiminin %60-70'ini oluşturur. Shoe press ile mekanik su alma en yüksek ROI yatırımdır.

### 3b.3 Seramik Sektörü

| Uygulama | Kurutucu Tipi | SEC (kJ/kg su) | ESI | Not |
|----------|--------------|-----------------|-----|-----|
| Karo kurutma | Tünel/roller | 2.500-4.000 | 0.10-0.18 | Atık ısı geri kazanımlı |
| Sanitaryware | Oda kurutma | 4.000-6.000 | 0.06-0.10 | Yavaş kurutma gerekli |
| Tuğla kurutma | Tünel | 2.000-3.500 | 0.12-0.20 | Fırın atık ısısı kullanımı |

**Seramik sektörü exergy iyileştirme fırsatları:**
- Fırın soğutma bölgesi atık ısısı → kurutma havasına yönlendirme: %30-50 yakıt tasarrufu
- Roller kurutucu (karo): hızlı geçiş → küçük kurutucu → daha az yüzey kaybı
- Nem profili kontrolü (karo): çatlak önleme + aşırı kurutma engelleme → %5-10 enerji
- Tuğla: tünel kurutucu hava akış yönü optimizasyonu (counter-current) → %10-15 tasarruf

> **Seramik sektörü avantajı:** Fırın atık ısısı (200-400 °C) doğrudan kurutma için kullanılabilir. Bu entegrasyon, kurutma SEC'ini %30-50 azaltır ve ek yakıt maliyeti sıfırdır.

### 3b.4 Gıda Sektörü

| Uygulama | Kurutucu Tipi | SEC (kJ/kg su) | ESI | Not |
|----------|--------------|-----------------|-----|-----|
| Süt tozu | Sprey + akışkan yatak | 4.500-6.500 | 0.05-0.10 | Çok kademeli en iyi pratik |
| Kahve | Sprey / freeze-dry | 5.000-12.000 | 0.03-0.08 | Freeze-dry daha kaliteli |
| Makarna | Konveksiyonel | 3.000-4.500 | 0.08-0.14 | Düşük T, uzun süre |
| Meyve (kurutulmuş) | Konveksiyonel / vakum | 4.000-6.000 | 0.06-0.12 | Renk ve vitamin koruma |

**Gıda sektörü exergy iyileştirme fırsatları:**
- Süt tozu: çok kademeli sprey + akışkan yatak konfigürasyonu en iyi pratik (BAT)
- Kahve: sprey kurutma + aglomerasyon → freeze-dry'a göre %50-60 daha düşük SEC
- Makarna: düşük sıcaklık uzun süre (LT-LT) → yüksek sıcaklık kısa süre (HT-ST) geçişi: %15-25 SEC azaltma, daha iyi pasta kalitesi
- Genel: egzoz havası ısı geri kazanım (economizer) tüm gıda kurutucularında uygulanabilir

> **Gıda sektörü notu:** Gıda kurutmada ürün kalitesi (renk, tat, besin değeri, mikrobiyolojik güvenlik) her zaman enerji verimliliğinin önünde gelir. Ancak modern kontrol sistemleri ile her ikisi birlikte optimize edilebilir.

### 3b.5 Tekstil Sektörü

| Uygulama | Kurutucu Tipi | SEC (kJ/kg su) | ESI | Not |
|----------|--------------|-----------------|-----|-----|
| Kumaş kurutma (tenter frame) | Konveksiyonel | 4.000-6.500 | 0.05-0.10 | Yüksek hava hızı gerekli |
| İplik kurutma | RF / Konveksiyonel | 3.500-5.500 | 0.06-0.12 | RF ile daha hızlı |
| Boya sonrası kurutma | Silindir + hava | 3.000-5.000 | 0.08-0.14 | Buhar kullanımlı |
| Halı kurutma | Konveksiyonel | 4.500-7.000 | 0.04-0.08 | Kalın → yavaş kurutma |

**Tekstil sektörü exergy iyileştirme fırsatları:**
- Mekanik ön su alma (vakum slot, mangle): her %1 nem azaltma ≈ 30-50 kJ/kg kumaş termal tasarruf
- Tenter frame egzoz ısı geri kazanımı: %15-25 doğal gaz tasarrufu
- IR ön kurutma + konveksiyonel son kurutma: hibrit konfigürasyon %10-20 SEC azaltma
- Boya prosesi sıcaklık optimizasyonu: daha düşük boya T → daha az kurutma yükü

### 3b.6 Kereste Sektörü

| Uygulama | Kurutucu Tipi | SEC (kJ/kg su) | ESI | Not |
|----------|--------------|-----------------|-----|-----|
| Yumuşak kereste | Konveksiyonel kabin | 3.500-5.000 | 0.06-0.12 | 50-80 °C, uzun süre |
| Sert kereste | Konveksiyonel kabin | 4.000-6.000 | 0.05-0.10 | Daha yavaş, çatlak riski |
| MDF/Yonga levha | Flash / tamburlu | 3.000-4.500 | 0.08-0.14 | Yüksek debili |
| Vakum kereste kurutma | Vakum | 2.500-4.000 | 0.10-0.18 | Hızlı, kaliteli |

**Kereste sektörü exergy iyileştirme fırsatları:**
- Isı pompalı kereste kurutma: SEC %40-60 azaltma, kuruma süresi %30 kısalma
- Biyokütle yakıtlı kurutucu: kereste atıkları → kurutma enerjisi (sıfır net yakıt maliyeti)
- Solar destekli ön kurutma: güneş kolektörleri ile hava ön ısıtma → %10-30 yakıt tasarrufu
- Kurutma programı optimizasyonu (scheduling): çatlak riski minimize + enerji optimize

---

## 4. BAT Referansı

### 4.1 EU BREF FDM 2019 (Food, Drink and Milk)

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| SEC (sprey kurutma, süt tozu) | 3.500 – 5.500 kJ/kg_su | Çok kademeli, entegre |
| SEC (konveksiyonel, tahıl) | 3.000 – 4.500 kJ/kg_su | Isı geri kazanımlı |
| Egzoz geri kazanım oranı | > %30 | Isı eşanjör veya resirkülasyon |
| Nem kontrol doğruluğu | ±%0.5 | Online nem ölçüm + kontrol |

### 4.2 Genel Kurutma BAT (Mujumdar, 2015)

| Kurutucu Tipi | BAT SEC (kJ/kg_su) | BAT η_ex | Kaynak |
|---------------|---------------------|---------|--------|
| Konveksiyonel + ısı geri kazanım | 3.000 – 3.800 | %15-20 | FDM BREF + Mujumdar |
| Sprey + akışkan yatak hibrit | 3.500 – 4.500 | %12-18 | FDM BREF |
| Isı pompalı kurutucu | 1.200 – 2.000 | %25-35 | Literatür, tahmini |
| Süperkritik CO₂ kurutma | — | %30-40 | Gelişen teknik |
| Mikrodalga destekli | 2.000 – 3.000 | %18-25 | Literatür |

### 4.3 BAT ESI Değerleri

| Uygulama | BAT ESI | Mevcut Ortalama ESI | Boşluk |
|----------|---------|---------------------|--------|
| Gıda kurutma (genel) | 0.12 – 0.18 | 0.05 – 0.10 | %40-80 iyileştirme |
| Kağıt kurutma | 0.15 – 0.22 | 0.08 – 0.14 | %30-60 iyileştirme |
| Tekstil kurutma | 0.10 – 0.16 | 0.04 – 0.08 | %50-100 iyileştirme |
| Kereste kurutma | 0.12 – 0.20 | 0.06 – 0.12 | %40-70 iyileştirme |

## 4b. İleri Kurutma Teknolojileri

### 4b.1 MVR — Mekanik Buhar Sıkıştırma (Mechanical Vapor Recompression)

MVR, kurutma egzozundaki su buharını mekanik olarak sıkıştırarak ısıtma kaynağı olarak yeniden kullanır:

```
Prensip:
  Egzoz: düşük basınçlı su buharı (90-100 °C)
  → Kompresör ile sıkıştırma (ΔP = 0.3-0.5 bar)
  → Yüksek basınç buhar (110-120 °C)
  → Kurutucu ısıtma kaynağı olarak kullanım

Enerji avantajı:
  Konvansiyonel: 1 kg su buharlaştırmak ≈ 2.500-3.000 kJ
  MVR ile: 1 kg su buharlaştırmak ≈ 150-300 kJ (elektrik)
  → %90+ tasarruf (termal → elektrik dönüşüm)
```

| Parametre | Konvansiyonel | MVR |
|-----------|--------------|-----|
| SEC | 3.000-5.000 kJ/kg su | 150-300 kJ_el/kg su |
| Enerji tipi | Termal (yakıt/buhar) | Elektrik |
| Exergy verimi | %5-15 | %25-40 |
| ESI | 0.05-0.12 | 0.20-0.35 |
| Sınırlama | — | T < 100 °C, büyük ölçek |
| Yatırım | Referans | 2-3× |
| ROI | — | 2-4 yıl |

**MVR uygulama koşulları:**
- En uygun: evaporasyon + kurutma hibrit sistemleri (süt, meyve suyu konsantrasyonu)
- Büyük ölçek gerekli: minimum 1.000 kg_su/h (kompresör ekonomisi)
- Düşük sıcaklık farkı (ΔT < 15 °C) en verimli çalışma noktası
- Elektrik/yakıt fiyat oranı kritik: elektrik ucuzsa (PV, rüzgar) ROI hızlanır
- Fouling riski: egzoz buharında partikül varsa kompresör aşınması — ön filtrasyon gerekli

**MVR exergy analizi:**
```
Konvansiyonel kurutma:
  Doğal gaz → brülör → sıcak hava (200 °C) → kurutma → egzoz (80 °C)
  Exergy akışı: 1.04 × Q_termal → %10-15'i faydalı iş
  Exergy yıkım: %85-90

MVR kurutma:
  Elektrik → kompresör → buhar sıkıştırma (ΔT ≈ 10-15 °C) → kurutma
  Exergy akışı: W_el (yüksek kalite) → düşük ΔT ısı transfer
  Exergy yıkım: %60-75

  Kazanım: ΔT küçük → ısı transfer irreversibilitesi düşük
```

### 4b.2 SSD — Kızgın Buhar ile Kurutma (Superheated Steam Drying)

Kızgın buhar (100+ °C, 1 atm) kurutma gazı olarak kullanılır:

```
Prensip:
  Kurutma gazı: hava yerine kızgın buhar (110-180 °C)
  Ürün nemi buharlaşınca → daha fazla buhar (geri kazanılabilir)
  Egzoz: saf su buharı → kolay yoğuştırma ve ısı geri kazanım
```

| Parametre | Sıcak Hava Kurutma | SSD |
|-----------|-------------------|-----|
| SEC | 3.000-6.000 kJ/kg su | 2.000-3.500 kJ/kg su |
| Egzoz geri kazanımı | Zor (nemli hava) | Kolay (saf buhar) |
| Emisyon | VOC olabilir | Kapalı devre |
| Exergy verimi | %5-15 | %15-25 |
| Uygulama | Genel | Kağıt, biyokütle, şeker pancarı |

**SSD avantajları ve sınırlamaları:**
- **Avantajlar:**
  - Egzoz saf su buharı → yoğuştırma ile kolay ısı geri kazanım
  - Kapalı devre → VOC emisyonu yok, çevresel avantaj
  - İnversion sıcaklığı üzerinde kurutma hızı havadan yüksek (tipik > 160 °C)
  - Ürün sterilizasyonu eş zamanlı → gıda güvenliği

- **Sınırlamalar:**
  - Başlangıç (inversion point altında) kurutma hızı düşük
  - Ürün kızgın buhara dayanıklı olmalı (bazı gıdalar uygun değil)
  - Sistem sızdırmazlığı kritik — hava girişi verim düşürür
  - Yatırım maliyeti konvansiyonele göre 1.5-2.5× yüksek

**SSD exergy avantajı:**
```
Sıcak hava kurutma: Hava ısıtma (yanma) + kütle transferi + egzoz kaybı
  → 3 ayrı irreversibilite kaynağı

SSD: Buhar ısıtma (daha düşük ΔT) + kütle transferi + egzoz geri kazanım
  → Egzoz kaybı neredeyse sıfır (yoğuştırma ile geri kazanım)
  → Net tasarruf: %20-40 exergy
```

### 4b.3 Isı Pompalı Kurutma (Heat Pump Drying)

| Parametre | Konveksiyonel | Isı Pompalı |
|-----------|--------------|-------------|
| SEC | 3.000-6.000 kJ/kg su | 800-2.000 kJ_el/kg su |
| Kurutma T | 60-200 °C | 30-70 °C |
| Ürün kalitesi | Orta | Yüksek (düşük T) |
| ESI | 0.05-0.12 | 0.15-0.35 |
| En iyi uygulama | Genel | Hassas gıda, kereste, ilaç |

**Isı pompalı kurutma prensip detayı:**
```
Çalışma döngüsü:
  1. Nemli egzoz havası → evaporatör (soğutma + nem yoğuşması)
  2. Soğutulan hava → düşük nem, düşük T
  3. Kompresör → soğutucu akışkan sıkıştırma
  4. Kondenser → hava ısıtma (kurutma havasına geri dönüş)
  5. Kuru, sıcak hava → kurutucuya geri besleme

Exergy avantajı:
  COP_HP = 3-5 → 1 kW elektrik ile 3-5 kW ısı
  Eşdeğer SEC = 3000/COP = 600-1000 kJ_el/kg su
  Exergy bazında: W_el direkt exergy → verimli kullanım
```

**Isı pompalı kurutma uygulama kriterleri:**
- Kurutma sıcaklığı < 70 °C (yüksek COP bölgesi)
- Düşük hava debisi uygulamaları (kapalı devre avantajı)
- Nem hassas ürünler (ilaç, hassas gıda, kereste)
- Elektrik maliyeti düşük bölgeler (yenilenebilir enerji entegrasyonu)
- Çevre regülasyonları sıkı bölgeler (kapalı devre → sıfır emisyon)

### 4b.4 Hibrit Kurutma Sistemleri

Tek teknoloji yerine birden fazla kurutma prensibini birleştiren sistemler daha yüksek exergy verimi sağlar:

| Hibrit Konfigürasyon | SEC (kJ/kg su) | ESI | Uygulama |
|----------------------|-----------------|-----|----------|
| Sprey + akışkan yatak | 3.500-5.000 | 0.08-0.14 | Süt tozu, deterjan |
| IR ön kurutma + konveksiyonel | 2.500-4.000 | 0.10-0.16 | Kaplama, tekstil |
| Mekanik pres + termal kurutma | 2.000-3.500 | 0.12-0.20 | Kağıt, çamur |
| Mikrodalga + vakum | 2.000-3.500 | 0.12-0.18 | İlaç, gıda (niş) |
| Solar ön ısıtma + konveksiyonel | 2.500-4.500 | 0.08-0.16 | Kereste, tarım ürünü |

**Hibrit sistemlerin exergy avantajı:**
Her kurutma aşaması için en uygun enerji kaynağını kullanma prensibi:
- **Yüksek nem aşaması:** Mekanik (düşük exergy tüketimi) veya düşük kalite ısı
- **Orta nem aşaması:** Konveksiyonel veya iletkenli (orta kalite ısı)
- **Düşük nem aşaması:** Mikrodalga/RF (hacimsel ısıtma, difüzyon sınırlı bölgede etkili)

Bu yaklaşım, Tsatsaronis'in "exergy eşleştirme" (exergy matching) prensibine uygundur: enerji kaynağı kalitesi, proses gereksinimi ile eşleştirilir.

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Yanma / ısı üretimi | 35 – 50 | Düşük-orta (CHP, ısı pompası geçişi) |
| 2 | Egzoz havası kaybı | 15 – 30 | Çok yüksek (geri kazanım, resirkülasyon) |
| 3 | Isı transferi ΔT | 15 – 25 | Orta (daha düşük T, daha uzun süre) |
| 4 | Kütle transferi | 5 – 10 | Düşük (proses doğası) |
| 5 | Aşırı kurutma | 3 – 8 | Yüksek (online nem kontrol) |
| 6 | Yüzey/izolasyon kaybı | 2 – 5 | Yüksek (izolasyon) |

### 5.1 Exergy Yıkım Dağılımı — Kurutucu Tipine Göre

| Kaynak | Konveksiyonel | Sprey | İletkenli | Isı Pompalı |
|--------|--------------|-------|-----------|-------------|
| Yanma / ısı üretimi | %45 | %40 | %35 | %10 (kompresör) |
| Egzoz kaybı | %25 | %30 | %15 | %5 (kapalı devre) |
| Isı transferi ΔT | %15 | %15 | %25 | %35 (evaporatör+kondenser) |
| Kütle transferi | %8 | %8 | %10 | %15 |
| Aşırı kurutma | %5 | %5 | %10 | %25 |
| Yüzey kaybı | %2 | %2 | %5 | %10 |

> **Yorum:** Isı pompalı kurutucuda yanma ve egzoz kaybı neredeyse sıfır, ancak ısı transfer irreversibilitesi artar (evaporatör ve kondenser ΔT). Toplam exergy yıkımı yine de %40-60 daha düşüktür.

### 5.2 Exergy Yıkım Azaltma Önceliklendirme

```
Öncelik sırası (en yüksek ROI):
  1. Egzoz ısı geri kazanımı → en kolay, en hızlı ROI
  2. Online nem kontrol → aşırı kurutma engelle, düşük yatırım
  3. İzolasyon iyileştirme → basit, hızlı uygulama
  4. Mekanik ön su alma → termal yükü azalt
  5. Isı kaynağı değişimi → CHP, ısı pompası (yüksek yatırım, yüksek kazanç)
```

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Egzoz havası ısı geri kazanımı** | %15-30 enerji | 1-3 yıl | Hava-hava eşanjör veya kısmi resirkülasyon; en büyük etki |
| 2 | **Isı pompalı kurutucu** | %40-65 enerji | 3-5 yıl | SEC < 2.000 kJ/kg_su; düşük T uygulamalar için ideal |
| 3 | **Çok kademeli kurutma** | %15-25 enerji | 2-4 yıl | Ön kurutma (mekanik) + son kurutma (termal) |
| 4 | **Online nem kontrol** | %5-15 enerji | 1-2 yıl | Aşırı kurutmayı önle; ürün kalitesi de artar |
| 5 | **Mekanik ön nem alma** | %20-40 termal yük | 1-3 yıl | Pres, santrifüj — mekanik enerji ile nem azaltma |
| 6 | **Egzoz havası resirkülasyonu** | %10-20 enerji | 1-2 yıl | Kısmi resirkülasyon — nem kapasitesi izin verdiği kadar |
| 7 | **İzolasyon iyileştirme** | %2-8 enerji | 0.5-1.5 yıl | Özellikle eski kurutucularda yüzey kaybı yüksek |
| 8 | **VFD (değişken hızlı sürücü) fan** | %10-20 fan enerjisi | 1-2 yıl | Kısmi yükte fan hızını düşür |
| 9 | **CHP entegrasyonu** | %15-30 birincil enerji | 4-7 yıl | Buhar + elektrik birlikte üretim |
| 10 | **Solar hava ön ısıtma** | %5-15 yakıt | 3-6 yıl | Güneşli bölgelerde etkili, mevsimsel değişken |

### 6.1 Strateji Seçim Karar Ağacı

```
BAŞLA
│
├─ Mevcut kurutucu yaşı > 15 yıl?
│   ├─ EVET → Komple yenileme değerlendir (ısı pompalı / MVR / SSD)
│   └─ HAYIR → Retrofit öncelikleri:
│       │
│       ├─ Egzoz T > 80 °C?
│       │   ├─ EVET → Isı geri kazanım (öncelik 1)
│       │   └─ HAYIR → Resirkülasyon veya nem kontrol
│       │
│       ├─ Aşırı kurutma var mı (ürün nem < hedef - %1)?
│       │   ├─ EVET → Online nem kontrol (öncelik 2)
│       │   └─ HAYIR → Diğer fırsatlar
│       │
│       ├─ T_kurutma < 80 °C?
│       │   ├─ EVET → Isı pompası retrofit değerlendir
│       │   └─ HAYIR → MVR veya SSD değerlendir
│       │
│       └─ Mekanik ön su alma mümkün mü?
│           ├─ EVET → Pres/santrifüj ekle
│           └─ HAYIR → Mevcut sistemi optimize et
```

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER kurutma prosesi (genel):
  → ESI > 0.15 "Kurutma için çok iyi — ısı pompalı veya entegre sistem"
  → ESI 0.08-0.15 "Kurutma için iyi — BAT yakınında"
  → ESI 0.04-0.08 "Kurutma için orta — tipik konveksiyonel"
  → ESI < 0.04 "Kurutma için zayıf — acil iyileştirme gerekli"
```

> **Önemli:** Kurutma ESI'si doğası gereği çok düşüktür (%3-25). ESI A-F skalasında genellikle E-F aralığında kalır. Bu normal! Proses bazlı değerlendirme kullan.

### 7.2 SEC Bazlı Hızlı Değerlendirme

| SEC (kJ/kg_su) | Değerlendirme |
|-----------------|---------------|
| < 3.000 | Mükemmel — ısı pompalı veya ileri sistem |
| 3.000 – 4.500 | İyi — BAT seviyesinde |
| 4.500 – 6.000 | Orta — iyileştirme fırsatları var |
| 6.000 – 8.000 | Zayıf — ısı geri kazanım eksik |
| > 8.000 | Kritik — kapsamlı dönüşüm gerekli |

### 7.3 Özel Durumlar

```
EĞER egzoz sıcaklığı > 100 °C:
  → "Yüksek egzoz sıcaklığı — ısı geri kazanım potansiyeli yüksek"
  → "Her 20 °C düşüş ≈ %5-8 enerji tasarrufu"

EĞER SEC > 2.5 × latent ısı (2.257 kJ/kg):
  → "SEC, buharlaştırma enerjisinin 2.5 katından fazla"
  → "Ciddi termal verimsizlik — egzoz, izolasyon, kontrol incele"

EĞER ısı pompası uygulanabilir (T < 80 °C):
  → "Isı pompalı kurutma ile SEC %40-65 azaltılabilir"
  → "Ürün kalitesi de genellikle artar (düşük T)"
```

### 7.4 Kurutucu Tipine Özel IF/THEN Kuralları

```
EĞER sprey kurutucu:
  → SEC > 6.000 kJ/kg su: "Yüksek — çok kademeli ve egzoz geri kazanım değerlendir"
  → "Akışkan yataklı son kurutma ile hibrit konfigürasyon %20-30 SEC azaltır"
  → "Giriş katı konsantrasyonunu artır (ön evaporasyon) → daha az su buharlaştır"

EĞER konveksiyonel (sıcak hava):
  → SEC > 4.500 kJ/kg su: "Egzoz ısı geri kazanım öncelikli"
  → "Her 20 °C egzoz sıcaklığı düşüşü ≈ %5-8 enerji tasarrufu"
  → T_kurutma < 80 °C: "Isı pompalı kurutma alternatifi değerlendir"

EĞER silindir/iletkenli kurutucu:
  → "Buhar basıncını minimize et — her 0.5 bar düşüş ≈ %2 tasarruf"
  → "Kondens geri dönüşü optimize et"
  → "Mekanik ön su alma (pres) ile termal yükü azalt"

EĞER akışkan yataklı:
  → "Hava dağıtım düzgünlüğü kontrol et — dead zone = exergy yıkım"
  → "Kısmi yükte fan hızını düşür (VFD) → %10-20 fan enerjisi tasarrufu"
  → "Çok kademeli (ön kurutma + son kurutma) konfigürasyon düşün"

EĞER vakum kurutucu:
  → "Vakum pompası enerji tüketimini dahil et"
  → "Düşük T avantajı: ürün kalitesi + daha iyi exergy eşleştirme"
  → "MVR entegrasyonu ile SEC dramatik düşer"

EĞER liyofilizasyon (freeze-drying):
  → "En yüksek SEC, en düşük ESI — ama kalite gereksinimi"
  → "ESI < 0.05 normal — bu proseste ESI değerlendirmesi daha az anlamlı"
  → "Vakum sistemini optimize et, sublimation rate kontrol et"
```

---

## İlgili Dosyalar

- `dryer/benchmarks.md` — Kurutucu ekipman benchmark
- `factory/process/heating.md` — Isıtma prosesi (kurutucu ısı kaynağı)
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi
- `factory/heat_integration.md` — Isı entegrasyonu (egzoz → proses)
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanım

## Referanslar

1. European Commission, JRC (2019). *BAT Reference Document for the Food, Drink and Milk Industries (FDM BREF)*. Ch. 5 — Drying operations.
2. Mujumdar, A.S. (2015). *Handbook of Industrial Drying*. 4th ed., CRC Press. — SEC tabloları ve kurutucu seçimi.
3. Kemp, I.C. (2012). "Fundamentals of energy analysis of dryers." In *Modern Drying Technology*, Wiley.
4. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Kurutma exergy analizi (Ch. 14).
5. Aghbashlo, M. et al. (2013). "A review of exergy analysis of drying processes." *Drying Technology*, 31(10), 1156-1170.
6. Mujumdar, A.S. (2015). *Handbook of Industrial Drying*. 4th ed., CRC Press. Bölüm 4 (Sprey), Bölüm 16 (Isı pompası), Bölüm 20 (SSD), Tablo 1.2 (SEC).
7. Kemp, I.C. (2012). "Fundamentals of energy analysis of dryers." In *Modern Drying Technology*, Vol. 4, Wiley. — Exergy analizi metodolojisi.
8. Chua, K.J. et al. (2002). "Intermittent drying of bioproducts — an overview." *Bioresource Technology*, 85(2), 219-230. — Kesikli kurutma exergy avantajı.
9. Aghbashlo, M. et al. (2013). "A review of exergy analysis of drying processes." *Drying Technology*, 31(10), 1156-1170. — Kurutma exergy analizi kapsamlı derleme.
10. Brammer, J.G. & Bridgwater, A.V. (1999). "Drying technologies for an integrated gasification bio-energy plant." *Renewable and Sustainable Energy Reviews*, 3(4), 243-289. — SSD teknolojisi.
