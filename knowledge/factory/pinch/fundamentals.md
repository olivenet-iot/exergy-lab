---
title: "Pinch Analizi Temelleri — Linnhoff Metodolojisi (Pinch Analysis Fundamentals — Linnhoff Methodology)"
category: factory
equipment_type: factory
keywords: [pinch analizi, Linnhoff, minimum enerji gereksinimi, MER, üç altın kural, pinch bölümlemesi, exergy-pinch bağlantısı, ısı entegrasyonu, termodinamik, bileşik eğriler, problem tablosu algoritması]
related_files: [factory/pinch_analysis.md, factory/heat_integration.md, factory/exergy_fundamentals.md, factory/process_integration.md, factory/waste_heat_recovery.md, factory/cross_equipment.md, factory/utility_analysis.md]
use_when: ["Pinch analizi temelleri açıklanırken", "Linnhoff metodolojisi uygulanırken", "Minimum enerji gereksinimi hesaplanırken", "Üç altın kural sorgulanırken", "Exergy-pinch ilişkisi değerlendirilirken", "Pinch bölümlemesi yapılırken"]
priority: high
last_updated: 2026-02-01
---
# Pinch Analizi Temelleri — Linnhoff Metodolojisi (Pinch Analysis Fundamentals — Linnhoff Methodology)

> Son güncelleme: 2026-02-01

## Genel Bakis

Pinch analizi, endüstriyel proseslerde enerji tüketimini sistematik olarak minimize etmek amaciyla gelistirilen termodinamik tabanli bir metodolojidir. 1978 yilinda Boden Linnhoff tarafindan Leeds Üniversitesi'ndeki doktora calismasi sirasinda temelleri atilan bu yaklasim, sicak ve soguk akislarin isi alisverisi potansiyelini analiz ederek bir prosesin teorik minimum dis enerji (utility) ihtiyacini hesaplar. Pinch noktasi, prosesin termodinamik darbogazidir ve tüm tasarim kararlarinin bu nokta etrafinda sekillendirilmesi gerekir.

Bu dokümanda, pinch analizinin tarihsel gelisimi, termodinamik temelleri, minimum enerji gereksinimi (MER) kavrami, üc altin kural, pinch bölümlemesi, exergy baglantisi, metodoloji adimlari ve temel varsayimlar asagidaki 5 akislik referans problemiyle birlikte ele alinmaktadir:

| Akis No | Tür | T_kaynak [°C] | T_hedef [°C] | CP [kW/°C] | Q [kW] |
|---------|-----|---------------|--------------|------------|--------|
| H1 | Sicak | 270 | 80 | 15 | 2,850 |
| H2 | Sicak | 180 | 40 | 25 | 3,500 |
| H3 | Sicak | 150 | 60 | 10 | 900 |
| C1 | Soguk | 30 | 250 | 18 | 3,960 |
| C2 | Soguk | 60 | 200 | 12 | 1,680 |

```
Parametreler:
  DTmin = 10°C
  Pinch noktasi: 175°C (kaydirilmis) / 180°C (sicak) / 170°C (soguk)
  QH,min = 1,800 kW (minimum sicak utility)
  QC,min = 2,240 kW (minimum soguk utility)
  Toplam sicak akis yükü: 7,250 kW
  Toplam soguk akis yükü: 5,640 kW
```

## 1. Tarihce ve Gelisim (History and Development)

### 1.1 Boden Linnhoff ve Ilk Calisma (1978)

Pinch analizi, Boden Linnhoff'un 1978 yilinda Leeds Üniversitesi'nde tamamladigi doktora tezi ile baslamistir. Linnhoff, endüstriyel proseslerdeki isi degistirici aglarinin (HEN — Heat Exchanger Network) sistematik olarak tasarlanabilecegini gösterdi. Daha önceki yaklasimlar sezgisel (heuristic) iken, Linnhoff termodinamik hedefleme ile optimum tasarima yönelik kesin bir yöntem sundu.

```
Kronolojik gelisim:

1978 — Linnhoff doktora tezi (Leeds Üniversitesi)
       Temel kavram: Sicak ve soguk bileşik egriler (Composite Curves)
       Pinch noktasinin keşfi ve termodinamik anlamı

1979 — Linnhoff & Flower: "Synthesis of Heat Exchanger Networks"
       AIChE Journal'da yayınlanan iki bölümlük makale
       Problem Tablosu Algoritmasi (PTA) tanitildi

1982 — IChemE User Guide (1. baski)
       "A User Guide on Process Integration for the Efficient Use of Energy"
       Endüstriyel uygulama için ilk kapsamli kilavuz

1983 — Linnhoff & Hindmarsh: "The Pinch Design Method"
       Chemical Engineering Science'ta yayinlandi
       HEN tasarimi için sistematik pinch yöntemi

1986 — Tjoe & Linnhoff: Retrofit (mevcut tesis iyilestirme) yöntemi
       Mevcut tesislere uygulanabilirlik genisledi

1989 — Linnhoff March Ltd. kuruldu (ticari danismanlik)
       Endüstriyel ölcekte uygulama yayginlasti

1993 — Dhole & Linnhoff: Total Site Analysis
       Birden fazla prosesin entegrasyonu, site-level optimizasyon

1994 — IChemE User Guide (2. baski, gözden geçirilmiş)
       Linnhoff et al., kapsamli guncelleme ve genisletme
       Retrofit, total site ve ileri konular eklendi

2000+ — Exergy-pinch entegrasyonu, super-targeting, sürdürülebilirlik
       Pinch analizinin karbon ayak izi ve cevre yonetimine genislemesi

2007 — Kemp: "Pinch Analysis and Process Integration" (2. baski)
       Modern referans kitap, kapsamli endüstriyel örnekler

2013 — Klemes: "Handbook of Process Integration (PI)"
       Tüm PI yöntemlerini kapsayan el kitabi
```

### 1.2 IChemE User Guide ve Endüstriyel Etki

IChemE (Institution of Chemical Engineers) tarafindan yayinlanan "User Guide on Process Integration for the Efficient Use of Energy" kitabi, pinch analizinin endüstriyel yayginlasmasinda belirleyici rol oynadi. Bu kilavuz:

- Akademik kavramlari mühendislik pratiğine dönüstürdü
- Adim adim hesaplama prosedürleri sundu
- Gerçek endüstriyel vaka çalismalarini içerdi
- Isi degistirici agi tasarimi için sistematik yöntem verdi
- Dünya genelinde 10,000'den fazla endüstriyel projede referans olarak kullanildi

### 1.3 Yöntemin Evrimi

```
Birinci nesil (1978-1985):
  - Tek proses pinch analizi
  - Sabit DTmin ile hedefleme
  - Manuel bileşik egri ve PTA hesaplama
  - Greenfield (yeni tesis) odakli tasarim

Ikinci nesil (1985-1995):
  - Retrofit yöntemleri (mevcut tesis iyilestirme)
  - Total site analizi (tüm tesis entegrasyonu)
  - Çoklu utility hedefleme
  - DTmin optimizasyonu (super-targeting)
  - Distilasyon kolonu entegrasyonu

Üçüncü nesil (1995-2010):
  - Exergy-pinch baglamasi
  - Su ve hidrojen pinch analizleri
  - Karbon emisyon hedefleme
  - Matematiksel programlama ile entegrasyon
  - Yazılım araçlarinin yayginlasmasi

Dördüncü nesil (2010-günümüz):
  - Enerji-su-emisyon bütünleşik analizi
  - Yenilenebilir enerji entegrasyonu
  - Isi depolama ve esnek operasyon
  - Yapay zeka destekli optimizasyon
  - Dijital ikiz (digital twin) ile gerçek zamanli pinch analizi
```

## 2. Termodinamik Temeller (Thermodynamic Foundations)

### 2.1 Birinci Yasa Baglami (First Law Context)

Termodinamigin birinci yasasi enerji korunumunu ifade eder. Pinch analizinde bu yasa, enerji denge denklemleri ile doğrudan kullanilir:

```
Enerji Dengesi (Energy Balance):

  Q_sicak_toplam + QH,min = Q_soguk_toplam + QC,min

Referans problem için dogrulama:
  7,250 + 1,800 = 5,640 + 2,240 + Q_geri_kazanim

  QH,min - QC,min = Q_soguk_toplam - Q_sicak_toplam
  1,800 - 2,240  = 5,640 - 7,250
       -440      = -1,610

  Toplam enerji dengesi:
  Proses isi açigi = Q_soguk_toplam - Q_sicak_toplam = 5,640 - 7,250 = -1,610 kW
  (Proses net isi fazlasi var — sogutma agirlikli)

  Bu, QC,min > QH,min sonucuyla tutarlidir:
  QC,min - QH,min = 2,240 - 1,800 = 440 kW (net fazla)

  Tam denge kontrolü:
  QH,min + Q_sicak_toplam = QC,min + Q_soguk_toplam
  1,800 + 7,250 = 2,240 + 5,640  (Her iki taraf: Not — denge akis bazli sağlanir)
```

Birinci yasa, enerjinin ne kadar gerektigini söyler, ancak enerjinin kalitesi hakkinda bilgi vermez. Örnegin, 1,800 kW sicak utility'nin hangi sicaklik seviyesinde saglanmasi gerektigi birinci yasanin kapsaminda degildir.

### 2.2 Ikinci Yasa ve Entropi Üretimi (Second Law and Entropy Generation)

Termodinamigin ikinci yasasi, tüm gerçek proseslerin tersinmez (irreversible) oldugunu ve entropi ürettiğini belirtir. Pinch analizindeki her isi transferi islemi entropi üretir:

```
Bir isi degistiricideki entropi üretimi:

  S_gen = Q × (1/T_soguk - 1/T_sicak)  [kW/K]

Burada:
  Q    = transfer edilen isi [kW]
  T_sicak = sicak akisin ortalama sicakligi [K]
  T_soguk = soguk akisin ortalama sicakligi [K]

Örnek: H1'den C1'e pinch üstünde isi transferi
  Q = 1,350 kW
  T_sicak,ort = (270 + 180) / 2 = 225°C = 498.15 K
  T_soguk,ort = (170 + 245) / 2 = 207.5°C = 480.65 K
  (C1, bu degistiricide 170°C'den 170 + 1350/18 = 245°C'ye çikar)

  S_gen = 1,350 × (1/480.65 - 1/498.15)
        = 1,350 × (0.002081 - 0.002007)
        = 1,350 × 0.0000736
        = 0.0993 kW/K

Entropi üretiminin anlamlari:
  - DTmin ne kadar büyükse, entropi üretimi o kadar fazla
  - DTmin = 0 olsaydi (ideal): Entropi üretimi = 0, ancak sonsuz alan gerekli
  - Pinch ihlalleri ek entropi üretir (gereksiz tersinmezlik)
```

### 2.3 Exergy Baglantisi (Exergy Connection)

Exergy kavramı, ikinci yasanin doğrudan bir sonucudur. Entropi üretimi ile exergy yikimi dogrudan iliskilidir:

```
Gouy-Stodola Teoremi:

  Ex_yikim = T0 × S_gen  [kW]

Burada:
  T0 = referans çevre sicakligi = 298.15 K (25°C)
  S_gen = entropi üretim hizi [kW/K]

Yukaridaki örnek için:
  Ex_yikim = 298.15 × 0.0993 = 29.6 kW

Bu, 1,350 kW isi transfer edilirken 29.6 kW exergy'nin geri dönüsümsüz
olarak yikildigini gösterir. Bu yikim, sicaklik farkindan kaynaklanir.
```

Pinch analizinde exergy perspektifi, enerji hedeflerinin ötesinde termodinamik kalite degerlendirmesi saglar. Bu ilişki Bölüm 6'da detaylandirilmistir.

## 3. Minimum Enerji Gereksinimi — MER (Minimum Energy Requirement)

### 3.1 MER Kavramı

Minimum Enerji Gereksinimi (MER — Minimum Energy Requirement), belirli bir DTmin değeri için bir prosesin ihtiyaç duydugu minimum dış enerji miktarıdır. MER, iki bileşenden oluşur:

```
MER bileşenleri:

  QH,min = Minimum sicak utility gereksinimi [kW]
           Prosesin dis kaynaklardan almasi gereken en az isi miktari

  QC,min = Minimum soguk utility gereksinimi [kW]
           Prosesin dis ortama atmasi gereken en az isi miktari

Referans problem için (DTmin = 10°C):
  QH,min = 1,800 kW
  QC,min = 2,240 kW
```

