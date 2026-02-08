---
title: "Genel Üretim Prosesleri (General Manufacturing Processes)"
category: factory
equipment_type: factory
keywords: [üretim, manufacturing, çimento, cam, kağıt, şeker, exergy, BAT, BREF, endüstriyel proses]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/heating.md, factory/process/drying.md, factory/process/steam_generation.md]
use_when: ["Spesifik üretim prosesi exergy analizi yapılacakken", "Sektörel üretim BAT karşılaştırması gerektiğinde", "Çimento/cam/kağıt/şeker prosesi değerlendirilecekken"]
priority: medium
last_updated: 2026-02-08
---

# Genel Üretim Prosesleri (General Manufacturing Processes)

Bu dosya, ExergyLab'da sıklıkla karşılaşılan enerji-yoğun üretim sektörlerinin exergy profilini, BAT referanslarını ve ESI değerlendirme kurallarını içerir. Her alt-bölüm bağımsız bir sektörü kapsar.

---

## 1. Çimento Üretimi (Cement Manufacturing)

### 1.1 Proses Tanımı
Çimento üretimi, hammaddelerin (kireçtaşı, kil) yüksek sıcaklıkta (~1450 °C) sinterleştirilmesi (klinker) ve öğütülmesi sürecidir. Enerji yoğun: 3.0 – 5.5 GJ/ton klinker.

**Proses aşamaları ve enerji dağılımı:**

```
Hammadde (kireçtaşı + kil + demir cevheri + alçıtaşı)
├── Kırma ve öğütme (hammadde hazırlama)
│   └── Elektrik: 25-35 kWh/ton hammadde
│   └── Exergy yıkımı: Düşük (~%2-3 toplam)
│
├── Ön ısıtma (cyclone preheater, 4-6 kademe)
│   └── Sıcaklık: 100 °C → 800-900 °C
│   └── Baca gazı ile karşı akımlı ısı değişimi
│   └── Exergy verimi: %30-45 (sıcaklık farkı büyük)
│
├── Ön kalsinasyon (precalciner, opsiyonel)
│   └── Kalsinasyon reaksiyonunun %60-95'i burada
│   └── Atık yakıt kullanımına uygun (düşük kalite yakıt)
│   └── Sıcaklık: 850-900 °C
│
├── Döner fırın (rotary kiln)
│   └── Sıcaklık: 1350-1450 °C (alev bölgesi ~2000 °C)
│   └── Termal enerji: 3.000-3.400 MJ/ton klinker (BAT)
│   └── BASKIN exergy yıkımı: Yanma irreversibilitesi (%35-45)
│   └── Radyasyon kaybı: %8-15
│
├── Klinker soğutma (grate cooler)
│   └── 1400 °C → 100-200 °C
│   └── Sekonder hava: fırına geri (600-800 °C)
│   └── Tersiyer hava: kalsinatöre geri (800-900 °C)
│   └── Atık ısı: ORC/Kalina potansiyeli (250-400 °C)
│
└── Çimento öğütme (ball mill veya VRM)
    └── Klinker + alçıtaşı + SCM → çimento
    └── Elektrik: 30-50 kWh/ton çimento
    └── VRM: %20-30 daha verimli
```

**Exergy yıkım dağılımı (tipik kuru proses):**

| Proses Adımı | Exergy Yıkımı Payı | Sıcaklık Aralığı | Tersinmezlik Kaynağı |
|-------------|---------------------|-------------------|----------------------|
| Yanma (döner fırın) | %35-45 | 1400-2000 °C | Kimyasal → termal dönüşüm |
| Radyasyon/konveksiyon | %10-15 | Fırın yüzeyi | Yüksek T → çevre |
| Ön ısıtıcı (cyclone) | %8-12 | 100-900 °C | Sonlu ΔT ısı transferi |
| Klinker soğutma | %8-10 | 200-1400 °C | Sonlu ΔT + atık ısı |
| Öğütme (elektrik) | %5-8 | Ortam | Mekanik → termal |
| Baca gazı (egzoz) | %10-15 | 250-400 °C | Termal exergy kaybı |
| Diğer (kondens, toz) | %5-8 | Çeşitli | Kütle kaybı + ısı |

### 1.2 Minimum Exergy
Klinker oluşumu için teorik minimum:
$$ex_{min,klinker} ≈ 1.700 \text{ kJ/kg\_klinker (tahmini)}$$

Bu değer, CaO oluşumu kalsinasyon reaksiyonundan gelir:
CaCO₃ → Cite + CO₂, ΔH ≈ 1.780 kJ/kg CaCO₃

> **Not:** Exergy minimum hesabı, reaksiyon Gibbs serbest enerjisine dayalıdır ve koşullara göre değişir. Verilen değer tahminidir, doğrulama gerekli.

### 1.2b Kalsinasyon Exergy Türetimi (Gibbs Serbest Enerjisi)

Çimento üretiminin temel reaksiyonu kireçtaşı kalsinasyonudur:

$$CaCO_3 \rightarrow CaO + CO_2$$

**Termodinamik veriler (298.15 K, 1 atm):**

| Bileşen | ΔH°_f (kJ/mol) | S° (J/(mol·K)) | ΔG°_f (kJ/mol) |
|---------|----------------|-----------------|------------------|
| CaCO₃ | −1206.9 | 92.9 | −1128.8 |
| CaO | −635.1 | 39.7 | −604.0 |
| CO₂ | −393.5 | 213.7 | −394.4 |

