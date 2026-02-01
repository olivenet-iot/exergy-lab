---
title: "Elektrikli Kazan — Electric Boiler"
category: equipment
equipment_type: boiler
subtype: "Elektrikli Kazan"
keywords: [elektrikli kazan, rezistans, verimlilik]
related_files: [boiler/benchmarks.md, boiler/formulas.md, boiler/solutions/insulation.md]
use_when: ["Elektrikli kazan analizi yapılırken", "Elektrikle ısıtma değerlendirilirken"]
priority: medium
last_updated: 2026-01-31
---
# Elektrikli Kazan — Electric Boiler

> Son güncelleme: 2026-01-31

## Genel Bilgiler
- Tip: Elektrikli kazan (Electric boiler) — rezistans (immersion/resistance) tipi ve elektrot (electrode) tipi olmak üzere iki ana yapı
- Kapasite aralığı: 10 kW – 50 MW (rezistans tipi), 5 MW – 60 MW (elektrot tipi)
- Çalışma basıncı: 0 – 40 bar (vakumlu sistemlerde negatif basınç da mümkündür)
- Çıkış: Doymuş buhar, kızgın su (sıcak su) veya kızgın buhar (superheated steam, ek ısıtıcı ile)
- Enerji verimi (energy efficiency): %98 – 99.9 (neredeyse mükemmel termal verim)
- Exergy verimi (exergy efficiency): %8 – 30 (ÇOK DÜŞÜK — elektrik saf exerjidir, ısıya dönüştürmek exerjiyi büyük ölçüde yok eder)
- Yanma yok, baca gazı yok, sahada sıfır emisyon (zero on-site emissions)
- Sessiz çalışma, hızlı devreye alma (saniyeler içinde tam yüke çıkabilir)
- Kompakt tasarım, baca ve yakıt depolama alanı gerektirmez
- Başlıca markalar: Parat Halvorsen (Norveç), Vapor Power (ABD), Precision Boilers (ABD), PARAT IEH (Avrupa), Zander & Ingeström (İsveç), Cleaver-Brooks (ABD)

## Çalışma Prensibi

Elektrikli kazanlar, elektrik enerjisini doğrudan ısıya dönüştürerek su ısıtır veya buhar üretir. İki temel tasarım mevcuttur.

### Rezistans (İmmersiyon) Tipi — Resistance/Immersion Type
- Elektrikli ısıtma elemanları (rezistanslar) doğrudan suyun içine daldırılmıştır
- Isı transferi: Rezistans yüzeyinden suya konveksiyon ile
- Tipik kapasite: 10 kW – 3 MW (daha büyük kapasiteler mümkün ancak nadir)
- Basit tasarım, düşük bakım maliyeti
- Rezistans ömrü: 15,000 – 30,000 saat (su kalitesine bağlı)
- Kireçlenme riski: Sert sularda rezistans yüzeyinde kireç birikmesi verimi düşürür
- Güç kontrolü: Kademe (step) bazlı — rezistans gruplarının açılıp kapatılmasıyla
- Düşük gerilim (400 V) veya orta gerilim (6.3 kV, 10 kV) bağlantı

### Elektrot Tipi — Electrode Type
- Elektrik akımı doğrudan suyun kendisinden geçer (su iletken olarak kullanılır)
- Su, iki elektrot arasında rezistans görevi görür ve ohmik ısınma ile ısınır
- Tipik kapasite: 5 MW – 60 MW (endüstriyel ölçek)
- Kademesiz güç kontrolü (stepless power modulation): %0 – 100 arasında sürekli ayar
- Güç kontrolü mekanizması: Elektrotların suya daldırılma derinliğinin ayarlanması veya nozul sistemleri ile
- Yüksek gerilim bağlantısı: 6.3 kV, 10 kV veya 20 kV
- Suyun elektriksel iletkenliği kritiktir: tipik olarak 200 – 1,500 µS/cm gereklidir
- İletkenlik ayarı için sodyum hidroksit (NaOH) veya trisodyum fosfat (Na₃PO₄) dozajlanır
- Devreye alma süresi: Soğuk başlatmada 5 – 10 dakika, sıcak beklemeden saniyeler içinde

