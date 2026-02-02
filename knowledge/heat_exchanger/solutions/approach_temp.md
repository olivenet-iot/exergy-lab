---
title: "Yaklasim Sicakligi Optimizasyonu (Approach Temperature Optimization)"
category: solution
equipment_type: heat_exchanger
keywords: [approach temperature, yaklasim sicakligi, pinch analizi, LMTD, yuzey alani, exergy]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/audit.md, factory/pinch_analysis.md]
use_when: ["DT_approach yuksek oldugunda", "Esanjor yuzey alani optimizasyonu yapilirken", "Pinch analizi ile entegrasyon planlanirken"]
priority: high
last_updated: 2026-02-01
---
# Yaklasim Sicakligi Optimizasyonu (Approach Temperature Optimization)

> Son guncelleme: 2026-02-01

## Ozet

**Problem:** Isi esanjorlerinde yaklasim sicakligi (approach temperature, DT_approach) isi transfer surucu kuvvetini belirler. Yuksek yaklasim sicakligi dusuk yuzey alani (dusuk yatirim) ancak yuksek exergy yikimi anlamina gelir. Dusuk yaklasim sicakligi ise yuksek exergy verimi saglar ancak buyuk yuzey alani gerektirir.

**Cozum:** Ekonomik optimum yaklasim sicakligini belirleyerek yatirim maliyeti ile enerji maliyeti arasindaki en iyi dengeyi bulmak. Pinch analizi ile fabrika genelinde sistematik optimizasyon.

**Tipik Tasarruf:** %5-25 (enerji maliyetlerinde azalma)
**Tipik ROI:** 1-4 yil

## Yaklasim Sicakligi Tanimi

### Karsi Akis (Counterflow) Esanjor

```
DT_approach = T_hot_out - T_cold_in

Burada:
  DT_approach = Yaklasim sicakligi [C]
  T_hot_out   = Sicak akiskan cikis sicakligi [C]
  T_cold_in   = Soguk akiskan giris sicakligi [C]
```

### Paralel Akis (Parallel Flow) Esanjor

```
DT_approach = T_hot_out - T_cold_out

Not: Paralel akista yaklasim sicakligi her zaman karsi akisa gore daha buyuktur;
     bu nedenle paralel akis termal olarak daha az verimlidir.
```

### Capraz Akis (Crossflow) ve Cok Gecisli (Multi-pass)

Capraz akis ve cok gecisli esanjorlerde yaklasim sicakligi LMTD duzeltme faktoru (F) ile birlikte degerlendirilir:

```
Q = U x A x F x LMTD_counterflow

F = LMTD_actual / LMTD_counterflow  (0 < F <= 1)
```

F < 0.75 durumunda esanjor tasarimi verimsizdir ve yeniden degerlendirilmelidir.

## Yaklasim Sicakligi ve Yuzey Alani Iliskisi

Yaklasim sicakligi azaldikca logaritmik ortalama sicaklik farki (LMTD) duser ve gerekli yuzey alani artar:

```
A = Q / (U x LMTD)

LMTD = (DT_1 - DT_2) / ln(DT_1 / DT_2)

Karsi akis icin:
  DT_1 = T_hot_in - T_cold_out
  DT_2 = T_hot_out - T_cold_in = DT_approach
```

### Sayisal Ornek: Yuzey Alani Degisimi

Kosullar: Q = 500 kW, U = 1,500 W/(m2-K), T_hot_in = 120 C, T_cold_in = 30 C, T_cold_out = 80 C

| DT_approach (C) | T_hot_out (C) | DT_1 (C) | DT_2 (C) | LMTD (C) | A (m2) | Goreli Maliyet |
|------------------|---------------|-----------|-----------|-----------|--------|----------------|
| 40 | 70 | 40 | 40 | 40.0 | 8.3 | 1.00x |
| 30 | 60 | 40 | 30 | 34.8 | 9.6 | 1.15x |
| 20 | 50 | 40 | 20 | 28.9 | 11.5 | 1.39x |
| 15 | 45 | 40 | 15 | 25.5 | 13.1 | 1.58x |
| 10 | 40 | 40 | 10 | 21.6 | 15.4 | 1.86x |
| 5 | 35 | 40 | 5 | 16.4 | 20.3 | 2.45x |

