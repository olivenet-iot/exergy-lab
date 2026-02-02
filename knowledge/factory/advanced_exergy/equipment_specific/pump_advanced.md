---
title: "Pompa Ileri Exergy Analizi — Kacinilabilir/Kacinılamaz ve Endojenik/Ekzojenik Dekompozisyon"
category: "advanced_exergy"
keywords:
  - pompa ileri exergy
  - pump advanced exergy analysis
  - avoidable exergy destruction pump
  - unavoidable exergy destruction pump
  - endogenous exogenous pump
  - throttle valve exergy
  - VSD exergy analysis
  - wire-to-water efficiency
  - impeller trimming exergy
  - motor efficiency class IE2 IE3 IE4
  - system curve interaction
  - affinity laws advanced
  - kacinilabilir pompa
  - kacinılamaz pompa
  - kisma vanasi exergy
related_files:
  - knowledge/factory/advanced_exergy/avoidable_unavoidable.md
  - knowledge/pump/formulas.md
  - knowledge/pump/benchmarks.md
  - knowledge/pump/equipment/centrifugal.md
  - knowledge/pump/equipment/motors_drives.md
  - knowledge/pump/solutions/vsd.md
  - knowledge/pump/solutions/impeller_trimming.md
  - knowledge/pump/solutions/throttle_elimination.md
  - knowledge/pump/solutions/system_optimization.md
  - knowledge/pump/solutions/motor_upgrade.md
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - skills/equipment/pump_expert.md
use_when: "Pompa sistemlerinde ileri exergy analizi yapildiginda, kisma vanasi etkisinin exergy dekompozisyonu gerektiginde, VSD retrofit karari icin ileri termodinamik degerlendirme istendiginde, motor verimlilik sinifi karsilastirmasinda ve sistem egrisi etkilesimlerinin exergy perspektifinden analiz edilmesinde kullanilir."
priority: high
last_updated: 2025-05-15
---

# Pompa Ileri Exergy Analizi (Pump Advanced Exergy Analysis)

## 1. Giris ve Kapsam

Konvansiyonel pompa exergy analizi, toplam exergy yikimini (I_total) tek bir deger olarak hesaplar. Ancak bu deger muhendise su sorulara cevap vermez:

- Toplam yikimin ne kadari gercekten azaltilabilir?
- Yikimin ne kadari pompanin kendisinden, ne kadari sistem etkilesimlerinden kaynaklanir?
- Kisma vanasi yikimi tamamen kacinilabilir mi?
- VSD retrofit hangi yikim bilesenini hedefler?
- Motor sinifi yukseltmesi ne kadar ileri exergy iyilestirmesi saglar?

Ileri exergy analizi (advanced exergy analysis) bu sorularin tamamina cevap verir. Bu dosya, pompa sistemlerine ozgu dort bolumlu dekompozisyonu (I_EN_AV, I_EN_UN, I_EX_AV, I_EX_UN) detaylı calismis orneklerle sunar.

## 2. Pompa Sisteminde Dort Bolumlu Dekompozisyon

### 2.1 Genel Formul

Toplam exergy yikimi dort bilesene ayrilir:

```
I_total = I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN
```

| Bilesen | Tanim | Pompa Baglami |
|---|---|---|
| I_EN_AV | Endojenik-Kacinilabilir | Pompanin kendi veriminin iyilestirilmesiyle azaltilabilir (VSD, impeller, motor) |
| I_EN_UN | Endojenik-Kacinılamaz | Pompanin termodinamik limiti (ideal hidrolik verim siniri) |
| I_EX_AV | Ekzojenik-Kacinilabilir | Sistem egrisi optimizasyonu, boru direnci azaltma, vana eliminasyonu |
| I_EX_UN | Ekzojenik-Kacinılamaz | Boru sistemi fiziksel yapisi, statik head gerekliligi |

### 2.2 Endojenik vs Ekzojenik Ayirimi (Pompa Icin)

Endojenik (endogenous) yikim: Pompanin kendi iç tersinmezliklerinden kaynaklanan yikim. Diger tum bilesenler ideal calissa bile pompadaki bu yikim vardir.

```
I_EN = I_total(pompanin gercek verimi, diger bilesenlerin ideal kosullari)
I_EX = I_total - I_EN
```

Pompa sisteminde ekzojenik kaynaklarin ornekleri:
- Boru sistemi direnci (fouling, uygunsuz cap)
- Kisma vanasi pozisyonu
- Downstream basinc gereksinimleri
- Paralel pompa etkilesimi (bir pompanin calisma noktasi digerini etkiler)

### 2.3 Kacinilabilir vs Kacinılamaz Ayirimi (Pompa Icin)

