import { useState, useMemo } from 'react';
import Plot from 'react-plotly.js';
import { formatNumber, formatPercentage, formatCurrency } from '../../utils/formatters';

/* ---------- Constants ---------- */
const LAYER_X = { 0: 0.01, 1: 0.20, 2: 0.45, 3: 0.75 };

const VIEW_MODES = [
  { id: 'exergy_flow', label: 'Exergy Akisi' },
  { id: 'destruction_focus', label: 'Yikim Analizi' },
  { id: 'cost_flow', label: 'Maliyet Akisi' },
];

/* ---------- View Mode Filter Pipeline ---------- */

function filterByViewMode(sankeyData, viewMode) {
  const rawNodes = sankeyData?.nodes || [];
  const rawLinks = sankeyData?.links || [];
  const summary = sankeyData?.summary || {};

  if (!rawNodes.length) return { nodes: [], links: [] };

  // Common: remove Layer 4 aggregation nodes and aggregation links
  let nodes = rawNodes.filter(n => n.layer !== 4);
  let links = rawLinks.filter(l => l.link_type !== 'aggregation');

  // Deep-copy nodes and links so mutations don't affect original data
  nodes = nodes.map(n => ({ ...n, metadata: { ...n.metadata } }));
  links = links.map(l => ({ ...l }));

  if (viewMode === 'exergy_flow') {
    return applyExergyFlowMode(nodes, links);
  } else if (viewMode === 'destruction_focus') {
    return applyDestructionFocusMode(nodes, links, summary);
  } else if (viewMode === 'cost_flow') {
    return applyCostFlowMode(nodes, links);
  }

  return { nodes, links };
}

function applyExergyFlowMode(nodes, links) {
  // For each equipment, merge dest_av_{id} + dest_un_{id} into single dest_combined_{id}
  const equipmentIds = nodes
    .filter(n => n.node_type === 'equipment')
    .map(n => n.id.replace('eq_', ''));

  for (const eqId of equipmentIds) {
    const avNode = nodes.find(n => n.id === `dest_av_${eqId}`);
    const unNode = nodes.find(n => n.id === `dest_un_${eqId}`);

    if (!avNode && !unNode) continue;

    const avValue = avNode?.value_kw || 0;
    const unValue = unNode?.value_kw || 0;
    const totalDest = avValue + unValue;

    if (totalDest <= 0) continue;

    // Get equipment name from the equipment node
    const eqNode = nodes.find(n => n.id === `eq_${eqId}`);
    const eqName = eqNode?.name || eqNode?.label || eqId;

    // Create merged destruction node
    const combinedNode = {
      id: `dest_combined_${eqId}`,
      name: `${eqName} Exergy Yikimi`,
      label: `${eqName} Exergy Yikimi`,
      layer: 3,
      node_type: 'destroyed_combined',
      color: '#ef4444',
      value_kw: totalDest,
      metadata: { name_en: `${eqName} Exergy Destruction` },
    };

    // Remove AV and UN nodes
    nodes = nodes.filter(n => n.id !== `dest_av_${eqId}` && n.id !== `dest_un_${eqId}`);

    // Replace AV/UN links targeting those nodes with a single combined link
    const avLinks = links.filter(
      l => l.target === `dest_av_${eqId}` && l.link_type === 'destruction_avoidable'
    );
    const unLinks = links.filter(
      l => l.target === `dest_un_${eqId}` && l.link_type === 'destruction_unavoidable'
    );

    // Remove old destruction links
    links = links.filter(
      l =>
        !(l.target === `dest_av_${eqId}` && l.link_type === 'destruction_avoidable') &&
        !(l.target === `dest_un_${eqId}` && l.link_type === 'destruction_unavoidable')
    );

    // Add combined link
    const sourceId = avLinks[0]?.source || unLinks[0]?.source;
    if (sourceId) {
      links.push({
        source: sourceId,
        target: `dest_combined_${eqId}`,
        value: totalDest,
        link_type: 'destruction_combined',
        color: 'rgba(239,68,68,0.40)',
        label: `${eqName} Exergy Yikimi`,
        is_opportunity: false,
      });
    }

    nodes.push(combinedNode);
  }

  // Keep integration opportunity links visible (purple) — they remain as-is
  return { nodes, links };
}

