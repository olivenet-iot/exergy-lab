---
title: "Enerji Gözden Geçirme (Energy Review — ISO 50001 Clause 6.3)"
category: factory
equipment_type: factory
keywords: [enerji gözden geçirme, energy review, SEU, önemli enerji kullanımı, Pareto analizi, enerji profili, enerji akış diyagramı, exergy analizi]
related_files: [factory/energy_management/INDEX.md, factory/energy_management/iso_50001_overview.md, factory/energy_management/baseline_enpi.md, factory/energy_management/enpi_guide.md, factory/energy_management/audit_methodology.md, factory/energy_management.md]
use_when: ["Enerji gözden geçirme süreci planlandığında", "SEU belirleme gerektiğinde", "Enerji profili oluşturulacağında"]
priority: high
last_updated: 2026-02-01
---

# Enerji Gözden Geçirme (Energy Review — ISO 50001 Clause 6.3)

> Son güncelleme: 2026-02-01

## 1. Genel Bakış

Enerji gözden geçirme (Energy Review), ISO 50001:2018 Madde 6.3 gereği organizasyonun enerji performansını analiz etme ve iyileştirme fırsatlarını tespit etme sürecidir. Standardın en kritik planlama adımlarından biri olup EnPI, EnB, hedefler ve eylem planlarının temelini oluşturur.

### 1.1 ISO 50001 Madde 6.3 Gereksinimleri

```
ISO 50001:2018 — Madde 6.3 zorunlulukları:

a) Enerji kaynaklarının ve geçmiş/mevcut tüketimin analizi
b) Önemli enerji kullanımlarının (SEU) belirlenmesi:
   ├── Mevcut enerji performansının değerlendirilmesi
   ├── İlgili değişkenlerin tanımlanması
   ├── Enerji performansını etkileyen kişilerin belirlenmesi
   └── İyileştirme fırsatlarının tespit edilmesi
c) Enerji gözden geçirmenin belirli aralıklarla güncellenmesi
d) Planlı veya önemli değişiklikler sonrası güncelleme
```

### 1.2 Enerji Gözden Geçirme ile Diğer Süreçlerin İlişkisi

| Süreç | Energy Review'ın Katkısı |
|-------|--------------------------|
| EnPI tanımlama (6.4) | SEU bazında performans göstergeleri |
| EnB oluşturma (6.5) | Baseline dönemi ve değişkenler |
| Hedef belirleme (6.6) | İyileştirme potansiyeli ve önceliklendirme |
| Operasyonel kontrol (8.1) | SEU bazında kontrol gereksinimleri |
| İzleme (9.1) | Neyin, ne sıklıkla izleneceği |

## 2. Enerji Profili Oluşturma (Energy Profile Development)

### 2.1 Enerji Kaynakları Analizi

```
Enerji kaynağı envanteri adımları:
1. Tüm enerji giriş noktalarının belirlenmesi
2. Her kaynak için son 12-36 aylık tüketim verisi
3. TEP (ton eşdeğer petrol) dönüşümü
4. Kaynak bazında yüzde dağılım
5. Maliyet bazında yüzde dağılım

Tipik bir Türk üretim tesisi — Enerji kaynağı dağılımı:

| Enerji Kaynağı | Tüketim [TEP/yıl] | Enerji Payı [%] | Maliyet Payı [%] |
|----------------|-------------------:|------------------:|-------------------:|
| Doğalgaz       | 4.200              | 52.5              | 42.0               |
| Elektrik       | 3.000              | 37.5              | 50.0               |
| LPG            | 400                | 5.0               | 5.0                |
| Motorin        | 300                | 3.8               | 2.5                |
| Biyokütle      | 100                | 1.2               | 0.5                |
| TOPLAM         | 8.000              | 100.0             | 100.0              |

Dikkat: Enerji payı ile maliyet payı farklıdır — Elektrik birim maliyeti
doğalgazın ~3 katıdır. Maliyet perspektifi yatırım kararlarını etkiler.
```

### 2.2 Tüketim Dağılımı ve Trendler

