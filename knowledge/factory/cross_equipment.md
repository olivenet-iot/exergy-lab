---
title: "Ekipmanlar Arası Optimizasyon Fırsatları (Cross-Equipment Optimization Opportunities)"
category: factory
equipment_type: factory
keywords: [ekipmanlar arası, çapraz optimizasyon, fabrika]
related_files: [factory/prioritization.md, factory/heat_integration.md, factory/waste_heat_recovery.md]
use_when: ["Ekipmanlar arası optimizasyon değerlendirilirken", "Çapraz enerji fırsatları analiz edilirken"]
priority: high
last_updated: 2026-01-31
---
# Ekipmanlar Arası Optimizasyon Fırsatları (Cross-Equipment Optimization Opportunities)

> Son güncelleme: 2026-01-31

## Genel Bakış

Ekipmanlar arası optimizasyon, ExergyLab platformunun temel değer önerisidir. Bireysel ekipman analizlerinin ötesine geçerek, farklı ekipmanlar arasındaki enerji akışlarını, atık ısı potansiyellerini ve sinerji fırsatlarını sistematik olarak değerlendirir. Tipik bir fabrikada ekipmanlar birbirinden bağımsız olarak optimize edilir; ancak gerçek tasarruf potansiyelinin %30-50'si ekipmanlar arası entegrasyonda yatar. Bu dosya, ExergyLab platformunun tespit ettiği ve kullanıcıya önerdiği tüm çapraz ekipman entegrasyon fırsatlarını detaylı olarak ele alır.

## 1. Kompresör → Kazan Entegrasyonu (Compressor Waste Heat → Boiler Feedwater Preheating)

### 1.1 Temel Prensip

Vidalı ve pistonlu kompresörlerin elektrik enerjisinin %70-94'ü ısıya dönüşür. Bu ısı normalde soğutma kuleleri veya hava soğutucuları ile atmosfere atılır. Kompresör atık ısısı genellikle 70-90°C sıcaklık seviyesindedir ve bu sıcaklık, kazan besleme suyunu ön ısıtmak için idealdir.

```
Kompresör atık ısı potansiyeli:
Q̇_atık = Ẇ_kompresör × η_atık_ısı [kW]

Burada:
- Ẇ_kompresör = kompresör şaft gücü [kW]
- η_atık_ısı = geri kazanılabilir ısı oranı [0.50–0.70]
  (tüm ısının değil, ekonomik olarak geri kazanılabilir kısmın oranı)

Toplam ısı üretimi (kompresör):
Q̇_toplam = Ẇ_kompresör × 0.94 (vidalı, su soğutmalı)
Q̇_toplam = Ẇ_kompresör × 0.76 (vidalı, hava soğutmalı, kısmi)

Geri kazanılabilir kısım:
- Su soğutmalı: Q̇_geri = Ẇ × 0.70 (ceket + yağ soğutma)
- Hava soğutmalı: Q̇_geri = Ẇ × 0.50–0.60 (hava kanalı ile)
```

### 1.2 Hesaplama Örneği

```
Senaryo: 37 kW vidalı kompresör, su soğutmalı
- Kompresör gücü: 37 kW
- Çalışma süresi: 6,000 saat/yıl
- Yük oranı: %80 ortalama
- Su soğutmalı: Soğutma suyu giriş/çıkış 70/85°C

Geri kazanılabilir ısı:
Q̇_geri = 37 × 0.80 × 0.70 = 20.7 kW

Besleme suyu ön ısıtma etkisi:
- Kazan: 4 ton/h buhar, besleme suyu 15°C (kondensat dönüşü düşük)
- ṁ_besleme = 4,000/3,600 = 1.11 kg/s (yoğuşma kayıpları dahil)
- ΔT = Q̇_geri / (ṁ × Cp) = 20.7 / (1.11 × 4.18) = 4.5°C
  (15°C → 19.5°C)

Daha büyük kompresörle:
- 75 kW kompresör: Q̇_geri = 75 × 0.80 × 0.70 = 42 kW
  → ΔT = 42 / (1.11 × 4.18) = 9.0°C (15°C → 24°C)

Yakıt tasarrufu hesabı:
E_tasarruf = Q̇_geri × t_çalışma / η_kazan [kWh/yıl]
           = 20.7 × 6,000 / 0.88
           = 141,136 kWh/yıl

Maliyet tasarrufu:
C_tasarruf = 141,136 × €0.045/kWh = €6,351/yıl

Kazan yakıt tüketimi azalması:
Kazan yakıt tüketimi = 4,000 × (2,675 - 63) / (0.88 × 34,500 × 1,000 / 3,600)
                     ≈ 1,237 kW yakıt girişi
Tasarruf yüzdesi = 20.7 / (1,237 × 0.88) × 100 = %1.9

75 kW kompresör ile:
C_tasarruf = 42 × 6,000 / 0.88 × €0.045 = €12,886/yıl
Tasarruf yüzdesi = %3.9

Yatırım maliyeti:
- Plakalı eşanjör (paslanmaz, 25 kW): €3,500
- Boru hattı (izoleli, 20 m): €2,500
- Dolaşım pompası: €800
- Kontrol vanası ve enstrümantasyon: €1,200
- Montaj: €2,000
- Toplam: €10,000

SPP = 10,000 / 6,351 = 1.57 yıl (37 kW)
SPP = 10,000 / 12,886 = 0.78 yıl (75 kW)
```

### 1.3 Uygulama Hususları

```
Teknik gereksinimler:
1. Mesafe: Kompresör-kazan arası <50 m (ideal <20 m)
   → >50 m ise boru maliyeti ve ısı kaybı artar
2. Soğutma tipi: Su soğutmalı kompresör tercih edilir
   (hava soğutmalı için kanal adaptasyonu gerekir)
3. Yük profili eşleştirme:
   - Kompresör sürekli çalışıyor mu?
   - Kazan besleme suyu sürekli akıyor mu?
   → Değişken yük: Bypass vanası gerekli
4. Sıcaklık kontrolü:
   - Kompresör çıkış suyu sıcaklığı izlenmeli
   - Aşırı sıcaklık durumunda bypass'a yönlendirme
5. Su kalitesi:
   - Soğutma suyu döngüsü ve kazan suyu ayrı tutulmalı
   - Ara eşanjör gerekli (kontaminasyon önleme)
6. Legionella riski:
   - 25–45°C aralığı riskli → sistemin bu aralıkta durağan
     kalmaması sağlanmalı

Uyumsuzluk durumları:
- Kompresör kuru çalışıyorsa (oil-free, hava soğutmalı): Q̇ düşük
- Kazan kondensat dönüşü zaten >60°C ise: ΔT yetersiz
- Kompresör VSD ile düşük yükte çalışıyorsa: Q̇ değişken
```

## 2. Kompresör → Bina Isıtma Entegrasyonu (Compressor Heat → Space Heating)

### 2.1 Temel Prensip

Kompresör atık ısısı, kış aylarında fabrika bina ısıtmasında kullanılabilir. Özellikle hava soğutmalı kompresörlerde, sıcak egzoz havasını doğrudan bina içine yönlendirmek en basit ve en düşük maliyetli çözümdür.

```
Hava soğutmalı kompresör → Bina ısıtma:
Q̇_ısıtma = Ẇ_kompresör × 0.94 × η_kanal [kW]

Burada:
η_kanal = kanal verimi [0.80–0.95] (izolasyon ve mesafeye bağlı)

Su soğutmalı kompresör → Fan-coil bina ısıtma:
Q̇_ısıtma = Q̇_geri × η_dağıtım [kW]
Dağıtım sıcaklığı: 70–80°C (radyatör uyumlu)

Hesaplama örneği (hava soğutmalı):
- 55 kW kompresör, hava soğutmalı
- Q̇ = 55 × 0.94 × 0.90 = 46.5 kW ısıtma
- Bina ısıtma ihtiyacı: 80 kW (kış)
- Karşılama oranı: 46.5 / 80 = %58

Yıllık tasarruf (yalnızca kış, 4 ay):
E = 46.5 × 2,500 = 116,250 kWh/yıl
C = 116,250 / 0.90 × €0.045 = €5,813/yıl
(Doğalgaz ile ısıtma yerine)

Yatırım (hava kanalı, damper, kontrol):
Yatırım = €5,000
SPP = 5,000 / 5,813 = 0.86 yıl (10 ay)
```

