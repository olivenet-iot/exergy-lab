# ExergyLab Brief: AI Sistemi Güncelleme (Post-Expansion)

> **Claude Code için:** Knowledge base 119 → 305 dosyaya genişledi. 3 yeni ekipman ve 6 ileri analiz yöntemi eklendi. AI sistemini (skills, decision trees, service, CLAUDE.md) bu yeni kapsamla güncellemek gerekiyor. Tüm bağlantıları kur, tutarlılığı sağla.

---

## 🎯 OTONOM YETKİ

Bu brief'i uygularken:
1. Önce mevcut proje yapısını tamamen incele (`/home/ubuntu/exergy-lab/`)
2. Mevcut tüm skill, knowledge ve service dosyalarını oku
3. Brief'teki görevleri tamamla
4. Kendi insiyatifinle ek iyileştirmeler yap
5. Eksik bağlantıları, tutarsızlıkları, hataları düzelt
6. **Mevcut çalışan işlevselliği bozma** — testler geçmeli
7. Commit ve push YAPMA

---

## 📋 MEVCUT DURUM (Güncelleme Öncesi)

### Proje Genişlemesi

```
ÖNCEKİ (Brief 0 zamanı):          ŞİMDİ:
─────────────────────────          ──────
4 ekipman tipi                     7 ekipman tipi
  - Kompresör                        - Kompresör
  - Kazan                            - Kazan
  - Chiller                          - Chiller
  - Pompa                            - Pompa
                                     - Isı Eşanjörü (YENİ)
                                     - Buhar Türbini/CHP (YENİ)
                                     - Kurutma Fırını (YENİ)

0 ileri analiz yöntemi             6 ileri analiz yöntemi
                                     - Pinch Analizi (YENİ)
                                     - Enerji Yönetimi/ISO 50001 (YENİ)
                                     - İleri Exergy Analizi (YENİ)
                                     - Exergoekonomik Analiz (YENİ)
                                     - Termoekonomik Optimizasyon (YENİ)
                                     - Entropi Üretim Minimizasyonu (YENİ)

119 knowledge dosyası              305 knowledge dosyası
~25K satır                         141K satır
```

### Güncellenmesi Gereken Dosyalar

```
GÜNCELLENMESİ GEREKEN:
├── CLAUDE.md                              # Proje rehberi (kapsamlı güncelleme)
├── skills/
│   ├── README.md                          # Skills sistemi açıklaması
│   ├── core/
│   │   ├── exergy_fundamentals.md         # İleri exergy kavramları ekle
│   │   ├── response_format.md             # Yeni analiz tipleri için JSON schema
│   │   └── decision_trees.md              # 3 yeni ekipman + ileri analiz ağaçları
│   ├── equipment/
│   │   ├── heat_exchanger_expert.md       # Brief 1'de oluşturuldu - DOĞRULA
│   │   ├── steam_turbine_expert.md        # Brief 2'de oluşturuldu - DOĞRULA
│   │   └── dryer_expert.md                # Brief 3'te oluşturuldu - DOĞRULA
│   ├── factory/
│   │   ├── factory_analyst.md             # İleri yöntem referansları ekle
│   │   ├── integration_expert.md          # Yeni ekipman entegrasyonları ekle
│   │   └── economic_advisor.md            # Exergoekonomik referanslar ekle
│   └── output/
│       └── turkish_style.md               # Yeni terimler ekle (varsa)
└── api/
    └── services/
        └── claude_code_service.py         # Yeni ekipman/analiz tip desteği
```

---

## 📋 GÖREV 1: CLAUDE.md Kapsamlı Güncelleme

`/CLAUDE.md` dosyasını baştan yaz. Bu dosya projenin tam resmini vermeli.

### Güncellenecek Bölümler:

#### 1.1 Proje Özeti
- 7 ekipman tipi
- 6 ileri analiz yöntemi
- 305 knowledge dosyası, 141K satır
- 17 skill dosyası
- 202 test

#### 1.2 Dizin Yapısı
Tam güncel dizin yapısını yansıt:

```
exergy-lab/
├── CLAUDE.md
├── QA_REPORT.md
│
├── api/
│   ├── routes/
│   │   ├── analysis.py        # Ekipman analizi (7 tip)
│   │   ├── factory.py         # Fabrika analizi
│   │   └── interpret.py       # AI yorumlama
│   ├── schemas/
│   └── services/
│       └── claude_code_service.py  # AI entegrasyonu
│
├── engine/
│   ├── compressor.py
│   ├── boiler.py
│   ├── chiller.py
│   ├── pump.py
│   ├── factory.py
│   └── sankey.py
│
├── knowledge/                  # 305 dosya, 141K satır
│   ├── INDEX.md
│   ├── compressor/    (19 dosya)
│   ├── boiler/        (23 dosya)
│   ├── chiller/       (25 dosya)
│   ├── pump/          (23 dosya)
│   ├── heat_exchanger/ (21 dosya)  ← YENİ
│   ├── steam_turbine/  (23 dosya)  ← YENİ
│   ├── dryer/          (26 dosya)  ← YENİ
│   └── factory/
│       ├── (34 root dosya)
│       ├── advanced_exergy/     (18 dosya)  ← YENİ
│       ├── energy_management/   (21 dosya)  ← YENİ
│       ├── entropy_generation/  (19 dosya)  ← YENİ
│       ├── exergoeconomic/      (18 dosya)  ← YENİ
│       ├── pinch/               (18 dosya)  ← YENİ
│       └── thermoeconomic_optimization/ (16 dosya) ← YENİ
│
├── skills/                     # 17 dosya
│   ├── README.md
│   ├── core/
│   │   ├── exergy_fundamentals.md
│   │   ├── response_format.md
│   │   └── decision_trees.md
│   ├── equipment/
│   │   ├── compressor_expert.md
│   │   ├── boiler_expert.md
│   │   ├── chiller_expert.md
│   │   ├── pump_expert.md
│   │   ├── heat_exchanger_expert.md  ← YENİ
│   │   ├── steam_turbine_expert.md   ← YENİ
│   │   └── dryer_expert.md           ← YENİ
│   ├── factory/
│   │   ├── factory_analyst.md
│   │   ├── integration_expert.md
│   │   └── economic_advisor.md
│   └── output/
│       └── turkish_style.md
│
├── frontend/
│   └── src/
│
└── tests/
    ├── test_api.py
    ├── test_engine.py
    └── test_skills.py    (95 test)
```

#### 1.3 AI Yorumlama Sistemi

Tam güncel akışı açıkla:

```
Kullanıcı isteği
       ↓
Analiz tipi belirleme
       ↓
┌──────────────────────────────────────────┐
│ Skill Yükleme (Modüler)                 │
│                                          │
│ 1. Core Skills (her zaman)               │
│    - exergy_fundamentals                 │
│    - response_format                     │
│    - decision_trees                      │
│                                          │
│ 2. Equipment Skill (7 tipten biri)       │
│    - compressor / boiler / chiller       │
│    - pump / heat_exchanger               │
│    - steam_turbine / dryer               │
│                                          │
│ 3. Factory Skills (fabrika analizi ise)  │
│    - factory_analyst                     │
│    - integration_expert                  │
│    - economic_advisor                    │
│                                          │
│ 4. İleri Analiz (varsa)                  │
│    - advanced_exergy                     │
│    - exergoeconomic                      │
│    - pinch_analysis                      │
│    - entropy_generation                  │
│    - thermoeconomic_optimization         │
│    - energy_management                   │
│                                          │
│ 5. Output Style                          │
│    - turkish_style                       │
└──────────────────────────────────────────┘
       ↓
Knowledge Yükleme (İlgili dosyalar)
       ↓
Claude API çağrısı
       ↓
Yapılandırılmış JSON yanıt
```

#### 1.4 Yeni Ekipman Tipleri Açıklaması

Her yeni ekipman için:
- Ne analiz edilir
- Hangi knowledge dosyaları kullanılır
- Exergy analizi yaklaşımı
- Tipik verim aralıkları

#### 1.5 İleri Analiz Yöntemleri

Her yöntem için kısa açıklama:
- Ne zaman kullanılır
- Hangi knowledge dosyaları
- Giriş/çıkış tanımı

