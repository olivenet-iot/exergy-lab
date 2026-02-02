---
skill_id: compressor_expert
version: 1.0
type: equipment
equipment_type: compressor
triggers:
  - single_equipment_analysis
  - equipment_type == "compressor"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/compressor/benchmarks.md
  - knowledge/compressor/formulas.md
  - knowledge/compressor/audit.md
  - knowledge/compressor/equipment/*.md
  - knowledge/compressor/solutions/*.md
---

# Kompresör Uzmanı

## Uzmanlık Alanı

Basınçlı hava sistemleri exergy analizi:
- Vidalı (screw), pistonlu, santrifüj kompresörler
- VSD, yük kontrolü, kaçak tespiti
- Atık ısı geri kazanımı
- Basınç optimizasyonu

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Spesifik güç | kW / (m³/min) | < 6.5 (7 bar) |
| Exergy verimi | Ex_out / Ex_in | > 50% |
| Kaçak oranı | Yük-boşta analizi | < 15% |
| Yük faktörü | Gerçek/Nominal | > 60% |

## Özel Kurallar

### Spesifik Güç Değerlendirmesi
```
7 bar için:
- < 6.0 kW/(m³/min): Mükemmel
- 6.0-6.5: İyi
- 6.5-7.5: Ortalama
- > 7.5: Kötü

Her +1 bar için +0.5 kW/(m³/min) ekle
```

### VSD Önerisi Koşulları
```
VSD öner eğer:
- Yük faktörü < 70% VE
- Çalışma saati > 4000 saat/yıl VE
- Motor gücü > 15 kW
```

### Atık Isı Potansiyeli
```
Geri kazanılabilir ısı = Motor gücü × 0.90 × 0.75
(Elektriğin %90'ı ısıya, bunun %75'i geri kazanılabilir)
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Kaçak tamiri | %10-30 enerji | Düşük | < 0.5 yıl |
| VSD retrofit | %15-35 enerji | €200-400/kW | 1-3 yıl |
| Basınç düşürme | %7/bar | Düşük | < 0.3 yıl |
| Atık ısı geri kazanım | €300-500/kW termal | €200-400/kW | 1-2 yıl |

## Yanıt Örneği

## EGM Bazlı Tasarım Kuralları

### Optimum Basınç Oranı / Kademe
Çok kademeli kompresörlerde her kademenin basınç oranı eşit olmalıdır:
```
r_opt = (P_out/P_in)^(1/n)
```
- n: kademe sayısı
- Eşit basınç oranı → minimum toplam S_gen

### Ara Soğutma Sıcaklığı (Intercooling)
İki kademeli kompresörde optimal ara soğutma sıcaklığı:
```
T_inter = √(T_in × T_out)
```
Geometrik ortalama → her kademede eşit entropi üretimi.

### Entropi Üretim Kaynakları
| Kaynak | S_gen Payı | Bejan Sayısı |
|--------|-----------|--------------|
| Mekanik sürtünme | %30-40 | Be < 0.5 |
| Gaz sıkıştırma ısısı | %25-35 | Be > 0.5 |
| Karışma/sızıntı | %15-25 | — |
| Motor kayıpları | %10-15 | — |

### Pratik EGM Kuralları
- VSD ile kısmi yükte S_gen %30-50 azaltılabilir (yük/boşta döngüsüne kıyasla)
- Ara soğutma: 2 kademe için S_gen %15-25 azalır (tek kademeye göre)
- Atık ısı geri kazanımı S_gen'i azaltmaz ama sistem genelinde exergy yıkımını düşürür
- Kaçaklar: her %1 kaçak ≈ %1 ilave S_gen (gereksiz sıkıştırma)

Detaylı bilgi: `knowledge/factory/entropy_generation/power_cycles_egm.md`

## İleri Exergy Referans Değerleri

### Kaçınılamaz Koşullar (Kompresör)
| Parametre | Kaçınılamaz Değer | Kaynak |
|-----------|-------------------|--------|
| İzentropik verim (η_is) — Vidalı | 0.92 | Tsatsaronis & Morosuk 2008 |
| İzentropik verim (η_is) — Santrifüj | 0.95 | Kelly et al. 2009 |
| İzentropik verim (η_is) — Pistonlu | 0.90 | Morosuk & Tsatsaronis 2011 |
| Mekanik verim (η_mech) | 0.98-0.99 | BAT referansı |
| Motor verimi (η_motor) | 0.96-0.97 | IE4 sınıfı |
| Aftercooler ΔT | 5°C | Plate HX minimum |
| Ara soğutucu ΔP | 0.05-0.10 bar | Minimum akış direnci |

### Tipik 4-Yollu Dekompozisyon (Vidalı Kompresör)
| Kategori | Tipik Oran | Açıklama |
|----------|-----------|----------|
| I_EN_AV | %25-35 | VSD, kademeli sıkıştırma ile azaltılabilir |
| I_EN_UN | %45-55 | Sıkıştırma termodinamik limiti |
| I_EX_AV | %5-10 | Soğutma sistemi etkileşimi |
| I_EX_UN | %8-12 | Sistem yapısal limiti |

### Göreceli Kaçınılabilirlik (θ)
- Vidalı kompresör tipik θ: 0.30-0.40
- θ > 0.4 → VSD retrofit ve/veya kademeli sıkıştırma öner
- θ < 0.25 → Kompresör zaten iyi durumda, sistem optimizasyonuna odaklan

Detaylı bilgi: `knowledge/factory/advanced_exergy/equipment_specific/compressor_advanced.md`

## Yanıt Örneği

```json
{
  "summary": "37 kW vidalı kompresör %58 exergy verimi ile kabul edilebilir seviyede çalışıyor ancak atık ısı geri kazanım potansiyeli değerlendirilmeli.",
  "key_findings": [
    {
      "finding": "Spesifik güç 6.8 kW/(m³/min) ile sektör ortalamasında",
      "severity": "medium",
      "evidence": "37 kW / 5.4 m³/min = 6.85"
    }
  ],
  "recommendations": [
    {
      "title": "Atık Isı Geri Kazanımı",
      "priority": "high",
      "description": "Kompresör atık ısısı (~25 kW termal) kazan besleme suyu ön ısıtması için kullanılabilir",
      "annual_savings_eur": 6000,
      "investment_eur": 12000,
      "payback_years": 2.0
    }
  ]
}
```
