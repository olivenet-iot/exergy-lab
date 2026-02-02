---
title: "Gelismis Exergy Analizi - 8 Adimli Hesaplama Metodolojisi"
category: "factory/advanced_exergy"
keywords:
  - advanced exergy analysis
  - avoidable exergy destruction
  - unavoidable exergy destruction
  - endogenous exergy destruction
  - exogenous exergy destruction
  - hybrid cycle simulation
  - sensitivity analysis
  - exergy splitting
related_files:
  - knowledge/factory/advanced_exergy/ideal_conditions.md
  - knowledge/factory/advanced_exergy/interpretation.md
  - knowledge/factory/advanced_exergy/equipment_specific/
  - knowledge/factory/exergy_flow_analysis.md
  - knowledge/factory/exergy_fundamentals.md
  - knowledge/factory/methodology.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - skills/core/exergy_fundamentals.md
  - skills/factory/factory_analyst.md
use_when: "Kullanici gelismis exergy analizi metodolojisi, kacinilamaz/kacinilabilir veya endojen/ekzojen exergy yikimi ayristirmasi hakkinda bilgi istediginde"
priority: high
last_updated: 2025-05-15
---

# Gelismis Exergy Analizi: 8 Adimli Hesaplama Metodolojisi

## Genel Bakis

Gelismis exergy analizi (advanced exergy analysis), konvansiyonel exergy analizinin otesine gecerek her bilesen icindeki exergy yikimini dort kategoriye ayirir:

1. **Endojen (Endogenous):** Bilesenin kendi icindeki tersinmezliklerden kaynaklanan
2. **Ekzojen (Exogenous):** Diger bilesen etkilesimlerinden kaynaklanan
3. **Kacinilabilir (Avoidable):** Teknolojik/ekonomik olarak azaltilabilir
4. **Kacinilmaz (Unavoidable):** Mevcut teknoloji ile azaltilamayan

Bu dort kategori birlestirilerek **4-yollu ayristirma (4-way splitting)** elde edilir:

| Kategori | Kisaltma | Anlam |
|----------|----------|-------|
| Endojen-Kacinilabilir | I_EN_AV | Bilesenin kendisi iyilestirilerek azaltilabilir |
| Endojen-Kacinilmaz | I_EN_UN | Bilesenin kendi fiziksel siniri |
| Ekzojen-Kacinilabilir | I_EX_AV | Diger bilesenler iyilestirilerek azaltilabilir |
| Ekzojen-Kacinilmaz | I_EX_UN | Sistem genelinin fiziksel siniri |

> **Neden Onemli:** Konvansiyonel analiz sadece "ne kadar exergy yikiliyor" der. Gelismis analiz "bu yikimin ne kadari onlenebilir ve nerede mudahale edilmeli" sorusunu yanitlar.

---

## ADIM 1: Sistem Siniri ve Bilesen Tanimlama

### 1.1 Kontrol Hacmi Cizme

Analiz edilecek sistemin sinirlarini acik ve net bicimde tanimlayin:

- Sistemin fiziksel sinirlari belirlenir
- Cevre ile etkilesim noktalari isaretlenir
- Isil, mekanik ve kimyasal etkilesimler tanilanir

### 1.2 Bilesen Tanimlama ve Numaralandirma

Her bilesen (component) benzersiz bir indeks alir:

```
k = 1, 2, 3, ..., n    (n: toplam bilesen sayisi)
```

**Bilesen tanimlama kurallari:**
- Her bilesen tek bir termodinamik islem yapmalidir
- Bilesenler arasi akislar net tanimlanmalidir
- Kontrol hacmi icinde kayip akim (leakage) olmamalidir

### 1.3 Akislari Tanimlama

Her akis icin uc temel buyukluk belirlenir:

| Akis Parametresi | Simge | Birim | Aciklama |
|-------------------|-------|-------|----------|
| Kutle debisi (mass flow rate) | m_dot | kg/s | Kutle korumu sarti |
| Enerji akisi (energy flow) | E_dot | kW | Birinci yasa dengesi |
| Exergy akisi (exergy flow) | Ex_dot | kW | Ikinci yasa dengesi |

Her akis noktasi icin sicaklik, basinc, entalpi, entropi ve exergy degerleri hesaplanir:

```
ex_i = (h_i - h_0) - T_0 * (s_i - s_0)    [kJ/kg]
Ex_dot_i = m_dot_i * ex_i                   [kW]
```

Burada:
- `h_0`, `s_0`: Olum durumu (dead state) entalpi ve entropi degerleri
- `T_0`: Olum durumu sicakligi (genellikle 25 degC = 298.15 K)

---

## ADIM 2: Konvansiyonel Exergy Analizi

### 2.1 Exergy Dengesi

Her bilesen `k` icin exergy dengesi yazilir:

```
I_k = Ex_F,k - Ex_P,k - Ex_L,k
```

Burada:
- `I_k`: Bilesen k'deki exergy yikimi (exergy destruction) [kW]
- `Ex_F,k`: Yakit exergy'si (fuel exergy) - bilesen girdisi [kW]
- `Ex_P,k`: Urun exergy'si (product exergy) - faydali cikti [kW]
- `Ex_L,k`: Exergy kaybi (exergy loss) - cevre ile kayip [kW]

### 2.2 Performans Gostergeleri

**Exergy Verimi (Exergetic Efficiency):**
```
epsilon_k = Ex_P,k / Ex_F,k
```

**Exergy Yikim Orani (Exergy Destruction Ratio):**
```
y_k = I_k / Ex_F,total
```

Bu oran, her bilesenin toplam sistem exergy yikimindan ne kadar pay aldigini gosterir.

**Exergy Yikim Yogunlugu (Exergy Destruction Density):**
```
y*_k = I_k / I_total
```

### 2.3 Konvansiyonel Analizin Sinirliliklari

Konvansiyonel analiz su sorulari yanitlayamaz:
- Bu yikimin ne kadari kacinilamazdir?
- Bu yikimin ne kadari bilesenin kendisinden, ne kadari diger bilesenlerden kaynaklanir?
- Hangi bilesenin iyilestirilmesi sisteme en cok fayda saglar?

> **Not:** Bu sinirliliklari asmak icin Adim 3-8 arasindaki gelismis analiz adimlarina ihtiyac vardir.

---

## ADIM 3: Kacinilmaz Kosullar Belirleme

### 3.1 En Iyi Mevcut Teknoloji (BAT) Parametreleri

Her bilesen icin teknolojik ve ekonomik olarak elde edilebilecek en iyi performans parametreleri belirlenir. Bu parametrelere **kacinilmaz kosullar (unavoidable conditions)** denir.

> **Referans:** `ideal_conditions.md` dosyasinda ekipman turune gore BAT parametreleri mevcuttur.

### 3.2 Parametre Seti Olusturma

| Bilesen Turu | Parametre | Gercek Deger | Kacinilmaz Deger | Kaynak |
|--------------|-----------|-------------|-------------------|--------|
| Isi degistirici (heat exchanger) | Delta_T_min | 15-25 K | 3-5 K | Tsatsaronis (2009) |
| Kompressor (compressor) | eta_is | 0.75-0.85 | 0.92-0.95 | Morosuk (2013) |
| Turbin (turbine) | eta_is | 0.80-0.88 | 0.93-0.96 | Petrakopoulou (2012) |
| Pompa (pump) | eta_is | 0.70-0.80 | 0.90-0.93 | Bejan et al. (1996) |
| Yanici/Kazan (combustor/boiler) | Hava fazlasi (excess air) | %20-40 | %5-10 | Kelly (2009) |

### 3.3 Secim Kriterleri

Kacinilmaz kosula karar verirken:

1. **Literatur taramasi:** Benzer sistemlerdeki en iyi rapor edilmis degerler
2. **Uretici verileri:** Piyasadaki en verimli ekipman
3. **Fiziksel sinirlar:** Termodinamik olanaksizliklari goz ardi etme
4. **Ekonomik fizibilite:** Makul yatirim maliyeti icinde kalan degerler

> **Uyari:** Kacinilmaz kosul secimi sonuclari onemli olcude etkiler. Hassasiyet analizi mutlaka yapilmalidir (Adim 8+ bakiniz).

---

## ADIM 4: Kacinilmaz Cevrim Simulasyonu

### 4.1 Simulasyon Kurulumu

**TUM** bilesenler kacinilmaz kosullara ayarlanir ve sistem tekrar simule edilir:

```
I_UN,k = I_k(tum bilesenler kacinilmaz kosullarda)
```

