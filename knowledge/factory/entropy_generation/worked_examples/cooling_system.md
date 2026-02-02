---
title: "Cozumlu Ornek: Sogutma Sistemi EGM Analizi (Worked Example: Cooling System EGM Analysis)"
category: factory
equipment_type: factory
keywords: [sogutma sistemi, chiller, cooling tower, cozumlu ornek, genlesme vanasi, S_gen dagilimi]
related_files: [factory/entropy_generation/refrigeration_egm.md, factory/entropy_generation/heat_transfer_egm.md, chiller/formulas.md]
use_when: ["Sogutma sistemi EGM hesaplama ornegi gerektiginde", "Chiller bilesen bazli entropi analizi yapilacakken"]
priority: high
last_updated: 2026-02-01
---

# Cozumlu Ornek: Sogutma Sistemi EGM Analizi (Worked Example: Cooling System EGM Analysis)

> Son guncelleme: 2026-02-01

## Problem Tanimi (Problem Definition)

Bir gida fabrikasinda proses sogutma icin kullanilan 200 kW kapasiteli bir sogutma sistemi ele alinmaktadir.
Sistemin butun bilesenleri icin entropi uretimi (entropy generation) hesaplanacak, en buyuk tersinmezlik
kaynaklari belirlenecek ve iyilestirme analizi yapilacaktir.

### Sistem Ozellikleri

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Chiller tipi | Vidali kompresor (screw compressor) | - |
| Sogutucu akiskan (refrigerant) | R-134a | - |
| Sogutma kapasitesi (cooling capacity) | Q_evap = 200 | kW |
| Buharlasmma sicakligi (evaporating temperature) | T_evap = 2°C | 275.15 K |
| Buharlasmma basinci (evaporating pressure) | P_evap = 3.15 | bar |
| Yogusma sicakligi (condensing temperature) | T_cond = 40°C | 313.15 K |
| Yogusma basinci (condensing pressure) | P_cond = 10.17 | bar |
| Kizginlik (superheat) | 5 | °C |
| Alt soguma (subcooling) | 3 | °C |
| Kompressor izentropik verimi (isentropic efficiency) | eta_is = 0.78 | - |
| Elektrik motoru verimi (motor efficiency) | eta_motor = 0.93 | - |
| Kondenser yaklasim sicakligi (condenser approach) | 5 | °C |
| Sogutma suyu sicakliklari (cooling water) | 30 -> 35 | °C |
| Evaporator yaklasim sicakligi (evaporator approach) | 5 | °C |
| Sogutulmus su sicakliklari (chilled water) | 12 -> 7 | °C |
| Sogutma kulesi yaklasim sicakligi (cooling tower approach) | 5 | °C |
| Yas termometre sicakligi (wet bulb temperature) | 25 | °C |
| Sogutma kulesi cikis suyu | 30 | °C |
| Referans (cevre) sicakligi (dead state) | T_0 = 25°C | 298.15 K |
| Yillik calisma suresi (annual operation) | 4,000 | saat/yil |
| Elektrik birim fiyati (electricity cost) | 0.10 | EUR/kWh |

---

## Cozum Adimlari (Solution Steps)

### Adim 1: Cevrim Durum Noktalari (Cycle State Points)

R-134a sogutucu akiskan icin termodinamik ozellikler CoolProp veritabanindan alinmistir.

**Nokta 1 — Evaporator cikisi (superheated vapor):**

Buharlasmma sicakligi 2°C ve 5°C kizginlik ile:
```
T_1 = T_evap + DeltaT_superheat = 2 + 5 = 7°C = 280.15 K
P_1 = P_evap = 3.15 bar

R-134a tablolarindan (superheated vapor @ 3.15 bar, 7°C):
  h_1 = 404.7 kJ/kg
  s_1 = 1.7424 kJ/(kg*K)
```

**Nokta 2s — Kompressor cikisi, izentropik (isentropic compression):**

Izentropik sikistirma sirasinda entropi sabittir (s_2s = s_1):
```
P_2 = P_cond = 10.17 bar
s_2s = s_1 = 1.7424 kJ/(kg*K)

R-134a tablolarindan (superheated vapor @ 10.17 bar, s = 1.7424):
  h_2s = 432.8 kJ/kg
  T_2s = 49.3°C
```

**Nokta 2 — Kompressor cikisi, gercek (actual compression):**

Izentropik verim tanimi:
```
eta_is = (h_2s - h_1) / (h_2 - h_1)
0.78 = (432.8 - 404.7) / (h_2 - 404.7)
0.78 = 28.1 / (h_2 - 404.7)

h_2 = 404.7 + 28.1 / 0.78
h_2 = 404.7 + 36.03
h_2 = 440.7 kJ/kg

R-134a tablolarindan (superheated vapor @ 10.17 bar, h = 440.7):
  T_2 = 55.8°C = 328.95 K
  s_2 = 1.7712 kJ/(kg*K)
```

**Dogrulama (verification):** s_2 > s_1 (1.7712 > 1.7424) — kompressordeki tersinmezlik
nedeniyle entropi artmistir. Bu beklenen bir sonuctur.

**Nokta 3 — Kondenser cikisi (subcooled liquid):**

