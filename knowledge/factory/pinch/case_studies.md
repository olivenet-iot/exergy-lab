---
title: "Pinch Analizi Vaka Çalışmaları (Pinch Analysis Case Studies)"
category: factory
equipment_type: factory
keywords: [vaka çalışması, endüstriyel uygulama, petrokimya, gıda, tekstil, çimento, kağıt, kimya, otomotiv]
related_files: [factory/pinch/fundamentals.md, factory/pinch/practical_guide.md, factory/pinch/hen_retrofit.md, factory/pinch/cost_estimation.md]
use_when: ["Sektörel pinch analizi referansı gerektiğinde", "Benzer endüstri örneği aranırken", "Proje fizibilite aşamasında"]
priority: low
last_updated: 2026-02-01
---

# Pinch Analizi Vaka Çalışmaları (Pinch Analysis Case Studies)

Bu belge, yedi farklı endüstriyel sektörden gerçek pinch analizi uygulamalarını detaylı olarak sunmaktadır. Her vaka çalışması; tesis profili, akış verileri özeti, pinch analizi sonuçları, ısı değiştirici ağı (HEN — Heat Exchanger Network) tasarımı veya retrofit uygulaması, ekonomik sonuçlar ve çıkarılan dersleri kapsamaktadır. Amaç, farklı sektörlerdeki pinch analizi yaklaşımlarını karşılaştırmalı olarak inceleyerek mühendislere pratik referans sağlamaktır.

---

## 1. Petrokimya Tesisi (Petrochemical Plant)

### 1.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Etilen krakeri (Ethylene Cracker) |
| Kapasite | 800.000 ton/yıl etilen |
| Konum | Marmara Bölgesi, Türkiye |
| Çalışma Rejimi | Sürekli (Continuous), 8.400 saat/yıl |
| Mevcut Enerji Tüketimi | 85 MW ısıtma (QH), 62 MW soğutma (QC) |
| Birincil Enerji Kaynağı | Doğal gaz (Natural Gas), proses buharı |
| Mevcut HEN | 18 ısı değiştirici, çoğunluğu shell-and-tube |

Etilen krakeri tesisleri, endüstrinin en enerji yoğun proseslerinden biridir. Piroliz fırını (Pyrolysis Furnace) çıkışında 800-850 degC sıcaklıklara ulaşan akışlar, çok sayıda fraksiyonlama ve ayırma kolonundan geçerek ürünlere dönüştürülür. Bu geniş sıcaklık aralığı, pinch analizi için zengin bir ısı entegrasyonu potansiyeli sunar.

### 1.2 Akış Verileri Özeti

Tesiste toplam **28 sıcak akış (Hot Stream)** ve **22 soğuk akış (Cold Stream)** tanımlanmıştır.

