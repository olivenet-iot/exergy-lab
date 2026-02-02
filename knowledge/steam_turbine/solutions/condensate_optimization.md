---
title: "Kondensat ve Besleme Suyu Optimizasyonu — Condensate & Feedwater Optimization"
category: solutions
equipment_type: steam_turbine
keywords: [kondensat sistemi, condensate system, deaerator, feedwater heating, regenerative heating, flash tank, kondensat geri dönüş, blowdown ısı geri kazanım, su arıtma]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/solutions/efficiency_improvement.md, steam_turbine/solutions/maintenance.md, boiler/solutions/condensate_return.md, boiler/solutions/blowdown_recovery.md, boiler/solutions/economizer.md, factory/cross_equipment.md]
use_when: ["Kondensat sistemi kayıpları değerlendirilirken", "Feedwater heating optimizasyonu yapılırken", "Deaerator performansı analiz edilirken", "Buhar çevriminin termal verimi artırılırken"]
priority: medium
last_updated: 2026-01-31
---
# Kondensat ve Besleme Suyu Optimizasyonu — Condensate & Feedwater Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Buhar türbini CHP sistemlerinde kondensat kaybı, yetersiz feedwater heating ve deaerator verimsizlikleri çevrim verimini %3-10 düşürür. Kondensat geri dönüş oranının düşük olması hem yakıt hem su hem kimyasal maliyetini artırır. Feedwater sıcaklığının düşük olması kazan ve çevrim verimini olumsuz etkiler.

**Çözüm:** Kondensat geri dönüş oranını artırma, deaerator optimizasyonu, regenerative feedwater heating (türbin kademelerinden buhar çekişi ile), flash tank uygulaması, blowdown ısı geri kazanımı ve su arıtma iyileştirmesi ile çevrim verimi ve exergy verimi artırılır.

**Tipik Tasarruf:** %3-8 yakıt tasarrufu + %10-30 su/kimyasal tasarrufu
**Tipik ROI:** 0.5-3 yıl

## 1. Kondensat Sistemi Genel Bakış — Condensate System Overview

### 1.1 Kondensat Akış Döngüsü

```
Buhar türbini çevriminde kondensat akışı:

Kazan → HP Buhar → Türbin → Çıkış Buhar → Proses/Kondenser
                                    ↓
                              Kondensat
                                    ↓
                        Kondensat Toplama Tankı
                                    ↓
                           Kondensat Pompası
                                    ↓
                     LP Feedwater Heater (opsiyonel)
                                    ↓
                             Deaerator
                                    ↓
                        Besleme Suyu Pompası
                                    ↓
                     HP Feedwater Heater (opsiyonel)
                                    ↓
                            Ekonomizer
                                    ↓
                              Kazan (drum)
```

### 1.2 Kondensat Kayıp Noktaları

| Kayıp Noktası | Tipik Kayıp [%] | Kayıp Türü | Geri Kazanım Potansiyeli |
|---------------|-----------------|------------|--------------------------|
| Proses doğrudan enjeksiyon | 5-30 | Kütle kaybı (geri dönüşsüz) | Düşük (proses kısıtı) |
| Arızalı buhar kapanları (steam traps) | 3-10 | Canlı buhar kaçağı | Yüksek — bakım ile |
| Kondensat deşarj (kanalizasyona) | 5-20 | Sıcak su kaybı | Yüksek — geri dönüş hattı |
| Flash buhar kaybı (açık tank) | 2-8 | Buhar enerjisi kaybı | Yüksek — flash tank |
| Kondensat hattı ısı kaybı | 1-3 | Isı kaybı (yetersiz yalıtım) | Orta — izolasyon |
| Blowdown deşarjı | 2-5 | Sıcak su + kimyasal kayıp | Yüksek — ısı geri kazanım |

## 2. Kondensat Geri Dönüş Oranı Artırma

### 2.1 Geri Dönüş Oranı ve Enerji Etkisi

