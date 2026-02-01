---
title: "Buhar Sıkıştırmalı Chiller — Vapor Compression Chiller (Genel)"
category: equipment
equipment_type: chiller
subtype: "Buhar Sıkıştırmalı"
keywords: [buhar sıkıştırma, çevrim, chiller]
related_files: [chiller/equipment/systems_overview.md, chiller/formulas.md, chiller/equipment/refrigerants.md]
use_when: ["Buhar sıkıştırma çevrimi analiz edilirken", "Soğutma prensibi açıklanırken"]
priority: medium
last_updated: 2026-01-31
---
# Buhar Sıkıştırmalı Chiller — Vapor Compression Chiller (Genel)

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Buhar sıkıştırmalı soğutma çevrimi (vapor compression refrigeration cycle)
- Kapasite aralığı: 5 kW - 35,000+ kW (kompresör tipine bağlı)
- Soğutkan akışkan: R-134a, R-410A, R-1234ze(E), R-290, R-717 (NH₃), R-744 (CO₂)
- Soğutma suyu sıcaklığı (CHW — chilled water supply): tipik 6-7°C
- Soğutma suyu dönüş sıcaklığı (CHW return): tipik 12-13°C
- Kondenser suyu giriş (CW supply): tipik 30-32°C (su soğutmalı)
- Kondenser suyu çıkış (CW return): tipik 35-37°C (su soğutmalı)
- COP aralığı: 2.5-7.5 (kompresör tipine ve koşullara bağlı)
- Exergy verimi: %18-45 (kompresör tipi, yük ve koşullara bağlı)
- Yaygın markalar: Carrier, Trane (Ingersoll Rand), York (Johnson Controls), Daikin, Mitsubishi, Bitzer, Danfoss (Turbocor)

## Çalışma Prensibi

Buhar sıkıştırmalı soğutma çevrimi dört ana bileşenden oluşur ve tersinmez (irreversible) bir termodinamik çevrim gerçekleştirir.

### Çevrim Adımları

1. **Evaporatör (Buharlaştırıcı):** Düşük basınç ve sıcaklıkta sıvı soğutkan, soğutulacak ortamdan (CHW) ısı alarak buharlaşır. Bu aşamada soğutucu akışkan faz değiştirir (sıvı → gaz). Evaporatör sıcaklığı tipik olarak 2-5°C'dir.
2. **Kompresör:** Düşük basınçlı soğutkan gazı emer, sıkıştırarak basıncını ve sıcaklığını yükseltir. Bu bileşen chillerın en fazla enerji tüketen elemanıdır. Kompresör çıkış sıcaklığı tipik 60-90°C'dir.
3. **Kondenser (Yoğuşturucu):** Yüksek basınç ve sıcaklıkta gaz halindeki soğutkan, kondenser suyuna (CW) veya havaya ısısını vererek yoğunlaşır (gaz → sıvı). Kondenser sıcaklığı tipik 35-45°C (su soğutmalı), 45-55°C (hava soğutmalı).
4. **Genleşme Vanası (Expansion Valve):** Yüksek basınçlı sıvı soğutkan, kısılarak (throttling) basıncı ve sıcaklığı düşürülür. Bu süreç isentalpik (sabit entalpi) bir süreçtir; termodinamik açıdan iş üretilmez ve exergy yıkılır.

### Carnot COP ve Gerçek COP

Soğutma makinelerinin teorik üst performans sınırı Carnot COP ile belirlenir:

```
COP_Carnot = T_evap / (T_cond - T_evap)

Burada:
  COP_Carnot = Carnot soğutma katsayısı (teorik maksimum)
  T_evap     = evaporatör sıcaklığı [K]
  T_cond     = kondenser sıcaklığı [K]
```

Örnek: T_evap = 5°C (278.15 K), T_cond = 40°C (313.15 K):
COP_Carnot = 278.15 / (313.15 - 278.15) = 278.15 / 35 = 7.95

Gerçek COP her zaman Carnot COP'nin altındadır. Gerçek COP/Carnot COP oranı chillerın "ikinci yasa verimliliğini" (second-law efficiency) yani exergy verimini verir.

```
COP_gercek = Q_evap / W_kompressor

Burada:
  COP_gercek   = gerçek soğutma katsayısı
  Q_evap       = evaporatörde alınan ısı (soğutma kapasitesi) [kW]
  W_kompressor = kompresör elektrik gücü [kW]
```

### Lift ve Yaklaşma (Approach) Kavramları

