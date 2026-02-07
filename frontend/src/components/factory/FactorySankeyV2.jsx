import { useState, useMemo } from 'react';
import Plot from 'react-plotly.js';
import { formatNumber, formatPercentage } from '../../utils/formatters';

/* ---------- Constants ---------- */
const LAYER_X = { 0: 0.01, 1: 0.20, 2: 0.45, 3: 0.75, 4: 0.99 };

const VIEW_MODES = [
  { id: 'exergy_flow', label: 'Exergy Akisi' },
  { id: 'destruction_focus', label: 'Yikim Analizi' },
  { id: 'cost_flow', label: 'Maliyet Akisi' },
];

const LEGEND_ITEMS = [
  { label: 'Elektrik', color: '#3b82f6' },
  { label: 'Yakit', color: '#f97316' },
  { label: 'Faydali Cikti', color: '#22c55e' },
  { label: 'Kacinilabilir Yikim', color: '#ef4444' },
  { label: 'Kacinilmaz Yikim', color: '#94a3b8' },
  { label: 'Geri Kazanim', color: '#8b5cf6' },
];

/* ---------- Helpers ---------- */

function buildPlotlyTrace(sankeyData, viewMode) {
  const nodes = sankeyData?.nodes || [];
  const links = sankeyData?.links || [];

  if (!nodes.length) {
    return {
      trace: {
        type: 'sankey', orientation: 'h',
        node: { label: [], color: [], x: [], y: [], pad: 20, thickness: 25 },
        link: { source: [], target: [], value: [], color: [], label: [] },
      },
    };
  }

  // Map string IDs to indices
  const idToIdx = {};
  nodes.forEach((n, i) => { idToIdx[n.id] = i; });

  // Filter links based on view mode
  let filteredLinks = links;
  if (viewMode === 'destruction_focus') {
    // Hide integration opportunity links, keep all destruction
    filteredLinks = links.filter(l => !l.is_opportunity);
  } else if (viewMode === 'cost_flow') {
    // Show all links but we'll adjust values below
    filteredLinks = links;
  }

  // Node arrays
  const nodeLabels = nodes.map(n => n.label || n.name || '');
  const nodeColors = nodes.map(n => {
    if (viewMode === 'destruction_focus' && n.node_type === 'equipment') {
      // Emphasize by destruction amount
      return n.color || '#94a3b8';
    }
    if (viewMode === 'cost_flow' && n.node_type === 'equipment') {
      const hasCost = n.metadata?.C_dot_destruction_eur_h > 0 || n.metadata?.Z_dot_eur_h > 0;
      return hasCost ? n.color : '#d1d5db';
    }
    return n.color || '#94a3b8';
  });
  const nodeX = nodes.map(n => LAYER_X[n.layer] ?? 0.5);
  const nodeY = nodes.map(() => null); // Let Plotly handle Y for now

  // Link arrays
  const linkSources = [];
  const linkTargets = [];
  const linkValues = [];
  const linkColors = [];
  const linkLabels = [];

  filteredLinks.forEach(link => {
    const srcIdx = idToIdx[link.source];
    const tgtIdx = idToIdx[link.target];
    if (srcIdx === undefined || tgtIdx === undefined) return;

    linkSources.push(srcIdx);
    linkTargets.push(tgtIdx);
    linkValues.push(link.value || 0.01);

    // Color based on link type
    let color = link.color || 'rgba(148,163,184,0.3)';
    if (link.is_opportunity) {
      color = 'rgba(168,85,247,0.35)';
    }
    if (viewMode === 'destruction_focus') {
      if (link.link_type === 'destruction_avoidable') color = 'rgba(239,68,68,0.65)';
      else if (link.link_type === 'destruction_unavoidable') color = 'rgba(148,163,184,0.55)';
    }
    linkColors.push(color);
    linkLabels.push(link.label || '');
  });

  const trace = {
    type: 'sankey',
    orientation: 'h',
    arrangement: 'snap',
    node: {
      label: nodeLabels,
      color: nodeColors,
      x: nodeX,
      y: nodeY,
      pad: 20,
      thickness: 25,
      line: { color: 'white', width: 1.5 },
      hovertemplate: '<b>%{label}</b><br>Deger: %{value:.1f} kW<extra></extra>',
    },
    link: {
      source: linkSources,
      target: linkTargets,
      value: linkValues,
      color: linkColors,
      label: linkLabels,
      hovertemplate: '<b>%{label}</b><br>Akis: %{value:.1f} kW<extra></extra>',
    },
  };

  return { trace };
}

/* ---------- Sub-components ---------- */

