---
title: "Endüstriyel Uygulama Rehberi (Practical Implementation Guide)"
category: thermoeconomic_optimization
keywords: [pratik uygulama, kontrol listesi, yaygın hatalar, Türkiye maliyet verileri, raporlama]
related_files: [knowledge/factory/thermoeconomic_optimization/iterative_method.md, knowledge/factory/thermoeconomic_optimization/sensitivity_analysis.md, knowledge/factory/thermoeconomic_optimization/objective_functions.md]
use_when: ["Endüstriyel termoekonomik optimizasyon uygulaması yapılırken", "Türkiye spesifik maliyet verileri ve varsayılan parametreler gerektiğinde"]
priority: high
last_updated: 2026-02-02
---

# Endüstriyel Uygulama Rehberi (Practical Implementation Guide)

## 1. 10 Adımlı Uygulama Prosedürü

### Adım 1: Proje Kapsamı ve Hedef Belirleme

```
Sorular:
  □ Yeni tesis mi, mevcut tesis retrofit mu?
  □ Hangi ekipmanlar kapsama alınacak?
  □ Bütçe kısıtı var mı?
  □ Karbon maliyeti (CBAM) dikkate alınacak mı?
  □ Tek amaçlı mı, çok amaçlı mı?
  □ Karar verici kim? Teknik ekip mi, yönetim mi?

Çıktı: Proje tanımı (scope) belgesi
```

### Adım 2: Veri Toplama

```
Gerekli veriler (Adım 3 kontrol listesi):
  □ Ekipman spesifikasyonları (kapasite, verim, yıl)
  □ Enerji tüketim faturaları (12 aylık)
  □ Proses talep profilleri (buhar, basınçlı hava, soğutma)
  □ Ekipman maliyet bilgisi (fatura, teklif)
  □ Enerji fiyatları (doğalgaz, elektrik, su)
  □ Çalışma saatleri (yıllık, vardiya düzeni)
  □ Yük profilleri (saatlik veya günlük)

Kaynak: `factory/data_collection.md`
```

### Adım 3: Veri Kalitesi Kontrolü

```
Kontrol noktaları:
  □ Enerji dengesi kapanıyor mu? (giriş ≈ çıkış + kayıp, <%5 hata)
  □ Ekipman verimleri fiziksel sınırlar içinde mi?
  □ Proses talebi ile üretim tutarlı mı?
  □ Eksik veri varsa → varsayım belgelenmiş mi?
  □ Ölçüm belirsizlikleri tanımlanmış mı?
```

### Adım 4: Exergy Analizi

```
Her bileşen için:
  □ Referans ortam koşulları tanımla (T₀, P₀, bileşim)
  □ Her akışın exergy hesapla (fiziksel + kimyasal)
  □ F ve P tanımla (SPECO yöntemi)
  □ Ėx_F, Ėx_P, Ėx_D, Ėx_L hesapla
  □ ε_k ve y_D,k hesapla
  □ Sonuçları doğrula (Ėx_D > 0, ε < 1)

Araç: CoolProp (su/buhar), ideal gaz tabloları
```

### Adım 5: Ekonomik Analiz

```
Her bileşen için:
  □ Mevcut ekipman maliyetini belirle (veya korelasyon ile tahmin)
  □ CEPCI ile güncelle
  □ Türkiye çarpanı uygula
  □ CRF hesapla (iskonto oranı + ömür)
  □ Ż_k hesapla
  □ Yakıt maliyet hızı hesapla

Kaynak: `objective_functions.md` (maliyet korelasyonları)
```

### Adım 6: Exergoekonomik Analiz

```
Denge denklemleri:
  □ Her bileşen için maliyet dengesi yaz
  □ Yardımcı denklemler ekle (F-kuralı, P-kuralı)
  □ Doğrusal denklem sistemini çöz → c ve Ċ değerleri
  □ f_k, r_k, Ċ_D,k hesapla
  □ Sonuçları yorumla

Kaynak: `overview.md` (SPECO), `iterative_method.md` (yorumlama)
```

### Adım 7: Optimizasyon