**Gozlem:** DT_approach 40 C'den 5 C'ye indirildiginde yuzey alani 2.45 kat artar, ancak sicak akiskandan %30 daha fazla isi geri kazanilir (T_hot_out 70 C -> 35 C).

## Ekonomik Optimum Yaklasim Sicakligi

### Maliyet Fonksiyonu

```
C_total = C_capital + C_energy

C_capital = a x A^n  [EUR/yil] (amortisman dahil)
C_energy = Q_kayip x t_isletme x c_enerji  [EUR/yil]

Burada:
  a = Maliyet katsayisi (malzeme, tip, basinca bagli) [EUR/m2^n]
  n = Maliyet ussu (tipik 0.6-0.8, economy of scale)
  A = Yuzey alani [m2]
  Q_kayip = Geri kazanilamayan isi [kW]
  t_isletme = Yillik calisma suresi [saat/yil]
  c_enerji = Birim enerji maliyeti [EUR/kWh]
```

### Optimal Nokta

Optimal yaklasim sicakligi, toplam yillik maliyetin minimumunda bulunur:

```
dC_total / d(DT_approach) = 0

Pratik kural:
  DT_approach_optimal = f(enerji_maliyeti, esanjor_maliyeti, calisma_suresi)
```

| Endüstri | Tipik Optimal DT_approach | Gerekce |
|----------|---------------------------|---------|
| Petrol rafineleri | 10-20 C | Yuksek enerji yogunlugu, surekli isletme |
| Kimya endustrisi | 10-25 C | Proses sicaklik hassasiyeti |
| Gida endustrisi | 5-15 C | Yuksek calisma suresi, enerji maliyeti |
| HVAC | 3-8 C | Dusuk sicaklik farklari, buyuk debiler |
| Enerji uretimi | 5-15 C | Yuksek calisma suresi, verim kritik |
| Kriyojenik | 1-5 C | Cok yuksek enerji degeri |

### Enerji Maliyetinin Etkisi

| Enerji Maliyeti (EUR/kWh) | Onerilen DT_approach Araligi | Aciklama |
|----------------------------|-------------------------------|----------|
| <0.03 | 20-40 C | Dusuk enerji maliyeti, buyuk DT kabul edilebilir |
| 0.03-0.06 | 10-25 C | Orta enerji maliyeti |
| 0.06-0.10 | 5-15 C | Yuksek enerji maliyeti, kucuk DT tercih |
| >0.10 | 3-10 C | Cok yuksek enerji maliyeti, minimum DT hedef |

## Exergy Verimi ile Iliskisi

Yaklasim sicakligi kuculdukce isi transferi sicaklik farki azalir ve entropi uretimi duser:

```
Entropi uretim hizi:
  S_gen = Q x (1/T_c - 1/T_h) [kW/K]

Exergy yikim hizi:
  Ex_d = T_0 x S_gen = T_0 x Q x (1/T_c - 1/T_h) [kW]

Exergy verimi:
  eta_ex = 1 - Ex_d / Ex_in
```

### Yaklasim Sicakligi ve Exergy Verimi Tablosu

Kosullar: Q = 500 kW, T_hot_in = 120 C, T_cold_in = 30 C, T_0 = 25 C (298 K)

| DT_approach (C) | T_hot_out (C) | Ortalama DT (C) | Ex_d (kW) | eta_ex (%) |
|------------------|---------------|------------------|-----------|------------|
| 40 | 70 | 35.0 | 42.3 | 52.8 |
| 30 | 60 | 27.5 | 33.9 | 62.2 |
| 20 | 50 | 22.5 | 26.1 | 70.9 |
| 15 | 45 | 20.0 | 22.5 | 74.9 |
| 10 | 40 | 17.5 | 18.4 | 79.5 |
| 5 | 35 | 15.0 | 13.8 | 84.6 |

**Sonuc:** DT_approach 40 C'den 10 C'ye dusuruldugunde exergy verimi %52.8'den %79.5'e yukselir — yaklasik %27 mutlak iyilesme.