function applyDestructionFocusMode(nodes, links, summary) {
  const totalInput = summary.total_input_kW || 0;
  const threshold = totalInput * 0.02;

  // Remove integration opportunity links
  links = links.filter(l => !l.is_opportunity);

  // Remove links below 2% threshold
  if (threshold > 0) {
    links = links.filter(l => l.value >= threshold);
  }

  // Recolor links by type
  links = links.map(l => {
    if (l.link_type === 'destruction_avoidable') {
      return { ...l, color: 'rgba(239,68,68,0.65)' };
    } else if (l.link_type === 'destruction_unavoidable') {
      return { ...l, color: 'rgba(148,163,184,0.55)' };
    } else if (l.link_type === 'product_flow') {
      return { ...l, color: 'rgba(16,185,129,0.15)' };
    } else if (l.link_type === 'recovery_potential') {
      return { ...l, color: 'rgba(139,92,246,0.20)' };
    } else if (
      l.link_type === 'electricity_flow' ||
      l.link_type === 'fuel_flow' ||
      l.link_type === 'thermal_flow'
    ) {
      return { ...l, color: l.color.replace(/[\d.]+\)$/, '0.25)') };
    }
    return l;
  });

  // Remove orphan nodes (no remaining links)
  const linkedNodeIds = new Set();
  links.forEach(l => {
    linkedNodeIds.add(l.source);
    linkedNodeIds.add(l.target);
  });
  nodes = nodes.filter(n => linkedNodeIds.has(n.id));

  return { nodes, links };
}

function applyCostFlowMode(nodes, links) {
  // Build cost lookup from equipment node metadata
  const costLookup = {};
  nodes.forEach(n => {
    if (n.node_type === 'equipment') {
      const eqId = n.id;
      const cDot = n.metadata?.C_dot_destruction_eur_h || 0;
      const zDot = n.metadata?.Z_dot_eur_h || 0;
      costLookup[eqId] = { cDot, zDot, hasCost: cDot > 0 || zDot > 0 };
    }
  });

  // Gray out equipment nodes without cost data
  nodes = nodes.map(n => {
    if (n.node_type === 'equipment') {
      const cost = costLookup[n.id];
      if (!cost?.hasCost) {
        return { ...n, color: '#d1d5db' };
      }
    }
    return n;
  });

  // Transform link values to cost-based EUR/h
  links = links.map(l => {
    const targetCost = costLookup[l.target];
    const sourceCost = costLookup[l.source];

    // Source -> Equipment links: value = C_dot + Z_dot for target equipment
    if (
      targetCost &&
      (l.link_type === 'electricity_flow' ||
        l.link_type === 'fuel_flow' ||
        l.link_type === 'thermal_flow')
    ) {
      if (!targetCost.hasCost) {
        return { ...l, color: 'rgba(209,213,219,0.25)', label: `${l.label} (veri yok)` };
      }
      const costValue = targetCost.cDot + targetCost.zDot;
      return {
        ...l,
        value: costValue > 0 ? costValue : 0.01,
        label: `${l.label} ${formatNumber(costValue, 2)} EUR/h`,
      };
    }

    // Equipment -> Destruction links: proportional share of C_dot
    if (
      sourceCost &&
      (l.link_type === 'destruction_avoidable' || l.link_type === 'destruction_unavoidable')
    ) {
      if (!sourceCost.hasCost) {
        return { ...l, color: 'rgba(209,213,219,0.25)', label: `${l.label} (veri yok)` };
      }
      // Proportional share: link.value / total_destruction * C_dot
      const eqNode = nodes.find(n => n.id === l.source);
      const totalDest = eqNode?.metadata?.exergy_destroyed_kW || 1;
      const proportion = totalDest > 0 ? l.value / totalDest : 0;
      const costValue = sourceCost.cDot * proportion;
      return {
        ...l,
        value: costValue > 0 ? costValue : 0.01,
        label: `${l.label} ${formatNumber(costValue, 2)} EUR/h`,
      };
    }

    // Equipment -> Product links: value = Z_dot
    if (sourceCost && l.link_type === 'product_flow') {
      if (!sourceCost.hasCost) {
        return { ...l, color: 'rgba(209,213,219,0.25)', label: `${l.label} (veri yok)` };
      }
      const costValue = sourceCost.zDot;
      return {
        ...l,
        value: costValue > 0 ? costValue : 0.01,
        label: `${l.label} ${formatNumber(costValue, 2)} EUR/h`,
      };
    }

    return l;
  });

  return { nodes, links };
}

