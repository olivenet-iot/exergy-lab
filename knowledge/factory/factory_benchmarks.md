---
title: "Fabrika Seviyesi Benchmark Verileri (Factory-Level Benchmark Data)"
category: factory
equipment_type: factory
keywords: [benchmark, fabrika, sektör, karşılaştırma]
related_files: [factory/performance_indicators.md, factory/kpi_definitions.md, factory/methodology.md]
use_when: ["Fabrika enerji performansı değerlendirilirken", "Sektör kıyaslaması yapılırken"]
priority: high
last_updated: 2026-01-31
---
# Fabrika Seviyesi Benchmark Verileri (Factory-Level Benchmark Data)

> Son güncelleme: 2026-01-31

## Genel Bakış

Fabrika seviyesinde enerji performansının değerlendirilmesi, sektörel benchmark verileriyle karşılaştırma yapılmasını gerektirir. Bu dosya; Türkiye'deki başlıca sanayi sektörleri için spesifik enerji tüketimi (SEC), exergy verimliliği, enerji kaynak dağılımı, karbon yoğunluğu ve performans sınıflandırma verilerini kapsamlı bir şekilde sunar. Tüm veriler EU BREF referans değerleri, US DOE IAC veritabanı istatistikleri ve Türkiye YEGM (Yenilenebilir Enerji Genel Müdürlüğü) verileriyle tutarlıdır.

Benchmark karşılaştırması, enerji audit çalışmalarında tespit edilen iyileştirme potansiyellerinin doğrulanması ve hedef belirlenmesi için temel araçtır. Sektörel karşılaştırma yapılırken üretim tipi, kapasite kullanım oranı, iklim koşulları ve hammadde farklılıkları mutlaka dikkate alınmalıdır.

## 1. Tekstil Sektörü (Textile Industry)

### 1.1 Alt Proses Bazında Spesifik Enerji Tüketimi (SEC)

| Alt Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim | Not |
|---|---|---|---|---|---|---|
| İplik (Ring) | 2.0 | 3.5 | 2.8 | <2.0 | kWh/kg iplik | Ring eğirme, Ne 30 bazında |
| İplik (Open-End) | 1.5 | 2.8 | 2.0 | <1.5 | kWh/kg iplik | OE eğirme, daha verimli |
| İplik (Kompakt) | 2.2 | 4.0 | 3.0 | <2.2 | kWh/kg iplik | Kompakt iplik, ek aspirasyon |
| Dokuma (Rapier) | 0.6 | 1.2 | 0.8 | <0.6 | kWh/kg kumaş | Rapier dokuma makinesi |
| Dokuma (Airjet) | 1.0 | 2.5 | 1.5 | <1.0 | kWh/kg kumaş | Basınçlı hava ihtiyacı yüksek |
| Örme (Yuvarlak) | 0.4 | 0.8 | 0.6 | <0.4 | kWh/kg kumaş | Yuvarlak örme |
| Boyama (Jet) | 6.0 | 15.0 | 10.0 | <6.0 | kWh/kg kumaş | Termal + elektrik toplam |
| Boyama (Pad-Batch) | 3.0 | 8.0 | 5.0 | <3.0 | kWh/kg kumaş | Soğuk pad-batch dahil |
| Boyama (Overflow) | 8.0 | 25.0 | 15.0 | <8.0 | kWh/kg kumaş | Yüksek flotte oranı |
| Terbiye (Kurutma) | 4.0 | 12.0 | 7.0 | <4.0 | kWh/kg kumaş | Ram/stenter |
| Terbiye (Apre) | 2.0 | 6.0 | 4.0 | <2.0 | kWh/kg kumaş | Kimyasal terbiye |
| Terbiye (Sanfor) | 1.5 | 4.0 | 2.5 | <1.5 | kWh/kg kumaş | Mekanik çekme kontrolü |
| Yıkama | 3.0 | 10.0 | 6.0 | <3.0 | kWh/kg kumaş | Sıcak yıkama prosesleri |
| Baskı (Rotary) | 1.5 | 5.0 | 3.0 | <1.5 | kWh/kg kumaş | Rotary baskı |
| Baskı (Dijital) | 0.8 | 2.5 | 1.5 | <0.8 | kWh/kg kumaş | Dijital baskı |

### 1.2 Tekstil Sektörü Toplam SEC Değerleri

