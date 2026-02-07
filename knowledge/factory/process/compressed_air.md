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