```
Yıllık/aylık trend analizi kontrol noktaları:

1. Mevsimsel desen:
   ├── Kış artışı → Isıtma yükü (doğalgaz)
   ├── Yaz artışı → Soğutma yükü (elektrik)
   └── Sabit bant → Baseload (üretim ekipmanları)

2. Üretim korelasyonu:
   ├── Üretim arttığında orantılı artış → Normal
   ├── Üretim düşerken tüketim sabit → Verimsiz baseload
   └── Artış oranı üretimden fazla → Verim düşüşü

3. Anormal noktalar:
   ├── Ani sıçrama → Ekipman arızası/ekleme
   ├── Ani düşüş → Duruş/kapasite azaltma
   └── Drift (kademeli artış) → Bakım eksikliği
```

## 3. SEU Belirleme (Significant Energy Uses Identification)

### 3.1 SEU Seçim Kriterleri

```
ISO 50001:2018 — SEU aşağıdaki özelliklerden en az birini taşır:

1. Önemli enerji tüketim payı:
   ├── Genellikle toplam tüketimin %5'inden fazla
   ├── Pareto analizinde kümülatif %80'in içinde
   └── Maliyet bazında önemli pay

2. Önemli iyileştirme potansiyeli:
   ├── Benchmark ile arasında >%10 fark
   ├── Bilinen ve uygulanabilir iyileştirme çözümü
   └── Exergy verimi sektör ortalamasının altında

3. Yasal/stratejik önem:
   ├── Mevzuat gereği izlenmesi gereken ekipman
   ├── Karbon emisyon yoğun proses
   └── Stratejik üretim hattı

Her SEU için zorunlu belirleme:
├── Mevcut enerji performansı (EnPI)
├── İlgili değişkenler (relevant variables)
├── Enerji performansını etkileyen kişiler
└── İyileştirme fırsatları
```

### 3.2 Pareto Analizi (80/20 Kuralı)

```
Örnek: Gıda fabrikası — Yıllık 10.000 TEP

| Sistem/Proses         | TEP/yıl | Pay [%] | Kümülatif [%] | SEU? |
|-----------------------|--------:|--------:|---------------:|------|
| Kompresörler (soğuk)  | 3.500   | 35.0    | 35.0           | ✓    |
| Kazanlar (buhar)      | 3.000   | 30.0    | 65.0           | ✓    |
| Chiller sistemi       | 2.000   | 20.0    | 85.0           | ✓    |
| Aydınlatma            | 1.000   | 10.0    | 95.0           | —    |
| Diğer (ofis, IT, vb.) | 500     | 5.0     | 100.0          | —    |

SEU'lar: İlk 3 sistem → %85 toplam tüketim
Karar: Aydınlatma (%10) iyileştirme potansiyeli yüksekse SEU olarak eklenebilir

Pareto grafiği verileri (ExergyLab dashboard):
- X ekseni: Sistemler (azalan sıra)
- Y sol ekseni: TEP/yıl (bar chart)
- Y sağ ekseni: Kümülatif % (çizgi grafik)
- Referans çizgi: %80 eşiği
```

### 3.3 SEU Kayıt Formu Şablonu

| Alan | Açıklama | Örnek |
|------|----------|-------|
| SEU kodu | Benzersiz tanımlayıcı | SEU-001 |
| SEU adı | Sistem/proses adı | Basınçlı hava sistemi |
| Enerji kaynağı | Elektrik, doğalgaz, vb. | Elektrik |
| Yıllık tüketim | TEP veya MWh | 3.500 TEP |
| Toplam içindeki payı | Yüzde | %35 |
| EnPI | Performans göstergesi | SPC: 7.2 kW/(m³/min) |
| İlgili değişkenler | Tüketimi etkileyen faktörler | Üretim miktarı, ortam sıcaklığı |
| Mevcut performans | Benchmark karşılaştırma | Sektör ortalaması: 6.5 |
| İyileştirme fırsatları | Belirlenen ECM'ler | VSD, kaçak onarım, basınç düşürme |
| Sorumlu kişi/ekip | SEU operasyonu | Bakım Mühendisi, Operatörler |
| Son güncelleme | Gözden geçirme tarihi | 2026-01-15 |

## 4. Değişkenlerin Belirlenmesi (Relevant Variables Identification)

### 4.1 Tipik İlgili Değişkenler

