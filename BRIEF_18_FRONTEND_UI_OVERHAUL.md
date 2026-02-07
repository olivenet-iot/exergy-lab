# Brief 18: Frontend UI Overhaul — Engineering Dashboard

> **Claude Code için:** Bu brief'i oku ve uygula. EquipmentAnalysis sayfasını alt-alta scroll cehennemi'nden profesyonel bir mühendislik dashboard'una dönüştür. Tab sistemi + collapsible sidebar + compact metric bar.

---

## 🎯 Hedef

Mevcut EquipmentAnalysis sayfası: MetricsCards, AvoidableBar, RadarBenchmark, SankeyDiagram, BenchmarkChart, AIInterpretation, What-If butonu/paneli, AI Chat — HEPSİ alt alta dizili. Kullanıcı sonsuza kadar scroll ediyor.

**Yeni layout:** Profesyonel mühendislik dashboard'u. Parametre sidebar'ı + üst metrik bar'ı + 4 tab ile organize edilmiş içerik. Her şey tek ekranda erişilebilir.

**Design direction:** Industrial Precision — temiz, data-yoğun, güven veren. Bloomberg Terminal meets modern SaaS. Flashy değil, precise.

---

## ⚠️ OTONOM YETKİ

1. Brief'teki görevleri tamamla
2. Mevcut component'ların **iç mantığını DEĞİŞTİRME** — sadece layout/wrapper değişiklikleri
3. 431 testi BOZMA (backend hiç değişmiyor)
4. Yeni npm paketi EKLEME
5. Frontend build başarılı olmalı

---

## 📋 Adım 0: Mevcut Durumu Anla (KRİTİK)

```bash
# 1. Ana sayfa — tüm state ve render yapısını anla
cat frontend/src/pages/EquipmentAnalysis.jsx

# 2. ResultsPanel — mevcut sonuç render sırası
cat frontend/src/components/results/ResultsPanel.jsx

# 3. Her result component'ın props'unu anla
cat frontend/src/components/results/MetricsCards.jsx
cat frontend/src/components/results/RadarBenchmark.jsx
cat frontend/src/components/results/AvoidableBar.jsx
cat frontend/src/components/results/SankeyDiagram.jsx
cat frontend/src/components/results/BenchmarkChart.jsx
cat frontend/src/components/results/AIInterpretation.jsx

# 4. What-If component'ları
cat frontend/src/components/whatif/ScenarioEditor.jsx
cat frontend/src/components/whatif/ComparisonPanel.jsx

# 5. Chat
cat frontend/src/components/chat/ChatPanel.jsx

# 6. Mevcut layout
cat frontend/src/components/layout/Layout.jsx
cat frontend/src/components/layout/Header.jsx
cat frontend/src/components/layout/Sidebar.jsx

# 7. Formlar
cat frontend/src/components/forms/ParameterForm.jsx

# 8. Hooks — analiz akışı
cat frontend/src/hooks/useAnalysis.js

# 9. Common components
cat frontend/src/components/common/Card.jsx

# 10. index.html — font ekleme için
cat frontend/index.html

# 11. Tailwind config varsa
cat frontend/tailwind.config.js 2>/dev/null || echo "No tailwind config"

# 12. Mevcut CSS
find frontend/src -name "*.css" | head -10
cat frontend/src/index.css
```

---

## 🎨 Design System

### Renk Paleti

```css
/* CSS Variables — index.css'e ekle veya inline kullan */

/* Primary: Thermodynamic Blue-Cyan */
--primary-50:  #ecfeff;
--primary-100: #cffafe;
--primary-500: #06b6d4;
--primary-600: #0891b2;
--primary-700: #0e7490;

/* Sidebar: Dark Slate */
--sidebar-bg:    #0f172a;   /* slate-900 */
--sidebar-hover:  #1e293b;   /* slate-800 */
--sidebar-text:   #94a3b8;   /* slate-400 */
--sidebar-active: #06b6d4;   /* cyan-500 */

/* Content */
--content-bg:    #f8fafc;   /* slate-50 */
--card-bg:       #ffffff;
--card-border:   #e2e8f0;   /* slate-200 */

/* Status Colors */
--status-good:    #10b981;   /* emerald-500 */
--status-warning: #f59e0b;   /* amber-500 */
--status-bad:     #ef4444;   /* red-500 */

/* Grade Colors */
--grade-A: #10b981;
--grade-B: #06b6d4;
--grade-C: #f59e0b;
--grade-D: #f97316;
--grade-F: #ef4444;
```