**Reaksiyon Gibbs serbest enerji değişimi:**
$$\Delta G°_{rxn} = [\Delta G°_f(CaO) + \Delta G°_f(CO_2)] - \Delta G°_f(CaCO_3)$$
$$= [(-604.0) + (-394.4)] - (-1128.8) = +130.4 \text{ kJ/mol}$$

**Reaksiyon entalpisi:**
$$\Delta H°_{rxn} = [(-635.1) + (-393.5)] - (-1206.9) = +178.3 \text{ kJ/mol}$$

**Minimum exergy gereksinimi:**
$$ex_{min,kalsinasyon} = \Delta G°_{rxn} = 130.4 \text{ kJ/mol CaCO_3}$$

Klinker başına (CaCO₃ → CaO dönüşüm oranı %65):
$$ex_{min,klinker} = 130.4 / 100.09 \times 0.65 \times 1000 = 846 \text{ kJ/kg klinker}$$

Toplam minimum exergy (kalsinasyon + sinterleşme + öğütme):
$$ex_{min,çimento} ≈ 1.500 - 1.800 \text{ kJ/kg klinker}$$

> **Not:** Bu hesap basitleştirilmiştir. Gerçek minimum, klinkerin mineralojik fazlarının (C₃S, C₂S, C₃A, C₄AF) oluşum enerjilerini de içerir.

**Engine değeri karşılaştırması:** bat_references.py → general_manufacturing/cement: exergy_efficiency_pct = 28%, specific_exergy = 0.85 kWh/kg = 3.060 kJ/kg. Literatür: BAT termal enerji 3.000-3.400 MJ/ton klinker.

**Kaynak:** Szargut et al. (1988), Bölüm 7 — Kimyasal proses exergy'si; CLM BREF 2013, s. 18-45.

### 1.3 BAT Referansı — EU BREF CLM 2013

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Klinker termal enerji | 3.000 – 3.400 MJ/ton klinker | Kuru proses, ön kalsinasyonlu |
| Elektrik tüketimi | 90 – 110 kWh/ton çimento | Öğütme dahil |
| CO₂ emisyonu | 0.55 – 0.70 t CO₂/t çimento | BAT-AEL |

> **BREF sayfa referansları:** CLM BREF 2013 — BAT 1-3 (Genel, s. 86-95), BAT 4-6 (Klinker üretimi, s. 96-108), BAT 8 (Atık yakıt, s. 109-112), BAT 15-20 (Emisyon, s. 113-115).

### 1.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %15 – %30 | %25-30 |
| ESI | 0.10 – 0.25 | 0.20-0.25 |
| Ana kayıp | Yanma (%40) + radyasyon/soğutma (%25) | — |

### 1.5 İyileştirme Stratejileri
1. **Klinker soğutma ısı geri kazanımı:** %5-10 yakıt tasarrufu (1-3 yıl ROI)
2. **Ön kalsinasyon ile atık yakıt:** %15-30 birincil yakıt azaltma (2-5 yıl ROI)
3. **Atık ısı elektrik üretimi (ORC/Kalina):** 10-30 kWh/ton klinker (3-6 yıl ROI)
4. **Yüksek verimli öğütücüler (VRM):** %20-30 elektrik tasarrufu (2-4 yıl ROI)
5. **Çimentoda SCM kullanımı:** Klinker oranı azaltma → exergy/ton çimento düşer

### 1.6 Yorumlama Kuralı
```
EĞER çimento tesisi:
  → ESI > 0.20 "Çimento için iyi — modern kuru proses"
  → ESI 0.12-0.20 "Çimento için orta — iyileştirme potansiyeli var"
  → ESI < 0.12 "Çimento için düşük — yaş proses veya eski teknoloji"
```

### 1.7 Çözümlü Örnek: Çimento Fırını Boşluk Analizi

**Problem:** Kuru prosesli çimento fabrikası. Klinker üretimi: 3.000 ton/gün. Termal enerji tüketimi: 3.600 MJ/ton klinker. Doğal gaz + alternatif yakıt (%30).

```
Üretim hızı: 3000 ton/gün = 125 ton/h = 34.72 kg/s

Ex_min = 1700 kJ/kg klinker (tahmini — kalsinasyon + sinterleşme)
Ex_min_toplam = 34.72 × 1700 = 59.024 kW = 59.0 MW

BAT SEC = 3.200 MJ/ton klinker (BREF CLM 2013, BAT 3-4)
Ex_BAT = 34.72 × 3200 / 1 = 111.104 kW (enerji)
Ex_BAT = 111.104 × 1.05 = 116.7 MW (yakıt exergy, φ ≈ 1.05 karışım)

Gerçek tüketim:
SEC_actual = 3.600 MJ/ton klinker
Ex_actual = 34.72 × 3600 × 1.05 / 1 = 131.2 MW

Boşluk analizi:
ESI = 59.0 / 131.2 = 0.450 → Beklenenden yüksek!

DÜZELTME: Klinker ex_min = 1700 kJ/kg değeri çok yüksek olabilir.
Daha gerçekçi ex_min (yalnızca kalsinasyon Gibbs) = 846 kJ/kg:
ESI = (34.72 × 846) / (131.2 × 1000) = 29.37 MW / 131.2 MW = 0.224 → Derece C

BPR = Ex_BAT / Ex_actual = 116.7 / 131.2 = 0.890

ΔEx_total = 131.2 − 29.4 = 101.8 MW
ΔEx_imp = 131.2 − 116.7 = 14.5 MW
η_imp = 14.5 / 101.8 = 14.2%
```

