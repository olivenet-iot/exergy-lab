---
title: "Soğutma Kulesi — Cooling Tower"
category: equipment
equipment_type: chiller
subtype: "Soğutma Kulesi"
keywords: [soğutma kulesi, kule, su, yaklaşım]
related_files: [chiller/equipment/water_cooled.md, chiller/solutions/condenser_optimization.md, chiller/benchmarks.md]
use_when: ["Soğutma kulesi analizi yapılırken", "Kule performansı değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Soğutma Kulesi — Cooling Tower

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Evaporatif soğutma cihazı — suyun kısmi buharlaşması yoluyla ısı atımı sağlar
- Kapasite aralığı: 10 kW - 100+ MW ısı atım kapasitesi
- Uygulama: Chiller kondenser suyu soğutma, endüstriyel proses soğutma, enerji santralleri, veri merkezleri
- Referans çevre koşulları: T₀ = 25°C (298.15 K), P₀ = 1 atm (101.325 kPa)
- Yaygın markalar: BAC (Baltimore Aircoil), Evapco, SPX Cooling Technologies (Marley), MITA, Carrier (HAM), Liang Chi
- Enerji tüketimi: Toplam soğutma sistemi enerjisinin %5-15'i (fan + pompa)
- Su tüketimi: Soğutulan her 1 kW ısı için yaklaşık 1.5-2.5 L/saat su buharlaşır
- Kritik konu: Legionella riski — düzenli bakım ve su arıtma zorunludur

## Çalışma Prensibi

Soğutma kuleleri, sıcak suyun hava ile doğrudan veya dolaylı temas ettirilmesi yoluyla çalışır. Soğutmanın büyük bölümü (~%80) suyun kısmi buharlaşması (evaporatif soğutma), geri kalanı (~%20) konvektif ısı transferi ile gerçekleşir.

### Temel Termodinamik

```
Q_kule = m_su × cp × (T_giriş - T_çıkış) = m_su × cp × Range

Burada:
  Q_kule   : Soğutma kulesinin ısı atım kapasitesi (kW)
  m_su     : Su debisi (kg/s)
  cp       : Suyun özgül ısısı (~4.18 kJ/kg·K)
  T_giriş  : Kuleye giren sıcak su sıcaklığı (°C)
  T_çıkış  : Kuleden çıkan soğuk su sıcaklığı (°C)
  Range    : Sıcaklık farkı = T_giriş - T_çıkış (°C veya K)
```

### Yaş Termometre Sıcaklığı ve Yaklaşma Kavramı

Soğutma kulesinin teorik sınırı, ortam havasının yaş termometre (wet bulb) sıcaklığıdır. Su asla bu sıcaklığın altına soğutulamaz.

```
Yaklaşma (Approach) = T_çıkış - T_wb

Burada:
  T_çıkış  : Kuleden çıkan soğuk su sıcaklığı (°C)
  T_wb     : Ortam havasının yaş termometre sıcaklığı (°C)
  Approach : Yaklaşma değeri (°C veya K) — düşük olması istenir

Toplam sıcaklık farkı:
  Range + Approach = T_giriş - T_wb
```

| Yaklaşma Değeri (°C) | Performans Sınıfı | Kule Boyutu |
|-----------------------|-------------------|-------------|
| 2-3 | Mükemmel | Çok büyük / çift hücreli |
| 3-5 | İyi | Standart tasarım |
| 5-8 | Ortalama | Ekonomik tasarım |
| 8-12 | Düşük | Küçük / eski kule |
| >12 | Yetersiz | Kirli dolgu, arızalı fan |

### Türkiye İçin Tipik Yaş Termometre Sıcaklıkları

| Şehir | Tasarım Yaş Termometre (°C) — %1 aşım | Kuru Termometre (°C) |
|-------|----------------------------------------|----------------------|
| İstanbul | 24.2 | 33.4 |
| Ankara | 20.8 | 34.6 |
| İzmir | 24.8 | 37.2 |
| Antalya | 26.4 | 37.8 |
| Adana | 27.1 | 38.4 |
| Bursa | 23.5 | 34.8 |
| Trabzon | 23.8 | 30.2 |

## Soğutma Kulesi Tipleri

### Açık Devre (Open Circuit)
- Soğutulacak su doğrudan hava ile temas eder
- En yaygın tip — chiller kondenser suyu soğutmada standart
- Avantaj: Düşük maliyet, yüksek verim, basit yapı
- Dezavantaj: Su kirlenmesi (havadan toz, biyolojik kirlilik), su arıtma gereksinimi, buharlaşma kaybı
- Uygulama: HVAC chiller sistemleri, endüstriyel soğutma

### Kapalı Devre (Closed Circuit / Fluid Cooler)
- Soğutulacak sıvı kapalı borularda (serpantin) dolaşır — hava ve dış su ile dolaylı temas
- Avantaj: Proses sıvısı kirlenmez, glikollü sistemler için uygun, düşük su arıtma gereksinimi
- Dezavantaj: Daha düşük verim (ek ısı transfer direnci), daha yüksek maliyet
- Uygulama: Hassas endüstriyel prosesler, veri merkezleri, glikollü sistemler

### Kuru Soğutucu (Dry Cooler)
- Su buharlaşması yok — yalnızca konvektif ısı transferi ile çalışır
- Avantaj: Su tüketimi sıfır, bakım minimum, Legionella riski yok
- Dezavantaj: Performans kuru termometre sıcaklığına bağlı (yaş termometre avantajı yok), büyük boyut
- Uygulama: Düşük ısı yükü, su kısıtlı bölgeler, kışın serbest soğutma (free cooling)

### Çapraz Akışlı (Crossflow) vs Karşı Akışlı (Counterflow)

| Özellik | Çapraz Akışlı | Karşı Akışlı |
|---------|---------------|--------------|
| Hava/su akışı | Yatay hava / dikey su | Dikey hava (yukarı) / dikey su (aşağı) |
| Dolgu yüksekliği | Düşük | Yüksek |
| Kule yüksekliği | Düşük (geniş taban) | Yüksek (dar taban) |
| Taze hava emiş mesafesi | Geniş | Dar |
| Enerji tüketimi (fan) | Düşük (düşük basınç kaybı) | Orta-yüksek |
| Isı transfer verimliliği | Orta | Yüksek (daha iyi yaklaşma) |
| Bakım kolaylığı | Kolay (yan panel erişimi) | Zor (üstten erişim) |
| Donma riski | Düşük | Orta (su dağıtım tabağı donar) |
| Yaygın uygulama | Büyük HVAC, endüstriyel | Orta/büyük HVAC |

## Dolgu (Fill) Tipleri

### Film Tipi Dolgu (Film Fill)
- Yapı: İnce PVC veya PP levhalar — su ince film halinde akar
- Isı transfer yüzeyi: Çok yüksek (m²/m³)
- Verim: Yüksek — küçük boyutta büyük kapasite
- Hassasiyet: Temiz suya ihtiyaç duyar — kirli/sert su ile tıkanma riski
- Uygulama: HVAC sistemleri, temiz su prosesleri

### Serpme Tipi Dolgu (Splash Fill)
- Yapı: Yatay çubuklar veya kafes yapılar — su damla halinde düşer
- Isı transfer yüzeyi: Düşük
- Verim: Düşük — daha büyük kule gerektirir
- Avantaj: Kirli ve sert suya dayanıklı, tıkanma riski düşük
- Uygulama: Endüstriyel proses suyu (kirli), ağır sanayi

## Enerji Dağılımı

Soğutma kulesi enerji tüketimi:

| Bileşen | Güç Payı (%) | Açıklama |
|---------|-------------|----------|
| Fan motoru | 70-85 | Ana enerji tüketici — hava debisini sağlar |
| Kondenser suyu pompası | 15-30 | Chiller-kule arası su sirkülasyonu |
| Su arıtma dozaj pompası | <1 | Kimyasal dozajlama |
| Toplam | 100 | Tipik: soğutma kapasitesinin %3-8'i |

### Fan Tipleri ve VSD Uygulaması

| Fan Tipi | Çap Aralığı | Güç Aralığı | Verim | VSD Uyumluluğu |
|----------|-------------|-------------|-------|----------------|
| Eksenel (aksiyel) | 1-12 m | 1-200 kW | Yüksek | Mükemmel — kübik güç tasarrufu |
| Santrifüj (radyal) | 0.5-3 m | 2-100 kW | Orta | İyi |

Fan affinite yasaları — VSD tasarruf potansiyeli:

```
Q_hava ∝ N
ΔP ∝ N²
P_fan ∝ N³

Burada:
  Q_hava : Hava debisi (m³/s)
  ΔP     : Basınç farkı (Pa)
  P_fan  : Fan güç tüketimi (kW)
  N      : Fan devri (RPM veya %)

Örnek: Fan devri %80'e düşürüldüğünde:
  Hava debisi = %80
  Güç tüketimi = 0.80³ = %51.2
  Tasarruf = %48.8
```

VSD ile soğutma kulesi fan kontrolü, özellikle kısmi yüklerde büyük tasarruf sağlar. Sabit devirli fanlarda on-off veya iki devirli kontrol kullanılır, ancak VSD kadar verimli değildir.

## Ekserji Analizi

### Soğutma Kulesinin Ekserji Akışları

Soğutma kulesi, yüksek sıcaklıklı suyu düşük sıcaklıklı suya dönüştürür. Çevreye yakın sıcaklıklarda çalıştığı için ekserji içeriği düşüktür.

```
Ekserji dengesi:
  Ex_giriş_su + Ex_fan + Ex_pompa = Ex_çıkış_su + Ex_buhar + Ex_yıkım

Ex_su = m_su × cp × [(T_su - T₀) - T₀ × ln(T_su / T₀)]

Burada:
  Ex_giriş_su  : Sıcak suyun ekserji akışı (kW)
  Ex_çıkış_su  : Soğuk suyun ekserji akışı (kW)
  Ex_fan       : Fan elektrik gücü = saf ekserji (kW)
  Ex_pompa     : Pompa elektrik gücü = saf ekserji (kW)
  Ex_buhar     : Buharlaşan suyun ekserji akışı (kW) — genellikle ihmal edilir
  Ex_yıkım     : Tersinmezlik kaynaklı ekserji yıkımı (kW)
  T_su         : Su sıcaklığı (K)
  T₀           : Referans çevre sıcaklığı (K) = 298.15 K
```

### Tipik Ekserji Değerleri

| Su Sıcaklığı (°C) | Özgül Ekserji (kJ/kg) | Not |
|--------------------|----------------------|-----|
| 30 (kule çıkış) | 0.42 | Çevreye çok yakın — düşük ekserji |
| 35 (kule giriş) | 1.67 | Tipik kondenser çıkışı |
| 37 (kule giriş) | 2.39 | Yüksek yük durumu |
| 40 (kule giriş) | 3.74 | Çok yüksek yük |

Soğutma kulesi ekserji verimi genellikle %5-20 aralığındadır. Bu düşük değer, suyun çevre sıcaklığına yakın olmasından kaynaklanır — enerji içeriği yüksek olsa da ekserji (iş yapma kapasitesi) düşüktür.

### Sistem Düzeyinde Ekserji Etkisi

Soğutma kulesinin asıl ekserji etkisi, kondenser su sıcaklığını düşürerek chiller COP'unu artırmasıdır:

```
Kondenser su sıcaklığının chiller COP'una etkisi:
  Her 1°C kondenser suyu sıcaklık düşüşü ≈ %1.5-2.5 COP artışı

Örnek (500 kW chiller, 2500 saat/yıl, 0.10 EUR/kWh):
  Kule yaklaşma: 5°C → 3°C iyileştirme (2°C düşüş)
  COP artışı: ~%4 (COP 5.0 → 5.2)
  Güç tasarrufu: 500/5.0 - 500/5.2 = 100 - 96.2 = 3.8 kW
  Yıllık tasarruf: 3.8 × 2,500 × 0.10 = 950 EUR/yıl
```

## Su Arıtma ve Blowdown

### Su Kalitesi Gereksinimleri

| Parametre | Önerilen Aralık | Birim | Risk (aşıldığında) |
|-----------|-----------------|-------|---------------------|
| pH | 7.0-9.0 | — | Korozyon (<7) veya kireç (<9) |
| Toplam sertlik (CaCO₃) | 200-500 | ppm | Kireçlenme |
| İletkenlik | 500-3,000 | µS/cm | Korozyon, kireç |
| Toplam çözünmüş katı (TDS) | 500-2,500 | ppm | Kireç, tıkanma |
| Klorür | <250 | ppm | Paslanmaz çelik korozyonu |
| Sülfat | <250 | ppm | Beton korozyonu |
| Silika | <150 | ppm | Silika kireçlenmesi |
| Toplam bakteri sayısı | <10,000 | CFU/mL | Biyofilm, Legionella |

### Konsantrasyon Döngüsü ve Blowdown

```
CoC = Makeup / Blowdown = TDS_kule / TDS_şebeke

Burada:
  CoC        : Konsantrasyon döngüsü sayısı (tipik 3-6)
  Makeup     : Taze su ilave debisi (L/s)
  Blowdown   : Blowdown (deşarj) debisi (L/s)
  TDS_kule   : Kule suyu toplam çözünmüş katı (ppm)
  TDS_şebeke : Şebeke suyu toplam çözünmüş katı (ppm)

Su dengesi:
  Makeup = Buharlaşma + Blowdown + Sürükleme (drift)
  Buharlaşma ≈ m_su × cp × Range / h_fg ≈ 0.00085 × m_su × Range
  Sürükleme ≈ %0.001-0.005 × m_su (yeni eliminator ile)
  Blowdown = Buharlaşma / (CoC - 1)

Burada:
  h_fg       : Suyun buharlaşma entalpisi (~2,430 kJ/kg @ 30°C)
  Range      : Kule sıcaklık farkı (°C)
  Sürükleme  : Hava akışıyla taşınan su damlacıkları (L/s)
```

### Kimyasal Arıtma Programı

| Kimyasal | Amaç | Tipik Doz | Uygulama |
|----------|------|-----------|----------|
| Kireç önleyici (antiscalant) | Kalsiyum karbonat çökelmesini önleme | 20-50 ppm | Sürekli dozaj |
| Korozyon inhibitörü | Metal yüzey koruması | 50-100 ppm | Sürekli dozaj |
| Biyosit (oksidatif) | Bakteri kontrolü, Legionella önleme | 0.5-2 ppm serbest klor | Sürekli veya şok dozaj |
| Biyosit (non-oksidatif) | Biyofilm kontrolü | Ürüne bağlı | Haftalık şok dozaj |
| pH ayarlayıcı (H₂SO₄) | pH kontrolü | pH 7.0-8.5 hedef | Otomatik dozaj |
| Dispersant | Askıda katı dispersiyonu | 10-30 ppm | Sürekli dozaj |

## Legionella Önleme

Legionella pneumophila, soğutma kulesi suyunda üreyebilen ve solunum yoluyla ciddi sağlık riski oluşturan bir bakteridir. Soğutma kuleleri, aerosol oluşturması nedeniyle en yüksek riskli kaynaklardır.

### Risk Faktörleri
- Su sıcaklığı 20-45°C arasında (en yüksek üreme: 35-40°C)
- Durgun su bölgeleri (ölü bacaklar, kullanılmayan hatlar)
- Biyofilm oluşumu (koruyucu tabaka — biyositlere direnç)
- Yetersiz dezenfeksiyon
- Kirli/bakımsız kule

### Önleme Tedbirleri
1. **Serbest klor:** 0.5-2.0 ppm sürekli — en yaygın ve ekonomik yöntem
2. **Klor dioksit (ClO₂):** 0.1-0.5 ppm — biyofilm penetrasyonu daha iyi
3. **Sıcaklık yönetimi:** Kule suyu sıcaklığını mümkünse 20°C altında tutma (kış döneminde)
4. **Damla tutucu (drift eliminator):** Aerosol emisyonunu <%0.005 oranına düşürme
5. **Düzenli temizlik:** Yılda en az 2 kez mekanik temizlik ve dezenfeksiyon
6. **İzleme:** Aylık Legionella testi (kültür yöntemi, sonuç 7-14 gün)
7. **Risk değerlendirmesi:** Yıllık yazılı risk değerlendirmesi (Türkiye: Biyosidal Ürünler Yönetmeliği kapsamında)

| Legionella Seviyesi (CFU/L) | Risk | Gerekli Aksiyon |
|-----------------------------|------|-----------------|
| <100 | Düşük | Rutin bakıma devam |
| 100-1,000 | Orta | Su arıtma programını gözden geçir |
| 1,000-10,000 | Yüksek | Acil dezenfeksiyon, kaynak araştırması |
| >10,000 | Çok yüksek | Kuleyi durdur, hiperoklorlama, yetkililere bildir |

## Ölçülmesi Gereken Parametreler

### Zorunlu
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Kuleye giren su sıcaklığı | °C | 32-42 | PT100 sensör |
| Kuleden çıkan su sıcaklığı | °C | 26-34 | PT100 sensör |
| Yaş termometre sıcaklığı | °C | 18-28 | Psikrometre veya nemli termometre |
| Su debisi | m³/h | Sisteme bağlı | Ultrasonik debimetre |
| Fan elektrik gücü | kW | 1-200 | Güç analizörü |
| Kondenser suyu pompa gücü | kW | 1-100 | Güç analizörü |
| Dış hava sıcaklığı (kuru) | °C | 15-42 | Termometre |
| Bağıl nem | % | 30-90 | Higrometre |

### Opsiyonel (detaylı analiz için)
| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Makeup su debisi | m³/h | Sisteme bağlı | Su sayacı |
| Blowdown debisi | m³/h | Sisteme bağlı | Su sayacı veya vana |
| İletkenlik (kule suyu) | µS/cm | 500-3,000 | İletkenlik ölçer |
| pH | — | 7.0-9.0 | pH metre |
| Serbest klor | ppm | 0.5-2.0 | Kolorimetrik test |
| Fan devri | RPM | 100-1,000 | Takometre / VSD okuma |
| Ses seviyesi | dB(A) | 55-85 | Ses ölçer |

### Nameplate Bilgileri
- Marka ve model
- Nominal ısı atım kapasitesi (kW)
- Nominal su debisi (m³/h veya L/s)
- Tasarım yaş termometre sıcaklığı (°C)
- Tasarım Range/Approach (°C)
- Fan motor gücü (kW)
- Fan tipi (aksiyel/santrifüj) ve çapı
- Dolgu tipi (film/splash)
- Hücre sayısı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Kule tipi | Açık devre, karşı akışlı | HVAC'de en yaygın |
| Dolgu tipi | Film tipi | Temiz su uygulamaları |
| Kuleye giren su sıcaklığı | 35°C | Standart chiller kondenseri |
| Kuleden çıkan su sıcaklığı | 30°C | Approach 5°C varsayımı |
| Range | 5°C | T_giriş - T_çıkış |
| Approach | 5°C | T_çıkış - T_wb |
| Yaş termometre sıcaklığı | 25°C | Türkiye yaz ortalaması |
| CoC (konsantrasyon döngüsü) | 4 | Ortalama su kalitesi |
| Sürükleme oranı | %0.002 | Modern damla tutucu |
| Fan güç yoğunluğu | 0.02-0.04 kW/kW_soğutma | Kule kapasitesine bağlı |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |
| Yıllık çalışma saati | 2,500 saat/yıl | Türkiye, ticari bina soğutma sezonu |
| Elektrik birim fiyatı | 0.10 EUR/kWh | Türkiye sanayi tarifesi (yaklaşık) |

## Performans Tablosu

### Kapasite ve Tipe Göre Tipik Değerler

| Nominal Kapasite (kW) | Kule Tipi | Fan Gücü (kW) | Su Debisi (m³/h) | Yaklaşma (°C) | Yaklaşık Fiyat (EUR) |
|-----------------------|-----------|---------------|------------------|---------------|----------------------|
| 50-100 | Açık, karşı akışlı | 0.75-2.2 | 8-17 | 5-7 | 2,000-5,000 |
| 100-300 | Açık, karşı akışlı | 2.2-7.5 | 17-50 | 4-6 | 4,000-12,000 |
| 300-1,000 | Açık, karşı akışlı | 7.5-30 | 50-170 | 3-5 | 10,000-40,000 |
| 1,000-3,000 | Açık, çok hücreli | 30-90 | 170-500 | 3-5 | 35,000-100,000 |
| 3,000-10,000 | Açık, çok hücreli | 90-300 | 500-1,700 | 2-4 | 80,000-300,000 |
| 100-500 | Kapalı devre | 3-22 | 17-85 | 5-8 | 8,000-35,000 |
| 100-1,000 | Kuru soğutucu | 3-45 | 17-170 | 8-15 (kuru) | 5,000-30,000 |

### Performans Eğrisi — Yaklaşma vs Yaş Termometre Sıcaklığı

| Yaş Termometre (°C) | Yaklaşma @ %100 Yük (°C) | Yaklaşma @ %75 Yük (°C) | Yaklaşma @ %50 Yük (°C) |
|----------------------|--------------------------|--------------------------|--------------------------|
| 18 | 4.0 | 3.0 | 2.0 |
| 20 | 4.5 | 3.3 | 2.2 |
| 22 | 5.0 | 3.6 | 2.4 |
| 24 | 5.5 | 4.0 | 2.7 |
| 26 | 6.0 | 4.5 | 3.0 |
| 28 | 7.0 | 5.2 | 3.5 |

Kısmi yüklerde yaklaşma değeri iyileşir — bu, VSD fan kontrolü ile birlikte büyük tasarruf fırsatı sağlar.

## Dikkat Edilecekler

1. **Legionella riski:** Soğutma kuleleri en yüksek Legionella riski taşıyan ekipmanlardandır — düzenli su arıtma, biyosit dozajlama ve periyodik temizlik zorunludur; ihmal ciddi sağlık ve hukuki sonuçlar doğurabilir
2. **Dolgu kirlenmesi:** Film tipi dolgu, kirli su ile hızla tıkanır — kireç, biyofilm ve yosun birikimi ısı transfer alanını azaltır; düzenli temizlik veya tıkanmaya dayanıklı dolgu seçimi yapılmalıdır
3. **Su kayıpları:** Buharlaşma + blowdown + sürükleme toplamı ciddi su tüketimi oluşturur — CoC optimizasyonu ile blowdown minimize edilmeli; su kıt bölgelerde kuru soğutucu veya hibrit sistem değerlendirilmelidir
4. **Kış döneminde donma:** Kule suyu ve havuz suyunun donma riski vardır — kış aylarında by-pass, ısıtıcı veya glikol gerekebilir; donmuş dolgu mekanik hasar görebilir
5. **Fan titreşimi:** Fan dengesizliği, kule yapısında titreşim ve rezonans yaratabilir — fan balans kontrolü ve titreşim izleme önemlidir
6. **Kondenser suyu sıcaklığı sınırları:** Chiller üreticisinin belirlediği minimum kondenser suyu sıcaklığı aşılmamalıdır (tipik olarak 15-18°C) — aksi halde chiller kontrol sorunları yaşanabilir
7. **Yerleşim ve hava kısa devresi:** Kule çıkışından atılan nemli sıcak hava, emme tarafına geri dönebilir (recirculation) — kule yerleşimi, bina ve komşu kulelere olan mesafe, rüzgar yönü dikkate alınmalıdır
8. **Ses emisyonu:** Soğutma kuleleri önemli gürültü kaynağıdır — şehir içi yerleşimlerde çevresel gürültü yönetmeliğine uyum gereklidir; ses bariyeri, düşük gürültülü fan veya hız kontrolü değerlendirilmelidir

## İlgili Dosyalar
- Soğutucu akışkanlar: `equipment/chiller_refrigerants.md`
- Soğutma suyu sistemleri genel bakış: `equipment/chilled_water_systems.md`
- Santrifüj pompa: `equipment/pump_centrifugal.md`
- VSD pompa uygulaması: `solutions/pump_vsd.md`
- Chiller ekserji hesaplamaları: `formulas/chiller_exergy.md`
- Serbest soğutma (free cooling): `solutions/chiller_free_cooling.md`
- Soğutma benchmark verileri: `benchmarks/chiller_benchmarks.md`

## Referanslar
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 40: Cooling Towers.
- CTI (Cooling Technology Institute) Standard STD-201. *Certification Standard for Commercial Water Cooling Towers*.
- Kloppers, J.C. & Kröger, D.G. (2005). "A critical investigation into the heat and mass transfer analysis of counterflow wet-cooling towers," *Int. J. Heat and Mass Transfer*, 48, 765-777.
- Merkel, F. (1925). "Verdunstungskühlung," VDI-Zeitschrift, 70, 123-128. (Temel Merkel yöntemi)
- EN 13741:2003. *Thermal performance acceptance testing of mechanical draught series wet cooling towers*.
- EUROVENT Certification: Cooling Towers — Rating Standard.
- ASHRAE Guideline 12-2020. *Minimizing the Risk of Legionellosis Associated with Building Water Systems*.
- HSE L8 (UK Health and Safety Executive). *Legionnaires' disease — The control of legionella bacteria in water systems*, 4th edition.
- Türkiye Biyosidal Ürünler Yönetmeliği (2009/128/EC uyumlaştırma). Soğutma kulesi su arıtma gereksinimleri.
- SPX Cooling Technologies (Marley). *Cooling Tower Fundamentals*, 2nd Edition.
- BAC (Baltimore Aircoil Company). *Product and Application Handbook*.
- Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
- Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Edition, Wiley.
