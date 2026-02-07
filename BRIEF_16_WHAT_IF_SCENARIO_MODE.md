# Brief 16: What-If Senaryo Modu — Canlı Parametre Karşılaştırma

> **Claude Code için:** Bu brief'i oku ve uygula. Mevcut analiz altyapısını yeniden kullanarak senaryo karşılaştırma özelliği ekle. Yeni engine hesaplaması YOK — mevcut analyze fonksiyonlarını iki farklı input seti ile çağır ve delta hesapla.

---

## 🎯 Hedef

Kullanıcı bir ekipman analizi yaptıktan sonra **"Ya şöyle olsaydı?"** sorusunu cevaplayabilmek:
- "Verimliliği %70'ten %85'e çıkarsak ne olur?"
- "Baca gazı sıcaklığını 250°C'den 130°C'ye düşürsek ne kazanırız?"
- "VSD takarsak throttle kaybı sıfırlanır mı?"

**Demo etkisi:** Müşteri toplantısında parametreyi kaydırıp anlık olarak "yılda €12,400 tasarruf" göstermek.

**Kapsam:** Tek ekipman What-If karşılaştırma. Factory-level comparison gelecek brief.

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut EquipmentAnalysis.jsx ve ParameterForm.jsx sayfalarını önce oku
3. Mevcut API endpoint pattern'larını anla
4. useAnalysis.js hook'unun nasıl çalıştığını incele
5. 401 testi BOZMA
6. Mevcut UI akışını bozma — What-If ek özellik, mevcut tek analiz akışı aynen kalmalı

---

## 📋 Adım 0: Mevcut Kodu Anla (KRİTİK)

```bash
# 1. EquipmentAnalysis sayfası — form submit → sonuç akışı
cat frontend/src/pages/EquipmentAnalysis.jsx

# 2. ParameterForm component — form alanları, submit handler
cat frontend/src/components/forms/ParameterForm.jsx

# 3. useAnalysis hook — API çağrı mekanizması
cat frontend/src/hooks/useAnalysis.js

# 4. ResultsPanel — sonuç gösterimi
cat frontend/src/components/results/ResultsPanel.jsx

# 5. API analyze endpoint
cat api/routes/analysis.py | head -80

# 6. API request schema
cat api/schemas/requests.py

# 7. API response schema
cat api/schemas/responses.py

# 8. api.js service
cat frontend/src/services/api.js
```

---

## 🧩 Mimari Tasarım

### Yaklaşım: Frontend-Driven + Backend Compare Endpoint

```
Kullanıcı Akışı:

1. Normal analiz yap → Sonuçları gör (mevcut akış, DEĞİŞMEZ)
2. "What-If Modu" butonuna tıkla
3. Parametreleri değiştir (slider/input)
4. "Karşılaştır" butonuna tıkla
5. POST /api/compare → baseline + senaryo sonuçları + delta
6. Karşılaştırma paneli: delta highlights, radar overlay, tasarruf hesabı
```

### Neden Backend Compare Endpoint?

- Tek API çağrısı ile iki analiz + delta hesaplama
- Annual savings / payback hesabı backend'de daha doğru
- Frontend sadece render eder — hesaplama karmaşıklığı backend'de kalır
- İleriye dönük: senaryo kaydetme, PDF'e ekleme kolay

---

## 📦 Adım 1: Backend — Compare Endpoint

### 1.1 `engine/compare.py` — Delta Hesaplama Modülü

