---
title: "Güneş Enerjisi ile Ön Isıtma (Solar Air Preheating for Dryers)"
category: dryer
equipment_type: dryer
keywords: [güneş enerjisi, solar preheating, solar dryer, güneş kolektörü, yenilenebilir enerji]
related_files: [dryer/formulas.md, dryer/benchmarks.md, dryer/solutions/exhaust_heat_recovery.md, dryer/sectors/food_drying.md, dryer/sectors/wood_drying.md]
use_when: ["Güneş ön ısıtma potansiyeli değerlendirilirken", "Yenilenebilir enerji entegrasyonu düşünüldüğünde"]
priority: low
last_updated: 2026-02-01
---
# Güneş Enerjisi ile Ön Isıtma (Solar Air Preheating for Dryers)

> Son güncelleme: 2026-02-01

## Genel Bakış

Endüstriyel kurutma proseslerinde hava ısıtma, toplam enerji tüketiminin en büyük kalemini oluşturur. Konvansiyonel sistemlerde bu enerji doğalgaz, LPG veya elektrikle sağlanır. Güneş enerjisi kolektörleri ile kurutma besleme havasının 10-40°C ön ısıtılması, konvansiyonel ısıtıcı yükünü doğrudan azaltarak yakıt tüketiminde %15-45 tasarruf potansiyeli sunar.

**Temel Fayda:** Güneş enerjisi sıfır yakıt maliyetiyle kurutma havasını ön ısıtarak fosil yakıt tüketimini ve karbon emisyonlarını düşürür.

**Tipik Yakıt Tasarrufu:** %15-45 (bölgeye, mevsime ve sistem konfigürasyonuna bağlı)
**Tipik Geri Ödeme Süresi (SPP):** 3-6 yıl (yakıt maliyeti ve teşviklere bağlı)
**Güneş Payı (Solar Fraction):** Yıllık bazda %20-50

## Çalışma Prensibi

Güneş enerjisi kolektörleri (solar air collectors), güneş radyasyonunu yakalayarak kurutma besleme havasını doğrudan veya dolaylı yollarla ön ısıtır. Konvansiyonel ısıtıcı (brülör veya elektrikli rezistans), yalnızca kalan sıcaklık farkını kapatmak için devreye girer. Bu sayede yakıt tüketimi, güneş enerjisinin sağladığı ön ısıtma miktarı kadar azalır.

### Enerji Akış Diyagramı

```
Konvansiyonel sistem (güneş enerjisiz):
T_ambient (20°C) ---> [Konvansiyonel Isıtıcı] ---> T_kurutma (70°C)
ΔT = 50°C ---> Tamamı fosil yakıt

Solar ön ısıtmalı sistem:
T_ambient (20°C) ---> [Güneş Kolektörü] ---> T_preheat (45°C) ---> [Konvansiyonel Isıtıcı] ---> T_kurutma (70°C)
Solar ΔT = 25°C ---> Güneş enerjisi (%50 enerji tasarrufu)
Konvansiyonel ΔT = 25°C ---> Fosil yakıt (kalan %50)
```

### Temel Enerji Dengesi Formülleri

```
Q_total = Q_solar + Q_conventional

Q_solar = m_air x c_p x (T_preheat - T_ambient)     [kW]
Q_conventional = m_air x c_p x (T_kurutma - T_preheat)  [kW]

Solar Fraction (SF) = Q_solar / Q_total               [-]

Burada:
- m_air       = Hava kütle debisi [kg/s]
- c_p         = Havanın özgül ısısı = 1.005 kJ/(kg.K)
- T_ambient   = Ortam sıcaklığı [°C]
- T_preheat   = Solar ön ısıtma sonrası hava sıcaklığı [°C]
- T_kurutma   = Hedef kurutma sıcaklığı [°C]
```

Güneş kolektörünün sağladığı ön ısıtma (T_preheat - T_ambient) genellikle 10-40°C aralığındadır ve kolektör tipine, güneş radyasyonuna ve hava debisine bağlıdır.

## Kolektör Tipleri