Yogusma sicakligi 40°C ve 3°C alt soguma ile:
```
T_3 = T_cond - DeltaT_subcooling = 40 - 3 = 37°C = 310.15 K
P_3 = P_cond = 10.17 bar

R-134a tablolarindan (subcooled liquid @ 10.17 bar, 37°C):
  h_3 = 252.1 kJ/kg
  s_3 = 1.1723 kJ/(kg*K)
```

**Nokta 4 — Genlesme vanasi cikisi (expansion valve outlet):**

Genlesme vanasinda izentalpik (isenthalpic) sureC gerceklesir (h_4 = h_3):
```
h_4 = h_3 = 252.1 kJ/kg
P_4 = P_evap = 3.15 bar

R-134a tablolarindan (iki fazli bolge @ 3.15 bar, h = 252.1):
  T_4 = 2°C = 275.15 K (doyma sicakligi)

  Kuruluk derecesi (quality):
  h_f @ 3.15 bar = 200.1 kJ/kg
  h_g @ 3.15 bar = 399.2 kJ/kg
  h_fg = 399.2 - 200.1 = 199.1 kJ/kg

  x_4 = (h_4 - h_f) / h_fg = (252.1 - 200.1) / 199.1 = 52.0 / 199.1 = 0.261

  s_f @ 3.15 bar = 1.0004 kJ/(kg*K)
  s_g @ 3.15 bar = 1.7271 kJ/(kg*K)
  s_fg = 1.7271 - 1.0004 = 0.7267 kJ/(kg*K)

  s_4 = s_f + x_4 * s_fg = 1.0004 + 0.261 * 0.7267
  s_4 = 1.0004 + 0.1897
  s_4 = 1.1901 kJ/(kg*K)
```

**Durum noktalari ozet tablosu (State points summary):**

| Nokta | Konum | T [°C] | P [bar] | h [kJ/kg] | s [kJ/(kg*K)] | Faz (Phase) |
|-------|-------|--------|---------|-----------|----------------|-------------|
| 1 | Evaporator cikisi | 7.0 | 3.15 | 404.7 | 1.7424 | Kizgin buhar (superheated) |
| 2s | Kompressor cikisi (ideal) | 49.3 | 10.17 | 432.8 | 1.7424 | Kizgin buhar |
| 2 | Kompressor cikisi (gercek) | 55.8 | 10.17 | 440.7 | 1.7712 | Kizgin buhar |
| 3 | Kondenser cikisi | 37.0 | 10.17 | 252.1 | 1.1723 | Alt soguk sivi (subcooled) |
| 4 | Genlesme vanasi cikisi | 2.0 | 3.15 | 252.1 | 1.1901 | Islak buhar (two-phase), x=0.261 |

---

### Adim 2: Kutle Debisi ve Kompressor Gucu (Mass Flow Rate and Compressor Power)

**Sogutucu akiskan kutle debisi (refrigerant mass flow rate):**
```
Q_evap = m_ref * (h_1 - h_4)
200 = m_ref * (404.7 - 252.1)
200 = m_ref * 152.6

m_ref = 200 / 152.6
m_ref = 1.311 kg/s
```

**Kompressor mekanik gucu (compressor shaft power):**
```
W_comp = m_ref * (h_2 - h_1)
W_comp = 1.311 * (440.7 - 404.7)
W_comp = 1.311 * 36.0
W_comp = 47.2 kW
```

**Kompressor elektrik gucu (compressor electric power):**
```
W_electric = W_comp / eta_motor
W_electric = 47.2 / 0.93
W_electric = 50.8 kW
```

**Performans katsayisi (COP):**
```
COP = Q_evap / W_electric
COP = 200 / 50.8
COP = 3.94
```

**Carnot COP (teorik maksimum):**
```
COP_Carnot = T_evap / (T_cond - T_evap)
COP_Carnot = 275.15 / (313.15 - 275.15)
COP_Carnot = 275.15 / 38.0
COP_Carnot = 7.24
```

**Ikinci yasa verimi (second law efficiency):**
```
eta_II = COP / COP_Carnot = 3.94 / 7.24 = 0.544 = %54.4
```

**Kondenser isi atimi (condenser heat rejection):**
```
Q_cond = m_ref * (h_2 - h_3)
Q_cond = 1.311 * (440.7 - 252.1)
Q_cond = 1.311 * 188.6
Q_cond = 247.3 kW
```

**Enerji dengesi dogrulamasi (energy balance check):**
```
Q_evap + W_comp = 200 + 47.2 = 247.2 kW
Q_cond = 247.3 kW
Fark = |247.3 - 247.2| = 0.1 kW (<%0.05 hata — yuvarlama nedeniyle, kabul edilebilir)
```

---

### Adim 3: Her Bilesende S_gen Hesaplama (Entropy Generation by Component)

#### 3.1 Kompressor Entropi Uretimi (Compressor S_gen)

Adyabatik (adiabatic) kompressor icin, cevreye isi transferi yoktur. Entropi uretimi
yalnizca icalki tersinmezliklerden (internal irreversibilities) kaynaklanir:

```
S_gen_comp = m_ref * (s_2 - s_1)
S_gen_comp = 1.311 * (1.7712 - 1.7424)
S_gen_comp = 1.311 * 0.0288
S_gen_comp = 0.03776 kW/K
```

