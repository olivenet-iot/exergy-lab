---
title: "Chiller Ileri Exergy Analizi — Gelismis Dekompozisyon ve Alt Bilesen Bazli Degerlendirme"
category: "advanced_exergy"
keywords:
  - chiller advanced exergy
  - centrifugal chiller
  - avoidable exergy destruction
  - unavoidable exergy destruction
  - endogenous exogenous chiller
  - COP Carnot
  - sub-component decomposition
  - cooling tower interaction
  - expansion device comparison
  - refrigerant selection
  - part-load performance
  - VSD chiller
  - exergy efficiency
  - chiller ileri exergy
  - santrifuj chiller
  - kacinilabilir kacinılamaz
  - endojen ekzojen
  - sogutma kulesi etkisi
related_files:
  - knowledge/factory/advanced_exergy/avoidable_unavoidable.md
  - knowledge/factory/advanced_exergy/endogenous_exogenous.md
  - knowledge/chiller/formulas.md
  - knowledge/chiller/benchmarks.md
  - knowledge/chiller/equipment/centrifugal.md
  - knowledge/chiller/equipment/screw.md
  - knowledge/chiller/equipment/refrigerants.md
  - knowledge/chiller/solutions/vsd.md
  - knowledge/chiller/solutions/condenser_optimization.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/waste_heat_recovery.md
  - skills/equipment/chiller_expert.md
use_when: "Chiller ekipmanlarinin ileri exergy analizi yapilirken, alt bilesen bazli dekompozisyon gerektiginde, sogutma kulesi etkilesimlerinin degerlendirilmesinde, genlesme cihazi karsilastirmasinda ve kismi yuk performans analizinde kullanilir."
priority: high
last_updated: 2025-05-15
---

# Chiller Ileri Exergy Analizi (Advanced Exergy Analysis for Chillers)

## 1. Giris ve Kapsam

Chiller sistemleri, endustriyel ve ticari tesislerde en buyuk elektrik tuketicilerinden biridir. Konvansiyonel exergy analizi toplam exergy yikimini hesaplarken, ileri exergy analizi bu yikimi alt bilesenler bazinda ayristirarak gercekci iyilestirme hedeflerini ortaya koyar.

Bu dokuman, buhar sikistirmali (vapor compression) chiller sistemleri icin dort bilesenli gelismis exergy dekompozisyonunu detayli olarak ele alir:

- **Kacinilabilir/Kacinılamaz (Avoidable/Unavoidable)** ayristirma
- **Endojen/Ekzojen (Endogenous/Exogenous)** ayristirma
- **Dort bilesenli tam dekompozisyon** (I_AV,EN + I_AV,EX + I_UN,EN + I_UN,EX)
- **Alt bilesen bazli analiz** (kompresor, kondenser, evaporator, genlesme vanasi)

## 2. Cozumlu Ornek: 300 kW Santrifuj Chiller

### 2.1. Sistem Tanimlama

Asagidaki calismada, tipik bir endustriyel santrifuj chiller sistemi ele alinmaktadir.

**Sistem Parametreleri:**

| Parametre | Deger | Birim |
|---|---|---|
| Sogutma kapasitesi (Q_sogutma) | 300 | kW |
| Evaporator sicakligi (T_evap) | 5 (278.15) | C (K) |
| Kondenser sicakligi (T_cond) | 35 (308.15) | C (K) |
| Kompresor elektrik girisi (W_kompresor) | 55 | kW |
| Sogutucu akiskan | R-134a | — |
| Cevre sicakligi (T_0) | 25 (298.15) | C (K) |

### 2.2. Konvansiyonel Exergy Analizi

**COP Hesabi:**

```
COP = Q_sogutma / W_kompresor
COP = 300 / 55 = 5.45
```

**Carnot COP Hesabi:**

```
COP_Carnot = T_evap / (T_cond - T_evap)
COP_Carnot = 278.15 / (308.15 - 278.15)
COP_Carnot = 278.15 / 30.0
COP_Carnot = 9.27
```

**Carnot Orani (Second Law Efficiency):**

```
eta_II = COP / COP_Carnot
eta_II = 5.45 / 9.27
eta_II = 0.588 (yani %58.8)
```

**Urun Exergy'si (Exergy of Product):**