Kurutma havasının güneş enerjisiyle ön ısıtılması için üç temel kolektör teknolojisi kullanılmaktadır.

### Teknoloji Karşılaştırma Tablosu

| Kolektör Tipi | Akışkan | ΔT Artışı [°C] | Verim (eta) | Maliyet [EUR/m2] | En Uygun Kullanım |
|---------------|---------|-----------------|-------------|-------------------|-------------------|
| Düz plakalı hava kolektörü (Flat plate air collector) | Hava | 15-40 | 0.40-0.60 | 150-250 | Genel amaçlı ön ısıtma |
| Vakumlu tüp kolektör (Evacuated tube) | Su (hava eşanjörü ile) | 30-80 | 0.45-0.65 | 250-400 | Yüksek sıcaklık gereksinimi, sınırlı alan |
| Transpire güneş duvarı (Transpired solar wall / Solarwall) | Hava | 10-30 | 0.50-0.70 | 100-180 | Büyük cephe alanı, düşük-orta T ön ısıtma |

### 1. Düz Plakalı Hava Kolektörü (Flat Plate Air Collector)

En yaygın kullanılan güneş kolektörü tipidir. Cam örtülü absorber plaka güneş radyasyonunu emer; plaka üzerinden geçen hava doğrudan ısıtılır.

- **Avantajlar:** Kanıtlanmış teknoloji, geniş tedarikçi ağı, orta-yüksek sıcaklık artışı (15-40°C), ısı eşanjörü gerektirmez (doğrudan hava ısıtma)
- **Dezavantajlar:** UTC'ye göre daha pahalı, cam bakımı gerekir (temizlik, kırılma riski), çatı taşıma kapasitesi kontrol edilmeli
- **Verim:** eta = 0.40-0.60 (güneş radyasyonu ve hava debisine bağlı)

### 2. Vakumlu Tüp Kolektör (Evacuated Tube Collector)

İç içe cam tüpler arasında vakum yalıtımı sayesinde yüksek sıcaklıklarda bile düşük ısı kaybı sağlar. Genellikle suyu ısıtır; kurutma havasına aktarım bir hava-su ısı eşanjörü (water-to-air heat exchanger) aracılığıyla yapılır.

- **Avantajlar:** En yüksek sıcaklık artışı (30-80°C), soğuk iklimlerde bile iyi performans, diffüz radyasyonu da değerlendirir
- **Dezavantajlar:** En pahalı seçenek, kırılganlık riski (cam tüpler), dolaylı ısıtma (su-hava eşanjörü gerektirir, ek maliyet ve verim kaybı), düşük sıcaklıklı kurutma uygulamalarında gereğinden fazla (overkill)
- **Verim:** eta = 0.45-0.65

### 3. Transpire Güneş Duvarı (Transpired Solar Wall / Solarwall)

Güneşe bakan metal duvar üzerindeki mikro deliklerden hava çekilerek ısıtılır. Fabrika cephelerine veya çatılara monte edilir.

- **Avantajlar:** Basit yapı, en düşük birim maliyet (100-180 EUR/m2), geniş yüzeylerde kolay uygulama, düşük basınç kaybı, uzun ömür (25-30 yıl), cam yok (kırılma riski düşük)
- **Dezavantajlar:** Düşük-orta sıcaklık artışı (10-30°C), rüzgar etkisine duyarlı, yüksek sıcaklık gerektiren uygulamalarda yetersiz
- **Verim:** eta = 0.50-0.70

## Güneş Kaynağı

### Türkiye Güneş Enerjisi Potansiyeli

Türkiye, yıllık 1,500-2,000 kWh/m2 güneş radyasyonu ile güneş enerjisi uygulamaları için mükemmel bir potansiyele sahiptir. Özellikle Güneydoğu Anadolu, Akdeniz ve Ege bölgeleri en yüksek güneşlenme değerlerine ulaşır.

### Bölgesel Güneş Radyasyonu Verileri

