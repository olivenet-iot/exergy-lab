---
title: "Exergoekonomik Analiz — Navigasyon Haritası (Exergoeconomic Analysis — INDEX)"
category: factory
keywords: [exergoekonomik, termoekonomik, SPECO, navigasyon, index, bilgi tabanı]
related_files: [factory/exergoeconomic/overview.md, factory/exergoeconomic/speco_method.md, factory/exergoeconomic/evaluation_criteria.md]
priority: high
last_updated: 2026-02-01
---
# Exergoekonomik Analiz — Bilgi Tabanı İndeksi

> Son güncelleme: 2026-02-01

## Genel Bakış

Bu dizin, exergoekonomik analiz (termoekonomik analiz) bilgi tabanını içerir. Termodinamiğin ikinci yasasını ekonomik analizle birleştiren bu yöntem, her bileşendeki exergy yıkımının ekonomik maliyetini hesaplar ve mühendislik iyileştirme kararlarını yönlendirir.

**Toplam:** 21 dosya (14 ana dosya + 3 çözümlü örnek + 3 vaka/veritabanı + 1 INDEX)

## Dizin Yapısı

```
knowledge/factory/exergoeconomic/
├── INDEX.md                        ← Bu dosya (navigasyon haritası)
│
├── ── Temel Kavramlar (Foundations) ────────────────────────
├── overview.md                     — Genel bakış, tarihçe, uygulama alanları [Öncelik: Yüksek]
├── speco_method.md                 — SPECO metodolojisi (Lazzaretto & Tsatsaronis 2006) [Öncelik: Yüksek]
├── fuel_product_definitions.md     — 10 ekipman tipi için F/P tanımları [Öncelik: Yüksek]
│
├── ── Maliyet Hesaplamaları (Cost Calculations) ───────────
├── cost_equations.md               — PEC korelasyonları, düzeltme faktörleri [Öncelik: Yüksek]
├── cost_databases.md               — CEPCI değerleri, Türkiye ayarları [Öncelik: Orta]
├── levelized_cost.md               — CRF formülü, Ż hesabı, Türkiye WACC [Öncelik: Yüksek]
│
├── ── Çekirdek Yöntem (Core Method) ───────────────────────
├── exergoeconomic_balance.md       — Ċ_P = Ċ_F + Ż denklemi, bileşen bilançoları [Öncelik: Yüksek]
├── auxiliary_equations.md          — F-kuralı, P-kuralı, sınır koşulları [Öncelik: Orta]
├── matrix_formulation.md           — [A]{c}={Z} matris çözümü, Python kodu [Öncelik: Orta]
│
├── ── Değerlendirme ve Optimizasyon (Evaluation & Optimization) ──
├── evaluation_criteria.md          — Ċ_D, f_k, r_k tanım/eşik/karar [Öncelik: Yüksek]
├── advanced_exergoeconomic.md      — AV/UN, EN/EX, 4-yollu matris [Öncelik: Orta]
├── optimization.md                 — İteratif ve matematiksel optimizasyon [Öncelik: Orta]
├── sensitivity_analysis.md         — OAT, tornado, Monte Carlo, Sobol [Öncelik: Orta]
│
├── ── Referans ve Veri (Reference & Data) ─────────────────
├── case_studies.md                 — 6 akademik vaka çalışması [Öncelik: Düşük]
│
└── worked_examples/                ← Çözümlü Örnekler
    ├── simple_cycle.md             — Basit Rankine çevrimi (4 bileşen) [Öncelik: Orta]
    ├── cogeneration.md             — Gaz türbini CHP (7 bileşen, ileri analiz) [Öncelik: Orta]
    └── industrial_plant.md         — ExergyLab tesis analizi (5 bileşen) [Öncelik: Yüksek]
```

## Navigasyon Kuralları

### Ne Zaman Hangi Dosyayı Oku?

#### Senaryo 1: Exergoekonomik Kavram Tanıtılacaksa
1. `overview.md` — Genel bakış ve tarihçe [Zorunlu]
2. `speco_method.md` — SPECO adımları [Önerilen]
3. `fuel_product_definitions.md` — F/P temel kuralları [Önerilen]

#### Senaryo 2: Ekipman/Sistem Exergoekonomik Analizi
1. `speco_method.md` — Metodoloji [Zorunlu]
2. `fuel_product_definitions.md` — İlgili ekipman F/P tanımı [Zorunlu]
3. `cost_equations.md` — PEC tahmini [Zorunlu]
4. `levelized_cost.md` — CRF ve Ż hesabı [Zorunlu]
5. `exergoeconomic_balance.md` — Maliyet bilançosu [Zorunlu]
6. `auxiliary_equations.md` — F/P kuralları ile yardımcı denklemler [Zorunlu]
7. `matrix_formulation.md` — Çözüm yöntemi [Gerektiğinde]
8. `evaluation_criteria.md` — f_k, r_k yorumlama [Zorunlu]