## Enerji Dağılımı

| Enerji kalemi | Oran (%) | Açıklama |
|---------------|----------|----------|
| Faydalı ısı (useful heat) | 98 – 99.5 | Suya/buhara aktarılan enerji |
| Bekleme kayıpları (standby losses) | 0.3 – 1.5 | Yüzeyden ışınım ve konveksiyon |
| Elektrik dağıtım kayıpları | 0.1 – 0.5 | Kablo, kontaktör, trafo kayıpları |
| Baca gazı kaybı | 0 | Yanma yok — baca gazı oluşmaz |
| Yakıt hazırlama kaybı | 0 | Yakıt yok — ön ısıtma veya atomizasyon gerekmez |

```
η_energy = Q_faydalı / W_elektrik

Tipik değer:
η_energy = 0.98 – 0.999

Burada:
  Q_faydalı  : Suya/buhara aktarılan ısı (kJ)
  W_elektrik : Tüketilen elektrik enerjisi (kJ)
```

## Exergy Analizi — Kritik Not

Elektrikli kazanlar, enerji verimi açısından neredeyse mükemmel olmasına rağmen, termodinamik (exergy) perspektifinden bakıldığında en verimsiz kazan tipidir. Bunun temel sebebi:

```
Elektrik = saf exergy (%100 exergy içeriği)
Buhar/sıcak su = düşük exergy içeriği

Exergy girdisi:
  Ex_in = W_elektrik (elektrik enerjisi = saf exergy)

Exergy çıktısı (doymuş buhar için):
  Ex_out = m_buhar × [(h_s - h₀) - T₀ × (s_s - s₀)]

Burada:
  h_s, s_s : Buharın entalpi ve entropisi
  h₀, s₀   : Ölü durum (dead state) entalpi ve entropisi (25°C, 1 atm)
  T₀        : Referans çevre sıcaklığı (298.15 K)
  m_buhar   : Buhar debisi (kg/s)
```

### Sayısal Örnek — 10 bar Doymuş Buhar Üretimi

```
Koşullar:
  P_buhar = 10 bar (doymuş)
  T_buhar = 179.9°C
  T_besleme = 80°C (besleme suyu sıcaklığı)
  T₀ = 25°C (298.15 K)

Buhar özellikleri (doymuş, 10 bar):
  h_s = 2,778 kJ/kg
  s_s = 6.586 kJ/(kg·K)

Besleme suyu (80°C, sıvı):
  h_fw = 335 kJ/kg
  s_fw = 1.075 kJ/(kg·K)

Ölü durum (25°C, 1 atm, sıvı):
  h₀ = 104.9 kJ/kg
  s₀ = 0.3674 kJ/(kg·K)

Enerji transferi (kg başına):
  q = h_s - h_fw = 2,778 - 335 = 2,443 kJ/kg

Exergy transferi (kg başına):
  ex_buhar = (h_s - h₀) - T₀ × (s_s - s₀)
  ex_buhar = (2,778 - 104.9) - 298.15 × (6.586 - 0.3674)
  ex_buhar = 2,673.1 - 298.15 × 6.219
  ex_buhar = 2,673.1 - 1,854.1
  ex_buhar = 819.0 kJ/kg

Exergy girdisi (elektrik, kg buhar başına):
  ex_in = q / η_energy = 2,443 / 0.99 = 2,468 kJ/kg

Exergy verimi:
  η_exergy = ex_buhar / ex_in = 819.0 / 2,468 = 0.332 = %33.2

Exergy yıkımı (irreversibility):
  I = ex_in - ex_buhar = 2,468 - 819 = 1,649 kJ/kg
  Exergy yıkım oranı = 1,649 / 2,468 = %66.8
```

**Sonuç:** Enerji verimi %99 olmasına rağmen, exergy veriminin sadece %33 olması, elektriğin ısıya dönüştürülmesinin termodinamik açıdan ne kadar israf olduğunu açıkça göstermektedir. Elektrik saf iş potansiyeli taşırken, düşük sıcaklıklı ısı çok düşük iş potansiyeli taşır.

### Sıcak Su Üretiminde Exergy Verimi (Daha Düşük)

