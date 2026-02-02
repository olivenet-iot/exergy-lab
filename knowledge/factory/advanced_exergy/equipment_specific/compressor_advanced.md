---
title: "Kompresör İleri Exergy Analizi (Advanced Exergy Analysis for Compressors)"
category: "factory/advanced_exergy/equipment_specific"
keywords:
  - ileri exergy analizi (advanced exergy analysis)
  - kaçınılabilir exergy yıkımı (avoidable exergy destruction)
  - endojen exergy (endogenous exergy)
  - ekzojen exergy (exogenous exergy)
  - kompresör optimizasyonu (compressor optimization)
  - vidalı kompresör (screw compressor)
  - santrifüj kompresör (centrifugal compressor)
  - tersinmezlik dekompozisyonu (irreversibility decomposition)
  - dört yollu ayrıştırma (four-way splitting)
  - mexojen analiz (mexogenous analysis)
related_files:
  - knowledge/compressor/formulas.md
  - knowledge/compressor/benchmarks.md
  - knowledge/compressor/solutions/efficiency_improvement.md
  - knowledge/factory/advanced_exergy/methodology.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/heat_integration.md
  - skills/equipment/compressor_expert.md
use_when: "Kompresör exergy analizinde konvansiyonel sonuçların ötesine geçmek, iyileştirme potansiyelini belirlemek ve sistem etkileşimlerini anlamak gerektiğinde kullanılır."
priority: high
last_updated: 2025-05-15
---

# Kompresör İleri Exergy Analizi (Advanced Exergy Analysis for Compressors)

## 1. Giriş ve Motivasyon

Konvansiyonel exergy analizi, bir kompresördeki toplam exergy yıkımını (I_total) ve exergy verimini (epsilon) hesaplar. Ancak bu yaklaşım iki kritik soruyu yanıtsız bırakır:

1. **Bu yıkımın ne kadarı gerçekten önlenebilir?** Termodinamik ve teknolojik limitler nedeniyle bir kısmı kaçınılamazdır.
2. **Yıkımın kaynağı nedir?** Kompresörün kendi iç tersinmezlikleri mi, yoksa sistemdeki diğer ekipmanların etkisi mi?

İleri exergy analizi (advanced exergy analysis), toplam exergy yıkımını sistematik olarak bileşenlerine ayırarak mühendislere hedefli iyileştirme stratejileri sunar. Bu dosya, kompresörlere özgü ileri exergy analiz metodolojisini, sayısal örneklerle ve karar tablolarıyla açıklamaktadır.

## 2. Temel Kavramlar

### 2.1. Kaçınılabilir / Kaçınılamaz Ayrıştırma (Avoidable / Unavoidable Splitting)

Toplam exergy yıkımı iki bileşene ayrılır:

```
I_total = I_AV + I_UN
```

- **I_UN (Unavoidable):** Mevcut en iyi teknoloji ve termodinamik limitler altında bile kaçınılamayan yıkım.
- **I_AV (Avoidable):** Gerçekçi iyileştirmelerle azaltılabilecek yıkım.

Kaçınılamazlık oranı (theta):

```
theta = I_AV / I_total
```

Theta değeri 0 ile 1 arasında olup, 1'e yakın değerler büyük iyileştirme potansiyeli anlamına gelir. Kompresörler için tipik theta aralığı 0.25-0.45'tir.

### 2.2. Endojen / Ekzojen Ayrıştırma (Endogenous / Exogenous Splitting)

Toplam exergy yıkımı kaynak bazında da ayrılır:

```
I_total = I_EN + I_EX
```

- **I_EN (Endogenous):** Kompresörün kendi iç tersinmezliklerinden (sürtünme, sızıntı, ısı transferi) kaynaklanan yıkım.
- **I_EX (Exogenous):** Sistemdeki diğer ekipmanların (aftercooler, soğutma kulesi, pompa, kazan) kompresör performansına etkisinden kaynaklanan yıkım.

Endojen bileşeni hesaplamak için, diğer tüm ekipmanlar ideal (tersinir) kabul edilerek kompresör tek başına analiz edilir.