```python
"""
ExergyLab - What-If Scenario Comparison Engine

İki analiz sonucunu karşılaştırır ve delta metrikleri hesaplar.
"""

from typing import Dict, Optional, Tuple


def compute_comparison(baseline_dict: dict, scenario_dict: dict,
                       energy_price_eur_kwh: float = 0.10,
                       operating_hours: int = 6000) -> dict:
    """
    İki analiz sonucunu karşılaştır ve delta hesapla.

    Args:
        baseline_dict: Mevcut durum to_api_dict() çıktısı
        scenario_dict: Senaryo to_api_dict() çıktısı
        energy_price_eur_kwh: Birim enerji fiyatı
        operating_hours: Yıllık çalışma saati

    Returns:
        {
            'delta': {metric: scenario - baseline for each metric},
            'delta_pct': {metric: percentage change},
            'savings': {
                'exergy_saved_kW': float,
                'annual_savings_kWh': float,
                'annual_savings_EUR': float,
                'efficiency_improvement_pct': float,
                'avoidable_reduction_kW': float,
            },
            'improved_metrics': ['metric1', 'metric2', ...],
            'degraded_metrics': ['metric3', ...],
            'summary_tr': str,   # Türkçe özet
        }
    """

    # Delta hesaplama — önemli metrikler
    COMPARE_METRICS = [
        'exergy_efficiency_pct',
        'exergy_in_kW',
        'exergy_out_kW',
        'exergy_destroyed_kW',
        'exergy_destroyed_avoidable_kW',
        'exergy_destroyed_unavoidable_kW',
        'avoidable_ratio_pct',
        'annual_loss_kWh',
        'annual_loss_EUR',
    ]

    delta = {}
    delta_pct = {}
    improved = []
    degraded = []

    for metric in COMPARE_METRICS:
        base_val = baseline_dict.get(metric, 0) or 0
        scen_val = scenario_dict.get(metric, 0) or 0
        d = scen_val - base_val
        delta[metric] = round(d, 2)

        if base_val != 0:
            delta_pct[metric] = round((d / abs(base_val)) * 100, 1)
        else:
            delta_pct[metric] = 0.0

        # İyileşme/kötüleşme tespiti
        # Efficiency UP = iyi, Destruction DOWN = iyi
        if metric in ('exergy_efficiency_pct', 'exergy_out_kW'):
            if d > 0.1:
                improved.append(metric)
            elif d < -0.1:
                degraded.append(metric)
        else:  # destruction, loss metrics — DOWN = iyi
            if d < -0.1:
                improved.append(metric)
            elif d > 0.1:
                degraded.append(metric)

    # Tasarruf hesabı
    exergy_saved = max(
        (baseline_dict.get('exergy_destroyed_kW', 0) or 0) -
        (scenario_dict.get('exergy_destroyed_kW', 0) or 0),
        0
    )
    annual_savings_kWh = exergy_saved * operating_hours
    annual_savings_EUR = annual_savings_kWh * energy_price_eur_kwh

    eff_base = baseline_dict.get('exergy_efficiency_pct', 0) or 0
    eff_scen = scenario_dict.get('exergy_efficiency_pct', 0) or 0
    eff_improvement = eff_scen - eff_base

    av_base = baseline_dict.get('exergy_destroyed_avoidable_kW', 0) or 0
    av_scen = scenario_dict.get('exergy_destroyed_avoidable_kW', 0) or 0
    av_reduction = max(av_base - av_scen, 0)

    savings = {
        'exergy_saved_kW': round(exergy_saved, 2),
        'annual_savings_kWh': round(annual_savings_kWh, 0),
        'annual_savings_EUR': round(annual_savings_EUR, 0),
        'efficiency_improvement_pct': round(eff_improvement, 1),
        'avoidable_reduction_kW': round(av_reduction, 2),
    }

    # Türkçe özet
    if exergy_saved > 0:
        summary = (
            f"Senaryo ile exergy verimi %{eff_base:.1f} → %{eff_scen:.1f} "
            f"(+{eff_improvement:.1f} puan). "
            f"Yıllık {annual_savings_kWh:,.0f} kWh / €{annual_savings_EUR:,.0f} tasarruf potansiyeli."
        )
    else:
        summary = "Senaryo mevcut durumdan daha kötü performans gösteriyor."

    return {
        'delta': delta,
        'delta_pct': delta_pct,
        'savings': savings,
        'improved_metrics': improved,
        'degraded_metrics': degraded,
        'summary_tr': summary,
    }
```

### 1.2 API Route — `api/routes/analysis.py` yeni endpoint

Mevcut `analysis.py` dosyasına yeni endpoint ekle:

```python
@router.post("/compare")
async def compare_scenarios(request: CompareRequest):
    """
    Baseline vs Scenario karşılaştırma.
    Aynı ekipman tipini iki farklı parametre seti ile analiz eder.
    """
    # 1. Baseline analiz
    baseline_result = _run_analysis(
        request.equipment_type, request.subtype, request.baseline_params
    )

    # 2. Scenario analiz
    scenario_result = _run_analysis(
        request.equipment_type, request.subtype, request.scenario_params
    )

    # 3. Delta hesaplama
    comparison = compute_comparison(
        baseline_result.to_api_dict(),
        scenario_result.to_api_dict(),
        energy_price_eur_kwh=getattr(request.baseline_params, 'energy_price_eur_kwh', 0.10),
        operating_hours=getattr(request.baseline_params, 'operating_hours', 6000),
    )

    # 4. Radar
    baseline_radar = generate_radar_data(baseline_result.to_api_dict())
    scenario_radar = generate_radar_data(scenario_result.to_api_dict())

    return CompareResponse(
        baseline=_build_analysis_response(baseline_result, request),
        scenario=_build_analysis_response(scenario_result, request),
        comparison=comparison,
        baseline_radar=baseline_radar,
        scenario_radar=scenario_radar,
    )
```

**DİKKAT:** Mevcut `_analyze_compressor()`, `_analyze_boiler()` vb. fonksiyonlar tek ekipman için yazılmış. Compare endpoint'i bunları tekrar kullanmalı. İki yaklaşım:

**Yaklaşım A (Önerilen):** Mevcut analyze handler'lardan ortak hesaplama mantığını bir helper'a çıkar:

```python
def _run_analysis(equipment_type: str, subtype: str, params: dict) -> ExergyResult:
    """Ortak analiz runner — hem /analyze hem /compare tarafından kullanılır"""
    # Mevcut route handler'larındaki validasyon + engine çağrısı burada
```