### Tipografi

```html
<!-- index.html'e ekle (Google Fonts) -->
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
/* Body text */
font-family: 'Plus Jakarta Sans', system-ui, sans-serif;

/* Sayısal veriler, metrikler */
font-family: 'JetBrains Mono', monospace;
```

---

## 🏗️ Sayfa Layout Mimarisi

### İki Durum

#### Durum 1: Analiz Yapılmamış (result yok)

```
┌──────────────────────────────────────────────┐
│ Header (mevcut)                              │
├──────────────────────────────────────────────┤
│                                              │
│     ┌──────────────────────────────┐         │
│     │                              │         │
│     │   🔧 Ekipman Tipi Seçimi     │         │
│     │   ⚙️ Alt Tip Seçimi          │         │
│     │                              │         │
│     │   ┌────────────────────┐     │         │
│     │   │ Parametre Formu    │     │         │
│     │   │ (Mevcut form)      │     │         │
│     │   │                    │     │         │
│     │   │ [Analiz Et]        │     │         │
│     │   └────────────────────┘     │         │
│     │                              │         │
│     └──────────────────────────────┘         │
│              max-w-2xl centered              │
│                                              │
└──────────────────────────────────────────────┘
```

Temiz, centered, odaklı. Kullanıcı tek şey yapabilir: parametreleri gir ve analiz et.

#### Durum 2: Analiz Tamamlandı (result var)

```
┌──────────────────────────────────────────────────────────────────┐
│ Header (mevcut)                                                  │
├────────────┬─────────────────────────────────────────────────────┤
│            │ ┌─────────────────────────────────────────────────┐ │
│  Parameter │ │ Compact Metric Bar (4-5 metrics, always visible)│ │
│  Sidebar   │ │ [59.1%] [15.1kW] [36.7%] [€4,240] [Grade: B]  │ │
│            │ ├─────────────────────────────────────────────────┤ │
│  280px     │ │ Tabs: [Genel Bakış│Akış Analizi│AI Danışman│   │ │
│  collaps.  │ │        Senaryo]                                 │ │
│            │ │                                                 │ │
│ ┌────────┐ │ │                                                 │ │
│ │Ekipman │ │ │         Active Tab Content                      │ │
│ │Tipi    │ │ │                                                 │ │
│ │Alt Tip │ │ │         (tek ekranda, scroll minimal)           │ │
│ │        │ │ │                                                 │ │
│ │T_in:25 │ │ │                                                 │ │
│ │T_out:85│ │ │                                                 │ │
│ │P: 8bar │ │ │                                                 │ │
│ │...     │ │ │                                                 │ │
│ │        │ │ │                                                 │ │
│ │[Tekrar │ │ │                                                 │ │
│ │ Analiz]│ │ │                                                 │ │
│ │        │ │ │                                                 │ │
│ │[◀Gizle]│ │ └─────────────────────────────────────────────────┘ │
│ └────────┘ │                                                     │
├────────────┴─────────────────────────────────────────────────────┤
```

---

## 📦 Yeni Component'lar

### Dosya 1: `frontend/src/components/dashboard/DashboardLayout.jsx`

Ana wrapper — iki durumu yönetir.

```jsx
/**
 * DashboardLayout — EquipmentAnalysis'ın ana layout wrapper'ı
 * 
 * Props:
 *   hasResult: boolean — sonuç var mı
 *   sidebar: ReactNode — sidebar içeriği (ParameterSidebar)
 *   metricBar: ReactNode — üst metrik bar
 *   children: ReactNode — tab container
 */
export default function DashboardLayout({ hasResult, sidebar, metricBar, children }) {
  // hasResult = false → centered single-column form layout
  // hasResult = true  → sidebar + main content (metric bar + tabs)
}
```

### Dosya 2: `frontend/src/components/dashboard/ParameterSidebar.jsx`

Analiz sonrası sol sidebar — parametre formu + ekipman bilgisi.

