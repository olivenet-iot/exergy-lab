---
title: "Çözüm: Throttle Valf Eliminasyonu — Throttle Valve Elimination"
category: solutions
equipment_type: pump
keywords: [kısma valfi, vana, pompa, kayıp]
related_files: [pump/solutions/vsd.md, pump/solutions/control_optimization.md, pump/benchmarks.md]
use_when: ["Kısma valfi eliminasyonu önerilirken", "Vana kayıpları analiz edilirken"]
priority: medium
last_updated: 2026-01-31
---
# Çözüm: Throttle Valf Eliminasyonu — Throttle Valve Elimination

> Son güncelleme: 2026-01-31

## Özet

**Problem:** Sabit hızlı santrifüj pompalarda kısma vanası (throttle valve) ile debi kontrolü büyük exergy yıkımı yaratır. Pompa gereksiz yere yüksek head üretir ve vana bu fazla enerjiyi ısıya dönüştürür. Tipik endüstriyel tesislerde kısma vanaları toplam pompalama gücünün %15-40'ını israf eder.

**Çözüm:** Throttle vanasını VSD (Variable Speed Drive), impeller trim veya doğru boyutlandırılmış pompa ile değiştirerek exergy yıkımını ortadan kaldırmak.

**Tipik Tasarruf:** %20-50
**Tipik ROI:** 0.5-3 yıl

## Çalışma Prensibi — Throttling'in Enerji Etkisi

Kısma vanası, pompa çıkışındaki basıncı düşürerek sistem direncini artırır ve debiyi azaltır. Ancak pompa hala aynı head'i üretir:

```
P_pompa = (Q × H × ρ × g) / η_pompa          [pompa tüketimi]
P_faydalı = (Q × H_sistem × ρ × g) / η_pompa  [gerçek ihtiyaç]
P_israf = (Q × ΔH_vana × ρ × g) / η_pompa     [vana kaybı]
```

Burada:
- `H` = pompa toplam head (sabit hızda sabit eğri üzerinde)
- `H_sistem` = gerçek sistem head ihtiyacı
- `ΔH_vana` = vana üzerindeki basınç düşüşü = `H - H_sistem`

### Exergy Yıkımı

Throttle vanasındaki exergy yıkımı:

```
Ex_yıkım_throttle = Q × ΔP_vana [W]
                   = Q × (ρ × g × ΔH_vana) [W]
```

Bu enerji tamamen ısıya dönüşür ve geri kazanılamaz.

## Kısmi Debi'de Güç Karşılaştırması

%50 nominal debi gerektiğinde farklı kontrol yöntemlerinin güç tüketimi:

| Kontrol Yöntemi | Güç Tüketimi (% nominal) | Açıklama |
|-----------------|--------------------------|----------|
| Throttle vana | %70-85 | Pompa tam hızda, vana fazla head'i ısıya çevirir |
| Bypass | %100 | Pompa tam kapasitede çalışır, fazla debi geri döner |
| VSD | %15-25 | Hız düşer, kübik yasa ile güç dramatik azalır |
| İmpeller trim | %50-65 | Kalıcı kapasite azaltma, tek çalışma noktası |
| Doğru boyut pompa | %50-60 | En verimli, BEP'te çalışma |

**Kritik örnek:** 50 kW pompa, %50 debi gereksinimi:
- Throttle ile: ~37.5 kW (75%) → 18.75 kW israf
- VSD ile: ~7.5 kW (15%) → 30 kW tasarruf
- **Fark: 30 kW sürekli tasarruf**

## Throttle Alternatifi Karşılaştırma Tablosu

| Alternatif | Tipik Tasarruf | Yatırım | Esneklik | En Uygun Durum |
|-----------|---------------|---------|----------|----------------|
| VSD (Değişken Hızlı Sürücü) | %30-50 | €3,000-30,000 | Çok yüksek (sürekli ayar) | Değişken talep, düşük statik head |
| İmpeller Trim | %15-25 | €500-2,000 | Düşük (sabit kapasite) | Sabit aşırı boyutlama, tek çalışma noktası |
| Yeni (doğru boyutlu) pompa | %20-40 | €2,000-50,000 | Orta | Ciddi aşırı boyutlama (>%30), pompa yaşlı |
| Paralel pompa | %10-25 | €5,000-40,000 | Yüksek | Geniş debi aralığı, yedeklilik ihtiyacı |
| Bypass eliminasyonu | %10-30 | €500-5,000 | Düşük | Bypass hattı sürekli açık olan sistemler |
| Kontrol valfi (modulating) | %5-15 | €1,000-5,000 | Orta | Çok küçük sistemler, hassas kontrol |

