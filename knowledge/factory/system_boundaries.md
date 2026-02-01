---
title: "Sistem Sınırları ve Ölçüm Noktaları (System Boundaries and Measurement Points)"
category: factory
equipment_type: factory
keywords: [sistem sınırı, kapsam, analiz]
related_files: [factory/methodology.md, factory/data_collection.md, factory/energy_flow_analysis.md]
use_when: ["Analiz sınırları belirlenirken", "Sistem kapsamı tanımlanırken"]
priority: low
last_updated: 2026-01-31
---
# Sistem Sınırları ve Ölçüm Noktaları (System Boundaries and Measurement Points)

> Son güncelleme: 2026-01-31

## Genel Bakış

Fabrika enerji/exergy analizinde doğru sistem sınırlarının tanımlanması, analizin güvenilirliği ve tekrarlanabilirliği için kritik öneme sahiptir. Sistem sınırları, kontrol hacimleri ve ölçüm noktaları ISO 50001 ve ISO 50002 standartlarına uygun olarak belirlenmelidir.

## 1. Sistem Sınırı Tanımı (System Boundary Definition)

### 1.1 Fabrika Sınır Seviyeleri

| Seviye | Kapsam | Kullanım Alanı |
|---|---|---|
| Seviye 0 — Tesis sınırı | Tüm fabrika kampüsü (bina, altyapı, ulaşım dahil) | Kurumsal enerji raporlama, ISO 50001 |
| Seviye 1 — Üretim sınırı | Ana üretim tesisleri ve yardımcı tesisler | Fabrika enerji audit, benchmarking |
| Seviye 2 — Proses sınırı | Belirli üretim hattı veya proses birimi | Proses optimizasyonu |
| Seviye 3 — Ekipman sınırı | Tekil ekipman (kazan, kompresör, chiller vb.) | Ekipman performans değerlendirmesi |
| Seviye 4 — Bileşen sınırı | Ekipman bileşeni (brülör, eşanjör, motor) | Detaylı mühendislik analizi |

### 1.2 Sınır Çizme İlkeleri

```
1. Kapsam netliği: Sınır içindeki ve dışındaki tüm elemanlar listeli olmalı
2. Ölçülebilirlik: Sınırı geçen her akış ölçülebilir noktada olmalı
3. Tutarlılık: Enerji ve kütle dengesi kapanmalı (±%5 kabul edilebilir)
4. Tekrarlanabilirlik: Farklı analistler aynı sonuçlara ulaşabilmeli
5. İlgili standart uyumu: ISO 50001, ISO 50002, EN 16247
```

## 2. Kontrol Hacmi Yaklaşımı (Control Volume Approach)

### 2.1 Termodinamik Kontrol Hacmi

Fabrika kontrol hacmi, termodinamiğin açık sistem (akışlı sistem) analizi kullanılarak tanımlanır:

```
Kütle dengesi:
Σ ṁ_giriş = Σ ṁ_çıkış + dm_cv/dt

Enerji dengesi (kararlı hal):
Σ (ṁ × h)_giriş + Q̇_giriş + Ẇ_giriş = Σ (ṁ × h)_çıkış + Q̇_çıkış + Ẇ_çıkış

Exergy dengesi (kararlı hal):
Σ (ṁ × ex)_giriş + Σ Q̇ᵢ(1-T₀/Tᵢ) + Ẇ = Σ (ṁ × ex)_çıkış + İ_toplam
```

### 2.2 İç İçe Kontrol Hacimleri

Fabrika analizi tipik olarak iç içe kontrol hacimleri kullanır:

```
FABRIKA (Seviye 1)
├── BUHAR SİSTEMİ (Seviye 2)
│   ├── Kazan #1 (Seviye 3)
│   ├── Kazan #2 (Seviye 3)
│   ├── Buhar dağıtım (Seviye 3)
│   └── Kondensat sistemi (Seviye 3)
│
├── BASINÇLI HAVA SİSTEMİ (Seviye 2)
│   ├── Kompresör #1-3 (Seviye 3)
│   ├── Kurutucu/filtre (Seviye 3)
│   └── Dağıtım (Seviye 3)
│
├── SOĞUTMA SİSTEMİ (Seviye 2)
│   ├── Chiller #1-2 (Seviye 3)
│   ├── Soğutma kulesi (Seviye 3)
│   └── Dağıtım (Seviye 3)
│
├── PROSES HATLARI (Seviye 2)
│   ├── Proses A (Seviye 3)
│   ├── Proses B (Seviye 3)
│   └── Proses C (Seviye 3)
│
└── BİNA SİSTEMLERİ (Seviye 2)
    ├── HVAC (Seviye 3)
    ├── Aydınlatma (Seviye 3)
    └── Ofis/destek (Seviye 3)
```

