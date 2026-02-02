---
title: "Buhar Türbini Verim İyileştirme — Steam Turbine Efficiency Improvement"
category: solutions
equipment_type: steam_turbine
keywords: [verim iyileştirme, fouling removal, seal replacement, tip clearance, steam path audit, kanat kaplama, ısı yalıtımı, online monitoring]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/audit.md, steam_turbine/solutions/maintenance.md, steam_turbine/solutions/load_matching.md, steam_turbine/equipment/back_pressure.md, steam_turbine/equipment/condensing.md]
use_when: ["Türbin verimi benchmark altında kaldığında", "Verim iyileştirme önerileri yapılırken", "İzentropik verim düşüşü tespit edildiğinde", "Exergy yıkımı yüksek çıktığında"]
priority: high
last_updated: 2026-01-31
---
# Buhar Türbini Verim İyileştirme — Steam Turbine Efficiency Improvement

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Buhar türbinlerinde işletme süresiyle birlikte izentropik verim %2-8 düşer; bu durum elektrik üretiminde ciddi kayıplara ve exergy yıkımının artmasına neden olur. Küçük-orta ölçekli endüstriyel türbinlerde verim bozunması genellikle fark edilmeden yıllarca sürer.

**Çözüm:** Kanat temizliği, sızdırmazlık değişimi, kanat ucu boşluğu ayarı, buhar yolu denetimi (steam path audit), kanat kaplama teknolojileri, gövde ısı yalıtımı ve online monitoring uygulamaları ile %1-5 verim iyileştirmesi sağlanabilir.

**Tipik Tasarruf:** %1-5 izentropik verim iyileştirmesi (türbin durumuna bağlı)
**Tipik ROI:** 0.5-3 yıl

## 1. Kanat Temizliği — Fouling Removal

### 1.1 Fouling Kaynakları

Buhar türbini kanatlarında birikim (fouling) başlıca şu kaynaklardan oluşur:

| Birikim Türü | Kaynak | Etki | Tipik Sektörler |
|--------------|--------|------|-----------------|
| Silika (SiO₂) birikimi | Kazan suyundan taşınan silika | Kanat profilini bozar, akış direncini artırır | Tüm sektörler |
| Tuz birikimi (NaCl, Na₂SO₄) | Kötü kaliteli buhar, carry-over | Korozyon + akış kısıtlaması | Gıda, kimya |
| Oksit tabakası | Yüksek sıcaklıkta oksidasyon | Yüzey pürüzlülüğü artışı | Tüm sektörler |
| Bakır birikimi | Kondensat hattı bakır korozyonu | Kanat kenarlarında birikim | Eski tesisler |

### 1.2 Fouling'in Verime Etkisi

```
Kanat yüzey pürüzlülüğü artışının verime etkisi:
- Hafif fouling: η_is düşüşü %0.5-1.0
- Orta fouling:  η_is düşüşü %1.0-2.5
- Ağır fouling:  η_is düşüşü %2.0-4.0

Kademe basınç oranı sapması:
ΔP_kademe/P_kademe > %5 ise fouling şüphesi doğar

Heat rate etkisi:
Her %1 η_is kaybı ≈ %1-1.5 heat rate artışı
```

### 1.3 Temizlik Yöntemleri

| Yöntem | Açıklama | Verim Kazanımı | Maliyet (€) | Duruş Süresi |
|--------|----------|----------------|-------------|--------------|
| Online su yıkama (water washing) | Düşük yükte sıcak su/kondensat enjeksiyonu | %0.3-1.0 | 500-2,000 | 4-8 saat (kısmi) |
| Offline kimyasal temizlik | Türbin açık, kanatlar asit/alkali ile yıkanır | %0.5-2.0 | 5,000-20,000 | 3-7 gün |
| Kuru buz temizliği (dry ice blasting) | CO₂ pelletleri ile birikinti temizleme | %0.5-1.5 | 3,000-10,000 | 2-5 gün |
| Mekanik temizlik (major overhaul sırasında) | Kanatlar sökülerek temizlenir/parlatılır | %1.0-3.0 | Overhaul dahilinde | Overhaul süresi |

**Öneri:** Online su yıkama yılda 1-2 kez, offline kimyasal temizlik her 3-5 yılda bir uygulanmalıdır. Kazan suyu kalitesi kontrol altında tutularak fouling hızı azaltılır.

## 2. Sızdırmazlık Optimizasyonu — Seal Replacement/Upgrade

### 2.1 Sızdırmazlık Türleri ve Kayıp Mekanizması

Buhar türbinlerinde üç temel sızdırmazlık noktası vardır:

