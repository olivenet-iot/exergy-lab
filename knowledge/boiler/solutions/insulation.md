# İzolasyon İyileştirme — Insulation Improvement

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Buhar kazanı sistemlerinde borular, vanalar, flanşlar ve bağlantı noktaları izolasyonsuz veya hasarlı izolasyonla çalışmaktadır. Çıplak yüzeylerden radyasyon ve konveksiyon yoluyla önemli miktarda ısı kaybı meydana gelir. Tipik bir tesiste izolasyonsuz yüzeylerin toplam ısı kaybına katkısı %5-10 arasındadır.

**Çözüm:** İzolasyonsuz veya bozulmuş izolasyona sahip boru hatları, vanalar, flanşlar ve ekipman yüzeylerinin uygun kalınlıkta ısı izolasyonu ile kaplanması. Sökülebilir izolasyon ceketleri (removable insulation jackets) ile bakım erişimi gerektiren noktalarda izolasyon sağlanması.

**Tipik Tasarruf:** %1-3 toplam yakıt tüketimi
**Tipik ROI:** 0.5-1.5 yıl

## Çalışma Prensibi

Buhar sistemlerinde yüksek sıcaklıktaki yüzeyler çevre havası ile temas ettiğinde iki temel mekanizma ile ısı kaybı oluşur:

- **Radyasyon (Işınım):** Sıcak yüzey, Stefan-Boltzmann yasasına göre elektromanyetik dalga yayarak enerji kaybeder. Kayıp, yüzey sıcaklığının dördüncü kuvvetiyle orantılıdır.
- **Konveksiyon (Taşınım):** Sıcak yüzey çevresindeki hava ısınarak yükselir ve doğal konveksiyon akımı oluşturur. Bu sürekli hava sirkülasyonu ile ısı transferi gerçekleşir.

İzolasyon malzemesi, düşük ısı iletkenliği (thermal conductivity) sayesinde yüzey ile ortam arasında termal bir bariyer oluşturur. İyi bir izolasyon:
- Dış yüzey sıcaklığını 50-60°C'nin altına düşürür (personel güvenliği sınırı)
- Isı kaybını %90-95 oranında azaltır
- Buhar kalitesinin korunmasına yardımcı olur (hat boyunca kondens miktarını düşürür)
- Proses sıcaklık stabilitesini artırır

## Yüzey Sıcaklığı ve Isı Kaybı