### 2.3. Dört Yollu Dekompozisyon (Four-Way Splitting)

Yukarıdaki iki ayrıştırma birleştirilerek dört kadran elde edilir:

```
I_total = I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN
```

| Kadran | Tanım | Mühendislik Anlamı |
|--------|--------|--------------------|
| I_EN_AV | Endojen-Kaçınılabilir | Kompresörde doğrudan iyileştirilebilir |
| I_EN_UN | Endojen-Kaçınılamaz | Kompresörün termodinamik limiti |
| I_EX_AV | Ekzojen-Kaçınılabilir | Sistem etkileşimi iyileştirilebilir |
| I_EX_UN | Ekzojen-Kaçınılamaz | Sistem yapısının termodinamik limiti |

Bu dört kadran, mühendislere hangi iyileştirmelerin en yüksek getiriyi sağlayacağını gösterir.

## 3. Kompresör Tipleri ve Kaçınılamaz Koşullar

### 3.1. Karşılaştırma Tablosu

Farklı kompresör tipleri için tipik gerçek ve kaçınılamaz koşullar:

| Parametre | Vidalı (Screw) | Santrifüj (Centrifugal) | Pistonlu (Reciprocating) | Scroll |
|-----------|----------------|-------------------------|--------------------------|--------|
| eta_is_real | 0.70 - 0.78 | 0.78 - 0.85 | 0.65 - 0.75 | 0.60 - 0.70 |
| eta_is_UN | 0.92 | 0.95 | 0.90 | 0.85 |
| Tipik theta | 0.30 - 0.40 | 0.25 - 0.35 | 0.35 - 0.45 | 0.35 - 0.45 |
| Baslica I_EN_AV Kaynagi | Ic sizdirma, surtunme | Surge/choke kayiplari | Supurme hacmi, sizinti | Sabit hacim orani uyumsuzlugu |
| Aftercooler DT_UN (C) | 5 | 3 | 5 | 8 |
| Aftercooler DP_UN (bar) | 0.05 | 0.03 | 0.05 | 0.08 |
| Tipik kapasite (kW) | 15 - 500 | 200 - 10000 | 5 - 300 | 2 - 50 |

### 3.2. Kaçınılamaz Koşulların Belirlenmesi

Kaçınılamaz koşullar belirlenirken şu kriterler uygulanır:

1. **Izentropik verim (eta_is_UN):** Mevcut en iyi ticari teknolojinin ulaşabildiği maksimum verim.
2. **Aftercooler yaklaşma sıcaklığı (DT_approach_UN):** Karşı akış plakalı eşanjör ile ulaşılabilir minimum sıcaklık farkı.
3. **Aftercooler basınç düşüşü (DP_UN):** Optimize edilmiş eşanjör tasarımı ile minimum basınç kaybı.
4. **Mekanik kayıplar:** Manyetik yatak teknolojisi ile minimize edilmiş sürtünme.

```
# Kacinılamaz kosullar ornegi (vidali kompresor)
eta_is_UN = 0.92          # En iyi ticari vidali kompresor verimi
DT_approach_UN = 5.0      # [C] Plakali esanjor minimum yaklasma
DP_aftercooler_UN = 0.05  # [bar] Optimize esanjor basinc kaybi
eta_mech_UN = 0.98        # Mekanik verim limiti
```

## 4. Tam Sayisal Ornek: 75 kW Vidali Kompresor

### 4.1. Sistem Tanimi

Bir fabrikada vidali kompresor, kazan, pompa ve soğutma kulesi birlikte calisiyor. Kompresör hava sıkıştırma işlemi yapmakta ve aftercooler ile çıkış havası soğutulmaktadır.

**Gercek kosullar:**

```
P_in = 75 kW              # Kompresore verilen guc
P_ratio = 7                # Basinc orani (1 bar -> 7 bar)
T_in = 25 + 273.15         # [K] Giris sicakligi = 298.15 K
T_out = 185 + 273.15       # [K] Cikis sicakligi = 458.15 K
eta_is = 0.72              # Izentropik verim (gercek)
DT_approach = 15           # [C] Aftercooler yaklasma sicakligi
DP_aftercooler = 0.3       # [bar] Aftercooler basinc dusumu
```

