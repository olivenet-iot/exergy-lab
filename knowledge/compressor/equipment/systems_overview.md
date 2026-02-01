# Basınçlı Hava Sistemleri (Compressed Air Systems)

> Son güncelleme: 2026-01-31

## Genel Bakış

Basınçlı hava, endüstride "dördüncü yardımcı enerji" olarak adlandırılır (elektrik, su ve doğalgaz'dan sonra). Tipik bir endüstriyel tesisin toplam elektrik tüketiminin %10-30'u basınçlı hava üretimi için harcanır.

**Kritik gerçek:** Basınçlı hava, en pahalı enerji taşıyıcılarından biridir. Son kullanım noktasında faydalı enerji verimi yalnızca %10-30'dur — yani giren elektrik enerjisinin %70-90'ı kaybolur.

## Sistem Bileşenleri

Bir basınçlı hava sistemi iki ana bölümden oluşur:

### Arz Tarafı (Supply Side)
1. **Kompresör(ler):** Havayı sıkıştırır
   - Vidalı (screw) — en yaygın, 3-500 kW
   - Pistonlu (piston) — yüksek basınç, küçük kapasite
   - Scroll — sessiz, yağsız, küçük kapasite (2-33 kW)
   - Santrifüj — büyük kapasite (150-3000+ kW)
   - Bkz. ilgili ekipman dosyaları

2. **Kurutucu (Dryer):** Nemli havadan suyu uzaklaştırır
   - Soğutmalı (refrigerated): +3°C PDP, %0.5-2 enerji
   - Adsorpsiyon (desiccant): -40°C PDP, %5-20 enerji
   - HOC (Heat of Compression): -40°C PDP, ~%0 ek enerji
   - Membran: -40°C PDP, %15-20 purge kaybı

3. **Filtreler:** Partikül, yağ buharı ve koku giderme
   - Partikül filtresi: 1-5 µm
   - Koalesan filtre: 0.01 ppm yağ
   - Aktif karbon filtresi: Koku ve buhar

4. **Depolama tankı (Receiver):** Basınç dalgalanmalarını tamponlar
   - Islak tank (wet receiver): Kompresör-kurutucu arası
   - Kuru tank (dry receiver): Kurutucu sonrası

5. **Kondansat drenaj:** Biriken suyun uzaklaştırılması
   - Timer drain: Periyodik açılma (hava kaybı var)
   - No-loss drain: Sadece su varken açılır

### Talep Tarafı (Demand Side)
1. **Dağıtım boruları:** Ana hat, branş hatları, düşme boruları
2. **Basınç regülatörleri:** Kullanım noktasında basınç ayarı
3. **FRL üniteleri:** Filtre-Regülatör-Lubrikatör (son kullanım noktasında)
4. **Son kullanıcılar:** Pnömatik silindir, aletler, üfleme, taşıma, kontrol

## Basınç Kavramları

### Basınç Terminolojisi
| Terim | Açıklama | Örnek |
|-------|----------|-------|
| Gage basıncı (P_g) | Atmosfer üzeri basınç | 7 bar(g) |
| Mutlak basınç (P_abs) | Gage + atmosfer | 8.013 bar(a) |
| Atmosfer basıncı (P_atm) | Deniz seviyesi standart | 1.013 bar(a) |
| Basınç bandı | Yük/boşta arası fark | 0.5-1.5 bar |
| Basınç düşüşü (ΔP) | Kompresör-kullanım arası kayıp | 0.5-2.0 bar |

### Basınç Seviyeleri

```
Kompresör çıkışı    : 7.5-8.5 bar(g)
  ↓ Aftercooler     : -0.1 bar
  ↓ Kurutucu        : -0.2-0.4 bar
  ↓ Filtreler       : -0.1-0.3 bar
  ↓ Ana hat borular : -0.1-0.3 bar
  ↓ Branş hatları   : -0.05-0.1 bar
  ↓ FRL üniteleri   : -0.1-0.3 bar
Kullanım noktası    : 5.5-7.0 bar(g)
```

**Hedef:** Kompresör çıkışı ile kullanım noktası arasındaki toplam basınç düşüşü <1.0 bar (en iyi uygulama: <0.5 bar).

### Basınç-Enerji İlişkisi
- Her 1 bar basınç düşürme ≈ %6-7 enerji tasarrufu
- Sistem basıncı gereksiz yere yüksek tutulması endüstrideki en yaygın israf

## Çoklu Kompresör Sistemleri

### Kontrol Stratejileri

#### 1. Kaskad Basınç Kontrolü
- Her kompresör farklı basınç bandında çalışır
- Basit, ama geniş basınç bandı gerektirir (1.5-2.0 bar)
- Yüksek ortalama basınç = enerji israfı

#### 2. Master Controller (Merkezi Kontrol)
- Tüm kompresörler tek kontrol ünitesinden yönetilir
- Dar basınç bandı (0.3-0.5 bar)
- En verimli kombinasyonu otomatik seçer
- Tipik tasarruf: %5-12

#### 3. Baz Yük + Trim Konfigürasyonu
- Sabit hızlı kompresör(ler): Sürekli baz yükü karşılar (%100 yükte en verimli)
- VSD kompresör: Değişken talebi karşılar (trim)
- En iyi enerji verimi için önerilen konfigürasyon

### Sistem Boyutlandırma Kuralları

| Parametre | Kural |
|-----------|-------|
| Tank hacmi (sabit hız) | 5-10 litre / (l/s kompresör kapasitesi) |
| Tank hacmi (VSD) | 2-5 litre / (l/s kompresör kapasitesi) |
| Ana hat boru hızı | <6 m/s |
| Branş hattı hızı | <15 m/s |
| Toplam basınç düşüşü | <1.0 bar (hedef <0.5 bar) |
| VSD kompresör oranı | Toplam kapasitenin %30-50'si |

## Hava Kalitesi (ISO 8573-1)

| Sınıf | Katı Partikül | Su (PDP) | Toplam Yağ |
|-------|---------------|----------|------------|
| Class 0 | Üretici beyanı | Üretici beyanı | Üretici beyanı |
| Class 1 | 0.1 µm | -70°C | 0.01 mg/m³ |
| Class 2 | 1 µm | -40°C | 0.1 mg/m³ |
| Class 3 | 5 µm | -20°C | 1 mg/m³ |
| Class 4 | 15 µm | +3°C | 5 mg/m³ |

### Sektörel Gereksinimler (Tipik)
| Sektör | Tipik Sınıf | Kritik Parametre |
|--------|-------------|-----------------|
| İlaç | 1.2.1 | Yağsız, kuru |
| Gıda (doğrudan temas) | 1.2.1 | Yağsız |
| Gıda (dolaylı temas) | 1.4.1 | Standart |
| Elektronik | 1.1.1 | Ultra temiz |
| Genel endüstri | 1.4.2 | Standart |
| Atölye/pnömatik alet | 2.4.2 | Temel |
| Boya kabini | 1.2.1 | Yağsız, kuru |

## Enerji Akışı ve Kayıp Noktaları

### Tipik Sistem Enerji Dağılımı
```
Elektrik Girişi (100%)
  ├── Motor kayıpları: %5-8
  ├── Sıkıştırma tersinmezliği (ısı): %60-75
  │     ├── Yağ soğutucu: ~%72 (vidalı yağlı)
  │     ├── Aftercooler: ~%13
  │     └── Radyasyon: ~%5
  ├── Kurutucu kayıpları: %2-15 (tipe bağlı)
  ├── Dağıtım basınç düşüşü: %3-8
  ├── Kaçak kayıpları: %15-30
  ├── Kontrol kayıpları: %5-20
  ├── Uygunsuz kullanım: %0-20
  └── Faydalı iş (exergy): %10-30
```

### Temel KPI'lar (Key Performance Indicators)

| KPI | Formül | İyi | Ortalama | Kötü |
|-----|--------|-----|----------|------|
| Spesifik güç (SEC) | Toplam kW / Toplam m³/min | <5.5 | 5.5-7.5 | >7.5 |
| Kaçak oranı | Kaçak debisi / Toplam debi × 100 | <%10 | %10-20 | >%20 |
| Basınç düşüşü | P_kompresör - P_kullanım | <0.5 bar | 0.5-1.5 bar | >1.5 bar |
| Yük faktörü | Ortalama kW / Nominal kW × 100 | >%80 | %50-80 | <%50 |
| Exergy verimi | Ex_çıkış / Ex_giriş × 100 | >%35 | %15-35 | <%15 |

## Maliyet Yapısı (Yaşam Döngüsü)

10 yıllık yaşam döngüsü maliyet dağılımı (tipik):

| Maliyet Kalemi | Oran |
|---------------|------|
| Enerji | %70-80 |
| İlk yatırım | %10-15 |
| Bakım ve yedek parça | %5-10 |
| Kurulum | %2-5 |

**Sonuç:** Enerji verimliliği, toplam maliyetin %70-80'ini belirler. Yatırım kararlarında yalnızca satın alma fiyatına değil, toplam sahip olma maliyetine (TCO) bakılmalıdır.

## Tasarruf Fırsat Alanları (Öncelik Sırasıyla)

| Öncelik | Alan | Tipik Tasarruf | Karmaşıklık |
|---------|------|---------------|-------------|
| 1 | Kaçak tespiti ve onarımı | %10-25 | Düşük |
| 2 | Basınç optimizasyonu | %6-14 | Düşük |
| 3 | Kontrol iyileştirme (VSD, master controller) | %5-15 | Orta |
| 4 | Kurutucu optimizasyonu | %2-18 | Orta |
| 5 | Isı geri kazanımı | %0 (enerji) ama dolaylı tasarruf | Orta |
| 6 | Giriş havası optimizasyonu | %1-7 | Düşük |
| 7 | Bakım iyileştirme | %3-15 | Düşük |
| 8 | Sistem tasarımı (boru, tank, drenaj) | %5-15 | Orta-Yüksek |

**Toplam potansiyel: %20-50 enerji tasarrufu** (kapsamlı bir optimizasyon programı ile).

## İlgili Dosyalar
- Ekipman: `equipment/compressor_screw.md`, `compressor_screw_oilfree.md`, `compressor_piston.md`, `compressor_scroll.md`, `compressor_centrifugal.md`, `compressor_roots.md`
- Benchmark: `benchmarks/compressor_benchmarks.md`
- Çözümler: `solutions/compressor_*.md`
- Formüller: `formulas/compressor_exergy.md`
- Metodoloji: `methodology/compressed_air_audit.md`

## Referanslar
- DOE/AMO, "Improving Compressed Air System Performance: A Sourcebook for Industry"
- Compressed Air Challenge, "Best Practices for Compressed Air Systems"
- Atlas Copco, "Compressed Air Manual," 9th Edition
- Carbon Trust, "Compressed Air — Opportunities for Businesses" (CTG027)
- ISO 8573-1:2010 — Compressed Air Quality Classes
- ISO 11011:2013 — Compressed Air Energy Efficiency Assessment
- CAGI, "Compressed Air & Gas Handbook," 7th Edition