| Bölge | Yıllık Radyasyon [kWh/m2/yıl] | Günlük Ortalama [kWh/m2/gün] | Güneşlenme Süresi [saat/yıl] | Potansiyel |
|-------|-------------------------------|------------------------------|------------------------------|------------|
| Güneydoğu Anadolu | 1,825-2,000 | 5.0-5.5 | 2,800-3,100 | Cok yüksek |
| Akdeniz | 1,640-1,900 | 4.5-5.2 | 2,600-2,900 | Yüksek |
| Ege | 1,570-1,825 | 4.3-5.0 | 2,500-2,800 | Yüksek |
| Ic Anadolu | 1,533-1,752 | 4.2-4.8 | 2,500-2,800 | Yüksek |
| Dogu Anadolu | 1,460-1,752 | 4.0-4.8 | 2,400-2,800 | Yüksek (soguk) |
| Marmara | 1,278-1,533 | 3.5-4.2 | 2,200-2,500 | Orta |
| Karadeniz (kıyı) | 1,095-1,387 | 3.0-3.8 | 1,600-2,000 | Düsük-Orta |

**Kaynak:** Türkiye Güneş Enerjisi Potansiyel Atlası (GEPA), T.C. Enerji ve Tabii Kaynaklar Bakanlığı

### Mevsimsel Değişkenlik

Güneş radyasyonu mevsimsel olarak önemli farklılık gösterir. Kış aylarında güneş radyasyonu yaz değerlerinin %30-50'sine düşebilir:

| Ay | Günlük Ortalama Radyasyon (Ic Anadolu) [kWh/m2/gün] | Solar Katkı Oranı |
|----|------------------------------------------------------|-------------------|
| Ocak | 2.0-2.5 | Düsük (%10-20) |
| Nisan | 4.5-5.0 | Yüksek (%35-50) |
| Temmuz | 6.5-7.5 | Maksimum (%50-65) |
| Ekim | 3.5-4.0 | Orta (%25-40) |

Bu nedenle yıllık ortalama solar fraction %20-50 arasında değişir ve konvansiyonel yedek sistem (backup) her zaman gereklidir.

## Konfigürasyonlar

Güneş enerjisi ile kurutma havasının ön ısıtılması için üç temel sistem konfigürasyonu uygulanmaktadır.

### 1. Doğrudan Güneş Hava Isıtma (Direct Solar Air Heating)

Hava doğrudan güneş kolektöründen geçerek ısınır ve kurutucuya beslenir. Ek ısı eşanjörü gerekmez.

```
[Ortam Havası] ---> [Güneş Hava Kolektörü] ---> [Konvansiyonel Isıtıcı] ---> [Kurutucu]
```

- **Avantajlar:** Basit sistem, düşük maliyet, yüksek verim (doğrudan ısı transferi)
- **Dezavantajlar:** Termal depolama zor, gece çalışma imkanı yok
- **En uygun:** Gündüz çalışan kurutucular, düz plakalı veya UTC kolektörlerle

### 2. Dolaylı Isıtma — Su Döngüsü (Indirect Heating — Water Loop)

Güneş kolektörü suyu ısıtır; sıcak su bir hava-su ısı eşanjörü aracılığıyla kurutma havasını ön ısıtır. Sıcak su tankı termal depolama görevi üstlenebilir.

```
[Güneş Kolektörü] ---> [Sıcak Su Tankı] ---> [Hava-Su Isı Eşanjörü] ---> [Kurutma Havası]
```

- **Avantajlar:** Termal depolama imkanı (tampon tank), kolektör-kurutucu mesafesi uzak olabilir, vakumlu tüp kolektörlerle uyumlu
- **Dezavantajlar:** Ek bileşenler (pompa, eşanjör, tank), sistem verimi düşer (%5-10 kayıp), daha yüksek yatırım maliyeti
- **En uygun:** Gece veya bulutlu saatlerde de katkı istenen sistemler, yüksek sıcaklık gereksinimleri

### 3. Hibrit Sistem — Güneş + Konvansiyonel Yedek (Hybrid Solar + Conventional Backup)

