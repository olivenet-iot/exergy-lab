---
title: "Mevcut Eşanjör İyileştirme (Heat Exchanger Retrofit)"
category: solution
equipment_type: heat_exchanger
keywords: [retrofit, tube insert, twisted tape, helical baffle, enhanced tube, iyileştirme, upgrade]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/audit.md, heat_exchanger/solutions/fouling_management.md]
use_when: ["Mevcut eşanjör performansı düşük olduğunda", "Eşanjör değişimi yerine iyileştirme değerlendirilirken", "Retrofit vs yenileme kararı verilirken"]
priority: medium
last_updated: 2026-02-01
---
# Mevcut Eşanjör İyileştirme (Heat Exchanger Retrofit)

> Son güncelleme: 2026-02-01

## Özet

**Problem:** Mevcut ısı eşanjörlerinin performansı zamanla düşer veya artan kapasite talepleri karşılanamaz hale gelir. Eşanjörü tamamen değiştirmek yüksek maliyet ve uzun duraklatma süresi gerektirir. Birçoğu durumda mevcut eşanjör gövdesi ve altyapısı korunarak iç yapıda iyileştirmeler yapmak daha ekonomiktir.

**Çözüm:** Boru içi eklentiler (tube inserts), plaka paketi ilavesi, baffle değişimi, geliştirilmiş yüzey borular ve paralel eşanjör ilavesi gibi retrofit yöntemleri ile mevcut ekipmanın performansını artırmak.

**Tipik Tasarruf:** %15-50 (ısı transfer kapasitesinde artış veya enerji tüketiminde azalma)
**Tipik ROI:** 0.5-3 yıl

## Boru İçi Eklenti Teknolojileri (Tube Insert Technologies)

### 1. Türklü Bant (Twisted Tape Insert)

Metal şerit boru ekseni boyunca burularak yerleştirilir; akışa döner hareket kazandırır:

```
Tasarım parametreleri:
  y = H / d_i  (twist ratio, burukluk oranı)

  H = 360 derece dönüş mesafesi [m]
  d_i = Boru iç çapı [m]

Tipik y aralığı: 3-6
  y = 3: Agresif karıştırma, yüksek h artışı, yüksek DP artışı
  y = 6: Yumuşak karıştırma, orta h artışı, düşük DP artışı
```

| Twist Oranı (y) | h Artışı (%) | DP Artışı (%) | PEC | Uygulama |
|------------------|-------------|---------------|-----|----------|
| 3.0 | +80-120 | +200-400 | 0.8-1.0 | Viskoz akışkanlar |
| 4.0 | +50-80 | +100-250 | 0.9-1.1 | Genel amaçlı |
| 5.0 | +30-50 | +60-150 | 1.0-1.2 | Standart |
| 6.0 | +20-35 | +40-80 | 1.0-1.3 | DP hassas uygulamalar |

**Maliyet:** €5-15/boru (malzeme + yerleştirme)
**Avantajlar:** Düşük maliyet, kolay montaj/demontaj, farklı burukluk oranları
**Dezavantajlar:** DP artışı yüksek olabilir, temizlik zorluğu (çıkarılabilir tip tercih)

### 2. Tel Sargı (Wire Coil Insert)

Boru iç yüzeyine yakın sarmal tel; sınır tabakasını bozarak türbülans oluşturur:

```
Tasarım parametreleri:
  e / d_i = Tel çap oranı (tipik 0.02-0.05)
  p / d_i = Adım oranı (tipik 0.5-2.0)

  e = Tel çapı [m]
  p = Sargı adımı [m]
  d_i = Boru iç çapı [m]
```

| e/d_i | p/d_i | h Artışı (%) | DP Artışı (%) | PEC |
|-------|-------|-------------|---------------|-----|
| 0.02 | 1.0 | +25-35 | +40-70 | 1.1-1.3 |
| 0.03 | 1.0 | +35-50 | +60-120 | 1.0-1.2 |
| 0.05 | 0.5 | +50-80 | +100-250 | 0.9-1.1 |
| 0.03 | 1.5 | +20-30 | +30-50 | 1.1-1.4 |

