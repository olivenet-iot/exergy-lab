# Proses Entegrasyonu (Process Integration)

> Son güncelleme: 2026-01-31

## Genel Bakış

Proses entegrasyonu, bir fabrikanın tüm proseslerini bütünleşik bir sistem olarak ele alarak enerji, su ve hammadde kullanımını minimize etmeyi amaçlayan sistematik bir metodoloji ailesidir. Isı entegrasyonunun (pinch analizi) ötesine geçerek kütle entegrasyonu, su pinch analizi, hidrojen pinch, toplam tesis entegrasyonu ve kesikli proses entegrasyonunu kapsar. Doğru uygulandığında, yalnızca ısı entegrasyonuna kıyasla %20-40 daha fazla tasarruf potansiyeli ortaya çıkar.

## 1. Entegrasyon Hiyerarşisi (Integration Hierarchy)

### 1.1 Onion Modeli (Öncelik Sırası)

Proses entegrasyonunda en içten dışa doğru optimize edilmelidir:

```
Öncelik sırası (en yüksekten en düşüğe):

1. Proses Değişikliği (Process Change)
   → Prosesin kendisini değiştir (sıcaklık, basınç, konsantrasyon)
   → En büyük tasarruf potansiyeli, en düşük yatırım (bazen)
   → Örnek: Boyama sıcaklığını 100°C → 80°C'ye düşürme

2. Isı Entegrasyonu (Heat Integration)
   → Prosesler arası ısı değişimi
   → Pinch analizi ile optimize et
   → Bkz: heat_integration.md

3. Yardımcı Sistem Optimizasyonu (Utility Optimization)
   → Buhar, basınçlı hava, soğutma suyu sistemlerini optimize et
   → Bkz: cross_equipment.md

4. Enerji Dönüşüm (Energy Conversion)
   → CHP, ORC, ısı pompası
   → Bkz: cogeneration.md, waste_heat_recovery.md

5. Dış Enerji Kaynağı (External Energy)
   → Yenilenebilir enerji, şebeke optimizasyonu
   → Son çare olarak fosil yakıt
```

### 1.2 Entegrasyon Fırsatları Tablosu (Proses Türüne Göre)

| Proses Tipi | Isı Entegrasyonu | Su Entegrasyonu | Kütle Entegrasyonu | Tipik Tasarruf |
|---|---|---|---|---|
| Gıda ve içecek | +++ | +++ | ++ | %15–30 |
| Tekstil (boyama/terbiye) | +++ | +++ | + | %20–35 |
| Kimya/petrokimya | +++ | ++ | +++ | %15–25 |
| Kağıt ve selüloz | +++ | +++ | ++ | %15–30 |
| Metal işleme | ++ | ++ | + | %10–20 |
| Otomotiv (boyahane) | ++ | +++ | + | %15–25 |
| Çimento | ++ | + | + | %5–15 |
| Cam | +++ | + | + | %10–20 |

```
+++ = Yüksek potansiyel
++  = Orta potansiyel
+   = Düşük potansiyel
```

## 2. Toplam Tesis Entegrasyonu (Total Site Integration)

### 2.1 Toplam Tesis Profilleri (Total Site Profiles)

Birden fazla proses birimi içeren büyük tesislerde, her prosesin ayrı ayrı pinch analizi yapılır, ardından site source ve site sink profilleri birleştirilir.

```
Total site entegrasyon adımları:

Adım 1: Her proses birimi için sıcak ve soğuk akışları tanımla
Adım 2: Her birim için bileşik eğrileri oluştur
Adım 3: Her birimin dış ısı ihtiyacını (utility) belirle
  - Pinch üstü: Dış ısı gereksinimi → Site sink profile
  - Pinch altı: Dış soğutma gereksinimi → Site source profile
Adım 4: Site source ve site sink profillerini birleştir
Adım 5: Buhar seviyelerini belirle (LP, MP, HP)
Adım 6: Total site pinch → minimum dış utility gereksinimi

Buhar seviyesi optimizasyonu:
- HP buhar (>10 bar): Yüksek sıcaklık prosesler
- MP buhar (3–10 bar): Orta sıcaklık prosesler
- LP buhar (1–3 bar): Düşük sıcaklık prosesler
- Her seviye arasında let-down station veya back-pressure türbin
```

### 2.2 Toplam Tesis Entegrasyonu Hesaplama Örneği