| SEU | İlgili Değişkenler | Birim | Kontrol Edilebilir? |
|-----|-------------------|-------|---------------------|
| Basınçlı hava | Üretim miktarı, ortam sıcaklığı | ton, °C | Kısmen |
| Buhar sistemi | Buhar talebi, ortam sıcaklığı, HDD | ton/h, °C, °C·gün | Kısmen |
| Soğutma | Soğutma yükü, ortam sıcaklığı, CDD | kW, °C, °C·gün | Kısmen |
| Isıl işlem | İşlenen parça sayısı, hedef sıcaklık | adet, °C | Evet |
| HVAC | HDD/CDD, iç mekan doluluk, dış sıcaklık | °C·gün, kişi, °C | Kısmen |
| Pompalama | Debi talebi, basınç kaybı | m³/h, bar | Kısmen |
| Aydınlatma | Çalışma saatleri, gün ışığı düzeyi | saat, lux | Evet |

### 4.2 Değişken-Tüketim İlişkisi (Scatter Plot Analizi)

```
Korelasyon analizi adımları:

1. Scatter plot (saçılma grafiği):
   - Her potansiyel değişken vs enerji tüketimi
   - Görsel ilişki kontrolü (doğrusal, eğrisel, yok)

2. Pearson korelasyon katsayısı (r):
   - |r| > 0.7  → Güçlü ilişki → Modele dahil et
   - 0.4 < |r| ≤ 0.7 → Orta ilişki → Değerlendir
   - |r| ≤ 0.4 → Zayıf ilişki → Dışarıda bırak

3. Çoklu regresyon:
   E = β₀ + β₁·X₁ + β₂·X₂ + ... + ε
   - p-value < 0.05 olan değişkenleri tut
   - VIF < 5 (çoklu doğrusallık kontrolü — Variance Inflation Factor)
   - Adjusted R² ile model karşılaştır
```

### 4.3 Regresyon Analizi Temelleri

```
Basit doğrusal regresyon:
  E = β₀ + β₁ × X + ε

Çoklu regresyon:
  E = β₀ + β₁ × X₁ + β₂ × X₂ + ε

Formüller:
  R² = 1 - (SS_res / SS_tot)
  Adjusted R² = 1 - [(1 - R²)(n - 1) / (n - k - 1)]
  RMSE = √(Σ(E_i - Ê_i)² / n)
  CV-RMSE = (RMSE / Ē) × 100 [%]

Burada:
  β₀ = Sabit terim (baseload — üretimden bağımsız tüketim) [kWh]
  β₁ = Eğim katsayısı (birim değişken başına enerji) [kWh/birim]
  X  = İlgili değişken (üretim, HDD, CDD, vb.)
  n  = Veri noktası sayısı
  k  = Değişken sayısı

Örnek — Buhar sistemi:
  Buhar [ton/ay] = 120 + 0.85 × Üretim [ton/ay] + 2.1 × HDD [°C·gün/ay]
  R² = 0.91, p₁ < 0.001, p₂ < 0.01
  → Üretim ve HDD her ikisi de istatistiksel olarak anlamlı değişkenler
```

## 5. Mevcut Enerji Performansının Değerlendirilmesi (Current Performance Assessment)

### 5.1 Benchmark Karşılaştırma

| SEU | Mevcut Değer | Sektör Ortalaması | En İyi Uygulama (BAT) | Fark [%] |
|-----|-------------|-------------------|----------------------|----------|
| Kompresörler (SPC) | 7.2 kW/(m³/min) | 6.5 kW/(m³/min) | 5.8 kW/(m³/min) | +10.8 / +24.1 |
| Kazan (yakma verimi) | %86 | %90 | %95 | -4.4 / -9.5 |
| Chiller (COP) | 4.2 | 5.0 | 6.0 | -16.0 / -30.0 |
| Pompa (verim) | %62 | %72 | %82 | -13.9 / -24.4 |

### 5.2 Enerji Yoğunluğu Hesaplama