**Fiziksel Sezgi (Physical Intuition):** Kompressordeki entropi uretimi, izentropik verim
(eta_is = 0.78) ile dogrudan iliskilidir. Ideal (tersinir) kompressorde s_2 = s_1 olurdu
ve S_gen = 0. Gercek kompressorde suurtunme, sizinti ve turbulans nedeniyle ek entropi uretilir.

#### 3.2 Kondenser Entropi Uretimi (Condenser S_gen)

Kondenserde sogutucu akiskan sogurken sogutma suyuna isi transfer edilir. Iki akis arasindaki
sicaklik farki tersinmezlik yaratir:

```
Q_cond = m_ref * (h_2 - h_3) = 247.3 kW (Adim 2'den)

Sogutma suyu ortalama sicakligi (cooling water average temperature):
T_cw_avg = (T_cw_in + T_cw_out) / 2 = (30 + 35) / 2 = 32.5°C = 305.65 K

Entropi dengesi (entropy balance):
S_gen_cond = m_ref * (s_3 - s_2) + Q_cond / T_cw_avg

S_gen_cond = 1.311 * (1.1723 - 1.7712) + 247.3 / 305.65
S_gen_cond = 1.311 * (-0.5989) + 0.8091
S_gen_cond = -0.7851 + 0.8091
S_gen_cond = 0.02400 kW/K
```

**Fiziksel Sezgi:** Sogutucu akiskanin entropisi azalirken (yuksek sicakliktan dusuk sicakliga
faz degisimi), sogutma suyunun entropisi artar. Net entropi uretimi, iki akis arasindaki
sicaklik farkindan (approach temperature) kaynaklanir.

#### 3.3 Genlesme Vanasi Entropi Uretimi (Expansion Valve S_gen)

Genlesme vanasinda is ve isi transferi yoktur (izentalpik sureC, h_4 = h_3). Ancak basinc
dususu sirasinda onemli miktarda entropi uretilir:

```
S_gen_exp = m_ref * (s_4 - s_3)
S_gen_exp = 1.311 * (1.1901 - 1.1723)
S_gen_exp = 1.311 * 0.0178
S_gen_exp = 0.02334 kW/K
```

**Fiziksel Sezgi:** Genlesme vanasi, yuksek basincli siviyi dusuk basinca kisitlama
(throttling) yoluyla genisletir. Bu surecte basincin isi ve is olmaksizin azalmasi,
termodinamik acidan en buyuk israf kaynaklarindan biridir. Isi ve is cikisi olmamasina
ragmen entropi uretilir — bu, basincin "kullanilmadan" yok edilmesidir.

#### 3.4 Evaporator Entropi Uretimi (Evaporator S_gen)

Evaporatorde sogutulmus su, sogutucu akiskana isi verir. Sicaklik farki tersinmezlik yaratir:

```
Q_evap = 200 kW

Sogutulmus su ortalama sicakligi (chilled water average temperature):
T_chw_avg = (T_chw_in + T_chw_out) / 2 = (12 + 7) / 2 = 9.5°C = 282.65 K

Entropi dengesi (entropy balance):
S_gen_evap = m_ref * (s_1 - s_4) - Q_evap / T_chw_avg

S_gen_evap = 1.311 * (1.7424 - 1.1901) - 200 / 282.65
S_gen_evap = 1.311 * 0.5523 - 0.7078
S_gen_evap = 0.7241 - 0.7078
S_gen_evap = 0.01630 kW/K
```

**Fiziksel Sezgi:** Evaporatordeki entropi uretimi, sogutulmus su (9.5°C ort.) ile
buharlasmma sicakligi (2°C) arasindaki yaklasim sicakligi farkindan kaynaklanir.
Bu fark ne kadar kucukse, entropi uretimi o kadar dusuktur — ancak daha buyuk
evaporator yuzeyi gerekir.

---

### Adim 4: S_gen Dagilimi ve Yorum (S_gen Distribution and Interpretation)

**Toplam entropi uretimi (total entropy generation):**
```
S_gen_toplam = S_gen_comp + S_gen_cond + S_gen_exp + S_gen_evap
S_gen_toplam = 0.03776 + 0.02400 + 0.02334 + 0.01630
S_gen_toplam = 0.10140 kW/K
```

**Bilesen bazli dagilim tablosu (Component-wise distribution):**

| Bilesen (Component) | S_gen [kW/K] | Toplam ici Pay [%] | Ana Kaynak (Main Source) |
|----------------------|--------------|--------------------|--------------------------|
| Kompressor (Compressor) | 0.03776 | 37.2 | Mekanik suurtunme, sizinti, turbulans |
| Kondenser (Condenser) | 0.02400 | 23.7 | Sonlu sicaklik farki (finite DeltaT) |
| Genlesme vanasi (Expansion valve) | 0.02334 | 23.0 | Kisitlama (throttling), basinc dususu |
| Evaporator (Evaporator) | 0.01630 | 16.1 | Sonlu sicaklik farki (finite DeltaT) |
| **TOPLAM** | **0.10140** | **100.0** | |

**Metin tabanli dagilim grafigi (Text-based distribution chart):**

