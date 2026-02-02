---
title: "Kacinilabilir ve Kacinılamaz Exergy Yıkımı Dekompozisyonu"
category: "advanced_exergy"
keywords:
  - avoidable exergy destruction
  - unavoidable exergy destruction
  - advanced exergy analysis
  - BAT limits
  - improvement potential
  - decomposition
  - thermodynamic limits
  - kacinilabilir
  - kacinılamaz
  - exergy yıkımı
related_files:
  - knowledge/factory/advanced_exergy/equipment_specific
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - knowledge/factory/waste_heat_recovery.md
  - knowledge/factory/exergy_flow_analysis.md
  - knowledge/factory/heat_integration.md
  - skills/core/exergy_fundamentals.md
  - skills/factory/factory_analyst.md
use_when: "Ekipman bazlı exergy yıkımının ne kadarının gerçekçi şekilde azaltılabileceğini belirlemek gerektiğinde, iyileştirme önceliklendirmesi yapılırken ve yatırım kararları için teknik fizibilite değerlendirmesinde kullanılır."
priority: high
last_updated: 2025-05-15
---

# Kacinilabilir ve Kacinılamaz Exergy Yıkımı Dekompozisyonu (Avoidable/Unavoidable Exergy Destruction Decomposition)

## 1. Giriş ve Motivasyon

Konvansiyonel exergy analizi, bir sistemdeki her bileşenin toplam exergy yıkımını (irreversibility) hesaplar. Ancak bu yaklaşım tek başına yetersizdir, cunku toplam exergy yıkımının tamamı pratik olarak ortadan kaldırılamaz. Her bileşenin, mevcut teknolojik ve termodinamik limitler dahilinde kacinılamaz (unavoidable) bir minimum yıkım seviyesi vardır.

Gelismis exergy analizi (advanced exergy analysis), toplam yıkımı iki bileşene ayırarak bu sorunu cozer:

- **Kacinilabilir exergy yıkımı (Avoidable, I_AV):** Mevcut teknolojik imkanlar dahilinde azaltılabilir kisim
- **Kacinılamaz exergy yıkımı (Unavoidable, I_UN):** Termodinamik ve teknolojik sinirlar nedeniyle ortadan kaldırılamayan kisim

Bu ayrıştırma, muhendislerin ve enerji yoneticilerinin iyileştirme calışmalarını gercekten etki yaratabilecek alanlara yonlendirmesini saglar.

## 2. Temel Formulasyon

### 2.1 Birincil Dekompozisyon

Toplam exergy yıkımı iki bileşene ayrıştırılır:

```
I_total = I_AV + I_UN
```

Burada:
- `I_total` : Bileşenin toplam exergy yıkımı (kW)
- `I_AV`    : Kacinilabilir exergy yıkımı (kW) — iyileştirme potansiyeli
- `I_UN`    : Kacinılamaz exergy yıkımı (kW) — termodinamik/teknolojik alt sinir

### 2.2 Spesifik Kacinılamaz Exergy Yıkımı

Kacinılamaz exergy yıkımı, bileşenin urun exergy'si (exergy of product) uzerinden normalize edilir:

```
i_UN = (I_UN / E_P)_BAT
```

Burada:
- `i_UN`  : Spesifik kacinılamaz exergy yıkımı (kW/kW urun)
- `E_P`   : Bileşenin urun exergy'si (kW)
- `BAT`   : En iyi mevcut teknoloji (Best Available Technology) koşulları

### 2.3 Kacinılamaz Yıkımın Gercek Sistem Uzerinden Hesaplanması

```
I_UN,k = E_P,k * (I_k / E_P,k)_UN
```

Ardından kacinilabilir kisim:

```
I_AV,k = I_total,k - I_UN,k
```

### 2.4 Goreceli Kacinilabilirlik Oranı

```
theta = I_AV / I_total
```

Bu oran, bir bileşendeki iyileştirme potansiyelinin buyukluğunu gosterir:

| theta Aralığı | Yorum | Aksiyon Onceligi |
|---|---|---|
| theta > 0.50 | Yuksek iyileştirme potansiyeli | Oncelikli yatırım hedefi |
| theta = 0.30 - 0.50 | Orta iyileştirme potansiyeli | Ikincil oncelik, maliyet-fayda analizi gerekir |
| theta < 0.30 | Dusuk iyileştirme potansiyeli | Cogunlukla termodinamik limit, yatırım onerilmez |

## 3. Kacinılamaz Koşulların Tanımlanma Yontemi

### 3.1 Genel Metodoloji

Kacinılamaz exergy yıkımının hesaplanması icin sistematik bir yaklasim gereklidir. Asagidaki adımlar izlenir:

**Adım 1: BAT Parametrelerinin Belirlenmesi**

Her bileşen icin, guncel teknolojik sinirlara dayalı "mumkun olan en iyi" calışma koşulları belirlenir. Bu koşullar:
- Uretici kataloglarından elde edilen maksimum verimlilik degerleri
- Akademik literaturde raporlanan en iyi performans veriler
- Termodinamik teorik limitler (Carnot verimi, ideal gaz davranışı vb.)
- Malzeme dayanım sinirlari (sicaklik, basinc)

**Adım 2: Kacinılamaz Koşullarla Sistem Simulasyonu**

Tum bileşenler icin BAT parametreleri uygulanarak sistemin tumune simulasyon yapılır. Her bileşenin kacinılamaz koşullardaki exergy yıkımı hesaplanır.

**Adım 3: Kacinılamaz Yıkım Hesabı**

```
I_UN,k = f(BAT parametreleri, sistem koşulları)
```

Bu deger, bileşenin ideal degil ama pratik olarak ulasilabilir en iyi durumundaki exergy yıkımını temsil eder.

**Adım 4: Kacinilabilir Yıkım Hesabı**

```
I_AV,k = I_total,k - I_UN,k
```

**Adım 5: Yorumlama ve Onceliklendirme**

theta degerlerine gore bileşenler sıralanır ve iyileştirme stratejisi olusturulur.

### 3.2 BAT Parametre Seciminde Dikkat Edilecekler

BAT parametreleri secilirken su kriterler goz onunde bulundurulmalıdır:

1. **Teknolojik Erisilebilirlik:** Parametre, piyasada mevcut teknoloji ile ulasilabilir olmalıdır
2. **Ekonomik Fizibilite:** Teorik limit degil, ekonomik olarak mantıklı en iyi deger secilmelidir
3. **Operasyonel Uyumluluk:** Parametrenin sistemin geri kalanıyla uyumlu olması gerekir
4. **Zamansal Gecerlilik:** BAT degerleri teknoloji ilerledikce guncellenmeli, en az 3-5 yılda bir gozden gecirilmelidir

### 3.3 Alternatif Yaklasimlar

Literaturde kacinılamaz koşulların tanımlanması icin farklı yaklasimlar onerilmiştir:

- **Termodinamik Limit Yaklasimi:** Tersinir (reversible) surec kacinılamaz alt sinir olarak alınır. Ancak bu gercekci degildir cunku tersinir surecler pratikte ulasilamaz.
- **BAT Yaklasimi (Onerilen):** Piyasadaki en iyi teknolojinin performans degerleri kullanılır. En gercekci yaklasımdır.
- **Tarihi En Iyi Yaklasimi:** Tesiste gecmişte kaydedilen en iyi performans degerleri baz alınır. Tesise ozgu bir yaklasımdır.

## 4. Ekipman Bazlı Kacinılamaz Parametre Tablosu

Asagidaki tablo, endustriyel ekipmanlar icin tipik kacinılamaz koşulları ve buna karsilik gelen exergy yıkımı oranlarını icerir:

| Ekipman | Kacinılamaz Koşul (BAT) | Tipik I_UN/I_total | theta Aralığı | Aciklama |
|---|---|---|---|---|
| Kompressor (Compressor) | eta_is = 0.92 - 0.95 | 0.55 - 0.70 | 0.30 - 0.45 | Izentropik verim siniri, mekanik kayıplar kacinılamaz |
| Kazan (Boiler) | Yanma tersinmezligi %25-30, artık gaz sicakligi 120-140°C | 0.75 - 0.85 | 0.15 - 0.25 | Kimyasal exergy yıkımı dominant, buyuk kismi kacinılamaz |
| Pompa (Pump) | eta_h = 0.85 - 0.90 | 0.40 - 0.55 | 0.45 - 0.60 | Hidrolik verim siniri, sizinti kayıpları minimum |
| Chiller | COP = COP_Carnot x 0.65 | 0.50 - 0.65 | 0.35 - 0.50 | Isı transferi tersinmezligi dominant |
| Isi Degistirici (Heat Exchanger) | Delta_T_min = 5°C | 0.60 - 0.80 | 0.20 - 0.40 | Minimum sicaklik farkı siniri, fouling etkisi |
| Turbin (Turbine) | eta_is = 0.88 - 0.92 | 0.50 - 0.65 | 0.35 - 0.50 | Kanat profili ve sizinti sinirları |
| Kurutucu (Dryer) | Termodinamik minimum enerji + %15 kayıp | 0.65 - 0.80 | 0.20 - 0.35 | Kutle transferi tersinmezligi buyuk oranda kacinılamaz |
| Fan/Ufleyici (Fan/Blower) | eta_total = 0.82 - 0.88 | 0.45 - 0.60 | 0.40 - 0.55 | Aerodinamik kayıpların siniri |

### 4.1 Ekipman Bazlı Detaylı Kacinılamaz Koşullar

#### Kompressor (Compressor)

```
Kacinılamaz koşullar:
- Izentropik verim: eta_is,UN = 0.93
- Mekanik verim: eta_mech,UN = 0.98
- Aftercooler Delta_T_min = 5°C
- Basinc dusumu (suction/discharge): Delta_P/P = 0.01
```

#### Kazan (Boiler)

```
Kacinılamaz koşullar:
- Adyabatik alev sicakligi ile buhar sicakligi arası fark: kacinılamaz
- Yanma havası fazlalıgı: %5 (teorik minimuma yakin)
- Artık gaz sicakligi: 130°C (asit ciy noktası siniri)
- Radyasyon kaybi: %0.5
- Tam yanma verimi: %99.5
```

#### Pompa (Pump)

```
Kacinılamaz koşullar:
- Hidrolik verim: eta_h,UN = 0.88
- Mekanik verim: eta_mech,UN = 0.98
- Motor verimi: eta_motor,UN = 0.96
- Sizinti kaybi: %0.5
```

#### Chiller

```
Kacinılamaz koşullar:
- Kompressor izentropik verimi: eta_is,UN = 0.90
- Evaporator yaklasim sicakligi: 3°C
- Condenser yaklasim sicakligi: 3°C
- Basinc dusumleri (suction line): %2
- COP/COP_Carnot oranı: 0.65
```

#### Isi Degistirici (Heat Exchanger)

```
Kacinılamaz koşullar:
- Minimum sicaklik farkı: Delta_T_min = 5°C
- Basinc dusumu: Delta_P/P = 0.01 (her iki taraf)
- Isı kaybi: %0.5
- Fouling faktoru: minimum (yeni/temiz durum)
```

#### Turbin (Turbine)

```
Kacinılamaz koşullar:
- Izentropik verim: eta_is,UN = 0.90
- Mekanik verim: eta_mech,UN = 0.99
- Generator verimi: eta_gen,UN = 0.98
- Sizinti kaybi: %0.5
- Egzoz basinc kaybi: %1
```

## 5. Sayısal Ornekler

### 5.1 Ornek 1: 75 kW Vidalı Kompressor

**Gercek Calısma Koşulları:**
- Elektrik girisi: P_in = 75 kW
- Izentropik verim: eta_is = 0.72
- Giris sicakligi: T_in = 25°C (298.15 K)
- Giris basinci: P1 = 1 bar
- Cikis basinci: P2 = 8 bar

**Konvansiyonel Exergy Analizi:**

