---
title: "İzleme ve Hedefleme Sistemi (Monitoring and Targeting — M&T)"
category: factory
equipment_type: factory
keywords: [M&T, izleme, hedefleme, monitoring, targeting, ölçüm hiyerarşisi, alt ölçüm, SCADA, dashboard, enerji yönetim yazılımı]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/enpi_guide.md, factory/energy_management/cusum_analysis.md, factory/energy_management/baseline_enpi.md, factory/data_collection.md, factory/performance_indicators.md]
use_when: ["M&T sistemi kurulacağında", "Ölçüm hiyerarşisi planlanacağında", "Enerji dashboard tasarlanacağında", "SCADA entegrasyonu sorgulandığında"]
priority: medium
last_updated: 2026-02-01
---

# İzleme ve Hedefleme Sistemi (Monitoring and Targeting — M&T)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış (Overview)

### 1.1 M&T Tanımı

İzleme ve Hedefleme (M&T — Monitoring and Targeting), enerji tüketim verilerinin sistematik olarak toplanması, analiz edilmesi, hedeflerle karşılaştırılması ve sapmalara müdahale edilmesi sürecidir. Carbon Trust (eski ETSU — İngiltere Enerji Teknoloji Destek Birimi) tarafından 1980'lerden itibaren geliştirilen M&T yaklaşımı, enerji yönetiminin temel taşıdır. M&T, "ölçemediğinizi yönetemezsiniz" ilkesinin pratik uygulamasıdır.

### 1.2 ISO 50001 Bağlantısı

```
ISO 50001:2018 — M&T ile ilgili maddeler:

Madde 6.3 — Enerji inceleme (Energy review):
├── Enerji kullanımını ve tüketimini analiz etme
├── Önemli enerji kullanımlarını (SEU) belirleme
└── İlgili değişkenleri tanımlama

Madde 6.5 — EnPI ve EnB:
├── Enerji performansını izlemek için göstergeler
├── Baseline ile karşılaştırma
└── Normalizasyon yöntemi

Madde 9.1 — İzleme, ölçme, analiz ve değerlendirme:
├── İzlenecek önemli özellikleri belirleme
├── Ölçüm cihazlarının kalibrasyonu
├── Planlanan aralıklarla analiz ve değerlendirme
└── Enerji performans iyileşmesini değerlendirme

Madde 9.3 — Yönetimin gözden geçirmesi:
├── EnPI sonuçları yönetime sunma
├── Hedeflere ulaşma durumu
└── İyileştirme fırsatları
```

### 1.3 M&T'nin Faydaları

| Fayda | Açıklama | Tipik Etki |
|-------|----------|-----------|
| Erken tespit | Enerji israfını hızlı fark etme | %5-15 tasarruf (ilk yıl) |
| Bilinçli yönetim | Veri bazlı karar alma | Operasyonel iyileşme |
| Hedef izleme | Tasarruf hedeflerinin takibi | Hedefe ulaşma oranı artışı |
| M&V desteği | Projelerin tasarruf doğrulaması | Teşvik başvurusu güçlendirme |
| Fatura kontrolü | Hatalı faturaları tespit etme | %1-3 fatura tasarrufu |
| Sürdürülebilirlik | CO₂ azaltma izleme ve raporlama | Kurumsal itibar |

## 2. M&T Sisteminin Bileşenleri (M&T System Components)

### 2.1 Beş Temel Bileşen

```
M&T sistemi beş bileşen döngüsü:

┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ 1.Ölçüm │───▶│ 2.Kayıt │───▶│ 3.Analiz│───▶│4.Rapor  │───▶│5.Aksiyon│
│(Measure)│    │(Record) │    │(Analyze)│    │(Report) │    │ (Act)   │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └────┬────┘
      ▲                                                          │
      └──────────────────────────────────────────────────────────┘
                        (Sürekli iyileştirme döngüsü)
```

**Bileşen 1 — Ölçüm (Measurement)**

```
Ölçüm altyapısı:
├── Elektrik sayaçları (ana + alt sayaçlar)
├── Doğalgaz sayaçları (mekanik veya ultrasonik)
├── Buhar debimetre (vortex, orifis, ultrasonik)
├── Su sayaçları
├── Sıcaklık sensörleri (PT100, termocouple)
├── Basınç transmitterleri
├── Güç analizörleri (harmonik, güç faktörü)
└── Çevresel sensörler (sıcaklık, nem — CDD/HDD için)

Ölçüm doğruluğu gereksinimleri:
├── Elektrik: ±%0.5 - %1 (Class 0.5 veya 1)
├── Gaz: ±%1 - %2 (Türbin veya ultrasonik)
├── Buhar: ±%2 - %5 (Vortex veya DP)
├── Sıcaklık: ±0.5°C (PT100)
└── Basınç: ±%0.5 (transmitter)
```

