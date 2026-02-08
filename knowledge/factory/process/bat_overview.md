---
title: "En İyi Mevcut Teknikler — BAT Genel Bakış (Best Available Techniques Overview)"
category: factory
equipment_type: factory
keywords: [BAT, BREF, en iyi mevcut teknik, EU direktifi, endüstriyel emisyon, referans doküman, IED]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/index.md, factory/factory_benchmarks.md]
use_when: ["BAT kavramı açıklanacakken", "EU BREF referans dokümanları sorgulanacakken", "BAT-AEL değerleri referans alınacakken"]
priority: high
last_updated: 2026-02-08
---

# En İyi Mevcut Teknikler — BAT Genel Bakış (Best Available Techniques Overview)

Bu dosya, Avrupa Birliği'nin Endüstriyel Emisyon Direktifi (IED 2010/75/EU) kapsamındaki **BAT (Best Available Techniques)** kavramını, BREF doküman sistemini ve ExergyLab'ın proses boşluk analizinde BAT'ı nasıl kullandığını açıklar.

---

## 1. BAT Nedir? (What are Best Available Techniques?)

### 1.1 Tanım

BAT, IED Direktifi Madde 3(10) uyarınca şu üç koşulu sağlayan tekniklerdir:

| Terim | Anlamı |
|-------|--------|
| **Best** (En İyi) | Çevresel performansı en yüksek düzeyde sağlayan |
| **Available** (Mevcut) | Ekonomik ve teknik olarak uygulanabilir, endüstriyel ölçekte kanıtlanmış |
| **Techniques** (Teknikler) | Hem kullanılan teknoloji hem de tesisin tasarım, bakım ve işletme biçimi |

### 1.2 BAT-AEL ve BAT-AEPL

- **BAT-AEL** (BAT-Associated Emission Levels): BAT uygulandığında beklenen emisyon seviyeleri
- **BAT-AEPL** (BAT-Associated Environmental Performance Levels): BAT uygulandığında beklenen çevresel performans — enerji verimliliği, kaynak kullanımı dahil

> **ExergyLab bağlamı:** BAT-AEPL'deki enerji verimliliği değerleri, exergy referans noktası olarak kullanılır. Enerji verimi → exergy verimine dönüştürülür.

### 1.3 BAT vs Konvansiyonel Teknik Karşılaştırması

Aşağıdaki tablo, tipik endüstriyel proseslerde konvansiyonel teknik ile BAT arasındaki performans farkını gösterir:

| Proses | Parametre | Konvansiyonel | BAT | İyileşme |
|--------|-----------|---------------|-----|----------|
| Isıtma (kazan) | Verimlilik (LHV) | %85 | %94 | +9 puan |
| Buhar üretimi | Blöf kaybı | %5-8 | %1-3 | ~%60 azalma |
| Basınçlı hava | SEC (kWh/m³) | 0.12 | 0.08 | %33 azalma |
| Soğutma | COP | 3.5-4.5 | 5.5-6.5 | %40-50 artış |
| Kurutma | SMER (kg/kWh) | 0.5-1.0 | 1.5-3.0 | 2-3x artış |
| CHP | FUF (Fuel Utilization Factor) | %65-70 | %80-90 | +15-20 puan |
| Soğuk depolama | kWh/m³/yıl | 40-60 | 20-30 | %50 azalma |

> **Kritik fark:** Enerji verimliliğindeki %10'luk iyileşme, exergy verimliliğinde %15-25'lik iyileşmeye karşılık gelebilir. Bunun nedeni, düşük kaliteli kayıpların exergy açısından daha fazla ağırlık taşımasıdır.

### 1.4 BAT Hiyerarşisi

BAT değerlendirmesinde teknikler şu hiyerarşiyle uygulanır:

```
1. Önleme (Prevention) — Kayıpları kaynağında önle
   Örnek: İyi yalıtım, sızıntı önleme, uygun boyutlandırma

2. Geri Kazanım (Recovery) — Atık enerjiyi/exergy'yi geri kazan
   Örnek: Ekonomizer, kondens geri dönüşü, atık ısı kazanı

3. Optimizasyon (Optimization) — Mevcut sistemi optimize et
   Örnek: VSD sürücü, otomatik kontrol, yük yönetimi

4. İkame (Substitution) — Daha verimli teknoloji ile değiştir
   Örnek: Eski kazan → kondensli kazan, PRV → buhar türbini
```