1. **Labirent sızdırmazlıklar (labyrinth seals):** Rotor-stator arası buhar kaçağını minimize eder
2. **Kanat ucu sızdırmazlıklar (tip seals):** Kanat ucu üzerinden geçen buhar kaçağını azaltır
3. **Mil sızdırmazlıkları (shaft seals / gland seals):** Mil geçiş noktalarındaki buhar kaçağını önler

### 2.2 Aşınmış Sızdırmazlıkların Etkisi

```
Sızdırmazlık boşluğu (clearance) artışının verime etkisi:
- Labirent seal boşluğu 2 katına çıkarsa: η_is düşüşü %0.5-1.5
- Tip seal boşluğu 2 katına çıkarsa: η_is düşüşü %0.5-2.0
- Gland seal kaçağı %50 artarsa: Buhar kaybı %0.3-1.0

Toplam sızdırmazlık kayıp potansiyeli: η_is %1.0-3.5 düşüş
```

### 2.3 Sızdırmazlık Yükseltme Seçenekleri

| Teknoloji | Açıklama | Verim Kazanımı | Yatırım (€/türbin) | SPP (yıl) |
|-----------|----------|----------------|---------------------|-----------|
| Geleneksel labirent yenileme | Aşınmış labirent segmentleri değişimi | %0.5-1.0 | 10,000-30,000 | 0.5-1.5 |
| Abradable sızdırmazlık | Rotor temas ettiğinde aşınan malzeme | %0.5-1.5 | 15,000-40,000 | 0.5-2.0 |
| Brush seal (fırça sızdırmazlık) | Esnek fırça telli ileri teknoloji seal | %0.8-2.0 | 20,000-60,000 | 1.0-2.5 |
| Honeycomb seal | Bal peteği yapılı düşük kaçak seal | %0.5-1.5 | 15,000-50,000 | 1.0-2.0 |

**Brush seal avantajı:** Konvansiyonel labirent sızdırmazlığa göre %40-60 daha az kaçak, rotor temasına karşı dayanıklı, daha uzun ömür.

### 2.4 Gland Sealing System Optimizasyonu

- Gland buhar basıncını optimize et (aşırı yüksek basınç gereksiz buhar tüketir)
- Gland kondanser vakumunu kontrol et (hava sızıntısı kondenser vakumunu bozar)
- Gland buhar geri kazanımını sağla (düşük basınçlı buhar olarak kullanılabilir)
- Tipik tasarruf: %0.2-0.5 buhar tasarrufu

## 3. Kanat Ucu Boşluğu Ayarı — Tip Clearance

### 3.1 Kanat Ucu Boşluğu ve Verim İlişkisi

```
Tip clearance (kanat ucu boşluğu):
- Tasarım boşluğu: 0.3-1.0 mm (türbin boyutuna bağlı)
- Kabul edilebilir aşınma: Tasarım + %50
- Kritik aşınma: Tasarım × 2 veya üzeri

Verim etkisi (yaklaşık):
Δη_is / Δ(tip_clearance) ≈ -%0.5 ile -%1.5 / mm (kademe başına)

Örnek:
0.5 mm tasarım boşluğu → 1.0 mm'ye artarsa
Kademe verimi düşüşü: %0.25-0.75
10 kademeli türbin toplam etkisi: %1.0-3.0 η_is düşüşü
```

### 3.2 Boşluk Ölçüm ve Ayar Yöntemi

| Aşama | Açıklama | Araç/Yöntem |
|-------|----------|-------------|
| Ölçüm (soğuk) | Türbin açıkken feeler gauge ile ölçüm | Feeler gauge, dial indicator |
| Ölçüm (sıcak) | Yakınlık probu (proximity probe) ile çalışma anı ölçümü | Eddy current probları |
| Ayar | Sızdırmazlık segmentlerinin yenilenmesi veya shim ile ayar | OEM parçalar |
| Doğrulama | Overhaul sonrası ölçüm ve trend karşılaştırma | OEM tolerans tablosu |

**Kritik not:** Kanat ucu boşluğu çok dar ayarlanırsa, termal genleşme sırasında rotor-stator teması (rub) oluşur — bu katastrofik hasara yol açabilir. OEM toleranslarına kesinlikle uyulmalıdır.

## 4. Buhar Yolu Denetimi — Steam Path Audit

### 4.1 Steam Path Audit Nedir?

Buhar yolu denetimi (steam path audit), türbinin tüm iç akış yolunun sistematik incelenmesidir. Major overhaul sırasında yapılır ve şu bileşenleri kapsar:

