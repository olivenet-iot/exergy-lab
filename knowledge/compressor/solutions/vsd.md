---
title: "Çözüm: VSD (Değişken Hızlı Sürücü) ile Kompresör Kontrolü"
category: solutions
equipment_type: compressor
keywords: [VSD, değişken hız, enerji tasarrufu, kompresör]
related_files: [compressor/formulas.md, compressor/benchmarks.md, compressor/equipment/screw.md]
use_when: ["Kompresöre VSD önerisi değerlendirilirken", "Değişken yük profili analiz edilirken"]
priority: high
last_updated: 2026-01-31
---
# Çözüm: VSD (Değişken Hızlı Sürücü) ile Kompresör Kontrolü

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Sabit hızlı kompresörler kısmi yükte load/unload kontrolü ile çalışır. Boşta bile %25-30 güç çekerler ve kısmi yükte spesifik güç tüketimleri dramatik şekilde artar.

**Çözüm:** VSD (Variable Speed Drive / Değişken Frekanslı Sürücü) ile motor hızını talebe göre ayarlayarak enerji tüketimini optimize etmek.

**Tipik Tasarruf:** %20-35 (değişken yük profilinde)
**Tipik ROI:** 1-3 yıl

## Çalışma Prensibi

VSD, gelen AC elektriği DC'ye çevirir, ardından değişken frekanslı AC'ye geri dönüştürür:
- **Frekans kontrolü:** 20-70 Hz aralığında (50 Hz sabit yerine)
- **Hız kontrolü:** Motor hızı frekansla doğru orantılı: `N = 120 × f / P_kutup`
- **Debi kontrolü:** Vidalı kompresörde debi hıza yaklaşık orantılıdır
- **Boşta çalışma eliminasyonu:** VSD kompresör yavaşlar, load/unload döngüsü gereksiz

## Affinity Laws (Benzerlik Yasaları)

| Parametre | İlişki |
|-----------|--------|
| Debi (Q) | Q ∝ N (hız) |
| Basınç (P) | P ∝ N² |
| Güç (W) | W ∝ N³ |

**Vidalı kompresör notu:** Affinity laws tam olarak santrifüj makinelere uygulanır. Pozitif deplasmanlı vidalı kompresörlerde:
- Debi-hız ilişkisi yaklaşık lineerdir
- Güç tasarrufu kübik yasadan biraz düşüktür
- %50 debi genelde ~%50-65 güç gerektirir (teorik %12.5 yerine)
- Yine de load/unload'a göre çok daha verimlidir

## Kısmi Yük Tasarruf Karşılaştırması

| Ort. Yük % | Load/Unload Güç % | VSD Güç % | VSD Tasarrufu |
|------------|-------------------|-----------|--------------|
| 100% | 100% | ~102% | -%2-3 (VSD kayıpları) |
| 80% | 83-90% | 78-82% | %5-10 |
| 60% | 72-80% | 58-65% | %15-22 |
| 50% | 68-75% | 48-55% | %20-30 |
| 40% | 63-72% | 40-48% | %25-35 |
| 30% | 60-68% | 32-40% | %30-40 |

## Uygulanabilirlik Kriterleri

### VSD Ne Zaman Uygulanmalı
- Yük profili %30-80 arasında değişiyorsa
- Boşta çalışma süresi toplam çalışmanın >%25'i ise
- Kısmi yükte güç tüketimi tam yükün >%60'ı ise
- Talep değişkenliği ortalamanın >%20'si ise
- Çok vardiyalı çalışma, değişken üretim desenleri

### VSD Ne Zaman Uygulanmamalı
- Sürekli tam yük (>%90): VSD elektroniği %2-3 kayıp ekler
- Çok küçük kompresörler (<4 kW): Maliyet/fayda dengesizliği
- Baz yük kompresörü olarak çalışan makineler (iyi sıralı çoklu sistemde)
- Pistonlu kompresörler: Düşük hızda yağlama ve mekanik gerilim sorunları
- Çok eski motorlar (IE1 öncesi): Motor uyumsuzluğu

## Retrofit vs Yeni VSD Kompresör

| Faktör | VSD Retrofit | Yeni VSD Kompresör |
|--------|-------------|-------------------|
| Yatırım maliyeti | Yeni ünitenin %30-50'si | Tam yeni ünite maliyeti |
| Motor uyumluluğu | İnvertör uyumlu motor gerekebilir | Fabrika eşleştirilmiş |
| Airend optimizasyonu | Sabit hız için optimize | Değişken hız için optimize |
| Hız aralığı (turndown) | %50-100 (sınırlı) | %20-100 (geniş) |
| Kısmi yük verimi | Best-in-class'tan %5-15 düşük | En iyi kısmi yük verimi |
| Garanti | Orijinal garanti bozulabilir | Tam üretici garantisi |
| Tavsiye edilen durum | Bütçe kısıtlı; kompresör <5 yaş | Kompresör yenileme zamanı |

