---
title: "Fabrika Enerji Verimlilik Vaka Çalışmaları (Factory Energy Efficiency Case Studies)"
category: factory
equipment_type: factory
keywords: [vaka çalışması, uygulama, fabrika]
related_files: [factory/implementation.md, factory/economic_analysis.md, factory/reporting.md]
use_when: ["Gerçek uygulama örnekleri gerektiğinde", "Benzer fabrika vaka çalışması aranırken"]
priority: low
last_updated: 2026-01-31
---
# Fabrika Enerji Verimlilik Vaka Çalışmaları (Factory Energy Efficiency Case Studies)

> Son güncelleme: 2026-01-31

## Genel Bakış

Bu dosya, çeşitli sektörlerden gerçek dünya fabrika enerji verimlilik projelerini içerir. Her vaka çalışması; fabrika profili, başlangıç durumu, uygulanan iyileştirmeler, elde edilen sonuçlar ve çıkarılan dersleri kapsar. Veriler anonimleştirilmiş olup, endüstri ortalamalarına dayalı temsili değerler kullanılmıştır.

## Vaka 1: Tekstil Fabrikası — Kapsamlı Enerji ve Exergy Audit

### Fabrika Profili

| Parametre | Değer |
|---|---|
| Sektör | Tekstil (boyama ve terbiye) |
| Konum | Bursa, Türkiye |
| Çalışan sayısı | 450 |
| Üretim kapasitesi | 8,000 ton kumaş/yıl |
| Çalışma rejimi | 3 vardiya, 300 gün/yıl |
| Ana enerji kaynakları | Doğalgaz + elektrik |

### Başlangıç Durumu (Baseline)

```
Enerji tüketimi:
- Doğalgaz: 3,200,000 Nm³/yıl (€1,440,000/yıl)
- Elektrik: 6,400,000 kWh/yıl (€768,000/yıl)
- Toplam enerji maliyeti: €2,208,000/yıl

KPI'lar:
- SEC: 5,450 kWh/ton kumaş
- Kazan enerji verimi: %82
- Kazan exergy verimi: %26
- Basınçlı hava SPC: 7.8 kW/(m³/min)
- Kondensat geri dönüş: %45
- Buhar kapanı arıza oranı: %28

Exergy analizi:
- Fabrika exergy verimi: %18.5
- En büyük exergy yıkım kaynakları:
  1. Yanma tersinmezliği: %27
  2. Boyahane atık su ısı kaybı: %15
  3. Kurutma egzoz kaybı: %12
  4. Basınçlı hava kaçakları ve kayıpları: %8
```

### Uygulanan İyileştirmeler

| # | Önlem | Yatırım [€] | Faz |
|---|---|---|---|
| 1 | Basınçlı hava kaçak onarımı | 3,000 | Faz 1 (0-3 ay) |
| 2 | Buhar kapanı değişimi (42 adet) | 12,000 | Faz 1 |
| 3 | Kazan brülör ayarı ve O₂ trim | 8,000 | Faz 1 |
| 4 | Boru izolasyon iyileştirme | 15,000 | Faz 1 |
| 5 | Kondensat geri dönüş sistemi genişletme | 35,000 | Faz 2 (3-12 ay) |
| 6 | Boyahane atık su ısı geri kazanımı | 65,000 | Faz 2 |
| 7 | Kompresör VSD retrofit | 22,000 | Faz 2 |
| 8 | Economizer (ana kazan) | 40,000 | Faz 2 |
| 9 | LED aydınlatma dönüşümü | 30,000 | Faz 2 |
| 10 | Ram egzoz ısı geri kazanımı | 55,000 | Faz 3 (1-2 yıl) |
| **TOPLAM** | | **€285,000** | |

### Sonuçlar