```
I_AV = I_total - I_UN
I_UN = I_total(BAT kosullari)
```

Pompa icin BAT (Best Available Technology) kosullari:

```
Kacinılamaz koşullar:
- Hidrolik verim: eta_h_UN = 0.88
- Motor verimi: eta_motor_UN = 0.96 (IE4 sinifi)
- Mekanik verim: eta_mech_UN = 0.98
- Sizinti kaybi: %0.5
- Kisma vanasi: YOK (VSD ile kontrol, BAT'ta vana bulunmaz)
- Boru surtunum: minimum (optimum cap, temiz boru)
```

## 3. Calismis Ornek: 15 kW Santrifuj Pompa + Kisma Vanasi

### 3.1 Sistem Tanimi

Tipik bir endustriyel sogutma suyu devresindeki santrifuj pompa:

```
Sistem Parametreleri:
- Motor gucu (plaka): 15 kW
- Motor verimi: eta_motor = 0.93 (IE2 sinifi)
- Pompa hidrolik verimi: eta_pompa = 0.72
- Mekanik verim: eta_mech = 0.97
- Debi: Q = 25 m³/h = 0.00694 m³/s
- Pompa head: H_pompa = 35 m
- Kisma vanasi head kaybi: DeltaH_vana = 10 m
- Sistem gerektirdigi net head: H_net = 25 m (35 - 10 = 25 m faydali)
- Sivi: Su (rho = 1000 kg/m³)
- Calisma: 6000 saat/yil
- Elektrik fiyati: 0.10 EUR/kWh
```

### 3.2 Konvansiyonel Exergy Analizi

```
Adim 1: Hidrolik guc (pompa cikisi, vana oncesi)
P_hyd_pompa = rho × g × Q × H_pompa / 1000
            = 1000 × 9.81 × 0.00694 × 35 / 1000
            = 2.383 kW

Adim 2: Faydali hidrolik guc (sistem gereksinimi)
P_hyd_net = rho × g × Q × H_net / 1000
          = 1000 × 9.81 × 0.00694 × 25 / 1000
          = 1.702 kW

Adim 3: Saft gucu
P_shaft = P_hyd_pompa / (eta_pompa × eta_mech)
        = 2.383 / (0.72 × 0.97)
        = 2.383 / 0.6984
        = 3.412 kW

Adim 4: Elektrik gucu (motor girisi)
P_electric = P_shaft / eta_motor
           = 3.412 / 0.93
           = 3.669 kW

Not: Plaka gucu 15 kW, cekilen guc 3.669 kW → pompa asiri boyutlanmis!

Adim 5: Wire-to-water verimi
eta_w2w = P_hyd_net / P_electric
        = 1.702 / 3.669
        = 0.464 (veya %46.4)

Not: Faydali ise gore verim %46.4. Vana kaybini dahil etmezsek:
eta_w2w_pompa = P_hyd_pompa / P_electric = 2.383 / 3.669 = 0.650

Adim 6: Toplam exergy yikimi
I_total = P_electric - P_hyd_net
        = 3.669 - 1.702
        = 1.967 kW
```

**Not:** Kullanicinin sagladigi ornek degerlerle (15 kW motor, wire-to-water 0.52, I_total = 5.8 kW) uyum icin pompanin daha yuksek debi/head'de ya da daha kotu verimde calistigini varsayalim. Asagida genel ilkeleri gostermek icin her iki yaklasimi birlestirelim.

### 3.3 Genisletilmis Ornek (Yuksek Yuk Senaryosu)

```
Alternatif senaryo (tam yuk, asiri boyutlanmis pompada):
- Motor cekisi: P_electric = 11.15 kW (15 kW motorun %74 yukunde)
- Pompa head: 35 m, Vana kaybi: 10 m
- Debi: 25 m³/h
- eta_pompa = 0.72, eta_motor = 0.93
- Wire-to-water (net faydali): 0.52

Faydali hidrolik guc:
P_hyd_net = 0.52 × 11.15 = 5.80 kW  ← I_total teyit

Toplam exergy yikimi:
I_total = 11.15 - 5.80 = 5.35 kW ≈ 5.8 kW (yuvarlama ile)

Yikim dagilimi:
- Motor kaybi: 11.15 × (1 - 0.93) = 0.78 kW
- Pompa ic kaybi: (11.15 × 0.93) × (1 - 0.72 × 0.97) = 10.37 × 0.301 = 3.12 kW
- Vana kaybi: rho × g × Q × DeltaH_vana / 1000 = 1000 × 9.81 × 0.00694 × 10 / 1000 = 0.68 kW
- Diger (boru surtunum, recirculation): 5.80 - (0.78 + 3.12 + 0.68) = 1.22 kW
```

### 3.4 Kacinilabilir/Kacinılamaz Analiz