---

## 2. BREF Doküman Sistemi

### 2.1 BREF Nedir?

**BREF** (BAT Reference Documents) Avrupa Komisyonu'nun Sevilla sürecinde (EIPPCB — European IPPC Bureau) hazırladığı referans dokümanlardır. Her BREF:

- İlgili sektör/faaliyetin teknik tanımını içerir
- Mevcut tekniklerin çevresel performansını karşılaştırır
- BAT sonuçlarını (BAT Conclusions) belirler
- Gelişen teknikleri (Emerging Techniques) listeler

### 2.2 ExergyLab İçin İlgili BREF Dokümanları

| # | BREF Dokümanı | Yıl | İlgili Prosesler | ExergyLab Dosyası |
|---|---------------|-----|-------------------|--------------------|
| 1 | **Energy Efficiency (ENE)** | 2009 | Tüm prosesler (genel) | Tüm proses dosyaları |
| 2 | **Large Combustion Plants (LCP)** | 2017 | Isıtma, buhar üretimi, CHP | `heating.md`, `steam_generation.md`, `chp.md` |
| 3 | **Industrial Cooling Systems (ICS)** | 2001 | Soğutma, soğuk depolama | `cooling.md`, `cold_storage.md` |
| 4 | **Food, Drink and Milk (FDM)** | 2019 | Kurutma, ısıtma (gıda sektörü) | `drying.md` |
| 5 | **Cement, Lime and Magnesium Oxide (CLM)** | 2013 | Çimento üretimi | `general_manufacturing.md` |
| 6 | **Manufacture of Glass (GLS)** | 2012 | Cam üretimi | `general_manufacturing.md` |
| 7 | **Production of Pulp, Paper and Board (PP)** | 2015 | Kağıt üretimi | `general_manufacturing.md` |

### 2.3 BREF Doküman Yapısı (Tipik)

Standart bir BREF dokümanı şu bölümlerden oluşur:

1. **Genel Bilgiler** — Sektör tanımı, üretim hacimleri
2. **Uygulandığı Teknikler** — Mevcut teknolojiler ve performansları
3. **Emisyon ve Tüketim Verileri** — Gerçek tesis verileri
4. **BAT Sonuçları** — BAT-AEL ve BAT-AEPL değerleri
5. **Gelişen Teknikler** — Henüz BAT olmayan umut vadeden teknolojiler

### 2.4 BREF Sayfa ve Bölüm Referansları (ExergyLab İçin İlgili)

Aşağıdaki tablo, her BREF dokümanının ExergyLab proses dosyalarıyla eşleşen spesifik bölüm ve sayfa referanslarını verir. Bu referanslar, BAT değerlerinin kaynağını doğrulamak ve detaylı teknik bilgiye erişmek için kullanılır.

| BREF | İlgili Bölüm/Sayfa | İçerik | ExergyLab Kullanımı |
|------|---------------------|--------|---------------------|
| ENE 2009 | Ch. 3.1-3.3, pp. 45-89 | Enerji verimliliği genel teknikleri: motor sistemleri, ısı geri kazanım, buhar, basınçlı hava | Tüm proses BAT referansı |
| ENE 2009 | Ch. 3.7, pp. 112-128 | Basınçlı hava sistemleri BAT | `compressed_air.md` BAT değerleri |
| ENE 2009 | Ch. 3.4, pp. 90-98 | Buhar ve kondens sistemleri | `steam_generation.md` dağıtım kayıpları |
| LCP 2017 | Ch. 3 (BAT Conclusions), pp. 48-72 | Kazan BAT-AEL: verimlilik, emisyon, baca gazı | `heating.md`, `steam_generation.md` temel BAT değerleri |
| LCP 2017 | Ch. 7, pp. 310-345 | CHP/kojenerasyon BAT: FUF, elektrik verimi | `chp.md` BAT değerleri |
| LCP 2017 | Ch. 10.2, pp. 420-438 | Atık ısı geri kazanım teknikleri | Tüm proses iyileştirme stratejileri |
| ICS 2001 | Ch. 3.1-3.4, pp. 55-120 | Soğutma kulesi, chiller tipleri, BAT COP | `cooling.md` BAT referansı |
| ICS 2001 | Ch. 4, pp. 121-155 | Doğal soğutucu akışkanlar, NH₃, CO₂ | `cold_storage.md` soğutucu seçimi |
| FDM 2019 | Ch. 5.2, pp. 285-320 | Kurutma operasyonları BAT | `drying.md` gıda kurutma BAT |
| FDM 2019 | Ch. 5.5, pp. 350-380 | Soğutma ve dondurma BAT | `cold_storage.md` gıda depolama |
| CLM 2013 | Ch. 1.2-1.4, pp. 18-85 | Klinker üretimi, döner fırın, ön kalsinatör | `general_manufacturing.md` çimento |
| CLM 2013 | BAT Conclusions, pp. 86-115 | BAT-AEL: termal enerji 3000-3400 MJ/ton, elektrik 90-110 kWh/ton | Çimento ESI hesaplama |
| GLS 2012 | Ch. 3, pp. 95-165 | Cam eritme fırınları, rejeneratif, oxy-fuel | `general_manufacturing.md` cam |
| GLS 2012 | BAT 8-12, pp. 180-210 | Eritme enerjisi BAT: 5000-6500 MJ/ton (float) | Cam ESI hesaplama |
| PP 2015 | Ch. 6, pp. 380-450 | Kağıt üretimi BAT: buhar, kurutma, CHP | `general_manufacturing.md` kağıt |
| PP 2015 | BAT 28-35, pp. 460-490 | Toplam enerji BAT: 10-20 GJ/ton kağıt | Kağıt ESI hesaplama |