```
Entegre Tekstil Fabrikası (İplik → Kumaş → Terbiye):
- En iyi uygulama: 8-12 kWh/kg mamul kumaş
- Sektör ortalaması: 15-25 kWh/kg mamul kumaş
- Düşük performans: >30 kWh/kg mamul kumaş

Burada:
- Elektrik payı: %40-55 (toplam enerjinin)
- Termal enerji payı: %45-60 (doğalgaz/kömür)
- Su tüketimi: 50-200 L/kg kumaş (boyama tipine bağlı)
- Buhar tüketimi: 5-15 kg buhar/kg kumaş

Örnek — Orta ölçekli terbiye fabrikası:
Yıllık üretim: 8,000 ton kumaş
Elektrik: 12,000,000 kWh/yıl → 1.50 kWh/kg
Doğalgaz: 3,200,000 Nm³/yıl × 10.33 kWh/Nm³ = 33,056,000 kWh/yıl → 4.13 kWh/kg
Kömür: 2,500 ton/yıl × 7,000 kWh/ton = 17,500,000 kWh/yıl → 2.19 kWh/kg
SEC_toplam = 1.50 + 4.13 + 2.19 = 7.82 kWh/kg (birincil enerji bazlı)
```

### 1.3 Tekstil Sektörü Performans Sınıflandırması

| Performans | SEC Aralığı [kWh/kg] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | <10 | >18 | Mevcut durumu koru, sektöre öncülük |
| İyi | 10-15 | 14-18 | Optimizasyon ve ince ayar |
| Ortalama | 15-22 | 10-14 | Sistematik enerji yönetimi başlat |
| Düşük | 22-30 | 6-10 | Kapsamlı iyileştirme programı |
| Kritik | >30 | <6 | Acil müdahale, ekipman yenileme |

## 2. Gıda Sektörü (Food Industry)

### 2.1 Alt Proses Bazında SEC

| Alt Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim | Not |
|---|---|---|---|---|---|---|
| Süt işleme (pastörizasyon) | 0.06 | 0.12 | 0.08 | <0.06 | kWh/L süt | UHT daha yüksek |
| Süt işleme (UHT) | 0.10 | 0.25 | 0.15 | <0.10 | kWh/L süt | Ultra-yüksek sıcaklık |
| Süt tozu | 0.50 | 1.20 | 0.80 | <0.50 | kWh/L süt eşd. | Buharlaştırma + kurutma |
| Peynir | 0.15 | 0.40 | 0.25 | <0.15 | kWh/L süt eşd. | Salamura dahil |
| Bira üretimi | 20 | 50 | 30 | <20 | kWh/hL bira | Modern bira fabrikası |
| Bira (eski tesis) | 40 | 80 | 55 | <40 | kWh/hL bira | Geleneksel proses |
| Et işleme | 0.40 | 1.10 | 0.70 | <0.40 | kWh/kg et | Kesim + parçalama |
| Et işleme (şarküteri) | 0.80 | 2.00 | 1.20 | <0.80 | kWh/kg ürün | Pişirme + soğutma |
| Ekmek (fırın) | 0.30 | 0.55 | 0.40 | <0.30 | kWh/kg ekmek | Endüstriyel fırın |
| Ekmek (artizanal) | 0.50 | 0.80 | 0.60 | <0.50 | kWh/kg ekmek | Küçük ölçekli |
| Bisküvi/Kraker | 0.40 | 0.80 | 0.55 | <0.40 | kWh/kg ürün | Sürekli fırın |
| Meyve suyu | 0.10 | 0.30 | 0.18 | <0.10 | kWh/L | Pastörizasyon + dolum |
| Dondurulmuş gıda | 0.30 | 0.80 | 0.50 | <0.30 | kWh/kg ürün | Dondurma enerjisi yoğun |
| Şeker | 200 | 400 | 280 | <200 | kWh/ton pancar | Kampanya dönemi |
| Bitkisel yağ | 150 | 350 | 230 | <150 | kWh/ton tohum | Ekstraksiyon + rafinasyon |

### 2.2 Gıda Sektörü Enerji Dağılımı

```
Tipik gıda fabrikası enerji dağılımı:

Termal enerji: %55-70
  - Buhar/sıcak su üretimi: %30-45
  - Pişirme/kurutma prosesleri: %15-25
  - Temizlik (CIP): %5-10

Elektrik: %30-45
  - Soğutma/dondurma: %10-20
  - Basınçlı hava: %5-8
  - Pompa/fan: %5-10
  - Aydınlatma: %3-5
  - Paketleme: %3-8

Su tüketimi: 2-10 m³/ton ürün (alt sektöre bağlı)
```

### 2.3 Gıda Sektörü Performans Sınıflandırması

