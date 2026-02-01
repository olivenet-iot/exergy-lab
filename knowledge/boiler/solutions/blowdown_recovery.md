# Blowdown Isi Geri Kazanimi — Blowdown Heat Recovery

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Kazan blowdown suyu, kazan basincindaki doyma sicakliginda disari atilir. Bu su önemli miktarda termal enerji tasir ve dogrudan kanalizasyona verilmesi hem enerji kaybi hem de cevre kirliligi olusturur.

**Çözüm:** Flash tank ile blowdown suyundan düsük basinçli buhar elde edilmesi ve ardindan isi esanjörü ile kalan sicak suyun besleme suyunu ön isitmasi için kullanilmasi.

**Tipik Tasarruf:** %1-3 (toplam kazan yakit tüketiminin)

**Tipik ROI:** 1-2 yil

## Çalisma Prensibi

Kazan blowdown islemi, kazan suyundaki çözünmüs kati madde (TDS — Total Dissolved Solids) konsantrasyonunu kontrol altinda tutmak için yapilir. Blowdown suyu, kazan çalisma basincinda doyma sicakligindadir ve yüksek entalpi tasir.

### Sürekli Blowdown (Continuous Blowdown)

- Kazan tamburundan (drum) sürekli olarak küçük debide su çekilir
- TDS konsantrasyonunu sabit ve kontrollü tutar
- Otomatik TDS kontrol sistemi ile yönetilir
- Genellikle kazan besleme suyu debisinin %1-4'ü kadardir
- Isi geri kazanimi için en uygun blowdown tipidir (sürekli ve öngörülebilir debi)

### Aralikli Blowdown (Intermittent Blowdown)

- Kazan alt noktasindan (mud drum / alt header) periyodik olarak yapilir
- Dip çamuru, tortu ve çökelmis katilari uzaklastirir
- Genellikle vardiya basinda veya her 4-8 saatte bir, 5-15 saniye süreyle açilir
- Debi ani ve yüksektir, ancak süre kisadir
- Isi geri kazanimi zordur (kesikli akis); genellikle blowdown tankina yönlendirilir ve sogutulur

### Blowdown Isi Geri Kazanim Sistemi Bileşenleri

Tipik bir blowdown isi geri kazanim sistemi iki kademeden olusur:

1. **Flash Tank (Flas Tank):** Yüksek basinçli blowdown suyu düsük basinca açildiginda bir kismi aninda buharlaşir (flash buhar). Bu düsük basinçli buhar, deaeratör beslemesi veya diger düsük basinçli buhar uygulamalari için kullanilabilir.

2. **Isı Eşanjörü (Heat Exchanger):** Flash tank çikisindaki kalan sicak su (hala doyma sicakliginda) bir plakalı veya kabuk-boru tipi esanjörden geçirilerek taze besleme suyunu (makeup water) ön isitir. Esanjör çikisindaki sogutulmus blowdown suyu güvenli bir sekilde kanalizasyona verilebilir (genellikle <40°C).

```
Blowdown Suyu (kazan basinci)
       │
       ▼
  ┌─────────────┐
  │  Flash Tank  │──── Flash Buhar ──→ Deaeratör / LP Header
  │  (düsük P)   │
  └──────┬──────┘
         │ Sicak su (doyma sicakligi, düsük P)
         ▼
  ┌──────────────┐
  │ Isı Esanjörü  │──── Ön isitilmis besleme suyu ──→ Deaeratör / Kazan
  │ (HX)          │
  └──────┬───────┘
         │ Sogutulmus blowdown suyu (<40°C)
         ▼
     Kanalizasyon
```

## Flash Buhar Hesabi

Blowdown suyu flash tanka girdiginde, yüksek basinçtaki doyma sivisinin entalpisi düsük basinçtaki denge kosullarindan fazladir. Bu fazla enerji, suyun bir kisminin buharlasmasi için kullanilir.

### Flash Buhar Yüzdesi Formülü

```
Flash% = (h_blowdown - h_flash_liquid) / h_fg_flash × 100

Burada:
  Flash%          = Buharlaşan kütle yüzdesi (%)
  h_blowdown      = Blowdown suyunun entalpisi, kazan basincinda doyma sivisi (kJ/kg)
  h_flash_liquid  = Flash tank basincinda doyma sivisi entalpisi (kJ/kg)
  h_fg_flash      = Flash tank basincinda buharlaşma gizli isisi (kJ/kg)
```