```
Kimya fabrikası — 3 proses birimi:

Birim A (Reaktör):
- Isı ihtiyacı (pinch üstü): 800 kW @ 180°C (MP buhar)
- Soğutma ihtiyacı (pinch altı): 600 kW @ 40°C

Birim B (Damıtma):
- Isı ihtiyacı: 1,200 kW @ 130°C (LP buhar)
- Soğutma ihtiyacı: 900 kW @ 35°C

Birim C (Kurutma):
- Isı ihtiyacı: 500 kW @ 200°C (HP/MP buhar)
- Soğutma ihtiyacı: 200 kW @ 50°C

Ayrı ayrı utility gereksinimi:
- Toplam ısıtma: 800 + 1,200 + 500 = 2,500 kW
- Toplam soğutma: 600 + 900 + 200 = 1,700 kW

Total site entegrasyonu sonrası:
- Birim A soğutma atığı (600 kW, 40°C) → düşük değer
- Birim C egzoz ısısı (200°C düşüşlü) → Birim B'ye aktarılabilir

Entegre utility gereksinimi:
- Toplam ısıtma: 2,100 kW (400 kW tasarruf, %16)
- Toplam soğutma: 1,300 kW (400 kW azaltma)
```

## 3. Su Pinch Analizi (Water Pinch Analysis)

### 3.1 Temel Prensipler

Su pinch analizi, bir tesisin minimum taze su ve atık su miktarını belirlemek ve su yeniden kullanımını (reuse/recycle) optimize etmek için kullanılır. Isı pinch analizinin su/kütle transferine uygulanmış halidir.

```
Su pinch analizi temel kavramları:

Kirletici konsantrasyonu bazlı analiz:
- Her su kullanıcı prosesinin giriş ve çıkış konsantrasyonu
- Kütle yükü (contaminant mass load): Δm = F × (C_out - C_in)
  F = su debisi [ton/h]
  C = konsantrasyon [ppm]

Minimum taze su (F_min):
Bileşik eğrilerin pinch noktasından belirlenir.

Minimum atık su (W_min):
Su dengesi: F_min = W_min + Kayıplar (buharlaşma vb.)
```

### 3.2 Su Pinch Hesaplama Örneği

```
Tekstil fabrikası — 3 su kullanım prosesi:

Proses 1 (Yıkama):
- Giriş konsantrasyonu (max): 20 ppm
- Çıkış konsantrasyonu: 100 ppm
- Kütle yükü: 2 kg/h
- Gerekli debi: 2,000 / (100 - 20) = 25 m³/h

Proses 2 (Boyama):
- Giriş konsantrasyonu (max): 50 ppm
- Çıkış konsantrasyonu: 200 ppm
- Kütle yükü: 3 kg/h
- Gerekli debi: 3,000 / (200 - 50) = 20 m³/h

Proses 3 (Durulama):
- Giriş konsantrasyonu (max): 0 ppm (taze su)
- Çıkış konsantrasyonu: 20 ppm
- Kütle yükü: 0.5 kg/h
- Gerekli debi: 500 / (20 - 0) = 25 m³/h

Mevcut durum (ayrı ayrı taze su):
Toplam taze su: 25 + 20 + 25 = 70 m³/h

Su pinch analizi sonrası (reuse):
- Proses 3 çıkışı (20 ppm) → Proses 1 girişine (max 20 ppm) ✓
- Proses 1 çıkışı (100 ppm) → Proses 2'ye kısmen (max 50 ppm)
  → Karıştırma: Taze su + P1 çıkışı → 50 ppm hedef

Optimizasyon sonucu:
- Minimum taze su: 45 m³/h (25 + 20 kısmi)
- Tasarruf: 70 - 45 = 25 m³/h (%36 azaltma)
- Minimum atık su: 45 m³/h (%36 azaltma)

Ekonomik etki:
- Su maliyeti: €2.5/m³ (taze su + atık su arıtma)
- Yıllık tasarruf: 25 × 8,000 × €2.5 = €500,000/yıl
- Yatırım (boru hattı, tank, pompa): ~€120,000
- SPP = 120,000 / 500,000 = 0.24 yıl (3 ay)
```

## 4. Kesikli Proses Entegrasyonu (Batch Process Integration)

### 4.1 Zamana Bağlı Isı Entegrasyonu

Kesikli proseslerde (gıda, ilaç, kimya, tekstil boyama) ısı kaynakları ve kullanıcıları aynı anda mevcut olmayabilir. Bu durumda termal enerji depolama (TES) veya üretim programı optimizasyonu gerekir.

