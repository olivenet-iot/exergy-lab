---
title: "Reküperatörler ve Rejeneratörler (Recuperators and Regenerators)"
category: equipment
equipment_type: heat_exchanger
subtype: "Reküperatör/Rejeneratör"
keywords: [reküperatör, recuperator, rejeneratör, regenerator, yüksek sıcaklık, atık ısı, fırın, seramik, metalik]
related_files: [heat_exchanger/formulas.md, heat_exchanger/benchmarks.md, heat_exchanger/equipment/systems_overview.md, heat_exchanger/equipment/air_preheater.md]
use_when: ["Yüksek sıcaklık atık ısı geri kazanımı değerlendirilirken", "Fırın ve fırın reküperatör analizi yapılırken", "Seramik rejeneratör seçimi gerektiğinde"]
priority: medium
last_updated: 2026-02-01
---
# Reküperatörler ve Rejeneratörler — Recuperators and Regenerators

> Son güncelleme: 2026-02-01

## Genel Bilgiler

Reküperatörler ve rejeneratörler, yüksek sıcaklık endüstriyel proseslerden (fırınlar, ocaklar, cam üretimi, metalürji) kaynaklanan baca gazı atık ısısını geri kazanmak için kullanılan ısı eşanjörleridir. Bu cihazlar genellikle 400°C'nin üzerindeki sıcaklıklarda çalışır ve yanma havasını ön ısıtarak %20-50 yakıt tasarrufu sağlayabilir.

- Çalışma sıcaklığı: 400-1,400°C (baca gazı giriş)
- Ön ısıtılmış hava sıcaklığı: 200-1,000°C
- Kapasite aralığı: 10 kW - 50 MW
- Tipik yakıt tasarrufu: %10-40
- Tipik exergy verimi: 35-70% (yüksek sıcaklıklarda daha yüksek)

## Terminoloji: Reküperatör vs Rejeneratör

### Temel Fark

| Özellik | Reküperatör (Recuperator) | Rejeneratör (Regenerator) |
|---------|--------------------------|---------------------------|
| Çalışma prensibi | Sürekli ısı transferi (rekuperatif) | Döngüsel ısı depolama/salma (rejeneratif) |
| Isı transferi | Duvar aracılığıyla (sıcak → soğuk) | Depolama matrisine → matrisden soğuğa |
| Akışkan teması | Eşzamanlı, ayrı kanallar | Ardışık, aynı kanal |
| Sızıntı | Yok (sızdırmaz duvar) | Olası (geçiş anında karışma) |
| Yapı | Metal veya seramik duvar | Seramik veya metal dolgu/matris |
| Sıcaklık sınırı | 1,100°C (metalik), 1,400°C+ (seramik) | 1,400°C+ (seramik rejeneratör) |
| Kompaktlık | Orta | Büyük (iki oda gerekli) |
| Yanıt hızı | Anlık (sürekli) | Döngüsel (geçiş süresi) |
| Tipik uygulama | Endüstriyel fırınlar, brülörler | Cam fırınları, çelik Cowper |

## Metalik Reküperatörler

### Radyasyon Reküperatörü

Yüksek sıcaklık baca gazından ısı transferinin büyük bölümü ışınım (radyasyon) ile gerçekleşir.

```
Radyasyon reküperatörü yapısı:

  ┌─────────────────────┐
  │ Dış boru (hava)     │
  │  ┌───────────────┐  │
  │  │ İç boru       │  │
  │  │ (baca gazı)   │  │
  │  │  800-1100°C   │  │
  │  └───────────────┘  │
  │  Hava 400-700°C →→  │
  └─────────────────────┘

  İç boru: Baca gazı (sıcak) — yüksek sıcaklık alaşımı
  Dış boru: Yanma havası (soğuk)
  Isı transferi: %60-80 radyasyon + %20-40 konveksiyon

Radyasyon ısı transferi:
  Q_rad = ε × σ × A × (T_baca⁴ - T_duvar⁴)

Burada:
  ε    : Efektif yayınım katsayısı (0.6-0.9)
  σ    : Stefan-Boltzmann sabiti (5.67 × 10⁻⁸ W/(m²·K⁴))
  T    : Mutlak sıcaklık (K)
  A    : Isı transfer alanı (m²)
```

