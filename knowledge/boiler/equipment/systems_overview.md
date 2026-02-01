---
title: "Buhar Sistemleri Genel Bakış — Steam Systems Overview"
category: equipment
equipment_type: boiler
subtype: "Sistem Genel Bakış"
keywords: [kazan sistemi, buhar, genel bakış]
related_files: [boiler/formulas.md, boiler/benchmarks.md, boiler/audit.md]
use_when: ["Kazan sistemine genel bakış gerektiğinde", "Buhar/sıcak su sistemi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Buhar Sistemleri Genel Bakış — Steam Systems Overview

> Son güncelleme: 2026-01-31

## Genel Bilgiler

Buhar, endüstride en yaygın kullanılan enerji taşıyıcılarından biridir. Isıtma, kurutma, sterilizasyon, güç üretimi ve proses uygulamalarında kritik rol oynar. Tipik bir endüstriyel tesisin toplam birincil enerji tüketiminin %30-60'ı buhar üretimi için harcanır.

- Tip: Enerji taşıyıcı akışkan (su buharı, H₂O gaz fazı)
- Basınç aralığı: 0.5 - 120+ bar
- Sıcaklık aralığı: 100 - 540+ °C
- Yaygın yakıtlar: Doğalgaz, fuel oil, kömür, biyokütle, atık ısı

### Basınç Sınıflandırması

| Sınıf | Basınç Aralığı (bar) | Sıcaklık (°C) | Tipik Kullanım |
|-------|----------------------|---------------|----------------|
| Düşük basınç (LP) | 1 - 5 | 100 - 158 | Isıtma, nemlendirme, sterilizasyon |
| Orta basınç (MP) | 5 - 25 | 158 - 224 | Proses ısıtma, kurutma, pişirme |
| Yüksek basınç (HP) | 25 - 100+ | 224 - 311+ | Türbin tahriği, güç üretimi, petrokimya |

### Buhar vs Sıcak Su Karşılaştırması

| Özellik | Buhar | Sıcak Su |
|---------|-------|----------|
| Enerji yoğunluğu | Yüksek (gizli ısı: ~2100 kJ/kg @ 10 bar) | Düşük (duyulur ısı: ~80 kJ/kg, ΔT=20°C) |
| Sıcaklık aralığı | 100 - 540+ °C | 60 - 200 °C (basınçlı) |
| Isı transfer katsayısı | ~5000-10000 W/m²K (yoğuşma) | ~1000-5000 W/m²K |
| Dağıtım kaybı | %3-10 (iyi izolasyonla) | %2-5 |
| Kontrol kolaylığı | Orta (basınç ile) | Yüksek (sıcaklık ile) |
| Yatırım maliyeti | Yüksek (kapanlar, kondensat hattı) | Orta |
| Güvenlik riski | Yüksek (basınçlı, yüksek sıcaklık) | Orta |
| Exergy verimi | %15-35 (tipik sistem) | %10-25 (tipik sistem) |

**Kural:** T < 100°C uygulamalarda sıcak su, T > 100°C veya gizli ısı gereken uygulamalarda buhar tercih edilir.

## Buhar Üretimi (Steam Generation)

### Kazan Tipleri

| Tip | Kapasite (t/h) | Basınç (bar) | Verim (%) | Avantaj | Dezavantaj |
|-----|---------------|-------------|-----------|---------|------------|
| Alev borulu (Firetube) | 0.5 - 25 | 1 - 25 | 82-90 | Kompakt, düşük maliyet, kolay işletme | Düşük basınç sınırı |
| Su borulu (Watertube) | 5 - 500+ | 10 - 120+ | 85-94 | Yüksek basınç/kapasite, hızlı yanıt | Yüksek yatırım, daha karmaşık |
| HRSG (Atık Isı Kazanı) | 5 - 300+ | 5 - 100+ | 70-85 (ek yakıtsız) | Atık ısıdan buhar üretimi | Egzoz kaynağına bağımlı |
| Elektrikli kazan | 0.1 - 5 | 1 - 25 | ~98 | Emisyonsuz, kompakt | Yüksek işletme maliyeti |

### Besleme Suyu Sistemi (Feedwater System)

Besleme suyu kalitesi kazan ömrü ve verimliliği için kritiktir:

1. **Su arıtma:** Sertlik giderme (softening), demineralizasyon (RO/IX)
2. **Deaeratör:** Çözünmüş O₂ ve CO₂ giderimi (ayrı bölümde detaylı)
3. **Ekonomizer:** Baca gazı ile besleme suyunun ön ısıtılması
   - Tipik tasarruf: Her 20°C ön ısıtma ≈ %1 verim artışı
   - Ekonomizer çıkış suyu sıcaklığı: 85-105°C (yoğuşmalı: 120-140°C)

### Blowdown (Kazan Tahliyesi)

Kazan suyundaki çözünmüş katı konsantrasyonunu kontrol altında tutmak için su tahliyesi yapılır.

- **Sürekli blowdown (continuous):** TDS kontrolü için sürekli küçük debide tahliye
- **Aralıklı blowdown (intermittent):** Dip çamuru ve tortu için periyodik tahliye
- Tipik blowdown oranı: %2-5 (besleme suyu debisinin)
- Blowdown suyunun entalpisi yüksektir — ısı geri kazanımı değerlendirilmelidir

```
Blowdown ısı kaybı = m_bd × h_f(P_kazan)

Burada:
  m_bd  = Blowdown debisi (kg/s)
  h_f   = Doyma sıvı entalpisi kazan basıncında (kJ/kg)
```

## Buhar Dağıtımı (Steam Distribution)

### Buhar Kolektörü (Steam Header) Tasarımı

Buhar kolektörü, kazanlardan gelen buharı farklı kullanım noktalarına dağıtan ana boru hattıdır.

- **Yüksek basınç kolektörü (HP header):** Kazandan çıkış, türbin girişi
- **Orta basınç kolektörü (MP header):** Proses uygulamaları
- **Düşük basınç kolektörü (LP header):** Isıtma, deaeratör besleme

### Boru Boyutlandırma

| Parametre | Önerilen Değer | Not |
|-----------|---------------|-----|
| Buhar hızı (doymuş) | 25-35 m/s | Ana hat |
| Buhar hızı (kızgın) | 35-50 m/s | Yüksek basınç hatları |
| Basınç düşüşü (toplam) | <%5 üretim basıncının | Sistem genelinde hedef |
| Kondensat hattı hızı | 1-2 m/s | Erozyon sınırlaması |

### Basınç Düşürme İstasyonu (Pressure Reduction Station — PRS)

Yüksek basınçlı buharı kullanım noktasının ihtiyacına göre düşüren istasyondur.

Bileşenler:
1. **Basınç düşürme vanası (PRV):** Basıncı düşürür, entalpi sabit kalır (isentalpik)
2. **Desuperheater (kızgınlık giderici):** Gerektiğinde su spreyleri ile buharı doyma sıcaklığına yaklaştırır
3. **Güvenlik vanası:** Aşırı basınçtan koruma
4. **By-pass hattı:** Bakım sırasında devamlılık

**Exergy notu:** PRV'de basınç düşürülmesi sırasında sıcaklık da düşer ancak isentalpik genişleme tersinmez bir süreçtir — exergy yıkımı oluşur. Alternatif olarak back-pressure türbin kullanılırsa exergy yıkımı yerine güç üretimi yapılabilir.

### Tipik Basınç Kayıpları

```
Kazan çıkışı          : 12.0 bar(g)
  ↓ Kolektör           : -0.1 bar
  ↓ Ana hat boruları   : -0.2-0.5 bar
  ↓ Branş hatları      : -0.1-0.3 bar
  ↓ Kontrol vanaları   : -0.3-0.5 bar
  ↓ Eşanjör girişi     : -0.1-0.2 bar
Kullanım noktası       : 10.0-11.0 bar(g)
```

### İzolasyon Gereksinimleri

| Boru Çapı (DN) | İzolasyon Kalınlığı (mm) | Yüzey Sıcaklığı Hedefi |
|----------------|--------------------------|------------------------|
| DN25 - DN50 | 40-50 | <50°C |
| DN65 - DN150 | 50-80 | <50°C |
| DN200 - DN400 | 80-100 | <50°C |
| Vana ve flanşlar | Sökülür takılır ceket | <60°C |

- Eksik veya hasarlı izolasyon tipik buhar kaybının %5-10'unu oluşturur
- Çıplak bir DN100 boru (10 bar, 184°C): ~500 W/m ısı kaybı
- İzole edilmiş aynı boru: ~50 W/m ısı kaybı (90% azalma)

## Buhar Kullanımı (Steam Utilization)

### Doğrudan Isıtma (Direct Steam Injection)

Buhar doğrudan ürüne veya prosese enjekte edilir. Yüksek ısı transfer hızı sağlar ancak kondensat geri dönüşü mümkün değildir.

- Uygulamalar: CIP yıkama, tekstil boyama, kağıt hamuru, beton kürleme
- Avantaj: Hızlı ısıtma, basit ekipman
- Dezavantaj: Kondensat kaybı, ürün seyreltmesi

### Dolaylı Isıtma (Indirect Heating)

Buhar, bir ısı eşanjörü veya serpantin aracılığıyla ürüne ısı aktarır. Kondensat geri döndürülebilir.

- Kabuk-boru (Shell & tube) eşanjör
- Plakalı eşanjör
- Serpantinli ısıtıcı (coil)
- Ceketli tank (jacketed vessel)

### Güç Üretimi (Power Generation)

| Türbin Tipi | Çalışma Prensibi | Çıkış | Tipik Verim |
|-------------|-------------------|-------|-------------|
| Karşı basınçlı (Back-pressure) | Buhar türbinden geçer, çıkışta proses basıncında | Elektrik + proses buharı | %80-90 (toplam, kojenerasyon) |
| Yoğuşmalı (Condensing) | Buhar vakuma kadar genişler | Sadece elektrik | %25-35 (elektrik) |
| Çekiş (Extraction) | Ara kademeden buhar çekilir | Elektrik + buhar | %75-85 (toplam) |

### Mekanik Tahrik (Mechanical Drive)

Buhar türbini doğrudan pompa, kompresör veya fan tahrik eder. Elektrik motoruna alternatiftir.

- Avantaj: Hız kontrolü kolay, elektrik şebekesinden bağımsız
- Dezavantaj: Düşük verim (~%20-30 tek başına), bakım yoğun

### Sektörel Uygulama Tablosu

| Sektör | Tipik Basınç (bar) | Ana Uygulama | Buhar Tüketimi (t/t ürün) |
|--------|-------------------|-------------|---------------------------|
| Gıda ve içecek | 3-15 | Pişirme, sterilizasyon, CIP | 0.5-3.0 |
| Tekstil | 5-15 | Boyama, kurutma, ütüleme | 5-20 |
| Kağıt ve selüloz | 5-40 | Pişirme, kurutma, güç üretimi | 2-5 |
| Kimya | 5-60 | Proses ısıtma, distilasyon, reaksiyon | 1-10 |
| Petrokimya | 10-100+ | Proses, güç, mekanik tahrik | 3-15 |
| İlaç | 3-10 | Sterilizasyon, HVAC, temiz buhar | 0.3-2.0 |
| Lastik ve plastik | 5-15 | Kalıplama, vulkanizasyon | 1-5 |
| Hastane | 3-10 | Sterilizasyon, HVAC, mutfak | - |

## Kondensat Geri Dönüşü (Condensate Return)

Buhar ısısını verdikten sonra yoğuşan su (kondensat) önemli miktarda enerji içerir.

### Kondensat Enerji İçeriği

```
Q_kondensat = m_k × h_f(T_k)

Burada:
  Q_kondensat = Kondensatın taşıdığı ısı enerjisi (kW)
  m_k         = Kondensat debisi (kg/s)
  h_f(T_k)    = Kondensat sıcaklığındaki doyma sıvı entalpisi (kJ/kg)
```

Örnek: 10 bar kondensat sıcaklığı ~184°C, h_f ≈ 763 kJ/kg. Bu, 15°C taze suyun entalpisi (63 kJ/kg) ile karşılaştırıldığında ~700 kJ/kg enerji tasarrufu sağlar.

### Geri Dönüş Oranı Kıyaslaması

| Geri Dönüş Oranı | Değerlendirme | Tipik Durum |
|-------------------|--------------|-------------|
| >80% | İyi | Bakımlı, kapalı devre sistem |
| 60-80% | Orta | Kısmen açık proses, bazı kayıplar |
| 40-60% | Kötü | Çok sayıda kaçak, açık proses |
| <40% | Çok kötü | Kondensat geri dönüş sistemi yetersiz veya yok |

### Kondensat Geri Dönüşünden Tasarruf

- Her %10 geri dönüş artışı ≈ %1-3 yakıt tasarrufu
- Ek tasarruf: Su arıtma kimyasalı, taze su, atıksu maliyeti
- Tipik geri ödeme süresi: 6-18 ay

### Kontaminasyon Riskleri

- **Yağ kontaminasyonu:** Buhar silindirli makineler, eski kondensat pompaları
- **Ürün kontaminasyonu:** Eşanjör kaçağı (gıda, kimya proseslerinde)
- **Korozyon ürünleri:** Demir oksit (pas), bakır
- Kontamine kondensat kazana döndürülmemeli — ayrı bir kondensat kalite izleme sistemi önerilir

## Buhar Kapanları (Steam Traps)

Buhar kapanları, buharı geçirmeden kondensatı ve yoğuşmayan gazları uzaklaştıran otomatik vanalardır.

### Kapan Tipleri

| Tip | Alt Tip | Çalışma Prensibi | Avantaj | Dezavantaj |
|-----|---------|-------------------|---------|------------|
| Termodinamik | Disk tipi | Buhar/kondensat hız farkı | Kompakt, ucuz, dayanıklı | Gürültülü, kızgın buharda sorun |
| Termostatik | Bimetal, balmumu, basınçlı kapsül | Sıcaklık farkı | Hava tahliyesi iyi, kompakt | Kondensat birikimi (su baskını riski) |
| Mekanik | Şamandıra (float) | Yoğunluk farkı (yüzen şamandıra) | Sürekli drenaj, büyük kapasite | Büyük, dona hassas |
| Mekanik | Ters kova (inverted bucket) | Yoğunluk farkı (ters kova) | Dayanıklı, güvenilir | Su baskını riski, büyük boyut |

### Arıza Modları

| Arıza Modu | Sonuç | Enerji Etkisi |
|------------|-------|---------------|
| Açık kalma (stuck open) | Canlı buhar kaçağı | Yüksek enerji kaybı (€1000-5000/yıl/kapan) |
| Kapalı kalma (stuck closed) | Kondensat birikimi, su darbesi riski | Düşük ısı transferi, ekipman hasarı |
| Aralıklı kaçak | Kısmi buhar kaçağı | Orta enerji kaybı |

### Kapan Bakım ve Denetim

- **Arıza oranı:** Bakımsız sistemlerde %15-25, iyi bakımlı sistemlerde %5-10
- **Denetim yöntemi:** Ultrasonik test, sıcaklık ölçümü (kızılötesi), görsel inceleme
- **Denetim sıklığı:** Yılda 1-2 kez (en iyi uygulama: yılda 2 kez)
- **Tipik tasarruf:** Kapan denetim ve onarım programı ile %5-15 buhar tasarrufu

## Deaeratör (Deaerator)

### Çalışma Prensibi

Deaeratör, besleme suyundaki çözünmüş oksijen (O₂) ve karbondioksit (CO₂) gazlarını uzaklaştıran bir cihazdır. Bu gazlar kazan ve boru hatlarında korozyona neden olur.

- Henry Yasası: Suyun doyma sıcaklığında çözünmüş gaz miktarı sıfıra yaklaşır
- Buhar ile ısıtma yoluyla su doyma sıcaklığına getirilir ve gazlar serbest bırakılır

### Deaeratör Tipleri

| Tip | Çalışma Basıncı | Çıkış O₂ Seviyesi | Sıcaklık | Enerji Tüketimi |
|-----|-----------------|-------------------|----------|-----------------|
| Termal (spray-tray) | 0.2-0.5 bar(g) | <7 ppb | 105-110°C | Buhar: %5-8 besleme suyu debisi |
| Termal (spray-scrubber) | 0.3-1.0 bar(g) | <7 ppb | 105-115°C | Buhar: %5-8 besleme suyu debisi |
| Vakumlu (vacuum) | -0.3 ile -0.7 bar(g) | <20 ppb | 50-80°C | Vakum pompası + az buhar |

### Enerji Entegrasyonu

- Deaeratöre düşük basınçlı buhar (flash buhar, türbin çıkışı) beslenebilir
- Kondensat geri dönüşü ile deaeratör yükü azaltılır
- Proses atık ısısı ile ön ısıtma yapılabilir

## Flash Buhar Geri Kazanımı (Flash Steam Recovery)

Yüksek basınçlı kondensat düşük basınca açıldığında bir kısmı anında buharlaşır (flash buhar). Bu buhar geri kazanılabilir.

### Flash Buhar Hesaplama Formülü

```
x_flash = (h_f(P_yüksek) - h_f(P_düşük)) / h_fg(P_düşük)

Burada:
  x_flash     = Flash buhar oranı (kg buhar / kg kondensat)
  h_f(P_yüksek) = Yüksek basınçtaki doyma sıvı entalpisi (kJ/kg)
  h_f(P_düşük)  = Düşük basınçtaki doyma sıvı entalpisi (kJ/kg)
  h_fg(P_düşük) = Düşük basınçtaki buharlaşma gizli ısısı (kJ/kg)
```

### Örnek Hesaplama

10 bar kondensatı 1 bar'a flash edildiğinde:
- h_f(10 bar) = 763 kJ/kg
- h_f(1 bar) = 417 kJ/kg
- h_fg(1 bar) = 2258 kJ/kg
- x_flash = (763 - 417) / 2258 = 0.153 → **%15.3 flash buhar oluşur**

### Flash Buhar Geri Kazanım Uygulamaları

- Deaeratör besleme buharı olarak kullanım
- Düşük basınçlı ısıtma uygulamaları
- Besleme suyu ön ısıtma
- Tipik tasarruf: Geri kazanılan flash buhar debisi × h_fg(P_düşük)
- Yatırım: Flash tank + bağlantı borusu, geri ödeme: 3-12 ay

## Sistem Seviyesi Exergy Akışı

### Yakıttan Faydalı İşe Exergy Dağılımı

```
Yakıt Exergysi (100%)
  ├── Yanma tersinmezliği: %25-30 (en büyük exergy yıkımı noktası)
  ├── Isı transfer tersinmezliği (kazan): %5-10
  ├── Baca gazı kaybı: %5-12
  ├── Blowdown kaybı: %1-3
  ├── Dağıtım kayıpları: %3-8
  │     ├── İzolasyon eksikliği: %2-5
  │     ├── Buhar kaçakları: %1-3
  │     └── Kapan kayıpları: %1-3
  ├── PRV (basınç düşürme) exergy yıkımı: %3-8
  ├── Son kullanım tersinmezliği: %5-15
  └── Faydalı exergy çıkışı: %15-35
```

### Exergy Verimlilik Kıyaslaması

| Sistem Tipi | Tipik Exergy Verimi | En İyi Uygulama |
|-------------|--------------------|--------------------|
| Sadece buhar (ısıtma) | %15-25 | %25-35 |
| Kojenerasyon (CHP) | %30-45 | %40-55 |
| Trijenerasyon (CCHP) | %35-50 | %45-60 |

### Ana Exergy Yıkım Noktaları ve İyileştirme Fırsatları

| Kaynak | Exergy Yıkımı | İyileştirme Yöntemi |
|--------|---------------|---------------------|
| Yanma | %25-30 | Ön ısıtmalı yanma havası, reküperatör, oksijen zenginleştirme |
| Baca gazı | %5-12 | Ekonomizer, yoğuşmalı kazanlar, hava ön ısıtıcı |
| PRV | %3-8 | Back-pressure türbin ile değiştirme |
| Dağıtım | %3-8 | İzolasyon, kaçak onarımı, kapan bakımı |
| Son kullanım | %5-15 | Eşanjör optimizasyonu, kaskad ısı kullanımı |

## Ölçülmesi Gereken Parametreler

### Zorunlu Parametreler

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Yakıt tüketimi | m³/h veya kg/h | Tesise bağlı | Sayaç (doğalgaz) veya tartı |
| Buhar üretimi | t/h | 0.5-100+ | Buhar debimetresi (vortex, orifis) |
| Kazan çıkış basıncı | bar | 3-100 | Basınç transmitteri |
| Kazan çıkış sıcaklığı | °C | 150-540 | Termoeleman |
| Baca gazı sıcaklığı | °C | 120-300 | Termoeleman |
| Baca gazı O₂ | % | 2-6 | Oksijen analizörü |
| Besleme suyu sıcaklığı | °C | 60-110 | Termometre |
| Kondensat geri dönüş oranı | % | 0-95 | Debimetre veya tahmin |
| Kondensat sıcaklığı | °C | 60-95 | Termometre |

### Opsiyonel Parametreler (Detaylı Analiz)

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Blowdown oranı | % | 2-5 | Debimetre veya TDS ölçümü |
| TDS (toplam çözünmüş katı) | ppm | 500-3500 | TDS ölçer |
| Baca gazı CO | ppm | 0-200 | Baca gazı analizörü |
| Baca gazı CO₂ | % | 8-12 | Baca gazı analizörü |
| Buhar kalitesi (kuruluk) | % | 95-100 | Kalorimetre veya izokinetik örnekleme |
| Kullanım noktası basıncı | bar | 1-60 | Basınç transmitteri |
| Dağıtım basınç düşüşü | bar | 0.5-3.0 | Fark basınç ölçümü |
| Kapan sayısı ve durumu | - | - | Ultrasonik denetim |

### Nameplate Bilgileri

- Kazan markası ve modeli
- Nominal kapasite (t/h veya kW)
- Maksimum çalışma basıncı (bar)
- Yakıt tipi ve tüketimi
- Üretim yılı
- Kazan verim sınıfı

## Varsayılan Değerler (Ölçüm Yoksa)

| Parametre | Varsayılan | Not |
|-----------|------------|-----|
| Kazan verimi (doğalgaz) | %90 (LHV bazında) | Modern alev borulu kazan |
| Kazan verimi (fuel oil) | %87 (LHV bazında) | Ortalama |
| Baca gazı sıcaklığı | 200°C | Ekonomizer yoksa |
| Baca gazı O₂ | %3.5 | Orta bakım seviyesi |
| Besleme suyu sıcaklığı | 80°C | Deaeratör varsa: 105°C |
| Kondensat geri dönüş oranı | 60% | Endüstriyel ortalama |
| Kondensat sıcaklığı | 80°C | Atmosferik kondensat tankı |
| Blowdown oranı | %3 | Ortalama su kalitesi |
| Buhar kuruluk oranı | %97 | Doymuş buhar |
| Çalışma saati | 5000 saat/yıl | Tek vardiya + mevsimsel |
| İzolasyon durumu | %85 kaplama | Kısmen eksik izolasyon |
| Kapan arıza oranı | %15 | Orta bakım seviyesi |
| Doğalgaz alt ısıl değeri (LHV) | 34.5 MJ/m³ | Türkiye doğalgazı tipik |
| Doğalgaz exergy faktörü | 1.04 | Kimyasal exergy / LHV |
| Doğalgaz birim fiyatı | 0.35 €/m³ | Türkiye endüstriyel (değişken) |

## İlgili Dosyalar

- Ekipman: `equipment/boiler_firetube.md`, `equipment/boiler_watertube.md`, `equipment/boiler_hrsg.md`
- Ekipman: `equipment/steam_turbine.md`, `equipment/heat_exchanger.md`
- Benchmark: `benchmarks/boiler_benchmarks.md`, `benchmarks/steam_system_benchmarks.md`
- Formüller: `formulas/boiler_exergy.md`, `formulas/steam_properties.md`
- Çözümler: `solutions/boiler_economizer.md`, `solutions/boiler_blowdown_recovery.md`
- Çözümler: `solutions/steam_trap_maintenance.md`, `solutions/condensate_return.md`
- Çözümler: `solutions/flash_steam_recovery.md`, `solutions/steam_insulation.md`
- Çözümler: `solutions/prv_to_turbine.md`
- Metodoloji: `methodology/steam_audit.md`

## Referanslar

- Spirax Sarco, "The Steam and Condensate Loop" (Spirax Sarco Learning Centre)
- U.S. DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition
- ASME PTC 4 — "Fired Steam Generators: Performance Test Codes"
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing, 1995
- Bejan, A., Tsatsaronis, G., Moran, M., "Thermal Design and Optimization," Wiley, 1996
- TRD (Technische Regeln für Dampfkessel) — Alman Buhar Kazanı Teknik Kuralları
- EN 12953 — Shell Boilers (Alev Borulu Kazanlar)
- EN 12952 — Water-tube Boilers (Su Borulu Kazanlar)
- Rosen, M.A., Dincer, I., "Exergy Analysis of Waste Emissions," Int. J. Energy Research, 1999
- IAPWS-IF97 — Suyun Termodinamik Özellikleri (Buhar Tabloları)