```
Kesikli proses entegrasyon yaklaşımları:

Yaklaşım 1: Zaman dilimi analizi (Time Slice Analysis)
- Her zaman diliminde mevcut kaynak ve kullanıcıları eşleştir
- Eşleşemeyen ısıyı TES'te depola
- Sonraki dilimde TES'ten kullan

Yaklaşım 2: Üretim programı kaydırma (Schedule Shifting)
- Uyumlu prosesleri aynı zaman dilimine kaydır
- Kaynak ve kullanıcı eşzamanlılığını artır
- Depolama ihtiyacını azalt

Yaklaşım 3: Hibrit (TES + program kaydırma)
- Program kaydırma ile eşzamanlılığı artır
- Kalan uyumsuzluk için TES kullan
```

### 4.2 Kesikli Proses TES Boyutlandırma

```
TES boyutlandırma formülü:
E_TES = Q̇_kaynak × Δt_kaynak × η_TES [kWh]

Burada:
- Q̇_kaynak = ısı kaynağı gücü [kW]
- Δt_kaynak = kaynak mevcut olma süresi [saat]
- η_TES = depolama verimi [0.85–0.95]

Tank boyutu (su depolama):
V_tank = E_TES / (ρ × Cp × ΔT) [m³]

Örnek:
Q̇_kaynak = 200 kW, Δt = 4 saat, η_TES = 0.90
E_TES = 200 × 4 × 0.90 = 720 kWh

Tank boyutu (su, ΔT = 40°C):
V = 720 × 3,600 / (1,000 × 4.18 × 40) = 15.5 m³
→ 16 m³ izoleli tank gerekli
```

### 4.3 Kesikli Proses Zamanlama Optimizasyonu Örneği

```
Gıda fabrikası — Günlük üretim programı:

Mevcut program:
| Saat | Proses | Isı İhtiyacı | Isı Kaynağı |
|------|--------|-------------|-------------|
| 06–10 | Pastörizasyon | 300 kW | — |
| 08–12 | Pişirme | 200 kW | — |
| 10–14 | Soğutma (P1) | — | 250 kW |
| 12–16 | Yıkama | 100 kW (sıcak su) | — |
| 14–18 | Soğutma (P2) | — | 200 kW |
| 16–20 | CIP temizlik | 150 kW (sıcak su) | — |

Eşzamanlılık analizi:
06–10: 300 kW ihtiyaç, 0 kW kaynak → Eksik
10–12: 200 kW ihtiyaç, 250 kW kaynak → 50 kW fazla
12–14: 100 kW ihtiyaç, 250 kW kaynak → 150 kW fazla
14–16: 100 kW ihtiyaç, 200 kW kaynak → 100 kW fazla
16–18: 150 kW ihtiyaç, 200 kW kaynak → 50 kW fazla

Optimize edilmiş program (kaydırma + TES):
- 10–14 saatleri arasında 200 kW fazla ısıyı TES'te depola
- 06–10 saatlerinde TES'ten 100 kW kullan
- TES boyutu: 200 × 4 = 800 kWh → 17 m³ tank

Sonuç:
- Dış ısı ihtiyacı: 750 kW → 550 kW (%27 azalma)
- Yıllık yakıt tasarrufu: 550 × 0.27 × 6,000 / 0.90 × €0.045 = €44,550/yıl
  (kaba tahmin)
```

## 5. Kütle Entegrasyonu (Mass Integration)

### 5.1 Temel Kavramlar

Kütle entegrasyonu, proses akışlarındaki madde transferini optimize ederek hammadde tüketimini ve atık oluşumunu minimize eder.

```
Kütle entegrasyonu türleri:

1. Çözücü geri kazanımı: Kullanılmış çözücünün damıtma ile
   saflaştırılarak yeniden kullanımı
   → Kimya, boya, ilaç sektörleri

2. Proses suyu yeniden kullanımı: Bkz. Su pinch analizi (Bölüm 3)

3. Yan ürün değerlendirme: Bir prosesin atığı diğerinin hammaddesi
   → Endüstriyel simbiyoz kavramı

4. Hammadde minimizasyonu: Proses koşullarını değiştirerek
   daha az hammadde ile aynı ürünü elde etme
```

### 5.2 Endüstriyel Simbiyoz Örnekleri

| Kaynak Proses | Atık/Yan ürün | Kullanıcı Proses | Tasarruf |
|---|---|---|---|
| Enerji santrali | Uçucu kül | Çimento fabrikası | Hammadde %15–25 |
| Bira fabrikası | Spent grain | Hayvan yemi | Atık azaltma %60 |
| Rafineri | CO₂ gazı | Sera (CO₂ gübrelemesi) | Verimlilik %20–30 |
| Çelik fabrikası | Cüruf | Yol yapımı, çimento | Atık azaltma %80 |
| Gıda fabrikası | Organik atık | Biyogaz tesisi | Enerji geri kazanım |

