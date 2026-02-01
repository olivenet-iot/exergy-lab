# Çözüm: Serbest Soğutma — Free Cooling (Economizer)

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Birçok tesiste chiller'lar yıl boyunca çalıştırılır — dış hava sıcaklığı yeterince düşük olduğunda bile. Kış ve geçiş mevsimlerinde dış ortam koşulları doğrudan soğutma sağlamaya uygun olmasına rağmen, chiller kompresörleri gereksiz yere enerji tüketmeye devam eder.

**Çözüm:** Dış hava sıcaklığı yeterince düşük olduğunda, dış havayı doğrudan (airside economizer) veya soğutma kulesi suyunu bir ısı eşanjörü üzerinden (waterside economizer) kullanarak chiller'ı bypass etmek. Bu yöntemle kompresör enerjisi tamamen veya büyük ölçüde elimine edilir.

**Tipik Tasarruf:** %10-40 (iklim bölgesine bağlı, yıllık chiller enerji tüketiminde)
**Tipik ROI:** 2-5 yıl

## Çalışma Prensibi

Serbest soğutma, dış ortam koşulları uygun olduğunda mekanik soğutma (kompresör) yerine doğal soğutma kaynaklarını kullanır. İki temel yöntem vardır:

### 1. Hava Taraflı Serbest Soğutma (Airside Economizer)

Dış hava doğrudan bina içine alınarak soğutma sağlanır:
- **Kuru termometre kontrolü:** Dış hava sıcaklığı < dönüş havası sıcaklığı olduğunda
- **Entalpi kontrolü:** Dış hava entalpisi < dönüş havası entalpisi olduğunda (nemli iklimlerde daha doğru)
- **Karışık mod:** Kısmi serbest soğutma + kısmi mekanik soğutma kombinasyonu
- **Uygulama alanı:** Genellikle AHU bazlı sistemlerde, veri merkezlerinde

### 2. Su Taraflı Serbest Soğutma (Waterside Economizer)

Soğutma kulesi suyu bir ısı eşanjörü (plate HX) üzerinden CHW devresine aktarılarak chiller bypass edilir:
- **Plaka eşanjör (Plate HX):** Kule suyu ile CHW arasında ısı transferi sağlar
- **Strainer cycle:** Kule suyu doğrudan CHW devresine gönderilir (su arıtma gerekli)
- **Kısmi serbest soğutma:** Kule suyu CHW'yi tam olarak soğutamıyorsa, ön soğutma + chiller kombinasyonu

### Waterside Economizer Şeması

```
Tam Serbest Soğutma Modu (Chiller bypass):
  Soğutma Kulesi → Kule Suyu → Plaka HX → CHW (soğutulmuş)
                                          → Chiller KAPALI

Kısmi Serbest Soğutma Modu:
  Soğutma Kulesi → Kule Suyu → Plaka HX → CHW (ön soğutulmuş) → Chiller (ek soğutma)

Normal Mod (Serbest soğutma yok):
  Soğutma Kulesi → Kule Suyu → Chiller Kondenser → CHW
                                                   → Plaka HX BYPASS
```

### Geçiş Sıcaklıkları ve Switchover Mantığı

```
T_kule_çıkış < CHW_setpoint + ΔT_HX → Tam serbest soğutma
T_kule_çıkış < CHW_dönüş - Histerez → Kısmi serbest soğutma
T_kule_çıkış > CHW_dönüş → Normal mod (serbest soğutma yok)
```

Burada:
- `T_kule_çıkış`: Soğutma kulesi çıkış suyu sıcaklığı [°C]
- `CHW_setpoint`: Soğutma suyu çıkış sıcaklık hedefi [°C]
- `ΔT_HX`: Plaka eşanjör yaklaşım sıcaklığı [°C] (tipik: 1-2°C)
- `CHW_dönüş`: Soğutma suyu dönüş sıcaklığı [°C]
- `Histerez`: Kontrol histerez değeri [°C] (tipik: 1-2°C)

## Airside vs Waterside Karşılaştırma

| Faktör | Airside Economizer | Waterside Economizer |
|--------|-------------------|---------------------|
| Prensip | Dış havayı doğrudan bina içine alma | Kule suyu ile CHW arasında HX |
| Uygulama alanı | AHU sistemleri, veri merkezleri | Merkezi chiller tesisleri |
| Yatırım maliyeti | Düşük-orta (damper + kontrol) | Orta-yüksek (HX + boru + kontrol) |
| Bakım | Düşük (filtre + damper) | Orta (HX temizlik + su arıtma) |
| Nem kontrolü | Zor (nemli iklimlerde sınırlı) | Etkilemez (CHW kapalı devre) |
| Hava kalitesi etkisi | Doğrudan (filtre kritik) | Etkilemez |
| Enerji tasarrufu | Yüksek (fan enerjisi düşük) | Yüksek (kule fan + pompa enerjisi) |
| Uygun iklim | Kuru, serin iklimler (kuru termometre düşük) | Tüm iklimler (yaş termometre düşük yeterli) |
| Retrofit kolaylığı | Zor (AHU modifikasyonu) | Kolay (boru bağlantısı) |

