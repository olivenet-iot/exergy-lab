---
title: "Ekipman Bazında İdeal ve Kaçınılamaz Koşullar (Ideal & Unavoidable Conditions per Equipment)"
category: factory
equipment_type: factory
keywords: [ideal koşullar, kaçınılamaz koşullar, unavoidable exergy destruction, advanced exergy, BAT, izentropik verim, kaçınılabilir kayıp, tersinmezlik, sınır koşullar]
related_files: [factory/advanced_exergy/equipment_specific, factory/cross_equipment.md, factory/waste_heat_recovery.md, factory/heat_integration.md, compressor/benchmarks.md, boiler/benchmarks.md, chiller/benchmarks.md, pump/benchmarks.md, dryer/benchmarks.md, steam_turbine/benchmarks.md, heat_exchanger/benchmarks.md]
use_when: ["İleri exergy analizinde ideal ve kaçınılamaz koşullar tanımlanırken", "Kaçınılabilir exergy yıkımı hesaplanırken", "BAT karşılaştırması yapılırken", "Ekipman bazında tersinmezlik alt sınırları belirlenirken"]
priority: critical
last_updated: 2025-05-15
---
# Ekipman Bazında İdeal ve Kaçınılamaz Koşullar (Ideal & Unavoidable Conditions per Equipment)

> Son güncelleme: 2025-05-15

## Genel Bakış

İleri exergy analizi (advanced exergy analysis), toplam exergy yıkımını (Ė_D) kaçınılabilir (avoidable) ve kaçınılamaz (unavoidable) bileşenlerine ayırır. Bu ayrım için her ekipmanın iki referans koşulunun tanımlanması gereklidir:

1. **İdeal koşullar (Ideal conditions):** Tersinir (reversible) çalışma durumu. Tüm tersinmezlikler sıfır, verimler %100.
2. **Kaçınılamaz koşullar (Unavoidable conditions):** Mevcut en iyi teknoloji (BAT — Best Available Technology) ve ekonomik/fiziksel sınırlamalar dahilinde ulaşılabilecek en iyi performans. Bu koşullarda bile bir miktar tersinmezlik kaçınılmazdır.

Bu dosya, ExergyLab platformunun ileri exergy analizinde kullandığı tüm referans parametrelerin **merkezi kaynağıdır**. Diğer tüm ileri exergy dosyaları bu dosyaya referans verir.

```
Temel ilişki:

Ė_D,toplam = Ė_D,kaçınılamaz + Ė_D,kaçınılabilir

Burada:
- Ė_D,toplam    = Gerçek çalışma koşullarındaki exergy yıkımı [kW]
- Ė_D,kaçınılamaz = Kaçınılamaz koşullarda hesaplanan exergy yıkımı [kW]
- Ė_D,kaçınılabilir = İyileştirme potansiyeli [kW]

İyileştirme potansiyeli oranı:
IP = Ė_D,kaçınılabilir / Ė_D,toplam × 100 [%]
```

## 1. Kompresör İdeal ve Kaçınılamaz Koşulları (Compressor Ideal/Unavoidable Conditions)

### 1.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| İzentropik verim (isentropic efficiency) | η_is | 1.00 | 0.92-0.95 | BAT vidalı: 0.92, santrifüj: 0.95 |
| Mekanik verim (mechanical efficiency) | η_mech | 1.00 | 0.98-0.99 | Modern rulmanlar ve güç aktarma |
| Motor verimi (motor efficiency) | η_motor | 1.00 | 0.96-0.97 | IE4 sınıfı yüksek verimli motor |
| Aftercooler yaklaşım ΔT (approach temperature) | ΔT_ac | 0 °C | 5 °C | Plate tipi ısı eşanjörü minimum |
| Ara soğutucu basınç düşüşü (intercooler ΔP) | ΔP_ic | 0 bar | 0.05-0.10 bar | Minimum akış direnci |
| Hava kaçağı (air leakage) | L | 0% | 2-3% | Yeni, iyi bakımlı sistem |
| Yağ taşınımı (oil carryover) | — | 0 ppm | 3-5 ppm | BAT yağ ayırıcı |

### 1.2 Alt Tip Bazlı Kaçınılamaz Koşullar

```
Vidalı kompresör (Rotary screw):
- η_is,UN = 0.92 (BAT profil optimizasyonlu rotor)
- η_mech,UN = 0.98
- η_motor,UN = 0.96 (37 kW üzeri IE4)
- Spesifik güç (UN): 5.5-6.0 kW/(m³/min) @ 7 bar
- Referans: Tsatsaronis & Park (2002), Kelly et al. (2009)

Pistonlu kompresör (Reciprocating):
- η_is,UN = 0.90 (BAT çok kademeli, ara soğutmalı)
- η_mech,UN = 0.97 (krank-biyel kayıpları)
- η_motor,UN = 0.96
- Spesifik güç (UN): 5.2-5.8 kW/(m³/min) @ 7 bar
- Not: Pistonlu kompresörlerde valf kayıpları η_is'yi sınırlar.

Santrifüj kompresör (Centrifugal):
- η_is,UN = 0.95 (BAT aerodynamik tasarım)
- η_mech,UN = 0.99 (manyetik rulman ile)
- η_motor,UN = 0.97 (büyük güçlerde IE4+)
- Spesifik güç (UN): 5.0-5.5 kW/(m³/min) @ 7 bar
- Referans: Morosuk & Tsatsaronis (2009)

Scroll kompresör (Scroll):
- η_is,UN = 0.88 (küçük kapasite, geometrik kısıt)
- η_mech,UN = 0.98
- η_motor,UN = 0.95 (küçük güç, IE3/IE4)
- Spesifik güç (UN): 6.0-7.0 kW/(m³/min) @ 7 bar
```

### 1.3 Sayısal Örnek — Vidalı Kompresör

