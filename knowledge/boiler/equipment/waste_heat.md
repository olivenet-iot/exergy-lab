---
title: "Atık Isı Kazanı / HRSG — Waste Heat Recovery Boiler"
category: equipment
equipment_type: boiler
subtype: "Atık Isı Kazanı"
keywords: [atık ısı, kazan, geri kazanım]
related_files: [boiler/benchmarks.md, boiler/formulas.md, factory/waste_heat_recovery.md]
use_when: ["Atık ısı kazanı analizi yapılırken", "Proses atık ısısı değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Atık Isı Kazanı / HRSG — Waste Heat Recovery Boiler

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Atık ısı kazanı, HRSG (Heat Recovery Steam Generator)
- Isı kaynakları (heat sources): Gaz türbini egzozu (450-600°C), motor egzozu (350-500°C), proses atık ısısı (200-800°C)
- Kapasite: 1-500+ ton/saat buhar üretimi
- Basınç: 5-120 bar (tek veya çok basınçlı — single or multi-pressure)
- Enerji verimi: %60-85 (egzoz gazı giriş sıcaklığına bağlı)
- Ekserji verimi: %35-55 (yanma tersinmezliği başka yerde gerçekleştiğinden, ateşli kazanlardan daha yüksek olabilir)
- Tipler: Tek basınçlı (single pressure), çift basınçlı (dual pressure), üç basınçlı (triple pressure), ek yakmalı (supplementary fired) / ek yakmasız (unfired)
- Markalar: Aalborg (Alfa Laval), NEM Energy, Nooter/Eriksen, CMI Group, Rentech, Vogt Power International
- Uygulama alanları: Kombine çevrim enerji santralleri, kojenerasyon (CHP) tesisleri, proses endüstrisi (çimento, cam, çelik), gemi motorları atık ısı geri kazanımı
- Standartlar: ASME Section I, EN 12952, API 560, NFPA 85

## Çalışma Prensibi
- HRSG'de yanma yoktur (ek yakmalı — supplementary fired tipler hariç); ısı kaynağı tamamen egzoz gazıdır
- Sıcak egzoz gazı, HRSG içindeki ısı değiştirici yüzeylerden geçerek enerjisini suya/buhara aktarır
- Isı transferi mekanizması: Konveksiyon ağırlıklı (radyasyon payı düşük, çünkü alev yoktur)
- Gaz akış yönüne göre iki ana tip:
  - Yatay akışlı (horizontal gas flow): Avrupa tipi, dikey borular
  - Dikey akışlı (vertical gas flow): Amerikan tipi, yatay borular
- Temel bileşenler sıcak gazdan soğuk gaza doğru:
  1. Kızdırıcı (superheater) — kuru buharı kızdırarak istenen sıcaklığa getirir
  2. Buharlaştırıcı (evaporator) — doyma noktasında su/buhar karışımı oluşturur
  3. Ekonomizer (economizer) — besleme suyunu ön ısıtır
- Doğal sirkülasyonlu (natural circulation) veya zorlanmış sirkülasyonlu (forced circulation) tasarım uygulanabilir
- Pinch point ve approach temperature tasarımın temel kısıtlarıdır; bkz. `## Pinch Point Analizi`

## Pinch Point Analizi

Pinch point (sıkışma noktası), HRSG tasarımında en kritik parametredir. Buharlaştırıcı çıkışında egzoz gazı sıcaklığı ile doyma sıcaklığı arasındaki farkı ifade eder.

```
Pinch point = T_gaz,buharlaştırıcı_çıkışı - T_doyma

Burada:
  T_gaz,buharlaştırıcı_çıkışı : Egzoz gazının buharlaştırıcıyı terk ettiği sıcaklık (°C)
  T_doyma                     : Çalışma basıncındaki doyma sıcaklığı (°C)
  Tipik aralık                : 8-15°C (optimum tasarım)
```

Approach temperature (yaklaşma sıcaklığı), ekonomizer çıkışındaki su sıcaklığı ile doyma sıcaklığı arasındaki farkı ifade eder.

```
Approach temperature = T_doyma - T_ekonomizer_çıkışı

Burada:
  T_doyma              : Çalışma basıncındaki doyma sıcaklığı (°C)
  T_ekonomizer_çıkışı  : Ekonomizerden çıkan suyun sıcaklığı (°C)
  Tipik aralık         : 5-10°C
```

### Pinch Point'in Etkisi

| Pinch Point (°C) | Isı Geri Kazanım Oranı | Isı Transfer Yüzeyi | Yatırım Maliyeti |
|-------------------|------------------------|----------------------|------------------|
| 5-8 | Yüksek (%80-85) | Büyük | Yüksek (EUR) |
| 8-12 | Orta (%75-80) | Orta | Orta |
| 12-20 | Düşük (%65-75) | Küçük | Düşük |
| >20 | Çok düşük (<65%) | Minimum | En düşük |

Pinch point düşürüldükçe daha fazla ısı geri kazanılır, ancak gerekli ısı transfer yüzeyi ve dolayısıyla yatırım maliyeti artar. Ekonomik optimum genellikle 8-12°C aralığındadır.

### Sıcaklık-Isı (T-Q) Diyagramı Yorumu

```
Sıcaklık (°C)
  |
  |  Egzoz gazı ------\
  |                     \
  |                      \______ Pinch point
  |                       \
  |                        \______
  |  Buhar/Su   ___________/      \
  |            /   Evaporator      \  Ekonomizer
  |  Kızdırıcı                     \______
  |
  +------------------------------------------→ Isı transferi (Q, kW)
```

T-Q diyagramında egzoz gazı ve su/buhar profilleri arasındaki en dar nokta pinch point'tir. Bu nokta, HRSG'nin toplam ısı geri kazanım kapasitesini sınırlar.

## Enerji Dağılımı

Tipik bir gaz türbini + HRSG kombine çevrim sisteminde enerji dağılımı:

| Enerji Kalemi | Oran (%) | Açıklama |
|---------------|----------|----------|
| Gaz türbini elektrik üretimi | 33-38 | Yakıt enerjisinin doğrudan elektriğe dönüşen kısmı |
| HRSG buhar üretimi | 25-35 | Egzoz gazından geri kazanılan enerji |
| Baca gazı kaybı | 8-15 | HRSG çıkışında kalan ısı (80-120°C) |
| Radyasyon ve konveksiyon kayıpları | 0.5-1.5 | HRSG gövdesinden çevreye kayıp |
| Blöf (blowdown) kaybı | 0.5-2.0 | Kazanın su kalitesi kontrolü için yapılan deşarj |
| Toplam verim (kombine çevrim) | 55-62 | Gaz türbini + buhar türbini toplam |

### Ekserji Dağılımı

```
Ekserji dengesi (HRSG bölümü):

Ex_gaz,giriş = Ex_buhar,çıkış + Ex_gaz,çıkış + Ex_yıkım + Ex_kayıp

Burada:
  Ex_gaz,giriş    : Egzoz gazının HRSG'ye giriş ekserjisi (kW)
  Ex_buhar,çıkış  : Üretilen buharın ekserjisi (kW)
  Ex_gaz,çıkış    : Baca gazının çıkış ekserjisi (kW)
  Ex_yıkım        : Isı transferi tersinmezliği nedeniyle yıkılan ekserji (kW)
  Ex_kayıp         : Çevreye kaybedilen ekserji (kW)
```

```
HRSG ekserji verimi:

η_ex,HRSG = Ex_buhar,çıkış / Ex_gaz,giriş

Tipik değer: %35-55

Ekserji yıkımının ana kaynakları:
  1. Isı transferi sıcaklık farkı (ΔT): %60-70 (en büyük pay)
  2. Basınç düşümleri (gaz ve su tarafı): %10-15
  3. Karışma (mixing) kayıpları: %5-10
  4. Isı kayıpları (çevreye): %5-10
```

## Supplementary Firing (Ek Yakma)

Ek yakma (supplementary firing / duct firing), HRSG öncesinde veya ilk bölümünde egzoz gazına ek yakıt (genellikle doğalgaz) verilerek gaz sıcaklığının artırılması işlemidir.

### Ne Zaman Kullanılır?
- Pik buhar talebi dönemlerinde ek kapasite gerektiğinde
- Gaz türbini kısmi yükte çalışırken buhar üretimini sabit tutmak için
- Proses buharı talebinin gaz türbini egzoz ısısından fazla olduğu tesislerde
- Kojenerasyon tesislerinde ısı/elektrik oranını (heat-to-power ratio) ayarlamak için

### Kapasite ve Sıcaklık Artışı

| Parametre | Ek Yakmasız | Düşük Ek Yakma | Yüksek Ek Yakma |
|-----------|-------------|-----------------|-------------------|
| Egzoz gazı sıcaklığı | 450-600°C | 600-750°C | 750-900°C |
| Ek buhar kapasitesi | Baz (referans) | +30-60% | +60-120% |
| O₂ tüketimi (egzozdaki) | %12-15 | %8-12 | %3-8 |
| HRSG enerji verimi | %75-85 | %80-90 | %85-92 |
| HRSG ekserji verimi | %40-55 | %35-48 | %30-42 |

### Verim ve Ekserji Etkisi

```
Ek yakma ile toplam enerji verimi artarken ekserji verimi düşer:

η_enerji,ek_yakma > η_enerji,ek_yakmasız   (enerji verimi artar)
η_ekserji,ek_yakma < η_ekserji,ek_yakmasız  (ekserji verimi düşer)

Nedeni:
  - Yüksek sıcaklıklı yanma (~1,800°C alev sıcaklığı) ile
    orta sıcaklıklı buhar üretimi (~250-540°C) arasındaki
    büyük sıcaklık farkı ekserji yıkımını artırır
  - Yanma tersinmezliği ek ekserji yıkımı oluşturur
```

Ek yakma kararı ekonomik bir optimizasyondur: Ek buhar geliri ile yakıt maliyeti karşılaştırılmalıdır. Ekserji perspektifinden, ek yakma yerine ısı pompası veya organik Rankine çevrimi (ORC) gibi alternatifler değerlendirilmelidir.

## Ölçülmesi Gereken Parametreler

### Egzoz Gazı Tarafı

| Parametre | Sembol | Birim | Ölçüm Yöntemi | Doğruluk |
|-----------|--------|-------|----------------|----------|
| Egzoz gazı giriş sıcaklığı | T_gaz,in | °C | Termokupl (K-tipi) | +/- 2°C |
| Egzoz gazı çıkış sıcaklığı (baca) | T_gaz,out | °C | Termokupl (K-tipi) | +/- 2°C |
| Egzoz gazı debisi | m_gaz | kg/s | Pitot tüpü veya ultrasonik | +/- 3% |
| Egzoz gazı bileşimi (O₂, CO₂, CO) | — | % vol | Gaz analizörü | +/- 0.1% |
| Gaz tarafı basınç düşümü | ΔP_gaz | mbar | Diferansiyel basınç | +/- 0.5 mbar |

### Su/Buhar Tarafı

| Parametre | Sembol | Birim | Ölçüm Yöntemi | Doğruluk |
|-----------|--------|-------|----------------|----------|
| Besleme suyu giriş sıcaklığı | T_su,in | °C | PT100 | +/- 0.5°C |
| Buhar çıkış sıcaklığı | T_buhar,out | °C | Termokupl | +/- 2°C |
| Buhar çıkış basıncı | P_buhar | bar | Basınç transmitteri | +/- 0.25% |
| Buhar debisi | m_buhar | ton/saat | Orifis / vortex metre | +/- 2% |
| Besleme suyu debisi | m_su | ton/saat | Elektromanyetik metre | +/- 1% |
| Blöf debisi | m_blöf | ton/saat | Orifis | +/- 5% |
| Drum seviyesi | L_drum | mm | Diferansiyel basınç | +/- 10 mm |
| Besleme suyu iletkenliği | κ | µS/cm | Konduktivite sensörü | +/- 2% |

### Ek Yakma Sistemi (varsa)

| Parametre | Sembol | Birim | Ölçüm Yöntemi | Doğruluk |
|-----------|--------|-------|----------------|----------|
| Ek yakıt debisi | m_yakıt | Nm³/saat | Türbin metre | +/- 1% |
| Yakıt giriş sıcaklığı | T_yakıt | °C | PT100 | +/- 1°C |
| Yakıt giriş basıncı | P_yakıt | bar | Basınç transmitteri | +/- 0.5% |

## Varsayılan Değerler (Ölçüm Yoksa)

Aşağıdaki değerler, tesis verisi mevcut olmadığında ekserji hesaplamalarında başlangıç tahmini olarak kullanılabilir.

| Parametre | Varsayılan Değer | Birim | Kaynak / Not |
|-----------|------------------|-------|--------------|
| Egzoz gazı giriş sıcaklığı (gaz türbini) | 550 | °C | Tipik ağır hizmet gaz türbini |
| Egzoz gazı çıkış sıcaklığı (baca) | 100 | °C | Ekonomizerli HRSG |
| Egzoz gazı debisi | Gaz türbini kapasitesine bağlı | kg/s | Üretici verisi gerekir |
| Egzoz gazı cp (ortalama) | 1.10 | kJ/(kg·K) | 200-550°C aralığı |
| Pinch point | 10 | °C | Standart tasarım |
| Approach temperature | 8 | °C | Standart tasarım |
| Buhar basıncı (tek basınçlı, endüstriyel) | 40 | bar | Tipik proses buharı |
| Buhar sıcaklığı (kızdırılmış) | 400 | °C | Tipik proses buharı |
| Besleme suyu sıcaklığı | 105 | °C | Degazör çıkışı |
| Blöf oranı | %2 | — | İyi su kalitesi ile |
| Radyasyon/konveksiyon kaybı | %0.5 | — | İzolasyonlu gövde |
| Gaz tarafı basınç düşümü | 25 | mbar | Tipik tasarım |
| HRSG enerji verimi | 78 | % | Ek yakmasız, tek basınçlı |
| HRSG ekserji verimi | 45 | % | Ek yakmasız, tek basınçlı |
| Referans çevre sıcaklığı (T₀) | 25 | °C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 | kPa | Standart ölü durum |

## Performans Tablosu

### Basınç Seviyesine Göre HRSG Performansı (Gaz Türbini Egzozu ~550°C)

| Parametre | Tek Basınçlı | Çift Basınçlı | Üç Basınçlı |
|-----------|-------------|---------------|-------------|
| Yüksek basınç (HP) | 40-80 bar | 60-120 bar | 80-170 bar |
| Orta basınç (IP) | — | — | 20-40 bar |
| Düşük basınç (LP) | — | 4-8 bar | 3-6 bar |
| HP buhar sıcaklığı | 350-450°C | 450-540°C | 540-600°C |
| Baca gazı çıkış sıcaklığı | 150-200°C | 110-150°C | 80-110°C |
| Isı geri kazanım oranı | %65-75 | %75-82 | %82-88 |
| Enerji verimi | %70-80 | %78-85 | %83-90 |
| Ekserji verimi | %35-45 | %42-50 | %48-55 |
| Buhar türbini çıkışı (MW, 100 MW GT) | 30-38 | 38-45 | 45-55 |
| Kombine çevrim toplam verim | %48-52 | %52-57 | %57-62 |
| Tahmini yatırım maliyeti (EUR/kW) | 200-350 | 350-500 | 500-750 |

### Farklı Isı Kaynaklarına Göre HRSG Performansı

| Isı Kaynağı | Gaz Sıcaklığı (°C) | Debi (kg/s) | Uygun HRSG Tipi | Tahmini Verim (%) |
|-------------|---------------------|-------------|-----------------|-------------------|
| Ağır hizmet gaz türbini | 550-620 | 100-700 | Üç basınçlı + tekrar kızdırma | 85-90 |
| Aero-derivatif gaz türbini | 450-520 | 30-120 | Tek/çift basınçlı | 70-80 |
| Gaz motoru egzozu | 350-500 | 5-30 | Tek basınçlı | 60-72 |
| Dizel motor egzozu | 300-450 | 3-20 | Tek basınçlı | 55-68 |
| Çimento fırını çıkışı | 300-400 | 50-150 | Tek basınçlı (özel) | 55-65 |
| Cam fırını çıkışı | 400-550 | 10-50 | Tek/çift basınçlı | 65-78 |
| Çelik ark ocağı (EAF) | 200-800 (değişken) | Değişken | Özel tasarım | 45-60 |
| İncineration (atık yakma) | 800-1,000 | 10-50 | Su borulu (özel) | 70-80 |

## Kombine Çevrim Entegrasyonu

HRSG, kombine çevrim (combined cycle) enerji santrallerinde gaz türbini ile buhar türbini arasındaki köprüdür. Toplam sistem verimini doğrudan etkiler.

### Tipik Kombine Çevrim Konfigürasyonları

| Konfigürasyon | Gaz Türbini (MW) | HRSG Tipi | Buhar Türbini (MW) | Toplam Verim (%) |
|---------------|-------------------|-----------|---------------------|------------------|
| 1×1 (tek GT + tek ST) | 50-350 | Üç basınçlı + reheat | 25-180 | 57-62 |
| 2×1 (iki GT + tek ST) | 2×50-350 | 2× üç basınçlı + reheat | 50-360 | 58-63 |
| Küçük ölçekli (aero-derivatif) | 20-50 | Tek/çift basınçlı | 8-25 | 48-55 |
| Kojenerasyon (CHP) | 5-50 | Tek basınçlı | Geri basınçlı veya yok | 75-90 (toplam) |

### Tekrar Kızdırma (Reheat)

Büyük üç basınçlı HRSG'lerde HP türbinden çıkan buhar, HRSG'ye dönerek tekrar kızdırılır (reheat). Bu işlem:
- Buhar türbini verimini %2-4 artırır
- Türbin son kademe nemini azaltır
- Toplam kombine çevrim verimini %1-2 iyileştirir

```
Reheat ile ekserji kazancı:

ΔEx_reheat = m_buhar × [(h_reheat_out - h_reheat_in) - T₀ × (s_reheat_out - s_reheat_in)]

Burada:
  m_buhar         : Tekrar kızdırılan buhar debisi (kg/s)
  h_reheat_out    : Tekrar kızdırıcı çıkış entalpisi (kJ/kg)
  h_reheat_in     : Tekrar kızdırıcı giriş entalpisi (kJ/kg)
  s_reheat_out    : Tekrar kızdırıcı çıkış entropisi (kJ/(kg·K))
  s_reheat_in     : Tekrar kızdırıcı giriş entropisi (kJ/(kg·K))
  T₀              : Referans çevre sıcaklığı (K)
```

## Dikkat Edilecekler

1. **Pinch point optimizasyonu**: Çok düşük pinch point (<5°C) ısı transfer yüzeyini orantısız artırır ve ekonomik olmaz. Çok yüksek pinch point (>20°C) ise önemli enerji ve ekserji kaybına neden olur. Optimum 8-12°C arasındadır.

2. **Gaz tarafı basınç düşümü (back pressure)**: HRSG'deki gaz tarafı basınç düşümü, gaz türbini performansını doğrudan etkiler. Her 10 mbar ek basınç düşümü gaz türbini gücünü yaklaşık %0.3-0.5 azaltır. Tasarımda 20-35 mbar hedeflenmelidir.

3. **Düşük yük çalışması**: Gaz türbini kısmi yükte çalıştığında egzoz sıcaklığı ve debisi değişir. HRSG tasarımının geniş yük aralığında verimli çalışabilmesi için bypass damper ve kontrol stratejileri gereklidir.

4. **Korozyon ve asit çiğ noktası**: Doğalgaz yakıtlı gaz türbini egzozunda kükürt bulunmadığından asit çiğ noktası düşüktür (~55°C). Ancak ek yakma kullanılıyorsa veya yakıtta kükürt varsa, baca gazı sıcaklığı asit çiğ noktasının (120-160°C) altına düşürülmemelidir.

5. **Buhar kalitesi ve su kimyası**: HRSG'lerde yüksek basınçlı buhar üretimi için demineralize su (iletkenlik <0.1 µS/cm) kullanılmalıdır. Yetersiz su kalitesi tüp fouling, korozyon ve türbin kanatçık erozyonuna yol açar.

6. **Termal döngüler ve yorulma (thermal cycling / fatigue)**: Sık başlatma/durdurma (daily cycling) HRSG borularında termal gerilme ve yorulma çatlaklarına neden olabilir. Isınma/soğuma hızı kontrol edilmelidir: maksimum sıcaklık değişim hızı genellikle 3-5°C/dakika ile sınırlandırılır.

7. **Akış dağılımı ve dengesizlik**: Çok basınçlı HRSG'lerde farklı basınç seviyelerindeki buharlaştırıcılar arasında gaz akışının homojen dağılması kritiktir. Dengesiz akış, lokal aşırı ısınma (overheating) ve tüp hasarına yol açabilir.

8. **SCR ve DeNOx entegrasyonu**: NOx emisyon limitlerine uyum için HRSG içine SCR (Selective Catalytic Reduction) katalizörü yerleştirilebilir. Katalizör optimum çalışma sıcaklığı 300-400°C aralığındadır ve HRSG tasarımında uygun konuma yerleştirilmelidir.

## İlgili Dosyalar
- Kazan yakıtları ve özellikleri: `equipment/boiler_fuels.md`
- Ateş borulu buhar kazanları: `equipment/boiler_steam_firetube.md`
- Su borulu buhar kazanları: `equipment/boiler_steam_watertube.md`
- Kazan ekserji hesaplamaları: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Baca gazı ısı geri kazanımı: `solutions/boiler_flue_gas_recovery.md`
- Gaz türbini ekserji analizi: `equipment/gas_turbine.md`
- Buhar türbini ekserji analizi: `equipment/steam_turbine.md`
- Kombine çevrim enerji santralleri: `systems/combined_cycle.md`

## Referanslar
- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators: Design, Applications, and Calculations*, Marcel Dekker.
- Kehlhofer, R., et al. (2009). *Combined-Cycle Gas & Steam Turbine Power Plants*, 3rd ed., PennWell.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths. (Reprinted by Krieger, 1995.)
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
- ASME PTC 4.4 (2008). *Gas Turbine Heat Recovery Steam Generators — Performance Test Codes*, ASME.
- ASME Section I (2021). *Rules for Construction of Power Boilers*, ASME.
- EN 12952 (2011). *Water-tube Boilers and Auxiliary Installations*, CEN.
- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Rahim, M.A. (2012). *Combined Cycle Systems for Near-Zero Emission Power Generation*, Woodhead Publishing.
- Franco, A., Casarosa, C. (2002). "On some perspectives for increasing the efficiency of combined cycle power plants." *Applied Thermal Engineering*, 22(13), pp. 1501-1518.
- Reddy, B.V., Mohamed, K. (2007). "Exergy analysis of a natural gas fired combined cycle power generation unit." *International Journal of Exergy*, 4(2), pp. 180-196.