### Örnek Hesaplama

**Senaryo:** 10 bar(g) kazan basinci, flash tank 1 bar(g) basincinda çalisiyor.

Buhar tablolarindan (IAPWS-IF97):
- h_blowdown = h_f(10 bar_g = 11 bar_abs) = 781 kJ/kg
- h_flash_liquid = h_f(1 bar_g = 2 bar_abs) = 505 kJ/kg
- h_fg_flash = h_fg(2 bar_abs) = 2202 kJ/kg

```
Flash% = (781 - 505) / 2202 × 100
Flash% = 276 / 2202 × 100
Flash% = %12.5
```

Her 1000 kg blowdown suyundan 125 kg düsük basinçli flash buhar elde edilir.

### Kazan Basincina Göre Flash Buhar Oranlari

Asagidaki tablo, farkli kazan basinçlarinda flash tankina 1 bar(g) basincinda açildiginda oluşan flash buhar yüzdelerini gösterir:

| Kazan Basinci (bar_g) | h_f (kJ/kg) | Flash% (→ 1 bar_g) | Flash Buhar Sicakligi |
|------------------------|-------------|---------------------|-----------------------|
| 5                      | 671         | %7.5                | 120°C                 |
| 8                      | 743         | %10.8               | 120°C                 |
| 10                     | 781         | %12.5               | 120°C                 |
| 13                     | 828         | %14.7               | 120°C                 |
| 15                     | 853         | %15.8               | 120°C                 |
| 20                     | 909         | %18.3               | 120°C                 |
| 25                     | 962         | %20.8               | 120°C                 |

## Blowdown Orani vs Kayip

Blowdown orani arttikça kazan enerji kaybi dogrudan artar. Asagidaki tablo, 10 bar(g) kazan basincinda farkli blowdown oranlarinin yakit kaybi üzerindeki etkisini gösterir (kazan verimi %90, isi geri kazanimi yok):

| Blowdown Orani (%) | Blowdown Isı Kaybı (%) | Yıllık Yakıt Kaybı (€/yıl)* | Geri Kazanımla Tasarruf (€/yıl)** |
|---------------------|------------------------|------------------------------|-----------------------------------|
| 1                   | %0.3                   | €1,500                       | €1,100                            |
| 2                   | %0.7                   | €3,000                       | €2,200                            |
| 3                   | %1.0                   | €4,500                       | €3,300                            |
| 5                   | %1.7                   | €7,500                       | €5,500                            |
| 8                   | %2.7                   | €12,000                      | €8,800                            |
| 10                  | %3.4                   | €15,000                      | €11,000                           |

\* 5 t/h kazan, 5000 saat/yil, dogalgaz €0.35/m³ bazinda
\** Flash tank + esanjör ile tipik %73 geri kazanim orani

## Otomatik vs Manuel Blowdown Kontrolü

| Özellik | Manuel Blowdown | Otomatik Blowdown |
|---------|-----------------|-------------------|
| Kontrol yöntemi | Operatör TDS ölçer, vanayı açar/kapar | TDS sensörü + kontrol vanasi otomatik |
| Blowdown orani | Genellikle yüksek (%5-10) — güvenlik marji | Optimize edilmis (%2-4) |
| Yakit tasarrufu | Referans | %1-3 ek tasarruf (azaltilmis blowdown) |
| TDS kontrolü | Degisken, dalgiç TDS ölçüm araliklarinda | Sürekli, hassas kontrol |
| Yatirim maliyeti | Düsük (sadece vana) | €5,000-15,000 (sensör + kontrol vanasi + PLC) |
| ROI | — | 6-18 ay |
| Önerilen durum | Küçük kazanlar (<2 t/h) | Tüm kazanlar >2 t/h |

Otomatik blowdown kontrolü, TDS seviyesini sürekli ölçerek blowdown debisini minimum düzeyde tutar. Bu sayede hem blowdown isi kaybi azalir hem de su ve kimyasal tüketimi düser.

## Uygulanabilirlik Kriterleri

| Kriter | Minimum | İdeal |
|--------|---------|-------|
| Kazan kapasitesi | 2 t/h | >5 t/h |
| Kazan basinci | 5 bar(g) | >10 bar(g) |
| Çalisma saati | 3000 saat/yil | >5000 saat/yil |
| Blowdown orani | %2 | >%5 |
| Mevcut geri kazanim | Yok | Yok |
| Besleme suyu sertligi | >50 ppm CaCO₃ | >150 ppm CaCO₃ |

