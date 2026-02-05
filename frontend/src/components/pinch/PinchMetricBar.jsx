import { formatNumber, formatCurrency } from '../../utils/formatters';

const MetricCard = ({ label, value, unit, color = 'text-gray-900' }) => (
  <div className="text-center px-3 py-2">
    <div className="text-xs text-gray-500">{label}</div>
    <div className={`text-sm font-mono font-semibold ${color}`}>
      {value} {unit && <span className="text-xs font-normal text-gray-400">{unit}</span>}
    </div>
  </div>
);

const PinchMetricBar = ({ pinch }) => {
  if (!pinch) return null;

  return (
    <div className="flex flex-wrap items-center justify-center gap-1 divide-x divide-gray-200 bg-white rounded-lg border border-gray-200 px-2 py-1">
      <MetricCard
        label="Pinch Sicakligi"
        value={pinch.pinch_temperature_C != null ? formatNumber(pinch.pinch_temperature_C, 1) : '—'}
        unit="°C"
        color="text-purple-700"
      />
      <MetricCard
        label="QH min"
        value={formatNumber(pinch.QH_min_kW, 1)}
        unit="kW"
        color="text-red-600"
      />
      <MetricCard
        label="QC min"
        value={formatNumber(pinch.QC_min_kW, 1)}
        unit="kW"
        color="text-blue-600"
      />
      <MetricCard
        label="Tasarruf"
        value={formatNumber(pinch.savings_pct, 1)}
        unit="%"
        color={pinch.savings_pct > 10 ? 'text-green-600' : 'text-gray-700'}
      />
      <MetricCard
        label="Yillik Tasarruf"
        value={formatCurrency(pinch.annual_savings_EUR)}
        color="text-green-700"
      />
      <MetricCard
        label="Akis Sayisi"
        value={`${pinch.hot_stream_count}S + ${pinch.cold_stream_count}C`}
      />
    </div>
  );
};

export default PinchMetricBar;