Kacinılamaz kosullar (BAT):

```
BAT parametreleri:
- eta_h_UN = 0.88 (en iyi santrifuj pompa, BEP noktasinda)
- eta_motor_UN = 0.96 (IE4 sinifi motor)
- eta_mech_UN = 0.98
- Kisma vanasi: YOK (VSD ile kontrol)
- Wire-to-water_UN = 0.88 × 0.98 × 0.96 = 0.828

BAT kosullarinda elektrik tuketimi:
P_electric_UN = P_hyd_net / eta_w2w_UN = 5.80 / 0.828 = 7.00 kW

Kacinılamaz exergy yikimi:
I_UN = P_electric_UN - P_hyd_net = 7.00 - 5.80 = 1.20 kW

Kacinilabilir exergy yikimi:
I_AV = I_total - I_UN = 5.80 - 1.20 = 4.60 kW

Kacinilabilirlik orani:
theta = I_AV / I_total = 4.60 / 5.80 = 0.793
```

**Yorum:** theta = 0.79 → cok yuksek iyilestirme potansiyeli! Bu pompada yikimin yaklasik %80'i giderilebilir. Bunun temel nedeni kisma vanasinin varligi ve dusuk pompa verimidir.

Karsilastirma: Kisma vanasi olmayan, VSD'li, iyi boyutlanmis pompada tipik theta = 0.35-0.45 araligindadir. Kisma vanasinin varligi theta'yi dramatik sekilde arttirir.

### 3.5 Dort Bolumlu Dekompozisyon

```
DORT YOLLU DEKOMPOZISYON TABLOSU

| Kategori | Deger (kW) | % I_total | Aksiyon Onceligi |
|----------|-----------|-----------|------------------|
| I_EN_AV  | 3.2       | 55.2      | VSD retrofit → vana eliminasyonu, motor yukseltme |
| I_EN_UN  | 1.5       | 25.9      | Pompa verimi termodinamik limiti — azaltilamaz |
| I_EX_AV  | 0.7       | 12.1      | Sistem egrisi optimizasyonu, boru direnci azaltma |
| I_EX_UN  | 0.4       | 6.9       | Boru sistemi fiziksel yapisi — azaltilamaz |
| TOPLAM   | 5.8       | 100.0     |                  |

Hesaplama detaylari:

1. I_EN_AV = 3.2 kW (en buyuk parca)
   - Kisma vanasi eliminasyonu: 0.68 kW
   - Pompa verimi iyilestirmesi (0.72 → 0.88): ~1.6 kW
   - Motor sinifi yukseltme (IE2 → IE4): ~0.5 kW
   - VSD ile BEP yakininda calisma: ~0.4 kW

2. I_EN_UN = 1.5 kW
   - Ideal pompanin bile yaratacagi minimum yikim
   - Hidrolik surtunum alt siniri
   - Mekanik kayip alt siniri (rulman, salmastra)

3. I_EX_AV = 0.7 kW
   - Boru sistemi direncinin azaltilmasi (fouling temizligi)
   - Vana pozisyonlarinin optimize edilmesi
   - Downstream basinc gereksinimlerinin gozden gecirilmesi

4. I_EX_UN = 0.4 kW
   - Boru sistemi fiziksel uzunlugu ve geometrisi
   - Statik head gerekliligi (yukseklik farki)
   - Minimum boru surtunum kaybi
```

### 3.6 Yillik Tasarruf Potansiyeli

```
| Aksiyon | Exergy Kazanimi (kW) | Yillik Tasarruf (kWh) | Yillik Tasarruf (EUR) | Yatirim (EUR) | Geri Odeme |
|---------|---------------------|----------------------|---------------------|--------------|------------|
| VSD + vana elim. | 2.1 | 12,600 | 1,260 | 3,000-5,000 | 2.4-4.0 yil |
| Motor IE4 | 0.5 | 3,000 | 300 | 800-1,200 | 2.7-4.0 yil |
| Impeller trim | 0.3 | 1,800 | 180 | 200-500 | 1.1-2.8 yil |
| Boru temizligi | 0.4 | 2,400 | 240 | 100-300 | 0.4-1.3 yil |
| TOPLAM | 3.3 | 19,800 | 1,980 | 4,100-7,000 | — |
```

## 4. Kisma Vanasi Analizi — Tamamen Kacinilabilir (theta = 1.0)

### 4.1 Termodinamik Aciklama

Kisma vanasi izentalpik genlesme (isenthalpic throttling) ile basinc dusurur. Bu surec %100 tersinmez (irreversible) dir. Cunku:

- Akiskanin basinci duserken sicakliginda anlamli degisim olmaz (sikistirilamaz sivi)
- Basinc dususu, ic surtunum yoluyla tamamen isi enerjisine donusur
- Isi, cevreye dagildigi icin kayip exergy'dir
- Bu surec hicbir faydali is uretmez

### 4.2 Kisma Vanasi Exergy Yikimi Hesabi

```
I_vana = rho × g × Q × DeltaH_vana / 1000

I_vana = 1000 × 9.81 × 0.00694 × 10 / 1000
       = 0.68 kW

Alternatif formulasyon (basinc cinsinden):
I_vana = Q × DeltaP_vana / 1000
       = 0.00694 × (1000 × 9.81 × 10) / 1000
       = 0.00694 × 98100 / 1000
       = 0.68 kW
```

### 4.3 Kisma Vanasinin Kacinilabilirlik Orani

```
theta_vana = 1.0

Aciklama: BAT'ta (en iyi mevcut teknoloji) kisma vanasi YOKTUR.
VSD ile debi kontrolu yapilir ve pompa hizi azaltilarak
istenilen calisma noktasina ulasilir.

Kisma vanasi yikiminin tamami kacinilabilirdir.
I_AV_vana = I_vana = 0.68 kW
I_UN_vana = 0 kW
```

### 4.4 Kisma Vanasi Eliminasyonu Stratejisi

Kisma vanasi eliminasyonu icin sirasiyla su adimlar uygulanir:

```
1. VSD kurulumu → pompa hizini azaltarak vana fonksiyonu devredisi birakilir
2. Vana tam acik pozisyona getirilir
3. Sistem calisma noktasi dogrulanir
4. Gerekirse impeller trim ile ince ayar yapilir

Beklenen sonuc:
- Vana kaybi: 0.68 kW → 0 kW (tamamen elimine)
- VSD kaybi (yeni): ~0.15 kW (VSD verimi %97-98)
- Net kazanim: 0.68 - 0.15 = 0.53 kW
- Ek kazanim: Pompa BEP'e yakinlasir → +0.2-0.5 kW daha
```

## 5. VSD Analizi Ileri Exergy Perspektifinden

### 5.1 VSD'nin Dort Bolumlu Dekompozisyona Etkisi

VSD eklenmesi, dort bilesenin her birini farkli oranlarda etkiler:

```
| Bilesen | VSD Oncesi (kW) | VSD Sonrasi (kW) | Degisim | Aciklama |
|---------|----------------|------------------|---------|----------|
| I_EN_AV | 3.2 | 1.0 | -2.2 kW | Vana eliminasyonu + BEP yakinlasma |
| I_EN_UN | 1.5 | 1.3 | -0.2 kW | Hafif iyilesme (kucuk etki) |
| I_EX_AV | 0.7 | 0.5 | -0.2 kW | Sistem egrisi uzerinde daha iyi nokta |
| I_EX_UN | 0.4 | 0.4 | 0 kW | Degismez (fiziksel yapi ayni) |
| VSD kaybi| — | 0.3 | +0.3 kW | VSD verimi %97 civarinda |
| TOPLAM  | 5.8 | 3.5 | -2.3 kW net | %40 toplam iyilesme |
```

### 5.2 Affinity Yasalari ile Kismi Yukte Guc Tasarrufu

Santrifuj pompada hiz dusurulurse (VSD ile):

```
Q2/Q1 = N2/N1
H2/H1 = (N2/N1)^2
P2/P1 = (N2/N1)^3

Ornek: Debi %80'e dusurmek icin hiz %80'e dusurulur.
Guc tuketimi: (0.80)^3 = 0.512 → %48.8 guc tasarrufu

Ancak bu sadece saf surtunum sistemi icin gecerlidir.
Statik head varsa tasarruf azalir (asagiya bakiniz).
```

### 5.3 Statik Head Oraninin VSD Etkisine Etkisi

Statik head orani yukseldikce VSD'nin exergy iyilestirmesi azalir:

```
| H_static/H_total | VSD ile Guc Tasarrufu (%80 debide) | I_AV Azaltma Orani |
|-------------------|-----------------------------------|-------------------|
| 0.00 (saf surtunum) | %48.8 | %85-90 |
| 0.20 | %38.5 | %70-80 |
| 0.40 | %28.1 | %55-65 |
| 0.60 | %17.8 | %35-45 |
| 0.80 | %7.4 | %15-20 |
| 1.00 (saf statik) | %0 | %0 |
```

**Ileri exergy yorumu:** Statik head bileseni I_EX_UN kategorisine girer. Bu nedenle yuksek statik head oranli sistemlerde VSD'nin I_AV azaltma potansiyeli sinirlidir. Bu kisimdaki yikim kacinılamazdir cunku fiziksel yukseklik farkinin ustesinden gelmek icin minimum enerji gereklidir.

