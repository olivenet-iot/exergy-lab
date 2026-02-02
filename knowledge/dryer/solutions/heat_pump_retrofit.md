---
title: "Isı Pompası Retrofit (Heat Pump Dryer Retrofit)"
category: dryer
equipment_type: dryer
keywords: [ısı pompası, heat pump retrofit, HPD, enerji verimliliği, kapalı döngü]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/equipment/heat_pump_dryer.md, dryer/solutions/exhaust_heat_recovery.md, factory/waste_heat_recovery.md]
use_when: ["Düşük sıcaklık kurutma (<80°C) yapılırken", "Yüksek enerji maliyetli kurutma tesislerinde", "Isı pompalı kurutucu dönüşümü değerlendirilirken"]
priority: medium
last_updated: 2026-02-01
---
# Isı Pompası Retrofit (Heat Pump Dryer Retrofit)

> Son güncelleme: 2026-02-01

## Genel Bakış

Endüstriyel kurutma süreçleri toplam sanayi enerji tüketiminin %12-20'sini oluşturur ve konvansiyonel konvektif kurutucularda exergy verimi yalnızca %5-15 seviyesindedir. Bu düşük verimin temel nedeni, yüksek sıcaklıktaki ısı kaynağının (>200 °C gaz yanması veya >150 °C buhar) düşük sıcaklıktaki buharlaştırma işlemine (60-100 °C) kullanılmasıdır. Egzoz havası ile atmosfere atılan latent ve sensible ısı, toplam enerji girdisinin %30-50'sine ulaşabilir.

Isı pompası retrofit çözümü, mevcut konvansiyonel kurutucuya bir buhar sıkıştırmalı ısı pompası devresi (heat pump dehumidification loop) eklenmesiyle bu kaybı büyük ölçüde ortadan kaldırır. Evaporatör egzoz havasından nemi yoğuştururken latent ısıyı geri kazanır; kondensör bu ısıyı kurutma havasına geri vererek hava sıcaklığını yükseltir. Sonuç: %50-70 enerji tasarrufu, SMER değerinin 0.5'ten 2.0+ kg/kWh'a yükselmesi ve exergy veriminde 2-4 kat artış.

**Tipik Tasarruf:** %50-70 enerji tüketiminde azalma (konvansiyonel konvektif sisteme göre)
**Tipik ROI:** 2-5 yıl (enerji fiyatlarına ve çalışma süresine bağlı)
**Hedef Kitle:** Kurutma sıcaklığı <80 °C olan tesisler

## Tetikleyici (Trigger Conditions)

Isı pompası retrofit değerlendirmesi aşağıdaki koşulların **her ikisi** birden sağlandığında başlatılmalıdır:

1. **Kurutma sıcaklığı < 80 °C:** Mevcut kurutucu, düşük-orta sıcaklıkta (40-80 °C) çalışıyorsa ısı pompası COP'u yeterince yüksek olur (COP > 2.5). Yüksek sıcaklık uygulamalarında (>80 °C) mevcut soğutucu akışkanların çalışma limitlerine yaklaşılır ve COP hızla düşer.

2. **Konvansiyonel ısı kaynağı kullanımı:** Mevcut sistem doğal gaz brülörü, buhar serpantini veya elektrik rezistansı ile ısıtma yapıyorsa ve egzoz havası doğrudan atmosfere atılıyorsa, ısı pompası retrofiti büyük enerji tasarrufu sağlar.

### Ek Tetikleyiciler

| Koşul | Açıklama | Etkisi |
|-------|----------|--------|
| Enerji maliyeti > €0.05/kWh (gaz) veya > €0.10/kWh (elektrik) | Yüksek enerji fiyatları geri ödeme süresini kısaltır | ROI iyileşir |
| Yıllık çalışma süresi > 3,000 saat | Uzun çalışma süresi tasarruf potansiyelini artırır | Ekonomik fizibilite güçlenir |
| Sıcaklığa hassas ürün kurutma | Gıda, ilaç, biyomalzeme, aromatik bitkiler | Kalite primi ek fayda sağlar |
| Karbon azaltma hedefi | Tesis CO2 emisyon azaltma taahhüdü varsa | Yanmasız sistem ile sıfır direkt emisyon |
| Egzoz emisyon sınırlaması | Çevresel düzenleme baskısı | Kapalı döngüde egzoz yok |

