---
title: "Isı Pompalı Kurutucu (Heat Pump Dryer)"
category: dryer
equipment_type: dryer
keywords: [ısı pompası, heat pump dryer, HPD, kapalı döngü, enerji verimli kurutma]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/solutions/heat_pump_retrofit.md, dryer/sectors/food_drying.md, dryer/sectors/wood_drying.md]
use_when: ["Isı pompalı kurutucu analiz edilirken", "Yüksek verimli kurutma değerlendirilirken"]
priority: medium
last_updated: 2026-02-01
---

# Isı Pompalı Kurutucu (Heat Pump Dryer)

> Son güncelleme: 2026-02-01

## Genel Bakış

Isı pompalı kurutucu (Heat Pump Dryer — HPD), buhar sıkıştırma soğutma çevrimini kurutma prosesine entegre ederek endüstriyel kurutucular arasında en yüksek enerji verimliliğini sağlayan sistemdir. Kapalı döngü (closed-loop) çalışma prensibi sayesinde egzoz havası kayıpları ortadan kalkar; nemli kurutma havası evaporatörde soğutularak nemi yoğuşma ile alınır, ardından kondensörde yeniden ısıtılarak kurutma odasına geri gönderilir. Yoğuşan nem drene edilir.

Konvansiyonel konvektif kurutucularda egzoz havası ile birlikte kaybedilen latent ve sensible ısının büyük bölümü HPD'de sistem içinde geri kazanılır. Bu nedenle birim enerji başına uzaklaştırılan nem miktarı (SMER) tüm kurutucu tipleri arasında en yüksektir.

**Temel Özellikler:**

| Parametre | Değer | Not |
|-----------|-------|-----|
| Çalışma sıcaklığı | 30-70 °C | Düşük sıcaklık avantajı |
| SMER (Specific Moisture Extraction Rate) | 1.0-4.0 kg/kWh | Sınıfının en iyisi |
| Exergy verimi | %15-35 | Kurutucular arasında en yüksek |
| COP_kurutma (drying COP) | 2.0-4.0 | SMER / SMER_ideal oranı |
| Tipik kapasite | 10-2,000 kg/h | Düşük-orta kapasite uygulamaları |
| Enerji kaynağı | Tamamen elektrik | Kompresör + fan |

---

## Çalışma Prensibi

HPD, kapalı döngü (closed-loop) bir sistemdir. Kurutma havası dışarıya atılmaz; sürekli olarak sistem içinde sirkülasyon yapar. Temel çalışma adımları:

1. **Kurutma odası:** Sıcak, kuru hava ürün üzerinden geçerek nemi alır. Hava nemli ve nispeten soğuk olarak odadan çıkar.
2. **Evaporatör (buharlaştırıcı):** Nemli kurutma havası, ısı pompasının evaporatör serpantini üzerinden geçirilir. Hava soğutularak çiğ noktasının altına düşürülür; havadaki nem yoğuşarak sıvı halde toplanır ve drene edilir (dehumidification).
3. **Kondensör (yoğuşturucu):** Nemsizleştirilmiş soğuk hava, ısı pompasının kondensör serpantini üzerinden geçirilir. Soğutucu akışkanın yoğuşma ısısı havaya aktarılır; hava tekrar kurutma sıcaklığına ısıtılır.
4. **Tekrar kurutma odasına besleme:** Kuru ve sıcak hava, kurutma odasına geri gönderilerek döngü tamamlanır.

```
Kapalı Döngü Şeması:

  Kurutma Odası (30-70 °C, düşük RH)
       |                    ^
       | nemli hava          | kuru, sıcak hava
       v                    |
  EVAPORATÖR ───────> KONDENSÖR
  (soğutma,           (ısıtma,
   nem yoğuşması)      hava ısıtma)
       |                    ^
       +--- Kompresör ------+
       |
  Yoğuşma suyu drenajı
```

**Enerji akışı karşılaştırması:**

```
Konvansiyonel kurutucu:  Q_giriş = Q_buharlaşma + Q_egzoz_kayıp + Q_yüzey_kayıp
Isı pompalı kurutucu:    Q_giriş = W_kompresör + W_fan  (Q_egzoz ≈ 0, geri kazanılır)

Egzoz kaybı eliminasyonu: tipik %30-50 toplam enerjinin
```

