---
title: "Hava Soğutmalı Eşanjörler (Air-Cooled Heat Exchangers)"
category: equipment
equipment_type: heat_exchanger
subtype: "Hava Soğutmalı"
keywords: [eşanjör, hava soğutmalı, air cooled, ACHE, fin fan, kanatlı boru, API 661, fan]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md]
use_when: ["Hava soğutmalı eşanjör analizi yapılırken", "Fin fan cooler değerlendirmesi gerektiğinde", "Soğutma suyu alternatifi araştırılırken"]
priority: high
last_updated: 2026-02-01
---
# Hava Soğutmalı Eşanjörler — Air-Cooled Heat Exchangers (ACHE)

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Hava soğutmalı eşanjörler (air-cooled heat exchangers — ACHE veya fin fan coolers), soğutma suyu yerine ortam havasını soğutma ortamı olarak kullanan ısı değiştiricileridir. Su kıtlığı olan bölgelerde, soğutma kulesi yatırım ve işletme maliyetinden kaçınılmak istendiğinde veya çevresel düzenlemeler nedeniyle tercih edilir.

- Kapasite aralığı: 50 kW - 200 MW
- Çalışma basıncı: 0.1 - 200 bar (boru tarafı)
- Çalışma sıcaklığı: -50°C ile 400°C (boru tarafı)
- Tipik U değeri: 20-300 W/(m²·K) (çıplak boru alanına göre)
- Yaklaşma sıcaklığı: 10-25°C (ortam hava sıcaklığına göre)
- Tipik ömür: 20-30 yıl

## Temel Bileşenler

### Yapısal Elemanlar

| Bileşen | İşlev | Malzeme |
|---------|-------|---------|
| Boru demetleri (tube bundles) | Sıcak akışkanı taşır | Karbon çelik, SS, Cu-Ni, Ti |
| Kanatlar (fins) | Hava tarafı yüzey alanını artırır | Alüminyum (en yaygın), galvanize çelik |
| Fanlar | Hava akışını sağlar | Alüminyum, fiberglas, polimer |
| Fan motorları | Fan tahriği | Elektrik motoru (IE3/IE4) |
| Yapısal çerçeve | Mekanik destek | Karbon çelik, galvanize |
| Kolektörler (headers) | Akışkan dağıtımı | Karbon çelik, alaşım |
| Plenum (hava odası) | Hava dağıtımı | Çelik sac |

## Çekiş Tipleri

### İndüklenmiş Çekiş (Induced Draft)

Fan, boru demetinin üzerinde yer alır ve havayı yukarı çeker.

```
Hava akış yönü:

  FAN ←←←←←←←← (emme)
  ==================  (boru demeti)
  →→→→→→→→→→→→→→→→  (ortam havası girer)

Burada:
  Hava, boru demetinden geçerek fan tarafından çekilir
```

**Avantajlar:**
- Daha düşük hava geri devridaimi (recirculation) — sıcak hava yukarı atılır
- Boru demeti doğal çekiş ile korunur (fan arızasında %30-40 kapasite)
- Yağmur ve dolu koruması daha iyi (üstte fan)
- Yapısal tasarım: ağırlık tabana yakın

**Dezavantajlar:**
- Fan sıcak hava içinde çalışır — daha kısa ömür
- Motor sıcak havaya maruz — soğutma gerekebilir
- Bakım erişimi daha zor (yüksekte)
- Fan verimliliği biraz düşük (sıcak, düşük yoğunluklu hava)

### Cebri Çekiş (Forced Draft)

Fan, boru demetinin altında yer alır ve havayı boru demetine doğru iter.

```
Hava akış yönü:

  →→→→→→→→→→→→→→→→  (sıcak hava çıkar)
  ==================  (boru demeti)
  FAN →→→→→→→→ (basma)

Burada:
  Fan, ortam havasını boru demetine doğru iter
```

**Avantajlar:**
- Fan soğuk hava ile çalışır — uzun ömür, yüksek verim
- Motor soğuk havada — soğutma sorunu yok
- Bakım erişimi kolay (altta)
- Fan gücü biraz daha düşük (yoğun soğuk hava)

**Dezavantajlar:**
- Sıcak hava geri devridaimi riski (özellikle rüzgarlı koşullarda)
- Doğal çekiş katkısı düşük (fan arızasında kapasite düşer)
- Yağmur/dolu doğrudan boru demetine etki eder

### Çekiş Tipi Seçim Karşılaştırması