```
Enerji yoğunluğu formülleri:

Spesifik enerji tüketimi (SEC):
  SEC = E_toplam / P_üretim [kWh/ton] veya [TEP/ton]

Ciro bazlı enerji yoğunluğu:
  EI = E_toplam / Ciro [MWh/M€] veya [TEP/M€]

Alan bazlı enerji yoğunluğu:
  EUI = E_toplam / A_bina [kWh/m²·yıl]

Exergy verimi (fabrika düzeyinde):
  η_ex = Σ(Ė_çıkış_i) / Σ(Ė_giriş_i) × 100 [%]
```

## 6. İyileştirme Fırsatlarının Belirlenmesi (Improvement Opportunity Identification)

### 6.1 Quick Scan Yöntemi

```
Quick scan ile hızlı fırsat tespiti:

1. Gözlemsel kontroller (walk-through):
   ├── Kaçak sesleri (basınçlı hava, buhar)
   ├── Sıcak yüzeyler (yalıtım eksikliği)
   ├── Boş çalışan ekipmanlar (idling)
   ├── Açık kapılar/pencereler (iklimlenmiş alan)
   └── Gereksiz çalışan aydınlatma/ekipman

2. Veri bazlı kontroller:
   ├── Gece/hafta sonu baseload analizi
   ├── EnPI trend bozulması
   ├── Set point uyumsuzlukları
   └── Bakım kayıt anormallikleri

3. Termal kamera tarama:
   ├── Buhar kapanı arızaları
   ├── Elektrik panosu aşırı ısınma
   ├── Yalıtım eksiklikleri
   └── Isı kaçak noktaları
```

### 6.2 Detaylı Analiz

```
Detaylı iyileştirme fırsatı değerlendirme:

Fırsat sınıflandırma:
| Kategori | Yatırım | Geri Ödeme | Örnekler |
|----------|---------|------------|----------|
| Quick Win | <€5.000 | <6 ay | Set point ayarı, kaçak onarım |
| Düşük yatırım | €5-25.000 | 6-18 ay | VSD retrofit, yalıtım |
| Orta yatırım | €25-100.000 | 1-3 yıl | Ekonomizer, ısı geri kazanım |
| Yüksek yatırım | >€100.000 | 3-7 yıl | CHP, absorption chiller |

ECM değerlendirme matrisi:
| Kriter | Ağırlık | Puanlama (1-5) |
|--------|---------|----------------|
| Enerji tasarrufu (TEP/yıl) | %30 | 1: <10, 2: 10-50, 3: 50-150, 4: 150-500, 5: >500 |
| Geri ödeme süresi | %25 | 1: >7y, 2: 5-7y, 3: 3-5y, 4: 1-3y, 5: <1y |
| Uygulama kolaylığı | %20 | 1: Major proje, 5: Hemen uygulanabilir |
| Çevresel fayda | %15 | 1: Düşük, 5: Yüksek CO₂ azaltma |
| Stratejik uyum | %10 | 1: Düşük, 5: Şirket stratejisi ile örtüşüyor |
```

## 7. Exergy Perspektifinde Enerji Gözden Geçirme (Exergy-Enhanced Energy Review)

### 7.1 Geleneksel Enerji Audit vs Exergy Audit

| Özellik | Geleneksel Enerji Audit | Exergy Audit |
|---------|------------------------|-------------|
| Temel yasa | Termodinamiğin 1. yasası (enerji korunumu) | 1. + 2. yasa (exergy yıkımı) |
| Ölçü | Enerji miktarı (kW, kWh) | Enerji kalitesi (exergy, kW) |
| Kazan verimi | %85-95 (düşük kayıp görünür) | %35-45 (gerçek termodinamik kayıp) |
| COP değeri | COP = 4-6 (verimli görünür) | η_ex = %20-35 (Carnot sınırına göre) |
| Kayıp sıralaması | Enerji bazlı (yanıltıcı olabilir) | Exergy bazlı (termodinamik gerçeklik) |
| Entegrasyon fırsatı | Sınırlı tespit | Cross-equipment fırsatlar belirgin |

### 7.2 SEU Exergy Derecelendirmesi

