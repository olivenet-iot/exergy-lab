---
title: "Döner Kurutucu (Rotary Dryer)"
category: dryer
equipment_type: dryer
keywords:
  - döner kurutucu
  - rotary dryer
  - tambur kurutucu
  - doğrudan temas
related_files:
  - dryer/formulas.md
  - dryer/benchmarks.md
  - dryer/solutions/exhaust_heat_recovery.md
  - dryer/solutions/insulation.md
  - dryer/sectors/wood_drying.md
use_when:
  - "Döner kurutucu analiz edilirken"
priority: medium
last_updated: 2026-02-01
---

# Döner Kurutucu (Rotary Dryer)

> Son güncelleme: 2026-02-01

## Genel Bakış

Döner kurutucu (rotary dryer), yatay veya hafif eğimli dönen bir silindir (tambur) içinde
granüler veya parçacıklı malzemenin sıcak hava veya sıcak yüzey yardımıyla kurutulduğu
endüstriyel bir kurutma sistemidir. Silindir iç yüzeyine monte edilen kanatçıklar (flights/lifters)
malzemeyi kaldırıp sıcak gaz akışına bırakarak etkin bir ısı ve kütle transferi sağlar. Yüksek
kapasitesi, sağlam yapısı ve geniş malzeme uyumluluğu sayesinde ağır sanayi uygulamalarında
en yaygın kullanılan kurutucu tipidir.

| Parametre | Değer |
|-----------|-------|
| Tip | Dönen silindir — doğrudan (direct) veya dolaylı (indirect) |
| Kapasite | 500 - 50.000 kg/h besleme |
| Giriş havası sıcaklığı (doğrudan) | 100 - 600 °C |
| Giriş havası sıcaklığı (dolaylı) | 80 - 200 °C |
| Silindir çapı | 1 - 5 m |
| Silindir uzunluğu | 5 - 30 m |
| L/D oranı | 4 - 10 (tipik) |
| Dönme hızı | 1 - 8 dev/dak |
| Eğim | %1 - 5 |
| Exergy verimi | %5 - 15 (tipik endüstriyel) |
| SMER | 0,3 - 1,0 kg/kWh |
| Enerji kaynağı | Doğal gaz, fuel oil, kömür, biyokütle, buhar (dolaylı) |

## Çalışma Prensibi

Döner kurutucu, yavaş dönme hareketindeki eğimli bir silindir boyunca malzemeyi ilerletirken
sıcak gaz ile temas ettirerek nemini uzaklaştırır. Temel çalışma adımları:

1. **Malzeme beslemesi (feeding):** Islak malzeme, silindir giriş ucundan (feed end) besleme
   vidalı veya şut aracılığıyla yüklenir.
2. **Dönme ve kaldırma (rotation & lifting):** Silindir, motor-dişli-zincir sistemiyle
   1-8 dev/dak hızda döner. İç kanatçıklar (flights/lifters) malzemeyi silindir tabanından
   kaldırır ve üstten sıcak gaz akışına perde (curtain) şeklinde bırakır.
3. **Isı ve kütle transferi:** Düşen malzeme tanecikleri sıcak gaz ile doğrudan temas eder;
   nem buharlaşarak gaz akışına geçer. Dolaylı tipte ise ısı silindir duvarı üzerinden
   iletim (conduction) yoluyla aktarılır.
4. **İlerleme (conveying):** Silindir eğimi (%1-5) ve gaz sürükleme etkisiyle malzeme
   giriş ucundan çıkış ucuna doğru ilerler. Kalma süresi 10-60 dakikadır.
5. **Çıkış ve ayırma:** Kurutulmuş malzeme çıkış ucundan (discharge end) boşaltılır.
   Egzoz gazı siklon ve/veya torba filtre ile toz ayrımına tabi tutulur.

### Doğrudan Kurutma (Direct Drying)

Sıcak gaz, malzeme ile doğrudan temas eder. Gaz sıcaklığı 100-600 °C arasında olabilir.
Yüksek kurutma hızı sağlar, ancak egzoz ile önemli enerji kaybı oluşur. Malzemenin gaz ile
kirlenmesi mümkündür (örneğin yanma ürünleri). Tipik exergy verimi %5-15 aralığındadır.

