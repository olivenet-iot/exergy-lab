# Brief 19: Factory Dashboard Overhaul — Fabrika Enerji Konsol

> **Claude Code için:** Bu brief'i oku ve uygula. FactoryDashboard sayfasını basit liste görünümünden profesyonel bir "fabrika enerji yönetim konsolu"na dönüştür. Equipment priority grid + integration opportunities + factory-level metrics.

---

## 🎯 Hedef

Mevcut FactoryDashboard: ekipman listesi + toplam sayılar + basit Sankey. Danışmanlık toplantısında gösterilebilir seviyede değil.

**Yeni layout:** Fabrika müdürüne "€85,000/yıl masada bırakıyorsunuz" diyebileceğin profesyonel konsol. İyileştirme önceliği, cross-equipment fırsatları, toplam potansiyel — hepsi tek ekranda.

**Design direction:** Brief 18 ile uyumlu — Plus Jakarta Sans, JetBrains Mono, cyan accent, dark sidebar (opsiyonel), industrial precision aesthetic.

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut factory engine ve API'ye DOKUNMA — sadece frontend değişikliği
3. 431 testi BOZMA
4. Yeni npm paketi EKLEME
5. Frontend build başarılı olmalı

---

## 📋 Adım 0: Mevcut Durumu Anla (KRİTİK)

```bash
# 1. Factory Dashboard — mevcut sayfa
cat frontend/src/pages/FactoryDashboard.jsx

# 2. Factory List — fabrika listesi
cat frontend/src/pages/FactoryList.jsx

# 3. Factory Wizard — fabrika oluşturma
cat frontend/src/pages/FactoryWizard.jsx

# 4. Factory components
ls frontend/src/components/factory/
cat frontend/src/components/factory/EquipmentInventory.jsx
cat frontend/src/components/factory/AddEquipmentModal.jsx
cat frontend/src/components/factory/FactoryMetrics.jsx 2>/dev/null || echo "Not found"

# 5. Factory API — ne veri dönüyor?
cat api/routes/factory.py

# 6. Factory engine — ne hesaplıyor?
cat engine/factory.py | head -100

# 7. Factory service frontend
cat frontend/src/services/factoryApi.js

# 8. Mevcut result components (Brief 18'den)
ls frontend/src/components/dashboard/
ls frontend/src/components/results/

# 9. App.jsx — routing
cat frontend/src/App.jsx

# 10. Radar engine — factory-level radar için kullanılabilir
cat engine/radar.py
```

---

## 🗺️ Factory API Response Yapısı

`POST /api/factory/{id}/analyze` dönen data:

```json
{
  "factory_id": "...",
  "factory_name": "...",
  "sector": "food",
  "total_equipment": 5,
  "analyzed_count": 5,
  "failed_count": 0,
  
  "aggregates": {
    "total_exergy_input_kW": 245.6,
    "total_exergy_output_kW": 142.3,
    "total_exergy_destroyed_kW": 103.3,
    "total_efficiency_percent": 57.9,
    "total_annual_loss_kWh": 825440,
    "total_annual_cost_EUR": 82544
  },
  
  "hotspots": [
    {
      "equipment_id": "eq_1",
      "equipment_name": "Ana Kompresör",
      "equipment_type": "compressor",
      "priority": "high",
      "efficiency_percent": 42.3,
      "destruction_kW": 35.2,
      "destruction_share_percent": 34.1,
      "annual_loss_EUR": 28160
    },
    // ... more hotspots (sorted by priority)
  ],
  
  "integration_opportunities": [
    {
      "id": "int_1",
      "source": "Ana Kompresör",
      "target": "Kazan Besleme",
      "type": "compressor_to_boiler_feedwater",
      "potential_savings_kW": 12.5,
      "potential_annual_savings_EUR": 10000,
      "complexity": "medium",
      "description": "Kompresör atık ısısı kazan besleme suyu ön ısıtmasında kullanılabilir"
    },
    // ... more opportunities
  ],
  
  "equipment_results": [
    {
      "equipment_id": "eq_1",
      "equipment_name": "Ana Kompresör",
      "equipment_type": "compressor",
      "subtype": "screw",
      "status": "success",
      "metrics": { ... },  // Full equipment metrics
      "radar_data": { ... },  // Radar chart data
      "sankey_data": { ... },
      "avoidable_unavoidable": { ... }  // AV/UN data
    },
    // ... more equipment
  ],
  
  "sankey_data": { ... },  // Factory-level Sankey
  
  "ai_interpretation": { ... }  // Factory AI analysis (if requested)
}
```

