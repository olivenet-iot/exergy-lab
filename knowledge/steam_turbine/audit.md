---
title: "Buhar Türbini Performans Denetimi — Steam Turbine Performance Audit"
category: reference
equipment_type: steam_turbine
keywords: [buhar türbini, denetim, ASME PTC 6, performans testi, heat rate, SSC, KPI]
related_files: [steam_turbine/formulas.md, steam_turbine/benchmarks.md, steam_turbine/solutions/efficiency_improvement.md, steam_turbine/solutions/maintenance.md]
use_when: ["Türbin performans denetimi yapılırken", "Ölçüm gereksinimleri belirlenirken", "KPI tanımları gerektiğinde"]
priority: medium
last_updated: 2026-01-31
---
# Buhar Türbini Performans Denetimi — Steam Turbine Performance Audit

> Son güncelleme: 2026-01-31

## 1. Denetim Amacı ve Kapsamı

### 1.1 Amaç

```
Buhar türbini performans denetiminin amaçları:
1. Mevcut performansın referans (design) değerlerle karşılaştırılması
2. Verim kayıplarının tespit edilmesi ve ölçülmesi
3. İyileştirme fırsatlarının belirlenmesi ve ROI hesaplanması
4. Bakım planlama için veri sağlanması
5. CHP sistemi genel performansının değerlendirilmesi
6. Exergy analizi ile gerçek termodinamik kayıpların ortaya konması
```

### 1.2 Kapsam Seviyeleri

| Seviye | Adı | Süre | İçerik | Maliyet |
|--------|-----|------|--------|---------|
| 1 | Ön değerlendirme (Walk-through) | 1-2 gün | Mevcut veri analizi, görsel kontrol | €2,000-5,000 |
| 2 | Standart denetim | 3-5 gün | Ölçüm + analiz, ASME PTC 6 basitleştirilmiş | €5,000-15,000 |
| 3 | Detaylı denetim | 1-2 hafta | Tam ASME PTC 6, kademe bazlı analiz, exergy | €15,000-40,000 |

## 2. ASME PTC 6 Bazlı Performans Testi

### 2.1 ASME PTC 6 Genel Bakış

```
ASME PTC 6 — Performance Test Code for Steam Turbines:

Amaç: Buhar türbini performansının hassas ve tekrarlanabilir
ölçümü için standart prosedür.

İki seviye:
1. PTC 6 — Full Test (Tam test):
   - Yüksek doğruluk (±0.25% heat rate)
   - Özel enstrümantasyon gerekli
   - Genellikle kabul testi (acceptance test) için

2. PTC 6S — Simplified Procedure (Basitleştirilmiş):
   - Daha düşük doğruluk (±1-2% heat rate)
   - Mevcut tesis enstrümantasyonu ile yapılabilir
   - Rutin performans izleme için uygun

Test koşulları:
- Kararlı durum (steady state): min 30 dk kararlı çalışma
- Yük: Nominal yükün >%90'ında test tercih edilir
- Çevre koşulları kayıt altına alınmalı
- Minimum 4 tekrar ölçüm seti
```

### 2.2 Test Prosedürü

```
Adım 1: Hazırlık (1-2 gün öncesi)
├── Tüm ölçüm cihazlarının kalibrasyonunu doğrula
├── Türbini kararlı yüke getir (>%90 nominal)
├── Tüm drenajları kapat, kaçakları minimize et
├── Çıkış sıcaklığı ve basıncı kararlı hale getir
└── Kayıt formlarını hazırla

Adım 2: Test çalışması
├── Kararlı durum kontrolü: 30 dk bekleme
├── Test süresi: Minimum 1 saat (PTC 6S) veya 4 saat (PTC 6)
├── Ölçüm frekansı: Her 5 dk (veya sürekli DCS kaydı)
├── Minimum 4 bağımsız ölçüm seti
└── Anomali kontrolü: ±%2'den fazla sapma → seti reddet

Adım 3: Veri analizi
├── Ortalama değerler hesapla (her ölçüm seti)
├── Standart sapma ve belirsizlik hesapla
├── Design koşullarına düzelt (correction curves)
├── Heat rate, SSC, η_is hesapla
└── Exergy analizi yap
```

## 3. Ölçüm Gereksinimleri

### 3.1 Birincil Ölçümler (Zorunlu)