```
Yöntem seçimi:
  □ Mevcut sistem, basit → İteratif yöntem
  □ Mevcut sistem, parametrik → SQP veya DE+SQP
  □ Yeni tesis / konfigürasyon kararı → MINLP (GA)
  □ Çok amaçlı → NSGA-II
  □ Büyük bütçe kısıtı → Portföy optimizasyonu

Kaynak: `algorithms.md` (algoritma seçim matrisi)
```

### Adım 8: Duyarlılık Analizi

```
Minimum:
  □ Enerji fiyatı duyarlılığı (±20-30%)
  □ Çalışma saati duyarlılığı (±20%)
  □ Tornado diyagramı

Önerilir:
  □ İskonto oranı duyarlılığı
  □ Karbon fiyatı senaryoları
  □ Monte Carlo (büyük yatırımlar için)

Kaynak: `sensitivity_analysis.md`
```

### Adım 9: Raporlama

```
Rapor içeriği:
  □ Yönetici özeti (1 sayfa)
  □ Mevcut durum exergy analizi
  □ Exergoekonomik analiz tabloları
  □ Optimizasyon sonuçları (önce/sonra)
  □ Yatırım gereksinimi ve getiri (NPV, SPP, IRR)
  □ Duyarlılık analizi sonuçları
  □ Uygulama yol haritası (Quick Win → Stratejik)
  □ Risk değerlendirmesi

Kaynak: Bölüm 8 (raporlama şablonu)
```

### Adım 10: Uygulama ve İzleme

```
  □ Öncelik sırasına göre uygula (Quick Win önce)
  □ Uygulama sonrası ölçüm ve doğrulama (M&V)
  □ Gerçekleşen tasarruf vs tahmin karşılaştırması
  □ Periyodik tekrar analiz (yılda 1)
```

---

## 2. Veri Gereksinimleri Kontrol Listesi

### 2.1. Ekipman Verileri

| Veri | Kazan | Kompresör | Chiller | Pompa | HX |
|------|-------|-----------|---------|-------|----|
| Kapasite [kW] | ✓ | ✓ | ✓ | ✓ | ✓ |
| Nominal verim [%] | ✓ | ✓ (kW/m³) | ✓ (COP) | ✓ (η_pump) | ✓ (η_HX) |
| Giriş T, P | ✓ | ✓ | ✓ | ✓ | ✓ |
| Çıkış T, P | ✓ | ✓ | ✓ | ✓ | ✓ |
| Debi | ✓ (buhar) | ✓ (hava) | ✓ (soğutucu) | ✓ (su) | ✓ (her akış) |
| Elektrik tüketimi | ✓ (fan, pompa) | ✓ | ✓ | ✓ | - |
| Yakıt tüketimi | ✓ | - | - | - | - |
| Yaş/durum | ✓ | ✓ | ✓ | ✓ | ✓ |
| Maliyet (satın alma) | ✓ | ✓ | ✓ | ✓ | ✓ |

### 2.2. Ekonomik Veriler

| Veri | Kaynak | Güncelleme |
|------|--------|-----------|
| Doğalgaz fiyatı [€/m³] | EPDK / Fatura | Aylık |
| Elektrik fiyatı [€/kWh] | EPDK / Fatura | Aylık |
| Su fiyatı [€/m³] | Belediye / Fatura | Yıllık |
| İskonto oranı [%] | Finans departmanı | Yıllık |
| EUR/TL kuru | TCMB | Günlük |
| Ekipman maliyeti | Teklif / Korelasyon | Proje bazlı |
| İşçilik maliyeti [€/saat] | İK departmanı | Yıllık |

### 2.3. Operasyonel Veriler

| Veri | Kaynak | Detay |
|------|--------|-------|
| Yıllık çalışma saati | Üretim planlama | Vardiya × gün × ay |
| Yük profili | SCADA / Sayaç | Saatlik veya günlük |
| Mevsimsellik | Geçmiş veri | 12 aylık ortalama |
| Bakım programı | Bakım departmanı | Duruş süreleri |
| Üretim miktarı | Üretim planlama | ton/yıl, birim/yıl |

---

## 3. Yöntem Seçim Matrisi

