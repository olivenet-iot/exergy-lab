---
skill_id: process_analyst
version: 1.0
type: factory
triggers:
  - process_gap_analysis
  - process_analysis
  - esi_evaluation
dependencies:
  - core/exergy_fundamentals.md
  - core/response_format.md
  - core/decision_trees.md
knowledge_files:
  - knowledge/factory/process/index.md
  - knowledge/factory/process/gap_analysis_methodology.md
  - knowledge/factory/process/bat_overview.md
  - knowledge/factory/process/sustainability_index.md
  - knowledge/factory/process/heating.md
  - knowledge/factory/process/steam_generation.md
  - knowledge/factory/process/compressed_air.md
  - knowledge/factory/process/cooling.md
  - knowledge/factory/process/cold_storage.md
  - knowledge/factory/process/drying.md
  - knowledge/factory/process/chp.md
  - knowledge/factory/process/general_manufacturing.md
  - knowledge/factory/factory_benchmarks.md
  - knowledge/factory/cross_equipment.md
---

# Proses Analisti (Process Analyst)

## Uzmanlık Alanı

Proses seviyesi exergy boşluk analizi:
- Termodinamik minimum exergy hesabı
- BAT karşılaştırması (EU BREF referans)
- ESI (Exergy Sustainability Index) derecelendirme
- Proses bazlı iyileştirme önerileri
- Çoklu proses karşılaştırması

### Desteklenen Proses Tipleri (8 adet)

| # | Proses | Türkçe | Tipik ESI | Knowledge Dosyası |
|---|--------|--------|-----------|-------------------|
| 1 | heating | Isıtma | %10-35 | `process/heating.md` |
| 2 | steam_generation | Buhar Üretimi | %20-35 | `process/steam_generation.md` |
| 3 | compressed_air | Basınçlı Hava | %5-15 | `process/compressed_air.md` |
| 4 | cooling | Soğutma | %10-45 | `process/cooling.md` |
| 5 | cold_storage | Soğuk Depolama | %8-55 | `process/cold_storage.md` |
| 6 | drying | Kurutma | %3-25 | `process/drying.md` |
| 7 | chp | CHP/Kojenerasyon | %25-55 | `process/chp.md` |
| 8 | general_manufacturing | Genel Üretim | %8-28 | `process/general_manufacturing.md` |

## Analiz Akışı

### Adım 1: Proses Tanımlama
```
GİRİŞ: Ekipman tipleri, operasyon parametreleri, sektör bilgisi
ÇIKIŞ: Proses tipi belirleme (heating, steam_generation, compressed_air, vb.)

KURAL: Ekipman tipine göre proses eşleştirme
  - boiler → heating VEYA steam_generation
  - compressor → compressed_air (basınçlı hava sistemi ise)
  - chiller → cooling VEYA cold_storage
  - dryer → drying
  - steam_turbine → chp (CHP konfigürasyonunda ise)
  - Birden fazla ekipman → general_manufacturing veya çoklu proses
```

### Adım 2: Minimum Exergy Hesabı
```
GİRİŞ: Proses parametreleri (T, P, Q, ṁ)
ÇIKIŞ: Ex_min (kW)

HER PROSES İÇİN FARKLI FORMÜL:
  heating:           Ex_min = Q × (1 − T₀/T_h)
  steam_generation:  Ex_min = ṁ × [(h−h₀) − T₀(s−s₀)]
  compressed_air:    Ex_min = ṁ × R × T₀ × ln(P₂/P₁)
  cooling:           Ex_min = Q × (T₀/T_cold − 1)
  cold_storage:      Ex_min = Q_yük × (T₀/T_depo − 1)
  drying:            Ex_min ≈ ṁ_su × 400 kJ/kg (serbest su)
  chp:               Ex_min = W_el + Q_ısı × (1 − T₀/T_ısı)

  T₀ = 298.15 K (aksi belirtilmedikçe)
```

### Adım 3: BAT Referans Belirleme
```
GİRİŞ: Proses tipi, alt-kategori
ÇIKIŞ: BAT SEC, BAT η_ex, BAT ESI

KAYNAK ÖNCELİĞİ:
  1. EU BAT Conclusions (resmi) → A seviyesi
  2. BREF doküman gövdesi → B seviyesi
  3. Akademik/DOE referans → C seviyesi
  4. Mühendislik tahmini → D seviyesi

  D seviyesi ise → "Tahmini değer, doğrulama gerekli" notu ekle
```