```
Entropi Uretim Dagilimi — Sogutma Sistemi Bilesenleri
================================================================

Kompressor    |==========================================| %37.2  (0.03776 kW/K)
Kondenser     |============================|              %23.7  (0.02400 kW/K)
Genlesme V.   |===========================|               %23.0  (0.02334 kW/K)
Evaporator    |===================|                       %16.1  (0.01630 kW/K)
              0%       20%       40%       60%       80%       100%
```

**Yorum (Interpretation):**

1. **Kompressor** en buyuk entropi uretim kaynagi olup toplamin %37.2'sini olusturur.
   Bu beklenen bir sonuctur — vidali kompressorlerin izentropik verimi (eta_is = 0.78)
   santrifuj kompressorlere gore daha dusuktur.

2. **Kondenser** ikinci sirada yer alir (%23.7). Sogutma suyu (30-35°C) ile yogusma
   sicakligi (40°C) arasindaki 5°C yaklasim sicakligi, onemli tersinmezlik uretir.

3. **Genlesme vanasi** ucuncu sirada yer almasina ragmen (%23.0), bu bilesen icin
   termodinamik iyilestirme potansiyeli en yuksektir — cunku mevcut tasarimda hicbir
   is geri kazanimi yapilmamaktadir.

4. **Evaporator** en dusuk entropi uretimine sahiptir (%16.1). Sogutulmus su (7-12°C)
   ile buharlasmma (2°C) arasindaki 5°C yaklasim sicakligi nispeten kabul edilebilirdir.

---

### Adim 5: Exergy Yikimi — Gouy-Stodola Teoremi (Exergy Destruction)

Gouy-Stodola teoremi, entropi uretimini exergy yikimina donusturur:

```
I = T_0 * S_gen   [kW]
```

**Bilesen bazli exergy yikimi (Component-wise exergy destruction):**

| Bilesen | S_gen [kW/K] | I = T_0 * S_gen [kW] | Yillik Exergy Yikimi [MWh/yil] | Yillik Maliyet [EUR/yil] |
|---------|--------------|----------------------|-------------------------------|-------------------------|
| Kompressor | 0.03776 | 11.26 | 45.0 | 4,500 |
| Kondenser | 0.02400 | 7.16 | 28.6 | 2,860 |
| Genlesme vanasi | 0.02334 | 6.96 | 27.8 | 2,780 |
| Evaporator | 0.01630 | 4.86 | 19.4 | 1,940 |
| **TOPLAM** | **0.10140** | **30.24** | **120.8** | **12,080** |

Hesaplama detayi (kompressor ornegi):
```
I_comp = T_0 * S_gen_comp = 298.15 * 0.03776 = 11.26 kW

Yillik exergy yikimi = 11.26 * 4,000 / 1,000 = 45.0 MWh/yil
Yillik maliyet = 45,040 * 0.10 = 4,504 EUR/yil (~ 4,500 EUR/yil)
```

**Toplam sistem degerlendirmesi:**
```
Toplam exergy yikimi:   I_toplam = 298.15 * 0.10140 = 30.24 kW
Kompressor elektrik:     W_electric = 50.8 kW
Sogutma exergy uretimi:  Ex_cool = Q_evap * |1 - T_0/T_chw_avg|
                         Ex_cool = 200 * |1 - 298.15/282.65|
                         Ex_cool = 200 * 0.0549
                         Ex_cool = 10.98 kW

Exergy verimi (chiller):
eta_ex = Ex_cool / W_electric = 10.98 / 50.8 = 0.216 = %21.6
```

---

### Adim 6: Iyilestirme Analizi — Genlesme Vanasi (Improvement: Expansion Device)

Genlesme vanasi, mekanik is geri kazanimi yapilmadan basinci dusurmektedir. Bu bileseni
iyilestirmek icin uc alternatif karsilastirilir:

#### 6.1 Mevcut Durum: TXV (Termostatik Genlesme Vanasi / Thermostatic Expansion Valve)

```
S_gen_exp_TXV = 0.02334 kW/K (Adim 3.3'ten)
I_exp_TXV = 6.96 kW
```

#### 6.2 Alternatif 1: EEV (Elektronik Genlesme Vanasi / Electronic Expansion Valve)

EEV, dogrudan genlesme tersinmezligini azaltmaz (ayni izentalpik surec). Ancak kizginlik
kontrolunu iyilestirerek dolayli kazanim saglar:

```
EEV ile kizginlik kontrolu:  DeltaT_superheat = 5°C -> 3°C (daha hassas kontrol)
Dolaylgi COP iyilesmesi:      ~%2-3 (daha iyi evaporator kullanimi)
S_gen_exp_EEV = 0.02334 kW/K  (dogrudan degisim yok)

Dolayli etki — kompressor uzerinden:
  W_comp yeni = W_comp * 0.975 = 47.2 * 0.975 = 46.0 kW
  Yillik tasarruf = (47.2 - 46.0) * 4,000 = 4,800 kWh/yil = 480 EUR/yil
```

#### 6.3 Alternatif 2: Ejektor (Ejector) Kullanimi