```
Kondensat geri dönüş oranı artışının yakıt tasarrufuna etkisi:

Her %10 geri dönüş artışı ≈ %1-2 yakıt tasarrufu

Detaylı hesap:
ΔQ̇_tasarruf = Δṁ_kondensat × c_p × (T_kondensat - T_taze_su)  [kW]

Burada:
- Δṁ_kondensat = Ek geri dönen kondensat debisi [kg/s]
- c_p = 4.18 kJ/(kg·K)
- T_kondensat = Geri dönen kondensat sıcaklığı [°C] (tipik 80-95°C)
- T_taze_su = Şebeke suyu sıcaklığı [°C] (tipik 10-15°C)

Yakıt tasarrufu:
ΔYakıt = ΔQ̇_tasarruf × t_çalışma × 3,600 / (LHV × η_kazan)  [m³/yıl veya kg/yıl]
```

### 2.2 Geri Dönüş Artırma Yöntemleri

| Yöntem | Açıklama | Maliyet (€) | Geri Dönüş Artışı [%] |
|--------|----------|-------------|----------------------|
| Buhar kapanı bakımı/değişimi | Arızalı kapanları tespit et ve değiştir | 500-5,000 | +5-15 |
| Kondensat boru hattı döşeme | Eksik hatları tamamla | 5,000-30,000 | +10-30 |
| Kondensat pompası kurulumu | Yerçekimi dönüşü yetersiz ise | 2,000-10,000 | +5-15 |
| Basınçlı kondensat dönüş sistemi | Yüksek basınçlı kondensat geri dönüşü | 5,000-20,000 | +5-20 |
| Kondensat polisher (arıtma) | Kontamine kondensatı arıtarak geri döndür | 8,000-25,000 | +10-25 |
| Kapalı kondensat devre | Açık tankı kapalı sisteme çevir | 3,000-15,000 | +3-8 (flash kayıp azaltma) |

Kondensat geri dönüşü hakkında detaylı bilgi için: `boiler/solutions/condensate_return.md`

## 3. Deaerator Optimizasyonu — Deaerator Optimization

### 3.1 Deaerator İşlevi ve Önemi

Deaerator (gaz giderici), besleme suyundaki çözünmüş oksijen (O₂) ve karbondioksit (CO₂) gazlarını uzaklaştırır. Yetersiz deaerasyon kazan ve kondensat hattı korozyonuna yol açar.

```
Deaerator prensipleri:
- Besleme suyu doyma sıcaklığına kadar ısıtılır
- Doyma sıcaklığında O₂ çözünürlüğü ≈ 0 (Henry yasası)
- Tipik deaerator basıncı: 0.2-1.5 bar(g)
- Tipik deaerator sıcaklığı: 104-127°C

Çıkış suyu kalitesi hedefi:
- O₂ < 7 ppb (ASME/ABMA önerisi)
- CO₂ ≈ 0 ppm
```

### 3.2 Deaerator Performans Sorunları ve Çözümleri

| Sorun | Belirti | Sebep | Çözüm |
|-------|---------|-------|-------|
| Yetersiz gaz giderimi (O₂ > 20 ppb) | Kondensat hattı korozyonu, kırmızı kondensat | Düşük buhar basıncı, aşırı taze su girişi | Buhar basıncını artır, taze su oranını azalt |
| Deaerator sıcaklığı düşük | Düşük besleme suyu sıcaklığı | Yetersiz ısıtma buharı | Buhar vanasını kontrol et, kaçak kontrol |
| Aşırı buhar tüketimi (venting) | Yüksek yakıt maliyeti | Vent vanası fazla açık | Vent miktarını optimize et (min O₂ hedefine göre) |
| Su seviye dalgalanması | Besleme pompası kavitasyonu riski | Kontrol sorunu, ani yük değişimi | Seviye kontrolü kalibre et, depolama hacmi artır |

### 3.3 Deaerator Buhar Kaynağı Optimizasyonu