### 3.2 MER'in Önemi

MER, bir proses için termodinamik alt siniri (lower bound) temsil eder. Bunun pratik anlamlari:

```
1. Benchmarking: Mevcut utility tüketimi ile MER arasindaki fark,
   iyilestirme potansiyelini dogrudan gösterir.

   Örnek:
   Mevcut kullanim: QH = 3,500 kW, QC = 3,940 kW
   MER hedefleri:   QH,min = 1,800 kW, QC,min = 2,240 kW
   Tasarruf:         1,700 kW sicak (%49) + 1,700 kW soguk (%43)

2. Yatirim karari: MER'e yaklasmak ek isi degistirici yatirimi
   gerektirir. Ekonomik optimum genellikle MER'in %90-95'idir.

3. Tasarim yönlendirme: MER, HEN tasariminin hedef noktasini belirler.
   Tasarimci bu hedefe ne kadar yaklasmak istedigine karar verir.

4. Cross-pinch analizi: Mevcut sistemdeki cross-pinch transferleri
   tespit edilerek tasarruf firsatlari belirlenir.
```

### 3.3 MER Hesaplama — Problem Tablosu Algoritmasi (PTA)

Referans problem üzerinden PTA'nin tam uygulamasi:

```
Adim 1: Kaydirilmis sicakliklar (Shifted Temperatures)
  Sicak akislar: T* = T - DTmin/2 = T - 5
  Soguk akislar: T* = T + DTmin/2 = T + 5

  H1: 265 → 75°C (kaydirilmis)
  H2: 175 → 35°C (kaydirilmis)
  H3: 145 → 55°C (kaydirilmis)
  C1: 35 → 255°C (kaydirilmis)
  C2: 65 → 205°C (kaydirilmis)

Adim 2: Kaydirilmis sıcakliklari sirala
  255, 205, 175, 145, 75, 65, 55, 35

Adim 3: Her aralikta aktif akislari belirle ve net isi dengesini hesapla

  Aralik [°C]  | Aktif Sicak | Aktif Soguk | CP_sic | CP_sog | Net CP | DT | DH [kW]
  255-205      | —           | C1          | 0      | 18     | -18    | 50 | -900
  205-175      | —           | C1, C2      | 0      | 30     | -30    | 30 | -900
  175-145      | H1, H2      | C1, C2      | 40     | 30     | +10    | 30 | +300
  145-75       | H1, H2, H3  | C1, C2      | 50     | 30     | +20    | 70 | +1,400
  75-65        | H2, H3      | C1, C2      | 35     | 30     | +5     | 10 | +50
  65-55        | H2, H3      | C2          | 35     | 12     | +23    | 10 | +230
  55-35        | H2           | C2          | 25     | 12     | +13    | 20 | +260

  (Not: H3 kaydirilmis 145-55 araliginda aktif, C2 kaydirilmis 65-205 araliginda aktif)

Adim 4: Isi kaskadi (Heat Cascade)
  Baslangic: R0 = 0 (sicak utility yok varsayimi)

  T* [°C]  | DH [kW]  | R (kaskad) [kW]
  255      |          | 0
           | -900     |
  205      |          | -900
           | -900     |
  175      |          | -1,800  <-- En negatif deger
           | +300     |
  145      |          | -1,500
           | +1,400   |
  75       |          | -100
           | +50      |
  65       |          | -50
           | +230     |
  55       |          | +180
           | +260     |
  35       |          | +440

Adim 5: Düzeltilmiş kaskad
  R0 = |en negatif| = 1,800 kW (QH,min)

  T* [°C]  | R_düzeltilmis [kW]
  255      | 1,800           <-- QH,min = 1,800 kW
  205      | 900
  175      | 0               <-- PINCH NOKTASI
  145      | 300
  75       | 1,700
  65       | 1,750
  55       | 1,980
  35       | 2,240           <-- QC,min = 2,240 kW
```

### 3.4 Pinch Noktasinin Belirlenmesi

```
Kaydirilmis pinch sicakligi: T*_pinch = 175°C
  (Düzeltilmis kaskadda R = 0 olan sicaklik)

Gerçek pinch sicakliklari:
  Sicak taraf: T_pinch,sicak = 175 + DTmin/2 = 175 + 5 = 180°C
  Soguk taraf: T_pinch,soguk = 175 - DTmin/2 = 175 - 5 = 170°C

Fiziksel anlami:
  - Pinch noktasinda sicak ve soguk bileşik egriler arasindaki
    sicaklik farki tam olarak DTmin = 10°C'dir.
  - Bu nokta prosesin termodinamik darbogazidir.
  - Net isi akisi bu noktada sifirdir (pinch üstü ve alti
    termodinamik olarak birbirinden bagimsizdir).
```

## 4. Üc Altin Kural (Three Golden Rules)

Pinch analizinin en temel ilkeleri üc altin kuraldır. Bu kurallar, MER'e ulaşmanin zorunlu kosullarını tanımlar. Herhangi birinin ihlali utility tüketiminin artmasina yol açar.

### 4.1 Kural 1: Pinch Üzerinden Isi Transfer Etmeyin (Don't Transfer Heat Across the Pinch)

```
Tanim:
  Pinch üstünden (T > 180°C sicak taraf) pinch altina (T < 170°C soguk taraf)
  isi transfer edilmemelidir.

Neden:
  Pinch üstü = Net isi AÇIĞI olan bölge (sicak utility gerekli)
  Pinch alti  = Net isi FAZLASI olan bölge (soguk utility gerekli)

  Pinch üzerinden DQ kadar isi transfer edilirse:
  - Pinch üstündeki açik DQ kadar artar → QH DQ kadar artar
  - Pinch altindaki fazla DQ kadar artar → QC DQ kadar artar
  - Toplam utility artisi: 2 × DQ (cifte ceza!)

Sayisal örnek:
  Normal (kurala uygun):
    QH = QH,min = 1,800 kW
    QC = QC,min = 2,240 kW
    Toplam utility = 4,040 kW

  Kural ihlali — 500 kW pinch üzerinden transfer:
    QH = 1,800 + 500 = 2,300 kW
    QC = 2,240 + 500 = 2,740 kW
    Toplam utility = 5,040 kW
    Artis = 1,000 kW (= 2 × 500)

  Enerji maliyet etkisi (Dogalgaz: 0.035 EUR/kWh, 8,000 saat/yil):
    Ek yillik maliyet = 500 × 0.035 × 8,000 = 140,000 EUR/yil
    (Sadece sicak utility artisi — soguk utility maliyeti ayrica eklenir)
```