## Karar Ağacı — Hangi Alternatif Ne Zaman?

```
Debi ihtiyacı değişken mi?
├── Evet → Değişkenlik aralığı geniş mi (>%30)?
│   ├── Evet → VSD öner
│   │   └── Statik head oranı yüksek mi (>%60)?
│   │       ├── Evet → VSD tasarrufu sınırlı; dikkatli ROI analizi yap
│   │       └── Hayır → VSD en iyi çözüm
│   └── Hayır → Küçük VSD veya kontrol valfi yeterli
└── Hayır → Debi sabit ama pompa aşırı boyutlu mu?
    ├── Evet → İmpeller trim veya yeni pompa
    │   └── Aşırı boyutlama >%25 mi?
    │       ├── Evet → Yeni pompa (impeller trim verimi düşürür)
    │       └── Hayır → İmpeller trim (düşük maliyet, hızlı ROI)
    └── Hayır → Throttle gerekli değil, sistem tasarımını gözden geçir
```

## İmpeller Trim Detayları

İmpeller trim, impeller dış çapının torna tezgahında küçültülmesidir:

### Affinity Laws ile Trim Hesabı
```
Q2/Q1 = D2/D1
H2/H1 = (D2/D1)²
P2/P1 = (D2/D1)³
```

### Trim Limitleri (Hydraulic Institute)
- Maksimum trim: Orijinal çapın %75'ine kadar (üretici tavsiyesine göre)
- %5'e kadar trim: Affinity laws doğrudan uygulanabilir
- >%5 trim: Üretici eğrilerine başvur, verim düşüşü artar
- Spesifik hız etkisi: Düşük Ns pompalarda trim daha etkili

### Trim Sonrası Verim
| Trim Oranı | Tipik Verim Değişimi | Not |
|------------|---------------------|-----|
| %5 | -%0.5-1 | Minimal etki |
| %10 | -%1-3 | Kabul edilebilir |
| %15 | -%3-5 | Dikkatle değerlendir |
| %20 | -%5-8 | Sınıra yakın |
| >%25 | -%8-15 | Genelde önerilmez; yeni pompa düşün |

## Uygulanabilirlik Kriterleri

### Throttle Eliminasyonu Ne Zaman Uygulanmalı
- Kısma vanası sürekli veya çoğunlukla kısık konumda ise
- Vana üzerinden >2 bar basınç düşüşü varsa
- Pompa gücü >5 kW ve çalışma >4,000 saat/yıl
- Pompa BEP'in >%20 solunda veya sağında çalışıyorsa

### Throttle Eliminasyonu Ne Zaman Uygulanmamalı
- Proses çok hassas basınç/debi kontrolü gerektiriyorsa (bazı kimya prosesleri)
- Pompa zaten BEP yakınında ve vana minimal kısıksa (<10%)
- Sistem çok kısa süreli çalışıyorsa (<1,000 saat/yıl)
- Yatırım bütçesi çok kısıtlıysa ve mevcut sistem yeterli ise

## Yatırım Maliyeti

| Çözüm | Pompa Gücü Aralığı | Tahmini Yatırım |
|-------|-------------------|----------------|
| İmpeller trim | 5-200 kW | €500-2,000 |
| VSD retrofit | 5-15 kW | €2,000-5,000 |
| VSD retrofit | 15-55 kW | €5,000-15,000 |
| VSD retrofit | 55-160 kW | €15,000-35,000 |
| Yeni doğru boyut pompa | 5-15 kW | €3,000-8,000 |
| Yeni doğru boyut pompa | 15-55 kW | €8,000-25,000 |
| Yeni doğru boyut pompa | 55-160 kW | €25,000-80,000 |

## ROI Hesabı