Güneş enerjisi mevcut olduğunda güneş ön ısıtma devrede; güneş yetersiz olduğunda konvansiyonel ısıtıcı otomatik olarak devreye girer. Bu konfigürasyon, endüstriyel uygulamalarda zorunlu standarttır.

```
Kontrol Stratejisi:
1. T_solar_out ölç (kolektör çıkış sıcaklığı)
2. Eğer T_solar_out >= T_hedef   --> Konvansiyonel kapalı (tam güneş enerjisi)
3. Eğer T_ambient < T_solar_out < T_hedef  --> Konvansiyonel fark kadar çalışır (hibrit mod)
4. Eğer T_solar_out ~ T_ambient  --> Konvansiyonel tam yük (gece/bulutlu hava)
```

- **Avantajlar:** Kesintisiz üretim garantisi, güneş enerjisi varken yakıt tasarrufu, otomatik geçiş
- **Dezavantajlar:** Kontrol sistemi karmaşıklığı, konvansiyonel ısıtıcı her zaman yedekte tutulmalı
- **En uygun:** Tüm endüstriyel kurutma uygulamaları (fiilen standart konfigürasyon)

## Boyutlandırma

### Kolektör Alanı Hesabı

Kolektör alanı, hava debisi ve hedeflenen sıcaklık artışına (delta T) göre belirlenir.

```
Gerekli ön ısıtma gücü:
Q_preheat = m_air x c_p x (T_preheat - T_ambient)     [kW]

Kolektör alanı:
A_collector = Q_preheat / (I_pik x eta_collector)       [m2]

Burada:
- m_air         = Hava kütle debisi [kg/s]
- c_p           = 1.005 kJ/(kg.K)
- T_preheat     = Hedef ön ısıtma sıcaklığı [°C]
- T_ambient     = Ortam sıcaklığı [°C]
- I_pik         = Pik güneş radyasyonu [kW/m2] (tipik: 0.7-0.9 kW/m2)
- eta_collector = Kolektör verimi [-] (0.40-0.65)
```

### Pratik Boyutlandırma Kuralı (Rule of Thumb)

Her 100 m3/h hava debisi için **0.5-1.0 m2 kolektör alanı** gerekir:

| Hava Debisi [m3/h] | Tahmini Kolektör Alanı [m2] | Yaklaşık ΔT [°C] |
|--------------------|-----------------------------|-------------------|
| 1,000 | 5-10 | 10-20 |
| 2,500 | 12-25 | 10-20 |
| 5,000 | 25-50 | 10-20 |
| 10,000 | 50-100 | 10-20 |
| 20,000 | 100-200 | 10-20 |

**Not:** Daha yüksek ΔT hedefleniyorsa kolektör alanı oransal olarak artırılmalıdır.

### Yıllık Enerji Üretimi Tahmini

```
E_solar_yillik = A_collector x I_yillik x eta_collector x f_kullanim    [kWh/yıl]

Burada:
- A_collector   = Kolektör alanı [m2]
- I_yillik      = Yıllık güneş radyasyonu [kWh/m2/yıl]
- eta_collector = Kolektör ortalama verimi [-]
- f_kullanim    = Güneş ile üretim örtüşme faktörü [-] (tipik: 0.4-0.8)
```

## Hesaplama

### Örnek Hesap: 5,000 m3/h Kurutma Havası, 50 m2 Kolektör

**Senaryo:** Gıda kurutucu, konvektif tip, doğalgaz yakıtlı, Akdeniz bölgesi

| Parametre | Değer |
|-----------|-------|
| Hava debisi | 5,000 m3/h |
| Hava kütle debisi (m_air) | 5,000 / 3,600 x 1.1 = 1.528 kg/s (rho ~ 1.1 kg/m3 @ 25°C) |
| Ortam sıcaklığı (T_ambient) | 25°C (yaz ortalaması) |
| Hedef kurutma sıcaklığı (T_kurutma) | 65°C |
| Güneş kolektör alanı (A_collector) | 50 m2 (düz plakalı hava kolektörü) |
| Kolektör verimi (eta) | 0.50 |
| Pik güneş radyasyonu (I_pik) | 0.80 kW/m2 |
| Yıllık güneş radyasyonu (I_yillik) | 1,750 kWh/m2/yıl |
| Güneş-üretim örtüşme faktörü (f_kullanim) | 0.60 |
| Kazan/brülör verimi | 0.90 |
| Doğalgaz fiyatı | 0.06 EUR/kWh |