```
Gerçek çalışma koşulları:
- Güç: 55 kW, Debi: 8.5 m³/min, Basınç: 7 bar(g)
- η_is = 0.78, η_mech = 0.95, η_motor = 0.93
- Spesifik güç: 55/8.5 = 6.47 kW/(m³/min)

İdeal koşullar:
- η_is = 1.00, η_mech = 1.00, η_motor = 1.00
- Ẇ_ideal = 8.5 × [k/(k-1)] × P₁ × [(P₂/P₁)^((k-1)/k) - 1] / (η_is × η_mech)
  (İzentropik sıkıştırma hesabı)
- Ẇ_ideal ≈ 36.2 kW → Ė_D,ideal = 0 kW

Kaçınılamaz koşullar:
- η_is,UN = 0.92, η_mech,UN = 0.98, η_motor,UN = 0.96
- Ẇ_UN = 36.2 / (0.92 × 0.98) / 0.96 ≈ 41.8 kW
- Ė_D,UN = 41.8 - 36.2 = 5.6 kW

Gerçek exergy yıkımı:
- Ė_D,toplam = 55 - 36.2 = 18.8 kW

Kaçınılabilir exergy yıkımı:
- Ė_D,AV = 18.8 - 5.6 = 13.2 kW
- IP = 13.2 / 18.8 × 100 = %70.2

Yorum: Kompresör exergy yıkımının %70'i kaçınılabilir.
Öncelikli iyileştirme alanları: η_is (en büyük etki), η_motor.
```

## 2. Kazan İdeal ve Kaçınılamaz Koşulları (Boiler Ideal/Unavoidable Conditions)

### 2.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| Yanma tersinmezliği (combustion irreversibility) | ε_comb | 0% | 25-30% | Kimyasal → termal dönüşüm termodinamik limiti |
| Baca gazı sıcaklığı (flue gas temperature) | T_bg | T₀ (ortam) | 130°C (doğalgaz), 160°C (fuel oil) | Asit çiğ noktası (acid dew point) riski |
| Termal verim (thermal efficiency) | η_th | 100% | 95-96% | BAT yoğuşmalı kazan (condensing boiler) |
| Fazla hava (excess air) | EA | 0% | 5-8% | Optimum yanma koşulları |
| Isı transfer ΔT (heat transfer temperature diff.) | ΔT_ht | 0 °C | 15-25 °C | Alev → tüp/duvar minimum sıcaklık farkı |
| Radyasyon kaybı (radiation loss) | Q_rad | 0% | 0.5-1.0% | BAT yalıtım standartları |
| Yanmamış kayıp (unburned loss) | L_ub | 0% | 0.1-0.5% | CO < 50 ppm kontrolü |
| Blowdown kaybı (blowdown loss) | L_bd | 0% | 1-2% | Minimum TDS kontrolü |

### 2.2 Alt Tip Bazlı Kaçınılamaz Koşullar

```
Ateş borulu kazan (Fire-tube boiler):
- η_th,UN = 93-94% (LHV bazlı)
- T_bg,UN = 140°C (doğalgaz), 170°C (fuel oil)
- EA_UN = 8-10%
- ΔT_ht,UN = 20-25°C (iç yüzey → kaynama suyu)
- Radyasyon kaybı_UN = 0.8-1.0%
- Referans: Tsatsaronis (2002), Bejan et al. (1996)

Su borulu kazan (Water-tube boiler):
- η_th,UN = 94-95% (LHV bazlı)
- T_bg,UN = 135°C (doğalgaz), 165°C (fuel oil)
- EA_UN = 5-8%
- ΔT_ht,UN = 15-20°C (daha iyi ısı transfer konfigürasyonu)
- Radyasyon kaybı_UN = 0.5-0.8%

Yoğuşmalı kazan (Condensing boiler):
- η_th,UN = 95-97% (LHV bazlı) — >100% HHV referanslı mümkün
- T_bg,UN = 55-70°C (yoğuşma sağlanır)
- EA_UN = 5-8%
- ΔT_ht,UN = 10-15°C (kondenserli bölüm dahil)
- Koşul: Dönüş suyu T < 55°C olmalı
- Referans: Petrakopoulou et al. (2012)

Atık ısı kazanı (Waste heat boiler — HRSG):
- η_th,UN = 85-90% (kaynak sıcaklığına bağlı)
- T_bg,UN = 100-120°C (düşük kükürt gazı)
- ΔT_ht,UN = 15-25°C (pinch noktası)
- Basınç seviye sayısına bağlı verim artışı:
  Tek seviye: η ≈ 75-80%, Çift: 82-87%, Üç: 85-90%
- Referans: Kelly (2008)

Biyokütle kazanı (Biomass boiler):
- η_th,UN = 88-91% (LHV bazlı)
- T_bg,UN = 150-180°C (yüksek nem + kül, korozyon riski)
- EA_UN = 20-30% (heterojen yakıt)
- Yanmamış kayıp_UN = 1-3% (kül içeriği yüksek)
```

### 2.3 Yanma Tersinmezliği Detayı

```
Yanma süreci, termodinamiğin en büyük tersinmezlik kaynağıdır.
Yakıtın kimyasal exergy'si, yanma ürünlerinin termal exergy'sine dönüşür.

Yanma exergy verimi:
ε_yanma = Ė_ürünler / Ė_yakıt

Kaçınılamaz yanma tersinmezliği:
- Doğalgaz (CH₄): ε_yanma,UN ≈ 0.70-0.75 → %25-30 kaçınılamaz kayıp
- Fuel oil: ε_yanma,UN ≈ 0.68-0.73 → %27-32 kaçınılamaz kayıp
- Kömür: ε_yanma,UN ≈ 0.65-0.70 → %30-35 kaçınılamaz kayıp
- Biyokütle: ε_yanma,UN ≈ 0.60-0.68 → %32-40 kaçınılamaz kayıp

NOT: Bu tersinmezlik yakıtın kimyasal doğasından kaynaklanır ve
hiçbir teknolojik iyileştirme ile ortadan kaldırılamaz.
Yanma sıcaklığını artırmak (oksijen zenginleştirme, ön ısıtma)
kısmen azaltabilir ancak tamamen gideremez.

Referans: Bejan, Tsatsaronis & Moran (1996), Bölüm 3.6
         Szargut et al. (1988), Bölüm 4
```