---

## Soğutma Çevrimi

HPD, standart buhar sıkıştırma soğutma çevrimi (vapor compression cycle) üzerine kuruludur. Çevrim bileşenleri ve kurutma döngüsüne entegrasyonu:

| Bileşen | İşlev | Tipik Koşul |
|---------|-------|-------------|
| Kompresör (compressor) | Soğutucu akışkanı sıkıştırarak basınç ve sıcaklığını yükseltir | 2-50 kW elektrik giriş |
| Kondensör (condenser) | Nemsizleştirilmiş havaya ısı vererek kurutma sıcaklığına getirir | Hava çıkış: 40-70 °C |
| Genleşme vanası (expansion valve) | Soğutucu akışkan basıncını düşürür, evaporatör girişini hazırlar | Elektronik genleşme vanası (EEV) tercih |
| Evaporatör (evaporator) | Nemli kurutma havasını soğutarak nem yoğuşması sağlar | Yüzey sıcaklığı: 5-15 °C |

### COP Hesabı (Coefficient of Performance)

```
COP_kurutma = Q_kondensör / W_kompresör

Burada:
  COP_kurutma  = Kurutma performans katsayısı (boyutsuz, tipik 2.0-4.0)
  Q_kondensör  = Kondensörde havaya verilen ısı (kW)
  W_kompresör  = Kompresör elektrik tüketimi (kW)
```

### SMER Hesabı

```
SMER = ṁ_su / (W_kompresör + W_fan)   [kg/kWh]

Burada:
  ṁ_su  = Birim zamanda uzaklaştırılan su miktarı (kg/h)
  W_fan = Sirkülasyon fanı elektrik tüketimi (kW)

İdeal SMER (sadece latent ısı bazında):
  SMER_ideal ≈ 3,600 / h_fg ≈ 3,600 / 2,400 ≈ 1.50 kg/kWh  (60 °C'de)

HPD'de COP > 1 olduğundan SMER, SMER_ideal değerini aşabilir.
```

### Soğutucu Akışkan Seçimi

| Soğutucu Akışkan | GWP | Kondensör T_max (°C) | Durum |
|------------------|-----|----------------------|-------|
| R134a | 1,430 | ~70 | F-gas ile aşamalı kısıtlama |
| R290 (propan) | 3 | ~70 | Düşük GWP, yanıcı — tercih ediliyor |
| R744 (CO2) | 1 | ~90 | Yüksek sıcaklık, özel tasarım |
| R1234ze(E) | <1 | ~75 | Yeni nesil, endüstriyel tavsiye |

---

## Parametreler

### Çalışma Koşulları

| Parametre | Aralık | Birim | Not |
|-----------|--------|-------|-----|
| Kurutma havası sıcaklığı | 30-70 | °C | Düşük sıcaklık, ısıya duyarlı ürünler |
| Kurutma havası bağıl nemi (giriş) | %15-35 | RH | Nemsizleştirme sonrası |
| Dönüş havası bağıl nemi | %60-90 | RH | Kurutma odasından çıkış |
| Evaporatör yüzey sıcaklığı | 5-15 | °C | Çiğ noktasının altında |
| Ortam sıcaklığı (kapalı döngü) | 10-35 | °C | Kapalı döngüde etki minimum |
| Kompresör gücü | 2-50 | kW | Kapasiteye bağlı |
| Fan gücü | 1-10 | kW | Toplam gücün ~%10-15'i |

### SMER Benchmark Değerleri

| Durum | SMER (kg/kWh) | Açıklama |
|-------|---------------|----------|
| Düşük performans | < 1.0 | Eski sistem, soğutucu kaçağı, defrost sorunu |
| Tipik performans | 1.0-2.0 | Standart işletme |
| İyi performans | 2.0-3.0 | Modern ekipman, optimize kontrol |
| En iyi uygulama (best practice) | 3.0-4.0 | Yeni nesil soğutucu akışkan, tam optimizasyon |

---

## Exergy Analizi

### Neden HPD'de Exergy Verimi Yüksektir?