| Kriter | İndüklenmiş Çekiş | Cebri Çekiş |
|--------|-------------------|-------------|
| Hava geri devridaimi | Düşük (tercih edilir) | Yüksek (dikkat gerekli) |
| Fan ömrü | Kısa (sıcak hava) | Uzun (soğuk hava) |
| Doğal çekiş yedekliliği | %30-40 | %10-15 |
| Bakım erişimi | Zor (yüksekte) | Kolay (altta) |
| Gürültü dağılımı | Yukarı yönlü | Yana yayılım |
| Maliyet | %5-10 daha pahalı | Referans |
| Endüstriyel tercih | %75-80 (çoğunluk) | %20-25 |

## Kanatlı Boru (Finned Tube) Tasarımı

### Kanat Tipleri

| Kanat Tipi | İmalat Yöntemi | Temas Direnci | Maks Sıcaklık | Maliyet |
|------------|---------------|---------------|---------------|---------|
| L-kanat (L-foot) | Alüminyum şerit sarma | Orta | 180°C | Düşük |
| Gömülü kanat (Embedded/grooved) | Boru yivine gömme | Düşük | 400°C | Orta |
| Ekstrüde kanat (Extruded) | Alüminyum ekstrüzyon | Çok düşük (metalik bağ) | 300°C | Orta-Yüksek |
| Kaynaklı kanat (Welded) | Çelik kanat kaynağı | Sıfır (kaynak) | 500°C+ | Yüksek |
| Plaka kanat (Plate fin) | Alüminyum levha | Düşük | 200°C | Düşük |

### Kanat Geometrisi Parametreleri

| Parametre | Tipik Aralık | Etkisi |
|-----------|-------------|--------|
| Kanat yüksekliği (h_f) | 12-16 mm | Alan artışı, ΔP artışı |
| Kanat kalınlığı (t_f) | 0.3-0.5 mm (Al), 1.0-2.0 mm (çelik) | Dayanım, ısı iletimi |
| Kanat aralığı (fin pitch) | 2.3-3.5 mm (275-433 kanat/m) | Kirlenme vs ısı transferi dengesi |
| Kanat verimi (η_f) | 0.85-0.95 (Al), 0.60-0.80 (çelik) | Efektif alan |
| Alan oranı (A_fin/A_çıplak) | 15-25 | Toplam yüzey büyütme |

### Kanat Aralığı ve Kirlenme İlişkisi

```
Kanat aralığı seçimi:

  Temiz servis (petrokimya, gaz soğutma):
    Kanat aralığı = 2.3-2.5 mm (394-433 kanat/m)
    → Maksimum alan, minimum boyut

  Orta kirli servis (genel endüstriyel):
    Kanat aralığı = 2.5-3.0 mm (333-394 kanat/m)
    → Denge

  Kirli servis (toz, pamuk lifleri, yaprak):
    Kanat aralığı = 3.0-3.5 mm (275-333 kanat/m)
    → Kolay temizlik, düşük tıkanma

  Çok kirli servis:
    Düz (kanatsız) boru veya geniş aralıklı plaka kanat
```

## Fan Seçimi ve Tasarımı

### Fan Tipleri

| Tip | Bıçak Sayısı | Verimlilik | Gürültü | Maliyet |
|-----|-------------|------------|---------|---------|
| Aksiyal — sabit kanat | 4-8 | %50-65 | Yüksek | Düşük |
| Aksiyal — ayarlanabilir kanat | 4-8 | %55-70 | Orta | Orta |
| Aksiyal — otomatik ayarlanabilir | 4-8 | %60-75 | Orta | Yüksek |
| VSD ile aksiyal | 4-8 | %60-80 (sistem) | Düşük (düşük devirde) | Yüksek |

### Fan Gücü Hesabı

```
Fan gücü:

  P_fan = V_hava × ΔP_toplam / (η_fan × η_motor)

Burada:
  V_hava     : Hacimsel hava debisi (m³/s)
  ΔP_toplam  : Toplam statik basınç düşüşü (Pa)
  η_fan      : Fan verimi (0.55-0.75)
  η_motor    : Motor verimi (0.90-0.95)

Tipik ΔP bileşenleri:
  Boru demeti (hava tarafı): 80-250 Pa
  Plenum ve yapı: 20-50 Pa
  Giriş/çıkış kayıpları: 20-40 Pa
  Toplam: 120-340 Pa

Tipik fan gücü: Soğutulan ısının %0.5-2.0'si
  Örnek: 1,000 kW soğutma → 5-20 kW fan gücü
```

### Fan Yasaları (Affinity Laws)