**Adım 1 — Pik Ön Isıtma Gücü:**

```
Q_solar_pik = A_collector x I_pik x eta
            = 50 x 0.80 x 0.50
            = 20.0 kW

ΔT_preheat = Q_solar_pik / (m_air x c_p)
           = 20.0 / (1.528 x 1.005)
           = 13.0°C

T_preheat = 25 + 13.0 = 38.0°C (güneşli saatlerde)
```

Konvansiyonel ısıtıcı yükü güneşli saatlerde: 65 - 38 = 27°C (38°C'den 65°C'ye)
Konvansiyonel ısıtıcı yükü güneşsiz saatlerde: 65 - 25 = 40°C (tamamı fosil yakıt)

**Pik saatlerde yakıt tasarrufu oranı:** 13 / 40 = %32.5

**Adım 2 — Yıllık Enerji Üretimi:**

```
E_solar = A_collector x I_yillik x eta x f_kullanim
        = 50 x 1,750 x 0.50 x 0.60
        = 26,250 kWh/yıl
```

**Adım 3 — Yakıt Tasarrufu:**

```
Gaz_tasarruf = E_solar / eta_kazan
             = 26,250 / 0.90
             = 29,167 kWh/yıl doğalgaz eşdeğeri
```

**Adım 4 — Parasal Tasarruf:**

```
Yillik_tasarruf = Gaz_tasarruf x birim_fiyat
               = 29,167 x 0.06
               = 1,750 EUR/yıl
```

**Adım 5 — CO2 Emisyon Azaltımı:**

```
CO2_azaltim = Gaz_tasarruf x 0.202 (kg CO2/kWh dogalgaz)
            = 29,167 x 0.202
            = 5,892 kg CO2/yıl ~ 5.9 ton CO2/yıl
```

### Exergy Perspektifi

Güneş enerjisinin exergy verimi, kolektör sıcaklığına bağlıdır. Düşük sıcaklıklı güneş ısıtma (40-60°C) termodinamik olarak düşük exergy kalitesindedir ancak sıfır yakıt maliyetiyle elde edildiği için ekonomik değeri yüksektir:

```
Kolektör çıkış exergy oranı (Carnot yaklaşımı):
eta_exergy_solar = 1 - T0/T_preheat = 1 - 298/311 = 0.042 (yalnızca %4.2 exergy verimi)
```

Bu düşük exergy verimi, güneş ön ısıtmanın "yüksek kaliteli" bir enerji kaynağı olmadığını gösterir. Ancak exergy kalitesi düşük olsa da maliyet sıfır olduğundan, toplam tesis exergo-ekonomik performansına pozitif katkı sağlar.

## Ekonomik Analiz

### Yatırım Maliyeti Bileşenleri

| Bileşen | Birim Maliyet | Açıklama |
|---------|---------------|----------|
| Düz plakalı hava kolektörü | 150-250 EUR/m2 | Malzeme + montaj |
| Transpire güneş duvarı (UTC) | 100-180 EUR/m2 | Malzeme + montaj |
| Vakumlu tüp kolektör | 250-400 EUR/m2 | Malzeme + montaj |
| Kanal/boru sistemi | 20-50 EUR/m uzunluk | Kolektör-kurutucu arası |
| Isı eşanjörü (su tipi için) | 1,000-5,000 EUR | Hava-su ısı değiştirici |
| Sirkülasyon pompası/fan (ilave) | 500-2,000 EUR | Ek fan veya pompa |
| Kontrol sistemi | 1,000-3,000 EUR | Sıcaklık kontrolü, damper, otomasyon |
| Destek yapısı (çatı/zemin) | 15-40 EUR/m2 | Çelik konstrüksiyon |
| Mühendislik ve tasarım | Toplam %8-12 | Detay tasarım, fizibilite |

