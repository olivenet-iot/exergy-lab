# Chiller Sistemi Enerji Denetimi Metodolojisi

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu metodoloji, AHRI 550/590 "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages" ve ASHRAE 90.1 "Energy Standard for Buildings" standartlarına dayalı olarak chiller sistemlerinin enerji verimliliği değerlendirmesi için 5 adımlı bir süreç tanımlar. Buhar sıkıştırmalı (santrifüj, vidalı, scroll, pistonlu) ve absorpsiyonlu chiller tipleri dahil olmak üzere tüm chiller tiplerini ve kapasite aralıklarını kapsar.

Denetim hem chiller ünitesi seviyesinde (kompresör, evaporatör, kondenser) hem de sistem seviyesinde (soğutma kuleleri, pompalar, boru hattı, kontrol stratejisi) analiz yapılmasını içerir. Exergy analizi ile termodinamik kayıp noktalarının belirlenmesi ve iyileştirme fırsatlarının niceliksel olarak değerlendirilmesi hedeflenir.

## Standart Referanslar

| Standart | Açıklama |
|----------|----------|
| AHRI 550/590 | Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages |
| AHRI 560 | Absorption Water-Chilling and Water-Heating Packages |
| ASHRAE 90.1-2019 | Energy Standard for Buildings Except Low-Rise Residential Buildings |
| ASHRAE Guideline 14 | Measurement of Energy, Demand, and Water Savings |
| ISO 50002:2014 | Energy audits — Requirements with guidance for use |
| ISO 50001:2018 | Energy management systems — Requirements with guidance for use |
| IPMVP | International Performance Measurement and Verification Protocol |
| Eurovent | Eurovent Certification Programme — Chillers |
| ARI 590 | Standard for Positive Displacement Compressor Chillers |

### Değerlendirme Seviyeleri

| Seviye | Açıklama | Kapsam |
|--------|----------|--------|
| Seviye 1 | Yürüyerek inceleme (walk-through) | Kalitatif, genel durum tespiti, fatura analizi |
| Seviye 2 | Detaylı değerlendirme | Kantitatif ölçümler, COP hesabı, approach analizi |
| Seviye 3 | Kapsamlı değerlendirme | Tam enstrümantasyon, exergy analizi, uzun süreli izleme, IPLV doğrulama |

### Sistem Sınırları

1. **Chiller ünitesi:** Kompresör, evaporatör, kondenser, genleşme valfi, kontrol sistemi
2. **Soğutma suyu (CHW) devresi:** CHW pompaları, boru hattı, vanalar, dengeleme
3. **Kondenser suyu (CW) devresi:** CW pompaları, soğutma kuleleri, boru hattı
4. **Kontrol sistemi:** BMS entegrasyonu, sıralama kontrolü, setpoint yönetimi
5. **Talep tarafı:** AHU/FCU soğutma bataryaları, proses soğutma noktaları
6. **Yardımcı sistemler:** Su arıtma, free cooling (varsa), ısı geri kazanım (varsa)

## Adım 1: Ön Hazırlık (Pre-Audit)

### 1.1 Toplanacak Bilgiler (En az 12 aylık)

| Kategori | Detay |
|----------|-------|
| Elektrik faturaları | Aylık chiller sistemi elektrik tüketimi (kWh), pik talep (kW), birim fiyat, toplam maliyet |
| BMS verileri | Chiller çalışma saatleri, CHW giriş/çıkış sıcaklıkları, CW sıcaklıkları, kompresör güç verileri |
| Ekipman envanteri | Chiller, soğutma kulesi, pompa nameplate bilgileri, teknik şartnameler |
| Sistem diyagramları | P&ID, tek hat şeması, boru yerleşim planı, kontrol şeması |
| Üretim/kullanım programı | Vardiya düzeni, mevsimsel değişimler, bina kullanım profili |
| Bakım kayıtları | Servis geçmişi, soğutucu akışkan ekleme/değişim, kompresör bakımı, tüp temizliği |
| Su arıtma kayıtları | Kondenser suyu kimyasal analizi, biyosit dozajlama, blöf kayıtları |
| Önceki denetim raporları | Varsa önceki verimlilik testleri ve denetimler |
| Soğutucu akışkan kayıtları | Akışkan tipi, şarj miktarı, kaçak geçmişi, ekleme miktarları |
| İklim verileri | Dış hava sıcaklığı, nem, yaş termometre sıcaklığı (meteoroloji istasyonu veya BMS) |
| Proses soğutma verileri | Proses soğutma gereksinimleri, sıcaklık seviyeleri, çalışma süreleri |

### 1.2 Ön Görüşme Soruları (Tesis Yönetimine)