### 2.2 Sıcak Su Üretimi (DHW)

```
Kompresör atık ısısı → sıcak kullanım suyu:
- Kaynak: 70–85°C kompresör soğutma suyu
- Hedef: 55–60°C sıcak su (lavabo, duş)
- Yıl boyu kullanılabilir (mevsimsel bağımlılık yok)

Örnek:
- 37 kW kompresör → 20 kW geri kazanım
- Sıcak su ihtiyacı: 2,000 L/gün @ 55°C
- Gerekli güç: 2,000 × 4.18 × (55-15) / (3,600 × 8) = 11.6 kW
- Karşılama: 20 / 11.6 = %100+ (fazla ısı bypass'a)

Yatırım: €6,000 (eşanjör + akü tank + kontrol)
Yıllık tasarruf: 11.6 × 6,000 / 0.90 × €0.045 = €3,480/yıl
SPP = 6,000 / 3,480 = 1.72 yıl
```

## 3. Kazan → Absorpsiyon Chiller Entegrasyonu (Boiler → Absorption Chiller)

### 3.1 Buhar ile Absorpsiyon Soğutma

```
Konfigürasyon: Kazan buharı → Absorpsiyon chiller → Chilled water

Tek etkili (single effect) LiBr-su:
- Kaynak: Düşük basınçlı buhar (0.5–2 bar) veya sıcak su (80–120°C)
- COP: 0.65–0.75
- Soğutma: 7°C chilled water

Çift etkili (double effect) LiBr-su:
- Kaynak: Orta basınçlı buhar (4–8 bar) veya baca gazı (>140°C)
- COP: 1.0–1.2
- Soğutma: 7°C chilled water

Hesaplama:
Q̇_soğutma = Q̇_ısı_kaynağı × COP [kW]

Örnek (tek etkili):
- Mevcut buhar: LP buhar 1.5 bar, 200 kW kullanılabilir
- COP = 0.70
- Q̇_soğutma = 200 × 0.70 = 140 kW soğutma

Örnek (çift etkili):
- Kaynak: MP buhar 6 bar, 200 kW
- COP = 1.10
- Q̇_soğutma = 200 × 1.10 = 220 kW soğutma

Ekonomik karşılaştırma (mekanik chiller vs. absorpsiyon):
Mekanik chiller (COP = 5.0):
Elektrik maliyeti: Q̇_soğutma / COP × c_elek = 140/5.0 × €0.12 = €3.36/saat

Absorpsiyon chiller (COP = 0.70):
Buhar maliyeti: Q̇_soğutma / COP × c_buhar = 140/0.70 × €0.030 = €6.00/saat

Absorpsiyon avantajlı olduğu durum:
→ Atık ısı veya fazla buhar bedava ise (c_buhar ≈ 0)
→ Elektrik fiyatı çok yüksek veya kısıtlı ise
→ CHP sistemi ile birlikte (CCHP)
→ Pik elektrik talebini azaltmak için
```

### 3.2 Baca Gazı Atık Isısı → Absorpsiyon Chiller

```
Kazan baca gazı (150–250°C) → sıcak su → tek etkili absorpsiyon

Konfigürasyon:
Baca gazı → Economizer/eşanjör → 90°C sıcak su → Absorpsiyon chiller

Hesaplama:
- Baca gazı: 200°C, 5,000 Nm³/h
- Geri kazanılabilir ısı: Q̇ = 180 kW (200→130°C soğutma)
- Absorpsiyon COP = 0.70
- Soğutma üretimi: 180 × 0.70 = 126 kW

Bu konfigürasyon özellikle yazın buhar talebinin düştüğü
ancak soğutma talebinin arttığı tesislerde değerlidir.
```

### 3.3 Blowdown Isı Geri Kazanımı

```
Kazan blowdown suyu (10 bar, 180°C) → ısı geri kazanım:

Flash tank → düşük basınç buhar + sıcak su
Flash buhar oranı: ~%14 (10 bar → atmosfer)

Q̇_geri = ṁ_blowdown × [(h_blowdown - h_flash_su) + x × h_fg] [kW]

Tipik geri kazanım:
- 6 ton/h buhar kazanı, %5 blowdown
- ṁ_blowdown = 0.3 ton/h = 0.083 kg/s
- Geri kazanım: ~15 kW (flash) + 8 kW (su soğutma) = 23 kW
- Yıllık tasarruf: 23 × 6,000 / 0.88 × €0.045 = €7,057/yıl
- Yatırım: €8,000 (flash tank + eşanjör)
- SPP = 1.13 yıl
```

## 4. Chiller → Isıtma Entegrasyonu (Chiller Heat Recovery)

### 4.1 Desuperheater ile Sıcak Su Üretimi

```
Çalışma prensibi:
Chiller kompresörü çıkışında kızgın buhar (superheated vapor)
sıcaklığı kondensasyon sıcaklığından çok yüksektir (70–90°C).
Desuperheater ile bu fazla ısı alınarak sıcak su üretilebilir.

Q̇_desup = ṁ_soğutucu × (h_kompresör_çıkış - h_doymuş_buhar) [kW]
Q̇_desup ≈ Q̇_soğutma × 0.10–0.15 (toplam soğutma kapasitesinin)

Örnek:
- Chiller: 500 kW soğutma, R134a
- Kompresör çıkışı: 85°C (kızgın buhar)
- Kondensasyon: 40°C
- Q̇_desup = 500 × 0.12 = 60 kW sıcak su (55–65°C)

Yatırım: €12,000 (desuperheater eşanjör + pompa + kontrol)
Yıllık tasarruf: 60 × 5,000 / 0.90 × €0.045 = €15,000/yıl
SPP = 12,000 / 15,000 = 0.80 yıl (10 ay)
```

### 4.2 Isı Geri Kazanımlı Chiller (Heat Recovery Chiller)

```
Çalışma prensibi:
Chiller kondenser ısısını (Q̇_kond = Q̇_evap + Ẇ_komp) tamamen
geri kazanarak ısıtmada kullanır. Eşzamanlı soğutma + ısıtma.

Q̇_kondenser = Q̇_soğutma + Ẇ_kompresör [kW]
Q̇_kondenser = Q̇_soğutma × (1 + 1/COP) [kW]

Örnek:
- Soğutma: 200 kW, COP = 4.5
- Kompresör: 200 / 4.5 = 44.4 kW
- Kondenser ısısı: 200 + 44.4 = 244.4 kW @ 45–55°C

COP_birleşik = (Q̇_soğutma + Q̇_ısıtma) / Ẇ_komp
             = (200 + 244.4) / 44.4 = 10.0

Eşzamanlı ihtiyaç koşulu:
- Yazın: Soğutma yüksek, ısıtma düşük → fazla ısı atılır
- Kışın: Soğutma düşük, ısıtma yüksek → soğutma kısıtlayıcı
- Ara mevsim: İdeal çalışma koşulu

Uygulamalar:
- Gıda fabrikaları (soğuk depo + proses sıcak su)
- Oteller (soğutma + DHW)
- Hastaneler (soğutma + ısıtma)
- Süpermarketler (soğutma vitrini + bina ısıtma)
```

### 4.3 Eşzamanlı Isıtma-Soğutma Analizi

