import Plot from 'react-plotly.js';

const AXIS_LABELS = {
  exergy_efficiency: 'Exergy Verimi',
  improvement_status: 'İyileştirme',
  sector_ranking: 'Sektör Sırası',
  heat_recovery: 'Isı Geri Kaz.',
  destruction_ratio: 'Yıkım Oranı',
  cost_efficiency: 'Maliyet Ver.',
};

const RadarComparison = ({ baselineRadar, scenarioRadar }) => {
  if (!baselineRadar?.scores || !scenarioRadar?.scores) return null;

  const axisKeys = Object.keys(AXIS_LABELS);

  const bValues = axisKeys.map(k => baselineRadar.scores[k] ?? 0);
  const sValues = axisKeys.map(k => scenarioRadar.scores[k] ?? 0);

  const closedLabels = [...axisKeys.map(k => AXIS_LABELS[k]), AXIS_LABELS[axisKeys[0]]];
  const closedB = [...bValues, bValues[0]];
  const closedS = [...sValues, sValues[0]];

  const plotData = [
    {
      type: 'scatterpolar',
      r: closedB,
      theta: closedLabels,
      fill: 'toself',
      fillcolor: 'rgba(156,163,175,0.1)',
      line: { color: 'rgb(156,163,175)', width: 2, dash: 'dash' },
      marker: { size: 5, color: 'rgb(156,163,175)' },
      name: `Mevcut (${baselineRadar.overall_score}/100)`,
    },
    {
      type: 'scatterpolar',
      r: closedS,
      theta: closedLabels,
      fill: 'toself',
      fillcolor: 'rgba(59,130,246,0.15)',
      line: { color: 'rgb(59,130,246)', width: 2 },
      marker: { size: 6, color: 'rgb(59,130,246)' },
      name: `Senaryo (${scenarioRadar.overall_score}/100)`,
    },
  ];

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
    margin: { l: 60, r: 60, t: 30, b: 30 },
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    showlegend: true,
    legend: { x: 0, y: -0.15, orientation: 'h', font: { size: 11 } },
  };

  const config = { displayModeBar: false, responsive: true };

  return (
    <div className="h-72 md:h-80">
      <Plot
        data={plotData}
        layout={layout}
        config={config}
        style={{ width: '100%', height: '100%' }}
      />
    </div>
  );
};

export default RadarComparison;