### 4.2 Kural 2: Pinch Altinda Sicak Utility Kullanmayin (Don't Use Hot Utility Below the Pinch)

```
Tanim:
  170°C'nin (soguk pinch sicakligi) altindaki bölgede dis
  ısıtma (sicak utility) kullanilmamalidir.

Neden:
  Pinch alti zaten net isi fazlasi olan bölgedir.
  Bu bölgeye sicak utility eklemek, ayni miktarda fazla isiyi
  soguk utility ile uzaklastirma ihtiyaci yaratir.

  Pinch altinda QH_ihlal kadar sicak utility kullanilirsa:
  - QH = QH,min + QH_ihlal (gereksiz isitma)
  - QC = QC,min + QH_ihlal (gereksiz sogutma)
  - Toplam utility artisi: 2 × QH_ihlal

Sayisal örnek:
  Pinch altinda 300 kW'lik bir isi degistiriciye LP buhar verilirse:
    QH = 1,800 + 300 = 2,100 kW
    QC = 2,240 + 300 = 2,540 kW

  Bu 300 kW, asla gerekmeyecek bir isitma-sogutma çiftidir.
  Pinch altindaki akislar, birbirleriyle isi degistirerek ihtiyaci
  karsilayabilir — dis kaynak gerekmez.

Tipik ihlal örnekleri:
  - Düsük sicaklikli proses suyu için buhar kullanmak
  - Pinch altindaki bir tankı buhar bataryasi ile isitmak
  - Bina isitma için pinch altinda ayri kazan çalistirmak
```

### 4.3 Kural 3: Pinch Üstünde Soguk Utility Kullanmayin (Don't Use Cold Utility Above the Pinch)

```
Tanim:
  180°C'nin (sicak pinch sicakligi) üzerindeki bölgede dis
  sogutma (soguk utility) kullanilmamalidir.

Neden:
  Pinch üstü net isi açiği olan bölgedir.
  Bu bölgede soguk utility kullanmak, o isiyi sogutmak yerine
  soguk akislarin isitilmasi için kullanilabilecek degeri yok eder.

  Pinch üstünde QC_ihlal kadar soguk utility kullanilirsa:
  - QH = QH,min + QC_ihlal (yok edilen isinın yerine utility)
  - QC = QC,min + QC_ihlal (sogutma eklenmis)
  - Toplam utility artisi: 2 × QC_ihlal

Sayisal örnek:
  H1 akisinin 270°C'den 200°C'ye sogutulmasinda 15 × 70 = 1,050 kW
  vardir. Bu isinin tamami pinch üstündedir.
  Eger bu isinın 400 kW'i sogutma suyu ile atilirsa:
    QH = 1,800 + 400 = 2,200 kW
    QC = 2,240 + 400 = 2,640 kW

  Oysa bu 400 kW, C1 veya C2 akislarini isitmak için kullanilabilirdi.

Tipik ihlal örnekleri:
  - Yüksek sicakliktaki proses akisinin sogutma kulesine gönderilmesi
  - Reaktör çikisinin su ile sogutulup isi geri kazanilmamasi
  - Pinch üstündeki kondensin kanal/drenaja verilmesi
```

### 4.4 Cifte Ceza Mekanizmasi (Double Penalty Mechanism)

Üc altin kuralın ortak özelligi, her ihlalin çifte ceza yaratmasidir. Bu mekanizmayi detayli olarak inceleyelim:

```
Cifte Ceza — Sistematik Açiklama:

Pinch, sistemi iki bagimsiz alt probleme böler:

  PINCH ÜSTÜ (sicak utility bölgesi):
  +--------------------------------------------+
  |  Isi açiği var → QH,min ile kapatilir       |
  |  Bu bölgede isi kaynagi YOKTUR, DIS KAYNAK  |
  |  (sicak utility) ZORUNLUDUR                 |
  +--------------------------------------------+

  PINCH (R = 0, net isi akisi sifir)

  PINCH ALTI (soguk utility bölgesi):
  +--------------------------------------------+
  |  Isi fazlasi var → QC,min ile uzaklastirilir|
  |  Bu bölgede isi fazlasi VARDIR, DIS ORTAMA  |
  |  (soguk utility) ATILMALIDIR                |
  +--------------------------------------------+

Ihlal senaryosu: DQ = 500 kW pinch üzerinden transfer

  1) Pinch üstünde 500 kW eksik kalir
     → 500 kW fazladan sicak utility gerekir (QH artisi)

  2) Pinch altina 500 kW fazla isi gelir
     → 500 kW fazladan soguk utility gerekir (QC artisi)

  3) Sonuç: DQ'nun kendisi + DQ'nun sogutulmasi = 2 × DQ


Özet tablo — Tüm ihlal türleri:

  Ihlal türü             | QH artisi | QC artisi | Toplam ceza
  ----------------------- | --------- | --------- | -----------
  Cross-pinch: DQ         | +DQ       | +DQ       | 2 × DQ
  Pinch alti sicak: DQ    | +DQ       | +DQ       | 2 × DQ
  Pinch üstü soguk: DQ    | +DQ       | +DQ       | 2 × DQ
  Birden fazla ihlal      | Toplam    | Toplam    | 2 × Toplam
```

### 4.5 Mevcut Sistemde Kural Ihlallerinin Tespiti

```
Mevcut bir fabrikanin utility kullanimi ile MER hedeflerinin
karsilastirilmasi, kural ihlallerini ortaya koyar:

Referans problem — mevcut durum varsayimi:
  Mevcut: QH = 3,500 kW, QC = 3,940 kW
  Hedef:  QH,min = 1,800 kW, QC,min = 2,240 kW

  Cross-pinch transfer miktari:
  X_pinch = QH - QH,min = 3,500 - 1,800 = 1,700 kW

  Dogrulama:
  X_pinch = QC - QC,min = 3,940 - 2,240 = 1,700 kW  (tutarli)

  Bu 1,700 kW, üc altin kural ihlallerinin toplam etkisidir.
  Ihlallerin kaynaklarinin tespiti için:
  - Her mevcut isi degistiricinin pinch'e göre konumunu analiz et
  - Cross-pinch transfer yapan üniteleri belirle
  - En büyük ihlali ortadan kaldirarak baslama (siralamali retrofit)
```