**Maliyet:** €3-10/boru
**Avantajlar:** Düşük maliyet, uniform türbülans, kolay üretim
**Dezavantajlar:** Çıkarılması zor (kalıcı), kirlenmeye karşı hassas

### 3. Hi-Tran Elemanları (Hi-Tran Matrix Elements)

Tel örgü matris şeklinde boru içine yerleştirilen ticari ürün (Cal Gavin Ltd):

```
Özellikler:
  - Tel yoğunluğu: %5-25 boş hacim doluluğu
  - Uzunluk: Boru uzunluğuna göre kesilir
  - Malzeme: Paslanmaz çelik tel
  - Montaj: Borunun bir ucundan itilerek yerleştirilir
```

| Doluluk (%) | h Artışı (%) | DP Artışı (%) | Öneri |
|-------------|-------------|---------------|-------|
| 5 | +30-50 | +50-100 | Standart |
| 10 | +50-80 | +100-200 | Viskoz akışkanlar |
| 15 | +80-120 | +200-350 | Çok viskoz, laminar |
| 25 | +120-200 | +350-600 | Özel uygulamalar |

**Maliyet:** €15-30/boru
**Avantajlar:** Laminar akışta bile etkili (Re < 2,300), boru yüzeyine temas etmez (korozyon yok)
**Dezavantajlar:** Yüksek DP artışı, temizlik için çıkarılmalı

### 4. Boru İçi Kanatçıklı Borular (Micro-Fin / Internally Enhanced Tubes)

Boru iç yüzeyine işlenmiş ince spiral kanatçıklar:

```
Parametreler:
  e = Kanatçık yüksekliği (tipik 0.2-0.4 mm)
  N_fin = Kanatçık sayısı (tipik 50-70)
  beta = Helis açısı (tipik 15-30 derece)
```

| Tip | h Artışı (%) | DP Artışı (%) | PEC | Maliyet Artışı |
|-----|-------------|---------------|-----|----------------|
| Standart micro-fin | +50-100 | +30-80 | 1.3-1.6 | %20-40 |
| Yüksek kanatçık | +80-150 | +60-150 | 1.2-1.5 | %30-50 |
| Çift spiral | +100-200 | +80-200 | 1.1-1.4 | %40-60 |

**Not:** Micro-fin borular yeni boru değişimi sırasında tercih edilir; mevcut borulara retrofit uygulanamaz.

## Plaka Paketi İlavesi (Plate Pack Addition)

### Plakalı Eşanjörler İçin

Mevcut plakalı eşanjöre ek plaka ilavesi ile kapasite artışı:

```
Kapasite artışı hesabı:
  Q_yeni = Q_eski x (N_plaka_yeni / N_plaka_eski)

  Ancak: Port boyutu ve çerçeve kapasitesi sınırlayıcı olabilir
```

| Mevcut Plaka Sayısı | Ek Plaka Sayısı | Kapasite Artışı (%) | Yaklaşık Maliyet |
|---------------------|-----------------|---------------------|-----------------|
| 50 | +10 | +20 | €3,000-5,000 |
| 50 | +20 | +40 | €5,000-9,000 |
| 100 | +20 | +20 | €5,000-9,000 |
| 100 | +50 | +50 | €12,000-20,000 |

**Avantajlar:** Düşük maliyet, hızlı uygulama (1-2 gün), çerçeve içinde alan yeterliyse kolay
**Dezavantajlar:** Çerçeve basıncı sınırı, port hızı artışı (DP artışı), mevcut plaka tipi bulunabilirlik

### Plaka Tipi Değişimi

Mevcut plakaların daha yüksek performanslı plakalarla değiştirilmesi:

| Plaka Tipi | h Değişimi | DP Değişimi | Kullanım |
|------------|-----------|-------------|----------|
| Düşük theta -> Yüksek theta | +20-40% | +30-60% | Kapasite artışı gerekli |
| Yüksek theta -> Düşük theta | -20-35% | -30-50% | DP azaltma gerekli |
| Karışık (yüksek/düşük) | Optimize | Optimize | h/DP dengesi |

## Re-Baffling: Baffle Değişimi

### Segmental -> Helisel Baffle Dönüşümü

