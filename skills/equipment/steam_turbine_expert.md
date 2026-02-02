---
skill_id: steam_turbine_expert
version: 1.0
type: equipment
equipment_type: steam_turbine
triggers:
  - single_equipment_analysis
  - equipment_type == "steam_turbine"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/steam_turbine/benchmarks.md
  - knowledge/steam_turbine/formulas.md
  - knowledge/steam_turbine/audit.md
  - knowledge/steam_turbine/equipment/*.md
  - knowledge/steam_turbine/solutions/*.md
  - knowledge/steam_turbine/systems/*.md
  - knowledge/steam_turbine/economics/*.md
---

# Buhar Türbini Uzmanı

## Uzmanlık Alanı

Buhar türbinleri ve CHP/kojenerasyon sistemleri exergy analizi:
- Karşı basınçlı (back-pressure), yoğuşmalı (condensing), çekişli (extraction) türbinler
- ORC (Organic Rankine Cycle) düşük sıcaklık türbinleri
- Mikro türbin ve PRV ikamesi uygulamaları
- CHP/CCHP sistem konfigürasyonları ve optimizasyonu
- Overhaul planlama ve bozunma (degradation) analizi

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| İzentropik verim (isentropic eff.) | η_is = (h_in - h_out) / (h_in - h_out,is) | > %80 (>5 MW) |
| Exergy verimi — iş bazlı | η_ex = Ẇ / (Ėx_in - Ėx_out) | > %72 |
| Exergy verimi — CHP toplam | η_ex,CHP = (Ẇ + Ėx_ısı) / Ėx_yakıt | > %32 |
| Heat rate (ısı hızı) | HR = Q̇_yakıt / Ẇ_net [kJ/kWh] | < 10,000 (condensing) |
| Spesifik buhar tüketimi (SSC) | SSC = ṁ / Ẇ_elek [kg/kWh] | < 5 (condensing) |
| Isı/Güç oranı (HPR) | HPR = Q̇_ısı / Ẇ_elek | Sektöre bağlı |
| Birincil enerji tasarrufu (PES) | PES = 1 - 1/(η_e/η_ref_e + η_ı/η_ref_ı) | > %10 |

## Özel Kurallar

### Exergy Verimi Değerlendirmesi — İş Bazlı
```
Buhar türbini iş bazlı exergy verimi:
- > 82%: Mükemmel — izleme ve rutin bakım yeterli
- 72-82%: İyi — küçük iyileştirme fırsatları araştır
- 60-72%: Orta — detaylı analiz ve overhaul değerlendir
- < 60%: Kritik — acil müdahale, major overhaul veya yenileme gerekli

Not: İş bazlı exergy verimi ≈ izentropik verime yakındır
(mekanik ve jeneratör kayıpları hariç).
```

### CHP Değerlendirmesi — Exergy Bazlı
```
CHP exergy verimi (η_ex,CHP):
- > 38%: İyi — yüksek verimli CHP, en iyi uygulama
- 32-38%: Kabul edilebilir — optimizasyon potansiyeli mevcut
- 25-32%: Orta — sistem revizyonu ve entegrasyon iyileştirmesi gerekli
- < 25%: Düşük — CHP konfigürasyonu gözden geçirilmeli

Dikkat: Enerji verimi %85+ olsa bile exergy verimi %25-35 olabilir.
Düşük sıcaklıklı proses buharı (< 5 bar) exergy verimini düşürür.
Bu, buhar türbini CHP'nin doğasıdır — yüksek HPR = düşük exergy verimi.
```

### PRV İkamesi Önerisi
```
Mikro türbin ile PRV ikamesi öner eğer:
- PRV debisi > 3 ton/h VE
- Basınç düşüşü (ΔP) > 10 bar VE
- Çalışma süresi > 4,000 saat/yıl

Potansiyel güç tahmini:
Ẇ ≈ ṁ × (h_HP - h_LP) × η_is × 0.94  [kW]
η_is = %55-65 (tek kademe mikro türbin)

ROI genellikle 2-5 yıl.
PRV exergy kaybı %100 → Türbin ile %40-55 geri kazanılabilir.
```

### Overhaul Önerisi
```
Major overhaul öner eğer:
- Çalışma saati > 40,000 saat VE/VEYA
- η_is bozunma (degradation) > %3 puan (design'a göre)

Bozunma sınıflandırması:
- %1-3 bozunma: Sızdırmazlık yenileme (minor overhaul)
- %3-6 bozunma: Orta bakım (intermediate — seal + kanat muayene)
- %6-10 bozunma: Major overhaul (rotor, kanat, tüm sızdırmazlık)
- > %10 bozunma: Yenileme ekonomik analizi (overhaul vs. yeni türbin)

Overhaul ROI genellikle 0.5-2 yıl (en yüksek ROI yatırımlardan).
> 100K saat türbinlerde yenileme ciddi olarak değerlendirilmeli.
```

## Exergy Kayıp Dağılımı (Tipik)

| Kayıp Kaynağı | Oran [%] | Açıklama |
|---------------|----------|----------|
| Kanat profil kayıpları (blade profile losses) | 2-5 | Aerodinamik kayıplar |
| İkincil akış kayıpları (secondary flow) | 1-3 | Kanat kök/uç bölgesi |
| Kanat ucu sızıntısı (tip leakage) | 1-4 | Sızdırmazlık aşınmasına bağlı |
| Nem kayıpları (moisture losses) | 0-3 | Yaş buhar bölgesinde (condensing) |
| Çıkış kinetik enerji (leaving loss) | 0.5-2 | Son kademe kanat boyuna bağlı |
| Sızdırmazlık kayıpları (seal leakage) | 0.5-2 | Şaft ve interstage seals |
| Mekanik kayıplar (bearings, governor) | 0.5-1 | Rulman sürtünmesi |
| Kondensere atılan exergy | 5-20 | Yalnızca condensing türbinlerde |

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Sızdırmazlık yenileme | %0.5-2 η_is | €20-50K | 0.3-1 yıl |
| Major overhaul | %2-5 η_is | €50-200K/MW | 0.5-2 yıl |
| Kontrol sistemi modernizasyonu | %1-3 güç artışı | €30-80K | 1-2 yıl |
| Kondenser temizliği/vakum iyileştirme | %1-2 güç (condensing) | €10-30K | 0.5-1 yıl |
| PRV → Mikro türbin ikamesi | 100-500 kW elektrik | €1,500-3,000/kW | 2-5 yıl |
| ORC atık ısı geri kazanımı | 50-5,000 kW elektrik | €1,500-4,000/kW | 3-7 yıl |
| Yük eşleştirme optimizasyonu | %5-15 yakıt | Düşük | < 0.5 yıl |
| Kondensat geri dönüş artırma | %1-3 yakıt | €5-15K | 0.5-1.5 yıl |

## JSON Yanıt Örneği

```json
{
  "summary": "10 MW karşı basınçlı buhar türbini CHP sistemi %78 izentropik verim ve %27 CHP exergy verimi ile çalışmaktadır. İzentropik verim design değerinden %4 düşük olup sızdırmazlık aşınmasına işaret etmektedir. Overhaul ile yıllık €130,000 tasarruf potansiyeli bulunmaktadır.",
  "key_findings": [
    {
      "finding": "İzentropik verim %78 — design %82'den %4 puan düşük, sızdırmazlık aşınması muhtemel",
      "severity": "medium",
      "evidence": "55,000 saat çalışma, son overhaul 5 yıl önce, η_is bozunma profili ile uyumlu"
    },
    {
      "finding": "CHP exergy verimi %27 — sektör ortalaması (%25-35) aralığında ancak iyileştirme potansiyeli mevcut",
      "severity": "low",
      "evidence": "Düşük basınçlı proses buharı (4 bar) nedeniyle exergy verimi doğal olarak sınırlı"
    },
    {
      "finding": "Türbin iç exergy yıkımı 1,460 kW — giriş exergisinin %8.4'ü",
      "severity": "medium",
      "evidence": "Exergy dengesi: 17,328 - 10,686 - 5,182 = 1,460 kW irreversibility"
    }
  ],
  "recommendations": [
    {
      "title": "Sızdırmazlık Yenileme (Seal Replacement)",
      "priority": "high",
      "description": "Interstage ve shaft sızdırmazlıkların yenilenmesi ile η_is %2 puan iyileştirme beklenir. Planlı bakım periyodunda uygulanabilir.",
      "annual_savings_eur": 42000,
      "investment_eur": 35000,
      "payback_years": 0.8
    },
    {
      "title": "Major Overhaul Planlaması",
      "priority": "medium",
      "description": "55K saat çalışma sonucu %4 η_is bozunması mevcuttur. 60K saat dolmadan major overhaul planlanmalıdır. Kanat muayenesi, tüm sızdırmazlıklar ve rulman değişimi kapsamında.",
      "annual_savings_eur": 130000,
      "investment_eur": 280000,
      "payback_years": 2.2
    },
    {
      "title": "Kondensat Geri Dönüş Oranı Artırma",
      "priority": "low",
      "description": "Mevcut kondensat geri dönüş oranı %65 — %80'e çıkarılması ile kazan yakıt tasarrufu sağlanır.",
      "annual_savings_eur": 25000,
      "investment_eur": 15000,
      "payback_years": 0.6
    }
  ],
  "exergy_analysis": {
    "exergy_input_kw": 17328,
    "useful_output_kw": 5182,
    "exergy_destruction_kw": 1460,
    "exergy_efficiency_work_pct": 78.0,
    "exergy_efficiency_chp_pct": 26.6,
    "primary_loss_source": "Türbin iç tersinmezlik (blade + seal losses)"
  }
}
```
