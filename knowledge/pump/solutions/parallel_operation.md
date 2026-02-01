---
title: "Çözüm: Paralel Pompa Operasyonu — Parallel Pump Operation"
category: solutions
equipment_type: pump
keywords: [paralel, pompa, çalışma, kapasite]
related_files: [pump/formulas.md, pump/solutions/control_optimization.md, pump/benchmarks.md]
use_when: ["Paralel pompa çalışması önerilirken", "Çoklu pompa yönetimi değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Paralel Pompa Operasyonu — Parallel Pump Operation

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Tek büyük pompa, değişken talep altında çoğu zaman kısmi yükte çalışır. BEP noktasından uzakta düşük verimle çalışır, enerji harcar ve mekanik stres yaşar.

**Çözüm:** Tek büyük pompa yerine birden fazla küçük pompa kullanarak talebe göre kademeli çalıştırma (staging/sequencing). Her pompa BEP'e yakın çalışır, toplam sistem verimi artar.

**Tipik Tasarruf:** %10-20
**Tipik ROI:** 2-5 yıl

## Çalışma Prensibi

Paralel bağlı pompalar aynı suction ve discharge manifolduna bağlanır. Her bir pompa aynı head'i üretir; debiler toplanır.

### Paralel Pompa Eğrisi Oluşturma
```
Paralel pompa eğrisi: Her head (H) değerinde debiler (Q) toplanır.

Tek pompa:    Q₁ @ H
İki pompa:    Q₁ + Q₂ @ H  (aynı head'de)
Üç pompa:     Q₁ + Q₂ + Q₃ @ H

Not: Özdeş pompalar için Q_toplam = n × Q_tek (aynı head'de)
Ancak sistem eğrisi ile kesişim noktası toplam debiyi belirler.
Gerçek artış n × Q_tek değildir; sürtünme head artışı nedeniyle daha azdır.
```

**Kritik kural:** Paralel pompalar ancak aynı (veya çok yakın) shut-off head değerine sahipse birlikte çalışabilir. Aksi takdirde düşük head'li pompa geri akışa maruz kalır.

## Sequencing (Sıralama) Stratejileri

| Strateji | Açıklama | Avantaj | Dezavantaj |
|----------|----------|---------|-----------|
| Lead/Lag | Birincil pompa sürekli çalışır; ikinci pompa talep artınca devreye girer | Basit kontrol, enerji tasarrufu | Lead pompa daha fazla yıpranır |
| Duty/Standby | Bir pompa aktif, diğeri arıza durumunda yedek | Yüksek güvenilirlik | Enerji tasarrufu yok (tek pompa çalışır) |
| Rotasyonlu Lead/Lag | Lead pompa günlük/haftalık rotasyonla değişir | Eşit aşınma dağılımı | Kontrol sistemi gerektirir |
| Lead/Lag/Standby | Lead + Lag çalışır; üçüncü pompa yedek | Yüksek kapasite + yedeklilik | Daha fazla yatırım |

## Performans Karşılaştırması: 2 Pompa Sistemi

### Senaryo: 100 m³/h toplam kapasite

| Konfigürasyon | Talep: 40 m³/h | Talep: 60 m³/h | Talep: 80 m³/h | Talep: 100 m³/h |
|---------------|----------------|----------------|----------------|-----------------|
| Tek 100 m³/h pompa | %40 yük — düşük verim | %60 yük — orta verim | %80 yük — iyi verim | %100 yük — BEP |
| 2 × 50 m³/h (Lead/Lag) | 1 pompa %80 — iyi | 1 pompa %100 + lead | 2 pompa %80 — iyi | 2 pompa %100 — BEP |
| Verim farkı | +%8-12 puan | +%5-8 puan | +%3-5 puan | ~Eşdeğer |

## Performans Karşılaştırması: 3 Pompa Sistemi

### Senaryo: 150 m³/h toplam kapasite, 3 × 50 m³/h pompa

| Talep (m³/h) | Çalışan Pompa Sayısı | Her Pompa Yükü | Sistem Verimi | Tek 150 m³/h Pompaya Göre Tasarruf |
|--------------|---------------------|----------------|--------------|-----------------------------------|
| 30 | 1 | %60 | Orta | +%5-10 |
| 50 | 1 | %100 (BEP) | Yüksek | +%10-15 |
| 75 | 2 | %75 | İyi | +%8-12 |
| 100 | 2 | %100 (BEP) | En yüksek | +%10-15 |
| 120 | 3 | %80 | İyi | +%5-8 |
| 150 | 3 | %100 (BEP) | En yüksek | ~Eşdeğer |

## Optimal Sıralama Kuralları

1. **Staging-up (pompa ekleme):** Lead pompa hızı/yükü >%90-95 olduğunda lag pompa devreye girer
2. **Staging-down (pompa çıkarma):** Toplam yük ≤(n-1) pompa kapasitesinin %80'ine düştüğünde bir pompa kapatılır
3. **Zamanlama:** Staging gecikmesi 3-10 dakika (ani dalgalanmalarda gereksiz on/off önlenir)
4. **Rotasyon:** Lead pompa 24-168 saatte bir değiştirilir (eşit aşınma)
5. **Minimum çalışma süresi:** Her pompa devreye girdiğinde minimum 15-30 dakika çalışmalı

## VSD + Sabit Hız Kombinasyonu (Baz Yük + Trim)

En verimli paralel pompa stratejisi: sabit hızlı pompa(lar) baz yükü karşılar, VSD'li pompa değişken "trim" talebini karşılar.

### Tasarım Prensibi
```
Toplam_debi = Q_sabit_hız_pompalar + Q_VSD_pompa

Baz yük: Sabit hızlı pompa(lar) BEP'te tam verimle çalışır
Trim yük: VSD pompa geriye kalan talebi karşılar (tüm hız aralığında verimli)
```

### Uygulama Örneği
- Sistem: toplam 200 m³/h, değişken talep 80-200 m³/h
- 2 × 80 m³/h sabit hızlı pompa (baz yük)
- 1 × 80 m³/h VSD pompa (trim yük)
- 80 m³/h talep: sadece VSD pompa çalışır
- 120 m³/h talep: 1 sabit + VSD (%50)
- 160 m³/h talep: 2 sabit + VSD (%0 veya düşük)
- 200 m³/h talep: 2 sabit + VSD (%100)

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Talep geniş aralıkta değişiyorsa (max/min oranı > 2:1)
- Yedeklilik (redundancy) gerekiyorsa
- Mevcut tek pompa sürekli kısmi yükte çalışıyorsa
- Yeni tesis tasarımı yapılıyorsa
- Kapasite artışı planlanıyorsa

### Ne Zaman Uygulanmamalı
- Sabit yük — tek pompa BEP'te yeterli
- Çok küçük sistem — paralel pompanın ek maliyeti haklı değil
- Alan kısıtı — ek pompa/manifold için yer yok

## Yatırım Maliyeti

| Sistem Kapasitesi | Tek Büyük Pompa | 2 Paralel Pompa (Sabit) | 2 Sabit + 1 VSD |
|-------------------|----------------|------------------------|-----------------|
| 50 m³/h, 30 m head | €10,000-18,000 | €14,000-24,000 | €22,000-38,000 |
| 100 m³/h, 40 m head | €18,000-30,000 | €24,000-40,000 | €38,000-60,000 |
| 200 m³/h, 50 m head | €30,000-50,000 | €40,000-65,000 | €60,000-95,000 |
| 500 m³/h, 60 m head | €60,000-100,000 | €80,000-130,000 | €120,000-190,000 |

*Manifold, vanalar, kontrol sistemi ve kurulum dahil.*

## ROI Hesabı

### Formül
```
P_tek = P_pompa_tek × (Güç%_kısmi_yük / 100)     [kW — sürekli]
P_paralel = Σ (P_pompa_i × Yük%_i / 100)          [kW — kademeli çalışma]
Yıllık_tasarruf_kWh = (P_tek - P_paralel) × Çalışma_saati
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Ek_yatırım = Maliyet_paralel - Maliyet_tek
Geri_ödeme_yıl = Ek_yatırım / Yıllık_tasarruf_EUR
```

### Örnek Hesap
- Mevcut: 75 kW tek pompa, ortalama %55 yükte, verim %65 → 42 kW ortalama çekim
- Yeni: 2 × 37 kW paralel pompa, kademeli çalışma, ortalama verim %78 → 32 kW toplam
- Çalışma: 6,500 saat/yıl, elektrik €0.15/kWh
- Yıllık tasarruf: (42 - 32) × 6,500 = 65,000 kWh = **€9,750/yıl**
- Ek yatırım (paralel sistem — tek pompa farkı): €25,000
- **Geri ödeme: 25,000 / 9,750 = 2.56 yıl**

## Uygulama Adımları

1. **Yük profili analizi:** En az 2 haftalık debi/basınç ölçümü ile talep dağılımını belirle
2. **Pompa seçimi:** Her pompanın BEP'i, baskın talep aralığına denk gelecek şekilde boyutlandır
3. **Manifold tasarımı:** Suction ve discharge manifold boyutlarını toplam debi için hesapla
4. **Kontrol sistemi:** PLC/SCADA ile staging mantığı, rotasyon ve alarm programla
5. **Vana konfigürasyonu:** Her pompa için check valve (geri dönüş vanası) ve izolasyon vanası kur
6. **Devreye alma:** Staging setpoint'leri optimize et, geçiş sürelerini ayarla
7. **Doğrulama:** Kademeli çalışma performansını izle, enerji tasarrufunu ölç

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Shut-off head uyumsuzluğu | Farklı pompaların shut-off head'i uyumsuz olursa geri akış olur | Aynı veya çok yakın pompa eğrileri seç |
| Geri akış (backflow) | Kapalı pompa üzerinden ters akış | Her pompaya check valve kur |
| Kontrol karmaşıklığı | Staging mantığı düzgün çalışmazsa enerji tasarrufu kaybolur | PLC/SCADA ile otomatik kontrol |
| Hunting (sürekli on/off) | Staging setpoint'leri yanlışsa pompalar sürekli devreye girip çıkar | Uygun hysteresis ve gecikme süresi ayarla |
| Alan gereksinimi | Paralel pompalar daha fazla yer kaplar | Tasarım aşamasında alan planlaması yap |
| Standby pompa sorunları | Uzun süre çalışmayan pompa sıkışabilir | Haftalık kısa çalıştırma rotasyonu |

## İlgili Dosyalar
- VSD ile kontrol: `solutions/pump_vsd.md`
- Pompa boyutlandırma: `solutions/pump_right_sizing.md`
- Sistem optimizasyonu: `solutions/pump_system_optimization.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- DOE Pumping Systems Tip Sheet, "Optimize Parallel Pumping Systems"
- Hydraulic Institute, ANSI/HI 14.3-2019, "Rotodynamic Pumps for Design and Application"
- Europump / Hydraulic Institute / DOE, "Variable Speed Pumping: A Guide to Successful Applications"
- Pumps & Systems, "The Basics of Lead-Lag Configurations" (2015)