### Dolaylı Kurutma (Indirect Drying)

Isı, silindir çift cidarlı duvarı veya iç boru demetleri üzerinden iletim ile aktarılır.
Buhar veya sıcak yağ ısıtma ortamı olarak kullanılır. Egzoz debisi çok düşüktür ve hassas
veya toz hassasiyetli malzemeler için uygundur. Tipik exergy verimi %10-20 aralığındadır,
düşük egzoz kaybı sayesinde doğrudan tipe kıyasla daha yüksektir.

### Eş Yönlü ve Karşı Yönlü Akış

| Konfigürasyon | Açıklama | Avantaj | Dezavantaj |
|---------------|----------|---------|------------|
| Eş yönlü (co-current) | Gaz ve malzeme aynı yönde ilerler | Isıya duyarlı malzemeler için uygun; ürün sıcaklığı düşük kalır | Egzoz sıcaklığı yüksek, verimlilik düşer |
| Karşı yönlü (counter-current) | Gaz ve malzeme zıt yönde ilerler | Düşük egzoz sıcaklığı, yüksek termal verimlilik | Ürün yüksek sıcaklığa maruz kalır; hassas malzeme için uygun değil |

### Kanatçık Tipleri (Flight Types)

Kanatçık tasarımı, malzeme-gaz temas etkinliğini doğrudan belirler:

| Kanatçık Tipi | Açıklama | Uygulama |
|---------------|----------|----------|
| Düz radyal (straight radial) | Silindir duvarından dik çıkar | Genel amaç, kolay imalat |
| Kaldırmalı (lifting) | Açılı kanat, malzemeyi yükseğe taşır | Granül ve iri tanecikler |
| Sarkıtmalı / kademeli (angled/stepped) | Kademeyi bırakma etkisi | Yapışmayan kuru malzemeler |
| Kombine (multi-section) | Silindir boyunca farklı tipler | Islak bölgede kaldırma, kuru bölgede yayma |

## Tipler

### 1. Doğrudan Ateşlemeli Döner Kurutucu (Direct-Fired Rotary Dryer)

- En yaygın tip; brülör veya fırın egzoz gazı doğrudan silindir içine verilir
- Giriş gazı sıcaklığı: 200-600 °C
- Kapasite: 1.000-50.000 kg/h
- Mineraller, agregalar, cevher kurutma

### 2. Dolaylı Isıtmalı Döner Kurutucu (Indirect/Steam Tube Rotary Dryer)

- Silindir içine yerleştirilen buhar boruları veya çift cidarlı gövde ile ısıtma
- Giriş ortam sıcaklığı: 80-200 °C (buhar basıncına bağlı)
- Kapasite: 500-15.000 kg/h
- Hassas malzemeler, çamur (sludge), kimyasal ürünler

### 3. Üç Geçişli Döner Kurutucu (Triple-Pass Rotary Dryer)

- İç içe üç konsantrik silindir; malzeme üç geçiş yapar
- Daha kompakt; aynı kapasitede %40-60 daha kısa uzunluk
- Biyokütle, odun talaşı, hayvan yemi kurutma
- Yüksek termal verimlilik: daha düşük egzoz kaybı

### 4. Döner Fırın-Kurutucu Kombinasyonu (Rotary Kiln-Dryer)

- Tek silindir içinde ön kurutma ve kalsinasyon/kavurma
- Çimento hammaddesi, kireçtaşı, kaolin işleme
- Çok yüksek sıcaklık (600-1000 °C gaz giriş)

## Parametreler

### Giriş (Ölçüm) Parametreleri

