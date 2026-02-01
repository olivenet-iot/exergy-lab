---
title: "Kojenerasyon ve Trijenerasyon Sistemleri (Cogeneration — CHP and Trigeneration — CCHP)"
category: factory
equipment_type: factory
keywords: [kojenerasyon, CHP, elektrik, ısı]
related_files: [factory/waste_heat_recovery.md, factory/economic_analysis.md, factory/energy_flow_analysis.md]
use_when: ["Kojenerasyon fizibilitesi değerlendirilirken", "CHP sistemi analiz edilirken"]
priority: medium
last_updated: 2026-01-31
---
# Kojenerasyon ve Trijenerasyon Sistemleri (Cogeneration — CHP and Trigeneration — CCHP)

> Son güncelleme: 2026-01-31

## Genel Bakış

Kojenerasyon (CHP — Combined Heat and Power), tek bir yakıt kaynağından aynı anda hem elektrik hem de faydalı ısı üretilmesidir. Trijenerasyon (CCHP — Combined Cooling, Heating, and Power) ise CHP sistemine absorpsiyonlu soğutma eklenerek soğutma üretiminin de dahil edildiği konfigürasyondur. CHP sistemleri, ayrı ayrı elektrik ve ısı üretimine kıyasla %15-40 birincil enerji tasarrufu ve %10-25 CO₂ azaltımı sağlar. Exergy analizi açısından, CHP sistemlerinin enerji verimi ile exergy verimi arasındaki fark dikkat çekicidir ve gerçek termodinamik performansı ortaya koyar.

## 1. CHP Temelleri (CHP Fundamentals)

### 1.1 Çalışma Prensibi

```
Ayrı üretim (konvansiyonel):
- Elektrik: Şebeke santrali η_elek = %35-45
- Isı: Kazan η_ısı = %85-92
- Toplam birincil enerji: 100 birim elektrik / 0.40 + 100 birim ısı / 0.90
                        = 250 + 111 = 361 birim yakıt

Kojenerasyon (CHP):
- Elektrik: 100 birim
- Isı: 100 birim (atık ısıdan)
- Toplam birincil enerji: 200 / 0.85 = 235 birim yakıt
  (η_CHP = %85 genel verimlilik varsayımı)

Birincil enerji tasarrufu:
PES = 1 - 1 / (η_elek,CHP/η_elek,ref + η_ısı,CHP/η_ısı,ref)

Burada:
- η_elek,CHP = CHP elektrik verimi
- η_ısı,CHP = CHP ısı verimi
- η_elek,ref = referans elektrik üretim verimi (şebeke)
- η_ısı,ref = referans ısı üretim verimi (kazan)

Örnek:
η_elek,CHP = %38, η_ısı,CHP = %47
η_elek,ref = %40, η_ısı,ref = %90
PES = 1 - 1 / (0.38/0.40 + 0.47/0.90)
    = 1 - 1 / (0.95 + 0.522)
    = 1 - 1 / 1.472
    = 1 - 0.679 = %32.1 birincil enerji tasarrufu
```

### 1.2 Topping ve Bottoming Çevrimler

```
Topping çevrim (üstten):
- Önce elektrik üretilir, atık ısı kullanılır
- En yaygın CHP konfigürasyonu
- Gaz türbini + HRSG (Heat Recovery Steam Generator)
- Gaz motoru + egzoz/ceket suyu ısı geri kazanımı

Bottoming çevrim (alttan):
- Önce ısı kullanılır (proses), ardından düşük sıcaklıktan elektrik
- Sanayi fırınları, cam fabrikaları
- Atık ısı → ORC veya buhar türbini

Isı/Güç oranı (Heat-to-Power Ratio):
HPR = Q̇_ısı / Ẇ_elek

Tipik HPR değerleri:
- Gaz türbini CHP: 1.5–2.5
- Gaz motoru CHP: 0.8–1.5
- Buhar türbini CHP: 3–10
- Yakıt hücresi CHP: 0.5–1.0
```

## 2. Birincil Güç Kaynakları (Prime Movers)

### 2.1 Gaz Türbinleri (Gas Turbines)