**Aftercooler:**

```
T_cooling_in = 30 + 273.15  # [K] Sogutma suyu giris = 303.15 K
T_cooling_out = 45 + 273.15 # [K] Sogutma suyu cikis = 318.15 K
T_air_out = 45 + 273.15     # [K] Sikistirilmis hava cikis = 318.15 K
```

### 4.2. Adim 1 — Konvansiyonel Exergy Analizi

Ilk olarak standart exergy analizi yapilir:

```
# Ideal (izentropik) cikis sicakligi
T_out_is = T_in * (P_ratio)^((k-1)/k)
# k = 1.4 (hava icin)
T_out_is = 298.15 * (7)^(0.4/1.4)
T_out_is = 298.15 * 7^0.2857
T_out_is = 298.15 * 1.7458
T_out_is = 520.6 K  (ideal)

# Gercek cikis sicakligi dogrulamasi
T_out_real = T_in + (T_out_is - T_in) / eta_is
T_out_real = 298.15 + (520.6 - 298.15) / 0.72
T_out_real = 298.15 + 308.96
T_out_real = 607.1 K  (bu sogutmasiz deger)
# NOT: T_out = 185°C aftercooler sonrasi degerdir

# Toplam exergy yikimi (verilen)
I_total = 22.5 kW

# Exergy verimi
epsilon = 1 - (I_total / P_in)
epsilon = 1 - (22.5 / 75)
epsilon = 0.70 = %70
```

Konvansiyonel analiz sonucu: Kompresörde 22.5 kW exergy yıkımı var, exergy verimi %70. Ancak bu bilgi tek başına iyileştirme stratejisi için yetersizdir.

### 4.3. Adim 2 — Kacinilabilir / Kacinılamaz Ayristirma

Kaçınılamaz koşullar altında kompresör yeniden analiz edilir:

```
# Kacinılamaz kosullar
eta_is_UN = 0.93
DT_approach_UN = 5         # [C]
DP_aftercooler_UN = 0.05   # [bar]

# Kacinılamaz izentropik sikistirma isi
W_is = m_dot * cp * T_in * ((P_ratio)^((k-1)/k) - 1)

# Kacinılamaz gercek guc (ideal kosullarda)
P_in_UN = W_is / eta_is_UN

# Kacinılamaz exergy yikimi
I_UN = 14.2 kW

# Kacinilabilir exergy yikimi
I_AV = I_total - I_UN
I_AV = 22.5 - 14.2
I_AV = 8.3 kW

# Kacinılabilirlik orani
theta = I_AV / I_total
theta = 8.3 / 22.5
theta = 0.369 ≈ 0.37
```

**Yorum:** Theta = 0.37, toplam yıkımın %37'sinin gerçekçi iyileştirmelerle azaltılabileceğini gösterir. Bu değer vidalı kompresörler için tipik aralıktadır (0.30-0.40).

### 4.4. Adim 3 — Endojen / Ekzojen Ayristirma

Sistemdeki diğer ekipmanlar (kazan, pompa, soğutma kulesi) ideal kabul edilerek kompresör tek başına analiz edilir:

```
# Diger ekipmanlar ideal (tersinir) kabul edildiginde:
# - Sogutma suyu sicakligi T_cooling_in = T_amb = 25°C (pompa ideal)
# - Aftercooler DT = 0 (esanjor ideal)
# - Sogutma kulesi verimi = 1.0

# Endojen exergy yikimi (sadece kompresorun kendi tersinmezligi)
I_EN = 18.5 kW

# Ekzojen exergy yikimi (diger ekipmanlarin etkisi)
I_EX = I_total - I_EN
I_EX = 22.5 - 18.5
I_EX = 4.0 kW
```

**Ekzojen bileşen kaynakları:**