### 5.4 VSD Motor Verimi Etkilesimi

VSD dusuk hizda motor verimini etkiler:

```
| Motor Hizi (% nominal) | Motor Verimi (IE2) | Motor Verimi (IE3) | Motor Verimi (IE4) |
|------------------------|--------------------|--------------------|-------------------|
| 100% | 0.930 | 0.945 | 0.960 |
| 80% | 0.915 | 0.932 | 0.950 |
| 60% | 0.890 | 0.910 | 0.935 |
| 50% | 0.870 | 0.895 | 0.920 |
| 40% | 0.840 | 0.870 | 0.900 |
| 25% | 0.780 | 0.820 | 0.860 |
```

**Sonuc:** Dusuk hizda verim duser, ancak kubik guc azalmasi (affinity law) bunun ustesinden gelir. Net etki her zaman pozitiftir (kisma vanasina kiyasla). Ancak cok dusuk hizlarda (<%30) net tasarruf daralir.

## 6. Motor Verimlilik Sinifi Etkisi (IE2 vs IE3 vs IE4)

### 6.1 IEC 60034-30-1 Standardi

Motor verimlilik siniflari ve tipik degerler (4-kutuplu, 50 Hz):

```
| Motor Gucu | IE2 (High) | IE3 (Premium) | IE4 (Super Premium) | IE4-IE2 Farki |
|-----------|-----------|--------------|--------------------|--------------|
| 3 kW | 0.868 | 0.893 | 0.912 | +0.044 |
| 7.5 kW | 0.895 | 0.917 | 0.937 | +0.042 |
| 11 kW | 0.908 | 0.930 | 0.948 | +0.040 |
| 15 kW | 0.915 | 0.937 | 0.955 | +0.040 |
| 22 kW | 0.924 | 0.943 | 0.960 | +0.036 |
| 37 kW | 0.933 | 0.951 | 0.966 | +0.033 |
| 75 kW | 0.945 | 0.960 | 0.972 | +0.027 |
```

### 6.2 Motor Yukseltmenin Ileri Exergy Etkisi

15 kW pompa ornegi icin (motor yukleme %74):

```
Motor kaybi hesabi:
I_motor = P_electric × (1 - eta_motor)

IE2 (mevcut): I_motor = 11.15 × (1 - 0.93) = 0.78 kW
IE3: I_motor = 11.15 × (1 - 0.945) = 0.61 kW → 0.17 kW kazanim
IE4: I_motor = 11.15 × (1 - 0.96) = 0.45 kW → 0.33 kW kazanim

Motor yukseltmenin dort bolumlu ayrimi:
- Tamami I_EN_AV kategorisindedir (pompanin kendi bileseni, kacinilabilir)
- Motor yukseltme maliyeti: IE2→IE4 icin yaklasik %15-25 fiyat farki
- 15 kW motor icin: ~300-600 EUR ek maliyet
- Yillik tasarruf: 0.33 × 6000 × 0.10 = 198 EUR/yil
- Geri odeme: 1.5-3.0 yil
```

### 6.3 Ileri Exergy Perspektifinden Motor Sinifi Degerlendirmesi

```
Motor kaybi tamamen I_EN kategorisindedir.
IE4'un bile kalan kaybi I_EN_UN'dur (termodinamik motor limiti).

| Motor Sinifi | I_motor (kW) | I_EN_AV_motor (kW) | I_EN_UN_motor (kW) |
|-------------|-------------|--------------------|--------------------|
| IE2 | 0.78 | 0.33 | 0.45 |
| IE3 | 0.61 | 0.16 | 0.45 |
| IE4 | 0.45 | 0.00 | 0.45 |

IE4'te I_EN_AV_motor = 0 cunku BAT kosulu olarak IE4 tanimlanmistir.
I_EN_UN_motor = 0.45 kW, motorun termodinamik kayip alt siniridir.
```

## 7. Impeller Trimming vs VSD: Ileri Exergy Karsilastirmasi

### 7.1 Genel Karsilastirma

Her iki yontem de calisma noktasini sistem gereksinimlerine uyarlar, ancak ileri exergy perspektifinden farkli bilesenleri hedeflerler.

```
IMPELLER TRIMMING:
- Sabit hiz, kucuk impeller
- Pompa egrisi kalici olarak degisir
- Tek bir calisma noktasi icin optimize
- Farkli debi ihtiyaclarina uyum saglaYAMAZ
- I_EN_AV'nin bir kismini giderir (sabit is noktasi)
- Ek exergy kaybi yok (mekanik islem)
- Maliyet: 200-500 EUR (tek seferlik)

VSD:
- Degisken hiz, ayni impeller
- Pompa egrisi dinamik olarak degisir
- Birden fazla calisma noktasina uyum saglayabilir
- I_EN_AV'nin buyuk kismini giderir
- VSD kaybi eklenir (~%2-3 tam yukte, ~%5-8 dusuk yukte)
- Maliyet: 2,000-8,000 EUR (motor gucune bagli)
```

