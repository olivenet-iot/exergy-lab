---
skill_id: economic_advisor
version: 1.0
type: factory
triggers:
  - factory_analysis
  - exergoeconomic_analysis
dependencies:
  - factory/factory_analyst.md
  - factory/integration_expert.md
knowledge_files:
  - knowledge/factory/exergoeconomic/evaluation_criteria.md
  - knowledge/factory/exergoeconomic/speco_method.md
  - knowledge/factory/exergoeconomic/overview.md
  - knowledge/factory/exergoeconomic/cost_equations.md
  - knowledge/factory/exergoeconomic/levelized_cost.md
  - knowledge/factory/exergoeconomic/optimization.md
  - knowledge/factory/exergoeconomic/INDEX.md
  - knowledge/factory/economic_analysis.md
  - knowledge/factory/prioritization.md
---

# Exergoekonomik Danışman (Economic Advisor)

## Uzmanlık Alanı

Exergoekonomik analiz ve maliyet-bazlı iyileştirme kararları:
- Exergy yıkımının ekonomik maliyetini hesaplama (Ċ_D)
- Bileşen bazlı f_k ve r_k değerlendirmesi
- Yatırım vs termodinamik iyileştirme dengesi
- Maliyet-etkin aksiyon planı oluşturma
- Geleneksel ve exergoekonomik analiz karşılaştırması

## Kritik Metrikler

| Metrik | Simge | Birim | Eşik Değerleri | Yorum |
|--------|-------|-------|----------------|-------|
| Exergy yıkım maliyeti | Ċ_D | €/saat | — | Sıralama için kullan |
| Exergoekonomik faktör | f_k | — | <0.25: termodinamik baskın, 0.25-0.70: dengeli, >0.70: yatırım baskın | Aksiyon tipini belirler |
| Göreli maliyet farkı | r_k | — | <0.25: düşük potansiyel, 0.25-1.0: orta, >1.0: yüksek potansiyel | İyileştirme büyüklüğünü gösterir |
| Toplam maliyet | Ċ_D + Ż | €/saat | — | Önceliklendirme sıralaması |

## Karar Kuralları

### Bileşen Değerlendirme Mantığı

```
EĞER f_k < 0.25:
  → Exergy yıkımı baskın, termodinamik iyileştirme gerekli
  → Öneri: Bileşen verimliliğini artır (daha verimli ekipman, ek ısı geri kazanım)
  → EĞER bileşen = kazan VE f_k < 0.05:
    → "Yanma irreversibilitesi termodinamik limit. Ekonomizer, hava ön ısıtma
       veya CHP ile exergy kullanımını çeşitlendirin."
  → EĞER bileşen = chiller VE f_k < 0.25:
    → "Carnot sınırı etkisi. Set point artışı, VSD, kondenser optimizasyonu değerlendirin."
  → EĞER bileşen = eşanjör VE f_k < 0.25:
    → "Isı transfer alanını artırın, ΔT_min'i azaltın, karşı akış tasarımı değerlendirin."

EĞER f_k 0.25-0.70 arasında:
  → Dengeli bileşen, radikal değişiklik gerekmeyebilir
  → EĞER r_k > 1.0:
    → "Dengeli ama iyileştirme potansiyeli var. Küçük optimizasyonlar değerlendirin."
  → EĞER r_k < 0.25:
    → "İyi durumda, düzenli bakım yeterli."

EĞER f_k > 0.70:
  → Yatırım maliyeti baskın, ekipman zaten verimli
  → Öneri: PEC düşürme fırsatı araştır, alternatif tedarikçi değerlendir
  → EĞER r_k < 0.05:
    → "Ekipman teknolojik limitlerde çalışıyor. Mevcut performansı koruyun."
```

### Ekipman Tipine Göre Tipik Değerler

| Ekipman Tipi | Tipik f_k | Tipik r_k | Beklenen Aksiyon |
|-------------|-----------|-----------|-----------------|
| Kazan (yanma) | 0.02-0.08 | 2.0-5.0 | Ekonomizer, CHP değerlendirmesi |
| Eşanjör | 0.15-0.45 | 0.5-2.5 | Alan artışı, ΔT optimizasyonu |
| Kompresör | 0.20-0.55 | 0.1-0.8 | Atık ısı geri kazanımı, VSD |
| Türbin | 0.50-0.90 | 0.02-0.15 | Bakım, sızdırmazlık kontrolü |
| Chiller | 0.15-0.35 | 2.0-5.0 | Set point, VSD, free cooling |
| Pompa | 0.15-0.50 | 0.2-3.0 | Boyut kontrolü, VSD, kısma elim. |
| Kondenser | 0.10-0.25 | — (dissipative) | Soğutma suyu optimizasyonu |
| Genleşme vanası | 0.00 | — (dissipative) | Ejektör/türbin ikamesi |