- Pompa performansının soğutma suyu debisine etkisi: ~1.5 kW
- Soğutma kulesinin aftercooler soğutma suyu sıcaklığına etkisi: ~1.8 kW
- Kazan buhar kalitesinin genel sistem dengesine etkisi: ~0.7 kW

```
I_EX = I_EX_pompa + I_EX_sogutma_kulesi + I_EX_kazan
I_EX = 1.5 + 1.8 + 0.7
I_EX = 4.0 kW
```

### 4.5. Adim 4 — Dort Yollu Dekompozisyon

Kaçınılabilir/kaçınılamaz ve endojen/ekzojen ayrıştırmaları birleştirilir:

```
# Endojen-Kacinılabilir
I_EN_AV = I_EN * (I_AV / I_total) * correction_EN
I_EN_AV = 6.5 kW

# Endojen-Kacinılamaz
I_EN_UN = I_EN - I_EN_AV
I_EN_UN = 18.5 - 6.5
I_EN_UN = 12.0 kW

# Ekzojen-Kacinılabilir
I_EX_AV = I_EX * (I_AV / I_total) * correction_EX
I_EX_AV = 1.8 kW

# Ekzojen-Kacinılamaz
I_EX_UN = I_EX - I_EX_AV
I_EX_UN = 4.0 - 1.8
I_EX_UN = 2.2 kW
```

**Dogrulama:**

```
I_total = I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN
I_total = 6.5 + 12.0 + 1.8 + 2.2
I_total = 22.5 kW  ✓
```

### 4.6. Sonuc Tablosu

| Kategori | Deger (kW) | Yuzde (%) | Aksiyon |
|----------|------------|-----------|---------|
| I_EN_AV | 6.5 | 28.9 | VSD retrofit, kademeli sikistirma, ic sizdimazlik iyilestirmesi |
| I_EN_UN | 12.0 | 53.3 | Termodinamik limit — iyilestirme mumkun degil |
| I_EX_AV | 1.8 | 8.0 | Sogutma sistemi iyilestir, pompa debisini optimize et |
| I_EX_UN | 2.2 | 9.8 | Sistem tasarimi limiti — yeniden tasarim gerekir |

**Ana bulgu:** Toplam iyileştirme potansiyeli I_EN_AV + I_EX_AV = 6.5 + 1.8 = 8.3 kW (%36.9). Bunun %78.3'u (6.5 kW) kompresör üzerinde doğrudan müdahale ile, %21.7'si (1.8 kW) sistem etkileşimlerinin iyileştirilmesiyle sağlanabilir.

## 5. Diğer Ekipmanlarla Etkileşim Analizi (Ekzojen Bileşen Detayı)

### 5.1. Kazan - Kompresör Etkileşimi

Kazan buhar kalitesi, fabrika genelindeki enerji dengesini etkiler. Kazanın düşük verimle çalışması, kompresörün aftercooler'ındaki soğutma suyu sıcaklığını dolaylı olarak artırabilir (ortak soğutma suyu hattı kullanılması durumunda).

```
# Kazan etkisi (mexojen bilesen)
I_MX_kazan_kompresor = 0.7 kW

# Hesaplama yontemi:
# 1. Kazan ideal, diger ekipmanlar gercek -> I_total_kazan_ideal hesapla
# 2. Tum ekipmanlar gercek -> I_total_gercek hesapla
# 3. I_MX = I_total_gercek - I_total_kazan_ideal - I_EN
```

### 5.2. Pompa - Kompresör Etkileşimi

Soğutma suyu pompasının performansı, aftercooler'a gelen soğutma suyu debisini ve sıcaklığını doğrudan etkiler.

```
# Pompa performansi etkisi
# Gercek pompa verimi: eta_pump = 0.65
# Ideal pompa verimi: eta_pump_ideal = 1.0

# Dusuk pompa verimi -> dusuk debi -> yuksek DT_approach
# Bu da kompresordeki exergy yikimini artirir

I_MX_pompa_kompresor = 1.5 kW

# Etki mekanizmasi:
# DT_approach_gercek = 15°C  (pompa gercek)
# DT_approach_pompa_ideal = 10°C  (pompa ideal, daha fazla debi)
# Fark: 5°C ek yaklasma -> 1.5 kW ek exergy yikimi
```

