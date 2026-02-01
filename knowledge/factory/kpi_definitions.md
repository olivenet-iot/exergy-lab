# Enerji Performans Göstergeleri Tanımları (Energy KPI Definitions)

> Son güncelleme: 2026-01-31

## Genel Bakış

Fabrika enerji yönetiminde doğru performans göstergelerinin (KPI — Key Performance Indicator) tanımlanması, izlenmesi ve karşılaştırılması kritik öneme sahiptir. Bu dosya, ISO 50001 uyumlu enerji performans göstergelerini (EnPI), exergy verimlilik ölçütlerini ve sektörel benchmark karşılaştırma metriklerini tanımlar.

## 1. Spesifik Enerji Tüketimi — SEC (Specific Energy Consumption)

### 1.1 Tanım

```
SEC = Toplam Enerji Tüketimi / Üretim Miktarı [kWh/ton veya MJ/ton]

Burada:
- Toplam Enerji Tüketimi: Tüm enerji kaynakları birincil enerji eşdeğerine dönüştürülür
- Üretim Miktarı: Ana ürün üretim miktarı (ton, m², adet, litre vb.)
```

### 1.2 SEC Hesaplama Örnekleri

```
Örnek 1 — Tekstil fabrikası:
Elektrik: 2,400,000 kWh/yıl
Doğalgaz: 800,000 Nm³/yıl × 10.33 kWh/Nm³ = 8,264,000 kWh/yıl
Toplam: 10,664,000 kWh/yıl
Üretim: 3,200 ton kumaş/yıl
SEC = 10,664,000 / 3,200 = 3,333 kWh/ton kumaş

Örnek 2 — Çimento fabrikası:
Elektrik: 45,000,000 kWh/yıl (110 kWh/ton)
Termal: 1,435,000 GJ/yıl = 398,611,111 kWh/yıl (975 kWh/ton)
Üretim: 410,000 ton çimento/yıl
SEC_elektrik = 110 kWh/ton
SEC_termal = 975 kWh/ton (3,500 MJ/ton)
SEC_toplam = 1,085 kWh/ton
```

### 1.3 SEC Performans Sınıflandırması

| Performans | SEC Konumu | Aksiyon |
|---|---|---|
| Mükemmel | < Sektör en iyi uygulama | Mevcut durumu koru, yayılım sağla |
| İyi | En iyi uygulama — sektör ortalaması arası | İnce ayar optimizasyonu |
| Ortalama | Sektör ortalaması ±%10 | Sistematik enerji yönetimi gerekli |
| Düşük | > Sektör ortalaması + %10 | Ciddi iyileştirme programı gerekli |
| Kritik | > Sektör ortalaması + %30 | Acil müdahale, kapsamlı audit |

## 2. Enerji Kullanım Yoğunluğu — EUI (Energy Use Intensity)

### 2.1 Tanım

```
EUI = Toplam Enerji Tüketimi / Bina/Tesis Alanı [kWh/m²·yıl]

Burada:
- Toplam Enerji: Birincil veya son kullanım enerjisi
- Alan: Brüt tesis alanı (üretim + ofis + depo) [m²]
```

### 2.2 EUI Benchmark Değerleri (Endüstriyel Tesisler)

| Tesis Tipi | Düşük [kWh/m²] | Ortalama [kWh/m²] | Yüksek [kWh/m²] | Not |
|---|---|---|---|---|
| Hafif üretim | 150-250 | 250-400 | >400 | Montaj, paketleme |
| Orta üretim | 300-500 | 500-800 | >800 | Tekstil, gıda |
| Ağır üretim | 500-1,000 | 1,000-2,000 | >2,000 | Metal, kimya |
| Depo/lojistik | 50-100 | 100-200 | >200 | Soğuk depo hariç |
| Soğuk depo | 200-400 | 400-700 | >700 | Soğutma yoğun |

### 2.3 Normalize EUI

```
EUI_normalize = EUI_gerçek × CF_hava × CF_üretim × CF_alan

Burada:
- CF_hava = Hava koşulları düzeltme faktörü (HDD/CDD bazlı)
- CF_üretim = Üretim yoğunluğu düzeltmesi
- CF_alan = Alan kullanım oranı düzeltmesi
```

## 3. Exergy Verimlilik Göstergeleri (Exergy Efficiency Indicators)