| Performans | Genel SEC Konumu | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | < Best practice değeri | >15 | Referans tesis, bilgi paylaşımı |
| İyi | Best practice — ortalama arası | 10-15 | İnce ayar, proses optimizasyonu |
| Ortalama | Sektör ortalaması ±%15 | 7-10 | Isı geri kazanımı, izolasyon iyileştirme |
| Düşük | > Sektör ortalaması + %15 | 4-7 | Kapsamlı audit ve yatırım planı |
| Kritik | > Sektör ortalaması + %40 | <4 | Acil müdahale, proses yenileme |

## 3. Çimento Sektörü (Cement Industry)

### 3.1 Proses Bazında SEC

| Alt Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim |
|---|---|---|---|---|---|
| Elektrik — Toplam | 80 | 110 | 90 | <80 | kWh/ton çimento |
| Elektrik — Hammadde öğütme | 15 | 25 | 18 | <15 | kWh/ton hammadde |
| Elektrik — Klinker pişirme | 20 | 35 | 25 | <20 | kWh/ton klinker |
| Elektrik — Çimento öğütme | 25 | 45 | 32 | <25 | kWh/ton çimento |
| Elektrik — Diğer (fan, konveyör) | 15 | 25 | 18 | <15 | kWh/ton çimento |
| Termal — Klinker pişirme (toplam) | 2,700 | 3,500 | 3,000 | <2,700 | MJ/ton klinker |
| Termal — Kuru proses | 2,700 | 3,200 | 2,900 | <2,700 | MJ/ton klinker |
| Termal — Yarı-kuru | 3,000 | 3,600 | 3,200 | <3,000 | MJ/ton klinker |
| Termal — Yaş proses | 4,200 | 5,800 | 4,800 | <4,200 | MJ/ton klinker |

### 3.2 Çimento Üretim Teknolojisi Karşılaştırması

```
Proses teknolojisi etkisi:

Kuru proses (modern, ön kalsinatörlü):
  Termal: 2,700-3,200 MJ/ton klinker
  Elektrik: 80-100 kWh/ton çimento
  Klinker/çimento oranı: 0.70-0.85

Yarı-kuru proses (Lepol):
  Termal: 3,000-3,600 MJ/ton klinker
  Elektrik: 85-110 kWh/ton çimento
  Klinker/çimento oranı: 0.75-0.90

Yaş proses (eski tesisler):
  Termal: 4,200-5,800 MJ/ton klinker
  Elektrik: 90-140 kWh/ton çimento
  Klinker/çimento oranı: 0.80-0.95

Klinker/çimento oranının düşürülmesi:
- Cüruf (GGBS) katkısı: %20-70 → CEM III
- Uçucu kül katkısı: %15-35 → CEM IV
- Kalker katkısı: %6-35 → CEM II
- Her %1 düşüş ≈ %0.8-1.0 termal enerji tasarrufu (toplam bazda)
```

### 3.3 Çimento Sektörü Alternatif Yakıt Kullanımı

| Alternatif Yakıt | Enerji İçeriği [MJ/kg] | Tipik İkame Oranı [%] | Maliyet Avantajı | Not |
|---|---|---|---|---|
| Atık lastik (TDF) | 28-35 | 5-20 | %30-50 | Demir içeriği faydalı |
| Atık yağ | 30-40 | 5-15 | %20-40 | Özel besleme sistemi |
| Endüstriyel atık (RDF) | 12-20 | 10-40 | %40-60 | Kalori stabilizasyonu önemli |
| Biyokütle (tarımsal) | 14-18 | 5-15 | %20-30 | Kül içeriğine dikkat |
| Çözücü atıkları | 20-30 | 3-10 | %30-50 | Klor sınırlaması |
| Atık su arıtma çamuru | 3-8 | 2-8 | Bertaraf geliri | Nem içeriği kritik |

### 3.4 Çimento Sektörü Performans Sınıflandırması

| Performans | Termal SEC [MJ/ton klinker] | Elektrik SEC [kWh/ton] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|---|
| Mükemmel | <2,800 | <85 | >35 | Referans tesis |
| İyi | 2,800-3,200 | 85-100 | 28-35 | Modern proses, ince ayar |
| Ortalama | 3,200-3,800 | 100-120 | 20-28 | Modernizasyon planla |
| Düşük | 3,800-4,500 | 120-140 | 15-20 | Kapsamlı yatırım gerekli |
| Kritik | >4,500 | >140 | <15 | Proses dönüşümü veya kapatma |

## 4. Kimya Sektörü (Chemical Industry)

### 4.1 Alt Proses Bazında SEC