```
Koşullar:
  T_çıkış = 90°C (sıcak su)
  T_giriş = 60°C (dönüş suyu)
  T₀ = 25°C

Exergy çıktısı (Carnot yaklaşımı):
  η_Carnot_ort = 1 - T₀ / T_log_mean
  T_log_mean = (90 - 60) / ln(363.15 / 333.15) = 30 / 0.0862 = 348 K
  η_Carnot_ort = 1 - 298.15 / 348 = 0.143

Exergy verimi:
  η_exergy ≈ η_energy × η_Carnot_ort = 0.99 × 0.143 = 0.142 = %14.2
```

Sıcak su üretiminde exergy verimi %14 seviyesine kadar düşer — bu, elektrikli kazanların düşük sıcaklık uygulamalarında termodinamik açıdan kabul edilemez derecede verimsiz olduğunu gösterir. Bu tür uygulamalarda ısı pompası (COP 3-5) çok daha uygun bir seçimdir.

## Ölçülmesi Gereken Parametreler

| Parametre | Sembol | Birim | Ölçüm yöntemi | Frekans |
|-----------|--------|-------|----------------|---------|
| Elektrik tüketimi | W_el | kWh | Enerji analizörü / sayaç | Sürekli |
| Buhar debisi | m_dot | t/h veya kg/s | Vortex veya orifis debimetre | Sürekli |
| Buhar basıncı | P_s | bar(g) | Basınç transmitteri | Sürekli |
| Buhar sıcaklığı | T_s | °C | Termokupl / PT100 | Sürekli |
| Besleme suyu sıcaklığı | T_fw | °C | PT100 | Sürekli |
| Besleme suyu debisi | m_fw | t/h | Elektromanyetik debimetre | Sürekli |
| Kondensat dönüş sıcaklığı | T_cond | °C | PT100 | Sürekli |
| Kondensat dönüş oranı | CR | % | Hesaplama | Günlük |
| Blöf oranı | BD | % | Debimetre veya hesaplama | Günlük |
| Su iletkenliği (elektrot tipi) | σ | µS/cm | İletkenlik sensörü | Sürekli |
| Ortam sıcaklığı | T₀ | °C | Termometre | Saatlik |
| Güç faktörü | cos φ | — | Enerji analizörü | Sürekli |
| Gerilim / akım | V, I | V, A | Enerji analizörü | Sürekli |

## Varsayılan Değerler (Ölçüm Yoksa)

Aşağıdaki değerler, tesis verisi mevcut olmadığında exergy hesaplamalarında başlangıç değeri olarak kullanılabilir.

| Parametre | Varsayılan Değer | Not |
|-----------|------------------|-----|
| Enerji verimi (η_energy) | %99 | Rezistans ve elektrot tipi için |
| Exergy verimi (buhar, 10 bar) | %30 – 33 | Doymuş buhar üretimi |
| Exergy verimi (sıcak su, 80°C) | %12 – 16 | Kalorifer/proses sıcak su |
| Bekleme kaybı | %1 | Izolasyonlu kazan |
| Besleme suyu sıcaklığı | 80°C | Kondensat dönüşlü sistem |
| Blöf oranı | %2 – 5 | Otomatik blöf sistemi |
| Su iletkenliği (elektrot tipi) | 800 µS/cm | NaOH dozajlı |
| Referans çevre sıcaklığı (T₀) | 25°C (298.15 K) | Standart ölü durum |
| Referans çevre basıncı (P₀) | 101.325 kPa | Standart ölü durum |
| Elektrik maliyeti (Türkiye, sanayi) | 0.08 – 0.12 EUR/kWh | 2025 yılı ortalama |
| Doğalgaz maliyeti (Türkiye, sanayi) | 0.035 – 0.05 EUR/kWh | 2025 yılı ortalama |

## Kullanım Senaryoları

### 1. Pik Tıraşlama / Yedekleme (Peak Shaving / Backup)
- Ana buhar kaynağı olan yakıtlı kazanın yetişemediği anlık talep artışlarında devreye girer
- Hızlı devreye alma özelliği (%0 → %100 yüke saniyeler içinde) kritik avantajdır
- Yıllık çalışma saati düşüktür (<500 saat/yıl) — yatırım maliyeti düşük, işletme maliyeti tolere edilebilir