```
Çalışma prensibi: Brayton çevrimi
Yakıt: Doğalgaz (primer), dizel, biyogaz
Güç aralığı: 1–350 MWe
Elektrik verimi: %25–40 (boyuta bağlı)
  - Mikro türbin (<500 kWe): %25–33
  - Küçük türbin (0.5–10 MWe): %28–35
  - Büyük türbin (>10 MWe): %33–40
Egzoz sıcaklığı: 450–550°C
Isı geri kazanım: HRSG ile buhar üretimi

Avantajlar:
+ Yüksek güvenilirlik (>95% kullanılabilirlik)
+ Düşük bakım maliyeti
+ Düşük NOx emisyonu (dry low NOx)
+ Yüksek egzoz sıcaklığı → yüksek kalite ısı

Dezavantajlar:
- Kısmi yükte verimlilik düşer
- Yüksek sıcaklık malzeme maliyeti
- Yakıt temizlik gereksinimi (özellikle biyogaz)
```

### 2.2 Buhar Türbinleri (Steam Turbines)

```
Çalışma prensibi: Rankine çevrimi
Yakıt: Herhangi (kazan üzerinden)
Güç aralığı: 0.5–500 MWe
Elektrik verimi: %15–30 (CHP modunda)
  (Yalnızca elektrik: %30–42)
Buhar çıkışı: Karşı basınçlı (back-pressure) veya çekiş (extraction)

Türler:
- Karşı basınçlı: Tüm buhar prosese gider, HPR yüksek
- Çekiş türbini: Orta kademeden buhar çekilir, daha esnek
- Yoğuşmalı (condensing): Proses buharı kalmadığında

Avantajlar:
+ Her yakıtı kullanabilir (kömür, biyokütle, atık)
+ Çok uzun ömür (>30 yıl)
+ Yüksek güvenilirlik
+ Geniş güç aralığı

Dezavantajlar:
- Düşük elektrik verimi (CHP modunda)
- Yavaş başlangıç (termal atalet)
- Büyük boyut ve ağırlık
- Su hazırlama gereksinimi
```

### 2.3 Gaz Motorları / Pistonlu Motorlar (Reciprocating Gas Engines)

```
Çalışma prensibi: Otto çevrimi (doğalgaz), Diesel çevrimi
Yakıt: Doğalgaz, biyogaz, LPG, dizel
Güç aralığı: 50 kWe – 10 MWe
Elektrik verimi: %35–45 (en yüksek küçük ölçek)
Isı kaynakları:
  - Egzoz gazı (450–500°C): toplam ısının %30–40'ı
  - Ceket soğutma suyu (80–95°C): toplam ısının %25–35'i
  - Yağ soğutma (70–80°C): toplam ısının %5–10'u
  - Şarj havası soğutma (40–60°C): toplam ısının %5–10'u

Avantajlar:
+ En yüksek elektrik verimi (küçük ölçek)
+ Hızlı başlangıç (dakikalar)
+ İyi kısmi yük performansı
+ Modüler kurulum

Dezavantajlar:
- Bakım maliyeti yüksek (yağ, bujiler, üst bakım)
- Gürültü ve titreşim
- NOx emisyonu (özellikle zengin karışım)
- Isı kalitesi orta (düşük egzoz sıcaklığı)
```

### 2.4 Yakıt Hücreleri (Fuel Cells)

```
Çalışma prensibi: Elektrokimyasal dönüşüm
Yakıt: Hidrojen (doğalgazdan reforming), doğalgaz (SOFC)
Güç aralığı: 1 kWe – 5 MWe
Elektrik verimi: %40–60 (en yüksek)
Isı verimi: %30–40
Çalışma sıcaklığı: 60–1,000°C (tipe bağlı)

Türler:
| Tip | Sıcaklık [°C] | η_elek [%] | Durum |
|---|---|---|---|
| PEMFC | 60–80 | 35–45 | Ticari |
| PAFC | 150–200 | 37–42 | Ticari |
| MCFC | 600–650 | 45–50 | Ticari |
| SOFC | 800–1,000 | 50–60 | Erken ticari |

Avantajlar:
+ En yüksek elektrik verimi
+ Çok düşük emisyon
+ Sessiz çalışma
+ Yüksek kısmi yük verimi

Dezavantajlar:
- Çok yüksek yatırım maliyeti (3,000–6,000 €/kWe)
- Sınırlı ömür (stak: 40,000–80,000 saat)
- Yakıt saflık gereksinimi
- Sınırlı ticari deneyim
```

