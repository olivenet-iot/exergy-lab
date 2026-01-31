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
      label: data.nodes.map(n => n.label),
      color: data.nodes.map(n => n.color),
    },
    link: {
      source: data.links.map(l => l.source),
      target: data.links.map(l => l.target),
      value: data.links.map(l => l.value),
      color: data.links.map(l => l.color),
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