## 3. Ölçüm Noktaları (Measurement Points)

### 3.1 Enerji Giriş Ölçüm Noktaları

| No | Ölçüm Noktası | Parametre | Cihaz | Doğruluk |
|---|---|---|---|---|
| E01 | Doğalgaz sayacı (ana) | Debi [Nm³/h] | Türbin/ultrasonik sayaç | ±%1 |
| E02 | Elektrik ana pano | kW, kVA, PF, kWh | Güç analizörü | ±%0.5 |
| E03 | Fuel oil sayacı | Debi [kg/h] | Koriolis debimetre | ±%0.5 |
| E04 | Su girişi (şebeke) | Debi [m³/h], T [°C] | Ultrasonik debimetre | ±%2 |
| E05 | Hammadde girişi | Kütle [ton/gün] | Kantar | ±%0.5 |

### 3.2 Ana Ekipman Ölçüm Noktaları

| No | Ölçüm Noktası | Parametreler | Cihaz |
|---|---|---|---|
| B01 | Kazan gaz girişi | Debi, basınç, sıcaklık | Alt sayaç, PT |
| B02 | Kazan besleme suyu | Debi, T, P | Debimetre, PT |
| B03 | Kazan buhar çıkışı | Debi, T, P | Orifis/vortex, PT |
| B04 | Baca gazı çıkışı | T, O₂, CO, CO₂ | Baca gazı analizörü |
| C01 | Kompresör elektrik | kW, A, PF | Güç analizörü |
| C02 | Basınçlı hava çıkışı | Debi, P, T | Debimetre, PT |
| C03 | Kompresör soğutucu | T_giriş, T_çıkış | Sıcaklık sensörü |
| CH01 | Chiller elektrik | kW | Güç analizörü |
| CH02 | Chilled water çıkışı | Debi, T_giriş, T_çıkış | Debimetre, PT |
| CH03 | Kondenser su | Debi, T_giriş, T_çıkış | Debimetre, PT |

### 3.3 Atık Akış Ölçüm Noktaları

| No | Ölçüm Noktası | Parametreler | Not |
|---|---|---|---|
| W01 | Baca gazı (her kazan) | T, debi, bileşim | Exergy kaybı hesabı |
| W02 | Soğutma kulesi çıkışı | T_hava, T_su, debi | Atık ısı miktarı |
| W03 | Kondensat deşarjı | T, debi | Geri kazanım potansiyeli |
| W04 | Blowdown deşarjı | T, debi, TDS | Isı geri kazanımı |
| W05 | Proses atık suyu | T, debi | Isı içeriği |
| W06 | Kompresör egzozu | T, debi | Atık ısı |

## 4. Veri Toplama Gereksinimleri (Data Collection Requirements)

### 4.1 Ölçüm Süresi ve Sıklığı

| Analiz Türü | Minimum Süre | Ölçüm Aralığı | Not |
|---|---|---|---|
| Hızlı değerlendirme | 24-72 saat | 1-5 dakika | Temel profil |
| Standart audit | 1-4 hafta | 1 dakika | Tam iş çevrimi |
| Detaylı analiz | 1-12 ay | 1 dakika | Mevsimsel etkileri kapsar |
| Sürekli izleme | Süresiz | 1-15 dakika | EnMS (ISO 50001) kapsamı |

### 4.2 Ölçüm Doğruluğu Gereksinimleri

```
Enerji dengesi kapanma kriteri:
|Σ Giriş - Σ Çıkış| / Σ Giriş ≤ %5 (kabul edilebilir)
|Σ Giriş - Σ Çıkış| / Σ Giriş ≤ %2 (iyi)
|Σ Giriş - Σ Çıkış| / Σ Giriş ≤ %1 (mükemmel)

Kütle dengesi kapanma kriteri:
|Σ ṁ_giriş - Σ ṁ_çıkış| / Σ ṁ_giriş ≤ %3
```

## 5. Alt Sistem Sınırları

### 5.1 Buhar Sistemi Sınırı

```
GİRİŞ:                          ÇIKIŞ:
├── Yakıt (doğalgaz/fuel oil) ─→│                    │─→ Buhar (kullanım noktaları)
├── Besleme suyu ──────────────→│   BUHAR SİSTEMİ    │─→ Baca gazı
├── Elektrik (pompalar, fan) ──→│   KONTROL HACMİ    │─→ Blowdown
├── Yanma havası ──────────────→│                    │─→ Radyasyon/konveksiyon kaybı
├── Kimyasallar (su arıtma) ───→│                    │─→ Kondensat (geri dönmeyen)
                                 └────────────────────┘

Sınır içi: Kazan(lar), economizer, deaeratör, besleme suyu pompası,
          buhar dağıtım hatları, kondensat toplama, blowdown sistemi
```