### Formül
```
ΔP_vana = Pompa_head - Sistem_head_ihtiyacı [bar veya m]
P_israf = (Q × ΔP_vana) / (36 × η_pompa)     [kW] (Q: m³/h, ΔP: bar)
Tasarruf_kWh = P_israf × Çalışma_saati
Tasarruf_EUR = Tasarruf_kWh × Elektrik_fiyatı
Geri_ödeme_yıl = Yatırım / Tasarruf_EUR
```

### Örnek Hesap — Throttle → VSD Dönüşümü
- 37 kW pompa, 100 m³/h nominal, 6,500 saat/yıl
- Pompa head: 45 m, gerçek ihtiyaç: 30 m (ortalama)
- Kısma vanasında ΔP: 15 m (1.5 bar)
- Pompa verimi: %72
- Elektrik: €0.15/kWh

```
P_israf = (100 × 1.5) / (36 × 0.72) = 5.79 kW (sadece vana kaybı)
VSD ile ek tasarruf (Affinity Laws): ~8 kW (hız düşüşü etkisi)
Toplam tasarruf ≈ 12 kW ortalama

Tasarruf_kWh = 12 × 6,500 = 78,000 kWh/yıl
Tasarruf_EUR = 78,000 × 0.15 = €11,700/yıl

VSD yatırımı = €10,000
Geri_ödeme = 10,000 / 11,700 = 0.85 yıl ≈ 10 ay
```

## Uygulama Adımları

1. **Sistem analizi:** Mevcut çalışma noktasını ölç (Q, H, P) ve throttle vana durumunu kaydet
2. **Debi profili:** En az 1 haftalık debi/basınç profili oluştur
3. **Vana basınç düşüşü:** Vana öncesi ve sonrası basıncı ölç → israf edilen enerjiyi hesapla
4. **Alternatif seçimi:** Karar ağacına göre en uygun çözümü belirle
5. **ROI hesabı:** Her alternatif için detaylı mali analiz yap
6. **Tasarım ve tedarik:** Seçilen çözümü (VSD, trim, yeni pompa) tasarla ve temin et
7. **Kurulum:** Mekanik ve elektrik montajı, kontrol sistemi entegrasyonu
8. **Devreye alma:** Yeni sistem ile çalışma noktası doğrulaması
9. **Performans doğrulama:** 1-4 haftalık ölçüm ile gerçek tasarrufu belgele

## Riskler ve Dikkat Edilecekler

| Risk | Açıklama | Önlem |
|------|----------|-------|
| Yetersiz debi | Trim veya VSD ile düşük hızda yeterli basınç sağlanamayabilir | Minimum hız/trim limiti belirle |
| Minimum akış | Düşük debide pompa minimum akışın altına düşebilir | Minimum akış koruma vanası |
| Kavitasyon | VSD ile düşük hızda NPSH koşulları değişir | NPSHa hesabını tekrarla |
| Rezonans | VSD ile belirli hızlarda mekanik rezonans | Kritik hız bölgelerini atla (skip freq) |
| Proses kontrolü | Vana kaldırılınca proses kontrolü bozulabilir | Otomasyon sistemi ile PID kontrol |
| Aşırı boyut hatası | Yeni pompa da aşırı boyutlu seçilebilir | Doğru sistem eğrisi hesabı yap |

## İlgili Dosyalar
- Pompa VSD çözümü: `solutions/pump_vsd.md`
- Pompa kontrol optimizasyonu: `solutions/pump_control_optimization.md`
- Pompa kavitasyon önleme: `solutions/pump_cavitation_prevention.md`
- Pompa exergy formülleri: `formulas/pump_exergy.md`

## Referanslar
- DOE/AMO, "Improving Pumping System Performance: A Sourcebook for Industry"
- Hydraulic Institute & Europump, "Variable Speed Pumping: A Guide to Successful Applications"
- Hydraulic Institute & Europump, "Pump Life Cycle Costs: LCC Analysis for Pumping Systems"
- DOE Energy Tips — Pumping Systems, "Trim or Replace Impellers on Oversized Pumps"
- Pumps.org (Hydraulic Institute), "Trimming Impellers to Reduce Energy Consumption" (2022)
- ABB, "Energy efficiency assessment: Improving pump system efficiency"
- Europump, "Guide to the Energy Efficiency of Pumping Systems" (ISO 14414)