```
Eşzamanlılık oranı:
SR = min(Q̇_soğutma, Q̇_ısıtma) / max(Q̇_soğutma, Q̇_ısıtma) [0–1]

SR > 0.5: Isı geri kazanımlı chiller ekonomik
SR > 0.8: Mükemmel uyum, yüksek tasarruf
SR < 0.3: Mevsimsel depolama veya hibrit sistem gerekli

Aylık profil analizi örneği:
| Ay | Q̇_soğutma [kW] | Q̇_ısıtma [kW] | SR | Değerlendirme |
|---|---|---|---|---|
| Ocak | 100 | 300 | 0.33 | Düşük (soğutma kısıtlar) |
| Şubat | 100 | 250 | 0.40 | Orta |
| Mart | 150 | 200 | 0.75 | İyi |
| Nisan | 200 | 150 | 0.75 | İyi |
| Mayıs | 300 | 100 | 0.33 | Düşük (ısıtma kısıtlar) |
| Haziran | 400 | 50 | 0.13 | Düşük |
| Temmuz | 500 | 30 | 0.06 | Çok düşük |
| Ağustos | 450 | 30 | 0.07 | Çok düşük |
| Eylül | 350 | 80 | 0.23 | Düşük |
| Ekim | 200 | 150 | 0.75 | İyi |
| Kasım | 150 | 250 | 0.60 | İyi |
| Aralık | 100 | 300 | 0.33 | Düşük |

Yıllık ortalama SR: ~0.38 → Kısmi uygulama önerilir
En iyi dönem: Mart-Nisan-Ekim-Kasım (SR > 0.60)
```

## 5. Pompa → Sistem Optimizasyonu (Pump System Optimization)

### 5.1 VSD ile Pompa Optimizasyonu

```
Pompa enerji tüketimi:
Ẇ_pompa = Q × ΔP / (η_pompa × η_motor) [kW]

Burada:
- Q = debi [m³/s]
- ΔP = toplam basınç farkı [Pa]
- η_pompa = pompa verimi [0.60–0.85]
- η_motor = motor verimi [0.90–0.96]

Affinite yasaları (VSD ile):
Q₂/Q₁ = n₂/n₁
ΔP₂/ΔP₁ = (n₂/n₁)²
Ẇ₂/Ẇ₁ = (n₂/n₁)³

Debi %20 azaltma → Güç %49 azalma:
Ẇ₂ = Ẇ₁ × (0.80)³ = 0.512 × Ẇ₁

Hesaplama örneği:
- Mevcut: 22 kW pompa, vana ile kısılarak %80 debi
- VSD ile: Ẇ_VSD = 22 × (0.80)³ = 11.3 kW
- Tasarruf: 22 - 11.3 = 10.7 kW
- Yıllık: 10.7 × 6,000 × €0.12 = €7,704/yıl
- VSD yatırımı: €4,500
- SPP = 4,500 / 7,704 = 0.58 yıl (7 ay)
```

### 5.2 Sistem Eğrisi Optimizasyonu

```
Pompa işletme noktası = pompa eğrisi ∩ sistem eğrisi

Sistem eğrisi: ΔP_sistem = ΔP_statik + K × Q²

Optimizasyon fırsatları:
1. Boru çapını artır → K azalır → ΔP düşer → güç azalır
2. Vanaları tam aç, kontrol VSD ile yap → kısma kaybı yok
3. Gereksiz dirsekleri/fitingleri azalt → K azalır
4. Boru iç yüzey pürüzlülüğünü azalt → sürtünme düşer
5. Daha kısa güzergah → boru uzunluğu azalır

Tipik tasarruf: %10–30 pompa enerji tüketiminde
```

### 5.3 Paralel Pompa Yönetimi

```
Paralel pompa stratejisi:
- Düşük yükte: Tek pompa çalıştır
- Orta yükte: İki pompa paralel (her biri %50 kapasite)
- Yüksek yükte: Üç pompa paralel

Verimlilik etkisi:
| Yük [%] | Tek Pompa η [%] | İki Pompa Paralel η [%] | Tercih |
|---|---|---|---|
| 30 | 55 | 40 (her biri %15'te) | Tek pompa |
| 50 | 75 | 60 (her biri %25'te) | Tek pompa |
| 70 | 82 | 75 (her biri %35'te) | Tek pompa |
| 90 | 78 | 82 (her biri %45'te) | İki pompa |
| 100 | — | 85 (her biri %50'de) | İki pompa |

VSD + paralel pompa kombinasyonu en yüksek tasarrufu verir.
Kontrol stratejisi: Kademeli açma + VSD hız kontrolü
```

## 6. Ortak Yardımcı Sistemler (Utility Sharing)

### 6.1 Ortak Soğutma Kulesi Optimizasyonu

```
Birden fazla ekipman aynı soğutma kulesini paylaşabilir:
- Chiller kondenseri
- Kompresör yağ/su soğutucu
- Proses soğutma
- Hidrolik sistem soğutma

Optimizasyon fırsatları:
1. Değişken hız fan kontrolü (VSD)
   → Soğutma suyu sıcaklığına göre fan hızı ayarı
   → Tasarruf: %20–50 fan enerjisi

2. Serbest soğutma (free cooling)
   → Yaş termometre sıcaklığı düşükse doğrudan soğutma
   → Chiller bypass → Elektrik tasarrufu: %30–70 (kış ayları)

3. Su kalitesi yönetimi
   → Fouling azaltma → ısı transfer verimi artışı
   → Kondenser yaklaşım sıcaklığı: 3°C → 1.5°C
   → Chiller COP artışı: %5–10

Hesaplama (VSD fan):
- Mevcut: 2 × 15 kW fan, sürekli çalışma
- Ortalama yük: %60
- VSD ile: 2 × 15 × (0.60)³ = 6.5 kW
- Tasarruf: 30 - 6.5 = 23.5 kW
- Yıllık: 23.5 × 8,000 × €0.12 = €22,560/yıl
- Yatırım: €8,000 (2 × VSD)
- SPP = 0.35 yıl (4 ay)
```

### 6.2 Ortak Basınçlı Hava Şebekesi Optimizasyonu

```
Merkezi basınçlı hava sistemi optimizasyonu:

1. Basınç seviyesi ayrımı:
   - Yüksek basınç (>7 bar): Yalnızca ihtiyaç olan proseslere
   - Normal basınç (6–7 bar): Genel fabrika
   - Düşük basınç (<5 bar): Taşıma, üfleme
   → Basınç 1 bar düşürme ≈ %7 enerji tasarrufu

2. Hava kalitesi ayrımı:
   - ISO 8573-1 Class 1: Kritik prosesler (gıda, ilaç)
   - Class 2-3: Genel kullanım
   → Gereksiz kalite = gereksiz enerji

3. Ring hat sistemi:
   → Basınç düşüşünü minimize eder
   → Yedeklilik sağlar

4. Otomatik kaçak tespiti:
   → Ultrasonik kaçak tespit programı
   → Tipik kaçak: %15–30 (bakımsız sistem)
   → Kaçak %20'den %10'a düşürme: %10 enerji tasarrufu
```

### 6.3 Buhar Dağıtım Optimizasyonu

```
Buhar sistemi entegrasyon fırsatları:

1. Kondensat geri dönüş oranını artır:
   - Mevcut: %50 → Hedef: %80
   - Tasarruf: Su + kimyasal + enerji
   - Her %10 artış ≈ %1 kazan yakıt tasarrufu

2. Buhar basınç seviyesi optimizasyonu:
   - Gereksiz yüksek basınç azaltma
   - Back-pressure türbin ile kademe düşürme (güç üretimi)

3. Buhar kapanı bakımı:
   - Arızalı kapanlar: %5–15 buhar kaybı
   - Yıllık kontrol programı
   - Kapan başına tasarruf: 50–500 €/yıl

4. İzolasyon iyileştirme:
   - Çıplak vana ve flanşlar: Önemli kayıp noktaları
   - Çıkarılabilir izolasyon ceketi: €100–300/parça
   - Geri ödeme: 3–12 ay
```

## 6A. Kurutma Fırını Entegrasyonları (Dryer Cross-Equipment Integration)

### 6A.1 Kazan Baca Gazı → Kurutma Havası Ön Isıtma