### 3.1 Fabrika Exergy Verimi

```
η_ex = Ex_ürün / Ex_giriş × 100 [%]

Burada:
- Ex_ürün = Σ(ürün exergy akışları) [kW]
- Ex_giriş = Σ(tüm exergy giriş akışları) [kW]
```

### 3.2 Exergy Yıkım Oranı

```
y_d = İ_k / Ex_giriş × 100 [%]

Burada:
- İ_k = k-inci bileşendeki exergy yıkımı [kW]
- Ex_giriş = Toplam exergy girişi [kW]

Tüm bileşenler için: Σ y_d,k = 100% - η_ex - y_atık
```

### 3.3 İyileştirilebilir Exergy Yıkımı Göstergesi

```
y_d,iyileştirilebilir = (İ_gerçek - İ_kaçınılamaz) / Ex_giriş × 100 [%]

Bu gösterge, mühendislik müdahalesiyle azaltılabilecek exergy
yıkımının toplam giriş exergisine oranıdır.
```

### 3.4 Sektörel Exergy Verimi Benchmark Tablosu

| Sektör | Kritik [%] | Düşük [%] | Ortalama [%] | İyi [%] | Mükemmel [%] |
|---|---|---|---|---|---|
| Çimento | <20 | 20-28 | 28-35 | 35-40 | >40 |
| Kimya | <25 | 25-35 | 35-45 | 45-55 | >55 |
| Gıda ve içecek | <12 | 12-18 | 18-25 | 25-32 | >32 |
| Tekstil | <15 | 15-22 | 22-30 | 30-38 | >38 |
| Metal işleme | <20 | 20-30 | 30-38 | 38-45 | >45 |
| Kağıt ve selüloz | <25 | 25-33 | 33-42 | 42-50 | >50 |
| Otomotiv | <15 | 15-22 | 22-30 | 30-36 | >36 |

## 4. ISO 50001 Enerji Performans Göstergeleri — EnPI (Energy Performance Indicators)

### 4.1 EnPI Türleri

| EnPI Türü | Formül | Kullanım |
|---|---|---|
| Mutlak tüketim | E [kWh/yıl] | Genel izleme, raporlama |
| Spesifik tüketim (SEC) | E / P [kWh/ton] | Üretim hacmi normalize |
| Yoğunluk (EUI) | E / A [kWh/m²] | Bina/tesis karşılaştırma |
| Oran | E_alt / E_toplam [%] | Alt sistem payı izleme |
| Regresyon bazlı | E = a × P + b × HDD + c | Çok değişkenli normalize |
| CUSUM | Σ(E_gerçek - E_baz) | Kümülatif tasarruf izleme |

### 4.2 Regresyon Bazlı EnPI

```
E_beklenen = β₀ + β₁ × P + β₂ × HDD + β₃ × CDD + ε

Burada:
- E_beklenen = beklenen enerji tüketimi [kWh]
- P = üretim miktarı [ton]
- HDD = ısıtma derece-gün
- CDD = soğutma derece-gün
- β₀, β₁, β₂, β₃ = regresyon katsayıları
- ε = hata terimi

R² ≥ 0.75 kabul edilebilir, R² ≥ 0.90 iyi
```

### 4.3 CUSUM (Cumulative Sum) Analizi

```
CUSUM_n = Σᵢ₌₁ⁿ (E_gerçek,i - E_baz,i)

Burada:
- E_gerçek,i = i-inci dönem gerçek tüketim
- E_baz,i = i-inci dönem baz çizgisi (regresyon modeli) tahmini

Yorumlama:
- CUSUM azalıyor → Tasarruf yapılıyor (enerji performansı iyileşiyor)
- CUSUM artıyor → Aşırı tüketim (performans kötüleşiyor)
- CUSUM sabit → Baz çizgisine yakın performans
```

### 4.4 CUSUM Hesaplama Örneği