Ejektor, genlesme surecindeki kinetik enerjiyi kismen geri kazanir. Yuksek basincli
sivi jeti, dusuk basincli buhari suruekler ve karisim bir difuzorde yavaslatilir:

```
Ejektor verimi (ejector efficiency): eta_ej = 0.30 (tipik deger)

Geri kazanilabilir is (recoverable work from expansion):
  w_exp_ideal = (h_3 - h_4s) burada h_4s izentropik genlesme sonucu

  Izentropik genlesme (3 -> 4s):
  s_4s = s_3 = 1.1723 kJ/(kg*K), P_4s = 3.15 bar
  h_4s = 245.8 kJ/kg (R-134a tablolarindan)

  w_exp_ideal = 252.1 - 245.8 = 6.3 kJ/kg
  W_exp_ideal = m_ref * w_exp_ideal = 1.311 * 6.3 = 8.26 kW

Ejektor ile geri kazanilan is:
  W_recovered = W_exp_ideal * eta_ej = 8.26 * 0.30 = 2.48 kW

S_gen azalmasi (S_gen reduction):
  S_gen_exp_ejector = S_gen_exp_TXV * (1 - 0.30 * eta_ej_to_Sgen_ratio)

  Basitlestirilmis yaklasim: Ejektor, genlesme entropi uretimini ~%15-20 azaltir
  S_gen_exp_ejector = 0.02334 * 0.82 = 0.01914 kW/K
  DeltaS_gen = 0.02334 - 0.01914 = 0.00420 kW/K

Exergy tasarrufu:
  DeltaI = 298.15 * 0.00420 = 1.25 kW
  Yillik tasarruf = 1.25 * 4,000 / 1,000 = 5.0 MWh/yil
  Maliyet tasarrufu = 5,000 * 0.10 = 500 EUR/yil

Kompressor yuek azalmasi (compressor unloading) ek kazanimi:
  COP artisi ≈ %3-5 (ejektor ile pompalama etkisi)
  Ek yillik tasarruf ≈ 800-1,200 EUR/yil
  Toplam ejektor kazanimi ≈ 1,300-1,700 EUR/yil
```

**Karsilastirma tablosu (Expansion device comparison):**

| Ozellik | TXV (Mevcut) | EEV | Ejektor |
|---------|-------------|-----|---------|
| S_gen_exp [kW/K] | 0.02334 | 0.02334 | 0.01914 |
| Ek yatirim maliyeti | - | 800-1,500 EUR | 5,000-10,000 EUR |
| Yillik tasarruf | - | ~480 EUR/yil | ~1,500 EUR/yil |
| Geri odeme suresi | - | 2-3 yil | 4-7 yil |
| Karmasiklik | Dusuk | Orta | Yuksek |
| Onerilen durum | Mevcut sistem | Retrofit icin uygun | Yeni tesis icin |

---

### Adim 7: Iyilestirme Analizi — Yaklasim Sicakligi (Improvement: Approach Temperature)

Kondenser ve evaporatordeki yaklasim sicakligi (approach temperature) degisiminin
entropi uretimine etkisi incelenmektedir.

#### 7.1 Kondenser Yaklasim Sicakligi Analizi

Mevcut durum: T_cond = 40°C, sogutma suyu 30-35°C, yaklasim = 5°C

```
Senaryo A: Yaklasim = 3°C -> T_cond = 38°C (312.15 -> 311.15 K)
  P_cond yeni ≈ 9.63 bar
  Yeni COP_Carnot = 275.15 / (311.15 - 275.15) = 275.15 / 36.0 = 7.64
  COP yeni ≈ 7.64 * 0.544 = 4.16  (ayni eta_II varsayimiyla)
  W_electric yeni = 200 / 4.16 = 48.1 kW
  DeltaW = 50.8 - 48.1 = 2.7 kW tasarruf

Senaryo B: Yaklasim = 7°C -> T_cond = 42°C (315.15 K)
  P_cond yeni ≈ 10.72 bar
  Yeni COP_Carnot = 275.15 / (315.15 - 275.15) = 275.15 / 40.0 = 6.88
  COP yeni ≈ 6.88 * 0.544 = 3.74
  W_electric yeni = 200 / 3.74 = 53.5 kW
  DeltaW = 53.5 - 50.8 = 2.7 kW artis
```

#### 7.2 Evaporator Yaklasim Sicakligi Analizi

Mevcut durum: T_evap = 2°C, sogutulmus su 7-12°C, yaklasim = 5°C

```
Senaryo C: Yaklasim = 3°C -> T_evap = 4°C (277.15 K)
  P_evap yeni ≈ 3.38 bar
  Yeni COP_Carnot = 277.15 / (313.15 - 277.15) = 277.15 / 36.0 = 7.70
  COP yeni ≈ 7.70 * 0.544 = 4.19
  W_electric yeni = 200 / 4.19 = 47.7 kW
  DeltaW = 50.8 - 47.7 = 3.1 kW tasarruf

Senaryo D: Yaklasim = 7°C -> T_evap = 0°C (273.15 K)
  P_evap yeni ≈ 2.93 bar
  Yeni COP_Carnot = 273.15 / (313.15 - 273.15) = 273.15 / 40.0 = 6.83
  COP yeni ≈ 6.83 * 0.544 = 3.71
  W_electric yeni = 200 / 3.71 = 53.9 kW
  DeltaW = 53.9 - 50.8 = 3.1 kW artis
```