### Tipik Toplam Sistem Maliyetleri

| Sistem Boyutu | Kolektör Alanı [m2] | Toplam Yatırım [EUR] | Tipik Uygulama |
|---------------|---------------------|----------------------|----------------|
| Küçük | 30-60 | 8,000-18,000 | Küçük tarımsal kurutucu, bitkisel ürünler |
| Orta | 60-150 | 18,000-45,000 | Orta ölçekli gıda/kereste kurutucu |
| Büyük (tipik 100 m2) | 100-300 | 20,000-90,000 | Büyük endüstriyel kurutucu |

**Tipik 100 m2 sistem maliyeti: 20,000-30,000 EUR** (düz plakalı hava kolektörü ile)

### Geri Ödeme Süresi (SPP) Analizi

```
SPP = Toplam Yatırım / Yıllık Tasarruf     [yıl]
```

| Senaryo | Yatırım [EUR] | Yıllık Tasarruf [EUR] | SPP [yıl] |
|---------|---------------|----------------------|-----------|
| Küçük sistem, Akdeniz, doğalgaz | 15,000 | 3,200 | 4.7 |
| Orta sistem (100 m2), Güneydoğu, doğalgaz | 25,000 | 5,500 | 4.5 |
| Orta sistem (100 m2), Ic Anadolu, LPG | 28,000 | 7,200 | 3.9 |
| Büyük sistem, Akdeniz, fuel oil | 55,000 | 12,000 | 4.6 |

**Genel geri ödeme aralığı: 3-6 yıl**

Yakıt fiyatlarının yüksek olduğu bölgelerde (kırsal, LPG/fuel oil kullanan tesisler) geri ödeme süresi 3 yılın altına inebilir. Devlet teşvikleri (KOSGEB, enerji verimliliği destekleri, yenilenebilir enerji teşvikleri) geri ödeme süresini %20-40 kısaltabilir.

### Net Bugünkü Değer (NPV) ve Iç Verim Oranı (IRR)

25 yıl kolektör ömrü ve %5 iskonto oranı ile tipik 100 m2 sistem (25,000 EUR yatırım, 4,500 EUR/yıl tasarruf):

```
NPV = -25,000 + 4,500 x [(1 - (1.05)^-25) / 0.05]
    = -25,000 + 4,500 x 14.09
    = -25,000 + 63,420
    = +38,420 EUR

IRR ~ %17 (yüksek getiri oranı)
```

## Sınırlamalar

Güneş enerjisi ile ön ısıtma çözümü her durumda uygulanabilir değildir. Aşağıdaki sınırlamalar dikkatle değerlendirilmelidir.

### Temel Sınırlamalar

| Sınırlama | Açıklama | Etkisi |
|-----------|----------|--------|
| Kesintili enerji (Intermittency) | Gündüz ve güneşli saatlerle sınırlı; gece, bulutlu ve yağışlı havada katkı yok | Konvansiyonel yedek sistem her zaman zorunlu |
| Mevsimsel değişkenlik (Seasonal variation) | Kış aylarında güneş radyasyonu yaz değerlerinin %30-50'sine düşer | Kışın solar katkı çok düşük; yıllık ortalama ile boyutlandırılmalı |
| Alan gereksinimi (Space requirement) | 50-300 m2 kolektör alanı gerekir; çatı veya zemin alanı yeterli olmalı | Sınırlı alana sahip tesislerde uygulanamayabilir |
| Yedek sistem zorunluluğu (Backup always needed) | Güneş enerjisi tek başına endüstriyel kurutma ihtiyacını karşılayamaz | Konvansiyonel ısıtıcı kaldırılamaz, yalnızca yükü azaltılır |
| Hava durumu bağımlılığı | Bulutlu günlerde kolektör verimi %70-90 düşer | Üretim planlaması güneş enerjisine bağımlı olamaz |
| Gölgeleme | Komşu binalar, ağaçlar veya ekipmanlar kolektörleri gölgeleyebilir | Gölgeleme analizi zorunlu; minimum 4 saat gölgesiz güneş gerekir |
| Toz ve kirlenme | Tozlu ortamlarda kolektör yüzey verimi hızla düşer | Düzenli temizlik programı gerekir (yılda 4-6 kez) |
| Rüzgar etkisi | UTC kolektörlerde rüzgar ısı kaybını artırır | Rüzgarlı bölgelerde cam örtülü kolektör tercih edilmeli |
| Çatı yükü | Kolektörler çatıya 15-30 kg/m2 ek yük bindirir | Yapısal değerlendirme ve gerekirse güçlendirme gerekir |