```
Tasarruf sonuçları (2. yıl sonunda):

Enerji tasarrufu:
- Doğalgaz: -520,000 Nm³/yıl (%16.3 azalma)
- Elektrik: -640,000 kWh/yıl (%10.0 azalma)
- Toplam: -5,620 MWh/yıl

Maliyet tasarrufu:
- Doğalgaz: €234,000/yıl
- Elektrik: €76,800/yıl
- Toplam: €310,800/yıl

KPI iyileştirmeleri:
- SEC: 5,450 → 4,520 kWh/ton (%17.1 azalma)
- Kazan enerji verimi: %82 → %91
- Kazan exergy verimi: %26 → %33
- SPC: 7.8 → 5.9 kW/(m³/min)
- Kondensat geri dönüş: %45 → %82
- Buhar kapanı arıza: %28 → %4
- Fabrika exergy verimi: %18.5 → %24.2

CO₂ azaltma: 1,250 tCO₂/yıl

Ekonomik göstergeler:
- Toplam yatırım: €285,000
- Toplam yıllık tasarruf: €310,800
- Basit geri ödeme: 0.92 yıl
- NPV (10 yıl, %10): €1,625,000
- IRR: %108
```

### Çıkarılan Dersler

1. Boyahane atık su ısı geri kazanımı tek başına toplam tasarrufun %35'ini sağladı
2. Kaçak onarımı ve kapan değişimi gibi düşük maliyetli önlemler hızlı sonuç verdi
3. Kondensat geri dönüş sistemi genişletmesi beklenenden %20 fazla tasarruf sağladı
4. Exergy analizi, geleneksel enerji auditinin tespit edemediği ısı entegrasyon fırsatlarını ortaya koydu

---

## Vaka 2: Gıda Fabrikası — Soğutma ve Isıtma Entegrasyonu

### Fabrika Profili

| Parametre | Değer |
|---|---|
| Sektör | Gıda (süt ürünleri) |
| Konum | Bolu, Türkiye |
| Çalışan sayısı | 280 |
| Üretim kapasitesi | 120,000 ton süt/yıl |
| Çalışma rejimi | 3 vardiya, 350 gün/yıl |
| Ana enerji kaynakları | Doğalgaz + elektrik |

### Başlangıç Durumu

```
Enerji tüketimi:
- Doğalgaz: 1,800,000 Nm³/yıl (€810,000/yıl)
- Elektrik: 8,200,000 kWh/yıl (€984,000/yıl)
- Toplam enerji maliyeti: €1,794,000/yıl

SEC: 155 kWh/ton süt (elektrik) + 155 Nm³/ton süt (gaz)
Fabrika exergy verimi: %16.2

Temel sorun: Soğutma sistemi elektriğin %45'ini tüketirken,
kazan atık ısısı ve kompresör ısısı kullanılmıyordu.
Eşzamanlı ısıtma ve soğutma talebi mevcuttu.
```

### Uygulanan İyileştirmeler

| # | Önlem | Yatırım [€] | Yıllık Tasarruf [€] | SPP [yıl] |
|---|---|---|---|---|
| 1 | Chiller kondenser ısı geri kazanımı (sıcak su) | 45,000 | 38,000 | 1.2 |
| 2 | Kompresör atık ısısı → CIP sıcak su | 18,000 | 12,000 | 1.5 |
| 3 | Soğutma kulesi fan VSD | 12,000 | 8,500 | 1.4 |
| 4 | Kazan economizer | 32,000 | 18,000 | 1.8 |
| 5 | Soğuk depo kapı otomasyonu | 8,000 | 6,500 | 1.2 |
| 6 | Buhar sistemi izolasyon | 10,000 | 7,000 | 1.4 |
| 7 | Pastörizatör ısı geri kazanımı iyileştirme | 25,000 | 15,000 | 1.7 |
| **TOPLAM** | | **€150,000** | **€105,000** | **1.4** |

### Sonuçlar

```
Toplam enerji tasarrufu: 2,850 MWh/yıl (%12.8)
Toplam maliyet tasarrufu: €105,000/yıl
SEC iyileştirmesi: %12.8 azalma
Fabrika exergy verimi: %16.2 → %21.8 (%34.6 artış)
CO₂ azaltma: 680 tCO₂/yıl
NPV (10 yıl, %10): €495,000
```

### Çıkarılan Dersler

1. Eşzamanlı ısıtma-soğutma talebi olan fabrikalarda ısı geri kazanımı çok etkili
2. Chiller kondenser ısısı CIP ve pastörizasyon ön ısıtması için ideal sıcaklıkta
3. Exergy analizi, düşük sıcaklıklı atık ısının (35-45°C) kullanım fırsatlarını gösterdi
4. Soğuk depo kapı otomasyonu basit ama etkili bir önlem

