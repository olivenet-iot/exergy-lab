---
title: "Yük Eşleştirme ve Operasyon Optimizasyonu — Load Matching & Operation Optimization"
category: solutions
equipment_type: steam_turbine
keywords: [yük eşleştirme, thermal load matching, electrical load matching, dispatch optimizasyonu, sliding pressure, peak shaving, multi-turbine sequencing, mevsimsel operasyon, CHP]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/solutions/efficiency_improvement.md, steam_turbine/systems/steam_turbine_chp.md, steam_turbine/economics/feasibility.md, factory/cross_equipment.md, factory/prioritization.md]
use_when: ["Türbin kısmi yükte çalışırken", "CHP termal-elektrik dengesi sorgulandığında", "Mevsimsel yük değişimi analiz edilirken", "Çoklu türbin sıralaması optimize edilirken"]
priority: high
last_updated: 2026-01-31
---
# Yük Eşleştirme ve Operasyon Optimizasyonu — Load Matching & Operation Optimization

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Buhar türbini CHP sistemlerinde termal yük ve elektrik yükü nadiren eşzamanlı olarak tasarım noktasında olur. Mevsimsel değişimler, vardiya düzenleri ve proses dalgalanmaları nedeniyle türbin sıklıkla kısmi yükte çalışır — bu da verim düşüşüne ve exergy yıkımının artmasına neden olur.

**Çözüm:** Termal/elektrik yük profili analizi, mevsimsel operasyon stratejisi, çoklu türbin sıralaması, dispatch optimizasyonu ve sliding pressure operasyon ile yıllık bazda %5-15 enerji ve maliyet tasarrufu sağlanabilir.

**Tipik Tasarruf:** %5-15 (yakıt maliyeti + elektrik satın alma maliyeti toplamı)
**Tipik ROI:** 0.5-2 yıl (çoğunlukla operasyonel değişiklik, düşük yatırım)

## 1. Yük Profili Analizi — Load Profile Analysis

### 1.1 Veri Toplama

Yük eşleştirme optimizasyonu için minimum 1 yıllık (ideal 2-3 yıl) aşağıdaki veriler gereklidir:

| Veri | Kaynak | Çözünürlük | Açıklama |
|------|--------|------------|----------|
| Buhar tüketimi (ton/h) | Flowmetre veya kazan yakıt verisi | Saatlik | HP, MP, LP ayrı ayrı |
| Elektrik tüketimi (kW) | Enerji analizörü, sayaç | 15 dk | Tesis toplam + ana yükler |
| Elektrik üretimi (kW) | Jeneratör güç ölçümü | 15 dk | Türbin üretimi |
| Proses sıcaklık/basınç | DCS/SCADA | Saatlik | Proses buhar koşulları |
| Dış hava sıcaklığı | Meteoroloji verisi | Günlük | Mevsimsel etki analizi |
| Üretim miktarı | MES/ERP | Günlük | Yük-üretim korelasyonu |

### 1.2 Yük Profili Göstergeleri

```
Temel yük profili metrikleri:

1. Yük Faktörü (Load Factor — LF):
   LF = Ortalama_yük / Maksimum_yük × 100  [%]
   Yüksek LF (>80%) → Kararlı operasyon, kolay optimizasyon
   Düşük LF (<50%) → Dalgalı yük, kısmi yük sorunu

2. Eşzamanlılık Faktörü (Coincidence Factor — CF):
   CF = Σ(termal_yük × elektrik_yük) / (Σ termal_yük × Σ elektrik_yük)
   CF = 1.0 → Mükemmel eşzamanlılık
   CF < 0.7 → Zayıf eşzamanlılık, depolama/esneklik gerekli

3. Isı/Güç Oranı Dağılımı (HPR Distribution):
   HPR_min, HPR_max, HPR_ortalama, HPR_standart_sapma
   Dar dağılım → Sabit yük profili
   Geniş dağılım → Esnek türbin gerekli

4. Kapasite Kullanım Oranı (Capacity Utilization):
   CU = Yıllık_üretim / (Kurulu_kapasite × 8,760) × 100  [%]
```

### 1.3 Yük Süreklilik Eğrisi (Load Duration Curve)

Yük süreklilik eğrisi, yük değerlerini büyükten küçüğe sıralayarak her yük seviyesinin yıl içinde kaç saat sürdüğünü gösterir:

