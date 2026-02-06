import Plot from 'react-plotly.js';

const NODE_COLORS = [
  '#3b82f6', '#6366f1', '#10b981', '#f59e0b', '#ef4444',
  '#8b5cf6', '#ec4899', '#14b8a6', '#f97316',
];

const LINK_COLORS = [
  'rgba(59,130,246,0.4)', 'rgba(16,185,129,0.4)', 'rgba(245,158,11,0.4)',
  'rgba(239,68,68,0.4)', 'rgba(139,92,246,0.4)', 'rgba(236,72,153,0.4)',
  'rgba(20,184,166,0.4)', 'rgba(249,115,22,0.4)',
];

const SankeyDiagram = ({ data }) => {
  if (!data || !data.nodes || !data.links) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        Veri yükleniyor...
      </div>
    );
  }

  const plotData = [{
    type: 'sankey',
    orientation: 'h',
    arrangement: 'fixed',
    node: {
      pad: 20,
      thickness: 30,
      line: { color: 'white', width: 2 },
      label: data.nodes.map(n => n.name),
      color: data.nodes.map((_, i) => NODE_COLORS[i % NODE_COLORS.length]),
    },
    link: {
      source: data.links.map(l => l.source),
      target: data.links.map(l => l.target),
      value: data.links.map(l => l.value),
      color: data.links.map((_, i) => LINK_COLORS[i % LINK_COLORS.length]),
    },
  }];

  const layout = {
    font: { family: 'Inter, system-ui, sans-serif', size: 12 },
    margin: { l: 20, r: 120, t: 20, b: 20 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    dragmode: false,
  };

  const config = {
    displayModeBar: false,
    responsive: true,
    scrollZoom: false,
    staticPlot: false,
  };

  return (
    <div style={{ height: '400px', overflow: 'hidden' }}>
      <Plot
        data={plotData}
        layout={layout}
        config={config}
        useResizeHandler={true}
        style={{ width: '100%', height: '100%' }}
      />
    </div>
  );
};

export default SankeyDiagram;