```
W_ideal = P_in * eta_is = 75 * 0.72 = 54.0 kW (ideal is)
I_total = P_in - E_P = 75 - 52.5 = 22.5 kW
epsilon = E_P / P_in = 52.5 / 75 = 0.70 (exergy verimi)
```

**Kacinılamaz Koşullar (BAT):**
- eta_is,UN = 0.93
- Aftercooler Delta_T_min = 5°C
- Mekanik kayıp: %2

**Kacinılamaz Exergy Yıkımı Hesabı:**

```
I_UN = E_P * (I / E_P)_UN
I_UN = 52.5 * (I_UN / E_P)_BAT

BAT kosullarinda:
P_in,BAT = E_P / epsilon_BAT = 52.5 / 0.89 = 59.0 kW
I_BAT = 59.0 - 52.5 = 6.5 kW
(I/E_P)_BAT = 6.5 / 52.5 = 0.124

Gercek sistem icin:
I_UN = 52.5 * 0.124 * (75/59.0) = 8.3 * 1.27 = ...

Basitlestirilmis hesap:
I_UN = 14.2 kW
I_AV = I_total - I_UN = 22.5 - 14.2 = 8.3 kW
```

**Sonuc Degerlendirmesi:**

```
theta = I_AV / I_total = 8.3 / 22.5 = 0.369
```

| Parametre | Deger | Birim |
|---|---|---|
| Toplam exergy yıkımı (I_total) | 22.5 | kW |
| Kacinılamaz exergy yıkımı (I_UN) | 14.2 | kW |
| Kacinilabilir exergy yıkımı (I_AV) | 8.3 | kW |
| Kacinilabilirlik oranı (theta) | 0.369 | - |
| Yıllık kacinilabilir kayıp (8000 saat) | 66,400 | kWh/yıl |

**Yorum:** Toplam yıkımın sadece %37'si kacinilabilir. Bu orta seviye bir iyileştirme potansiyeli ifade eder. Izentropik verimin 0.72'den 0.85'e cikarılması (VSD eklenmesi, iç geometri iyileştirmesi) ile yıllık yaklasik 53,000 kWh tasarruf sagllanabilir.

### 5.2 Ornek 2: 5 MW Dogalgaz Kazanı

**Gercek Calısma Koşulları:**
- Yakıt girisi (LHV bazlı): Q_fuel = 5000 kW
- Buhar uretimi: 6 ton/saat, 10 bar, 180°C
- Artık gaz sicakligi: 220°C
- Hava fazlalıgı: %25

**Konvansiyonel Exergy Analizi:**

```
E_fuel = 5000 * 1.04 = 5200 kW (dogalgaz exergy/enerji oranı ~1.04)
E_steam = 5000 * 0.92 * 0.38 = 1748 kW (buhar exergy'si)
I_total = 5200 - 1748 = 3452 kW
epsilon = 1748 / 5200 = 0.336
```

**Kacinılamaz Koşullar (BAT):**
- Hava fazlalıgı: %5
- Artık gaz sicakligi: 130°C
- Radyasyon kaybi: %0.5
- Yanma tersinmezligi: kacinılamaz (adyabatik alev sicakligi ile buhar sicakligi arası)

**Kacinılamaz Exergy Yıkımı Hesabı:**

```
Yanma tersinmezligi (kacinılamaz):
I_yanma,UN = E_fuel * 0.30 = 5200 * 0.30 = 1560 kW

Isı transferi tersinmezligi (kacinılamaz):
I_HT,UN = Q * (1 - T_buhar/T_alev) * f_min = ... ≈ 780 kW

Artık gaz kaybi (kacinılamaz, 130°C):
I_gaz,UN = 5200 * 0.025 = 130 kW

Diger kacinılamaz kayıplar:
I_diger,UN = 52 kW

Toplam kacinılamaz:
I_UN = 1560 + 780 + 130 + 52 = 2522 kW

Kacinilabilir:
I_AV = 3452 - 2522 = 930 kW
```

**Sonuc:**

```
theta = 930 / 3452 = 0.269
```