### 2.5 Mikro Türbinler (Micro Turbines)

```
Çalışma prensibi: Brayton çevrimi (reküperatörlü)
Yakıt: Doğalgaz, biyogaz, LPG
Güç aralığı: 30–500 kWe
Elektrik verimi: %25–33
Isı verimi: %40–50
Egzoz sıcaklığı: 250–350°C

Avantajlar:
+ Kompakt boyut
+ Düşük bakım (tek hareketli parça: türbin-jeneratör mili)
+ Düşük emisyon
+ Modüler (çoklu kurulum)

Dezavantajlar:
- Düşük elektrik verimi (motor alternatifine göre)
- Sınırlı güç aralığı
- Yüksek birim maliyet (küçük ölçek)
```

## 3. Birincil Güç Kaynağı Karşılaştırma Tablosu

| Parametre | Gaz Türbini | Buhar Türbini | Gaz Motoru | Yakıt Hücresi | Mikro Türbin |
|---|---|---|---|---|---|
| Güç aralığı [MWe] | 1–350 | 0.5–500 | 0.05–10 | 0.001–5 | 0.03–0.5 |
| Elektrik verimi [%] | 25–40 | 15–30 | 35–45 | 40–60 | 25–33 |
| Isı verimi [%] | 40–50 | 50–70 | 35–45 | 30–40 | 40–50 |
| Toplam verimlilik [%] | 70–85 | 75–90 | 75–90 | 75–90 | 65–80 |
| Exergy verimi [%] | 35–48 | 25–38 | 40–52 | 48–62 | 30–40 |
| HPR (Isı/güç) | 1.5–2.5 | 3–10 | 0.8–1.5 | 0.5–1.0 | 1.5–2.0 |
| Yatırım [€/kWe] | 800–1,500 | 600–1,200 | 700–1,400 | 3,000–6,000 | 1,200–2,000 |
| Bakım [€ct/kWh_e] | 0.5–1.0 | 0.3–0.5 | 1.0–2.0 | 1.5–3.0 | 0.8–1.5 |
| Ömür [yıl] | 20–30 | 25–35 | 15–25 | 10–20 | 15–20 |
| Başlangıç süresi | 10–30 dk | 1–8 saat | 1–5 dk | 1–3 saat | 1–5 dk |
| Kısmi yük (%50) η kaybı | %15–25 | %10–15 | %5–10 | %2–5 | %10–20 |
| NOx emisyonu | Düşük | Yakıta bağlı | Orta | Çok düşük | Düşük |

## 4. CHP Exergy Analizi (Exergy Analysis of CHP)

### 4.1 Enerji vs. Exergy Verimlilik Karşılaştırması

```
CHP enerji verimi:
η_enerji = (Ẇ_elek + Q̇_ısı) / Q̇_yakıt × 100 [%]

CHP exergy verimi:
η_exergy = (Ẇ_elek + Ex_ısı) / Ex_yakıt × 100 [%]

Isı exergisi:
Ex_ısı = Q̇_ısı × (1 - T₀/T_ısı)    [kW]

Örnek: 500 kWe gaz motoru CHP
- Q̇_yakıt = 1,250 kW (doğalgaz, LHV)
- Ẇ_elek = 500 kW
- Q̇_ısı = 450 kW (ceket suyu 85°C + egzoz → sıcak su 80°C)
  → T_ısı ≈ 353 K (ortalama)

Enerji verimi:
η_enerji = (500 + 450) / 1,250 = %76.0

Exergy verimi:
Ex_yakıt = 1,250 × 1.04 = 1,300 kW (φ = 1.04 doğalgaz)
Ex_ısı = 450 × (1 - 298.15/353) = 450 × 0.155 = 69.8 kW
η_exergy = (500 + 69.8) / 1,300 = %43.8

Karşılaştırma:
η_enerji = %76.0  (yüksek görünüyor)
η_exergy = %43.8  (gerçek termodinamik performans)

Fark nedeni: Düşük sıcaklıklı ısının exergy içeriği düşüktür.
Elektrik saf exergydir, ısı ise düşük kalitelidir.
```