| Durum | Önerilen Yöntem | Gerekçe |
|-------|----------------|---------|
| Tek ekipman, mevcut sistem | İteratif yöntem | Basit, hızlı |
| Tek ekipman, parametre optimizasyonu | SQP (multi-start) | Hassas sonuç |
| Fabrika, mevcut sistem, hızlı tarama | Basitleştirilmiş tarama (Bölüm 5) | Enerji denetimi |
| Fabrika, retrofit, <200k € yatırım | İteratif + parametrik | Yeterli detay |
| Fabrika, retrofit, >200k € yatırım | Parametrik + duyarlılık | Detaylı analiz |
| Yeni tesis / büyük retrofit | Yapısal + parametrik | Konfigürasyon kararı |
| CHP kararı | Yapısal (MINLP) | İkili karar |
| CBAM etkili sektör | Çok amaçlı (NSGA-II) | Maliyet + CO₂ |
| Bütçe kısıtı altında | Portföy optimizasyonu | Knapsack problemi |

---

## 4. Türkiye Pazarı Ekipman Maliyet Korelasyonları

### 4.1. Güncel Maliyet Referansları (2024, EUR)

| Ekipman | Kapasite | PEC Aralığı [€] | TCI Aralığı [€] |
|---------|---------|----------------|-----------------|
| Kazan (doğalgaz, yerli) | 500-5,000 kW | 15,000-80,000 | 35,000-180,000 |
| Kazan (doğalgaz, ithal) | 500-5,000 kW | 20,000-100,000 | 55,000-300,000 |
| Economizer | 10-100 m² | 3,000-25,000 | 6,000-50,000 |
| Air preheater | 50-500 kW | 5,000-35,000 | 12,000-75,000 |
| Kompresör (vidalı, ithal) | 20-200 kW | 8,000-60,000 | 22,000-170,000 |
| VSD (retrofit) | 20-200 kW | 3,000-15,000 | 4,500-22,000 |
| Chiller (santrifüj) | 100-1,000 kW | 20,000-120,000 | 55,000-350,000 |
| Pompa (santrifüj, yerli) | 5-100 kW | 2,000-15,000 | 5,000-35,000 |
| HX (shell-tube, yerli) | 10-200 m² | 3,000-40,000 | 6,000-80,000 |
| HX (plakalı, ithal) | 5-100 m² | 4,000-50,000 | 8,000-90,000 |
| CHP (gaz motoru) | 100-2,000 kWe | 100,000-800,000 | 250,000-2,000,000 |
| CHP (gaz türbini) | 500-5,000 kWe | 150,000-1,500,000 | 400,000-4,000,000 |

### 4.2. Kurulum Çarpanları

```
TCI = PEC × f_kurulum × f_Türkiye

f_kurulum (PEC → TCI):
  Mekanik ekipman: 2.5-3.5
  Elektrik/kontrol: 3.0-4.0
  CHP sistemi: 2.5-3.0

f_Türkiye (pazar düzeltme):
  Yerli üretim: 0.80-0.90
  İthal (AB): 1.05-1.15
  İthal (Çin): 0.70-0.85
```

---

## 5. Yaklaşık Hesaplama Yöntemi (Hızlı Tarama)

Enerji denetçileri için detaylı optimizasyon yapmadan hızlı ekonomik değerlendirme:

### 5.1. Basitleştirilmiş Ċ_D Hesaplama

```
Her bileşen için:
  Ċ_D,k ≈ c_fuel × Ėx_D,k    [€/h]

Burada:
  c_fuel = Yakıt exergy birim maliyeti (doğalgaz: ~0.037 €/kWh)
  Ėx_D,k = Exergy yıkımı [kW] (exergy analizinden)

Yıllık:
  C_D,k ≈ c_fuel × Ėx_D,k × τ    [€/yıl]
```

### 5.2. Hızlı Tarama Prosedürü

```
1. Her ekipman için Ėx_D hesapla (motor nominal, kompresör basınç, kazan verim)
2. Ċ_D,k = c_fuel × Ėx_D,k × τ hesapla
3. Ċ_D,k'ları büyükten küçüğe sırala → Öncelik listesi
4. İlk 3 büyük kaynak için basit iyileştirme öneri ve tahmini tasarruf
5. Tahmini yatırım ile SPP hesapla

Bu tarama 2-4 saatte yapılabilir.
```

### 5.3. Hızlı Tarama Örneği

Tekstil fabrikası hızlı tarama:

| Bileşen | Ėx_D [kW] | Ċ_D [€/yıl] | Öneri | Tahmini Tasarruf |
|---------|-----------|-------------|-------|-----------------|
| Kazan (yanma) | 1,200 | 244,200 | Kaçınılamaz (büyük kısmı) | ~%10 azaltılabilir |
| Kazan (baca gazı) | 180 | 36,630 | Economizer | ~25,000 €/yıl |
| Kompresör | 28 | 16,940 | VSD + basınç opt. | ~6,000 €/yıl |
| Chiller | 85 | 51,425 | Kondenser opt. | ~8,000 €/yıl |
| Pompa | 12 | 7,260 | VSD | ~3,000 €/yıl |
| **Toplam** | **1,505** | **356,455** | | **~42,000 €/yıl** |

---

## 6. Yaygın Hatalar ve Tuzaklar

### Hata 1: Referans Ortam Tutarsızlığı
```
Problem: Farklı bileşenler için farklı T₀ kullanmak
Etki: Exergy dengeleri kapanmaz, f_k/r_k yanıltıcı
Çözüm: Tüm sistemde tek T₀ (Türkiye: 20°C veya 25°C)
```

### Hata 2: Kaçınılamaz Exergy Yıkımını Görmezden Gelmek
```
Problem: Kazanın f_k = 0.03 çıkıyor → "Kazanı değiştir" demek
Etki: Yanma tersinmezliğinin %60-80'i kaçınılamaz
Çözüm: İleri exergy analizi (kaçınılabilir/kaçınılamaz ayrımı)
       Yalnızca kaçınılabilir Ėx_D kısmını hedefle
```

### Hata 3: Maliyet Korelasyonlarını Doğrudan Kullanmak
```
Problem: ABD bazlı PEC korelasyonunu Türkiye'ye uygulamak
Etki: %30-50 maliyet hatası
Çözüm: CEPCI düzeltmesi + Türkiye çarpanı + yerel teklif ile doğrulama
```

### Hata 4: İskonto Oranı Hatasını Görmezden Gelmek
```
Problem: Türkiye'de nominal %20 faizle, reel %5 iskonto hesaplamak
Etki: CRF çok düşük → yatırım maliyeti hafife alınır
Çözüm: Reel iskonto oranı kullan (nominal - enflasyon, Fisher denklemi)
       Duyarlılık analizi yapılmalı
```

### Hata 5: Kısmi Yük Davranışını İhmal Etmek
```
Problem: Tüm hesaplamaları nominal kapasitede yapmak
Etki: Gerçek işletmede verimler farklı (kısmi yükte %5-15 düşük)
Çözüm: Yıllık ortalama yük faktörü kullan veya saatlik simülasyon
```

### Hata 6: Bileşen Etkileşimlerini İhmal Etmek
```
Problem: Her ekipmanı bağımsız optimize etmek
Etki: Bir ekipmanın iyileştirilmesi diğerini kötüleştirebilir
Çözüm: Fabrika seviyesinde bütünleşik optimizasyon
```

### Hata 7: Aşırı Hassasiyetle Çalışmak
```
Problem: %0.1 maliyet farkı için 20 iterasyon daha yapmak
Etki: Zaman kaybı, veri belirsizliği zaten %5-10
Çözüm: %1-2 yakınsama yeterli, duyarlılık analizi daha değerli
```

### Hata 8: Sonuçları Bağlamdan Kopartmak
```
Problem: "Optimal exergy verimi %34.2" demek
Etki: Karar verici bu sayıyı yorumlayamaz
Çözüm: Her zaman maliyet ile birlikte sun:
       "Exergy verimi %27→%34'e çıkarılarak yıllık 85.000 € tasarruf,
        42.000 € yatırım, 6 ay geri ödeme"
```

### Hata 9: Dinamik Etkileri Görmezden Gelmek
```
Problem: Statik optimizasyon sonucu, 8.760 saat sabit kabul etmek
Etki: Mevsimsel yük değişimleri optimal noktayı değiştirir
Çözüm: En az 2-3 tipik senaryo (kış/yaz/orta) ile kontrol
```

### Hata 10: Stratejik Bakış Eksikliği
```
Problem: 3 yıl SPP çıkan projeyi reddetmek, 15 yıl NPV bakmamak
Etki: Uzun vadeli fırsatlar kaçırılır
Çözüm: SPP yanında NPV ve IRR de sun; CBAM etkisini göster
```

---

