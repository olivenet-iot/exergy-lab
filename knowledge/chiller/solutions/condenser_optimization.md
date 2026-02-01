---
title: "Çözüm: Kondenser Optimizasyonu — Condenser Optimization"
category: solutions
equipment_type: chiller
keywords: [kondenser, optimizasyon, chiller]
related_files: [chiller/equipment/cooling_tower.md, chiller/benchmarks.md, chiller/solutions/maintenance.md]
use_when: ["Kondenser optimizasyonu önerilirken", "Kondenser kirlenme/performans analiz edilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Kondenser Optimizasyonu — Condenser Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Yüksek kondenser sıcaklığı chiller'ın lift'ini (evaporatör-kondenser basınç farkı) artırır ve COP'u düşürür. Kirli kondenser boruları, optimize edilmemiş soğutma kulesi performansı ve sabit kondenser suyu sıcaklığı setpoint'i yaygın enerji israfı kaynaklarıdır. Kondenser tarafındaki her 1°C sıcaklık artışı, chiller COP'unu yaklaşık %2-3 düşürür.

**Çözüm:** Kondenser suyu sıcaklığını ve yaklaşım sıcaklığını (approach temperature) optimize etmek. Soğutma kulesi performansını iyileştirmek, kondenser borularını temiz tutmak ve su arıtma programını geliştirmek.

**Tipik Tasarruf:** %5-15 (chiller enerji tüketiminde)
**Tipik ROI:** 0.5-2 yıl

## Çalışma Prensibi

Chiller performansı doğrudan kondenser koşullarına bağlıdır. Kompresörün görevi, düşük basınçlı soğutucu akışkanı yüksek basınca sıkıştırmaktır; kondenser sıcaklığı ne kadar yüksekse, bu basınç farkı (lift) o kadar büyük olur ve kompresör daha fazla enerji harcar.

### Kondenser Sıcaklığı ve COP İlişkisi

Carnot COP formülünden türetilen yaklaşım:

```
COP_soğutma = T_evap / (T_kond - T_evap)
```

Burada:
- `T_evap`: Evaporatör sıcaklığı [K]
- `T_kond`: Kondenser sıcaklığı [K]
- Sıcaklıklar Kelvin cinsindendir (°C + 273.15)

**Pratik kural:** Kondenser suyu sıcaklığındaki her 1°C düşüş, chiller COP'unda yaklaşık %2-3 iyileşme sağlar.

### COP İyileşme Tablosu (Kondenser Suyu Sıcaklığına Göre)

| Kondenser Suyu Giriş (°C) | Kondenser Suyu Çıkış (°C) | Kondensasyon Sıcaklığı (°C) | Yaklaşık COP | Baz COP'a Göre İyileşme |
|----------------------------|---------------------------|----------------------------|--------------|--------------------------|
| 32 (baz) | 37 | 40 | 5.50 | — |
| 30 | 35 | 38 | 5.85 | +%6.4 |
| 28 | 33 | 36 | 6.25 | +%13.6 |
| 26 | 31 | 34 | 6.70 | +%21.8 |
| 24 | 29 | 32 | 7.20 | +%30.9 |

*Not: Değerler 7°C evaporatör çıkış suyu sıcaklığı ve tipik santrifüj chiller için yaklaşık değerlerdir.*

### Optimizasyon Alanları

Kondenser optimizasyonu üç ana alana ayrılır:

1. **Soğutma kulesi optimizasyonu:** Fan hızı kontrolü, dolgu (fill) bakımı/yenileme, su dağıtım düzeni
2. **Kondenser boru temizliği:** Online/offline temizlik yöntemleri, fouling faktörü kontrolü
3. **Su arıtma iyileştirmesi:** Kireç, korozyon ve biyolojik büyüme kontrolü

## Soğutma Kulesi Optimizasyonu

### Fan Hızı Kontrolü

| Kontrol Yöntemi | Enerji Tasarrufu | Maliyet | Açıklama |
|-----------------|-----------------|---------|----------|
| Tek hızlı fan (açık/kapalı) | Baz | — | En verimsiz; sık açma/kapama |
| İki hızlı fan | %15-25 | Düşük | Orta iyileşme, düşük yatırım |
| VSD fan kontrolü | %30-50 | Orta | En iyi enerji optimizasyonu |
| Fan kaldırma (fan cycling) | %10-20 | Düşük | Çok hücreli kulelerde bazı fanları kapatma |

**Optimum yaklaşım sıcaklığı:** Soğutma kulesi çıkış suyu sıcaklığı ile dış hava yaş termometre sıcaklığı arasındaki fark. Tipik hedef: 3-5°C (yeni/bakımlı kule), 5-8°C (eski kule).

### Dolgu (Fill) Bakımı ve Yenileme

| Dolgu Durumu | Yaklaşım Sıcaklığı Etkisi | Aksiyon |
|-------------|---------------------------|---------|
| Yeni/temiz | Tasarım değeri (3-5°C) | Düzenli kontrol |
| Kısmen kirli/kireçli | +2-4°C | Kimyasal temizlik |
| Ciddi kirli/hasarlı | +5-10°C | Dolgu değişimi |
| Biyofilm kaplamalı | +3-6°C | Biyosit uygulama + temizlik |

### Su Dağıtım Düzeni

- Tıkalı nozullar eşit olmayan su dağılımına yol açar ve kule verimini düşürür
- Düzenli nozul kontrolü ve temizliği
- Kırık veya eksik nozulların değiştirilmesi
- Su dağıtım tepsisinin düzgünlük kontrolü

## Kondenser Boru Temizliği

### Online Temizlik Yöntemleri

| Yöntem | Etkinlik | Maliyet | Açıklama |
|--------|----------|---------|----------|
| Sünger top sistemi (automatic ball) | Yüksek | €5,000-15,000 | Sürekli temizlik, fouling oluşumunu engeller |
| Fırça sistemi (brush system) | Yüksek | €8,000-20,000 | Boru içinde ileri-geri hareket eden fırçalar |
| Kimyasal dozlama (anti-scaling) | Orta | €2,000-5,000/yıl | Kireç önleyici kimyasal sürekli dozlama |

### Offline Temizlik Yöntemleri

| Yöntem | Etkinlik | Maliyet | Süre | Açıklama |
|--------|----------|---------|------|----------|
| Mekanik fırçalama | İyi | €1,000-3,000 | 1-2 gün | Manuel fırça ile boru temizliği |
| Kimyasal temizlik | İyi | €1,500-4,000 | 4-8 saat | Asidik/alkalin solüsyon ile kimyasal çözme |
| Yüksek basınçlı su | Çok iyi | €2,000-5,000 | 1-2 gün | Hidrojet ile sert kireç giderme |
| Mekanik + kimyasal kombine | Mükemmel | €3,000-8,000 | 2-3 gün | En kapsamlı temizlik |

### Fouling Faktörü ve Etkisi

Fouling (kirlenme), kondenser borularında kireç, biyofilm ve tortu birikerek ısı transferini azaltır:

```
Q = U × A × LMTD
U_kirli = 1 / (1/U_temiz + R_fouling)
```

Burada:
- `Q`: Isı transfer hızı [kW]
- `U`: Toplam ısı transfer katsayısı [kW/m²·K]
- `A`: Isı transfer yüzeyi [m²]
- `LMTD`: Logaritmik ortalama sıcaklık farkı [K]
- `R_fouling`: Fouling direnci [m²·K/kW]

| Fouling Durumu | R_fouling (m²·K/kW) | Kondenser Sıcaklık Artışı | COP Etkisi |
|----------------|---------------------|--------------------------|------------|
| Temiz | 0 | 0°C | Baz |
| Hafif kirli | 0.044 | +1-2°C | -%2 ile -%6 |
| Orta kirli | 0.088 | +3-5°C | -%6 ile -%15 |
| Ciddi kirli | 0.176 | +6-10°C | -%12 ile -%30 |

## Su Arıtma İyileştirmesi

| Kontrol Parametresi | Hedef Aralık | Ölçüm Sıklığı | Kontrol Yöntemi |
|---------------------|-------------|----------------|-----------------|
| pH | 7.0-8.5 | Günlük | Asit/baz dozlama |
| İletkenlik (TDS) | <2,500 µS/cm | Günlük | Blöf (blowdown) kontrolü |
| Sertlik (CaCO₃) | <200 ppm | Haftalık | Kireç önleyici dozlama |
| Klorür | <250 ppm | Haftalık | Blöf ile seyreltme |
| Biyolojik kontrol | Legionella <1,000 CFU/L | Aylık | Biyosit dozlama, UV |
| Konsantrasyon oranı | 3-6 çevrim | Sürekli | Otomatik blöf kontrolü |

## Kondenser Suyu Sıcaklığı Reset Stratejisi

Sabit kondenser suyu setpoint'i (örn. 30°C) yerine, dış hava yaş termometre sıcaklığına göre dinamik reset uygulanır:

```
T_kond_su_setpoint = T_yaş_termometre + Yaklaşım_hedef + Güvenlik_marjı
```

Burada:
- `T_yaş_termometre`: Dış ortam yaş termometre sıcaklığı [°C]
- `Yaklaşım_hedef`: Soğutma kulesi yaklaşım sıcaklığı hedefi [°C] (tipik: 4-5°C)
- `Güvenlik_marjı`: Chiller minimum kondenser suyu sıcaklık sınırı için güvenlik payı [°C] (tipik: 1-2°C)

**Dikkat:** Kondenser suyu sıcaklığı çok düşürüldüğünde aşağıdaki riskler oluşur:
- Düşük kompresör head basıncı → genişleme vanası kontrolünde sorun
- Yağ viskozitesi artışı → yağ geri dönüş problemi
- Bazı chiller'larda minimum kondenser suyu sıcaklığı limiti vardır (tipik: 15-18°C)

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Kondenser yaklaşım sıcaklığı >5°C ise (boru temizliği / kule bakımı gerekli)
- Soğutma kulesi fanları tek hızlı ise (VSD retrofit fırsatı)
- Kondenser suyu sıcaklığı sabit setpoint'te çalışıyorsa (reset stratejisi fırsatı)
- Su arıtma programı yetersiz veya yoksa
- Son 2 yılda kondenser boru temizliği yapılmamışsa

### Ne Zaman Uygulanmamalı
- Chiller zaten minimum kondenser suyu sıcaklığında çalışıyorsa
- Soğutma kulesi kapasitesi yetersizse (kule büyütme gerekli — farklı proje)
- Proses gereksinimleri sabit kondenser koşulları gerektiriyorsa

## Yatırım Maliyeti

| Optimizasyon Kalemi | Maliyet Aralığı (€) | Tipik Tasarruf | Not |
|---------------------|---------------------|----------------|-----|
| Kondenser boru mekanik temizliği | 2,000-5,000 | %2-5 | Yılda 1-2 kez |
| Kondenser boru kimyasal temizliği | 1,500-4,000 | %2-5 | Yılda 1 kez |
| Online boru temizlik sistemi (sünger top) | 5,000-15,000 | %3-8 | Tek seferlik yatırım |
| Soğutma kulesi fan VSD | 5,000-15,000 | %3-8 | Fan başına maliyet |
| Soğutma kulesi dolgu değişimi | 8,000-25,000 | %2-5 | Kule boyutuna bağlı |
| Su arıtma sistemi iyileştirme | 3,000-10,000 | %1-3 | Dozlama sistemi + kimyasal |
| Kondenser suyu reset kontrolü (BMS) | 2,000-8,000 | %3-8 | BMS programlama + sensörler |
| Kapsamlı kondenser optimizasyonu (paket) | 15,000-30,000 | %8-15 | Tüm kalemlerin kombinasyonu |

## ROI Hesabı

### Formül
```
COP_iyileşme_% = 2.5 × ΔT_kondenser_düşüş
Yıllık_chiller_enerji = Kapasite_kW × Çalışma_saati × Ort_yük / COP_mevcut
Yıllık_tasarruf_kWh = Yıllık_chiller_enerji × COP_iyileşme_% / 100
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

Burada:
- `ΔT_kondenser_düşüş`: Kondenser suyu sıcaklık düşüşü [°C]
- `Kapasite_kW`: Chiller nominal soğutma kapasitesi [kW]
- `Çalışma_saati`: Yıllık chiller çalışma süresi [saat/yıl]
- `Ort_yük`: Ortalama yük oranı (0-1 arası)
- `COP_mevcut`: Mevcut ortalama COP
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap
- 800 kW chiller, 4,000 saat/yıl, ortalama %65 yük
- Mevcut kondenser suyu giriş: 32°C → Optimizasyon sonrası: 28°C (4°C düşüş)
- Mevcut COP: 5.0
- Elektrik fiyatı: €0.12/kWh

```
COP_iyileşme = 2.5 × 4 = %10
Yıllık_chiller_enerji = 800 × 4,000 × 0.65 / 5.0 = 416,000 kWh
Yıllık_tasarruf_kWh = 416,000 × 10 / 100 = 41,600 kWh
Yıllık_tasarruf_EUR = 41,600 × 0.12 = €4,992/yıl
Yatırım (boru temizlik + kule fan VSD + reset kontrolü) = €18,000
Geri_ödeme = 18,000 / 4,992 = 3.6 yıl
```

- **Geri ödeme süresi: ~3.6 yıl**

*Not: Bu hesapta soğutma kulesi fan enerjisindeki ek tasarruf dahil edilmemiştir; VSD fan kontrolü ile kule fan enerjisinden %30-50 ek tasarruf beklenir, bu da geri ödeme süresini kısaltır.*

## Uygulama Adımları

1. **Mevcut durum tespiti:** Kondenser suyu giriş/çıkış sıcaklıklarını, yaklaşım sıcaklığını, fouling faktörünü ve soğutma kulesi performansını ölç
2. **Su analizi:** Su kalitesi parametrelerini (pH, TDS, sertlik, biyolojik) ölç ve mevcut su arıtma programını değerlendir
3. **Boru temizliği:** Kondenser borularını mekanik ve/veya kimyasal yöntemle temizle; temizlik öncesi/sonrası yaklaşım sıcaklığını karşılaştır
4. **Soğutma kulesi bakımı:** Dolgu, nozul, fan ve eliminator durumunu kontrol et; gerekli bakım/değişimi yap
5. **Fan VSD kurulumu:** Tek hızlı fanları VSD'ye dönüştür; yaş termometre sıcaklığına göre fan hız kontrolü programla
6. **Kondenser suyu reset programlama:** BMS'te dinamik kondenser suyu sıcaklık reset stratejisini programla; chiller minimum limitlerine uygun güvenlik kilitleri ayarla
7. **Su arıtma iyileştirme:** Blöf kontrolünü otomatize et, kireç önleyici ve biyosit dozlama programını optimize et
8. **Performans izleme:** Sürekli izleme ile kondenser yaklaşım sıcaklığı, COP ve enerji tüketimini takip et; sapmalarda alarm oluştur

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Düşük kondenser suyu sıcaklığı | Chiller minimum liminin altında çalışma → genişleme vanası kontrolü bozulur | Chiller üreticisinin minimum kondenser suyu sıcaklığını BMS'te alt limit olarak tanımla |
| Yağ dönüş problemi | Düşük kondenser basıncında yağ viskozitesi artar, dönüş zorlaşır | Minimum head basıncı limiti koy, yağ geri dönüş sistemi kontrol et |
| Legionella riski | Soğutma kulesi suyunda biyolojik üreme | Düzenli biyosit dozlama, su sıcaklığını izle, yıllık Legionella testi |
| Kireçlenme | Su arıtma yetersizse borularda hızlı kireç birikimi | Otomatik blöf kontrolü, kireç önleyici dozlama, düzenli su analizi |
| Korozyon | Aşırı kimyasal dozlama veya düşük pH borularda korozyona yol açar | Korozyon kupon testi, pH kontrolü, inhibitör dozlama |
| Aşırı blöf | Gereğinden fazla blöf yapılırsa su ve enerji israfı oluşur | Konsantrasyon oranı kontrolü (3-6 çevrim), iletkenlik bazlı otomatik blöf |
| Donma riski | Kış aylarında kule suyu donabilir | Düşük sıcaklıkta kuleyi bypass et, ısıtıcı veya glikol kullan |

## İlgili Dosyalar
- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller VSD çözümü: `solutions/chiller_vsd.md`
- Soğutma suyu sıcaklık reset: `solutions/chiller_chilled_water_reset.md`
- Serbest soğutma: `solutions/chiller_free_cooling.md`
- Chiller sıralama optimizasyonu: `solutions/chiller_sequencing.md`
- Chiller exergy formülleri: `formulas/chiller_exergy.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, "Cooling Towers" and "Condensers" chapters
- ASHRAE Guideline 22, "Instrumentation for Monitoring Central Chilled-Water Plant Efficiency"
- Cooling Technology Institute (CTI), "Standard 201 — Certification Standard for Commercial Water Cooling Towers"
- DOE/FEMP, "Best Practices for Chiller Plant Operation"
- BSRIA, "Rules of Thumb — Guidelines for Building Services"
- Carrier/Trane/York, "Application Guide — Condenser Water Temperature Optimization"
- Nalco Water (Ecolab), "Cooling Water Treatment Handbook"
- AHRI Standard 550/590, "Performance Rating of Water-Chilling Packages"