**Bileşen 2 — Kayıt (Recording)**

```
Veri kayıt yöntemleri:
├── Manuel okuma: Günlük/haftalık sayaç okuma + formlar
├── Yarı otomatik: Pulse çıkışlı sayaç + veri toplayıcı (data logger)
├── Tam otomatik: SCADA / BMS / IoT platformu
└── Fatura bazlı: Aylık fatura verisi (en basit)

Veri saklama:
├── Veritabanı: SQL / NoSQL (zaman serisi — InfluxDB, TimescaleDB)
├── Bulut: AWS IoT, Azure IoT Hub, Google Cloud IoT
├── Yerel: SCADA historian (OSIsoft PI, Wonderware)
└── Spreadsheet: Küçük tesisler için Excel (geçici çözüm)
```

**Bileşen 3 — Analiz (Analysis)**

```
Analiz türleri:
├── Trend analizi: Zaman serisi grafikleri (günlük, haftalık, aylık)
├── Karşılaştırma: Dönemler arası, vardiyalar arası, benzer tesisler arası
├── Regresyon: Enerji vs ilgili değişkenler (baseline model)
├── CUSUM: Kümülatif performans izleme (Bkz: cusum_analysis.md)
├── Pareto: En büyük tüketim noktalarını sıralama
├── Sankey: Enerji akış diyagramı (ExergyLab çıktısı)
├── Exergy: Termodinamik kalite analizi (ExergyLab çıktısı)
└── Oran analizi: EnPI hesaplama ve izleme (Bkz: enpi_guide.md)
```

**Bileşen 4 — Raporlama (Reporting)**

```
Raporlama katmanları:
├── Operasyon raporu: Günlük/vardiya bazlı, anlık sapma bildirimi
├── Mühendislik raporu: Haftalık/aylık, detaylı analiz ve öneriler
├── Yönetim raporu: Aylık/çeyreklik, özet EnPI + maliyet + trend
├── Uyum raporu: Yıllık, YEGM bildirimi, ISO 50001 denetim
└── Stratejik rapor: Yıllık, yatırım planı, hedef güncelleme
```

**Bileşen 5 — Aksiyon (Action)**

```
Aksiyon türleri:
├── Acil müdahale: Anomali tespit → araştırma → düzeltme (saat-gün)
├── Operasyonel düzeltme: Ayar değişikliği, çalışma programı (gün-hafta)
├── Bakım aksiyonu: Planlı bakım, onarım, temizlik (hafta-ay)
├── Proje uygulaması: Ekipman değişikliği, yenileme (ay-yıl)
└── Stratejik karar: Yatırım, teknoloji değişikliği (yıl)

Aksiyon takip mekanizması:
├── Aksiyon kartı: Sorun → neden → aksiyon → sorumlu → tarih → durum
├── Toplantı: Haftalık enerji ekibi toplantısı
├── Sistem: İş emri / CMMS entegrasyonu
└── KPI: Aksiyon kapanma oranı ve süresi
```

## 3. Ölçüm Hiyerarşisi (Metering Hierarchy)

### 3.1 Beş Seviye Ölçüm Yapısı

```
Ölçüm hiyerarşisi (üstten alta):

Seviye 0 — Fatura (Utility Bill):
├── Kaynak: Enerji tedarikçisi faturası
├── Ölçüm: Aylık toplam tüketim [kWh, Sm³]
├── Cihaz: Tedarikçi sayacı (tesis dışı)
├── Veri sıklığı: Aylık
├── Maliyet: Sıfır (zaten mevcut)
└── Kullanım: Genel trend, fatura kontrolü

Seviye 1 — Ana Sayaç (Main Meter):
├── Kaynak: Tesis girişi (trafo, gaz istasyonu)
├── Ölçüm: Toplam tüketim [kWh, Sm³, ton buhar]
├── Cihaz: Şebeke sayacı + check meter
├── Veri sıklığı: 15 dakika (otomatik) veya günlük (manuel)
├── Maliyet: 5.000-20.000 TL/sayaç (check meter)
└── Kullanım: Fatura doğrulama, tesis toplam izleme

Seviye 2 — Bina / Alan (Building / Area):
├── Kaynak: Bina veya üretim alanı panelleri
├── Ölçüm: Alan bazlı tüketim [kWh, Sm³]
├── Cihaz: CT bazlı enerji analizörü, gaz sayacı
├── Veri sıklığı: 15 dakika - saatlik
├── Maliyet: 3.000-15.000 TL/sayaç
└── Kullanım: Bina/alan karşılaştırma, maliyet dağıtımı

Seviye 3 — Sistem (System):
├── Kaynak: Buhar sistemi, basınçlı hava, soğutma, aydınlatma
├── Ölçüm: Sistem bazlı tüketim + parametreler
├── Cihaz: Debimetre, güç analizörü, enerji sayacı
├── Veri sıklığı: 1 dakika - 15 dakika
├── Maliyet: 5.000-30.000 TL/sistem
└── Kullanım: Sistem verimi izleme, SEU yönetimi

Seviye 4 — Ekipman (Equipment):
├── Kaynak: Tekil ekipman (kazan, kompresör, chiller, pompa)
├── Ölçüm: Ekipman verimi, enerji tüketimi, çıktı
├── Cihaz: Güç ölçer, debimetre, sıcaklık/basınç sensörü
├── Veri sıklığı: 1 saniye - 1 dakika (PLC/SCADA)
├── Maliyet: 2.000-20.000 TL/ekipman
└── Kullanım: Ekipman verimi, bakım planı, ExergyLab analizi
```

