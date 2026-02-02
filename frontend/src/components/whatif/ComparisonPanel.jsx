import RadarComparison from './RadarComparison';

const METRIC_LABELS = {
  exergy_efficiency_pct: 'Exergy Verimi (%)',
  exergy_input_kW: 'Exergy Girisi (kW)',
  exergy_destroyed_kW: 'Exergy Yikimi (kW)',
  exergy_destroyed_avoidable_kW: 'Onlenebilir Yikim (kW)',
  annual_loss_EUR: 'Yillik Kayip (EUR)',
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

  const isImproved = savings.efficiency_improvement_pct > 0 || savings.exergy_saved_kW > 0;

  // Flatten baseline/scenario for table
  const bFlat = { ...baseline.metrics, ...baseline.heat_recovery };
  const sFlat = { ...scenario.metrics, ...scenario.heat_recovery };

  return (
    <div className="space-y-6">
      {/* Summary card */}
      <div className={`rounded-xl border p-6 ${isImproved ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`}>
        <h3 className={`text-lg font-semibold mb-4 ${isImproved ? 'text-green-800' : 'text-red-800'}`}>
          Senaryo Karsilastirmasi
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="text-center">
            <div className={`text-2xl font-bold ${isImproved ? 'text-green-700' : 'text-red-700'}`}>
              {fmt(savings.exergy_saved_kW)} kW
            </div>
            <div className="text-sm text-gray-600 mt-1">Exergy Tasarrufu</div>
          </div>
          <div className="text-center">
            <div className={`text-2xl font-bold ${isImproved ? 'text-green-700' : 'text-red-700'}`}>
              {fmt(savings.annual_savings_kWh)} kWh/yil
            </div>
            <div className="text-sm text-gray-600 mt-1">Yillik Tasarruf</div>
          </div>
          <div className="text-center">
            <div className={`text-2xl font-bold ${isImproved ? 'text-green-700' : 'text-red-700'}`}>
              {fmt(savings.annual_savings_EUR)} EUR/yil
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
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Metrik Karsilastirmasi</h3>
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
                    <td className="py-2 px-4 text-right font-mono text-gray-600">{fmt(bVal)}</td>
                    <td className="py-2 px-4 text-right font-mono text-gray-900">{fmt(sVal)}</td>
                    <td className={`py-2 pl-4 text-right font-mono font-semibold ${
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
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Radar Karsilastirmasi</h3>
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