**Yorumlama:**
- **ESI = 0.224 (Derece C):** Çimento sektörü için tipik — kuru proses, modern tesis
- **BPR = 0.890:** BAT'a çok yakın — bu tesis iyi yönetiliyor
- **η_imp = %14.2:** İyileştirilebilir boşluk küçük — BAT'a yakınlık yüksek
- **Öncelikli aksiyon:** Alternatif yakıt oranını %30→%50 artırma, klinker soğutma ısı geri kazanımı (ORC)
- **Ekonomik etki:** 14.5 MW × 0.04 €/kWh × 8.000 h = 4.640.000 €/yıl potansiyel

**Kaynak:** CLM BREF 2013, BAT Conclusions, s. 86-115.

---

## 2. Cam Üretimi (Glass Manufacturing)

### 2.1 Proses Tanımı
Cam üretimi, silika (SiO₂) ve diğer hammaddelerin yüksek sıcaklıkta (~1500-1600 °C) eritilmesi, şekillendirilmesi ve tavlanması sürecidir.

**Cam tipleri ve enerji profilleri:**

| Cam Tipi | Eritme T (°C) | SEC (MJ/ton) | Üretim Payı | Fırın Tipi |
|----------|--------------|--------------|-------------|------------|
| Float cam (düz cam) | 1550-1600 | 5.000-7.000 | %35 | Rejeneratif |
| Şişe/ambalaj camı | 1500-1550 | 3.500-5.500 | %45 | Rejeneratif/oxy-fuel |
| Cam elyaf | 1250-1400 | 4.000-8.000 | %10 | Elektrik/gaz hibrit |
| Özel cam (borosilikat) | 1600-1700 | 6.000-10.000 | %5 | Oxy-fuel |
| Cam yünü (izolasyon) | 1300-1500 | 5.000-9.000 | %5 | Kubbe fırın |

**Fırın tipi ve exergy etkileri:**

| Fırın Teknolojisi | Termal Verim | Exergy Verimi | Avantaj | Dezavantaj |
|-------------------|-------------|---------------|---------|------------|
| Rejeneratif (end-fired) | %45-55 | %18-25 | Yüksek verim, büyük kapasite | Yüksek yatırım, NOx |
| Rejeneratif (cross-fired) | %40-50 | %15-22 | İyi kalite kontrol | Biraz düşük verim |
| Rekuperatif | %30-40 | %12-18 | Düşük yatırım, esnek | Düşük ısı geri kazanımı |
| Oxy-fuel | %50-65 | %20-28 | Düşük NOx, kompakt | O₂ üretim maliyeti |
| Elektrik | %70-85 | %30-40 | Çok yüksek verim | Sınırlı kapasite, maliyet |
| Hibrit (gaz + elektrik) | %50-60 | %22-30 | Esneklik | Karmaşık kontrol |

### 2.2 Minimum Exergy
Cam eritme minimum exergy (teorik):
$$ex_{min,cam} ≈ 2.500 - 3.000 \text{ kJ/kg cam (tahmini, doğrulama gerekli)}$$

### 2.2b Cam Eritme Termodinamiği

Cam eritme prosesinin exergy analizi, silika ve diğer oksitlerin eritme ve vitrifikasyon enerjisini içerir:

**Temel reaksiyon (soda-kireç cam):**
SiO₂ + Na₂CO₃ + CaCO₃ → Na₂O·CaO·6SiO₂ + CO₂

**Enerji bileşenleri:**

| Bileşen | Enerji (kJ/kg cam) | Exergy (kJ/kg cam) | Pay |
|---------|-------------------|---------------------|-----|
| Kimyasal reaksiyonlar | 500-600 | 450-550 | %15-20 |
| Eritme entalpisi (1500 °C) | 1.200-1.500 | 900-1.100 | %35-40 |
| Fırın duvar/radyasyon kaybı | 1.000-2.000 | 800-1.600 | %30-35 |
| Egzoz gazı kaybı | 500-1.500 | 300-900 | %10-20 |
| Soğutma kaybı | 200-500 | 100-300 | %5-10 |

**Minimum exergy (teorik):**
$$ex_{min,cam} = \Delta G_{reaksiyon} + ex_{ısıtma,1500°C}$$
$$≈ 500 + (h_{1500} - h_0) - T_0 \times (s_{1500} - s_0) ≈ 2.500 - 3.000 \text{ kJ/kg}$$

### 2.3 BAT Referansı — EU BREF GLS 2012

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Eritme enerjisi (float cam) | 5.000 – 6.500 MJ/ton cam | Rejeneratif fırın |
| Eritme enerjisi (şişe camı) | 3.500 – 5.000 MJ/ton cam | Oxy-fuel veya rejeneratif |
| Elektrik tüketimi | 100 – 200 kWh/ton cam | İşleme dahil |

> **BREF sayfa referansları:** GLS BREF 2012 — BAT 1-5 (Genel, s. 170-178), BAT 8-12 (Eritme enerjisi, s. 180-210), BAT 15-18 (Emisyon, s. 215-230).

### 2.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %10 – %25 | %20-25 |
| ESI | 0.08 – 0.20 | 0.15-0.20 |
| Ana kayıp | Yanma (%35) + fırın duvarı/radyasyon (%30) + egzoz (%15) | — |