### Ne Zaman Uygulanmamalı

- Güneş radyasyonu düşük bölgelerde (<3.0 kWh/m2/gün yıllık ortalama)
- Yalnızca gece çalışan kurutucularda (güneş ile üretim örtüşmesi yok)
- Yüksek sıcaklıklı kurutma uygulamalarında (>150°C, güneş katkısı marjinal)
- Kullanılabilir çatı/zemin alanı <30 m2 olan tesislerde
- Kurutucunun kalan ömrü <5 yıl ise (geri ödeme süresi doldurulmayabilir)
- Çok ucuz yakıt kullanan tesislerde (geri ödeme süresi ekonomik olmayabilir)

## Uygun Uygulamalar

Güneş enerjisi ile hava ön ısıtma, özellikle aşağıdaki durumlarda en yüksek faydayı sağlar.

### En Uygun Sektörler ve Uygulamalar

| Uygulama | Kurutma T [°C] | Solar Uygunluk | Neden |
|----------|---------------|----------------|-------|
| Gıda kurutma (meyve, sebze, baharat) | 40-70 | Cok yüksek | Düşük T, gündüz çalışma, kırsal konum |
| Bitkisel ürün kurutma (herbs) | 35-55 | Cok yüksek | Çok düşük T, mevsimsel üretim (yaz) |
| Kereste/ahşap kurutma (wood drying) | 50-80 | Yüksek | Düşük-orta T, uzun kurutma süreleri |
| Tahıl kurutma (grain drying) | 40-65 | Yüksek | Düşük T, büyük hava debisi, tarımsal konum |
| Çamur kurutma (sludge drying) | 60-90 | Orta-Yüksek | Orta T, sürekli çalışma |
| Tekstil kurutma | 80-120 | Orta | Orta T, büyük tesislerde alan mevcut |
| Kağıt kurutma | 100-150 | Düşük | Yüksek T, solar katkı sınırlı |

### Ideal Koşullar

- **Konum:** Güneşli bölge (>4.0 kWh/m2/gün), güney cepheli çatı veya geniş zemin alanı
- **Yakıt:** Pahalı yakıt kullanan tesisler (LPG, fuel oil, elektrik) -- geri ödeme kısalır
- **Çalışma profili:** Gündüz ağırlıklı üretim (güneş saatleriyle örtüşme)
- **Sıcaklık:** Düşük-orta sıcaklık kurutma (<80°C) -- solar fraction yüksek
- **Konum tipi:** Kırsal/tarımsal (geniş alan, yüksek yakıt maliyeti)

## Uygulama Adımları

1. **Güneş radyasyonu değerlendirmesi:** Tesisin bulunduğu konumun güneş radyasyonu verilerini edinin (Meteoroloji Genel Müdürlüğü, PVGIS veritabanı veya GEPA). Yıllık ve aylık ortalama radyasyon değerlerini belirleyin.

2. **Kurutucu enerji profili analizi:** Mevcut kurutucunun saatlik/günlük enerji tüketim profilini çıkarın. Gündüz saatlerinde çalışma yoğunluğunu ve güneş saatleriyle örtüşme oranını (f_kullanim) hesaplayın.

3. **Alan değerlendirmesi:** Uygun çatı veya zemin alanını belirleyin. Yönelim (güney +-15° ideal), eğim açısı, gölgeleme durumu ve çatı taşıma kapasitesini değerlendirin.