```
Deaerator ısıtma buharı kaynağı seçenekleri (verimlilik sırasına göre):

1. Türbin çekiş buharı (extraction steam) — EN VERİMLİ
   - Buhar türbinden iş çıkardıktan sonra deaeratöre gelir
   - Exergy açısından optimum (buharın iş potansiyeli kullanılmış)
   - Tipik çekiş basıncı: 1-3 bar(g)

2. Flash buhar (flash tank'tan)
   - Yüksek basınçlı kondensat flash tankından çıkan buhar
   - Ücretsiz enerji — zaten mevcut, sadece yönlendirme gerekli
   - Exergy kalitesi düşük ama uygun seviyede

3. Düşük basınçlı buhar kolektörü
   - LP header'dan alınan buhar
   - Proses ile rekabet edebilir

4. PRV ile yüksek basınçtan düşürme — EN VERİMSİZ
   - HP buharın iş potansiyeli (exergy) boşa harcanır
   - Mümkünse kaçınılmalı (türbinden çekiş tercih et)

Exergy karşılaştırma (10 bar, 200°C buharı 1.5 bar deaeratöre vermek):
- Türbin çekişi ile: Exergy kaybı ≈ 50-80 kJ/kg (iş çıkarılmış)
- PRV ile: Exergy kaybı ≈ 200-300 kJ/kg (tüm iş potansiyeli kayıp)
```

## 4. Feedwater Heating — Regenerative Isıtma

### 4.1 Regenerative Feedwater Heating Prensibi

Türbin kademelerinden buhar çekerek besleme suyunu kademeli olarak ısıtma, Rankine çevriminin verimini artırır.

```
Regenerative heating ile çevrim verimi artışı:

Her feedwater heater ile:
- Besleme suyu sıcaklığı artar → Kazan yakıt tüketimi azalır
- Çevrim termal verimi artar: Δη_th ≈ %1-3 / heater

Optimal feedwater heater sayısı:
- Küçük endüstriyel (<5 MW): 0-1 heater
- Orta endüstriyel (5-20 MW): 1-3 heater
- Büyük endüstriyel (20-100 MW): 3-5 heater
- Santral tipi (>100 MW): 6-8 heater

Heater sayısı arttıkça marjinal fayda azalır:
1. heater: +%2.5-3.5 verim
2. heater: +%1.5-2.5 ek verim
3. heater: +%1.0-1.5 ek verim
4. heater: +%0.5-1.0 ek verim
```

### 4.2 Feedwater Heater Tipleri

| Tip | Açıklama | Avantaj | Dezavantaj | Uygulama |
|-----|----------|---------|------------|----------|
| Open (karışımlı) — Deaerator | Buhar doğrudan suyla karışır | Basit, ucuz, gaz giderimi | Basınç eşleşmesi gerekli | Her çevrimde var |
| Closed (yüzey tipi) — Shell & tube | Buhar ve su ayrı, eşanjörde ısı transferi | Basınç bağımsız, esnek | Daha pahalı, fouling riski | LP ve HP heaters |

### 4.3 Feedwater Heater Performans Metrikleri

```
Terminal Temperature Difference (TTD):
TTD = T_doyma(P_çekiş) - T_su_çıkış  [°C]
Tasarım TTD: 2-5°C
Bozulmuş TTD: > 8°C → Fouling/tube kaçağı şüphesi

Drain Cooler Approach (DCA):
DCA = T_dren_çıkış - T_su_giriş  [°C]
Tasarım DCA: 5-10°C
Bozulmuş DCA: > 15°C → Dren seviye kontrolü sorunu

Heater düşüş (degradation) etkisi:
- TTD her 1°C artışı ≈ %0.1-0.2 çevrim verimi kaybı
- Heater bypass edilirse: %1-3 çevrim verimi kaybı
```

### 4.4 Endüstriyel Uygulama Örneği

```
Senaryo: 10 MW back-pressure türbin, feedwater heater YOK
Mevcut:
- Deaerator çıkışı: 105°C (0.2 bar(g))
- Kazan giriş (ekonomizer öncesi): 105°C
- Kazan basıncı: 40 bar

Önerilen: 1 adet closed LP feedwater heater
- Türbin çekiş buharı: 3 bar(g), ~150°C doymuş
- FW heater çıkış sıcaklığı: 130°C
- ΔT besleme suyu: 130 - 105 = 25°C

Yakıt tasarrufu:
ΔQ̇ = ṁ_fw × c_p × ΔT = 12 kg/s × 4.18 × 25 = 1,254 kW
Yıllık yakıt tasarrufu = 1,254 × 7,000 × 3.6 / (36,000 × 0.88) = 997,636 kWh/yıl
Doğalgaz: 997,636 / 10 = 99,764 m³/yıl
Maliyet tasarrufu: 99,764 × 0.35 = €34,917/yıl

FW heater yatırımı: ~€40,000 (küçük shell & tube eşanjör + boru)
SPP: 40,000 / 34,917 = 1.15 yıl

Not: Türbinden çekilen buhar elektrik üretimini azaltır.
Net fayda: Yakıt tasarrufu - Elektrik kaybı = Net pozitif (%60-80 net fayda)
```