**Yaklaşım B:** Compare endpoint'i frontend'den iki ayrı `/api/analyze` çağrısı yaparak sonuçları birleştirir (bu durumda backend'e compare endpoint eklemeye gerek yok — ama delta hesabı frontend'de yapılır, daha karmaşık).

**Mevcut koda bak — _analyze_compressor() vb. fonksiyonların ortak pattern'ını gör ve en uygun refactor'ı yap.**

### 1.3 API Schemas

#### `api/schemas/requests.py` — CompareRequest

```python
class CompareRequest(BaseModel):
    equipment_type: str
    subtype: Optional[str] = None
    baseline_params: dict   # Mevcut durum parametreleri
    scenario_params: dict   # Senaryo parametreleri
```

#### `api/schemas/responses.py` — CompareResponse

```python
class ComparisonSavings(BaseModel):
    exergy_saved_kW: float = 0
    annual_savings_kWh: float = 0
    annual_savings_EUR: float = 0
    efficiency_improvement_pct: float = 0
    avoidable_reduction_kW: float = 0

class ComparisonData(BaseModel):
    delta: Dict[str, float] = {}
    delta_pct: Dict[str, float] = {}
    savings: ComparisonSavings = ComparisonSavings()
    improved_metrics: List[str] = []
    degraded_metrics: List[str] = []
    summary_tr: str = ""

class CompareResponse(BaseModel):
    baseline: AnalysisResponse
    scenario: AnalysisResponse
    comparison: ComparisonData
```

---

## 📦 Adım 2: Frontend — What-If Mode Toggle

### 2.1 Mimari Karar

Mevcut `EquipmentAnalysis.jsx` sayfasının akışı:
1. Ekipman tipi seç → config/form alanları yükle → parametreleri gir → "Analiz Et"
2. Sonuçlar gösterilir (ResultsPanel)

What-If modu bu akışa eklenir:
1. Normal analiz yap → sonuçlar gör (MEVCUT)
2. **"What-If Modu" butonu görünür** (YENİ)
3. Butona tıkla → **Senaryo paneli açılır** (parametreler baseline değerlerle dolu)
4. Parametreleri değiştir → **"Karşılaştır"** butonu
5. `/api/compare` çağrılır
6. **Karşılaştırma görünümü** (delta highlights + radar overlay)
7. **"Normal Moda Dön"** butonu ile kapatılır

### 2.2 State Yönetimi

```jsx
// EquipmentAnalysis.jsx'e eklenecek state:
const [whatIfMode, setWhatIfMode] = useState(false);
const [baselineParams, setBaselineParams] = useState(null);
const [baselineResult, setBaselineResult] = useState(null);
const [scenarioParams, setScenarioParams] = useState(null);
const [compareResult, setCompareResult] = useState(null);
const [isComparing, setIsComparing] = useState(false);
```

### 2.3 Flow

```
Normal Analiz:
  onSubmit(params) → analyzeEquipment(params) → setResult(data)
  → setBaselineParams(params)  // What-If için sakla
  → setBaselineResult(data)

What-If Toggle:
  setWhatIfMode(true) → setScenarioParams({...baselineParams})  // Kopyala

Senaryo Değiştir:
  Slider/input → setScenarioParams({...scenarioParams, [field]: newValue})

Karşılaştır:
  onCompare() → POST /api/compare → setCompareResult(data)

Normal Moda Dön:
  setWhatIfMode(false) → setCompareResult(null)
```

---

## 📦 Adım 3: Frontend — Senaryo Parametre Editörü

### 3.1 `ScenarioEditor.jsx` Component

Bu component, mevcut `ParameterForm`'un basitleştirilmiş versiyonu:
- Mevcut parametreleri gösterir (baseline değerler)
- Kullanıcı sadece değiştirmek istediği parametreleri ayarlar
- **Range slider + sayısal input** birlikte çalışır