## 6. Birleşik Enerji-Su Optimizasyonu (Combined Energy-Water)

### 6.1 Enerji-Su Bağıntısı

Birçok endüstriyel proseste enerji ve su tüketimi birbirine bağlıdır. Su tasarrufu enerji tasarrufu getirir ve tersi de geçerlidir.

```
Enerji-su etkileşimi:

1. Su ısıtma: Daha az su = daha az ısıtma enerjisi
   E_ısıtma = V_su × ρ × Cp × ΔT / η_kazan

2. Atık su arıtma: Daha az atık su = daha az arıtma enerjisi

3. Buhar üretimi: Kondensat geri dönüşü = hem su hem enerji tasarrufu
   Su tasarrufu: %60–80 azaltma
   Enerji tasarrufu: %10–15 (besleme suyu ön ısıtma etkisi)

4. Soğutma kulesi: Drift ve buharlaşma → su kaybı
   Su tasarrufu: VSD fan, dolgu iyileştirme

Birleşik optimizasyon formülü:
C_toplam = C_su × V_su + C_enerji × E_ısıtma + C_arıtma × V_atık_su
Minimize: C_toplam = f(V_su, E, V_atık)
```

### 6.2 Birleşik Optimizasyon Örneği

```
Tekstil fabrikası — Boyama prosesi:

Mevcut durum:
- Taze su: 50 m³/h, T = 15°C
- Boyama sıcaklığı: 90°C
- Isıtma enerjisi: 50 × 1,000 × 4.18 × (90-15) / 3,600 = 4,354 kW
- Atık su: 48 m³/h, T = 60°C

Su yeniden kullanımı + ısı geri kazanımı:
- Atık su → eşanjör → taze su ön ısıtma
- Atık su çıkış: 60°C → 35°C (25°C kurtarma)
- Taze su: 15°C → 38°C (23°C ısınma, η = 0.70)
- Isı tasarrufu: 50 × 1,000 × 4.18 × 23 / 3,600 = 1,335 kW

Su yeniden kullanımı (kısmen):
- 20 m³/h atık su → arıtma → yeniden kullanım
- Taze su: 50 → 30 m³/h (%40 azaltma)
- Isıtma enerjisi azaltımı: 20 × 1,000 × 4.18 × 75 / 3,600 = 1,742 kW
  (yeniden kullanılan su zaten sıcak)

Toplam tasarruf:
- Su: 20 m³/h × 8,000 h × €2.5 = €400,000/yıl
- Enerji: (1,335 + 1,742) × 8,000 / 1,000 / 0.90 × €0.045 = €1,223,600/yıl
  (Kontrol: Bu büyük bir fabrika senaryosu)
  Düzeltme: Mevsimsel kapasite kullanımı %60 ortalama
  Gerçek tasarruf: ~€733,000/yıl (enerji) + €400,000/yıl (su)
```

## 7. Proses Değişikliği ile Enerji Tasarrufu (Process Modification)

### 7.1 Proses Değişikliği Fırsatları

| Sektör | Proses Değişikliği | Enerji Tasarrufu | Ek Fayda |
|---|---|---|---|
| Tekstil | Düşük sıcaklık boyama (100→60°C) | %30–50 ısı | Su tasarrufu %20 |
| Gıda | Membran filtrasyon (damıtma yerine) | %40–60 | Ürün kalitesi artışı |
| Kimya | Reaktif damıtma | %20–40 | Ekipman azaltımı |
| Kağıt | Kapalı su döngüsü | %15–25 ısı | Su %50 azaltma |
| Metal | Düşük sıcaklık kaplama | %20–30 | Kimyasal azaltma |
| Gıda | UHT yerine HPP (yüksek basınç) | %50–70 | Besin değeri korunur |

### 7.2 Proses Yoğunlaştırma (Process Intensification)

```
Proses yoğunlaştırma kavramı:
Daha küçük ekipmanla aynı veya daha iyi sonuç elde etme.

Örnekler:
1. Mikro reaktör: Geleneksel reaktörün 1/100 boyutunda,
   daha iyi ısı transferi → daha az enerji

2. Rotary heat exchanger: Geleneksel shell-tube'un 1/5 boyutunda

3. Hibrit sistemler: Membran + damıtma birleşimi

4. Ters ozmoz (RO): Buharlaştırma yerine, %90 enerji tasarrufu

Enerji tasarruf potansiyeli: %30–80 (uygulamaya göre)
Yatırım: Genellikle düşer (daha küçük ekipman)
Risk: Yeni teknoloji riski (kanıtlanmamış olabilir)
```