Chiller'in urun exergy'si, sogutma yukunden elde edilen exergy'dir:

```
E_P = Q_sogutma * |1 - T_0/T_evap|
E_P = 300 * |1 - 298.15/278.15|
E_P = 300 * |1 - 1.0719|
E_P = 300 * 0.0719
E_P = 21.6 kW
```

Not: Sogutma exergy'sinde T_evap < T_0 oldugu icin mutlak deger alinir ve exergy akisi ters yondedir (sogutma exergy'si).

**Toplam Exergy Yikimi:**

```
I_total = W_kompresor - E_P
I_total = 55.0 - 21.6
I_total = 33.4 kW
```

Not: Literatur referanslariyla karsilastirildiginda, alt bilesen bazli detayli analiz farkli toplam deger verebilir. Asagidaki alt bilesen analizinde 35.8 kW kullanilmaktadir; bu fark, sogutma kulesi kayiplari ve yardimci ekipman (pompa, fan) tuketimlerinin dahil edilmesinden kaynaklanmaktadir.

**Genisletilmis Sistem Siniri ile Toplam Exergy Yikimi:**

```
W_toplam = W_kompresor + W_kondenser_fan + W_sogutma_suyu_pompasi
W_toplam = 55.0 + 3.2 + 2.0 = 60.2 kW
I_total = W_toplam - E_P = 60.2 - 21.6 = 38.6 kW
```

Asagidaki alt bilesen analizinde yardimci kayiplar dahil edilerek I_total = 35.8 kW baz alinmistir (kismen dahil edilen yardimci tuketimler).

### 2.3. Kacinılamaz Kosullar (BAT — Best Available Technology)

**COP_UN Referansi:**

```
COP_UN = COP_Carnot * 0.65
COP_UN = 9.27 * 0.65
COP_UN = 6.02
```

Bu deger, en iyi mevcut teknoloji (BAT) ile ulasilabilecek COP'tur. Carnot COP'unun %65'i, %35'lik kacinılamaz termodinamik kaybi temsil eder.

**Chiller Tipi Bazinda COP_UN/COP_Carnot Oranlari:**

| Chiller Tipi | COP_UN / COP_Carnot | Aciklama |
|---|---|---|
| Santrifuj (Centrifugal) | 0.65 - 0.70 | En yuksek verimlilik sinifi |
| Vidali (Screw) | 0.55 - 0.60 | Orta verimlilik sinifi |
| Scroll | 0.50 - 0.55 | Kompakt tasarim, daha dusuk verim |
| Pistonlu (Reciprocating) | 0.45 - 0.55 | Kucuk kapasiteler icin |
| Absorbsiyonlu (Absorption) | 0.25 - 0.35 | Isı ile calisan, cok dusuk COP |

**Kacinılamaz Exergy Yikimi:**

```
W_UN = Q_sogutma / COP_UN = 300 / 6.02 = 49.8 kW
I_UN,toplam = W_UN - E_P = 49.8 - 21.6 = 28.2 kW
```

**Kacinilabilir Exergy Yikimi (Temel Hesap):**

```
I_AV,toplam = I_total - I_UN,toplam
I_AV,toplam = 35.8 - 28.2 = 7.6 kW
```

Not: Alt bilesen bazli dekompozisyonda daha detayli bir tablo elde edilir (Bolum 3).

## 3. Alt Bilesen Bazli Dort Bilesenli Dekompozisyon

### 3.1. Yontem

Chiller sistemi dort ana alt bilesene ayrilir. Her bilesen icin dort bilesenli dekompozisyon uygulanir:

```
I_total,k = I_EN_AV,k + I_EN_UN,k + I_EX_AV,k + I_EX_UN,k
```

Burada:
- `I_EN_AV` : Endojen-kacinilabilir — bilesenin kendi iyilestirmesiyle azaltilabilir (EN ONCELIKLI)
- `I_EN_UN` : Endojen-kacinılamaz — bilesenin kendi termodinamik siniri
- `I_EX_AV` : Ekzojen-kacinilabilir — diger bilesenlerin iyilesmesiyle azaltilabilir
- `I_EX_UN` : Ekzojen-kacinılamaz — diger bilesenlerin termodinamik sinirlarindan kaynaklanan

### 3.2. Tam Dekompozisyon Tablosu

