---
title: "Entropi Üretim Minimizasyonu — Navigasyon Haritası (Entropy Generation Minimization — INDEX)"
category: factory
keywords: [EGM, entropi üretimi, Bejan, navigasyon, index, bilgi tabanı]
related_files: [factory/entropy_generation/overview.md, factory/entropy_generation/fundamentals.md, factory/exergy_fundamentals.md]
priority: high
last_updated: 2026-02-01
---
# Entropi Üretim Minimizasyonu (EGM) — Bilgi Tabanı İndeksi

> Son güncelleme: 2026-02-01

## Genel Bakış

Bu dizin, Adrian Bejan'ın Entropy Generation Minimization (EGM) metodolojisine dayalı termodinamik optimizasyon bilgi tabanını içerir. Exergy analizi **mevcut durumu** değerlendirirken, EGM **optimum tasarımı** belirler.

**Toplam:** 19 dosya (15 ana dosya + 3 çözümlü örnek + 1 INDEX)

## Dizin Yapısı

```
knowledge/factory/entropy_generation/
├── INDEX.md                        ← Bu dosya (navigasyon haritası)
│
├── ── Temel Teori (Core Theory) ──────────────────────────────
├── overview.md                     — EGM genel bakış ve felsefesi [Öncelik: Yüksek]
├── fundamentals.md                 — Termodinamik temeller, Gouy-Stodola [Öncelik: Yüksek]
├── bejan_number.md                 — Bejan sayısı ve entropi üretim sayısı [Öncelik: Yüksek]
├── heat_transfer_egm.md            — Isı transferinde EGM [Öncelik: Yüksek]
├── fluid_flow_egm.md               — Akış sistemlerinde EGM [Öncelik: Yüksek]
├── finite_time_thermo.md           — Sonlu zamanlı termodinamik (Curzon-Ahlborn) [Öncelik: Orta]
│
├── ── Ekipman Uygulamaları (Equipment Applications) ──────────
├── heat_exchanger_egm.md           — Eşanjör optimizasyonu [Öncelik: Yüksek]
├── pipe_flow_egm.md                — Boru akışı optimizasyonu [Öncelik: Orta]
├── power_cycles_egm.md             — Güç çevrimlerinde EGM [Öncelik: Orta]
├── refrigeration_egm.md            — Soğutma çevrimlerinde EGM [Öncelik: Orta]
├── heat_storage_egm.md             — Isı depolama optimizasyonu [Öncelik: Orta]
│
├── ── İleri Teori ve Rehberler (Advanced Theory) ─────────────
├── constructal_theory.md           — Constructal yasa ve uygulamaları [Öncelik: Orta]
├── industrial_applications.md      — Endüstriyel uygulama rehberi [Öncelik: Orta]
├── egm_vs_exergoeconomic.md        — EGM vs exergoekonomik karşılaştırma [Öncelik: Orta]
├── case_studies.md                 — Endüstriyel vaka çalışmaları [Öncelik: Düşük]
│
└── worked_examples/                ← Çözümlü Örnekler
    ├── heat_exchanger_opt.md       — Eşanjör EGM optimizasyonu örneği [Öncelik: Yüksek]
    ├── pipe_sizing.md              — Boru çapı optimizasyonu örneği [Öncelik: Yüksek]
    └── cooling_system.md           — Soğutma sistemi EGM analizi örneği [Öncelik: Yüksek]
```

## Navigasyon Kuralları

### Ne Zaman Hangi Dosyayı Oku?

#### Senaryo 1: EGM Kavramı Tanıtılacaksa
1. `overview.md` — Genel bakış ve felsefe [Zorunlu]
2. `fundamentals.md` — Gouy-Stodola ve temel kavramlar [Zorunlu]
3. `bejan_number.md` — Bejan sayısı yorumlama [Önerilen]

#### Senaryo 2: Ekipman Bazlı EGM Analizi
1. `fundamentals.md` — S_gen hesaplama temeli [Zorunlu]
2. `bejan_number.md` — Bejan sayısı ile kaynak belirleme [Zorunlu]
3. İlgili ekipman dosyası:
   - Eşanjör → `heat_exchanger_egm.md`
   - Boru sistemi → `pipe_flow_egm.md`
   - Güç çevrimi / kazan / türbin → `power_cycles_egm.md`
   - Chiller / soğutma → `refrigeration_egm.md`
   - Isı depolama → `heat_storage_egm.md`
4. İlgili çözümlü örnek (varsa)