## 8. Performans Sınıflandırması (Proses Entegrasyonu)

| Performans Kriteri | Düşük | Ortalama | İyi | Mükemmel |
|---|---|---|---|---|
| Isı entegrasyon oranı | <%15 | %15–30 | %30–50 | >%50 |
| Su yeniden kullanım oranı | <%10 | %10–30 | %30–50 | >%50 |
| Proses değişikliği uygulaması | Yok | 1–2 proses | 3–5 proses | >5 proses |
| Toplam tesis entegrasyonu | Yok | Kısmi | Tam | Tam + CHP |
| Yıllık tasarruf (toplam enerji) | <%5 | %5–15 | %15–25 | >%25 |

| Entegrasyon Olgunluk Seviyesi | Düşük | Ortalama | İyi | Mükemmel | Kritik |
|---|---|---|---|---|---|
| Pinch analizi yapılmış mı? | Hayır | Basit | Detaylı | Detaylı + uygulama | — |
| Su pinch yapılmış mı? | Hayır | Basit | Detaylı | Detaylı + uygulama | — |
| TES kullanımı | Yok | Basit tank | Optimze tank | PCM/gelişmiş | — |
| Proses kontrol seviyesi | Manuel | Yarı otomatik | Otomatik | AI tabanlı | Manuel+eski |

## 9. ExergyLab Platformunda Proses Entegrasyonu

### 9.1 Platform Proses Entegrasyon Algoritması

```
ExergyLab proses entegrasyon değerlendirmesi:

1. Ekipman veri girişinden proses akışlarını tanımla
   - Kazan verileri → buhar üretim/dağıtım profili
   - Kompresör verileri → basınçlı hava profili
   - Chiller verileri → soğutma yükü profili
   - Pompa verileri → su dağıtım profili

2. Çapraz ekipman entegrasyon fırsatlarını tara
   → cross_equipment.md algoritması

3. Isı entegrasyon potansiyelini değerlendir
   → heat_integration.md kaynak-kullanım eşleştirmesi

4. WHR teknoloji önerilerini oluştur
   → waste_heat_recovery.md teknoloji seçimi

5. Ekonomik değerlendirme ve önceliklendirme
   → economic_analysis.md yatırım analizi
```

## İlgili Dosyalar

- [Isı Entegrasyonu](heat_integration.md) — Pinch analizi ve kaynak-kullanım eşleştirme
- [Atık Isı Geri Kazanım](waste_heat_recovery.md) — WHR teknoloji detayları
- [Kojenerasyon](cogeneration.md) — CHP/CCHP proses entegrasyonu
- [Ekipmanlar Arası Optimizasyon](cross_equipment.md) — Çapraz ekipman entegrasyon fırsatları
- [Ekonomik Analiz](economic_analysis.md) — Yatırım analizi
- [Enerji Yönetimi](energy_management.md) — ISO 50001 entegrasyon
- [Kazan Çözümleri](../boiler/solutions/) — Kazan tarafı proses iyileştirmeleri
- [Kompresör Çözümleri](../compressor/solutions/) — Basınçlı hava sistemi optimizasyonu
- [Chiller Çözümleri](../chiller/solutions/) — Soğutma sistemi entegrasyonu
- [Sistem Sınırları](system_boundaries.md) — Proses sınır tanımları
- [Exergy Temelleri](exergy_fundamentals.md) — Proses exergy analizi

## Referanslar

- Linnhoff, B. et al., "A User Guide on Process Integration for the Efficient Use of Energy," IChemE, 1982
- Kemp, I.C., "Pinch Analysis and Process Integration," Butterworth-Heinemann, 2nd Edition, 2007
- El-Halwagi, M.M., "Sustainable Design Through Process Integration," Butterworth-Heinemann, 2nd Edition, 2017
- Klemeš, J.J. (Ed.), "Handbook of Process Integration (PI)," Woodhead Publishing, 2013
- Wang, Y.P. & Smith, R. (1994), "Wastewater minimization," Chemical Engineering Science, 49(7), 981-1006
- Manan, Z.A. et al. (2004), "Targeting the minimum water flow rate using water cascade analysis technique," AIChE Journal, 50(12)
- Majozi, T., "Batch Chemical Process Integration," Springer, 2010
- Stankiewicz, A.I. & Moulijn, J.A. (2000), "Process Intensification: Transforming Chemical Engineering," Chemical Engineering Progress, 96(1)
- European Commission, "Reference Document on Best Available Techniques for Energy Efficiency," 2009
- IEA, "Energy Technology Perspectives — Industrial Sector," 2020