### Konveksiyon Reküperatörü

Daha düşük sıcaklıklarda (400-800°C) konvektif ısı transferi dominant olur.

```
Konveksiyon reküperatörü:

  Tipik yapılar:
    1. Boru demetli (tube bundle) — gövde-boru benzeri
    2. Plakalı (plate type) — paralel plakalar
    3. Kanatlı boru (finned tube) — düşük sıcaklıkta

  Isı transfer katsayısı:
    Baca gazı tarafı (konveksiyon): h = 30-100 W/(m²·K)
    Hava tarafı: h = 20-80 W/(m²·K)
    Toplam U: 15-50 W/(m²·K) (gaz/gaz)

  Kanatlı boru ile:
    Efektif U: 40-120 W/(m²·K)
```

### Kombine Radyasyon-Konveksiyon Reküperatörü

```
İki bölümli reküperatör:

  BACA GAZI 1000°C →→→ [RADYASİYON BÖLÜMÜ] →→→ 600°C →→→ [KONVEKSİYON BÖLÜMÜ] →→→ 300°C

  Hava 200°C ←←← [KONVEKSİYON BÖLÜMÜ] ←←← 400°C ←←← [RADYASİYON BÖLÜMÜ] ←←← 700°C

  Radyasyon bölümü: T_baca > 800°C, yüksek sıcaklık alaşımı
  Konveksiyon bölümü: T_baca < 800°C, karbon çelik veya düşük alaşım
  Bu kombinasyon en yüksek verimliliği en düşük maliyetle sağlar
```

### Metalik Reküperatör Malzemeleri

| Malzeme | Maks Sürekli Sıcaklık (°C) | Korozyon Direnci | Göreceli Maliyet |
|---------|---------------------------|------------------|------------------|
| Karbon çelik | 400 | Düşük | 1× |
| Cr-Mo alaşım (1.25Cr-0.5Mo) | 550 | Orta | 1.5× |
| SS304 (18Cr-8Ni) | 800 | İyi | 4× |
| SS309/310 (25Cr-20Ni) | 1,000 | Çok iyi | 6× |
| Inconel 600 (Ni-Cr) | 1,100 | Mükemmel | 15× |
| Inconel 601 | 1,150 | Mükemmel | 18× |
| RA330 (Fe-Ni-Cr) | 1,100 | Çok iyi | 12× |
| Haynes 230 (Ni-Cr-W-Mo) | 1,150 | Mükemmel | 25× |
| SiC (silisyum karbür) | 1,400 | Mükemmel | 30×+ |

### Metalik Reküperatör Arıza Modları

| Arıza Modu | Sıcaklık Aralığı | Önleme |
|------------|-------------------|--------|
| Oksidasyon | >600°C (CS) | Yüksek Cr alaşım |
| Kreep (sürünme) | >0.4 × T_erime | Kalın et, düşük gerilme |
| Termal yorulma | Çevrimsel çalışma | Genleşme bağlantıları, esnek tasarım |
| Sülfürizasyon | >400°C, S içeren gaz | Yüksek Cr-Ni alaşım |
| Karburizing (karbürleme) | >500°C, CO/CH₄ ortam | Yüksek Ni alaşım |
| Erozyon | Yüksek hızlı partikül | Hız sınırlama, kalın et |

## Seramik Rejeneratörler

### Çalışma Prensibi

```
Seramik rejeneratör çalışma döngüsü (iki odalı):

  Döngü 1 (ODA A: Isıtma, ODA B: Soğutma):
    ODA A: Sıcak baca gazı → seramik dolguyu ısıtır → soğuk gaz çıkışı
    ODA B: Soğuk yanma havası → sıcak seramik dolgudan ısı alır → ön ısıtılmış hava

  Döngü 2 (ODA A: Soğutma, ODA B: Isıtma):
    ODA A: Soğuk yanma havası → sıcak seramik dolgudan ısı alır → ön ısıtılmış hava
    ODA B: Sıcak baca gazı → seramik dolguyu ısıtır → soğuk gaz çıkışı

  Geçiş süresi: 20-120 saniye (uygulamaya bağlı)
  Geçiş sırasında kısa süre karışma olur → hava sızıntısı eşdeğeri

  Termal verimlilik:
    Yüksek NTU (büyük termal kütle) → %85-95 hava ön ısıtma verimi
```

