# Kondensat Geri Dönüşü — Condensate Return

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Buhar sistemlerinde kondensat (yoğuşma suyu) 80-95°C sıcaklıkta önemli miktarda enerji içermesine rağmen, birçok tesiste kanalizasyona deşarj edilmektedir. Yerine soğuk şebeke suyu (10-15°C) kullanılarak kazan besleme suyu hazırlanmakta, bu da yakıt, su ve kimyasal maliyetlerini gereksiz yere artırmaktadır.

**Çözüm:** Kondensatı toplayarak kondensat geri dönüş hattı ile kazana geri döndürmek. Kondensat zaten arıtılmış, sıcak ve düşük TDS'li sudur — kazana en uygun besleme suyudur.

**Tipik Tasarruf:** %5-15 (yakıt + su + arıtma kimyasalları toplamı)
**Tipik ROI:** 0.5-2 yıl

## Çalışma Prensibi

Buhar, proses ekipmanlarında gizli ısısını (latent heat) vererek yoğuşur ve kondensat haline gelir. Bu kondensat, buharın toplam enerji içeriğinin yaklaşık %25'ini hala barındırmaktadır (duyulur ısı — sensible heat). Kondensatı kazana geri döndürmek üç temel avantaj sağlar:

1. **Yakıt tasarrufu:** Kazan besleme suyu sıcaklığı yükselir, daha az yakıt ile aynı miktarda buhar üretilir. Her 6°C besleme suyu sıcaklık artışı yaklaşık %1 yakıt tasarrufu sağlar.
2. **Su tasarrufu:** Taze şebeke suyu yerine geri dönen kondensat kullanılır. Taze su maliyeti, su alma bedeli ve atıksu deşarj bedeli azalır.
3. **Kimyasal tasarrufu:** Kondensat zaten arıtılmış ve yumuşatılmış sudur. Geri dönüş oranı arttıkça taze su arıtma ihtiyacı ve kimyasal tüketimi (softener tuzu, O₂ bağlayıcı, pH düzenleyici, fosfat vb.) azalır.

Ek olarak, kondensat düşük TDS (Toplam Çözünmüş Katı) değerine sahip olduğundan blowdown ihtiyacını da azaltır — bu da ek yakıt ve su tasarrufu demektir.

## Kondensat Enerji İçeriği

Aşağıdaki tablo, farklı kondensat sıcaklıklarında taze su (15°C) yerine kondensat kullanıldığında ton başına tasarruf edilen enerjiyi göstermektedir.

| Kondensat Sıcaklığı (°C) | Kondensat Entalpisi (kJ/kg) | Taze Su Entalpisi (kJ/kg) | Enerji Tasarrufu (kJ/kg) | Enerji Tasarrufu (kWh/ton) |
|---------------------------|----------------------------|--------------------------|-------------------------|---------------------------|
| 60 | 251 | 63 | 188 | 52.2 |
| 70 | 293 | 63 | 230 | 63.9 |
| 80 | 335 | 63 | 272 | 75.6 |
| 85 | 356 | 63 | 293 | 81.4 |
| 90 | 377 | 63 | 314 | 87.2 |
| 95 | 398 | 63 | 335 | 93.1 |
| 100 (kaynama) | 419 | 63 | 356 | 98.9 |

**Not:** Taze su entalpisi 15°C referans sıcaklığında alınmıştır (h_f(15°C) ≈ 63 kJ/kg).

## Geri Dönüş Oranı Benchmarkları

| Geri Dönüş Oranı | Değerlendirme | Açıklama |
|-------------------|--------------|----------|
| >90% | Mükemmel (Excellent) | Kapalı devre kondensat sistemi, tüm eşanjörlerde geri dönüş, iyi bakımlı kapanlar |
| 70-90% | İyi (Good) | Çoğu dolaylı ısıtma noktasından geri dönüş, sınırlı açık proses kayıpları |
| 50-70% | Orta (Average) | Kısmi geri dönüş, bazı noktalarda kanalizasyona deşarj, bakımsız kapanlar |
| <50% | Kötü (Poor) | Yetersiz veya olmayan geri dönüş altyapısı, önemli enerji ve su kaybı |

**Endüstriyel ortalama (Türkiye):** %50-65 — iyileştirme potansiyeli yüksektir.