```
Çalışma prensibi:
Kazan baca gazı (150-250°C) ısı eşanjörü ile kurutma giriş havasını
ön ısıtmak için kullanılır. Kurutma fırınları büyük hacimde sıcak
hava tükettiğinden, bu entegrasyon önemli yakıt tasarrufu sağlar.

Konfigürasyon:
Baca gazı → Ekonomizer/eşanjör → Kurutma havası ön ısıtma

Hesaplama:
- Baca gazı: 200°C, 5,000 Nm³/h
- Geri kazanılabilir ısı: Q̇ = 120 kW (200°C → 140°C soğutma)
- Kurutma havası debisi: 8,000 m³/h
- Hava sıcaklık artışı: ΔT = Q̇ / (ṁ_hava × Cp)
  = 120 / (8,000/3,600 × 1.2 × 1.005) = 44.5°C
  → Ortam 20°C → 64.5°C ön ısıtma

Yakıt tasarrufu:
E_tasarruf = 120 × 6,000 / 0.88 = 818,182 kWh/yıl
C_tasarruf = 818,182 × €0.045 = €36,818/yıl

Yatırım: €25,000 (gaz-hava eşanjör + kanal + kontrol)
SPP = 25,000 / 36,818 = 0.68 yıl

Dikkat:
- Baca gazı tarafı korozyona dayanıklı malzeme (asit çiğ noktası)
- Kurutma havası kontaminasyon riski → dolaylı eşanjör tercih
- Baca gazı basınç düşüşü → ID fan güç artışı hesaplanmalı
```

### 6A.2 Kompresör Atık Isısı → Düşük Sıcaklık Kurutma

```
Çalışma prensibi:
Kompresör atık ısısı (70-90°C) düşük sıcaklık kurutma uygulamalarında
(kereste, gıda, tekstil ön kurutma) hava ön ısıtma için kullanılabilir.

Uygun kurutma tipleri:
- Kereste kurutma fırını (50-80°C)
- Gıda kurutma (40-70°C)
- Isı pompalı kurutucu destek ısıtma

Hesaplama:
- Kompresör: 55 kW, su soğutmalı, %75 yük
- Q̇_geri = 55 × 0.75 × 0.70 = 28.9 kW
- Kurutma havası: 3,000 m³/h
- ΔT = 28.9 / (3,000/3,600 × 1.2 × 1.005) = 28.8°C
  → 20°C → 48.8°C (kereste kurutma için yeterli başlangıç)

Yıllık tasarruf: 28.9 × 6,000 / 0.88 × €0.045 = €8,873/yıl
Yatırım: €12,000 (eşanjör + fan-coil + boru + kontrol)
SPP = 12,000 / 8,873 = 1.35 yıl
```

### 6A.3 Kurutma Egzozu → Kazan Besleme Suyu Ön Isıtma

```
Çalışma prensibi:
Kurutma fırını egzoz havası (80-150°C) kazan besleme suyunu
ön ısıtmak için kullanılabilir. Egzoz havası nemli olduğundan
yoğuşmalı ısı geri kazanımı ile gizli ısı da alınabilir.

Hesaplama:
- Kurutma egzozu: 120°C, 6,000 m³/h, %40 bağıl nem
- Eşanjör ile soğutma: 120°C → 70°C
- Q̇_geri = 6,000/3,600 × 1.1 × 1.02 × (120 - 70) × 0.65 = 60 kW
  (gizli ısı dahil edilirse: ~80 kW)

Besleme suyu etkisi:
- Kazan 6 ton/h buhar, besleme suyu 15°C
- ΔT = 80 / (6,000/3,600 × 4.18) = 11.5°C (15°C → 26.5°C)

Yıllık tasarruf: 80 × 5,000 / 0.88 × €0.045 = €20,455/yıl
Yatırım: €18,000 (hava-su eşanjör + boru + pompa + kontrol)
SPP = 18,000 / 20,455 = 0.88 yıl

Dikkat:
- Egzoz havası toz/partikül içerebilir → ön filtre gerekli
- Yoğuşma suyu drenajı → korozyon önleme
- Kurutma ile kazan çalışma saatleri eşzamanlı olmalı
```

### 6A.4 Fırın/Kiln Egzozu → Kurutma Havası (Seramik Sektörü)

```
Çalışma prensibi:
Seramik ve tuğla sektöründe, pişirme fırını (kiln) egzozu
250-600°C sıcaklığındadır. Bu yüksek sıcaklık, kurutma
fırınına doğrudan veya dolaylı olarak aktarılabilir.
Bu entegrasyon seramik sektöründe yaygın ve yüksek tasarruf sağlar.

Hesaplama:
- Kiln egzozu: 400°C, 8,000 Nm³/h
- Kurutma ihtiyacı: 150°C hava, 6,000 m³/h
- Karışım/eşanjör ile: 400°C gaz → 200°C soğutma
- Q̇_transfer = 350 kW

Yakıt tasarrufu: Kurutma fırını yakıtının %50-80'i karşılanabilir
Yıllık tasarruf: 350 × 5,000 / 0.88 × €0.045 = €89,489/yıl
Yatırım: €50,000-80,000 (eşanjör + kanal + fan + kontrol)
SPP = 65,000 / 89,489 = 0.73 yıl

Uygulamalar:
- Tuğla fabrikası: Tünel kiln → kurutma odası
- Seramik karo: Roller kiln → kurutma fırını
- Çimento: Klinker soğutucu → hammadde kurutma
```

### 6A.5 Kurutma Entegrasyon Karar Matrisi

| No | Kaynak (Source) | Hedef (Target) | Uyumluluk | T_kaynak [°C] | Tipik Tasarruf [€/yıl] | Yatırım [€] | SPP [yıl] |
|---|---|---|---|---|---|---|---|
| 17 | Kazan baca gazı | Kurutma havası ön ısıtma | +++ | 150-250 | 20,000-80,000 | 15,000-40,000 | 0.5-1.5 |
| 18 | Kompresör atık ısı | Düşük sıcaklık kurutma | ++ | 70-90 | 5,000-15,000 | 8,000-15,000 | 1.0-2.5 |
| 19 | Kurutma egzozu | Kazan besleme suyu | ++ | 80-150 | 10,000-30,000 | 12,000-25,000 | 0.8-2.0 |
| 20 | Fırın/kiln egzozu | Kurutma havası | +++ | 250-600 | 40,000-150,000 | 40,000-100,000 | 0.5-1.5 |
| 21 | Kurutma egzozu | Bina ısıtma (kış) | + | 80-120 | 3,000-10,000 | 5,000-15,000 | 1.5-3.0 |

## 7. Karar Matrisi — Ekipmanlar Arası Entegrasyon (Decision Matrix)

### 7.1 Kapsamlı Kaynak-Hedef Kombinasyonları