---

## 🏗️ Sayfa Layout Mimarisi

### Ana Yapı

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Header: Fabrika Adı + Sektör Badge + [Analizi Güncelle] + [Ekipman Ekle] │
├──────────────────────────────────────────────────────────────────────────┤
│ Factory MetricBar (6 metrics — always visible)                           │
│ [Toplam Giriş] [Toplam Çıkış] [Toplam Yıkım] [Verim%] [Yıllık €] [Potansiyel €] │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────┐  ┌─────────────────────────────┐│
│  │                                     │  │                             ││
│  │  📊 İyileştirme Öncelik Listesi     │  │  🔗 Entegrasyon Fırsatları  ││
│  │                                     │  │                             ││
│  │  ┌─────────────────────────────┐    │  │  Kompresör → Kazan          ││
│  │  │ 🔴 Ana Kompresör      HIGH  │    │  │  12.5 kW → €10,000/yıl      ││
│  │  │ 42.3% ████░░░░ €28,160     │    │  │  [Detay]                    ││
│  │  └─────────────────────────────┘    │  │                             ││
│  │  ┌─────────────────────────────┐    │  │  Kazan → Chiller            ││
│  │  │ 🟡 Buhar Kazanı      MED   │    │  │  8.2 kW → €6,560/yıl        ││
│  │  │ 58.1% ██████░░ €18,400     │    │  │  [Detay]                    ││
│  │  └─────────────────────────────┘    │  │                             ││
│  │  ┌─────────────────────────────┐    │  │  Toplam Potansiyel:         ││
│  │  │ 🟢 Soğutma Grubu     LOW   │    │  │  €24,560/yıl                ││
│  │  │ 71.2% ████████░ €8,960     │    │  │                             ││
│  │  └─────────────────────────────┘    │  └─────────────────────────────┘│
│  │                                     │                                 │
│  └─────────────────────────────────────┘                                 │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                                                                     │ │
│  │  Factory Sankey Diagram (full width)                                │ │
│  │                                                                     │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  🤖 AI Fabrika Analizi                                               │ │
│  │                                                                     │ │
│  │  "Bu fabrikada toplam 103 kW exergy yıkımı tespit edilmiştir.       │ │
│  │   En kritik ekipman Ana Kompresör olup, toplam yıkımın %34'ünü      │ │
│  │   oluşturmaktadır. Kompresör atık ısısının kazan besleme suyunda    │ │
│  │   kullanılması ile yılda €10,000 tasarruf sağlanabilir..."          │ │
│  │                                                                     │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Yeni Component'lar

### Dosya 1: `frontend/src/components/factory/FactoryMetricBar.jsx`

Factory-level MetricBar — 6 compact metrics.

```jsx
/**
 * FactoryMetricBar — Factory summary metrics strip
 * 
 * Props:
 *   aggregates: object — factory aggregates from API
 *   integrationPotential: number — total €/year from integration opportunities
 */
export default function FactoryMetricBar({ aggregates, integrationPotential }) {
  // 6 metric cards yan yana (flex, gap-3, overflow-x-auto on mobile)
  // 
  // 1. TOPLAM GİRİŞ: total_exergy_input_kW → "245.6 kW"
  // 2. TOPLAM ÇIKIŞ: total_exergy_output_kW → "142.3 kW"
  // 3. TOPLAM YIKIM: total_exergy_destroyed_kW → "103.3 kW" (always red)
  // 4. FABRİKA VERİMİ: total_efficiency_percent → "57.9%" (color coded)
  // 5. YILLIK KAYIP: total_annual_cost_EUR → "€82,544" (always red)
  // 6. TASARRUF POTANSİYELİ: integrationPotential → "€24,560" (always green, highlight)
  
  // Card #6 özel: green background, larger font — dikkat çekici
  // Styling: Brief 18 MetricBar ile aynı design system
}
```