Mevcut gövde-boru eşanjörün segmental baffle'larının helisel baffle ile değiştirilmesi:

```
Tipik iyileşme:
  - Gövde tarafı DP: %40-70 azalma
  - Gövde tarafı h: %5-20 azalma (veya değişim yok)
  - h/DP oranı: %50-150 iyileşme
  - Titreşim riski: Önemli ölçüde azalır
  - Ölü bölge (dead zone): Elimine edilir
```

| Parametre | Segmental | Helisel | Değişim |
|-----------|-----------|---------|---------|
| DP_shell (kPa) | 80 | 30 | -%62 |
| h_shell W/(m2-K) | 2,500 | 2,300 | -%8 |
| h/DP oranı | 31.3 | 76.7 | +%145 |
| Titreşim | Risk var | Düşük risk | İyileşme |

**Yatırım maliyeti:** €10,000-30,000 (eşanjör boyutuna bağlı)
**Uygulama süresi:** 3-5 gün (gövde açma + baffle montaj + test)

### Segmental -> No-Tubes-in-Window (NTIW)

Pencere bölgesindeki boruların kaldırılması ile titreşim sorunu çözülür:

```
NTIW avantajları:
  - Boru titreşimi tamamen elimine edilir
  - Gövde tarafı akış daha homojen
  - Uzun vadeli güvenilirlik artar

Dezavantajları:
  - Transfer alanı %15-25 azalır (boru sayısı azalır)
  - Gövde çapı artırmak gerekebilir
```

## Boru Değişimi (Tube Replacement)

### Düz Boru -> Geliştirilmiş Yüzey Boru

Mevcut düz boruların geliştirilmiş yüzey borularla değiştirilmesi:

| Boru Tipi | Dış Yüzey Artışı | h_dış Artışı (%) | Maliyet Artışı | Uygulama |
|-----------|-----------------|-------------------|----------------|----------|
| Düz boru (referans) | 1.0x | Referans | 1.0x | Standart |
| Alçak kanatçıklı (low-fin) | 2.5-4.0x | +50-100 | 1.3-1.8x | Gaz-sıvı |
| Yüksek kanatçıklı (high-fin) | 5-20x | +100-300 | 1.5-2.5x | Gaz soğutma |
| Corrugated (oluklu) | 1.0x (dış) | +20-40 (iç) | 1.2-1.5x | Sıvı-sıvı |
| Dimpled (girinti-çıkıntılı) | 1.0x | +15-30 (iç+dış) | 1.1-1.3x | Genel |
| Twisted / ovalized | 1.0x | +20-40 | 1.2-1.4x | Gövde tarafı iyileştirme |

### Boru Değişimi Zamanlama