### 4.2 Onemli Noktalar

- Sistem baslanma kaynagi (boundary conditions) ayni tutulur
- Sadece bilesen icleri parametreleri degisir
- Kutle ve enerji dengeleri korunmalidir
- CoolProp veya benzeri kutuphane ile termodinamik ozellikler yeniden hesaplanir

### 4.3 Ornek Hesaplama Sablonu

```
Gercek sistem:
  Bilesen 1 (kompressor): eta_is = 0.80
  Bilesen 2 (isi degistirici): Delta_T_min = 20 K

Kacinilmaz simulasyon:
  Bilesen 1 (kompressor): eta_is = 0.94
  Bilesen 2 (isi degistirici): Delta_T_min = 3 K

Sonuc: Her bilesen icin I_UN,k degeri elde edilir.
```

---

## ADIM 5: Kacinilabilir Exergy Yikimi

### 5.1 Hesaplama

Kacinilabilir exergy yikimi, gercek deger ile kacinilmaz deger arasindaki farktir:

```
I_AV,k = I_k - I_UN,k
```

Burada:
- `I_AV,k`: Bilesen k'nin kacinilabilir exergy yikimi [kW]
- `I_k`: Konvansiyonel analizdeki toplam exergy yikimi [kW]
- `I_UN,k`: Kacinilmaz exergy yikimi [kW]

### 5.2 Yorumlama

| Durum | Anlam | Aksiyon |
|-------|-------|---------|
| I_AV,k >> I_UN,k | Buyuk iyilestirme potansiyeli | Oncelikli mudahale |
| I_AV,k << I_UN,k | Sinirli iyilestirme potansiyeli | Dusuk oncelik |
| I_AV,k / I_k > 0.50 | Kacinilabilir pay yuksek | Teknoloji yukseltme (upgrade) degerlendir |
| I_AV,k / I_k < 0.20 | Kacinilabilir pay dusuk | Mevcut teknoloji sinirina yakin |

---

## ADIM 6: Hibrit Cevrimler ve Endojen Exergy Yikimi

### 6.1 Hibrit Cevrim Kavrami

Her bilesen `k` icin bir hibrit cevrim (hybrid cycle) olusturulur:

- **Bilesen k:** Gercek (actual) kosullarinda calisir
- **Diger tum bilesenler:** Ideal (tersinir / reversible) kosullarinda calisir

```
I_EN,k = I_k(k=gercek, diger bilesenler=ideal)
```

### 6.2 Simulasyon Sayisi

`n` bilesenli bir sistem icin **n adet** hibrit cevrim simulasyonu gerekir:

```
Hibrit Cevrim 1: Bilesen 1 gercek, Bilesen 2..n ideal
Hibrit Cevrim 2: Bilesen 2 gercek, Bilesen 1,3..n ideal
...
Hibrit Cevrim n: Bilesen n gercek, Bilesen 1..n-1 ideal
```

### 6.3 Ideal Kosullar

Ideal (tersinir) kosullar, kacinilmaz kosullardan farklidir:

| Parametre | Kacinilmaz (Unavoidable) | Ideal (Reversible) |
|-----------|--------------------------|---------------------|
| Kompressor eta_is | 0.94 | 1.00 |
| Turbin eta_is | 0.96 | 1.00 |
| Isi degistirici Delta_T_min | 3 K | 0 K |
| Basinc kaybi | Minimum | 0 |
| Isi kaybi | Minimum | 0 |

> **Dikkat:** Ideal kosullarda bazi bilesenler sifir exergy yikimi uretir. Bu, hibrit cevrimlerde sayisal zorluklar yaratabilir. Cok kucuk bir epsilon (ornegin 0.001) eklenebilir.

---

## ADIM 7: Ekzojen Exergy Yikimi

### 7.1 Hesaplama

Ekzojen exergy yikimi, toplam ile endojen kismin farkidir:

```
I_EX,k = I_k - I_EN,k
```

### 7.2 Anlami

- **I_EN,k (Endojen):** Bilesen k'nin kendi tersinmezlikleri nedeniyle olusan yikim. Bu bilesen iyilestirilirse dogrudan azalir.
- **I_EX,k (Ekzojen):** Diger bilesen etkilesimlerinden kaynaklanan yikim. Bu bilesenin kendisi iyilestirilse bile azalmaz; diger bilesenler iyilestirilmelidir.