## Pinch Analizi Baglantisi

### DT_min ve Isi Geri Kazanim Arasindaki Iliski

Pinch analizinde DT_min (minimum yaklasim sicakligi) secimi fabrika genelindeki isi geri kazanim miktarini dogrudan etkiler:

```
DT_min artarsa:
  - Gerekli esanjor yuzey alani azalir (dusuk yatirim)
  - Maksimum isi geri kazanim (Q_recovery_max) azalir
  - Dis enerji ihtiyaci (Q_H_min, Q_C_min) artar

DT_min azalirsa:
  - Gerekli esanjor yuzey alani artar (yuksek yatirim)
  - Maksimum isi geri kazanim artar
  - Dis enerji ihtiyaci azalir
```

### Kompozit Egriler (Composite Curves)

Sicak ve soguk kompozit egriler, tum proses akimlarinin entalpiye karsi sicaklik grafiginde birlestirilmesidir:

```
Sicak kompozit egri: Tum sicak akimlarin birlestirilerek
  sicakliktan entalpiye (T-H) olarak cizilmesi

Soguk kompozit egri: Tum soguk akimlarin birlestirilerek
  sicakliktan entalpiye (T-H) olarak cizilmesi

Pinch noktasi: Iki egrinin en yakin oldugu nokta
  DT_min = (T_hot - T_cold) pinch noktasinda
```

### Buyuk Kompozit Egri (Grand Composite Curve — GCC)

GCC, net isi acigini sicakliga karsi gosterir ve optimal isi yardimci ekipman secimini yonlendirir:

- **Pinch ustu (above pinch):** Dis isitma (kazan, vb.) gerekli — sadece isi verici (heat sink) esanjorleri
- **Pinch alti (below pinch):** Dis sogutma (sogutma kulesi, vb.) gerekli — sadece isi alici (heat source) esanjorleri
- **Cep (pocket) bolgeleri:** Proses ici isi degisimi ile karsilanabilir — esanjor firsatlari

### Fabrika Geneli DT_min Secimi

| DT_min (C) | Q_recovery | Q_H_min | Q_C_min | Esanjor Alani | Toplam Yatirim | Yillik Enerji |
|-------------|------------|---------|---------|---------------|----------------|---------------|
| 30 | 2,500 kW | 1,800 kW | 1,200 kW | 450 m2 | €180,000 | €650,000 |
| 20 | 3,200 kW | 1,100 kW | 500 kW | 680 m2 | €270,000 | €400,000 |
| 10 | 3,800 kW | 500 kW | 100 kW | 1,200 m2 | €480,000 | €180,000 |

**Not:** Yukaridaki tablo bir gida fabrikasi icin ornek degerlerdir. Optimal DT_min genellikle 10-25 C arasindadir.

## Sayisal Optimizasyon Ornegi

### Senaryo: Proses Isi Esanjoru Yenileme

Mevcut durum:
- 50 m2 govde-boru esanjor, U = 800 W/(m2-K)
- T_hot_in = 150 C, T_hot_out = 90 C, T_cold_in = 25 C, T_cold_out = 70 C
- DT_approach = 90 - 25 = 65 C (yuksek)
- Q = 300 kW, calisma: 7,500 saat/yil

Hedef: DT_approach'u optimize et

**Secenek 1: DT_approach = 40 C (T_hot_out = 65 C)**
```
Q_yeni = m_hot x Cp x (150 - 65) = 398 kW (ilave 98 kW geri kazanim)
LMTD = (80 - 40) / ln(80/40) = 57.7 C
A_gerekli = 398,000 / (800 x 57.7) = 8.6 m2 ek alan
Ek esanjor maliyeti: €12,000
Yillik enerji tasarrufu: 98 x 7,500 x 0.045 = €33,075/yil
Geri odeme: 12,000 / 33,075 = 0.36 yil
```