1. Kanat profili muayenesi (erozyon, korozyon, birikinti, çatlak)
2. Kanat ucu boşluk ölçümü (tüm kademelerde)
3. Sızdırmazlık boşluk ölçümü (labirent ve tip seals)
4. Nozül/diyafram muayenesi (erozyon, eğilme)
5. Gövde ek yeri (horizontal joint) kontaminasyon kontrolü

### 4.2 Steam Path Audit Sonuçları ve Aksiyon

| Bulgu | Tipik Verim Etkisi | Aksiyon | Maliyet Aralığı (€) |
|-------|---------------------|--------|---------------------|
| Kanat erozyon (SPE — solid particle erosion) | %0.5-2.0 | Kanat değişimi veya yeniden profilleme | 20,000-100,000 |
| Kanat kenar hasar (FOD — foreign object damage) | %0.3-1.5 | Kanat onarımı/değişimi | 10,000-50,000 |
| Labirent seal aşınması | %0.5-1.5 | Seal segment değişimi | 10,000-40,000 |
| Tip seal aşınması | %0.5-2.0 | Seal değişimi / brush seal upgrade | 15,000-60,000 |
| Nozül erozyon | %0.3-1.0 | Nozül onarımı/değişimi | 15,000-80,000 |
| Gövde ek yeri sızıntı | %0.2-0.5 | Yüzey işleme, yeniden sızdırmazlık | 5,000-20,000 |

### 4.3 Steam Path Audit Maliyeti ve ROI

```
Tipik steam path audit maliyeti: €15,000-40,000 (major overhaul dahilinde)

Beklenen verim iyileştirmesi: %2-5 η_is (ihmal edilmiş türbinlerde)

ROI hesabı örneği (10 MW türbin, η_is %75 → %79):
- Mevcut güç: 10,000 kW
- İyileştirilmiş güç: 10,000 × (1 + 0.04/0.75) ≈ 10,533 kW
- Ek güç: 533 kW
- Yıllık ek üretim: 533 × 7,000 h = 3,731,000 kWh
- Tasarruf: 3,731,000 × 0.10 €/kWh = €373,100/yıl
- SPP: Overhaul maliyeti dahil 1-3 yıl
```

## 5. Kanat Kaplama Teknolojileri — Blade Coating

### 5.1 Kaplama Türleri ve Uygulamaları

| Kaplama Türü | Uygulama | Avantaj | Ek Maliyet (€/türbin) | Ömür Uzatma |
|-------------|----------|---------|----------------------|-------------|
| Stellite kaplama (kenar) | Son kademe kanat kenarları | Erozyon direnci 5-10 kat artar | 5,000-20,000 | 2-3 kat |
| Boride difüzyon kaplama | Tüm kanat yüzeyi | Erozyon + korozyon direnci | 10,000-30,000 | 2-4 kat |
| Termik sprey kaplama (HVOF) | Kanat yüzeyi | Yüzey sertliği ve pürüzsüzlüğü | 15,000-40,000 | 2-3 kat |
| Lazer kaplama (cladding) | Hasar görmüş kanat onarımı | OEM profili geri kazanım | 8,000-25,000 | Orijinal ömür |
| PVD/CVD ince film kaplama | Yüksek performans kanatlar | Sürtünme azaltma, pürüzsüzlük | 20,000-60,000 | 2-4 kat |

### 5.2 Kaplama ile Verim İyileştirmesi

```
Kanat yüzey pürüzlülüğünün azaltılması ile verim etkisi:
- Yeni kanat: Ra = 0.8-1.6 µm
- 20,000 saat sonrası: Ra = 3.2-6.3 µm
- Kaplama sonrası: Ra = 0.4-1.2 µm

Verim kazanımı (kaplama + parlatma):
- HP kademe: %0.3-0.8
- IP kademe: %0.2-0.5
- LP kademe: %0.1-0.3
- Toplam: %0.5-1.5 η_is iyileştirme
```

## 6. Gövde Isı Yalıtımı — Casing Insulation

### 6.1 Yalıtım Eksikliğinin Etkisi

Türbin gövde yüzey sıcaklığının yüksek olması doğrudan ısı kaybıdır ve buhar enerjisinin bir kısmı iş yerine çevreye atılır.

| Durum | Gövde Yüzey Sıcaklığı (°C) | Isı Kaybı (kW/m²) | Toplam Kayıp (10 MW türbin) |
|-------|----------------------------|--------------------|----------------------------|
| Yalıtımsız | 200-350 | 2.0-5.0 | 20-80 kW |
| Kötü yalıtımlı | 80-150 | 0.5-1.5 | 5-25 kW |
| İyi yalıtımlı | 40-60 | 0.1-0.3 | 1-5 kW |