Boru değişimi şu durumlarda değerlendirilmelidir:
- Boru duvar kalınlığı minimum değerin altına düştüğünde (UT inspeksiyon ile)
- Sık boru tıkaç (tube plug) gerekliliği (%10'dan fazla tıkaçlı boru)
- Kapasite artışı gereksinimi
- Malzeme değişikliği gerekliliği (korozyon nedeniyle)

## Gövde Tarafı İyileştirme (Shell Side Enhancement)

### Rod Baffle (Çubuk Baffle)

Segmental baffle yerine çubuk demetleri ile boru destekleme:

```
Rod baffle avantajları:
  - DP %60-80 azalma
  - Titreşim riski tamamen elimine
  - Kirlenme önemli ölçüde azalır (ölü bölge yok)

Rod baffle dezavantajları:
  - h_shell %20-40 azalma
  - Özel tasarım ve üretim gerekli
```

### Gövde Tarafı Dolgu (Packing / Turbulators)

Boru demeti dışına yerleştirilen türbülansı artırıcı elemanlar:

- Gövde tarafı boru dış yüzeyine eklenen spiral tel veya pim
- h_shell %20-50 artış, DP %30-80 artış
- Özel uygulamalarda faydalı olabilir, ancak temizlik zorluğu

## Paralel Eşanjör İlavesi

### Ne Zaman Tercih Edilir

```
Paralel eşanjör ilavesi:
  1. Mevcut eşanjör kapasitesi yetersiz ve retrofit yeterli değil
  2. Basınç düşüşü kritik ve azaltılması gerekli
  3. Redundancy (yedekleme) gereksinimi var
  4. Mevcut eşanjör gövdesi bozulmamış, sadece ek alan gerekli
```

### Paralel vs Seri Düzenleme

| Düzenleme | DP Etkisi | Kapasite Etkisi | Kullanım |
|-----------|-----------|-----------------|----------|
| Paralel | DP %75 azalır (2x) | Toplam kapasite 2x | DP kritik |
| Seri | DP 2x artar | DT_approach azalır, Q artar | Sıcaklık yaklaşımı kritik |
| Paralel-seri karma | Optimize | Optimize | Karmaşık sistemler |

### Örnek: Paralel Eşanjör İlavesi

Mevcut: 1 adet 100 m2 gövde-boru, U=800 W/(m2-K), Q=400 kW, DP=90 kPa

Ek eşanjör: Aynı tip, 100 m2, paralel bağlantı

```
Paralel düzenleme:
  DP_yeni = 90 / 4 = 22.5 kPa
  U korunur (aynı akışkan koşulları)
  Toplam alan = 200 m2
  DT_approach azalır -> Q artar (daha fazla ısı geri kazanım)
```

## Performans Testi: Önce ve Sonra

### Test Prosedürü

1. **Retrofit öncesi:** En az 1 hafta sürekli veri toplama
   - 4 sıcaklık noktası (her iki taraf giriş/çıkış)
   - 2 debi ölçümü (her iki taraf)
   - 2 basınç düşüşü ölçümü
   - Hesaplanan: Q, LMTD, U, CF

2. **Retrofit sonrası:** Aynı koşullarda en az 1 hafta veri toplama
   - Aynı parametreler
   - Karşılaştırma: DU/U, DDP/DP, DQ/Q

### Performans Karşılaştırma Tablosu

| Parametre | Retrofit Öncesi | Retrofit Sonrası | Değişim |
|-----------|-----------------|------------------|---------|
| U W/(m2-K) | 650 | 950 | +%46 |
| DP_tube (kPa) | 45 | 65 | +%44 |
| DP_shell (kPa) | 90 | 35 | -%61 |
| Q (kW) | 400 | 520 | +%30 |
| DT_approach (C) | 25 | 15 | -%40 |
| eta_ex (%) | 48 | 62 | +%14 mutlak |

## ROI Hesapları: Retrofit Seçenekleri Karşılaştırma

### Senaryo: 200 m2 Gövde-Boru Eşanjör, Proses Soğutma

| Retrofit Seçeneği | Yatırım (EUR) | h Artışı (%) | DP Etkisi | Yıllık Tasarruf (EUR) | SPP (yıl) |
|-------------------|---------------|-------------|-----------|----------------------|-----------|
| Twisted tape insert | 4,000 | +50 | +150% DP | 18,000 | 0.22 |
| Wire coil insert | 2,500 | +35 | +80% DP | 12,000 | 0.21 |
| Hi-Tran elements | 8,000 | +80 | +200% DP | 25,000 | 0.32 |
| Helisel baffle | 22,000 | -10 (h) / -60 (DP) | -%60 DP | 8,000 | 2.75 |
| Boru değişimi (enhanced) | 35,000 | +60 | +40% DP | 22,000 | 1.59 |
| Plaka ek (50 plaka) | 12,000 | +40 (alan) | +20% DP | 15,000 | 0.80 |
| Paralel ek eşanjör | 45,000 | Alan 2x | -%75 DP | 12,000 | 3.75 |
| Komple eşanjör değişimi | 80,000 | Sıfırdan tasarım | Optimize | 30,000 | 2.67 |

### ROI Formülü

```
ROI = (Yıllık_tasarruf - Yıllık_bakım) / Yatırım x 100 [%]

SPP = Yatırım / (Yıllık_tasarruf - Yıllık_bakım) [yıl]
```

## Karar Çerçevesi: Retrofit vs Değiştirme

```
Eşanjör performans düşüşü tespit edildi
  |
  +-- Gövde ve boru demeti sağlamlık kontrolü
  |     |-- Gövde bozuk (korozyon, çatlak) -> DEĞİŞTİRME
  |     |-- Gövde sağlam -> Devam
  |
  +-- Performans düşüşü nedeni?
  |     |-- Kirlenme -> Temizlik + izleme (FOULING MANAGEMENT)
  |     |-- Yetersiz kapasite -> Devam
  |     |-- Malzeme uyumsuzluğu -> MALZEME DEĞİŞİMİ veya DEĞİŞTİRME
  |
  +-- Retrofit yeterli olur mu?
  |     |-- h artışı <%30 yeterli -> TUBE INSERT (düşük maliyet)
  |     |-- h artışı %30-60 yeterli -> ENHANCED TUBE veya PLAKA EK
  |     |-- DP azaltma gerekli -> HELİSEL BAFFLE veya PARALEL
  |     |-- Kapasite >2x gerekli -> DEĞİŞTİRME veya PARALEL
  |
  +-- Maliyet karşılaştırması
        |-- Retrofit maliyeti < %40 x değiştirme maliyeti -> RETROFIT
        |-- Retrofit maliyeti > %60 x değiştirme maliyeti -> DEĞİŞTİRME
        |-- Arasında -> SPP karşılaştırması yap
```

## Uygulama Adımları

1. **Performans ölçümü:** Mevcut eşanjörün detaylı performans testi yap
2. **Gövde/boru inspeksiyonu:** UT, eddy current veya görsel muayene ile yapısal durumu değerlendir
3. **Root-cause analizi:** Performans düşüşünün nedenini belirle (kirlenme, kapasite, malzeme)
4. **Retrofit seçenekleri değerlendirmesi:** Uygun retrofit yöntemlerini listele
5. **Termal-hidrolik simülasyon:** Her seçenek için h, DP, Q, eta_ex hesapla
6. **Ekonomik analiz:** Her seçenek için yatırım, tasarruf, SPP hesapla
7. **Karar:** Retrofit vs değiştirme kararı ver
8. **Tasarım ve tedarik:** Seçilen retrofit komponentlerini tasarla ve temin et
9. **Uygulama:** Eşanjörü durdur, retrofit uygula (1-5 gün)
10. **Performans doğrulama:** Retrofit sonrası performans testi ile iyileşmeyi doğrula
11. **İzleme:** Sürekli performans izleme programına al

## İlgili Dosyalar

- Isı eşanjörü exergy formülleri: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Kirlenme yönetimi: `heat_exchanger/solutions/fouling_management.md`
- Basınç düşüşü azaltma: `heat_exchanger/solutions/pressure_drop.md`
- Yaklaşım sıcaklığı optimizasyonu: `heat_exchanger/solutions/approach_temp.md`
- Malzeme seçimi: `heat_exchanger/solutions/material_selection.md`
- Gövde-boru eşanjör: `heat_exchanger/equipment/shell_and_tube.md`
- Plakalı eşanjör: `heat_exchanger/equipment/plate.md`

## Referanslar

- Manglik, R.M. and Bergles, A.E., "Heat Transfer and Pressure Drop Correlations for Twisted-Tape Inserts in Isothermal Tubes," J. Heat Transfer, 1993
- Cal Gavin Ltd., "Hi-Tran Turbulator Technology — Engineering Data and Application Guide"
- Koch Heat Transfer Company, "Twisted Tube Heat Exchanger Technology"
- Lummus Technology, "Helixchanger Heat Exchangers — Technical Bulletin"
- TEMA, "Standards of the Tubular Exchanger Manufacturers Association," 10th Edition
- Mukherjee, R., "Effectively Design Shell-and-Tube Heat Exchangers," Chemical Engineering Progress, 1998
- Webb, R.L. and Kim, N.-H., "Principles of Enhanced Heat Transfer," 2nd Edition, Taylor & Francis, 2005
- Bergles, A.E., "ExHFT for Fourth Generation Heat Transfer Technology," Experimental Thermal and Fluid Science, 2002
- Shah, R.K. and Sekulic, D.P., "Fundamentals of Heat Exchanger Design," Wiley, 2003
- Alfa Laval, "Plate Heat Exchanger Upgrade and Optimization Guide"