**Sektörel referanslar:**
- Gıda ve içecek: %60-80 (doğrudan enjeksiyon nedeniyle %100 mümkün değil)
- Tekstil: %40-70 (boyama proseslerinde kontaminasyon riski)
- Kimya: %70-90 (kapalı devre eşanjörler yaygın)
- Kağıt: %80-95 (yüksek buhar tüketimi, ekonomik gereklilik)

## Flash Buhar Geri Kazanımı

Yüksek basınçlı kondensat atmosferik basınca veya düşük basınçlı kondensat hattına açıldığında bir kısmı anında buharlaşır. Bu "flash buhar" önemli miktarda enerji taşır ve geri kazanılmalıdır.

### Flash Buhar Oranı Hesabı

```
x_flash = (h_f(P_yüksek) - h_f(P_düşük)) / h_fg(P_düşük)

Burada:
  x_flash      = Flash buhar kütle oranı (kg buhar / kg kondensat)
  h_f(P_yüksek) = Yüksek basınçtaki doyma sıvı entalpisi (kJ/kg)
  h_f(P_düşük)  = Düşük basınçtaki doyma sıvı entalpisi (kJ/kg)
  h_fg(P_düşük) = Düşük basınçtaki buharlaşma gizli ısısı (kJ/kg)
```

### Örnek Flash Buhar Oranları

| Kondensat Basıncı (bar) | Flash Basıncı (bar) | Flash Buhar Oranı (%) |
|--------------------------|---------------------|----------------------|
| 5 | 1 (atm.) | 8.5 |
| 8 | 1 (atm.) | 12.1 |
| 10 | 1 (atm.) | 15.3 |
| 12 | 1 (atm.) | 17.2 |
| 15 | 1 (atm.) | 19.8 |
| 10 | 3 | 8.0 |
| 15 | 3 | 12.7 |

### Geri Kazanım Yöntemleri

- **Flash tank (flash buhar tankı):** Yüksek basınçlı kondensat flash tanka girer, oluşan flash buhar düşük basınç kolektörüne veya deaeratöre yönlendirilir
- **Deaeratör beslemesi:** Flash buhar doğrudan deaeratöre verilir — hem gaz giderimi hem enerji geri kazanımı
- **Besleme suyu ön ısıtma:** Flash buhar ile besleme suyu ön ısıtılır
- **Düşük basınçlı proses:** Flash buhar LP (düşük basınç) uygulamalarında kullanılır

## Kontaminasyon Riskleri

Kondensat geri dönüşünde en kritik risk, kontamine kondensatın kazana döndürülmesidir. Bu durum kazan borularında tortu, korozyon ve köpürme sorunlarına yol açar.

### Kontaminasyon Türleri

| Kontaminasyon Türü | Kaynak | Belirti | Tehlike Seviyesi |
|--------------------|--------|---------|-----------------|
| Yağ (oil) | Buhar silindirli makineler, eski pompalar, proses kaçağı | Yüzey filmi, köpürme, priming | Yüksek |
| Ürün kontaminasyonu | Eşanjör boru kaçağı (gıda, kimya, şeker vb.) | pH değişimi, renk, koku | Yüksek |
| Korozyon ürünleri | Kondensat hattı korozyonu (demir oksit, bakır) | Kırmızımsı renk, tortu | Orta |
| Karbondioksit (CO₂) | Bikarbonat ayrışması, hava kaçağı | Düşük pH (<7), korozyon | Orta |

### İzleme Parametreleri

| Parametre | Kabul Edilebilir Sınır | Ölçüm Yöntemi | Ölçüm Sıklığı |
|-----------|----------------------|---------------|----------------|
| pH | 8.0-9.5 | pH metre | Sürekli veya günlük |
| İletkenlik (conductivity) | <300 µS/cm | İletkenlik ölçer | Sürekli |
| Toplam demir (Fe) | <0.5 ppm | Kolorimetrik test | Haftalık |
| Yağ içeriği | <1 ppm | Yağ-in-su analizörü | Haftalık |
| Sertlik (hardness) | <0.5 ppm CaCO₃ | Titre veya test kiti | Haftalık |

### Koruma Önlemleri