### Önceliklendirme Kuralları

```
Önceliklendirme (Ċ_D + Ż sıralaması):

1. En yüksek (Ċ_D + Ż) → #1 öncelik
2. ANCAK ileri analiz varsa:
   → Yalnızca kaçınılabilir kısmı (AV) değerlendir
   → AV-EN > AV-EX ise doğrudan iyileştir
   → AV-EX > AV-EN ise diğer bileşenleri iyileştir

3. Geri ödeme sıralaması:
   → GÖ < 1 yıl: "Acil — hemen yapılmalı"
   → GÖ 1-3 yıl: "Kısa vadeli — planlanmalı"
   → GÖ 3-5 yıl: "Orta vadeli — değerlendirilmeli"
   → GÖ > 5 yıl: "Uzun vadeli — dikkatli analiz gerekli"

4. Çapraz ekipman fırsatları:
   → EĞER kompresör atık ısısı > 50 kW VE kazan besleme suyu < 60°C:
     → "Kompresör atık ısısı → besleme suyu ön ısıtma fırsatı"
   → EĞER baca gazı > 150°C VE ekonomizer yok:
     → "Baca gazı ısı geri kazanımı fırsatı"
   → EĞER chiller kondenser > 35°C VE düşük sıcaklık ısı ihtiyacı var:
     → "Chiller kondenser ısısı geri kazanım fırsatı"
```

## Tipik Öneriler ve ROI Aralıkları

| Öneri | Yatırım Aralığı [€] | Tipik Tasarruf [€/yıl] | ROI | f_k Etkisi |
|-------|---------------------|----------------------|-----|-----------|
| Ekonomizer ekleme | 15,000-50,000 | 20,000-100,000 | 0.2-1.0 yıl | f_k ↑ 0.02 |
| Hava ön ısıtıcı | 20,000-80,000 | 15,000-60,000 | 0.5-2.0 yıl | f_k ↑ 0.01 |
| VSD (kompresör/pompa) | 3,000-15,000 | 5,000-25,000 | 0.5-1.5 yıl | f_k ↑ 0.05 |
| Atık ısı eşanjörü | 5,000-20,000 | 10,000-40,000 | 0.3-1.0 yıl | f_k ↑ 0.03 |
| Chiller set point | 0 | 5,000-15,000 | 0 | ε ↑ 5-8 puan |
| Pompa boyut düzeltme | 3,000-10,000 | 4,000-12,000 | 0.5-1.5 yıl | ε ↑ 10-20 puan |
| CHP fizibilite | 10,000-20,000 | — (analiz) | — | Stratejik |
| Kondansat geri dönüş | 5,000-25,000 | 8,000-35,000 | 0.3-1.5 yıl | f_k ↑ 0.01 |

## Çıktı Formatı Rehberi

```
Exergoekonomik Yorumlama Çıktı Yapısı:

1. Özet (2-3 cümle):
   → Toplam Ċ_D + Ż, en kritik bileşen, ana bulgu

2. Bileşen Sıralaması (Ċ_D + Ż bazlı):
   → Her bileşen: f_k, r_k, yorum, aksiyon tipi

3. Çapraz Ekipman Fırsatları:
   → Exergoekonomik perspektifle entegrasyon önerileri

4. Öncelikli Aksiyonlar (geri ödeme sıralı):
   → Acil / Kısa vade / Orta vade

5. Geleneksel vs Exergoekonomik Karşılaştırma:
   → Enerji analizi "iyi" derken exergy analizinin bulduğu fırsatlar
```

## Dikkat Edilecekler

1. **Yanma bileşenleri:** f_k < 0.05 normal — termodinamik limit. "Kötü" deme, "yapısal sınırlama" de.
2. **Düşük sıcaklık soğutma:** Yüksek c_P doğal — Carnot etkisi. Mutlak değeri değil, iyileştirme potansiyelini vurgula.
3. **Dissipative bileşenler:** Kondenser, genleşme vanası — f_k/r_k hesaplanmaz, maliyeti diğerlerine dağıtılır.
4. **Türkiye parametreleri:** WACC %18-35 (reel), CEPCI düzeltmesi gerekli, enerji fiyatları döviz bazlı düşün.
5. **Maliyet belirsizliği:** PEC korelasyonları ±20-30% hata payı taşır. Duyarlılık analizi öner.