### 2.5 İyileştirme Stratejileri
1. **Rejeneratif/rekuperatif fırın:** %15-25 yakıt tasarrufu (5-10 yıl ROI)
2. **Oxy-fuel yakma:** %10-20 yakıt tasarrufu + emisyon azaltma (5-8 yıl ROI)
3. **Cullet (kırık cam) oranı artırma:** Her %10 cullet ≈ %2.5 enerji tasarrufu
4. **Atık ısı geri kazanımı (batch preheating):** %5-15 tasarruf (3-5 yıl ROI)
5. **Elektrik boosting:** Hibrit eritme, kısmi elektrikleştirme (3-6 yıl ROI)

### 2.6 Yorumlama Kuralı
```
EĞER cam tesisi:
  → ESI > 0.18 "Cam için iyi — modern rejeneratif veya oxy-fuel"
  → ESI 0.10-0.18 "Cam için orta"
  → ESI < 0.10 "Cam için düşük — fırın teknolojisi eski"
```

### 2.7 Çözümlü Örnek: Float Cam Fırını ESI Analizi

**Problem:** Float cam fırını. Üretim: 600 ton/gün. Rejeneratif fırın, doğal gaz. SEC = 5.800 MJ/ton cam.

```
Üretim: 600/24 = 25 ton/h = 6.944 kg/s

ex_min ≈ 2.700 kJ/kg (tahmini, doğrulama gerekli — Güvenilirlik D)
Ex_min = 6.944 × 2700 = 18.750 kW = 18.75 MW

Gerçek:
SEC = 5.800 MJ/ton → Q = 6.944 × 5800 = 40.275 kW = 40.3 MW
Ex_actual = 40.3 × 1.04 = 41.9 MW

BAT SEC = 5.200 MJ/ton (GLS BREF 2012, BAT 8-10)
Ex_BAT = 6.944 × 5200 × 1.04 = 37.5 MW

ESI = 18.75 / 41.9 = 0.448 → Derece B (!)
BPR = 37.5 / 41.9 = 0.895

UYARI: ex_min = 2.700 kJ/kg tahminidir (Güvenilirlik D).
       Gerçek ex_min daha düşük olabilir → ESI daha düşük çıkar.
```

**Yorum:**
- ESI tahmini 0.448 ama güvenilirlik düşük — tahmini ex_min aralığı geniş
- BPR = 0.895 → BAT'a çok yakın
- **Cullet etkisi:** Her %10 kırık cam artışı ≈ %2.5 enerji tasarrufu (eritme enerjisi azalır)
- **Oxy-fuel:** Azot ısıtma yükü kalkar → %10-20 yakıt tasarrufu

**Kaynak:** GLS BREF 2012, BAT 8-12, s. 180-210.

---

## 3. Kağıt Üretimi (Pulp and Paper Manufacturing)

### 3.1 Proses Tanımı
Kağıt üretimi, selüloz liflerinin hamur haline getirilmesi (pulping), temizlenmesi, kağıt makinesinde şekillendirilmesi ve kurutulması sürecidir. Buhar ve elektrik yoğun; CHP yaygın.

**Hamur türleri ve enerji karşılaştırması:**

| Hamur Türü | Elektrik (kWh/ton) | Termal (GJ/ton) | Verim (odun→hamur) | Exergy Notu |
|-----------|-------------------|------------------|---------------------|-------------|
| Mekanik (TMP) | 1.500-2.500 | 0-1 | %85-95 | Yüksek elektrik, düşük termal |
| Kimyasal (Kraft) | 600-800 | 3-5 | %40-50 | Siyah likör enerji geri kazanımı |
| Yarı-kimyasal (NSSC) | 800-1.200 | 1-3 | %65-80 | Orta enerji |
| Geri dönüşüm (DIP) | 300-600 | 0.5-2 | N/A | En düşük enerji |

**Kağıt makinesi su dengesi ve exergy etkisi:**

| Bölüm | Giriş Kuru Madde | Çıkış Kuru Madde | Su Uzaklaştırma Yöntemi | Exergy Maliyeti |
|-------|-----------------|------------------|-------------------------|-----------------|
| Wire (tel bölümü) | %0.5-1.0 | %18-22 | Yerçekimi + vakum | Çok düşük |
| Press (pres bölümü) | %18-22 | %40-50 | Mekanik sıkıştırma | Düşük (elektrik) |
| Dryer (kurutma) | %40-50 | %92-95 | Buhar ile termal | YÜKSEK (%60-70 toplam) |

> **Kritik nokta:** Pres bölümünde her %1 kuru madde artışı, kurutma bölümünde %4 buhar tasarrufu sağlar. Shoe press teknolojisi kuru maddeyi %42→%50 çıkarabilir → %32 kurutma tasarrufu.

### 3.2 Minimum Exergy
Kağıt kurutma baskın:
$$ex_{min,kağıt} ≈ 3.000 - 5.000 \text{ kJ/kg kuru kağıt (tahmini, ürüne bağlı)}$$

(Büyük kısmı su uzaklaştırma — bkz. `drying.md`)

### 3.2b Kraft Prosesi Enerji Akışı

Kraft kağıt hamuru + kağıt üretimi, entegre bir enerji sistemdir:

```
Hammadde (odun)
├── Pulping (hamur hazırlama)
│   ├── Mekanik: 1.000-2.500 kWh_el/ton (yüksek enerji, düşük kimya)
│   └── Kimyasal (Kraft): 600-800 kWh_el/ton + 3-5 GJ_termal/ton
│       └── Siyah likör → Geri kazanım kazanı (recovery boiler)
│           └── 10-15 GJ/ton hamur (yakıt değeri)
│           └── Buhar üretimi: 3-5 ton buhar/ton hamur
│
├── Kağıt makinesi
│   ├── Forming (tel bölümü): Düşük enerji
│   ├── Pressing (pres bölümü): 50-100 kWh_el/ton
│   │   └── Shoe press: Kuru madde %42→%50 (her %1 = %4 kurutma tasarrufu)
│   └── Drying (kurutma bölümü): 2-4 GJ_termal/ton kağıt (BASKIN!)
│       └── Silindir kurutma: 4-10 ton buhar/ton kağıt
│       └── Hood egzoz: 80-120 °C (geri kazanım potansiyeli)
│
└── CHP (standart Kraft tesiste)
    └── Geri kazanım kazanı + karşı basınç türbini
    └── Proses buharı: 6-15 bar
    └── Elektrik: 100-400 kWh/ton kağıt (öz tüketim)
```

### 3.3 BAT Referansı — EU BREF PP 2015

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Toplam enerji (entegre tesis) | 10 – 20 GJ/ton kağıt | Ürüne bağlı |
| Buhar tüketimi | 4 – 10 ton buhar/ton kağıt | Kurutma baskın |
| Elektrik tüketimi | 400 – 800 kWh/ton kağıt | Öğütme + makineler |
| CHP kullanımı | Yaygın (genellikle buhar türbini) | BAT olarak tanımlı |

> **BREF sayfa referansları:** PP BREF 2015 — BAT 1-10 (Genel, s. 440-460), BAT 28-35 (Kağıt makinesi enerji, s. 460-490), BAT 40-45 (CHP, s. 500-510).

### 3.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %15 – %30 | %25-30 |
| ESI | 0.12 – 0.28 | 0.22-0.28 |
| Ana kayıp | Kurutma (%40) + hamur hazırlama (%20) + kazan (%20) | — |

### 3.5 İyileştirme Stratejileri
1. **Mekanik ön su alma (pres verim artırma):** %10-20 buhar tasarrufu (2-4 yıl ROI)
2. **Buhar ve kondens geri dönüşü optimizasyonu:** %5-15 buhar (1-2 yıl ROI)
3. **CHP optimizasyonu (buhar türbini):** %5-10 birincil enerji (3-5 yıl ROI)
4. **Pinch analizi ile ısı entegrasyonu:** %10-25 termal enerji (2-5 yıl ROI)
5. **Hood egzoz ısı geri kazanımı:** %5-12 kurutma enerjisi (2-3 yıl ROI)

### 3.6 Yorumlama Kuralı
```
EĞER kağıt tesisi:
  → ESI > 0.25 "Kağıt için iyi — entegre ve CHP'li tesis"
  → ESI 0.15-0.25 "Kağıt için orta — ısı entegrasyon fırsatları var"
  → ESI < 0.15 "Kağıt için düşük — kurutma ve CHP incele"
```

### 3.7 Çözümlü Örnek: Kraft Kağıt Tesisi ESI Analizi

**Problem:** Entegre Kraft kağıt tesisi. Üretim: 1.000 ton kağıt/gün. Toplam enerji: 16 GJ/ton kağıt. CHP (geri kazanım kazanı + buhar türbini) mevcut.

```
Üretim: 1000/24 = 41.67 ton/h = 11.57 kg/s

ex_min ≈ 4.000 kJ/kg kağıt (tahmini — kurutma baskın)
Ex_min = 11.57 × 4000 = 46.3 MW

Gerçek tüketim:
SEC = 16 GJ/ton = 16.000 kJ/kg
Q_toplam = 11.57 × 16000 = 185.1 MW

Yakıt karışımı: %60 siyah likör (φ ≈ 1.10) + %40 doğal gaz (φ = 1.04)
φ_ort ≈ 1.076
Ex_actual = 185.1 × 1.076 = 199.2 MW

BAT SEC = 12 GJ/ton (PP BREF 2015, BAT 28-32, iyi entegre tesis)
Ex_BAT = 11.57 × 12000 × 1.076 = 149.4 MW

ESI = 46.3 / 199.2 = 0.232 → Derece C
BPR = 149.4 / 199.2 = 0.750

ΔEx_imp = 199.2 − 149.4 = 49.8 MW
Ekonomik etki: 49.8 MW × 0.035 €/kWh × 8000 h = 13.9 M€/yıl
```

**Yorum:**
- ESI = 0.232 → Derece C, kağıt için orta
- BPR = 0.750 → BAT'tan %25 uzakta — iyileştirme potansiyeli var
- **Öncelik:** Shoe press (mekanik ön su alma), hood ısı geri kazanımı, CHP optimizasyonu
- **Siyah likör avantajı:** Kraft tesisler yakıtın büyük kısmını kendi üretir → düşük karbon ayak izi

**Kaynak:** PP BREF 2015, BAT 28-35, s. 460-490.

---

## 4. Şeker Üretimi (Sugar Manufacturing)

### 4.1 Proses Tanımı
Şeker üretimi, şeker pancarı veya kamışından şeker kristallerinin çıkarılması sürecidir. Buhar yoğun: difüzyon, evaporasyon (çok kademeli), kristalizasyon, kurutma.