### Tetikleyici Karar Ağacı

```
Kurutma sıcaklığı < 80°C?
├── EVET → Konvansiyonel ısı kaynağı kullanılıyor mu?
│   ├── EVET → Yıllık çalışma > 3,000 saat?
│   │   ├── EVET → ISI POMPASI RETROFIT DEĞERLENDİR
│   │   └── HAYIR → Ekonomik analiz yap (düşük kullanım riski)
│   └── HAYIR → Mevcut sistem zaten verimli mi? (Ör: atık ısı ile kurutma)
│       ├── EVET → Retrofit gereksiz
│       └── HAYIR → Alternatif çözümleri değerlendir
└── HAYIR (>80°C) → CO2 (R744) transkritik sistem değerlendir (COP düşük olacak)
    ├── 80-100°C → Sınırlı uygunluk, dikkatli analiz
    └── >100°C → Uygun değil, egzoz ısı geri kazanımı tercih et
```

## Retrofit Konfigürasyonları (System Configurations)

Isı pompası retrofiti üç temel konfigürasyonda uygulanabilir. Seçim, mevcut kurutucu tipine, kapasite ihtiyacına ve bütçeye göre yapılır.

### 1. Tam Kapalı Döngü (Full Closed-Loop)

Kurutma havası tamamen kapalı devre içinde döner. Egzoz atmosfere atılmaz.

```
┌──────────────────────────────────────────────────┐
│                  KURUTMA ODASI                    │
│  (Ürün kurutma: 40-70°C, %20-35 RH)             │
└──────────┬───────────────────────────┬───────────┘
           │ Nemli sıcak hava         │ Kuru sıcak hava
           ▼                          ▲
    ┌──────────────┐          ┌──────────────┐
    │  EVAPORATÖR   │          │  KONDENSÖR   │
    │  (Soğutma +   │ ------→ │  (Isıtma)    │
    │   Nem alma)   │ Soğutucu│              │
    └──────────────┘ Akışkan  └──────────────┘
           │                          ▲
           │    ┌──────────────┐      │
           └──→ │ KOMPRESÖR    │ ─────┘
                └──────────────┘
                    ▲
                    │ W_kompresör (elektrik)
```

| Parametre | Tipik Değer |
|-----------|-------------|
| Enerji tasarrufu | %60-70 |
| SMER | 2.5-4.0 kg/kWh |
| COP_drying | 3.0-5.0 |
| Egzoz kaybı | ~%0 (kapalı devre) |
| Kurutma süresi artışı | %20-40 |
| Uygunluk | Batch kabin, oda tipi kurutucular |

### 2. Kısmi Destek Modu (Partial Assist / Semi-Closed Loop)

Isı pompası mevcut konvansiyonel sisteme ek olarak çalışır. Hava kısmen geri devir edilir, kısmen taze hava alınır.

| Parametre | Tipik Değer |
|-----------|-------------|
| Enerji tasarrufu | %35-55 |
| SMER | 1.5-2.5 kg/kWh |
| COP_drying | 2.0-3.5 |
| Egzoz kaybı | %10-25 (kısmi egzoz) |
| Kurutma süresi artışı | %5-15 |
| Uygunluk | Tünel, bant kurutucular (mevcut sisteme ekleme) |

### 3. Hibrit Sistem (Heat Pump + Gaz Brülör Yedek)

Isı pompası birincil ısı kaynağı, gaz brülör ise yedek/destek olarak kullanılır. Yüksek yük dönemlerinde veya ısı pompası bakımında brülör devreye girer.

| Parametre | Tipik Değer |
|-----------|-------------|
| Enerji tasarrufu | %40-60 |
| SMER | 1.8-3.0 kg/kWh |
| COP_drying (HP kısmı) | 2.5-4.0 |
| Egzoz kaybı | %5-20 (brülör çalışırken) |
| Esneklik | Yüksek — çift kaynak |
| Uygunluk | Büyük kapasiteli ve değişken yüklü tesisler |