## İklim Bölgesi Potansiyel Tablosu

| İklim Bölgesi / Şehir | Yıllık Serbest Soğutma Saati | Serbest Soğutma Potansiyeli | Tipik Enerji Tasarrufu |
|------------------------|-----------------------------|-----------------------------|------------------------|
| İstanbul | 1,500-2,500 saat | %10-25 | %10-20 |
| Ankara | 2,000-3,000 saat | %15-30 | %15-25 |
| İzmir | 1,000-1,800 saat | %8-18 | %8-15 |
| Kuzey Avrupa (Londra, Amsterdam) | 3,500-5,000 saat | %30-50 | %30-45 |
| Orta Avrupa (Berlin, Viyana) | 3,000-4,500 saat | %25-45 | %25-40 |
| Güney Avrupa (Roma, Madrid) | 1,500-2,500 saat | %12-25 | %10-20 |
| Kuzey Amerika — Kuzey (Chicago, Toronto) | 3,000-4,500 saat | %25-45 | %25-40 |
| Orta Doğu (Dubai, Riyad) | 200-500 saat | %2-5 | %2-5 |

*Not: Değerler waterside economizer için tipik CHW setpoint'i 7°C ve 24 saat/7 gün çalışma esasına göre hesaplanmıştır. Gerçek tasarruf çalışma saatlerine ve yük profiline bağlıdır.*

## Waterside Economizer Tasarım Parametreleri

### Plaka Eşanjör Boyutlandırma

| Parametre | Tipik Değer | Açıklama |
|-----------|------------|----------|
| Yaklaşım sıcaklığı (approach) | 1-2°C | Kule suyu çıkış ile CHW çıkış farkı |
| Fouling faktörü | 0.044 m²·K/kW | Kule suyu tarafı (açık devre) |
| Basınç kaybı (CHW tarafı) | 30-70 kPa | Pompa ek enerji tüketimi |
| Basınç kaybı (kule suyu tarafı) | 30-70 kPa | Kule pompası ek enerji tüketimi |
| Plaka malzemesi | AISI 316L paslanmaz çelik | Korozyon direnci |
| Conta malzemesi | EPDM veya NBR | Sıcaklık ve kimyasal uyumluluk |

### Switchover Sıcaklıkları (İstanbul Örneği)

| Mod | Koşul | Kule Suyu Çıkış (°C) | Dönem |
|-----|-------|----------------------|-------|
| Tam serbest soğutma | T_kule < 9°C | <9 | Aralık-Şubat |
| Kısmi serbest soğutma | 9°C < T_kule < 14°C | 9-14 | Kasım, Mart-Nisan |
| Normal mod (chiller) | T_kule > 14°C | >14 | Mayıs-Ekim |

## Strainer Cycle (Doğrudan Kule Suyu Kullanımı)

Plaka eşanjör yerine kule suyu doğrudan CHW devresine yönlendirilir:

| Avantaj | Dezavantaj |
|---------|-----------|
| HX maliyeti yok | Su arıtma kritik — CHW devresine kule suyu girer |
| Daha düşük yaklaşım sıcaklığı | Korozyon ve kirlenme riski yüksek |
| Basit boru tesisatı | Strainer (süzgeç) bakımı gerekli |
| Daha yüksek verimlilik | CHW devresi kontaminasyon riski |

**Önerilen durum:** Yalnızca su kalitesinin çok iyi kontrol edilebildiği tesislerde ve uygun strainer/filtre sistemi ile birlikte uygulanmalıdır.

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Tesiste yılın önemli bir kısmında soğutma gereksinimi olan sistemler (veri merkezi, 7/24 proses soğutma)
- Serin iklim bölgelerinde (yıllık ortalama sıcaklık <18°C)
- Mevcut soğutma kulesi kapasitesinde yedek kapasite varsa
- CHW sıcaklık reset uygulanabiliyorsa (yüksek CHW setpoint → serbest soğutma saatlerini artırır)
- Tesisin yıllık chiller enerji maliyeti >€20,000 ise