**Pancar vs. kamış karşılaştırması:**

| Parametre | Şeker Pancarı | Şeker Kamışı |
|-----------|--------------|--------------|
| Şeker içeriği | %15-18 | %10-14 |
| Termal enerji (GJ/ton şeker) | 8-14 | 6-12 |
| Biyokütle yakıt | Pancar posası (%30-40 ikame) | Bagasse (%80-100 ikame) |
| CHP potansiyeli | Orta | Yüksek (bagasse fazlası) |
| Kampanya süresi | 80-120 gün/yıl | 150-250 gün/yıl |
| Exergy verimi (tipik) | %12-22 | %15-25 |
| CO₂ profili | Orta (doğal gaz bağımlı) | Düşük (bagasse baskın) |

**Evaporasyon kademelerinin exergy etkisi:**

| Kademe Sayısı | Buhar Tüketimi (ton/ton şeker) | Göreceli Enerji | Yatırım |
|--------------|-------------------------------|-----------------|---------|
| 3 kademe | 3.0-4.0 | %100 (referans) | Düşük |
| 4 kademe | 2.0-3.0 | %75-80 | Orta |
| 5 kademe | 1.5-2.5 | %55-65 | Orta-yüksek |
| 6 kademe | 1.2-2.0 | %45-55 | Yüksek |
| 5 kademe + MVR | 0.8-1.5 | %30-40 | Çok yüksek |

> **MVR (Mechanical Vapour Recompression):** Buharlaştırılan suyun buharını mekanik olarak sıkıştırarak yeniden ısıtma kaynağı olarak kullanır. Elektrik tüketir ama buhar tüketimini dramatik azaltır. Exergy perspektifinden optimal: yüksek kaliteli enerji (elektrik) kullanarak düşük kaliteli enerji (düşük basınç buharı) ihtiyacını azaltır.

### 4.2 Minimum Exergy
Evaporasyon baskın:
$$ex_{min,şeker} ≈ 3.000 - 6.000 \text{ kJ/kg şeker (tahmini, hammaddeye bağlı)}$$

### 4.2b Şeker Pancarı Proses Zinciri

```
Pancar Girişi (15-18% şeker)
├── Yıkama ve dilimleme
│   └── Elektrik: 10-20 kWh/ton pancar
│
├── Difüzyon (70-75 °C)
│   └── Buhar: 0.1-0.2 ton/ton pancar
│   └── Düşük T ısıtma → exergy verimi düşük
│
├── Arıtma (kireçleme + karbonatasyonda)
│   └── CaO + CO₂ kullanımı
│   └── Buhar: 0.05-0.1 ton/ton pancar
│
├── Evaporasyon (5 kademe tipik)
│   └── BASKIN enerji tüketimi: 1.5-3.0 ton buhar/ton pancar
│   └── 5 kademe: her kademe öncekinin buharını kullanır
│   └── MVR: buhar tüketimini %30-50 azaltır
│
├── Kristalizasyon
│   └── Vakum altında buharlaştırma
│   └── Düşük enerji
│
└── Kurutma (kristal şeker)
    └── 0.1-0.3 ton buhar/ton şeker
    └── Akışkan yataklı tipik

Toplam: 8-14 GJ/ton şeker (pancar)
CHP: Standart (pancar posası yakacak + doğal gaz)
```

### 4.3 BAT Referansı — EU BREF FDM 2019

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Termal enerji (pancar) | 8 – 14 GJ/ton şeker | Çok kademeli evaporasyon |
| Elektrik | 100 – 200 kWh/ton şeker | CHP ile kendi üretimi |
| CHP kullanımı | Standart (buhar türbini) | BAT olarak tanımlı |

> **BREF sayfa referansları:** FDM BREF 2019 — BAT 1-5 (Genel enerji, s. 220-240), BAT 12-15 (Evaporasyon/kurutma, s. 285-320), BAT 25-30 (Soğutma, s. 350-380).

### 4.4 Exergy Profili

| Parametre | Tipik Aralık | BAT |
|-----------|-------------|-----|
| Termal exergy verimi | %12 – %25 | %20-25 |
| ESI | 0.10 – 0.22 | 0.18-0.22 |
| Ana kayıp | Evaporasyon (%35) + kazan (%30) + kurutma (%15) | — |

### 4.5 İyileştirme Stratejileri
1. **Çok kademeli evaporasyon (5+ kademe):** %15-30 buhar tasarrufu (3-5 yıl ROI)
2. **Termal buhar sıkıştırma (MVR/TVR):** %20-40 buhar tasarrufu (3-6 yıl ROI)
3. **Pinch analizi:** %10-25 termal enerji (2-4 yıl ROI)
4. **CHP optimizasyonu:** %5-15 birincil enerji (3-5 yıl ROI)
5. **Biyokütle yakma (pancar posası):** %30-50 dış yakıt azaltma (2-4 yıl ROI)

### 4.6 Yorumlama Kuralı
```
EĞER şeker tesisi:
  → ESI > 0.20 "Şeker için iyi — çok kademeli ve CHP entegre"
  → ESI 0.12-0.20 "Şeker için orta — evaporasyon optimizasyonu gerekli"
  → ESI < 0.12 "Şeker için düşük — MVR ve pinch analizi değerlendir"
```

### 4.7 Çözümlü Örnek: Şeker Fabrikası ESI Analizi