| Parametre | Sembol | Birim | Konum | Doğruluk | Ölçüm Yöntemi |
|-----------|--------|-------|-------|----------|----------------|
| Giriş buhar basıncı | P_giriş | bar | Türbin stop vanası önce | ±0.25% | Basınç transmitter |
| Giriş buhar sıcaklığı | T_giriş | °C | Türbin giriş flanşı | ±1°C | Termokupl (K/J tipi) |
| Çıkış buhar basıncı | P_çıkış | bar | Türbin çıkış | ±0.25% | Basınç transmitter |
| Çıkış buhar sıcaklığı | T_çıkış | °C | Türbin çıkış | ±1°C | Termokupl |
| Buhar debisi | ṁ | kg/s | Giriş borusu | ±1% | Orifis / Vortex / Coriolis |
| Jeneratör elektrik gücü | Ẇ_elek | kW | Jeneratör terminali | ±0.5% | Güç analizörü |
| Devir sayısı | n | rpm | Türbin mili | ±0.1% | Tachometre |

### 3.2 İkincil Ölçümler (Önerilen)

| Parametre | Sembol | Birim | Amaç |
|-----------|--------|-------|------|
| Kondenser basıncı | P_kond | mbar | Vakum performansı (yoğuşmalı) |
| Kondenser suyu giriş T | T_cw_in | °C | Kondenser performansı |
| Kondenser suyu çıkış T | T_cw_out | °C | Kondenser ısı transferi |
| Çekiş buhar basıncı | P_ext | bar | Extraction performansı |
| Çekiş buhar sıcaklığı | T_ext | °C | Extraction performansı |
| Çekiş buhar debisi | ṁ_ext | kg/s | CHP HPR hesabı |
| Yağ basıncı | P_yağ | bar | Rulman/yağ sistemi |
| Yağ sıcaklığı | T_yağ | °C | Rulman/yağ sistemi |
| Titreşim | v | mm/s | Mekanik durum |
| Eksenel pozisyon | δ | mm | Rotor termal genleşme |

### 3.3 CHP Denetimi İçin Ek Ölçümler

| Parametre | Sembol | Birim | Amaç |
|-----------|--------|-------|------|
| Kazan yakıt debisi | ṁ_yakıt | Nm³/h veya kg/h | CHP toplam verim |
| Yakıt alt ısıl değer | LHV | kJ/kg veya kJ/Nm³ | Enerji girişi |
| Proses buhar debisi | ṁ_proses | kg/s | HPR hesabı |
| Kondensat dönüş T | T_kond | °C | Proses ısısı |
| Kondensat dönüş debisi | ṁ_kond | kg/s | Kondensat geri dönüş oranı |
| Kazan besleme suyu T | T_bw | °C | Kazan verimi |
| Şebeke elektrik alışı | Ẇ_şebeke | kW | Öz tüketim oranı |

## 4. KPI Tanımları (Key Performance Indicators)

### 4.1 Türbin Performans KPI'ları

```
1. İzentropik Verim (Isentropic Efficiency):
   η_is = (h_giriş - h_çıkış) / (h_giriş - h_çıkış,is) × 100 [%]
   Hedef: Benchmark değerine göre (bkz. benchmarks.md)

2. Heat Rate (Isı Hızı):
   HR = Q̇_yakıt / Ẇ_net [kJ/kWh]
   HR = 3,600 / η_net [kJ/kWh]
   Hedef: Design HR ± %3

3. Spesifik Buhar Tüketimi (SSC):
   SSC = ṁ_toplam / Ẇ_net [kg/kWh]
   Hedef: Design SSC ± %5

4. Mekanik Verim:
   η_mek = Ẇ_türbin_mil / Ẇ_türbin_termal
   Hedef: >%97

5. Jeneratör Verimi:
   η_jen = Ẇ_elek / Ẇ_mil
   Hedef: >%96

6. Availability (Kullanılabilirlik):
   A = (Toplam saat - Plansız duruş) / Toplam saat × 100 [%]
   Hedef: >%95

7. Kapasite Faktörü:
   CF = Ẇ_ortalama / Ẇ_nominal × 100 [%]
```

### 4.2 CHP Denetim KPI'ları

```
8. Toplam Enerji Verimi:
   η_enerji = (Ẇ_elek + Q̇_ısı) / Q̇_yakıt × 100 [%]
   Hedef: >%80 (BP CHP), >%75 (extraction CHP)

9. Exergy Verimi:
   η_exergy = (Ẇ_elek + Ėx_ısı) / Ėx_yakıt × 100 [%]
   Hedef: bkz. benchmarks.md

10. Birincil Enerji Tasarrufu (PES):
    PES = 1 - 1 / (η_elek/η_ref_elek + η_ısı/η_ref_ısı) × 100 [%]
    Hedef: >%10 (EU yüksek verimli CHP tanımı)

11. Isı/Güç Oranı (HPR):
    HPR = Q̇_ısı / Ẇ_elek
    Design HPR ile karşılaştır

12. Eşdeğer Elektrik Verimi:
    η_elek,eşdeğer = Ẇ_elek / (Q̇_yakıt - Q̇_ısı/η_kazan_ref) × 100 [%]

13. Öz Tüketim Oranı:
    SCR = Ẇ_elek,CHP / Ẇ_elek,toplam × 100 [%]
    (CHP elektriğinin ne kadarı kendi tüketildiği)
```