### 3.2 Şematik Hiyerarşi

```
                    ┌──────────────────────┐
                    │  Seviye 0: Fatura     │ ← Aylık toplam (ücretsiz)
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │  Seviye 1: Ana Sayaç  │ ← 15dk / günlük
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────┴──────┐ ┌──────┴───────┐ ┌──────┴───────┐
    │ Seviye 2: Üretim│ │Seviye 2:Ofis │ │Seviye 2:Depo │ ← Alan bazlı
    └────────┬───────┘ └──────────────┘ └──────────────┘
             │
    ┌────────┼─────────────────┐
    │        │                 │
┌───┴───┐ ┌──┴──────┐ ┌───────┴──────┐
│Buhar  │ │Basınçlı │ │ Soğutma      │  ← Seviye 3: Sistem
│Sistemi│ │Hava     │ │ Sistemi      │
└───┬───┘ └────┬────┘ └──────┬───────┘
    │          │             │
┌───┴──┐ ┌────┴──┐   ┌──────┴──────┐
│Kazan1│ │Komp.1 │   │Chiller 1    │   ← Seviye 4: Ekipman
│Kazan2│ │Komp.2 │   │Chiller 2    │
└──────┘ └───────┘   └─────────────┘
```

## 4. Alt Ölçüm (Sub-Metering) Stratejisi

### 4.1 Pareto Bazlı Önceliklendirme

```
Pareto prensibi ile alt ölçüm stratejisi:

İlke: %80 enerji tüketimini kapsayacak minimum sayaç sayısı

Örnek — Bir fabrikada enerji dağılımı:

Sıra  Sistem              Pay     Kümülatif  Sayaç Gerekli?
1     Buhar kazanları      %32     %32        ✓ Öncelik 1
2     Basınçlı hava        %18     %50        ✓ Öncelik 1
3     Soğutma sistemi      %15     %65        ✓ Öncelik 1
4     Üretim motorları     %12     %77        ✓ Öncelik 2
5     Kurutma fırını        %8     %85        ✓ Öncelik 2
6     Aydınlatma            %5     %90        ○ Değerlendir
7     HVAC                  %4     %94        ○ Değerlendir
8     Ofis + yardımcı       %3     %97        ✗ Düşük öncelik
9     Diğer                 %3     %100       ✗ Düşük öncelik

Sonuç: İlk 5 sistem için alt ölçüm → %85 kapsam → 5-8 sayaç yeterli
Bütçe: 5 × 10.000 TL = 50.000 TL (kurulum dahil)
Beklenen tasarruf: %5-10 → 100.000-200.000 TL/yıl
ROI: 3-12 ay geri ödeme
```

### 4.2 Maliyet-Fayda Analizi

| Seviye | Sayaç Sayısı | Toplam Maliyet (TL) | Kapsam | Beklenen Tasarruf | Geri Ödeme |
|--------|-------------|--------------------|---------|--------------------|-----------|
| Sadece Seviye 1 | 2-3 | 20.000-40.000 | %100 (toplam) | %2-5 | 3-6 ay |
| + Seviye 2 | 5-8 | 50.000-100.000 | Alan bazlı | %5-8 | 6-12 ay |
| + Seviye 3 | 10-15 | 100.000-200.000 | Sistem bazlı | %8-12 | 12-18 ay |
| + Seviye 4 | 20-40 | 200.000-500.000 | Ekipman bazlı | %10-15 | 18-24 ay |