### 5.3. Soğutma Kulesi - Kompresör Etkileşimi

Soğutma kulesinin performansı, soğutma suyu giriş sıcaklığını belirler ve aftercooler üzerinden kompresör exergy yıkımını etkiler.

```
# Sogutma kulesi etkisi
# Gercek sogutma kulesi etkinligi: eta_ct = 0.70
# Ideal sogutma kulesi etkinligi: eta_ct_ideal = 1.0

# Dusuk sogutma kulesi verimi -> yuksek sogutma suyu sicakligi
# T_cooling_in_gercek = 30°C
# T_cooling_in_ideal = 25°C (yaslak termometre sicakligina yakin)

I_MX_sogutma_kulesi_kompresor = 1.8 kW

# Toplam ekzojen dogrulama
I_EX = I_MX_kazan + I_MX_pompa + I_MX_sogutma_kulesi
I_EX = 0.7 + 1.5 + 1.8
I_EX = 4.0 kW  ✓
```

### 5.4. Mexojen Etkileşim Özet Tablosu

| Kaynak Ekipman | Etki Mekanizmasi | I_MX (kW) | Yuzde (%) |
|----------------|------------------|-----------|-----------|
| Kazan | Ortak sogutma suyu hatti ile dolayli etki | 0.7 | 17.5 |
| Pompa | Sogutma suyu debisi ve basinci | 1.5 | 37.5 |
| Sogutma Kulesi | Sogutma suyu giris sicakligi | 1.8 | 45.0 |
| **Toplam I_EX** | — | **4.0** | **100.0** |

## 6. Duyarlılık Analizi (Sensitivity Analysis)

### 6.1. Izentropik Verimin Etkisi

Kompresörün izentropik verimi değiştikçe dört yollu dekompozisyon nasıl değişir:

| eta_is | I_total (kW) | I_EN_AV (kW) | I_EN_UN (kW) | I_EX_AV (kW) | I_EX_UN (kW) | theta |
|--------|-------------|-------------|-------------|-------------|-------------|-------|
| 0.60 | 30.0 | 12.8 | 11.5 | 3.2 | 2.5 | 0.53 |
| 0.65 | 26.5 | 9.8 | 11.8 | 2.6 | 2.3 | 0.47 |
| 0.70 | 23.5 | 7.2 | 11.9 | 2.1 | 2.3 | 0.40 |
| 0.72 | 22.5 | 6.5 | 12.0 | 1.8 | 2.2 | 0.37 |
| 0.75 | 21.0 | 5.3 | 12.0 | 1.5 | 2.2 | 0.32 |
| 0.80 | 18.8 | 3.2 | 12.1 | 1.3 | 2.2 | 0.24 |
| 0.85 | 16.5 | 1.0 | 12.2 | 1.1 | 2.2 | 0.13 |

**Gozlem:** Izentropik verim arttikca I_EN_AV hizla duser, ancak I_EN_UN yaklasik sabit kalir. Theta degeri duser, yani iyilestirme potansiyeli azalir. eta_is > 0.85 durumunda theta < 0.15 olur ve ek yatirim genellikle ekonomik degildir.

### 6.2. Aftercooler Yaklaşma Sıcaklığının Etkisi

| DT_approach (C) | I_aftercooler (kW) | I_AV_aftercooler (kW) | Ek maliyet (%) |
|-----------------|--------------------|-----------------------|----------------|
| 3 | 1.2 | 0 (limit) | +80 |
| 5 | 1.8 | 0.2 | +40 |
| 10 | 3.5 | 1.5 | +10 |
| 15 | 5.2 | 3.2 | Referans |
| 20 | 7.0 | 5.0 | -5 |
| 30 | 10.5 | 8.5 | -15 |

**Gozlem:** Yaklasma sicakligi 15°C'den 5°C'ye dusurulmesi, 3.0 kW exergy tasarrufu saglar ancak esanjor maliyetini %40 artirir. Ekonomik optimum genellikle 8-12°C arasindadir.

