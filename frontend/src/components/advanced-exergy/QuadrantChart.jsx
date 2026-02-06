import Plot from 'react-plotly.js';

const QuadrantChart = ({ chartData }) => {
  if (!chartData?.labels?.length) return null;

  const traces = [
    {
      name: 'AV-EN',
      y: chartData.labels,
      x: chartData.AV_EN,
      type: 'bar',
      orientation: 'h',
      marker: { color: '#22c55e' },
      hovertemplate: '%{y}: %{x:.1f} kW<extra>AV-EN</extra>',
    },
    {
      name: 'AV-EX',
      y: chartData.labels,
      x: chartData.AV_EX,
      type: 'bar',
      orientation: 'h',
      marker: { color: '#f59e0b' },
      hovertemplate: '%{y}: %{x:.1f} kW<extra>AV-EX</extra>',
    },
    {
      name: 'UN-EN',
      y: chartData.labels,
      x: chartData.UN_EN,
      type: 'bar',
      orientation: 'h',
      marker: { color: '#9ca3af' },
      hovertemplate: '%{y}: %{x:.1f} kW<extra>UN-EN</extra>',
    },
    {
      name: 'UN-EX',
      y: chartData.labels,
      x: chartData.UN_EX,
      type: 'bar',
      orientation: 'h',
      marker: { color: '#d1d5db' },
      hovertemplate: '%{y}: %{x:.1f} kW<extra>UN-EX</extra>',
    },
  ];

  const layout = {
    barmode: 'stack',
    xaxis: { title: 'Exergy Yıkımı (kW)', fixedrange: true },
    yaxis: { autorange: 'reversed', fixedrange: true },
    margin: { l: 120, r: 20, t: 10, b: 40 },
    height: Math.max(200, chartData.labels.length * 45 + 60),
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    legend: { orientation: 'h', y: -0.15, x: 0.5, xanchor: 'center' },
    font: { size: 11 },
  };

  return (
    <Plot
      data={traces}
      layout={layout}
      config={{ displayModeBar: false, responsive: true }}
      useResizeHandler
      style={{ width: '100%' }}
    />
  );
};

export default QuadrantChart;
