import Plot from 'react-plotly.js';

const BejanNumberChart = ({ chartData }) => {
  if (!chartData?.labels?.length) {
    return (
      <div className="text-center py-6 text-gray-500 text-sm">
        Bejan sayisi verisi yok
      </div>
    );
  }

  const data = [
    {
      type: 'bar',
      orientation: 'h',
      y: chartData.labels,
      x: chartData.N_s_values,
      marker: {
        color: chartData.colors,
      },
      text: chartData.grades.map((g, i) => `${g} (${chartData.N_s_values[i]})`),
      textposition: 'outside',
      hovertemplate: '%{y}: N_s = %{x:.4f} (%{text})<extra></extra>',
    },
  ];

  const layout = {
    xaxis: {
      title: 'Bejan Sayısı (N_s)',
      range: [0, 1.1],
      dtick: 0.2,
    },
    yaxis: {
      automargin: true,
    },
    margin: { l: 120, r: 60, t: 10, b: 40 },
    height: Math.max(200, chartData.labels.length * 40 + 60),
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    font: { size: 11 },
    shapes: [
      // Grade zone lines
      { type: 'line', x0: 0.15, x1: 0.15, y0: -0.5, y1: chartData.labels.length - 0.5, line: { color: '#d1d5db', width: 1, dash: 'dot' } },
      { type: 'line', x0: 0.30, x1: 0.30, y0: -0.5, y1: chartData.labels.length - 0.5, line: { color: '#d1d5db', width: 1, dash: 'dot' } },
      { type: 'line', x0: 0.50, x1: 0.50, y0: -0.5, y1: chartData.labels.length - 0.5, line: { color: '#d1d5db', width: 1, dash: 'dot' } },
      { type: 'line', x0: 0.70, x1: 0.70, y0: -0.5, y1: chartData.labels.length - 0.5, line: { color: '#d1d5db', width: 1, dash: 'dot' } },
    ],
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

export default BejanNumberChart;