- **Kondensat örnekleme noktaları:** Her ana kondensat hattında örnekleme vanası
- **Otomatik kondensat dönüş vanası:** pH veya iletkenlik sınır değerini aşarsa kondensatı otomatik olarak drene yönlendirir
- **Ayrı kondensat hatları:** Kontaminasyon riski yüksek proseslerden gelen kondensat ayrı hatta toplanır
- **Kondensat polisher (parlatıcı):** Kontamine kondensat iyon değişim reçinesi ile arıtılarak kazana döndürülür

## Tasarruf Hesabı

### 1. Yakıt Tasarrufu

```
ΔT_besleme = (T_kondensat - T_taze_su) × (Δ_geri_dönüş / 100)

Q_tasarruf = m_buhar × c_p × ΔT_besleme   (kW)

Yakıt_tasarrufu_yıl = Q_tasarruf × Çalışma_saati × 3600 / (LHV × η_kazan)   (m³/yıl veya kg/yıl)

Yakıt_tasarrufu_EUR = Yakıt_tasarrufu_yıl × Yakıt_birim_fiyatı   (€/yıl)

Burada:
  T_kondensat       = Kondensat sıcaklığı (°C), tipik 80-95°C
  T_taze_su         = Şebeke suyu sıcaklığı (°C), tipik 10-15°C
  Δ_geri_dönüş      = Geri dönüş oranındaki artış (%, örn. %30'dan %80'e → 50)
  m_buhar           = Buhar üretimi (kg/s)
  c_p               = Suyun özgül ısısı (≈ 4.18 kJ/kg·°C)
  LHV               = Yakıt alt ısıl değeri (kJ/m³ veya kJ/kg)
  η_kazan           = Kazan verimi (0-1 arası)
```

### 2. Su Tasarrufu

```
Su_tasarrufu_yıl = m_buhar × Çalışma_saati × (Δ_geri_dönüş / 100)   (m³/yıl)

Su_tasarrufu_EUR = Su_tasarrufu_yıl × (Su_birim_fiyat + Atıksu_birim_fiyat)   (€/yıl)

Burada:
  Su_birim_fiyat    = Endüstriyel su fiyatı (tipik 1.5-4.0 €/m³, Türkiye)
  Atıksu_birim_fiyat = Atıksu deşarj bedeli (tipik 1.0-3.0 €/m³)
```

### 3. Kimyasal Tasarrufu

```
Kimyasal_tasarrufu_EUR = Su_tasarrufu_yıl × Kimyasal_birim_maliyet   (€/yıl)

Burada:
  Kimyasal_birim_maliyet = Taze su arıtma kimyasal maliyeti (tipik 0.5-2.0 €/m³)
  (Softener tuzu, O₂ bağlayıcı, fosfat, pH düzenleyici, dispersant vb.)
```

### 4. Toplam Tasarruf

```
Toplam_tasarruf_EUR = Yakıt_tasarrufu_EUR + Su_tasarrufu_EUR + Kimyasal_tasarrufu_EUR
```

## Uygulanabilirlik Kriterleri

### Ne Zaman Uygulanmalı

- Mevcut kondensat geri dönüş oranı <%70 ise
- Buhar tüketimi >1 t/h olan tesislerde
- Dolaylı ısıtma (eşanjör, ceketli tank, serpantin) ağırlıklı prosesler
- Kondensat hatları mevcut ancak bakımsız veya kısmen devre dışı ise
- Taze su ve atıksu maliyetlerinin yüksek olduğu bölgelerde

### Ne Zaman Uygulanamaz veya Sınırlıdır

- Doğrudan buhar enjeksiyonlu prosesler (kondensat ürünle karışır, geri dönmez)
- Kontamine kondensat (yağ, ürün karışımı) — ancak kondensat polisher ile çözülebilir
- Çok düşük buhar tüketimli tesisler (<0.5 t/h) — yatırım/fayda dengesizliği
- Kondensat noktaları kazan dairesinden çok uzak (>500 m) — boru maliyeti ve ısı kaybı

## Yatırım Maliyeti