```
Tekstil fabrikası aylık veri:

| Ay     | Üretim [ton] | E_gerçek [kWh] | E_baz [kWh]  | Fark     | CUSUM     |
|--------|-------------|----------------|-------------|----------|-----------|
| Ocak   | 250         | 830,000        | 870,000     | -40,000  | -40,000   |
| Şubat  | 280         | 910,000        | 960,000     | -50,000  | -90,000   |
| Mart   | 300         | 1,020,000      | 1,020,000   | 0        | -90,000   |
| Nisan  | 310         | 1,000,000      | 1,050,000   | -50,000  | -140,000  |
| Mayıs  | 290         | 960,000        | 980,000     | -20,000  | -160,000  |
| Haziran| 270         | 920,000        | 930,000     | -10,000  | -170,000  |

Azalan CUSUM trendi → %5-6 civarında tasarruf sağlanıyor
```

## 5. Alt Sistem KPI'ları

### 5.1 Buhar Sistemi KPI'ları

| KPI | Formül | İyi | Ortalama | Kötü |
|---|---|---|---|---|
| Kazan verimi (enerji) | Q̇_buhar / Q̇_yakıt | >%90 | %82-90 | <%82 |
| Kazan verimi (exergy) | Ėx_buhar / Ėx_yakıt | >%40 | %28-40 | <%28 |
| Kondensat geri dönüş | ṁ_kond / ṁ_buhar | >%80 | %50-80 | <%50 |
| Buhar kapanı arıza oranı | N_arızalı / N_toplam | <%5 | %5-15 | >%15 |
| Spesifik yakıt tüketimi | m³_gaz / ton_buhar | <78 | 78-90 | >90 |

### 5.2 Basınçlı Hava Sistemi KPI'ları

| KPI | Formül | İyi | Ortalama | Kötü |
|---|---|---|---|---|
| Spesifik güç (SPC) | kW / (m³/min) @7bar | <5.5 | 5.5-7.5 | >7.5 |
| Kaçak oranı | V̇_kaçak / V̇_toplam | <%15 | %15-30 | >%30 |
| Sistem exergy verimi | Ėx_hava / Ẇ_elekt | >%18 | %10-18 | <%10 |
| Basınç kararlılığı | P_max - P_min [bar] | <0.5 | 0.5-1.5 | >1.5 |

### 5.3 Soğutma Sistemi KPI'ları

| KPI | Formül | İyi | Ortalama | Kötü |
|---|---|---|---|---|
| COP (Coefficient of Performance) | Q̇_soğutma / Ẇ_elekt | >5.5 | 3.5-5.5 | <3.5 |
| kW/TR (ton soğutma başına) | Ẇ_elekt / TR | <0.65 | 0.65-1.0 | >1.0 |
| Exergy COP | Ėx_soğutma / Ẇ_elekt | >%30 | %15-30 | <%15 |
| Yaklaşım sıcaklığı | T_evap - T_chw_çıkış | <2°C | 2-5°C | >5°C |

### 5.4 Pompa Sistemi KPI'ları

| KPI | Formül | İyi | Ortalama | Kötü |
|---|---|---|---|---|
| Pompa verimi | η_pompa = Q×ΔP / Ẇ_şaft | >%75 | %55-75 | <%55 |
| Sistem verimi | η_sistem = Q×ΔP_kullanım / Ẇ_elekt | >%50 | %30-50 | <%30 |
| Spesifik enerji | kWh/m³ pompalanan | Sisteme özgü | — | — |

## 6. Karbon Yoğunluğu Göstergeleri (Carbon Intensity Indicators)

### 6.1 Tanımlar

```
CI_üretim = CO₂_emisyonu / Üretim_miktarı [kgCO₂/ton ürün]

CI_enerji = CO₂_emisyonu / Enerji_tüketimi [kgCO₂/kWh]

CO₂ emisyon faktörleri (Türkiye):
- Doğalgaz: 0.202 kgCO₂/kWh (56.1 tCO₂/TJ)
- Elektrik şebekesi: ~0.47 kgCO₂/kWh (Türkiye 2024 ortalaması)
- Kömür (linyit): ~0.35 kgCO₂/kWh
- Fuel oil: 0.267 kgCO₂/kWh
```

### 6.2 Sektörel Karbon Yoğunluğu

| Sektör | Düşük [kgCO₂/ton] | Ortalama [kgCO₂/ton] | Yüksek [kgCO₂/ton] |
|---|---|---|---|
| Çimento (klinker) | 600 | 800 | 1,000 |
| Çelik (EAF) | 200 | 400 | 600 |
| Kağıt | 300 | 600 | 900 |
| Tekstil | 1,500 | 3,000 | 5,000 |
| Gıda (süt) | 50 | 100 | 180 |