### 4.3 Ölçüm Teknolojileri

| Teknoloji | Tip | Avantaj | Dezavantaj | Maliyet |
|-----------|-----|---------|-----------|---------|
| CT (Akım Trafosu) bazlı | Elektrik | Retrofit kolay, kesintisiz | Yalnız elektrik | 2.000-5.000 TL |
| Vortex debimetre | Buhar | Dayanıklı, geniş aralık | Düşük debide hata | 8.000-20.000 TL |
| Ultrasonik debimetre | Sıvı/gaz | Kelepçeli, kesintisiz kurulum | Kalibrasyona duyarlı | 5.000-25.000 TL |
| Kablosuz sensör (IoT) | Çeşitli | Kablolama gerektirmez, hızlı kurulum | Pil ömrü, sinyal | 1.500-5.000 TL |
| Kablolu Modbus | Çeşitli | Güvenilir, sürekli | Kablolama maliyeti | 3.000-10.000 TL |
| SCADA entegrasyonu | Tümü | Mevcut altyapı kullanımı | Entegrasyon karmaşıklığı | Proje bazlı |

## 5. Veri Toplama ve İletişim (Data Collection and Communication)

### 5.1 Veri Toplama Yöntemleri

```
Veri toplama yöntemleri karşılaştırma:

1. Manuel Okuma:
   ├── Yöntem: Personel ile sayaç okuma + form doldurma
   ├── Sıklık: Günlük veya haftalık
   ├── Maliyet: Düşük (personel zamanı)
   ├── Avantaj: Basit, ek yatırım yok
   ├── Dezavantaj: İnsan hatası, sınırlı sıklık, zaman kaybı
   └── Uygun: Küçük tesisler, başlangıç seviyesi

2. Yarı Otomatik (Pulse + Data Logger):
   ├── Yöntem: Sayaçtan pulse çıkışı → data logger → USB/SD kart
   ├── Sıklık: 1 dakika - 15 dakika
   ├── Maliyet: 2.000-5.000 TL/logger
   ├── Avantaj: Otomatik, yüksek çözünürlük
   ├── Dezavantaj: Manuel veri indirme gerekli
   └── Uygun: Orta ölçekli tesisler, proje bazlı izleme

3. Tam Otomatik (SCADA / BMS):
   ├── Yöntem: Sayaçlar → PLC/RTU → SCADA → veritabanı
   ├── Protokoller: Modbus RTU/TCP, BACnet, Profinet, OPC-UA
   ├── Sıklık: 1 saniye - 15 dakika (programlanabilir)
   ├── Maliyet: 50.000-500.000 TL (sistem büyüklüğüne göre)
   ├── Avantaj: Gerçek zamanlı, alarm, otomasyon
   ├── Dezavantaj: Yüksek başlangıç yatırımı, bakım
   └── Uygun: Büyük tesisler, ISO 50001 hedefi olanlar

4. IoT Platformu (Bulut Tabanlı):
   ├── Yöntem: Kablosuz sensörler → gateway → bulut → dashboard
   ├── Protokoller: LoRa, Zigbee, NB-IoT, Wi-Fi, 4G/5G
   ├── Sıklık: 1 dakika - 15 dakika
   ├── Maliyet: 1.500-5.000 TL/sensör + aylık platform ücreti
   ├── Avantaj: Hızlı kurulum, ölçeklenebilir, uzaktan erişim
   ├── Dezavantaj: İnternet bağımlılığı, pil ömrü, güvenlik
   └── Uygun: Retrofit projeler, çoklu tesis yönetimi
```

### 5.2 Veri Sıklığı Seçimi

| Kullanım Amacı | Önerilen Sıklık | Veri Hacmi (1 yıl/sayaç) | Açıklama |
|-----------------|-----------------|--------------------------|----------|
| Fatura kontrolü | Aylık | 12 kayıt | En basit |
| EnPI izleme | Haftalık/aylık | 52-12 kayıt | ISO 50001 uyumlu |
| CUSUM analizi | Aylık | 12 kayıt | Regresyon modeli ile |
| Yük profili | 15 dakika | 35.040 kayıt | Tepe yük yönetimi |
| Proses optimizasyon | 1 dakika | 525.600 kayıt | SCADA seviyesi |
| Ekipman M&V | 1 dakika | 525.600 kayıt | IPMVP Opsiyon B |

### 5.3 İletişim Protokolleri