| Parametre | Birim | Tipik Aralık | Açıklama |
|-----------|-------|-------------|----------|
| Giriş gaz sıcaklığı (T_gas_in) | °C | 100-600 | Brülör veya ısıtıcı çıkış sıcaklığı |
| Ortam sıcaklığı (T_0) | °C | 15-40 | Referans (ölü durum) sıcaklığı |
| Malzeme giriş nemi (M_in) | % (yaş baz) | 5-50 | Besleme malzemesi nem içeriği |
| Malzeme çıkış nemi (M_out) | % (yaş baz) | 0,5-8 | Ürün hedef nem içeriği |
| Besleme debisi (m_feed) | kg/h | 500-50.000 | Islak malzeme besleme hızı |
| Yakıt tüketimi (fuel_rate) | m³/h veya kg/h | - | Brülör yakıt debisi |
| Egzoz sıcaklığı (T_exhaust) | °C | 70-150 | Silindir çıkışındaki gaz sıcaklığı |
| Egzoz nemi (RH_exhaust) | % RH | 30-80 | Egzoz gazı bağıl nemi |
| Gövde yüzey sıcaklığı (T_shell) | °C | 50-120 | Radyasyon kaybı hesabı için |
| Silindir dönme hızı | dev/dak | 1-8 | - |
| Silindir boyutları (D x L) | m | 1-5 çap, 5-30 uzunluk | - |

### Hesaplanan Parametreler

| Parametre | Formül / Açıklama | Birim |
|-----------|-------------------|-------|
| Buharlaşan su (m_evap) | m_feed × (M_in - M_out) / (1 - M_out) | kg/h |
| Özgül enerji tüketimi (SEC) | Q_total / m_evap | kJ/kg su |
| SMER | m_evap / Q_total (kW cinsinden) | kg/kWh |
| Termal verimlilik | Q_evaporation / Q_input × 100 | % |
| Exergy verimi (psi) | Ex_evaporation / Ex_input × 100 | % |
| Gövde radyasyon kaybı | epsilon × sigma × A_shell × (T_shell⁴ - T_0⁴) | kW |
| Doluluk oranı (fill ratio) | V_malzeme / V_silindir | - (tipik 0,10-0,15) |

### Varsayılan Değerler

| Parametre | Varsayılan | Birim | Kaynak |
|-----------|-----------|-------|--------|
| Ortam sıcaklığı (T_0) | 25 | °C | ISO standart |
| Ortam nemi (RH_0) | 60 | % | Tipik endüstriyel |
| Giriş gaz sıcaklığı (doğrudan) | 350 | °C | Orta ölçek mineral kurutma |
| Egzoz sıcaklığı | 110 | °C | Tipik değer |
| Malzeme giriş nemi | 20 | % (yaş baz) | Mineral için tipik |
| Malzeme çıkış nemi | 3 | % (yaş baz) | Mineral için tipik |
| Gövde emisivitesi (emissivity) | 0,85 | - | Boyalı çelik yüzey |
| Doluluk oranı | 0,12 | - | Optimum aralıkta |
| Brülör verimi | 0,88 | - | Doğal gaz brülör |
| Fan verimi | 0,70 | - | Standart santrifüj fan |
| Mekanik tahrik verimi | 0,95 | - | Dişli sistemi |
| Yıllık çalışma saati | 6.000 | h/yıl | Sürekli endüstriyel işletme |

## Exergy Analizi

### Exergy Girdisi

Döner kurutucunun exergy girdisi temel olarak yakıtın kimyasal exergysinden veya sıcak gazın
termomekanik exergysinden oluşur:

```
Ex_input = Ex_fuel + W_fan + W_drive

Ex_fuel = m_fuel × ex_ch   (kimyasal exergy, doğal gaz için ~51.000 kJ/kg)

Ex_gas = m_gas × [Cp × (T - T0 - T0 × ln(T/T0))]   (termal exergy)

Burada:
  T0 = Referans sıcaklığı (298,15 K)
  T  = Gaz sıcaklığı (K)
  Cp = Gazın özgül ısısı (kJ/kg·K)
```

### Exergy Çıktısı (Faydalı)

Kurutma işleminin faydalı exergy çıktısı, malzemeden uzaklaştırılan nemin exergy değişimidir:

```
Ex_useful = m_evap × [h_fg × (1 - T0/T_evap) + Cp_w × (T_product - T0 - T0 × ln(T_product/T0))]
```

### Exergy Verimi

```
psi = Ex_useful / Ex_input × 100

Tipik değerler:
  Doğrudan döner kurutucu:  %5 - 15
  Dolaylı döner kurutucu:   %10 - 20
  Isı geri kazanımlı:       %15 - 25
```