### 2.4 Sayısal Örnek — Ateş Borulu Doğalgaz Kazanı

```
Gerçek çalışma koşulları:
- Kapasite: 6 ton/h buhar @ 10 bar
- Yakıt: Doğalgaz, Q̇_yakıt = 4,500 kW (LHV bazlı)
- η_th = 88%, T_bg = 210°C, EA = 18%
- Ė_yakıt = 4,700 kW (yakıtın kimyasal exergy'si, LHV × 1.04)

İdeal koşullar:
- Tüm kayıplar sıfır, yanma tersinir
- Ė_D,ideal = 0

Kaçınılamaz koşullar:
- η_th,UN = 94%, T_bg,UN = 140°C, EA_UN = 8%
- Yanma tersinmezliği: Ė_D,yanma,UN = 4,700 × 0.27 = 1,269 kW
- Baca gazı kaybı (UN): Q̇_bg,UN = 4,500 × (1-0.94) = 270 kW
  → Ė_bg,UN = 270 × (1 - T₀/T_bg,avg) ≈ 270 × 0.28 = 75.6 kW
- Isı transfer tersinmezliği (UN): ΔT_UN = 20°C
  → Ė_D,ht,UN ≈ Q̇_buhar × T₀ × ΔT_ht / (T_alev × T_buhar)
  ≈ 3,960 × 298 × 20 / (1,800 × 453) ≈ 28.9 kW
- Radyasyon (UN): 4,500 × 0.008 = 36 kW → Ė_D,rad,UN ≈ 12 kW
- Ė_D,UN,toplam = 1,269 + 75.6 + 28.9 + 12 ≈ 1,385.5 kW

Gerçek exergy yıkımı:
- Ė_D,toplam ≈ 2,100 kW (yanma + baca + ısı transfer + radyasyon + diğer)

Kaçınılabilir exergy yıkımı:
- Ė_D,AV = 2,100 - 1,385.5 = 714.5 kW
- IP = 714.5 / 2,100 × 100 = %34.0

Yorum: Kazan exergy yıkımının %66'sı kaçınılamaz (yanma tersinmezliği dominant).
Kaçınılabilir %34'lük kısım: baca gazı geri kazanımı, fazla hava azaltma,
yalıtım iyileştirme ile hedeflenebilir.
```

## 3. Isı Değiştirici İdeal ve Kaçınılamaz Koşulları (Heat Exchanger Ideal/Unavoidable Conditions)

### 3.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| Minimum yaklaşım ΔT (LMTD approach) | ΔT_min | 0 °C | 5-10 °C | Plate: 5°C, Shell&tube: 10°C |
| Basınç düşüşü (pressure drop) | ΔP | 0 bar | 0.01-0.05 bar | Tip ve boyuta bağlı |
| Kirlenme faktörü (fouling factor) | R_f | 0 | 0.0001-0.0002 m²K/W | Temiz çalışma koşulları |
| Isı kaybı (heat loss to ambient) | Q_loss | 0% | 0.5-1.0% | BAT yalıtım |
| Karışım (mixing/leakage) | — | 0% | 0-0.5% | Conta sızıntısı (gasketed plate) |

### 3.2 Alt Tip Bazlı Kaçınılamaz Koşullar

```
Plakalı ısı eşanjörü (Plate heat exchanger):
- ΔT_min,UN = 3-5 °C (yüksek ısı transfer katsayısı)
- ΔP_UN = 0.02-0.05 bar (kanal geometrisi)
- R_f,UN = 0.0001 m²K/W (düzgün yüzey, kolay temizlik)
- Etkililik (effectiveness): ε_UN = 0.90-0.95
- Sınırlama: Basınç <25 bar, sıcaklık <200°C (conta malzemesi)
- Referans: Tsatsaronis & Park (2002)

Borulu ısı eşanjörü (Shell & tube):
- ΔT_min,UN = 8-10 °C (sığdırma kısıtları, akış dağılımı)
- ΔP_UN = 0.01-0.03 bar (kabuk tarafı), 0.02-0.05 bar (boru tarafı)
- R_f,UN = 0.0001-0.0002 m²K/W
- Etkililik: ε_UN = 0.85-0.90
- Avantaj: Yüksek basınç ve sıcaklık dayanımı

Kanatlı borulu (Finned tube):
- ΔT_min,UN = 10-15 °C (hava tarafı direnci)
- ΔP_UN = 0.001-0.005 bar (hava tarafı)
- R_f,UN = 0.0002-0.0005 m²K/W (kanat arası toz birikimi)
- Etkililik: ε_UN = 0.70-0.85
- Not: Hava tarafı ısı transfer katsayısı düşük → daha büyük ΔT

Hava soğutmalı (Air-cooled):
- ΔT_min,UN = 15-25 °C (hava tarafı düşük h-değeri)
- ΔP_UN = 0.001-0.003 bar (hava, fan basıncı)
- Fan gücü_UN = toplam ısı transferinin %0.5-1.0'i
- Etkililik: ε_UN = 0.60-0.75
- Referans: Morosuk & Tsatsaronis (2009)
```

### 3.3 Sayısal Örnek — Plakalı Eşanjör