## 5. Flash Tank Uygulaması — Flash Tank Application

### 5.1 Flash Tank Sistemi

Yüksek basınçlı kondensat bir flash tanka yönlendirildiğinde, basınç düşüşü ile bir kısım kondensat buharlaşır (flash steam). Bu flash buhar değerli enerji taşır ve geri kazanılmalıdır.

```
Flash buhar oranı hesabı:
x_flash = (h_f(P_yüksek) - h_f(P_düşük)) / h_fg(P_düşük)

Örnek:
P_yüksek = 10 bar → h_f = 763 kJ/kg
P_düşük = 1.5 bar → h_f = 467 kJ/kg, h_fg = 2,226 kJ/kg
x_flash = (763 - 467) / 2,226 = %13.3

10 ton/h kondensat için:
Flash buhar debisi = 10 × 0.133 = 1.33 ton/h
Flash buhar enerji içeriği = 1.33 × 2,693 / 3,600 = 995 kW
```

### 5.2 Flash Buhar Kullanım Alanları

| Kullanım | Açıklama | Verimlilik |
|----------|----------|-----------|
| Deaerator beslemesi | Flash buhar doğrudan deaeratöre verilir | Yüksek — hem ısıtma hem gaz giderimi |
| Düşük basınçlı proses | LP buhar ihtiyacını karşılamak | Yüksek — proses kullanımı |
| Besleme suyu ön ısıtma | FW heater'da ısı kaynağı olarak | Orta — ek eşanjör gerekli |
| Bina/tesis ısıtma | Düşük sıcaklık ısıtma | Orta — mevsimsel |

### 5.3 Çok Kademeli Flash Sistemi

```
Çok kademeli flash (multi-stage flash recovery):
Yüksek basınçlı kondensat → Flash Tank 1 (orta basınç) → Flash Tank 2 (düşük basınç)

Her kademe buhar kalitesini optimize eder:
- 1. kademe flash buharı: MP kolektörüne
- 2. kademe flash buharı: LP kolektörüne veya deaeratöre

Yatırım: €5,000-15,000 / flash tank
SPP: 0.5-2 yıl (kondensat debisine bağlı)
```

## 6. Su Arıtma Optimizasyonu — Water Treatment

### 6.1 Besleme Suyu Kalite Gereksinimleri

| Parametre | Kazan Basıncı <20 bar | Kazan Basıncı 20-40 bar | Kazan Basıncı >40 bar |
|-----------|-----------------------|-------------------------|-----------------------|
| TDS [ppm] | <3,500 | <2,500 | <500 |
| Sertlik [ppm CaCO₃] | <2.0 | <0.5 | ~0 |
| O₂ [ppb] | <20 | <7 | <7 |
| pH | 8.5-9.5 | 9.0-9.5 | 9.0-9.5 |
| Silika [ppm SiO₂] | <150 | <30 | <5 |
| İletkenlik [µS/cm] | <7,000 | <5,000 | <1,000 |

### 6.2 Arıtma Sistemi ve Maliyet

| Arıtma Teknolojisi | Uygulama | Yatırım (€) | İşletme Maliyeti (€/m³) |
|---------------------|----------|-------------|------------------------|
| Yumuşatma (softening) | Düşük basınçlı kazanlar (<20 bar) | 5,000-15,000 | 0.3-0.8 |
| RO (reverse osmosis) | Orta-yüksek basınçlı kazanlar | 15,000-50,000 | 0.5-1.5 |
| DM (demineralization) — iyon değişim | Yüksek basınçlı kazanlar (>40 bar) | 20,000-80,000 | 1.0-3.0 |
| Mixed-bed polisher | Ultra saf su gereksinimi | 10,000-30,000 | 0.5-2.0 |
| Kondensat polisher | Kontamine kondensat arıtma | 8,000-25,000 | 0.5-1.5 |