1. Kaç chiller kurulu? Tipleri (santrifüj, vidalı, scroll, absorpsiyon) ve kapasiteleri (kW veya ton)?
2. Chiller'ların yaşı ve üreticileri? Hangi soğutucu akışkanları kullanılıyor (R-134a, R-410A, R-1234ze vb.)?
3. Kompresör tipleri ve kontrol yöntemleri (sabit hız, VSD, IGV, slide valve)?
4. Tipik soğutma suyu (CHW) gidiş/dönüş sıcaklıkları? Setpoint değişikliği yapılıyor mu?
5. Soğutma kuleleri: tip (açık/kapalı devre), kapasite, fan kontrol yöntemi?
6. Pompa düzeni: primer/sekonder mu, değişken debi mi, VSD var mı?
7. Ortalama ve pik soğutma talebi? Mevsimsel değişim profili?
8. Free cooling (serbest soğutma) sistemi mevcut mu? Kullanılıyor mu?
9. Isı geri kazanım sistemi var mı (kondenser ısısı geri kazanımı)?
10. BMS/otomasyon sistemi nasıl, chiller sıralama stratejisi nedir?
11. Bilinen sorunlar: vibrasyon, gürültü, kapasite düşüşü, yüksek enerji tüketimi?
12. Son tüp temizliği (evaporatör/kondenser) ne zaman yapıldı?
13. Soğutucu akışkan kaçağı geçmişi var mı? Son ekleme ne zaman?
14. Kondenser suyu arıtma rejimi: kimyasal dozajlama, blöf, Legionella kontrolü?
15. Genişleme veya modernizasyon planları var mı? Chiller değişimi düşünülüyor mu?

### 1.3 Denetim Ekipman Listesi

| Ekipman | Örnek Model | Amacı | Yaklaşık Maliyet |
|---------|-------------|-------|-----------------|
| Güç analizörü | Fluke 435-II, Hioki PW3198 | Kompresör, pompa, fan güç profilleme | €4,000-8,000 |
| Sıcaklık veri kaydedici | Onset HOBO U12-015, Testo 176 T4 | CHW, CW sıcaklık kaydı (en az 4 kanal) | €200-800 |
| Yüzey sıcaklık probu | Testo pipe clamp, Fluke 80PK-8 | Boru yüzey sıcaklık ölçümü | €50-200 |
| Ultrasonik debimetre | Flexim FLUXUS F601, Katronic KATflow 200 | CHW ve CW debi ölçümü (clamp-on) | €3,000-12,000 |
| Dijital manometre | Keller LEO 2, Testo 549 | Soğutucu akışkan basınç ölçümü | €200-500 |
| Termal kamera | FLIR E96, Testo 890 | İzolasyon kaybı, sıcak/soğuk nokta tespiti | €5,000-20,000 |
| IR termometre | Fluke 62 MAX+ | Hızlı yüzey sıcaklığı ölçümü | €50-150 |
| Yaş termometre / psikrometre | Kestrel 5400, Testo 480 | Yaş termometre sıcaklığı (soğutma kulesi) | €300-1,000 |
| Ortam sıcaklık/nem kaydedici | Onset HOBO MX2301 | Dış hava koşulları kaydı | €100-300 |
| Veri kaydedici (çok kanallı) | Yokogawa GP20, Hioki LR8450 | Uzun süreli çoklu parametre kaydı | €1,500-5,000 |
| Su kalitesi test kiti | Hach DR900, Palintest | pH, iletkenlik, sertlik, klor (kondenser suyu) | €500-2,000 |
| Kamera | Akıllı telefon/dijital | Durum belgeleme, nameplate fotoğrafı | — |

## Adım 2: Saha Çalışması (Field Work)

### 2.1 Sistem Envanteri

#### Her Chiller İçin Kaydedilecekler

| Parametre | Açıklama |
|-----------|----------|
| Üretici | Carrier, Trane, York, Daikin, Mitsubishi, vb. |
| Model | Tam model numarası |
| Seri numarası | Nameplate'den |
| Nominal soğutma kapasitesi | kW veya ton |
| Kompresör tipi | Santrifüj, vidalı, scroll, pistonlu |
| Kompresör sayısı | Tek/çift devre |
| Soğutucu akışkan | R-134a, R-410A, R-1234ze(E), R-513A, R-717, LiBr-Su vb. |
| Soğutucu akışkan şarj miktarı | kg |
| Üretim yılı | Nameplate veya seri numarasından |
| Kontrol tipi | Sabit hız, VSD, IGV, slide valve, on/off |
| Nominal COP / kW/ton | Nameplate veya katalog değeri |
| IPLV/NPLV | Katalog değeri |
| Nominal güç tüketimi | kW (kompresör) |
| Çalışma saati | Sayaçtan veya BMS'den |
| Tasarım CHW sıcaklıkları | Giriş/çıkış (°C) |
| Tasarım CW sıcaklıkları | Giriş/çıkış (°C) |

#### Her Soğutma Kulesi İçin

