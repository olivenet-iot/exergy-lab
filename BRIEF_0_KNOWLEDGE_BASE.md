# BRIEF 0: Proses Knowledge Base Araştırma ve Dokümantasyon

> **Tarih:** 2026-02-07
> **Öncelik:** Yüksek — Brief 1 ile paralel çalıştırılabilir
> **Çıktı:** knowledge/factory/process/ altında 8+ Markdown dosyası
> **Dokunduğu Klasörler:** SADECE knowledge/factory/process/ (engine'e dokunma)
> **Tahmini:** ~2000 satır dokümantasyon

---

## 1. Amaç

ExergyLab'e "Proses Tanımı + Gap Analysis" özelliği ekleniyor. AI yorumlama motorunun (Claude) bu yeni özelliği anlamlı yorumlayabilmesi için proses bazlı referans dokümanları gerekiyor.

Bu brief **sadece knowledge base dosyaları** oluşturur. Engine kodu Brief 1'de yazılacak.

---

## 2. Oluşturulacak Dosyalar

```
knowledge/
  factory/
    process/                              ← YENİ KLASÖR
      index.md                            ← Ana giriş: proses analizi nedir, nasıl çalışır
      gap_analysis_methodology.md         ← Gap analizi metodolojisi açıklaması
      sustainability_index.md             ← ESI skoru açıklaması ve yorumlama rehberi
      bat_overview.md                     ← BAT kavramı, EU BREF sistemi, nasıl kullanılır
      drying.md                           ← Kurutma prosesleri exergy analizi
      heating.md                          ← Isıtma prosesleri exergy analizi
      cooling.md                          ← Soğutma prosesleri exergy analizi
      steam_generation.md                 ← Buhar üretimi exergy analizi
      compressed_air.md                   ← Basınçlı hava sistemleri exergy analizi
      chp.md                              ← CHP/Kojenerasyon exergy analizi
      cold_storage.md                     ← Soğuk depolama exergy analizi
      general_manufacturing.md            ← Genel üretim prosesleri (çimento, cam, kağıt, şeker)
```

Ek olarak mevcut index dosyasını güncelle:
```
knowledge/factory/index.md               ← Güncelle: process/ klasörünü referansla
```

---

## 3. Her Proses Dosyasının Yapısı

Her proses dosyası (drying.md, heating.md, vb.) şu yapıda olmalı:

```markdown
# [Proses Adı] — Exergy Analizi Referans Dokümanı

## 1. Proses Tanımı
- Bu proses ne yapar, endüstride nerede kullanılır
- Tipik ekipman kombinasyonları
- Ölçek aralığı (küçük/orta/büyük tesis)

## 2. Termodinamik Minimum Exergy
- Teorik alt limit formülü ve açıklaması
- Varsayımlar ve sınırlamalar
- Sayısal örnek (tipik değerlerle)
- Akademik referans kaynağı

## 3. Tipik Endüstriyel Exergy Tüketimi
- Mevcut endüstriyel sistemlerin tipik spesifik exergy tüketimi
- Exergy verimlilik aralıkları (düşük-orta-yüksek)
- Neden idealden bu kadar uzak? (tersinmezlik kaynakları)

## 4. BAT (Best Available Technology) Referansı
- En iyi mevcut teknoloji tanımı
- BAT spesifik exergy tüketimi
- BAT exergy verimi
- Kaynak: EU BREF doküman adı ve yılı
- Alt kategoriler varsa (örn: tahıl kurutma vs kereste kurutma)

## 5. Tipik Exergy Yıkım Kaynakları
- Ana tersinmezlik noktaları (sıralı, en büyükten küçüğe)
- Her bir kaynak için kısa açıklama
- İyileştirme potansiyeli

## 6. İyileştirme Stratejileri
- Pratik iyileştirme önerileri (3-5 madde)
- Her öneri için tahmini tasarruf yüzdesi
- Yatırım/geri dönüş perspektifi

## 7. Yorumlama Rehberi
- AI bu proses analizi sonuçlarını nasıl yorumlamalı
- ESI skoru bu proses tipi için ne anlama gelir
- Tipik benchmarklar ve karşılaştırma noktaları
- Dikkat edilmesi gereken özel durumlar
```

---

## 4. Araştırma Kaynakları ve Yönergeleri

### 4.1 Birincil Kaynaklar (Öncelikli)

Claude Code şu kaynakları web araştırmasıyla taramalı:

1. **EU BREF Dokümanları** (en güvenilir BAT kaynağı)
   - Energy Efficiency BREF (2009)
   - Food, Drink and Milk Industries BREF (2019)
   - Large Combustion Plants BREF (2017)
   - Cement, Lime and Magnesium Oxide BREF (2013)
   - Glass Manufacturing BREF (2012)
   - Pulp and Paper BREF (2015)
   - Industrial Cooling Systems BREF (2001)
   - URL pattern: https://eippcb.jrc.ec.europa.eu/reference

2. **Akademik Referanslar** (formüller için)
   - Dincer & Rosen — "Exergy: Energy, Environment and Sustainable Development" (formül referansı)
   - Bejan — "Advanced Engineering Thermodynamics"
   - Szargut — "Exergy Method: Technical and Ecological Applications"
   - Kotas — "The Exergy Method of Thermal Plant Analysis"
   - Tsatsaronis — "Thermoeconomic Analysis and Optimization"
   - Mujumdar — "Handbook of Industrial Drying" (kurutma spesifik)

3. **Endüstri Raporları**
   - DOE (US Department of Energy) Best Practices
   - IEA (International Energy Agency) endüstriyel verimlilik raporları
   - Compressed Air Challenge — basınçlı hava referansları

### 4.2 Araştırma Yönergeleri

- **Spesifik exergy tüketimi** araması: "[proses tipi] specific exergy consumption kJ/kg"
- **BAT değerleri** araması: "EU BREF [sektör] BAT associated energy consumption levels"
- **Minimum exergy** araması: "[proses tipi] minimum thermodynamic exergy theoretical limit"
- **Exergy verimlilik** araması: "[proses tipi] exergy efficiency range industrial"

### 4.3 Doğrulama Kuralları

Her sayısal değer için:
- [ ] Kaynak belirtilmiş mi?
- [ ] Birim açık mı? (kJ/kg, kWh/ton, %, vb.)
- [ ] Büyüklük sırası (order of magnitude) mantıklı mı?
- [ ] Birden fazla kaynak varsa tutarlı mı?
- [ ] Formül boyut analizi doğru mu?

---

## 5. Kritik Dosyalar — Detaylı İçerik Rehberi

### 5.1 index.md

```markdown
# Proses Exergy Analizi

ExergyLab'in proses analizi modülü, fabrikaların **ne ürettiğini** bilerek 
termodinamik performanslarını değerlendirir.

## Temel Kavramlar

### Exergetic Gap Analysis
Üç katmanlı karşılaştırma:
1. **Termodinamik Minimum** — Prosesin fizik yasaları tarafından belirlenen alt limit
2. **BAT (Best Available Technology)** — Mevcut en iyi teknoloji ile ulaşılabilir seviye  
3. **Mevcut Tesis** — Fabrikanın gerçek exergy tüketimi

Gap = Mevcut - Minimum → toplam iyileştirme potansiyeli
BAT Gap = Mevcut - BAT → gerçekçi iyileştirme potansiyeli

### Exergetic Sustainability Index (ESI)
ESI = Minimum / Mevcut (0-1 arası, 1 = ideal)

### Spesifik Exergy Tüketimi
Birim ürün başına exergy tüketimi (kWh/kg, kWh/ton, vb.)

## Desteklenen Proses Tipleri
- [Kurutma](drying.md) — Nem alma prosesleri
- [Isıtma](heating.md) — Akışkan/malzeme ısıtma
- [Soğutma](cooling.md) — Proses/konfor soğutma
- [Buhar Üretimi](steam_generation.md) — Endüstriyel buhar sistemleri
- [Basınçlı Hava](compressed_air.md) — Pnömatik sistemler
- [CHP/Kojenerasyon](chp.md) — Kombine ısı-güç
- [Soğuk Depolama](cold_storage.md) — Soğuk zincir
- [Genel Üretim](general_manufacturing.md) — Çimento, cam, kağıt, şeker, beton

## Metodoloji
Detaylı açıklama: [Gap Analysis Metodolojisi](gap_analysis_methodology.md)
BAT sistemi hakkında: [BAT Genel Bakış](bat_overview.md)
Sürdürülebilirlik skoru: [ESI Skoru](sustainability_index.md)
```

### 5.2 gap_analysis_methodology.md

Bu dosya şunları açıklamalı:
- Gap analysis'in akademik temeli (Tsatsaronis, Bejan)
- 3 katmanın (minimum, BAT, actual) nasıl hesaplandığı
- Gap dağılımının ekipman bazlı nasıl yapıldığı
- Ekonomik etki hesaplama yöntemi (gap × enerji fiyatı × çalışma saati)
- Sınırlamalar ve varsayımlar
- Referans kaynaklar

### 5.3 sustainability_index.md

Bu dosya şunları açıklamalı:
- ESI (Exergetic Sustainability Index) tanımı: ESI = Ex_min / Ex_actual
- Not sistemi (A-F) ve her notun anlamı
- Sektör bazlı tipik ESI değerleri
- Yorumlama rehberi: AI bu skoru nasıl anlatmalı
- "İdealin X katı" ifadesinin açıklaması
- Referans: Rosen & Dincer, "Exergy-based indicators for sustainability"

### 5.4 bat_overview.md

Bu dosya şunları açıklamalı:
- BAT (Best Available Techniques) kavramı
- EU BREF sistemi nasıl çalışır
- BAT-AEELs (BAT Associated Energy Efficiency Levels) nedir
- ExergyLab'da BAT nasıl kullanılıyor
- BAT değerlerinin sınırlamaları (bölgesel farklılıklar, ölçek etkileri)
- Referans: EU Industrial Emissions Directive 2010/75/EU

---

## 6. Proses Dosyaları — Araştırılacak Spesifik Değerler

### 6.1 drying.md

Araştırılacak değerler:
- Minimum exergy: Su buharlaştırma exergisi @25°C ≈ ? kJ/kg su (Dincer & Rosen referansı)
- Tipik endüstriyel SEC (Specific Exergy Consumption): ? - ? kJ/kg su uzaklaştırma
  - Araştırma bulgusu: Dryer exergy consumption 330-10,490 kJ/kg H2O (kaynak: ScienceDirect 2023 review)
  - Convective dryer tipik: 2000-5000 kJ/kg su (energy), exergy bunun ~%15-40'ı
  - Corn drying exergy efficiency: %14.8 - %40.1 (MDPI 2020)
- BAT alt kategorileri: tahıl, sprey, kereste, genel
- BAT teknolojisi: Isı pompalı kurutucu, MVR (Mechanical Vapor Recompression)
- EU BREF Food, Drink and Milk Industries (2019) — kurutma bölümü
- Tersinmezlik kaynakları: Yanma (%45-55), ısı transferi (%20-30), egzoz (%15-25)

### 6.2 heating.md

Araştırılacak değerler:
- Minimum exergy: Carnot bazlı → Ex_min = Q × (1 - T0/T_lm)
- Tipik kazan exergy verimi: %25-50 (kaynak: Tsatsaronis)
  - Araştırma bulgusu: Boiler exergy efficiency ~%38.5-61.5 (power plant scale)
  - Industrial boiler energy efficiency: %80-95 ama exergy verimi çok daha düşük
  - Büyük fark: energy efficiency yüksek, exergy efficiency düşük — yanma tersinmezliği
- BAT: Kondensasyonlu kazan + ekonomizer + hava ön ısıtıcı
- EU BREF Large Combustion Plants (2017)

### 6.3 cooling.md

Araştırılacak değerler:
- Minimum exergy: Ters Carnot → Ex_min = Q_cool × (T0/T_cold - 1)
- Tipik chiller exergy verimi: %20-40
- COP değerleri: Tipik 3-6, BAT 6-10 (yüksek verimli santrifüj)
- BAT: Yüksek COP chiller + free cooling + değişken akış
- EU BREF Industrial Cooling Systems (2001)

### 6.4 steam_generation.md

Araştırılacak değerler:
- Minimum exergy: Buharın fiziksel exergisi = h - h0 - T0(s - s0)
  - CoolProp ile hesaplanabilir
  - 10 bar doymuş buhar exergisi ≈ 780 kJ/kg (referans doğrulanmalı)
- Tipik kazan exergy verimi: %30-50 (endüstriyel)
  - Araştırma: Boiler exergy performance ~%61.5 (power plant), endüstriyel daha düşük
  - Yanma tersinmezliği en büyük kayıp (%40-50 exergy yıkımı)
- BAT: Yoğuşmalı kazan + ekonomizer + hava ön ısıtıcı + blowdown heat recovery
- EU BREF Large Combustion Plants (2017)

### 6.5 compressed_air.md

Araştırılacak değerler:
- Minimum exergy: İzothermal sıkıştırma → W_min = m × R × T0 × ln(P2/P1)
  - 7 bar için ≈ 0.054 kWh/m³ FAD (hesaplanacak)
- Tipik sistem exergy verimi: %5-15 (son kullanım dahil çok düşük!)
  - Araştırma: Foundry compressed air system overall exergy efficiency ~%33.9
  - Ama bu sadece kompresör, sistem dahil çok daha düşük
  - "Only 10-15% of compressed air energy reaches end use" — DOE
- BAT: VSD kompresör + ısı geri kazanımı + kaçak azaltma + basınç optimizasyonu
  - DOE Compressed Air Challenge referansları
  - Tipik BAT spesifik güç: 5-7 kW/(m³/min) @7bar
- Exergy = basınç exergisi + (atılırsa) termal exergy

### 6.6 chp.md

Araştırılacak değerler:
- Minimum exergy: Ex_elec + Ex_thermal çıktı toplamı
- Tipik CHP exergy verimi: %40-65
- BAT: Kombine çevrim gaz türbini + HRSG
- Fuel utilization factor vs exergy efficiency farkı (önemli kavram)
- EU BREF Large Combustion Plants (2017)

### 6.7 cold_storage.md

Araştırılacak değerler:
- Minimum exergy: Q_load × (T0/T_cold - 1)
- Tipik soğutma sistemi exergy verimi: %15-30
- BAT: Yüksek COP soğutma + gelişmiş yalıtım + defrost optimizasyonu
- Sıcaklık aralıklarına göre: +5°C (taze gıda), -18°C (donmuş), -30°C (derin dondurucu)

### 6.8 general_manufacturing.md

Alt kategoriler ve araştırılacak değerler:

| Sektör | Spesifik Enerji (BAT) | Kaynak BREF |
|--------|----------------------|-------------|
| Çimento | 3.0-3.5 GJ/ton klinker | Cement BREF 2013 |
| Cam | 4-8 GJ/ton cam | Glass BREF 2012 |
| Kağıt | 10-25 GJ/ton kağıt | Pulp & Paper BREF 2015 |
| Şeker | 8-12 GJ/ton şeker pancarı | Food BREF 2019 |
| Beton | 0.1-0.3 GJ/ton beton | Genel referanslar |

NOT: Bunlar enerji değerleri — exergy değerlerine dönüştürme gerekli (yakıt exergy faktörü ile çarpma).

---

## 7. Skills Dosyası

### 7.1 Yeni Skill: `skills/factory/process_analyst.md`

```markdown
# Proses Analizi Yorumlama Becerisi

Bu beceri, ExergyLab'in proses gap analizi sonuçlarını yorumlamak için kullanılır.

## Ne Zaman Kullanılır
- Kullanıcı fabrika analizi sonuçlarını görüntülediğinde
- Proses tanımı olan bir fabrika için AI yorumu istendiğinde
- Gap analizi sonuçları hakkında soru sorulduğunda

## Yorumlama Çerçevesi

### 1. Büyük Resim (İlk Cümle)
"Bu [proses tipi] tesisi, termodinamik ideale göre [X] kat fazla exergy tüketiyor."

### 2. BAT Karşılaştırması
"En iyi mevcut teknoloji ile kıyaslandığında [Y] kat fazla tüketim var. 
Gerçekçi iyileştirme potansiyeli: [Z] kW ([%W])."

### 3. Ekonomik Etki
"Bu, yıllık yaklaşık [€A] tasarruf potansiyeline karşılık geliyor."

### 4. Öncelik Sıralaması
Gap dağılımından en büyük 3 kaynağı sırala ve her biri için kısa öneri ver.

### 5. Aksiyon Önerisi
Proses tipine özel 2-3 somut iyileştirme önerisi.

## ESI Skoru Yorumlama

| Not | ESI Aralığı | Yorum |
|-----|-------------|-------|
| A | > 0.50 | "Dünya lideri seviyesinde. Marjinal iyileştirmeler mümkün." |
| B | 0.35 - 0.50 | "Çok iyi performans. BAT seviyesine yakın." |
| C | 0.20 - 0.35 | "İyi performans. Önemli iyileştirme fırsatları mevcut." |
| D | 0.10 - 0.20 | "Ortalama. Ciddi iyileştirme potansiyeli var." |
| E | 0.05 - 0.10 | "Zayıf. Acil iyileştirme gerekiyor." |
| F | < 0.05 | "Kritik. Büyük yatırım/dönüşüm gerekli." |

## Dikkat Edilecekler
- Minimum exergy termodinamik ALT LİMİTTİR — gerçek hayatta ulaşılamaz
- BAT gerçekçi hedeftir — ama yatırım gerektirir
- "İdealin X katı" büyük sayılar ürkütücü olabilir — bağlam ver
- Her sektörün kendine has ESI aralığı var — çimento D ile gıda D aynı anlama gelmez
```

---

## 8. Çalışma Yönergeleri

1. **Önce `knowledge/factory/process/` klasörünü oluştur**
2. **index.md'yi yaz** — genel giriş
3. **gap_analysis_methodology.md, sustainability_index.md, bat_overview.md** yaz — temel kavramlar
4. **Her proses dosyasını sırayla yaz** — web araştırması yaparak
5. **Her dosyada sayısal değerleri kaynak ile birlikte belirt**
6. **skills/factory/process_analyst.md** oluştur
7. **knowledge/factory/index.md** güncelle — yeni process/ klasörünü referansla

### Doğrulama Kontrol Listesi

Her proses dosyası tamamlandığında:
- [ ] Minimum exergy formülü var ve kaynağı belirtilmiş
- [ ] BAT spesifik exergy tüketimi var ve kaynağı belirtilmiş
- [ ] En az 2 farklı kaynak referans verilmiş
- [ ] Tipik endüstriyel exergy verimlilik aralığı belirtilmiş
- [ ] Yorumlama rehberi bölümü var
- [ ] Birimler tutarlı ve açık

---

## 9. UYARILAR

1. **Engine koduna DOKUNMA** — Bu brief sadece knowledge/ ve skills/ klasörlerine yazar
2. **Frontend'e DOKUNMA** — Bu brief sadece dokümantasyon üretir
3. **Sayısal değerler yaklaşık olabilir** — %10-20 hata payı kabul edilebilir, önemli olan büyüklük sırası
4. **Kaynak bulunamayan değerler için** — açıkça "tahmini değer, doğrulama gerekli" yaz
5. **Türkçe ve İngilizce karışık olabilir** — Teknik terimler İngilizce, açıklamalar Türkçe tercih edilir

---

*Bu brief, ExergyLab'in AI yorumlama kapasitesini proses analizi için zenginleştirir. Brief 1 ile paralel çalıştırılabilir.*