---

## Vaka 3: Kimya Fabrikası — Pinch Analizi ve Isı Entegrasyonu

### Fabrika Profili

| Parametre | Değer |
|---|---|
| Sektör | Kimya (temel kimyasallar) |
| Konum | Kocaeli, Türkiye |
| Çalışan sayısı | 180 |
| Üretim kapasitesi | 50,000 ton/yıl |
| Ana enerji kaynakları | Doğalgaz + elektrik + buhar (dışarıdan) |

### Başlangıç Durumu

```
Toplam enerji maliyeti: €3,200,000/yıl
Fabrika exergy verimi: %32

Problem: Çok sayıda sıcak ve soğuk akış, birbirinden bağımsız
ısıtma ve soğutma yapılıyor. Isı entegrasyonu minimal.
```

### Pinch Analizi Sonuçları

```
Akış verileri (6 sıcak + 5 soğuk akış):

| Akış | Tip | T_giriş [°C] | T_çıkış [°C] | CP [kW/°C] | Q [kW] |
|------|-----|-------------|-------------|-----------|--------|
| H1 | Sıcak | 250 | 120 | 15 | 1,950 |
| H2 | Sıcak | 180 | 80 | 22 | 2,200 |
| H3 | Sıcak | 130 | 40 | 18 | 1,620 |
| H4 | Sıcak | 90 | 50 | 30 | 1,200 |
| H5 | Sıcak | 200 | 100 | 10 | 1,000 |
| H6 | Sıcak | 70 | 35 | 25 | 875 |
| C1 | Soğuk | 30 | 200 | 12 | 2,040 |
| C2 | Soğuk | 50 | 150 | 20 | 2,000 |
| C3 | Soğuk | 80 | 180 | 8 | 800 |
| C4 | Soğuk | 20 | 90 | 15 | 1,050 |
| C5 | Soğuk | 120 | 220 | 10 | 1,000 |

ΔTmin = 10°C

Pinch noktası: 95°C (sıcak), 85°C (soğuk)

Mevcut durum:
- Sıcak utility (QH): 4,200 kW
- Soğuk utility (QC): 5,100 kW

Pinch hedefleri:
- QH,min: 2,050 kW
- QC,min: 2,950 kW

Tasarruf potansiyeli:
- Sıcak utility: 4,200 - 2,050 = 2,150 kW (%51 azalma)
- Soğuk utility: 5,100 - 2,950 = 2,150 kW (%42 azalma)
```

### Uygulanan Önlemler

| # | Eşanjör | Kapasite [kW] | Yatırım [€] |
|---|---|---|---|
| 1 | H1 → C5 (pinch üstü) | 850 | 45,000 |
| 2 | H2 → C3 (pinch üstü) | 600 | 35,000 |
| 3 | H5 → C2 (pinch üstü) | 500 | 30,000 |
| 4 | H3 → C4 (pinch altı) | 400 | 28,000 |
| 5 | Economizer iyileştirme | 350 | 20,000 |
| **TOPLAM** | | **2,700 kW** | **€158,000** |

### Sonuçlar

```
Gerçekleşen ısı entegrasyonu: 2,700 kW (hedefin %85'i)
Sıcak utility azalma: 2,150 kW → gerçekleşen 1,900 kW (%45)
Yıllık yakıt tasarrufu: €480,000/yıl
Yıllık soğutma tasarrufu: €85,000/yıl
Toplam tasarruf: €565,000/yıl
SPP: 0.28 yıl (3.4 ay)
Fabrika exergy verimi: %32 → %41 (%28 artış)
CO₂ azaltma: 2,100 tCO₂/yıl
```

### Çıkarılan Dersler

1. Pinch analizi, kimya sektöründe en yüksek getiriyi sağlayan yöntem
2. Retrofit durumunda hedefin %80-90'ına ulaşmak pratik sınır
3. Pinch kurallarına uyum kritik: Pinch noktasını geçen ısı transferi engellenilmeli
4. Proses bilgisi ve operatör deneyimi tasarımda kritik öneme sahip

---