```
Senaryo: Kompresör atık ısısı → Kazan besleme suyu
- Sıcak taraf: 85°C → 65°C (kompresör soğutma suyu, 2 kg/s)
- Soğuk taraf: 15°C → 55°C (kazan besleme suyu, 1.2 kg/s)
- Q̇ = 2 × 4.18 × (85 - 65) = 167.2 kW

Gerçek koşullar:
- ΔT_min = 15°C (fouling dahil), ΔP = 0.08 bar
- R_f = 0.0004 m²K/W (kireç birikimi)

Kaçınılamaz koşullar:
- ΔT_min,UN = 5°C, ΔP_UN = 0.03 bar
- R_f,UN = 0.0001 m²K/W

Exergy yıkımı karşılaştırması:
Ė_D = Q̇ × T₀ × [(1/T_soğuk,avg) - (1/T_sıcak,avg)]

Gerçek: T_sıcak,avg = (85+65)/2 = 75°C = 348 K
        T_soğuk,avg = (15+55)/2 = 35°C = 308 K
        Ė_D = 167.2 × 298 × [(1/308) - (1/348)] = 167.2 × 298 × 0.000373
            = 18.6 kW

Kaçınılamaz (ΔT_min = 5°C → soğuk çıkış 60°C):
        T_soğuk,avg,UN = (15+60)/2 = 37.5°C = 310.5 K
        Ė_D,UN = 167.2 × 298 × [(1/310.5) - (1/348)] = 167.2 × 298 × 0.000347
               = 17.3 kW

Ė_D,AV = 18.6 - 17.3 = 1.3 kW
IP = 1.3 / 18.6 × 100 = %7.0

Yorum: Isı eşanjörlerinde kaçınılabilir kayıp oranı genellikle düşüktür.
Asıl fırsat, fouling kontrolü ve uygun tip seçimindedir.
```

## 4. Pompa İdeal ve Kaçınılamaz Koşulları (Pump Ideal/Unavoidable Conditions)

### 4.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| Hidrolik verim (hydraulic efficiency) | η_h | 1.00 | 0.85-0.90 | BAT santrifüj pompa, BEP'te |
| Mekanik verim (mechanical efficiency) | η_mech | 1.00 | 0.98-0.99 | Modern mekanik sızdırmazlık |
| Motor verimi (motor efficiency) | η_motor | 1.00 | 0.96-0.97 | IE4 sınıfı motor |
| Kısma vanası kaybı (throttle valve loss) | ΔP_vana | Yok | VSD kontrol | Vana ile kısma = tamamen kaçınılabilir kayıp |
| Sızdırmazlık kaybı (leakage) | L | 0% | 0.5-1.0% | Modern mekanik seal |
| Disk sürtünmesi (disk friction) | — | 0 | Pompa η_h içinde | Çark arka yüzey sürtünmesi |

### 4.2 Alt Tip Bazlı Kaçınılamaz Koşullar

```
Santrifüj pompa (Centrifugal pump):
- η_h,UN = 0.87-0.90 (BEP noktasında, >30 kW)
- η_h,UN = 0.80-0.85 (küçük pompalar, <10 kW)
- η_mech,UN = 0.98-0.99
- η_motor,UN = 0.96-0.97
- Toplam verim_UN = η_h × η_mech × η_motor = 0.82-0.86
- Kontrol: VSD (kaçınılamaz), vana kısma kaçınılabilir
- Referans: Tsatsaronis (2002), Kelly (2008)

Pozitif deplasmanlı pompa (Positive displacement):
- η_vol,UN = 0.95-0.98 (iç kaçak)
- η_mech,UN = 0.90-0.95 (daha yüksek mekanik kayıp)
- η_motor,UN = 0.96-0.97
- Toplam verim_UN = 0.82-0.90
- Avantaj: Değişken viskozite ve basınca daha az duyarlı

Dalgıç pompa (Submersible pump):
- η_h,UN = 0.80-0.85 (kompakt tasarım kısıtı)
- η_motor,UN = 0.90-0.93 (su soğutmalı, ancak kompakt)
- Kablo kaybı_UN = 1-3% (uzun kablo mesafesi)
- Toplam verim_UN = 0.70-0.78
- Not: Motor erişilemez → bakım maliyeti yüksek
```

### 4.3 Sayısal Örnek — Santrifüj Pompa

```
Gerçek çalışma koşulları:
- Pompa gücü: 15 kW, Debi: 30 m³/h, Basma yüksekliği: 35 m
- η_h = 0.72, η_mech = 0.96, η_motor = 0.93
- Kontrol: Kısma vanası ile debi ayarı (%70 yük)
- Gerçek güç: 15 × 0.70 = 10.5 kW (kısma ile hala yüksek)

Hidrolik güç:
Ẇ_hid = ρ × g × Q × H / 1000 = 1000 × 9.81 × (30/3600) × 35 / 1000
      = 2.86 kW (faydalı iş)

Gerçek exergy yıkımı:
Ė_D,toplam = 10.5 - 2.86 = 7.64 kW

Kaçınılamaz koşullar (VSD kontrol, BEP çalışma):
- η_h,UN = 0.88, η_mech,UN = 0.98, η_motor,UN = 0.96
- Ẇ_UN = 2.86 / (0.88 × 0.98 × 0.96) = 3.46 kW
  (VSD ile %70 debi → affinity law: güç ≈ 3.46 × 0.70³ ≈ 1.19 kW)
  NOT: Burada BEP'te tam debi çalışma varsayılmıştır.
  VSD kullanıldığında pompaj gücü dramatik düşer.
- Ė_D,UN = 3.46 - 2.86 = 0.60 kW

Kaçınılabilir exergy yıkımı:
Ė_D,AV = 7.64 - 0.60 = 7.04 kW
IP = 7.04 / 7.64 × 100 = %92.1

Yorum: Vana kısmalı pompada kaçınılabilir kayıp oranı çok yüksek.
VSD retrofit en yüksek IP sağlayan müdahaledir.
```

## 5. Chiller İdeal ve Kaçınılamaz Koşulları (Chiller Ideal/Unavoidable Conditions)