| Parametre | Açıklama |
|-----------|----------|
| Üretici ve model | Nameplate bilgisi |
| Kule tipi | Açık devre (cross-flow/counter-flow), kapalı devre |
| Nominal kapasite | kW ısı atma kapasitesi |
| Fan tipi ve sayısı | Aksiyel/santrifüj, tek/çift fan |
| Fan motor gücü | kW |
| Fan kontrol tipi | Sabit hız, çift hız, VSD |
| Fill (dolgu) tipi | Film/splash, malzeme |
| Tasarım yaş termometre sıcaklığı | °C |
| Tasarım approach | °C |
| Su dağıtım sistemi | Nozul/gravity |

#### Her Pompa İçin

| Pompa Tipi | Kaydedilecekler |
|------------|----------------|
| CHW pompaları (primer) | Üretici, model, güç (kW), debi (m³/h), basma yüksekliği (m), VSD var/yok |
| CHW pompaları (sekonder) | Üretici, model, güç (kW), debi (m³/h), basma yüksekliği (m), VSD var/yok |
| CW pompaları | Üretici, model, güç (kW), debi (m³/h), basma yüksekliği (m), VSD var/yok |
| Yedek pompalar | Aynı bilgiler |

### 2.2 Ölçümler

#### Elektrik Ölçümleri

Aşağıdaki tüm ekipmanda eşzamanlı güç ölçümü yapılmalıdır:

| Ölçüm Noktası | Parametre | Birim |
|---------------|-----------|-------|
| Chiller kompresör(ler) | Aktif güç, akım, gerilim, güç faktörü | kW, A, V, cos(φ) |
| CHW pompaları (primer + sekonder) | Aktif güç | kW |
| CW pompaları | Aktif güç | kW |
| Soğutma kulesi fanları | Aktif güç | kW |

**Ölçüm süresi:** Minimum 24 saat (tam bir günlük çevrim), ideal olarak 1 hafta (hafta içi + hafta sonu)

**Kayıt aralığı:** 1 dakika (güç analizörü), tüm ekipmanda eşzamanlı kayıt

**Dikkat:** Birden fazla chiller çalışıyorsa her birinin güç tüketimi ayrı ayrı kaydedilmelidir.

#### Sıcaklık Ölçümleri

| Ölçüm Noktası | Parametre | Yöntem |
|---------------|-----------|--------|
| CHW gidiş (supply) | T_chw_supply | Yüzey probu veya immersion |
| CHW dönüş (return) | T_chw_return | Yüzey probu veya immersion |
| CW giriş (kondensere) | T_cw_in (entering condenser) | Yüzey probu |
| CW çıkış (kondenserden) | T_cw_out (leaving condenser) | Yüzey probu |
| Evaporatör soğutucu akışkan sıcaklığı | T_evap_ref | Basınç-sıcaklık tablosu veya sensör |
| Kondenser soğutucu akışkan sıcaklığı | T_cond_ref | Basınç-sıcaklık tablosu veya sensör |
| Dış hava sıcaklığı | T_ambient | Ortam kaydedici |
| Yaş termometre sıcaklığı | T_wb | Psikrometre (soğutma kulesi yakınında) |
| Soğutma kulesi çıkış suyu | T_tower_out | Yüzey probu (havuz veya çıkış hattı) |
| Hava soğutmalı chiller hava girişi | T_air_in | Ortam kaydedici (kondenser fanı önü) |

**Kayıt aralığı:** 1 dakika, tüm noktalar eşzamanlı, minimum 24 saat

#### Basınç Ölçümleri

| Ölçüm Noktası | Parametre | Birim |
|---------------|-----------|-------|
| Evaporatör soğutucu akışkan basıncı | P_evap | bar |
| Kondenser soğutucu akışkan basıncı | P_cond | bar |
| Kompresör yağ basıncı | P_oil | bar |
| CHW diferansiyel basınç | ΔP_chw | bar (veya kPa) |
| CW diferansiyel basınç | ΔP_cw | bar (veya kPa) |

**Not:** Soğutucu akışkan basınçları, doyma basınç-sıcaklık tablosu ile birlikte değerlendirilerek evaporatör ve kondenser sıcaklıkları doğrudan hesaplanabilir.

#### Debi Ölçümleri

| Ölçüm Noktası | Parametre | Birim | Yöntem |
|---------------|-----------|-------|--------|
| Soğutma suyu (CHW) debisi | V̇_chw | m³/h veya l/s | Ultrasonik clamp-on veya mevcut debimetre |
| Kondenser suyu (CW) debisi | V̇_cw | m³/h veya l/s | Ultrasonik clamp-on veya mevcut debimetre |

**Dikkat:** Debi ölçümü soğutma kapasitesi hesabının temelidir; kalibrasyonu doğrulanmış debimetre kullanılmalıdır.

### 2.3 Görsel İnceleme

#### Chiller Dairesi Kontrol Listesi

