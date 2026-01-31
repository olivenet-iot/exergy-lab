import Plot from 'react-plotly.js';

const SankeyDiagram = ({ data }) => {
  if (!data || !data.nodes || !data.links) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        Veri yukleniyor...
      </div>
    );
  }

  const plotData = [{
    type: 'sankey',
    orientation: 'h',
    node: {
      pad: 20,
      thickness: 30,
      line: { color: 'white', width: 2 },
      label: data.nodes.map(n => n.name),
      color: ['#3b82f6', '#6366f1', '#10b981', '#f59e0b', '#ef4444'],
    },
    link: {
      source: data.links.map(l => l.source),
      target: data.links.map(l => l.target),
      value: data.links.map(l => l.value),
      color: ['rgba(59,130,246,0.4)', 'rgba(16,185,129,0.4)', 'rgba(245,158,11,0.4)', 'rgba(239,68,68,0.4)'],
    },
  }];

  const layout = {
    font: { family: 'Inter, system-ui, sans-serif', size: 12 },
    margin: { l: 20, r: 20, t: 20, b: 20 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
  };

  const config = {
    displayModeBar: false,
    responsive: true,
  };

  return (
    <div className="h-64 md:h-80">
      <Plot
        data={plotData}
        layout={layout}
        config={config}
        style={{ width: '100%', height: '100%' }}
      />
    </div>
  );
};

export default SankeyDiagram;