### 5.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| COP | COP | COP_Carnot | COP_Carnot × 0.60-0.70 | Carnot oranı (second-law efficiency) |
| Kompresör izentropik verim | η_is | 1.00 | 0.82-0.88 | BAT santrifüj chiller kompresörü |
| Kondenser yaklaşım ΔT (condenser approach) | ΔT_cond | 0 °C | 2-3 °C | Shell&tube kondenser minimum |
| Evaporatör yaklaşım ΔT (evaporator approach) | ΔT_evap | 0 °C | 2-3 °C | Shell&tube evaporatör minimum |
| Genleşme prosesi (expansion process) | — | İzentropik | İzentalpik (vana) | Genleşme vanası tersinmezliği kaçınılamaz |
| Alt soğuma (subcooling) | ΔT_sc | 0 °C | 3-5 °C | Sıvı hattı güvenliği |
| Kızgınlık (superheat) | ΔT_sh | 0 °C | 5-8 °C | Kompresör koruma |
| Soğutucu kaçağı (refrigerant leakage) | — | 0%/yıl | 1-3%/yıl | Modern hermetik sistem |

### 5.2 Alt Tip Bazlı Kaçınılamaz Koşullar

```
Santrifüj chiller (Centrifugal):
- η_is,UN = 0.85-0.88 (BAT tek kademeli)
- COP/COP_Carnot_UN = 0.65-0.70
- ΔT_cond,UN = 2°C, ΔT_evap,UN = 2°C
- Tipik COP_UN = 6.5-7.5 (7/35°C)
- IPLV/NPLV_UN > 10.0 (kısmi yükte BAT)
- Referans: Morosuk & Tsatsaronis (2009), Kelly et al. (2009)

Vidalı chiller (Screw):
- η_is,UN = 0.82-0.85
- COP/COP_Carnot_UN = 0.60-0.65
- ΔT_cond,UN = 3°C, ΔT_evap,UN = 3°C
- Tipik COP_UN = 5.5-6.5 (7/35°C)
- VSD avantajı: Kısmi yükte COP artışı %15-25

Scroll chiller (Scroll):
- η_is,UN = 0.78-0.82 (küçük kapasite kısıtı)
- COP/COP_Carnot_UN = 0.55-0.60
- ΔT_cond,UN = 3-4°C, ΔT_evap,UN = 3-4°C
- Tipik COP_UN = 4.5-5.5 (7/35°C)

Absorpsiyonlu chiller (Absorption):
- Tek etkili COP_UN = 0.75-0.80 (LiBr-H₂O)
- Çift etkili COP_UN = 1.20-1.30 (LiBr-H₂O)
- Jeneratör yaklaşım ΔT_UN = 5°C
- Absorber yaklaşım ΔT_UN = 5°C
- Kristalizasyon marjı_UN = 3-5°C (güvenlik)
- Referans: Petrakopoulou et al. (2012)
```

### 5.3 Sayısal Örnek — Santrifüj Chiller

```
Gerçek çalışma koşulları:
- Soğutma kapasitesi: 500 kW @ 7°C chilled water
- Kondenser: 35°C su soğutmalı
- COP = 4.5, Ẇ_komp = 500 / 4.5 = 111.1 kW
- η_is = 0.78, ΔT_cond = 5°C, ΔT_evap = 5°C

Carnot COP:
COP_Carnot = T_evap / (T_cond - T_evap)
           = (7-5+273) / [(35+5+273) - (7-5+273)]   [iç sıcaklıklar]
           = 275 / (313 - 275) = 275 / 38 = 7.24
η_II = COP / COP_Carnot = 4.5 / 7.24 = 0.621

Kaçınılamaz koşullar:
- ΔT_cond,UN = 2°C, ΔT_evap,UN = 2°C
- T_cond,UN = 35+2 = 37°C = 310 K
- T_evap,UN = 7-2 = 5°C = 278 K
- COP_Carnot,UN = 278 / (310 - 278) = 278/32 = 8.69
- COP_UN = 8.69 × 0.67 = 5.82 (η_II,UN = 0.67)
- Ẇ_komp,UN = 500 / 5.82 = 85.9 kW

Exergy analizi:
Ė_D,toplam = Ẇ_komp - Ė_soğutma
Ė_soğutma = Q̇_evap × (T₀/T_evap - 1) = 500 × (298/280 - 1) = 32.1 kW
Ė_D,toplam = 111.1 - 32.1 = 79.0 kW

Ė_D,UN = 85.9 - 32.1 = 53.8 kW
Ė_D,AV = 79.0 - 53.8 = 25.2 kW
IP = 25.2 / 79.0 × 100 = %31.9

Yorum: Chiller'da kaçınılabilir kayıp oranı %32.
Genleşme vanası tersinmezliği ve ΔT kayıpları önemli kaçınılamaz bileşenler.
```

## 6. Buhar/Gaz Türbini İdeal ve Kaçınılamaz Koşulları (Turbine Ideal/Unavoidable Conditions)

### 6.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| İzentropik verim — buhar (steam isentropic eff.) | η_is,st | 1.00 | 0.88-0.92 | BAT condensing türbin |
| İzentropik verim — gaz (gas isentropic eff.) | η_is,gt | 1.00 | 0.90-0.95 | BAT gaz türbini (modern F/H sınıfı) |
| Mekanik kayıplar (mechanical losses) | L_mech | 0% | 1-2% | Rulman ve sızdırmazlık |
| Jeneratör verimi (generator efficiency) | η_gen | 1.00 | 0.97-0.98 | Modern senkron jeneratör |
| Egzoz kaybı — buhar (exhaust loss) | L_exh | 0% | 3-5% | Son kademe nemli buhar kaybı |
| Egzoz sıcaklığı — gaz (exhaust temperature) | T_exh | T₀ | 450-550°C | Metalurjik limit (TIT bağımlı) |
| Soğutma kaybı — gaz (cooling loss) | L_cool | 0% | 2-4% | Kanat soğutma havası |

