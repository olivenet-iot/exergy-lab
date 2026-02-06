import Plot from 'react-plotly.js';

const EntropyDecompositionChart = ({ chartData }) => {
  if (!chartData?.labels?.length) {
    return (
      <div className="text-center py-6 text-gray-500 text-sm">
        Dekompozisyon verisi yok
      </div>
    );
  }

  const data = [
    {
      type: 'bar',
      orientation: 'h',
      name: 'Isı Transferi (DeltaT)',
      y: chartData.labels,
      x: chartData.heat_transfer,
      marker: { color: '#f97316' },
      hovertemplate: '%{y}: %{x:.6f} kW/K<extra>DeltaT</extra>',
    },
    {
      type: 'bar',
      orientation: 'h',
      name: 'Basınç Düşüşü (DeltaP)',
      y: chartData.labels,
      x: chartData.pressure_drop,
      marker: { color: '#3b82f6' },
      hovertemplate: '%{y}: %{x:.6f} kW/K<extra>DeltaP</extra>',
    },
    {
      type: 'bar',
      orientation: 'h',
      name: 'Karışma (Mix)',
      y: chartData.labels,
      x: chartData.mixing,
      marker: { color: '#8b5cf6' },
      hovertemplate: '%{y}: %{x:.6f} kW/K<extra>Mix</extra>',
    },
  ];

  const layout = {
    barmode: 'stack',
    xaxis: {
      title: 'Entropi Üretimi (kW/K)',
    },
    yaxis: {
      automargin: true,
    },
    margin: { l: 120, r: 20, t: 10, b: 40 },
    height: Math.max(200, chartData.labels.length * 40 + 60),
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    font: { size: 11 },
    legend: {
      orientation: 'h',
      yanchor: 'bottom',
      y: 1.02,
      xanchor: 'center',
      x: 0.5,
      font: { size: 10 },
    },
  };

  return (
    <Plot
      data={data}
      layout={layout}
      config={{ responsive: true, displayModeBar: false }}
      style={{ width: '100%' }}
    />
  );
};

export default EntropyDecompositionChart;