| Yük Bandı [%] | Süre [h/yıl] | Kümülatif [h] | Strateji |
|----------------|-------------|---------------|----------|
| 90-100 | 1,500 | 1,500 | Tam yük operasyon |
| 80-90 | 2,000 | 3,500 | Tam yük yakını |
| 70-80 | 1,500 | 5,000 | Kabul edilebilir kısmi yük |
| 60-70 | 800 | 5,800 | Verim düşüşü belirgin |
| 50-60 | 500 | 6,300 | Alternatif operasyon düşün |
| <50 | 700 | 7,000 | Türbin durdur / bypass |

## 2. Termal/Elektrik Yük Eşleştirme — Thermal/Electrical Load Matching

### 2.1 CHP Yük Eşleştirme Modları

| Mod | Açıklama | Avantaj | Dezavantaj | Uygun Profil |
|-----|----------|---------|------------|-------------|
| Termal takip (thermal following) | Türbin çıkışı proses buhar ihtiyacına göre ayarlanır | Tüm ısı kullanılır, atık minimum | Elektrik fazlası/açığı oluşur | HPR > 3 |
| Elektrik takip (electrical following) | Türbin çıkışı elektrik ihtiyacına göre ayarlanır | Elektrik dengesi sağlanır | Isı fazlası/açığı oluşur | HPR < 2 |
| Hibrit mod | Zaman dilimine göre termal/elektrik takip değişir | Optimum maliyet | Karmaşık kontrol | Değişken HPR |
| Baz yük (base load) | Türbin sabit güçte çalışır | Basit operasyon, kararlı verim | Esneklik yok | Sabit yük profili |

### 2.2 Termal Takip Optimizasyonu

```
Termal takip modunda (en yaygın endüstriyel CHP):

1. Buhar ihtiyacı → Kazan buhar üretimi → Türbin akış → Elektrik üretimi
2. Elektrik açığı → Şebekeden alım
3. Elektrik fazlası → Şebekeye satış veya yük azaltma

Optimizasyon fırsatları:
a) Elektrik satış fiyatı yüksek saatlerde türbin yükünü maksimize et
   (buhar depolama veya kazan yükünü artırarak)

b) Elektrik alış fiyatı düşük saatlerde türbin yükünü azalt
   (buhar PRV bypass — ancak exergy kaybı yüksek!)

c) Saatlik elektrik fiyatı dalgalanmasından faydalanma:
   ΔGelir = Σ(Ẇ_t × c_elek,t) - Σ(Q̇_yakıt,t × c_yakıt,t)
   t = saatlik zaman dilimi
```

### 2.3 HPR Uyumsuzluğu Çözümleri

| HPR Durumu | Problem | Çözüm | Açıklama |
|------------|---------|-------|----------|
| HPR_tesis > HPR_türbin | Elektrik fazlası, ısı açığı | Yardımcı kazan (auxiliary boiler) | Ek ısı kaynağı |
| HPR_tesis < HPR_türbin | Isı fazlası, elektrik açığı | Kısmi yoğuşma (condensing tail) | Fazla buharı yoğuştur, elektrik üret |
| HPR_tesis dalgalı | Sürekli dengesizlik | Çekişli (extraction) türbin | Esnek HPR ile operasyon |
| HPR_tesis mevsimsel | Yaz/kış farklı | Mevsimsel operasyon stratejisi | Bölüm 3'e bak |

## 3. Mevsimsel Operasyon Stratejisi — Seasonal Operation

### 3.1 Mevsimsel Yük Profili (Türkiye Endüstriyel)

| Mevsim | Proses Buhar [%] | Isıtma Buhar [%] | Toplam Termal [%] | Elektrik [%] | HPR |
|--------|------------------|-------------------|-------------------|-------------|-----|
| Kış (Aralık-Şubat) | 100 | 100 | 120-150 | 100 | Yüksek (8-12) |
| İlkbahar (Mart-Mayıs) | 100 | 30-50 | 110-130 | 100 | Orta (5-8) |
| Yaz (Haziran-Ağustos) | 100 | 0 | 80-100 | 110 (soğutma) | Düşük (3-5) |
| Sonbahar (Eylül-Kasım) | 100 | 20-40 | 105-125 | 100 | Orta (5-7) |

*%100 referans = tasarım noktası

### 3.2 Mevsimsel Strateji Önerileri

**Kış — Yüksek termal yük:**
- Türbin tam yükte çalıştır
- Isıtma buharını türbin çıkışından sağla (PRV bypass etme)
- Kazan yükünü artır, ek elektrik üretimi sağla
- Eksik ısı için yardımcı kazan devreye al

**Yaz — Düşük termal yük:**
- Türbin yükünü azalt veya durdur (ekonomik analiz gerekli)
- Düşük yükte çalıştırmak yerine: kısa süreli tam yük + duruş rotasyonu
- Condensing tail (varsa) ile fazla buharı elektriğe dönüştür
- Absorpsiyon soğutma entegrasyonu ile termal yükü artır (trijenerasyon)