### Dosya 2: `frontend/src/components/factory/PriorityList.jsx`

Hotspot-based equipment priority list.

```jsx
/**
 * PriorityList — Equipment improvement priority list
 * 
 * Props:
 *   hotspots: array — sorted hotspot data from API
 *   equipmentResults: array — full equipment results (for drill-down)
 *   onEquipmentClick: function(equipmentId) — navigate to equipment detail
 */
export default function PriorityList({ hotspots, equipmentResults, onEquipmentClick }) {
  // Card container: bg-white rounded-lg border shadow-sm
  // Header: "📊 İyileştirme Öncelik Listesi" + badge showing count
  
  // Each equipment row:
  // ┌──────────────────────────────────────────────────────────────┐
  // │ 🔴 [HIGH]  Ana Kompresör (Vidalı Kompresör)                  │
  // │                                                              │
  // │ Verim: 42.3%  ████████░░░░░░░░░░░░  AV: 65% | UN: 35%       │
  // │                                                              │
  // │ Yıkım: 35.2 kW (%34.1)    Yıllık Kayıp: €28,160    [B]      │
  // │                                           radar grade ↑      │
  // └──────────────────────────────────────────────────────────────┘
  
  // Priority badge colors:
  //   HIGH: bg-red-100 text-red-700 border-red-300
  //   MEDIUM: bg-amber-100 text-amber-700 border-amber-300
  //   LOW: bg-green-100 text-green-700 border-green-300
  
  // Efficiency bar: gradient from red (0%) to green (100%)
  //   Current value marker on the bar
  
  // AV/UN mini bar: inline horizontal bar
  //   Avoidable (red portion) | Unavoidable (gray portion)
  //   If no AV/UN data, hide this section
  
  // Radar grade badge: colored circle (A=green, B=cyan, C=amber, D=orange, F=red)
  //   If no radar data, hide
  
  // Click handler: onEquipmentClick(equipment_id)
  //   This could navigate to equipment detail or expand inline
  
  // Sort order: HIGH first, then MEDIUM, then LOW (API already sorted)
  // If no hotspots: "Henüz ekipman analizi yapılmadı"
}
```

**Equipment Row Visual Detail:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  🔴 HIGH   Ana Kompresör                                    [B]     │
│           Vidalı Kompresör                                          │
│                                                                     │
│  Verim ━━━━━━━━━━━━━━━░░░░░░░░░░░░░░ 42.3%                         │
│                                                                     │
│  AV/UN  ████████████░░░░░░░░  65% kaçınılabilir                    │
│                                                                     │
│  💀 35.2 kW (%34.1 pay)      💰 €28,160/yıl                        │
│                                                                     │
│  [Detaylı Analiz →]                                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Dosya 3: `frontend/src/components/factory/IntegrationPanel.jsx`

Cross-equipment integration opportunities.

```jsx
/**
 * IntegrationPanel — Cross-equipment integration opportunities
 * 
 * Props:
 *   opportunities: array — integration_opportunities from API
 *   onOpportunityClick: function(opportunityId) — show detail modal
 */
export default function IntegrationPanel({ opportunities, onOpportunityClick }) {
  // Card container: bg-white rounded-lg border shadow-sm
  // Header: "🔗 Entegrasyon Fırsatları" + total potential badge
  
  // Calculate total potential:
  //   sum of all opportunity.potential_annual_savings_EUR
  
  // Each opportunity card:
  // ┌────────────────────────────────────────┐
  // │ 🔄 Kompresör → Kazan Besleme           │
  // │                                        │
  // │ Potansiyel: 12.5 kW                    │
  // │ Tasarruf: €10,000/yıl                  │
  // │                                        │
  // │ Karmaşıklık: 🟡 Orta                   │
  // │                                        │
  // │ [Detay]                                │
  // └────────────────────────────────────────┘
  
  // Complexity badges:
  //   low: 🟢 Düşük (bg-green-100)
  //   medium: 🟡 Orta (bg-amber-100)
  //   high: 🔴 Yüksek (bg-red-100)
  
  // Connection icon based on type:
  //   compressor_to_boiler_feedwater: 🔄
  //   compressor_to_space_heating: 🏠
  //   boiler_flue_to_absorption: 💨
  //   chiller_condenser_to_hotwater: 🚿
  //   pump_vsd_retrofit: ⚡
  
  // Total summary at bottom:
  // ┌────────────────────────────────────────┐
  // │ TOPLAM POTANSİYEL                      │
  // │ €24,560/yıl                            │
  // │ (3 fırsat)                             │
  // └────────────────────────────────────────┘
  
  // If no opportunities: "Entegrasyon fırsatı tespit edilmedi"
}
```

