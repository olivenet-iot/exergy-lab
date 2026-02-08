---
title: "Basınçlı Hava Prosesi (Compressed Air Process)"
category: factory
equipment_type: factory
keywords: [basınçlı hava, compressed air, kompresör, spesifik güç, kaçak, exergy, sistem verimi, DOE]
related_files: [factory/process/gap_analysis_methodology.md, factory/process/sustainability_index.md, compressor/benchmarks.md, factory/process/index.md]
use_when: ["Basınçlı hava sistemi exergy analizi yapılacakken", "Kompresör sistemi performansı değerlendirilecekken", "Basınçlı hava BAT karşılaştırması gerektiğinde"]
priority: high
last_updated: 2026-02-08
---

# Basınçlı Hava Prosesi (Compressed Air Process)

---

## 1. Proses Tanımı

### Nedir?
Basınçlı hava prosesi, atmosferik havayı mekanik enerji (elektrik motoru) ile sıkıştırarak belirli basınçta endüstriyel kullanıma sunma işlemidir. "Dördüncü enerji kaynağı" olarak bilinir (elektrik, gaz, su'dan sonra).

### Nerede Kullanılır?
- Pnömatik aletler ve aktüatörler
- Malzeme taşıma (konveyör, vakum)
- Proses havası (fermentasyon, oksidasyon, kurutma)
- Kontrol havası (enstrümantasyon)
- Temiz oda ve gıda sektörü (filtrelenmiş hava)

### İlgili Ekipmanlar
- Vidalı kompresörler (screw): %80-90 pazar payı
- Pistonlu kompresörler: Küçük ölçek, yüksek basınç
- Santrifüj kompresörler: Büyük ölçek (> 500 kW)
- Kurutucular (refrigerant, desiccant)
- Filtreler, ayırıcılar, depolama tankları
- Dağıtım hatları (borular, bağlantılar)

### Tipik Ölçek
- Küçük: 5 – 50 kW (tek kompresör)
- Orta: 50 – 500 kW (2-4 kompresör)
- Büyük: 500 – 5.000+ kW (merkezi istasyon)

---

## 2. Termodinamik Minimum Exergy

### 2.1 Formül

İzotermik (tersinir) sıkıştırma için minimum güç:

$$W_{min} = \dot{m} \cdot R \cdot T_0 \cdot \ln\left(\frac{P_2}{P_1}\right)$$

| Sembol | Tanım | Birim | Tipik Değer |
|--------|-------|-------|-------------|
| ṁ | Hava kütle debisi | kg/s | — |
| R | Havanın gaz sabiti | kJ/(kg·K) | 0.287 |
| T₀ | Emme sıcaklığı ≈ Çevre sıcaklığı | K | 298.15 |
| P₂ | Çıkış basıncı (mutlak) | kPa | — |
| P₁ | Giriş basıncı (mutlak) | kPa | 101.325 |

### 2.1b İzotermik Sıkıştırma Türetimi (1. Yasa Temeli)

İzotermik (sabit sıcaklık) sıkıştırma, minimum iş gerektiren tersinir prosestir. Türetim:

**Adım 1: 1. Yasa — kapalı sistem**
İdeal gaz için iç enerji sıcaklığa bağlıdır. İzotermik proseste T = sabit → ΔU = 0:
$$Q = W$$

**Adım 2: İdeal gaz hal denklemi**
$$PV = mRT \Rightarrow V = \frac{mRT}{P}$$

**Adım 3: Tersinir iş**
$$W = \int_{P_1}^{P_2} V \, dP = \int_{P_1}^{P_2} \frac{mRT}{P} \, dP = mRT \ln\left(\frac{P_2}{P_1}\right)$$

Sürekli akış sistemi için:
$$\dot{W}_{min} = \dot{m} R T_0 \ln\left(\frac{P_2}{P_1}\right)$$

**Adım 4: Neden minimum?**
- İzotermik sıkıştırmada sıkıştırma ısısı anlık olarak çevreye atılır (T = sabit)
- Adyabatik sıkıştırmada ısı atılamaz → sıcaklık artar → daha fazla iş gerekir
- Polotropik sıkıştırma: n = 1 (izotermik) ile n = k (adyabatik) arasında

**Sıkıştırma yöntemlerinin karşılaştırması (7 bar_g, T₁ = 25 °C):**

| Yöntem | Polotropik n | W (kJ/kg) | W/W_izotermik |
|--------|------------|-----------|---------------|
| İzotermik | 1.0 | 176.8 | 1.00 (minimum) |
| Kademeli (2 kademe, ara soğutma) | ~1.15 | 198 | 1.12 |
| Polotropik (tipik vidalı) | 1.3 | 228 | 1.29 |
| Adyabatik (isentropik) | 1.4 | 252 | 1.43 |

> **Sonuç:** Gerçek kompresörler izotermik idealin %29-43 fazlası iş tüketir. Ara soğutmalı kademeli sıkıştırma, bu farkı %12'ye düşürür.

**Kaynak:** Moran & Shapiro (2014), Bölüm 6.9 — Kompresör termodinamiği; CAGI Handbook (2016), Ch. 3.

### 2.2 Basınca Bağlı Minimum Spesifik Enerji

| Basınç (bar_g) | P₂/P₁ | ln(P₂/P₁) | W_min (kJ/kg) | W_min (kW/m³/min) |
|----------------|--------|-----------|---------------|---------------------|
| 4 | 4.95 | 1.599 | 136.8 | 2.73 |
| 6 | 6.91 | 1.933 | 165.4 | 3.30 |
| 7 | 7.90 | 2.067 | 176.8 | 3.53 |
| 8 | 8.89 | 2.185 | 186.9 | 3.73 |
| 10 | 10.87 | 2.386 | 204.1 | 4.07 |
| 12 | 12.84 | 2.553 | 218.4 | 4.36 |

> **Anahtar Değer:** 7 bar_g basınçlı hava için minimum spesifik güç ≈ **3.53 kW/(m³/min)**. Gerçek sistemler 5-8 kW/(m³/min) aralığında çalışır.

### 2.3 Çözümlü Örnek

**Problem:** 7 bar_g, 10 m³/min kapasiteli basınçlı hava sistemi.

```
P₁ = 101.325 kPa (1.013 bar_abs)
P₂ = (7 + 1.013) × 100 = 801.3 kPa (8.013 bar_abs)
T₀ = 298.15 K
ṁ = 10 m³/min × 1.205 kg/m³ / 60 = 0.2008 kg/s

W_min = 0.2008 × 0.287 × 298.15 × ln(8.013/1.013)
      = 0.2008 × 0.287 × 298.15 × 2.069
      = 35.5 kW

Spesifik güç (minimum) = 35.5 / 10 = 3.55 kW/(m³/min)
```

Gerçek kompresör gücü (tipik): 65 kW → η_izotermik = 35.5/65 = 54.6%

```
ESI = W_min / W_actual = 35.5 / 65 = 0.546 (sadece kompresör)
```

**Ancak sistem ESI'si çok farklıdır:**
Kaçaklar (%25), boş çalışma (%15), basınç düşümü (%5), yapay talep (%10):
```
W_actual_sistem = 65 / (1 − 0.25 − 0.15 − 0.05) = 65 / 0.55 = 118 kW

ESI_sistem = 35.5 / 118 = 0.30 → Derece C (ama basınçlı hava için aslında "iyi")
```

> **Kritik:** Kompresör ESI ile sistem ESI arasında büyük fark var. Her zaman **sistem ESI'sini** raporla.

**Kaynak:** Compressed Air & Gas Institute (CAGI); DOE Air Master+.

### 2.4 Çözümlü Örnek: Sistem Seviyesi Kayıp Şelale Analizi

**Problem:** 75 kW vidalı kompresör sistemi. Gerçek enerji tüketimi ölçümlerle 120 kW (tüm yardımcı ekipman dahil). Nereye gidiyor?

**Sistem Bileşenleri ve Kayıp Dağılımı:**

```
Giriş: 120 kW elektrik (sistem toplam)
├── Kompresör motoru: 75 kW
│   ├── Motor kayıpları (%5): 3.8 kW
│   ├── Mekanik kayıplar (%3): 2.3 kW
│   └── Sıkıştırma işi: 68.9 kW
│       ├── İzotermik minimum: 35.5 kW (Ex_min)
│       └── Sıkıştırma irreversibilitesi: 33.4 kW
├── Kurutucu: 15 kW
│   ├── Rejenerasyon enerjisi: 12 kW
│   └── Fan/kontrol: 3 kW
├── Soğutucu (aftercooler): 5 kW fan
├── Kontrol sistemi boş çalışma: 12 kW
├── Kaçak kayıpları (eşdeğer): 18 kW
│   (Kaçak oranı: 18/75 = %24 — ciddi!)
└── Dağıtım basınç düşümü (eşdeğer): 5 kW

Yararlı çıkış: 120 − (3.8+2.3+33.4+15+5+12+18+5) = 25.5 kW
```

**Kayıp Şelale Tablosu:**

| # | Kayıp Kaynağı | kW | % | Kümülatif % | Öncelik |
|---|---------------|-----|---|-----------|---------|
| 1 | Sıkıştırma irreversibilitesi | 33.4 | 27.8% | 27.8% | Orta (kompresör tipi) |
| 2 | Kaçaklar | 18.0 | 15.0% | 42.8% | **ÇOK YÜKSEK** |
| 3 | Kurutucu | 15.0 | 12.5% | 55.3% | Orta (tip seçimi) |
| 4 | Boş çalışma | 12.0 | 10.0% | 65.3% | **YÜKSEK** (VFD) |
| 5 | Motor kayıpları | 3.8 | 3.2% | 68.5% | Düşük |
| 6 | Basınç düşümü | 5.0 | 4.2% | 72.7% | Orta |
| 7 | Aftercooler | 5.0 | 4.2% | 76.9% | Düşük |
| 8 | Mekanik | 2.3 | 1.9% | 78.8% | Düşük |
| — | **Yararlı exergy çıkışı** | **25.5** | **21.2%** | **100%** | — |

**ESI hesabı:**
```
Ex_min (yararlı hava) = 35.5 × (120−18)/120 = 35.5 × 0.85 = 30.2 kW
(kaçak olmayan kısım için minimum)

ESI_sistem = 30.2 / 120 = 0.252
```

> **Kritik bulgu:** 120 kW giren enerjinin sadece %21.2'si yararlı basınçlı hava exergy'si olarak çıkıyor. Kaçak giderme (%24→%10) ve VFD ile toplam %20-25 kW tasarruf mümkün.

---

## 3. Tipik Endüstriyel Exergy Tüketimi

### 3.1 Spesifik Güç Aralıkları (Sistem Seviyesi)

| Alt-kategori | Spesifik Güç | Birim | Sistem ESI |
|-------------|-------------|-------|------------|
| En iyi pratik | 4.5 – 5.5 | kW/(m³/min) @ 7 bar | 0.12 – 0.15 |
| İyi | 5.5 – 6.5 | kW/(m³/min) @ 7 bar | 0.09 – 0.12 |
| Ortalama | 6.5 – 8.0 | kW/(m³/min) @ 7 bar | 0.07 – 0.09 |
| Kötü | 8.0 – 12.0 | kW/(m³/min) @ 7 bar | 0.05 – 0.07 |

### 3.2 Kompresör Tipi ve Verimi

| Kompresör Tipi | η_izotermik | η_ex (kompresör) | Kapasite Aralığı |
|----------------|-----------|-------------------|------------------|
| Vidalı (yağlı) | %50-70 | %45-65 | 5 – 500 kW |
| Vidalı (yağsız) | %45-60 | %40-55 | 15 – 500 kW |
| Pistonlu | %55-75 | %50-70 | 1 – 50 kW |
| Santrifüj | %60-80 | %55-75 | 200 – 5.000 kW |

### 3.3 Sistem Kayıp Kaynakları

| Kaynak | Tipik Pay | Açıklama |
|--------|-----------|----------|
| Kompresör irreversibilitesi | %35 – %50 | Adyabatik vs izotermik fark |
| Hava kaçakları | %20 – %35 | 1 mm delik @ 7 bar ≈ 1.2 kW |
| Boş çalışma / modülasyon | %10 – %20 | Kısmi yük kontrolü |
| Basınç düşümü (dağıtım) | %5 – %10 | Borular, filtreler, kurutucular |
| Yapay talep | %5 – %15 | Gereğinden yüksek sistem basıncı |
| Kurutucu enerji tüketimi | %5 – %10 | Özellikle rejeneratif tip |
| Aftercooler / soğutma | %2 – %5 | Sıkıştırma ısısının atılması |

---

## 4. BAT Referansı

### 4.1 DOE Compressed Air Challenge / Air Master+

| Parametre | BAT Değeri | Koşul |
|-----------|-----------|-------|
| Spesifik güç (sistem) | 4.5 – 5.5 kW/(m³/min) | 7 bar_g, merkezi sistem |
| Kaçak oranı | < %10 | Düzenli ultrasonik test |
| Basınç bandı | ±0.3 bar | VFD + depolama tank |
| Kısmi yük kontrolü | VFD (inverter) | İlk kompresöre VFD |

### 4.2 EU BREF ENE 2009 (Energy Efficiency)

| Parametre | BAT Açıklaması |
|-----------|----------------|
| Sistem tasarımı | Merkezi + desantralize hibrit tasarım |
| Basınç seviyesi | İhtiyaca göre minimum basınç, çoklu basınç hatları |
| Kaçak yönetimi | Periyodik ultrasonik kaçak tespiti + onarım programı |
| Isı geri kazanımı | Kompresör soğutma suyu/havasından ısı geri kazanımı (%70-94 elde edilebilir) |
| Kontrol sistemi | Master controller, VFD, depolama optimizasyonu |

### 4.3 BAT Exergy Değerleri

| Sistem Tipi | BAT Spesifik Güç | BAT Sistem ESI | Kaynak |
|-------------|-------------------|----------------|--------|
| VFD + kaçak < %10 + optimum basınç | 4.5 kW/(m³/min) | 0.14 – 0.15 | DOE Air Master+ |
| Isı geri kazanımlı + VFD | 4.5 kW/(m³/min) + ısı | 0.20 – 0.25 | ENE BREF 2009, tahmini |
| Turbo (büyük ölçek) + VGV | 4.0 kW/(m³/min) | 0.15 – 0.18 | CAGI data |

## 4b. DOE Air Master+ Metodolojisi

### 4b.1 Air Master+ Nedir?

DOE (US Department of Energy) Compressed Air Challenge programı kapsamında geliştirilen **Air Master+**, basınçlı hava sistemlerinin kapsamlı analizini yapan bir metodoloji ve yazılımdır.

**Analiz adımları:**
1. Mevcut durum profilleme (24h/7gün ölçüm)
2. Kompresör performans haritalaması
3. Kaçak testi (ultrasonik)
4. Kontrol stratejisi değerlendirmesi
5. Isı geri kazanım potansiyeli
6. Alternatif senaryolar ve tasarruf hesabı

### 4b.2 Ultrasonik Kaçak Tespiti Detayı

| Kaçak Çapı | Kaçak Debisi (7 bar) | Güç Kaybı | Yıllık Maliyet (0.10 €/kWh, 8000h) |
|-----------|---------------------|-----------|--------------------------------------|
| 0.8 mm | 0.4 m³/min | 0.5 kW | 400 € |
| 1.6 mm | 1.6 m³/min | 1.2 kW | 960 € |
| 3.2 mm | 6.4 m³/min | 4.8 kW | 3.840 € |
| 6.4 mm | 25.6 m³/min | 19.2 kW | 15.360 € |

> **Ampirik kural:** Tipik bir tesiste ultrasonik kaçak testi 50-200 kaçak noktası tespit eder. Onarım maliyeti genellikle < 5.000 €, yıllık tasarruf 10.000-50.000 €.

### 4b.3 Ölçüm Protokolü

Air Master+ metodolojisinde doğru analiz için aşağıdaki ölçüm noktaları gereklidir:

| Ölçüm Parametresi | Sensör Tipi | Konum | Örnekleme Sıklığı |
|-------------------|-------------|-------|-------------------|
| Güç tüketimi (kW) | Güç analizörü | Her kompresör paneli | 1 sn (minimum 1 dk) |
| Hava debisi (m³/min) | Termal kütle akış ölçer | Ana hat çıkışı | 1 sn |
| Sistem basıncı (bar) | Piezorezistif transmitter | Kollektör çıkışı + kullanım noktaları | 1 sn |
| Emme sıcaklığı (°C) | Pt100 / RTD | Kompresör girişi | 1 dk |
| Çıkış sıcaklığı (°C) | Pt100 / RTD | Kompresör çıkışı | 1 dk |
| Çiğ noktası (°C dp) | Kapasitif dp sensörü | Kurutucu çıkışı | 5 dk |
| Yağ içeriği (mg/m³) | Fotoakustik | Ana hat (gerekirse) | Spot ölçüm |

**Ölçüm süresi:** Minimum 7 gün (tam üretim haftası), ideal 14-30 gün (mevsimsel varyasyonları yakalamak için).

**Veri analizi adımları:**
1. Yük profili çıkarma (demand profile) — zaman vs debi grafiği
2. Spesifik güç hesabı (kW/(m³/min)) — zaman ortalaması ve anlık
3. Basınç bandı analizi — min/max/ortalama ve dalgalanma genliği
4. Boş çalışma süresi tespiti — güç > 0 ama debi ≈ 0 periyotları
5. Kompresör yük dağılımı — her kompresörün çalışma saatleri ve yük oranı

### 4b.4 Kontrol Stratejileri Karşılaştırması

| Kontrol Yöntemi | Kısmi Yük Verimi | Avantaj | Dezavantaj |
|-----------------|-----------------|---------|-----------|
| Yük/boş (load/unload) | %60-75 @ %50 yük | Basit, güvenilir | Boş çalışmada %25-40 güç |
| Modülasyon (throttling) | %70-80 @ %50 yük | Kademesiz | Düşük yükte verimsiz |
| VFD (inverter) | %85-95 @ %50 yük | En verimli kısmi yük | Yüksek yatırım maliyeti |
| VGV (variable geometry) | %80-90 @ %50 yük | Santrifüj için | Sadece turbo tip |
| Master controller + VFD | %90-97 @ %50 yük | Optimum çoklu kompresör | En yüksek yatırım |

**Kısmi yük güç tüketimi formülü (ampirik):**

```
Yük/boş: P_kısmi = P_tam × [0.25 + 0.75 × (Q/Q_max)]
Modülasyon: P_kısmi = P_tam × [0.20 + 0.80 × (Q/Q_max)]
VFD: P_kısmi = P_tam × (Q/Q_max)^2.5 (fan yasası benzeri)
```

> **VFD seçim kuralı:** VFD en çok "trim" (son kalan, yükü dengeleyici) kompresöre takılmalıdır. Baz yük kompresörleri VFD'siz tam yükte çalışmalıdır — VFD tam yükte %2-3 kayıp ekler.

---

## 4c. Sektörel Varyasyonlar

### 4c.1 Otomotiv Sektörü

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| Sistem basıncı | 6-7 bar_g | Pnömatik aletler, boya |
| Kapasite | 500-5000 kW | Büyük merkezi istasyon |
| Hava kalitesi | ISO 8573 Sınıf 2.4.2 | Boya için yüksek kalite |
| Kaçak oranı | %20-35 | Geniş dağıtım ağı |
| Tipik ESI | 0.06-0.10 | Sistem kayıpları yüksek |

### 4c.2 Gıda Sektörü

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| Sistem basıncı | 7-10 bar_g | Paketleme, taşıma |
| Hava kalitesi | ISO 8573 Sınıf 1.2.1 | Gıda teması — yağsız, kuru |
| Kurutucu tipi | Dessicant (adsorpsiyon) | Çiğ noktası −40 °C |
| Kurutucu enerji payı | %15-25 | Yüksek kalite → yüksek maliyet |
| Tipik ESI | 0.05-0.08 | Kurutucu yükü nedeniyle düşük |

### 4c.3 Tekstil Sektörü

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| Sistem basıncı | 5-7 bar_g | Dokuma tezgahları |
| Talep profili | Çok değişken | Tezgah sayısına bağlı |
| VFD gereksinimi | Kritik | Değişken talep |
| Tipik ESI | 0.07-0.12 | Orta |

### 4c.4 İlaç Sektörü

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| Sistem basıncı | 7-8 bar_g | Temiz oda, proses |
| Hava kalitesi | ISO 8573 Sınıf 1.1.1 | En yüksek kalite |
| Yedeklilik | N+1 minimum | Kesintisiz üretim |
| Tipik ESI | 0.05-0.08 | Kalite gereksinimleri nedeniyle |

### 4c.5 Çimento Sektörü

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| Sistem basıncı | 4-6 bar_g | Pnömatik taşıma, filtre |
| Kapasite | 200-2000 kW | Yüksek debi, düşük basınç |
| Hava kalitesi | ISO 8573 Sınıf 4.6.4 | Düşük kalite yeterli |
| Ortam koşulları | Tozlu, sıcak | Filtre bakımı kritik |
| Tipik ESI | 0.08-0.14 | Düşük basınç avantajı |

### 4c.6 Cam ve Seramik Sektörü

| Parametre | Tipik Değer | Not |
|-----------|-------------|-----|
| Sistem basıncı | 6-8 bar_g | Şekillendirme, soğutma |
| Özel gereksinim | Yüksek T ortam | Emme havası sıcaklığı yüksek |
| Emme T etkisi | %3-5 verim kaybı / 10 °C | Soğuk emme havası kritik |
| Tipik ESI | 0.06-0.10 | Ortam sıcaklığı etkisi |

### 4c.7 Sektör Karşılaştırma Özet Tablosu

| Sektör | Basınç (bar_g) | ISO 8573 Sınıfı | Tipik ESI | Kritik Parametre |
|--------|---------------|-----------------|-----------|-----------------|
| Otomotiv | 6-7 | 2.4.2 | 0.06-0.10 | Kaçak oranı |
| Gıda | 7-10 | 1.2.1 | 0.05-0.08 | Kurutucu yükü |
| Tekstil | 5-7 | 3.4.3 | 0.07-0.12 | Talep değişkenliği |
| İlaç | 7-8 | 1.1.1 | 0.05-0.08 | Hava kalitesi |
| Çimento | 4-6 | 4.6.4 | 0.08-0.14 | Filtre bakımı |
| Cam/Seramik | 6-8 | 3.4.3 | 0.06-0.10 | Emme sıcaklığı |

---

## 5. Tipik Exergy Yıkım Kaynakları

| Sıra | Kaynak | Pay (%) | İyileştirme Potansiyeli |
|------|--------|---------|------------------------|
| 1 | Kompresör irreversibilitesi | 35 – 50 | Orta (daha verimli kompresör tipi) |
| 2 | Hava kaçakları | 20 – 35 | Çok yüksek (kaçak tespiti + onarım) |
| 3 | Boş çalışma / modülasyon | 10 – 20 | Yüksek (VFD, master controller) |
| 4 | Yapay talep (aşırı basınç) | 5 – 15 | Yüksek (basınç optimizasyonu) |
| 5 | Dağıtım basınç düşümü | 5 – 10 | Orta (boru çapı, layout) |
| 6 | Kurutucu/soğutucu | 5 – 10 | Düşük-orta (tip seçimi) |

---

## 6. İyileştirme Stratejileri

| # | Strateji | Tahmini Tasarruf | ROI | Detay |
|---|----------|-----------------|-----|-------|
| 1 | **Kaçak tespiti ve onarımı** | %15-30 enerji | 0-6 ay | Ultrasonik dedektör; her 1 mm delik ≈ 1.2 kW; en hızlı geri dönüş |
| 2 | **VFD (değişken hız sürücü)** | %15-35 enerji | 1-3 yıl | Trim kompresöre VFD; kısmi yükte dramatik tasarruf |
| 3 | **Basınç optimizasyonu** | %7-10 enerji | 0-1 yıl | Her 1 bar düşüş ≈ %7 enerji tasarrufu (ampirik kural) |
| 4 | **Kompresör ısı geri kazanımı** | %70-94 atık ısı | 1-3 yıl | Soğutma suyu/havası → bina/proses ısıtma; çok yüksek potansiyel |
| 5 | **Master controller** | %5-12 enerji | 1-2 yıl | Çoklu kompresör koordinasyonu, band minimizasyonu |

### 6a. Basınç Optimizasyonu Detayı

Sistem basıncının her 1 bar düşürülmesi yaklaşık **%6-7 enerji tasarrufu** sağlar:

**Ampirik kural türetimi:**
```
Polotropik sıkıştırma: W ∝ [(P₂/P₁)^((n-1)/n) − 1]
7 bar_g → 8.013 bar_abs: W₁ ∝ (8.013/1.013)^0.286 − 1 = 1.086
6 bar_g → 7.013 bar_abs: W₂ ∝ (7.013/1.013)^0.286 − 1 = 1.016

Tasarruf = (1.086 − 1.016) / 1.086 = 6.4%
```

**Basınç düşürme kontrol listesi:**

| Adım | Aksiyon | Açıklama |
|------|---------|----------|
| 1 | Basınç profili ölçümü | Tüm kullanım noktalarında minimum gerekli basınç tespiti |
| 2 | Darboğaz tespiti | Yetersiz boru çapı, tıkalı filtre, uzun hatlar |
| 3 | Basınç düşümü giderme | Filtre değişimi, boru çapı artırma (ΔP < 0.3 bar hedef) |
| 4 | Yapay talep analizi | Gereksiz yere yüksek basınçla beslenen noktalar |
| 5 | Çoklu basınç hattı | Yüksek basınç gerektiren noktalar için ayrı hat veya lokal booster |
| 6 | Basınç/akış kontrol | Sistem basıncını talebe göre dinamik ayarlama |

**Yapay talep (artificial demand) etkisi:**
Sistem basıncı gereğinden yüksek olduğunda, açık uçlu tüketim noktaları (üfleme nozulları, kaçaklar) daha fazla hava tüketir. Bu "yapay talep"dir:

```
Q_kaçak ∝ P^0.65 (orifice flow)
7 bar_g → 6 bar_g: Q_kaçak azalma = 1 − (7.013/8.013)^0.65 = %9
```

> **Önemli:** Basınç düşürme hem kompresör güç tüketimini (%6-7/bar) hem de kaçak debisini (%8-10/bar) azaltır. Çift yönlü tasarruf.

### 6b. Kompresör Isı Geri Kazanım Detayı

Sıkıştırma prosesinde giriş enerjisinin **%80-94'ü ısıya** dönüşür:

| Geri Kazanım Noktası | Sıcaklık Aralığı | Geri Kazanım Oranı | Uygulama |
|----------------------|-------------------|---------------------|----------|
| Yağ soğutucusu (yağlı vidalı) | 60-90 °C | %70-80 | Sıcak su üretimi, bina ısıtma |
| Aftercooler | 40-60 °C | %10-15 | Düşük T ön ısıtma |
| Motor soğutma (su soğutmalı) | 50-70 °C | %5-10 | Ek sıcak su |
| Hava soğutmalı (kanal) | 40-50 °C | %50-60 | Bina ısıtma (sıcak hava) |

**Exergy değerlendirmesi:**
Geri kazanılan ısının exergy değeri düşüktür (Carnot faktörü 0.08-0.20), ancak bu ısı yoksa ayrıca üretilmesi gerekir. Karşılaştırma:

```
75 kW kompresör, %75 ısı geri kazanım = 56 kW termal (70 °C)
Alternatif: 56 kW ısıyı doğal gaz kazanı ile üretmek:
  Q_yakıt = 56/0.90 = 62 kW → Ex = 62 × 1.04 = 64.5 kW

Isı geri kazanım ile kaçınılan exergy = 64.5 kW
Sistem ESI'ye etkisi: ESI_yeni = (35.5 + 64.5) / 75 → anlamsız!

Doğru yaklaşım: Geri kazanım sistemin ex_actual'ını düşürmez,
ama fabrika seviyesinde toplam exergy tüketimini azaltır.
```

> **AI Kuralı:** Kompresör ısı geri kazanımını HER ZAMAN öner (ısı talebi varsa). Ancak ESI hesabında kompresör ESI'sına değil, fabrika toplam exergy'sine etkisini göster.

---

## 7. Yorumlama Rehberi (AI Kullanımı İçin)

### 7.1 ESI Değerlendirmesi

```
EĞER Sistem ESI > 0.15 → "Basınçlı hava için dünya sınıfı — ESI Derece D ama prosese göre çok iyi"
EĞER Sistem ESI 0.10-0.15 → "Basınçlı hava için iyi — tipik BAT seviyesi"
EĞER Sistem ESI 0.07-0.10 → "Basınçlı hava için orta — iyileştirme fırsatları var"
EĞER Sistem ESI 0.05-0.07 → "Basınçlı hava için zayıf — acil aksiyon gerekli"
EĞER Sistem ESI < 0.05 → "Basınçlı hava için kritik — büyük kaçak veya sistem sorunu"
```

> **Önemli:** Basınçlı hava ESI'si doğası gereği düşüktür (%5-15). ESI A-F skalasında hep D-E aralığında kalır. Bu normal! Proses bazlı değerlendirme kullan.

### 7.2 Anahtar Kontrol Noktaları

| Parametre | İyi | Orta | Kötü |
|-----------|-----|------|------|
| Spesifik güç | < 5.5 kW/(m³/min) | 5.5-7 | > 7 |
| Kaçak oranı | < %10 | %10-25 | > %25 |
| Boş çalışma süresi | < %10 | %10-25 | > %25 |
| Basınç bandı | < ±0.3 bar | ±0.3-0.5 | > ±0.5 bar |

### 7.3 Hızlı Teşhis

```
EĞER spesifik güç > 7 kW/(m³/min):
  → Öncelikle kaçak testi, basınç seviyesi, boş çalışma kontrol et
  → "Basınçlı hava sisteminde ciddi enerji israfı tespit edildi"

EĞER kompresör η_ex > %55 AMA sistem ESI < 0.08:
  → "Kompresör verimi iyi ancak sistem kayıpları çok yüksek"
  → "Kaçak, basınç düşümü ve kontrol stratejisini incele"

EĞER ısı geri kazanım yok:
  → "Kompresör atık ısısının %70-94'ü geri kazanılabilir"
  → "Sıcak su (70-90 °C) veya sıcak hava olarak kullanım değerlendir"
```

### 7.4 Sektöre Göre Özel Teşhis

```
EĞER sektör = "gıda" VE kurutucu_tipi = "desiccant":
  → "Adsorpsiyon kurutucu enerji tüketimi toplam sistemin %15-25'ini oluşturabilir"
  → "Dönüşümlü ısıtmalı (externally heated) veya blower purge tipi değerlendir"
  → "%40-60 kurutucu enerji tasarrufu mümkün"

EĞER sektör = "otomotiv" VE kaçak_oranı > %25:
  → "Otomotiv tesislerinde geniş dağıtım ağı nedeniyle kaçak kritik"
  → "Bölgesel kaçak izleme programı ve aylık ultrasonik tarama öner"
  → "Kaçak oranını %25'ten %10'a düşürmek: %15-20 sistem tasarrufu"

EĞER sektör = "tekstil" VE VFD_yok:
  → "Dokuma tezgahları çok değişken talep profili oluşturur"
  → "VFD olmadan yük/boş kontrol %25-40 enerji israfı yaratır"
  → "VFD + master controller ile %20-35 tasarruf beklenir"

EĞER sektör = "ilaç" VE yedeklilik < "N+1":
  → "İlaç sektöründe üretim kesintisi tolere edilemez"
  → "N+1 yedekliliği sağlanmalı, ancak yedek kompresör rotasyon programı ile bakım optimize edilmeli"
```

### 7.5 Çoklu Kompresör Sistemi Teşhis

```
EĞER kompresör_sayısı >= 3 VE master_controller = yok:
  → "3+ kompresörlü sistemde master controller %5-12 tasarruf sağlar"
  → "Baz yük + trim yaklaşımı: en verimli kompresörler tam yükte, VFD'li kompresör değişken yükte"

EĞER tüm_kompresörler_aynı_kapasitede:
  → "Farklı kapasiteli kompresör kombinasyonu daha verimli kısmi yük yönetimi sağlar"
  → "Örnek: 75 kW (baz) + 45 kW (baz) + 37 kW VFD (trim)"

EĞER depolama_tankı_hacmi < (toplam_debi × 3):
  → "Yetersiz depolama hacmi kompresör sık açma/kapama (cycling) yaratır"
  → "Minimum depolama: 3-5 gal/cfm (DOE önerisi) veya 3-8 L/(m³/h)"
  → "Yeterli depolama ile basınç bandı daraltılabilir → yapay talep azalır"
```

### 7.6 Exergy Muhasebesi ve Raporlama Kuralları

| Metrik | Nasıl Hesaplanır | Nasıl Raporlanır |
|--------|-----------------|-----------------|
| Kompresör ESI | W_min / W_kompresör | "Kompresör birimi exergy verimi" |
| Sistem ESI | W_min / W_sistem_toplam | "Sistem geneli exergy sürdürülebilirlik indeksi" |
| Kaçak eşdeğer güç | (kaçak_oranı) × W_kompresör | "Kaçaklara harcanan güç eşdeğeri" |
| Isı geri kazanım potansiyeli | 0.80 × W_kompresör | "Geri kazanılabilir termal güç" |
| Net exergy yıkımı | W_sistem − W_min | "Toplam exergy yıkımı" |

```
AI raporlama şablonu:

1. Sistem ESI: [değer] ([derece]) — basınçlı hava prosesi için [iyi/orta/zayıf/kritik]
2. En büyük kayıp: [kaynak] (%[değer]) — [iyileştirme önerisi]
3. Hızlı kazanım (quick win): [aksiyon] → [tasarruf kW] → [ROI ay]
4. Isı geri kazanım: [potansiyel kW termal] → [uygulama önerisi]
5. Uzun vadeli: [strateji] → [toplam tasarruf potansiyeli %]
```

---

## İlgili Dosyalar

- `compressor/benchmarks.md` — Kompresör ekipman benchmark
- `factory/process/gap_analysis_methodology.md` — Boşluk analizi formülleri
- `factory/process/sustainability_index.md` — ESI derecelendirme
- `factory/heat_integration.md` — Isı geri kazanım fırsatları
- `factory/waste_heat_recovery.md` — Atık ısı geri kazanım teknolojileri

## Referanslar

1. US DOE (2003). *Improving Compressed Air System Performance: A Sourcebook for Industry*. Office of Energy Efficiency.
2. Compressed Air & Gas Institute — CAGI (2016). *Compressed Air and Gas Handbook*. 7th ed.
3. European Commission, JRC (2009). *Reference Document on Best Available Techniques for Energy Efficiency (ENE BREF)*. Ch. 3.7 — Compressed Air.
4. Saidur, R., Rahim, N.A. & Hasanuzzaman, M. (2010). "A review on compressed-air energy use and energy savings." *Renewable and Sustainable Energy Reviews*, 14(4), 1135-1153.
5. Dincer, I. & Rosen, M.A. (2013). *Exergy*. Elsevier. — Kompresör exergy analizi.
6. US DOE (2003). *Improving Compressed Air System Performance: A Sourcebook for Industry*. Ch. 4 — System Assessment, Ch. 8 — Heat Recovery.
7. ISO 8573-1:2010. *Compressed air — Part 1: Contaminants and purity classes*. — Hava kalitesi sınıflandırması.
8. Radgen, P. & Blaustein, E. (2001). *Compressed Air Systems in the European Union*. Fraunhofer ISI. — EU basınçlı hava enerji tüketimi verileri.
9. Kaya, D., Phelan, P. & Chau, D. (2002). "Energy conservation in compressed-air systems." *International Journal of Energy Research*, 26(9), 837-849.
10. CAGI (2016). *Compressed Air and Gas Handbook*. 7th ed. — Sıkıştırma termodinamiği, Ch. 3.