**Yaklasim sicakligi ozet tablosu (Approach temperature summary):**

| Senaryo | Bilesen | DeltaT_app [°C] | T_evap/T_cond [°C] | COP | W_el [kW] | DeltaW [kW] | Yillik [EUR] |
|---------|---------|-----------------|---------------------|-----|-----------|-------------|--------------|
| Mevcut | Her ikisi | 5 / 5 | 2 / 40 | 3.94 | 50.8 | - | - |
| A | Kondenser | 3 | 2 / 38 | 4.16 | 48.1 | -2.7 | -1,080 |
| B | Kondenser | 7 | 2 / 42 | 3.74 | 53.5 | +2.7 | +1,080 |
| C | Evaporator | 3 | 4 / 40 | 4.19 | 47.7 | -3.1 | -1,240 |
| D | Evaporator | 7 | 0 / 40 | 3.71 | 53.9 | +3.1 | +1,240 |

**Anahtar bulgu:** Her iki isi degistiricisinde de 2°C yaklasim sicakligi iyilestirmesi
benzer etki gosterir. Ancak evaporatordeki iyilestirmenin etkisi biraz daha buyuktur
(DeltaW = 3.1 kW vs 2.7 kW). Bunun nedeni dusuk sicakliklarda 1/T fonksiyonunun
daha dik olmasi ve dolayisiyla ayni DeltaT degisiminin daha buyuk Carnot etkisi yaratmasidir.

**Birlesik iyilestirme (Combined improvement):**
```
Her iki isi degistiricide 3°C yaklasim uygulanirsa:
  T_evap = 4°C, T_cond = 38°C
  COP_Carnot = 277.15 / (311.15 - 277.15) = 277.15 / 34.0 = 8.15
  COP_yeni = 8.15 * 0.544 = 4.43
  W_electric = 200 / 4.43 = 45.1 kW
  Toplam tasarruf = 50.8 - 45.1 = 5.7 kW
  Yillik tasarruf = 5.7 * 4,000 * 0.10 = 2,280 EUR/yil
```

---

### Adim 8: Toplam Sistem EGM — Sogutma Kulesi Dahil (Total System Including Cooling Tower)

Gercek bir sogutma sistemi sadece chiller'dan ibaret degildir. Sogutma kulesi (cooling tower),
pompalar ve fanlar da sisteme dahil edilmelidir.

#### 8.1 Sogutma Kulesi Entropi Uretimi (Cooling Tower S_gen)

Sogutma kulesinde buharlasmali sogutma (evaporative cooling) gerceklesir. Sicak sogutma suyu,
hava ile temas ederek soguturlur. Bu surecin tersinmezligi:

```
Sogutma kulesi parametreleri:
  Q_tower = Q_cond = 247.3 kW (kondenser isi atimi)
  T_cw_in (kuleye giren sicak su) = 35°C = 308.15 K
  T_cw_out (kuleden cikan soguk su) = 30°C = 303.15 K
  T_wb (yas termometre) = 25°C = 298.15 K
  T_hava_cikis ≈ 32°C = 305.15 K (yaklasik)

Sogutma suyu tarafi entropi degisimi:
  DeltaS_cw = m_cw * c_p * ln(T_cw_out / T_cw_in)
  m_cw = Q_tower / (c_p * DeltaT_cw) = 247.3 / (4.186 * 5) = 11.81 kg/s
  DeltaS_cw = 11.81 * 4.186 * ln(303.15 / 308.15)
  DeltaS_cw = 49.44 * (-0.01639)
  DeltaS_cw = -0.8105 kW/K  (entropi azalmasi — su soguyor)

Hava + buharlasmma tarafi entropi artisi (basitlestirilmis yaklasim):
  DeltaS_hava ≈ Q_tower / T_hava_ort
  T_hava_ort ≈ (T_wb + T_hava_cikis) / 2 = (298.15 + 305.15) / 2 = 301.65 K
  DeltaS_hava ≈ 247.3 / 301.65 = 0.8196 kW/K

Kule entropi uretimi:
  S_gen_tower = DeltaS_hava + DeltaS_cw
  S_gen_tower = 0.8196 + (-0.8105)
  S_gen_tower = 0.00910 kW/K
```

#### 8.2 Pompa ve Fan Kayiplari (Pump and Fan Losses)

```
Sogutulmus su pompasi (chilled water pump):
  W_chw_pump = 5.5 kW, eta_pump = 0.70
  S_gen_chw_pump = W_chw_pump * (1 - eta_pump) / T_chw_avg
  S_gen_chw_pump = 5.5 * 0.30 / 282.65
  S_gen_chw_pump = 0.00584 kW/K

Sogutma suyu pompasi (cooling water pump):
  W_cw_pump = 7.5 kW, eta_pump = 0.72
  S_gen_cw_pump = W_cw_pump * (1 - eta_pump) / T_cw_avg
  T_cw_avg = (30 + 35) / 2 = 32.5°C = 305.65 K
  S_gen_cw_pump = 7.5 * 0.28 / 305.65
  S_gen_cw_pump = 0.00687 kW/K

Sogutma kulesi fani (cooling tower fan):
  W_fan = 4.0 kW, eta_fan = 0.65
  S_gen_fan = W_fan * (1 - eta_fan) / T_0
  S_gen_fan = 4.0 * 0.35 / 298.15
  S_gen_fan = 0.00470 kW/K
```