### 6.2 Alt Tip Bazlı Kaçınılamaz Koşullar

```
Karşı basınçlı buhar türbini (Back-pressure):
- η_is,UN = 0.80-0.85 (küçük/orta ölçek)
- η_is,UN = 0.85-0.88 (büyük ölçek, çok kademeli)
- η_mech,UN = 0.98-0.99
- η_gen,UN = 0.97-0.98
- Egzoz basıncı: Proses ihtiyacına göre (3-15 bar)
- Referans: Bejan et al. (1996)

Yoğuşmalı buhar türbini (Condensing):
- η_is,UN = 0.88-0.92 (modern, çok kademeli)
- η_mech,UN = 0.99
- η_gen,UN = 0.98
- Kondenser basıncı_UN = 0.04-0.06 bar (soğutma suyuna bağlı)
- Son kademe ıslaklık_UN < %12 (malzeme sınırı)
- Referans: Tsatsaronis (2002)

Ara buhar çekişli türbin (Extraction):
- η_is,UN = 0.85-0.90 (çekiş noktasına kadar)
- Çekiş miktarı kontrolü: Çekiş vanası kaybı kaçınılamaz
- Referans: Kelly et al. (2009)

Gaz türbini (Gas turbine):
- η_is,komp,UN = 0.90-0.92 (aksiyel kompresör)
- η_is,türbin,UN = 0.90-0.95 (sıcak gaz genleşme)
- TIT_UN (Türbin giriş sıcaklığı) = 1,300-1,600°C (malzeme limiti)
- Basınç oranı_UN = 20-35 (modern heavy-duty)
- Soğutma kaybı_UN = 2-4% (TBC kaplamalı kanatlar)
- Yanma tersinmezliği_UN = %25-30 (kazan ile aynı)
- Referans: Petrakopoulou et al. (2012), Morosuk & Tsatsaronis (2009)

ORC türbini (Organic Rankine Cycle):
- η_is,UN = 0.80-0.85 (organik akışkan genleşme)
- η_gen,UN = 0.95-0.97
- Çevrim verimi_UN = %12-18 (kaynak sıcaklığına bağlı)
- İç geri kazanım (recuperator)_UN: ΔT_min = 5°C
```

### 6.3 Sayısal Örnek — Gaz Türbini CHP

```
Gerçek çalışma koşulları:
- Gaz türbini: 5 MW_e, doğalgaz yakıtlı
- TIT = 1,200°C, basınç oranı = 16
- Elektrik verimi: η_e = 30%
- Egzoz sıcaklığı: 520°C
- Q̇_yakıt = 5,000 / 0.30 = 16,667 kW

Kaçınılamaz koşullar:
- η_is,komp,UN = 0.91, η_is,türbin,UN = 0.92
- η_gen,UN = 0.98, TIT = 1,200°C (mevcut makine limiti)
- Yanma Ė_D,UN = 16,667 × 1.04 × 0.27 = 4,680 kW
- Kompresör Ė_D,UN: ~350 kW (η_is farkı)
- Türbin Ė_D,UN: ~400 kW
- Egzoz Ė_D,UN: ~800 kW (T_exh düşürülemez, HRSG'ye gider)
- Ė_D,UN,toplam ≈ 6,230 kW

Gerçek Ė_D,toplam ≈ 8,500 kW (tüm bileşenler)

Ė_D,AV = 8,500 - 6,230 = 2,270 kW
IP = 2,270 / 8,500 × 100 = %26.7

Yorum: Gaz türbini exergy yıkımının %73'ü kaçınılamaz.
Yanma tersinmezliği en büyük kaçınılamaz bileşendir.
```

## 7. Kurutma Fırını İdeal ve Kaçınılamaz Koşulları (Dryer Ideal/Unavoidable Conditions)

### 7.1 Genel Parametre Tablosu

| Parametre | Sembol | İdeal | Kaçınılamaz | Açıklama |
|---|---|---|---|---|
| Egzoz sıcaklığı (exhaust temperature) | T_exh | T₀ + ΔT_wb | T_giriş × 0.40-0.50 | Kurutma kinetiği limiti |
| Egzoz nemi (exhaust humidity) | w_exh | Doygunluk | %70-85 bağıl nem | Ürün kalitesi limiti |
| Isı kaybı (shell/wall heat loss) | Q_wall | 0% | 3-5% | BAT yalıtım |
| Hava geri devir oranı (recirculation) | R | Optimum | %40-70 | Ürün kalitesi ve VOC limiti |
| Fan verimi (fan efficiency) | η_fan | 1.00 | 0.80-0.85 | BAT santrifüj fan |
| Spesifik enerji tüketimi (SEC) | SEC | h_fg (buharlaşma entalpisi) | 3,000-4,500 kJ/kg_su | Kurutucu tipine bağlı |

### 7.2 Sayısal Örnek — Konvektif Bant Kurutucu

```
Gerçek çalışma koşulları:
- Kurutma kapasitesi: 1,000 kg_su/h buharlaştırma
- Giriş havası: 150°C, Egzoz havası: 95°C
- SEC = 4,200 kJ/kg_su → Q̇_toplam = 1,167 kW
- Hava geri devir oranı: %30

Minimum enerji ihtiyacı (ideal):
SEC_ideal = h_fg = 2,257 kJ/kg (100°C'de buharlaşma gizli ısısı)
Q̇_ideal = 1,000 × 2,257 / 3,600 = 627 kW

Kaçınılamaz koşullar:
- SEC_UN = 3,200 kJ/kg (BAT bant kurutucu, %60 geri devir)
- Q̇_UN = 1,000 × 3,200 / 3,600 = 889 kW

Exergy karşılaştırması:
Ė_D,toplam = 1,167 - 627 = 540 kW (basitleştirilmiş)
Ė_D,UN = 889 - 627 = 262 kW
Ė_D,AV = 540 - 262 = 278 kW
IP = 278 / 540 × 100 = %51.5

Yorum: Kurutma fırınında %51 kaçınılabilir kayıp.
Egzoz ısı geri kazanımı ve hava geri devir oranı artışı öncelikli.
```