### Konfigürasyon Seçim Kriterleri

| Kriter | Tam Kapalı Döngü | Kısmi Destek | Hibrit |
|--------|-------------------|--------------|--------|
| Yatırım maliyeti | En yüksek | Orta | Yüksek |
| Enerji tasarrufu | En yüksek | Orta | Yüksek |
| Kapasite esnekliği | Düşük | Orta | Yüksek |
| Mevcut sisteme entegrasyon | Kapsamlı değişiklik | Kolay ekleme | Orta değişiklik |
| Kurutma süresi etkisi | Uzar | Az uzar | Esnek |
| Egzoz yönetimi | Yok (kapalı) | Kısmen var | Var |
| En uygun tesis tipi | Küçük-orta batch | Mevcut konvektif | Büyük endüstriyel |

## SMER ve Verimlilik İyileştirmesi (SMER Improvement)

Isı pompası retrofitinin temel performans göstergesi SMER'deki artıştır.

### Retrofit Öncesi / Sonrası Karşılaştırma

| Parametre | Konvansiyonel (Gaz Brülörlü) | Isı Pompası Retrofit | İyileşme |
|-----------|------------------------------|----------------------|----------|
| SMER | 0.4-1.0 kg/kWh | 2.0-4.0 kg/kWh | 3-5x artış |
| Enerji verimi (1. yasa) | %35-55 | %65-85 | +30 puan |
| Exergy verimi (2. yasa) | %5-12 | %15-30 | 2-4x artış |
| Egzoz enerji kaybı | %30-50 | %0-10 | Büyük azalma |
| Spesifik enerji tüketimi | 3,000-5,000 kJ/kg su | 900-1,800 kJ/kg su | %60-70 azalma |

### SMER İyileşme Faktörleri

SMER iyileşmesi aşağıdaki faktörlere bağlıdır:

1. **Isı pompası COP'u:** COP arttıkça SMER doğrusal olarak artar
2. **Kapalılık oranı:** Tam kapalı döngü > kısmi döngü > açık döngü
3. **Evaporatör boyutlandırması:** Büyük evaporatör = daha düşük kompresör sıcaklık farkı = daha yüksek COP
4. **Hava debisi optimizasyonu:** Optimal hava debisinde egzoz bağıl nemi %70-85 aralığında tutulur
5. **Defrost yönetimi:** Akıllı defrost (demand-based) ile enerji kaybı azalır

```
SMER_HP = COP_drying × SMER_conventional / η_burner

Örnek:
  COP = 3.5, SMER_conv = 0.7 kg/kWh, η_burner = 0.90
  SMER_HP = 3.5 × 0.7 / 0.90 = 2.72 kg/kWh
  İyileşme = 2.72 / 0.7 = 3.9× (%289 artış)
```

## COP Analizi (Coefficient of Performance)

### COP Tanımları

Isı pompası kurutma sisteminde iki farklı COP tanımı kullanılır:

```
COP_heating = Q_kondensör / W_kompresör [-]
  → Kondensörün kurutma havasına verdiği ısının kompresör gücüne oranı
  → Tipik: 3.0-5.0

COP_drying = m_water_removed × h_fg / W_total [-]
  → Uzaklaştırılan nemin latent ısısının toplam elektrik tüketimine oranı
  → Tipik: 2.0-4.0
  → W_total = W_kompresör + W_fan + W_yardımcı

SMER = m_water_removed / W_total [kg/kWh]
  → COP_drying ile doğrudan ilişkili: SMER = COP_drying / h_fg × 3,600
```

### COP'u Etkileyen Parametreler

| Parametre | COP Üzerindeki Etki | Açıklama |
|-----------|---------------------|----------|
| Evaporatör sıcaklığı (T_evap) | T_evap artar → COP artar | Daha düşük sıkıştırma oranı |
| Kondensör sıcaklığı (T_cond) | T_cond artar → COP düşer | Daha yüksek sıkıştırma oranı |
| (T_cond - T_evap) sıcaklık farkı | ΔT artar → COP düşer | Carnot sınırı etkisi |
| Soğutucu akışkan türü | Akışkana bağlı | R134a, R290 yüksek COP |
| Kompresör isentropik verimi | η_is artar → COP artar | İnvertörlü scroll kompresör tercih |
| Part-load (kısmi yük) | Kısmi yükte COP değişir | VSD kompresör avantajlı |