## Vaka 4: Çimento Fabrikası — Atık Isı Geri Kazanımı (ORC)

### Fabrika Profili

| Parametre | Değer |
|---|---|
| Sektör | Çimento |
| Konum | Gaziantep, Türkiye |
| Üretim kapasitesi | 1,200,000 ton çimento/yıl |
| Fırın kapasitesi | 4,000 ton klinker/gün |
| Çalışma | 330 gün/yıl |

### Başlangıç Durumu

```
Enerji tüketimi:
- Elektrik: 132,000 MWh/yıl (110 kWh/ton)
- Termal: 4,200,000 GJ/yıl (3,500 MJ/ton klinker)
- Toplam enerji maliyeti: €18,500,000/yıl

Atık ısı kaynakları:
- Klinker soğutucu egzoz: 340°C, 180,000 Nm³/h
- Preheater egzoz: 330°C, 250,000 Nm³/h

Fabrika exergy verimi: %28
```

### Uygulanan İyileştirme — ORC Sistemi

```
ORC sistemi spesifikasyonları:
- Kapasite: 5.5 MWe
- Isı kaynağı: Klinker soğutucu egzoz (340°C) + preheater egzoz (330°C)
- Çalışma akışkanı: Pentane
- ORC termal verimi: %22
- Yıllık çalışma: 7,500 saat

Yatırım:
- ORC sistemi: €8,500,000
- Atık ısı kazanları: €2,500,000
- Mühendislik ve montaj: €1,500,000
- Toplam: €12,500,000
```

### Sonuçlar

```
Yıllık elektrik üretimi: 5,500 × 7,500 = 41,250 MWh/yıl
Elektrik tasarrufu: %31.2 (iç tüketim)
Maliyet tasarrufu: 41,250 × €0.10 = €4,125,000/yıl
(Endüstriyel elektrik fiyatı üzerinden)

SPP: €12,500,000 / €4,125,000 = 3.03 yıl
NPV (15 yıl, %10): €18,900,000
IRR: %32

Fabrika exergy verimi: %28 → %34 (%21 artış)
CO₂ azaltma: 19,400 tCO₂/yıl
SEC elektrik: 110 → 76 kWh/ton (%31 azalma)
```

### Çıkarılan Dersler

1. Çimento sektöründe ORC, yüksek yatırıma rağmen çok iyi ekonomik getiri sağlar
2. Her iki atık ısı kaynağının (klinker soğutucu + preheater) birlikte kullanımı kapasite artırır
3. Toz filtrasyon ekipmanının bakımı ORC verimini doğrudan etkiler
4. ORC çalışma akışkanı seçimi kaynak sıcaklığına göre optimize edilmeli

---

## Vaka 5: Metal İşleme Fabrikası — Kompresör ve Fırın Optimizasyonu

### Fabrika Profili

| Parametre | Değer |
|---|---|
| Sektör | Metal (dövme ve ısıl işlem) |
| Konum | Konya, Türkiye |
| Çalışan sayısı | 150 |
| Üretim kapasitesi | 12,000 ton/yıl |
| Çalışma | 2 vardiya, 280 gün/yıl |

### Başlangıç Durumu

```
Enerji tüketimi:
- Doğalgaz: 2,800,000 Nm³/yıl (fırınlar + ısıl işlem)
- Elektrik: 4,500,000 kWh/yıl
- Toplam enerji maliyeti: €1,800,000/yıl

SEC: 2,650 kWh/ton
Fabrika exergy verimi: %22

Sorunlar:
1. Isıl işlem fırınları eski, düşük verimli (yalıtım zayıf)
2. Basınçlı hava kaçak oranı: %35
3. Fırın atık gazı (500-700°C) kullanılmıyor
4. Kompresörler tam yükte on/off çalışıyor
```

### Uygulanan İyileştirmeler

| # | Önlem | Yatırım [€] | Yıllık Tasarruf [€] | SPP [yıl] |
|---|---|---|---|---|
| 1 | Kaçak onarımı (kapsamlı) | 5,000 | 42,000 | 0.12 |
| 2 | VSD kompresör (75 kW) | 20,000 | 15,000 | 1.3 |
| 3 | Fırın yalıtım yenileme (3 fırın) | 45,000 | 55,000 | 0.8 |
| 4 | Fırın atık gazı → besleme suyu ısıtma | 60,000 | 48,000 | 1.3 |
| 5 | Fırın kontrol sistemi modernizasyonu | 35,000 | 32,000 | 1.1 |
| 6 | Rejeneratif brülör (1 fırın) | 80,000 | 65,000 | 1.2 |
| **TOPLAM** | | **€245,000** | **€257,000** | **0.95** |