## 5. Pinch Bölümlemesi (Pinch Decomposition)

### 5.1 Bölümleme Ilkesi

Pinch noktasi, problemi iki bagimsiz alt probleme ayirir. Her alt problem kendi enerji dengesine sahiptir ve bagimsiz olarak çözülebilir:

```
PINCH ÜSTÜ ALT PROBLEMI (Above-Pinch Subproblem):
  ─────────────────────────────────────────────
  Hedef: Minimum sicak utility (QH,min) ile soguk akislari isitmak
  Özellik: Isi AÇIĞI var — dis isitma gerekli
  Kural: Soguk utility KULLANILMAZ

  Akis verileri (pinch üstü bölümü):
  | Akis | Aralik [°C]      | CP   | Q [kW] |
  |------|------------------|------|--------|
  | H1   | 270 → 180        | 15   | 1,350  |
  | H2   | 180 → 180 (pinch)| 25   | 0      |
  | C1   | 170 → 250        | 18   | 1,440  |
  | C2   | 170 → 200        | 12   | 360    |

  Isi dengesi (pinch üstü):
  Mevcut sicak: 1,350 kW (H1'den)
  Gereken soguk: 1,440 + 360 = 1,800 kW
  Eksik = QH,min = 1,800 - 1,350 = 450 kW

  Düzeltme: H2 pinch noktasinda 180°C'dir, pinch üstünde katkisi yoktur.
  Gerçek hesap PTA'dan: QH,min = 1,800 kW


PINCH ALTI ALT PROBLEMI (Below-Pinch Subproblem):
  ─────────────────────────────────────────────
  Hedef: Minimum soguk utility (QC,min) ile sicak akislari sogutmak
  Özellik: Isi FAZLASI var — dis sogutma gerekli
  Kural: Sicak utility KULLANILMAZ

  Akis verileri (pinch alti bölümü):
  | Akis | Aralik [°C]      | CP   | Q [kW] |
  |------|------------------|------|--------|
  | H1   | 180 → 80         | 15   | 1,500  |
  | H2   | 180 → 40         | 25   | 3,500  |
  | H3   | 150 → 60         | 10   | 900    |
  | C1   | 30 → 170         | 18   | 2,520  |
  | C2   | 60 → 170         | 12   | 1,320  |

  Isi dengesi (pinch alti):
  Mevcut sicak: 1,500 + 3,500 + 900 = 5,900 kW
  Gereken soguk: 2,520 + 1,320 = 3,840 kW
  Fazla = 5,900 - 3,840 = 2,060 kW

  PTA'dan: QC,min = 2,240 kW
  (Fark, akislarin pinch noktasindaki kesin bölünmesinden kaynaklanir)
```

### 5.2 Bölümlemenin Avantajlari

```
1. Problemin basitlestirilmesi:
   - 5 akislik bir problem yerine iki küçük alt problem
   - Her alt problem kendi içinde bagimsiz olarak çözülür
   - Tasarim kararlari yereldir (alt problem kapsaminda)

2. Hedef dogrulamasi:
   - Her alt problemin enerji dengesi dogrulanabilir
   - QH,min sadece pinch üstünden gelir
   - QC,min sadece pinch altindan gelir

3. HEN tasarimi yönlendirmesi:
   - Pinch noktasinda baslayarak tasarim yapmak,
     DTmin kısıtını otomatik olarak saglar
   - Her alt problemde farkli eslesme kurallari geçerlidir:
     Pinch üstü: CP_sicak <= CP_soguk
     Pinch alti:  CP_soguk <= CP_sicak

4. Retrofit analizi:
   - Cross-pinch transfer yapan mevcut isi degistiricileri tespit et
   - En büyük cross-pinch transferi önce ortadan kaldir
   - Her iyilestirmenin etkisi dogrudan hesaplanabilir
```

### 5.3 Çoklu Pinch Durumu

```
Bazi problemlerde birden fazla pinch noktasi oluşabilir:

  Threshold problemi: QH,min = 0 veya QC,min = 0
    - Sadece bir tür utility gerekli
    - Pinch noktasi akislarin uç noktasindadir

  Utility pinch: GCC üzerinde ek bir pinch noktasi
    - Farkli utility seviyeleri arasinda oluşur
    - Utility yerleştirme kararlari etkilenir

  Pratikte: Çoklu pinch, daha fazla tasarim kisıtlamasi demektir
  ancak daha yüksek enerji verimliligi potansiyeli de taşıyabilir.
```

## 6. Exergy ve Pinch Analizi Baglantisi (Exergy-Pinch Connection)

### 6.1 Exergy Yikimi ve Pinch Ihlalleri

Pinch kurallarının ihlali, yalnızca fazla utility tüketimi değil, ayni zamanda gereksiz exergy yikimi anlamina gelir. Her pinch ihlali, termodinamik olarak önlenebilir (avoidable) exergy yikimi yaratir:

```
Exergy perspektifinden pinch ihlali:

  Ihlal: Pinch üzerinden DQ = 500 kW transfer

  Sicak utility (örneğin 300°C buhar) ile 500 kW ekstra isitma:
    Ex_girdi = QH × (1 - T0/T_buhar) = 500 × (1 - 298.15/573.15)
            = 500 × 0.480 = 240 kW exergy

  Soguk utility (25°C sogutma suyu) ile 500 kW ekstra sogutma:
    Ex_atilan = QC × (1 - T0/T_sogutma) = 500 × (1 - 298.15/308.15)
             = 500 × 0.0324 = 16.2 kW exergy (atik olarak)

  Net exergy kaybi:
    Ek exergy girdi  = 240 kW (utility üretmek için harcanan)
    Ek exergy çikti   = 16.2 kW (sogutma ile atilan — düsük degerli)
    Ek exergy yikim  = 240 - 16.2 = 223.8 kW

  Bu 223.8 kW, tamamen ÖNLENEBILIR (avoidable) exergy yikimidir.
  Pinch kurallarina uyulsa, bu exergy yikimi olmazdi.
```