### 4.2 Exergy Yıkım Dağılımı (CHP)

| Bileşen | Exergy Yıkımı [%] | Açıklama |
|---|---|---|
| Yanma | 25–32 | En büyük kayıp (termodinamik zorunluluk) |
| Isı transferi (egzoz → su) | 8–15 | Sıcaklık farkından kaynaklanan |
| Mekanik kayıplar | 2–5 | Sürtünme, yardımcı ekipman |
| Jeneratör kayıpları | 2–4 | Elektrik dönüşüm kayıpları |
| Egzoz atık ısısı | 5–10 | Geri kazanılamayan kısım |
| Diğer (radyasyon vb.) | 1–3 | Yüzey kayıpları |

## 5. CCHP — Trijenerasyon (Trigeneration)

### 5.1 CCHP Konfigürasyonu

```
CCHP = CHP + Absorpsiyon Chiller

CHP bölümü:
Yakıt → Birincil güç kaynağı → Elektrik + Isı

Isı kullanımı (mevsimsel):
- Kış: Doğrudan ısıtma
- Yaz: Absorpsiyon chiller ile soğutma
- Ara mevsim: Kısmen ısıtma + kısmen soğutma

Absorpsiyon chiller entegrasyonu:
- Tek etkili (single effect): COP 0.65–0.75
  → Kaynak: 80–120°C sıcak su veya düşük basınçlı buhar
- Çift etkili (double effect): COP 1.0–1.2
  → Kaynak: 140–180°C buhar veya doğrudan baca gazı

CCHP toplam verimlilik:
η_CCHP = (Ẇ_elek + Q̇_ısıtma + Q̇_soğutma) / Q̇_yakıt
Tipik: %70–85 (enerji bazında)
```

### 5.2 CCHP Exergy Analizi

```
CCHP exergy verimi:
η_ex,CCHP = (Ẇ_elek + Ex_ısıtma + Ex_soğutma) / Ex_yakıt

Soğutma exergisi:
Ex_soğutma = Q̇_soğutma × |1 - T₀/T_soğutma|

Örnek (7°C chilled water):
Ex_soğutma = 200 kW × |1 - 298.15/280.15| = 200 × 0.064 = 12.8 kW

Not: Soğutma exergisi çok düşüktür (düşük sıcaklık farkı).
Bu nedenle CCHP'nin exergy verimi, CHP'ye kıyasla marjinal artış gösterir.
```

## 6. CHP Boyutlandırma Metodolojisi (Sizing)

### 6.1 Fizibilite Kriterleri

```
CHP fizibilite ön koşulları:
1. Yıllık çalışma süresi: ≥4,000 saat (tercihen >5,000)
2. Kararlı termal talep: Yıl boyunca sürekli ısı ihtiyacı
3. Elektrik fiyat farkı: Şebeke > üretim maliyeti
4. Uygun yakıt mevcudiyeti: Doğalgaz bağlantısı
5. Alan ve altyapı: Kurulum alanı, baca, gaz hattı

Boyutlandırma yaklaşımları:
- Termal talep bazlı: CHP ısı çıkışı ≤ taban termal yük
- Elektrik bazlı: CHP elektrik ≤ taban elektrik yükü
- Ekonomik optimizasyon: NPV'yi maksimize eden boyut

Pratik kural:
CHP_termal ≤ Taban termal yük × 0.80
(Pik yük için yardımcı kazan bırakılır)
```

### 6.2 Boyutlandırma Hesabı Örneği

```
Gıda fabrikası CHP boyutlandırması:
- Termal talep profili:
  Taban yük: 400 kW_th (yıl boyu, 8,000 saat)
  Kış piki: 700 kW_th (3,000 saat)
  Yaz minimumu: 300 kW_th (2,000 saat)

- Elektrik talebi:
  Taban yük: 600 kWe
  Pik: 900 kWe
  Yıllık: 5,000,000 kWh

Boyutlandırma (termal bazlı):
CHP_termal = 300 kW_th (yaz minimumuna göre)
HPR = 1.0 varsayımı (gaz motoru)
CHP_elektrik = 300 / 1.0 = 300 kWe

Kontrol:
- 300 kWe < 600 kWe taban elektrik → Tüm elektrik iç tüketim ✓
- 300 kW_th ≤ 300 kW_th yaz minimum → Isı her zaman kullanılır ✓
- Çalışma saati: ~7,500 saat (>4,000 saat) ✓

Alternatif (daha büyük):
CHP = 500 kWe → 500 kW_th
Yazın 200 kW_th ısı fazlası → atılır veya absorption chiller
→ CCHP'ye dönüştürülebilir
```

