# Economizer — Baca Gazı Isı Geri Kazanımı (Flue Gas Heat Recovery)

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Kazanlarda baca gazı yüksek sıcaklıkta (180-300°C) bacadan atmosfere atılmaktadır. Bu durum toplam yakıt enerjisinin %8-15'inin kayıp olarak atılması anlamına gelir. Özellikle doğal gaz yakıtlı kazanlarda baca gazı sıcaklığı genellikle 200-250°C aralığındadır ve bu ısının büyük kısmı geri kazanılabilir.

**Çözüm:** Economizer (ekonomizör) ile baca gazı ısısını kazan besleme suyuna (feedwater) transfer ederek baca gazı sıcaklığını düşürmek. Economizer, kazan çıkışındaki baca gazı yoluna yerleştirilen bir ısı eşanjörüdür ve besleme suyunu ön ısıtarak kazan verimini artırır.

**Tipik Tasarruf:** %4-8 (yakıt tüketiminde azalma)
**Tipik ROI:** 1-3 yıl

## Çalışma Prensibi

Economizer, baca gazındaki atık ısıyı besleme suyuna aktaran bir karşı akışlı (counter-flow) ısı eşanjörüdür:

- **Kanatlı boru tasarımı (Finned tube heat exchanger):** Baca gazı tarafındaki düşük ısı transfer katsayısını telafi etmek için kanatçıklı borular kullanılır
- **Besleme suyu ön ısıtma:** Degazörden veya kondensat tankından gelen besleme suyu (80-105°C) kazana girmeden önce economizer'da ısıtılır (tipik olarak 115-140°C'ye)
- **Verimlilik kuralı:** Baca gazı sıcaklığındaki her 20°C düşüş, kazan veriminde yaklaşık %1 artış sağlar
- **Konumlandırma:** Economizer, kazan çıkışında baca gazı kanalına yerleştirilir; besleme suyu karşı akış yönünde akar
- **Yoğuşmalı (condensing) vs yoğuşmasız (non-condensing):** Baca gazı sıcaklığı asit çiğ noktasının (acid dew point) altına düşürülürse yoğuşma meydana gelir; bu durumda korozyona dayanıklı malzeme gereklidir ancak ek ısı geri kazanımı sağlanır

### Verimlilik İlişkisi

| Parametre | İlişki |
|-----------|--------|
| Baca gazı sıcaklık düşüşü (ΔT) | Her 20°C → ~%1 verim artışı |
| Besleme suyu sıcaklık artışı | ΔT_su = (ṁ_gaz × Cp_gaz × ΔT_gaz) / (ṁ_su × Cp_su) |
| Geri kazanılan ısı (Q) | Q = ṁ_gaz × Cp_gaz × (T_giriş - T_çıkış) [kW] |
| Kazan verimi artışı | η_artış ≈ Q_gerikazanım / Q_yakıt × 100 [%] |

## Tasarım Kriterleri

### Pinch Point Sıcaklığı (Minimum Yaklaşım Sıcaklığı)

Economizer tasarımında baca gazı çıkış sıcaklığı ile besleme suyu giriş sıcaklığı arasındaki minimum sıcaklık farkıdır:
- **Yoğuşmasız economizer:** Minimum 20-30°C pinch point
- **Yoğuşmalı economizer:** Pinch point 5-15°C'ye kadar düşürülebilir
- Pinch point düştükçe ısı transfer yüzeyi ve maliyet artar

### Yaklaşım Sıcaklığı (Approach Temperature)

Baca gazı giriş sıcaklığı ile besleme suyu çıkış sıcaklığı arasındaki fark. Besleme suyu çıkış sıcaklığı, kazan doyma sıcaklığının en az 10-15°C altında kalmalıdır; aksi halde buhar oluşumu ve su çekici (water hammer) riski doğar.

### Asit Çiğ Noktası (Acid Dew Point)

Baca gazındaki SO₃ ve su buharının birleşerek sülfürik asit (H₂SO₄) oluşturduğu sıcaklıktır:

| Yakıt Türü | Asit Çiğ Noktası | Su Çiğ Noktası | Önerilen Min. Baca Gazı Çıkış Sıcaklığı |
|-------------|-------------------|----------------|------------------------------------------|
| Doğal gaz | Yok (kükürt yok) | ~57°C | 65-80°C (yoğuşmasız), 30-40°C (yoğuşmalı) |
| LPG | Yok (kükürt yok) | ~55°C | 65-80°C (yoğuşmasız), 30-40°C (yoğuşmalı) |
| Fuel oil (No.6) | 130-150°C | ~50°C | 160-180°C |
| Fuel oil (No.2/Dizel) | 110-130°C | ~48°C | 140-160°C |
| Kömür (düşük kükürt) | 120-140°C | ~50°C | 150-170°C |
| Kömür (yüksek kükürt) | 140-165°C | ~55°C | 170-190°C |

### Malzeme Seçimi

| Çalışma Koşulu | Malzeme | Açıklama |
|----------------|---------|----------|
| Yoğuşmasız (T > asit çiğ noktası) | Karbon çelik (Carbon steel) | Ekonomik, standart uygulama |
| Yoğuşmalı - doğal gaz | Paslanmaz çelik (AISI 316L) | Asidik kondensata dayanıklı |
| Yoğuşmalı - doğal gaz (premium) | Teflon kaplı veya Cor-Ten çelik | Uzun ömür, düşük bakım |
| Yoğuşmalı - fuel oil | Cam kaplı veya polimer borular | Sülfürik asit korozyonuna dayanıklı |

## Yoğuşmalı vs Yoğuşmasız Economizer Karşılaştırması

| Faktör | Yoğuşmasız Economizer | Yoğuşmalı Economizer |
|--------|----------------------|---------------------|
| Baca gazı çıkış sıcaklığı | 120-180°C | 30-55°C |
| Verimlilik artışı | %3-5 | %8-12 |
| Uygun yakıtlar | Tüm yakıtlar | Doğal gaz, LPG (düşük kükürtlü) |
| Malzeme | Karbon çelik | Paslanmaz çelik / Polimer |
| Yatırım maliyeti | Düşük-orta | Yüksek (1.5-2.5× yoğuşmasız) |
| Kondensat yönetimi | Gerekli değil | Nötralizasyon tankı, drenaj gerekli |
| Bakım | Düşük | Orta (kondensat sistemi) |
| Geri ödeme süresi | 1-2 yıl | 2-4 yıl |
| Latent ısı geri kazanımı | Hayır | Evet (su buharının yoğuşma ısısı) |
| Kazan verimi (üst ısıl değer) | %85-90 | %95-99 |

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı
- Baca gazı sıcaklığı 180°C'nin üzerindeyse (doğal gaz yakıtlı kazanlar)
- Baca gazı sıcaklığı 200°C'nin üzerindeyse (fuel oil / kömür yakıtlı kazanlar)
- Kazan yıllık çalışma süresi >4,000 saat ise
- Kazan kapasitesi >500 kW ise (küçük kazanlarda maliyet/fayda dengesizliği)
- Besleme suyu sıcaklığı baca gazı sıcaklığından en az 50°C düşükse
- Doğal gaz fiyatı yüksek olan bölgelerde
- Sürekli veya yarı-sürekli çalışan proses kazanlarında

### Ne Zaman Uygulanmamalı
- Baca gazı sıcaklığı zaten düşükse (<150°C doğal gaz, <200°C fuel oil)
- Kazanın mevcut verimi zaten yüksekse (>%92 üst ısıl değere göre)
- Yıllık çalışma süresi düşükse (<2,000 saat/yıl)
- Baca gazı kanalında yeterli alan yoksa
- Yüksek kükürtlü yakıt kullanılıyor ve yoğuşma riski yönetilemiyorsa
- Kazan kısa vadede (2-3 yıl) değiştirilecekse
- Besleme suyu sıcaklığı zaten yüksekse (>120°C, dar ΔT)

## Yatırım Maliyeti