> **Kullanım notu:** Sayfa numaraları BREF'in resmi PDF versiyonuna aittir. Online HTML versiyonlarında bölüm numaralandırması değişebilir.

---

## 3. BAT Değerlerinin Exergy'ye Dönüşümü

### 3.1 Dönüşüm Prensibi

BREF dokümanları genellikle **enerji verimliliği** (1. yasa verimi) cinsinden değer verir. ExergyLab bunları **exergy verimliliğine** dönüştürür:

```
η_energy (BREF) → η_exergy (ExergyLab)
```

### 3.2 Dönüşüm Faktörleri (Yakıt Bazlı)

Yakıtın exergy/enerji oranı (φ = Ex_fuel / LHV):

| Yakıt | φ (Exergy/LHV) | Kaynak |
|-------|----------------|--------|
| Doğal gaz | 1.04 | Kotas (1985) |
| Kömür (bitümlü) | 1.06 | Kotas (1985) |
| Fuel oil | 1.04 | Szargut et al. (1988) |
| Biyokütle | 1.05 – 1.15 | Ptasinski et al. (2007) |
| Elektrik | 1.00 | Tanım gereği |

### 3.3 Ürün Exergy Hesabı

Proses ürününün exergy'si, ürüne bağlıdır:

| Ürün | Exergy Hesabı | Not |
|------|---------------|-----|
| Sıcak su/buhar | ex = (h − h₀) − T₀(s − s₀) | CoolProp ile hesaplanır |
| Basınçlı hava | ex = RT₀ ln(P₂/P₁) | İzotermik minimum |
| Soğutma | ex = Q × (T₀/T_cold − 1) | Ters Carnot |
| Kurutma | ex = m_w × [(h_v − h₀) − T₀(s_v − s₀)] | Buharlaşma exergy'si |
| Mekanik iş | ex = W | Doğrudan eşdeğer |

### 3.4 BAT Exergy Verimi Hesabı

```
η_ex_BAT = (Ex_product) / (Ex_fuel_BAT)

Burada:
  Ex_fuel_BAT = Q_product / η_energy_BAT × φ
```

### 3.5 Çözümlü Örnek: Soğutma BAT Dönüşümü

**Problem:** EU BREF ICS 2001'de belirtilen endüstriyel soğutma BAT COP = 6.0
(7 °C soğuk su, 35 °C kondenser). Bu değerin exergy karşılığı nedir?

**Çözüm:**

```
Adım 1: Ters Carnot minimum exergy
  COP_Carnot = T_cold / (T₀ − T_cold) = 280.15 / (308.15 − 280.15) = 10.0
  Ex_min / Q_cold = 1/COP_Carnot = 0.10 (yani %10)

Adım 2: BAT gerçek COP ile karşılaştırma
  COP_BAT = 6.0
  W_BAT / Q_cold = 1/COP_BAT = 0.167

Adım 3: BAT exergy verimi (soğutma prosesi)
  η_ex_BAT = Ex_min / W_BAT = (Q × 0.10) / (Q × 0.167) = 0.60 (%60)

Adım 4: ESI_BAT
  ESI_BAT = Ex_min / Ex_actual_BAT = 0.60
```

