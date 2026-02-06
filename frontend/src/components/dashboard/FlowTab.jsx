import Card from '../common/Card';
import SankeyDiagram from '../results/SankeyDiagram';
import BenchmarkChart from '../results/BenchmarkChart';
import { formatNumber } from '../../utils/formatters';

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
  // Boiler-specific
  combustion_loss_kW: { label: 'Yanma Kaybı', unit: 'kW' },
  flue_gas_loss_kW: { label: 'Baca Gazı Kaybı', unit: 'kW' },
  // Chiller-specific
  cop: { label: 'COP', unit: '' },
  cop_carnot: { label: 'Carnot COP', unit: '' },
  kw_per_ton: { label: 'kW/ton', unit: 'kW/ton' },
  // Pump-specific
  hydraulic_power_kW: { label: 'Hidrolik Güç', unit: 'kW' },
  wire_to_water_efficiency_pct: { label: 'Wire-to-Water Verim', unit: '%' },
  throttle_loss_kW: { label: 'Kısma Kaybı', unit: 'kW' },
  // Exergoeconomic
  exergoeconomic_f_factor: { label: 'Exergoekonomik Faktör (f)', unit: '' },
  exergoeconomic_r_factor: { label: 'Goreli Maliyet Farki (r)', unit: '' },
  exergoeconomic_Z_dot_eur_h: { label: 'Yatırım Maliyet Akışı (Z)', unit: 'EUR/h' },
  exergoeconomic_C_dot_destruction_eur_h: { label: 'Yıkım Maliyet Akışı (C_D)', unit: 'EUR/h' },
  exergoeconomic_c_product_eur_kWh: { label: 'Urun Birim Maliyeti (c_P)', unit: 'EUR/kWh' },
  exergoeconomic_total_cost_rate_eur_h: { label: 'Toplam Maliyet Akışı (Z+C_D)', unit: 'EUR/h' },
};

const FlowTab = ({ result }) => {
  if (!result) return null;

  const { metrics = {}, heat_recovery = {}, benchmark = {}, sankey } = result;

  // Build detailed metrics table rows
  const coreMetrics = [
    { label: 'Exergy Verimi', value: metrics.exergy_efficiency_percent, unit: '%' },
    { label: 'Exergy Girişi', value: metrics.exergy_input_kW, unit: 'kW' },
    { label: 'Faydalı Exergy', value: metrics.exergy_output_kW, unit: 'kW' },
    { label: 'Exergy Yıkımı', value: metrics.exergy_destroyed_kW, unit: 'kW' },
  ];

  if (metrics.exergy_destroyed_avoidable_kW != null) {
    coreMetrics.push(
      { label: 'Önlenebilir Yıkım', value: metrics.exergy_destroyed_avoidable_kW, unit: 'kW' },
      { label: 'Önlenemez Yıkım', value: metrics.exergy_destroyed_unavoidable_kW, unit: 'kW' },
      { label: 'Önlenebilir Oran', value: metrics.avoidable_ratio_pct, unit: '%' },
    );
  }

  const extraRows = Object.entries(EXTRA_METRICS)
    .filter(([key]) => metrics[key] != null)
    .map(([key, meta]) => ({
      label: meta.label,
      value: meta.scale ? metrics[key] * meta.scale : metrics[key],
      unit: meta.unit,
    }));

  const allMetrics = [...coreMetrics, ...extraRows].filter((m) => m.value != null);

  return (
    <div className="space-y-6">
      {/* Sankey Diagram */}
      <Card title="Exergy Akış Diyagramı">
        <SankeyDiagram data={sankey} />
      </Card>

      {/* Benchmark */}
      <Card title="Benchmark Karşılaştırma">
        <BenchmarkChart
          efficiency={metrics.exergy_efficiency_percent}
          rating={benchmark.rating}
          percentile={benchmark.percentile}
        />
        {benchmark.comparison_text && (
          <p className="mt-4 text-sm text-gray-600">{benchmark.comparison_text}</p>
        )}
      </Card>

      {/* Detailed Metrics Table */}
      <Card title="Detaylı Metrikler">
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-gray-200">
                <th className="text-left py-2 pr-4 text-gray-600 font-medium">Metrik</th>
                <th className="text-right py-2 pl-4 text-gray-600 font-medium">Değer</th>
              </tr>
            </thead>
            <tbody>
              {allMetrics.map((row, i) => (
                <tr
                  key={row.label}
                  className={`border-b border-gray-100 ${i % 2 === 0 ? 'bg-slate-50' : ''}`}
                >
                  <td className="py-2 pr-4 text-gray-700">{row.label}</td>
                  <td className="py-2 pl-4 text-right font-mono font-semibold text-gray-900">
                    {formatNumber(row.value)} {row.unit}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>

      {/* Annual Impact */}
      <Card title="Yıllık Etki">
        <div className="space-y-4">
          <div className="flex justify-between items-center">
            <span className="text-gray-600">Yıllık Kayıp</span>
            <span className="font-mono font-semibold text-red-600">
              {formatNumber(metrics.annual_loss_kWh)} kWh
            </span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-gray-600">Yıllık Maliyet</span>
            <span className="font-mono font-semibold text-red-600">
              &euro;{formatNumber(metrics.annual_cost_eur)}
            </span>
          </div>
          <hr />
          <div className="flex justify-between items-center">
            <span className="text-gray-600">Isı Geri Kazanım Potansiyeli</span>
            <span className="font-mono font-semibold text-amber-600">
              {formatNumber(heat_recovery.potential_kW)} kW
            </span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-gray-600">Potansiyel Tasarruf</span>
            <span className="font-mono font-semibold text-green-600">
              &euro;{formatNumber(heat_recovery.annual_savings_eur)}/yıl
            </span>
          </div>
        </div>
      </Card>
    </div>
  );
};

export default FlowTab;