const ViewModeToggle = ({ viewMode, onChange }) => (
  <div className="flex items-center gap-1 bg-gray-100 rounded-lg p-1">
    {VIEW_MODES.map(mode => (
      <button
        key={mode.id}
        onClick={() => onChange(mode.id)}
        className={`px-3 py-1.5 text-xs font-medium rounded-md transition-colors ${
          viewMode === mode.id
            ? 'bg-blue-600 text-white shadow-sm'
            : 'text-gray-600 hover:bg-gray-200'
        }`}
      >
        {mode.label}
      </button>
    ))}
  </div>
);

const SankeyLegend = () => (
  <div className="flex flex-wrap items-center gap-4 px-2 py-2">
    {LEGEND_ITEMS.map(item => (
      <div key={item.label} className="flex items-center gap-1.5">
        <span
          className="w-3 h-3 rounded-full inline-block"
          style={{ backgroundColor: item.color }}
        />
        <span className="text-xs text-gray-600">{item.label}</span>
      </div>
    ))}
    <div className="flex items-center gap-1.5">
      <span className="w-6 border-t-2 border-dashed border-purple-400 inline-block" />
      <span className="text-xs text-gray-600">Entegrasyon Firsati</span>
    </div>
  </div>
);

const SankeySummaryBar = ({ summary }) => {
  if (!summary) return null;

  const totalIn = summary.total_input_kW || 0;
  const cards = [
    {
      label: 'Toplam Giris',
      value: totalIn,
      color: 'text-gray-900',
      bg: 'bg-gray-50',
      pct: null,
    },
    {
      label: 'Faydali Cikti',
      value: summary.useful_output_kW || 0,
      color: 'text-green-600',
      bg: 'bg-green-50',
      pct: totalIn > 0 ? ((summary.useful_output_kW || 0) / totalIn * 100) : 0,
    },
    {
      label: 'Toplam Yikim',
      value: summary.irreversibility_kW || 0,
      color: 'text-red-600',
      bg: 'bg-red-50',
      pct: totalIn > 0 ? ((summary.irreversibility_kW || 0) / totalIn * 100) : 0,
    },
    {
      label: 'Kacinilabilir Yikim',
      value: summary.total_destroyed_avoidable_kW || summary.exergy_destroyed_avoidable_kW || 0,
      color: 'text-red-500',
      bg: 'bg-red-50/50',
      pct: totalIn > 0 ? ((summary.total_destroyed_avoidable_kW || summary.exergy_destroyed_avoidable_kW || 0) / totalIn * 100) : 0,
    },
    {
      label: 'Geri Kazanim',
      value: summary.recoverable_heat_kW || 0,
      color: 'text-violet-600',
      bg: 'bg-violet-50',
      pct: totalIn > 0 ? ((summary.recoverable_heat_kW || 0) / totalIn * 100) : 0,
    },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-5 gap-3 mt-4 pt-4 border-t border-gray-100">
      {cards.map(card => (
        <div key={card.label} className={`text-center rounded-lg py-2 px-2 ${card.bg}`}>
          <div className="text-xs text-gray-500 mb-0.5">{card.label}</div>
          <div className={`text-sm font-mono font-semibold ${card.color}`}>
            {formatNumber(card.value, 1)} kW
          </div>
          {card.pct !== null && (
            <div className="text-xs text-gray-400 mt-0.5">
              {formatPercentage(card.pct)}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

/* ---------- Main Component ---------- */

const FactorySankeyV2 = ({
  sankeyData,
  equipmentResults,
  aggregates,
  hotspots,
  integrationOpportunities,
  advancedExergy,
}) => {
  const [viewMode, setViewMode] = useState('exergy_flow');

  const { trace } = useMemo(
    () => buildPlotlyTrace(sankeyData, viewMode),
    [sankeyData, viewMode]
  );

  if (!sankeyData || !sankeyData.nodes || !sankeyData.nodes.length) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        Sankey verisi bulunamadi
      </div>
    );
  }

  const layout = {
    font: { family: 'Inter, system-ui, sans-serif', size: 11 },
    margin: { l: 10, r: 10, t: 10, b: 10 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    height: 700,
  };

  const config = {
    displayModeBar: false,
    responsive: true,
    scrollZoom: false,
    staticPlot: false,
  };

  return (
    <div>
      {/* Header: view mode toggle */}
      <div className="flex items-center justify-between mb-3">
        <div className="text-xs text-gray-500">
          {sankeyData.metadata?.equipment_count || 0} ekipman &middot; 5 katman
        </div>
        <ViewModeToggle viewMode={viewMode} onChange={setViewMode} />
      </div>

      {/* Sankey Chart */}
      <div className="bg-white rounded-lg border border-gray-100" style={{ height: '700px', overflow: 'hidden' }}>
        <Plot
          data={[trace]}
          layout={layout}
          config={config}
          useResizeHandler={true}
          style={{ width: '100%', height: '100%' }}
        />
      </div>

      {/* Legend */}
      <SankeyLegend />

      {/* Summary Bar */}
      <SankeySummaryBar summary={sankeyData.summary} />
    </div>
  );
};

export default FactorySankeyV2;