**Geçiş mevsimleri:**
- Sliding pressure operasyon ile kısmi yük verimini iyileştir
- Isıtma sistemi kademeli geçiş planla
- Yardımcı kazan yerine türbin çıkış buharını öncelikle kullan

## 4. Çoklu Türbin Sıralaması — Multi-Turbine Sequencing

### 4.1 Sequencing Prensibi

Birden fazla türbin olan tesislerde, toplam yükü türbinler arasında en verimli şekilde dağıtmak önemlidir.

```
Temel prensip:
- Her türbinin verim-yük eğrisi farklıdır
- Kısmi yükte verim düşer (nonlinear)
- Bir türbini tam yükte, diğerini kısmi yükte çalıştırmak
  genellikle ikisini de %75'te çalıştırmaktan iyidir

Optimizasyon formülü:
min Σ(Q̇_yakıt,i)  subject to  Σ(Ẇ_i) = Ẇ_talep  ve  Σ(Q̇_ısı,i) = Q̇_talep

Burada i = türbin numarası
```

### 4.2 Sequencing Stratejileri

| Strateji | Açıklama | Uygun Durum |
|----------|----------|-------------|
| Eşit yük dağılımı (equal loading) | Her türbine eşit yük | Aynı tip/boyut türbinler |
| Verimlilik bazlı (efficiency-based) | En verimli türbin önce tam yüke | Farklı boyut/yaşta türbinler |
| Marjinal maliyet bazlı | En düşük marjinal maliyetli türbin önce | Farklı yakıtlı veya farklı verimli |
| Kısıt bazlı (constraint-based) | Proses kısıtları (buhar basınç/debi) öncelikli | Çoklu basınç seviyesi |

### 4.3 Sequencing Karar Tablosu

| Toplam Yük [%] | 2 Türbin (Eşit) | 2 Türbin (Optimize) | Tasarruf [%] |
|-----------------|-----------------|---------------------|-------------|
| 100 | 100 + 100 | 100 + 100 | 0 |
| 80 | 80 + 80 | 100 + 60 | 1-3 |
| 60 | 60 + 60 | 100 + 20 veya 100 + kapalı | 3-6 |
| 50 | 50 + 50 | 100 + kapalı | 5-10 |
| 40 | 40 + 40 | 80 + kapalı | 5-12 |

## 5. Dispatch Optimizasyonu — Dispatch Optimization

### 5.1 Saatlik Dispatch Optimizasyonu

```
Dispatch optimizasyonu — saatlik maliyet minimizasyonu:

Karar değişkenleri (her saat için):
- Ẇ_türbin,i: Her türbinin elektrik üretimi [kW]
- Q̇_kazan,j: Her kazanın buhar üretimi [kg/s]
- Ẇ_şebeke: Şebekeden alınan/satılan elektrik [kW]

Amaç fonksiyonu:
min C_toplam = Σ(Q̇_yakıt,j × c_yakıt) + Ẇ_şebeke_alım × c_alım - Ẇ_şebeke_satış × c_satış

Kısıtlar:
1. Buhar dengesi: Σ(Q̇_kazan,j) = Σ(ṁ_türbin,i) + ṁ_PRV + ṁ_proses_direkt
2. Elektrik dengesi: Σ(Ẇ_türbin,i) + Ẇ_şebeke_alım = Ẇ_talep + Ẇ_şebeke_satış
3. Isı dengesi: Σ(Q̇_proses,i) ≥ Q̇_talep
4. Kapasite sınırları: Ẇ_min,i ≤ Ẇ_türbin,i ≤ Ẇ_max,i
5. Rampa hızı: |ΔẆ_türbin,i/Δt| ≤ rampa_max,i
```

### 5.2 Dispatch Yazılım Araçları

| Araç | Açıklama | Maliyet | Uygulanabilirlik |
|------|----------|---------|-----------------|
| Excel/Python optimizasyon | Basit LP/MILP modeli | Düşük (€1,000-5,000) | Küçük sistemler (1-3 türbin) |
| MATLAB/Simulink | Dinamik simülasyon + optimizasyon | Orta (€5,000-20,000) | Orta karmaşıklıkta |
| Endüstriyel EMS (DEMS) | Distributed Energy Management System | Yüksek (€50,000-200,000) | Büyük tesisler, gerçek zamanlı |
| AI/ML tabanlı dispatch | Makine öğrenmesi ile tahminli optimizasyon | Orta-Yüksek | İleri seviye, veri gerektirir |

## 6. Sliding Pressure Operasyon — Değişken Basınç