### 6.3 Kondensat Geri Dönüşünün Su Arıtma Maliyetine Etkisi

```
Kondensat geri dönüş oranı arttıkça:
- Taze su arıtma ihtiyacı azalır (kondensat zaten arıtılmış)
- Kimyasal tüketim azalır
- Blowdown oranı azalır (düşük TDS)

Hesap:
Arıtma_tasarrufu = Δṁ_kondensat × (c_arıtma + c_su + c_atıksu)  [€/saat]

Burada:
c_arıtma = Su arıtma kimyasal maliyeti [€/m³] (tipik 0.5-2.0)
c_su = Şebeke/kuyu suyu maliyeti [€/m³] (tipik 1.5-4.0)
c_atıksu = Atıksu deşarj bedeli [€/m³] (tipik 1.0-3.0)
```

## 7. Blowdown Isı Geri Kazanımı — Blowdown Heat Recovery

### 7.1 Blowdown Enerji İçeriği

```
Blowdown oranı: %2-8 (kazan basıncı ve su kalitesine bağlı)
Blowdown sıcaklığı: Kazan doyma sıcaklığı (40 bar → ~250°C)

Enerji geri kazanım potansiyeli:
- Flash buhar geri kazanımı: Blowdown enerjisinin %30-50'si
- Isı eşanjörü ile taze su ön ısıtma: Enerjinin %40-60'ı

Blowdown ısı geri kazanım sistemi:
1. Blowdown → Flash tank → Flash buhar → Deaerator/LP header
2. Flash tank kondensat → Isı eşanjörü → Taze su ön ısıtma
3. Soğumuş blowdown → Drain

Yatırım: €5,000-20,000
SPP: 0.5-2 yıl
```

Blowdown geri kazanımı hakkında detaylı bilgi: `boiler/solutions/blowdown_recovery.md`

### 7.2 Blowdown Oranı Optimizasyonu

| Blowdown Oranı [%] | Değerlendirme | Aksiyon |
|---------------------|--------------|--------|
| <2 | Mükemmel (kondensat geri dönüşü yüksek) | İzle |
| 2-4 | İyi | Su kalitesini kontrol et |
| 4-6 | Orta | Kondensat geri dönüşünü artır |
| 6-8 | Yüksek | Su arıtma sistemini iyileştir |
| >8 | Aşırı | Acil su kalitesi analizi yap |

## 8. Toplam Kondensat Sistemi Optimizasyonu — Özet ROI

| İyileştirme | Yatırım (€) | Yıllık Tasarruf (€)* | SPP (yıl) |
|-------------|-------------|----------------------|-----------|
| Buhar kapanı bakımı/değişimi | 2,000-10,000 | 5,000-30,000 | 0.2-1.0 |
| Kondensat geri dönüş hattı | 5,000-30,000 | 10,000-60,000 | 0.5-2.0 |
| Flash tank (kondensat) | 3,000-12,000 | 5,000-25,000 | 0.5-1.5 |
| Deaerator buhar kaynağı değişikliği | 5,000-20,000 | 8,000-30,000 | 0.5-1.5 |
| LP feedwater heater | 20,000-60,000 | 15,000-50,000 | 1.0-2.5 |
| Blowdown ısı geri kazanım | 5,000-20,000 | 5,000-20,000 | 0.5-2.0 |
| Kondensat polisher | 8,000-25,000 | 5,000-20,000 | 1.0-3.0 |
| Su arıtma yükseltme | 15,000-50,000 | 10,000-30,000 | 1.0-3.0 |

*5 t/h buhar, 7,000 h/yıl, doğalgaz 0.35 €/m³ bazında tahmini değerler

## 9. Exergy Perspektifi — Kondensat Sistemi