```
Aynı gıda fabrikası — Exergy perspektifi:

| SEU               | Enerji Kaybı [kW] | Exergy Kaybı [kW] | Exergy Verimi [%] |
|-------------------|-------------------:|-------------------:|-------------------:|
| Kazanlar (buhar)  | 150                | 580                | 38                 |
| Kompresörler      | 420                | 390                | 15                 |
| Chiller sistemi   | 180                | 280                | 22                 |
| Aydınlatma        | 85                 | 85                 | 10                 |

ÖNEMLİ FARK:
- Enerji bazlı kayıp sıralaması: Kompresörler > Chiller > Kazanlar > Aydınlatma
- Exergy bazlı kayıp sıralaması: Kazanlar > Kompresörler > Chiller > Aydınlatma

→ Exergy analizi, kazan sisteminin en büyük termodinamik kayıp kaynağı
  olduğunu ortaya koyar. Enerji analizi bu farkı yakalayamaz çünkü
  kazan "enerji verimi" %85+ görünür, ancak yüksek sıcaklıkta yakma
  ile düşük sıcaklıkta kullanım arasındaki exergy uyumsuzluğu büyüktür.
→ ExergyLab bu farkı otomatik olarak hesaplar ve raporlar.
```

### 7.3 ExergyLab'ın Sağladığı Ek İçgörüler

```
ExergyLab ile zenginleştirilmiş energy review:

1. Exergy Sankey diyagramı:
   ├── Tesis genelinde exergy akışı görselleştirme
   ├── Her noktadaki exergy yıkımı (kW ve %)
   └── Kayıp noktalarının hızlı tespiti

2. Cross-equipment fırsatlar:
   ├── Kompresör atık ısısı → Kazan ön ısıtma
   ├── Baca gazı ısısı → ORC ile elektrik üretimi
   ├── Soğutma kondenser ısısı → Sıcak su ihtiyacı
   └── Buhar flash → Düşük basınçlı buhar kullanımı

3. AI destekli yorumlama:
   ├── Exergy verimlilik benchmarking
   ├── Otomatik iyileştirme önerileri
   ├── Termodinamik kalite uyumsuzluk tespiti
   └── Sektörel en iyi uygulama karşılaştırma

4. SEU önceliklendirme:
   ├── Exergy bazlı Pareto (gerçek kayıp sıralaması)
   ├── İyileştirme potansiyeli: IP = (1 - η_ex) × Ė_giriş [kW]
   └── Exergy maliyet analizi (€/kW_ex tasarruf)
```

## 8. Çalışılmış Örnek — Gıda Fabrikası Enerji Gözden Geçirme

### 8.1 Fabrika Profili

```
Fabrika: Orta ölçekli gıda işleme tesisi (süt ürünleri)
Lokasyon: Türkiye — İç Anadolu (iklim bölgesi 3)
Yıllık üretim: 50.000 ton/yıl
Çalışan: 250 kişi
Çalışma: 3 vardiya, yılda 330 gün
Yıllık enerji tüketimi: 8.500 TEP
Yıllık enerji maliyeti: €1.200.000
```

### 8.2 Adım 1 — Enerji Kaynağı Analizi

| Kaynak | Yıllık Tüketim | TEP | Pay [%] | Maliyet [€] | Maliyet Pay [%] |
|--------|---------------|-----|---------|-------------|-----------------|
| Doğalgaz | 4.800.000 m³ | 4.320 | 50.8 | 480.000 | 40.0 |
| Elektrik | 18.500 MWh | 3.700 | 43.5 | 650.000 | 54.2 |
| Motorin | 120.000 lt | 360 | 4.2 | 55.000 | 4.6 |
| LPG | 30.000 kg | 120 | 1.4 | 15.000 | 1.3 |
| **TOPLAM** | | **8.500** | **100** | **1.200.000** | **100** |

### 8.3 Adım 2 — SEU Belirleme

```
Pareto analizi sonucu:

| #  | Sistem           | TEP/yıl | Pay [%] | Kümülatif [%] | SEU |
|----|------------------|--------:|--------:|---------------:|-----|
| 1  | Soğutma kompresör| 2.550   | 30.0    | 30.0           | ✓   |
| 2  | Buhar kazanları  | 2.125   | 25.0    | 55.0           | ✓   |
| 3  | Pastörizasyon    | 1.275   | 15.0    | 70.0           | ✓   |
| 4  | Paketleme        | 850     | 10.0    | 80.0           | ✓   |
| 5  | CIP (temizlik)   | 595     | 7.0     | 87.0           | —   |
| 6  | Aydınlatma       | 425     | 5.0     | 92.0           | —   |
| 7  | HVAC             | 340     | 4.0     | 96.0           | —   |
| 8  | Ofis + Diğer     | 340     | 4.0     | 100.0          | —   |

SEU'lar (1-4): %80 toplam tüketim
CIP sistemi: Pareto dışı, ancak ısı geri kazanım potansiyeli nedeniyle izlemeye alınır
```