4. **Kolektör tipi seçimi:** Kurutma sıcaklığına, bütçeye ve mevcut alana göre uygun kolektör tipini seçin (UTC: düşük maliyet/büyük alan, düz plaka: genel amaç, vakumlu tüp: yüksek T/sınırlı alan).

5. **Boyutlandırma hesabı:** Hava debisi, hedef delta T ve güneş radyasyonu verilerine göre kolektör alanını hesaplayın. Pratik kural: 0.5-1.0 m2 kolektör / 100 m3/h hava debisi.

6. **Konfigürasyon belirleme:** Doğrudan hava ısıtma, dolaylı (su döngüsü) veya hibrit sistem konfigürasyonunu belirleyin. Termal depolama gereksinimi varsa su tankı veya kaya yatağı seçeneklerini değerlendirin.

7. **Fizibilite ve ekonomik analiz:** Yıllık enerji üretimi simülasyonu, yatırım/tasarruf hesabı, SPP, NPV ve IRR değerlendirmesi yapın.

8. **Teşvik araştırması:** KOSGEB enerji verimliliği destekleri, yenilenebilir enerji teşvikleri ve vergi avantajlarını araştırın. Teşvikler geri ödeme süresini %20-40 kısaltabilir.

9. **Tedarikçi seçimi ve teklif:** Minimum 3 tedarikçiden teklif alın. Referans projelerini ve garanti koşullarını inceleyin.

10. **Detay mühendislik tasarımı:** Kolektör yerleşimi, kanal güzergahı, kontrol stratejisi, konvansiyonel yedek entegrasyonu ve by-pass sistemi tasarlayın.

11. **Kurulum ve devreye alma:** Montaj, kanal bağlantısı, kontrol sistemi kalibrasyonu. Konvansiyonel ısıtıcı ile hibrit çalışmayı test edin.

12. **Performans izleme:** Devreye alma sonrası en az 1 ay veri toplayarak gerçek solar fraction ve yakıt tasarrufunu doğrulayın. Beklenen değerlerle karşılaştırın ve gerekirse ayarlama yapın.

13. **Periyodik bakım:** Kolektör yüzey temizliği (3-6 ayda bir), bağlantı kontrolü, fan/pompa bakımı, verim izleme. Temizlik sonrası verim %5-10 artabilir.

## İlgili Dosyalar

- Kurutucu exergy formülleri: `dryer/formulas.md`
- Kurutucu benchmark verileri: `dryer/benchmarks.md`
- Egzoz havası ısı geri kazanımı: `dryer/solutions/exhaust_heat_recovery.md`
- Gıda kurutma sektörü: `dryer/sectors/food_drying.md`
- Kereste/ahşap kurutma sektörü: `dryer/sectors/wood_drying.md`
- Hava geri deviri çözümü: `dryer/solutions/air_recirculation.md`
- Fabrika çapraz ekipman optimizasyonu: `factory/cross_equipment.md`

## Referanslar

- Mujumdar, A.S., "Handbook of Industrial Drying," 4th Edition, CRC Press, 2014 — Solar Drying Chapter
- Ekechukwu, O.V., Norton, B., "Review of Solar-Energy Drying Systems: An Overview of Solar Dryer Technologies," Energy Conversion and Management, 1999
- Duffie, J.A., Beckman, W.A., "Solar Engineering of Thermal Processes," 4th Edition, Wiley, 2013
- T.C. Enerji ve Tabii Kaynaklar Bakanlığı, "Türkiye Güneş Enerjisi Potansiyel Atlası (GEPA)"
- SolarWall (Conserval Engineering), "Unglazed Transpired Collector Technical Guide"
- IEA-SHC Task 49/IV, "Solar Process Heat for Production and Advanced Applications"
- PVGIS (Photovoltaic Geographical Information System), European Commission Joint Research Centre
- Sharma, A., Chen, C.R., Vu Lan, N., "Solar-energy drying systems: A review," Renewable and Sustainable Energy Reviews, 2009
- Fudholi, A., et al., "Review of solar dryers for agricultural and marine products," Renewable and Sustainable Energy Reviews, 2010
- DOE/AMO, "Improving Process Heating System Performance: A Sourcebook for Industry"