#### 1.6 Güncel İstatistikler

```
Knowledge Base: 305 dosya, 141,229 satır
Skills: 17 dosya
Testler: 202 geçiyor
Ekipman: 7 tip
İleri Analiz: 6 yöntem
```

---

## 📋 GÖREV 2: Core Skills Güncelleme

### 2.1 skills/core/exergy_fundamentals.md

Mevcut dosyayı oku ve şu bölümleri ekle (yoksa):

```markdown
## İleri Exergy Kavramları

### Kaçınılabilir vs Kaçınılamaz Exergy Yıkımı
- I_total = I_avoidable + I_unavoidable
- Kaçınılabilir: Mevcut teknolojiyle azaltılabilir
- Kaçınılamaz: Termodinamik sınırların sonucu
- Detay: knowledge/factory/advanced_exergy/

### Endojen vs Ekzojen Exergy Yıkımı
- I_total = I_endogenous + I_exogenous
- Endojen: Ekipmanın kendi iç kayıpları
- Ekzojen: Diğer ekipmanlardan kaynaklanan
- Detay: knowledge/factory/advanced_exergy/

### Dörtlü Ayrıştırma
- I_EN_AV: Endojen-Kaçınılabilir → Bu ekipmanı iyileştir
- I_EN_UN: Endojen-Kaçınılamaz → Yapılamaz
- I_EX_AV: Ekzojen-Kaçınılabilir → Diğer ekipmanı iyileştir
- I_EX_UN: Ekzojen-Kaçınılamaz → Yapılamaz

### Exergoekonomik Temel Kavramlar
- SPECO metodu: c_P, c_F, Ċ_D, Ż_k
- Exergoekonomik faktör: f_k = Ż/(Ż + Ċ_D)
- Detay: knowledge/factory/exergoeconomic/

### Entropi Üretim Minimizasyonu (EGM)
- Bejan yaklaşımı: min S_gen
- Gouy-Stodola: I = T₀ × S_gen
- Bejan sayısı: Be = S_gen_ΔT / S_gen_total
- Detay: knowledge/factory/entropy_generation/

### Pinch Analizi Temel
- Minimum enerji hedefleri (MER)
- Composite curves
- ΔT_min seçimi
- Detay: knowledge/factory/pinch/
```

### 2.2 skills/core/response_format.md

Yeni analiz tipleri için JSON schema'lar ekle:

```markdown
## İleri Exergy Analizi JSON Schema

{
  "avoidable_unavoidable": {
    "equipment_id": "string",
    "I_total_kW": number,
    "I_avoidable_kW": number,
    "I_unavoidable_kW": number,
    "I_avoidable_percent": number,
    "improvement_potential": "string"
  },
  "endogenous_exogenous": {
    "equipment_id": "string",
    "I_endogenous_kW": number,
    "I_exogenous_kW": number,
    "exogenous_sources": ["string"]
  },
  "four_way_split": {
    "I_EN_AV_kW": number,
    "I_EN_UN_kW": number,
    "I_EX_AV_kW": number,
    "I_EX_UN_kW": number,
    "priority_action": "string"
  }
}

## Exergoekonomik Analiz JSON Schema

{
  "equipment_costs": [
    {
      "equipment_id": "string",
      "Z_investment_eur_h": number,
      "C_destruction_eur_h": number,
      "c_product_eur_kwh": number,
      "c_fuel_eur_kwh": number,
      "f_exergoeconomic": number,
      "r_relative_cost_diff": number,
      "recommendation": "string"
    }
  ],
  "total_cost_eur_year": number,
  "optimization_potential_eur_year": number
}

## Pinch Analizi JSON Schema

{
  "pinch_temperature_C": number,
  "minimum_hot_utility_kW": number,
  "minimum_cold_utility_kW": number,
  "current_hot_utility_kW": number,
  "current_cold_utility_kW": number,
  "saving_potential_kW": number,
  "saving_potential_percent": number,
  "delta_t_min_C": number,
  "recommended_hen_modifications": ["string"]
}
```

### 2.3 skills/core/decision_trees.md

Mevcut dosyayı oku. Şu karar ağaçlarını ekle (yoksa):

