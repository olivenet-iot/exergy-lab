import { formatNumber } from '../../utils/formatters';
import Card from '../common/Card';
import MetricsCard from './MetricsCard';
import SankeyDiagram from './SankeyDiagram';
import BenchmarkChart from './BenchmarkChart';
import RadarBenchmark from './RadarBenchmark';

const EXTRA_METRICS = {
  // Heat exchanger
  lmtd_K:          { label: 'LMTD', unit: 'K' },
  effectiveness:   { label: 'Isıl Etkinlik', unit: '%', scale: 100 },
  bejan_number:    { label: 'Bejan Sayısı', unit: '' },
  heat_duty_kW:    { label: 'Isı Yükü', unit: 'kW' },
  // Steam turbine
  shaft_power_kW:  { label: 'Şaft Gücü', unit: 'kW' },
  electrical_power_kW: { label: 'Elektrik Gücü', unit: 'kW' },
  chp_exergy_efficiency_pct: { label: 'CHP Exergy Verimi', unit: '%' },
  // Dryer
  water_removed_kg_h: { label: 'Su Uzaklaştırma', unit: 'kg/h' },
  specific_energy_kJ_kg_water: { label: 'Spesifik Enerji', unit: 'kJ/kg-su' },
  // Shared
  thermal_efficiency_pct: { label: 'Termal Verim', unit: '%' },
};

const ResultsPanel = ({ data }) => {
  console.log('[ResultsPanel] rendering with data:', data);
  if (!data) return null;

  const { metrics = {}, heat_recovery = {}, benchmark = {}, sankey, radar_data } = data;

  const extraMetricEntries = Object.entries(EXTRA_METRICS).filter(
    ([key]) => metrics[key] != null
  );

  return (
    <div className="space-y-6">
      {/* Metric Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <MetricsCard
          title="Exergy Verimi"
          value={metrics?.exergy_efficiency_percent}
          unit="%"
          rating={benchmark?.rating}
          icon="gauge"
        />
        <MetricsCard
          title="Exergy Girisi"
          value={metrics?.exergy_input_kW}
          unit="kW"
          icon="zap"
        />
        <MetricsCard
          title="Faydali Exergy"
          value={metrics?.exergy_output_kW}
          unit="kW"
          icon="check-circle"
        />
        <MetricsCard
          title="Exergy Yikimi"
          value={metrics?.exergy_destroyed_kW}
          unit="kW"
          icon="x-circle"
        />
      </div>

      {/* Avoidable/Unavoidable Destruction Split */}
      {metrics.exergy_destroyed_avoidable_kW != null && (
        <Card title="Yıkım Ayrıştırması (AV/UN)">
          <div className="space-y-3">
            <div className="flex items-center justify-between text-sm mb-1">
              <span className="text-gray-600">Önlenebilir (AV)</span>
              <span className="font-mono font-semibold text-red-600">
                {formatNumber(metrics.exergy_destroyed_avoidable_kW)} kW
              </span>
            </div>
            <div className="flex items-center justify-between text-sm mb-1">
              <span className="text-gray-600">Önlenemez (UN)</span>
              <span className="font-mono font-semibold text-gray-500">
                {formatNumber(metrics.exergy_destroyed_unavoidable_kW)} kW
              </span>
            </div>
            {/* Stacked horizontal bar */}
            <div className="w-full h-6 rounded-full overflow-hidden flex bg-gray-200">
              {metrics.avoidable_ratio_pct > 0 && (
                <div
                  className="h-full bg-red-500 flex items-center justify-center text-xs text-white font-semibold"
                  style={{ width: `${Math.max(metrics.avoidable_ratio_pct, 8)}%` }}
                >
                  {formatNumber(metrics.avoidable_ratio_pct, 1)}%
                </div>
              )}
              {(100 - (metrics.avoidable_ratio_pct || 0)) > 0 && (
                <div
                  className="h-full bg-gray-400 flex items-center justify-center text-xs text-white font-semibold"
                  style={{ width: `${Math.max(100 - (metrics.avoidable_ratio_pct || 0), 8)}%` }}
                >
                  {formatNumber(100 - (metrics.avoidable_ratio_pct || 0), 1)}%
                </div>
              )}
            </div>
            <div className="flex items-center gap-4 text-xs text-gray-500 mt-1">
              <span className="flex items-center gap-1">
                <span className="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                Önlenebilir — iyileştirme potansiyeli
              </span>
              <span className="flex items-center gap-1">
                <span className="w-3 h-3 rounded-full bg-gray-400 inline-block"></span>
                Önlenemez — fiziksel sınır
              </span>
            </div>
          </div>
        </Card>
      )}

      {/* Equipment-specific Extra Metrics */}
      {extraMetricEntries.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold text-gray-900 mb-3">Ekipman Detay Metrikleri</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {extraMetricEntries.map(([key, meta]) => (
              <MetricsCard
                key={key}
                title={meta.label}
                value={meta.scale ? metrics[key] * meta.scale : metrics[key]}
                unit={meta.unit}
              />
            ))}
          </div>
        </div>
      )}

      {/* Radar Benchmark */}
      {radar_data && <RadarBenchmark radarData={radar_data} />}

      {/* Sankey Diagram */}
      <Card title="Exergy Akis Diyagrami">
        <SankeyDiagram data={sankey} />
      </Card>

      {/* Annual Impact & Benchmark */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Yillik Etki">
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Yillik Kayip</span>
              <span className="font-mono font-semibold text-red-600">
                {formatNumber(metrics?.annual_loss_kWh)} kWh
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Yillik Maliyet</span>
              <span className="font-mono font-semibold text-red-600">
                &euro;{formatNumber(metrics?.annual_cost_eur)}
              </span>
            </div>
            <hr />
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Isi Geri Kazanim Potansiyeli</span>
              <span className="font-mono font-semibold text-amber-600">
                {formatNumber(heat_recovery?.potential_kW)} kW
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-gray-600">Potansiyel Tasarruf</span>
              <span className="font-mono font-semibold text-green-600">
                &euro;{formatNumber(heat_recovery?.annual_savings_eur)}/yil
              </span>
            </div>
          </div>
        </Card>

        <Card title="Benchmark Karsilastirma">
          <BenchmarkChart
            efficiency={metrics?.exergy_efficiency_percent}
            rating={benchmark?.rating}
            percentile={benchmark?.percentile}
          />
          <p className="mt-4 text-sm text-gray-600">
            {benchmark?.comparison_text}
          </p>
        </Card>
      </div>
    </div>
  );
};

export default ResultsPanel;