| Ürün/Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim |
|---|---|---|---|---|---|
| Amonyak (doğalgaz bazlı) | 28 | 36 | 31 | <28 | GJ/ton NH₃ |
| Üre | 3.5 | 5.5 | 4.2 | <3.5 | GJ/ton üre |
| Klor-alkali (membran) | 2,200 | 2,800 | 2,400 | <2,200 | kWh/ton Cl₂ |
| Klor-alkali (diyafram) | 2,800 | 3,500 | 3,000 | <2,800 | kWh/ton Cl₂ |
| Etilen (buhar kraking) | 14 | 20 | 16 | <14 | GJ/ton etilen |
| PVC | 3.0 | 5.5 | 4.0 | <3.0 | GJ/ton PVC |
| Polietilen (HDPE) | 2.5 | 4.5 | 3.2 | <2.5 | GJ/ton PE |
| Polipropilen | 2.0 | 4.0 | 2.8 | <2.0 | GJ/ton PP |
| Soda (Solvay) | 9.0 | 14.0 | 11.0 | <9.0 | GJ/ton Na₂CO₃ |
| Cam (düzcam) | 5.5 | 8.5 | 6.5 | <5.5 | GJ/ton cam |
| Cam (ambalaj) | 4.5 | 7.5 | 5.5 | <4.5 | GJ/ton cam |
| Gübre (NPK) | 1.5 | 3.0 | 2.0 | <1.5 | GJ/ton NPK |
| Boya/Kaplama | 1.0 | 3.0 | 1.8 | <1.0 | GJ/ton boya |
| İlaç | 50 | 150 | 80 | <50 | kWh/kg API |

### 4.2 Kimya Sektörü Performans Sınıflandırması

| Performans | Genel SEC Konumu | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | < EU BREF alt sınır | >40 | Dünya sınıfı tesis |
| İyi | BREF alt — ortalama arası | 30-40 | Modern proses, sürekli iyileştirme |
| Ortalama | BREF ortalama ±%10 | 22-30 | Isı entegrasyonu ve proses optimizasyonu |
| Düşük | > BREF ortalama + %10 | 15-22 | Pinch analizi, kapsamlı proses revizyonu |
| Kritik | > BREF ortalama + %30 | <15 | Proses yenileme veya kapasite artışı |

## 5. Metal Sektörü (Metal Industry)

### 5.1 Alt Proses Bazında SEC

| Alt Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim |
|---|---|---|---|---|---|
| Çelik — EAF (Electric Arc Furnace) | 400 | 550 | 450 | <400 | kWh/ton sıvı çelik |
| Çelik — BOF (Basic Oxygen Furnace) | 150 | 250 | 180 | <150 | kWh/ton + 18 GJ/ton |
| Çelik — Haddeleme (sıcak) | 1,200 | 2,000 | 1,500 | <1,200 | MJ/ton ürün |
| Çelik — Haddeleme (soğuk) | 400 | 800 | 550 | <400 | MJ/ton ürün |
| Çelik — Dövme | 300 | 500 | 380 | <300 | kWh/ton ürün |
| Çelik — Dövme (açık kalıp) | 400 | 600 | 480 | <400 | kWh/ton ürün |
| Alüminyum — Elektroliz (Hall-Héroult) | 13,000 | 15,000 | 13,800 | <13,000 | kWh/ton Al |
| Alüminyum — Sekonder (hurda) | 500 | 1,200 | 750 | <500 | kWh/ton Al |
| Alüminyum — Ekstrüzyon | 800 | 1,500 | 1,000 | <800 | kWh/ton profil |
| Bakır — Elektrolitik rafinasyon | 300 | 500 | 380 | <300 | kWh/ton Cu |
| Döküm (demir) | 500 | 900 | 650 | <500 | kWh/ton döküm |
| Döküm (alüminyum) | 700 | 1,400 | 950 | <700 | kWh/ton döküm |
| Isıl işlem | 200 | 500 | 300 | <200 | kWh/ton ürün |
| Galvaniz (sıcak daldırma) | 300 | 600 | 420 | <300 | kWh/ton ürün |

### 5.2 Metal Sektörü Fırın Verimlilikleri