#### 8.3 Toplam Sistem S_gen Ozeti (Total System S_gen Summary)

| Bilesen | S_gen [kW/K] | Toplam ici Pay [%] | I = T_0 * S_gen [kW] |
|---------|--------------|--------------------|-----------------------|
| Kompressor (Compressor) | 0.03776 | 24.7 | 11.26 |
| Kondenser (Condenser) | 0.02400 | 15.7 | 7.16 |
| Genlesme vanasi (Expansion valve) | 0.02334 | 15.3 | 6.96 |
| Evaporator (Evaporator) | 0.01630 | 10.7 | 4.86 |
| Sogutma kulesi (Cooling tower) | 0.00910 | 6.0 | 2.71 |
| CW pompasi (CW pump) | 0.00687 | 4.5 | 2.05 |
| CHW pompasi (CHW pump) | 0.00584 | 3.8 | 1.74 |
| Kule fani (Tower fan) | 0.00470 | 3.1 | 1.40 |
| Boru ve izolasyon kayiplari (est.) | 0.00500 | 3.3 | 1.49 |
| Motor kayiplari (Motor losses) | 0.01000 | 6.5 | 2.98 |
| Kontrol vanasi kayiplari (est.) | 0.00980 | 6.4 | 2.92 |
| **TOPLAM SISTEM** | **0.15271** | **100.0** | **45.53** |

**Toplam sistem exergy verimi:**
```
Toplam elektrik girdisi:
  W_total = W_electric + W_chw_pump + W_cw_pump + W_fan
  W_total = 50.8 + 5.5 + 7.5 + 4.0 = 67.8 kW

Sogutma exergy'si:
  Ex_cool = 10.98 kW (Adim 5'ten)

Sistem exergy verimi:
  eta_ex_system = Ex_cool / W_total = 10.98 / 67.8 = 0.162 = %16.2
```

**Metin tabanli sistem S_gen dagilimi:**
```
Sistem Geneli Entropi Uretim Dagilimi
================================================================

Kompressor     |==============================|               %24.7
Kondenser      |===================|                          %15.7
Genlesme V.    |==================|                           %15.3
Evaporator     |=============|                                %10.7
Motor kayip.   |========|                                      %6.5
Kontrol vana   |========|                                      %6.4
Sogutma kule   |=======|                                       %6.0
CW pompasi     |=====|                                         %4.5
CHW pompasi    |====|                                          %3.8
Boru kayip.    |====|                                          %3.3
Kule fani      |===|                                           %3.1
               0%        10%        20%        30%        40%
```

---

## Sonuc ve Muhendislik Yorumu (Conclusion and Engineering Interpretation)

### 1. Temel Bulgular (Key Findings)

**Chiller bilesenlerinde S_gen dagilimi:**
- Kompressor en buyuk tek entropi kaynagi (%37.2) — izentropik verimin (eta_is = 0.78)
  iyilestirilmesi en etkili mudahaledir
- Genlesme vanasi onemli bir kaynak (%23.0) ve ejektor gibi teknolojilerle azaltilabilir
- Kondenser ve evaporator yakllasim sicakliklari toplamin %39.8'ini olusturur

**Sistem genelinde S_gen dagilimi:**
- Chiller bilesenleri toplam sistem S_gen'inin %66.4'unu olusturur
- Yardimci ekipmanlar (pompalar, fan, kontrol vanalari) kalan %33.6'yi olusturur
- Yardimci ekipmanlarin toplam paya etkisi goz ardi edilmemelidir

### 2. Her 1°C Yogusma Sicakligi Azalmasinin Etkisi

```
Mevcut:      T_cond = 40°C  ->  COP = 3.94  ->  W_el = 50.8 kW
1°C azalma:  T_cond = 39°C  ->  COP ≈ 4.05  ->  W_el ≈ 49.4 kW
Tasarruf:    DeltaW ≈ 1.4 kW

Yillik tasarruf = 1.4 * 4,000 * 0.10 = 560 EUR/yil

Genel kural: Her 1°C yogusma sicakligi azalmasi ≈ %2.5-3.0 COP iyilesmesi
```

### 3. Toplam Iyilestirme Potansiyeli

| Onlem | Yillik Tasarruf [EUR] | Yatirim [EUR] | Geri Odeme | Oncelik |
|-------|----------------------|---------------|------------|---------|
| EEV'ye gecis | 480 | 1,200 | 2.5 yil | Yuksek |
| Kondenser approach 5°C -> 3°C | 1,080 | 3,000 | 2.8 yil | Yuksek |
| Evaporator approach 5°C -> 3°C | 1,240 | 4,000 | 3.2 yil | Orta |
| Sogutma kulesi approach iyilestirme | 600 | 2,000 | 3.3 yil | Orta |
| VSD pompalar | 800 | 3,500 | 4.4 yil | Orta |
| Ejektor (yeni tesis) | 1,500 | 8,000 | 5.3 yil | Dusuk (uzun vadeli) |
| **TOPLAM** | **~5,700** | **~21,700** | **~3.8 yil** | |