### 6.1 Sliding Pressure Prensibi

```
Sabit basınç (throttle control):
- Kazan sabit basınçta buhar üretir
- Türbin giriş vanası kısılarak yük kontrolü yapılır
- Kısma ile tersinmezlik (irreversibility) → exergy yıkımı artar
- Kısmi yükte verim düşüşü fazla

Sliding pressure (değişken basınç):
- Kazan basıncı türbin yüküne göre ayarlanır
- Türbin giriş vanası tam açık kalır (kısma yok)
- Kısma kaybı elimine → daha iyi kısmi yük verimi
- Kısmi yükte exergy yıkımı azalır

Verim karşılaştırma:
| Yük [%] | Throttle η/η_tam | Sliding η/η_tam | Fark |
|---------|------------------|------------------|------|
| 100     | 1.00             | 1.00             | 0    |
| 80      | 0.97             | 0.99             | +%2  |
| 60      | 0.90             | 0.96             | +%6  |
| 50      | 0.85             | 0.93             | +%8  |
| 40      | 0.78             | 0.89             | +%11 |
```

### 6.2 Sliding Pressure Uygulama Koşulları

- Kazan sliding pressure operasyona uygun olmalı (once-through veya drum tipi — drum tipi sınırlı)
- Türbin kontrol sistemi uyumlu olmalı
- Buhar kalitesi tüm basınç aralığında korunmalı
- Minimum basınç sınırı belirlenmeli (buhar kalitesi ve proses gereksinimi)
- Büyük türbinlerde (>20 MW) yaygın, küçük endüstriyel türbinlerde nadir

## 7. Peak Shaving ve Base Load CHP

### 7.1 Peak Shaving (Pik Tıraşlama)

```
Peak shaving stratejisi:
- Türbin, şebeke pik talep saatlerinde maksimum yükte çalıştırılır
- Gece/düşük tarife saatlerinde yük azaltılır veya durdurulur
- Pik saatlerde yüksek elektrik fiyatından tasarruf / gelir

Ekonomik fayda:
Ek_gelir = Σ(Ẇ_pik × Δc_pik × t_pik)

Burada:
Δc_pik = Pik tarife - Normal tarife  [€/kWh]
t_pik = Pik saat süresi  [h]

Türkiye endüstriyel tarife (2025-2026 yaklaşık):
- Pik: 0.12-0.15 €/kWh (17:00-22:00)
- Gündüz: 0.09-0.11 €/kWh (06:00-17:00)
- Gece: 0.05-0.07 €/kWh (22:00-06:00)
```

### 7.2 Base Load CHP vs. Peak Load CHP

| Parametre | Base Load CHP | Peak Load CHP |
|-----------|--------------|---------------|
| Çalışma saati [h/yıl] | 7,000-8,500 | 3,000-5,000 |
| Kapasite faktörü [%] | >80 | 40-60 |
| Türbin tipi | Back-pressure / extraction | Condensing-extraction |
| SPP [yıl] | 3-5 | 4-7 |
| Elektrik üretim maliyeti [€/kWh] | 0.04-0.07 | 0.06-0.10 |
| Uygun profil | Sabit termal yük | Mevsimsel yük, yüksek ΔC_pik |

## 8. Yıllık Operasyon Optimizasyonu — Annual Optimization

### 8.1 Yıllık Planlama Çerçevesi

| Ay | Termal Talep | Elektrik Stratejisi | Türbin Operasyon | Bakım Penceresi |
|----|-------------|---------------------|-----------------|-----------------|
| Ocak-Şubat | Yüksek | Tam üretim | Tam yük | Hayır |
| Mart-Nisan | Azalan | Pik saatlere odaklan | %80-100 | Nisan (kısa duruş) |
| Mayıs-Haziran | Orta-Düşük | Pik saatlere odaklan | %60-80 | Mayıs (major overhaul) |
| Temmuz-Ağustos | En düşük | Ekonomik analiz yap | %50-70 veya durdur | Temmuz (opsiyonel) |
| Eylül-Ekim | Artan | Pik saatlere odaklan | %70-90 | Hayır |
| Kasım-Aralık | Yüksek | Tam üretim | Tam yük | Hayır |

### 8.2 Bakım Planlama ile Entegrasyon

```
Optimal bakım zamanlaması:
- Düşük termal yük döneminde planlı bakım yap
- Major overhaul → Yaz ayları (düşük ısıtma talebi)
- Minor bakım → Geçiş mevsimleri (hafta sonu)

Bakım kaybı hesabı:
C_bakım_kaybı = Ẇ_türbin × c_elek × t_duruş + ṁ_PRV × (h_HP - h_LP) × c_yakıt × t_duruş/η_kazan

PRV bypass maliyeti → Exergy kaybı → Türbinden geçmeyen buharın iş potansiyeli kaybedilir
```