### 6.2 Yalıtım Uygulama

- **Malzeme:** Mineral yünü (rockwool) veya kalsiyum silikat, aluminyum folyo kaplama
- **Kalınlık:** 50-100 mm (gövde sıcaklığına bağlı)
- **Hedef:** Yüzey sıcaklığı <60°C (personel güvenliği + enerji tasarrufu)
- **Yatırım:** €3,000-10,000 (türbin boyutuna bağlı)
- **SPP:** 0.5-2 yıl

## 7. Online Monitoring — Sürekli İzleme

### 7.1 İzlenecek Parametreler

| Parametre | Sensör Tipi | Amacı | Alarm Eşiği |
|-----------|------------|-------|-------------|
| Giriş basıncı (P_in) | Basınç transmitteri | Buhar koşul izleme | ±%5 tasarım |
| Giriş sıcaklığı (T_in) | Termokuple/RTD | Kızdırma kontrolü | ±10°C tasarım |
| Çıkış basıncı (P_out) | Basınç transmitteri | Yük/vakum izleme | ±%5 tasarım |
| Çıkış sıcaklığı (T_out) | Termokuple/RTD | Verim sapma tespiti | ΔT > 5°C trend |
| Buhar debisi (ṁ) | Orifis/vortex flowmetre | Güç hesaplama | — |
| Elektrik gücü (Ẇ) | Güç analizörü | Verim hesaplama | — |
| Titreşim | Accelerometre | Mekanik durum | ISO 10816 |
| Kademe basınçları | Basınç transmitteri | Fouling/erozyon tespiti | ΔP sapma > %5 |

### 7.2 Performans İzleme Sistemi

```
Online performans izleme:
1. Anlık izentropik verim hesaplama:
   η_is = (h_in - h_out) / (h_in - h_out,is)

2. Heat rate trendi:
   HR = ṁ × (h_in - h_fw) / Ẇ_elek  [kJ/kWh]

3. Sapma analizi (deviation analysis):
   Δη_is = η_is,mevcut - η_is,referans
   ΔHR = HR_mevcut - HR_referans

4. Alarm seviyeleri:
   Uyarı: Δη_is > %1.0 veya ΔHR > %1.5
   Aksiyon: Δη_is > %2.0 veya ΔHR > %3.0
   Acil: Δη_is > %4.0 veya ΔHR > %5.0

Yatırım: €15,000-50,000 (sensörler + DCS entegrasyon)
SPP: 1-3 yıl (erken arıza tespiti + verim izleme ile)
```

## 8. Verim İyileştirme ROI Tablosu — Özet

### 8.1 İyileştirme Bazında ROI

| İyileştirme | η_is Kazanım [%] | Yatırım (€) | Yıllık Tasarruf (€)* | SPP (yıl) | Uygulama Kolaylığı |
|-------------|-------------------|-------------|----------------------|-----------|---------------------|
| Kanat temizliği (online) | 0.3-1.0 | 500-2,000 | 5,000-30,000 | <0.5 | Kolay |
| Kanat temizliği (offline) | 0.5-2.0 | 5,000-20,000 | 10,000-60,000 | 0.3-1.0 | Orta |
| Sızdırmazlık değişimi (konvansiyonel) | 0.5-1.5 | 10,000-40,000 | 10,000-45,000 | 0.5-2.0 | Orta |
| Brush seal yükseltme | 0.8-2.0 | 20,000-60,000 | 15,000-60,000 | 1.0-2.5 | Orta |
| Kanat ucu boşluğu ayarı | 0.5-2.0 | Overhaul dahilinde | 10,000-60,000 | 0.5-1.5 | Overhaul gerektirir |
| Steam path audit + onarım | 2.0-5.0 | 50,000-200,000 | 50,000-400,000 | 0.5-2.0 | Büyük overhaul |
| Kanat kaplama | 0.5-1.5 | 10,000-60,000 | 10,000-45,000 | 1.0-3.0 | Orta |
| Gövde ısı yalıtımı | 0.1-0.3 | 3,000-10,000 | 5,000-20,000 | 0.3-1.0 | Kolay |
| Online monitoring | — (dolaylı) | 15,000-50,000 | 20,000-80,000 | 0.5-2.0 | Orta |

*5 MW türbin, 7,000 h/yıl, elektrik 0.10 €/kWh bazında hesaplanmıştır.

### 8.2 Kombine İyileştirme Senaryosu