### Dosya 4: `frontend/src/components/factory/FactorySankey.jsx`

Factory-level Sankey diagram wrapper.

```jsx
/**
 * FactorySankey — Factory Sankey diagram with equipment breakdown
 * 
 * Props:
 *   sankeyData: object — factory sankey_data from API
 *   aggregates: object — for summary display
 */
export default function FactorySankey({ sankeyData, aggregates }) {
  // Card container with header: "🔄 Fabrika Exergy Akışı"
  
  // Uses existing SankeyDiagram component internally
  // But with factory-specific node coloring:
  //   - Input nodes: blue shades
  //   - Equipment nodes: equipment type colors
  //   - Output nodes: green shades
  //   - Loss nodes: red/orange shades
  
  // Below Sankey: quick stats
  //   "Toplam Giriş: 245.6 kW → Faydalı Çıkış: 142.3 kW (57.9%) → Kayıp: 103.3 kW"
  
  // If no sankeyData: placeholder message
}
```

### Dosya 5: `frontend/src/components/factory/FactoryAIPanel.jsx`

Factory-level AI interpretation panel.

```jsx
/**
 * FactoryAIPanel — Factory AI analysis display
 * 
 * Props:
 *   interpretation: object — ai_interpretation from API
 *   loading: boolean — AI loading state
 *   onRequestAI: function — trigger AI analysis
 */
export default function FactoryAIPanel({ interpretation, loading, onRequestAI }) {
  // Card container with header: "🤖 AI Fabrika Analizi"
  
  // If loading: spinner + "AI analizi hazırlanıyor..."
  
  // If no interpretation and not loading:
  //   [AI Analizi İste] button → calls onRequestAI
  
  // If interpretation exists:
  //   Render interpretation content (similar to AIInterpretation component)
  //   Sections: executive_summary, findings, recommendations, etc.
  
  // Uses similar Markdown rendering as AIInterpretation
}
```

### Dosya 6: `frontend/src/components/factory/FactoryHeader.jsx`

Factory page header with actions.

```jsx
/**
 * FactoryHeader — Factory name, sector, and action buttons
 * 
 * Props:
 *   factory: object — factory info (name, sector)
 *   onRefreshAnalysis: function — re-run all equipment analyses
 *   onAddEquipment: function — open add equipment modal
 *   isAnalyzing: boolean — analysis in progress
 */
export default function FactoryHeader({ factory, onRefreshAnalysis, onAddEquipment, isAnalyzing }) {
  // Layout: flex justify-between items-center
  
  // Left side:
  //   Factory name (text-2xl font-bold)
  //   Sector badge (bg-slate-100 text-slate-700 px-3 py-1 rounded-full)
  //   Equipment count (text-sm text-slate-500)
  
  // Right side:
  //   [+ Ekipman Ekle] button (outline style)
  //   [🔄 Analizi Güncelle] button (primary style, loading state)
  
  // Sector labels (Turkish):
  //   food: "Gıda", cement: "Çimento", textile: "Tekstil"
  //   paper: "Kağıt", metal: "Metal", automotive: "Otomotiv"
  //   chemical: "Kimya"
}
```

---

## 📦 Ana Sayfa Restructure