## 5. Performans Test Sonuçları Değerlendirmesi

### 5.1 Design Karşılaştırma Tablosu

```
Sonuç tablosu formatı:

| Parametre | Design | Ölçülen | Sapma [%] | Durum |
|-----------|--------|---------|-----------|-------|
| η_is | — | — | — | ✓/⚠/✗ |
| HR | — | — | — | ✓/⚠/✗ |
| SSC | — | — | — | ✓/⚠/✗ |
| Ẇ_elek | — | — | — | ✓/⚠/✗ |
| η_enerji (CHP) | — | — | — | ✓/⚠/✗ |
| HPR | — | — | — | ✓/⚠/✗ |

Durum kriterleri:
✓ = Sapma < %3 (kabul edilebilir)
⚠ = Sapma %3-8 (dikkat, izleme gerekli)
✗ = Sapma > %8 (müdahale gerekli)
```

### 5.2 Exergy Analizi Sonuç Formatı

```
Exergy dengesi raporu:

┌─────────────────────────────────────────────────┐
│ EXERGY DENGESİ — [Türbin Adı]                   │
├─────────────────────────────────────────────────┤
│ Giriş exergisi: _____ kW (%100)                 │
│                                                  │
│ Çıkışlar:                                       │
│   Elektrik (iş):      _____ kW (___%)           │
│   Proses buhar exergy: _____ kW (___%)  [CHP]   │
│   Kondenser exergy:    _____ kW (___%)  [cond]   │
│                                                  │
│ Kayıplar:                                       │
│   Türbin iç tersinmezlik: _____ kW (___%)       │
│   Mekanik kayıplar:       _____ kW (___%)       │
│   Jeneratör kayıpları:    _____ kW (___%)       │
│   Sızdırmazlık kayıpları: _____ kW (___%)       │
│   Kondensere atılan:       _____ kW (___%)      │
│                                                  │
│ Exergy verimi (iş): _____ %                     │
│ Exergy verimi (CHP): _____ %                    │
└─────────────────────────────────────────────────┘
```

## 6. Kademe Performans Analizi (Stage Performance)

### 6.1 Kademe Basınç Kontrolü

```
Her kademe grubu için basınç oranı izleme:

Beklenen basınç oranı (design):
PR_design = P_giriş,kademe / P_çıkış,kademe

Ölçülen basınç oranı:
PR_ölçülen = P_giriş,kademe / P_çıkış,kademe

Sapma:
ΔPR = (PR_ölçülen - PR_design) / PR_design × 100 [%]

Yorumlama:
- ΔPR > +%5: Olası kanat birikintisi (fouling) veya aşınma
- ΔPR < -%5: Olası iç kaçak (internal leakage)
- |ΔPR| < %3: Normal aralık
```

### 6.2 Sıcaklık-Entropi Kontrolü

```
Kademe çıkış sıcaklığı kontrolü:

T_çıkış,beklenen = f(P_çıkış, h_çıkış_beklenen)

ΔT = T_çıkış,ölçülen - T_çıkış,beklenen

ΔT > +5°C: Kademe verimi düşük (aşınma, kaçak)
ΔT < -3°C: Ölçüm hatası veya buhar koşulları değişmiş
```

## 7. Denetim Raporu Şablonu

### 7.1 Rapor Yapısı

```
1. Yönetici Özeti
   - Mevcut performans durumu
   - Tespit edilen kayıplar (kW ve EUR/yıl)
   - Önerilen iyileştirmeler ve ROI

2. Türbin Teknik Bilgileri
   - Marka, model, yıl, kapasite
   - Design koşulları ve garanti değerleri
   - Bakım geçmişi, son overhaul tarihi

3. Ölçüm Sonuçları
   - Ölçüm koşulları ve cihazlar
   - Ham veri tabloları
   - Design ile karşılaştırma

4. Performans Analizi
   - Heat rate hesaplaması
   - İzentropik verim hesaplaması
   - Kısmi yük performansı

5. Exergy Analizi
   - Exergy dengesi
   - Exergy yıkım dağılımı
   - CHP exergy verimi (varsa)

6. İyileştirme Önerileri
   - Öncelik sıralı öneri listesi
   - Her öneri için: Tasarruf, yatırım, SPP
   - Uygulama takvimi

7. Ekler
   - Ölçüm sertifikaları
   - Detaylı hesap tabloları
   - Buhar tabloları referansı
```