Döner kurutucuların exergy verimi düşüktür; bunun temel nedeni yüksek sıcaklıktaki girdinin
düşük sıcaklıktaki buharlaşma işlemine aktarılmasıdır. Büyük sıcaklık farkı (Delta_T) yüksek
tersinmezlik (irreversibility) ve dolayısıyla yüksek exergy yıkımı üretir.

## Kayıp Dağılımı

### Enerji Kayıp Dağılımı

| Kayıp Bileşeni | Oran (%) | Açıklama |
|----------------|----------|----------|
| Buharlaşma (faydalı iş) | ~35-40 | Malzemedeki suyun buharlaştırılması |
| Egzoz gazı kaybı (exhaust loss) | ~30-40 | Yüksek sıcaklık ve debide atılan gaz |
| Gövde radyasyon kaybı (shell radiation) | ~8-15 | Büyük silindir yüzeyinden ısı kaybı |
| Ürün ısıtma (product heating) | ~3-5 | Malzeme kütlesinin ısıtılması |
| Diğer (sızıntı, toz toplama, vb.) | ~3-5 | Conta sızıntıları, fan kayıpları |

### Exergy Kayıp Dağılımı

| Exergy Kayıp Bileşeni | Oran (%) | Açıklama |
|------------------------|----------|----------|
| Egzoz gazı exergy kaybı | 40 - 50 | En büyük kaynak; yüksek debili sıcak ve nemli egzoz |
| Yanma tersinmezliği (combustion irreversibility) | 15 - 25 | Kimyasal exergynin termal exergyye dönüşümündeki kayıp |
| Isı transferi tersinmezliği | 10 - 15 | Büyük Delta_T nedeniyle temas bölgesinde exergy yıkımı |
| Gövde radyasyon kaybı | 5 - 10 | Düşük sıcaklıkta geniş yüzey; düşük exergy oranı |
| Mekanik sürtünme ve tahrik | 2 - 5 | Dişli, rulman, fan mekanik kayıpları |
| Karışma ve difüzyon | 1 - 3 | Gaz-buhar karışım entropisi |

> **Kilit nokta:** Egzoz gazı kaybı hem enerji hem exergy açısından baskın kayıptır.
> Yanma tersinmezliği ise yalnızca exergy analizinde görünür; enerji analizinde gizlidir.
> Bu, exergy analizinin gerçek kayıp kaynaklarını ortaya çıkarmadaki üstünlüğünü gösterir.

### Tipik Enerji Tüketim Değerleri

| Parametre | Değer | Birim |
|-----------|-------|-------|
| Özgül enerji tüketimi (SEC) | 3.500 - 6.500 | kJ/kg su buharlaştırma |
| Elektrik tüketimi (tahrik + fan) | 30 - 200 | kW |
| Isıtma gücü (thermal input) | 500 - 20.000 | kW |
| Hava debisi | 10.000 - 200.000 | m³/h |
| Rejime geçiş süresi | 30 - 120 | dakika |

## Avantaj/Dezavantajlar

### Avantajlar

| Avantaj | Açıklama |
|---------|----------|
| Yüksek kapasite | 500-50.000 kg/h; büyük ölçekli endüstriyel kurutma için ideal |
| Geniş malzeme uyumluluğu | Mineraller, biyokütle, çamur, kimyasallar, gıda yan ürünleri |
| Sağlam ve dayanıklı yapı | Ağır çalışma koşullarına (toz, aşınma, yüksek sıcaklık) uygun |
| Basit işletme | Düşük operatör beceri gereksinimi; sürekli beslemeli otomatik çalışma |
| Geniş sıcaklık aralığı | 80-600 °C; düşükten yükseğe çeşitli ısı kaynakları kullanılabilir |
| Uzun ömür | Düzgün bakım ile 20-30 yıl hizmet ömrü |
| Atık ısı kullanımı | Fırın, kazan, türbin egzoz gazlarıyla beslenebilir |

### Dezavantajlar

