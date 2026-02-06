import { useState } from 'react';
import Plot from 'react-plotly.js';
import { ZoomIn, ZoomOut, RotateCcw } from 'lucide-react';

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
  const [zoomLevel, setZoomLevel] = useState(1);

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
    margin: { l: 20, r: 20, t: 20, b: 20 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    width: 600 * zoomLevel,
    height: 380 * zoomLevel,
    dragmode: false,
  };

  const config = {
    displayModeBar: false,
    responsive: true,
    scrollZoom: false,
  };

  const handleZoomIn = () => setZoomLevel(prev => Math.min(prev + 0.2, 2));
  const handleZoomOut = () => setZoomLevel(prev => Math.max(prev - 0.2, 0.6));
  const handleReset = () => setZoomLevel(1);

  return (
    <div className="relative" style={{ height: '400px', overflow: 'hidden' }}>
      {/* Zoom controls */}
      <div className="absolute top-2 right-2 z-10 flex items-center gap-1">
        <button
          onClick={handleZoomIn}
          className="p-1.5 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          title="Yakinlastir"
        >
          <ZoomIn className="w-4 h-4 text-gray-600" />
        </button>
        <button
          onClick={handleZoomOut}
          className="p-1.5 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          title="Uzaklastir"
        >
          <ZoomOut className="w-4 h-4 text-gray-600" />
        </button>
        <button
          onClick={handleReset}
          className="p-1.5 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          title="Sifirla"
        >
          <RotateCcw className="w-4 h-4 text-gray-600" />
        </button>
      </div>

      <div className="w-full h-full overflow-auto">
        <Plot
          data={plotData}
          layout={layout}
          config={config}
          style={{ width: '100%', height: '100%' }}
        />
      </div>
    </div>
  );
};

export default SankeyDiagram;