**Not:** Blowdown orani yüksek olan tesislerde (kötü su kalitesi, yetersiz aritma) isi geri kazanim yatirimi çok daha hizli geri döner. Ancak öncelikli olarak besleme suyu aritma kalitesinin iyilestirilmesi degerlendirmelidir — blowdown oranini düsürmek, geri kazanimdan daha etkili bir tasarruf yöntemidir.

## Yatirim Maliyeti

| Kazan Kapasitesi (t/h) | Flash Tank | Isı Esanjörü | Boru/Vana/Montaj | Toplam Yatirim |
|-------------------------|-----------|--------------|------------------|----------------|
| 2-5                     | €2,000-4,000 | €1,500-3,000 | €1,000-2,000  | €4,500-9,000   |
| 5-10                    | €3,000-6,000 | €2,500-5,000 | €1,500-3,000  | €7,000-14,000  |
| 10-20                   | €5,000-8,000 | €4,000-7,000 | €2,000-4,000  | €11,000-19,000 |
| 20-50                   | €7,000-12,000 | €6,000-10,000 | €3,000-6,000 | €16,000-28,000 |

Otomatik TDS kontrol sistemi eklenmesi durumunda toplam maliyete €5,000-15,000 ilave edilmelidir.

## ROI Hesabi

### Formül

```
Geri kazanilan isi (kW):
Q_recovery = m_bd × [(Flash% / 100) × h_fg_flash + (1 - Flash% / 100) × (h_flash_liquid - h_makeup)] × η_HX

Basitleştirilmiş formül:
Q_recovery ≈ m_bd × (h_blowdown - h_makeup) × η_system

Burada:
  m_bd       = Blowdown debisi (kg/s)
  h_blowdown = Kazan basincinda doyma sivisi entalpisi (kJ/kg)
  h_makeup   = Taze su (makeup) entalpisi, tipik 15°C → 63 kJ/kg
  η_system   = Sistem geri kazanim verimi, tipik 0.70-0.80
  Flash%     = Flash buhar yüzdesi (%)
  h_fg_flash = Flash basincinda buharlaşma gizli isisi (kJ/kg)
  h_flash_liquid = Flash basincinda doyma sivisi entalpisi (kJ/kg)
  η_HX       = Esanjör verimi, tipik 0.80-0.90

Yillik parasal tasarruf (€/yil):
Savings = Q_recovery × 3600 × çalisma_saati / (LHV_yakit × η_kazan) × yakit_birim_fiyati

Geri ödeme süresi:
ROI_yil = Toplam_yatirim / Savings
```

### Örnek Hesap

**Senaryo:** 10 t/h buhar kazani, 10 bar(g), %3 blowdown, 5000 saat/yil, dogalgaz

```
Blowdown debisi:
  m_bd = 10,000 kg/h × 0.03 = 300 kg/h = 0.083 kg/s

Blowdown entalpisi (10 bar_g):
  h_blowdown = 781 kJ/kg

Taze su entalpisi (15°C):
  h_makeup = 63 kJ/kg

Geri kazanilabilir isi:
  Q_recovery = 0.083 × (781 - 63) × 0.75 = 44.7 kW

Yillik tasarruf:
  E_saved = 44.7 × 3600 × 5000 = 804,600,000 kJ/yil = 804.6 GJ/yil

Dogalgaz tasarrufu:
  V_gas = 804,600,000 / (36,000 × 0.90) = 24,833 m³/yil

Parasal tasarruf:
  Savings = 24,833 × 0.35 = €8,692/yil

Yatirim (10 t/h kazan):
  Toplam = €12,000 (flash tank + HX + montaj)

Geri ödeme süresi:
  ROI = 12,000 / 8,692 = 1.38 yil
```

## Uygulama Adimlari