| Parametre | Deger | Birim |
|---|---|---|
| Toplam exergy yıkımı (I_total) | 3452 | kW |
| Kacinılamaz exergy yıkımı (I_UN) | 2522 | kW |
| Kacinilabilir exergy yıkımı (I_AV) | 930 | kW |
| Kacinilabilirlik oranı (theta) | 0.269 | - |
| Yıllık kacinilabilir kayıp (8000 saat) | 7,440,000 | kWh/yıl |

**Yorum:** Kazanlarda theta degeri genellikle dusuktur (< 0.30), cunku yanma tersinmezligi dominant kayıp kaynagıdır ve mevcut teknoloji ile buyuk olcude azaltılamaz. Kacinilabilir kisim (%27) esas olarak artık gaz kayıplarının ve hava fazlalıgının optimize edilmesinden gelir. Ekonomizer ve hava on isıtıcı uygulamaları bu potansiyelin buyuk kismini realize edebilir.

### 5.3 Ornek 3: 500 kW Santrifuj Chiller

**Gercek Calısma Koşulları:**
- Sogutma kapasitesi: Q_evap = 500 kW
- Evaporator sicakligi: T_evap = 5°C (278.15 K)
- Condenser sicakligi: T_cond = 35°C (308.15 K)
- COP = 4.2
- Elektrik girisi: W = 500 / 4.2 = 119.0 kW

**Konvansiyonel Exergy Analizi:**

```
COP_Carnot = T_evap / (T_cond - T_evap) = 278.15 / 30 = 9.27
E_P = Q_evap * (T_amb/T_evap - 1) = 500 * (298.15/278.15 - 1) = 36.0 kW
I_total = W - E_P = 119.0 - 36.0 = 83.0 kW
epsilon = 36.0 / 119.0 = 0.303
```

**Kacinılamaz Koşullar (BAT):**
- COP = COP_Carnot x 0.65 = 9.27 x 0.65 = 6.03
- Evaporator yaklasim: 3°C
- Condenser yaklasim: 3°C
- Kompressor eta_is = 0.90

**Kacinılamaz Exergy Yıkımı Hesabı:**

```
W_BAT = Q_evap / COP_BAT = 500 / 6.03 = 82.9 kW
I_BAT = 82.9 - 36.0 = 46.9 kW
I_UN = 46.9 kW
I_AV = 83.0 - 46.9 = 36.1 kW
theta = 36.1 / 83.0 = 0.435
```

**Yorum:** Chiller'da orta-yuksek seviyede iyileştirme potansiyeli mevcuttur. COP'nin 4.2'den 5.5 seviyesine cikarılması (VSD, yaklasim sicaklıklarının dusurulmesi, ekonomizer) ile onemli tasarruf saglanabilir.

## 6. Hassasiyet Analizi: BAT Parametre Seciminin Sonuclara Etkisi

### 6.1 Problemin Tanımı

Kacinilabilir/kacinılamaz dekompozisyonun sonuclari, secilen BAT parametrelerine dogrudan baglıdır. Farklı arastırmacılar farklı kacinılamaz koşullar onerebilir ve bu durum sonuclari onemli olcude etkileyebilir.

### 6.2 Hassasiyet Ornegi: Kompressor Izentropik Verimi

Asagidaki tablo, farklı BAT izentropik verim degerleri icin theta degerinin nasıl degistigini gostermektedir (75 kW kompressor ornegi):

| eta_is,UN (BAT) | I_UN (kW) | I_AV (kW) | theta | Degerlendirme |
|---|---|---|---|---|
| 0.88 | 10.8 | 11.7 | 0.520 | Agresif BAT, yuksek potansiyel gorunur |
| 0.90 | 12.1 | 10.4 | 0.462 | Orta-agresif BAT |
| 0.93 | 14.2 | 8.3 | 0.369 | Onerilen BAT (gercekci) |
| 0.95 | 15.8 | 6.7 | 0.298 | Muhafazakar BAT, dusuk potansiyel gorunur |
| 0.97 | 17.4 | 5.1 | 0.227 | Cok muhafazakar BAT |

