# Çözüm: Kontrol Optimizasyonu — Control Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Uygun olmayan kontrol stratejisi pompa sistemlerinde ciddi enerji israfına neden olur. Sabit basınç setpoint'i, gereksiz yüksek basınç, gereğinden fazla pompa çalışması ve yetersiz otomasyon tipik sorunlardır. Endüstriyel tesislerde pompa kontrol optimizasyonu ile %10-30 enerji tasarrufu potansiyeli mevcuttur.

**Çözüm:** Sistem ihtiyacına uygun kontrol yöntemi seçimi, basınç setpoint optimizasyonu, talep bazlı kontrol ve BMS (Building Management System) entegrasyonu ile pompa enerji tüketimini minimize etmek.

**Tipik Tasarruf:** %10-30
**Tipik ROI:** 0.5-2 yıl

## Kontrol Yöntemleri Karşılaştırması

| Kontrol Yöntemi | Enerji Verimliliği | Karmaşıklık | Maliyet | En Uygun Uygulama |
|-----------------|-------------------|-------------|---------|-------------------|
| On-off (aç-kapa) | Düşük-Orta | Çok basit | Çok düşük | Depo dolum, küçük sistemler |
| Throttle (kısma) | Düşük | Basit | Düşük | Sabit debi, küçük sistemler (önerilmez) |
| Bypass (recirculation) | Çok düşük | Basit | Düşük | Acil koruma hattı (sürekli kullanılmamalı) |
| VSD (değişken hız) | Çok yüksek | Orta | Orta-Yüksek | Değişken debi, büyük sistemler |
| Cascade (kademeli) | Yüksek | Orta-Yüksek | Orta | Çok pompalı paralel sistemler |
| Demand-based (talep bazlı) | Çok yüksek | Yüksek | Orta-Yüksek | Bina HVAC, su dağıtım |
| Adaptive (uyarlanır) | En yüksek | Çok yüksek | Yüksek | Akıllı bina, büyük şebeke |

## Kontrol Yöntemleri Detayları

### 1. On-Off Kontrol

```
Çalışma mantığı:
  Seviye < Alt_limit → Pompa AÇ
  Seviye > Üst_limit → Pompa KAPAT
```

| Avantaj | Dezavantaj |
|---------|-----------|
| Basit, ucuz | Basınç dalgalanması |
| Güvenilir | Su çekiç riski (water hammer) |
| Bakım kolay | Motorun sık açılıp kapanması (termal stres) |
| | Konfor düşüklüğü |

**Enerji iyileştirme:** Minimum çalışma süreleri ve akıllı zamanlayıcı ile gereksiz döngüleri azalt.

### 2. VSD (Değişken Hız) Kontrol

Affinity Laws sayesinde en verimli kontrol yöntemidir:

```
P ∝ N³ (güç, hızın küpü ile orantılı)
%80 hız → %51 güç
%60 hız → %22 güç
%50 hız → %12.5 güç
```

**VSD kontrol modları:**

| Mod | Kontrol Değişkeni | Uygulanabilirlik |
|-----|-------------------|-----------------|
| Sabit basınç | Çıkış basıncı = setpoint | Basit, yaygın |
| Oransal basınç | Basınç setpoint ∝ debi | HVAC, enerji tasarrufu |
| Sabit sıcaklık farkı | ΔT = setpoint | Soğutma/ısıtma devreleri |
| Sabit debi | Q = setpoint | Proses uygulamaları |
| Minimum vana açıklığı | En uzak vana ~%90 açık | En verimli BMS modu |

### 3. Cascade (Kademeli) Kontrol

Çok pompalı paralel sistemlerde pompaların sıralı devreye alınması:

```
Senaryo: 3 × 50 kW pompa (toplam 150 kW kapasite)
Talep %30: 1 pompa VSD ile %90 hız → ~36 kW
Talep %50: 1 pompa %100 + 1 pompa VSD %50 → ~56 kW
Talep %80: 2 pompa %100 + 1 pompa VSD %70 → ~117 kW
Talep %100: 3 pompa %100 → 150 kW
```