- [ ] Chiller dairesi havalandırması yeterli mi (soğutucu akışkan kaçağı riski)?
- [ ] Soğutucu akışkan kaçak dedektörü mevcut ve çalışır durumda mı?
- [ ] Chiller ünitesinde anormal vibrasyon veya gürültü var mı?
- [ ] Kompresör yağ seviyesi göstergesi normal aralıkta mı?
- [ ] Evaporatör ve kondenser yüzeylerinde korozyon veya hasar var mı?
- [ ] Kontrol panelinde aktif alarm veya uyarı var mı?
- [ ] Soğutucu akışkan şarj seviyesi (sight glass) normal mi?
- [ ] Boru bağlantıları ve flanşlarda sızıntı belirtisi var mı?
- [ ] Chiller elektrik bağlantıları sıkı ve güvenli mi?
- [ ] Yağ filtresi, soğutucu akışkan filtresi bakım tarihleri güncel mi?

#### İzolasyon ve Boru Durumu Kontrol Listesi

- [ ] CHW boru izolasyonu sağlam ve sürekli mi (terleme yok mu)?
- [ ] CW boruları uygun izolasyona sahip mi (dış ortam geçişleri)?
- [ ] Vana, flanş ve fittinglerin izolasyonu eksiksiz mi?
- [ ] Buhar bariyeri (vapor barrier) sağlam mı (soğuk hatlarda)?
- [ ] İzolasyonda nem hasarı, küf veya çökelme var mı?
- [ ] Boru destekleri ve askıları sağlam mı?
- [ ] Genleşme kompansatörleri düzgün çalışıyor mu?

#### Soğutma Kulesi Kontrol Listesi

- [ ] Kule dolgu (fill) malzemesi temiz ve hasarsız mı?
- [ ] Su dağıtım nozulları tıkanık veya hasarlı mı?
- [ ] Fan kanatları temiz ve dengeli mi (vibrasyon kontrolü)?
- [ ] Kule havuzunda tortu, yosun veya biyolojik büyüme var mı?
- [ ] Drift eliminator (damlacık tutucu) yerinde ve temiz mi?
- [ ] Blöf sistemi çalışıyor mu, iletkenlik kontrol altında mı?
- [ ] Kule yapısında korozyon veya yapısal hasar var mı?
- [ ] Hava giriş panjurları/ızgaraları temiz mi?
- [ ] Havuz su seviyesi kontrol vanası düzgün çalışıyor mu?

#### Su Arıtma Kontrol Listesi

- [ ] Kondenser suyu kimyasal dozajlama sistemi aktif mi?
- [ ] pH, iletkenlik, sertlik değerleri hedef aralıkta mı?
- [ ] Biyosit dozajlama ve Legionella kontrolü yapılıyor mu?
- [ ] Korozyon ve keçeleşme (scaling) inhibitörleri dozajlanıyor mu?
- [ ] Otomatik blöf sistemi çalışıyor mu?
- [ ] Su analiz kayıtları düzenli tutuluyor mu?

## Adım 3: Veri Analizi

### 3.1 Performans Hesaplama

#### Soğutma Kapasitesi (Evaporatör Yükü)

```
Q_evap = m_chw × Cp × ΔT_chw

Burada:
  Q_evap = Soğutma kapasitesi (kW)
  m_chw  = Soğutma suyu kütle debisi (kg/s)
  Cp     = Suyun özgül ısısı (4.186 kJ/kg·K)
  ΔT_chw = CHW dönüş sıcaklığı - CHW gidiş sıcaklığı (°C)
```

Hacimsel debi ile:
```
Q_evap = V̇_chw × ρ × Cp × ΔT_chw / 1000

Burada:
  V̇_chw = Hacimsel debi (l/s)
  ρ      = Suyun yoğunluğu (~998 kg/m³)
```

Ton cinsinden:
```
Q_evap (ton) = Q_evap (kW) / 3.517
```

#### COP (Performans Katsayısı)

```
COP = Q_evap / W_comp

Burada:
  Q_evap = Soğutma kapasitesi (kW)
  W_comp = Kompresör elektrik gücü (kW)
```

#### kW/ton

```
kW/ton = W_comp / Q_evap_ton = 3.517 / COP

Burada:
  Q_evap_ton = Soğutma kapasitesi (ton)
```

#### Sistem COP

```
COP_system = Q_evap / (W_comp + W_chw_pump + W_cw_pump + W_tower_fan)

Burada:
  W_chw_pump  = CHW pompa gücü (kW)
  W_cw_pump   = CW pompa gücü (kW)
  W_tower_fan = Soğutma kulesi fan gücü (kW)
```

### 3.2 Approach Temperature Analizi

#### Kondenser Yaklaşım Sıcaklığı (Su Soğutmalı)