```jsx
/**
 * ParameterSidebar — Collapsible parameter sidebar
 * 
 * Props:
 *   equipmentType, subtype: string
 *   children: ReactNode (ParameterForm component)
 *   isCollapsed: boolean
 *   onToggleCollapse: function
 *   onReanalyze: function — "Tekrar Analiz" butonu
 */
export default function ParameterSidebar({
  equipmentType, subtype, children,
  isCollapsed, onToggleCollapse, onReanalyze
}) {
  // Collapsed state: sadece ekipman ikonu + "▶" expand butonu (w-14)
  // Expanded state: full form (w-72 / 288px)
  // Header: Ekipman tipi label + alt tip
  // Body: children (ParameterForm)
  // Footer: [Tekrar Analiz] + [◀ Gizle]
  
  // Styling:
  // - Background: slate-900 (dark)
  // - Text: slate-300/400
  // - Active/hover: cyan-500 accent
  // - Smooth transition: width change animated (duration-300)
  // - Scrollable if form is long (overflow-y-auto)
  // - Border-right: slate-700
}
```

**Collapsed state detayı:**
```
┌──┐
│🔧│  ← Ekipman ikonu
│  │
│▶ │  ← Expand butonu
│  │
└──┘
w-14
```

**Expanded state:**
```
┌──────────────────────┐
│ 🔧 Kompresör         │
│    Vidalı (Screw)    │
│ ─────────────────── │
│ Giriş Sıcaklığı     │
│ [  25  ] °C          │
│                      │
│ Çıkış Sıcaklığı     │
│ [  85  ] °C          │
│                      │
│ Basınç               │
│ [  8   ] bar         │
│                      │
│ ...                  │
│                      │
│ [🔄 Tekrar Analiz]  │
│ [◀ Sidebar'ı Gizle] │
└──────────────────────┘
w-72 (288px)
```

### Dosya 3: `frontend/src/components/dashboard/MetricBar.jsx`

Analiz sonuçlarının özet metrikleri — her zaman görünür.

```jsx
/**
 * MetricBar — Compact horizontal metrics strip
 * 
 * Props:
 *   metrics: object — analiz sonuç metrikleri
 *   radarData: object — radar grade bilgisi  
 */
export default function MetricBar({ metrics, radarData }) {
  // 4-5 metric card yan yana (flex, gap-3)
  // Her card: ~120px, compact
  //   - Icon (küçük) + label (text-xs, muted)
  //   - Value (text-lg, font-mono, bold)
  //   - Color-coded (green/amber/red based on thresholds)
  
  // Metrics to show:
  // 1. Exergy Verimi: metrics.exergy_efficiency_pct → "%59.1"
  // 2. Exergy Yıkımı: metrics.exergy_destruction_kW → "15.1 kW"
  // 3. Kaçınılabilir Oran: metrics.avoidable_ratio_pct → "%36.7"
  // 4. Yıllık Kayıp: metrics.annual_exergy_loss_EUR → "€4,240"
  // 5. Genel Not: radarData.grade + radarData.overall_score → "B (72)"
  
  // Color thresholds for efficiency:
  //   >= 70%: emerald/green
  //   >= 50%: amber
  //   < 50%: red
  
  // Card styling:
  //   bg-white rounded-lg border border-slate-200 px-4 py-3
  //   shadow-sm hover:shadow-md transition
  //   Numbers: font-mono font-semibold text-lg
  //   Labels: text-xs text-slate-500 uppercase tracking-wider
  
  // Grade badge: colored circle with letter
  //   A=emerald B=cyan C=amber D=orange F=red
}
```

**Visual:**
```
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ Exergy   │ │ Yıkım    │ │ Kaçınıl. │ │ Yıllık   │ │ Genel    │
│ Verimi   │ │          │ │ Oran     │ │ Kayıp    │ │ Not      │
│ 59.1%    │ │ 15.1 kW  │ │ 36.7%    │ │ €4,240   │ │ B (72)   │
│ 🟡       │ │ 🔴       │ │ 🟡       │ │ 🔴       │ │ 🔵       │
└──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘
```

### Dosya 4: `frontend/src/components/dashboard/TabContainer.jsx`

Reusable tab component.

```jsx
/**
 * TabContainer — Reusable tab navigation + content panels
 * 
 * Props:
 *   tabs: [{ id, label, icon?, badge? }]
 *   activeTab: string (tab id)
 *   onTabChange: function(tabId)
 *   children: ReactNode (active tab content)
 */
export default function TabContainer({ tabs, activeTab, onTabChange, children }) {
  // Tab bar: flex, border-b border-slate-200
  // Each tab: px-4 py-3, cursor-pointer
  //   Active: text-cyan-600 border-b-2 border-cyan-600 font-semibold
  //   Inactive: text-slate-500 hover:text-slate-700
  // Badge: optional counter (e.g. chat message count)
  
  // Content area: pt-6, flex-1, overflow-y-auto
  // Render children (active tab content only)
}
```