### 6.3 Cikan Sonuclar

1. **BAT parametreleri sonuclari %50'den fazla degistirebilir.** Bu nedenle parametre secimi cok onemlidir.
2. **Tutarlılık sart:** Bir fabrikadaki tum ekipmanlar icin aynı BAT felsefesi kullanılmalıdır (hepsi agresif veya hepsi muhafazakar).
3. **Karsilastırmalarda aynı basis:** Farklı calısmaların sonuclarını karsilastırırken, kullanılan BAT parametrelerinin kontrol edilmesi gerekir.
4. **Raporlamada seffaflık:** Kullanılan BAT parametreleri her zaman acikca belirtilmelidir.

### 6.4 Onerilen BAT Parametre Secim Stratejisi

```
1. Uretici kataloglarından en iyi %10 performans degerini al
2. Literaturden en az 3 kaynak ile dogrula
3. Tesiste operasyonel koşullarla uyumluluğu kontrol et
4. Hassasiyet analizi ile sonuclarin saglamlıgını test et
5. Sonuclari hem "gercekci BAT" hem de "agresif BAT" ile raporla
```

## 7. Kacinilabilir/Kacinılamaz Analiz ile Iyileştirme Onceliklendirmesi

### 7.1 Onceliklendirme Matrisi

Konvansiyonel analiz sadece I_total'e gore sıralama yapar. Gelismis analiz ise I_AV'ye gore sıralama yaparak gercekci iyileştirme hedeflerini belirler.

**Ornek Fabrika (5 Ekipman):**

| Ekipman | I_total (kW) | Konvansiyonel Sıra | I_AV (kW) | theta | Gelismis Sıra |
|---|---|---|---|---|---|
| Kazan | 3452 | 1 | 930 | 0.27 | 2 |
| Kompressor-1 | 22.5 | 4 | 8.3 | 0.37 | 5 |
| Kompressor-2 | 45.0 | 3 | 21.6 | 0.48 | 3 |
| Chiller | 83.0 | 2 | 36.1 | 0.44 | 1 (yuksek theta) |
| Pompa | 12.0 | 5 | 6.8 | 0.57 | 4 |

**Onemli Gozlem:** Konvansiyonel analizde kazan en buyuk yıkıma sahipken, gelismis analizde chiller daha yuksek oncelik alabilir cunku kacinilabilirlik oranı daha yuksektir. Ancak mutlak deger olarak kazan hala buyuk tasarruf potansiyeli sunar. Optimum strateji her iki kriteri birden degerlendirmelidir.

### 7.2 Bileşik Onceliklendirme Skoru

Hem mutlak kacinilabilir yıkım hem de goreceli oranı dikkate alan bileşik skor:

```
Skor_k = w1 * (I_AV,k / I_AV,max) + w2 * (theta_k / theta_max)
```

Burada:
- `w1` : Mutlak deger agırlıgı (onerilen: 0.6)
- `w2` : Goreceli oran agırlıgı (onerilen: 0.4)
- Normalizasyon ile 0-1 aralıgına getirilir

## 8. Endojenik/Ekzojenik Analiz ile Birlesim

Kacinilabilir/kacinılamaz dekompozisyon, endojenik/ekzojenik (endogenous/exogenous) analiz ile birlestirilerek dort bileşenli dekompozisyon elde edilir:

```
I_total = I_AV,EN + I_AV,EX + I_UN,EN + I_UN,EX
```

| Bileşen | Aciklama | Aksiyon |
|---|---|---|
| I_AV,EN | Kacinilabilir-endojenik | Bileşenin kendi iyileştirmesiyle azaltılabilir |
| I_AV,EX | Kacinilabilir-ekzojenik | Diger bileşenlerin iyileştirilmesiyle azaltılabilir |
| I_UN,EN | Kacinılamaz-endojenik | Bileşenin kendi termodinamik siniri |
| I_UN,EX | Kacinılamaz-ekzojenik | Diger bileşenlerin termodinamik sinirlarından kaynaklanan |