```
Approach_cond = T_cond_ref - T_cw_in

Burada:
  T_cond_ref = Kondenser soğutucu akışkan yoğuşma sıcaklığı (°C)
  T_cw_in    = Kondenser suyu giriş sıcaklığı (°C)

Hedef: <2.5°C (yeni/temiz), >4.0°C ise acil temizlik gerekli
```

#### Kondenser Yaklaşım Sıcaklığı (Hava Soğutmalı)

```
Approach_cond = T_cond_ref - T_ambient

Hedef: <15°C (iyi), >20°C ise bakım gerekli
```

#### Evaporatör Yaklaşım Sıcaklığı

```
Approach_evap = T_chw_out - T_evap_ref

Burada:
  T_chw_out  = Soğutma suyu çıkış sıcaklığı (°C)
  T_evap_ref = Evaporatör soğutucu akışkan buharlaşma sıcaklığı (°C)

Hedef: <2.5°C (iyi), >4.0°C ise fouling başlamış
```

#### Soğutma Kulesi Yaklaşım Sıcaklığı

```
Tower_approach = T_cw_out - T_wb

Burada:
  T_cw_out = Soğutma kulesi çıkış suyu sıcaklığı (°C)
  T_wb     = Ortam yaş termometre sıcaklığı (°C)

Hedef: <5°C (iyi), >8°C ise kule bakımı/revizyonu gerekli
```

### 3.3 Kısmi Yük Analizi

#### Yük Profili Çıkarma

BMS verilerinden veya ölçüm kampanyasından:
1. Saatlik soğutma yükü hesapla (Q_evap)
2. Yükü nominal kapasiteye göre yüzdelik olarak ifade et
3. Yük dağılım histogramı oluştur (%0-25, %25-50, %50-75, %75-100)
4. Ağırlıklı ortalama yük faktörünü belirle

#### Kısmi Yük COP

Her yük seviyesinde ölçülen COP değerlerini kaydet:

| Yük (%) | Q_evap (kW) | W_comp (kW) | COP | kW/ton |
|---------|-------------|-------------|-----|--------|
| 100% | | | | |
| 75% | | | | |
| 50% | | | | |
| 25% | | | | |

#### IPLV Tahmini

```
IPLV = 0.01 × COP_100% + 0.42 × COP_75% + 0.45 × COP_50% + 0.12 × COP_25%

Burada:
  COP_100% = Tam yük COP'u
  COP_75%  = %75 yükte COP
  COP_50%  = %50 yükte COP
  COP_25%  = %25 yükte COP
```

Hesaplanan IPLV değerini ASHRAE 90.1 minimum gereksinimleri ve katalog IPLV değeri ile karşılaştır.

### 3.4 Exergy Analizi

ExergyLab engine kullanarak:

#### 1. Exergy Girdisi

```
Ex_input = W_comp + W_chw_pump + W_cw_pump + W_tower_fan   [kW]

Not: Elektrik enerjisi saf exergy'dir (exergy/enerji oranı = 1.0)
```

#### 2. Soğutma Exergy Çıkışı

```
Ex_cool = Q_evap × |1 - T₀/T_cool|   [kW]

Burada:
  T₀     = Referans sıcaklık = 298.15 K (25°C)
  T_cool = Soğutma suyu ortalama sıcaklığı = (T_chw_in + T_chw_out) / 2   [K]
```

#### 3. Toplam Exergy Yıkımı

```
Ex_destroyed = Ex_input - Ex_cool   [kW]
```

#### 4. Bileşen Bazlı Exergy Yıkım Dağılımı

| Bileşen | Exergy Yıkım Payı | Açıklama |
|---------|-------------------|----------|
| Kompresör | %35-45 | İzentropik verimlilik kayıpları |
| Kondenser | %15-25 | Isı transferi sıcaklık farkı |
| Evaporatör | %10-20 | Isı transferi sıcaklık farkı |
| Genleşme valfi | %15-25 | Throttling (kısılma) kaybı |
| Pompalar | %5-10 | Hidrolik ve motor kayıpları |
| Soğutma kulesi | %3-8 | Isı ve kütle transferi kayıpları |
| Boru ve izolasyon | %2-5 | Sürtünme ve ısı kazancı |

#### 5. Chiller Exergy Verimi

```
η_ex_chiller = Ex_cool / W_comp × 100%   [%]

Veya Carnot bazlı:
η_ex_chiller = COP / COP_Carnot × 100%

COP_Carnot = T_evap / (T_cond - T_evap)   [K cinsinden]
```

#### 6. Sistem Exergy Verimi

```
η_ex_system = Ex_cool / Ex_input × 100%   [%]

Tipik değerler:
  Düşük:    <%15 (eski, bakımsız, sabit hız)
  Ortalama: %15-25 (standart sistem)
  İyi:      %25-35 (VSD, optimize kontrol)
  Mükemmel: >%35 (tam optimize, free cooling dahil)
```

### 3.5 Benchmark Karşılaştırması