### Dosya 5: `frontend/src/components/dashboard/OverviewTab.jsx`

Tab 1 — Genel Bakış: Radar + AV/UN + AI özet.

```jsx
/**
 * OverviewTab — Executive summary view
 * 
 * Props:
 *   result: object — full analysis result
 */
export default function OverviewTab({ result }) {
  // Layout: 2-column grid on lg, stack on mobile
  //
  // ┌─────────────────────┬─────────────────────┐
  // │                     │                     │
  // │   RadarBenchmark    │   AvoidableBar      │
  // │   (from result)     │   (from result)     │
  // │                     │                     │
  // │                     │   Grade Badge       │
  // │                     │   (large, centered) │
  // │                     │                     │
  // ├─────────────────────┴─────────────────────┤
  // │                                           │
  // │   AI Yorum Özeti (ilk 3 cümle)            │
  // │   [Devamını AI sekmesinde oku →]           │
  // │                                           │
  // └───────────────────────────────────────────┘
  
  // AI özeti: result.ai_interpretation.executive_summary veya
  //           result.ai_interpretation.analysis ilk 3 cümle
  
  // NOT: RadarBenchmark ve AvoidableBar component'larını
  // olduğu gibi kullan — sadece container/wrapper değişiyor
}
```

### Dosya 6: `frontend/src/components/dashboard/FlowTab.jsx`

Tab 2 — Akış Analizi: Sankey + Benchmark + detaylı metrikler.

```jsx
/**
 * FlowTab — Technical deep-dive view
 * 
 * Props:
 *   result: object — full analysis result
 */
export default function FlowTab({ result }) {
  // Layout: Stack (full width)
  //
  // ┌───────────────────────────────────────────┐
  // │                                           │
  // │   SankeyDiagram (full width)              │
  // │                                           │
  // ├───────────────────────────────────────────┤
  // │                                           │
  // │   BenchmarkChart (full width)             │
  // │                                           │
  // ├─────────────────────┬─────────────────────┤
  // │   Detaylı Metrikler │  Tavsiyeler         │
  // │   (all metrics      │  (recommendations   │
  // │    table format)    │   from result)      │
  // └─────────────────────┴─────────────────────┘
  
  // Detaylı metrikler tablosu:
  //   Her metrik: label | value | unit
  //   font-mono for values
  //   Alternating row backgrounds (stripe)
  
  // NOT: SankeyDiagram ve BenchmarkChart component'larını
  // olduğu gibi kullan
}
```

### Dosya 7: `frontend/src/components/dashboard/AITab.jsx`

Tab 3 — AI Danışman: Full AI yorum + Chat.

```jsx
/**
 * AITab — AI interpretation + interactive chat (combined)
 * 
 * Props:
 *   result: object — analysis result (includes ai_interpretation)
 *   equipmentType, subtype: string
 */
export default function AITab({ result, equipmentType, subtype }) {
  // Layout: 2-section vertical split
  //
  // ┌───────────────────────────────────────────┐
  // │   📊 AI Analiz Yorumu                      │
  // │                                           │
  // │   Full AIInterpretation content            │
  // │   (collapsible sections)                   │
  // │                                           │
  // ├───────────────────────────────────────────┤
  // │   💬 AI Danışmana Sor                      │
  // │                                           │
  // │   ChatPanel (always visible in this tab)  │
  // │   Height: min 400px                       │
  // │                                           │
  // └───────────────────────────────────────────┘
  
  // AIInterpretation: mevcut component olduğu gibi
  // ChatPanel: isVisible=true (bu tab'da her zaman açık)
  //   analysisData olarak result geçir
  
  // NOT: Önceki ayrı "AI Danışmana Sor" butonu kaldırılıyor
  //   Chat artık bu tab'ın parçası
}
```

### Dosya 8: `frontend/src/components/dashboard/ScenarioTab.jsx`

Tab 4 — Senaryo: What-If analizi.