Konvansiyonel kurutucularda yüksek sıcaklıktaki enerji kaynağı (>200 °C gaz yanması veya >150 °C buhar) düşük sıcaklıktaki buharlaştırma işlemine (~60-100 °C) kullanılır. Bu büyük sıcaklık farkı (temperature mismatch) ciddi exergy yıkımına neden olur.

HPD'de ise:
- **Enerji girişi tamamen elektrik (iş)**: Elektrik saf exergy'dir (%100 exergy içeriği), ancak COP sayesinde birim elektrik başına birden fazla birim ısı sağlanır.
- **Düşük sıcaklık farkı:** Kondensör ile kurutma odası arasındaki ΔT düşüktür (10-20 °C), ısı transferi tersinmezliği azalır.
- **Egzoz kaybı yok:** Kapalı döngü sayesinde egzoz exergy kaybı ortadan kalkar.

### Exergy Verimi Hesabı

```
ψ_HPD = Ėx_nem_uzaklaştırma / (W_kompresör + W_fan)

Burada:
  ψ_HPD             = Exergy verimi (boyutsuz, tipik 0.15-0.35)
  Ėx_nem_uzaklaştırma = Nem uzaklaştırma için gereken minimum exergy (kW)
  W_kompresör        = Kompresör elektrik tüketimi (kW)
  W_fan              = Fan elektrik tüketimi (kW)

Ėx_nem_uzaklaştırma = ṁ_su × [(h_sıvı - h₀) - T₀ × (s_sıvı - s₀)]

Burada:
  ṁ_su    = Uzaklaştırılan su debisi (kg/s)
  h₀, s₀  = Ölü durum (dead state) değerleri (T₀=298.15 K, P₀=101.325 kPa)
```

### COP'a Göre Exergy Verimi ve SMER

| COP_kurutma | Exergy Verimi (%) | SMER (kg/kWh) | Tipik Koşul |
|-------------|-------------------|----------------|-------------|
| 2.0 | 15-20 | 1.0-1.5 | Düşük COP, eski sistem |
| 2.5 | 18-24 | 1.5-2.0 | Orta performans |
| 3.0 | 22-28 | 2.0-3.0 | İyi performans |
| 3.5 | 26-32 | 2.5-3.5 | Modern optimize sistem |
| 4.0 | 30-35 | 3.0-4.0 | En iyi uygulama |

---

## Kayıp Dağılımı

Tipik bir HPD için exergy kayıp dağılımı (tüm giriş elektrik bazında):

| Kayıp Kalemi | Oran (%) | Açıklama |
|--------------|----------|----------|
| Kompresör tersinmezliği (compressor irreversibility) | 25-35 | En büyük kaynak — izentropik verimi belirler |
| Kondensör ısı transferi tersinmezliği | 10-15 | ΔT büyüdükçe artar |
| Evaporatör ısı transferi tersinmezliği | 8-12 | Yüzey alanı yetersizliği |
| Genleşme vanası tersinmezliği | 3-5 | Throttling kaybı |
| Fan tersinmezliği | 5-8 | Aerodinamik kayıplar |
| Yüzey/radyasyon kayıpları | 2-5 | İzolasyona bağlı |
| Defrost döngüsü kaybı | 3-8 | Evaporatör buz çözme |
| **Faydalı çıkış (nem uzaklaştırma exergy)** | **15-35** | **Exergy verimi** |

```
Exergy Akışı (Grassmann) — HPD:

EXERGY GİRİŞİ (100% elektrik)
│
├── Kompresör girdisi (%80-85)
│   ├── Kompresör tersinmezliği (%25-35) ───> EXERGY YIKIM
│   ├── Kondensör → hava ısıtma (%10-15) ───> ΔT tersinmezliği
│   ├── Evaporatör ← nem alma (%8-12) ──────> ΔT tersinmezliği
│   └── Faydalı nem uzaklaştırma (%15-35) ──> FAYDALI ÇIKIŞ
│
├── Fan girdisi (%10-15)
│   └── Aerodinamik kayıp (%5-8) ───────────> EXERGY YIKIM
│
└── Yüzey + defrost kayıpları (%5-13) ─────> KAYIP
```

---

## Konvansiyonel ile Karşılaştırma

### Kurutucu Tiplerine Göre Performans Karşılaştırması