**Sıralama kuralları:**
- Pompaları eşit çalışma saatine getirmek için sıralama rotasyonu uygula
- VSD pompayı her zaman "trim" (düzenleme) pompası olarak kullan
- Pompa ekleme/çıkarma eşiklerinde histerezis (hysteresis) uygula
- Geçiş sırasında basınç dalgalanmasını minimize et

### 4. Demand-Based (Talep Bazlı) Kontrol

Gerçek sistem ihtiyacına göre dinamik kontrol:

```
Geleneksel:  Setpoint = sabit (en kötü durum için tasarlanmış)
Talep bazlı: Setpoint = f(gerçek talep, sensör verileri)
```

## Basınç Setpoint Optimizasyonu

### Setpoint'in Enerji Etkisi

Her 1 bar gereksiz basınç artışının enerji etkisi:

```
ΔP_enerji = Q × ΔP / (36 × η_pompa × η_motor)  [kW]

Örnek: 50 m³/h, η_pompa = 0.72, η_motor = 0.93
ΔP_enerji = 50 × 1 / (36 × 0.72 × 0.93) = 2.07 kW / bar
```

| Sistem Head | 1 bar Fazla Basınç = | Yıllık Enerji İsrafı (6,000 saat) |
|-------------|---------------------|-----------------------------------|
| 30 m (3 bar) | +%33 enerji artışı | 12,420 kWh |
| 50 m (5 bar) | +%20 enerji artışı | 12,420 kWh |
| 80 m (8 bar) | +%12.5 enerji artışı | 12,420 kWh |
| 100 m (10 bar) | +%10 enerji artışı | 12,420 kWh |

**Not:** Mutlak enerji israfı (kWh) aynıdır; yüzdesel etki düşük basınçlı sistemlerde daha belirgindir.

### Diferansiyel Basınç Reset (DP Reset)

ASHRAE 90.1 standardına göre değişken debili sistemlerde DDC/BMS ile DP setpoint'i resetlenmeli:

```
Geleneksel: DP_setpoint = sabit (tasarım değeri)
Reset:      DP_setpoint = MIN(DP_ihtiyaç) → tüm vanalar gözetlenir
Kural:      En uzak vana ≥ %90 açık olana kadar DP_setpoint düşür
```

**Gerçek dünya sonuçları:**
- DP setpoint'i 5 PSI → 2 PSI'a düşürüldüğünde pompa gücü 0.70 kW → 0.30 kW (%57 azalma)
- DP setpoint'i 8 PSI → 4 PSI'a düzeltildiğinde pompa gücü 4.5 kW → 0.80 kW (%82 azalma)
- Yıllık tasarruf: 22,000 kWh ($2,600/yıl) — tek bir pompa grubu için

## Hidrofor (Paket Pompa) Sistemleri İçin Özel Öneriler

### Enerji Tasarruf Modları

| Mod | Koşul | Ayar | Tasarruf |
|-----|-------|------|---------|
| Gece modu | 22:00-06:00 | Basınç setpoint -%10-20 | %15-25 |
| Uyku modu (sleep) | Sıfır talep (debi=0) | Tüm pompalar durdur, basınç tankı ile karşıla | %100 (uyku sırasında) |
| Pikdışı modu | Düşük talep dönemleri | Minimum pompa sayısı, düşük setpoint | %20-40 |
| Yangın modu | Yangın alarmı | Tam kapasite, yüksek basınç | %0 (güvenlik) |

### Pompa Sıralama (Sequencing) Optimizasyonu

```
Optimum çalışma prensibi:
1. Toplam talebi en az pompa ile karşıla
2. Çalışan pompaları BEP yakınında tut
3. VSD pompayı trim (düzenleme) için kullan
4. Eşit çalışma saati için rotasyon uygula

Pompa ekleme kriteri:  VSD hızı > %95 ve talep artıyor
Pompa çıkarma kriteri: VSD hızı < %40 ve talep azalıyor
Histerezis:            ±%5 bant ile hunting (sürekli açma/kapama) önle
```

### Üretici Akıllı Kontrol Çözümleri