### Dosya 7: `frontend/src/pages/FactoryDashboard.jsx` — MAJOR REWRITE

Mevcut dosya tamamen yeniden yazılıyor.

**Mevcut yapı (basit):**
- Factory bilgisi + equipment listesi
- Basit metrik gösterimi
- Sankey (varsa)

**Yeni yapı (dashboard):**

```jsx
import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import FactoryHeader from '../components/factory/FactoryHeader';
import FactoryMetricBar from '../components/factory/FactoryMetricBar';
import PriorityList from '../components/factory/PriorityList';
import IntegrationPanel from '../components/factory/IntegrationPanel';
import FactorySankey from '../components/factory/FactorySankey';
import FactoryAIPanel from '../components/factory/FactoryAIPanel';
import AddEquipmentModal from '../components/factory/AddEquipmentModal';
import { getFactory, analyzeFactory, getFactoryInterpretation } from '../services/factoryApi';

export default function FactoryDashboard() {
  const { id } = useParams();
  const navigate = useNavigate();
  
  // State
  const [factory, setFactory] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [analyzing, setAnalyzing] = useState(false);
  const [aiLoading, setAiLoading] = useState(false);
  const [showAddModal, setShowAddModal] = useState(false);
  const [error, setError] = useState(null);
  
  // Load factory data
  useEffect(() => {
    loadFactory();
  }, [id]);
  
  const loadFactory = async () => {
    setLoading(true);
    try {
      const data = await getFactory(id);
      setFactory(data);
      if (data.equipment?.length > 0) {
        await runAnalysis();
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  const runAnalysis = async () => {
    setAnalyzing(true);
    try {
      const result = await analyzeFactory(id);
      setAnalysisResult(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setAnalyzing(false);
    }
  };
  
  const requestAI = async () => {
    setAiLoading(true);
    try {
      const interpretation = await getFactoryInterpretation(id, analysisResult);
      setAnalysisResult(prev => ({ ...prev, ai_interpretation: interpretation }));
    } catch (err) {
      console.error('AI failed:', err);
    } finally {
      setAiLoading(false);
    }
  };
  
  const handleEquipmentClick = (equipmentId) => {
    // Navigate to equipment detail or show modal
    // For now: navigate to equipment analysis page with pre-filled data
    const equipment = analysisResult?.equipment_results?.find(e => e.equipment_id === equipmentId);
    if (equipment) {
      navigate(`/equipment/${equipment.equipment_type}`, { 
        state: { prefill: equipment } 
      });
    }
  };
  
  const handleEquipmentAdded = () => {
    setShowAddModal(false);
    loadFactory();
  };
  
  // Calculate integration potential
  const integrationPotential = analysisResult?.integration_opportunities?.reduce(
    (sum, opp) => sum + (opp.potential_annual_savings_EUR || 0), 0
  ) || 0;
  
  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage message={error} />;
  if (!factory) return <NotFound />;
  
  const hasAnalysis = !!analysisResult?.aggregates;
  const hasEquipment = factory.equipment?.length > 0;
  
  return (
    <div className="space-y-6">
      {/* Header */}
      <FactoryHeader
        factory={factory}
        onRefreshAnalysis={runAnalysis}
        onAddEquipment={() => setShowAddModal(true)}
        isAnalyzing={analyzing}
      />
      
      {!hasEquipment ? (
        /* Empty state */
        <EmptyState onAddEquipment={() => setShowAddModal(true)} />
      ) : !hasAnalysis ? (
        /* No analysis yet */
        <AnalyzePrompt onAnalyze={runAnalysis} isAnalyzing={analyzing} />
      ) : (
        /* Full dashboard */
        <>
          {/* Metric Bar */}
          <FactoryMetricBar
            aggregates={analysisResult.aggregates}
            integrationPotential={integrationPotential}
          />
          
          {/* Main content: Priority List + Integration Panel */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Priority List - 2/3 width */}
            <div className="lg:col-span-2">
              <PriorityList
                hotspots={analysisResult.hotspots}
                equipmentResults={analysisResult.equipment_results}
                onEquipmentClick={handleEquipmentClick}
              />
            </div>
            
            {/* Integration Panel - 1/3 width */}
            <div className="lg:col-span-1">
              <IntegrationPanel
                opportunities={analysisResult.integration_opportunities}
                onOpportunityClick={(id) => console.log('Show opportunity', id)}
              />
            </div>
          </div>
          
          {/* Factory Sankey */}
          <FactorySankey
            sankeyData={analysisResult.sankey_data}
            aggregates={analysisResult.aggregates}
          />
          
          {/* AI Panel */}
          <FactoryAIPanel
            interpretation={analysisResult.ai_interpretation}
            loading={aiLoading}
            onRequestAI={requestAI}
          />
        </>
      )}
      
      {/* Add Equipment Modal */}
      {showAddModal && (
        <AddEquipmentModal
          factoryId={id}
          onClose={() => setShowAddModal(false)}
          onEquipmentAdded={handleEquipmentAdded}
        />
      )}
    </div>
  );
}

// Helper components
function EmptyState({ onAddEquipment }) {
  return (
    <div className="text-center py-16 bg-white rounded-lg border">
      <div className="text-6xl mb-4">🏭</div>
      <h3 className="text-xl font-semibold text-slate-700 mb-2">
        Henüz ekipman eklenmedi
      </h3>
      <p className="text-slate-500 mb-6">
        Fabrika analizi için ekipman eklemeye başlayın
      </p>
      <button
        onClick={onAddEquipment}
        className="px-6 py-3 bg-cyan-600 text-white rounded-lg hover:bg-cyan-700"
      >
        + İlk Ekipmanı Ekle
      </button>
    </div>
  );
}

function AnalyzePrompt({ onAnalyze, isAnalyzing }) {
  return (
    <div className="text-center py-16 bg-white rounded-lg border">
      <div className="text-6xl mb-4">📊</div>
      <h3 className="text-xl font-semibold text-slate-700 mb-2">
        Analiz bekleniyor
      </h3>
      <p className="text-slate-500 mb-6">
        Tüm ekipmanların exergy analizini başlatın
      </p>
      <button
        onClick={onAnalyze}
        disabled={isAnalyzing}
        className="px-6 py-3 bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 disabled:opacity-50"
      >
        {isAnalyzing ? '⏳ Analiz yapılıyor...' : '🔬 Analizi Başlat'}
      </button>
    </div>
  );
}
```