## Yatırım Maliyeti

| Kompresör Gücü | VSD Retrofit | Yeni VSD Kompresör |
|----------------|-------------|-------------------|
| 7.5 kW | €3,000-5,000 | €12,000-18,000 |
| 15 kW | €4,000-7,000 | €18,000-28,000 |
| 22 kW | €5,000-9,000 | €25,000-38,000 |
| 37 kW | €7,000-12,000 | €35,000-55,000 |
| 55 kW | €10,000-16,000 | €50,000-75,000 |
| 75 kW | €12,000-20,000 | €65,000-95,000 |
| 110 kW | €18,000-28,000 | €90,000-130,000 |
| 160 kW | €22,000-35,000 | €120,000-170,000 |

## ROI Hesabı

### Formül
```
Yıllık_tasarruf_kWh = P_nominal × Çalışma_saati × (Güç%_LoadUnload - Güç%_VSD) / 100
Yıllık_tasarruf_EUR = Yıllık_tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Yıllık_tasarruf_EUR
```

### Örnek Hesap
- 55 kW kompresör, 6,000 saat/yıl, ortalama %60 yük
- Elektrik: €0.15/kWh
- Load/unload'da: ~%75 güç = 41.25 kW ortalama
- VSD ile: ~%60 güç = 33 kW ortalama
- Yıllık tasarruf: (41.25 - 33) × 6,000 = 49,500 kWh = €7,425/yıl
- VSD retrofit maliyeti: €14,000
- **Geri ödeme: 14,000 / 7,425 = 1.9 yıl**

## Sistem Tasarımı: Baz Yük + Trim

En iyi uygulama: Sabit hızlı + VSD kombinasyonu
- **Sabit hızlı kompresör(ler):** Sürekli baz yükü karşılar (%100 yükte en verimli)
- **VSD kompresör:** Değişken "trim" talebi karşılar (tüm yük aralığında verimli)

### Tasarım Kuralları
- VSD kapasitesi: Toplam sistem kapasitesinin %30-50'si
- VSD kompresör: Son yüklenen, ilk boşalan olmalı
- Master controller ile koordineli çalışma
- Aynı anda birden fazla kompresörün kısmi yükte çalışmasından kaçınılmalı

## Ürün Örnekleri

| Marka | Model | Özellik |
|-------|-------|---------|
| Atlas Copco | GA VSD+ | iPM motor, %55 daha küçük alan, %50 tasarruf iddiası, 7-315 kW |
| Kaeser | SFC serisi | Sigma Profile airend, 1:1 direkt tahrik, IE4 motor, 18.5-355 kW |
| Ingersoll Rand | R-Series VSD | Tek kademe veya çift kademe, V-Shield™ teknolojisi |
| Boge | S serisi VSD | Super Silenzio sessiz çalışma, kompakt tasarım |
| CompAir | L-Series RS | Değişken hız, enerji geri kazanım seçeneği |

## Uygulama Adımları

1. **Yük profili analizi:** Minimum 1 haftalık güç profilleme ile yük dağılımını belirle
2. **Karar:** Retrofit veya yeni VSD kompresör kararını ver
3. **Boyutlandırma:** VSD kompresör kapasitesini yük değişkenliğine göre belirle
4. **Elektrik altyapısı:** VSD için harmonik filtre, EMC uyumu, kablo boyutu kontrol
5. **Kurulum:** Mekanik ve elektrik bağlantıları
6. **Devreye alma:** Basınç setpoint, hız sınırları, rampa süreleri ayarla
7. **Doğrulama:** Kurulum sonrası 1 haftalık güç profilleme ile tasarrufu doğrula

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Harmonikler | VSD elektrik şebekesine harmonik bozulma yaratır | Harmonik filtre, IEEE 519 uyumu |
| Motor ısınması | Düşük hızda motor soğutması azalır | İnvertör uyumlu motor, ayrı fan |
| Yatak ömrü | Düşük hızda yağlama yetersizliği | Minimum hız sınırı (%20-25) |
| EMC | Elektromanyetik parazit | Ekranlı kablolar, uygun topraklama |
| Kondansasyon | Düşük hızda daha fazla nem | Yeterli kurutucu kapasitesi |

## İlgili Dosyalar
- Benchmark verileri: `benchmarks/compressor_benchmarks.md` (Bölüm 3: Kısmi Yük)
- Vidalı kompresör: `equipment/compressor_screw.md`
- Sistem tasarımı: `solutions/compressor_system_design.md`
- Exergy formülleri: `formulas/compressor_exergy.md`

## Referanslar
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- Compressed Air Challenge, "Best Practices for Compressed Air Systems"
- Atlas Copco, "Compressed Air Manual," 9th Edition — VSD Chapter
- Kaeser, "Compressed Air Engineering" — Sigma Frequency Control Documentation
- CAGI Performance Verification Data Sheets