Hesaplanan değerleri `benchmarks/chiller_benchmarks.md` dosyasındaki referans değerlerle karşılaştır:

| Parametre | Ölçülen Değer | Benchmark (İyi) | Sapma | Durum |
|-----------|---------------|-----------------|-------|-------|
| COP (tam yük) | | Bkz. benchmark | | |
| kW/ton (tam yük) | | Bkz. benchmark | | |
| IPLV | | ASHRAE 90.1 min. | | |
| Sistem kW/ton | | <0.90 | | |
| Kondenser approach | | <2.5°C | | |
| Evaporatör approach | | <2.5°C | | |
| Kule approach | | <5°C | | |
| Exergy verimi (chiller) | | >30% | | |
| Exergy verimi (sistem) | | >25% | | |

## Adım 4: Raporlama

### Rapor Yapısı

#### 1. Yönetici Özeti (1 sayfa)

- Sistem genel bakışı (chiller sayısı, toplam kapasite kW/ton, yıllık enerji maliyeti)
- Temel bulgular (3-5 madde)
- Toplam tasarruf potansiyeli (kWh/yıl ve €/yıl)
- Öncelikli öneriler ve ROI
- Uygulama zaman çizelgesi özeti

#### 2. Sistem Tanımı (2-4 sayfa)