## 7. Ekonomik Analiz Örneği: 500 kWe Gaz Motoru CHP

### 7.1 Teknik Parametreler

```
Gaz motoru CHP sistemi:
- Elektrik çıkışı: 500 kWe (net)
- Isı çıkışı: 520 kW_th (ceket suyu + egzoz)
- Yakıt girişi: 1,250 kW (doğalgaz, LHV)
- Elektrik verimi: %40.0
- Isı verimi: %41.6
- Toplam verimlilik: %81.6
- Çalışma süresi: 7,000 saat/yıl
- Bakım aralığı: 2,000 saat/minor, 8,000 saat/major
```

### 7.2 Ekonomik Değerlendirme

```
Yatırım maliyeti:
- Motor-jeneratör: €350,000
- HRSG + ısı geri kazanım: €45,000
- Gaz bağlantısı + altyapı: €30,000
- Elektrik bağlantısı + panel: €35,000
- Montaj ve devreye alma: €40,000
- Toplam yatırım: €500,000

Yıllık gelir/tasarruf:
- Elektrik üretimi: 500 × 7,000 = 3,500,000 kWh/yıl
  Tasarruf: 3,500,000 × €0.12 = €420,000/yıl
- Isı üretimi: 520 × 7,000 = 3,640,000 kWh_th/yıl
  Kazan yakıt tasarrufu: 3,640,000 / 0.90 × €0.045 = €182,000/yıl
- Toplam gelir: €602,000/yıl

Yıllık giderler:
- Yakıt maliyeti: 1,250 × 7,000 × €0.045/kWh = €393,750/yıl
- Bakım maliyeti: 3,500,000 × €0.015/kWh = €52,500/yıl
- Sigorta + diğer: €10,000/yıl
- Toplam gider: €456,250/yıl

Net yıllık tasarruf:
Net = €602,000 - €456,250 = €145,750/yıl

Ekonomik göstergeler:
- SPP = 500,000 / 145,750 = 3.43 yıl
- NPV (15 yıl, %10): €608,000
- IRR: %28
- CO₂ azaltımı: ~450 ton/yıl (şebeke emisyon faktörüne bağlı)
```

## 8. CHP vs. Ayrı Üretim Karşılaştırma Tablosu

| Parametre | Ayrı Üretim | CHP (Gaz Motoru) | Fark |
|---|---|---|---|
| Elektrik: 3,500 MWh/yıl | Şebeke: €420,000 | CHP yakıt payı: €262,500 | -€157,500 |
| Isı: 3,640 MWh_th/yıl | Kazan: €182,000 | CHP yakıt payı: €131,250 | -€50,750 |
| Toplam yakıt | Kazan: 4,044 MWh | CHP: 8,750 MWh | +4,706 MWh |
| Toplam maliyet | €602,000/yıl | €456,250/yıl | -€145,750/yıl |
| Birincil enerji | 12,944 MWh | 8,750 MWh | -32% |
| CO₂ emisyonu | 2,850 ton | 1,750 ton | -39% |

## 9. Türkiye CHP Mevzuatı ve Teşvikleri

### 9.1 Yasal Çerçeve

```
Elektrik Piyasası Kanunu (No. 6446):
- Öz tüketim CHP: Lisans gerektirmez (<1 MWe)
- Şebekeye satış: Üretim lisansı gerekli
- Bağlantı: Dağıtım şirketi ile bağlantı anlaşması

Enerji Verimliliği Kanunu (No. 5627):
- CHP teşvikleri: VAP kapsamında destek
- Yüksek verimli CHP tanımı (EU 2012/27 uyumlu)

Teşvikler:
- Yüksek verimli CHP belgesi: PES > %10
- Şebeke önceliği (dispatch priority)
- Sistem kullanım indirimi
- VAP desteği: Yatırımın %30'una kadar (max 5M TL)
```