| Parametre | Konvektif Tünel | Döner Tambur | Akışkan Yatak | Sprey Kurutucu | **HPD** |
|-----------|-----------------|-------------|---------------|----------------|---------|
| Çalışma sıcaklığı (°C) | 80-200 | 100-250 | 80-200 | 150-250 | **30-70** |
| SMER (kg/kWh) | 0.5-1.0 | 0.6-1.0 | 0.8-1.5 | 0.3-0.8 | **1.0-4.0** |
| Enerji verimi (%) | 40-60 | 45-65 | 50-70 | 30-55 | **60-85** |
| Exergy verimi (%) | 5-12 | 8-15 | 10-18 | 5-12 | **15-35** |
| Enerji kaynağı | Gaz/buhar | Gaz/buhar | Gaz/buhar | Gaz/buhar | **Elektrik** |
| Egzoz kaybı | Yüksek | Yüksek | Orta-yüksek | Çok yüksek | **Yok (kapalı)** |
| Kapasite (kg/h) | 100-10,000+ | 500-50,000+ | 100-5,000 | 100-20,000+ | **10-2,000** |
| Yatırım maliyeti (baz) | 1.0x | 1.0x | 1.2x | 1.5x | **2.0-4.0x** |
| İşletme maliyeti (baz) | 1.0x | 0.9x | 0.8x | 1.2x | **0.3-0.6x** |

### Enerji Analizi — Elektrik Girişi vs Termal Eşdeğer

HPD tamamen elektrikle çalışır. Konvansiyonel sistemlerle adil karşılaştırma için birincil enerji bazında değerlendirme yapılmalıdır:

```
Konvansiyonel (doğalgaz):
  Birincil enerji = Q_gaz / η_yakma
  Örnek: 100 kW termal / 0.90 = 111 kW birincil

HPD (elektrik + COP):
  Birincil enerji = W_elektrik / η_santral = (Q_termal / COP) / η_santral
  Örnek: 100 kW termal / 3.0 COP / 0.40 santral = 83.3 kW birincil

Birincil enerji tasarrufu: (111 - 83.3) / 111 = %25
COP > 2.5 olduğunda HPD birincil enerji bazında da avantajlıdır.
```

---

## Avantajlar ve Dezavantajlar

### Avantajlar

1. **En yüksek enerji verimliliği:** SMER 1.0-4.0 kg/kWh ile tüm kurutucu tipleri arasında en verimli. İşletme enerji maliyeti konvansiyonelin %30-60'ı düzeyinde.
2. **Kapalı döngü — egzoz emisyonu yok:** Atmosfere sıcak/nemli hava atılmaz. Toz, uçucu organik bileşik (VOC) ve koku emisyonu minimize edilir. Çevresel uyumluluk avantajı.
3. **Düşük sıcaklık — ürün kalitesi:** 30-70 °C çalışma sıcaklığı, ısıya duyarlı ürünlerde (enzimler, vitaminler, renk, aroma, aktif bileşenler) kalite korumasını sağlar.
4. **Ortam koşullarından bağımsız nemgiderme:** Kapalı döngü sayesinde dış hava sıcaklığı ve nemi performansı etkilemez. Yılın her mevsiminde sabit SMER.
5. **Hassas kontrol:** Sıcaklık ve nem düzeyi bağımsız olarak kontrol edilebilir. Kurutma profili ürüne göre optimize edilebilir.

### Dezavantajlar

1. **Yüksek yatırım maliyeti:** Konvansiyonel kurutuculara göre 2-4 kat daha yüksek ilk yatırım. Soğutma çevrimi ekipmanları (kompresör, eşanjörler, soğutucu akışkan şarjı) ek maliyet yaratır.
2. **Sınırlı sıcaklık aralığı:** Standart soğutucu akışkanlarla (R134a, R290) kondensör çıkış sıcaklığı ~70 °C ile sınırlıdır. Yüksek sıcaklık gerektiren ürünler için CO2 (R744) transkritik veya kaskad sistem gerekir.
3. **Bakım gereksinimi (soğutma çevrimi):** Kompresör, soğutucu akışkan kaçak kontrolü, defrost sistemi bakımı ek operasyonel yük getirir. Uzman teknisyen gerektirir.
4. **Düşük throughput:** Düşük çalışma sıcaklığı nedeniyle kurutma hızı yavaştır. Aynı kapasite için daha büyük kurutma odası veya daha uzun kurutma süresi gerekir.
5. **Defrost döngüsü:** Evaporatör yüzeyinde buzlanma oluşur; periyodik defrost enerji tüketir ve kurutma sürekliliğini kesintiye uğratır. Akıllı defrost (demand-based) ile minimize edilebilir.