**Yorum:** COP = 6.0 olan BAT chiller, ESI = 0.60 ile A derecesinde çalışır.
Gerçek tesislerde COP = 4.0-5.0 arasında olduğunda ESI 0.40-0.50 arasına düşer.

**Engine değeri karşılaştırması:** `engine/bat_references.py`'de cooling/process
exergy_efficiency_pct = 35%, cooling/comfort = 42%. Literatür aralığı: %35-60.

### 3.6 Çözümlü Örnek: Isıtma (Kazan) BAT Dönüşümü

**Problem:** LCP BREF 2017'ye göre doğal gaz kazanı BAT enerji verimi η_en = %94 (LHV).
Proses suyu 80 °C → 120 °C ısıtılıyor (T₀ = 25 °C). BAT exergy verimi nedir?

**Çözüm:**

```
Adım 1: Ortalama proses sıcaklığı
  T_m = (80 + 120) / 2 = 100 °C = 373.15 K

Adım 2: Carnot faktörü (ürün exergy/enerji oranı)
  τ = 1 − T₀/T_m = 1 − 298.15/373.15 = 0.201

Adım 3: Yakıt exergy/enerji oranı (doğal gaz)
  φ = 1.04

Adım 4: BAT exergy verimi
  η_ex_BAT = (τ × η_en_BAT) / φ
           = (0.201 × 0.94) / 1.04
           = 0.189 / 1.04
           = 0.182 (%18.2)

Adım 5: ESI_BAT
  ESI_BAT = η_ex_BAT = 0.182
```

**Yorum:** Enerji verimi %94 olan BAT kazan, exergy verimi sadece %18.2'dir. Bu dramatik
fark, kazanın yüksek sıcaklıktaki yanma exergy'sini düşük sıcaklıktaki ısıya dönüştürmesinden
kaynaklanır. Exergy analizi, proses sıcaklığını artırmanın veya CHP'ye geçmenin asıl
iyileştirme fırsatları olduğunu gösterir.

---

## 4. BAT Değerlerinin Güvenilirlik Seviyeleri

ExergyLab'da kullanılan BAT referans değerleri farklı güvenilirlik seviyelerine sahiptir:

| Seviye | Kaynak | Güvenilirlik | İşaretleme |
|--------|--------|-------------|------------|
| **A — Kesin** | EU BAT Conclusions (resmi) | Çok yüksek | Doğrudan kullan |
| **B — Güvenilir** | BREF doküman gövdesi | Yüksek | Kullan, kaynak belirt |
| **C — Tahmini** | Akademik kaynak, DOE | Orta | "Literatür değeri" notu |
| **D — Yaklaşık** | Mühendislik tahmini | Düşük | "Tahmini değer, doğrulama gerekli" |

> **AI Kuralı:** BAT değeri güvenilirlik seviyesi C veya D ise, yorumda bunu açıkça belirt.

---

## 5. BAT Güncelleme Süreci

BREF dokümanları periyodik olarak güncellenir. Güncel BREF durumu:

| BREF | Mevcut Versiyon | Sonraki Güncelleme | Durum |
|------|----------------|--------------------|-------|
| ENE (Enerji Verimliliği) | 2009 | Revizyonu değerlendiriliyor | Aktif |
| LCP (Büyük Yakma) | 2017 | ~2027 | Aktif |
| ICS (Endüstriyel Soğutma) | 2001 | Revizyon gündemde | Eski, dikkatli kullan |
| FDM (Gıda) | 2019 | ~2029 | Güncel |
| CLM (Çimento) | 2013 | Revizyon başladı | Aktif |
| GLS (Cam) | 2012 | Revizyon başladı | Aktif |
| PP (Kağıt) | 2015 | ~2025 | Güncellenmek üzere |

> **Not:** ICS BREF 2001 yılına ait olup güncelliğini yitirmiş olabilir. Modern chiller COP değerleri bu dokümandaki değerleri aşabilir.

---

## 5b. IED İzin Süreci ve BAT Uygulaması (IED Permit Process)

### 5b.1 IED Direktifi Temel Maddeleri