#### Isı Eşanjörü Karar Ağacı
```
BAŞLA: Isı eşanjörü analizi
│
├── Effectiveness < 60%?
│   ├── EVET → Düşük performans
│   │   ├── U değeri düşmüş mü? (fouling?)
│   │   │   └── OKU: heat_exchanger/solutions/fouling_management.md
│   │   ├── Approach temp > 15°C?
│   │   │   └── OKU: heat_exchanger/solutions/approach_temp.md
│   │   └── Eşanjör eski/küçük?
│   │       └── OKU: heat_exchanger/solutions/retrofit.md
│   └── HAYIR → Kabul edilebilir
│       └── Basınç düşüşü kontrolü
│
└── Exergy yıkımı analizi
    ├── S_gen_ΔT baskın (Be > 0.5) → ΔT azalt
    └── S_gen_ΔP baskın (Be < 0.5) → Akış direncini azalt
```

#### Buhar Türbini / CHP Karar Ağacı
```
BAŞLA: Buhar türbini / CHP analizi
│
├── Türbin tipi?
│   ├── Back-pressure → Proses buhar + güç dengesi
│   ├── Condensing → Vakum performansı
│   └── Extraction → Her seviye ayrı
│
├── İzentropik verim < benchmark?
│   └── OKU: steam_turbine/solutions/efficiency_improvement.md
│
├── CHP sistemi ise:
│   ├── PES > 10%? → Yüksek verimli CHP ✓
│   ├── PHR (Power-to-Heat Ratio) kontrol
│   └── Exergy paylaşımı: Elektrik vs Isı
│
├── ORC potansiyeli?
│   └── Düşük sıcaklık atık ısı > 100 kW ve > 90°C?
│       └── OKU: steam_turbine/equipment/orc.md
│
└── SONUÇ: Verim, maliyet, emisyon önerileri
```

#### Kurutma Fırını Karar Ağacı
```
BAŞLA: Kurutma fırını analizi
│
├── ÖNEMLİ NOT: Kurutma inherently exergy-destructive
│   Tipik exergy verimi %10-25 (konvektif)
│   Bu diğer ekipmanlardan farklı!
│
├── SMER < 0.5 kg/kWh?
│   └── EVET → Ciddi verim sorunu
│
├── Egzoz sıcaklığı > 80°C?
│   └── OKU: dryer/solutions/exhaust_heat_recovery.md
│
├── Egzoz bağıl nem < 60%?
│   └── OKU: dryer/solutions/air_recirculation.md
│
├── Düşük sıcaklık kurutma (<80°C)?
│   └── OKU: dryer/solutions/heat_pump_retrofit.md
│
├── Mekanik ön su alma yapılıyor mu?
│   └── HAYIR → OKU: dryer/solutions/mechanical_dewatering.md
│
└── SONUÇ: Egzoz geri kazanımı genellikle en büyük potansiyel
```

#### İleri Analiz Tetikleme Karar Ağacı
```
BAŞLA: Hangi ileri analiz yöntemi önerilmeli?
│
├── Fabrikada 3+ ekipman var mı?
│   ├── EVET + Hem ısıtma hem soğutma var
│   │   └── ÖNERİ: Pinch Analizi
│   │       → knowledge/factory/pinch/
│   │
│   ├── EVET + Yatırım kararı gerekiyor
│   │   └── ÖNERİ: Exergoekonomik Analiz
│   │       → knowledge/factory/exergoeconomic/
│   │
│   └── EVET + Hangi ekipmana odaklanmalı belirsiz
│       └── ÖNERİ: İleri Exergy Analizi (dörtlü ayrıştırma)
│           → knowledge/factory/advanced_exergy/
│
├── Tek ekipman optimizasyonu mu?
│   └── ÖNERİ: Entropi Üretim Minimizasyonu
│       → knowledge/factory/entropy_generation/
│
├── Maliyet-verim dengesi mi?
│   └── ÖNERİ: Termoekonomik Optimizasyon
│       → knowledge/factory/thermoeconomic_optimization/
│
├── ISO 50001 / Enerji denetimi mi?
│   └── ÖNERİ: Enerji Yönetim Sistemi
│       → knowledge/factory/energy_management/
│
└── Tüm ileri yöntemler isteğe bağlı olarak önerilir
    → Fabrika yorumunun sonunda "İleri Analiz Önerileri" bölümü ekle
```