---

## 📦 Factory API Güncellemeleri

### Dosya 8: `frontend/src/services/factoryApi.js` — Ek Fonksiyonlar

Mevcut dosyaya ekleme:

```javascript
// Mevcut fonksiyonlara EK olarak:

/**
 * Get factory AI interpretation
 * POST /api/factory/{id}/interpret
 */
export const getFactoryInterpretation = async (factoryId, analysisResult) => {
  const response = await api.post(`/factory/${factoryId}/interpret`, {
    analysis_result: analysisResult
  });
  return response.data;
};

// NOT: Eğer bu endpoint yoksa, mevcut interpret endpoint'ini kullan
// veya backend'e yeni endpoint eklenmesi gerekiyorsa bunu belirt
```

**KONTROL:** Backend'de `/api/factory/{id}/interpret` endpoint'i var mı? Yoksa mevcut `/api/interpret` endpoint'i factory data ile çağrılabilir mi? Bu durumu keşif aşamasında belirle.

---

## 🎨 Styling Notları

### Design System Uyumu (Brief 18 ile)

```css
/* Aynı font'lar kullanılıyor (index.html'de zaten var) */
font-family: 'Plus Jakarta Sans', system-ui, sans-serif;

/* Sayısal veriler için */
font-family: 'JetBrains Mono', monospace;

/* Accent color */
--primary: #06b6d4; /* cyan-500 */

/* Priority colors */
--priority-high: #ef4444;   /* red-500 */
--priority-medium: #f59e0b; /* amber-500 */
--priority-low: #10b981;    /* emerald-500 */
```

### Responsive Breakpoints