## 7. Türkiye Spesifik Varsayılan Parametreler

Veri eksikliğinde kullanılabilecek varsayılan değerler:

| Parametre | Varsayılan | Aralık | Not |
|-----------|-----------|--------|-----|
| T₀ (referans ortam) | 20°C | 15-25°C | Mevsimsel ortalama |
| P₀ (referans ortam) | 1.013 bar | - | Deniz seviyesi |
| Doğalgaz fiyatı | 0.038 €/kWh | 0.030-0.050 | Sanayi, 2024 |
| Elektrik fiyatı (OG) | 0.11 €/kWh | 0.08-0.16 | Sanayi, 2024 |
| İskonto oranı (reel) | 8% | 6-12% | Türkiye endüstriyel |
| Ekonomik ömür | 15 yıl | 12-20 yıl | Ekipman bazlı |
| CRF (i=%8, n=15) | 0.1168 | - | Hesaplanan |
| Çalışma saati (sürekli) | 7,500 h/yıl | 5,000-8,500 | 3 vardiya |
| Çalışma saati (2 vardiya) | 5,500 h/yıl | 4,000-6,000 | - |
| Çalışma saati (1 vardiya) | 3,000 h/yıl | 2,000-4,000 | - |
| İ&B çarpanı (φ) | 1.06 | 1.04-1.12 | Ekipman bazlı |
| CEPCI (2024) | 810 | - | Tahmini |
| Türkiye çarpanı (yerli) | 0.85 | 0.75-0.95 | İşçilik ucuz |
| Türkiye çarpanı (ithal) | 1.10 | 1.00-1.20 | Gümrük + nakliye |
| Karbon fiyatı (CBAM, 2025) | 50 €/tCO₂ | 30-80 | Geçiş dönemi |
| Karbon fiyatı (CBAM, 2030) | 80 €/tCO₂ | 60-120 | Tam uygulama |
| CO₂ EF (doğalgaz) | 0.202 kgCO₂/kWh | - | IPCC |
| CO₂ EF (elektrik, şebeke) | 0.44 kgCO₂/kWh | 0.38-0.50 | TEİAŞ |

---

## 8. Raporlama Şablonu

### Yönetici Özeti (1 sayfa)

```
TERMOEKONOMIK OPTİMİZASYON RAPORU
[Fabrika Adı] - [Tarih]

MEVCUT DURUM:
  Toplam enerji maliyeti: ___ €/yıl
  Fabrika exergy verimi: ___%
  Toplam exergy yıkım maliyeti: ___ €/yıl

OPTİMİZASYON SONUÇLARI:
  Potansiyel tasarruf: ___ €/yıl (__% azalma)
  Gerekli yatırım: ___ €
  Basit geri ödeme: ___ yıl
  NPV (15 yıl): ___ €
  CO₂ azaltma: ___ ton/yıl

ÖNCELİK SIRALAMA:
  1. [Quick Win] ___ — ___€/yıl tasarruf, SPP ___ yıl
  2. [Quick Win] ___ — ___€/yıl tasarruf, SPP ___ yıl
  3. [Stratejik] ___ — ___€/yıl tasarruf, SPP ___ yıl

DİKKAT: Sonuçlar doğalgaz fiyatına %25 duyarlıdır.
        Karbon fiyatı 80€/t olursa ek ___€/yıl tasarruf.
```

---

## İlgili Dosyalar

- `overview.md` — Termoekonomik optimizasyon temelleri
- `iterative_method.md` — İteratif yöntem
- `sensitivity_analysis.md` — Duyarlılık analizi
- `objective_functions.md` — Maliyet bileşenleri
- `algorithms.md` — Algoritma seçimi
- `factory/data_collection.md` — Veri toplama rehberi
- `factory/methodology.md` — Analiz metodolojisi
- `factory/economic_analysis.md` — Ekonomik analiz
- `factory/reporting.md` — Raporlama şablonları

## Referanslar

- Bejan, A., Tsatsaronis, G., & Moran, M. (1996). *Thermal Design and Optimization*. Wiley.
- ISO 50001:2018 — Energy Management Systems.
- ASHRAE Handbook — HVAC Systems and Equipment.
- EPDK, Enerji piyasası tarifeleri.
- Türkiye Enerji Verimliliği Strateji Belgesi (2012/1).