### 5.2 Basınçlı Hava Sistemi Sınırı

```
GİRİŞ:                          ÇIKIŞ:
├── Elektrik ──────────────────→│                    │─→ Basınçlı hava (kullanım noktaları)
├── Ortam havası ──────────────→│  BASINÇLI HAVA     │─→ Atık ısı (soğutucu)
├── Su (soğutma) ──────────────→│  KONTROL HACMİ     │─→ Kondansat
                                 │                    │─→ Kaçaklar
                                 └────────────────────┘

Sınır içi: Kompresör(ler), aftercooler, kurutucu, filtreler,
          tank(lar), boru dağıtım, drenajlar
```

### 5.3 Soğutma Sistemi Sınırı

```
GİRİŞ:                          ÇIKIŞ:
├── Elektrik ──────────────────→│                    │─→ Chilled water (kullanım noktaları)
├── Su (soğutma kulesi) ───────→│  SOĞUTMA SİSTEMİ   │─→ Atık ısı (kondenser/kule)
                                 │  KONTROL HACMİ     │─→ Su buharlaşması (kulede)
                                 └────────────────────┘

Sınır içi: Chiller(lar), soğutma kulesi, pompalar, boru dağıtım
```

## 6. Sınır Durumları ve Özel Hususlar

### 6.1 Kojenerasyon Sistemi

Kojenerasyon (CHP) durumunda fabrika sınırına ek giriş ve çıkışlar eklenir:

```
Ek giriş: Jeneratör yakıtı
Ek çıkış: Üretilen elektrik (self-consumption veya şebekeye satış)
Ek çıkış: Atık ısıdan üretilen buhar/sıcak su

Dikkat: Şebekeye satılan elektrik fabrika exergy çıkışı olarak sayılır,
iç tüketim ise sistemin bir parçasıdır.
```

### 6.2 Çoklu Ürünlü Fabrikalar

Birden fazla ürün üreten fabrikalarda exergy paylaştırma (allocation) gerekir:

```
Paylaştırma yöntemleri:
1. Kütle bazlı: Ex_ürünA = Ex_toplam × (m_A / m_toplam)
2. Ekonomik bazlı: Ex_ürünA = Ex_toplam × (Gelir_A / Gelir_toplam)
3. Exergy bazlı: Her ürünün exergy içeriğine göre
4. Fiziksel nedensellik: Prosese göre doğrudan atama (tercih edilen)
```

### 6.3 Mevsimsel Değişimler

```
Ortam koşulları sınır analizini etkiler:
- Yaz: T₀ yüksek → soğutma exergisi artar, ısıtma ihtiyacı azalır
- Kış: T₀ düşük → ısıtma exergisi artar, atık ısı geri kazanım potansiyeli artar
- Nem: Yüksek nem → kurutma exergisi artar, soğutma kulesi performansı düşer

Yıllık bazda analiz için aylık ortalama koşullar kullanılabilir.
```

## 7. Pratik Uygulama Kontrol Listesi

### 7.1 Sistem Sınırı Tanımlama Kontrol Listesi

- [ ] Tesis vaziyet planı üzerinde sınır çizildi mi?
- [ ] Tüm enerji giriş noktaları belirlendi mi?
- [ ] Tüm ürün çıkış noktaları belirlendi mi?
- [ ] Tüm atık akışlar tanımlandı mı?
- [ ] İç içe kontrol hacimleri belirlendi mi?
- [ ] Ölçüm noktaları sınır geçiş noktalarıyla eşleşiyor mu?
- [ ] Kütle ve enerji dengesi kapanıyor mu (±%5)?
- [ ] Mevsimsel ve yük değişimleri dikkate alındı mı?

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) — Exergy analizi temel kavramları
- [Veri Toplama](data_collection.md) — Ölçüm cihazları ve protokoller
- [Enerji Akış Analizi](energy_flow_analysis.md) — Enerji dengesi ve Sankey diyagramları
- [Metodoloji](methodology.md) — Fabrika enerji audit metodolojisi
- [Kütle Dengesi](mass_balance.md) — Materyal akış analizi

## Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50002:2014, "Energy audits — Requirements with guidance for use"
- EN 16247-1:2022, "Energy audits — Part 1: General requirements"
- ASHRAE, "Procedures for Commercial Building Energy Audits," 2nd Edition, 2011
- Bejan, A., Tsatsaronis, G., Moran, M., "Thermal Design and Optimization," Wiley, 1996
- US DOE/AMO, "Improving Steam System Performance: A Sourcebook for Industry"