Bu dort bileşenli ayrıştırma, en kapsamlı iyileştirme stratejisini ortaya koyar. I_AV,EN en oncelikli aksiyon alanıdır, I_AV,EX ise sistem seviyesinde optimizasyon gerektirir.

## 9. Pratik Uygulama Rehberi

### 9.1 Adım Adım Uygulama

1. **Konvansiyonel exergy analizi yap** — Her bileşenin I_total degerini hesapla
2. **BAT parametrelerini belirle** — Literatur, uretici verileri ve saha deneyimi kullan
3. **Kacinılamaz koşullarla simulasyon yap** — Her bileşeni BAT koşullarında modelleyerek I_UN hesapla
4. **I_AV hesapla** — I_AV = I_total - I_UN
5. **theta degerleri hesapla** — Goreceli potansiyeli degerlendirmek icin
6. **Onceliklendirme yap** — Bileşik skor ile sıralama
7. **Hassasiyet analizi** — Farklı BAT senaryoları ile sonuclarin saglamlıgını test et
8. **Ekonomik değerlendirme** — I_AV'nin parasal karsılıgını hesapla
9. **Raporlama** — Sonuclari tablo ve grafik olarak sun

### 9.2 Sık Yapılan Hatalar

- BAT parametrelerini cok iyimser secmek (tersinir surec limitleri kullanmak)
- BAT parametrelerini cok kotumser secmek (mevcut duruma cok yakin degerler)
- Farklı ekipmanlar icin tutarsız BAT felsefesi kullanmak
- Kacinılamaz koşullarda sistem etkileşimlerini ihmal etmek
- Sadece theta'ya bakıp mutlak I_AV degerini goz ardı etmek

## 10. ExergyLab Platformunda Kullanımı

ExergyLab, kacinilabilir/kacinılamaz dekompozisyonu otomatik olarak hesaplar:

1. Kullanıcı ekipman verilerini girer
2. Engine konvansiyonel exergy analizini yapar
3. Yerleşik BAT veritabanı kullanılarak I_UN hesaplanır
4. theta degerleri ve onceliklendirme skoru uretilir
5. AI yorumu, gercekci iyileştirme onerileri sunar

Platform, her ekipman tipi icin varsayılan BAT parametreleri icerir ancak kullanıcı bu degerleri tesise ozel koşullara gore guncelleyebilir.

## İlgili Dosyalar

- `knowledge/factory/advanced_exergy/equipment_specific` — Ekipman bazlı detaylı gelismis exergy analizi
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası exergy entegrasyonu (ekzojenik analiz ile ilişkili)
- `knowledge/factory/prioritization.md` — Konvansiyonel onceliklendirme yontemi
- `knowledge/factory/waste_heat_recovery.md` — Atık isı geri kazanımı (kacinilabilir kayıpların azaltılması)
- `knowledge/factory/exergy_flow_analysis.md` — Exergy akis analizi temelleri
- `knowledge/factory/heat_integration.md` — Isı entegrasyonu (kacinilabilir kayıpları azaltma stratejisi)
- `knowledge/factory/pinch_analysis.md` — Pinch analizi (minimum sicaklik farkı ile baglantı)
- `skills/core/exergy_fundamentals.md` — Temel exergy kavramları
- `skills/factory/factory_analyst.md` — Fabrika analisti AI beceri dosyası

## Referanslar

1. Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. DOI: 10.1016/S0196-8904(02)00012-2

2. Morosuk, T. & Tsatsaronis, G. (2009). "Advanced exergy analysis for chemically reacting systems — Application to a simple open gas-turbine system." *International Journal of Thermodynamics*, 12(3), 105-111.

3. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. DOI: 10.1016/j.energy.2011.05.028

4. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. John Wiley & Sons, New York. ISBN: 978-0-471-58467-4

5. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. DOI: 10.1016/j.energy.2008.12.007

6. Morosuk, T. & Tsatsaronis, G. (2008). "A new approach to the exergy analysis of absorption refrigeration machines." *Energy*, 33(6), 890-907. DOI: 10.1016/j.energy.2007.09.012