| Marka | Çözüm | Özellik |
|-------|-------|---------|
| Grundfos | CUE/Control MPC | 26 zone DP izleme, autotune, BACnet/Modbus |
| Grundfos | DDD (Demand Driven Distribution) | Hidrolik model, sürekli optimizasyon |
| Wilo | Wilo-Smart Control | Enerji modu, paralel pompa yönetimi |
| KSB | PumpDrive 2 / PumpManager | Uzaktan izleme, prediktif bakım |
| Xylem | Flygt Concertor | Gömülü akıllı kontrol, enerji optimizasyonu |

## BMS (Building Management System) Entegrasyonu

### Entegrasyon Seviyeleri

| Seviye | Açıklama | Tasarruf Potansiyeli | Maliyet |
|--------|----------|---------------------|---------|
| 1 — İzleme | Pompa durumu BMS'te görüntülenir | %0 (sadece bilgi) | €1,000-5,000 |
| 2 — Temel kontrol | BMS pompa aç/kapa komutu verir | %5-10 | €3,000-10,000 |
| 3 — Setpoint kontrol | BMS basınç setpoint'ini ayarlar | %10-20 | €5,000-15,000 |
| 4 — Adaptif kontrol | BMS vana konumlarına göre setpoint reset | %15-30 | €10,000-30,000 |
| 5 — Tam optimizasyon | BMS + AI ile tüm sistem optimizasyonu | %20-40 | €20,000-50,000 |

### İletişim Protokolleri

| Protokol | Kullanım Alanı | Özellik |
|----------|---------------|---------|
| BACnet IP | Bina otomasyonu (HVAC) | ASHRAE standardı, yaygın |
| Modbus TCP/RTU | Endüstriyel otomasyon | Basit, güvenilir |
| PROFINET | PLC entegrasyonu | Yüksek hız, deterministik |
| OPC UA | Üst seviye entegrasyon | Güvenli, platform bağımsız |
| MQTT | IoT / bulut | Hafif, uzaktan izleme |

## SCADA/PLC Kontrol Optimizasyonu

### Optimizasyon Parametreleri

| Parametre | Varsayılan (Tipik) | Optimize Edilmiş | Tasarruf |
|-----------|-------------------|-----------------|---------|
| Basınç setpoint | Sabit (tasarım değeri) | Dinamik (talebe göre) | %10-20 |
| Pompa değiştirme eşiği | Sabit | Adaptif (yük bazlı) | %3-8 |
| PID ayarları | Fabrika ayarı | Sistem tepkisine optimize | %2-5 |
| Rampa süreleri | Standart | Optimum (hızlı ama güvenli) | %1-3 |
| Uyku modu | Yok | Sıfır talep tespiti + uyku | %5-15 |
| Zaman programı | 7/24 aynı | Gündüz/gece/hafta sonu | %5-15 |

## Uygulanabilirlik Kriterleri

### Kontrol Optimizasyonu Ne Zaman Uygulanmalı
- Basınç setpoint'i hiç değiştirilmemiş (orijinal tasarım değerinde)
- Pompalar gece/gündüz aynı ayarlarda çalışıyor
- Birden fazla pompa aynı anda kısmi yükte çalışıyor
- BMS mevcut ama pompa entegrasyonu yapılmamış
- Kontrol valfleri sürekli kısık konumda (>%50 kısılmış)

### Kontrol Optimizasyonu Ne Zaman Uygulanmamalı
- Tek pompalı, sabit debili, küçük sistem (<2 kW)
- Sürekli tam yükte çalışan proses pompası
- Optimizasyon için gerekli sensörler ekonomik değilse

## Yatırım Maliyeti

| Çözüm | Maliyet Aralığı | Tipik Bileşenler |
|-------|-----------------|-----------------|
| Setpoint optimizasyonu (mevcut sistem) | €0-2,000 | Mühendislik + PLC programlama |
| Basınç sensörü ekleme | €500-2,000/adet | Transmitter + montaj |
| Debi sensörü ekleme | €1,000-5,000/adet | Elektromanyetik debimetre + montaj |
| PLC/SCADA yazılım güncelleme | €2,000-10,000 | Programlama + devreye alma |
| BMS entegrasyonu (Seviye 3-4) | €5,000-20,000 | Gateway + programlama + sensörler |
| Akıllı pompa kontrolörü | €3,000-15,000 | Grundfos CUE/Control MPC vb. |
| Tam otomasyon yenileme | €15,000-50,000 | PLC + VSD + sensörler + yazılım |