```jsx
// frontend/src/components/whatif/ScenarioEditor.jsx

export default function ScenarioEditor({
  config,           // Equipment config (fields, subtypes)
  baselineParams,   // Orijinal parametreler
  scenarioParams,   // Senaryo parametreleri (editable)
  onParamChange,    // (fieldName, newValue) => void
  onCompare,        // () => void — Karşılaştır butonu
  onCancel,         // () => void — Kapat
  isLoading,        // Boolean — API çağrısı devam ediyor mu
}) {
  return (
    <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-sm font-semibold text-amber-800 flex items-center gap-2">
          <span>🔬</span> What-If Senaryo Modu
        </h3>
        <button onClick={onCancel} className="text-gray-400 hover:text-gray-600">
          ✕
        </button>
      </div>

      <p className="text-xs text-amber-700 mb-4">
        Parametreleri değiştirin ve "Karşılaştır" butonuna tıklayın.
        Değişiklikler sarı ile vurgulanır.
      </p>

      {/* Her parametre için slider + input */}
      <div className="space-y-3">
        {config.fields
          .filter(field => field.type === 'number')
          .map(field => {
            const baseVal = baselineParams[field.name];
            const scenVal = scenarioParams[field.name];
            const isChanged = baseVal !== scenVal;

            return (
              <div key={field.name}
                   className={`p-2 rounded ${isChanged ? 'bg-amber-100 border border-amber-300' : ''}`}>
                <div className="flex justify-between text-xs mb-1">
                  <label className="font-medium text-gray-700">
                    {field.label}
                    {field.unit && <span className="text-gray-400 ml-1">({field.unit})</span>}
                  </label>
                  {isChanged && (
                    <span className="text-amber-600 font-medium">
                      {baseVal} → {scenVal}
                    </span>
                  )}
                </div>

                <div className="flex items-center gap-3">
                  {/* Range slider */}
                  <input
                    type="range"
                    min={field.min || 0}
                    max={field.max || baseVal * 3}
                    step={field.step || (baseVal > 10 ? 1 : 0.01)}
                    value={scenVal || 0}
                    onChange={(e) => onParamChange(field.name, parseFloat(e.target.value))}
                    className="flex-1"
                  />
                  {/* Number input */}
                  <input
                    type="number"
                    value={scenVal || ''}
                    onChange={(e) => onParamChange(field.name, parseFloat(e.target.value) || 0)}
                    className="w-24 px-2 py-1 text-sm border rounded"
                    step={field.step || 'any'}
                  />
                </div>
              </div>
            );
          })}
      </div>

      {/* Butonlar */}
      <div className="flex gap-3 mt-4">
        <button
          onClick={onCompare}
          disabled={isLoading}
          className="flex-1 bg-amber-600 text-white py-2 px-4 rounded-lg hover:bg-amber-700 disabled:opacity-50 text-sm font-medium"
        >
          {isLoading ? 'Karşılaştırılıyor...' : '🔍 Karşılaştır'}
        </button>
        <button
          onClick={() => {
            // Baseline'a geri dön
            Object.keys(baselineParams).forEach(key => {
              onParamChange(key, baselineParams[key]);
            });
          }}
          className="px-4 py-2 border border-gray-300 rounded-lg text-sm text-gray-600 hover:bg-gray-50"
        >
          Sıfırla
        </button>
      </div>
    </div>
  );
}
```

**NOT:** Bu JSX referans. Mevcut ParameterForm ve FormField component'larının pattern'ına uyarla. Slider min/max değerleri config'den alınabilir veya baseline değerine göre hesaplanabilir.

---

## 📦 Adım 4: Frontend — Karşılaştırma Paneli

### 4.1 `ComparisonPanel.jsx` Component

Karşılaştırma sonuçlarını gösteren ana panel:

```jsx
// frontend/src/components/whatif/ComparisonPanel.jsx

export default function ComparisonPanel({ compareResult }) {
  if (!compareResult) return null;

  const { baseline, scenario, comparison } = compareResult;
  const { delta, delta_pct, savings, improved_metrics, degraded_metrics, summary_tr } = comparison;

  return (
    <div className="space-y-4">
      {/* Özet Kartı */}
      <div className={`rounded-lg p-4 border ${
        savings.exergy_saved_kW > 0
          ? 'bg-green-50 border-green-200'
          : 'bg-red-50 border-red-200'
      }`}>
        <h3 className="text-sm font-semibold mb-2">
          {savings.exergy_saved_kW > 0 ? '✅ Senaryo İyileşme Gösteriyor' : '⚠️ Senaryo Kötüleşme Gösteriyor'}
        </h3>
        <p className="text-sm text-gray-700">{summary_tr}</p>

        {savings.exergy_saved_kW > 0 && (
          <div className="grid grid-cols-3 gap-4 mt-3">
            <div className="text-center">
              <div className="text-lg font-bold text-green-700">
                {savings.exergy_saved_kW.toFixed(1)} kW
              </div>
              <div className="text-xs text-gray-500">Exergy Tasarruf</div>
            </div>
            <div className="text-center">
              <div className="text-lg font-bold text-green-700">
                {savings.annual_savings_kWh.toLocaleString()} kWh
              </div>
              <div className="text-xs text-gray-500">Yıllık Tasarruf</div>
            </div>
            <div className="text-center">
              <div className="text-lg font-bold text-green-700">
                €{savings.annual_savings_EUR.toLocaleString()}
              </div>
              <div className="text-xs text-gray-500">Yıllık Maliyet Tasarrufu</div>
            </div>
          </div>
        )}
      </div>

      {/* Delta Metrik Tablosu */}
      <div className="bg-white rounded-lg border border-gray-200 p-4">
        <h3 className="text-sm font-semibold text-gray-700 mb-3">Metrik Karşılaştırma</h3>
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left text-xs text-gray-500 border-b">
              <th className="pb-2">Metrik</th>
              <th className="pb-2 text-right">Mevcut</th>
              <th className="pb-2 text-right">Senaryo</th>
              <th className="pb-2 text-right">Δ</th>
            </tr>
          </thead>
          <tbody>
            {/* Key metrics */}
            {[
              { key: 'exergy_efficiency_pct', label: 'Exergy Verimi (%)', upIsGood: true },
              { key: 'exergy_destroyed_kW', label: 'Exergy Yıkımı (kW)', upIsGood: false },
              { key: 'exergy_destroyed_avoidable_kW', label: 'Kaçınılabilir Yıkım (kW)', upIsGood: false },
              { key: 'avoidable_ratio_pct', label: 'Kaçınılabilir Oran (%)', upIsGood: false },
              { key: 'annual_loss_EUR', label: 'Yıllık Kayıp (€)', upIsGood: false },
            ].map(({ key, label, upIsGood }) => {
              const baseVal = baseline.metrics?.[key] ?? delta[key] ?? 0;
              const scenVal = scenario.metrics?.[key] ?? 0;
              const d = delta[key] || 0;
              const isImproved = upIsGood ? d > 0.1 : d < -0.1;
              const isDegraded = upIsGood ? d < -0.1 : d > 0.1;

              return (
                <tr key={key} className="border-b border-gray-50">
                  <td className="py-2">{label}</td>
                  <td className="py-2 text-right font-mono">{typeof baseVal === 'number' ? baseVal.toFixed(1) : baseVal}</td>
                  <td className="py-2 text-right font-mono">{typeof scenVal === 'number' ? scenVal.toFixed(1) : scenVal}</td>
                  <td className={`py-2 text-right font-mono font-medium ${
                    isImproved ? 'text-green-600' : isDegraded ? 'text-red-600' : 'text-gray-400'
                  }`}>
                    {d > 0 ? '+' : ''}{d.toFixed(1)}
                    {delta_pct[key] ? ` (${delta_pct[key] > 0 ? '+' : ''}${delta_pct[key]}%)` : ''}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* Radar Overlay — Baseline (outline) + Scenario (filled) */}
      <RadarComparison
        baselineRadar={compareResult.baseline.radar_data}
        scenarioRadar={compareResult.scenario.radar_data}
      />
    </div>
  );
}
```