### 7.3 Yorum Tablosu

| Oran (I_EX,k / I_k) | Yorum |
|----------------------|-------|
| < 0.25 | Yikim agirliki olarak endojen; bilesen kendisi iyilestirilmeli |
| 0.25 - 0.50 | Karma etki; hem bilesen hem sistem optimizasyonu gerekli |
| > 0.50 | Yikim agirliki olarak ekzojen; diger bilesenler iyilestirilmeli |

---

## ADIM 8: 4-Yollu Birlestirme

### 8.1 Alt Kategoriler

Endojen/ekzojen ve kacinilabilir/kacinilmaz ayristirmalari birlestirilerek dort alt kategori elde edilir:

**Endojen-Kacinilmaz (I_EN_UN,k):**
```
I_EN_UN,k = I_EN,k(tum bilesenler kacinilmaz kosullarda, k=gercek)
```
Bu deger icin ek bir hibrit simulasyon gerekir: Bilesen k gercek kosullarda, diger bilesenler kacinilmaz kosullarda.

> **Aciklama:** Aslinda I_EN_UN,k icin bilesen k gercek, diger bilesenler ideal olan hibrit cevrimin kacinilmaz versiyonu kullanilir. Pratikte, bilesen k gercek ve diger bilesenler kacinilmaz kosullardaki hibrit simulasyondan elde edilir.

**Endojen-Kacinilabilir (I_EN_AV,k):**
```
I_EN_AV,k = I_EN,k - I_EN_UN,k
```

**Ekzojen-Kacinilabilir (I_EX_AV,k):**
```
I_EX_AV,k = I_AV,k - I_EN_AV,k
```

**Ekzojen-Kacinilmaz (I_EX_UN,k):**
```
I_EX_UN,k = I_UN,k - I_EN_UN,k
```

### 8.2 Dogrulama

Dort alt kategorinin toplami, konvansiyonel exergy yikimine esit olmalidir:

```
I_EN_AV,k + I_EN_UN,k + I_EX_AV,k + I_EX_UN,k = I_k
```

Bu denklem **mutlaka** kontrol edilmelidir. Esitsizlik varsa hesapta hata vardir.

### 8.3 Onceliklendirme Matrisi

| Oncelik | Kategori | Aksiyon |
|---------|----------|---------|
| 1 (en yuksek) | I_EN_AV,k yuksek | Bilesen k'yi iyilestir (retrofit, degisim) |
| 2 | I_EX_AV,k yuksek | Diger bilesen(ler)i iyilestir |
| 3 | I_EN_UN,k yuksek | Bilesen k'nin teknolojik siniri; yeni teknoloji ara |
| 4 (en dusuk) | I_EX_UN,k yuksek | Sistem genelinin fiziksel siniri; yapisal degisiklik gerekli |

---

## Dogrulama Kontrolleri

### Toplam Denge Kontrolu

```
Kontrol 1: I_EN,k + I_EX,k = I_k              (her k icin)
Kontrol 2: I_AV,k + I_UN,k = I_k              (her k icin)
Kontrol 3: I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN = I_k  (her k icin)
Kontrol 4: sum(I_k) = I_total                  (tum bilesenler)
```

### Negatif Deger Kontrolu

Eger herhangi bir alt kategori **negatif** deger veriyorsa:

- Kacinilmaz parametre secimlerini gozden gecir
- Ideal kosul tanimlarini kontrol et
- Termodinamik ozellik hesaplamalarini dogrula
- Kutle ve enerji dengelerini yeniden kontrol et

> **Onemli:** Negatif deger fiziksel olarak anlamsizdir ve hesaplama hatasina isaret eder.

### Fiziksel Anlam Kontrolu

- I_UN,k < I_k olmalidir (kacinilmaz, toplamdan buyuk olamaz)
- I_EN,k >= 0 olmalidir
- I_AV,k >= 0 olmalidir
- epsilon_k (exergy verimi) 0 ile 1 arasinda olmalidir

### Hassasiyet Kontrolu

Sonuclarin kacinilmaz parametre secimine ne kadar duyarli oldugu kontrol edilmelidir (asagidaki Hassasiyet Analizi Rehberi bolumune bakiniz).

---