## 8. Denetim Sıklığı ve İzleme

### 8.1 Önerilen Denetim Programı

| Aktivite | Sıklık | Süre | Kapsam |
|----------|--------|------|--------|
| Sürekli izleme (online) | Sürekli | — | Heat rate, η_is, titreşim |
| Aylık performans raporu | Aylık | 1 gün | KPI trend analizi |
| Yıllık performans testi | Yıllık | 2-3 gün | PTC 6S bazlı test |
| Detaylı denetim | 3-5 yılda | 1-2 hafta | Tam PTC 6, exergy |
| Overhaul öncesi denetim | Overhaul öncesi | 2-3 gün | Baseline oluşturma |
| Overhaul sonrası test | Overhaul sonrası | 2-3 gün | Performans doğrulama |

### 8.2 Online İzleme Parametreleri

```
Sürekli izlenmesi gereken parametreler:

Kritik (alarm gerekli):
- Titreşim (radyal ve eksenel): Alarm > 4 mm/s
- Yağ basıncı: Alarm < 1.5 bar
- Eksenel pozisyon: Alarm > ±0.5 mm
- Egzoz sıcaklığı (yoğuşmalı): Alarm > design + 10°C

Performans (trend izleme):
- Heat rate: Haftalık trend
- İzentropik verim: Haftalık trend
- Kademe basınçları: Aylık trend
- Çıkış sıcaklıkları: Aylık trend
- Kondenser vakum: Günlük izleme
```

## 9. Dikkat Edilecek Hususlar

```
1. Ölçüm belirsizliği:
   - Debi ölçümü en büyük belirsizlik kaynağıdır (±1-3%)
   - Heat rate belirsizliği ≈ ±1-2% (PTC 6S)
   - Coriolis debimetre tercih edilir (±0.5%)

2. Kararlı durum kontrolü:
   - Yük değişimi: <%2 nominal güç
   - Basınç değişimi: <%1
   - Sıcaklık değişimi: <±2°C
   - Minimum 30 dk kararlı çalışma

3. CHP denetiminde ek zorluklar:
   - Proses buhar debisi ölçümü genellikle yoktur
   - Kondensat dönüş ölçümü zor olabilir
   - Kazan verimi ayrıca belirlenmelidir
   - Yakıt kalörimetrik değeri doğrulanmalıdır

4. Mevsimsel etki:
   - Yoğuşmalı türbinlerde soğutma suyu T etkisi
   - Yaz: +3-5°C soğutma suyu → -%1-2 güç
   - Kış: -5-10°C soğutma suyu → +%1-3 güç
   - Test sonuçlarını design koşullarına düzelt

5. Güvenlik:
   - Buhar sızdırma noktaları: Yanık riski
   - Yüksek gürültü bölgeleri: İşitme koruması
   - Dönen ekipman: Koruyucu mesafe
   - Sıcak yüzeyler: İzolasyon kontrolü
```

## İlgili Dosyalar

- [Formüller](formulas.md) — Exergy hesaplama formülleri
- [Benchmarklar](benchmarks.md) — Performans karşılaştırma verileri
- [Verim İyileştirme](solutions/efficiency_improvement.md) — İyileştirme çözümleri
- [Bakım](solutions/maintenance.md) — Bakım planlaması
- [Yük Eşleştirme](solutions/load_matching.md) — Yük optimizasyonu
- [Kazan Denetim](../boiler/audit.md) — CHP kapsamında kazan denetimi
- [Fabrika Veri Toplama](../factory/data_collection.md) — Veri toplama rehberi

## Referanslar

- ASME PTC 6 (2004). *Steam Turbines Performance Test Codes*, ASME.
- ASME PTC 6S (2020). *Procedures for Routine Performance Tests of Steam Turbines*, ASME.
- Cotton, K.C. (1998). *Evaluating and Improving Steam Turbine Performance*, Cotton Fact Inc.
- API 612 (2005). *Petroleum, Petrochemical and Natural Gas Industries — Steam Turbines*, API.
- ISO 50002 (2014). *Energy Audits — Requirements with Guidance for Use*, ISO.
- EN 16247-3 (2014). *Energy Audits — Part 3: Processes*, CEN.
- Kotas, T.J. (1985). *The Exergy Method of Thermal Plant Analysis*, Butterworths.
- Bejan, A. (2016). *Advanced Engineering Thermodynamics*, 4th Edition, Wiley.
- Turner, W.C. & Doty, S. (2013). *Energy Management Handbook*, 9th Edition, Fairmont Press.