### 4.2 `RadarComparison.jsx` — Radar Overlay

İki radar'ı üst üste çiz: baseline dashed outline + scenario filled.

```jsx
// frontend/src/components/whatif/RadarComparison.jsx

import Plot from 'react-plotly.js';

export default function RadarComparison({ baselineRadar, scenarioRadar }) {
  if (!baselineRadar?.scores || !scenarioRadar?.scores) return null;

  const axes = ['exergy_efficiency', 'improvement_status', 'sector_ranking',
                'heat_recovery', 'destruction_ratio', 'cost_efficiency'];
  const labels = ['Exergy Verimi', 'Optimizasyon', 'Sektör Sıralaması',
                  'Isı Geri Kazanım', 'Exergy Koruma', 'Maliyet Etkinliği'];

  const baseValues = axes.map(a => baselineRadar.scores[a] || 0);
  const scenValues = axes.map(a => scenarioRadar.scores[a] || 0);

  // Kapatmak için ilk noktayı tekrar ekle
  const theta = [...labels, labels[0]];

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-4">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-sm font-semibold text-gray-700">Radar Karşılaştırma</h3>
        <div className="flex gap-3 text-xs">
          <span className="flex items-center gap-1">
            <span className="w-3 h-0.5 bg-gray-400 inline-block" style={{borderTop: '2px dashed #9ca3af'}}></span>
            Mevcut ({baselineRadar.overall_score})
          </span>
          <span className="flex items-center gap-1">
            <span className="w-3 h-1 bg-blue-500 inline-block rounded"></span>
            Senaryo ({scenarioRadar.overall_score})
          </span>
        </div>
      </div>

      <Plot
        data={[
          // Baseline — dashed outline
          {
            type: 'scatterpolar',
            r: [...baseValues, baseValues[0]],
            theta: theta,
            fill: 'none',
            line: { color: '#9ca3af', width: 2, dash: 'dash' },
            marker: { size: 4, color: '#9ca3af' },
            name: 'Mevcut',
          },
          // Scenario — filled
          {
            type: 'scatterpolar',
            r: [...scenValues, scenValues[0]],
            theta: theta,
            fill: 'toself',
            fillcolor: 'rgba(59, 130, 246, 0.15)',
            line: { color: '#3b82f6', width: 2 },
            marker: { size: 6, color: '#3b82f6' },
            name: 'Senaryo',
          },
        ]}
        layout={{
          polar: {
            radialaxis: { visible: true, range: [0, 100], tickfont: { size: 10 } },
            angularaxis: { tickfont: { size: 11 } },
          },
          showlegend: false,
          margin: { t: 20, b: 20, l: 60, r: 60 },
          height: 300,
          paper_bgcolor: 'transparent',
          plot_bgcolor: 'transparent',
        }}
        config={{ displayModeBar: false, responsive: true }}
        style={{ width: '100%' }}
      />
    </div>
  );
}
```