## Tam Hesaplama Ornegi: 2-Bilesenli Sistem

### Sistem Tanimi

Basit bir gaz turbini sistemi: Kompressor (K) ve Turbin (T)

```
Hava girisi --> [Kompressor K] --> [Yanici] --> [Turbin T] --> Egzoz
                     |                              |
                     <---- Mekanik guc aktarimi ----->
```

> **Not:** Ornegin sadelestirilmesi icin yanici ayri bir bilesen olarak modellenmiyor; isi ekleme olarak varsayiliyor.

### Verilen Degerler

| Parametre | Deger | Birim |
|-----------|-------|-------|
| Hava kutle debisi (m_dot) | 1.0 | kg/s |
| Cevre sicakligi (T_0) | 298.15 | K |
| Cevre basinci (P_0) | 100 | kPa |
| Kompressor cikis basinci (P_2) | 800 | kPa |
| Turbin giris sicakligi (T_3) | 1200 | K |
| Kompressor izentropik verim (eta_is,K) | 0.82 | - |
| Turbin izentropik verim (eta_is,T) | 0.85 | - |
| Hava: ideal gaz, c_p = 1.005 kJ/(kg.K), k = 1.4 | | |

### ADIM 1: Akis Noktalarinin Belirlenmesi

```
Nokta 1 (kompressor girisi):  T_1 = 298.15 K, P_1 = 100 kPa
Nokta 2 (kompressor cikisi):  P_2 = 800 kPa
Nokta 3 (turbin girisi):      T_3 = 1200 K, P_3 = 800 kPa
Nokta 4 (turbin cikisi):      P_4 = 100 kPa
```

**Kompressor cikis sicakligi:**
```
T_2s = T_1 * (P_2/P_1)^((k-1)/k) = 298.15 * (800/100)^(0.4/1.4)
T_2s = 298.15 * 8^(0.2857) = 298.15 * 1.8114 = 540.0 K

T_2 = T_1 + (T_2s - T_1) / eta_is,K
T_2 = 298.15 + (540.0 - 298.15) / 0.82
T_2 = 298.15 + 294.94 = 593.1 K
```

**Turbin cikis sicakligi:**
```
T_4s = T_3 * (P_4/P_3)^((k-1)/k) = 1200 * (100/800)^(0.2857)
T_4s = 1200 * (0.125)^(0.2857) = 1200 * 0.5523 = 662.7 K

T_4 = T_3 - eta_is,T * (T_3 - T_4s)
T_4 = 1200 - 0.85 * (1200 - 662.7)
T_4 = 1200 - 456.7 = 743.3 K
```

### ADIM 2: Konvansiyonel Exergy Analizi

**Exergy hesabi (ideal gaz icin):**
```
ex_i = c_p * (T_i - T_0) - T_0 * c_p * ln(T_i / T_0) + T_0 * R * ln(P_i / P_0)
```
Hava icin R = 0.287 kJ/(kg.K)

```
Nokta 1: ex_1 = 0 kJ/kg  (olum durumu)

Nokta 2: ex_2 = 1.005*(593.1-298.15) - 298.15*1.005*ln(593.1/298.15) + 298.15*0.287*ln(800/100)
         ex_2 = 296.42 - 298.15*1.005*0.6867 + 298.15*0.287*2.0794
         ex_2 = 296.42 - 205.72 + 177.93
         ex_2 = 268.63 kJ/kg

Nokta 3: ex_3 = 1.005*(1200-298.15) - 298.15*1.005*ln(1200/298.15) + 298.15*0.287*ln(800/100)
         ex_3 = 905.86 - 298.15*1.005*1.3928 + 177.93
         ex_3 = 905.86 - 417.31 + 177.93
         ex_3 = 666.48 kJ/kg

Nokta 4: ex_4 = 1.005*(743.3-298.15) - 298.15*1.005*ln(743.3/298.15) + 298.15*0.287*ln(100/100)
         ex_4 = 447.37 - 298.15*1.005*0.9128 + 0
         ex_4 = 447.37 - 273.44
         ex_4 = 173.93 kJ/kg
```

**Exergy akislari (m_dot = 1.0 kg/s):**
```
Ex_1 = 0 kW
Ex_2 = 268.63 kW
Ex_3 = 666.48 kW
Ex_4 = 173.93 kW
```