---

## 📋 GÖREV 3: Equipment Skills Doğrulama

Brief 1-3 tarafından oluşturulan skill dosyalarını kontrol et:

### 3.1 skills/equipment/heat_exchanger_expert.md
Kontrol et:
- [ ] YAML frontmatter (skill_id, version, type, triggers, dependencies, knowledge_files)
- [ ] Kritik metrikler tablosu (U, effectiveness, NTU, approach temp, exergy verimi)
- [ ] Karar ağacı
- [ ] Tip bazlı değerlendirme (shell&tube, plate, air-cooled, economizer)
- [ ] Tipik öneriler ve ROI tablosu
- [ ] JSON yanıt örneği
- [ ] Cross-reference (boiler economizer, compressor heat recovery, chiller condenser)

Eksik varsa tamamla.

### 3.2 skills/equipment/steam_turbine_expert.md
Kontrol et:
- [ ] YAML frontmatter
- [ ] Kritik metrikler (izentropik verim, exergy verimi, PES, PHR)
- [ ] Karar ağacı (back-pressure, condensing, extraction, ORC)
- [ ] CHP değerlendirme kuralları
- [ ] Ekonomik fizibilite kriterleri
- [ ] JSON yanıt örneği
- [ ] Cross-reference (boiler, factory CHP)

Eksik varsa tamamla.

### 3.3 skills/equipment/dryer_expert.md
Kontrol et:
- [ ] YAML frontmatter
- [ ] Kritik metrikler (SMER, exergy verimi, egzoz sıcaklık/nem)
- [ ] Karar ağacı
- [ ] UYARI: Kurutma inherently düşük exergy verimli — bunu AI'a vurgula
- [ ] Sektör bazlı kurutma tipleri
- [ ] JSON yanıt örneği
- [ ] Cross-reference (boiler steam, heat_exchanger exhaust recovery)

Eksik varsa tamamla.

---

## 📋 GÖREV 4: Factory Skills Güncelleme

### 4.1 skills/factory/factory_analyst.md

Mevcut dosyayı oku ve şu güncellemeleri yap:

1. **Ekipman listesini güncelle:** 4 → 7 tip
2. **Benchmark tablosuna yeni ekipmanları ekle**
3. **Cross-equipment matrisini genişlet:**

```
YENİ CROSS-EQUIPMENT FIRSATLARI:

Isı Eşanjörü:
- Her entegrasyon bir eşanjörden geçer — eşanjör seçimi/boyutlandırma tavsiyesi ver

Buhar Türbini:
- Kazan → Türbin → Proses buhar (back-pressure CHP)
- Yüksek basınç buhar → Türbin → Düşük basınç buhar + Elektrik
- Baca gazı / Egzoz → ORC → Elektrik (düşük sıcaklık)

Kurutma Fırını:
- Kazan buharı → Kurutma
- Kompresör atık ısı → Düşük sıcaklık kurutma ön ısıtma
- Kurutma egzozu → Isı eşanjörü → Besleme havası ön ısıtma
- Kurutma egzozu → Isı pompası → Kurutma havası (kapalı çevrim)
- Kurutma + Chiller → Absorption chiller potansiyeli
```

4. **İleri analiz önerisi bölümü ekle:**

```markdown
## İleri Analiz Önerileri

Fabrika analizinin sonunda, uygun olan ileri analiz yöntemlerini öner:

| Koşul | Öneri |
|-------|-------|
| 3+ ekipman + ısıtma/soğutma | Pinch Analizi |
| Yatırım kararı gerekiyor | Exergoekonomik Analiz |
| Hangi ekipmana odaklanılacağı belirsiz | İleri Exergy (dörtlü ayrıştırma) |
| ISO 50001 uyumluluk | Enerji Yönetim Sistemi |
| Tasarım optimizasyonu | Termoekonomik Optimizasyon |
| Ekipman boyutlandırma | Entropi Üretim Minimizasyonu |
```

### 4.2 skills/factory/integration_expert.md