### 8.4 Adım 3 — Değişken Analizi ve Adım 4 — Fırsatlar

```
Her SEU için değişken ve fırsat özeti:

SEU-001 Soğutma kompresörleri:
  Değişkenler: Üretim miktarı (r=0.85), dış sıcaklık (r=0.72)
  Mevcut COP: 3.8 | Benchmark: 5.0 | Fırsat: %24
  ECM: VSD retrofit, kondenser temizlik, free cooling (kış)

SEU-002 Buhar kazanları:
  Değişkenler: Buhar talebi (r=0.92), dış sıcaklık (r=0.65)
  Mevcut verim: %86 | Benchmark: %92 | Fırsat: %6.5
  ECM: Ekonomizer, O₂ trim kontrol, kondensat geri kazanım, yalıtım

SEU-003 Pastörizasyon:
  Değişkenler: Süt işleme miktarı (r=0.95)
  Mevcut SEC: 45 kWh/ton | Benchmark: 35 kWh/ton | Fırsat: %22
  ECM: Rejenerasyon oranı artırma, ısı geri kazanım

SEU-004 Paketleme:
  Değişkenler: Paketlenen ürün miktarı (r=0.88)
  Mevcut SEC: 15 kWh/ton | Benchmark: 12 kWh/ton | Fırsat: %20
  ECM: Boş çalışma kontrolü, servo motor yükseltme
```

### 8.5 Sonuç Özeti

```
Gıda fabrikası enerji gözden geçirme sonuçları:

Toplam iyileştirme potansiyeli: 1.020 TEP/yıl (%12)
Tasarruf değeri: ~€144.000/yıl

Öncelik sıralaması (exergy bazlı):
1. Buhar kazanları — Exergy kayıp: 580 kW (en yüksek)
2. Soğutma kompresörleri — Exergy kayıp: 390 kW
3. Pastörizasyon — Exergy kayıp: 180 kW
4. Paketleme — Exergy kayıp: 95 kW

Cross-equipment fırsat:
→ Soğutma kondenser atık ısısı (85°C) → CIP sıcak su ön ısıtma
→ Tasarruf: ~80 TEP/yıl ek potansiyel
→ Bu fırsat yalnızca exergy analiziyle tespit edilmiştir
```

## 9. İlgili Dosyalar

- [Enerji Yönetimi INDEX](INDEX.md) — Bilgi tabanı navigasyonu
- [ISO 50001 Genel Bakış](iso_50001_overview.md) — Standart gereksinimleri
- [Baseline ve EnPI](baseline_enpi.md) — EnB ve EnPI oluşturma süreci
- [EnPI Rehberi](enpi_guide.md) — EnPI türleri ve exergy-bazlı EnPI
- [Eylem Planlama](action_planning.md) — Fırsat önceliklendirme ve planlama
- [CUSUM Analizi](cusum_analysis.md) — Performans trend analizi
- [Denetim Metodolojisi](audit_methodology.md) — Saha denetim süreci
- [Enerji Yönetimi (genel)](../energy_management.md) — SEU ve operasyonel kontroller

## 10. Referanslar

- ISO 50001:2018, Clause 6.3 "Energy review"
- ISO 50006:2014, "Measuring energy performance using EnB and EnPI"
- ISO 50015:2014, "Measurement and verification of energy performance"
- US DOE, "Energy Review Guidance"
- UNIDO, "Practical Guide for Implementing an Energy Management System", Chapter 4
- Morvay, Z. & Gvozdenac, D., "Applied Industrial Energy and Environmental Management"
- Tsatsaronis, G. & Morosuk, T., "Advanced exergy-based methods for industrial energy assessment"
- BREF (Best Available Techniques Reference Documents), "Food, Drink and Milk Industries"