### 7.2 Dort Bolumlu Karsilastirma Tablosu

```
| Parametre | Mevcut (Vana) | Impeller Trim | VSD | VSD + IE4 Motor |
|-----------|--------------|---------------|-----|----------------|
| I_EN_AV (kW) | 3.2 | 1.8 | 1.0 | 0.7 |
| I_EN_UN (kW) | 1.5 | 1.5 | 1.3 | 1.1 |
| I_EX_AV (kW) | 0.7 | 0.6 | 0.5 | 0.5 |
| I_EX_UN (kW) | 0.4 | 0.4 | 0.4 | 0.4 |
| VSD/ek kayip | 0 | 0 | 0.3 | 0.3 |
| I_total (kW) | 5.8 | 4.3 | 3.5 | 3.0 |
| theta | 0.79 | 0.65 | 0.52 | 0.43 |
| Yatirim (EUR)| — | 400 | 4,000 | 4,800 |
```

### 7.3 Karar Kriterleri

```
IMPELLER TRIM tercih edilir:
- Debi ihtiyaci sabit ve ongorulubilir
- Proses degisikligi beklenmiyorsa
- Bütce kisitli ise (en dusuk maliyet)
- VSD harmonik sorunlari onlenemiyorsa

VSD tercih edilir:
- Debi ihtiyaci degisken (gunluk/mevsimsel)
- Kisma vanasi mevcut ve debi sureki ayarlaniyor
- Coklu calisma noktasi gerekli
- Uzun vadeli esneklik isteniyor
- I_EN_AV / I_total > 0.50 (yuksek iyilestirme potansiyeli)

HER IKISI birlikte:
- VSD kurulumu + impeller trim ile optimum BEP yakinsama
- En dusuk I_EN_AV'yi verir
- Kompleks sistemlerde onerilen yaklasim
```

## 8. Sistem Egrisi Etkilesimleri

### 8.1 Pompa Egrisi + Sistem Egrisi Kesisimi

Calisma noktasi, pompa H-Q egrisi ile sistem egrisi kesisiminde olusur:

```
H_pompa(Q) = H_sistem(Q)
A - B × Q^2 = H_static + K × Q^2

Cozum:
Q_op = sqrt[(A - H_static) / (B + K)]
H_op = H_static + K × Q_op^2
```

### 8.2 Sistem Egrisi Degisikligi ve Ekzojenik Etki

Sistem egrisi zamanla degisir. Bu degisiklikler I_EX bilesenini etkiler:

```
| Degisiklik | Etki | I_EX Degisimi | Kacinilabilir mi? |
|-----------|------|--------------|-------------------|
| Boru kirlenmesi (fouling) | K artar, Q duser | I_EX_AV artar | Evet (temizlik) |
| Vana kismasi | K artar | I_EX_AV artar | Evet (VSD ile eliminasyon) |
| Downstream basinc artisi | H_static artar | I_EX_UN artar | Kismen |
| Filtre tikanmasi | K artar | I_EX_AV artar | Evet (filtre degisimi) |
| Boru yasi (korozyon) | K artar | I_EX_UN artar | Hayir (yapısal) |
| Sivi sicaklik degisimi | Viskosite degisir | I_EX_AV degisir | Kismen |
```

### 8.3 Paralel Pompa Operasyonunda Ekzojenik Etki

Paralel pompalar birbirlerinin calisma noktasini etkiler:

```
Senaryo: 2 esit pompa paralel calisiyor
- Tek pompa BEP: Q=25 m³/h, H=35 m, eta=0.82
- Paralel calisma noktasi: Her pompa Q=18 m³/h, H=42 m, eta=0.74

Verim dususu: 0.82 → 0.74 (%10 dusus)
Bu verim dususunun yaklasik %60'i ekzojenik (diger pompadan kaynaklanan etki)
                           %40'i endojenik (BEP'ten uzaklasma)

Ileri exergy acisindan:
- 1. pompanin I_EX'i, 2. pompanin varligindan etkilenir
- Eger 1 pompa yeterliyse, 2. pompanin kapatilmasi I_EX'i azaltir
- VSD ile her pompanin hizi bagimsiz ayarlanabilir → I_EX_AV minimize edilir
```

## 9. Tam Adim Adim Hesaplama Rehberi

### 9.1 Veri Toplama