| Kazan Kapasitesi | Economizer Maliyeti (Yoğuşmasız) | Economizer Maliyeti (Yoğuşmalı) | Not |
|-----------------|----------------------------------|--------------------------------|-----|
| 500 kW | €5,000-10,000 | €8,000-16,000 | Küçük ölçek, kompakt tasarım |
| 1 MW | €8,000-18,000 | €14,000-30,000 | Orta ölçek endüstriyel |
| 3 MW | €15,000-35,000 | €28,000-60,000 | Standart endüstriyel uygulama |
| 5 MW | €25,000-50,000 | €45,000-90,000 | Büyük endüstriyel |
| 10 MW | €40,000-80,000 | €70,000-140,000 | Büyük tesis, özel tasarım |
| 20 MW | €70,000-140,000 | €120,000-250,000 | Çok büyük tesis |

**Not:** Maliyetler montaj, baca gazı kanalı modifikasyonu, boru tesisatı ve devreye alma dahildir. Yoğuşmalı economizer maliyetine kondensat nötralizasyon sistemi dahildir.

## ROI Hesabı

### Formül
```
Baca_gazı_sıcaklık_düşüşü = T_giriş - T_çıkış [°C]
Verimlilik_artışı ≈ (T_giriş - T_çıkış) / 20 × 1 [%]
Yıllık_yakıt_tüketimi = Kazan_kapasitesi × Çalışma_saati × Ortalama_yük / (Mevcut_verim / 100) [kWh]
Yıllık_yakıt_maliyeti = Yıllık_yakıt_tüketimi × Yakıt_fiyatı [€]
Yıllık_yakıt_tasarrufu = Yıllık_yakıt_maliyeti × Verimlilik_artışı / 100 [€]
Geri_ödeme_süresi = Yatırım / Yıllık_yakıt_tasarrufu [yıl]
```

Burada:
- `T_giriş`: Economizer öncesi baca gazı sıcaklığı [°C]
- `T_çıkış`: Economizer sonrası baca gazı sıcaklığı [°C]
- `Kazan_kapasitesi`: Kazan nominal kapasitesi [kW]
- `Çalışma_saati`: Yıllık çalışma süresi [saat/yıl]
- `Ortalama_yük`: Ortalama yük oranı (0-1 arası)
- `Mevcut_verim`: Kazan mevcut verimi [%]
- `Yakıt_fiyatı`: Birim yakıt fiyatı [€/kWh]

### Örnek Hesap
- 5 MW doğal gaz yakıtlı kazan, 6,000 saat/yıl, ortalama %75 yük
- Baca gazı sıcaklığı: 220°C → Economizer sonrası: 130°C
- Mevcut kazan verimi: %87 (alt ısıl değere göre)
- Doğal gaz fiyatı: €0.045/kWh

```
Baca_gazı_sıcaklık_düşüşü = 220 - 130 = 90°C
Verimlilik_artışı = 90 / 20 × 1 = %4.5
Yıllık_yakıt_tüketimi = 5,000 × 6,000 × 0.75 / 0.87 = 25,862,069 kWh
Yıllık_yakıt_maliyeti = 25,862,069 × 0.045 = €1,163,793
Yıllık_yakıt_tasarrufu = 1,163,793 × 4.5 / 100 = €52,371/yıl
```

- Yoğuşmasız economizer yatırım maliyeti: €40,000
- **Geri ödeme süresi: 40,000 / 52,371 = 0.76 yıl**

**Not:** Bu örnekte geri ödeme süresi 1 yılın altındadır; bu, 5 MW üzeri kazanlarda economizer yatırımının son derece cazip olduğunu göstermektedir.

## Uygulama Adımları