| No | Kaynak (Source) | Hedef (Target) | Uyumluluk | T_kaynak [°C] | Tipik Tasarruf [€/yıl] | Yatırım [€] | SPP [yıl] | ROI [%] |
|---|---|---|---|---|---|---|---|---|
| 1 | Kompresör atık ısı | Kazan besleme suyu | +++ | 70–90 | 5,000–15,000 | 8,000–15,000 | 1.0–2.0 | 50–100 |
| 2 | Kompresör atık ısı | Bina ısıtma | +++ | 60–85 | 4,000–12,000 | 3,000–8,000 | 0.5–1.5 | 67–200 |
| 3 | Kompresör atık ısı | Sıcak kullanım suyu | ++ | 70–85 | 2,000–5,000 | 5,000–8,000 | 1.5–3.0 | 33–67 |
| 4 | Kazan baca gazı | Besleme suyu (economizer) | +++ | 150–250 | 15,000–50,000 | 15,000–40,000 | 0.5–2.0 | 50–200 |
| 5 | Kazan baca gazı | Yakma havası ön ısıtma | ++ | 200–400 | 10,000–30,000 | 20,000–50,000 | 1.5–3.0 | 33–67 |
| 6 | Kazan blowdown | Besleme suyu ön ısıtma | ++ | 140–180 | 3,000–10,000 | 5,000–10,000 | 1.0–2.0 | 50–100 |
| 7 | Kazan fazla buhar | Absorpsiyon chiller | ++ | 120–180 | 8,000–25,000 | 40,000–120,000 | 3.0–6.0 | 17–33 |
| 8 | Chiller kondenser | Sıcak su (desuperheater) | +++ | 70–90 | 8,000–20,000 | 8,000–15,000 | 0.8–1.5 | 67–125 |
| 9 | Chiller kondenser | Bina ısıtma | ++ | 35–45 | 5,000–15,000 | 10,000–25,000 | 1.5–3.0 | 33–67 |
| 10 | Chiller kondenser | Yerden ısıtma | +++ | 35–45 | 4,000–10,000 | 15,000–30,000 | 2.0–4.0 | 25–50 |
| 11 | Pompa VSD | Sistem enerji azaltma | +++ | — | 5,000–20,000 | 3,000–8,000 | 0.5–1.0 | 100–200 |
| 12 | Soğutma kulesi VSD | Fan enerji azaltma | +++ | — | 10,000–25,000 | 5,000–12,000 | 0.3–0.8 | 125–333 |
| 13 | Kompresör VSD | Enerji azaltma | +++ | — | 8,000–25,000 | 10,000–25,000 | 1.0–2.0 | 50–100 |
| 14 | Kazan kondensat | Besleme suyu geri dönüş | +++ | 80–100 | 5,000–20,000 | 5,000–15,000 | 0.5–1.5 | 67–200 |
| 15 | Chiller + kompresör | Ortak soğutma kulesi | ++ | — | 3,000–10,000 | 8,000–20,000 | 1.5–3.0 | 33–67 |
| 16 | CHP egzoz | Kazan besleme suyu | +++ | 450–550 | 20,000–80,000 | 30,000–80,000 | 1.0–2.5 | 40–100 |
| 17 | Türbin exhaust buhar | Proses ısıtma (BP CHP) | +++ | 120–200 | 30,000–200,000 | 300,000–2,000,000 | 3.0–6.0 | 17–33 |
| 18 | CHP elektrik | Fabrika ekipman besleme | +++ | — | 50,000–500,000 | 300,000–3,000,000 | 3.0–7.0 | 14–33 |
| 19 | Proses/motor atık ısı | ORC ile elektrik üretimi | ++ | 80–350 | 15,000–100,000 | 200,000–2,000,000 | 4.0–7.0 | 14–25 |

### 7.2 Uyumluluk Puanlama Kriterleri

```
+++ = Mükemmel uyum (3 puan):
  - Sıcaklık eşleşmesi ideal
  - Ekonomik geri dönüş <2 yıl
  - Uygulama basit, kanıtlanmış teknoloji

++ = İyi uyum (2 puan):
  - Sıcaklık eşleşmesi yeterli
  - Ekonomik geri dönüş 2–4 yıl
  - Uygulama orta karmaşıklık

+ = Sınırlı uyum (1 puan):
  - Sıcaklık eşleşmesi kısmi (ısı pompası gerekebilir)
  - Ekonomik geri dönüş 4–7 yıl
  - Özel koşullarda uygulanabilir

- = Uyumsuz (0 puan):
  - Sıcaklık yetersiz
  - Ekonomik değil
  - Teknik engeller yüksek
```

## 8. Entegrasyon Değerlendirme Kriterleri (Integration Assessment Criteria)

### 8.1 Teknik Uygunluk (Technical Suitability)

```
A. Sıcaklık Eşleştirme (Temperature Matching):
Puan = f(ΔT_uygun / ΔT_minimum)

| Kriter | Puan (1–5) | Koşul |
|--------|-----------|-------|
| 5 | Mükemmel | T_kaynak > T_kullanıcı + 30°C |
| 4 | İyi | T_kaynak > T_kullanıcı + 20°C |
| 3 | Yeterli | T_kaynak > T_kullanıcı + 10°C |
| 2 | Sınırlı | T_kaynak > T_kullanıcı + 5°C |
| 1 | Yetersiz | T_kaynak ≤ T_kullanıcı + 5°C |

B. Yük Profili Eşleştirme (Load Profile Matching):
Puan = Eşzamanlılık oranı × 5

| Eşzamanlılık | Puan (1–5) | Koşul |
|--------------|-----------|-------|
| 5 | Mükemmel | SR > 0.80 |
| 4 | İyi | SR = 0.60–0.80 |
| 3 | Yeterli | SR = 0.40–0.60 |
| 2 | Düşük | SR = 0.20–0.40 |
| 1 | Yetersiz | SR < 0.20 |

C. Fiziksel Mesafe (Physical Distance):
| Mesafe [m] | Puan (1–5) | Maliyet Etkisi |
|-----------|-----------|----------------|
| <10 | 5 | Minimal boru maliyeti |
| 10–25 | 4 | Düşük maliyet |
| 25–50 | 3 | Orta maliyet |
| 50–100 | 2 | Yüksek maliyet |
| >100 | 1 | Çok yüksek, runaround gerekli |
```

### 8.2 Ekonomik Uygunluk (Economic Suitability)

```
A. Enerji Maliyet Tasarrufu:
Puan = f(C_tasarruf / C_toplam_enerji)

| Tasarruf Oranı | Puan (1–5) |
|----------------|-----------|
| >%10 | 5 |
| %5–10 | 4 |
| %3–5 | 3 |
| %1–3 | 2 |
| <%1 | 1 |

B. Yatırım Geri Dönüşü:
| SPP [yıl] | Puan (1–5) |
|-----------|-----------|
| <1 | 5 |
| 1–2 | 4 |
| 2–3 | 3 |
| 3–5 | 2 |
| >5 | 1 |

C. NPV/Yatırım Oranı:
| NPV/C₀ | Puan (1–5) |
|---------|-----------|
| >3.0 | 5 |
| 2.0–3.0 | 4 |
| 1.0–2.0 | 3 |
| 0.5–1.0 | 2 |
| <0.5 | 1 |
```

### 8.3 Operasyonel Değerlendirme (Operational Considerations)

```
A. Bakım Gereksinimi:
| Seviye | Puan (1–5) | Açıklama |
|--------|-----------|----------|
| Minimal | 5 | Yılda 1 kontrol yeterli |
| Düşük | 4 | 6 ayda 1 bakım |
| Orta | 3 | 3 ayda 1 bakım |
| Yüksek | 2 | Aylık bakım |
| Çok yüksek | 1 | Haftalık bakım/izleme |

B. Operasyonel Esneklik:
| Seviye | Puan (1–5) | Açıklama |
|--------|-----------|----------|
| Tam bağımsız | 5 | Bir ekipman dursa diğeri etkilenmez |
| Bypass mevcut | 4 | Bypass ile bağımsız çalışabilir |
| Kısmen bağımlı | 3 | Kısa süreli bağımsız çalışabilir |
| Bağımlı | 2 | Her iki ekipman birlikte çalışmalı |
| Tamamen bağımlı | 1 | Biri durduğunda diğeri de durur |

C. Yedek Sistem Gereksinimi:
| Yedek İhtiyacı | Puan (1–5) | Açıklama |
|----------------|-----------|----------|
| Yedek gereksiz | 5 | Mevcut sistem yedek görevi görür |
| Mevcut yedek yeterli | 4 | Ek yedek gerekmiyor |
| Kısmi yedek | 3 | Küçük yedek ekipman gerekli |
| Tam yedek | 2 | Paralel yedek gerekli |
| Kritik yedek | 1 | N+1 yedeklilik zorunlu |
```

### 8.4 Toplam Entegrasyon Puanı Hesaplama

