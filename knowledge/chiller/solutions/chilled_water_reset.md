# Çözüm: Soğutma Suyu Sıcaklığı Reset — Chilled Water Temperature Reset

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Birçok chiller tesisinde soğutma suyu (CHW) çıkış sıcaklığı sabit setpoint'te (tipik olarak 6-7°C) tutulur — yük düşük olduğunda bile. Bu durum chiller'ı gereğinden düşük evaporatör sıcaklığında çalışmaya zorlar ve COP'u düşürür. Özellikle geçiş mevsimlerinde ve düşük yüklerde önemli enerji israfı oluşur.

**Çözüm:** Soğutma yükü azaldığında CHW setpoint'ini yükselterek (reset ederek) evaporatör sıcaklığını artırmak ve chiller COP'unu iyileştirmek. Yük bazlı veya dış hava sıcaklığı bazlı reset stratejileri uygulanır.

**Tipik Tasarruf:** %3-10 (chiller enerji tüketiminde)
**Tipik ROI:** <1 yıl (çoğunlukla kontrol değişikliği, düşük yatırım)

## Çalışma Prensibi

Chiller performansı doğrudan evaporatör sıcaklığına bağlıdır. Evaporatör sıcaklığı yükseldikçe kompresörün yapması gereken iş azalır ve COP artar.

### Termodinamik Temel

```
COP_soğutma = T_evap / (T_kond - T_evap)
```

Burada:
- `T_evap`: Evaporatör sıcaklığı [K]
- `T_kond`: Kondenser sıcaklığı [K]