| Dezavantaj | Açıklama |
|------------|----------|
| Düşük exergy verimi | Tipik %5-15; büyük Delta_T ve yüksek egzoz kaybı |
| Büyük tesis alanı | L/D oranı 4-10; 30 m'ye kadar uzunluk, ağır temel gerekir |
| Yüksek termal kütle | Rejime geçiş süresi 30-120 dak; sık duruş/kalkış büyük enerji kaybı |
| Toz oluşumu | Kanatçık hareketi toz üretir; siklon/filtre enerji tüketir |
| Conta sızıntıları | Dönen-sabit bağlantılarda hava sızıntısı verimi düşürür |
| Yüksek egzoz kaybı | Toplam girdinin %30-40'ı egzoz ile atılır |
| Yavaş tepki süresi | Proses parametre değişikliklerine yavaş yanıt; kontrol güçlüğü |

## Uygulamalar

### Sektörel Kullanım Alanları

| Sektör | Tipik Malzeme | Giriş Nemi (%) | Çıkış Nemi (%) | Gaz Sıcaklığı (°C) |
|--------|---------------|:--------------:|:--------------:|:------------------:|
| Mineraller ve kum | Kuvars, kalsit, kil | 8-15 | 0,5-2 | 300-600 |
| Agregalar ve inşaat | Kum, çakıl, cüruf | 5-12 | 0,5-3 | 250-500 |
| Biyokütle | Odun talaşı, kabuk, pelet hammaddesi | 40-55 | 8-15 | 200-400 |
| Çamur (sludge) | Arıtma çamuru, endüstriyel çamur | 60-85 | 10-30 | 300-500 |
| Gübre | Granül gübre, fosfat | 8-15 | 1-3 | 200-350 |
| Madencilik | Cevher konsantresi, kömür | 8-20 | 1-5 | 300-600 |
| Hayvan yemi | Yem hammaddesi, küspe | 15-35 | 8-12 | 150-300 |
| Kimya | Tuz, pigment, katalizör | 5-20 | 0,5-2 | 150-350 |

### Öne Çıkan Uygulamalar

- **Odun talaşı kurutma (wood chip drying):** Pelet üretimi için %50 nemden %10 neme kurutma;
  üç geçişli tip tercih edilir. Biyokütle kazanı veya CHP egzoz gazı ile beslenebilir.
- **Mineral kumu kurutma:** Döküm kumu, cam kumu; yüksek sıcaklıkta doğrudan ateşleme.
- **Arıtma çamuru kurutma:** Mekanik ön susuzlaştırma sonrası %20-30 KM'den %85-95 KM'ye.
- **Agrega kurutma:** Asfalt plent kurutucuları; 500-600 °C gaz giriş sıcaklığı.

## İyileştirme

### Enerji ve Exergy İyileştirme Fırsatları

| Önlem | Enerji Tasarrufu (%) | Yatırım (EUR) | Geri Ödeme | Exergy Etkisi |
|-------|:-------------------:|:--------------:|:----------:|---------------|
| Egzoz ısı geri kazanımı (heat recovery) | 15-25 | 50.000-250.000 | 1-3 yıl | Egzoz exergy kaybını %30-50 azaltır |
| Gövde dış yalıtımı (insulation) | 8-15 | 20.000-80.000 | 1-2 yıl | Radyasyon kaybını %60-80 azaltır |
| Kanatçık optimizasyonu (flight redesign) | 5-10 | 15.000-60.000 | 1-2 yıl | Isı transferi tersinmezliğini düşürür |
| Conta iyileştirmesi (seal upgrade) | 3-7 | 5.000-20.000 | 0,5-1 yıl | Karışma exergy kaybını azaltır |
| Değişken hızlı tahrik (VFD) | 5-15 (elektrik) | 10.000-40.000 | 1-2 yıl | Mekanik exergy kaybını düşürür |
| Doluluk oranı kontrolü | 3-8 | 5.000-15.000 | 0,5-1 yıl | Temas etkinliğini artırır |
| Otomatik egzoz sıcaklık kontrolü | 5-10 | 8.000-25.000 | 1-1,5 yıl | Egzoz kaybını sürekli minimize eder |
| Mekanik ön susuzlaştırma (pre-dewatering) | 10-30 | 30.000-200.000 | 1-3 yıl | Toplam exergy girdisini azaltır |
| Karşı yönlü akışa geçiş (co→counter) | 5-12 | 50.000-150.000 | 2-4 yıl | Egzoz sıcaklığını düşürür |
| Atık ısı beslemesi (waste heat utilization) | 20-40 | 40.000-300.000 | 1-3 yıl | Yanma tersinmezliğini ortadan kaldırır |