```
Toplam puan hesaplama formülü:

P_toplam = w₁×P_sıcaklık + w₂×P_yük + w₃×P_mesafe +
           w₄×P_tasarruf + w₅×P_SPP + w₆×P_NPV +
           w₇×P_bakım + w₈×P_esneklik + w₉×P_yedek

Ağırlıklar (varsayılan):
| Kriter | Ağırlık | Kategori |
|--------|---------|----------|
| Sıcaklık eşleştirme | w₁ = 0.15 | Teknik |
| Yük profili | w₂ = 0.12 | Teknik |
| Mesafe | w₃ = 0.08 | Teknik |
| Enerji tasarrufu | w₄ = 0.15 | Ekonomik |
| SPP | w₅ = 0.15 | Ekonomik |
| NPV/Yatırım | w₆ = 0.10 | Ekonomik |
| Bakım | w₇ = 0.10 | Operasyonel |
| Esneklik | w₈ = 0.08 | Operasyonel |
| Yedek | w₉ = 0.07 | Operasyonel |
| TOPLAM | 1.00 | |

Karar eşikleri:
P_toplam ≥ 4.0: Mükemmel fırsat → hemen uygula
P_toplam ≥ 3.0: İyi fırsat → planlı yatırım
P_toplam ≥ 2.0: Orta fırsat → detaylı fizibilite yap
P_toplam < 2.0: Düşük fırsat → şimdilik ertele
```

## 9. ExergyLab Entegrasyon Algoritması (Platform Integration Algorithm)

### 9.1 Algoritma Akış Diyagramı

```
┌──────────────────────────────────────────────────────────────┐
│                 ExergyLab Entegrasyon Motoru                  │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  AŞAMA 1: VERİ TOPLAMA                                       │
│  ┌─────────────┐ ┌─────────────┐ ┌──────────┐ ┌──────────┐  │
│  │ Kazan       │ │ Kompresör   │ │ Chiller  │ │ Pompa    │  │
│  │ verileri    │ │ verileri    │ │ verileri │ │ verileri │  │
│  └──────┬──────┘ └──────┬──────┘ └─────┬────┘ └─────┬────┘  │
│         └───────────────┴──────────────┴────────────┘        │
│                          │                                    │
│  AŞAMA 2: ATIK ISI PROFİLİ ÇIKARMA                          │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ Her ekipman için:                                    │     │
│  │ - Atık ısı miktarı [kW]                             │     │
│  │ - Atık ısı sıcaklığı [°C]                           │     │
│  │ - Çalışma süresi [saat/yıl]                         │     │
│  │ - Yük profili [saatlik/günlük]                      │     │
│  └──────────────────────┬──────────────────────────────┘     │
│                          │                                    │
│  AŞAMA 3: ISI İHTİYACI PROFİLİ ÇIKARMA                      │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ Her ekipman/proses için:                             │     │
│  │ - Isı ihtiyacı [kW]                                 │     │
│  │ - Gerekli sıcaklık [°C]                             │     │
│  │ - Çalışma süresi [saat/yıl]                         │     │
│  │ - Mevsimsellik faktörü                              │     │
│  └──────────────────────┬──────────────────────────────┘     │
│                          │                                    │
│  AŞAMA 4: EŞLEŞTİRME MATRİSİ                               │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ Her kaynak-hedef çifti için:                         │     │
│  │ 1. Sıcaklık kontrolü: T_kaynak > T_hedef + ΔT_min? │     │
│  │ 2. Kapasite eşleştirme: Q̇_kaynak vs Q̇_hedef        │     │
│  │ 3. Zaman eşleştirme: Eşzamanlılık oranı (SR)       │     │
│  │ 4. Ön ekonomik değerlendirme                        │     │
│  └──────────────────────┬──────────────────────────────┘     │
│                          │                                    │
│  AŞAMA 5: PUANLAMA VE SIRALAMA                               │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ Her uyumlu çift için:                                │     │
│  │ - Teknik puan (sıcaklık + yük + mesafe)             │     │
│  │ - Ekonomik puan (tasarruf + SPP + NPV)              │     │
│  │ - Operasyonel puan (bakım + esneklik + yedek)       │     │
│  │ → Toplam puan = Σ(wᵢ × Pᵢ)                         │     │
│  │ → Sıralama: Puan büyükten küçüğe                    │     │
│  └──────────────────────┬──────────────────────────────┘     │
│                          │                                    │
│  AŞAMA 6: ÖNERİ LİSTESİ OLUŞTURMA                           │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ Kullanıcıya sunulan çıktı:                           │     │
│  │ 1. Öncelik sıralı entegrasyon fırsatları listesi    │     │
│  │ 2. Her fırsat için: tasarruf, yatırım, SPP, NPV    │     │
│  │ 3. Uygulama zorluğu değerlendirmesi                 │     │
│  │ 4. Birbirine bağımlı projelerin gruplandırılması    │     │
│  │ 5. Toplam portföy ekonomik özeti                    │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### 9.2 Algoritma Kuralları (Rule Engine)

```
Kural Seti 1 — Kompresör Atık Isı:
IF kompresör_gücü > 15 kW AND soğutma_tipi = "su"
  AND kazan_besleme_T < 60°C
THEN öneri: "Kompresör → Kazan besleme suyu ön ısıtma"
  Q̇_geri = kompresör_gücü × yük_oranı × 0.70
  SPP_tahmini = f(Q̇_geri, mesafe, yakıt_fiyatı)

Kural Seti 2 — Kompresör Bina Isıtma:
IF kompresör_gücü > 15 kW AND soğutma_tipi = "hava"
  AND bina_ısıtma_ihtiyacı = TRUE AND iklim = "soğuk/ılıman"
THEN öneri: "Kompresör → Bina ısıtma (kanal yönlendirme)"
  Q̇_ısıtma = kompresör_gücü × 0.94 × 0.90
  SPP_tahmini = f(Q̇_ısıtma, kanal_mesafesi, yakıt_fiyatı)

Kural Seti 3 — Kazan Economizer:
IF kazan_baca_T > 160°C AND economizer_mevcut = FALSE
THEN öneri: "Kazan baca gazı economizer"
  Q̇_eco = f(baca_T, baca_debisi)
  SPP_tahmini < 2.0 yıl (tipik)

Kural Seti 4 — Chiller Isı Geri Kazanım:
IF chiller_kapasitesi > 100 kW AND desuperheater = FALSE
  AND sıcak_su_ihtiyacı = TRUE
THEN öneri: "Chiller desuperheater → sıcak su"
  Q̇_desup = chiller_kapasitesi × 0.12
  SPP_tahmini < 1.5 yıl (tipik)

Kural Seti 5 — Pompa VSD:
IF pompa_gücü > 5 kW AND VSD_mevcut = FALSE
  AND kontrol_yöntemi = "vana_kısma"
THEN öneri: "Pompa VSD retrofit"
  tasarruf = f(yük_profili, nominal_güç)
  SPP_tahmini < 1.0 yıl (tipik)

Kural Seti 6 — CHP Değerlendirme:
IF kazan_yakıt > 500 kW AND elektrik_tüketim > 200 kW
  AND çalışma_süresi > 4,000 h/yıl
  AND doğalgaz_bağlantısı = TRUE
THEN öneri: "CHP fizibilite çalışması önerilir"
  CHP_boyut = f(termal_taban_yük, HPR)
  SPP_tahmini = 3–5 yıl

Kural Seti 7 — Absorption Chiller:
IF kazan_kapasite > minimum_ihtiyaç × 1.3
  AND chiller_kapasitesi > 100 kW AND yaz_buhar_fazlası = TRUE
THEN öneri: "Fazla buhar → Absorpsiyon chiller (CCHP)"
  Q̇_abs = Q̇_buhar_fazlası × COP_abs
  SPP_tahmini = 4–6 yıl

Kural Seti 8 — PRV Değiştirme (Buhar Türbini):
IF PRV_mevcut = TRUE AND ṁ_buhar > 3 ton/h
  AND ΔP_PRV > 10 bar AND çalışma_süresi > 4,000 h/yıl
THEN öneri: "PRV yerine mikro/küçük buhar türbini kur"
  Ẇ_potansiyel = ṁ × (h_HP - h_LP) × η_is × η_mek × η_jen
  Referans: steam_turbine/equipment/micro_turbine.md
  SPP_tahmini = 2–5 yıl
