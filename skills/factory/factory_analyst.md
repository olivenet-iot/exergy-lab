---
skill_id: factory_analyst
version: 1.0
type: factory
triggers:
  - factory_analysis
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
  - equipment/*.md
knowledge_files:
  - knowledge/factory/cross_equipment.md
  - knowledge/factory/prioritization.md
  - knowledge/factory/factory_benchmarks.md
  - knowledge/factory/sector_*.md
  - knowledge/factory/pinch/INDEX.md
  - knowledge/factory/pinch/fundamentals.md
  - knowledge/factory/pinch/targeting.md
  - knowledge/factory/pinch/hen_retrofit.md
  - knowledge/factory/thermoeconomic_optimization/overview.md
  - knowledge/factory/thermoeconomic_optimization/iterative_method.md
  - knowledge/factory/thermoeconomic_optimization/practical_guide.md
  - knowledge/factory/advanced_exergy/INDEX.md
  - knowledge/factory/advanced_exergy/overview.md
  - knowledge/factory/advanced_exergy/four_way_splitting.md
  - knowledge/factory/advanced_exergy/ideal_conditions.md
  - knowledge/factory/advanced_exergy/interpretation_guide.md
  - knowledge/factory/advanced_exergy/improvement_priority.md
---

# Fabrika Analisti

## Uzmanlık Alanı

Fabrika seviyesi exergy analizi:
- Çoklu ekipman aggregation
- Hotspot belirleme
- Cross-equipment entegrasyon
- Sektörel karşılaştırma
- Önceliklendirme

## Analiz Sırası

1. **Aggregation:** Toplam exergy giriş, çıkış, kayıp
2. **Hotspot:** En büyük kayıp kaynakları
3. **Cross-equipment:** Entegrasyon fırsatları
4. **Sektör karşılaştırma:** Benchmark
5. **Önceliklendirme:** ROI bazlı sıralama

## Fabrika Exergy Verimi Benchmark

| Sektör | Düşük | Ortalama | İyi |
|--------|-------|----------|-----|
| Çimento | < 25% | 25-35% | > 35% |
| Kimya | < 30% | 30-45% | > 45% |
| Gıda | < 15% | 15-25% | > 25% |
| Tekstil | < 20% | 20-30% | > 30% |
| Metal | < 25% | 25-40% | > 40% |
| Kağıt | < 30% | 30-45% | > 45% |

## Cross-Equipment Fırsatları

### Kompresör → Kazan
```
Potansiyel: Kompresör gücünün %50-70'i termal olarak geri kazanılabilir
Kullanım: Kazan besleme suyu ön ısıtma
Tipik ROI: 1.5-2.5 yıl
```

### Kazan → Absorption Chiller
```
Potansiyel: Baca gazı ısısı ile soğutma
Kullanım: Eşzamanlı buhar ve soğutma ihtiyacı varsa
Tipik ROI: 3-5 yıl
```

### Chiller → Sıcak Su
```
Potansiyel: Kondenser ısısının %15-20'si
Kullanım: Düşük sıcaklık ısıtma, sıcak su
Tipik ROI: 2-4 yıl
```

## Önceliklendirme Kuralları

```
Sıralama kriterleri (ağırlıklı):
1. ROI (payback) - %40
2. Mutlak tasarruf (€/yıl) - %30
3. Uygulama kolaylığı - %20
4. Risk - %10

Quick Wins (önce yap):
- ROI < 1 yıl
- Düşük yatırım
- Düşük risk

Strategic Projects (sonra planla):
- Yüksek mutlak tasarruf
- ROI 2-5 yıl
- Kapsamlı mühendislik gerektirir
```

## Pinch Analizi Karar Kuralları

### Pinch Analizi Öner
Aşağıdaki koşullar sağlandığında detaylı pinch analizi öner:

```
Koşul 1: Fabrikada 3+ sıcak akış VE 2+ soğuk akış varsa
Koşul 2: Toplam ısı yükü > 500 kW ise
Koşul 3: Hem ısıtma hem soğutma ihtiyacı varsa

→ Öneri: "Detaylı pinch analizi ile %10-30 ek tasarruf mümkün"
→ Referans: knowledge/factory/pinch/fundamentals.md, pinch/targeting.md
```

### Retrofit Öner
Mevcut tesiste pinch tabanlı iyileştirme öner:

```
Koşul 1: Mevcut ısı entegrasyon oranı < %30 ise
Koşul 2: Cross-pinch transfer > %20 ise
Koşul 3: Mevcut utility kullanımı > QH,min × 1.5 ise

→ Öneri: "HEN retrofit ile kayda değer tasarruf potansiyeli"
→ Referans: knowledge/factory/pinch/hen_retrofit.md, pinch/practical_guide.md
```

### Utility Optimizasyonu Öner
```
Koşul: Tek seviye utility kullanılıyor ve toplam utility > 1,000 kW ise
→ Öneri: "Çoklu utility seviyesi ile maliyet optimizasyonu mümkün"
→ Referans: knowledge/factory/pinch/utility_systems.md, pinch/grand_composite.md
```

## İleri Exergy Tabanlı Önceliklendirme

### İleri Exergy Analizi Tetikleyicileri
Aşağıdaki koşullardan herhangi biri sağlandığında ileri exergy analizi öner:

```
Tetikleyici 1: Fabrikada 3+ ekipman varsa ve toplam I_total > 100 kW
  → Konvansiyonel sıralama yanıltıcı olabilir
  → OKU: advanced_exergy/overview.md

Tetikleyici 2: Büyük I_total olan ekipman var ama düşük iyileştirme beklentisi
  → θ düşük olabilir (kazan gibi), gerçek potansiyel az
  → OKU: advanced_exergy/four_way_splitting.md

Tetikleyici 3: Ekipmanlar arası güçlü etkileşim var (atık ısı, soğutma suyu paylaşımı)
  → Ekzojen bileşen yüksek olabilir
  → OKU: advanced_exergy/endogenous_exogenous.md
```

### Göreceli Kaçınılabilirlik (θ) ile Önceliklendirme
```
θ = I_AV / I_total (her ekipman için)

Karar kuralları:
- θ > 0.5: YÜKSEK öncelik → Quick Win kategorisine yükselt
- θ = 0.3-0.5: ORTA → Maliyet-fayda analizi yap
- θ < 0.3: DÜŞÜK → Düşük öncelik (I_total büyük olsa bile!)

Tipik θ değerleri:
- Pompa + kısma vanası: 0.55-0.75 (en yüksek)
- Chiller: 0.40-0.55
- Kompresör: 0.30-0.40
- Türbin: 0.35-0.45
- Kazan: 0.15-0.25 (en düşük)
```

### IPN (Improvement Priority Number) ile Sıralama
```
IPN_k = (I_AV,k × c_F,k × t_annual) / Σ_j(I_AV,j × c_F,j × t_annual)

IPN: [0, 1] arasında, toplamları = 1.0
En yüksek IPN = en yüksek yatırım önceliği

Kombine skor (konvansiyonel + ileri):
Score_k = 0.3 × ROI_score + 0.3 × IPN_k + 0.2 × θ_k + 0.2 × kolaylık_score
```

### Konvansiyonel vs İleri Sıralama Karşılaştırması
Her fabrika analizinde:
1. Konvansiyonel sıralama (I_total büyükten küçüğe)
2. İleri sıralama (IPN ile)
3. Fark varsa açıkça belirt: "İleri analiz, sıralamayı değiştirmektedir..."

Referans: `knowledge/factory/advanced_exergy/improvement_priority.md`

## Termoekonomik Optimizasyon Tetikleyicileri

Aşağıdaki koşullardan herhangi biri sağlandığında termoekonomik optimizasyon öner
ve `knowledge/factory/thermoeconomic_optimization/` bilgi tabanına yönlendir:

```
Tetikleyici 1: Toplam exergy yıkım maliyeti > 50.000 €/yıl
  → Basit ROI yeterli değil, bileşen bazlı Ċ_D analizi gerekli
  → OKU: thermoeconomic_optimization/iterative_method.md

Tetikleyici 2: f_k < 0.25 olan bileşen varsa
  → Exergy yıkım maliyeti baskın, bileşen verimliliği artırılmalı
  → OKU: thermoeconomic_optimization/overview.md (Bölüm 4: f_k yorumlama)

Tetikleyici 3: f_k > 0.70 olan bileşen varsa
  → Yatırım maliyeti baskın, daha ucuz alternatif değerlendirilmeli
  → OKU: thermoeconomic_optimization/overview.md (Bölüm 4: f_k yorumlama)

Tetikleyici 4: Birden fazla büyük yatırım alternatifi varsa
  → Bütünleşik optimizasyon gerekli, tek tek ROI yanıltıcı
  → OKU: thermoeconomic_optimization/practical_guide.md (Bölüm 3: Yöntem seçim matrisi)

Tetikleyici 5: CHP / büyük sistem konfigürasyon kararı varsa
  → Yapısal optimizasyon (MINLP) değerlendirilmeli
  → OKU: thermoeconomic_optimization/structural_optimization.md

Tetikleyici 6: CBAM etkisi değerlendiriliyorsa (AB ihracatı olan sektörler)
  → Çok amaçlı optimizasyon (maliyet + CO₂) gerekli
  → OKU: thermoeconomic_optimization/multi_objective.md
```

## Basitleştirilmiş Termoekonomik Tarama

Her fabrika analizinde hızlı termoekonomik tarama yap:

```
Hızlı Ċ_D Hesaplama (her ekipman için):

  Ċ_D,k ≈ c_fuel × Ėx_D,k × τ    [€/yıl]

  c_fuel varsayılanları:
    Doğalgaz exergy maliyeti: ~0.037 €/kWh
    Elektrik exergy maliyeti: ~0.11 €/kWh

Prosedür:
  1. Her ekipman için Ėx_D hesapla (exergy analizinden)
  2. Yakıt tipine göre c_fuel seç
  3. Ċ_D,k = c_fuel × Ėx_D,k × τ hesapla
  4. Ċ_D,k sıralama → en büyük 3 kaynak = öncelikli hedef
  5. Toplam Σ Ċ_D > 50.000 €/yıl ise → detaylı termoekonomik analiz öner

Referans: thermoeconomic_optimization/practical_guide.md (Bölüm 5: Hızlı tarama)
```

## Sektör Bilgisi Kullanımı

Sektör biliniyorsa mutlaka `knowledge/factory/sector_{sector}.md` oku ve:
- Tipik enerji dağılımını referans al
- Sektöre özel best practice'leri öner
- BAT (Best Available Techniques) referans ver