### Seramik Malzemeler

| Malzeme | Maks Sıcaklık (°C) | Isı Kapasitesi (kJ/(kg·K)) | Yoğunluk (kg/m³) | Uygulama |
|---------|---------------------|---------------------------|------------------|----------|
| Alümina (Al₂O₃) | 1,700 | 0.78 | 3,900 | Çelik Cowper, cam fırını |
| Mullit (3Al₂O₃·2SiO₂) | 1,600 | 0.80 | 2,800 | Cam fırını, seramik |
| Kordierit (2MgO·2Al₂O₃·5SiO₂) | 1,300 | 0.90 | 2,100 | Otomotiv katalizör, küçük fırın |
| Silika (SiO₂) tuğla | 1,500 | 0.80 | 1,800 | Çelik Cowper üst bölge |
| Magnezit (MgO) | 1,800 | 1.00 | 3,500 | Çok yüksek sıcaklık |
| SiC (silisyum karbür) | 1,400 (oksidatif) | 0.75 | 3,100 | Yüksek iletkenlik gereken |

### Seramik Dolgu Geometrileri

| Geometri | Alan Yoğunluğu (m²/m³) | ΔP | Isı Kapasitesi | Uygulama |
|----------|------------------------|-----|---------------|----------|
| Tuğla yığını (brick checker) | 20-50 | Düşük | Çok yüksek | Cowper (çelik) |
| Bal peteği (honeycomb) | 200-600 | Düşük | Orta | Modern cam fırını |
| Rastgele dolgu (saddle, ball) | 50-200 | Yüksek | Yüksek | Eski tip |
| Yapılandırılmış dolgu | 100-400 | Orta | Orta | Modern tasarımlar |

## Yüksek Sıcaklık Endüstriyel Uygulamalar

### Uygulama Tablosu

| Sektör | Uygulama | Baca Gazı Sıcaklığı (°C) | Tip | Yakıt Tasarrufu (%) |
|--------|----------|--------------------------|-----|---------------------|
| Çelik | Cowper (yüksek fırın) | 1,200-1,400 | Seramik rejeneratör | %25-35 |
| Çelik | Hadde fırını | 800-1,200 | Metalik/seramik reküperatör | %15-30 |
| Çelik | Tav fırını | 600-1,000 | Metalik reküperatör | %15-25 |
| Cam | Eritme fırını | 1,200-1,500 | Seramik rejeneratör | %30-50 |
| Cam | Tavlama fırını | 500-700 | Metalik reküperatör | %15-25 |
| Alüminyum | Ergitme fırını | 700-1,100 | Metalik reküperatör | %15-30 |
| Seramik | Tünel fırın | 800-1,300 | Metalik/seramik | %20-35 |
| Çimento | Klinker fırını | 800-1,100 | Seramik rejeneratör | %15-25 |
| Kireç | Kireç fırını | 600-1,000 | Metalik reküperatör | %15-25 |
| Dövme | Dövme fırını | 800-1,200 | Metalik reküperatör | %20-35 |
| Isıl işlem | Sertleştirme fırını | 600-1,000 | Metalik reküperatör | %15-25 |

### Rejeneratif Brülör Sistemi

```
Rejeneratif brülör (regenerative burner) konsepti:

  Brülör çifti (A ve B):

  Döngü 1:
    Brülör A: YANAR → sıcak baca gazı → Brülör B'den çıkar
    Brülör B: KAÇAR → seramik matris ısınır (1,000°C+)

  Döngü 2 (15-60 saniye sonra geçiş):
    Brülör B: YANAR → sıcak baca gazı → Brülör A'dan çıkar
    Brülör A: KAÇAR → ön ısıtılmış hava Brülör B'ye gider

  Hava ön ısıtma: %85-95 baca gazı sıcaklığına ulaşılabilir
  Baca gazı giriş: 1,000-1,300°C
  Ön ısıtılmış hava: 900-1,200°C
  Baca gazı çıkış: 100-200°C

  Yakıt tasarrufu: %30-50 (geleneksele göre)
  NOx riski: Yüksek hava sıcaklığı → yüksek alev sıcaklığı → yüksek NOx
  Çözüm: Flameless combustion (FLOX), düşük NOx brülör tasarımı
```