## 9. Yük Profili Analiz Yöntemleri

### 9.1 Kümeleme Analizi (Clustering Analysis)

Yıllık yük verisini tipik gün profillerine ayırma:
- **İş günü profili:** Sabah rampa, gündüz sabit, akşam düşüş
- **Hafta sonu profili:** Düşük veya sıfır üretim
- **Kampanya profili:** Mevsimsel tam yük (şeker, konserve)
- **Duruş profili:** Planlı bakım, bayram tatili

### 9.2 Korelasyon Analizi

| İlişki | Korelasyon | Kullanım |
|--------|------------|----------|
| Buhar talebi vs. üretim miktarı | Yüksek (r > 0.8) | Üretim planından buhar tahmini |
| Buhar talebi vs. dış hava sıcaklığı | Orta-Yüksek (r = 0.5-0.8) | Isıtma yükü tahmini |
| Elektrik talebi vs. saat | Orta (r = 0.4-0.7) | Günlük yük profili tahmini |

## 10. Uygulama Örneği

```
Senaryo: 5 MW back-pressure türbin, kağıt fabrikası
Mevcut durum:
- Yıl boyu sabit yük, HPR = 6.5
- Kış aylarında ısıtma buharı ek kazan ile sağlanıyor
- Yaz aylarında buhar fazlası PRV ile basınç düşürülüyor

Optimizasyon sonrası:
1. Kış: Ek kazan yerine türbin kapasitesi artırıldı (10% overload)
   Tasarruf: €25,000/yıl (ek kazan yakıtı)

2. Yaz: PRV bypass yerine türbin yükü azaltıldı + sliding pressure
   Tasarruf: €18,000/yıl (azaltılmış exergy kaybı)

3. Dispatch: Pik saatlerde türbin tam yük, gece kısmi yük
   Tasarruf: €12,000/yıl (pik tarife avantajı)

4. Bakım: Major overhaul Mayıs'a taşındı (düşük yük dönemi)
   Tasarruf: €8,000/yıl (PRV bypass maliyeti azaltma)

Toplam yıllık tasarruf: €63,000/yıl
Yatırım (kontrol sistemi güncelleme): €30,000
SPP: 0.48 yıl (~6 ay)
```

## İlgili Dosyalar

- Hesaplama formülleri: `steam_turbine/formulas.md` — Kısmi yük ve CHP hesaplamaları
- Benchmark verileri: `steam_turbine/benchmarks.md` — Kısmi yük verim tabloları (Bölüm 3)
- Verim iyileştirme: `steam_turbine/solutions/efficiency_improvement.md` — Türbin iç verim artırma
- CHP konfigürasyonları: `steam_turbine/systems/steam_turbine_chp.md` — Sistem tasarımı
- Ekonomik analiz: `steam_turbine/economics/feasibility.md` — CHP fizibilite kriterleri
- Ekipmanlar arası fırsatlar: `factory/cross_equipment.md` — Fabrika seviyesinde entegrasyon
- Önceliklendirme: `factory/prioritization.md` — İyileştirme önceliklendirme matrisi
- Boyutlandırma: `steam_turbine/solutions/sizing_guide.md` — Yeni türbin seçimi
- Bakım: `steam_turbine/solutions/maintenance.md` — Bakım planlama ile entegrasyon
- Kazan yük optimizasyonu: `boiler/solutions/load_optimization.md` — Kazan tarafı optimizasyon

## Referanslar

- Horlock, J.H. (2003). *Advanced Gas Turbine Cycles*, Pergamon Press.
- Kehlhofer, R. et al. (2009). *Combined-Cycle Gas & Steam Turbine Power Plants*, PennWell.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- US DOE (2012). *Improving Steam System Performance — A Sourcebook for Industry*, 2nd Edition.
- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- EU Directive 2012/27/EU, "Energy Efficiency Directive — High Efficiency Cogeneration"
- Tsatsaronis, G. (2007). "Definitions and nomenclature in exergy analysis and exergoeconomics," *Energy*, 32(4).
- Frangopoulos, C.A. (2009). "A method to determine the power to heat ratio in cogeneration systems," *Energy*, 34(9).
- Rosen, M.A. & Dincer, I. (2003). "Thermoeconomic, exergoeconomic and sustainability analyses of CHP systems," *International Journal of Energy Research*.
- Türkiye Enerji Piyasası Düzenleme Kurumu (EPDK), Elektrik Piyasası Tarifeler Yönetmeliği.