### COP Değerleri: Soğutucu Akışkan ve Çalışma Koşullarına Göre

| Soğutucu Akışkan | T_evap [°C] | T_cond [°C] | COP_heating | SMER [kg/kWh] | Uygulama |
|------------------|-------------|-------------|-------------|---------------|----------|
| R134a | 5 | 55 | 4.5 | 3.5 | Gıda, ilaç (düşük T) |
| R134a | 10 | 65 | 3.8 | 2.8 | Genel endüstriyel |
| R407C | 5 | 60 | 4.0 | 3.0 | Mevcut sistemler |
| R410A | 5 | 55 | 4.2 | 3.2 | HVAC kaynaklı |
| R410A | 10 | 70 | 3.3 | 2.4 | Orta-yüksek T |
| R290 (propan) | 5 | 60 | 4.3 | 3.3 | Yeni nesil, düşük GWP |
| R1234ze(E) | 5 | 65 | 3.9 | 2.9 | Yeni nesil, EU uyumlu |
| CO2 (R744) | 5 | 80 | 2.5 | 1.8 | Yüksek T (transkritik) |
| CO2 (R744) | 10 | 90 | 2.0 | 1.4 | Çok yüksek T |

### COP_heating ile COP_drying Karşılaştırması

```
COP_drying < COP_heating çünkü:
  1. Fan enerjisi (W_fan) COP_drying paydasına dahildir
  2. Defrost kayıpları gerçek COP'u düşürür
  3. Yardımcı ekipman (konveyör, kontrol) enerji tüketir
  4. Kısmi yük çalışmada COP düşer

Tipik ilişki:
  COP_drying ≈ COP_heating × 0.65-0.80
```

## Ekonomik Analiz (Economic Analysis)

### Yatırım Maliyeti

Isı pompası retrofit yatırımı konvansiyonel sisteme göre daha yüksektir ancak işletme maliyeti çok daha düşüktür.

| Kapasite (kg su/saat) | Retrofit Maliyeti [EUR] | Yeni HP Kurutucu [EUR] | Birim Maliyet [EUR/kW_evap] |
|----------------------:|------------------------:|------------------------:|----------------------------:|
| 10-50 | 30,000-60,000 | 50,000-90,000 | 350-500 |
| 50-100 | 60,000-100,000 | 90,000-150,000 | 300-450 |
| 100-200 | 100,000-150,000 | 150,000-220,000 | 250-400 |
| 200-500 | 150,000-200,000 | 200,000-350,000 | 200-350 |

**Maliyet kalemleri:** Isı pompası ünitesi (%45-55), evaporatör/kondensör serpantinleri (%15-20), kanal modifikasyonu (%10-15), kontrol sistemi entegrasyonu (%8-12), montaj ve devreye alma (%10-15).

### Örnek Ekonomik Analiz

**Senaryo:** Kereste kurutma tesisi, 100 kg su/saat kapasite

| Parametre | Konvansiyonel (Gaz) | Isı Pompası Retrofit |
|-----------|---------------------|----------------------|
| Kurutma sıcaklığı | 65 °C | 55 °C |
| SMER | 0.6 kg/kWh | 2.5 kg/kWh |
| Enerji tüketimi | 167 kW (gaz) | 40 kW (elektrik) |
| Enerji maliyeti | €0.045/kWh | €0.12/kWh |
| Saatlik enerji maliyeti | €7.50/saat | €4.80/saat |
| Yıllık çalışma süresi | 5,000 saat | 5,000 saat |
| Yıllık enerji maliyeti | €37,500/yıl | €24,000/yıl |
| **Yıllık tasarruf** | — | **€13,500/yıl** |