```jsx
/**
 * ScenarioTab — What-If scenario analysis
 * 
 * Props:
 *   result: object — baseline analysis result
 *   equipmentType, subtype: string
 *   baselineParams: object — original parameters
 */
export default function ScenarioTab({ result, equipmentType, subtype, baselineParams }) {
  // Bu tab What-If akışını tamamen kendi içinde yönetir
  // State: scenarioParams, compareResult, isComparing
  
  // Layout:
  // ┌─────────────────────┬─────────────────────┐
  // │                     │                     │
  // │  ScenarioEditor     │  ComparisonPanel    │
  // │  (parameter sliders)│  (delta results)    │
  // │                     │                     │
  // │  [Karşılaştır]      │  veya               │
  // │  [Sıfırla]          │  "Parametreleri      │
  // │                     │   değiştirip         │
  // │                     │   Karşılaştır'a      │
  // │                     │   basın"             │
  // │                     │                     │
  // └─────────────────────┴─────────────────────┘
  
  // Eğer compareResult varsa:
  // └── ComparisonPanel full width (delta table + savings + radar overlay)
  
  // NOT: What-If state'i EquipmentAnalysis'tan bu component'a TAŞINIYOR
  //   Bu tab tamamen self-contained
}
```

---

## 📦 Mevcut Component Değişiklikleri

### Dosya 9: `frontend/src/pages/EquipmentAnalysis.jsx` — MAJOR RESTRUCTURE

Bu dosya tamamen yeniden yazılıyor. Mevcut mantık (analiz çağrısı, state management) korunuyor ama render kısmı tamamen değişiyor.

**Mevcut state (korulacak):**
```jsx
// Bunlar kalıyor:
const [equipmentType, setEquipmentType] = useState(...)
const [selectedSubtype, setSelectedSubtype] = useState(...)
const [result, setResult] = useState(null)
const [loading, setLoading] = useState(false)
// useAnalysis hook kullanılıyorsa o da kalıyor
```

**Kaldırılacak state:**
```jsx
// Bunlar kaldırılıyor (ScenarioTab kendi yönetiyor):
const [whatIfMode, setWhatIfMode] = useState(false)
const [scenarioParams, setScenarioParams] = useState(null)
const [compareResult, setCompareResult] = useState(null)
// chatOpen da kaldırılıyor (AITab her zaman gösteriyor)
const [chatOpen, setChatOpen] = useState(false)
```

**Yeni state:**
```jsx
const [activeTab, setActiveTab] = useState('overview')
const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
```

**Yeni render yapısı:**

```jsx
return (
  <DashboardLayout
    hasResult={!!result}
    sidebar={
      result ? (
        <ParameterSidebar
          equipmentType={equipmentType}
          subtype={selectedSubtype}
          isCollapsed={sidebarCollapsed}
          onToggleCollapse={() => setSidebarCollapsed(!sidebarCollapsed)}
          onReanalyze={handleAnalyze}
        >
          <ParameterForm ... />
        </ParameterSidebar>
      ) : null
    }
    metricBar={result ? <MetricBar metrics={result.metrics} radarData={result.radar_data} /> : null}
  >
    {!result ? (
      // Durum 1: Form centered
      <div className="max-w-2xl mx-auto">
        <EquipmentTypeSelector ... />
        <SubtypeSelector ... />
        <ParameterForm ... />
      </div>
    ) : (
      // Durum 2: Tab dashboard
      <TabContainer
        tabs={[
          { id: 'overview', label: 'Genel Bakış', icon: '📊' },
          { id: 'flow', label: 'Akış Analizi', icon: '🔄' },
          { id: 'ai', label: 'AI Danışman', icon: '🤖' },
          { id: 'scenario', label: 'Senaryo', icon: '⚡' },
        ]}
        activeTab={activeTab}
        onTabChange={setActiveTab}
      >
        {activeTab === 'overview' && <OverviewTab result={result} />}
        {activeTab === 'flow' && <FlowTab result={result} />}
        {activeTab === 'ai' && (
          <AITab
            result={result}
            equipmentType={equipmentType}
            subtype={selectedSubtype}
          />
        )}
        {activeTab === 'scenario' && (
          <ScenarioTab
            result={result}
            equipmentType={equipmentType}
            subtype={selectedSubtype}
            baselineParams={currentParams}
          />
        )}
      </TabContainer>
    )}
  </DashboardLayout>
);
```

### Dosya 10: `frontend/src/components/results/ResultsPanel.jsx` — DEPRECATED

Bu component artık kullanılmayacak. Tab component'ları doğrudan result prop'larını alıyor. ResultsPanel'ın yaptığı iş (component'ları sıralama) artık OverviewTab ve FlowTab tarafından yapılıyor.