#### Senaryo 3: Maliyet Sonuçları Yorumlanacaksa
1. `evaluation_criteria.md` — Ċ_D, f_k, r_k tanım ve eşikleri [Zorunlu]
2. `optimization.md` — İteratif iyileştirme stratejisi [Önerilen]
3. `case_studies.md` — Benzer sistem referans değerleri [Gerektiğinde]

#### Senaryo 4: İleri Exergoekonomik Analiz
1. `advanced_exergoeconomic.md` — AV/UN ve EN/EX teori [Zorunlu]
2. `evaluation_criteria.md` — Temel kriterlerin ileri versiyonları [Zorunlu]
3. `worked_examples/cogeneration.md` — İleri analiz uygulaması [Önerilen]

#### Senaryo 5: Karar Güvenilirliği ve Belirsizlik
1. `sensitivity_analysis.md` — OAT, Monte Carlo yöntemleri [Zorunlu]
2. `cost_databases.md` — Maliyet belirsizlik aralıkları [Önerilen]
3. `levelized_cost.md` — CRF parametre duyarlılığı [Önerilen]

#### Senaryo 6: Çözümlü Örnek Gerektiğinde
- Basit sistem (Rankine) → `worked_examples/simple_cycle.md`
- CHP / kojenerasyon → `worked_examples/cogeneration.md`
- ExergyLab ekipmanları → `worked_examples/industrial_plant.md`
- Akademik referans → `case_studies.md`

## Bağımlılık Haritası

```
overview.md ← Bağımsız giriş noktası
    │
    └── speco_method.md
            │
            ├── fuel_product_definitions.md
            │
            ├── cost_equations.md ──── cost_databases.md
            │         │
            │         └── levelized_cost.md
            │                   │
            │                   └── exergoeconomic_balance.md
            │                             │
            │                   auxiliary_equations.md
            │                             │
            │                   matrix_formulation.md
            │
            └── evaluation_criteria.md
                        │
                        ├── advanced_exergoeconomic.md
                        │
                        ├── optimization.md
                        │         │
                        │         └── sensitivity_analysis.md
                        │
                        └── case_studies.md

worked_examples/ ← evaluation_criteria.md bağımlı
    ├── simple_cycle.md       (speco + matrix + evaluation)
    ├── cogeneration.md       (speco + advanced + matrix)
    └── industrial_plant.md   (speco + evaluation + cross_equipment)
```

## Mevcut Knowledge Base ile Çapraz Referanslar

| Exergoekonomik Dosyası | İlişkili Mevcut Dosyalar |
|------------------------|--------------------------|
| `cost_equations.md` | `factory/economic_analysis.md`, `factory/life_cycle_cost.md` |
| `levelized_cost.md` | `factory/economic_analysis.md`, `factory/energy_pricing.md` |
| `evaluation_criteria.md` | `factory/prioritization.md`, `factory/cross_equipment.md` |
| `optimization.md` | `factory/implementation.md` |
| `sensitivity_analysis.md` | `factory/economic_analysis.md` |
| `worked_examples/industrial_plant.md` | `factory/cross_equipment.md`, `factory/prioritization.md` |
| `advanced_exergoeconomic.md` | `factory/entropy_generation/egm_vs_exergoeconomic.md` |
| `case_studies.md` | `factory/case_studies.md`, `factory/sector_*.md` |

## Öncelik Sırası

1. **Yüksek** — Her exergoekonomik analizde okunması gereken dosyalar
   - `overview.md`, `speco_method.md`, `fuel_product_definitions.md`
   - `cost_equations.md`, `levelized_cost.md`
   - `exergoeconomic_balance.md`, `evaluation_criteria.md`
   - `worked_examples/industrial_plant.md`

2. **Orta** — İlgili senaryo için okunması gereken dosyalar
   - `auxiliary_equations.md`, `matrix_formulation.md`
   - `advanced_exergoeconomic.md`, `optimization.md`, `sensitivity_analysis.md`
   - `cost_databases.md`
   - `worked_examples/simple_cycle.md`, `worked_examples/cogeneration.md`

3. **Düşük** — Referans ve destekleyici dosyalar
   - `case_studies.md`

## Anahtar Kavram Sözlüğü

| Kavram | Simge | Birim | Tanım |
|--------|-------|-------|-------|
| Exergy yıkım maliyet akışı | Ċ_D | €/saat | c_F × Ė_D |
| Exergoekonomik faktör | f_k | — | Ż / (Ż + Ċ_D) |
| Göreli maliyet farkı | r_k | — | (c_P - c_F) / c_F |
| Birim exergy maliyeti | c | €/kWh | Akış başına birim maliyet |
| Maliyet akışı | Ċ | €/saat | c × Ė |
| Yıllıklaştırılmış yatırım | Ż | €/saat | PEC × (CRF+φ) / τ |
| Sermaye geri kazanım faktörü | CRF | — | i(1+i)^n / [(1+i)^n - 1] |
| Ekipman satın alma maliyeti | PEC | € | Purchased Equipment Cost |
| Fuel exergy | Ė_F | kW | Bileşene giren exergy kaynağı |
| Product exergy | Ė_P | kW | Bileşenden çıkan faydalı exergy |
