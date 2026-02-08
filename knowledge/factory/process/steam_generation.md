---
title: "Buhar Üretim Prosesi (Steam Generation Process)"
category: factory
equipment_type: factory
keywords: [buhar, steam, kazan, buhar üretimi, doymuş buhar, kızgın buhar, exergy, BAT, LCP BREF]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, factory/process/heating.md, factory/process/chp.md, boiler/benchmarks.md]
use_when: ["Buhar üretim prosesi exergy analizi yapılacakken", "Buhar sistemi performansı değerlendirilecekken", "Buhar BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Buhar Üretim Prosesi (Steam Generation Process)

---

## 1. Proses Tanımı

### Nedir?
Buhar üretim prosesi, yakıt enerjisini kullanarak suyu belirli basınç ve sıcaklıkta buhara dönüştürme işlemidir. Endüstriyel tesislerin en yaygın enerji taşıyıcı üretim prosesidir.

### Nerede Kullanılır?
- Proses ısıtma (kimya, gıda, tekstil, kağıt)
- Güç üretimi (buhar türbini çevrimleri)
- Sterilizasyon (gıda, ilaç, sağlık)
- Mekanik sürüş (buhar türbini ile pompa/kompresör)
- Isıtma (bina, sera)

### İlgili Ekipmanlar
- Ateş tüplü kazanlar (shell boilers): 0.5 – 25 ton/h
- Su borulu kazanlar (water-tube boilers): 10 – 500+ ton/h
- Atık ısı kazanları (HRSG): Türbin egzozu geri kazanımı
- Ekonomizer, süperısıtıcı, degazör, kondenstop
- Buhar dağıtım hatları, redüksiyon vanaları

### Tipik Ölçek
- Küçük: 0.5 – 5 ton/h buhar
- Orta: 5 – 50 ton/h buhar
- Büyük: 50 – 500+ ton/h buhar

### Buhar Sisteminin Bileşenleri

Bir buhar üretim sistemi sadece kazandan ibaret değildir. Tüm bileşenlerin exergy performansı toplam sistem verimini belirler:

| Bileşen | İşlev | Exergy Etkisi |
|---------|-------|---------------|
| Kazan (boiler) | Suyu buhara dönüştürme | Ana exergy dönüşüm noktası — yanma irreversibilitesi baskın |
| Ekonomizer | Baca gazı ile beslenme suyunu ön ısıtma | Baca gazı exergy kaybını %3-8 azaltır |
| Süperısıtıcı (superheater) | Doymuş buharı kızgın buhara yükseltme | Buhar exergy'sini %15-30 artırır |
| Hava ön ısıtıcı (air preheater) | Baca gazı ile yanma havasını ısıtma | Yanma verimi artırır, %2-4 yakıt tasarrufu |
| Degazör (deaerator) | Beslenme suyundan çözünmüş gazları uzaklaştırma | Korozyon önleme, ısı geri kazanım noktası |
| Kondenstop (steam trap) | Kondensi buhar hattından uzaklaştırma | Arızalı trap = %5-15 buhar kaybı |
| Blowdown sistemi | TDS kontrolü, çamur atımı | Flash steam geri kazanımı ile exergy kaybı azaltılır |
| Buhar dağıtım hattı | Buharı kullanım noktalarına taşıma | İzolasyon eksikliği = %3-8 ısı kaybı |
| Kondens geri dönüş hattı | Kondesi kazana geri getirme | Her %10 kondens artışı ≈ %1 yakıt tasarrufu |

### Buhar Kalitesi ve Exergy İlişkisi

Buharın termodinamik kalitesi (basınç, sıcaklık, kuruluk derecesi) doğrudan exergy içeriğini belirler:

```
Exergy hiyerarşisi (düşükten yükseğe):
  Islak buhar (x < 1.0) < Doymuş buhar (x = 1.0) < Kızgın buhar (T > T_sat)

Pratik etkisi:
  - Islak buhar: Türbin kanatlarında erozyon, düşük iş çıktısı
  - Doymuş buhar: Proses ısıtma için yeterli, faz değişimi sabit T'de
  - Kızgın buhar: Türbin sürüşü için gerekli, daha yüksek exergy
```

> **Önemli:** Doymuş buharın exergy'si aynı basınçtaki kızgın buhara göre daha düşüktür, ancak proses ısıtmada faz değişimi (latent heat) kullanılacaksa kızgınlığa gerek yoktur — gereksiz kızgınlık exergy israfıdır.

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

Buhar üretimi için minimum exergy, üretilen buharın spesifik exergy'sidir:

$$ex_{min} = (h_{steam} - h_0) - T_0 \times (s_{steam} - s_0)$$

| Sembol | Tanım | Birim |
|--------|-------|-------|
| h_steam | Buhar entalpisi | kJ/kg |
| h₀ | Ölü hal entalpisi (25 °C, 1 atm, sıvı su) | kJ/kg |
| s_steam | Buhar entropisi | kJ/(kg·K) |
| s₀ | Ölü hal entropisi | kJ/(kg·K) |
| T₀ | Çevre sıcaklığı | K (298.15 K) |

Ölü hal referans değerleri (25 °C, 101.325 kPa, sıvı su):
- h₀ = 104.9 kJ/kg
- s₀ = 0.3672 kJ/(kg·K)

### 2.1b Entalpi ve Entropi Bağlamı (Mollier Diyagramı)

Buhar exergy hesabı, buharın termodinamik özelliklerine (h, s) doğrudan bağlıdır. Bu değerler **buhar tabloları** (steam tables) veya **CoolProp** kütüphanesi ile elde edilir.

**Mollier (h-s) diyagramı üzerinde exergy:**
- Ölü hal noktası (25 °C, 1 atm, sıvı su): h₀ = 104.9, s₀ = 0.3672
- Buhar noktası (ör. 10 bar doymuş): h = 2778, s = 6.586
- Exergy = (h−h₀) − T₀×(s−s₀) = entalpi farkı − "entropi cezası"

**"Entropi cezası" kavramı:**
T₀×(s−s₀) terimi, prosesteki entropi artışının exergy maliyetini temsil eder. Bu terim ne kadar büyükse, ısının o kadar "düşük kaliteli" kısmı fazladır.

| Buhar Durumu | h−h₀ (kJ/kg) | T₀×(s−s₀) (kJ/kg) | Exergy (kJ/kg) | Exergy/Entalpi |
|-------------|------------|-------------------|----------------|----------------|
| 2 bar doymuş | 2602 | 2015 | 587 | %22.6 |
| 10 bar doymuş | 2673 | 1854 | 819 | %30.7 |
| 20 bar doymuş | 2694 | 1781 | 913 | %33.9 |
| 40 bar doymuş | 2696 | 1700 | 996 | %36.9 |
| 10 bar / 300 °C | 2947 | 2015 | 935 | %31.7 |
| 40 bar / 400 °C | 3109 | 1907 | 1202 | %38.7 |
| 100 bar / 540 °C | 3476 | 2068 | 1408 | %40.5 |

> **Gözlem:** Basınç arttıkça exergy/entalpi oranı yükselir — yüksek basınç buharı termodinamik olarak "daha değerli"dir.

**CoolProp kullanımı (Python):**
```python
from CoolProp.CoolProp import PropsSI
T_steam = 273.15 + 180  # 10 bar doymuş ≈ 180 °C
P_steam = 10e5  # 10 bar = 1 MPa
h = PropsSI('H', 'T', T_steam, 'P', P_steam, 'Water') / 1000  # kJ/kg
s = PropsSI('S', 'T', T_steam, 'P', P_steam, 'Water') / 1000  # kJ/(kg·K)
```

**Kaynak:** Kotas (1985), Tablo 2.1, s. 28-32; NIST/ASME Steam Properties (IAPWS-IF97).

### 2.1c Beslenme Suyu Exergy'si

Exergy hesabında beslenme suyunun exergy'si çıkarılmalıdır. Beslenme suyu sıcaklığı ne kadar yüksekse, net exergy artışı o kadar düşüktür (ancak kazan verimi artar):

| Beslenme Suyu T (°C) | h_bw (kJ/kg) | s_bw (kJ/(kg·K)) | ex_bw (kJ/kg) | Not |
|----------------------|--------------|-------------------|---------------|-----|
| 20 (şebeke suyu) | 84.0 | 0.296 | 0.3 | Çok düşük, ihmal edilebilir |
| 60 (düşük kondens) | 251.1 | 0.831 | 8.0 | Kısmi kondens geri dönüşü |
| 80 (tipik kondens) | 335.0 | 1.075 | 19.1 | Endüstriyel standart |
| 105 (degazör çıkışı) | 440.2 | 1.363 | 38.3 | İyi degazör uygulaması |
| 130 (HP degazör) | 546.4 | 1.634 | 63.5 | Yüksek basınç sistemler |
| 150 (ekonomizer çıkışı) | 632.2 | 1.842 | 87.4 | Ekonomizer ile ön ısıtma |

> **Pratik kural:** Beslenme suyu sıcaklığı 60 °C'nin altındaysa, kondens geri dönüş sistemi kontrol edilmeli. Kondens geri dönüşünün iyileştirilmesi hem enerji hem exergy tasarrufu sağlar.

### 2.2 Tipik Buhar Basınçlarında Minimum Exergy

| Basınç (bar) | Durum | T (°C) | h (kJ/kg) | s (kJ/(kg·K)) | ex_min (kJ/kg) |
|-------------|-------|--------|-----------|----------------|-----------------|
| 2 | Doymuş | 120.2 | 2.707 | 7.127 | 587 |
| 4 | Doymuş | 143.6 | 2.739 | 6.896 | 679 |
| 6 | Doymuş | 158.8 | 2.757 | 6.760 | 746 |
| 10 | Doymuş | 179.9 | 2.778 | 6.586 | 819 |
| 15 | Doymuş | 198.3 | 2.792 | 6.445 | 874 |
| 20 | Doymuş | 212.4 | 2.799 | 6.340 | 913 |
| 40 | Doymuş | 250.4 | 2.801 | 6.070 | 996 |
| 10 | Kızgın 300 °C | 300 | 3.052 | 7.124 | 935 |
| 40 | Kızgın 400 °C | 400 | 3.214 | 6.769 | 1.202 |

> **Anahtar Değer:** 10 bar doymuş buhar ≈ **819 kJ/kg** minimum exergy. Bu, proses boşluk analizinde en sık kullanılan referans noktasıdır.

### 2.2b Kızgın (Superheated) Buhar Exergy Tablosu

| Basınç (bar) | T (°C) | h (kJ/kg) | s (kJ/(kg·K)) | ex_min (kJ/kg) | Kullanım Alanı |
|-------------|--------|-----------|----------------|-----------------|----------------|
| 10 | 250 | 2.943 | 6.926 | 881 | Proses ısıtma |
| 10 | 300 | 3.052 | 7.124 | 935 | Kimya endüstrisi |
| 10 | 400 | 3.264 | 7.466 | 1040 | Türbin girişi (küçük) |
| 20 | 300 | 3.024 | 6.768 | 1010 | Yüksek basınç proses |
| 20 | 400 | 3.248 | 7.127 | 1130 | CHP buhar türbini |
| 40 | 400 | 3.214 | 6.769 | 1202 | Büyük ölçek CHP |
| 40 | 450 | 3.331 | 6.937 | 1268 | Kombine çevrim |
| 60 | 480 | 3.361 | 6.805 | 1338 | Enerji santrali |
| 100 | 540 | 3.476 | 6.823 | 1408 | Yüksek verimli santral |

> **Engine karşılaştırması:** bat_references.py → steam_generation/industrial_high = 0.28 kWh/kg buhar, exergy_efficiency_pct = 48%. Literatür aralığı: %38-55 (basınca bağlı).

### 2.3 Çözümlü Örnek

**Problem:** 8 ton/h, 10 bar doymuş buhar üreten kazan. Beslenme suyu 80 °C.

```
Buhar: h = 2778 kJ/kg, s = 6.586 kJ/(kg·K)
Ölü hal: h₀ = 104.9 kJ/kg, s₀ = 0.3672 kJ/(kg·K)
T₀ = 298.15 K

ex_buhar = (2778 − 104.9) − 298.15 × (6.586 − 0.3672)
         = 2673.1 − 1853.7
         = 819.4 kJ/kg

Beslenme suyu (80 °C): h_bw = 335 kJ/kg, s_bw = 1.075 kJ/(kg·K)
ex_bw = (335 − 104.9) − 298.15 × (1.075 − 0.3672) = 230.1 − 211.0 = 19.1 kJ/kg

Ex_min (net) = ṁ × (ex_buhar − ex_bw)
             = (8000/3600) × (819.4 − 19.1)
             = 2.222 × 800.3
             = 1778 kW
```

**Kaynak:** CoolProp steam tables; Kotas (1985), Tablo 2.1.

### 2.4 Çözümlü Örnek: Kızgın Buhar (40 bar / 400 °C)

**Problem:** 15 ton/h, 40 bar, 400 °C kızgın buhar üreten su borulu kazan. Beslenme suyu 105 °C. Doğal gaz, η_en = %91 (LHV).

```
Kızgın buhar (40 bar, 400 °C):
  h_steam = 3214 kJ/kg, s_steam = 6.769 kJ/(kg·K)

Ölü hal (25 °C, 1 atm):
  h₀ = 104.9 kJ/kg, s₀ = 0.3672 kJ/(kg·K)

ex_steam = (3214 − 104.9) − 298.15 × (6.769 − 0.3672)
         = 3109.1 − 1908.8
         = 1200.3 kJ/kg

Beslenme suyu (105 °C, basınçlı):
  h_bw = 440.2 kJ/kg, s_bw = 1.363 kJ/(kg·K)
  ex_bw = (440.2 − 104.9) − 298.15 × (1.363 − 0.3672)
        = 335.3 − 297.0
        = 38.3 kJ/kg

Ex_min (net) = ṁ × (ex_steam − ex_bw)
             = (15000/3600) × (1200.3 − 38.3)
             = 4.167 × 1162.0
             = 4841 kW

Q_yakıt = ṁ × (h_steam − h_bw) / η_en
        = 4.167 × (3214 − 440.2) / 0.91
        = 4.167 × 2773.8 / 0.91
        = 12.698 kW (LHV termal)

Ex_actual = Q_yakıt × φ = 12698 × 1.04 = 13206 kW

ESI = 4841 / 13206 = 0.367 → Derece B
η_ex = 4841 / 13206 = %36.7
BPR (BAT η_ex = %42): Ex_BAT = 4841/0.42 = 11526 kW
BPR = 11526 / 13206 = 0.873 → BAT yakınında
```

**Yorum:**
- ESI = 0.367 ile B derecesinde — yüksek basınç kızgın buhar için iyi
- BPR = 0.873 → BAT'a çok yakın, operasyonel iyileştirmeler önerilir
- Kızgın buharın yüksek exergy'si (1200 kJ/kg vs 819 kJ/kg doymuş), daha yüksek ESI sağlar
- **CHP potansiyeli:** 40 bar buhar → 10 bar kullanım → ~100 kJ/kg türbin işi çıkarılabilir

**Kaynak:** CoolProp steam tables; Tsatsaronis (2007).

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 SEC Aralıkları

| Alt-kategori | SEC (kJ_fuel/kg_buhar) | η_energy (LHV) | Not |
|-------------|------------------------|-----------------|-----|
| Doğal gaz kazanı (yoğuşmalı) | 2.700 – 2.900 | %92-98 | Latent ısı geri kazanımı |
| Doğal gaz kazanı (konvansiyonel) | 2.900 – 3.400 | %78-92 | Yaygın tesis tipi |
| Kömür kazanı | 3.200 – 4.000 | %70-86 | Kül ve kükürt etkisi |
| Atık ısı kazanı (HRSG) | 0 (atık ısı) | — | Yakıt tüketimi yok |

### 3.2 Exergy Verim Aralıkları

| Alt-kategori | η_ex Aralığı | Tipik η_ex |
|-------------|-------------|------------|
| Doğal gaz kazanı (en iyi) | %30 – %40 | %35 |
| Doğal gaz kazanı (tipik) | %25 – %35 | %30 |
| Kömür kazanı | %20 – %30 | %25 |
| HRSG | %45 – %65 | %55 |

### 3.3 Irreversibilite Payları

1. **Yanma:** %45 – %60 — Yakıtın kimyasal exergy'sinin yüksek sıcaklıkta termal exergy'ye dönüşümü
2. **Isı transferi (baca gazı → su/buhar):** %15 – %20 — Büyük ΔT (1200-1800 °C → 180-250 °C)
3. **Baca gazı çıkış kaybı:** %8 – %15 — Sıcak egzoz (120-250 °C)
4. **Blowdown kaybı:** %2 – %5 — TDS kontrolü için sıcak su atımı
5. **Yüzey ve radyasyon kaybı:** %2 – %4 — İzolasyon, sıcak noktalar
6. **Dağıtım hattı kaybı:** %3 – %8 — Kondenstop, izolasyon, kaçak

---

## 3b. Atık Isı Kazanı — HRSG (Heat Recovery Steam Generator)

### 3b.1 HRSG Genel Bakış

HRSG, gaz türbini veya endüstriyel proses egzoz gazından ısı geri kazanarak buhar üretir. Yakıt tüketimi olmadığı için exergy verimi kavramı farklıdır:

$$\eta_{ex,HRSG} = \frac{Ex_{buhar}}{Ex_{egzoz,giriş} - Ex_{egzoz,çıkış}}$$

| HRSG Tipi | Basınç Seviyesi | η_ex | Tipik Uygulama |
|-----------|-----------------|------|----------------|
| Tek basınçlı | 1 | %50-60 | Küçük GT-CHP |
| Çift basınçlı | 2 (HP+LP) | %60-70 | Orta ölçek CCGT |
| Üç basınçlı + reheat | 3 (HP+IP+LP) | %70-78 | Büyük CCGT (>100 MWe) |

### 3b.2 HRSG Exergy Analizi

Tipik HRSG exergy yıkım kaynakları:

| Kaynak | Pay | Açıklama |
|--------|-----|----------|
| Pinch point ΔT | %30-40 | Egzoz gazı − buhar sıcaklık farkı (tipik 8-15 °C) |
| Approach ΔT | %10-15 | Ekonomizer çıkış − doymuş sıvı sıcaklık farkı |
| Stack kayıp | %20-30 | HRSG çıkış gaz sıcaklığı (tipik 80-120 °C) |
| Basınç düşümü | %5-10 | Gaz tarafı ve su/buhar tarafı |

> **İyileştirme:** Pinch point'i 15 °C'den 8 °C'ye düşürmek HRSG exergy verimini %5-8 artırır, ancak ısı transfer yüzeyi (ve maliyet) %30-50 artar — exergoekonomik optimizasyon gerektirir.

### 3b.3 HRSG Çözümlü Örnek

**Problem:** 30 MW gaz türbini egzoz gazı (540 °C, 80 kg/s) ile tek basınçlı HRSG. Buhar: 20 bar doymuş, egzoz çıkış: 150 °C.

```
Egzoz giriş exergy (540 °C):
  T_ex_in = 813.15 K, cp_gas ≈ 1.1 kJ/(kg·K)
  ex_gas_in = cp × [(T − T₀) − T₀ × ln(T/T₀)]
            = 1.1 × [(813.15 − 298.15) − 298.15 × ln(813.15/298.15)]
            = 1.1 × [515.0 − 298.15 × 1.003]
            = 1.1 × [515.0 − 299.0]
            = 237.6 kJ/kg

Egzoz çıkış exergy (150 °C):
  T_ex_out = 423.15 K
  ex_gas_out = 1.1 × [(423.15 − 298.15) − 298.15 × ln(423.15/298.15)]
             = 1.1 × [125.0 − 298.15 × 0.349]
             = 1.1 × [125.0 − 104.1]
             = 23.0 kJ/kg

ΔEx_gas = 80 × (237.6 − 23.0) = 17168 kW

Buhar exergy (20 bar doymuş):
  ex_steam = 913 kJ/kg (tablodan)
  Buhar debisi ≈ ṁ_gas × cp × (T_in − T_out) / (h_steam − h_bw)
              ≈ 80 × 1.1 × 390 / (2799 − 440)
              ≈ 34320 / 2359
              ≈ 14.55 kg/s = 52.4 ton/h

Ex_steam = 14.55 × (913 − 38.3) = 12727 kW

η_ex,HRSG = 12727 / 17168 = %74.1 → İyi
```

**Yorum:** Tek basınçlı HRSG'de %74 exergy verimi, çift basınçlı ile %78-82'ye çıkarılabilir.

---

## 3c. Sektörel Buhar Uygulamaları

| Sektör | Tipik Basınç | Tipik Kapasite | Buhar Kullanımı | ESI Aralığı |
|--------|-------------|----------------|-----------------|-------------|
| Gıda & İçecek | 6-15 bar | 2-20 ton/h | Pişirme, pastörizasyon, CIP | 0.22-0.32 |
| Kağıt | 10-40 bar | 20-200 ton/h | Kurutma silindirleri, Yankee | 0.25-0.35 |
| Kimya | 10-60 bar | 5-100 ton/h | Reaktör ısıtma, distilasyon | 0.25-0.38 |
| Tekstil | 6-15 bar | 2-20 ton/h | Boyama, kurutma, ütüleme | 0.20-0.30 |
| İlaç | 3-10 bar | 0.5-5 ton/h | Sterilizasyon, kurutma | 0.18-0.28 |
| Rafineri | 20-100 bar | 50-500 ton/h | Proses ısıtma, türbin sürüşü | 0.30-0.42 |

### Karşı Basınç vs Kondens-Ekstraksiyon Türbini

Buhar proseslerinde CHP değerlendirmesi kritiktir:

| Özellik | Karşı Basınç Türbini | Kondens-Ekstraksiyon |
|---------|----------------------|----------------------|
| Elektrik üretimi | Düşük-orta (%10-25 η_el) | Orta-yüksek (%15-35 η_el) |
| Isı verimi | Çok yüksek (%55-70) | Orta (%30-55) |
| Esneklik | Düşük — ısı talebi belirler | Yüksek — ısı/elektrik ayarlanır |
| Exergy verimi | %25-40 | %35-50 |
| En iyi uygulama | Sabit buhar talebi olan tesisler | Değişken ısı/elektrik talebi |
| Yatırım | Daha düşük | Daha yüksek |

> **AI kuralı:** Buhar üretim kapasitesi > 5 ton/h ve sürekli ise, HER ZAMAN CHP değerlendirmesi öner. Detay için bkz. `process/chp.md`.

### Sektöre Özel Buhar Optimizasyonu İpuçları

**Gıda & İçecek:**
- CIP (Clean-in-Place) sistemleri için düşük basınç yeterli — 3-6 bar
- Pastörizasyon buharı geri kazanımı: rejeneratif ısı eşanjörü ile %60-80 ısı geri kazanımı
- Mevsimsel talep değişimi yüksek → modüler kazan yönetimi kritik

**Kağıt:**
- Yankee silindiri buharı: sabit ve yüksek debi, CHP için ideal profil
- Çok basınçlı buhar sistemi: HP (türbin) → MP (proses) → LP (ısıtma)
- Kondens geri dönüşü zor (kirlenme) → ayrı devre önerilir

**Kimya:**
- Reaktör ısıtma: hassas sıcaklık kontrolü, kızgın buhar tercih edilir
- Distilasyon: reboiler buharı sürekli, pinch analizi ile ısı entegrasyonu yüksek potansiyel
- Güvenlik: buhar basıncı/sıcaklık sınıflandırması ASME/PED uyumlu olmalı

**Rafineri:**
- Çok basınçlı buhar şebekesi: 100/40/10/3 bar seviyeleri
- Büyük ölçek CHP: buhar türbini + gaz türbini kombine çevrim
- Flare gazı geri kazanımı → tamamlayıcı yakıt olarak kazan beslemesi

---

## 4. BAT Referansı

### 4.1 EU BREF LCP 2017

| Parametre | BAT Aralığı | Koşul |
|-----------|------------|-------|
| Kazan enerji verimi (doğal gaz) | %92 – %96 (LHV) | > 50 MW_th |
| Kazan enerji verimi (kömür) | %86 – %92 (LHV) | > 50 MW_th |
| Baca gazı sıcaklığı (doğal gaz) | 80 – 120 °C | Ekonomizer ile |
| Baca gazı sıcaklığı (kömür) | 120 – 160 °C | Asit çiğ noktası sınırı |
| O₂ fazlası (doğal gaz) | %1 – %3 | Otomatik kontrol |
| CO emisyonu (doğal gaz) | < 100 mg/Nm³ | BAT-AEL |

### 4.2 BAT Exergy Verimi (ExergyLab Hesabı)

| Buhar Koşulu | BAT η_energy | BAT η_ex | ESI_BAT |
|-------------|-------------|---------|---------|
| 10 bar doymuş, doğal gaz | %95 | %35-38 | 0.35-0.38 |
| 10 bar doymuş, kömür | %90 | %28-32 | 0.28-0.32 |
| 40 bar kızgın, doğal gaz | %94 | %38-42 | 0.38-0.42 |
| HRSG (atık ısıdan) | — | %50-60 | 0.50-0.60 |

### 4.3 Alt-kategoriler

| Alt-kategori | BAT SEC | BAT η_ex | Not |
|-------------|---------|---------|-----|
| Yoğuşmalı + ekonomizer + hava ön ısıtıcı | 2.750 kJ/kg | %36-40 | En iyi ticari paket |
| Oksijen zenginleştirilmiş yanma | — | %40-45 | Gelişen teknik |
| Flameless combustion | — | %42-48 | Gelişen teknik, R&D |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Yanma (kimyasal → termal) | 45 – 60 | Düşük (termodinamik sınır) |
| 2 | Isı transferi (baca gazı → su/buhar) | 15 – 20 | Orta (yüzey artırma, CHP) |
| 3 | Baca gazı kaybı | 8 – 15 | Yüksek (ekonomizer, air preheater) |
| 4 | Dağıtım kayıpları | 3 – 8 | Yüksek (izolasyon, trap bakımı) |
| 5 | Blowdown | 2 – 5 | Orta (flash steam geri kazanım) |
| 6 | Yüzey/radyasyon kaybı | 2 – 4 | Yüksek (izolasyon onarımı) |

### 5.1 Yanma İrreversibilitesi Detayı

Yanma, buhar üretim prosesindeki en büyük exergy yıkım kaynağıdır ve termodinamik bir sınır oluşturur. Yakıtın kimyasal exergy'si (~1.04 × LHV doğal gaz için) yüksek sıcaklıktaki baca gazı termal exergy'sine dönüşürken büyük irreversibilite oluşur:

```
Yanma exergy verimi:
  η_ex,yanma = Ex_baca_gazı / Ex_yakıt

Tipik değerler:
  Doğal gaz, %3 fazla hava:     η_ex,yanma ≈ %65-70
  Doğal gaz, %15 fazla hava:    η_ex,yanma ≈ %58-63
  Kömür, %20 fazla hava:        η_ex,yanma ≈ %50-58
  Biyokütle, %30 fazla hava:    η_ex,yanma ≈ %45-52
```

**Azaltma yöntemleri (sınırlı ama mümkün):**
- Fazla hava oranının optimize edilmesi (O₂ trim): %2-5 iyileştirme
- Hava ön ısıtma (regeneratif): Adyabatik alev sıcaklığını yükseltir, %3-5 iyileştirme
- Oksijen zenginleştirme: N₂ dilüsyonunu azaltır, %5-10 iyileştirme (özel uygulama)
- Flameless combustion: Homojen sıcaklık dağılımı, %5-8 iyileştirme (R&D aşamasında)

> **Termodinamik sınır:** Yanma irreversibilitesi tamamen ortadan kaldırılamaz. Teorik minimum, yakıtın gibbs serbest enerjisi ile ilişkilidir. Gerçek sistemlerde %40-55 kayıp kaçınılmazdır.

### 5.2 Isı Transferi İrreversibilitesi

Baca gazı ile su/buhar arasındaki büyük sıcaklık farkı (ΔT) exergy yıkımının ikinci büyük kaynağıdır:

| Bölge | T_sıcak (°C) | T_soğuk (°C) | ΔT (°C) | Exergy Yıkım Payı |
|-------|-------------|-------------|---------|-------------------|
| Radyant bölge | 1200-1800 | 250-350 | 900-1500 | Çok yüksek |
| Konveksiyon bölge | 400-800 | 180-250 | 200-550 | Yüksek |
| Ekonomizer | 150-300 | 80-150 | 50-200 | Orta |
| Süperısıtıcı | 600-900 | 250-450 | 200-500 | Yüksek |

**Azaltma stratejisi:** ΔT'yi azaltmak için çok aşamalı ısı değişimi (ekonomizer + evaporatör + süperısıtıcı) ve karşı akış (counter-flow) düzeni kullanılır.

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Ekonomizer** | %4-8 yakıt | 1-2 yıl | Baca gazı → beslenme suyu; her 20 °C ≈ %1 verim |
| 2 | **Kondens geri dönüşü artırma** | %5-15 yakıt + su | 0.5-1 yıl | %80→%95 kondens geri dönüşü büyük tasarruf |
| 3 | **Blowdown ısı geri kazanımı** | %1-3 yakıt | 1-2 yıl | Flash steam + ısı eşanjör |
| 4 | **Dağıtım hattı izolasyonu** | %3-8 kayıp azaltma | 0.5-1 yıl | Çıplak flanş, vana izolasyonu |
| 5 | **CHP dönüşümü** | %20-35 exergy | 3-7 yıl | Buhar türbini + jeneratör; en yüksek etki |
| 6 | **O₂ trim kontrolü** | %1-3 yakıt | 0.5-1 yıl | Fazla hava oranını optimize et |
| 7 | **Modüler kazan yönetimi** | %5-12 yakıt | 1-3 yıl | Düşük yükte küçük kazan, yüksek yükte büyük kazan |
| 8 | **Buhar basıncı optimizasyonu** | %2-5 exergy | 0 (operasyonel) | Gereksiz yüksek basınçtan kaçın |
| 9 | **Kondenstop bakım programı** | %3-10 buhar | 0.3-0.5 yıl | Yıllık ultrasonik denetim |
| 10 | **Beslenme suyu arıtma** | %1-2 yakıt | 1-2 yıl | TDS azaltma → blowdown azaltma |

### 6.1 İyileştirme Önceliklendirme Matrisi

Buhar sisteminde iyileştirme önceliklendirmesi, tasarruf potansiyeli ve uygulama kolaylığı ile yapılır:

```
Hızlı kazanım (Quick wins) — 0-6 ay ROI:
  ├── Kondenstop onarımı/değişimi
  ├── İzolasyon onarımı (çıplak yüzeyler)
  ├── Kondens geri dönüş oranı artırma
  └── O₂ trim kontrolü ayarı

Orta vadeli — 1-3 yıl ROI:
  ├── Ekonomizer ekleme/upgrade
  ├── Blowdown ısı geri kazanımı
  ├── Modüler kazan yönetimi
  └── Hava ön ısıtıcı ekleme

Stratejik yatırım — 3-7 yıl ROI:
  ├── CHP dönüşümü (karşı basınç türbini)
  ├── Yoğuşmalı kazan yatırımı
  └── Buhar dağıtım hattı yenileme
```

### 6.2 Exergoekonomik Değerlendirme Rehberi

Buhar üretim sisteminde exergoekonomik analiz, yatırım kararlarını exergy bazlı maliyetlerle yönlendirir:

| Parametre | Formül | Hedef |
|-----------|--------|-------|
| Exergy yıkım maliyeti (Ċ_D) | Ċ_D = c_F × İ_D | Minimize et |
| Exergoekonomik faktör (f_k) | f_k = Ż / (Ż + Ċ_D) | %25-%65 optimum |
| Göreceli maliyet farkı (r_k) | r_k = (c_P − c_F) / c_F | Düşük tutmayı hedefle |

**Yorumlama kuralları:**
- f_k < 0.25 → Exergy yıkımı baskın, termodinamik iyileştirme öncelikli (ekonomizer, hava ön ısıtıcı)
- f_k > 0.65 → Yatırım maliyeti baskın, daha ucuz ekipman veya bakım odaklı yaklaşım
- 0.25 < f_k < 0.65 → Dengeli, her iki yön de değerlendirilmeli

> **Kaynak:** SPECO yöntemi — Lazzaretto & Tsatsaronis (2006). Detay için bkz. `factory/exergoeconomic/evaluation_criteria.md`.

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER buhar basıncı < 5 bar (düşük basınç):
  → ESI > 0.30 "Düşük basınç buhar için iyi"
  → ESI < 0.20 "Düşük basınç buhar için zayıf — kazan verimi kontrol et"

EĞER buhar basıncı 5-20 bar (orta basınç):
  → ESI > 0.30 "Orta basınç buhar için iyi"
  → ESI < 0.25 "Orta basınç buhar için iyileştirme gerekli"

EĞER buhar basıncı > 20 bar (yüksek basınç):
  → ESI > 0.35 "Yüksek basınç buhar için iyi"
  → ESI < 0.28 "Yüksek basınç buhar için düşük"

EĞER CHP mevcut:
  → ESI > 0.40 "CHP sistemi etkin çalışıyor"
  → ESI < 0.30 "CHP avantajı yeterince kullanılamıyor"
```

### 7.2 Anahtar Karşılaştırma Noktaları

- **Baca gazı sıcaklığı:** < 120 °C (doğal gaz) veya < 160 °C (kömür) hedefle
- **Kondens geri dönüş oranı:** > %85 olmalı
- **Blowdown oranı:** < %5 TDS kontrolü ile
- **Dağıtım kaybı:** < %5 (iyi bakım ile %2-3 mümkün)

### 7.3 CHP Değerlendirmesi

Buhar prosesinde **her zaman** CHP potansiyelini değerlendir:
- Buhar basıncı > üretim gereksinimi + 5 bar → türbin yerleştir
- Buhar tüketimi > 5 ton/h ve sürekli → CHP fizibilitesi öner
- Detay için bkz. `process/chp.md`

### 7.4 Yaygın Hata Tespiti (AI Diagnostic)

AI yorumlama sırasında aşağıdaki uyarıları kontrol et:

```
EĞER η_energy > %96 (LHV, doğal gaz):
  → "Enerji verimi olağandışı yüksek — ölçüm/hesap kontrolü önerilir"

EĞER η_energy < %75:
  → "Ciddi verim sorunu — baca gazı sıcaklığı, fazla hava, izolasyon kontrol et"

EĞER η_ex > η_energy × 0.45:
  → "Exergy verimi beklenenin üzerinde — giriş parametreleri doğrulanmalı"

EĞER beslenme suyu T < 50 °C:
  → "Beslenme suyu çok soğuk — kondens geri dönüşü yok veya çok düşük"

EĞER blowdown > %8:
  → "Aşırı blowdown — su arıtma sistemi kontrol et, TDS seviyesi optimize et"

EĞER buhar basıncı > proses ihtiyacı + 10 bar VE CHP yok:
  → "Gereksiz yüksek basınç — PRV (pressure reducing valve) üzerinden exergy israfı"
  → "CHP veya buhar türbini entegrasyonu değerlendir"
```

### 7.5 Gap Analysis Entegrasyonu

Bu dosyadaki değerler, gap analysis engine ile şu şekilde eşleşir:

| Bu Dosyadaki Kavram | gap_analysis.py Karşılığı | Açıklama |
|---------------------|---------------------------|----------|
| ex_min (kJ/kg) | minimum_exergy_kW | Termodinamik alt sınır |
| BAT η_ex | bat_exergy_kW | En iyi mevcut teknoloji exergy tüketimi |
| SEC (kJ/kg_buhar) | actual_kW | Mevcut tüketim (aggregates'den) |
| ESI | esi_score | Exergy Sürdürülebilirlik İndeksi |
| BPR | bpr | BAT Performans Oranı |

```python
# gap_analysis.py'deki hesaplama (basitleştirilmiş):
minimum_exergy_kW = mass_flow * ex_min_per_kg
bat_exergy_kW = minimum_exergy_kW / bat_exergy_efficiency
actual_kW = aggregates["total_exergy_input_kW"]
esi_score = minimum_exergy_kW / actual_kW
bpr = bat_exergy_kW / actual_kW
```

> **Kaynak:** `engine/gap_analysis.py`, `engine/bat_references.py` — steam_generation alt-kategorileri.

### 7.6 Buhar Dağıtım Hattı Kayıp Hesabı

Dağıtım kaybı genellikle ihmal edilir ancak exergy açısından önemlidir:

| Durum | Kayıp Miktarı | Exergy Etkisi |
|-------|---------------|---------------|
| İzolasyonsuz DN100 boru (10 bar, 10m) | ~50 kW/10m | %1-2 toplam exergy |
| İzolasyonlu DN100 boru (10 bar, 10m) | ~5 kW/10m | %0.1-0.2 toplam exergy |
| Arızalı kondenstop (1 adet, 10 bar) | 25-100 kg/h buhar | 5-22 kW exergy |
| Buhar kaçağı (3 mm delik, 10 bar) | ~70 kg/h | ~16 kW exergy |

**Pratik formül — yıllık izolasyon tasarrufu:**
```
Q_kayıp (W/m) = π × D_dış × U × (T_yüzey − T_çevre)

Tipik U değerleri:
  İzolasyonsuz çelik boru: 10-15 W/(m²·K)
  50 mm mineral yünü izolasyonlu: 0.5-1.0 W/(m²·K)

Yıllık maliyet = Q_kayıp × 8000 h × yakıt fiyatı / (η_kazan × LHV)
```

---

## İlgili Dosyalar

- `factory/process/heating.md` — Isıtma prosesi (kazan exergy analizi)
- `factory/process/chp.md` — CHP/kojenerasyon prosesi
- `boiler/benchmarks.md` — Kazan ekipman benchmark
- `steam_turbine/systems/` — Buhar türbini CHP konfigürasyonları
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri

## Referanslar

1. European Commission, JRC (2017). *BAT Reference Document for Large Combustion Plants (LCP BREF)*. Ch. 3 — Boiler BAT-AELs.
2. Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*. Butterworths. — Buhar exergy tabloları.
3. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Buhar üretim exergy analizi örnekleri.
4. Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis." *Energy*, 32(4), 249-253.
5. Spirax Sarco (2023). *Steam Engineering Tutorials*. — Kondens, blowdown, dağıtım kayıpları.
6. IAPWS-IF97 (1997). *International Association for the Properties of Water and Steam — Industrial Formulation*. — Buhar tablosu standartı.
7. Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators*. Marcel Dekker. — HRSG tasarımı ve performansı.
8. Spirax Sarco (2023). *Design of Fluid Systems: Steam Utilization*. — Kondens geri dönüş, blowdown, dağıtım.
9. DOE (2012). *Steam System Assessment Tool (SSAT)*. Office of Energy Efficiency. — Buhar sistemi değerlendirme metodolojisi.