---

## Uygulamalar

HPD, düşük-orta kapasite ve ısıya duyarlı ürün kurutma uygulamalarında öne çıkar:

| Uygulama Alanı | Tipik Ürün | Sıcaklık (°C) | SMER (kg/kWh) | Avantaj |
|----------------|------------|----------------|----------------|---------|
| Kereste/ahşap kurutma (timber drying) | Çam, meşe, kayın | 35-65 | 1.5-3.5 | Çatlama riski azalır, düzgün kurutma |
| Bitki/ot kurutma (herbs) | Kekik, nane, adaçayı | 30-45 | 1.5-3.0 | Uçucu yağlar korunur, renk kalitesi |
| Baharat kurutma (spices) | Karabiber, tarçın, zencefil | 35-50 | 1.5-2.5 | Aroma ve aktif bileşen koruması |
| Yüksek değerli gıda (premium food) | Meyve, sebze dilimleri | 35-55 | 1.0-2.5 | Vitamin, renk ve doku koruması |
| İlaç hammaddeleri (pharmaceutical) | Bitki ekstraktları, granüller | 30-50 | 1.0-2.0 | GMP uyumlu, hassas sıcaklık |
| Deniz ürünleri (seafood) | Balık, karides, yosun | 35-55 | 1.0-2.5 | Protein bozunması önlenir |
| Arıtma çamuru (sludge drying) | Atıksu çamuru | 45-70 | 1.0-2.0 | Kapalı döngü koku avantajı |

**Sektör dağılımı:** Kereste kurutma HPD'nin en olgun ve yaygın uygulama alanıdır. Gıda ve ilaç sektörleri en hızlı büyüyen segmentlerdir.

---

## İyileştirme

Mevcut HPD sistemlerinde uygulanabilecek enerji verimliliği önlemleri:

| Önlem | Enerji Tasarrufu (%) | Geri Ödeme | Detay |
|-------|----------------------|------------|-------|
| Değişken hızlı kompresör (VSD/inverter) | 10-20 | 1-3 yıl | Kısmi yükte COP iyileştirmesi |
| Soğutucu akışkan değişimi (düşük GWP) | 5-15 | 2-4 yıl | R134a → R290 veya R1234ze(E) |
| Akıllı defrost kontrolü (demand defrost) | 5-10 | 0.5-1 yıl | Zamanlayıcı yerine sensör bazlı |
| Evaporatör/kondensör boyutlandırma | 5-10 | 2-3 yıl | Daha büyük ısı değiştirici = düşük ΔT = yüksek COP |
| VSD fan (değişken hızlı sirkülasyon fanı) | 3-8 | 1-2 yıl | Hava debisini kurutma aşamasına göre ayarla |
| Ön nem giderme (mekanik sıkma/pres) | 10-20 | 1-2 yıl | Termal yükü azaltarak HPD verimini artır |
| Sızdırmazlık iyileştirmesi | 2-5 | <0.5 yıl | Kapalı döngü hava kaçaklarını önle |
| Subcooling/superheating optimizasyonu | 3-7 | 1-2 yıl | Soğutma çevrimi optimizasyonu |

---

## Yatırım ve Ekonomik Analiz

### Kapasite-Maliyet Tablosu (2026, Avrupa Piyasası)

| Kapasite (kg/h ürün) | Nem Çıkarma (kg/h) | SMER (kg/kWh) | Elektrik (kW) | Tahmini Yatırım (EUR) |
|----------------------:|--------------------:|---------------:|--------------:|----------------------:|
| 10-50 | 5-25 | 1.0-2.5 | 2-10 | 15,000-50,000 |
| 50-200 | 25-100 | 1.5-3.0 | 8-35 | 50,000-150,000 |
| 200-500 | 100-250 | 2.0-3.5 | 30-75 | 120,000-250,000 |
| 500-1,000 | 250-500 | 2.5-3.8 | 70-150 | 200,000-350,000 |
| 1,000-2,000 | 500-1,000 | 2.5-4.0 | 140-280 | 300,000-500,000 |

