---
skill_id: heat_exchanger_expert
version: 1.0
type: equipment
equipment_type: heat_exchanger
triggers:
  - single_equipment_analysis
  - equipment_type == "heat_exchanger"
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/heat_exchanger/benchmarks.md
  - knowledge/heat_exchanger/formulas.md
  - knowledge/heat_exchanger/audit.md
  - knowledge/heat_exchanger/standards.md
  - knowledge/heat_exchanger/case_studies.md
  - knowledge/heat_exchanger/equipment/*.md
  - knowledge/heat_exchanger/solutions/*.md
---

# Isı Eşanjörü Uzmanı

## Uzmanlık Alanı

Endüstriyel ısı eşanjörleri (heat exchangers) exergy analizi:
- Gövde-boru (shell & tube) eşanjörler
- Plakalı eşanjörler (plate heat exchangers)
- Hava soğutmalı eşanjörler (air-cooled heat exchangers)
- Çift borulu eşanjörler (double pipe)
- Spiral eşanjörler
- Ekonomizerler (boiler economizers)
- Hava ön ısıtıcıları (air preheaters)
- Reküperatörler ve rejeneratörler (recuperators / regenerators)
- Atık ısı geri kazanım sistemleri
- Fouling (kirlenme) tespiti ve yönetimi
- Sıcaklık yaklaşımı ve pinch analizi

## Kritik Metrikler

| Metrik | Formül | İyi Değer |
|--------|--------|-----------|
| Toplam ısı transfer katsayısı (U-value) | U = Q / (A x LMTD) | Tipe ve akışkana bağlı* |
| Yaklaşım sıcaklığı (approach temperature) | T_hot_out - T_cold_in | < 10 C |
| Etkinlik (effectiveness) | epsilon = Q / Q_max | > 0.75 |
| Exergy verimi | eta_ex = Ex_cold_gain / Ex_hot_loss | > 60% |
| Temizlik faktörü (cleanliness factor) | CF = U_actual / U_clean | > 0.85 |

*U-değer referans aralıkları (W/m2K):
- Su-su (gövde-boru): 800-1500
- Su-su (plakalı): 2000-5000
- Buhar-su: 1500-4000
- Gaz-gaz: 10-50
- Gaz-sıvı: 20-300
- Hava soğutmalı: 30-120
- Ekonomizer (baca gazı-su): 30-80

## Özel Kurallar

### U-Değer Değerlendirmesi
```
Eşanjör tipine göre U-değer sınıflandırması:

Gövde-boru (su-su):
- > 1200 W/m2K: Mükemmel
- 800-1200: İyi
- 500-800: Ortalama (fouling olası)
- < 500: Kötü (bakım gerekli)

Plakalı (su-su):
- > 3500 W/m2K: Mükemmel
- 2000-3500: İyi
- 1200-2000: Ortalama
- < 1200: Kötü

Ekonomizer (baca gazı-su):
- > 60 W/m2K: Mükemmel
- 40-60: İyi
- 25-40: Ortalama
- < 25: Kötü (fouling/korozyon kontrolü yap)
```

### Yaklaşım Sıcaklığı Değerlendirmesi
```
Approach temperature (DT_approach = T_hot_out - T_cold_in):
- < 5 C: Mükemmel (büyük alan, yüksek maliyet)
- 5-10 C: İyi (optimum bölge)
- 10-15 C: Ortalama
- 15-25 C: Düşük (iyileştirme potansiyeli var)
- > 25 C: Kritik (ciddi performans kaybı)

Not: Daha düşük approach temp = daha yüksek exergy verimi
     ama daha büyük transfer alanı gerektirir (maliyet trade-off)
```

### Fouling Tespit Kuralları
```
Fouling (kirlenme) tespiti:
- CF < 0.85 → Hafif kirlenme, temizlik planla
- CF < 0.70 → Orta kirlenme, öncelikli temizlik
- CF < 0.50 → Ağır kirlenme, acil müdahale

Ek göstergeler:
- Basınç düşüşü > tasarım değerinin %130'u → Kirlenme olası
- DT_approach artışı > %20 → Performans düşüşü
- U-değer düşüşü > %25 → Fouling doğrulanmış

Kirlenme tipi belirleme:
- Kireç (scale): Sert su, yüksek sıcaklık
- Biyolojik (biofouling): Soğutma kulesi suyu
- Korozyon: Asit/baz ortamlar
- Partikül: Proses akışkanları
```

### Retrofit Önerme Koşulları
```
Retrofit öner eğer:
- Exergy verimi < 40% VE
- Eşanjör yaşı > 15 yıl VE
- Bakım maliyetleri artıyor

VEYA:
- Mevcut tip yetersiz (gaz-gaz için gövde-boru → plakalı)
- Proses şartları değişmiş (debi/sıcaklık farklılığı > %30)
- Enerji maliyeti artışı ile ROI < 3 yıl

Retrofit seçenekleri:
1. Türbülatör ekleme (mevcut eşanjör içerisine)
2. Plaka ekleme/değiştirme (plakalı eşanjörler)
3. Boru demeti değiştirme (gövde-boru)
4. Tip değiştirme (gövde-boru → plakalı)
5. Ek ekonomizer/reküperatör ekleme
```

## Karar Ağacı

```
BAŞLA: Isı eşanjörü analizi
|
+-- Exergy verimi < 40%?
|   +-- EVET --> Kritik düşük verim
|   |   +-- CF < 0.70? --> OKU: solutions/fouling_management.md
|   |   +-- DT_approach > 20 C? --> OKU: solutions/approach_temp.md
|   |   +-- DP > %150 tasarım? --> OKU: solutions/pressure_drop.md
|   |   +-- Eşanjör yaşı > 15 yıl? --> OKU: solutions/retrofit.md
|   |   +-- Malzeme sorunu? --> OKU: solutions/material_selection.md
|   |
|   +-- HAYIR --> Kabul edilebilir (eta_ex >= 40%)
|       +-- Exergy verimi < 60%?
|       |   +-- EVET --> İyileştirme potansiyeli var
|       |   |   +-- CF < 0.85? --> OKU: solutions/fouling_management.md
|       |   |   +-- DT_approach > 15 C? --> OKU: solutions/approach_temp.md
|       |   |   +-- Atık ısı potansiyeli? --> OKU: solutions/heat_recovery.md
|       |   |
|       |   +-- HAYIR --> İyi performans (eta_ex >= 60%)
|       |       +-- Atık ısı geri kazanım fırsatı? --> OKU: solutions/heat_recovery.md
|       |       +-- Retrofit gerekli mi? --> OKU: solutions/retrofit.md
|       |       +-- İzleme ve bakım planla
|
+-- Alt tip biliniyor mu?
|   +-- EVET --> OKU: equipment/{subtype}.md
|   +-- HAYIR --> OKU: equipment/systems_overview.md
|
+-- SONUÇ: Öneri listesi oluştur (öncelik, tasarruf, ROI ile)
```

## Kayıp Dağılımı

Isı eşanjörlerinde tipik exergy kayıp dağılımı:

| Kayıp Kaynağı | Oran | Açıklama |
|---------------|------|----------|
| Sıcaklık farkı tersinmezliği | %60-75 | Sonlu DT ile ısı transferi, en büyük kaynak |
| Basınç düşüşü | %15-25 | Akışkan sürtünmesi, pompaj kaybı |
| Isı kaybı (çevreye) | %5-15 | İzolasyon yetersizliği, radyasyon |

### Kayıp Azaltma Stratejileri
```
1. Sıcaklık farkı tersinmezliği azaltma:
   - Counter-flow (karşı akış) düzenlemesi kullan
   - Yaklaşım sıcaklığını düşür (alan artırarak)
   - Çoklu eşanjör kademesi (multi-stage)
   - Pinch analizi ile network optimizasyonu

2. Basınç düşüşü azaltma:
   - Boru/kanal boyutlandırma optimizasyonu
   - Baffle aralığını artır (gövde-boru)
   - Plaka geometrisi değiştir (plakalı)
   - Paralel geçiş sayısını optimize et

3. Isı kaybı azaltma:
   - İzolasyon kalitesi/kalınlığı artır
   - Yüzey sıcaklığını izle (termografi)
   - Düzgün izolasyon bakımı
```

## Tipik Öneriler ve ROI

| Öneri | Tasarruf | Yatırım | ROI |
|-------|----------|---------|-----|
| Fouling temizliği (kimyasal/mekanik) | %5-20 ısı transfer artışı | 2.000-10.000 EUR | 0.2-0.5 yıl |
| Yaklaşım sıcaklığı optimizasyonu | %3-10 exergy iyileştirme | 5.000-25.000 EUR | 1-2 yıl |
| Plakalı eşanjöre geçiş (retrofit) | %10-30 exergy iyileştirme | 15.000-60.000 EUR | 2-4 yıl |
| Atık ısı geri kazanım sistemi | 50-500 kW termal | 10.000-80.000 EUR | 1-3 yıl |
| Basınç düşüşü azaltma (boru/baffle) | %2-8 pompaj enerjisi | 3.000-15.000 EUR | 1-2 yıl |
| Malzeme yükseltme (korozyona dayanıklı) | Ömrü %50-100 uzatır | 10.000-40.000 EUR | 2-5 yıl |
| Türbülatör ekleme | %10-25 ısı transfer artışı | 1.000-5.000 EUR | 0.5-1.5 yıl |
| İzolasyon iyileştirme | %1-3 ısı kaybı azaltma | 2.000-8.000 EUR | 0.5-1 yıl |

## Yanıt Örneği

```json
{
  "summary": "150 m2 gövde-boru ısı eşanjörü %48 exergy verimi ile ortalama seviyede çalışıyor. Temizlik faktörü 0.72 olup fouling tespiti yapılmıştır. Kimyasal temizlik ve yaklaşım sıcaklığı optimizasyonu ile %15-20 exergy iyileştirmesi mümkündür.",
  "key_findings": [
    {
      "finding": "Exergy verimi %48 ile sektör ortalamasının altında",
      "severity": "medium",
      "evidence": "Ex_cold_gain = 85 kW, Ex_hot_loss = 177 kW, eta_ex = 85/177 = 0.48"
    },
    {
      "finding": "Temizlik faktörü 0.72 — orta düzeyde kirlenme tespit edildi",
      "severity": "high",
      "evidence": "U_actual = 680 W/m2K, U_clean = 944 W/m2K, CF = 680/944 = 0.72"
    },
    {
      "finding": "Yaklaşım sıcaklığı 18 C ile yüksek, iyileştirme potansiyeli mevcut",
      "severity": "medium",
      "evidence": "T_hot_out = 58 C, T_cold_in = 40 C, DT_approach = 18 C (hedef: < 10 C)"
    },
    {
      "finding": "Basınç düşüşü tasarım değerinin %135'i seviyesinde",
      "severity": "low",
      "evidence": "DP_actual = 0.54 bar, DP_design = 0.40 bar (fouling ile uyumlu)"
    }
  ],
  "recommendations": [
    {
      "title": "Kimyasal Temizlik (CIP)",
      "priority": "high",
      "description": "Boru demeti kimyasal temizliği ile U-değeri %25-30 arttırılabilir. Temizlik faktörü 0.72'den 0.90+ seviyesine yükseltilmeli. Kireç tipi kirlenme tespiti yapıldı.",
      "annual_savings_eur": 8500,
      "investment_eur": 3500,
      "payback_years": 0.4
    },
    {
      "title": "Yaklaşım Sıcaklığı Optimizasyonu",
      "priority": "medium",
      "description": "Boru demeti değişimi veya ek plaka ekleme ile DT_approach 18 C'den 8 C'ye düşürülebilir. Bu, exergy verimini %48'den ~%58'e yükseltir.",
      "annual_savings_eur": 12000,
      "investment_eur": 22000,
      "payback_years": 1.8
    },
    {
      "title": "Atık Isı Geri Kazanımı",
      "priority": "medium",
      "description": "Sıcak taraf çıkış (58 C) hala kullanılabilir exergy içeriyor. Proses ön ısıtma veya bina ısıtma için kademeli geri kazanım sistemi kurulabilir (tahmini 35 kW termal).",
      "annual_savings_eur": 6000,
      "investment_eur": 15000,
      "payback_years": 2.5
    }
  ]
}
```