### 9.2 Performans Sınıflandırması (CHP)

| Performans Kriteri | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Toplam enerji verimi | <%70 | %70–80 | %80–88 | >%88 |
| Exergy verimi | <%30 | %30–40 | %40–50 | >%50 |
| Yıllık çalışma süresi | <4,000 h | 4,000–6,000 h | 6,000–7,500 h | >7,500 h |
| PES (birincil enerji tasarrufu) | <%10 | %10–20 | %20–30 | >%30 |
| SPP | >5 yıl | 3–5 yıl | 2–3 yıl | <2 yıl |

## 10. Merkezi vs. Dağıtık CHP Karşılaştırması

| Kriter | Merkezi CHP | Dağıtık CHP |
|---|---|---|
| Güç aralığı | >5 MWe | 50 kWe – 5 MWe |
| Elektrik verimi | %35–45 | %30–45 |
| Isı dağıtım kaybı | %5–15 (bölgesel ısıtma) | <%3 (yerinde) |
| Yatırım [€/kWe] | 600–1,000 | 800–1,500 |
| Esneklik | Düşük | Yüksek |
| Güvenilirlik | Yüksek (yedeklilik) | Orta (tek ünite) |
| Bakım | Merkezi, verimli | Dağıtık, maliyetli |
| Uygun uygulama | Bölgesel ısıtma, OSB | Tek fabrika, bina |

## 11. Bakım Gereksinimleri

| Bakım Tipi | Gaz Motoru | Gaz Türbini | Buhar Türbini |
|---|---|---|---|
| Yağ değişimi | 2,000 h | — | — |
| Bujiler/enjektör | 4,000–8,000 h | — | — |
| Minor bakım | 8,000 h | 4,000 h | 8,000 h |
| Major bakım | 30,000–40,000 h | 25,000–30,000 h | 40,000–60,000 h |
| Bakım maliyeti [€ct/kWhe] | 1.0–2.0 | 0.5–1.0 | 0.3–0.5 |
| Kullanılabilirlik | %92–95 | %95–98 | %95–99 |

## İlgili Dosyalar

- [Isı Entegrasyonu](heat_integration.md) — CHP ısı entegrasyonu ile bağlantı
- [Atık Isı Geri Kazanım](waste_heat_recovery.md) — CHP atık ısı değerlendirme
- [Ekipmanlar Arası Optimizasyon](cross_equipment.md) — CHP ve diğer ekipmanlar arası entegrasyon
- [Proses Entegrasyonu](process_integration.md) — CHP proses entegrasyonu
- [Ekonomik Analiz](economic_analysis.md) — CHP yatırım analizi
- [Kazan Formülleri](../boiler/formulas.md) — Kazan verimlilik karşılaştırması
- [Kazan Benchmarkları](../boiler/benchmarks.md) — Kazan performans referansları
- [Chiller Formülleri](../chiller/formulas.md) — Absorpsiyon chiller hesaplamaları (CCHP)
- [Kompresör Formülleri](../compressor/formulas.md) — Basınçlı hava enerji hesaplamaları
- [Exergy Temelleri](exergy_fundamentals.md) — CHP exergy analizi temelleri

## Referanslar

- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration"
- ASHRAE, "ASHRAE Combined Heat and Power Design Guide," 2015
- US DOE, "Catalog of CHP Technologies," 2017
- Moran, M.J. et al., "Fundamentals of Engineering Thermodynamics," Wiley, 9th Edition, 2018
- Bejan, A., "Advanced Engineering Thermodynamics," Wiley, 4th Edition, 2016
- Tsatsaronis, G. & Morosuk, T., "Advanced exergy-based methods used to understand and improve energy-conversion systems," Energy, 2012
- Lozano, M.A. et al., "Theory of the exergetic cost," Energy, 1993
- Rosen, M.A. & Dincer, I., "Exergy analysis of cogeneration and district energy systems," Exergy, An International Journal, 2004
- Türkiye Elektrik Piyasası Kanunu (No. 6446) ve ilgili yönetmelikler
- EPDK, "Kojenerasyon ve Mikrokojenerasyon Tesislerine İlişkin Usul ve Esaslar"