### 2. Gaz Altyapısı Olmayan Tesisler
- Doğalgaz şebekesine erişimi olmayan bölgelerde (dağlık alanlar, adalar, uzak tesisler)
- LPG veya fuel oil alternatifine göre daha temiz ve bakımı kolay
- Tesis içi yakıt depolama riski ortadan kalkar

### 3. Şebeke Dengeleme / Talep Yanıtı (Grid Balancing / Demand Response)
- Elektrik şebekesinde arz fazlası olduğunda (rüzgar/güneş üretim piki) kazan devreye alınarak ısı depolanır
- Power-to-Heat (P2H) konsepti: Negatif elektrik fiyatlarında ısı üretimi
- Termal depolama tankı ile birleştirildiğinde esnek enerji yönetimi sağlar
- Frekans regülasyonu hizmetleri için uygun (hızlı yanıt kapasitesi)

### 4. Yeşil Elektrik Senaryoları (Green Electricity)
- %100 yenilenebilir elektrik tedarik sözleşmesi (PPA) veya sertifika (I-REC, GO) ile
- Sahada sıfır karbon emisyonu + yeşil elektrik = tam karbon nötr ısı üretimi
- ESG raporlama ve karbon nötr hedefler için cazip
- Ancak exergy perspektifinden hala verimsiz — ısı pompası öncelikli değerlendirilmelidir

### 5. Temiz Oda / Gıda / İlaç Endüstrisi
- Yanma ürünleri sıfır — kontaminasyon riski yok
- Titreşim ve gürültü minimum
- Kompakt boyutlar — temiz alan içine yerleştirilebilir

## Maliyet Karşılaştırması — Elektrikli vs Doğalgazlı Kazan

Aşağıdaki tablo, 5 MW kapasiteli bir buhar kazanı (10 bar, 8,000 saat/yıl) için karşılaştırma sunar.

| Kalem | Elektrikli Kazan | Doğalgazlı Kazan | Birim |
|-------|-------------------|-------------------|-------|
| Yatırım maliyeti (CAPEX) | 150,000 – 300,000 | 400,000 – 700,000 | EUR |
| Kurulum maliyeti | 30,000 – 60,000 | 80,000 – 150,000 | EUR |
| Enerji verimi | %99 | %90 (LHV bazlı) | — |
| Enerji tüketimi (yıllık) | 40,400 MWh_el | 44,444 MWh_th (4,444 m³/h NG) | — |
| Enerji birim maliyeti | 0.10 EUR/kWh_el | 0.04 EUR/kWh_th | — |
| Yıllık enerji maliyeti (OPEX) | 4,040,000 | 1,778,000 | EUR/yıl |
| Bakım maliyeti (yıllık) | 5,000 – 15,000 | 20,000 – 50,000 | EUR/yıl |
| Baca / emisyon altyapısı | Gerekli değil | Gerekli (baca, brülör, gaz hattı) | — |
| CO₂ emisyonu (sahada) | 0 | ~8,000 t CO₂/yıl | — |
| CO₂ maliyeti (ETS, ~80 EUR/t) | 0 | ~640,000 | EUR/yıl |
| **Toplam yıllık maliyet** | **~4,050,000** | **~2,448,000** | **EUR/yıl** |

```
Sonuç:
  Elektrikli kazanın yıllık işletme maliyeti, doğalgazlı kazanın
  yaklaşık 1.65 katıdır (Türkiye 2025 enerji fiyatlarıyla).

  Ancak CO₂ maliyeti (ETS veya karbon vergisi) dahil edildiğinde
  fark azalır:
    Elektrikli: 4,050,000 EUR/yıl
    Doğalgazlı: 2,448,000 EUR/yıl (CO₂ dahil)

  Kırılma noktası (break-even):
    Elektrik fiyatı ≤ 0.06 EUR/kWh olduğunda elektrikli kazan
    ekonomik hale gelir (mevcut gaz fiyatları ve CO₂ maliyeti ile).
```

## Dikkat Edilecekler