```
Endüstriyel iletişim protokolleri:

Modbus RTU (RS-485):
├── Yaygın endüstriyel standart
├── Mesafe: 1.200 m (RS-485)
├── Hız: 9.600 - 115.200 baud
├── Kablolu, ucuz, güvenilir
└── Enerji sayaçları, sıcaklık/basınç transmitterleri

Modbus TCP (Ethernet):
├── Modbus over Ethernet
├── Mesafe: 100 m (Cat5/6), fiber ile sınırsız
├── Hız: 10/100/1000 Mbps
├── Mevcut ağ altyapısı kullanımı
└── Modern sayaçlar, gateway'ler

BACnet (Building Automation):
├── Bina otomasyon standardı
├── BACnet IP veya BACnet MS/TP
├── HVAC, aydınlatma kontrolü
└── BMS (Building Management System)

OPC-UA:
├── Platform bağımsız
├── SCADA ve üst seviye entegrasyon
├── Güvenli iletişim (şifreleme)
└── Endüstri 4.0 uyumlu

MQTT (IoT):
├── Hafif mesajlaşma protokolü
├── Publish/subscribe modeli
├── Bulut platformlar ile entegrasyon
└── Düşük bant genişliği, pil dostu
```

## 6. Dashboard Tasarımı (Dashboard Design)

### 6.1 Yönetici Dashboard (Executive)

```
Yönetici dashboard bileşenleri:

┌─────────────────────────────────────────────────────┐
│ ENERJİ PERFORMANS ÖZETİ — Ocak 2026                │
├──────────────┬──────────────┬───────────────────────┤
│ Bu Ay SEC    │ Hedef SEC    │ Durum                 │
│ 142 kWh/ton  │ 135 kWh/ton  │ 🔴 %5.2 üzerinde     │
├──────────────┴──────────────┴───────────────────────┤
│                                                     │
│  [Enerji Maliyeti Trendi — Son 12 Ay]              │
│  ═══════════════════════════════                    │
│  Bar chart: Aylık TL + hedef çizgisi               │
│                                                     │
├─────────────────────┬───────────────────────────────┤
│  Enerji Dağılımı    │  CUSUM Grafik                 │
│  Pie chart:         │  Line chart:                  │
│  Elektrik %45       │  Son 12 ay kümülatif          │
│  Doğalgaz %48       │  tasarruf/kayıp               │
│  Diğer %7           │                               │
├─────────────────────┴───────────────────────────────┤
│  KPI Kartları:                                      │
│  [Toplam Maliyet] [CO₂ Emisyon] [Exergy Verimi]   │
│  1.250.000 TL      485 ton       %26.8             │
└─────────────────────────────────────────────────────┘

Güncelleme sıklığı: Aylık
Alarm: Kırmızı/sarı/yeşil trafik ışığı
```

### 6.2 Operatör Dashboard (Operator)

```
Operatör dashboard bileşenleri:

┌──────────────────────────────────────────────────────┐
│ CANLI ENERJİ İZLEME — Anlık                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [Anlık Güç Tüketimi]    [Doğalgaz Akış]            │
│  Gauge: 850 kW           Gauge: 380 Sm³/h            │
│  Limit: 1.000 kW         Limit: 500 Sm³/h            │
│                                                      │
├──────────────────────────────────────────────────────┤
│  [Ekipman Durumu Tablosu]                            │
│                                                      │
│  Ekipman      Durum    Verim    Alarm                │
│  Kazan 1      Çalışır  %87.2    ─                    │
│  Kazan 2      Standby  ─        ─                    │
│  Kompresör 1  Çalışır  %72.5    ▲ Yüksek SPC        │
│  Kompresör 2  Çalışır  %78.1    ─                    │
│  Chiller 1    Çalışır  COP 4.3  ─                    │
│  Chiller 2    Arıza    ─        ▲▲ Servis gerekli   │
│                                                      │
├──────────────────────────────────────────────────────┤
│  [Bugünkü Tüketim vs Beklenen]                      │
│  Elektrik: 18.500 kWh / 19.200 kWh (-%3.6 ✓)       │
│  Doğalgaz: 8.200 Sm³ / 7.800 Sm³ (+%5.1 ▲)         │
│                                                      │
│  [Son 24 Saat Yük Profili]                           │
│  Line chart: Gerçek vs beklenen (15 dk aralık)       │
└──────────────────────────────────────────────────────┘

Güncelleme: Gerçek zamanlı (1-15 dakika)
Alarm: Sesli + görsel uyarı
```

### 6.3 Mühendis Dashboard (Engineer)