```
Gerekli olcumler:
1. Motor elektrik gucu: P_electric (kW) — guc analizoru ile
2. Debi: Q (m³/h) — ultrasonik debimetre veya orifis
3. Emis basinci: P_suction (bar) — basinc transmitteri
4. Basma basinci: P_discharge (bar) — basinc transmitteri
5. Motor devir: N (rpm) — takometri veya VSD'den
6. Motor plaka verimi: eta_motor_plaka
7. Sivi sicakligi: T (°C)
8. Sivi yogunlugu: rho (kg/m³)

Hesaplanan degerler:
- H_total = (P_discharge - P_suction) / (rho × g) × 100000  [m]
- P_hyd = rho × g × Q/3600 × H_total / 1000  [kW]
- eta_w2w = P_hyd / P_electric
```

### 9.2 Konvansiyonel Exergy Analizi

```
Adim 1: Exergy girisi = P_electric (elektrik saf exergy)
Adim 2: Exergy cikisi = P_hyd_net (faydali hidrolik guc, vana kaybi cikarilmis)
Adim 3: I_total = P_electric - P_hyd_net
Adim 4: epsilon = P_hyd_net / P_electric
```

### 9.3 Kacinilabilir/Kacinılamaz Ayirimi

```
Adim 5: BAT parametrelerini belirle
  - eta_h_UN = 0.88
  - eta_motor_UN = 0.96
  - eta_mech_UN = 0.98
  - Vana = YOK

Adim 6: I_UN hesapla
  P_electric_UN = P_hyd_net / (eta_h_UN × eta_mech_UN × eta_motor_UN)
  I_UN = P_electric_UN - P_hyd_net

Adim 7: I_AV hesapla
  I_AV = I_total - I_UN

Adim 8: theta hesapla
  theta = I_AV / I_total
```

### 9.4 Endojenik/Ekzojenik Ayirimi

```
Adim 9: Ideal sistem kosullarini tanimla
  - Boru surtunum kaybi: minimum (optimum cap)
  - Vana: tam acik veya yok
  - Downstream basinc: minimum gerekli

Adim 10: Endojenik yikim hesapla
  I_EN = I_total(pompa gercek, sistem ideal)
  Bu deger, pompanin kendi ic kayiplarini temsil eder.

Adim 11: Ekzojenik yikim hesapla
  I_EX = I_total - I_EN
  Bu deger, sistem kaynaklarindan pompadaki ek yikimi temsil eder.
```

### 9.5 Dort Bolumlu Birlesim

```
Adim 12: Dort bileseni hesapla
  I_EN_AV = I_EN - I_EN_UN
  I_EN_UN = I_EN(pompa BAT kosullarinda, sistem ideal)
  I_EX_AV = I_EX - I_EX_UN
  I_EX_UN = I_EX(pompa BAT, sistem BAT)

Adim 13: Dogrulama
  I_EN_AV + I_EN_UN + I_EX_AV + I_EX_UN = I_total  (hata < %1 olmali)

Adim 14: Yorumlama
  - I_EN_AV en buyukse → pompa iyilestirmesine odaklan
  - I_EX_AV en buyukse → sistem optimizasyonuna odaklan
  - I_EN_UN + I_EX_UN > %70 ise → sinirli iyilestirme potansiyeli
```

## 10. Tipik Pompa Sistemlerinde theta Degerleri

Farkli pompa sistemi konfigurasyonlari icin beklenen theta degerleri:

```
| Sistem Konfigurasyonu | Tipik theta | I_EN_AV % | I_EX_AV % | Oncelikli Aksiyon |
|----------------------|------------|----------|----------|-------------------|
| Vana kontrol, asiri boyut | 0.65-0.80 | 45-60 | 10-20 | VSD + dogru boyut |
| Vana kontrol, dogru boyut | 0.45-0.60 | 30-45 | 10-15 | VSD retrofit |
| VSD, asiri boyut | 0.35-0.50 | 20-35 | 10-15 | Impeller trim |
| VSD, dogru boyut | 0.25-0.40 | 15-25 | 5-10 | Motor yukseltme |
| VSD + IE4 + dogru boyut | 0.15-0.25 | 10-15 | 3-8 | Bakim optimizasyonu |
| Tam optimize | 0.10-0.15 | 7-10 | 2-5 | Termodinamik limit |
```

## 11. Hassasiyet Analizi: BAT Parametre Seciminin Etkisi

BAT parametreleri secimi sonuclari onemli olcude etkiler:

```
| BAT Senaryosu | eta_h_UN | eta_motor_UN | theta | Yorum |
|--------------|---------|-------------|-------|-------|
| Agresif | 0.92 | 0.97 | 0.84 | Teorik limite yakin, gercekci degil |
| Onerilen (varsayilan) | 0.88 | 0.96 | 0.79 | Piyasa en iyisi, gercekci |
| Muhafazakar | 0.85 | 0.95 | 0.73 | Eski teknoloji en iyisi |
| Cok muhafazakar | 0.82 | 0.94 | 0.66 | Mevcut tesise yakin |
```

