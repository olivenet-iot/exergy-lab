const BenchmarkChart = ({ efficiency, rating, percentile }) => {
  const ranges = [
    { label: 'Dusuk', max: 30, color: '#ef4444' },
    { label: 'Ortalama', max: 45, color: '#f59e0b' },
    { label: 'Iyi', max: 55, color: '#3b82f6' },
    { label: 'Mukemmel', max: 70, color: '#10b981' },
  ];

  return (
    <div className="space-y-3">
      {/* Bar chart */}
      <div className="relative h-8 bg-gray-100 rounded-full overflow-hidden flex">
        {ranges.map((range, i) => {
          const prevMax = i > 0 ? ranges[i - 1].max : 0;
          const width = ((range.max - prevMax) / 70) * 100;
          return (
            <div
              key={range.label}
              className="h-full"
              style={{ width: `${width}%`, backgroundColor: range.color, opacity: 0.3 }}
            />
          );
        })}

        {/* Current value indicator */}
        <div
          className="absolute top-0 h-full w-1 bg-gray-900"
          style={{ left: `${(Math.min(efficiency ?? 0, 70) / 70) * 100}%` }}
        />
      </div>

      {/* Legend */}
      <div className="flex justify-between text-xs text-gray-500">
        <span>0%</span>
        <span>30%</span>
        <span>45%</span>
        <span>55%</span>
        <span>70%</span>
      </div>

      {/* Percentile */}
      {percentile != null && (
        <div className="text-center text-sm">
          <span className="text-gray-600">Sektor siralamasi: </span>
          <span className="font-semibold">Ilk %{100 - percentile}</span>
        </div>
      )}
    </div>
  );
};

export default BenchmarkChart;