### Sonuçlar

```
Toplam enerji tasarrufu: 3,200 MWh/yıl (%14.3)
Toplam maliyet tasarrufu: €257,000/yıl
SEC: 2,650 → 2,270 kWh/ton (%14.3 azalma)
Fabrika exergy verimi: %22 → %29 (%32 artış)
CO₂ azaltma: 850 tCO₂/yıl
NPV (10 yıl, %10): €1,335,000
```

### Çıkarılan Dersler

1. Fırın yalıtım yenileme basit ama çok etkili — en yüksek ROI önlemlerden biri
2. Rejeneratif brülör fırın yakıt tüketimini %30-40 azalttı
3. Basınçlı hava kaçak oranı (%35) sektör ortalamasının üzerindeydi — düzenli tarama kritik
4. Fırın kontrol modernizasyonu (PLC + PID) yatırımın ötesinde kalite iyileşmesi de sağladı

---

## Vaka 6: Otomotiv Fabrikası — Boyahane Enerji Optimizasyonu

### Fabrika Profili

| Parametre | Değer |
|---|---|
| Sektör | Otomotiv (araç montaj) |
| Konum | Sakarya, Türkiye |
| Üretim kapasitesi | 150,000 araç/yıl |
| Çalışma | 2 vardiya, 250 gün/yıl |

### Başlangıç Durumu

```
Enerji tüketimi:
- Doğalgaz: 12,000,000 Nm³/yıl
- Elektrik: 75,000,000 kWh/yıl
- Toplam enerji maliyeti: €14,400,000/yıl

SEC: 1,720 kWh/araç (toplam)
Boyahane payı: %62 (toplam enerjinin)

Fabrika exergy verimi: %21

Boyahane enerji dağılımı:
- Boya kabini HVAC: %35
- Boya fırınları: %25
- RTO (regeneratif termal oksidizer): %20
- Ön işlem + E-coat: %12
- Diğer: %8
```

### Uygulanan İyileştirmeler

| # | Önlem | Yatırım [€] | Yıllık Tasarruf [€] | SPP [yıl] |
|---|---|---|---|---|
| 1 | RTO ısı geri kazanımı → kabin HVAC | 180,000 | 320,000 | 0.6 |
| 2 | Kabin hava resirkülasyonu artırma (%30→%70) | 120,000 | 280,000 | 0.4 |
| 3 | Fırın yalıtım iyileştirme | 60,000 | 85,000 | 0.7 |
| 4 | Basınçlı hava optimizasyonu (kaçak + basınç) | 25,000 | 150,000 | 0.2 |
| 5 | LED aydınlatma (tüm fabrika) | 200,000 | 180,000 | 1.1 |
| 6 | Chiller free cooling (ekonomizer modu) | 50,000 | 95,000 | 0.5 |
| 7 | Robot standby enerji yönetimi | 15,000 | 45,000 | 0.3 |
| **TOPLAM** | | **€650,000** | **€1,155,000** | **0.56** |

### Sonuçlar

```
Toplam enerji tasarrufu: 12,500 MWh/yıl (%8.5)
Toplam maliyet tasarrufu: €1,155,000/yıl
SEC: 1,720 → 1,570 kWh/araç (%8.7 azalma)
Fabrika exergy verimi: %21 → %25 (%19 artış)
CO₂ azaltma: 4,200 tCO₂/yıl
NPV (10 yıl, %10): €6,400,000
```

### Çıkarılan Dersler

1. Boyahane HVAC ve RTO ısı entegrasyonu en büyük tasarruf kaynağı
2. Kabin hava resirkülasyonu boya kalitesini etkilemeden enerji tasarrufu sağladı
3. Robot standby yönetimi düşük maliyetli ama etkili — üretim durağanlarında %60 güç azalması
4. Free cooling (kış aylarında dış hava ile soğutma) Türkiye kuzey bölgelerinde etkili