---

## 📦 Adım 5: Frontend — EquipmentAnalysis Entegrasyonu

### 5.1 Sayfa Akışı Güncelleme

`EquipmentAnalysis.jsx`'in güncellenmesi:

```jsx
// State eklemeleri
const [whatIfMode, setWhatIfMode] = useState(false);
const [baselineParams, setBaselineParams] = useState(null);
const [scenarioParams, setScenarioParams] = useState(null);
const [compareResult, setCompareResult] = useState(null);
const [isComparing, setIsComparing] = useState(false);

// Mevcut onSubmit — baseline'ı sakla
const handleAnalyze = async (params) => {
  const result = await analyzeEquipment(...);
  setResult(result);
  setBaselineParams(params);          // What-If için sakla
  setWhatIfMode(false);               // Reset
  setCompareResult(null);
};

// What-If butonuna basınca
const handleWhatIfToggle = () => {
  setWhatIfMode(true);
  setScenarioParams({ ...baselineParams });  // Baseline parametreleri kopyala
  setCompareResult(null);
};

// Karşılaştır
const handleCompare = async () => {
  setIsComparing(true);
  try {
    const resp = await api.compareScenarios({
      equipment_type: selectedType,
      subtype: selectedSubtype,
      baseline_params: baselineParams,
      scenario_params: scenarioParams,
    });
    setCompareResult(resp);
  } catch (err) {
    console.error('Compare error:', err);
  } finally {
    setIsComparing(false);
  }
};

// Render'da:
// 1. Normal sonuçlar gösterilir (mevcut ResultsPanel)
// 2. Sonuçların altında "What-If Modu" butonu
// 3. What-If mode açıksa ScenarioEditor + ComparisonPanel gösterilir
```

### 5.2 Sayfa Layout

```
┌─────────────────────────────────────────────┐
│ Ekipman Tipi Seçimi + Alt Tip               │
├─────────────────────────────────────────────┤
│ Parametre Formu          │ Sonuçlar          │
│ (Mevcut ParameterForm)   │ (Mevcut Results)  │
│                          │                   │
│ [Analiz Et]              │ MetricsCards      │
│                          │ AV/UN Bar         │
│                          │ Radar Chart       │
│                          │ Sankey            │
│                          │ AI Interpretation │
│                          │                   │
│                          │ ┌───────────────┐ │
│                          │ │ [🔬 What-If]  │ │  ← Butonu
│                          │ └───────────────┘ │
├──────────────────────────┴───────────────────┤
│ (What-If mode açıksa)                        │
│ ┌──────────────────────────────────────────┐ │
│ │ ScenarioEditor (sarı arka plan)          │ │
│ │ Parametreler + Slider'lar                │ │
│ │ [Karşılaştır] [Sıfırla] [✕ Kapat]      │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌──────────────────────────────────────────┐ │
│ │ ComparisonPanel (sonuçlar açıksa)        │ │
│ │ ✅ Senaryo İyileşme Gösteriyor           │ │
│ │ 12.3 kW tasarruf │ 73,800 kWh │ €7,380  │ │
│ │                                          │ │
│ │ Metrik Karşılaştırma Tablosu             │ │
│ │ Mevcut → Senaryo → Delta                 │ │
│ │                                          │ │
│ │ Radar Overlay (baseline vs scenario)     │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

---

## 📦 Adım 6: API Service

### 6.1 `frontend/src/services/api.js`

```javascript
// Yeni fonksiyon ekle:
export async function compareScenarios({ equipment_type, subtype, baseline_params, scenario_params }) {
  const response = await axios.post(`${API_BASE}/api/compare`, {
    equipment_type,
    subtype,
    baseline_params,
    scenario_params,
  });
  return response.data;
}
```

---

## 📦 Adım 7: Testler

### 7.1 `tests/test_compare.py` — Backend Testleri

```python
"""What-If Scenario Comparison testleri"""
import pytest
from engine.compare import compute_comparison