**Kompressor (K) exergy dengesi:**
```
Ex_F,K = W_K = m_dot * c_p * (T_2 - T_1) = 1.0 * 1.005 * (593.1 - 298.15) = 296.42 kW
Ex_P,K = Ex_2 - Ex_1 = 268.63 - 0 = 268.63 kW
I_K = Ex_F,K - Ex_P,K = 296.42 - 268.63 = 27.79 kW
epsilon_K = 268.63 / 296.42 = 0.9063 (yuzde 90.6)
```

**Turbin (T) exergy dengesi:**
```
Ex_F,T = Ex_3 - Ex_4 = 666.48 - 173.93 = 492.55 kW
Ex_P,T = W_T = m_dot * c_p * (T_3 - T_4) = 1.0 * 1.005 * (1200 - 743.3) = 459.03 kW
I_T = Ex_F,T - Ex_P,T = 492.55 - 459.03 = 33.52 kW
epsilon_T = 459.03 / 492.55 = 0.9320 (yuzde 93.2)
```

**Toplam exergy yikimi:**
```
I_total = I_K + I_T = 27.79 + 33.52 = 61.31 kW
y_K = 27.79 / 61.31 = 0.4533 (yuzde 45.3)
y_T = 33.52 / 61.31 = 0.5467 (yuzde 54.7)
```

### ADIM 3-4: Kacinilmaz Kosullar ve Simulasyon

**Kacinilmaz parametreler:**
```
Kompressor: eta_is,K_UN = 0.94
Turbin:     eta_is,T_UN = 0.96
```

**Kacinilmaz cevrim hesabi (tum bilesenler kacinilmaz kosullarda):**
```
T_2,UN = 298.15 + (540.0 - 298.15) / 0.94 = 298.15 + 257.29 = 555.44 K
T_4,UN = 1200 - 0.96 * (1200 - 662.7) = 1200 - 515.8 = 684.2 K
```

Exergy hesaplari (kacinilmaz cevrim):
```
ex_2,UN = 1.005*(555.44-298.15) - 298.15*1.005*ln(555.44/298.15) + 177.93
        = 258.57 - 298.15*1.005*0.6212 + 177.93
        = 258.57 - 186.09 + 177.93
        = 250.41 kJ/kg

ex_4,UN = 1.005*(684.2-298.15) - 298.15*1.005*ln(684.2/298.15)
        = 387.98 - 298.15*1.005*0.8300
        = 387.98 - 248.65
        = 139.33 kJ/kg
```

**Kacinilmaz exergy yikimlari:**
```
W_K,UN = 1.005 * (555.44 - 298.15) = 258.57 kW
I_UN,K = W_K,UN - (Ex_2,UN - Ex_1) = 258.57 - 250.41 = 8.16 kW

Ex_F,T_UN = ex_3_UN - ex_4,UN
```

Turbin girisi ayni sicaklikta (T_3 = 1200 K) ancak kompressor cikis sicakligi degisti. Sadelelik icin yanici etkisini sabit T_3 varsayiyoruz:

```
ex_3,UN = 1.005*(1200-298.15) - 298.15*1.005*ln(1200/298.15) + 177.93
        = 666.48 kJ/kg  (degismedi, T_3 ve P_3 ayni)

I_UN,T = (ex_3,UN - ex_4,UN) - c_p*(T_3 - T_4,UN)
       = (666.48 - 139.33) - 1.005*(1200 - 684.2)
       = 527.15 - 518.38
       = 8.77 kW
```

### ADIM 5: Kacinilabilir Exergy Yikimi

```
I_AV,K = I_K - I_UN,K = 27.79 - 8.16 = 19.63 kW
I_AV,T = I_T - I_UN,T = 33.52 - 8.77 = 24.75 kW
```

| Bilesen | I_k (kW) | I_UN,k (kW) | I_AV,k (kW) | I_AV / I_k |
|---------|----------|-------------|-------------|-------------|
| Kompressor | 27.79 | 8.16 | 19.63 | %70.6 |
| Turbin | 33.52 | 8.77 | 24.75 | %73.8 |

> **Yorum:** Her iki bilesende de kacinilabilir yikim orani yuksek (%70+ uzerinde). Bu, mevcut ekipmanlarin verimsiz calistigini ve iyilestirme potansiyelinin yuksek oldugunu gosterir.