---

## Sektörler Arası Karşılaştırma

### Özet Tablo

| Vaka | Sektör | Yatırım [€] | Tasarruf [€/yıl] | SPP [yıl] | η_ex Artış |
|---|---|---|---|---|---|
| 1 | Tekstil | 285,000 | 310,800 | 0.92 | %18.5 → %24.2 |
| 2 | Gıda | 150,000 | 105,000 | 1.43 | %16.2 → %21.8 |
| 3 | Kimya | 158,000 | 565,000 | 0.28 | %32.0 → %41.0 |
| 4 | Çimento | 12,500,000 | 4,125,000 | 3.03 | %28.0 → %34.0 |
| 5 | Metal | 245,000 | 257,000 | 0.95 | %22.0 → %29.0 |
| 6 | Otomotiv | 650,000 | 1,155,000 | 0.56 | %21.0 → %25.0 |

### Ortak Başarı Faktörleri

```
1. Exergy analizi: Tüm vakalarda geleneksel enerji analizinin ötesinde
   fırsatlar ortaya koydu (özellikle ısı entegrasyonu)

2. Faz yaklaşımı: Hızlı kazanımlarla başlayıp güven inşa etmek
   büyük yatırımlar için yönetim desteğini kolaylaştırdı

3. Ölçüm: Detaylı ölçüm ve profilleme, tahminlerin
   doğruluğunu artırdı (gerçekleşme oranı: %85-110)

4. Operatör katılımı: Teknik personelin dahil edilmesi
   hem uygulama hem sürdürülebilirlik için kritik

5. M&V: Uygulama sonrası ölçüm ve doğrulama, tasarrufların
   belgelenmesini ve gelecek yatırımlar için referans oluşturulmasını sağladı
```

### Sektörel Öncelik Haritası

| Sektör | En Etkili 1. Önlem | En Etkili 2. Önlem | En Etkili 3. Önlem |
|---|---|---|---|
| Tekstil | Boyahane atık su ısı geri kazanımı | Kondensat geri dönüş | Kazan optimizasyonu |
| Gıda | Soğutma-ısıtma entegrasyonu | Kazan economizer | Soğuk depo optimizasyonu |
| Kimya | Pinch analizi tabanlı ısı entegrasyonu | Proses optimizasyonu | CHP değerlendirme |
| Çimento | ORC atık ısı elektrik üretimi | Alternatif yakıt | Öğütme optimizasyonu |
| Metal | Fırın yalıtım/brülör | Basınçlı hava kaçak | Fırın kontrol modernizasyonu |
| Otomotiv | Boyahane HVAC optimizasyonu | RTO ısı geri kazanımı | Basınçlı hava |

## İlgili Dosyalar

- [Fabrika Benchmarkları](factory_benchmarks.md) — Sektörel SEC ve exergy verileri
- [Metodoloji](methodology.md) — Audit süreci ve raporlama
- [Ekonomik Analiz](economic_analysis.md) — NPV, IRR hesaplamaları
- [Pinch Analizi](pinch_analysis.md) — Isı entegrasyonu metodolojisi
- [Atık Isı Geri Kazanımı](waste_heat_recovery.md) — WHR teknolojileri
- [Ekipmanlar Arası Optimizasyon](cross_equipment.md) — Entegrasyon fırsatları
- [Sektörel Dosyalar](sector_textile.md) — Her sektörün detaylı profili
- [Ölçüm ve Doğrulama](measurement_verification.md) — IPMVP protokolleri

## Referanslar

- US DOE Industrial Assessment Center (IAC) Database, iac.university
- Carbon Trust, "Industrial Energy Efficiency Case Studies"
- IEA, "Energy Technology Perspectives — Industry Chapter"
- EU BREF Documents — Sectoral Best Available Techniques
- YEGM, "Verimlilik Artırıcı Proje (VAP) Örnekleri"
- Türkiye Sanayi ve Teknoloji Bakanlığı, "Sektörel Enerji Verimlilik Raporları"
- COGEN Europe, "CHP Case Studies Database"
- UNIDO, "Industrial Energy Efficiency — Good Practice Cases"