Yeni entegrasyon kalıplarını ekle:

```markdown
## Yeni Entegrasyon Kalıpları

### Kurutma Sistemi Entegrasyonları
1. Kazan buharı → Kurutma havası ısıtma
2. Kompresör atık ısı → Kurutma ön ısıtma (düşük T)
3. Kurutma egzozu → Eşanjör → Taze hava ön ısıtma
4. Kurutma egzozu → Isı pompası → Kurutma havası (COP 3-5)
5. Kurutma egzozu → Absorption chiller (eşzamanlı soğutma varsa)

### CHP Entegrasyonları
1. Kazan → Back-pressure türbin → Proses buhar + Elektrik
2. Gaz türbini → HRSG → Proses buhar
3. Düşük sıcaklık atık ısı → ORC → Elektrik
4. Motor CHP → Isı geri kazanım → Proses/ısıtma

### Isı Eşanjörü Ağı Optimizasyonu
1. Mevcut eşanjörlerin performans değerlendirmesi
2. Pinch analizi ile yeni eşanjör önerileri
3. Eşanjör tipi seçimi (shell&tube vs plate)
4. Fouling yönetimi ve bakım planı
```

### 4.3 skills/factory/economic_advisor.md

Exergoekonomik referanslar ekle (yoksa oluştur):

```markdown
## Exergoekonomik Değerlendirme Kuralları

### Temel Metrikler
- f_k (exergoekonomik faktör): Ż / (Ż + Ċ_D)
- r_k (göreli maliyet farkı): (c_P - c_F) / c_F
- Ċ_D (exergy yıkım maliyeti): c_F × İ_D

### Yorumlama
- f_k < 0.25 → "Exergy yıkım maliyeti baskın → ekipman verimliliğini artır"
- f_k > 0.70 → "Yatırım maliyeti baskın → daha ekonomik alternatif düşün"
- Yüksek r_k → "Bu ekipman ürün maliyetini önemli ölçüde artırıyor"
- Yüksek Ċ_D → "Para burada kaybediliyor — öncelikli iyileştirme"

### Referans Knowledge
- Detay: knowledge/factory/exergoeconomic/
- SPECO metodu: knowledge/factory/exergoeconomic/speco_method.md
- Maliyet fonksiyonları: knowledge/factory/exergoeconomic/cost_equations.md
```

---

## 📋 GÖREV 5: claude_code_service.py Güncelleme

`/api/services/claude_code_service.py` dosyasını oku ve güncelle:

### 5.1 Yeni Ekipman Tipleri Desteği

```python
# _load_skills() metodunda yeni ekipman tiplerini ekle
EQUIPMENT_TYPES = [
    "compressor", "boiler", "chiller", "pump",
    "heat_exchanger", "steam_turbine", "dryer"  # YENİ
]

# _load_relevant_knowledge() metodunda yeni dizinleri ekle
KNOWLEDGE_DIRS = {
    "compressor": "knowledge/compressor/",
    "boiler": "knowledge/boiler/",
    "chiller": "knowledge/chiller/",
    "pump": "knowledge/pump/",
    "heat_exchanger": "knowledge/heat_exchanger/",    # YENİ
    "steam_turbine": "knowledge/steam_turbine/",       # YENİ
    "dryer": "knowledge/dryer/",                       # YENİ
}
```

### 5.2 İleri Analiz Yöntemi Desteği

```python
# Yeni metot: interpret_advanced_analysis()
ADVANCED_METHODS = {
    "advanced_exergy": {
        "skill": "factory/factory_analyst.md",
        "knowledge_dir": "knowledge/factory/advanced_exergy/",
        "key_files": ["overview.md", "four_way_splitting.md", "methodology.md"]
    },
    "exergoeconomic": {
        "skill": "factory/economic_advisor.md",
        "knowledge_dir": "knowledge/factory/exergoeconomic/",
        "key_files": ["speco_method.md", "evaluation_criteria.md"]
    },
    "pinch_analysis": {
        "skill": "factory/integration_expert.md",
        "knowledge_dir": "knowledge/factory/pinch/",
        "key_files": ["fundamentals.md", "composite_curves.md", "hen_design.md"]
    },
    "entropy_generation": {
        "knowledge_dir": "knowledge/factory/entropy_generation/",
        "key_files": ["overview.md", "heat_transfer_egm.md"]
    },
    "thermoeconomic_optimization": {
        "knowledge_dir": "knowledge/factory/thermoeconomic_optimization/",
        "key_files": ["overview.md", "iterative_method.md"]
    },
    "energy_management": {
        "knowledge_dir": "knowledge/factory/energy_management/",
        "key_files": ["iso_50001_overview.md", "audit_methodology.md"]
    }
}
```