## 8. Kaynak Tablosu — Kaçınılamaz Değerler için Literatür Referansları (Source Table)

Aşağıdaki tabloda, her kaçınılamaz parametrenin hangi akademik kaynağa dayandığı belirtilmektedir.

| Ekipman | Parametre | Kaçınılamaz Değer | Kaynak |
|---|---|---|---|
| Kompresör | η_is,UN = 0.92-0.95 | Tsatsaronis & Park (2002) |
| Kompresör | η_mech,UN = 0.98-0.99 | Kelly et al. (2009) |
| Kompresör | η_motor,UN = 0.96-0.97 | IEC 60034-30 IE4 standardı |
| Kazan | Yanma tersinmezliği %25-30 | Bejan, Tsatsaronis & Moran (1996) |
| Kazan | T_bg,UN = 130-160°C | EU BAT Reference (2009) |
| Kazan | η_th,UN = 95-96% | Petrakopoulou et al. (2012) |
| Isı eşanjörü | ΔT_min,UN = 5-10°C | Tsatsaronis & Park (2002) |
| Isı eşanjörü | R_f,UN = 0.0001-0.0002 | TEMA standartları |
| Pompa | η_h,UN = 0.85-0.90 | Tsatsaronis (2002) |
| Pompa | VSD vs vana kısma | Kelly (2008) |
| Chiller | COP/COP_Carnot = 0.60-0.70 | Morosuk & Tsatsaronis (2009) |
| Chiller | η_is,UN = 0.82-0.88 | Kelly et al. (2009) |
| Chiller | ΔT_cond,UN = 2-3°C | ASHRAE 90.1 (2019) |
| Chiller (abs.) | COP_UN = 0.75-0.80 (tek etkili) | Petrakopoulou et al. (2012) |
| Türbin (buhar) | η_is,UN = 0.88-0.92 | Bejan et al. (1996) |
| Türbin (gaz) | η_is,UN = 0.90-0.95 | Morosuk & Tsatsaronis (2009) |
| Türbin (gaz) | TIT metalurjik limit | Petrakopoulou et al. (2012) |
| Türbin (ORC) | η_is,UN = 0.80-0.85 | Quoilin et al. (2013) |
| Kurutucu | SEC_UN = 3,000-4,500 kJ/kg | Kemp (2012), EU BAT |

## 9. Sınır Durumların Ele Alınması (Handling Borderline Cases)

### 9.1 Kaçınılamaz Değer Belirsizliği

```
Kaçınılamaz koşullar tanımlanırken belirsizlik kaynakları:

1. Teknoloji gelişimi:
   - Bugünün "kaçınılamaz" değeri, yarın teknoloji ile "kaçınılabilir" olabilir.
   - Örnek: 2000 yılında η_is,UN = 0.88 olan kompresör, 2025'te η_is,UN = 0.92.
   - Çözüm: Kaçınılamaz değerleri periyodik olarak güncelleyin (3-5 yılda bir).

2. Boyut bağımlılığı:
   - Küçük ekipmanlar daha düşük verimlerde çalışır.
   - Örnek: 5 kW pompa η_h,UN = 0.75, 100 kW pompa η_h,UN = 0.90.
   - Çözüm: Kapasite bazlı kaçınılamaz değer eğrileri kullanın.

3. Çalışma koşulları:
   - Aynı ekipman farklı koşullarda farklı kaçınılamaz sınırlara sahiptir.
   - Örnek: Chiller COP → T_evap ve T_cond'a güçlü bağımlı.
   - Çözüm: Koşulları normalleştirin veya referans koşullarını belirtin.
```

### 9.2 Eşik Değer Kuralları

```
ExergyLab platformunda sınır durum kuralları:

Kural 1 — Küçük kapasite düzeltmesi:
IF ekipman_kapasitesi < 10 kW:
  η_UN = η_UN,referans × 0.90  (verim %10 düşürülür)

Kural 2 — Eski ekipman toleransı:
IF ekipman_yaşı > 15 yıl:
  η_UN = η_UN,referans × 0.95  (retrofite uygun olmayabilir)
  NOT: Bu durumda ekipman yenileme de kaçınılabilir seçenek olarak önerilir.

Kural 3 — Çalışma koşulu düzeltmesi:
IF ekipman_yükü < %50 sürekli:
  η_UN = η_UN,BEP × f(yük_oranı)
  Kompresör: f = 0.85 @ %50 yük (VSD ile)
  Pompa: f = 0.80 @ %50 yük (VSD ile)
  Chiller: f = 0.90 @ %50 yük (VSD ile)

Kural 4 — Sıcak iklim düzeltmesi (chiller):
IF T_ortam > 35°C:
  ΔT_cond,UN = 3°C (standart 2°C yerine)
  COP_UN *= 0.90 (soğutma kulesi yaklaşımı artar)

Kural 5 — Kirli proses düzeltmesi (eşanjör):
IF proses_akışkan = "kirli" veya "viskoz":
  R_f,UN = 0.0003-0.0005 m²K/W (standart 0.0001 yerine)
  ΔT_min,UN += 3-5°C

Kural 6 — Güvenlik marjı:
Hesaplanan Ė_D,AV < 0.5 kW veya IP < %5 durumunda:
  → "Bu ekipman için iyileştirme potansiyeli ihmal edilebilir" raporu
  → Öncelik listesinden çıkar
```

### 9.3 Çoklu Ekipman Etkileşimi

