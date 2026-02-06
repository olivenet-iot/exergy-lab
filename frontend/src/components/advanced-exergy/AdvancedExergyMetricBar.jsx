import { formatNumber } from '../../utils/formatters';

const MetricCard = ({ label, value, unit, color = 'text-gray-900' }) => (
  <div className="text-center px-3 py-2">
    <div className="text-xs text-gray-500">{label}</div>
    <div className={`text-sm font-mono font-semibold ${color}`}>
      {value} {unit && <span className="text-xs font-normal text-gray-400">{unit}</span>}
    </div>
  </div>
);

const AdvancedExergyMetricBar = ({ data }) => {
  if (!data) return null;

  const enPct = data.endogenous_ratio != null
    ? formatNumber(data.endogenous_ratio * 100, 1)
    : '—';
  const exPct = data.endogenous_ratio != null
    ? formatNumber((1 - data.endogenous_ratio) * 100, 1)
    : '—';

  return (
    <div className="flex flex-wrap items-center justify-center gap-1 divide-x divide-gray-200 bg-white rounded-lg border border-gray-200 px-2 py-1">
      <MetricCard
        label="Endojen"
        value={enPct}
        unit="%"
        color="text-emerald-700"
      />
      <MetricCard
        label="Eksojen"
        value={exPct}
        unit="%"
        color="text-amber-700"
      />
      <MetricCard
        label="AV-EN"
        value={formatNumber(data.total_I_AV_EN_kW, 1)}
        unit="kW"
        color="text-green-600"
      />
      <MetricCard
        label="AV-EX"
        value={formatNumber(data.total_I_AV_EX_kW, 1)}
        unit="kW"
        color="text-amber-600"
      />
      <MetricCard
        label="Etkileşim"
        value={formatNumber(data.interaction_density * 100, 0)}
        unit="%"
        color={data.interaction_density > 0.5 ? 'text-red-600' : 'text-gray-700'}
      />
      <MetricCard
        label="Ekipman"
        value={data.equipment_results?.length || 0}
        color="text-slate-700"
      />
    </div>
  );
};

export default AdvancedExergyMetricBar;