```
Kondensat sistemi exergy analizi:

Kondensat sıcaklığının exergy içeriği:
ex_kondensat = c_p × [(T_kond - T₀) - T₀ × ln(T_kond/T₀)]  [kJ/kg]

Örnek değerler (T₀ = 25°C = 298.15 K):
| T_kondensat [°C] | ex [kJ/kg] | Enerji [kJ/kg] | Exergy/Enerji [%] |
|-------------------|-----------|----------------|-------------------|
| 60                | 5.8       | 146            | 4.0               |
| 80                | 14.2      | 230            | 6.2               |
| 95                | 22.1      | 293            | 7.5               |
| 120               | 41.5      | 397            | 10.5              |
| 150               | 70.0      | 523            | 13.4              |

Not: Kondensat exergy içeriği enerji içeriğine göre düşüktür
(düşük sıcaklık = düşük exergy kalitesi). Ancak miktar büyük
olduğunda toplam exergy kaybı önemlidir.

PRV ile basınç düşürme exergy yıkımı:
Ėx_PRV_yıkım = ṁ × T₀ × (s_çıkış - s_giriş)  [kW]
→ Bu exergy, türbin ile çalışmaya dönüştürülebilirdi!
```

## 10. Uygulama Adımları

### 10.1 Mevcut Durum Tespiti
1. Tüm kondensat kaynaklarını ve deşarj noktalarını haritalandır
2. Kondensat geri dönüş oranını ölç (veya hesapla)
3. Buhar kapanı denetimi yap (ultrasonik + sıcaklık)
4. Deaerator performansını doğrula (O₂ ölçümü)
5. Besleme suyu sıcaklık profilini kaydet
6. Blowdown oranını belirle

### 10.2 İyileştirme Önceliklendirme
1. **Hemen:** Arızalı buhar kapanlarını değiştir (en hızlı ROI)
2. **Kısa vade (1-3 ay):** Kondensat geri dönüş hatlarını tamamla
3. **Orta vade (3-6 ay):** Flash tank kur, deaerator optimize et
4. **Uzun vade (6-12 ay):** Feedwater heater ekle, su arıtma yükselt

## İlgili Dosyalar

- Hesaplama formülleri: `steam_turbine/formulas.md` — Çevrim verimi ve exergy hesaplamaları
- Benchmark verileri: `steam_turbine/benchmarks.md` — Buhar koşulları benchmark
- Verim iyileştirme: `steam_turbine/solutions/efficiency_improvement.md` — Türbin iç verim
- Bakım: `steam_turbine/solutions/maintenance.md` — Bakım planlaması
- Kazan kondensat dönüşü: `boiler/solutions/condensate_return.md` — Detaylı kondensat geri dönüş rehberi
- Kazan blowdown geri kazanım: `boiler/solutions/blowdown_recovery.md` — Blowdown ısı geri kazanım
- Kazan ekonomizer: `boiler/solutions/economizer.md` — Baca gazı ısı geri kazanım
- Kazan buhar kapanı: `boiler/solutions/steam_trap.md` — Buhar kapanı bakım
- Ekipmanlar arası fırsatlar: `factory/cross_equipment.md` — Fabrika seviyesi entegrasyon
- Fabrika benchmarkları: `factory/factory_benchmarks.md` — Sektörel kondensat geri dönüş oranları

## Referanslar

- Spirax Sarco (2021). *The Steam and Condensate Loop*, Technical Reference Guide.
- US DOE (2012). *Improving Steam System Performance — A Sourcebook for Industry*, 2nd Edition.
- ASME PTC 12.2 (2010). *Steam Condensing Apparatus Performance Test Codes*, ASME.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- Armstrong International, "Condensate Recovery Systems" Application Guide.
- TLV Co., "Steam Engineering — Condensate Recovery Systems" Technical Handbook.
- Rosen, M.A. & Dincer, I. (1999). "Exergy analysis of waste emissions," *International Journal of Energy Research*.
- IAPWS-IF97, International Association for the Properties of Water and Steam — Steam Tables.
- Türkiye Enerji Verimliliği Derneği (ENVER), Buhar Sistemleri Verimlilik Kılavuzu.
- Bejan, A., Tsatsaronis, G. & Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
