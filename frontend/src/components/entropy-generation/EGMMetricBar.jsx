import { formatNumber } from '../../utils/formatters';

const MetricCard = ({ label, value, unit, color = 'text-gray-900' }) => (
  <div className="text-center px-3 py-2">
    <div className="text-xs text-gray-500">{label}</div>
    <div className={`text-sm font-mono font-semibold ${color}`}>
      {value} {unit && <span className="text-xs font-normal text-gray-400">{unit}</span>}
    </div>
  </div>
);

const MECHANISM_LABELS = {
  heat_transfer: 'Isı Transferi',
  pressure_drop: 'Basınç Düşüşü',
  mixing: 'Karışma',
};

const EGMMetricBar = ({ data }) => {
  if (!data) return null;

  return (
    <div className="flex flex-wrap items-center justify-center gap-1 divide-x divide-gray-200 bg-white rounded-lg border border-gray-200 px-2 py-1">
      <MetricCard
        label="S_gen Toplam"
        value={formatNumber(data.S_gen_total_kW_K, 4)}
        unit="kW/K"
        color="text-purple-700"
      />
      <MetricCard
        label="N_s Fabrika"
        value={formatNumber(data.N_s_factory, 3)}
        color={data.N_s_factory > 0.5 ? 'text-red-600' : 'text-emerald-700'}
      />
      <MetricCard
        label="Baskin"
        value={MECHANISM_LABELS[data.dominant_mechanism_factory] || data.dominant_mechanism_factory}
        color="text-slate-700"
      />
      <MetricCard
        label="DeltaT"
        value={formatNumber(data.heat_transfer_pct, 0)}
        unit="%"
        color="text-orange-600"
      />
      <MetricCard
        label="DeltaP"
        value={formatNumber(data.pressure_drop_pct, 0)}
        unit="%"
        color="text-blue-600"
      />
      <MetricCard
        label="Karışma"
        value={formatNumber(data.mixing_pct, 0)}
        unit="%"
        color="text-violet-600"
      />
      <MetricCard
        label="Ekipman"
        value={data.num_equipment || 0}
        color="text-slate-700"
      />
    </div>
  );
};

export default EGMMetricBar;