### Ne Zaman Uygulanmamalı
- Sıcak ve nemli iklimlerde serbest soğutma saatleri çok düşükse (<500 saat/yıl)
- Chiller tesisi sadece yaz aylarında çalışıyorsa (serbest soğutma dönemi ile çakışma yok)
- Su kalitesi çok kötü ve su arıtma maliyeti yüksekse (strainer cycle için)
- Mevcut mekanik dairede HX ve boru tesisatı için yeterli alan yoksa

## Yatırım Maliyeti

| Kalem | Maliyet Aralığı (€) | Açıklama |
|-------|---------------------|----------|
| Plaka eşanjör (100-300 kW) | 5,000-15,000 | Kapasiteye göre boyutlandırılmış |
| Plaka eşanjör (300-1,000 kW) | 15,000-35,000 | Orta-büyük tesis |
| Plaka eşanjör (1,000-3,000 kW) | 35,000-50,000 | Büyük tesis |
| Boru tesisatı ve vanalar | 5,000-20,000 | Bağlantı boruları, izolasyon, vanalar |
| Kontrol sistemi (BMS entegrasyonu) | 5,000-15,000 | Sensörler, motorlu vanalar, programlama |
| Pompa güncelleme (gerekirse) | 3,000-10,000 | HX basınç kaybını karşılama |
| Strainer/filtre sistemi (strainer cycle) | 2,000-8,000 | Strainer cycle tercih edilirse |
| Devreye alma ve test | 2,000-5,000 | Modlar arası geçiş testi |
| **Toplam waterside economizer projesi** | **20,000-80,000** | **Tesis boyutuna bağlı** |

| Kalem (Airside) | Maliyet Aralığı (€) | Açıklama |
|-----------------|---------------------|----------|
| Damper sistemi (AHU başına) | 2,000-5,000 | Motorlu dış hava/egzoz damperleri |
| Dış hava sensörleri | 500-1,500 | Sıcaklık, nem, entalpi sensörleri |
| BMS programlama | 2,000-8,000 | Economizer modu kontrol yazılımı |
| Filtreleme güncelleme | 1,000-5,000 | Dış hava kalitesine göre filtre iyileştirme |
| **Toplam airside economizer (AHU başına)** | **5,000-15,000** | **AHU boyutuna bağlı** |

## ROI Hesabı