### 5.3 Modüler Knowledge Yükleme

_load_relevant_knowledge() metodunu güncelle — yeni ekipman ve ileri analiz knowledge dosyalarını yükleyebilmeli.

### 5.4 Fabrika Analizi Prompt'unda İleri Yöntemler

Fabrika analizi yapılırken, ileri analiz yöntemlerini öneren bir bölüm ekle:

```python
def _build_factory_prompt(self, ...):
    # ... mevcut prompt ...
    
    # İleri analiz önerileri
    prompt += """
    
    Analizin sonunda, uygun olduğunda şu ileri yöntemleri öner:
    - Pinch Analizi (3+ ekipman, ısıtma/soğutma varsa)
    - İleri Exergy Analizi (kaçınılabilir/kaçınılamaz ayrıştırma)
    - Exergoekonomik Analiz (maliyet optimizasyonu)
    - Enerji Yönetim Sistemi (ISO 50001 uyumluluk)
    """
```

---

## 📋 GÖREV 6: Cross-Reference Ağı Kontrolü

### 6.1 Mevcut Ekipmanlar → Yeni Ekipmanlar

Mevcut knowledge dosyalarında yeni ekipman referansları var mı kontrol et:

```
knowledge/boiler/solutions/economizer.md 
  → heat_exchanger/ referansı olmalı

knowledge/compressor/solutions/heat_recovery.md 
  → heat_exchanger/ referansı olmalı

knowledge/chiller/equipment/*.md 
  → heat_exchanger/ referansı olmalı (evaporatör/kondenser)

knowledge/factory/cross_equipment.md 
  → heat_exchanger/, steam_turbine/, dryer/ referansları olmalı

knowledge/factory/cogeneration.md 
  → steam_turbine/ referansı olmalı
```

Eksik referansları ekle.

### 6.2 Yeni Ekipmanlar → İleri Analiz

```
knowledge/heat_exchanger/formulas.md
  → entropy_generation/heat_exchanger_egm.md referansı

knowledge/steam_turbine/benchmarks.md
  → advanced_exergy/equipment_specific/turbine_advanced.md referansı

knowledge/dryer/formulas.md
  → entropy_generation/ referansı (kurutma EGM)
```

### 6.3 İleri Analiz Yöntemleri Arası Referanslar

```
advanced_exergy/ ↔ exergoeconomic/ (ileri exergoekonomik)
exergoeconomic/ ↔ thermoeconomic_optimization/ (optimizasyon)
entropy_generation/ ↔ advanced_exergy/ (Gouy-Stodola bağlantısı)
pinch/ ↔ heat_exchanger/ (HEN tasarımı)
energy_management/ ↔ tüm ekipmanlar (denetim prosedürleri)
```

---

## 📋 GÖREV 7: Skills README Güncelleme

`/skills/README.md` dosyasını kapsamlı güncelle:

```markdown
# ExergyLab Skills Sistemi

## Genel Bakış
Skills, AI'ın davranışını tanımlayan modüler dosyalardır.
Toplam: 17 skill dosyası

## Skill Kategorileri

### Core Skills (3)
| Skill | Dosya | Açıklama |
|-------|-------|----------|
| exergy_fundamentals | core/exergy_fundamentals.md | Temel + ileri exergy kavramları |
| response_format | core/response_format.md | JSON schema (7 ekipman + ileri analiz) |
| decision_trees | core/decision_trees.md | 7 ekipman + ileri analiz karar ağaçları |

### Equipment Skills (7)
| Skill | Dosya | Ekipman |
|-------|-------|---------|
| compressor_expert | equipment/compressor_expert.md | Kompresör |
| boiler_expert | equipment/boiler_expert.md | Kazan |
| chiller_expert | equipment/chiller_expert.md | Chiller |
| pump_expert | equipment/pump_expert.md | Pompa |
| heat_exchanger_expert | equipment/heat_exchanger_expert.md | Isı Eşanjörü |
| steam_turbine_expert | equipment/steam_turbine_expert.md | Buhar Türbini/CHP |
| dryer_expert | equipment/dryer_expert.md | Kurutma Fırını |

### Factory Skills (3)
| Skill | Dosya | Açıklama |
|-------|-------|----------|
| factory_analyst | factory/factory_analyst.md | Fabrika analizi + ileri yöntem önerileri |
| integration_expert | factory/integration_expert.md | Cross-equipment + pinch entegrasyonu |
| economic_advisor | factory/economic_advisor.md | Ekonomik + exergoekonomik değerlendirme |

### Output Skills (1)
| Skill | Dosya | Açıklama |
|-------|-------|----------|
| turkish_style | output/turkish_style.md | Türkçe yazım kuralları |

## Skill Seçim Mantığı

1. Analiz tipi belirlenir (single_equipment / factory / advanced)
2. Ekipman tipi belirlenir (7 tipten biri)
3. İlgili skill dosyaları yüklenir
4. Karar ağacı işletilir
5. İleri analiz gerekiyorsa ilgili knowledge yüklenir
6. Yanıt formatına göre çıktı üretilir
```

---

## 📋 GÖREV 8: Testlerin Geçtiğini Doğrula

```bash
cd /home/ubuntu/exergy-lab
python -m pytest tests/ -v

# Frontend build
cd frontend && npm run build
```

Testler kırılırsa düzelt. Yeni skill/knowledge dosyaları test dosyalarında referans ediliyorsa güncelle.

---

## 📋 GÖREV 9: Genel Kalite İyileştirmeleri

Projeyi genel olarak tara ve şunları düzelt:

1. **Kırık cross-reference'lar:** Referans edilen dosya yolu var mı?
2. **Orphan dosyalar:** Hiçbir INDEX'te referans edilmeyen dosyalar
3. **Duplicate içerik:** Aynı bilginin birden fazla yerde tekrarlanması
4. **Terminoloji tutarlılığı:** "Isı eşanjörü" vs "eşanjör" vs "heat exchanger" — tutarlı mı?
5. **Birim tutarlılığı:** EUR vs USD, kW vs MW, °C vs K
6. **Kod-knowledge tutarlılığı:** Engine'deki formüller knowledge'daki formüllerle uyumlu mu?

---

## ✅ Tamamlama Kontrol Listesi

### CLAUDE.md:
- [ ] Tam güncel dizin yapısı
- [ ] 7 ekipman tipi açıklanmış
- [ ] 6 ileri analiz yöntemi açıklanmış
- [ ] AI yorumlama akışı güncel
- [ ] İstatistikler güncel (305 dosya, 141K satır)

### Core Skills:
- [ ] exergy_fundamentals.md → İleri kavramlar eklendi
- [ ] response_format.md → Yeni JSON schema'lar eklendi
- [ ] decision_trees.md → 3 yeni ekipman + ileri analiz ağaçları eklendi

### Equipment Skills:
- [ ] heat_exchanger_expert.md doğrulandı/tamamlandı
- [ ] steam_turbine_expert.md doğrulandı/tamamlandı
- [ ] dryer_expert.md doğrulandı/tamamlandı

### Factory Skills:
- [ ] factory_analyst.md → 7 ekipman + ileri yöntem önerileri
- [ ] integration_expert.md → Yeni entegrasyon kalıpları
- [ ] economic_advisor.md → Exergoekonomik kurallar

### Service:
- [ ] claude_code_service.py → 7 ekipman tipi desteği
- [ ] claude_code_service.py → İleri analiz yöntemi desteği

### Entegrasyon:
- [ ] Cross-reference'lar kontrol edildi ve tamamlandı
- [ ] Skills README güncellendi
- [ ] Testler geçiyor (202+)

**Bu brief projenin AI beynini günceller. Her görevi dikkatle tamamla. Commit ve push YAPMA.**