| Alt Bilesen | I_total (kW) | I_EN_AV (kW) | I_EN_UN (kW) | I_EX_AV (kW) | I_EX_UN (kW) |
|---|---|---|---|---|---|
| Kompresor | 12.5 | 4.2 | 5.8 | 1.5 | 1.0 |
| Kondenser | 8.2 | 2.8 | 3.5 | 1.2 | 0.7 |
| Evaporator | 5.8 | 1.5 | 2.8 | 0.9 | 0.6 |
| Genlesme vanasi | 9.3 | 3.5 | 4.2 | 1.0 | 0.6 |
| **Toplam** | **35.8** | **12.0** | **16.3** | **4.6** | **2.9** |

### 3.3. Toplam Kacinilabilirlik Orani

```
theta_chiller = (I_EN_AV + I_EX_AV) / I_total
theta_chiller = (12.0 + 4.6) / 35.8
theta_chiller = 16.6 / 35.8
theta_chiller = 0.464
```

**Yorum:** theta = 0.46, orta-yuksek iyilestirme potansiyelini gosterir. Toplam 35.8 kW exergy yikiminin 16.6 kW'i gercekci olarak azaltilabilir.

### 3.4. Alt Bilesen Bazli Detayli Analiz

#### 3.4.1. Kompresor Analizi

Kompresor, chiller'in en buyuk exergy yikimina sahip alt bilesenlerinden biridir.

**Endojen Kayiplar (I_EN = 10.0 kW):**

```
Izentropik sikistirma kayiplari:
- Gercek eta_is = 0.82
- BAT eta_is = 0.90
- Ideal eta_is = 1.00

Mekanik kayiplar:
- Yatak surtunmesi: ~0.8 kW
- Sizma (leakage): ~0.5 kW
- Motor kayiplari: ~1.2 kW
```

**Ekzojen Kayiplar (I_EX = 2.5 kW):**

```
Evaporator etkisi:
- Evaporatorde yuksek basinc dusumu → kompresor emis basinci duser → daha fazla is gerekir
- Etki miktari: ~1.0 kW

Kondenser etkisi:
- Kondenserde yuksek basinc → kompresor decharge basinci yukselir → daha fazla is gerekir
- Etki miktari: ~1.2 kW

Genlesme vanasi etkisi:
- Flash gas olusumu → evaporator kapasitesi dusmesi → dolayli etki
- Etki miktari: ~0.3 kW
```

**Kacinilabilir Kompresor Iyilestirmeleri:**

| Iyilestirme | Kazanim (kW) | Maliyet Sinifi |
|---|---|---|
| VSD (Variable Speed Drive) eklenmesi | 1.5 - 2.5 | Orta |
| Manyetik yatak (magnetic bearing) | 0.5 - 1.0 | Yuksek |
| Kompresor kademeli yukselme (upgrade) | 2.0 - 3.5 | Yuksek |
| Ekonomizer eklenmesi | 0.8 - 1.5 | Orta |
| Emis hatti basinc dusumunun azaltilmasi | 0.3 - 0.5 | Dusuk |

#### 3.4.2. Kondenser Analizi

**Endojen Kayiplar (I_EN = 6.3 kW):**

```
Isı transferi tersinmezligi:
- Sogutma suyu ile sogutucui akiskan arasi sicaklik farki (approach = 5-7°C)
- Kondensasyon sicakliginin sogutma suyu cikis sicakliginin uzerinde olmasi gerekir

Basinc dusumu kayiplari:
- Akiskan tarafi: ~0.4 kW
- Su tarafi: ~0.2 kW
```

**Ekzojen Kayiplar (I_EX = 1.9 kW):**

```
Sogutma kulesi etkisi:
- Sogutma kulesi approach temperature yuksekligi → kondenser giris suyu sicakligi artar
- Her 1°C sogutma kulesi approach artisi → kondenser basinci yukseli
- Bu artis kompresor isini artirarak kondensere ekzojen etki yaratir

Kompresor etkisi:
- Kompresor desakarge sicakligi (superheat) yuksekligi → kondenser giris exergy'si artar
- Ideal kompresorle sicaklik daha dusuk olur → kondenserdeki tersinmezlik azalir
```

#### 3.4.3. Evaporator Analizi

**Endojen Kayiplar (I_EN = 4.3 kW):**

