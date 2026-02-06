import Plot from 'react-plotly.js';

const GRADE_COLORS = {
  A: { r: 16, g: 185, b: 129 },   // green-500
  B: { r: 59, g: 130, b: 246 },   // blue-500
  C: { r: 245, g: 158, b: 11 },   // amber-500
  D: { r: 249, g: 115, b: 22 },   // orange-500
  F: { r: 239, g: 68, b: 68 },    // red-500
};

const GRADE_BG = {
  A: 'bg-green-100 text-green-800',
  B: 'bg-blue-100 text-blue-800',
  C: 'bg-amber-100 text-amber-800',
  D: 'bg-orange-100 text-orange-800',
  F: 'bg-red-100 text-red-800',
};

const AXIS_LABELS = {
  exergy_efficiency: 'Ekserji Verimi',
  improvement_status: 'İyileştirme',
  sector_ranking: 'Sektör Sırası',
  heat_recovery: 'Isı Geri Kaz.',
  destruction_ratio: 'Yıkım Oranı',
  cost_efficiency: 'Maliyet Verimi',
};

const RadarBenchmark = ({ radarData }) => {
  if (!radarData || !radarData.scores) return null;

  const { scores, overall_score, grade, grade_letter } = radarData;
  const color = GRADE_COLORS[grade_letter] || GRADE_COLORS.C;
  const badgeClass = GRADE_BG[grade_letter] || GRADE_BG.C;

  const axisKeys = Object.keys(AXIS_LABELS);
  const values = axisKeys.map(k => scores[k] ?? 0);
  // Close the polygon
  const closedValues = [...values, values[0]];
  const closedLabels = [...axisKeys.map(k => AXIS_LABELS[k]), AXIS_LABELS[axisKeys[0]]];

  const plotData = [{
    type: 'scatterpolar',
    r: closedValues,
    theta: closedLabels,
    fill: 'toself',
    fillcolor: `rgba(${color.r},${color.g},${color.b},0.15)`,
    line: { color: `rgb(${color.r},${color.g},${color.b})`, width: 2 },
    marker: { size: 6, color: `rgb(${color.r},${color.g},${color.b})` },
    name: 'Skor',
  }];

  const layout = {
    polar: {
      radialaxis: {
        visible: true,
        range: [0, 100],
        tickvals: [0, 25, 50, 75, 100],
        tickfont: { size: 10, color: '#9ca3af' },
        gridcolor: '#e5e7eb',
      },
      angularaxis: {
        tickfont: { size: 11, family: 'Inter, system-ui, sans-serif', color: '#374151' },
        gridcolor: '#e5e7eb',
      },
      bgcolor: 'transparent',
    },
    font: { family: 'Inter, system-ui, sans-serif' },
    margin: { l: 80, r: 80, t: 40, b: 40 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    showlegend: false,
  };

  const config = { displayModeBar: false, responsive: true };

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900">Benchmark Radar</h3>
        <div className="flex items-center gap-2">
          <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-bold ${badgeClass}`}>
            {grade_letter}
          </span>
          <span className="text-sm text-gray-500 font-mono tabular-nums">{overall_score}/100</span>
        </div>
      </div>

      {/* Chart */}
      <div className="h-80 md:h-96">
        <Plot
          data={plotData}
          layout={layout}
          config={config}
          style={{ width: '100%', height: '100%' }}
        />
      </div>

      {/* Score breakdown grid */}
      <div className="grid grid-cols-2 md:grid-cols-3 gap-3 mt-4">
        {axisKeys.map(key => {
          const val = scores[key] ?? 0;
          let dotColor = 'bg-red-500';
          if (val >= 85) dotColor = 'bg-green-500';
          else if (val >= 70) dotColor = 'bg-blue-500';
          else if (val >= 50) dotColor = 'bg-amber-500';
          else if (val >= 30) dotColor = 'bg-orange-500';

          return (
            <div key={key} className="flex items-center gap-2 text-sm">
              <span className={`w-2.5 h-2.5 rounded-full ${dotColor} flex-shrink-0`} />
              <span className="text-gray-600">{AXIS_LABELS[key]}</span>
              <span className="ml-auto font-mono font-semibold tabular-nums text-gray-900">{val}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default RadarBenchmark;