```
Retrofit yatırım maliyeti: €55,000
Yıllık enerji tasarrufu:   €13,500/yıl
Kalite primi (düşük T):    ~€4,000/yıl (tahmini — daha az çatlama, daha iyi renk)
Bakım farkı:               -€1,500/yıl (HP bakım gideri artışı)
Net yıllık fayda:          €16,000/yıl

Basit geri ödeme süresi (SPP) = €55,000 / €16,000 = 3.4 yıl

TCO karşılaştırması (10 yıllık):
  Konvansiyonel: €37,500 × 10 = €375,000
  Isı pompası:   €55,000 + (€24,000 + €1,500) × 10 = €310,000
  TCO avantajı:  €65,000 → HP retrofit 10 yılda €65,000 daha ekonomik
  Kırılma noktası (break-even): ~3.4 yıl
```

### Basit Geri Ödeme Süresi (SPP) Hassasiyet Analizi

| Gaz Fiyatı [EUR/kWh] | Elektrik Fiyatı [EUR/kWh] | Yıllık Tasarruf [EUR] | SPP [yıl] |
|----------------------:|-------------------------:|----------------------:|----------:|
| 0.035 | 0.10 | 9,250 | 5.9 |
| 0.045 | 0.10 | 13,750 | 4.0 |
| 0.045 | 0.12 | 13,500 | 4.1 |
| 0.055 | 0.10 | 18,250 | 3.0 |
| 0.055 | 0.12 | 16,500 | 3.3 |
| 0.055 | 0.15 | 14,250 | 3.9 |
| 0.065 | 0.12 | 20,750 | 2.7 |
| 0.065 | 0.15 | 18,500 | 3.0 |

**Sonuç:** Gaz fiyatının yüksek ve elektrik/gaz fiyat oranının < 3.0 olduğu senaryolarda ısı pompası retrofiti 3 yılın altında geri öder. Fiyat oranı > 3.5 olduğunda ekonomik avantaj önemli ölçüde azalır.

### TCO Avantaj Noktası

Isı pompası retrofit yatırımı tipik olarak **3-4. yıldan itibaren** konvansiyonel sisteme göre toplam sahip olma maliyeti (TCO) avantajı sağlamaya başlar. Sistemin ekonomik ömrü 15-20 yıl olduğundan, uzun vadeli fayda çok yüksektir.

## Uygunluk Değerlendirmesi (Suitability Assessment)

### Uygun Uygulamalar (Suitable Applications)

| Uygulama | Kurutma T [°C] | Neden Uygun | Tipik SMER [kg/kWh] |
|----------|:--------------:|-------------|:--------------------:|
| Kereste kurutma (timber) | 40-65 | Düşük T, uzun süre tolere edilir, kalite hassas | 2.5-3.5 |
| Tıbbi bitkiler / baharatlar | 35-55 | Aroma korunması, düşük T zorunlu | 2.0-3.0 |
| Meyve / sebze (dilim) | 40-60 | Renk ve vitamin korunması | 2.0-3.0 |
| Deniz ürünleri (balık, karides) | 35-50 | Düşük T zorunlu, hijyen kontrolü | 1.8-2.8 |
| Tekstil kurutma | 50-70 | Orta T, kapalı ortam avantajı | 2.0-2.8 |
| Arıtma çamuru (sludge) | 50-75 | Koku kontrolü (kapalı döngü), uzun süre | 1.5-2.5 |
| İlaç hammaddeleri | 30-50 | Düşük T zorunlu, kontrollü ortam | 2.0-3.5 |
| Biyomalzeme / enzimler | 30-45 | Çok düşük T zorunlu, denaturasyon riski | 2.5-4.0 |

### Uygun Olmayan Uygulamalar (Unsuitable Applications)

| Uygulama | Kurutma T [°C] | Neden Uygun Değil | Alternatif |
|----------|:--------------:|-------------------|------------|
| Yüksek sıcaklık kurutma (>80°C) | >80 | Soğutucu akışkan sınırı, düşük COP | Egzoz ısı geri kazanımı |
| Çok yüksek kapasite (>500 kg su/saat) | Herhangi | HP boyutu ve maliyeti aşırı artar | Hibrit sistem veya konvansiyonel + HR |
| Kirli/yapışkan egzoz havası | Herhangi | Evaporatör serpantin tıkanması | Filtre + egzoz HR |
| Patlayıcı ortam (ATEX) | Herhangi | Kompresör kıvılcım riski | ATEX uyumlu alternatifler |
| Hızlı kurutma gereken prosesler | Yüksek | HP düşük T nedeniyle yavaş | Konvektif + IR |
| Kalan ömür < 4 yıl olan kurutucu | Herhangi | Yatırım geri dönmez | Bakım optimizasyonu |
| Ucuz atık ısı kaynağı mevcut | Herhangi | Atık ısı ile kurutma daha ekonomik | Atık ısı entegrasyonu |