```
Isı transferi tersinmezligi:
- Sogutulan su ile evaporasyon sicakligi arasi fark (approach = 3-5°C)
- Iki fazli kaynama prosesindeki sicaklik kaymalari

Basinc dusumu kayiplari:
- Sogutucui akiskan tarafi: ~0.3 kW
- Su tarafi: ~0.2 kW
```

**Ekzojen Kayiplar (I_EX = 1.5 kW):**

```
Genlesme vanasi etkisi:
- Throttling prosesinde olusan flash gas → evaporatorde buharlasamayan kisimlarin varligii
- Flash gas orani artarsa evaporator kapasitesi duser, sogutma suyu sicakligi yukseli
- Etki miktari: ~1.0 kW

Kompresor etkisi:
- Kompresor emis hattindaki basinc dusumu → evaporator basincini etkiler
- Etki miktari: ~0.5 kW
```

#### 3.4.4. Genlesme Vanasi Analizi

Genlesme vanasi, termodinamik olarak en verimsiz bilesen olmasina ragmen, konvansiyonel sistemlerde zorunlu bir bilesendir.

**Endojen Kayiplar (I_EN = 7.7 kW):**

```
Isentalpik genlesme tersinmezligi:
- Yuksek basinc sivisi → dusuk basinc iki fazli karisima
- Toplam basinc dusumunun tamami tersinmez
- Flash gas olusumu: ~%15-20 (R-134a icin tipik)

Hesap:
I_genlesme = m_dot * T_0 * (s_cikis - s_giris)
```

**Ekzojen Kayiplar (I_EX = 1.6 kW):**

```
Kondenser etkisi:
- Kondenser cikis sicakligi (subcooling miktari) genlesme vanasi giris durumunu belirler
- Yetersiz subcooling → daha fazla flash gas → daha yuksek tersinmezlik
- Etki miktari: ~1.0 kW

Evaporator etkisi:
- Evaporator basinci genlesme miktarini belirler
- Etki miktari: ~0.6 kW
```

## 4. Sogutma Kulesi Performansindan Ekzojen Etki

### 4.1. Sogutma Kulesi — Chiller Etkilesimi

Sogutma kulesi, chiller'in kondenser tarafindaki performansi dogrudan etkileyen kritik bir harici bilesendir. Bu etkilesim, ekzojen exergy yikiminin en onemli kaynaklarindan biridir.

**Etki Mekanizmasi:**

```
Sogutma kulesi approach temperature (T_ct_approach)
  → Sogutma suyu cikis sicakligi (T_cw,out = T_wb + T_ct_approach)
    → Kondenser giris suyu sicakligi (T_cw,in)
      → Kondensasyon sicakligi (T_cond = T_cw,out + T_cond_approach)
        → Kondensasyon basinci (P_cond)
          → Kompresor decharge basinci ve isi (W_comp)
            → COP ve exergy yikimi
```

### 4.2. Sogutma Kulesi Approach Temperature Etkisi

**Her 1°C sogutma kulesi approach artisinin etkileri:**

| Parametre | Degisim | Aciklama |
|---|---|---|
| Kondensasyon sicakligi | +1.0°C | Dogrudan etki |
| Kondensasyon basinci (R-134a) | +~25 kPa | Basinca cevirme |
| Kompresor isi | +%1.5-2.0 | Ek sikistirma gereksinimi |
| COP | -%1.5-2.0 | Verim dususu |
| I_EX,kondenser | +0.3-0.5 kW | Ek ekzojen yikim |
| I_EX,kompresor | +0.2-0.3 kW | Ek ekzojen yikim |

**Sayisal Ornek:**

```
Temel durum:
  T_wb = 24°C, T_ct_approach = 4°C
  T_cw,out = 24 + 4 = 28°C
  T_cond = 28 + 5 = 33°C → COP = 5.70

Bozulmus durum (kirli sogutma kulesi):
  T_wb = 24°C, T_ct_approach = 8°C
  T_cw,out = 24 + 8 = 32°C
  T_cond = 32 + 5 = 37°C → COP = 4.95

COP dususu: (5.70 - 4.95) / 5.70 = %13.2
Ek exergy yikimi: ~4.2 kW (tamami ekzojen)
```

### 4.3. Mevsimsel Ekzojen Etki Degisimi