- Ekipman envanter tablosu (chiller'lar, soğutma kuleleri, pompalar)
- Sistem şeması/yerleşimi (primer-sekonder, değişken primer vb.)
- Soğutma suyu dağıtım şeması (tüketiciler, sıcaklık seviyeleri)
- Çalışma koşulları (sıcaklık setpointleri, vardiya, mevsim)
- Kontrol stratejisi açıklaması (sıralama, setpoint reset, VSD)
- Su arıtma sistemi açıklaması

#### 3. Mevcut Durum Değerlendirmesi (3-5 sayfa)

- Enerji tüketimi analizi (kWh miktarı, maliyet, trend)
- Chiller COP hesapları (tam yük ve kısmi yük)
- Approach temperature analizi (kondenser, evaporatör, kule)
- Yük profili analizi ve IPLV tahmini
- Sistem seviyesi kW/ton
- Exergy verimi ve exergy yıkım dağılımı (Sankey diyagramı)
- Benchmark karşılaştırması

#### 4. Bulgular ve Analiz (5-10 sayfa)

Her bulgu için:
- Açıklama ve ölçüm verileri
- Fotoğraflar, termal görüntüler, grafik/trend verileri
- Mevcut durumun niceliksel ifadesi
- Temel neden analizi
- Enerji etkisi (kWh/yıl), maliyet etkisi (€/yıl), CO₂ etkisi (ton/yıl)

#### 5. İyileştirme Önerileri (3-5 sayfa)

Öncelik matrisi formatında:

| # | Öneri | Yatırım | Yıllık Tasarruf | Geri Ödeme | Öncelik |
|---|-------|---------|----------------|------------|---------|
| 1 | Kondenser/evaporatör tüp temizliği | €3,000 | €12,000 | 0.3 yıl | YÜKSEK |
| 2 | CHW setpoint reset kontrolü | €2,000 | €8,000 | 0.3 yıl | YÜKSEK |
| 3 | Soğutma kulesi bakımı ve fill değişimi | €10,000 | €15,000 | 0.7 yıl | YÜKSEK |
| 4 | CW pompa VSD retrofit | €12,000 | €10,000 | 1.2 yıl | ORTA |
| 5 | Chiller sıralama optimizasyonu | €5,000 | €18,000 | 0.3 yıl | YÜKSEK |
| 6 | Free cooling sistemi eklenmesi | €30,000 | €16,000 | 1.9 yıl | ORTA |
| 7 | Kondenser suyu sıcaklık reset | €1,500 | €6,000 | 0.3 yıl | YÜKSEK |
| 8 | Chiller değişimi (eski ünite) | €150,000 | €35,000 | 4.3 yıl | DÜŞÜK |

Her öneri için:
- Teknik açıklama ve uygulama detayları
- Yatırım maliyet tahmini (ekipman + montaj + komisyon)
- Yıllık tasarruf hesabı (varsayımlarla birlikte)
- Basit geri ödeme süresi
- CO₂ azaltma (ton/yıl): kWh tasarruf × emisyon faktörü (0.4-0.5 kg CO₂/kWh)
- Uygulama karmaşıklığı (düşük/orta/yüksek)
- Risk ve dikkat edilecek hususlar

#### 6. ROI Hesapları (2-3 sayfa)

- Her öneri için detaylı hesaplama
- Anahtar varsayımlara duyarlılık analizi (elektrik fiyatı, çalışma saati, soğutma yükü)
- Birden fazla önlem uygulandığında kombine tasarruf (interaksiyon etkileri dikkate alınarak)
- Büyük yatırımlar için net bugünkü değer (NPV) ve iç verim oranı (IRR)

#### 7. Uygulama Yol Haritası (1-2 sayfa)

- **Faz 1:** Hızlı kazanımlar (0-3 ay) — tüp temizliği, setpoint optimizasyonu, sıralama düzeltme, kule bakımı
- **Faz 2:** Orta vadeli (3-12 ay) — VSD retrofit, free cooling, kontrol iyileştirme, su arıtma optimizasyonu
- **Faz 3:** Uzun vadeli (1-3 yıl) — chiller değişimi, sistem yeniden tasarımı, ısı geri kazanım sistemi
- Tasarruf doğrulama izleme planı (bkz. Adım 5)

#### 8. Ekler

- A: Ham ölçüm verileri (güç profilleri, sıcaklık logları, debi verileri)
- B: Ekipman nameplate fotoğrafları
- C: Termal kamera görüntüleri
- D: Approach temperature trend grafikleri
- E: Hesaplama detayları (COP, exergy, IPLV)
- F: Ekipman teknik şartnameleri (önerilmiş ise)

### Öncelik Matrisi

| Yatırım | Düşük Tasarruf | Yüksek Tasarruf |
|---------|---------------|-----------------|
| Düşük yatırım | CHW izolasyon tamamlama, vana bakımı | Setpoint reset, sıralama optimizasyonu, tüp temizliği |
| Yüksek yatırım | Kondenser suyu side-stream filtrasyon | VSD retrofit, free cooling, chiller değişimi |

### Tipik Bulgular ve Tasarruf Aralıkları

| Kategori | Tipik Bulgu | Tipik Tasarruf |
|----------|------------|---------------|
| Kondenser/evaporatör fouling | Approach >4°C, COP düşük | %5-15 |
| Soğutma kulesi performans düşüklüğü | Kule approach >8°C | %3-10 |
| CHW setpoint çok düşük | CHW gidiş <6°C (gerekmediği halde) | %3-5 |
| Sabit hız pompalar (aşırı debi) | VSD yok, kısma vanası kullanımı | %20-50 (pompa) |
| Kötü chiller sıralama stratejisi | Verimsiz chiller önce devrede | %5-15 |
| Free cooling kullanılmıyor | Kış aylarında chiller çalışması | %10-30 (mevsimsel) |
| Kondenser suyu sıcaklık reset yok | Sabit CW setpoint yaz/kış | %5-10 |
| Soğutucu akışkan eksik şarj | Kaçak sonrası düşük şarj | %5-15 |
| Eski/verimsiz chiller | Yaş >15 yıl, COP düşüş >%20 | %15-30 (değişim) |
| Non-condensable gaz varlığı | Yüksek head pressure | %5-15 |

## Adım 5: Doğrulama ve Takip

### Uygulama Sonrası Doğrulama

- Öneri uygulandıktan sonra 2-4 haftalık ölçüm kampanyası (aynı parametreler)
- Önceki/sonraki COP ve kW/ton karşılaştırması (aynı yük ve ortam koşullarında)
- IPMVP yöntemiyle doğrulama:
  - **Option A:** Kısmi ölçüm (ana parametrelerde örnekleme)
  - **Option B:** Tüm parametrelerde sürekli ölçüm (tercih edilen)
  - **Option C:** Tüm tesis fatura analizi (büyük değişiklikler için)
- Enerji tüketimi trend analizi (dış hava sıcaklığı normalizasyonu ile)
- ASHRAE Guideline 14 uyumlu M&V planı

### Sürekli İzleme KPI'ları

| KPI | Formül | Hedef | Ölçüm Sıklığı |
|-----|--------|-------|---------------|
| Chiller COP | COP = Q_evap / W_comp | Bkz. benchmark | Haftalık (veya sürekli BMS) |
| Chiller kW/ton | kW/ton = W_comp / Q_evap_ton | <0.65 (su soğ.) | Haftalık |
| Sistem kW/ton | kW/ton_sys = (W_comp + W_pump + W_fan) / Q_evap_ton | <0.90 | Aylık |
| Kondenser approach | T_cond_ref - T_cw_in | <2.5°C | Haftalık |
| Evaporatör approach | T_chw_out - T_evap_ref | <2.5°C | Haftalık |
| Kule approach | T_cw_out - T_wb | <5°C | Haftalık |
| IPLV (hesaplanan) | AHRI 550/590 formülü | ≥Katalog IPLV | 6 ayda bir |
| CHW ΔT | T_chw_return - T_chw_supply | ≥Tasarım ΔT | Sürekli |
| Yük faktörü | Q_actual / Q_nominal × 100% | — | Aylık |
| Sistem exergy verimi | Ex_cool / Ex_input × 100% | >25% | Yıllık (denetimde) |
| Soğutucu akışkan şarj durumu | Seviye kontrolü veya subcooling | Nominal ±%5 | 3 ayda bir |
| Kondenser suyu kalitesi | pH, iletkenlik, sertlik | Hedef aralık | Haftalık |

### İzleme ve Trend Analizi

1. Aylık enerji raporlamasında chiller sistemi kW/ton ve COP takibi
2. Approach temperature trendleri ile fouling tespiti (temizlik zamanlama)
3. Yük profili analizi ile sıralama stratejisi doğrulama
4. Dış hava sıcaklığına göre normalize edilmiş verim takibi
5. Yıllık kapsamlı denetim tekrarı ile uzun vadeli performans izleme

## Audit Kontrol Listesi

### Ön Hazırlık

- [ ] En az 12 aylık elektrik faturaları toplandı
- [ ] BMS verileri (sıcaklık, güç, çalışma saati) talep edildi
- [ ] Ekipman nameplate bilgileri ve kataloglar temin edildi
- [ ] P&ID ve sistem diyagramları incelendi
- [ ] Bakım kayıtları ve soğutucu akışkan logları alındı
- [ ] Tesis yönetimi ile ön görüşme yapıldı
- [ ] Denetim ekipmanları kalibrasyonu kontrol edildi

### Saha Çalışması

- [ ] Tüm chiller'ların envanteri çıkarıldı
- [ ] Soğutma kuleleri ve pompaların envanteri çıkarıldı
- [ ] Güç ölçümleri başlatıldı (min. 24 saat, ideal 1 hafta)
- [ ] Sıcaklık kaydedicileri yerleştirildi (CHW, CW, ortam, yaş termometre)
- [ ] Debi ölçümleri yapıldı (CHW ve CW)
- [ ] Soğutucu akışkan basınçları kaydedildi (evaporatör, kondenser)
- [ ] Chiller dairesi görsel incelemesi tamamlandı
- [ ] Soğutma kulesi görsel incelemesi tamamlandı
- [ ] İzolasyon durumu değerlendirildi (termal kamera)
- [ ] Kondenser suyu kalitesi ölçüldü
- [ ] Operatörler ile görüşme yapıldı

### Analiz

- [ ] COP ve kW/ton hesaplandı (tam yük ve kısmi yük)
- [ ] Approach temperature analizi yapıldı
- [ ] Yük profili çıkarıldı ve IPLV tahmin edildi
- [ ] Exergy analizi tamamlandı
- [ ] Benchmark karşılaştırması yapıldı
- [ ] İyileştirme fırsatları belirlendi
- [ ] Tasarruf ve yatırım hesapları tamamlandı

### Raporlama

- [ ] Yönetici özeti hazırlandı
- [ ] Sistem tanımı yazıldı
- [ ] Mevcut durum değerlendirmesi tamamlandı
- [ ] Bulgular ve öneriler dokümante edildi
- [ ] ROI hesapları yapıldı
- [ ] Uygulama yol haritası oluşturuldu
- [ ] Rapor gözden geçirildi ve onaylandı

## İlgili Dosyalar

- Chiller exergy formülleri: `formulas/chiller_exergy.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Buhar sıkıştırmalı chiller: `equipment/chiller_vapor_compression.md`
- Absorpsiyonlu chiller: `equipment/chiller_absorption.md`
- Soğutucu akışkanlar: `equipment/chiller_refrigerants.md`
- Soğutma kulesi: `equipment/cooling_tower.md`
- Chiller VSD çözümü: `solutions/chiller_vsd.md`
- Chiller setpoint reset: `solutions/chiller_setpoint_reset.md`
- Chiller free cooling: `solutions/chiller_free_cooling.md`
- Chiller kondenser optimizasyon: `solutions/chiller_condenser_optimization.md`
- Pompa ekipman dosyaları: `equipment/pump_centrifugal.md`
- Pompa VSD çözümü: `solutions/pump_vsd.md`

## Referanslar

- AHRI Standard 550/590, "Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages Using the Vapor Compression Cycle"
- AHRI Standard 560, "Absorption Water-Chilling and Water-Heating Packages"
- ASHRAE Standard 90.1-2019, "Energy Standard for Buildings Except Low-Rise Residential Buildings"
- ASHRAE Guideline 14-2014, "Measurement of Energy, Demand, and Water Savings"
- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- IPMVP, "International Performance Measurement and Verification Protocol," Volume I
- Eurovent Certification Programme, "Liquid Chilling Packages and Heat Pumps"
- ASHRAE Handbook — HVAC Systems and Equipment (2020), Chapter 42: Centrifugal Chillers
- Cengel & Boles, "Thermodynamics: An Engineering Approach" — Refrigeration Cycles
- Dincer & Rosen, "Exergy: Energy, Environment and Sustainable Development"
- Carrier, "Handbook of Air Conditioning System Design"
- US DOE, "Federal Energy Management Program — Chiller Efficiency"
- Lawrence Berkeley National Laboratory, "Chiller Plant Optimization"