**Secenek 2: DT_approach = 20 C (T_hot_out = 45 C)**
```
Q_yeni = m_hot x Cp x (150 - 45) = 525 kW (ilave 225 kW geri kazanim)
LMTD = (80 - 20) / ln(80/20) = 43.3 C
A_gerekli = 525,000 / (800 x 43.3) = 15.2 m2 ek alan
Ek esanjor maliyeti: €22,000
Yillik enerji tasarrufu: 225 x 7,500 x 0.045 = €75,938/yil
Geri odeme: 22,000 / 75,938 = 0.29 yil
```

**Secenek 3: DT_approach = 10 C (T_hot_out = 35 C)**
```
Q_yeni = m_hot x Cp x (150 - 35) = 575 kW (ilave 275 kW geri kazanim)
LMTD = (80 - 10) / ln(80/10) = 33.7 C
A_gerekli = 575,000 / (800 x 33.7) = 21.3 m2 ek alan
Ek esanjor maliyeti: €32,000
Yillik enerji tasarrufu: 275 x 7,500 x 0.045 = €92,813/yil
Geri odeme: 32,000 / 92,813 = 0.34 yil
```

**Karar:** Her uc secenek de hizli geri odemeye sahip. Secenek 2 (DT_approach = 20 C) en iyi geri odemeye sahipken, Secenek 3 (DT_approach = 10 C) en yuksek mutlak tasarrufu saglar. Yuzey alani kisitina gore karar verilmelidir.

## Uygulama Adimlari

1. **Mevcut durum analizi:** Tum esanjorlerin mevcut yaklasim sicakliklarini olc ve kaydet
2. **Pinch analizi:** Fabrika geneli sicak ve soguk akimlari belirle, kompozit egrileri ciz
3. **Hedef belirleme:** DT_min secimi ile teorik minimum enerji tuketimini hesapla
4. **Maliyet analizi:** Her esanjor icin yuzey alani artisi ve enerji tasarrufunu karsilastir
5. **Optimizasyon:** Toplam yillik maliyeti minimize eden DT_approach degerini belirle
6. **Onceliklendirme:** En yuksek tasarruf/yatirim oranina sahip esanjorlerden basla
7. **Tasarim:** Secilen DT_approach icin esanjor boyutlandirmasi yap
8. **Uygulama:** Esanjor degisimi veya ek yuzey alan eklemesi yap
9. **Dogrulama:** Yeni sicaklik olcumleri ile performansi dogrula

## İlgili Dosyalar

- Isi esanjoru exergy formulleri: `heat_exchanger/formulas.md`
- Benchmark verileri ve U-deger araliklari: `heat_exchanger/benchmarks.md`
- Kirlenme yonetimi: `heat_exchanger/solutions/fouling_management.md`
- Basinc dususu optimizasyonu: `heat_exchanger/solutions/pressure_drop.md`
- Isi geri kazanim uygulamalari: `heat_exchanger/solutions/heat_recovery.md`
- Fabrika pinch analizi: `factory/pinch_analysis.md`
- Fabrika isi entegrasyonu: `factory/heat_integration.md`
- Fabrika proses entegrasyonu: `factory/process_integration.md`
- Fabrika ekonomik analiz: `factory/economic_analysis.md`

## Referanslar

- Linnhoff, B., et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1982
- Kemp, I.C., "Pinch Analysis and Process Integration," 2nd Edition, Butterworth-Heinemann, 2007
- Smith, R., "Chemical Process Design and Integration," 2nd Edition, Wiley, 2016
- Shenoy, U.V., "Heat Exchanger Network Synthesis: Process Optimization by Energy and Resource Analysis," Gulf Publishing, 1995
- Townsend, D.W. and Linnhoff, B., "Heat and Power Networks in Process Design," AIChE Journal, 1983
- ESDU, "Heat Exchanger Fouling in the Pre-Heat Train of a Crude Oil Distillation Unit"
- Bejan, A., "Entropy Generation Through Heat and Fluid Flow," Wiley, 1982 — Chapter 4
- Yilmaz, M., Sara, O.N., Karsli, S., "Performance Evaluation Criteria for Heat Exchangers Based on Second Law Analysis," Exergy Int. J., 2001
- TEMA, "Standards of the Tubular Exchanger Manufacturers Association," 10th Edition