#### Senaryo 3: Isı Transferi / Akış İrreversiblliği Detayı
1. `heat_transfer_egm.md` — Isı transferi kaynaklı S_gen [İlgili ise]
2. `fluid_flow_egm.md` — Akış kaynaklı S_gen [İlgili ise]
3. İlgili ekipman dosyası

#### Senaryo 4: Termodinamik Optimizasyon Karşılaştırması
1. `overview.md` — EGM pozisyonu [Zorunlu]
2. `egm_vs_exergoeconomic.md` — Yöntem karşılaştırması [Zorunlu]
3. `finite_time_thermo.md` — Verim sınırları [Önerilen]

#### Senaryo 5: Fabrika / Sistem Düzeyinde EGM
1. `industrial_applications.md` — Uygulama rehberi ve checklist [Zorunlu]
2. `case_studies.md` — Gerçek dünya örnekleri [Önerilen]
3. `constructal_theory.md` — Ağ tasarımı perspektifi [İlgili ise]

#### Senaryo 6: Çözümlü Örnek Gerektiğinde
- Eşanjör hesabı → `worked_examples/heat_exchanger_opt.md`
- Boru boyutlandırma → `worked_examples/pipe_sizing.md`
- Soğutma sistemi → `worked_examples/cooling_system.md`

## Bağımlılık Haritası

```
fundamentals.md ──────────┐
    │                     │
    ├── bejan_number.md   │
    │       │             │
    │       ├── heat_transfer_egm.md ──── heat_exchanger_egm.md
    │       │                                    │
    │       ├── fluid_flow_egm.md ─────── pipe_flow_egm.md
    │       │                                    │
    │       └── finite_time_thermo.md ─── power_cycles_egm.md
    │                                            │
    ├── refrigeration_egm.md ◄───────────────────┘
    │
    ├── heat_storage_egm.md
    │
    ├── constructal_theory.md
    │
    └── industrial_applications.md
            │
            ├── egm_vs_exergoeconomic.md
            └── case_studies.md

overview.md ← Bağımsız giriş noktası (tüm dosyalara referans verir)
```

## Mevcut Knowledge Base ile Çapraz Referanslar

| EGM Dosyası | İlişkili Mevcut Dosyalar |
|-------------|--------------------------|
| `heat_exchanger_egm.md` | `factory/heat_integration.md`, `factory/pinch_analysis.md` |
| `pipe_flow_egm.md` | `pump/formulas.md`, `pump/solutions/system_optimization.md` |
| `power_cycles_egm.md` | `factory/cogeneration.md`, `boiler/formulas.md` |
| `refrigeration_egm.md` | `chiller/formulas.md`, `chiller/equipment/*.md` |
| `heat_storage_egm.md` | `chiller/solutions/thermal_storage.md` |
| `egm_vs_exergoeconomic.md` | `factory/economic_analysis.md`, `factory/life_cycle_cost.md` |
| `industrial_applications.md` | `factory/implementation.md`, `factory/sector_*.md` |
| `constructal_theory.md` | `factory/process_integration.md` |
| `fundamentals.md` | `factory/exergy_fundamentals.md` |

## Öncelik Sırası

1. **Yüksek** — Her EGM analizinde okunması gereken temel dosyalar
   - `fundamentals.md`, `bejan_number.md`, `overview.md`
   - `heat_transfer_egm.md`, `fluid_flow_egm.md`
   - `heat_exchanger_egm.md`

2. **Orta** — İlgili ekipman/konu için okunması gereken dosyalar
   - Ekipman uygulamaları (`pipe_flow_egm.md`, `power_cycles_egm.md`, `refrigeration_egm.md`, `heat_storage_egm.md`)
   - İleri teori (`constructal_theory.md`, `finite_time_thermo.md`)
   - Rehberler (`industrial_applications.md`, `egm_vs_exergoeconomic.md`)

3. **Düşük** — Referans ve destekleyici dosyalar
   - `case_studies.md`

## Anahtar Kavram Sözlüğü

| Kavram | Simge | Birim | Tanım |
|--------|-------|-------|-------|
| Entropi üretimi | S_gen | kW/K | Tersinmezlik ölçüsü |
| Exergy yıkımı | I | kW | Kaybedilen iş potansiyeli |
| Bejan sayısı | Be | — | Isı transferi / toplam irreversibility |
| Entropi üretim sayısı | N_s | — | Boyutsuz S_gen |
| Gouy-Stodola | I = T₀ × S_gen | — | Temel bağlantı denklemi |
| Curzon-Ahlborn verimi | η_CA | — | Sonlu zamanlı optimum verim |
| Referans sıcaklık | T₀ | K | Çevre sıcaklığı (genellikle 298 K) |