/* ---------- Plotly Trace Builder ---------- */

function buildPlotlyTrace(filteredData, viewMode) {
  const { nodes, links } = filteredData;

  if (!nodes || !nodes.length) {
    return {
      trace: {
        type: 'sankey', orientation: 'h',
        node: { label: [], color: [], x: [], y: [], pad: 30, thickness: 20 },
        link: { source: [], target: [], value: [], color: [], label: [] },
      },
    };
  }

  // Map string IDs to indices (rebuilt from filtered node list)
  const idToIdx = {};
  nodes.forEach((n, i) => { idToIdx[n.id] = i; });

  // Calculate total exergy for label visibility threshold
  const totalExergy = nodes
    .filter(n => n.node_type?.startsWith('source_'))
    .reduce((sum, n) => sum + (n.value_kw || 0), 0);
  const labelThreshold = totalExergy * 0.03;

  // Node arrays
  const nodeLabels = nodes.map(n => {
    if (n.value_kw < labelThreshold && n.layer >= 2) return '';
    return n.label || n.name || '';
  });
  const nodeColors = nodes.map(n => n.color || '#94a3b8');
  const nodeX = nodes.map(n => LAYER_X[n.layer] ?? 0.75);
  const nodeY = nodes.map(() => null);
  const nodeCustomdata = nodes.map(n => ({
    ...n.metadata,
    realLabel: n.label || n.name || '',
  }));

  // Link arrays
  const linkSources = [];
  const linkTargets = [];
  const linkValues = [];
  const linkColors = [];
  const linkLabels = [];

  links.forEach(link => {
    const srcIdx = idToIdx[link.source];
    const tgtIdx = idToIdx[link.target];
    if (srcIdx === undefined || tgtIdx === undefined) return;

    linkSources.push(srcIdx);
    linkTargets.push(tgtIdx);
    linkValues.push(link.value || 0.01);
    linkColors.push(link.color || 'rgba(148,163,184,0.3)');
    linkLabels.push(link.label || '');
  });

  // Mode-aware hovertemplates
  const isCostMode = viewMode === 'cost_flow';
  const nodeHover = isCostMode
    ? '<b>%{customdata.realLabel}</b><br>Deger: %{value:.2f} EUR/h<extra></extra>'
    : '<b>%{customdata.realLabel}</b><br>Deger: %{value:.1f} kW<extra></extra>';
  const linkHover = isCostMode
    ? '<b>%{label}</b><br>Akis: %{value:.2f} EUR/h<extra></extra>'
    : '<b>%{label}</b><br>Akis: %{value:.1f} kW<extra></extra>';

  const trace = {
    type: 'sankey',
    orientation: 'h',
    arrangement: 'snap',
    node: {
      label: nodeLabels,
      color: nodeColors,
      x: nodeX,
      y: nodeY,
      pad: 30,
      thickness: 20,
      line: { color: 'white', width: 1.5 },
      hovertemplate: nodeHover,
      customdata: nodeCustomdata,
    },
    link: {
      source: linkSources,
      target: linkTargets,
      value: linkValues,
      color: linkColors,
      label: linkLabels,
      hovertemplate: linkHover,
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

const SankeyLegend = ({ viewMode }) => {
  let items = [];
  let extras = null;

  if (viewMode === 'exergy_flow') {
    items = [
      { label: 'Elektrik', color: '#3b82f6' },
      { label: 'Yakit', color: '#f97316' },
      { label: 'Exergy Yikimi', color: '#ef4444' },
      { label: 'Faydali Cikti', color: '#22c55e' },
      { label: 'Geri Kazanim', color: '#8b5cf6' },
    ];
    extras = (
      <div className="flex items-center gap-1.5">
        <span className="w-6 border-t-2 border-dashed border-purple-400 inline-block" />
        <span className="text-xs text-gray-600">Entegrasyon Firsati</span>
      </div>
    );
  } else if (viewMode === 'destruction_focus') {
    items = [
      { label: 'Kacinilabilir Yikim', color: '#ef4444' },
      { label: 'Kacinilmaz Yikim', color: '#94a3b8' },
      { label: 'Faydali Cikti', color: 'rgba(16,185,129,0.4)' },
    ];
  } else if (viewMode === 'cost_flow') {
    items = [
      { label: 'Maliyet verisi olan', color: '#3b82f6' },
      { label: 'Maliyet verisi olmayan', color: '#d1d5db' },
      { label: 'C_D (Yikim maliyeti)', color: '#ef4444' },
      { label: 'Z (Yatirim maliyeti)', color: '#3b82f6' },
    ];
  }

  return (
    <div className="flex flex-wrap items-center gap-4 px-2 py-2">
      {items.map(item => (
        <div key={item.label} className="flex items-center gap-1.5">
          <span
            className="w-3 h-3 rounded-full inline-block"
            style={{ backgroundColor: item.color }}
          />
          <span className="text-xs text-gray-600">{item.label}</span>
        </div>
      ))}
      {extras}
    </div>
  );
};

const SankeySummaryBar = ({ summary, viewMode, nodes }) => {
  if (!summary) return null;

  let cards = [];
  let gridCols = 'md:grid-cols-5';

  if (viewMode === 'exergy_flow') {
    const totalIn = summary.total_input_kW || 0;
    cards = [
      {
        label: 'Toplam Giris',
        value: formatNumber(totalIn, 1),
        unit: 'kW',
        color: 'text-gray-900',
        bg: 'bg-gray-50',
        sub: null,
      },
      {
        label: 'Faydali Cikti',
        value: formatNumber(summary.useful_output_kW || 0, 1),
        unit: 'kW',
        color: 'text-green-600',
        bg: 'bg-green-50',
        sub: totalIn > 0 ? formatPercentage((summary.useful_output_kW || 0) / totalIn * 100) : null,
      },
      {
        label: 'Toplam Yikim',
        value: formatNumber(summary.irreversibility_kW || 0, 1),
        unit: 'kW',
        color: 'text-red-600',
        bg: 'bg-red-50',
        sub: totalIn > 0 ? formatPercentage((summary.irreversibility_kW || 0) / totalIn * 100) : null,
      },
      {
        label: 'Kacinilabilir Yikim',
        value: formatNumber(summary.total_destroyed_avoidable_kW || summary.exergy_destroyed_avoidable_kW || 0, 1),
        unit: 'kW',
        color: 'text-red-500',
        bg: 'bg-red-50/50',
        sub: totalIn > 0 ? formatPercentage((summary.total_destroyed_avoidable_kW || summary.exergy_destroyed_avoidable_kW || 0) / totalIn * 100) : null,
      },
      {
        label: 'Geri Kazanim',
        value: formatNumber(summary.recoverable_heat_kW || 0, 1),
        unit: 'kW',
        color: 'text-violet-600',
        bg: 'bg-violet-50',
        sub: totalIn > 0 ? formatPercentage((summary.recoverable_heat_kW || 0) / totalIn * 100) : null,
      },
    ];
  } else if (viewMode === 'destruction_focus') {
    gridCols = 'md:grid-cols-4';
    const avKW = summary.total_destroyed_avoidable_kW || summary.exergy_destroyed_avoidable_kW || 0;
    const unKW = summary.total_destroyed_unavoidable_kW || summary.exergy_destroyed_unavoidable_kW || 0;
    const totalDest = avKW + unKW;
    const avRatio = totalDest > 0 ? (avKW / totalDest * 100) : 0;
    const biggestName = summary.biggest_loss_equipment || '';
    const biggestKW = summary.biggest_loss_kW || 0;

    cards = [
      {
        label: 'Kacinilabilir Yikim',
        value: formatNumber(avKW, 1),
        unit: 'kW',
        color: 'text-red-600',
        bg: 'bg-red-50',
        sub: null,
      },
      {
        label: 'Kacinilmaz Yikim',
        value: formatNumber(unKW, 1),
        unit: 'kW',
        color: 'text-gray-600',
        bg: 'bg-gray-50',
        sub: null,
      },
      {
        label: 'Kacinilabilir Oran',
        value: formatPercentage(avRatio),
        unit: '',
        color: 'text-orange-600',
        bg: 'bg-orange-50',
        sub: null,
      },
      {
        label: 'En Buyuk Kayip',
        value: biggestName || '—',
        unit: biggestKW > 0 ? `${formatNumber(biggestKW, 1)} kW` : '',
        color: 'text-red-700',
        bg: 'bg-red-50/50',
        sub: null,
      },
    ];
  } else if (viewMode === 'cost_flow') {
    gridCols = 'md:grid-cols-3';

    // Sum cost data from equipment nodes
    const equipmentNodes = (nodes || []).filter(n => n.node_type === 'equipment');
    let totalCDot = 0;
    let totalZDot = 0;
    let hasCostData = false;

    equipmentNodes.forEach(n => {
      const cDot = n.metadata?.C_dot_destruction_eur_h || 0;
      const zDot = n.metadata?.Z_dot_eur_h || 0;
      if (cDot > 0 || zDot > 0) hasCostData = true;
      totalCDot += cDot;
      totalZDot += zDot;
    });

    if (!hasCostData) {
      return (
        <div className="mt-4 pt-4 border-t border-gray-100 text-center text-sm text-gray-400 py-4">
          Exergoekonomik veri bulunamadi
        </div>
      );
    }

    cards = [
      {
        label: 'Toplam C_D',
        value: formatNumber(totalCDot, 2),
        unit: 'EUR/h',
        color: 'text-red-600',
        bg: 'bg-red-50',
        sub: null,
      },
      {
        label: 'Toplam Z',
        value: formatNumber(totalZDot, 2),
        unit: 'EUR/h',
        color: 'text-blue-600',
        bg: 'bg-blue-50',
        sub: null,
      },
      {
        label: 'Toplam Maliyet Orani',
        value: formatNumber(totalCDot + totalZDot, 2),
        unit: 'EUR/h',
        color: 'text-gray-900',
        bg: 'bg-gray-50',
        sub: null,
      },
    ];
  }

  return (
    <div className={`grid grid-cols-2 ${gridCols} gap-3 mt-4 pt-4 border-t border-gray-100`}>
      {cards.map(card => (
        <div key={card.label} className={`text-center rounded-lg py-2 px-2 ${card.bg}`}>
          <div className="text-xs text-gray-500 mb-0.5">{card.label}</div>
          <div className={`text-sm font-mono font-semibold ${card.color}`}>
            {card.value}{card.unit ? ` ${card.unit}` : ''}
          </div>
          {card.sub && (
            <div className="text-xs text-gray-400 mt-0.5">{card.sub}</div>
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

  const filteredData = useMemo(
    () => filterByViewMode(sankeyData, viewMode),
    [sankeyData, viewMode]
  );

  const { trace } = useMemo(
    () => buildPlotlyTrace(filteredData, viewMode),
    [filteredData, viewMode]
  );

  if (!sankeyData || !sankeyData.nodes || !sankeyData.nodes.length) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        Sankey verisi bulunamadi
      </div>
    );
  }

  const equipmentCount = sankeyData.metadata?.equipment_count || 0;
  const chartHeight = Math.max(500, 120 * equipmentCount);

  const layout = {
    font: { family: 'Inter, system-ui, sans-serif', size: 11 },
    margin: { l: 10, r: 10, t: 10, b: 10 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    height: chartHeight,
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
          {equipmentCount} ekipman &middot; {viewMode === 'cost_flow' ? 'Maliyet gorunumu' : 'Exergy gorunumu'}
        </div>
        <ViewModeToggle viewMode={viewMode} onChange={setViewMode} />
      </div>

      {/* Sankey Chart */}
      <div className="bg-white rounded-lg border border-gray-100" style={{ height: `${chartHeight}px`, overflow: 'hidden' }}>
        <Plot
          data={[trace]}
          layout={layout}
          config={config}
          useResizeHandler={true}
          style={{ width: '100%', height: '100%' }}
        />
      </div>

      {/* Legend */}
      <SankeyLegend viewMode={viewMode} />

      {/* Summary Bar */}
      <SankeySummaryBar summary={sankeyData.summary} viewMode={viewMode} nodes={sankeyData.nodes} />
    </div>
  );
};

export default FactorySankeyV2;