```

### 9.3 Entegrasyon Çakışma Yönetimi

```
Aynı ısı kaynağı birden fazla hedefe önerildiğinde:

Örnek: Kompresör atık ısısı (30 kW)
→ Hedef A: Kazan besleme suyu (puan: 4.2)
→ Hedef B: Bina ısıtma (puan: 3.8)
→ Hedef C: Sıcak su (puan: 3.5)

Çözüm stratejileri:

1. Öncelik bazlı atama:
   → En yüksek puanlı hedefe tam atama
   → Kalan ısı varsa sıradakine

2. Kademeli atama:
   → Kompresör sıcak su çıkışı (85°C) → Kazan besleme (20 kW)
   → Kalan (65°C su) → Bina ısıtma (10 kW)
   → Sıcaklık kademesi ile toplam kullanım optimize

3. Mevsimsel atama:
   → Kış: Bina ısıtma (öncelik 1)
   → Yaz: Kazan besleme suyu (öncelik 1)
   → Tüm yıl: Sıcak su (sabit ihtiyaç)

Platform varsayılan: Strateji 2 (kademeli atama)
Kullanıcı tercihi ile değiştirilebilir.
```

## 10. Kapsamlı Hesaplama Örnekleri (Comprehensive Worked Examples)

### 10.1 Örnek Fabrika Profili

```
Orta ölçekli gıda fabrikası:
- Kazan: 4 ton/h buhar, doğalgaz, η = %88, baca T = 195°C
- Kompresör: 55 kW vidalı, su soğutmalı, 6,500 h/yıl, %75 yük
- Chiller: 300 kW su soğutmalı, COP = 4.2, 5,000 h/yıl
- Pompalar: 3 × 15 kW (soğutma suyu), vana kısmalı
- Soğutma kulesi: 2 × 11 kW fan, sürekli çalışma
- Doğalgaz: €0.045/kWh, Elektrik: €0.12/kWh
- Bina ısıtma ihtiyacı: 100 kW (3,000 h/yıl kış)
- Sıcak su ihtiyacı: 15 kW (6,500 h/yıl)
```

### 10.2 Otomatik Tespit ve Puanlama

```
ExergyLab tespit sonuçları:

Fırsat 1: Kompresör → Kazan besleme suyu
├── Q̇_geri = 55 × 0.75 × 0.70 = 28.9 kW
├── Yıllık tasarruf: 28.9 × 6,500 / 0.88 × €0.045 = €9,608/yıl
├── Yatırım: €10,000
├── SPP = 1.04 yıl
├── Teknik puan: 4.2/5
├── Ekonomik puan: 4.0/5
├── Operasyonel puan: 4.5/5
└── TOPLAM: 4.15/5 ★★★★ (Mükemmel)

Fırsat 2: Kazan economizer
├── Q̇_eco = 85 kW (195°C → 130°C, η = 0.75)
├── Yıllık tasarruf: 85 × 6,500 / 0.88 × €0.045 = €28,267/yıl
├── Yatırım: €25,000
├── SPP = 0.88 yıl
├── Teknik puan: 4.5/5
├── Ekonomik puan: 4.5/5
├── Operasyonel puan: 4.0/5
└── TOPLAM: 4.38/5 ★★★★ (Mükemmel)

Fırsat 3: Chiller desuperheater → sıcak su
├── Q̇_desup = 300 × 0.12 = 36 kW
├── Kullanılan kısım: 15 kW (sıcak su ihtiyacı)
├── Yıllık tasarruf: 15 × 5,000 / 0.88 × €0.045 = €3,835/yıl
├── Yatırım: €8,000
├── SPP = 2.09 yıl
├── Teknik puan: 3.5/5
├── Ekonomik puan: 3.0/5
├── Operasyonel puan: 4.0/5
└── TOPLAM: 3.40/5 ★★★ (İyi)

Fırsat 4: Pompa VSD retrofit (3 × 15 kW)
├── Ortalama yük: %65 (kısma ile)
├── VSD ile güç: 15 × (0.65)³ = 4.1 kW (her pompa)
├── Tasarruf: 3 × (15 - 4.1) = 32.7 kW
├── Yıllık tasarruf: 32.7 × 6,500 × €0.12 = €25,506/yıl
├── Yatırım: €12,000 (3 × €4,000)
├── SPP = 0.47 yıl
├── Teknik puan: 4.5/5
├── Ekonomik puan: 5.0/5
├── Operasyonel puan: 4.5/5
└── TOPLAM: 4.68/5 ★★★★★ (Mükemmel)

Fırsat 5: Soğutma kulesi VSD
├── Ortalama yük: %55
├── VSD ile güç: 2 × 11 × (0.55)³ = 3.7 kW
├── Tasarruf: 22 - 3.7 = 18.3 kW
├── Yıllık tasarruf: 18.3 × 8,000 × €0.12 = €17,568/yıl
├── Yatırım: €6,000
├── SPP = 0.34 yıl
├── Teknik puan: 4.5/5
├── Ekonomik puan: 5.0/5
├── Operasyonel puan: 4.5/5
└── TOPLAM: 4.68/5 ★★★★★ (Mükemmel)

Fırsat 6: Kompresör → Bina ısıtma (kış)
├── Q̇ = 55 × 0.75 × 0.50 = 20.6 kW (hava kanalı eşdeğeri)
├── NOT: Kaynak zaten Fırsat 1'de kullanılıyor
├── Kademeli: Fırsat 1'den sonra kalan ısı ile
├── Kalan: Q̇_kalan ≈ 12 kW (düşük sıcaklık kısmı)
├── Yıllık tasarruf: 12 × 3,000 / 0.90 × €0.045 = €1,800/yıl
├── Yatırım: €4,000
├── SPP = 2.22 yıl
└── TOPLAM: 2.85/5 ★★★ (Orta)
```

### 10.3 Toplam Portföy Özeti

```
ExergyLab Entegrasyon Portföy Özeti
══════════════════════════════════════════════════════════════

Sıra │ Fırsat                        │ Yatırım [€] │ Tasarruf [€/yıl] │ SPP [yıl]
─────┼───────────────────────────────┼─────────────┼──────────────────┼──────────
  1  │ Pompa VSD retrofit            │    12,000    │     25,506       │   0.47
  2  │ Soğutma kulesi VSD            │     6,000    │     17,568       │   0.34
  3  │ Kazan economizer              │    25,000    │     28,267       │   0.88
  4  │ Kompresör → besleme suyu      │    10,000    │      9,608       │   1.04
  5  │ Chiller desuperheater         │     8,000    │      3,835       │   2.09
  6  │ Kompresör → bina ısıtma       │     4,000    │      1,800       │   2.22
─────┼───────────────────────────────┼─────────────┼──────────────────┼──────────
     │ TOPLAM                        │    65,000    │     86,584       │   0.75
══════════════════════════════════════════════════════════════

Toplam yatırım: €65,000
Toplam yıllık tasarruf: €86,584/yıl
Bileşik geri ödeme: 0.75 yıl (9 ay)
NPV (10 yıl, %10): €467,000
Toplam enerji tasarrufu: ~%22
CO₂ azaltımı: ~185 ton/yıl