class TestComputeComparison:

    def test_basic_improvement(self):
        """Senaryo daha iyi → pozitif tasarruf"""
        baseline = {'exergy_efficiency_pct': 50, 'exergy_destroyed_kW': 50,
                     'exergy_in_kW': 100, 'exergy_out_kW': 50,
                     'exergy_destroyed_avoidable_kW': 30, 'avoidable_ratio_pct': 60,
                     'annual_loss_kWh': 300000, 'annual_loss_EUR': 30000,
                     'exergy_destroyed_unavoidable_kW': 20}
        scenario = {'exergy_efficiency_pct': 70, 'exergy_destroyed_kW': 30,
                     'exergy_in_kW': 100, 'exergy_out_kW': 70,
                     'exergy_destroyed_avoidable_kW': 10, 'avoidable_ratio_pct': 33,
                     'annual_loss_kWh': 180000, 'annual_loss_EUR': 18000,
                     'exergy_destroyed_unavoidable_kW': 20}

        result = compute_comparison(baseline, scenario)
        assert result['savings']['exergy_saved_kW'] == 20.0
        assert result['savings']['annual_savings_EUR'] > 0
        assert result['savings']['efficiency_improvement_pct'] == 20.0
        assert 'exergy_efficiency_pct' in result['improved_metrics']

    def test_degradation(self):
        """Senaryo daha kötü → negatif değişim"""
        baseline = {'exergy_efficiency_pct': 70, 'exergy_destroyed_kW': 30,
                     'exergy_in_kW': 100}
        scenario = {'exergy_efficiency_pct': 50, 'exergy_destroyed_kW': 50,
                     'exergy_in_kW': 100}

        result = compute_comparison(baseline, scenario)
        assert result['savings']['exergy_saved_kW'] == 0  # max(0, ...)
        assert 'exergy_efficiency_pct' in result['degraded_metrics']

    def test_no_change(self):
        """Aynı parametreler → sıfır delta"""
        same = {'exergy_efficiency_pct': 60, 'exergy_destroyed_kW': 40,
                'exergy_in_kW': 100}
        result = compute_comparison(same, same)
        assert result['savings']['exergy_saved_kW'] == 0
        assert len(result['improved_metrics']) == 0
        assert len(result['degraded_metrics']) == 0

    def test_empty_dicts(self):
        """Boş input'larla crash olmamalı"""
        result = compute_comparison({}, {})
        assert 'savings' in result
        assert 'delta' in result

    def test_delta_pct_calculation(self):
        """Yüzde değişim doğru hesaplanmalı"""
        baseline = {'exergy_efficiency_pct': 50, 'exergy_destroyed_kW': 50, 'exergy_in_kW': 100}
        scenario = {'exergy_efficiency_pct': 75, 'exergy_destroyed_kW': 25, 'exergy_in_kW': 100}
        result = compute_comparison(baseline, scenario)
        assert result['delta_pct']['exergy_efficiency_pct'] == 50.0  # (75-50)/50 * 100
        assert result['delta_pct']['exergy_destroyed_kW'] == -50.0   # (25-50)/50 * 100

    def test_summary_tr(self):
        """Türkçe özet üretilmeli"""
        baseline = {'exergy_efficiency_pct': 50, 'exergy_destroyed_kW': 50, 'exergy_in_kW': 100}
        scenario = {'exergy_efficiency_pct': 70, 'exergy_destroyed_kW': 30, 'exergy_in_kW': 100}
        result = compute_comparison(baseline, scenario)
        assert 'tasarruf' in result['summary_tr'].lower() or 'senaryo' in result['summary_tr'].lower()

    def test_custom_energy_price(self):
        """Farklı enerji fiyatı → farklı tasarruf"""
        baseline = {'exergy_destroyed_kW': 50, 'exergy_in_kW': 100}
        scenario = {'exergy_destroyed_kW': 30, 'exergy_in_kW': 100}
        r1 = compute_comparison(baseline, scenario, energy_price_eur_kwh=0.10)
        r2 = compute_comparison(baseline, scenario, energy_price_eur_kwh=0.20)
        assert r2['savings']['annual_savings_EUR'] == r1['savings']['annual_savings_EUR'] * 2


class TestCompareAPI:
    """API endpoint testleri"""

    def test_compare_compressor(self, client):
        """Kompresör compare endpoint'i"""
        resp = client.post('/api/compare', json={
            'equipment_type': 'compressor',
            'subtype': 'screw',
            'baseline_params': {},
            'scenario_params': {'outlet_temp_C': 120},  # Farklı çıkış sıcaklığı
        })
        assert resp.status_code == 200
        data = resp.json()
        assert 'baseline' in data
        assert 'scenario' in data
        assert 'comparison' in data

    def test_compare_all_equipment(self, client):
        """Tüm ekipman tipleri compare edilebilmeli"""
        for eq_type in ['compressor', 'boiler', 'chiller', 'pump',
                        'heat_exchanger', 'steam_turbine', 'dryer']:
            resp = client.post('/api/compare', json={
                'equipment_type': eq_type,
                'baseline_params': {},
                'scenario_params': {},
            })
            assert resp.status_code == 200, f'{eq_type} compare failed: {resp.status_code}'

    def test_compare_returns_radar(self, client):
        """Compare response'da radar data olmalı"""
        resp = client.post('/api/compare', json={
            'equipment_type': 'compressor',
            'baseline_params': {},
            'scenario_params': {},
        })
        data = resp.json()
        assert data['baseline'].get('radar_data') is not None
        assert data['scenario'].get('radar_data') is not None

    def test_compare_invalid_type(self, client):
        """Geçersiz ekipman tipi → 400/422"""
        resp = client.post('/api/compare', json={
            'equipment_type': 'invalid_type',
            'baseline_params': {},
            'scenario_params': {},
        })
        assert resp.status_code in (400, 422)