```
Mühendis dashboard bileşenleri:

Sekme 1 — EnPI Analiz:
├── Tüm EnPI trend grafikleri (SEC, exergy verim, COP, vb.)
├── Regresyon model kontrol (R², residual)
├── CUSUM grafiği + kontrol sınırları
├── Sektörel benchmark karşılaştırma çubuğu
└── Hedef gerçekleşme tablosu

Sekme 2 — Enerji Denge:
├── Sankey diyagramı (enerji + exergy — ExergyLab)
├── Kaynak bazlı dağılım (pie + bar)
├── Sistem bazlı dağılım
├── Kayıp analizi (exergy yıkımı haritası)
└── Karşılaştırma: Bu ay vs geçen yıl aynı ay

Sekme 3 — Proje İzleme:
├── Uygulanan ECM'lerin CUSUM ile tasarruf doğrulaması
├── Devam eden projelerin ilerleme durumu
├── Planlanan projelerin fizibilite özeti
└── Toplam portföy ROI hesabı

Sekme 4 — Ham Veri:
├── Tüm sayaçlardan ham veriye erişim
├── Veri dışa aktarma (CSV, Excel)
├── Veri kalitesi kontrol (eksik veri, anomali)
└── Kalibrasyon takip tablosu

Güncelleme: Saatlik — günlük
Format: İnteraktif grafik, filtre, zoom, drill-down
```

## 7. Hedefleme ve Alarm (Targeting and Alarms)

### 7.1 Hedef Çizgisi Belirleme

```
Hedef çizgisi (target line) belirleme yöntemleri:

Yöntem 1 — Regresyon bazlı hedef:
├── Baseline regresyon: E_baseline = β₀ + β₁X₁ + β₂X₂
├── Hedef: E_hedef = (1 - tasarruf_hedefi%) × E_baseline
├── Örnek: E_hedef = 0.92 × E_baseline (%8 tasarruf hedefi)
└── Avantaj: Normalizasyonlu, adil karşılaştırma

Yöntem 2 — SEC bazlı hedef:
├── Baseline SEC: 108 kWh/ton
├── Hedef SEC: 100 kWh/ton (%7.4 iyileşme)
├── E_hedef = SEC_hedef × Üretim_dönem
└── Avantaj: Basit, anlaşılır

Yöntem 3 — Benchmark bazlı hedef:
├── Sektörel en iyi uygulama: 90 kWh/ton
├── Tesis mevcut: 108 kWh/ton
├── Kısa vadeli hedef: 100 kWh/ton (%7.4)
├── Orta vadeli hedef: 95 kWh/ton (%12)
├── Uzun vadeli hedef: 90 kWh/ton (%17)
└── Avantaj: Stratejik vizyon sağlar

Yöntem 4 — Exergy bazlı hedef (ExergyLab):
├── Mevcut exergy verimi: %26.8
├── Sektör ortalaması: %28
├── En iyi uygulama: %35
├── Kısa vadeli hedef: %28 (sektör ortalamasına ulaşma)
├── Orta vadeli hedef: %32
└── Avantaj: Termodinamik limit farkındalığı
```

### 7.2 Tolerans Bandı ve Alarm Seviyeleri

```
Hedef etrafında tolerans bandı:

           ─── Kritik (≥%15 sapma)  → Kırmızı alarm
         ─── Dikkat (≥%10 sapma)    → Turuncu alarm
       ─── Uyarı (≥%5 sapma)       → Sarı uyarı
═══════ Hedef çizgisi               → Yeşil
       ─── Uyarı (≥%5 altında)     → Mavi (olumlu)
         ─── İyi performans         → Koyu yeşil

Alarm eskalasyon prosedürü:

Seviye 1 — Sarı uyarı (%5-10 sapma):
├── Bildirim: Operatör + enerji yöneticisi
├── Süre: 48 saat içinde neden araştırması
└── Aksiyon: Operasyonel düzeltme

Seviye 2 — Turuncu alarm (%10-15 sapma):
├── Bildirim: Enerji ekibi + üretim müdürü
├── Süre: 24 saat içinde root cause analizi
└── Aksiyon: Bakım veya operasyon değişikliği

Seviye 3 — Kırmızı alarm (≥%15 sapma):
├── Bildirim: Tesis müdürü + teknik direktör
├── Süre: Acil müdahale
└── Aksiyon: Ekipman durdurma/değiştirme, acil bakım
```

## 8. M&T Yazılımları (M&T Software)

### 8.1 Ticari Çözümler