```
Sabit çaplı fan için hız değişiminde:

  V₂ / V₁ = n₂ / n₁           (debi ∝ hız)
  ΔP₂ / ΔP₁ = (n₂ / n₁)²     (basınç ∝ hız²)
  P₂ / P₁ = (n₂ / n₁)³       (güç ∝ hız³)

Burada:
  n = Fan devir hızı (rpm)

Örnek (VSD ile %50 hız):
  Debi: %50
  Basınç: %25
  Güç: %12.5 → %87.5 enerji tasarrufu!
```

## Ortam Sıcaklığı Düzeltmesi

### Tasarım Sıcaklığı Seçimi

| Parametre | Tipik Değer | Not |
|-----------|------------|-----|
| Tasarım hava sıcaklığı | %2 aşılma olasılığı (yıllık) | Yaz pik sıcaklık |
| Türkiye — İstanbul | 34°C kuru termometre | Yaz tasarım |
| Türkiye — Ankara | 36°C kuru termometre | Yaz tasarım |
| Türkiye — Adana | 39°C kuru termometre | Yaz tasarım |
| Kış çalışma sıcaklığı | 0-5°C | Kontrolsüz aşırı soğutma riski |
| Gece/gündüz farkı | 8-15°C | Kapasite değişimi |

### Sıcaklık Etkisi ve Kapasite

```
Hava sıcaklığının kapasiteye etkisi:

  Q = U × A × LMTD
  LMTD ∝ (T_proses - T_hava)

  T_hava artarsa → LMTD azalır → Q azalır

Yaklaşık etki:
  Her 1°C hava sıcaklığı artışı → %2-4 kapasite düşüşü
  (yaklaşma sıcaklığına bağlı)

Yüksek ortam sıcaklığı telafi yöntemleri:
  1. Daha büyük yüzey alanı (aşırı tasarım)
  2. Daha fazla fan gücü (daha yüksek hava hızı)
  3. Su spreyi (evaporatif soğutma)
  4. VSD ile kontrol (düşük sıcaklıkta enerji tasarrufu)
```

## Gürültü Kontrol Gereksinimleri

| Mesafe | Hedef Gürültü (dBA) | Tipik ACHE (dBA) | Azaltma Gereksinimi |
|--------|---------------------|-------------------|---------------------|
| 1 m (fan) | — | 90-105 | — |
| 10 m | <85 (işçi güvenliği) | 70-85 | Düşük hızlı fan, VSD |
| 50 m | <65 (endüstriyel sınır) | 55-70 | Fan hız kontrolü |
| 100 m | <55 (yerleşim sınırı) | 45-60 | Düşük gürültü fan, bariyer |
| 200 m | <45 (gece sınırı) | 35-50 | Özel tasarım gerekli |

### Gürültü Azaltma Yöntemleri

| Yöntem | Azaltma (dBA) | Maliyet Etkisi |
|--------|-------------|----------------|
| VSD ile düşük devir | 10-20 | Yüksek yatırım, düşük işletme |
| Geniş çaplı, düşük hızlı fan | 5-10 | Daha büyük yapı |
| Tip FRP (fiberglas) bıçak | 3-5 | Orta |
| Gürültü bariyeri/duvar | 5-15 | Orta-Yüksek |
| Giriş/çıkış silencer | 3-8 | Düşük-Orta |

## API 661 Standardı

API 661 (Air-Cooled Heat Exchangers for General Refinery Service), rafineri ve petrokimya endüstrisinde ACHE tasarımı için temel standarttır.

### API 661 Temel Gereksinimleri

| Gereksinim | Detay |
|-----------|-------|
| Yapısal tasarım | Rüzgar yükü: minimum 150 km/h |
| Minimum boru et kalınlığı | BWG 14 (2.11 mm) karbon çelik |
| Minimum kanat kalınlığı | 0.40 mm (alüminyum) |
| Fan ucu boşluğu | <%1 fan çapı |
| Titreşim limiti | <2.5 mm/s (RMS hız) |
| Gürültü sınırı | 85 dBA @ 1 m (API varsayımı) |
| Korozyon payı | Minimum 3 mm (karbon çelik) |
| Test basıncı | 1.5 × tasarım basıncı |

## Exergy Analizi — Hava Soğutmalı Eşanjör

### Exergy Dengesi

```
Giriş exergyleri:
  Ex_proses,in : Sıcak proses akışkanı giriş exergysi (kW)
  Ex_fan       : Fan elektrik gücü (saf exergy) (kW)

Çıkış exergyleri:
  Ex_proses,out : Soğutulmuş proses akışkanı çıkış exergysi (kW)
  Ex_hava,out   : Isınan havanın exergysi (genellikle ihmal edilebilir düşük)

Exergy verimi:
  η_ex = (Ex_proses,in - Ex_proses,out) / (Ex_proses,in - Ex_proses,out + Ex_fan)

  Veya daha kullanışlı tanım:
  η_ex = Ex_soğutma_işi / (Ex_fan + Ex_yıkım + Ex_kayıp)

Exergy yıkım kaynakları:
  1. Sonlu sıcaklık farkı (proses-hava): %60-80
  2. Fan gücü (mekanik-termal dönüşüm): %15-30
  3. Çevre kaybı: %5-10
```