- **Lift:** Kondenser ve evaporatör sıcaklıkları arasındaki fark. Düşük lift = yüksek COP.
- **Evaporatör yaklaşma (approach):** CHW çıkış sıcaklığı - evaporatör sıcaklığı, tipik 2-4°C
- **Kondenser yaklaşma (approach):** Kondenser sıcaklığı - CW çıkış sıcaklığı, tipik 1-3°C

## Soğutucu Akışkanlar

### ODP ve GWP Değerleri Tablosu

| Soğutkan | Kimyasal Formül | Tip | ODP | GWP (100 yıl) | Güvenlik Sınıfı | Tipik Uygulama |
|----------|----------------|-----|-----|----------------|-----------------|----------------|
| R-134a | CH₂FCF₃ | HFC | 0 | 1430 | A1 | Santrifüj, scroll |
| R-410A | R-32/R-125 (%50/%50) | HFC karışım | 0 | 2088 | A1 | Scroll, vidalı (küçük) |
| R-407C | R-32/R-125/R-134a | HFC karışım | 0 | 1774 | A1 | Scroll, vidalı |
| R-1234ze(E) | CF₃CH=CHF | HFO | 0 | 7 | A2L | Santrifüj (yeni nesil) |
| R-1234yf | CF₃CF=CH₂ | HFO | 0 | 4 | A2L | Otomotiv, küçük chiller |
| R-513A | R-1234yf/R-134a | HFO/HFC karışım | 0 | 631 | A1 | Santrifüj (geçiş dönemi) |
| R-290 | C₃H₈ (propan) | HC (doğal) | 0 | 3 | A3 | Küçük chiller (<50 kW) |
| R-717 | NH₃ (amonyak) | Doğal | 0 | 0 | B2L | Endüstriyel (>500 kW) |
| R-744 | CO₂ | Doğal | 0 | 1 | A1 | Transkritik sistemler |

### F-gaz Yönetmeliği Özeti

- **AB F-gaz Yönetmeliği (EU 517/2014, revize 2024):** HFC tüketimini aşamalı olarak azaltır (phase-down). 2030'a kadar %79, 2050'ye kadar %95 azaltım hedefi.
- **Kigali Değişikliği (Montreal Protokolü, 2016):** Gelişmekte olan ülkelerde (Türkiye dahil) HFC azaltımı 2029'dan itibaren başlar.
- **GWP > 2500:** 2025'ten itibaren AB'de yeni ekipmanlarda yasaklı (R-404A, R-507A)
- **GWP > 750:** 2025'ten itibaren AB'de yeni split klimalar ve paket sistemlerde yasaklı
- **Trend:** Düşük GWP'li HFO soğutkanlar (R-1234ze, R-1234yf) ve doğal soğutkanlar (NH₃, CO₂, propan) giderek yaygınlaşmaktadır.

## Kompresör Tiplerine Göre Kapasite Aralıkları

| Kompresör Tipi | Kapasite Aralığı (kW) | Kapasite (ton) | Tipik COP (Su Soğutmalı) | Tipik COP (Hava Soğutmalı) |
|---------------|----------------------|----------------|--------------------------|---------------------------|
| Scroll | 10-500 | 3-140 | 4.5-6.0 | 2.5-3.5 |
| Vidalı (Screw) | 50-1,500 | 14-430 | 5.0-6.5 | 2.8-3.5 |
| Santrifüj | 300-10,000+ | 85-2,800+ | 6.0-7.5 | — |
| Pistonlu (Reciprocating) | 5-300 | 1.5-85 | 3.5-5.0 | 2.0-3.0 |

> **Not:** 1 ton soğutma = 3.517 kW = 12,000 BTU/h

## Enerji Dağılımı (Tipik Buhar Sıkıştırmalı Chiller Sistemi)
- Kompresör elektrik tüketimi: ~%78-85
- Kondenser pompası / fanı: ~%8-12
- Evaporatör pompası (CHW pompa): ~%5-8
- Kontrol ve yardımcı ekipman: ~%1-2

## Exergy Verimi Kavramı

Chillerlarda exergy verimi, gerçek performansın tersinir (reversible) performansa oranıdır:

```
ψ_chiller = COP_gercek / COP_Carnot

Burada:
  ψ_chiller  = chiller exergy verimi (ikinci yasa verimi)
  COP_gercek = ölçülen / hesaplanan gerçek COP
  COP_Carnot = Carnot COP (teorik maksimum)
```

Daha kesin ifade ile:

```
ψ_chiller = Ex_sogutma / W_kompressor

Ex_sogutma = Q_evap × (T₀/T_CHW - 1)

Burada:
  Ex_sogutma  = soğutma exergysi [kW]
  Q_evap      = evaporatör kapasitesi (soğutma yükü) [kW]
  T₀          = referans (ortam) sıcaklığı = 298.15 K (25°C)
  T_CHW       = soğutulmuş su ortalama sıcaklığı [K]
  W_kompressor = kompresör elektrik gücü [kW]
```

**Örnek hesap:**
- Q_evap = 500 kW, T₀ = 298.15 K, T_CHW = 280 K (7°C), W = 100 kW
- COP = 500/100 = 5.0
- Ex_sogutma = 500 × (298.15/280 - 1) = 500 × 0.0648 = 32.4 kW
- ψ = 32.4 / 100 = 0.324 = %32.4

**Önemli:** Chillerlarda exergy verimi %18-45 aralığındadır. Düşük olmasının temel sebebi, soğutma çıktısının termodinamik "kalitesinin" düşük olmasıdır — 7°C'lik soğutulmuş su, 25°C ortam sıcaklığına çok yakındır ve Carnot faktörü küçüktür.

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kompresör elektrik gücü | kW | 5-5000+ | Güç analizörü (3 faz) |
| CHW giriş sıcaklığı (return) | °C | 11-14 | PT100 veya termokupl |
| CHW çıkış sıcaklığı (supply) | °C | 5-8 | PT100 veya termokupl |
| CHW debisi | m³/h veya l/s | Kapasiteye bağlı | Ultrasonik veya elektromanyetik flowmeter |
| CW giriş sıcaklığı (su soğutmalıda) | °C | 28-35 | PT100 veya termokupl |
| CW çıkış sıcaklığı (su soğutmalıda) | °C | 33-40 | PT100 veya termokupl |