### İyileştirme Önceliklendirme

1. **Egzoz ısı geri kazanımı** — En yüksek tasarruf, kabul edilebilir geri ödeme; egzoz
   gazı ile giriş havasını veya besleme malzemesini ön ısıtma.
2. **Gövde yalıtımı** — Düşük yatırım, hızlı geri ödeme; 50-100 mm mineral yünü veya
   kalsiyum silikat ile gövde yüzey sıcaklığını 120 °C'den 45 °C'ye düşürmek mümkün.
3. **Conta iyileştirmesi** — Dönen-sabit bağlantılarda labirent veya esnek contalarla
   hava sızıntısını minimize etmek; düşük yatırımlı hızlı kazanım.
4. **Kanatçık tasarımı** — CFD destekli kanatçık optimizasyonu ile malzeme-gaz temas
   süresini ve dağılımını iyileştirme; %5-10 verimlilik artışı.
5. **Otomatik kontrol** — Egzoz sıcaklığı ve nem bazlı PID kontrol ile işletme koşullarını
   sürekli optimize etme.

### Cross-Equipment Fırsatları

Döner kurutucu, fabrika düzeyinde exergy entegrasyonunda önemli bir ısı alıcısıdır:

- **Kazan/türbin egzoz gazı → kurutucu:** 200-500 °C sıcaklıktaki egzoz gazları doğrudan
  kurutucu ısı kaynağı olarak kullanılabilir; yanma tersinmezliği ortadan kalkar.
- **Fırın atık ısısı → kurutucu:** Çimento, seramik, cam fırınlarının egzoz gazları.
- **Kompresör atık ısısı → ön ısıtma:** Düşük sıcaklıklı (80-120 °C) kompresör soğutma
  suyu ile besleme malzemesini veya giriş havasını ön ısıtma.
- **Kurutucu egzoz → ekonomizer:** Kurutucu egzoz gazının kazan besleme suyu ön ısıtması.

## Yatırım

### Kapasite-Maliyet Tablosu

| Kapasite (kg/h besleme) | Silindir Boyutu (D×L, m) | Termal Güç (kW) | Tahmini Yatırım (EUR) | SMER (kg/kWh) |
|------------------------:|:------------------------:|:----------------:|:---------------------:|:--------------:|
| 500-1.000 | 1,2 × 6 | 200-500 | 80.000-200.000 | 0,4-0,7 |
| 1.000-3.000 | 1,5 × 10 | 500-1.500 | 200.000-500.000 | 0,5-0,8 |
| 3.000-8.000 | 2,0 × 14 | 1.500-4.000 | 400.000-900.000 | 0,5-0,9 |
| 8.000-15.000 | 2,5 × 18 | 3.000-8.000 | 700.000-1.500.000 | 0,6-0,9 |
| 15.000-30.000 | 3,5 × 22 | 6.000-15.000 | 1.200.000-2.500.000 | 0,6-1,0 |
| 30.000-50.000 | 4,5 × 28 | 12.000-25.000 | 2.000.000-4.000.000 | 0,6-1,0 |

> **Not:** Yatırım maliyetleri 2026 yılı Avrupa piyasa fiyatlarıdır; montaj, temel, toz toplama
> sistemi ve otomasyon dahil. Dolaylı tip için maliyet %20-40 daha yüksektir.

### İşletme Maliyetleri

| Maliyet Kalemi | Tipik Değer | Açıklama |
|----------------|-------------|----------|
| Yakıt (doğal gaz) | 15-60 EUR/saat | Kapasiteye bağlı; 500-20.000 kW termal güç |
| Elektrik (fan + tahrik) | 3-15 EUR/saat | 30-200 kW elektrik tüketimi |
| Bakım | %2-4/yıl × yatırım | Kanatçık, conta, rulman değişimi |
| Toz toplama filtresi | 2.000-10.000 EUR/yıl | Torba/kartuş değişimi |

### SMER Benchmark

