---
title: "Absorpsiyonlu Chiller — Absorption Chiller"
category: equipment
equipment_type: chiller
subtype: "Absorpsiyon"
keywords: [absorpsiyon, chiller, LiBr, ısı kaynaklı]
related_files: [chiller/benchmarks.md, chiller/formulas.md, chiller/solutions/heat_recovery.md]
use_when: ["Absorpsiyon chiller analizi yapılırken", "Isı kaynaklı soğutma değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Absorpsiyonlu Chiller — Absorption Chiller

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Absorpsiyon soğutma çevrimi — ısı enerjisi ile çalışan soğutma sistemi
- Kapasite aralığı: 100 - 10,000+ kW (28 - 2,800+ ton)
- Çalışma çifti: LiBr-Su (pozitif basınç, konfor soğutma) veya NH₃-Su (negatif basınç, düşük sıcaklık)
- Enerji kaynağı: Buhar, sıcak su, doğrudan yakma (direct fired), atık ısı
- COP aralığı: Tek etkili 0.65-0.75, çift etkili 1.0-1.4, üç etkili 1.4-1.7
- Elektrik tüketimi: ~5-10 kW / 100 kW soğutma kapasitesi (çok düşük)
- Ekserji verimi (termal giriş bazlı): %10 - 28
- Yaygın markalar: Thermax, Broad, Carrier, York (Johnson Controls), LG, Hitachi, Ebara, Shuangliang
- Tipik uygulama: Trijenerasyon, atık ısı geri kazanımı, doğalgaz ile soğutma, güneş enerjisi soğutma

## Çalışma Prensibi

Absorpsiyonlu chiller, buhar sıkıştırmalı sistemlerdeki mekanik kompresörün yerine bir termal kompresör (absorber + jeneratör) kullanır. Sıkıştırma işlemi için elektrik yerine ısı enerjisi tüketilir.

### Temel Bileşenler
- **Evaporatör (Evaporator):** Soğutucu akışkan buharlaşarak soğutma etkisi üretir
- **Absorber:** Evaporatörden gelen buhar, güçlü (konsantre) çözelti tarafından absorbe edilir; absorpsiyon ısısı soğutma suyu ile atılır
- **Jeneratör (Generator/Desorber):** Zayıf (seyreltik) çözelti ısıtılarak soğutucu akışkan buharı ayrıştırılır; çözelti yeniden güçlü hale gelir
- **Kondenser:** Jeneratörden gelen soğutucu akışkan buharı yoğuşarak sıvılaşır
- **Çözelti ısı değiştiricisi (Solution Heat Exchanger - SHX):** Jeneratöre giden zayıf çözelti ile dönen güçlü çözelti arasında ısı aktarımı — COP'u %40-60 artırır
- **Çözelti pompası:** Çözeltiyi absorberin düşük basıncından jeneratörün yüksek basıncına pompalar (çok düşük güç)
- **Genleşme vanası:** Soğutucu akışkan ve çözelti basınç düşürücüleri

### LiBr-Su Sistemi (Lityum Bromür - Su)

| Özellik | Değer |
|---------|-------|
| Soğutucu akışkan | Su (H₂O) |
| Absorban | Lityum bromür (LiBr) çözeltisi |
| Çalışma basıncı | Pozitif basınç altında (~0.8-8 kPa, vakuma yakın ama atmosferin altında) |
| Evaporasyon sıcaklığı | 3 - 10°C (donma riski nedeniyle alt sınır ~3°C) |
| Soğutma çıkış suyu | Tipik 6-7°C (minimum ~4°C) |
| Kristalizasyon riski | Var — konsantrasyon ve sıcaklık dengesine dikkat gerekli |
| Uygulama | Konfor soğutma (HVAC), proses soğutma (>3°C) |
| Avantaj | Zehirsiz, kokusuz, yüksek COP (çift etkili) |
| Dezavantaj | Kristalizasyon riski, korozyon, donma sınırlaması |

### NH₃-Su Sistemi (Amonyak - Su)

| Özellik | Değer |
|---------|-------|
| Soğutucu akışkan | Amonyak (NH₃) |
| Absorban | Su (H₂O) |
| Çalışma basıncı | Negatif ve pozitif basınç (2-20 bar) |
| Evaporasyon sıcaklığı | -60°C'ye kadar |
| Soğutma çıkış sıcaklığı | -40°C'ye kadar |
| Kristalizasyon riski | Yok |
| Uygulama | Endüstriyel soğutma, dondurucu depolama, proses soğutma |
| Avantaj | Düşük sıcaklık, kristalizasyon yok |
| Dezavantaj | Zehirli ve yanıcı (NH₃), rektifikasyon kolonu gerekli, düşük COP |

### Tek Etkili, Çift Etkili ve Üç Etkili Karşılaştırma

| Parametre | Tek Etkili (Single Effect) | Çift Etkili (Double Effect) | Üç Etkili (Triple Effect) |
|-----------|----------------------------|-----------------------------|-----------------------------|
| Jeneratör sayısı | 1 | 2 (yüksek ve düşük basınçlı) | 3 (yüksek, orta, düşük basınçlı) |
| Isı kaynağı sıcaklığı | 80 - 120°C | 140 - 180°C | 200 - 230°C |
| Enerji kaynağı | Sıcak su, düşük basınçlı buhar, atık ısı | Orta basınçlı buhar, doğrudan yakma | Yüksek basınçlı buhar, doğrudan yakma |
| COP (LiBr-Su) | 0.65 - 0.75 | 1.0 - 1.4 | 1.4 - 1.7 |
| COP (NH₃-Su) | 0.4 - 0.6 | 0.8 - 1.2 | — |
| Yatırım maliyeti | Düşük | Orta | Yüksek |
| Karmaşıklık | Basit | Orta | Karmaşık |
| Korozyon riski | Düşük | Orta | Yüksek (yüksek sıcaklık) |

## Enerji Dağılımı (Tipik — Çift Etkili LiBr-Su, Tam Yük)

| Enerji Akışı | Oran (%) | Açıklama |
|---------------|----------|----------|
| Jeneratör ısı girdisi | 100 | Buhar, sıcak su veya yakma ısısı |
| Evaporatörde alınan ısı (soğutma etkisi) | 100 - 140 | COP 1.0-1.4 (ısı girdisine oranla) |
| Kondenserde atılan ısı | ~80 - 100 | Soğutucu akışkan yoğuşması |
| Absorberde atılan ısı | ~80 - 110 | Absorpsiyon ısısı |
| Toplam soğutma suyu yükü | ~160 - 210 | Kondenser + absorber (çok yüksek) |
| Elektrik tüketimi | ~3 - 5 | Çözelti pompası, soğutma suyu pompası, kontrol |

Absorpsiyonlu chillerlerde kondensere ve absorbere atılan toplam ısı, buhar sıkıştırmalı sistemlere göre çok daha yüksektir. Bu nedenle soğutma kulesi kapasitesi daha büyük olmalıdır.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Soğuk su giriş sıcaklığı (evaporatör) | °C | 10 - 16 | PT100 sensör |
| Soğuk su çıkış sıcaklığı (evaporatör) | °C | 5 - 9 | PT100 sensör |
| Soğuk su debisi | m³/h | Kapasiteye bağlı | Ultrasonik debimetre |
| Jeneratör ısı kaynağı giriş sıcaklığı | °C | 80 - 200 (tipe göre) | PT100 sensör |
| Jeneratör ısı kaynağı çıkış sıcaklığı | °C | 60 - 160 (tipe göre) | PT100 sensör |
| Jeneratör ısı kaynağı debisi | m³/h veya kg/h | Kapasiteye bağlı | Debimetre / buhar sayacı |
| Soğutma suyu giriş sıcaklığı | °C | 28 - 35 | PT100 sensör |
| Soğutma suyu çıkış sıcaklığı | °C | 33 - 42 | PT100 sensör |
| Toplam elektrik tüketimi | kW | 5 - 50 | Güç analizörü |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| LiBr çözelti konsantrasyonu (güçlü) | % ağırlık | 60 - 66 | Yoğunluk ölçer / refraktometre |
| LiBr çözelti konsantrasyonu (zayıf) | % ağırlık | 55 - 60 | Yoğunluk ölçer / refraktometre |
| Jeneratör sıcaklığı | °C | 80 - 200 | Termokupl |
| Absorber sıcaklığı | °C | 30 - 40 | Termokupl |
| Evaporatör sıcaklığı | °C | 3 - 7 | Termokupl |
| Kondenser sıcaklığı | °C | 35 - 45 | Termokupl |
| Vakum seviyesi (LiBr sistem) | kPa | 0.5 - 8 | Vakum manometresi |
| Soğutma suyu debisi | m³/h | Kapasiteye bağlı | Ultrasonik debimetre |
| İnhibitör konsantrasyonu | ppm | Üretici spesifikasyonuna göre | Kimyasal analiz |
| Kaçak hava (non-condensable) | — | — | Purge ünitesi çalışma süresi |
| Çalışma saati | saat/yıl | 2,000 - 6,000 | Sayaç |

### Nameplate Bilgileri
- Marka ve model (örn. Thermax TD-20A, Broad BDH)
- Nominal soğutma kapasitesi (kW veya ton)
- Çalışma çifti (LiBr-Su veya NH₃-Su)
- Etki sayısı (tek/çift/üç etkili)
- Nominal COP
- Isı kaynağı tipi ve parametreleri (buhar basıncı, sıcak su sıcaklığı)
- Soğutma suyu gereksinimleri (debi, sıcaklık)
- Çözelti şarj miktarı (kg)
- Üretim yılı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Soğuk su giriş sıcaklığı | 12°C | Konfor soğutma varsayımı |
| Soğuk su çıkış sıcaklığı | 7°C | Standart chiller çıkışı |
| Soğutma suyu giriş sıcaklığı | 30°C | Yaz tasarım koşulu |
| Soğutma suyu çıkış sıcaklığı | 37°C | Absorpsiyon sistemi (ΔT daha yüksek) |
| Jeneratör giriş sıcaklığı (sıcak su) | 90°C | Tek etkili varsayımı |
| Jeneratör buhar basıncı | 8 bar | Çift etkili varsayımı |
| COP (tek etkili) | 0.70 | Ortalama tam yük |
| COP (çift etkili) | 1.20 | Ortalama tam yük |
| Elektrik tüketimi | 8 kW / 100 kW soğutma | Pompalar ve kontrol |
| Ekserji verimi | %15 | Termal giriş bazlı ortalama |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa (1 atm) | Standart ölü durum |
| Çalışma saati | 3,000 saat/yıl | Türkiye, ticari soğutma |
| Yük oranı (ortalama) | %60 | Mevsimsel ortalama |

## Performans Tablosu

### Kapasite ve COP Değerleri (Tam Yük, Standart Koşullar — LiBr-Su)

| Kapasite (kW) | Etki | COP | Elektrik (kW) | Ekserji Verimi (%) | Tipik Uygulama | Yaklaşık Fiyat (€) |
|---------------|------|-----|---------------|---------------------|----------------|---------------------|
| 100 - 300 | Tek | 0.65 - 0.72 | 5 - 20 | 10 - 15 | Atık ısı, sıcak su kaynağı | 30,000 - 80,000 |
| 300 - 1,000 | Tek | 0.68 - 0.75 | 15 - 50 | 12 - 18 | Trijenerasyon, atık ısı | 70,000 - 200,000 |
| 300 - 1,000 | Çift | 1.0 - 1.2 | 15 - 50 | 15 - 22 | Buhar kaynaklı, doğrudan yakma | 100,000 - 300,000 |
| 1,000 - 3,000 | Çift | 1.1 - 1.3 | 30 - 120 | 18 - 25 | Endüstriyel, bölgesel soğutma | 250,000 - 700,000 |
| 3,000 - 10,000+ | Çift | 1.2 - 1.4 | 80 - 400 | 20 - 28 | Büyük endüstriyel, kampüs | 600,000 - 2,500,000+ |
| 1,000 - 5,000 | Üç | 1.4 - 1.7 | 40 - 200 | 22 - 28 | Yüksek verim, doğrudan yakma | 500,000 - 1,500,000 |

### Ekserji Verimi Hesabı (Termal Giriş Bazlı)

```
COP_termal = Q_evap / Q_gen

η_exergy = COP_termal / COP_Carnot_abs × 100

COP_Carnot_abs = (T₀ / T_cold - 1) / (1 - T₀ / T_gen)

Burada:
  Q_evap        : Evaporatörde alınan ısı — soğutma kapasitesi (kW)
  Q_gen         : Jeneratöre verilen ısı (kW)
  COP_termal    : Termal COP (—)
  T₀            : Referans çevre sıcaklığı = 25°C (298.15 K)
  T_cold        : Evaporatör soğuk su ortalama sıcaklığı (K)
  T_gen         : Jeneratör ısı kaynağı ortalama sıcaklığı (K)
  COP_Carnot_abs: Tersinir absorpsiyon çevriminin COP değeri (—)
  η_exergy      : Ekserji verimi (%)
```

Örnek hesaplama (çift etkili, 1,000 kW):

```
T_cold = (12 + 7) / 2 + 273.15 = 282.65 K
T_gen  = (170 + 150) / 2 + 273.15 = 433.15 K  (buhar jeneratörü)
T₀     = 298.15 K

COP_Carnot_abs = (298.15 / 282.65 - 1) / (1 - 298.15 / 433.15)
              = 0.0549 / 0.3116 = 0.176
              → 1 / 0.176 = 5.68 (ters Carnot COP)

COP_gerçek = 1.2
η_exergy = 1.2 / 5.68 × 100 = %21.1

Burada:
  Absorpsiyon çevriminde COP_Carnot hesabı buhar sıkıştırmalı sistemden farklıdır.
  Isı girdisi düşük ekserji kalitesindedir; bu nedenle ekserji verimi daha düşüktür.
```

## Kristalizasyon Riski ve Önleme (LiBr-Su Sistemleri)

Kristalizasyon, LiBr çözeltisinin aşırı konsantre hale gelmesi veya çok düşük sıcaklığa ulaşması durumunda meydana gelir. Kristalize olan çözelti borularda tıkanmaya ve sistemin durmasına neden olur.

### Kristalizasyon Nedenleri
- Soğutma suyu sıcaklığının aşırı düşmesi (kış aylarında soğutma kulesi kontrolsüzlüğü)
- Elektrik kesintisi sırasında çözeltinin soğuması
- Çözelti konsantrasyonunun tasarım değerinin üzerine çıkması
- Kaçak hava (non-condensable gas) birikmesi

### Önleme Yöntemleri
- Soğutma suyu minimum sıcaklık kontrolü (tipik >24°C)
- Dilüsyon çevrimi (elektrik kesintisi öncesi otomatik seyreltme)
- Düzenli purge (kaçak hava tahliyesi)
- Çözelti konsantrasyonu izleme ve alarm sistemi
- Kristalizasyon sonrası çözme: Jeneratöre buhar verilerek kademeli ısıtma

## Dikkat Edilecekler

1. **Kristalizasyon riski (LiBr):** Soğutma suyu sıcaklığı kontrolü kritiktir — minimum 24°C altına düşmemeli; kış aylarında soğutma kulesi bypass veya fan kontrolü şarttır
2. **Vakum kaçağı (LiBr):** LiBr sistemi vakum altında çalışır — en küçük hava kaçağı performansı ciddi düşürür; düzenli purge işlemi ve kaçak testi gerekli
3. **Korozyon:** LiBr çözeltisi koroziftir — lityum kromat veya lityum molibdat bazlı inhibitör düzenli kontrol ve takviye edilmeli
4. **Soğutma suyu kapasitesi:** Absorpsiyon sistemlerinde soğutma suyu yükü buhar sıkıştırmalı sistemin ~1.5-2 katıdır — soğutma kulesi buna göre boyutlandırılmalı
5. **Kısmi yük kontrolü:** %30 altında kısmi yükte verim hızla düşer — kristalizasyon riski artar; minimum yük sınırına dikkat edilmeli
6. **NH₃ güvenliği:** Amonyak sistemi kullanılıyorsa gaz dedektörü, havalandırma ve emniyet prosedürleri zorunlu
7. **Enerji kaynağı kalitesi:** Jeneratör giriş sıcaklığı düşerse COP doğrudan düşer — buhar basıncı veya sıcak su sıcaklığı stabil tutulmalı

## İlgili Dosyalar
- Su soğutmalı chiller: `equipment/chiller_water_cooled.md`
- Hava soğutmalı chiller: `equipment/chiller_air_cooled.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Atık ısı geri kazanım çözümleri: `solutions/chiller_waste_heat_recovery.md`
- Trijenerasyon sistemi: `equipment/trigeneration.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 2: Absorption Cooling, Heating, and Refrigeration Equipment
- ASHRAE Handbook — Refrigeration (2022), Chapter 18: Absorption Equipment
- Herold, K.E., Radermacher, R., Klein, S.A. (2016). *Absorption Chillers and Heat Pumps*, CRC Press, 2nd Edition
- Thermax Absorption Chiller Technical Documentation & Selection Guide
- Broad Group — Non-Electric Chiller Technical Manual
- Carrier/York Absorption Chiller Application Guide
- LG Absorption Chiller Engineering Manual
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley
- Ziegler, F. et al. (2009). "State of the art in sorption cooling and heating", *International Journal of Refrigeration*
- ARI Standard 560: Absorption Water-Chilling and Water-Heating Packages