Wet-bulb sicakligi mevsimlere gore degistigi icin, ekzojen exergy yikimi da mevsimsel olarak degisir:

| Mevsim | T_wb (°C) | T_cond (°C) | COP | I_EX,toplam (kW) | I_EX Degisimi |
|---|---|---|---|---|---|
| Kis | 5 | 20 | 8.2 | 1.2 | Referans |
| Ilkbahar | 15 | 28 | 6.1 | 3.0 | +150% |
| Yaz | 26 | 39 | 4.5 | 6.8 | +467% |
| Sonbahar | 18 | 31 | 5.5 | 3.8 | +217% |

**Yorum:** Yaz aylarinda ekzojen exergy yikimi kis aylarinin 5.7 katina ulasabilir. Bu durum, sogutma kulesi bakim ve optimizasyonunun ozellikle yaz oncesinde yapilmasinin onemini vurgular.

### 4.4. Sogutma Kulesi Iyilestirme Etkileri

| Iyilestirme | I_EX Azalmasi (kW) | Yillik Tasarruf (kWh) | Maliyet Sinifi |
|---|---|---|---|
| Kule dolgu malzemesi yenileme | 1.0 - 2.0 | 5,000 - 10,000 | Dusuk |
| Fan VSD eklenmesi | 0.5 - 1.0 | 2,500 - 5,000 | Orta |
| Su dagitim sistemini iyilestirme | 0.3 - 0.8 | 1,500 - 4,000 | Dusuk |
| Kule kapasitesini artirma | 1.5 - 3.0 | 7,500 - 15,000 | Yuksek |
| Serbest sogutma (free cooling) entegrasyonu | 2.0 - 5.0 | 10,000 - 25,000 | Yuksek |

## 5. Genlesme Cihazi Karsilastirmasi

### 5.1. Alternatiflerin Gelismis Exergy Karsilastirmasi

Konvansiyonel genlesme vanasi, chiller'deki en buyuk exergy yikimi kaynaklarindan biridir. Alternatif genlesme cihazlari bu kaybi onemli olcude azaltabilir.

**300 kW Chiller Icin Karsilastirma:**

| Genlesme Cihazi | I_genlesme (kW) | I_tasarruf (kW) | Geri Kazanim | Maliyet |
|---|---|---|---|---|
| Termostatik genlesme vanasi (TXV) | 9.3 | Referans | — | Referans |
| Elektronik genlesme vanasi (EEV) | 8.5 | 0.8 | — | Dusuk |
| Ejektor (Ejector) | 5.2 | 4.1 | Kinetik enerji | Orta |
| Turbo-ekspander (Turbo-expander) | 3.8 | 5.5 | Is geri kazanimi | Yuksek |
| Vortex tup (Vortex tube) | 7.1 | 2.2 | Termal ayristirma | Orta |

### 5.2. Ejektor Entegrasyonu Detayli Analiz

```
Ejektor COP iyilestirmesi:
  COP_TXV = 5.45
  COP_ejektor = 5.45 * 1.12 = 6.10  (tipik %10-15 iyilestirme)

Exergy yikimi azalmasi:
  I_TXV = 9.3 kW
  I_ejektor = 5.2 kW
  Tasarruf = 4.1 kW

Yillik enerji tasarrufu (5000 saat):
  dW = Q_sogutma * (1/COP_TXV - 1/COP_ejektor)
  dW = 300 * (1/5.45 - 1/6.10)
  dW = 300 * (0.1835 - 0.1639)
  dW = 300 * 0.0196
  dW = 5.88 kW
  Yillik = 5.88 * 5000 = 29,400 kWh
```

### 5.3. Turbo-Ekspander Detayli Analiz

```
Turbo-ekspander is geri kazanimi:
  W_geri = m_dot_ref * (h_giris - h_cikis,is) * eta_turbo
  Tipik geri kazanim: 1.5 - 3.0 kW (300 kW chiller icin)

Exergy yikimi azalmasi:
  I_TXV = 9.3 kW
  I_turbo = 3.8 kW
  Tasarruf = 5.5 kW

COP iyilestirmesi:
  COP_turbo = COP_TXV * (W_comp / (W_comp - W_geri))
  COP_turbo ≈ 5.45 * (55 / (55 - 2.2))
  COP_turbo ≈ 5.45 * 1.042
  COP_turbo ≈ 5.68

  Alternatif hesap (kapasite artisi dahil):
  COP_turbo_net ≈ 6.30 (tipik %12-18 iyilestirme)
```