| Yazılım | Geliştirici | Özellikler | Fiyat Aralığı |
|---------|-------------|-----------|----------------|
| EnergyCAP | EnergyCAP Inc. | Fatura yönetimi + analiz + raporlama | $$$ |
| eSight Energy | eSight | Gerçek zamanlı izleme + alarm + dashboard | $$$ |
| DEXMA | DEXMA Sensors | Bulut tabanlı + AI + benchmark | $$ |
| Schneider EcoStruxure | Schneider Electric | IoT + SCADA + enerji yönetimi | $$$$ |
| Siemens Navigator | Siemens | Bina + sanayi enerji yönetimi | $$$$ |
| Honeywell Forge | Honeywell | AI bazlı optimizasyon | $$$$ |
| EnergyCap SmartAnalytics | EnergyCAP | Regresyon + CUSUM + raporlama | $$ |
| Carbon Trust M&T Tool | Carbon Trust | Excel bazlı, ücretsiz | Ücretsiz |

### 8.2 Açık Kaynak ve Düşük Maliyetli Seçenekler

```
Açık kaynak enerji yönetimi araçları:

1. OpenEnergyMonitor:
   ├── Donanım + yazılım (açık kaynak)
   ├── CT bazlı elektrik ölçüm
   ├── Emoncms web arayüzü
   └── Maliyet: ~500-2.000 TL/nokta

2. Grafana + InfluxDB:
   ├── Zaman serisi veritabanı + dashboard
   ├── MQTT, Modbus entegrasyonu
   ├── Alarm kuralları + bildirim
   └── Maliyet: Ücretsiz (self-hosted)

3. Home Assistant (sanayi adaptasyonu):
   ├── Otomasyon platformu
   ├── Geniş sensör/cihaz desteği
   ├── Dashboard özelleştirme
   └── Maliyet: Ücretsiz (self-hosted)

4. Google Sheets / Excel:
   ├── Başlangıç seviyesi M&T
   ├── Manuel veri girişi + formüller
   ├── Grafik ve analiz
   └── Maliyet: Düşük
```

### 8.3 ExergyLab ile Entegrasyon Vizyonu

```
ExergyLab — M&T entegrasyon vizyonu:

Mevcut ExergyLab yetenekleri:
├── Ekipman bazında exergy analizi
├── Fabrika toplam exergy değerlendirme
├── Sankey diyagramı (enerji + exergy)
├── Cross-equipment fırsat analizi
├── AI yorumlama ve öneri
└── Benchmark karşılaştırma

M&T entegrasyonu ile eklenecekler:
├── Zaman serisi veri depolama (aylık snapshot)
├── Regresyon modeli otomatik kurulum
├── CUSUM hesaplama ve görselleştirme
├── EnPI dashboard (tesis → sistem → ekipman)
├── Alarm ve bildirim sistemi
├── Otomatik raporlama (PDF export)
├── SCADA/IoT veri bağlantısı (API)
└── Exergy bazlı M&T (benzersiz)

Exergy bazlı M&T avantajı:
├── Enerji M&T: Miktar bazlı izleme (kWh, Sm³)
├── Exergy M&T: Kalite bazlı izleme (η_ex, Ė_destroyed)
├── Birlikte: Hem miktar hem kalite → tam resim
└── Örnek: "Doğalgaz tüketimi %2 arttı ama exergy verimi %3 iyileşti
    → daha yüksek buhar basıncına geçildi, net pozitif etki"
```

## 9. Çalışılmış Örnek — Tekstil Fabrikasında M&T Kurulumu

### 9.1 Tesis Tanımı

```
Tesis: Tekstil boyama ve terbiye fabrikası
Kapasite: 50 ton/gün kumaş boyama
Yıllık enerji tüketimi: 4.200 TEP (doğalgaz %62, elektrik %38)
Çalışma: 300 gün/yıl, 3 vardiya
Ana sistemler: Buhar (boyama + kurutma), basınçlı hava, soğutma, aydınlatma
```

### 9.2 Ölçüm Hiyerarşisi Tasarımı

```
Kurulu ölçüm hiyerarşisi (3 seviye, 12 sayaç):

Seviye 1 — Ana Sayaçlar (2 adet):
├── S01: Ana elektrik sayacı (trafo çıkışı) — 3 fazlı, CT bazlı
└── S02: Ana doğalgaz sayacı (istasyon) — ultrasonik

Seviye 2 — Alan Sayaçları (4 adet):
├── S03: Boyahane elektrik (CT bazlı)
├── S04: Kurutma/ram elektrik (CT bazlı)
├── S05: Kazan dairesi doğalgaz (Modbus)
└── S06: Kompresör dairesi elektrik (CT bazlı)

Seviye 3 — Sistem/Ekipman Sayaçları (6 adet):
├── S07: Kazan 1 buhar debimetre (vortex)
├── S08: Kazan 2 buhar debimetre (vortex)
├── S09: Kompresör 1 güç ölçer
├── S10: Kompresör 2 güç ölçer
├── S11: Ram (stenter) doğalgaz sayacı
└── S12: Boyama makineleri buhar sayacı

İletişim: Modbus RTU (RS-485) → RTU → Ethernet → Sunucu
Veri sıklığı: 15 dakika (tüm sayaçlar)
Yazılım: Grafana + InfluxDB (açık kaynak) + ExergyLab API
```