### ADIM 6-7: Endojen ve Ekzojen Ayristirma

**Hibrit Cevrim 1 (Kompressor gercek, Turbin ideal):**
```
Kompressor: eta_is,K = 0.82 (gercek)
Turbin:     eta_is,T = 1.00 (ideal)

T_2,H1 = 593.1 K (gercek kompressor)
T_4,H1 = T_3 * (P_4/P_3)^((k-1)/k) = 662.7 K (ideal turbin)

I_EN,K = W_K - (Ex_2 - Ex_1)  (turbin ideal olsa bile kompressor exergy yikimi)
```

Turbin ideal oldugunda kompressor girdisi/ciktisi degismez (turbin kompressor cikisini etkilemez bu basit cevrinde):
```
I_EN,K = 27.79 kW  (bu basit ornekte kompressor bagimsiz calisiyor)
I_EX,K = I_K - I_EN,K = 27.79 - 27.79 = 0 kW
```

**Hibrit Cevrim 2 (Turbin gercek, Kompressor ideal):**
```
Kompressor: eta_is,K = 1.00 (ideal)
Turbin:     eta_is,T = 0.85 (gercek)

T_2,H2 = 540.0 K (ideal kompressor)
T_4,H2 = 743.3 K (gercek turbin)
```

Bu ornekte kompressor ve turbin arasinda dogrudan termodinamik etkilesim sinirli (yanici sicakligini sabit tutuyoruz):
```
I_EN,T = 33.52 kW  (basit seri cevrinde turbin de bagimsiz)
I_EX,T = I_T - I_EN,T = 33.52 - 33.52 = 0 kW
```

> **Not:** Bu basit 2-bilesenli ornekte kompressor ve turbin birbirini dogrudan etkilemiyor (T_3 sabit). Gercek uygulamalarda (rejeneratif cevrimler, isi geri kazanimi olan sistemler) ekzojen pay onemli olabilir. Kompressor cikis sicakliginin rejenerator uzerinden turbin cikisini etkiledigi sistemlerde I_EX degerleri sifirdan buyuk olur.

### ADIM 8: 4-Yollu Birlestirme

Bu basit ornekte I_EX = 0 oldugu icin:

```
Kompressor:
  I_EN_AV,K = I_AV,K = 19.63 kW
  I_EN_UN,K = I_UN,K = 8.16 kW
  I_EX_AV,K = 0 kW
  I_EX_UN,K = 0 kW

  Dogrulama: 19.63 + 8.16 + 0 + 0 = 27.79 kW = I_K  [DOGRU]

Turbin:
  I_EN_AV,T = I_AV,T = 24.75 kW
  I_EN_UN,T = I_UN,T = 8.77 kW
  I_EX_AV,T = 0 kW
  I_EX_UN,T = 0 kW

  Dogrulama: 24.75 + 8.77 + 0 + 0 = 33.52 kW = I_T  [DOGRU]
```

### Sonuc Ozet Tablosu

| Kategori | Kompressor (kW) | Turbin (kW) | Toplam (kW) |
|----------|-----------------|-------------|-------------|
| I_EN_AV (iyilestirilebilir) | 19.63 | 24.75 | 44.38 |
| I_EN_UN (bilesen siniri) | 8.16 | 8.77 | 16.93 |
| I_EX_AV (sistem iyilestirme) | 0.00 | 0.00 | 0.00 |
| I_EX_UN (sistem siniri) | 0.00 | 0.00 | 0.00 |
| **Toplam I_k** | **27.79** | **33.52** | **61.31** |

**Yorum:** Bu basit cevrinde tum yikim endojen-kacinilabilir kategorisinde yogunlasiyor. Bu, her iki bilesenin de bagimsiz olarak iyilestirilebilecegini gosterir. Turbin (24.75 kW) kompresorden (19.63 kW) daha yuksek iyilestirme potansiyeline sahiptir.

---

## Hassasiyet Analizi Rehberi

### 8+1: Parametre Hassasiyeti

Gelismis exergy analizinin en onemli belirsizlik kaynagi, kacinilmaz parametre secimdir. Bu nedenle hassasiyet analizi (sensitivity analysis) zorunludur.

### Tornado Diyagram Yaklasimi

Her kacinilmaz parametre +-yuzde 10 degistirilir ve sonuc uzerindeki etki olculur:

```
Ornek: Kompressor eta_is,UN = 0.94

Alt sinir: eta_is,UN = 0.94 * 0.90 = 0.846
Ust sinir: eta_is,UN = 0.94 * 1.10 = 1.00 (fiziksel sinir: max 1.0)

Her iki deger icin I_UN,K ve I_AV,K yeniden hesaplanir.
```

**Tornado diyagram hesaplama tablosu:**

| Parametre | Baz Deger | -%10 | +%10 | I_AV,K Degisimi (kW) | Hassasiyet |
|-----------|-----------|------|------|----------------------|------------|
| eta_is,K_UN | 0.94 | 0.846 | 1.00 | +5.2 / -3.8 | Yuksek |
| eta_is,T_UN | 0.96 | 0.864 | 1.00 | +4.1 / -2.9 | Yuksek |

### En Hassas Parametrelerin Belirlenmesi

1. Tum kacinilmaz parametreler icin tornado analizi yap
2. I_AV degisimini buyukten kucuge sirala
3. En hassas 3-5 parametre uzerinde odaklan
4. Bu parametreler icin literatur taramasi derinlestir

### Guven Araligi Tahmini

```
I_AV,k_alt = I_AV,k(en kotu kacinilmaz varsayimlar)
I_AV,k_ust = I_AV,k(en iyi kacinilmaz varsayimlar)

Guven araligi: [I_AV,k_alt, I_AV,k_ust]
```

Eger guven araligi cok genisse (ornegin I_AV,k_ust / I_AV,k_alt > 2), kacinilmaz parametre secimi icin daha fazla literatur destegi gerekir.

### Raporlama Onerileri

- Sonuclari her zaman guven araligiyla birlikte raporlayin
- En hassas parametreleri belirtin
- Farkli kacinilmaz senaryo sonuclarini karsilastirmali tablo olarak sunun
- Hassasiyet analizi yapilmadan sonuclara guvenilmemesini vurgulayin

---

## İlgili Dosyalar

- `knowledge/factory/advanced_exergy/ideal_conditions.md` - Ideal ve kacinilmaz kosul parametre tablolari
- `knowledge/factory/advanced_exergy/interpretation.md` - Gelismis analiz sonuc yorumlama rehberi
- `knowledge/factory/advanced_exergy/equipment_specific/` - Ekipman bazli gelismis analiz detaylari
- `knowledge/factory/exergy_fundamentals.md` - Temel exergy kavramlari
- `knowledge/factory/exergy_flow_analysis.md` - Exergy akis analizi
- `knowledge/factory/cross_equipment.md` - Ekipmanlar arasi etkilesim analizi
- `knowledge/factory/methodology.md` - Konvansiyonel metodoloji
- `knowledge/factory/prioritization.md` - Iyilestirme onceliklendirmesi
- `skills/core/exergy_fundamentals.md` - AI exergy temel becerileri
- `skills/factory/factory_analyst.md` - AI fabrika analisti beceri dosyasi

---

## Referanslar

1. **Tsatsaronis, G., & Park, M.-H.** (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. - Kacinilabilir/kacinilmaz ayristirmanin temel makalesi.

2. **Morosuk, T., & Tsatsaronis, G.** (2009). "Advanced exergetic evaluation of refrigeration machines using different working fluids." *Energy*, 34(12), 2248-2258. - Endojen/ekzojen ayristirma metodolojisi ve sogutma sistemlerine uygulamasi.

3. **Kelly, S., Tsatsaronis, G., & Morosuk, T.** (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. - Hibrit cevrim yontemi ve 4-yollu ayristirma formalizasyonu.

4. **Petrakopoulou, F., Tsatsaronis, G., Morosuk, T., & Carassai, A.** (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. - Kombine cevrim guc santraline gelismis exergy analizi uygulamasi.

5. **Bejan, A., Tsatsaronis, G., & Moran, M.J.** (1996). *Thermal Design and Optimization*. John Wiley & Sons. - Exergy analizi ve termoekonominin temel referans kitabi.

6. **Morosuk, T., & Tsatsaronis, G.** (2013). "Comparative evaluation of LNG-based cogeneration systems using advanced exergetic analysis." *Energy*, 36(6), 3771-3778. - Kojenerasyon sistemlerinde gelismis analiz uygulamasi.