## Exergy Analizi — Yüksek Sıcaklık Uygulamalar

### Yüksek Sıcaklıkta Exergy Kalitesi

```
Exergy ve sıcaklık ilişkisi:

  Carnot faktörü (exergy kalitesi):
    η_Carnot = 1 - T₀/T

  Sıcaklığa göre exergy kalitesi:
    200°C (473 K): η_Carnot = 1 - 298/473 = 0.37 → %37
    500°C (773 K): η_Carnot = 1 - 298/773 = 0.61 → %61
    800°C (1073 K): η_Carnot = 1 - 298/1073 = 0.72 → %72
    1000°C (1273 K): η_Carnot = 1 - 298/1273 = 0.77 → %77
    1200°C (1473 K): η_Carnot = 1 - 298/1473 = 0.80 → %80

  Yorum: Yüksek sıcaklık atık ısı YÜKSEK exergy kalitesindedir
         → Geri kazanım exergy açısından çok değerli
         → Kaçırılan atık ısı büyük exergy yıkımıdır
```

### Reküperatör/Rejeneratör Exergy Verimi

```
Exergy verimi:

  η_ex = (Ex_hava,çıkış - Ex_hava,giriş) / (Ex_baca,giriş - Ex_baca,çıkış)

İdeal gaz yaklaşımı:
  Ex = m × cp × [(T - T₀) - T₀ × ln(T/T₀)]

Tipik exergy verimleri:

  Metalik reküperatör (600-1000°C baca gazı):
    Hava 200-500°C'ye ön ısıtılırsa: η_ex = 40-60%
    Hava 500-800°C'ye ön ısıtılırsa: η_ex = 50-70%

  Seramik rejeneratör (1000-1400°C baca gazı):
    Hava 800-1200°C'ye ön ısıtılırsa: η_ex = 55-75%

  Rejeneratif brülör (1000-1300°C):
    Hava 900-1200°C'ye ön ısıtılırsa: η_ex = 60-80%

Karşılaştırma:
  Reküperatörsüz fırın: Baca gazı exergysi tamamen kayıp → η_ex,geri_kazanım = 0%
  Metalik reküperatör: %40-70 atık exergy geri kazanılır
  Seramik rejeneratör: %55-80 atık exergy geri kazanılır
```

### Exergy Yıkım Kaynakları

| Kaynak | Metalik Reküperatör | Seramik Rejeneratör |
|--------|--------------------|--------------------|
| Sonlu ΔT (dominant) | %50-70 | %30-50 |
| Basınç düşüşü | %5-10 | %5-15 |
| Sızıntı/karışma | %0 | %5-15 |
| Çevre kaybı (izolasyon) | %5-15 | %5-10 |
| Döngü kayıpları | %0 | %5-10 |
| Kirlenme/birikme | %5-15 | %5-15 |

## Ekonomik Analiz

### Yatırım Maliyeti

| Tip | Kapasite (kW) | Maks Sıcaklık | Maliyet (EUR) | EUR/kW |
|-----|-------------|---------------|---------------|--------|
| Konveksiyon reküperatör (CS) | 200 | 500°C | 10,000-25,000 | 50-125 |
| Konveksiyon reküperatör (SS) | 200 | 800°C | 20,000-50,000 | 100-250 |
| Radyasyon reküperatör (Ni alaşım) | 500 | 1,100°C | 60,000-150,000 | 120-300 |
| Kombine reküperatör | 1,000 | 1,000°C | 80,000-200,000 | 80-200 |
| Seramik rejeneratör (küçük) | 500 | 1,400°C | 80,000-200,000 | 160-400 |
| Rejeneratif brülör çifti | 500 | 1,300°C | 40,000-100,000 | 80-200 |
| Seramik rejeneratör (büyük) | 10,000 | 1,400°C | 500,000-2,000,000 | 50-200 |