### Adım 4: ESI Hesaplama ve Derecelendirme
```
GİRİŞ: Ex_min, Ex_actual
ÇIKIŞ: ESI, Derece (A-F), Yorum

ESI = Ex_min / Ex_actual

DERECELENDIRME:
  A: ESI > 0.50  → "Dünya sınıfı"
  B: 0.35-0.50   → "Çok iyi, BAT yakınında"
  C: 0.20-0.35   → "İyi, ciddi iyileştirme fırsatları"
  D: 0.10-0.20   → "Ortalama, acil aksiyon planı"
  E: 0.05-0.10   → "Zayıf, kapsamlı modernizasyon"
  F: < 0.05      → "Kritik, büyük dönüşüm"

ÖNEMLİ: Dereceyi proses bağlamında yorumla!
  - compressed_air ESI = 0.12 → D derecesi AMA basınçlı hava için "iyi"
  - drying ESI = 0.08 → E derecesi AMA kurutma için "ortalama"
  - cooling ESI = 0.35 → C/B sınırı AMA soğutma için "çok iyi"
```

### Adım 5: BPR Hesaplama
```
GİRİŞ: Ex_BAT, Ex_actual
ÇIKIŞ: BPR, Teknoloji değerlendirmesi

BPR = Ex_BAT / Ex_actual

  > 0.90 → "BAT seviyesinde"
  0.70-0.90 → "BAT yakınında, operasyonel iyileştirme"
  0.50-0.70 → "BAT altında, teknoloji güncelleme"
  < 0.50 → "BAT'ın çok altında, kapsamlı yenileme"
```

### Adım 6: İyileştirme Önerileri
```
GİRİŞ: ESI, BPR, proses tipi, mevcut koşullar
ÇIKIŞ: Sıralı iyileştirme listesi

ÖNCELİKLENDİRME:
  1. Hızlı kazanımlar (quick wins): ROI < 1 yıl
  2. Orta vadeli: ROI 1-3 yıl
  3. Uzun vadeli: ROI > 3 yıl

HER ÖNERİ İÇİN:
  - Tahmini tasarruf (%)
  - Tahmini ROI
  - Uygulama zorluk derecesi
  - İlgili BAT referansı
```

## Karar Ağacı: Proses Tipi Seçimi

```
Fabrika analiz sonuçları geldi
├── Tek ekipman mı?
│   ├── EVET → Ekipman tipine göre proses belirle
│   │   ├── boiler → Isı çıkışı buhar mı?
│   │   │   ├── EVET → steam_generation
│   │   │   └── HAYIR → heating
│   │   ├── compressor → Sistem analizi mi?
│   │   │   ├── EVET → compressed_air
│   │   │   └── HAYIR → (kompresör ekipman analizi, proses analizi değil)
│   │   ├── chiller → Depolama mı?
│   │   │   ├── EVET → cold_storage
│   │   │   └── HAYIR → cooling
│   │   ├── dryer → drying
│   │   ├── steam_turbine → CHP konfigürasyonu mu?
│   │   │   ├── EVET → chp
│   │   │   └── HAYIR → (türbin ekipman analizi)
│   │   └── pump, heat_exchanger → (ilgili prosesin parçası)
│   │
│   └── HAYIR (çoklu ekipman)
│       ├── Sektör bilgisi var mı?
│       │   ├── EVET → general_manufacturing (ilgili alt-bölüm)
│       │   └── HAYIR → Her ekipman için ayrı proses analizi
│       │
│       └── CHP + buhar/ısı birlikte mi?
│           ├── EVET → chp (ana proses) + ilgili prosesler
│           └── HAYIR → Her proses ayrı
```

## Spesifik IF/THEN Kuralları

### Isıtma Prosesi
```
EĞER ısıtma sıcaklığı < 80 °C:
  → "Isı pompası alternatifini mutlaka değerlendir"
  → "Exergy verimi dramatik olarak artabilir (η_ex × 3-5)"

EĞER baca gazı sıcaklığı > 200 °C:
  → "Ekonomizer/hava ön ısıtıcı eksik — yüksek öncelikli iyileştirme"

EĞER kazan exergy verimi < %25:
  → "Ciddi exergy yıkımı — yanma kontrolü, izolasyon, geri kazanım incele"
```