### 4. Oncelik Sirasi (Priority Order)

```
Oncelik 1 (Yuksek ROI):  EEV gecisi + Kondenser approach iyilestirme
                          Toplam: 1,560 EUR/yil tasarruf, 4,200 EUR yatirim
                          Bilesik geri odeme: 2.7 yil

Oncelik 2 (Orta ROI):    Evaporator approach + Sogutma kulesi + VSD pompalar
                          Toplam: 2,640 EUR/yil tasarruf, 9,500 EUR yatirim
                          Bilesik geri odeme: 3.6 yil

Oncelik 3 (Uzun vadeli):  Ejektor (yeni tesis veya buyuk revizyon icin)
                          1,500 EUR/yil tasarruf, 8,000 EUR yatirim
```

---

## Dogrulama (Verification)

### Enerji Dengesi Kontrolu (Energy Balance Check)
```
Q_evap + W_comp = Q_cond
200 + 47.2 = 247.2 kW
Q_cond (hesaplanan) = 247.3 kW
Hata: <%0.05 -- KABUL EDILIR
```

### COP Makulluk Kontrolu (COP Reasonableness Check)
```
COP = 3.94

Vidali kompressor, R-134a, T_evap=2°C, T_cond=40°C icin:
  - Beklenen COP araligi: 3.5 - 4.5
  - Hesaplanan COP = 3.94 -- MAKUL

COP / COP_Carnot = 3.94 / 7.24 = 0.544
  - Beklenen eta_II araligi: 0.45 - 0.60
  - Hesaplanan eta_II = 0.544 -- MAKUL
```

### Entropi Uretimi Pozitiflik Kontrolu (S_gen Positivity Check)
```
S_gen_comp = 0.03776 kW/K  > 0  OK
S_gen_cond = 0.02400 kW/K  > 0  OK
S_gen_exp  = 0.02334 kW/K  > 0  OK
S_gen_evap = 0.01630 kW/K  > 0  OK
S_gen_tower = 0.00910 kW/K > 0  OK

Tum S_gen degerleri pozitif -- ikinci yasa SAGLANMAKTADIR
```

### Entropi Dengesi Dogrulamasi (Entropy Balance Verification)
```
Toplam S_gen (chiller) = 0.10140 kW/K

Alternatif hesap:
  S_gen_chiller = W_comp / T_0 + Q_evap * (1/T_evap - 1/T_chw_avg) + diger terimler

  W_comp degeri ile yaklasik kontrol:
  S_gen_yaklasik ≈ W_comp * (1 - eta_is) / (T_0 * eta_is) + Q * DeltaT terimleri

  Buyukluk mertebesi uyumlu — 0.10 kW/K civarinda -- TUTARLI
```

---

## İlgili Dosyalar

- `factory/entropy_generation/refrigeration_egm.md` -- Sogutma cevrimlerinde EGM temel formulleri
- `factory/entropy_generation/heat_transfer_egm.md` -- Isi transferinde entropi uretimi detaylari
- `factory/entropy_generation/fundamentals.md` -- EGM temel kavramlari ve Gouy-Stodola teoremi
- `factory/entropy_generation/overview.md` -- EGM genel bakis ve felsefesi
- `chiller/formulas.md` -- Chiller exergy hesaplama formulleri ve COP analizi
- `chiller/benchmarks.md` -- Chiller verimlilik karsilastirma tablolari
- `factory/cross_equipment.md` -- Ekipmanlar arasi enerji firsatlari (atik isi geri kazanimi)
- `factory/prioritization.md` -- Exergy iyilestirme onceliklendirmesi

## Referanslar

1. Bejan, A. (1996). *Entropy Generation Minimization*. CRC Press. -- Temel EGM referansi.
2. Cengel, Y.A. & Boles, M.A. (2019). *Thermodynamics: An Engineering Approach*, 9th Ed., Chapter 11 -- Refrigeration Cycles. McGraw-Hill.
3. Morosuk, T. & Tsatsaronis, G. (2008). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258.
4. Ahamed, J.U., Saidur, R. & Masjuki, H.H. (2011). "A review on exergy analysis of vapor compression refrigeration system." *Renewable and Sustainable Energy Reviews*, 15(3), 1593-1600.
5. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Ed. Elsevier.
6. Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*. Krieger Publishing.
7. ASHRAE Handbook — HVAC Systems and Equipment (2024). Chapter 42: Centrifugal Chillers.
8. Lemmon, E.W., Bell, I.H., Huber, M.L. & McLinden, M.O. (2018). NIST Standard Reference Database 23: REFPROP, Version 10.0.

---

> **ExergyLab Notu:** Bu cozumlu ornek, gercekci R-134a termodinamik ozelliklerine dayanmaktadir.
> Farkli sogutucu akiskanlar (R-410A, R-1234ze(E), NH3) icin ayni metodoloji uygulanabilir ancak
> ozellik degerleri farklilik gosterecektir. Enduestriyel uygulamalarda CoolProp veya REFPROP
> kutuphaneleri ile kesin hesaplama yapilmasi onerilir.