```

**DİKKAT:** Test client fixture'ı (`client`) mevcut `conftest.py`'de tanımlı mı kontrol et. Yoksa ekle.

---

## 📋 Entegrasyon Doğrulama

```bash
# 1. Compare engine çalışıyor
python3 -c "
from engine.compare import compute_comparison
baseline = {'exergy_efficiency_pct': 50, 'exergy_destroyed_kW': 50, 'exergy_in_kW': 100}
scenario = {'exergy_efficiency_pct': 70, 'exergy_destroyed_kW': 30, 'exergy_in_kW': 100}
result = compute_comparison(baseline, scenario)
print(f'Savings: {result[\"savings\"][\"exergy_saved_kW\"]} kW')
print(f'Annual: €{result[\"savings\"][\"annual_savings_EUR\"]:,.0f}')
print(f'Efficiency: +{result[\"savings\"][\"efficiency_improvement_pct\"]}%')
print(f'Summary: {result[\"summary_tr\"]}')
"

# 2. Compare API endpoint
python3 -c "
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
resp = client.post('/api/compare', json={
    'equipment_type': 'compressor',
    'subtype': 'screw',
    'baseline_params': {},
    'scenario_params': {'outlet_temp_C': 120},
})
assert resp.status_code == 200, f'Error: {resp.json()}'
data = resp.json()
comp = data['comparison']
print(f'Baseline eff: {data[\"baseline\"][\"metrics\"][\"exergy_efficiency_pct\"]:.1f}%')
print(f'Scenario eff: {data[\"scenario\"][\"metrics\"][\"exergy_efficiency_pct\"]:.1f}%')
print(f'Delta eff: {comp[\"delta\"][\"exergy_efficiency_pct\"]:+.1f}%')
print(f'Annual savings: €{comp[\"savings\"][\"annual_savings_EUR\"]:,.0f}')
"

# 3. Tüm ekipman tipleri
python3 -c "
from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
for eq in ['compressor', 'boiler', 'chiller', 'pump', 'heat_exchanger', 'steam_turbine', 'dryer']:
    resp = client.post('/api/compare', json={
        'equipment_type': eq,
        'baseline_params': {},
        'scenario_params': {},
    })
    status = '✅' if resp.status_code == 200 else '❌'
    print(f'{status} {eq}: {resp.status_code}')
"

# 4. Frontend build
cd frontend && npx vite build 2>&1 | tail -5

# 5. Tüm testler
cd .. && pytest tests/ -v | tail -20
```

---

## ⚠️ Dikkat Edilecekler

1. **Mevcut analiz akışını BOZMA.** What-If mode opsiyonel — mevcut "Analiz Et" butonu ve sonuç gösterimi aynen kalmalı.

2. **Compare endpoint'i mevcut analyze handler'ları yeniden kullanmalı.** Copy-paste yerine ortak helper fonksiyon çıkar. Mevcut handler'ların validasyon, subtype routing, Pydantic parse mantığını incele.

3. **Slider min/max değerleri.** Config endpoint'inden gelen field tanımlarında min/max varsa kullan. Yoksa baseline değerinin ×0.5 ile ×2 aralığını kullan.

4. **Empty scenario_params.** Kullanıcı hiçbir parametreyi değiştirmezse compare, aynı sonuçları dönecek (delta=0). Bu kabul edilebilir.

5. **Loading state.** Compare API çağrısı iki analiz + delta hesabı = mevcut analyze'dan ~2× yavaş olabilir. Loading spinner göster.

6. **Mobile responsive.** ComparisonPanel'deki 3'lü grid mobile'da 1 kolona düşmeli.

---

## ✅ Tamamlanma Kriterleri

- [ ] `engine/compare.py` oluşturuldu — `compute_comparison()` çalışıyor
- [ ] `engine/__init__.py` güncellendi — compare export
- [ ] `/api/compare` endpoint oluşturuldu ve çalışıyor
- [ ] `api/schemas/requests.py` — CompareRequest schema eklendi
- [ ] `api/schemas/responses.py` — CompareResponse schema eklendi
- [ ] 7 ekipman tipi compare edilebiliyor
- [ ] `frontend/src/components/whatif/ScenarioEditor.jsx` oluşturuldu
- [ ] `frontend/src/components/whatif/ComparisonPanel.jsx` oluşturuldu
- [ ] `frontend/src/components/whatif/RadarComparison.jsx` oluşturuldu
- [ ] `EquipmentAnalysis.jsx` What-If mode entegrasyonu tamamlandı
- [ ] `api.js` — `compareScenarios()` fonksiyonu eklendi
- [ ] Mevcut 401 test hâlâ geçiyor
- [ ] Yeni testler (~12) geçiyor
- [ ] Frontend build başarılı
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| What-If karşılaştırma | Yok | 7/7 ekipman |
| Compare API | Yok | `/api/compare` endpoint |
| Radar overlay | Tek radar | Baseline vs Scenario overlay |
| Delta gösterimi | Yok | Yeşil/kırmızı delta tablosu |
| Tasarruf hesabı | Yok | kW / kWh / EUR hesabı |
| Test sayısı | 401 | ~413+ |