## Soğutucu Akışkan Seçimi (Refrigerant Selection)

Soğutucu akışkan seçimi, kurutma sıcaklığına, çevresel düzenlemelere ve sistem performansına göre yapılır.

### Soğutucu Akışkan Karşılaştırması

| Soğutucu Akışkan | GWP | ODP | T_cond_max [°C] | COP (tipik) | EU F-Gas Durumu | Tercih |
|------------------|:---:|:---:|:----------------:|:-----------:|:---------------:|--------|
| R134a | 1,430 | 0 | ~70 | 3.5-4.5 | Aşamalı azaltma | Mevcut sistemler |
| R407C | 1,774 | 0 | ~65 | 3.0-4.0 | Aşamalı azaltma | Mevcut sistemler |
| R410A | 2,088 | 0 | ~60 | 3.3-4.2 | Aşamalı azaltma | Düşük T uygulamaları |
| R290 (propan) | 3 | 0 | ~70 | 3.5-4.5 | Tercih ediliyor | Yeni yatırımlar (yanıcı!) |
| R1234yf | <1 | 0 | ~65 | 3.2-4.0 | Tercih ediliyor | Yeni nesil OEM |
| R1234ze(E) | <1 | 0 | ~75 | 3.3-4.2 | Tercih ediliyor | Yeni yatırımlar (endüstriyel) |
| R744 (CO2) | 1 | 0 | ~90+ | 2.0-2.8 | En uyumlu | Yüksek T (transkritik) |
| R717 (amonyak) | 0 | 0 | ~80 | 3.5-4.5 | En uyumlu | Büyük endüstriyel (toksik!) |

### Seçim Kriterleri

- **Kurutma sıcaklığı < 65 °C:** R134a, R290, R1234ze(E) veya R1234yf tercih edilir. En yüksek COP bu aralıkta elde edilir.
- **Kurutma sıcaklığı 65-80 °C:** R1234ze(E), R717 (büyük sistemler) veya CO2 (R744) değerlendirilir. R134a sınırda çalışır.
- **Kurutma sıcaklığı > 80 °C:** Yalnızca CO2 (R744) transkritik çevrim ile mümkündür. COP düşüktür (2.0-2.5) ancak konvansiyonel sisteme göre hala avantajlıdır.
- **EU F-Gas Regulation (517/2014) uyumu:** GWP > 2,500 olan akışkanlar 2025'ten itibaren yasaklanmıştır. GWP > 750 olan akışkanlar aşamalı kısıtlama altındadır. **Yeni yatırımlarda düşük GWP akışkanlar (R290, R1234ze, R744) kesinlikle tercih edilmelidir.**

### Yeni Nesil Düşük GWP Seçenekleri

| Akışkan | GWP | Avantaj | Dezavantaj | Uygunluk |
|---------|:---:|---------|------------|----------|
| R290 (propan) | 3 | Yüksek COP, ucuz, doğal | Yanıcı (A3), güvenlik önlemi gerekli | En yaygın düşük GWP seçenek |
| R1234ze(E) | <1 | Düşük GWP, iyi COP, düşük yanıcılık (A2L) | R134a'dan pahalı, daha düşük kapasite | Endüstriyel tercih edilen |
| R744 (CO2) | 1 | Doğal, yüksek T mümkün, ucuz | Yüksek basınç (>100 bar), özel kompresör | Yüksek sıcaklık nişi |

## Uygulama Adımları (Implementation Steps)

### Aşama 1: Fizibilite ve Mühendislik (4-8 hafta)