```
Endüstriyel fırın tipleri ve verim aralıkları:

| Fırın Tipi          | Düşük | Ortalama | İyi  | Birim |
|---------------------|-------|----------|------|-------|
| Ark ocağı (EAF)    | 45%   | 55%      | 65%  | η_th  |
| İndüksiyon ocağı    | 55%   | 65%      | 75%  | η_th  |
| Gaz yakıtlı tav fırını | 25% | 40%    | 55%  | η_th  |
| Rejenertif fırın    | 40%   | 55%      | 70%  | η_th  |
| Elektrikli direnç fırını | 60% | 75%   | 85%  | η_th  |

Fırın exergy verimlilikleri (tipik):
- Yüksek sıcaklık (>1000°C): Exergy verimi %25-45
- Orta sıcaklık (400-1000°C): Exergy verimi %15-30
- Düşük sıcaklık (<400°C): Exergy verimi %5-15
```

### 5.3 Metal Sektörü Performans Sınıflandırması

| Performans | EAF SEC [kWh/ton] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | <420 | >30 | En iyi teknoloji, referans |
| İyi | 420-480 | 24-30 | Modern EAF, ince ayar |
| Ortalama | 480-550 | 18-24 | Hurda ön ısıtma, enerji yönetimi |
| Düşük | 550-650 | 12-18 | Kapsamlı modernizasyon |
| Kritik | >650 | <12 | EAF yenileme veya dönüşüm |

## 6. Kağıt Sektörü (Pulp and Paper Industry)

### 6.1 Alt Proses Bazında SEC

| Alt Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim |
|---|---|---|---|---|---|
| Selüloz — Kraft (kimyasal) | 1,500 | 2,200 | 1,800 | <1,500 | kWh/ton selüloz (elektrik) |
| Selüloz — Kraft (termal) | 10 | 15 | 12 | <10 | GJ/ton selüloz |
| Selüloz — Mekanik (TMP) | 2,000 | 3,000 | 2,400 | <2,000 | kWh/ton selüloz |
| Selüloz — Geri dönüşüm | 300 | 600 | 400 | <300 | kWh/ton selüloz |
| Kağıt — Gazete kağıdı (elektrik) | 400 | 600 | 480 | <400 | kWh/ton kağıt |
| Kağıt — Gazete kağıdı (termal) | 4.0 | 6.5 | 5.0 | <4.0 | GJ/ton kağıt |
| Kağıt — Yazı/baskı (elektrik) | 500 | 800 | 600 | <500 | kWh/ton kağıt |
| Kağıt — Yazı/baskı (termal) | 5.0 | 8.0 | 6.0 | <5.0 | GJ/ton kağıt |
| Kağıt — Ambalaj (elektrik) | 350 | 600 | 450 | <350 | kWh/ton kağıt |
| Kağıt — Ambalaj (termal) | 4.0 | 7.0 | 5.0 | <4.0 | GJ/ton kağıt |
| Kağıt — Tissue (elektrik) | 600 | 1,000 | 750 | <600 | kWh/ton kağıt |
| Kağıt — Tissue (termal) | 5.5 | 9.0 | 7.0 | <5.5 | GJ/ton kağıt |
| Kurutma seksiyonu | 3.0 | 5.5 | 4.0 | <3.0 | GJ/ton kağıt |
| Presleme | 30 | 55 | 40 | <30 | kWh/ton kağıt |

### 6.2 Kağıt Sektörü Enerji Akışı

```
Entegre kağıt fabrikası enerji dengesi örneği:

Girdi:
  Doğalgaz: 5,500 TJ/yıl
  Satın alınan elektrik: 150 GWh/yıl
  Biyokütle (siyah likör): 3,200 TJ/yıl
  Toplam birincil enerji: ~9,240 TJ/yıl

Dönüşüm:
  CHP (kojenerasyon): 350 MWth buhar + 80 MWe elektrik
  Geri kazanım kazanı: 200 MWth (siyah likör)

Tüketim dağılımı:
  Kurutma: %40-50 (termal enerjinin)
  Buharlaştırma (siyah likör): %15-20
  Pişirme (kraft): %10-15
  Mekanik tahrik: %20-30 (elektriğin)
  Pompa/fan: %15-25
  Aydınlatma/HVAC: %5-10

Üretim: 400,000 ton/yıl yazı kağıdı
SEC_elektrik = 600 kWh/ton
SEC_termal = 6.5 GJ/ton
SEC_toplam = 8.66 GJ/ton
```

### 6.3 Kağıt Sektörü Performans Sınıflandırması

| Performans | Elektrik SEC [kWh/ton] | Termal SEC [GJ/ton] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|---|
| Mükemmel | <450 | <4.5 | >28 | CHP entegrasyonu mükemmel |
| İyi | 450-600 | 4.5-6.0 | 22-28 | İyi proses kontrolü |
| Ortalama | 600-750 | 6.0-7.5 | 16-22 | Kurutma ve presleme optimizasyonu |
| Düşük | 750-950 | 7.5-9.0 | 10-16 | Kapsamlı enerji programı |
| Kritik | >950 | >9.0 | <10 | Proses modernizasyonu şart |

