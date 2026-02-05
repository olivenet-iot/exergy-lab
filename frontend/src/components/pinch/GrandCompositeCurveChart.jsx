import Plot from 'react-plotly.js';

const GrandCompositeCurveChart = ({ data }) => {
  if (!data?.H_kW || !data?.T_shifted_C || data.H_kW.length === 0) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        GCC verisi yok
      </div>
    );
  }

  const traces = [
    {
      x: data.H_kW,
      y: data.T_shifted_C,
      name: 'GCC',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#8b5cf6', width: 2.5 },
      marker: { size: 4 },
      fill: 'tozerox',
      fillcolor: 'rgba(139, 92, 246, 0.08)',
    },
  ];

  // Add pinch annotation
  const annotations = [];
  if (data.pinch_T_C != null) {
    annotations.push({
      x: 0,
      y: data.pinch_T_C,
      text: `Pinch: ${data.pinch_T_C}°C`,
      showarrow: true,
      arrowhead: 2,
      ax: 40,
      ay: -30,
      font: { size: 11, color: '#7c3aed' },
    });
  }

  const layout = {
    xaxis: { title: 'Net Isi Akisi (kW)', zeroline: true },
    yaxis: { title: 'Kaydirmali Sicaklik (°C)', zeroline: true },
    annotations,
    margin: { l: 60, r: 20, t: 10, b: 60 },
    showlegend: false,
    hovermode: 'closest',
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
  };

  return (
    <Plot
      data={traces}
      layout={layout}
      config={{ responsive: true, displayModeBar: false }}
      style={{ width: '100%', height: '320px' }}
    />
  );
};

export default GrandCompositeCurveChart;