### Opsiyonel (daha detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| CW debisi | m³/h | Kapasiteye bağlı | Ultrasonik flowmeter |
| Evaporatör giriş/çıkış basıncı | bar | 2-5 | Basınç transmiteri |
| Kondenser giriş/çıkış basıncı | bar | 8-18 | Basınç transmiteri |
| Soğutkan akış sıcaklıkları | °C | -5 ile +60 | Yüzey termokupl |
| Kompresör motor akımı | A | Etikete bağlı | Pens ampermetre |
| Hava sıcaklığı (hava soğutmalı) | °C | 25-45 | Termometre |
| Yük oranı (% kapasite) | % | 20-100 | BMS / chiller kontrol paneli |
| Çalışma saati | saat | — | Chiller kontrol paneli |
| Kompresör devri (VSD'li) | RPM | Değişken | Frekans konvertör çıkışı |

### Nameplate Bilgileri
- Marka ve model
- Nominal soğutma kapasitesi (kW veya ton)
- Nominal elektrik gücü (kW)
- Nominal COP / EER / kW/ton
- Soğutkan tipi ve şarj miktarı (kg)
- Maksimum çalışma basıncı (yüksek taraf / düşük taraf) (bar)
- Nominal CHW sıcaklıkları (giriş/çıkış)
- Nominal CW sıcaklıkları (giriş/çıkış)
- Üretim yılı ve seri numarası

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| CHW supply sıcaklığı | 7°C | ARI 550/590 standart koşul |
| CHW return sıcaklığı | 12°C | ΔT = 5°C standart |
| CW giriş sıcaklığı | 30°C | ARI 550/590 standart koşul |
| CW çıkış sıcaklığı | 35°C | ΔT = 5°C standart |
| Ortam sıcaklığı (referans T₀) | 25°C (298.15 K) | Exergy referansı |
| Yük oranı (sezonluk ortalama) | %55 | ASHRAE 90.1 tipik profil |
| Çalışma saati | 2500 saat/yıl | Türkiye (ofis binası, soğutma sezonu) |
| CHW pompası gücü | Kapasitenin %6'sı | Yaklaşık değer |
| CW pompası gücü | Kapasitenin %8'i | Yaklaşık değer |
| Kule fanı gücü | Kapasitenin %4'ü | Yaklaşık değer |
| Soğutkan tipi | R-134a | En yaygın (mevcut stok) |
| Elektrik birim fiyatı | 0.10 €/kWh | Türkiye endüstriyel ortalama (2025) |

## Performans Tablosu (Kompresör Tipine Göre)

| Parametre | Scroll | Vidalı (Screw) | Santrifüj | Pistonlu |
|-----------|--------|----------------|-----------|----------|
| Kapasite (kW) | 10-500 | 50-1,500 | 300-10,000+ | 5-300 |
| Tam yük COP (su soğutmalı) | 4.5-6.0 | 5.0-6.5 | 6.0-7.5 | 3.5-5.0 |
| Tam yük COP (hava soğutmalı) | 2.5-3.5 | 2.8-3.5 | — | 2.0-3.0 |
| IPLV/NPLV (su soğutmalı) | 5.5-7.5 | 6.0-9.0 | 7.0-11.5+ | 4.5-6.0 |
| kW/ton (tam yük, su soğ.) | 0.58-0.78 | 0.54-0.70 | 0.47-0.58 | 0.70-1.00 |
| Exergy verimi (tam yük) | %18-30 | %20-35 | %25-45 | %15-25 |
| Exergy verimi (IPLV koşulları) | %22-35 | %25-40 | %30-45 | %18-28 |
| Kısmi yük performansı | Orta | İyi | Çok iyi (VSD ile) | Kötü-orta |
| Gürültü seviyesi | Düşük | Orta | Düşük-orta | Yüksek |
| Tipik ömür | 15-20 yıl | 20-25 yıl | 25-30+ yıl | 15-20 yıl |
| Tahmini yatırım (€/kW) | 80-200 | 100-250 | 120-350 | 70-180 |

> **Not:** kW/ton = 3.517 / COP. Düşük kW/ton daha yüksek verim demektir.

## Dikkat Edilecekler

1. **Lift etkisi:** Her 1°C lift azalması COP'yi yaklaşık %2-3 artırır. CHW set noktasını yükseltmek ve CW sıcaklığını düşürmek en etkili verim iyileştirmesidir.
2. **Yaklaşma sıcaklıkları:** Evaporatör ve kondenser yaklaşma sıcaklıkları kirlenme (fouling) göstergesidir. Yaklaşma sıcaklığının artması ısı transfer yüzeylerinin temizlenmesi gerektiğini gösterir.
3. **Kısmi yük davranışı:** Chillerlar tam yük yerine çoğunlukla %40-70 yükte çalışır. IPLV/NPLV değeri tam yük COP'den daha önemli bir göstergedir.
4. **Soğutkan seçimi:** F-gaz yönetmelikleri nedeniyle yüksek GWP'li soğutkanlardan (R-134a, R-410A) düşük GWP'li alternatiflere (R-1234ze, R-290, NH₃) geçiş hızlanmaktadır.
5. **Su debisi kontrolü:** Değişken birincil (variable primary) CHW sistemleri sabit debili sistemlere göre pompa enerjisinden %30-50 tasarruf sağlar.
6. **Kondenser suyu sıcaklığı:** Soğutma kulesinde wet-bulb sıcaklığına yaklaşmak chiller COP'yi önemli ölçüde artırır. Kule bakımı ve su arıtması kritiktir.
7. **VSD uygulama:** Santrifüj kompresörlerde VSD, kısmi yüklerde %15-30 enerji tasarrufu sağlar.
8. **Exergy perspektifi:** Düşük chiller exergy verimini iyileştirmenin en etkili yolu lift azaltmadır. Serbest soğutma (free cooling), soğutma kulesi ekonomizörü ve CHW reset stratejileri exergy verimini önemli ölçüde artırır.

## İlgili Dosyalar
- Vidalı chiller: `equipment/chiller_screw.md`
- Santrifüj chiller: `equipment/chiller_centrifugal.md`
- Scroll chiller: `equipment/chiller_scroll.md`
- Absorpsiyon chiller: `equipment/chiller_absorption.md`
- Soğutma kulesi: `equipment/cooling_tower.md`
- Chiller exergy hesaplamaları: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Soğutma sistemi optimizasyonu: `solutions/chiller_optimization.md`
- VSD uygulama: `solutions/chiller_vsd.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, 2024 (Chapters 38-43)
- ASHRAE Standard 90.1 — Energy Standard for Buildings
- ARI Standard 550/590 — Performance Rating of Water-Chilling Packages
- Kotas, T.J. "The Exergy Method of Thermal Plant Analysis", Krieger Publishing, 1995
- Bejan, A., Tsatsaronis, G., Moran, M. "Thermal Design and Optimization", Wiley, 1996
- Stoecker, W.F., Jones, J.W. "Refrigeration and Air Conditioning", McGraw-Hill
- EUROVENT — Chiller Energy Efficiency Certification Programme
- EU F-gas Regulation 517/2014 (revised 2024)
- Kigali Amendment to the Montreal Protocol, 2016
- DOE/FEMP — Best Practices for Chiller Plant Optimization