## 7. Otomotiv Sektörü (Automotive Industry)

### 7.1 Alt Proses Bazında SEC

| Alt Proses | Düşük (Best Practice) | Ortalama | İyi | Mükemmel | Birim |
|---|---|---|---|---|---|
| Boyahane (toplam) | 1,000 | 1,500 | 1,200 | <1,000 | kWh/araç |
| Boyahane — Ön işlem (fosfat) | 80 | 150 | 100 | <80 | kWh/araç |
| Boyahane — Elektrokaplama (E-coat) | 60 | 120 | 80 | <60 | kWh/araç |
| Boyahane — Astar (primer) | 150 | 300 | 200 | <150 | kWh/araç |
| Boyahane — Üst kat boya | 200 | 400 | 280 | <200 | kWh/araç |
| Boyahane — Vernik (clearcoat) | 150 | 300 | 200 | <150 | kWh/araç |
| Boyahane — Kurutma fırınları | 300 | 500 | 380 | <300 | kWh/araç |
| Gövde kaynak (BIW) | 250 | 500 | 350 | <250 | kWh/araç |
| Pres (damgalama) | 150 | 350 | 220 | <150 | kWh/araç |
| Montaj hattı | 200 | 400 | 280 | <200 | kWh/araç |
| HVAC (fabrika iklimlendirme) | 200 | 500 | 300 | <200 | kWh/araç |
| Basınçlı hava | 100 | 250 | 150 | <100 | kWh/araç |
| Aydınlatma | 50 | 120 | 70 | <50 | kWh/araç |
| Motor/transmisyon işleme | 300 | 700 | 450 | <300 | kWh/araç |

### 7.2 Otomotiv Sektörü Toplam SEC

```
Otomotiv fabrikası toplam enerji tüketimi:

Toplam SEC:
- En iyi uygulama: 1,800-2,500 kWh/araç
- Sektör ortalaması: 3,000-4,500 kWh/araç
- Düşük performans: >5,000 kWh/araç

Enerji dağılımı (tipik):
  Boyahane: %50-60 (en enerji yoğun bölüm)
  Gövde kaynak (BIW): %12-18
  Pres: %5-10
  Montaj: %8-15
  Yardımcı tesisler: %10-20

Boyahane detay:
  Termal enerji (kurutma fırınları, ön işlem): %65-75
  Elektrik (HVAC, pompa, robot): %25-35
  VOC yakma (RTO/TAR): Termal enerjinin %15-25'i
```

### 7.3 Otomotiv Sektörü Performans Sınıflandırması

| Performans | Toplam SEC [kWh/araç] | Exergy Verimi [%] | Aksiyon |
|---|---|---|---|
| Mükemmel | <2,200 | >20 | Lean enerji yönetimi, benchmark |
| İyi | 2,200-3,000 | 15-20 | Modern boyahane, VSD yaygın |
| Ortalama | 3,000-4,000 | 10-15 | Boyahane modernizasyonu planla |
| Düşük | 4,000-5,500 | 6-10 | Kapsamlı yatırım programı |
| Kritik | >5,500 | <6 | Tesis yenileme değerlendir |

## 8. Sektörler Arası Karşılaştırmalı Analiz

### 8.1 Fabrika Exergy Verimliliği Sektörel Karşılaştırma

| Sektör | Düşük [%] | Ortalama [%] | İyi [%] | Mükemmel [%] | En İyi Uygulama [%] |
|---|---|---|---|---|---|
| Tekstil | <6 | 6-10 | 10-15 | 15-20 | >20 |
| Gıda | <5 | 5-8 | 8-12 | 12-16 | >16 |
| Çimento | <15 | 15-22 | 22-30 | 30-38 | >38 |
| Kimya | <15 | 15-25 | 25-35 | 35-45 | >45 |
| Metal (EAF çelik) | <12 | 12-20 | 20-28 | 28-35 | >35 |
| Kağıt | <10 | 10-18 | 18-24 | 24-30 | >30 |
| Otomotiv | <6 | 6-12 | 12-18 | 18-22 | >22 |
| Seramik | <8 | 8-15 | 15-22 | 22-28 | >28 |
| Cam | <12 | 12-20 | 20-28 | 28-35 | >35 |
| Plastik | <8 | 8-14 | 14-20 | 20-25 | >25 |