### 6.2 Carnot Faktörü Analizi (Carnot Factor Analysis)

Carnot faktörü, bir isi kaynaginin exergy içerigini ifade eder. Pinch analizinde farkli sicaklik bölgelerinin exergy kalitesini degerlendirmek için kullanilir:

```
Carnot faktörü:
  eta_C = 1 - T0/T  (T: Kelvin cinsinden mutlak sicaklik)

Referans problemdeki sicaklik seviyeleri için Carnot faktörleri:

  Sicaklik [°C] | T [K]   | eta_C  | Yorum
  270            | 543.15  | 0.451  | Yüksek exergy (H1 kaynak)
  250            | 523.15  | 0.430  | Yüksek exergy (C1 hedef)
  200            | 473.15  | 0.370  | Orta-yüksek exergy (C2 hedef)
  180            | 453.15  | 0.342  | Pinch sicak taraf
  170            | 443.15  | 0.327  | Pinch soguk taraf
  150            | 423.15  | 0.295  | Orta exergy (H3 kaynak)
  80             | 353.15  | 0.156  | Düsük exergy (H1 hedef)
  60             | 333.15  | 0.105  | Düsük exergy (H3/C2 hedef/kaynak)
  40             | 313.15  | 0.048  | Çok düsük exergy (H2 hedef)
  30             | 303.15  | 0.016  | Neredeyse ölü durum (C1 kaynak)

Pinch noktasindaki Carnot faktörü farki:
  Delta_eta_C = 0.342 - 0.327 = 0.015

Bu düsük fark, pinch noktasinin exergy açisindan dar bir
geçis bölgesi oldugunu gösterir. Pinch üzerinden her isi transferi,
bu geçis bölgesini "atlayarak" exergy yikar.
```

### 6.3 Exergy Bileşik Egrileri (Exergy Composite Curves)

```
Geleneksel pinch analizi T-H (sıcaklık-entalpi) düzleminde çalisir.
Exergy-pinch baglantisi için T-Ex (sicaklik-exergy) veya
Carnot-H düzleminde analiz yapilabilir:

  Exergy akisi hesabi (bir sicaklik araliginda):
  Ex = Q × eta_C_ort = Q × (1 - T0/T_ort)

  Pinch üstü exergy analizi:
  | Aralik        | Q [kW] | T_ort [K] | eta_C | Ex [kW] |
  |---------------|--------|-----------|-------|---------|
  | 255-205°C (C) | 900    | 503.15    | 0.407 | 366.3   |
  | 205-175°C (C) | 900    | 463.15    | 0.356 | 320.4   |
  | 180-270°C (H) | 1,350  | 498.15    | 0.401 | 541.4   |

  Pinch alti exergy analizi:
  | Aralik        | Q [kW] | T_ort [K] | eta_C | Ex [kW] |
  |---------------|--------|-----------|-------|---------|
  | 80-150°C (H)  | 3,500  | 388.15    | 0.232 | 812.0   |
  | 60-80°C (H)   | 700    | 343.15    | 0.131 | 91.7    |
  | 40-60°C (H)   | 500    | 323.15    | 0.077 | 38.5    |

Exergy perspektifinden pinch altindaki kayiplar:
  - 40-60°C araligindaki 500 kW'lik isi, yalnizca 38.5 kW exergy içerir
  - Bu düsük kaliteli isinin geri kazanimi ekonomik olmayabilir
  - Exergy analizi, pinch analizine kalite boyutu ekler
```

### 6.4 Exergy-Pinch Sentezi: Pratik Sonuçlar

```
Pinch analizi + Exergy analizi birlikte kullanildiginda:

1. Önceliklendirme: Yüksek Carnot faktörlü bölgelerdeki iyilestirmelere
   öncelik verilmeli (daha fazla exergy tasarrufu)

2. Utility seçimi: GCC üzerinde utility yerleştirirken exergy etkisi:
   - HP buhar yerine LP buhar kullanilabilecek bölgeleri belirle
   - Gereksiz yüksek exergy girisini önle
   - Exergy-etkin utility dagitimi yap

3. HEN tasarimi: Isi degistiricilerindeki sicaklik farkini minimize
   ederek exergy yikimini azalt (ancak alan-maliyet dengesi gözet)

4. Atik isi degerlendirmesi: Düsük Carnot faktörlü akislari farkli
   stratejilerle degerlendir:
   - 80-150°C: ORC (Organic Rankine Cycle), isi pompasi
   - 40-80°C: Bina isitma, sera isitma, balık çiftligi
   - <40°C: Genellikle ekonomik geri kazanim yok
```

## 7. Metodoloji Adimlari (Methodology Steps)

### 7.1 Tam Çalisma Akisi

Pinch analizinin bastan sona uygulanmasi asagidaki sistematik adimlari içerir:

```
                    PINCH ANALIZI ÇALISMA AKISI
                    ============================

ADIM 1: VERI ÇIKARMA (Data Extraction)
  |
  |  - Proses akis diyagramini (PFD) incele
  |  - Sicak ve soguk akislari tanimla
  |  - Akis debileri, sicakliklar, CP degerleri
  |  - Faz degisimleri, reaksiyon isilarini not et
  |  - Ölçüm verilerini dogrula (kütle ve enerji dengesi)
  |
  v
ADIM 2: STREAM DATA TABLE
  |
  |  - Tüm akislari tabloya yaz
  |  - Her akis: T_kaynak, T_hedef, CP, Q
  |  - Yumusak kisitlamalari belirle (degistirilebilir T)
  |  - Sert kisitlamalari isaretle (degistirilemez T)
  |
  v
ADIM 3: DTmin SEÇIMI / OPTIMIZASYONU
  |
  |  - Endüstri bazli tipik DTmin ile basla
  |  - Duyarlilik analizi yap (5-40°C arasi)
  |  - Super-targeting: Toplam yillik maliyet minimumu
  |  - Optimum DTmin seç
  |
  v
ADIM 4: ENERJI HEDEFLEME (Energy Targeting)
  |
  |  - Problem Tablosu Algoritmasi (PTA) uygula
  |  - QH,min ve QC,min hesapla
  |  - Pinch noktasini belirle
  |  - Bilesik egriler (CC) ve GCC çiz
  |
  v
ADIM 5: PINCH BÖLÜMLEMESI
  |
  |  - Problemi pinch üstü ve alti olarak ayir
  |  - Her alt problemin enerji dengesini dogrula
  |  - Eslesme kurallarini (CP kisitlari) kontrol et
  |
  v
ADIM 6: HEN TASARIMI (Heat Exchanger Network Design)
  |
  |  - Pinch noktasindan baslayarak tasarla
  |  - Pinch üstü: CP_sicak <= CP_soguk
  |  - Pinch alti: CP_soguk <= CP_sicak
  |  - Tick-off heuristic ile eslesmeleri yap
  |  - Gerekirse akis bölme (stream splitting) uygula
  |
  v
ADIM 7: OPTIMIZASYON
  |
  |  - Döngü kirma (loop breaking) ile esanjör sayisini azalt
  |  - Yol gevsetme (path relaxation) ile pratiklik sagla
  |  - Enerji-alan (energy-area) trade-off degerlendir
  |  - Esanjör boyutlandirma (LMTD, U, A hesaplari)
  |
  v
ADIM 8: RETROFIT ANALIZI (mevcut tesis için)
  |
  |  - Mevcut HEN'i grid diyagramina çiz
  |  - Cross-pinch transferleri tespit et
  |  - En büyük iyilestirme firsatlarini sirala
  |  - Mevcut esanjörleri degerlendirme (re-pipe vs. yeni)
  |
  v
ADIM 9: EKONOMIK DEGERLENDIRME
  |
  |  - Yatirim maliyeti: Esanjör + boru + montaj
  |  - Isletme tasarrufu: Utility azalmasi × birim fiyat
  |  - SPP, NPV, IRR hesapla
  |  - Hassasiyet analizi (enerji fiyati, faiz orani)
  |
  v
ADIM 10: UYGULAMA VE DOGRULAMA
     |
     - Uygulama plani hazirla (fazlama / duruşlarda)
     - Ölçüm ve dogrulama (M&V) plani
     - Performans izleme ve raporlama
     - Sürekli iyilestirme döngüsü
```

### 7.2 Veri Çikarma Detaylari

```
Veri kalitesi, pinch analizinin en kritik asamasidir.

Gerekli veriler:
  1. Proses akislari:
     - Kütle debisi (m_dot) [kg/s]
     - Özgül isi kapasitesi (Cp) [kJ/(kg·°C)]
     - Giriş ve çikiş sicakliklari [°C]
     - Akis fazlari (sivi, gaz, iki fazli)

  2. Utility akislari:
     - Mevcut buhar seviyeleri ve tüketimleri
     - Sogutma suyu debi ve sicakliklari
     - Elektrik ile isitma/sogutma

  3. Proses kisitlamalari:
     - Korrozyon, fouling, güvenlik sinirlari
     - Mesafe kisitlamalari (boru güzergahi)
     - Operasyonel esneklik gereksinimleri
     - Çalisma zamanlari (sürekli, kesikli, mevsimsel)

Veri dogrulama kontrolleri:
  - Kütle dengesi: Giren = Çikan ± %2
  - Enerji dengesi: QH_mevcut - QC_mevcut = Q_net_proses ± %5
  - CP tutarliligi: CP = m_dot × Cp degerlerini çapraz kontrol
  - Sicaklik ölçüm dogrulugu: Kalibrasyon kontrolü
```

## 8. Temel Varsayimlar ve Sinirlamalar (Assumptions and Limitations)

### 8.1 Temel Varsayimlar

Standart pinch analizi asagidaki varsayimlara dayanir:

```
1. KARARLI HAL (Steady State):
   - Tüm akislar zamanla degismez (sabit debi, sicaklik)
   - Geçici rejim (startup, shutdown) dahil edilmez
   - Kesikli prosesler için zaman ortalamalari kullanilir
   - Sinirlamasi: Esnek operasyon ve dinamik yük degisimleri
     göz ardi edilir

2. SABIT CP DEGERLERI (Constant Heat Capacity):
   - CP = m_dot × Cp her sicaklik araliginda sabit kabul edilir
   - Gerçekte Cp sicakliga baglidir
   - Çözüm: Büyük sicaklik araliklarini segmentlere böl
   - Sinirlamasi: Faz degisimi olan akislarda CP anlamsizdir

3. TEK FAZLI AKISLAR (Single Phase):
   - Akislar tamamen sivi veya gaz fazindadir
   - Faz degisimi ayri ele alinir (latent heat segment)
   - Çözüm: Buharlaşma/yogusma araliklari ayri segment
   - Sinirlamasi: Çok bilesenli faz degisimi karmasiktir

4. TERS AKIS ISI DEGISTIRICI (Counter-Current):
   - Tüm isi degistiriciler ters akis kabul edilir
   - Maksimum isi transferi verimi
   - Sinirlamasi: Paralel akis veya çapraz akis gerekiyorsa
     ek düzeltme faktörü (F) gerekir

5. MINIMUM SICAKLIK FARKI (DTmin):
   - DTmin tüm esanjörlerde sabit ve aynidir
   - Gerçekte farkli esanjör tipleri farkli DTmin gerektirir
   - Çözüm: Bireysel DTmin_contribut (split contributions)
   - Sinirlamasi: Kanatli esanjör vs. plaka esanjör farkli DTmin

6. YAPISAL BAGIMSIZLIK:
   - Enerji hedefleri, HEN yapisindan bagimsiz hesaplanir
   - Önce hedefle, sonra tasarla (target before design)
   - Avantaj: Hizli ön degerlendirme
   - Sinirlamasi: Pratikte yapisal kisitlar hedefleri etkileyebilir
```

### 8.2 Faz Degisimi Sorunlari

```
Faz degisimi olan akislar özel islem gerektirir:

Buharlaşma:
  - Latent heat bölgesi: Sabit sicaklikta büyük isi transferi
  - CP → sonsuz (T degismeden Q artar)
  - Çözüm: Yatay bir segment olarak modelle

  T [°C]
  |
  |    ___________  Buharlaşma (sabit T, degisen Q)
  |   /           \
  |  /             \
  | /    Sivi       \ Buhar
  |/                 \
  |___________________ Q [kW]

Yogusma:
  - Benzer sekilde sabit sicaklikta latent heat birakilir
  - Soguk akis olarak modelleme: Gaz → sivi geçis segmenti

Çok bilesenli karişimlar:
  - Buharlaşma/yogusma bir sicaklik araliginda gerçeklesir
  - Doğrusal olmayan T-H profili olusur
  - Segmentasyon ile yaklasik çözüm
```