**Pratik kural:** Evaporatör sıcaklığındaki (CHW setpoint'indeki) her 1°C artış, chiller COP'unda yaklaşık %2-3 iyileşme sağlar.

### CHW Sıcaklığı ve COP İlişkisi

| CHW Çıkış Sıcaklığı (°C) | Evaporatör Sıcaklığı (°C) | Yaklaşık COP | Baz COP'a Göre İyileşme |
|---------------------------|---------------------------|--------------|--------------------------|
| 6 (baz — tasarım) | 3 | 5.50 | — |
| 7 | 4 | 5.65 | +%2.7 |
| 8 | 5 | 5.80 | +%5.5 |
| 9 | 6 | 5.95 | +%8.2 |
| 10 | 7 | 6.12 | +%11.3 |
| 12 | 9 | 6.48 | +%17.8 |

*Not: Değerler 35°C kondenser sıcaklığı ve tipik santrifüj chiller için yaklaşık değerlerdir. Evaporatör yaklaşım sıcaklığı ~3°C alınmıştır.*

### Neden Sabit Setpoint Verimsiz?

Chiller tesislerinde CHW setpoint'i genellikle yılın en sıcak ve en nemli gününe (tasarım koşulları) göre belirlenir:
- İstanbul tasarım koşulu: ~34°C kuru termometre, ~24°C yaş termometre
- Bu koşulda 6-7°C CHW gereklidir (nem alma + soğutma)
- Ancak yılın >%80'inde yük tasarım yükünün altındadır
- Düşük yükte 6°C CHW gereksizdir; 8-12°C yeterli olabilir
- Sabit 6°C setpoint, chiller'ı gereksiz yere düşük COP'ta çalıştırır

## Reset Stratejileri

### 1. Yük Bazlı Reset (Load-Based Reset)

En yaygın ve etkili strateji. Soğutma yükü azaldıkça CHW setpoint'i yükseltilir:

```
CHW_setpoint = CHW_min + (CHW_max - CHW_min) × (1 - Yük_oranı)
```

Burada:
- `CHW_min`: Minimum CHW sıcaklığı (tasarım koşulu) [°C] — tipik: 6-7°C
- `CHW_max`: Maximum CHW sıcaklığı (düşük yük) [°C] — tipik: 10-12°C
- `Yük_oranı`: Anlık soğutma yükü / tasarım yükü (0-1 arası)

| Yük Oranı | CHW Setpoint (6-12°C aralığı) | Tahmini COP İyileşmesi |
|-----------|-------------------------------|------------------------|
| %100 | 6.0°C | %0 (baz) |
| %75 | 7.5°C | ~%3-4 |
| %50 | 9.0°C | ~%6-8 |
| %25 | 10.5°C | ~%9-12 |

**Yük belirleme yöntemleri:**
- CHW debi × ΔT (gidiş-dönüş sıcaklık farkı)
- AHU/FCU vana pozisyonları (en açık vana yöntemi)
- Bypass vanası pozisyonu (değişken debili sistemlerde)
- Dış hava entalpisi ile korelasyon

### 2. Dış Hava Sıcaklığı Bazlı Reset (OAT-Based Reset)

Dış hava sıcaklığı düştükçe CHW setpoint'i yükseltilir:

```
CHW_setpoint = CHW_min + (CHW_max - CHW_min) × (T_dış_max - T_dış) / (T_dış_max - T_dış_min)
```

Burada:
- `T_dış`: Dış hava sıcaklığı [°C]
- `T_dış_max`: Tasarım dış hava sıcaklığı [°C] (örn. 34°C)
- `T_dış_min`: Reset başlangıç sıcaklığı [°C] (örn. 18°C)

| Dış Hava Sıcaklığı | CHW Setpoint (İstanbul örneği) |
|---------------------|-------------------------------|
| ≥34°C | 6.0°C (minimum — tasarım koşulu) |
| 30°C | 7.5°C |
| 26°C | 9.0°C |
| 22°C | 10.5°C |
| ≤18°C | 12.0°C (maximum) |

### 3. Nem Kontrollü Reset (Humidity-Constrained Reset)

Nem alma (dehumidification) gerekliliği, CHW reset aralığını sınırlar:

```
CHW_max_nem = T_çiğ_noktası_hedef - Yaklaşım_AHU
```

Burada:
- `T_çiğ_noktası_hedef`: İç ortam hedef çiğ noktası sıcaklığı [°C]
- `Yaklaşım_AHU`: AHU serpantini yaklaşım sıcaklığı [°C] (tipik: 1-2°C)

**Kritik kural:** CHW sıcaklığı, AHU soğutma serpantininde yeterli nem alma sağlayacak düzeyde kalmalıdır. Tipik olarak CHW sıcaklığı iç ortam çiğ noktası hedefinin 1-2°C altında olmalıdır.

| İç Ortam Koşulu | Çiğ Noktası | Maximum CHW Setpoint |
|-----------------|-------------|---------------------|
| %50 RH, 24°C | 13.2°C | ~11-12°C |
| %55 RH, 24°C | 14.4°C | ~12-13°C |
| %60 RH, 24°C | 15.7°C | ~14-15°C |
| %50 RH, 22°C | 11.1°C | ~9-10°C |

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- CHW setpoint'i sabit çalışıyorsa (en yaygın durum)
- Tesis yılın >%50'sinde tasarım yükünün altında çalışıyorsa
- BMS veya chiller kontrolcüsü programlanabilir ise
- AHU/FCU kapasitesi CHW sıcaklık artışını tolere edebiliyorsa
- Nem kontrolü kritik olmayan alanlarda (ofis, ticari bina)

### Ne Zaman Uygulanmamalı veya Sınırlı Uygulanmalı
- Hassas nem kontrolü gereken alanlar (ameliyathane, ilaç üretimi, veri merkezi)
- AHU serpantinleri tasarım sınırında çalışıyorsa (ek kapasite yok)
- Sürekli tam yükte çalışan tesisler (reset fırsatı yok)
- Chiller kontrolcüsü CHW reset fonksiyonunu desteklemiyorsa
- Proses soğutma uygulamalarında sabit sıcaklık gerekliyse

## Yatırım Maliyeti

| Uygulama Kalemi | Maliyet Aralığı (€) | Açıklama |
|-----------------|---------------------|----------|
| BMS programlama (mevcut BMS yeterli ise) | 0-2,000 | Yazılım değişikliği, test ve devreye alma |
| Ek sıcaklık sensörü (CHW gidiş/dönüş) | 200-500 | Mevcut sensörler yetersizse |
| Dış hava sıcaklık/nem sensörü | 300-800 | Dış hava bazlı reset için |
| CHW debi ölçer (yük hesabı için) | 1,500-5,000 | Ultrasonik veya elektromanyetik debimetre |
| Nem sensörü (iç ortam) | 200-500 | Nem kontrollü reset için |
| Kontrol paneli güncelleme | 1,000-3,000 | Eski BMS sistemlerinde |
| Kapsamlı CHW reset projesi | 3,000-10,000 | Sensörler + BMS programlama + devreye alma |

**Not:** Mevcut BMS CHW reset fonksiyonunu destekliyorsa, yatırım maliyeti yalnızca programlama ve devreye alma ile sınırlı kalır (€0-2,000).

## ROI Hesabı

### Formül
```
COP_iyileşme_ort_% = 2.5 × ΔT_CHW_ortalama_artış
Yıllık_chiller_enerji = Kapasite_kW × Çalışma_saati × Ort_yük / COP_mevcut
Yıllık_tasarruf_kWh = Yıllık_chiller_enerji × COP_iyileşme_ort_% / 100
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_ay = Yatırım / (Yıllık_tasarruf_EUR / 12)
```

Burada:
- `ΔT_CHW_ortalama_artış`: Yıllık ağırlıklı ortalama CHW setpoint artışı [°C]
- `Kapasite_kW`: Chiller nominal soğutma kapasitesi [kW]
- `Çalışma_saati`: Yıllık chiller çalışma süresi [saat/yıl]
- `Ort_yük`: Ortalama yük oranı (0-1 arası)
- `COP_mevcut`: Mevcut ortalama COP
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap
- 600 kW chiller, 3,500 saat/yıl, ortalama %55 yük
- Sabit CHW setpoint: 7°C → Yıllık ağırlıklı ortalama artış: 2°C (ortalama 9°C)
- Mevcut COP: 5.2
- Elektrik fiyatı: €0.12/kWh
- Yatırım: €3,000 (BMS programlama + sensörler)

```
COP_iyileşme_ort = 2.5 × 2 = %5
Yıllık_chiller_enerji = 600 × 3,500 × 0.55 / 5.2 = 222,115 kWh
Yıllık_tasarruf_kWh = 222,115 × 5 / 100 = 11,106 kWh
Yıllık_tasarruf_EUR = 11,106 × 0.12 = €1,333/yıl
Geri_ödeme = 3,000 / 1,333 = 2.25 yıl
```

- **Geri ödeme süresi: ~2.3 yıl**

*Not: Eğer mevcut BMS CHW reset programlamayı destekliyorsa (ek yatırım ~€500), geri ödeme süresi yaklaşık 4.5 aya düşer.*

## Uygulama Adımları

1. **Mevcut kontrol stratejisi analizi:** Mevcut CHW setpoint'ini, kontrol yöntemini ve BMS yeteneklerini belirle. CHW sıcaklık ve yük profilini en az 2 hafta kaydet
2. **AHU/FCU kapasite değerlendirmesi:** Her AHU/FCU'nun yükseltilmiş CHW sıcaklığında yeterli kapasiteye sahip olup olmadığını kontrol et. Serpantin seçim verilerini incele
3. **Nem gereksinimlerini belirle:** Nem kontrolü gereken alanları tanımla ve CHW reset üst limitini bu gereksinimlere göre ayarla
4. **Reset stratejisi seçimi:** Yük bazlı, dış hava bazlı veya kombinasyon stratejisi arasında karar ver. Dış hava bazlı daha basittir ancak yük bazlı daha doğrudur
5. **BMS programlama:** Reset algoritmasını BMS'te programla. Minimum ve maximum CHW setpoint'lerini, reset eğrisini ve güvenlik kilitlelerini tanımla
6. **Kademeli devreye alma:** İlk aşamada dar reset aralığı (1-2°C) ile başla. İç ortam koşullarını (sıcaklık, nem) izleyerek sorun olmadığını doğrula
7. **Optimizasyon:** 2-4 hafta boyunca veri toplayarak reset aralığını kademeli olarak genişlet. İç ortam konfor şikayetlerini takip et
8. **Performans doğrulama:** Reset öncesi ve sonrası chiller enerji tüketimini karşılaştır. COP iyileşmesini ölç ve raporla

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yetersiz nem alma (dehumidification) | CHW sıcaklığı çok yükseltilirse AHU serpantininde yeterli nem alınamaz | Nem kontrollü üst limit tanımla; nem sensörleri ile izle |
| Serpantin kapasite yetersizliği | Yüksek CHW sıcaklığında AHU/FCU yeterli soğutma sağlayamaz | AHU kapasitesini önceden kontrol et; vana tam açık alarmı kur |
| Konfor şikayeti | İç ortam sıcaklık/nem hedefi tutturulamaz | Kademeli devreye alma; şikayet bazlı üst limit ayarı |
| Ani yük artışı | Reset durumunda CHW sıcaklığı yüksekken ani yük artışında yetersiz soğutma | Hızlı geri dönüş (fast recovery) algoritması; rampa hızını ayarla |
| Kontrol kararsızlığı | Reset ve chiller kapasite kontrolü arasında kararsızlık (hunting/oscillation) | Yeterli ölü bant (deadband) tanımla; rampa hızını sınırla |
| Proses alanları | Bazı alanlar sabit düşük CHW sıcaklığı gerektirir | Proses alanlarını ayrı CHW devresine al veya reset'ten muaf tut |
| Veri yetersizliği | Yük ölçümü yoksa yük bazlı reset uygulanamaz | Dış hava bazlı reset ile başla; debimetre yatırımı planla |

## İlgili Dosyalar
- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller VSD çözümü: `solutions/chiller_vsd.md`
- Kondenser optimizasyonu: `solutions/chiller_condenser_optimization.md`
- Serbest soğutma: `solutions/chiller_free_cooling.md`
- Chiller sıralama optimizasyonu: `solutions/chiller_sequencing.md`
- Chiller exergy formülleri: `formulas/chiller_exergy.md`

## Referanslar
- ASHRAE Handbook — HVAC Applications, "Supervisory Control Strategies and Optimization"
- ASHRAE Guideline 36, "High-Performance Sequences of Operation for HVAC Systems"
- ASHRAE Standard 90.1, "Energy Standard for Buildings Except Low-Rise Residential Buildings"
- DOE/FEMP, "Chiller Management Best Practices"
- Taylor, S.T., "Optimizing Design & Control of Chilled Water Plants," ASHRAE Journal
- Hartman, T., "All-Variable Speed Centrifugal Chiller Plants," ASHRAE Journal
- BSRIA, "Rules of Thumb — Guidelines for Building Services" 5th Edition
- Carrier/Trane/York, "Application Guide — Chilled Water Temperature Reset"