### Tipik Exergy Verimi

| Servis | Proses Sıcaklığı | Exergy Verimi (%) | Not |
|--------|-------------------|-------------------|-----|
| Gaz soğutma (yüksek sıcaklık) | 150-300°C | 30-50 | Yüksek exergy kalitesi |
| Sıvı soğutma (orta sıcaklık) | 60-150°C | 20-40 | Orta exergy kalitesi |
| Sıvı soğutma (düşük sıcaklık) | 40-60°C | 10-25 | Düşük exergy, yüksek fan payı |
| Yoğuşma | 40-100°C | 15-35 | Faz değişimi + düşük ΔT mümkün |

### ACHE vs Su Soğutmalı Exergy Karşılaştırması

```
1,000 kW soğutma yükü karşılaştırması:

Su soğutmalı S&T:
  Fan gücü (soğutma kulesi) : 8 kW
  Pompa gücü                : 12 kW
  Toplam yardımcı güç       : 20 kW
  U değeri                  : 800 W/(m²·K)
  ΔT_lm                     : 8°C
  Exergy verimi             : 50-65%

Hava soğutmalı (ACHE):
  Fan gücü                  : 15 kW
  Pompa gücü                : 0 kW (hava tarafı)
  Toplam yardımcı güç       : 15 kW
  U değeri                  : 80 W/(m²·K)
  ΔT_lm                     : 25°C
  Exergy verimi             : 25-40%

Not: ACHE daha düşük exergy verimine sahip (büyük ΔT)
     ancak su tüketimi sıfır (su exergysi hesaba katılırsa fark azalır)
```

## Hava Tarafı Kirlenme ve Temizlik

| Kirlenme Türü | Kaynak | Kapasite Etkisi | Temizlik Yöntemi |
|---------------|--------|-----------------|------------------|
| Toz birikimi | Çevre, endüstriyel | %5-15 | Hava ile üfleme, su yıkama |
| Yağlı toz | Rafineri, fabrika | %10-25 | Sıcak su + deterjan |
| Pamuk/lif | Tekstil, tarım | %15-30 | Mekanik temizlik, vakumlama |
| Kavak tüyü/böcek | Mevsimsel | %5-20 | Su yıkama, koruyucu filtre |
| Kireç/mineral | Su spreyi (evaporatif) | %10-20 | Asidik yıkama |
| Buz | Kış ayları | %20-50 | Anti-icing çalışma, VSD |

### Temizlik Sıklığı ve Enerji Etkisi

```
Kirlenme ile enerji etkisi:

  Q_kirli = Q_temiz × (1 - kirlenme_faktörü)

  Kompanzasyon: Fan hızı artışı
  P_fan,kirli = P_fan,temiz × (Q_temiz / Q_kirli)^x   burada x ≈ 2-3

  Örnek:
    %20 kirlenme → Q %80'e düşer
    Kompanzasyon için fan gücü: (1/0.8)^2.5 ≈ 1.75× → %75 fan gücü artışı

  Yıllık temizlik maliyeti: 500-3,000 EUR/ünite
  Kirlenme kaynaklı ek enerji maliyeti: 2,000-15,000 EUR/yıl
  → Düzenli temizlik ekonomiktir
```

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Gövde-boru eşanjör: `heat_exchanger/equipment/shell_and_tube.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Soğutma kulesi (alternatif): `chiller/equipment/cooling_tower.md`

## Referanslar

- API Standard 661 (2013). *Air-Cooled Heat Exchangers for General Refinery Service*, 7th Edition, American Petroleum Institute.
- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- ESDU (Engineering Sciences Data Unit) 86018. *Performance of Air-Cooled Heat Exchangers*.
- Mukherjee, R. (1997). "Does Your Application Need an Air-Cooled Heat Exchanger?," *Hydrocarbon Processing*, 76(4).
- Ganapathy, V. (2003). *Industrial Boilers and Heat Recovery Steam Generators*, Marcel Dekker.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- ASHRAE Handbook — HVAC Systems and Equipment (2024), Chapter 40: Air-Cooled Condensers.
- EN 1216:1999 — Heat exchangers — Forced convection air cooling and air heating coils.
