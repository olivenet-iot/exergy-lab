const GaugeChart = ({ value, maxValue = 100, color = '#2563eb' }) => {
  const clampedValue = Math.min(Math.max(value || 0, 0), maxValue);
  const ratio = clampedValue / maxValue;

  // Semi-circle arc: 180 degrees total
  const radius = 42;
  const cx = 60;
  const cy = 55;
  const circumference = Math.PI * radius; // half-circle length
  const offset = circumference * (1 - ratio);

  // Arc path for semi-circle (left to right, 180° to 0°)
  const arcPath = `M ${cx - radius} ${cy} A ${radius} ${radius} 0 0 1 ${cx + radius} ${cy}`;

  return (
    <svg viewBox="0 0 120 70" className="w-full h-full">
      {/* Background arc */}
      <path
        d={arcPath}
        fill="none"
        stroke="#e2e8f0"
        strokeWidth="10"
        strokeLinecap="round"
      />
      {/* Value arc */}
      <path
        d={arcPath}
        fill="none"
        stroke={color}
        strokeWidth="10"
        strokeLinecap="round"
        strokeDasharray={circumference}
        strokeDashoffset={offset}
        style={{
          transition: 'stroke-dashoffset 800ms cubic-bezier(0.4, 0, 0.2, 1)',
        }}
      />
      {/* Center text */}
      <text
        x={cx}
        y={cy - 6}
        textAnchor="middle"
        className="text-lg font-bold"
        style={{ fontSize: '18px', fontWeight: 700, fontFamily: 'Inter, system-ui, sans-serif' }}
        fill={color}
      >
        %{Math.round(clampedValue)}
      </text>
      <text
        x={cx}
        y={cy + 8}
        textAnchor="middle"
        style={{ fontSize: '8px', fill: '#94a3b8', fontFamily: 'Inter, system-ui, sans-serif' }}
      >
        Exergy Verimi
      </text>
    </svg>
  );
};

export default GaugeChart;