1. **Baca gazı analizi:** Mevcut baca gazı sıcaklığı, debisi ve bileşimini ölç (O₂, CO₂, CO, SO₂). Yakıt kükürt içeriğini belirle
2. **Besleme suyu analizi:** Besleme suyu sıcaklığı, debisi ve su kalitesini belirle. Degazör/kondensat tankı çıkış sıcaklığını kaydet
3. **Economizer tipi seçimi:** Yakıt türüne ve hedef baca gazı çıkış sıcaklığına göre yoğuşmalı veya yoğuşmasız economizer kararını ver
4. **Termal tasarım:** Pinch point, yaklaşım sıcaklığı, ısı transfer yüzeyi hesaplarını yap. LMTD (Log Mean Temperature Difference) yöntemi ile boyutlandır
5. **Malzeme seçimi:** Korozyon riski analizine göre boru ve kanatçık malzemesini belirle
6. **Mekanik tasarım:** Baca gazı kanalında basınç kaybını (draft loss) hesapla. Gerekirse indüklü çekiş fanı (induced draft fan) güçlendirmesini planla
7. **Alan ve yerleşim planı:** Economizer için gerekli alanı belirle, baca gazı kanalı modifikasyonunu planla. Bakım erişimi için yeterli alan bırak
8. **Tedarik ve montaj:** Economizer ünitesini, boru tesisatını, kontrol vanalarını ve enstrümantasyonu (sıcaklık, basınç sensörleri) temin et ve monte et
9. **Kondensat yönetimi (yoğuşmalı tip):** Kondensat toplama, nötralizasyon tankı ve drenaj sistemi kur
10. **Devreye alma:** By-pass damperini test et, besleme suyu debi kontrolünü ayarla. Sıcaklık sensörlerini kalibre et
11. **Performans doğrulama:** Devreye alma sonrası en az 1 haftalık veri toplayarak tasarruf hesabını doğrula. Baca gazı çıkış sıcaklığını ve verim artışını kaydet

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Asit korozyonu (Acid corrosion) | Baca gazı sıcaklığı asit çiğ noktasının altına düşerse sülfürik asit yoğuşması oluşur | Minimum baca gazı çıkış sıcaklığını asit çiğ noktasının 15-20°C üzerinde tut; yakıt türüne uygun malzeme seç |
| Kirlenme / Fouling | Baca gazındaki kurum, kül ve partiküller economizer yüzeyinde birikerek ısı transferini düşürür | Kurum üfleme (soot blowing) sistemi kur; düzenli temizlik programı uygula; kanatçık aralığını yeterli tut |
| Yoğuşma (Condensation) | Düşük yüklerde veya düşük besleme suyu sıcaklığında beklenmedik yoğuşma | Besleme suyu giriş sıcaklığını minimum 60°C tut; düşük yükte by-pass damperini devreye al |
| Alan kısıtı (Space limitation) | Mevcut baca gazı kanalında economizer için yeterli alan bulunamayabilir | Erken aşamada saha ölçümü yap; gerekirse dış mekan montajı veya kompakt tasarım kullan |
| Geri basınç (Backpressure) | Economizer baca gazı tarafında 2-5 mbar ek basınç kaybı yaratır | Mevcut baca çekişini kontrol et; gerekirse indüklü çekiş fanını güçlendir veya yenile |
| Su çekici (Water hammer) | Besleme suyu buharlaşırsa boru hattında ani basınç darbesi oluşabilir | Besleme suyu çıkış sıcaklığını doyma sıcaklığının en az 10-15°C altında tut |
| Düşük yükte performans düşüşü | Düşük yükte baca gazı debisi ve sıcaklığı azalır, economizer verimi düşer | By-pass sistemi ile düşük yükte baca gazını yönlendir; modülasyon kontrolü uygula |
| Su kalitesi | Yetersiz su arıtma economizer iç yüzeylerinde kireçlenmeye yol açar | Besleme suyu kalitesini standartlara uygun tut (TDS, sertlik, pH kontrolü) |

## İlgili Dosyalar
- Kazan benchmarkları: `benchmarks/boiler_benchmarks.md`
- Kazan ekipman bilgisi: `equipment/boiler_steam.md`
- Baca gazı ısı kaybı formülleri: `formulas/boiler_exergy.md`
- Kazan bakım optimizasyonu: `solutions/boiler_maintenance.md`
- Kazan yoğuşma ısı geri kazanımı: `solutions/boiler_condensate_recovery.md`

## Referanslar
- ASME PTC 4, "Fired Steam Generators — Performance Test Codes"
- DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition
- CIBO (Council of Industrial Boiler Owners), "Energy Efficiency Handbook"
- Spirax Sarco, "The Steam and Condensate Loop" — Economizer Chapter
- Cleaver-Brooks, "Boiler Book — Economizer Selection and Application Guide"
- EN 12952-15, "Water-tube boilers and auxiliary installations — Acceptance tests"
- Babcock & Wilcox, "Steam: Its Generation and Use," 42nd Edition — Heat Recovery Systems
