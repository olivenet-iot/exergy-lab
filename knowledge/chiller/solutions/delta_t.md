---
title: "Çözüm: Delta-T Optimizasyonu — Delta-T Optimization"
category: solutions
equipment_type: chiller
keywords: [delta-T, sıcaklık farkı, chiller, debi]
related_files: [chiller/solutions/chilled_water_reset.md, chiller/benchmarks.md, chiller/formulas.md]
use_when: ["Delta-T iyileştirme önerilirken", "Soğuk su debi optimizasyonu değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Delta-T Optimizasyonu — Delta-T Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Düşük delta-T sendromu, soğutma sistemlerinde yaygın bir sorundur. Tasarım delta-T değeri genellikle 5-7°C iken, gerçek çalışma koşullarında 3-4°C'ye düşer. Bu durum pompa enerji tüketimini artırır, chiller kapasitesini düşürür ve erken chiller devreye girişine (premature staging) neden olur.

**Çözüm:** Düşük delta-T nedenlerini teşhis ederek ortadan kaldırmak: 3 yollu vanalardan 2 yollu vanaya geçiş, serpantin temizliği, kontrol optimizasyonu ve değişken debili sisteme dönüşüm.

**Tipik Tasarruf:** %5-20 (pompa enerjisi + chiller verimliliği)
**Tipik ROI:** 0.5-3 yıl

## Çalışma Prensibi

### Delta-T Nedir?

Delta-T (ΔT), soğutma sisteminde soğutulmuş su gidiş (supply) ve dönüş (return) sıcaklıkları arasındaki farktır:

```
ΔT = T_dönüş - T_gidiş [°C]

Burada:
  T_dönüş  = Dönüş suyu sıcaklığı [°C]
  T_gidiş  = Gidiş suyu sıcaklığı [°C]
```

Soğutma kapasitesi, debi ve delta-T ile doğrudan ilişkilidir:

```
Q = ṁ × Cp × ΔT = V̇ × ρ × Cp × ΔT

Burada:
  Q    = Soğutma kapasitesi [kW]
  ṁ    = Kütle debisi [kg/s]
  V̇    = Hacimsel debi [m³/s]
  ρ    = Suyun yoğunluğu ≈ 1000 [kg/m³]
  Cp   = Suyun özgül ısısı ≈ 4.186 [kJ/kg·°C]
  ΔT   = Sıcaklık farkı [°C]
```

### Düşük Delta-T'nin Etkileri

| Etki | Açıklama | Maliyet Etkisi |
|------|----------|---------------|
| Artan pompa enerjisi | Aynı soğutma kapasitesi için daha fazla su debisi gerekir | Pompa gücü ∝ debi³ (fan yasaları) |
| Azalan chiller kapasitesi | Yüksek dönüş suyu debisi evaporatör performansını düşürür | Kapasite %10-30 azalma |
| Erken chiller staging | İkinci/üçüncü chiller gereksiz yere devreye girer | Ek chiller enerji tüketimi |
| Düşük evaporatör verimliliği | Düşük delta-T, düşük LMTD demektir | COP düşüşü %5-15 |
| Artan toplam enerji | Pompa + chiller toplam enerji artışı | %10-30 fazla enerji |

### Sayısal Örnek: Delta-T Etkisi

Aynı 500 kW soğutma kapasitesi için:

| Parametre | Tasarım (ΔT=6°C) | Düşük ΔT (ΔT=3°C) | Fark |
|-----------|-------------------|---------------------|------|
| Su debisi | 19.9 L/s | 39.8 L/s | 2× artış |
| Pompa gücü (teorik) | 10 kW | ~80 kW | 8× artış |
| Chiller kullanılabilir kapasitesi | 500 kW | 350-400 kW | %20-30 kayıp |
| Ek chiller gereksinimi | Hayır | Muhtemelen evet | Ek enerji maliyeti |

**Not:** Pompa gücü artışı küp yasasına göre hesaplanmıştır (debi 2× artınca güç 2³=8× artar); gerçekte sistem eğrisi nedeniyle artış daha düşük olabilir (3-5×).

## Düşük Delta-T Nedenleri

### 1. Üç Yollu Vana By-pass Akışı

En yaygın neden: 3 yollu kontrol vanaları kısmi yükte soğuk su ile sıcak dönüş suyunu karıştırarak delta-T'yi düşürür.

- **Mekanizma:** Serpantin yükü düştüğünde 3 yollu vana by-pass portunu açar; soğuk gidiş suyu doğrudan dönüş hattına karışır
- **Sonuç:** Dönüş suyu sıcaklığı tasarım değerinin altına düşer, delta-T azalır
- **Çözüm:** 3 yollu vanaları 2 yollu vanalarla değiştir, değişken debili sisteme geç

### 2. Aşırı Boyutlandırılmış Serpantinler

- **Mekanizma:** Tasarım aşamasında güvenlik payı ile aşırı büyük seçilen serpantinler, kısmi yükte su sıcaklığını çok fazla düşüremez
- **Sonuç:** Serpantin çıkış suyu sıcaklığı yeterince yükselmez
- **Çözüm:** Kontrol optimizasyonu, gidiş suyu sıcaklığını yükseltme (reset schedule)

### 3. Kirli Serpantinler

- **Mekanizma:** Hava tarafı kirlenme (toz, tüy birikimi) ısı transfer performansını düşürür
- **Sonuç:** Serpantin tam kapasiteye ulaşamaz, su tarafı delta-T düşer
- **Çözüm:** Düzenli serpantin temizliği, filtre bakımı

### 4. Uygunsuz Kontrol Stratejisi

- **Mekanizma:** Yanlış vana karakteristiği (lineer yerine eşit yüzde), yetersiz PI/PID ayarı, sensör kalibrasyonsuzluğu
- **Sonuç:** Kontrol döngüsü kararsız çalışır, vana aşırı açık kalır
- **Çözüm:** Kontrol parametreleri optimizasyonu, sensör kalibrasyonu, doğru vana karakteristiği seçimi

### 5. Değişken Hava Debili (VAV) Sistem Etkileşimi

- **Mekanizma:** VAV sistemi hava debisini kısınca serpantin kapasitesi düşer, su tarafı delta-T azalır
- **Sonuç:** Düşük hava debisinde serpantin tam ısı transferi yapamaz
- **Çözüm:** VAV minimum hava debisi ayarı, serpantin kontrolü ile koordinasyon

## Teşhis Yöntemleri

### 1. Delta-T Trend Analizi

BMS (Bina Yönetim Sistemi) üzerinden gidiş ve dönüş suyu sıcaklıklarını trendleyerek:

- **Sağlıklı sistem:** ΔT ≈ tasarım değeri (5-7°C) kısmi yükte bile
- **Düşük delta-T sendromu:** ΔT kısmi yükte <3°C'ye düşer
- **Ölçüm noktaları:** Chiller evaporatör giriş/çıkış, bina gidiş/dönüş header, her AHU giriş/çıkış

### 2. Serpantin Bazlı Analiz

Her AHU veya fancoil serpantini için ayrı ayrı delta-T ölçümü yaparak sorunlu birimleri tespit etme:

- Portatif ultrasonik debi ölçer + sıcaklık sensörleri ile geçici ölçüm
- Düşük delta-T'ye sahip serpantinlerin listesi ve neden analizi

### 3. Vana Pozisyonu Analizi

BMS üzerinden vana açıklık oranlarını izleyerek:

- Kısmi yükte bile %80-100 açık vanalar → muhtemel aşırı boyutlandırma veya tıkanma
- Hızlı salınım yapan vanalar → kontrol kararsızlığı

## Çözüm Stratejileri

### 1. Üç Yollu Vanadan İki Yollu Vanaya Geçiş

| Parametre | 3 Yollu Vana Sistemi | 2 Yollu Vana Sistemi |
|-----------|---------------------|---------------------|
| Debi karakteristiği | Sabit (by-pass ile) | Değişken (vana kısılması ile) |
| Delta-T korunumu | Düşük (by-pass karışımı) | Yüksek (debi azalır, ΔT korunur) |
| Pompa enerji tasarrufu | Yok | %30-60 (VSD ile) |
| Dönüşüm maliyeti | — | Vana + VSD + basınç kontrolü |

### 2. Değişken Debili Sisteme Dönüşüm

- Primer pompalara VSD ekleme veya primer-sekonder sisteme geçiş
- Diferansiyel basınç sensörü ile pompa hız kontrolü
- Minimum debi koruması (chiller minimum debi gereksinimi)

### 3. Gidiş Suyu Sıcaklığı Reset (Sıfırlama)

Dış hava sıcaklığına göre chiller gidiş suyu sıcaklığını yükseltme:

```
T_gidiş = T_min + (T_dış_ref - T_dış) × K_reset

Burada:
  T_gidiş    = Chiller gidiş suyu sıcaklık setpoint'i [°C]
  T_min      = Minimum gidiş suyu sıcaklığı (tasarım: tipik 6-7°C) [°C]
  T_dış      = Anlık dış hava sıcaklığı [°C]
  T_dış_ref  = Referans dış hava sıcaklığı (tasarım değeri) [°C]
  K_reset    = Reset katsayısı (tipik 0.3-0.5) [°C/°C]
```

- **Fayda:** Daha yüksek gidiş suyu sıcaklığı = daha yüksek evaporatör basıncı = daha yüksek COP
- **Her 1°C gidiş suyu sıcaklık artışı ≈ %2-3 COP artışı**

### 4. Serpantin Temizliği ve Bakımı

- Hava tarafı serpantin temizliği (basınçlı su, kimyasal temizlik)
- Hava filtreleri düzenli değişimi
- Su tarafı temizlik (gerekirse)
- Temizlik sonrası delta-T iyileşmesini doğrulama

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı

- Sistem delta-T değeri tasarımın %60'ının altına düşmüşse (ör. tasarım 6°C, gerçek <3.6°C)
- Pompalar sürekli tam hızda çalışıyorsa ve VSD yoksa
- Chiller'lar erken staging yapıyorsa (ikinci chiller düşük yükte devreye giriyorsa)
- 3 yollu kontrol vanaları kullanılıyorsa
- Serpantin bakımı düzenli yapılmıyorsa
- BMS trend verilerinde düşük delta-T gözleniyorsa

### Ne Zaman Uygulanmamalı

- Sistem zaten değişken debili çalışıyorsa ve delta-T tasarım değerindeyse
- Chiller minimum debi gereksinimleri karşılanamıyorsa (çok küçük sistem)
- Sistem yakın zamanda tamamen yenilenecekse

## Yatırım Maliyeti

| Uygulama | Maliyet (€) | Açıklama |
|----------|-------------|----------|
| 3 yollu → 2 yollu vana değişimi (AHU başına) | 500-3,000 | Vana boyutu ve erişilebilirliğe göre |
| Tüm AHU'larda vana dönüşümü (10-30 AHU) | 5,000-30,000 | Toplu uygulama |
| Pompa VSD ekleme (per pompa) | 3,000-15,000 | Motor gücüne göre (7.5-75 kW) |
| Diferansiyel basınç sensörü + BMS entegrasyonu | 1,500-5,000 | Sensör + programlama |
| Kontrol optimizasyonu (BMS programlama) | 3,000-15,000 | Mühendislik + programlama işçiliği |
| Serpantin temizliği (tüm AHU'lar) | 2,000-8,000 | Yıllık bakım kapsamında |
| Gidiş suyu reset stratejisi uygulaması | 2,000-5,000 | BMS programlama |

## ROI Hesabı

### Formül

```
Pompa_tasarrufu_kW = P_pompa_mevcut × (1 - (ΔT_tasarım/ΔT_mevcut)³)
Chiller_tasarrufu_kW = Q_soğutma × (1/COP_mevcut - 1/COP_iyileştirilmiş)
Toplam_tasarruf_kW = Pompa_tasarrufu_kW + Chiller_tasarrufu_kW
Yıllık_tasarruf_EUR = Toplam_tasarruf_kW × Çalışma_saati × Elektrik_fiyatı
Geri_ödeme_yıl = Toplam_yatırım / Yıllık_tasarruf_EUR
```

Burada:
- `P_pompa_mevcut`: Mevcut pompa elektrik tüketimi [kW]
- `ΔT_tasarım`: Tasarım delta-T değeri [°C]
- `ΔT_mevcut`: Mevcut ortalama delta-T değeri [°C]
- `Q_soğutma`: Soğutma kapasitesi [kW]
- `COP_mevcut`: Mevcut chiller COP [-]
- `COP_iyileştirilmiş`: Delta-T düzeltme sonrası COP [-]
- `Çalışma_saati`: Yıllık soğutma sezonu çalışma saati [saat/yıl]
- `Elektrik_fiyatı`: Birim elektrik fiyatı [€/kWh]

### Örnek Hesap

- 800 kW soğutma kapasiteli sistem
- Tasarım ΔT: 6°C, Mevcut ΔT: 3°C
- Mevcut pompa gücü: 30 kW, Chiller COP: 5.0
- İyileştirme sonrası COP: 5.5 (daha iyi evaporatör performansı)
- Yıllık çalışma: 3,500 saat
- Elektrik fiyatı: €0.12/kWh

```
Pompa_tasarrufu = 30 × (1 - (6/3)³) = burada ΔT düzeltildiğinde debi azalır
  → Debi oranı = ΔT_mevcut/ΔT_tasarım = 3/6 = 0.5 (mevcut debi tasarımın 2 katı)
  → İyileştirme sonrası debi = tasarım değerine döner
  → Pompa_tasarrufu = 30 × (1 - (1/2)³) = 30 × (1 - 0.125) = 30 × 0.875 = 26.25 kW
  → Ancak mevcut VSD yoksa pompa tam hızda çalışıyor, VSD ile tasarruf:
  → Pompa_tasarrufu = 30 × (1 - 0.5³) = 30 × 0.875 = 26.3 kW

Chiller_tasarrufu = 800 × (1/5.0 - 1/5.5) = 800 × (0.200 - 0.182) = 800 × 0.018 = 14.5 kW

Toplam_tasarruf = 26.3 + 14.5 = 40.8 kW
Yıllık_tasarruf = 40.8 × 3,500 × 0.12 = €17,136/yıl
```

- Yatırım: Vana dönüşümü €15,000 + Pompa VSD €10,000 + Kontrol €5,000 = **€30,000**
- **Geri ödeme: 30,000 / 17,136 = 1.75 yıl**

## Uygulama Adımları

1. **Mevcut delta-T ölçümü:** BMS veya portatif cihazlarla chiller, header ve AHU bazında delta-T ölçümü yap
2. **Neden analizi:** Düşük delta-T nedenlerini belirle (vana tipi, serpantin durumu, kontrol)
3. **Serpantin bazlı teşhis:** Her AHU/fancoil için ayrı delta-T ve vana pozisyonu analizi yap
4. **Serpantin temizliği:** Kirli serpantinleri hava ve su tarafından temizle
5. **Vana dönüşümü planlaması:** 3 yollu vanaları 2 yollu ile değiştirilecek birimleri listele, boyutlandırma yap
6. **VSD kurulumu:** Pompalara VSD ekle, diferansiyel basınç kontrolü kur
7. **Kontrol optimizasyonu:** Vana karakteristiklerini doğrula, PID parametrelerini ayarla
8. **Gidiş suyu reset:** Dış hava sıcaklığına göre gidiş suyu sıcaklık reset stratejisi uygula
9. **Minimum debi koruması:** Chiller minimum debi gereksinimini karşılayacak by-pass veya debi kontrolü sağla
10. **Performans doğrulama:** Uygulama sonrası delta-T trendini izle, tasarruf hesabını doğrula
11. **Sürekli izleme:** BMS üzerinde delta-T alarm ve trend izleme ekranları oluştur

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Düşük debi problemi | Değişken debili sistemde aşırı düşük debi serpantin performansını bozar | Minimum debi setpoint'i, baypas hattı |
| Serpantin donma riski | Düşük debide serpantin su tarafı donabilir (soğuk iklimlerde) | Antifriz veya minimum debi koruması, don koruma sensörü |
| Chiller minimum debi | Chiller evaporatörü minimum debi gerektirir (tipik %30-50 tasarım debisi) | Debi ölçer ve interlock, baypas hattı |
| Kontrol kararsızlığı | Vana değişimi sonrası PID ayarları uyumsuz kalabilir | Kontrol parametreleri optimizasyonu, adım yanıtı testi |
| Hidrolik dengesizlik | Vana değişimi sistem hidrolik dengesini bozabilir | Dengeleme vanaları kontrolü, komisyonlama |
| Hava kilidi (air lock) | Değişken debide hava birikimi riski artar | Otomatik hava tahliye vanaları, yüksek nokta venting |
| Mevcut vana uyumsuzluğu | 2 yollu vana mevcut boru hatları ile uyumsuz olabilir | Vana Cv hesabı, basınç düşüşü analizi |

## İlgili Dosyalar

- Chiller ekipman bilgisi: `equipment/chiller_centrifugal.md`
- Chiller benchmark verileri: `benchmarks/chiller_benchmarks.md`
- Chiller bakım: `solutions/chiller_maintenance.md`
- Pompa VSD uygulaması: `solutions/pump_vsd.md`
- Soğutma yükü azaltma: `solutions/chiller_load_reduction.md`
- Termal depolama: `solutions/chiller_thermal_storage.md`

## Referanslar

- ASHRAE Handbook — HVAC Systems and Equipment, Chapter 13: "Hydronic Heating and Cooling"
- ASHRAE Journal, "Solving the Low Delta-T Syndrome" — Taylor, S.T. (2002)
- ASHRAE Guideline 22, "Instrumentation for Monitoring Central Chilled-Water Plant Efficiency"
- Trane, "Chilled Water System Analysis — Low Delta-T Syndrome" — Engineers Newsletter
- Carrier Corporation, "System Design Manual — Chilled Water Systems"
- CIBSE Guide B, "Heating, Ventilating, Air Conditioning and Refrigeration" — Chilled Water Design
- DOE/FEMP, "Best Practices Guide for Energy-Efficient Chilled Water Plant Operations"
- Taylor, S.T., "Degrading Chilled Water Plant Delta-T: Causes and Mitigation," ASHRAE Transactions
- Avery, G., "Controlling Chillers in Variable Flow Systems," ASHRAE Journal