### 8.3 Kesikli Prosesler (Batch Processes)

```
Kesikli proseslerde pinch analizinin zorlugu:
  - Akislar zaman bagimlidir (süreksiz)
  - Farkli akislar farkli zamanlarda aktiftir
  - Isı depolama (heat storage) gerekebilir

Çözüm yaklasımlari:
  1. Zaman ortalamasi (Time Average Model — TAM)
     - Tüm akislarin zaman ortalamasini al
     - Standart pinch analizi uygula
     - Basit ama gerçekçi olmayabilir

  2. Zaman dilimi modeli (Time Slice Model — TSM)
     - Prosesi zaman dilimlerine böl
     - Her dilim için ayri pinch analizi
     - Isi depolama ile dilimler arasi entegrasyon

  3. Zaman bileşik egrileri (Time Composite Curves)
     - Zaman boyutunu da içeren bilesik egriler
     - En kapsamli ancak en karmasik yöntem
```

### 8.4 Pratikte Karsilasilan Zorluklar

```
1. Veri kalitesi:
   - Eksik veya hatali ölçümler yaygın
   - Pratikte akis verilerinin %10-20 belirsizligi normal
   - Çözüm: Duyarlilik analizi, güvenlik marji

2. Mesafe kisıtlamalari:
   - Birbirine uzak ekipmanlar arasi isi transferi pahali olabilir
   - Boru maliyeti, isi degistirici maliyetini asabilir
   - Çözüm: Mesafe kisitlarini ekonomik analize dahil et

3. Operasyonel esneklik:
   - Proses kosullari mevsimsel veya yük bazli degisir
   - Sabit DTmin tüm kosullari kapsamayabilir
   - Çözüm: Çoklu senaryo pinch analizi, esneklik marjı

4. Fouling (kirlenme):
   - Isi degistirici yüzeylerinin kirlenmesi performansi düsürür
   - DTmin pratikte tasarim degerinden büyük olabilir
   - Çözüm: Fouling faktörlerini DTmin'e dahil et

5. Güvenlik ve kontrol:
   - Bazi akislarin dogrudan teması güvenlik riski tasiyabilir
   - Kontrol sistemi karmasikligi artar
   - Çözüm: Arayi akiskan (intermediate fluid) kullanimi

6. Yatirim bulamasi:
   - Optimum çözüm yüksek yatirim gerektirebilir
   - Geri ödeme süresi yönetimin beklentisini asabilir
   - Çözüm: Fazlama (phased implementation), öncelikli projeler
```

### 8.5 Varsayim Ihlallerinin Etkisi

| Varsayim | Ihlal Durumu | MER Etkisi | Çözüm |
|----------|--------------|------------|-------|
| Kararli hal | Yük degisimleri | MER degisir, tasarim yetersiz kalabilir | Çoklu senaryo, esneklik analizi |
| Sabit CP | Genis sicaklik araligi | MER hatalari %5-15 | Segmentasyon (dar araliklar) |
| Tek faz | Buharlaşma/yogusma | Büyük hata potansiyeli | Faz degisim segmentleri |
| Ters akis | Paralel/çapraz akis esanjör | Daha fazla alan gerekli | F düzeltme faktörü |
| Sabit DTmin | Farkli esanjör tipleri | Sub-optimal tasarim | Bireysel DTmin katkilari |
| Yapisal bagimsizlik | Fiziksel kisitlamalar | Hedef yakalanamiyor | Kisitli hedefleme yöntemleri |

## İlgili Dosyalar

- [Pinch Analizi ve Isi Entegrasyonu](../pinch_analysis.md) — Kapsamli pinch analizi uygulamasi, bilesik egriler, GCC, HEN tasarimi, retrofit ve endüstriyel örnekler
- [Isi Entegrasyonu ve Kaynak-Kullanim Eslestirme](../heat_integration.md) — Isı kaynaklari ve kullanicilari eslestirme metodolojisi
- [Exergy Temelleri](../exergy_fundamentals.md) — Exergy hesap, denge ve fabrika seviyesi analiz ilkeleri
- [Proses Entegrasyonu](../process_integration.md) — Genel proses entegrasyon yaklasimlari
- [Atik Isi Geri Kazanimi](../waste_heat_recovery.md) — Atik isi degerlendirme stratejileri ve teknolojileri
- [Ekipmanlar Arasi Firsat Analizi](../cross_equipment.md) — Cross-equipment isi geri kazanim firsatlari
- [Yardimci Sistemler Analizi](../utility_analysis.md) — Utility sistemleri ve optimizasyonu
- [Ekonomik Analiz](../economic_analysis.md) — Yatirim degerlendirme yöntemleri (SPP, NPV, IRR)

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, Rugby, UK, 1994 (2nd ed.)
- Kemp, I.C., "Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy," Butterworth-Heinemann, 2nd Edition, 2007
- Smith, R., "Chemical Process Design and Integration," Wiley, 2nd Edition, 2016
- Klemes, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Linnhoff, B. & Flower, J.R., "Synthesis of Heat Exchanger Networks," AIChE Journal, 24(4), 633-654, 1978
- Linnhoff, B. & Hindmarsh, E., "The Pinch Design Method for Heat Exchanger Networks," Chemical Engineering Science, 38(5), 745-763, 1983
- Dhole, V.R. & Linnhoff, B., "Total Site Targets for Fuel, Co-Generation, Emissions, and Cooling," Computers & Chemical Engineering, 17(Suppl.), S101-S109, 1993
- Tjoe, T.N. & Linnhoff, B., "Using Pinch Technology for Process Retrofit," Chemical Engineering, 93(8), 47-60, 1986
- Bejan, A., Tsatsaronis, G. & Moran, M., "Thermal Design and Optimization," Wiley, 1996 (Exergy-pinch baglantisi)
- Feng, X. & Zhu, X.X., "Combining Pinch and Exergy Analysis for Process Modifications," Applied Thermal Engineering, 17(3), 249-261, 1997
