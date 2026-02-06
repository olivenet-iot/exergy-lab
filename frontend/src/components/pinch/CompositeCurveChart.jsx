import Plot from 'react-plotly.js';

const CompositeCurveChart = ({ data }) => {
  if (!data?.hot_curve || !data?.cold_curve) {
    return (
      <div className="h-64 flex items-center justify-center text-gray-400">
        Kompozit egri verisi yok
      </div>
    );
  }

  const traces = [
    {
      x: data.hot_curve.H_kW,
      y: data.hot_curve.T_C,
      name: 'Sicak Kompozit',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#ef4444', width: 2.5 },
      marker: { size: 4 },
    },
    {
      x: data.cold_curve.H_kW,
      y: data.cold_curve.T_C,
      name: 'Soguk Kompozit',
      type: 'scatter',
      mode: 'lines+markers',
      line: { color: '#3b82f6', width: 2.5 },
      marker: { size: 4 },
    },
  ];

  const layout = {
    xaxis: { title: 'Entalpi (kW)', zeroline: true },
    yaxis: { title: 'Sıcaklık (°C)', zeroline: true },
    legend: { orientation: 'h', y: -0.2 },
    margin: { l: 60, r: 20, t: 10, b: 60 },
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

export default CompositeCurveChart;