Aşağıdaki tablo, DN100 (4") çıplak çelik boru için farklı buhar basınçlarında metre başına ısı kaybını gösterir. Ortam sıcaklığı 20°C, rüzgarsız ortam (doğal konveksiyon) kabul edilmiştir.

| Buhar Basıncı (barg) | Doyma Sıcaklığı (°C) | Yüzey Sıcaklığı (°C) | Isı Kaybı — Çıplak (W/m) | Isı Kaybı — İzole (W/m) | Tasarruf (%) |
|----------------------|----------------------|----------------------|--------------------------|--------------------------|-------------|
| 2 | 134 | ~130 | 290 | 25 | 91% |
| 5 | 159 | ~155 | 410 | 32 | 92% |
| 8 | 175 | ~170 | 510 | 37 | 93% |
| 10 | 184 | ~180 | 570 | 40 | 93% |
| 15 | 201 | ~196 | 680 | 46 | 93% |
| 20 | 215 | ~210 | 790 | 51 | 94% |
| 30 | 236 | ~230 | 960 | 60 | 94% |
| 40 | 252 | ~246 | 1,120 | 68 | 94% |

**Not:** İzole değerler 50 mm mineral yün izolasyon (λ = 0.040 W/m·K) için hesaplanmıştır. Gerçek değerler boru çapı, izolasyon kalınlığı ve ortam koşullarına göre değişir.

## Radyasyon ve Konveksiyon Kaybı Formülü

Çıplak yüzeyden toplam ısı kaybı, konveksiyon ve radyasyon bileşenlerinin toplamıdır:

```
Q_loss = h × A × (T_surface - T_ambient) + ε × σ × A × (T_surface⁴ - T_ambient⁴)

Burada:
  Q_loss     = Toplam ısı kaybı [W]
  h          = Konvektif ısı transfer katsayısı [W/m²·K]
               (doğal konveksiyon yatay boru: 5-15 W/m²·K)
  A          = Yüzey alanı [m²]
  T_surface  = Yüzey sıcaklığı [K]
  T_ambient  = Ortam sıcaklığı [K]
  ε          = Yüzey yayma katsayısı (emisivite) [-]
               (oksitli çelik: 0.7-0.9, parlak alüminyum: 0.05-0.1)
  σ          = Stefan-Boltzmann sabiti = 5.67 × 10⁻⁸ [W/m²·K⁴]
```

### Pratik Kullanım için Basitleştirilmiş Formül

Enerji denetimlerinde ve hızlı hesaplamalarda aşağıdaki basitleştirilmiş formül kullanılır:

```
Q_loss_basit = C × (T_surface - T_ambient)^1.25 × A

Burada:
  C = Ampirik katsayı ≈ 10 W/m² (yatay boru, doğal konveksiyon, oksitli çelik)
  T_surface, T_ambient = °C cinsinden sıcaklıklar
  A = Yüzey alanı [m²]
```

### Boru Yüzey Alanı Hesabı

```
A_boru = π × D_dış × L

Burada:
  D_dış = Borunun dış çapı [m]
  L     = Boru uzunluğu [m]

Örnek: DN100 (D_dış = 0.1143 m), 50 m uzunluk
  A = 3.14159 × 0.1143 × 50 = 17.95 m²
```

## İzolasyon Malzemesi Karşılaştırması

| Özellik | Mineral Yün (Taş Yünü) | Kalsiyum Silikat | Cam Köpük (Foam Glass) | Aerojel |
|---------|------------------------|-----------------|----------------------|---------|
| Isı İletkenliği (W/m·K) @200°C | 0.045-0.055 | 0.065-0.080 | 0.050-0.065 | 0.020-0.025 |
| Maks. Kullanım Sıcaklığı (°C) | 700 | 1000 | 480 | 650 |
| Yoğunluk (kg/m³) | 80-150 | 200-350 | 120-170 | 120-200 |
| Nem Direnci | Düşük (hidrofobik kaplı: Orta) | Orta | Çok Yüksek | Yüksek |
| Basma Dayanımı | Düşük | Yüksek | Çok Yüksek | Düşük |
| Tipik Fiyat (€/m², 50mm) | 15-30 | 35-60 | 50-80 | 150-300 |
| Avantaj | Ekonomik, yaygın, kolay uygulama | Mekanik dayanım, yüksek sıcaklık | Su geçirmez, kimyasal dayanım | Ultra ince, en düşük iletkenlik |
| Dezavantaj | Nem hassasiyeti, ezilme | Ağır, kırılgan | Pahalı, kırılgan | Çok pahalı |
| Tipik Kullanım Alanı | Genel amaçlı boru izolasyonu | Yüksek sıcaklık, mekanik yük | Soğutma sistemleri, yer altı | Alan kısıtlı alanlar, yüksek performans |

**Seçim Kriteri:** Buhar sistemlerinde en yaygın ve ekonomik çözüm **mineral yün** (taş yünü) izolasyondur. Alüminyum kaplı (cladding) uygulanarak nem koruması ve mekanik dayanımı artırılır.

## Çıplak Flanş ve Vana İzolasyonu

Buhar sistemlerinde flanşlar ve vanalar bakım/sökme ihtiyacı nedeniyle genellikle izolasyonsuz bırakılır. Ancak bu noktalar toplam izolasyonsuz yüzeyin büyük bir bölümünü oluşturur.

### Flanş ve Vana Isı Kaybı Eşdeğeri

| Bileşen | DN50 | DN100 | DN150 | DN200 | DN300 |
|---------|------|-------|-------|-------|-------|
| Çıplak flanş çifti (eşdeğer boru uzunluğu, m) | 0.5 | 1.0 | 1.5 | 2.0 | 3.0 |
| Çıplak sürgülü vana (eşdeğer boru uzunluğu, m) | 0.8 | 1.5 | 2.2 | 3.0 | 4.5 |
| Çıplak kontrol vanası (eşdeğer boru uzunluğu, m) | 1.0 | 2.0 | 3.0 | 4.0 | 6.0 |
| Çıplak buhar kapanı (eşdeğer boru uzunluğu, m) | 0.6 | 1.2 | 1.8 | 2.5 | 3.5 |

### Sökülebilir İzolasyon Ceketleri (Removable Insulation Jackets)

Sökülebilir izolasyon ceketleri, flanş ve vanalar için ideal çözümdür:

- **Malzeme:** İç katman yüksek sıcaklık silikon kumaş + mineral yün dolgu + dış katman su geçirmez kumaş
- **Bağlama:** Paslanmaz çelik tokalı kayışlar veya Velcro bantlar
- **Sökme/takma süresi:** 1-5 dakika (bakım erişimi)
- **Ömür:** 5-10 yıl (tekrar tekrar kullanılabilir)
- **Isı kaybı azaltma:** %85-95

### Sökülebilir Ceket Maliyeti

| Bileşen Boyutu | Flanş Ceketi (€/adet) | Vana Ceketi (€/adet) |
|----------------|----------------------|---------------------|
| DN50 | 80-150 | 120-200 |
| DN100 | 120-220 | 180-320 |
| DN150 | 180-320 | 280-480 |
| DN200 | 250-420 | 380-650 |
| DN300 | 350-600 | 520-900 |

## Ekonomik Kalınlık Optimizasyonu (Economic Thickness)

İzolasyon kalınlığı arttıkça ısı kaybı azalır ancak izolasyon maliyeti artar. **Ekonomik kalınlık**, toplam maliyetin (izolasyon yatırımı + ısı kaybı maliyeti) minimum olduğu noktadır.

```
Toplam_maliyet = İzolasyon_yatırımı(t) + Σ [Isı_kaybı(t) × Enerji_fiyatı × Çalışma_saati] / (1+r)^n

Burada:
  t = İzolasyon kalınlığı [mm]
  r = İskonto oranı [%]
  n = Değerlendirme süresi [yıl]
```

### Pratik Ekonomik Kalınlık Değerleri (Mineral Yün)

| Boru Çapı | 5 barg (159°C) | 10 barg (184°C) | 20 barg (215°C) | 40 barg (252°C) |
|-----------|---------------|-----------------|-----------------|-----------------|
| DN25 | 40 mm | 50 mm | 60 mm | 80 mm |
| DN50 | 50 mm | 60 mm | 70 mm | 90 mm |
| DN100 | 60 mm | 70 mm | 80 mm | 100 mm |
| DN150 | 60 mm | 80 mm | 90 mm | 110 mm |
| DN200 | 70 mm | 80 mm | 100 mm | 120 mm |
| DN300 | 80 mm | 90 mm | 110 mm | 130 mm |

**Not:** Değerler €0.06/kWh doğalgaz fiyatı, 8,000 saat/yıl çalışma ve 15 yıl değerlendirme süresi için hesaplanmıştır.

## Uygulanabilirlik Kriterleri

### İzolasyon İyileştirme Ne Zaman Uygulanmalı
- Yüzey sıcaklığı >50°C olan izolasyonsuz boru, vana veya flanş varsa
- Mevcut izolasyon hasarlı, ezilmiş, ıslanmış veya çökmiş ise
- Alüminyum kaplama (cladding) yırtılmış, nemli izolasyon açığa çıkmış ise
- Termografik taramada (kızılötesi kamera) sıcak noktalar (hot spots) tespit edilmiş ise
- Kondens hatlarında aşırı kondens oluşumu gözleniyorsa (izolasyon yetersizliği belirtisi)

### İzolasyon Ne Zaman Uygulanmamalı
- Kasıtlı ısı yayma gerektiren yüzeyler (bazı proses radyatörleri)
- Çok kısa süreli (<500 saat/yıl) çalışan hatlar (maliyet/fayda dengesizliği)
- Korozyon altında izolasyon (CUI) riski yüksek ve önlem alınamayan yüzeyler

## Yatırım Maliyeti

| Uygulama Türü | Birim Maliyet | Açıklama |
|---------------|--------------|----------|
| Mineral yün boru izolasyonu (malzeme + işçilik) | €25-60/m (DN50-DN200) | Alüminyum kaplama dahil |
| Sökülebilir flanş ceketi | €80-600/adet | Boyuta göre değişir |
| Sökülebilir vana ceketi | €120-900/adet | Boyuta göre değişir |
| Mevcut izolasyon tamiri/değişimi | €15-40/m | Kısmi hasar durumu |
| Kazan gövde izolasyonu yenileme | €3,000-15,000/kazan | Kazan kapasitesine göre |
| Termografik tarama (tesis geneli) | €1,000-3,000 | İlk tespit aşaması |

### Tipik Tesis Yatırım Özeti

| Tesis Ölçeği | İzolasyonsuz Yüzey (m²) | Tahmini Yatırım (€) | Yıllık Tasarruf (€/yıl) |
|-------------|------------------------|---------------------|------------------------|
| Küçük (<5 ton/saat buhar) | 10-30 | 3,000-10,000 | 4,000-15,000 |
| Orta (5-20 ton/saat buhar) | 30-100 | 10,000-40,000 | 15,000-60,000 |
| Büyük (>20 ton/saat buhar) | 100-500 | 40,000-150,000 | 60,000-250,000 |

## ROI Hesabı

### Formül

```
Isı_kaybı_çıplak (kW) = Q_basit × A_toplam / 1000
Isı_kaybı_izole (kW) = Isı_kaybı_çıplak × (1 - η_izolasyon)
Tasarruf_kW = Isı_kaybı_çıplak - Isı_kaybı_izole

Yıllık_tasarruf_kWh = Tasarruf_kW × Çalışma_saati
Yıllık_yakıt_tasarrufu_EUR = Yıllık_tasarruf_kWh / η_kazan × Yakıt_fiyatı
Geri_ödeme_yıl = Toplam_yatırım / Yıllık_yakıt_tasarrufu_EUR
```

### Örnek Hesap

**Senaryo:** Bir fabrikada 10 barg buhar hattında 80 m uzunluğunda DN100 çıplak boru, 12 adet çıplak flanş ve 6 adet çıplak vana tespit edilmiştir.

```
Adım 1: Çıplak boru ısı kaybı
  Q_boru = 570 W/m × 80 m = 45,600 W = 45.6 kW

Adım 2: Flanş ve vana ısı kaybı (eşdeğer boru uzunluğu)
  Flanş: 12 × 1.0 m = 12 m eşdeğer → 570 × 12 = 6,840 W = 6.84 kW
  Vana:  6 × 1.5 m = 9 m eşdeğer  → 570 × 9  = 5,130 W = 5.13 kW

Adım 3: Toplam ısı kaybı
  Q_toplam = 45.6 + 6.84 + 5.13 = 57.57 kW

Adım 4: İzolasyon sonrası kayıp (%93 azalma)
  Q_izole = 57.57 × 0.07 = 4.03 kW
  Tasarruf = 57.57 - 4.03 = 53.54 kW

Adım 5: Yıllık tasarruf (8,000 saat/yıl, kazan verimi %88, doğalgaz €0.06/kWh)
  Yıllık_kWh = 53.54 × 8,000 = 428,320 kWh
  Yakıt_maliyeti = 428,320 / 0.88 × 0.06 = €29,204/yıl

Adım 6: Yatırım
  Boru izolasyonu: 80 m × €45/m = €3,600
  Flanş ceketleri: 12 × €150/adet = €1,800
  Vana ceketleri:  6 × €250/adet = €1,500
  Toplam yatırım = €6,900

Adım 7: Geri ödeme
  ROI = 6,900 / 29,204 = 0.24 yıl ≈ 3 ay
```

**Sonuç:** Bu uygulama son derece kısa geri ödeme süresine sahip, yüksek öncelikli bir enerji verimliliği projesidir.

## Uygulama Adımları

1. **Termografik tarama:** Kızılötesi kamera ile tüm buhar hatlarının, vanaların, flanşların ve ekipmanların taranması. Sıcak noktaların fotoğraflanması ve konumlarının harita üzerinde işaretlenmesi.
2. **Envanter çıkarma:** İzolasyonsuz ve hasarlı izolasyonlu yüzeylerin listesi (boru çapı, uzunluk, bileşen tipi, buhar basıncı, yüzey sıcaklığı).
3. **Isı kaybı hesabı:** Her bir yüzey için ısı kaybı hesaplanması, toplam kaybın ve potansiyel tasarrufun belirlenmesi.
4. **Ekonomik kalınlık belirleme:** Buhar basıncı ve boru çapına göre optimum izolasyon kalınlığının seçilmesi.
5. **Malzeme seçimi:** Çalışma sıcaklığı, ortam koşulları ve bütçeye göre izolasyon malzemesinin belirlenmesi (genellikle mineral yün + alüminyum kaplama).
6. **Tedarik ve teklif:** Minimum 3 izolasyon firmasından detaylı teklif alınması. Sökülebilir ceketler için özel ölçü alımı.
7. **Uygulama:** İzolasyonun montajı. Boru izolasyonunda dikişlerin alt tarafa gelmemesi, alüminyum kaplamanın üst üste binme yönünün yağmur suyu akışına uygun olması sağlanmalı.
8. **Kalite kontrol:** Kurulum sonrası termografik tarama ile izolasyon kalitesinin doğrulanması, soğuk köprü (thermal bridge) noktalarının tespit edilmesi.
9. **Periyodik bakım programı:** Yılda bir termografik tarama ile izolasyon durumunun takibi, hasarlı bölgelerin onarımı.

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| İzolasyon altı korozyon (CUI) | Nem izolasyon altına girerse boru yüzeyinde korozyon oluşur | Su geçirmez kaplama (cladding), buhar bariyeri, periyodik kontrol |
| Yanlış malzeme seçimi | Çalışma sıcaklığını aşan malzeme erken bozulur | Maks. sıcaklık değerlerine uygun malzeme seçimi |
| Yetersiz kalınlık | Ekonomik kalınlığın altında uygulama, optimum tasarruf sağlamaz | Ekonomik kalınlık hesabı yapılması |
| Mekanik hasar | Trafik, bakım çalışmaları ile izolasyon ezilmesi | Alüminyum kaplama, koruyucu kafes, dikkat işareti |
| Islanmış izolasyon | Isı iletkenliği 3-5 kat artarak izolasyonu etkisiz kılar | Hasar gören izolasyonun derhal değiştirilmesi |
| Flanş/vana erişimi | Sabit izolasyon bakım erişimini engeller | Sökülebilir ceketler kullanılması |
| Asbest içerikli eski izolasyon | Eski tesislerde asbest izolasyon sağlık riski taşır | Uzman firma ile asbest sökümü, yasal prosedür |
| Personel güvenliği | İzolasyonsuz yüzeylerde yanık riski (>60°C) | İzolasyon önceliği: personel erişimi olan alanlar |

## İlgili Dosyalar

- Kazan ekipmanı: `equipment/boiler_firetube.md`
- Buhar dağıtım sistemi: `equipment/steam_distribution.md`
- Kondens sistemi: `equipment/condensate_return.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Exergy formülleri: `formulas/boiler_exergy.md`
- Buhar kapanı bakımı: `solutions/boiler_steam_trap.md`
- Ekonomizer: `solutions/boiler_economizer.md`

## Referanslar

- EIEI / Yenilenebilir Enerji Genel Müdürlüğü, "Sanayide Enerji Verimliliği Rehberi"
- BS 5970:2012, "Thermal insulation of pipework, ductwork, associated equipment and other industrial installations"
- ASTM C585, "Standard Practice for Inner and Outer Diameters of Thermal Insulation for Nominal Sizes of Pipe and Tubing"
- VDI 2055, "Thermal insulation for heated and refrigerated industrial and domestic installations"
- DOE/AMO, "Steam System Best Practices — Insulate Steam Distribution and Condensate Return Lines"
- 3EPlus (DOE), "Insulation Thickness Computer Program" — ekonomik kalınlık hesap aracı
- CINI (Committee for Industrial Insulation), "Insulation Standards for Industrial Installations"
- Türkiye Enerji Verimliliği Derneği (ENVER), "Buhar Sistemlerinde Enerji Verimliliği"