> **Not:** Yatırım maliyetleri kurutma odası hariçtir. Konvansiyonel konvektif kurutucuya göre 2-4 kat daha yüksek yatırım, ancak işletme maliyeti %40-70 daha düşüktür.

### Ekonomik Karşılaştırma Örneği

Senaryo: 200 kg/h nem çıkarma kapasitesi, 4,000 saat/yıl çalışma

| Kalem | Konvansiyonel (doğalgaz) | HPD (elektrik) |
|-------|--------------------------|----------------|
| Enerji tüketimi | 200 kW termal (222 kW gaz) | 66 kW elektrik (COP=3.0) |
| Enerji birim fiyatı | 0.05 EUR/kWh (gaz) | 0.12 EUR/kWh (elektrik) |
| Yıllık enerji maliyeti | 222 × 4,000 × 0.05 = 44,400 EUR | 66 × 4,000 × 0.12 = 31,680 EUR |
| Yıllık tasarruf | — | 12,720 EUR/yıl |
| Yatırım farkı | Referans | +100,000 EUR (ek maliyet) |
| Basit geri ödeme | — | 100,000 / 12,720 = **7.9 yıl** |

```
Elektrik/gaz fiyat oranı kritik eşik: ~3.0
  Oran < 3.0: HPD ekonomik olarak avantajlı
  Oran > 3.0: Ekonomik avantaj azalır, ürün kalitesi ve çevresel faydalar değerlendirilmeli

Karbon vergisi (>50 EUR/ton CO2) HPD geri ödeme süresini 1-2 yıl kısaltır.
```

### Yatırım Karar Kriterleri

- HPD şu durumlarda öncelikli tercih edilmelidir:
  - Ürün ısıya duyarlı (T < 70 °C yeterli)
  - Kapasite < 2,000 kg/h
  - Çevresel emisyon kısıtlaması var (kapalı döngü gerekli)
  - Yıllık çalışma süresi > 3,000 saat (yüksek işletme saati yatırımı amorti eder)
  - Ürün katma değeri yüksek (kalite primi > enerji maliyeti)

---

## İlgili Dosyalar

- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Exergy hesaplama formülleri: `dryer/formulas.md`
- Isı pompası retrofit rehberi: `dryer/solutions/heat_pump_retrofit.md`
- Gıda kurutma sektör bilgisi: `dryer/sectors/food_drying.md`
- Ahşap kurutma sektör bilgisi: `dryer/sectors/wood_drying.md`
- Tünel kurutucu: `dryer/equipment/tunnel_dryer.md`
- Sprey kurutucu: `dryer/equipment/spray_dryer.md`
- Chiller bilgi (ısı pompası teknolojisi): `chiller/equipment/systems_overview.md`
- Fabrika seviye analiz: `factory/cross_equipment.md`

---

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press — Chapter 17: Heat Pump Drying.
2. Chua, K.J., Chou, S.K. & Yang, W.M. (2010). "Heat pump drying: Recent developments and future trends," *Drying Technology*, 28(12), 1518-1533.
3. Colak, N. & Hepbasli, A. (2009). "A review of heat pump drying: Part 1 — Systems, models and studies," *Energy Conversion and Management*, 50, 2180-2186.
4. Colak, N. & Hepbasli, A. (2009). "A review of heat pump drying: Part 2 — Exergy analysis," *Energy Conversion and Management*, 50, 2187-2193.
5. European Commission, EU BREF — "Reference Document on Best Available Techniques for Energy Efficiency," 2009 (revised 2017).
6. EU F-gas Regulation 517/2014 — Soğutucu akışkan düzenlemeleri.
7. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press.
8. Minea, V. (2013). "Heat pump-assisted drying: Recent technological advances and emerging opportunities," *Drying Technology*, 31(10), 1177-1189.
9. Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley — Exergy analizi referansı.
10. IEA Heat Pump Centre, *Heat Pump Drying — Technology Brief*.