### 6.3. Basınç Oranının Etkisi

| P_ratio | I_total (kW) | I_EN_AV (kW) | theta | Onerilecek kademe sayisi |
|---------|-------------|-------------|-------|--------------------------|
| 4 | 14.2 | 3.8 | 0.32 | 1 |
| 6 | 19.8 | 5.6 | 0.35 | 1 |
| 7 | 22.5 | 6.5 | 0.37 | 1-2 |
| 8 | 25.3 | 7.5 | 0.39 | 2 |
| 10 | 31.0 | 10.2 | 0.42 | 2 |
| 14 | 42.5 | 16.0 | 0.48 | 2-3 |
| 20 | 58.0 | 24.5 | 0.53 | 3 |

**Gozlem:** Basinc orani arttikca theta degeri de artar, cunku tek kademeli sikistirmadaki tersinmezlikler hizla buyur. P_ratio > 8 durumunda kademeli sikistirma (intercooling ile) ciddi I_EN_AV azaltmasi saglar.

### 6.4. Sogutma Suyu Giris Sicakliginin Etkisi

| T_cooling_in (C) | I_EX (kW) | I_EX_AV (kW) | I_EX_UN (kW) |
|-------------------|-----------|-------------|-------------|
| 20 | 2.0 | 0.5 | 1.5 |
| 25 | 3.0 | 1.2 | 1.8 |
| 30 | 4.0 | 1.8 | 2.2 |
| 35 | 5.2 | 2.8 | 2.4 |
| 40 | 6.5 | 3.8 | 2.7 |

**Gozlem:** Sogutma suyu sicakligi arttikca I_EX bileşeni hizla buyur. Sicak iklimlerde (T_cooling_in > 35°C) ekzojen bileşen toplam yikimin %25'ini asabilir. Bu durumda sogutma kulesi iyilestirmesi kompresor iyilestirmesinden daha oncelikli olabilir.

## 7. Karar Tablosu — Her Kadran İçin Aksiyon

### 7.1. Genel Karar Matrisi

| Kadran | Durum | Oncelikli Aksiyon | Tipik ROI | Uygulama Kolayligi |
|--------|-------|-------------------|-----------|---------------------|
| I_EN_AV yuksek (>25%) | Kompresor verimsiz | VSD retrofit, yeni kompresor, kademeli sikistirma | 1-3 yil | Orta |
| I_EN_UN yuksek (>50%) | Termodinamik limit | Teknoloji degisikligi yok, kabul et | — | — |
| I_EX_AV yuksek (>10%) | Sistem etkilesimi kotu | Sogutma sistemi iyilestir, pompa optimize et | 1-2 yil | Kolay-Orta |
| I_EX_UN yuksek (>10%) | Sistem yapisi limiti | Sistem yeniden tasarimi, yeni sogutma kulesi | 3-5 yil | Zor |

### 7.2. I_EN_AV Yüksek Olduğunda Detaylı Aksiyonlar

Kompresörün endojen-kaçınılabilir exergy yıkımı yüksekse (%25 üzeri), şu iyileştirmeler değerlendirilmelidir:

1. **VSD (Variable Speed Drive) Retrofit:**
   - Kısmi yüklerde izentropik verimi %5-15 artırır
   - Tipik I_EN_AV azaltma: %30-50
   - Yatırım: 3000-8000 EUR/kW
   - ROI: 1-2 yıl

2. **Kademeli Sıkıştırma (Multi-stage Compression):**
   - P_ratio > 8 durumunda etkili
   - Ara soğutma (intercooling) ile izentropik işe yaklaşma
   - Tipik I_EN_AV azaltma: %40-60
   - Yatırım: Yeni sistem maliyetinin %60-80'i
   - ROI: 2-4 yıl

3. **İç Sızdırmazlık İyileştirmesi:**
   - Vidalı kompresörlerde rotor profili optimizasyonu
   - Tipik I_EN_AV azaltma: %10-20
   - Yatırım: Bakım bütçesi dahilinde
   - ROI: < 1 yıl