1. **Kurutma profili analizi:** Mevcut kurutma sıcaklıklarını, sürelerini, ürün özelliklerini ve nem profillerini detaylı olarak belgele. En az 2 hafta sürekli veri topla. Kurutma eğrisi (drying curve) oluştur.
2. **Isı pompası uygunluk değerlendirmesi:** Kurutma sıcaklığının < 80 °C olduğunu doğrula. Ürünün uzun kurutma süresini tolere edip etmeyeceğini değerlendir. Tetikleyici koşulları kontrol et.
3. **Enerji denetimi:** Mevcut enerji tüketimini, SMER değerini ve egzoz koşullarını ölç. Referans (baseline) oluştur.
4. **Ekonomik fizibilite:** Retrofit maliyet tahmini, enerji tasarrufu hesabı, SPP ve TCO analizi yap. Enerji fiyat hassasiyet analizi ekle.

### Aşama 2: Tasarım ve Tedarik (6-12 hafta)

5. **Soğutucu akışkan seçimi:** Kurutma sıcaklığına göre uygun akışkanı belirle. GWP ve mevzuat uyumunu kontrol et.
6. **Isı pompası boyutlandırma:** Evaporatör ve kondensör kapasitelerini, kompresör gücünü hesapla. Part-load (kısmi yük) performansını değerlendir.
7. **Hava devir sistemi tasarımı:** Kapalı döngü veya yarı kapalı döngü konfigürasyonunu seç. Kanal, damper ve fan boyutlandırması yap.
8. **Kontrol sistemi tasarımı:** Sıcaklık, nem ve basınç kontrolü. VFD (Variable Frequency Drive) kompresör ve fan dahil.
9. **Ekipman tedariki:** Kompresör, evaporatör, kondensör, genleşme vanası, soğutucu akışkan boruları, kontrol paneli siparişi.

### Aşama 3: Montaj ve Devreye Alma (4-8 hafta)

10. **Mekanik montaj:** Isı pompası ünitesini, serpantinleri, soğutucu akışkan borularını ve kontrol panelini monte et.
11. **Kondensat yönetimi:** Evaporatörde yoğuşan suyun toplanması, drenajı ve gerekirse arıtılması.
12. **Soğutucu akışkan şarjı:** Sistemi vakumla, kaçak testi yap ve akışkanı doldur.
13. **Devreye alma:** Sistemi aşamalı olarak devreye al. COP, SMER, kurutma süresi ve ürün kalitesini ölç.

### Aşama 4: Optimizasyon ve İzleme (sürekli)

14. **Performans optimizasyonu:** İlk 1-3 ay boyunca farklı parametreleri test et. Kompresör hızı, hava debisi, evaporatör sıcaklığını optimize et.
15. **Bakım programı oluştur:** Soğutucu akışkan seviyesi, kompresör yağı, filtre ve serpantin temizliği periyotlarını belirle.
16. **Performans takibi:** Aylık SMER, COP ve enerji tüketimi raporları ile performans izle. Degradasyonu erken tespit et.

## Riskler ve Önlemler (Risks and Mitigation)