**Seçenek A:** Dosyayı sil, import'ları temizle.
**Seçenek B:** Dosyayı koru ama kullanılmadığından emin ol.

→ **Seçenek A tercih edilir** (dead code olmasın).

### Dosya 11: `frontend/index.html` — Font Ekleme

```html
<head>
  ...
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
```

### Dosya 12: `frontend/src/index.css` — Global Stiller

```css
/* Mevcut stillere EKLE (üzerine yazma) */

body {
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
}

/* Monospace numbers for metrics */
.font-mono {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

/* Smooth transitions */
.sidebar-transition {
  transition: width 300ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Scrollbar styling for sidebar */
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #475569;
  border-radius: 2px;
}

/* Tab content area minimum height */
.tab-content {
  min-height: calc(100vh - 200px);
}
```

---

## 📐 Responsive Davranış

### Desktop (≥1024px / lg)
- Sidebar: 288px (w-72), collapsible to 56px (w-14)
- Content: flex-1 (kalan alan)
- MetricBar: 5 card horizontal
- Tab content: 2-column grids where specified

### Tablet (768-1023px / md)
- Sidebar: auto-collapse → 56px
- Content: full width minus sidebar
- MetricBar: 5 card (smaller, compact)
- Tab content: single column

### Mobile (<768px / sm)
- Sidebar: hidden (off-canvas), toggle butonla göster
- MetricBar: horizontal scroll veya 2x3 grid
- Tab content: single column, full width
- Tabs: scrollable horizontal

---

## 🔄 State Management Değişikliği

### EquipmentAnalysis.jsx — Önceki

```jsx
// State:
equipmentType, selectedSubtype, result, loading, error
whatIfMode, baselineParams, scenarioParams, compareResult, isComparing  // Brief 16
chatOpen  // Brief 17

// Render: alt alta her şey
<MetricsCards />
<AvoidableBar />
<RadarBenchmark />
<SankeyDiagram />
<BenchmarkChart />
<AIInterpretation />
{whatIfMode && <ScenarioEditor />}
{compareResult && <ComparisonPanel />}
{chatOpen && <ChatPanel />}
```

### EquipmentAnalysis.jsx — Sonrası

```jsx
// State:
equipmentType, selectedSubtype, result, loading, error
activeTab, sidebarCollapsed  // YENİ

// Render: structured dashboard
<DashboardLayout>
  <ParameterSidebar />    // Sidebar
  <MetricBar />           // Üst bar (her zaman)
  <TabContainer>          // Tab sistemi
    <OverviewTab />       // Radar + AV/UN + AI özet
    <FlowTab />           // Sankey + Benchmark + detay
    <AITab />             // AI yorum + Chat
    <ScenarioTab />       // What-If (kendi state'i var)
  </TabContainer>
</DashboardLayout>
```

**What-If state taşıma:** `whatIfMode`, `scenarioParams`, `compareResult`, `isComparing` state'leri **ScenarioTab** component'ına taşınıyor. ScenarioTab tamamen self-contained.

**Chat state taşıma:** `chatOpen` kaldırılıyor. ChatPanel, AITab içinde her zaman görünür.

---

## ⚠️ Mevcut Component'lara Dokunma Kuralları

Bu component'ların **iç mantığı DEĞİŞMEYECEK** — sadece wrapper/container değişiyor:

| Component | Ne Değişiyor | Ne DEĞİŞMİYOR |
|-----------|-------------|----------------|
| RadarBenchmark | Container genişliği | Plotly chart logic |
| SankeyDiagram | Container genişliği | Plotly chart logic |
| BenchmarkChart | Container genişliği | Chart logic |
| AvoidableBar | Container genişliği | Bar render logic |
| AIInterpretation | Container | AI content rendering |
| MetricsCards | **KULLANILMAYACAK** → MetricBar ile değişiyor | — |
| ParameterForm | Form dark theme support | Form fields, validation |
| ScenarioEditor | Container | Slider logic |
| ComparisonPanel | Container | Delta table, savings |
| ChatPanel | isVisible prop management | Chat logic, API calls |

**MetricsCards NOT:** Mevcut MetricsCards component'ı hâlâ FlowTab'daki detaylı metrikler tablosu olarak kullanılabilir. MetricBar yeni compact versiyonu.

### ParameterForm Dark Theme Uyumu