| Bileşen | Kapasite / Boyut | Maliyet Aralığı (€) |
|---------|-----------------|---------------------|
| Kondensat toplama tankı (paslanmaz) | 0.5-2 m³ | 2,000-8,000 |
| Kondensat toplama tankı (paslanmaz) | 2-10 m³ | 8,000-25,000 |
| Kondensat pompası (elektrikli) | 1-5 m³/h | 1,500-5,000 |
| Kondensat pompası (basınçlı, mekanik) | 1-5 m³/h | 3,000-10,000 |
| Kondensat boru hattı (paslanmaz, izoleli) | DN25-DN50, 100 m | 5,000-15,000 |
| Kondensat boru hattı (paslanmaz, izoleli) | DN65-DN100, 100 m | 10,000-30,000 |
| Flash tank (flash buhar geri kazanımı) | 0.5-2 m³ | 3,000-12,000 |
| Kondensat kalite izleme sistemi | pH + iletkenlik | 2,000-8,000 |
| Otomatik divert vanası (kontaminasyon koruma) | DN25-DN80 | 1,500-5,000 |
| Kondensat polisher (iyon değişim) | 1-5 m³/h | 8,000-25,000 |
| Montaj ve devreye alma | — | Ekipman maliyetinin %15-25'i |

**Tipik toplam yatırım (orta ölçekli tesis, 3-5 t/h buhar):** €15,000-60,000

## ROI Hesabı

### Formül

```
Geri_ödeme_yıl = Toplam_yatırım / Toplam_yıllık_tasarruf

Burada:
  Toplam_yatırım      = Ekipman + boru + montaj + devreye alma (€)
  Toplam_yıllık_tasarruf = Yakıt + su + kimyasal tasarrufu (€/yıl)
```

### Örnek Hesap

**Senaryo:** 5 t/h buhar üretimi, 10 bar, doğalgaz yakıtlı kazan, 5,000 saat/yıl
- Mevcut kondensat geri dönüş oranı: %40
- Hedef kondensat geri dönüş oranı: %85
- Geri dönüş artışı: %45
- Kondensat sıcaklığı: 85°C
- Taze su sıcaklığı: 15°C

```
1. Yakıt Tasarrufu:
   ΔT_besleme = (85 - 15) × (45 / 100) = 31.5°C
   Q_tasarruf = (5,000 / 3600) × 4.18 × 31.5 = 183 kW
   Yakıt_tasarruf = 183 × 5,000 × 3.6 / (36,000 × 0.90) = 101,667 kWh/yıl
   Doğalgaz_tasarrufu = 101,667 / 10 = 10,167 m³/yıl
   Yakıt_tasarrufu_EUR = 10,167 × 0.35 = €3,558/yıl

2. Su Tasarrufu:
   Su_tasarrufu = 5.0 × 5,000 × (45 / 100) = 11,250 m³/yıl
   Su_tasarrufu_EUR = 11,250 × (2.5 + 1.5) = €45,000/yıl
   (Not: Bu değer yüksek görünebilir — gerçek tasarruf buhar/kondensat
   oranına ve tesis su fiyatına bağlıdır)

   Düzeltilmiş hesap (kondensat debisi = buhar debisinin ~%90'ı):
   Kondensat_debi = 5.0 × 0.90 = 4.5 t/h
   Ek geri dönen kondensat = 4.5 × (45/100) = 2.025 t/h
   Su_tasarrufu = 2.025 × 5,000 = 10,125 m³/yıl
   Su_tasarrufu_EUR = 10,125 × 4.0 = €40,500/yıl

3. Kimyasal Tasarrufu:
   Kimyasal_tasarrufu_EUR = 10,125 × 1.0 = €10,125/yıl

4. Toplam Yıllık Tasarruf:
   Toplam = 3,558 + 40,500 + 10,125 = €54,183/yıl

5. Yatırım:
   Kondensat tankı + pompalar + boru hattı + izleme = €35,000

6. Geri Ödeme:
   ROI = 35,000 / 54,183 = 0.65 yıl (~8 ay)
```

**Not:** Su ve atıksu maliyetlerinin toplam tasarrufa katkısı genellikle yakıt tasarrufundan daha büyüktür. Türkiye'de organize sanayi bölgelerinde su + atıksu maliyeti 3-6 €/m³ aralığındadır.

## Uygulama Adımları

1. **Mevcut durum tespiti:** Mevcut kondensat geri dönüş oranını ölç veya tahmin et. Tüm buhar kullanım noktalarını ve kondensat deşarj noktalarını haritalandır.

2. **Kondensat kalite analizi:** Her ana kondensat kaynağından numune al. pH, iletkenlik, yağ, demir içeriği analiz et. Kontaminasyon riski olan ve olmayan hatları belirle.

