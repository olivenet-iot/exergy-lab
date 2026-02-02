# ExergyLab AI Skill Dosyaları

Bu dizin, ExergyLab AI yorumlama sisteminin davranışını tanımlayan skill dosyalarını içerir. Her dosya, AI'ın belirli bir alanda nasıl yanıt üreteceğini, hangi karar ağaçlarını takip edeceğini ve çıktı formatını belirler.

## Dizin Yapısı

```
skills/
├── README.md                          ← Bu dosya
├── SKILL_exergy_calculator.md         — Exergy hesaplama skill tanımı
├── SKILL_exergy_interpreter.md        — Exergy yorumlama skill tanımı
├── core/                              — Temel beceriler (3 dosya)
│   ├── exergy_fundamentals.md         — Exergy temel kavramları ve terminoloji
│   ├── response_format.md             — AI yanıt formatı (JSON schema)
│   └── decision_trees.md              — Karar ağaçları (tüm ekipmanlar)
├── equipment/                         — Ekipman uzmanları (7 dosya)
│   ├── compressor_expert.md           — Kompresör AI uzmanı
│   ├── boiler_expert.md               — Kazan AI uzmanı
│   ├── chiller_expert.md              — Chiller AI uzmanı
│   ├── pump_expert.md                 — Pompa AI uzmanı
│   ├── heat_exchanger_expert.md       — Isı eşanjörü AI uzmanı
│   ├── steam_turbine_expert.md        — Buhar türbini AI uzmanı
│   └── dryer_expert.md               — Kurutma fırını AI uzmanı
├── factory/                           — Fabrika analizi (3 dosya)
│   ├── factory_analyst.md             — Fabrika seviyesi analiz uzmanı
│   ├── integration_expert.md          — Çapraz ekipman entegrasyon uzmanı
│   └── economic_advisor.md            — Exergoekonomik danışman
└── output/                            — Çıktı formatı (1 dosya)
    └── turkish_style.md               — Türkçe yazım ve terminoloji kuralları
```

## Dosya Sayıları

| Kategori | Dosya Sayısı | Açıklama |
|----------|-------------|----------|
| Root skills | 2 | Hesaplama ve yorumlama ana skill tanımları |
| Core | 3 | Temel kavramlar, yanıt formatı, karar ağaçları |
| Equipment | 7 | Kompresör, kazan, chiller, pompa, ısı eşanjörü, buhar türbini, kurutma fırını |
| Factory | 3 | Fabrika analisti, entegrasyon uzmanı, ekonomik danışman |
| Output | 1 | Türkçe yazım kuralları |
| **Toplam** | **17** | |

## Kullanım

Skill dosyaları, `api/services/claude_code_service.py` tarafından AI yorumlama sırasında otomatik olarak yüklenir. Her ekipman analizi için ilgili equipment skill dosyası + core dosyaları birlikte kullanılır.

### Yükleme Sırası
1. `core/exergy_fundamentals.md` — Temel terminoloji [Her zaman]
2. `core/response_format.md` — Çıktı formatı [Her zaman]
3. `core/decision_trees.md` — Karar ağaçları [Her zaman]
4. `equipment/{type}_expert.md` — İlgili ekipman uzmanı [Ekipman analizinde]
5. `factory/factory_analyst.md` — Fabrika analisti [Fabrika analizinde]
6. `factory/integration_expert.md` — Entegrasyon uzmanı [Çoklu ekipmanda]
7. `factory/economic_advisor.md` — Ekonomik danışman [Maliyet analizinde]
8. `output/turkish_style.md` — Türkçe kuralları [Her zaman]

### Skill Dosyası Yazım Kuralları
- Her skill dosyasında YAML frontmatter bulunmalı
- Karar ağaçları açık ve takip edilebilir olmalı
- Eşik değerleri (threshold) sayısal ve net olmalı
- Referans bilgi tabanı dosyaları belirtilmeli
- Türkçe başlıklar, teknik terimler parantez içinde İngilizce