| Risk | Açıklama | Etki | Önlem |
|------|----------|------|-------|
| Uzun kurutma süresi | Düşük sıcaklık nedeniyle kurutma süresi %20-50 uzayabilir | Kapasite düşüşü | Kapasite planlamasında dikkate al; ek kurutucu kabini düşün; hibrit sistem değerlendir |
| Yüksek yatırım maliyeti | Konvansiyonel sisteme göre 2-4x daha pahalı | Nakit akışı baskısı | TCO analizini göster; teşvik/hibe programlarını araştır; kiralama/leasing seçenekleri |
| Sıcaklık sınırlaması | Mevcut akışkanlarla genellikle < 80 °C ile sınırlı | Uygulama alanı kısıtı | CO2 (R744) ile 90 °C'ye kadar çıkılabilir; >90 °C uygun değil |
| Soğutucu akışkan sızıntısı | Kaçak sistem performansını düşürür ve çevresel etki yaratır | COP düşüşü, maliyet | Düzenli kaçak kontrolü; otomatik algılama sistemi; düşük GWP akışkan seç |
| Evaporatör buzlanması (frosting) | T_evap < 0 °C ise evaporatörde buz oluşur | Verim düşüşü, kapasite azalması | Otomatik defrost çevrimi; sıcak gaz bypass; demand-based defrost kontrolü |
| Kompresör arızası | Kompresör arızalanırsa kurutma tamamen durur | Üretim kaybı | Yedek ısıtma sistemi (backup heater); düzenli bakım programı; vibrasyon izleme |
| F-Gas mevzuat değişiklikleri | Soğutucu akışkan yasakları yatırımı riske atabilir | Akışkan değişimi maliyeti | Yeni yatırımlarda düşük GWP akışkan seç; drop-in uyumlu sistem tasarla |
| Gürültü ve titreşim | Kompresör ve fanlar gürültü kaynağıdır | Çalışma ortamı etkisi | Ses yalıtımı; titreşim damperleri; sessiz çalışan scroll kompresör seçimi |
| Ölçek büyütme zorluğu | >500 kg su/saat için HP boyutu ve maliyeti hızla artar | Maliyet/fayda bozulması | Büyük kapasitelerde hibrit sistem (HP + konvansiyonel); modüler HP üniteleri |
| Elektrik altyapısı yetersizliği | Yüksek güçlü kompresör mevcut trafo kapasitesini aşabilir | Ek elektrik yatırımı | Ön fizibilite aşamasında elektrik altyapısını kontrol et |

### Kritik Başarı Faktörleri

1. **Doğru boyutlandırma:** Evaporatör ve kondensör kapasiteleri kurutma yüküne uygun olmalıdır. Aşırı boyutlandırma maliyet artışı, yetersiz boyutlandırma düşük COP demektir.
2. **VSD kompresör kullanımı:** Değişken hızlı kompresör kısmi yükte COP'u korur ve %10-20 ek tasarruf sağlar.
3. **Akıllı defrost kontrolü:** Zamanlayıcı yerine sensör bazlı (demand-based) defrost %5-10 enerji tasarrufu sağlar.
4. **Eğitimli operatör:** Personelin ısı pompası sistemi çalışma prensiplerini ve bakım gereksinimlerini bilmesi kritik önem taşır.

## İlgili Dosyalar

- Kurutucu exergy formülleri: `dryer/formulas.md`
- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Isı pompalı kurutucu ekipman bilgisi: `dryer/equipment/heat_pump_dryer.md`
- Egzoz ısı geri kazanımı: `dryer/solutions/exhaust_heat_recovery.md`
- Hava geri deviri: `dryer/solutions/air_recirculation.md`
- Mekanik ön su alma: `dryer/solutions/mechanical_dewatering.md`
- Fabrika atık ısı geri kazanımı: `factory/waste_heat_recovery.md`
- Fabrika çapraz ekipman fırsatları: `factory/cross_equipment.md`
- Psikrometrik hesaplar: `dryer/psychrometrics.md`

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014 — Chapter 17: Heat Pump Drying
- Chua, K.J., Chou, S.K., Ho, J.C., Hawlader, M.N.A., "Heat Pump Drying: Recent Developments and Future Trends," Drying Technology, Vol. 20, No. 8, 2002
- Colak, N. & Hepbasli, A., "A Review of Heat Pump Drying: Part 1 — Systems, Models, and Studies," Energy Conversion and Management, Vol. 50, 2009
- Perera, C.O. & Rahman, M.S., "Heat Pump Dehumidifier Drying of Food," Trends in Food Science & Technology, Vol. 8, 1997
- Minea, V., "Heat Pump-Assisted Drying: Recent Technological Advances and R&D Needs," Drying Technology, Vol. 31, 2013
- IEA Heat Pump Centre, "Heat Pump Drying — Application and Optimization," HPT Annex 52
- EU Best Available Techniques Reference Document (BREF) for Energy Efficiency, European Commission, 2009
- EN 14511, "Air Conditioners, Liquid Chilling Packages and Heat Pumps — Performance Testing"
- European Commission, EU F-Gas Regulation 517/2014 — Fluorinated Greenhouse Gases Regulation
- ASHRAE Handbook — HVAC Applications, Drying and Dehumidification Chapter
- Kudra, T. & Mujumdar, A.S., "Advanced Drying Technologies," 2nd Edition, CRC Press, 2009