1. **Mevcut durum tespiti:** Kazan blowdown oranini ölç veya hesapla (TDS ölçümü ile)
2. **Su kalitesi analizi:** Besleme suyu ve kazan suyu TDS, sertlik, pH degerlerini belirle
3. **Blowdown optimizasyonu:** Önce blowdown oranini minimize et (su aritma iyilestirmesi)
4. **Isi geri kazanim potansiyeli hesapla:** Yukaridaki formüllerle yillik tasarrufu hesapla
5. **Sistem tasarimi:** Flash tank basincini belirle (deaeratör veya LP header basincina uygun)
6. **Esanjör boyutlandirma:** Blowdown debisi ve sicaklik farki baz alinarak LMTD yöntemiyle
7. **Boru güzergahi planlama:** Kazan → flash tank → esanjör → kanalizasyon hatti
8. **Teklif toplama:** Minimum 3 tedarikçiden teklif al (paket sistem veya ayri bilesenler)
9. **Kurulum:** Tipik kurulum süresi 2-5 gün (kazan durdurma gerektirebilir)
10. **Devreye alma:** Flash tank basinci, esanjör performansi, blowdown sicakligi dogrulama
11. **Performans izleme:** Ilk 3 ay boyunca haftalik sicaklik ve debi ölçümleri ile dogrulama

## Riskler ve Dikkat Edilecekler

| Risk | Açiklama | Önlem |
|------|----------|-------|
| Korozyon | Blowdown suyu yüksek TDS içerir, esanjörde korozyon | Paslanmaz çelik (SS316) esanjör kullan |
| Kireçlenme (scaling) | Yüksek sertlik esanjörde kireç birikimi olusturur | Düzenli temizlik, otomatik blowdown ile TDS kontrol |
| Flash buhar basinci dalgalanmasi | Degisken blowdown debisi flash tank basincini etkiler | Uygun boyutlu flash tank, basinci regülatörü |
| Su darbesi (water hammer) | Ani blowdown açilmasinda boru hattinda darbe | Yavas açilan vanalar, uygun boru destekleri |
| Kanalizasyon sicakligi | Sogutulmamis blowdown kanalizasyona zarar verebilir | Esanjör çikisini <40°C olacak sekilde boyutla |
| Geri basinç | Flash tank basinci kazan blowdown debisini etkileyebilir | Blowdown hattinda çek vana ve basinci kontrol |
| Legionella | Düsük sicaklikta duran sularda bakteri üremesi | Esanjör çikis suyunu >60°C tut veya sürekli sirkülasyon |
| Yetersiz blowdown | Isi geri kazanimi için blowdown arttirilmasi yanlis uygulamadir | Blowdown orani su kalitesine göre belirlenmeli, tasarrufa göre degil |

## Tedarikçi ve Ekipman Örnekleri

| Marka | Ürün | Özellik |
|-------|------|---------|
| Spirax Sarco | BRV2S Flash Vessel + Heat Exchanger | Entegre paket sistem, otomatik kontrol |
| Armstrong | Blowdown Heat Recovery System | Modüler tasarim, farkli kapasiteler |
| TLV | Flash Tank + SC serisi esanjör | Japon mühendisligi, yüksek güvenilirlik |
| Alfa Laval | CB serisi plakalı esanjör | Yüksek verimli, kompakt |
| Gestra (Flowserve) | BK serisi blowdown sistemi | Alman kalitesi, endüstriyel standart |

## Ilgili Dosyalar

- Buhar sistemleri genel bakis: `equipment/steam_systems_overview.md`
- Kazan yakitlari: `equipment/boiler_fuels.md`
- Besleme suyu aritma: `solutions/boiler_feedwater_treatment.md`
- Ekonomizer optimizasyonu: `solutions/boiler_economizer.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Kazan ekserji hesaplamalari: `formulas/boiler_exergy.md`
- Flash buhar geri kazanimi: `solutions/flash_steam_recovery.md`
- Kondensat geri dönüsü: `solutions/condensate_return.md`

## Referanslar

- Spirax Sarco, "The Steam and Condensate Loop," Technical Reference Guide — Blowdown & Heat Recovery Chapter
- U.S. DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition — Tip Sheet #9: Recover Heat from Boiler Blowdown
- ASME PTC 4 (2013), "Fired Steam Generators — Performance Test Codes"
- Kotas, T.J. (1985), "The Exergy Method of Thermal Plant Analysis," Butterworths (Reprinted by Krieger, 1995)
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996), "Thermal Design and Optimization," Wiley
- IAPWS-IF97, International Association for the Properties of Water and Steam — Buhar Tablolari
- Rosen, M.A., Dincer, I. (1999), "Exergy Analysis of Waste Emissions," Int. J. Energy Research
- EN 12953, Shell Boilers (Alev Borulu Kazanlar) — Blowdown Requirements
- ABMA (American Boiler Manufacturers Association), "Boiler Water Limits and Steam Purity Recommendations"
