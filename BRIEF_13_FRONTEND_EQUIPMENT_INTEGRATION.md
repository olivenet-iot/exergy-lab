# Brief 13: Frontend — 3 Yeni Ekipman UI Entegrasyonu

> **Claude Code için:** Bu brief'i oku ve uygula. Mevcut frontend pattern'larını önce incele, uyumsuzluk görürsen mevcut kodu referans al.

---

## 🎯 Hedef

Brief 12 ile backend'e eklenen **heat_exchanger, steam_turbine, dryer** engine'lerini frontend'e entegre et. 7/7 ekipman UI'dan analiz edilebilir hale gelecek.

**Durum:**
- Backend: ✅ 7/7 engine ready, API route'ları aktif, 307 test geçiyor
- Frontend: ❌ Sadece 4 ekipman görünüyor (compressor, boiler, chiller, pump)

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. **ÖNCE mevcut frontend kodunu oku** — her dosyayı incele, pattern'ı anla
3. Mevcut pattern ile uyumsuzluk varsa **mevcut kodu referans al** (brief'i değil)
4. Eksik gördüğün UX iyileştirmesi, validation, error handling ekle
5. **Mevcut çalışan ekipmanları (compressor, boiler, chiller, pump) ASLA bozma**
6. Backend testleri etkileme — `pytest tests/ -v` hâlâ 307 test geçmeli
7. Yeni Türkçe label'lar ve açıklamalar ekle

---

## 📋 Adım 0: ÖNCE Mevcut Frontend'i Anla (KRİTİK)

Kod yazmaya başlamadan ÖNCE tüm frontend dosyalarını incele. Backend pattern'larını Brief 12 zaten değiştirdi — şimdi frontend'in bunları nasıl kullandığını anlamalısın.

```bash
# 1. Genel yapı
find frontend/src -name "*.jsx" -o -name "*.js" | sort
cat frontend/package.json

# 2. Router ve sayfa yapısı
cat frontend/src/App.jsx
cat frontend/src/pages/EquipmentAnalysis.jsx

# 3. Form sistemi — nasıl çalışıyor?
cat frontend/src/components/forms/ParameterForm.jsx
cat frontend/src/components/forms/FormField.jsx
cat frontend/src/components/forms/CompressorTypeSelector.jsx
cat frontend/src/components/equipment/SubtypeSelector.jsx

# 4. Sonuç gösterimi
ls frontend/src/components/results/
cat frontend/src/components/results/ResultsPanel.jsx 2>/dev/null || echo "Not found"
cat frontend/src/components/results/BenchmarkChart.jsx 2>/dev/null || echo "Not found"
cat frontend/src/components/results/SankeyDiagram.jsx 2>/dev/null || echo "Not found"

# 5. API servisleri — mevcut endpoint çağrıları
cat frontend/src/services/api.js
cat frontend/src/services/factoryApi.js

# 6. Hook'lar — state management
cat frontend/src/hooks/useAnalysis.js
cat frontend/src/hooks/useCompressorTypes.js

# 7. Sidebar — navigation
cat frontend/src/components/layout/Sidebar.jsx

# 8. Factory modal — ekipman ekleme
cat frontend/src/components/factory/AddEquipmentModal.jsx

# 9. Backend'den dönen config — 3 yeni ekipman config'leri
python3 -c "
from api.routes.analysis import router
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
for eq in ['heat_exchanger', 'steam_turbine', 'dryer']:
    resp = client.get(f'/api/config/{eq}')
    print(f'=== {eq} config ===')
    if resp.status_code == 200:
        import json
        print(json.dumps(resp.json(), indent=2)[:500])
    else:
        print(f'Status: {resp.status_code}')
    print()
"

# 10. Backend'den dönen types listesi
python3 -c "
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
resp = client.get('/api/types')
import json
print(json.dumps(resp.json(), indent=2))
"
```

**Bu çıktıları incele. Aşağıdaki tüm talimatlar mevcut pattern'a UYUMLU olmalı.**

---

## 📋 Adım 1: Mevcut Pattern'ı Haritalandır

Frontend'in veri akışını çıkar:

```
1. Sidebar.jsx → equipment type seçimi → route: /equipment/:type
2. EquipmentAnalysis.jsx → `GET /api/config/{type}` ile form tanımı alır
3. SubtypeSelector.jsx → alt tip seçimi (config'den gelen subtypes)
4. ParameterForm.jsx → config'den gelen fields'ları render eder
5. useAnalysis.js hook → `POST /api/analyze` çağırır
6. Sonuç component'leri → response'u gösterir (metrikler, sankey, AI)
```

**Her adımda 3 yeni ekipmanın düzgün çalışması lazım.**

---

## 🔧 Adım 2: Backend Config Endpoint'lerini Doğrula

Brief 12'de `api/routes/analysis.py`'ye 3 yeni ekipman için config eklendi. Frontend'in `GET /api/config/{type}` çağrısının doğru sonuç döndüğünden emin ol.

Her config şunları içermeli:
- `equipment_type`: string
- `label`: Türkçe isim
- `subtypes`: array of {id, label} — alt tip seçenekleri
- `fields`: array of {name, label, type, default, min, max, unit, ...}
- `field_groups`: (varsa) parametrelerin gruplanması

**Eğer config eksikse veya yanlışsa, `api/routes/analysis.py`'deki config builder fonksiyonlarını düzelt.**

Beklenen config yapısı (mevcut 4 ekipman pattern'ını referans al):

### Heat Exchanger Config

```
Türkçe Label: "Isı Eşanjörü"
Subtypes:
  - shell_tube: "Gövde-Boru (Shell & Tube)"
  - plate: "Plakalı"
  - finned_tube: "Kanatlı Boru"
  - economizer: "Ekonomizer"
  - air_cooled: "Hava Soğutmalı"
  - double_pipe: "Çift Borulu"
  - spiral: "Spiral"

Field Groups:
  Sıcak Taraf:
    - hot_fluid (select): water, steam, air, flue_gas, thermal_oil, glycol_30, glycol_50
    - hot_inlet_temp_C (number): 90°C default, "Sıcak Giriş Sıcaklığı"
    - hot_outlet_temp_C (number): 70°C default, "Sıcak Çıkış Sıcaklığı"
    - hot_mass_flow_kg_s (number): 2.0 default, "Sıcak Debi (kg/s)"
    - hot_pressure_drop_kPa (number): 10.0 default, "Sıcak Basınç Düşüşü (kPa)"

  Soğuk Taraf:
    - cold_fluid (select): water, steam, air, flue_gas, thermal_oil, glycol_30, glycol_50
    - cold_inlet_temp_C (number): 20°C default, "Soğuk Giriş Sıcaklığı"
    - cold_outlet_temp_C (number): 50°C default, "Soğuk Çıkış Sıcaklığı"
    - cold_mass_flow_kg_s (number): 1.5 default, "Soğuk Debi (kg/s)"
    - cold_pressure_drop_kPa (number): 15.0 default, "Soğuk Basınç Düşüşü (kPa)"

  Operasyonel:
    - operating_hours (number): 6000 default
    - electricity_price_eur_kwh (number): 0.10 default
    - fuel_price_eur_kwh (number): 0.06 default
```

### Steam Turbine Config

```
Türkçe Label: "Buhar Türbini"
Subtypes:
  - backpressure: "Karşı Basınçlı"
  - condensing: "Yoğuşmalı"
  - extraction: "Ara Çekişli"
  - condensing_extraction: "Yoğuşmalı Ara Çekişli"
  - chp_backpressure: "CHP Karşı Basınçlı"

Field Groups:
  Giriş Buharı:
    - inlet_temp_C (number): 400°C, "Giriş Buhar Sıcaklığı"
    - inlet_pressure_bar (number): 40 bar, "Giriş Basıncı"
    - mass_flow_kg_s (number): 5.0, "Buhar Debisi (kg/s)"

  Çıkış Koşulları:
    - outlet_pressure_bar (number): 0.1 bar, "Çıkış Basıncı"
    - outlet_temp_C (number, optional): null, "Çıkış Sıcaklığı (opsiyonel)"

  Türbin Verimleri:
    - isentropic_efficiency (number): 0.80, "İzentropik Verim" (0-1 aralık)
    - mechanical_efficiency (number): 0.98, "Mekanik Verim"
    - generator_efficiency (number): 0.97, "Jeneratör Verimi"

  CHP Parametreleri (is_chp true ise göster):
    - is_chp (checkbox): false, "Kojenerasyon (CHP)"
    - heat_recovery_temp_C (number): null, "Isı Geri Kazanım Sıcaklığı"
    - heat_recovery_fraction (number): 0.60, "Isı Geri Kazanım Oranı"

  Operasyonel:
    - operating_hours (number): 7000
    - electricity_price_eur_kwh (number): 0.10
    - fuel_price_eur_kwh (number): 0.04
```

### Dryer Config

```
Türkçe Label: "Kurutma Fırını"
Subtypes:
  - conveyor: "Konveyörlü"
  - rotary: "Döner Tambur"
  - spray: "Spreyli"
  - fluidized_bed: "Akışkan Yataklı"
  - tray: "Raflı (Tepsili)"
  - drum: "Tambur"
  - infrared: "Kızılötesi"
  - microwave: "Mikrodalga"

Field Groups:
  Ürün Parametreleri:
    - product_mass_flow_kg_h (number): 1000, "Ürün Debisi (kg/h)"
    - moisture_in_pct (number): 60, "Giriş Nem (%, yaş baz)" (0-99)
    - moisture_out_pct (number): 10, "Çıkış Nem (%, yaş baz)" (0-99)
    - product_inlet_temp_C (number): 25, "Ürün Giriş Sıcaklığı"
    - product_outlet_temp_C (number): 60, "Ürün Çıkış Sıcaklığı"

  Isıtma Parametreleri:
    - heat_source (select): natural_gas, steam, electrical, hot_air → "Isı Kaynağı"
    - supply_temp_C (number): 200, "Besleme Sıcaklığı"
    - heat_input_kW (number, optional): null, "Isı Girişi (kW)" — boşsa otomatik
    - fuel_efficiency (number): 0.85, "Yakıt Verimi"

  Hava Parametreleri:
    - air_inlet_temp_C (number): 25, "Hava Giriş Sıcaklığı"
    - air_outlet_temp_C (number): 80, "Hava Çıkış Sıcaklığı"

  Ortam:
    - ambient_temp_C (number): 25
    - ambient_humidity_pct (number): 50, "Ortam Nemi (%)"

  Operasyonel:
    - operating_hours (number): 5000
    - electricity_price_eur_kwh (number): 0.10
    - fuel_price_eur_kwh (number): 0.05
```

---

## 🔧 Adım 3: Sidebar Navigation Güncelleme

`frontend/src/components/layout/Sidebar.jsx` dosyasında mevcut 4 ekipman link'i var. 3 yeni ekipman ekle:

```
Mevcut:
  🔧 Kompresör       → /equipment/compressor
  🔥 Kazan           → /equipment/boiler
  ❄️ Chiller          → /equipment/chiller
  💧 Pompa           → /equipment/pump

Ekle:
  🔄 Isı Eşanjörü    → /equipment/heat_exchanger
  ⚡ Buhar Türbini   → /equipment/steam_turbine
  🌡️ Kurutma Fırını  → /equipment/dryer
```

Mevcut Sidebar'ın icon sistemi ne ise (lucide-react veya emoji) aynı pattern'ı kullan. lucide-react icon önerileri:
- Heat Exchanger: `ArrowLeftRight` veya `Repeat`
- Steam Turbine: `Zap` veya `Gauge`
- Dryer: `Wind` veya `Thermometer`

---

## 🔧 Adım 4: EquipmentAnalysis.jsx — Genel Kontrol

Bu sayfa muhtemelen `useParams()` ile equipment type alıp, config'e göre form render ediyor. Eğer yapı generic ise (config-driven), yeni ekipmanlar otomatik çalışmalı.

**Kontrol et:**
1. Route `/equipment/:type` pattern'ı 3 yeni type'ı kabul ediyor mu?
2. `GET /api/config/{type}` çağrısı doğru sonuç dönüyor mu?
3. Form render'ı config-driven mi yoksa type-specific component'ler mi var?

**Eğer type-specific logic varsa** (if/switch ile compressor/boiler/chiller/pump ayrımı), 3 yeni ekipmanı da ekle.

---

## 🔧 Adım 5: SubtypeSelector Güncellemesi

`SubtypeSelector.jsx` muhtemelen config'den gelen subtypes array'ini render eder. Eğer generic ise, yeni ekipmanlar otomatik çalışır.

**Kontrol et:** Selector'ın subtypes render ettiği yerde hardcoded type-specific logic var mı?

---

## 🔧 Adım 6: ParameterForm Güncellemesi

Mevcut `ParameterForm.jsx`'in config'den gelen field'ları nasıl render ettiğini incele. Muhtemel yapı:
- Her field bir `FormField` component'i
- `type: "number"` → number input
- `type: "select"` → dropdown
- `type: "checkbox"` → toggle/checkbox

**Yeni ihtiyaçlar:**

1. **Select field tipi:** Heat exchanger'da `hot_fluid`, `cold_fluid` ve dryer'da `heat_source` select field. Mevcut form'da select field desteği yoksa ekle.

2. **Conditional fields:** Steam turbine'de `is_chp: true` olduğunda CHP alanları gösterilmeli. Dryer'da `heat_source` seçimine göre farklı alanlar gösterilebilir.

3. **Field grupları:** 3 yeni ekipman çok parametreli. Gruplar halinde gösterim düşün:
   - Heat Exchanger: "Sıcak Taraf" / "Soğuk Taraf" / "Operasyonel"
   - Steam Turbine: "Giriş Buharı" / "Çıkış" / "Verimler" / "CHP"
   - Dryer: "Ürün" / "Isıtma" / "Hava" / "Ortam"

---

## 🔧 Adım 7: Sonuç Gösterimi — Yeni Metrikler

Mevcut result panel standart metrikleri gösterir: exergy_in, exergy_out, exergy_destroyed, efficiency, annual_loss vb.

**3 yeni ekipman ek metrikler döndürüyor.** Bunları da göster:

### Heat Exchanger Ek Metrikleri
| Backend field | Türkçe Label | Birim |
|---|---|---|
| `lmtd_K` | LMTD | K |
| `effectiveness_pct` | Isıl Etkinlik | % |
| `bejan_number` | Bejan Sayısı | - |
| `entropy_gen_heat_transfer` | Entropi Üretimi (ΔT) | kW/K |
| `entropy_gen_pressure_drop` | Entropi Üretimi (ΔP) | kW/K |
| `ntu` | NTU | - |
| `heat_duty_kW` | Isı Yükü | kW |
| `fouling_indicator` | Fouling İndikatör | - |

### Steam Turbine Ek Metrikleri
| Backend field | Türkçe Label | Birim |
|---|---|---|
| `power_output_kW` | Güç Çıkışı | kW |
| `isentropic_efficiency_pct` | İzentropik Verim | % |
| `exhaust_exergy_kW` | Egzoz Exergy | kW |
| `heat_rate_kJ_kWh` | Heat Rate | kJ/kWh |
| `is_chp` | CHP Modu | bool |
| `chp_heat_output_kW` | CHP Isı Çıkışı | kW |
| `chp_total_efficiency_pct` | CHP Toplam Verim | % |
| `chp_power_heat_ratio` | Güç/Isı Oranı | - |
| `chp_exergy_pct` | CHP Exergy Verimi | % |

### Dryer Ek Metrikleri
| Backend field | Türkçe Label | Birim |
|---|---|---|
| `water_removed_kg_h` | Su Uzaklaştırma | kg/h |
| `specific_energy_kJ_kg_water` | Spesifik Enerji | kJ/kg-su |
| `thermal_efficiency_pct` | Termal Verim (1. Yasa) | % |
| `exhaust_exergy_kW` | Egzoz Exergy | kW |
| `exhaust_recovery_potential_kW` | Geri Kazanım Potansiyeli | kW |
| `heat_input_kW` | Isı Girişi | kW |
| `evaporation_exergy_kW` | Buharlaşma Exergy | kW |

**Yaklaşım:** Mevcut ResultsPanel (veya eşdeğeri) muhtemelen standart metrikleri gösteriyor. Ek metrikler için:
- Equipment-type bazlı ek metrik kartları ekle
- Veya mevcut panel'e conditional rendering ekle
- Standart metrikleri (efficiency, exergy_in/out/destroyed, annual_loss) zaten gösterecek
- Ek metrikleri "Detay" veya "Ekipman Özel Metrikleri" bölümünde göster

---

## 🔧 Adım 8: Sankey Diyagramı

Mevcut Sankey component'i muhtemelen backend'den gelen `sankey_data` (nodes + links) ile plotly render eder. 3 yeni ekipman aynı format'ta sankey data dönüyor, dolayısıyla mevcut component çalışmalı.

**Kontrol et:**
1. Sankey component'i node/link yapısını generic olarak render ediyor mu?
2. Renk şeması veya layout hardcoded mı?
3. Yeni ekipman node'ları (Türkçe isimlerle) doğru gösteriliyor mu?

Sankey node yapısı (Brief 12'de implement edildi):
```json
{
  "nodes": [
    {"id": 0, "name": "Yakıt Exergy", "name_en": "Fuel Exergy"},
    {"id": 1, "name": "Faydalı Çıkış", "name_en": "Useful Output"},
    ...
  ],
  "links": [
    {"source": 0, "target": 1, "value": 150.5},
    ...
  ],
  "title": "Kurutma Fırını Exergy Akışı",
  "summary": {"exergy_in": ..., "exergy_out": ..., ...}
}
```

---

## 🔧 Adım 9: Factory (Fabrika) Entegrasyonu

### AddEquipmentModal.jsx

Bu modal'da fabrika projesine ekipman eklerken tip seçimi yapılır. Mevcut 4 ekipman varsa, 3 yeni ekipmanı da ekle.

**Kontrol et:** Modal'ın equipment type listesi nereden geliyor?
- Backend'den `GET /api/types` ile mi?
- Yoksa hardcoded mi?

Eğer backend'den geliyorsa, 7/7 ekipman otomatik görünmeli (registry'de hepsi `engine_ready: true`).

### FactoryWizard.jsx

Fabrika oluşturma sihirbazında ekipman ekleme adımı var. Aynı kontrol burada da geçerli.

### FactoryDashboard.jsx

Fabrika analiz sonuçlarında 3 yeni ekipman sonuçları da gösterilmeli. Dashboard muhtemelen ekipman sonuçlarını döngüyle render eder — generic ise otomatik çalışır.

---

## 🔧 Adım 10: API Service Güncellemesi

`frontend/src/services/api.js` dosyasında endpoint çağrıları var. Yeni ekipmanlar aynı endpoint'leri kullanıyorsa ek iş gerekmez:

```
POST /api/analyze        ← equipment_type + params (tüm tipler aynı endpoint)
GET  /api/config/{type}  ← form field tanımları
GET  /api/types          ← equipment type listesi
POST /api/interpret      ← AI yorumlama
GET  /api/benchmarks/{type}/{subtype} ← benchmark verileri
GET  /api/solutions/{type} ← çözüm önerileri
```

**Kontrol et:** api.js'de type-specific endpoint çağrısı var mı? Varsa 3 yeni tip için de ekle.

---

## 🔧 Adım 11: Hook Güncellemesi

### useAnalysis.js

Bu hook muhtemelen generic. Kontrol et:
- `analyzeEquipment(type, params)` generic mi?
- Type-specific preprocessing var mı?

### useCompressorTypes.js

Bu dosya adı compressor-specific görünüyor. İçeriğini incele:
- Sadece compressor'a özel mi?
- Yoksa generic `useEquipmentTypes.js` olarak refactor edilebilir mi?

Eğer sadece compressor subtypes'ı yönetiyorsa ve diğer ekipmanlar SubtypeSelector + config pattern'ı ile çalışıyorsa, dokunmana gerek yok.

---

## 📋 Türkçe Label Referansı

```javascript
const EQUIPMENT_LABELS = {
  compressor: 'Kompresör',
  boiler: 'Kazan',
  chiller: 'Chiller',
  pump: 'Pompa',
  heat_exchanger: 'Isı Eşanjörü',
  steam_turbine: 'Buhar Türbini',
  dryer: 'Kurutma Fırını',
};

const EQUIPMENT_ICONS = {
  // lucide-react icons
  compressor: 'Settings',        // veya mevcut icon ne ise
  boiler: 'Flame',
  chiller: 'Snowflake',
  pump: 'Droplets',
  heat_exchanger: 'ArrowLeftRight',
  steam_turbine: 'Zap',
  dryer: 'Wind',
};

// Akışkan seçenekleri (Heat Exchanger select fields)
const FLUID_OPTIONS = [
  { value: 'water', label: 'Su' },
  { value: 'steam', label: 'Buhar' },
  { value: 'air', label: 'Hava' },
  { value: 'flue_gas', label: 'Baca Gazı' },
  { value: 'thermal_oil', label: 'Termal Yağ' },
  { value: 'glycol_30', label: 'Glikol %30' },
  { value: 'glycol_50', label: 'Glikol %50' },
];

// Isı kaynağı seçenekleri (Dryer select field)
const HEAT_SOURCE_OPTIONS = [
  { value: 'natural_gas', label: 'Doğalgaz' },
  { value: 'steam', label: 'Buhar' },
  { value: 'electrical', label: 'Elektrik' },
  { value: 'hot_air', label: 'Sıcak Hava' },
];

// Subtype Türkçe label'ları
const SUBTYPE_LABELS = {
  // Heat Exchanger
  shell_tube: 'Gövde-Boru (Shell & Tube)',
  plate: 'Plakalı',
  finned_tube: 'Kanatlı Boru',
  economizer: 'Ekonomizer',
  air_cooled: 'Hava Soğutmalı',
  double_pipe: 'Çift Borulu',
  spiral: 'Spiral',

  // Steam Turbine
  backpressure: 'Karşı Basınçlı',
  condensing: 'Yoğuşmalı',
  extraction: 'Ara Çekişli',
  condensing_extraction: 'Yoğuşmalı Ara Çekişli',
  chp_backpressure: 'CHP Karşı Basınçlı',

  // Dryer
  conveyor: 'Konveyörlü',
  rotary: 'Döner Tambur',
  spray: 'Spreyli',
  fluidized_bed: 'Akışkan Yataklı',
  tray: 'Raflı (Tepsili)',
  drum: 'Tambur',
  infrared: 'Kızılötesi',
  microwave: 'Mikrodalga',
};
```

---

## 📋 Test Stratejisi

Frontend testi yoksa (ve muhtemelen yok), en azından şunları yap:

### Manuel Doğrulama Listesi

```bash
# 1. Dev server çalıştır
cd frontend && npm run dev &
cd .. && uvicorn api.main:app --reload --port 8000 &

# 2. Her yeni ekipman için doğrula:
#    a. Sidebar'da görünüyor mu?
#    b. Sayfaya tıklayınca form yükleniyor mu?
#    c. Alt tip seçimi çalışıyor mu?
#    d. Default değerler doğru mu?
#    e. Analiz çalıştırınca sonuç dönüyor mu?
#    f. Sankey diyagramı render ediliyor mu?
#    g. AI yorumlama butonu çalışıyor mu?
#    h. Benchmark bilgisi gösteriliyor mu?

# 3. Regression: Mevcut 4 ekipman hâlâ çalışıyor mu?
# 4. Factory: Yeni ekipmanlar fabrikaya eklenebiliyor mu?
```

### Backend Regression

```bash
# Brief 12 testleri hâlâ geçiyor olmalı
pytest tests/ -v
# Beklenti: 307 test, 0 fail
```

### API Smoke Test

```bash
# Heat Exchanger
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "equipment_type": "heat_exchanger",
    "subtype": "shell_tube",
    "params": {
      "hot_fluid": "water",
      "hot_inlet_temp_C": 90,
      "hot_outlet_temp_C": 70,
      "hot_mass_flow_kg_s": 2.0,
      "cold_fluid": "water",
      "cold_inlet_temp_C": 20,
      "cold_outlet_temp_C": 50,
      "cold_mass_flow_kg_s": 1.5
    }
  }' | python3 -m json.tool | head -30

# Steam Turbine
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "equipment_type": "steam_turbine",
    "subtype": "backpressure",
    "params": {
      "inlet_temp_C": 400,
      "inlet_pressure_bar": 40,
      "mass_flow_kg_s": 5.0,
      "outlet_pressure_bar": 3.0,
      "isentropic_efficiency": 0.80
    }
  }' | python3 -m json.tool | head -30

# Dryer
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "equipment_type": "dryer",
    "subtype": "conveyor",
    "params": {
      "product_mass_flow_kg_h": 1000,
      "moisture_in_pct": 60,
      "moisture_out_pct": 10,
      "heat_source": "natural_gas",
      "supply_temp_C": 200
    }
  }' | python3 -m json.tool | head -30
```

---

## ⚠️ Dikkat Edilecekler

1. **Config-driven frontend ise işin büyük kısmı backend config'de.**
   Eğer frontend config'den gelen field'ları dinamik render ediyorsa, backend config doğru tanımlandıysa form otomatik çalışır. Bu durumda frontend değişiklikleri minimal olur (sadece sidebar + icon + ek metrik gösterimi).

2. **Hardcoded frontend ise her yerde 3 tip ekle.**
   Eğer frontend'de compressor/boiler/chiller/pump if/switch block'ları varsa, her birine heat_exchanger/steam_turbine/dryer ekle.

3. **Select field desteği olmalı.**
   Heat exchanger fluid seçimi ve dryer heat_source seçimi dropdown gerektirir. Mevcut FormField component'inde select tipi yoksa ekle.

4. **Conditional field rendering.**
   Steam turbine is_chp checkbox'ı işaretlendiğinde CHP alanları gösterilmeli. Bu tür conditional logic FormField/ParameterForm seviyesinde handle edilmeli.

5. **Responsive tasarım.**
   Heat exchanger formu çok alan içeriyor (sıcak/soğuk taraf). Mobile'da scroll etmek yerine collapsible section veya tab kullan.

6. **Number formatting.**
   Bejan sayısı 0-1 aralığında, LMTD Kelvin cinsinde, water_removed kg/h. Doğru birim ve precision göster.

---

## ✅ Tamamlanma Kriterleri

- [ ] Sidebar'da 7 ekipman görünüyor ve tıklanabiliyor
- [ ] Heat Exchanger: form → subtype → analiz → sonuç → sankey → AI çalışıyor
- [ ] Steam Turbine: form → subtype → analiz → sonuç → sankey → AI çalışıyor
- [ ] Dryer: form → subtype → analiz → sonuç → sankey → AI çalışıyor
- [ ] Ek metrikler (Bejan, LMTD, water_removed, CHP vb.) gösteriliyor
- [ ] Select field'lar (fluid, heat_source) düzgün çalışıyor
- [ ] CHP conditional fields çalışıyor (steam turbine)
- [ ] Mevcut 4 ekipman hâlâ sorunsuz çalışıyor (regression yok)
- [ ] Factory'ye 3 yeni ekipman eklenebiliyor
- [ ] Backend 307 test hâlâ geçiyor
- [ ] Commit ve push yapıldı

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Sidebar ekipman sayısı | 4 | 7 |
| UI'dan analiz edilebilir ekipman | 4/7 | 7/7 |
| Frontend component/page | ~31 JSX | ~31-35 JSX |
| Fabrikaya eklenebilir ekipman | 4 | 7 |
| Backend test (değişmemeli) | 307 | 307 |