```
İleri exergy analizinde endojen/eksojen (endogenous/exogenous) ayrımı:

Ė_D,k = Ė_D,k^EN + Ė_D,k^EX

Burada:
- Ė_D,k^EN = k-ıncı ekipmanın kendi iç tersinmezliğinden kaynaklanan yıkım
- Ė_D,k^EX = Diğer ekipmanların tersinmezliğinden k'ya yansıyan yıkım

Sınır durum: Bir ekipmanın Ė_D,AV değerinin büyük kısmı eksojen ise,
o ekipmana müdahale yerine kaynak ekipmana müdahale daha etkilidir.

Örnek:
Chiller evaporatör Ė_D,AV = 15 kW
  - Endojen: 5 kW (kendi ΔT'si)
  - Eksojen: 10 kW (kompresör düşük veriminden kaynaklanan yüksek kızgınlık)
→ Kompresör iyileştirmesi, evaporatör iyileştirmesinden 2× daha etkili.

ExergyLab bu etkileşimi cross_equipment.md ile birlikte değerlendirir.
```

### 9.4 Özet Karar Tablosu — Tüm Ekipmanlar

| Ekipman | Tipik IP [%] | Dominant Kaçınılamaz Kaynak | Öncelikli İyileştirme Alanı |
|---|---|---|---|
| Kompresör | 55-75 | İzentropik verim sınırı | VSD, bakım, doğru boyutlama |
| Kazan | 25-40 | Yanma tersinmezliği (%25-30) | Baca gazı WHR, fazla hava optimizasyonu |
| Isı eşanjörü | 5-15 | ΔT_min geometrik sınır | Fouling kontrolü, tip seçimi |
| Pompa | 70-95 | Hidrolik verim + kısma | VSD retrofit (en yüksek IP) |
| Chiller | 25-40 | Genleşme + ΔT kayıpları | Kompresör verimi, kondenser bakımı |
| Buhar türbini | 20-35 | İzentropik verim metal. sınır | Kademe sayısı, bakım, sızdırmazlık |
| Gaz türbini | 20-30 | Yanma tersinmezliği + TIT limit | Bakım, hava filtre temizliği |
| Kurutucu | 40-55 | Buharlaşma entalpisi + egzoz | Egzoz WHR, hava geri devir |

## İlgili Dosyalar

- [Ekipman Bazlı İleri Exergy](equipment_specific/) -- Ekipman detaylı ileri exergy analiz dosyaları
- [Ekipmanlar Arası Optimizasyon](../cross_equipment.md) -- Eksojen exergy yıkımı ve çapraz müdahale
- [Atık Isı Geri Kazanım](../waste_heat_recovery.md) -- WHR teknolojileri ve kaçınılabilir kayıp azaltma
- [Isı Entegrasyonu](../heat_integration.md) -- Pinch analizi ile kaçınılabilir ΔT kayıplarının azaltılması
- [Kompresör Benchmarkları](../../compressor/benchmarks.md) -- Kompresör BAT performans referansları
- [Kazan Benchmarkları](../../boiler/benchmarks.md) -- Kazan BAT performans referansları
- [Chiller Benchmarkları](../../chiller/benchmarks.md) -- Chiller BAT performans referansları
- [Pompa Benchmarkları](../../pump/benchmarks.md) -- Pompa BAT performans referansları
- [Kurutma Benchmarkları](../../dryer/benchmarks.md) -- Kurutucu BAT performans referansları
- [Buhar Türbini Benchmarkları](../../steam_turbine/benchmarks.md) -- Türbin BAT performans referansları
- [Isı Eşanjörü Benchmarkları](../../heat_exchanger/benchmarks.md) -- HX performans referansları
- [Exergy Temelleri](../exergy_fundamentals.md) -- Temel exergy kavramları ve formüller
- [Pinch Analizi](../pinch_analysis.md) -- Pinch analizi ile ΔT_min belirleme

## Referanslar

- Tsatsaronis, G. & Park, M.H., "On Avoidable and Unavoidable Exergy Destructions and Investment Costs in Thermal Systems," Energy Conversion and Management, Vol. 43, pp. 1259-1270, 2002
- Morosuk, T. & Tsatsaronis, G., "Advanced Exergy-Based Methods Used to Understand and Improve Energy-Conversion Systems," Energy, Vol. 169, pp. 238-246, 2009
- Bejan, A., Tsatsaronis, G. & Moran, M., "Thermal Design and Optimization," Wiley-Interscience, 1996
- Kelly, S., Tsatsaronis, G. & Morosuk, T., "Advanced Exergetic Analysis: Approaches for Splitting the Exergy Destruction into Endogenous and Exogenous Parts," Energy, Vol. 34, pp. 384-391, 2009
- Petrakopoulou, F., Tsatsaronis, G., Morosuk, T. & Carassai, A., "Conventional and Advanced Exergetic Analyses Applied to a Combined Cycle Power Plant," Energy, Vol. 41, pp. 146-152, 2012
- Kelly, S., "Energy Systems Improvement Based on Endogenous and Exogenous Exergy Destruction," PhD Thesis, Technische Universitaet Berlin, 2008
- Szargut, J., Morris, D.R. & Steward, F.R., "Exergy Analysis of Thermal, Chemical, and Metallurgical Processes," Hemisphere Publishing, 1988
- European Commission, "Reference Document on Best Available Techniques for Energy Efficiency," 2009
- ASHRAE, "ASHRAE Standard 90.1 — Energy Standard for Buildings Except Low-Rise Residential Buildings," 2019
- Quoilin, S. et al., "Techno-economic Survey of Organic Rankine Cycle (ORC) Systems," Renewable and Sustainable Energy Reviews, Vol. 22, pp. 168-186, 2013
- Kemp, I.C., "Pinch Analysis and Process Integration," Butterworth-Heinemann, 2nd Edition, 2007
- IEC 60034-30-1:2014, "Rotating Electrical Machines — Efficiency Classes of Line Operated AC Motors," International Electrotechnical Commission, 2014