Endüstriyel Emisyon Direktifi (2010/75/EU), AB'deki büyük endüstriyel tesisler için çevresel izin çerçevesini belirler:

| Madde | Konu | ExergyLab Bağlamı |
|-------|------|-------------------|
| **Madde 3(10)** | BAT tanımı — "en iyi mevcut teknikler" | BAT referans değerlerinin yasal dayanağı |
| **Madde 14** | İzin koşulları — BAT Conclusions'a dayalı emisyon limitleri | Tesislerin BAT-AEL'e uyum yükümlülüğü |
| **Madde 15** | Emisyon limit değerleri — BAT-AEL aralığında belirlenmeli | Ulusal makamlar BAT-AEL aralığından seçim yapar |
| **Madde 21** | İzin güncelleme — Yeni BAT Conclusions yayınlandığında 4 yıl içinde uyum | BAT değerleri periyodik güncellenir |
| **Madde 24** | Kamuoyu katılımı — İzin sürecinde paydaş görüşleri | Şeffaflık ve hesap verebilirlik |

### 5b.2 Sevilla Süreci (BAT Conclusions Oluşturma)

BAT Conclusions'un oluşturulma süreci:

```
1. EIPPCB (European IPPC Bureau, Sevilla) koordine eder
2. TWG (Technical Working Group) oluşturulur:
   - Üye devlet temsilcileri
   - Endüstri temsilcileri
   - Çevre STK'ları
   - Avrupa Komisyonu
3. Veri toplama: Tesis anketleri, ölçüm verileri
4. BREF taslağı hazırlanır
5. BAT Conclusions taslağı — teknik tartışma
6. IED Madde 75 Forumu oylaması
7. Avrupa Komisyonu onayı → Resmi Gazete yayını
8. 4 yıl uyum süresi başlar
```

### 5b.3 BAT Derogation (İstisna) Mekanizması

IED Madde 15(4) uyarınca, bir tesis BAT-AEL'den daha gevşek emisyon limitleri talep edebilir:

| Koşul | Açıklama |
|-------|----------|
| Orantısız maliyet | BAT uygulaması çevresel faydaya kıyasla aşırı maliyetli |
| Coğrafi konum | Çevresel etki düşük (ör. uzak bölge) |
| Teknik özellik | Tesisin teknik yapısı BAT'ı engelliyor |
| Geçici süre | Derogation süreli ve koşullu olmalı |

> **ExergyLab notu:** BAT derogation, ESI hesaplamasını etkilemez. ExergyLab her zaman BAT Conclusions'daki standart değerleri referans alır.

### 5b.4 Sektörel BAT Uygulama Örnekleri

**Büyük Yakma Tesisleri (LCP BREF 2017):**
- Kapsam: > 50 MW_th yakma tesisleri
- BAT 1-7: Çevresel yönetim teknikleri
- BAT 8-15: Genel performans iyileştirme (verimlilik dahil)
- BAT 28-42: Yakıta özel emisyon limitleri
- BAT 43-52: CHP spesifik gereksinimler

**Gıda, İçecek ve Süt (FDM BREF 2019):**
- Kapsam: > 300 ton/gün veya > 200 ton/gün (hayvansal ürün)
- BAT 1-5: Genel enerji verimliliği teknikleri
- BAT 6-8: Su tüketimi azaltma
- BAT 12-15: Kurutma ve ısıtma spesifik teknikler
- BAT 25-30: Soğutma ve dondurma BAT

**Çimento (CLM BREF 2013):**
- Kapsam: > 500 ton/gün klinker kapasitesi
- BAT 1-3: Genel teknikler — enerji yönetimi, hammadde seçimi
- BAT 4-10: Klinker üretimi — fırın verimi, alternatif yakıt
- BAT 15-20: Emisyon kontrol — toz, NOx, SO₂

---

## 6. ExergyLab'da BAT Kullanımı

### 6.1 Proses Boşluk Analizinde
```
1. Proses tipi belirlenir (ör. "heating")
2. İlgili proses dosyası yüklenir (ör. process/heating.md)
3. BAT SEC / BAT η_ex değeri okunur
4. ESI ve BPR hesaplanır (bkz. gap_analysis_methodology.md)
```