## 6. Sogutucu Akiskan Seciminin Gelismis Exergy Sonuclarina Etkisi

### 6.1. Farkli Sogutucu Akiskanlarla Exergy Karsilastirmasi

Ayni calisme kosullarinda (T_evap = 5°C, T_cond = 35°C, Q = 300 kW) farkli sogutucu akiskanlar icin gelismis exergy sonuclari:

| Sogutucu Akiskan | I_total (kW) | I_AV (kW) | I_UN (kW) | theta | COP |
|---|---|---|---|---|---|
| R-134a | 35.8 | 16.6 | 19.2 | 0.464 | 5.45 |
| R-1234yf | 37.2 | 17.5 | 19.7 | 0.470 | 5.25 |
| R-1234ze(E) | 36.5 | 16.9 | 19.6 | 0.463 | 5.35 |
| R-513A | 36.0 | 16.7 | 19.3 | 0.464 | 5.42 |
| R-290 (Propan) | 34.8 | 16.0 | 18.8 | 0.460 | 5.58 |
| R-717 (Amonyak) | 33.5 | 15.2 | 18.3 | 0.454 | 5.80 |

### 6.2. Sogutucu Akiskan Secimi Karar Matrisi

```
Exergy acisından en iyi secim: R-717 (Amonyak)
  - En dusuk I_total (33.5 kW)
  - En yuksek COP (5.80)
  - ANCAK: toksisite ve yanicilik sinirlamasi (ASHRAE B2L)

Pratik en iyi secim (endustriyel): R-513A veya R-1234ze(E)
  - Dusuk GWP (< 150)
  - R-134a'ya yakin exergy performansi
  - Guvenlik sinifi A1 veya A2L
  - Mevcut ekipmanla uyumluluk
```

### 6.3. Sogutucu Akiskan Bazli Alt Bilesen Exergy Dagılimi

R-134a vs R-717 (Amonyak) karsilastirmasi — alt bilesen exergy yikimi dagilimi:

| Alt Bilesen | R-134a I_total (kW) | R-717 I_total (kW) | Fark (%) |
|---|---|---|---|
| Kompresor | 12.5 | 10.8 | -13.6% |
| Kondenser | 8.2 | 7.5 | -8.5% |
| Evaporator | 5.8 | 5.2 | -10.3% |
| Genlesme vanasi | 9.3 | 10.0 | +7.5% |
| **Toplam** | **35.8** | **33.5** | **-6.4%** |

**Yorum:** Amonyak, kompresor ve isi degistiricilerinde daha dusuk exergy yikimi saglarken, genlesme vanasinda biraz daha yuksek yikim gosterir. Net etki %6.4 exergy tasarrufudur.

## 7. Kismi Yuk Performansi ve VSD Etkisi

### 7.1. Kismi Yuk Exergy Analizi

Chiller'lar nadiren tam yukde calisir. Kismi yuk performansi, yillik bazda gercek exergy tasarruf potansiyelini belirler.

**Yuk Profiline Gore Exergy Yikimi (300 kW Chiller):**

| Yuk Orani (%) | Q_sogutma (kW) | W_sabit_hiz (kW) | COP_sabit | I_total (kW) | W_VSD (kW) | COP_VSD | I_total_VSD (kW) |
|---|---|---|---|---|---|---|---|
| 100 | 300 | 55.0 | 5.45 | 35.8 | 55.0 | 5.45 | 35.8 |
| 75 | 225 | 44.5 | 5.06 | 30.3 | 36.0 | 6.25 | 19.8 |
| 50 | 150 | 34.0 | 4.41 | 24.2 | 20.5 | 7.32 | 9.3 |
| 25 | 75 | 25.0 | 3.00 | 20.3 | 11.2 | 6.70 | 5.8 |

### 7.2. VSD Etkisinin Gelismis Exergy Analizi

VSD eklenmesi, ozellikle kismi yukde kacinilabilir exergy yikimini onemli olcude azaltir:

```
VSD olmadan (sabit hiz), %50 yukde:
  I_total = 24.2 kW
  I_AV = 11.2 kW (theta = 0.463)
  I_UN = 13.0 kW

VSD ile, %50 yukde:
  I_total = 9.3 kW
  I_AV = 2.1 kW (theta = 0.226)
  I_UN = 7.2 kW
```

**Yorum:** VSD eklenmesiyle %50 yukde exergy yikimi %62 azalmistir. Theta degeri 0.463'ten 0.226'ya duserek, VSD'li sistemin termodinamik limitine daha yakin calistigini gostermektedir.

### 7.3. Yillik Baz Exergy Tasarrufu Hesabi

Tipik bir yuk profili kullanarak yillik bazda hesaplama:

```
Yillik calısma saatleri: 5000 saat
Yuk dagilimi:
  - %100 yuk: 500 saat (%10)
  - %75 yuk:  1500 saat (%30)
  - %50 yuk:  2000 saat (%40)
  - %25 yuk:  1000 saat (%20)

VSD olmadan yillik exergy yikimi:
  I_yillik = 35.8*500 + 30.3*1500 + 24.2*2000 + 20.3*1000
  I_yillik = 17,900 + 45,450 + 48,400 + 20,300
  I_yillik = 132,050 kWh

VSD ile yillik exergy yikimi:
  I_yillik_VSD = 35.8*500 + 19.8*1500 + 9.3*2000 + 5.8*1000
  I_yillik_VSD = 17,900 + 29,700 + 18,600 + 5,800
  I_yillik_VSD = 72,000 kWh

Yillik exergy tasarrufu: 132,050 - 72,000 = 60,050 kWh
Tasarruf orani: %45.5
```

## 8. Adim Adim Hesaplama Rehberi

### 8.1. Tam Hesaplama Proseduru

Chiller icin ileri exergy analizinin eksiksiz uygulamasi icin asagidaki adimlar izlenir:

**Adim 1 — Sistem Verilerinin Toplanmasi:**

```
Gerekli veriler:
1. Q_sogutma (kW) — Sogutma kapasitesi
2. W_kompresor (kW) — Elektrik tuketimi
3. T_evap (°C) — Evaporasyon sicakligi
4. T_cond (°C) — Kondensasyon sicakligi
5. T_cw,in (°C) — Kondenser sogutma suyu giris
6. T_cw,out (°C) — Kondenser sogutma suyu cikis
7. T_chw,in (°C) — Soguk su giris
8. T_chw,out (°C) — Soguk su cikis
9. T_0 (°C) — Cevre sicakligi
10. Sogutucu akiskan tipi
```

**Adim 2 — Konvansiyonel Exergy Analizi:**

```
a) COP = Q_sogutma / W_kompresor
b) COP_Carnot = T_evap / (T_cond - T_evap)  [K cinsinden]
c) eta_II = COP / COP_Carnot
d) E_P = Q_sogutma * |1 - T_0/T_evap|  [K cinsinden]
e) I_total = W_kompresor - E_P
```

**Adim 3 — BAT Kosullarinin Belirlenmesi:**

```
a) COP_UN = COP_Carnot * 0.65  [santrifuj icin]
b) Kompresor: eta_is,UN = 0.90
c) Evaporator approach: dT_evap,UN = 3°C
d) Kondenser approach: dT_cond,UN = 3°C
e) Basinc dusumu: dP/P = %2
```

**Adim 4 — Kacinılamaz Exergy Yikimi Hesabi:**

```
a) W_UN = Q_sogutma / COP_UN
b) I_UN = W_UN - E_P
c) I_AV = I_total - I_UN
d) theta = I_AV / I_total
```

**Adim 5 — Alt Bilesen Bazli Dekompozisyon:**

```
Her alt bilesen (k = kompresor, kondenser, evaporator, genlesme) icin:
a) Hibrit cevrim olustur: bilesen k gercek, digerileri ideal
b) I_EN,k = Hibrit cevrimdeki bilesen k'nin exergy yikimi
c) I_EX,k = I_total,k - I_EN,k
d) BAT kosullarini uygulayarak I_UN,k hesapla
e) I_AV,k = I_total,k - I_UN,k
f) Dort bilesen: I_EN_AV, I_EN_UN, I_EX_AV, I_EX_UN
```

**Adim 6 — Sogutma Kulesi Ekzojen Etki Hesabi:**