| Performans Seviyesi | SMER (kg/kWh) | Değerlendirme |
|---------------------|:-------------:|---------------|
| Düşük performans | < 0,5 | Acil iyileştirme gerekli; yalıtım, conta, kontrol eksikliği |
| Tipik alt sınır | 0,5-0,7 | Eski veya bakım gerektiren sistem |
| Tipik üst sınır | 0,7-1,0 | Normal çalışan, kısmen optimize sistem |
| İyi performans | 1,0-1,3 | Modern, optimize edilmiş sistem |
| En iyi uygulama (best practice) | 1,3-1,5 | Isı geri kazanımlı, yalıtımlı, otomatik kontrollü |
| Teorik sınır | ~1,6 | İdeal koşullarda termodinamik sınır |

### Exergy Verimi Benchmark

| Seviye | Exergy Verimi (%) | Yorum |
|--------|:-----------------:|-------|
| Düşük | < 8 | Büyük iyileştirme potansiyeli; ısı geri kazanım yok, yalıtım yok |
| Orta | 8-15 | Tipik endüstriyel döner kurutucu |
| İyi | 15-20 | Optimize edilmiş; yalıtım + egzoz ısı geri kazanımı |
| Mükemmel | > 20 | En iyi uygulama; atık ısı beslemeli dolaylı tip |

## İlgili Dosyalar

- `knowledge/dryer/formulas.md` — Kurutma exergy hesaplama formülleri (SEC, SMER, exergy verimi)
- `knowledge/dryer/benchmarks.md` — Genel kurutucu benchmark değerleri ve karşılaştırma
- `knowledge/dryer/solutions/exhaust_heat_recovery.md` — Egzoz ısı geri kazanım çözümleri
- `knowledge/dryer/solutions/insulation.md` — Yalıtım iyileştirme detayları ve hesapları
- `knowledge/dryer/sectors/wood_drying.md` — Odun kurutma sektörel uygulama rehberi
- `knowledge/dryer/equipment/belt_dryer.md` — Bant kurutucu (alternatif karşılaştırma)
- `knowledge/dryer/equipment/fluidized_bed.md` — Akışkan yataklı kurutucu (alternatif)
- `knowledge/dryer/equipment/tunnel_dryer.md` — Tünel kurutucu detayları
- `knowledge/factory/cross_equipment.md` — Ekipmanlar arası exergy entegrasyon fırsatları
- `knowledge/factory/waste_heat_recovery.md` — Atık ısı geri kazanım stratejileri

## Referanslar

1. Mujumdar, A.S. (2014). *Handbook of Industrial Drying*, 4th Edition, CRC Press — Bölüm 7: Rotary Drying.
2. Perry, R.H. & Green, D.W. (2019). *Perry's Chemical Engineers' Handbook*, 9th Edition, McGraw-Hill — Section 12: Psychrometry, Evaporative Cooling, and Solids Drying.
3. European Commission (2006). *Reference Document on Best Available Techniques in the Cement, Lime and Magnesium Oxide Manufacturing Industries (CLM BREF)* — Kurutma enerji verimliliği.
4. European Commission (2006). *Reference Document on Best Available Techniques for Large Volume Inorganic Chemicals (LVIC BREF)* — Endüstriyel kurutma BAT değerleri.
5. Kemp, I.C. (2012). "Fundamentals of Energy Analysis of Dryers", *Modern Drying Technology*, Vol. 4, Wiley-VCH.
6. Kudra, T. & Mujumdar, A.S. (2009). *Advanced Drying Technologies*, 2nd Edition, CRC Press — Bölüm 3: Rotary Dryers.
7. Dincer, I. & Rosen, M.A. (2013). *Exergy: Energy, Environment and Sustainable Development*, 2nd Edition, Elsevier.
8. Szargut, J. (2005). *Exergy Method: Technical and Ecological Applications*, WIT Press.
9. Friedman, S.J. & Marshall, W.R. (1949). "Studies in Rotary Drying", *Chemical Engineering Progress*, 45(9) — Klasik döner kurutucu modeli.
10. DOE/AMO. *Improving Process Heating System Performance — A Sourcebook for Industry*, U.S. Department of Energy.