```
Desktop (≥1024px / lg):
  - MetricBar: 6 cards horizontal
  - Priority + Integration: 2/3 + 1/3 grid
  - Sankey: full width

Tablet (768-1023px / md):
  - MetricBar: 2 rows of 3
  - Priority + Integration: stack
  - Sankey: full width

Mobile (<768px):
  - MetricBar: horizontal scroll
  - Everything stacked
  - Cards full width
```

---

## 📋 Uygulama Sırası

### Faz 1: Keşif
1. Mevcut factory pages ve components'ı oku
2. Factory API response yapısını doğrula
3. Mevcut SankeyDiagram component'ın factory data ile nasıl çalıştığını anla
4. Factory AI interpret endpoint'i kontrol et

### Faz 2: Yeni Components
5. `components/factory/FactoryMetricBar.jsx`
6. `components/factory/PriorityList.jsx`
7. `components/factory/IntegrationPanel.jsx`
8. `components/factory/FactorySankey.jsx`
9. `components/factory/FactoryAIPanel.jsx`
10. `components/factory/FactoryHeader.jsx`

### Faz 3: Ana Sayfa
11. `pages/FactoryDashboard.jsx` yeniden yaz
    - Mevcut dosyayı ÖNCE yedekle
    - Yeni component'ları import et
    - State management güncelle
    - Layout uygula

### Faz 4: API (gerekirse)
12. `services/factoryApi.js` güncellemeler
13. Backend'de eksik endpoint varsa not et (bu brief frontend-only olmalı)

### Faz 5: Doğrulama
14. `cd frontend && npx vite build` → 0 error
15. `cd .. && pytest tests/ -v` → 431 test geçmeli
16. Manual test: factory oluştur, ekipman ekle, analiz yap, dashboard'u gör

### Faz 6: Commit
17. `git add -A && git commit -m 'Overhaul factory dashboard with priority grid and integration opportunities panel' && git push`

---

## ⚠️ Edge Cases

| Case | Handling |
|------|----------|
| No equipment | Empty state with "Ekipman Ekle" CTA |
| Equipment but no analysis | "Analizi Başlat" prompt |
| Analysis in progress | Loading overlay, buttons disabled |
| Some equipment failed | Show partial results, mark failed equipment |
| No hotspots (all good) | "Kritik sorun tespit edilmedi" message |
| No integration opportunities | "Entegrasyon fırsatı bulunamadı" message |
| No AI interpretation | "AI Analizi İste" button |
| AI loading | Spinner in AI panel |
| Missing radar_data on equipment | Hide radar grade badge |
| Missing AV/UN data | Hide AV/UN mini bar |

---

## ✅ Tamamlanma Kriterleri

- [ ] FactoryMetricBar: 6 metric, color coded, responsive
- [ ] PriorityList: priority badges, efficiency bar, AV/UN mini bar, clickable
- [ ] IntegrationPanel: opportunity cards, complexity badges, total potential
- [ ] FactorySankey: factory Sankey with wrapper
- [ ] FactoryAIPanel: AI interpretation display with request button
- [ ] FactoryHeader: name, sector badge, action buttons
- [ ] FactoryDashboard: full restructure with all components
- [ ] Empty state handling (no equipment)
- [ ] Analysis prompt (equipment but no analysis)
- [ ] Integration potential calculated and prominently displayed
- [ ] Equipment click navigates or shows detail
- [ ] Responsive layout (desktop/tablet/mobile)
- [ ] Design system consistent with Brief 18
- [ ] Frontend build successful — 0 errors
- [ ] 431 tests still passing
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Dashboard yapısı | Basit liste | Priority-based grid |
| Integration fırsatları | Gizli/görünmez | Prominent panel |
| Tasarruf potansiyeli | Hesaplanmıyor | Büyük rakam (€/yıl) |
| Equipment prioritization | Yok | HIGH/MEDIUM/LOW badges |
| AV/UN visibility | Yok | Mini bars on each equipment |
| AI analysis | Ayrı endpoint? | Integrated panel |
| UX hissi | "MVP" | "Danışmanlık aracı" |