### Formül (Waterside Economizer)
```
Serbest_soğutma_saati = Yıllık T_kule < (CHW_setpoint + ΔT_HX) olan saat sayısı
Chiller_tasarruf_kWh = Ort_chiller_güç × Serbest_soğutma_saati
Kule_fan_ek_enerji = Kule_fan_güç × Serbest_soğutma_saati × Ek_fan_yüzdesi
HX_pompa_ek_enerji = HX_pompa_güç × Serbest_soğutma_saati
Net_tasarruf_kWh = Chiller_tasarruf_kWh - Kule_fan_ek_enerji - HX_pompa_ek_enerji
Yıllık_tasarruf_EUR = Net_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

Burada:
- `Serbest_soğutma_saati`: Yıllık serbest soğutma modu süresi [saat/yıl]
- `Ort_chiller_güç`: Chiller ortalama elektrik tüketimi [kW]
- `Kule_fan_güç`: Soğutma kulesi fan gücü [kW]
- `Ek_fan_yüzdesi`: Serbest soğutma modunda ek fan çalışma yüzdesi [%]
- `HX_pompa_güç`: HX devresi ek pompa gücü [kW]
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap (İstanbul — Waterside Economizer)
- 1,000 kW chiller tesisi, 6,000 saat/yıl soğutma gereksinimi
- Ortalama chiller elektrik tüketimi: 180 kW
- Serbest soğutma potansiyeli: 1,800 saat/yıl (tam + kısmi)
- Kule fan ek enerji: 25 kW × 1,800 saat = 45,000 kWh
- HX pompa ek enerji: 8 kW × 1,800 saat = 14,400 kWh
- Elektrik fiyatı: €0.12/kWh
- Yatırım: €45,000 (HX + boru + kontrol)

```
Chiller_tasarruf = 180 × 1,800 = 324,000 kWh
Net_tasarruf = 324,000 - 45,000 - 14,400 = 264,600 kWh
Yıllık_tasarruf_EUR = 264,600 × 0.12 = €31,752/yıl
Geri_ödeme = 45,000 / 31,752 = 1.42 yıl
```

- **Geri ödeme süresi: ~1.4 yıl**

*Not: İstanbul'da serbest soğutma potansiyeli orta düzeydedir. Kuzey Avrupa iklimlerinde geri ödeme süresi 1 yılın altına düşebilir.*

## Uygulama Adımları

1. **İklim analizi:** Tesisin bulunduğu lokasyon için saatlik dış hava sıcaklık ve yaş termometre verilerini analiz et. TMY (Typical Meteorological Year) verileri kullan
2. **Serbest soğutma saati hesabı:** CHW setpoint'i ve HX yaklaşım sıcaklığına göre yıllık serbest soğutma saatlerini hesapla. Bin-saat analizi yap
3. **CHW reset entegrasyonu:** CHW sıcaklık reset stratejisi ile serbest soğutma kombinasyonunu değerlendir (yüksek CHW setpoint → daha fazla serbest soğutma saati)
4. **Ekipman boyutlandırma:** Plaka eşanjör, boru, vana ve pompa boyutlandırmasını yap. HX yaklaşım sıcaklığını 1-2°C hedefle
5. **Soğutma kulesi kapasite kontrolü:** Mevcut soğutma kulesinin serbest soğutma modunda yeterli kapasiteye sahip olduğunu doğrula
6. **Kontrol stratejisi tasarımı:** Tam serbest soğutma, kısmi serbest soğutma ve normal mod arasındaki geçiş mantığını, histerez değerlerini ve güvenlik kilitlelerini tanımla
7. **Mekanik kurulum:** HX, boru tesisatı, motorlu vanalar, izolasyon ve enstrümantasyonu monte et
8. **Devreye alma ve test:** Her çalışma modunu ayrı ayrı test et; mod geçişlerinin sorunsuz olduğunu doğrula
9. **Donma koruması:** Kış koşullarında donma riskine karşı by-pass vanası, glikol veya elektrik ısıtıcı önlemlerini al
10. **Performans izleme:** İlk yıl boyunca serbest soğutma saatlerini, enerji tasarrufunu ve sistem performansını izle ve raporla

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Su kalitesi (waterside) | Kule suyu açık devredir; HX'te kirlenme ve korozyon riski | Plaka HX düzenli temizlik; su arıtma programı; strainer cycle'da ek filtreleme |
| Donma koruması | Kış aylarında kule suyu ve HX'te donma riski | Glikol sistemi, elektrikli ısıtıcı, donma termostadı ile acil kapatma |
| Kontrol karmaşıklığı | Üç modlu çalışma (tam/kısmi/normal) karmaşık kontrol gerektirir | Kapsamlı BMS programlama, yeterli histerez, modlar arası yumuşak geçiş |
| Legionella (waterside) | Düşük sıcaklıklarda kule suyunda Legionella riski artabilir | Düzenli biyosit dozlama, su sıcaklığı izleme, yıllık Legionella testi |
| Yetersiz kule kapasitesi | Serbest soğutma modunda kule kapasitesi yetersiz kalabilir | Kule kapasitesini önceden doğrula; gerekirse kule iyileştirme/büyütme |
| Hava kalitesi (airside) | Dış hava kalitesi düşükse iç ortam etkilenir | Yüksek verimli filtreleme (MERV 13+), hava kalitesi sensörleri |
| Nem kontrolü (airside) | Nemli iklimlerde dış hava nem alma yükünü artırır | Entalpi kontrolü kullan; nem sensörleri ile switchover |
| HX basınç kaybı | Ek basınç kaybı pompa enerjisini artırır | HX boyutlandırmada düşük basınç kaybı hedefle; VSD pompa kullan |

## İlgili Dosyalar
- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller VSD çözümü: `solutions/chiller_vsd.md`
- Kondenser optimizasyonu: `solutions/chiller_condenser_optimization.md`
- Soğutma suyu sıcaklık reset: `solutions/chiller_chilled_water_reset.md`
- Chiller sıralama optimizasyonu: `solutions/chiller_sequencing.md`
- Chiller exergy formülleri: `formulas/chiller_exergy.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment, "Air-Side Economizers" and "Waterside Economizers" chapters
- ASHRAE Standard 90.1, "Energy Standard for Buildings — Economizer Requirements"
- ASHRAE Guideline 36, "High-Performance Sequences of Operation for HVAC Systems"
- DOE/FEMP, "Best Practices for Chiller Plant Operation — Free Cooling"
- Trane Engineering Newsletter, "Waterside Economizer Application Guide"
- Carrier, "Application Guide — Free Cooling Systems"
- BSRIA, "Free Cooling Design Guide"
- Eurovent, "Guideline for Free Cooling — Chiller Systems"
- CIBSE Guide B, "Heating, Ventilating, Air Conditioning and Refrigeration" — Free Cooling Section