### 8.2 Enerji Kaynak Dağılımı (Sektörel)

| Sektör | Elektrik [%] | Doğalgaz [%] | Kömür [%] | Diğer [%] | Not |
|---|---|---|---|---|---|
| Tekstil | 40-55 | 30-45 | 5-15 | 5-10 | Kömür payı Türkiye'de yüksek |
| Gıda | 35-50 | 40-55 | 0-5 | 5-15 | Biyokütle potansiyeli |
| Çimento | 10-15 | 5-20 | 40-60 | 15-35 | Alternatif yakıtlar artıyor |
| Kimya | 25-40 | 40-60 | 5-15 | 5-15 | Feedstock hariç |
| Metal | 50-80 | 15-35 | 0-10 | 5-15 | EAF elektrik yoğun |
| Kağıt | 25-40 | 30-45 | 0-5 | 25-40 | Biyokütle (siyah likör) |
| Otomotiv | 35-50 | 40-55 | 0-5 | 5-10 | Boyahane gaz yoğun |
| Seramik | 20-35 | 50-70 | 0-5 | 5-15 | Fırın gaz ağırlıklı |

### 8.3 Karbon Yoğunluğu (Sektörel)

| Sektör | Düşük [kgCO₂/ton] | Ortalama [kgCO₂/ton] | Yüksek [kgCO₂/ton] | Birim Bazı | Not |
|---|---|---|---|---|---|
| Tekstil | 2,500 | 5,000 | 8,000 | ton kumaş | Boyama yoğunluğuna bağlı |
| Gıda (süt) | 30 | 60 | 100 | 1000 L süt | CIP ve pastörizasyon |
| Çimento | 550 | 700 | 900 | ton çimento | Proses CO₂ dahil (~%60) |
| Kimya (amonyak) | 1,500 | 2,000 | 2,800 | ton NH₃ | Feedstock CO₂ dahil |
| Çelik (EAF) | 200 | 400 | 600 | ton çelik | Grid emisyon faktörüne bağlı |
| Çelik (BOF) | 1,600 | 2,000 | 2,400 | ton çelik | Kok + demir cevheri |
| Kağıt | 300 | 600 | 1,000 | ton kağıt | CHP ve biyokütle avantajı |
| Otomotiv | 400 | 800 | 1,200 | araç | Boyahane dominant |
| Cam | 500 | 800 | 1,200 | ton cam | Soda dekompozisyonu dahil |
| Alüminyum (primer) | 6,000 | 10,000 | 16,000 | ton Al | Elektrik kaynağına bağlı |

### 8.4 EU BREF ve Uluslararası Referans Değerler

```
Avrupa Birliği En İyi Mevcut Teknikler (BAT — Best Available Techniques):

Çimento:
  BAT-AEL termal: 2,900-3,300 MJ/ton klinker (kuru proses)
  BAT-AEL elektrik: 80-100 kWh/ton çimento
  Referans: BREF Cement, Lime and Magnesium Oxide (2013)

Cam:
  BAT-AEL düzcam: 5.0-8.0 GJ/ton cam
  BAT-AEL ambalaj camı: 3.5-6.5 GJ/ton cam
  Referans: BREF Glass Manufacturing (2013)

Demir-Çelik:
  BAT-AEL EAF: 350-500 kWh/ton sıvı çelik
  BAT-AEL kok fırını: 3.6-4.0 GJ/ton kok
  Referans: BREF Iron and Steel Production (2012)

Kağıt:
  BAT-AEL kraft selüloz: 10-14 GJ/ton ADt
  BAT-AEL ince kağıt: 4.0-7.0 GJ/ton
  Referans: BREF Pulp and Paper (2015)

US DOE IAC Database İstatistikleri:
  - 19,000+ audit tamamlandı
  - Ortalama tasarruf: Toplam enerji maliyetinin %8-12'si
  - En yaygın fırsat: Atık ısı geri kazanımı (%22)
  - İkinci: Enerji yönetimi ve kontrol (%18)
  - Üçüncü: Motor/tahrik sistemleri (%15)

Türkiye YEGM Verileri:
  - Zorunlu enerji etüdü sınırı: 1,000 TEP/yıl
  - Ortalama belirlenen tasarruf: Toplam tüketimin %15-20'si
  - Uygulanan tasarruf oranı: Belirlenenin %40-60'ı
  - En yüksek tasarruf sektörleri: Tekstil (%18), çimento (%12), metal (%15)
```

## 9. Benchmark Karşılaştırma Metodolojisi

### 9.1 Normalize Etme Prosedürü