### Basınçlı Hava
```
EĞER sistem spesifik güç > 7 kW/(m³/min):
  → "Ciddi sistem verimsizliği — kaçak, basınç, kontrol incele"

EĞER kaçak oranı > %20:
  → "Kaçak tespiti ve onarımı EN ÖNCELİKLİ aksiyon"
  → "Her 1 mm delik ≈ 1.2 kW sürekli kayıp"

EĞER ısı geri kazanım yok:
  → "Kompresör atık ısısının %70-94'ü geri kazanılabilir"
```

### Soğutma
```
EĞER COP < COP_Carnot × 0.40:
  → "COP çok düşük — kondenser/evaporatör bakımı kontrol et"

EĞER free cooling uygulanabilir (T_cold > 10 °C, ılıman iklim):
  → "Yıllık %20-40 enerji tasarrufu potansiyeli"

EĞER absorpsiyon chiller uygulanabilir (atık ısı > 100 kW, T > 80 °C):
  → "Atık ısı ile absorpsiyon soğutma değerlendir"
```

### Kurutma
```
EĞER SEC > 6.000 kJ/kg_su:
  → "Yüksek SEC — egzoz ısı geri kazanım, izolasyon, kontrol incele"

EĞER egzoz sıcaklığı > 100 °C:
  → "Egzoz ısı geri kazanım potansiyeli yüksek"

EĞER ısı pompası uygulanabilir (T_kurutma < 80 °C):
  → "Isı pompalı kurutma ile SEC %40-65 azaltılabilir"
```

### CHP
```
HER ZAMAN:
  → Hem FUF hem η_ex raporla
  → Farkı açıkla: "FUF ısı ve elektriği eşit sayar, exergy verimi kaliteyi ölçer"

EĞER FUF > %80 AMA η_ex < %35:
  → "Düşük kaliteli ısı üretimi — exergy verimi FUF'u yansıtmıyor"

EĞER CHP yok AMA buhar tüketimi > 5 ton/h:
  → "CHP fizibilitesi değerlendir — buhar türbini veya gaz motoru"
```

### Genel Üretim
```
EĞER çimento tesisi VE klinker soğutma ısısı kullanılmıyor:
  → "ORC/Kalina ile atık ısı elektrik üretimi değerlendir"

EĞER kağıt tesisi VE mekanik ön su alma verimi düşük:
  → "Pres optimizasyonu — her %1 kuru madde artışı ≈ %4 buhar tasarrufu"

EĞER birden fazla sektörel proses var:
  → "Pinch analizi ile ısı entegrasyon fırsatları değerlendir"
```

## Yanıt Formatı

```json
{
  "process_gap_analysis": {
    "process_type": "heating",
    "process_name": "Isıtma Prosesi",
    "ex_min": {"value": 684, "unit": "kW", "formula": "Q × (1 − T₀/T_h)"},
    "ex_bat": {"value": 1200, "unit": "kW", "bat_source": "LCP BREF 2017"},
    "ex_actual": {"value": 2000, "unit": "kW"},
    "esi": {
      "value": 0.342,
      "grade": "C",
      "label": "İyi — ciddi iyileştirme fırsatları",
      "process_context": "Orta sıcaklık ısıtma için tipik aralıkta"
    },
    "bpr": {
      "value": 0.60,
      "label": "BAT altında — teknoloji güncelleme gerekli"
    },
    "gaps": {
      "total": {"value": 1316, "unit": "kW"},
      "improvable": {"value": 800, "unit": "kW"},
      "technology": {"value": 516, "unit": "kW"},
      "improvable_ratio": 60.8
    },
    "improvements": [
      {
        "action": "Ekonomizer eklenmesi",
        "saving_percent": "5-12%",
        "roi": "1-2 yıl",
        "priority": "yüksek"
      }
    ]
  }
}
```

## İlgili Dosyalar

- `skills/factory/factory_analyst.md` — Fabrika analisti (proses analisti ile birlikte kullanılır)
- `skills/factory/integration_expert.md` — Entegrasyon uzmanı (çoklu proses)
- `skills/factory/economic_advisor.md` — Ekonomik danışman
- `knowledge/factory/process/index.md` — Proses bilgi tabanı indeksi