**Temsili Sıcak Akışlar (Hot Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| H1 | Kraker çıkış gazı (Cracked Gas) | 820 | 350 | 45,3 | 21.291 |
| H2 | Quench suyu dönüşü | 185 | 40 | 82,1 | 11.895 |
| H3 | Deetanizer üst ürün | 65 | -30 | 35,7 | 3.392 |
| H4 | Propilen kolonu kondenser | 48 | 38 | 210,5 | 2.105 |
| H5 | Etilen kolonu yansıtma | -28 | -104 | 18,2 | 1.383 |
| ... | (Diğer 23 sıcak akış) | ... | ... | ... | ... |

**Temsili Soğuk Akışlar (Cold Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| C1 | Fırın besleme ön ısıtma | 25 | 580 | 38,6 | 21.423 |
| C2 | Depropanizer kaynatıcı | 55 | 62 | 520,0 | 3.640 |
| C3 | Demetanizer besleme | -80 | -35 | 42,3 | 1.904 |
| C4 | Proses buhar üretimi | 105 | 254 | 28,9 | 4.306 |
| ... | (Diğer 18 soğuk akış) | ... | ... | ... | ... |

### 1.3 Pinch Analizi Sonuçları

Optimum delta-T-min belirlemesi (Supertargeting) ile:

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 20 | — |
| Pinch Sıcaklığı (degC) | — | 128 (sıcak taraf: 138, soğuk taraf: 118) | — |
| QH,min (MW) | 85,0 | 51,8 | 33,2 MW (%39,1) |
| QC,min (MW) | 62,0 | 28,8 | 33,2 MW (%53,5) |
| Minimum Isı Değiştirici Sayısı | 18 | 42 | — |
| Isı Geri Kazanımı (MW) | 38,5 | 71,7 | +33,2 MW |

**Kompozit Eğriler (Composite Curves) Analizi:**
- Grand Composite Curve (GCC) incelendiğinde, 128 degC pinch noktasının altında ve üstünde belirgin ısı cebi (Heat Pocket) yapıları tespit edilmiştir.
- Pinch üstünde 12 MW'lık bir ısı cebi, orta basınç buhar (MP Steam, 15 bar) ile karşılanmaktaydı; bu cebin iç entegrasyonla kapatılması hedeflenmiştir.
- Kriyojenik bölgede (-104 degC ile -28 degC arası) ayrı bir alt-pinch (Sub-Ambient Pinch) noktası belirlenmiştir.

### 1.4 HEN Retrofit Tasarımı

Mevcut tesisin brownfield koşullarında tam grassroots (sıfırdan) tasarım yerine retrofit yaklaşımı benimsenmiştir:

**Uygulanan Modifikasyonlar:**

1. **Fırın Besleme Ön Isıtma Treni Genişletme:** Kraker çıkış gazı (H1) ile fırın besleme (C1) arasına 2 adet yeni shell-and-tube ısı değiştirici eklenerek, besleme ön ısıtma sıcaklığı 340 degC'den 480 degC'ye yükseltilmiştir. Kazanılan yük: 5.400 kW.

2. **Quench Suyu Isı Geri Kazanımı:** H2 akışından alçak basınç buhar (LP Steam, 3,5 bar) üretimi için yeni bir buhar jeneratörü kurulmuştur. Kazanılan yük: 8.200 kW.

3. **Kolon Entegrasyonu:** Depropanizer kaynatıcı (C2) ile propilen kolonu kondenser (H4) arasında direkt ısı entegrasyonu sağlanmıştır. Yeni 1 adet plate-type ısı değiştirici. Kazanılan yük: 2.100 kW.

4. **Orta Sıcaklık Cebi Kapatma:** Pinch üstündeki 12 MW'lık cebin 8,5 MW'ı, 3 yeni ısı değiştirici ile iç entegrasyona dönüştürülmüştür.

5. **Kriyojenik Bölge Optimizasyonu:** Mevcut soğutma kaskatı (Refrigeration Cascade) yeniden düzenlenmiş, 2 adet çapraz bağlantı (Cross-Pinch Heat Transfer) kaldırılmıştır. Soğutma kompresörü yükü 1.800 kW azaltılmıştır.

**Retrofit Sonrası Performans:**

| Parametre | Mevcut | Retrofit Sonrası | Hedef |
|---|---|---|---|
| QH (MW) | 85,0 | 58,7 | 51,8 |
| QC (MW) | 62,0 | 35,7 | 28,8 |
| Isı Geri Kazanımı (MW) | 38,5 | 64,8 | 71,7 |
| Toplam HEN Birim Sayısı | 18 | 26 | 42 |

Retrofit ile hedefe %79 oranında ulaşılmıştır. Kalan %21'lik potansiyel, mevcut boru güzergahı kısıtlamaları ve operasyonel esneklik gereksinimleri nedeniyle ileri faza bırakılmıştır.

### 1.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 4.200.000 EUR |
| Yeni Isı Değiştirici Maliyeti | 2.850.000 EUR |
| Boru ve Montaj Maliyeti | 980.000 EUR |
| Mühendislik ve Proje Yönetimi | 370.000 EUR |
| Yıllık Enerji Tasarrufu | 26.300 kW x 8.400 h x 0,035 EUR/kWh = 7.730.000 EUR/yıl |
| Ek Soğutma Tasarrufu | 480.000 EUR/yıl |
| Toplam Yıllık Tasarruf | 8.210.000 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 0,51 yıl (~6,1 ay) |
| NPV (Net Present Value, %10, 15 yıl) | 58.200.000 EUR |
| IRR (Internal Rate of Return) | > %190 |
| CO2 Azaltma | 42.000 ton CO2/yıl |

**Not:** Bu proje, yüksek enerji fiyatları ve büyük ölçek nedeniyle olağanüstü kısa geri ödeme süresi göstermektedir. Ancak büyük petrokimya tesislerinde bu tip getiriler literatürde yaygın olarak raporlanmaktadır (Linnhoff, 1994).

### 1.6 Çıkarılan Dersler

- Büyük petrokimya tesislerinde akış sayısının fazla olması (50+), sistematik pinch analizi olmadan optimizasyon yapılmasını neredeyse imkansız kılmaktadır.
- Retrofit projeleri, grassroots hedefin %70-85'ine ulaşabilir; bu oran yeterli ekonomik getiriyi sağlamaktadır.
- Kriyojenik bölge ayrı bir alt-problem (Sub-Problem) olarak ele alınmalı; ortam üstü ve ortam altı sistemler bağımsız analiz edilmelidir.
- Pinch üstü ısı ceplerinin (Heat Pockets) kapatılması, doğrudan dış enerji tüketimini azaltmaktadır.
- Proje başarısı için operasyon ekibinin erken dahil edilmesi kritik önem taşımaktadır.

---

## 2. Gıda Endüstrisi — Süt İşleme Tesisi (Dairy Processing Plant)

### 2.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Süt işleme (Pastörizasyon ve UHT Sterilizasyon) |
| Kapasite | 500.000 litre/gün süt işleme |
| Çalışma Rejimi | Kesikli-sürekli karma, 6.500 saat/yıl |
| Mevcut Enerji Tüketimi | 3,8 MW ısıtma, 2,1 MW soğutma |
| Birincil Enerji Kaynağı | Doğal gaz kazanı, buhar sistemi |
| Gıda Güvenliği Kısıtı | HACCP uyumlu, çapraz kontaminasyon önleme |

Süt işleme tesislerinde ısıtma ve soğutma operasyonları arasındaki sıcaklık yakınlığı, pinch analizinin en etkili olduğu alanlardan birini oluşturur. Pastörizasyon (72 degC, 15 s) ve UHT sterilizasyon (137 degC, 4 s) prosesleri yüksek rejenerasyon potansiyeline sahiptir.

### 2.2 Akış Verileri Özeti

Tesiste **6 sıcak akış** ve **5 soğuk akış** tanımlanmıştır.

**Sıcak Akışlar (Hot Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| H1 | Pastörize süt soğutma | 72 | 4 | 24,5 | 1.666 |
| H2 | UHT süt soğutma | 137 | 25 | 8,2 | 918 |
| H3 | CIP (Clean-In-Place) dönüş suyu | 85 | 30 | 5,8 | 319 |
| H4 | Yoğurt inkübasyon soğutma | 43 | 4 | 12,3 | 480 |
| H5 | Evaporatör kondensat | 65 | 25 | 4,1 | 164 |
| H6 | Krema pastörizasyon soğutma | 95 | 8 | 3,5 | 305 |

**Soğuk Akışlar (Cold Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| C1 | Çiğ süt ön ısıtma (Pastörizasyon) | 4 | 72 | 24,5 | 1.666 |
| C2 | UHT besleme ısıtma | 4 | 137 | 8,2 | 1.091 |
| C3 | CIP çözelti ısıtma | 15 | 85 | 5,8 | 406 |
| C4 | Kazan besleme suyu ön ısıtma | 12 | 80 | 3,2 | 218 |
| C5 | Sıcak su hazırlama | 10 | 60 | 5,5 | 275 |

### 2.3 Pinch Analizi Sonuçları

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 5 | — |
| Pinch Sıcaklığı (degC) | — | 42 (sıcak taraf: 44,5, soğuk taraf: 39,5) | — |
| QH,min (MW) | 3,80 | 2,42 | 1,38 MW (%36,3) |
| QC,min (MW) | 2,10 | 0,72 | 1,38 MW (%65,7) |
| Isı Geri Kazanımı (MW) | 1,20 | 2,58 | +1,38 MW |

**Önemli Bulgu:** Gıda endüstrisinde delta-T-min=5 degC uygulanabilir, çünkü akışların büyük çoğunluğu sıvı fazda ve temiz koşullardadır. Plate-type ısı değiştiriciler (PHE — Plate Heat Exchanger) gıda endüstrisinin standart ekipmanıdır ve düşük delta-T-min değerlerini ekonomik olarak destekler.

**Pinch Noktası Yorumu:** 42 degC'lik pinch, pastörizasyon sonrası soğutma ile çiğ süt ön ısıtma arasındaki doğal eşleşmeyi yansıtmaktadır. Mevcut rejeneratif pastörizatörler zaten bu prensibi kısmen kullanmakta ancak tam optimizasyona ulaşmamaktadır.

### 2.4 HEN Tasarımı

Gıda endüstrisinde hijyen ve gıda güvenliği kısıtları, dolaylı ısı transfer sistemlerini (ara akışkan devresi) zorunlu kılabilir. Tasarım bu kısıtları dikkate almıştır:

1. **Pastörizatör Rejenerasyon Artırma:** Mevcut rejenerasyon oranı %85'ten %94'e yükseltilmiştir. Ek 2 adet gıda sınıfı (Food-Grade) PHE plakası eklenerek, pastörizasyon bölümünde 230 kW ek geri kazanım sağlanmıştır.

2. **UHT — Pastörizasyon Çapraz Entegrasyon:** UHT soğutma (H2) ile pastörizasyon ön ısıtma (C1) arasında ara glikol devresi üzerinden dolaylı ısı transferi. Gıda güvenliği açısından iki akış doğrudan temas etmemektedir. Kazanılan yük: 420 kW.

3. **CIP Isı Geri Kazanımı:** CIP dönüş suyu (H3) ile CIP taze çözelti ısıtma (C3) ve sıcak su hazırlama (C5) arasında kaskad geri kazanım. Kazanılan yük: 310 kW.

4. **Evaporatör Kondensat Değerlendirme:** H5 akışı ile kazan besleme suyu ön ısıtma (C4) eşleşmesi. Kazanılan yük: 155 kW.

5. **Yoğurt Soğutma — Sıcak Su Entegrasyonu:** H4 akışından düşük sıcaklıklı (43 degC) ısı ile sıcak su ön ısıtma. Isı pompası (Heat Pump) desteği ile COP=4,5 elde edilmiştir. Kazanılan yük: 265 kW.

### 2.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 120.000 EUR |
| PHE Ekipman Maliyeti | 68.000 EUR |
| Isı Pompası (Yoğurt Bölümü) | 28.000 EUR |
| Boru, Pompa ve Montaj | 16.000 EUR |
| Mühendislik | 8.000 EUR |
| Yıllık Enerji Tasarrufu (Isıtma) | 1.380 kW x 6.500 h x 0,040 EUR/kWh = 358.800 EUR/yıl |
| Yıllık Soğutma Tasarrufu | 1.380 kW x 6.500 h x 0,015 EUR/kWh = 134.550 EUR/yıl |
| Isı Pompası Elektrik Maliyeti (Negatif) | -38.200 EUR/yıl |
| Toplam Yıllık Net Tasarruf | 455.150 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 0,26 yıl (~3,2 ay) |
| NPV (%8, 10 yıl) | 2.930.000 EUR |
| CO2 Azaltma | 2.150 ton CO2/yıl |
| Su Tasarrufu | 18.000 m3/yıl (soğutma kulesi yükü azalması) |

### 2.6 Çıkarılan Dersler

- Gıda endüstrisinde delta-T-min=5 degC ile çalışmak ekonomik ve teknik olarak uygulanabilirdir.
- Hijyen kısıtları, ısı entegrasyonunu engellemez ancak dolaylı devre maliyetlerini artırır.
- Pastörizasyon-soğutma döngüsü, pinch analizinin en klasik uygulama alanıdır; mevcut rejeneratörlerin %90+ verimliliğe çıkarılması öncelikli hedeftir.
- Düşük sıcaklıklı akışlarda (40-50 degC) ısı pompası entegrasyonu, pinch analizi ile birleştirildiğinde sinerjik fayda sağlar.
- Gıda tesislerinde CIP sistemi genellikle ihmal edilir, ancak önemli bir ısı geri kazanım kaynağıdır.

---

## 3. Tekstil Fabrikası (Textile Plant)

### 3.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Boyama ve terbiye (Dyeing and Finishing) |
| Kapasite | 25 ton/gün kumaş işleme |
| Çalışma Rejimi | Kesikli (Batch), 5.800 saat/yıl |
| Mevcut Enerji Tüketimi | 4,2 MW ısıtma, 1,8 MW soğutma |
| Su Tüketimi | 3.500 m3/gün |
| Birincil Enerji Kaynağı | Doğal gaz kazanı, LPG yedek |
| Atıksu Sıcaklığı | 45-80 degC (boyama banyosu tipine bağlı) |

Tekstil boyama ve terbiye tesislerinde ısıl işlemler çok yoğun su kullanımı ile birlikte yürütülür. Bu durum, pinch analizini enerji-su bütünleşik optimizasyonu (Combined Energy-Water Pinch) boyutuna taşımaktadır.

### 3.2 Akış Verileri Özeti

**8 sıcak akış** ve **6 soğuk akış** tanımlanmıştır.

**Sıcak Akışlar (Hot Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| H1 | Reaktif boyama atık banyosu | 80 | 35 | 18,2 | 819 |
| H2 | Dispersiyon boyama atık banyosu | 130 | 35 | 12,5 | 1.188 |
| H3 | Yıkama suyu drenajı (1. kademe) | 70 | 30 | 22,0 | 880 |
| H4 | Yıkama suyu drenajı (2. kademe) | 50 | 30 | 15,3 | 306 |
| H5 | Kurutma havası çıkışı (Stenter Exhaust) | 150 | 80 | 6,8 | 476 |
| H6 | Fiksaj fırını çıkışı | 180 | 100 | 3,2 | 256 |
| H7 | Buhar kondensat dönüşü | 95 | 60 | 4,5 | 158 |
| H8 | Merserizasyon soğutma | 85 | 25 | 7,8 | 468 |

**Soğuk Akışlar (Cold Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| C1 | Boyama banyosu hazırlama (Reaktif) | 15 | 80 | 18,2 | 1.183 |
| C2 | Boyama banyosu hazırlama (Dispersiyon) | 15 | 130 | 12,5 | 1.438 |
| C3 | Yıkama suyu ısıtma | 15 | 70 | 22,0 | 1.210 |
| C4 | Stenter besleme havası ısıtma | 25 | 180 | 4,5 | 698 |
| C5 | Kazan besleme suyu | 20 | 90 | 3,8 | 266 |
| C6 | Tesis sıcak su ihtiyacı | 15 | 55 | 5,2 | 208 |

### 3.3 Pinch Analizi Sonuçları

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 15 | — |
| Pinch Sıcaklığı (degC) | — | 72 (sıcak taraf: 79,5, soğuk taraf: 64,5) | — |
| QH,min (MW) | 4,20 | 2,90 | 1,30 MW (%31,0) |
| QC,min (MW) | 1,80 | 0,50 | 1,30 MW (%72,2) |
| Isı Geri Kazanımı (MW) | 1,80 | 3,10 | +1,30 MW |

**delta-T-min=15 degC Seçimi Gerekçesi:** Tekstil atıksularında lif kalıntıları, boyar madde ve kimyasal katkılar fouling (kirlenme) riskini artırır. Bu nedenle delta-T-min gıda endüstrisine kıyasla daha yüksek seçilmiştir. Ayrıca batch operasyonda eşzamanlı akış garantisi olmadığından, termal depolama (Thermal Energy Storage — TES) ihtiyacı delta-T-min seçimini etkiler.

### 3.4 HEN Retrofit ve Su Entegrasyonu

Tekstil fabrikasında enerji ve su pinch analizleri birlikte yürütülmüştür:

1. **Atık Banyo Isı Geri Kazanımı:** H1 ve H2 akışlarından gelen sıcak atıksu, filtreleme sonrası bir termal depolama tankına (50 m3, stratifiye tank) yönlendirilmiştir. Depolanan ısı, bir sonraki batch'in banyo hazırlama (C1, C2) ön ısıtmasında kullanılmaktadır. Kazanılan yük: 680 kW (ortalama).

2. **Yıkama Suyu Kaskadı (Counter-Current Washing):** Mevcut eş-akımlı (co-current) yıkama sistemi, karşı-akımlı (counter-current) kaskada dönüştürülmüştür. Bu değişiklik hem su tüketimini %15 azaltmış hem de yıkama suyu drenaj sıcaklığını artırarak geri kazanım potansiyelini yükseltmiştir. Su tasarrufu: 525 m3/gün.

3. **Stenter Baca Gazı Geri Kazanımı:** H5 akışından (stenter egzost, 150 degC) yoğuşturmalı ekonomizer ile C4 akışı (stenter taze hava) ön ısıtması. Kazanılan yük: 380 kW. Dikkat: Stenter egzostunda uçucu organik bileşik (VOC) ve yağ damlacıkları bulunabilir; özel korozyon dayanımlı paslanmaz çelik (AISI 316L) ısı değiştirici kullanılmıştır.

4. **Kondensat ve Merserizasyon Entegrasyonu:** H7 ve H8 akışları birleştirilerek C5 ve C6 soğuk akışlarının ön ısıtmasında kullanılmıştır. Kazanılan yük: 240 kW.

### 3.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 185.000 EUR |
| Termal Depolama Tankı | 42.000 EUR |
| Isı Değiştiriciler (4 adet) | 65.000 EUR |
| Karşı-Akımlı Yıkama Sistemi Dönüşümü | 48.000 EUR |
| Boru, Pompa ve Montaj | 22.000 EUR |
| Mühendislik | 8.000 EUR |
| Yıllık Enerji Tasarrufu | 1.300 kW x 5.800 h x 0,042 EUR/kWh = 316.680 EUR/yıl |
| Yıllık Su Tasarrufu | 525 m3/gün x 300 gün x 2,50 EUR/m3 = 393.750 EUR/yıl |
| Toplam Yıllık Tasarruf | 710.430 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 0,26 yıl (~3,1 ay) |
| NPV (%10, 10 yıl) | 4.180.000 EUR |
| CO2 Azaltma | 1.980 ton CO2/yıl |
| Su Tasarrufu | 157.500 m3/yıl (%15 azalma) |

### 3.6 Çıkarılan Dersler

- Tekstil sektöründe enerji ve su pinch analizleri birlikte yapılmalıdır; ayrı ayrı yapıldığında alt-optimal sonuçlar elde edilir.
- Batch proseslerde termal depolama (TES) olmadan pinch hedeflerine ulaşmak mümkün değildir.
- Fouling riski yüksek akışlarda uygun filtrasyon ve delta-T-min seçimi kritiktir.
- Karşı-akımlı yıkama dönüşümü, en düşük yatırımla en yüksek su ve enerji tasarrufunu sağlayan müdahaledir.
- Stenter egzost geri kazanımı teknik olarak zorlu olsa da ekonomik getirisi yüksektir.

---

## 4. Kağıt Fabrikası (Paper Mill)

### 4.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Selüloz ve kağıt üretimi (Pulp and Paper) |
| Kapasite | 1.200 ton/gün kağıt üretimi |
| Çalışma Rejimi | Sürekli, 8.200 saat/yıl |
| Mevcut Enerji Tüketimi | 48 MW ısıtma (çoğunlukla buhar), 12 MW soğutma |
| Buhar Sistemi | Bark boiler + doğal gaz yedek kazan, 3 basınç seviyesi |
| Su Tüketimi | 45.000 m3/gün |

Kağıt fabrikaları, hem büyük ölçekli buhar sistemleri hem de yoğun su kullanımı ile pinch analizinin klasik uygulama alanlarındandır. Buhar sistemi optimizasyonu (Steam System Pinch) ve proses pinch analizi ayrı ayrı yürütülmüştür.

### 4.2 Akış Verileri Özeti

Tesiste **12 sıcak akış** ve **10 soğuk akış** tanımlanmıştır.

**Temsili Sıcak Akışlar (Hot Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| H1 | Siyah likör evaporasyon kondensat | 85 | 40 | 52,3 | 2.354 |
| H2 | Kurutma bölümü egzost havası | 95 | 60 | 68,5 | 2.398 |
| H3 | Beyazlatma (Bleaching) atıksu | 70 | 35 | 42,8 | 1.498 |
| H4 | Pişirme (Digester) relief buharı | 165 | 120 | 15,2 | 684 |
| H5 | Kağıt makinesi pres suyu | 55 | 30 | 85,0 | 2.125 |
| ... | (Diğer 7 sıcak akış) | ... | ... | ... | ... |

**Temsili Soğuk Akışlar (Cold Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| C1 | Siyah likör ön ısıtma (Digestere) | 65 | 155 | 18,5 | 1.665 |
| C2 | Taze su ısıtma (Proses) | 8 | 55 | 120,0 | 5.640 |
| C3 | Beyazlatma çözeltisi ısıtma | 25 | 70 | 38,2 | 1.719 |
| C4 | Kurutma bölümü taze hava ön ısıtma | 5 | 50 | 55,0 | 2.475 |
| ... | (Diğer 6 soğuk akış) | ... | ... | ... | ... |

### 4.3 Pinch Analizi Sonuçları

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 10 | — |
| Pinch Sıcaklığı (degC) | — | 58 (sıcak taraf: 63, soğuk taraf: 53) | — |
| QH,min (MW) | 48,0 | 36,0 | 12,0 MW (%25,0) |
| QC,min (MW) | 12,0 | 0 (su ile karşılanabilir) | 12,0 MW (%100) |
| Isı Geri Kazanımı (MW) | 22,5 | 34,5 | +12,0 MW |

**GCC Analizi Bulguları:**
- Grand Composite Curve, 58 degC pinch noktasının altında büyük miktarda düşük sıcaklıklı ısı fazlası göstermektedir. Bu ısının tamamı proses suyu veya hava ön ısıtma ile değerlendirilebilir.
- Pinch üstünde, orta basınç buhar (MP, 10 bar) ile karşılanan yüklerin bir kısmı, proses akışları arası entegrasyonla düşük basınç buharına (LP, 3,5 bar) kaydırılabilir. Bu durum, buhar sistemi optimizasyonuna olanak sağlamaktadır.

### 4.4 HEN Tasarımı ve Buhar Sistemi Optimizasyonu

**Proses Tarafı Modifikasyonlar:**

1. **Siyah Likör Ön Isıtma Entegrasyonu:** Digester relief buharı (H4) ile siyah likör ön ısıtma (C1) arasında direkt eşleşme. Mevcut MP buhar tüketimi 684 kW azaltılmıştır.

2. **Evaporasyon Kondensat — Taze Su Isıtma:** H1 akışı ile C2 akışının ilk kademesi (8 degC → 38 degC) eşleştirilmiştir. Bu büyük hacimli düşük sıcaklıklı geri kazanım, toplam projenin en büyük tek kalemini oluşturmaktadır. Kazanılan yük: 3.600 kW.

3. **Kurutma Bölümü Kapalı Çevrim:** Kurutma egzostu (H2) ile taze hava ön ısıtma (C4) arasına run-around coil sistemi kurulmuştur. Kurutma bölümünde nem yoğuşması sorunu nedeniyle direkt eşleşme yerine dolaylı devre tercih edilmiştir. Kazanılan yük: 2.100 kW.

4. **Beyazlatma Atıksu — Çözelti Isıtma:** H3 ve C3 akışları arasında PHE ile direkt geri kazanım. Kazanılan yük: 1.200 kW.

5. **Pres Suyu Değerlendirme:** H5 akışının düşük sıcaklığı (55 degC) nedeniyle doğrudan geri kazanım sınırlıdır; kalan ısı, tesis ısıtma (Space Heating) desteği için kullanılmıştır (mevsimsel). Kazanılan yük: 850 kW (kış ortalaması).

**Buhar Sistemi Optimizasyonu:**
- Pinch analizi sonuçlarına göre, MP buhar tüketimi 4,2 MW azaltılmıştır.
- Bark boiler'da LP buhar üretimi artırılarak, doğal gaz yedek kazanın devre dışı bırakılması hedeflenmiştir.
- Let-down valfi (basınç düşürme vanası) üzerinden geçen 3,8 MW'lık buhar akışı, back-pressure türbin ile elektrik üretimine dönüştürülmüştür. Ek elektrik üretimi: 780 kW_e.

### 4.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 1.850.000 EUR |
| Isı Değiştiriciler (8 adet) | 680.000 EUR |
| Run-Around Coil Sistemi | 320.000 EUR |
| Back-Pressure Türbin | 480.000 EUR |
| Boru, Pompa ve Montaj | 265.000 EUR |
| Mühendislik ve Proje Yönetimi | 105.000 EUR |
| Yıllık Enerji Tasarrufu (Buhar) | 12.000 kW x 8.200 h x 0,025 EUR/kWh = 2.460.000 EUR/yıl |
| Yıllık Elektrik Üretimi (Türbin) | 780 kW x 8.200 h x 0,085 EUR/kWh = 543.240 EUR/yıl |
| Toplam Yıllık Tasarruf | 3.003.240 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 0,62 yıl (~7,4 ay) |
| NPV (%8, 15 yıl) | 23.800.000 EUR |
| CO2 Azaltma | 18.500 ton CO2/yıl |

### 4.6 Çıkarılan Dersler

- Kağıt fabrikalarında proses pinch ve buhar sistemi pinch analizleri birlikte yapılmalıdır.
- Buhar sistemi let-down valfi üzerinden geçen enerji, back-pressure türbin ile değerlendirilmelidir.
- Düşük sıcaklıklı büyük hacimli akışlar (proses suyu, pres suyu), toplam ısı geri kazanımının en büyük kısmını oluşturur.
- Kurutma bölümü ısı geri kazanımında nem yönetimi kritik tasarım parametresidir.
- Kağıt sektöründe %25'lik ısıtma tasarrufu hedefi, endüstri ortalaması ile uyumludur (IEA, 2018).

---

## 5. Kimya Tesisi (Chemical Plant)

### 5.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Özel kimyasallar üretimi (Specialty Chemicals), batch ve sürekli karma |
| Kapasite | Çoklu ürün hattı, 15 farklı ürün |
| Çalışma Rejimi | Karma: 3 sürekli hat + 8 batch reaktör, 7.200 saat/yıl |
| Mevcut Enerji Tüketimi | 6,5 MW ısıtma, 4,2 MW soğutma |
| Birincil Enerji Kaynağı | Buhar (3 basınç seviyesi) + termik yağ (Thermal Oil, 280 degC) |
| Soğutma | Soğutma kulesi + chiller (-15 degC glikol) |

Kimya tesislerinde batch ve sürekli proseslerin bir arada bulunması, zamana bağlı (Time-Dependent) pinch analizi gerektirir. Bu vaka çalışmasında Termal Enerji Depolama (TES — Thermal Energy Storage) entegrasyonunun kritik rolü incelenmektedir.

### 5.2 Akış Verileri Özeti

Batch prosesler için zaman-ortalama (Time-Average) akış verileri kullanılmıştır. Tesiste sürekli proseslerden **10 sıcak + 8 soğuk**, batch proseslerden **10 sıcak + 7 soğuk** akış tanımlanmıştır. Toplam: **20 sıcak akış**, **15 soğuk akış**.

**Temsili Sürekli Akışlar:**

| Akış No | Tip | Tanım | Ts (degC) | Tt (degC) | Q (kW) |
|---|---|---|---|---|---|
| SC-H1 | Sıcak | Distilasyon kondenser | 120 | 40 | 850 |
| SC-H2 | Sıcak | Reaktör soğutma (ekzotermik) | 180 | 60 | 1.200 |
| SC-C1 | Soğuk | Distilasyon kaynatıcı | 115 | 135 | 920 |
| SC-C2 | Soğuk | Reaktör ön ısıtma | 25 | 160 | 680 |

**Temsili Batch Akışlar (Zaman-Ortalama):**

| Akış No | Tip | Tanım | Ts (degC) | Tt (degC) | Q (kW) | Zaman Dilimi |
|---|---|---|---|---|---|---|
| B-H1 | Sıcak | Batch reaktör soğutma (Ürün A) | 150 | 30 | 480 | 08:00-14:00 |
| B-H2 | Sıcak | Kristalizör soğutma | 80 | -10 | 620 | 10:00-16:00 |
| B-C1 | Soğuk | Batch reaktör ısıtma (Ürün B) | 20 | 120 | 350 | 06:00-12:00 |
| B-C2 | Soğuk | Çözücü geri kazanım ısıtma | 30 | 85 | 280 | 14:00-20:00 |

### 5.3 Pinch Analizi Sonuçları

**Zaman-Bağımsız (Time-Average) Analiz:**

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 20 | — |
| Pinch Sıcaklığı (degC) | — | 95 | — |
| QH,min (MW) | 6,50 | 4,85 | 1,65 MW (%25,4) |
| QC,min (MW) | 4,20 | 2,55 | 1,65 MW (%39,3) |

**Zaman-Bağımlı (Time-Slice) Analiz:**

Zaman dilimli analiz, batch proseslerin eşzamanlılık sorununu ortaya koymuştur. Bazı zaman dilimlerinde ısı fazlası, bazılarında ısı açığı bulunmaktadır.

| Zaman Dilimi | Isı Fazlası (kW) | Isı Açığı (kW) | Net Durum |
|---|---|---|---|
| 00:00-06:00 | 2.050 | 1.580 | +470 (Fazla) |
| 06:00-12:00 | 3.180 | 2.850 | +330 (Fazla) |
| 12:00-18:00 | 2.720 | 3.400 | -680 (Açık) |
| 18:00-24:00 | 1.850 | 2.370 | -520 (Açık) |

TES kullanılmadan zaman-ortalama hedefine ulaşmak mümkün değildir. 24 saat ortalamada %25,4 potansiyel varken, TES olmadan sadece %12 gerçekleştirilebilmektedir. TES ile hedefe %80 yaklaşarak %20 net tasarruf elde edilmiştir.

### 5.4 HEN Tasarımı ve TES Entegrasyonu

1. **Sürekli Prosesler Arası Doğrudan Entegrasyon:** SC-H1 (kondenser) ve SC-C2 (reaktör ön ısıtma) arasında doğrudan eşleşme. Sürekli çalıştıkları için TES ihtiyacı yoktur. Kazanılan yük: 650 kW.

2. **Distilasyon Kolon Entegrasyonu:** SC-H1 kondenser (120 degC) ile SC-C1 kaynatıcı (115 degC) arasında delta-T=5 degC ile direkt entegrasyon. Heat-Integrated Distillation Column (HIDiC) benzeri yaklaşım uygulanmıştır. Kazanılan yük: 420 kW.

3. **Termal Enerji Depolama (TES) Sistemi:**
   - 2 adet stratifiye TES tankı kurulmuştur:
     - **TES-1 (Yüksek Sıcaklık):** 30 m3, termik yağ, 100-180 degC aralığı, 4.200 kWh kapasite
     - **TES-2 (Düşük Sıcaklık):** 50 m3, su, 40-85 degC aralığı, 2.600 kWh kapasite
   - Gece ve sabah saatlerindeki ısı fazlası TES'e depolanmakta, öğleden sonra ve akşam açığı TES'ten karşılanmaktadır.
   - TES etkinliği: %85 (termal kayıplar ve stratifikasyon bozulması dahil)
   - TES ile ek geri kazanım: 580 kW (ortalama)

4. **Batch Reaktörler Arası Zaman-Kaydırma:** B-H1 (08:00-14:00) ile B-C2 (14:00-20:00) arasında TES-1 üzerinden dolaylı entegrasyon. Kazanılan yük: 280 kW.

### 5.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 420.000 EUR |
| Isı Değiştiriciler (5 adet) | 145.000 EUR |
| TES Tankları (2 adet) | 165.000 EUR |
| Kontrol ve Otomasyon (TES Yönetim Sistemi) | 58.000 EUR |
| Boru, Pompa ve Montaj | 38.000 EUR |
| Mühendislik | 14.000 EUR |
| Yıllık Enerji Tasarrufu (Isıtma) | 1.300 kW x 7.200 h x 0,038 EUR/kWh = 355.680 EUR/yıl |
| Yıllık Soğutma Tasarrufu | 1.300 kW x 7.200 h x 0,018 EUR/kWh = 168.480 EUR/yıl |
| Toplam Yıllık Tasarruf | 524.160 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 0,80 yıl (~9,6 ay) |
| NPV (%10, 12 yıl) | 3.150.000 EUR |
| CO2 Azaltma | 3.850 ton CO2/yıl |

### 5.6 Çıkarılan Dersler

- Batch proseslerde standart pinch analizi yetersizdir; zaman dilimli (Time-Slice) veya zaman-ortalama (Time-Average) analiz uygulanmalıdır.
- TES, batch-sürekli karma tesislerde pinch hedeflerine ulaşmak için zorunlu bir teknolojidir.
- TES tank boyutlandırması, zaman dilimli ısı dengesi profiline göre yapılmalıdır; aşırı boyutlandırma termal kayıpları artırır.
- Kontrol ve otomasyon, TES entegrasyonunun başarısında kritik rol oynar; ısı depolama-boşaltma stratejisi gerçek zamanlı olarak optimize edilmelidir.
- Çoklu ürün hatlı tesislerde, ürün değişimlerinin ısı dengesi profili üzerindeki etkisi senaryo analizi ile değerlendirilmelidir.

---

## 6. Çimento Fabrikası (Cement Plant)

### 6.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Entegre çimento fabrikası (Portland çimento) |
| Kapasite | 5.000 ton/gün klinker (Clinker) |
| Çalışma Rejimi | Sürekli, 7.800 saat/yıl |
| Mevcut Enerji Tüketimi | 125 MW termal (döner fırın — Rotary Kiln), 18 MW elektrik |
| Birincil Yakıt | Kömür + alternatif yakıt (%15 RDF) |
| Spesifik Enerji Tüketimi | 3.450 kJ/kg klinker (sektör ortalaması: 3.300 kJ/kg) |

Çimento fabrikaları, yüksek sıcaklık (1.450 degC klinker sinterlemesi) ve büyük ölçek ile karakterize edilir. Geleneksel pinch analizi düşük-orta sıcaklık aralıklarına odaklanırken, çimento sektöründe yüksek sıcaklıklı akışlar baskındır. Bu durum, farklı bir delta-T-min stratejisi ve özel malzeme gereksinimleri doğurur.

### 6.2 Akış Verileri Özeti

Çimento prosesinde akış sayısı sınırlı olmasına rağmen, her akışın termal yükü çok yüksektir. **5 sıcak akış** ve **4 soğuk akış** tanımlanmıştır.

**Sıcak Akışlar (Hot Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| H1 | Fırın egzost gazı (Kiln Exhaust Gas) | 350 | 120 | 82,5 | 18.975 |
| H2 | Klinker soğutucu orta hava (Clinker Cooler Mid-Air) | 450 | 120 | 45,2 | 14.916 |
| H3 | Klinker soğutucu atık hava (Clinker Cooler Excess Air) | 280 | 80 | 38,8 | 7.760 |
| H4 | Öğütme atık havası (Mill Exhaust) | 95 | 60 | 65,0 | 2.275 |
| H5 | Bypass gazı (Kiln Bypass Gas) | 850 | 200 | 5,8 | 3.770 |

**Soğuk Akışlar (Cold Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| C1 | Ham farin ön ısıtma (Raw Meal Preheat) | 60 | 850 | 42,0 | 33.180 |
| C2 | Yanma havası ön ısıtma | 25 | 200 | 18,5 | 3.238 |
| C3 | Kömür değirmeni kurutma havası | 25 | 120 | 32,0 | 3.040 |
| C4 | Alternatif yakıt kurutma | 15 | 85 | 8,5 | 595 |

### 6.3 Pinch Analizi Sonuçları

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 40 | — |
| Pinch Sıcaklığı (degC) | — | 310 (sıcak taraf: 330, soğuk taraf: 290) | — |
| QH,min (MW) | 125,0 | 106,0 | 19,0 MW (%15,2) |
| QC,min (MW) | 30,0 | 11,0 | 19,0 MW (%63,3) |
| Isı Geri Kazanımı (MW) | 15,5 | 34,5 | +19,0 MW |

**delta-T-min=40 degC Seçimi Gerekçesi:**
- Yüksek sıcaklıklarda radyasyon ve konveksiyon ısı transferi dominanttır; büyük delta-T daha ekonomik ısı değiştirici tasarımına olanak verir.
- Gaz-katı (Gas-Solid) ısı transferi düşük katsayılara sahiptir (h = 20-50 W/m2K).
- Aşınma (Erosion) ve fouling koşulları, daha büyük boşluklu (Pitch) ekipman gerektirmektedir.
- Supertargeting analizi, delta-T-min=30-50 degC aralığında toplam yıllık maliyet eğrisinin oldukça düz (flat) olduğunu göstermiş; 40 degC operasyonel esneklik açısından tercih edilmiştir.

### 6.4 Klinker Soğutucu ve Fırın Entegrasyonu

Çimento fabrikasında geleneksel HEN retrofit yerine, proses entegrasyonu modifikasyonları uygulanmıştır:

1. **Klinker Soğutucu Orta Hava (H2) — Ön Isıtıcı (C1) Entegrasyonu:** Klinker soğutucu orta havası (450 degC) doğrudan ön ısıtıcı kademelerine (Preheater Cyclone Stages) yönlendirilmiştir. Mevcut durumda bu havanın bir kısmı bacadan atılmaktaydı. Modifikasyon ile fırına giren tersiyer hava sıcaklığı artırılmıştır. Kazanılan yük: 8.200 kW.

2. **Fırın Egzost (H1) — Kömür Değirmeni ve Alternatif Yakıt Kurutma:** Fırın egzostu (350 degC) mevcut durumda zaten ham farin kurutma ve ön ısıtma için kullanılmaktadır, ancak kömür değirmeni kurutma havası (C3) ve alternatif yakıt kurutma (C4) için ayrıca sıcak hava üretilmekteydi. Bu akışlar fırın egzost devresine entegre edilmiştir. Kazanılan yük: 2.800 kW.

3. **Atık Hava ile Atık Isı Geri Kazanım Sistemi (WHRS — Waste Heat Recovery System):** Klinker soğutucu atık havası (H3, 280 degC) ve fırın egzostunun kullanılmayan kısmı ile ORC (Organic Rankine Cycle) tabanlı elektrik üretim sistemi kurulmuştur.
   - ORC çalışma akışkanı: n-Pentane
   - Evaporasyon sıcaklığı: 165 degC
   - Kondensasyon sıcaklığı: 35 degC
   - Termal verim: %18,5
   - Ek elektrik üretimi: 2.850 kW_e
   - Termal giriş: 15.400 kW

4. **Bypass Gazı (H5) Isı Geri Kazanımı:** Bypass gazı yüksek sıcaklığına rağmen (850 degC), alkali ve klor içeriği nedeniyle doğrudan proses entegrasyonu risklidir. Radyatif ısı değiştirici ile buhar üretimi değerlendirilmiştir. Üretilen buhar, ORC sistemine ek giriş olarak yönlendirilmiştir. Kazanılan yük: 2.200 kW.

### 6.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 6.800.000 EUR |
| ORC Sistemi | 4.200.000 EUR |
| Klinker Soğutucu Modifikasyonu | 1.100.000 EUR |
| Boru, Kanal ve Montaj | 850.000 EUR |
| Bypass Gazı Isı Değiştirici | 420.000 EUR |
| Mühendislik ve Proje Yönetimi | 230.000 EUR |
| Yıllık Yakıt Tasarrufu | 11.000 kW x 7.800 h x 0,018 EUR/kWh = 1.544.400 EUR/yıl |
| Yıllık Elektrik Üretimi (ORC) | 2.850 kW x 7.800 h x 0,085 EUR/kWh = 1.889.100 EUR/yıl |
| Toplam Yıllık Tasarruf/Gelir | 3.433.500 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 1,98 yıl (~23,8 ay) |
| NPV (%10, 20 yıl) | 22.400.000 EUR |
| IRR | %48 |
| CO2 Azaltma | 28.500 ton CO2/yıl |
| Spesifik Enerji İyileştirmesi | 3.450 → 3.120 kJ/kg klinker (%9,6 iyileşme) |

### 6.6 Çıkarılan Dersler

- Çimento sektöründe pinch analizi, klasik HEN tasarımından çok proses modifikasyonu ve enerji dönüşümü (ORC, WHRS) odaklıdır.
- Yüksek sıcaklıklarda (>300 degC) delta-T-min=40 degC veya üzeri uygulanmalıdır.
- Klinker soğutucu, çimento fabrikasının en büyük ısı geri kazanım kaynağıdır; orta hava (Secondary/Tertiary Air) yönetimi kritik önem taşır.
- Bypass gazı ve fırın egzostundaki alkali/klor/sülfat bileşikleri, ısı değiştirici malzeme seçimini doğrudan etkiler.
- ORC sistemi, düşük-orta sıcaklıklı atık ısıyı elektriğe dönüştürmede ekonomik olarak uygulanabilirdir; ancak yatırım maliyeti yüksektir.
- Sektördeki en iyi uygulamalara (BAT — Best Available Techniques) kıyaslama, iyileştirme potansiyelini belirlemede temel referanstır (EU BREF, 2013).

---

## 7. Otomotiv Fabrikası (Automotive Plant)

### 7.1 Tesis Profili

| Parametre | Değer |
|---|---|
| Tesis Tipi | Otomotiv boya hattı (Paint Shop) |
| Kapasite | 1.200 araç/gün (3 vardiya) |
| Çalışma Rejimi | Sürekli, 6.000 saat/yıl |
| Mevcut Enerji Tüketimi | 8,5 MW ısıtma, 5,2 MW soğutma |
| Birincil Enerji Kaynağı | Doğal gaz, buhar ve sıcak su |
| Boya Prosesi | E-Coat (Kataforez) + Primer + Taban Boya + Vernik (4 kat) |
| Sıcaklık Aralığı | 20-200 degC (düşük sıcaklık profili) |

Otomotiv boya hatları, düşük-orta sıcaklık aralığında yoğun ısıtma ve soğutma gerektiren proseslerdir. Kabin klimatizasyonu (sıcaklık ve nem kontrolü), fırın kurutma ve banyo ısıtma ana enerji tüketicileridir. Bu düşük sıcaklık profili, ısı pompası (Heat Pump) entegrasyonu için ideal bir zemin oluşturur.

### 7.2 Akış Verileri Özeti

**9 sıcak akış** ve **7 soğuk akış** tanımlanmıştır.

**Sıcak Akışlar (Hot Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| H1 | E-Coat fırın egzostu | 200 | 100 | 12,5 | 1.250 |
| H2 | Primer fırın egzostu | 180 | 90 | 10,8 | 972 |
| H3 | Taban boya fırın egzostu | 165 | 80 | 14,2 | 1.207 |
| H4 | Vernik fırın egzostu | 160 | 75 | 11,5 | 978 |
| H5 | Boya kabini egzost havası | 23 | 18 | 420,0 | 2.100 |
| H6 | RTO (Regenerative Thermal Oxidizer) çıkış | 250 | 120 | 8,5 | 1.105 |
| H7 | E-Coat banyo soğutma | 32 | 28 | 85,0 | 340 |
| H8 | Fosfatlama dönüş suyu | 55 | 35 | 18,5 | 370 |
| H9 | DI su (Deiyonize Su) soğutma | 35 | 20 | 22,0 | 330 |

**Soğuk Akışlar (Cold Streams):**

| Akış No | Tanım | Ts (degC) | Tt (degC) | CP (kW/degC) | Q (kW) |
|---|---|---|---|---|---|
| C1 | Boya kabini taze hava ısıtma (kış) | -5 | 23 | 380,0 | 10.640 |
| C2 | E-Coat banyo ısıtma (başlangıç) | 20 | 32 | 85,0 | 1.020 |
| C3 | Fosfatlama banyosu ısıtma | 20 | 55 | 18,5 | 648 |
| C4 | Fırın taze hava ön ısıtma | 5 | 80 | 15,0 | 1.125 |
| C5 | DI su ön ısıtma (yıkama) | 8 | 40 | 22,0 | 704 |
| C6 | Enerji santrali kazan besleme suyu | 15 | 90 | 5,5 | 413 |
| C7 | Ofis/idari bina ısıtma (kış) | 18 | 22 | 125,0 | 500 |

**Kritik Gözlem:** Otomotiv boya hattında en büyük enerji tüketicisi boya kabini havalandırma (C1, 10.640 kW kış pik) olmasına rağmen, kabin egzostu (H5) sıcaklığı sadece 23 degC'dir. Bu durum, klasik pinch analizi ile direkt geri kazanımı neredeyse imkansız kılar ve ısı pompası çözümünü zorunlu hale getirir.

### 7.3 Pinch Analizi Sonuçları

| Parametre | Mevcut Durum | Hedef (Target) | Tasarruf |
|---|---|---|---|
| delta-T-min (degC) | — | 10 | — |
| Pinch Sıcaklığı (degC) | — | 32 (sıcak taraf: 37, soğuk taraf: 27) | — |
| QH,min (MW) | 8,50 | 5,20 | 3,30 MW (%38,8) |
| QC,min (MW) | 5,20 | 1,90 | 3,30 MW (%63,5) |

**GCC Analizi — Isı Pompası Yerleştirme (Heat Pump Placement):**

Grand Composite Curve analizi, pinch noktası (32 degC) etrafında büyük bir ısı cebi olduğunu göstermiştir. Bu cep, ısı pompası ile köprülenebilir:
- Pinch altından alınacak ısı (evaporatör tarafı): 2.400 kW, 18-28 degC
- Pinch üstüne verilecek ısı (kondenser tarafı): 3.200 kW, 35-55 degC
- Gerekli kompresör işi: 800 kW_e
- COP (Coefficient of Performance): 4,0

Isı pompası, GCC üzerinde pinch noktasını çaprazlayan (Cross-Pinch) tek termodinamik olarak geçerli yöntemdir. Doğrudan ısı transferi pinch ihlali yaratırken, ısı pompası hem ısıtma hem soğutma yükünü eş zamanlı olarak azaltır.

### 7.4 HEN Tasarımı ve Isı Pompası Entegrasyonu

1. **Fırın Egzostu Kaskad Geri Kazanımı:** 4 adet fırın egzostu (H1-H4) birleştirilerek (manifold), kaskad ısı geri kazanım sistemi oluşturulmuştur:
   - 1. kademe (200-120 degC): Fırın taze hava ön ısıtma (C4). Kazanılan yük: 1.125 kW.
   - 2. kademe (120-60 degC): Kazan besleme suyu ve fosfatlama ön ısıtma (C6, C3). Kazanılan yük: 820 kW.
   - Toplam fırın egzostu geri kazanımı: 1.945 kW.

2. **RTO Atık Isı Geri Kazanımı:** RTO çıkışından (H6, 250 degC) buhar veya sıcak su üretimi. RTO mevcut durumda %95 termal rejenerasyon veriminde çalışmaktadır; ancak kalan atık ısıdan 680 kW geri kazanılmıştır. Bu ısı, fırın ön ısıtma ve DI su ısıtma için kullanılmaktadır.

3. **Endüstriyel Isı Pompası (Industrial Heat Pump) Sistemi:**
   - Tip: R-1234ze(E) akışkanlı vidalı kompresörlü (Screw Compressor)
   - Evaporatör: Boya kabini egzost havası (H5) ve E-Coat banyo soğutma (H7) kaynak olarak kullanılmıştır.
   - Kondenser: Boya kabini taze hava ön ısıtma (C1) ve ofis ısıtma (C7).
   - Isı pompası kapasitesi: 3.200 kW termal (kondenser tarafı).
   - Elektrik tüketimi: 800 kW_e.
   - COP: 4,0 (mevsimsel ortalama SCOP: 3,6)
   - Bu sistem, soğutma yükünü 2.400 kW azaltırken, ısıtma yükünü 3.200 kW azaltmaktadır.

4. **DI Su ve Fosfatlama Entegrasyonu:** H8 (fosfatlama dönüş, 55 degC) ve H9 (DI su, 35 degC) akışlarından C5 (DI su ön ısıtma) için geri kazanım. Kazanılan yük: 450 kW.

### 7.5 Ekonomik Sonuçlar

| Ekonomik Parametre | Değer |
|---|---|
| Toplam Yatırım (CAPEX) | 1.250.000 EUR |
| Endüstriyel Isı Pompası | 680.000 EUR |
| Isı Değiştiriciler (Fırın Kaskad, 6 adet) | 285.000 EUR |
| RTO Isı Geri Kazanım Üniteleri | 135.000 EUR |
| Boru, Kanal ve Montaj | 105.000 EUR |
| Kontrol ve Otomasyon | 25.000 EUR |
| Mühendislik | 20.000 EUR |
| Yıllık Isıtma Tasarrufu (Doğrudan Geri Kazanım) | 2.250 kW x 6.000 h x 0,040 EUR/kWh = 540.000 EUR/yıl |
| Yıllık Isıtma Tasarrufu (Isı Pompası) | 3.200 kW x 5.000 h x 0,040 EUR/kWh = 640.000 EUR/yıl |
| Yıllık Soğutma Tasarrufu (Isı Pompası) | 2.400 kW x 5.000 h x 0,015 EUR/kWh = 180.000 EUR/yıl |
| Isı Pompası Elektrik Maliyeti (Negatif) | -800 kW x 5.000 h x 0,085 EUR/kWh = -340.000 EUR/yıl |
| Toplam Yıllık Net Tasarruf | 1.020.000 EUR/yıl |
| Basit Geri Ödeme Süresi (SPP) | 1,23 yıl (~14,7 ay) |
| NPV (%8, 15 yıl) | 7.480.000 EUR |
| IRR | %82 |
| CO2 Azaltma | 5.200 ton CO2/yıl |

### 7.6 Çıkarılan Dersler

- Otomotiv boya hatlarında düşük sıcaklık profili nedeniyle, pinch analizi ısı pompası yerleştirme analizi (Heat Pump Placement) ile birlikte yürütülmelidir.
- GCC üzerinde ısı pompası yerleştirme, pinch noktasını çaprazlayan tek termodinamik olarak meşru yöntemdir.
- Boya kabini havalandırma en büyük enerji tüketicisi olmasına rağmen, düşük sıcaklık farkı nedeniyle doğrudan geri kazanım uygulanamaz; ısı pompası bu engeli aşar.
- Fırın egzostlarının birleştirilmesi (manifold), ölçek ekonomisi sağlayarak ısı değiştirici maliyetini düşürür.
- RTO sistemlerinde termal rejenerasyon oranı yüksek olsa da kalan atık ısı yine de değerli bir kaynaktır.
- Isı pompası COP değeri, kaynağın ve kullanıcının sıcaklık seviyesine çok duyarlıdır; pinch analizi ile bu eşleşmenin optimizasyonu kritiktir.

---

## 8. Karşılaştırma Tablosu (Comparison Table)

Aşağıdaki tablo, yedi vaka çalışmasının temel parametrelerini yan yana karşılaştırmaktadır:

| Parametre | Petrokimya | Süt İşleme | Tekstil | Kağıt | Kimya | Çimento | Otomotiv |
|---|---|---|---|---|---|---|---|
| **Akış Sayısı (Sıcak+Soğuk)** | 28+22 = 50 | 6+5 = 11 | 8+6 = 14 | 12+10 = 22 | 20+15 = 35 | 5+4 = 9 | 9+7 = 16 |
| **delta-T-min (degC)** | 20 | 5 | 15 | 10 | 20 | 40 | 10 |
| **Pinch T (degC)** | 128 | 42 | 72 | 58 | 95 | 310 | 32 |
| **Mevcut QH (MW)** | 85,0 | 3,8 | 4,2 | 48,0 | 6,5 | 125,0 | 8,5 |
| **QH,min (MW)** | 51,8 | 2,42 | 2,90 | 36,0 | 4,85 | 106,0 | 5,20 |
| **Isıtma Tasarrufu (%)** | 39,1 | 36,3 | 31,0 | 25,0 | 25,4 | 15,2 | 38,8 |
| **Gerçekleşen Tasarruf (%)** | ~31 | ~36 | ~31 | ~25 | ~20 | ~15 | ~39 |
| **Toplam Yatırım (EUR)** | 4.200.000 | 120.000 | 185.000 | 1.850.000 | 420.000 | 6.800.000 | 1.250.000 |
| **Yıllık Tasarruf (EUR/yıl)** | 8.210.000 | 455.150 | 710.430 | 3.003.240 | 524.160 | 3.433.500 | 1.020.000 |
| **SPP (yıl)** | 0,51 | 0,26 | 0,26 | 0,62 | 0,80 | 1,98 | 1,23 |
| **NPV (EUR)** | 58.200.000 | 2.930.000 | 4.180.000 | 23.800.000 | 3.150.000 | 22.400.000 | 7.480.000 |
| **CO2 Azaltma (ton/yıl)** | 42.000 | 2.150 | 1.980 | 18.500 | 3.850 | 28.500 | 5.200 |
| **Anahtar Teknoloji** | Shell-tube HEX retrofit | PHE, ısı pompası | TES tank, kaskad yıkama | Run-around coil, türbin | TES, HIDiC | ORC, WHRS | Endüstriyel ısı pompası |
| **Özel Zorluk** | Kriyojenik alt-pinch | Hijyen kısıtları | Batch operasyon, fouling | Nem yönetimi | Zaman-bağımlı profil | Yüksek T, korozyon | Düşük T farkı |

### Sektörel Eğilimler

- **En yüksek mutlak tasarruf:** Petrokimya ve çimento (büyük ölçek etkisi)
- **En hızlı geri ödeme:** Gıda ve tekstil (düşük yatırım, yüksek enerji fiyatı oranı)
- **En karmaşık analiz:** Kimya (batch-sürekli karma) ve petrokimya (akış sayısı)
- **En yenilikçi teknoloji:** Otomotiv (ısı pompası), çimento (ORC)
- **En yüksek ek fayda (su):** Tekstil (%15 su tasarrufu)

---

## 9. Öğrenilen Dersler (Lessons Learned)

Yedi sektörel vaka çalışmasından elde edilen ortak temalar ve çapraz sektörel dersler aşağıda özetlenmektedir:

### 9.1 Genel Prensipler

1. **delta-T-min Seçimi Sektöre Özgüdür:** Gıda sektöründe 5 degC, çimento sektöründe 40 degC — on kat fark. Fouling, malzeme kısıtları, ısı transfer katsayıları ve ekonomik optimizasyon (Supertargeting) delta-T-min'i belirler.

2. **Retrofit, Grassroots'un %70-85'ine Ulaşabilir:** Mevcut tesislerde pinch hedefinin tamamına ulaşmak maliyet-etkin olmayabilir; %70-85 oranı genellikle optimum ekonomik noktadır.

3. **Pinch İhlali (Cross-Pinch Heat Transfer) Her Yerde Vardır:** Mevcut tesislerin tamamında pinch ihlali tespit edilmiştir. Bu ihlallerin kaldırılması, ilk ve en etkili müdahaledir.

4. **Büyük Ölçek, Büyük Tasarruf:** Mutlak tasarruf miktarı tesis ölçeği ile doğru orantılıdır. Ancak yüzdesel iyileşme ölçekten bağımsız olabilir.

### 9.2 Teknoloji Seçimi

5. **Isı Pompası, Düşük Sıcaklıklı Proseslerde Oyun Değiştiricidir:** Otomotiv, gıda ve tekstil sektörlerinde ısı pompası entegrasyonu, geleneksel ısı değiştirici çözümlerinin ötesinde tasarruf sağlamıştır. Pinch analizi ile ısı pompası yerleştirme analizi her zaman birlikte yapılmalıdır.

6. **TES, Batch Proseslerin Anahtarıdır:** Tekstil ve kimya sektörlerinde termal enerji depolama olmadan pinch hedeflerine ulaşılamaz. TES boyutlandırması, zaman dilimli ısı dengesi profiline göre optimize edilmelidir.

7. **ORC ve WHRS, Yüksek Sıcaklık Atık Isıda Geçerlidir:** Çimento gibi yüksek sıcaklıklı sektörlerde, ısı geri kazanımının ötesinde elektrik üretimi (Waste-to-Power) ekonomik olarak uygulanabilirdir.

8. **Buhar Sistemi Optimizasyonu, Proses Pinch'in Tamamlayıcısıdır:** Kağıt fabrikası örneğinde olduğu gibi, proses pinch analizi ve buhar sistemi optimizasyonu birlikte yürütüldüğünde sinerjik faydalar ortaya çıkar.

### 9.3 Proje Yönetimi

9. **Erken Operatör Katılımı Kritiktir:** Tüm vaka çalışmalarında, operasyon ekibinin proje tasarım aşamasına erken dahil edilmesi başarı oranını artırmıştır. Kağıt üzerinde optimal çözüm, operasyonel kısıtlar nedeniyle uygulanamayabilir.

10. **Aşamalı Uygulama Tercih Edilir:** Büyük tesislerde (petrokimya, çimento) tüm modifikasyonların aynı anda yapılması yerine, aşamalı (phased) uygulama riski azaltır ve her aşamada kazanılan deneyim sonraki aşamalara aktarılır.

11. **Enerji-Su-Emisyon Üçlü Optimizasyonu:** Tekstil örneğinde görüldüğü gibi, enerji tasarrufunun ötesinde su tasarrufu ve CO2 azaltma hedefleri birlikte değerlendirilmelidir. Çoklu fayda (Multiple Benefits) yaklaşımı, proje fizibilitesini güçlendirir.

12. **Ölçüm ve Doğrulama (M&V — Measurement and Verification):** Her vaka çalışmasında, uygulama sonrası performans ölçümü yapılmıştır. Gerçekleşen tasarruf ile hedeflenen tasarruf arasındaki fark, gelecekteki projeler için kalibrasyon verisi sağlar. IPMVP (International Performance Measurement and Verification Protocol) standardının takip edilmesi önerilmektedir.

### 9.4 Ekonomik Değerlendirme

13. **SPP Tek Başına Yeterli Değildir:** Basit geri ödeme süresi hızlı bir gösterge olsa da, NPV ve IRR analizleri daha sağlıklı karar verme imkanı sağlar. Çimento vakasında SPP=1,98 yıl olmasına rağmen NPV=22,4 milyon EUR ile en yüksek ikinci getiri elde edilmiştir.

14. **Enerji Fiyat Duyarlılığı:** Tüm ekonomik sonuçlar enerji fiyatlarına duyarlıdır. Doğal gaz ve elektrik fiyatlarında +/-%20 senaryo analizi yapılmalıdır. Karbon fiyatlandırması (EU ETS) eklendiğinde, özellikle çimento ve petrokimya sektörlerinde proje getirileri önemli ölçüde artmaktadır.

---

## İlgili Dosyalar

- `factory/pinch/fundamentals.md` — Pinch analizi temel kavramları ve terminoloji
- `factory/pinch/practical_guide.md` — Adım adım pinch analizi uygulama rehberi
- `factory/pinch/hen_retrofit.md` — Mevcut tesislerde HEN retrofit yöntemleri
- `factory/pinch/cost_estimation.md` — Isı değiştirici maliyet tahmini ve ekonomik analiz
- `factory/cross_equipment.md` — Ekipmanlar arası ısı entegrasyonu fırsatları
- `factory/prioritization.md` — Enerji tasarruf projelerinin önceliklendirilmesi
- `factory/factory_benchmarks.md` — Sektörel enerji verimliliği benchmark değerleri

## Referanslar

1. Linnhoff, B. (1994). "Use Pinch Analysis to Knock Down Capital Costs and Emissions." *Chemical Engineering Progress*, 90(8), 32-57.
2. Kemp, I.C. (2007). *Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy*. 2nd ed., Butterworth-Heinemann.
3. Klemes, J.J. (2013). *Handbook of Process Integration: Minimisation of Energy and Water Use, Waste and Emissions*. Woodhead Publishing.
4. IEA (2018). "Energy Efficiency in Industrial Processes." International Energy Agency Technical Report.
5. U.S. DOE (2016). "Waste Heat Recovery: Technology and Opportunities in U.S. Industry." Department of Energy Report.
6. EU BREF (2013). "Best Available Techniques Reference Document for the Production of Cement, Lime and Magnesium Oxide." European Commission.
7. Savulescu, L.E., Kim, J.K., Smith, R. (2005). "Studies on simultaneous energy and water minimisation." *Chemical Engineering Science*, 60(11), 3279-3290.
8. Walmsley, T.G., Walmsley, M.R.W., Atkins, M.J., Neale, J.R. (2014). "Integration of industrial solar and gaseous waste heat into heat recovery loops using constant and variable temperature storage." *Energy*, 75, 53-67.
9. IPMVP (2012). "International Performance Measurement and Verification Protocol: Concepts and Options for Determining Energy and Water Savings." Efficiency Valuation Organization.
10. Wang, Y., Smith, R. (2005). "Time Pinch Analysis." *Chemical Engineering Research and Design*, 83(A8), 981-993.