ParameterForm sidebar'da (dark bg) gösterilecek. Label'lar ve input'lar dark theme'de okunabilir olmalı:

```jsx
// ParameterForm'a className prop desteği ekle (eğer yoksa)
// Veya ParameterSidebar içinde wrapper div ile renk override:
<div className="[&_label]:text-slate-300 [&_input]:bg-slate-800 [&_input]:text-white [&_input]:border-slate-600">
  <ParameterForm ... />
</div>
```

Eğer bu Tailwind arbitrary selectors çalışmıyorsa, ParameterForm'a `darkMode` prop ekle ve conditional class'lar kullan.

---

## 📋 Uygulama Sırası

### Faz 1: Altyapı (index.html + CSS)
1. `frontend/index.html` — Google Fonts ekleme
2. `frontend/src/index.css` — Global stiller ekleme

### Faz 2: Dashboard Component'ları (yeni dosyalar)
3. `components/dashboard/TabContainer.jsx` — Reusable tab component
4. `components/dashboard/MetricBar.jsx` — Compact metric strip
5. `components/dashboard/ParameterSidebar.jsx` — Collapsible dark sidebar
6. `components/dashboard/DashboardLayout.jsx` — Ana layout wrapper

### Faz 3: Tab Content Component'ları (yeni dosyalar)
7. `components/dashboard/OverviewTab.jsx` — Radar + AV/UN + AI özet
8. `components/dashboard/FlowTab.jsx` — Sankey + Benchmark + detay
9. `components/dashboard/AITab.jsx` — AI yorum + Chat
10. `components/dashboard/ScenarioTab.jsx` — What-If (self-contained)

### Faz 4: Ana Sayfa Restructure
11. `pages/EquipmentAnalysis.jsx` — Tamamen yeniden yazılıyor
    - Mevcut dosyayı ÖNCE yedekle (cp ... ...backup)
    - Mevcut state management korunuyor
    - What-If state ScenarioTab'a taşınıyor
    - Chat state kaldırılıyor
    - Render tamamen yeni layout

### Faz 5: Temizlik
12. `components/results/ResultsPanel.jsx` — Kullanılmıyorsa sil/archive
13. Import'ları temizle (unused imports)

### Faz 6: Doğrulama
14. `cd frontend && npx vite build` — build başarılı
15. `cd .. && pytest tests/ -v` — 431 test geçiyor (backend değişmedi)

---

## ✅ Tamamlanma Kriterleri

- [ ] Google Fonts (Plus Jakarta Sans + JetBrains Mono) yükleniyor
- [ ] Analiz öncesi: temiz, centered form layout
- [ ] Analiz sonrası: sidebar + metric bar + tab layout
- [ ] Sidebar collapsible (genişlet/daralt animasyonlu)
- [ ] Sidebar dark theme — form okunabilir
- [ ] MetricBar: 5 compact metric card, renk kodlu
- [ ] Tab 1 (Genel Bakış): Radar + AV/UN + AI özeti yan yana
- [ ] Tab 2 (Akış Analizi): Sankey + Benchmark + detaylı tablo
- [ ] Tab 3 (AI Danışman): Full AI yorum + Chat paneli
- [ ] Tab 4 (Senaryo): ScenarioEditor + ComparisonPanel (self-contained)
- [ ] What-If state EquipmentAnalysis'tan ScenarioTab'a taşındı
- [ ] Chat artık buton ile açılmıyor — AI tab'ında her zaman mevcut
- [ ] Mevcut result component'larının iç mantığı bozulmadı
- [ ] Responsive: desktop + tablet + mobile temel uyum
- [ ] Frontend build başarılı — 0 error
- [ ] 431 test hâlâ geçiyor
- [ ] `git add -A && git commit && git push`

---

## 📊 Beklenen Sonuç

| Metrik | Önceki | Sonrası |
|--------|--------|---------|
| Sayfa yapısı | Alt alta scroll | Tab-based dashboard |
| İlk bakışta metrikler | Scroll gerekli | Her zaman görünür (MetricBar) |
| Parametre erişimi | Sayfanın üstünde | Collapsible sidebar |
| AI Chat erişimi | Buton tıkla → panel | Tab'da her zaman hazır |
| What-If erişimi | Buton tıkla → inline | Kendi tab'ı, self-contained |
| Tipografi | Generic system font | Plus Jakarta Sans + JetBrains Mono |
| Genel his | "Prototype" | "Engineering Tool" |