**Oneri:** Raporlamada her zaman kullanilan BAT parametrelerini acikca belirtin. Mumkunse hem onerilen hem de muhafazakar senaryolari sunun.

## 12. Endustriyel Uygulama Ipuclari

### 12.1 Hizli Degerlendirme Icin Pratik Kurallar

```
Kural 1: Kisma vanasi varsa theta >= 0.60 → mutlaka VSD degerlendir
Kural 2: Wire-to-water < 0.40 ve vana yoksa → asiri boyutlanma veya bakim sorunu
Kural 3: Motor IE2 ve > 5000 saat/yil → IE4 yukseltme genellikle ekonomik
Kural 4: H_static/H_total > 0.60 → VSD etkisi sinirli, diger aksiyonlara odaklan
Kural 5: Paralel pompa, biri surekli → VSD ile sira kontrol degerlendir
```

### 12.2 ExergyLab Platformunda Kullanim

ExergyLab pompa analizi yapildiginda, ileri exergy sonuclari otomatik olarak hesaplanir:

1. Kullanici motor gucu, debi, head ve vana bilgilerini girer
2. Engine konvansiyonel exergy analizini yapar
3. BAT veritabani kullanilarak dort bolumlu dekompozisyon hesaplanir
4. AI yorumcu, theta degerine gore oncelikli aksiyonlari sıralar
5. Yatirim-tasarruf analizi otomatik olarak sunulur

## İlgili Dosyalar

- `knowledge/factory/advanced_exergy/avoidable_unavoidable.md` — Genel kacinilabilir/kacinılamaz teorisi ve metodoloji
- `knowledge/pump/formulas.md` — Pompa exergy temel hesaplama formulleri
- `knowledge/pump/benchmarks.md` — Pompa sektorel benchmark verileri
- `knowledge/pump/equipment/centrifugal.md` — Santrifuj pompa detaylari
- `knowledge/pump/equipment/motors_drives.md` — Motor ve surucu bilgileri
- `knowledge/pump/solutions/vsd.md` — VSD uygulama detaylari
- `knowledge/pump/solutions/impeller_trimming.md` — Impeller trim teknigi
- `knowledge/pump/solutions/throttle_elimination.md` — Kisma vanasi eliminasyonu
- `knowledge/pump/solutions/system_optimization.md` — Sistem optimizasyonu
- `knowledge/pump/solutions/motor_upgrade.md` — Motor yukseltme rehberi
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arasi exergy entegrasyonu
- `knowledge/factory/prioritization.md` — Yatirim onceliklendirme
- `skills/equipment/pump_expert.md` — Pompa uzman AI beceri dosyasi

## Referanslar

1. Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions and investment costs in thermal systems." *Energy Conversion and Management*, 43(9-12), 1259-1270. DOI: 10.1016/S0196-8904(02)00012-2

2. Kelly, S., Tsatsaronis, G. & Morosuk, T. (2009). "Advanced exergetic analysis: Approaches for splitting the exergy destruction into endogenous and exogenous parts." *Energy*, 34(3), 384-391. DOI: 10.1016/j.energy.2008.12.007

3. Morosuk, T. & Tsatsaronis, G. (2009). "Advanced exergy analysis for chemically reacting systems — Application to a simple open gas-turbine system." *International Journal of Thermodynamics*, 12(3), 105-111.

4. Bejan, A., Tsatsaronis, G. & Moran, M. (1996). *Thermal Design and Optimization*. John Wiley & Sons, New York. ISBN: 978-0-471-58467-4

5. Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A. (2012). "Conventional and advanced exergetic analyses applied to a combined cycle power plant." *Energy*, 41(1), 146-152. DOI: 10.1016/j.energy.2011.05.028

6. Bejan, A. (2006). *Advanced Engineering Thermodynamics*, 3rd Edition. John Wiley & Sons. ISBN: 978-0-471-67763-5

7. Europump & Hydraulic Institute (2001). *Pump Life Cycle Costs: A Guide to LCC Analysis for Pumping Systems*. Elsevier Science.

8. US DOE/AMO (2006). "Improving Pumping System Performance: A Sourcebook for Industry." DOE/GO-102006-2079.

9. Saidur, R., Mekhilef, S., Ali, M.B., Safari, A. & Mohammed, H.A. (2012). "Applications of variable speed drive (VSD) in electrical motors energy savings." *Renewable and Sustainable Energy Reviews*, 16(1), 543-550. DOI: 10.1016/j.rser.2011.08.020