**Problem:** Şeker pancarı fabrikası. Üretim: 1.200 ton şeker/gün. 5 kademeli evaporasyon. CHP (buhar türbini). Toplam SEC: 11 GJ/ton şeker.

```
Üretim: 1200/24 = 50 ton/h = 13.89 kg/s

ex_min ≈ 4.500 kJ/kg şeker (tahmini — evaporasyon baskın)
Ex_min = 13.89 × 4500 = 62.5 MW

Gerçek:
SEC = 11 GJ/ton = 11.000 kJ/kg
Q_toplam = 13.89 × 11000 = 152.8 MW
φ_ort ≈ 1.06 (pancar posası + doğal gaz karışımı)
Ex_actual = 152.8 × 1.06 = 162.0 MW

BAT SEC = 9 GJ/ton (FDM BREF 2019, iyi entegre tesis)
Ex_BAT = 13.89 × 9000 × 1.06 = 132.5 MW

ESI = 62.5 / 162.0 = 0.386 → Derece B (!)

UYARI: ex_min = 4500 kJ/kg tahmini çok yüksek olabilir.
Daha muhafazakar tahmin: ex_min ≈ 3500 kJ/kg:
ESI = (13.89 × 3500) / 162000 = 48.6 MW / 162.0 MW = 0.300 → Derece C

BPR = 132.5 / 162.0 = 0.818
```

**Yorum:**
- ESI = 0.30 (Derece C, muhafazakar) — şeker için iyi
- BPR = 0.818 → BAT'a yakın
- **Evaporasyon optimizasyonu:** 5→6 kademe veya MVR ile %15-25 buhar tasarrufu
- **Biyokütle avantajı:** Pancar posası yakma ile %30-50 dış yakıt ikamesi
- **CHP:** Buhar türbini ile 5-15 MWe elektrik üretimi mümkün

**Kaynak:** FDM BREF 2019, Ch. 12 — Sugar processing BAT.

---

## 5. Sektörler Arası Karşılaştırma

### 5.1 ESI Karşılaştırma Tablosu

| Sektör | Tipik ESI | BAT ESI | Ana Exergy Kaybı |
|--------|-----------|---------|-------------------|
| Çimento | 0.10 – 0.25 | 0.20-0.25 | Yanma + radyasyon |
| Cam | 0.08 – 0.20 | 0.15-0.20 | Yanma + fırın duvarı |
| Kağıt | 0.12 – 0.28 | 0.22-0.28 | Kurutma + hamur |
| Şeker | 0.10 – 0.22 | 0.18-0.22 | Evaporasyon + kazan |

### 5.2 Sıcaklık Profili Karşılaştırması

Her sektörün enerji ihtiyacı farklı sıcaklık seviyelerinde yoğunlaşır. Bu durum exergy kalitesini ve iyileştirme stratejisini belirler:

| Sektör | Proses Sıcaklığı (°C) | Carnot Faktörü (η_C) | Exergy Kalitesi | Atık Isı T (°C) |
|--------|----------------------|----------------------|-----------------|-----------------|
| Çimento | 1400-1500 | 0.83-0.85 | Çok yüksek | 250-400 |
| Cam | 1500-1600 | 0.84-0.86 | Çok yüksek | 300-500 |
| Kağıt | 100-180 | 0.19-0.37 | Düşük-orta | 80-120 |
| Şeker | 80-130 | 0.14-0.25 | Düşük | 60-90 |

> **Exergy perspektifi:** Çimento ve cam tesislerinde exergy yıkımı yüksek kaliteli enerji kullanımından kaynaklanır (yüksek T yanma). Kağıt ve şeker tesislerinde ise düşük kaliteli ısı (buhar) gereksinimi baskındır — bu nedenle farklı iyileştirme stratejileri gerekir.

### 5.3 Dekarbonizasyon Yol Haritası ve Exergy Etkisi

Her sektörün dekarbonizasyon yolu, exergy profilini köklü değiştirir:

| Sektör | Kısa Vade (0-5 yıl) | Orta Vade (5-15 yıl) | Uzun Vade (15+ yıl) |
|--------|---------------------|---------------------|---------------------|
| Çimento | Atık yakıt (%50+), SCM, ORC | Elektrik kalsinasyon, CCS | Doğrudan elektrik fırın, yeşil hidrojen |
| Cam | Oxy-fuel, cullet artışı, batch preheating | Elektrik boosting (%50+), H₂ yakıt | Tam elektrik eritme |
| Kağıt | CHP optimizasyonu, biyokütle, shoe press | Lignin bazlı biyoyakıt, MVR | Derin ısı entegrasyonu, elektrik kurutma |
| Şeker | 6+ kademe evaporasyon, MVR, bagasse CHP | Elektrik MVR, güneş termal | Tam elektrifik proses ısı |

### 5.4 Ortak İyileştirme Fırsatları

Tüm üretim sektörlerinde geçerli:
1. **Atık ısı geri kazanımı** — Baca gazı, soğutma, proses egzozu
2. **CHP entegrasyonu** — Buhar ihtiyacı olan her tesis
3. **Pinch analizi** — Karmaşık ısı akışları olan tesisler
4. **VFD uygulamaları** — Fan, pompa, kompresörlerde
5. **İzolasyon iyileştirmesi** — Yüksek sıcaklık ekipmanları
6. **Enerji yönetim sistemi (ISO 50001)** — Sistematik izleme ve hedefleme
7. **Dijital ikiz (digital twin)** — Gerçek zamanlı exergy izleme ve optimizasyon
8. **Isı pompası entegrasyonu** — Düşük T atık ısı değerlendirme (kağıt, şeker)

