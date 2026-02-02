---
skill_id: boiler_expert
version: 1.0
type: equipment
equipment_type: boiler
triggers:
  - single_equipment_analysis
  - equipment_type == "boiler"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/boiler/benchmarks.md
  - knowledge/boiler/formulas.md
  - knowledge/boiler/audit.md
  - knowledge/boiler/equipment/*.md
  - knowledge/boiler/solutions/*.md
---

# Kazan Uzmanı

## Uzmanlık Alanı

Buhar ve sıcak su kazanları exergy analizi:
- Ateş borulu, su borulu kazanlar
- Yanma optimizasyonu
- Ekonomizer, hava ön ısıtıcı
- Blowdown, kondensat geri dönüş

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Enerji verimi | Q_buhar / Q_yakıt | > 88% |
| Exergy verimi | Ex_buhar / Ex_yakıt | > 38% |
| Baca gazı sıcaklığı | Ölçüm | < 180°C |
| Fazla hava | O2 veya CO2 ölçümü | 10-15% |
| Blowdown oranı | | < 3% |

## Özel Kurallar

### Exergy Verimi Değerlendirmesi
```
Buhar kazanı için:
- > 40%: İyi
- 35-40%: Ortalama
- 30-35%: Düşük
- < 30%: Kritik (acil müdahale)

Not: Exergy verimi her zaman enerji veriminden düşüktür!
Tipik: Enerji %88 iken Exergy %35
```

### Ekonomizer Önerisi
```
Ekonomizer öner eğer:
- Baca gazı sıcaklığı > 180°C VE
- Kazan kapasitesi > 1 ton/h buhar
- ROI genellikle < 1.5 yıl
```

### Yanma Optimizasyonu
```
O2 seviyesi kontrolü:
- < 2%: Eksik yanma riski
- 2-4%: Optimum
- > 5%: Fazla hava kaybı

Her %1 fazla hava ≈ %0.5 verim kaybı
```

## Exergy Kayıp Dağılımı (Tipik)

| Kayıp Kaynağı | Oran |
|---------------|------|
| Yanma irreversibility | 25-30% |
| Baca gazı kaybı | 8-15% |
| Isı transferi irreversibility | 5-10% |
| Blowdown | 1-3% |
| Radyasyon | 1-2% |

## EGM Bazlı Tasarım Kuralları

### Yanma İrreversiblliği — En Büyük S_gen Kaynağı
Kazanlarda entropi üretiminin %55-65'i yanma prosesinden gelir:
```
S_gen_yanma ≈ Yakıt exergy'sinin %25-30'u
```
Bu, yanmanın doğası gereği yüksek derecede irreversible olmasından kaynaklanır (kimyasal → termal enerji dönüşümü). Tamamen ortadan kaldırılamaz ancak şu yollarla azaltılabilir:
- Fazla hava optimizasyonu (O₂ = %2-4 optimum)
- Hava ön ısıtma (yanma havası sıcaklığını artırarak ΔT azaltma)
- Oksijen zenginleştirme (ileri uygulama)

### Optimum Baca Gazı Sıcaklığı
Baca gazı sıcaklığı entropi-maliyet dengesiyle belirlenir:
```
T_baca_opt: S_gen_baca + S_gen_ekonomizer = minimum
```
- Düşük T_baca → düşük S_gen_baca ama büyük ekonomizer (yatırım)
- Yüksek T_baca → yüksek S_gen_baca ama küçük ekonomizer
- Tipik optimum: 120-160°C (doğalgaz), 150-180°C (fuel oil)
- Yoğuşmalı ekonomizer ile 50-65°C'ye indirilebilir (S_gen %35-50 azalır)

### Ekonomizer/Preheater: S_gen_ΔT Azaltma Aracı
```
S_gen_ΔT = Q̇ × (1/T_cold - 1/T_hot)
```
Ekonomizer, baca gazı ve besleme suyu arasındaki ΔT'yi kademeli olarak azaltarak S_gen_ΔT'yi düşürür. Her 20°C baca gazı sıcaklık düşüşü → yaklaşık %1 verim artışı.

### Bejan Sayısı — Kazan
| Bileşen | Tipik Be | Yorum |
|---------|----------|-------|
| Yanma odası | 0.85-0.95 | Isı transferi çok baskın |
| Konveksiyon bölümü | 0.70-0.85 | Isı transferi baskın |
| Ekonomizer | 0.50-0.70 | Dengeli |
| Hava ön ısıtıcı | 0.40-0.60 | Dengeye yakın |

Detaylı bilgi: `knowledge/factory/entropy_generation/power_cycles_egm.md`

## İleri Exergy Referans Değerleri

### Kaçınılamaz Koşullar (Kazan)
| Parametre | Kaçınılamaz Değer | Kaynak |
|-----------|-------------------|--------|
| Yanma tersinmezliği | %25-30 (exergy girdisinin) | Tsatsaronis 2009 |
| Baca gazı sıcaklığı (doğalgaz) | 130°C | Asit yoğuşma limiti |
| Baca gazı sıcaklığı (fuel oil) | 160°C | Kükürt asidi yoğuşma |
| Termal verim (η_th) | %95-96 | BAT yoğuşmalı kazan |
| Fazla hava | %5-8 | Optimum yanma |
| Isı transfer ΔT (alev-tüp) | 15-25°C | Minimum approach |
| Radyasyon kaybı | %0.5-1.0 | BAT yalıtım |

### Tipik 4-Yollu Dekompozisyon (Buhar Kazanı)
| Kategori | Tipik Oran | Açıklama |
|----------|-----------|----------|
| I_EN_AV | %10-18 | Ekonomizer, O₂ trim ile azaltılabilir |
| I_EN_UN | %60-70 | Yanma tersinmezliği (çoğunlukla kaçınılamaz) |
| I_EX_AV | %5-10 | Besleme suyu/hava sıcaklığı etkisi |
| I_EX_UN | %8-12 | Sistem yapısal limiti |

### Göreceli Kaçınılabilirlik (θ)
- Kazan tipik θ: 0.15-0.25 → DÜŞÜK
- Kazanlarda θ düşüktür çünkü yanma tersinmezliği termodinamiğin doğasıdır
- θ > 0.25 → Ekonomizer yok veya fazla hava çok yüksek, acil müdahale
- θ < 0.15 → Kazan zaten optimize, diğer ekipmanlara odaklan
- **Uyarı:** Kazan I_total çok büyük olabilir ama θ düşüktür — mutlak I_AV ile göreceli θ'yı birlikte değerlendir

### Exergoekonomik Maliyet Tahmini
```
C_D,kazan_AV = c_F × I_AV × t_annual
```
- c_F (doğalgaz) ≈ 0.035 €/kWh exergetik birim maliyet
- Tipik C_D,kazan_AV = 30,000-80,000 €/yıl (4-10 ton/h kazan)

Detaylı bilgi: `knowledge/factory/advanced_exergy/equipment_specific/boiler_advanced.md`

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Ekonomizer | %3-6 yakıt | €20-40K | 0.8-1.5 yıl |
| O2 trim | %1-3 yakıt | €5-15K | 0.5-1 yıl |
| Blowdown heat recovery | %1-2 yakıt | €5-10K | 1-2 yıl |
| Kondensat geri dönüş | %1/her %10 artış | Değişken | 0.5-1 yıl |
| İzolasyon | %1-2 | €3-8K | 0.5-1 yıl |
