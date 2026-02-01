---
title: "Çözüm: Pompa Sistemi Optimizasyonu — Pumping System Optimization"
category: solutions
equipment_type: pump
keywords: [sistem, optimizasyon, pompa, boru]
related_files: [pump/formulas.md, pump/benchmarks.md, pump/solutions/throttle_elimination.md]
use_when: ["Pompa sistemi optimizasyonu önerilirken", "Boru hattı kayıpları değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Pompa Sistemi Optimizasyonu — Pumping System Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Boru sistemi ve bileşenler (dirsekler, vanalar, filtreler, daralmalar) gereksiz sürtünme ve basınç kaybı yaratır. Pompa bu kayıpları karşılamak için fazla enerji harcar. Endüstriyel pompalama sistemlerinde toplam elektrik tüketiminin %10-30'u sistem tarafı kayıplardan kaynaklanır.

**Çözüm:** Boru sistemi ve bileşenlerde iyileştirmeler yaparak toplam head gereksinimini düşürmek. Pompa tarafına dokunmadan, sistem tarafı optimizasyonlar ile enerji tüketimini azaltmak.

**Tipik Tasarruf:** %5-15
**Tipik ROI:** 1-5 yıl

## Çalışma Prensibi

Pompa sistemi toplam head gereksinimi:
```
H_toplam = H_statik + H_sürtünme + H_bileşen + H_kontrol

Burada:
- H_statik = Statik yükseklik farkı + tank basınç farkı [m]
- H_sürtünme = Boru sürtünme kayıpları [m]
- H_bileşen = Fitting, vana, filtre vb. kayıpları [m]
- H_kontrol = Kısma vanası kayıpları [m]

Pompa gücü:
P = Q × H_toplam × ρ × g / (η_pompa × η_motor × 3600)  [kW]
```

Sistem optimizasyonu, H_sürtünme, H_bileşen ve H_kontrol bileşenlerini azaltmayı hedefler. H_statik genellikle değiştirilemez (tesis yerleşimi tarafından belirlenir).

## Boru Çapı Artırma

En etkili sistem optimizasyonu aracı boru çapı artırmadır. Sürtünme kaybı boru çapının beşinci kuvveti ile ters orantılıdır:

### Darcy-Weisbach Formülü
```
H_sürtünme = f × (L/D) × (v²/2g)

Burada:
- f = Darcy sürtünme faktörü (boyutsuz)
- L = Boru uzunluğu [m]
- D = Boru iç çapı [m]
- v = Akış hızı [m/s]
- g = yerçekimi ivmesi [9.81 m/s²]

Güç-çap ilişkisi:
P_sürtünme ∝ Q² / D⁵

Sonuç: Boru çapını %20 artırmak sürtünme kaybını ~%60 azaltır.
```

### Boru Çapı Artırma Etki Tablosu

| Çap Artışı | Hız Değişimi | Sürtünme Kaybı Değişimi | Açıklama |
|------------|-------------|------------------------|----------|
| DN50 → DN65 (%30) | -%40 | -%75 | Çok etkili |
| DN80 → DN100 (%25) | -%36 | -%70 | Çok etkili |
| DN100 → DN125 (%25) | -%36 | -%70 | Etkili |
| DN150 → DN200 (%33) | -%44 | -%80 | Büyük etki |

### Optimum Akış Hızları

| Uygulama | Önerilen Hız (m/s) | Maksimum Hız (m/s) |
|----------|-------------------|-------------------|
| Suction (emme) hattı | 1.0-1.5 | 2.0 |
| Discharge (basma) hattı | 1.5-2.5 | 3.5 |
| Ana dağıtım hattı | 1.5-3.0 | 4.0 |
| Soğutma suyu | 1.5-2.5 | 3.0 |

*Hız bu değerlerin üzerindeyse boru büyütme değerlendirilmelidir.*

## Dirsek, Vana ve Fitting Kayıpları

Her boru bileşeni ek basınç kaybı yaratır. Bu kayıplar "eşdeğer boru uzunluğu" (equivalent length) olarak ifade edilir:

### Eşdeğer Uzunluk Tablosu (DN100 boru için)

| Bileşen | Eşdeğer Uzunluk (m) | K Faktörü |
|---------|---------------------|-----------|
| 90° standart dirsek | 3.0 | 0.75 |
| 90° uzun yarıçaplı dirsek | 2.0 | 0.45 |
| 45° dirsek | 1.5 | 0.35 |
| T-parça (düz geçiş) | 2.0 | 0.40 |
| T-parça (branş) | 5.0 | 1.30 |
| Küresel vana (tam açık) | 0.5 | 0.10 |
| Kelebek vana (tam açık) | 2.5 | 0.50 |
| Sürgülü vana (tam açık) | 0.5 | 0.10 |
| Geri dönüş vanası (check valve) | 5.0 | 1.50 |
| Y-tipi filtre (temiz) | 5.0 | 1.20 |
| Ani daralma (D/2) | 2.0 | 0.50 |
| Ani genişleme (2D) | 4.0 | 1.00 |
| Giriş (sharp-edged) | 1.5 | 0.50 |
| Giriş (rounded, bell-mouth) | 0.3 | 0.05 |

## Bypass Hattı Eliminasyonu

Bypass hattı, fazla debiyi pompanın suction tarafına veya tanka geri gönderir. Bu durum:
- Pompa gereksiz yere tam kapasitede çalışır
- Bypass hattında enerji tamamen israf olur
- Sıvı ısınır (enerji ısıya dönüşür)

### Bypass Eliminasyonu Tasarrufu
```
P_bypass_israf = Q_bypass × H_pompa × ρ × g / (η_pompa × 3600)  [kW]

Örnek:
- 100 m³/h pompa, %30'u bypass → Q_bypass = 30 m³/h
- H_pompa = 40 m, η_pompa = 0.75
- P_israf = 30 × 40 × 1000 × 9.81 / (0.75 × 3,600,000) = 4.36 kW
- 6000 saat/yıl → 26,160 kWh/yıl = €3,924/yıl israf
```

**Çözüm:** Bypass hattı yerine VSD, impeller trim veya doğru boyut pompa kullan.

## Gereksiz Bileşen Çıkarma

Zaman içinde eklenen ama artık gerekli olmayan bileşenler sisteme gereksiz basınç kaybı ekler:

| Gereksiz Bileşen | Tipik Kayıp | Kontrol Et |
|-------------------|------------|-----------|
| Kullanılmayan filtre (tıkalı) | 2-10 m head | Filtre basınç farkını ölç |
| Fazla dirsek (gereksiz güzergah) | Her biri 1-3 m | Boru güzergahını gözden geçir |
| Yarı açık vana (unutulmuş) | 5-20 m head | Tüm vana pozisyonlarını kontrol et |
| Eski orifis plaka (artık gerekmez) | 2-8 m head | Proses gereksinimini doğrula |
| Fazla genişleme/daralma | Her biri 1-4 m | Boru planını incele |

## Boru Yüzey Pürüzlülüğü Etkisi

Boru iç yüzey pürüzlülüğü (roughness) sürtünme faktörünü doğrudan etkiler:

| Boru Malzemesi / Durum | Pürüzlülük ε (mm) | Sürtünme Etkisi |
|-----------------------|-------------------|----------------|
| Yeni çelik boru | 0.045 | Referans |
| Eski çelik boru (korozyonlu) | 0.5-2.0 | %30-100 daha fazla sürtünme |
| Paslanmaz çelik | 0.015 | %10-20 daha az sürtünme |
| PVC / HDPE plastik | 0.005 | %30-50 daha az sürtünme |
| Bakır | 0.0015 | %40-60 daha az sürtünme |
| İç kaplama (epoksi lining) | 0.01 | Eski boruyu yeniler |

**Uyarı:** Eski çelik borularda korozyon ve tortu birikimi sürtünmeyi 2-5 kat artırabilir. İç temizlik veya kaplama önemli tasarruf sağlayabilir.

## Sistem Basınç Haritası Çıkarma Yöntemi

### Adım 1: Ölçüm Noktaları Belirle
- Pompa çıkışı (discharge)
- Ana hat branş noktaları
- Kritik kullanım noktaları (en uzak, en yüksek)
- Kısma vanası öncesi ve sonrası

### Adım 2: Basınç Ölçümü
- Her noktada basınç manometresi veya transmitter ile ölç
- Normal çalışma koşullarında (tam yük ve kısmi yük)

### Adım 3: Basınç Haritası Çiz
```
Pompa çıkışı: 6.0 bar
  ↓ Ana hat (200 m): -0.3 bar → 5.7 bar
    ↓ Dirsek + fitting: -0.2 bar → 5.5 bar
      ↓ Filtre: -0.5 bar → 5.0 bar  ← YÜKSEK KAYIP!
        ↓ Kısma vanası: -1.2 bar → 3.8 bar  ← EN BÜYÜK KAYIP!
          ↓ Kullanım noktası: 3.8 bar (gerekli: 3.5 bar)
```

### Adım 4: Yüksek Kayıp Noktalarını Tespit Et
- Kısma vanası kaybı: VSD veya impeller trim ile elimine et
- Filtre kaybı: Temizle/değiştir veya daha büyük filtre kur
- Boru kaybı: Kritik bölümlerde çap artır

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Boru sistemi eski ve hiç optimize edilmemiş
- Sürtünme head, toplam head'in >%30'u
- Tıkanmış filtre veya yarı açık vana tespit edilmiş
- Büyük yenileme veya genişleme projesi planlanıyor
- Boru çapları mevcut debiler için yetersiz (yüksek hızlar)

### Ne Zaman Uygulanmamalı
- Sistem zaten iyi tasarlanmış ve bakımlı
- Sürtünme head toplam head'in <%15'i
- Boru değişimi fiziksel olarak çok zor veya pahalı
- Tesis yakında kapatılacak

## Yatırım Maliyeti

| İyileştirme | Maliyet Aralığı (€) | Karmaşıklık |
|-------------|---------------------|-------------|
| Vana pozisyon kontrolü ve düzeltme | €0-500 | Düşük |
| Filtre temizleme/değişimi | €200-2,000 | Düşük |
| Gereksiz bileşen çıkarma | €500-3,000 | Düşük-Orta |
| Boru iç temizleme (pigging) | €2,000-10,000 | Orta |
| Boru iç kaplama (lining) | €5,000-20,000 | Orta |
| Dirsek değişimi (uzun yarıçaplı) | €1,000-5,000 | Orta |
| Boru çapı artırma (kısa bölüm) | €5,000-20,000 | Orta-Yüksek |
| Boru çapı artırma (uzun hat) | €20,000-100,000+ | Yüksek |

*Boru çapı artırma pahalıdır; genelde büyük yenileme/genişleme sırasında ekonomik olur.*

## ROI Hesabı

### Formül
```
ΔH = H_kayıp_mevcut - H_kayıp_yeni   [m head azalma]
ΔP = Q × ΔH × ρ × g / (η_pompa × η_motor × 3600)   [kW tasarruf]
Yıllık_tasarruf_kWh = ΔP × Çalışma_saati
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

### Örnek Hesap
- 45 kW pompa, 80 m³/h, 50 m toplam head, 7,000 saat/yıl
- Sistem analizi: 8 m head gereksiz kayıplardan (tıkalı filtre: 3 m, yarı açık vana: 3 m, gereksiz dirsekler: 2 m)
- Head azalma: 50 m → 42 m (%16 azalma)
- Güç tasarrufu: 45 × (8/50) = 7.2 kW
- Yıllık tasarruf: 7.2 × 7,000 = 50,400 kWh = **€7,560/yıl**
- İyileştirme maliyeti: €8,000 (filtre + vana + dirsek değişimi)
- **Geri ödeme: 8,000 / 7,560 = 1.06 yıl**

## Uygulama Adımları

1. **Sistem basınç haritası:** Tüm kritik noktalarda basınç ölçümü yap
2. **Kayıp analizi:** Her bileşenin basınç kaybını hesapla/ölç
3. **Önceliklendirme:** En yüksek kayıplı noktaları belirle (80/20 kuralı)
4. **Hızlı kazanımlar:** Vana düzeltme, filtre temizleme gibi düşük maliyetli işleri hemen uygula
5. **Orta vadeli iyileştirmeler:** Gereksiz bileşen çıkarma, dirsek değişimi planla
6. **Uzun vadeli yatırımlar:** Boru çapı artırma gibi büyük işleri yenileme projesine dahil et
7. **Doğrulama:** İyileştirme sonrası basınç haritasını tekrarla, tasarrufu ölç

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yetersiz analiz | Yanlış bileşen değiştirilirse tasarruf olmaz | Basınç haritası ile kayıp noktalarını doğrula |
| Üretim kesintisi | Boru değişimi üretimi durdurabilir | Planlı duruşlarda uygula |
| Hız değişimi | Boru büyütme sonrası hız düşerse çökelme olabilir | Minimum hız gereksinimini kontrol et |
| Maliyet aşımı | Boru değişimi projesi beklenenden pahalı olabilir | Detaylı keşif ve maliyet analizi yap |
| Su darbesi (water hammer) | Vana veya bileşen değişikliği su darbesi riskini etkileyebilir | Geçiş analizi yaptır |

## İlgili Dosyalar
- VSD ile kontrol: `solutions/pump_vsd.md`
- İmpeller kesme: `solutions/pump_impeller_trimming.md`
- Pompa boyutlandırma: `solutions/pump_right_sizing.md`
- Paralel pompa: `solutions/pump_parallel_operation.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- Hydraulic Institute, "Eight Tips to Boost Pump Piping Efficiency" (2023)
- Hydraulic Institute, ANSI/HI 14.3-2019, "Rotodynamic Pumps for Design and Application"
- Europump / Hydraulic Institute / DOE, "Variable Speed Pumping: A Guide to Successful Applications"
- Pumps & Systems, "Minimizing Pumping-System Friction Loss"
- Darcy-Weisbach equation, Moody chart — standard hydraulic engineering references