### 9.3 Dashboard ve Raporlama

```
M&T dashboard yapısı:

Ekran 1 — Boyahane kontrol odası:
├── Anlık buhar ve elektrik tüketimi
├── Boyama makinesi bazlı tüketim (canlı)
├── Vardiya bazlı performans karşılaştırma
└── Alarm paneli

Ekran 2 — Enerji yöneticisi ofisi:
├── Fabrika SEC trendi (haftalık güncelleme)
├── CUSUM grafiği (aylık güncelleme)
├── Sistem bazlı EnPI tablosu
├── ExergyLab exergy verim trendi
└── Aksiyon takip tablosu

Aylık rapor (PDF):
├── Yönetici özeti (1 sayfa)
├── EnPI performans tablosu + grafikler (2 sayfa)
├── CUSUM analizi + yorum (1 sayfa)
├── Sistem bazlı değerlendirme (2 sayfa)
├── Aksiyon planı güncelleme (1 sayfa)
└── ExergyLab exergy analiz özeti (1 sayfa)
```

### 9.4 Sonuçlar (İlk 12 Ay)

```
M&T kurulumu sonuçları:

Yatırım:
├── Sayaçlar + kurulum: 145.000 TL
├── Yazılım + altyapı: 35.000 TL
├── Toplam: 180.000 TL

Tespit edilen tasarruf fırsatları:
├── Hafta sonu boş makine buhar tüketimi: 85.000 Sm³/yıl (operasyonel)
├── Kompresör 1 düşük verim: VSD gerekli (proje)
├── Ram doğalgaz aşırı tüketim: Brülör ayarı (bakım)
├── Gece vardiyası aydınlatma fazlalığı: Otomasyon (proje)
└── Boyama makinesi bekleme buharı: Program optimizasyonu (operasyonel)

Gerçekleşen tasarruf (sadece operasyonel düzeltmeler):
├── Doğalgaz: 120.000 Sm³/yıl → 350.000 TL/yıl
├── Elektrik: 85.000 kWh/yıl → 212.500 TL/yıl
├── Toplam: 562.500 TL/yıl
├── Geri ödeme: 180.000 / 562.500 = 3.8 ay
└── CO₂ azaltma: 280 ton/yıl

ExergyLab ek bulguları:
├── Fabrika exergy verimi: %23.5 → %26.2 (operasyonel düzeltmeler sonrası)
├── Kazan exergy verimi: %33.8 → economizer ile %40+ hedeflenebilir
├── Boyama prosesi exergy analizi: %62 kayıp → ısı geri kazanım fırsatı
└── Cross-equipment: Ram baca gazı → boyama makinesi ön ısıtma (potansiyel: 120 kW)
```

## 10. İlgili Dosyalar

- [Enerji Yönetimi INDEX](INDEX.md) — Dosya navigasyonu
- [EnPI Rehberi](enpi_guide.md) — Performans göstergeleri tanımlama ve izleme
- [CUSUM Analizi](cusum_analysis.md) — Kümülatif toplam analizi
- [Baseline ve EnPI](baseline_enpi.md) — Regresyon modeli ve EnB oluşturma
- [Veri Toplama](../data_collection.md) — Fabrika veri toplama yöntemleri
- [Performans Göstergeleri](../performance_indicators.md) — Fabrika seviyesi göstergeler
- [Türkiye Mevzuatı](turkey_legislation.md) — YEGM ölçüm ve bildirim zorunlulukları

## 11. Referanslar

- Carbon Trust, "Monitoring and Targeting in Large Companies", CTG008
- Carbon Trust, "Monitoring and Targeting — A Cost-Effective Route to Energy Savings", Good Practice Guide GPG112
- CIBSE, "TM39: Building Energy Metering", 2009
- CIBSE, "TM22: Energy Assessment and Reporting Methodology"
- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50006:2014, "Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI)"
- ASHRAE, "Energy Management Handbook", 9th ed., 2020
- US DOE, "Metering Best Practices Guide"
- BACnet Standard — ASHRAE 135
- Modbus Organization, "Modbus Application Protocol Specification V1.1b3"
- Grafana Labs, "Grafana Open Source Documentation"
- InfluxData, "InfluxDB Time Series Database Documentation"