```
Senaryo: 10 MW karşı basınçlı türbin, η_is mevcut = %72 (benchmark: %78-82)

Uygulanan iyileştirmeler:
1. Offline kanat temizliği:      +%1.5 → η_is = %73.5
2. Labirent seal yenileme:       +%1.0 → η_is = %74.5
3. Brush seal yükseltme:         +%1.5 → η_is = %76.0
4. Kanat ucu boşluk ayarı:      +%1.0 → η_is = %77.0
5. Nozül onarımı:                +%0.5 → η_is = %77.5

Toplam iyileştirme: +%5.5 (gerçekçi hedef: %4-5, etkileşim düzeltmesi ile)

Ek güç üretimi: 10,000 × 0.05/0.72 ≈ 694 kW
Yıllık ek gelir: 694 × 7,000 × 0.10 = €485,800/yıl
Toplam yatırım: ~€150,000 (overhaul dahilinde)
SPP: 150,000 / 485,800 = 0.31 yıl (~4 ay)
```

## 9. Uygulama Önceliklendirme

### 9.1 Hızlı Kazanım (Quick Win) — İlk Aşama
1. Online su yıkama ile kanat temizliği
2. Gövde ısı yalıtım kontrolü ve eksik yalıtım tamamlama
3. Gland sealing system basınç optimizasyonu

### 9.2 Orta Vadeli İyileştirmeler — Planlı Duruş
1. Sızdırmazlık değişimi (labirent → brush seal upgrade)
2. Offline kimyasal temizlik
3. Online monitoring sistemi kurulumu

### 9.3 Uzun Vadeli İyileştirmeler — Major Overhaul
1. Tam steam path audit
2. Kanat değişimi/kaplama
3. Kanat ucu boşluk optimizasyonu
4. Nozül/diyafram yenileme

## 10. Risk ve Dikkat Edilecek Noktalar

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Aşırı dar tip clearance | Termal genleşmede rotor-stator teması (rub) | OEM toleranslarına uy |
| Kötü kaliteli yedek parça | Düşük kalite seal/kanat → erken aşınma | OEM veya sertifikalı tedarikçi kullan |
| Online yıkama sırasında termal şok | Soğuk su ile sıcak kanatlar arası termal stres | Yıkama prosedürüne uy, kademeli soğutma |
| Hatalı kaplama uygulaması | Kanat profilini bozabilir, balans sorununa yol açar | Deneyimli kaplama firması seç |
| Overhaul sonrası balans sorunu | Kanat değişimi sonrası rotor dengesi bozulabilir | Rotor balans testi yap |

## İlgili Dosyalar

- Hesaplama formülleri: `steam_turbine/formulas.md` — İzentropik verim ve exergy formülleri
- Benchmark verileri: `steam_turbine/benchmarks.md` — Verimlilik karşılaştırma tabloları
- Performans denetimi: `steam_turbine/audit.md` — ASME PTC 6 bazlı denetim metodolojisi
- Bakım planlaması: `steam_turbine/solutions/maintenance.md` — Preventive/predictive bakım
- Yük eşleştirme: `steam_turbine/solutions/load_matching.md` — Operasyon optimizasyonu
- Kondensat optimizasyonu: `steam_turbine/solutions/condensate_optimization.md` — Feedwater/kondensat sistemi
- Karşı basınçlı türbin: `steam_turbine/equipment/back_pressure.md` — BP türbin detayları
- Yoğuşmalı türbin: `steam_turbine/equipment/condensing.md` — Condensing türbin detayları
- Kazan kondensat dönüşü: `boiler/solutions/condensate_return.md` — Kondensat geri dönüş sistemi
- Fabrika benchmarkları: `factory/factory_benchmarks.md` — Sektörel karşılaştırma

## Referanslar

- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Sanders, W.P. (2001). *Turbine Steam Path Engineering*, PennWell Publishing.
- Leyzerovich, A.S. (2008). *Steam Turbines for Modern Fossil-Fuel Power Plants*, Fairmont Press.
- GE Power (2019). "Steam Path Audit and Upgrade Solutions," Technical Documentation.
- Siemens Energy (2020). "Steam Turbine Modernization and Upgrades," Application Guide.
- Chupp, R.E. et al. (2006). "Sealing in Turbomachinery," *Journal of Propulsion and Power*, 22(2).
- Ingistov, S. (2003). "Brush seal application in industrial gas and steam turbines," *ASME Turbo Expo*, GT2003-38509.
- US DOE (2012). *Improving Steam System Performance — A Sourcebook for Industry*, 2nd Edition.
- Tsatsaronis, G. & Park, M.H. (2002). "On avoidable and unavoidable exergy destructions," *Energy Conversion and Management*.
