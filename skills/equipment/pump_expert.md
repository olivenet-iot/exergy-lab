---
skill_id: pump_expert
version: 1.0
type: equipment
equipment_type: pump
triggers:
  - single_equipment_analysis
  - equipment_type == "pump"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
knowledge_files:
  - knowledge/pump/benchmarks.md
  - knowledge/pump/formulas.md
  - knowledge/pump/equipment/*.md
  - knowledge/pump/solutions/*.md
---

# Pompa Uzmanı

## Uzmanlık Alanı

Pompalama sistemleri exergy analizi:
- Santrifüj, pozitif deplasman pompalar
- VSD retrofit
- Throttle eliminasyonu
- Sistem optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Pompa verimi | P_hidrolik / P_mil | > 80% |
| Motor verimi | P_mil / P_elektrik | > 92% |
| Wire-to-water | P_hidrolik / P_elektrik | > 65% |
| Exergy verimi | ≈ Wire-to-water | > 60% |

## Özel Kurallar

### Wire-to-Water Değerlendirmesi
```
- > 70%: Mükemmel
- 60-70%: İyi
- 50-60%: Ortalama
- 40-50%: Düşük
- < 40%: Kritik (muhtemelen throttle veya aşırı boyut)
```

### VSD Tasarruf Potansiyeli
```
Affinity Laws:
- Debi ∝ Hız
- Head ∝ Hız²
- Güç ∝ Hız³

%50 debi için:
- Throttle: Güç ≈ %80-90 (vana kaybı)
- VSD: Güç ≈ %12.5-20 (kübik yasa)

Tasarruf potansiyeli: %30-70 (yük profiline bağlı)
```

### VSD Uygunluk Kriterleri
```
VSD öner eğer:
- Kontrol yöntemi = throttle VEYA bypass VE
- Motor gücü > 5 kW VE
- Değişken debi ihtiyacı var VE
- Statik head oranı < %60 (yoksa tasarruf düşük)
```

### Statik Head Uyarısı
```
Statik head / Toplam head oranı:
- < 30%: VSD çok etkili
- 30-60%: VSD etkili
- > 60%: VSD etkisi sınırlı, dikkatli değerlendir
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| VSD retrofit | %30-50 | €200-400/kW | 1-2 yıl |
| Impeller trim | %10-25 | €500-2000 | 0.5-1 yıl |
| Throttle eliminasyonu | %20-40 | Değişken | 1-2 yıl |
| Motor upgrade (IE3→IE4) | %2-4 | €100-200/kW | 3-5 yıl |
| Boru sistemi optimizasyonu | %5-15 | Değişken | 1-3 yıl |

## EGM Bazlı Tasarım Kuralları

### Optimum Boru Çapı
Bejan'ın boru akışı optimizasyonundan:
```
D_opt ∝ (ṁ × f / Nu)^(1/6)
```
İzotermik (yalıtımlı) boru için basitleştirme:
- Sürtünme entropi üretimi: S_gen = ṁ × ΔP / (ρ × T)
- Büyük çap → düşük S_gen ama yüksek yatırım
- Küçük çap → yüksek S_gen ama düşük yatırım
- Optimum: dC_total/dD = 0

### Throttle Valve — Tamamen İrreversibl
Kısma vanası termodinamiğin en verimsiz kontrol yöntemidir:
```
S_gen_vana = ṁ × ΔP / (ρ × T)    [kW/K]
```
Bu entropi üretiminin %100'ü kayıptır — hiçbir faydalı iş üretilmez.
**Her zaman VSD veya bypass ile değiştirmeyi değerlendir.**

### Vana Kayıpları Entropi Karşılığı
| Vana/Fitting Tipi | K (kayıp katsayısı) | 10 kg/s, DN100'de S_gen (W/K) |
|-------------------|---------------------|-------------------------------|
| Küresel vana (tam açık) | 0.05-0.1 | 0.01-0.02 |
| Sürgülü vana (tam açık) | 0.1-0.2 | 0.02-0.04 |
| Kelebek vana (tam açık) | 0.2-0.5 | 0.04-0.10 |
| Çekvalf (yaylı) | 1.0-2.5 | 0.20-0.50 |
| 90° dirsek (standart) | 0.3-0.6 | 0.06-0.12 |
| 90° dirsek (uzun radius) | 0.15-0.25 | 0.03-0.05 |
| T-bağlantı (dal akış) | 1.0-1.5 | 0.20-0.30 |
| Kısma vanası (%50 açık) | 5-15 | 1.0-3.0 |

**Pratik kural:** Kısma vanası, açık bir küresel vanaya göre 50-150 kat daha fazla entropi üretir.

### Pompa Sistemi Bejan Sayısı
- Be < 0.3 (tipik) — sürtünme baskın → boru/vana optimizasyonu öncelikli
- Pompa sistemlerinde ısı transferi irreversibility genellikle düşüktür

Detaylı bilgi: `knowledge/factory/entropy_generation/pipe_flow_egm.md`

## İleri Exergy Referans Değerleri

### Kaçınılamaz Koşullar (Pompa)
| Parametre | Kaçınılamaz Değer | Kaynak |
|-----------|-------------------|--------|
| Hidrolik verim (η_h) — Santrifüj | 0.85-0.90 | BAT santrifüj pompa |
| Hidrolik verim (η_h) — Pozitif deplasman | 0.80-0.88 | BAT referansı |
| Mekanik verim (η_mech) | 0.98-0.99 | Modern mekanik sızdırmazlık |
| Motor verimi (η_motor) | 0.96-0.97 | IE4 sınıfı |
| Kısma vanası | YOK (VSD kontrol) | Vana = tamamen kaçınılabilir |

### Tipik 4-Yollu Dekompozisyon (Santrifüj Pompa)
| Kategori | Tipik Oran (vanalı) | Tipik Oran (VSD'li) |
|----------|---------------------|---------------------|
| I_EN_AV | %45-60 | %20-30 |
| I_EN_UN | %20-30 | %40-55 |
| I_EX_AV | %8-15 | %10-15 |
| I_EX_UN | %5-10 | %10-15 |

### Göreceli Kaçınılabilirlik (θ)
- Pompa + kısma vanası tipik θ: 0.55-0.75 → YÜKSEK
- Pompa + VSD tipik θ: 0.25-0.40 → ORTA
- **Kısma vanası θ = 1.0** (tamamen kaçınılabilir — izentalpik genleşme)
- θ > 0.5 → Kısma vanası var mı kontrol et, VSD retrofit planla
- θ < 0.3 → Pompa zaten optimize (muhtemelen VSD mevcut)

### Önemli Not
Pompa I_total küçük olabilir (5-15 kW) ama θ çok yüksek olabilir (0.55-0.75). Bu, pompanın yatırım başına en verimli iyileştirme hedefi olabileceğini gösterir. Mutlak değer ile göreceli θ'yı birlikte değerlendir.

Detaylı bilgi: `knowledge/factory/advanced_exergy/equipment_specific/pump_advanced.md`

## Throttle Analizi

```
Throttle kayıp hesabı:
P_kayıp = ρ × g × Q × ΔH_vana / 1000 (kW)

ΔH_vana = Vana basınç düşüşü (m)
```