## 7. EnPI Seçim Kriterleri

### 7.1 İyi Bir EnPI'ın Özellikleri

```
1. Ölçülebilir: Güvenilir veri ile hesaplanabilir
2. İlgili: İzlenen enerji kullanımıyla doğrudan ilişkili
3. Tekrarlanabilir: Farklı dönemlerde tutarlı sonuç
4. Karşılaştırılabilir: Sektörel benchmark ile kıyaslanabilir
5. Anlaşılır: Yönetim ve operasyon ekibi tarafından anlaşılabilir
6. Eyleme yönelten: Kötü değer gördüğünde ne yapılacağı belli
7. Normalize: Üretim hacmi, hava koşulları gibi değişkenlerden arınmış
```

### 7.2 EnPI Seçim Matrisi

| Kriter | SEC | EUI | η_ex | CUSUM | Regresyon |
|---|---|---|---|---|---|
| Hesaplama kolaylığı | Yüksek | Yüksek | Düşük | Orta | Düşük |
| Benchmark karşılaştırma | Yüksek | Orta | Yüksek | Düşük | Düşük |
| Normalize etme | Orta | Düşük | Yüksek | Yüksek | Yüksek |
| Trend izleme | Orta | Orta | Orta | Yüksek | Yüksek |
| Yönetim sunumu | Yüksek | Yüksek | Düşük | Orta | Düşük |

## 8. Hesaplama Örneği: Fabrika EnPI Paketi

### 8.1 Senaryo — Orta Ölçekli Gıda Fabrikası

```
Girdiler:
- Elektrik: 3,600,000 kWh/yıl (€ 0.12/kWh)
- Doğalgaz: 1,200,000 Nm³/yıl (€ 0.45/Nm³)
- Üretim: 18,000 ton/yıl
- Tesis alanı: 8,000 m²
- Çalışma: 6,000 saat/yıl
- Buhar: 4 ton/h, 7 bar doymuş
- Basınçlı hava: 10 m³/min, 7 bar
- Soğutma: 300 kW, 5°C chilled water

Hesaplamalar:

SEC = (3,600,000 + 1,200,000 × 10.33) / 18,000
    = (3,600,000 + 12,396,000) / 18,000
    = 888 kWh/ton ürün

EUI = 15,996,000 / 8,000 = 2,000 kWh/m²·yıl

η_ex (yaklaşık):
  Ex_giriş = 3,600 + (1,200,000/6,000 × 10.33 × 1.04/3.6) ≈ 3,600 + 596 = 4,196 kW
  Ex_ürün ≈ 1,100 kW (buhar + hava + soğutma exergisi)
  η_ex ≈ 1,100/4,196 ≈ %26.2

CI = (3,600,000 × 0.47 + 12,396,000 × 0.202) / 18,000
   = (1,692,000 + 2,503,992) / 18,000
   = 233 kgCO₂/ton ürün
```

## İlgili Dosyalar

- [Exergy Temelleri](exergy_fundamentals.md) — Exergy verimlilik tanımları
- [Fabrika Benchmarkları](factory_benchmarks.md) — Sektörel SEC ve exergy verimlilikleri
- [Performans Göstergeleri](performance_indicators.md) — Hedefler ve izleme yöntemleri
- [Enerji Yönetimi](energy_management.md) — ISO 50001 EnPI gereksinimleri
- [Ölçüm ve Doğrulama](measurement_verification.md) — IPMVP ile tasarruf doğrulama

## Referanslar

- ISO 50001:2018, "Energy management systems — Requirements with guidance for use"
- ISO 50006:2014, "Energy management systems — Measuring energy performance using energy baselines (EnB) and energy performance indicators (EnPI)"
- ISO 50015:2014, "Energy management systems — Measurement and verification of energy performance of organizations"
- ASHRAE, "Guideline 14-2014: Measurement of Energy, Demand and Water Savings"
- US DOE, "Superior Energy Performance (SEP) — Measurement and Verification Protocol"
- EU BREF, "Energy Efficiency," European Commission, 2009
- Tanaka, K. (2008), "Assessment of energy efficiency performance measures in industry," Energy Policy, 36(8), 2887-2902