4. **Yağ Enjeksiyonu Optimizasyonu (Oil-injected Screw):**
   - Sıkıştırma sırasında soğutma etkisi
   - İzentropik verimi %3-8 artırabilir
   - Tipik I_EN_AV azaltma: %15-25
   - Yatırım: Düşük (operasyonel değişiklik)
   - ROI: < 6 ay

### 7.3. I_EX_AV Yüksek Olduğunda Detaylı Aksiyonlar

Ekzojen-kaçınılabilir bileşen yüksekse (%10 üzeri), sistem etkileşimleri iyileştirilmelidir:

1. **Soğutma Kulesi İyileştirmesi:**
   - Doldurma malzemesi değişimi, fan optimizasyonu
   - T_cooling_in'i 3-5°C düşürür
   - Tipik I_EX_AV azaltma: %40-60
   - ROI: 1-2 yıl

2. **Soğutma Suyu Pompası Optimizasyonu:**
   - Pompa VSD retrofit veya impeller trim
   - Debi artışı ile daha düşük DT_approach
   - Tipik I_EX_AV azaltma: %20-35
   - ROI: 1-1.5 yıl

3. **Aftercooler Yenileme:**
   - Plakalı eşanjöre geçiş
   - DT_approach'u 15°C'den 8°C'ye düşürme
   - Tipik I_EX_AV azaltma: %50-70
   - ROI: 1.5-3 yıl

## 8. Adım Adım Hesaplama Rehberi (Step-by-Step Walkthrough)

Bir kompresör için ileri exergy analizi yapmak isteyen mühendis aşağıdaki adımları izlemelidir:

### Adim 1: Veri Toplama
```
# Gerekli veriler:
# 1. Kompresor: P_in, P_ratio, T_in, T_out, eta_is, tip
# 2. Aftercooler: DT_approach, DP, T_cooling_in, T_cooling_out
# 3. Sistem: Diger ekipman parametreleri (kazan, pompa, sogutma kulesi)
# 4. Ortam: T_0, P_0 (olum durum - dead state)
```

### Adim 2: Konvansiyonel Analiz
```
# a) Exergy giris hesapla
Ex_in = P_in  # (elektrik exergisi = guc)

# b) Exergy cikis hesapla
Ex_out = m_dot * [(h_out - h_0) - T_0 * (s_out - s_0)]

# c) Exergy yikimi
I_total = Ex_in - Ex_out

# d) Exergy verimi
epsilon = Ex_out / Ex_in
```

### Adim 3: Kaçınılamaz Koşulları Belirle
```
# Kompresor tipine gore Tablo 3.1'den sec:
# eta_is_UN, DT_approach_UN, DP_UN

# Kacinılamaz kosullarda yeniden hesapla:
I_UN = f(eta_is_UN, DT_approach_UN, DP_UN)
I_AV = I_total - I_UN
theta = I_AV / I_total
```

### Adim 4: Endojen Bileşeni Hesapla
```
# Diger tum ekipmanlari ideal (tersinir) yap
# Sadece kompresoru gercek kosuluyla calistir
# Yeni sistem dengesini coz

I_EN = I_total_diger_ideal
I_EX = I_total - I_EN
```

### Adim 5: Dört Yollu Dekompozisyon
```
# Kacinılamaz kosullarda endojen analiz yap
I_EN_UN = f(eta_is_UN, diger_ekipman_ideal)
I_EN_AV = I_EN - I_EN_UN
I_EX_UN = I_UN - I_EN_UN
I_EX_AV = I_EX - I_EX_UN

# Dogrulama
assert abs(I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN - I_total) < 0.01
```

### Adim 6: Sonuçları Yorumla
```
# Karar tablosunu uygula (Bolum 7)
# En yuksek I_XX_AV bileseninden basla
# ROI ve uygulama kolayligi degerlendir
# Onceliklendirme yap
```

## 9. Pratik Ipuçları ve Yaygın Hatalar

### 9.1. Sık Yapılan Hatalar

1. **Kaçınılamaz koşulları çok iyimser belirlemek:** eta_is_UN = 1.0 almak fiziksel olarak anlamsızdır. Gerçekçi ticari limitler kullanılmalıdır (Tablo 3.1).