## ROI Hesabı

### Formül
```
Tasarruf_kWh = P_mevcut_ortalama × t × Tasarruf_yüzdesi
Tasarruf_EUR = Tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Toplam_yatırım / Tasarruf_EUR
```

### Örnek Hesap — Basınç Setpoint Optimizasyonu + BMS Entegrasyonu
- Hidrofor sistemi: 3 × 15 kW pompa
- Mevcut ortalama tüketim: 22 kW (7/24 sabit setpoint)
- 8,000 saat/yıl çalışma
- Elektrik: €0.15/kWh

```
Optimizasyon sonrası (gece modu + DP reset + sıralama):
  Beklenen tasarruf: %25
  Yeni ortalama tüketim: 22 × 0.75 = 16.5 kW

Tasarruf_kWh = (22 - 16.5) × 8,000 = 44,000 kWh/yıl
Tasarruf_EUR = 44,000 × 0.15 = €6,600/yıl

Yatırım:
  BMS entegrasyonu: €8,000
  Ek sensörler (2 adet basınç): €2,000
  PLC programlama: €3,000
  Toplam: €13,000

Geri_ödeme = 13,000 / 6,600 = 2.0 yıl
```

## Uygulama Adımları

1. **Sistem audit:** Mevcut kontrol stratejisini, basınç setpoint'lerini ve çalışma paternlerini belgele
2. **Veri toplama:** En az 2 haftalık debi, basınç ve güç profili oluştur
3. **Analiz:** Gereksiz basınç, kötü sıralama, eksik modlar tespit et
4. **Optimizasyon planı:** Yazılım değişiklikleri, sensör eklemeleri, BMS entegrasyon kapsamını belirle
5. **PLC/BMS programlama:** Yeni kontrol algoritmalarını tasarla ve uygula
6. **Devreye alma:** Aşamalı devreye al, her adımda performansı doğrula
7. **İnce ayar:** 2-4 hafta boyunca PID parametreleri ve eşik değerlerini optimize et
8. **Doğrulama:** Tasarrufu ölçüm ile belgele, referans değerleri güncelle
9. **Eğitim:** Operatörlere yeni kontrol mantığı ve müdahale prosedürlerini öğret

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Konfor kaybı | Basınç düşürüldüğünde son noktalarda yetersiz debi | Kademeli düşür, şikayet takibi yap |
| Sensör arızası | Yanlış sensör verisi ile yanlış kontrol | Sensör arıza modu tanımla (fail-safe) |
| Karmaşık otomasyon | Operatörlerin anlayamadığı sistem | Basit HMI, iyi dokümantasyon, eğitim |
| Su çekici (water hammer) | Hızlı pompa açma/kapama | Rampa süreleri, yavaş vana kapanışı |
| Legionella riski | Düşük sıcaklık/basınçta bakteriyel üreme | Termal dezenfeksiyon programı koru |
| Overriding | Operatörlerin manual moda alması | Override alarm, auto-reset zamanlayıcısı |

## İlgili Dosyalar
- Pompa VSD çözümü: `solutions/pump_vsd.md`
- Pompa throttle eliminasyonu: `solutions/pump_throttle_elimination.md`
- Pompa bakım çözümü: `solutions/pump_maintenance.md`
- Pompa motor yükseltme: `solutions/pump_motor_upgrade.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- ASHRAE 90.1-2019 — "Energy Standard for Buildings Except Low-Rise Residential Buildings" (Pumping requirements)
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Grundfos, "Application Guide: Variable Speed Pumping in HVAC Systems"
- Grundfos, "Demand Driven Distribution (DDD)" Technical Documentation
- Hydraulic Institute, "Optimizing Pumping Systems: A Guide for Improved Energy Efficiency"
- ISO 14414 — "Pump system energy assessment"
- CX Associates, "Testing Differential Pressure Reset For Fun and Profit" (2012)
