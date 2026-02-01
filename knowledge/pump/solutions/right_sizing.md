---
title: "Çözüm: Pompa Boyutlandırma Optimizasyonu — Pump Right-Sizing"
category: solutions
equipment_type: pump
keywords: [boyutlandırma, pompa, BEP, verimlilik]
related_files: [pump/formulas.md, pump/solutions/impeller_trimming.md, pump/benchmarks.md]
use_when: ["Pompa doğru boyutlandırma önerilirken", "Aşırı boyutlu pompa değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Pompa Boyutlandırma Optimizasyonu — Pump Right-Sizing

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Endüstriyel pompaların %20-30'u aşırı boyutlandırılmıştır (oversized). Kademeli güvenlik marjları (cascading safety margins) sonucunda pompalar gerçek ihtiyacın çok üzerinde kapasiteyle seçilir. Bu durum sürekli enerji israfına, erken aşınmaya ve kontrol problemlerine yol açar. DOE araştırmalarına göre, pompa sistemlerinde tüketilen enerjinin %30-50'si ekipman veya kontrol değişiklikleri ile tasarruf edilebilir.

**Çözüm:** Gerçek sistem ihtiyacını ölçerek pompa boyutunu optimize etmek — yeni pompa seçimi, impeller kesme veya VSD uygulaması ile.

**Tipik Tasarruf:** %15-40
**Tipik ROI:** 1-4 yıl

## Çalışma Prensibi

Aşırı boyutlandırılmış pompa, sisteme gereğinden fazla debi ve/veya head sağlar. Fazla enerji kısma vanası, bypass hattı veya düşük verimli çalışma noktasında harcanır. Doğru boyutlandırma, pompa seçimini gerçek sistem eğrisine ve BEP (Best Efficiency Point) noktasına yakın olacak şekilde optimize eder.

## Oversizing (Aşırı Boyutlandırma) Nedenleri

| Neden | Açıklama | Tipik Marj |
|-------|----------|-----------|
| Proses tasarım marjı | Proses mühendisi "yetersiz kalmasın" diye marj ekler | +%10-20 debi |
| Boru sistemi belirsizliği | Boru güzergahı henüz belli değilken basınç kaybı tahmini | +%15-25 head |
| Gelecek genişleme | "Gelecekte kapasite artabilir" varsayımı | +%20-50 |
| Pompa üreticisi marjı | Üretici garanti performansını aşmak için büyük seçer | +%5-10 |
| Standart boyut sıçraması | Hesaplanan değer iki boyut arasında kalır, büyüğü seçilir | +%10-20 |
| Kademeli birikim (cascading) | Tüm marjlar üst üste eklenir | Toplam: +%50-100 |

**Sonuç:** Gerçekte 30 kW pompa yeterli olan sisteme 55-75 kW pompa kurulabilir.

## Oversizing Belirtileri

Aşağıdaki durumlardan biri veya birkaçı varsa pompa büyük olasılıkla aşırı boyutlandırılmıştır:

| Belirti | Açıklama |
|---------|----------|
| Kısma vanası sürekli kısık | Vana <%60 açık, sürekli throttle ile debi kontrol ediliyor |
| Bypass hattı açık | Fazla debi bypass ile tanka veya suction'a geri gönderiliyor |
| Pompa BEP'in çok solunda | Gerçek debi, BEP debisinin <%70'i |
| Aşırı gürültü/titreşim | İç resirkülasyon ve kavitasyon belirtileri |
| Sık conta/salmastra arızası | Yüksek basınç mekanik parçaları zorluyor |
| Motor düşük yükte çalışıyor | Motor yükü <%50 nominal — düşük güç faktörü |
| Vana bakım sıklığı yüksek | Throttle vanası sürekli kısık çalışmadan yıpranıyor |

## Doğru Boyut Seçimi Kriterleri

### Adım 1: Gerçek Sistem Eğrisini Belirle
```
H_sistem = H_statik + H_sürtünme
H_sürtünme = K × Q²

Burada:
- H_statik = Statik head (yükseklik farkı + tank basıncı) [m]
- H_sürtünme = Sürtünme head kayıpları [m]
- K = Boru sistemi direnç katsayısı
- Q = Debi [m³/h]
```

### Adım 2: Gerçek Debi ve Head Gereksinimini Doğrula
- Sahada debi ve basınç ölçümü yap (en az 1 hafta)
- Minimum, ortalama ve maksimum gereksinimleri belirle
- Proses gereksinimlerini operatörlerle doğrula

### Adım 3: Makul Güvenlik Marjı Uygula
| Parametre | Önerilen Marj | Kaçınılması Gereken |
|-----------|---------------|-------------------|
| Debi | +%5-10 | +%30-50 |
| Head | +%10-15 | +%30-50 |
| Toplam güvenlik | +%10-15 | +%50-100 (cascading) |

### Adım 4: BEP Yakınında Pompa Seç
- Pompa, normal çalışma noktasında BEP'in %80-110 aralığında olmalı (Hydraulic Institute HI 9.6.3)
- Minimum debi, pompa üreticisinin önerdiğinin üzerinde kalmalı

## Mevcut Pompa İçin Alternatif Çözümler

Her zaman yeni pompa almak gerekmez. Mevcut durumda uygulanabilecek alternatifler:

| Çözüm | Tasarruf | Maliyet | En Uygun Durum |
|-------|---------|---------|---------------|
| İmpeller kesme (trimming) | %10-25 | €1,000-7,000 | Sabit oversizing, <%15 çap azaltma yeterli |
| VSD retrofit | %20-60 | €3,000-40,000 | Değişken yük, büyük pompa |
| Yeni doğru boyut pompa | %15-40 | €5,000-50,000 | Pompa eski veya >%20 oversized |
| Paralel küçük pompalar | %10-20 | €10,000-60,000 | Geniş yük değişimi, yedeklilik gerekli |

## Yatırım Maliyeti (Yeni Pompa — Boyuta Göre)

| Pompa Gücü | Standart Santrifüj Pompa | Yüksek Verimli Pompa |
|------------|--------------------------|---------------------|
| 5.5 kW | €2,500-5,000 | €3,500-7,000 |
| 11 kW | €4,000-8,000 | €6,000-12,000 |
| 22 kW | €6,000-12,000 | €9,000-18,000 |
| 37 kW | €8,000-18,000 | €12,000-25,000 |
| 55 kW | €12,000-25,000 | €18,000-38,000 |
| 75 kW | €16,000-35,000 | €25,000-50,000 |
| 110 kW | €22,000-50,000 | €35,000-70,000 |

*Motor, kaplin, taban plakası ve kurulum dahil tahmini fiyatlar.*

## ROI Hesabı

### Formül
```
P_mevcut = P_ölçülen (mevcut güç tüketimi) [kW]
P_yeni = Q_gerekli × H_gerekli × ρ × g / (η_pompa × η_motor × 3600)  [kW]
Yıllık_tasarruf_kWh = (P_mevcut - P_yeni) × Çalışma_saati
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

### Örnek Hesap
- Mevcut: 55 kW pompa, gerçek çekim 38 kW (throttle ile), 7,000 saat/yıl
- Sistem analizi: gerçek ihtiyaç 30 kW pompa ile karşılanabilir
- Yeni pompa BEP'te: 25 kW çekim (verimli çalışma)
- Yıllık tasarruf: (38 - 25) × 7,000 = 91,000 kWh
- Elektrik: €0.15/kWh → Yıllık tasarruf: **€13,650/yıl**
- Yeni pompa + kurulum maliyeti: €20,000
- **Geri ödeme: 20,000 / 13,650 = 1.47 yıl**

## Uygulama Adımları

1. **Envanter tarama:** Tüm pompaları listele; motor güçleri, yaşları ve çalışma koşullarını kaydet
2. **Oversizing taraması:** Kısma vanası pozisyonu, bypass durumu ve motor yükü ile hızlı tarama yap
3. **Önceliklendirme:** Büyük güçlü ve uzun çalışma süreli pompalardan başla (enerji etkisi yüksek)
4. **Detaylı ölçüm:** Debi, basınç, güç profili ile gerçek sistem eğrisini belirle
5. **Çözüm seçimi:** İmpeller trim, VSD veya yeni pompa arasında maliyet-fayda analizi yap
6. **Uygulama:** Seçilen çözümü uygula
7. **Doğrulama:** Uygulama sonrası enerji tüketimini ölç ve tasarrufu doğrula

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yetersiz boyutlandırma | Çok küçük pompa seçilirse proses olumsuz etkilenir | Gerçek ölçüme dayanan boyutlandırma; makul marj (%10-15) |
| Gelecek genişleme | Kapasite artışı olasılığı göz ardı edilebilir | VSD veya paralel pompa ile esneklik sağla |
| Geçici yükler | Startup, cleaning gibi geçici yüksek talepler | Geçici talepler için alternatif çözüm planla |
| Motor verimliliği | Küçük motor seçilirken verimlilik düşebilir | IE3/IE4 sınıfı motor seç |
| Operatör direnci | "Büyük pompa daha güvenli" algısı | Ölçüm verileri ile güven oluştur |

## İlgili Dosyalar
- İmpeller kesme: `solutions/pump_impeller_trimming.md`
- VSD ile kontrol: `solutions/pump_vsd.md`
- Paralel pompa: `solutions/pump_parallel_operation.md`
- Sistem optimizasyonu: `solutions/pump_system_optimization.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry," 2nd Edition
- Hydraulic Institute, ANSI/HI 9.6.3, "Rotodynamic Pumps — Guideline for Allowable Operating Region"
- Hydraulic Institute, "Five Warning Signs of Oversized Pumps—And How to Fix Them" (2022)
- Europump / Hydraulic Institute / DOE, "Variable Speed Pumping: A Guide to Successful Applications"
- Fraunhofer Institute, Industrial Pump Survey (2010) — oversizing statistics
- Pumps & Systems, "The Effects of Oversizing or Undersizing a Pump"