2. **Ekzojen bileşeni ihmal etmek:** Özellikle ortak soğutma suyu hattı olan sistemlerde I_EX, toplam yıkımın %15-25'ini oluşturabilir.

3. **Ölü durum (dead state) tanımını değiştirmek:** T_0 ve P_0 tüm analizde sabit tutulmalıdır. Mevsimsel değişimler ayrı senaryolar olarak analiz edilmelidir.

4. **Aftercooler'ı ayrı bileşen olarak analiz etmemek:** Aftercooler kompresör sisteminin ayrılmaz parçasıdır ve birlikte analiz edilmelidir.

### 9.2. Veri Kalitesi Gereksinimleri

| Parametre | Minimum Dogruluk | Olcum Yontemi |
|-----------|-----------------|---------------|
| P_in | +/- 2% | Guc analizoru |
| T_in, T_out | +/- 0.5°C | Kalibrasyon sertifikali termokupl |
| P_ratio | +/- 1% | Basinc transmiteri |
| m_dot | +/- 3% | Orifis plaka veya ultrasonik |
| T_cooling | +/- 1°C | PT100 sensor |

## 10. İlgili Dosyalar

- `knowledge/compressor/formulas.md` — Kompresör exergy hesaplama formülleri
- `knowledge/compressor/benchmarks.md` — Kompresör verimlilik karşılaştırma tabloları
- `knowledge/compressor/solutions/efficiency_improvement.md` — Verimlilik iyileştirme çözümleri
- `knowledge/factory/advanced_exergy/methodology.md` — İleri exergy analizi genel metodolojisi
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası exergy etkileşimleri
- `knowledge/factory/heat_integration.md` — Isı entegrasyonu ve atık ısı geri kazanımı
- `knowledge/factory/pinch_analysis.md` — Pinch analizi ile sistem optimizasyonu
- `skills/equipment/compressor_expert.md` — Kompresör uzman AI beceri dosyası

## 11. Referanslar

1. **Tsatsaronis, G.** (2009). "Strengths and Limitations of Exergy Analysis." *Thermodynamic Optimization of Complex Energy Systems*, NATO Science Series, Vol. 69, pp. 93-100. Springer. — İleri exergy analizinin temel teorik çerçevesini ve dört yollu dekompozisyon metodolojisini tanımlar.

2. **Morosuk, T. & Tsatsaronis, G.** (2009). "Advanced Exergy Analysis for Chemically Reacting Systems — Application to a Simple Open Gas-Turbine System." *International Journal of Thermodynamics*, 12(3), pp. 105-111. — Endojen/ekzojen ve kaçınılabilir/kaçınılamaz ayrıştırma metodolojisinin detaylı matematiksel formülasyonunu sunar ve endüstriyel sistemlere uygulamasını gösterir.

3. **Bejan, A., Tsatsaronis, G. & Moran, M.** (1996). *Thermal Design and Optimization*. John Wiley & Sons, New York. — Exergy analizi, exergoekonomik ve termoekonomik optimizasyonun temel referans kitabıdır. Kompresör dahil tüm endüstriyel ekipmanlar için exergy hesaplama yöntemlerini kapsar.

4. **Kelly, S., Tsatsaronis, G. & Morosuk, T.** (2009). "Advanced Exergetic Analysis: Approaches for Splitting the Exergy Destruction into Endogenous and Exogenous Parts." *Energy*, 34(3), pp. 384-391. — Ekzojen exergy yıkımının hesaplama yöntemlerini (termodinamik döngü metodu, mühendislik metodu) karşılaştırır ve pratik uygulama rehberi sunar.

5. **Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A.** (2012). "Conventional and Advanced Exergetic Analyses Applied to a Combined Cycle Power Plant." *Energy*, 41(1), pp. 146-152. — Kombine çevrim sistemlerinde ileri exergy analizinin uygulamasını ve ekipmanlar arası etkileşimlerin (mexojen analiz) sayısal sonuçlarını sunar.