```
Fabrikalar arası adil karşılaştırma için normalizasyon:

SEC_normalize = SEC_gerçek × CF_kapasite × CF_ürün × CF_iklim × CF_hammadde

Burada:
- CF_kapasite = Kapasite kullanım oranı düzeltmesi
  CF_kapasite = (KKO_referans / KKO_gerçek)^α
  α = 0.2-0.4 (sektöre bağlı ölçek faktörü)

- CF_ürün = Ürün karmasının karmaşıklık düzeltmesi
  CF_ürün = Σ(wi × SECi_referans) / Σ(wi × SECi_gerçek)
  wi = ürün i'nin üretim payı

- CF_iklim = İklim koşulları düzeltmesi
  CF_iklim = HDD_referans / HDD_gerçek (ısıtma yoğun tesisler için)
  CF_iklim = CDD_referans / CDD_gerçek (soğutma yoğun tesisler için)

- CF_hammadde = Hammadde kalitesi düzeltmesi
  (çimento: nem, kimyasal bileşim; kağıt: lif kalitesi; metal: hurda kalitesi)

Örnek — Çimento fabrikası normalizasyonu:
SEC_gerçek = 3,400 MJ/ton klinker
KKO = %72 (referans: %85)
CF_kapasite = (0.85/0.72)^0.3 = 1.05
SEC_normalize = 3,400 × 1.05 = 3,570 MJ/ton
→ Düşük kapasite kullanımı SEC'i artırır, normalizasyon bu etkiyi düzeltir.
```

### 9.2 Benchmark Veri Kaynakları

| Kaynak | Kapsam | Güncelleme | Erişim | Güvenilirlik |
|---|---|---|---|---|
| EU BREF/BAT | Avrupa, sektörel | 8-10 yılda bir | Ücretsiz, online | Çok yüksek |
| US DOE IAC | ABD, tüm sektörler | Sürekli | Ücretsiz, online | Yüksek |
| IEA Energy Technology Perspectives | Küresel | Yıllık | Ücretli | Çok yüksek |
| YEGM Enerji Etüdü DB | Türkiye | Yıllık | Kısıtlı | Orta-yüksek |
| UNIDO Benchmarking | Gelişmekte olan ülkeler | Proje bazlı | Ücretsiz | Orta |
| Solomon (rafineri) | Küresel rafineriler | Yıllık | Ücretli | Çok yüksek |
| ENERGY STAR (EPA) | ABD endüstri | Yıllık | Ücretsiz | Yüksek |

## İlgili Dosyalar

- [KPI Tanımları](kpi_definitions.md) — Performans göstergeleri detayları
- [Performans Göstergeleri](performance_indicators.md) — Hedef belirleme ve izleme
- [Metodoloji](methodology.md) — Audit metodolojisi ve seviyeleri
- [Ekonomik Analiz](economic_analysis.md) — Yatırım değerlendirme
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy verimlilik hesaplama
- [Sistem Sınırları](system_boundaries.md) — Fabrika sınır tanımları
- [Kazan Benchmarkları](../boiler/benchmarks.md) — Kazan exergy verim aralıkları
- [Kompresör Benchmarkları](../compressor/benchmarks.md) — Kompresör verim aralıkları
- [Chiller Benchmarkları](../chiller/benchmarks.md) — Chiller COP ve exergy verileri

## Referanslar

- European Commission, "Best Available Techniques (BAT) Reference Documents," JRC IPTS, https://eippcb.jrc.ec.europa.eu/reference
- US DOE, "Industrial Assessment Centers (IAC) Database," https://iac.university
- IEA, "Energy Technology Perspectives 2023," International Energy Agency, 2023
- YEGM, "Enerji Verimliliği Strateji Belgesi 2012-2023," T.C. Enerji ve Tabii Kaynaklar Bakanlığı
- Szargut, J., Morris, D.R. & Steward, F.R., "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes," Hemisphere Publishing, 1988
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," 3rd Edition, Elsevier, 2021
- UNIDO, "Industrial Energy Efficiency Benchmarking," United Nations Industrial Development Organization, 2010
- Worrell, E. et al., "Industrial Energy Efficiency and Climate Change Mitigation," Energy Efficiency, Springer, 2009
- Solomon Associates, "Worldwide Refinery Performance Analysis," (annual)
- ENERGY STAR, "Energy Performance Indicators for Industrial Plants," US EPA
- Phylipsen, G.J.M. et al., "International Comparisons of Energy Efficiency: Methodologies for the Manufacturing Industry," Energy Policy, 1997