3. **Geri dönüş potansiyeli belirleme:** Dolaylı ısıtma noktalarından geri dönüş yapılabilir, doğrudan enjeksiyon noktalarından yapılamaz. Her noktanın debisini ve mesafesini belirle.

4. **Boru güzergahı planlama:** Kondensat toplama tankı konumunu belirle (genellikle kazan dairesi yakını). Boru güzergahını, çaplarını ve izolasyon kalınlığını hesapla.

5. **Ekipman seçimi:** Kondensat tankı, pompa, flash tank (gerekirse), izleme sistemi, otomatik divert vanası seç. Minimum 3 tedarikçiden teklif al.

6. **Kurulum:** Kondensat toplama tankı, pompalar, boru hattı ve kontrol sistemi montajı. Tipik kurulum süresi: 1-4 hafta (tesis büyüklüğüne göre).

7. **Devreye alma ve doğrulama:** Kondensat kalitesini kontrol et, pompa çalışmasını doğrula, geri dönüş oranını ölç. İlk 1 ay yoğun izleme yap.

8. **Sürekli izleme:** pH ve iletkenlik sürekli ölçümü ile kondensat kalitesini takip et. Geri dönüş oranını aylık olarak raporla.

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Kondensat kontaminasyonu | Eşanjör kaçağı veya proses karışımı ile kondensat kirlenir, kazan hasarı | Otomatik divert vanası, sürekli pH/iletkenlik izleme, kondensat polisher |
| Kondensat hattı korozyonu | CO₂ kaynaklı karbonik asit korozyonu (pH düşüşü) | Kondensat hattında paslanmaz çelik veya plastik boru, kondensat nötralizasyon kimyasalları |
| Su darbesi (water hammer) | Kondensat hattında buhar ve su karışımı ani basınç darbesi yaratır | Uygun eğim (%1-2 düşüş), kondensat cepleri ve drenaj noktaları, boyutlandırma |
| Flash buhar kaybı | Atmosferik kondensat tankından flash buhar atmosfere kaçar | Kapalı kondensat tankı, flash buhar geri kazanım sistemi |
| Kondensat pompası arızası | Pompa durduğunda kondensat geri dönüşü durur | Yedek pompa (standby), otomatik geçiş, alarm sistemi |
| Boru tıkanması | Korozyon ürünleri veya tortu birikmesi ile boru tıkanır | Süzgeç (strainer), periyodik temizlik, uygun boru malzemesi |
| Kondensat tankı taşması | Ani yük değişimlerinde tank kapasitesi yetersiz kalır | Uygun tank boyutlandırma (15-20 dakika depolama), taşma hattı |

## İlgili Dosyalar

- Buhar sistemleri genel bakış: `equipment/steam_systems_overview.md`
- Kazan yakıtları: `equipment/boiler_fuels.md`
- Flash buhar geri kazanımı: `solutions/flash_steam_recovery.md`
- Buhar kapanı bakımı: `solutions/steam_trap_maintenance.md`
- Blowdown ısı geri kazanımı: `solutions/boiler_blowdown_recovery.md`
- Ekonomizer: `solutions/boiler_economizer.md`
- Buhar izolasyonu: `solutions/steam_insulation.md`
- Kazan exergy formülleri: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Buhar denetim metodolojisi: `methodology/steam_audit.md`

## Referanslar

- Spirax Sarco, "The Steam and Condensate Loop," Technical Reference Guide — Condensate Recovery Chapter
- U.S. DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry," 2nd Edition
- ASME PTC 4 (2013), "Fired Steam Generators — Performance Test Codes"
- Kotas, T.J., "The Exergy Method of Thermal Plant Analysis," Krieger Publishing, 1995
- Bejan, A., Tsatsaronis, G., Moran, M.J., "Thermal Design and Optimization," Wiley, 1996
- Rosen, M.A., Dincer, I., "Exergy Analysis of Waste Emissions," Int. J. Energy Research, 1999
- IAPWS-IF97, International Association for the Properties of Water and Steam — Steam Tables
- Armstrong International, "Condensate Recovery" Application Guide
- TLV Co., "Steam Engineering — Condensate Recovery Systems" Technical Handbook
- Türkiye Enerji Verimliliği Derneği (ENVER), Buhar Sistemleri Verimlilik Kılavuzu