1. **Exergy israfı farkındalığı:** Elektrikli kazan enerji verimli görünse de, exergy analizi büyük termodinamik kayıp olduğunu ortaya koyar. Isı pompası (heat pump) alternatifleri mutlaka değerlendirilmelidir — COP 3-5 olan bir ısı pompası, aynı ısıyı %60-80 daha az elektrikle üretir. Bkz. `solutions/heat_pump_vs_electric_boiler.md`

2. **Elektrik altyapısı ve güç kalitesi:** Büyük kapasiteli elektrikli kazanlar (>1 MW) yüksek gerilim bağlantısı, özel trafo ve yeterli şebeke kapasitesi gerektirir. Güç faktörü düzeltmesi (power factor correction) gerekebilir. Şebeke bağlantı maliyeti CAPEX'i önemli ölçüde artırabilir.

3. **Su kalitesi yönetimi (özellikle elektrot tipi):** Elektrot tipi kazanlarda suyun iletkenliği doğrudan güç çıktısını belirler. Düşük iletkenlik = düşük güç. Kimyasal dozajlama sistemi ve iletkenlik kontrolü zorunludur. Rezistans tipinde ise kireçlenme önleyici su arıtma gereklidir.

4. **Termal depolama entegrasyonu:** Elektrikli kazanların ekonomik fizibilitesi, termal enerji depolama (TES) tankları ile birleştirildiğinde önemli ölçüde artar. Ucuz elektrik saatlerinde (gece tarife, yenilenebilir pik) ısı depolanıp pahalı saatlerde kullanılabilir.

5. **Redündansi ve güvenilirlik:** Elektrik kesintilerinde kazan tamamen devre dışı kalır — yakıtlı kazanlardan farklı olarak UPS veya jeneratör ile çalıştırılamaz (güç yetmez). Kritik buhar ihtiyacı olan tesislerde yedek yakıtlı kazan bulundurulmalıdır.

6. **Yasal ve düzenleyici gereksinimler:** Türkiye'de elektrikli kazanlar basınçlı kap mevzuatına (Basınçlı Ekipmanlar Yönetmeliği — 2014/68/AB uyumlu) tabidir. Periyodik muayene zorunludur. Baca ve emisyon izni gerekmez. Yüksek gerilim bağlantısı için TEDAŞ/dağıtım şirketi onayı ve proje gereklidir.

## İlgili Dosyalar
- Kazan yakıtları ve özellikleri: `equipment/boiler_fuels.md`
- Ateş borulu buhar kazanları: `equipment/boiler_steam_firetube.md`
- Su borulu buhar kazanları: `equipment/boiler_steam_watertube.md`
- Sıcak su kazanları: `equipment/boiler_hotwater.md`
- Kazan exergy hesaplamaları: `formulas/boiler_exergy.md`
- Kazan benchmark verileri: `benchmarks/boiler_benchmarks.md`
- Isı pompası karşılaştırması: `solutions/heat_pump_vs_electric_boiler.md`
- Power-to-Heat senaryoları: `solutions/power_to_heat.md`
- Termal enerji depolama: `solutions/thermal_energy_storage.md`

## Referanslar
- Bejan, A., Tsatsaronis, G., Moran, M.J. (1996). *Thermal Design and Optimization*, Wiley.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths. (Reprinted by Krieger, 1995.)
- Szargut, J., Morris, D.R., Steward, F.R. (2005). *Exergy Analysis of Thermal, Chemical, and Metallurgical Processes*, Springer.
- Parat Halvorsen (2024). *Electrode Boiler Technical Documentation*, Parat Halvorsen AS.
- ASME BPV Code Section I (2023). *Rules for Construction of Power Boilers*, ASME.
- Spirax Sarco (2023). *The Steam and Condensate Loop*, Technical Reference Guide.
- IEC 60335-2-35 (2020). *Safety of Household and Similar Electrical Appliances — Particular Requirements for Instantaneous Water Heaters*.
- Danish Energy Agency (2024). *Technology Data for Generation of Electricity and District Heating*, Chapter on Electric Boilers.
- IPCC (2006). *Guidelines for National Greenhouse Gas Inventories*, Volume 2: Energy.
- Türk Standardları Enstitüsü — Basınçlı Ekipmanlar Yönetmeliği (2014/68/AB uyumu).