### 6.2 AI Yorumlama Kuralları
```
EĞER η_actual > η_BAT → "BAT üzerinde performans, best-in-class"
EĞER η_actual ≈ η_BAT (±5%) → "BAT seviyesinde, bakım odaklı iyileştirme"
EĞER η_actual < η_BAT × 0.80 → "BAT altında, teknoloji güncellemesi değerlendir"
EĞER η_actual < η_BAT × 0.50 → "BAT'ın çok altında, kapsamlı modernizasyon gerekli"
```

### 6.3 BAT Değerlerinin Engine Entegrasyonu

ExergyLab'ın `engine/bat_references.py` dosyası, her proses tipi ve alt kategorisi için BAT referans değerlerini tutar. Bu değerlerin kaynağı ve güvenilirlik seviyesi aşağıdaki gibi eşleştirilir:

| Proses Tipi | Engine Alanı | BAT Kaynağı | Güvenilirlik |
|-------------|-------------|-------------|-------------|
| `drying` | `exergy_efficiency_pct` | FDM BREF 2019, ENE BREF 2009 | B |
| `heating` | `exergy_efficiency_pct` | LCP BREF 2017 | A |
| `cooling` | `exergy_efficiency_pct` | ICS BREF 2001 | B (eski) |
| `steam_generation` | `exergy_efficiency_pct` | LCP BREF 2017, ENE BREF 2009 | A |
| `compressed_air` | `exergy_efficiency_pct` | ENE BREF 2009 | B |
| `chp` | `exergy_efficiency_pct` | LCP BREF 2017 | A |
| `cold_storage` | `exergy_efficiency_pct` | ICS BREF 2001, FDM BREF 2019 | B |
| `general_manufacturing` | `exergy_efficiency_pct` | CLM/GLS/PP BREF | A-B |

### 6.4 BAT Güncelleme Prosedürü (ExergyLab İçin)

Yeni bir BREF yayınlandığında ExergyLab'da aşağıdaki güncelleme adımları izlenir:

```
1. Yeni BAT Conclusions okunur → enerji performans değerleri çıkarılır
2. Enerji verimi → exergy verimine dönüştürülür (Bölüm 3 formülleri)
3. engine/bat_references.py'deki BAT_REFERENCES dict güncellenir
4. İlgili knowledge/factory/process/*.md dosyaları güncellenir
5. Testler güncellenir (tests/test_gap_analysis.py)
6. bat_overview.md'deki Bölüm 5 tablosu güncellenir
```

---

## İlgili Dosyalar

- `factory/process/gap_analysis_methodology.md` — 3 katmanlı boşluk modeli ve formüller
- `factory/process/sustainability_index.md` — ESI derecelendirme sistemi
- `factory/process/index.md` — Proses bilgi tabanı navigasyon haritası
- Her proses dosyası (`heating.md`, `steam_generation.md`, vb.) — Proses bazlı BAT değerleri
- `factory/factory_benchmarks.md` — Fabrika seviyesi sektörel benchmark

## Referanslar

1. European Commission (2010). Directive 2010/75/EU on Industrial Emissions (IED).
2. European Commission, JRC (2009). *Reference Document on Best Available Techniques for Energy Efficiency (ENE BREF)*.
3. European Commission, JRC (2017). *Best Available Techniques (BAT) Reference Document for Large Combustion Plants (LCP BREF)*.
4. European Commission, JRC (2001). *Reference Document on the Application of Best Available Techniques to Industrial Cooling Systems (ICS BREF)*.
5. European Commission, JRC (2019). *Best Available Techniques (BAT) Reference Document for the Food, Drink and Milk Industries (FDM BREF)*.
6. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
7. Szargut, J., Morris, D.R. & Steward, F.R. (1988). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*. Hemisphere.
8. European Commission (2012). Implementing Decision 2012/134/EU — BAT Conclusions for Iron and Steel Production.
9. European Parliament & Council (2010). Directive 2010/75/EU on Industrial Emissions — Article 3(10), 14, 15, 21.
10. JRC Reference Report on Monitoring of Emissions to Air and Water from IED Installations (2018). — Ölçüm ve doğrulama metodolojisi.
11. European Commission (2017). *Commission Implementing Decision (EU) 2017/1442* — BAT Conclusions for Large Combustion Plants. Official Journal L 212.
12. Ptasinski, K.J., Prins, M.J. & Pierik, A. (2007). "Exergetic evaluation of biomass gasification." *Energy*, 32(4), 568-574. — Biyokütle exergy/enerji oranları.