Uygulama önerisi:
Faz 1 (0–3 ay): Pompa VSD + Soğutma kulesi VSD (€18,000, €43,074/yıl)
Faz 2 (3–6 ay): Kazan economizer (€25,000, €28,267/yıl)
Faz 3 (6–12 ay): Kompresör ısı geri kazanım + chiller desuperheater (€22,000, €15,243/yıl)
```

## 11. Entegrasyon Karar Akış Diyagramı (Decision Flowchart)

```
                ┌────────────────────────────┐
                │  Ekipman verilerini topla    │
                │  (kazan, kompresör, chiller, │
                │   pompa, soğutma kulesi)     │
                └─────────────┬──────────────┘
                              │
                ┌─────────────▼──────────────┐
                │  Atık ısı kaynaklarını       │
                │  tespit et                   │
                └─────────────┬──────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                   │
    ┌──────▼──────┐   ┌──────▼──────┐    ┌───────▼──────┐
    │ Kompresör   │   │ Kazan baca  │    │ Chiller      │
    │ atık ısı    │   │ gazı        │    │ kondenser    │
    │ (70-90°C)   │   │ (150-250°C) │    │ (35-90°C)    │
    └──────┬──────┘   └──────┬──────┘    └───────┬──────┘
           │                  │                   │
    ┌──────▼──────┐   ┌──────▼──────┐    ┌───────▼──────┐
    │ Besleme suyu│   │ Economizer  │    │ Desuperheater│
    │ ön ısıtma   │   │ var mı?     │    │ var mı?      │
    │ T<60°C?     │   │             │    │              │
    └───┬────┬────┘   └───┬────┬────┘    └───┬─────┬────┘
    Evet│    │Hayır    Hayır│   │Evet     Hayır│    │Evet
        │    │            │    │              │     │
    ┌───▼─┐ │        ┌───▼──┐ │         ┌───▼──┐  │
    │ÖNERİ│ │        │ÖNERİ │ │         │ÖNERİ │  │
    │1    │ │        │Eco.  │ │         │DSH   │  │
    └─────┘ │        │ekle  │ │         │ekle  │  │
            │        └──────┘ │         └──────┘  │
     ┌──────▼──────┐          │                   │
     │ Bina ısıtma │          │                   │
     │ ihtiyacı?   │  ┌──────▼──────┐    ┌───────▼──────┐
     └───┬────┬────┘  │ Baca T      │    │ Isı geri     │
     Evet│    │Hayır   │ optimize?   │    │ kazanımlı    │
         │    │        └─────────────┘    │ chiller?     │
     ┌───▼─┐ ┌▼────┐                     └──────────────┘
     │ÖNERİ│ │DHW  │
     │bina │ │öner │
     └─────┘ └─────┘
                              │
                ┌─────────────▼──────────────┐
                │  VSD fırsatlarını tara       │
                │  (pompalar, fanlar,          │
                │   kompresörler)              │
                └─────────────┬──────────────┘
                              │
                ┌─────────────▼──────────────┐
                │  Tüm fırsatları puanla      │
                │  ve sırala                   │
                └─────────────┬──────────────┘
                              │
                ┌─────────────▼──────────────┐
                │  Portföy önerisi oluştur    │
                │  (fazlı uygulama planı)     │
                └────────────────────────────┘
```

## 12. Performans Sınıflandırması (Çapraz Ekipman Entegrasyonu)

| Performans Kriteri | Düşük | Ortalama | İyi | Mükemmel | Kritik |
|---|---|---|---|---|---|
| Uygulanan entegrasyon sayısı | 0 | 1–2 | 3–4 | >4 | — |
| Toplam enerji tasarrufu | <%5 | %5–15 | %15–25 | >%25 | — |
| Atık ısı geri kazanım oranı | <%10 | %10–30 | %30–50 | >%50 | — |
| Portföy SPP | >4 yıl | 2–4 yıl | 1–2 yıl | <1 yıl | — |
| ExergyLab entegrasyon puanı | <2.0 | 2.0–3.0 | 3.0–4.0 | >4.0 | — |
| Ekipmanlar arası iletişim | Yok | Kısmi | Tam | Tam + AI | Yok + eski sistem |

## İlgili Dosyalar

- [Isı Entegrasyonu](heat_integration.md) — Kaynak-kullanım eşleştirme detayları
- [Atık Isı Geri Kazanım](waste_heat_recovery.md) — WHR teknoloji detayları ve seçim
- [Kojenerasyon](cogeneration.md) — CHP/CCHP entegrasyon fırsatları
- [Proses Entegrasyonu](process_integration.md) — Proses düzeyinde entegrasyon
- [Ekonomik Analiz](economic_analysis.md) — Yatırım değerlendirme metodları
- [KPI Tanımları](kpi_definitions.md) — Entegrasyon KPI'ları
- [Kazan Formülleri](../boiler/formulas.md) — Kazan verimlilik hesaplamaları
- [Kazan Benchmarkları](../boiler/benchmarks.md) — Kazan performans referansları
- [Kazan Çözümleri](../boiler/solutions/) — Kazan tarafı iyileştirme önerileri
- [Kompresör Formülleri](../compressor/formulas.md) — Kompresör enerji hesaplamaları
- [Kompresör Benchmarkları](../compressor/benchmarks.md) — Kompresör performans verileri
- [Kompresör Çözümleri](../compressor/solutions/) — Kompresör optimizasyon önerileri
- [Chiller Formülleri](../chiller/formulas.md) — Chiller COP ve enerji hesaplamaları
- [Chiller Benchmarkları](../chiller/benchmarks.md) — Chiller performans referansları
- [Chiller Çözümleri](../chiller/solutions/) — Chiller optimizasyon önerileri
- [Pompa Formülleri](../pump/formulas.md) — Pompa enerji hesaplamaları
- [Pompa Çözümleri](../pump/solutions/) — Pompa optimizasyon önerileri
- [Kurutma Formülleri](../dryer/formulas.md) — Kurutma exergy hesaplamaları
- [Kurutma Benchmarkları](../dryer/benchmarks.md) — Kurutma performans referansları
- [Kurutma Çözümleri](../dryer/solutions/) — Kurutma optimizasyon önerileri
- [Kurutma Egzoz Isı Geri Kazanımı](../dryer/solutions/exhaust_heat_recovery.md) — Egzoz WHR detayları
- [Buhar Türbini Formülleri](../steam_turbine/formulas.md) — Türbin exergy hesaplamaları
- [Buhar Türbini Benchmarkları](../steam_turbine/benchmarks.md) — Türbin verim karşılaştırma
- [Buhar Türbini CHP](../steam_turbine/systems/steam_turbine_chp.md) — CHP konfigürasyonları
- [ORC](../steam_turbine/equipment/orc.md) — Atık ısıdan elektrik (düşük T)
- [Mikro Türbin PRV](../steam_turbine/equipment/micro_turbine.md) — PRV ikamesi
- [CHP Fizibilite](../steam_turbine/economics/feasibility.md) — CHP yatırım fizibilitesi
- [Isı Eşanjörü Benchmarklar](../heat_exchanger/benchmarks.md) — Eşanjör performans verileri
- [Isı Eşanjörü Çözümleri](../heat_exchanger/solutions/heat_recovery.md) — Isı geri kazanım detayları
- [Exergy Temelleri](exergy_fundamentals.md) — Exergy analizi temelleri
- [Sistem Sınırları](system_boundaries.md) — Entegrasyon sınır tanımları

## Referanslar

- Kemp, I.C., "Pinch Analysis and Process Integration," Butterworth-Heinemann, 2nd Edition, 2007
- US DOE, "Waste Heat Recovery: Technology and Opportunities in U.S. Industry," 2008
- US DOE, "Improving Compressed Air System Performance — A Sourcebook for Industry," 2003
- US DOE, "Improving Steam System Performance — A Sourcebook for Industry," 2nd Edition, 2012
- US DOE, "Improving Pumping System Performance — A Sourcebook for Industry," 2006
- ASHRAE, "ASHRAE Handbook — HVAC Systems and Equipment," 2020
- Thumann, A. & Mehta, D.P., "Handbook of Energy Engineering," 7th Edition, Fairmont Press, 2013
- Dincer, I. & Rosen, M.A., "Exergy: Energy, Environment and Sustainable Development," Elsevier, 3rd Edition, 2021
- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1982
- European Commission, "Reference Document on Best Available Techniques for Energy Efficiency," 2009
- Klemeš, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Arpagaus, C. et al., "High temperature heat pumps: Market overview, state of the art," Energy, 2018
- Turner, W.C. & Doty, S., "Energy Management Handbook," 9th Edition, Fairmont Press, 2013
