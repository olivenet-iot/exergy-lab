---
title: "Çözüm: Chiller Bakım ve Performans İyileştirme — Chiller Maintenance and Performance Improvement"
category: solutions
equipment_type: chiller
keywords: [bakım, chiller, izleme, performans]
related_files: [chiller/audit.md, chiller/benchmarks.md, chiller/solutions/condenser_optimization.md]
use_when: ["Chiller bakım programı önerilirken", "Performans izleme sistemi kurulurken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Chiller Bakım ve Performans İyileştirme — Chiller Maintenance and Performance Improvement

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Bakımı ihmal edilen chiller (soğutma grubu) sistemlerinde COP (Coefficient of Performance) zamanla %10-30 oranında düşer. Kirli kondenser ve evaporatör boruları, yetersiz soğutucu akışkan şarjı, yağ birikimi ve kontrol arızaları en yaygın performans düşüşü nedenleridir. Bir chiller'ın toplam yaşam döngüsü maliyetinin %70-80'i enerji tüketimine aittir; bu nedenle küçük verimlilik kayıpları bile büyük enerji maliyetlerine yol açar.

**Çözüm:** Sistematik önleyici (preventive) bakım programı uygulamak. Kondenser ve evaporatör boru temizliği, soğutucu akışkan şarj kontrolü, yağ yönetimi, purge ünitesi bakımı, titreşim analizi ve elektriksel denetim ile chiller performansını tasarım değerlerinde tutmak.

**Tipik Tasarruf:** %5-15 (enerji tüketiminde azalma)
**Tipik ROI:** <1 yıl

## Çalışma Prensibi

Chiller bakım programı, performans düşüşüne neden olan faktörleri sistematik olarak kontrol altında tutar:

- **Kondenser boru temizliği:** Kondenser borularında biriken kireç, alg ve biyofilm tabakası ısı transfer direncini artırır (fouling factor). Her 0.001 m²·K/W fouling artışı, chiller COP değerini yaklaşık %2-3 düşürür
- **Evaporatör boru temizliği:** Evaporatör tarafında da benzer kirlenme ısı transferini engeller ve suction basıncının düşmesine neden olur
- **Soğutucu akışkan şarj kontrolü:** Eksik şarj düşük evaporatör basıncına, fazla şarj yüksek kondenser basıncına yol açar; her iki durum da COP'u düşürür
- **Yağ yönetimi:** Kompresör yağı zamanla evaporatör ve kondenser borularına sızar; boru iç yüzeyinde yağ filmi ısı transferini %5-10 azaltabilir
- **Purge ünitesi:** Düşük basınçlı chiller'larda (R-123, R-1233zd) hava ve nem sızıntısı kondenser basıncını artırır; purge ünitesi bu gazları uzaklaştırır
- **Titreşim analizi:** Kompresör rulmanları, dişli takımları ve motor arızalarının erken tespiti ile plansız duruşları önler

### Performans Düşüşü Nedenleri ve Etkileri

| Neden | COP Düşüşü | Etki Mekanizması |
|-------|------------|------------------|
| Kirli kondenser boruları | %2-10 | Yüksek kondenser basıncı, artan kompresör işi |
| Kirli evaporatör boruları | %2-8 | Düşük evaporatör basıncı, artan kompresör işi |
| Eksik soğutucu akışkan şarjı (%10) | %5-10 | Düşük evaporatör kapasitesi, düşük suction basıncı |
| Fazla soğutucu akışkan şarjı (%10) | %3-7 | Yüksek kondenser basıncı, sıvı taşması riski |
| Yağ birikimi (evaporatörde) | %2-5 | Isı transfer yüzeyinde yalıtım etkisi |
| Hava sızıntısı (düşük basınçlı tip) | %3-8 | Yoğuşmayan gaz kondenser basıncını artırır |
| Aşınmış kompresör parçaları | %5-15 | Düşük kompresyon verimi, iç kaçak |
| Yanlış superheat/subcooling ayarı | %2-6 | Optimum olmayan çevrim koşulları |

## Kondenser ve Evaporatör Boru Temizliği

### Online Temizlik (Sistem Çalışırken)

Online boru temizleme sistemleri, chiller çalışırken sürekli veya periyodik temizlik sağlar:

- **Sünger top (sponge ball) sistemi:** Yüzer sünger toplar su akışı ile borulardan geçerek yumuşak birikintileri temizler (ör. Taprogge, Eqobrush)
- **Fırça sistemi:** Her borunun iki ucuna yerleştirilen fırçalar, akış yönü değiştirilerek ileri-geri hareket eder
- **Avantaj:** Kesintisiz çalışma, sürekli temiz boru, enerji tasarrufu
- **Dezavantaj:** Yüksek ilk yatırım (€10,000-50,000), mekanik parça bakımı

### Offline Temizlik (Sistem Durdurularak)

- **Mekanik temizlik:** Fırça, rotary cleaner veya su jeti ile boru iç yüzeyi temizlenir
- **Kimyasal temizlik:** Asidik (inhibitörlü hidroklorik asit) veya organik çözücüler ile kireç ve mineral birikinti çözülür
- **Sıklık:** Yılda 1-2 kez (su kalitesine bağlı)
- **Maliyet:** €2,000-8,000 per sefer (chiller kapasitesine göre)

### Fouling Factor Etkileri

| Fouling Factor (m²·K/W) | Durum | COP Kaybı | Kapasite Kaybı |
|--------------------------|-------|-----------|----------------|
| 0.000044 | Temiz (tasarım değeri) | %0 (referans) | %0 |
| 0.000088 | Hafif kirli | %2-3 | %3-5 |
| 0.000176 | Orta kirli | %5-8 | %8-12 |
| 0.000352 | Çok kirli | %10-15 | %15-25 |
| 0.000500+ | İhmal edilmiş | %15-25 | %25-40 |

## Soğutucu Akışkan Şarj Kontrolü

Soğutucu akışkan şarjının doğru miktarda olması chiller performansı için kritiktir:

- **Subcooling kontrolü:** Kondenser çıkışında sıvı subcooling değeri 3-6°C olmalıdır (R-134a, R-1234ze). Düşük subcooling eksik şarjı, yüksek subcooling fazla şarjı gösterir
- **Superheat kontrolü:** Evaporatör çıkışında superheat değeri 3-8°C olmalıdır. Yüksek superheat eksik şarjı gösterir
- **Sight glass kontrolü:** Sıvı hattındaki sight glass'ta kabarcık (bubble) görünümü eksik şarj belirtisidir
- **Kaçak testi:** Yıllık kaçak testi zorunludur (F-gaz yönetmeliği). Elektronik kaçak dedektörü veya UV boya yöntemi kullanılır
- **Nem kontrolü:** Sıvı hattı filtre-dryer nem göstergesi yeşil (kuru) olmalıdır; sarı veya kahverengi renk nem kirliliğini gösterir

## Yağ Yönetimi ve Yağ Geri Dönüşü

- **Yağ seviyesi kontrolü:** Kompresör yağ seviyesi sight glass aralığında tutulmalıdır
- **Yağ analizi:** Yıllık yağ numunesi analizi: asit sayısı (TAN), nem içeriği, metal parçacıklar ve viskozite
- **Yağ geri dönüş sistemi:** Evaporatör ve kondenserde biriken yağın kompresöre geri döndürülmesi
- **Yağ değişimi:** Analiz sonuçlarına göre veya 3-5 yılda bir (tam değişim)
- **Uygun yağ seçimi:** Soğutucu akışkan uyumlu yağ kullanılmalıdır (POE yağ: R-134a, R-1234ze; mineral yağ: R-123)

## Purge Ünitesi (Düşük Basınçlı Chiller'lar)

R-123 ve R-1233zd soğutucu akışkanlı düşük basınçlı santrifüj chiller'larda evaporatör basıncı atmosfer basıncının altındadır; bu nedenle hava ve nem sızıntısı oluşur:

- **Hava etkisi:** Yoğuşmayan gaz (NCG) kondenser basıncını artırır, COP düşer
- **Nem etkisi:** Su, soğutucu akışkan ile reaksiyona girerek asit oluşturur, motor yalıtımını ve boru yüzeylerini aşındırır
- **Purge ünitesi çalışma prensibi:** Kondenserdeki yoğuşmayan gazları toplar ve dışarı atar; soğutucu akışkanı geri kazanır
- **Purge sayacı takibi:** Günlük purge sayısı trendi, sızıntı oranını gösterir; artış contaları ve sızıntı noktalarını gösterir
- **Hedef:** Günlük purge sayısı <5 (iyi durumda), >20 ise sızıntı araştırması gerekli

## Titreşim Analizi

Kompresör rulman ve dişli takımı arızalarının erken tespiti için titreşim analizi yapılır:

- **Ölçüm noktaları:** Kompresör ana rulmanlar, motor NDE/DE rulmanlar, dişli kutusu
- **Parametreler:** Toplam titreşim (mm/s rms), frekans spektrumu, zarf analizi (envelope)
- **Alarm seviyeleri (ISO 10816):** İyi <2.8 mm/s, Uyarı 2.8-7.1 mm/s, Alarm >7.1 mm/s
- **Sıklık:** 3 ayda bir veya sürekli izleme
- **Fayda:** Plansız duruşu %60-80 azaltır, büyük arıza maliyetinden kaçınılır

## Elektriksel Denetim

| Denetim Kalemi | Sıklık | Açıklama |
|----------------|--------|----------|
| Motor akım çekimi | Aylık | Nominal akımın %90-105'i arasında olmalı |
| Motor yalıtım direnci (megger) | Yıllık | Minimum 50 MΩ (yeni), 5 MΩ (uyarı), 2 MΩ (kritik) |
| Kontaktör kontakları | 6 aylık | Çukurlaşma, aşınma, ark izleri kontrol |
| Kablo bağlantıları | Yıllık | Gevşek bağlantı, ısınma kontrolü (IR termometre) |
| Koruma röleleri | Yıllık | Trip ayarları ve fonksiyon testi |
| Starter ve VSD | 6 aylık | Fan, kapasitör, bağlantı kontrolü |

## Performans Bozulma Önleme Kontrol Listesi

| Kontrol | Sıklık | Kabul Kriteri | Sapma Durumunda |
|---------|--------|---------------|-----------------|
| Kondenser yaklaşım sıcaklığı | Haftalık | <2°C (tasarım) | Boru temizliği planlama |
| Evaporatör yaklaşım sıcaklığı | Haftalık | <2°C (tasarım) | Boru temizliği planlama |
| Kompresör akım çekimi | Aylık | ±%5 nominal | Motor ve yük kontrolü |
| Yağ seviyesi | Haftalık | Sight glass aralığında | Yağ ekleme, kaçak kontrolü |
| Soğutucu akışkan şarjı | Aylık | Subcooling 3-6°C | Şarj düzeltme, kaçak testi |
| Purge sayısı (düşük basınçlı) | Günlük | <5/gün | Sızıntı noktası arama |
| Titreşim seviyesi | 3 aylık | <2.8 mm/s | Rulman/dişli takımı kontrolü |
| Su kalitesi (kondenser) | Aylık | İletkenlik <1500 µS/cm | Su arıtma dozajı ayarı |

## Yıllık Bakım Programı

| Dönem | İşlem | Sorumlu |
|-------|-------|---------|
| Her hafta | COP hesaplama, yaklaşım sıcaklığı trendi, yağ seviyesi | Operatör |
| Her ay | Akım ölçümü, soğutucu akışkan şarj kontrolü, su kalitesi | Teknisyen |
| Her 3 ay | Titreşim analizi, kontrol sensör kalibrasyonu | Bakım mühendisi |
| Her 6 ay | Elektriksel denetim, kontaktör bakımı, güvenlik testi | Elektrik teknisyeni |
| Yılda 1 kez (sezon öncesi) | Kondenser boru temizliği, evaporatör kontrolü, yağ analizi | Yetkili servis |
| Yılda 1 kez | Kaçak testi, purge ünitesi bakımı, filtre-dryer kontrolü | Yetkili servis |
| Her 3-5 yıl | Yağ değişimi, kompresör genel bakım, motor yalıtım testi | Yetkili servis / üretici |

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı

- Chiller COP değeri tasarım değerinin %10'dan fazla altına düşmüşse
- Kondenser yaklaşım sıcaklığı >3°C ise (kirli boru belirtisi)
- Evaporatör yaklaşım sıcaklığı >2°C ise
- Son 12 ayda kapsamlı bakım yapılmamışsa
- Enerji tüketiminde açıklanamayan artış gözleniyorsa
- Chiller yaşı >5 yıl ve bakım geçmişi yetersizse
- Kompresörde anormal titreşim veya gürültü varsa
- Purge ünitesi sık çalışıyorsa (düşük basınçlı tipler)

### Ne Zaman Uygulanmamalı

- Chiller ömrünün sonuna yaklaşmışsa ve değişim planlanıyorsa (bakım yerine değişim)
- Yıllık çalışma süresi çok düşükse (<1,000 saat)
- Chiller zaten düzenli bakım altındaysa ve COP tasarım değerinde ise

## Yatırım Maliyeti

| Bakım Kalemi | Maliyet (€) | Açıklama |
|--------------|-------------|----------|
| Yıllık bakım sözleşmesi (200-500 kW) | 5,000-10,000 | Üretici yetkili servis |
| Yıllık bakım sözleşmesi (500-2,000 kW) | 10,000-20,000 | Kapsamlı sözleşme |
| Kondenser boru temizliği (offline) | 2,000-8,000 | Kapasite ve kirlilik durumuna göre |
| Online boru temizleme sistemi | 10,000-50,000 | Tek seferlik yatırım |
| Soğutucu akışkan şarj düzeltme | 500-5,000 | Akışkan miktarı ve tipine göre |
| Yağ değişimi | 1,000-5,000 | Kompresör kapasitesine göre |
| Titreşim analizi hizmeti | 500-2,000 | Yıllık 4 ölçüm |
| Filtre-dryer değişimi | 300-1,500 | Tip ve boyuta göre |
| Purge ünitesi bakımı | 500-2,000 | Düşük basınçlı tipler |

## ROI Hesabı

### Formül

```
COP_mevcut = Q_evap / W_comp (mevcut performans)
COP_hedef = COP_tasarım × 0.95 (bakım sonrası hedef)
Enerji_tasarrufu_kW = Q_soğutma × (1/COP_mevcut - 1/COP_hedef)
Yıllık_tasarruf_kWh = Enerji_tasarrufu_kW × Çalışma_saati
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Bakım_maliyeti / Yıllık_tasarruf_EUR
```

Burada:
- `COP_mevcut`: Bakım öncesi mevcut COP değeri [-]
- `COP_hedef`: Bakım sonrası hedeflenen COP değeri [-]
- `Q_soğutma`: Chiller soğutma kapasitesi [kW]
- `W_comp`: Kompresör elektrik tüketimi [kW]
- `Çalışma_saati`: Yıllık eşdeğer tam yük çalışma süresi [saat/yıl]
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap

- 1,000 kW soğutma kapasiteli santrifüj chiller
- Tasarım COP: 6.0, Mevcut COP: 4.5 (bakımsızlık nedeniyle düşmüş)
- Hedef COP (bakım sonrası): 5.7
- Yıllık eşdeğer tam yük çalışma: 3,000 saat
- Elektrik fiyatı: €0.12/kWh

```
Mevcut_güç = 1,000 / 4.5 = 222.2 kW
Hedef_güç = 1,000 / 5.7 = 175.4 kW
Enerji_tasarrufu = 222.2 - 175.4 = 46.8 kW
Yıllık_tasarruf_kWh = 46.8 × 3,000 = 140,400 kWh
Yıllık_tasarruf_EUR = 140,400 × 0.12 = €16,848/yıl
```

- Yıllık bakım sözleşme maliyeti: €12,000
- **Geri ödeme süresi: 12,000 / 16,848 = 0.71 yıl (yaklaşık 8.5 ay)**

**Not:** Bakım sayesinde ayrıca plansız duruşlar azalır, kompresör ömrü uzar ve soğutucu akışkan kayıpları önlenir; bu dolaylı faydalar hesaba dahil değildir.

## Uygulama Adımları

1. **Mevcut performans tespiti:** Chiller COP değerini ölç (Q_evap, W_comp), tasarım değeri ile karşılaştır. Kondenser ve evaporatör yaklaşım sıcaklıklarını kaydet
2. **Bakım geçmişi incelemesi:** Son bakım kayıtlarını gözden geçir, eksik ve gecikmiş bakım kalemlerini belirle
3. **Kondenser boru temizliği:** Su tarafı boruları mekanik veya kimyasal yöntemle temizle, fouling factor değerini düşür
4. **Evaporatör kontrolü:** Evaporatör boru yüzeylerini kontrol et, gerekirse temizlik yap
5. **Soğutucu akışkan şarj kontrolü:** Subcooling ve superheat değerlerini ölç, gerekirse şarj düzelt
6. **Yağ analizi ve yağ geri dönüşü:** Yağ numunesi al, analiz yaptır; evaporatör ve kondenserdeki yağ birikimini geri kazan
7. **Purge ünitesi bakımı:** (Düşük basınçlı tipler) Purge ünitesini kontrol et, sayacı sıfırla, sızıntı noktalarını tespit et
8. **Titreşim ölçümü:** Kompresör ve motor rulmanlarında titreşim ölçümü yap, trend analizi ile karşılaştır
9. **Elektriksel denetim:** Motor akımı, yalıtım direnci, kontaktör ve koruma rölesi kontrollerini yap
10. **Kontrol sistemi kalibrasyonu:** Sıcaklık, basınç ve debi sensörlerini kalibre et, kontrol parametrelerini optimize et
11. **Performans doğrulama:** Bakım sonrası COP değerini ölç, tasarruf hesabını doğrula
12. **Bakım planı oluştur:** Yıllık bakım takvimini oluştur, sorumlulukları ata, KPI'ları belirle

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Eksik bakım kapsamı | Sadece boru temizliği yapılıp diğer kalemlerin ihmal edilmesi | Kapsamlı bakım kontrol listesi kullanılması |
| Uygunsuz soğutucu akışkan kullanımı | Yanlış tip veya kirli akışkan şarj edilmesi | Orijinal üretici spesifikasyonuna uyum, sertifikalı akışkan kullanımı |
| Aşırı kimyasal temizlik | Agresif kimyasallar boru malzemesini aşındırabilir | İnhibitörlü çözeltiler kullanılması, üretici önerilerine uyum |
| Kaçak oluşumu | Bakım sırasında conta hasarı veya bağlantı gevşemesi | Bakım sonrası kaçak testi, moment değerlerine uygun sıkma |
| Yanlış yağ türü | Soğutucu akışkan ile uyumsuz yağ kullanımı | Üretici spesifikasyonuna uygun yağ seçimi (POE, PVE, mineral) |
| Yetersiz eğitimli personel | Hatalı bakım uygulamaları ciddi arızalara yol açabilir | Üretici sertifikalı teknisyen kullanımı, düzenli eğitim |
| Soğutucu akışkan emisyonu | Bakım sırasında atmosfere akışkan salınımı | Geri kazanım cihazı kullanılması, F-gaz yönetmeliğine uyum |
| Güvenlik riskleri | Yüksek basınç, elektrik ve kimyasal tehlikeleri | İş güvenliği prosedürleri, kişisel koruyucu donanım (KKD) |

## İlgili Dosyalar

- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller exergy formülleri: `formulas/chiller_exergy.md`
- Soğutma kulesi optimizasyonu: `solutions/chiller_cooling_tower.md`
- Chiller yük optimizasyonu: `solutions/chiller_load_reduction.md`
- Delta-T optimizasyonu: `solutions/chiller_delta_t.md`

## Referanslar

- ASHRAE Handbook — HVAC Systems and Equipment, Chapter 43: "Centrifugal Chillers"
- ASHRAE Guideline 3-2022, "Reducing Emission of Halogenated Refrigerants in Refrigeration and Air-Conditioning Equipment and Systems"
- ARI Standard 550/590, "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages Using the Vapor Compression Cycle"
- Carrier Corporation, "Operation and Maintenance Manual — Centrifugal Liquid Chillers"
- Trane, "Chiller System Design and Control — Application Engineering Manual"
- DOE/FEMP, "Best Practices Guide for Energy-Efficient Chiller Operations"
- ISO 13256, "Water-source heat pumps — Testing and rating for performance"
- EUROVENT, "Energy Efficiency Classification for Liquid Chilling Packages"
- Türkiye Enerji Verimliliği Derneği (ENVER), "Soğutma Sistemlerinde Enerji Verimliliği Rehberi"