### 5.5 Ekonomik Değerlendirme Çerçevesi

Farklı sektörlerde exergy iyileştirmesinin ekonomik değeri farklıdır:

| Sektör | Enerji Maliyeti/Üretim Maliyeti | Tipik ΔEx_imp (MW) | Tasarruf Potansiyeli (€/yıl) |
|--------|-------------------------------|---------------------|-------------------------------|
| Çimento | %30-40 | 10-30 | 3-10 M€ |
| Cam | %15-25 | 5-15 | 1.5-5 M€ |
| Kağıt | %25-35 | 20-50 | 5-15 M€ |
| Şeker | %20-30 | 10-30 | 3-8 M€ |

> **Not:** Değerler orta ölçekli tesis (100-500 MW termal girdi) için tahminidir. Gerçek değerler tesis kapasitesi, enerji fiyatları ve yerel koşullara göre değişir.

---

## 6. Genel Yorumlama Rehberi (AI Kullanımı İçin)

### 6.1 Sektör Belirleme

```
EĞER sektör bilgisi var:
  → İlgili alt-bölümdeki ESI skalasını kullan
  → Sektörel BAT referansı ile karşılaştır

EĞER sektör bilinmiyor AMA üretim tesisi:
  → Genel ESI skalasını kullan (sustainability_index.md)
  → "Sektörel BAT karşılaştırması için sektör bilgisi gerekli" notu ekle
```

### 6.2 Çapraz Proses Değerlendirme

Bir üretim tesisinde birden fazla proses varsa:
1. Her prosesi ayrı ESI ile değerlendir
2. En düşük ESI'li prosesi öncelikli hedef olarak belirle
3. Exergy yıkım payına göre sırala
4. Prosesler arası entegrasyon fırsatlarını ara (pinch analizi)

**Çapraz proses entegrasyon örnekleri:**

| Kaynak Proses | Atık Enerji | Hedef Proses | Tasarruf |
|---------------|------------|--------------|---------|
| Çimento fırın egzozu (300-400 °C) | Termal exergy | ORC elektrik üretimi | 10-30 kWh/ton klinker |
| Cam fırın egzozu (400-500 °C) | Termal exergy | Batch preheating | %5-15 yakıt |
| Kağıt hood egzozu (80-120 °C) | Düşük T termal | Isı pompası ile ön ısıtma | %5-12 buhar |
| Şeker evaporasyon kondensi (60-80 °C) | Düşük T termal | Pancar yıkama suyu ısıtma | %3-5 buhar |

### 6.3 BAT Değer Güvenilirliği

| Sektör | BAT Kaynak | Güvenilirlik | Not |
|--------|-----------|-------------|-----|
| Çimento | BREF CLM 2013 | B — Güvenilir | Exergy dönüşümü tahmini |
| Cam | BREF GLS 2012 | B — Güvenilir | Exergy dönüşümü tahmini |
| Kağıt | BREF PP 2015 | B — Güvenilir | Geniş ürün yelpazesi |
| Şeker | BREF FDM 2019 | B — Güvenilir | Bölgesel farklar var |

---

## İlgili Dosyalar

- `factory/process/heating.md` — Isıtma prosesi (tüm sektörlerde mevcut)
- `factory/process/drying.md` — Kurutma prosesi (kağıt, gıda, çimento)
- `factory/process/steam_generation.md` — Buhar üretimi (tüm sektörlerde)
- `factory/process/chp.md` — CHP (kağıt, şeker, kimya)
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi
- `factory/sector_cement.md` — Çimento sektörü detayları
- `factory/sector_paper.md` — Kağıt sektörü detayları
- `factory/sector_food.md` — Gıda sektörü detayları

## Referanslar

1. European Commission, JRC (2013). *BAT Reference Document for the Production of Cement, Lime and Magnesium Oxide (CLM BREF)*.
2. European Commission, JRC (2012). *BAT Reference Document for the Manufacture of Glass (GLS BREF)*.
3. European Commission, JRC (2015). *BAT Reference Document for the Production of Pulp, Paper and Board (PP BREF)*.
4. European Commission, JRC (2019). *BAT Reference Document for the Food, Drink and Milk Industries (FDM BREF)*.
5. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths.
6. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier.
7. Szargut, J., Morris, D.R. & Steward, F.R. (1988). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*. Hemisphere.
8. Szargut, J., Morris, D.R. & Steward, F.R. (1988). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*. Hemisphere. Bölüm 7 — Kimyasal prosesler exergy hesabı.
9. Madlool, N.A. et al. (2011). "A critical review on energy use and savings in the cement industries." *Renewable and Sustainable Energy Reviews*, 15(4), 2042-2060.
10. Beerkens, R.G.C. (2004). "Analysis of advanced and innovative glass melting concepts." *Ceramic Engineering and Science Proceedings*, 25(1), 143-158.
11. Bajpai, P. (2018). *Biermann's Handbook of Pulp and Paper*. 3rd ed., Elsevier. — Kağıt üretimi enerji analizi.
12. Ensinas, A.V. et al. (2007). "Analysis of process steam demand reduction and electricity generation in sugar and ethanol production." *Energy Conversion and Management*, 48(11), 2978-2987.