### Geri Ödeme Hesabı

```
Reküperatör geri ödeme örneği:

  Fırın: 2,000 kW doğalgaz tüketimi
  Baca gazı sıcaklığı: 800°C
  Reküperatör sonrası baca gazı: 350°C
  Hava ön ısıtma: 25°C → 500°C

  Enerji geri kazanımı:
    Q_geri = m_hava × cp × (500-25) = ~600 kW
    Yakıt tasarrufu: 600/2000 = %30

  Yıllık tasarruf:
    Çalışma saati: 6,000 h/yıl
    Doğalgaz fiyatı: 0.35 EUR/m³, LHV: 9.58 kWh/m³
    Yıllık yakıt tasarrufu: 600 × 6,000 / 9.58 = 375,783 kWh = 39,224 m³
    Yıllık maliyet tasarrufu: 39,224 × 0.35 = 13,728 EUR/yıl

  Yatırım: 60,000 EUR (montaj dahil)
  Geri ödeme: 60,000 / 13,728 = 4.4 yıl
```

## Ölçülmesi Gereken Parametreler

| Parametre | Birim | Tipik Aralık | Nasıl Ölçülür |
|-----------|-------|--------------|---------------|
| Baca gazı giriş sıcaklığı | °C | 400-1,400 | Termoeleman (K, S veya B tipi) |
| Baca gazı çıkış sıcaklığı | °C | 100-500 | Termoeleman (K tipi) |
| Hava giriş sıcaklığı | °C | 0-35 | Termoeleman veya PT100 |
| Hava çıkış sıcaklığı | °C | 200-1,200 | Termoeleman (K veya S tipi) |
| Baca gazı debisi | Nm³/h veya kg/s | Sisteme bağlı | Pitot tüpü, ultrasonik |
| Hava debisi | Nm³/h veya kg/s | Sisteme bağlı | Venturi, orifis |
| Baca gazı bileşimi (O₂, CO, CO₂) | % | Yakıta bağlı | Gaz analizörü |
| Basınç düşüşü (her taraf) | Pa | 50-1,000 | Diferansiyel basınç |

## İlgili Dosyalar

- Genel bakış: `heat_exchanger/equipment/systems_overview.md`
- Hava ön ısıtıcı: `heat_exchanger/equipment/air_preheater.md`
- Ekonomizer: `heat_exchanger/equipment/economizer.md`
- Formüller: `heat_exchanger/formulas.md`
- Benchmark verileri: `heat_exchanger/benchmarks.md`
- Kazan hava ön ısıtıcı: `boiler/solutions/air_preheater.md`
- Çelik sanayi: `factory/sector_metal.md`
- Çimento sanayi: `factory/sector_cement.md`

## Referanslar

- Trinks, W. et al. (2004). *Industrial Furnaces*, 6th Edition, Wiley.
- Mullinger, P. & Jenkins, B. (2014). *Industrial and Process Furnaces: Principles, Design and Operation*, 2nd Edition, Butterworth-Heinemann.
- Kakaç, S., Liu, H., Pramuanjaroenkij, A. (2020). *Heat Exchangers: Selection, Rating, and Thermal Design*, 4th Edition, CRC Press.
- Shah, R.K. & Sekulić, D.P. (2003). *Fundamentals of Heat Exchanger Design*, John Wiley & Sons.
- Kotas, T.J. (1995). *The Exergy Method of Thermal Plant Analysis*, Krieger Publishing.
- Bejan, A., Tsatsaronis, G., Moran, M. (1996). *Thermal Design and Optimization*, Wiley.
- Baukal, C.E. (2000). *Heat Transfer in Industrial Combustion*, CRC Press.
- U.S. DOE/AMO (2008). *Waste Heat Recovery: Technology and Opportunities in U.S. Industry*.
- EN 746 — Industrial Thermoprocessing Equipment.
- ASME PTC 4 — Fired Steam Generators: Performance Test Codes.
- Hasanbeigi, A. et al. (2010). "Energy-Efficiency Improvement Opportunities for the Cement Industry," Lawrence Berkeley National Laboratory.