```
a) Mevcut sogutma kulesi approach degerini ol (T_ct_approach)
b) BAT sogutma kulesi approach = 3°C
c) dT_excess = T_ct_approach - 3
d) I_EX,sogutma_kulesi ≈ dT_excess * 0.4 kW/°C  [300 kW chiller icin tipik]
```

**Adim 7 — Onceliklendirme ve Raporlama:**

```
a) Alt bilesenleri I_EN_AV'ye gore sirala (en yuksek = en oncelikli)
b) Ekzojen etkileri tanimla ve kaynaklarina gore grupla
c) Yillik enerji ve maliyet tasarrufunu hesapla
d) Yatirim gerektiren ve gerektirmeyen iyilestirmeleri ayir
e) Sonuclari tablo ve grafik olarak raporla
```

### 8.2. Hizli Degerlendirme Formulleri

Detayli alt bilesen analizi yapilamadigi durumlarda, asagidaki ampirik formuller hizli tahmin icin kullanilabilir:

```
Santrifuj chiller icin:
  theta ≈ 0.35 + 0.20 * (1 - COP/COP_Carnot)
  I_AV ≈ I_total * theta
  I_AV_kompresor ≈ I_AV * 0.35
  I_AV_genlesme ≈ I_AV * 0.30
  I_AV_kondenser ≈ I_AV * 0.20
  I_AV_evaporator ≈ I_AV * 0.15
```

## 9. ExergyLab Platformunda Kullanim

ExergyLab, chiller ileri exergy analizini asagidaki sekilde uygular:

1. Kullanici chiller calisme verilerini girer (Q, W, T_evap, T_cond)
2. Engine konvansiyonel exergy analizini hesaplar
3. Chiller tipi bazinda BAT veritabanindan COP_UN degeri cekilir
4. Alt bilesen bazli dekompozisyon yaklasik ampirik formullerle hesaplanir
5. Sogutma kulesi verileri varsa ekzojen etki analizi eklenir
6. AI yorumlama motoru, sonuclari bu dosyadaki bilgilerle harmanlayarak yorum uretir
7. Onceliklendirme ve aksiyon plani olusturulur

## İlgili Dosyalar

- `knowledge/factory/advanced_exergy/avoidable_unavoidable.md` — Kacinilabilir/kacinılamaz temel metodoloji
- `knowledge/factory/advanced_exergy/endogenous_exogenous.md` — Endojen/ekzojen temel metodoloji
- `knowledge/chiller/formulas.md` — Chiller exergy hesaplama formulleri
- `knowledge/chiller/benchmarks.md` — Chiller verimlilik benchmarklari
- `knowledge/chiller/equipment/centrifugal.md` — Santrifuj chiller detaylari
- `knowledge/chiller/equipment/screw.md` — Vidali chiller detaylari
- `knowledge/chiller/equipment/refrigerants.md` — Sogutucu akiskan bilgileri
- `knowledge/chiller/solutions/vsd.md` — VSD uygulama rehberi
- `knowledge/chiller/solutions/condenser_optimization.md` — Kondenser optimizasyonu
- `knowledge/factory/cross_equipment.md` — Capraz ekipman exergy entegrasyonu
- `knowledge/factory/waste_heat_recovery.md` — Atik isi geri kazanim teknolojileri
- `skills/equipment/chiller_expert.md` — Chiller AI uzman beceri dosyasi

## Referanslar

1. Morosuk, T. & Tsatsaronis, G. (2008). "A new approach to the exergy analysis of absorption refrigeration machines." *Energy*, 33(6), 890-907. DOI: 10.1016/j.energy.2007.09.012

2. Morosuk, T. & Tsatsaronis, G. (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258. DOI: 10.1016/j.energy.2009.10.005

3. Tsatsaronis, G. & Park, M.-H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. DOI: 10.1016/S0196-8904(02)00012-2

4. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. DOI: 10.1016/j.energy.2008.12.007

5. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. John Wiley & Sons, New York. ISBN: 978-0-471-58467-4

6. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. DOI: 10.1016/j.energy.2011.05.028

7. Erbay, Z. & Hepbasli, A. (2017). "Advanced exergoeconomic analysis of a heat pump food dryer." *Biosystems Engineering*, 154, 53-66. DOI: 10.1016/j.biosystemseng.2016.10.003
