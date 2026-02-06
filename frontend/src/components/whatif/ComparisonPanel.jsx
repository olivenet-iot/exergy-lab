import RadarComparison from './RadarComparison';

const METRIC_LABELS = {
  exergy_efficiency_pct: 'Exergy Verimi (%)',
  exergy_input_kW: 'Exergy Girişi (kW)',
  exergy_destroyed_kW: 'Exergy Yıkımı (kW)',
  exergy_destroyed_avoidable_kW: 'Önlenebilir Yıkım (kW)',
  annual_loss_EUR: 'Yıllık Kayıp (EUR)',
};

const DISPLAY_METRICS = Object.keys(METRIC_LABELS);

const fmt = (v) => {
  if (v == null) return '-';
  if (Math.abs(v) >= 1000) return v.toLocaleString('tr-TR', { maximumFractionDigits: 0 });
  return v.toLocaleString('tr-TR', { maximumFractionDigits: 2 });
};

const ComparisonPanel = ({ compareResult }) => {
  if (!compareResult) return null;

  const { baseline, scenario, comparison } = compareResult;
  const { savings, improved_metrics, degraded_metrics, summary_tr, delta } = comparison;

  const improved = improved_metrics?.length || 0;
  const degraded = degraded_metrics?.length || 0;
  const resultType = improved > degraded ? 'improved' : degraded > improved ? 'degraded' : 'mixed';

  const cardStyles = {
    improved: 'bg-emerald-50 border-emerald-200',
    degraded: 'bg-red-50 border-red-200',
    mixed: 'bg-amber-50 border-amber-200',
  };
  const textStyles = {
    improved: 'text-emerald-800',
    degraded: 'text-red-800',
    mixed: 'text-amber-800',
  };
  const valueStyles = {
    improved: 'text-emerald-700',
    degraded: 'text-red-700',
    mixed: 'text-amber-700',
  };

  // Flatten baseline/scenario for table
  const bFlat = { ...baseline.metrics, ...baseline.heat_recovery };
  const sFlat = { ...scenario.metrics, ...scenario.heat_recovery };

  return (
    <div className="space-y-6">
      {/* Summary card */}
      <div className={`rounded-xl border p-6 ${cardStyles[resultType]}`}>
        <h3 className={`text-lg font-semibold mb-4 ${textStyles[resultType]}`}>
          Senaryo Karşılaştırması
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="text-center">
            <div className={`text-2xl font-bold font-mono tabular-nums ${valueStyles[resultType]}`}>
              {fmt(savings.exergy_saved_kW)} kW
            </div>
            <div className="text-sm text-gray-600 mt-1">Exergy Tasarrufu</div>
          </div>
          <div className="text-center">
            <div className={`text-2xl font-bold font-mono tabular-nums ${valueStyles[resultType]}`}>
              {fmt(savings.annual_savings_kWh)} kWh/yıl
            </div>
            <div className="text-sm text-gray-600 mt-1">Yıllık Tasarruf</div>
          </div>
          <div className="text-center">
            <div className={`text-2xl font-bold font-mono tabular-nums ${valueStyles[resultType]}`}>
              {fmt(savings.annual_savings_EUR)} EUR/yıl
            </div>
            <div className="text-sm text-gray-600 mt-1">Maliyet Tasarrufu</div>
          </div>
        </div>
        {summary_tr && (
          <p className="mt-4 text-sm text-gray-700 text-center">{summary_tr}</p>
        )}
      </div>

      {/* Delta metrics table */}
      <div className="bg-white rounded-xl border border-gray-200 p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Metrik Karşılaştırması</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-gray-200">
                <th className="text-left py-2 pr-4 text-gray-600 font-medium">Metrik</th>
                <th className="text-right py-2 px-4 text-gray-600 font-medium">Mevcut</th>
                <th className="text-right py-2 px-4 text-gray-600 font-medium">Senaryo</th>
                <th className="text-right py-2 pl-4 text-gray-600 font-medium">Delta</th>
              </tr>
            </thead>
            <tbody>
              {DISPLAY_METRICS.map(metric => {
                const bVal = bFlat[metric];
                const sVal = sFlat[metric];
                const d = delta[metric];
                const isGood = improved_metrics.includes(metric);
                const isBad = degraded_metrics.includes(metric);

                return (
                  <tr key={metric} className="border-b border-gray-100">
                    <td className="py-2 pr-4 text-gray-800">{METRIC_LABELS[metric]}</td>
                    <td className="py-2 px-4 text-right font-mono tabular-nums text-gray-600">{fmt(bVal)}</td>
                    <td className="py-2 px-4 text-right font-mono tabular-nums text-gray-900">{fmt(sVal)}</td>
                    <td className={`py-2 pl-4 text-right font-mono tabular-nums font-semibold ${
                      isGood ? 'text-green-600' : isBad ? 'text-red-600' : 'text-gray-500'
                    }`}>
                      {d != null ? (d > 0 ? '+' : '') + fmt(d) : '-'}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Radar overlay */}
      {baseline.radar_data && scenario.radar_data && (
        <div className="bg-white rounded-xl border border-gray-200 p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Radar Karşılaştırması</h3>
          <RadarComparison
            baselineRadar={baseline.radar_data}
            scenarioRadar={scenario.radar_data}
          />
        </div>
      )}
    </div>
  );
};

export default ComparisonPanel;
